---
authors:
- Fayçal Drissi
- Xuchen Wu
- Sebastian Jaimungal
doc_id: arxiv:2512.19838v1
family_id: arxiv:2512.19838
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Equilibrium Liquidity and Risk Offsetting in Decentralised Markets
url_abs: http://arxiv.org/abs/2512.19838v1
url_html: https://arxiv.org/html/2512.19838v1
venue: arXiv q-fin
version: 1
year: 2025
---


Fayçal Drissi§
F. Drissi is with the Oxford-Man Institute, University of Oxford.
  
Xuchen Wu§
X. Wu is with the Department of Mathematics, University of Toronto.
  
Sebastian Jaimungal
S. Jaimungal is with the Department of Statistical Sciences, University of Toronto and the Oxford-Man Institute, University of Oxford.
  
§\S\ These authors contributed equally to this work.
  
Acknowledgments: We are grateful to Álvaro Cartea, Patrick Chang, and participants at the Research in Options 2025 conference for insightful discussions. SJ would like to acknowledge support from the Natural Sciences and Engineering Research Council of Canada through grant RGPIN-2024-04317.

(Latest [version](https://www.faycaldrissi.com/files/CEX_DEX.pdf).
  
This version: December 22, 2025.)

ABSTRACT

We develop an economic model of decentralised exchanges (DEXs) in which risk-averse liquidity providers (LPs) manage risk in a centralised exchange (CEX) based on preferences, information, and trading costs. Rational, risk-averse LPs anticipate the frictions associated with replication and manage risk primarily by reducing the reserves supplied to the DEX. Greater aversion reduces the equilibrium viability of liquidity provision, resulting in thinner markets and lower trading volumes. Greater uninformed demand supports deeper liquidity, whereas higher fundamental price volatility erodes it. Finally, while moderate anticipated price changes can improve LP performance, larger changes require more intensive trading in the CEX, generate higher replication costs, and induce LPs to reduce liquidity supply.

Decentralised exchanges (DEXs) organise trading on blockchains and have become a central component of decentralised finance.111Monthly trading volumes on DEXs reached $​420\mathdollar 420 billion in 2025; see cong2019blockchain; john2023smart; harvey2024evolution. Their widespread adoption hinges on whether liquidity provision remains viable when DEXs operate alongside competing centralised exchanges (CEXs), where prices form and liquidity providers (LPs) actively manage risk. Yet, the extant literature abstracts from key economic mechanisms when assessing LP returns and risks: it treats liquidity supply and market conditions as exogenous and focuses on perfect replication in a frictionless CEX. This paper studies the endogenous viability of DEX liquidity provision and the resulting market outcomes when risk-averse LPs anticipate (i) managing exposure in a CEX, accounting for risk preferences, private information, and trading costs, and (ii) strategic interactions with liquidity takers (LTs) whose trading volumes adjust to the level of liquidity supplied.

Our main finding is that a rational, risk-averse LP anticipates the frictions associated with risk offsetting in the CEX and manages risk exposure not only through replication, but primarily by reducing the level of reserves supplied to the DEX. The intuition is as follows. Both (i) net inventory exposure and (ii) trading costs incurred in the CEX generate disutility for a risk-averse LP. Disutility from inventory risk incentivises the LP to actively replicate her DEX position in the CEX, while disutility from CEX trading costs discourages such replication. The equilibrium outcome reflects the balance between these two forces: the ratio of risk aversion to trading costs determines the aggressiveness of replication in the CEX and, in turn, the level and profitability of liquidity provision in the DEX. We find that the viability of liquidity provision in DEXs deteriorates as the disutility from risk aversion dominates that from trading costs, because this leads the LP to trade more heavily on the CEX, and to supply less liquidity due to increasing anticipated trading costs.222A limiting case corresponds to perfect replication, which yields the lowest liquidity supply in our model. In contrast, the extant literature focuses on this case under the assumption of a frictionless CEX; see, for example, milionis2022automated; cartea2023predictable; bichuch2024defi. In some cases, there exists a threshold level of aversion beyond which liquidity provision in DEXs is no longer viable and markets shut down.

Our second finding is that access to private information about future prices does not systematically translate into more profitable liquidity provision. For moderate expected price innovations, the LP benefits from her informational advantage. However, when a risk-averse LP expects large price movements, she anticipates that replicating the position in the CEX will require more intensive trading and higher costs. Anticipating these frictions, the LP supplies less liquidity in the DEX, resulting in thinner markets, lower profitability of liquidity provision, and lower trading volumes of uninformed demand.

Our third finding is that the viability of liquidity provision is fundamentally driven by the elasticity and profitability of noise demand, and by the volatility of fundamentals. When noise demand increases or becomes less sensitive to trading costs, the LP anticipates higher fee revenue and is willing to bear greater risk. She does so by reducing the aggressiveness of her CEX trading and by increasing her liquidity supply on the DEX. In contrast, higher fundamental price volatility substantially increases expected adverse selection costs. The LP anticipates this by reducing liquidity supply and offsetting risk aggressively in the CEX to maintain expected outcomes consistent with her risk preferences.

Overall, our results show that the risks and rewards of liquidity provision are not summarised by a single measure from exogenous market conditions. Instead, they emerge endogenously and are determined by (i) the LP’s risk preferences, (ii) her private information, and (iii) market conditions, including CEX liquidity depth, fundamental volatility, and the elasticity of uninformed liquidity demand.

Our theoretical contribution is to propose an economic model that endogenises the risk-reward trade-off of liquidity provision in DEXs and the trading volumes of liquidity takers, when the liquidity provider has access to a CEX where inventory risk can be offset at a cost. In our model, there are three types of agents: a representative liquidity provider (LP), noise liquidity takers (noise LTs), and arbitrageurs. These agents interact in three stages. In stage one, the LP chooses the amount of reserves to deposit in the DEX. In stage two, the LP determines a dynamic strategy to (partially) offset exposure in the CEX, taking into account costs, risk preferences, and private price information. In stage three, trading begins: noise LTs with elastic demand arrive (unpredictably) at the DEX and optimise their trading volumes, arbitrageurs align the DEX’s marginal price with its fundamental value, and the LP executes her strategy. Our model assumes that the DEX operates as a secondary market and does not influence equilibrium outcomes in the CEX. The model is solved recursively, by dynamic programming.

In stage three, noise LTs arrive in the DEX at a known intensity and take the current reserves as given to determine their optimal trading volumes. Specifically, they balance the trading costs implied by the LP’s reserves in the DEX against their private utility from holding the asset. Trading costs directly depend on the liquidity reserves deposited by the LP. Specifically, in DEXs, liquidity providers deposit capital into a pool that liquidity takers use to execute trades in exchange for a fee. The DEX functions as an algorithmic market maker whose price and liquidity dynamics are determined by the pricing rules encoded in the DEX’s smart contract,333A smart contract is a publicly accessible and immutable program running on the blockchain that defines the rules of interaction with the pool for both liquidity providers and liquidity takers. the amount of capital in the pool, and the trading fee.

In stage two, the LP determines her optimal CEX risk offsetting strategy for an arbitrary level of liquidity supply. The strategy explicitly accounts for CEX trading costs, investment horizon, net exposure risk aversion, and private information. We employ variational methods to characterise and solve the optimal strategy in the setting of a DEX with an arbitrary convex bonding curve and when the LP’s trading activity generates both permanent and transient market impact. We show that the system of forward–backward stochastic differential equations (FBSDEs) characterizing the LP’s strategy reduces to a differential Riccati equation (DRE), whose solution exists, is unique, and can be efficiently computed. In the absence of transient impact, we further derive a closed-form solution. The optimal risk-offsetting strategy comprises two components: (i) a *tracking component*, which balances net exposure aversion and CEX trading costs to partially replicate changes in the DEX’s liquidity position, and (ii) a *speculative component*, which adjusts the LP’s net exposure to exploit private information.

In stage one, the LP anticipates that (i) noise LTs are sensitive to the trading costs implied by the level of DEX reserves, (ii) part of her risk will be offset in the CEX, and (iii) arbitrageurs will align the DEX price to its fundamental value. Thus, the LP sets the optimal level of DEX reserves by trading off anticipated losses to arbitrageurs against (i) anticipated fee revenue from the elastic demand of noise LTs and (ii) the effects of her activity in the CEX. We characterise the LP’s optimisation problem and show it admits a solution for DEXs with arbitrary convex bonding curves.

Finally, in the case of constant product markets such as Uniswap, and in the absence of transient price impact in the CEX, we derive analytical formulae for the equilibrium trading volumes, liquidity supply, and the returns and risks of liquidity provision.

Literature review. Numerous works explore the microstructure of DEXs.
angeris2021replicating2; capponi2023decentralized; cartea2024decentralized show that DEXs generate losses for liquidity suppliers.
jaimungal2023optimal; cartea2025decentralised study liquidity taking in DEXs. lehar2021decentralized describe competition between DEXs and order books.
hasbrouck2022need show that higher DEX fees increase liquidity supply and reduce trading costs. bichuch2022axioms formalise the axioms governing DEX design.
klein2023price examine the role of informed liquidity supply in price discovery. park2023conceptual discuss the different types of trading costs in DEXs.
malinova2024learning investigate the potential of DEXs to organise equity trading. cartea2024strategic; he2024optimal propose DEX designs aimed at mitigating losses for liquidity suppliers.
Recent works also examine the optimal behavior of liquidity providers and the optimal dynamic fee structure of DEXs assuming exogenous levels of reserves; see bergault2025optimal; baggiani2025optimal. In particular, campbell2025optimal also discusses the costs of replication in the CEX. Finally, capponi2025longer; he2025arbitrage characterise the microstructure of DEXs by incorporating the consensus protocols of blockchains.

Our work is related to the literature on algorithmic trading using stochastic control tools; see cartea2015algorithmic, gueant2016financial, and donnelly2022optimal.
We incorporate trading signals, first introduced in cartea2016incorporating, where they were interpreted as order-flow indicators.444A specific application is investigated in lehalle2019incorporating. Latent models with trading signals were studied in casgrain2019trading, while a variational approach to solving trading problems involving multiple agents with heterogeneous beliefs was proposed in casgrain2018mean; casgrain2020mean; wu2024broker.
Finally, inventory targeting in optimal trading was analysed in cartea2016closed and bank2017hedging.

The remainder of this paper proceeds as follows. Section [II](https://arxiv.org/html/2512.19838v1#S2 "II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") describes the economic trade-offs faced by liquidity providers in DEXs and introduces the model.
Section [III](https://arxiv.org/html/2512.19838v1#S3 "III Stage three: trading volumes ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") solves for the trading volumes of noise LTs in stage three.
Section [IV](https://arxiv.org/html/2512.19838v1#S4 "IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") analyses the replication problem of the LP in stage two.
Section [V](https://arxiv.org/html/2512.19838v1#S5 "V Stage one: liquidity supply ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") derives the optimal liquidity supply in stage one.
Section [VI](https://arxiv.org/html/2512.19838v1#S6 "VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") examines the equilibrium reward–risk trade-off in the case of a constant product market such as Uniswap and presents numerical experiments.

## I TO-DOs

* •

  emphasize a bit more in intro that liquidity demand incentivises increasing the supply

## II General features of the model

DEXs operate with liquidity pooling, where available reserves are aggregated in a common pool, and algorithmic rules, hardcoded in smart contracts running on the blockchain, determine execution prices for liquidity takers (LTs) and revenue for liquidity providers (LPs). This section describes the mechanics of price and liquidity in DEXs, and introduces the general features of our model.

Consider a DEX for a pair of assets {X,Y}\{X,Y\}, where XX is a reference asset used by agents to value their wealth, and YY is a risky asset. Let a representative LP deposit initial reserves X0X\_{0} and Y0Y\_{0} of assets XX and YY, respectively, into the DEX pool at time 0. The LP then remains passive until a terminal investment horizon TT, i.e., she neither adds to, nor withdraws from, the reserves in the pool. As trading unfolds over a time window [0,T][0,T], where T>0,T>0, the available reserves in the pool serve as counterparty to LT trades. Consequently, the reserves in both assets XX and YY in the DEX evolve dynamically. Let (Xt)t≥0(X\_{t})\_{t\geq 0} and (Yt)t≥0(Y\_{t})\_{t\geq 0} denote the processes describing the evolution of reserves in assets XX and YY, respectively.

DEX price and liquidity. The mechanics of DEXs that determine price and liquidity are defined by iso-liquidity curves. Once the LP establishes the pool, and provided she remains passive, the reserves satisfy, for all t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(Xt,Yt)=κ2=f​(X0,Y0),f(X\_{t},Y\_{t})=\kappa^{2}=f(X\_{0},Y\_{0})\,, |  | (1) |

where κ>0\kappa>0 denotes the *liquidity depth* of the DEX, and
f:(0,∞)2→(0,∞)f:(0,\infty)^{2}\to(0,\infty) is the DEX’s *trading function*.
The trading function ff defines, in ([1](https://arxiv.org/html/2512.19838v1#S2.E1 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), all combinations of reserves in assets XX and YY that leave the LP indifferent, i.e., that do not change the liquidity depth κ\kappa. For the analysis that follows, we make the following assumptions.

###### Assumption 1:

1. (i)

   f∈C3​((0,∞)2)f\in C^{3}((0,\infty)^{2}) and has strictly positive partial derivatives.
2. (ii)

   For each y>0y>0, f​(⋅,y):(0,∞)→(0,∞)f(\cdot,y):(0,\infty)\to(0,\infty) is surjective. Thus, for each κ>0\kappa>0, the level set
   f​(x,y)=κ2f(x,y)=\kappa^{2} admits a unique solution
   x=φ​(y,κ).x=\varphi(y,\kappa)\,.
3. (iii)

   R:=∂2f∂1fR:=\tfrac{\partial\_{2}f}{\partial\_{1}f} satisfies
   R​∂1R−∂2R>0R\,\partial\_{1}R-\partial\_{2}R>0 everywhere, and is decreasing in κ.\kappa.
4. (iv)

   ∂1φ\partial\_{1}\varphi satisfies the limits limy↓0∂1φ​(y,κ)=−∞\lim\_{y\downarrow 0}\partial\_{1}\varphi(y,\kappa)=-\infty\quad and limy↑∞∂1φ​(y,κ)=0.\quad\lim\_{y\uparrow\infty}\partial\_{1}\varphi(y,\kappa)=0\,.

Assumption [1(i)](https://arxiv.org/html/2512.19838v1#S2.I1.i1 "item 1(i) ‣ Assumption 1: ‣ II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") implies that the liquidity depth κ\kappa increases in the reserves held in the DEX. We refer to φ\varphi in Assumption [1(ii)](https://arxiv.org/html/2512.19838v1#S2.I1.i2 "item 1(ii) ‣ Assumption 1: ‣ II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") as the *level function*.
By the implicit function theorem, and since ff has strictly positive partial derivatives by Assumption [1(i)](https://arxiv.org/html/2512.19838v1#S2.I1.i1 "item 1(i) ‣ Assumption 1: ‣ II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"), the mapping φ\varphi is C3C^{3} on (0,∞)2(0,\infty)^{2}. Using ([1](https://arxiv.org/html/2512.19838v1#S2.E1 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), and assuming no additional liquidity is supplied nor withdrawn, we express the reserve in the reference asset XX as a function of the reserves in the risky asset YY and the liquidity depth κ\kappa as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=φ​(Yt,κ).X\_{t}=\varphi(Y\_{t},\kappa). |  | (2) |

In DEXs, if an LT wishes to buy a quantity Δ​y\Delta y of the risky asset,
the indifference condition ([1](https://arxiv.org/html/2512.19838v1#S2.E1 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), or equivalently ([2](https://arxiv.org/html/2512.19838v1#S2.E2 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), determines the amount Δ​x\Delta x of the reference asset that she must pay to the DEX, which satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt+Δ​x=φ​(Yt−Δ​y,κ).X\_{t}+\Delta x=\varphi(Y\_{t}-\Delta y,\kappa). |  | (3) |

Thus, the execution price obtained by the LT per unit of the risky asset is given by555The execution price here refers to the amount of the reference asset that the LP pays per unit of the risky asset purchased.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​xΔ​y=φ​(Yt−Δ​y,κ)−XtΔ​y=φ​(Yt−Δ​y,κ)−φ​(Yt,κ)Δ​y.\frac{\Delta x}{\Delta y}=\frac{\varphi(Y\_{t}-\Delta y,\kappa)-X\_{t}}{\Delta y}=\frac{\varphi(Y\_{t}-\Delta y,\kappa)-\varphi(Y\_{t},\kappa)}{\Delta y}. |  | (4) |

Similarly, if an LT wishes to sell a quantity Δ​y\Delta y of the risky asset,
the execution price is666The execution price here refers to the amount of the reference asset that the LP receives per unit of the risky asset sold.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​xΔ​y=φ​(Yt,κ)−φ​(Yt+Δ​y,κ)Δ​y.\frac{\Delta x}{\Delta y}=\frac{\varphi(Y\_{t},\kappa)-\varphi(Y\_{t}+\Delta y,\kappa)}{\Delta y}. |  | (5) |

Note that as the traded quantity tends to zero, the execution prices to buy and sell the risky asset in ([4](https://arxiv.org/html/2512.19838v1#S2.E4 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"))–([5](https://arxiv.org/html/2512.19838v1#S2.E5 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) both converge to the execution price for an infinitesimal quantity −∂1φ​(Yt,κ)-\partial\_{1}\varphi(Y\_{t},\kappa), which we refer to as the marginal price.
The marginal price serves as a reference price analogous to the midprice in limit order books. In particular, the difference between the marginal price and the execution prices in ([4](https://arxiv.org/html/2512.19838v1#S2.E4 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"))–([5](https://arxiv.org/html/2512.19838v1#S2.E5 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) quantifies the trading costs associated with executing a given quantity in the DEX. These trading costs are expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(Yt−Δ​y,κ)−φ​(Yt,κ)Δ​y+∂1φ​(Yt,κ)andφ​(Yt,κ)−φ​(Yt+Δ​y,κ)Δ​y+∂1φ​(Yt,κ),\frac{\varphi(Y\_{t}-\Delta y,\kappa)-\varphi(Y\_{t},\kappa)}{\Delta y}+\partial\_{1}\varphi(Y\_{t},\kappa)\qquad\text{and}\qquad\frac{\varphi(Y\_{t},\kappa)-\varphi(Y\_{t}+\Delta y,\kappa)}{\Delta y}+\partial\_{1}\varphi(Y\_{t},\kappa), |  | (6) |

and they are positive only when φ\varphi is convex in the reserves YtY\_{t}, which is ensured by Assumption [1(iii)](https://arxiv.org/html/2512.19838v1#S2.I1.i3 "item 1(iii) ‣ Assumption 1: ‣ II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

Assumption [1](https://arxiv.org/html/2512.19838v1#Thmassume1 "Assumption 1: ‣ II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")-3 also guarantees that the marginal price −∂1φ-\partial\_{1}\varphi is strictly decreasing in the reserves, because

|  |  |  |
| --- | --- | --- |
|  | ∂1φ​(y,κ)=−∂2f​(φ​(y,κ),y)∂1f​(φ​(y,κ),y)=−R​(φ​(y,κ),y),\partial\_{1}\varphi(y,\kappa)=-\frac{\partial\_{2}f(\varphi(y,\kappa),y)}{\partial\_{1}f(\varphi(y,\kappa),y)}=-R(\varphi(y,\kappa),y), |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂11φ​(y,κ)\displaystyle\partial\_{11}\varphi(y,\kappa) | =∂1R​(φ​(y,κ),y)​R​(φ​(y,κ),y)−∂2R​(φ​(y,κ),y).\displaystyle=\partial\_{1}R(\varphi(y,\kappa),y)\,R(\varphi(y,\kappa),y)-\partial\_{2}R(\varphi(y,\kappa),y). |  |

Thus, as LTs sell (resp. buy) the asset YY to the DEX, the reserves in asset YY increase (resp. decrease) and the marginal price decreases (resp. increases).

Moreover, the convexity of the level function ensures that the trading costs ([6](https://arxiv.org/html/2512.19838v1#S2.E6 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) are increasing in the quantity Δ​y\Delta y bought or sold by the LT. This is akin to limit order books where the cost of walking the book increases with the traded quantity. Finally, Assumption [1(iii)](https://arxiv.org/html/2512.19838v1#S2.I1.i3 "item 1(iii) ‣ Assumption 1: ‣ II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") imply that the costs in ([6](https://arxiv.org/html/2512.19838v1#S2.E6 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) are decreasing in the liquidity depth κ\kappa, so lower levels of reserves make trading more expensive for LTs.
This property is central to the trade-offs faced by LPs in DEXs: higher reserve levels reduce trading costs for LTs and attract organic, profitable order flow. However, as discussed below, they also increase the LP’s exposure to adverse selection costs.

Liquidity provision rewards. In addition to the liquidity costs arising from the convexity of the level function, LTs also pay a proportional fee π∈(0,1)\pi\in(0,1) to LPs when transacting in the DEX. Specifically, for a desired buy quantity Δ​y\Delta y of asset YY, an additional amount π​Δ​y​Ft\pi\,\Delta y\,F\_{t} of the reference asset is paid to LPs. Similarly, for a desired sell quantity Δ​y\Delta y , a portion π​Δ​y​Ft\pi\,\Delta y\,F\_{t} of the amount received from the DEX is kept by LPs. Thus, liquidity-taking activity generates fee revenue for LPs and incentivises increasing the reserves supplied to the DEX.

Liquidity position. Next, we describe the dynamics of the LP’s reserves in DEXs. In the remainder of this paper, we work on a filtered probability space (Ω,ℱ,𝔽=(ℱt)t∈[0,T],ℙ)(\Omega,\mathcal{F},\mathbb{F}=(\mathcal{F}\_{t})\_{t\in[0,T]},\mathbb{P}) satisfying the usual conditions. Denote by (Ft)t≥0\left(F\_{t}\right)\_{t\geq 0} the fundamental price of the risky asset in units of the reference asset XX. We assume that the price FF follows the stochastic differential equation (SDE)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ft=At​Ft​d​t+σ​Ft​d​Wt,\mathrm{d}F\_{t}=A\_{t}\,F\_{t}\,\mathrm{d}t+\sigma\,F\_{t}\,\mathrm{d}W\_{t}, |  | (7) |

where F0>0F\_{0}>0 is known, WW is an 𝔽\mathbb{F}-Brownian motion, σ>0\sigma>0 is a volatility parameter, and A=(At)t∈[0,T]A=(A\_{t})\_{t\in[0,T]} is a progressively measurable process satisfying 𝔼​[∫0T|At|p​dt]<∞\mathbb{E}\left[\int\_{0}^{T}|A\_{t}|^{p}\,{\mathrm{d}t}\right]<\infty for some p>2p>2. In our model, the process AA represents the LP’s stochastic private signal.777The private signal of the LP may be observable, partially observable, or fully latent. Examples include filtering the LT order flow or using price predictors.

In this work, we assume arbitrageurs continuously align the pool’s marginal price −∂1φ​(Yt,κ)-\partial\_{1}\varphi(Y\_{t},\kappa) with the fundamental value FtF\_{t} so

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft=−∂1φ​(Yt,κ).F\_{t}=-\partial\_{1}\varphi(Y\_{t},\kappa). |  | (8) |

Assumption [1(iv)](https://arxiv.org/html/2512.19838v1#S2.I1.i4 "item 1(iv) ‣ Assumption 1: ‣ II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") ensures that −∂1φ​(⋅,κ)-\partial\_{1}\varphi(\cdot,\kappa) is a C2C^{2}-diffeomorphism from (0,∞)(0,\infty) to (0,∞)(0,\infty), and therefore admits an inverse h​(⋅,κ)h(\cdot,\kappa) which is C2C^{2} on (0,∞)(0,\infty), so888Here, FF satisfies the SDE ([7](https://arxiv.org/html/2512.19838v1#S2.E7 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), whose solution is
Ft=F0​exp⁡{∫0t(As−σ22)​ds+σ​Wt}F\_{t}=F\_{0}\,\exp\left\{\int\_{0}^{t}(A\_{s}-\tfrac{\sigma^{2}}{2})\,\mathrm{d}s+\sigma\,W\_{t}\right\},
so the equality ([9](https://arxiv.org/html/2512.19838v1#S2.E9 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) is well defined.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft=−∂1φ​(Yt,κ)⇔Yt=h​(Ft,κ).F\_{t}=-\partial\_{1}\varphi(Y\_{t},\kappa)\iff Y\_{t}=h(F\_{t},\kappa). |  | (9) |

By Itô’s formula, the dynamics of the value of the DEX reserves in units of the reference asset XX are

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​(Xt+Yt​Ft)\displaystyle d\left(X\_{t}+Y\_{t}\,F\_{t}\right) | =d​(φ​(Yt,κ)−Yt​∂1φ​(Yt,κ))\displaystyle=d\left(\varphi(Y\_{t},\kappa)-Y\_{t}\,\partial\_{1}\varphi(Y\_{t},\kappa)\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Yt​d​Ft−12​∂11φ​(h​(Ft,κ),κ)​(∂1h​(Ft,κ))2​σ2​Ft2​d​t⏟LVR, convexity cost.\displaystyle=Y\_{t}\,\mathrm{d}F\_{t}-\underbrace{\tfrac{1}{2}\partial\_{11}\varphi(h(F\_{t},\kappa),\kappa)\,\left(\partial\_{1}h(F\_{t},\kappa)\right)^{2}\,\sigma^{2}\,F\_{t}^{2}\,dt}\_{\text{LVR, convexity cost}}\,. |  | (10) |

The term Yt​d​FtY\_{t}\,\mathrm{d}F\_{t} on the right-hand side of ([II](https://arxiv.org/html/2512.19838v1#S2.Ex3 "II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) is commonly regarded as the source of risk for a liquidity position with exogenously fixed initial reserves Y0Y\_{0}. LPs who short a portfolio in a frictionless CEX that fully replicates their position YtY\_{t} in the DEX are subject to the negative and predictable loss term on the right-hand side of ([II](https://arxiv.org/html/2512.19838v1#S2.Ex3 "II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")).
This term, known as the loss-versus-rebalancing (LVR) or convexity cost, is commonly interpreted as a measure of adverse selection costs in DEXs, which must be compensated by rewards in the form of fee revenue; see milionis2022automated.

In particular, the expected losses to arbitrageurs in ([II](https://arxiv.org/html/2512.19838v1#S2.Ex3 "II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) are increasing in the depth of liquidity κ\kappa and the volatility σ\sigma. Thus, the adverse selection component incentivises LPs to reduce the reserves they provide to the DEX.

The model. In contrast to existing characterisations of the viability of liquidity provision, this paper determines the endogenous distribution of LP performance when the LP offsets all or part of her risk in a CEX, at a cost and according to her risk preferences and private information. We also characterise the associated equilibrium depth of liquidity in the DEX and the resulting trading volumes.

The following sections introduce and solve a three-stage model that captures the strategic interactions between LPs and LTs in a DEX. In Stage one, the LP chooses the optimal level of reserves to deposit in the DEX. In Stage two, the LP determines her optimal replication strategy in the CEX. In Stage three, arbitrageurs and noise LTs trade in the DEX.

We solve the model by backward induction. Section [III](https://arxiv.org/html/2512.19838v1#S3 "III Stage three: trading volumes ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") solves stage three, where LTs take the liquidity depth κ\kappa as given and determine their optimal trading volumes by balancing DEX trading costs and utility from transacting. These volumes in turn generate fee revenue earned by the LP. Section [IV](https://arxiv.org/html/2512.19838v1#S4 "IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") solves stage two, where the LP takes the liquidity depth κ\kappa as given and determines her optimal CEX replication strategy to balance (i) replication penalties scaled by the LP’s risk aversion, (ii) CEX trading costs, and (iii) private signals. Finally, Section [V](https://arxiv.org/html/2512.19838v1#S5 "V Stage one: liquidity supply ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") solves stage one, where the LP anticipates the effects of her trading in the CEX and the activity of both arbitrageurs and noise LTs, to determine the optimal level of DEX reserves.

## III Stage three: trading volumes

### A Assumptions

The timing of stage three corresponds to the LP’s investment window [0,T][0,T]. Throughout this window, two types of LTs interact with the DEX.
First, arbitrageurs continuously align the pool’s price −∂1φ​(Yt,κ)-\partial\_{1}\varphi(Y\_{t},\kappa) with the fundamental value FtF\_{t}; for simplicity, we do not account for the fee revenue generated by their activity. Second, LTs with elastic demand for the asset trade against the pool. We assume that demand is symmetric, i.e., the number of buyers equals the number of sellers in expectation.

Assume an LT arrives to the DEX at time tt, and that her private utility for the asset is V.V. If V>0V>0 and the LT wishes to buy a quantity δ>0\delta>0 of asset YY, her execution costs consist of (i) the execution costs ([4](https://arxiv.org/html/2512.19838v1#S2.E4 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) implied by the liquidity supply κ\kappa and (ii) the fees π​δ​Ft\pi\,\delta\,F\_{t} paid to LTs. Thus, the execution price is

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(Yt−δ,κ)−φ​(Yt,κ)+π​δ​Ftδ.\frac{\varphi(Y\_{t}-\delta,\kappa)-\varphi(Y\_{t},\kappa)+\pi\,\delta\,F\_{t}}{\delta}. |  | (11) |

In our model, noise LTs use the following second-order approximation of the execution price:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | φ​(Yt−δ,κ)−φ​(Yt,κ)+π​δ​Ftδ\displaystyle\frac{\varphi(Y\_{t}-\delta,\kappa)-\varphi(Y\_{t},\kappa)+\pi\,\delta\,F\_{t}}{\delta} | ≈−δ​∂1φ​(Yt,κ)+12​δ2​∂11φ​(Yt,κ)+π​δ​Ftδ\displaystyle\approx\frac{-\delta\,\partial\_{1}\varphi(Y\_{t},\kappa)+\tfrac{1}{2}\delta^{2}\partial\_{11}\varphi(Y\_{t},\kappa)+\pi\,\delta\,F\_{t}}{\delta} |  | (12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Ft+π​Ft+12​δ​∂11φ​(Yt,κ).\displaystyle=F\_{t}+\pi\,F\_{t}+\tfrac{1}{2}\delta\,\partial\_{11}\varphi(Y\_{t},\kappa)\,. |  | (13) |

As shown in cartea2025decentralised; drissi2023models, this approximation is accurate in practice.999Mathematically, the approximation in ([12](https://arxiv.org/html/2512.19838v1#S3.E12 "In A Assumptions ‣ III Stage three: trading volumes ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) reduces the LT’s problem to a linear-quadratic optimisation problem with an analytical solution. In particular, the approximation captures the key economic effect that execution prices worsen as liquidity depth κ\kappa decreases, because the convexity term ∂11φ\partial\_{11}\varphi is decreasing in κ\kappa by Assumption [1(iii)](https://arxiv.org/html/2512.19838v1#S2.I1.i3 "item 1(iii) ‣ Assumption 1: ‣ II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

Similarly, if V<0V<0 and the LT wishes to sell the quantity δ>0\delta>0 of asset YY, her execution price is

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(Yt,κ)−φ​(Yt+δ,κ)−π​δ​Ftδ≈Ft−π​Ft−12​δ​∂11φ​(Yt,κ).\frac{\varphi(Y\_{t},\kappa)-\varphi(Y\_{t}+\delta,\kappa)-\pi\,\delta\,F\_{t}}{\delta}\approx F\_{t}-\pi\,F\_{t}-\tfrac{1}{2}\delta\,\partial\_{11}\varphi\left(Y\_{t},\kappa\right)\,. |  | (14) |

### B Liquidity needs

Noise LTs have random liquidity needs and take the liquidity depth κ\kappa in the DEX, determined by the LP in stage 1, as given. To model the random liquidity needs of an LT arriving at time t∈[0,T]t\in[0,T], we assume that she has a private utility for holding the asset in the form of a private valuation of the risky asset. In our model, the noise LT’s utility from holding one unit of the risky asset is Ft​(1+V)F\_{t}\,(1+V), where VV is the realization of a random variable symmetrically distributed around zero and independent of all other processes. Specifically, we assume that the distribution of |V||V| is supported on the compact interval [π,1][\pi,1], and we denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | v=𝔼​[|V|].v=\mathbb{E}[|V|]\,. |  | (15) |

Thus, an LT observing V≥πV\geq\pi (resp. V≤−πV\leq-\pi) wishes to buy (resp. sell) the asset. We assume that the proportional utility |V||V| exceeds π\pi to ensure positive trading volumes. Moreover, note that 𝔼​[V]=0\mathbb{E}[V]=0, so the expected cumulative trading volume of noise LTs, from the perspective of the LP, is zero.

### C Trading volumes

If an LT arrives at the DEX at time tt, then she determines her optimal trading volume δt⋆\delta\_{t}^{\star} by trading off execution costs ([12](https://arxiv.org/html/2512.19838v1#S3.E12 "In A Assumptions ‣ III Stage three: trading volumes ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"))–([14](https://arxiv.org/html/2512.19838v1#S3.E14 "In A Assumptions ‣ III Stage three: trading volumes ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) against her private utility for the asset.
Specifically, the noise LT’s performance criterion, when buying or selling a quantity δ>0\delta>0, is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​(|V|−π)​Ft−12​δ2​∂11φ​(Yt,κ),\displaystyle\delta\,\big(|V|-\pi\big)\,F\_{t}-\frac{1}{2}\,\delta^{2}\,\partial\_{11}\varphi\left(Y\_{t},\kappa\right), |  | (16) |

which is maximised with

|  |  |  |  |
| --- | --- | --- | --- |
|  | δt⋆=Ft​|V|−π∂11φ​(Yt,κ).\delta^{\star}\_{t}=F\_{t}\,\frac{|V|-\pi}{\partial\_{11}\varphi\left(Y\_{t},\kappa\right)}\,. |  | (17) |

The trading volume of a noise LT can be written as a function of
(i) the liquidity depth κ\kappa and
(ii) the current level of reserves YtY\_{t}, both of which determine the convexity of the level function. Accordingly, we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | δt⋆=δ⋆​(Yt,κ)=|V|−π∂11φ​(Yt,κ)​∂1φ​(Yt,κ).\delta\_{t}^{\star}=\delta^{\star}(Y\_{t},\kappa)=\frac{|V|-\pi}{\partial\_{11}\varphi(Y\_{t},\kappa)}\,\partial\_{1}\varphi(Y\_{t},\kappa)\,. |  | (18) |

Using the equivalence ([9](https://arxiv.org/html/2512.19838v1#S2.E9 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), we may also express noise LT trading volumes as a function of the depth κ\kappa and the fundamental price FtF\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δt⋆=δ⋆​(Ft,κ)=|V|−π∂11φ​(h​(Ft,κ),κ)​Ft.\delta\_{t}^{\star}=\delta^{\star}(F\_{t},\kappa)=\frac{|V|-\pi}{\partial\_{11}\varphi\left(h(F\_{t},\kappa),\kappa\right)}\,F\_{t}\,. |  | (19) |

We assume that, throughout the time window [0,T][0,T], the number of noise LTs arriving to the DEX follows a Poisson process (Nt)t∈[0,T](N\_{t})\_{t\in[0,T]} with constant intensity λ\lambda.
Noise LTs therefore generate fee revenue at a stochastic rate, and the LP’s anticipated expected fee revenue in stage one is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0Tπ​δt⋆​Ft​𝑑Nt]=λ​π​(v−π)​𝔼​[∫0TFt2∂11φ​(h​(Ft,κ),κ)​𝑑t].\mathbb{E}\left[\int\_{0}^{T}\pi\,\delta\_{t}^{\star}\,F\_{t}\,dN\_{t}\right]=\lambda\,\pi\,(v-\pi)\,\mathbb{E}\left[\int\_{0}^{T}\frac{F\_{t}^{2}}{\partial\_{11}\varphi\left(h(F\_{t},\kappa),\kappa\right)}\,dt\right]. |  | (20) |

We define the instantaneous rate of fee revenue from the perspective of the LP, and expressed in units of the reference asset XX, as a function of the fundamental price and liquidity depth:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πt=Π​(Ft,κ)=λ​π​(v−π)​Ft2∂11φ​(h​(Ft,κ),κ).\Pi\_{t}=\Pi(F\_{t},\kappa)=\frac{\lambda\,\pi\,(v-\pi)\,F\_{t}^{2}}{\partial\_{11}\varphi\left(h(F\_{t},\kappa),\kappa\right)}\,. |  | (21) |

The key economic force implied by the trading volumes ([21](https://arxiv.org/html/2512.19838v1#S3.E21 "In C Trading volumes ‣ III Stage three: trading volumes ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) is that greater liquidity depth attracts larger trading volumes because convexity costs are lower, thereby generating higher fee revenue for LPs. In Stage 1, the LP anticipates that supplying more liquidity increases fee income. However, as discussed below, higher liquidity also amplifies losses to arbitrageurs.

## IV Stage two: risk offsetting in the centralised exchange

In this section, the LP takes as given the liquidity deposit κ\kappa determined in stage one. The liquidity position in the DEX is exposed to adverse selection costs, which increase with market volatility. To manage the risk of her position and to exploit private information, the LP trades in the CEX to maximise her total wealth accross the DEX and the CEX, subject to risk constraints and trading costs.

### A Assumptions

In our model, the LP deposits reserves (X0,Y0)(X\_{0},Y\_{0}) at time 0 into a DEX characterised by a strictly convex level function φ\varphi, and withdraws liquidity at a terminal time T>0T>0. We assume that the LP remains passive over this interval.101010Active and high-frequency adjustments of liquidity positions are impractical on blockchains: such rebalancing would incur prohibitive gas fees, and on-chain transactions are exposed to predatory bots that exploit transaction public visibility. The risky asset is also traded on a CEX. The LP earns fee revenue from noise LTs trading in the DEX and manages the risk exposure of her DEX position by trading in the CEX at rate ν=(νt)t∈[0,T]\nu=(\nu\_{t})\_{t\in[0,T]}. Moreover, the LP also exploits private information driving the fundamental price.

The risky asset’s mid-price Sν=(Stν)t∈[0,T]S^{\nu}=(S\_{t}^{\nu})\_{t\in[0,T]} in the CEX has two components: the fundamental price FF and a transient market impact Iν=(Itν)t∈[0,T]I^{\nu}=(I\_{t}^{\nu})\_{t\in[0,T]} induced by the LP’s trades in the CEX. Formally,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Stν=Ft+Itν,t∈[0,T].S\_{t}^{\nu}=F\_{t}+I\_{t}^{\nu},\qquad t\in[0,T]. |  | (22) |

The transient impact process IνI^{\nu} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Itν=∫0t(c​νs−β​Isν)​ds,I\_{t}^{\nu}=\int\_{0}^{t}\left(c\,\nu\_{s}-\beta\,I^{\nu}\_{s}\right)\,\mathrm{d}s\,, |  | (23) |

so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Itν=c​∫0teβ​(s−t)​νs​ds.I^{\nu}\_{t}=c\int\_{0}^{t}e^{\beta\,(s-t)}\,\nu\_{s}\,\mathrm{d}s\,. |  | (24) |

Here, c>0c>0 measures the linear price of the LP’s trades, and β>0\beta>0 is the resilience parameter governing the decay of transient impact.

By Itô’s formula, the LP’s DEX reserves in asset YY follow the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt\displaystyle\mathrm{d}Y\_{t} | =∂1h​(Ft,κ)​d​Ft+12​∂11h​(Ft,κ)​d​⟨F⟩t\displaystyle=\partial\_{1}h(F\_{t},\kappa)\,\mathrm{d}F\_{t}+\tfrac{1}{2}\,\partial\_{11}h(F\_{t},\kappa)\,\mathrm{d}\langle F\rangle\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(∂1h​(Ft,κ)​At​Ft+σ22​∂11h​(Ft,κ)​Ft2)​d​t+σ​∂1h​(Ft,κ)​Ft​d​Wt\displaystyle=\left(\partial\_{1}h(F\_{t},\kappa)\,A\_{t}\,F\_{t}+\tfrac{\sigma^{2}}{2}\,\partial\_{11}h(F\_{t},\kappa)\,F\_{t}^{2}\right)\,{\mathrm{d}t}+\sigma\,\partial\_{1}h(F\_{t},\kappa)\,F\_{t}\,\mathrm{d}W\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Gt​Ft​d​t+σ​∂1h​(Ft,κ)​Ft​d​Wt,\displaystyle=G\_{t}\,F\_{t}\,{\mathrm{d}t}+\sigma\,\partial\_{1}h(F\_{t},\kappa)\,F\_{t}\,\mathrm{d}W\_{t}\,, |  | (25) |

where we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt:=∂1h​(Ft,κ)​At+σ22​∂11h​(Ft,κ)​Ft.G\_{t}:=\partial\_{1}h(F\_{t},\kappa)\,A\_{t}+\tfrac{\sigma^{2}}{2}\,\partial\_{11}h(F\_{t},\kappa)\,F\_{t}\,. |  | (26) |

The changes in the reserves in the risky asset YY in ([IV.A](https://arxiv.org/html/2512.19838v1#S4.Ex5 "A Assumptions ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) are driven by reserves changes due to arbitrageurs continuously aligning the marginal price to its fundamental value.

In our model, we denote the LP’s wealth in the pool by (Ltν)t∈[0,T](L\_{t}^{\nu})\_{t\in[0,T]}, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ltν:=∫0tΠ​(Fu,κ)​𝑑u+Xt+Yt​Stν.L\_{t}^{\nu}:=\int\_{0}^{t}\Pi(F\_{u},\kappa)\,du+X\_{t}+Y\_{t}\,S\_{t}^{\nu}. |  | (27) |

The first term represents the cumulative fee revenue paid by noise LTs, while the second and third terms correspond to the mark-to-market value of the LP’s liquidity position valued using the CEX price.

### B The performance criterion

The LP holds reserves {Xt,Yt}\{X\_{t},Y\_{t}\} in the DEX, and her inventory (Qtν)t∈[0,T]\left(Q\_{t}^{\nu}\right)\_{t\in[0,T]} in the CEX is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qtν=Q0+∫0tνs​ds.Q\_{t}^{\nu}=Q\_{0}+\int\_{0}^{t}\nu\_{s}\,{\mathrm{d}s}. |  | (28) |

Thus, her terminal holdings in the CEX are QTνQ\_{T}^{\nu}, which she values at the terminal CEX price STνS\_{T}^{\nu}. In our model, the LP maximises her terminal wealth subject to penalties for deviating from a perfect replication strategy, i.e., Qtν=−YtQ\_{t}^{\nu}=-Y\_{t}. Specifically, the LP’s performance criterion, when employing the strategy ν\nu from the admissible set 𝒜2{\mathcal{A}}\_{2} of 𝔽\mathbb{F}-progressively measurable processes that satisfy 𝔼​[∫0T|νt|2​dt]<∞\mathbb{E}\left[\int\_{0}^{T}|\nu\_{t}|^{2}\,{\mathrm{d}t}\right]<\infty, is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[LTν+QTν​STν−∫0T(Stν+η​νt)​νt​dt−ϕ2​∫0T(Qtν+Yt)2​dt].\displaystyle\mathbb{E}\Bigg[L\_{T}^{\nu}+Q\_{T}^{\nu}\,S\_{T}^{\nu}-\int\_{0}^{T}(S\_{t}^{\nu}+\eta\,\nu\_{t})\,\nu\_{t}\,\mathrm{d}t-\tfrac{\phi}{2}\int\_{0}^{T}(Q\_{t}^{\nu}+Y\_{t})^{2}\,\mathrm{d}t\Bigg]\,. |  | (P) |

Equivalently, by omitting terms that do not depend on ν\nu, the LP’s problem is to maximise

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[(YT+QTν)​STν⏟combined CEX-DEX position−∫0T(Stν+η​νt)​νt​dt⏟risk offsetting−ϕ2∫0T(Qtν+Yt)2dt]⏟deviation penalty.\mathbb{E}\bigg[\underbrace{\left(Y\_{T}+Q\_{T}^{\nu}\right)\,S\_{T}^{\nu}}\_{\text{combined CEX-DEX position}}-\underbrace{\int\_{0}^{T}\left(S\_{t}^{\nu}+\eta\,\nu\_{t}\right)\,\nu\_{t}\,{\mathrm{d}t}}\_{\text{risk offsetting}}-\underbrace{\tfrac{\phi}{2}\int\_{0}^{T}\left(Q\_{t}^{\nu}+Y\_{t}\right)^{2}\,{\mathrm{d}t}\bigg]}\_{\text{deviation penalty}}\,. |  | (29) |

The first term in the performance criterion ([29](https://arxiv.org/html/2512.19838v1#S4.E29 "In B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) represents the sum of the terminal values of the LP’s inventory in the CEX and her reserves in the DEX.
The second term captures the proceeds from trading in the CEX, and the corresponding trading costs incurred by the LP. We model these costs as a quadratic friction term governed by the cost parameter η>0\eta>0, which reflects the depth of liquidity in the CEX. Note that we assume the DEX operates as a secondary market and does not influence equilibrium outcomes in the CEX.

The third term in ([29](https://arxiv.org/html/2512.19838v1#S4.E29 "In B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) is a running penalty for deviating from a perfect replication strategy. Here, ϕ>0\phi>0 is a penalty parameter that scales the deviation cost; higher values of ϕ\phi correspond to greater aversion to holding non-zero net exposure between the LP’s positions in the DEX and the CEX. As ϕ→∞\phi\to\infty, the optimal strategy tends to the perfect replication of the DEX’s reserves.

The criterion in ([29](https://arxiv.org/html/2512.19838v1#S4.E29 "In B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) can be expressed entirely as a running reward under the following set of assumptions, which we adopt in the remainder of the paper.

###### Assumption 2:

1. (i)

   The private signal satisfies 𝔼​[exp⁡(r​∫0T|As|​ds)]<∞\mathbb{E}\left[\exp\left(r\int\_{0}^{T}|A\_{s}|\,{\mathrm{d}s}\right)\right]<\infty for all r∈ℝr\in\mathbb{R}.
2. (ii)

   For each κ>0\kappa>0, there exist real numbers
   Cκ,qκ,pκC\_{\kappa},q\_{\kappa},p\_{\kappa} such that, for all x>0x>0,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |h​(x,κ)|+|∂1h​(x,κ)|+|∂11h​(x,κ)|≤Cκ​(xqκ+xpκ).|h(x,\kappa)|+|\partial\_{1}h(x,\kappa)|+|\partial\_{11}h(x,\kappa)|\leq C\_{\kappa}\left(x^{q\_{\kappa}}+x^{p\_{\kappa}}\right)\,. |  | (30) |

Examples satisfying Assumption [2(i)](https://arxiv.org/html/2512.19838v1#S4.I1.i1 "item 2(i) ‣ Assumption 2: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") include all continuous Gaussian processes, while constant product markets such as Uniswap is an example of a market that fulfills Assumption [2(ii)](https://arxiv.org/html/2512.19838v1#S4.I1.i2 "item 2(ii) ‣ Assumption 2: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

###### Lemma 1:

The following inequalities hold:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝔼​[supt≤TFtq]<∞,𝔼​[∫0TFtq​dt]<∞,∀q∈ℝ,\displaystyle\mathbb{E}\left[\sup\_{t\leq T}F\_{t}^{q}\right]<\infty\,,\quad\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{q}\,{\mathrm{d}t}\right]<\infty\,,\quad\forall q\in\mathbb{R}\,, |  | (31) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝔼​[supt≤TYtq]<∞,𝔼​[∫0tYtq​dt]<∞,∀q∈[1,∞),\displaystyle\mathbb{E}\left[\sup\_{t\leq T}Y\_{t}^{q}\right]<\infty\,,\quad\mathbb{E}\left[\int\_{0}^{t}Y\_{t}^{q}\,{\mathrm{d}t}\right]<\infty\,,\quad\forall q\in[1,\infty)\,, |  | (32) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | and | 𝔼​[∫0T|Gt|q​dt]<∞,∀q∈[1,p).\displaystyle\mathbb{E}\left[\int\_{0}^{T}|G\_{t}|^{q}\,{\mathrm{d}t}\right]<\infty\,,\quad\forall q\in[1,p)\,. |  | (33) |

See Appendix [A.A](https://arxiv.org/html/2512.19838v1#S1.SS1 "A Proof of Lemma 1 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

The space 𝒜2{\mathcal{A}}\_{2} is precisely the real Hilbert space L2​(Ω×[0,T],𝒫,d​ℙ⊗d​t)L^{2}\left(\Omega\times[0,T],\mathcal{P},\mathrm{d}\mathbb{P}\otimes{\mathrm{d}t}\right), where 𝒫\mathcal{P} is the progressive σ\sigma-algebra, with the inner product ⟨ν,ζ⟩≔𝔼​[∫0Tνt​ζt​dt]\langle\nu,\zeta\rangle\coloneqq\mathbb{E}\!\left[\int\_{0}^{T}\nu\_{t}\,\zeta\_{t}\,{\mathrm{d}t}\right] and the norm ‖ν‖≔⟨ν,ν⟩1/2\|\nu\|\coloneqq\langle\nu,\nu\rangle^{1/2}. Lemma [1](https://arxiv.org/html/2512.19838v1#Thmlemma1 "Lemma 1: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") and Assumption [3](https://arxiv.org/html/2512.19838v1#Thmassume3 "Assumption 3: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") immediately imply the following lemma.

###### Lemma 2:

Fq∈𝒜2F^{q}\in{\mathcal{A}}\_{2} for all q∈ℝq\in\mathbb{R}.
Moreover, for all κ>0\kappa>0 and q≥1q\geq 1, h​(F,κ)qh(F,\kappa)^{q}, (∂1h​(F,κ))q(\partial\_{1}h(F,\kappa))^{q}, and (∂11h​(F,κ))q(\partial\_{11}h(F,\kappa))^{q} are in 𝒜2{\mathcal{A}}\_{2}.

Use the inequalities

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[∫0T|∫0tνs​ds|2​dt]\displaystyle\mathbb{E}\!\left[\int\_{0}^{T}\left|\int\_{0}^{t}\nu\_{s}\,{\mathrm{d}s}\right|^{2}\,{\mathrm{d}t}\right] | ≤𝔼​[∫0Tt​∫0t|νs|2​ds​dt]≤T2​𝔼​[∫0T|νt|2​dt]\displaystyle\leq\mathbb{E}\!\left[\int\_{0}^{T}t\int\_{0}^{t}|\nu\_{s}|^{2}\,{\mathrm{d}s}\,{\mathrm{d}t}\right]\leq T^{2}\;\mathbb{E}\!\left[\int\_{0}^{T}|\nu\_{t}|^{2}\,{\mathrm{d}t}\right] |  | (34) |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[∫0T|∫0teβ​(s−t)​νs​ds|2​dt]\displaystyle\mathbb{E}\!\left[\int\_{0}^{T}\left|\int\_{0}^{t}e^{\beta\,(s-t)}\nu\_{s}\,{\mathrm{d}s}\right|^{2}\,{\mathrm{d}t}\right] | ≤𝔼​[∫0Tt​∫0t|νs|2​ds​dt]≤T2​𝔼​[∫0T|νt|2​dt],\displaystyle\leq\mathbb{E}\!\left[\int\_{0}^{T}t\int\_{0}^{t}|\nu\_{s}|^{2}\,{\mathrm{d}s}\,{\mathrm{d}t}\right]\leq T^{2}\;\mathbb{E}\!\left[\int\_{0}^{T}|\nu\_{t}|^{2}\,{\mathrm{d}t}\right]\,, |  | (35) |

to define the two bounded linear operators 𝔔,ℑ:𝒜2→𝒜2\mathfrak{Q}\,,\mathfrak{I}:{\mathcal{A}}\_{2}\to{\mathcal{A}}\_{2} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝔔​ν)t=∫0tνs​dsand(ℑ​ν)t=c​∫0teβ​(s−t)​νs​ds.(\mathfrak{Q}\nu)\_{t}=\int\_{0}^{t}\nu\_{s}\,{\mathrm{d}s}\qquad\text{and}\qquad(\mathfrak{I}\nu)\_{t}=c\int\_{0}^{t}e^{\beta(s-t)}\,\nu\_{s}\,{\mathrm{d}s}\,. |  | (36) |

Notice that Qν=Q0+𝔔​νQ^{\nu}=Q\_{0}+\mathfrak{Q}\nu and Iν=ℑ​νI^{\nu}=\mathfrak{I}\nu. The following result shows that the performance criterion is a real-valued functional on 𝒜2{\mathcal{A}}\_{2}.

###### Lemma 3:

Let GG be defined in ([26](https://arxiv.org/html/2512.19838v1#S4.E26 "In A Assumptions ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")). The performance criterion ([29](https://arxiv.org/html/2512.19838v1#S4.E29 "In B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​[ν]+H,J[\nu]+H\,, |  | (37) |

where JJ is a linear functional on 𝒜2{\mathcal{A}}\_{2}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | H=(Y0+Q0)​F0+[∫0T{(Gt+σ2​∂1h​(Ft,κ))​Ft2+(Yt+Q0)​At​Ft−ϕ2​(Yt+Q0)2}​dt]H=(Y\_{0}+Q\_{0})\,F\_{0}+\left[\int\_{0}^{T}\left\{\left(G\_{t}+\sigma^{2}\,\partial\_{1}h(F\_{t},\kappa)\right)\,F\_{t}^{2}+(Y\_{t}+Q\_{0})\,A\_{t}\,F\_{t}-\tfrac{\phi}{2}\,(Y\_{t}+Q\_{0})^{2}\right\}\,{\mathrm{d}t}\right] |  | (38) |

is a well-defined real number which does not depend on ν\nu. Moreover, JJ takes the linear-quadratic form

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​[ν]=−12​𝒬​(ν)+ℒ​ν,J[\nu]=-\frac{1}{2}\,\mathcal{Q}(\nu)+\mathcal{L}\nu\,, |  | (39) |

where 𝒬:𝒜2×𝒜2→ℝ\mathcal{Q}:{\mathcal{A}}\_{2}\times{\mathcal{A}}\_{2}\to\mathbb{R} is the quadratic form defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒬​(ν)=2​η​‖ν‖2+2​⟨𝔔​ν,β​ℑ​ν−c​ν⟩+ϕ​‖𝔔​ν‖2,\mathcal{Q}(\nu)=2\,\eta\,\|\nu\|^{2}+2\,\langle\mathfrak{Q}\nu,\beta\,\mathfrak{I}\nu-c\,\nu\rangle+\phi\,\|\mathfrak{Q}\nu\|^{2}\,, |  | (40) |

and ℒ:𝒜2→ℝ\mathcal{L}:{\mathcal{A}}\_{2}\to\mathbb{R} is the bounded linear functional defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​ν=⟨G​F,ℑ​ν⟩+⟨Y+Q0,c​ν−β​ℑ​ν−ϕ​𝔔​ν⟩+⟨A​F,𝔔​ν⟩.\mathcal{L}\nu=\langle G\,F,\mathfrak{I}\nu\rangle+\langle Y+Q\_{0},c\,\nu-\beta\,\mathfrak{I}\nu-\phi\,\mathfrak{Q}\nu\rangle+\langle A\,F,\mathfrak{Q}\nu\rangle\,. |  | (41) |

See Appendix [A.B](https://arxiv.org/html/2512.19838v1#S1.SS2 "B Proof of Lemma 3 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

### C The optimal risk offsetting strategy

In the remainder of this work, we make the following standing assumption.

###### Assumption 3:

c<2​η​ϕc<\sqrt{2\,\eta\,\phi}.

This assumption bounds the instantaneous impact of the LP’s trades on CEX prices and ensures that such impacts are offset by sufficiently high trading costs and deviation penalty. This prevents degenerate strategies that would otherwise push prices to infinity. Assumption [3](https://arxiv.org/html/2512.19838v1#Thmassume3 "Assumption 3: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") is not very restrictive, as the parameter ϕ\phi is typically large to reflect the LP’s preference for strategies that closely replicate the LP’s position in the DEX. Moreover, trading costs η\eta associated with walking the book in the CEX are typically of a larger order of magnitude than the impact parameter cc.

We take a variational approach to characterize the optimal replication strategy. To this end, we obtain the following results:

###### Proposition 1:

Define the symmetric bounded linear operator Λ:𝒜2→𝒜2\Lambda:{\mathcal{A}}\_{2}\to{\mathcal{A}}\_{2} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ≔2​η+β​(ℑ⊤​𝔔+𝔔⊤​ℑ)−c​(𝔔+𝔔⊤)+ϕ​𝔔⊤​𝔔\Lambda\coloneqq 2\,\eta+\beta\,(\mathfrak{I}^{\top}\mathfrak{Q}+\mathfrak{Q}^{\top}\mathfrak{I})-c\,(\mathfrak{Q}+\mathfrak{Q}^{\top})+\phi\,\mathfrak{Q}^{\top}\mathfrak{Q} |  | (42) |

and b∈𝒜2b\in{\mathcal{A}}\_{2} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | b≔ℑ⊤​(G​F)+(c−β​ℑ⊤−ϕ​𝔔⊤)​(Y+Q0)+𝔔⊤​(A​F).b\coloneqq\mathfrak{I}^{\top}(G\,F)+(c-\beta\,\mathfrak{I}^{\top}-\phi\,\mathfrak{Q}^{\top})(Y+Q\_{0})+\mathfrak{Q}^{\top}(A\,F)\,. |  | (43) |

Then the objective JJ defined in Lemma [3](https://arxiv.org/html/2512.19838v1#Thmlemma3 "Lemma 3: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​[ν]=−12​⟨Λ​ν,ν⟩+⟨b,ν⟩.\displaystyle J[\nu]=-\frac{1}{2}\,\langle\Lambda\nu,\nu\rangle+\langle b,\nu\rangle\,. |  | (44) |

See Appendix [A.C](https://arxiv.org/html/2512.19838v1#S1.SS3 "C Proof of Proposition 1 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

###### Proposition 2:

Λ\Lambda defined in ([42](https://arxiv.org/html/2512.19838v1#S4.E42 "In Proposition 1: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) is *coercive*, i.e., there exists a constant C>0C>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Λ​ν,ν⟩≥C​‖ν‖2,\langle\Lambda\nu,\nu\rangle\geq C\,\|\nu\|^{2}\,, |  | (45) |

for all ν∈𝒜2\nu\in{\mathcal{A}}\_{2}. Consequently, Λ\Lambda has an inverse, which is also a bounded linear functional on 𝒜2{\mathcal{A}}\_{2}. Moreover, The objective JJ defined in Lemma [3](https://arxiv.org/html/2512.19838v1#Thmlemma3 "Lemma 3: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") is strictly concave.

See Appendix [A.D](https://arxiv.org/html/2512.19838v1#S1.SS4 "D Proof of Proposition 2 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

###### Proposition 3:

The objective JJ defined in Lemma [3](https://arxiv.org/html/2512.19838v1#Thmlemma3 "Lemma 3: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") is Gâteaux differentiable, and its Gâteaux derivative 𝔇​J​[ν]{\mathfrak{D}}J[\nu] at ν∈𝒜2\nu\in{\mathcal{A}}\_{2} is an element of 𝒜2{\mathcal{A}}\_{2}, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔇​J​[ν]t=−2​η​νt+c​(Yt+Qtν)+𝔼​[∫tT(As​Fs+c​νs−β​Isν−ϕ​(Ys+Qsν))​ds|ℱt]+c​et​β​𝔼​[∫tTe−s​β​(Gs​Fs−β​(Ys+Qsν))​ds|ℱt].\begin{split}{\mathfrak{D}}J[\nu]\_{t}&=-2\,\eta\,\nu\_{t}+c\,\left(Y\_{t}+Q\_{t}^{\nu}\right)+\mathbb{E}\left[\left.\int\_{t}^{T}\left(A\_{s}\,F\_{s}+c\,\nu\_{s}-\beta\,I\_{s}^{\nu}-\phi\left(Y\_{s}+Q\_{s}^{\nu}\right)\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]\\ &\quad\ +c\,e^{t\,\beta}\,\mathbb{E}\left[\left.\int\_{t}^{T}e^{-s\,\beta}\left(G\_{s}\,F\_{s}-\beta\,\left(Y\_{s}+Q\_{s}^{\nu}\right)\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]\,.\end{split} |  | (46) |

See Appendix [A.E](https://arxiv.org/html/2512.19838v1#S1.SS5 "E Proof of Proposition 3 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

###### Theorem 1:

The Gâteaux derivative ([46](https://arxiv.org/html/2512.19838v1#S4.E46 "In Proposition 3: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) vanishes at ν⋆∈𝒜2\nu^{\star}\in\mathcal{A}\_{2} if and only if ν⋆\nu^{\star} solves the FBSDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | {2​η​d​νt⋆=(−At​Ft+β​It+(ϕ+c​β)​(Yt+Qt)+c​β​Zt)​d​t+d​Mt,2​η​νT⋆=c​(YT+QT),d​Zt=(β​(Zt+Yt+Qt)−Gt​Ft)​d​t+d​Nt,ZT=0,d​It=(c​νt⋆−β​It)​d​t,I0=0,d​Qt=νt⋆​d​t,\displaystyle\begin{split}\left\{\begin{array}[]{rlrl}2\,\eta\,\mathrm{d}\nu^{\star}\_{t}&=\left(-A\_{t}\,F\_{t}+\beta\,I\_{t}+(\phi+c\,\beta)\,\left(Y\_{t}+Q\_{t}\right)+c\,\beta\,Z\_{t}\right)\,{\mathrm{d}t}+\mathrm{d}M\_{t},&2\,\eta\,\nu^{\star}\_{T}&=c\,\left(Y\_{T}+Q\_{T}\right)\,,\\ \mathrm{d}Z\_{t}&=\left(\beta\,\left(Z\_{t}+Y\_{t}+Q\_{t}\right)-G\_{t}\,F\_{t}\right)\,{\mathrm{d}t}+\mathrm{d}N\_{t},&Z\_{T}&=0\,,\\ \mathrm{d}I\_{t}&=\left(c\,\nu^{\star}\_{t}-\beta\,I\_{t}\right)\,{\mathrm{d}t},&I\_{0}&=0\,,\\ \mathrm{d}Q\_{t}&=\nu^{\star}\_{t}\,{\mathrm{d}t}\,,&\end{array}\right.\end{split} | |  | (47) |

for some 𝔽\mathbb{F}-martingales MM and NN such that MT,NT∈L2​(Ω)M\_{T},N\_{T}\in L^{2}(\Omega).

See Appendix [A.F](https://arxiv.org/html/2512.19838v1#S1.SS6 "F Proof of Theorem 1 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

The next result shows that the solution to the replication problem in the general case reduces to the solution of a differential Riccati equation, whose solution exists, is unique, and can be obtained efficiently numerically.

###### Proposition 4:

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | B11\displaystyle B\_{11} | =(−β000),B12=(c010),B21=12​η​(βϕ+c​β02​η​β),B22=12​η​(0c​β02​η​β),\displaystyle=\begin{pmatrix}-\beta&0\\ 0&0\end{pmatrix},\quad B\_{12}=\begin{pmatrix}c&0\\ 1&0\end{pmatrix},\quad B\_{21}=\frac{1}{2\,\eta}\begin{pmatrix}{\beta}&{\phi+c\beta}\\ 0&2\,\eta\,\beta\end{pmatrix},\quad B\_{22}=\frac{1}{2\,\eta}\begin{pmatrix}0&c\,\beta\\ 0&2\,\eta\,\beta\end{pmatrix}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | bt\displaystyle b\_{t} | =12​η​(−At​Ft+(ϕ+c​β)​Yt2​η​(β​Yt−Gt​Ft)),G=12​η​(0c00),K=(0Q0),L=12​η​(c​YT0).\displaystyle=\frac{1}{2\,\eta}\begin{pmatrix}-A\_{t}F\_{t}+(\phi+c\beta)Y\_{t}\\[1.99997pt] 2\,\eta\left(\beta\,Y\_{t}-G\_{t}\,F\_{t}\right)\end{pmatrix},\quad G=\frac{1}{2\,\eta}\begin{pmatrix}0&c\\ 0&0\end{pmatrix},\quad K=\begin{pmatrix}0\\ Q\_{0}\end{pmatrix},\quad L=\frac{1}{2\,\eta}\begin{pmatrix}c\,Y\_{T}\\ 0\end{pmatrix}. |  |

Suppose there exists a solution PP, which is an ℝ2×2\mathbb{R}^{2\times 2}-valued C1C^{1} function, to the DRE

|  |  |  |  |
| --- | --- | --- | --- |
|  | P′​(t)+P​(t)​B11+P​(t)​B12​P​(t)−B21−B22​P​(t)=0,P^{\prime}(t)+P(t)\,B\_{11}+P(t)\,B\_{12}\,P(t)-B\_{21}-B\_{22}\,P(t)=0\,, |  | (48) |

with terminal condition P​(T)=GP(T)=G. Define the ℝ2\mathbb{R}^{2}-valued processes ℓ\ell, Ψ\Psi, and Φ\Phi as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {ℓt=e−∫0t(P​(u)​B12−B22)​du​𝔼​[L−∫tTe∫0s(P​(u)​B12−B22)​du​bs​ds|ℱt],Φt=e∫0t(B12​P​(u)+B11)​du​(K+∫0te−∫0s(B12​P​(u)+B11)​du​B12​ℓs​ds),Ψ​(t)=P​(t)​Φt+ℓt.\begin{cases}\ell\_{t}&=e^{-\int\_{0}^{t}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,\mathbb{E}\!\left[\left.L-\int\_{t}^{T}e^{\int\_{0}^{s}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,b\_{s}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]\,,\\ \Phi\_{t}&=e^{\int\_{0}^{t}\left(B\_{12}\,P(u)+B\_{11}\right)\,{\mathrm{d}u}}\,\left(K+\int\_{0}^{t}e^{-\int\_{0}^{s}\left(B\_{12}\,P(u)+B\_{11}\right)\,{\mathrm{d}u}}\,B\_{12}\,\ell\_{s}\,{\mathrm{d}s}\right)\,,\\ \Psi(t)&=P(t)\,\Phi\_{t}+\ell\_{t}\,.\end{cases} |  | (49) |

Then (Φ,Ψ)(\Phi,\Psi) is a solution to the FBSDE ([47](https://arxiv.org/html/2512.19838v1#S4.E47 "In Theorem 1: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) with

|  |  |  |
| --- | --- | --- |
|  | Ψt=(νt⋆Zt),Φt=(ItQt).\Psi\_{t}=\begin{pmatrix}\nu\_{t}^{\star}\\ Z\_{t}\end{pmatrix}\,,\quad\Phi\_{t}=\begin{pmatrix}I\_{t}\\ Q\_{t}\end{pmatrix}\,. |  |

Moreover, under Assumption [3](https://arxiv.org/html/2512.19838v1#Thmassume3 "Assumption 3: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"), the DRE ([48](https://arxiv.org/html/2512.19838v1#S4.E48 "In Proposition 4: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) admits a unique solution.

See Appendix [A.G](https://arxiv.org/html/2512.19838v1#S1.SS7 "G Proof of Proposition 4 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

Proposition [4](https://arxiv.org/html/2512.19838v1#Thmproposition4 "Proposition 4: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") shows that in the general case of a DEX with convex level function, the replication strategy of the LP can be obtained efficiently by solving the associated differential Riccati equation ([48](https://arxiv.org/html/2512.19838v1#S4.E48 "In Proposition 4: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")).

### D No transient impact

Here, we consider the case where the LP’s trading activity in the CEX is significantly smaller than the overall market activity, so the LP’s transient price impact is negligible. Specifically, we assume c=0c=0, in which case Iν=0I^{\nu}=0 for any ν\nu. Under this assumption, the LP’s optimisation problem is solved explicitly in the following result.

###### Proposition 5:

Assume c=0.c=0\,. The optimal risk offsetting strategy in the CEX is

|  |  |  |  |
| --- | --- | --- | --- |
|  | νt=P​(t)​(Q0​P~​(0,t)+∫0tP~​(s,t)​ℓs​ds)+ℓt,\nu\_{t}=P(t)\,\left(Q\_{0}\,\tilde{P}(0,t)+\int\_{0}^{t}\tilde{P}(s,t)\,\ell\_{s}\,{\mathrm{d}s}\right)+\ell\_{t}\,, |  | (50) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓt=12​η​𝔼​[∫tTP~​(t,s)​(As​Fs−ϕ​Ys)​ds|ℱt],\ell\_{t}=\tfrac{1}{2\,\eta}\mathbb{E}\left[\left.\int\_{t}^{T}\tilde{P}(t,s)\,(A\_{s}\,F\_{s}-\phi\,Y\_{s})\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]\,, |  | (51) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(t)=ϕ2​η​tanh⁡(ϕ2​η​(t−T))andP~​(s,t)=cosh⁡(ϕ2​η​(t−T))cosh⁡(ϕ2​η​(s−T)).P(t)=\sqrt{\tfrac{\phi}{2\,\eta}}\tanh\left(\sqrt{\tfrac{\phi}{2\,\eta}}(t-T)\right)\qquad\text{and}\qquad\tilde{P}(s,t)=\frac{\cosh\left(\sqrt{\tfrac{\phi}{2\,\eta}}(t-T)\right)}{\cosh\left(\sqrt{\tfrac{\phi}{2\,\eta}}(s-T)\right)}\,. |  | (52) |

See Appendix [A.H](https://arxiv.org/html/2512.19838v1#S1.SS8 "H Proof of Proposition 5 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

## V Stage one: liquidity supply

In the previous section, we derived the optimal stage two replication strategy νt⋆\nu\_{t}^{\star} in the CEX for an arbitrary initial position Q0Q\_{0} and an arbitrary depth of liquidity κ\kappa, corresponding to initial DEX reserves Y0=h​(F0,κ)Y\_{0}=h(F\_{0},\kappa). To determine the optimal liquidity depth κ⋆\kappa^{\star} in stage one, the LP anticipates that (i) she will execute her optimal strategy in the CEX at a cost, (ii) trading volumes will respond endogenously to the level of liquidity she supplies, and (iii) adverse selection losses increase with the amount of liquidity deposited in the DEX.

For simplicity, we assume that the LP starts with a CEX position Q0=−Y0=−h​(F0,κ)Q\_{0}=-Y\_{0}=-h(F\_{0},\kappa). This assumption facilitates comparisons of performance and risk across different values of the model primitives: CEX trading costs η\eta, risk aversion ϕ\phi, and the profitability parameters {λ,v,π}\{\lambda,v,\pi\}.

Let St⋆S\_{t}^{\star}, Qt⋆Q\_{t}^{\star}, and Lt⋆L\_{t}^{\star} be the price, inventory, and DEX wealth when the LP executes the optimal strategy νt⋆\nu\_{t}^{\star} in the CEX, where

|  |  |  |
| --- | --- | --- |
|  | Lt⋆:=∫0tΠ​(Fu,κ)​du+Xt+Yt​St⋆,L\_{t}^{\star}:=\int\_{0}^{t}\Pi(F\_{u},\kappa)\,{\mathrm{d}u}+X\_{t}+Y\_{t}\,S^{\star}\_{t}\,, |  |

and Π\Pi is defined in ([21](https://arxiv.org/html/2512.19838v1#S3.E21 "In C Trading volumes ‣ III Stage three: trading volumes ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")). In the general case, the optimisation problem of stage one is

|  |  |  |  |
| --- | --- | --- | --- |
|  | supκ∈[0,κ¯]𝔼​[LT⋆+QT⋆​ST⋆−∫0T(St⋆+η​νt⋆)​νt⋆​dt−ϕ2​∫0T(Qt⋆+Yt)2​dt],\displaystyle\sup\_{\kappa\in[0,\overline{\kappa}]}\mathbb{E}\!\left[L\_{T}^{\star}+Q\_{T}^{\star}\,S\_{T}^{\star}-\int\_{0}^{T}\left(S\_{t}^{\star}+\eta\,\nu^{\star}\_{t}\right)\,\nu^{\star}\_{t}\,\mathrm{d}t-\frac{\phi}{2}\int\_{0}^{T}\left(Q\_{t}^{\star}+Y\_{t}\right)^{2}\,\mathrm{d}t\right]\,, |  | (K) |

where κ¯\overline{\kappa} denotes the maximum admissible liquidity depth implied by the LP’s budget constraint.

The next results show that the LP’s objective is well defined and establish mild conditions under which it is continuous and therefore attains its maximum over the compact set [0,κ¯][0,\overline{\kappa}].

###### Proposition 6:

The LP’s objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[LTν⋆+QTν⋆​STν⋆−∫0T(Stν⋆+η​νt⋆)​νt⋆​dt−ϕ2​∫0T(Qtν⋆+Yt)2​dt]\mathbb{E}\!\left[L\_{T}^{\nu^{\star}}+Q\_{T}^{\nu^{\star}}\,S\_{T}^{\nu^{\star}}-\int\_{0}^{T}\left(S\_{t}^{\nu^{\star}}+\eta\,\nu^{\star}\_{t}\right)\,\nu^{\star}\_{t}\,\mathrm{d}t-\frac{\phi}{2}\int\_{0}^{T}\left(Q\_{t}^{\nu^{\star}}+Y\_{t}\right)^{2}\,\mathrm{d}t\right] |  | (53) |

is well-defined and can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​[ν⋆]+𝔼​[∫0T{(σ22+λ​π​(π−v))​∂1h​(Ft,κ)​Ft2+At​Ft​(Yt−Y0)−ϕ2​(Yt−Y0)2}​dt]J[\nu^{\star}]+\mathbb{E}\!\left[\int\_{0}^{T}\left\{\left(\frac{\sigma^{2}}{2}+\lambda\,\pi\,(\pi-v)\right)\,\partial\_{1}h(F\_{t},\kappa)\,F\_{t}^{2}+A\_{t}\,F\_{t}\,(Y\_{t}-Y\_{0})-\tfrac{\phi}{2}\,(Y\_{t}-Y\_{0})^{2}\right\}\,{\mathrm{d}t}\right] |  | (54) |

for all κ>0\kappa>0.

See Appendix [A.I](https://arxiv.org/html/2512.19838v1#S1.SS9 "I Proof of Proposition 6 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

###### Proposition 7:

Suppose there exist 𝔭,𝔮∈ℝ\mathfrak{p},\mathfrak{q}\in\mathbb{R} and a continuous function ℭ:(0,∞)→(0,∞)\mathfrak{C}:(0,\infty)\to(0,\infty) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |h​(x,κ)−h​(x,κ′)|+|∂1h​(x,κ)−∂1h​(x,κ′)|+|∂11h​(x,κ)−∂11h​(x,κ′)|≤(x𝔭+x𝔮)​|ℭ​(κ)−ℭ​(κ′)||h(x,\kappa)-h(x,\kappa^{\prime})|+|\partial\_{1}h(x,\kappa)-\partial\_{1}h(x,\kappa^{\prime})|+|\partial\_{11}h(x,\kappa)-\partial\_{11}h(x,\kappa^{\prime})|\leq\left(x^{\mathfrak{p}}+x^{\mathfrak{q}}\right)\,|\mathfrak{C}(\kappa)-\mathfrak{C}(\kappa^{\prime})| |  | (55) |

for all x,κ,κ′>0x,\kappa,\kappa^{\prime}>0. Then the LP’s objective ([53](https://arxiv.org/html/2512.19838v1#S5.E53 "In Proposition 6: ‣ V Stage one: liquidity supply ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) is continuous in κ\kappa.

See Appendix [A.J](https://arxiv.org/html/2512.19838v1#S1.SS10 "J Proof of Proposition 7 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

## VI Constant product markets

To study the implications of risk offsetting in CEXs for liquidity supply and trading in DEXs, we examine the equilibrium outcomes in constant product markets (CPMs) such as Uniswap. In this setting, the level function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(Y,κ)=κ2Y,\varphi(Y,\kappa)=\frac{\kappa^{2}}{Y}, |  | (56) |

and the corresponding fundamental price and reserves satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft=−∂1φ​(Yt,κ)=κ2Yt2andYt=h​(Ft,κ)=κFt.F\_{t}=-\partial\_{1}\varphi(Y\_{t},\kappa)=\frac{\kappa^{2}}{Y\_{t}^{2}}\qquad\text{and}\qquad Y\_{t}=h(F\_{t},\kappa)=\frac{\kappa}{\sqrt{F\_{t}}}\,. |  | (57) |

For simplicity, we assume that the LP is a sufficiently small agent whose trades do not generate transient price impact, that is, we set c=0c=0 in ([23](https://arxiv.org/html/2512.19838v1#S4.E23 "In A Assumptions ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")).

### A Without private information

Assume that the liquidity provider does not use private information and that the fundamental price evolves according to ([7](https://arxiv.org/html/2512.19838v1#S2.E7 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) with A=0A=0.
The following result characterises the equilibrium liquidity supply, trading volumes, and the LP’s strategy in the CEX. The result below is a special case of Proposition [8](https://arxiv.org/html/2512.19838v1#Thmproposition8 "Proposition 8: ‣ B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") and we omit the proof.

###### Corollary 1:

Assume the level function ([56](https://arxiv.org/html/2512.19838v1#S6.E56 "In VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) of a CPM. Then the liquidity supply κ¯\underline{\kappa} when the LP does not offset her risk in the CEX is

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ¯=8​γ​(1−e−σ2​T/8)−σ2​(1−2​e−σ2​T/8)ϕ​(eσ2​T−1−163​(e3​σ2​T/8−1)+σ2​T)​F03/2,\displaystyle\underline{\kappa}=\frac{{\displaystyle 8\,\gamma\left(1-e^{-\sigma^{2}T/8}\right)-\sigma^{2}\left(1-2e^{-\sigma^{2}T/8}\right)}}{{\displaystyle\phi\left(e^{\sigma^{2}T}-1-\tfrac{16}{3}\left(e^{3\sigma^{2}T/8}-1\right)+\sigma^{2}T\right)}}F\_{0}^{3/2}\,, |  | (58) |

where we refer to

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ=λ​π​(v−π)2,\gamma=\frac{\lambda\,\pi\,(v-\pi)}{2}\,, |  | (59) |

as the profitability parameter. The equilibrium liquidity supply when the LP offsets her risk in the CEX is

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ⋆=κ¯​cσ2​𝔅+c,\kappa^{\star}=\underline{\kappa}\,\frac{c}{\sigma^{2}\,\mathfrak{B}+c}\,, |  | (60) |

where PP and P~\tilde{P} are defined in ([52](https://arxiv.org/html/2512.19838v1#S4.E52 "In Proposition 5: ‣ D No transient impact ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔅=\displaystyle\mathfrak{B}= | ∫0T(1−P~​(0,t))​(e3​σ2​t/8−1)​dt−β2​∫0T∫sTg​(s)​P~​(s,t)​(eσ2​s​e3​σ2​(t−s)/8−e3​σ2​s/8)​dt​ds,\displaystyle\int\_{0}^{T}\big(1-\tilde{P}(0,t)\big)\,\big(e^{3\,\sigma^{2}t/8}-1\big){\mathrm{d}t}-\beta^{2}\int\_{0}^{T}\int\_{s}^{T}g(s)\,\tilde{P}(s,t)\,\big(e^{\sigma^{2}s}e^{3\,\sigma^{2}(t-s)/8}-e^{3\,\sigma^{2}s/8}\big)\,{\mathrm{d}t}\,{\mathrm{d}s}\,, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | c=\displaystyle c= | eσ2​T+133−163​e3​σ2​T/8+σ2​T,\displaystyle\,e^{\sigma^{2}T}+\frac{13}{3}-\frac{16}{3}\,e^{3\,\sigma^{2}T/8}+\sigma^{2}\,T\,, |  |

and the function gg is

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(s)\displaystyle g(s) | =1cosh⁡(β​(s−T))​∫sTcosh⁡(β​(u−T))​e3​σ2​(u−s)/8​𝑑u,β=ϕ2​η.\displaystyle=\frac{1}{\cosh\left(\beta\,\left(s-T\right)\right)}\int\_{s}^{T}\cosh\left(\beta\,\left(u-T\right)\right)\,e^{3\,\sigma^{2}(u-s)/8}\,du\,,\qquad\beta=\sqrt{\frac{\phi}{2\,\eta}}. |  |

In addition, the equilibrium trading volumes generate fee revenue at the instantaneous rate ([21](https://arxiv.org/html/2512.19838v1#S3.E21 "In C Trading volumes ‣ III Stage three: trading volumes ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π​(Ft,κ⋆)=γ​κ⋆​Ft.\Pi\left(F\_{t},\kappa^{\star}\right)=\gamma\,\kappa^{\star}\sqrt{F\_{t}}\,. |  | (61) |

Finally, the equilibrium risk-offsetting strategy is in ([50](https://arxiv.org/html/2512.19838v1#S4.E50 "In Proposition 5: ‣ D No transient impact ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓt=−β2​κ⋆​Ft−1/2​g​(t).\ell\_{t}=-\beta^{2}\,\kappa^{\star}\,F\_{t}^{-1/2}\,g\left(t\right)\,. |  | (62) |

Next, we show how model primitives influence market outcomes in CPMs. Namely, we study the effect of CEX trading costs η\eta, risk aversion ϕ\phi, fundamental volatility σ\sigma, and profitability γ.\gamma.

Liquidity supply. In CPMs, the equilibrium liquidity κ⋆\kappa^{\star} in ([60](https://arxiv.org/html/2512.19838v1#S6.E60 "In Corollary 1: ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), when the LP dynamically manages her risk in a CEX, takes the no-CEX liquidity κ¯\underline{\kappa} in ([58](https://arxiv.org/html/2512.19838v1#S6.E58 "In Corollary 1: ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) as a reference, and scales it by the coefficient cσ2​𝔅+c\frac{c}{\sigma^{2}\mathfrak{B}+c}.

The reference liquidity κ¯\underline{\kappa} does not depend on the trading costs η\eta in the CEX and is decreasing in the aversion parameter ϕ\phi because without access to a CEX, reducing risk exposure is only possible by reducing the size of liquidity supply. In contrast, the scaling coefficient depends on both aversion and CEX costs, and it does so only through their ratio β=ϕ/η\beta=\phi/\eta. Specifically, both aversion and trading costs represent forms of disutility to the LP; see  ([K](https://arxiv.org/html/2512.19838v1#S5.Ex11 "In V Stage one: liquidity supply ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")). The disutility associated with CEX trading costs discourages active replication of the LP’s position, whereas the disutility associated with risk aversion encourages active replication. Ultimately, the ratio of these disutilities determines the equilibrium level of liquidity supply and, as we show below, also shapes the LP’s behaviour in the CEX. Figure [1](https://arxiv.org/html/2512.19838v1#S6.F1 "Figure 1 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") showcases the liquidity supplies ([60](https://arxiv.org/html/2512.19838v1#S6.E60 "In Corollary 1: ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) and ([58](https://arxiv.org/html/2512.19838v1#S6.E58 "In Corollary 1: ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), with and without access to a CEX, as a function of model primitives.

![Refer to caption](x1.png)


Figure 1: Equilibrium liquidity supply κ⋆\kappa^{\star} in ([60](https://arxiv.org/html/2512.19838v1#S6.E60 "In Corollary 1: ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) (black curves) and reference liquidity κ¯\underline{\kappa} in ([58](https://arxiv.org/html/2512.19838v1#S6.E58 "In Corollary 1: ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) (blue curves), plotted as functions of the model primitives. Default parameter values are: fundamental volatility σ=0.1\sigma=0.1, investment horizon T=1T=1, private signal A=0A=0, CEX trading cost η=10−2\eta=10^{-2}, ratio β=ϕ/η=10\beta=\phi/\eta=10, and profitability γ=0.2\gamma=0.2.

The first panel illustrates the dependence of CPM liquidity according to the ratio β\beta of risk aversion to CEX trading costs (for fixed η\eta). As this ratio increases, the disutility from not closely replicating the DEX position outweighs the disutility generated by CEX trading costs. In this case, the LP more tightly replicates her position in the DEX, as illustrated in more detail in Figure [2(a)](https://arxiv.org/html/2512.19838v1#S6.F2.sf1 "In Figure 2 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"). Moreover, to further decrease the disutility associated with risk exposure, the LP reduces the size of her liquidity supply.

![Refer to caption](x2.png)


(a) η=10−2\eta=10^{-2}

![Refer to caption](x3.png)


(b) η=10−1\eta=10^{-1}

Figure 2: Each figure [2(a)](https://arxiv.org/html/2512.19838v1#S6.F2.sf1 "In Figure 2 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") and [2(b)](https://arxiv.org/html/2512.19838v1#S6.F2.sf2 "In Figure 2 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") plots a sample path of the LP’s reserves YtY\_{t} held in the DEX and the inventory QtQ\_{t} held in the CEX (top panels), together with their corresponding values expressed in units of the reference asset XX (bottom panels). The left panels of each figure correspond to a ratio of risk aversion to trading costs β=10\beta=10, while the right panels correspond to β=103\beta=10^{3}. Other default parameter values are profitability γ=0.1\gamma=0.1, fundamental volatility σ=0.2\sigma=0.2, and investment horizon T=0.3T=0.3.

Moreover, the first panel of Figure [1](https://arxiv.org/html/2512.19838v1#S6.F1 "Figure 1 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") also shows that the LP increases the scaling applied to the reference liquidity κ¯\underline{\kappa} as the ratio β\beta rises. The intuition is as follows. The optimal offsetting strategy effectively reduces the disutility from deviations between CEX and DEX positions, and this benefit becomes increasingly valuable as risk aversion ϕ\phi grows relative to the trading cost η\eta. Anticipating this, the LP applies a higher scaling to the reference liquidity.

The second panel of Figure [1](https://arxiv.org/html/2512.19838v1#S6.F1 "Figure 1 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") shows that, for a fixed ratio β\beta, higher trading costs η\eta reduce equilibrium DEX liquidity. The underlying economic force is that dynamic replication in the CEX, at the intensity implied by the ratio β\beta, becomes more costly as η\eta increases. The LP anticipates these higher costs by decreasing her DEX exposure, which reduces the amount of CEX trading required to replicate her position.

This mechanism is further illustrated in Figure [2(b)](https://arxiv.org/html/2512.19838v1#S6.F2.sf2 "In Figure 2 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"). Figures [2(a)](https://arxiv.org/html/2512.19838v1#S6.F2.sf1 "In Figure 2 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") and [2(b)](https://arxiv.org/html/2512.19838v1#S6.F2.sf2 "In Figure 2 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") together show that the degree with which the LP replicates her position in the CEX is governed by the ratio β\beta, while the overall level of liquidity supply decreases as CEX trading costs or aversion increases (holding β\beta fixed).

Finally, the third panel of Figure [1](https://arxiv.org/html/2512.19838v1#S6.F1 "Figure 1 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") shows that fundamental price volatility decreases liquidity, and the last panel shows that greater profitability of liquidity demand increases it. In our model, the profitability increases with the fee rate π\pi, the arrival intensity of noise LTs λ\lambda, and the average absolute liquidity need vv.

Risks and returns. Next, we study the equilibrium risks and returns of liquidity provision in a CPM as a function of model primitives. Specifically, we study the LP’s relative change in wealth when she offsets her risk in the CEX, which we compute as follows. Recall that the LP starts with a neutral cumulative CEX–DEX position in asset YY, satisfying Q0+Y0=0Q\_{0}+Y\_{0}=0, and with an initial DEX position in the reference asset XX equal to X0=κ​F0X\_{0}=\kappa\,\sqrt{F\_{0}}. When the LP executes her optimal CEX strategy, her change in wealth, measured in units of XX, is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∫0TΠ​(Ft,κ⋆)​𝑑t+XT+(QT⋆+YT)​FT−∫0T(Ft−η​νt⋆)​νt⋆​𝑑t−X0,\displaystyle\int\_{0}^{T}\Pi(F\_{t},\kappa^{\star})\,dt+X\_{T}+\big(Q\_{T}^{\star}+Y\_{T}\big)\,F\_{T}-\int\_{0}^{T}\left(F\_{t}-\eta\,\nu\_{t}^{\star}\right)\nu\_{t}^{\star}\,dt-X\_{0}, |  | (63) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∫0TΠ​(Ft,κ⋆)​𝑑t⏟fee revenue+2​κ⋆​(FT1/2−F01/2)⏟DEX position value change−∫0TQt⋆​𝑑Ft⏟risk offsetting−∫0Tη​νt⋆ 2​𝑑t⏟CEX cost,\displaystyle\underbrace{\int\_{0}^{T}\Pi(F\_{t},\kappa^{\star})\,dt}\_{\text{fee revenue}}+\underbrace{2\,\kappa^{\star}\big(F\_{T}^{1/2}-F\_{0}^{1/2}\big)}\_{\text{DEX position value change}}-\underbrace{\int\_{0}^{T}Q\_{t}^{\star}\,dF\_{t}}\_{\text{risk offsetting}}-\underbrace{\int\_{0}^{T}\eta\,\nu\_{t}^{\star\,2}\,dt}\_{\text{CEX cost}}\,, |  | (64) |

where νt⋆\nu\_{t}^{\star} is the optimal trading rate in the CEX and Qt⋆Q\_{t}^{\star} the corresponding inventory. To obtain the relative change in the LP’s wealth, we normalise ([63](https://arxiv.org/html/2512.19838v1#S6.E63 "In A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) by the initial cash position X0=κ⋆​F0X\_{0}=\kappa^{\star}\sqrt{F\_{0}}.

Note that the expected change in the value of the LP’s DEX liquidity position is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[2​κ⋆​(FT1/2−F01/2)]=F01/2​(e−σ2​T/8−1),\mathbb{E}\left[2\,\kappa^{\star}\,(F\_{T}^{1/2}-F\_{0}^{1/2})\right]=F\_{0}^{1/2}\left(e^{-\sigma^{2}\,T/8}-1\right)\,, |  | (65) |

which is always negative. The viability of DEX liquidity provision depends on whether the stage-three fee revenue, adjusted by replication costs and the proceeds form risk offsetting, covers the adverse selection costs ([65](https://arxiv.org/html/2512.19838v1#S6.E65 "In A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")).

When the LP does not offset her exposure in the CEX, i.e., when ν≡0\nu\equiv 0, her inventory in the CEX remains constant, Qt=Q0Q\_{t}=Q\_{0}, and the expected change in her wealth is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∫0TΠ​(Ft,κ¯)​𝑑t⏟fee revenue+2​κ¯​(FT1/2−F01/2)⏟DEX position value change−Q0​(FT−F0)⏟CEX position.\displaystyle\underbrace{\int\_{0}^{T}\Pi(F\_{t},\underline{\kappa})\,dt}\_{\text{fee revenue}}+\underbrace{2\,\underline{\kappa}\big(F\_{T}^{1/2}-F\_{0}^{1/2}\big)}\_{\text{DEX position value change}}-\underbrace{Q\_{0}\,(F\_{T}-F\_{0})}\_{\text{CEX position}}. |  | (66) |

Comparing ([63](https://arxiv.org/html/2512.19838v1#S6.E63 "In A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) and ([66](https://arxiv.org/html/2512.19838v1#S6.E66 "In A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) isolates the effect of dynamic risk offsetting in the CEX: it reduces inventory risk at the expense of trading frictions η​νt2\eta\,\nu\_{t}^{2}, but it may also alter expected fee revenue and terminal payoffs through the adjusted liquidity choice κ⋆\kappa^{\star} studied above. Figure [3](https://arxiv.org/html/2512.19838v1#S6.F3 "Figure 3 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") illustrates these effects by plotting the distribution of the profit and loss of DEX liquidity provision as a function of model primitives.

![Refer to caption](x4.png)


Figure 3: Distribution of the equilibrium adverse selection and trading costs (top panels) and the equilibrium payoff of liquidity provision (bottom panels).
The distribution is obtained from 20002000 market simulations, with the time interval discretised into 10001000 steps. Default parameter values are σ=0.1\sigma=0.1, T=1T=1, A=0A=0, η=10−2\eta=10^{-2}, β=10\beta=10, and γ=0.25\gamma=0.25.

Figure [3](https://arxiv.org/html/2512.19838v1#S6.F3 "Figure 3 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") highlights a first-order economic effect of risk offsetting on the viability of liquidity provision in DEXs. While the expected adverse selection losses to arbitrageurs in ([65](https://arxiv.org/html/2512.19838v1#S6.E65 "In A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) are unaffected by the LP’s trading in the CEX, the variance of these losses decreases as the ratio β\beta increases and replication becomes more aggressive. At the same time, the trading costs generated by the LP’s activity in the CEX increase with the intensity of replication. Consequently, the viability of DEX liquidity provision is shaped by (i) the LP’s aversion to risk, which determine the trading costs incurred in the CEX, and by (ii) fee revenue. In particular, Figure [3](https://arxiv.org/html/2512.19838v1#S6.F3 "Figure 3 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") shows that beyond a threshold level of risk aversion, liquidity provision is no longer viable and DEX markets shut down.

The second column of panels in Figure [3](https://arxiv.org/html/2512.19838v1#S6.F3 "Figure 3 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") shows that the equilibrium percentage returns and risk of liquidity provision depend only on the ratio of risk aversion to trading costs, and not on the absolute level of either parameter. The intuition is that the LP adjusts the aggressiveness of risk offsetting according to the ratio β\beta, while she adjusts the level of liquidity supply according to the absolute level of risk aversion. As a result, returns and risks of liquidity provision, when measured relative to the LP’s initial wealth, are driven solely by the ratio β\beta.

The third column of Figure [3](https://arxiv.org/html/2512.19838v1#S6.F3 "Figure 3 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") shows that higher fundamental price volatility substantially increases adverse selection costs, thereby undermining the viability of liquidity provision in CPMs. In contrast, the final column illustrates how the profitability of noise demand affects the returns and risks of liquidity provision. As profitability γ\gamma increases, the LP is willing to supply more liquidity (see Figure [1](https://arxiv.org/html/2512.19838v1#S6.F1 "Figure 1 ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) and to bear greater inventory risk, and the incentive to offset large positions at quadratic cost in the CEX diminishes. In equilibrium, although adverse selection losses and inventory risk rise, they are more than compensated by higher fee revenue.

### B Risk offsetting and private information

Here, we assume that the LP employs a private signal driving the drift of the fundamental price of asset YY. The equilibrium liquidity supplies, with and without risk offsetting, are characterised in the following result.

###### Proposition 8:

Assume Yt=Ft−1/2​κY\_{t}=F\_{t}^{-1/2}\,\kappa as in ([57](https://arxiv.org/html/2512.19838v1#S6.E57 "In VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")). The equilibrium liquidity supply in the CPM when the LP does not use the CEX is

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ¯=𝔼​[∫0Tγ​Ft1/2​dt+2​FT1/2−F0−1/2​FT]ϕ​𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt],\underline{\kappa}=\frac{\mathbb{E}\left[\int\_{0}^{T}\gamma\,F\_{t}^{1/2}\,{\mathrm{d}t}+2\,F\_{T}^{1/2}-F\_{0}^{-1/2}\,F\_{T}\right]}{\phi\,\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]}\,, |  | (67) |

Moreover, define the following processes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Ctℓ\displaystyle C\_{t}^{\ell} | =−ϕ2​η​𝔼​[∫tTP~​(t,s)​Fs−1/2​ds|ℱt],\displaystyle=-\frac{\phi}{2\,\eta}\,\mathbb{E}\left[\left.\int\_{t}^{T}\tilde{P}(t,s)\,F\_{s}^{-1/2}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right], | Dtℓ\displaystyle D\_{t}^{\ell} | =12​η​𝔼​[∫tTP~​(t,s)​As​Fs​ds|ℱt],\displaystyle=\frac{1}{2\,\eta}\,\mathbb{E}\left[\left.\int\_{t}^{T}\tilde{P}(t,s)\,A\_{s}\,F\_{s}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right], |  | (68) |
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | CtQ\displaystyle C\_{t}^{Q} | =−F0−1/2​P~​(0,t)+∫0tP~​(s,t)​Csℓ​ds,\displaystyle=-F\_{0}^{-1/2}\,\tilde{P}(0,t)+\int\_{0}^{t}\tilde{P}(s,t)\,C\_{s}^{\ell}\,{\mathrm{d}s}, | M~t\displaystyle\tilde{M}\_{t} | =𝔼​[∫0TP~​(0,s)​Fs−1/2​ds|ℱt],\displaystyle=\mathbb{E}\left[\left.\int\_{0}^{T}\tilde{P}(0,s)\,F\_{s}^{-1/2}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right], |  | (69) |

|  |  |  |
| --- | --- | --- |
|  | DtQ=∫0tP~​(s,t)​Dsℓ​ds,Ctν=P​(t)​CtQ+Ctℓ,andDtν=P​(t)​DtQ+Dtℓ,D\_{t}^{Q}=\int\_{0}^{t}\tilde{P}(s,t)\,D\_{s}^{\ell}\,{\mathrm{d}s},\qquad C\_{t}^{\nu}=P(t)\,C\_{t}^{Q}+C\_{t}^{\ell},\qquad\text{and}\qquad D\_{t}^{\nu}=P(t)\,D\_{t}^{Q}+D\_{t}^{\ell}, |  |

where PP and P~\tilde{P} are defined in ([52](https://arxiv.org/html/2512.19838v1#S4.E52 "In Proposition 5: ‣ D No transient impact ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), and assume that the processes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tP~​(s,0)​DsQ​dM~sand∫0tP~​(s,0)​CsQ​dM~s,0≤t≤T,\int\_{0}^{t}\tilde{P}(s,0)\,D^{Q}\_{s}\,\mathrm{d}\tilde{M}\_{s}\,\qquad\text{and}\qquad\int\_{0}^{t}\tilde{P}(s,0)\,C^{Q}\_{s}\,\mathrm{d}\tilde{M}\_{s}\,,\quad 0\leq t\leq T\,, |  | (70) |

are martingales. Then the equilibrium supply of liquidity is

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ⋆=(κ¯+𝔄ϕ​𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt])​𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt]𝔅+𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt],\displaystyle\kappa^{\star}=\left(\underline{\kappa}+\frac{\mathfrak{A}}{\phi\,\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]}\right)\frac{\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]}{\mathfrak{B}+\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]}\,, |  | (71) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝔄=𝔼​[∫0T(CtQ+F0−1/2)​At​Ft​dt],𝔅=𝔼​[∫0T(CtQ+F0−1/2)​(Ft−1/2−F0−1/2)​dt].\mathfrak{A}=\mathbb{E}\left[\int\_{0}^{T}\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,A\_{t}\,F\_{t}\,{\mathrm{d}t}\right]\,,\quad\mathfrak{B}=\mathbb{E}\left[\int\_{0}^{T}\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)\,{\mathrm{d}t}\right]\,. |  |

In particular,

|  |  |  |
| --- | --- | --- |
|  | 𝔅+𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt]≥0.\quad\mathfrak{B}+\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]\geq 0. |  |

Appendix [A.K](https://arxiv.org/html/2512.19838v1#S1.SS11 "K Proof of Proposition 8 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

The next result shows that Proposition [8](https://arxiv.org/html/2512.19838v1#Thmproposition8 "Proposition 8: ‣ B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") applies to the popular case in which the private signal AA follows an Ornstein–Uhlenbeck process with dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​At=θ​(μ−At)​d​t+ξ​d​Wt.\mathrm{d}A\_{t}=\theta\,(\mu-A\_{t})\,dt+\xi\,dW\_{t}\,. |  | (72) |

###### Lemma 4:

The processes defined in ([70](https://arxiv.org/html/2512.19838v1#S6.E70 "In Proposition 8: ‣ B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) are martingales if AA is an Ornstein-Uhlenbeck process with dynamics ([72](https://arxiv.org/html/2512.19838v1#S6.E72 "In B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")).

Appendix [A.L](https://arxiv.org/html/2512.19838v1#S1.SS12 "L Proof of Lemma 4 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

The equilibrium liquidity supply ([71](https://arxiv.org/html/2512.19838v1#S6.E71 "In Proposition 8: ‣ B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) takes the liquidity level ([67](https://arxiv.org/html/2512.19838v1#S6.E67 "In Proposition 8: ‣ B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) as a reference, adjusts it upward or downward depending on the value of the private signal, and then applies a scaling that depends on the ratio β\beta of risk aversion to trading costs. The dependence of liquidity supply on β\beta, trading costs η\eta, volatility σ\sigma, and profitability γ\gamma is qualitatively similar to that studied in the previous section. Figure [4](https://arxiv.org/html/2512.19838v1#S6.F4 "Figure 4 ‣ B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") considers the simple case of constant signal AA and examines how equilibrium liquidity supply varies with the LP’s private information.

![Refer to caption](x5.png)


Figure 4: Top panels plot the equilibrium liquidity supply κ⋆\kappa^{\star} in ([71](https://arxiv.org/html/2512.19838v1#S6.E71 "In Proposition 8: ‣ B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) as a function of the constant signal AA (black curves), together with the equilibrium liquidity supply κ⋆\kappa^{\star} evaluated at A=0A=0 (blue curves). The bottom panels show the equilibrium distribution of payoffs from DEX liquidity provision. The left panels correspond to a ratio of aversion to CEX trading costs β=10−2\beta=10^{-2}, the middle panels to β=1\beta=1, and the right panels to β=100\beta=100. Default parameter values are: fundamental volatility σ=0.2\sigma=0.2, investment horizon T=1T=1, CEX trading cost η=10−6\eta=10^{-6}, and profitability γ=0.2\gamma=0.2. The distributions in the bottom panels are obtained from 20002000 market simulations, with the time interval discretised into 10001000 steps.

Figure [4](https://arxiv.org/html/2512.19838v1#S6.F4 "Figure 4 ‣ B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") shows that, counterintuitively, private information does not systematically lead to higher performance or deeper markets. For moderate positive values of the fundamental price drift, the LP anticipates that, in addition to fee revenue, the positive drift will improve performance, and therefore increases liquidity supply relative to the zero-drift benchmark. However, for large absolute values of the signal, the LP anticipates that replicating the position in the CEX will require more intensive trading and generate higher trading costs. Anticipating these costs, she reduces her liquidity supply.

The extent of this reduction increases with the ratio β\beta, as illustrated in Figure [4](https://arxiv.org/html/2512.19838v1#S6.F4 "Figure 4 ‣ B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"). When β\beta is large, equilibrium liquidity supply is lower and the LP anticipates reduced CEX trading activity. As a result, the range of signal values AA for which liquidity supply exceeds the reference level widens.

## VII Conclusions

This paper builds a structural model of liquidity provision in DEXs in which arbitrageurs align DEX prices with fundamentals, thereby generating adverse selection losses for LPs, while noise and elastic demand generates fee revenue. We show that, once trading volumes and liquidity supply are endogenised, the losses and risks borne by liquidity providers are not summarised by any single measure. Instead, they depend on (i) market conditions, including CEX liquidity depth, fundamental volatility, and noise trading activity, and on (ii) the LP’s risk aversion, which ultimately shapes the distribution of returns from DEX liquidity provision.

## A Proofs

### A Proof of Lemma [1](https://arxiv.org/html/2512.19838v1#Thmlemma1 "Lemma 1: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

For each q∈ℝq\in\mathbb{R}, consider the exponential martingale M​(q)=(M​(q)t)t≥0M(q)=(M(q)\_{t})\_{t\geq 0}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​(q)t:=eq​σ​Wt−12​q2​σ2​t,M(q)\_{t}:=e^{q\,\sigma\,W\_{t}-\tfrac{1}{2}\,q^{2}\,\sigma^{2}\,t}, |  | (A73) |

and write

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ftq=F0q​e12​(q2−q)​σ2​t​eq​∫0tAs​ds​M​(q)t.F\_{t}^{q}=F\_{0}^{q}\,e^{\tfrac{1}{2}\,(q^{2}-q)\,\sigma^{2}\,t}\;e^{q\int\_{0}^{t}A\_{s}\,{\mathrm{d}s}}\,M(q)\_{t}\,. |  | (A74) |

By Cauchy-Schwarz inequality, Doob’s inequality, and Assumption [2](https://arxiv.org/html/2512.19838v1#Thmassume2 "Assumption 2: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")-1, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[supt≤TFtq]\displaystyle\mathbb{E}\left[\sup\_{t\leq T}F\_{t}^{q}\right] | ≤F0q​e12​|q2−q|​σ2​T​𝔼​[e|q|​∫0T|As|​ds​supt≤TM​(q)t]\displaystyle\leq F\_{0}^{q}\,e^{\tfrac{1}{2}\,|q^{2}-q|\,\sigma^{2}\,T}\,\mathbb{E}\left[e^{|q|\int\_{0}^{T}|A\_{s}|\,{\mathrm{d}s}}\;\sup\_{t\leq T}M(q)\_{t}\right] |  | (A75) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤F0q​e12​|q2−q|​σ2​T​𝔼​[e2​|q|​∫0T|As|​ds]1/2​𝔼​[supt≤T(M​(q)t)2]1/2\displaystyle\leq F\_{0}^{q}\,e^{\tfrac{1}{2}\,|q^{2}-q|\,\sigma^{2}\,T}\,\mathbb{E}\left[e^{2\,|q|\int\_{0}^{T}|A\_{s}|\,{\mathrm{d}s}}\right]^{1/2}\,\mathbb{E}\left[\sup\_{t\leq T}(M(q)\_{t})^{2}\right]^{1/2} |  | (A76) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤2​F0q​e12​|q2−q|​σ2​T​𝔼​[e2​|q|​∫0T|As|​ds]1/2​𝔼​[(M​(q)T)2]1/2\displaystyle\leq 2\,F\_{0}^{q}\,e^{\tfrac{1}{2}\,|q^{2}-q|\,\sigma^{2}\,T}\,\mathbb{E}\left[e^{2\,|q|\int\_{0}^{T}|A\_{s}|\,{\mathrm{d}s}}\right]^{1/2}\,\mathbb{E}\left[(M(q)\_{T})^{2}\right]^{1/2} |  | (A77) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤2​F0q​e12​(|q2−q|+q2)​σ2​T​𝔼​[e2​|q|​∫0T|As|​ds]1/2\displaystyle\leq 2\,F\_{0}^{q}\,e^{\tfrac{1}{2}\,(|q^{2}-q|+q^{2})\,\sigma^{2}\,T}\,\mathbb{E}\left[e^{2\,|q|\int\_{0}^{T}|A\_{s}|\,{\mathrm{d}s}}\right]^{1/2} |  | (A78) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <∞\displaystyle<\infty |  | (A79) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0TFtq​dt]≤T​𝔼​[supt≤TFtq]<∞.\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{q}\,{\mathrm{d}t}\right]\leq T\,\mathbb{E}\left[\sup\_{t\leq T}F\_{t}^{q}\right]<\infty\,. |  | (A80) |

By Assumption [2](https://arxiv.org/html/2512.19838v1#Thmassume2 "Assumption 2: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")-2, we obtain, for all q∈[1,∞)q\in[1,\infty),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[supt≤TYtq]=𝔼​[supt≤Th​(Ft,κ)q]\displaystyle\mathbb{E}\left[\sup\_{t\leq T}Y\_{t}^{q}\right]=\mathbb{E}\left[\sup\_{t\leq T}h(F\_{t},\kappa)^{q}\right] | ≤Cκq​𝔼​[supt≤T(Ftqκ+Ftpκ)q]\displaystyle\leq C\_{\kappa}^{q}\,\mathbb{E}\left[\sup\_{t\leq T}\left(F\_{t}^{q\_{\kappa}}+F\_{t}^{p\_{\kappa}}\right)^{q}\right] |  | (A81) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤Cκq​ 2q−1​(𝔼​[supt≤TFtqκ​q]+𝔼​[supt≤TFtpκ​q])\displaystyle\leq C\_{\kappa}^{q}\,2^{q-1}\,\left(\mathbb{E}\left[\sup\_{t\leq T}F\_{t}^{q\_{\kappa}\,q}\right]+\mathbb{E}\left[\sup\_{t\leq T}F\_{t}^{p\_{\kappa}\,q}\right]\right) |  | (A82) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <∞.\displaystyle<\infty\,. |  | (A83) |

Moreover, we also obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0tYtq​dt]≤T​𝔼​[supt≤TYtq]<∞.\mathbb{E}\left[\int\_{0}^{t}Y\_{t}^{q}\,{\mathrm{d}t}\right]\leq T\,\mathbb{E}\left[\sup\_{t\leq T}Y\_{t}^{q}\right]<\infty\,. |  | (A84) |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[∫0T|Gt|q​dt]\displaystyle\mathbb{E}\left[\int\_{0}^{T}|G\_{t}|^{q}\,{\mathrm{d}t}\right] | =𝔼​[∫0T|∂1h​(Ft,κ)​At+σ22​∂11h​(Ft,κ)​Ft|q​dt]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left|\partial\_{1}h(F\_{t},\kappa)\,A\_{t}+\tfrac{\sigma^{2}}{2}\,\partial\_{11}h(F\_{t},\kappa)\,F\_{t}\right|^{q}\,{\mathrm{d}t}\right] |  | (A85) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≲𝔼​[∫0T(Ftqκ​q+Ftpκ​q)​|At|q​dt+∫0T(Ftqκ​q+q+Ftpκ​q+q)​dt]\displaystyle\lesssim\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{q\_{\kappa}\,q}+F\_{t}^{p\_{\kappa}\,q}\right)\,|A\_{t}|^{q}\,{\mathrm{d}t}+\int\_{0}^{T}\left(F\_{t}^{q\_{\kappa}\,q+q}+F\_{t}^{p\_{\kappa}\,q+q}\right)\,{\mathrm{d}t}\right] |  | (A86) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≲𝔼​[∫0T(Ftp​qκ​qp−q+Ftp​pκ​qp−q)​dt]p−qp​𝔼​[∫0T|At|p​dt]qp+𝔼​[∫0T(Ftqκ​q+q+Ftpκ​q+q)​dt]\displaystyle\lesssim\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{\tfrac{p\,q\_{\kappa}\,q}{p-q}}+F\_{t}^{\tfrac{p\,p\_{\kappa}\,q}{p-q}}\right)\,{\mathrm{d}t}\right]^{\tfrac{p-q}{p}}\,\mathbb{E}\left[\int\_{0}^{T}|A\_{t}|^{p}\,{\mathrm{d}t}\right]^{\tfrac{q}{p}}+\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{q\_{\kappa}\,q+q}+F\_{t}^{p\_{\kappa}\,q+q}\right)\,{\mathrm{d}t}\right] |  | (A87) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <∞,∀q∈[1,p).\displaystyle<\infty\,,\quad\forall q\in[1,p)\,. |  | (A88) |

∎

### B Proof of Lemma [3](https://arxiv.org/html/2512.19838v1#Thmlemma3 "Lemma 3: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

The proof proceeds in four steps. First, we show that the performance criterion ([29](https://arxiv.org/html/2512.19838v1#S4.E29 "In B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) is well-defined and continuous. Next, we show that the functional JJ in ([39](https://arxiv.org/html/2512.19838v1#S4.E39 "In Lemma 3: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) is also well-defined and continuous. Next, we show that the performance criterion ([29](https://arxiv.org/html/2512.19838v1#S4.E29 "In B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) and JJ in ([39](https://arxiv.org/html/2512.19838v1#S4.E39 "In Lemma 3: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) agree up to a constant on bounded processes. Finally, we conclude.

Step 1. First, we show that the performance criterion ([29](https://arxiv.org/html/2512.19838v1#S4.E29 "In B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) is well-defined and continuous. Take ν∈𝒜2\nu\in{\mathcal{A}}\_{2}. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|QTν|2]=𝔼​[|Q0+∫0Tνt​dt|2]≤2​(|Q0|2+T​𝔼​[∫0T|νt|2​dt])<∞\mathbb{E}\!\left[\left|Q^{\nu}\_{T}\right|^{2}\right]=\mathbb{E}\!\left[\left|Q\_{0}+\int\_{0}^{T}\nu\_{t}\,{\mathrm{d}t}\right|^{2}\right]\leq 2\,\left(|Q\_{0}|^{2}+T\,\mathbb{E}\!\left[\int\_{0}^{T}|\nu\_{t}|^{2}\,{\mathrm{d}t}\right]\right)<\infty |  | (A89) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|ITν|2]=𝔼​[|c​∫0Teβ​(t−T)​νt​dt|2]≤c2​T​𝔼​[∫0T|νt|2​dt]<∞.\displaystyle\mathbb{E}\!\left[\left|I^{\nu}\_{T}\right|^{2}\right]=\mathbb{E}\!\left[\left|c\int\_{0}^{T}e^{\beta\,(t-T)}\,\nu\_{t}\,{\mathrm{d}t}\right|^{2}\right]\leq c^{2}\,T\,\mathbb{E}\!\left[\int\_{0}^{T}|\nu\_{t}|^{2}\,{\mathrm{d}t}\right]<\infty\,. |  | (A90) |

These estimates together with Lemma [1](https://arxiv.org/html/2512.19838v1#Thmlemma1 "Lemma 1: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") and Cauchy-Schwarz inequality imply

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(YT+QTν)​STν]\mathbb{E}\!\left[\left(Y\_{T}+Q^{\nu}\_{T}\right)\,S^{\nu}\_{T}\right] |  | (A91) |

is well-defined. Because ([29](https://arxiv.org/html/2512.19838v1#S4.E29 "In B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(YT+QTν)​STν]−η​‖ν‖2−⟨ℑ​ν,ν⟩−ϕ2​‖𝔔​ν‖2−⟨F,ν⟩−ϕ​⟨Y,𝔔​ν⟩−ϕ2​‖Y‖2,\displaystyle\mathbb{E}\!\left[\left(Y\_{T}+Q^{\nu}\_{T}\right)\,S^{\nu}\_{T}\right]-\eta\,\|\nu\|^{2}-\langle\mathfrak{I}\nu,\nu\rangle-\frac{\phi}{2}\,\|\mathfrak{Q}\nu\|^{2}-\langle F,\nu\rangle-\phi\,\langle Y,\mathfrak{Q}\nu\rangle-\frac{\phi}{2}\,\|Y\|^{2}\,, |  | (A92) |

where Y∈𝒜2Y\in{\mathcal{A}}\_{2} by Lemma [1](https://arxiv.org/html/2512.19838v1#Thmlemma1 "Lemma 1: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") and 𝔔\mathfrak{Q} and ℑ\mathfrak{I} are bounded linear operators on 𝒜2{\mathcal{A}}\_{2}, it is well-defined.

Write

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν↦−η​‖ν‖2−⟨ℑ​ν,ν⟩−ϕ2​‖𝔔​ν‖2−⟨F,ν⟩−ϕ​⟨Y,𝔔​ν⟩\nu\mapsto-\eta\,\|\nu\|^{2}-\langle\mathfrak{I}\nu,\nu\rangle-\frac{\phi}{2}\,\|\mathfrak{Q}\nu\|^{2}-\langle F,\nu\rangle-\phi\,\langle Y,\mathfrak{Q}\nu\rangle |  | (A93) |

is a linear-quadratic form on 𝒜2{\mathcal{A}}\_{2}, it is continuous, it remains to show 𝔼​[(YT+QTν)​STν]\mathbb{E}\!\left[\left(Y\_{T}+Q^{\nu}\_{T}\right)\,S^{\nu}\_{T}\right] is continuos in ν\nu. To that end, take ν(n)→ν\nu^{(n)}\to\nu in 𝒜2{\mathcal{A}}\_{2}. Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |𝔼​[YT​(ITν(n)−ITν)]|\displaystyle\left|\mathbb{E}\left[Y\_{T}\,\left(I^{\nu^{(n)}}\_{T}-I^{\nu}\_{T}\right)\right]\right| | ≤𝔼​[|YT|2]1/2​𝔼​[|ITν(n)−ITν|2]1/2\displaystyle\leq\mathbb{E}\left[|Y\_{T}|^{2}\right]^{1/2}\,\mathbb{E}\left[\left|I^{\nu^{(n)}}\_{T}-I^{\nu}\_{T}\right|^{2}\right]^{1/2} |  | (A94) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤c​T​𝔼​[|YT|]1/2​𝔼​[∫0T|νt(n)−νt|2​dt]1/2,\displaystyle\leq c\,\sqrt{T}\,\mathbb{E}\left[|Y\_{T}|\right]^{1/2}\,\mathbb{E}\left[\int\_{0}^{T}\left|\nu^{(n)}\_{t}-\nu\_{t}\right|^{2}\,{\mathrm{d}t}\right]^{1/2}\,, |  | (A95) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |𝔼​[FT​(QTν(n)−QTν)]|\displaystyle\left|\mathbb{E}\left[F\_{T}\,\left(Q^{\nu^{(n)}}\_{T}-Q^{\nu}\_{T}\right)\right]\right| | ≤𝔼​[|FT|2]1/2​𝔼​[|QTν(n)−QTν|2]1/2\displaystyle\leq\mathbb{E}\left[|F\_{T}|^{2}\right]^{1/2}\,\mathbb{E}\left[\left|Q^{\nu^{(n)}}\_{T}-Q^{\nu}\_{T}\right|^{2}\right]^{1/2} |  | (A96) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤2​T​𝔼​[|FT|]1/2​𝔼​[∫0T|νt(n)−νt|2​dt]1/2,\displaystyle\leq\sqrt{2\,T}\,\mathbb{E}\left[|F\_{T}|\right]^{1/2}\,\mathbb{E}\left[\int\_{0}^{T}\left|\nu^{(n)}\_{t}-\nu\_{t}\right|^{2}\,{\mathrm{d}t}\right]^{1/2}\,, |  | (A97) |

and, by Minkwoski’s inequality

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |𝔼​[QTν(n)​ITν(n)−QTν​ITν]|\displaystyle\left|\mathbb{E}\left[Q^{\nu^{(n)}}\_{T}\,I^{\nu^{(n)}}\_{T}-Q^{\nu}\_{T}\,I^{\nu}\_{T}\right]\right| | =|𝔼​[QTν(n)​(ITν(n)−ITν)+(QTν(n)−QTν)​ITν]|\displaystyle=\left|\mathbb{E}\left[Q^{\nu^{(n)}}\_{T}\,\left(I^{\nu^{(n)}}\_{T}-I^{\nu}\_{T}\right)+\left(Q^{\nu^{(n)}}\_{T}-Q^{\nu}\_{T}\right)\,I^{\nu}\_{T}\right]\right| |  | (A98) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤𝔼​[|QTν(n)|2]1/2​𝔼​[|ITν(n)−ITν|2]1/2+𝔼​[|QTν(n)−QTν|2]1/2​𝔼​[|ITν|2]1/2\displaystyle\leq\mathbb{E}\left[\left|Q^{\nu^{(n)}}\_{T}\right|^{2}\right]^{1/2}\,\mathbb{E}\left[\left|I^{\nu^{(n)}}\_{T}-I^{\nu}\_{T}\right|^{2}\right]^{1/2}+\mathbb{E}\left[\left|Q^{\nu^{(n)}}\_{T}-Q^{\nu}\_{T}\right|^{2}\right]^{1/2}\,\mathbb{E}\left[\left|I^{\nu}\_{T}\right|^{2}\right]^{1/2} |  | (A99) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤(𝔼​[|QTν(n)−QTν|2]1/2+𝔼​[|QTν|2]1/2)​𝔼​[|ITν(n)−ITν|2]1/2\displaystyle\leq\left(\mathbb{E}\left[\left|Q^{\nu^{(n)}}\_{T}-Q^{\nu}\_{T}\right|^{2}\right]^{1/2}+\mathbb{E}\left[\left|Q^{\nu}\_{T}\right|^{2}\right]^{1/2}\right)\,\mathbb{E}\left[\left|I^{\nu^{(n)}}\_{T}-I^{\nu}\_{T}\right|^{2}\right]^{1/2} |  | (A100) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝔼​[|QTν(n)−QTν|2]1/2​𝔼​[|ITν|2]1/2\displaystyle\quad\ +\mathbb{E}\left[\left|Q^{\nu^{(n)}}\_{T}-Q^{\nu}\_{T}\right|^{2}\right]^{1/2}\,\mathbb{E}\left[\left|I^{\nu}\_{T}\right|^{2}\right]^{1/2} |  | (A101) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤2​c​T​𝔼​[∫0T|νt(n)−νt|2​dt]+c​T​𝔼​[|QTν|2]1/2​𝔼​[∫0T|νt(n)−νt|2​dt]1/2\displaystyle\leq\sqrt{2}\,c\,T\,\mathbb{E}\left[\int\_{0}^{T}\left|\nu^{(n)}\_{t}-\nu\_{t}\right|^{2}\,{\mathrm{d}t}\right]+\,c\,\sqrt{T}\,\mathbb{E}\left[\left|Q^{\nu}\_{T}\right|^{2}\right]^{1/2}\,\mathbb{E}\left[\int\_{0}^{T}\left|\nu^{(n)}\_{t}-\nu\_{t}\right|^{2}\,{\mathrm{d}t}\right]^{1/2} |  | (A102) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2​T​𝔼​[∫0T|νt(n)−νt|2​dt]1/2​𝔼​[|ITν|2]1/2.\displaystyle\quad\ +\sqrt{2\,T}\,\mathbb{E}\left[\int\_{0}^{T}\left|\nu^{(n)}\_{t}-\nu\_{t}\right|^{2}\,{\mathrm{d}t}\right]^{1/2}\,\mathbb{E}\left[\left|I^{\nu}\_{T}\right|^{2}\right]^{1/2}\,. |  | (A103) |

These estimates imply 𝔼​[(YT+QTν)​STν]\mathbb{E}\!\left[\left(Y\_{T}+Q^{\nu}\_{T}\right)\,S^{\nu}\_{T}\right] is continuous in ν\nu, as desired.

Step 2. Next, we show that JJ is well-defined and continuous. Because 𝔔\mathfrak{Q} and ℑ\mathfrak{I} are bounded linear operators on 𝒜2{\mathcal{A}}\_{2}, the quadratic form 𝒬\mathcal{Q} is well-defined and continuous. Because we know F∈𝒜2F\in{\mathcal{A}}\_{2} by Lemma [1](https://arxiv.org/html/2512.19838v1#Thmlemma1 "Lemma 1: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"), it remains to show the processes G​FG\,F and A​FA\,F are in 𝒜2{\mathcal{A}}\_{2}. Indeed, if q∈(2,p)q\in(2,p), then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[∫0T|Gt​Ft|2​dt]\displaystyle\mathbb{E}\!\left[\int\_{0}^{T}\left|G\_{t}\,F\_{t}\right|^{2}\,{\mathrm{d}t}\right] | ≤𝔼​[∫0T|Gt|q​dt]2q​𝔼​[∫0TFt2​qq−2​dt]q−2q<∞\displaystyle\leq\mathbb{E}\!\left[\int\_{0}^{T}\left|G\_{t}\right|^{q}\,{\mathrm{d}t}\right]^{\tfrac{2}{q}}\,\mathbb{E}\!\left[\int\_{0}^{T}F\_{t}^{\tfrac{2\,q}{q-2}}\,{\mathrm{d}t}\right]^{\tfrac{q-2}{q}}<\infty |  | (A104) |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[∫0T|At​Ft|2​dt]\displaystyle\mathbb{E}\!\left[\int\_{0}^{T}\left|A\_{t}\,F\_{t}\right|^{2}\,{\mathrm{d}t}\right] | ≤𝔼​[∫0T|At|p​dt]2p​𝔼​[∫0TFt2​pp−2​dt]p−2p<∞,\displaystyle\leq\mathbb{E}\!\left[\int\_{0}^{T}\left|A\_{t}\right|^{p}\,{\mathrm{d}t}\right]^{\tfrac{2}{p}}\,\mathbb{E}\!\left[\int\_{0}^{T}F\_{t}^{\tfrac{2\,p}{p-2}}\,{\mathrm{d}t}\right]^{\tfrac{p-2}{p}}<\infty\,, |  | (A105) |

by Lemma [1](https://arxiv.org/html/2512.19838v1#Thmlemma1 "Lemma 1: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets").

Step 3. Next, we show that the performance criterion ([29](https://arxiv.org/html/2512.19838v1#S4.E29 "In B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) and JJ in ([39](https://arxiv.org/html/2512.19838v1#S4.E39 "In Lemma 3: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) agree up to a constant on bounded processes. Take ν∈𝒜2\nu\in{\mathcal{A}}\_{2} such that |ν|≤N|\nu|\leq N for some constant NN. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Qtν|=|Q0+∫0tνs​ds|≤|Q0|+T​N\left|Q^{\nu}\_{t}\right|=\left|Q\_{0}+\int\_{0}^{t}\nu\_{s}\,{\mathrm{d}s}\right|\leq|Q\_{0}|+T\,N |  | (A106) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Itν|=|c​∫0teβ​(s−t)​νs​ds|≤c​T​N,.\left|I^{\nu}\_{t}\right|=\left|c\,\int\_{0}^{t}e^{\beta(s-t)}\,\nu\_{s}\,{\mathrm{d}s}\right|\leq c\,T\,N,. |  | (A107) |

By Itô’s formula, ([23](https://arxiv.org/html/2512.19838v1#S4.E23 "In A Assumptions ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), ([7](https://arxiv.org/html/2512.19838v1#S2.E7 "In II General features of the model ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), ([IV.A](https://arxiv.org/html/2512.19838v1#S4.Ex5 "A Assumptions ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), and ([28](https://arxiv.org/html/2512.19838v1#S4.E28 "In B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (YT+QTν)​STν\displaystyle(Y\_{T}+Q\_{T}^{\nu})\,S\_{T}^{\nu} | =(Y0+Q0)​F0+∫0T(Yt+Qtν)​dStν+∫0TStν​dYt+∫0TStν​dQtν+∫0Td​⟨Y,F⟩t\displaystyle=(Y\_{0}+Q\_{0})\,F\_{0}+\int\_{0}^{T}(Y\_{t}+Q^{\nu}\_{t})\,\mathrm{d}S^{\nu}\_{t}+\int\_{0}^{T}S^{\nu}\_{t}\,\mathrm{d}Y\_{t}+\int\_{0}^{T}S^{\nu}\_{t}\,\mathrm{d}Q^{\nu}\_{t}+\int\_{0}^{T}\mathrm{d}\langle Y,F\rangle\_{t} |  | (A108) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(Y0+Q0)​F0+∫0T(Yt+Qtν)​(At​Ft+c​νt−β​Itν)​dt\displaystyle=(Y\_{0}+Q\_{0})\,F\_{0}+\int\_{0}^{T}(Y\_{t}+Q^{\nu}\_{t})\,(A\_{t}\,F\_{t}+c\,\nu\_{t}-\beta\,I^{\nu}\_{t}){\mathrm{d}t} |  | (A109) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫0T(Ft+Itν)​Gt​Ft​dt+∫0TStν​νt​dt+∫0Tσ2​∂1h​(Ft,κ)​Ft2​d​t\displaystyle\quad+\int\_{0}^{T}(F\_{t}+I^{\nu}\_{t})\,G\_{t}\,F\_{t}\,{\mathrm{d}t}+\int\_{0}^{T}S^{\nu}\_{t}\,\nu\_{t}\,{\mathrm{d}t}+\int\_{0}^{T}\sigma^{2}\,\partial\_{1}h(F\_{t},\kappa)\,F\_{t}^{2}\,{\mathrm{d}t} |  | (A110) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +σ​∫0TFt​[Yt+Qtν+∂1h​(Ft,κ)​(Ft+Itν)]​dWt,\displaystyle\quad+\sigma\int\_{0}^{T}F\_{t}\,\left[Y\_{t}+Q^{\nu}\_{t}+\partial\_{1}h(F\_{t},\kappa)\,(F\_{t}+I^{\nu}\_{t})\right]\,\mathrm{d}W\_{t}\,, |  | (A111) |

so

|  |  |  |  |
| --- | --- | --- | --- |
|  | (YT+QTν)​STν−∫0T(Stν+η​νt)​νt​dt−ϕ2​∫0T(Qtν+Yt)2​dt\displaystyle\left(Y\_{T}+Q\_{T}^{\nu}\right)\,S\_{T}^{\nu}-\int\_{0}^{T}\left(S\_{t}^{\nu}+\eta\,\nu\_{t}\right)\,\nu\_{t}\,{\mathrm{d}t}-\tfrac{\phi}{2}\int\_{0}^{T}\left(Q\_{t}^{\nu}+Y\_{t}\right)^{2}\,{\mathrm{d}t} |  | (A112) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =(Y0+Q0)​F0+∫0T{(Gt+σ2​∂1h​(Ft,κ))​Ft2+(Yt+Q0)​At​Ft−ϕ2​(Yt+Q0)2}​dt\displaystyle=(Y\_{0}+Q\_{0})\,F\_{0}+\int\_{0}^{T}\left\{\left(G\_{t}+\sigma^{2}\,\partial\_{1}h(F\_{t},\kappa)\right)\,F\_{t}^{2}+(Y\_{t}+Q\_{0})\,A\_{t}\,F\_{t}-\tfrac{\phi}{2}\,(Y\_{t}+Q\_{0})^{2}\right\}\,{\mathrm{d}t} |  | (A113) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +∫0T{Itν​Gt​Ft−η​νt2+(Yt+Qtν)​(c​νt−β​Itν)+(At​Ft−ϕ​(Yt+Q0))​(Qtν−Q0)−ϕ2​(Qtν−Q0)2}​dt\displaystyle\quad+\int\_{0}^{T}\left\{I^{\nu}\_{t}\,G\_{t}\,F\_{t}-\eta\,\nu\_{t}^{2}+\left(Y\_{t}+Q\_{t}^{\nu}\right)\,\left(c\,\nu\_{t}-\beta\,I\_{t}^{\nu}\right)+\left(A\_{t}\,F\_{t}-\phi\,(Y\_{t}+Q\_{0})\right)\,\left(Q^{\nu}\_{t}-Q\_{0}\right)-\tfrac{\phi}{2}\,\left(Q\_{t}^{\nu}-Q\_{0}\right)^{2}\right\}\,{\mathrm{d}t} |  | (A114) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +σ​∫0TFt​[Yt+Qtν+∂1h​(Ft,κ)​(Ft+Itν)]​dWt,\displaystyle\quad+\sigma\int\_{0}^{T}F\_{t}\,\left[Y\_{t}+Q^{\nu}\_{t}+\partial\_{1}h(F\_{t},\kappa)\,(F\_{t}+I^{\nu}\_{t})\right]\,\mathrm{d}W\_{t}\,, |  | (A115) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|(Gt+σ2​∂1h​(Ft,κ))​Ft2+(Yt+Q0)​At​Ft−ϕ2​(Yt+Q0)2|​dt]<∞.\displaystyle\mathbb{E}\left[\int\_{0}^{T}\left|\left(G\_{t}+\sigma^{2}\,\partial\_{1}h(F\_{t},\kappa)\right)\,F\_{t}^{2}+(Y\_{t}+Q\_{0})\,A\_{t}\,F\_{t}-\tfrac{\phi}{2}\,(Y\_{t}+Q\_{0})^{2}\right|\,{\mathrm{d}t}\right]<\infty\,. |  | (A116) |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0TFt2​|Yt+Qtν+∂1h​(Ft,κ)​(Ft+Itν)|2​dt]\displaystyle\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{2}\,\left|Y\_{t}+Q^{\nu}\_{t}+\partial\_{1}h(F\_{t},\kappa)\,(F\_{t}+I^{\nu}\_{t})\right|^{2}\,{\mathrm{d}t}\right] |  | (A117) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≲𝔼​[∫0TFt2​(Yt2+|Qtν|2+|∂1h​(Ft,κ)|2​(Ft2+|Itν|2))​dt]\displaystyle\lesssim\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{2}\,\left(Y\_{t}^{2}+|Q^{\nu}\_{t}|^{2}+|\partial\_{1}h(F\_{t},\kappa)|^{2}\,\left(F\_{t}^{2}+|I^{\nu}\_{t}|^{2}\right)\right)\,{\mathrm{d}t}\right] |  | (A118) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≲𝔼​[∫0TFt2​(Yt2+(|Q0|+T​N)2+(Ft2​qκ+Ft2​pκ)​(Ft2+c2​T2​N2))​dt]\displaystyle\lesssim\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{2}\,\left(Y\_{t}^{2}+(|Q\_{0}|+T\,N)^{2}+\left(F\_{t}^{2\,q\_{\kappa}}+F\_{t}^{2\,p\_{\kappa}}\right)\,\left(F\_{t}^{2}+c^{2}\,T^{2}\,N^{2}\right)\right)\,{\mathrm{d}t}\right] |  | (A119) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | <∞,\displaystyle<\infty\,, |  | (A120) |

the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tFt​[Yt+Qtν+∂1h​(Ft,κ)​(Ft+Itν)]​dWt,0≤t≤T,\int\_{0}^{t}F\_{t}\,\left[Y\_{t}+Q^{\nu}\_{t}+\partial\_{1}h(F\_{t},\kappa)\,(F\_{t}+I^{\nu}\_{t})\right]\,\mathrm{d}W\_{t}\,,\quad 0\leq t\leq T\,, |  | (A121) |

is a martingale, so

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0TFt​[Yt+Qtν+∂1h​(Ft,κ)​(Ft+Itν)]​dWt]=0.\mathbb{E}\left[\int\_{0}^{T}F\_{t}\,\left[Y\_{t}+Q^{\nu}\_{t}+\partial\_{1}h(F\_{t},\kappa)\,(F\_{t}+I^{\nu}\_{t})\right]\,\mathrm{d}W\_{t}\right]=0\,. |  | (A122) |

It follows that we may rewrite the performance criterion ([29](https://arxiv.org/html/2512.19838v1#S4.E29 "In B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Y0+Q0)​F0+[∫0T{(Gt+σ2​∂1h​(Ft,κ))​Ft2+(Yt+Q0)​At​Ft−ϕ2​(Yt+Q0)2}​dt]+J​[ν].\displaystyle(Y\_{0}+Q\_{0})\,F\_{0}+\left[\int\_{0}^{T}\left\{\left(G\_{t}+\sigma^{2}\,\partial\_{1}h(F\_{t},\kappa)\right)\,F\_{t}^{2}+(Y\_{t}+Q\_{0})\,A\_{t}\,F\_{t}-\tfrac{\phi}{2}\,(Y\_{t}+Q\_{0})^{2}\right\}\,{\mathrm{d}t}\right]+J[\nu]\,. |  | (A123) |

Step 4. Because bounded processes are dense in 𝒜2{\mathcal{A}}\_{2}, by continuity, ([A123](https://arxiv.org/html/2512.19838v1#S1.E123 "In B Proof of Lemma 3 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) holds for all ν∈𝒜2\nu\in{\mathcal{A}}\_{2}.
∎

### C Proof of Proposition [1](https://arxiv.org/html/2512.19838v1#Thmproposition1 "Proposition 1: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

Consider the quadratic form 𝒬\mathcal{Q} and the linear functional ℒ\mathcal{L} defined in Lemma [3](https://arxiv.org/html/2512.19838v1#Thmlemma3 "Lemma 3: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"). Define the symmetric bounded bilinear form B:𝒜2×𝒜2→ℝB:{\mathcal{A}}\_{2}\times{\mathcal{A}}\_{2}\to\mathbb{R} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(ν,ζ)=14​(𝒬​(ν+ζ)−𝒬​(ν−ζ)).B(\nu,\zeta)=\frac{1}{4}\,(\mathcal{Q}(\nu+\zeta)-\mathcal{Q}(\nu-\zeta))\,. |  | (A124) |

Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | B​(ν,ζ)\displaystyle B(\nu,\zeta) | =2​η​⟨ν,ζ⟩+β​(⟨𝔔​ν,ℑ​ζ⟩+⟨𝔔​ζ,ℑ​ν⟩)−c​(⟨𝔔​ν,ζ⟩+⟨𝔔​ζ,ν⟩)+ϕ​⟨𝔔​ν,𝔔​ζ⟩\displaystyle=2\,\eta\,\langle\nu,\zeta\rangle+\beta\,(\langle\mathfrak{Q}\nu,\mathfrak{I}\zeta\rangle+\langle\mathfrak{Q}\zeta,\mathfrak{I}\nu\rangle)-c\,(\langle\mathfrak{Q}\nu,\zeta\rangle+\langle\mathfrak{Q}\zeta,\nu\rangle)+\phi\,\langle\mathfrak{Q}\nu,\mathfrak{Q}\zeta\rangle |  | (A125) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​η​⟨ν,ζ⟩+β​(⟨ℑ⊤​𝔔​ν,ζ⟩+⟨ζ,𝔔⊤​ℑ​ν⟩)−c​(⟨𝔔​ν,ζ⟩+⟨ζ,𝔔⊤​ν⟩)+ϕ​⟨𝔔⊤​𝔔​ν,ζ⟩\displaystyle=2\,\eta\,\langle\nu,\zeta\rangle+\beta\,(\langle\mathfrak{I}^{\top}\mathfrak{Q}\nu,\zeta\rangle+\langle\zeta,\mathfrak{Q}^{\top}\mathfrak{I}\nu\rangle)-c\,(\langle\mathfrak{Q}\nu,\zeta\rangle+\langle\zeta,\mathfrak{Q}^{\top}\nu\rangle)+\phi\,\langle\mathfrak{Q}^{\top}\mathfrak{Q}\nu,\zeta\rangle |  | (A126) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =⟨(2​η+β​(ℑ⊤​𝔔+𝔔⊤​ℑ)−c​(𝔔+𝔔⊤)+ϕ​𝔔⊤​𝔔)​ν,ζ⟩\displaystyle=\langle(2\,\eta+\beta\,(\mathfrak{I}^{\top}\mathfrak{Q}+\mathfrak{Q}^{\top}\mathfrak{I})-c\,(\mathfrak{Q}+\mathfrak{Q}^{\top})+\phi\,\mathfrak{Q}^{\top}\mathfrak{Q})\nu,\zeta\rangle |  | (A127) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =⟨Λ​ν,ζ⟩\displaystyle=\langle\Lambda\nu,\zeta\rangle |  | (A128) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒬​(ν)=B​(ν,ν)=⟨Λ​ν,ν⟩.\mathcal{Q}(\nu)=B(\nu,\nu)=\langle\Lambda\nu,\nu\rangle\,. |  | (A129) |

For the linear functional ℒ\mathcal{L}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ(ν)=⟨(ℑ⊤(GF)+(c−βℑ⊤−ϕ𝔔⊤)+𝔔⊤(AF),ν⟩=⟨b,ν⟩.\mathcal{L}(\nu)=\langle(\mathfrak{I}^{\top}(G\,F)+(c-\beta\,\mathfrak{I}^{\top}-\phi\,\mathfrak{Q}^{\top})+\mathfrak{Q}^{\top}(A\,F),\nu\rangle=\langle b,\nu\rangle\,. |  | (A130) |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​[ν]=−12​𝒬​(ν)+ℒ​(ν)=−12​⟨Λ​ν,ν⟩+⟨b,ν⟩.J[\nu]=-\frac{1}{2}\,\mathcal{Q}(\nu)+\mathcal{L}(\nu)=-\frac{1}{2}\,\langle\Lambda\nu,\nu\rangle+\langle b,\nu\rangle\,. |  | (A131) |

∎

### D Proof of Proposition [2](https://arxiv.org/html/2512.19838v1#Thmproposition2 "Proposition 2: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

Take ν∈𝒜2\nu\in{\mathcal{A}}\_{2}. Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨Λ​ν,ν⟩=𝒬​(ν)\displaystyle\langle\Lambda\nu,\nu\rangle=\mathcal{Q}(\nu) | =2​η​‖ν‖2+2​⟨𝔔​ν,β​ℑ​ν−c​ν⟩+ϕ​‖𝔔​ν‖2\displaystyle=2\,\eta\,\|\nu\|^{2}+2\,\langle\mathfrak{Q}\nu,\beta\,\mathfrak{I}\nu-c\,\nu\rangle+\phi\,\|\mathfrak{Q}\nu\|^{2} |  | (A132) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​η​‖ν‖2−2​c​⟨𝔔​ν,ν⟩+ϕ​‖𝔔​ν‖2+2​β​⟨𝔔​ν,ℑ​ν⟩\displaystyle=2\,\eta\,\|\nu\|^{2}-2\,c\,\langle\mathfrak{Q}\nu,\nu\rangle+\phi\,\|\mathfrak{Q}\nu\|^{2}+2\,\beta\langle\mathfrak{Q}\nu,\mathfrak{I}\nu\rangle |  | (A133) |

By integration by parts, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨𝔔​ν,ν⟩=𝔼​[∫0T∫0tνs​ds​νt​dt]\displaystyle\langle\mathfrak{Q}\nu,\nu\rangle=\mathbb{E}\!\left[\int\_{0}^{T}\int\_{0}^{t}\nu\_{s}\,{\mathrm{d}s}\,\nu\_{t}\,{\mathrm{d}t}\right] | =𝔼​[(∫0Tνt​dt)2−∫0T∫0tνs​ds​νt​dt],\displaystyle=\mathbb{E}\!\left[\left(\int\_{0}^{T}\nu\_{t}\,{\mathrm{d}t}\right)^{2}-\int\_{0}^{T}\int\_{0}^{t}\nu\_{s}\,{\mathrm{d}s}\,\nu\_{t}\,{\mathrm{d}t}\right]\,, |  | (A134) |

so

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨𝔔​ν,ν⟩=12​𝔼​[(∫0Tνt​dt)2]≥0.\langle\mathfrak{Q}\nu,\nu\rangle=\frac{1}{2}\,\mathbb{E}\!\left[\left(\int\_{0}^{T}\nu\_{t}\,{\mathrm{d}t}\right)^{2}\right]\geq 0\,. |  | (A135) |

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℑ~t≔∫0teβ​(s−t)​νs​ds.\tilde{\mathfrak{I}}\_{t}\coloneqq\int\_{0}^{t}e^{\beta\,(s-t)}\,\nu\_{s}\,{\mathrm{d}s}\,. |  | (A136) |

The dynamics ([23](https://arxiv.org/html/2512.19838v1#S4.E23 "In A Assumptions ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) implies

|  |  |  |
| --- | --- | --- |
|  | c​ℑ~t=Itν=c​∫0tνs​ds−β​∫0tIsν​ds=c​(𝔔​ν)t−β​∫0tc​ℑ~s​ds,\displaystyle c\,\tilde{\mathfrak{I}}\_{t}=I^{\nu}\_{t}=c\int\_{0}^{t}\nu\_{s}\,\mathrm{d}s-\beta\int\_{0}^{t}I^{\nu}\_{s}\,\mathrm{d}s=c\,(\mathfrak{Q}\nu)\_{t}-\beta\int\_{0}^{t}c\,\tilde{\mathfrak{I}}\_{s}\,\mathrm{d}s\,, |  |

so

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(𝔔​ν)t=c​(ℑ~t+β​∫0tℑ~s​ds).\displaystyle c\,(\mathfrak{Q}\nu)\_{t}=c\,\left(\tilde{\mathfrak{I}}\_{t}+\beta\int\_{0}^{t}\tilde{\mathfrak{I}}\_{s}\,{\mathrm{d}s}\right)\,. |  | (A137) |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨𝔔​ν,ℑ​ν⟩=𝔼​[∫0T(𝔔​ν)t​(ℑ​ν)t​dt]\displaystyle\langle\mathfrak{Q}\nu,\mathfrak{I}\nu\rangle=\mathbb{E}\!\left[\int\_{0}^{T}(\mathfrak{Q}\nu)\_{t}\,(\mathfrak{I}\nu)\_{t}\,{\mathrm{d}t}\right] | =𝔼​[∫0Tc​(𝔔​ν)t​ℑ~t​dt]\displaystyle=\mathbb{E}\!\left[\int\_{0}^{T}c\,(\mathfrak{Q}\nu)\_{t}\,\tilde{\mathfrak{I}}\_{t}\,{\mathrm{d}t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c​𝔼​[∫0T(ℑ~t+β​∫0tℑ~s​ds)​ℑ~t​dt]\displaystyle=c\,\mathbb{E}\!\left[\int\_{0}^{T}\left(\tilde{\mathfrak{I}}\_{t}+\beta\int\_{0}^{t}\tilde{\mathfrak{I}}\_{s}\,{\mathrm{d}s}\right)\,\tilde{\mathfrak{I}}\_{t}\,{\mathrm{d}t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c​𝔼​[∫0Tℑ~t2​dt+β​∫0Tℑ~t​∫0tℑ~s​ds​dt]\displaystyle=c\,\mathbb{E}\!\left[\int\_{0}^{T}\tilde{\mathfrak{I}}\_{t}^{2}\,{\mathrm{d}t}+\beta\int\_{0}^{T}\tilde{\mathfrak{I}}\_{t}\int\_{0}^{t}\tilde{\mathfrak{I}}\_{s}\,\mathrm{d}s\,{\mathrm{d}t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c​(‖ℑ~‖2+β​⟨𝔔​ℑ~,ℑ~⟩)\displaystyle=c\,\left(\|\tilde{\mathfrak{I}}\|^{2}+\beta\,\left\langle\mathfrak{Q}\tilde{\mathfrak{I}},\tilde{\mathfrak{I}}\right\rangle\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥0\displaystyle\geq 0 |  |

due to ([A135](https://arxiv.org/html/2512.19838v1#S1.E135 "In D Proof of Proposition 2 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")). It follows that (recall Assumption [3](https://arxiv.org/html/2512.19838v1#Thmassume3 "Assumption 3: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨Λ​ν,ν⟩\displaystyle\langle\Lambda\nu,\nu\rangle | =2​η​‖ν‖2−2​c​⟨𝔔​ν,ν⟩+ϕ​‖𝔔​ν‖2+2​β​⟨𝔔​ν,ℑ​ν⟩\displaystyle=2\,\eta\,\|\nu\|^{2}-2\,c\,\langle\mathfrak{Q}\nu,\nu\rangle+\phi\,\|\mathfrak{Q}\nu\|^{2}+2\,\beta\langle\mathfrak{Q}\nu,\mathfrak{I}\nu\rangle |  | (A138) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥2​η​‖ν‖2−2​2​η​ϕ​⟨𝔔​ν,ν⟩+ϕ​‖𝔔​ν‖2\displaystyle\geq 2\,\eta\,\|\nu\|^{2}-2\,\sqrt{2\,\eta\,\phi}\,\langle\mathfrak{Q}\nu,\nu\rangle+\phi\,\|\mathfrak{Q}\nu\|^{2} |  | (A139) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =‖2​η​ν−ϕ​𝔔​ν‖2.\displaystyle=\left\|\sqrt{2\,\eta}\,\nu-\sqrt{\phi}\,\mathfrak{Q}\nu\right\|^{2}\,. |  | (A140) |

Consider the bounded linear operator 𝔙:L2​[0,T]→L2​[0,T]\mathfrak{V}:L^{2}[0,T]\to L^{2}[0,T] defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝔙​f)​(t)=2​η​f​(t)−ϕ​∫0tf​(s)​ds,\displaystyle(\mathfrak{V}f)(t)=\sqrt{2\,\eta}f(t)-\sqrt{\phi}\int\_{0}^{t}f(s)\,{\mathrm{d}s}\,, |  | (A141) |

whose inverse is also a bounded linear operator on L2​[0,T]L^{2}[0,T] and is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝔙−1​f)​(t)=12​η​f​(t)+ϕ2​η​∫0teϕ2​η​(t−s)​f​(s)​ds.\displaystyle(\mathfrak{V}^{-1}f)(t)=\frac{1}{\sqrt{2\,\eta}}\,f(t)+\frac{\sqrt{\phi}}{2\,\eta}\,\int\_{0}^{t}e^{\sqrt{\tfrac{\phi}{2\,\eta}}\,(t-s)}\,f(s)\,{\mathrm{d}s}\,. |  | (A142) |

Since ν​(ω)∈L2​[0,T]\nu(\omega)\in L^{2}[0,T] for ℙ\mathbb{P}-a.e. ω\omega, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖ν‖2=∫Ω‖ν​(ω)‖L2​[0,T]2​dℙ​(ω)\displaystyle\|\nu\|^{2}=\int\_{\Omega}\|\nu(\omega)\|\_{L^{2}[0,T]}^{2}\,\mathrm{d}\mathbb{P}(\omega) | =∫Ω‖𝔙−1​𝔙​(ν​(ω))‖L2​[0,T]2​dℙ​(ω)\displaystyle=\int\_{\Omega}\left\|\mathfrak{V}^{-1}\mathfrak{V}(\nu(\omega))\right\|\_{L^{2}[0,T]}^{2}\,\mathrm{d}\mathbb{P}(\omega) |  | (A143) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤∫Ω‖𝔙−1‖op2​‖𝔙​(ν​(ω))‖L2​[0,T]2​dℙ​(ω)\displaystyle\leq\int\_{\Omega}\left\|\mathfrak{V}^{-1}\right\|\_{\operatorname{op}}^{2}\,\left\|\mathfrak{V}(\nu(\omega))\right\|\_{L^{2}[0,T]}^{2}\,\mathrm{d}\mathbb{P}(\omega) |  | (A144) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =‖𝔙−1‖op2​‖2​η​ν−ϕ​𝔔​ν‖2.\displaystyle=\left\|\mathfrak{V}^{-1}\right\|\_{\operatorname{op}}^{2}\,\left\|\sqrt{2\,\eta}\,\nu-\sqrt{\phi}\,\mathfrak{Q}\nu\right\|^{2}\,. |  | (A145) |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Λ​ν,ν⟩≥‖𝔙−1‖op−2​‖ν‖2.\langle\Lambda\nu,\nu\rangle\geq\left\|\mathfrak{V}^{-1}\right\|\_{\operatorname{op}}^{-2}\,\|\nu\|^{2}\,. |  | (A146) |

so Λ\Lambda is coercive. By Lax-Milgram lemma, Λ\Lambda has an inverse, which is a bounded linear operator on 𝒜2{\mathcal{A}}\_{2}.

Next, take ν,ζ∈𝒜2\nu,\zeta\in{\mathcal{A}}\_{2} and ρ∈(0,1)\rho\in(0,1). Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J​[ρ​ν+(1−ρ)​ζ]\displaystyle J[\rho\,\nu+(1-\rho)\,\zeta] | =−12​⟨Λ​(ρ​ν+(1−ρ)​ζ),ρ​ν+(1−ρ)​ζ⟩+⟨b,ρ​ν+(1−ρ)​ζ⟩\displaystyle=-\frac{1}{2}\,\langle\Lambda(\rho\,\nu+(1-\rho)\,\zeta),\rho\,\nu+(1-\rho)\,\zeta\rangle+\langle b,\rho\,\nu+(1-\rho)\,\zeta\rangle |  | (A147) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−12​(ρ2​⟨Λ​ν,ν⟩+2​ρ​(1−ρ)​⟨Λ​ν,ζ⟩+(1−ρ)2​⟨Λ​ζ,ζ⟩)+ρ​⟨b,ν⟩+(1−ρ)​⟨b,ζ⟩\displaystyle=-\frac{1}{2}\left(\rho^{2}\,\langle\Lambda\nu,\nu\rangle+2\,\rho\,(1-\rho)\,\langle\Lambda\nu,\zeta\rangle+(1-\rho)^{2}\,\langle\Lambda\zeta,\zeta\rangle\right)+\rho\,\langle b,\nu\rangle+(1-\rho)\,\langle b,\zeta\rangle |  | (A148) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−12​((ρ2−ρ)​⟨Λ​ν,ν⟩+2​ρ​(1−ρ)​⟨Λ​ν,ζ⟩+((1−ρ)2−(1−ρ))​⟨Λ​ζ,ζ⟩)\displaystyle=-\frac{1}{2}\left(\left(\rho^{2}-\rho\right)\,\langle\Lambda\nu,\nu\rangle+2\,\rho\,(1-\rho)\,\langle\Lambda\nu,\zeta\rangle+\left((1-\rho)^{2}-(1-\rho)\right)\,\langle\Lambda\zeta,\zeta\rangle\right) |  | (A149) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +ρ​J​[ν]+(1−ρ)​J​[ζ]\displaystyle\quad\ +\rho\,J[\nu]+(1-\rho)\,J[\zeta] |  | (A150) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​ρ​(1−ρ)​(⟨Λ​ν,ν⟩−2​⟨Λ​ν,ζ⟩+⟨Λ​ζ,ζ⟩)+ρ​J​[ν]+(1−ρ)​J​[ζ]\displaystyle=\frac{1}{2}\,\rho\,(1-\rho)\,\left(\langle\Lambda\nu,\nu\rangle-2\,\langle\Lambda\nu,\zeta\rangle+\langle\Lambda\zeta,\zeta\rangle\right)+\rho\,J[\nu]+(1-\rho)\,J[\zeta] |  | (A151) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​ρ​(1−ρ)​⟨Λ​(ν−ζ),ν−ζ⟩+ρ​J​[ν]+(1−ρ)​J​[ζ]\displaystyle=\frac{1}{2}\,\rho\,(1-\rho)\,\langle\Lambda(\nu-\zeta),\nu-\zeta\rangle+\rho\,J[\nu]+(1-\rho)\,J[\zeta] |  | (A152) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​ρ​(1−ρ)​‖𝔙−1‖op−2​‖ν−ζ‖2+ρ​J​[ν]+(1−ρ)​J​[ζ]\displaystyle=\frac{1}{2}\,\rho\,(1-\rho)\,\left\|\mathfrak{V}^{-1}\right\|\_{\operatorname{op}}^{-2}\,\|\nu-\zeta\|^{2}+\rho\,J[\nu]+(1-\rho)\,J[\zeta] |  | (A153) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥ρ​J​[ν]+(1−ρ)​J​[ζ],\displaystyle\geq\rho\,J[\nu]+(1-\rho)\,J[\zeta]\,, |  | (A154) |

with equality if and only if ν=ζ\nu=\zeta. Hence, JJ is strictly concave.
∎

### E Proof of Proposition [3](https://arxiv.org/html/2512.19838v1#Thmproposition3 "Proposition 3: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

Take ν,δ∈𝒜2\nu,\delta\in\mathcal{A}\_{2} and ϵ>0\epsilon>0. Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1ϵ​(J​[ν+ϵ​δ]−J​[ν])\displaystyle\frac{1}{\epsilon}\,(J[\nu+\epsilon\,\delta]-J[\nu]) | =1ϵ​(−12​⟨Λ​(ν+ϵ​δ),ν+ϵ​δ⟩+⟨b,ν+ϵ​δ⟩+12​⟨Λ​ν,ν⟩−⟨b,ν⟩)\displaystyle=\frac{1}{\epsilon}\,\left(-\frac{1}{2}\,\langle\Lambda(\nu+\epsilon\,\delta),\nu+\epsilon\,\delta\rangle+\langle b,\nu+\epsilon\,\delta\rangle+\frac{1}{2}\langle\Lambda\nu,\nu\rangle-\langle b,\nu\rangle\right) |  | (A155) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1ϵ​(−12​⟨Λ​ν,ν⟩−ϵ​⟨Λ​ν,δ⟩−ϵ22​⟨Λ​δ,δ⟩+⟨b,ϵ​δ⟩+12​⟨Λ​ν,ν⟩)\displaystyle=\frac{1}{\epsilon}\,\left(-\frac{1}{2}\,\langle\Lambda\nu,\nu\rangle-\epsilon\,\langle\Lambda\nu,\delta\rangle-\frac{\epsilon^{2}}{2}\,\langle\Lambda\delta,\delta\rangle+\langle b,\epsilon\,\delta\rangle+\frac{1}{2}\langle\Lambda\nu,\nu\rangle\right) |  | (A156) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−⟨Λ​ν,δ⟩−ϵ2​⟨Λ​δ,δ⟩+⟨b,δ⟩\displaystyle=-\langle\Lambda\nu,\delta\rangle-\frac{\epsilon}{2}\,\langle\Lambda\delta,\delta\rangle+\langle b,\delta\rangle |  | (A157) |

It follows that the Gâteaux derivative 𝔇​J​[ν]{\mathfrak{D}}J[\nu] at ν∈𝒜2\nu\in{\mathcal{A}}\_{2} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔇​J​[ν]​(δ)=limϵ↓0J​[ν+ϵ​δ]−J​[ν]ϵ=⟨−Λ​ν+b,δ⟩.\displaystyle{\mathfrak{D}}J[\nu](\delta)=\lim\_{\epsilon\downarrow 0}\frac{J[\nu+\epsilon\delta]-J[\nu]}{\epsilon}=\langle-\Lambda\nu+b,\delta\rangle\,. |  | (A158) |

We identify 𝔇​J​[ν]{\mathfrak{D}}J[\nu] with −Λ​ν+b-\Lambda\nu+b. From ([42](https://arxiv.org/html/2512.19838v1#S4.E42 "In Proposition 1: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) and ([43](https://arxiv.org/html/2512.19838v1#S4.E43 "In Proposition 1: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔇​J​[ν]=−Λ​ν+b=−2​η​ν+c​(Y+Q0+𝔔​ν)+𝔔T​(A​F−β​ℑ​ν+c​ν−ϕ​(Y+Q0+𝔔​ν))+ℑ⊤​(G​F−β​(Y+Q0+𝔔​ν)).\displaystyle\begin{split}{\mathfrak{D}}J[\nu]=-\Lambda\nu+b&=-2\,\eta\,\nu+c\,(Y+Q\_{0}+\mathfrak{Q}\nu)+\mathfrak{Q}^{T}(A\,F-\beta\,\mathfrak{I}\nu+c\,\nu-\phi\,(Y+Q\_{0}+\mathfrak{Q}\nu))\\ &\quad\ +\mathfrak{I}^{\top}(G\,F-\beta\,(Y+Q\_{0}+\mathfrak{Q}\nu))\,.\end{split} | |  | (A159) |

Write

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨𝔔​ν,ζ⟩=𝔼​[∫0T∫0tνs​ds​ζt​dt]\displaystyle\langle\mathfrak{Q}\nu,\zeta\rangle=\mathbb{E}\left[\int\_{0}^{T}\int\_{0}^{t}\nu\_{s}\,{\mathrm{d}s}\,\zeta\_{t}\,{\mathrm{d}t}\right] | =𝔼​[∫0Tνs​∫sTζt​dt​ds]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\nu\_{s}\int\_{s}^{T}\zeta\_{t}\,{\mathrm{d}t}\,{\mathrm{d}s}\right] |  | (A160) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0T𝔼​[νs​∫sTζt​dt]​ds\displaystyle=\int\_{0}^{T}\mathbb{E}\!\left[\nu\_{s}\int\_{s}^{T}\zeta\_{t}\,{\mathrm{d}t}\right]\,{\mathrm{d}s} |  | (A161) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0T𝔼​[𝔼​[νs​∫sTζt​dt|ℱs]]​ds\displaystyle=\int\_{0}^{T}\mathbb{E}\!\left[\mathbb{E}\!\left[\left.\nu\_{s}\int\_{s}^{T}\zeta\_{t}\,{\mathrm{d}t}\,\right|\,{\mathcal{F}}\_{s}\right]\right]\,{\mathrm{d}s} |  | (A162) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0T𝔼​[νs​𝔼​[∫sTζt​dt|ℱs]]​ds\displaystyle=\int\_{0}^{T}\mathbb{E}\!\left[\nu\_{s}\,\mathbb{E}\!\left[\left.\int\_{s}^{T}\zeta\_{t}\,{\mathrm{d}t}\,\right|\,{\mathcal{F}}\_{s}\right]\right]\,{\mathrm{d}s} |  | (A163) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼​[∫0Tνs​𝔼​[∫sTζt​dt|ℱs]​ds],\displaystyle=\mathbb{E}\!\left[\int\_{0}^{T}\nu\_{s}\,\mathbb{E}\!\left[\left.\int\_{s}^{T}\zeta\_{t}\,{\mathrm{d}t}\,\right|\,{\mathcal{F}}\_{s}\right]\,{\mathrm{d}s}\right]\,, |  | (A164) |

thus, 𝔔⊤\mathfrak{Q}^{\top} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝔔⊤​ζ)t=𝔼​[∫tTζs​ds|ℱt]=𝔼​[∫0Tζs​ds|ℱt]−∫0tζs​ds,(\mathfrak{Q}^{\top}\zeta)\_{t}=\mathbb{E}\!\left[\left.\int\_{t}^{T}\zeta\_{s}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]=\mathbb{E}\!\left[\left.\int\_{0}^{T}\zeta\_{s}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]-\int\_{0}^{t}\zeta\_{s}\,{\mathrm{d}s}\,, |  | (A165) |

where the in the last expression, the martingale term is càdlàg, so the entire process is càdlàg and thus progressively measurable. Similarly, since

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ℑ​ν,ζ⟩=𝔼​[∫0Tc​∫0teβ​(s−t)​νs​ds​ζt​dt]=𝔼​[∫0Tνs​c​𝔼​[∫sTeβ​(s−t)​ζt​dt|ℱs]​ds],\displaystyle\langle\mathfrak{I}\nu,\zeta\rangle=\mathbb{E}\left[\int\_{0}^{T}c\int\_{0}^{t}e^{\beta\,(s-t)}\,\nu\_{s}\,{\mathrm{d}s}\,\zeta\_{t}\,{\mathrm{d}t}\right]=\mathbb{E}\!\left[\int\_{0}^{T}\nu\_{s}\,c\,\mathbb{E}\!\left[\left.\int\_{s}^{T}e^{\beta\,(s-t)}\,\zeta\_{t}\,{\mathrm{d}t}\,\right|\,{\mathcal{F}}\_{s}\right]\,{\mathrm{d}s}\right]\,, |  | (A166) |

ℑ⊤\mathfrak{I}^{\top} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ℑ⊤​ζ)t=c​𝔼​[∫tTeβ​(t−s)​ζs​ds|ℱt].(\mathfrak{I}^{\top}\zeta)\_{t}=c\,\mathbb{E}\!\left[\left.\int\_{t}^{T}e^{\beta\,(t-s)}\,\zeta\_{s}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]\,. |  | (A167) |

It follows from ([A159](https://arxiv.org/html/2512.19838v1#S1.E159 "In E Proof of Proposition 3 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔇​J​[ν]t\displaystyle{\mathfrak{D}}J[\nu]\_{t} | =−2​η​νt+c​(Yt+Qtν)+𝔼​[∫tT(As​Fs+c​νs−β​Isν−ϕ​(Ys+Qsν))​ds|ℱt]\displaystyle=-2\,\eta\,\nu\_{t}+c\,\left(Y\_{t}+Q^{\nu}\_{t}\right)+\mathbb{E}\left[\left.\int\_{t}^{T}\left(A\_{s}\,F\_{s}+c\,\nu\_{s}-\beta\,I^{\nu}\_{s}-\phi\,\left(Y\_{s}+Q^{\nu}\_{s}\right)\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right] |  | (A168) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +c​et​β​𝔼​[∫tTe−s​β​(Gs​Fs−β​(Ys+Qsν))​ds|ℱt].\displaystyle\quad+c\,e^{t\,\beta}\,\mathbb{E}\left[\left.\int\_{t}^{T}e^{-s\,\beta}\,\left(G\_{s}\,F\_{s}-\beta\,\left(Y\_{s}+Q^{\nu}\_{s}\right)\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]\,. |  | (A169) |

∎

### F Proof of Theorem [1](https://arxiv.org/html/2512.19838v1#Thmtheorem1 "Theorem 1: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

Suppose 𝔇​J​[ν⋆]=0{\mathfrak{D}}J[\nu^{\star}]=0 for some ν⋆∈𝒜2\nu^{\star}\in{\mathcal{A}}\_{2}. Then by Proposition [3](https://arxiv.org/html/2512.19838v1#Thmproposition3 "Proposition 3: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 2​η​νt⋆\displaystyle 2\,\eta\,\nu^{\star}\_{t} | =𝔼​[c​(Yt+Qtν⋆)+∫tT(As​Fs+c​νs⋆−β​Isν⋆−ϕ​(Ys+Qsν⋆))​ds|ℱt]\displaystyle=\mathbb{E}\left[\left.c\,\left(Y\_{t}+Q\_{t}^{\nu^{\star}}\right)+\int\_{t}^{T}\left(A\_{s}\,F\_{s}+c\,\nu^{\star}\_{s}-\beta\,I\_{s}^{\nu^{\star}}-\phi\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right] |  | (A170) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +c​et​β​𝔼​[∫tTe−s​β​(Gs​Fs−β​(Ys+Qsν⋆))​ds|ℱt]\displaystyle\quad\ +c\,e^{t\,\beta}\,\mathbb{E}\left[\left.\int\_{t}^{T}e^{-s\,\beta}\left(G\_{s}\,F\_{s}-\beta\,\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right] |  | (A171) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼​[c​(YT+QTν⋆)+∫tT((As−c​Gs)​Fs−β​Isν⋆−ϕ​(Ys+Qsν⋆))​ds|ℱt]\displaystyle=\mathbb{E}\left[\left.c\,\left(Y\_{T}+Q\_{T}^{\nu^{\star}}\right)+\int\_{t}^{T}\left(\left(A\_{s}-c\,G\_{s}\right)\,F\_{s}-\beta\,I\_{s}^{\nu^{\star}}-\phi\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right] |  | (A172) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +c​et​β​𝔼​[∫tTe−s​β​(Gs​Fs−β​(Ys+Qsν⋆))​ds|ℱt]−c​σ​𝔼​[∫tT∂1h​(Fs,κ)​Fs​d​Ws|ℱt]\displaystyle\quad\ +c\,e^{t\,\beta}\,\mathbb{E}\left[\left.\int\_{t}^{T}e^{-s\,\beta}\left(G\_{s}\,F\_{s}-\beta\,\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]-c\,\sigma\,\mathbb{E}\left[\left.\int\_{t}^{T}\partial\_{1}h(F\_{s},\kappa)\,F\_{s}\,\mathrm{d}W\_{s}\,\right|\,{\mathcal{F}}\_{t}\right] |  | (A173) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼​[c​(YT+QTν⋆)+∫0T((As−c​Gs)​Fs−β​Isν⋆−ϕ​(Ys+Qsν⋆))​ds|ℱt]\displaystyle=\mathbb{E}\left[\left.c\,\left(Y\_{T}+Q\_{T}^{\nu^{\star}}\right)+\int\_{0}^{T}\left(\left(A\_{s}-c\,G\_{s}\right)\,F\_{s}-\beta\,I\_{s}^{\nu^{\star}}-\phi\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right] |  | (A174) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −∫0t((As−c​Gs)​Fs−β​Isν⋆−ϕ​(Ys+Qsν⋆))​ds+c​et​β​𝔼​[∫0Te−s​β​(Gs​Fs−β​(Ys+Qsν⋆))​ds|ℱt]\displaystyle-\int\_{0}^{t}\left(\left(A\_{s}-c\,G\_{s}\right)\,F\_{s}-\beta\,I\_{s}^{\nu^{\star}}-\phi\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}+c\,e^{t\,\beta}\,\mathbb{E}\left[\left.\int\_{0}^{T}e^{-s\,\beta}\left(G\_{s}\,F\_{s}-\beta\,\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right] |  | (A175) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −c​et​β​∫0te−s​β​(Gs​Fs−β​(Ys+Qsν⋆))​ds−c​σ​𝔼​[∫tT∂1h​(Fs,κ)​Fs​d​Ws|ℱt].\displaystyle-c\,e^{t\,\beta}\int\_{0}^{t}e^{-s\,\beta}\left(G\_{s}\,F\_{s}-\beta\,\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}-c\,\sigma\,\mathbb{E}\left[\left.\int\_{t}^{T}\partial\_{1}h(F\_{s},\kappa)\,F\_{s}\,\mathrm{d}W\_{s}\,\right|\,{\mathcal{F}}\_{t}\right]\,. |  | (A176) |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|∂1h​(Ft,κ)|2​Ft2​dt]≲𝔼​[∫0T(Ft2​qκ+2+Ft2​pκ+2)​dt]<∞,\displaystyle\mathbb{E}\left[\int\_{0}^{T}\left|\partial\_{1}h(F\_{t},\kappa)\right|^{2}\,F\_{t}^{2}\,{\mathrm{d}t}\right]\lesssim\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{2\,q\_{\kappa}+2}+F\_{t}^{2\,p\_{\kappa}+2}\right)\,{\mathrm{d}t}\right]<\infty\,, |  | (A177) |

the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0t∂1h​(Fs,κ)​Fs​d​Ws,0≤t≤T,\int\_{0}^{t}\partial\_{1}h(F\_{s},\kappa)\,F\_{s}\,\mathrm{d}W\_{s}\,,\quad 0\leq t\leq T\,, |  | (A178) |

is a martingale, so

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫tT∂1h​(Fs,κ)​Fs​d​Ws|ℱt]=0.\mathbb{E}\left[\left.\int\_{t}^{T}\partial\_{1}h(F\_{s},\kappa)\,F\_{s}\,\mathrm{d}W\_{s}\,\right|\,{\mathcal{F}}\_{t}\right]=0\,. |  | (A179) |

Define process N~\tilde{N} by

|  |  |  |
| --- | --- | --- |
|  | N~t=𝔼​[∫0Te−s​β​(Gs​Fs−β​(Ys+Qsν⋆))​ds|ℱt].\displaystyle\tilde{N}\_{t}=\mathbb{E}\left[\left.\int\_{0}^{T}e^{-s\,\beta}\left(G\_{s}\,F\_{s}-\beta\,\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]\,. |  |

Then N~\tilde{N} is a martingale with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[|N~T|2]\displaystyle\mathbb{E}\left[|\tilde{N}\_{T}|^{2}\right] | ≤𝔼​[|∫0Te−s​β​(Gs​Fs−β​(Ys+Qsν⋆))​ds|2]\displaystyle\leq\mathbb{E}\left[\left|\int\_{0}^{T}e^{-s\,\beta}\left(G\_{s}\,F\_{s}-\beta\,\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}\right|^{2}\right] |  | (A180) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≲𝔼​[∫0T|Gs​Fs|2​ds]+𝔼​[∫0T|Ys|2​ds]+𝔼​[∫0T|Qsν⋆|2​ds]\displaystyle\lesssim\mathbb{E}\left[\int\_{0}^{T}\left|G\_{s}\,F\_{s}\right|^{2}\,{\mathrm{d}s}\right]+\mathbb{E}\left[\int\_{0}^{T}\left|Y\_{s}\right|^{2}\,{\mathrm{d}s}\right]+\mathbb{E}\left[\int\_{0}^{T}\left|Q^{\nu^{\star}}\_{s}\right|^{2}\,{\mathrm{d}s}\right] |  | (A181) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≲𝔼​[∫0T|Gs|q​ds]2/q​𝔼​[∫0T|Fs|r​ds]2/r+𝔼​[∫0T|Ys|2​ds]+𝔼​[∫0T|Qsν⋆|2​ds]\displaystyle\lesssim\mathbb{E}\left[\int\_{0}^{T}\left|G\_{s}\right|^{q}\,{\mathrm{d}s}\right]^{2/q}\,\mathbb{E}\left[\int\_{0}^{T}\left|F\_{s}\right|^{r}\,{\mathrm{d}s}\right]^{2/r}+\mathbb{E}\left[\int\_{0}^{T}\left|Y\_{s}\right|^{2}\,{\mathrm{d}s}\right]+\mathbb{E}\left[\int\_{0}^{T}\left|Q^{\nu^{\star}}\_{s}\right|^{2}\,{\mathrm{d}s}\right] |  | (A182) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <∞\displaystyle<\infty |  | (A183) |

for some q∈(2,p)q\in(2,p) and r>2r>2 such that 1q+1r=12\tfrac{1}{q}+\tfrac{1}{r}=\tfrac{1}{2} due to Lemma [1](https://arxiv.org/html/2512.19838v1#Thmlemma1 "Lemma 1: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"). Define process ZZ by

|  |  |  |
| --- | --- | --- |
|  | Zt=et​β​(N~t−∫0te−s​β​(Gs​Fs−β​(Ys+Qsν⋆))​ds).\displaystyle Z\_{t}=e^{t\,\beta}\,\left(\tilde{N}\_{t}-\int\_{0}^{t}e^{-s\,\beta}\left(G\_{s}\,F\_{s}-\beta\,\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}\right)\,. |  |

Then ZT=0Z\_{T}=0, and generalized Itô’s formula (note N~\tilde{N} is càdlàg but not necessarily continuous) implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | −Zt\displaystyle-Z\_{t} | =∫tTβ​es​β​(N~s−−∫0se−u​β​(Gu​Fu−β​(Yu+Quν⋆))​du)​ds+∫tTes​β​dN~s\displaystyle=\int\_{t}^{T}\beta\,e^{s\,\beta}\left(\tilde{N}\_{s-}-\int\_{0}^{s}e^{-u\,\beta}\left(G\_{u}\,F\_{u}-\beta\,\left(Y\_{u}+Q\_{u}^{\nu^{\star}}\right)\right)\,{\mathrm{d}u}\right)\,\mathrm{d}s+\int\_{t}^{T}e^{s\,\beta}\,\mathrm{d}\tilde{N}\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫tT(Gs​Fs−β​(Ys+Qsν⋆))​ds+∑t<s≤T[es​β​N~s−es​β​N~s−−es​β​Δ​N~s]\displaystyle\quad\ -\int\_{t}^{T}\left(G\_{s}\,F\_{s}-\beta\,\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s}+\sum\_{t<s\leq T}\left[e^{s\,\beta}\,\tilde{N}\_{s}-e^{s\,\beta}\,\tilde{N}\_{s-}-e^{s\,\beta}\,\Delta\tilde{N}\_{s}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫tTβ​es​β​(N~s−∫0se−u​β​(Gu​Fu−β​(Yu+Quν⋆))​du)​ds+∫tTes​β​dN~s\displaystyle=\int\_{t}^{T}\beta\,e^{s\,\beta}\left(\tilde{N}\_{s}-\int\_{0}^{s}e^{-u\,\beta}\left(G\_{u}\,F\_{u}-\beta\,\left(Y\_{u}+Q\_{u}^{\nu^{\star}}\right)\right)\,{\mathrm{d}u}\right)\,\mathrm{d}s+\int\_{t}^{T}e^{s\,\beta}\,\mathrm{d}\tilde{N}\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫tT(Gs​Fs−β​(Ys+Qsν⋆))​ds\displaystyle\quad\ -\int\_{t}^{T}\left(G\_{s}\,F\_{s}-\beta\,\left(Y\_{s}+Q\_{s}^{\nu^{\star}}\right)\right)\,{\mathrm{d}s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫tT(β​(Zs+Ys+Qsν⋆)−Gs​Fs)​ds+∫tTes​β​dN~s,\displaystyle=\int\_{t}^{T}\left(\beta\,\left(Z\_{s}+Y\_{s}+Q^{\nu^{\star}}\_{s}\right)-G\_{s}\,F\_{s}\right)\,\mathrm{d}s+\int\_{t}^{T}e^{s\,\beta}\,\mathrm{d}\tilde{N}\_{s}\,, |  |

where the second equality is because a càdlàg path has at most countably many jumps, which form a Lebesgue measure zero set. Define process NN by

|  |  |  |
| --- | --- | --- |
|  | Nt=∫0tes​β​dN~s,0≤t≤T.\displaystyle N\_{t}=\int\_{0}^{t}e^{s\,\beta}\,\mathrm{d}\tilde{N}\_{s}\,,\quad 0\leq t\leq T\,. |  |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0Te2​s​η​d​⟨N~⟩s]≤e2​T​η​𝔼​[⟨N~⟩T]≤e2​T​η​𝔼​[|N~T|2]<∞,\displaystyle\mathbb{E}\left[\int\_{0}^{T}e^{2\,s\,\eta}\,\mathrm{d}\langle\tilde{N}\rangle\_{s}\right]\leq e^{2\,T\,\eta}\,\mathbb{E}\left[\langle\tilde{N}\rangle\_{T}\right]\leq e^{2\,T\,\eta}\,\mathbb{E}\left[|\tilde{N}\_{T}|^{2}\right]<\infty\,, |  | (A184) |

NN is a martingale with NT∈L2​(Ω)N\_{T}\in L^{2}(\Omega). Moreover, the process MM, defined by

|  |  |  |
| --- | --- | --- |
|  | Mt=𝔼​[c​(YT+QTν⋆)+∫0T((As−c​Gs)​Fs−β​Isν⋆−ϕ​(Ys+Qsν⋆))​ds|ℱt]+c​Nt,\displaystyle M\_{t}=\mathbb{E}\left[\left.c\,\left(Y\_{T}+Q^{\nu^{\star}}\_{T}\right)+\int\_{0}^{T}\left(\left(A\_{s}-c\,G\_{s}\right)\,F\_{s}-\beta\,I^{\nu^{\star}}\_{s}-\phi\,\left(Y\_{s}+Q^{\nu^{\star}}\_{s}\right)\right)\,\mathrm{d}s\,\right|\,{\mathcal{F}}\_{t}\right]+c\,N\_{t}\,, |  |

is also a martingale with MT∈L2​(Ω)M\_{T}\in L^{2}(\Omega). Combining everything gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​η​νs⋆\displaystyle 2\,\eta\,\nu^{\star}\_{s} | =Mt−c​Nt−∫0t((As−c​Gs)​Fs−β​Isν⋆−ϕ​(Ys+Qsν⋆))​ds+c​Zt\displaystyle=M\_{t}-c\,N\_{t}-\int\_{0}^{t}\left(\left(A\_{s}-c\,G\_{s}\right)\,F\_{s}-\beta\,I^{\nu^{\star}}\_{s}-\phi\,\left(Y\_{s}+Q^{\nu^{\star}}\_{s}\right)\right)\,\mathrm{d}s+c\,Z\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Mt−c​Nt−∫0t((As−c​Gs)​Fs−β​Isν⋆−ϕ​(Ys+Qsν⋆))​ds\displaystyle=M\_{t}-c\,N\_{t}-\int\_{0}^{t}\left(\left(A\_{s}-c\,G\_{s}\right)\,F\_{s}-\beta\,I^{\nu^{\star}}\_{s}-\phi\,\left(Y\_{s}+Q^{\nu^{\star}}\_{s}\right)\right)\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −c​∫tT(β​(Zs+Ys+Qsν⋆)−Gs​Fs)​ds−c​(NT−Nt)\displaystyle\quad-c\int\_{t}^{T}\left(\beta\,\left(Z\_{s}+Y\_{s}+Q^{\nu^{\star}}\_{s}\right)-G\_{s}\,F\_{s}\right)\,\mathrm{d}s-c\,(N\_{T}-N\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Mt−∫0T((As−c​Gs)​Fs−β​Isν⋆−ϕ​(Ys+Qsν⋆))​ds\displaystyle=M\_{t}-\int\_{0}^{T}\left(\left(A\_{s}-c\,G\_{s}\right)\,F\_{s}-\beta\,I^{\nu^{\star}}\_{s}-\phi\,\left(Y\_{s}+Q^{\nu^{\star}}\_{s}\right)\right)\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫tT(As​Fs−β​Isν⋆−(ϕ+c​β)​(Ys+Qsν⋆)−c​β​Zs)​ds−c​NT\displaystyle\quad+\int\_{t}^{T}\left(A\_{s}\,F\_{s}-\beta\,I^{\nu^{\star}}\_{s}-(\phi+c\,\beta)\,\left(Y\_{s}+Q^{\nu^{\star}}\_{s}\right)-c\,\beta\,Z\_{s}\right)\,\mathrm{d}s-cN\_{T} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c​(YT+QTν⋆)−∫tT(−As​Fs−β​Isν⋆+(ϕ+c​β)​(Ys+Qsν⋆)+c​β​Zs)​ds−(MT−Mt).\displaystyle=c\,\left(Y\_{T}+Q^{\nu^{\star}}\_{T}\right)-\int\_{t}^{T}\left(-A\_{s}\,F\_{s}-\beta\,I^{\nu^{\star}}\_{s}+(\phi+c\,\beta)\,\left(Y\_{s}+Q^{\nu^{\star}}\_{s}\right)+c\,\beta\,Z\_{s}\right)\,\mathrm{d}s-(M\_{T}-M\_{t})\,. |  |

Thus ν⋆\nu^{\star} satisfies the FBSDE ([47](https://arxiv.org/html/2512.19838v1#S4.E47 "In Theorem 1: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")).

Conversely, assume ν⋆∈𝒜2\nu^{\star}\in{\mathcal{A}}\_{2} satisfies the FBSDE ([47](https://arxiv.org/html/2512.19838v1#S4.E47 "In Theorem 1: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) for some martingales MM and NN such that MT,NT∈L2​(Ω)M\_{T},N\_{T}\in L^{2}(\Omega). By integrating ν⋆\nu^{\star} and ZZ and using the terminal conditions, we may write

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​η​νt⋆=c​(YT+QT)+∫tT(As​Fs−β​Is−(ϕ+c​β)​(Ys+Qs)−c​β​Zs)​ds−MT+Mt\displaystyle 2\,\eta\,\nu^{\star}\_{t}=c\,(Y\_{T}+Q\_{T})+\int\_{t}^{T}\left(A\_{s}\,F\_{s}-\beta\,I\_{s}-(\phi+c\,\beta)\,(Y\_{s}+Q\_{s})-c\,\beta\,Z\_{s}\right)\,{\mathrm{d}s}-M\_{T}+M\_{t} |  | (A185) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt=∫tT(−β​(Zs+Ys+Qs)+Gs​Fs)​ds−NT+Nt\displaystyle Z\_{t}=\int\_{t}^{T}\left(-\beta\,(Z\_{s}+Y\_{s}+Q\_{s})+G\_{s}\,F\_{s}\right)\,{\mathrm{d}s}-N\_{T}+N\_{t} |  | (A186) |

Combining above two identities as well as the dynamics of YY and QQ gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 2​η​νt⋆\displaystyle 2\,\eta\,\nu^{\star}\_{t} | =c​(Yt+Qt)+∫tTc​Gs​Fs​ds+∫tTc​σ​∂1h​(Fs,κ)​Fs​d​Ws+∫tTc​νs⋆​ds\displaystyle=c\,(Y\_{t}+Q\_{t})+\int\_{t}^{T}c\,G\_{s}\,F\_{s}\,{\mathrm{d}s}+\int\_{t}^{T}c\,\sigma\,\partial\_{1}h(F\_{s},\kappa)\,F\_{s}\,\mathrm{d}W\_{s}+\int\_{t}^{T}c\,\nu^{\star}\_{s}\,{\mathrm{d}s} |  | (A187) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫tT(As​Fs−β​Is−(ϕ+c​β)​(Ys+Qs))​ds−MT+Mt\displaystyle\quad\ +\int\_{t}^{T}\left(A\_{s}\,F\_{s}-\beta\,I\_{s}-(\phi+c\,\beta)\,(Y\_{s}+Q\_{s})\right)\,{\mathrm{d}s}-M\_{T}+M\_{t} |  | (A188) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +c​Zt+∫tT(c​β​(Ys+Qs)−c​Gs​Fs)​ds+c​NT−c​Nt\displaystyle\quad\ +c\,Z\_{t}+\int\_{t}^{T}\left(c\,\beta\,(Y\_{s}+Q\_{s})-c\,G\_{s}\,F\_{s}\right)\,{\mathrm{d}s}+c\,N\_{T}-c\,N\_{t} |  | (A189) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =c​(Yt+Qt)+∫tT(As​Fs+c​νs⋆−β​Is−ϕ​(Ys+Qs))​ds+c​Zt\displaystyle=c\,(Y\_{t}+Q\_{t})+\int\_{t}^{T}\left(A\_{s}\,F\_{s}+c\,\nu^{\star}\_{s}-\beta\,I\_{s}-\phi\,(Y\_{s}+Q\_{s})\right)\,{\mathrm{d}s}+c\,Z\_{t} |  | (A190) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫tTc​σ​∂1h​(Fs,κ)​Fs​d​Ws−MT+Mt+c​NT−c​Nt.\displaystyle\quad\ +\int\_{t}^{T}c\,\sigma\,\partial\_{1}h(F\_{s},\kappa)\,F\_{s}\,\mathrm{d}W\_{s}-M\_{T}+M\_{t}+c\,N\_{T}-c\,N\_{t}\,. |  | (A191) |

Recall that the process in ([A178](https://arxiv.org/html/2512.19838v1#S1.E178 "In F Proof of Theorem 1 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) is a martingale, so taking conditional expectation on above equation gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​η​νt⋆=c​(Yt+Qt)+𝔼​[∫tT(As​Fs+c​νs⋆−β​Is−ϕ​(Ys+Qs))​ds|ℱt]+c​𝔼​[Zt|ℱt]2\,\eta\,\nu^{\star}\_{t}=c\,(Y\_{t}+Q\_{t})+\mathbb{E}\left[\left.\int\_{t}^{T}\left(A\_{s}\,F\_{s}+c\,\nu^{\star}\_{s}-\beta\,I\_{s}-\phi\,(Y\_{s}+Q\_{s})\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]+c\,\mathbb{E}[Z\_{t}\,|\,{\mathcal{F}}\_{t}] |  | (A192) |

To solve for ZZ, we use generalized Itô’s formula and the dynamics and terminal condition of ZZ to write

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Zt=et​β​e−t​β​Zt\displaystyle Z\_{t}=e^{t\,\beta}\,e^{-t\,\beta}\,Z\_{t} | =et​β​(∫tTβ​e−s​β​Zs​ds−∫tTe−s​β​(β​(Zs+Ys+Qs)−Gs​Fs)​ds−∫tTe−s​β​dNs)\displaystyle=e^{t\,\beta}\,\left(\int\_{t}^{T}\beta\,e^{-s\,\beta}\,Z\_{s}\,{\mathrm{d}s}-\int\_{t}^{T}e^{-s\,\beta}\,\left(\beta\,(Z\_{s}+Y\_{s}+Q\_{s})-G\_{s}\,F\_{s}\right)\,{\mathrm{d}s}-\int\_{t}^{T}e^{-s\,\beta}\,\mathrm{d}N\_{s}\right) |  | (A193) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−et​β​(∫tTe−s​β​(β​(Ys+Qs)−Gs​Fs)​ds+∫tTe−s​β​dNs).\displaystyle=-e^{t\,\beta}\,\left(\int\_{t}^{T}e^{-s\,\beta}\,\left(\beta\,(Y\_{s}+Q\_{s})-G\_{s}\,F\_{s}\right)\,{\mathrm{d}s}+\int\_{t}^{T}e^{-s\,\beta}\,\mathrm{d}N\_{s}\right)\,. |  | (A194) |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0Te−2​s​η​d​⟨N⟩s]≤𝔼​[⟨N⟩T]≤𝔼​[|NT|2]<∞,\displaystyle\mathbb{E}\left[\int\_{0}^{T}e^{-2\,s\,\eta}\,\mathrm{d}\langle N\rangle\_{s}\right]\leq\mathbb{E}\left[\langle N\rangle\_{T}\right]\leq\mathbb{E}\left[|N\_{T}|^{2}\right]<\infty\,, |  | (A195) |

the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0te−s​β​dNs,0≤t≤T,\int\_{0}^{t}e^{-s\,\beta}\,\mathrm{d}N\_{s}\,,\quad 0\leq t\leq T\,, |  | (A196) |

is a martingale. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Zt|ℱt]=et​β​𝔼​[∫tTe−s​β​(Gs​Fs−β​(Ys+Qs))​ds|ℱt].\mathbb{E}[Z\_{t}\,|\,{\mathcal{F}}\_{t}]=e^{t\,\beta}\,\mathbb{E}\left[\left.\int\_{t}^{T}e^{-s\,\beta}\,\left(G\_{s}\,F\_{s}-\beta\,(Y\_{s}+Q\_{s})\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]\,. |  | (A197) |

Plugging this into ([A191](https://arxiv.org/html/2512.19838v1#S1.E191 "In F Proof of Theorem 1 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 2​η​νt⋆\displaystyle 2\,\eta\,\nu^{\star}\_{t} | =c​(Yt+Qt)+𝔼​[∫tT(As​Fs+c​νs⋆−β​Is−ϕ​(Ys+Qs))​ds|ℱt]\displaystyle=c\,(Y\_{t}+Q\_{t})+\mathbb{E}\left[\left.\int\_{t}^{T}\left(A\_{s}\,F\_{s}+c\,\nu^{\star}\_{s}-\beta\,I\_{s}-\phi\,(Y\_{s}+Q\_{s})\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right] |  | (A198) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +c​et​β​𝔼​[∫tTe−s​β​(Gs​Fs−β​(Ys+Qs))​ds|ℱt],\displaystyle\quad\ +c\,e^{t\,\beta}\,\mathbb{E}\left[\left.\int\_{t}^{T}e^{-s\,\beta}\,\left(G\_{s}\,F\_{s}-\beta\,(Y\_{s}+Q\_{s})\right)\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]\,, |  | (A199) |

that is, 𝔇​J​[ν⋆]t=0{\mathfrak{D}}J[\nu^{\star}]\_{t}=0.

### G Proof of Proposition [4](https://arxiv.org/html/2512.19838v1#Thmproposition4 "Proposition 4: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

First, we show we may construct a solution of the FBSDE from a solution of the DRE. Suppose PP is a solution to the DRE ([48](https://arxiv.org/html/2512.19838v1#S4.E48 "In Proposition 4: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) and the processes ℓ\ell, Φ\Phi, Ψ\Psi are defined as stated in the proposition. Let us differentiate these processes. For Φ\Phi, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Φt\displaystyle\mathrm{d}\Phi\_{t} | =(B12​P​(t)+B11)​Φt​d​t+e∫0t(B12​P​(u)+B11)​du​e−∫0t(B12​P​(u)+B11)​du​B12​ℓt​d​t\displaystyle=\left(B\_{12}\,P(t)+B\_{11}\right)\,\Phi\_{t}\,{\mathrm{d}t}+e^{\int\_{0}^{t}\left(B\_{12}\,P(u)+B\_{11}\right)\,{\mathrm{d}u}}\,e^{-\int\_{0}^{t}\left(B\_{12}\,P(u)+B\_{11}\right)\,{\mathrm{d}u}}\,B\_{12}\,\ell\_{t}\,{\mathrm{d}t} |  | (A200) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(B12​(P​(t)​Φt+ℓt)+B11​Φt)​d​t\displaystyle=\left(B\_{12}\,\left(P(t)\,\Phi\_{t}+\ell\_{t}\right)+B\_{11}\,\Phi\_{t}\right)\,{\mathrm{d}t} |  | (A201) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(B12​Ψt+B11​Φt)​d​t.\displaystyle=\left(B\_{12}\,\Psi\_{t}+B\_{11}\,\Phi\_{t}\right)\,{\mathrm{d}t}\,. |  | (A202) |

For ℓ\ell, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℓt\displaystyle\ell\_{t} | =e−∫0t(P​(u)​B12−B22)​du​𝔼​[L−∫tTe∫0s(P​(u)​B12−B22)​du​bs​ds|ℱt]\displaystyle=e^{-\int\_{0}^{t}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,\mathbb{E}\!\left[\left.L-\int\_{t}^{T}e^{\int\_{0}^{s}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,b\_{s}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right] |  | (A203) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =e−∫0t(P​(u)​B12−B22)​du​(𝔼​[L−∫0Te∫0s(P​(u)​B12−B22)​du​bs​ds|ℱt]+∫0te∫0s(P​(u)​B12−B22)​du​bs​ds).\displaystyle=e^{-\int\_{0}^{t}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,\left(\mathbb{E}\!\left[\left.L-\int\_{0}^{T}e^{\int\_{0}^{s}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,b\_{s}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]+\int\_{0}^{t}e^{\int\_{0}^{s}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,b\_{s}\,{\mathrm{d}s}\right)\,. |  | (A204) |

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ~t=𝔼​[L−∫0Te∫0s(P​(u)​B12−B22)​du​bs​ds|ℱt],\tilde{\mathcal{M}}\_{t}=\mathbb{E}\!\left[\left.L-\int\_{0}^{T}e^{\int\_{0}^{s}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,b\_{s}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]\,, |  | (A205) |

then M~\tilde{M} is an ℝ2\mathbb{R}^{2}-valued martingale. By Lemma [1](https://arxiv.org/html/2512.19838v1#Thmlemma1 "Lemma 1: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[∫0T|bt|2​dt]≲𝔼​[∫0T(|At​Ft|2+|Yt|2+|Gt​Ft|2)​dt]≤𝔼​[∫0T|At|p​dt]2p​𝔼​[∫0T|Ft|2​pp−2​dt]p−2p+𝔼​[∫0T|Ft|2​dt]+𝔼​[∫0T|Gt|q​dt]2q​𝔼​[∫0T|Ft|2​qq−2​dt]q−2q<∞\displaystyle\begin{split}&\mathbb{E}\!\left[\int\_{0}^{T}|b\_{t}|^{2}\,{\mathrm{d}t}\right]\\ &\lesssim\mathbb{E}\!\left[\int\_{0}^{T}\left(|A\_{t}\,F\_{t}|^{2}+|Y\_{t}|^{2}+|G\_{t}\,F\_{t}|^{2}\right)\,{\mathrm{d}t}\right]\\ &\leq\mathbb{E}\!\left[\int\_{0}^{T}|A\_{t}|^{p}\,{\mathrm{d}t}\right]^{\tfrac{2}{p}}\,\mathbb{E}\!\left[\int\_{0}^{T}|F\_{t}|^{\tfrac{2\,p}{p-2}}\,{\mathrm{d}t}\right]^{\tfrac{p-2}{p}}+\mathbb{E}\!\left[\int\_{0}^{T}|F\_{t}|^{2}\,{\mathrm{d}t}\right]+\mathbb{E}\!\left[\int\_{0}^{T}|G\_{t}|^{q}\,{\mathrm{d}t}\right]^{\tfrac{2}{q}}\,\mathbb{E}\!\left[\int\_{0}^{T}|F\_{t}|^{\tfrac{2\,q}{q-2}}\,{\mathrm{d}t}\right]^{\tfrac{q-2}{q}}\\ &<\infty\end{split} | |  | (A206) |

for some q∈(2,p)q\in(2,p), and thus

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[|ℳ~T|2]\displaystyle\mathbb{E}\!\left[\left|\tilde{\mathcal{M}}\_{T}\right|^{2}\right] | ≤𝔼​[|L−∫0Te∫0s(P​(u)​B12−B22)​du​bs​ds|2]≲𝔼​[YT2]+𝔼​[∫0T|bs|2​ds]<∞.\displaystyle\leq\mathbb{E}\!\left[\left|L-\int\_{0}^{T}e^{\int\_{0}^{s}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,b\_{s}\,{\mathrm{d}s}\right|^{2}\right]\lesssim\mathbb{E}[Y\_{T}^{2}]+\mathbb{E}\!\left[\int\_{0}^{T}|b\_{s}|^{2}\,{\mathrm{d}s}\right]<\infty\,. |  | (A207) |

By generalized Itô’s formula,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​ℓt\displaystyle\mathrm{d}\ell\_{t} | =−(P​(t)​B12−B22)​ℓt​d​t+e−∫0t(P​(u)​B12−B22)​du​(d​ℳ~t+e∫0t(P​(u)​B12−B22)​du​bt​d​t)\displaystyle=-\left(P(t)\,B\_{12}-B\_{22}\right)\,\ell\_{t}\,{\mathrm{d}t}+e^{-\int\_{0}^{t}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,\left(\mathrm{d}\tilde{\mathcal{M}}\_{t}+e^{\int\_{0}^{t}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,b\_{t}\,{\mathrm{d}t}\right) |  | (A208) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =((−P​(t)​B12+B22)​ℓt+bt)​d​t+e−∫0t(P​(u)​B12−B22)​du​d​ℳ~t.\displaystyle=\left(\left(-P(t)\,B\_{12}+B\_{22}\right)\,\ell\_{t}+b\_{t}\right)\,{\mathrm{d}t}+e^{-\int\_{0}^{t}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,\mathrm{d}\tilde{\mathcal{M}}\_{t}\,. |  | (A209) |

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳt=∫0te−∫0s(P​(u)​B12−B22)​du​dℳ~s.\mathcal{M}\_{t}=\int\_{0}^{t}e^{-\int\_{0}^{s}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,\mathrm{d}\tilde{\mathcal{M}}\_{s}\,. |  | (A210) |

Since the integrand is deterministic and differentiable and because of ([A207](https://arxiv.org/html/2512.19838v1#S1.E207 "In G Proof of Proposition 4 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), ℳ\mathcal{M} is an ℝ2\mathbb{R}^{2}-valued martingale with 𝔼​[|ℳT|]2<∞\mathbb{E}[|\mathcal{M}\_{T}|]^{2}<\infty. For Ψ\Psi, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ψt\displaystyle\mathrm{d}\Psi\_{t} | =P′​(t)​Φt​d​t+P​(t)​d​Φt+d​ℓt\displaystyle=P^{\prime}(t)\,\Phi\_{t}\,{\mathrm{d}t}+P(t)\,\mathrm{d}\Phi\_{t}+\mathrm{d}\ell\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =P′​(t)​Φt​d​t+P​(t)​(B11​Φt+B12​(P​(t)​Φt+ℓt))​d​t+d​ℓt\displaystyle=P^{\prime}(t)\,\Phi\_{t}\,{\mathrm{d}t}+P(t)\,(B\_{11}\,\Phi\_{t}+B\_{12}\,(P(t)\,\Phi\_{t}+\ell\_{t}))\,{\mathrm{d}t}+\mathrm{d}\ell\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(P′​(t)+P​(t)​B11+P​(t)​B12​P​(t))​Φt​d​t+P​(t)​B12​ℓt​d​t+d​ℓt\displaystyle=(P^{\prime}(t)+P(t)\,B\_{11}+P(t)\,B\_{12}\,P(t))\,\Phi\_{t}\,{\mathrm{d}t}+P(t)\,B\_{12}\,\ell\_{t}\,{\mathrm{d}t}+\mathrm{d}\ell\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(B21+B22​P​(t))​Φt​d​t+P​(t)​B12​ℓt​d​t+((−P​(t)​B12+B22)​ℓt+bt)​d​t+d​ℳt\displaystyle=(B\_{21}+B\_{22}\,P(t))\,\Phi\_{t}\,{\mathrm{d}t}+P(t)\,B\_{12}\,\ell\_{t}\,{\mathrm{d}t}+((-P(t)\,B\_{12}+B\_{22})\,\ell\_{t}+b\_{t})\,{\mathrm{d}t}+\mathrm{d}\mathcal{M}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(B21​Φt+B22​(P​(t)​Φt+ℓt)+bt)​d​t+d​ℳt\displaystyle=(B\_{21}\,\Phi\_{t}+B\_{22}\,(P(t)\,\Phi\_{t}+\ell\_{t})+b\_{t})\,{\mathrm{d}t}+\mathrm{d}\mathcal{M}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(B21​Φt+B22​Ψt+bt)​d​t+d​ℳt.\displaystyle=(B\_{21}\,\Phi\_{t}+B\_{22}\,\Psi\_{t}+b\_{t})\,{\mathrm{d}t}+\mathrm{d}\mathcal{M}\_{t}\,. |  |

Thus we obtain the FBSDE

|  |  |  |
| --- | --- | --- |
|  | {d​Φt=(B11​Φt+B12​Ψt)​d​t,Φ0=Kd​Ψt=(B21​Φt+B22​Ψt+bt)​d​t+d​ℳt,ΨT=G​ΦT+L,\displaystyle\left\{\begin{array}[]{rlrl}\mathrm{d}\Phi\_{t}&=\left(B\_{11}\,\Phi\_{t}+B\_{12}\,\Psi\_{t}\right)\,{\mathrm{d}t}\,,&\Phi\_{0}&=K\\ \\ \mathrm{d}\Psi\_{t}&=\left(B\_{21}\,\Phi\_{t}+B\_{22}\,\Psi\_{t}+b\_{t}\right)\,{\mathrm{d}t}+\mathrm{d}\mathcal{M}\_{t}\,,&\Psi\_{T}&=G\,\Phi\_{T}+L\end{array}\right.\,, |  |

which is precisely FBSDE ([47](https://arxiv.org/html/2512.19838v1#S4.E47 "In Theorem 1: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) written in vectorial form, provided we identify

|  |  |  |
| --- | --- | --- |
|  | Ψt=(νt⋆Zt),Φt=(ItQt),ℳt=(12​η​MtNt).\Psi\_{t}=\begin{pmatrix}\nu\_{t}^{\star}\\ Z\_{t}\end{pmatrix}\,,\quad\Phi\_{t}=\begin{pmatrix}I\_{t}\\ Q\_{t}\end{pmatrix}\,,\quad\mathcal{M}\_{t}=\begin{pmatrix}\tfrac{1}{2\,\eta}\,M\_{t}\\ N\_{t}\end{pmatrix}\,. |  |

Moreover, due to ([A206](https://arxiv.org/html/2512.19838v1#S1.E206 "In G Proof of Proposition 4 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) and ([A207](https://arxiv.org/html/2512.19838v1#S1.E207 "In G Proof of Proposition 4 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), we obtain the three inequalities

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[∫0T|ℓt|2​dt]\displaystyle\mathbb{E}\!\left[\int\_{0}^{T}|\ell\_{t}|^{2}\,{\mathrm{d}t}\right] | =𝔼​[∫0T|e−∫0t(P​(u)​B12−B22)​du​(ℳ~t+∫0te∫0s(P​(u)​B12−B22)​du​bs​ds)|2​dt]\displaystyle=\mathbb{E}\!\left[\int\_{0}^{T}\left|e^{-\int\_{0}^{t}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,\left(\tilde{\mathcal{M}}\_{t}+\int\_{0}^{t}e^{\int\_{0}^{s}\left(P(u)\,B\_{12}-B\_{22}\right)\,{\mathrm{d}u}}\,b\_{s}\,{\mathrm{d}s}\right)\right|^{2}\,{\mathrm{d}t}\right] |  | (A211) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≲𝔼​[∫0T(|ℳ~t|2+∫0t|bs|2​ds)​dt]\displaystyle\lesssim\mathbb{E}\!\left[\int\_{0}^{T}\left(\left|\tilde{\mathcal{M}}\_{t}\right|^{2}+\int\_{0}^{t}|b\_{s}|^{2}\,{\mathrm{d}s}\right)\,{\mathrm{d}t}\right] |  | (A212) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≲𝔼​[|ℳT~|2]+𝔼​[∫0T|bt|2​dt]\displaystyle\lesssim\mathbb{E}\!\left[\left|\tilde{\mathcal{M}\_{T}}\right|^{2}\right]+\mathbb{E}\!\left[\int\_{0}^{T}|b\_{t}|^{2}\,{\mathrm{d}t}\right] |  | (A213) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <∞,\displaystyle<\infty\,, |  | (A214) |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[∫0T|Φt|2​dt]\displaystyle\mathbb{E}\!\left[\int\_{0}^{T}|\Phi\_{t}|^{2}\,{\mathrm{d}t}\right] | =𝔼​[∫0T|e∫0t(B12​P​(u)+B11)​du​(K+∫0te−∫0s(B12​P​(u)+B11)​du​B12​ℓs​ds)|2​dt]\displaystyle=\mathbb{E}\!\left[\int\_{0}^{T}\left|e^{\int\_{0}^{t}\left(B\_{12}\,P(u)+B\_{11}\right)\,{\mathrm{d}u}}\,\left(K+\int\_{0}^{t}e^{-\int\_{0}^{s}\left(B\_{12}\,P(u)+B\_{11}\right)\,{\mathrm{d}u}}\,B\_{12}\,\ell\_{s}\,{\mathrm{d}s}\right)\right|^{2}\,{\mathrm{d}t}\right] |  | (A215) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≲Q02+𝔼​[∫0T∫0t|ℓs|2​ds​dt]\displaystyle\lesssim Q\_{0}^{2}+\mathbb{E}\!\left[\int\_{0}^{T}\int\_{0}^{t}|\ell\_{s}|^{2}\,{\mathrm{d}s}\,{\mathrm{d}t}\right] |  | (A216) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≲Q02+𝔼​[∫0T|ℓt|2​dt]\displaystyle\lesssim Q\_{0}^{2}+\mathbb{E}\!\left[\int\_{0}^{T}|\ell\_{t}|^{2}\,{\mathrm{d}t}\right] |  | (A217) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <∞,\displaystyle<\infty\,, |  | (A218) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|Ψt|2​dt]=𝔼​[∫0T|P​(t)​Φt+ℓt|2​dt]≲𝔼​[∫0T|Φt|2​dt]+𝔼​[∫0T|ℓt|2​dt]<∞,\mathbb{E}\!\left[\int\_{0}^{T}|\Psi\_{t}|^{2}\,{\mathrm{d}t}\right]=\mathbb{E}\!\left[\int\_{0}^{T}\left|P(t)\,\Phi\_{t}+\ell\_{t}\right|^{2}\,{\mathrm{d}t}\right]\lesssim\mathbb{E}\!\left[\int\_{0}^{T}|\Phi\_{t}|^{2}\,{\mathrm{d}t}\right]+\mathbb{E}\!\left[\int\_{0}^{T}|\ell\_{t}|^{2}\,{\mathrm{d}t}\right]<\infty\,, |  | (A219) |

which implies ν⋆∈𝒜2\nu^{\star}\in{\mathcal{A}}\_{2}.

Next, we show the DRE ([48](https://arxiv.org/html/2512.19838v1#S4.E48 "In Proposition 4: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) admits a unique solution under Assumption [3](https://arxiv.org/html/2512.19838v1#Thmassume3 "Assumption 3: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"), that is, c2<2​η​ϕc^{2}<2\,\eta\,\phi. Here we only consider the case where c>0c>0. The c=0c=0 case is addressed in Proposition [5](https://arxiv.org/html/2512.19838v1#Thmproposition5 "Proposition 5: ‣ D No transient impact ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"), where we derive an explicit solution of ([48](https://arxiv.org/html/2512.19838v1#S4.E48 "In Proposition 4: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")). Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | z=−12​(c22​β+ϕ​c2​η2​β2)<0z=-\frac{1}{2}\left(\frac{c^{2}}{2\,\beta}+\sqrt{\frac{\phi\,c^{2}\,\eta}{2\,\beta^{2}}}\right)<0 |  | (A220) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | w=2​β​z2c​η.w=\frac{2\,\beta\,z^{2}}{c\,\eta}\,. |  | (A221) |

Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​c2​η2​β2>c44​β2=c22​β,\sqrt{\frac{\phi\,c^{2}\,\eta}{2\,\beta^{2}}}>\sqrt{\frac{c^{4}}{4\,\beta^{2}}}=\frac{c^{2}}{2\,\beta}\,, |  | (A222) |

we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | −ϕ​c2​η2​β2<z<−c22​β.-\sqrt{\frac{\phi\,c^{2}\,\eta}{2\,\beta^{2}}}<z<-\frac{c^{2}}{2\,\beta}\,. |  | (A223) |

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | C=(100w),D=(0z2​ηz−c​z2​η),C=\begin{pmatrix}1&0\\ 0&w\end{pmatrix}\,,\quad D=\begin{pmatrix}0&\tfrac{z}{2\,\eta}\\ z&-\tfrac{c\,z}{2\,\eta}\end{pmatrix}\,, |  | (A224) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=(C​B11+D​B21C​B12+B11⊤​D+D​B220B12⊤​D).\mathcal{L}=\begin{pmatrix}C\,B\_{11}+D\,B\_{21}&C\,B\_{12}+B\_{11}^{\top}\,D+D\,B\_{22}\\ 0&B\_{12}^{\top}\,D\end{pmatrix}\,. |  | (A225) |

Consider

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ+ℒ⊤=(𝒦11𝒦12𝒦12⊤𝒦22),\mathcal{L}+\mathcal{L}^{\top}=\begin{pmatrix}\mathcal{K}\_{11}&\mathcal{K}\_{12}\\ \mathcal{K}\_{12}^{\top}&\mathcal{K}\_{22}\end{pmatrix}\,, |  | (A226) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒦11\displaystyle\mathcal{K}\_{11} | =C​B11+(C​B11)⊤+D​B21+(D​B21)⊤=(−2​ββ​zkβ​zkϕ​zk),\displaystyle=C\,B\_{11}+(C\,B\_{11})^{\top}+D\,B\_{21}+(D\,B\_{21})^{\top}=\begin{pmatrix}-2\,\beta&\tfrac{\beta\,z}{k}\\ \tfrac{\beta\,z}{k}&\tfrac{\phi\,z}{k}\end{pmatrix}\,, |  | (A227) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒦12\displaystyle\mathcal{K}\_{12} | =C​B12+B11⊤​D+D​B22=(c0w0),\displaystyle=C\,B\_{12}+B\_{11}^{\top}\,D+D\,B\_{22}=\begin{pmatrix}c&0\\ w&0\end{pmatrix}\,, |  | (A228) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒦22\displaystyle\mathcal{K}\_{22} | =B12⊤​D+D⊤​B12=(2​z000).\displaystyle=B\_{12}^{\top}\,D+D^{\top}\,B\_{12}=\begin{pmatrix}2\,z&0\\ 0&0\end{pmatrix}\,. |  | (A229) |

We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒦22⪯0\mathcal{K}\_{22}\preceq 0 |  | (A230) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I−𝒦22​𝒦22†)​𝒦12⊤=(0001)​(cw00)=(0000).(I-\mathcal{K}\_{22}\,\mathcal{K}\_{22}^{\dagger})\,\mathcal{K}\_{12}^{\top}=\begin{pmatrix}0&0\\ 0&1\end{pmatrix}\,\begin{pmatrix}c&w\\ 0&0\end{pmatrix}=\begin{pmatrix}0&0\\ 0&0\end{pmatrix}\,. |  | (A231) |

Also, consider

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒦11−𝒦12​𝒦22†​𝒦12⊤\displaystyle\mathcal{K}\_{11}-\mathcal{K}\_{12}\,\mathcal{K}\_{22}^{\dagger}\,\mathcal{K}\_{12}^{\top} | =(−2​ββ​zkβ​zkϕ​zk)−(c0w0)​(12​z000)​(cw00)=(−2​β−c22​z00ϕ​zk−w22​z).\displaystyle=\begin{pmatrix}-2\,\beta&\tfrac{\beta\,z}{k}\\ \tfrac{\beta\,z}{k}&\tfrac{\phi\,z}{k}\end{pmatrix}-\begin{pmatrix}c&0\\ w&0\end{pmatrix}\,\begin{pmatrix}\tfrac{1}{2\,z}&0\\ 0&0\end{pmatrix}\,\begin{pmatrix}c&w\\ 0&0\end{pmatrix}=\begin{pmatrix}-2\,\beta-\tfrac{c^{2}}{2\,z}&0\\ 0&\tfrac{\phi\,z}{k}-\tfrac{w^{2}}{2\,z}\end{pmatrix}\,. |  | (A232) |

Due to ([A223](https://arxiv.org/html/2512.19838v1#S1.E223 "In G Proof of Proposition 4 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | −2​β−c22​z<−2​β+c22⋅2​βc2=−β<0-2\,\beta-\frac{c^{2}}{2\,z}<-2\,\beta+\frac{c^{2}}{2}\cdot\frac{2\,\beta}{c^{2}}=-\beta<0 |  | (A233) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​zk−w22​z=ϕ​zk−2​β2​z3c2​η2=zk​(ϕ−2​β2​z2c2​η)<zk​(ϕ−2​β2c2​η⋅ϕ​c2​η2​β2)=0,\displaystyle\frac{\phi\,z}{k}-\frac{w^{2}}{2\,z}=\frac{\phi\,z}{k}-\frac{2\,\beta^{2}\,z^{3}}{c^{2}\,\eta^{2}}=\frac{z}{k}\left(\phi-\frac{2\,\beta^{2}\,z^{2}}{c^{2}\,\eta}\right)<\frac{z}{k}\left(\phi-\frac{2\,\beta^{2}}{c^{2}\,\eta}\cdot\frac{\phi\,c^{2}\,\eta}{2\,\beta^{2}}\right)=0, |  | (A234) |

so

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒦11−𝒦12​𝒦22†​𝒦12⊤≺0.\mathcal{K}\_{11}-\mathcal{K}\_{12}\,\mathcal{K}\_{22}^{\dagger}\,\mathcal{K}\_{12}^{\top}\prec 0\,. |  | (A235) |

Combining ([A230](https://arxiv.org/html/2512.19838v1#S1.E230 "In G Proof of Proposition 4 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), ([A231](https://arxiv.org/html/2512.19838v1#S1.E231 "In G Proof of Proposition 4 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), and ([A235](https://arxiv.org/html/2512.19838v1#S1.E235 "In G Proof of Proposition 4 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), we conclude

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ+ℒ⊤⪯0.\mathcal{L}+\mathcal{L}^{\top}\preceq 0\,. |  | (A236) |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | C+D​G+G⊤​D⊤=(100w+c​zk)≻0,C+D\,G+G^{\top}\,D^{\top}=\begin{pmatrix}1&0\\ 0&w+\tfrac{c\,z}{k}\end{pmatrix}\succ 0\,, |  | (A237) |

since ([A223](https://arxiv.org/html/2512.19838v1#S1.E223 "In G Proof of Proposition 4 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | w+c​zk=2​β​z2c​η+c​zk=z​(2​β​zc​η+ck)>z​(−2​βc​η⋅c22​β+ck)=0.w+\frac{c\,z}{k}=\frac{2\,\beta\,z^{2}}{c\,\eta}+\frac{c\,z}{k}=z\,\left(\frac{2\,\beta\,z}{c\,\eta}+\frac{c}{k}\right)>z\,\left(-\frac{2\,\beta}{c\,\eta}\cdot\frac{c^{2}}{2\,\beta}+\frac{c}{k}\right)=0\,. |  | (A238) |

By Theorem 2.3 in freiling2000, DRE ([48](https://arxiv.org/html/2512.19838v1#S4.E48 "In Proposition 4: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) has a unique solution.

∎

### H Proof of Proposition [5](https://arxiv.org/html/2512.19838v1#Thmproposition5 "Proposition 5: ‣ D No transient impact ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

The LP’s optimisation problem reduces to solving the following simplified FBSDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​νt=(ϕ2​η​Qt+−At​Ft+ϕ​Yt2​η)​d​t+12​η​d​Mt,νT=0d​Qt=νt​d​t,\displaystyle\left\{\begin{array}[]{rlrl}\mathrm{d}\nu\_{t}&=\left(\tfrac{\phi}{2\,\eta}\,Q\_{t}+\tfrac{-A\_{t}\,F\_{t}+\phi\,Y\_{t}}{2\,\eta}\right)\,{\mathrm{d}t}+\tfrac{1}{2\,\eta}\,\mathrm{d}M\_{t},&\nu\_{T}&=0\\ \mathrm{d}Q\_{t}&=\nu\_{t}\,{\mathrm{d}t},&&\end{array}\right. |  | (A241) |

and the ansatz νt=P​(t)​Qt+ℓt\nu\_{t}=P(t)\,Q\_{t}+\ell\_{t} gives the equations

|  |  |  |  |
| --- | --- | --- | --- |
|  | P′​(t)=−P​(t)2+ϕ2​η,P​(T)=0P^{\prime}(t)=-P(t)^{2}+\tfrac{\phi}{2\,\eta},\quad P(T)=0 |  | (A242) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℓt=(−P​(t)​ℓt+−At​Ft+ϕ​Yt2​η)​d​t+12​η​d​Mt,ℓT=0\mathrm{d}\ell\_{t}=\left(-P(t)\,\ell\_{t}+\tfrac{-A\_{t}\,F\_{t}+\phi\,Y\_{t}}{2\,\eta}\right){\mathrm{d}t}+\tfrac{1}{2\,\eta}\,\mathrm{d}M\_{t},\quad\ell\_{T}=0 |  | (A243) |

The solution of ([A242](https://arxiv.org/html/2512.19838v1#S1.E242 "In H Proof of Proposition 5 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) is

|  |  |  |
| --- | --- | --- |
|  | P​(t)=ϕ2​η​tanh⁡(ϕ2​η​(t−T)).\displaystyle P(t)=\sqrt{\tfrac{\phi}{2\,\eta}}\tanh\left(\sqrt{\tfrac{\phi}{2\,\eta}}(t-T)\right)\,. |  |

To solve ([A243](https://arxiv.org/html/2512.19838v1#S1.E243 "In H Proof of Proposition 5 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | P~​(s,t)≔e∫stP​(u)​du=cosh⁡(ϕ2​η​(t−T))cosh⁡(ϕ2​η​(s−T))\tilde{P}(s,t)\coloneqq e^{\int\_{s}^{t}P(u)\,\mathrm{d}u}=\frac{\cosh\left(\sqrt{\tfrac{\phi}{2\,\eta}}(t-T)\right)}{\cosh\left(\sqrt{\tfrac{\phi}{2\,\eta}}(s-T)\right)} |  | (A244) |

and use generalized Itô’s formula to write

|  |  |  |  |
| --- | --- | --- | --- |
|  | P~​(0,t)​ℓt\displaystyle\tilde{P}(0,t)\,\ell\_{t} | =−∫tTP~​(0,s)​P​(s)​ℓs​ds−∫tTP~​(0,s)​dℓs\displaystyle=-\int\_{t}^{T}\tilde{P}(0,s)\,P(s)\,\ell\_{s}\,{\mathrm{d}s}-\int\_{t}^{T}\tilde{P}(0,s)\,\mathrm{d}\ell\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∫tTP~​(0,s)​P​(s)​ℓs​ds−∫tTP~​(0,s)​(−P​(s)​ℓs+−As​Fs+ϕ​Ys2​η)​ds−12​η​∫tTP~​(0,s)​dMs\displaystyle=-\int\_{t}^{T}\tilde{P}(0,s)\,P(s)\,\ell\_{s}\,{\mathrm{d}s}-\int\_{t}^{T}\tilde{P}(0,s)\,\left(-P(s)\,\ell\_{s}+\tfrac{-A\_{s}\,F\_{s}+\phi\,Y\_{s}}{2\,\eta}\right)\,{\mathrm{d}s}-\tfrac{1}{2\,\eta}\int\_{t}^{T}\tilde{P}(0,s)\,\mathrm{d}M\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​η​∫tTP~​(0,s)​(As​Fs−ϕ​Ys)​ds−12​η​∫tTP~​(0,s)​dMs,\displaystyle=\tfrac{1}{2\,\eta}\int\_{t}^{T}\tilde{P}(0,s)\,(A\_{s}\,F\_{s}-\phi\,Y\_{s})\,{\mathrm{d}s}-\tfrac{1}{2\,\eta}\int\_{t}^{T}\tilde{P}(0,s)\,\mathrm{d}M\_{s}, |  |

therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓt=12​η​𝔼​[∫tTP~​(t,s)​(As​Fs−ϕ​Ys)​ds|ℱt].\ell\_{t}=\tfrac{1}{2\,\eta}\,\mathbb{E}\left[\left.\int\_{t}^{T}\tilde{P}(t,s)\,(A\_{s}\,F\_{s}-\phi\,Y\_{s})\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]. |  | (A245) |

Similarly, QQ is obtained by solving the equation

|  |  |  |
| --- | --- | --- |
|  | d​Qt=(P​(t)​Qt+ℓt)​d​t,\mathrm{d}Q\_{t}=(P(t)\,Q\_{t}+\ell\_{t})\,{\mathrm{d}t}, |  |

whose solution is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qt=Q0​P~​(0,t)+∫0tP~​(s,t)​ℓs​ds.\displaystyle Q\_{t}=Q\_{0}\,\tilde{P}(0,t)+\int\_{0}^{t}\tilde{P}(s,t)\,\ell\_{s}\,{\mathrm{d}s}. |  | (A246) |

Finally,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | νt\displaystyle\nu\_{t} | =P​(t)​Qt+ℓt\displaystyle=P(t)\,Q\_{t}+\ell\_{t} |  | (A247) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =P​(t)​(Q0​P~​(0,t)+∫0tP~​(s,t)​ℓs​ds)+ℓt\displaystyle=P(t)\,\left(Q\_{0}\,\tilde{P}(0,t)+\int\_{0}^{t}\tilde{P}(s,t)\,\ell\_{s}\,{\mathrm{d}s}\right)+\ell\_{t} |  | (A248) |

∎

### I Proof of Proposition [6](https://arxiv.org/html/2512.19838v1#Thmproposition6 "Proposition 6: ‣ V Stage one: liquidity supply ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

Let κ>0\kappa>0. By Lemma [3](https://arxiv.org/html/2512.19838v1#Thmlemma3 "Lemma 3: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"), The quantity ([53](https://arxiv.org/html/2512.19838v1#S5.E53 "In Proposition 6: ‣ V Stage one: liquidity supply ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​[ν⋆]+H+H~,\displaystyle J[\nu^{\star}]+H+\tilde{H}\,, |  | (A249) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | H=𝔼​[∫0T{(Gt+σ2​∂1h​(Ft,κ))​Ft2+At​Ft​(Yt−Y0)−ϕ2​(Yt−Y0)2}​dt]\displaystyle H=\mathbb{E}\!\left[\int\_{0}^{T}\left\{\left(G\_{t}+\sigma^{2}\,\partial\_{1}h(F\_{t},\kappa)\right)\,F\_{t}^{2}+A\_{t}\,F\_{t}\,(Y\_{t}-Y\_{0})-\tfrac{\phi}{2}\,(Y\_{t}-Y\_{0})^{2}\right\}\,{\mathrm{d}t}\right] |  | (A250) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | H~≔𝔼​[∫0TΠ​(Ft,κ)​dt+XT].\displaystyle\tilde{H}\coloneqq\mathbb{E}\!\left[\int\_{0}^{T}\Pi(F\_{t},\kappa)\,{\mathrm{d}t}+X\_{T}\right]\,. |  | (A251) |

Since HH and J​[ν⋆]J[\nu^{\star}] are well-defined, it remains to show H~\tilde{H} is well-defined. Recall that h​(⋅,κ)h(\cdot,\kappa) is the inverse of −∂1φ​(⋅,κ)-\partial\_{1}\varphi(\cdot,\kappa), so

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∂11φ​(h​(x,κ),κ)=1∂1h​(x,κ),∀x>0.-\partial\_{11}\varphi(h(x,\kappa),\kappa)=\frac{1}{\partial\_{1}h(x,\kappa)}\,,\quad\forall x>0\,. |  | (A252) |

By Itô’s formula and ([IV.A](https://arxiv.org/html/2512.19838v1#S4.Ex5 "A Assumptions ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | XT=φ​(YT,κ)\displaystyle X\_{T}=\varphi(Y\_{T},\kappa) | =φ​(Y0,κ)+∫0T∂1φ​(Yt,κ)​d​Yt+12​∫0T∂11φ​(Yt,κ)​d​⟨Y⟩t\displaystyle=\varphi(Y\_{0},\kappa)+\int\_{0}^{T}\partial\_{1}\varphi(Y\_{t},\kappa)\,\mathrm{d}Y\_{t}+\frac{1}{2}\int\_{0}^{T}\partial\_{11}\varphi(Y\_{t},\kappa)\,\mathrm{d}\langle Y\rangle\_{t} |  | (A253) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =φ​(Y0,κ)−∫0TFt​dYt−12​∫0T1∂1h​(Ft,κ)​d​⟨Y⟩t\displaystyle=\varphi(Y\_{0},\kappa)-\int\_{0}^{T}F\_{t}\,\mathrm{d}Y\_{t}-\frac{1}{2}\int\_{0}^{T}\frac{1}{\partial\_{1}h(F\_{t},\kappa)}\,\mathrm{d}\langle Y\rangle\_{t} |  | (A254) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =φ​(h​(F0,κ),κ)−∫0T(Gt+σ22​∂1h​(Ft,κ))​Ft2​dt−σ​∫0T∂1h​(Ft,κ)​Ft2​d​Wt.\displaystyle=\varphi(h(F\_{0},\kappa),\kappa)-\int\_{0}^{T}\left(G\_{t}+\frac{\sigma^{2}}{2}\,\partial\_{1}h(F\_{t},\kappa)\right)\,F\_{t}^{2}\,{\mathrm{d}t}-\sigma\int\_{0}^{T}\partial\_{1}h(F\_{t},\kappa)\,F\_{t}^{2}\,\mathrm{d}W\_{t}\,. |  | (A255) |

We know from Lemma [2](https://arxiv.org/html/2512.19838v1#Thmlemma2 "Lemma 2: ‣ B The performance criterion ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") that GG, ∂1h​(F,κ)\partial\_{1}h(F,\kappa), and F2F^{2} are in 𝒜2{\mathcal{A}}\_{2}, so

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T(Gt+σ22​∂1h​(Ft,κ))​Ft2​dt]=⟨G,F2⟩+σ22​⟨∂1h​(F,κ),F2⟩\mathbb{E}\!\left[\int\_{0}^{T}\left(G\_{t}+\frac{\sigma^{2}}{2}\,\partial\_{1}h(F\_{t},\kappa)\right)\,F\_{t}^{2}\,{\mathrm{d}t}\right]=\left\langle G,F^{2}\right\rangle+\frac{\sigma^{2}}{2}\,\left\langle\partial\_{1}h(F,\kappa),F^{2}\right\rangle |  | (A256) |

is well-defined. Since

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T(∂1h​(Ft,κ))2​Ft4​dt]≤‖(∂1h​(F,κ))2‖​‖F4‖<∞,\mathbb{E}\!\left[\int\_{0}^{T}(\partial\_{1}h(F\_{t},\kappa))^{2}\,F\_{t}^{4}\,{\mathrm{d}t}\right]\leq\left\|(\partial\_{1}h(F,\kappa))^{2}\right\|\,\left\|F^{4}\right\|<\infty, |  | (A257) |

the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0t∂1h​(Fs,κ)​Fs2​d​Ws,0≤t≤T,\int\_{0}^{t}\partial\_{1}h(F\_{s},\kappa)\,F\_{s}^{2}\,\mathrm{d}W\_{s}\,,\quad 0\leq t\leq T\,, |  | (A258) |

is a martingale, so

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T∂1h​(Ft,κ)​Ft2​d​Wt]=0.\mathbb{E}\!\left[\int\_{0}^{T}\partial\_{1}h(F\_{t},\kappa)\,F\_{t}^{2}\,\mathrm{d}W\_{t}\right]=0\,. |  | (A259) |

Therefore, 𝔼​[XT]\mathbb{E}[X\_{T}] is well-defined, with

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[XT]=φ​(h​(F0,κ),κ)−𝔼​[∫0T(Gt+σ22​∂1h​(Ft,κ))​Ft2​dt].\mathbb{E}[X\_{T}]=\varphi(h(F\_{0},\kappa),\kappa)-\mathbb{E}\!\left[\int\_{0}^{T}\left(G\_{t}+\frac{\sigma^{2}}{2}\,\partial\_{1}h(F\_{t},\kappa)\right)\,F\_{t}^{2}\,{\mathrm{d}t}\right]\,. |  | (A260) |

On the other hand, ([A252](https://arxiv.org/html/2512.19838v1#S1.E252 "In I Proof of Proposition 6 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π​(Ft,κ)=λ​π​(v−π)​Ft2∂11φ​(h​(Ft,κ),κ)=λ​π​(π−v)​∂1h​(Ft,κ)​Ft2,\Pi(F\_{t},\kappa)=\frac{\lambda\,\pi\,(v-\pi)\,F\_{t}^{2}}{\partial\_{11}\varphi\left(h(F\_{t},\kappa),\kappa\right)}=\lambda\,\pi\,(\pi-v)\,\partial\_{1}h(F\_{t},\kappa)\,F\_{t}^{2}\,, |  | (A261) |

so

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0TΠ​(Ft,κ)​dt]=λ​π​(π−v)​𝔼​[∫0T∂1h​(Ft,κ)​Ft2​d​t]=λ​π​(π−v)​⟨∂1h​(F,κ),F2⟩\mathbb{E}\!\left[\int\_{0}^{T}\Pi(F\_{t},\kappa)\,{\mathrm{d}t}\right]=\lambda\,\pi\,(\pi-v)\,\mathbb{E}\!\left[\int\_{0}^{T}\partial\_{1}h(F\_{t},\kappa)\,F\_{t}^{2}\,{\mathrm{d}t}\right]=\lambda\,\pi\,(\pi-v)\,\left\langle\partial\_{1}h(F,\kappa),F^{2}\right\rangle |  | (A262) |

is well-defined. It follows that H~\tilde{H} is well-defined and ([53](https://arxiv.org/html/2512.19838v1#S5.E53 "In Proposition 6: ‣ V Stage one: liquidity supply ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​[ν⋆]+𝔼​[∫0T{(σ22+λ​π​(π−v))​∂1h​(Ft,κ)​Ft2+At​Ft​(Yt−Y0)−ϕ2​(Yt−Y0)2}​dt].J[\nu^{\star}]+\mathbb{E}\!\left[\int\_{0}^{T}\left\{\left(\frac{\sigma^{2}}{2}+\lambda\,\pi\,(\pi-v)\right)\,\partial\_{1}h(F\_{t},\kappa)\,F\_{t}^{2}+A\_{t}\,F\_{t}\,(Y\_{t}-Y\_{0})-\tfrac{\phi}{2}\,(Y\_{t}-Y\_{0})^{2}\right\}\,{\mathrm{d}t}\right]\,. |  | (A263) |

∎

### J Proof of Proposition [7](https://arxiv.org/html/2512.19838v1#Thmproposition7 "Proposition 7: ‣ V Stage one: liquidity supply ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

By Proposition [6](https://arxiv.org/html/2512.19838v1#Thmproposition6 "Proposition 6: ‣ V Stage one: liquidity supply ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"), it is enough to show J​[ν⋆]J[\nu^{\star}] and

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^≔𝔼​[∫0T{(σ22+λ​π​(π−v))​∂1h​(Ft,κ)​Ft2+At​Ft​(Yt−Y0)−ϕ2​(Yt−Y0)2}​dt],\hat{H}\coloneqq\mathbb{E}\!\left[\int\_{0}^{T}\left\{\left(\frac{\sigma^{2}}{2}+\lambda\,\pi\,(\pi-v)\right)\,\partial\_{1}h(F\_{t},\kappa)\,F\_{t}^{2}+A\_{t}\,F\_{t}\,(Y\_{t}-Y\_{0})-\frac{\phi}{2}\,(Y\_{t}-Y\_{0})^{2}\right\}\,{\mathrm{d}t}\right]\,, |  | (A264) |

are both continuous in κ\kappa. To that end, fix κn→κ\kappa\_{n}\to\kappa. Because

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Yt​(κn)−Yt​(κ)|=|h​(Ft,κn)−h​(Ft,κ)|≤(Ft𝔭+Ft𝔮)​|ℭ​(κn)−ℭ​(κ)|,\displaystyle|Y\_{t}(\kappa\_{n})-Y\_{t}(\kappa)|=|h(F\_{t},\kappa\_{n})-h(F\_{t},\kappa)|\leq\left(F\_{t}^{\mathfrak{p}}+F\_{t}^{\mathfrak{q}}\right)\,|\mathfrak{C}(\kappa\_{n})-\mathfrak{C}(\kappa)|\,, |  | (A265) |

we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖Y​(κn)−Y​(κ)‖=𝔼​[∫0T|Yt​(κn)−Yt​(κ)|2​dt]1/2\displaystyle\|Y(\kappa\_{n})-Y(\kappa)\|=\mathbb{E}\!\left[\int\_{0}^{T}|Y\_{t}(\kappa\_{n})-Y\_{t}(\kappa)|^{2}\,{\mathrm{d}t}\right]^{1/2} | ≤|ℭ​(κn)−ℭ​(κ)|​𝔼​[∫0T(Ft𝔭+Ft𝔮)2​dt]1/2\displaystyle\leq|\mathfrak{C}(\kappa\_{n})-\mathfrak{C}(\kappa)|\,\mathbb{E}\!\left[\int\_{0}^{T}\left(F\_{t}^{\mathfrak{p}}+F\_{t}^{\mathfrak{q}}\right)^{2}\,{\mathrm{d}t}\right]^{1/2} |  | (A266) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤|ℭ​(κn)−ℭ​(κ)|​(‖F𝔭‖+‖F𝔮‖)\displaystyle\leq|\mathfrak{C}(\kappa\_{n})-\mathfrak{C}(\kappa)|\,\left(\left\|F^{\mathfrak{p}}\right\|+\left\|F^{\mathfrak{q}}\right\|\right) |  | (A267) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Y0​(κn)−Y0​(κ)‖≤|ℭ​(κn)−ℭ​(κ)|​(‖F0𝔭‖+‖F0𝔮‖)\displaystyle\|Y\_{0}(\kappa\_{n})-Y\_{0}(\kappa)\|\leq|\mathfrak{C}(\kappa\_{n})-\mathfrak{C}(\kappa)|\,\left(\left\|F\_{0}^{\mathfrak{p}}\right\|+\left\|F\_{0}^{\mathfrak{q}}\right\|\right) |  | (A268) |

so the map κ↦Y​(κ)−Y0​(κ)\kappa\mapsto Y(\kappa)-Y\_{0}(\kappa) from (0,∞)(0,\infty) to 𝒜2{\mathcal{A}}\_{2} is continuous. It follows that κ↦H^​(κ)\kappa\mapsto\hat{H}(\kappa) is continuous as the composition of

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ↦(σ22+λ​π​(π−v))​⟨∂1h​(F,κ),F2⟩+⟨A​F,ζ⟩−ϕ2​‖ζ‖2\zeta\mapsto\left(\frac{\sigma^{2}}{2}+\lambda\,\pi\,(\pi-v)\right)\,\left\langle\partial\_{1}h(F,\kappa),F^{2}\right\rangle+\langle A\,F,\zeta\rangle-\frac{\phi}{2}\,\|\zeta\|^{2} |  | (A269) |

with κ↦Y​(κ)−Y0​(κ)\kappa\mapsto Y(\kappa)-Y\_{0}(\kappa).

Next, we consider J​[ν⋆]J[\nu^{\star}]. By Proposition [2](https://arxiv.org/html/2512.19838v1#Thmproposition2 "Proposition 2: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets") and Proposition [3](https://arxiv.org/html/2512.19838v1#Thmproposition3 "Proposition 3: ‣ C The optimal risk offsetting strategy ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"), ν⋆=Λ−1​b\nu^{\star}=\Lambda^{-1}b, so

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​[ν⋆]=−12​⟨Λ​Λ−1​b,Λ−1​b⟩+⟨b,Λ−1​b⟩=12​⟨b,Λ−1​b⟩,J[\nu^{\star}]=-\frac{1}{2}\,\left\langle\Lambda\Lambda^{-1}b,\Lambda^{-1}b\right\rangle+\left\langle b,\Lambda^{-1}b\right\rangle=\frac{1}{2}\,\left\langle b,\Lambda^{-1}b\right\rangle\,, |  | (A270) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | b=ℑ⊤​(F​G)+(c−β​ℑ⊤−ϕ​𝔔⊤)​(Y−Y0)+𝔔⊤​(A​F).b=\mathfrak{I}^{\top}(F\,G)+(c-\beta\,\mathfrak{I}^{\top}-\phi\,\mathfrak{Q}^{\top})(Y-Y\_{0})+\mathfrak{Q}^{\top}(A\,F)\,. |  | (A271) |

Since

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Gt​(κn)−Gt​(κ)|\displaystyle|G\_{t}(\kappa\_{n})-G\_{t}(\kappa)| | ≤|At|​|∂1h​(Ft,κn)−∂1h​(Ft,κ)|+σ22​Ft​|∂11h​(Ft,κn)−∂11h​(Ft,κ)|\displaystyle\leq|A\_{t}|\,|\partial\_{1}h(F\_{t},\kappa\_{n})-\partial\_{1}h(F\_{t},\kappa)|+\frac{\sigma^{2}}{2}F\_{t}\,|\partial\_{11}h(F\_{t},\kappa\_{n})-\partial\_{11}h(F\_{t},\kappa)| |  | (A272) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤(|At|+σ22​Ft)​(Ft𝔭+Ft𝔮)​|ℭ​(κn)−ℭ​(κ)|,\displaystyle\leq\left(|A\_{t}|+\frac{\sigma^{2}}{2}\,F\_{t}\right)\,\left(F\_{t}^{\mathfrak{p}}+F\_{t}^{\mathfrak{q}}\right)\,|\mathfrak{C}(\kappa\_{n})-\mathfrak{C}(\kappa)|\,, |  | (A273) |

we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ℑ⊤​(F​G​(κn))−ℑ⊤​(F​G​(κ))‖\displaystyle\|\mathfrak{I}^{\top}(F\,G(\kappa\_{n}))-\mathfrak{I}^{\top}(F\,G(\kappa))\| |  | (A274) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤‖ℑ⊤‖op​𝔼​[∫0TFt2​|Gt​(κn)−Gt​(κ)|2​dt]12\displaystyle\leq\left\|\mathfrak{I}^{\top}\right\|\_{\operatorname{op}}\,\mathbb{E}\!\left[\int\_{0}^{T}F\_{t}^{2}\,|G\_{t}(\kappa\_{n})-G\_{t}(\kappa)|^{2}\,{\mathrm{d}t}\right]^{\tfrac{1}{2}} |  | (A275) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤‖ℑ⊤‖op​𝔼​[∫0T(|At|+σ22​Ft)2​(Ft𝔭+1+Ft𝔮+1)2​|ℭ​(κn)−ℭ​(κ)|2​dt]12\displaystyle\leq\left\|\mathfrak{I}^{\top}\right\|\_{\operatorname{op}}\,\mathbb{E}\!\left[\int\_{0}^{T}\left(|A\_{t}|+\frac{\sigma^{2}}{2}\,F\_{t}\right)^{2}\,\left(F\_{t}^{\mathfrak{p}+1}+F\_{t}^{\mathfrak{q}+1}\right)^{2}\,|\mathfrak{C}(\kappa\_{n})-\mathfrak{C}(\kappa)|^{2}\,{\mathrm{d}t}\right]^{\tfrac{1}{2}} |  | (A276) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤‖ℑ⊤‖op​{𝔼​[∫0T|At|p​dt]1p​(‖F(𝔭+1)​pp−2‖p−2p+‖F(𝔮+1)​pp−2‖p−2p)+σ22​‖F𝔭+2+F𝔮+2‖}​|ℭ​(κn)−ℭ​(κ)|,\displaystyle\leq\left\|\mathfrak{I}^{\top}\right\|\_{\operatorname{op}}\,\left\{\mathbb{E}\,\left[\int\_{0}^{T}|A\_{t}|^{p}\,{\mathrm{d}t}\right]^{\tfrac{1}{p}}\,\left(\left\|F^{\tfrac{(\mathfrak{p}+1)\,p}{p-2}}\right\|^{\tfrac{p-2}{p}}+\left\|F^{\tfrac{(\mathfrak{q}+1)\,p}{p-2}}\right\|^{\tfrac{p-2}{p}}\right)+\frac{\sigma^{2}}{2}\,\left\|F^{\mathfrak{p}+2}+F^{\mathfrak{q}+2}\right\|\right\}\,|\mathfrak{C}(\kappa\_{n})-\mathfrak{C}(\kappa)|\,, |  | (A277) |

so κ↦ℑ⊤​(F​G​(κ))\kappa\mapsto\mathfrak{I}^{\top}(F\,G(\kappa)) is continuous and thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ↦b​(κ)=ℑ⊤​(F​G​(κ))+(c−β​ℑ⊤−ϕ​𝔔⊤)​(Y​(κ)−Y0​(κ))+𝔔⊤​(A​F)\kappa\mapsto b(\kappa)=\mathfrak{I}^{\top}(F\,G(\kappa))+(c-\beta\,\mathfrak{I}^{\top}-\phi\,\mathfrak{Q}^{\top})(Y(\kappa)-Y\_{0}(\kappa))+\mathfrak{Q}^{\top}(A\,F) |  | (A278) |

is continuous. It follows that κ↦J​[ν⋆]​(κ)=⟨Λ−1​b​(κ),b​(κ)⟩/2\kappa\mapsto J[\nu^{\star}](\kappa)=\left\langle\Lambda^{-1}b(\kappa),b(\kappa)\right\rangle/2 is continuous.
∎

### K Proof of Proposition [8](https://arxiv.org/html/2512.19838v1#Thmproposition8 "Proposition 8: ‣ B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

Recall that the stage-three trading volumes generate fee revenue ([21](https://arxiv.org/html/2512.19838v1#S3.E21 "In C Trading volumes ‣ III Stage three: trading volumes ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")). In the case of a CPM, these write

|  |  |  |
| --- | --- | --- |
|  | Π​(Ft,κ)=γ​κ​Ft,\Pi(F\_{t},\kappa)=\gamma\,\kappa\,\sqrt{F\_{t}}\,, |  |

where we define γ\gamma as in ([59](https://arxiv.org/html/2512.19838v1#S6.E59 "In Corollary 1: ‣ A Without private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")). In the no-replication case ν≡0\nu\equiv 0, the value function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0TΠ​(Ft,κ)​dt+XT+(YT−Y0)​FT−ϕ2​∫0T(Yt−Y0)2​dt]\displaystyle\mathbb{E}\left[\int\_{0}^{T}\Pi(F\_{t},\kappa)\,{\mathrm{d}t}+X\_{T}+(Y\_{T}-Y\_{0})\,F\_{T}-\tfrac{\phi}{2}\int\_{0}^{T}(Y\_{t}-Y\_{0})^{2}\,{\mathrm{d}t}\right] |  | (A279) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =𝔼​[∫0Tγ​κ​Ft1/2​dt+2​κ​FT1/2−κ​F0−1/2​FT−ϕ2​∫0Tκ2​(Ft−1/2−F0−1/2)2​dt]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\gamma\,\kappa\,F\_{t}^{1/2}\,{\mathrm{d}t}+2\,\kappa\,F\_{T}^{1/2}-\kappa\,F\_{0}^{-1/2}\,F\_{T}-\tfrac{\phi}{2}\int\_{0}^{T}\kappa^{2}\,\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right] |  | (A280) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =−ϕ2​𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt]​κ2+𝔼​[∫0Tγ​Ft1/2​dt+2​FT1/2−F0−1/2​FT]​κ.\displaystyle=-\tfrac{\phi}{2}\,\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]\kappa^{2}+\mathbb{E}\left[\int\_{0}^{T}\gamma\,F\_{t}^{1/2}\,{\mathrm{d}t}+2\,F\_{T}^{1/2}-F\_{0}^{-1/2}\,F\_{T}\right]\kappa\,. |  | (A281) |

In this case the optimal supply of liquidity is

|  |  |  |
| --- | --- | --- |
|  | κ¯=𝔼​[∫0Tγ​Ft1/2​dt+2​FT1/2−F0−1/2​FT]ϕ​𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt].\displaystyle\underline{\kappa}=\frac{\mathbb{E}\left[\int\_{0}^{T}\gamma\,F\_{t}^{1/2}\,{\mathrm{d}t}+2\,F\_{T}^{1/2}-F\_{0}^{-1/2}\,F\_{T}\right]}{\phi\,\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]}\,. |  |

In the no-transient-impact case, the solutions in ([51](https://arxiv.org/html/2512.19838v1#S4.E51 "In Proposition 5: ‣ D No transient impact ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"))–([A246](https://arxiv.org/html/2512.19838v1#S1.E246 "In H Proof of Proposition 5 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets"))–([50](https://arxiv.org/html/2512.19838v1#S4.E50 "In Proposition 5: ‣ D No transient impact ‣ IV Stage two: risk offsetting in the centralised exchange ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) become

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓt⋆\displaystyle\ell^{\star}\_{t} | =−κ​ϕ2​η​𝔼​[∫tTP~​(t,s)​Fs−1/2​ds|ℱt]⏟=⁣:−Ctℓ+12​η​𝔼​[∫tTP~​(t,s)​As​Fs​ds|ℱt]⏟=⁣:Dtℓ\displaystyle=-\kappa\ \underbrace{\tfrac{\phi}{2\,\eta}\mathbb{E}\left[\left.\int\_{t}^{T}\tilde{P}(t,s)\,F\_{s}^{-1/2}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]}\_{=:-C^{\ell}\_{t}}+\underbrace{\tfrac{1}{2\,\eta}\mathbb{E}\left[\left.\int\_{t}^{T}\tilde{P}(t,s)\,A\_{s}\,F\_{s}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right]}\_{=:D^{\ell}\_{t}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Qt⋆\displaystyle Q^{\star}\_{t} | =κ​∫0tP~​(s,t)​Csℓ​ds−F0−1/2​P~​(0,t)⏟=⁣:CtQ+∫0tP~​(s,t)​Dsℓ​ds⏟=⁣:DtQ\displaystyle=\kappa\ \underbrace{\int\_{0}^{t}\tilde{P}(s,t)\,C^{\ell}\_{s}\,{\mathrm{d}s}-F\_{0}^{-1/2}\,\tilde{P}(0,t)}\_{=:C^{Q}\_{t}}+\underbrace{\int\_{0}^{t}\tilde{P}(s,t)\,D^{\ell}\_{s}\,{\mathrm{d}s}}\_{=:D^{Q}\_{t}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | νt⋆\displaystyle\nu^{\star}\_{t} | =(P​(t)​CtQ+Ctℓ)⏟=⁣:Ctν​κ+P​(t)​DtQ+Dtℓ⏟=⁣:Dtν\displaystyle=\underbrace{\left(P(t)\,C^{Q}\_{t}+C^{\ell}\_{t}\right)}\_{=:C^{\nu}\_{t}}\,\kappa+\underbrace{P(t)\,D^{Q}\_{t}+D^{\ell}\_{t}}\_{=:D^{\nu}\_{t}} |  |

When ν=ν⋆\nu=\nu^{\star}, the value function is

|  |  |  |
| --- | --- | --- |
|  | −ϕ2​𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt]​κ2+𝔼​[∫0Tγ​Ft1/2​dt+2​FT1/2−F0−1/2​FT]​κ\displaystyle-\tfrac{\phi}{2}\,\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]\kappa^{2}+\mathbb{E}\left[\int\_{0}^{T}\gamma\,F\_{t}^{1/2}\,{\mathrm{d}t}+2\,F\_{T}^{1/2}-F\_{0}^{-1/2}\,F\_{T}\right]\kappa |  |
|  |  |  |
| --- | --- | --- |
|  | +𝔼​[(QT⋆+Y0)​FT−∫0T(Ft+η​νt⋆)​νt⋆​dt−ϕ2​∫0T((Qt⋆+Y0)2+2​(Qt⋆+Y0)​(Yt−Y0))​dt]\displaystyle\quad+\mathbb{E}\left[\left(Q^{\star}\_{T}+Y\_{0}\right)\,F\_{T}-\int\_{0}^{T}\left(F\_{t}+\eta\,\nu^{\star}\_{t}\right)\,\nu^{\star}\_{t}\,{\mathrm{d}t}-\tfrac{\phi}{2}\int\_{0}^{T}\left(\left(Q^{\star}\_{t}+Y\_{0}\right)^{2}+2\,\left(Q^{\star}\_{t}+Y\_{0}\right)\,\left(Y\_{t}-Y\_{0}\right)\right)\,{\mathrm{d}t}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =−ϕ2​𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt]​κ2+𝔼​[∫0Tγ​Ft1/2​dt+2​FT1/2−F0−1/2​FT]​κ\displaystyle=-\tfrac{\phi}{2}\,\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]\kappa^{2}+\mathbb{E}\left[\int\_{0}^{T}\gamma\,F\_{t}^{1/2}\,{\mathrm{d}t}+2\,F\_{T}^{1/2}-F\_{0}^{-1/2}\,F\_{T}\right]\kappa |  |
|  |  |  |
| --- | --- | --- |
|  | +𝔼[(CTQκ+DTQ+F0−1/2κ)FT−∫0T(Ft+η(Ctνκ+Dtν))(Ctνκ+Dtν)dt\displaystyle\quad\ +\mathbb{E}\left[\left(C^{Q}\_{T}\,\kappa+D^{Q}\_{T}+F\_{0}^{-1/2}\,\kappa\right)\,F\_{T}-\int\_{0}^{T}\left(F\_{t}+\eta\,\left(C^{\nu}\_{t}\,\kappa+D^{\nu}\_{t}\right)\right)\left(C^{\nu}\_{t}\,\kappa+D^{\nu}\_{t}\right)\,{\mathrm{d}t}\right. |  |
|  |  |  |
| --- | --- | --- |
|  | −ϕ2∫0T((CtQκ+DtQ+F0−1/2κ)2+2(CtQκ+DtQ+F0−1/2κ)(Ft−1/2−F0−1/2)κ)dt]\displaystyle\quad\quad\quad\quad\left.-\tfrac{\phi}{2}\int\_{0}^{T}\left(\left(C^{Q}\_{t}\,\kappa+D^{Q}\_{t}+F\_{0}^{-1/2}\,\kappa\right)^{2}+2\left(C^{Q}\_{t}\,\kappa+D^{Q}\_{t}+F\_{0}^{-1/2}\,\kappa\right)\,\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)\,\kappa\right)\,{\mathrm{d}t}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =−ϕ2​𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt]​κ2+𝔼​[∫0Tγ​Ft1/2​dt+2​FT1/2−F0−1/2​FT]​κ\displaystyle=-\tfrac{\phi}{2}\,\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]\kappa^{2}+\mathbb{E}\left[\int\_{0}^{T}\gamma\,F\_{t}^{1/2}\,{\mathrm{d}t}+2\,F\_{T}^{1/2}-F\_{0}^{-1/2}\,F\_{T}\right]\kappa |  |
|  |  |  |
| --- | --- | --- |
|  | −𝔼​[∫0T(η​(Ctν)2+ϕ2​(CtQ+F0−1/2)2+ϕ​(CtQ+F0−1/2)​(Ft−1/2−F0−1/2))​dt]​κ2\displaystyle\quad\ -\mathbb{E}\left[\int\_{0}^{T}\left(\eta\,\left(C^{\nu}\_{t}\right)^{2}+\tfrac{\phi}{2}\,\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)^{2}+\phi\,\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)\right)\,{\mathrm{d}t}\right]\,\kappa^{2} |  |
|  |  |  |
| --- | --- | --- |
|  | +𝔼​[(CTQ+F0−1/2)​FT−∫0T(Ctν​Ft+2​η​Ctν​Dtν+ϕ​DtQ​(CtQ+Ft−1/2))​dt]​κ\displaystyle\quad\ +\mathbb{E}\left[\left(C^{Q}\_{T}+F\_{0}^{-1/2}\right)\,F\_{T}-\int\_{0}^{T}\left(C^{\nu}\_{t}\,F\_{t}+2\,\eta\,C^{\nu}\_{t}\,D^{\nu}\_{t}+\phi\,D^{Q}\_{t}\,\left(C^{Q}\_{t}+F\_{t}^{-1/2}\right)\right)\,{\mathrm{d}t}\right]\,\kappa |  |
|  |  |  |
| --- | --- | --- |
|  | +𝔼​[DTQ​FT−∫0T(Ft​Dtν+η​(Dtν)2+ϕ2​(DtQ)2)​dt].\displaystyle\quad\ +\mathbb{E}\left[D^{Q}\_{T}\,F\_{T}-\int\_{0}^{T}\left(F\_{t}\,D^{\nu}\_{t}+\eta\,\left(D^{\nu}\_{t}\right)^{2}+\tfrac{\phi}{2}\,\left(D^{Q}\_{t}\right)^{2}\right)\,{\mathrm{d}t}\right]\,. |  |

In this case the optimal κ\kappa is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | κ⋆\displaystyle\kappa^{\star} | =𝔄+𝔼​[∫0Tγ​Ft1/2​dt+2​FT1/2−F0−1/2​FT]ϕ​(𝔅+𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt])\displaystyle=\frac{\mathfrak{A}+\mathbb{E}\left[\int\_{0}^{T}\gamma\,F\_{t}^{1/2}\,{\mathrm{d}t}+2\,F\_{T}^{1/2}-F\_{0}^{-1/2}\,F\_{T}\right]}{\phi\,\left(\mathfrak{B}+\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]\right)} |  | (A282) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(κ¯+𝔄ϕ​𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt])​𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt]𝔅+𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt]\displaystyle=\left(\underline{\kappa}+\frac{\mathfrak{A}}{\phi\,\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]}\right)\frac{\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]}{\mathfrak{B}+\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]} |  | (A283) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔄≔𝔼​[(CTQ+F0−1/2)​FT−∫0T(Ctν​Ft+2​η​Ctν​Dtν+ϕ​DtQ​(CtQ+Ft−1/2))​dt],\mathfrak{A}\coloneqq\mathbb{E}\left[\left(C^{Q}\_{T}+F\_{0}^{-1/2}\right)\,F\_{T}-\int\_{0}^{T}\left(C^{\nu}\_{t}\,F\_{t}+2\,\eta\,C^{\nu}\_{t}\,D^{\nu}\_{t}+\phi\,D^{Q}\_{t}\,\left(C^{Q}\_{t}+F\_{t}^{-1/2}\right)\right)\,{\mathrm{d}t}\right]\,, |  | (A284) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔅≔𝔼​[∫0T(2​ηϕ​(Ctν)2+(CtQ+F0−1/2)2+2​(CtQ+F0−1/2)​(Ft−1/2−F0−1/2))​dt].\mathfrak{B}\coloneqq\mathbb{E}\left[\int\_{0}^{T}\left(\tfrac{2\,\eta}{\phi}\,\left(C^{\nu}\_{t}\right)^{2}+\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)^{2}+2\,\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)\right)\,{\mathrm{d}t}\right]\,. |  | (A285) |

We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ctℓ\displaystyle C^{\ell}\_{t} | =−ϕ2​η​𝔼​[∫tTP~​(t,s)​Fs−1/2​ds|ℱt]\displaystyle=-\tfrac{\phi}{2\,\eta}\mathbb{E}\left[\left.\int\_{t}^{T}\tilde{P}(t,s)\,F\_{s}^{-1/2}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−ϕ2​η​P~​(t,0)​𝔼​[∫tTP~​(0,s)​Fs−1/2​ds|ℱt]\displaystyle=-\tfrac{\phi}{2\,\eta}\,\tilde{P}(t,0)\,\mathbb{E}\left[\left.\int\_{t}^{T}\tilde{P}(0,s)\,F\_{s}^{-1/2}\,{\mathrm{d}s}\,\right|\,{\mathcal{F}}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−ϕ2​η​P~​(t,0)​(M~t−∫0tP~​(0,s)​Fs−1/2​ds),\displaystyle=-\tfrac{\phi}{2\,\eta}\,\tilde{P}(t,0)\left(\tilde{M}\_{t}-\int\_{0}^{t}\tilde{P}(0,s)\,F\_{s}^{-1/2}{\mathrm{d}s}\right)\,, |  |

Then generalized Itô’s formula gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ctℓ\displaystyle\mathrm{d}C^{\ell}\_{t} | =−P​(t)​Ctℓ​d​t−ϕ2​η​P~​(t,0)​(d​M~t−P~​(0,t)​Ft−1/2​d​t)\displaystyle=-P(t)\,C^{\ell}\_{t}\,{\mathrm{d}t}-\tfrac{\phi}{2\,\eta}\,\tilde{P}(t,0)\,\left(\mathrm{d}\tilde{M}\_{t}-\tilde{P}(0,t)\,F\_{t}^{-1/2}\,{\mathrm{d}t}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(−P​(t)​Ctℓ+ϕ2​η​Ft−1/2)​d​t−ϕ2​η​P~​(t,0)​d​M~t.\displaystyle=\left(-P(t)\,C^{\ell}\_{t}+\tfrac{\phi}{2\,\eta}\,F\_{t}^{-1/2}\right)\,{\mathrm{d}t}-\tfrac{\phi}{2\,\eta}\,\tilde{P}(t,0)\,\mathrm{d}\tilde{M}\_{t}. |  | (A286) |

Since

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Ctν\displaystyle\mathrm{d}C^{\nu}\_{t} | =P′​(t)​CtQ​d​t+P​(t)​Ctν​d​t+d​Ctℓ\displaystyle=P^{\prime}(t)\,C^{Q}\_{t}\,{\mathrm{d}t}+P(t)\,C^{\nu}\_{t}\,{\mathrm{d}t}+\mathrm{d}C^{\ell}\_{t} |  | (A287) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(P′​(t)​CtQ+P​(t)​(P​(t)​CtQ+Ctℓ)−P​(t)​Ctℓ+ϕ2​η​Ft−1/2)​d​t−ϕ2​η​P~​(t,0)​d​M~t\displaystyle=\left(P^{\prime}(t)\,C^{Q}\_{t}+P(t)\,\left(P(t)\,C^{Q}\_{t}+C^{\ell}\_{t}\right)-P(t)\,C^{\ell}\_{t}+\tfrac{\phi}{2\,\eta}\,F\_{t}^{-1/2}\right)\,{\mathrm{d}t}-\tfrac{\phi}{2\,\eta}\,\tilde{P}(t,0)\,\mathrm{d}\tilde{M}\_{t} |  | (A288) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =((P′​(t)+P​(t)2)​CtQ+ϕ2​η​Ft−1/2)​d​t−ϕ2​η​P~​(t,0)​d​M~t\displaystyle=\left(\left(P^{\prime}(t)+P(t)^{2}\right)\,C^{Q}\_{t}+\tfrac{\phi}{2\,\eta}\,F\_{t}^{-1/2}\right)\,{\mathrm{d}t}-\tfrac{\phi}{2\,\eta}\,\tilde{P}(t,0)\,\mathrm{d}\tilde{M}\_{t} |  | (A289) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =ϕ2​η​(CtQ+Ft−1/2)​d​t−ϕ2​η​P~​(t,0)​d​M~t,\displaystyle=\tfrac{\phi}{2\,\eta}\,\left(C^{Q}\_{t}+F\_{t}^{-1/2}\right)\,{\mathrm{d}t}-\tfrac{\phi}{2\,\eta}\,\tilde{P}(t,0)\,\mathrm{d}\tilde{M}\_{t}\,, |  | (A290) |

where the last equality uses ([A242](https://arxiv.org/html/2512.19838v1#S1.E242 "In H Proof of Proposition 5 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")), and

|  |  |  |
| --- | --- | --- |
|  | d​(Ctν​DtQ)=[Ctν​Dtν+ϕ2​η​DtQ​(CtQ+Ft−1/2)]​d​t−ϕ2​η​P~​(t,0)​DtQ​d​M~t,\displaystyle\mathrm{d}\left(C^{\nu}\_{t}\,D^{Q}\_{t}\right)=\left[C^{\nu}\_{t}\,D^{\nu}\_{t}+\tfrac{\phi}{2\,\eta}\,D^{Q}\_{t}\,\left(C^{Q}\_{t}+F\_{t}^{-1/2}\right)\right]\,{\mathrm{d}t}-\tfrac{\phi}{2\,\eta}\,\tilde{P}(t,0)\,D^{Q}\_{t}\,\mathrm{d}\tilde{M}\_{t}\,, |  |

we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔄\displaystyle\mathfrak{A} | =𝔼​[(CTQ+F0−1/2)​FT−∫0T(Ctν​Ft+2​η​Ctν​Dtν+ϕ​DtQ​(CtQ+Ft−1/2))​dt]\displaystyle=\mathbb{E}\left[\left(C^{Q}\_{T}+F\_{0}^{-1/2}\right)\,F\_{T}-\int\_{0}^{T}\left(C^{\nu}\_{t}\,F\_{t}+2\,\eta\,C^{\nu}\_{t}\,D^{\nu}\_{t}+\phi\,D^{Q}\_{t}\,\left(C^{Q}\_{t}+F\_{t}^{-1/2}\right)\right)\,{\mathrm{d}t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼[∫0T(CtνFt+(CtQ+F0−1/2)AtFt)dt+σ∫0T(CtQ+F0−1/2)FtdWt\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left(C^{\nu}\_{t}\,F\_{t}+\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,A\_{t}\,F\_{t}\right){\mathrm{d}t}+\sigma\int\_{0}^{T}\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,F\_{t}\,\mathrm{d}W\_{t}\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0T(CtνFt+2ηCtνDtν+ϕDtQ(CtQ+Ft−1/2))dt]\displaystyle\quad\quad\quad\left.\phantom{\int\_{0}^{T}}-\int\_{0}^{T}\left(C^{\nu}\_{t}\,F\_{t}+2\,\eta\,C^{\nu}\_{t}\,D^{\nu}\_{t}+\phi\,D^{Q}\_{t}\,\left(C^{Q}\_{t}+F\_{t}^{-1/2}\right)\right)\,{\mathrm{d}t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T((CtQ+F0−1/2)​At​Ft−2​η​Ctν​Dtν−ϕ​DtQ​(CtQ+Ft−1/2))​dt]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left(\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,A\_{t}\,F\_{t}-2\,\eta\,C^{\nu}\_{t}\,D^{\nu}\_{t}-\phi\,D^{Q}\_{t}\,\left(C^{Q}\_{t}+F\_{t}^{-1/2}\right)\right)\,{\mathrm{d}t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T(CtQ+F0−1/2)​At​Ft​dt−2​η​(CTν​DTQ−C0ν​D0Q)−ϕ​∫0TP~​(t,0)​DtQ​dM~t]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,A\_{t}\,F\_{t}\,{\mathrm{d}t}-2\,\eta\,(C^{\nu}\_{T}\,D^{Q}\_{T}-C^{\nu}\_{0}\,D^{Q}\_{0})-\phi\int\_{0}^{T}\tilde{P}(t,0)\,D^{Q}\_{t}\,\mathrm{d}\tilde{M}\_{t}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼​[∫0T(CtQ+F0−1/2)​At​Ft​dt],\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,A\_{t}\,F\_{t}\,{\mathrm{d}t}\right]\,, |  | (A291) |

where the term 𝔼​[∫0T(CtQ+F0−1/2)​Ft​dWt]\mathbb{E}\left[\int\_{0}^{T}\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,F\_{t}\,\mathrm{d}W\_{t}\right] vanishes because

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|CtQ+F0−1/2|2​Ft2​dt]\displaystyle\mathbb{E}\left[\int\_{0}^{T}\left|C^{Q}\_{t}+F\_{0}^{-1/2}\right|^{2}\,F\_{t}^{2}\,{\mathrm{d}t}\right] |  | (A292) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≲𝔼​[∫0T|CtQ|2​Ft2​dt]+𝔼​[∫0TFt2​dt]\displaystyle\lesssim\mathbb{E}\left[\int\_{0}^{T}\left|C^{Q}\_{t}\right|^{2}\,F\_{t}^{2}\,{\mathrm{d}t}\right]+\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{2}\,{\mathrm{d}t}\right] |  | (A293) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤𝔼​[∫0T|CtQ|4​dt]1/2​𝔼​[∫0TFt4​dt]1/2+𝔼​[∫0TFt2​dt]\displaystyle\leq\mathbb{E}\left[\int\_{0}^{T}\left|C^{Q}\_{t}\right|^{4}\,{\mathrm{d}t}\right]^{1/2}\,\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{4}\,{\mathrm{d}t}\right]^{1/2}+\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{2}\,{\mathrm{d}t}\right] |  | (A294) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =𝔼​[∫0T|∫0tP~​(s,t)​Csℓ​ds−F0−1/2​P~​(0,t)|4​dt]1/2​𝔼​[∫0TFt4​dt]1/2+𝔼​[∫0TFt2​dt]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left|\int\_{0}^{t}\tilde{P}(s,t)\,C^{\ell}\_{s}\,{\mathrm{d}s}-F\_{0}^{-1/2}\,\tilde{P}(0,t)\right|^{4}\,{\mathrm{d}t}\right]^{1/2}\,\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{4}\,{\mathrm{d}t}\right]^{1/2}+\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{2}\,{\mathrm{d}t}\right] |  | (A295) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≲(𝔼​[∫0T|Ctℓ|4​dt]+F0−2)1/2​𝔼​[∫0TFt4​dt]1/2+𝔼​[∫0TFt2​dt]\displaystyle\lesssim\left(\mathbb{E}\left[\int\_{0}^{T}\left|C^{\ell}\_{t}\right|^{4}\,{\mathrm{d}t}\right]+F\_{0}^{-2}\right)^{1/2}\,\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{4}\,{\mathrm{d}t}\right]^{1/2}+\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{2}\,{\mathrm{d}t}\right] |  | (A296) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤(∫0T𝔼​[|∫tTP~​(t,s)​Fs−1/2​ds|4]​dt+F0−2)1/2​𝔼​[∫0TFt4​dt]1/2+𝔼​[∫0TFt2​dt]\displaystyle\leq\left(\int\_{0}^{T}\mathbb{E}\left[\left|\int\_{t}^{T}\tilde{P}(t,s)\,F\_{s}^{-1/2}\,{\mathrm{d}s}\right|^{4}\right]\,{\mathrm{d}t}+F\_{0}^{-2}\right)^{1/2}\,\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{4}\,{\mathrm{d}t}\right]^{1/2}+\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{2}\,{\mathrm{d}t}\right] |  | (A297) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≲(𝔼​[∫0TFt−2​dt]+F0−2)1/2​𝔼​[∫0TFt4​dt]1/2+𝔼​[∫0TFt2​dt]\displaystyle\lesssim\left(\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{-2}\,{\mathrm{d}t}\right]+F\_{0}^{-2}\right)^{1/2}\,\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{4}\,{\mathrm{d}t}\right]^{1/2}+\mathbb{E}\left[\int\_{0}^{T}F\_{t}^{2}\,{\mathrm{d}t}\right] |  | (A298) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | <∞.\displaystyle<\infty\,. |  | (A299) |

Next, we simplify 𝔅\mathfrak{B}. By ([A290](https://arxiv.org/html/2512.19838v1#S1.E290 "In K Proof of Proposition 8 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")),

|  |  |  |
| --- | --- | --- |
|  | d​(Ctν​(CtQ+F0−1/2))=[(Ctν)2+ϕ2​η​(CtQ+F0−1/2)​(CtQ+Ft−1/2)]​d​t−ϕ2​η​P~​(t,0)​(CtQ+F0−1/2)​d​M~t,\displaystyle\mathrm{d}\left(C^{\nu}\_{t}\,\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\right)=\left[\left(C^{\nu}\_{t}\right)^{2}+\tfrac{\phi}{2\,\eta}\,\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,\left(C^{Q}\_{t}+F\_{t}^{-1/2}\right)\right]\,{\mathrm{d}t}-\tfrac{\phi}{2\,\eta}\,\tilde{P}(t,0)\,\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,\mathrm{d}\tilde{M}\_{t}\,, |  |

It follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔅\displaystyle\mathfrak{B} | =𝔼​[∫0T(2​ηϕ​(Ctν)2+(CtQ+F0−1/2)2+2​(CtQ+F0−1/2)​(Ft−1/2−F0−1/2))​dt]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left(\tfrac{2\,\eta}{\phi}\,\left(C^{\nu}\_{t}\right)^{2}+\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)^{2}+2\,\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)\right)\,{\mathrm{d}t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T(2​ηϕ​(Ctν)2+(CtQ+F0−1/2)​(CtQ+Ft−1/2)+(CtQ+F0−1/2)​(Ft−1/2−F0−1/2))​dt]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left(\tfrac{2\,\eta}{\phi}\,\left(C^{\nu}\_{t}\right)^{2}+\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,\left(C^{Q}\_{t}+F\_{t}^{-1/2}\right)+\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)\right)\,{\mathrm{d}t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T(CtQ+F0−1/2)​(Ft−1/2−F0−1/2)​dt]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left(C^{Q}\_{t}+F\_{0}^{-1/2}\right)\,\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)\,{\mathrm{d}t}\right] |  |

On the other hand,

|  |  |  |
| --- | --- | --- |
|  | 𝔅+𝔼​[∫0T(Ft−1/2−F0−1/2)2​dt]=𝔼​[∫0T(2​ηϕ​(Ctν)2+(CtQ+Ft−1/2)2)​dt]≥0.\displaystyle\mathfrak{B}+\mathbb{E}\left[\int\_{0}^{T}\left(F\_{t}^{-1/2}-F\_{0}^{-1/2}\right)^{2}\,{\mathrm{d}t}\right]=\mathbb{E}\left[\int\_{0}^{T}\left(\tfrac{2\,\eta}{\phi}\,(C^{\nu}\_{t})^{2}+\left(C^{Q}\_{t}+F\_{t}^{-1/2}\right)^{2}\right)\,{\mathrm{d}t}\right]\geq 0\,. |  |

∎

### L Proof of Lemma [4](https://arxiv.org/html/2512.19838v1#Thmlemma4 "Lemma 4: ‣ B Risk offsetting and private information ‣ VI Constant product markets ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")

It is enough to show 𝔼​[∫0tP~​(t,0)2​(DtQ)2​d​⟨M~⟩t]<∞\mathbb{E}\left[\int\_{0}^{t}\tilde{P}(t,0)^{2}\,(D^{Q}\_{t})^{2}\,\mathrm{d}\langle\tilde{M}\rangle\_{t}\right]<\infty
and 𝔼​[∫0tP~​(t,0)2​(CtQ)2​d​⟨M~⟩t]<∞.\mathbb{E}\left[\int\_{0}^{t}\tilde{P}(t,0)^{2}\,(C^{Q}\_{t})^{2}\,\mathrm{d}\langle\tilde{M}\rangle\_{t}\right]<\infty\,.
If t≤st\leq s, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fs=F0​e∫0s(Au−σ22)​du+σ​Ws=Ft​e−σ22​(s−t)​e∫tsAu​du+σ​(Ws−Wt).\displaystyle F\_{s}=F\_{0}\,e^{\int\_{0}^{s}\left(A\_{u}-\tfrac{\sigma^{2}}{2}\right)\,{\mathrm{d}u}+\sigma\,W\_{s}}=F\_{t}\,e^{-\tfrac{\sigma^{2}}{2}\,(s-t)}\,e^{\int\_{t}^{s}A\_{u}\,{\mathrm{d}u}+\sigma\,(W\_{s}-W\_{t})}\,. |  | (A300) |

AA has the representation

|  |  |  |
| --- | --- | --- |
|  | Au=μ+(At−μ)​e−θ​(u−t)+ξ​∫tue−θ​(u−r)​dWrt≤u.\displaystyle A\_{u}=\mu+(A\_{t}-\mu)\,e^{-\theta\,(u-t)}+\xi\int\_{t}^{u}e^{-\theta\,(u-r)}\mathrm{d}W\_{r}\,\quad t\leq u\,. |  |

Since the integrand is jointly continuous, deterministic, and bounded, the stochastic Fubini theorem implies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∫tsAu​du\displaystyle\int\_{t}^{s}A\_{u}\,{\mathrm{d}u} | =μ​(s−t)+(At−μ)​1−e−θ​(s−t)θ+ξ​∫ts∫tue−θ​(u−r)​dWr​du\displaystyle=\mu\,(s-t)+(A\_{t}-\mu)\,\frac{1-e^{-\theta\,(s-t)}}{\theta}+\xi\int\_{t}^{s}\int\_{t}^{u}e^{-\theta\,(u-r)}\,\mathrm{d}W\_{r}\,{\mathrm{d}u} |  | (A301) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =μ​(s−t)+(At−μ)​1−e−θ​(s−t)θ+ξ​∫ts∫rse−θ​(u−r)​du​dWr\displaystyle=\mu\,(s-t)+(A\_{t}-\mu)\,\frac{1-e^{-\theta\,(s-t)}}{\theta}+\xi\int\_{t}^{s}\int\_{r}^{s}e^{-\theta\,(u-r)}\,{\mathrm{d}u}\,\mathrm{d}W\_{r} |  | (A302) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =μ​(s−t)+(At−μ)​1−e−θ​(s−t)θ+ξθ​∫ts(1−e−θ​(s−r))​dWr.\displaystyle=\mu\,(s-t)+(A\_{t}-\mu)\,\frac{1-e^{-\theta\,(s-t)}}{\theta}+\frac{\xi}{\theta}\int\_{t}^{s}\left(1-e^{-\theta\,(s-r)}\right)\,\mathrm{d}W\_{r}\,. |  | (A303) |

Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[Fs−1/2|ℱt]\displaystyle\mathbb{E}\left[\left.F\_{s}^{-1/2}\,\right|\,{\mathcal{F}}\_{t}\right] | =Ft−1/2​e(−μ2+σ24)​(s−t)−(At−μ)​(1−e−θ​(s−t))2​θ​𝔼​[e−12​∫ts(ξθ+σ−ξθ​e−θ​(s−r))​dWr],\displaystyle=F\_{t}^{-1/2}\,e^{\left(-\tfrac{\mu}{2}+\tfrac{\sigma^{2}}{4}\right)\,(s-t)-\tfrac{(A\_{t}-\mu)\,\left(1-e^{-\theta\,(s-t)}\right)}{2\,\theta}}\,\mathbb{E}\left[e^{-\tfrac{1}{2}\int\_{t}^{s}\left(\tfrac{\xi}{\theta}+\sigma-\tfrac{\xi}{\theta}\,e^{-\theta\,(s-r)}\right)\,\mathrm{d}W\_{r}}\right]\,, |  | (A304) |

where the quantity −12​∫ts(ξθ+σ−ξθ​e−θ​(s−r))​dWr-\tfrac{1}{2}\int\_{t}^{s}\left(\tfrac{\xi}{\theta}+\sigma-\tfrac{\xi}{\theta}\,e^{-\theta\,(s-r)}\right)\,\mathrm{d}W\_{r}, viewed as a Wiener integral, is a Gaussian random variable with mean zero and variance

|  |  |  |  |
| --- | --- | --- | --- |
|  | 14​∫ts(ξθ+σ−ξθ​e−θ​(s−r))2​dr,\tfrac{1}{4}\int\_{t}^{s}\left(\tfrac{\xi}{\theta}+\sigma-\tfrac{\xi}{\theta}\,e^{-\theta\,(s-r)}\right)^{2}\,\mathrm{d}r\,, |  | (A305) |

so

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[Fs−1/2|ℱt]\displaystyle\mathbb{E}\left[\left.F\_{s}^{-1/2}\,\right|\,{\mathcal{F}}\_{t}\right] | =Ft−1/2​e−At​(1−e−θ​(s−t))2​θ​e(−μ2+σ24)​(s−t)+μ​(1−e−θ​(s−t))2​θ+18​∫ts(ξθ+σ−ξθ​e−θ​(s−r))2​dr\displaystyle=F\_{t}^{-1/2}\,e^{-\tfrac{A\_{t}\,\left(1-e^{-\theta\,(s-t)}\right)}{2\,\theta}}\,e^{\left(-\tfrac{\mu}{2}+\tfrac{\sigma^{2}}{4}\right)\,(s-t)+\tfrac{\mu\,\left(1-e^{-\theta\,(s-t)}\right)}{2\,\theta}+\tfrac{1}{8}\int\_{t}^{s}\left(\tfrac{\xi}{\theta}+\sigma-\tfrac{\xi}{\theta}\,e^{-\theta\,(s-r)}\right)^{2}\,\mathrm{d}r} |  | (A306) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Ft−1/2​e−At​g​(s,t)​h​(s,t),\displaystyle=F\_{t}^{-1/2}\,e^{-A\_{t}\,g(s,t)}\,h(s,t)\,, |  | (A307) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(s,t)≔(1−e−θ​(s−t))2​θ\displaystyle g(s,t)\coloneqq\frac{\left(1-e^{-\theta\,(s-t)}\right)}{2\,\theta} |  | (A308) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(s,t)≔e(−μ2+σ24)​(s−t)+μ​(1−e−θ​(s−t))2​θ+18​∫ts(ξθ+σ−ξθ​e−θ​(s−r))2​dr.\displaystyle h(s,t)\coloneqq e^{\left(-\tfrac{\mu}{2}+\tfrac{\sigma^{2}}{4}\right)\,(s-t)+\tfrac{\mu\,\left(1-e^{-\theta\,(s-t)}\right)}{2\,\theta}+\tfrac{1}{8}\int\_{t}^{s}\left(\tfrac{\xi}{\theta}+\sigma-\tfrac{\xi}{\theta}\,e^{-\theta\,(s-r)}\right)^{2}\,\mathrm{d}r}\,. |  | (A309) |

Thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | M~t\displaystyle\tilde{M}\_{t} | =∫0tP~​(0,s)​Fs−1/2​ds+Ft−1/2​∫tTP~​(0,s)​e−At​g​(s,t)​h​(s,t)​ds\displaystyle=\int\_{0}^{t}\tilde{P}(0,s)\,F\_{s}^{-1/2}\,{\mathrm{d}s}+F\_{t}^{-1/2}\int\_{t}^{T}\tilde{P}(0,s)\,e^{-A\_{t}\,g(s,t)}\,h(s,t)\,{\mathrm{d}s} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0tP~​(0,s)​Fs−1/2​ds+Ft−1/2​H​(At,t)\displaystyle=\int\_{0}^{t}\tilde{P}(0,s)\,F\_{s}^{-1/2}\,{\mathrm{d}s}+F\_{t}^{-1/2}\,H(A\_{t},t)\, |  | (A310) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(a,t)≔∫tTP~​(0,s)​e−a​g​(s,t)​h​(s,t)​ds.\displaystyle H(a,t)\coloneqq\int\_{t}^{T}\tilde{P}(0,s)\,e^{-a\,g(s,t)}\,h(s,t)\,{\mathrm{d}s}\,. |  | (A311) |

Note that HH is smooth with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂1H​(a,t)=−∫tTP~​(0,s)​e−a​g​(s,t)​g​(s,t)​h​(s,t)​ds\displaystyle\partial\_{1}H(a,t)=-\int\_{t}^{T}\tilde{P}(0,s)\,e^{-a\,g(s,t)}\,g(s,t)\,h(s,t)\,{\mathrm{d}s} |  | (A312) |

Applying Itô to ([A310](https://arxiv.org/html/2512.19838v1#S1.E310 "In L Proof of Lemma 4 ‣ A Proofs ‣ Equilibrium Liquidity and Risk Offsetting in Decentralised Markets")) and using the fact that all finite variation terms must vanish since M~\tilde{M} is a martingale give

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​M~t=Ft−1/2​(ξ​∂1H​(At,t)−σ2​H​(At,t))​d​Wt.\displaystyle\mathrm{d}\tilde{M}\_{t}=F\_{t}^{-1/2}\,\left(\xi\,\partial\_{1}H(A\_{t},t)-\frac{\sigma}{2}\,H(A\_{t},t)\right)\,\mathrm{d}W\_{t}\,. |  | (A313) |

For any q≥1q\geq 1, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|ξ​∂1H​(At,t)−σ2​H​(At,t)|q​dt]\displaystyle\mathbb{E}\left[\int\_{0}^{T}\left|\xi\,\partial\_{1}H(A\_{t},t)-\frac{\sigma}{2}\,H(A\_{t},t)\right|^{q}\,{\mathrm{d}t}\right] |  | (A314) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =𝔼​[∫0T|∫tTP~​(0,s)​e−At​g​(s,t)​(ξ​g​(s,t)+σ2)​h​(s,t)​ds|q​dt]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\left|\int\_{t}^{T}\tilde{P}(0,s)\,e^{-A\_{t}\,g(s,t)}\,\left(\xi\,g(s,t)+\frac{\sigma}{2}\right)\,h(s,t)\,{\mathrm{d}s}\right|^{q}\,{\mathrm{d}t}\right] |  | (A315) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≲𝔼​[∫0T∫0Te−q​g​(s,t)​At​ds​dt]\displaystyle\lesssim\mathbb{E}\left[\int\_{0}^{T}\int\_{0}^{T}e^{-q\,g(s,t)\,A\_{t}}\,{\mathrm{d}s}\,{\mathrm{d}t}\right] |  | (A316) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =𝔼​[∫0T∫0Te−q​g​(s,t)​(μ+(A0−μ)​e−θ​t+ξ​∫0te−θ​(t−r)​dWr)​ds​dt]\displaystyle=\mathbb{E}\left[\int\_{0}^{T}\int\_{0}^{T}e^{-q\,g(s,t)\,\left(\mu+(A\_{0}-\mu)\,e^{-\theta\,t}+\xi\int\_{0}^{t}e^{-\theta\,(t-r)}\mathrm{d}W\_{r}\right)}\,{\mathrm{d}s}\,{\mathrm{d}t}\right] |  | (A317) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =∫0T∫0Te−q​g​(s,t)​(μ+(A0−μ)​e−θ​t)​𝔼​[e−q​g​(s,t)​ξ​∫0te−θ​(t−r)​dWr]​ds​dt\displaystyle=\int\_{0}^{T}\int\_{0}^{T}e^{-q\,g(s,t)\,\left(\mu+(A\_{0}-\mu)\,e^{-\theta\,t}\right)}\,\mathbb{E}\left[e^{-q\,g(s,t)\,\xi\int\_{0}^{t}e^{-\theta\,(t-r)}\mathrm{d}W\_{r}}\right]\,{\mathrm{d}s}\,{\mathrm{d}t} |  | (A318) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =∫0T∫0Te−q​g​(s,t)​(μ+(A0−μ)​e−θ​t)+12​q2​g​(s,t)2​ξ2​∫0te−2​θ​(t−r)​dr​ds​dt\displaystyle=\int\_{0}^{T}\int\_{0}^{T}e^{-q\,g(s,t)\,\left(\mu+(A\_{0}-\mu)\,e^{-\theta\,t}\right)+\tfrac{1}{2}\,q^{2}\,g(s,t)^{2}\,\xi^{2}\,\int\_{0}^{t}e^{-2\,\theta\,(t-r)}\,\mathrm{d}r}\,{\mathrm{d}s}\,{\mathrm{d}t} |  | (A319) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | <∞.\displaystyle<\infty\,. |  | (A320) |

Now take q∈(2,p)q\in(2,p) and r,s>1r,s>1 such that 2q+1r+1s=1\tfrac{2}{q}+\tfrac{1}{r}+\tfrac{1}{s}=1, then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0tP~​(t,0)2​(DtQ)2​d​⟨M~⟩t]\displaystyle\mathbb{E}\left[\int\_{0}^{t}\tilde{P}(t,0)^{2}\,(D^{Q}\_{t})^{2}\,\mathrm{d}\langle\tilde{M}\rangle\_{t}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼​[∫0tP~​(t,0)2​(DtQ)2​Ft−1​(ξ​∂1H​(At,t)−σ2​H​(At,t))2​dt]\displaystyle=\mathbb{E}\left[\int\_{0}^{t}\tilde{P}(t,0)^{2}\,(D^{Q}\_{t})^{2}\,F\_{t}^{-1}\,\left(\xi\,\partial\_{1}H(A\_{t},t)-\frac{\sigma}{2}\,H(A\_{t},t)\right)^{2}\,{\mathrm{d}t}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≲𝔼​[∫0t(DtQ)2​Ft−1​(ξ​∂1H​(At,t)−σ2​H​(At,t))2​dt]\displaystyle\lesssim\mathbb{E}\left[\int\_{0}^{t}(D^{Q}\_{t})^{2}\,F\_{t}^{-1}\,\left(\xi\,\partial\_{1}H(A\_{t},t)-\frac{\sigma}{2}\,H(A\_{t},t)\right)^{2}\,{\mathrm{d}t}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝔼​[∫0t|CtQ|q​dt]2q​𝔼​[∫0tFt−r​dt]1r​𝔼​[∫0T|ξ​∂1H​(At,t)−σ2​H​(At,t)|2​s​dt]1s\displaystyle\leq\mathbb{E}\left[\int\_{0}^{t}|C^{Q}\_{t}|^{q}\,{\mathrm{d}t}\right]^{\tfrac{2}{q}}\,\mathbb{E}\left[\int\_{0}^{t}F\_{t}^{-r}\,{\mathrm{d}t}\right]^{\tfrac{1}{r}}\mathbb{E}\left[\int\_{0}^{T}\left|\xi\,\partial\_{1}H(A\_{t},t)-\frac{\sigma}{2}\,H(A\_{t},t)\right|^{2\,s}\,{\mathrm{d}t}\right]^{\tfrac{1}{s}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≲𝔼​[∫0t|At​Ft|q​dt]2q​𝔼​[∫0tFt−r​dt]1r​𝔼​[∫0T|ξ​∂1H​(At,t)−σ2​H​(At,t)|2​s​dt]1s\displaystyle\lesssim\mathbb{E}\left[\int\_{0}^{t}|A\_{t}\,F\_{t}|^{q}\,{\mathrm{d}t}\right]^{\tfrac{2}{q}}\,\mathbb{E}\left[\int\_{0}^{t}F\_{t}^{-r}\,{\mathrm{d}t}\right]^{\tfrac{1}{r}}\mathbb{E}\left[\int\_{0}^{T}\left|\xi\,\partial\_{1}H(A\_{t},t)-\frac{\sigma}{2}\,H(A\_{t},t)\right|^{2\,s}\,{\mathrm{d}t}\right]^{\tfrac{1}{s}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≲𝔼​[∫0t|At|p​dt]2p​𝔼​[∫0tFtp​qp−q​dt]2​(p−q)p​q​𝔼​[∫0tFt−r​dt]1r​𝔼​[∫0T|ξ​∂1H​(At,t)−σ2​H​(At,t)|2​s​dt]1s\displaystyle\lesssim\mathbb{E}\left[\int\_{0}^{t}|A\_{t}|^{p}\,{\mathrm{d}t}\right]^{\tfrac{2}{p}}\,\mathbb{E}\left[\int\_{0}^{t}F\_{t}^{\tfrac{p\,q}{p-q}}\,{\mathrm{d}t}\right]^{\tfrac{2\,(p-q)}{p\,q}}\,\mathbb{E}\left[\int\_{0}^{t}F\_{t}^{-r}\,{\mathrm{d}t}\right]^{\tfrac{1}{r}}\mathbb{E}\left[\int\_{0}^{T}\left|\xi\,\partial\_{1}H(A\_{t},t)-\frac{\sigma}{2}\,H(A\_{t},t)\right|^{2\,s}\,{\mathrm{d}t}\right]^{\tfrac{1}{s}} |  |
|  |  |  |
| --- | --- | --- |
|  | <∞,\displaystyle<\infty\,, |  |

and similarly,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0tP~​(t,0)2​(CtQ)2​d​⟨M~⟩t]<∞.\displaystyle\mathbb{E}\left[\int\_{0}^{t}\tilde{P}(t,0)^{2}\,(C^{Q}\_{t})^{2}\,\mathrm{d}\langle\tilde{M}\rangle\_{t}\right]<\infty\,. |  |