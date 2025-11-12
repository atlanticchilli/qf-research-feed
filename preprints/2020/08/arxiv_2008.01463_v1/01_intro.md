---
authors:
- Teemu Pennanen
- Udomsak Rakwongwan
doc_id: arxiv:2008.01463v1
family_id: arxiv:2008.01463
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2008.01463] Optimal semi-static hedging in illiquid markets'
url_abs: http://arxiv.org/abs/2008.01463v1
url_html: https://ar5iv.org/html/2008.01463v1
venue: arXiv q-fin
version: 1
year: 2020
---


Teemu Pennanen
teemu.pennanen@kcl.ac.uk
Department of Mathematics,
  
King’s College London,
  
Strand, London, WC2R 2LS, United Kingdom

 Udomsak Rakwongwan
udomsak.rakwongwan@kcl.ac.uk
Department of Mathematics,
  
King’s College London,
  
Strand, London, WC2R 2LS, United Kingdom

###### Abstract

We study indifference pricing of exotic derivatives by using hedging strategies that take static positions in quoted derivatives but trade the underlying and cash dynamically over time. We use real quotes that come with bid-ask spreads and finite quantities. Galerkin method and integration quadratures are used to approximate the hedging problem by a finite dimensional convex optimization problem which is solved by an interior point method. The techniques are extended also to situations where the underlying is subject to bid-ask spreads. As an illustration, we compute indifference prices of path-dependent options written on S&P500 index. Semi-static hedging improves considerably on the purely static options strategy as well as dynamic trading without options. The indifference prices make good economic sense even in the presence of arbitrage opportunities that are found when the underlying is assumed perfectly liquid. When transaction costs are introduced, the arbitrage opportunities vanish but the indifference prices remain almost unchanged.

## 1 Introduction

