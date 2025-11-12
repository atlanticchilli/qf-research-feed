---
authors:
- Kevin S. Zhang
- Traian A. Pirvu
doc_id: arxiv:2006.07771v1
family_id: arxiv:2006.07771
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2006.07771] Numerical Simulation of Exchange Option with Finite Liquidity:
  Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.'
url_abs: http://arxiv.org/abs/2006.07771v1
url_html: https://ar5iv.org/html/2006.07771v1
venue: arXiv q-fin
version: 1
year: 2020
---


Kevin S. Zhang
Department of Mathematics and Statistics, McMaster University, Hamilton, ON, Canada.
  
Traian A. Pirvu33footnotemark: 3
Department of Mathematics and Statistics, McMaster University, Hamilton, ON, Canada.

###### Abstract

In this paper we develop numerical pricing methodologies for European style Exchange Options written on a pair of correlated assets, in a market with finite liquidity. In contrast to the standard multi-asset Black-Scholes framework, trading in our market model has a direct impact on the asset’s price. The price impact is incorporated into the dynamics of the first asset through a specific trading strategy, as in large trader liquidity model. Two-dimensional Milstein scheme is implemented to simulate the pair of assets prices. The option value is numerically estimated by Monte Carlo with the Margrabe option as controlled variate. Time complexity of these numerical schemes are included. Finally, we provide a deep learning framework to implement this model effectively in a production environment.

###### keywords:

Exchange Option, FX, price impact, XVA, illiquid market, Monte Carlo, deep learning

{AMS}

91G20, 68T99, 65C30, 65C05

## 1 Introduction

