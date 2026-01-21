---
authors:
- Alexander Barzykin
doc_id: arxiv:2601.13421v1
family_id: arxiv:2601.13421
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Market Making and Transient Impact in Spot FX
url_abs: http://arxiv.org/abs/2601.13421v1
url_html: https://arxiv.org/html/2601.13421v1
venue: arXiv q-fin
version: 1
year: 2026
---


Alexander Barzykin
Email: alexander.barzykin@hsbc.com

(January 17, 2026)

###### Abstract

Dealers in foreign exchange markets provide bid and ask prices to their clients at which they are happy to buy and sell, respectively. To manage risk, dealers can skew their quotes and hedge in the interbank market. Hedging offers certainty but comes with transaction costs and market impact. Optimal market making with execution has previously been addressed within the Almgren-Chriss market impact model, which includes instantaneous and permanent components. However, there is overwhelming empirical evidence of the transient nature of market impact, with instantaneous and permanent impacts arising as the two limiting cases. In this note, we consider an intermediate scenario and study the interplay between risk management and impact resilience.

Keywords: Market Making; Stochastic Optimal Control; Market Impact; Algorithmic Trading.

## 1 Introduction

Foreign exchange (FX) markets continue to operate largely on an OTC (over-the-counter) basis where dealers offer bid and ask prices to their clients bilaterally or via aggregators.
The dealer aims to make a spread but must manage inventory risk arising from the asynchronicity between client flow and market volatility.
To attract risk-reducing flows, the dealer can skew their quotes, but may ultimately hedge excess inventory in the interbank market.
Hedging offers certainty but comes with transaction costs and market impact.
Optimal strategies balancing spread capture and risk management have been a subject of recent active research (Avellaneda and Stoikov, [2008](https://arxiv.org/html/2601.13421v1#bib.bib2); Guéant et al., [2013](https://arxiv.org/html/2601.13421v1#bib.bib15); Cartea et al., [2014](https://arxiv.org/html/2601.13421v1#bib.bib10); Butz and Oomen, [2019](https://arxiv.org/html/2601.13421v1#bib.bib9); Bergault and Guéant, [2021](https://arxiv.org/html/2601.13421v1#bib.bib6); Barzykin et al., [2023](https://arxiv.org/html/2601.13421v1#bib.bib3), [2025](https://arxiv.org/html/2601.13421v1#bib.bib4)).
In particular, the internalization versus externalization dilemma has been in focus (Butz and Oomen, [2019](https://arxiv.org/html/2601.13421v1#bib.bib9)), and the Almgren-Chriss ([2001](https://arxiv.org/html/2601.13421v1#bib.bib1)) model with instantaneous cost and linear permanent impact has been employed to describe execution in the interbank market (Barzykin et al., [2023](https://arxiv.org/html/2601.13421v1#bib.bib3)).
One of the conclusions of this research is the existence of a pure internalization zone where it is not optimal for the dealer to execute.
The inventory threshold, beyond which the dealer will begin to execute, depends on risk aversion, volatility, client flow, and, importantly, transaction costs and market impact.
There is overwhelming empirical evidence for the transient nature of market impact, with the propagator model of Bouchaud et al. ([2018](https://arxiv.org/html/2601.13421v1#bib.bib7)) capturing its essence.
A particular case of exponential relaxation in the Obizhaeva-Wang model ([2013](https://arxiv.org/html/2601.13421v1#bib.bib19)) is accompanied by a clear explanation in terms of the limit order book’s resilience.
At the same time, large order execution demonstrates a universal square root dependence on the total executed quantity (Tóth et al., [2011](https://arxiv.org/html/2601.13421v1#bib.bib21); Sato and Kanazawa, [2025](https://arxiv.org/html/2601.13421v1#bib.bib20)).
Both effects are found to be very important in optimal execution (Neuman and Voß, [2022](https://arxiv.org/html/2601.13421v1#bib.bib18); Hey et al., [2023](https://arxiv.org/html/2601.13421v1#bib.bib17); Webster, [2023](https://arxiv.org/html/2601.13421v1#bib.bib22)).
So, why Almgren-Chriss?

First of all, the square root law is a meta feature that arises for relatively large parent orders due to latent liquidity (Bucci et al., [2019](https://arxiv.org/html/2601.13421v1#bib.bib8)) and/or sophisticated traders able to take advantage of the market over-reaction to the metaorder (Durin et al., [2023](https://arxiv.org/html/2601.13421v1#bib.bib12)).
For smaller sizes/participation rates, the impact is found to be linear (Bucci et al., [2019](https://arxiv.org/html/2601.13421v1#bib.bib8); Durin et al., [2023](https://arxiv.org/html/2601.13421v1#bib.bib12)).
The primary route for dealers’ risk reduction is internalization, so the linearity of hedging impact is a natural assumption, ensuring no dynamic arbitrage (Gatheral, [2010](https://arxiv.org/html/2601.13421v1#bib.bib14)).
Secondly, the impact, albeit transient, is known to be highly persistent (Bouchaud et al., [2018](https://arxiv.org/html/2601.13421v1#bib.bib7)), whereas the typical timescale for risk relaxation for FX dealers is short (Butz and Oomen, [2019](https://arxiv.org/html/2601.13421v1#bib.bib9)).
Thus, the assumption of permanent impact (on the timescale of risk relaxation) is also plausible.
However, one can reasonably conjecture that at least part of the impact decay should be comparable to the risk decay, as execution trades can end up in other market makers’ inventory,
and the interplay between the impact resilience and risk management can become important.

We begin by demonstrating that OTC trading implies a propagator-type impact, as in Obizhaeva and Wang ([2013](https://arxiv.org/html/2601.13421v1#bib.bib19)) and echoing the findings of Eisler and Bouchaud ([2016](https://arxiv.org/html/2601.13421v1#bib.bib13)) in a different market.
Then we introduce the resilient impact state into the market-making model and solve the corresponding Hamilton-Jacobi-Bellman (HJB) equation to find optimal controls both numerically and analytically within a quadratic approximation à la Bergault et al. ([2021](https://arxiv.org/html/2601.13421v1#bib.bib5)).
Using parameters relevant to institutional FX, we find a clear performance benefit when risk-managing large inventories and accounting for resilient impact.

## 2 Transient Impact of Client Trades with the Dealer

Let us demonstrate that the market-making model itself implies a transient impact, namely, as soon as the client trades with the market maker, the price jumps and then relaxes back to its initial value.
We consider a standard Avellaneda-Stoikov ([2008](https://arxiv.org/html/2601.13421v1#bib.bib2)) OTC market-making model with Bergault-Guéant ([2021](https://arxiv.org/html/2601.13421v1#bib.bib6)) extension to a ladder of sizes.
The dealer offers bid/ask prices Stn,b/a=St∓δtn,b/a\displaystyle S\_{t}^{n,b/a}=S\_{t}\mp\delta\_{t}^{n,b/a} for a set of trade sizes Δn\displaystyle\Delta^{n} (0<Δ1<…<ΔN\displaystyle 0<\Delta^{1}<\ldots<\Delta^{N}, N≥1\displaystyle N\geq 1) to clients.
Here, the mid-price St\displaystyle S\_{t} is modeled as a Brownian motion, and deltas are dealer’s controls to optimize risk-adjusted P&L over a finite time horizon T\displaystyle T (Cartea et al., [2014](https://arxiv.org/html/2601.13421v1#bib.bib10)).
We consider Poisson trade arrivals with side-symmetric intensity λn,b/a​(δ)=λn​(δ)\displaystyle\lambda^{n,b/a}(\delta)=\lambda^{n}(\delta).
This formulation is standard, and the corresponding baseline HJB equation for the value function V​(t,q)\displaystyle V(t,q) at time t\displaystyle t and inventory q\displaystyle q reads (Guéant et al., [2013](https://arxiv.org/html/2601.13421v1#bib.bib15); Cartea et al., [2015](https://arxiv.org/html/2601.13421v1#bib.bib11); Guéant, [2016](https://arxiv.org/html/2601.13421v1#bib.bib16))

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=∂tV−γ​σ2​q22+∑nΔn​(HOTCn​[Dq+n​V​(t,q)]+HOTCn​[Dq−n​V​(t,q)])0=\partial\_{t}V-\frac{\gamma\sigma^{2}q^{2}}{2}+\sum\_{n}\Delta^{n}\Bigg(H^{n}\_{\text{\tiny{OTC}}}\left[D\_{q+}^{n}V(t,q)\right]+H^{n}\_{\text{\tiny{OTC}}}\left[D\_{q-}^{n}V(t,q)\right]\Bigg) |  | (1) |

with t∈[0,T]\displaystyle t\in[0,T] and appropriate terminal condition
111Terminal penalty does not alter optimal controls at time 0 when T\displaystyle T is sufficiently large,
so one can assume V​(T,q)=0\displaystyle V(T,q)=0.
at t=T\displaystyle t=T, where σ\displaystyle\sigma denotes volatility, γ\displaystyle\gamma the risk aversion coefficient and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dq±n​V​(t,q)=V​(t,q)−V​(t,q±Δn)ΔnD\_{q\pm}^{n}V(t,q)=\frac{V(t,q)-V(t,q\pm\Delta^{n})}{\Delta^{n}} |  | (2) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | HOTCn​(p)=supδ∈ℝλn​(δ)​(δ−p)H^{n}\_{\text{\tiny{OTC}}}(p)=\sup\_{\delta\in\mathbb{R}}\lambda^{n}(\delta)(\delta-p) |  | (3) |

Following Bergault et al. ([2021](https://arxiv.org/html/2601.13421v1#bib.bib5)), we seek an approximate solution via second-order Hamiltonian expansion and quadratic ansatz for the value function,
leading to Riccati ODE.
Thus, we write
222Linear term disappears due to symmetry.
V​(t,q)=−A​(t)​q2−C​(t)\displaystyle V(t,q)=-A(t)q^{2}-C(t) and obtain a stationary solution:
333C​(t)\displaystyle C(t) does not influence the controls and thus is not shown.

|  |  |  |  |
| --- | --- | --- | --- |
|  | A0=limT→∞A​(0)=σ​γ8​ξ,ξ=∑nHOTCn′′​(0)​ΔnA\_{0}=\lim\_{T\to\infty}A(0)=\sigma\sqrt{\frac{\gamma}{8\xi}},\qquad\xi=\sum\_{n}H^{n^{\prime\prime}}\_{\text{\tiny{OTC}}}(0)\Delta^{n} |  | (4) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | HOTCn′′​(0)=λn​(δ0n)δ0n​cn,cn=2−λn​(δ0n)​λn′′​(δ0n)(λn′​(δ0n))2H^{n^{\prime\prime}}\_{\text{\tiny{OTC}}}(0)=\frac{\lambda^{n}(\delta^{n}\_{0})}{\delta^{n}\_{0}c^{n}},\qquad c^{n}=2-\frac{\lambda^{n}(\delta^{n}\_{0})\lambda^{n^{\prime\prime}}(\delta^{n}\_{0})}{(\lambda^{n^{\prime}}(\delta^{n}\_{0}))^{2}} |  | (5) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ0n=argmaxδ∈ℝ​δ​λn​(δ).\delta^{n}\_{0}=\underset{\delta\in\mathbb{R}}{\text{argmax}}\,\delta\lambda^{n}(\delta). |  | (6) |

Optimal quotes are, therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ∗n,b/a≃δ0n+A0cn​(Δn±2​q)\delta\_{\*}^{n,b/a}\simeq\delta^{n}\_{0}+\frac{A\_{0}}{c^{n}}\left(\Delta^{n}\pm 2q\right) |  | (7) |

where ±\displaystyle\pm corresponds to b/a\displaystyle b/a, respectively.
This approximate solution is well-known, even though it may not have appeared explicitly in the early literature.
It provides a valid expansion in the limit of low risk aversion and can serve as a starting point for policy iteration – an efficient method for solving HJB numerically.

We can immediately see an instantaneous impact signature in optimal quotes.
The equilibrium cost (half-spread) for size Δn\displaystyle\Delta^{n} is δ0n+A0​Δn/cn\displaystyle\delta^{n}\_{0}+A\_{0}\Delta^{n}/c^{n}, but as soon as one trades, the mid-price jumps by 2​A0​Δn/cn\displaystyle 2A\_{0}\Delta^{n}/c^{n}, ensuring no-arbitrage.444The weighted average price of executing two consecutive Δn\displaystyle\Delta^{n} orders should equal the price of a single 2​Δn\displaystyle 2\Delta^{n} order.
Under stationary control, the ODE for the mean-field inventory q¯t=𝔼​[qt]\displaystyle\bar{q}\_{t}=\mathbb{E}[q\_{t}] reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | q¯˙t=∑nΔn​(λn​(δ∗n,b​(q¯t))−λn​(δ∗n,a​(q¯t)))≃−ω​q¯t\dot{\bar{q}}\_{t}=\sum\_{n}\Delta^{n}\Big(\lambda^{n}\big(\delta^{n,b}\_{\*}(\bar{q}\_{t})\big)-\lambda^{n}\big(\delta^{n,a}\_{\*}(\bar{q}\_{t})\big)\Big)\simeq-\omega\bar{q}\_{t} |  | (8) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ω=σ​2​γ​ξ\omega=\sigma\sqrt{2\gamma\xi} |  | (9) |

which is exponential relaxation. After an inventory shock of magnitude q0\displaystyle q\_{0}, the dealer’s position relaxes as q¯t=q0​exp⁡(−ω​t)\displaystyle\bar{q}\_{t}=q\_{0}\exp(-\omega t), and so does optimal pricing.
This is essentially an OTC equivalent of the Obizhaeva-Wang ([2013](https://arxiv.org/html/2601.13421v1#bib.bib19)) model.
While this is understandably an internal transient impact on a particular dealer’s pricing, skewing is known to potentially influence the external market as well via price reading (Barzykin et al., [2025](https://arxiv.org/html/2601.13421v1#bib.bib4)), not to mention the direct market impact of the external hedging activity.

## 3 Hedging with Transient Impact

Let us now return to the market maker’s optimization problem.
In addition to skewing, the dealer can trade in the interbank market to hedge their risk.
As in Barzykin et al. ([2023](https://arxiv.org/html/2601.13421v1#bib.bib3)), it is assumed that hedging is continuous with speed vt\displaystyle v\_{t} and transaction cost L​(v)=ψ​|v|+η​v2\displaystyle L(v)=\psi|v|+\eta v^{2}.
Hedging also causes market impact that decays exponentially over time, as in Obizhaeva-Wang ([2013](https://arxiv.org/html/2601.13421v1#bib.bib19)).
Thus, we write for the mid-price evolution

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=σ​d​Wt+d​xt,d​xt=(−β​xt+k​vt)​d​tdS\_{t}=\sigma dW\_{t}+dx\_{t},\qquad dx\_{t}=(-\beta x\_{t}+kv\_{t})dt |  | (10) |

where xt\displaystyle x\_{t} denotes the resilient impact state.
Clearly, β=0\displaystyle\beta=0 brings us back to Almgren-Chriss ([2001](https://arxiv.org/html/2601.13421v1#bib.bib1)).
The corresponding HJB for the value function V​(t,q,x)\displaystyle V(t,q,x) reads (after standard substitution to eliminate price diffusion):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=∂tV−β​x​(q+∂xV)−12​γ​σ2​q2+HE​(pE)+∑nΔn​(HOTCn​[Dq+n​V]+HOTCn​[Dq−n​V])0=\partial\_{t}V-\beta x(q+\partial\_{x}V)-\frac{1}{2}\gamma\sigma^{2}q^{2}+H\_{\text{\tiny{E}}}(p\_{\text{\tiny{E}}})+\sum\_{n}\Delta^{n}\Bigg(H^{n}\_{\text{\tiny{OTC}}}\left[D\_{q+}^{n}V\right]+H^{n}\_{\text{\tiny{OTC}}}\left[D\_{q-}^{n}V\right]\Bigg) |  | (11) |

with zero terminal condition and

|  |  |  |  |
| --- | --- | --- | --- |
|  | HE​(p)=supv∈ℝp​v−L​(v)=(|p|−ψ)+24​η,\displaystyle\displaystyle H\_{\text{\tiny{E}}}(p)=\sup\_{v\in\mathbb{R}}pv-L(v)=\frac{(|p|-\psi)^{2}\_{+}}{4\eta}, |  | (12) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | pE=k​(q+∂xV)+∂qV\displaystyle\displaystyle p\_{\text{\tiny{E}}}=k(q+\partial\_{x}V)+\partial\_{q}V |  | (13) |

The terms −β​x​(q+∂xV)\displaystyle-\beta x(q+\partial\_{x}V) come from the controlled drift in S\displaystyle S and the state drift of x\displaystyle x.
The optimal quotes are given by (using the envelope theorem)

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ∗n,b/a=(λn)−1​(−HOTCn′​[Dq±n​V​(t,q,x)])\delta\_{\*}^{n,b/a}=(\lambda^{n})^{-1}\left(-H^{n^{\prime}}\_{\text{\tiny{OTC}}}\left[D\_{q\pm}^{n}V(t,q,x)\right]\right) |  | (14) |

and the optimal execution speed is

|  |  |  |  |
| --- | --- | --- | --- |
|  | v∗={sign​(pE)​|pE|−ψ2​η,if |pE|>ψ.0,otherwise.v\_{\*}=\begin{cases}\mathrm{sign}(p\_{\text{\tiny{E}}})\frac{|p\_{\text{\tiny{E}}}|-\psi}{2\eta},&\text{if $\displaystyle|p\_{\text{\tiny{E}}}|>\psi$}.\\ 0,&\text{otherwise}.\end{cases} |  | (15) |

For qualitative insight let us again follow Bergault et al. ([2021](https://arxiv.org/html/2601.13421v1#bib.bib5)) and approximate HOTCn​(p)\displaystyle H^{n}\_{\text{\tiny{OTC}}}(p) up to the second order in p\displaystyle p
and then use the quadratic ansatz for the value function
555Linear terms vanish due to symmetry, and the x2\displaystyle x^{2} term is small.

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,q,x)=−A​(t)​q2−B​(t)​q​x−C​(t)V(t,q,x)=-A(t)q^{2}-B(t)qx-C(t) |  | (16) |

The execution Hamiltonian HE​(p)\displaystyle H\_{\text{\tiny{E}}}(p) is neglected when approximating the value function due to the spread cost.666One can neglect the spread and keep the quadratic cost as an alternative approximation, but the difference is insignificant.
HJB thus reduces to the Riccati system for the coefficients and
the stationary solution is given by
777The free term does not influence the controls and thus is not shown.

|  |  |  |  |
| --- | --- | --- | --- |
|  | B0=limT→∞B​(0)=ββ+ωB\_{0}=\lim\_{T\to\infty}B(0)=\frac{\beta}{\beta+\omega} |  | (17) |

  

with A0\displaystyle A\_{0} being the same as defined earlier in Eq. ([4](https://arxiv.org/html/2601.13421v1#S2.E4 "In 2 Transient Impact of Client Trades with the Dealer ‣ Market Making and Transient Impact in Spot FX")).
B0\displaystyle B\_{0} directly reflects the competition between impact resilience and risk relaxation via client flow.
Optimal quotes can be obtained from Eq. [14](https://arxiv.org/html/2601.13421v1#S3.E14 "In 3 Hedging with Transient Impact ‣ Market Making and Transient Impact in Spot FX").
Keeping only the first significant correction, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ∗n,b/a​(q,x)≃δ0n+A0cn​(Δn±2​q)±B0cn​x\delta\_{\*}^{n,b/a}(q,x)\simeq\delta^{n}\_{0}+\frac{A\_{0}}{c^{n}}(\Delta^{n}\pm 2q)\pm\frac{B\_{0}}{c^{n}}x |  | (18) |

with additional linear dependence on the impact state.
Optimal execution speed is driven by the value of pE\displaystyle p\_{\text{\tiny{E}}} which is
now given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | pE​(q,x)=−(2​A0−k​(1−B0))​q−B0​xp\_{\text{\tiny{E}}}(q,x)=-\big(2A\_{0}-k(1-B\_{0})\big)q-B\_{0}x |  | (19) |

|pE​(q,x)|=ψ\displaystyle|p\_{\text{\tiny{E}}}(q,x)|=\psi defines the boundary of the pure internalization zone.

![Refer to caption](x1.png)


Figure 1: 
Optimal top of book (TOB) ask quote δ∗1,a\displaystyle\delta^{1,a}\_{\*} and execution speed v∗\displaystyle v\_{\*} as functions of inventory q\displaystyle q and impact state x\displaystyle x for a set of parameters defined in the text.
The dashed line corresponds to the approximate solution for x=0\displaystyle x=0.

## 4 Numerical Examples

As an illustration, consider a standard size ladder of Δn=(1,2,5,10,20,50)\displaystyle\Delta^{n}=(1,2,5,10,20,50) M notional and a sigmoid intensity function λn​(δ)=λ0n​(1+exp⁡(an+bn​δ))−1\displaystyle\lambda^{n}(\delta)=\lambda^{n}\_{0}\big(1+\exp(a^{n}+b^{n}\delta)\big)^{-1}
with amplitudes λ0n=(2000,800,600,400,100,50)\displaystyle\lambda\_{0}^{n}=(2000,800,600,400,100,50) day-1 and uniform parameters an=−1\displaystyle a^{n}=-1, bn=7\displaystyle b^{n}=7 bp-1.
Here, bp stands for basis points.888This implies GBM while we deal here with simple Brownian motion.
The difference is negligible in FX market making due to short trading horizons.
This set of parameters corresponds to a liquid currency pair with a daily turnover of ≃5\displaystyle\simeq 5 billion notional and a top-of-book spread of ≃0.5\displaystyle\simeq 0.5 bp.
We also assume a daily volatility of 100\displaystyle 100 bp and a risk aversion coefficient of γ=10−3\displaystyle\gamma=10^{-3} bp-1 M-1.
Execution related parameters are ψ=0.2\displaystyle\psi=0.2 bp, η=1.5\displaystyle\eta=1.5 bp⋅\displaystyle\cdots/M, k=0.005\displaystyle k=0.005 bp/M and β=1000\displaystyle\beta=1000 day-1.
The impact decay rate was intentionally chosen to be comparable to the risk relaxation time (ω≃560\displaystyle\omega\simeq 560 day-1 in this case).

![Refer to caption](x2.png)


Figure 2: 
2d plot of optimal execution speed v∗\displaystyle v\_{\*} as a function of inventory q\displaystyle q and impact state x\displaystyle x for a set of parameters defined in the text.

Figure [1](https://arxiv.org/html/2601.13421v1#S3.F1 "Figure 1 ‣ 3 Hedging with Transient Impact ‣ Market Making and Transient Impact in Spot FX") illustrates the optimal controls δ∗1,a\displaystyle\delta^{1,a}\_{\*} and v∗\displaystyle v\_{\*} as functions of the dealer’s inventory q\displaystyle q and the impact state x\displaystyle x (colour coded).
The solution was obtained by numerically solving the HJB equation using the explicit Euler scheme (taking sub-second in JAX).
The overall shape resembles the optimal solution with Almgren-Chriss impact (Barzykin et al., [2023](https://arxiv.org/html/2601.13421v1#bib.bib3)), but the dependence on the impact state is significant.
In particular, the pure internalization zone depends on the impact state, as shown in Figure [2](https://arxiv.org/html/2601.13421v1#S4.F2 "Figure 2 ‣ 4 Numerical Examples ‣ Market Making and Transient Impact in Spot FX"), which is understandable because impact relaxation is a form of price prediction.
Moreover, an approximate closed-form solution, obtained by substituting the quadratic expansion of the value function into Eqs. ([14](https://arxiv.org/html/2601.13421v1#S3.E14 "In 3 Hedging with Transient Impact ‣ Market Making and Transient Impact in Spot FX")) and ([15](https://arxiv.org/html/2601.13421v1#S3.E15 "In 3 Hedging with Transient Impact ‣ Market Making and Transient Impact in Spot FX")), is found to capture the optimal solution qualitatively but deviates for larger inventories, as expected.

![Refer to caption](x3.png)


Figure 3: 
P&L, position, execution speed and impact state dynamics following an inventory shock of q0=50\displaystyle q\_{0}=50 M for a parameter set defined in the text.
The results were obtained via Monte Carlo simulation with 104\displaystyle 10^{4} trajectories.
Dashed lines correspond to the model optimized with Almgren-Chriss impact.

Figure [3](https://arxiv.org/html/2601.13421v1#S4.F3 "Figure 3 ‣ 4 Numerical Examples ‣ Market Making and Transient Impact in Spot FX") shows how P&L, position, execution speed, and impact state evolve following an inventory shock (large client trade).
The results were obtained via Monte Carlo simulations with 104\displaystyle 10^{4} trajectories using the corresponding SDE and optimal controls (numerically exact).
As expected, we can see the inventory decreasing due to skewing and hedging, with the absolute execution speed decreasing in tandem, while the absolute impact reaches a maximum.
P&L jumps at time zero as the dealer makes a half spread, then decreases due to impact, but then rises again due to continuing flow monetization.
We compare the performance of optimal controls with transient impact to those with permanent impact (i.e., HJB is solved with β=0\displaystyle\beta=0), even though the underlying impact is transient in both cases.
The benefit of incorporating impact resilience is very clear in this case.
However, if large trades are rare, the majority of client flow will be internalized, so that the impact state will rarely be sufficiently large to cause a significant difference to the total expected P&L.
Therefore, the Almgren-Chriss model can be a reasonable approximation after all.
Nevertheless, risk management of larger trades is usually under scrutiny by the desk, and this is where considering impact resilience becomes important.

## Acknowledgment

The author would like to express his sincere gratitude to Olivier Guéant (Université Paris Cité) for fruitful discussions and valuable comments and to Richard Anthony (HSBC) for support throughout the project.
The views expressed are those of the author and do not necessarily reflect the views or practices at HSBC.

## References

* Almgren and Chriss (2001)

  Almgren, R. and Chriss, N.,
  Optimal execution of portfolio transactions.
  J. Risk, 2001, 3, 5–40.
* Avellaneda and Stoikov (2008)

  Avellaneda, M. and Stoikov, S.,
  High-frequency trading in a limit order book.
  Quant. Finance, 2008, 8, 217–224.
* Barzykin et al. (2023)

  Barzykin, A., Bergault, P. and Guéant, O.,
  Algorithmic market making in dealer markets with hedging and market impact.
  Math. Finance, 2023, 33, 41–79.
* Barzykin et al. (2025)

  Barzykin, A., Bergault, P., Guéant, O. and Lemmel, M.,
  Optimal Quoting under Adverse Selection and Price Reading, 2025.
  Available online at: https://arxiv.org/abs/2508.20225 (accessed 19 December 2025).
* Bergault et al. (2021)

  Bergault, P., Evangelista, D., Guéant, O. and Vieira, D.,
  Closed-form approximations in multi-asset market making.
  Appl. Math. Finance, 2021, 28, 101–142.
* Bergault and Guéant (2021)

  Bergault, P. and Guéant, O.,
  Size matters for otc market makers: general results and dimensionality reduction techniques.
  Math. Finance, 2021, 31, 279–322.
* Bouchaud et al. (2018)

  Bouchaud, J.-P., Bonart, J., Donier, J. and Gould, M.,
  Trades, Quotes and Prices: Financial Markets Under the Microscope, 2018
  (Cambridge University Press: Cambridge, United Kingdom).
* Bucci et al. (2019)

  Bucci, F., Benzaquen, M., Lillo, F. and Bouchaud, J.-P.,
  Crossover from Linear to Square-Root Market Impact.
  Phys. Rev. Lett., 2019, 122, 108302.
* Butz and Oomen (2019)

  Butz, M. and Oomen, R.,
  Internalisation by electronic fx spot dealers.
  Quant. Finance, 2019, 19, 35–56.
* Cartea et al. (2014)

  Cartea, Á, Jaimungal, S. and Ricci, J.,
  Buy low, sell high: A high frequency trading perspective.
  SIAM J. Financ. Math., 2014, 5, 415–444.
* Cartea et al. (2015)

  Cartea, Á, Jamingual, S. and Penalva, J.,
  Algorithmic and High Frequency Trading, 2015
  (Cambridge University Press: Cambridge, United Kingdom).
* Durin et al. (2023)

  Durin, B., Rosenbaum, M. and Szymansk, G.,
  The two square root laws of market impact and the role of sophisticated market participants, 2023.
  Available online at: https://arxiv.org/abs/2311.18283 (accessed 19 December 2025).
* Eisler and Bouchaud (2016)

  Eisler, Z. and Bouchaud, J.-P.,
  Price impact without order book: A study of the OTC credit index market, 2016.
  Available online at: https://arxiv.org/abs/1609.04620 (accessed 19 December 2025).
* Gatheral (2010)

  Gatheral, J.,
  No-Dynamic-Arbitrage and Market Impact.
  Quant. Finance, 2010, 10, 749–759.
* Guéant et al. (2013)

  Guéant, O., Lehalle, C.-A. and Fernandez-Tapia, J.,
  Dealing with the inventory risk: a solution to the market making problem.
  Math. Financ. Econ., 2013, 7, 477–507.
* Guéant (2016)

  Guéant, O.,
  The Financial Mathematics of Market Liquidity: From optimal execution to market making, 2016
  (Chapman and Hall/CRC: Boca Raton, FL).
* Hey et al. (2023)

  Hey, N., Bouchaud, J.-P., Mastromatteo, I., Muhle-Karbe, J. and Webster, K.,
  The cost of misspecifying price impact, 2023.
  Available online at: https://arxiv.org/abs/2306.00599 (accessed 19 December 2025).
* Neuman and Voß (2022)

  Neuman, E. and Voß, M.,
  Optimal Signal-Adaptive Trading with Temporary and Transient Price Impact.
  SIAM J. Financ. Math., 2022, 13, 551–575.
* Obizhaeva and Wang (2013)

  Obizhaeva, A.A. and Wang, J.,
  Optimal trading strategy and supply/demand dynamics.
  J. Financ. Mark., 2013, 16, 1–32.
* Sato and Kanazawa (2025)

  Sato, Y. and Kanazawa, K.,
  Strict universality of the square-root law in price impact across stocks: A complete survey of the Tokyo stock exchange.
  Phys. Rev. Lett., 2025, 135, 257401.
* Tóth et al. (2011)

  Tóth, B., Lempérière, Y., Deremble, C., De Lataillade, J., Kockelkoren, J. and Bouchaud, J.-P.,
  Anomalous price impact and the critical nature of liquidity in financial markets.
  Phys. Rev. X, 2011, 1, 021006.
* Webster (2023)

  Webster, K.
  Handbook of Price Impact Modeling, 2023
  (Chapman and Hall/CRC: Boca Raton, FL).