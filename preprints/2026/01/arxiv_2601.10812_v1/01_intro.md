---
authors:
- Ryan Donnelly
- Junhan Lin
- Matthew Lorig
doc_id: arxiv:2601.10812v1
family_id: arxiv:2601.10812
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal Liquidation of Perpetual Contracts
url_abs: http://arxiv.org/abs/2601.10812v1
url_html: https://arxiv.org/html/2601.10812v1
venue: arXiv q-fin
version: 1
year: 2026
---


Ryan Donnelly
[ryan.f.donnelly@kcl.ac.uk](mailto:ryan.f.donnelly@kcl.ac.uk)

Junhan Lin
[junhan.1.lin@kcl.ac.uk](mailto:junhan.1.lin@kcl.ac.uk)

Matthew Lorig
[mlorig@uw.edu](mailto:mlorig@uw.edu)
King’s College London, United Kingdom
King’s College London, United Kingdom
University of Washington, Seattle, WA

###### Abstract

An agent holds a position in a perpetual contract with payoff function ψ\psi and attempts to liquidate the position while managing transaction costs, inventory risk, and funding rate payments. By solving the agent’s stochastic control problem we obtain a closed-form expression for the optimal trading strategy when the payoff function is given by ψ​(s)=s\psi(s)=s. When the payoff function is non-linear we provide approximations to the optimal strategy which apply when the funding rate parameter is small or when the length of the trading interval is small. We further prove that when ψ\psi is non-linear, the short time approximation can be written in terms of the closed-form trading strategy corresponding to the case of the ideneity payoff function.

###### keywords:

algorithmic trading, price impact, perpetual contract

††journal: TBA

## 1 Introduction

In this paper we investigate how an agent optimally liquidates a position in a perpetual contract before some fixed maturity date. The challenge facing the agent is to determine the optimal trading strategy whilst her trades are subject to market impact, risk associated with price changes of the inventory she is holding, and the cashflow payments which are made between parties that have a non-zero position in the perpetual contract.

