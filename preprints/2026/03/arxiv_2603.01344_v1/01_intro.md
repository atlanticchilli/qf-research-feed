---
authors:
- Jimmy Risk
- Shen-Ning Tung
- Tai-Ho Wang
doc_id: arxiv:2603.01344v1
family_id: arxiv:2603.01344
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Pricing and hedging for liquidity provision in Constant Function Market Making
url_abs: http://arxiv.org/abs/2603.01344v1
url_html: https://arxiv.org/html/2603.01344v1
venue: arXiv q-fin
version: 1
year: 2026
---


Jimmy Risk
, 
Shen-Ning Tung
 and 
Tai-Ho Wang
Jimmy Risk
  
Department of Mathematics and Statistics,
  
Cal Poly Pomona
  
3801 W Temple Ave, Pomona CA 91768
[jrisk@cpp.edu](2603.01344v1/mailto:jrisk@cpp.edu)
Shen-Ning Tung
  
Department of Mathematics,
  
National Tsing Hua University
  
Hsinchu, Taiwan
[tung@math.nthu.edu.tw](2603.01344v1/mailto:tung@math.nthu.edu.tw)
Tai-Ho Wang
  
Department of Mathematics
  
Baruch College, The City University of New York
  
1 Bernard Baruch Way, New York, NY10010
[tai-ho.wang@baruch.cuny.edu](2603.01344v1/mailto:tai-ho.wang@baruch.cuny.edu)

###### Abstract.

This paper develops a robust mathematical framework for Constant Function Market Makers (CFMMs) by transitioning from traditional token reserve analyses to a coordinate system defined by price and intrinsic liquidity. We establish a canonical parametrization of the bonding curve that ensures dimensional consistency across diverse trading functions, such as those employed by Uniswap and Balancer, and demonstrate that asset reserves and value functions exhibit a linear dependence on this intrinsic liquidity. This linear structure facilitates a streamlined approach to arbitrage-free pricing, delta hedging, and systematic risk management. By leveraging the Carr-Madan spanning formula, we characterize Impermanent Loss (IL) as a weighted strip of vanilla options, thereby defining a fine-grained implied volatility structure for liquidity profiles. Furthermore, we provide a path-dependent analysis of IL using the last-passage time. Empirical results from Uniswap v3 ETH/USDC pools and Deribit option markets confirm a volatility smile consistent with crypto-asset dynamics, validating the framework’s utility in characterizing the risk-neutral fair value of liquidity provision.

###### Key words and phrases:

Automatic market making, Decentralized exchange, Decentralized finance

It all begins with the canonical parametrization of the bonding curve in CFMM.

## 1. Introduction

The emergence of Decentralized Finance (DeFi) [harvey2021defi, gobet2023decentralized, capponi2021adoption] has revolutionized asset exchange through the implementation of Constant Function Market Makers (CFMMs) [angeris2020improved, angeris2024geometry]. Unlike traditional limit order books that rely on discrete orders, protocols such as Uniswap [adams2020uniswapv2, adams2021uniswapv3, adams2023uniswapv4] and Balancer [martinelli2019balancer] utilize a deterministic bonding curve to govern the relationship between token reserves and exchange rates. This mechanism ensures that liquidity remains available across a continuous price spectrum, contingent on the slippage costs defined by the underlying trading function.

Within this ecosystem, the role of the Liquidity Provider (LP) has undergone a profound transformation. By depositing assets into a smart contract, LPs effectively sell tokens to the market according to a pre-defined rule [angeris2023replicating]. Consequently, an LP position can be mathematically framed as a sophisticated financial derivative. The growing academic and industrial recognition of this equivalence is highlighted by protocols such as Panoptic [lambert2022panoptic], which utilize Uniswap v3 liquidity positions as the underlying engine for perpetual options.

As the complexity of these automated strategies increases, research has shifted toward the optimal design of bonding curves. While early automated market makers (AMMs) relied on simple invariants, the current landscape demands capital-efficient structures that reflect specific financial payoffs. Determining an “optimal” curve requires a rigorous understanding of how liquidity profiles interact with market volatility and informed order flow.

### Literature Review

#### LP Positions as Synthetic Derivatives

A foundational branch of literature characterizes the payoff structures of LPs as equivalent to traditional derivatives. Early work replicated Uniswap v2 payoffs with portfolios of options, a framework subsequently extended to the concentrated liquidity models of Uniswap v3 [clark2020replicating, clark2021replicating]. This equivalence was formalized by Angeris et al. [angeris2023replicating], who characterized the space of feasible CFMM payoffs in terms of the properties of the trading function. Within this lens, Impermanent Loss (IL) is increasingly viewed as a hedgeable risk; notably, Fukasawa et al. [fukasawa2023weighted] demonstrate that IL in constant product markets can be perfectly hedged using a weighted variance swap of order 1/21/2. More practical hedging strategies involve standard put and call options to mitigate the idiosyncratic risks of concentrated liquidity positions [lipton2025unified].

#### Pricing, Hedging, and Implied Volatility

As LP positions are recognized as derivatives, the question of their “fair value” arises. Recent works establish a rigorous framework for the arbitrage-free pricing of liquidity tokens [bichuch2025arbitrage, bichuch2025price]. By defining an implied volatility metric derived from transaction-fee streams, this research enables LPs to quantify the “price of liquidity” in a manner consistent with the Black–Scholes paradigm, bridging the gap between endogenous fee generation and exogenous asset volatility.

#### Dynamic Modeling and Parameterization

To move beyond static payoffs, recent studies model the temporal evolution of liquidity. The framework introduced in [tung2024mathematical] provides a canonical parameterization of CFMMs through a “liquidity profile,” offering a unified mathematical language for various bonding curves. Building on this, [risk2025dynamics] models the stochastic dynamics of these profiles to capture shifts in response to market behavior. These models are essential for analyzing the “Loss-Versus-Rebalancing” (LVR) metric, which [singh2025modeling] presents as a continuous-installment option to price the ongoing costs of providing liquidity against informed arbitrageurs.

#### Strategic and Optimal Liquidity Provision

Finally, a growing body of work focuses on LPs’ strategic behavior. Using an optimal stopping approach, Capponi and Zhu [capponi2025optimal] demonstrate the existence of strategies that remain profitable relative to “buy-and-hold” benchmarks, even after accounting for LVR [capponi2025optimal]. This suggests that the “natural coordinates” for AMM analysis are price and intrinsic liquidity, which together dictate the optimal design of the bonding function.

### Contribution

This paper reviews and extends the market model framework proposed in [tung2024mathematical]. By shifting the perspective from token reserves to a coordinate system defined by price and liquidity, the framework achieves several key objectives:

1. (1)

   It defines an intrinsic liquidity that maintains dimensional consistency (ETH×USDC\sqrt{{\rm ETH}\times{\rm USDC}}) across all CFMM bonding functions, providing a universal metric for market depth.
2. (2)

   It demonstrates that relevant financial quantities, including asset reserves and value functions, are encoded in the linear dependence of the model on the intrinsic liquidity profile.
3. (3)

   It simplifies complex tasks such as arbitrage-free pricing, delta hedging, and systematic risk management by exploiting this linear structure.
4. (4)

   It unifies diverse results from existing literature—ranging from constant product formulas to concentrated liquidity—into a single, concise representation.
5. (5)

   It enables the evaluation of liquidity profiles through fine-structure implied volatility and path-dependent last-passage time analysis, allowing for a granular assessment of market-implied risk.

We argue that the price-intrinsic liquidity pair is the natural coordinate system for the pricing and hedging of bonding functions. In the following sections, we detail the mathematical derivation of this framework and demonstrate its application to several canonical AMM structures.

## 2. Intrinsic Liquidity and Liquidity Profile

In the study of Constant Function Market Makers (CFMMs) [angeris2020improved, angeris2024geometry], the system is typically characterized by a bonding function ff and its associated level set f​(x,y)=Kf(x,y)=K, often termed the bonding curve. Conventionally, the level KK is interpreted as the “liquidity depth.” We argue, however, that this definition is dimensionally inconsistent across different CFMM architectures. To resolve this, we propose an intrinsic definition of liquidity that is invariant under reparametrization and maintains dimensional consistency across all CFMM models. While aspects of this discussion appear in [tung2024mathematical], we provide the key arguments here for completeness.

### 2.1. Dimensionally Consistent Liquidity

Consider the Constant Product Market Maker (CPMM) [adams2020uniswapv2] for a pair of tokens, e.g., ETH and USDC. The bonding curve is defined by the level set x​y=K\sqrt{xy}=K, where the parameter KK possesses the physical dimension ETH×USDC\sqrt{\mathrm{ETH}\times\mathrm{USDC}}. In contrast, for Geometric Mean Market Makers (G3Ms) [martinelli2019balancer], the bonding curve is given by xα​y1−α=Kx^{\alpha}y^{1-\alpha}=K for some weight α∈(0,1)\alpha\in(0,1). For this model, KK carries the dimension ETHα×USDC1−α\mathrm{ETH}^{\alpha}\times\mathrm{USDC}^{1-\alpha}.

This dimensional disparity implies that the parameter KK is not a consistent proxy for market depth across protocols; specifically, the same numerical value of KK represents different physical quantities depending on the exponent α\alpha. To resolve this, we utilize the framework established in [tung2024mathematical, Appendix B] to define a local intrinsic liquidity ℓ\ell that is both dimensionally consistent and invariant under reparametrization. For a smooth bonding curve f​(x,y)=Kf(x,y)=K, we define ℓ\ell at the reserve state (x,y)(x,y) as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ:=−2​(fx​fy)3/2fy​y​fx2−2​fx​y​fx​fy+fx​x​fy2,\ell:=\frac{-2(f\_{x}f\_{y})^{3/2}}{f\_{yy}f\_{x}^{2}-2f\_{xy}f\_{x}f\_{y}+f\_{xx}f\_{y}^{2}}, |  | (1) |

where subindices denote partial derivatives.