Unlike in complete markets where derivative prices are uniquely determined by replication arguments, in incomplete markets, quoted prices depend on subjective factors such as the agents’ financial positions, risk preferences and views concerning future market developments. Such dependencies are consistently described by indifference pricing which can be viewed as an extension of replication arguments to the incomplete markets; see e.g. [[4](#bib.bib4), [8](#bib.bib8), [5](#bib.bib5), [9](#bib.bib9)] and the references therein. Extensions to illiquid markets and the corresponding duality theory has been studied in [[14](#bib.bib14)] and [[15](#bib.bib15)], respectively.

This paper develops computational techniques for utility-based semi-static hedging with a finite number of derivatives whose quotes have bid-ask spreads and finite quantities. The hedging strategies involve buy-and-hold positions in the derivatives while the underlying and cash are traded dynamically. We use a Galerkin method to approximate the hedging problem by a finite-dimensional convex optimization problem which is then numerically solved by an interior point method much like in [[1](#bib.bib1)] in a purely static setting. The approach extends with minor modifications to situations where the dynamically traded underlying is also subject to bid ask spreads.

The techniques are illustrated by computing indifference prices of various path-dependent options (including knock-out, Asian and look-back options) on the S&P500 index. As hedging instruments, we use exchange-traded puts and calls on the index. For the nearest maturities, one can find hundreds of options with bid and/or ask quotes.
We find that semi-static hedging significantly improves on the hedges obtained by purely static or purely dynamic strategies. The semi-static hedging strategies provide good approximations of the payouts of the hedged derivatives and the corresponding spreads between seller’s and buyer’s prices are considerably tighter than those obtained with purely static or dynamic hedging. The computational approach applies to arbitrary utility functions and stochastic models that allow for numerical sampling.

Compared to the more traditional super/subhedging, indifference pricing is less sensitive to market imperfections and it makes good sense even in the presence of arbitrage. This was found a useful feature as the quotes on exchange traded options seem to often lead to arbitrage if the dynamically traded underlying is assumed perfectly liquid (as is the case in most models studied in the literature). The arbitrage opportunities vanish when moderate transaction costs on the underlying are introduced but the indifference prices remain almost unaffected.

When the statically hedged options are discarded, the optimal investment strategy to maximize the expected exponential utility coincides with the classical Merton strategy. More surprisingly, the corresponding hedging strategies obtained with indifference pricing seem to coincide with the delta-hedging strategies for replication in complete market models.

Semi-static hedging has been actively studied in the recent literature but mainly under the assumption of perfect liquidity for both the static and dynamic instruments. Moreover, it is common to assume also that there exist quotes for a continuum of strikes as opposed to the finite number of strikes traded in real markets. Much of the research has focused on duality theory in a distributionally roust superhedging; see e.g. [[3](#bib.bib3)]. Guo and Obloj [[7](#bib.bib7)] developed computational techniques for the martingale optimal transport problems by using discretization and interior point methods much like we do below. Their problem can be viewed as the dual of a semi-static superhedging problem with a continuum of strikes for statically held call options (which fixes the marginals of the martingale measures). Extensions of the duality theory of model-free semi-static superhedging to illiquid markets were given in the examples of [[16](#bib.bib16)]. In the computational studies below, we find that with real finite-liquidity quotes for finitely many options, superhedging tends to give prices with very wide spreads.

The present paper is closely related to [[11](#bib.bib11)] and [[10](#bib.bib10)] that studied utility indifference pricing under semi-static trading. While they studied duality and asymptotics of indifference prices in a perfectly liquid continuous-time model, we focus on real illiquid markets and compute prices and hedging portfolios numerically.

The rest of this paper is organized as follows. Sections [2](#S2 "2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets") and [3](#S3 "3 Indifference pricing ‣ Optimal semi-static hedging in illiquid markets") describe the optimal hedging model and the corresponding indifference prices, respectively. Section [4](#S4 "4 Numerical optimization ‣ Optimal semi-static hedging in illiquid markets") presents the techniques employed in the numerical computation of optimal hedging and indifference pricing. Section [5](#S5 "5 Extension to illiquid underlying ‣ Optimal semi-static hedging in illiquid markets") extends the techniques to markets with an illiquid underlying. Sections [6](#S6 "6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") and [7](#S7 "7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") present the numerical results obtained with S&P500 derivatives.

## 2 Semi-static optimisation

Consider a finite set J𝐽J of quoted derivatives whose payouts are determined by the values of an underlying index X𝑋X at times t=0,1,…,T𝑡

01…𝑇t=0,1,\ldots,T. We assume that the derivatives are traded only at t=0𝑡0t=0 and they are held to maturity. The underlying can be traded at any t=0,1,…,T𝑡

01…𝑇t=0,1,\ldots,T. The cost of buying xjsuperscript𝑥𝑗x^{j} units of j∈J𝑗𝐽j\in J is denoted by

|  |  |  |
| --- | --- | --- |
|  | S0j​(xj):={saj​xjif xj≥0,sbj​xjif xj≤0,assignsubscriptsuperscript𝑆𝑗0superscript𝑥𝑗casessubscriptsuperscript𝑠𝑗𝑎superscript𝑥𝑗if xj≥0subscriptsuperscript𝑠𝑗𝑏superscript𝑥𝑗if xj≤0S^{j}\_{0}(x^{j}):=\begin{cases}s^{j}\_{a}x^{j}&\text{if $x^{j}\geq 0$},\\ s^{j}\_{b}x^{j}&\text{if $x^{j}\leq 0$},\end{cases} |  |

where sbj<sajsubscriptsuperscript𝑠𝑗𝑏subscriptsuperscript𝑠𝑗𝑎s^{j}\_{b}<s^{j}\_{a} are the bid and ask prices of j𝑗j. The quantities available at the best bid and ask quotes will be denoted by qbjsubscriptsuperscript𝑞𝑗𝑏q^{j}\_{b} and qajsubscriptsuperscript𝑞𝑗𝑎q^{j}\_{a}, respectively. This means that the position xjsuperscript𝑥𝑗x^{j} we take in asset j𝑗j has to lie in the interval [−qbj,qaj]subscriptsuperscript𝑞𝑗𝑏subscriptsuperscript𝑞𝑗𝑎[-q^{j}\_{b},q^{j}\_{a}]. The payoff of j∈J𝑗𝐽j\in J at time t𝑡t will be denoted by Ptjsuperscriptsubscript𝑃𝑡𝑗P\_{t}^{j}. We assume for now that the underlying index is perfectly liquid and can be dynamically traded at price Xtsubscript𝑋𝑡X\_{t}, t=0,…,T𝑡

0…𝑇t=0,\ldots,T. More realistic markets will be considered in Section [5](#S5 "5 Extension to illiquid underlying ‣ Optimal semi-static hedging in illiquid markets").

Consider an agent with w∈ℝ𝑤ℝw\in\mathbb{R} units of initial cash and the liability to deliver ctsubscript𝑐𝑡c\_{t} units of cash at t=1,…,T𝑡

1…𝑇t=1,\ldots,T. In the applications below, ctsubscript𝑐𝑡c\_{t} will be the payout of an exotic option to be priced. We model the price process X=(Xt)t=1T𝑋superscriptsubscriptsubscript𝑋𝑡𝑡1𝑇X=(X\_{t})\_{t=1}^{T}, the payouts pj=(ptj)t=1Tsuperscript𝑝𝑗superscriptsubscriptsuperscriptsubscript𝑝𝑡𝑗𝑡1𝑇p^{j}=(p\_{t}^{j})\_{t=1}^{T} and the liability c=(ct)t=1T𝑐superscriptsubscriptsubscript𝑐𝑡𝑡1𝑇c=(c\_{t})\_{t=1}^{T} as adapted stochastic processes in a filtered probability space (Ω,ℱ,(ℱt)t=1T,P)Ωℱsuperscriptsubscriptsubscriptℱ𝑡𝑡1𝑇𝑃(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t=1}^{T},P). We will study the optimal investment problem

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | minimizeminimize\displaystyle\mathop{\rm minimize}\limits |  | E​v​(∑t=1T[ct−∑j∈Jptj​xj]−∑t=0T−1zt​Δ​Xt+1)​over​x∈D,z∈𝒩formulae-sequence𝐸𝑣superscriptsubscript𝑡1𝑇delimited-[]subscript𝑐𝑡subscript𝑗𝐽superscriptsubscript𝑝𝑡𝑗superscript𝑥𝑗superscriptsubscript𝑡0𝑇1subscript𝑧𝑡Δsubscript𝑋𝑡1over𝑥𝐷𝑧𝒩\displaystyle Ev\left(\sum\_{t=1}^{T}[c\_{t}-\sum\_{j\in J}p\_{t}^{j}x^{j}]-\sum\_{t=0}^{T-1}z\_{t}\Delta X\_{t+1}\right)\ \text{over}\ x\in D,z\in\mathcal{N} |  | (SSP) |
|  |  | subject​tosubjectto\displaystyle\mathop{\rm subject\ to} |  | ∑j∈JS0j​(xj)≤w,subscript𝑗𝐽subscriptsuperscript𝑆𝑗0superscript𝑥𝑗𝑤\displaystyle\sum\_{j\in J}S^{j}\_{0}(x^{j})\leq w, |  |

where

|  |  |  |
| --- | --- | --- |
|  | D:=∏j∈J[−qbj,qaj],assign𝐷subscriptproduct𝑗𝐽subscriptsuperscript𝑞𝑗𝑏subscriptsuperscript𝑞𝑗𝑎D:=\prod\_{j\in J}[-q^{j}\_{b},q^{j}\_{a}], |  |

𝒩𝒩\mathcal{N} is the linear space of adapted trading strategies z=(zt)t=1T−1𝑧superscriptsubscriptsubscript𝑧𝑡𝑡1𝑇1z=(z\_{t})\_{t=1}^{T-1}, and v:ℝ→ℝ:𝑣→ℝℝv:\mathbb{R}\to\mathbb{R} is a loss function describing the investor’s risk preferences; see e.g. [[6](#bib.bib6), Section 4.9]. One may think of u​(c):=−v​(−c)assign𝑢𝑐𝑣𝑐u(c):=-v(-c) as a utility function so v𝑣v will be assumed nondecreasing and convex. The argument of v𝑣v is the unhedged part of the claims (ct)t=1Tsubscriptsuperscriptsubscript𝑐𝑡𝑇𝑡1{(c\_{t})}^{T}\_{t=1}, the last term being interpreted as the payout of a self-financing trading strategy in the underlying and cash. One could also include various margin requirements in the specification of the set D𝐷D.

It is clear that the optimum value and solutions of problem ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")) depend on

1. 1.

   the financial position described by the initial cash w𝑤w and liability c𝑐c,
2. 2.

   the views concerning the future values of X𝑋X, p𝑝p and c𝑐c described by the probabilistic model,
3. 3.

   the risk preferences described by the loss function v𝑣v

all of which are subjective. The effect of these factors on the optimal hedging strategies and the associated prices of c𝑐c will be studied below. It turns out that, if the claims c𝑐c are replicable, then the prices will be unique and independent of the subjectivities; see Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 3 Indifference pricing ‣ Optimal semi-static hedging in illiquid markets") below.

Another important feature of ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")) is that it is a convex optimization problem. Convexity is crucial in numerical solution of ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")) as well as in the mathematical analysis of the indifference prices.

## 3 Indifference pricing

We shall denote the optimum value of ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")) by

|  |  |  |
| --- | --- | --- |
|  | φ​(w,c):=infx∈D,z∈𝒩{E​v​(∑t=1T[ct−∑j∈Jptj​xj]−∑t=1T−1Δ​Xt+1​zt)|∑j∈JS0j​(xj)≤w}.assign𝜑𝑤𝑐subscriptinfimumformulae-sequence𝑥𝐷𝑧𝒩conditional-set𝐸𝑣superscriptsubscript𝑡1𝑇delimited-[]subscript𝑐𝑡subscript𝑗𝐽superscriptsubscript𝑝𝑡𝑗superscript𝑥𝑗superscriptsubscript𝑡1𝑇1Δsubscript𝑋𝑡1subscript𝑧𝑡subscript𝑗𝐽subscriptsuperscript𝑆𝑗0superscript𝑥𝑗𝑤\varphi(w,c):=\inf\_{x\in D,\ z\in\mathcal{N}}\bigg{\{}Ev\big{(}\sum\_{t=1}^{T}[c\_{t}-\sum\_{j\in J}p\_{t}^{j}x^{j}]-\sum\_{t=1}^{T-1}\Delta X\_{t+1}z\_{t}\big{)}\bigg{|}\,\sum\_{j\in J}S^{j}\_{0}(x^{j})\leq w\bigg{\}}. |  |

For an agent with financial position of w¯¯𝑤\bar{w} units of initial wealth and a liability of delivering a sequence c¯=(c¯t)t=1T¯𝑐superscriptsubscriptsubscript¯𝑐𝑡𝑡1𝑇\bar{c}=(\bar{c}\_{t})\_{t=1}^{T} of payments, the indifference price for selling a claim c=(ct)t=1T𝑐superscriptsubscriptsubscript𝑐𝑡𝑡1𝑇c=(c\_{t})\_{t=1}^{T} is given by

|  |  |  |
| --- | --- | --- |
|  | πs​(w¯,c¯;c):=inf{w∈ℝ|φ​(w¯+w,c¯+c)≤φ​(w¯,c¯)}.assignsubscript𝜋𝑠¯𝑤¯𝑐𝑐infimumconditional-set𝑤ℝ𝜑¯𝑤𝑤¯𝑐𝑐𝜑¯𝑤¯𝑐\pi\_{s}(\bar{w},\bar{c};c):=\inf\{w\in\mathbb{R}\,|\,\varphi(\bar{w}+w,\bar{c}+c)\leq\varphi(\bar{w},\bar{c})\}. |  |

This is the minimum price at which the agent could sell the claim c𝑐c without worsening her financial position as measured by the optimum value of ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")). Analogously, the indifference price for buying c𝑐c is given by

|  |  |  |
| --- | --- | --- |
|  | πb​(w¯,c¯;c):=sup{w∈ℝ|φ​(w¯−w,c¯−c)≤φ​(w¯,c¯)}.assignsubscript𝜋𝑏¯𝑤¯𝑐𝑐supremumconditional-set𝑤ℝ𝜑¯𝑤𝑤¯𝑐𝑐𝜑¯𝑤¯𝑐\pi\_{b}(\bar{w},\bar{c};c):=\sup\{w\in\mathbb{R}\,|\,\varphi(\bar{w}-w,\bar{c}-c)\leq\varphi(\bar{w},\bar{c})\}. |  |

We shall compare the indifference prices with the superhedging and subhedging costs defined by

|  |  |  |
| --- | --- | --- |
|  | πsup​(c):=infx∈D,z∈𝒩{∑j∈JS0j​(xj)|∑t=1T∑j∈Jptj​xj+∑t=1T−1Δ​Xt+1​zt−∑t=1Tct≥0​P​-a.s.},assignsubscript𝜋supremum𝑐subscriptinfimumformulae-sequence𝑥𝐷𝑧𝒩conditional-setsubscript𝑗𝐽subscriptsuperscript𝑆𝑗0superscript𝑥𝑗superscriptsubscript𝑡1𝑇subscript𝑗𝐽superscriptsubscript𝑝𝑡𝑗superscript𝑥𝑗superscriptsubscript𝑡1𝑇1Δsubscript𝑋𝑡1subscript𝑧𝑡superscriptsubscript𝑡1𝑇subscript𝑐𝑡0𝑃-a.s.\pi\_{\sup}(c):=\inf\_{x\in D,\ z\in\mathcal{N}}\bigg{\{}\sum\_{j\in J}S^{j}\_{0}(x^{j})\,\bigg{|}\,\sum\_{t=1}^{T}\sum\_{j\in J}p\_{t}^{j}x^{j}+\sum\_{t=1}^{T-1}\Delta X\_{t+1}z\_{t}-\sum\_{t=1}^{T}c\_{t}\geq 0\ P\text{-a.s.}\bigg{\}}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | πinf​(c):=supx∈D,z∈𝒩{−∑j∈JS0j​(xj)|∑t=1T∑j∈Jptj​xj+∑t=1T−1Δ​Xt+1​zt+∑t=1Tct≥0​P​-a.s.}.assignsubscript𝜋infimum𝑐subscriptsupremumformulae-sequence𝑥𝐷𝑧𝒩conditional-setsubscript𝑗𝐽subscriptsuperscript𝑆𝑗0superscript𝑥𝑗superscriptsubscript𝑡1𝑇subscript𝑗𝐽superscriptsubscript𝑝𝑡𝑗superscript𝑥𝑗superscriptsubscript𝑡1𝑇1Δsubscript𝑋𝑡1subscript𝑧𝑡superscriptsubscript𝑡1𝑇subscript𝑐𝑡0𝑃-a.s.\pi\_{\inf}(c):=\sup\_{x\in D,\ z\in\mathcal{N}}\bigg{\{}-\sum\_{j\in J}S^{j}\_{0}(x^{j})\,\bigg{|}\,\sum\_{t=1}^{T}\sum\_{j\in J}p\_{t}^{j}x^{j}+\sum\_{t=1}^{T-1}\Delta X\_{t+1}z\_{t}+\sum\_{t=1}^{T}c\_{t}\geq 0\ P\text{-a.s.}\bigg{\}}. |  |

The superhedging cost is the least cost of a superhedging portfolio while the subhedging cost is the greatest revenue one could get by entering position that superhedges the negative of c𝑐c. Whereas the indifference prices of a claim depend on our financial position, views and risk preferences described by (w¯,c¯)¯𝑤¯𝑐(\bar{w},\bar{c}), P𝑃P and v𝑣v, respectively, the superhedging and subhedging costs are independent of such subjective factors.

In situations where the quantities available at the best quotes are large enough to be nonbinding, the indifference prices lie between the superhedging and subhedging costs. Indeed, an application of [[14](#bib.bib14), Theorem 4.1] to the present situation gives the following.

###### Theorem 1.

The function πs​(w¯,c¯;⋅)subscript𝜋𝑠¯𝑤¯𝑐⋅\pi\_{s}(\bar{w},\bar{c};\cdot) is convex, nondecreasing and πs​(w¯,c¯;0)≤0subscript𝜋𝑠¯𝑤¯𝑐00\pi\_{s}(\bar{w},\bar{c};0)\leq 0. If there are no quantity constraints (or if they are not active), then πs​(w¯,c¯;c)≤πsup​(c)subscript𝜋𝑠¯𝑤¯𝑐𝑐subscript𝜋supremum𝑐\pi\_{s}(\bar{w},\bar{c};c)\leq\pi\_{\sup}(c). If in addition, πs​(w¯,c¯;0)=0subscript𝜋𝑠¯𝑤¯𝑐00\pi\_{s}(\bar{w},\bar{c};0)=0, then

|  |  |  |
| --- | --- | --- |
|  | πinf​(c)≤πl​(w¯,c¯;c)≤πs​(w¯,c¯;c)≤πsup​(c)∀c∈L0formulae-sequencesubscript𝜋infimum𝑐subscript𝜋𝑙¯𝑤¯𝑐𝑐subscript𝜋𝑠¯𝑤¯𝑐𝑐subscript𝜋supremum𝑐for-all𝑐superscript𝐿0\pi\_{\inf}(c)\leq\pi\_{l}(\bar{w},\bar{c};c)\leq\pi\_{s}(\bar{w},\bar{c};c)\leq\pi\_{\sup}(c)\quad\forall c\in L^{0} |  |

with equalities throughout if sb=sasuperscript𝑠𝑏superscript𝑠𝑎s^{b}=s^{a} and c𝑐c is replicable.

As long as one can (numerically) compute the optimum values φ​(w,c)𝜑𝑤𝑐\varphi(w,c) for given (w,c)𝑤𝑐(w,c), the indifference prices can be computed by a simple line search with respect to the price. This can, however, be computationally expensive. If cash is perfectly liquid and the interest rate is zero, the indifference prices can be expressed in terms of two optimization problems as follows.

###### Proposition 1.

If cash is perfectly liquid with zero interest rate, the indifference prices for buying and selling for an agent with exponential risk measure can be expressed as,

|  |  |  |
| --- | --- | --- |
|  | πb​(w¯,c¯;c)=w¯λ​log⁡(φ​(w¯,c¯)φ​(w¯,c¯−c)),subscript𝜋𝑏¯𝑤¯𝑐𝑐¯𝑤𝜆𝜑¯𝑤¯𝑐𝜑¯𝑤¯𝑐𝑐\pi\_{b}(\bar{w},\bar{c};c)=\frac{\bar{w}}{\lambda}\log\bigg{(}\frac{\varphi(\bar{w},\bar{c})}{\varphi(\bar{w},\bar{c}-c)}\bigg{)}, |  |

|  |  |  |
| --- | --- | --- |
|  | πs​(w¯,c¯;c)=w¯λ​log⁡(φ​(w¯,c¯+c)φ​(w¯,c¯)),subscript𝜋𝑠¯𝑤¯𝑐𝑐¯𝑤𝜆𝜑¯𝑤¯𝑐𝑐𝜑¯𝑤¯𝑐\pi\_{s}(\bar{w},\bar{c};c)=\frac{\bar{w}}{\lambda}\log\bigg{(}\frac{\varphi(\bar{w},\bar{c}+c)}{\varphi(\bar{w},\bar{c})}\bigg{)}, |  |

where w¯¯𝑤\bar{w} is an initial wealth, and λ𝜆\lambda is a risk aversion factor.

###### Proof.

By definition,

|  |  |  |
| --- | --- | --- |
|  | φ​(w¯+w,c¯+c)=infx∈D,z∈𝒩{Eexp(λw¯(∑t=1T[c¯t+ct−∑j∈Jptjxj]−∑t=1T−1ΔXt+1zt))|∑j∈JS0j(xj)≤w¯+w},=infx∈D,z∈𝒩{Eexp(λw¯(∑t=1T[c¯t+ct−∑j∈Jptjxj]−w−∑t=1T−1ΔXt+1zt))|∑j∈JS0j(xj)≤w¯},=φ​(w¯,c¯+c)​exp⁡(−λ​ww¯).\begin{split}\varphi(\bar{w}+w,\bar{c}+c)=&\inf\_{x\in D,\ z\in\mathcal{N}}\bigg{\{}E\exp(\frac{\lambda}{\bar{w}}(\sum\_{t=1}^{T}[\bar{c}\_{t}+c\_{t}-\sum\_{j\in J}p^{j}\_{t}x^{j}]-\sum\_{t=1}^{T-1}\Delta X\_{t+1}z\_{t}))\,\\ &\qquad\qquad\bigg{|}\,\sum\_{j\in J}S^{j}\_{0}(x^{j})\leq\bar{w}+w\bigg{\}},\\ =&\inf\_{x\in D,\ z\in\mathcal{N}}\bigg{\{}E\exp(\frac{\lambda}{\bar{w}}(\sum\_{t=1}^{T}[\bar{c}\_{t}+c\_{t}-\sum\_{j\in J}p^{j}\_{t}x^{j}]-w-\sum\_{t=1}^{T-1}\Delta X\_{t+1}z\_{t}))\\ &\qquad\qquad\bigg{|}\,\sum\_{j\in J}S^{j}\_{0}(x^{j})\leq\bar{w}\bigg{\}},\\ =&\varphi(\bar{w},\bar{c}+c)\exp(\frac{-\lambda w}{\bar{w}}).\end{split} |  |

Thus,

|  |  |  |
| --- | --- | --- |
|  | πb​(w¯,c¯;c)=inf{w|φ​(w¯−w,c¯−c)≤φ​(w¯,c¯)},=inf{w|φ​(w¯,c¯−c)​exp⁡(λ​ww¯)≤φ​(w¯,c¯)},=w¯λ​log⁡(φ​(w¯,c¯)φ​(w¯,c¯−c)),\begin{split}\pi\_{b}(\bar{w},\bar{c};c)=&\inf\{w\,|\,\varphi(\bar{w}-w,\bar{c}-c)\leq\varphi(\bar{w},\bar{c})\},\\ =&\inf\{w\,|\,\varphi(\bar{w},\bar{c}-c)\exp(\frac{\lambda w}{\bar{w}})\leq\varphi(\bar{w},\bar{c})\},\\ =&\frac{\bar{w}}{\lambda}\log\bigg{(}\frac{\varphi(\bar{w},\bar{c})}{\varphi(\bar{w},\bar{c}-c)}\bigg{)},\\ \end{split} |  |

and

|  |  |  |
| --- | --- | --- |
|  | πs​(w¯,c¯;c)=inf{w|φ​(w¯+w,c¯+c)≤φ​(w¯,c¯)},=inf{w|φ​(w¯,c¯+c)​exp⁡(−λ​ww¯)≤φ​(w¯,c¯)},=w¯λ​log⁡(φ​(w¯,c¯+c)φ​(w¯,c¯)),\begin{split}\pi\_{s}(\bar{w},\bar{c};c)=&\inf\{w\,|\,\varphi(\bar{w}+w,\bar{c}+c)\leq\varphi(\bar{w},\bar{c})\},\\ =&\inf\{w\,|\,\varphi(\bar{w},\bar{c}+c)\exp(\frac{-\lambda w}{\bar{w}})\leq\varphi(\bar{w},\bar{c})\},\\ =&\frac{\bar{w}}{\lambda}\log\bigg{(}\frac{\varphi(\bar{w},\bar{c}+c)}{\varphi(\bar{w},\bar{c})}\bigg{)},\end{split} |  |

which completes the proof.
∎

## 4 Numerical optimization

We assume from now on that the derivative and liability payouts pjsuperscript𝑝𝑗p^{j} and c𝑐c, respectively, are adapted to the filtration generated by the underlying X𝑋X. This clearly holds when pjsuperscript𝑝𝑗p^{j} and c𝑐c are contingent claims on X𝑋X.

### 4.1 Galerkin method

To solve ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")), we need to optimize the dynamic part z𝑧z over the infinite-dimensional space 𝒩𝒩\mathcal{N} of adapted stochastic processes. We will employ the Galerkin method where one optimizes z𝑧z only over the finite-dimensional subspace 𝒩N⊂𝒩superscript𝒩𝑁𝒩\mathcal{N}^{N}\subset\mathcal{N} spanned by the simple processes zs,n∈𝒩superscript𝑧

𝑠𝑛𝒩z^{s,n}\in\mathcal{N} of the form

|  |  |  |
| --- | --- | --- |
|  | zts,n​(ω):={1if t=s, Xt​(ω)∈[Kn,Kn+1),0otherwise,assignsubscriptsuperscript𝑧  𝑠𝑛𝑡𝜔cases1if t=s, Xt(ω)∈[Kn,Kn+1)0otherwisez^{s,n}\_{t}(\omega):=\begin{cases}1&\text{if $t=s$, $X\_{t}(\omega)\in[K\_{n},K\_{n+1})$},\\ 0&\text{otherwise},\end{cases} |  |

where s=1,2,…,T−1𝑠

12…𝑇1s=1,2,\ldots,T-1 and Knsubscript𝐾𝑛K\_{n}, n=1,2,…,Ns𝑛

12…subscript𝑁𝑠n=1,2,\ldots,N\_{s} are the strikes of the quoted options with maturity s𝑠s, while K0=0subscript𝐾00K\_{0}=0 and KNs+1=+∞subscript𝐾subscript𝑁𝑠1K\_{N\_{s}+1}=+\infty. The dimension of the linear span 𝒩Nsuperscript𝒩𝑁\mathcal{N}^{N} is thus N=∏s=1T−1(Ns+1)𝑁superscriptsubscriptproduct𝑠1𝑇1subscript𝑁𝑠1N=\prod\_{s=1}^{T-1}(N\_{s}+1). Clearly, each zts,nsubscriptsuperscript𝑧

𝑠𝑛𝑡z^{s,n}\_{t} is adapted to the filtration generated by X𝑋X so indeed, 𝒩N⊂𝒩superscript𝒩𝑁𝒩\mathcal{N}^{N}\subset\mathcal{N}. The linear span 𝒩Nsuperscript𝒩𝑁\mathcal{N}^{N} consists of simple processes that that are constant between consecutive strikes.

### 4.2 Integration quadrature

Since the filtration (ℱt)t=0Tsuperscriptsubscriptsubscriptℱ𝑡𝑡0𝑇(\mathcal{F}\_{t})\_{t=0}^{T} is generated by X𝑋X, the Doob-Dynkin lemma implies that the random variables ctsubscript𝑐𝑡c\_{t} and ptsubscript𝑝𝑡p\_{t} are functions of Xt=(X1,X2,…,Xt)superscript𝑋𝑡subscript𝑋1subscript𝑋2…subscript𝑋𝑡X^{t}=(X\_{1},X\_{2},\ldots,X\_{t}). The objective of ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")) can be written as

|  |  |  |
| --- | --- | --- |
|  | E​f​(x,z)=∫ℝ+Tf​(x,z​(X),X)​φ​(X)​𝑑X,𝐸𝑓𝑥𝑧subscriptsuperscriptsubscriptℝ𝑇𝑓𝑥𝑧𝑋𝑋𝜑𝑋differential-d𝑋Ef(x,z)=\int\_{\mathbb{R}\_{+}^{T}}f(x,z(X),X)\varphi(X)dX, |  |

where φ𝜑\varphi is the density function of X, and

|  |  |  |
| --- | --- | --- |
|  | f​(x,z​(X),X):=v​(∑t=1T[ct​(Xt)−∑j∈Jptj​(Xt)​xj]−∑t=1T−1Δ​Xt+1​zt​(Xt)).assign𝑓𝑥𝑧𝑋𝑋𝑣superscriptsubscript𝑡1𝑇delimited-[]subscript𝑐𝑡superscript𝑋𝑡subscript𝑗𝐽superscriptsubscript𝑝𝑡𝑗superscript𝑋𝑡superscript𝑥𝑗superscriptsubscript𝑡1𝑇1Δsubscript𝑋𝑡1subscript𝑧𝑡subscript𝑋𝑡f(x,z(X),X):=v\left(\sum\_{t=1}^{T}[c\_{t}(X^{t})-\sum\_{j\in J}p\_{t}^{j}(X^{t})x^{j}]-\sum\_{t=1}^{T-1}\Delta X\_{t+1}z\_{t}(X\_{t})\right). |  |

We will approximate the multivariate integral by an integration quadrature:

|  |  |  |
| --- | --- | --- |
|  | ∫ℝ+Tf​(x,z​(X),X)​φ​(X)​𝑑X≈∑i=1Mwi​f​(x,z​(X(i)),X(i))​φ​(X(i)),subscriptsuperscriptsubscriptℝ𝑇𝑓𝑥𝑧𝑋𝑋𝜑𝑋differential-d𝑋superscriptsubscript𝑖1𝑀subscript𝑤𝑖𝑓𝑥𝑧superscript𝑋𝑖superscript𝑋𝑖𝜑superscript𝑋𝑖\int\_{\mathbb{R}\_{+}^{T}}f(x,z(X),X)\varphi(X)dX\approx\sum\_{i=1}^{M}w\_{i}f(x,z(X^{(i)}),X^{(i)})\varphi(X^{(i)}), |  |

where M𝑀M is the number of the quadrature points, X(i)superscript𝑋𝑖X^{(i)} are the quadrature points and wisubscript𝑤𝑖w\_{i} are the corresponding weights.

There are many possible choices for the integration quadrature. In this study, we take X(i)=(Xt(i))t=1Tsuperscript𝑋𝑖superscriptsubscriptsubscriptsuperscript𝑋𝑖𝑡𝑡1𝑇X^{(i)}=(X^{(i)}\_{t})\_{t=1}^{T} where Xt(i)subscriptsuperscript𝑋𝑖𝑡X^{(i)}\_{t} are the strikes at maturity t𝑡t. The corresponding weights wisubscript𝑤𝑖w\_{i} will be the volumes of the hyper cubes defined by the consecutive strikes. This choice of quadrature points yields fairly accurate results because the portfolio payout depends linearly on the index value between two strikes. In addition, the probability that the index is smaller than the smallest strike or bigger than the biggest strike is very small.

### 4.3 Interior point method

The approximate problem obtained with the Galerkin method and the integration quadrature, problem ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")) becomes a finite-dimensional convex optimization problem with finitely many constraints. It can be written as

|  |  |  |
| --- | --- | --- |
|  | minimize∑i=1Mv​(∑t=1T[ct​(Xt)−∑j∈Jptj​(Xt)​xj]−∑t=1T−1Δ​Xt+1​zt​(Xt))​wi​φ​(Xi)  minimizesuperscriptsubscript𝑖1𝑀𝑣superscriptsubscript𝑡1𝑇delimited-[]subscript𝑐𝑡superscript𝑋𝑡subscript𝑗𝐽superscriptsubscript𝑝𝑡𝑗superscript𝑋𝑡superscript𝑥𝑗superscriptsubscript𝑡1𝑇1Δsubscript𝑋𝑡1subscript𝑧𝑡subscript𝑋𝑡subscript𝑤𝑖𝜑superscript𝑋𝑖\displaystyle\mathop{\rm minimize}\limits\quad\sum\_{i=1}^{M}v\left(\sum\_{t=1}^{T}[c\_{t}(X^{t})-\sum\_{j\in J}p\_{t}^{j}(X^{t})x^{j}]-\sum\_{t=1}^{T-1}\Delta X\_{t+1}z\_{t}(X\_{t})\right)w\_{i}\varphi(X^{i}) |  |
|  |  |  |
| --- | --- | --- |
|  | overx∈D,z∈𝒩Nformulae-sequence  over𝑥 𝐷𝑧superscript𝒩𝑁\displaystyle\text{over}\quad x\in D,\ z\in\mathcal{N}^{N} |  |
|  |  |  |
| --- | --- | --- |
|  | subject​to∑j∈JS0j​(xj)≤w.  subjecttosubscript𝑗𝐽subscriptsuperscript𝑆𝑗0superscript𝑥𝑗 𝑤\displaystyle\mathop{\rm subject\ to}\quad\sum\_{j\in J}S^{j}\_{0}(x^{j})\leq w. |  |

This is a finite-dimensional convex optimization problem that can be solved numerically e.g. by interior-point methods. In this study, we use the exponential utility so the problem can be written as a conic exponential optimization problem and solved using the interior-point solver of MOSEK [[2](#bib.bib2)]. Numerical results are given in Section [6](#S6 "6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") below.

## 5 Extension to illiquid underlying

Up to now, we have assumed that the underlying index is a perfectly liquid asset that can bought and sold at price X𝑋X. The same assumption is made in most of the literature on semi-static hedging but from a practical point of view, this is not quite realistic. This section considers a more realistic variant of ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")) where the index is subject to a transaction costs, or equivalently, a constant bid-ask spread. More precisely, we assume that an agent needs to pay a δ𝛿\delta% transaction cost to buy or sell the index at time t=1,2,…,T−1𝑡

12…𝑇1t=1,2,\ldots,T-1, and the index is liquid at T𝑇T. The semi-static hedging problem can then be written as

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | minimizeminimize\displaystyle\mathop{\rm minimize}\limits\quad |  | E​v​(∑t=1T[ct−∑j∈Jptj​xj]+∑t=1TSt​(Δ​zt))over​x∈D,z∈𝒩formulae-sequence  𝐸𝑣superscriptsubscript𝑡1𝑇delimited-[]subscript𝑐𝑡subscript𝑗𝐽superscriptsubscript𝑝𝑡𝑗superscript𝑥𝑗superscriptsubscript𝑡1𝑇subscript𝑆𝑡Δsubscript𝑧𝑡over𝑥 𝐷𝑧𝒩\displaystyle Ev\left(\sum\_{t=1}^{T}[c\_{t}-\sum\_{j\in J}p\_{t}^{j}x^{j}]+\sum\_{t=1}^{T}S\_{t}(\Delta z\_{t})\right)\quad\text{over}\ x\in D,z\in\mathcal{N} |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | subject​tosubjectto\displaystyle\mathop{\rm subject\ to}\quad |  | ∑j∈JS0j​(xj)≤w,subscript𝑗𝐽subscriptsuperscript𝑆𝑗0superscript𝑥𝑗𝑤\displaystyle\sum\_{j\in J}S^{j}\_{0}(x^{j})\leq w, |  |

where Δ​zt:=zt−zt−1assignΔsubscript𝑧𝑡subscript𝑧𝑡subscript𝑧𝑡1\Delta z\_{t}:=z\_{t}-z\_{t-1} is the number of the unit of the underlying bought at t𝑡t and

|  |  |  |
| --- | --- | --- |
|  | St​(Δ​zt):={(1+δ100)​Xt​Δ​ztif Δ​zt≥0,(1−δ100)​Xt​Δ​ztif Δ​zt≤0.assignsubscript𝑆𝑡Δsubscript𝑧𝑡cases1𝛿100subscript𝑋𝑡Δsubscript𝑧𝑡if Δzt≥01𝛿100subscript𝑋𝑡Δsubscript𝑧𝑡if Δzt≤0S\_{t}(\Delta z\_{t}):=\begin{cases}(1+\frac{\delta}{100})X\_{t}\Delta z\_{t}&\text{if $\Delta z\_{t}\geq 0$},\\ (1-\frac{\delta}{100})X\_{t}\Delta z\_{t}&\text{if $\Delta z\_{t}\leq 0$}.\end{cases} |  |

Here and in what follows, z−1=zT=0subscript𝑧1subscript𝑧𝑇0z\_{-1}=z\_{T}=0. Note that if δ=0𝛿0\delta=0,

|  |  |  |
| --- | --- | --- |
|  | ∑t=1TSt​(Δ​zt)=∑t=1TXt​Δ​zt=−∑t=1T−1Δ​Xt+1​zt,superscriptsubscript𝑡1𝑇subscript𝑆𝑡Δsubscript𝑧𝑡superscriptsubscript𝑡1𝑇subscript𝑋𝑡Δsubscript𝑧𝑡superscriptsubscript𝑡1𝑇1Δsubscript𝑋𝑡1subscript𝑧𝑡\sum\_{t=1}^{T}S\_{t}(\Delta z\_{t})=\sum\_{t=1}^{T}X\_{t}\Delta z\_{t}=-\sum\_{t=1}^{T-1}\Delta X\_{t+1}{z\_{t}}, |  |

so the original model ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")) is a special case of the above.

To solve the problem numerically, we express the purchases Δ​zΔ𝑧\Delta z as

|  |  |  |
| --- | --- | --- |
|  | Δ​zt=Δ​zt+−Δ​zt−,Δsubscript𝑧𝑡Δsuperscriptsubscript𝑧𝑡Δsuperscriptsubscript𝑧𝑡\Delta z\_{t}=\Delta z\_{t}^{+}-\Delta z\_{t}^{-}, |  |

where Δ​zt+,Δ​zt−≥0

Δsuperscriptsubscript𝑧𝑡Δsuperscriptsubscript𝑧𝑡
0\Delta z\_{t}^{+},\Delta z\_{t}^{-}\geq 0 represent purchases and sales, respectively, of the underlying. Thus, the trading cost can be written as

|  |  |  |
| --- | --- | --- |
|  | St​(Δ​zt)=(1+δ100)​Xt​Δ​zt+−(1−δ100)​Xt​Δ​zt−.subscript𝑆𝑡Δsubscript𝑧𝑡1𝛿100subscript𝑋𝑡Δsubscriptsuperscript𝑧𝑡1𝛿100subscript𝑋𝑡Δsubscriptsuperscript𝑧𝑡S\_{t}(\Delta z\_{t})=(1+\frac{\delta}{100})X\_{t}\Delta z^{+}\_{t}-(1-\frac{\delta}{100})X\_{t}\Delta z^{-}\_{t}. |  |

We then can apply the Galerkin method to Δ​zt+Δsubscriptsuperscript𝑧𝑡\Delta z^{+}\_{t} and Δ​zt−Δsubscriptsuperscript𝑧𝑡\Delta z^{-}\_{t} where the multipliers of the basis functions are restricted to be positive. The rest is similar to the numerical solution of ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")) described in Section [4](#S4 "4 Numerical optimization ‣ Optimal semi-static hedging in illiquid markets").

## 6 An application to S&P500 derivatives

This section illustrates the presented models and techniques in the S&P500 derivatives market with option quotes taken from Bloomberg. For the nearest maturities, there are hundreds of exchange traded puts and calls whose quotes come with bid-ask spreads and finite quantities. The resulting optimization and pricing problems are then solved using the techniques described in Sections [4](#S4 "4 Numerical optimization ‣ Optimal semi-static hedging in illiquid markets")–[5](#S5 "5 Extension to illiquid underlying ‣ Optimal semi-static hedging in illiquid markets").

We start by finding optimal portfolios in the quoted derivatives when assuming that the liability c𝑐c in Problem ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")) is zero. We study the dependence of the optimal solution on the risk preferences as well as on the distribution of the underlying, both of which are highly subjective components of the model. Building on the optimization model, we then compute indifference prices for path-dependent derivatives namely a knock-out call option, an Asian call option, look-back call options and a look-back digital option. We compare the optimized portfolios and indifference prices obtained by semi-static hedging with different transaction costs to those obtained by purely dynamic hedging without options.

### 6.1 Quotes, views, and preferences

We use quotes for S&P500 index options with maturities 21 April 2017 and 19 May 2017. The strikes of the options range from 1500 to 2500. The quotes were obtained from Bloomberg on 21 March 2017 at 3:00:00 PM when the value of the S&P500 index was 236023602360. All quotes come with bid ask spreads and finite quantities. Table [1](#S6.T1 "Table 1 ‣ 6.1 Quotes, views, and preferences ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") gives an example of quotes on put and call options written on the S&P500 index available on 21 March 2017 at 15:00:00 expiring on 21 April 2017 and 19 May 2017. The index value was 2,360 at the time. The bid and ask prices shown in the table are per one option, whereas the available quantities are given in terms of a lot size which is 100. For example, the cost of buying or selling a call option with strike 2300 expiring on 5/19/2017 are 81.80 and 79.50, and there are 51 contracts (5100 options) and 48 contracts (4800 options) available for buying and selling respectively.

Call options are more liquid at lower strikes. One can find quotes for call options whose strikes are as low as 500, whereas the lowest strike for put options available in the market is 1,555. For the two nearest maturities, one can find quotes for 678 options whose strikes range from 1,500 to 2,500 with 5 dollar increments.

| Ticker | Type | Bid quantity | Bid price | Ask price | Ask quantity |
| --- | --- | --- | --- | --- | --- |
| SPX US 5/19/2017 C2300 Index | Call | 48 | 79.5 | 81.8 | 51 |
| SPX US 5/19/2017 P2300 Index | Put | 182 | 22.6 | 24 | 376 |
| SPX US 4/21/2017 C2370 Index | Call | 300 | 18.7 | 20.3 | 273 |
| SPX US 4/21/2017 P2370 Index | Put | 275 | 28.6 | 30.5 | 322 |

Table 1: Market quotes extracted from Bloomberg on 21 March 2017 at 15:00:00 for put and call options expiring on 21 April 2017 and 19 May 2017.

In the applications below, we assume zero interest on cash. In practice, the index is not tradable, but one can trade exchange-traded funds, ETFs, which are securities that track the index. An example of a fairly liquid ETF which efficiently tracks the S&P500 index is the SPY is issued by State Street Global Advisors.

We model the logarithm of the S&P500 index by a variance gamma process, obtained by evaluating Brownian motion with drift θ𝜃\theta and volatility σ𝜎\sigma at a random time change given by a gamma process with a unit mean rate and a variance rate ν𝜈\nu; see [[12](#bib.bib12)] and [[13](#bib.bib13)]. The parameters θ𝜃\theta and ν𝜈\nu provide control over skewness and kurtosis, respectively. As a base case, we use the parameter values given in Table [2](#S6.T2 "Table 2 ‣ 6.1 Quotes, views, and preferences ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets"). The parameter θ𝜃\theta is assumed to be zero, whereas the parameters σ𝜎\sigma, and ν𝜈\nu are estimated using 10-year historical daily data. The effect of varying the parameters will be studied later on. The initial wealth w𝑤w is 100,000

100000100,000 USD and for now, the claim ctsubscript𝑐𝑡c\_{t} is assumed to be zero for all t𝑡t.

As for risk preferences, we use exponential loss function

|  |  |  |
| --- | --- | --- |
|  | v​(c)=eλ​c/w,𝑣𝑐superscript𝑒𝜆𝑐𝑤v(c)=e^{\lambda c/w}, |  |

where w𝑤w is the initial wealth and λ>0𝜆0\lambda>0 is a risk aversion parameter. It should be noted that, in general, the net position at maturity can take both positive as well as negative values which prevents the use of utility functions with constant relative risk aversion.

| λ𝜆\lambda | θ𝜃\theta | σ𝜎\sigma | ν𝜈\nu |
| --- | --- | --- | --- |
| 2 | 0 | 0.1206 | 0.0031 |

Table 2: Base-case parameters including a risk aversion factor λ𝜆\lambda and variance gamma parameters θ,σ

𝜃𝜎\theta,\sigma, and ν𝜈\nu used to model the index value.

### 6.2 Optimized strategies

To simplify the presentation and to ease the extensive numerical computations on a relatively modest computational setup, we will study a two-period instance of semi-static hedging and pricing. With the available set of quotes options and the numerical procedure described in Section [4](#S4 "4 Numerical optimization ‣ Optimal semi-static hedging in illiquid markets"), there are over 1700 variables and 2700 constraints in the discretized optimization problem. In the quadrature approximation of the expected loss function there are over 160,000 points on the grid; see Section [4.2](#S4.SS2 "4.2 Integration quadrature ‣ 4 Numerical optimization ‣ Optimal semi-static hedging in illiquid markets"). The interior point solver of MOSEK takes on average of 650.40 seconds on a PC with Intel(R) Core(TM) i5-4690 CPU @ 3.50GHz processor and 16.00 GB memory.

Figure [1](#S6.F1 "Figure 1 ‣ 6.2 Optimized strategies ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") represents the structure of the optimized semi-static strategy. The bars represent the optimal positions in the options, whereas the line plots show the positions in cash and the index taken at t=1𝑡1t=1 as functions of X1subscript𝑋1X\_{1}. Figure [2](#S6.F2 "Figure 2 ‣ 6.2 Optimized strategies ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") plots the payout of the portfolio as a function of X1subscript𝑋1X\_{1} and X2subscript𝑋2X\_{2}.

The portfolio enjoys higher profit if the index values at the first and second maturities are close to each other, while its loss is greater elsewhere. This makes sense as it is unlikely that the index value at the second maturity greatly deviates from that of the first maturity.

![Refer to caption](/html/2008.01463/assets/x1.png)


Figure 1: The structure of the optimized semi-static strategy where an index value is modelled by symmetric variance gamma with parameters given in Table [2](#S6.T2 "Table 2 ‣ 6.1 Quotes, views, and preferences ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets").

![Refer to caption](/html/2008.01463/assets/x2.png)


Figure 2: The payout of the optimal portfolio by semi-static optimization as a function of X1subscript𝑋1X\_{1} and X2subscript𝑋2X\_{2}. The grey horizontal plane represents the initial wealth.

Figure [3](#S6.F3 "Figure 3 ‣ 6.2 Optimized strategies ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") represents the structure of the optimized portfolio obtained with risk aversion λ=6𝜆6\lambda=6. The other parameters are as in Table [2](#S6.T2 "Table 2 ‣ 6.1 Quotes, views, and preferences ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets"). The payout of the portfolio is plotted in Figure [4](#S6.F4 "Figure 4 ‣ 6.2 Optimized strategies ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") (left) together with the payout of the optimal portfolio obtained with risk aversion λ=2𝜆2\lambda=2. The right plot of Figure [4](#S6.F4 "Figure 4 ‣ 6.2 Optimized strategies ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") shows the kernel density estimates (using 1,000,000 out-of-sample simulated price paths) of the terminal wealth of the optimal portfolios obtained with risk aversion 2 and 6.

![Refer to caption](/html/2008.01463/assets/x3.png)


Figure 3: The structure of the optimized semi-static strategy obtained when the risk aversion increased from 2 to 6.

![Refer to caption](/html/2008.01463/assets/x4.png)


Figure 4: The payout as functions of X1subscript𝑋1X\_{1} and X2subscript𝑋2X\_{2} of the optimal portfolios obtained with risk aversions 2 and 6 (left). The kernel density estimates of the terminal wealths of the optimal portfolios obtained with risk aversions 2 and 6 using 1,000,000 out-of-sample simulated price paths (right).

We see that the positions of the optimized portfolio obtained with risk aversion λ=6𝜆6\lambda=6 are smaller than the ones with risk aversion λ=2𝜆2\lambda=2. As expected, the payout of the portfolio obtained with higher risk aversion is less variable. Except for the scale, the shapes of the two kernel density plots look fairly similar, both exhibiting profits in roughly the same area. This makes sense as changing risk aversion does not change the view on the index value.

| base case | λ=6𝜆6\lambda=6 | σ=0.08𝜎0.08\sigma=0.08 | σ=0.2𝜎0.2\sigma=0.2 |
| --- | --- | --- | --- |
| -2.4404 | -6.4832 | -2.7947 | -2.7895 |

Table 3: Logarithms of optimum objective values obtained with different parameters in the semi-static optimization problem ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")). As one of the parameters changes, the others remain the same as in the base case.

Figure [5](#S6.F5 "Figure 5 ‣ 6.2 Optimized strategies ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") plots the optimal payouts obtained with σ=0.08𝜎0.08\sigma=0.08 (left) and σ=0.2𝜎0.2\sigma=0.2 (right). Not surprisingly, increasing σ𝜎\sigma results in a portfolio that gives higher payout further in the tails (a straddle). Table [3](#S6.T3 "Table 3 ‣ 6.2 Optimized strategies ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") gives the logarithms of the optimum objective values when σ=0.1206𝜎0.1206\sigma=0.1206, σ=0.08𝜎0.08\sigma=0.08 and σ=0.2𝜎0.2\sigma=0.2. Note that, since we use the exponential loss function, the logarithmic objective is the “entropic risk measure” which has units of cash. It can also be interpreted as the “certainty equivalent”. The highest objective value is obtained with the base-case parameters which are estimated from historical data. This may be thought of as consistency of the market quotes and the market participants’ views of the future behavior of the underlying. With a model that is inconsistent with the “market views”, the available quotes may seem to offer profitable trading opportunities.

![Refer to caption](/html/2008.01463/assets/x5.png)


Figure 5: The payout of the optimal portfolios by semi-static optimization as functions of X1subscript𝑋1X\_{1} and X2subscript𝑋2X\_{2}, obtained with σ=0.08𝜎0.08\sigma=0.08 (left) and σ=0.2𝜎0.2\sigma=0.2 (right). The grey horizontal planes represent the initial wealth.

### 6.3 Arbitrage

We found that, with the quotes obtained from Bloomberg, there exists an arbitrage opportunity if the index can be traded without transaction costs. Due to the finite quantities at the best bid and ask quotes, however, the optimization model admits a bounded solution so that the pricing and hedging problems still make economic sense.

To identify an arbitrage portfolio, we add the constraint

|  |  |  |
| --- | --- | --- |
|  | ∑t=1T∑j∈Jptj​xj+∑t=1T−1Δ​Xt+1​zt≥wP​-a.s.superscriptsubscript𝑡1𝑇subscript𝑗𝐽superscriptsubscript𝑝𝑡𝑗superscript𝑥𝑗superscriptsubscript𝑡1𝑇1Δsubscript𝑋𝑡1subscript𝑧𝑡  𝑤𝑃-a.s.\sum\_{t=1}^{T}\sum\_{j\in J}p\_{t}^{j}x^{j}+\sum\_{t=1}^{T-1}\Delta X\_{t+1}z\_{t}\geq w\quad P\text{-a.s.} |  |

to problem ([SSP](#S2.Ex2 "In 2 Semi-static optimisation ‣ Optimal semi-static hedging in illiquid markets")). This means that the portfolio payout is at least the initial wealth in all scenarios. In numerical computations, we impose the constraint on all quadrature points. As the payout is a linear function between the strikes, the constraint will then hold everywhere. Figure [6](#S6.F6 "Figure 6 ‣ 6.3 Arbitrage ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") represents the structure of the arbitrage strategy and Figure [7](#S6.F7 "Figure 7 ‣ 6.3 Arbitrage ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") plots the corresponding payout. The solution uses both static and dynamic trading and achieves a net payout that never falls below the initial wealth but is likely to end up strictly higher.

![Refer to caption](/html/2008.01463/assets/x6.png)


Figure 6: The structure of the arbitrage strategy

![Refer to caption](/html/2008.01463/assets/x7.png)


Figure 7: The payout of the arbitrage portfolio as a function of X1subscript𝑋1X\_{1} and X2subscript𝑋2X\_{2}

### 6.4 Semi-static problem with transaction costs

We will now study the effect of a bid-ask spread on the dynamically traded underlying. Figure [8](#S6.F8 "Figure 8 ‣ 6.4 Semi-static problem with transaction costs ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") illustrates the structure of the optimal solution when the proportional transaction cost is δ=0.1𝛿0.1\delta=0.1. The optimized options portfolio is sparser than the one obtained with perfectly liquid underlying. In addition, the quantities traded are smaller in the options as well as the index. A kernel density plot of the net payout is given in Figure [9](#S6.F9 "Figure 9 ‣ 6.4 Semi-static problem with transaction costs ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets").

![Refer to caption](/html/2008.01463/assets/x8.png)


Figure 8: The structure of the optimal portfolio by semi-static optimization with 0.1% transaction cost

![Refer to caption](/html/2008.01463/assets/x9.png)


Figure 9: The payout of the optimized portfolio by semi-static optimization as a function of X1subscript𝑋1X\_{1} and X2subscript𝑋2X\_{2} with 0.1% transaction cost. The grey horizontal plane represents the initial wealth.

To examine the effects of the transaction cost further, we study the payouts of the optimized portfolios for varying levels of the transaction costs. The left plot of Figure [10](#S6.F10 "Figure 10 ‣ 6.4 Semi-static problem with transaction costs ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") shows the payout of the optimized portfolio with 0.1% transaction cost subtracted by the payout of the optimized portfolio with 1% transaction cost, whereas the right plot shows the payout of the optimized portfolio with 0.1% transaction cost subtracted by the payout of the optimized portfolio with 10% transaction cost. Figure [11](#S6.F11 "Figure 11 ‣ 6.4 Semi-static problem with transaction costs ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") shows the optimal index quantities bought or sold at t=1𝑡1t=1 obtained with different transaction costs as functions of X1subscript𝑋1X\_{1}.

We see that, for the index values up to 2500, which is the highest strike among the options available in the market, a higher transaction cost results in payouts that tend to be higher when X1subscript𝑋1X\_{1} and X2subscript𝑋2X\_{2} are close to each other. As the transaction cost increases, we invest less in the index at t=1𝑡1t=1; see Figure [11](#S6.F11 "Figure 11 ‣ 6.4 Semi-static problem with transaction costs ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets").

![Refer to caption](/html/2008.01463/assets/x10.png)


Figure 10: The payout of the optimized portfolio with 0.1% transaction cost subtracted by 1% transaction cost’s (left). The payout of the optimized portfolio with 0.1% transaction cost subtracted by 10% transaction cost’s (right).

![Refer to caption](/html/2008.01463/assets/x11.png)


Figure 11: The optimal index quantities bought or sold at t=1𝑡1t=1 by semi-static optimization as functions of X1subscript𝑋1X\_{1} with different transaction costs

Table [4](#S6.T4 "Table 4 ‣ 6.4 Semi-static problem with transaction costs ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") shows how the expected loss function value increases with the transaction cost.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| transaction cost | 0% | 0.1% | 1% | 10% |
| log objective | -2.4404 | -2.3845 | -2.3559 | -2.3136 |

Table 4: Logarithms of the optimum objective values in semi-static optimization with different transaction costs

### 6.5 Dynamic trading without options

To illustrate the benefits of employing buy-and-hold strategies in the quoted options, we will compare the results with a purely dynamic optimization model where we are not allowed to trade the options. Other than that, the model is identical with the ones studied above. The numerical optimization is done with the Galerkin discretization and quadrature approximations as described in Section [4](#S4 "4 Numerical optimization ‣ Optimal semi-static hedging in illiquid markets").

Figure [12](#S6.F12 "Figure 12 ‣ 6.5 Dynamic trading without options ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets") plots the mark-to-market values of the optimal index holding at time t=1𝑡1t=1 as functions of the underlying X1subscript𝑋1X\_{1} for varying levels of transaction costs δ𝛿\delta. When there are no transaction costs, the amount of wealth invested in the underlying does not depend on the value of the underlying except for the more extreme values. This is in line with the theory which says that with exponential utility, the amount of wealth invested in the risky assets is constant. The deviations at the extremes are due to discretization errors. The corresponding terminal wealth of the optimal index position as a function of X1subscript𝑋1X\_{1} and X2subscript𝑋2X\_{2} when there are no transaction costs is given in Figure [13](#S6.F13 "Figure 13 ‣ 6.5 Dynamic trading without options ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets"). With higher transaction costs, the terminal wealth is lower as one would expect, and with 0.20%percent0.200.20\% transaction cost, the terminal wealth is constant as there is no trading at all.

![Refer to caption](/html/2008.01463/assets/figures/moneyInvestedInIndex.jpg)


Figure 12: Mark-to-market value of the index at time t=1𝑡1t=1 as a function of X1subscript𝑋1X\_{1} obtained by dynamic optimization with different transaction costs

![Refer to caption](/html/2008.01463/assets/x12.png)


Figure 13: The payout of the optimized portfolio by purely dynamic optimization when there are no transaction costs. The grey horizontal plane represents the initial wealth.

## 7 Indifference pricing of path-dependent options

To illustrate numerical indifference pricing, we will consider a standard call option and four path-dependent options namely, a knock-out call option with payoff

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(X1,X2)={(X2−K)+if X1<B,0if X1≥B,𝑐subscript𝑋1subscript𝑋2casessuperscriptsubscript𝑋2𝐾if X1<B0if X1≥B,c(X\_{1},X\_{2})=\begin{cases}(X\_{2}-K)^{+}&\text{if $X\_{1}<B$},\\ 0&\text{if $X\_{1}\geq B$,}\end{cases} |  | (1) |

an Asian call option with payoff

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(X1,X2)=(X1+X22−K)+,𝑐subscript𝑋1subscript𝑋2superscriptsubscript𝑋1subscript𝑋22𝐾c(X\_{1},X\_{2})=\bigg{(}\frac{X\_{1}+X\_{2}}{2}-K\bigg{)}^{+}, |  | (2) |

a look-back call option with payoff

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(X1,X2)=maxt=1,2⁡{(Xt−K)+},𝑐subscript𝑋1subscript𝑋2subscript𝑡  12superscriptsubscript𝑋𝑡𝐾c(X\_{1},X\_{2})=\max\_{t=1,2}\{(X\_{t}-K)^{+}\}, |  | (3) |

and a look-back digital call option with payoff

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(X1,X2)={10if X1​or​X2≥K,0otherwise,𝑐subscript𝑋1subscript𝑋2cases10if X1orX2≥K0otherwise,c(X\_{1},X\_{2})=\begin{cases}10&\text{if $X\_{1}\ \text{or}\ X\_{2}\geq K$},\\ 0&\text{otherwise,}\end{cases} |  | (4) |

all with strike K=2,350𝐾

2350K=2,350 and barrier B=2,400𝐵

2400B=2,400. The contract size for all options is 100.

Tables [5](#S7.T5 "Table 5 ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets")–[7](#S7.T7 "Table 7 ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") give the indifference prices for buying and selling as well as the super- and subhedging costs for the above options. The prices in Table [5](#S7.T5 "Table 5 ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") were obtained with semi-static hedging with perfectly liquid underlying while those in Table [6](#S7.T6 "Table 6 ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") were obtained with transaction cost of δ=0.1%𝛿percent0.1\delta=0.1\%. Table [7](#S7.T7 "Table 7 ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") gives the prices obtained without statically held options. To make the pricing of the call option nontrivial, the call option with strike 2,350 is taken out from the hedging instruments when being priced. The super- and subhedging costs are computed on the interval [1000,3000]10003000[1000,3000] instead of all positive real values. This is due to the fact that some options cannot be super- or subhedged for all possible real values resulting in super- and subhedging costs being infinity.

As expected, the indifference prices for the vanilla call option are more expensive than the knock-out option but cheaper than the look-back call option. The indifference prices for the Asian call option are cheaper than the vanilla call option. This is not surprising as X2subscript𝑋2X\_{2} is likely to deviate from X0subscript𝑋0X\_{0} more than from X1subscript𝑋1X\_{1}. The indifference prices for the look-back call option are between 0 and 10 but closer to 10 as it is in the money.

As reported in Section [6.3](#S6.SS3 "6.3 Arbitrage ‣ 6 An application to S&P500 derivatives ‣ Optimal semi-static hedging in illiquid markets"), there is arbitrage opportunity in the semi-static model without transaction costs. Accordingly, the superhedging costs are below the subhedging costs. However, the existence of the arbitrage does not prohibit us from computing sensible indifference prices. One should note that in the presence of arbitrage, the quantity constraints for the options are binding so Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 3 Indifference pricing ‣ Optimal semi-static hedging in illiquid markets") does not apply in the present situation. Adding a 0.1% transaction cost on the underlying removes the arbitrage and puts us back in the setting of Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 3 Indifference pricing ‣ Optimal semi-static hedging in illiquid markets") in terms of the order of the four prices; see Table [6](#S7.T6 "Table 6 ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets").

As expected, adding transaction costs increases superhedging costs and lowers the subhedging costs. Removing the statically traded options has a similar effect. This is simply because the construction of a superhedging strategy becomes cheaper when trading costs are reduced. The same does not apply to indifference pricing because both sides of the indifference inequality increase when trading becomes more expensive.

Without the statically traded options, the true superhedging cost is +∞+\infty for all but the digital option. Accordingly, the numerically computed superhedging costs in Table [7](#S7.T7 "Table 7 ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") would converge to infinity when the scenario grid is extended further. Similarly, the true subhedging costs of all but the call and Asian option are zero.

| claim | subhedging | buying price | selling price | superhedging |
| --- | --- | --- | --- | --- |
| call | 52.9626 | 45.3296 | 45.3939 | 37.4974 |
| knock-out call | 18.1167 | 22.4763 | 22.7125 | 18.6974 |
| Asian | 38.9026 | 35.0562 | 35.1019 | 29.8066 |
| look-back call | 53.6604 | 53.9293 | 54.0110 | 51.5058 |
| look-back digital | 14.4026 | 7.6834 | 7.6966 | 0.6058 |

Table 5: Indifference prices, together with super- and subhedging costs by semi-static hedging without transaction costs on the underlying



| claim | subhedging | buying price | selling price | superhedging |
| --- | --- | --- | --- | --- |
| call | 43.4250 | 44.5308 | 44.8265 | 45.8000 |
| knock-out call | 4.8957 | 20.6770 | 21.1444 | 29.5397 |
| Asian | 29.8327 | 35.0303 | 35.2427 | 38.9201 |
| look-back call | 43.9763 | 53.7226 | 54.0400 | 61.1320 |
| look-back digital | 5.2640 | 7.5498 | 7.5663 | 9.2374 |

Table 6: Indifference prices, together with super- and subhedging costs by semi-static hedging with 0.1% transaction cost on the underlying



| claim | subhedging | buying price | selling price | superhedging |
| --- | --- | --- | --- | --- |
| call | 10.0000 | 49.9490 | 51.2605 | 442.0000 |
| knock-out call | 0.0000 | 15.3326 | 16.5480 | 442.0000 |
| Asian | 0.0000 | 41.1187 | 42.1857 | 442.0000 |
| look-back call | 10.0000 | 60.4879 | 62.3530 | 485.2906 |
| look-back digital | 0.1538 | 6.4321 | 6.4469 | 10.0000 |

Table 7: Indifference prices, together with super- and subhedging costs by two-period dynamic hedging without statically held options

The hedging portfolios, which are x−x¯𝑥¯𝑥x-\bar{x} and z−z¯𝑧¯𝑧z-\bar{z} where x¯¯𝑥\bar{x} and x𝑥x are options portfolios, and z¯¯𝑧\bar{z} and z𝑧z are index quantities before and after selling the options, as well as their payouts for each hedging will be shown in the later subsections.

### 7.1 Optimal hedges

Figure [14](#S7.F14 "Figure 14 ‣ 7.1 Optimal hedges ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") illustrates the hedging strategy for selling one contract of the call option strike K=2,350𝐾

2350K=2,350. This includes the hedging portfolio, as well as its payout plotted together with the payoff (grids) of the call option. The payouts of the hedging portfolios for the other options are shown in Figure [15](#S7.F15 "Figure 15 ‣ 7.1 Optimal hedges ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets"). We see that the path-dependent exotic options can be hedged reasonably well especially for the scenarios with higher probability of occurring.

![Refer to caption](/html/2008.01463/assets/x13.png)


Figure 14: The hedging portfolio for selling one contract of a call option with strike 2,350.

![Refer to caption](/html/2008.01463/assets/x14.png)


Figure 15: The payouts of the hedging portfolios for selling one contract of a knockout call option, Asian call option, look-back call option, and look-back digital option all with strike 2,350 and barrier 2,400.

### 7.2 Optimal hedges with transaction costs

Figure [16](#S7.F16 "Figure 16 ‣ 7.2 Optimal hedges with transaction costs ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") illustrates the hedging strategy for selling one contract of the call option strike K=2,350𝐾

2350K=2,350 when the underlying is subject to 0.1% transaction cost. The payouts of the hedging portfolios for the other options are shown in Figure [15](#S7.F15 "Figure 15 ‣ 7.1 Optimal hedges ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets").

![Refer to caption](/html/2008.01463/assets/x15.png)


Figure 16: The hedging portfolio for selling one contract of a call option with strike 2,350 with 0.01% transaction cost.

![Refer to caption](/html/2008.01463/assets/x16.png)


Figure 17: The payouts of the hedging portfolios for selling one contract of a knockout call option, Asian call option, look-back call option, and look-back digital option all with strike 2,350 with 0.01% transaction cost.

Despite having the transaction cost, the path-dependent options are still hedged well. However, the lower the transaction cost, the better the hedge as we can see from Figure [18](#S7.F18 "Figure 18 ‣ 7.2 Optimal hedges with transaction costs ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") which shows the payouts of the hedging portfolios for selling the look-back call option with strike 2,350 when the transaction costs are 1 and 10 percents. The semi-static hedging with the 10% transaction cost coincides with the static hedging as the underlying is not traded. Note that static hedging is a special case of semi-static hedging. We see that the 2-dimensional shapes of the payout are identical for any given values of X1subscript𝑋1X\_{1} or X2subscript𝑋2X\_{2}

![Refer to caption](/html/2008.01463/assets/x17.png)


Figure 18: The payouts of hedging portfolios for selling one contract of a lookback call option with strike 2350 with 1% and 10% transaction costs.

### 7.3 Optimal hedging without options

Figure [19](#S7.F19 "Figure 19 ‣ 7.3 Optimal hedging without options ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") illustrates the hedging strategy for selling one contract of the call option strike K=2,350𝐾

2350K=2,350 by two-period dynamic hedging. The payouts of the hedging portfolios for the other options are shown in Figure [20](#S7.F20 "Figure 20 ‣ 7.3 Optimal hedging without options ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets"). Only cash and the underlying, allowed to be traded without transaction costs at t=0,1𝑡

01t=0,1, are the hedging instruments. We see that, without the call and put options as the hedging instruments, they badly hedge the options. However, hedging portfolios tend to be more profitable when X1subscript𝑋1X\_{1} and X2subscript𝑋2X\_{2} are close to each other which is an area with higher probability of occurring.

![Refer to caption](/html/2008.01463/assets/x18.png)


Figure 19: The quantity of the index bought at t=1𝑡1t=1 as a function of X1subscript𝑋1X\_{1} of the hedging portfolio for selling one contract of a call option with strike 2,350 by dynamic strategy (left) and its payout (right).

![Refer to caption](/html/2008.01463/assets/x19.png)


Figure 20: The payouts of the hedging portfolios for selling one contract of a knockout call option, Asian call option, look-back call option, and look-back digital option all with strike 2,350 and barrier 2,400 by dynamic hedging.

The quantity of trade in the index as shown in Figure [19](#S7.F19 "Figure 19 ‣ 7.3 Optimal hedging without options ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") looks similar to the one of the delta hedging. This is very surprising because the dynamic hedging is implemented in a two-period setting, whereas the delta hedging is a continuous trading strategy. The indifference prices for buying and selling are 49.9490 and 51.2605, whereas the Black-Scholes price with μ=0𝜇0\mu=0 and σ=0.1206𝜎0.1206\sigma=0.1206 is 50.7242. Indifference prices depend on an agent’s initial position, risk preference and market liquidity, while the Black-Scholes price does not.

Figure [21](#S7.F21 "Figure 21 ‣ 7.3 Optimal hedging without options ‣ 7 Indifference pricing of path-dependent options ‣ Optimal semi-static hedging in illiquid markets") shows the quantities of the index traded at t=1𝑡1t=1 of the hedging portfolios for selling one contract of a call option with strike 2,350 as functions of X1subscript𝑋1X\_{1} obtained by two-period dynamic hedging with different transaction costs. We see that the quantities traded in the underlying at both t=0𝑡0t=0 and t=1𝑡1t=1 decrease as the transaction cost increases. Except at the tails, which have low probability of occurring, the strategies are to buy some underlying at the beginning and buy more if it goes up or sell if it goes down. However, we see that, for the 0.2%percent0.20.2\% transaction cost, it is optimal to do nothing at t=1𝑡1t=1 if the index value at t=1𝑡1t=1 is below 2400.

![Refer to caption](/html/2008.01463/assets/figures/differentTrans.jpg)


Figure 21: The quantities of the index traded at t=1𝑡1t=1 of the hedging portfolios for selling one contract of a call option with strike 2,350 as functions of X1subscript𝑋1X\_{1} by two-period dynamic hedging with different transaction costs.

## References

* APR [18]

  J. Armstrong, T. Pennanen, and U. Rakwongwan.
  Pricing index options by static hedging under finite liquidity.
  International Journal of Theoretical and Applied Finance,
  21(06):1850044, 2018.
* ApS [15]

  MOSEK ApS.
  The MOSEK optimization toolbox for MATLAB manual. Version 7.1
  (Revision 28), 2015.
* BHLP [13]

  M. Beiglböck, P. Henry-Labordère, and F. Penkner.
  Model-independent bounds for option prices—a mass transport
  approach.
  Finance Stoch., 17(3):477–501, 2013.
* Büh [70]

  H. Bühlmann.
  Mathematical methods in risk theory.
  Die Grundlehren der mathematischen Wissenschaften, Band 172.
  Springer-Verlag, New York, 1970.
* Car [09]

  R. Carmona, editor.
  Indifference pricing: theory and applications.
  Princeton series in financial engineering. Princeton University
  Press, Princeton, NJ, 2009.
* FS [11]

  H. Föllmer and A. Schied.
  Stochastic finance.
  Walter de Gruyter & Co., Berlin, extended edition, 2011.
  An introduction in discrete time.
* GOo [19]

  G. Guo and J. Obł ój.
  Computational methods for martingale optimal transport problems.
  Ann. Appl. Probab., 29(6):3311–3347, 2019.
* HN [89]

  S. D. Hodges and A. Neuberger.
  Optimal replication of contingent claims under transaction costs.
  Reviev of Futures Markets, 8:222–239, 1989.
* IJS [04]

  A. Ilhan, M. Jonsson, and R. Sircar.
  Portfolio optimization with derivatives and indifference pricing.
  In R. Carmona, editor, Indifference pricing -theory and
  applications, pages 183–210. Princeton University Press, 2004.
* IJS [08]

  A. Ilhan, M. Jonsson, and R. Sircar.
  Optimal static-dynamic hedges for exotic options under convex risk
  measures.
  SSRN Electronic Journal, 2008.
* IS [06]

  A. Ilhan and R. Sircar.
  Optimal static-dynamic hedges for barrier options.
  Mathematical Finance, 16(2):359–385, 2006.
* MCC [98]

  D. Madan, P. Carr, and E. Chang.
  The Variance Gamma Process and Option Pricing.
  Review of Finance, 2(1):79–105, 04 1998.
* MS [90]

  D. Madan and E. Seneta.
  The variance gamma (v.g.) model for share market returns.
  The Journal of Business, 63(4):511–524, 1990.
* Pen [14]

  T. Pennanen.
  Optimal investment and contingent claim valuation in illiquid
  markets.
  Finance Stoch., 18(4):733–754, 2014.
* PP [18]

  T. Pennanen and A.-P. Perkkiö.
  Convex duality in optimal investment and contingent claim valuation
  in illiquid markets.
  Finance Stoch., 22(4):733–771, 2018.
* PP [19]

  T. Pennanen and A.-P. Perkkiö.
  Convex duality in nonlinear optimal transport.
  J. Funct. Anal., 277(4):1029–1060, 2019.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2008.01463)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2008.01463)
[View original  
on arXiv](https://arxiv.org/abs/2008.01463)[►](javascript: void(0))