Our model captures two distinct components to market impact: temporary price impact, which refers to the immediate effect on the transaction price as a trade consumes liquidity and penetrates through the available orders in the limit order book (LOB), and permanent price impact, which constitutes a long lasting persistent shift in the asset’s mid-price that subsequently affects the transaction prices of all future trades. Previous research on LOB structures and market impact can be found in for example Eisler
et al. ([2012](https://arxiv.org/html/2601.10812v1#bib.bib11)), Cont
et al. ([2014](https://arxiv.org/html/2601.10812v1#bib.bib9)), and Xu
et al. ([2018](https://arxiv.org/html/2601.10812v1#bib.bib18)). Our research bridges the literature on perpetual contracts with that of the optimal execution problem. Liquidation of large inventory with market impacts has developed from the early models of Bertsimas and
Lo ([1998](https://arxiv.org/html/2601.10812v1#bib.bib5)) and Almgren and
Chriss ([2001](https://arxiv.org/html/2601.10812v1#bib.bib2)) to more recent contributions such as Cartea and
Jaimungal ([2016](https://arxiv.org/html/2601.10812v1#bib.bib7)), Horst
et al. ([2022](https://arxiv.org/html/2601.10812v1#bib.bib15)), and Fouque
et al. ([2022](https://arxiv.org/html/2601.10812v1#bib.bib13)).

A perpetual contract (sometimes referred to as a perpetual future or perpetual swap) is a financial derivative that gives exposure to an underlying asset without owning the asset itself. This exposure occurs through the exchange of cash flows over time between the long and short positions. The magnitude and direction of this cash flow, called the funding rate, depends on the price of the underlying asset and the price of the perpetual contract itself. Perpetual contracts are traded extremely actively in cryptocurrency markets, with daily turnovers measured in the billions of USD, so transaction costs and market impact are economically significant. Hence, optimal trading of perpetual contracts is crucial for agents who seek to liquidate their large positions. Trading decisions must balance immediate market impact costs, long-lasting price impact, ongoing funding payments, inventory risk control as well as a terminal liquidation penalty.

Previous work which studies perpetual contracts has largely been related to pricing and hedging. In Angeris
et al. ([2023](https://arxiv.org/html/2601.10812v1#bib.bib3)), model-free expressions for the funding rate together with replication strategies are derived. In Ackerer
et al. ([2025](https://arxiv.org/html/2601.10812v1#bib.bib1)) the authors derive no-arbitrage pricing formulas for several types of perpetual contracts including linear, inverse, and quanto contracts. Along similar lines, He
et al. ([2022](https://arxiv.org/html/2601.10812v1#bib.bib14)) and Dai
et al. ([2025](https://arxiv.org/html/2601.10812v1#bib.bib10)) introduce no-arbitrage bounds for perpetual contract prices, the former including the effects of transaction costs and the latter further incorporating the popular clamping function on the funding mechanism. Most of the existing research regarding perpetual contracts focuses on pricing and hedging with little work having been conducted in the context of optimal liquidation.

In this work we divide the analysis into two sections, one in which the funding rate depends linearly on the spot price, and one where the exposure is an arbitrary function.111A perpetual contract with non-linear dependence of the funding rate is often called an everlasting option, see Bankman-Fried and
White ([2021](https://arxiv.org/html/2601.10812v1#bib.bib4)). When the funding rate is a linear function of spot, we classify the agent’s value function in terms of the solution to a system of ordinary differential equations (ODEs) (Proposition [1](https://arxiv.org/html/2601.10812v1#Thmtheorem1 "Proposition 1 (Value Function for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) and solve for the optimal trading strategy in closed form (Theorem [2](https://arxiv.org/html/2601.10812v1#Thmtheorem2 "Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")). The explicit form of the solution allows us to see directly how the trading strategy depends on remaining inventory and the current funding rate. When the payoff function is non-linear we derive multiple trading strategies which are asymptotically optimal with respect to certain model parameters. The first applies when the funding rate parameter is small
and we observe that this approximation arises from a perturbation of the Almgren–Chriss optimal strategy (Theorem [6](https://arxiv.org/html/2601.10812v1#Thmtheorem6 "Theorem 6 (Asymptotic Approximation of Optimal Trading Speed) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")). The next two approximations (Theorem [8](https://arxiv.org/html/2601.10812v1#Thmtheorem8 "Theorem 8 (Asymptotic Approximation of Optimal Trading Speed) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") and Theorem [9](https://arxiv.org/html/2601.10812v1#Thmtheorem9 "Proposition 9 (Closed-form Approximation of Optimal Trading Speed) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) apply when the time horizon is short, and we demonstrate the effectiveness of these strategies compared to the Almgren-Chriss strategy for different payoff functions.

The remainder of the paper is structured as follows. In Section 2 we propose a trading model for the perpetual contract and formulate an optimal stochastic control problem faced by the agent. In Section 3 we obtain an optimal trading strategy in closed form when the payoff function is the identity function and conduct some analysis of the optimal strategy. In Section 4 we consider an arbitrary payoff function and compute various approximations to the optimal strategy when the funding rate parameter or the length of trading interval are small. We also compare the performances of different approximations which applicable for short maturity through simulations. Section 5 concludes, and longer proofs are deferred to the appendix.

## 2 Model

### 2.1 Dynamics

In this section we outline the dynamics of the assets involved in the trading problem which will include price impact effects. Additionally we describe the dynamics of the inventory and cash processes of the agent. Let T>0T>0 be finite and represent the length of the trading horizon so that all processes are defined on [0,T][0,T]. We denote by S=(St)t∈[0,T]S=(S\_{t})\_{t\in[0,T]} the value of the underlying spot price which will determine the funding rate of the perpetual contract. We denote by Pν=(Ptν)t∈[0,T]P^{\nu}=(P^{\nu}\_{t})\_{t\in[0,T]} the (controlled) midprice of the perpetual contract which can be directly traded by the agent and which is subject to price impact effects of trading. We let Qν=(Qtν)t∈[0,T]Q^{\nu}=(Q^{\nu}\_{t})\_{t\in[0,T]} denote the (controlled) inventory that the agent holds in the perpetual contract, and the control ν=(νt)t∈[0,T]\nu=(\nu\_{t})\_{t\in[0,T]} represents the rate at which the agent trades (positive and negative values of νt\nu\_{t} represent buying and selling of the perpetual contract, respectively). The dynamics of the controlled inventory are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Qtν\displaystyle Q^{\nu}\_{t} | =Q0+∫0tνu​𝑑u,\displaystyle=Q\_{0}+\int\_{0}^{t}\nu\_{u}\,du\,, |  | (1) |

for some given initial inventory Q0∈ℝQ\_{0}\in\mathbb{R}. The spot and perpetual prices are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | St\displaystyle S\_{t} | =S0+∫0tσ​𝑑WuS,\displaystyle=S\_{0}+\int\_{0}^{t}\sigma\,dW^{S}\_{u}\,, |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ptν\displaystyle P^{\nu}\_{t} | =P0+∫0tb​νu​𝑑u+∫0tη​𝑑WuP,\displaystyle=P\_{0}+\int\_{0}^{t}b\,\nu\_{u}\,du+\int\_{0}^{t}\eta\,dW^{P}\_{u}\,, |  | (3) |

for given initial prices S0,P0∈ℝS\_{0},P\_{0}\in\mathbb{R}, where WS=(WtS)t∈[0,T]W^{S}=(W^{S}\_{t})\_{t\in[0,T]} and WP=(WtP)t∈[0,T]W^{P}=(W^{P}\_{t})\_{t\in[0,T]} are Brownian motions with constant correlation ρ∈(−1,1)\rho\in(-1,1). The term b​νub\,\nu\_{u} with b≥0b\geq 0 constant represents a permanent price impact effect due to the agent’s trading of the perpetual contract. These trades will also incur a temporary price impact which is modeled by setting the transaction price process of trades equal to P^ν=(P^tν)t∈[0,T]\widehat{P}^{\nu}=(\widehat{P}^{\nu}\_{t})\_{t\in[0,T]} which is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P^tν\displaystyle\widehat{P}^{\nu}\_{t} | =Ptν+k​νt,\displaystyle=P^{\nu}\_{t}+k\,\nu\_{t}\,, |  | (4) |

for k>0k>0 a constant. This transaction price represents the price that the agent pays (receives) per unit of the perpetual contract when buying (selling) at rate νt\nu\_{t}. Trading at a faster rate means the agent engages in transactions at less favourable prices compared to a slower rate. Further discussion of permanent and temporary price impact can be found in Cartea
et al. ([2015](https://arxiv.org/html/2601.10812v1#bib.bib8)).

The cash holdings of the agent are affected by the agent’s own trades as well as the funding rate. We assume that the funding rate, equal to β​(Ptν−ψ​(St))\beta\,(P^{\nu}\_{t}-\psi(S\_{t})), is paid continuously by the long side of the contract to the short side, where β>0\beta>0 is a constant and ψ:ℝ→ℝ\psi:\mathbb{R}\rightarrow\mathbb{R}, referred to as the payoff function, is continuous.222The most common payoff function is the identity. When the payoff function is non-linear the perpetual contract is sometimes referred to as an everlasting option, see Bankman-Fried and
White ([2021](https://arxiv.org/html/2601.10812v1#bib.bib4)) and Ackerer
et al. ([2025](https://arxiv.org/html/2601.10812v1#bib.bib1)). We denote the agent’s cash process by Xν=(Xtν)t∈[0,T]X^{\nu}=(X^{\nu}\_{t})\_{t\in[0,T]} and set it equal to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xtν\displaystyle X^{\nu}\_{t} | =X0−∫0tP^uν​νu+β​Quν​(Puν−ψ​(Su))​d​u,\displaystyle=X\_{0}-\int\_{0}^{t}\widehat{P}^{\nu}\_{u}\,\nu\_{u}+\beta\,Q^{\nu}\_{u}\,(P^{\nu}\_{u}-\psi(S\_{u}))\,du\,, |  | (5) |

for a given initial cash value X0∈ℝX\_{0}\in\mathbb{R}. In many perpetual contracts, the funding rate is further modified by a clamping function so that the associated cash flows never exceeds some value in either the positive or negative direction. We do not consider this added complexity for tractability reasons.

Throughout this work we employ the complete filtered probability space (Ω,ℙ,(ℱt)t∈[0,T])(\Omega,\mathbb{P},(\mathcal{F}\_{t})\_{t\in[0,T]}) where (ℱt)t∈[0,T](\mathcal{F}\_{t})\_{t\in[0,T]} is the standard augmentation of the natural filtration generated by (WS,WP)(W^{S},W^{P}).

### 2.2 Performance Criterion

The agent wishes to maximize the expected value of her terminal wealth subject to an inventory risk control and liquidation penalty. When trading according to the strategy ν\nu, her performance is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Hν​(t,x,q,p,s)\displaystyle H^{\nu}(t,x,q,p,s) | =𝔼t,x,q,p,s​[XTν+QTν​(PTν−α​QTν)−ϕ​∫tT(Quν)2​𝑑u],\displaystyle=\mathbb{E}\_{t,x,q,p,s}\biggl[X\_{T}^{\nu}+Q\_{T}^{\nu}\,(P\_{T}^{\nu}-\alpha\,Q\_{T}^{\nu})-\phi\int\_{t}^{T}(Q^{\nu}\_{u})^{2}\,du\biggr]\,, |  | (6) |

where 𝔼t,x,q,p,s​[⋅]\mathbb{E}\_{t,x,q,p,s}\left[\cdot\right] represents expectation conditional on Xtν=xX^{\nu}\_{t}=x, Qtν=qQ^{\nu}\_{t}=q, Ptν=pP^{\nu}\_{t}=p and St=sS\_{t}=s. The term XTνX\_{T}^{\nu} is the value in her cash account at time TT and QTν​PTνQ\_{T}^{\nu}\,P\_{T}^{\nu} is the mark to market value of her remaining inventory. The term α​(QTν)2\alpha\,(Q\_{T}^{\nu})^{2} with α>0\alpha>0 constant represents a penalty of having to liquidate her remaining inventory. Finally, ϕ≥0\phi\geq 0 acts as a risk control term which penalizes holding large amounts of inventory for long periods of time.

The agent’s value function is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H​(t,x,q,p,s)\displaystyle H(t,x,q,p,s) | =supν∈𝒜Hν​(t,x,q,p,s),\displaystyle=\sup\_{\nu\in\mathcal{A}}H^{\nu}(t,x,q,p,s)\,, |  | (7) |

where the set of admissible trading strategies is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒜\displaystyle\mathcal{A} | ={ν:ν​ is ​(ℱt)t∈[0,T]​-adapted and ​𝔼​[∫0Tνt2​𝑑t]<∞}.\displaystyle=\biggl\{\nu:\nu\mbox{ is }(\mathcal{F}\_{t})\_{t\in[0,T]}\mbox{-adapted and }\mathbb{E}\biggl[\int\_{0}^{T}\nu\_{t}^{2}\,dt\biggr]<\infty\biggr\}\,. |  | (8) |

The control problem posed in ([7](https://arxiv.org/html/2601.10812v1#S2.E7 "In 2.2 Performance Criterion ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts")) has the associated Hamilton-Jacobi-Bellman (HJB) partial differential equation (PDE):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tH+supν{ℒν​H}−ϕ​q2=0,H​(T,x,q,p,s)=x+q​(p−α​q),\displaystyle\partial\_{t}H+\sup\_{\nu}\left\{\mathcal{L}^{\nu}H\right\}-\phi\,q^{2}=0\,,\qquad H\left(T,x,q,p,s\right)=x+q\,\left(p-\alpha\,q\right)\,, |  | (9) |

where the operator ℒν\mathcal{L}^{\nu} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒν=−((p+k​ν)​ν+β​q​(p−ψ​(s)))​∂x+ν​∂q+b​ν​∂p+12​σ2​∂s​s+12​η2​∂p​p+ρ​σ​η​∂s​p.\displaystyle\mathcal{L}^{\nu}=-\biggl((p+k\,\nu)\,\nu+\beta\,q\,(p-\psi\left(s\right))\biggr)\,\partial\_{x}+\nu\,\partial\_{q}+b\,\nu\,\partial\_{p}+\frac{1}{2}\,\sigma^{2}\,\partial\_{ss}+\frac{1}{2}\,\eta^{2}\,\partial\_{pp}+\rho\,\sigma\,\eta\,\partial\_{sp}\,. |  | (10) |

## 3 Identity Payoff Function

In this section we consider the special case of payoff function ψ​(s)=s\psi(s)=s and derive the optimal trading strategy in closed form. To this end, it is convenient to introduce the process Z=(Ztν)t∈[0,T]Z=(Z\_{t}^{\nu})\_{t\in[0,T]} defined by Ztν=Ptν−StZ^{\nu}\_{t}=P\_{t}^{\nu}-S\_{t} along with an associated state variable z=p−sz=p-s. Additionally, we assume 2​α>b2\,\alpha>b which ensures that solutions to ODEs appearing in subsequent results do not blow up.

###### Proposition 1 (Value Function for Identity Payoff Function)

Suppose ψ​(s)=s\psi(s)=s and define the constant Σ\Sigma by Σ2=σ2+η2−2​ρ​σ​η\Sigma^{2}=\sigma^{2}+\eta^{2}-2\,\rho\,\sigma\,\eta. Suppose the functions h0h\_{0}, h1h\_{1}, h2h\_{2}, and h3h\_{3} satisfy the system of ODEs

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h0′+Σ2​h2=0,h0​(T)=0,h1′−ϕ+14​k​(b​(1+h3)+2​h1)2=0,h1​(T)=−α,h2′+14​k​(2​b​h2+h3)2=0,h2​(T)=0,h3′−β+12​k​(b​(1+h3)+2​h1)​(2​b​h2+h3)=0,h3​(T)=0.\displaystyle\begin{split}h^{\prime}\_{0}+\Sigma^{2}\,h\_{2}&=0\,,\qquad h\_{0}(T)=0\,,\\ h^{\prime}\_{1}-\phi+\frac{1}{4k}\,\biggl(b\,(1+h\_{3})+2\,h\_{1}\biggr)^{2}&=0\,,\qquad h\_{1}(T)=-\alpha\,,\\ h^{\prime}\_{2}+\frac{1}{4k}\,(2\,b\,h\_{2}+h\_{3})^{2}&=0\,,\qquad h\_{2}(T)=0\,,\\ h^{\prime}\_{3}-\beta+\frac{1}{2k}\,(b\,(1+h\_{3})+2\,h\_{1})\,(2\,b\,h\_{2}+h\_{3})&=0\,,\qquad h\_{3}(T)=0\,.\end{split} | |  | (11) |

Then the solution to ([9](https://arxiv.org/html/2601.10812v1#S2.E9 "In 2.2 Performance Criterion ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts")) is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H​(t,x,q,p,s)\displaystyle H(t,x,q,p,s) | =x+q​p+h​(t,q,p−s),\displaystyle=x+q\,p+h(t,q,p-s)\,, |  | (12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h​(t,q,z)\displaystyle h(t,q,z) | =h0​(t)+h1​(t)​q2+h2​(t)​z2+h3​(t)​q​z.\displaystyle=h\_{0}(t)+h\_{1}(t)\,q^{2}+h\_{2}(t)\,z^{2}+h\_{3}(t)\,q\,z\,. |  | (13) |

Assuming ([11](https://arxiv.org/html/2601.10812v1#S3.E11 "In Proposition 1 (Value Function for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) holds, ([12](https://arxiv.org/html/2601.10812v1#S3.E12 "In Proposition 1 (Value Function for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) can be seen to solve the HJB equation ([9](https://arxiv.org/html/2601.10812v1#S2.E9 "In 2.2 Performance Criterion ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts")) by direct substitution.

The form of the value function in ([12](https://arxiv.org/html/2601.10812v1#S3.E12 "In Proposition 1 (Value Function for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) shows that a dimensional reduction occurs. The excess value function of the agent, hh, only depends on the two variables pp and ss through their difference. At the time of writing, we are unable to solve the system of ODEs ([11](https://arxiv.org/html/2601.10812v1#S3.E11 "In Proposition 1 (Value Function for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) in closed form, even through the application of symbolic computer algebra systems. However, we are able to compute the optimal trading strategy in closed-form which appears in Theorem [2](https://arxiv.org/html/2601.10812v1#Thmtheorem2 "Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). This allows us to write the solution to ([11](https://arxiv.org/html/2601.10812v1#S3.E11 "In Proposition 1 (Value Function for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) in terms of definite integrals of known functions which can be easily computed numerically.

###### Theorem 2 (Optimal Trading Strategy for Identity Payoff Function)

Suppose ψ​(s)=s\psi(s)=s. Then the optimal trading speed in feedback form is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν∗​(t,q,p,s)=14​k​((ξ​(t)+π​(t))​q+1b​(ξ​(t)−π​(t))​(p−s)),\displaystyle\nu^{\*}(t,q,p,s)=\frac{1}{4\,k}\,\left((\xi(t)+\pi(t))\,q+\frac{1}{b}\,(\xi(t)-\pi(t))\,(p-s)\right)\,, |  | (14) |

where the function ξ\xi and π\pi are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ξ​(t)\displaystyle\xi(t) | =a​C​e−2​ω​(T−t)−1C​e−2​ω​(T−t)+1,\displaystyle=a\,\frac{C\,e^{-2\,\omega\,(T-t)}-1}{C\,e^{-2\,\omega\,(T-t)}+1}\,, |  | (15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π​(t)=−4​k​ϕ​(C​e−ω​(T−t)+1)​(1−e−ω​(T−t))a​(C​e−2​ω​(T−t)+1)+e−ω​(T−t)C​e−2​ω​(T−t)+1​(C+1)​(b−2​α),\displaystyle\begin{split}\pi(t)&=-\frac{4\,k\,\phi\,(Ce^{-\omega\,(T-t)}+1)\,(1-e^{-\omega\,(T-t)})}{a\,(C\,e^{-2\,\omega\,(T-t)}+1)}\\ &\hskip 56.9055pt+\frac{e^{-\omega\,(T-t)}}{C\,e^{-2\,\omega\,(T-t)}+1}\,(C+1)\,(b-2\,\alpha)\,,\end{split} | |  | (16) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | a=2​k​(b​β+ϕ),C=a+b−2​αa−b+2​α,ω=a2​k.\displaystyle a=2\,\sqrt{k\,(b\,\beta+\phi)}\,,\qquad C=\frac{a+b-2\,\alpha}{a-b+2\,\alpha}\,,\qquad\omega=\frac{a}{2\,k}\,. |  | (17) |

Moreover, the solution provided in ([12](https://arxiv.org/html/2601.10812v1#S3.E12 "In Proposition 1 (Value Function for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) is indeed the value function as defined in ([7](https://arxiv.org/html/2601.10812v1#S2.E7 "In 2.2 Performance Criterion ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts")).

For a proof see Appendix A.

The optimal trading strategy ([14](https://arxiv.org/html/2601.10812v1#S3.E14 "In Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) in Theorem [2](https://arxiv.org/html/2601.10812v1#Thmtheorem2 "Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") shows how the trading speed is affected by the remaining inventory qq and (scaled) funding rate z=p−sz=p-s at time tt. By noting that ξ​(t)<0\xi(t)<0 for all tt and inspecting the ODEs for the functions ff and gg introduced in the proof of Theorem [2](https://arxiv.org/html/2601.10812v1#Thmtheorem2 "Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"), we see that the coefficients of qq and z=p−sz=p-s in ([14](https://arxiv.org/html/2601.10812v1#S3.E14 "In Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) are negative for all t∈[0,T)t\in[0,T). A negative coefficient on qq is typical for optimal liquidation problems when the unaffected price of the traded asset (given by ([3](https://arxiv.org/html/2601.10812v1#S2.E3 "In 2.1 Dynamics ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts"))) is a martingale and when impact effects do not outweigh the terminal penalty (ensured by the assumption 2​α>b2\,\alpha>b). This is a result of the agent’s desire to minimize the risk associated with holding inventory through time and the penalty associated with terminal inventory holdings. A negative coefficient on z=p−sz=p-s (except at t=Tt=T where the coefficient is zero) is due to the agent’s desire to decrease the cost of paying the funding rate in a long position or to increase the profit from receiving the funding rate in a short position.

In Figure [1](https://arxiv.org/html/2601.10812v1#S3.F1 "Figure 1 ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") we plot the (normalized) density of the inventory process for each value of tt along with the optimal Almgren-Chriss inventory liquidation path which assumes there is no funding rate. This is done for three different values of the initial funding rate which are positive, zero, and negative in the left, middle, and right panels, respectively. Note that when the initial funding rate is zero (middle panel) the agent behaves similar to the Almgren-Chriss strategy on average when early in the trading period, but then ends up holding higher inventory on average before finally speeding up liquidation towards the end of the trading period. This is due to the impact effects of the agents trades on the perpetual price and the resulting change in the funding rate. When the funding rate is zero, the agent is not rewarded or penalized for holding inventory and so she liquidates as normal. Once their initial liquidating trades have impacted the price, the funding rate will tend to be negative and the agent is rewarded by holding positive inventory. Subsequently, when there is little time left until the agent must liquidate, she speeds up her trading because there is little benefit left in receiving the funding rate and she wishes to avoid the terminal liquidation penalty.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

![Refer to caption](x3.png)

Figure 1: Cross sectional density plots of inventory when trading according to the optimal strategy given in ([14](https://arxiv.org/html/2601.10812v1#S3.E14 "In Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")). The thick dotted curve shows the Almgren-Chriss liquidation strategy. Thin curves represent the 5t​h5^{th} and 95t​h95^{th} percentile and the mean. In each panel, the initial spot price is S0=100S\_{0}=100, but the initial perpetual price is P0=101P\_{0}=101 (left), P0=100P\_{0}=100 (middle), and P0=99P\_{0}=99 (right). Parameter values are T=1T=1, k=0.1k=0.1, b=0.1b=0.1, α=100\alpha=100, ϕ=0.5\phi=0.5, β=5\beta=5, σ=1\sigma=1, η=1\eta=1, ρ=0.3\rho=0.3.

In the following proposition we show that when the effect of temporary impact is small, the agent attempts to maintain a relationship between her inventory and the funding rate.

###### Proposition 3

Let ν∗\nu^{\ast} be the optimal trading strategy for the identity payoff function given in ([14](https://arxiv.org/html/2601.10812v1#S3.E14 "In Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")). Define a stochastic process A=(At)t∈[0,T]A=(A\_{t})\_{t\in[0,T]} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | At=(b​β+2​ϕ)​Qtν∗+β​Ztν∗.\displaystyle A\_{t}=(b\,\beta+2\,\phi)\,Q^{\nu^{\ast}}\_{t}+\beta\,Z^{\nu^{\ast}}\_{t}\,. |  | (18) |

Then the following limit holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | limk→0𝔼​[∫0TAt2​𝑑t]=0.\displaystyle\lim\_{k\to 0}\mathbb{E}\biggl[\int\_{0}^{T}A\_{t}^{2}\,dt\biggr]=0\,. |  | (19) |

For a proof see Appendix A.

Proposition [3](https://arxiv.org/html/2601.10812v1#Thmtheorem3 "Proposition 3 ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") gives a rule of thumb that the agent can follow if the market state would not result in significant costs due to trading. Namely, she should trade in such a way that she maintains the process AA defined in ([18](https://arxiv.org/html/2601.10812v1#S3.E18 "In Proposition 3 ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) to be close to zero. This is similar to other results in portfolio optimization or algorithmic trading in which there is an optimal long-term inventory position which balances risk and return (see for example Cartea
et al. ([2020](https://arxiv.org/html/2601.10812v1#bib.bib6))). However, after observing the funding rate it is not a direct task of computing the desired inventory which is a multiple of ZtZ\_{t} and submitting the appropriate trade which attains that inventory value, because the trade itself impacts the value of the funding rate.

In Figure [2](https://arxiv.org/html/2601.10812v1#S3.F2 "Figure 2 ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") we show a sample path of the processes AA and Qν∗Q^{\nu^{\*}} for several values of the temporary price impact parameter kk. Note that as kk decreases the whole path of AA tends to become zero (except at times t=0t=0 and t=Tt=T). Indeed, Figure [3](https://arxiv.org/html/2601.10812v1#S3.F3 "Figure 3 ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") shows the cross sectional density of AA for three values of kk which shows this convergence. The right panel of Figure [2](https://arxiv.org/html/2601.10812v1#S3.F2 "Figure 2 ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") shows that for moderate values of temporary price impact the inventory tends to “chase” the value which is optimal for small impact, but for large values of impact this is too costly to perform.

![Refer to caption](x4.png)

![Refer to caption](x5.png)

Figure 2: Sample paths of the process AA defined in Proposition [3](https://arxiv.org/html/2601.10812v1#Thmtheorem3 "Proposition 3 ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") (left panel) and inventory (right panel) for various values of temporary price impact parameter kk. Other parameter values are T=5T=5, b=0.1b=0.1, α=100\alpha=100, ϕ=0.5\phi=0.5, β=5\beta=5, σ=1\sigma=1, η=1\eta=1, ρ=0.3\rho=0.3.



![Refer to caption](x6.png)

![Refer to caption](x7.png)

![Refer to caption](x8.png)

Figure 3: Cross sectional density plots of the process AA defined in Proposition [3](https://arxiv.org/html/2601.10812v1#Thmtheorem3 "Proposition 3 ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). The temporary price impact parameter in each panel is k=2⋅10−1k=2\cdot 10^{-1} (left), k=2⋅10−3k=2\cdot 10^{-3} (middle), k=2⋅10−5k=2\cdot 10^{-5} (right). Other parameter values are T=5T=5, b=0.1b=0.1, α=100\alpha=100, ϕ=0.5\phi=0.5, β=5\beta=5, σ=1\sigma=1, η=1\eta=1, ρ=0.3\rho=0.3.

## 4 Arbitrary Payoff Function

In this section we consider the payoff function ψ\psi to be arbitrary with some mild technical restrictions given below. The associated HJB equation ([9](https://arxiv.org/html/2601.10812v1#S2.E9 "In 2.2 Performance Criterion ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts")) no longer admits the dimensional reduction which appears in ([12](https://arxiv.org/html/2601.10812v1#S3.E12 "In Proposition 1 (Value Function for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")), but we still apply the excess value ansatz which takes the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Hψ​(t,x,q,p,s;β)\displaystyle H\_{\psi}(t,x,q,p,s;\beta) | =x+q​p+hψ​(t,q,p,s;β),\displaystyle=x+q\,p+h\_{\psi}(t,q,p,s;\beta)\,, |  | (20) |

where we have emphasized that the value function depends on the payoff function ψ\psi and funding parameter β\beta. By substitution in ([9](https://arxiv.org/html/2601.10812v1#S2.E9 "In 2.2 Performance Criterion ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts")) the excess value function hψh\_{\psi} satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂thψ+12​(σ2​∂s​shψ+η2​∂p​phψ+2​ρ​σ​η​∂s​phψ)−ϕ​q2−β​q​(p−ψ​(s))+supν{−k​v2+(∂qhψ+b​(q+∂phψ))​ν}=0,\displaystyle\begin{split}\partial\_{t}h\_{\psi}+\frac{1}{2}\,\biggl(\sigma^{2}\,\partial\_{ss}h\_{\psi}+\eta^{2}\,\partial\_{pp}h\_{\psi}+2\,\rho\,\sigma\,\eta\,\partial\_{sp}h\_{\psi}\biggr)-\phi\,q^{2}\hskip 28.45274pt\\ -\beta\,q\,(p-\psi(s))+\sup\_{\nu}\biggl\{-k\,v^{2}+(\partial\_{q}h\_{\psi}+b\,(q+\partial\_{p}h\_{\psi}))\,\nu\biggr\}&=0\,,\end{split} | |  | (21) |

with terminal condition hψ​(T,q,p,s;β)=−α​q2h\_{\psi}(T,q,p,s;\beta)=-\alpha\,q^{2}. The supremum in equation ([21](https://arxiv.org/html/2601.10812v1#S4.E21 "In 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) is attained at

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν∗\displaystyle\nu^{\*} | =12​k​(∂qhψ+b​(q+∂phψ)),\displaystyle=\frac{1}{2\,k}\biggl(\partial\_{q}h\_{\psi}+b\,(q+\partial\_{p}h\_{\psi})\biggr)\,, |  | (22) |

which upon substitution into ([21](https://arxiv.org/html/2601.10812v1#S4.E21 "In 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂thψ+12​(σ2​∂s​shψ+η2​∂p​phψ+2​ρ​σ​η​∂s​phψ)−ϕ​q2−β​q​(p−ψ​(s))+14​k​(∂qhψ+b​(q+∂phψ))2=0.\displaystyle\begin{split}\partial\_{t}h\_{\psi}+\frac{1}{2}\,\biggl(\sigma^{2}\,\partial\_{ss}h\_{\psi}+\eta^{2}\,\partial\_{pp}h\_{\psi}+2\,\rho\,\sigma\,\eta\,\partial\_{sp}h\_{\psi}\biggr)-\phi\,q^{2}\hskip 28.45274pt\\ -\beta\,q\,(p-\psi(s))+\frac{1}{4\,k}\biggl(\partial\_{q}h\_{\psi}+b\,(q+\partial\_{p}h\_{\psi})\biggr)^{2}&=0\,.\end{split} | |  | (23) |

In order to prove the validity of the expansion given below, we make the following technical assumptions.

###### Assumption 4

1. 1.

   ψ∈C4​(ℝ)\psi\in C^{4}\left(\mathbb{R}\right) with all derivatives bounded.
2. 2.

   Given initial states xx, qq, pp and ss, there exist positive constants ϵ∗\epsilon^{\*}, β∗\beta^{\*}, and KK that satisfy the following uniform boundedness condition: for every ϵ∈(0,ϵ∗)\epsilon\in\left(0,\epsilon^{\*}\right) and β∈(0,β∗)\beta\in\left(0,\beta^{\*}\right) if ν\nu is an admissible control such that

   |  |  |  |
   | --- | --- | --- |
   |  | Hψν​(0,x,q,p,s;β)+ϵ≥Hψ​(0,x,q,p,s;β),\displaystyle H^{\nu}\_{\psi}\left(0,x,q,p,s;\beta\right)+\epsilon\geq H\_{\psi}\left(0,x,q,p,s;\beta\right)\,, |  |

   then for every t∈[0,T]t\in[0,T]

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝔼​[(Qtν)2]\displaystyle\mathbb{E}[(Q\_{t}^{\nu})^{2}] | ≤K.\displaystyle\leq K\,. |  |

Part i) of Assumption [4](https://arxiv.org/html/2601.10812v1#Thmtheorem4 "Assumption 4 ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") is made for technical convenience in proving the asymptotic convergence of our proposed strategies and can likely be weakened to include more payoff functions, but we want to focus on the derivation and interpretation of such strategies rather than classifying their effectiveness in full generality. Likewise, part ii) of Assumption [4](https://arxiv.org/html/2601.10812v1#Thmtheorem4 "Assumption 4 ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") is a technical assumption which assists in the proofs of our convergence results. The interpretation of this assumption is that the underlying processes satisfy a type of uniform boundedness condition with respect to the control when controls are restricted to being close to optimal. Similar assumptions about boundedness and regularity are made in other works that derive approximations to optimal trading strategies such as in Ekren and
Muhle-Karbe ([2019](https://arxiv.org/html/2601.10812v1#bib.bib12)) and Cartea
et al. ([2020](https://arxiv.org/html/2601.10812v1#bib.bib6)). This assumption implies a similar boundedness condition for PtνP\_{t}^{\nu} because price impact is linear, and StS\_{t} satisfies is trivially because it does not depend on the control.

The following theorem gives an approximation of the value function which has an error that vanishes to second order with respect to the funding rate parameter β\beta.

###### Theorem 5 (Asymptotic Approximation of Value Function)

The excess value function hψh\_{\psi} admits the following approximation:
  
i) Expansion:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hψ​(t,q,p,s;β)\displaystyle h\_{\psi}(t,q,p,s;\beta) | =h^ψ​(t,q,p,s;β)+R​(t,q,p,s;β),\displaystyle=\widehat{h}\_{\psi}(t,q,p,s;\beta)+R(t,q,p,s;\beta)\,, |  | (24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h^ψ​(t,q,p,s;β)\displaystyle\widehat{h}\_{\psi}(t,q,p,s;\beta) | =h0​(t,q)+β​h1,ψ​(t,q,p,s)+β2​h2,ψ​(t,q,p,s),\displaystyle=h\_{0}(t,q)+\beta\,h\_{1,\psi}(t,q,p,s)+\beta^{2}\,h\_{2,\psi}(t,q,p,s)\,, |  | (25) |

such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limβ↓01β2​R​(t,q,p,s;β)\displaystyle\lim\_{\beta\downarrow 0}\frac{1}{\beta^{2}}\,R(t,q,p,s;\beta) | =0,\displaystyle=0, |  | (26) |

  

ii) Zero and First Order Terms: The functions h0h\_{0} and h1,ψh\_{1,\psi} may be taken as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h0​(t,q)\displaystyle h\_{0}(t,q) | =γ​(t)​q2,\displaystyle=\gamma(t)\,q^{2}\,, |  | (27) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h1,ψ​(t,q,p,s)\displaystyle h\_{1,\psi}(t,q,p,s) | =γ0,ψ​(t,s)​q+γ1​(t)​q​p+γ2​(t)​q2,\displaystyle=\gamma\_{0,\psi}(t,s)\,q+\gamma\_{1}(t)\,q\,p+\gamma\_{2}(t)\,q^{2}\,, |  | (28) |

where the functions γ\gamma, γ0,ψ\gamma\_{0,\psi}, γ1\gamma\_{1} and γ2\gamma\_{2} are given as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ​(t)\displaystyle\gamma(t) | =a~2​C~​e−2​ω~​(T−t)−1C~​e−2​ω~​(T−t)+1−b2,\displaystyle=\frac{\widetilde{a}}{2}\,\frac{\widetilde{C}\,e^{-2\,\widetilde{\omega}\,(T-t)}-1}{\widetilde{C}\,e^{-2\,\widetilde{\omega}\,(T-t)}+1}-\frac{b}{2}\,, |  | (29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ0,ψ​(t,s)\displaystyle\gamma\_{0,\psi}(t,s) | =∫tTC~​e−ω~​(T−u)+eω~​(T−u)C~​e−ω~​(T−t)+eω~​(T−t)​𝔼​[ψ​(Su)|St=s]​𝑑u,\displaystyle=\int\_{t}^{T}\frac{\widetilde{C}\,e^{-\widetilde{\omega}\,(T-u)}+e^{\widetilde{\omega}\,(T-u)}}{\widetilde{C}\,e^{-\widetilde{\omega}\,(T-t)}+e^{\widetilde{\omega}\,(T-t)}}\,\mathbb{E}[\psi(S\_{u})|S\_{t}=s]\,du\,, |  | (30) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ1​(t)\displaystyle\gamma\_{1}(t) | =(C~​e−ω~​(T−t)+1)​(e−ω~​(T−t)−1)ω~​(C~​e−2​ω~​(T−t)+1),\displaystyle=\frac{(\widetilde{C}\,e^{-\widetilde{\omega}\,(T-t)}+1)\,(e^{-\widetilde{\omega}\,(T-t)}-1)}{\widetilde{\omega}\,(\widetilde{C}\,e^{-2\,\widetilde{\omega}\,(T-t)}+1)}\,, |  | (31) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ2​(t)=−b​e−2​ω~​(T−t)2​ω~​(C~​e−2​ω~​(T−t)+1)2(4ω~C~(T−t)−2(1−C~)(1−eω~​(T−t))+2(C~2−C~)(1−e−ω~​(T−t))+(1−e2​ω~​(T−t))−C~2(1−e−2​ω~​(T−t))),\displaystyle\begin{split}\gamma\_{2}(t)&=\frac{-b\,e^{-2\,\widetilde{\omega}\,(T-t)}}{2\,\widetilde{\omega}\,(\widetilde{C}\,e^{-2\,\widetilde{\omega}\,(T-t)}+1)^{2}}\,\biggl(4\,\widetilde{\omega}\,\widetilde{C}\,(T-t)-2\,(1-\widetilde{C})\,(1-e^{\widetilde{\omega}\,(T-t)})\\ &\hskip 28.45274pt+2(\widetilde{C}^{2}-\widetilde{C})\,(1-e^{-\widetilde{\omega}\,(T-t)})+(1-e^{2\,\widetilde{\omega}\,(T-t)})-\widetilde{C}^{2}\,(1-e^{-2\,\widetilde{\omega}\,(T-t)})\biggr)\,,\end{split} | |  | (32) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | a~=2​k​ϕ,C~=a~+b−2​αa~−b+2​α,ω~=a~2​k.\displaystyle\widetilde{a}=2\,\sqrt{k\,\phi}\,,\qquad\widetilde{C}=\frac{\widetilde{a}+b-2\,\alpha}{\widetilde{a}-b+2\,\alpha}\,,\qquad\widetilde{\omega}=\frac{\widetilde{a}}{2\,k}\,. |  | (33) |

iii) Second Order Terms: The function h2,ψh\_{2,\psi} may be taken as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h2,ψ​(t,q,p,s)\displaystyle h\_{2,\psi}(t,q,p,s) | =λ0​(t,s)+λ1​(t,s)​q+λ2​(t)​q2+λ3​(t)​q​p+λ4​(t,s)​p+λ5​(t)​p2,\displaystyle=\lambda\_{0}(t,s)+\lambda\_{1}(t,s)\,q+\lambda\_{2}(t)\,q^{2}+\lambda\_{3}(t)q\,p+\lambda\_{4}(t,s)\,p+\lambda\_{5}(t)\,p^{2}\,, |  | (34) |

where λ0\lambda\_{0} has at most quadratic growth in ss, and λ1\lambda\_{1} and λ4\lambda\_{4} have at most linear growth in ss.

For a proof see Appendix B.

With an approximation to the value function in hand through Theorem [5](https://arxiv.org/html/2601.10812v1#Thmtheorem5 "Theorem 5 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"), one can substitute this approximation into the candidate feedback control ([22](https://arxiv.org/html/2601.10812v1#S4.E22 "In 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")), which is well defined because it is continuously differentiable, and collect terms according to powers of β\beta. The following theorem indicates the result of the computation and shows that truncating after terms of order greater than one in β\beta results in performance which is accurate to second order.

###### Theorem 6 (Asymptotic Approximation of Optimal Trading Speed)

Let ν^\widehat{\nu} be a feedback control given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν^​(t,q,p,s;β)\displaystyle\widehat{\nu}(t,q,p,s;\beta) | =ν0​(t,q)+β​ν1​(t,q,p,s),\displaystyle=\nu\_{0}(t,q)+\beta\,\nu\_{1}(t,q,p,s)\,, |  | (35) |

with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν0​(t,q)\displaystyle\nu\_{0}(t,q) | =12​k​(b+2​γ​(t))​q,\displaystyle=\frac{1}{2\,k}\,(b+2\,\gamma(t))\,q\,, |  | (36) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν1​(t,q,p,s)\displaystyle\nu\_{1}(t,q,p,s) | =12​k​(γ0,ψ​(t,s)+γ1​(t)​p+(2​γ2​(t)+b​γ1​(t))​q).\displaystyle=\frac{1}{2\,k}\,\biggl(\gamma\_{0,\psi}(t,s)+\gamma\_{1}(t)\,p+\bigl(2\,\gamma\_{2}(t)+b\,\gamma\_{1}(t)\bigr)\,q\biggr)\,. |  | (37) |

Then ν^t=ν^​(t,Qtν^,Ptν^,St;β)\widehat{\nu}\_{t}=\widehat{\nu}\left(t,Q^{\widehat{\nu}}\_{t},P^{\widehat{\nu}}\_{t},S\_{t};\beta\right) is an admissible control. Defining hψν^h\_{\psi}^{\widehat{\nu}} by the relation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hψν^​(t,x,q,p,s;β)=x+q​p+hψν^​(t,q,p,s;β),\displaystyle H\_{\psi}^{\widehat{\nu}}\left(t,x,q,p,s;\beta\right)=x+q\,p+h\_{\psi}^{\widehat{\nu}}\left(t,q,p,s;\beta\right)\,, |  | (38) |

ν^\widehat{\nu} is asymptotically optimal to second order with respect to β\beta. Specifically

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limβ→0hψ​(t,q,p,s;β)−hψν^​(t,q,p,s;β)β2\displaystyle\lim\_{\beta\rightarrow 0}\frac{h\_{\psi}\left(t,q,p,s;\beta\right)-h\_{\psi}^{\widehat{\nu}}\left(t,q,p,s;\beta\right)}{\beta^{2}} | =0.\displaystyle=0\,. |  | (39) |

For the proof see Appendix B.

Inspection of the strategy in ([35](https://arxiv.org/html/2601.10812v1#S4.E35 "In Theorem 6 (Asymptotic Approximation of Optimal Trading Speed) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) and comparison to other results in optimal execution give an interpretation for its structure. The term ν0​(t,q)\nu\_{0}(t,q) representing the order zero contribution is the Almgren-Chriss strategy, which is to be expected since we are considering an expansion with respect to the funding parameter β\beta. The first order correction contains two contributions. The first is 12​k​(γ0,ψ​(t,s)+γ1​(t)​p)\frac{1}{2\,k}\,(\gamma\_{0,\psi}(t,s)+\gamma\_{1}(t)\,p) which satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​k​γ0,ψ​(t,s)+γ1​(t)​p\displaystyle\frac{1}{2\,k}\,\gamma\_{0,\psi}(t,s)+\gamma\_{1}(t)\,p | =−12​k​∫tTC~​e−ω~​(T−u)+eω~​(T−u)C~​e−ω~​(T−t)+eω~​(T−t)​𝔼​[p−ψ​(Su)|St=s]​𝑑u.\displaystyle=-\frac{1}{2\,k}\,\int\_{t}^{T}\frac{\widetilde{C}\,e^{-\widetilde{\omega}\,(T-u)}+e^{\widetilde{\omega}\,(T-u)}}{\widetilde{C}\,e^{-\widetilde{\omega}\,(T-t)}+e^{\widetilde{\omega}\,(T-t)}}\,\mathbb{E}[p-\psi(S\_{u})|S\_{t}=s]\,du\,. |  |

This has an analogous form to execution strategies with an alpha signal, where the signal here is the quantity p−ψ​(s)p-\psi(s) (see for example Cartea and
Jaimungal ([2016](https://arxiv.org/html/2601.10812v1#bib.bib7)) and Neuman and
Voß ([2022](https://arxiv.org/html/2601.10812v1#bib.bib17))). The remaining term 12​k​(2​γ2​(t)+b​γ1​(t))​q\frac{1}{2\,k}\,\bigl(2\,\gamma\_{2}(t)+b\,\gamma\_{1}(t)\bigr)\,q represents how the agent unwinds the additional inventory which is acquired by taking advantage of the signal p−ψ​(s)p-\psi(s).

In a similar vein to Theorem [5](https://arxiv.org/html/2601.10812v1#Thmtheorem5 "Theorem 5 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"), the following result gives an approximation of the value function when the time remaining until maturity is small.

###### Theorem 7 (Asymptotic Approximation of Value Function)

The excess value function hψh\_{\psi} admits the following approximation:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hψ​(t,q,p,s;T)\displaystyle h\_{\psi}(t,q,p,s;T) | =h~ψ​(t,q,p,s;T)+R~​(t,q,p,s;T),\displaystyle=\widetilde{h}\_{\psi}(t,q,p,s;T)+\widetilde{R}(t,q,p,s;T)\,, |  | (40) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h~ψ​(t,q,p,s;T)\displaystyle\widetilde{h}\_{\psi}(t,q,p,s;T) | =h~0​(q)+(T−t)​h~1,ψ​(q,p,s)+(T−t)2​h~2,ψ​(q,p,s),\displaystyle=\widetilde{h}\_{0}(q)+(T-t)\,\widetilde{h}\_{1,\psi}(q,p,s)+(T-t)^{2}\,\widetilde{h}\_{2,\psi}(q,p,s)\,, |  | (41) |

such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limT↓01T2​R~​(t,q,p,s;T)\displaystyle\lim\_{T\downarrow 0}\frac{1}{T^{2}}\,\widetilde{R}(t,q,p,s;T) | =0,\displaystyle=0, |  | (42) |

where the function h~0\widetilde{h}\_{0}, h~1,ψ\widetilde{h}\_{1,\psi} and h~2,ψ\widetilde{h}\_{2,\psi} are given as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h~0​(q)\displaystyle\widetilde{h}\_{0}(q) | =−α​q2,\displaystyle=-\alpha\,q^{2}, |  | (43) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h~1,ψ​(q,p,s)\displaystyle\widetilde{h}\_{1,\psi}(q,p,s) | =((b−2​α)24​k−ϕ)​q2−β​(p−ψ​(s))​q,\displaystyle=\biggl(\frac{(b-2\alpha)^{2}}{4\,k}-\phi\biggr)\,q^{2}-\beta\,(p-\psi(s))\,q, |  | (44) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h~2,ψ​(q,p,s)\displaystyle\widetilde{h}\_{2,\psi}(q,p,s) | =b−2​α4​k​((b−2​α)22​k−2​ϕ−b​β)​q2+β4​(−b−2​αk​(p−ψ​(s))+σ2​ψ′′′​(s))​q.\displaystyle=\frac{b-2\,\alpha}{4\,k}\biggl(\frac{(b-2\,\alpha)^{2}}{2\,k}-2\,\phi-b\,\beta\biggr)\,q^{2}+\frac{\beta}{4}\,\biggl(-\frac{b-2\,\alpha}{k}\,(p-\psi(s))+\sigma^{2}\,\psi^{\prime\prime\prime}(s)\biggr)\,q. |  | (45) |

For a proof see Appendix B.

Using a similar process to computing a trading strategy which is approximately optimal as in Theorem [6](https://arxiv.org/html/2601.10812v1#Thmtheorem6 "Theorem 6 (Asymptotic Approximation of Optimal Trading Speed) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"), the approximation to the value function can be substituted into the candidate feedback control ([22](https://arxiv.org/html/2601.10812v1#S4.E22 "In 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")). The following theorem shows that by truncating the resulting expression after the terms which are linear with respect to TT, the control obtained yields performance which is accurate to second order.

###### Theorem 8 (Asymptotic Approximation of Optimal Trading Speed)

Let ν~\widetilde{\nu} be a feedback control given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν~​(t,q,p,s;T)\displaystyle\widetilde{\nu}(t,q,p,s;T) | =ν~0​(q)+(T−t)​ν~1​(q,p,s),\displaystyle=\widetilde{\nu}\_{0}(q)+(T-t)\,\widetilde{\nu}\_{1}(q,p,s)\,, |  | (46) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν~0​(q)\displaystyle\widetilde{\nu}\_{0}(q) | =12​k​(b​q+∂qh~0)\displaystyle=\frac{1}{2\,k}\,(b\,q+\partial\_{q}\widetilde{h}\_{0}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−2​α−b2​k​q,\displaystyle=-\frac{2\,\alpha-b}{2\,k}\,q\,, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ν~1​(t,q,p,s)\displaystyle\widetilde{\nu}\_{1}(t,q,p,s) | =12​k​(∂qh~1,ψ+b​∂ph~1,ψ)\displaystyle=\frac{1}{2\,k}\,(\partial\_{q}\widetilde{h}\_{1,\psi}+b\,\partial\_{p}\widetilde{h}\_{1,\psi}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​k​((2​α−b)22​k−(b​β+2​ϕ))​q−β2​k​(p−ψ​(s)).\displaystyle=\frac{1}{2\,k}\biggl(\frac{(2\,\alpha-b)^{2}}{2\,k}-(b\,\beta+2\,\phi)\biggr)\,q-\frac{\beta}{2\,k}\,(p-\psi(s))\,. |  |

Then ν~t=ν~​(t,Qtν~,Ptν~,St;T)\widetilde{\nu}\_{t}=\widetilde{\nu}\left(t,Q^{\widetilde{\nu}}\_{t},P^{\widetilde{\nu}}\_{t},S\_{t};T\right) is an admissible control. Defining hψν~h\_{\psi}^{\widetilde{\nu}} by the relation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hψν~​(t,x,q,p,s;T)=x+q​p+hψν~​(t,q,p,s;T),\displaystyle H\_{\psi}^{\widetilde{\nu}}\left(t,x,q,p,s;T\right)=x+q\,p+h\_{\psi}^{\widetilde{\nu}}\left(t,q,p,s;T\right)\,, |  | (47) |

ν~\widetilde{\nu} is asymptotically optimal to second order with respect to TT. Specifically

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limT→0hψ​(t,q,p,s;T)−hψν~​(t,q,p,s;T)T2\displaystyle\lim\_{T\rightarrow 0}\frac{h\_{\psi}\left(t,q,p,s;T\right)-h\_{\psi}^{\widetilde{\nu}}\left(t,q,p,s;T\right)}{T^{2}} | =0.\displaystyle=0\,. |  | (48) |

For the proof see Appendix B.

The trading strategy given in ([46](https://arxiv.org/html/2601.10812v1#S4.E46 "In Theorem 8 (Asymptotic Approximation of Optimal Trading Speed) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) has two contributing terms. Notice that the first term given by −2​α−b2​k​q-\frac{2\,\alpha-b}{2\,k}\,q does not depend on the running inventory penalty ϕ\phi or the funding rate parameter β\beta. This is because those parameters both affect the performance criterion according to a quantity which accumulates over time, but this term represents the limit of an optimal control as the length of the time horizon approaches zero. In fact, any control which is reasonably close to optimal is equal to this value at time TT as can be seen from the terminal condition of equation ([21](https://arxiv.org/html/2601.10812v1#S4.E21 "In 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) and the feedback from of the candidate optimal strategy given in ([22](https://arxiv.org/html/2601.10812v1#S4.E22 "In 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")). The remaining term in the control ([46](https://arxiv.org/html/2601.10812v1#S4.E46 "In Theorem 8 (Asymptotic Approximation of Optimal Trading Speed) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) captures the agent’s attempt to minimize the last remaining portion of the running inventory penalty through −ϕk​q-\frac{\phi}{k}\,q, and to adjust for the final funding payments through −β2​k​(p−ψ​(s))-\frac{\beta}{2\,k}\,(p-\psi(s)). The remainder of this term represents the agent compensating their strategy to avoid associated inventory penalties, and a higher order correction to the constant strategy taken at time TT as discussed above.

In the next result we show that the optimal trading strategy which is computed in closed form when the function ψ\psi is the identity may be used to attain performance which is approximately optimal for short time horizons in the case of a general payoff function. Recall the feedback form of this strategy is given by a function ν∗:[0,T]×ℝ3→ℝ\nu^{\*}:[0,T]\times\mathbb{R}^{3}\to\mathbb{R} written in closed form in ([14](https://arxiv.org/html/2601.10812v1#S3.E14 "In Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")). The approximating strategy is attained by substituting the quantity ψ​(s)\psi(s) for the fourth argument in place of ss.

###### Proposition 9 (Closed-form Approximation of Optimal Trading Speed)

The following approximation holds locally uniformly in (t,q,p,s)(t,q,p,s):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν∗​(t,q,p,ψ​(s);T)=ν~​(t,q,p,s;T)+o​(T).\displaystyle\nu^{\ast}(t,q,p,\psi(s);T)=\widetilde{\nu}(t,q,p,s;T)+o(T)\,. |  | (49) |

Let ν¯\overline{\nu} be a feedback control given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν¯​(t,q,p,s;T)\displaystyle\overline{\nu}(t,q,p,s;T) | =ν∗​(t,q,p,ψ​(s);T).\displaystyle=\nu^{\ast}(t,q,p,\psi(s);T)\,. |  | (50) |

Then ν¯t=ν¯​(t,Qtν¯,Ptν¯,St;T)\overline{\nu}\_{t}=\overline{\nu}(t,Q\_{t}^{\overline{\nu}},P\_{t}^{\overline{\nu}},S\_{t};T) is an admissible control. Define hψν¯h^{\overline{\nu}}\_{\psi} by the relation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hψν¯​(t,x,q,p,s;T)=x+q​p+hψν¯​(t,q,p,s;T).\displaystyle H^{\overline{\nu}}\_{\psi}(t,x,q,p,s;T)=x+q\,p+h^{\overline{\nu}}\_{\psi}(t,q,p,s;T)\,. |  | (51) |

Then ν¯\overline{\nu} is asymptotically approximately optimal to second order with respect to TT. Specifically,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limT→0hψ​(t,q,p,s;T)−hψν¯​(t,q,p,s;T)T2\displaystyle\lim\_{T\rightarrow 0}\frac{h\_{\psi}\left(t,q,p,s;T\right)-h\_{\psi}^{\overline{\nu}}\left(t,q,p,s;T\right)}{T^{2}} | =0.\displaystyle=0\,. |  | (52) |

For the proof see Appendix B.

Given two different approximations to optimal performance for small values of TT, it is reasonable to ask if one might typically perform better than the other. To this end, we conduct simulations of both strategies given in ([46](https://arxiv.org/html/2601.10812v1#S4.E46 "In Theorem 8 (Asymptotic Approximation of Optimal Trading Speed) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) and ([50](https://arxiv.org/html/2601.10812v1#S4.E50 "In Proposition 9 (Closed-form Approximation of Optimal Trading Speed) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")), along with the corresponding Almgren-Chriss strategy which assumes the funding rate is identically zero, and compare their performance for several values of TT. These simulations are conducted for two different payoff functions shown in Figure [4](https://arxiv.org/html/2601.10812v1#S4.F4 "Figure 4 ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). In the left panel the payoff function is chosen to be

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(S)\displaystyle\psi(S) | =S+2​L1+e−κ​(S−S0−ΔS),\displaystyle=S+\frac{2\,L}{1+e^{-\kappa\,(S-S\_{0}-\Delta\_{S})}}\,, |  |

with S0=100S\_{0}=100, ΔS=−0.1\Delta\_{S}=-0.1, κ=10\kappa=10, and L=1L=1. In the right panel the payoff function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(S)\displaystyle\psi(S) | =S+L​(S−S0−ΔS)2+Δψ,\displaystyle=S+L\,(S-S\_{0}-\Delta\_{S})^{2}+\Delta\_{\psi}\,, |  |

with S0=100S\_{0}=100, ΔS=0.2\Delta\_{S}=0.2, Δψ=−2\Delta\_{\psi}=-2, and L=5L=5.

![Refer to caption](x9.png)

![Refer to caption](x10.png)

Figure 4: The payoff functions use to demonstrate asymptotic accuracy of trading strategies. The left and right panels add a logistic and quadratic function, respectively, to the identity.

The performance of each strategy applied to both of these payoff functions is shown in Figure [5](https://arxiv.org/html/2601.10812v1#S4.F5 "Figure 5 ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). Note that as TT approaches zero, the excess performance of each strategy approaches −α​Q02-\alpha\,Q\_{0}^{2}. This is to be expected from any reasonable strategy which does not accumulate exorbitant costs due to temporary price impact. For larger values of TT in these examples, the performance of ν¯\overline{\nu} (blue) is better than that of ν~\widetilde{\nu} (red). While both are approximations to an optimal strategy which applies for small TT, the superior performance by ν¯\overline{\nu} can be explained by the fact that it is derived from a strategy (ν∗\nu^{\*} from ([14](https://arxiv.org/html/2601.10812v1#S3.E14 "In Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"))) which is optimal for all TT, albeit for a particular payoff function (identity), and that this strategy is optimal when the funding parameter β\beta is equal to zero. Thus, the strategy ν~\widetilde{\nu} tends to deviate from optimality more because it is derived using a method which approximates all elements of the problem under a small TT regime. Indeed, as the value of TT grows larger, we see in the right panel of Figure [5](https://arxiv.org/html/2601.10812v1#S4.F5 "Figure 5 ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") that the performance of ν~\widetilde{\nu} is substantially worse than that of ν¯\overline{\nu}, and even worse than the Almgren-Chriss strategy which completely ignores the funding rate.

The two examples in Figure [5](https://arxiv.org/html/2601.10812v1#S4.F5 "Figure 5 ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") show that hν¯>hν~h^{\overline{\nu}}>h^{\widetilde{\nu}}. Through the course of our numerical experiments we find that this is typically the case (generally expected due to the discussion of the previous paragraph) but examples can be found where hν~>hν¯h^{\widetilde{\nu}}>h^{\overline{\nu}}, although this does not hold over a wide range of parameter values. In particular, for larger values of TT the strategy ν~\widetilde{\nu} tends to deviate more significantly from optimality.

![Refer to caption](x11.png)

![Refer to caption](x12.png)

Figure 5: Strategy performance for various values of TT. The left and right panels use the logistic and quadratic payoff functions, respectively, from Figure [4](https://arxiv.org/html/2601.10812v1#S4.F4 "Figure 4 ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). Other parameter values are k=0.1k=0.1, b=0.1b=0.1, α=0.1\alpha=0.1, ϕ=0.5\phi=0.5, β=5\beta=5, σ=1\sigma=1, η=1\eta=1, ρ=0.3\rho=0.3, Q0=10Q\_{0}=10, P0=100P\_{0}=100, S0=100S\_{0}=100.

## 5 Conclusion

We have proposed a model in which an agent is able to trade a perpetual contract written on an underlying spot price process and attempts to maximize expected risk-adjusted terminal wealth when liquidating their position. When the payoff function of the perpetual contract is the identity we solve for the agent’s optimal trading strategy in closed form. We derive a limiting relation between inventory and funding rate under small transaction costs. Through simulation studies we demonstrate how the trading pattern deviates from a typical optimal liquidation strategy in the presence of a funding rate, and show that this deviation depends on the initial value of the funding rate. When the payoff function of the perpetual contract is an arbitrary function we propose multiple trading strategies which asymptotically approach optimal performance as either the funding rate parameter or time to maturity vanish. In particular, if one treats the payoff function as the spot price and uses the closed form strategy corresponding to the identity payoff case, then performance is asymptotically optimal for small values of maturity.

## 6 Proofs

## Appendix A: Proofs for Section [3](https://arxiv.org/html/2601.10812v1#S3 "3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") (Identity Payoff Function)

From Proposition [1](https://arxiv.org/html/2601.10812v1#Thmtheorem1 "Proposition 1 (Value Function for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"), the optimizer in the HJB equation is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν∗​(t,q,p,s)=12​k​((2​h1​(t)+b​(1+h3​(t)))​q+(h3​(t)+2​b​h2​(t))​(p−s)).\displaystyle\nu^{\*}(t,q,p,s)=\frac{1}{2\,k}\,\biggl(\bigl(2\,h\_{1}(t)+b\,(1+h\_{3}(t))\bigr)\,q+\bigl(h\_{3}(t)+2\,b\,h\_{2}(t)\bigr)\,(p-s)\biggr)\,. |  | (53) |

Define the functions ff and gg as the coefficients of qq and p−sp-s, that is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(t)\displaystyle f(t) | =2​h1​(t)+b​(1+h3​(t)),\displaystyle=2\,h\_{1}(t)+b\,(1+h\_{3}(t))\,, |  | (54) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g​(t)\displaystyle g(t) | =h3​(t)+2​b​h2​(t).\displaystyle=h\_{3}(t)+2\,b\,h\_{2}(t)\,. |  | (55) |

Using ([11](https://arxiv.org/html/2601.10812v1#S3.E11 "In Proposition 1 (Value Function for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) we see that ff and gg satisfy the system of ODEs

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f′​(t)\displaystyle f^{\prime}(t) | =b​β+2​ϕ−12​k​f​(t)​(b​g​(t)+f​(t)),\displaystyle=b\,\beta+2\,\phi-\frac{1}{2\,k}\,f(t)\,(b\,g(t)+f(t))\,, |  | (56) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g′​(t)\displaystyle g^{\prime}(t) | =β−12​k​g​(t)​(b​g​(t)+f​(t)),\displaystyle=\beta-\frac{1}{2\,k}\,g(t)\,(b\,g(t)+f(t))\,, |  | (57) |

with terminal condition f​(T)=b−2​αf(T)=b-2\,\alpha and g​(T)=0g(T)=0. We further define ξ​(t)=f​(t)+b​g​(t)\xi(t)=f(t)+b\,g(t) and π​(t)=f​(t)−b​g​(t)\pi(t)=f(t)-b\,g(t) which are seen to satisfy

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ξ′​(t)\displaystyle\xi^{\prime}(t) | =2​(b​β+ϕ)−12​k​ξ2​(t),\displaystyle=2\,(b\,\beta+\phi)-\frac{1}{2\,k}\,\xi^{2}(t)\,, |  | (58) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π′​(t)\displaystyle\pi^{\prime}(t) | =2​ϕ−12​k​ξ​(t)​π​(t),\displaystyle=2\,\phi-\frac{1}{2\,k}\,\xi(t)\,\pi(t)\,, |  | (59) |

with terminal conditions ξ​(T)=π​(T)=b−2​α\xi(T)=\pi(T)=b-2\,\alpha. The ODE ([58](https://arxiv.org/html/2601.10812v1#Sx1.E58 "In Appendix A: Proofs for Section 3 (Identity Payoff Function) ‣ Optimal Liquidation of Perpetual Contracts")) for ξ\xi is uncoupled of Riccati type and has solution

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ξ​(t)\displaystyle\xi(t) | =a​C​e−2​ω​(T−t)−1C​e−2​ω​(T−t)+1,\displaystyle=a\,\frac{C\,e^{-2\,\omega\,(T-t)}-1}{C\,e^{-2\,\omega\,(T-t)}+1}\,, |  | (60) |

with aa, CC, and ω\omega as in the statement of the theorem. The ODE ([59](https://arxiv.org/html/2601.10812v1#Sx1.E59 "In Appendix A: Proofs for Section 3 (Identity Payoff Function) ‣ Optimal Liquidation of Perpetual Contracts")) for π\pi may then be solved directly, and the solution is seen to be

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π​(t)=−4​k​ϕ​(C​e−ω​(T−t)+1)​(1−e−ω​(T−t))a​(C​e−2​ω​(T−t)+1)+e−ω​(T−t)C​e−2​ω​(T−t)+1​(C+1)​(b−2​α).\displaystyle\begin{split}\pi(t)&=-\frac{4\,k\,\phi\,(Ce^{-\omega\,(T-t)}+1)\,(1-e^{-\omega\,(T-t)})}{a\,(C\,e^{-2\,\omega\,(T-t)}+1)}\\ &\hskip 56.9055pt+\frac{e^{-\omega\,(T-t)}}{C\,e^{-2\,\omega\,(T-t)}+1}\,(C+1)\,(b-2\,\alpha)\,.\end{split} | |  | (61) |

The assumption 2​α>b2\,\alpha>b implies C∈(−1,1)C\in(-1,1) which ensures that the expressions for ξ​(t)\xi(t) and π​(t)\pi(t) above are well defined and finite for all t∈[0,T]t\in[0,T]. The definitions of ξ\xi and π\pi yield f​(t)=12​(ξ​(t)+π​(t))f(t)=\frac{1}{2}(\xi(t)+\pi(t)) and g​(t)=12​b​(ξ​(t)−π​(t))g(t)=\frac{1}{2\,b}(\xi(t)-\pi(t)), thus the feedback form of the optimal trading strategy is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν∗​(t,q,p,s)=14​k​((ξ​(t)+π​(t))​q+1b​(ξ​(t)−π​(t))​(p−s)).\displaystyle\nu^{\*}(t,q,p,s)=\frac{1}{4\,k}\,\biggl((\xi(t)+\pi(t))\,q+\frac{1}{b}\,(\xi(t)-\pi(t))\,(p-s)\biggr)\,. |  | (62) |

This control is linear with respect to the state variables with bounded coefficients and therefore is admissible. A standard verification argument shows that the solution to the HJB equation given in Proposition [1](https://arxiv.org/html/2601.10812v1#Thmtheorem1 "Proposition 1 (Value Function for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") is the value function as defined in ([7](https://arxiv.org/html/2601.10812v1#S2.E7 "In 2.2 Performance Criterion ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts")).
\qed

Define a stochastic process Y=(Yt)t∈[0,T]Y=(Y\_{t})\_{t\in[0,T]} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt=1k​(f​(t)​Qtν∗+g​(t)​Ztν∗),\displaystyle Y\_{t}=\frac{1}{\sqrt{k}}\,\biggl(f(t)\,Q^{\nu^{\ast}}\_{t}+g(t)\,Z^{\nu^{\ast}}\_{t}\biggr)\,, |  | (63) |

where f​(t)=12​(ξ​(t)+π​(t))f(t)=\frac{1}{2}(\xi(t)+\pi(t)) and g​(t)=12​b​(ξ​(t)−π​(t))g(t)=\frac{1}{2\,b}(\xi(t)-\pi(t)) as in the proof of Theorem [2](https://arxiv.org/html/2601.10812v1#Thmtheorem2 "Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). Application of Itô’s Lemma to the process YY yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt=1k​At​d​t+g​(t)​Σk​d​WtZ,\displaystyle dY\_{t}=\frac{1}{\sqrt{k}}\,A\_{t}\,dt+\frac{g(t)\,\Sigma}{\sqrt{k}}\,dW^{Z}\_{t}\,, |  | (64) |

where WZ=(WtZ)t∈[0,T]W^{Z}=(W^{Z}\_{t})\_{t\in[0,T]} is a Brownian motion defined to satisfy Σ​d​WtZ=η​d​WtP−σ​d​WtS\Sigma\,dW^{Z}\_{t}=\eta\,dW^{P}\_{t}-\sigma\,dW^{S}\_{t}. Applying Itô’s Lemma again to the process AA yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​At=1k​(b​β+ϕ)​Yt​d​t+β​Σ​d​WtZ.\displaystyle dA\_{t}=\frac{1}{\sqrt{k}}(b\,\beta+\phi)\,Y\_{t}\,dt+\beta\,\Sigma\,dW^{Z}\_{t}\,. |  | (65) |

Define a 2-dimensional vector process V=(Vt)t∈[0,T]V=(V\_{t})\_{t\in[0,T]} by Vt=[Yt,At]TV\_{t}=[Y\_{t},A\_{t}]^{T} which has dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt=Mk​Vt​d​t+uk​(t)​d​WtZ,\displaystyle dV\_{t}=M\_{k}\,V\_{t}\,dt+u\_{k}(t)\,dW^{Z}\_{t}\,, |  | (66) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mk=[01kb​β+ϕk0],uk​(t)=[g​(t)​Σkβ​Σ].\displaystyle M\_{k}=\begin{bmatrix}0&\frac{1}{\sqrt{k}}\\ \frac{b\,\beta+\phi}{\sqrt{k}}&0\end{bmatrix}\,,\qquad u\_{k}(t)=\begin{bmatrix}\frac{g(t)\,\Sigma}{\sqrt{k}}\\ \beta\,\Sigma\end{bmatrix}\,. |  | (67) |

From equation (6.10) in Karatzas and
Shreve ([1991](https://arxiv.org/html/2601.10812v1#bib.bib16)), the expectation VtV\_{t} can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Vt]=Φ​(t)​V0,\displaystyle\mathbb{E}[V\_{t}]=\Phi(t)\,V\_{0}\,, |  | (68) |

where Φ\Phi is the solution of the matrix differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ′​(t)=Mk​Φ​(t),Φ​(0)=[1001].\displaystyle\Phi^{\prime}(t)=M\_{k}\,\Phi(t)\,,\qquad\Phi(0)=\begin{bmatrix}1&0\\ 0&1\end{bmatrix}\,. |  | (69) |

This equation has solution

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Φ​(t)\displaystyle\Phi(t) | =eMk​t\displaystyle=e^{M\_{k}\,t}\, |  | (70) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =cosh⁡(m​tk)​[1001]+km​sinh⁡(m​tk)​Mk,\displaystyle=\cosh\biggl(\frac{m\,t}{\sqrt{k}}\biggr)\,\begin{bmatrix}1&0\\ 0&1\end{bmatrix}+\frac{\sqrt{k}}{m}\,\sinh\biggl(\frac{m\,t}{\sqrt{k}}\biggr)\,M\_{k}\,, |  | (71) |

where m=b​β+ϕm=\sqrt{b\,\beta+\phi}. Hence, the expectation of AtA\_{t} can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[At]=cosh⁡(ω​t)​A0+m​sinh⁡(ω​t)​Y0,\displaystyle\mathbb{E}[A\_{t}]=\cosh(\omega\,t)\,A\_{0}+m\,\sinh(\omega\,t)\,Y\_{0}\,, |  | (72) |

with ω=b​β+ϕk\omega=\sqrt{\frac{b\beta+\phi}{k}} as in ([17](https://arxiv.org/html/2601.10812v1#S3.E17 "In Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) of Theorem [2](https://arxiv.org/html/2601.10812v1#Thmtheorem2 "Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). For t≠{0,T}t\neq\{0,T\} a tedious but direct computation yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | limk→0𝔼​[At]\displaystyle\lim\_{k\rightarrow 0}\mathbb{E}[A\_{t}] | ={A0,t=00,0<t<T−b​β​Q0+β​Z0,t=T.\displaystyle=\left\{\begin{array}[]{cl}A\_{0}\,,&t=0\\ 0\,,&0<t<T\\ -b\,\beta\,Q\_{0}+\beta\,Z\_{0}\,,&t=T\end{array}\right.\,. |  |

From equation (6.6) in Karatzas and
Shreve ([1991](https://arxiv.org/html/2601.10812v1#bib.bib16)) and by using the Itô isometry, the covariance matrix of VtV\_{t} can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cov​(Vt)\displaystyle\text{Cov}(V\_{t}) | =Cov​(Φ​(t)​∫0tΦ−1​(s)​uk​(s)​𝑑WsZ)\displaystyle=\text{Cov}\biggl(\Phi(t)\int^{t}\_{0}\Phi^{-1}(s)\,u\_{k}(s)\,dW^{Z}\_{s}\biggr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0tΦ​(t−s)​uk​(s)​(uk​(s))T​(Φ​(t−s))T​𝑑s.\displaystyle=\int^{t}\_{0}\Phi(t-s)\,u\_{k}(s)\,(u\_{k}(s))^{T}\,(\Phi(t-s))^{T}\,ds. |  |

Let [⋅]2[\cdot]\_{2} represent the bottom element of a 2-dimensional vector and let [⋅]2,2[\cdot]\_{2,2} represent the (2,2)(2,2) entry of a 2×22\times 2 matrix. Then the variance of AtA\_{t} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(At)=[Cov​(Vt)]2,2=∫0t([Φ​(t−s)​uk​(s)]2)2​𝑑s.\displaystyle\text{Var}(A\_{t})=[\text{Cov}(V\_{t})]\_{2,2}=\int^{t}\_{0}\biggl([\Phi(t-s)\,u\_{k}(s)]\_{2}\biggr)^{2}\,ds. |  | (73) |

Another tedious but direct computation gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | [Φ​(t−s)​uk​(s)]2\displaystyle[\Phi(t-s)\,u\_{k}(s)]\_{2} | =β​Σ​cosh⁡(ω​(t−s))+ω​Σ​g​(s)​sinh⁡(ω​(t−s))\displaystyle=\beta\,\Sigma\,\cosh(\omega\,(t-s))+\omega\,\Sigma\,g(s)\,\sinh(\omega\,(t-s)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =β​Σ2​(C​e−2​ω​(T−s)+1)(eω​(t−s)e−ω​(T−s)(2Ce−ω​(T−s)−C+1)\displaystyle=\frac{\beta\,\Sigma}{2\,(C\,e^{-2\,\omega\,(T-s)}+1)}\biggl(e^{\omega\,(t-s)}\,e^{-\omega\,(T-s)}\,(2\,C\,e^{-\omega(T-s)}-C+1) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−ω​(t−s)((C−1)e−ω​(T−s)+2)).\displaystyle\hskip 28.45274pt+e^{-\omega(t-s)}((C-1)e^{-\omega(T-s)}+2)\biggr)\,. |  |

From this expression we see

|  |  |  |  |
| --- | --- | --- | --- |
|  | limk→0[Φ​(t−s)​uk​(s)]2\displaystyle\lim\_{k\to 0}[\Phi(t-s)\,u\_{k}(s)]\_{2} | ={β​Σ,s=t​ or ​t=T0,s<t<T.\displaystyle=\left\{\begin{array}[]{cl}\beta\,\Sigma\,,&s=t\mbox{ or }t=T\\ 0\,,&s<t<T\end{array}\right.\,. |  |

The Dominated Convergence Theorem may be used to interchange the integral and limit in ([73](https://arxiv.org/html/2601.10812v1#Sx1.E73 "In Appendix A: Proofs for Section 3 (Identity Payoff Function) ‣ Optimal Liquidation of Perpetual Contracts")) which yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | limk→0Var​(At)\displaystyle\lim\_{k\rightarrow 0}\text{Var}(A\_{t}) | ={β2​Σ2​T,t=T0,t<T.\displaystyle=\left\{\begin{array}[]{cl}\beta^{2}\,\Sigma^{2}\,T\,,&t=T\\ 0\,,&t<T\end{array}\right.\,. |  |

Finally the limit in ([19](https://arxiv.org/html/2601.10812v1#S3.E19 "In Proposition 3 ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) holds since

|  |  |  |  |
| --- | --- | --- | --- |
|  | limk→0𝔼​[∫0T(At)2​𝑑t]=limk→0∫0TVar​(At)+𝔼​[At]2​d​t=0.\displaystyle\lim\_{k\to 0}\mathbb{E}\biggl[\int\_{0}^{T}(A\_{t})^{2}\,dt\biggr]=\lim\_{k\to 0}\int\_{0}^{T}\text{Var}(A\_{t})+\mathbb{E}[A\_{t}]^{2}\,dt=0. |  | (74) |

The first claim follows from Fubini’s Theorem and the second claim follows from Dominated Convergence Theorem.
\qed

## Appendix B: Proofs for Section [4](https://arxiv.org/html/2601.10812v1#S4 "4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") (Arbitrary Payoff Function)

The following two Lemmas are used repeatedly in the proofs of the approximation results which appear in this appendix.

###### Lemma 10

Suppose ψ\psi satisfies Assumption [4](https://arxiv.org/html/2601.10812v1#Thmtheorem4 "Assumption 4 ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") i). For an integrable function ζ:ℝ→ℝ\zeta:\mathbb{R}\to\mathbb{R}, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(t,s)=𝔼​[∫tTζ​(u)​ψ​(Su)​𝑑u|St=s],\displaystyle g(t,s)=\mathbb{E}\biggl[\int^{T}\_{t}\zeta(u)\,\psi(S\_{u})\,du\biggl|S\_{t}=s\biggr]\,, |  | (75) |

then g​(t,s)g\left(t,s\right) is Lipschitz with respect to the variable ss, uniformly in tt.

###### Lemma 11

Suppose θ:[0,T]×ℝ→ℝ\theta:[0,T]\times\mathbb{R}\rightarrow\mathbb{R} is continuous with ∂sθ\partial\_{s}\theta continuous and bounded, and suppose ζ:[0,T]→ℝ\zeta:[0,T]\rightarrow\mathbb{R} is integrable. Define

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g1​(t,s)\displaystyle g\_{1}(t,s) | =𝔼​[∫0Tζ​(u)​θ​(u,Su)​𝑑u|St=s],\displaystyle=\mathbb{E}\biggl[\int\_{0}^{T}\zeta(u)\,\theta(u,S\_{u})\,du\biggl|S\_{t}=s\biggr]\,, |  | (76) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g2​(t,s)\displaystyle g\_{2}(t,s) | =𝔼​[∫0Tζ​(u)​θ2​(u,Su)​𝑑u|St=s].\displaystyle=\mathbb{E}\biggl[\int\_{0}^{T}\zeta(u)\,\theta^{2}(u,S\_{u})\,du\biggl|S\_{t}=s\biggr]\,. |  | (77) |

Then ∂sg1\partial\_{s}g\_{1} is bounded and ∂sg2\partial\_{s}g\_{2} has linear growth in ss uniformly in tt.

From the dynamics of SS given in ([2](https://arxiv.org/html/2601.10812v1#S2.E2 "In 2.1 Dynamics ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts")) the transition density of this process between times tt and uu is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p​(z;t,u,s)\displaystyle p(z;t,u,s) | =12​π​σ2​(u−t)​exp⁡(−(z−s)22​σ2​(u−t)),\displaystyle=\frac{1}{\sqrt{2\,\pi\,\sigma^{2}\,(u-t)}}\exp\biggl(-\frac{(z-s)^{2}}{2\,\sigma^{2}\,(u-t)}\biggr)\,, |  | (78) |

By Fubini’s Theorem the function gg can be written

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(t,s)\displaystyle g(t,s) | =∫tTζ​(u)​𝔼​[ψ​(Su)|St=s]​𝑑u\displaystyle=\int\_{t}^{T}\zeta(u)\,\mathbb{E}[\psi(S\_{u})|S\_{t}=s]\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫tTζ​(u)​∫ℝψ​(z)​p​(z;t,u,s)​𝑑z​𝑑u\displaystyle=\int\_{t}^{T}\zeta(u)\int\_{\mathbb{R}}\psi(z)\,p(z;t,u,s)\,dz\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫tTζ​(u)​∫ℝψ​(x+s)​p​(x;t,u,0)​𝑑x​𝑑u.\displaystyle=\int\_{t}^{T}\zeta(u)\int\_{\mathbb{R}}\psi(x+s)\,p(x;t,u,0)\,dx\,du\,. |  |

Thus, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |g​(t,s1)−g​(t,s2)|\displaystyle|g(t,s\_{1})-g(t,s\_{2})| | ≤∫tT|ζ​(u)|​∫ℝ|ψ​(x+s1)−ψ​(x+s2)|​p​(x;t,u,0)​𝑑x​𝑑u.\displaystyle\leq\int\_{t}^{T}|\zeta(u)|\,\int\_{\mathbb{R}}|\psi(x+s\_{1})-\psi(x+s\_{2})|\,p(x;t,u,0)\,dx\,du\,. |  |

The function ψ\psi is Lipschitz because it has continuous bounded first derivative, therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | |g​(t,s1)−g​(t,s2)|\displaystyle|g(t,s\_{1})-g(t,s\_{2})| | ≤∫tT|ζ​(u)|​∫ℝL1​|s1−s2|​p​(x;t,u,0)​𝑑x​𝑑u\displaystyle\leq\int\_{t}^{T}|\zeta(u)|\,\int\_{\mathbb{R}}L\_{1}\,|s\_{1}-s\_{2}|\,p(x;t,u,0)\,dx\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =L1​|s1−s2|​∫tT|ζ​(u)|​𝑑u\displaystyle=L\_{1}\,|s\_{1}-s\_{2}|\,\int\_{t}^{T}|\zeta(u)|\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤L1​|s1−s2|​∫0T|ζ​(u)|​𝑑u\displaystyle\leq L\_{1}\,|s\_{1}-s\_{2}|\,\int\_{0}^{T}|\zeta(u)|\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =L2​|s1−s2|.\displaystyle=L\_{2}\,|s\_{1}-s\_{2}|\,. |  |

\qed

From the dynamics of SS given in ([2](https://arxiv.org/html/2601.10812v1#S2.E2 "In 2.1 Dynamics ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts")) the transition density of this process between times tt and uu is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p​(z;t,u,s)\displaystyle p(z;t,u,s) | =12​π​σ2​(u−t)​exp⁡(−(z−s)22​σ2​(u−t)),\displaystyle=\frac{1}{\sqrt{2\,\pi\,\sigma^{2}\,(u-t)}}\exp\biggl(-\frac{(z-s)^{2}}{2\,\sigma^{2}\,(u-t)}\biggr)\,, |  | (79) |

By Fubini’s Theorem the function g1g\_{1} can be written

|  |  |  |  |
| --- | --- | --- | --- |
|  | g1​(t,s)\displaystyle g\_{1}(t,s) | =∫tTζ​(u)​𝔼​[θ​(u,Su)|St=s]​𝑑u\displaystyle=\int\_{t}^{T}\zeta(u)\,\mathbb{E}[\theta(u,S\_{u})|S\_{t}=s]\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫tTζ​(u)​∫ℝθ​(u,z)​p​(z;t,u,s)​𝑑z​𝑑u\displaystyle=\int\_{t}^{T}\zeta(u)\,\int\_{\mathbb{R}}\theta(u,z)\,p(z;t,u,s)\,dz\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫tTζ​(u)​∫ℝθ​(u,x+s)​p​(x;t,u,0)​𝑑x​𝑑u.\displaystyle=\int\_{t}^{T}\zeta(u)\,\int\_{\mathbb{R}}\theta(u,x+s)\,p(x;t,u,0)\,dx\,du\,. |  |

By the Leibniz integration rule, we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂sg1​(t,s)\displaystyle\partial\_{s}g\_{1}(t,s) | =∫tTζ​(u)​∫ℝ∂sθ​(u,x+s)​p​(x;t,u,0)​d​x​d​u\displaystyle=\int\_{t}^{T}\zeta(u)\,\int\_{\mathbb{R}}\partial\_{s}\theta(u,x+s)\,p(x;t,u,0)\,dx\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |∂sg1​(t,s)|\displaystyle|\partial\_{s}g\_{1}(t,s)| | ≤∫tT|ζ​(u)|​∫ℝ|∂sθ​(u,x+s)|​p​(x;t,u,0)​𝑑x​𝑑u\displaystyle\leq\int\_{t}^{T}|\zeta(u)|\,\int\_{\mathbb{R}}|\partial\_{s}\theta(u,x+s)|\,p(x;t,u,0)\,dx\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​∫0T|ζ​(u)|​𝑑u.\displaystyle\leq K\int\_{0}^{T}|\zeta(u)|\,du\,. |  |

Similarly, we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | g2​(t,s)\displaystyle g\_{2}(t,s) | =∫tTζ​(u)​∫ℝθ2​(u,x+s)​p​(x;t,u,0)​𝑑x​𝑑u\displaystyle=\int\_{t}^{T}\zeta(u)\,\int\_{\mathbb{R}}\theta^{2}(u,x+s)\,p(x;t,u,0)\,dx\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂sg2​(t,s)\displaystyle\partial\_{s}g\_{2}(t,s) | =∫tTζ​(u)​∫ℝ2​θ​(u,x+s)​∂sθ​(u,x+s)​p​(x;t,u,0)​d​x​d​u\displaystyle=\int\_{t}^{T}\zeta(u)\,\int\_{\mathbb{R}}2\,\theta(u,x+s)\partial\_{s}\,\theta(u,x+s)\,p(x;t,u,0)\,dx\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |∂sg2​(t,s)|\displaystyle|\partial\_{s}g\_{2}(t,s)| | ≤∫tT|ζ​(u)|​∫ℝ2​|θ​(u,x+s)|​|∂sθ​(u,x+s)|​p​(x;t,u,0)​𝑑x​𝑑u.\displaystyle\leq\int\_{t}^{T}|\zeta(u)|\,\int\_{\mathbb{R}}2\,|\theta(u,x+s)||\partial\_{s}\,\theta(u,x+s)|\,p(x;t,u,0)\,dx\,du\,. |  |

Since ∂sθ\partial\_{s}\theta is continuous and bounded, θ\theta has linear growth in ss uniformly in tt and we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∂sg2​(t,s)|\displaystyle|\partial\_{s}g\_{2}(t,s)| | ≤K​∫0T|ζ​(u)|​∫ℝ(1+|x+s|)​p​(x;t,u,0)​𝑑x​𝑑u\displaystyle\leq K\int\_{0}^{T}|\zeta(u)|\,\int\_{\mathbb{R}}(1+|x+s|)\,p(x;t,u,0)\,dx\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​∫0T|ζ​(u)|​∫ℝ(1+|x|)​p​(x;t,u,0)​𝑑x​𝑑u+K​∫0T|ζ​(u)|​∫ℝ|s|​p​(x;t,u,0)​𝑑x​𝑑u\displaystyle\leq K\int\_{0}^{T}|\zeta(u)|\,\int\_{\mathbb{R}}(1+|x|)\,p(x;t,u,0)\,dx\,du+K\,\int\_{0}^{T}|\zeta(u)|\,\int\_{\mathbb{R}}|s|\,p(x;t,u,0)\,dx\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K′​(1+|s|).\displaystyle\leq K^{\prime}(1+|s|)\,. |  |

\qed

Part I (formal solution): Substituting h^ψ\widehat{h}\_{\psi} into the left hand side of ([23](https://arxiv.org/html/2601.10812v1#S4.E23 "In 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) and setting terms proportional to β0\beta^{0} to vanish gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂th0−ϕ​q2+14​k​(∂qh0+b​q)2=0,\displaystyle\partial\_{t}h\_{0}-\phi\,q^{2}+\frac{1}{4\,k}\,(\partial\_{q}h\_{0}+b\,q)^{2}=0\,, |  | (80) |

with terminal condition h0​(T,q)=−α​q2h\_{0}(T,q)=-\alpha\,q^{2}. It is easily verified that this equation has solution given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h0​(t,q)\displaystyle h\_{0}(t,q) | =γ​(t)​q2,\displaystyle=\gamma(t)\,q^{2}\,, |  | (81) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ​(t)\displaystyle\gamma(t) | =−a~2​C~​e−2​ω~​(T−t)−1C~​e−2​ω~​(T−t)+1−b2,\displaystyle=-\frac{\widetilde{a}}{2}\frac{\widetilde{C}e^{-2\,\widetilde{\omega}\,(T-t)}-1}{\widetilde{C}\,e^{-2\,\widetilde{\omega}\,(T-t)}+1}-\frac{b}{2}\,, |  | (82) |

with a~\widetilde{a}, C~\widetilde{C}, and ω~\widetilde{\omega} as in the statement of the theorem. Similarly, grouping terms proportional to β1\beta^{1} gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂th1,ψ+12​(σ2​∂s​sh1,ψ+η2​∂p​ph1,ψ+2​ρ​σ​η​∂s​ph1,ψ)−q​(p−ψ​(s))+12​k​(∂qh1,ψ+b​∂ph1,ψ)​(∂qh0+b​q)=0,\displaystyle\begin{split}\partial\_{t}h\_{1,\psi}+\frac{1}{2}\,(\sigma^{2}\,\partial\_{ss}h\_{1,\psi}+\eta^{2}\,\partial\_{pp}h\_{1,\psi}+2\,\rho\,\sigma\,\eta\,\partial\_{sp}h\_{1,\psi})-q\,(p-\psi(s))\\ +\frac{1}{2\,k}(\partial\_{q}h\_{1,\psi}+b\,\partial\_{p}h\_{1,\psi})\,(\partial\_{q}h\_{0}+b\,q)=0\,,\end{split} | |  | (83) |

with terminal condition h1,ψ​(T,q,p,s)=0h\_{1,\psi}(T,q,p,s)=0. We now write h1,ψ​(t,q,p,s)h\_{1,\psi}(t,q,p,s) in the form h1,ψ​(t,q,p,s)=γ0,ψ​(t,s)​q+γ1​(t)​q​p+γ2​(t)​q2h\_{1,\psi}(t,q,p,s)=\gamma\_{0,\psi}(t,s)\,q+\gamma\_{1}(t)\,q\,p+\gamma\_{2}(t)\,q^{2}, substitute this into ([83](https://arxiv.org/html/2601.10812v1#Sx2.E83 "In Appendix B: Proofs for Section 4 (Arbitrary Payoff Function) ‣ Optimal Liquidation of Perpetual Contracts")) and set the qq, q​pq\,p and q2q^{2} terms to vanish independently, obtaining

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂tγ0,ψ+12​σ2​∂s​sγ0,ψ+ψ​(s)+12​k​(2​γ+b)​γ0,ψ\displaystyle\partial\_{t}\gamma\_{0,\psi}+\frac{1}{2}\,\sigma^{2}\,\partial\_{ss}\gamma\_{0,\psi}+\psi(s)+\frac{1}{2\,k}\,(2\,\gamma+b)\,\gamma\_{0,\psi} | =0,\displaystyle=0\,, |  | (84) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂tγ1−1+12​k​(2​γ+b)​γ1\displaystyle\partial\_{t}\gamma\_{1}-1+\frac{1}{2\,k}\,(2\,\gamma+b)\,\gamma\_{1} | =0,\displaystyle=0\,, |  | (85) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂tγ2+12​k​(2​γ+b)​(b​γ1+2​γ2)\displaystyle\partial\_{t}\gamma\_{2}+\frac{1}{2\,k}\,(2\,\gamma+b)\,(b\,\gamma\_{1}+2\,\gamma\_{2}) | =0,\displaystyle=0\,, |  | (86) |

with terminal conditions γ0,ψ​(T,s)=γ1​(T)=γ2​(T)=0\gamma\_{0,\psi}(T,s)=\gamma\_{1}(T)=\gamma\_{2}(T)=0. The solutions to the ODEs for γ1\gamma\_{1} and γ2\gamma\_{2} are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ1​(t)\displaystyle\gamma\_{1}(t) | =(C~​e−ω~​(T−t)+1)​(e−ω~​(T−t)−1)ω~​(C~​e−2​ω~​(T−t)+1),\displaystyle=\frac{(\widetilde{C}\,e^{-\widetilde{\omega}\,(T-t)}+1)\,(e^{-\widetilde{\omega}\,(T-t)}-1)}{\widetilde{\omega}\,(\widetilde{C}\,e^{-2\,\widetilde{\omega}\,(T-t)}+1)}\,, |  | (87) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ2​(t)=−b​e−2​ω~​(T−t)2​ω~​(C~​e−2​ω~​(T−t)+1)2(4ω~C~(T−t)−2(1−C~)(1−eω~​(T−t))+2(C~2−C~)(1−e−ω~​(T−t))+(1−e2​ω~​(T−t))−C~2(1−e−2​ω~​(T−t))),\displaystyle\begin{split}\gamma\_{2}(t)&=\frac{-b\,e^{-2\,\widetilde{\omega}\,(T-t)}}{2\,\widetilde{\omega}\,(\widetilde{C}\,e^{-2\,\widetilde{\omega}\,(T-t)}+1)^{2}}\,\biggl(4\,\widetilde{\omega}\,\widetilde{C}\,(T-t)-2\,(1-\widetilde{C})\,(1-e^{\widetilde{\omega}\,(T-t)})\\ &\hskip 28.45274pt+2(\widetilde{C}^{2}-\widetilde{C})\,(1-e^{-\widetilde{\omega}\,(T-t)})+(1-e^{2\,\widetilde{\omega}\,(T-t)})-\widetilde{C}^{2}\,(1-e^{-2\,\widetilde{\omega}\,(T-t)})\biggr)\,,\end{split} | |  | (88) |

and by the Feynman-Kac formula, the solution to the PDE of γ0,ψ\gamma\_{0,\psi} is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ0,ψ​(t,s)\displaystyle\gamma\_{0,\psi}(t,s) | =∫tTC~​e−ω~​(T−u)+eω~​(T−u)C~​e−ω~​(T−t)+eω~​(T−t)​𝔼​[ψ​(Su)|St=s]​𝑑u.\displaystyle=\int\_{t}^{T}\frac{\widetilde{C}\,e^{-\widetilde{\omega}\,(T-u)}+e^{\widetilde{\omega}\,(T-u)}}{\widetilde{C}\,e^{-\widetilde{\omega}\,(T-t)}+e^{\widetilde{\omega}\,(T-t)}}\,\mathbb{E}[\psi(S\_{u})|S\_{t}=s]\,du\,. |  | (89) |

Finally, grouping the terms proportional to β2\beta^{2} and setting them equal to zero gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂th2,ψ+12​k​(∂qh2,ψ+b​∂ph2,ψ)​(2​γ+b)​q+14​k​(γ0,ψ+γ1​p+(b​γ1+2​γ2)​q)2+12​(σ2​∂s​sh2,ψ+η2​∂p​ph2,ψ+2​ρ​σ​η​∂s​ph2,ψ)=0,\displaystyle\begin{split}\partial\_{t}h\_{2,\psi}+\frac{1}{2\,k}\,(\partial\_{q}h\_{2,\psi}+b\,\partial\_{p}h\_{2,\psi})\,(2\,\gamma+b)\,q+\frac{1}{4\,k}\,(\gamma\_{0,\psi}+\gamma\_{1}\,p+(b\,\gamma\_{1}+2\,\gamma\_{2})\,q)^{2}\\ +\frac{1}{2}\,(\sigma^{2}\,\partial\_{ss}h\_{2,\psi}+\eta^{2}\,\partial\_{pp}h\_{2,\psi}+2\,\rho\,\sigma\,\eta\,\partial\_{sp}h\_{2,\psi})&=0\,,\end{split} | |  | (90) |

with terminal condition h2,ψ​(T,q,p,s)=0h\_{2,\psi}(T,q,p,s)=0. Writing h2,ψh\_{2,\psi} in the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h2,ψ​(t,q,p,s)\displaystyle h\_{2,\psi}(t,q,p,s) | =λ0​(t,s)+λ1​(t,s)​q+λ2​(t)​q2+λ3​(t)​q​p+λ4​(t,s)​p+λ5​(t)​p2,\displaystyle=\lambda\_{0}(t,s)+\lambda\_{1}(t,s)\,q+\lambda\_{2}(t)\,q^{2}+\lambda\_{3}(t)\,q\,p+\lambda\_{4}(t,s)\,p+\lambda\_{5}(t)\,p^{2}\,, |  | (91) |

substituting into ([90](https://arxiv.org/html/2601.10812v1#Sx2.E90 "In Appendix B: Proofs for Section 4 (Arbitrary Payoff Function) ‣ Optimal Liquidation of Perpetual Contracts")), and grouping terms by like powers shows that {λi}i=0,…,5\{\lambda\_{i}\}\_{i=0,\dots,5} satisfies the system of differential equations

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂tλ0+12​σ2​∂s​sλ0+ρ​σ​η​∂sλ4+η2​λ5+γ0,ψ24​k\displaystyle\partial\_{t}\lambda\_{0}+\frac{1}{2}\,\sigma^{2}\,\partial\_{ss}\lambda\_{0}+\rho\,\sigma\,\eta\,\partial\_{s}\lambda\_{4}+\eta^{2}\,\lambda\_{5}+\frac{\gamma\_{0,\psi}^{2}}{4\,k} | =0,\displaystyle=0\,, | λ0​(T,s)\displaystyle\lambda\_{0}(T,s) | =0,\displaystyle=0\,, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂tλ1+12​σ2​∂s​sλ1+2​γ+b2​k​λ1+b​(2​γ+b)2​k​λ4+(b​γ1+2​γ2)​γ0,ψ2​k\displaystyle\partial\_{t}\lambda\_{1}+\frac{1}{2}\,\sigma^{2}\,\partial\_{ss}\lambda\_{1}+\frac{2\,\gamma+b}{2\,k}\,\lambda\_{1}+\frac{b\,(2\,\gamma+b)}{2\,k}\,\lambda\_{4}+\frac{(b\,\gamma\_{1}+2\,\gamma\_{2})\,\gamma\_{0,\psi}}{2\,k} | =0,\displaystyle=0\,, | λ1​(T,s)\displaystyle\lambda\_{1}(T,s) | =0,\displaystyle=0\,, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | λ2′+2​γ+bk​λ2+b​(2​γ+b)2​k​λ3+(b​γ1+2​γ2)24​k\displaystyle\lambda\_{2}^{\prime}+\frac{2\,\gamma+b}{k}\,\lambda\_{2}+\frac{b\,(2\,\gamma+b)}{2\,k}\,\lambda\_{3}+\frac{(b\,\gamma\_{1}+2\,\gamma\_{2})^{2}}{4\,k} | =0,\displaystyle=0\,, | λ2​(T)\displaystyle\lambda\_{2}(T) | =0,\displaystyle=0\,, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | λ3′+2​γ+b2​k​λ3+b​(2​γ+b)k​λ5+(b​γ1+2​γ2)​γ12​k\displaystyle\lambda\_{3}^{\prime}+\frac{2\,\gamma+b}{2\,k}\,\lambda\_{3}+\frac{b\,(2\,\gamma+b)}{k}\,\lambda\_{5}+\frac{(b\,\gamma\_{1}+2\,\gamma\_{2})\,\gamma\_{1}}{2\,k} | =0,\displaystyle=0\,, | λ3​(T)\displaystyle\lambda\_{3}(T) | =0,\displaystyle=0\,, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂tλ4+12​σ2​∂s​sλ4+γ0,ψ​γ12​k\displaystyle\partial\_{t}\lambda\_{4}+\frac{1}{2}\,\sigma^{2}\,\partial\_{ss}\lambda\_{4}+\frac{\gamma\_{0,\psi}\,\gamma\_{1}}{2\,k} | =0,\displaystyle=0\,, | λ4​(T,s)\displaystyle\lambda\_{4}(T,s) | =0,\displaystyle=0\,, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | λ5′+γ124​k\displaystyle\lambda\_{5}^{\prime}+\frac{\gamma\_{1}^{2}}{4\,k} | =0,\displaystyle=0\,, | λ5​(T)\displaystyle\lambda\_{5}(T) | =0.\displaystyle=0\,. |  |

The solution for each λi\lambda\_{i} can be written using the Feynman-Kac formula, and then by Lemma [11](https://arxiv.org/html/2601.10812v1#Thmtheorem11 "Lemma 11 ‣ Appendix B: Proofs for Section 4 (Arbitrary Payoff Function) ‣ Optimal Liquidation of Perpetual Contracts") we see that ∂sλ1\partial\_{s}\lambda\_{1} and ∂sλ4\partial\_{s}\lambda\_{4} are continuous and bounded, and thus λ1\lambda\_{1} and λ4\lambda\_{4} have linear growth in ss uniformly in tt. Additionally from Lemma [11](https://arxiv.org/html/2601.10812v1#Thmtheorem11 "Lemma 11 ‣ Appendix B: Proofs for Section 4 (Arbitrary Payoff Function) ‣ Optimal Liquidation of Perpetual Contracts"), ∂sλ0\partial\_{s}\lambda\_{0} has linear growth in ss uniformly in tt.

Part II: (accuracy of approximation).
With h^ψ\widehat{h}\_{\psi} as given in the theorem, define

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H^ψ​(t,x,q,p,s;β)\displaystyle\widehat{H}\_{\psi}(t,x,q,p,s;\beta) | =x+q​p+h^ψ​(t,q,p,s;β).\displaystyle=x+q\,p+\widehat{h}\_{\psi}(t,q,p,s;\beta)\,. |  | (92) |

For simplicity, we prove the approximation holds for t=0t=0 with initial states given by xx, qq, pp, and ss. The case of t≠0t\neq 0 follows similarly. Let νβ,ϵ\nu^{\beta,\epsilon} be an admissible control which is ϵ​β2\epsilon\,\beta^{2}-optimal. Specifically, the control satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hνβ,ϵ​(0,x,q,p,s;β)+ϵ​β2≥Hψ​(0,x,q,p,s;β).\displaystyle H^{\nu^{\beta,\epsilon}}(0,x,q,p,s;\beta)+\epsilon\,\beta^{2}\geq H\_{\psi}(0,x,q,p,s;\beta)\,. |  | (93) |

Define the process GG by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt=H^ψ​(t,Xtνβ,ϵ,Qtνβ,ϵ,Ptνβ,ϵ,St;β)−∫0tϕ​(Quνβ,ϵ)2​𝑑u,\displaystyle G\_{t}=\widehat{H}\_{\psi}(t,X\_{t}^{\nu^{\beta,\epsilon}},Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t};\beta)-\int\_{0}^{t}\phi\,(Q\_{u}^{\nu^{\beta,\epsilon}})^{2}\,du\,, |  | (94) |

and apply Itô’s Lemma to obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | GT−G0=∫0T(∂t+ℒνβ,ϵ)​H^ψ​(t,Xtνβ,ϵ,Qtνβ,ϵ,Ptνβ,ϵ,St;β)−ϕ​(Qtνβ,ϵ)2​d​t+∫0Tσ​∂sH^ψ​(t,Xtνβ,ϵ,Qtνβ,ϵ,Ptνβ,ϵ,St;β)​d​Wts+∫0Tη​∂pH^ψ​(t,Xtνβ,ϵ,Qtνβ,ϵ,Ptνβ,ϵ,St;β)​d​Wtp,\displaystyle\begin{split}G\_{T}-G\_{0}&=\int\_{0}^{T}(\partial\_{t}+\mathcal{L}^{\nu^{\beta,\epsilon}})\,\widehat{H}\_{\psi}(t,X\_{t}^{\nu^{\beta,\epsilon}},Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t};\beta)-\phi\,\,(Q\_{t}^{\nu^{\beta,\epsilon}})^{2}dt\\ &\hskip 14.22636pt+\int\_{0}^{T}\sigma\,\partial\_{s}\widehat{H}\_{\psi}(t,X\_{t}^{\nu^{\beta,\epsilon}},Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t};\beta)\,dW^{s}\_{t}\\ &\hskip 14.22636pt+\int\_{0}^{T}\eta\,\partial\_{p}\widehat{H}\_{\psi}(t,X\_{t}^{\nu^{\beta,\epsilon}},Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t};\beta)\,dW^{p}\_{t}\,,\end{split} | |  | (95) |

where the differential operator ℒν\mathcal{L}^{\nu} is given in section [2.2](https://arxiv.org/html/2601.10812v1#S2.SS2 "2.2 Performance Criterion ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts"). The two stochastic integrands are computed explicitly as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂sH^ψ​(t,x,q,p,s;β)\displaystyle\partial\_{s}\widehat{H}\_{\psi}(t,x,q,p,s;\beta) | =β​∂sγ0​(t,s)​q+β2​(∂sλ0​(t,s)+∂sλ1​(t,s)​q+∂sλ4​(t,s)​p),\displaystyle=\beta\,\partial\_{s}\gamma\_{0}(t,s)\,q+\beta^{2}\biggl(\partial\_{s}\lambda\_{0}(t,s)+\partial\_{s}\lambda\_{1}(t,s)\,q+\partial\_{s}\lambda\_{4}(t,s)\,p\biggr)\,, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂pH^ψ​(t,x,q,p,s;β)\displaystyle\partial\_{p}\widehat{H}\_{\psi}(t,x,q,p,s;\beta) | =q+β​γ1​(t)​q+β2​(λ3​(t)​q+λ4​(t,s)+2​λ5​(t)​p).\displaystyle=q+\beta\,\gamma\_{1}(t)\,q+\beta^{2}\biggl(\lambda\_{3}(t)\,q+\lambda\_{4}(t,s)+2\,\lambda\_{5}(t)\,p\biggr)\,. |  |

Lemma [11](https://arxiv.org/html/2601.10812v1#Thmtheorem11 "Lemma 11 ‣ Appendix B: Proofs for Section 4 (Arbitrary Payoff Function) ‣ Optimal Liquidation of Perpetual Contracts") implies that these stochastic integrands satisfy linear growth conditions, and therefore are square integrable for all admissible controls and the stochastic integrals are martingales. Thus, taking an expectation yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[GT]−G0\displaystyle\mathbb{E}[G\_{T}]-G\_{0} | =𝔼​[∫0T(∂t+ℒνβ,ϵ)​H^ψ​(t,Xtνβ,ϵ,Qtνβ,ϵ,Ptνβ,ϵ,St;β)−ϕ​(Qtνβ,ϵ)2​d​t].\displaystyle=\mathbb{E}\biggl[\int\_{0}^{T}(\partial\_{t}+\mathcal{L}^{\nu^{\beta,\epsilon}})\,\widehat{H}\_{\psi}(t,X\_{t}^{\nu^{\beta,\epsilon}},Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t};\beta)-\phi\,\,(Q\_{t}^{\nu^{\beta,\epsilon}})^{2}dt\biggr]\,. |  |

Given the explicit form of H^\widehat{H}, we obtain the bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∂t+ℒνβ,ϵ)​H^ψ​(t,x,q,p,s;β)−ϕ​q2\displaystyle\biggl(\partial\_{t}+\mathcal{L}^{\nu^{\beta,\epsilon}}\biggr)\,\widehat{H}\_{\psi}(t,x,q,p,s;\beta)-\phi\,q^{2} | ≤supν(∂t+ℒν)​H^ψ​(t,x,q,p,s;β)−ϕ​q2\displaystyle\leq\sup\_{\nu}\biggl(\partial\_{t}+\mathcal{L}^{\nu}\biggr)\,\widehat{H}\_{\psi}(t,x,q,p,s;\beta)-\phi\,q^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =β3​A​(t,q,p,s)+β4​B​(t,q,p,s),\displaystyle=\beta^{3}\,A(t,q,p,s)+\beta^{4}\,B(t,q,p,s)\,, |  |

where the functions AA and BB are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(t,q,p,s)\displaystyle A(t,q,p,s) | =12​k(γ0,ψ(t,s)+γ1(t)p+(bγ1(t)+2γ2(t))q)(λ1(t,s)+bλ4(t,s)\displaystyle=\frac{1}{2\,k}\,\biggl(\gamma\_{0,\psi}(t,s)+\gamma\_{1}(t)\,p+\bigl(b\,\gamma\_{1}(t)+2\,\gamma\_{2}(t)\bigr)\,q\biggr)\,\biggl(\lambda\_{1}(t,s)+b\,\lambda\_{4}(t,s) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(λ3(t)+2bλ5(t))p+(2λ2(t)+bλ3(t))q),\displaystyle\hskip 142.26378pt+\bigl(\lambda\_{3}(t)+2\,b\,\lambda\_{5}(t)\bigr)\,p+\bigl(2\,\lambda\_{2}(t)+b\,\lambda\_{3}(t)\bigr)\,q\biggr)\,, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(t,q,p,s)\displaystyle B(t,q,p,s) | =14​k​(λ1​(t,s)+b​λ4​(t,s)+(λ3​(t)+2​b​λ5​(t))​p+(2​λ2​(t)+b​λ3​(t))​q)2.\displaystyle=\frac{1}{4\,k}\,\biggl(\lambda\_{1}(t,s)+b\,\lambda\_{4}(t,s)+\bigl(\lambda\_{3}(t)+2\,b\,\lambda\_{5}(t)\bigr)\,p+\bigl(2\,\lambda\_{2}(t)+b\,\lambda\_{3}(t)\bigr)\,q\biggr)^{2}\,. |  |

The aforementioned growth conditions on the functions γ0,ψ\gamma\_{0,\psi}, λ0\lambda\_{0}, λ1\lambda\_{1}, and λ4\lambda\_{4} imply that the functions AA and BB satisfy quadratic growth conditions in the variables qq, pp, and ss. Recalling the definition of GG, this gives

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[H^ψ​(T,XTνβ,ϵ,QTνβ,ϵ,PTνβ,ϵ,ST;β)−∫0Tϕ​(Qtνβ,ϵ)2​𝑑t]−H^ψ​(0,x,q,p,s;β)\displaystyle\mathbb{E}\biggl[\widehat{H}\_{\psi}(T,X\_{T}^{\nu^{\beta,\epsilon}},Q\_{T}^{\nu^{\beta,\epsilon}},P\_{T}^{\nu^{\beta,\epsilon}},S\_{T};\beta)-\int\_{0}^{T}\phi\,(Q\_{t}^{\nu^{\beta,\epsilon}})^{2}\,dt\biggr]-\widehat{H}\_{\psi}(0,x,q,p,s;\beta) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤β3​𝔼​[∫0TA​(t,Qtνβ,ϵ,Ptνβ,ϵ,St)+β​B​(t,Qtνβ,ϵ,Ptνβ,ϵ,St)​d​t]\displaystyle\hskip 113.81102pt\leq\beta^{3}\,\mathbb{E}\biggl[\int\_{0}^{T}A(t,Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t})+\beta\,B(t,Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t})\,dt\biggr] |  |
|  |  |  |
| --- | --- | --- |
|  | 𝔼​[XTνβ,ϵ+QTνβ,ϵ​(PTνβ,ϵ−α​QTνβ,ϵ)−∫0Tϕ​(Qtνβ,ϵ)2​𝑑t]−H^ψ​(0,x,q,p,s;β)\displaystyle\mathbb{E}\biggl[X\_{T}^{\nu^{\beta,\epsilon}}+Q\_{T}^{\nu^{\beta,\epsilon}}\,(P\_{T}^{\nu^{\beta,\epsilon}}-\alpha\,Q\_{T}^{\nu^{\beta,\epsilon}})-\int\_{0}^{T}\phi\,(Q\_{t}^{\nu^{\beta,\epsilon}})^{2}\,dt\biggr]-\widehat{H}\_{\psi}(0,x,q,p,s;\beta) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤β3​𝔼​[∫0TA​(t,Qtνβ,ϵ,Ptνβ,ϵ,St)+β​B​(t,Qtνβ,ϵ,Ptνβ,ϵ,St)​d​t]\displaystyle\hskip 113.81102pt\leq\beta^{3}\,\mathbb{E}\biggl[\int\_{0}^{T}A(t,Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t})+\beta\,B(t,Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t})\,dt\biggr] |  |
|  |  |  |
| --- | --- | --- |
|  | Hνβ,ϵ​(0,x,q,p,s;β)−H^ψ​(0,x,q,p,s;β)\displaystyle H^{\nu^{\beta,\epsilon}}(0,x,q,p,s;\beta)-\widehat{H}\_{\psi}(0,x,q,p,s;\beta) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤β3​𝔼​[∫0TA​(t,Qtνβ,ϵ,Ptνβ,ϵ,St)+β​B​(t,Qtνβ,ϵ,Ptνβ,ϵ,St)​d​t].\displaystyle\hskip 113.81102pt\leq\beta^{3}\,\mathbb{E}\biggl[\int\_{0}^{T}A(t,Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t})+\beta\,B(t,Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t})\,dt\biggr]\,. |  |

Recalling the definition of νβ,ϵ\nu^{\beta,\epsilon} gives

|  |  |  |
| --- | --- | --- |
|  | Hψ​(0,x,q,p,s;β)−H^ψ​(0,x,q,p,s;β)\displaystyle H\_{\psi}(0,x,q,p,s;\beta)-\widehat{H}\_{\psi}(0,x,q,p,s;\beta) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤ϵ​β2+β3​𝔼​[∫0TA​(t,Qtνβ,ϵ,Ptνβ,ϵ,St)+β​B​(t,Qtνβ,ϵ,Ptνβ,ϵ,St)​d​t].\displaystyle\hskip 113.81102pt\leq\epsilon\,\beta^{2}+\beta^{3}\,\mathbb{E}\biggl[\int\_{0}^{T}A(t,Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t})+\beta\,B(t,Q\_{t}^{\nu^{\beta,\epsilon}},P\_{t}^{\nu^{\beta,\epsilon}},S\_{t})\,dt\biggr]\,. |  |

By Assumption [4](https://arxiv.org/html/2601.10812v1#Thmtheorem4 "Assumption 4 ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") ii) and the growth conditions on the functions AA and BB, the expectation is uniformly bounded by a constant CC for all sufficiently small ϵ\epsilon and β\beta, giving

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Hψ​(0,x,q,p,s;β)−H^ψ​(0,x,q,p,s;β)|β2\displaystyle\frac{|H\_{\psi}(0,x,q,p,s;\beta)-\widehat{H}\_{\psi}(0,x,q,p,s;\beta)|}{\beta^{2}} | ≤ϵ+β​C.\displaystyle\leq\epsilon+\beta\,C\,. |  |

Since ϵ>0\epsilon>0 is arbitrary, the desired limit follows. \qed

Consider the inventory and perpetual contract price when the agents follows the conjectured approximate strategy, specifically such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Qtν^\displaystyle dQ\_{t}^{\widehat{\nu}} | =ν^​(t,Qtν^,Ptν^,St;β)​d​t,\displaystyle=\widehat{\nu}(t,Q^{\widehat{\nu}}\_{t},P^{\widehat{\nu}}\_{t},S\_{t};\beta)\,dt\,, |  | (96) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Ptν^\displaystyle dP^{\widehat{\nu}}\_{t} | =b​ν^​(t,Qtν^,Ptν^,St;β)​d​t+η​d​Wtp.\displaystyle=b\,\widehat{\nu}(t,Q^{\widehat{\nu}}\_{t},P^{\widehat{\nu}}\_{t},S\_{t};\beta)\,dt+\eta\,dW\_{t}^{p}\,. |  | (97) |

By Theorem [5](https://arxiv.org/html/2601.10812v1#Thmtheorem5 "Theorem 5 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"), the function ν^\widehat{\nu} may be written as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν^​(t,q,p,s;β)\displaystyle\widehat{\nu}(t,q,p,s;\beta) | =F1​(t;β)​q+F2​(t;β)​p+β2​k​γ0,ψ​(t,s),\displaystyle=F\_{1}(t;\beta)\,q+F\_{2}(t;\beta)\,p+\frac{\beta}{2\,k}\,\gamma\_{0,\psi}(t,s)\,, |  | (98) |

where F1F\_{1} and F2F\_{2} are bounded. Therefore ν^\widehat{\nu} is Lipschitz with linear growth in variables qq, pp and ss by Lemma [10](https://arxiv.org/html/2601.10812v1#Thmtheorem10 "Lemma 10 ‣ Appendix B: Proofs for Section 4 (Arbitrary Payoff Function) ‣ Optimal Liquidation of Perpetual Contracts"). Thus, the SDEs for Qν^Q^{\widehat{\nu}} and Pν^P^{\widehat{\nu}} have a unique strong solution (see Theorem 5.2.9 in Karatzas and
Shreve ([1991](https://arxiv.org/html/2601.10812v1#bib.bib16))). Moreover, there exists a constant M^\widehat{M}, such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[(Qtν^)2+(Ptν^)2]\displaystyle\mathbb{E}\biggl[(Q\_{t}^{\widehat{\nu}})^{2}+(P\_{t}^{\widehat{\nu}})^{2}\biggr] | ≤M^​eM^​t,∀t∈[0,T].\displaystyle\leq\widehat{M}\,e^{\widehat{M}\,t}\,,\qquad\forall t\in[0,T]\,. |  | (99) |

Therefore, by Fubini’s Theorem, we have 𝔼​[∫0Tν^u2​𝑑t]<∞\mathbb{E}[\int\_{0}^{T}\widehat{\nu}\_{u}^{2}\,dt]<\infty and ν^\widehat{\nu} is an admissible control.

To show that ν^\widehat{\nu} is asymptotically optimal, we proceed with a verification argument while keeping track of the magnitude of the error with respect to optimization, analogous to the proof of Theorem [5](https://arxiv.org/html/2601.10812v1#Thmtheorem5 "Theorem 5 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). We also remark that with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Hψ​(t,x,q,p,s;β)\displaystyle H\_{\psi}(t,x,q,p,s;\beta) | =x+q​p+hψ​(t,q,p,s;β),\displaystyle=x+q\,p+h\_{\psi}(t,q,p,s;\beta)\,, |  | (100) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Hψν^​(t,x,q,p,s;β)\displaystyle H\_{\psi}^{\widehat{\nu}}(t,x,q,p,s;\beta) | =x+q​p+hψν^​(t,q,p,s;β),\displaystyle=x+q\,p+h\_{\psi}^{\widehat{\nu}}(t,q,p,s;\beta)\,, |  | (101) |

our desired approximation result is equivalent to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limβ→0Hψ​(t,x,q,p,s;β)−Hψν^​(t,x,q,p,s;β)β2\displaystyle\lim\_{\beta\rightarrow 0}\frac{H\_{\psi}(t,x,q,p,s;\beta)-H\_{\psi}^{\widehat{\nu}}(t,x,q,p,s;\beta)}{\beta^{2}} | =0.\displaystyle=0\,. |  | (102) |

We prove the accuracy result at t=0t=0 with given initial states xx, qq, pp and ss, which we henceforth consider to be fixed. The general result for t≠0t\neq 0 follows similarly. Given the control ν^\widehat{\nu}, and the resulting state processes Xν^X^{\widehat{\nu}}, Qν^Q^{\widehat{\nu}}, Pν^P^{\widehat{\nu}} and SS, define the process G=(Gt)t∈[0,T]G=(G\_{t})\_{t\in[0,T]} by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Gt\displaystyle G\_{t} | =Xtν^+Qtν^​Ptν^+h^ψ​(t,Qtν^,Ptν^,St;β)−∫0tϕ​(Quν^)2​𝑑u,\displaystyle=X\_{t}^{\widehat{\nu}}+Q\_{t}^{\widehat{\nu}}\,P\_{t}^{\widehat{\nu}}+\widehat{h}\_{\psi}(t,Q\_{t}^{\widehat{\nu}},P\_{t}^{\widehat{\nu}},S\_{t};\beta)-\int\_{0}^{t}\phi\,(Q\_{u}^{\widehat{\nu}})^{2}\,du\,, |  | (103) |

where h^ψ\widehat{h}\_{\psi} is the approximation of hψh\_{\psi} given in Theorem [5](https://arxiv.org/html/2601.10812v1#Thmtheorem5 "Theorem 5 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). Applying Itô’s Lemma to GG gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | GT−G0=∫0T(∂t+ℒν^)​H^ψ​(t,Xtν^,Qtν^,Ptν^,St;β)−ϕ​(Qtν^)2​d​t+∫0Tσ​∂sH^ψ​(t,Xtν^,Qtν^,Ptν^,St;β)​d​Wts+∫0Tη​∂pH^ψ​(t,Xtν^,Qtν^,Ptν^,St;β)​d​Wtp.\displaystyle\begin{split}G\_{T}-G\_{0}=&\int\_{0}^{T}(\partial\_{t}+\mathcal{L}^{\widehat{\nu}})\,\widehat{H}\_{\psi}(t,X\_{t}^{\widehat{\nu}},Q\_{t}^{\widehat{\nu}},P\_{t}^{\widehat{\nu}},S\_{t};\beta)-\phi\,(Q\_{t}^{\widehat{\nu}})^{2}\,dt\\ &+\int\_{0}^{T}\sigma\,\partial\_{s}\widehat{H}\_{\psi}(t,X\_{t}^{\widehat{\nu}},Q\_{t}^{\widehat{\nu}},P\_{t}^{\widehat{\nu}},S\_{t};\beta)\,dW^{s}\_{t}\\ &+\int\_{0}^{T}\eta\,\partial\_{p}\widehat{H}\_{\psi}(t,X\_{t}^{\widehat{\nu}},Q\_{t}^{\widehat{\nu}},P\_{t}^{\widehat{\nu}},S\_{t};\beta)\,dW^{p}\_{t}\,.\end{split} | |  | (104) |

The growth conditions established on the stochastic integrands in the proof of Theorem [5](https://arxiv.org/html/2601.10812v1#Thmtheorem5 "Theorem 5 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") mean that the stochastic integrals are martingales. Thus, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[GT]−G0\displaystyle\mathbb{E}[G\_{T}]-G\_{0} | =𝔼​[∫0T(∂t+ℒν^)​H^ψ​(t,Xtν^,Qtν^,Ptν^,St;β)−ϕ​(Qtν^)2​d​t].\displaystyle=\mathbb{E}\biggl[\int\_{0}^{T}(\partial\_{t}+\mathcal{L}^{\widehat{\nu}})\,\widehat{H}\_{\psi}(t,X\_{t}^{\widehat{\nu}},Q\_{t}^{\widehat{\nu}},P\_{t}^{\widehat{\nu}},S\_{t};\beta)-\phi\,(Q\_{t}^{\widehat{\nu}})^{2}\,dt\biggr]\,. |  | (105) |

By fully expanding the integrand using the expressions in Theorem [5](https://arxiv.org/html/2601.10812v1#Thmtheorem5 "Theorem 5 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∂t+ℒν^)​H^ψ​(t,Xtν^,Qtν^,Ptν^,St;β)−ϕ​(Qtν^)2=β3​A3​(t,Qtν^,Ptν^,St),\displaystyle(\partial\_{t}+\mathcal{L}^{\widehat{\nu}})\,\widehat{H}\_{\psi}(t,X\_{t}^{\widehat{\nu}},Q\_{t}^{\widehat{\nu}},P\_{t}^{\widehat{\nu}},S\_{t};\beta)-\phi\,(Q\_{t}^{\widehat{\nu}})^{2}=\beta^{3}\,A\_{3}(t,Q\_{t}^{\widehat{\nu}},P\_{t}^{\widehat{\nu}},S\_{t})\,, |  | (106) |

where the function A3A\_{3} is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A3​(t,q,p,s)=12​k(γ0,ψ(t,s)+(2γ2(t)+bγ1(t))q+γ1(t)p)(λ1(t,s)+bλ4(t,s)+(2λ2(t)+bλ3(t))q+(λ3(t)+2bλ5(t))p).\displaystyle\begin{split}A\_{3}(t,q,p,s)&=\frac{1}{2\,k}\biggl(\gamma\_{0,\psi}(t,s)+(2\,\gamma\_{2}(t)+b\,\gamma\_{1}(t))\,q+\gamma\_{1}(t)\,p\biggr)\biggl(\lambda\_{1}(t,s)+b\,\lambda\_{4}(t,s)\\ &\hskip 99.58464pt+(2\,\lambda\_{2}(t)+b\,\lambda\_{3}(t))\,q+(\lambda\_{3}(t)+2\,b\,\lambda\_{5}(t))\,p\biggr)\,.\end{split} | |  | (107) |

Previously established growth conditions of all terms on the right hand side and the fact that ν^\widehat{\nu} is an admissible control imply that for sufficiently small β\beta

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | β3​𝔼​[∫0T|A3​(t,Qtν^,Ptν^,St)|​𝑑t]\displaystyle\beta^{3}\,\mathbb{E}\biggl[\int\_{0}^{T}|A\_{3}(t,Q\_{t}^{\widehat{\nu}},P\_{t}^{\widehat{\nu}},S\_{t})|\,dt\biggr] | ≤β3​C,\displaystyle\leq\beta^{3}\,C\,, |  | (108) |

where CC is a finite constant that does not depend on β\beta. Thus, recalling the definition of GG we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼​[XTν^+QTν^​PTν^+h^​(T,QTν^,PTν^,ST;β)−∫0Tϕ​(Qtν^)2​𝑑t]−H^ψ​(0,x,q,p,s;β)|\displaystyle\biggl|\mathbb{E}\biggl[X\_{T}^{\widehat{\nu}}+Q\_{T}^{\widehat{\nu}}\,P\_{T}^{\widehat{\nu}}+\widehat{h}(T,Q\_{T}^{\widehat{\nu}},P\_{T}^{\widehat{\nu}},S\_{T};\beta)-\int\_{0}^{T}\phi\,(Q\_{t}^{\widehat{\nu}})^{2}\,dt\biggr]-\widehat{H}\_{\psi}(0,x,q,p,s;\beta)\biggr| | ≤β3​C\displaystyle\leq\beta^{3}\,C |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |Hψν^​(0,x,q,p,s;β)−H^ψ​(0,x,q,p,s;β)|\displaystyle\biggl|H\_{\psi}^{\widehat{\nu}}(0,x,q,p,s;\beta)-\widehat{H}\_{\psi}(0,x,q,p,s;\beta)\biggr| | ≤β3​C\displaystyle\leq\beta^{3}\,C |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |Hψν^​(0,x,q,p,s;β)−H^ψ​(0,x,q,p,s;β)|β2\displaystyle\frac{|H\_{\psi}^{\widehat{\nu}}(0,x,q,p,s;\beta)-\widehat{H}\_{\psi}(0,x,q,p,s;\beta)|}{\beta^{2}} | ≤β​C,\displaystyle\leq\beta\,C\,, |  |

and the desired limit follows. \qed

Part I (formal solution): By the terminal condition of the HJB equation ([20](https://arxiv.org/html/2601.10812v1#S4.E20 "In 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")), it is easy to show that h~0​(q)=−α​q2\widetilde{h}\_{0}(q)=-\alpha\,q^{2}. Substituting h~ψ\widetilde{h}\_{\psi} into the left hand side of ([23](https://arxiv.org/html/2601.10812v1#S4.E23 "In 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts")) and setting terms proportional to (T−t)0(T-t)^{0} to vanish gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | h~1,ψ​(q,p,s)=((b−2​α)24​k−ϕ)​q2−β​(p−ψ​(s))​q.\displaystyle\widetilde{h}\_{1,\psi}(q,p,s)=\biggl(\frac{(b-2\alpha)^{2}}{4\,k}-\phi\biggr)\,q^{2}-\beta\,(p-\psi(s))\,q. |  | (109) |

Similarly, grouping terms proportional to (T−t)1(T-t)^{1} gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h~2,ψ​(q,p,s)\displaystyle\widetilde{h}\_{2,\psi}(q,p,s) | =b−2​α4​k​((b−2​α)22​k−2​ϕ−b​β)​q2+β4​(−b−2​αk​(p−ψ​(s))+σ2​ψ′′​(s))​q.\displaystyle=\frac{b-2\,\alpha}{4\,k}\biggl(\frac{(b-2\,\alpha)^{2}}{2\,k}-2\,\phi-b\,\beta\biggr)\,q^{2}+\frac{\beta}{4}\,\biggl(-\frac{b-2\,\alpha}{k}\,(p-\psi(s))+\sigma^{2}\,\psi^{\prime\prime}(s)\biggr)\,q. |  | (110) |

Part II: (accuracy of approximation).
With h~ψ\widetilde{h}\_{\psi} as given in the theorem, define

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H~ψ​(t,x,q,p,s;T)\displaystyle\widetilde{H}\_{\psi}(t,x,q,p,s;T) | =x+q​p+h~ψ​(t,q,p,s;T).\displaystyle=x+q\,p+\widetilde{h}\_{\psi}(t,q,p,s;T)\,. |  | (111) |

For simplicity, we prove the approximation holds for t=0t=0 with initial states given by xx, qq, pp, and ss. The case of t≠0t\neq 0 follows similarly. Let νT,ϵ\nu^{T,\epsilon} be an admissible control which is ϵ​T2\epsilon\,T^{2}-optimal. Specifically, the control satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | HνT,ϵ​(0,x,q,p,s;T)+ϵ​T2≥Hψ​(0,x,q,p,s;T).\displaystyle H^{\nu^{T,\epsilon}}(0,x,q,p,s;T)+\epsilon\,T^{2}\geq H\_{\psi}(0,x,q,p,s;T)\,. |  | (112) |

Define the process GG by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt=H~ψ​(t,XtνT,ϵ,QtνT,ϵ,PtνT,ϵ,St;T)−∫0tϕ​(QuνT,ϵ)2​𝑑u,\displaystyle G\_{t}=\widetilde{H}\_{\psi}(t,X\_{t}^{\nu^{T,\epsilon}},Q\_{t}^{\nu^{T,\epsilon}},P\_{t}^{\nu^{T,\epsilon}},S\_{t};T)-\int\_{0}^{t}\phi\,(Q\_{u}^{\nu^{T,\epsilon}})^{2}\,du\,, |  | (113) |

and apply Itô’s Lemma to obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | GT−G0=∫0T(∂t+ℒνT,ϵ)​H~ψ​(t,XtνT,ϵ,QtνT,ϵ,PtνT,ϵ,St;T)−ϕ​(QtνT,ϵ)2​d​t+∫0Tσ​∂sH~ψ​(t,XtνT,ϵ,QtνT,ϵ,PtνT,ϵ,St;T)​d​Wts+∫0Tη​∂pH~ψ​(t,XtνT,ϵ,QtνT,ϵ,PtνT,ϵ,St;T)​d​Wtp,\displaystyle\begin{split}G\_{T}-G\_{0}&=\int\_{0}^{T}(\partial\_{t}+\mathcal{L}^{\nu^{T,\epsilon}})\,\widetilde{H}\_{\psi}(t,X\_{t}^{\nu^{T,\epsilon}},Q\_{t}^{\nu^{T,\epsilon}},P\_{t}^{\nu^{T,\epsilon}},S\_{t};T)-\phi\,\,(Q\_{t}^{\nu^{T,\epsilon}})^{2}dt\\ &\hskip 14.22636pt+\int\_{0}^{T}\sigma\,\partial\_{s}\widetilde{H}\_{\psi}(t,X\_{t}^{\nu^{T,\epsilon}},Q\_{t}^{\nu^{T,\epsilon}},P\_{t}^{\nu^{T,\epsilon}},S\_{t};T)\,dW^{s}\_{t}\\ &\hskip 14.22636pt+\int\_{0}^{T}\eta\,\partial\_{p}\widetilde{H}\_{\psi}(t,X\_{t}^{\nu^{T,\epsilon}},Q\_{t}^{\nu^{T,\epsilon}},P\_{t}^{\nu^{T,\epsilon}},S\_{t};T)\,dW^{p}\_{t}\,,\end{split} | |  | (114) |

where the differential operator ℒν\mathcal{L}^{\nu} is given by ([10](https://arxiv.org/html/2601.10812v1#S2.E10 "In 2.2 Performance Criterion ‣ 2 Model ‣ Optimal Liquidation of Perpetual Contracts")). The two stochastic integrands are computed explicitly as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂sH~ψ​(t,x,q,p,s;T)\displaystyle\partial\_{s}\widetilde{H}\_{\psi}(t,x,q,p,s;T) | =β​ψ′​(s)​q​(T−t)+β4​((b−2​α)​ψ′​(s)k+σ2​ψ′′′​(s))​q​(T−t)2,\displaystyle=\beta\,\psi^{\prime}(s)\,q\,(T-t)+\frac{\beta}{4}\,\biggl(\frac{(b-2\,\alpha)\,\psi^{\prime}(s)}{k}+\sigma^{2}\psi^{\prime\prime\prime}(s)\biggr)\,q\,(T-t)^{2}\,, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂pH~ψ​(t,x,q,p,s;T)\displaystyle\partial\_{p}\widetilde{H}\_{\psi}(t,x,q,p,s;T) | =−β​q​(T−t)−(b−2​α)​β4​k​q​(T−t)2.\displaystyle=-\beta\,q\,(T-t)-\frac{(b-2\,\alpha)\,\beta}{4\,k}\,q\,(T-t)^{2}\,. |  |

Boundedness of derivatives of ψ\psi from assumption [4](https://arxiv.org/html/2601.10812v1#Thmtheorem4 "Assumption 4 ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") implies that these stochastic integrands satisfy linear growth conditions, and therefore are square integrable for all admissible controls and the stochastic integrals are martingales. Thus, taking an expectation yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[GT]−G0\displaystyle\mathbb{E}[G\_{T}]-G\_{0} | =𝔼​[∫0T(∂t+ℒνT,ϵ)​H~ψ​(t,XtνT,ϵ,QtνT,ϵ,PtνT,ϵ,St;T)−ϕ​(QtνT,ϵ)2​d​t].\displaystyle=\mathbb{E}\biggl[\int\_{0}^{T}(\partial\_{t}+\mathcal{L}^{\nu^{T,\epsilon}})\,\widetilde{H}\_{\psi}(t,X\_{t}^{\nu^{T,\epsilon}},Q\_{t}^{\nu^{T,\epsilon}},P\_{t}^{\nu^{T,\epsilon}},S\_{t};T)-\phi\,\,(Q\_{t}^{\nu^{T,\epsilon}})^{2}dt\biggr]\,. |  |

Given the explicit form of H~\widetilde{H}, we obtain the bound

|  |  |  |
| --- | --- | --- |
|  | (∂t+ℒνT,ϵ)​H~ψ​(t,x,q,p,s;T)−ϕ​q2\displaystyle\biggl(\partial\_{t}+\mathcal{L}^{\nu^{T,\epsilon}}\biggr)\,\widetilde{H}\_{\psi}(t,x,q,p,s;T)-\phi\,q^{2} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤supν(∂t+ℒν)​H~ψ​(t,x,q,p,s;T)−ϕ​q2\displaystyle\leq\sup\_{\nu}\biggl(\partial\_{t}+\mathcal{L}^{\nu}\biggr)\,\widetilde{H}\_{\psi}(t,x,q,p,s;T)-\phi\,q^{2} |  |
|  |  |  |
| --- | --- | --- |
|  | =(T−t)2​A~​(q,p,s)+(T−t)3​B~​(q,p,s)+(T−t)4​C~​(q,p,s),\displaystyle=(T-t)^{2}\,\widetilde{A}(q,p,s)+(T-t)^{3}\,\widetilde{B}(q,p,s)+(T-t)^{4}\,\widetilde{C}(q,p,s)\,, |  |

where the functions A~\widetilde{A}, B~\widetilde{B} and C~\widetilde{C} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | A~​(q,p,s)\displaystyle\widetilde{A}(q,p,s) | =12​σ2​∂s​sh~2,ψ+14​k​((b​∂ph~1,ψ+∂qh~1,ψ)2+2​(b−2​α)​(b​∂ph~2,ψ+∂qh~2,ψ)​q),\displaystyle=\frac{1}{2}\,\sigma^{2}\,\partial\_{ss}\widetilde{h}\_{2,\psi}+\frac{1}{4\,k}\,\biggl((b\,\partial\_{p}\widetilde{h}\_{1,\psi}+\partial\_{q}\widetilde{h}\_{1,\psi})^{2}+2\,(b-2\,\alpha)\,(b\,\partial\_{p}\widetilde{h}\_{2,\psi}+\partial\_{q}\widetilde{h}\_{2,\psi})\,q\biggr), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B~​(q,p,s)\displaystyle\widetilde{B}(q,p,s) | =12​k​(b​∂ph~1,ψ+∂qh~1,ψ)​(b​∂ph~2,ψ+∂qh~2,ψ),\displaystyle=\frac{1}{2\,k}\,(b\,\partial\_{p}\widetilde{h}\_{1,\psi}+\partial\_{q}\widetilde{h}\_{1,\psi})\,(b\,\partial\_{p}\widetilde{h}\_{2,\psi}+\partial\_{q}\widetilde{h}\_{2,\psi}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C~​(q,p,s)\displaystyle\widetilde{C}(q,p,s) | =14​k​(b​∂ph~2,ψ+∂qh~2,ψ)2.\displaystyle=\frac{1}{4\,k}\,(b\,\partial\_{p}\widetilde{h}\_{2,\psi}+\partial\_{q}\widetilde{h}\_{2,\psi})^{2}. |  |

The functions h~1,ψ\widetilde{h}\_{1,\psi} and h~2,ψ\widetilde{h}\_{2,\psi} have at most quadratic growth in the variables qq and pp. Substituting the definition of GG and applying assumption [4](https://arxiv.org/html/2601.10812v1#Thmtheorem4 "Assumption 4 ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") gives

|  |  |  |
| --- | --- | --- |
|  | |HνT,ϵ(0,x,q,p,s;T)−H~ψ(0,x,q,p,s;T)|≤𝔼[∫0T|(T−t)2A~(t,QtνT,ϵ,PtνT,ϵ,St)\displaystyle\biggl|H^{\nu^{T,\epsilon}}(0,x,q,p,s;T)-\widetilde{H}\_{\psi}(0,x,q,p,s;T)\biggr|\leq\mathbb{E}\biggl[\int\_{0}^{T}\biggl|(T-t)^{2}\,\widetilde{A}(t,Q\_{t}^{\nu^{T,\epsilon}},P\_{t}^{\nu^{T,\epsilon}},S\_{t}) |  |
|  |  |  |
| --- | --- | --- |
|  | +(T−t)3B~(t,QtνT,ϵ,PtνT,ϵ,St)+(T−t)4C~(t,QtνT,ϵ,PtνT,ϵ,St)|dt]\displaystyle\hskip 128.0374pt+(T-t)^{3}\,\widetilde{B}(t,Q\_{t}^{\nu^{T,\epsilon}},P\_{t}^{\nu^{T,\epsilon}},S\_{t})+(T-t)^{4}\,\widetilde{C}(t,Q\_{t}^{\nu^{T,\epsilon}},P\_{t}^{\nu^{T,\epsilon}},S\_{t})\biggr|\,dt\biggr] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤T3​C,\displaystyle\hskip 213.39566pt\leq T^{3}\,C\,, |  |

for some constant CC that does not depend on TT. Recalling the definition of νT,ϵ\nu^{T,\epsilon} gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Hψ​(0,x,q,p,s;T)−H~ψ​(0,x,q,p,s;T)|\displaystyle|H\_{\psi}(0,x,q,p,s;T)-\widetilde{H}\_{\psi}(0,x,q,p,s;T)| | ≤ϵ​T2+T3​C\displaystyle\leq\epsilon\,T^{2}+T^{3}\,C |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |Hψ​(0,x,q,p,s;T)−H~ψ​(0,x,q,p,s;T)|T2\displaystyle\frac{|H\_{\psi}(0,x,q,p,s;T)-\widetilde{H}\_{\psi}(0,x,q,p,s;T)|}{T^{2}} | ≤ϵ+T​C.\displaystyle\leq\epsilon+T\,C\,. |  |

Since ϵ>0\epsilon>0 is arbitrary, the desired limit follows. \qed

When the agent follows the proposed strategy the inventory and perpetual price processes satisfy

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Qtν~\displaystyle dQ\_{t}^{\widetilde{\nu}} | =ν~​(t,Qtν~,Ptν~,St;T)​d​t,\displaystyle=\widetilde{\nu}(t,Q^{\widetilde{\nu}}\_{t},P^{\widetilde{\nu}}\_{t},S\_{t};T)\,dt\,, |  | (115) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Ptν~\displaystyle dP^{\widetilde{\nu}}\_{t} | =b​ν~​(t,Qtν~,Ptν~,St;T)​d​t+η​d​Wtp.\displaystyle=b\,\widetilde{\nu}(t,Q^{\widetilde{\nu}}\_{t},P^{\widetilde{\nu}}\_{t},S\_{t};T)\,dt+\eta\,dW\_{t}^{p}\,. |  | (116) |

By Theorem [7](https://arxiv.org/html/2601.10812v1#Thmtheorem7 "Theorem 7 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"), the function ν~\widetilde{\nu} may be written as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν~​(t,q,p,s;T)\displaystyle\widetilde{\nu}(t,q,p,s;T) | =F~1​(T−t)​q+F~2​(T−t)​p+β2​k​ψ​(s),\displaystyle=\widetilde{F}\_{1}(T-t)\,q+\widetilde{F}\_{2}(T-t)\,p+\frac{\beta}{2\,k}\,\psi(s)\,, |  | (117) |

where F~1\widetilde{F}\_{1} and F~2\widetilde{F}\_{2} are bounded. Therefore ν~\widetilde{\nu} is Lipschitz with linear growth in variables qq, pp and ss. Thus, the SDEs for Qν~Q^{\widetilde{\nu}} and Pν~P^{\widetilde{\nu}} have a unique strong solution (see Theorem 5.2.9 in Karatzas and
Shreve ([1991](https://arxiv.org/html/2601.10812v1#bib.bib16))). Moreover, there exists a constant M~\widetilde{M}, such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[(Qtν~)2+(Ptν~)2]\displaystyle\mathbb{E}\biggl[(Q\_{t}^{\widetilde{\nu}})^{2}+(P\_{t}^{\widetilde{\nu}})^{2}\biggr] | ≤M~​eM~​t,∀t∈[0,T].\displaystyle\leq\widetilde{M}\,e^{\widetilde{M}\,t}\,,\qquad\forall t\in[0,T]\,. |  | (118) |

Therefore, by Fubini’s Theorem, we have 𝔼​[∫0Tν~u2​𝑑t]<∞\mathbb{E}[\int\_{0}^{T}\widetilde{\nu}\_{u}^{2}\,dt]<\infty and ν~\widetilde{\nu} is an admissible control.

To show that ν~\widetilde{\nu} is asymptotically optimal, we proceed with a verification argument while keeping track of the magnitude of the error with respect to optimization, analogous to the proof of Theorem [7](https://arxiv.org/html/2601.10812v1#Thmtheorem7 "Theorem 7 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). We also remark that with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Hψ​(t,x,q,p,s;T)\displaystyle H\_{\psi}(t,x,q,p,s;T) | =x+q​p+hψ​(t,q,p,s;T),\displaystyle=x+q\,p+h\_{\psi}(t,q,p,s;T)\,, |  | (119) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Hψν~​(t,x,q,p,s;T)\displaystyle H\_{\psi}^{\widetilde{\nu}}(t,x,q,p,s;T) | =x+q​p+hψν~​(t,q,p,s;T),\displaystyle=x+q\,p+h\_{\psi}^{\widetilde{\nu}}(t,q,p,s;T)\,, |  | (120) |

our desired approximation result is equivalent to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limT→0Hψ​(t,x,q,p,s;T)−Hψν~​(t,x,q,p,s;T)T2\displaystyle\lim\_{T\rightarrow 0}\frac{H\_{\psi}(t,x,q,p,s;T)-H\_{\psi}^{\widetilde{\nu}}(t,x,q,p,s;T)}{T^{2}} | =0.\displaystyle=0\,. |  | (121) |

We prove the accuracy result at t=0t=0 with given initial states xx, qq, pp and ss, which we henceforth consider to be fixed. The general result for t≠0t\neq 0 follows similarly. Given the control ν~\widetilde{\nu}, and the resulting state processes Xν~X^{\widetilde{\nu}}, Qν~Q^{\widetilde{\nu}}, Pν~P^{\widetilde{\nu}} and SS, define the process G=(Gt)t∈[0,T]G=(G\_{t})\_{t\in[0,T]} by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Gt\displaystyle G\_{t} | =Xtν~+Qtν~​Ptν~+h~ψ​(t,Qtν~,Ptν~,St;T)−∫0tϕ​(Quν~)2​𝑑u,\displaystyle=X\_{t}^{\widetilde{\nu}}+Q\_{t}^{\widetilde{\nu}}\,P\_{t}^{\widetilde{\nu}}+\widetilde{h}\_{\psi}(t,Q\_{t}^{\widetilde{\nu}},P\_{t}^{\widetilde{\nu}},S\_{t};T)-\int\_{0}^{t}\phi\,(Q\_{u}^{\widetilde{\nu}})^{2}\,du\,, |  | (122) |

where h~ψ\widetilde{h}\_{\psi} is the approximation of hψh\_{\psi} given in Theorem [7](https://arxiv.org/html/2601.10812v1#Thmtheorem7 "Theorem 7 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). Applying Itô’s Lemma to GG gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | GT−G0=∫0T(∂t+ℒν~)​H~ψ​(t,Xtν~,Qtν~,Ptν~,St;T)−ϕ​(Qtν~)2​d​t+∫0Tσ​∂sH~ψ​(t,Xtν~,Qtν~,Ptν~,St;T)​d​Wts+∫0Tη​∂pH~ψ​(t,Xtν~,Qtν~,Ptν~,St;T)​d​Wtp.\displaystyle\begin{split}G\_{T}-G\_{0}=&\int\_{0}^{T}(\partial\_{t}+\mathcal{L}^{\widetilde{\nu}})\,\widetilde{H}\_{\psi}(t,X\_{t}^{\widetilde{\nu}},Q\_{t}^{\widetilde{\nu}},P\_{t}^{\widetilde{\nu}},S\_{t};T)-\phi\,(Q\_{t}^{\widetilde{\nu}})^{2}\,dt\\ &+\int\_{0}^{T}\sigma\,\partial\_{s}\widetilde{H}\_{\psi}(t,X\_{t}^{\widetilde{\nu}},Q\_{t}^{\widetilde{\nu}},P\_{t}^{\widetilde{\nu}},S\_{t};T)\,dW^{s}\_{t}\\ &+\int\_{0}^{T}\eta\,\partial\_{p}\widetilde{H}\_{\psi}(t,X\_{t}^{\widetilde{\nu}},Q\_{t}^{\widetilde{\nu}},P\_{t}^{\widetilde{\nu}},S\_{t};T)\,dW^{p}\_{t}\,.\end{split} | |  | (123) |

The growth conditions established on the stochastic integrands in the proof of Theorem [7](https://arxiv.org/html/2601.10812v1#Thmtheorem7 "Theorem 7 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") mean that the stochastic integrals are martingales. Thus, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[GT]−G0\displaystyle\mathbb{E}[G\_{T}]-G\_{0} | =𝔼​[∫0T(∂t+ℒν~)​H~ψ​(t,Xtν~,Qtν~,Ptν~,St;T)−ϕ​(Qtν~)2​d​t].\displaystyle=\mathbb{E}\biggl[\int\_{0}^{T}(\partial\_{t}+\mathcal{L}^{\widetilde{\nu}})\,\widetilde{H}\_{\psi}(t,X\_{t}^{\widetilde{\nu}},Q\_{t}^{\widetilde{\nu}},P\_{t}^{\widetilde{\nu}},S\_{t};T)-\phi\,(Q\_{t}^{\widetilde{\nu}})^{2}\,dt\biggr]\,. |  | (124) |

By fully expanding the integrand using the expressions in Theorem [7](https://arxiv.org/html/2601.10812v1#Thmtheorem7 "Theorem 7 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∂t+ℒν~)​H~ψ​(t,Xtν~,Qtν~,Ptν~,St;T)−ϕ​(Qtν~)2=(T−t)2​A~​(q,p,s)+(T−t)3​B~​(q,p,s),\displaystyle(\partial\_{t}+\mathcal{L}^{\widetilde{\nu}})\,\widetilde{H}\_{\psi}(t,X\_{t}^{\widetilde{\nu}},Q\_{t}^{\widetilde{\nu}},P\_{t}^{\widetilde{\nu}},S\_{t};T)-\phi\,(Q\_{t}^{\widetilde{\nu}})^{2}=(T-t)^{2}\,\widetilde{A}(q,p,s)+(T-t)^{3}\,\widetilde{B}(q,p,s)\,, |  | (125) |

where the functions A~\widetilde{A} and B~\widetilde{B} are given in the proof of Theorem [7](https://arxiv.org/html/2601.10812v1#Thmtheorem7 "Theorem 7 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). Previously established growth conditions of all terms on the right hand side and the fact that ν~\widetilde{\nu} is an admissible control imply that for sufficiently small TT

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[∫0T|(T−t)2​A~​(Qtν~,Ptν~,St)+(T−t)3​B~​(Qtν~,Ptν~,St)|​𝑑t]\displaystyle\mathbb{E}\biggl[\int\_{0}^{T}|(T-t)^{2}\,\widetilde{A}(Q\_{t}^{\widetilde{\nu}},P\_{t}^{\widetilde{\nu}},S\_{t})+(T-t)^{3}\,\widetilde{B}(Q\_{t}^{\widetilde{\nu}},P\_{t}^{\widetilde{\nu}},S\_{t})|\,dt\biggr] | ≤T3​C​(1+eM~​T),\displaystyle\leq T^{3}\,C\,(1+e^{\widetilde{M}\,T})\,, |  | (126) |

where CC is a constant that does not depend on TT. Thus, recalling the definition of GG we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼​[XTν~+QTν~​PTν~+h~​(T,QTν~,PTν~,ST;T)−∫0Tϕ​(Qtν~)2​𝑑t]−H~ψ​(0,x,q,p,s;T)|\displaystyle\biggl|\mathbb{E}\biggl[X\_{T}^{\widetilde{\nu}}+Q\_{T}^{\widetilde{\nu}}\,P\_{T}^{\widetilde{\nu}}+\widetilde{h}(T,Q\_{T}^{\widetilde{\nu}},P\_{T}^{\widetilde{\nu}},S\_{T};T)-\int\_{0}^{T}\phi\,(Q\_{t}^{\widetilde{\nu}})^{2}\,dt\biggr]-\widetilde{H}\_{\psi}(0,x,q,p,s;T)\biggr| | ≤T3​C​(1+eM~​T)\displaystyle\leq T^{3}\,C\,(1+e^{\widetilde{M}\,T}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |Hψν~​(0,x,q,p,s;T)−H~ψ​(0,x,q,p,s;T)|\displaystyle\biggl|H\_{\psi}^{\widetilde{\nu}}(0,x,q,p,s;T)-\widetilde{H}\_{\psi}(0,x,q,p,s;T)\biggr| | ≤T3​C​(1+eM~​T)\displaystyle\leq T^{3}\,C\,(1+e^{\widetilde{M}\,T}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |Hψν~​(0,x,q,p,s;T)−H~ψ​(0,x,q,p,s;T)|T2\displaystyle\frac{|H\_{\psi}^{\widetilde{\nu}}(0,x,q,p,s;T)-\widetilde{H}\_{\psi}(0,x,q,p,s;T)|}{T^{2}} | ≤T​C​(1+eM~​T),\displaystyle\leq T\,C\,(1+e^{\widetilde{M}\,T})\,, |  |

and the desired limit follows. \qed

By Theorems [2](https://arxiv.org/html/2601.10812v1#Thmtheorem2 "Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") and [8](https://arxiv.org/html/2601.10812v1#Thmtheorem8 "Theorem 8 (Asymptotic Approximation of Optimal Trading Speed) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") the controls ν¯\overline{\nu} and ν~\widetilde{\nu} are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν¯​(t,q,p,s;T)\displaystyle\overline{\nu}(t,q,p,s;T) | =ν0∗​(t;T)​q+ν1∗​(t;T)​(p−ψ​(s)),\displaystyle=\nu^{\ast}\_{0}(t;T)\,q+\nu^{\ast}\_{1}(t;T)\,(p-\psi(s))\,, |  | (127) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν~​(t,q,p,s;T)\displaystyle\widetilde{\nu}(t,q,p,s;T) | =ν~2​(t;T)​q+ν~3​(t;T)​(p−ψ​(s)),\displaystyle=\widetilde{\nu}\_{2}(t;T)\,q+\widetilde{\nu}\_{3}(t;T)\,(p-\psi(s))\,, |  | (128) |

where ν0∗\nu^{\ast}\_{0}, ν1∗\nu^{\ast}\_{1}, ν~2\widetilde{\nu}\_{2} and ν~3\widetilde{\nu}\_{3} are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν0∗​(t;T)\displaystyle\nu^{\ast}\_{0}(t;T) | =14​k((ξ(t;T)+π(t;T)),\displaystyle=\frac{1}{4\,k}\,\left((\xi(t;T)+\pi(t;T)\right)\,, |  | (129) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν1∗​(t;T)\displaystyle\nu^{\ast}\_{1}(t;T) | =14​k​b((ξ(t;T)−π(t;T)),\displaystyle=\frac{1}{4\,k\,b}\,\left((\xi(t;T)-\pi(t;T)\right)\,, |  | (130) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν~2​(t;T)\displaystyle\widetilde{\nu}\_{2}(t;T) | =12​k​[b−2​α+(12​k​(b−2​α)2−2​ϕ−b​β)​(T−t)],\displaystyle=\frac{1}{2\,k}\,\biggl[b-2\,\alpha+\biggl(\frac{1}{2\,k}\,(b-2\,\alpha)^{2}-2\,\phi-b\,\beta\biggr)\,(T-t)\biggr]\,, |  | (131) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν~3​(t;T)\displaystyle\widetilde{\nu}\_{3}(t;T) | =−12​k​β​(T−t),\displaystyle=-\frac{1}{2\,k}\,\beta\,(T-t)\,, |  | (132) |

where ξ\xi and π\pi are given in Theorem [2](https://arxiv.org/html/2601.10812v1#Thmtheorem2 "Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). Showing that ν¯\overline{\nu} is admissible follows the same reasoning as showing ν~\widetilde{\nu} is admissible from the proof of Theorem [8](https://arxiv.org/html/2601.10812v1#Thmtheorem8 "Theorem 8 (Asymptotic Approximation of Optimal Trading Speed) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). A direct computation gives

|  |  |  |
| --- | --- | --- |
|  | limT→0ξ​(t;T)=limT→0π​(t;T)=b−2​α,\displaystyle\lim\_{T\to 0}\xi(t;T)=\lim\_{T\to 0}\pi(t;T)=b-2\,\alpha\,, |  |

which further gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0(ν0∗​(t;T)−ν~2​(t;T))\displaystyle\lim\_{T\to 0}(\nu^{\ast}\_{0}(t;T)-\widetilde{\nu}\_{2}(t;T)) | =0,\displaystyle=0\,, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0(ν1∗​(t;T)−ν~3​(t;T))\displaystyle\lim\_{T\to 0}(\nu^{\ast}\_{1}(t;T)-\widetilde{\nu}\_{3}(t;T)) | =0.\displaystyle=0\,. |  |

The first derivative of ξ\xi and π\pi with respect to TT is computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Tξ​(t;T)\displaystyle\partial\_{T}\xi(t;T) | =−4​a​ω​C​e−2​ω​(T−t)(C​e−2​ω​(T−t)+1)2,\displaystyle=-4\,a\,\omega\,C\,\frac{e^{-2\,\omega\,(T-t)}}{(C\,e^{-2\,\omega\,(T-t)}+1)^{2}}\,, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Tπ​(t;T)\displaystyle\partial\_{T}\pi(t;T) | =(C+1)​(b−2​α)​2​ω​C​e−3​ω​(T−t)−ω​e−ω​(T−t)​(C​e−2​ω​(T−t)+1)(C​e−2​ω​(T−t)+1)2\displaystyle=(C+1)\,(b-2\,\alpha)\,\frac{2\,\omega\,C\,e^{-3\,\omega\,(T-t)}-\omega\,e^{-\omega\,(T-t)}\,(C\,e^{-2\,\omega\,(T-t)}+1)}{(C\,e^{-2\,\omega\,(T-t)}+1)^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −8​k​ϕ​ω​C​e−2​ω​(T−t)​(C​e−ω​(T−t)+1)​(1−e−ω​(T−t))a​(C​e−2​ω​(T−t)+1)2\displaystyle-\frac{8\,k\,\phi\,\omega\,C\,e^{-2\,\omega\,(T-t)}\,(C\,e^{-\omega\,(T-t)}+1)\,(1-e^{-\omega\,(T-t)})}{a\,(C\,e^{-2\,\omega\,(T-t)}+1)^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −4​k​ϕ​(C​e−2​ω​(T−t)+1)​(ω​e−ω​(T−t)​(C​e−ω​(T−t)+1)−ω​C​e−ω​(T−t)​(1−e−ω​(T−t)))a​(C​e−2​ω​(T−t)+1)2,\displaystyle-\frac{4\,k\,\phi\,(C\,e^{-2\,\omega\,(T-t)}+1)\,(\omega\,e^{-\omega\,(T-t)}\,(C\,e^{-\omega\,(T-t)}+1)-\omega\,C\,e^{-\omega\,(T-t)}\,(1-e^{-\omega\,(T-t)}))}{a\,(C\,e^{-2\,\omega\,(T-t)}+1)^{2}}\,, |  |

where the constants aa, CC and ω\omega are stated in Theorem [2](https://arxiv.org/html/2601.10812v1#Thmtheorem2 "Theorem 2 (Optimal Trading Strategy for Identity Payoff Function) ‣ 3 Identity Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). A tedious but direct computation yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0∂Tξ​(t;T)\displaystyle\lim\_{T\to 0}\partial\_{T}\xi(t;T) | =12​k​(b−2​α)2−2​(b​β+ϕ),\displaystyle=\frac{1}{2\,k}\,(b-2\,\alpha)^{2}-2\,(b\,\beta+\phi)\,, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0∂Tπ​(t;T)\displaystyle\lim\_{T\to 0}\partial\_{T}\pi(t;T) | =12​k​(b−2​α)2−2​ϕ.\displaystyle=\frac{1}{2\,k}\,(b-2\,\alpha)^{2}-2\,\phi\,. |  |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0∂T(ν0∗​(t;T)−ν~2​(t;T))\displaystyle\lim\_{T\to 0}\partial\_{T}(\nu^{\ast}\_{0}(t;T)-\widetilde{\nu}\_{2}(t;T)) | =0,\displaystyle=0\,, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0∂T(ν1∗​(t;T)−ν~3​(t;T))\displaystyle\lim\_{T\to 0}\partial\_{T}(\nu^{\ast}\_{1}(t;T)-\widetilde{\nu}\_{3}(t;T)) | =0.\displaystyle=0\,. |  |

Combining all the limits which are given above implies that the following limit holds locally uniformly in (t,q,p,s)(t,q,p,s) by L’Hopital’s rule:

|  |  |  |
| --- | --- | --- |
|  | limT→0ν¯​(t,q,p,s;T)−ν~​(t,q,p,s;T)T=0.\displaystyle\lim\_{T\to 0}\frac{\overline{\nu}(t,q,p,s;T)-\widetilde{\nu}(t,q,p,s;T)}{T}=0\,. |  |

Given the candidate strategy ν¯t=ν∗​(t,Qtν¯,Ptν¯,ψ​(St);T)\overline{\nu}\_{t}=\nu^{\ast}(t,Q^{\overline{\nu}}\_{t},P^{\overline{\nu}}\_{t},\psi(S\_{t});T), define the stochastic process (Gt)t∈[0,T](G\_{t})\_{t\in[0,T]} by

|  |  |  |
| --- | --- | --- |
|  | Gt=H~ψ​(t,Xtν¯,Qtν¯,Ptν¯,St;T)−∫0tϕ​(Quν¯)2​𝑑u,\displaystyle G\_{t}=\widetilde{H}\_{\psi}(t,X\_{t}^{\overline{\nu}},Q\_{t}^{\overline{\nu}},P\_{t}^{\overline{\nu}},S\_{t};T)-\int\_{0}^{t}\phi\,(Q\_{u}^{\overline{\nu}})^{2}\,du\,, |  |

and H~ψ\widetilde{H}\_{\psi} is the approximation of HψH\_{\psi} in Theorem [7](https://arxiv.org/html/2601.10812v1#Thmtheorem7 "Theorem 7 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts"). Apply Ito’s Lemma to GG and write

|  |  |  |  |
| --- | --- | --- | --- |
|  | GT−G0=∫0T(∂t+ℒν¯)​H~ψ​(t,Xtν¯,Qtν¯,Ptν¯,St;T)−ϕ​(Qtν¯)2​d​t+∫0Tσ​∂sH~ψ​(t,Xtν¯,Qtν¯,Ptν¯,St;T)​d​Wts+∫0Tη​∂pH~ψ​(t,Xtν¯,Qtν¯,Ptν¯,St;T)​d​Wtp.\displaystyle\begin{split}G\_{T}-G\_{0}&=\int\_{0}^{T}(\partial\_{t}+\mathcal{L}^{\overline{\nu}})\,\widetilde{H}\_{\psi}(t,X\_{t}^{\overline{\nu}},Q\_{t}^{\overline{\nu}},P\_{t}^{\overline{\nu}},S\_{t};T)-\phi\,\,(Q\_{t}^{\overline{\nu}})^{2}dt\\ &\hskip 14.22636pt+\int\_{0}^{T}\sigma\,\partial\_{s}\widetilde{H}\_{\psi}(t,X\_{t}^{\overline{\nu}},Q\_{t}^{\overline{\nu}},P\_{t}^{\overline{\nu}},S\_{t};T)\,dW^{s}\_{t}\\ &\hskip 14.22636pt+\int\_{0}^{T}\eta\,\partial\_{p}\widetilde{H}\_{\psi}(t,X\_{t}^{\overline{\nu}},Q\_{t}^{\overline{\nu}},P\_{t}^{\overline{\nu}},S\_{t};T)\,dW^{p}\_{t}\,.\end{split} | |  |

The growth conditions established on the stochastic integrands in the proof of Theorem [7](https://arxiv.org/html/2601.10812v1#Thmtheorem7 "Theorem 7 (Asymptotic Approximation of Value Function) ‣ 4 Arbitrary Payoff Function ‣ Optimal Liquidation of Perpetual Contracts") mean that the stochastic integrals are martingales. Defining r​(t,q,p,s;T)=ν¯​(t,q,p,s;T)−ν~​(t,q,p,s;T)r(t,q,p,s;T)=\overline{\nu}(t,q,p,s;T)-\widetilde{\nu}(t,q,p,s;T)

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∂t+ℒν¯)​H~ψ−ϕ​q2\displaystyle(\partial\_{t}+\mathcal{L}^{\overline{\nu}})\,\widetilde{H}\_{\psi}-\phi\,q^{2} | =∂th~ψ+(∂qh~ψ+b​(q+∂ph~ψ))​ν¯−k​(ν¯)2\displaystyle=\partial\_{t}\widetilde{h}\_{\psi}+(\partial\_{q}\widetilde{h}\_{\psi}+b(q+\partial\_{p}\widetilde{h}\_{\psi}))\,\overline{\nu}-k\,(\overline{\nu})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −β​q​(p−ψ​(s))+12​σ2​∂s​sh~ψ−ϕ​q2\displaystyle\hskip 42.67912pt-\beta\,q\,(p-\psi(s))+\frac{1}{2}\,\sigma^{2}\,\partial\_{ss}\widetilde{h}\_{\psi}-\phi\,q^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(∂t+ℒν~)​H~ψ−ϕ​q2+(∂qh~ψ+b​(q+∂ph~ψ)−2​k​ν~)​r−k​r2\displaystyle=(\partial\_{t}+\mathcal{L}^{\widetilde{\nu}})\,\widetilde{H}\_{\psi}-\phi\,q^{2}+(\partial\_{q}\widetilde{h}\_{\psi}+b\,(q+\partial\_{p}\widetilde{h}\_{\psi})-2\,k\,\widetilde{\nu})\,r-k\,r^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(T−t)2​A~​(q,p,s)+(T−t)3​B~​(q,p,s)+V​(t,q,p,s;T),\displaystyle=(T-t)^{2}\,\widetilde{A}(q,p,s)+(T-t)^{3}\,\widetilde{B}(q,p,s)+V(t,q,p,s;T), |  |

where the function VV is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,q,p,s;T)\displaystyle V(t,q,p,s;T) | =(∂qh~ψ+b​(q+∂ph~ψ)−2​k​ν~)​r−k​r2\displaystyle=(\partial\_{q}\widetilde{h}\_{\psi}+b\,(q+\partial\_{p}\widetilde{h}\_{\psi})-2\,k\,\widetilde{\nu})\,r-k\,r^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(T−t)2​(∂qh~2,ψ+b​∂ph~2,ψ)​r−k​r2.\displaystyle=(T-t)^{2}\,(\partial\_{q}\widetilde{h}\_{2,\psi}+b\,\partial\_{p}\widetilde{h}\_{2,\psi})\,r-k\,r^{2}. |  |

Since the functions V​(t,q,p,s;T)V(t,q,p,s;T) is at most quadratic growth in variables qq and pp and we have already shown that r​(t,q,p,s;T)=o​(T)r(t,q,p,s;T)=o(T) as T→0T\to 0, we have

|  |  |  |
| --- | --- | --- |
|  | limT→0V​(t,q,p,s;T)T2=0.\displaystyle\lim\_{T\to 0}\frac{V(t,q,p,s;T)}{T^{2}}=0. |  |

Taking an expectation and combining all the results yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼​[GT]−G0|\displaystyle\biggl|\mathbb{E}[G\_{T}]-G\_{0}\biggr| | =|𝔼​[∫0T(∂t+ℒν¯)​H~ψ​(t,Xtν¯,Qtν¯,Ptν¯,St;T)−ϕ​(Qtν¯)2​d​t]|\displaystyle=\biggl|\mathbb{E}\biggl[\int\_{0}^{T}(\partial\_{t}+\mathcal{L}^{\overline{\nu}})\,\widetilde{H}\_{\psi}(t,X\_{t}^{\overline{\nu}},Q\_{t}^{\overline{\nu}},P\_{t}^{\overline{\nu}},S\_{t};T)-\phi\,(Q\_{t}^{\overline{\nu}})^{2}\,dt\biggr]\biggr| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤T3​C​(1+eM~​T)+V​(T).\displaystyle\leq T^{3}\,C\,(1+e^{\widetilde{M}\,T})+V(T). |  |

where the function V​(T)V(T) can be chosen to satisfy

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[∫0TV​(t,Qtν¯,Ptν¯,St;T)​𝑑t]|≤V​(T),\displaystyle\biggl|\mathbb{E}\biggl[\int\_{0}^{T}V(t,Q\_{t}^{\overline{\nu}},P\_{t}^{\overline{\nu}},S\_{t};T)\,dt\biggr]\biggr|\leq V(T), |  |

and

|  |  |  |
| --- | --- | --- |
|  | limT→0V​(T)T3=0.\displaystyle\lim\_{T\to 0}\frac{V(T)}{T^{3}}=0. |  |

Thus, recalling the definition of GG we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Hψν¯​(0,x,q,p,s;T)−H~ψ​(0,x,q,p,s;T)|\displaystyle\biggl|H\_{\psi}^{\overline{\nu}}(0,x,q,p,s;T)-\widetilde{H}\_{\psi}(0,x,q,p,s;T)\biggr| | ≤T3​C​(1+eM~​T)+V​(T)\displaystyle\leq T^{3}\,C\,(1+e^{\widetilde{M}\,T})+V(T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |Hψν¯​(0,x,q,p,s;T)−H~ψ​(0,x,q,p,s;T)|T2\displaystyle\frac{|H\_{\psi}^{\overline{\nu}}(0,x,q,p,s;T)-\widetilde{H}\_{\psi}(0,x,q,p,s;T)|}{T^{2}} | ≤T​C​(1+eM~​T)+V​(T)T2,\displaystyle\leq T\,C\,(1+e^{\widetilde{M}\,T})+\frac{V(T)}{T^{2}}\,, |  |

and the desired limit follows. \qed

## References

* Ackerer
  et al. (2025)

  Ackerer, D., J. Hugonnier, and U. Jermann (2025).
  Perpetual futures pricing.
  Mathematical Finance.
* Almgren and
  Chriss (2001)

  Almgren, R. and N. Chriss (2001).
  Optimal execution of portfolio transactions.
  Journal of Risk 3, 5–40.
* Angeris
  et al. (2023)

  Angeris, G., T. Chitra, A. Evans, and M. Lorig (2023).
  A primer on perpetuals.
  SIAM Journal on Financial Mathematics 14(1),
  SC17–SC30.
* Bankman-Fried and
  White (2021)

  Bankman-Fried, S. and D. White (2021).
  Everlasting options.
* Bertsimas and
  Lo (1998)

  Bertsimas, D. and A. W. Lo (1998).
  Optimal control of execution costs.
  Journal of financial markets 1(1), 1–50.
* Cartea
  et al. (2020)

  Cartea, Á., R. Donnelly, and S. Jaimungal (2020).
  Hedging nontradable risks with transaction costs and price impact.
  Mathematical Finance 30(3), 833–868.
* Cartea and
  Jaimungal (2016)

  Cartea, Á. and S. Jaimungal (2016).
  Incorporating order-flow into optimal execution.
  Mathematics and Financial Economics 10(3), 339–364.
* Cartea
  et al. (2015)

  Cartea, Á., S. Jaimungal, and J. Penalva (2015).
  Algorithmic and high-frequency trading.
  Cambridge University Press.
* Cont
  et al. (2014)

  Cont, R., A. Kukanov, and S. Stoikov (2014).
  The price impact of order book events.
  Journal of financial econometrics 12(1), 47–88.
* Dai
  et al. (2025)

  Dai, M., L. Li, and C. Yang (2025).
  Arbitrage in perpetual contracts.
  Available at SSRN 5262988.
* Eisler
  et al. (2012)

  Eisler, Z., J.-P. Bouchaud, and J. Kockelkoren (2012).
  The price impact of order book events: market orders, limit orders
  and cancellations.
  Quantitative Finance 12(9), 1395–1419.
* Ekren and
  Muhle-Karbe (2019)

  Ekren, I. and J. Muhle-Karbe (2019).
  Portfolio choice with small temporary and transient price impact.
  Mathematical Finance 29(4), 1066–1115.
* Fouque
  et al. (2022)

  Fouque, J.-P., S. Jaimungal, and Y. F. Saporito (2022).
  Optimal trading with signals and stochastic price impact.
  SIAM Journal on Financial Mathematics 13(3),
  944–968.
* He
  et al. (2022)

  He, S., A. Manela, O. Ross, and V. von Wachter (2022).
  Fundamentals of perpetual futures.
  arXiv preprint arXiv:2212.06888.
* Horst
  et al. (2022)

  Horst, U., X. Xia, and C. Zhou (2022).
  Portfolio liquidation under factor uncertainty.
  The Annals of Applied Probability 32(1), 80–123.
* Karatzas and
  Shreve (1991)

  Karatzas, I. and S. Shreve (1991).
  Brownian motion and stochastic calculus, Volume 113.
  Springer Science & Business Media.
* Neuman and
  Voß (2022)

  Neuman, E. and M. Voß (2022).
  Optimal signal-adaptive trading with temporary and transient price
  impact.
  SIAM Journal on Financial Mathematics 13(2),
  551–575.
* Xu
  et al. (2018)

  Xu, K., M. D. Gould, and S. D. Howison (2018).
  Multi-level order-flow imbalance in a limit order book.
  Market Microstructure and Liquidity 4(03n04),
  1950011.