The definition in ([1](#S2.E1 "In 2.1. Dimensionally Consistent Liquidity ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) ensures that ℓ\ell always yields the dimension ETH×USDC\sqrt{\mathrm{ETH}\times\mathrm{USDC}}, matching the CPMM standard regardless of the functional form of ff. Mathematically, this definition is related to the curvature of the bonding curve in the (x,y)(x,y) plane. We emphasize two critical properties of ℓ\ell:

* •

  Locality: Unlike the global constant KK, ℓ\ell is a state-dependent quantity ℓ​(x,y)\ell(x,y) that characterizes the immediate price impact at a specific reserve point.
* •

  Invariance: The definition is intrinsic to the geometry of the curve f​(x,y)=Kf(x,y)=K, meaning it is independent of the choice of functional representation (e.g., x​y=K2xy=K^{2} versus x​y=K\sqrt{xy}=K).

###### Example 2.1 (G3M Liquidity).

For the G3M f​(x,y)=xα​y1−α=Kf(x,y)=x^{\alpha}y^{1-\alpha}=K, the intrinsic liquidity is computed as:

|  |  |  |
| --- | --- | --- |
|  | ℓ=2​α​(1−α)​x​y=2​α​(1−α)​K​x12−α​yα−12.\ell=2\sqrt{\alpha(1-\alpha)}\sqrt{xy}=2\sqrt{\alpha(1-\alpha)}K\,x^{\frac{1}{2}-\alpha}y^{\alpha-\frac{1}{2}}. |  |

This expression explicitly restores the ETH×USDC\sqrt{\mathrm{ETH}\times\mathrm{USDC}} dimension. In the specific case of the CPMM (α=12\alpha=\frac{1}{2}), the local intrinsic liquidity simplifies to ℓ=x​y=K\ell=\sqrt{xy}=K. Thus, for a CPMM, the liquidity profile is uniform across all price points, and the intrinsic liquidity coincides with the traditional depth parameter.

### 2.2. Liquidity Profile and Reserves

In the study of CFMMs, the spot price pp is endogenously determined by the pool’s current reserve state (x,y)(x,y). By adopting token YY as the numéraire, the spot price is defined as the marginal rate of substitution:

|  |  |  |
| --- | --- | --- |
|  | p:=−d​yd​x=fxfy.p:=-\frac{dy}{dx}=\frac{f\_{x}}{f\_{y}}. |  |

This value represents the unit price of token XX required for an infinitesimal swap d​xdx. While conventional models define reserves xx and yy as primary variables, we demonstrate that the bonding curve f​(x,y)=Kf(x,y)=K admits a more fundamental representation via the spot price pp and the local intrinsic liquidity ℓ\ell. This leads to what we term the canonical parametrization of the bonding curve.

###### Theorem 2.2 (Canonical Parametrization).

Let the bonding function f​(x,y)f(x,y) be smooth, strictly increasing, and convex in (x,y)(x,y). For the CFMM f​(x,y)=Kf(x,y)=K, the reserve levels (x,y)(x,y) are uniquely determined by the spot price pp and the local intrinsic liquidity ℓ\ell via the following integral representations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x​(p)=∫p∞ℓ​(q)2​q3​𝑑q,y​(p)=∫0pℓ​(q)2​q​𝑑q,x(p)=\int\_{p}^{\infty}\frac{\ell(q)}{2\sqrt{q^{3}}}\,dq,\qquad y(p)=\int\_{0}^{p}\frac{\ell(q)}{2\sqrt{q}}\,dq, |  | (2) |

where ℓ​(q)\ell(q) is the intrinsic liquidity at price qq defined in ([1](#S2.E1 "In 2.1. Dimensionally Consistent Liquidity ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")).

###### Proof.

Consider an arbitrary parametrization (x​(s),y​(s))(x(s),y(s)) of the level curve f​(x,y)=Kf(x,y)=K with x˙<0\dot{x}<0 and y˙>0\dot{y}>0. Implicit differentiation yields fx​x˙+fy​y˙=0f\_{x}\dot{x}+f\_{y}\dot{y}=0, implying p=−y˙/x˙p=-\dot{y}/\dot{x}. By differentiating pp with respect to the parameter ss, we have:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​pd​s\displaystyle\frac{dp}{ds} | =\displaystyle= | −dd​s​(y˙x˙)=−y¨​x˙+x¨​y˙x˙2\displaystyle-\frac{d}{ds}\left(\frac{\dot{y}}{\dot{x}}\right)=\frac{-\ddot{y}\dot{x}+\ddot{x}\dot{y}}{\dot{x}^{2}} |  |
|  |  | =\displaystyle= | dd​s​(fxfy)=−y˙fx​fy2​(fx​x​fy2−2​fx​y​fx​fy+fy​y​fx2).\displaystyle\frac{d}{ds}\left(\frac{f\_{x}}{f\_{y}}\right)=-\frac{\dot{y}}{f\_{x}f\_{y}^{2}}(f\_{xx}f\_{y}^{2}-2f\_{xy}f\_{x}f\_{y}+f\_{yy}f\_{x}^{2}). |  |

Utilizing the definition of ℓ\ell in ([1](#S2.E1 "In 2.1. Dimensionally Consistent Liquidity ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) and changing the variable of integration from ss to pp, we obtain:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℓ\displaystyle\ell | =\displaystyle= | −2​(fx​fy)3/2fy​y​fx2−2​fx​y​fx​fy+fx​x​fy2=2​(−x˙​y˙)3/2y¨​x˙−x¨​y˙,\displaystyle\frac{-2(f\_{x}f\_{y})^{3/2}}{f\_{yy}f\_{x}^{2}-2f\_{xy}f\_{x}f\_{y}+f\_{xx}f\_{y}^{2}}=2\,\frac{(-\dot{x}\dot{y})^{3/2}}{\ddot{y}\dot{x}-\ddot{x}\dot{y}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​xd​p\displaystyle\frac{dx}{dp} | =\displaystyle= | x˙​d​sd​p=−x˙3y¨​x˙−x¨​y˙=−12​2​(−x˙​y˙)3/2y¨​x˙−x¨​y˙​(−x˙y˙)3/2=−ℓ2​p3/2,\displaystyle\dot{x}\frac{ds}{dp}=-\frac{\dot{x}^{3}}{\ddot{y}\dot{x}-\ddot{x}\dot{y}}=-\frac{1}{2}\frac{2(-\dot{x}\dot{y})^{3/2}}{\ddot{y}\dot{x}-\ddot{x}\dot{y}}\left(-\frac{\dot{x}}{\dot{y}}\right)^{3/2}=-\frac{\ell}{2p^{3/2}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​yd​p\displaystyle\frac{dy}{dp} | =\displaystyle= | y˙​d​sd​p=−x˙2​y˙y¨​x˙−x¨​y˙=12​2​(−x˙​y˙)3/2y¨​x˙−x¨​y˙​−x˙y˙=ℓ2​p.\displaystyle\dot{y}\frac{ds}{dp}=-\frac{\dot{x}^{2}\dot{y}}{\ddot{y}\dot{x}-\ddot{x}\dot{y}}=\frac{1}{2}\frac{2(-\dot{x}\dot{y})^{3/2}}{\ddot{y}\dot{x}-\ddot{x}\dot{y}}\sqrt{-\frac{\dot{x}}{\dot{y}}}=\frac{\ell}{2\sqrt{p}}. |  |

Integrating these expressions with respect to pp from the respective boundaries (p→∞p\to\infty for xx and p→0p\to 0 for yy) completes the proof.
∎

The relationship in Theorem [2.2](#S2.Thmtheorem2 "Theorem 2.2 (Canonical Parametrization). ‣ 2.2. Liquidity Profile and Reserves ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making") allows us to define the local intrinsic liquidity profile as a distribution function ℓ​(p)\ell(p) over the price spectrum (0,∞)(0,\infty). For the purpose of financial modeling, it is often more convenient to work with the liquidity profile L​(q)L(q), defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(q):=ℓ​(q)2​q3/2.L(q):=\frac{\ell(q)}{2q^{3/2}}. |  | (3) |

Substituting L​(q)L(q) into ([2](#S2.E2 "In Theorem 2.2 (Canonical Parametrization). ‣ 2.2. Liquidity Profile and Reserves ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) yields a succinct representation of the pool reserves:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x​(p)=∫p∞ℓ​(q)2​q3​𝑑q=∫p∞L​(q)​𝑑q,y​(p)=∫0pℓ​(q)2​q​𝑑q=∫0pq​L​(q)​𝑑q.\displaystyle x(p)=\int\_{p}^{\infty}\frac{\ell(q)}{2\sqrt{q^{3}}}dq=\int\_{p}^{\infty}L(q)dq,\quad y(p)=\int\_{0}^{p}\frac{\ell(q)}{2\sqrt{q}}dq=\int\_{0}^{p}qL(q)dq. |  | (4) |

The dimensional consistency is preserved: L​(q)​d​qL(q)dq carries the dimension of token XX, while q​L​(q)​d​qqL(q)dq carries the dimension of token YY. This formulation highlights the infinitesimal price impact of a trade volume d​xdx:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​p=−1L​(p)​d​x.dp=-\frac{1}{L(p)}dx. |  | (5) |

This identity confirms the economic intuition that higher liquidity density L​(p)L(p) suppresses slippage, as a larger L​(p)L(p) results in a smaller price adjustment d​pdp for any given volume d​xdx.

### 2.3. Liquidity Profile Value and Option Replication

For a given liquidity profile LL, we define its mark-to-market value VL​(p)V\_{L}(p) as a function of the spot price pp. Taking token YY as the numéraire, the value is defined by the sum of the value of its constituent token holdings:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VL​(p)\displaystyle V\_{L}(p) | =x​(p)​p+y​(p)\displaystyle=x(p)p+y(p) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞p​𝟙[p,∞)​(q)​L​(q)​𝑑q+∫0∞q​𝟙[0,p]​(q)​L​(q)​𝑑q\displaystyle=\int\_{0}^{\infty}p\mathbbm{1}\_{[p,\infty)}(q)L(q)dq+\int\_{0}^{\infty}q\mathbbm{1}\_{[0,p]}(q)L(q)dq |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0∞min⁡{p,q}​L​(q)​𝑑q,\displaystyle=\int\_{0}^{\infty}\min\{p,q\}L(q)dq, |  | (6) |

where 𝟙A​(⋅)\mathbbm{1}\_{A}(\cdot) denotes the indicator function for the interval AA. The representation in ([6](#S2.E6 "In 2.3. Liquidity Profile Value and Option Replication ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) provides a direct financial interpretation: since min⁡{p,q}=p−(p−q)+\min\{p,q\}=p-(p-q)^{+} corresponds to the payoff of a covered call struck at qq, the total pool value VLV\_{L} is equivalent to the payoff of a strip of weighted covered calls. The weights of this portfolio are determined entirely by the liquidity profile L​(q)L(q).

A more fundamental decomposition is achieved by applying the spanning formula of Carr and Madan [carr2001towards], which enables the representation of any twice-differentiable payoff φ​(S)\varphi(S) via a portfolio of OTM options:

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(S)=φ​(S0)+φ′​(S0)​(S−S0)+∫0S0φ′′​(K)​(K−S)+​𝑑K+∫S0∞φ′′​(K)​(S−K)+​𝑑K.\varphi(S)=\varphi(S\_{0})+\varphi^{\prime}(S\_{0})(S-S\_{0})+\int\_{0}^{S\_{0}}\varphi^{\prime\prime}(K)(K-S)^{+}\,dK+\int\_{S\_{0}}^{\infty}\varphi^{\prime\prime}(K)(S-K)^{+}\,dK. |  | (7) |

By noting that VL′​(p)=x​(p)V\_{L}^{\prime}(p)=x(p) and VL′′​(p)=x′​(p)=−L​(p)V\_{L}^{\prime\prime}(p)=x^{\prime}(p)=-L(p), we apply this decomposition to the value function VLV\_{L}. Substituting these derivatives into ([7](#S2.E7 "In 2.3. Liquidity Profile Value and Option Replication ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) yields:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | VL​(p)\displaystyle V\_{L}(p) | =\displaystyle= | VL​(p0)+VL′​(p0)​(p−p0)+∫0p0VL′′​(q)​(q−p)+​𝑑q+∫p0∞VL′′​(q)​(p−q)+​𝑑q\displaystyle V\_{L}(p\_{0})+V\_{L}^{\prime}(p\_{0})(p-p\_{0})+\int\_{0}^{p\_{0}}V\_{L}^{\prime\prime}(q)(q-p)^{+}dq+\int\_{p\_{0}}^{\infty}V\_{L}^{\prime\prime}(q)(p-q)^{+}dq |  | (8) |
|  |  | =\displaystyle= | x​(p0)​p+y​(p0)−∫0p0L​(q)​(q−P)+​𝑑q−∫p0∞L​(q)​(p−q)+​𝑑q.\displaystyle x(p\_{0})p+y(p\_{0})-\int\_{0}^{p\_{0}}L(q)(q-P)^{+}dq-\int\_{p\_{0}}^{\infty}L(q)(p-q)^{+}dq. |  |

The identity in ([8](#S2.E8 "In 2.3. Liquidity Profile Value and Option Replication ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) demonstrates that the liquidity provider’s position is equivalent to a linear combination of the initial holding value and a short position in a continuously weighted strip of out-of-the-money (OTM) put options (for q∈[0,p0]q\in[0,p\_{0}]) and OTM call options (for q∈[p0,∞)q\in[p\_{0},\infty)). This equivalence is central to the pricing and hedging strategies developed in subsequent sections. In a complete market, ([8](#S2.E8 "In 2.3. Liquidity Profile Value and Option Replication ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) implies that the value VLV\_{L} can be perfectly replicated by a self-financing trading strategy involving the underlying assets and vanilla options.

### 2.4. Replicating Market Makers

In [angeris2023replicating], it is established that every CFMM possesses a concave, nonnegative, and 1-homogeneous payoff function, and conversely, any payoff function satisfying these properties has a corresponding convex CFMM. We demonstrate in this section that the canonical relationships established in ([4](#S2.E4 "In 2.2. Liquidity Profile and Reserves ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) provide a straightforward, alternative approach for constructing a CFMM trading function for any given target portfolio value V​(p)V(p).

Assume a liquidity provider (LP) wishes to replicate a target portfolio value V​(p):=p​x​(p)+y​(p)V(p):=px(p)+y(p) by designing an appropriate CFMM. Recall from the canonical parametrization that x​(p)=V′​(p)x(p)=V^{\prime}(p). By inverting this relationship, we obtain the spot price as a function of reserves: p=(V′)−1​(x)p=(V^{\prime})^{-1}(x). Furthermore, since the liquidity profile is given by L​(p)=−V′′​(p)L(p)=-V^{\prime\prime}(p), we can derive the CFMM trading function by integrating the reserve relationship for yy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y+∫0(V′)−1​(x)q​V′′​(q)​𝑑q=0.y+\int\_{0}^{(V^{\prime})^{-1}(x)}qV^{\prime\prime}(q)\,dq=0. |  | (9) |

We illustrate this procedure with two canonical examples from the literature.

###### Example 2.3 (Payoff of a Covered Call at Expiry).

Consider an LP whose target portfolio value is the payoff of a covered call struck at KK at expiry:

|  |  |  |
| --- | --- | --- |
|  | V​(p)=p−(p−K)+.V(p)=p-(p-K)^{+}. |  |

The corresponding liquidity profile is a Dirac delta function: L​(p)=−V′′​(p)=δ​(p−K)L(p)=-V^{\prime\prime}(p)=\delta(p-K). Applying the canonical parametrization yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x​(p)\displaystyle x(p) | =∫p∞δ​(q−K)​𝑑q=θ​(K−p),\displaystyle=\int\_{p}^{\infty}\delta(q-K)\,dq=\theta(K-p), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y​(p)\displaystyle y(p) | =∫0pq​δ​(q−K)​𝑑q=K​θ​(p−K),\displaystyle=\int\_{0}^{p}q\,\delta(q-K)\,dq=K\theta(p-K), |  |

where θ\theta denotes the Heaviside step function. Using the identity 1−θ​(K−p)=θ​(p−K)1-\theta(K-p)=\theta(p-K), we recover the linear trading function:

|  |  |  |
| --- | --- | --- |
|  | K​x+y=K,Kx+y=K, |  |

consistent with the results in [angeris2023replicating].

###### Example 2.4 (Black–Scholes Covered Call).

Assume the target portfolio value is the price of a covered call under Black–Scholes dynamics:

|  |  |  |
| --- | --- | --- |
|  | V​(p)=p−p​N​(d1)+K​N​(d2),V(p)=p-pN(d\_{1})+KN(d\_{2}), |  |

where d1=ln⁡(p/K)v+v2d\_{1}=\frac{\ln(p/K)}{v}+\frac{v}{2} and d2=d1−vd\_{2}=d\_{1}-v. Since x=V′​(p)=1−N​(d1)x=V^{\prime}(p)=1-N(d\_{1}), we find the price as a function of the xx reserve: p=K​ev​N−1​(1−x)−v2/2p=Ke^{vN^{-1}(1-x)-v^{2}/2}. Given that L​(p)=−V′′​(p)=Γ​(p)L(p)=-V^{\prime\prime}(p)=\Gamma(p) (the Black–Scholes Gamma), the yy reserve is obtained via:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y\displaystyle y | =\displaystyle= | ∫0pq​L​(q)​𝑑q=∫0K​ev​N−1​(1−x)−v22q​Γ​(q)​𝑑q=K​N​(N−1​(1−x)−v),\displaystyle\int\_{0}^{p}qL(q)dq=\int\_{0}^{Ke^{vN^{-1}(1-x)-\frac{v^{2}}{2}}}q\,\Gamma(q)dq=KN\left(N^{-1}(1-x)-v\right), |  |

This can be expressed in the symmetric form:

|  |  |  |
| --- | --- | --- |
|  | N−1​(1−x)−N−1​(y/K)=v,N^{-1}(1-x)-N^{-1}(y/K)=v, |  |

recovering the replicating market maker results for perpetual options in [angeris2023replicating].

## 3. Pricing and Hedging for General Liquidity Profiles

In this section, we establish that liquidity provision within a CFMM pool is mathematically equivalent to maintaining a short position in a contingent claim characterized by a convex payoff. Leveraging the canonical parametrization developed in ([4](#S2.E4 "In 2.2. Liquidity Profile and Reserves ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")), we quantify the risk inherent to the liquidity provider (LP) and derive the associated risk-neutral pricing and hedging frameworks by exploiting the spanning formula introduced in ([8](#S2.E8 "In 2.3. Liquidity Profile Value and Option Replication ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")).

### 3.1. Static Replication of Impermanent Loss by Vanilla Options

The primary risk for an LP in a CFMM is quantified as impermanent loss (IL), also referred to as divergence loss. Defined as the opportunity cost of providing liquidity relative to a simple buy-and-hold strategy of the underlying assets, IL can be expressed as a weighted sum of payoffs from a continuous strip of vanilla options.

Let p0p\_{0} denote the current pool price and pTp\_{T} the future price at time TT. Utilizing the expression for the value function VL​(pT)V\_{L}(p\_{T}) from ([8](#S2.E8 "In 2.3. Liquidity Profile Value and Option Replication ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")), the IL at time TT is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IL​(pT|p0,L)\displaystyle{\rm IL}(p\_{T}|p\_{0},L) | :=x​(p0)​pT+y​(p0)−VL​(pT)\displaystyle:=x(p\_{0})p\_{T}+y(p\_{0})-V\_{L}(p\_{T}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0p0L​(q)​(q−pT)+​𝑑q+∫p0∞L​(q)​(pT−q)+​𝑑q.\displaystyle=\int\_{0}^{p\_{0}}L(q)(q-p\_{T})^{+}dq+\int\_{p\_{0}}^{\infty}L(q)(p\_{T}-q)^{+}dq. |  | (10) |

This representation highlights the linearity of IL with respect to the liquidity profile LL and its universal applicability across diverse bonding functions. The formula can be simplified to a more concise integral form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IL​(pT|p0,L)=∫p0pT(pT−q)​L​(q)​𝑑q,{\rm IL}(p\_{T}|p\_{0},L)=\int\_{p\_{0}}^{p\_{T}}(p\_{T}-q)L(q)dq, |  | (11) |

which underscores that IL is essentially the cost of the option embedded in the LP’s position rather than a mere metric of pool stability.

This replication framework unifies several disparate expressions found in the literature [clark2020replicating, clark2021replicating, maire2024market, lipton2025unified]. For instance, [lipton2025unified] showed that a concentrated liquidity position in the range [pa,pb][p\_{a},p\_{b}] with a single unit of liquidity (L​(q)=12​q3/2​𝟙{pa≤q≤pb}L(q)=\frac{1}{2q^{3/2}}\mathbbm{1}\_{\{p\_{a}\leq q\leq p\_{b}\}}) can be decomposed into terms u0u\_{0}, u1/2u\_{1/2}, and u1u\_{1} as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u0​(pt)\displaystyle u\_{0}(p\_{t}) | =p0+ptp0,\displaystyle=\sqrt{p\_{0}}+\frac{p\_{t}}{\sqrt{p\_{0}}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | u1/2​(pt)\displaystyle u\_{1/2}(p\_{t}) | =−2​pt​𝟙{pa≤pt≤pb},\displaystyle=-2\sqrt{p\_{t}}\mathbbm{1}\_{\{p\_{a}\leq p\_{t}\leq p\_{b}\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | u1​(pt)\displaystyle u\_{1}(p\_{t}) | =−2​pa​𝟙{pt<pa}+1pa​(pa−pt)+−2​pb​𝟙{pt>pb}−1pb​(pt−pb)+.\displaystyle=-2\sqrt{p\_{a}}\mathbbm{1}\_{\{p\_{t}<p\_{a}\}}+\frac{1}{\sqrt{p\_{a}}}(p\_{a}-p\_{t})^{+}-2\sqrt{p\_{b}}\mathbbm{1}\_{\{p\_{t}>p\_{b}\}}-\frac{1}{\sqrt{p\_{b}}}(p\_{t}-p\_{b})^{+}. |  |

Applying the general result in ([10](#S3.E10 "In 3.1. Static Replication of Impermanent Loss by Vanilla Options ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) provides a direct derivation of this specific case. By integrating over the range [pa,pb][p\_{a},p\_{b}] and considering the price relative to the boundaries, we recover the tripartite formula:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | IL​(pt|p0,L)\displaystyle{\rm IL}(p\_{t}|p\_{0},L) | =\displaystyle= | ∫pap0(q−pt)+​d​q2​q3/2+∫p0pb(pt−q)+​d​q2​q3/2\displaystyle\int\_{p\_{a}}^{p\_{0}}(q-p\_{t})^{+}\frac{dq}{2q^{3/2}}+\int\_{p\_{0}}^{p\_{b}}(p\_{t}-q)^{+}\frac{dq}{2q^{3/2}} |  |
|  |  | =\displaystyle= | {∫pap0(q−pt)+​d​q2​q3/2+∫p0pb(pt−q)+​d​q2​q3/2}​𝟙{pt<pa}\displaystyle\left\{\int\_{p\_{a}}^{p\_{0}}(q-p\_{t})^{+}\frac{dq}{2q^{3/2}}+\int\_{p\_{0}}^{p\_{b}}(p\_{t}-q)^{+}\frac{dq}{2q^{3/2}}\right\}\mathbbm{1}\_{\{p\_{t}<p\_{a}\}} |  |
|  |  |  | +{∫pap0(q−pt)+​d​q2​q3/2+∫p0pb(pt−q)+​d​q2​q3/2}​𝟙{pt>pb}\displaystyle+\left\{\int\_{p\_{a}}^{p\_{0}}(q-p\_{t})^{+}\frac{dq}{2q^{3/2}}+\int\_{p\_{0}}^{p\_{b}}(p\_{t}-q)^{+}\frac{dq}{2q^{3/2}}\right\}\mathbbm{1}\_{\{p\_{t}>p\_{b}\}} |  |
|  |  |  | +{∫pap0(q−pt)+​d​q2​q3/2+∫p0pb(pt−q)+​d​q2​q3/2}​𝟙{pa≤pt≤pb}\displaystyle+\left\{\int\_{p\_{a}}^{p\_{0}}(q-p\_{t})^{+}\frac{dq}{2q^{3/2}}+\int\_{p\_{0}}^{p\_{b}}(p\_{t}-q)^{+}\frac{dq}{2q^{3/2}}\right\}\mathbbm{1}\_{\{p\_{a}\leq p\_{t}\leq p\_{b}\}} |  |
|  |  | =\displaystyle= | {p0−pa−ptpa+ptp0}​𝟙{pt<pa}\displaystyle\left\{\sqrt{p\_{0}}-\sqrt{p\_{a}}-\frac{p\_{t}}{\sqrt{p\_{a}}}+\frac{p\_{t}}{\sqrt{p\_{0}}}\right\}\mathbbm{1}\_{\{p\_{t}<p\_{a}\}} |  |
|  |  |  | +{ptp0−ptpb−pb+p0}​𝟙{pt>pb}\displaystyle+\left\{\frac{p\_{t}}{\sqrt{p\_{0}}}-\frac{p\_{t}}{\sqrt{p\_{b}}}-\sqrt{p\_{b}}+\sqrt{p\_{0}}\right\}\mathbbm{1}\_{\{p\_{t}>p\_{b}\}} |  |
|  |  |  | +{p0−2​pt+ptp0}​𝟙{pa≤pt≤pb}\displaystyle+\left\{\sqrt{p\_{0}}-2\sqrt{p\_{t}}+\frac{p\_{t}}{\sqrt{p\_{0}}}\right\}\mathbbm{1}\_{\{p\_{a}\leq p\_{t}\leq p\_{b}\}} |  |
|  |  | =\displaystyle= | (p0+ptp0)−2​pt​𝟙{pa≤pt≤pb}−{pa+ptpa}​𝟙{pt<pa}−{ptpb+pb}​𝟙{pt>pb}\displaystyle\left(\sqrt{p\_{0}}+\frac{p\_{t}}{\sqrt{p\_{0}}}\right)-2\sqrt{p\_{t}}\mathbbm{1}\_{\{p\_{a}\leq p\_{t}\leq p\_{b}\}}-\left\{\sqrt{p\_{a}}+\frac{p\_{t}}{\sqrt{p\_{a}}}\right\}\mathbbm{1}\_{\{p\_{t}<p\_{a}\}}-\left\{\frac{p\_{t}}{\sqrt{p\_{b}}}+\sqrt{p\_{b}}\right\}\mathbbm{1}\_{\{p\_{t}>p\_{b}\}} |  |
|  |  | =\displaystyle= | (p0+ptp0)−2​pt​𝟙{pa≤pt≤pb}\displaystyle\left(\sqrt{p\_{0}}+\frac{p\_{t}}{\sqrt{p\_{0}}}\right)-2\sqrt{p\_{t}}\mathbbm{1}\_{\{p\_{a}\leq p\_{t}\leq p\_{b}\}} |  |
|  |  |  | −[2​pa−1pa​(pa−pt)]​𝟙{pt<pa}−[2​pb+1pb​(pt−pb)]​𝟙{pt>pb}\displaystyle-\left[2\sqrt{p\_{a}}-\frac{1}{\sqrt{p\_{a}}}(p\_{a}-p\_{t})\right]\mathbbm{1}\_{\{p\_{t}<p\_{a}\}}-\left[2\sqrt{p\_{b}}+\frac{1}{\sqrt{p\_{b}}}(p\_{t}-p\_{b})\right]\mathbbm{1}\_{\{p\_{t}>p\_{b}\}} |  |
|  |  | =\displaystyle= | p0+ptp0−2​pt​𝟙{pa≤pt≤pb}\displaystyle\sqrt{p\_{0}}+\frac{p\_{t}}{\sqrt{p\_{0}}}-2\sqrt{p\_{t}}\mathbbm{1}\_{\{p\_{a}\leq p\_{t}\leq p\_{b}\}} |  |
|  |  |  | −2​pa​𝟙{pt<pa}+1pa​(pa−pt)+−2​pb​𝟙{pt>pb}−1pb​(pt−pb)+\displaystyle-2\sqrt{p\_{a}}\mathbbm{1}\_{\{p\_{t}<p\_{a}\}}+\frac{1}{\sqrt{p\_{a}}}(p\_{a}-p\_{t})^{+}-2\sqrt{p\_{b}}\mathbbm{1}\_{\{p\_{t}>p\_{b}\}}-\frac{1}{\sqrt{p\_{b}}}(p\_{t}-p\_{b})^{+} |  |
|  |  | =\displaystyle= | u0​(pt)+u1/2​u0​(pt)+u1​u0​(pt).\displaystyle u\_{0}(p\_{t})+u\_{1/2}u\_{0}(p\_{t})+u\_{1}u\_{0}(p\_{t}). |  |

### 3.2. Dynamic Decomposition: Loss-Versus-Rebalancing

In this subsection, we transition to a continuous-time framework to analyze the temporal evolution of Impermanent Loss (IL). A critical, non-hedgeable component of IL is the loss-versus-rebalancing (LVR), first introduced in [milionis2022loss-versus-rebalancing]. We utilize the canonical parametrization in ([4](#S2.E4 "In 2.2. Liquidity Profile and Reserves ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) to provide alternative understandings of the relationship between IL, LVR, and contracts on realized variance such as variance and gamma swaps.

#### 3.2.1. IL as Hedging Cost plus LVR

By applying the Tanaka formula, we derive an alternative expression for the LVR in terms of the local times of the underlying price process PtP\_{t}. Given that IL​(P0|P0,L)=0\mathrm{IL}(P\_{0}|P\_{0},L)=0, the evolution of the impermanent loss can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IL​(Pt|P0,L)\displaystyle\mathrm{IL}(P\_{t}|P\_{0},L) | =∫0td​(IL​(Ps|P0,L))\displaystyle=\int\_{0}^{t}d\left(\mathrm{IL}(P\_{s}|P\_{0},L)\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0t∫0P0L​(q)​d​(q−Ps)+​𝑑q+∫0t∫P0∞L​(q)​d​(Ps−q)+​𝑑q.\displaystyle=\int\_{0}^{t}\int\_{0}^{P\_{0}}L(q)d(q-P\_{s})^{+}dq+\int\_{0}^{t}\int\_{P\_{0}}^{\infty}L(q)d(P\_{s}-q)^{+}dq. |  | (12) |

Applying the Tanaka formula:

|  |  |  |
| --- | --- | --- |
|  | d​(Pt−q)+=−𝟙{Pt≤q}​d​Pt+12​d​ℒtq​(P),d​(q−Pt)+=𝟙{Pt≥q}​d​Pt+12​d​ℒtq​(P),d(P\_{t}-q)^{+}=-\mathbbm{1}\_{\{P\_{t}\leq q\}}dP\_{t}+\frac{1}{2}d\mathcal{L}\_{t}^{q}(P),\quad d(q-P\_{t})^{+}=\mathbbm{1}\_{\{P\_{t}\geq q\}}dP\_{t}+\frac{1}{2}d\mathcal{L}\_{t}^{q}(P), |  |

where ℒtq​(P)\mathcal{L}\_{t}^{q}(P) denotes the local time of PP at qq, we obtain:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | IL​(Pt|P0,L)\displaystyle{\rm IL}(P\_{t}|P\_{0},L) |  | (13) |
|  |  | =\displaystyle= | ∫0P0L​(q)​{−∫0t𝟙{Ps<q}​𝑑Ps+12​ℒtq​(P)}​𝑑q+∫P0∞L​(q)​{∫0t𝟙{Ps>q}​𝑑Ps+12​ℒtq​(P)}​𝑑q\displaystyle\int\_{0}^{P\_{0}}L(q)\left\{-\int\_{0}^{t}\mathbbm{1}\_{\{P\_{s}<q\}}dP\_{s}+\frac{1}{2}\mathcal{L}\_{t}^{q}(P)\right\}dq+\int\_{P\_{0}}^{\infty}L(q)\left\{\int\_{0}^{t}\mathbbm{1}\_{\{P\_{s}>q\}}dP\_{s}+\frac{1}{2}\mathcal{L}\_{t}^{q}(P)\right\}dq |  |
|  |  | =\displaystyle= | −∫0t{∫0P0L​(q)​𝟙{Ps<q}​𝑑q−∫P0∞L​(q)​𝟙{Ps>q}​𝑑q}​𝑑Ps+12​∫0∞L​(q)​ℒtq​(P)​𝑑q.\displaystyle-\int\_{0}^{t}\left\{\int\_{0}^{P\_{0}}L(q)\mathbbm{1}\_{\{P\_{s}<q\}}dq-\int\_{P\_{0}}^{\infty}L(q)\mathbbm{1}\_{\{P\_{s}>q\}}dq\right\}dP\_{s}+\frac{1}{2}\int\_{0}^{\infty}L(q)\mathcal{L}\_{t}^{q}(P)dq.\qquad |  |

Recalling the reserve identity x​(p)=∫p∞L​(q)​𝑑qx(p)=\int\_{p}^{\infty}L(q)\,dq , the term multiplying d​PsdP\_{s} is identified as the change in token XX reserves relative to the initial state:

|  |  |  |
| --- | --- | --- |
|  | ∫0P0L​(q)​𝟙{Ps<q}​𝑑q−∫P0∞L​(q)​𝟙{Ps>q}​𝑑q=x​(Ps)−x​(P0).\int\_{0}^{P\_{0}}L(q)\mathbbm{1}\_{\{P\_{s}<q\}}dq-\int\_{P\_{0}}^{\infty}L(q)\mathbbm{1}\_{\{P\_{s}>q\}}dq=x(P\_{s})-x(P\_{0}). |  |

Substituting this into ([13](#S3.E13 "In 3.2.1. IL as Hedging Cost plus LVR ‣ 3.2. Dynamic Decomposition: Loss-Versus-Rebalancing ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) yields the fundamental dynamic decomposition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IL​(Pt|P0,L)=∫0t{x​(P0)−x​(Ps)}​𝑑Ps+12​∫0∞ℒtq​(P)​L​(q)​𝑑q.\mathrm{IL}(P\_{t}|P\_{0},L)=\int\_{0}^{t}\left\{x(P\_{0})-x(P\_{s})\right\}dP\_{s}+\frac{1}{2}\int\_{0}^{\infty}\mathcal{L}\_{t}^{q}(P)L(q)dq. |  | (14) |

The first integral, ∫0t{x​(P0)−x​(Ps)}​𝑑Ps\int\_{0}^{t}\{x(P\_{0})-x(P\_{s})\}dP\_{s}, represents the hedging cost or arbitrage profit arising from continuous rebalancing. The remaining term defines the LVR:

|  |  |  |  |
| --- | --- | --- | --- |
|  | LVRt:=12​∫0∞ℒtq​(P)​L​(q)​𝑑q.\mathrm{LVR}\_{t}:=\frac{1}{2}\int\_{0}^{\infty}\mathcal{L}\_{t}^{q}(P)L(q)\,dq. |  | (15) |

This representation characterizes LVR as a weighted sum of the local times of the price process across the entire price spectrum, with weights provided by the liquidity profile LL. By the occupation time formula, the LVR can be expressed as a time-integral of the quadratic variation ⟨P⟩\langle P\rangle:

|  |  |  |  |
| --- | --- | --- | --- |
|  | LVRt=12​∫0tL​(Ps)​d​⟨P⟩s,\mathrm{LVR}\_{t}=\frac{1}{2}\int\_{0}^{t}L(P\_{s})d\langle P\rangle\_{s}, |  | (16) |

This formulation generalizes the LVR results in [milionis2022loss-versus-rebalancing] to arbitrary liquidity profiles and establishes a direct functional link between LL and the non-hedgeable risk of the position.

###### Example 3.1.

Consider the edge case L​(q)=l​δ​(q−q0)L(q)=l\,\delta(q-q\_{0}), where an LP provides liquidity ll only at price q0q\_{0}. In this scenario:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IL​(Pt|P0,L)\displaystyle\mathrm{IL}(P\_{t}|P\_{0},L) | =l​(q0−Pt)+​𝟙{P0≥q0}+l​(Pt−q0)+​𝟙{P0≤q0},\displaystyle=l(q\_{0}-P\_{t})^{+}\mathbbm{1}\_{\{P\_{0}\geq q\_{0}\}}+l(P\_{t}-q\_{0})^{+}\mathbbm{1}\_{\{P\_{0}\leq q\_{0}\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | LVRt\displaystyle{\rm LVR}\_{t} | =l2​∫0∞ℒtq​(P)​δ​(q−q0)​𝑑q=l2​ℒtq0​(P).\displaystyle=\frac{l}{2}\int\_{0}^{\infty}\mathcal{L}\_{t}^{q}(P)\delta(q-q\_{0})dq=\frac{l}{2}\mathcal{L}\_{t}^{q\_{0}}(P). |  |

Thus, the IL equates to the payoff of ll vanilla options struck at q0q\_{0}, while the LVR is precisely half the local time spent by the price process at q0q\_{0}.

To demonstrate the advantages of expressing LVR via the liquidity profile LL as defined in ([16](#S3.E16 "In 3.2.1. IL as Hedging Cost plus LVR ‣ 3.2. Dynamic Decomposition: Loss-Versus-Rebalancing ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")), we recover several key results from Sections 6.1 and 6.2 of [fukasawa2023weighted]:

###### Proposition 3.2.

1. (1)

   For a CFMM with the bonding curve x+ln⁡y=Kx+\ln y=K , the Impermanent Loss at time TT is given by:

   |  |  |  |
   | --- | --- | --- |
   |  | ILT=−PT+P0+PT​ln⁡PTP0,\mathrm{IL}\_{T}=-P\_{T}+P\_{0}+P\_{T}\ln\frac{P\_{T}}{P\_{0}}, |  |

   where PTP\_{T} and P0P\_{0} are the spot prices at times TT and 0, respectively. Modulo the P&L from holding one unit of the risky asset, this IL is equivalent to the payoff of an entropy contract and, at time 0, corresponds to the value of a gamma swap (up to a factor of 2).
2. (2)

   For a CFMM with the bonding curve ln⁡x+y=K\ln x+y=K, the Impermanent Loss at time TT is:

   |  |  |  |
   | --- | --- | --- |
   |  | ILT=PTP0−1−ln⁡PTP0.\mathrm{IL}\_{T}=\frac{P\_{T}}{P\_{0}}-1-\ln\frac{P\_{T}}{P\_{0}}. |  |

   Modulo the P&L from holding one unit of the risky asset, this IL is equivalent to the payoff of a log contract and, at time 0, corresponds to the value of a variance swap (up to a factor of 2).

###### Proof.

For the curve x+ln⁡y=Kx+\ln y=K, we set f​(x,y)=x+ln⁡yf(x,y)=x+\ln y. It follows that p=fxfy=yp=\frac{f\_{x}}{f\_{y}}=y. Using ([1](#S2.E1 "In 2.1. Dimensionally Consistent Liquidity ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")), the local intrinsic liquidity is:

|  |  |  |
| --- | --- | --- |
|  | ℓ=−2​(fx​fy)3/2fx​x​fy2−2​fx​y​fx​fy+fy​y​fx2=−2​y−3/2−y−2=2​y=2​p.\displaystyle\ell=\frac{-2(f\_{x}f\_{y})^{3/2}}{f\_{xx}f\_{y}^{2}-2f\_{xy}f\_{x}f\_{y}+f\_{yy}f\_{x}^{2}}=\frac{-2y^{-3/2}}{-y^{-2}}=2\sqrt{y}=2\sqrt{p}. |  |

Thus, the liquidity profile is L​(q)=ℓ​(q)2​q3=1qL(q)=\frac{\ell(q)}{2\sqrt{q^{3}}}=\frac{1}{q}. Applying ([11](#S3.E11 "In 3.1. Static Replication of Impermanent Loss by Vanilla Options ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) yields:

|  |  |  |
| --- | --- | --- |
|  | ILT=∫P0PT​(PT−q)​d​qq=PT​ln⁡PTP0−PT+P0.\displaystyle\mathrm{IL}\_{T}=\int{P\_{0}}^{P\_{T}}(P\_{T}-q)\frac{dq}{q}=P\_{T}\ln\frac{P\_{T}}{P\_{0}}-P\_{T}+P\_{0}. |  |

For the curve ln⁡x+y=K\ln x+y=K, we have p=1xp=\frac{1}{x} and ℓ=2p\ell=\frac{2}{\sqrt{p}}. This results in L​(q)=1q2L(q)=\frac{1}{q^{2}} , and ([11](#S3.E11 "In 3.1. Static Replication of Impermanent Loss by Vanilla Options ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) gives:

|  |  |  |
| --- | --- | --- |
|  | ILT=∫P0PT​(PT−q)​d​qq2=PTP0−1−ln⁡PTP0.\displaystyle\mathrm{IL}\_{T}=\int{P\_{0}}^{P\_{T}}(P\_{T}-q)\frac{dq}{q^{2}}=\frac{P\_{T}}{P\_{0}}-1-\ln\frac{P\_{T}}{P\_{0}}. |  |

∎

We remark that the gamma and variance swaps identified above result directly from the LVR. Equation ([16](#S3.E16 "In 3.2.1. IL as Hedging Cost plus LVR ‣ 3.2. Dynamic Decomposition: Loss-Versus-Rebalancing ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) implies that for the curve x+ln⁡y=Kx+\ln y=K (where L​(q)=1qL(q)=\frac{1}{q}), we have:

|  |  |  |
| --- | --- | --- |
|  | 2×LVRT=∫0Td​⟨P⟩sPs,2\times\mathrm{LVR}\_{T}=\int\_{0}^{T}\frac{d\langle P\rangle\_{s}}{P\_{s}}, |  |

which is precisely the payoff of a gamma swap. For the curve ln⁡x+y=K\ln x+y=K, we similarly obtain:

|  |  |  |
| --- | --- | --- |
|  | 2×LVRT=∫0Td​⟨P⟩sPs2,2\times\mathrm{LVR}\_{T}=\int\_{0}^{T}\frac{d\langle P\rangle\_{s}}{P\_{s}^{2}}, |  |

representing the payoff of a variance swap.

The converse also holds: if a gamma swap hedges the LVR pathwise such that LVRT=12​∫0Td​⟨P⟩tPt\mathrm{LVR}\_{T}=\frac{1}{2}\int\_{0}^{T}\frac{d\langle P\rangle\_{t}}{P\_{t}} , then L​(p)=1pL(p)=\frac{1}{p}. The canonical parametrization then yields:

|  |  |  |
| --- | --- | --- |
|  | x​(p)=∫pC1q​𝑑q=ln⁡C−ln⁡p,y​(p)=∫0p𝑑q=p,\displaystyle x(p)=\int\_{p}^{C}\frac{1}{q}dq=\ln C-\ln p,\quad y(p)=\int\_{0}^{p}dq=p, |  |

for a constant C>0C>0. Eliminating pp confirms the bonding curve x+ln⁡y=ln⁡Cx+\ln y=\ln C. For a variance swap where LVRT=12​∫0Td​⟨P⟩tPt2\mathrm{LVR}\_{T}=\frac{1}{2}\int\_{0}^{T}\frac{d\langle P\rangle\_{t}}{P\_{t}^{2}} , the profile L​(p)=1p2L(p)=\frac{1}{p^{2}} corresponds to the bonding curve ln⁡x+y=K\ln x+y=K.

#### 3.2.2. Implications for LVR Design and Pricing

The formulation of LVR in ([16](#S3.E16 "In 3.2.1. IL as Hedging Cost plus LVR ‣ 3.2. Dynamic Decomposition: Loss-Versus-Rebalancing ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) provides a constructive method for designing liquidity profiles, and by extension bonding curves, that satisfy specific risk-management objectives under a time-homogeneous local volatility model. This approach mirrors the “replicating market maker” strategy discussed in Section [2.4](#S2.SS4 "2.4. Replicating Market Makers ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making"), but redirects the focus toward the non-hedgeable LVR component.

Consider a price process PtP\_{t} governed by the following SDE:

|  |  |  |
| --- | --- | --- |
|  | d​PtPt=μt​d​t+σ​(Pt)​d​Wt.\frac{dP\_{t}}{P\_{t}}=\mu\_{t}dt+\sigma(P\_{t})dW\_{t}. |  |

The quadratic variation is given by d​⟨P⟩t=Pt2​σ2​(Pt)​d​td\langle P\rangle\_{t}=P\_{t}^{2}\sigma^{2}(P\_{t})dt. By selecting a liquidity profile L​(q)L(q) that inversely scales with the stochastic term of the quadratic variation, specifically:

|  |  |  |
| --- | --- | --- |
|  | L​(q)=Cq2​σ2​(q),L(q)=\frac{C}{q^{2}\sigma^{2}(q)}, |  |

for some constant CC, the resulting LVR process becomes:

|  |  |  |
| --- | --- | --- |
|  | LVRt=12​∫0tL​(Ps)​d​⟨P⟩s=12​∫0tCPs2​σ2​(Ps)​Ps2​σ2​(Ps)​𝑑s=C2​t.\mathrm{LVR}\_{t}=\frac{1}{2}\int\_{0}^{t}L(P\_{s})d\langle P\rangle\_{s}=\frac{1}{2}\int\_{0}^{t}\frac{C}{P\_{s}^{2}\sigma^{2}(P\_{s})}P\_{s}^{2}\sigma^{2}(P\_{s})ds=\frac{C}{2}t. |  |

In this configuration, the LVR is entirely deterministic and proportional to time, effectively eliminating the risk stemming from price volatility. This design methodology allows for the construction of LVR-neutral profiles tailored to specific market assumptions.

###### Example 3.3 (LVR-neutral profile in the CEV model).

The Constant Elasticity of Variance (CEV) model is a local volatility model characterized by the SDE:

|  |  |  |
| --- | --- | --- |
|  | d​Pt=ν​Ptβ​d​WtdP\_{t}=\nu P\_{t}^{\beta}dW\_{t} |  |

for constants ν>0\nu>0 and β≥0\beta\geq 0. Under risk-neutral probability with zero interest and dividend rates, the local volatility function is σ​(p)=ν​pβ−1\sigma(p)=\nu p^{\beta-1}. Setting the liquidity profile as

|  |  |  |
| --- | --- | --- |
|  | L​(q)=Cq2​σ2​(q)=Cν2​q2​β,L(q)=\frac{C}{q^{2}\sigma^{2}(q)}=\frac{C}{\nu^{2}q^{2\beta}}, |  |

renders the LVR deterministic at C2​t\frac{C}{2}t. The bonding curves associated with this profile vary by the elasticity parameter β\beta:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x\displaystyle x | =\displaystyle= | Cν2​∫p∞1q2​β​𝑑q={Cν2​p1−2​β2​β−1 if ​β>12;Cν2​(ln⁡M−ln⁡p) if ​β=12, for some large ​M>0;Cν2​11−2​β​(M1−2​β−p1−2​β) if ​β<12, for some large ​M>0;\displaystyle\frac{C}{\nu^{2}}\int\_{p}^{\infty}\frac{1}{q^{2\beta}}dq=\left\{\begin{array}[]{ll}\frac{C}{\nu^{2}}\frac{p^{1-2\beta}}{2\beta-1}&\mbox{ if }\beta>\frac{1}{2};\\ &\\ \frac{C}{\nu^{2}}(\ln M-\ln p)&\mbox{ if }\beta=\frac{1}{2},\mbox{ for some large }M>0;\\ &\\ \frac{C}{\nu^{2}}\frac{1}{1-2\beta}(M^{1-2\beta}-p^{1-2\beta})&\mbox{ if }\beta<\frac{1}{2},\mbox{ for some large }M>0;\end{array}\right. |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y\displaystyle y | =\displaystyle= | Cν2​∫0p1q2​β−1​𝑑q={Cν2​12​(1−β)​p2​(1−β) if ​β<1;Cν2​(ln⁡p−ln⁡ϵ) if ​β=1, for some small ​ϵ>0;;Cν2​12​(β−1)​(ϵ2−2​β−p2−2​β) if ​β>1, for some small ​ϵ>0;\displaystyle\frac{C}{\nu^{2}}\int\_{0}^{p}\frac{1}{q^{2\beta-1}}dq=\left\{\begin{array}[]{ll}\frac{C}{\nu^{2}}\frac{1}{2(1-\beta)}p^{2(1-\beta)}&\mbox{ if }\beta<1;\\ &\\ \frac{C}{\nu^{2}}(\ln p-\ln\epsilon)&\mbox{ if }\beta=1,\mbox{ for some small }\epsilon>0;;\\ &\\ \frac{C}{\nu^{2}}\frac{1}{2(\beta-1)}(\epsilon^{2-2\beta}-p^{2-2\beta})&\mbox{ if }\beta>1,\mbox{ for some small }\epsilon>0;\end{array}\right. |  |

In particular, when 12<β<1\frac{1}{2}<\beta<1, the bonding curve is represented by the G3M form xα​y1−α=Kx^{\alpha}y^{1-\alpha}=K, where α=2−2​β\alpha=2-2\beta.

Despite its path-dependent nature, LVR can be priced as a static European contingent claim. Let Ψ​(P)\Psi(P) be the second antiderivative of the liquidity profile, such that Ψ′′​(P)=L​(P)\Psi^{\prime\prime}(P)=L(P). Applying Itô’s formula to Ψ​(Pt)\Psi(P\_{t}):

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | d​Ψ​(Pt)\displaystyle d\Psi(P\_{t}) | =\displaystyle= | Ψ′​(Pt)​d​Pt+12​Ψ′′​(Pt)​d​⟨P⟩t\displaystyle\Psi^{\prime}(P\_{t})dP\_{t}+\frac{1}{2}\Psi^{\prime\prime}(P\_{t})d\langle P\rangle\_{t} |  | (19) |
|  |  | =\displaystyle= | Ψ′​(Pt)​d​Pt+12​L​(Pt)​d​⟨P⟩t.\displaystyle\Psi^{\prime}(P\_{t})dP\_{t}+\frac{1}{2}L(P\_{t})d\langle P\rangle\_{t}. |  |

If the price process PtP\_{t} is a ℚ\mathbb{Q}-martingale, integrating from 0 to TT and taking the expectation yields the LVR price:

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​[LVRT]=𝔼ℚ​[Ψ​(PT)]−Ψ​(P0).\mathbb{E}^{\mathbb{Q}}[\mathrm{LVR}\_{T}]=\mathbb{E}^{\mathbb{Q}}[\Psi(P\_{T})]-\Psi(P\_{0}). |  |

This reduction allows for the use of standard European option pricing techniques, such as Fourier transforms or Monte Carlo simulations, to value the ongoing cost of liquidity provision.

### 3.3. Risk Neutral Pricing and Hedging for Impermanent Loss

In this subsection, we move beyond static replication to address the pricing and hedging of liquidity provision in a dynamic market setting. Building on the equivalence between providing liquidity and maintaining a short position in a convex contingent claim, we apply option pricing theory to quantify risk and establish hedging parameters. By assuming the spot price process PtP\_{t} is a martingale under a risk-neutral probability ℚ\mathbb{Q}, we derive the fair value of IL and define implied volatility metrics for general liquidity profiles.

#### 3.3.1. Pricing IL as a European-Style Contingent Claim

If we treat IL as a European-style contingent claim that pays the amount IL​(PT|P0,L)\mathrm{IL}(P\_{T}|P\_{0},L) at maturity TT, its risk-neutral price ΠtIL​(L,T)\Pi\_{t}^{\mathrm{IL}}(L,T) at any time t∈[0,T]t\in[0,T] is determined by the conditional expectation under the risk-neutral measure ℚ\mathbb{Q}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΠtIL​(L,T)\displaystyle\Pi^{\mathrm{IL}}\_{t}(L,T) | :=𝔼ℚ​[IL​(PT|P0,L)∣ℱt]\displaystyle:=\mathbb{E}^{\mathbb{Q}}\left[\mathrm{IL}(P\_{T}|P\_{0},L)\mid\mathcal{F}\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0P0L​(q)​𝔼ℚ​[(q−PT)+∣ℱt]​𝑑q+∫P0∞​L​(q)​𝔼ℚ​[(PT−q)+∣ℱt]​𝑑q\displaystyle=\int\_{0}^{P\_{0}}L(q)\mathbb{E}^{\mathbb{Q}}\left[(q-P\_{T})^{+}\mid\mathcal{F}\_{t}\right]dq+\int{P\_{0}}^{\infty}L(q)\mathbb{E}^{\mathbb{Q}}\left[(P\_{T}-q)^{+}\mid\mathcal{F}\_{t}\right]dq |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0P0L​(q)​Pt​(q,T)​𝑑q+∫P0∞​L​(q)​Ct​(q,T)​𝑑q,\displaystyle=\int\_{0}^{P\_{0}}L(q)P\_{t}(q,T)dq+\int{P\_{0}}^{\infty}L(q)C\_{t}(q,T)dq, |  | (20) |

where Ct​(q,T)C\_{t}(q,T) and Pt​(q,T)P\_{t}(q,T) represent the time-tt market prices of European call and put options with strike qq and maturity TT.

Applying Jensen’s inequality, it follows that for t∈[0,T]t\in[0,T]:

|  |  |  |
| --- | --- | --- |
|  | ΠtIL​(L,T)≥IL​(Pt|P0,L).\Pi\_{t}^{\mathrm{IL}}(L,T)\geq\mathrm{IL}(P\_{t}|P\_{0},L). |  |

This inequality underscores a vital distinction for LPs: the risk-neutral fair value of their potential loss is always greater than or equal to the current realized IL prior to expiry.

##### Delta of IL

The Delta of the risk-neutral price ΠtIL\Pi\_{t}^{\mathrm{IL}} with respect to the pool price PtP\_{t} is given by the weighted integral of the constituent option deltas:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔtΠIL=∂ΠIL​t∂Pt=∫0P0L​(q)​ΔtP​(q,T)​𝑑q+∫P0∞L​(q)​ΔtC​(q,T)​𝑑q,\Delta^{\Pi^{\mathrm{IL}}}\_{t}=\frac{\partial\Pi^{\mathrm{IL}}t}{\partial P\_{t}}=\int\_{0}^{P\_{0}}L(q)\Delta^{P}\_{t}(q,T)dq+\int\_{P\_{0}}^{\infty}L(q)\Delta^{C}\_{t}(q,T)dq, |  | (21) |

where Δti​(q,T)\Delta^{i}\_{t}(q,T) is the Delta of a put or call option (i∈{P,C}i\in\{P,C\}). This result confirms that within a local volatility framework, the market is complete, and the IL risk can be dynamically hedged by holding ΔtΠIL\Delta^{\Pi^{\mathrm{IL}}}\_{t} units of the underlying asset XX.

We distinguish this from the Delta of the current realized IL value, ΔtIL\Delta\_{t}^{\mathrm{IL}}, which is defined as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΔtIL\displaystyle\Delta\_{t}^{\rm IL} | :=\displaystyle:= | ∂∂Pt​IL​(Pt|P0,L)=∂∂Pt​{∫0P0L​(q)​(q−Pt)+​𝑑q+∫P0∞L​(q)​(Pt−q)+​𝑑q}\displaystyle\frac{\partial}{\partial P\_{t}}{\rm IL}(P\_{t}|P\_{0},L)=\frac{\partial}{\partial P\_{t}}\left\{\int\_{0}^{P\_{0}}L(q)(q-P\_{t})^{+}dq+\int\_{P\_{0}}^{\infty}L(q)(P\_{t}-q)^{+}dq\right\} |  |
|  |  | =\displaystyle= | −∫0P0L​(q)​θ​(q−Pt)​𝑑q+∫P0∞L​(q)​θ​(Pt−q)​𝑑q\displaystyle-\int\_{0}^{P\_{0}}L(q)\theta(q-P\_{t})dq+\int\_{P\_{0}}^{\infty}L(q)\theta(P\_{t}-q)dq |  |
|  |  | =\displaystyle= | ∫P0PtL​(q)​𝑑q,\displaystyle\int\_{P\_{0}}^{P\_{t}}L(q)dq, |  |

where recall that θ​(⋅)\theta(\cdot) denotes the Heaviside function. Importantly, ΔtIL\Delta\_{t}^{\mathrm{IL}} reflects the instantaneous sensitivity of current reserves but does not generate the terminal payoff required to replicate the IL at maturity in a complete market.

###### Example 3.4 (Delta of Concentrated Liquidity).

Consider a concentrated liquidity position L​(q)=ℓ2​q3/2​𝟙[pa,pb]​(q)L(q)=\frac{\ell}{2q^{3/2}}\mathbbm{1}\_{[p\_{a},p\_{b}]}(q) for a constant ℓ>0\ell>0 and price boundaries 0<pa<P0<pb0<p\_{a}<P\_{0}<p\_{b}. The Delta of the realized Impermanent Loss, ΔtIL\Delta\_{t}^{\mathrm{IL}}, represents the instantaneous change in current value:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔtIL\displaystyle\Delta\_{t}^{\mathrm{IL}} | =∫P0PtL​(q),d​q=∫P0Ptℓ2​q3/2​𝟙[pa,pb]​(q)​𝑑q={ℓP0−ℓmin⁡{Pt,pb}if ​Pt≥P0,ℓmax⁡{Pt,pa}−ℓP0if ​Pt≤P0,\displaystyle=\int\_{P\_{0}}^{P\_{t}}L(q),dq=\int\_{P\_{0}}^{P\_{t}}\frac{\ell}{2q^{3/2}}\mathbbm{1}\_{[p\_{a},p\_{b}]}(q)dq=\begin{cases}\frac{\ell}{\sqrt{P\_{0}}}-\frac{\ell}{\sqrt{\min\{P\_{t},p\_{b}\}}}&\text{if }P\_{t}\geq P\_{0},\\ \frac{\ell}{\sqrt{\max\{P\_{t},p\_{a}\}}}-\frac{\ell}{\sqrt{P\_{0}}}&\text{if }P\_{t}\leq P\_{0},\end{cases} |  |

whereas the risk-neutral Delta, ΔtΠIL\Delta\_{t}^{\Pi^{\mathrm{IL}}}, which incorporates market expectations and time-to-maturity, is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔtΠIL\displaystyle\Delta\_{t}^{\Pi^{\mathrm{IL}}} | =∫0P0ΔtP​(q,T)​L​(q)​𝑑q+∫P0∞ΔtC​(q,T)​L​(q)​𝑑q\displaystyle=\int\_{0}^{P\_{0}}\Delta\_{t}^{P}(q,T)L(q)dq+\int\_{P\_{0}}^{\infty}\Delta\_{t}^{C}(q,T)L(q)dq |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℓ​∫paP0ΔtP​(q,T)​d​q2​q3/2+ℓ​∫P0pbΔtC​(q,T)​d​q2​q3/2.\displaystyle=\ell\int\_{p\_{a}}^{P\_{0}}\Delta\_{t}^{P}(q,T)\frac{dq}{2q^{3/2}}+\ell\int\_{P\_{0}}^{p\_{b}}\Delta\_{t}^{C}(q,T)\frac{dq}{2q^{3/2}}. |  |

##### Gamma of IL

The Gamma of the risk-neutral price, ΓtΠIL\Gamma\_{t}^{\Pi^{\mathrm{IL}}}, is the second-order sensitivity to the pool price:

|  |  |  |
| --- | --- | --- |
|  | ΓtΠIL=∂2ΠtIL∂Pt2=∫0P0L​(q)​ΓtP​(q,T)​𝑑q+∫P0∞L​(q)​ΓtC​(q,T)​𝑑q,\Gamma^{\Pi^{\mathrm{IL}}}\_{t}=\frac{\partial^{2}\Pi\_{t}^{\mathrm{IL}}}{\partial P\_{t}^{2}}=\int\_{0}^{P\_{0}}L(q)\Gamma^{P}\_{t}(q,T)dq+\int\_{P\_{0}}^{\infty}L(q)\Gamma^{C}\_{t}(q,T)dq, |  |

where Γti​(q,T)\Gamma^{i}\_{t}(q,T) is the gamma of the option struck at qq and expiry TT, for i={C,P}i=\{C,P\}.

For the current realized value, the Gamma simplifies directly to the liquidity profile density at the current price:

|  |  |  |
| --- | --- | --- |
|  | ΓtIL=∂∂Pt​ΔtIL=L​(Pt),\Gamma\_{t}^{\mathrm{IL}}=\frac{\partial}{\partial P\_{t}}\Delta\_{t}^{\mathrm{IL}}=L(P\_{t}), |  |

###### Example 3.5 (Gamma of Concentrated Liquidity).

Continuing with the concentrated liquidity profile L​(q)=ℓ2​q3/2​𝟙[pa,pb]​(q)L(q)=\frac{\ell}{2q^{3/2}}\mathbbm{1}\_{[p\_{a},p\_{b}]}(q) from Example [3.4](#S3.Thmtheorem4 "Example 3.4 (Delta of Concentrated Liquidity). ‣ Delta of IL ‣ 3.3.1. Pricing IL as a European-Style Contingent Claim ‣ 3.3. Risk Neutral Pricing and Hedging for Impermanent Loss ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making"), the Gamma of the realized IL corresponds directly to the liquidity density at the current price:

|  |  |  |
| --- | --- | --- |
|  | ΓtIL=L​(Pt)=ℓ2​Pt3​𝟙[pa,pb]​(Pt).\Gamma\_{t}^{\mathrm{IL}}=L(P\_{t})=\frac{\ell}{2\sqrt{P\_{t}^{3}}}\mathbbm{1}\_{[p\_{a},p\_{b}]}(P\_{t}). |  |

The Gamma of the risk-neutral price ΠtIL\Pi\_{t}^{\mathrm{IL}} is the expectation-weighted sum of vanilla option Gammas:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΓtΠIL\displaystyle\Gamma\_{t}^{\Pi^{\mathrm{IL}}} | =∫0P0ΓtP​(q,T)​L​(q)​𝑑q+∫P0∞ΓtC​(q,T)​L​(q)​𝑑q\displaystyle=\int\_{0}^{P\_{0}}\Gamma\_{t}^{P}(q,T)L(q)dq+\int\_{P\_{0}}^{\infty}\Gamma\_{t}^{C}(q,T)L(q)dq |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℓ​∫paP0ΓtP​(q,T)​d​q2​q3/2+ℓ​∫P0pbΓtC​(q,T)​d​q2​q3/2.\displaystyle=\ell\int\_{p\_{a}}^{P\_{0}}\Gamma\_{t}^{P}(q,T)\frac{dq}{2q^{3/2}}+\ell\int\_{P\_{0}}^{p\_{b}}\Gamma\_{t}^{C}(q,T)\frac{dq}{2q^{3/2}}. |  |

Vega of IL
In models such as Black–Scholes, the Vega of the IL position is likewise a weighted sum of vanilla Vegas:

|  |  |  |
| --- | --- | --- |
|  | νtΠIL=∫0P0L​(q)​νtP​(q,T)​𝑑q+∫P0∞L​(q)​νtC​(q,T)​𝑑q,\nu^{\Pi^{\mathrm{IL}}}\_{t}=\int\_{0}^{P\_{0}}L(q)\nu^{P}\_{t}(q,T)dq+\int\_{P\_{0}}^{\infty}L(q)\nu^{C}\_{t}(q,T)dq, |  |

where νti​(q,T)\nu^{i}\_{t}(q,T) is the vega of the option struck at qq and expiry TT, for i={C,P}i=\{C,P\}, enabling LPs to quantify their exposure to forward-looking volatility shifts.

#### 3.3.2. Implied Volatility for Liquidity Profile

For a given liquidity profile LL, we define the Black–Scholes implied volatility σBS​(L,T)\sigma\_{\mathrm{BS}}(L,T) as the unique value σ\sigma that satisfies the following equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0P0L​(q)​PBS​(q,T,σ)​𝑑q+∫P0∞L​(q)​CBS​(q,T,σ)​𝑑q=∫0P0L​(q)​P​(q,T)​𝑑q+∫P0∞L​(q)​C​(q,T)​𝑑q,\int\_{0}^{P\_{0}}L(q)P\_{\mathrm{BS}}(q,T,\sigma)dq+\int\_{P\_{0}}^{\infty}L(q)C\_{\mathrm{BS}}(q,T,\sigma)dq=\int\_{0}^{P\_{0}}L(q)P(q,T)dq+\int\_{P\_{0}}^{\infty}L(q)C(q,T)dq, |  | (22) |

where PBSP\_{\mathrm{BS}} and CBSC\_{\mathrm{BS}} denote the risk-neutral prices of European puts and calls under the Black–Scholes model. The right-hand side represents the market price of the IL contingent claim, ΠIL\Pi^{\mathrm{IL}}, constructed from discrete market option quotes. Similarly, the Bachelier implied volatility σB​(L,T)\sigma\_{\mathrm{B}}(L,T) is defined by solving:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0P0L​(q)​PB​(q,T,σ)​𝑑q+∫P0∞L​(q)​CB​(q,T,σ)​𝑑q=∫0P0L​(q)​P​(q,T)​𝑑q+∫P0∞L​(q)​C​(q,T)​𝑑q,\int\_{0}^{P\_{0}}L(q)P\_{\mathrm{B}}(q,T,\sigma)dq+\int\_{P\_{0}}^{\infty}L(q)C\_{\mathrm{B}}(q,T,\sigma)dq=\int\_{0}^{P\_{0}}L(q)P(q,T)dq+\int\_{P\_{0}}^{\infty}L(q)C(q,T)dq, |  | (23) |

where PBP\_{\mathrm{B}} and CBC\_{\mathrm{B}} are option prices under the Bachelier model. We note that the implied volatilities defined in ([22](#S3.E22 "In 3.3.2. Implied Volatility for Liquidity Profile ‣ 3.3. Risk Neutral Pricing and Hedging for Impermanent Loss ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) and ([23](#S3.E23 "In 3.3.2. Implied Volatility for Liquidity Profile ‣ 3.3. Risk Neutral Pricing and Hedging for Impermanent Loss ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) are homogeneous of degree zero in LL, as the pricing equations on both sides are linear with respect to the liquidity profile. This metric allows for a standardized “price of liquidity” that is consistent with the Black–Scholes paradigm, bridging the gap between endogenous fee generation and exogenous asset volatility.

Since the left-hand side of both ([22](#S3.E22 "In 3.3.2. Implied Volatility for Liquidity Profile ‣ 3.3. Risk Neutral Pricing and Hedging for Impermanent Loss ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) and ([23](#S3.E23 "In 3.3.2. Implied Volatility for Liquidity Profile ‣ 3.3. Risk Neutral Pricing and Hedging for Impermanent Loss ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) is strictly increasing with respect to σ\sigma, we establish the following existence and uniqueness result:

###### Proposition 3.6 (Existence and Uniqueness of Implied Volatility).

For a given liquidity profile LL and maturity TT, there exists a unique solution σBS​(L,T)\sigma\_{\mathrm{BS}}(L,T) (resp. σB​(L,T)\sigma\_{\mathrm{B}}(L,T)) for equation ([22](#S3.E22 "In 3.3.2. Implied Volatility for Liquidity Profile ‣ 3.3. Risk Neutral Pricing and Hedging for Impermanent Loss ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) (resp. equation ([23](#S3.E23 "In 3.3.2. Implied Volatility for Liquidity Profile ‣ 3.3. Risk Neutral Pricing and Hedging for Impermanent Loss ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making"))).

The central insight is that, for each liquidity profile LL and a given maturity TT, we can assign an implied volatility σ​(L,T)\sigma(L,T) by equating the theoretical IL price under a specific model (e.g., Black-Scholes or Bachelier) to the option-implied risk neutral price of IL.

#### 3.3.3. Fine Structure of Implied Volatility

While the global implied volatilities σBS​(L,⋅)\sigma\_{\mathrm{BS}}(L,\cdot) and σB​(L,⋅)\sigma\_{\mathrm{B}}(L,\cdot) characterize the risk profile of the liquidity position in aggregation, they do not distinguish between the risks associated with different segments of the price spectrum. To achieve a more granular assessment, we define the fine structure of implied volatility, which highlights the market-implied risk associated with specific intervals within the liquidity profile. This approach is particularly instructive for platforms like Uniswap v3, where liquidity is non-uniformly distributed across discrete tick ranges.

Assume the liquidity profile LL is supported on the interval [pm,pM][p\_{m},p\_{M}] where 0<pm<pM<∞0<p\_{m}<p\_{M}<\infty. Let {πk}\{\pi\_{k}\} be a sequence of nested partitions of this interval such that πk={pm=p0<p1<⋯<pik=pM}\pi\_{k}=\{p\_{m}=p\_{0}<p\_{1}<\cdots<p\_{i\_{k}}=p\_{M}\}. For each sub-interval j∈{1,…,ik}j\in\{1,\dots,i\_{k}\}, we define the segmented liquidity profile LjπkL\_{j}^{\pi\_{k}} as:

|  |  |  |
| --- | --- | --- |
|  | Ljπk​(q)=L​(q)​𝟙{pj−1≤q≤pj},L\_{j}^{\pi\_{k}}(q)=L(q)\mathbbm{1}\_{\{p\_{j-1}\leq q\leq p\_{j}\}}, |  |

with its corresponding risk-neutral market price Πjπk\Pi\_{j}^{\pi\_{k}} defined by the sum of market put and call options integrated over the segment:

|  |  |  |
| --- | --- | --- |
|  | Πjπk:=∫0P0P​(q,T)​Ljπk​(q)​𝑑q+∫P0∞C​(q,T)​Ljπk​(q)​𝑑q.\Pi\_{j}^{\pi\_{k}}:=\int\_{0}^{P\_{0}}P(q,T)L\_{j}^{\pi\_{k}}(q)dq+\int\_{P\_{0}}^{\infty}C(q,T)L\_{j}^{\pi\_{k}}(q)dq. |  |

The fine structure of the Black–Scholes implied volatility for the profile LL is then defined as the collection of values {σj,BSπk}\{\sigma\_{j,\mathrm{BS}}^{\pi\_{k}}\} that solve the pricing equation for each segment jj:

|  |  |  |
| --- | --- | --- |
|  | Πjπk,BS​(σ)=∫0P0PBS​(q,T,σ)​Ljπk​(q)​𝑑q+∫P0∞CBS​(q,T,σ)​Ljπk​(q)​𝑑q=Πjπk.\Pi\_{j}^{\pi\_{k},\mathrm{BS}}(\sigma)=\int\_{0}^{P\_{0}}P\_{\mathrm{BS}}(q,T,\sigma)L\_{j}^{\pi\_{k}}(q)dq+\int\_{P\_{0}}^{\infty}C\_{\mathrm{BS}}(q,T,\sigma)L\_{j}^{\pi\_{k}}(q)dq=\Pi\_{j}^{\pi\_{k}}. |  |

By the linearity of the integral, the total risk-neutral price ΠIL\Pi^{\mathrm{IL}} is recovered as the sum of the segmented prices:

|  |  |  |
| --- | --- | --- |
|  | ΠIL=∑j=1ikΠjπk=∑j=1ikΠjπk,BS​(σj,BSπk).\Pi^{\mathrm{IL}}=\sum\_{j=1}^{i\_{k}}\Pi\_{j}^{\pi\_{k}}=\sum\_{j=1}^{i\_{k}}\Pi\_{j}^{\pi\_{k},\mathrm{BS}}(\sigma\_{j,\mathrm{BS}}^{\pi\_{k}}). |  |

However, there are no simple expressions relating the aggregate implied volatility σBS​(L,⋅)\sigma\_{\mathrm{BS}}(L,\cdot) to its fine structure components, the σj,BSπk\sigma\_{j,\mathrm{BS}}^{\pi\_{k}}’s. We conclude that the fine structure for the Bachelier implied volatility can be constructed similarly. We reiterate that examples on the fine structures of implied volatilities for liquidity profiles of various liquidity pools in the Uniswap v3 platform can be found in Section [5](#S5 "5. Data and Numerical Implementation ‣ Pricing and hedging for liquidity provision in Constant Function Market Making").

## 4. Pricing via Last Passage Time

In this section, we move beyond the standard treatment of Impermanent Loss (IL) as a perpetual Bermudan or American option [bichuch2025price, capponi2025optimal] to propose a valuation framework based on the theory of diffusion processes and last passage time. The core rationale for this approach is the "reset" property of Constant Function Market Makers: if an LP provides liquidity at a specific price pp, the associated IL returns to zero whenever the market price revisits that entry level.

We argue that it is economically rational for an LP to withdraw liquidity when the pool price reaches the entry price pp for the final time. Under this rule, the LP’s realized IL is minimized (approaching zero) while the duration of liquidity provision is maximized, allowing for optimal compensation through transaction fee collection. Although a last passage time is not a stopping time—making its real-time implementation more subtle than traditional rules—its distribution and associated statistics are well-characterized by the transition densities of diffusion processes.

For the purpose of clear exposition, we assume the pool price PtP\_{t} follows a geometric Brownian motion (GBM):

|  |  |  |
| --- | --- | --- |
|  | d​PtPt=μ​d​t+σ​d​Wt\frac{dP\_{t}}{P\_{t}}=\mu dt+\sigma dW\_{t} |  |

where μ\mu and σ>0\sigma>0 are constants and WtW\_{t} is a standard Brownian motion. The LP is compensated by a transaction fee at a constant rate φ\varphi. Consequently, the LP’s discounted P&L up to a random time τ\tau is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −e−r​τ​IL​(Pτ|P0,L)+∫0τe−r​t​φ​𝑑t=−e−r​τ​IL​(Pτ|P0,L)+φr​(1−e−r​τ),-e^{-r\tau}\mathrm{IL}(P\_{\tau}|P\_{0},L)+\int\_{0}^{\tau}e^{-rt}\varphi dt=-e^{-r\tau}\mathrm{IL}(P\_{\tau}|P\_{0},L)+\frac{\varphi}{r}(1-e^{-r\tau}), |  | (24) |

where the first term represents the discounted loss realized upon exiting the position and the second term represents the accumulated discounted fees.

### 4.1. Transiency and the Last Passage Time

To analyze the behavior of the last passage time, we first characterize the long-term asymptotic properties of the pool price process PtP\_{t}. The scale function s​(p)s(p) for the geometric Brownian motion defined in the market model is given by:

|  |  |  |
| --- | --- | --- |
|  | s​(p)=11−α​(p1−α−1),s(p)=\frac{1}{1-\alpha}\left(p^{1-\alpha}-1\right), |  |

where α=2​μσ2≠1\alpha=\frac{2\mu}{\sigma^{2}}\neq 1. The transiency of the process depends on the relationship between the drift μ\mu and the volatility σ\sigma:

* •

  Downward Transient: If μ<σ22\mu<\frac{\sigma^{2}}{2} (i.e., α<1\alpha<1), then s​(0+)=1α−1>−∞s(0+)=\frac{1}{\alpha-1}>-\infty and s​(∞)=∞s(\infty)=\infty. In this regime, the process PtP\_{t} is transient toward zero, such that ℙ​[limt→∞Pt=0∣P0=p]=1\mathbb{P}\left[\lim\_{t\to\infty}P\_{t}=0\mid P\_{0}=p\right]=1 for all p∈(0,∞)p\in(0,\infty).
* •

  Upward Transient: If μ>σ22\mu>\frac{\sigma^{2}}{2} (i.e., α>1\alpha>1), then s​(0+)=−∞s(0+)=-\infty and s​(∞)=1α−1<∞s(\infty)=\frac{1}{\alpha-1}<\infty. Here, the process PtP\_{t} is transient toward infinity, with ℙ​[limt→∞Pt=∞∣P0=p]=1\mathbb{P}\left[\lim\_{t\to\infty}P\_{t}=\infty\mid P\_{0}=p\right]=1 for all p∈(0,∞)p\in(0,\infty).

For any ϵ∈ℝ\epsilon\in\mathbb{R}, we define the last passage time πϵ\pi^{\epsilon} at the price level P0​eϵP\_{0}e^{\epsilon} as:

|  |  |  |
| --- | --- | --- |
|  | πϵ:=sup{t≥0:Pt=P0​eϵ}=sup{t≥0:ν​t+σ​Wt=ϵ},\pi^{\epsilon}:=\sup\{t\geq 0:P\_{t}=P\_{0}e^{\epsilon}\}=\sup\{t\geq 0:\nu t+\sigma W\_{t}=\epsilon\}, |  |

where ν=μ−σ22\nu=\mu-\frac{\sigma^{2}}{2}. By convention, πϵ=0\pi^{\epsilon}=0 if the process PtP\_{t} never visits the price level P0​eϵP\_{0}e^{\epsilon}. In the critical case where μ=σ22\mu=\frac{\sigma^{2}}{2}, the process is recurrent, and the last passage time πϵ=∞\pi^{\epsilon}=\infty almost surely for all ϵ∈ℝ\epsilon\in\mathbb{R}.

In the subsequent analysis, we focus on the case μ>σ22\mu>\frac{\sigma^{2}}{2} (upward transient), noting that the results for the downward transient case μ<σ22\mu<\frac{\sigma^{2}}{2} can be obtained by symmetry.

### 4.2. Optimal Withdrawal Strategy

In the upward transient regime where μ>σ22\mu>\frac{\sigma^{2}}{2} (and thus ν=μ−σ22>0\nu=\mu-\frac{\sigma^{2}}{2}>0), we identify the log-exit price ϵ\epsilon that maximizes the liquidity provider’s returns. The expected discounted P&L, v​(ϵ)v(\epsilon), is defined as the difference between accumulated transaction fees and the realized impermanent loss at the last passage time πϵ\pi^{\epsilon}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(ϵ)\displaystyle v(\epsilon) | :=𝔼ℚ​[−e−r​πϵ​IL​(Pπϵ|P0,L)+φr​(1−e−r​πϵ)∣P0]\displaystyle:=\mathbb{E}^{\mathbb{Q}}\left[-e^{-r\pi^{\epsilon}}\mathrm{IL}(P\_{\pi^{\epsilon}}|P\_{0},L)+\frac{\varphi}{r}\left(1-e^{-r\pi^{\epsilon}}\right)\mid P\_{0}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =φr−{∫P0P0​eϵ(P0​eϵ−q)​L​(q)​𝑑q+φr}​ϕϵ​(r),\displaystyle=\frac{\varphi}{r}-\left\{\int^{P\_{0}e^{\epsilon}}\_{P\_{0}}(P\_{0}e^{\epsilon}-q)L(q)dq+\frac{\varphi}{r}\right\}\phi\_{\epsilon}(r), |  | (25) |

where ϕϵ​(r)\phi\_{\epsilon}(r) is the moment generating function of the last passage time πϵ\pi^{\epsilon}. Following [egami2025decomposition, (36) on p.12] or [profeta2010option, (2.25) on p.28], the function ϕϵ​(r)\phi\_{\epsilon}(r) is given by:

|  |  |  |
| --- | --- | --- |
|  | ϕϵ​(r)={νν2+2​r​σ2​eϵσ2​(ν−ν2+2​r​σ2) if ​ϵ≥0;1−e2​νσ2​ϵ+νν2+2​r​σ2​eϵσ2​(ν+ν2+2​r​σ2) if ​ϵ<0.\phi\_{\epsilon}(r)=\left\{\begin{array}[]{ll}\displaystyle\frac{\nu}{\sqrt{\nu^{2}+2r\sigma^{2}}}\,e^{\frac{\epsilon}{\sigma^{2}}\left(\nu-\sqrt{\nu^{2}+2r\sigma^{2}}\right)}&\mbox{ if }\epsilon\geq 0;\\ &\\ \displaystyle 1-e^{\frac{2\nu}{\sigma^{2}}\epsilon}+\frac{\nu}{\sqrt{\nu^{2}+2r\sigma^{2}}}\,e^{\frac{\epsilon}{\sigma^{2}}\left(\nu+\sqrt{\nu^{2}+2r\sigma^{2}}\right)}&\mbox{ if }\epsilon<0.\end{array}\right. |  |

The value v​(0)v(0) represents the expected P&L if the LP withdraws at the final moment the price revisits the initial entry level P0P\_{0}.

#### 4.2.1. Analytic Characterization of the Optimal Exit

The determination of the optimal exit level ϵ∗\epsilon^{\*} depends on the sign of the derivative v′​(ϵ)v^{\prime}(\epsilon):

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | v′​(ϵ)\displaystyle v^{\prime}(\epsilon) | =\displaystyle= | ν​(ν2+2​r​σ2−ν)σ2​ν2+2​r​σ2eϵσ2​(ν−ν2+2​r​σ2)×\displaystyle\frac{\nu\left(\sqrt{\nu^{2}+2r\sigma^{2}}-\nu\right)}{\sigma^{2}\sqrt{\nu^{2}+2r\sigma^{2}}}e^{\frac{\epsilon}{\sigma^{2}}\left(\nu-\sqrt{\nu^{2}+2r\sigma^{2}}\right)}\times |  | (26) |
|  |  |  | {ν2+2​r​σ2−ν−σ2ν2+2​r​σ2−ν​P0​eϵ​∫P0P0​eϵL​(q)​𝑑q−∫P0P0​eϵq​L​(q)​𝑑q+φr}.\displaystyle\left\{\frac{\sqrt{\nu^{2}+2r\sigma^{2}}-\nu-\sigma^{2}}{\sqrt{\nu^{2}+2r\sigma^{2}}-\nu}\,P\_{0}e^{\epsilon}\int^{P\_{0}e^{\epsilon}}\_{P\_{0}}L(q)dq-\int^{P\_{0}e^{\epsilon}}\_{P\_{0}}qL(q)dq+\frac{\varphi}{r}\right\}. |  |

Note that v′​(0+)=limϵ→0+v′​(ϵ)=−νσ2​ν2+2​r​σ2​φr​(ν−ν2+2​r​σ2)>0v^{\prime}(0^{+})=\lim\_{\epsilon\to 0^{+}}v^{\prime}(\epsilon)=-\frac{\nu}{\sigma^{2}\sqrt{\nu^{2}+2r\sigma^{2}}}\frac{\varphi}{r}(\nu-\sqrt{\nu^{2}+2r\sigma^{2}})>0, indicating that vv is increasing to the right of the origin.

Utilizing the identity ν2+2​r​σ2−(σ2+ν)2=2​(r−μ)​σ2\nu^{2}+2r\sigma^{2}-(\sigma^{2}+\nu)^{2}=2(r-\mu)\sigma^{2}, the behavior of v​(ϵ)v(\epsilon) is categorized by the relationship between the drift μ\mu and the discount rate rr:

1. (1)

   Asymptotic Maximization (μ<r\mu<r): If the bracketed term in ([26](#S4.E26 "In 4.2.1. Analytic Characterization of the Optimal Exit ‣ 4.2. Optimal Withdrawal Strategy ‣ 4. Pricing via Last Passage Time ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) remains positive for all ϵ>0\epsilon>0, vv is monotonically increasing. This typically occurs when μ<r\mu<r, as the first term in the brackets is positive and increasing. In this regime, the LP optimally maintains the position indefinitely, with the expected P&L approaching the supremum φr\frac{\varphi}{r} as ϵ→∞\epsilon\to\infty.
2. (2)

   Unique Interior Maximizer (μ≥r\mu\geq r): If a unique ϵ∗>0\epsilon^{\*}>0 exists such that v′​(ϵ∗)=0v^{\prime}(\epsilon^{\*})=0, then vv is maximized at this point. This uniqueness is guaranteed for μ≥r\mu\geq r because the first term in the brackets decreases toward −∞-\infty as ϵ→∞\epsilon\to\infty.

When μ=r\mu=r, the identity ν+σ2−ν2+2​r​σ2=0\nu+\sigma^{2}-\sqrt{\nu^{2}+2r\sigma^{2}}=0 holds. Consequently, the first-order condition v′​(ϵ)=0v^{\prime}(\epsilon)=0 simplifies to ∫P0P0​eϵq​L​(q)​𝑑q=φr\int\_{P\_{0}}^{P\_{0}e^{\epsilon}}qL(q)\,dq=\frac{\varphi}{r}. This yields the explicit solution:

|  |  |  |
| --- | --- | --- |
|  | P0​eϵ∗=y−1​(φr−y​(P0)),P\_{0}e^{\epsilon^{\*}}=y^{-1}\left(\frac{\varphi}{r}-y(P\_{0})\right), |  |

where y​(⋅)y(\cdot) is the reserve function defined in ([4](#S2.E4 "In 2.2. Liquidity Profile and Reserves ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")). These results are summarized in Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.2.1. Analytic Characterization of the Optimal Exit ‣ 4.2. Optimal Withdrawal Strategy ‣ 4. Pricing via Last Passage Time ‣ Pricing and hedging for liquidity provision in Constant Function Market Making").

###### Theorem 4.1.

Let the pool price PtP\_{t} follow the geometric Brownian motion d​PtPt=μ​d​t+σ​d​Wt\frac{dP\_{t}}{P\_{t}}=\mu dt+\sigma dW\_{t}, with σ>0\sigma>0 and μ>σ22\mu>\frac{\sigma^{2}}{2}. The expected discounted P&L v​(ϵ)v(\epsilon), stopped at the last passage time πϵ\pi^{\epsilon} of the price level P0​eϵP\_{0}e^{\epsilon}, is given by:

|  |  |  |
| --- | --- | --- |
|  | v​(ϵ)=𝔼ℚ​[−e−r​πϵ​IL​(Pπϵ|P0,L)+φr​(1−e−r​πϵ)∣P0].v(\epsilon)=\mathbb{E}^{\mathbb{Q}}\left[-e^{-r\pi^{\epsilon}}\mathrm{IL}(P\_{\pi^{\epsilon}}|P\_{0},L)+\frac{\varphi}{r}(1-e^{-r\pi^{\epsilon}})\mid P\_{0}\right]. |  |

The optimal exit level ϵ∗\epsilon^{\*} is characterized as follows:

1. (1)

   If μ≥r\mu\geq r, there exists a unique maximizer ϵ∗>0\epsilon^{\*}>0 satisfying the transcendental equation:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ν2+2​r​σ2−ν−σ2ν2+2​r​σ2−ν​P0​eϵ​∫P0P0​eϵL​(q)​𝑑q−∫P0P0​eϵq​L​(q)​𝑑q+φr=0,\frac{\sqrt{\nu^{2}+2r\sigma^{2}}-\nu-\sigma^{2}}{\sqrt{\nu^{2}+2r\sigma^{2}}-\nu}P\_{0}e^{\epsilon}\int\_{P\_{0}}^{P\_{0}e^{\epsilon}}L(q)dq-\int\_{P\_{0}}^{P\_{0}e^{\epsilon}}qL(q)dq+\frac{\varphi}{r}=0, |  | (27) |

   where ν=μ−σ22\nu=\mu-\frac{\sigma^{2}}{2}.
2. (2)

   In the specific case μ=r\mu=r, the optimal exit price admits the explicit solution:

   |  |  |  |
   | --- | --- | --- |
   |  | P0​eϵ∗=y−1​(φr−y​(P0)),P\_{0}e^{\epsilon^{\*}}=y^{-1}\left(\frac{\varphi}{r}-y(P\_{0})\right), |  |

   where yy is the reserve function defined in ([4](#S2.E4 "In 2.2. Liquidity Profile and Reserves ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")).
3. (3)

   If μ<r\mu<r, v​(ϵ)v(\epsilon) may be monotonically increasing for all ϵ∈ℝ\epsilon\in\mathbb{R}, in which case ([27](#S4.E27 "In item 1 ‣ Theorem 4.1. ‣ 4.2.1. Analytic Characterization of the Optimal Exit ‣ 4.2. Optimal Withdrawal Strategy ‣ 4. Pricing via Last Passage Time ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) has no solution and vv attains its supremum φr\frac{\varphi}{r} as ϵ→∞\epsilon\to\infty.

###### Example 4.2.

Consider an initial pool price P0=1P\_{0}=1 and a liquidity profile L​(q)=e−110​|q−1|L(q)=e^{-\frac{1}{10}|q-1|}. With volatility σ=10%\sigma=10\% and fee rate φ=2%\varphi=2\%, we evaluate the optimal exit strategy under varying drift μ\mu and discount rate rr:

* •

  Case 1 (μ=2%,r=1%\mu=2\%,r=1\%): Since μ>r\mu>r, Equation ([27](#S4.E27 "In item 1 ‣ Theorem 4.1. ‣ 4.2.1. Analytic Characterization of the Optimal Exit ‣ 4.2. Optimal Withdrawal Strategy ‣ 4. Pricing via Last Passage Time ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) yields a unique finite maximizer ϵ∗≈0.65\epsilon^{\*}\approx 0.65, as seen in the left panel of Figure [1](#S4.F1 "Figure 1 ‣ Example 4.2. ‣ 4.2.1. Analytic Characterization of the Optimal Exit ‣ 4.2. Optimal Withdrawal Strategy ‣ 4. Pricing via Last Passage Time ‣ Pricing and hedging for liquidity provision in Constant Function Market Making").
* •

  Case 2 (μ=2%,r=3%\mu=2\%,r=3\%): Despite μ<r\mu<r, the specific interplay of parameters allows for a unique interior maximizer ϵ∗≈0.45\epsilon^{\*}\approx 0.45, illustrated in the middle panel of Figure [1](#S4.F1 "Figure 1 ‣ Example 4.2. ‣ 4.2.1. Analytic Characterization of the Optimal Exit ‣ 4.2. Optimal Withdrawal Strategy ‣ 4. Pricing via Last Passage Time ‣ Pricing and hedging for liquidity provision in Constant Function Market Making").
* •

  Case 3 (μ=1%,r=4%\mu=1\%,r=4\%): Here, the drift is significantly lower than the discount rate. The equation has no solution, and v​(ϵ)v(\epsilon) increases toward its supremum φr=0.5\frac{\varphi}{r}=0.5 as ϵ→∞\epsilon\to\infty, shown in the right panel of Figure [1](#S4.F1 "Figure 1 ‣ Example 4.2. ‣ 4.2.1. Analytic Characterization of the Optimal Exit ‣ 4.2. Optimal Withdrawal Strategy ‣ 4. Pricing via Last Passage Time ‣ Pricing and hedging for liquidity provision in Constant Function Market Making").

![[Uncaptioned image]](2603.01344v1/fig/optimal_exit-1.png)

![[Uncaptioned image]](2603.01344v1/fig/optimal_exit-2.png)

![[Uncaptioned image]](2603.01344v1/fig/optimal_exit-3.png)

Figure 1. The expected P&L v​(ϵ)v(\epsilon) defined in ([27](#S4.E27 "In item 1 ‣ Theorem 4.1. ‣ 4.2.1. Analytic Characterization of the Optimal Exit ‣ 4.2. Optimal Withdrawal Strategy ‣ 4. Pricing via Last Passage Time ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) as a function of the log-exit price ϵ\epsilon. Left (Case 1): A unique maximizer ϵ∗>0\epsilon^{\*}>0 exists because μ>r\mu>r. Middle (Case 2): A unique interior maximizer exists despite μ<r\mu<r, due to the interplay of fee income and last-passage statistics. Right (Case 3): v​(ϵ)v(\epsilon) increases monotonically toward the supremum φr=0.5\frac{\varphi}{r}=0.5 as ϵ→∞\epsilon\to\infty, indicating an optimal strategy of never withdrawing.

## 5. Data and Numerical Implementation

In this section, we present empirical results on the fine structure of implied volatility for Uniswap V3 liquidity profiles, utilizing the framework developed in Section [3](#S3 "3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making"). The central advancement of this framework is the impermanent loss (IL) replication formula ([10](#S3.E10 "In 3.1. Static Replication of Impermanent Loss by Vanilla Options ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")), which characterizes IL as a weighted strip of vanilla options. For a liquidity profile L​(q)=ℓ​(q)/(2​q3/2)L(q)=\ell(q)/(2q^{3/2}), we can assign an implied volatility to any liquidity provision by equating the option-implied IL price to its corresponding model price under Black-Scholes or Bachelier dynamics.

A primary advantage of this canonical parametrization is that it enables a direct economic comparison across disparate liquidity pools. Specifically, pools with varying fee tiers or liquidity concentrations can be evaluated on a unified basis of implied volatility. In the following analysis, we compare Black-Scholes and Bachelier implied volatilities across multiple expiries and fee tiers using market data.

### 5.1. Data Sources and Collection

This subsection details the empirical data acquisition process required to synthesize the market-side IL integral and reconstruct the corresponding liquidity profiles.

#### 5.1.1. Option Data

European option quotes for ETH are obtained from the Deribit exchange through its public API. For each hourly snapshot, the following data points are collected:

* •

  Bid-ask mid prices: Prices for both call and put options are gathered across the full spectrum of available strikes.
* •

  Quarterly expiries: The dataset includes four specific expiries: December 2025, March 2026, June 2026, and September 2026.
* •

  Forward Price and Maturity: We collect the underlying reference forward price FF (Deribit underlying\_price) and the time to maturity TT in years for each respective expiry.

Let P0P\_{0} denote the Uniswap pool spot price at the snapshot, and let FF denote the Deribit maturity-TT reference forward used for the option surface. In our pipeline, P0P\_{0} is used only to implement the IL replication split in ([20](#S3.E20 "In 3.3.1. Pricing IL as a European-Style Contingent Claim ‣ 3.3. Risk Neutral Pricing and Hedging for Impermanent Loss ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) (i.e., the boundary between the put and call legs), while FF is used for put–call parity, model option prices, and the log-moneyness coordinate x=log⁡(K/F)x=\log(K/F). Consequently, the IL split point K=P0K=P\_{0} corresponds to x=log⁡(P0/F)x=\log(P\_{0}/F) on the plots.

#### 5.1.2. Liquidity Data

On-chain liquidity profiles are extracted directly from the Uniswap V3 ETH/USDC pool contracts. For each snapshot, the following parameters are queried:

* •

  Tick Data: All initialized ticks and their corresponding signed liquidity deltas Δ​ℓi\Delta\ell\_{i}.
* •

  Pool State: The pool’s current tick, reported in-range liquidity ℓcurr\ell\_{\mathrm{curr}}, and the pool price P0P\_{0}.

The intrinsic liquidity ℓ​(q)\ell(q)—representing active in-range liquidity at price qq—is reconstructed by aggregating the signed tick deltas. Here, Δ​ℓi\Delta\ell\_{i} corresponds to the pool’s liquidityNet, representing the change in active liquidity as the price crosses tick tit\_{i} upward [uniswap2023math]. To fix the additive constant of the cumulative sum, the profile is anchored to the reported in-range liquidity ℓcurr\ell\_{\mathrm{curr}} at the current tick t0t\_{0}, setting ℓ​(P0−)=ℓcurr\ell(P\_{0}^{-})=\ell\_{\mathrm{curr}}.

The analysis focuses on two ETH/USDC pools with fee tiers of 5 basis points (5bp) and 30 basis points (30bp). These pools allow for a contrast between tight liquidity concentration (5bp) and broader spatial distributions (30bp). The main-text empirical results use the November 17, 2025 snapshot, while additional weekly snapshots are reported in Appendix [D](#A4 "Appendix D Additional Snapshot Overlays ‣ Pricing and hedging for liquidity provision in Constant Function Market Making").

### 5.2. Data Cleaning and Processing

#### 5.2.1. Option Data Cleaning

To ensure the integrity of the market-side IL integrals, raw option quotes from Deribit are subjected to standard no-arbitrage filters as recommended by CBOE [cboe2019options]. The following constraints are applied:

* •

  Positive Prices: All quotes with non-positive mid prices are removed.
* •

  Monotonicity: Call prices must be non-increasing with respect to the strike, while put prices must be non-decreasing.
* •

  Convexity: To prevent butterfly arbitrage, the second difference in prices relative to the strike must be non-negative (i.e., C​(Ki−1)−2​C​(Ki)+C​(Ki+1)≥0C(K\_{i-1})-2C(K\_{i})+C(K\_{i+1})\geq 0).

In our analyzed snapshots, OTM quotes passed these filters after positive-price filtering. ITM coverage gaps, where arbitrage violations are more common, are addressed implicitly via put–call parity.

#### 5.2.2. Interpolation and Synthetic Pricing

The integration variable is identified with the strike KK (measured in USD per ETH), which aligns with the price axis qq used in the liquidity profile. Between observed strikes, option prices are linearly interpolated. For strikes K∈[Ki,Ki+1]K\in[K\_{i},K\_{i+1}] with observed prices CiC\_{i} and Ci+1C\_{i+1}, the call price is given by:

|  |  |  |
| --- | --- | --- |
|  | C​(K)=Ci+Ci+1−CiKi+1−Ki​(K−Ki).C(K)=C\_{i}+\frac{C\_{i+1}-C\_{i}}{K\_{i+1}-K\_{i}}(K-K\_{i}). |  |

This piecewise linear representation, when combined with the piecewise constant liquidity profile derived from the Uniswap tick structure, allows for the use of closed-form antiderivatives for the IL integrals. Specifically, on any interval [a,b][a,b] where ℓ\ell is constant, thus L​(q)=ℓ/(2​q3/2)L(q)=\ell/(2q^{3/2}), and the option price O​(q)=a0+a1​qO(q)=a\_{0}+a\_{1}q is linear:

|  |  |  |
| --- | --- | --- |
|  | ∫abL​(q)​O​(q),d​q=ℓ2​[−2​a0q+2​a1​q]ab.\int\_{a}^{b}L(q)O(q),dq=\frac{\ell}{2}\left[-\frac{2a\_{0}}{\sqrt{q}}+2a\_{1}\sqrt{q}\right]\_{a}^{b}. |  |

This analytic approach completely sidesteps numerical quadrature noise. The piecewise-linear interpolant is the pointwise maximal arbitrage-free fill-in between observed strikes [cohen2020detecting]. Since L​(q)L(q) is positive, this upper bound on the market price translates into a conservative benchmark for the subsequent implied-volatility inversion.

Higher-order spline interpolation is avoided for two reasons [lefloch2020arbitrage]:

* •

  Static Arbitrage: Splines are not necessarily shape-preserving and can violate the convexity constraints required to exclude butterfly arbitrage [wystup2017arbitrage].
* •

  Numerical Ringing: Cubic splines may overshoot between knots, and these artifacts can be amplified into spurious high-frequency oscillations in the implied volatility curve during the nonlinear inversion process.

##### Synthetic option pricing.

When strike coverage on one side of the market is sparse, missing prices are synthesized from the better-covered side using put–call parity. With r=0r=0, this is C​(K)−P​(K)=F−KC(K)-P(K)=F-K (equivalently, P=C−F+KP=C-F+K and C=P+F−KC=P+F-K). This approach guarantees continuous coverage across the integration domain while preserving no-arbitrage conditions, as put–call parity is an exact identity.

The threshold for switching to synthetic pricing is a local strike gap of 500 USD or more. This data-coverage heuristic reflects the transition from dense near-ATM strike spacing on Deribit (typically 25–50 USD) to sparse deep-OTM spacing (500 USD or more). We found this to be a stable cutoff across expiries in our snapshot. When gaps exceed this threshold, linear interpolation becomes unreliable, and we instead rely on the synthetic prices derived from the more liquid side of the market.

##### Market Proxy vs. Model Prices.

Our empirical pipeline utilizes two distinct objects to facilitate the implied-volatility inversion:

* •

  Market Proxy (O^mkt​(K)\widehat{O}^{\rm mkt}(K)): This is constructed from discrete market option quotes via no-arbitrage cleaning and piecewise-linear interpolation. It is used exclusively to evaluate the market-side IL integrals. We maintain this evaluation as analytically as possible by using closed-form antiderivatives to avoid injecting numerical quadrature noise into the subsequent inversion process.
* •

  Model Option Prices (OBS​(K;σ)O^{\rm BS}(K;\sigma) and OB​(K;σ)O^{\rm B}(K;\sigma)): These are the theoretical prices used to define Black–Scholes and Bachelier implied volatilities. Inversion is performed by matching model-side and market-side IL integrals on each integration bin at the chosen resolution.

By partitioning the integration domain at all Uniswap V3 tick boundaries, strike knots, and the split point P0P\_{0}, we ensure that the intrinsic liquidity ℓ\ell remains constant and the market proxy remains affine on each segment. This structure allows for an exact closed-form evaluation of the market-side integral, providing a robust and noise-free benchmark for determining the fine structure of implied volatility.

#### 5.2.3. Integration Partitioning

To maintain analytic precision, the integration domain is partitioned at every point where the integrand’s functional form changes. These boundaries include all Uniswap V3 tick limits where the intrinsic liquidity ℓ\ell shifts, all strike knots where the market proxy O^mkt​(K)\widehat{O}^{\text{mkt}}(K) undergoes a change in slope, and the spot price P0P\_{0}, which serves as the put–call split point. Because liquidity ℓ\ell remains constant and the market proxy remains affine on each resulting segment, the market-side integral admits an exact closed-form evaluation.

#### 5.2.4. Numerical Integration Details

The IL integrals, characterized by the form

|  |  |  |
| --- | --- | --- |
|  | ∫abO​(K)K3/2​𝑑K,\int\_{a}^{b}\frac{O(K)}{K^{3/2}}\,dK, |  |

are evaluated using strategies tailored to the specific model dynamics. For market prices and the Black–Scholes model (r=0r=0), we utilize piecewise linear interpolation and closed-form antiderivatives for

|  |  |  |
| --- | --- | --- |
|  | ∫abCBS​(K;σ)K3/2​𝑑K\int\_{a}^{b}\frac{C\_{\mathrm{BS}}(K;\sigma)}{K^{3/2}}\,dK |  |

to avoid injecting numerical quadrature noise into the evaluation. In the Bachelier model, where the auxiliary term involving Φ​(d​(K))/K\Phi(d(K))/\sqrt{K} lacks an elementary antiderivative, we employ a hybrid approach: exact boundary terms are combined with 32-point Gauss–Legendre quadrature on the smooth remainder. This semi-closed-form method ensures machine-precision accuracy across each segment; see Appendix [B](#A2 "Appendix B Numerical Integration for Bachelier IL ‣ Pricing and hedging for liquidity provision in Constant Function Market Making") for the derivation and numerical validation.

#### 5.2.5. Interest Rate Convention

In accordance with Deribit exchange conventions, the risk-free rate is set to r=0r=0 throughout the implementation. This is consistent with the theoretical assumption of equal interest rates for both tokens in the pool in Section [3](#S3 "3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making"). While the empirical forward price FF is used for model pricing and put–call parity identities, the pool price P0P\_{0} is used exclusively as the boundary to split the integral between put and call terms in ([20](#S3.E20 "In 3.3.1. Pricing IL as a European-Style Contingent Claim ‣ 3.3. Risk Neutral Pricing and Hedging for Impermanent Loss ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")).

### 5.3. Implied Volatility Computation (Multi-Resolution)

Let x:=log⁡(K/F)x:=\log(K/F) denote log-moneyness (identifying the integration variable qq with strike KK). For a given resolution nn, we define a partition
x0<x1<⋯<xnx\_{0}<x\_{1}<\cdots<x\_{n} and corresponding bins
Bn,k:={K:x​(K)∈[xk−1,xk)}B\_{n,k}:=\{K:x(K)\in[x\_{k-1},x\_{k})\}, k=1,…,nk=1,\dots,n.
In practice, the partition is taken as a coarsening of the finest initialized-tick partition, obtained by aggregating adjacent tick buckets into nn bins.
We then restrict the liquidity profile LL to each bin via

|  |  |  |
| --- | --- | --- |
|  | Ln,k​(K):=L​(K)​𝟙{K∈Bn,k}.L\_{n,k}(K):=L(K)\mathbbm{1}\_{\{K\in B\_{n,k}\}}. |  |

For each bin we compute Black–Scholes and Bachelier implied volatilities
σn,kBS\sigma^{\rm BS}\_{n,k} and σn,kB\sigma^{\rm B}\_{n,k} by matching model and market IL prices:

|  |  |  |
| --- | --- | --- |
|  | ∫Ln,k​(K)​O^mkt​(K)​𝑑K=∫Ln,k​(K)​OBS​(K;σn,kBS)​𝑑K,\int L\_{n,k}(K)\,\widehat{O}^{\rm mkt}(K)\,dK=\int L\_{n,k}(K)\,O^{\rm BS}(K;\sigma^{\rm BS}\_{n,k})\,dK, |  |

and the same for Bachelier. By Proposition [3.6](#S3.Thmtheorem6 "Proposition 3.6 (Existence and Uniqueness of Implied Volatility). ‣ 3.3.2. Implied Volatility for Liquidity Profile ‣ 3.3. Risk Neutral Pricing and Hedging for Impermanent Loss ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making"), each equation admits a unique solution because the combined put+call map is strictly increasing in σ\sigma. We solve by bisection and do not invert put and call components separately.

We report multiple resolutions n∈{1,3,6,12,N}n\in\{1,3,6,12,N\}, where NN is the finest initialized-tick partition. The Black–Scholes IV is reported as an annualized volatility level, and the Bachelier IV is normalized as

|  |  |  |
| --- | --- | --- |
|  | σ¯B:=σB/P0,\bar{\sigma}\_{\rm B}:=\sigma\_{\rm B}/P\_{0}, |  |

matching the scale used in the multi-resolution overlay figures.

### 5.4. Empirical Results: Multi-Resolution Implied Volatility

The main-text empirical results use the November 17, 2025 snapshot for both 5bp and 30bp ETH/USDC pools. Additional weekly snapshots are reported in the Appendix [D](#A4 "Appendix D Additional Snapshot Overlays ‣ Pricing and hedging for liquidity provision in Constant Function Market Making") as robustness checks.

#### 5.4.1. Liquidity Concentration and IL Contribution

Figures [2](#S5.F2 "Figure 2 ‣ 5.4.1. Liquidity Concentration and IL Contribution ‣ 5.4. Empirical Results: Multi-Resolution Implied Volatility ‣ 5. Data and Numerical Implementation ‣ Pricing and hedging for liquidity provision in Constant Function Market Making") and [3](#S5.F3 "Figure 3 ‣ 5.4.1. Liquidity Concentration and IL Contribution ‣ 5.4. Empirical Results: Multi-Resolution Implied Volatility ‣ 5. Data and Numerical Implementation ‣ Pricing and hedging for liquidity provision in Constant Function Market Making") report IL contribution for a representative expiry (March 2026) in each fee tier. In this snapshot, the 5bp pool concentrates weight more tightly near P0P\_{0}, while the 30bp pool distributes weight more broadly.

![[Uncaptioned image]](2603.01344v1/fig/iv_smile_dual_20251117T000001_2026-03-27_30bps.png)

Figure 2. IL contribution for the 30bp ETH/USDC pool (Nov 17, 2025 snapshot; representative expiry). The left column reports IL contribution; the remaining columns show the corresponding single-resolution IV outputs from the shared plotting routine.

![[Uncaptioned image]](2603.01344v1/fig/iv_smile_dual_20251117T000001_2026-03-27_5bps.png)

Figure 3. IL contribution for the 5bp ETH/USDC pool (Nov 17, 2025 snapshot; representative expiry). The left column reports IL contribution; the remaining columns show the corresponding single-resolution IV outputs from the shared plotting routine.

Having established how each fee tier loads the IL strip, we now turn to the implied-volatility surfaces obtained by equating IL prices across models.

Figures [4](#S5.F4 "Figure 4 ‣ 5.4.1. Liquidity Concentration and IL Contribution ‣ 5.4. Empirical Results: Multi-Resolution Implied Volatility ‣ 5. Data and Numerical Implementation ‣ Pricing and hedging for liquidity provision in Constant Function Market Making") and [5](#S5.F5 "Figure 5 ‣ 5.4.1. Liquidity Concentration and IL Contribution ‣ 5.4. Empirical Results: Multi-Resolution Implied Volatility ‣ 5. Data and Numerical Implementation ‣ Pricing and hedging for liquidity provision in Constant Function Market Making") overlay implied-volatility curves across resolutions n∈{1,3,6,12,N}n\in\{1,3,6,12,N\} for four expiries (columns). The top row shows Black–Scholes IV and the bottom row shows normalized Bachelier IV σ¯B=σB/P0\bar{\sigma}\_{\rm B}=\sigma\_{\rm B}/P\_{0}.

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251117T000001_30bps_plasma.png)

Figure 4. Multi-resolution implied-volatility overlay for the 30bp ETH/USDC pool (Nov 17, 2025 snapshot). Curves correspond to n∈{1,3,6,12,N}n\in\{1,3,6,12,N\}, with NN the finest initialized-tick partition. Columns are quarterly expiries; rows are Black–Scholes IV (top) and normalized Bachelier IV σ¯B=σB/P0\bar{\sigma}\_{\rm B}=\sigma\_{\rm B}/P\_{0} (bottom).

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251117T000001_5bps_plasma.png)

Figure 5. Multi-resolution implied-volatility overlay for the 5bp ETH/USDC pool (Nov 17, 2025 snapshot). Fine-scale oscillations are most visible at n=Nn=N, while coarser aggregations (e.g., n=6n=6 and n=12n=12) recover a stable macro smile/skew structure.

The overlays support four robust empirical findings:

* •

  Scale separation: the macro smile and skew are already visible at coarse resolutions and remain qualitatively stable as nn increases.
* •

  Microstructure concentration: high-frequency wiggles are concentrated at the finest resolution, consistent with small-bin conditioning effects rather than large economic regime shifts.
* •

  Term structure: near-dated expiries show stronger curvature, while longer-dated expiries are flatter in both Black–Scholes and Bachelier representations.
* •

  Fee-tier comparison: the 5bp pool exhibits finer native structure at n=Nn=N, but at matched coarse resolution (e.g., n=12n=12) the 5bp and 30bp smiles are closely aligned. This coincides with tighter IL concentration in Figures [2](#S5.F2 "Figure 2 ‣ 5.4.1. Liquidity Concentration and IL Contribution ‣ 5.4. Empirical Results: Multi-Resolution Implied Volatility ‣ 5. Data and Numerical Implementation ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")–[3](#S5.F3 "Figure 3 ‣ 5.4.1. Liquidity Concentration and IL Contribution ‣ 5.4. Empirical Results: Multi-Resolution Implied Volatility ‣ 5. Data and Numerical Implementation ‣ Pricing and hedging for liquidity provision in Constant Function Market Making"), which can make small-bin inversions more sensitive.

### 5.5. Summary Statistics

Under the multi-resolution framing, extreme min/max values at the native finest partition are sensitive to microstructure and are not the preferred primary summary for economic interpretation. We therefore emphasize the cross-resolution overlays in Figures [4](#S5.F4 "Figure 4 ‣ 5.4.1. Liquidity Concentration and IL Contribution ‣ 5.4. Empirical Results: Multi-Resolution Implied Volatility ‣ 5. Data and Numerical Implementation ‣ Pricing and hedging for liquidity provision in Constant Function Market Making") and [5](#S5.F5 "Figure 5 ‣ 5.4.1. Liquidity Concentration and IL Contribution ‣ 5.4. Empirical Results: Multi-Resolution Implied Volatility ‣ 5. Data and Numerical Implementation ‣ Pricing and hedging for liquidity provision in Constant Function Market Making"); additional weekly snapshots are provided in Appendix [D](#A4 "Appendix D Additional Snapshot Overlays ‣ Pricing and hedging for liquidity provision in Constant Function Market Making").

### 5.6. Key Takeaways

The empirical analysis of multi-resolution implied volatility yields several significant conclusions regarding the pricing of liquidity provision in Uniswap V3:

1. (1)

   Persistence of the Volatility Smile: The IL-implied volatility exhibits the characteristic "smile" shape prevalent in traditional options markets, with elevated IV for out-of-the-money strikes on both sides. This confirms that the option-based replication formula ([10](#S3.E10 "In 3.1. Static Replication of Impermanent Loss by Vanilla Options ‣ 3. Pricing and Hedging for General Liquidity Profiles ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) effectively inherits the market’s complex view on price dynamics and tail risk.
2. (2)

   Model Convergence near ATM: Near the money, Black–Scholes IV and normalized Bachelier IV are closely aligned; divergence is primarily a wing effect.
3. (3)

   Term Structure Dynamics: The overlays reveal systematic maturity smoothing: near-term expiries exhibit stronger smile curvature, while longer-term expiries are flatter.
4. (4)

   Decoupling of Fee Tiers and Economic Risk: While the 5bp and 30bp pools have very different native bucket granularity, their coarse-resolution smiles remain close. This indicates fee tiers primarily reshape liquidity placement rather than the market-implied level of economic risk.
5. (5)

   Unified Cross-Pool Comparison: The canonical parametrization using (P,ℓ)(P,\ell) enables direct comparison across fee tiers and resolutions. The persistence of similar coarse-scale IV levels across pools suggests LP risk is largely a market-level property.
6. (6)

   Level: The inferred Black–Scholes IV levels are consistent with the Deribit option surface used as input in our snapshots.

## 6. Conclusion and Discussion

We have demonstrated in this article that the canonical parametrization of the bonding curve in a CFMM, as established in ([4](#S2.E4 "In 2.2. Liquidity Profile and Reserves ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")), provides a robust and convenient framework for addressing several key problems in decentralized finance. Specifically, this formulation enables:

* •

  Risk-Neutral Pricing and Hedging: The derivation of fair values and sensitivities (Delta, Gamma, Vega) for both pool value and impermanent loss.
* •

  Implied Volatility Fine Structure: The assignment of model-implied volatilities to discrete liquidity segments, allowing for a granular assessment of risk across the price spectrum.
* •

  Loss-Versus-Rebalancing (LVR): A generalized understanding of the non-hedgeable costs of liquidity provision as a time-integral of quadratic variation weighted by the liquidity profile.
* •

  Path-Dependent Analysis: The pricing of impermanent loss using the last-passage time theory, which accounts for the "reset" property of CFMM positions.

Numerical examples utilizing market data from Uniswap V3 ETH/USDC pools and Deribit option markets validate these methodologies. Our empirical results confirm a volatility smile consistent with crypto-asset dynamics and demonstrate that while fee tiers alter the structural concentration of liquidity, the underlying economic risk remains consistent across the market.

Throughout this work, except for the numerical analysis, liquidity profiles have been treated as static. In practice, while the intrinsic liquidity profile ℓ\ell is observable on-chain, its evolution is dynamic, driven by block-level validation and LP activity. This observation motivates the shift toward statistical and dynamical modeling of liquidity surfaces. Preliminary empirical analyses of the temporal evolution of these profiles can be found in [risk2025dynamics].

Furthermore, the parametrization in ([4](#S2.E4 "In 2.2. Liquidity Profile and Reserves ‣ 2. Intrinsic Liquidity and Liquidity Profile ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")) provides a foundation for developing market models that are fully consistent with the CFMM mechanism. By accounting for the dual nature of pool updates—where trades move the state along the bonding curve while LP additions or withdrawals shift the curve itself—the evolution of the pool state (xt,yt,Pt)(x\_{t},y\_{t},P\_{t}) can be modeled as a dynamical system:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​xt\displaystyle dx\_{t} | =∫Pt∞𝑑Lt​(q)​𝑑q+d​Λta−d​Λtb,\displaystyle=\int\_{P\_{t}}^{\infty}dL\_{t}(q)dq+d\Lambda^{a}\_{t}-d\Lambda^{b}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​yt\displaystyle dy\_{t} | =∫0Ptq​𝑑Lt​(q)​𝑑q−Pt​(d​Λta−d​Λtb),\displaystyle=\int\_{0}^{P\_{t}}qdL\_{t}(q)dq-P\_{t}\left(d\Lambda^{a}\_{t}-d\Lambda^{b}\_{t}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Pt\displaystyle dP\_{t} | =−1Lt​(Pt)​(d​Λta−d​Λtb),\displaystyle=-\frac{1}{L\_{t}(P\_{t})}\left(d\Lambda^{a}\_{t}-d\Lambda^{b}\_{t}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Lt​(q)\displaystyle dL\_{t}(q) | ={𝒜​Lt​(q)+h​(t,q)}​d​t,\displaystyle=\left\{\mathcal{A}\,L\_{t}(q)+h(t,q)\right\}dt, |  |

where Λti\Lambda^{i}\_{t} represents cumulative trade volumes and the operator 𝒜\mathcal{A} describes the diffusive properties of liquidity over time. We refer the reader to [lee2026dynamics] for a stochastic treatment of the dynamic for LL. These equations capture the complex interplay between order flow, liquidity provision, and price formation. The comprehensive analysis of this system, particularly under stochastic noise, remains an area for future research.

## Acknowledgements

S. N. T. is grateful for the financial support from the National Science and Technology Council of Taiwan under grant 114-2115-M-007-012-MY3, "Mathematical Foundation of Automated Market Makers."

The authors used Google Gemini 3 (Flash version, March 2, 2026) to polish the manuscript’s grammar and style. All original theorems, proofs, and analyses were developed solely by the authors, who assume full responsibility for the integrity of the work.

## Appendix A Note on Interest Rates

This section details the interest rate conventions and forward price mechanics utilized in the pricing models, specifically relating them to standard Black-Scholes dynamics. We define the relevant rates as follows:

* •

  rr: The risk-free rate of the numeraire (e.g., USD).
* •

  δ\delta: The yield or staking reward of the underlying asset (e.g., ETH). This is functionally equivalent to a foreign short rate in foreign exchange (FX) market models.

The risk-neutral drift for the underlying asset under the numeraire measure is determined by the differential r−δr-\delta. Consequently, the forward price F0,TF\_{0,T} at time TT is defined by:

|  |  |  |
| --- | --- | --- |
|  | F0,T=P0​e(r−δ)​T.F\_{0,T}=P\_{0}e^{(r-\delta)T}. |  |

Under these definitions, the standard put-call parity identity holds, mirroring the convention used in FX markets:

|  |  |  |
| --- | --- | --- |
|  | C−P=e−r​T​(F0,T−K)=P0​e−δ​T−K​e−r​T.C-P=e^{-rT}(F\_{0,T}-K)=P\_{0}e^{-\delta T}-Ke^{-rT}. |  |

In the numerical implementation discussed in Section [5](#S5 "5. Data and Numerical Implementation ‣ Pricing and hedging for liquidity provision in Constant Function Market Making"), the risk-free rate is set to r=0r=0 throughout, consistent with the assumption of equal interest rates for both tokens in the pool. Under this r=δ=0r=\delta=0 assumption, the theoretical forward price FF equals the spot price S0S\_{0}. Empirically, however, the Deribit forward price (underlying\_price) may differ slightly from the Uniswap pool price P0P\_{0}; we utilize the forward FF for all pricing and parity calculations while maintaining P0P\_{0} as the put/call split point.

## Appendix B Numerical Integration for Bachelier IL

Both Black-Scholes and Bachelier models require the evaluation of integrals in the form:

|  |  |  |
| --- | --- | --- |
|  | ∫abO​(K)K3/2​𝑑K,\int\_{a}^{b}\frac{O(K)}{K^{3/2}}\,dK, |  |

where O​(K)O(K) represents an option price. Applying integration by parts with f=O​(K)f=O(K) and g′=K−3/2g^{\prime}=K^{-3/2} yields:

|  |  |  |
| --- | --- | --- |
|  | ∫abO​(K)K3/2​𝑑K=[−2​O​(K)K]ab+2​∫abO′​(K)K​𝑑K,\int\_{a}^{b}\frac{O(K)}{K^{3/2}}\,dK=\left[-\frac{2O(K)}{\sqrt{K}}\right]\_{a}^{b}+2\int\_{a}^{b}\frac{O^{\prime}(K)}{\sqrt{K}}\,dK, |  |

where the derivative O′​(K)O^{\prime}(K) is −Φ​(d)-\Phi(d) for call options and 1−Φ​(d)1-\Phi(d) for put options. Consequently, the computational problem reduces to evaluating the auxiliary integral ∫Φ​(d​(K))K​𝑑K\int\frac{\Phi(d(K))}{\sqrt{K}}dK.

### B.1. Model-Specific Analytic Properties

The feasibility of a closed-form solution depends on the underlying price dynamics:

* •

  Black-Scholes (Closed Form): In the lognormal model,

  |  |  |  |
  | --- | --- | --- |
  |  | d2​(K)=log⁡(P0/K)−12​σ2​Tσ​Td\_{2}(K)=\frac{\log(P\_{0}/K)-\tfrac{1}{2}\sigma^{2}T}{\sigma\sqrt{T}} |  |

  is proportional to log⁡K\log K. By substituting u=Ku=\sqrt{K},

  |  |  |  |
  | --- | --- | --- |
  |  | d2​(u2)=log⁡P0−2​log⁡uσ​T−σ​T2=A−B​log⁡ud\_{2}(u^{2})=\frac{\log P\_{0}-2\log u}{\sigma\sqrt{T}}-\frac{\sigma\sqrt{T}}{2}=A-B\log u |  |

  becomes linear in log⁡u\log u. The resulting integral takes the form ∫Φ​(linear)×exp⁡(linear)\int\Phi(\text{linear})\times\exp(\text{linear}), which admits an elementary antiderivative involving only Φ\Phi and exp\exp.
* •

  Bachelier (Non-Elementary): In the normal model,

  |  |  |  |
  | --- | --- | --- |
  |  | d​(K)=F−Kσ​Td(K)=\frac{F-K}{\sigma\sqrt{T}} |  |

  is proportional to KK. The substitution u=Ku=\sqrt{K} results in

  |  |  |  |
  | --- | --- | --- |
  |  | d​(u2)=F−u2σ​T=A−B​u2,d(u^{2})=\frac{F-u^{2}}{\sigma\sqrt{T}}=A-Bu^{2}, |  |

  which is quadratic in uu. The auxiliary integral ∫Φ​(quadratic)​𝑑u\int\Phi(\text{quadratic})\,du has no elementary antiderivative and typically requires Owen’s TT-functions or complex error functions for exact evaluation.

### B.2. Semi-Closed Form Solution

To maintain high precision without the complexity of non-elementary functions, we compute the Bachelier integral using a semi-closed form:

|  |  |  |
| --- | --- | --- |
|  | ∫abCB​(K)K3/2​𝑑K=[−2​CB​(K)K]ab⏟exact−2​∫abΦ​(d)K​𝑑K⏟Gauss-Legendre\int\_{a}^{b}\frac{C\_{\mathrm{B}}(K)}{K^{3/2}}\,dK=\underbrace{\left[-\frac{2C\_{\mathrm{B}}(K)}{\sqrt{K}}\right]\_{a}^{b}}\_{\text{exact}}-2\underbrace{\int\_{a}^{b}\frac{\Phi(d)}{\sqrt{K}}\,dK}\_{\text{Gauss-Legendre}} |  |

The boundary terms are evaluated exactly. For the remaining integral, we employ nn-point Gauss-Legendre quadrature on the interval [a,b][a,b]:

|  |  |  |
| --- | --- | --- |
|  | ∫abf​(K)​𝑑K≈b−a2​∑i=1nwi​f​(b−a2​xi+a+b2),\int\_{a}^{b}f(K)\,dK\approx\frac{b-a}{2}\sum\_{i=1}^{n}w\_{i}\,f\!\left(\frac{b-a}{2}x\_{i}+\frac{a+b}{2}\right), |  |

where xix\_{i} and wiw\_{i} denote the Legendre nodes and weights on [−1,1][-1,1].

### B.3. Error Control and Validation

The integrand Φ​(d​(K))/K\Phi(d(K))/\sqrt{K} is C∞C^{\infty} on any interval [a,b]⊂(0,∞)[a,b]\subset(0,\infty), ensuring exponential convergence for Gauss-Legendre quadrature. Empirical testing demonstrates the following precision levels:

| nn (Points) | Relative Error |
| --- | --- |
| 8 | 6×10−76\times 10^{-7} |
| 16 | 2×10−152\times 10^{-15} |
| 32 | <10−15<10^{-15} |

Table 1. Convergence of relative error with increasing number of quadrature points.

In our implementation, we utilize n=32n=32 points to consistently achieve machine precision with negligible computational overhead.

## Appendix C Discretization of Integral Remainder

This section provides a formal discretization of the remainder term I​(P0,T)I(P\_{0},T), which is essential for practitioners implementing IL pricing within the piecewise-constant liquidity environment of Uniswap V3.

###### Proposition C.1.

Assume a constant risk-free rate rr and dividend rate δ\delta. The total impermanent loss value is given by:

|  |  |  |
| --- | --- | --- |
|  | ΠIL​(P0)=∫0∞L​(q)​C​(q,T)​𝑑q+I​(P0,T),\Pi\_{\text{IL}}(P\_{0})=\int\_{0}^{\infty}L(q)C(q,T)dq+I(P\_{0},T), |  |

where, defining α=1.0001\alpha=\sqrt{1.0001} and ℓi\ell\_{i} as the liquidity present in the interval [xi,xi+1)[x\_{i},x\_{i+1}) with xi=(1.0001)i=α2​ix\_{i}=(1.0001)^{i}=\alpha^{2i}, the remainder I​(P0,T)I(P\_{0},T) evaluates to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(P0,T)=\displaystyle I(P\_{0},T)= | (α−1)​∑i=imink−1ℓi​[e−r​T​αi−P0​e−δ​T​α−(i+1)]\displaystyle(\alpha-1)\sum\_{i=i\_{\min}}^{k-1}\ell\_{i}\Big[e^{-rT}\alpha^{i}-P\_{0}e^{-\delta T}\alpha^{-(i+1)}\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +ℓk​[e−r​T​(P0−αk)+P0​e−δ​T​(1P0−α−k)].\displaystyle+\ell\_{k}\Big[e^{-rT}\big(\sqrt{P\_{0}}-\alpha^{k}\big)+P\_{0}e^{-\delta T}\Big(\frac{1}{\sqrt{P\_{0}}}-\alpha^{-k}\Big)\Big]. |  | (28) |

Here, imini\_{\min} is the first index with non-zero liquidity, and kk is the index such that xk≤P0<xk+1x\_{k}\leq P\_{0}<x\_{k+1}.

###### Corollary C.2.

If a unit of liquidity ℓ​(q)=1\ell(q)=1 is deposited in the interval [a,b)[a,b) where a=(1.0001)ia=(1.0001)^{i} and b=(1.0001)jb=(1.0001)^{j} for some integers i,ji,j, and a≤P0≤ba\leq P\_{0}\leq b, then the IL value simplifies to:

|  |  |  |
| --- | --- | --- |
|  | ΠIL​(P0)=∫abL​(q)​C​(q,T)​𝑑q+e−r​T​(P0−a)+P0​e−δ​t​(1P0−1a).\Pi\_{\text{IL}}(P\_{0})=\int\_{a}^{b}L(q)C(q,T)dq+e^{-rT}\big(\sqrt{P\_{0}}-\sqrt{a}\big)+P\_{0}e^{-\delta t}\left(\frac{1}{\sqrt{P\_{0}}}-\frac{1}{\sqrt{a}}\right). |  |

### C.1. C.1. Proof of Proposition

Using put-call parity, the impermanent loss integral is split as follows:

|  |  |  |
| --- | --- | --- |
|  | ΠIL​(P0)=∫0∞L​(q)​C​(q,T)​𝑑q+∫0P0L​(q)​(q​e−r​T−P0​e−δ​T)​𝑑q⏟=⁣:I​(P0).\Pi\_{\text{IL}}(P\_{0})=\int\_{0}^{\infty}L(q)C(q,T)dq+\underbrace{\int\_{0}^{P\_{0}}L(q)\big(qe^{-rT}-P\_{0}e^{-\delta T}\big)dq}\_{=:I(P\_{0})}. |  |

Since the intrinsic liquidity ℓ​(q)\ell(q) is piecewise constant on the intervals [xi,xi+1)[x\_{i},x\_{i+1}) defined by the Uniswap V3 tick structure, I​(P0)I(P\_{0}) can be expressed in closed form. For any sub-interval (a,b)⊂[xi,xi+1)(a,b)\subset[x\_{i},x\_{i+1}), the integral evaluates as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I[a,b]​(P0,T)\displaystyle I\_{[a,b]}(P\_{0},T) | =∫abℓi2​q3/2​(q​e−r​T−P0​e−δ​T),d​q\displaystyle=\int\_{a}^{b}\frac{\ell\_{i}}{2q^{3/2}}\big(qe^{-rT}-P\_{0}e^{-\delta T}\big),dq |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℓi​[e−r​T​(b−a)+P0​e−δ​T​(1b−1a)].\displaystyle=\ell\_{i}\Big[e^{-rT}\big(\sqrt{b}-\sqrt{a}\big)+P\_{0}e^{-\delta T}\Big(\frac{1}{\sqrt{b}}-\frac{1}{\sqrt{a}}\Big)\Big]. |  |

By discretizing I​(P0,T)I(P\_{0},T) as a sum over the active tick range:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(P0,T)\displaystyle I(P\_{0},T) | =∑i=imink−1I[xi,xi+1]​(P0,T)+I[xk,P0]​(P0,T)\displaystyle=\sum\_{i=i\_{\min}}^{k-1}I\_{[x\_{i},x\_{i+1}]}(P\_{0},T)+I\_{[x\_{k},P\_{0}]}(P\_{0},T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=imink−1ℓi​[e−r​T​(xi+1−xi)+P0​e−δ​T​(1xi+1−1xi)]\displaystyle=\sum\_{i=i\_{\min}}^{k-1}\ell\_{i}\Big[e^{-rT}\big(\sqrt{x\_{i+1}}-\sqrt{x\_{i}}\big)+P\_{0}e^{-\delta T}\Big(\frac{1}{\sqrt{x\_{i+1}}}-\frac{1}{\sqrt{x\_{i}}}\Big)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ℓk​[e−r​T​(P0−xk)+P0​e−δ​T​(1P0−1xk)].\displaystyle\quad+\ell\_{k}\Big[e^{-rT}\big(\sqrt{P\_{0}}-\sqrt{x\_{k}}\big)+P\_{0}e^{-\delta T}\Big(\frac{1}{\sqrt{P\_{0}}}-\frac{1}{\sqrt{x\_{k}}}\Big)\Big]. |  |

Substituting α=1.0001\alpha=\sqrt{1.0001} such that xi=αi\sqrt{x\_{i}}=\alpha^{i} and 1/xi=α−i1/\sqrt{x\_{i}}=\alpha^{-i}, we arrive at the final summation form in ([28](#A3.E28 "In Proposition C.1. ‣ Appendix C Discretization of Integral Remainder ‣ Pricing and hedging for liquidity provision in Constant Function Market Making")).

## Appendix D Additional Snapshot Overlays

Main-text figures use the November 17, 2025 snapshot. For completeness, this appendix reports the same multi-resolution overlays for additional weekly snapshots.

### 30bp Pool

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251027T000002_30bps_plasma.png)

Figure 6. Multi-resolution implied-volatility overlay for the 30bp pool (Oct 27, 2025 snapshot).

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251103T000002_30bps_plasma.png)

Figure 7. Multi-resolution implied-volatility overlay for the 30bp pool (Nov 3, 2025 snapshot).

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251110T000002_30bps_plasma.png)

Figure 8. Multi-resolution implied-volatility overlay for the 30bp pool (Nov 10, 2025 snapshot).

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251124T000001_30bps_plasma.png)

Figure 9. Multi-resolution implied-volatility overlay for the 30bp pool (Nov 24, 2025 snapshot).

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251201T000001_30bps_plasma.png)

Figure 10. Multi-resolution implied-volatility overlay for the 30bp pool (Dec 1, 2025 snapshot).

### 5bp Pool

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251027T000002_5bps_plasma.png)

Figure 11. Multi-resolution implied-volatility overlay for the 5bp pool (Oct 27, 2025 snapshot).

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251103T000002_5bps_plasma.png)

Figure 12. Multi-resolution implied-volatility overlay for the 5bp pool (Nov 3, 2025 snapshot).

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251110T000002_5bps_plasma.png)

Figure 13. Multi-resolution implied-volatility overlay for the 5bp pool (Nov 10, 2025 snapshot).

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251124T000001_5bps_plasma.png)

Figure 14. Multi-resolution implied-volatility overlay for the 5bp pool (Nov 24, 2025 snapshot).

![[Uncaptioned image]](2603.01344v1/fig/multires_iv_overlay_20251201T000001_5bps_plasma.png)

Figure 15. Multi-resolution implied-volatility overlay for the 5bp pool (Dec 1, 2025 snapshot).

## References

BETA