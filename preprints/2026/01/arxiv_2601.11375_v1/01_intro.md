---
authors:
- B. K. Meister
doc_id: arxiv:2601.11375v1
family_id: arxiv:2601.11375
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Automated Liquidity: Market Impact, Cycles, and De-pegging Risk'
url_abs: http://arxiv.org/abs/2601.11375v1
url_html: https://arxiv.org/html/2601.11375v1
venue: arXiv q-fin
version: 1
year: 2026
---


B. K. Meister
[bernhard.k.meister@gmail.com](mailto:bernhard.k.meister@gmail.com)

###### Abstract

Three traits of decentralized finance are studied.
First, the market impact function is derived for optimal-growth liquidity providers. For a standard random walk, the classic square-root impact is recovered. An extension is then derived to fit general fractional Ornstein-Uhlenbeck processes. These findings break with the ‘linearized’ liquidity models used in most decentralized exchanges.

Second, a Constant Product Market Maker is viewed as a multi-phase Carnot engine, where one phase matches the exchange of tokens by a liquidity taker, and another the change of pool size by a liquidity provider.

Third, stablecoin de-pegging is a form of catastrophe risk.
By using growth optimization, default odds are linked to the cost of catastrophe bonds. De-pegging insurance can act as a counterweight and a key marketing tool when the law forbids the payment of interest on stablecoins.

## I Introduction

All functioning markets are alike, but every dysfunctional market is dysfunctional in its own way, to paraphrase Tolstoi.
By bypassing legacy frictions, cryptofinance has traded old inefficiencies for new faults that can only be outgrown through iteration. While some mismatches are in plain sight others are hidden. Three such properties and related design challenges are examined; but as William Blake remarked, ‘the errors of a wise man make your rule, rather than the perfections of a fool’.

Decentralized Exchanges (DEXs), often in direct competition with Centralized Exchanges (CEXs), are one of the innovations of Decentralized Finance (DeFi) with tokens worth tens of billions of dollars currently committed by Liquidity Providers (LPs) and tokens worth billions of dollars switched daily by Liquidity Takers (LTs).

