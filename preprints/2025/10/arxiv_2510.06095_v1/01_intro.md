---
authors:
- Althea Sterrett
- Austin Adams
doc_id: arxiv:2510.06095v1
family_id: arxiv:2510.06095
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob
  Horne and Bridgett Frey for helpful comments.
url_abs: http://arxiv.org/abs/2510.06095v1
url_html: https://arxiv.org/html/2510.06095v1
venue: arXiv q-fin
version: 1
year: 2025
---


Althea Sterrett
  
Whetstone Research
  
email: [althea@whetstone.cc](mailto:althea@whetstone.cc)
  
Austin Adams
  
Whetstone Research
  
email: [austin@whetstone.cc](mailto:austin@whetstone.cc)

(Initial version: October 7, 2025
  
This version: October 7, 2025)

###### Abstract

The programmable and composable nature of smart contract protocols has enabled the emergence of novel market structures and asset classes that are architecturally frictional to implement in traditional financial paradigms. This fluidity has produced an understudied class of market dynamics, particularly in coupled markets where one market serves as an oracle for the other. In such market structures, purchases or liquidations through the intermediate asset create coupled price action between the intermediate and final assets; leading to basket inflation or deflation when denominated in the riskless asset. This paper examines the microstructure of this inflationary dynamic given two constant function market makers (CFMMs) as the intermediate market structures; attempting to quantify their contributions to the former relative to familiar pool metrics such as price drift, trade size, and market depth. Further, a concrete case study is developed, where both markets are constant product markets. The intention is to shed light on the market design process within such coupled environments.

## 1 Introduction

Programmatic markets have created a new language for market creation. This is done by enabling creators and market designers to rapidly experiment with new and novel asset classes. One impact from this growth of programmable markets is the commodification of issuance. Asset issuance used to be an arduous challenge on all fronts, historically with fixed costs of inclusion into popular market destinations.

Additionally, programmatic markets have unlocked net-new designs that are not feasible with manual systems. For example, long-tail markets and what we refer to as "coupled markets". Coupled markets are a new primitive where the output to one market is used as the input to another - effectively coupling the prices of the assets together. This effect is easier to examine in markets where the pairing is an “oracle market”, where the price feed for the asset is solely determined by the AMM. Most markets trade in the most liquid venue - allowing an asset coupling effect by denoting the sale of an asset in another and placing them in an automated market maker.