The Black-Scholes (BS) model was truly a breakthrough for pricing single asset options. It assumes participants operate in a perfectly liquid, friction-less and complete market. In practice, one or more of these assumptions are violated. When the liquidity restriction is relaxed, trading will impact the price of the underlying assets. Wilmott (2000) [[28](#bib.bib28)] was one of the pioneers of these price impact models. He considered price impacts depending upon different trading strategies such as buy and hold, limit order and portfolio optimization. To account for price impact, Liu and Yong (2005) [[18](#bib.bib18)] included an additional term in the asset price stochastic differential equation (SDE). This inclusion indirectly adds a valuation adjustment to the price of the option. Such an adjustment stems from a lack of liquidity, and may be classified as liquidity valuation adjustment (LVA). Various non-linear BS-like partial differential equations (PDE), capturing the resulting price impact from trading have been studied [[12](#bib.bib12), [6](#bib.bib6), [1](#bib.bib1), [4](#bib.bib4)]. All these models share the similarity of being single-asset LVA models.

Exchange Options provide the utility of exchanging one asset for another. Under the BS assumption for binary asset markets, Margrabe (1978) [[19](#bib.bib19)] derived a closed form solution for the price of Exchange Options. The Exchange Option plays an essential role in currency markets. The Foreign Exchange (FX) Option is an Exchange Option where the assets are currencies. A common concern is raised when one considers the interaction between liquid and illiquid currencies. A trader might ask, “How reliable is the price of a 3-month European style USD/UAH (Ukrainian Hryvnia, an infrequently traded currency) FX Option?”. In this work, we are interested in these type of scenarios. Recent studies on Exchange Options, such as [[3](#bib.bib3), [2](#bib.bib2), [27](#bib.bib27), [13](#bib.bib13)], exhibit deviation from the assumptions of BS. The aforementioned studies predominately involve stochastic volatility models. Similar to Exchange Options, studies on Spread Option pricing have been conducted in the presence of full or partial price impact [[25](#bib.bib25), [22](#bib.bib22)].

In this paper, we consider a binary-asset market with a single illiquid asset. Under this consideration, we construct a price impact model, called the finite liquidity market model (FLMM). The model is a system of SDEs, one for each asset. The liquid asset is unchanged, the illiquid is modified to incorporate the resulting price impact from trading. Existence and uniqueness conditions on the SDES are established for the FLMM (see [section 7](#S7 "7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")). By replicating a portfolio, We derive the partial differential equation (PDE) characterization of option prices. Further, we consider a market consisting of market makers, who trade by Delta Hedging. We utilize the Milstein method and simulate the FLMM SDEs as inspired by [[10](#bib.bib10), [14](#bib.bib14)]. The Margrabe Exchange Option is used as the control variate for our Monte Carlo (MC) pricing of the option. Motivated by [[7](#bib.bib7), [5](#bib.bib5)], we apply deep feed-forward network to our MC pricing engine and achieves accurate high speed pricing.

The remainder of the content written in this paper is organized in the following sections. Section [2](#S2 "2 Model Framework ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.") discusses the model framework. In Section [3](#S3 "3 Analysis of Replication of Exchange Option by Delta Hedging as Price Impact ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700."), we analyze the price impact effect when majority of the market participants implement Delta Hedging. In Section [4](#S4 "4 Numerical Simulations ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700."), we apply Milstein’s method to simulate the path-wise price and sensitivity. Subsequently, we deploy control variate MC for estimation. Section [5](#S5 "5 Deep Learning Method ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.") contains the methodology of Deeply Learning Derivative for Exchange Option with price impact. In Section [6](#S6 "6 Conclusions ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700."), we make some concluding statements for the readers. The last Section is an Appendix containing the proofs of our results.

## 2 Model Framework

In this section we describe the dynamics of FLMM. There is a filtered probability space (Ω,ℙ,ℱ​(t))Ωℙℱ𝑡\big{(}\Omega,\mathbb{P},\mathscr{F}(t)\big{)} that satisfies the usual conditions. There are two risky assets whose prices are assumed to be a two-dimensional correlated It̂o process 𝐒​(t)=(S1​(t),S2​(t))𝐒𝑡subscript𝑆1𝑡subscript𝑆2𝑡\mathbf{S}(t)=\big{(}S\_{1}(t),S\_{2}(t)\big{)}. There is also a risk-free asset D​(t).𝐷𝑡D(t). The uncertainty in this model is driven by a two-dimensional independent Brownian Motion 𝐖​(t)=(W1​(t),W2​(t))𝐖𝑡subscript𝑊1𝑡subscript𝑊2𝑡\mathbf{W}(t)=\big{(}W\_{1}(t),W\_{2}(t)\big{)}. The system of SDEs which captures the asset price dynamics can be illustrated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | d​S1​(t)S1​(t)=μ1​(t)​d​t+σ1​d​W1​(t)+λ​(t,S1​(t),S2​(t))​d​f​(t,S1​(t),S2​(t)),𝑑subscript𝑆1𝑡subscript𝑆1𝑡subscript𝜇1𝑡𝑑𝑡subscript𝜎1𝑑subscript𝑊1𝑡𝜆𝑡subscript𝑆1𝑡subscript𝑆2𝑡𝑑𝑓𝑡subscript𝑆1𝑡subscript𝑆2𝑡\displaystyle\frac{dS\_{1}(t)}{S\_{1}(t)}=\mu\_{1}(t)dt+\sigma\_{1}dW\_{1}(t)+\lambda\big{(}t,S\_{1}(t),S\_{2}(t)\big{)}df\big{(}t,S\_{1}(t),S\_{2}(t)\big{)}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (1) |  |  | d​S2​(t)S2​(t)=μ2​(t)​d​t+σ2​ρ​d​W1​(t)+σ2​1−ρ2​d​W2​(t),𝑑subscript𝑆2𝑡subscript𝑆2𝑡subscript𝜇2𝑡𝑑𝑡subscript𝜎2𝜌𝑑subscript𝑊1𝑡subscript𝜎21superscript𝜌2𝑑subscript𝑊2𝑡\displaystyle\frac{dS\_{2}(t)}{S\_{2}(t)}=\mu\_{2}(t)dt+\sigma\_{2}\rho{}dW\_{1}(t)+\sigma\_{2}\sqrt{1-\rho^{2}}dW\_{2}(t), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | d​D​(t)D​(t)=−r​d​t,𝑑𝐷𝑡𝐷𝑡𝑟𝑑𝑡\displaystyle\frac{dD(t)}{D(t)}=-rdt, |  |

where μi​(t)subscript𝜇𝑖𝑡\mu\_{i}(t), σisubscript𝜎𝑖\sigma\_{i}, ρ𝜌\rho are the drift process, volatility and correlation of each It̂o Process respectively. The novelty here is the term λ​(t,S1​(t),S2​(t))​d​f​(t,S1​(t),S2​(t)),𝜆𝑡subscript𝑆1𝑡subscript𝑆2𝑡𝑑𝑓𝑡subscript𝑆1𝑡subscript𝑆2𝑡\lambda\big{(}t,S\_{1}(t),S\_{2}(t)\big{)}df\big{(}t,S\_{1}(t),S\_{2}(t)\big{)}, and it represents the price impact λ​(t,s1,s2)𝜆𝑡subscript𝑠1subscript𝑠2\lambda(t,s\_{1},s\_{2}) from a trading strategy f​(t,s1,s2).𝑓𝑡subscript𝑠1subscript𝑠2f(t,s\_{1},s\_{2}). We will assumed the price impact is always non-negative, that is λ​(t,s1,s2)≥0.𝜆𝑡subscript𝑠1subscript𝑠20\lambda(t,s\_{1},s\_{2})\geq{0}. Let us point out the two-dimensional market model used by Margrabe (1978) [[19](#bib.bib19)] is a special case of this model when λ​(t,s1,s2)=0𝜆𝑡subscript𝑠1subscript𝑠20\lambda(t,s\_{1},s\_{2})=0.

We plan to obtain a canonical SDE of Asset 1,11, and this will allow for a better understanding of the model’s dynamics. In order to achieve this, we first apply Itô’s Theorem to compute the following differential d​f​(t,S1​(t),S2​(t)).𝑑𝑓𝑡subscript𝑆1𝑡subscript𝑆2𝑡df\big{(}t,S\_{1}(t),S\_{2}(t)\big{)}. Then, we isolate the d​S1​(t)𝑑subscript𝑆1𝑡dS\_{1}(t) terms, and compute the following quadratic/cross-variation terms: d​S1​(t)​d​S1​(t)𝑑subscript𝑆1𝑡𝑑subscript𝑆1𝑡dS\_{1}(t)dS\_{1}(t), d​S1​(t)​d​S2​(t)𝑑subscript𝑆1𝑡𝑑subscript𝑆2𝑡dS\_{1}(t)dS\_{2}(t) and d​S2​(t)​d​S2​(t)𝑑subscript𝑆2𝑡𝑑subscript𝑆2𝑡dS\_{2}(t)dS\_{2}(t). By doing so we arrive at:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2) |  | d​S1​(t)𝑑subscript𝑆1𝑡\displaystyle dS\_{1}(t) | =μ¯1​(𝐒​(t))​d​t+σ¯11​(𝐒​(t))​d​W1​(t)+σ¯12​(𝐒​(t))​d​W2​(t),absentsubscript¯𝜇1𝐒𝑡𝑑𝑡subscript¯𝜎11𝐒𝑡𝑑subscript𝑊1𝑡subscript¯𝜎12𝐒𝑡𝑑subscript𝑊2𝑡\displaystyle=\bar{\mu}\_{1}\big{(}\mathbf{S}(t)\big{)}dt+\bar{\sigma}\_{11}\big{(}\mathbf{S}(t)\big{)}dW\_{1}(t)+\bar{\sigma}\_{12}\big{(}\mathbf{S}(t)\big{)}dW\_{2}(t), |  |

where the drift and diffusion functions are:

|  |  |  |
| --- | --- | --- |
|  | μ¯1(t,s1,s2)=11−λ​fs1(μ1s1+λft+s2μ2λfs2+fs1​s2​(ρ​σ1​σ2​s1​s2+σ22​s22​λ​fs2)1−λ​fs1\displaystyle\bar{\mu}\_{1}(t,s\_{1},s\_{2})=\frac{1}{1-\lambda{}f\_{s\_{1}}}\Big{(}\mu\_{1}s\_{1}+\lambda{}f\_{t}+s\_{2}\mu\_{2}\lambda{}f\_{s\_{2}}+\frac{f\_{s\_{1}s\_{2}}(\rho\sigma\_{1}\sigma\_{2}s\_{1}s\_{2}+\sigma\_{2}^{2}s\_{2}^{2}\lambda{}f\_{s\_{2}})}{1-\lambda{}f\_{s\_{1}}} |  |
|  |  |  |
| --- | --- | --- |
|  | +fs1​s1​(σ12​s12+σ22​s22​λ2​fs22+2​ρ​σ1​σ2​s1​s2​λ​fs2)2​(1−λ​fs1)2+σ22​s22​fs2​s22),\displaystyle\qquad\qquad\quad+\frac{f\_{s\_{1}s\_{1}}(\sigma\_{1}^{2}s\_{1}^{2}+\sigma^{2}\_{2}s\_{2}^{2}\lambda^{2}f\_{s\_{2}}^{2}+2\rho\sigma\_{1}\sigma\_{2}s\_{1}s\_{2}\lambda{}f\_{s\_{2}})}{2\big{(}1-\lambda{}f\_{s\_{1}}\big{)}^{2}}+\frac{\sigma\_{2}^{2}s\_{2}^{2}f\_{s\_{2}s\_{2}}}{2}\Big{)}, |  |
|  |  |  |
| --- | --- | --- |
|  | σ¯11​(t,s1,s2)=σ1​s11−λ​fs1,σ¯12​(t,s1,s2)=σ2​s2​λ​fs21−λ​fs1.formulae-sequencesubscript¯𝜎11𝑡subscript𝑠1subscript𝑠2subscript𝜎1subscript𝑠11𝜆subscript𝑓subscript𝑠1subscript¯𝜎12𝑡subscript𝑠1subscript𝑠2subscript𝜎2subscript𝑠2𝜆subscript𝑓subscript𝑠21𝜆subscript𝑓subscript𝑠1\displaystyle\bar{\sigma}\_{11}(t,s\_{1},s\_{2})=\frac{\sigma\_{1}s\_{1}}{1-\lambda{}f\_{s\_{1}}},\qquad\bar{\sigma}\_{12}(t,s\_{1},s\_{2})=\frac{\sigma\_{2}s\_{2}\lambda{}f\_{s\_{2}}}{1-\lambda{}f\_{s\_{1}}}. |  |

With the model dynamics in hand, we can determine the requirements for the SDE driving S1subscript𝑆1S\_{1} to have a unique solution. In classical literature on SDE such as Oksendal (1992) [[21](#bib.bib21)], there are classical theorems for the existence and uniqueness of different kinds (strong, weak) solutions. The following theorem provides sufficient conditions for the existence and uniqueness of FLMM SDEs:

###### Theorem 2.1 (Finite Liquidity Existence and Uniqueness Theorem I).

Under the assumptions (1)1(1) to (6)6(6) of ([7.1](#S7.SS1 "7.1 Finite Liquidity Existence and Uniqueness Theorem I ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")), the SDE of
S1subscript𝑆1S\_{1} in ([2](#S2.E2 "Equation 2 ‣ 2 Model Framework ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")) has a unique strong solution.

###### Proof 2.2.

Please refer to the Appendix Section [7.1](#S7.SS1 "7.1 Finite Liquidity Existence and Uniqueness Theorem I ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.").

The replicating portfolio argument is fundamental to the derivations of BS equation. The replication argument in Chapter 4.5 of Shreve (2004) [[26](#bib.bib26)] can be modified to replicate the option within FLMM framework. The portfolio used for replication will have two assets and one cash account. The resulting equation will be a linear BS-like PDE of the parabolic family:

|  |  |  |
| --- | --- | --- |
|  | {r​V=Vt+r​s1​Vs1+r​s2​Vs2+Vs1​s21−λ​fs1​(ρ​σ1​σ2​s1​s2+λ​fs2​σ22​s22)+Vs1​s12​(1−λ​fs1)2​(σ12​s12+λ2​fs22​σ22​s22+2​λ​fs2​ρ​σ1​σ2​s1​s2)+12​Vs2​s2​σ22​s22,V​(T,s1,s2)=h​(s1,s2),with 0<s1,s2<∞, 0≤t≤T,\left\{\begin{aligned} rV&=V\_{t}+rs\_{1}V\_{s\_{1}}+rs\_{2}V\_{s\_{2}}+\frac{V\_{s\_{1}s\_{2}}}{1-\lambda{}f\_{s\_{1}}}\big{(}\rho\sigma\_{1}\sigma\_{2}s\_{1}s\_{2}+\lambda{}f\_{s\_{2}}\sigma\_{2}^{2}s\_{2}^{2}\big{)}\cr&+\frac{V\_{s\_{1}s\_{1}}}{2(1-\lambda{}f\_{s\_{1}})^{2}}\big{(}\sigma\_{1}^{2}s\_{1}^{2}+\lambda^{2}f\_{s\_{2}}^{2}\sigma^{2}\_{2}s\_{2}^{2}+2\lambda{}f\_{s\_{2}}\rho\sigma\_{1}\sigma\_{2}s\_{1}s\_{2}\big{)}+\frac{1}{2}V\_{s\_{2}s\_{2}}\sigma\_{2}^{2}s\_{2}^{2},\cr V(T,s\_{1},s\_{2})&=h(s\_{1},s\_{2}),\quad\text{with $0<s\_{1},s\_{2}<\infty$, $0\leq{t}\leq{T}$},\end{aligned}\right. |  |

where h​(s1,s2)ℎsubscript𝑠1subscript𝑠2h(s\_{1},s\_{2}) is a general payoff function. Existence results in Chapter 4 of Friedman (1975) [[8](#bib.bib8)] yield a unique classical solution for this PDE, granted 1−λ​fs11𝜆subscript𝑓subscript𝑠11-\lambda{}f\_{s\_{1}} satisfies condition (3)3(3) of Theorem [2.1](#S2.Thmtheorem1 "Theorem 2.1 (Finite Liquidity Existence and Uniqueness Theorem I). ‣ 2 Model Framework ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.").

Feynman-Kac formula allows that the solutions for this PDE to be represented as a conditional expectations. As a by product of Feynman-Kac, we will discover an induced risk-neutral measure ℙ~~ℙ\widetilde{\mathbbm{P}}. Under this measure, we have the pricing formula:

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | V​(t,s1,s2)=𝔼~t,s1,s2​[e−r​(T−t)​V​(T,S1​(T),S2​(T))].𝑉𝑡subscript𝑠1subscript𝑠2superscript~𝔼  𝑡subscript𝑠1subscript𝑠2delimited-[]superscript𝑒𝑟𝑇𝑡𝑉𝑇subscript𝑆1𝑇subscript𝑆2𝑇\displaystyle V\big{(}t,s\_{1},s\_{2}\big{)}=\widetilde{\mathbb{E}}^{t,s\_{1},s\_{2}}[e^{-r(T-t)}V\big{(}T,S\_{1}(T),S\_{2}(T)\big{)}]. |  |

## 3 Analysis of Replication of Exchange Option by Delta Hedging as Price Impact

In this section, we show that FLMM has a unique strong solution for a specific choice of price impact λ​(t,S1​(t))​d​f​(t,S1​(t),S2​(t))𝜆𝑡subscript𝑆1𝑡𝑑𝑓𝑡subscript𝑆1𝑡subscript𝑆2𝑡\lambda\big{(}t,S\_{1}(t)\big{)}df\big{(}t,S\_{1}(t),S\_{2}(t)\big{)}. There have been numerous studies in the past focused on price impacts from trading. For example, Liu and Yong (2005) [[18](#bib.bib18)] studied a price impact model for single asset options. Pirvu et al. (2014) [[25](#bib.bib25)] also studied a price impact model for spread option. In this paper, we adopt the following price impact function:

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | λ¯​(t,s1)={ϵ​(1−e−β​(T−t)32)ifS1¯≤s1≤S¯1,0otherwise,¯𝜆𝑡subscript𝑠1casesitalic-ϵ1superscript𝑒𝛽superscript𝑇𝑡32  if¯subscript𝑆1 subscript𝑠1subscript¯𝑆10otherwise\displaystyle\bar{\lambda}\big{(}t,s\_{1}\big{)}=\begin{cases}\epsilon\big{(}1-e^{-\beta(T-t)^{\frac{3}{2}}}\big{)}\quad&\text{if}\quad\underline{S\_{1}}\leq{}s\_{1}\leq\overline{S}\_{1},\\ 0\quad&\text{otherwise},\end{cases} |  |

where S1¯¯subscript𝑆1\underline{S\_{1}} and S¯1subscript¯𝑆1\overline{S}\_{1} represents a trading floor and cap of the asset respectively. This cause the trading price impact to be truncated within the floor and cap. As for the other parameters, ϵitalic-ϵ\epsilon is the price impact per share, and β𝛽\beta is a decaying constant.
It is important to emphasize that λ¯​(t,s1)¯𝜆𝑡subscript𝑠1\bar{\lambda}(t,s\_{1}) will be employed for numerical approximation. The theoretical λ​(t,s1)𝜆𝑡subscript𝑠1\lambda(t,s\_{1}) should be a function with bounded derivative, that is obtained through standard mollifying λ¯​(t,s1)¯𝜆𝑡subscript𝑠1\bar{\lambda}(t,s\_{1}).

Delta hedging is a strategy adopted by many big financial institutions to reduce their option portfolio’s exposure against movements in the underlying assets. In this paper, we assume majority of the market participants implement Delta hedging with the Delta of the impact-less Exchange Option. Therefore, we choose the trading strategy function to be Δ1​(t)subscriptΔ1𝑡\Delta\_{1}(t) of Margrabe’s option, that is f​(t,s1,s2)=Δ1​(t)𝑓𝑡subscript𝑠1subscript𝑠2subscriptΔ1𝑡f\big{(}t,s\_{1},s\_{2}\big{)}=\Delta\_{1}(t). The closed form expression for Δ1subscriptΔ1\Delta\_{1} can be found in the Appendix Section ([7.3](#S7.Ex96 "7.3 Margrabe’s Pricing Formula and Greeks ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")).

As a result, the drift and diffusion functions in ([2](#S2.E2 "Equation 2 ‣ 2 Model Framework ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")) have the following dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | μ~1(t,s1,s2)=11−λ​Γ11(μ1s1+λChm1+μ2s2λΓ12+S​p​d112​(ρ​σ1​σ2​s1​s2+σ22​s22​λ​Γ12)1−λ​Γ11\displaystyle\widetilde{\mu}\_{1}(t,s\_{1},s\_{2})=\frac{1}{1-\lambda\Gamma\_{11}}\Big{(}\mu\_{1}s\_{1}+\lambda{}Chm\_{1}+\mu\_{2}s\_{2}\lambda\Gamma\_{12}+\frac{Spd\_{112}(\rho\sigma\_{1}\sigma\_{2}s\_{1}s\_{2}+\sigma\_{2}^{2}s\_{2}^{2}\lambda\Gamma\_{12})}{1-\lambda\Gamma\_{11}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +S​p​d111​(σ12​s12+σ22​s22​λ2​Γ122+2​ρ​σ1​σ2​s1​s2​λ​Γ12)2​(1−λ​Γ11)2+σ22​s22​S​p​d1222),\displaystyle\qquad\qquad\quad+\frac{Spd\_{111}(\sigma\_{1}^{2}s\_{1}^{2}+\sigma^{2}\_{2}s\_{2}^{2}\lambda^{2}\Gamma\_{12}^{2}+2\rho\sigma\_{1}\sigma\_{2}s\_{1}s\_{2}\lambda\Gamma\_{12})}{2(1-\lambda\Gamma\_{11})^{2}}+\frac{\sigma\_{2}^{2}s\_{2}^{2}Spd\_{122}}{2}\Big{)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | σ~11​(t,s1,s2)=σ1​s11−λ​Γ11,σ~12​(t,s1,s2)=σ2​s2​λ​Γ121−λ​Γ11.formulae-sequencesubscript~𝜎11𝑡subscript𝑠1subscript𝑠2subscript𝜎1subscript𝑠11𝜆subscriptΓ11subscript~𝜎12𝑡subscript𝑠1subscript𝑠2subscript𝜎2subscript𝑠2𝜆subscriptΓ121𝜆subscriptΓ11\displaystyle\widetilde{\sigma}\_{11}(t,s\_{1},s\_{2})=\frac{\sigma\_{1}s\_{1}}{1-\lambda\Gamma\_{11}},\qquad\widetilde{\sigma}\_{12}(t,s\_{1},s\_{2})=\frac{\sigma\_{2}s\_{2}\lambda\Gamma\_{12}}{1-\lambda\Gamma\_{11}}. |  |

Here C​h​m𝐶ℎ𝑚Chm, ΓΓ\Gamma and S​p​d𝑆𝑝𝑑Spd are higher order Greeks of Magrabe’s option derived from Margrabe’s formula. All the Greek formulas are given in the Appendix section [7.3](#S7.Ex96 "7.3 Margrabe’s Pricing Formula and Greeks ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.").

###### Theorem 3.1 (Existence and Uniqueness of Finite Liquidity Market Model SDE II).

The SDE of S1subscript𝑆1S\_{1} with drift and diffusion function of ([7.3](#S7.Ex96 "7.3 Margrabe’s Pricing Formula and Greeks ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")) has a unique strong solution.

###### Proof 3.2.

Please refer to Appendix [7.1](#S7.SS1 "7.1 Finite Liquidity Existence and Uniqueness Theorem I ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.") for the proof.

## 4 Numerical Simulations

In this section, our first objective is to simulate the FLMM assets by applying the Milstein Algorithm. Once we have the asset processes, we can use the results in our control variate MC estimator to price the Exchange Option with price impact. As a naming convention for our analysis, we refer to the number of points M𝑀M used to generate the stochastic assets as “path dimension”. The amount of asset paths N𝑁N used in the MC estimator will be referred to as “space dimension”.

### 4.1 Milstein Scheme for Asset Price

Compared with the more well known Euler-Maruyama, Milstein is a second-order pathwise method for approximating SDE solutions. It was created by Mil’shtein G. N. (1975) [[20](#bib.bib20)], this method retains the second order terms from It̂o Taylor expansion. For a 2-dimensional SDE system satisfied by the process 𝐗​(t)=(X1​(t),X2​(t)),𝐗𝑡subscript𝑋1𝑡subscript𝑋2𝑡\mathbf{X}(t)=\big{(}X\_{1}(t),X\_{2}(t)\big{)}, a second-order approximation of the solution is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | X1​(t)subscript𝑋1𝑡\displaystyle X\_{1}(t) | ≈X1​(t0)+∫t0tμ1​(𝐗​(u))​𝑑u+∫t0tσ11​(𝐗​(u))​𝑑W1​(u)+∫t0tσ12​(𝐗​(u))​𝑑W2​(u)absentsubscript𝑋1subscript𝑡0superscriptsubscriptsubscript𝑡0𝑡subscript𝜇1𝐗𝑢differential-d𝑢superscriptsubscriptsubscript𝑡0𝑡subscript𝜎11𝐗𝑢differential-dsubscript𝑊1𝑢superscriptsubscriptsubscript𝑡0𝑡subscript𝜎12𝐗𝑢differential-dsubscript𝑊2𝑢\displaystyle\approx{}X\_{1}(t\_{0})+\int\_{t\_{0}}^{t}\mu\_{1}\big{(}\mathbf{X}(u)\big{)}du+\int\_{t\_{0}}^{t}\sigma\_{11}\big{(}\mathbf{X}(u)\big{)}dW\_{1}(u)+\int\_{t\_{0}}^{t}\sigma\_{12}\big{(}\mathbf{X}(u)\big{)}dW\_{2}(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​∑j,k,l=12∂σ1​j∂xl​σl​k​(𝐗​(t0))​(Δ​Wj​(t)​Δ​Wk​(t)+ρj​k​(t−t0)−𝒜j​k​(t0,t)),12superscriptsubscript  𝑗𝑘𝑙 12subscript𝜎1𝑗subscript𝑥𝑙subscript𝜎𝑙𝑘𝐗subscript𝑡0Δsubscript𝑊𝑗𝑡Δsubscript𝑊𝑘𝑡subscript𝜌𝑗𝑘𝑡subscript𝑡0subscript𝒜𝑗𝑘subscript𝑡0𝑡\displaystyle+\frac{1}{2}\sum\_{j,k,l=1}^{2}\frac{\partial\sigma\_{1j}}{\partial{}x\_{l}}\sigma\_{lk}\big{(}\mathbf{X}(t\_{0})\big{)}\big{(}\Delta{W}\_{j}(t)\Delta{W}\_{k}(t)+\rho\_{jk}(t-t\_{0})-\mathcal{A}\_{jk}(t\_{0},t)\big{)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | X2​(t)subscript𝑋2𝑡\displaystyle X\_{2}(t) | ≈X2​(t0)+∫t0tμ2​(𝐗​(u))​𝑑u+∫t0tσ21​(𝐗​(u))​𝑑W1​(u)+∫t0tσ22​(𝐗​(u))​𝑑W2​(u)absentsubscript𝑋2subscript𝑡0superscriptsubscriptsubscript𝑡0𝑡subscript𝜇2𝐗𝑢differential-d𝑢superscriptsubscriptsubscript𝑡0𝑡subscript𝜎21𝐗𝑢differential-dsubscript𝑊1𝑢superscriptsubscriptsubscript𝑡0𝑡subscript𝜎22𝐗𝑢differential-dsubscript𝑊2𝑢\displaystyle\approx{}X\_{2}(t\_{0})+\int\_{t\_{0}}^{t}\mu\_{2}\big{(}\mathbf{X}(u)\big{)}du+\int\_{t\_{0}}^{t}\sigma\_{21}\big{(}\mathbf{X}(u)\big{)}dW\_{1}(u)+\int\_{t\_{0}}^{t}\sigma\_{22}\big{(}\mathbf{X}(u)\big{)}dW\_{2}(u) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​∑j,k,l=12∂σ2​j∂xl​σl​k​(𝐗​(t0))​(Δ​Wj​(t)​Δ​Wk​(t)+ρj​k​(t−t0)−𝒜j​k​(t0,t)),12superscriptsubscript  𝑗𝑘𝑙 12subscript𝜎2𝑗subscript𝑥𝑙subscript𝜎𝑙𝑘𝐗subscript𝑡0Δsubscript𝑊𝑗𝑡Δsubscript𝑊𝑘𝑡subscript𝜌𝑗𝑘𝑡subscript𝑡0subscript𝒜𝑗𝑘subscript𝑡0𝑡\displaystyle+\frac{1}{2}\sum\_{j,k,l=1}^{2}\frac{\partial\sigma\_{2j}}{\partial{}x\_{l}}\sigma\_{lk}\big{(}\mathbf{X}(t\_{0})\big{)}\big{(}\Delta{W}\_{j}(t)\Delta{W}\_{k}(t)+\rho\_{jk}(t-t\_{0})-\mathcal{A}\_{jk}(t\_{0},t)\big{)}, |  |

According to Giles (2018) [[10](#bib.bib10)], the term Ai​j​(t0,t)subscript𝐴𝑖𝑗subscript𝑡0𝑡A\_{ij}(t\_{0},t) is the Lévy Area between two the two driving Brownian motions. It’s behavior is captured by following stochastic integral:

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | 𝒜i​j​(t0,t)=∫t0t(Δ​Wi​(u)​d​Wj​(u)−Δ​Wj​(u)​d​Wi​(u)).subscript𝒜𝑖𝑗subscript𝑡0𝑡subscriptsuperscript𝑡subscript𝑡0Δsubscript𝑊𝑖𝑢𝑑subscript𝑊𝑗𝑢Δsubscript𝑊𝑗𝑢𝑑subscript𝑊𝑖𝑢\displaystyle\mathcal{A}\_{ij}(t\_{0},t)=\int^{t}\_{t\_{0}}\big{(}\Delta{W}\_{i}(u)dW\_{j}(u)-\Delta{W}\_{j}(u)dW\_{i}(u)\big{)}. |  |

Since we are only interested in pricing and hedging, it is advantageous to work under the risk-neutral measure. FLMM in ([2](#S2.E2 "Equation 2 ‣ 2 Model Framework ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")) with the updated drift and diffusion functions of ([3](#S3.Ex7 "3 Analysis of Replication of Exchange Option by Delta Hedging as Price Impact ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")) has the following dynamics under ℙ~~ℙ\widetilde{\mathbbm{P}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S1​(t)𝑑subscript𝑆1𝑡\displaystyle dS\_{1}(t) | =r​S1​(t)​d​t+σ~11​(𝐒​(t))​d​W~1​(t)+σ~12​(𝐒​(t))​d​W~2​(t),absent𝑟subscript𝑆1𝑡𝑑𝑡subscript~𝜎11𝐒𝑡𝑑subscript~𝑊1𝑡subscript~𝜎12𝐒𝑡𝑑subscript~𝑊2𝑡\displaystyle=rS\_{1}(t)dt+\widetilde{\sigma}\_{11}\big{(}\mathbf{S}(t)\big{)}d\widetilde{W}\_{1}(t)+\widetilde{\sigma}\_{12}\big{(}\mathbf{S}(t)\big{)}d\widetilde{W}\_{2}(t), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (6) |  | d​S2​(t)𝑑subscript𝑆2𝑡\displaystyle dS\_{2}(t) | =r​S2​(t)​d​t+σ~21​(t)​d​W~1​(t)+σ~22​(t)​d​W~2​(t),absent𝑟subscript𝑆2𝑡𝑑𝑡subscript~𝜎21𝑡𝑑subscript~𝑊1𝑡subscript~𝜎22𝑡𝑑subscript~𝑊2𝑡\displaystyle=rS\_{2}(t)dt+\widetilde{\sigma}\_{21}(t)d\widetilde{W}\_{1}(t)+\widetilde{\sigma}\_{22}(t)d\widetilde{W}\_{2}(t), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​D​(t)D​(t)𝑑𝐷𝑡𝐷𝑡\displaystyle\frac{dD(t)}{D(t)} | =−r​d​t,absent𝑟𝑑𝑡\displaystyle=-rdt, |  |

for simplicity, we set:

|  |  |  |
| --- | --- | --- |
|  | σ~21​(t)=σ2​s2​ρ,σ~22​(t)=σ2​s2​1−ρ2.formulae-sequencesubscript~𝜎21𝑡subscript𝜎2subscript𝑠2𝜌subscript~𝜎22𝑡subscript𝜎2subscript𝑠21superscript𝜌2\displaystyle\widetilde{\sigma}\_{21}(t)=\sigma\_{2}s\_{2}\rho{},\qquad\widetilde{\sigma}\_{22}(t)=\sigma\_{2}s\_{2}\sqrt{1-\rho^{2}}. |  |

The Milstein approximation for ([4.1](#S4.Ex14 "4.1 Milstein Scheme for Asset Price ‣ 4 Numerical Simulations ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")) can be set up by following these procedures:

1. 1.

   Partition [t,T]𝑡𝑇[t,T] into M𝑀M equivalent intervals of length Δ​t=T−tMΔ𝑡𝑇𝑡𝑀\Delta{t}=\frac{T-t}{M}.
2. 2.

   Set the initial values as S1​(0)=s1subscript𝑆10subscript𝑠1S\_{1}(0)=s\_{1} and S2​(0)=s2subscript𝑆20subscript𝑠2S\_{2}(0)=s\_{2}.
3. 3.

   Sample {Δ​W1​(j),Δ​W2​(j)}j=1,2,…​MsubscriptΔsubscript𝑊1𝑗Δsubscript𝑊2𝑗𝑗
   12…𝑀\{\Delta{}W\_{1}(j),\Delta{}W\_{2}(j)\}\_{j=1,2,...M}, where each
     
   {Δ​W1​(j),Δ​W2​(j)}∼𝒩2​(𝟎,Δ​t​I2)similar-toΔsubscript𝑊1𝑗Δsubscript𝑊2𝑗subscript𝒩20Δ𝑡subscript𝐼2\{\Delta{}W\_{1}(j),\Delta{}W\_{2}(j)\}\sim\mathcal{N}\_{2}(\mathbf{0},\Delta{t}I\_{2}).
4. 4.

   Generate Lévy Areas 𝒜i​j​(0,Δ​t)subscript𝒜𝑖𝑗0Δ𝑡\mathcal{A}\_{ij}(0,\Delta{t}).
5. 5.

   Recursively define:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | S1​(m+1)subscript𝑆1𝑚1\displaystyle S\_{1}(m+1) | =S1​(m)+r​S1​(m)​Δ​t+∑i=12σ~1​i​(𝐒​(m))​Δ​Wi​(m+1)+12​∑i,j,k=12∂σ~1​i∂skabsentsubscript𝑆1𝑚𝑟subscript𝑆1𝑚Δ𝑡superscriptsubscript𝑖12subscript~𝜎1𝑖𝐒𝑚Δsubscript𝑊𝑖𝑚112superscriptsubscript 𝑖𝑗𝑘12subscript~𝜎1𝑖subscript𝑠𝑘\displaystyle=S\_{1}(m)+rS\_{1}(m)\Delta{t}+\sum\_{i=1}^{2}\widetilde{\sigma}\_{1i}\big{(}\mathbf{S}(m)\big{)}\Delta{}W\_{i}(m+1)+\frac{1}{2}\sum\_{i,j,k=1}^{2}\frac{\partial{\widetilde{\sigma}}\_{1i}}{\partial{s}\_{k}} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ×σ~k​j​(𝐒​(m))​(Δ​Wi​(m+1)​Δ​Wj​(m+1)−𝟙(i=j)​Δ​t−𝒜i​j),absentsubscript~𝜎𝑘𝑗𝐒𝑚Δsubscript𝑊𝑖𝑚1Δsubscript𝑊𝑗𝑚1subscript1𝑖𝑗Δ𝑡subscript𝒜𝑖𝑗\displaystyle\times\widetilde{\sigma}\_{kj}\big{(}\mathbf{S}(m)\big{)}\big{(}\Delta{}W\_{i}(m+1)\Delta{}W\_{j}(m+1)-\mathbbm{1}\_{(i=j)}\Delta{t}-\mathcal{A}\_{ij}\big{)}, |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | S2​(m+1)subscript𝑆2𝑚1\displaystyle S\_{2}(m+1) | =S2​(m)+r​S2​(m)​Δ​t+∑i=12σ~2​i​(𝐒​(m))​Δ​Wi​(m+1)+12​∑i,j,k=12∂σ~2​i∂skabsentsubscript𝑆2𝑚𝑟subscript𝑆2𝑚Δ𝑡superscriptsubscript𝑖12subscript~𝜎2𝑖𝐒𝑚Δsubscript𝑊𝑖𝑚112superscriptsubscript 𝑖𝑗𝑘12subscript~𝜎2𝑖subscript𝑠𝑘\displaystyle=S\_{2}(m)+rS\_{2}(m)\Delta{t}+\sum\_{i=1}^{2}\widetilde{\sigma}\_{2i}\big{(}\mathbf{S}(m)\big{)}\Delta{}W\_{i}(m+1)+\frac{1}{2}\sum\_{i,j,k=1}^{2}\frac{\partial{\widetilde{\sigma}}\_{2i}}{\partial{s}\_{k}} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ×σ~k​j​(𝐒​(m))​(Δ​Wi​(m+1)​Δ​Wj​(m+1)−𝟙(i=j)​Δ​t−𝒜i​j).absentsubscript~𝜎𝑘𝑗𝐒𝑚Δsubscript𝑊𝑖𝑚1Δsubscript𝑊𝑗𝑚1subscript1𝑖𝑗Δ𝑡subscript𝒜𝑖𝑗\displaystyle\times\widetilde{\sigma}\_{kj}\big{(}\mathbf{S}(m)\big{)}\big{(}\Delta{}W\_{i}(m+1)\Delta{}W\_{j}(m+1)-\mathbbm{1}\_{(i=j)}\Delta{t}-\mathcal{A}\_{ij}\big{)}. |  |

There are many techniques to approximate the Lévy Area, one of the simplest is to generate the stochastic integral ([5](#S4.E5 "Equation 5 ‣ 4.1 Milstein Scheme for Asset Price ‣ 4 Numerical Simulations ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")) piece by piece. In this paper, we adopted an algorithm which closely resembles the method found in Scheicher (2007) [[24](#bib.bib24)]. According to Scheicher, this algorithm for Lévy Area has complexity cost of 𝒪​(K)𝒪𝐾\mathcal{O}(K), where K𝐾K is the number of partition of the time interval Δ​tΔ𝑡\Delta{t}.

Algorithm 1  Lévy Area

Define sub-partition length Δ2​t:=Δ​tKassignsuperscriptΔ2𝑡Δ𝑡𝐾\Delta^{2}{t}:=\frac{\Delta{t}}{K}

Generate 𝐳1,𝐳2∼𝒩K​(𝟎,IK)similar-to

subscript𝐳1subscript𝐳2
subscript𝒩𝐾0subscript𝐼𝐾\mathbf{z}\_{1},\mathbf{z}\_{2}\sim{}\mathcal{N}\_{K}(\mathbf{0},I\_{K}).

Generate lower triangular matrix of 111s T𝑇T, set R:=Δ2​t​Tassign𝑅superscriptΔ2𝑡𝑇R:=\Delta^{2}{t}T

Generate lower and upper diagonal matrices of 111s L𝐿L and U𝑈U.

Set 𝐁1:=R​𝐳1assignsubscript𝐁1𝑅subscript𝐳1\mathbf{B}\_{1}:=R\mathbf{z}\_{1} and 𝐁2=:R𝐳2\mathbf{B}\_{2}=:R\mathbf{z}\_{2}

A=𝐛𝟏T​(U−L)​𝐛𝟐𝐴superscriptsubscript𝐛1𝑇𝑈𝐿subscript𝐛2A=\mathbf{b\_{1}}^{T}(U-L)\mathbf{b\_{2}}

return  A𝐴A

We may redefine a matrix recursion version of the Milstein Scheme. Consider the following evolutionary dynamic of 𝐒​(t)𝐒𝑡\mathbf{S}(t):

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | 𝐒​(m+1)=𝐁​(m)​𝐒​(m)+12​𝐛​(m).𝐒𝑚1𝐁𝑚𝐒𝑚12𝐛𝑚\displaystyle\mathbf{S}(m+1)=\mathbf{B}(m)\mathbf{S}(m)+\frac{1}{2}\mathbf{b}(m). |  |

The matrix 𝐁​(m)𝐁𝑚\mathbf{B}(m) consists of the first order approximation and the vector 𝐛​(m)𝐛𝑚\mathbf{b}(m) is the second order approximation. For our SDE system ([3](#S3.Ex7 "3 Analysis of Replication of Exchange Option by Delta Hedging as Price Impact ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")), 𝐁​(m)𝐁𝑚\mathbf{B}(m) and 𝐛​(m)𝐛𝑚\mathbf{b}(m) can be defined as follows:

|  |  |  |
| --- | --- | --- |
|  | 𝐁​(m)=[1+r​Δ​t+σ~11​(𝐒​(m))​Δ​W1​(m+1)σ~12​(𝐒​(m))​Δ​W2​(m+1)σ~21​(𝐒​(m))​Δ​W1​(m+1)1+r​Δ​t+σ~21​(𝐒​(m))​Δ​W2​(m+1)],𝐁𝑚matrix1𝑟Δ𝑡subscript~𝜎11𝐒𝑚Δsubscript𝑊1𝑚1subscript~𝜎12𝐒𝑚Δsubscript𝑊2𝑚1subscript~𝜎21𝐒𝑚Δsubscript𝑊1𝑚11𝑟Δ𝑡subscript~𝜎21𝐒𝑚Δsubscript𝑊2𝑚1\displaystyle\mathbf{B}(m)=\begin{bmatrix}1+r\Delta{t}+\widetilde{\sigma}\_{11}\big{(}\mathbf{S}(m)\big{)}\Delta{W}\_{1}(m+1)&\widetilde{\sigma}\_{12}\big{(}\mathbf{S}(m)\big{)}\Delta{W}\_{2}(m+1)\\ \widetilde{\sigma}\_{21}\big{(}\mathbf{S}(m)\big{)}\Delta{W}\_{1}(m+1)&1+r\Delta{t}+\widetilde{\sigma}\_{21}\big{(}\mathbf{S}(m)\big{)}\Delta{W}\_{2}(m+1)\end{bmatrix}, |  |
|  |  |  |
| --- | --- | --- |
|  | 𝐛​(m)=[𝐖T​(m+1)​J1​Σ​𝐖​(m+1)−t​r​(J1​Σ)−𝟏T​(J1​Σ∘𝒜)​𝟏𝐖T​(m+1)​J2​Σ​𝐖​(m+1)−t​r​(J2​Σ)−𝟏T​(J2​Σ∘𝒜)​𝟏].𝐛𝑚matrixsuperscript𝐖𝑇𝑚1subscript𝐽1Σ𝐖𝑚1𝑡𝑟subscript𝐽1Σsuperscript1𝑇subscript𝐽1Σ𝒜1superscript𝐖𝑇𝑚1subscript𝐽2Σ𝐖𝑚1𝑡𝑟subscript𝐽2Σsuperscript1𝑇subscript𝐽2Σ𝒜1\displaystyle\mathbf{b}(m)=\begin{bmatrix}\mathbf{W}^{T}(m+1)J\_{1}\Sigma\mathbf{W}(m+1)-tr(J\_{1}\Sigma)-\mathbf{1}^{T}(J\_{1}\Sigma\circ\mathcal{A})\mathbf{1}\\ \mathbf{W}^{T}(m+1)J\_{2}\Sigma\mathbf{W}(m+1)-tr(J\_{2}\Sigma)-\mathbf{1}^{T}(J\_{2}\Sigma\circ\mathcal{A})\mathbf{1}\end{bmatrix}. |  |

Here Jisubscript𝐽𝑖J\_{i} is the Jacobi matrix of the i𝑖i-th asset’s diffusion functions at the m𝑚m-th step. Matrix ΣΣ\Sigma encapsulates diffusion functions of all assets, also at m𝑚m-th step. They are of the form:

|  |  |  |
| --- | --- | --- |
|  | Ji=[∂σ~i​1∂s1∂σ~i​1∂s2∂σ~i​2∂s1∂σ~i​2∂s2],Σ=[σ~11σ~12σ~21σ~22].formulae-sequencesubscript𝐽𝑖matrixsubscript~𝜎𝑖1subscript𝑠1subscript~𝜎𝑖1subscript𝑠2subscript~𝜎𝑖2subscript𝑠1subscript~𝜎𝑖2subscript𝑠2Σmatrixsubscript~𝜎11subscript~𝜎12subscript~𝜎21subscript~𝜎22\displaystyle J\_{i}=\begin{bmatrix}\frac{\partial{\widetilde{\sigma}}\_{i1}}{\partial{s}\_{1}}&\frac{\partial{\widetilde{\sigma}}\_{i1}}{\partial{s}\_{2}}\\ \frac{\partial{\widetilde{\sigma}}\_{i2}}{\partial{s}\_{1}}&\frac{\partial{\widetilde{\sigma}}\_{i2}}{\partial{s}\_{2}}\end{bmatrix},\quad\Sigma=\begin{bmatrix}\widetilde{\sigma}\_{11}&\widetilde{\sigma}\_{12}\\ \widetilde{\sigma}\_{21}&\widetilde{\sigma}\_{22}\end{bmatrix}. |  |

𝒜𝒜\mathbf{\mathcal{A}} is the matrix of Lévy Areas at step m𝑚m, it has the form:

|  |  |  |
| --- | --- | --- |
|  | 𝒜=[0𝒜12𝒜210],𝒜matrix0subscript𝒜12subscript𝒜210\displaystyle\mathbf{\mathcal{A}}=\begin{bmatrix}0&\mathcal{A}\_{12}\\ \mathcal{A}\_{21}&0\end{bmatrix}, |  |

notice 𝒜𝒜\mathcal{A} is an off diagonal matrix, this is because the stochastic integral ([5](#S4.E5 "Equation 5 ‣ 4.1 Milstein Scheme for Asset Price ‣ 4 Numerical Simulations ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")) is 00 when i=j𝑖𝑗i=j.

It is mentioned in Higham (2015) [[14](#bib.bib14)] that Milstein scheme has complexity of 𝒪​(M2)𝒪superscript𝑀2\mathcal{O}(M^{2}) compared to 𝒪​(M)𝒪𝑀\mathcal{O}(M) of Euler-Maruyama. This is important because Milstein scheme will carry a steeper computation time increase as M𝑀M increases.

### 4.2 Control Variate Estimator of the Option Price

The model without liquidity impact is a special case of FLMM. One would naturally assume there exists a high inherited correlation of option prices produced by the two models. It would make sense to use the Magrabe option’s value as the control variate of impacted option’s value. The Magrabe option can be priced by Magrabe’s formula, which uses a pair of correlated GBMs. In fact, we can simultaneously generate the GBM paths while generating FLMM SDEs. We shall do this through Milstein scheme, in the algorithm below; 𝐒𝐒\mathbf{S} and 𝐒c​vsubscript𝐒𝑐𝑣\mathbf{S}\_{cv} represents FLMM and GBM asset prices respectively.

Algorithm 2  Milstein Control Variate Path

Initialize Values 𝐒​(t)=𝐒c​v​(t)=𝐬𝐒𝑡subscript𝐒𝑐𝑣𝑡𝐬\mathbf{S}(t)=\mathbf{S}\_{cv}(t)=\mathbf{s}

Define Δt=:T−tM\Delta{t}=:\frac{T-t}{M}

for m=0𝑚0m=0 to M−1𝑀1M-1 do

𝚫​𝐖​(m)=(Δ​w1​(m),Δ​w2​(m))∼𝒩2​(0,Δ​t​I2)𝚫𝐖𝑚Δsubscript𝑤1𝑚Δsubscript𝑤2𝑚similar-tosubscript𝒩20Δ𝑡subscript𝐼2\mathbf{\Delta{}W}(m)=\big{(}\Delta{}w\_{1}(m),\Delta{}w\_{2}(m)\big{)}\sim\mathcal{N}\_{2}(0,\Delta{t}I\_{2})

Set 𝐁​(m)𝐁𝑚\mathbf{B}(m), 𝐛​(m)𝐛𝑚\mathbf{b}(m), Jisubscript𝐽𝑖J\_{i}, ΣΣ\Sigma and 𝒜𝒜\mathbf{\mathcal{A}}

𝐒​(m+1)=𝐁​(m)​𝐒​(m)+12​𝐛​(m)𝐒𝑚1𝐁𝑚𝐒𝑚12𝐛𝑚\mathbf{S}(m+1)=\mathbf{B}(m)\mathbf{S}(m)+\frac{1}{2}\mathbf{b}(m)

𝐒c​v​(m+1)=𝐁c​v​(m)​𝐒c​v​(m)+12​𝐛c​v​(m)subscript𝐒𝑐𝑣𝑚1subscript𝐁𝑐𝑣𝑚subscript𝐒𝑐𝑣𝑚12subscript𝐛𝑐𝑣𝑚\mathbf{S}\_{cv}(m+1)=\mathbf{B}\_{cv}(m)\mathbf{S}\_{cv}(m)+\frac{1}{2}\mathbf{b}\_{cv}(m)

end for

return  𝐒​(M)𝐒𝑀\mathbf{S}(M), 𝐒c​v​(M)subscript𝐒𝑐𝑣𝑀\mathbf{S}\_{cv}(M)

By generating {𝐒(i)(M)\{\mathbf{S}^{(i)}(M), 𝐒c​v(i)(M)}i=1,2,…​N\mathbf{S}^{(i)}\_{cv}(M)\}\_{i=1,2,...N}, we can define the control variate MC estimator of FLMM Exchange Option as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (8) |  | V¯¯𝑉\displaystyle\overline{V} | =e−r​(T−t)N​∑i=1N((S1(i)​(M)−S2(i)​(M))++c​(Sc​v,1(i)​(M)−Sc​v,2(i)​(M))+)absentsuperscript𝑒𝑟𝑇𝑡𝑁superscriptsubscript𝑖1𝑁superscriptsuperscriptsubscript𝑆1𝑖𝑀superscriptsubscript𝑆2𝑖𝑀𝑐superscriptsuperscriptsubscript𝑆  𝑐𝑣1𝑖𝑀superscriptsubscript𝑆  𝑐𝑣2𝑖𝑀\displaystyle=\frac{e^{-r(T-t)}}{N}\sum\_{i=1}^{N}\Big{(}\big{(}S\_{1}^{(i)}(M)-S\_{2}^{(i)}(M)\big{)}^{+}+c\big{(}S\_{cv,1}^{(i)}(M)-S\_{cv,2}^{(i)}(M)\big{)}^{+}\Big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −c​VM​a​r​g​r​a​b​e,𝑐subscript𝑉𝑀𝑎𝑟𝑔𝑟𝑎𝑏𝑒\displaystyle-cV\_{Margrabe}, |  |

here VM​a​r​g​r​a​b​esubscript𝑉𝑀𝑎𝑟𝑔𝑟𝑎𝑏𝑒V\_{Margrabe} is the price of Magrabe option given by Margrabe’s formula in a model without liquidity impact. The term c𝑐c is the optimization constant. In this case, the variance of our MC estimator is minimized when c^=−C​o​v​(VF​L​M​M,VM​a​r​g​r​a​b​e)V​a​r​(VM​a​r​g​r​a​b​e)^𝑐𝐶𝑜𝑣subscript𝑉𝐹𝐿𝑀𝑀subscript𝑉𝑀𝑎𝑟𝑔𝑟𝑎𝑏𝑒𝑉𝑎𝑟subscript𝑉𝑀𝑎𝑟𝑔𝑟𝑎𝑏𝑒\hat{c}=-\frac{Cov(V\_{FLMM},V\_{Margrabe})}{Var(V\_{Margrabe})}.

### 4.3 Option Hedges

Managing the Greeks is an essential part of trading. To determine the Deltas of FLMM Exchange Option, we will adopt the adjoint method of Giles and Glasserman (2006) [[9](#bib.bib9)]. This method first requires the Greeks to be generated pathwise, then a MC can be applied to estimate the actual value. The adjoint method is advantageous because these pathwise Greeks can be generated simultaneously with the assets. Suppose interchangeability exists between the differential operator and expectation, then the j𝑗j-th Delta of FLMM Exchange Option is:

|  |  |  |
| --- | --- | --- |
|  | Δj​(t)=∂∂Sj​(t)​𝔼~t,s1,s2​[e−r​(T−t)​V​(𝐒​(T))]=e−r​(T−t)​𝔼~t,s1,s2​[∂∂Sj​(t)​V​(𝐒​(T))].subscriptΔ𝑗𝑡subscript𝑆𝑗𝑡superscript~𝔼  𝑡subscript𝑠1subscript𝑠2delimited-[]superscript𝑒𝑟𝑇𝑡𝑉𝐒𝑇superscript𝑒𝑟𝑇𝑡superscript~𝔼  𝑡subscript𝑠1subscript𝑠2delimited-[]subscript𝑆𝑗𝑡𝑉𝐒𝑇\displaystyle\Delta\_{j}(t)=\frac{\partial}{\partial S\_{j}(t)}\widetilde{\mathbb{E}}^{t,s\_{1},s\_{2}}\Big{[}e^{-r(T-t)}V\big{(}\mathbf{S}(T)\big{)}\Big{]}=e^{-r(T-t)}\widetilde{\mathbb{E}}^{t,s\_{1},s\_{2}}\Big{[}\frac{\partial}{\partial S\_{j}(t)}V\big{(}\mathbf{S}(T)\big{)}\Big{]}. |  |

By relaxing certain regularity conditions outlined in Glasserman (2004) [[11](#bib.bib11)], we may rewrite it as:

|  |  |  |
| --- | --- | --- |
|  | ∂∂Sj​(t)​V​(𝐒​(T))=∑i=12∂V∂Si​(T)​∂Si​(T)∂Sj​(t).subscript𝑆𝑗𝑡𝑉𝐒𝑇subscriptsuperscript2𝑖1𝑉subscript𝑆𝑖𝑇subscript𝑆𝑖𝑇subscript𝑆𝑗𝑡\displaystyle\frac{\partial}{\partial S\_{j}(t)}V\big{(}\mathbf{S}(T)\big{)}=\sum^{2}\_{i=1}\frac{\partial V}{\partial S\_{i}(T)}\frac{\partial S\_{i}(T)}{\partial S\_{j}(t)}. |  |

During implementation, ∂V∂Si​(T)𝑉subscript𝑆𝑖𝑇\frac{\partial V}{\partial S\_{i}(T)} can be approximated through algorithmic differentiation. While the ∂Si​(T)∂Sj​(t)subscript𝑆𝑖𝑇subscript𝑆𝑗𝑡\frac{\partial S\_{i}(T)}{\partial S\_{j}(t)} term is obtained from taking the path-wise derivative of Milstein scheme ([5](#S4.Ex17 "Item 5 ‣ 4.1 Milstein Scheme for Asset Price ‣ 4 Numerical Simulations ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")). Set Δi​j​(t)=∂Si​(T)∂Sj​(t)subscriptΔ𝑖𝑗𝑡subscript𝑆𝑖𝑇subscript𝑆𝑗𝑡\Delta\_{ij}(t)=\frac{\partial S\_{i}(T)}{\partial S\_{j}(t)}, we obtain an approximating scheme for Δi​j​(m)subscriptΔ𝑖𝑗𝑚\Delta\_{ij}(m) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δi​j​(m+1)subscriptΔ𝑖𝑗𝑚1\displaystyle\Delta\_{ij}(m+1) | =Δi​j​(m)+r​Δi​j​(m)​Δ​t+∑k,l=12∂σ~i​k∂sl​Δl​j​(m)​Δ​Wk​(m+1)absentsubscriptΔ𝑖𝑗𝑚𝑟subscriptΔ𝑖𝑗𝑚Δ𝑡superscriptsubscript  𝑘𝑙 12subscript~𝜎𝑖𝑘subscript𝑠𝑙subscriptΔ𝑙𝑗𝑚Δsubscript𝑊𝑘𝑚1\displaystyle=\Delta\_{ij}(m)+r\Delta\_{ij}(m)\Delta{t}+\sum\_{k,l=1}^{2}\frac{\partial\widetilde{\sigma}\_{ik}}{\partial s\_{l}}\Delta\_{lj}(m)\Delta{W}\_{k}(m+1) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​∑k,l,p,q=12Δq​j​(m)​(∂2σ~i​k∂sp​∂sq​σ~p​j​(𝐒​(m))+∂σ~i​k∂sp​∂σ~p​l∂sq),12superscriptsubscript  𝑘𝑙𝑝𝑞 12subscriptΔ𝑞𝑗𝑚superscript2subscript~𝜎𝑖𝑘subscript𝑠𝑝subscript𝑠𝑞subscript~𝜎𝑝𝑗𝐒𝑚subscript~𝜎𝑖𝑘subscript𝑠𝑝subscript~𝜎𝑝𝑙subscript𝑠𝑞\displaystyle+\frac{1}{2}\sum\_{k,l,p,q=1}^{2}\Delta\_{qj}(m)\Big{(}\frac{\partial^{2}\widetilde{\sigma}\_{ik}}{\partial s\_{p}\partial s\_{q}}\widetilde{\sigma}\_{pj}\big{(}\mathbf{S}(m)\big{)}+\frac{\partial\widetilde{\sigma}\_{ik}}{\partial s\_{p}}\frac{\partial\widetilde{\sigma}\_{pl}}{\partial s\_{q}}\Big{)}, |  |

where m=0,1,…​M−1𝑚

01…𝑀1m=0,1,...M-1. If we define a matrix 𝐃​(m)𝐃𝑚\mathbf{D}(m) as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Di​j​(m)subscript𝐷𝑖𝑗𝑚\displaystyle D\_{ij}(m) | =δi​j​(m)+r​Δ​t+∑k=12∂σ~i​k∂sj​Δ​Wk​(m+1)absentsubscript𝛿𝑖𝑗𝑚𝑟Δ𝑡superscriptsubscript𝑘12subscript~𝜎𝑖𝑘subscript𝑠𝑗Δsubscript𝑊𝑘𝑚1\displaystyle=\delta\_{ij}(m)+r\Delta{t}+\sum\_{k=1}^{2}\frac{\partial\widetilde{\sigma}\_{ik}}{\partial s\_{j}}\Delta{W}\_{k}(m+1) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​∑k,l,p=12(∂2σ~i​k∂sp​∂sj​σ~p​j​(𝐒​(m))+∂σ~i​k∂sp​∂σ~p​l∂sj),12superscriptsubscript  𝑘𝑙𝑝 12superscript2subscript~𝜎𝑖𝑘subscript𝑠𝑝subscript𝑠𝑗subscript~𝜎𝑝𝑗𝐒𝑚subscript~𝜎𝑖𝑘subscript𝑠𝑝subscript~𝜎𝑝𝑙subscript𝑠𝑗\displaystyle+\frac{1}{2}\sum\_{k,l,p=1}^{2}\Big{(}\frac{\partial^{2}\widetilde{\sigma}\_{ik}}{\partial s\_{p}\partial s\_{j}}\widetilde{\sigma}\_{pj}\big{(}\mathbf{S}(m)\big{)}+\frac{\partial\widetilde{\sigma}\_{ik}}{\partial s\_{p}}\frac{\partial\widetilde{\sigma}\_{pl}}{\partial s\_{j}}\Big{)}, |  |

then the evolution of 𝚫𝚫\mathbf{\Delta} can be redefined using matrix recursion as follows:

|  |  |  |
| --- | --- | --- |
|  | 𝚫​(m+1)=D​(m)​𝚫​(m),𝚫𝑚1𝐷𝑚𝚫𝑚\displaystyle\mathbf{\Delta}(m+1)=D(m)\mathbf{\Delta}(m), |  |

where 𝚫​(t)=I𝚫𝑡𝐼\mathbf{\Delta}(t)=I. Similar to estimating the option price, we a can use the Delta from the Magrabe option as a multivariate control variate. We adopt the method presented by Rubinstein and Marcus (1985) [[23](#bib.bib23)] and set up the estimator for Delta:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (9) |  | 𝚫¯¯𝚫\displaystyle\overline{\mathbf{\Delta}} | =e−r​(T−t)N​∑i=1N(𝚫(i)​(M)+C1​𝚫c​v(i)​(M))−C1​𝚫M​a​r​g​r​a​b​e.absentsuperscript𝑒𝑟𝑇𝑡𝑁superscriptsubscript𝑖1𝑁superscript𝚫𝑖𝑀subscript𝐶1superscriptsubscript𝚫𝑐𝑣𝑖𝑀subscript𝐶1subscript𝚫𝑀𝑎𝑟𝑔𝑟𝑎𝑏𝑒\displaystyle=\frac{e^{-r(T-t)}}{N}\sum\_{i=1}^{N}\Big{(}\mathbf{\Delta}^{(i)}(M)+C\_{1}\mathbf{\Delta}\_{cv}^{(i)}(M)\Big{)}-C\_{1}\mathbf{\Delta}\_{Margrabe}. |  |

The variance of 𝚫¯¯𝚫\overline{\mathbf{\Delta}} is minimized when C^1=Σ𝚫​𝚫c​v​Σ𝚫c​v​𝚫c​v−1subscript^𝐶1subscriptΣ𝚫subscript𝚫𝑐𝑣superscriptsubscriptΣsubscript𝚫𝑐𝑣subscript𝚫𝑐𝑣1\hat{C}\_{1}=\Sigma\_{\mathbf{\Delta}\mathbf{\Delta}\_{cv}}\Sigma\_{\mathbf{\Delta}\_{cv}\mathbf{\Delta}\_{cv}}^{-1}.

### 4.4 Experimental results

We implement our MC engine with alternating space and path parameter for the purpose of determining the effect on a 99%percent9999\% Gaussian confidence interval (CI). For consistency, we fix a set of option parameters: s1=60subscript𝑠160s\_{1}=60, s2=80subscript𝑠280s\_{2}=80, T=0.5𝑇0.5T=0.5, t=0𝑡0t=0, σ1=0.4subscript𝜎10.4\sigma\_{1}=0.4, σ2=0.2subscript𝜎20.2\sigma\_{2}=0.2, ρ=0.5𝜌0.5\rho=0.5 and r=0.05𝑟0.05r=0.05. We also fix the price impact function parameters to: ϵ=0.04italic-ϵ0.04\epsilon=0.04 and β=100𝛽100\beta=100. The numerical results are presented below:

Table 1: Space (N) Dimension MC Results

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| N | M | V¯¯𝑉\overline{V} | 99%percent9999\% CI of V¯¯𝑉\overline{V} | CI Length | CPU Time |
| 100100100 | 100100100 | 1.00081.00081.0008 | [0.998642,1.00295]0.9986421.00295[0.998642,1.00295] | 0.00431240.00431240.0043124 | 0.11s |
| 100010001000 | 100100100 | 1.001451.001451.00145 | [1.00088,1.00201]1.000881.00201[1.00088,1.00201] | 0.001125140.001125140.00112514 | 1.08s |
| 10​k10𝑘10k | 100100100 | 1.00131.00131.0013 | [1.0011,1.00151]1.00111.00151[1.0011,1.00151] | 0.0004123770.0004123770.000412377 | 9.84s |
| 100​k100𝑘100k | 100100100 | 1.001341.001341.00134 | [1.00128,1.0014]1.001281.0014[1.00128,1.0014] | 0.0001262870.0001262870.000126287 | 99.97s |
| 1​m1𝑚1m | 100100100 | 1.00139 | [1.00137,1.00141]1.001371.00141[1.00137,1.00141] | 0.00004056830.00004056830.0000405683 | 1033.30s |




Table 2: Path (M) Dimension MC Results

| N | M | V¯¯𝑉\overline{V} | 99%percent9999\% CI of V¯¯𝑉\overline{V} | CI Length | CPU Time |
| --- | --- | --- | --- | --- | --- |
| 100010001000 | 100100100 | 1.001451.001451.00145 | [1.00088,1.00201]1.000881.00201[1.00088,1.00201] | 0.001125140.001125140.00112514 | 1.08s |
| 100010001000 | 200200200 | 1.001291.001291.00129 | [1.00072,1.00186]1.000721.00186[1.00072,1.00186] | 0.001132210.001132210.00113221 | 3.82s |
| 100010001000 | 400400400 | 1.001811.001811.00181 | [1.00118,1.00244]1.001181.00244[1.00118,1.00244] | 0.001262760.001262760.00126276 | 15.63s |
| 100010001000 | 800800800 | 1.001111.001111.00111 | [1.00053,1.00169]1.000531.00169[1.00053,1.00169] | 0.001151770.001151770.00115177 | 66.96s |
| 100010001000 | 160016001600 | 1.001511.001511.00151 | [1.00088,1.00215]1.000881.00215[1.00088,1.00215] | 0.001272710.001272710.00127271 | 237.92s |

One observation from our experiment is that as the path dimension doubles, the computation time almost quadruples. This is in agreement with Higham’s assertion on the complexity cost of Milstein Scheme.

![[Uncaptioned image]](/html/2006.07771/assets/figure/NDimComplex.png)

![[Uncaptioned image]](/html/2006.07771/assets/figure/MDimComplex.png)

From a practitioner’s point of view, we must consider the trade off between time complexity and accuracy of estimation. In the first graph above, we observe that as the computation time increases in space dimension, the length of CI exponentially decays. However, as we increase the computation time in path dimension, there is an ambiguous effect on CI length. This is emphasized in the second graph above. It is fairly self-explanatory that we should focus our computation resources on the space dimension to get the best complexity vs accuracy trade off.

We also would like to compare FLMM against the frictionless model. In particular, we want to confirm the liquidity impact of FLMM requires a strictly positive valuation adjustment.

Table 3: Analysis of Liquidity Premium

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| N=100000𝑁100000N=100000, M=100𝑀100M=100 | s1subscript𝑠1s\_{1} | FLMM | Margrabe | Excess Price |
| s2=10subscript𝑠210s\_{2}=10 | 101010 | 0.985910.985910.98591 | 0.9747670.9747670.974767 | 0.0111430.0111430.011143 |
|  | 202020 | 0.002371990.002371990.00237199 | 0.002369620.002369620.00236962 | 0.000002366550.000002366550.00000236655 |
|  | 101010 | 0.002375140.002375140.00237514 | 0.002369620.002369620.00236962 | 0.000005521520.000005521520.00000552152 |
| s2=20subscript𝑠220s\_{2}=20 | 202020 | 1.960651.960651.96065 | 1.949531.949531.94953 | 0.01111810.01111810.0111181 |
|  | 303030 | 0.1226690.1226690.122669 | 0.1215750.1215750.121575 | 0.00109370.00109370.0010937 |
|  | 202020 | 0.1225540.1225540.122554 | 0.1215750.1215750.121575 | 0.0009785860.0009785860.000978586 |
| s2=30subscript𝑠230s\_{2}=30 | 303030 | 2.935982.935982.93598 | 2.92432.92432.9243 | 0.01168190.01168190.0116819 |
|  | 404040 | 10.50410.50410.504 | 10.49910.49910.499 | 0.004968710.004968710.00496871 |
|  |  | ⋮ |  |  |
|  | 909090 | 5.108665.108665.10866 | 5.098795.098795.09879 | 0.009874720.009874720.00987472 |
| s2=100subscript𝑠2100s\_{2}=100 | 100100100 | 9.758469.758469.75846 | 9.747679.747679.74767 | 0.0107830.0107830.010783 |

From our experiments, we indeed observe an excess in the option price due to the FLMM. This premium seems to be the greatest for at-the-money options. Furthermore, as the trade-cost-per-share parameter ϵitalic-ϵ\epsilon increases, we observe a higher liquidity premium. This effect is illustrated in the figures below.

Figure 2: Liquidity Value Adjustment

![Refer to caption](/html/2006.07771/assets/figure/HeatValue.png)

It only appears natural to be also interested in the liquidity adjustment for Delta. Using the Margrabe Delta as a reference, one would expect that the strictly greater price of our illiquid asset 111 would cause Δ1subscriptΔ1\Delta\_{1} to be greater and Δ2subscriptΔ2\Delta\_{2} to be less. Empirically, we observe an excess effect in Δ1subscriptΔ1\Delta\_{1}, but we also observed an excess effect in Δ2subscriptΔ2\Delta\_{2}. We illustrate this surprising result in the figures below.

Figure 3: Liquidity Delta Adjustment

![Refer to caption](/html/2006.07771/assets/figure/HeatD1.png)

![Refer to caption](/html/2006.07771/assets/figure/HeatD2.png)

These positive Delta adjustments effects also reach their respective pinnacles when the option is at-the-money. In a model with transaction costs these
Delta adjustments would add extra value to the option price.

## 5 Deep Learning Method

Artificial neural network have powerful predictive capabilities, one of the first versions are the FFN. This network is structured as a sequence of layers, with various numbers of neurons embedded in each layer. We shall use N𝑁N to denote the number of layers, and nisubscript𝑛𝑖n\_{i} to denote the number of neurons in the i𝑖i-th layer. In a fully connected FFN, each neuron in the current layer has a connection with each neuron in the subsequent layer. The strength of these connections are known as weights, we denote the weights connected to the j𝑗j-th neuron in the i𝑖i-th layer as 𝐰j[i]subscriptsuperscript𝐰delimited-[]𝑖𝑗\mathbf{w}^{[i]}\_{j}. Each neuron also carries a unique bias term bj[i]subscriptsuperscript𝑏delimited-[]𝑖𝑗b^{[i]}\_{j}, this term has a similar effect as the regression intercept. The final component of a neuron is the activation function f​(z)𝑓𝑧f(z), similar to linking functions of non-linear regression, its purpose is to add non-linearity. In this study, we used these types of activation functions:

Table 4: Activation Functions

| Type | Activation Function |
| --- | --- |
| ReLU | f​(z)=max⁡(z,0)𝑓𝑧𝑧0f(z)=\max(z,0) |
| SoftPlus | f​(z)=log⁡(1+ez)𝑓𝑧1superscript𝑒𝑧f(z)=\log(1+e^{z}) |

The operation of a neuron can be expressed as:

|  |  |  |
| --- | --- | --- |
|  | zj[i]=𝐰j[i]​𝐡[i−1]+bj[i],subscriptsuperscript𝑧delimited-[]𝑖𝑗subscriptsuperscript𝐰delimited-[]𝑖𝑗superscript𝐡delimited-[]𝑖1subscriptsuperscript𝑏delimited-[]𝑖𝑗\displaystyle z^{[i]}\_{j}=\mathbf{w}^{[i]}\_{j}\mathbf{h}^{[i-1]}+b^{[i]}\_{j}, |  |
|  |  |  |
| --- | --- | --- |
|  | hj[i−1]=f​(zj[i]).subscriptsuperscriptℎdelimited-[]𝑖1𝑗𝑓subscriptsuperscript𝑧delimited-[]𝑖𝑗\displaystyle h^{[i-1]}\_{j}=f(z^{[i]}\_{j}). |  |

We also provide a computation graph on the j𝑗j-th neuron in the i𝑖i-th layer:

h1[i−1]superscriptsubscriptℎ1delimited-[]𝑖1h\_{1}^{[i-1]}h2[i−1]superscriptsubscriptℎ2delimited-[]𝑖1h\_{2}^{[i-1]}h3[i−1]superscriptsubscriptℎ3delimited-[]𝑖1h\_{3}^{[i-1]}hn[i−1]superscriptsubscriptℎ𝑛delimited-[]𝑖1h\_{n}^{[i-1]}wi​1[i]subscriptsuperscript𝑤delimited-[]𝑖𝑖1w^{[i]}\_{i1}wi​2[i]subscriptsuperscript𝑤delimited-[]𝑖𝑖2w^{[i]}\_{i2}wi​3[i]subscriptsuperscript𝑤delimited-[]𝑖𝑖3w^{[i]}\_{i3}wi​ni[i]subscriptsuperscript𝑤delimited-[]𝑖𝑖subscript𝑛𝑖w^{[i]}\_{in\_{i}}f​(zj[i])𝑓subscriptsuperscript𝑧delimited-[]𝑖𝑗f\big{(}z^{[i]}\_{j}\big{)}hj[i]subscriptsuperscriptℎdelimited-[]𝑖𝑗h^{[i]}\_{j}

This process is repeated for every single neuron, which allows us to transverse through the network and arrive at the output layer h[N]=y^superscriptℎdelimited-[]𝑁^𝑦h^{[N]}=\hat{y} (For the purpose of option pricing, we have a single output h[N]superscriptℎdelimited-[]𝑁h^{[N]}, but in general h[N]superscriptℎdelimited-[]𝑁h^{[N]} is a vector). This entire process is often referred to as forward propagation. The figure below describes the FFN architecture deployed to price Exchange Option under FLMM:

Input LayerHidden Layer 1Hidden Layer 2Hidden Layer 3Hidden Layer 4Output Neurons1subscript𝑠1s\_{1}s2subscript𝑠2s\_{2}σ1subscript𝜎1\sigma\_{1}σ2subscript𝜎2\sigma\_{2}r𝑟rρ𝜌\rhoτ𝜏\tauh1[1]superscriptsubscriptℎ1delimited-[]1h\_{1}^{[1]}h2[1]superscriptsubscriptℎ2delimited-[]1h\_{2}^{[1]}h3[1]superscriptsubscriptℎ3delimited-[]1h\_{3}^{[1]}hn[1]superscriptsubscriptℎ𝑛delimited-[]1h\_{n}^{[1]}h1[2]superscriptsubscriptℎ1delimited-[]2h\_{1}^{[2]}h2[2]superscriptsubscriptℎ2delimited-[]2h\_{2}^{[2]}h3[2]superscriptsubscriptℎ3delimited-[]2h\_{3}^{[2]}hn[2]superscriptsubscriptℎ𝑛delimited-[]2h\_{n}^{[2]}h1[3]superscriptsubscriptℎ1delimited-[]3h\_{1}^{[3]}h2[3]superscriptsubscriptℎ2delimited-[]3h\_{2}^{[3]}h3[3]superscriptsubscriptℎ3delimited-[]3h\_{3}^{[3]}hn[3]superscriptsubscriptℎ𝑛delimited-[]3h\_{n}^{[3]}h1[4]superscriptsubscriptℎ1delimited-[]4h\_{1}^{[4]}h2[4]superscriptsubscriptℎ2delimited-[]4h\_{2}^{[4]}h3[4]superscriptsubscriptℎ3delimited-[]4h\_{3}^{[4]}hn[4]superscriptsubscriptℎ𝑛delimited-[]4h\_{n}^{[4]}V𝑉V

The loss function measures the goodness of fit. We use mean squared error (MSE) as the loss function, which is commonly used in regression analysis. We will use MSE to evaluate the result of the forward propagation. This evaluation is preformed for every B𝐵B input, B𝐵B is known as the batch size. Our loss function is formulated as:

|  |  |  |
| --- | --- | --- |
|  | ℒ​(𝐲^,𝐲)=∑k=1B(y^k−yk)2.ℒ^𝐲𝐲superscriptsubscript𝑘1𝐵superscriptsubscript^𝑦𝑘subscript𝑦𝑘2\displaystyle\mathcal{L}(\mathbf{\hat{y}},\mathbf{y})=\sum\_{k=1}^{B}(\hat{y}\_{k}-y\_{k})^{2}. |  |

Minimization of the loss function follows the steepest descent idea, so one has to compute gradient fields with respect to the weights and biases. This is often accomplished through algorithmic differentiation referenced as back propagation. Then, the weights and biases are updated in the direction of the gradient field, in hope of discovering a “good enough” local minimum. The common choice of methodology for optimization is the batch gradient descent method. This method is demonstrated as:

|  |  |  |
| --- | --- | --- |
|  | 𝐰j[i],(n​e​w)=𝐰j[i],(o​l​d)−α​∂ℒ∂𝐰j[i],(o​l​d),superscriptsubscript𝐰𝑗  delimited-[]𝑖𝑛𝑒𝑤subscriptsuperscript𝐰  delimited-[]𝑖𝑜𝑙𝑑𝑗𝛼ℒsuperscriptsubscript𝐰𝑗  delimited-[]𝑖𝑜𝑙𝑑\displaystyle\mathbf{w}\_{j}^{[i],(new)}=\mathbf{w}^{[i],(old)}\_{j}-\alpha\frac{\partial\mathcal{L}}{\partial\mathbf{w}\_{j}^{[i],(old)}}, |  |
|  |  |  |
| --- | --- | --- |
|  | 𝐛j[i],(n​e​w)=𝐛j[i],(o​l​d)−α​∂ℒ∂𝐛j[i],(o​l​d),superscriptsubscript𝐛𝑗  delimited-[]𝑖𝑛𝑒𝑤superscriptsubscript𝐛𝑗  delimited-[]𝑖𝑜𝑙𝑑𝛼ℒsuperscriptsubscript𝐛𝑗  delimited-[]𝑖𝑜𝑙𝑑\displaystyle\mathbf{b}\_{j}^{[i],(new)}=\mathbf{b}\_{j}^{[i],(old)}-\alpha\frac{\partial\mathcal{L}}{\partial\mathbf{b}\_{j}^{[i],(old)}}, |  |
|  |  |  |
| --- | --- | --- |
|  | forj=1,2,…​ni, and ​i=1,2,…​N.formulae-sequence  for𝑗 1  2…subscript𝑛𝑖 and 𝑖 1  2…𝑁\displaystyle\text{for}\quad{}j=1,2,...n\_{i},\text{ and }i=1,2,...N. |  |

In the above expression, α𝛼\alpha is the learning rate.

One batch of forward propagation combined with one instance of back propagation is considered as one iteration of batch training. An epoch encompasses a series of batch training that exhausts the entire data set. Normally, the training is either repeated for a fixed number of epochs, or stopped early when the loss function ceases to decrease further.

The central theorem in neural networks is the universal approximation theorem. This theorem highlights the approximation power of FFNs. Hornik (1989) [[15](#bib.bib15)] established the fact that deep FFNs are universal approximators, in other words, any function can be accurately approximated by some deep FFN. Since option prices are smooth solutions of PDEs, then it should be feasible to predict these solutions with FFNs.

### 5.1 Deeply Learning Derivative

Option pricing can often be computationally expensive. Ferguson and Green (2018) [[7](#bib.bib7)] demonstrated the power of FFN, and achieved a much faster speed than traditional MC engines when pricing baskets. However, the initial costs comes from generation of option inputs, as well as, estimating the corresponding option values through MC engines. Furthermore, training and calibrating the FFN takes tedious effort as well. Nevertheless, these “costs” are reasonable to large financial institutions, and at least in theory, will integrate well with their operations. This is largely because both the data generation and network training can be done offline, when the markets are closed. In addition, the input space can be restricted to reflect a set of likely market scenarios.

To build a FFN pricer for our FLMM Exchange Option, we will use Algorithm ([8](#S4.E8 "Equation 8 ‣ 4.2 Control Variate Estimator of the Option Price ‣ 4 Numerical Simulations ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")) as the underlying MC engine. Our estimator has 7 parameters
  
(𝐱=(s1,s2,r,ρ,σ1,σ2,τ)𝐱subscript𝑠1subscript𝑠2𝑟𝜌subscript𝜎1subscript𝜎2𝜏\mathbf{x}=(s\_{1},s\_{2},r,\rho,\sigma\_{1},\sigma\_{2},\tau)), a set of these parameters count as 111 sample input. It is important to emphasize the particular distribution used to generate the inputs, these should be unique for each option. Indeed, some factors to be considered when choosing the distributions are:

* •

  The physical meaning of each underlying parameter.
* •

  The payoff function itself should be considered because it is pointless to generate excessive of out-of-money MC paths.

Generating the inputs in judicious ways will not only help the loss to converge faster, but will also help the FFN to approximate a meaningful solution.
In our case, we adopted an even spilt between 222 data generation schemes. The first method allows us to sample unbiasly from the entire input space. The second method will allow us to sample more realistic input parameters, as well as, capture more in-the-money payout paths.

Table 5: Data Generation Schemes

| Parameter | Method 1 | Method 2 |
| --- | --- | --- |
| s1subscript𝑠1s\_{1} | s1∼𝒰​(0,100)similar-tosubscript𝑠1𝒰0100s\_{1}\sim\mathcal{U}(0,100) | s1∼50​exp⁡(X1)similar-tosubscript𝑠150subscript𝑋1s\_{1}\sim 50\exp(X\_{1}), X1∼𝒩​(0.5,0.25)similar-tosubscript𝑋1𝒩0.50.25X\_{1}\sim\mathcal{N}(0.5,0.25) |
| s2subscript𝑠2s\_{2} | s2∼𝒰​(0,100)similar-tosubscript𝑠2𝒰0100s\_{2}\sim\mathcal{U}(0,100) | s2∼50​exp⁡(X1−X2)similar-tosubscript𝑠250subscript𝑋1subscript𝑋2s\_{2}\sim 50\exp(X\_{1}-X\_{2}), X2∼𝒩​(0.5,0.25)similar-tosubscript𝑋2𝒩0.50.25X\_{2}\sim\mathcal{N}(0.5,0.25) |
| σ1subscript𝜎1\sigma\_{1} | σ1∼𝒰​(0,0.5)similar-tosubscript𝜎1𝒰00.5\sigma\_{1}\sim\mathcal{U}(0,0.5) | σ1∼𝒰​(0,0.5)similar-tosubscript𝜎1𝒰00.5\sigma\_{1}\sim\mathcal{U}(0,0.5) |
| σ2subscript𝜎2\sigma\_{2} | σ2∼𝒰​(0,0.5)similar-tosubscript𝜎2𝒰00.5\sigma\_{2}\sim\mathcal{U}(0,0.5) | σ2∼𝒰​(0,0.5)similar-tosubscript𝜎2𝒰00.5\sigma\_{2}\sim\mathcal{U}(0,0.5) |
| r𝑟r | r∼𝒰​(0,0.1)similar-to𝑟𝒰00.1r\sim\mathcal{U}(0,0.1) | r∼𝒰​(0,0.1)similar-to𝑟𝒰00.1r\sim\mathcal{U}(0,0.1) |
| ρ𝜌\rho | ρ∼𝒰​(1,−1)similar-to𝜌𝒰11\rho\sim\mathcal{U}(1,-1) | ρ∼2​(X3−0.5)similar-to𝜌2subscript𝑋30.5\rho\sim{}2(X\_{3}-0.5), X3∼β​(5,2)similar-tosubscript𝑋3𝛽52X\_{3}\sim\mathcal{\beta}(5,2) |
| τ𝜏\tau | τ∼𝒰​(0,2)similar-to𝜏𝒰02\tau\sim\mathcal{U}(0,2) | τ∼𝒰​(0,2)similar-to𝜏𝒰02\tau\sim\mathcal{U}(0,2) |

The implementation of Deeply Learning Derivative method can be synthesized by the following programming architectural graph:

Data GenerationMethod 1Method 2MC EngineMilsteinControl VariateDeep Feed Forward NetworkTrainingCross-ValidationTestingExport to Production

### 5.2 Experimental Results

The FFN contains 4 fully connected deep layers with 300300300 ReLu neurons per layer. The output layer contain a single SoftPlus Neuron to ensure the prediction would be positive definite. We generated 111 million inputs, and uses a relatively inaccurate MC engine (N𝑁N=100,M𝑀M=100) to construct the training set. The logic is it has been shown in practice a well-trained deep FFN has the ability to remove the inaccuracy of weak MC estimators. We trained the FNN with mini-batch size of 102410241024, and updated the gradient with ADAM optimizer (2015) [[17](#bib.bib17)]. We performed validation with samples created from a highly accurate MC engine (N𝑁N=100k,M𝑀M=100), at a 100/11001100/1 ratio. Initially, the FFN was set to train for 100010001000 epochs. After 850850850 epochs of training, the loss function cease to decreases further significantly. To prevent over-fitting, it is justifiable to apply early stopping.

![[Uncaptioned image]](/html/2006.07771/assets/figure/MAEgood.png)

![[Uncaptioned image]](/html/2006.07771/assets/figure/MSEgood.png)

We observe both of the mean absolute error (MAE) and MSE of the validation set oscillate around the training set. Furthermore, the amplitude of the oscillation decreases as we train our network. This implies our network is learning to minimize in terms of ℒ1subscriptℒ1\mathcal{L}\_{1} and ℒ2subscriptℒ2\mathcal{L}\_{2} simultaneously. Another important observation is that the MAE error is more consistent than MSE. This implies the smaller errors matched up more consistently between training and validation set. Overall, we can conclude there is no significant over-fitting.

In the testing phase, we generated 100010001000 highly accurate samples with MC engine specification (N𝑁N=100k, M𝑀M=100). We test our trained network and came to the following testing results:

![[Uncaptioned image]](/html/2006.07771/assets/figure/TrueValue.png)

![[Uncaptioned image]](/html/2006.07771/assets/figure/error.png)

Moving on to analyzing the testing set, we observe a strong linear relationship between the predicted value and true value. This is an indication our net performs extremely well in predicting option prices. In the graph above, we observe relatively few misclassification points (error that are more than 333 standard deviation away from the mean). Furthermore, we observes approximate normality in the residual histogram. The slight leptokurtic shape could hint hyper-parameter tuning might yield better results. However due to the close resemblances to normality, the source of error should be relatively homogeneous.

We will use option parameters s1=60subscript𝑠160s\_{1}=60, s2=80subscript𝑠280s\_{2}=80, σ1=0.4subscript𝜎10.4\sigma\_{1}=0.4, σ2=0.2subscript𝜎20.2\sigma\_{2}=0.2, and r=0.05𝑟0.05r=0.05 to illustrate the capability of our trained neural net pricer in the table below:

Table 6: FLMM Exchange Option Prediction Results

| N=1m, M=100 | τ=0.5𝜏0.5\tau=0.5 | τ=1𝜏1\tau=1 | τ=2𝜏2\tau=2 | Computation Time |
| --- | --- | --- | --- | --- |
| ρ=0.1𝜌0.1\rho=0.1 | 1.92002591.92002591.9200259 | 4.40978064.40978064.4097806 | 8.46083318.46083318.4608331 | 1028.88s |
| Neural Net | 1.92891191.92891191.9289119 | 4.39217544.39217544.3921754 | 8.4391038.4391038.439103 | 0.02s |
| ρ=0.3𝜌0.3\rho=0.3 | 1.45873091.45873091.4587309 | 3.58371043.58371043.5837104 | 7.16653197.16653197.1665319 | 992.23s |
| Neural Net | 1.44134491.44134491.4413449 | 3.57143083.57143083.5714308 | 7.1499927.1499927.149992 | 0.02s |
| ρ=0.5𝜌0.5\rho=0.5 | 1.00139511.00139511.0013951 | 2.71388712.71388712.7138871 | 5.75753915.75753915.7575391 | 995.11 |
| Neural Net | 1.003796051.003796051.00379605 | 2.70730132.70730132.7073013 | 5.73236755.73236755.7323675 | 0.02s |
| ρ=0.7𝜌0.7\rho=0.7 | 0.56746760.56746760.5674676 | 1.80493081.80493081.8049308 | 4.20728354.20728354.2072835 | 1032.56 |
| Neural Net | 0.56549360.56549360.5654936 | 1.79640921.79640921.7964092 | 4.1839544.1839544.183954 | 0.02s |
| ρ=0.9𝜌0.9\rho=0.9 | 0.202591040.202591040.20259104 | 0.888844140.888844140.88884414 | 2.48886842.48886842.4888684 | 1012.16 |
| Neural Net | 0.200344860.200344860.20034486 | 0.87358170.87358170.8735817 | 2.4740482.4740482.474048 | 0.02s |

## 6 Conclusions

In this paper, we explored the effects of liquidity on pricing Exchange Options in a binary-asset market which we refer to as FLMM. In this market, trading only affected the price of one (the iliquid) asset. Subsequently, we established the existence and uniqueness of a strong solution for
the SDEs driving the asset prices within FLMM. By the standard replication argument we obtained a two-dimensional BS-like PDE, which
characterized the options prices. We simulated asset prices by Milstein algorithm and developed a fast-converging MC estimator with the Margrabe option as its control variate. Finally, we deployed deep learning and further improved the pricing speed.

Conforming to our hypothesis, we observed the same transaction cost “super-replication” effect as described by Liu and Yong [[18](#bib.bib18)]. This paper may serve as a cautionary note for FX traders who regularly deal with option on iliquid currencies. Option issuers may also adopt this model as a LVA model for any type of Exchange Options.

## 7 Appendix

This section will include some of the formulas and proofs left out from the main body.

### 7.1 Finite Liquidity Existence and Uniqueness Theorem I

In this section, ∥⋅∥\|\cdot\| and |||⋅||||||\cdot||| represents the supremum norms:

|  |  |  |
| --- | --- | --- |
|  | ‖f‖=sup(s1,s2)∈𝒟1|f​(t,s1,s2)|, where ​𝒟1=(ℝ+)2,formulae-sequencenorm𝑓subscriptsupremumsubscript𝑠1subscript𝑠2subscript𝒟1𝑓𝑡subscript𝑠1subscript𝑠2 where subscript𝒟1superscriptsuperscriptℝ2\displaystyle\|f\|=\sup\_{(s\_{1},s\_{2})\in\mathcal{D}\_{1}}|f(t,s\_{1},s\_{2})|,\quad\text{ where }\mathcal{D}\_{1}=\big{(}\mathbbm{R}^{+}\big{)}^{2}, |  |
|  |  |  |
| --- | --- | --- |
|  | ‖|f|‖=sup(t,s1,s2)∈𝒟2|f​(t,s1,s2)|, where ​𝒟2=[0,T]×(ℝ+)2,formulae-sequencenorm𝑓subscriptsupremum𝑡subscript𝑠1subscript𝑠2subscript𝒟2𝑓𝑡subscript𝑠1subscript𝑠2 where subscript𝒟20𝑇superscriptsuperscriptℝ2\displaystyle|||f|||=\sup\_{(t,s\_{1},s\_{2})\in\mathcal{D}\_{2}}|f(t,s\_{1},s\_{2})|,\quad\text{ where }\mathcal{D}\_{2}=[0,T]\times\big{(}\mathbbm{R}^{+}\big{)}^{2}, |  |

The following combination of conditions (1)−(6)16(1)-(6) will guarantee existence and uniqueness of a strong solution for S1subscript𝑆1S\_{1}.

|  |  |  |
| --- | --- | --- |
|  | (1)‖λ​(s1​fs1​s1+s1​fs1​s2+fs2+s2​fs2+s2​fs1​s1+s2​fs1​s2+s2​fs2​s2)‖<∞.  1norm𝜆subscript𝑠1subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠1subscript𝑓subscript𝑠1subscript𝑠2subscript𝑓subscript𝑠2subscript𝑠2subscript𝑓subscript𝑠2subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠2subscript𝑠2subscript𝑓subscript𝑠2subscript𝑠2 \displaystyle(1)\qquad\|\lambda(s\_{1}f\_{s\_{1}s\_{1}}+s\_{1}f\_{s\_{1}s\_{2}}+f\_{s\_{2}}+s\_{2}f\_{s\_{2}}+s\_{2}f\_{s\_{1}s\_{1}}+s\_{2}f\_{s\_{1}s\_{2}}+s\_{2}f\_{s\_{2}s\_{2}})\|<\infty. |  |

|  |  |  |
| --- | --- | --- |
|  | (2)‖(λs1+λs2)​(s1​fs1+s2​fs1+s2​fs2)‖<∞.  2normsubscript𝜆subscript𝑠1subscript𝜆subscript𝑠2subscript𝑠1subscript𝑓subscript𝑠1subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠2subscript𝑓subscript𝑠2 \displaystyle(2)\qquad\|\big{(}\lambda\_{s\_{1}}+\lambda\_{s\_{2}}\big{)}\big{(}s\_{1}f\_{s\_{1}}+s\_{2}f\_{s\_{1}}+s\_{2}f\_{s\_{2}}\big{)}\|<\infty. |  |

|  |  |  |
| --- | --- | --- |
|  | (3)‖|1−λ​fs1|‖>δ0, for some ​δ0>0.formulae-sequence  3norm1𝜆subscript𝑓subscript𝑠1 subscript𝛿0 for some subscript𝛿00\displaystyle(3)\qquad|||1-\lambda{}f\_{s\_{1}}|||>\delta\_{0},\text{ for some }\delta\_{0}>0. |  |

|  |  |  |
| --- | --- | --- |
|  | (4)∥(λ+λs1+λs2)(ft+fs1+fs2+fs1​s1+fs1​s2+fs2​s2+fs1​s1​s2\displaystyle(4)\qquad\|(\lambda+\lambda\_{s\_{1}}+\lambda\_{s\_{2}})(f\_{t}+f\_{s\_{1}}+f\_{s\_{2}}+f\_{s\_{1}s\_{1}}+f\_{s\_{1}s\_{2}}+f\_{s\_{2}s\_{2}}+f\_{s\_{1}s\_{1}s\_{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | +fs1​s2​s2)∥<∞.\displaystyle+f\_{s\_{1}s\_{2}s\_{2}})\|<\infty. |  |

|  |  |  |
| --- | --- | --- |
|  | (5)‖λ​(ft​s1+ft​s2+fs1​s1​s1+fs2​s2​s2)+λs1​fs1​s1​s1+λs2​fs2​s2​s2‖<∞.  5norm𝜆subscript𝑓𝑡subscript𝑠1subscript𝑓𝑡subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠1subscript𝑓subscript𝑠2subscript𝑠2subscript𝑠2subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠1subscript𝜆subscript𝑠2subscript𝑓subscript𝑠2subscript𝑠2subscript𝑠2 \displaystyle(5)\qquad\|\lambda(f\_{ts\_{1}}+f\_{ts\_{2}}+f\_{s\_{1}s\_{1}s\_{1}}+f\_{s\_{2}s\_{2}s\_{2}})+\lambda\_{s\_{1}}f\_{s\_{1}s\_{1}s\_{1}}+\lambda\_{s\_{2}}f\_{s\_{2}s\_{2}s\_{2}}\|<\infty. |  |

|  |  |  |
| --- | --- | --- |
|  | (6)∥s1fs1​s1+s1fs1​s2+s2fs1​s2+s2fs2​s2+s12fs1​s1​s2+s12fs1​s2​s2+s1s2fs1​s1​s2\displaystyle(6)\qquad\|s\_{1}f\_{s\_{1}s\_{1}}+s\_{1}f\_{s\_{1}s\_{2}}+s\_{2}f\_{s\_{1}s\_{2}}+s\_{2}f\_{s\_{2}s\_{2}}+s\_{1}^{2}f\_{s\_{1}s\_{1}s\_{2}}+s\_{1}^{2}f\_{s\_{1}s\_{2}s\_{2}}+s\_{1}s\_{2}f\_{s\_{1}s\_{1}s\_{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | +s1s2fs1​s2​s2+s22fs1​s2​s2+s22fs2​s2​s2∥<∞.\displaystyle+s\_{1}s\_{2}f\_{s\_{1}s\_{2}s\_{2}}+s\_{2}^{2}f\_{s\_{1}s\_{2}s\_{2}}+s\_{2}^{2}f\_{s\_{2}s\_{2}s\_{2}}\|<\infty. |  |

###### Proof 7.1.

Recall that the SDE of S1subscript𝑆1S\_{1} is of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S1​(t)𝑑subscript𝑆1𝑡\displaystyle dS\_{1}(t) | =μ¯1​(𝐒​(t))​d​t+σ¯11​(𝐒​(t))​d​W1​(t)+σ¯12​(𝐒​(t))​d​W2​(t),absentsubscript¯𝜇1𝐒𝑡𝑑𝑡subscript¯𝜎11𝐒𝑡𝑑subscript𝑊1𝑡subscript¯𝜎12𝐒𝑡𝑑subscript𝑊2𝑡\displaystyle=\bar{\mu}\_{1}\big{(}\mathbf{S}(t)\big{)}dt+\bar{\sigma}\_{11}\big{(}\mathbf{S}(t)\big{)}dW\_{1}(t)+\bar{\sigma}\_{12}\big{(}\mathbf{S}(t)\big{)}dW\_{2}(t), |  |

where

|  |  |  |
| --- | --- | --- |
|  | μ¯1(t,s1,s2)=11−λ​fs1(μ1s1+λft+s2μ2λfs2+fs1​s2​(ρ​σ1​σ2​s1​s2+σ22​s22​λ​fs2)1−λ​fs1\displaystyle\bar{\mu}\_{1}(t,s\_{1},s\_{2})=\frac{1}{1-\lambda{}f\_{s\_{1}}}\Big{(}\mu\_{1}s\_{1}+\lambda{}f\_{t}+s\_{2}\mu\_{2}\lambda{}f\_{s\_{2}}+\frac{f\_{s\_{1}s\_{2}}(\rho\sigma\_{1}\sigma\_{2}s\_{1}s\_{2}+\sigma\_{2}^{2}s\_{2}^{2}\lambda{}f\_{s\_{2}})}{1-\lambda{}f\_{s\_{1}}} |  |
|  |  |  |
| --- | --- | --- |
|  | +fs1​s1​(σ12​s12+σ22​s22​λ2​fs22+2​ρ​σ1​σ2​s1​s2​λ​fs2)2​(1−λ​fs1)2+σ22​s22​fs2​s22),\displaystyle\qquad\qquad\quad+\frac{f\_{s\_{1}s\_{1}}(\sigma\_{1}^{2}s\_{1}^{2}+\sigma^{2}\_{2}s\_{2}^{2}\lambda^{2}f\_{s\_{2}}^{2}+2\rho\sigma\_{1}\sigma\_{2}s\_{1}s\_{2}\lambda{}f\_{s\_{2}})}{2\big{(}1-\lambda{}f\_{s\_{1}}\big{)}^{2}}+\frac{\sigma\_{2}^{2}s\_{2}^{2}f\_{s\_{2}s\_{2}}}{2}\Big{)}, |  |
|  |  |  |
| --- | --- | --- |
|  | σ¯11​(t,s1,s2)=σ1​s11−λ​fs1,σ¯12​(t,s1,s2)=σ2​s2​λ​fs21−λ​fs1.formulae-sequencesubscript¯𝜎11𝑡subscript𝑠1subscript𝑠2subscript𝜎1subscript𝑠11𝜆subscript𝑓subscript𝑠1subscript¯𝜎12𝑡subscript𝑠1subscript𝑠2subscript𝜎2subscript𝑠2𝜆subscript𝑓subscript𝑠21𝜆subscript𝑓subscript𝑠1\displaystyle\bar{\sigma}\_{11}(t,s\_{1},s\_{2})=\frac{\sigma\_{1}s\_{1}}{1-\lambda{}f\_{s\_{1}}},\qquad\bar{\sigma}\_{12}(t,s\_{1},s\_{2})=\frac{\sigma\_{2}s\_{2}\lambda{}f\_{s\_{2}}}{1-\lambda{}f\_{s\_{1}}}. |  |

Following the classical existence uniqueness result for SDEs, we have to show the functions μ¯1​(t,s1,s2)subscript¯𝜇1𝑡subscript𝑠1subscript𝑠2\bar{\mu}\_{1}(t,s\_{1},s\_{2}), σ¯11​(t,s1,s2)subscript¯𝜎11𝑡subscript𝑠1subscript𝑠2\bar{\sigma}\_{11}(t,s\_{1},s\_{2}) and σ¯12​(t,s1,s2)subscript¯𝜎12𝑡subscript𝑠1subscript𝑠2\bar{\sigma}\_{12}(t,s\_{1},s\_{2}) are uniformly Lipschitz continuous with respect to ∥⋅∥\|\cdot\|. Thus, it is sufficient to check the boundedness of their respective partial derivatives. Computing the derivatives, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | [σ¯11]s1subscriptdelimited-[]subscript¯𝜎11subscript𝑠1\displaystyle\big{[}\bar{\sigma}\_{11}\big{]}\_{s\_{1}} | =σ1​(11−λ​fs1+s1​(λs1​fs1+λ​fs1​s1)(1−λ​fs1)2),absentsubscript𝜎111𝜆subscript𝑓subscript𝑠1subscript𝑠1subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠1superscript1𝜆subscript𝑓subscript𝑠12\displaystyle=\sigma\_{1}\big{(}\frac{1}{1-\lambda{}f\_{s\_{1}}}+\frac{s\_{1}(\lambda\_{s\_{1}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{2}}\big{)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | [σ¯11]s2subscriptdelimited-[]subscript¯𝜎11subscript𝑠2\displaystyle\big{[}\bar{\sigma}\_{11}\big{]}\_{s\_{2}} | =σ1​s1​λs2​fs1+λ​fs1​s2(1−λ​fs1)2,absentsubscript𝜎1subscript𝑠1subscript𝜆subscript𝑠2subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠2superscript1𝜆subscript𝑓subscript𝑠12\displaystyle=\sigma\_{1}s\_{1}\frac{\lambda\_{s\_{2}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{2}}}{(1-\lambda{}f\_{s\_{1}})^{2}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | [σ¯12]s1subscriptdelimited-[]subscript¯𝜎12subscript𝑠1\displaystyle\big{[}\bar{\sigma}\_{12}\big{]}\_{s\_{1}} | =σ2​s2​((λs1​fs2+λ​fs1​s2)1−λ​fs1+λ​fs2​(λ​fs1​s1+λs1​fs1)(1−λ​fs1)2),absentsubscript𝜎2subscript𝑠2subscript𝜆subscript𝑠1subscript𝑓subscript𝑠2𝜆subscript𝑓subscript𝑠1subscript𝑠21𝜆subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠2𝜆subscript𝑓subscript𝑠1subscript𝑠1subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1superscript1𝜆subscript𝑓subscript𝑠12\displaystyle=\sigma\_{2}s\_{2}\big{(}\frac{(\lambda\_{s\_{1}}f\_{s\_{2}}+\lambda{}f\_{s\_{1}s\_{2}})}{1-\lambda{}f\_{s\_{1}}}+\frac{\lambda{}f\_{s\_{2}}(\lambda{}f\_{s\_{1}s\_{1}}+\lambda\_{s\_{1}}f\_{s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{2}}\big{)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | [σ¯12]s2subscriptdelimited-[]subscript¯𝜎12subscript𝑠2\displaystyle\big{[}\bar{\sigma}\_{12}\big{]}\_{s\_{2}} | =σ2​(λ​fs2+s2​(λs2​fs2+λ​fs2​s2)1−λ​fs1+λ​s2​fs2​(λs2​fs1+λ​fs1​s2)(1−λ​fs1)2).absentsubscript𝜎2𝜆subscript𝑓subscript𝑠2subscript𝑠2subscript𝜆subscript𝑠2subscript𝑓subscript𝑠2𝜆subscript𝑓subscript𝑠2subscript𝑠21𝜆subscript𝑓subscript𝑠1𝜆subscript𝑠2subscript𝑓subscript𝑠2subscript𝜆subscript𝑠2subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠2superscript1𝜆subscript𝑓subscript𝑠12\displaystyle=\sigma\_{2}\big{(}\frac{\lambda{}f\_{s\_{2}}+s\_{2}(\lambda\_{s\_{2}}f\_{s\_{2}}+\lambda{}f\_{s\_{2}s\_{2}})}{1-\lambda{}f\_{s\_{1}}}+\lambda\frac{s\_{2}f\_{s\_{2}}(\lambda\_{s\_{2}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{2}})}{(1-\lambda{}f\_{s\_{1}})^{2}}\big{)}. |  |

We can clearly see the boundedness requirement for [σ¯11]s1subscriptdelimited-[]subscript¯𝜎11subscript𝑠1\big{[}\bar{\sigma}\_{11}\big{]}\_{s\_{1}}, [σ¯12]s1subscriptdelimited-[]subscript¯𝜎12subscript𝑠1\big{[}\bar{\sigma}\_{12}\big{]}\_{s\_{1}}, [σ¯11]s2subscriptdelimited-[]subscript¯𝜎11subscript𝑠2\big{[}\bar{\sigma}\_{11}\big{]}\_{s\_{2}} and [σ¯12]s2subscriptdelimited-[]subscript¯𝜎12subscript𝑠2\big{[}\bar{\sigma}\_{12}\big{]}\_{s\_{2}} can be condensed into:

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | ‖λ​(s1​fs1​s1+s1​fs1​s2+fs2+s2​fs2+s2​fs1​s1+s2​fs1​s2+s2​fs2​s2)‖<∞,norm𝜆subscript𝑠1subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠1subscript𝑓subscript𝑠1subscript𝑠2subscript𝑓subscript𝑠2subscript𝑠2subscript𝑓subscript𝑠2subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠2subscript𝑠2subscript𝑓subscript𝑠2subscript𝑠2\displaystyle\|\lambda(s\_{1}f\_{s\_{1}s\_{1}}+s\_{1}f\_{s\_{1}s\_{2}}+f\_{s\_{2}}+s\_{2}f\_{s\_{2}}+s\_{2}f\_{s\_{1}s\_{1}}+s\_{2}f\_{s\_{1}s\_{2}}+s\_{2}f\_{s\_{2}s\_{2}})\|<\infty, |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | ‖(λs1+λs2)​(s1​fs1+s2​fs1+s2​fs2)‖<∞.normsubscript𝜆subscript𝑠1subscript𝜆subscript𝑠2subscript𝑠1subscript𝑓subscript𝑠1subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠2subscript𝑓subscript𝑠2\displaystyle\|\big{(}\lambda\_{s\_{1}}+\lambda\_{s\_{2}}\big{)}\big{(}s\_{1}f\_{s\_{1}}+s\_{2}f\_{s\_{1}}+s\_{2}f\_{s\_{2}}\big{)}\|<\infty. |  |

Furthermore, we will require the denominator terms in the partial derivatives above to satisfy:

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | ‖|1−λ​fs1|‖>δ0, for some ​δ0>0.formulae-sequencenorm1𝜆subscript𝑓subscript𝑠1subscript𝛿0 for some subscript𝛿00\displaystyle|||1-\lambda{}f\_{s\_{1}}|||>\delta\_{0},\text{ for some }\delta\_{0}>0. |  |

The partial derivatives [μ¯1​s1]s1subscriptdelimited-[]subscript¯𝜇1subscript𝑠1subscript𝑠1\big{[}\bar{\mu}\_{1}s\_{1}\big{]}\_{s\_{1}} and [μ¯1​s1]s2subscriptdelimited-[]subscript¯𝜇1subscript𝑠1subscript𝑠2\big{[}\bar{\mu}\_{1}s\_{1}\big{]}\_{s\_{2}} are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | [μ¯1​s1]s1subscriptdelimited-[]subscript¯𝜇1subscript𝑠1subscript𝑠1\displaystyle\big{[}\bar{\mu}\_{1}s\_{1}\big{]}\_{s\_{1}} | =μ1​(11−λ​fs1+s1​(λs1​fs1+λ​fs1​s1)(1−λ​fs1)2)+λ​ft​s1+λs1​ft1−λ​fs1absentsubscript𝜇111𝜆subscript𝑓subscript𝑠1subscript𝑠1subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠1superscript1𝜆subscript𝑓subscript𝑠12𝜆subscript𝑓𝑡subscript𝑠1subscript𝜆subscript𝑠1subscript𝑓𝑡1𝜆subscript𝑓subscript𝑠1\displaystyle=\mu\_{1}\big{(}\frac{1}{1-\lambda{}f\_{s\_{1}}}+\frac{s\_{1}(\lambda\_{s\_{1}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{2}}\big{)}+\frac{\lambda{}f\_{ts\_{1}}+\lambda\_{s\_{1}}f\_{t}}{1-\lambda{}f\_{s\_{1}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ​ft​(λs1​fs1+λ​fs1​s1)(1−λ​fs1)2+μ2​s2​(λ​fs1​s2+λs1​fs21−λ​fs1+λ​fs2​(λs1​fs1+λ​fs1​s1)(1−λ​fs1)2)𝜆subscript𝑓𝑡subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠1superscript1𝜆subscript𝑓subscript𝑠12subscript𝜇2subscript𝑠2𝜆subscript𝑓subscript𝑠1subscript𝑠2subscript𝜆subscript𝑠1subscript𝑓subscript𝑠21𝜆subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠2subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠1superscript1𝜆subscript𝑓subscript𝑠12\displaystyle+\frac{\lambda{}f\_{t}(\lambda\_{s\_{1}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{2}}+\mu\_{2}s\_{2}\big{(}\frac{\lambda{}f\_{s\_{1}s\_{2}}+\lambda\_{s\_{1}}f\_{s\_{2}}}{1-\lambda{}f\_{s\_{1}}}+\frac{\lambda{}f\_{s\_{2}}(\lambda\_{s\_{1}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{2}}\big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​σ12​(s12​fs1​s1​s1+2​s1​fs1​s1(1−λ​fs1)3+3​s12​fs1​s1​(λs1​fs1+λ​fs1​s1)(1−λ​fs1)4)12superscriptsubscript𝜎12superscriptsubscript𝑠12subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠12subscript𝑠1subscript𝑓subscript𝑠1subscript𝑠1superscript1𝜆subscript𝑓subscript𝑠133superscriptsubscript𝑠12subscript𝑓subscript𝑠1subscript𝑠1subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠1superscript1𝜆subscript𝑓subscript𝑠14\displaystyle+\frac{1}{2}\sigma\_{1}^{2}\big{(}\frac{s\_{1}^{2}f\_{s\_{1}s\_{1}s\_{1}}+2s\_{1}f\_{s\_{1}s\_{1}}}{(1-\lambda{}f\_{s\_{1}})^{3}}+3\frac{s\_{1}^{2}f\_{s\_{1}s\_{1}}(\lambda\_{s\_{1}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{4}}\big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12σ22s22(λ2​fs22​fs1​s1​s1+2​λ​fs2​fs1​s1​(λs1​fs2+λ​fs1​s2)(1−λ​fs1)3\displaystyle+\frac{1}{2}\sigma\_{2}^{2}s\_{2}^{2}\big{(}\frac{\lambda^{2}f\_{s\_{2}}^{2}f\_{s\_{1}s\_{1}s\_{1}}+2\lambda{}f\_{s\_{2}}f\_{s\_{1}s\_{1}}(\lambda\_{s\_{1}}f\_{s\_{2}}+\lambda{}f\_{s\_{1}s\_{2}})}{(1-\lambda{}f\_{s\_{1}})^{3}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3λ2​fs22​fs1​s1​(λs1​fs1+λ​fs1​s1)(1−λ​fs1)4)\displaystyle+3\frac{\lambda^{2}f\_{s\_{2}}^{2}f\_{s\_{1}s\_{1}}(\lambda\_{s\_{1}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{4}}\big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ρσ1σ2s2(s1​λ​fs2​fs1​s1​s1+s1​fs1​s1​(λs1​fs2+λ​fs1​s2)+λ​fs1​s1​fs2(1−λ​fs1)3\displaystyle+\rho\sigma\_{1}\sigma\_{2}s\_{2}\big{(}\frac{s\_{1}\lambda{}f\_{s\_{2}}f\_{s\_{1}s\_{1}s\_{1}}+s\_{1}f\_{s\_{1}s\_{1}}(\lambda\_{s\_{1}}f\_{s\_{2}}+\lambda{}f\_{s\_{1}s\_{2}})+\lambda{}f\_{s\_{1}s\_{1}}f\_{s\_{2}}}{(1-\lambda{}f\_{s\_{1}})^{3}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +3s1​λ​fs2​fs1​s1​(λs1​fs1+λ​fs1​s1)(1−λ​fs1)4)\displaystyle+3\frac{s\_{1}\lambda{}f\_{s\_{2}}f\_{s\_{1}s\_{1}}(\lambda\_{s\_{1}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{4}}\big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ρ​σ1​σ2​s2​(fs1​s2+s1​fs1​s1​s2(1−λ​fs1)2+2​s1​(λs1​fs1+λ​fs1​s1)(1−λ​fs1)3)𝜌subscript𝜎1subscript𝜎2subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠2subscript𝑠1subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠2superscript1𝜆subscript𝑓subscript𝑠122subscript𝑠1subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠1superscript1𝜆subscript𝑓subscript𝑠13\displaystyle+\rho\sigma\_{1}\sigma\_{2}s\_{2}\big{(}\frac{f\_{s\_{1}s\_{2}}+s\_{1}f\_{s\_{1}s\_{1}s\_{2}}}{(1-\lambda{}f\_{s\_{1}})^{2}}+2\frac{s\_{1}(\lambda\_{s\_{1}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{3}}\big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +σ22​s22​(λ​fs2​fs1​s1​s2+fs1​s2​(λs1​fs1+λ​fs1​s1)(1−λ​fs1)2+λ​fs2​fs1​s2​(λs1​fs1+λ​fs1​s1)(1−λ​fs1)3)superscriptsubscript𝜎22superscriptsubscript𝑠22𝜆subscript𝑓subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠2subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠1superscript1𝜆subscript𝑓subscript𝑠12𝜆subscript𝑓subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠2subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠1superscript1𝜆subscript𝑓subscript𝑠13\displaystyle+\sigma\_{2}^{2}s\_{2}^{2}\big{(}\frac{\lambda{}f\_{s\_{2}}f\_{s\_{1}s\_{1}s\_{2}}+f\_{s\_{1}s\_{2}}(\lambda\_{s\_{1}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{2}}+\frac{\lambda{}f\_{s\_{2}}f\_{s\_{1}s\_{2}}(\lambda\_{s\_{1}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{3}}\big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​σ22​s22​(fs1​s2​s21−λ​fs1+fs2​s2​(λs1​fs1+λ​fs1​s1)(1−λ​fs1)2).12superscriptsubscript𝜎22superscriptsubscript𝑠22subscript𝑓subscript𝑠1subscript𝑠2subscript𝑠21𝜆subscript𝑓subscript𝑠1subscript𝑓subscript𝑠2subscript𝑠2subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠1superscript1𝜆subscript𝑓subscript𝑠12\displaystyle+\frac{1}{2}\sigma\_{2}^{2}s\_{2}^{2}\big{(}\frac{f\_{s\_{1}s\_{2}s\_{2}}}{1-\lambda{}f\_{s\_{1}}}+\frac{f\_{s\_{2}s\_{2}}(\lambda\_{s\_{1}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{1}})}{(1-\lambda{}f\_{s\_{1}})^{2}}\big{)}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | [μ¯1​s1]s2=subscriptdelimited-[]subscript¯𝜇1subscript𝑠1subscript𝑠2absent\displaystyle\big{[}\bar{\mu}\_{1}s\_{1}\big{]}\_{s\_{2}}= | μ1​s1​λs2​fs1+λ​fs1​s2(1−λ​fs1)2+λs2​ft+λ​ft​s21−λ​fs1+λ​ft​(λs2​fs1+λ​fs1​s2)(1−λ​fs1)2subscript𝜇1subscript𝑠1subscript𝜆subscript𝑠2subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠2superscript1𝜆subscript𝑓subscript𝑠12subscript𝜆subscript𝑠2subscript𝑓𝑡𝜆subscript𝑓𝑡subscript𝑠21𝜆subscript𝑓subscript𝑠1𝜆subscript𝑓𝑡subscript𝜆subscript𝑠2subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠2superscript1𝜆subscript𝑓subscript𝑠12\displaystyle\mu\_{1}s\_{1}\frac{\lambda\_{s\_{2}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{2}}}{(1-\lambda{}f\_{s\_{1}})^{2}}+\frac{\lambda\_{s\_{2}}f\_{t}+\lambda{}f\_{ts\_{2}}}{1-\lambda{}f\_{s\_{1}}}+\frac{\lambda{}f\_{t}(\lambda\_{s\_{2}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{2}})}{(1-\lambda{}f\_{s\_{1}})^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | μ2​(λ​fs2+s2​(λs2​fs2+λ​fs1​s2)1−λ​fs1+s2​λ​fs2​(λs2​fs1+λ​fs1​s2)(1−λ​fs1)2)subscript𝜇2𝜆subscript𝑓subscript𝑠2subscript𝑠2subscript𝜆subscript𝑠2subscript𝑓subscript𝑠2𝜆subscript𝑓subscript𝑠1subscript𝑠21𝜆subscript𝑓subscript𝑠1subscript𝑠2𝜆subscript𝑓subscript𝑠2subscript𝜆subscript𝑠2subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠2superscript1𝜆subscript𝑓subscript𝑠12\displaystyle\mu\_{2}\big{(}\frac{\lambda{}f\_{s\_{2}}+s\_{2}(\lambda\_{s\_{2}}f\_{s\_{2}}+\lambda{}f\_{s\_{1}s\_{2}})}{1-\lambda{}f\_{s\_{1}}}+\frac{s\_{2}\lambda{}f\_{s\_{2}}(\lambda\_{s\_{2}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{2}})}{(1-\lambda{}f\_{s\_{1}})^{2}}\big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | 12​σ12​s12​(fs1​s1​s2(1−λ​fs1)3+3​fs1​s1​(λs2​fs1+λ​fs1​s2)(1−λ​fs1)4)12superscriptsubscript𝜎12superscriptsubscript𝑠12subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠2superscript1𝜆subscript𝑓subscript𝑠133subscript𝑓subscript𝑠1subscript𝑠1subscript𝜆subscript𝑠2subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠2superscript1𝜆subscript𝑓subscript𝑠14\displaystyle\frac{1}{2}\sigma\_{1}^{2}s\_{1}^{2}\big{(}\frac{f\_{s\_{1}s\_{1}s\_{2}}}{(1-\lambda{}f\_{s\_{1}})^{3}}+3\frac{f\_{s\_{1}s\_{1}}(\lambda\_{s\_{2}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{2}})}{(1-\lambda{}f\_{s\_{1}})^{4}}\big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | 12σ22(λ2​fs1​s1​fs22+s2​(λ2+fs1​s1​s2​fs22+fs1​s1​(2​λ​λs2​fs22+s​λ2​fs2​fs2​s2))(1−λ​fs1)3\displaystyle\frac{1}{2}\sigma\_{2}^{2}\Big{(}\frac{\lambda^{2}f\_{s\_{1}s\_{1}}f\_{s\_{2}}^{2}+s\_{2}\big{(}\lambda^{2}+f\_{s\_{1}s\_{1}s\_{2}}f\_{s\_{2}}^{2}+f\_{s\_{1}s\_{1}}(2\lambda\lambda\_{s\_{2}}f\_{s\_{2}}^{2}+s\lambda^{2}f\_{s\_{2}}f\_{s\_{2}s\_{2}})\big{)}}{(1-\lambda{}f\_{s\_{1}})^{3}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | 3s2​λ2​fs1​s1​fs22​(λs2​fs1+λ​fs1​s2)(1−λ​fs1)4)\displaystyle 3\frac{s\_{2}\lambda^{2}f\_{s\_{1}s\_{1}}f\_{s\_{2}}^{2}(\lambda\_{s\_{2}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{2}})}{(1-\lambda{}f\_{s\_{1}})^{4}}\Big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | ρσ1σ2s1(λ​fs2​fs12+s2​(λs2​fs2​fs12+λ​(fs2​s2​fs12+2​fs2​fs1​fs1​s2))(1−λ​fs1)3\displaystyle\rho\sigma\_{1}\sigma\_{2}s\_{1}\Big{(}\frac{\lambda{}f\_{s\_{2}}f\_{s\_{1}}^{2}+s\_{2}\big{(}\lambda\_{s\_{2}}f\_{s\_{2}}f\_{s\_{1}}^{2}+\lambda(f\_{s\_{2}s\_{2}}f\_{s\_{1}}^{2}+2f\_{s\_{2}}f\_{s\_{1}}f\_{s\_{1}s\_{2}})\big{)}}{(1-\lambda{}f\_{s\_{1}})^{3}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | 3s2​λ​fs2​fs1​s1​(λs2​fs1+λ​fs1​s2)(1−λ​fs1)4)\displaystyle 3\frac{s\_{2}\lambda{}f\_{s\_{2}}f\_{s\_{1}s\_{1}}(\lambda\_{s\_{2}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{2}})}{(1-\lambda{}f\_{s\_{1}})^{4}}\Big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | ρ​σ1​σ2​s1​(fs1​s2+s2​fs1​s2​s2(1−λ​fs1)2+s2fs1​s2(λs2fs1+λfs1​s2(1−λ​fs1)3)\displaystyle\rho\sigma\_{1}\sigma\_{2}s\_{1}\big{(}\frac{f\_{s\_{1}s\_{2}}+s\_{2}f\_{s\_{1}s\_{2}s\_{2}}}{(1-\lambda{}f\_{s\_{1}})^{2}}+\frac{s\_{2}f\_{s\_{1}s\_{2}}(\lambda\_{s\_{2}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{2}}}{(1-\lambda{}f\_{s\_{1}})^{3}}\big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | σ22(2​s22​λ​fs2​fs1​s2+s22​(λs2​fs2​fs1​s2+λ​(fs1​s2​fs2​s2+fs2​fs1​s2​s2))(1−λ​fs1)2\displaystyle\sigma\_{2}^{2}\Big{(}\frac{2s\_{2}^{2}\lambda{}f\_{s\_{2}}f\_{s\_{1}s\_{2}}+s\_{2}^{2}\big{(}\lambda\_{s\_{2}}f\_{s\_{2}}f\_{s\_{1}s\_{2}}+\lambda(f\_{s\_{1}s\_{2}}f\_{s\_{2}s\_{2}}+f\_{s\_{2}}f\_{s\_{1}s\_{2}s\_{2}})\big{)}}{(1-\lambda{}f\_{s\_{1}})^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | s22​λ​fs2​fs1​s2​(λs2​fs1+λ​fs1​s2)(1−λ​fs1)3)\displaystyle\frac{s\_{2}^{2}\lambda{}f\_{s\_{2}}f\_{s\_{1}s\_{2}}(\lambda\_{s\_{2}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{2}})}{(1-\lambda{}f\_{s\_{1}})^{3}}\Big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | 12​σ22​(2​s2​fs2​s2+s22​fs2​s2​s21−λ​fs1+s22​fs2​s2​(λs2​fs1+λ​fs1​s2)(1−λ​fs1)2).12superscriptsubscript𝜎222subscript𝑠2subscript𝑓subscript𝑠2subscript𝑠2superscriptsubscript𝑠22subscript𝑓subscript𝑠2subscript𝑠2subscript𝑠21𝜆subscript𝑓subscript𝑠1superscriptsubscript𝑠22subscript𝑓subscript𝑠2subscript𝑠2subscript𝜆subscript𝑠2subscript𝑓subscript𝑠1𝜆subscript𝑓subscript𝑠1subscript𝑠2superscript1𝜆subscript𝑓subscript𝑠12\displaystyle\frac{1}{2}\sigma\_{2}^{2}\big{(}\frac{2s\_{2}f\_{s\_{2}s\_{2}}+s\_{2}^{2}f\_{s\_{2}s\_{2}s\_{2}}}{1-\lambda{}f\_{s\_{1}}}+\frac{s\_{2}^{2}f\_{s\_{2}s\_{2}}(\lambda\_{s\_{2}}f\_{s\_{1}}+\lambda{}f\_{s\_{1}s\_{2}})}{(1-\lambda{}f\_{s\_{1}})^{2}}\big{)}. |  |

We conclude the partial derivatives of μ¯1​(t,s1,s2)subscript¯𝜇1𝑡subscript𝑠1subscript𝑠2\bar{\mu}\_{1}(t,s\_{1},s\_{2}) will be bonded when ‖|1−λ​fs1|‖>δ0norm1𝜆subscript𝑓subscript𝑠1subscript𝛿0|||1-\lambda{}f\_{s\_{1}}|||>\delta\_{0} and:

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | ∥(λ+λs1+λs2)(ft+fs1+fs2+fs1​s1+fs1​s2+fs2​s2+fs1​s1​s2\displaystyle\|(\lambda+\lambda\_{s\_{1}}+\lambda\_{s\_{2}})(f\_{t}+f\_{s\_{1}}+f\_{s\_{2}}+f\_{s\_{1}s\_{1}}+f\_{s\_{1}s\_{2}}+f\_{s\_{2}s\_{2}}+f\_{s\_{1}s\_{1}s\_{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | +fs1​s2​s2)∥<∞,\displaystyle+f\_{s\_{1}s\_{2}s\_{2}})\|<\infty, |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | ‖λ​(ft​s1+ft​s2+fs1​s1​s1+fs2​s2​s2)+λs1​fs1​s1​s1+λs2​fs2​s2​s2‖<∞,norm𝜆subscript𝑓𝑡subscript𝑠1subscript𝑓𝑡subscript𝑠2subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠1subscript𝑓subscript𝑠2subscript𝑠2subscript𝑠2subscript𝜆subscript𝑠1subscript𝑓subscript𝑠1subscript𝑠1subscript𝑠1subscript𝜆subscript𝑠2subscript𝑓subscript𝑠2subscript𝑠2subscript𝑠2\displaystyle\|\lambda(f\_{ts\_{1}}+f\_{ts\_{2}}+f\_{s\_{1}s\_{1}s\_{1}}+f\_{s\_{2}s\_{2}s\_{2}})+\lambda\_{s\_{1}}f\_{s\_{1}s\_{1}s\_{1}}+\lambda\_{s\_{2}}f\_{s\_{2}s\_{2}s\_{2}}\|<\infty, |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (15) |  | ∥s1fs1​s1+s1fs1​s2+s2fs1​s2+s2fs2​s2+s12fs1​s1​s2+s12fs1​s2​s2+s1s2fs1​s1​s2\displaystyle\|s\_{1}f\_{s\_{1}s\_{1}}+s\_{1}f\_{s\_{1}s\_{2}}+s\_{2}f\_{s\_{1}s\_{2}}+s\_{2}f\_{s\_{2}s\_{2}}+s\_{1}^{2}f\_{s\_{1}s\_{1}s\_{2}}+s\_{1}^{2}f\_{s\_{1}s\_{2}s\_{2}}+s\_{1}s\_{2}f\_{s\_{1}s\_{1}s\_{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | +s1s2fs1​s2​s2+s22fs1​s2​s2+s22fs2​s2​s2∥<∞,\displaystyle+s\_{1}s\_{2}f\_{s\_{1}s\_{2}s\_{2}}+s\_{2}^{2}f\_{s\_{1}s\_{2}s\_{2}}+s\_{2}^{2}f\_{s\_{2}s\_{2}s\_{2}}\|<\infty, |  |

The combination of requirements ([10](#S7.E10 "Equation 10 ‣ Proof 7.1. ‣ 7.1 Finite Liquidity Existence and Uniqueness Theorem I ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")), ([11](#S7.E11 "Equation 11 ‣ Proof 7.1. ‣ 7.1 Finite Liquidity Existence and Uniqueness Theorem I ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")), ([12](#S7.E12 "Equation 12 ‣ Proof 7.1. ‣ 7.1 Finite Liquidity Existence and Uniqueness Theorem I ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")), ([13](#S7.E13 "Equation 13 ‣ Proof 7.1. ‣ 7.1 Finite Liquidity Existence and Uniqueness Theorem I ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")), ([14](#S7.E14 "Equation 14 ‣ Proof 7.1. ‣ 7.1 Finite Liquidity Existence and Uniqueness Theorem I ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")), ([15](#S7.E15 "Equation 15 ‣ Proof 7.1. ‣ 7.1 Finite Liquidity Existence and Uniqueness Theorem I ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")) will guarantee s1​μ¯1​(t,s1,s2)subscript𝑠1subscript¯𝜇1𝑡subscript𝑠1subscript𝑠2s\_{1}\bar{\mu}\_{1}(t,s\_{1},s\_{2}), s1​σ¯11​(t,s1,s2)subscript𝑠1subscript¯𝜎11𝑡subscript𝑠1subscript𝑠2s\_{1}\bar{\sigma}\_{11}(t,s\_{1},s\_{2}) and s1​σ¯12​(t,s1,s2)subscript𝑠1subscript¯𝜎12𝑡subscript𝑠1subscript𝑠2s\_{1}\bar{\sigma}\_{12}(t,s\_{1},s\_{2}) are uniformly Lipschitz continuous in (ℝ+)2superscriptsuperscriptℝ2\big{(}\mathbb{R}^{+}\big{)}^{2}. By Itô’s Existence and Uniqueness Theorem Itô [[16](#bib.bib16)] (1979), the SDE for S1subscript𝑆1S\_{1} will have a unique strong solution.

### 7.2 Finite Liquidity Existence and Uniqueness Theorem II

To show the SDE have a unique strong solution, it is sufficient to show that the conditions (1)−(6)16(1)-(6) in Appendix Section [7.1](#S7.SS1 "7.1 Finite Liquidity Existence and Uniqueness Theorem I ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.") are satisfied for the particular choice of λ​(t,s1)𝜆𝑡subscript𝑠1\lambda(t,s\_{1}) and f​(t,s1,s2)=Δ1​(t)𝑓𝑡subscript𝑠1subscript𝑠2subscriptΔ1𝑡f(t,s\_{1},s\_{2})=\Delta\_{1}(t).

* •

  Condition (1):

  |  |  |  |
  | --- | --- | --- |
  |  | ‖λ​(s1​S​p​d111+s1​S​p​d112+Γ12+s2​Γ12+s2​S​p​d111+s2​S​p​d112+s2​S​p​d122)‖norm𝜆subscript𝑠1𝑆𝑝subscript𝑑111subscript𝑠1𝑆𝑝subscript𝑑112subscriptΓ12subscript𝑠2subscriptΓ12subscript𝑠2𝑆𝑝subscript𝑑111subscript𝑠2𝑆𝑝subscript𝑑112subscript𝑠2𝑆𝑝subscript𝑑122\displaystyle\|\lambda(s\_{1}Spd\_{111}+s\_{1}Spd\_{112}+\Gamma\_{12}+s\_{2}\Gamma\_{12}+s\_{2}Spd\_{111}+s\_{2}Spd\_{112}+s\_{2}Spd\_{122})\| |  |
  |  |  |  |
  | --- | --- | --- |
  |  | =∥λ(N′​(d+)σ​s1​τ(2​d+σ​s1​τ+1)+s12​d+​N′​(d+)σ2​τ​s1​s2+1σ​τs2​N′​(d+)s12+s22​N′​(d+)σ​τ​s12\displaystyle=\|\lambda\Big{(}\frac{N^{\prime}(d\_{+})}{\sigma{}s\_{1}\sqrt{\tau}}\big{(}\frac{2d\_{+}}{\sigma{}s\_{1}\sqrt{\tau}}+1\big{)}+s\_{1}\frac{2d\_{+}N^{\prime}(d\_{+})}{\sigma^{2}\tau{}s\_{1}s\_{2}}+\frac{1}{\sigma\sqrt{\tau}}\frac{s\_{2}N^{\prime}(d\_{+})}{s\_{1}^{2}}+\frac{s\_{2}^{2}N^{\prime}(d\_{+})}{\sigma\sqrt{\tau}s\_{1}^{2}} |  |
  |  |  |  |
  | --- | --- | --- |
  |  | +s2​N′​(d+)σ​s12​τ(2​d+σ​s1​τ+1)+2​d+​N′​(d+)σ2​τ​s1+2​d−​s2​N′​(d+)σ2​τ​s12)∥<∞.\displaystyle+\frac{s\_{2}N^{\prime}(d\_{+})}{\sigma{}s\_{1}^{2}\sqrt{\tau}}\big{(}\frac{2d\_{+}}{\sigma{}s\_{1}\sqrt{\tau}}+1\big{)}+\frac{2d\_{+}N^{\prime}(d\_{+})}{\sigma^{2}\tau{}s\_{1}}+\frac{2d\_{-}s\_{2}N^{\prime}(d\_{+})}{\sigma^{2}\tau{}s\_{1}^{2}}\Big{)}\|<\infty. |  |

  ###### Proof 7.2.

  Notice there is a common term of the form N′​(d+)s1nsuperscript𝑁′subscript𝑑superscriptsubscript𝑠1𝑛\frac{N^{\prime}(d\_{+})}{s\_{1}^{n}}. These terms appears naturally in higher order Greeks. Consider any real number n𝑛n, we have:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | N′​(d+)s1nsuperscript𝑁′subscript𝑑superscriptsubscript𝑠1𝑛\displaystyle\frac{N^{\prime}(d\_{+})}{s\_{1}^{n}} | =1s1n​2​π​exp⁡{−(log⁡(s1s2)+12​σ2​τσ​τ)2}absent1superscriptsubscript𝑠1𝑛2𝜋superscriptsubscript𝑠1subscript𝑠212superscript𝜎2𝜏𝜎𝜏2\displaystyle=\frac{1}{s\_{1}^{n}\sqrt{2\pi}}\exp{\Big{\{}-\Big{(}\frac{\log(\frac{s\_{1}}{s\_{2}})+\frac{1}{2}\sigma^{2}\tau}{\sigma\sqrt{\tau}}\Big{)}^{2}\Big{\}}} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =1s1n​2​π​e{−log2⁡(s1)+log⁡(s1)​(12​σ2​τ−log⁡(s2))+(12​σ2​τ−log⁡(s2))2σ2​τ}​e−n​log⁡(s1)absent1superscriptsubscript𝑠1𝑛2𝜋superscript𝑒superscript2subscript𝑠1subscript𝑠112superscript𝜎2𝜏subscript𝑠2superscript12superscript𝜎2𝜏subscript𝑠22superscript𝜎2𝜏superscript𝑒𝑛subscript𝑠1\displaystyle=\frac{1}{s\_{1}^{n}\sqrt{2\pi}}e^{\Big{\{}-\frac{\log^{2}(s\_{1})+\log(s\_{1})\big{(}\frac{1}{2}\sigma^{2}\tau-\log(s\_{2})\big{)}+\big{(}\frac{1}{2}\sigma^{2}\tau-\log(s\_{2})\big{)}^{2}}{\sigma^{2}\tau}\Big{\}}}e^{-n\log(s\_{1})} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =12​π​exp⁡{−log2⁡(s1)+o​(log⁡(s1))σ2​τ},absent12𝜋superscript2subscript𝑠1𝑜subscript𝑠1superscript𝜎2𝜏\displaystyle=\frac{1}{\sqrt{2\pi}}\exp{\Big{\{}-\frac{\log^{2}(s\_{1})+o\big{(}\log(s\_{1})\big{)}}{\sigma^{2}\tau}\Big{\}}}, |  |

  which approaches to 00 as s1subscript𝑠1s\_{1} approaches to zero, and approaches to 00 as well as s1subscript𝑠1s\_{1} approaches ∞\infty. Since n𝑛n was arbitrary, then all of the functions in Condition (1)1(1) are bounded in s1subscript𝑠1s\_{1}. With a similar method involving the common term N′​(d+)s2nsuperscript𝑁′subscript𝑑superscriptsubscript𝑠2𝑛\frac{N^{\prime}(d\_{+})}{s\_{2}^{n}}, we can also show that all of the terms in Condition (1)1(1) are bounded in s2subscript𝑠2s\_{2}. We can ultimately conclude that the entire function of Condition (1)1(1) is bounded in (s1,s2)subscript𝑠1subscript𝑠2(s\_{1},s\_{2}).
* •

  Condition (2):

  |  |  |  |
  | --- | --- | --- |
  |  | ‖λs1​(s1​Γ11+s2​Γ11+s2​Γ12)‖<∞.normsubscript𝜆subscript𝑠1subscript𝑠1subscriptΓ11subscript𝑠2subscriptΓ11subscript𝑠2subscriptΓ12\displaystyle\|\lambda\_{s\_{1}}\big{(}s\_{1}\Gamma\_{11}+s\_{2}\Gamma\_{11}+s\_{2}\Gamma\_{12}\big{)}\|<\infty. |  |

  ###### Proof 7.3.

  Same proof as Condition (1).
* •

  Condition (3):

  |  |  |  |
  | --- | --- | --- |
  |  | ‖|1−λ​Γ11|‖>δ0, for some ​δ0>0.formulae-sequencenorm1𝜆subscriptΓ11subscript𝛿0 for some subscript𝛿00\displaystyle|||1-\lambda\Gamma\_{11}|||>\delta\_{0},\text{ for some }\delta\_{0}>0. |  |

  ###### Proof 7.4.

  This condition already holds in the s1,s2
  subscript𝑠1subscript𝑠2s\_{1},s\_{2} dimension. For t𝑡t we have limt→Tλ¯​(t,s1)=0subscript→𝑡𝑇¯𝜆𝑡subscript𝑠10\lim\_{t\to T}\bar{\lambda}(t,s\_{1})=0 and limt→TΓ11​(t)=∞subscript→𝑡𝑇subscriptΓ11𝑡\lim\_{t\to T}\Gamma\_{11}(t)=\infty for at the money options. Since λ¯​(t,s1)¯𝜆𝑡subscript𝑠1\bar{\lambda}(t,s\_{1}) approach to 00 at a greater rate, then limt→Tλ¯​(t,s1)​Γ11​(t)=0.subscript→𝑡𝑇¯𝜆𝑡subscript𝑠1subscriptΓ11𝑡0\lim\_{t\to T}\bar{\lambda}(t,s\_{1})\Gamma\_{11}(t)=0. In fact, this ensures the λ¯​(t,s1)​Γ11​(t)¯𝜆𝑡subscript𝑠1subscriptΓ11𝑡\bar{\lambda}(t,s\_{1})\Gamma\_{11}(t) term stays small, which ultimately guarantees the existence of δ0subscript𝛿0\delta\_{0}. There is a more detailed explanation in Pirvu et al (2014) [[25](#bib.bib25)].
* •

  Condition (4):

  |  |  |  |
  | --- | --- | --- |
  |  | ∥(λ+λs1)(Chm1+Γ11+Γ12+Spd111+Spd112+Spd122+Acc1112\displaystyle\|(\lambda+\lambda\_{s\_{1}})(Chm\_{1}+\Gamma\_{11}+\Gamma\_{12}+Spd\_{111}+Spd\_{112}+Spd\_{122}+Acc\_{1112} |  |
  |  |  |  |
  | --- | --- | --- |
  |  | +Acc1122)∥<∞.\displaystyle+Acc\_{1122})\|<\infty. |  |

  ###### Proof 7.5.

  Same proof as Condition (1).
* •

  Condition (5):

  |  |  |  |
  | --- | --- | --- |
  |  | ‖λ​(C​o​l1+C​o​l2+A​c​c1111+A​c​c1222)+λs1​A​c​c1111+λs2​A​c​c1222‖<∞.norm𝜆𝐶𝑜subscript𝑙1𝐶𝑜subscript𝑙2𝐴𝑐subscript𝑐1111𝐴𝑐subscript𝑐1222subscript𝜆subscript𝑠1𝐴𝑐subscript𝑐1111subscript𝜆subscript𝑠2𝐴𝑐subscript𝑐1222\displaystyle\|\lambda(Col\_{1}+Col\_{2}+Acc\_{1111}+Acc\_{1222})+\lambda\_{s\_{1}}Acc\_{1111}+\lambda\_{s\_{2}}Acc\_{1222}\|<\infty. |  |

  ###### Proof 7.6.

  Same proof as Condition (1).
* •

  Condition (6):

  |  |  |  |
  | --- | --- | --- |
  |  | ∥s1Spd111+s1Spd112+s2Spd112+s2Spd122+s12Acc1112+s12Acc1122\displaystyle\|s\_{1}Spd\_{111}+s\_{1}Spd\_{112}+s\_{2}Spd\_{112}+s\_{2}Spd\_{122}+s\_{1}^{2}Acc\_{1112}+s\_{1}^{2}Acc\_{1122} |  |
  |  |  |  |
  | --- | --- | --- |
  |  | +s1s2Acc1112+s1s2Acc1122+s22Acc1122+s22Acc1222∥<∞.\displaystyle+s\_{1}s\_{2}Acc\_{1112}+s\_{1}s\_{2}Acc\_{1122}+s\_{2}^{2}Acc\_{1122}+s\_{2}^{2}Acc\_{1222}\|<\infty. |  |

  ###### Proof 7.7.

  Same proof as Condition (1).

Since we have shown Condition (1)1(1) to (5)5(5) in the Appendix Section [7.1](#S7.SS1 "7.1 Finite Liquidity Existence and Uniqueness Theorem I ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.") holds for our price impact trading strategy λ​(t,S1​(t))​d​f​(t,S1​(t),S2​(t))𝜆𝑡subscript𝑆1𝑡𝑑𝑓𝑡subscript𝑆1𝑡subscript𝑆2𝑡\lambda\big{(}t,S\_{1}(t)\big{)}df\big{(}t,S\_{1}(t),S\_{2}(t)\big{)}. We can conclude the SDEs S1subscript𝑆1S\_{1} ([3](#S3.Ex7 "3 Analysis of Replication of Exchange Option by Delta Hedging as Price Impact ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")) has a strong solution.

### 7.3 Margrabe’s Pricing Formula and Greeks

Margrabe (1978) [[19](#bib.bib19)] derived the following closed form price for Exchange Option.

|  |  |  |  |
| --- | --- | --- | --- |
| (16) |  | V​(t,s1,s2)=𝔼~​[e−r​τ​(S1​(T)−S2​(T))+|ℱ​(t)]=s1​N​(d+)−s2​N​(d−),𝑉𝑡subscript𝑠1subscript𝑠2~𝔼delimited-[]conditionalsuperscript𝑒𝑟𝜏superscriptsubscript𝑆1𝑇subscript𝑆2𝑇ℱ𝑡subscript𝑠1𝑁subscript𝑑subscript𝑠2𝑁subscript𝑑\displaystyle V(t,s\_{1},s\_{2})=\widetilde{\mathbb{E}}\big{[}e^{-r\tau}\big{(}S\_{1}(T)-S\_{2}(T)\big{)}^{+}|\mathscr{F}(t)\big{]}=s\_{1}N(d\_{+})-s\_{2}N(d\_{-}), |  |
|  |  |  |
| --- | --- | --- |
|  | where ​d±=log⁡(s1s2)±12​σ2​τσ​τ, and ​σ2=σ12+σ22−2​σ1​σ2​ρ.formulae-sequencewhere subscript𝑑plus-or-minusplus-or-minussubscript𝑠1subscript𝑠212superscript𝜎2𝜏𝜎𝜏 and superscript𝜎2superscriptsubscript𝜎12superscriptsubscript𝜎222subscript𝜎1subscript𝜎2𝜌\displaystyle\text{where }d\_{\pm}=\frac{\log(\frac{s\_{1}}{s\_{2}})\pm\frac{1}{2}\sigma^{2}\tau}{\sigma\sqrt{\tau}},\text{ and }\sigma^{2}=\sigma\_{1}^{2}+\sigma\_{2}^{2}-2\sigma\_{1}\sigma\_{2}\rho. |  |

We can derive the Exchange Option Greeks by differentiating formula ([16](#S7.E16 "Equation 16 ‣ 7.3 Margrabe’s Pricing Formula and Greeks ‣ 7 Appendix ‣ Numerical Simulation of Exchange Option with Finite Liquidity: Controlled Variate ModelPreprint. \fundingThis work was funded by NSERC grant 5-36700.")). The first order Greeks are well known, they are available in papers such as Alos and Thorsten (2017) [[3](#bib.bib3)].

|  |  |  |
| --- | --- | --- |
|  | Δ1​(t)=N​(d+)Δ2​(t)=−N​(d−).formulae-sequencesubscriptΔ1𝑡𝑁subscript𝑑subscriptΔ2𝑡𝑁subscript𝑑\displaystyle\Delta\_{1}(t)=N(d\_{+})\qquad\Delta\_{2}(t)=-N(d\_{-}). |  |
|  |  |  |
| --- | --- | --- |
|  | Θ​(t)=σ​s1​N′​(d+)2​τ=−σs2N′(d−).2​τ.\displaystyle\Theta(t)=\frac{\sigma{}s\_{1}N^{\prime}(d\_{+})}{2\sqrt{\tau}}=-\frac{\sigma{}s\_{2}N^{\prime}(d\_{-}).}{2\sqrt{\tau}}. |  |

For the second and higher order Greeks, we will provide derivations.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Γ11​(t)=∂Δ1​(t)∂s1=N′​(d+)​∂d+∂s1=N′​(d+)σ​s1​τ.subscriptΓ11𝑡subscriptΔ1𝑡subscript𝑠1superscript𝑁′subscript𝑑subscript𝑑subscript𝑠1superscript𝑁′subscript𝑑𝜎subscript𝑠1𝜏\displaystyle\Gamma\_{11}(t)=\frac{\partial{\Delta\_{1}(t)}}{\partial{s\_{1}}}=N^{\prime}(d\_{+})\frac{\partial{d\_{+}}}{\partial{s\_{1}}}=\frac{N^{\prime}(d\_{+})}{\sigma s\_{1}\sqrt{\tau}}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Γ22​(t)=∂Δ2​(t)∂s2=−N′​(d−)​∂d−∂s2=N′​(d−)σ​s2​τ.subscriptΓ22𝑡subscriptΔ2𝑡subscript𝑠2superscript𝑁′subscript𝑑subscript𝑑subscript𝑠2superscript𝑁′subscript𝑑𝜎subscript𝑠2𝜏\displaystyle\Gamma\_{22}(t)=\frac{\partial{\Delta\_{2}(t)}}{\partial{s\_{2}}}=-N^{\prime}(d\_{-})\frac{\partial{d\_{-}}}{\partial{s\_{2}}}=\frac{N^{\prime}(d\_{-})}{\sigma s\_{2}\sqrt{\tau}}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Γ12​(t)=Γ21​(t)=∂Δ1​(t)∂s2=N′​(d+)​∂d+∂s2=−1σ​τ​N′​(d+)s2=−1σ​τ​N′​(d−+σ​τ)s2subscriptΓ12𝑡subscriptΓ21𝑡subscriptΔ1𝑡subscript𝑠2superscript𝑁′subscript𝑑subscript𝑑subscript𝑠21𝜎𝜏superscript𝑁′subscript𝑑subscript𝑠21𝜎𝜏superscript𝑁′subscript𝑑𝜎𝜏subscript𝑠2\displaystyle\Gamma\_{12}(t)=\Gamma\_{21}(t)=\frac{\partial{\Delta\_{1}(t)}}{\partial{s\_{2}}}=N^{\prime}(d\_{+})\frac{\partial{d\_{+}}}{\partial{s\_{2}}}=-\frac{1}{\sigma\sqrt{\tau}}\frac{N^{\prime}(d\_{+})}{s\_{2}}=-\frac{1}{\sigma\sqrt{\tau}}\frac{N^{\prime}(d\_{-}+\sigma\sqrt{\tau})}{s\_{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−1σ​τ​1s2​12​π​exp⁡{−12​d−2−d−​σ​τ−12​σ2​τ}absent1𝜎𝜏1subscript𝑠212𝜋12superscriptsubscript𝑑2subscript𝑑𝜎𝜏12superscript𝜎2𝜏\displaystyle\quad=-\frac{1}{\sigma\sqrt{\tau}}\frac{1}{s\_{2}}\frac{1}{\sqrt{2\pi}}\exp\Big{\{}-\frac{1}{2}d\_{-}^{2}-d\_{-}\sigma\sqrt{\tau}-\frac{1}{2}\sigma^{2}\tau\Big{\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−1σ​τ​1s2​12​π​exp⁡{−12​d−2−log⁡(s1s2)}=−N′​(d−)σ​s1​τ.absent1𝜎𝜏1subscript𝑠212𝜋12superscriptsubscript𝑑2subscript𝑠1subscript𝑠2superscript𝑁′subscript𝑑𝜎subscript𝑠1𝜏\displaystyle\quad=-\frac{1}{\sigma\sqrt{\tau}}\frac{1}{s\_{2}}\frac{1}{\sqrt{2\pi}}\exp\Big{\{}-\frac{1}{2}d\_{-}^{2}-\log{\big{(}\frac{s\_{1}}{s\_{2}}\big{)}}\Big{\}}=-\frac{N^{\prime}(d\_{-})}{\sigma s\_{1}\sqrt{\tau}}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | C​h​a​r​m1​(t)=∂Δ1​(t)∂τ=N′​(d+)​∂d+∂τ=N′​(d+)​(−log⁡(s1s2)2​σ​τ32+σ4​τ).𝐶ℎ𝑎𝑟subscript𝑚1𝑡subscriptΔ1𝑡𝜏superscript𝑁′subscript𝑑subscript𝑑𝜏superscript𝑁′subscript𝑑subscript𝑠1subscript𝑠22𝜎superscript𝜏32𝜎4𝜏\displaystyle Charm\_{1}(t)=\frac{\partial{\Delta\_{1}(t)}}{\partial\tau}=N^{\prime}(d\_{+})\frac{\partial{d\_{+}}}{\partial\tau}=N^{\prime}(d\_{+})\Big{(}-\frac{\log\big{(}\frac{s\_{1}}{s\_{2}}\big{)}}{2\sigma\tau^{\frac{3}{2}}}+\frac{\sigma}{4\sqrt{\tau}}\Big{)}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | C​h​a​r​m2​(t)=∂Δ2​(t)∂τ=−N′​(d−)​∂d−∂τ=N′​(d−)​(log⁡(s1s2)2​σ​τ32+σ4​τ).𝐶ℎ𝑎𝑟subscript𝑚2𝑡subscriptΔ2𝑡𝜏superscript𝑁′subscript𝑑subscript𝑑𝜏superscript𝑁′subscript𝑑subscript𝑠1subscript𝑠22𝜎superscript𝜏32𝜎4𝜏\displaystyle Charm\_{2}(t)=\frac{\partial{\Delta\_{2}(t)}}{\partial\tau}=-N^{\prime}(d\_{-})\frac{\partial{d\_{-}}}{\partial\tau}=N^{\prime}(d\_{-})\Big{(}\frac{\log\big{(}\frac{s\_{1}}{s\_{2}}\big{)}}{2\sigma\tau^{\frac{3}{2}}}+\frac{\sigma}{4\sqrt{\tau}}\Big{)}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | S​p​e​e​d111​(t)=∂Γ11​(t)∂s1=1σ​τ​N′′​(d+)​∂d+∂s1−N′​(d+)s12=1σ​τ​−2​d+​N′​(d+)σ​s1​τ−N′​(d+)s12𝑆𝑝𝑒𝑒subscript𝑑111𝑡subscriptΓ11𝑡subscript𝑠11𝜎𝜏superscript𝑁′′subscript𝑑subscript𝑑subscript𝑠1superscript𝑁′subscript𝑑superscriptsubscript𝑠121𝜎𝜏2subscript𝑑superscript𝑁′subscript𝑑𝜎subscript𝑠1𝜏superscript𝑁′subscript𝑑superscriptsubscript𝑠12\displaystyle Speed\_{111}(t)=\frac{\partial{\Gamma\_{11}(t)}}{\partial{s\_{1}}}=\frac{1}{\sigma\sqrt{\tau}}\frac{N^{\prime\prime}(d\_{+})\frac{\partial{d\_{+}}}{\partial{s\_{1}}}-N^{\prime}(d\_{+})}{s\_{1}^{2}}=\frac{1}{\sigma\sqrt{\tau}}\frac{-\frac{2d\_{+}N^{\prime}(d\_{+})}{\sigma{}s\_{1}\sqrt{\tau}}-N^{\prime}(d\_{+})}{s\_{1}^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−Γ11s1​(2​d+σ​s1​τ+1).absentsubscriptΓ11subscript𝑠12subscript𝑑𝜎subscript𝑠1𝜏1\displaystyle\quad=-\frac{\Gamma\_{11}}{s\_{1}}\big{(}\frac{2d\_{+}}{\sigma{}s\_{1}\sqrt{\tau}}+1\big{)}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | S​p​e​e​d222​(t)=∂Γ22​(t)∂s2=1σ​τ​N′′​(d−)​∂d−∂s2−N′​(d−)s22=1σ​τ​−2​d−​N′​(d−)σ​s2​τ−N′​(d−)s22𝑆𝑝𝑒𝑒subscript𝑑222𝑡subscriptΓ22𝑡subscript𝑠21𝜎𝜏superscript𝑁′′subscript𝑑subscript𝑑subscript𝑠2superscript𝑁′subscript𝑑superscriptsubscript𝑠221𝜎𝜏2subscript𝑑superscript𝑁′subscript𝑑𝜎subscript𝑠2𝜏superscript𝑁′subscript𝑑superscriptsubscript𝑠22\displaystyle Speed\_{222}(t)=\frac{\partial{\Gamma\_{22}(t)}}{\partial{s\_{2}}}=\frac{1}{\sigma\sqrt{\tau}}\frac{N^{\prime\prime}(d\_{-})\frac{\partial{d\_{-}}}{\partial{s\_{2}}}-N^{\prime}(d\_{-})}{s\_{2}^{2}}=\frac{1}{\sigma\sqrt{\tau}}\frac{-\frac{2d\_{-}N^{\prime}(d\_{-})}{\sigma{}s\_{2}\sqrt{\tau}}-N^{\prime}(d\_{-})}{s\_{2}^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−Γ22s2​(2​d−σ​s2​τ+1).absentsubscriptΓ22subscript𝑠22subscript𝑑𝜎subscript𝑠2𝜏1\displaystyle\quad=-\frac{\Gamma\_{22}}{s\_{2}}\big{(}\frac{2d\_{-}}{\sigma{}s\_{2}\sqrt{\tau}}+1\big{)}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | S​p​e​e​d112​(t)=∂Γ11​(t)∂s2=1σ​τ​N′′​(d+)​∂d+∂s2s1=−2​d+​N′​(d+)σ2​τ​s1​s2=−2​d+​Γ11σ​s2.𝑆𝑝𝑒𝑒subscript𝑑112𝑡subscriptΓ11𝑡subscript𝑠21𝜎𝜏superscript𝑁′′subscript𝑑subscript𝑑subscript𝑠2subscript𝑠12subscript𝑑superscript𝑁′subscript𝑑superscript𝜎2𝜏subscript𝑠1subscript𝑠22subscript𝑑subscriptΓ11𝜎subscript𝑠2\displaystyle Speed\_{112}(t)=\frac{\partial{\Gamma\_{11}(t)}}{\partial{s\_{2}}}=\frac{1}{\sigma\sqrt{\tau}}\frac{N^{\prime\prime}(d\_{+})\frac{\partial{d\_{+}}}{\partial{s\_{2}}}}{s\_{1}}=-\frac{2d\_{+}N^{\prime}(d\_{+})}{\sigma^{2}\tau s\_{1}s\_{2}}=-\frac{2d\_{+}\Gamma\_{11}}{\sigma s\_{2}}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | S​p​e​e​d221​(t)=∂Γ22​(t)∂s1=1σ​τ​N′′​(d−)​∂d−∂s1s2=−2​d−​N′​(d−)σ2​τ​s1​s2=−2​d−​Γ22σ​s1.𝑆𝑝𝑒𝑒subscript𝑑221𝑡subscriptΓ22𝑡subscript𝑠11𝜎𝜏superscript𝑁′′subscript𝑑subscript𝑑subscript𝑠1subscript𝑠22subscript𝑑superscript𝑁′subscript𝑑superscript𝜎2𝜏subscript𝑠1subscript𝑠22subscript𝑑subscriptΓ22𝜎subscript𝑠1\displaystyle Speed\_{221}(t)=\frac{\partial{\Gamma\_{22}(t)}}{\partial{s\_{1}}}=\frac{1}{\sigma\sqrt{\tau}}\frac{N^{\prime\prime}(d\_{-})\frac{\partial{d\_{-}}}{\partial{s\_{1}}}}{s\_{2}}=-\frac{2d\_{-}N^{\prime}(d\_{-})}{\sigma^{2}\tau s\_{1}s\_{2}}=-\frac{2d\_{-}\Gamma\_{22}}{\sigma s\_{1}}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | C​o​l​o​u​r11​(t)=∂Γ11​(t)∂τ=1σ​s1​(−12​τ32​N′​(d+)−1τ12​N′​(d+)​d+​∂d+∂τ)𝐶𝑜𝑙𝑜𝑢subscript𝑟11𝑡subscriptΓ11𝑡𝜏1𝜎subscript𝑠112superscript𝜏32superscript𝑁′subscript𝑑1superscript𝜏12superscript𝑁′subscript𝑑subscript𝑑subscript𝑑𝜏\displaystyle Colour\_{11}(t)=\frac{\partial{\Gamma\_{11}(t)}}{\partial\tau}=\frac{1}{\sigma{}s\_{1}}\Big{(}-\frac{1}{2\tau^{\frac{3}{2}}}N^{\prime}(d\_{+})-\frac{1}{\tau^{\frac{1}{2}}}N^{\prime}(d\_{+})d\_{+}\frac{\partial{d\_{+}}}{\partial\tau}\Big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =N′​(d+)2​σ​τ32​s1​{−1+d+​(log⁡(s1s2)​1σ​τ−12​σ​τ)}absentsuperscript𝑁′subscript𝑑2𝜎superscript𝜏32subscript𝑠11subscript𝑑subscript𝑠1subscript𝑠21𝜎𝜏12𝜎𝜏\displaystyle\quad=\frac{N^{\prime}(d\_{+})}{2\sigma\tau^{\frac{3}{2}}s\_{1}}\Big{\{}-1+d\_{+}\Big{(}\log(\frac{s\_{1}}{s\_{2}})\frac{1}{\sigma\sqrt{\tau}}-\frac{1}{2}\sigma\sqrt{\tau}\Big{)}\Big{\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−Γ1123​σ2​τ2​(σ4​τ2+4​σ2​τ−4​log2⁡(s1s2)),absentsubscriptΓ11superscript23superscript𝜎2superscript𝜏2superscript𝜎4superscript𝜏24superscript𝜎2𝜏4superscript2subscript𝑠1subscript𝑠2\displaystyle\quad=-\frac{\Gamma\_{11}}{2^{3}\sigma^{2}\tau^{2}}\Big{(}\sigma^{4}\tau^{2}+4\sigma^{2}\tau-4\log^{2}(\frac{s\_{1}}{s\_{2}})\Big{)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | C​o​l​o​u​r22​(t)=∂Γ22​(t)∂τ=1σ​s2​(−12​τ32​N′​(d−)−1τ12​N′​(d−)​d+​∂d−∂τ)𝐶𝑜𝑙𝑜𝑢subscript𝑟22𝑡subscriptΓ22𝑡𝜏1𝜎subscript𝑠212superscript𝜏32superscript𝑁′subscript𝑑1superscript𝜏12superscript𝑁′subscript𝑑subscript𝑑subscript𝑑𝜏\displaystyle Colour\_{22}(t)=\frac{\partial{\Gamma\_{22}(t)}}{\partial\tau}=\frac{1}{\sigma{}s\_{2}}\Big{(}-\frac{1}{2\tau^{\frac{3}{2}}}N^{\prime}(d\_{-})-\frac{1}{\tau^{\frac{1}{2}}}N^{\prime}(d\_{-})d\_{+}\frac{\partial{d\_{-}}}{\partial\tau}\Big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−Γ2223​σ2​τ2​(σ4​τ2+4​σ2​τ−4​log2⁡(s1s2)),absentsubscriptΓ22superscript23superscript𝜎2superscript𝜏2superscript𝜎4superscript𝜏24superscript𝜎2𝜏4superscript2subscript𝑠1subscript𝑠2\displaystyle\quad=-\frac{\Gamma\_{22}}{2^{3}\sigma^{2}\tau^{2}}\Big{(}\sigma^{4}\tau^{2}+4\sigma^{2}\tau-4\log^{2}(\frac{s\_{1}}{s\_{2}})\Big{)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | C​o​l​o​u​r12​(t)=C​o​l​o​u​r21​(t)=∂Γ12​(t)∂τ=1σ​s2​(12​τ32​N′​(d+)+1τ12​N′​(d+)​d+​∂d+∂τ)𝐶𝑜𝑙𝑜𝑢subscript𝑟12𝑡𝐶𝑜𝑙𝑜𝑢subscript𝑟21𝑡subscriptΓ12𝑡𝜏1𝜎subscript𝑠212superscript𝜏32superscript𝑁′subscript𝑑1superscript𝜏12superscript𝑁′subscript𝑑subscript𝑑subscript𝑑𝜏\displaystyle Colour\_{12}(t)=Colour\_{21}(t)=\frac{\partial{\Gamma\_{12}(t)}}{\partial\tau}=\frac{1}{\sigma{}s\_{2}}\Big{(}\frac{1}{2\tau^{\frac{3}{2}}}N^{\prime}(d\_{+})+\frac{1}{\tau^{\frac{1}{2}}}N^{\prime}(d\_{+})d\_{+}\frac{\partial{d\_{+}}}{\partial\tau}\Big{)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−Γ1223​σ2​τ2​(σ4​τ2+4​σ2​τ−4​log2⁡(s1s2))=−Γ2123​σ2​τ2​(σ4​τ2+4​σ2​τ−4​log2⁡(s1s2)).absentsubscriptΓ12superscript23superscript𝜎2superscript𝜏2superscript𝜎4superscript𝜏24superscript𝜎2𝜏4superscript2subscript𝑠1subscript𝑠2subscriptΓ21superscript23superscript𝜎2superscript𝜏2superscript𝜎4superscript𝜏24superscript𝜎2𝜏4superscript2subscript𝑠1subscript𝑠2\displaystyle\quad=\frac{-\Gamma\_{12}}{2^{3}\sigma^{2}\tau^{2}}\Big{(}\sigma^{4}\tau^{2}+4\sigma^{2}\tau-4\log^{2}(\frac{s\_{1}}{s\_{2}})\Big{)}=\frac{-\Gamma\_{21}}{2^{3}\sigma^{2}\tau^{2}}\Big{(}\sigma^{4}\tau^{2}+4\sigma^{2}\tau-4\log^{2}(\frac{s\_{1}}{s\_{2}})\Big{)}. |  |

|  |  |  |
| --- | --- | --- |
|  | A​c​c​e​l​e​r​a​t​i​o​n1111​(t)𝐴𝑐𝑐𝑒𝑙𝑒𝑟𝑎𝑡𝑖𝑜subscript𝑛1111𝑡\displaystyle Acceleration\_{1111}(t) |  |
|  |  |  |
| --- | --- | --- |
|  | =∂S​p​e​e​d111​(t)∂s1=−((∂∂s1​Γ11s1)​(2​d+σ​s1​τ+1)+Γ11s1​2σ​τ​(∂∂s1​d+s1))absent𝑆𝑝𝑒𝑒subscript𝑑111𝑡subscript𝑠1subscript𝑠1subscriptΓ11subscript𝑠12subscript𝑑𝜎subscript𝑠1𝜏1subscriptΓ11subscript𝑠12𝜎𝜏subscript𝑠1subscript𝑑subscript𝑠1\displaystyle\quad=\frac{\partial{Speed\_{111}(t)}}{\partial{s\_{1}}}=-\Big{(}\big{(}\frac{\partial}{\partial{s\_{1}}}{\frac{\Gamma\_{11}}{s\_{1}}}\big{)}\big{(}\frac{2d\_{+}}{\sigma{}s\_{1}\sqrt{\tau}}+1\big{)}+\frac{\Gamma\_{11}}{s\_{1}}\frac{2}{\sigma\sqrt{\tau}}\big{(}\frac{\partial}{\partial{s\_{1}}}\frac{d\_{+}}{s\_{1}}\big{)}\Big{)} |  |
|  |  |  |
| --- | --- | --- |
|  | =−(S​p​e​e​d111​s1−Γ11s12​(2​d+σ​s1​τ+1)+Γ11s1​2σ​τ​(1σ​τ−d+s12))absent𝑆𝑝𝑒𝑒subscript𝑑111subscript𝑠1subscriptΓ11superscriptsubscript𝑠122subscript𝑑𝜎subscript𝑠1𝜏1subscriptΓ11subscript𝑠12𝜎𝜏1𝜎𝜏subscript𝑑superscriptsubscript𝑠12\displaystyle\quad=-\Big{(}\frac{Speed\_{111}s\_{1}-\Gamma\_{11}}{s\_{1}^{2}}\big{(}\frac{2d\_{+}}{\sigma{}s\_{1}\sqrt{\tau}}+1\big{)}+\frac{\Gamma\_{11}}{s\_{1}}\frac{2}{\sigma\sqrt{\tau}}\big{(}\frac{\frac{1}{\sigma\sqrt{\tau}}-d\_{+}}{s\_{1}^{2}}\big{)}\Big{)} |  |
|  |  |  |
| --- | --- | --- |
|  | =−2​Γ11σ​τ​s13​(d+​(2​d+σ​τ​s1+1)+(1σ​τ−d+))absent2subscriptΓ11𝜎𝜏superscriptsubscript𝑠13subscript𝑑2subscript𝑑𝜎𝜏subscript𝑠111𝜎𝜏subscript𝑑\displaystyle\quad=-\frac{2\Gamma\_{11}}{\sigma\sqrt{\tau}s\_{1}^{3}}\Big{(}d\_{+}\big{(}\frac{2d\_{+}}{\sigma{}\sqrt{\tau}s\_{1}}+1\big{)}+\big{(}\frac{1}{\sigma\sqrt{\tau}}-d\_{+}\big{)}\Big{)} |  |
|  |  |  |
| --- | --- | --- |
|  | =−2​Γ11σ2​s13​τ​(2​d+2s1+1),absent2subscriptΓ11superscript𝜎2superscriptsubscript𝑠13𝜏2superscriptsubscript𝑑2subscript𝑠11\displaystyle\quad=-\frac{2\Gamma\_{11}}{\sigma^{2}s\_{1}^{3}\tau}\big{(}\frac{2d\_{+}^{2}}{s\_{1}}+1\big{)}, |  |
|  |  |  |
| --- | --- | --- |
|  | A​c​c​e​l​e​r​a​t​i​o​n1112​(t)𝐴𝑐𝑐𝑒𝑙𝑒𝑟𝑎𝑡𝑖𝑜subscript𝑛1112𝑡\displaystyle Acceleration\_{1112}(t) |  |
|  |  |  |
| --- | --- | --- |
|  | =∂S​p​e​e​d111​(t)∂s2=−(1s1​(∂∂s2​Γ11)​(2​d+σ​s1​τ+1)+Γ11s1​2σ​τ​s1​(∂∂s2​d+))absent𝑆𝑝𝑒𝑒subscript𝑑111𝑡subscript𝑠21subscript𝑠1subscript𝑠2subscriptΓ112subscript𝑑𝜎subscript𝑠1𝜏1subscriptΓ11subscript𝑠12𝜎𝜏subscript𝑠1subscript𝑠2subscript𝑑\displaystyle\quad=\frac{\partial{Speed\_{111}(t)}}{\partial{s\_{2}}}=-\Big{(}\frac{1}{s\_{1}}\big{(}\frac{\partial}{\partial{s\_{2}}}\Gamma\_{11}\big{)}\big{(}\frac{2d\_{+}}{\sigma{}s\_{1}\sqrt{\tau}}+1\big{)}+\frac{\Gamma\_{11}}{s\_{1}}\frac{2}{\sigma\sqrt{\tau}s\_{1}}\big{(}\frac{\partial}{\partial{s\_{2}}}d\_{+}\big{)}\Big{)} |  |
|  |  |  |
| --- | --- | --- |
|  | =−(S​p​e​e​d112s1​(2​d+σ​τ​s1+1)−Γ11s1​2σ​τ​s1​1σ​τ​s2)absent𝑆𝑝𝑒𝑒subscript𝑑112subscript𝑠12subscript𝑑𝜎𝜏subscript𝑠11subscriptΓ11subscript𝑠12𝜎𝜏subscript𝑠11𝜎𝜏subscript𝑠2\displaystyle\quad=-\Big{(}\frac{Speed\_{112}}{s\_{1}}\big{(}\frac{2d\_{+}}{\sigma{}\sqrt{\tau}s\_{1}}+1\big{)}-\frac{\Gamma\_{11}}{s\_{1}}\frac{2}{\sigma\sqrt{\tau}s\_{1}}\frac{1}{\sigma\sqrt{\tau}s\_{2}}\Big{)} |  |
|  |  |  |
| --- | --- | --- |
|  | =2​Γ11σ​s1​s2​τ​(2​d+2σ​τ+d++1σ​s1​τ),absent2subscriptΓ11𝜎subscript𝑠1subscript𝑠2𝜏2superscriptsubscript𝑑2𝜎𝜏subscript𝑑1𝜎subscript𝑠1𝜏\displaystyle\quad=\frac{2\Gamma\_{11}}{\sigma s\_{1}s\_{2}\sqrt{\tau}}\big{(}\frac{2d\_{+}^{2}}{\sigma\sqrt{\tau}}+d\_{+}+\frac{1}{\sigma s\_{1}\sqrt{\tau}}\big{)}, |  |
|  |  |  |
| --- | --- | --- |
|  | A​c​c​e​l​e​r​a​t​i​o​n1122​(t)𝐴𝑐𝑐𝑒𝑙𝑒𝑟𝑎𝑡𝑖𝑜subscript𝑛1122𝑡\displaystyle Acceleration\_{1122}(t) |  |
|  |  |  |
| --- | --- | --- |
|  | =∂S​p​e​e​d112​(t)∂s2=2σ​τ​s1​(∂∂s2​d+)​Γ12+d+​(∂∂s2​Γ12)absent𝑆𝑝𝑒𝑒subscript𝑑112𝑡subscript𝑠22𝜎𝜏subscript𝑠1subscript𝑠2subscript𝑑subscriptΓ12subscript𝑑subscript𝑠2subscriptΓ12\displaystyle\quad=\frac{\partial{Speed\_{112}(t)}}{\partial{s\_{2}}}=\frac{2}{\sigma\sqrt{\tau}s\_{1}}\big{(}\frac{\partial}{\partial{s\_{2}}}d\_{+}\big{)}\Gamma\_{12}+d\_{+}\big{(}\frac{\partial}{\partial{s\_{2}}}\Gamma\_{12}\big{)} |  |
|  |  |  |
| --- | --- | --- |
|  | =2​Γ12σ2​s1​s2​τ​(d+​d−−1),absent2subscriptΓ12superscript𝜎2subscript𝑠1subscript𝑠2𝜏subscript𝑑subscript𝑑1\displaystyle\quad=\frac{2\Gamma\_{12}}{\sigma^{2}s\_{1}s\_{2}\tau}\big{(}d\_{+}d\_{-}-1\big{)}, |  |
|  |  |  |
| --- | --- | --- |
|  | A​c​c​e​l​e​r​a​t​i​o​n1222​(t)𝐴𝑐𝑐𝑒𝑙𝑒𝑟𝑎𝑡𝑖𝑜subscript𝑛1222𝑡\displaystyle Acceleration\_{1222}(t) |  |
|  |  |  |
| --- | --- | --- |
|  | =∂S​p​e​e​d222​(t)∂s1=−(1s2​(∂∂s1​Γ22)​(2​d−σ​s2​τ+1)+Γ22s2​2σ​τ​s2​(∂∂s1​d−))absent𝑆𝑝𝑒𝑒subscript𝑑222𝑡subscript𝑠11subscript𝑠2subscript𝑠1subscriptΓ222subscript𝑑𝜎subscript𝑠2𝜏1subscriptΓ22subscript𝑠22𝜎𝜏subscript𝑠2subscript𝑠1subscript𝑑\displaystyle\quad=\frac{\partial{Speed\_{222}(t)}}{\partial{s\_{1}}}=-\Big{(}\frac{1}{s\_{2}}\big{(}\frac{\partial}{\partial{s\_{1}}}\Gamma\_{22}\big{)}\big{(}\frac{2d\_{-}}{\sigma{}s\_{2}\sqrt{\tau}}+1\big{)}+\frac{\Gamma\_{22}}{s\_{2}}\frac{2}{\sigma\sqrt{\tau}s\_{2}}\big{(}\frac{\partial}{\partial{s\_{1}}}d\_{-}\big{)}\Big{)} |  |
|  |  |  |
| --- | --- | --- |
|  | =−(S​p​e​e​d122s2​(2​d−σ​τ​s2+1)+Γ22s2​2σ​τ​s2​1σ​τ​s1)absent𝑆𝑝𝑒𝑒subscript𝑑122subscript𝑠22subscript𝑑𝜎𝜏subscript𝑠21subscriptΓ22subscript𝑠22𝜎𝜏subscript𝑠21𝜎𝜏subscript𝑠1\displaystyle\quad=-\Big{(}\frac{Speed\_{122}}{s\_{2}}\big{(}\frac{2d\_{-}}{\sigma{}\sqrt{\tau}s\_{2}}+1\big{)}+\frac{\Gamma\_{22}}{s\_{2}}\frac{2}{\sigma\sqrt{\tau}s\_{2}}\frac{1}{\sigma\sqrt{\tau}s\_{1}}\Big{)} |  |
|  |  |  |
| --- | --- | --- |
|  | =2​Γ22σ​s1​s2​τ​(2​d−2σ​s2​τ+d−−1σ​s2​τ),absent2subscriptΓ22𝜎subscript𝑠1subscript𝑠2𝜏2superscriptsubscript𝑑2𝜎subscript𝑠2𝜏subscript𝑑1𝜎subscript𝑠2𝜏\displaystyle\quad=\frac{2\Gamma\_{22}}{\sigma s\_{1}s\_{2}\sqrt{\tau}}\big{(}\frac{2d\_{-}^{2}}{\sigma s\_{2}\sqrt{\tau}}+d\_{-}-\frac{1}{\sigma s\_{2}\sqrt{\tau}}\big{)}, |  |

|  |  |  |
| --- | --- | --- |
|  | A​c​c​e​l​e​r​a​t​i​o​n2222​(t)𝐴𝑐𝑐𝑒𝑙𝑒𝑟𝑎𝑡𝑖𝑜subscript𝑛2222𝑡\displaystyle Acceleration\_{2222}(t) |  |
|  |  |  |
| --- | --- | --- |
|  | =∂S​p​e​e​d222​(t)∂s2=−((∂∂s2​Γ22s2)​(2​d−σ​s2​τ+1)+Γ22s2​2σ​τ​(∂∂s2​d−s2))absent𝑆𝑝𝑒𝑒subscript𝑑222𝑡subscript𝑠2subscript𝑠2subscriptΓ22subscript𝑠22subscript𝑑𝜎subscript𝑠2𝜏1subscriptΓ22subscript𝑠22𝜎𝜏subscript𝑠2subscript𝑑subscript𝑠2\displaystyle\quad=\frac{\partial{Speed\_{222}(t)}}{\partial{s\_{2}}}=-\Big{(}\big{(}\frac{\partial}{\partial{s\_{2}}}\frac{\Gamma\_{22}}{s\_{2}}\big{)}\big{(}\frac{2d\_{-}}{\sigma{}s\_{2}\sqrt{\tau}}+1\big{)}+\frac{\Gamma\_{22}}{s\_{2}}\frac{2}{\sigma\sqrt{\tau}}\big{(}\frac{\partial}{\partial{s\_{2}}}\frac{d\_{-}}{s\_{2}}\big{)}\Big{)} |  |
|  |  |  |
| --- | --- | --- |
|  | =−2​Γ22σ2​s23​τ​(2​d−2s2+1).absent2subscriptΓ22superscript𝜎2superscriptsubscript𝑠23𝜏2superscriptsubscript𝑑2subscript𝑠21\displaystyle\quad=-\frac{2\Gamma\_{22}}{\sigma^{2}s\_{2}^{3}\tau}\big{(}\frac{2d\_{-}^{2}}{s\_{2}}+1\big{)}. |  |

## Acknowledgments

The authors are grateful to the anonymous referee for a careful checking of the details and for helpful comments that improved this paper.

## References

* [1]

  D. Ahmadian, O. F. Rouz, K. Ivaz, and A. Safdari-Vaighani, Robust
  numerical algorithm to the european option with illiquid markets, Applied
  Mathematics and Computation, 366 (2020), p. 124693,
  <http://www.sciencedirect.com/science/article/pii/S009630031930685X>.
* [2]

  E. Alòs and M. Coulon, On the optimal choice of strike conventions
  in exchange option pricing, EconPapers, (2018),
  <https://arxiv.org/abs/1807.05396>.
* [3]

  E. Alòs and T. Rheinländer, Pricing and hedging margrabe options
  with stochastic volatilities, EconPapers, (2017),
  <https://EconPapers.repec.org/RePEc:upf:upfgen:1475>.
* [4]

  A. J. Arenas, G. Gonzalez-Parra, and B. M. Caraballo, A nonstandard
  finite difference scheme for a nonlinear black-scholes equation,
  Mathematical and Computer Modelling, 57 (2013), pp. 1663 – 1670,
  <http://www.sciencedirect.com/science/article/pii/S0895717711006947>.
* [5]

  R. Culkin and S. R. Das, Machine learning in finance: The case of
  deep learning for option pricing, Journal of Investment Management, (2017).
* [6]

  M. Dyshaev and V. Fedorov, The sensitivities (greeks) for some
  models of option pricing with market illiquidity, Mathematical notes of
  NEFU, 26 (2019), <https://doi.org/10.25587/SVFU.2019.102.31514>.
* [7]

  R. Ferguson and A. D. Green, Applying deep learning to derivatives
  valuation, SSRN Electronic Journal, (2018),
  <http://dx.doi.org/10.2139/ssrn.3244821>.
* [8]

  A. Friedman, Stochastic Differential Equations and Applications,
  Academic Press, 1st edition ed., 1975.
* [9]

  M. Giles and P. Glasserman, Smoking adjoints: fast evaluation of
  greeks in monte carlo calculations, Risk Journals, (2005).
* [10]

  M. B. Giles and L. Szpruch, Multilevel monte carlo methods for
  applications in finance, High-Performance Computing in Finance, (2018),
  pp. 197–247, <https://arxiv.org/pdf/1212.1377.pdf>.
* [11]

  P. Glasserman, Monte Carlo methods in financial engineering,
  Springer, 2004.
* [12]

  K. J. Glover, P. W. Duck, and D. P. Newton, On nonlinear models of
  markets with finite liquidity: Some cautionary notes, SIAM Journal on
  Applied Mathematics, 70 (2010), pp. 3252–3271,
  <https://doi.org/10.1137/080736119>.
* [13]

  D. Hainaut, Calendar spread exchange options pricing with gaussian
  random fields, Risks, 6 (2018), p. 77,
  <https://doi.org/10.3390/risks6030077>.
* [14]

  D. J. Higham, An introduction to multilevel monte carlo for option
  valuation, International Journal of Computer Mathematics, 92 (2015),
  pp. 2347–2360, <https://doi.org/10.1080/00207160.2015.1077236>.
* [15]

  K. Hornik, M. Stinchcombe, and H. White, Multilayer feedforward
  networks are universal approximators, Neural Networks, 2 (1989), pp. 359 –
  366, <http://www.sciencedirect.com/science/article/pii/0893608089900208>.
* [16]

  I. Itô, On the existence and uniqueness of solutions of
  stochastic integral equations of the volterra type, Kodai Math, 2 (1979),
  pp. 158–170, <https://doi.org/https://doi.org/10.2996/kmj/1138036013>.
* [17]

  D. Kingma and J. Ba, Adam: A method for stochastic optimization,
  International Conference on Learning Representations, (2014).
* [18]

  H. Liu and J. Yong, Option pricing with an illiquid underlying asset
  market, Journal of Economic Dynamics & Control, 29 (2005), pp. 2125–2156,
  <https://doi.org/http://apps.olin.wustl.edu/faculty/liuh/Papers/Liu_Yong.pd>.
* [19]

  W. Margrabe, The value of an option to exchange one asset for
  another, Journal of Finance, 33 (1978), pp. 177–186,
  <https://doi.org/https://doi.org/10.2307/2326358>.
* [20]

  G. N. Mil’shtein, Approximate integration of stochastic
  differential equations, Theory of Probability & Its Applications., 19
  (1975), pp. 557–000, <https://doi.org/https://doi.org/10.1137/1119062>.
* [21]

  B. Oksendal, Stochastic Differential Equations (3rd Ed.): An
  Introduction with Applications, Springer-Verlag, Berlin, Heidelberg, 1992.
* [22]

  T. Pirvu and A. Yazdanian, Numerical analysis for spread option
  pricing model in illiquid underlying asset market: Full feedback model,
  Applied Mathematics & Information Sciences, 10 (2015), pp. 1271–1281,
  <https://doi.org/10.18576/amis/100406>.
* [23]

  R. Y. Rubinstein and R. Marcus, Efficiency of multivariate control
  variates in monte carlo simulation, Operations Research, 33 (1985),
  pp. 661–677, <https://doi.org/10.1287/opre.33.3.661>,
  <https://doi.org/10.1287/opre.33.3.661>.
* [24]

  K. Scheicher, Complexity and effective dimension of discrete lévy
  areas, Journal of Complexity, 23 (2007), pp. 152–168,
  <https://doi.org/doi:10.1016/j.jco.2006.12.006>.
* [25]

  A. Shidfar, K. Paryab, A. Yazdanian, and T. A. Pirvu, Numerical
  analysis for spread option pricing model of markets with finite liquidity:
  first-order feedback model, International Journal of Computer Mathematics,
  91 (2014), pp. 2603–2620,
  <https://doi.org/https://doi.org/10.1080/00207160.2014.887274>.
* [26]

  S. E. Shreve, Stochastic calculus for finance II, Continuous-time
  models, Springer, New York, NY; Heidelberg, 2004.
* [27]

  S. ul Islam and I. Ahmad, A comparative analysis of local meshless
  formulation for multi-asset option models, Engineering Analysis with
  Boundary Elements, 65 (2016), pp. 159 – 176,
  <http://www.sciencedirect.com/science/article/pii/S0955799716000175>.
* [28]

  P. Wilmott and P. J. Schönbucher, The feedback effect of hedging in
  illiquid markets, SIAM Journal on Applied Mathematics, 61 (2000),
  pp. 232–272, <https://doi.org/10.1137/S0036139996308534>.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2006.07771)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2006.07771)
[View original  
on arXiv](https://arxiv.org/abs/2006.07771)[►](javascript: void(0))