The paper starts with re-deriving, extending and applying the widely-known square root market impact[bouchaud2004subtle](https://arxiv.org/html/2601.11375v1#bib4)  of relevances for CEXs and DEXs, and then rephrases in terms of a thermodynamical heat engine the Constant Product Market Maker (CPMM) - a sub-category of the Constant Function Market Maker (CFMM).
A look at the pricing of catastrophe bonds follows, showing how it bears on stablecoin insurance, before a final wrap-up.

## II A Route to Market Impact

Market impact is of interest for centralised as well as decentralised markets. It will be shown how growth optimal behaviour of liquidity providers, who allocate capital across multiple assets,
and a mean-reverting Ornstein Uhlenbeck process for mis-pricings leads to a square root market impact.

A compressed derivation is first given, which is then expanded.
The Ornstein-Uhlenbeck (OU) price process of the asset of interest is

|  |  |  |
| --- | --- | --- |
|  | d​Pt=κ​(Pt−K)​d​t+σ​d​Bt,dP\_{t}=\kappa(P\_{t}-K)dt+\sigma dB\_{t}, |  |

with Δ​P:=κ​(Pt−K)\Delta P:=\kappa(P\_{t}-K), and the optimal Kelly fraction[meister2011](https://arxiv.org/html/2601.11375v1#bib7)  is

|  |  |  |
| --- | --- | --- |
|  | f=Δ​Pσ2.f=\frac{\Delta P}{\sigma^{2}}. |  |

For LPs investing across multiple assets their large capital WW times ff scales as W​f∝QWf\propto\sqrt{Q}.
As a consequence, since the total wealth WW of an active market maker adjusts slowly in respect to any single investment,
ff becomes dynamic and has to scale with square root of QQ, which immediately leads to the square root impact relation:

|  |  |  |
| --- | --- | --- |
|  | Δ​P∝σ2W​Q.\Delta P\propto\frac{\sigma^{2}}{W}\sqrt{Q}. |  |

Next, follows an extended version of the derivation directly relating Δ​P\Delta P to QQ without introducing ff.
Market makers are assumed to maximize an objective function such as change of log utility:

|  |  |  |
| --- | --- | --- |
|  | g=E​[ln⁡(W+d​X)−ln⁡(W)]=E​[ln⁡(1+d​XW)],g=E[\ln(W+dX)-\ln(W)]=E\left[\ln\left(1+\frac{dX}{W}\right)\right], |  |

where d​XdX is the uncertain change in the value of the position in the risky asset. Taylor expansion111Cubic terms and above, i.e. O​((d​XW)3)O\Big(\big(\frac{dX}{W}\big)^{3}\Big), are excluded, but in the continuous Ornstein-Uhlenbeck setting these terms are negligible.  gives

|  |  |  |
| --- | --- | --- |
|  | g=E​[d​XW−12​(d​XW)2]=E​[d​X]W−12​V​a​r​[d​X]W2.g=E\left[\frac{dX}{W}-\frac{1}{2}\left(\frac{dX}{W}\right)^{2}\right]=\frac{E[dX]}{W}-\frac{1}{2}\frac{Var[dX]}{W^{2}}. |  |

For a market maker with position QQ, price change Δ​P\Delta P, and volatility σ\sigma, we have E​[d​X]=Q​Δ​PE[dX]=Q\Delta P and V​a​r​[d​X]=Q2​σ2Var[dX]=Q^{2}\sigma^{2}. This yields the fundamental growth equation

|  |  |  |
| --- | --- | --- |
|  | g​(Q)=Q​Δ​PW−Q2​σ22​W2.g(Q)=\frac{Q\Delta P}{W}-\frac{Q^{2}\sigma^{2}}{2W^{2}}. |  |

The next step requires closer scrutiny, since a further constraint is imposed.
For a diversified portfolio, capital WW scales with the square root of the position: W=k​QW=k\sqrt{Q}.
Unlike an investor with one risky holding, a multi-asset liquidity providers only hedges the tail of the exposure, after averaging over a large number of positions, which scales with N\sqrt{N} instead of NN. This is capital efficient.
In other words, when LPs observe flow in a particular asset, they will provide liquidity at a ‘price’. This leads to LPs being saddled with market exposure requiring hedging of risk factors using liquid assets. As an example, the first factor is often overall market exposure and the second factor might be the exposure of a stock to the oil price, or as an alternative the hedge could be determined through the Lyons’ Signature Transform, which is computationally demanding but can be again asset light.

A large LP does not bet its whole capital on just one OU process. It sets aside a ‘slice’ of balance sheet to back each trade. If a trade has a size QQ, the firm’s risk model only charges capital at the rate of Q\sqrt{Q} due to portfolio wide netting, and the Kelly growth optimzation logic then sets the price gap Δ​P\Delta P accordingly. This creates investment consistency for individual LPs across a multitude of simultaneously available investment opportunities. Since the capital cost is measured in Q\sqrt{Q}, while the trade size and returns grow with QQ, the gap between them widens with size.
The ‘optimal fraction’ ff is in effect subsidized by the firm’s size. This is one reason besides technological scaling why LPs, and also multi-strategy hedge funds, which are governed by the same diversification logic, have become behemoth.

Substituting W=k​QW=k\sqrt{Q} into the growth equation gives

|  |  |  |
| --- | --- | --- |
|  | g​(Q)=Q​Δ​Pk​Q−Q2​σ22​(k​Q)2=Δ​Pk​Q−σ2​Q2​k2.g(Q)=\frac{Q\Delta P}{k\sqrt{Q}}-\frac{Q^{2}\sigma^{2}}{2(k\sqrt{Q})^{2}}=\frac{\Delta P}{k}\sqrt{Q}-\frac{\sigma^{2}Q}{2k^{2}}. |  |

The maximal growth rate is obtained by setting the derivative of gg to zero,

|  |  |  |
| --- | --- | --- |
|  | d​gd​Q=Δ​P2​k​Q−σ22​k2=0,\frac{dg}{dQ}=\frac{\Delta P}{2k\sqrt{Q}}-\frac{\sigma^{2}}{2k^{2}}=0, |  |

which ties Δ​P\Delta P to QQ

|  |  |  |
| --- | --- | --- |
|  | Δ​P=σ2k​Q.\Delta P=\frac{\sigma^{2}}{k}\sqrt{Q}. |  |

The square root Δ​P\Delta P impact is directly linked to the Kelly-optimal QQ under the choice of portfolio diversification constraint222In this footnote it is shown that the same result can also be derived using the conventional terminology, where the leverage ratio ff is optimised instead of linking QQ directly with Δ​P\Delta P.
To stay unit-consistent, we use the identity P​Q=f​WP\,Q=f\,W. We substitute the square root capital constraint, W=k​QW=k\sqrt{Q}, to find the relationship between wealth WW and leverage ff



W=k​f​WP⟹W=k2​fP.W=k\sqrt{\frac{fW}{P}}\implies W=\frac{k^{2}f}{P}.
Substituting WW back into the sizing identity:

Q=fP​(k2​fP)=k2​f2P2,Q=\frac{f}{P}\left(\frac{k^{2}f}{P}\right)=\frac{k^{2}f^{2}}{P^{2}},
ergo leverage ff scales quadratically with position size QQ.
The instantaneous growth rate g​(f)g(f) is defined as the expected change in wealth minus the variance

g=E​[d​W]W−12​V​a​r​[d​W]W2.g=\frac{E[dW]}{W}-\frac{1}{2}\frac{Var[dW]}{W^{2}}.
 In an OU process with edge Δ​P\Delta P and volatility σ\sigma, the wealth change is driven by

d​W=Q​(Δ​P​d​t+σ​d​B).dW=Q(\Delta Pdt+\sigma dB).
Substituting Q=f​WPQ=\frac{fW}{P}



g​(f)=f​W​Δ​PP​W−12​(f​W)2​σ2P2​W2,g(f)=\frac{f\,W\,\Delta P}{P\,W}-\frac{1}{2}\frac{(fW)^{2}\sigma^{2}}{P^{2}\,W^{2}},



g​(f)=Δ​PP​f−σ22​P2​f2,g(f)=\frac{\Delta P}{P}f-\frac{\sigma^{2}}{2P^{2}}f^{2},
 and setting the derivative with respect to ff to zero leads to

g′​(f)=0=Δ​PP−σ2P2​f⟹Δ​P​P=σ2​f,g^{\prime}(f)=0=\frac{\Delta P}{P}-\frac{\sigma^{2}}{P^{2}}f\,\,\Longrightarrow\,\,\Delta P\,P=\sigma^{2}f,
together with

Q​P=f​k,\sqrt{Q}\,P=fk,
 results in

Δ​P=σ2k​Q.\Delta P=\frac{\sigma^{2}}{k}\sqrt{Q}.
Other choices for ff, e.g.
f=c​o​n​s​tf=const, are inconsistent. In an OU process, Δ​P\Delta P decays as the price moves toward the mean. If ff is constant, the growth rate g=f​Δ​P−12​f2​σ2g=f\Delta P-\frac{1}{2}f^{2}\sigma^{2} would eventually become negative as Δ​P\Delta P becomes small. By using f∝Δ​Pf\propto\Delta P the growth rate gg stays positive: g=12​(Δ​P/σ)2≥0g=\frac{1}{2}(\Delta P/\sigma)^{2}\geq 0. Trading stops exactly when the edge disappears, i.e. Δ​P=0⟹f=0\Delta P=0\implies f=0.
  
What should be compared across assets is therefore not the growth rate, but the risk-adjusted edge, i.e. f=Δ​P/σ2f=\Delta P/\sigma^{2}. The reason one allocates the same amount ff to two assets with different growth rates gg is that capital allocation is a function of what could be termed ‘leverage efficiency’. This can lead to paradoxes. For example, the increase of the investable universe can lead under special conditions to a drop in growth or even bankruptcy, see the Proebsting’s paradox or the Braess paradox in the not completely unrelated field of traffic theory.
.

This stands in contrast to the single-asset portfolio, where time-dependence is explicitly captured by the subindex tt. The investment strategy is governed by ft​Wt=Pt​Qtf\_{t}W\_{t}=P\_{t}Q\_{t}, and the self-financing condition is

|  |  |  |
| --- | --- | --- |
|  | d​Wt=Qt​d​Pt.dW\_{t}=Q\_{t}dP\_{t}. |  |

The optimal fraction for the previously introduced OU process is

|  |  |  |
| --- | --- | --- |
|  | ft=κ​(Pt−K)σ2.f\_{t}=\frac{\kappa(P\_{t}-K)}{\sigma^{2}}. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | Qt=Wt​κ​(Pt−K)Pt​σ2.Q\_{t}=W\_{t}\frac{\kappa(P\_{t}-K)}{P\_{t}\,\sigma^{2}}. |  |

For convenience KK is set to zero, and this leads to

|  |  |  |
| --- | --- | --- |
|  | d​log⁡Wt=κσ2​d​Pt,d\log W\_{t}=\frac{\kappa}{\sigma^{2}}dP\_{t}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | Wt=W0​eκσ2​(Pt−P0),W\_{t}=W\_{0}e^{\frac{\kappa}{\sigma^{2}}(P\_{t}-P\_{0})}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Qt=W0​κσ2​eκσ2​(Pt−P0).Q\_{t}=W\_{0}\frac{\kappa}{\sigma^{2}}e^{\frac{\kappa}{\sigma^{2}}(P\_{t}-P\_{0})}. |  |

The discussion is in the next section broadened to fractional Ornstein-Uhlenbeck (fOU) processes.

## III Derivation of the Impact Law for Informative Order Flow

The extension of the impact rule to general fOU processes,

|  |  |  |
| --- | --- | --- |
|  | d​Pt=κ​(Pt−K)​d​t+σ​d​BtH,dP\_{t}=\kappa(P\_{t}-K)dt+\sigma dB^{H}\_{t}, |  |

with any Hurst exponent, H∈(0,1)H\in(0,1), is carried out next.
For details about fOU see [biagini2008stochastic](https://arxiv.org/html/2601.11375v1#bib3) . The variance of the portfolio for a position size QQ invested in asset PtP\_{t} over time TT scales as Q2​σ2​T2​HQ^{2}\sigma^{2}T^{2H}. Under the portfolio capital constraint W=k​QW=k\sqrt{Q}, the Kelly growth rate becomes,

|  |  |  |
| --- | --- | --- |
|  | g​(Q)=Q​T​Δ​Pk​Q−σ2​Q2​T2​H2​k2​Q.g(Q)=\frac{QT\Delta P}{k\sqrt{Q}}-\frac{\sigma^{2}Q^{2}T^{2H}}{2k^{2}Q}. |  |

Assuming the number of traded units QQ scales linearly with TT, i.e. T∝QT\propto Q or T=k^​QT=\hat{k}Q, the growth equation simplifies to

|  |  |  |
| --- | --- | --- |
|  | g​(Q)=Δ​Pk​k^​Q​Q−σ22​k2​k^2​H​Q2​H+1.g(Q)=\frac{\Delta P}{k}\hat{k}Q\sqrt{Q}-\frac{\sigma^{2}}{2k^{2}}\hat{k}^{2H}Q^{2H+1}. |  |

Taking the derivative with respect to QQ and setting it to zero of g​(Q)/Tg(Q)/T, since one is interested in the optimal growth per unit of time, one gets

|  |  |  |
| --- | --- | --- |
|  | Δ​P​Q2​k−2​H​σ2​k^2​H−12​k2​Q2​H=0,\frac{\Delta P\sqrt{Q}}{2k}-\frac{2H\,\,\sigma^{2}\,\,\hat{k}^{2H-1}}{2k^{2}}Q^{2H}=0, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Δ​P=2​H​k^2​H−1​σ2k​Q2​H−12.\Delta P=\frac{2H\,\hat{k}^{2H-1}\,\,\sigma^{2}}{k}Q^{2H-\frac{1}{2}}\,\,. |  |

An LP’s adjustment of the market impact function in the face of skewed order flow is not malicious; it is instead a natural defence against toxic flow and distinct from informational rent-seeking like front-running. In this context, ‘making a mistake is human, but repeating it is a choice’. Being ‘picked off’ is a signal, and to neglect this information and leave the impact function unchanged would be an error.

The above formulation of market impact stands in contrast to the ‘linearised’ liquidity models prevalent in decentralised exchanges.

## IV Informational Attrition: CPMM eroded by Toxic Flow

In a standard CPMM, the invariant is X​Y=KX\,Y=K. The token exchange rate PP is the ratio of the reserves P:=Y/XP:=Y/X. The associated market impact is derived next. Assume a LT buys a small amount Δ​X\Delta X, the reserves change to X+Δ​XX+\Delta X and Y−Δ​YY-\Delta Y. The new price Pn​e​wP\_{new} is

|  |  |  |
| --- | --- | --- |
|  | Pn​e​w=Y−Δ​YX+Δ​X=K(X+Δ​X)2.P\_{new}=\frac{Y-\Delta Y}{X+\Delta X}=\frac{K}{(X+\Delta X)^{2}}. |  |

A Taylor expansion around Δ​X=0\Delta X=0,

|  |  |  |
| --- | --- | --- |
|  | P​(X+Δ​X)≈P​(X)+P′​(X)​Δ​X,P(X+\Delta X)\approx P(X)+P^{\prime}(X)\,\Delta X, |  |

combined with P​(X)=K​X−2P(X)=KX^{-2} and P′​(X)=−2​k​X−3=−2​PXP^{\prime}(X)=-2kX^{-3}=-2\frac{P}{X}
leads to

|  |  |  |
| --- | --- | --- |
|  | 2​Δ​PP≈−Δ​XX.2\frac{\Delta P}{P}\approx-\frac{\Delta X}{X}\,. |  |

This is in conflict with the
square-root and more generally Hurst dependent market impact found above.

In an environment where block updates are orders of magnitude slower than high-frequency execution, DEXs for many liquid assets lag CEXs, causing the local Hurst exponent to approach H≈1H\approx 1. This is especially acute, if the price on the CEX due to information inflow jumps. One is confronted with an ‘entropy leak’ where the LP is under-compensated for the variance drag of ‘toxic flow’. While linearization attracts volume, it creates a path-independent step-wise ‘crawl’ that can subsidize arbitrageurs. The path-independence of CPMMs is in this case a liability.
The problem is amplified in protocols that concentrate liquidity and heap on leverage.

As a simple consequence of the above result, the Kelly-optimal market impact must be steeper than linear at the origin for H<3/4H<3/4, i.e. sub-linear equates to 2​H−1/2<12H-1/2<1.
Misjudging the Hurst exponent and implementing the wrong impact function does not necessarily lead to loss of capital, but can instead be associated with opportunity cost, especially for HH trending towards zero. Sensitivity analysis determines the amount of leakage due to misspecification.

One way to ameliorate the cost to DEX LPs is to penalize small orders and shift execution prices closer to the post-execution pool ratio. The advantage and disadvantages of this and other proposals will be discussed elsewhere.
For a fuller analysis one also has to consider ‘impermanence loss’ and ‘loss-versus-rebalancing’ (LVR)[milionis2022automated](https://arxiv.org/html/2601.11375v1#bib13)  for different proposals under a range of HH.

Next follows sections on the Carnot engine.

## V A DEX trading strategy mapped into Thermodynamics

In this section the workings of a heat engine and a DEX trading strategy are positioned side by side after some introductory definitions.

![Refer to caption](diagram2.png)


Figure 1:  Crypto Carnot Cycle: Four stage cyclic DEX trading strategy with two switching and two pool liquidity modification stages.

Thermodynamics - Callen[callen](https://arxiv.org/html/2601.11375v1#bib5)  provides background - holds an exalted position in science.
As Arthur Eddington famously remarked, ‘the law that entropy always increases holds, I think, the supreme position among the laws of Nature. If someone points out to you that your pet theory of the universe is in disagreement with Maxwell’s equations - then so much the worse for Maxwell’s equations. If it is found to be contradicted by observation - well, these experimentalists do bungle things sometimes. But if your theory is found to be against the Second Law of Thermodynamics I can give you no hope; there is nothing for it to collapse in deepest humiliation.’

The ideal gas law, P​V=n​k​TPV=nkT, finds a direct translation into the mechanics of CPMMs. By mapping the reserve amounts XX and YY to pressure PP and volume VV respectively, KK emerges as the analogue to the system’s thermal energy n​k​TnkT, where nn is the number of moles, kk is the ideal gas constant, and TT is the temperature. Within this framework, a token swap represents an ‘isoenergetic process’, where the state variables XX and YY adjust while the product KK remains invariant. Conversely, the provision or withdrawal of liquidity at the prevailing price ratio constitutes what could be termed an ‘isothermal process’333Energy is an extensive quantity, while temperature is an intensive quantity, and the analogy between thermodynamics and DeFi has to be taken with a grain of salt. . The X/YX/Y ratio is then the system’s temperature.
The cyclic process[bbm2000](https://arxiv.org/html/2601.11375v1#bib1) ; [bbm2002](https://arxiv.org/html/2601.11375v1#bib2)  with four stages, see figure one, is next described in more detail.
The initial and final amounts in the pool are for the first token XX and for the second token YY with X​Y=KXY=K. At each stage an investor takes an action.
In stage one and three an investor acts as a liquidity taker and switches tokens, whereas in stage two and four an investor expands and contracts the size of the pool.

Side by side in the table below are the four stages of the cyclic processes:
  
Thermodynamics  
  
 
  
 
            DeFi

Step one

Isothermal Expansion
  
 
  
 
  
 
  
Switching α\alpha of the first token to β\beta of the second token while leaving KK unchanged leading to X−αX-\alpha and Y+βY+\beta with (X−α)​(Y+β)(X-\alpha)(Y+\beta)

Step two

Isentropic Expansion
  
 
  
  
  
Adding MM of the first and NN of the second token in the right ratio, i.e. while (X−α)/(Y+β)=M/N(X-\alpha)/(Y+\beta)=M/N

Step three

Isothermal Compression
  
 
  
 
  
 
  
Switching δ\delta of the second token to σ\sigma of the first token with
(X−α+M)​(Y+β+N)=(X−α+M+σ)​(Y+β+N−δ)(X-\alpha+M)(Y+\beta+N)=(X-\alpha+M+\sigma)(Y+\beta+N-\delta)

Step four

Isentropic Compression
  
 
  
  
  
Subtracting GG of the first and HH of the second token in the right ratio, i.e.
while (X−α+M+σ)/(Y+β+N−δ)=G/H(X-\alpha+M+\sigma)/(Y+\beta+N-\delta)=G/H

In thermodynamics the area enclosed corresponds to the work, and in DeFi the net gain or loss should have a similar interpretation.

We assume the operator of the engine, as well as the trader accessing the DEX, can carry out the four stages without interference, i.e. there is complete control by the trader over the incorporations of transactions into the blockchain.
The following caveats further apply.
A ‘perfect’ engine is considered with no extraneous losses, and in the trading context, a
‘perfect’ market with neither transaction or nor gas cost.
The next paragraphs provide an example calculation and implicitly answer the question.
What takes the role ofheat baths in CPMM? In thermodynamics the Carnot efficiency bound for a heat engine with access to two heat baths is given by 1−T1/T21-T\_{1}/T\_{2} with T2≥T1T\_{2}\geq T\_{1}.

The calculation accompanying the four stages of the crypto Carnot cycle are given next. the starting and final composition of the pool will be identical. There are three parts to the description of the token composition at each stage. These are the total token amounts in the pool, the token amounts owned by the investor in the pool, and the token amounts owned by the investor outside the pool. Temporary short position are allowed. This could involve a marginal amount of borrowing cost, which is ignored.

Starting point:
  
Pool: (X,Y) with XY=K, i.e. the pool composition is a two component vector of amount XX of the first and amount YY of the second token.
  
Investor:
  
Investor position inside pool : (0,0)(0,0)
  
Investor position outside pool: (0,0)(0,0)

Result of stage 1: Switch of α\alpha of the first token for β\beta of the second token.
  
Pool: (X−α,Y​X/(X−α))(X-\alpha,YX/(X-\alpha))
  
Investor:
  
Investor position inside pool : (0,0)(0,0)
  
Investor position outside pool: (α,−β)(\alpha,-\beta)
  
with β=X​Y/(X−α)−Y\beta=XY/(X-\alpha)-Y

Result of stage 2: Addition of MM of the first token and NN of the second token.
  
Pool: (X−α+M,X​Y/(X−α)+N)(X-\alpha+M,XY/(X-\alpha)+N)
  
Investor:
  
Investor position inside pool : (M,N)(M,N)
  
Investor position outside pool: (α−M,−β−N)(\alpha-M,-\beta-N)
with N=M​Y​X/(X−α)2N=M\,Y\,X/(X-\alpha)^{2}

Result of stage 3: Switch of δ\delta of the second token for σ\sigma of the first token.
  
Pool:(X−α+σ+M,Y​X​(1+M/(X−α))/(X−α)−δ)(X-\alpha+\sigma+M,YX(1+M/(X-\alpha))/(X-\alpha)-\delta)
  
Investor:
  
Investor position inside pool : (M,N)(M,N)
  
Investor position outside pool: (α−M−σ,−β−N+δ)(\alpha-M-\sigma,-\beta-N+\delta)
  
with δ=σ​Y​XX−α​(1+MX−α)​1X+M\delta=\sigma\frac{YX}{X-\alpha}\Big(1+\frac{M}{X-\alpha}\Big)\frac{1}{X+M}

Result of stage 4: Removal of GG of the first token and HH of the second token.
  
Pool: (X−α+σ+M−G,Y​XX−α​(1+MX−α)−δ−H)(X-\alpha+\sigma+M-G,\frac{YX}{X-\alpha}(1+\frac{M}{X-\alpha})-\delta-H).
  
Investor:
  
Investor position inside pool : (M−G,N−H)(M-G,N-H)
  
Investor position outside pool: (α−M−σ+G,−β−N+δ+H).(\alpha-M-\sigma+G,-\beta-N+\delta+H).
  
The four stage cycle does not generally close, and even if by setting M−G−α+σ=0M-G-\alpha+\sigma=0 and Y​XX−α​(1+MX−α)−δ−H=Y\frac{YX}{X-\alpha}\Big(1+\frac{M}{X-\alpha}\Big)-\delta-H=Y the
final pool composition is again (X,Y)(X,Y), the final investor position inside and outside the pool will not have collapsed back to zero.

The strategy described above is not capital free444A requirement exists to borrow tokens temporarily to add to the pool in stage two. This needs capital. The same holds true for stage one and three to enable the investor to switch tokens. This leads to borrowing cost and collateral requirements and adds a twist to the analysis ignored in the idealised setting. Flashloans can potentially reduce the capital employed.. Friction associated with pool dependent transaction fees, variable gas fees and the need to access the blockchain without for example MEV interference was ignored, complicates the situation and weakens any obtainable profit. Viewed geometrically, transaction costs distort the crypto-equivalent ‘isothermal curves’. A formal investigation reducing these frictional effects to a system of inequalities will be carried out elsewhere.
Stablecoin de-pegging risk is the topic of the next part.

## VI Kelly and the Cat-bonds: Optimality in Catastrophe Bond Portfolios

How stablecoin de-pegging, both temporary as well as irreversibly, can be covered by catastrophe insurance either in form of conventional cat-bonds or on-chain is investigated. The passing of ‘The Guiding and Establishing National Innovation for U.S. Stablecoins Act’ (GENIUS Act) has spawned a multibillion-dollar yield windfall by forbidding issuers to pay interest to stablecoin holders. Foregone interest collected by issuers could be partially pumped into insurance premiums, subsidizing the cost of a private-market backstop. This has been an active topic of discussion, but the market remains nascent, held back by legal thickets and wrangling.

In a recent paper[eichengreen2025](https://arxiv.org/html/2601.11375v1#bib6)  estimates were given for de-pegging risk.
It will be shown how to relate the price of different catastrophe risks, e.g. de-pegging priced on the back of catastrophe bond benchmarks.

Stablecoins - whether backed by a vault or algorithmic - have suffered crashes. They are still a work in progress, even as hundreds of billions of dollars courses through the system. While they aim to be as steady as cash, their history is dotted with sudden melt-downs, rendering them into a risk to be managed.

The Kelly criterion can provide this relative pricing of catastrophe bonds.
Two different basic edge cases are considered. First, either a bond AA or bond BB is contained in the portfolio. In the second method, both bond A&BA\&B are held in the same portfolio and the relative weights are determined.

Discrete and continuous price processes lead to different Kelly optimizations.
In the one dimensional continuous case the optimal fraction is under relatively general conditions given by the ratio of the excess return minus the short rate and variance. In the multidimensional case the excess return is a vector multiplied by the inverse (or more generally the Moore-Penrose inverse[meister2011](https://arxiv.org/html/2601.11375v1#bib7) ) of the covariance matrix. For independent assets it would be a diagonal matrix. This restriction to the first and second moment does not hold when one considers optimization for discrete payouts, where higher order moments cannot be neglected. The discrete view is more natural for catastrophe payouts and will be used here, nevertheless even in the discrete case the ratio of the mean and variance gives a first estimate for the optimal fraction. It provides the simplest way to relate different catastrophe risks.

If the portfolio has only access to one risky asset with qq the default probability, p=1−qp=1-q the corresponding survival probability, ff the fraction invested in the risky assets, and rr the return in the non-default case. Recovery in the case of a default is set to zero. The growth expression to maximize is

|  |  |  |
| --- | --- | --- |
|  | q​log⁡(1−f)+p​log⁡(1+f​r)\displaystyle q\log(1-f)+p\log(1+fr) |  |

to get

|  |  |  |
| --- | --- | --- |
|  | f=1−q−qr,\displaystyle f=1-q-\frac{q}{r}, |  |

which corresponds to the conventional statement of the formula in the double-or-nothing betting game for rr equal to one.
How can the optimal ff remain unchanged, if qq is replaced by q+Δq+\Delta and rr by r+δr+\delta? This requires the following relationship between the additive adjustments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ϵ\displaystyle\epsilon | ≈\displaystyle\approx | δr​(q1+r),\displaystyle\frac{\delta}{r}\left(\frac{q}{1+r}\right), |  |
|  |  | ≈\displaystyle\approx | δr​(q1+r+q2(1+r)2+q3(1+r)3+…).\displaystyle\frac{\delta}{r}\left(\frac{q}{1+r}+\frac{q^{2}}{(1+r)^{2}}+\frac{q^{3}}{(1+r)^{3}}+\dots\right). |  |

As a next and final step, we consider the two bond portfolio with fA=fB:=f∗f\_{A}=f\_{B}:=f^{\*} and include the lowest cross term, but instead assume qA=qB:=qq\_{A}=q\_{B}:=q and therefore rA=rB:=rr\_{A}=r\_{B}:=r to get

|  |  |  |
| --- | --- | --- |
|  | f∗≈12−qr−q22​r2−q3​r​(qr)2,f^{\*}\approx\frac{1}{2}-\frac{q}{r}-\frac{q^{2}}{2r^{2}}-\frac{q}{3r}\left(\frac{q}{r}\right)^{2}, |  |

where the last term is a cross term capturing that both bonds can default simultaneously.
To reiterate, investment fraction equality does not translate into growth equality, especially when rare events are involved, and as already mentioned at the end of footnote 2 this can lead to paradoxes.

The two toy examples explored how in idealized settings catastrophe risks can be related.
Similar and more interesting scenarios have been considered by Ziemba and others.

## VII Conclusion

Derivations based on information theory, called colloquially ‘Kelly optimisation’ in some finance applications[bkm2016](https://arxiv.org/html/2601.11375v1#bib8) ; [meister2022](https://arxiv.org/html/2601.11375v1#bib9) ; [meister2023](https://arxiv.org/html/2601.11375v1#bib10) ; [meister2024](https://arxiv.org/html/2601.11375v1#bib11) ; [meister2025](https://arxiv.org/html/2601.11375v1#bib12) , can provide insights into market-place design conundrums.

After deriving market impact for a range of Hurst exponents, it was shown how this differs from the artificial market impact implemented on CPMMs.
As HH moves towards extremes the capital misallocations of LPs on CPMMs are exacerbated, and the LPs liquidity provisions becomes decoupled from the true growth-optimal pricing curve, leading to both sub-optimal fee accumulation and increased exposure to uncompensated jump-risk.

Market impact arises from the bottom-up competition inside individual LPs for capital allocation. However there is also top-down competition between LPs enforcing price consistency across the market - the ‘law of one price’ - even as the Q−QQ-\sqrt{Q} effect grants advantages that widen with scale. This is balanced by drawbacks, since a ‘monopoly’ LP becomes the market itself and, as ‘a whale in a tub’, is unable to stir due to liquidity constraints. The critical threshold is easier to observe in a crisis, as one saw with Archegos Capital Management or earlier with LTCM, then to predict beforehand, for as Keats noted, ‘axioms in philosophy are not axioms until they are proved upon our pulses’.

Tail risk associated with various de-pegging events hampers the influx of institutional and retail money to decentralized finance.
Enumerating these risks and providing hedging tools through catastrophe bonds or similar instruments enables broader institutional and retail adoption. It would expand the range of uncorrelated investments available to tail risk funds on the demand side and stable coin issuers could use it on the supply side to distinguish their coins from competitors. The availability of protection can enhance the attractiveness of a stable coin and can be viewed as a cost efficient marketing, especially when due to the GENIUS Act payment of interest on stable coin deposits is forbidden.

De-pegging risk is a tuneable risk similar to an option strike, since it ranges all the way from a temporary deviation of a chosen percentage from the peg to an irreversible failure. This gives design flexibility to obtain yields ranging from single to low double digits.

Paul Volcker quipped after the 2008 financial crisis that ‘ATMs were the only useful innovation in banking for the past 20 years’. One might say the same for stablecoins. They are the plainest part of DeFi, but they fill a market need. In doing so, they take on the main role of fiat money as a means of exchange. Other assets can handle the other two functions: being a store of wealth and a unit of account.

Tweedledee spells out the looking-glass logic555W. H. Auden’s 1962 essay, “Today’s ‘Wonder-World’ Needs Alice”, draws a parallel between a rational Alice caught in a maze of upside-down logic and a modern world of vanishing certainties.
 of DeFi: ’Contrariwise, if it was so, it might be; and if it were so, it would be; but as it isn’t, it ain’t. That’s logic.’

1. (1)
    C M Bender, D C Brody & B K Meister (2000). Quantum-mechanical Carnot engine. Journal of Physics A33, 4427-4436.- (2)
     C M Bender, D C Brody & B K Meister (2002). Entropy and temperature of a quantum Carnot engine. Proceedings of the Royal Society of London A458, 1519-1526.- (3)

       F Biagini, Y Hu, B Øksendal & T Zhang (2008).
       Stochastic Calculus for Fractional Brownian Motion and Applications.
       Springer.- (4)

         J P Bouchaud, Y Gefen, M Potters & M Wyart (2004).
         Fluctuations and response in financial markets: the subtle nature of ‘random’ price changes.
         Quantitative Finance, 4(2), 176-190.- (5)
            H B Callen (1985). Thermodynamics and an Introduction to Thermostatistics (2nd ed.). John Wiley & Sons.- (6)
              B Eichengreen, M T Nguyen, & G Viswanath-Natraj (2025). Stablecoin devaluation risk. The European Journal of Finance, pp.1-28.- (7)

               Y  Lv & B K Meister (2010)
               Applications of the Kelly Criterion to multi-dimensional Diffusion Processes. International Journal of Theoretical and Applied Finance 13, 93-112.
               27, reprinted in
               The Kelly Criterion: Theory & Practice:, ed. by MacClean, Thorp & Ziemba, World Scientific. 285-300. (2011).- (8)

                 B K Meister (2016). Meta-CTA Trading Strategies based on the Kelly Criterion,
                 arXiv:1610.10029.- (9)

                   B K Meister (2022).
                    Meta-CTA Trading Strategies and Rational Market Failures, arXiv:2209.05360.- (10)

                     B K Meister (2023).
                     Gambling the World Away: Myopic Investors, arXiv:2302.13994.- (11)

                       B K Meister (2024).
                       Application of the Kelly Criterion to Prediction Markets, arXiv:2412.14144.- (12)

                         B K Meister (2025).
                         Through the Looking Glass: Bitcoin Treasury Companies, arXiv:2507.14910.- (13)

                           J Milionis, C C Moallemi, T Roughgarden & A L Zhang (2022).
                           Automated Market Making and Loss-Versus-Rebalancing, arXiv:2208.06046.