In an automated market maker, the exchange rate can only be changed by trading against the pool. Because for (large enough) price deviations, there exists an arbitrage against the true value of this asset (generally assumed to be a centralized exchange) [[6](https://arxiv.org/html/2510.06095v1#bib.bib6)]. This arbitrage enables a class of users who keep AMM prices inline with the "true value" of the asset by constantly arbitraging the market [[5](https://arxiv.org/html/2510.06095v1#bib.bib5)].

In a central limit order book, the traders must both price the asset and provide liquidity for the market (via limit orders). By unbundling these two functions, new markets can be created by allowing sophisticated counterparties to only compete on their ability to price an asset - potentially at both low and high-frequencies. One simplifying assumption of AMM models is that there exists an external liquid venue which functions as the “true” market price [[7](https://arxiv.org/html/2510.06095v1#bib.bib7)]. This assumption is likely true for the most well-known assets, but due to the growth of programmatic issuance it is being challenged for newer assets.

A key question emerges when the AMM is the liquid venue. This could emerge from the pool could be the only tradeable market for this asset or liquid enough to force asset coupling through carrying costs. We label this market as an "oracle market", as the “true” price of the asset is derived from this market, effectively making it an oracle. The oracle markets have unique properties, some of which we will explore today within asset coupling markets.

First, the delineation between noise and informed traders becomes meaningless. All traders functionally become informed, because there exists no market to arbitrage the price against. It is possible for some informed party to reset the market back (making the previous trade uninformed), but this is not without risk, as there exists no liquid venue to fully offset the costs. Constant fee AMMs treat every participant as informed (by charging every participant the same fee), making them well suited for this type of trading.

Secondly, because of the lack of "noise trading", this market is almost exclusively being adversely selected. In traditional markets, this would leading to liquidity drying up, as traditional market makers require some amount of non-toxic flow to continue pricing assets. However, the asset issuer greatly benefits from the pricing information provided by the pool, and is thus greatly incentivized to provide long-term liquidity in the market. The value of pricing information is generally disregarded in most LPing models, because only the issuer is incentivized to pay this cost (and functionally does using market making deals).

We argue that oracle markets are much more likely to occur when combined with issuance protocols, such as [Doppler](https://doppler.lol/whitepaper.pdf), because liquidity is placed into the pool to abstract most of the complexities with market making. This makes the “canonical pool” (the pool where the issuance protocol houses most liquidity) an oracle market almost by design. It is possible as the token project grows that other venues may emerge (and we have seen this occur). This generally occurs because of high fees in the canonical pool, but issuance protocols have responded with dynamic fees to lower the spread.

Oracle markets may have more emergent properties as their place in the ecosystem evolves.

In this paper, we explore asset coupling within oracle markets. By making the output currency of one oracle market as the input to another, strange properties arise, because the informed price update in the first oracle market effectively adds value to the second oracle market via utilizing that currency as their pair.

This asset coupling strategy has been a popular way to drive value to arbitrary assets by utilizing [issuer monopoly](https://aada.ms/pdfs/dlb.pdf). By specifying the specific asset that value is traded in, the auction effectively becomes priced in the desired asset and has a coupling effect. Historically, asset issuers want to denote this in some widely used currency like the dollar or native tokens like ETH, as the ease of use in bidding in auctions far outweighs the benefit of an alternative currency.

However, this problem is fixed due to guaranteed market linking via AMMs. With these links, arbitrary liquidity can flow into the pool because of a guaranteed market link between the issuance protocol and the market. By denoting the asset in the market, you create a programmable economic link between the two assets. The nature of the liquidity placement determines this link and can be adjusted to target specific outcomes.

## 2 Analysis

Suppose we have three different assets xx, yy and zz, and two constant function market makers, or CFMMs, φ1,φ2\varphi\_{1},\varphi\_{2} with trading pairs yy/xx and zz/yy respectively. If both CFMMs are the only yy and zz-markets available, a positive coupling condition arises between the price of yy and the price of zz during purchase or liquidation events between assets xx and zz. Any such trade will require routing through both intermediary markets, inherently dragging the price of yy along in the direction of the trade. This creates compound slippage and price action that inflates or deflates the received basket’s value relative to the xx base.

To quantify coupling effects, we establish a baseline where the yy/xx market has sufficient depth that zz market activity negligibly impacts yy’s price. This approximates the scenario where yy serves as a stable numeraire for zz pricing - analogous to how ETH functions for small-cap token markets, where realistic trade volumes don’t meaningfully move the ETH/USDC price. The intention of this baseline is to isolate the marginal effect of finite yy/xx liquidity and the slippage it creates. For large-cap assets where this assumption breaks, the coupling effects we derive represent an upper bound on the inflationary dynamics.

The key point worth noting here is that if the consumption of yy and zz liquidity is correlated to changes in their respective market prices, then the potential for these inflationary or deflationary effects remains when coupled. This correlated consumption of liquidity could occur when underlying asset prices themselves are correlated, likely due to asset-specific effects. Hence, using the decoupled scenario as the analytic baseline allows for the direct isolation of the effect of coupled price action on the trader’s portfolio.

Quantifying the effects of coupling on the output basket, and how the underlying market structures contribute to this behavior, requires defining the following trader metrics:

* i.

  The basket value discrepancy between coupled and decoupled scenarios on purchase and liquidation, both in the intermediate and output baskets.
* ii.

  The price drift transmission (how the price drift incurred in the initial swap market affects the drift incurred in latter markets), allowing us to see the exact coupling in price drifts in the yy and zz markets.
* iii.

  The marginal cost of additional swap liquidity as a function of the trade sizes, again on both purchase and liquidation.
* iv.

  The curvature of the compound zz/xx-market and what this implies about the compound market depth

These four metrics allow direct determination of the net inflation on the output value due to the coupling, how sensitive that inflation is to additional swap liquidity or price drift, and the dependencies these outcomes have on the depths of each swap market.

## 3 Market Metrics

Consider a pool described by pair (𝐑,φ​(x,y))(\mathbf{R},\varphi(x,y)) where 𝐑=(x,y)\mathbf{R}=(x,y), xx is the base reserve, yy the quote, and φ​(𝐑)=k\varphi(\mathbf{R})=k is the invariant functions of the pool. The spot price, denominated in the market’s base asset, follows the instantaneous marginal exchange rate of the pool reserves.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Px​(𝐑)=∂φ∂x∂φ∂y​(𝐑)=−d​yd​x​(𝐑),\displaystyle P\_{x}(\mathbf{R})=\frac{\frac{\partial\varphi}{\partial x}}{\frac{\partial\varphi}{\partial y}}(\mathbf{R})=-\frac{dy}{dx}(\mathbf{R}), | Py​(𝐑)=−d​xd​y​(𝐑).\displaystyle P\_{y}(\mathbf{R})=-\frac{dx}{dy}(\mathbf{R}). |  |

Note that this only gives the reported price, not the actual cost of a swap. Consider the case where 𝐑=(x,y)\mathbf{R}=(x,y), with swap input amount Δ\Delta of xx and discount factor γ\gamma. The swap is computed by enforcing our invariant holds under a discounted token exchange [[2](https://arxiv.org/html/2510.06095v1#bib.bib2)]. So the following equation must hold:

|  |  |  |
| --- | --- | --- |
|  | φ​(x+γ​Δ,y−Λ)=k.\varphi(x+\gamma\Delta,y-\Lambda)=k. |  |

The actual price received on such a trade is simply Pe​f​f=ΔΛP\_{eff}=\frac{\Delta}{\Lambda}. This also shifts the pool price based on how we update the reserves during such a trade 𝐑→𝐑′\mathbf{R}\rightarrow\mathbf{R}^{\prime}. To get the marginal execution price for a trade of Δ\Delta, we can just derive the above invariant:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​Δ​φ​(x+γ​Δ,y−Λ​(Δ))\displaystyle\frac{d}{d\Delta}\varphi(x+\gamma\Delta,y-\Lambda(\Delta)) | =∇→​φ⋅(γ​x^−d​Λd​Δ​y^)=0\displaystyle=\vec{\nabla}\varphi\cdot\left(\gamma\hat{x}-\frac{d\Lambda}{d\Delta}\hat{y}\right)=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​∂φ∂x\displaystyle\gamma\frac{\partial\varphi}{\partial x} | −∂φ∂y​d​Λd​Δ=0\displaystyle-\frac{\partial\varphi}{\partial y}\frac{d\Lambda}{d\Delta}=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Λd​Δ​(Δ)\displaystyle\frac{d\Lambda}{d\Delta}(\Delta) | =γ​Px​(𝐑′)\displaystyle=\gamma P\_{x}(\mathbf{R}^{\prime}) |  |

Notice that the marginal execution price is just the discounted price of the pool after the trade. As such, the relative price drift a market undergoes as a result of a trade can be expressed in terms of the marginal execution price for that trade.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μx​(Δ)=1−1γ​Px​d​Λd​Δ​(Δ),\displaystyle\mu\_{x}(\Delta)=1-\frac{1}{\gamma P\_{x}}\frac{d\Lambda}{d\Delta}(\Delta), | μy​(Δ)=γPy​(d​Λd​Δ​(Δ))−1−1.\displaystyle\mu\_{y}(\Delta)=\frac{\gamma}{P\_{y}}\left(\frac{d\Lambda}{d\Delta}(\Delta)\right)^{-1}-1. |  | (1) |

It will also prove useful to derive their inverse relationships, as they can be used to study how these drift terms transmit through coupled markets.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ​(μy)=Py′⁣−1​(Py​(μy+1)γ),\displaystyle\Delta(\mu\_{y})=P\_{y}^{\prime-1}\left(\frac{P\_{y}(\mu\_{y}+1)}{\gamma}\right), | Λ​(μy)=Λ​(Py′⁣−1​(Py​(μy+1)γ)).\displaystyle\Lambda(\mu\_{y})=\Lambda\left(P\_{y}^{\prime-1}\left(\frac{P\_{y}(\mu\_{y}+1)}{\gamma}\right)\right). |  | (2) |

Deriving the drift will give us the percent rate of change of the reported price as a function of swap input amount:

|  |  |  |
| --- | --- | --- |
|  | d​μyd​Δ​(Δ)=−γPy​d2​Λd​Δ2(d​Λd​Δ)2.\frac{d\mu\_{y}}{d\Delta}(\Delta)=-\frac{\gamma}{P\_{y}}\frac{\frac{d^{2}\Lambda}{d\Delta^{2}}}{(\frac{d\Lambda}{d\Delta})^{2}}. |  |

Now, the marginal swap depth, a measure of the rate of change of swap liquidity as a function of the price drift, is the reciprocal of this quantity.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dmarg,y​(μy)=−Pyγ​(d​Λd​Δ)2d2​Λd​Δ2.D\_{\text{marg},y}(\mu\_{y})=-\frac{P\_{y}}{\gamma}\frac{(\frac{d\Lambda}{d\Delta})^{2}}{\frac{d^{2}\Lambda}{d\Delta^{2}}}. |  | (3) |

This quantity gives us a direct measure of the market’s ability to absorb additional trade liquidity. So much like most measures of depth; the higher the value, the less shock that market will feel.

For the total depth of the market for a given price drift, simply integrate above marginal depth:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(μ)=−∫0μPyγ​(d​Λd​Δ)2d2​Λd​Δ2​𝑑μy.D(\mu)=-\int\_{0}^{\mu}\frac{P\_{y}}{\gamma}\frac{(\frac{d\Lambda}{d\Delta})^{2}}{\frac{d^{2}\Lambda}{d\Delta^{2}}}d\mu\_{y}. |  | (4) |

This covers all the relevant CFMM metrics we utilize in our analysis.

### 3.1 zz-Purchase

To start, consider the difference of intermediate basket value between the coupled and decoupled scenarios:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v1\displaystyle v\_{1} | =Py′​Λ​(Δ)−γ​Δ\displaystyle=P\_{y}^{\prime}\Lambda(\Delta)-\gamma\Delta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =γ​(Λ​(Δ)−Δ​d​Λd​Δd​Λd​Δ)\displaystyle=\gamma\left(\frac{\Lambda(\Delta)-\Delta\frac{d\Lambda}{d\Delta}}{\frac{d\Lambda}{d\Delta}}\right) |  |

Given that CFMMs must remain concave, the price of xx after swap, Px′=d​Λd​Δ/γP\_{x}^{\prime}=\frac{d\Lambda}{d\Delta}/\gamma, must obey the limit:

|  |  |  |
| --- | --- | --- |
|  | limΔ→∞d​Λd​Δ/γ=0.\lim\_{\Delta\to\infty}\frac{d\Lambda}{d\Delta}/\gamma=0. |  |

This implies that the intermediate value discrepancy itself must be unbounded, v1→∞v\_{1}\to\infty, with respect to trade size. Thus the concave nature of CFMMs (and realistically, most markets broadly) is the source of this basket value inflation relative to the decoupled scenario; the coupling only compounds this.

For the final zz/xx trade output value, propagate the above amounts received through the zz market and compute the after trade prices for each scenario. Use the relation Py′=γ​(d​Λd​Δ)−1=Py​(μ+1)P\_{y}^{\prime}=\gamma(\frac{d\Lambda}{d\Delta})^{-1}=P\_{y}(\mu+1) along with the inverse functions ([2](https://arxiv.org/html/2510.06095v1#S3.E2 "Equation 2 ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")) to change the base coordinate to price drift in the yy market.

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(Δ)\displaystyle v(\Delta) | =Pz′​Py′​Γ​(Λ​(Δ))−Pz′​Py​Γ​(γ1​Δ/Py)\displaystyle=P\_{z}^{\prime}P\_{y}^{\prime}\Gamma(\Lambda(\Delta))-P\_{z}^{\prime}P\_{y}\Gamma(\gamma\_{1}\Delta/P\_{y}) |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(μy)=γ2​Py​[Γ​(Λ​(μy))​(μy+1)d​Γd​Λ​(Λ​(μy))−Γ​(γ1​Δ​(μy)/Py)d​Γd​Λ​(γ1​Δ​(μy)/Py)].v(\mu\_{y})=\gamma\_{2}P\_{y}\left[\frac{\Gamma(\Lambda(\mu\_{y}))(\mu\_{y}+1)}{\frac{d\Gamma}{d\Lambda}(\Lambda(\mu\_{y}))}-\frac{\Gamma(\gamma\_{1}\Delta(\mu\_{y})/P\_{y})}{\frac{d\Gamma}{d\Lambda}(\gamma\_{1}\Delta(\mu\_{y})/P\_{y})}\right]. |  | (5) |

Notice that the only difference between the two compared cases, coupled as the initial term and decoupled as the latter, is the amount of tokens flowing into the zz market and the yy drift adjustment for the coupled scenario. Consider the effective trade price in this context, Pe​f​f=Δ​(μy)Λ​(μy)P\_{eff}=\frac{\Delta(\mu\_{y})}{\Lambda(\mu\_{y})}. By concavity requirements, the effective price paid will be necessarily greater than or equal to the fee augmented spot price, Pe​f​f≥γ1​PyP\_{eff}\geq\gamma\_{1}P\_{y}, only equivalent in the case of constant sum markets. This would imply the inequality

|  |  |  |
| --- | --- | --- |
|  | d​Γd​Λ​(γ1​Δ​(μy)/Py)>d​Γd​Λ​(Λ​(μy)).{\frac{d\Gamma}{d\Lambda}(\gamma\_{1}\Delta(\mu\_{y})/P\_{y})}>{\frac{d\Gamma}{d\Lambda}(\Lambda(\mu\_{y}))}. |  |

Which just means when denominated purely in yy, the coupled basket comes out at a loss relative to the decoupled basket, which should be expected given the reduced Λ\Lambda input amount. This also gives us exactly the condition we want for determining when this coupling causes inflationary versus deflationary purchases relative to decoupled:

|  |  |  |
| --- | --- | --- |
|  | μy≥Γ​(γ1​Δ​(μy)/Py)Γ​(Λ​(μy))​d​Γd​Λ​(Λ​(μy))d​Γd​Λ​(γ1​Δ​(μy)/Py)−1.\mu\_{y}\geq\frac{\Gamma(\gamma\_{1}\Delta(\mu\_{y})/P\_{y})}{\Gamma(\Lambda(\mu\_{y}))}\frac{\frac{d\Gamma}{d\Lambda}(\Lambda(\mu\_{y}))}{\frac{d\Gamma}{d\Lambda}(\gamma\_{1}\Delta(\mu\_{y})/P\_{y})}-1. |  |

First note that because the quantity of zz received in the decoupled case is necessarily higher than the coupled case regardless of the yy/xx CFMM at play, the right-hand side of this inequality is positive for all μy>0\mu\_{y}>0. Meaning that it is theoretically possible for a CFMM to cause deflationary purchases when coupled in this setting, even with small purchases; the only requirement is that the price drift percentage is less than this right-hand side. Arranging this as an indicator function, for reasonable trade sizes, Δ≪Py​y1\Delta\ll P\_{y}y\_{1} (or the equivalent price drift range),

|  |  |  |  |
| --- | --- | --- | --- |
|  | l​(μy)=μy+1−Γ​(γ1​Δ​(μy)/Py)Γ​(Λ​(μy))​d​Γd​Λ​(Λ​(μy))d​Γd​Λ​(γ1​Δ​(μy)/Py)l(\mu\_{y})=\mu\_{y}+1-\frac{\Gamma(\gamma\_{1}\Delta(\mu\_{y})/P\_{y})}{\Gamma(\Lambda(\mu\_{y}))}\frac{\frac{d\Gamma}{d\Lambda}(\Lambda(\mu\_{y}))}{\frac{d\Gamma}{d\Lambda}(\gamma\_{1}\Delta(\mu\_{y})/P\_{y})} |  | (6) |

where l>0l>0 implies inflation, l<0l<0 implies deflation, and l=0l=0 implies parity between coupled and decoupled behavior.

Next, for the price drift transmission, take the post-swap quantity from ([2](https://arxiv.org/html/2510.06095v1#S3.E2 "Equation 2 ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")) and propagate into the drift term ([1](https://arxiv.org/html/2510.06095v1#S3.E1 "Equation 1 ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")) for the zz market.

|  |  |  |  |
| --- | --- | --- | --- |
|  | μz​(μy)=γ2Pz​(d​Γd​Λ​(Λy​(Py′⁣−1​(Py​(μy+1)γ))))−1−1.\mu\_{z}(\mu\_{y})=\frac{\gamma\_{2}}{P\_{z}}\left(\frac{d\Gamma}{d\Lambda}\left(\Lambda\_{y}\left(P\_{y}^{\prime-1}\left(\frac{P\_{y}(\mu\_{y}+1)}{\gamma}\right)\right)\right)\right)^{-1}-1. |  | (7) |

This is a little opaque without a specific CFMM, but intuitively, this just computing the swap amount required to achieve a particular μy\mu\_{y}, then propagating that amount through the computation of the price drift incurred in the second swap, μz\mu\_{z}. Looking at the limiting behavior, as μy→∞\mu\_{y}\to\infty, the liquidity in the first pool is exhausted, leading to a bound on the input amount into the second swap. This means that μz​(μy)\mu\_{z}(\mu\_{y}) is always bounded based on the quantity of yy assets in the yy market, implying that transmission is bounded by this same amount. This is exactly the expected behavior for any potential yy market structure, not just CFMMs, due to the inherent finite liquidity constraint any realistic asset will encounter. Most of what is interesting about this function appears in its curvature, however, as this property would require a fixed CFMM function for proper analysis, it is left for the constant product market maker case study.

Now, to study the marginal cost of purchase, consider a shared reserve state (x,y1,y2,z)∈ℝ+4(x,y\_{1},y\_{2},z)\in\mathbb{R}^{4}\_{+}. For a multi-asset trade 𝚫\mathbf{\Delta} with output 𝚲​(𝚫)\mathbf{\Lambda}(\mathbf{\Delta}), we can study the output received by looking at how this reserve state changes under a this trade’s transition function, defined around the respective pool invariants:

|  |  |  |
| --- | --- | --- |
|  | 𝐑′=𝐅​(𝐑,𝚫)=(x+Δx−Λx​(𝚫),y1+Δy1−Λy1​(𝚫),y2+Δy2−Λy2​(𝚫),z+Δz−Λz​(𝚫)),\mathbf{R}^{\prime}=\mathbf{F}(\mathbf{R},\mathbf{\Delta})=(x+\Delta\_{x}-\Lambda\_{x}(\mathbf{\Delta}),y\_{1}+\Delta\_{y\_{1}}-\Lambda\_{y\_{1}}(\mathbf{\Delta}),y\_{2}+\Delta\_{y\_{2}}-\Lambda\_{y\_{2}}(\mathbf{\Delta}),z+\Delta\_{z}-\Lambda\_{z}(\mathbf{\Delta})), |  |

with the definitions of Λi​(𝚫)\Lambda\_{i}(\mathbf{\Delta}) fixed via solving for the swap output amount given the respective output reserve’s invariant function.

For the coupled scenario of interest, restrict Δy1=Δz=0\Delta\_{y\_{1}}=\Delta\_{z}=0, and Δy2′=Λy2​(Δx)\Delta\_{y\_{2}}^{\prime}=\Lambda\_{y\_{2}}(\Delta\_{x}). Since this transition function gives the reserves after swap, the marginal output of purchasing additional units is found by perturbing the swap input by δ​Δ\delta\Delta. So, consider the following expansion of 𝐅\mathbf{F}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​𝐑′\displaystyle\delta\mathbf{R}^{\prime} | =∑n=0∞1n!​∂n𝐅∂Δn​(δ​Δ)n\displaystyle=\sum\_{n=0}^{\infty}\frac{1}{n!}\frac{\partial^{n}\mathbf{F}}{\partial\Delta^{n}}(\delta\Delta)^{n} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​𝐑′\displaystyle\delta\mathbf{R}^{\prime} | =J𝐅​(Δ)​δ​Δ+H𝐅​(Δ)​(δ​Δ)2+⋯\displaystyle=J\_{\mathbf{F}}(\Delta)\delta\Delta+H\_{\mathbf{F}}(\Delta)(\delta\Delta)^{2}+\cdots |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​𝐑′\displaystyle\delta\mathbf{R}^{\prime} | =[1−d​Λd​Δd​Λd​Δ−d​Γd​Λ​d​Λd​Δ]​δ​Δ+12​[0−d2​Λd​Δ2d2​Λd​Δ2−d2​Γd​Λ2​(d​Λd​Δ)2−d​Γd​Λ​d2​Λd​Δ2]​(δ​Δ)2+⋯\displaystyle=\begin{bmatrix}1\\ -\frac{d\Lambda}{d\Delta}\\ \frac{d\Lambda}{d\Delta}\\ -\frac{d\Gamma}{d\Lambda}\frac{d\Lambda}{d\Delta}\end{bmatrix}\delta\Delta+\frac{1}{2}\begin{bmatrix}0\\ -\frac{d^{2}\Lambda}{d\Delta^{2}}\\ \frac{d^{2}\Lambda}{d\Delta^{2}}\\ -\frac{d^{2}\Gamma}{d\Lambda^{2}}(\frac{d\Lambda}{d\Delta})^{2}-\frac{d\Gamma}{d\Lambda}\frac{d^{2}\Lambda}{d\Delta^{2}}\end{bmatrix}(\delta\Delta)^{2}+\cdots |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​𝐑′\displaystyle\delta\mathbf{R}^{\prime} | =[1−d​Λd​Δd​Λd​Δ−d​Γd​Λ​d​Λd​Δ]​δ​Δ+12​[0γ1Py​(μy+1)2​Dmarg,y−γ1Py​(μy+1)2​Dmarg,yγ2Pz​(μz​(μy)+1)2​Dmarg,z​d​Λd​Δ2+γ1Py​(μy+1)2​Dmarg,y​d​Γd​Λ]​(δ​Δ)2+⋯\displaystyle=\begin{bmatrix}1\\ -\frac{d\Lambda}{d\Delta}\\ \frac{d\Lambda}{d\Delta}\\ -\frac{d\Gamma}{d\Lambda}\frac{d\Lambda}{d\Delta}\end{bmatrix}\delta\Delta+\frac{1}{2}\begin{bmatrix}0\\ \frac{\gamma\_{1}}{P\_{y}(\mu\_{y}+1)^{2}D\_{\text{marg},y}}\\ -\frac{\gamma\_{1}}{P\_{y}(\mu\_{y}+1)^{2}D\_{\text{marg},y}}\\ \frac{\gamma\_{2}}{P\_{z}(\mu\_{z}(\mu\_{y})+1)^{2}D\_{\text{marg},z}}\frac{d\Lambda}{d\Delta}^{2}+\frac{\gamma\_{1}}{P\_{y}(\mu\_{y}+1)^{2}D\_{\text{marg},y}}\frac{d\Gamma}{d\Lambda}\end{bmatrix}(\delta\Delta)^{2}+\cdots |  |

Stop at second order for now, as it contains most of the information needed about curvature in the compound market. Because the only unit being purchased in the end in the zz asset, ignore everything but the fourth coordinate. In one line this reads as

|  |  |  |
| --- | --- | --- |
|  | δ​Rz′≈−d​Γd​Λ​d​Λd​Δ​δ​Δ+12​[γ2Pz​(μz​(μy)+1)2​Dmarg,z​d​Λd​Δ2+γ1Py​(μy+1)2​Dmarg,y​d​Γd​Λ]​(δ​Δ)2.\delta R\_{z}^{\prime}\approx-\frac{d\Gamma}{d\Lambda}\frac{d\Lambda}{d\Delta}\delta\Delta+\frac{1}{2}\left[\frac{\gamma\_{2}}{P\_{z}(\mu\_{z}(\mu\_{y})+1)^{2}D\_{\text{marg},z}}\frac{d\Lambda}{d\Delta}^{2}+\frac{\gamma\_{1}}{P\_{y}(\mu\_{y}+1)^{2}D\_{\text{marg},y}}\frac{d\Gamma}{d\Lambda}\right](\delta\Delta)^{2}. |  |

Substituting in the price drift in the yy-market, and changing the variables of the perturbation to be in terms of a change in drift, with δ​Δ=Dmarg,y​(μy)​δ​μy\delta\Delta=D\_{\text{marg},y}(\mu\_{y})\delta\mu\_{y},

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​Rz′​(μy)≈−\displaystyle\delta R\_{z}^{\prime}(\mu\_{y})\approx- | γ1​γ2​Dmarg,yPz​Py​(μz​(μy)+1)​(μy+1)​δ​μy\displaystyle\frac{\gamma\_{1}\gamma\_{2}D\_{\text{marg},y}}{P\_{z}P\_{y}(\mu\_{z}(\mu\_{y})+1)(\mu\_{y}+1)}\delta\mu\_{y} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​[γ2​Dmarg,y2Pz​(μz​(μy)+1)2​Py2​(μy+1)2​Dmarg,z+γ1​Dmarg,yPy​(μy+1)2​Pz​(μz​(μy)+1)]​(δ​μy)2.\displaystyle+\frac{1}{2}\left[\frac{\gamma\_{2}D\_{\text{marg},y}^{2}}{P\_{z}(\mu\_{z}(\mu\_{y})+1)^{2}P\_{y}^{2}(\mu\_{y}+1)^{2}D\_{\text{marg},z}}+\frac{\gamma\_{1}D\_{\text{marg},y}}{P\_{y}(\mu\_{y}+1)^{2}P\_{z}(\mu\_{z}(\mu\_{y})+1)}\right]\left(\delta\mu\_{y}\right)^{2}. |  |

Read another way, with P′=P⋅(μ+1)P^{\prime}=P\cdot(\mu+1), the change in reserves in both Δ\Delta and μy\mu\_{y}-spaces are the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​Rz′≈−γ1​γ2Pz′​Py′​δ​Δ+12​[γ2Pz′​(μz​(μy)+1)​Py′⁣2​Dmarg,z+γ1Pz′​Py′​(μy+1)​Dmarg,y]​(δ​Δ)2,\delta R\_{z}^{\prime}\approx-\frac{\gamma\_{1}\gamma\_{2}}{P\_{z}^{\prime}P\_{y}^{\prime}}\delta\Delta+\frac{1}{2}\left[\frac{\gamma\_{2}}{P\_{z}^{\prime}(\mu\_{z}(\mu\_{y})+1)P\_{y}^{\prime 2}D\_{\text{marg},z}}+\frac{\gamma\_{1}}{P\_{z}^{\prime}P\_{y}^{\prime}(\mu\_{y}+1)D\_{\text{marg},y}}\right]\left(\delta\Delta\right)^{2}, |  | (8) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​Rz′≈−γ1​γ2Pz′​Py′​Dmarg,y​δ​μy+12​[γ2​Dmarg,y2Pz′​(μz​(μy)+1)​Py′⁣2​Dmarg,z+γ1​Dmarg,yPz′​Py′​(μy+1)]​(δ​μy)2.\delta R\_{z}^{\prime}\approx-\frac{\gamma\_{1}\gamma\_{2}}{P\_{z}^{\prime}P\_{y}^{\prime}}D\_{\text{marg},y}\delta\mu\_{y}+\frac{1}{2}\left[\frac{\gamma\_{2}D\_{\text{marg},y}^{2}}{P\_{z}^{\prime}(\mu\_{z}(\mu\_{y})+1)P\_{y}^{\prime 2}D\_{\text{marg},z}}+\frac{\gamma\_{1}D\_{\text{marg},y}}{P\_{z}^{\prime}P\_{y}^{\prime}(\mu\_{y}+1)}\right]\left(\delta\mu\_{y}\right)^{2}. |  | (9) |

Let’s be more explicit about how this relates to the trader’s output basket now:

|  |  |  |
| --- | --- | --- |
|  | 𝐎​(Δ)=𝐑−𝐑′\mathbf{O}(\Delta)=\mathbf{R}-\mathbf{R}^{\prime} |  |

with the marginal output as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | o​(δ​Δ)=−δ​𝐑′o(\delta\Delta)=-\delta\mathbf{R}^{\prime} |  | (10) |

Now to get the marginal cost, all we need to do is flip this so:

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(δ​Δ)=−δ​Δδ​𝐑′c(\delta\Delta)=-\frac{\delta\Delta}{\delta\mathbf{R}^{\prime}} |  | (11) |

First thing worth noticing in ([9](https://arxiv.org/html/2510.06095v1#S3.E9 "Equation 9 ‣ 3.1 𝑧-Purchase ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")), there’s a consistent factor of (μy+1)−1(\mu\_{y}+1)^{-1}, implying that the marginal cost has a proportional relationship with the percent price adjustment in the yy-market. This implies a cost structure that inflates relative to xx due to this yy dependence.

Now breaking down more intuitively what each term represents, ([8](https://arxiv.org/html/2510.06095v1#S3.E8 "Equation 8 ‣ 3.1 𝑧-Purchase ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")) and ([9](https://arxiv.org/html/2510.06095v1#S3.E9 "Equation 9 ‣ 3.1 𝑧-Purchase ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")) can be summarized as:

|  |  |  |
| --- | --- | --- |
|  | Marginal Output=Compounded Sensitivity − Pool Curvature Penalties\text{Marginal Output}=\text{Compounded Sensitivity }-\text{ Pool Curvature Penalties} |  |

The linear term is just the product of marginal trade prices in each pool, and acts as a measure of the marginal price after trade on the compound zz/xx market:

|  |  |  |  |
| --- | --- | --- | --- |
|  | a1\displaystyle a\_{1} | =d​Γd​Λ​d​Λd​Δ\displaystyle=\frac{d\Gamma}{d\Lambda}\frac{d\Lambda}{d\Delta} |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | |d​Λd​Δ|=\displaystyle\bigg|\frac{d\Lambda}{d\Delta}\bigg|= | marginal output sensitivity from the z-market,\displaystyle\text{ marginal output sensitivity from the $z$-market}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |d​Λd​Δ|=\displaystyle\bigg|\frac{d\Lambda}{d\Delta}\bigg|= | marginal output sensitivity from the yy-market. |  |

This would suggest the expected: intermediate CFMMs curves compound their slippage in the zz/xx market.

For the second term of the expansion, let’s define actual trade curvature for each pool as the second derivative of their swap methods:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κy=−d2​Λd​Δ2=γ1Py​(μy+1)2​Dmarg,y,\displaystyle\kappa\_{y}=-\frac{d^{2}\Lambda}{d\Delta^{2}}=\frac{\gamma\_{1}}{P\_{y}(\mu\_{y}+1)^{2}D\_{\text{marg},y}}, | κz=γ2Pz​(μz+1)2​Dmarg,z\displaystyle\kappa\_{z}=\frac{\gamma\_{2}}{P\_{z}(\mu\_{z}+1)^{2}D\_{\text{marg},z}} |  |

substituting these into our second-order term leaves us with:

|  |  |  |  |
| --- | --- | --- | --- |
|  | a2=−12​(κy​γ2Pz′+κzPy′⁣2)a\_{2}=-\frac{1}{2}\left(\frac{\kappa\_{y}\gamma\_{2}}{P\_{z}^{\prime}}+\frac{\kappa\_{z}}{P\_{y}^{\prime 2}}\right) |  | (12) |

Notice what each term in a2a\_{2} represents. κy​γ2Pz′\frac{\kappa\_{y}\gamma\_{2}}{P\_{z}^{\prime}} is just a product of the yy-purchase curvature with the marginal execution price of purchasing zz. In a sense, the contribution of how the yy-market curvature contributes to the immediate curvature in the zz-market. The latter term has the inverse interpretation, capture how the immediate marginal execution price in the yy-market propagates into the purchase curvature on the zz-market, where the squared factor arises due to the coupling the purchase has on the price of yy. Thus, −2​a2-2a\_{2}, which is exactly the compound zz/xx market’s purchase curvature, is a coupled sum of the intermediate markets purchase curvatures.

More practically speaking, ([12](https://arxiv.org/html/2510.06095v1#S3.E12 "Equation 12 ‣ 3.1 𝑧-Purchase ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")) shows that poor depth in *either* pool creates outsized slippage in the compound market. From the perspective of a market designer, choosing where to concentrate liquidity isn’t about just optimizing each pool’s distribution in isolation - you need to balance depth across both pools.

### 3.2 zz-Liquidation

Consider now a zz liquidation event. The trader holds a basket of Γ\Gamma zz tokens and wishes to liquidate all of it for xx assets. Note that the swap functions will be flipped for this event, Λ​(Δ)→Δ​(Λ)\Lambda(\Delta)\to\Delta(\Lambda).

First, use the relation Pz=Pz/y=1Py/zP\_{z}=P\_{z/y}=\frac{1}{P\_{y/z}} to redefine the price drift in terms of familiar xx denominations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μz=μy/z​(Γ)=1−1γ2​Pz​d​Λd​Γ​(Γ),\displaystyle\mu\_{z}=\mu\_{y/z}(\Gamma)=1-\frac{1}{\gamma\_{2}P\_{z}}\frac{d\Lambda}{d\Gamma}(\Gamma), | μy​(Γ)=γ2​Pz​(d​Λd​Γ​(Γ))−1−1\displaystyle\mu\_{y}(\Gamma)=\gamma\_{2}P\_{z}\left(\frac{d\Lambda}{d\Gamma}(\Gamma)\right)^{-1}-1 |  |

Similarly, on the yy market,

|  |  |  |  |
| --- | --- | --- | --- |
|  | μy1=μx/y​(Λ)=1−1γ1​Py​d​Δd​Λ​(Λ),\displaystyle\mu\_{y\_{1}}=\mu\_{x/y}(\Lambda)=1-\frac{1}{\gamma\_{1}P\_{y}}\frac{d\Delta}{d\Lambda}(\Lambda), | μx​(Λ)=γ1​Py​(d​Δd​Λ​(Λ))−1−1\displaystyle\mu\_{x}(\Lambda)=\gamma\_{1}P\_{y}\left(\frac{d\Delta}{d\Lambda}(\Lambda)\right)^{-1}-1 |  |

To start, again consider the difference in basket value between coupled and baseline scenarios on just the yy sale alone:

|  |  |  |
| --- | --- | --- |
|  | v2=Δ​(Λ)−γ1​Py​Λ\displaystyle v\_{2}=\Delta(\Lambda)-\gamma\_{1}P\_{y}\Lambda |  |

There is nothing special really happening here. Because Py,e​f​f<γ1​PyP\_{y,eff}<\gamma\_{1}P\_{y} where Δ​(Λ)=Py,e​f​f​Λ\Delta(\Lambda)=P\_{y,eff}\Lambda its clear that v2<0v\_{2}<0 for all Λ\Lambda, simply implying the sale of tokens on a CFMM undergoes slippage. Now propagate the swap output from the sale of Γ\Gamma on the zz/yy market through v2v\_{2} for the net value discrepancy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(Γ)=Δ​(Λ​(Γ))−γ1​Py​Λ​(Γ)v(\Gamma)=\Delta(\Lambda(\Gamma))-\gamma\_{1}P\_{y}\Lambda(\Gamma) |  | (13) |

Since this is fundamentally the same equation as above relative to the amount of yy assets being sold, the same deflationary principle persists. The main distinction will appear again in the compounded curvature of this function relative to Γ\Gamma as opposed to v2v\_{2} with Λ\Lambda. It should also be noted the different form this takes relative to these metrics for the purchase event is simply from the choice of denomination being the target asset rather than the initial.

Now, using the same state space model as the purchase event, define a liquidation transition function by swapping in the opposite direction.

|  |  |  |
| --- | --- | --- |
|  | 𝐅l​(𝐑,Γ)=(Rx−Δ​(Λ​(Γ)),Ry1+Λ​(Γ),Ry2−Λ​(Γ),Rz+Γ)\mathbf{F}\_{l}(\mathbf{R},\Gamma)=(R\_{x}-\Delta(\Lambda(\Gamma)),R\_{y\_{1}}+\Lambda(\Gamma),R\_{y\_{2}}-\Lambda(\Gamma),R\_{z}+\Gamma) |  |

So, with a similar perturbative expansion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​𝐑′\displaystyle\delta\mathbf{R}^{\prime} | =∑n=0∞1n!​∂n𝐅l∂Γn​(δ​Γ)n\displaystyle=\sum\_{n=0}^{\infty}\frac{1}{n!}\frac{\partial^{n}\mathbf{F}\_{l}}{\partial\Gamma^{n}}(\delta\Gamma)^{n} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​𝐑′\displaystyle\delta\mathbf{R}^{\prime} | =J𝐅l​(Γ)​δ​Γ+H𝐅l​(Γ)​(δ​Γ)2+⋯\displaystyle=J\_{\mathbf{F}\_{l}}(\Gamma)\delta\Gamma+H\_{\mathbf{F}\_{l}}(\Gamma)(\delta\Gamma)^{2}+\cdots |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[−d​Δd​Λ​d​Λd​Γd​Λd​Γ−d​Λd​Γ1]​δ​Γ+12​[−d2​Δd​Λ2​(d​Λd​Γ)2−d​Δd​Λ​d2​Λd​Γ2d2​Λd​Γ2−d2​Λd​Γ20]​(δ​Γ)2+⋯\displaystyle=\begin{bmatrix}-\frac{d\Delta}{d\Lambda}\frac{d\Lambda}{d\Gamma}\\ \frac{d\Lambda}{d\Gamma}\\ -\frac{d\Lambda}{d\Gamma}\\ 1\end{bmatrix}\delta\Gamma+\frac{1}{2}\begin{bmatrix}-\frac{d^{2}\Delta}{d\Lambda^{2}}\left(\frac{d\Lambda}{d\Gamma}\right)^{2}-\frac{d\Delta}{d\Lambda}\frac{d^{2}\Lambda}{d\Gamma^{2}}\\ \frac{d^{2}\Lambda}{d\Gamma^{2}}\\ -\frac{d^{2}\Lambda}{d\Gamma^{2}}\\ 0\end{bmatrix}(\delta\Gamma)^{2}+\cdots |  |

Isolating just for the xx reserve coordinate, and substituting in the curvature terms for each sale:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​R′≈−d​Δd​Λ​d​Λd​Γ​δ​Γ+12​[1γ1​Py​Dmarg,x​(d​Δd​Λ​d​Λd​Γ)2+1γ2​Pz​Dmarg,y​d​Δd​Λ​(d​Λd​Γ)2]​(δ​Γ)2.\delta R^{\prime}\approx-\frac{d\Delta}{d\Lambda}\frac{d\Lambda}{d\Gamma}\delta\Gamma+\frac{1}{2}\left[\frac{1}{\gamma\_{1}P\_{y}D\_{\text{marg},x}}\left(\frac{d\Delta}{d\Lambda}\frac{d\Lambda}{d\Gamma}\right)^{2}+\frac{1}{\gamma\_{2}P\_{z}D\_{\text{marg},y}}\frac{d\Delta}{d\Lambda}\left(\frac{d\Lambda}{d\Gamma}\right)^{2}\right](\delta\Gamma)^{2}. |  | (14) |

In terms of the relative marginal depths, with the change of variables δ​Γ=Dmarg,y​δ​μy\delta\Gamma=D\_{\text{marg},y}\delta\mu\_{y} this reads as

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​R′≈−γ1​γ2​Py​Pz​Dmarg,y(μy+1)​(μx+1)​δ​μy+12​[γ1​γ22​Py​Pz2​Dmarg,y2(μy+1)2​(μx+1)2​Dmarg,x+γ1​γ2​Py​Pz(μy+1)2​(μx+1)​Dmarg,y]​(δ​μy)2.\delta R^{\prime}\approx-\frac{\gamma\_{1}\gamma\_{2}P\_{y}P\_{z}D\_{\text{marg},y}}{(\mu\_{y}+1)(\mu\_{x}+1)}\delta\mu\_{y}+\frac{1}{2}\left[\frac{\gamma\_{1}\gamma\_{2}^{2}P\_{y}P\_{z}^{2}D\_{\text{marg},y}^{2}}{(\mu\_{y}+1)^{2}(\mu\_{x}+1)^{2}D\_{\text{marg},x}}+\frac{\gamma\_{1}\gamma\_{2}P\_{y}P\_{z}}{(\mu\_{y}+1)^{2}(\mu\_{x}+1)}D\_{\text{marg},y}\right](\delta\mu\_{y})^{2}. |  | (15) |

Where the marginal cost function is again c​(δ​Γ)=−δ​R′δ​Γc(\delta\Gamma)=-\frac{\delta R^{\prime}}{\delta\Gamma}. This is essentially the same result as the purchase scenario, with the only difference being direction (hence the reciprocal price appearances). Looking at the liquidation curvature terms for each pool now:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κy=γ2​Pz(μy+1)2​Dmarg,y1,\displaystyle\kappa\_{y}=\frac{\gamma\_{2}P\_{z}}{(\mu\_{y}+1)^{2}D\_{\text{marg},y\_{1}}}, | κx=γ1​Py(μx+1)2​Dmarg,x\displaystyle\kappa\_{x}=\frac{\gamma\_{1}P\_{y}}{(\mu\_{x}+1)^{2}D\_{\text{marg},x}} |  |

with the compound liquidation curvature being −2​b2-2b\_{2} for

|  |  |  |
| --- | --- | --- |
|  | b2=−(γ22​Pz2​κx(μy+1)2+κy​γ1​Py(μx+1)).b\_{2}=-\left(\frac{\gamma\_{2}^{2}P\_{z}^{2}\kappa\_{x}}{(\mu\_{y}+1)^{2}}+\frac{\kappa\_{y}\gamma\_{1}P\_{y}}{(\mu\_{x}+1)}\right). |  |

## 4 Constant Product Market Maker Case Study

Constant product market makers (CPMM), such as Uniswap v2, is a protocol that facilitates spot trading markets. The constant product market maker, defined by the invariant

|  |  |  |
| --- | --- | --- |
|  | φ​(x,y)=x​y,\varphi(x,y)=xy, |  |

is one of the most well studied CFMMs to date. It boasts many nice properties for a spot market, such as readily available marginal trading liquidity at any price, for either asset in the pool, or extremely implementation-friendly core trading functions. Most importantly for this analysis, it provides a tractable setting to develop an intuition that readily extends to the general case, for how many CFMMs will behave.

Before the coupled analysis, start by computing the core pool metrics defined in (1) for a CPMM. The price functions are simply the ratio of reserves,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Px=φxφy=yx,\displaystyle P\_{x}=\frac{\varphi\_{x}}{\varphi\_{y}}=\frac{y}{x}, | Py=xy.\displaystyle P\_{y}=\frac{x}{y}. |  |

To compute the swap function, hold φ​(x,y)\varphi(x,y) invariant under the trade and isolate for Λ\Lambda:

|  |  |  |
| --- | --- | --- |
|  | (x+γ​Δ)​(y−Λ)=k\displaystyle(x+\gamma\Delta)(y-\Lambda)=k |  |
|  |  |  |
| --- | --- | --- |
|  | y−Λ=x​yx+γ​Δ\displaystyle y-\Lambda=\frac{xy}{x+\gamma\Delta} |  |
|  |  |  |
| --- | --- | --- |
|  | Λ​(Δ)=y​γ​Δx+γ​Δ.\displaystyle\Lambda(\Delta)=\frac{y\gamma\Delta}{x+\gamma\Delta}. |  |

Deriving this functions, and substituting into ([1](https://arxiv.org/html/2510.06095v1#S3.E1 "Equation 1 ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")), yields the price drift of both asset prices due to the trade:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μy=(x+γ​Δ)2y2−1,\displaystyle\mu\_{y}=\frac{(x+\gamma\Delta)^{2}}{y^{2}}-1, | μx=1−x2(x+γ​Δ)2,\displaystyle\mu\_{x}=1-\frac{x^{2}}{(x+\gamma\Delta)^{2}}, |  |

with inverse function

|  |  |  |
| --- | --- | --- |
|  | Δ​(μy)=yγ​μy+1−xγ.\Delta(\mu\_{y})=\frac{y}{\gamma}\sqrt{\mu\_{y}+1}-\frac{x}{\gamma}. |  |

Deriving the drift more time and taking the reciprocal recovers the marginal trade depth ([3](https://arxiv.org/html/2510.06095v1#S3.E3 "Equation 3 ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")),

|  |  |  |
| --- | --- | --- |
|  | Dmarg,y=2​γ​(x+γ​Δ)y2D\_{\text{marg},y}=\frac{2\gamma(x+\gamma\Delta)}{y^{2}} |  |

This concludes the single pool CPMM metrics required to derive the relevant coupling behavior. Note for both purchase and liquidation events, all visualizations will be taken with respect to the same parameterization of the coupled system. So consider an auction house-like liquidity structure with the reserves x=107x=10^{7}, y1=4.5×108y\_{1}=4.5\times 10^{8}, y2=7.2×107y\_{2}=7.2\times 10^{7}, and z=109z=10^{9}, where both pool fees are set to 3%3\%. While these fees are typically way too high for established markets, this structure mirrors what is seen in a lot of emerging markets, where the yy-market rightfully holds the majority share of the yy liquidity relative to the zz market and the effect of coupling is significant.

### 4.1 zz-Purchase

For the zz purchase event on a coupled CPMM-CPMM market, start by computing the quantity of zz the trader receives,

|  |  |  |
| --- | --- | --- |
|  | z​ received=Γ​(Δ)=y1​z​γ2​γ1​Δx​y2+(y2+γ2​y1)​γ1​Δ.z\text{ received}=\Gamma(\Delta)=\frac{y\_{1}z\gamma\_{2}\gamma\_{1}\Delta}{xy\_{2}+(y\_{2}+\gamma\_{2}y\_{1})\gamma\_{1}\Delta}. |  |

In the decoupled scenario, use the spot price of the initial market to fix the entry swap quantity in the zz market, so Γ​(y1x​γ1​Δ)\Gamma(\frac{y\_{1}}{x}\gamma\_{1}\Delta).

Substituting the derived pool metrics in ([5](https://arxiv.org/html/2510.06095v1#S3.E5 "Equation 5 ‣ 3.1 𝑧-Purchase ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")), the basket value discrepancy as a function of price drift in the yy market reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(μy)=γ2​xy1​y2​(y1x​μy+1−1)​(μy+1​(x​y2+x​y1​γ2−γ2​y13/x)+γ2​(y12−x2)−y1​y2).v(\mu\_{y})=\frac{\gamma\_{2}x}{y\_{1}y\_{2}}\left(\frac{y\_{1}}{x}\sqrt{\mu\_{y}+1}-1\right)\left(\sqrt{\mu\_{y}+1}(xy\_{2}+xy\_{1}\gamma\_{2}-\gamma\_{2}y\_{1}^{3}/x)+\gamma\_{2}(y\_{1}^{2}-x^{2})-y\_{1}y\_{2}\right). |  | (16) |

Notice this is a quadratic function with respect to u=μy+1u=\sqrt{\mu\_{y}+1}, with v​(0)=0v(0)=0, v′​(0)=0v^{\prime}(0)=0, and v′′​(u)>0v^{\prime\prime}(u)>0 for ∀u>0\forall u>0; implying the zz purchase event yields always a basket with inflated value.

![Refer to caption](figures/val.png)


Figure 1: The basket value difference between the coupled and decoupled market scenarios on a zz-purchase event.

On a per-trade level, each pool experiences some amount of portfolio loss as the trade pushes the prices higher, often referred to as impermanent loss in this context. This loss is path-independent in the price process, implying that any change in valuation dynamic between trader and pool can be reversed (up to fee accounting). The liquidity provider’s portfolio loss is exactly the source the above convex basket inflation, just sourced from two pools as opposed to one.

Now turning to the price drift transmission,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μz​(μy)\displaystyle\mu\_{z}(\mu\_{y}) | =(y2​x​μy+1+γ2​y1​x​(μy+1−1))2x2​(μy+1)​y22−1.\displaystyle=\frac{(y\_{2}x\sqrt{\mu\_{y}+1}+\gamma\_{2}y\_{1}x(\sqrt{\mu\_{y}+1}-1))^{2}}{x^{2}(\mu\_{y}+1)y\_{2}^{2}}-1. |  | (17) |

For the provided reserve and fee values set at the start of the section, [2](https://arxiv.org/html/2510.06095v1#S4.F2 "Figure 2 ‣ 4.1 𝑧-Purchase ‣ 4 Constant Product Market Maker Case Study ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.") displays this transmission function.

![Refer to caption](figures/f7.png)


Figure 2: The transmission of μy\mu\_{y} into the price drift in the zz-market, μz​(μy)\mu\_{z}(\mu\_{y}).

Notice the rate of change of this function is more strongly positive for small swap amounts, gradually slowing until the price coupling flattens out once most of the yy tokens have been purchased in the initial market. Whether this transmission is reflexive, however, where the drift μz\mu\_{z} denominated relative to yy outpaces μy\mu\_{y} depends entirely on how the yy liquidity is distributed among the intermediate pools.

Next, look at the marginal cost function in μy\mu\_{y}-space. Explicit closed-form expressions for the CPMM marginal cost functions are available in the supplementary materials, though practitioners will find equation ([9](https://arxiv.org/html/2510.06095v1#S3.E9 "Equation 9 ‣ 3.1 𝑧-Purchase ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")) and the derived swap, marginal depth, and price drift functions more tractable for numerical evaluation.

A topographic plot of o​(μy,δ​μy)o(\mu\_{y},\delta\mu\_{y}) is for the purchase event is seen in [3](https://arxiv.org/html/2510.06095v1#S4.F3 "Figure 3 ‣ 4.1 𝑧-Purchase ‣ 4 Constant Product Market Maker Case Study ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.") below.

![Refer to caption](figures/mcostpurch.png)


Figure 3: The marginal output amount, o​(δ​μy)o(\delta\mu\_{y}), for δ​μy\delta\mu\_{y} additional price drift in the yy-market.

As convexity of the CFMM invariant would suggest, the marginal output amount received is highest for small trade sizes diminishing with larger and larger size. As well, from what can be observed in the gradient, the rate that this marginal output decreases by also decreases with trade size. This is very much what we would expect from any CFMM that doesn’t specifically fix these values (such as a constant sum curve would), implying that the compounded market behaves much like a CFMM in its own right when isolating the markets for just zz/xx trades. This is also a supported conclusion in the general case derived in [3.1](https://arxiv.org/html/2510.06095v1#S3.SS1 "3.1 𝑧-Purchase ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.") considering the compound market’s path-independence, along with all the convexity requirements being met in the liquidity provider’s portfolio and trader’s basket value functions. In reality, however, so long as the yy market has it’s own structure and external liquidity markets, the macroeconomic behavior of the compound zz/xx market will never simplify to *just* a CFMM. Instead, it may be observed that liquidity will percolate in and out of the market through the yy asset.

### 4.2 zz-Liquidation

Next, the zz-Liquidation scenario. First we should note we are flipping the direction of everything. So for swap functions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(Γ)=y2−z​y2z+γ2​Γ=y2​γ2​Γz+γ2​Γ\displaystyle\Lambda(\Gamma)=y\_{2}-\frac{zy\_{2}}{z+\gamma\_{2}\Gamma}=\frac{y\_{2}\gamma\_{2}\Gamma}{z+\gamma\_{2}\Gamma} | Δ​(Λ)=x​γ1​Λy1+γ1​Λ\displaystyle\Delta(\Lambda)=\frac{x\gamma\_{1}\Lambda}{y\_{1}+\gamma\_{1}\Lambda} |  |

Which leaves the final xx received to be:

|  |  |  |
| --- | --- | --- |
|  | x​ received=Δ​(Λ​(Γ))=x​γ1​y2​γ2​Γy1​(z+γ2​Γ)+γ1​y2​γ2​Γx\text{ received}=\Delta(\Lambda(\Gamma))=\frac{x\gamma\_{1}y\_{2}\gamma\_{2}\Gamma}{y\_{1}({z+\gamma\_{2}\Gamma})+\gamma\_{1}y\_{2}\gamma\_{2}\Gamma} |  |

Start by formalizing the net value discrepancy, relative to price drift in yy on the zz/yy market, μy\mu\_{y},

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(μy)=−x​(γ1​y22​μy+1−γ1​y2​z)2y1​(z+γ2)​(y1​y2​μy+1+γ1​y22​μy+1−γ1​y2​z)v(\mu\_{y})=-\frac{x(\gamma\_{1}y\_{2}^{2}\sqrt{\mu\_{y}+1}-\gamma\_{1}y\_{2}z)^{2}}{y\_{1}(z+\gamma\_{2})(y\_{1}y\_{2}\sqrt{\mu\_{y}+1}+\gamma\_{1}y\_{2}^{2}\sqrt{\mu\_{y}+1}-\gamma\_{1}y\_{2}z)} |  | (18) |

Notice that for μy>0\mu\_{y}>0, v​(μy)<0v(\mu\_{y})<0 implying a deflation in the basket value relative to the decoupled scenario, just as observed in the general case with ([13](https://arxiv.org/html/2510.06095v1#S3.E13 "Equation 13 ‣ 3.2 𝑧-Liquidation ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")). For the provided reserves and fee parameters set at the beginning of the case study, this function can be seen in figure [4](https://arxiv.org/html/2510.06095v1#S4.F4 "Figure 4 ‣ 4.2 𝑧-Liquidation ‣ 4 Constant Product Market Maker Case Study ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.") below.

![Refer to caption](figures/vliq.png)


Figure 4: The basket value difference between the coupled and decoupled market scenarios on a zz-liquidation event.

Recall where this value deflation is going as well. In the decoupled scenario, it’s assumed the price of yy cannot be impacted; whereas in the coupled scenario, the second trade occurs on a regular CFMM. Both scenarios have the same trade outcome on the zz market, meaning the only place this deflation is going to is slippage on the yy/xx market, or its liquidity providers to be more precise. This is why the effect is less compounded (by a factor of roughly μy+1\sqrt{\mu\_{y}+1}) on liquidation rather than in purchases, given the fixed xx denomination. We highlight that this does not necessarily mean that there is an arbitrage opportunity here. Both markets are still robust - implying their compound is as well. In both scenarios, if one were to atomically perform the zz purchase and liquidation events to and from the xx asset, their net basket value would be roughly the same as their starting point, minus fees paid. The asymmetry in this value metric between both directions comes mainly from a difference in *what* it’s measuring rather than any inherent market asymmetry itself.

Next, the price drift transmission function.

|  |  |  |
| --- | --- | --- |
|  | μx​(μy)=(y1​z​μy+1+γ1​y2​z​μy+1−y2​z)2y12​z2​(μy+1)−1\mu\_{x}(\mu\_{y})=\frac{(y\_{1}z\sqrt{\mu\_{y}+1}+\gamma\_{1}y\_{2}z\sqrt{\mu\_{y}+1}-y\_{2}z)^{2}}{y\_{1}^{2}z^{2}(\mu\_{y}+1)}-1 |  |

This is the exact mirror of ([17](https://arxiv.org/html/2510.06095v1#S4.E17 "Equation 17 ‣ 4.1 𝑧-Purchase ‣ 4 Constant Product Market Maker Case Study ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")) in the opposite direction; same behavior and scaling with respect to the initial market’s price drift. This is more of an artifact of the symmetry of constant product curves, leading to very symmetrical compound behavior as well in either direction (particularly when unnormalized by a particular denomination).

Lastly, the marginal cost functional. Like before, in practice it will make more sense to work with the above derived quantities and ([15](https://arxiv.org/html/2510.06095v1#S3.E15 "Equation 15 ‣ 3.2 𝑧-Liquidation ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")) directly. A topographic plot of this ([15](https://arxiv.org/html/2510.06095v1#S3.E15 "Equation 15 ‣ 3.2 𝑧-Liquidation ‣ 3 Market Metrics ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.")) for the coupled CPMM case study, using the reserves and fees set at the beginning of the section, can be seen in figure [5](https://arxiv.org/html/2510.06095v1#S4.F5 "Figure 5 ‣ 4.2 𝑧-Liquidation ‣ 4 Constant Product Market Maker Case Study ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments.") below.

![Refer to caption](figures/mcostliq.png)


Figure 5: The marginal output amount, oliq​(δ​μy)o\_{\text{liq}}(\delta\mu\_{y}), for δ​μy\delta\mu\_{y} additional price drift on the zz-market.

Similar results as what we see in the purchase scenario, marginal output received is highest for small swap sizes with a gradual degradation in the marginal amount as the pool liquidity gets used. You’ll notice that the gradient is much more gradual in this direction relative to the purchase scenario. This is nothing more than an artifact of the liquidity imbalances in the pools. Recalling our set up, the yy/xx market holds most of the yy liquidity, and the xx token liquidity is in much lower *quantity* than the zz liquidity in its respective market, which in this scenario manifests in a more gradual degradation in the liquidation direction.

While the liquidation metrics appear to algebraically mirror the purchase metrics, the incidence of value transfer is reversed. In purchases, convexity favors the trader through basket inflation, whereas in liquidations the same convexity shifts value back toward LPs, manifesting as systematic basket deflation. As well, this isn’t so much a property of coupled markets as it is one of CFMMs themselves, only compounding in the coupling scenario to create a naturally leveraged derivative of this dynamic. Similarly, although price drift transmission follows the same structural form, the liquidity bottlenecks differ: deeper purchasable yy liquidity implies higher drift transmission, but whereas deeper yy liquidity in the final swap market implies a smoother gradient in the marginal cost and output amounts.

## 5 Macro Implications

Now that we have established the foundational equations, we will now briefly explore the direct implications of the market structure.

First, consider what happens when the yy/xx market is the oracle market for the yy asset. There is no restriction on the amount of markets that use that yy base asset. However, the oracle market is main route between yy and it’s derivatives with the numeraire. This means there is likely a large demand from non-toxic flow that will move through this route, as the price is correct more often than other markets [[1](https://arxiv.org/html/2510.06095v1#bib.bib1)]. As mentioned near the end of [4.2](https://arxiv.org/html/2510.06095v1#S4.SS2 "4.2 𝑧-Liquidation ‣ 4 Constant Product Market Maker Case Study ‣ A Microstructure Analysis of Coupling in CFMMsThe authors wish to thank Jacob Horne and Bridgett Frey for helpful comments."), if yy is not a fully internalized asset, then there will be some form of liquidity percolation from both xx and zz out of their respectively paired yy reserves, especially as the number of yy denominated markets expand. The optimal design for a yy-asset would mimic more of a currency than an asset. Both of these will push their local market prices of yy upwards, for use by the trader somewhere else they may find utility for yy. In the context where the yy/xx market is an oracle market, this percolation can only flow upward rather than grounding back to the numeraire, as a form of rebalancing effects.

This implies an internalization of the natural inflation introduced in the coupled market scenario, as no arbitrage can realistically be established to push the price of yy in opposition of any traders through the oracle market onto the derivative markets. The base oracle market only deflates all traders baskets through the trickle of traders aiming to capitalize on their profits, or from some macro pressure on traders to no longer remain within the yy derivative ecosystem as a whole. This internalization is why, in practice, this cannot be treated as simply inflation that immediately gets deflated out of the system by arbitrage; flows stay internal unless pressured to reverse. While a trader’s portfolio consists of yy derivative market assets, the portfolio will move with leveraged price action relative to the drift in the yy asset price, by a factor of (μy+1)(\mu\_{y}+1). It’s more the oracle market dependence naturally introduces leverage for the whole yy derivative ecosystem, which is not dissimilar to other currencies.

It is possible that a market participant, such as a trader or asset issuer, could see the inflation in the zz-market as a short-run opportunity to reset the price and capture additional value. This functions similarly to back-running arbitrage in traditional CFMM markets. However, as previously stated, this is not free as it requires users to take on significant price risk as the market exists in a fully liquid state of no-arbitrage (there is no-where to offload the risk). Additionally, because asset issuers are likely coupling assets with some type of informed price relationship, the belief in the correlation undoing itself would require some informed decision on the coupling changing or price movements. This functions similarly to outsourcing price risk via underwriting the loss with the value in the pool.

This coupling is not without downsides. It is more likely that internal leverage theoretically builds up in the system and then could potentially flushed swiftly during periods of financial malaise. This has been the focus of many financial papers specifically on financial crises (see Geanakoplos (2010) [[4](https://arxiv.org/html/2510.06095v1#bib.bib4)]). Leverage is rapidly flushed out of a system, because asset holders become forced sellers into illiquidity, resulting in a large amount of value loss.

However, we now stop to say that Geanakoplos is highlighting leverage in the 2008 financial crisis. Leverage in traditional financial institutions, such as GSIBs, grew to such a point that it was flushed. The argument here is rather that this risk being internalized is better due to less information asymmetry, more collectivization, and better internalization to believers in the system.

We argue that the key difference between the implied leverage in this system vs. others is how it is managed and by whom. In the coupled markets model, the markets themselves manage the leverage and the leverage is essentially programmatic. There is also less information asymmetry because all participants know the leverage in the system. Additionally, collectivization could enable more value demanders, perhaps many of which may not be able to access leverage. We argue that one of the large issues with leverage in traditional financial systems is that it is hidden. Every user is incentivized to leverage up as much as possible while also hiding it from other participants. This creates a similar effect to the tragedy of the commons where everyone is likely better off from not using leverage, but individual payoffs create a great incentive to deviate from the collective good strategy.

However, the cost of a leverage collapse is direct losses to users and should be avoided if possible. We argue that mechanics such as guaranteed liquidity, PID controllers, and slowing down the price evolution could programmatically limit the catastrophic effects of a forced deleverage event. On the other hand, this could increase the amount of moral hazard in the system [[3](https://arxiv.org/html/2510.06095v1#bib.bib3)].

Because the leverage is programmatic and a direct result of the chosen curvature, it could be adapted over time in response to market events. We envision that this will be how issuance protocols and market participants adapt to this new technology.

### 5.1 Coupled Content Market Implications

While the market described in this note applies to a lot of situations, one especially prominent case is in content markets such as with [Zora Protocol](https://zora.co/), the largest user of Doppler as an issuance protocol. Creators themselves have their own assets, which in this case is yy, where their primary market is denominated in the $zora token, our xx. Further, creators make content that has its own fungible asset, the zz asset here, traded against the creator’s asset. This is exactly the coupling we modeled above for the purchases and sales of the content asset from a user’s basket of $zora tokens.

This coupling effect is used in content markets to quite literally couple the price paths of the assets together, creating a price relationship between two assets. This allows the creator’s coin to function as partly a market of a basket of derivatives of their underlying content, coupling the asset prices together. Additionally, the content itself gains an economic relationship with the creator, allowing for content to potentially gain in value due to the derivative asset it functionally holds from the creator.

We argue that this is a valuable relationship as it enables unique long-term pricing relationships. Additionally, this effect is only possible because of the implicit price correlation. With no price correlation, there zz-market would be compressed to extract the added leverage. In reality, we argue that this coupling effect likely does impact larger assets, as there exists no infinite depth market. Token issuance has effectively locked up billions of dollars worth of assets to date. While it is impossible to say for certain, it has likely had enormous compounding effects on assets such as ETH and SOL, which are widely used as the liquid asset for token projects.

This relationship is programmatic and adjustable, allowing more or less price impact to be accrued as desired. Importantly, this price impact is not equal in both directions as the implied leverage effect is based on the depth of the y−y- and z−z-markets. The deeper the market, the less effect on the asset’s price. This phenomenon of asset coupling, as demonstrated by empirical results from Zora’s content markets, testifies to the price coupling of these paired assets and the programmability enabled by issuance protocols like Doppler.

### 5.2 Future Directions

The above framework can be extended in a few ways to study the behavior of these markets further. The above only models the microstructure behavior of a single atomic swap sequence. Analyzing price discovery behavior more quantitatively will require a time series in the state space we can model with 𝐅\mathbf{F}, 𝐅l\mathbf{F}\_{l}, and the single pool swap transition functions. Further, it may merit a simple multi-agent simulation of this discovery process if the stochastic processes that arises becomes too burdensome to approach analytically.

Beyond this another simple extension, as seen by both the unnormalized marginal cost and value discrepancy functionals in the CPMM case study, we can directly observe the exact dependencies each variable has on each term as well as the final outcome. This suggest that, given some exotic CFMM with parameterizations other than just the fee, so:

|  |  |  |
| --- | --- | --- |
|  | φ​(𝐑,α0,α1,α2,⋯)=k​ ⟶ ​Λ​(Δ)=Λ​(Δ,α0,α1,α2,⋯)\displaystyle\varphi(\mathbf{R},\alpha\_{0},\alpha\_{1},\alpha\_{2},\cdots)=k\text{ }\longrightarrow\text{ }\Lambda(\Delta)=\Lambda(\Delta,\alpha\_{0},\alpha\_{1},\alpha\_{2},\cdots) |  |

We could further derive and study the behaviors of these cost functionals over parameter space instead of reserve state. This would allow a preliminary framework to studying optimal parameterizations analytically, although given the complexity that arises from simple CPMM coupled markets, indicates this would likely require numerical methods.

While there are an immense amount of learnings from this model, understanding both the short and long-term springback effect will require expanding the model past a single swap.

## 6 Conclusion

While price coupling exists in traditional financial structures (this is essentially the definition of beta), the ability to do programmatic coupling at an asset level is novel. Issuance protocols such Doppler Protocol have enabled programmatic issuance. This new market structure enables a wider economic link through guaranteed liquidity and standardization via automated market makers. In short, both finding a liquid venue for an asset and running an auction both are incredible undertaking, thus the benefit of novel asset couplings has been outpaced by their cost. Programmatic markets help lessen the burden on all parties through standardization and programming.

Although there are added risks with coupling, we argue that a deeper understanding and adaptation of solutions from traditional financial markets will allow iterating to counteract the deleterious effects. With more analysis and more experimentation, market participants will slowly converge to better market structures and enable unique asset relationships that are totally novel.

## References

* [1]

  Austin Adams, Ciamac C. Moallemi, Sara Reynolds, and Dan Robinson.
  am-amm: An auction-managed automated market maker, 2025.
* [2]

  Guillermo Angeris, Akshay Agrawal, Alex Evans, Tarun Chitra, and Stephen Boyd.
  Constant function market makers: Multi-asset trades via convex optimization.
  arXiv preprint, 2021.
* [3]

  Anna Cieslak and Annette Vissing-Jorgensen.
  The economics of the fed put.
  The Review of Financial Studies, 34(9):4045–4089, 2021.
* [4]

  John Geanakoplos.
  The leverage cycle.
  NBER macroeconomics annual, 24(1):1–66, 2010.
* [5]

  Alfred Lehar and Christine Parlour.
  Decentralized exchange: The uniswap automated market maker.
  The Journal of Finance, 80(1):321–374, 2025.
* [6]

  Jason Milionis, Ciamac C. Moallemi, and Tim Roughgarden.
  Automated market making and arbitrage profits in the presence of fees, 2025.
* [7]

  Jason Milionis, Ciamac C. Moallemi, Tim Roughgarden, and Anthony Lee Zhang.
  Automated market making and loss-versus-rebalancing, 2024.

## Notation

|  |  |  |  |
| --- | --- | --- | --- |
|  | x,y,z\displaystyle x,y,z | Three assets forming the coupled market, where yy/xx and zz/yy are the trading pairs. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | R=(x,y)\displaystyle R=(x,y) | Reserve state of an yy/xx liquidity pool. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(R)=k\displaystyle\phi(R)=k | Constant function market maker invariant. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ,Λ,Γ\displaystyle\Delta,\Lambda,\Gamma | Amount of xx, yy, and zz assets involved in a swap context respectively, (input or output). |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | γ∈(0,1]\displaystyle\gamma\in\left(0,1\right] | Discount factor for the pool, γ=1−pool fee\gamma=1-\text{pool fee}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Px​(R),Py​(R)\displaystyle P\_{x}(R),P\_{y}(R) | Spot price of the pool denominated in base asset xx or yy. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μy​(Δ)\displaystyle\mu\_{y}(\Delta) | Relative price drift: μy=Py′−PyPy\mu\_{y}=\frac{P^{\prime}\_{y}-P\_{y}}{P\_{y}}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Dmarg,y​(μy)\displaystyle D\_{\text{marg},y}(\mu\_{y}) | Marginal swap depth, measuring liquidity absorption rate. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(μy)\displaystyle v(\mu\_{y}) | Value discrepancy between coupled and decoupled scenarios. |  |