---
authors:
- Alexander Barzykin
doc_id: arxiv:2603.07752v1
family_id: arxiv:2603.07752
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Dynamic slippage control and rejection feedback in spot FX market making
url_abs: http://arxiv.org/abs/2603.07752v1
url_html: https://arxiv.org/html/2603.07752v1
venue: arXiv q-fin
version: 1
year: 2026
---


Alexander Barzykin
Email: alexander.barzykin@hsbc.com

###### Abstract

We study an OTC FX market-making problem, built on the Avellaneda-Stoikov tradition, in which a dealer streams size-dependent quotes on a discrete ladder and manages inventory risk over a finite horizon under Poisson arrivals of trade requests.
Adverse selection is modeled through latency-driven price moves over a delay window, represented by Gaussian marks whose conditional means can depend on the quoted spread, capturing selective client reaction to stale quotes.
The dealer can address latency risk through trade rejection when slippage breaches a tolerance threshold.
We treat slippage tolerance as an explicit control jointly optimized with quotes: upon receiving a trade request, the dealer chooses an acceptance/rejection rule, which makes the trade economically akin to an embedded option written on the latency price move.
We further introduce rejection feedback through an EMA-based rejection score used as a reputation proxy, so that client intensity is endogenously modulated by past rejections via a multiplicative factor.
Using dynamic programming, we derive a Markov control problem with state variables (inventory, rejection-score) and show how rejection decision enters the Hamilton-Jacobi-Bellman equation through Hamiltonians that include an expectation over the latency mark and a maximization over both quote and rejection rule parameters.
For practical control evaluation, we develop an adiabatic-quadratic approximation: fixing reputation on the inventory-control time scale, expanding Hamiltonians to the second order à la Bergault et al., and adopting quadratic ansatz in inventory, yielding tractable Riccati-type ODE and closed-form expressions for approximate quotes and slippage thresholds.
This approximation provides a fast surrogate for policy design and enables self-consistent calibration of rejection behavior.
We complement the analysis with exact numerical solutions of the reduced HJB and compare unrestricted and fair rejection protocols in terms of spread, rejection probability, and value.

Keywords: Foreign Exchange; Market Making; Stochastic Optimal Control; Market Impact; Algorithmic Trading; Price Validation; Trade Rejection; Last Look; Adverse Selection; Latency

## 1 Introduction

Electronic dealer-to-client (D2C) markets, especially in spot FX and related OTC products, routinely expose liquidity providers (LPs)
to latency risk: a client may hit a streamed quote that was formed on information that is already stale by the time the request reaches the dealer’s pricing and risk stack.
A widely used response specific to FX is last look (LL), i.e., a short post-request window in which the dealer can accept or reject the trade, sometimes subject to protocol constraints on permissible price improvement or slippage.
As this practice reallocates execution risk between dealers and clients, its fairness relies on design choices such as
whether the acceptance rule is symmetric or asymmetric, whether price improvements are passed through, and how much discretion the dealer has.
These issues are central enough that industry codes emphasize transparency and the interpretation of LL as a risk-control mechanism rather than a profit tool
(GFXC [2024](#bib.bib12)).

LL is primarily treated as an execution protocol shaping the client’s effective costs and risks.
Oomen ([2017b](#bib.bib17)) develops a unified framework to compare LL designs – symmetric versus asymmetric thresholds, and variants allowing or disallowing price
improvements/slippage – focusing on execution risk, effective spreads, and how LL changes the trader’s experience across protocols.
Closely related, Stevenson ([2016](#bib.bib18)) frames LL as a millisecond-expiry option embedded in the trading protocol and studies valuation and the incentives
created by this opportunity.
Oomen ([2017a](#bib.bib16)) models execution through an aggregator that routes to the best displayed price among multiple LPs and highlights how competition for
(apparently) uninformed flow can generate a “winner’s curse” and adverse selection-type effects at the LP level.
Cartea et al. ([2019](#bib.bib8)) develop an equilibrium-style model of FX trading with LL that distinguishes between fast and slow traders, and study how LL and competition
affect spreads, rejection rates, and welfare across participant types.
Cartea and Sánchez-Betancourt ([2021](#bib.bib10)), Cartea et al. ([2021](#bib.bib11)) further study the interplay between latency and liquidity risk.

Current institutional practice reduces post-request hold time to zero – the decision is made as soon as the request is received and resembles in this sense the mechanics of an exchange with firm liquidity.
The term “last look” itself may be misleading here, and one can talk about price validation instead.
There is an important difference from the exchange logic, however.
The dealer typically keeps slippage tolerance as a control parameter with an understanding that latency inherent in delocalized FX markets can lead to excessive rejections.

The market-making literature beginning with Avellaneda-Stoikov ([2008](#bib.bib1)) and subsequent refinements
(Guéant et al. [2013](#bib.bib13), Cartea et al. [2014](#bib.bib6), [2015](#bib.bib7), Guéant [2016](#bib.bib14)) provides tractable stochastic-control foundations for optimal quoting under inventory risk
and Poisson trade arrivals, but typically treats price dynamics as exogenous and does not model trade rejection decision as part of the control set.
Recently, Olding ([2022](#bib.bib15)) explicitly adapts classical market-making control models to incorporate LL via an exogenous survival/cancellation mechanism
(e.g., symmetric cancellation when the mid moves beyond a threshold during the LL window), deriving reservation-price adjustments and optimal quotes under LL.
Importantly, in Olding’s control formulation LL parameters (window/threshold) are treated as given, while the dealer optimizes quotes.
Finally, beyond LL-specific work, the growing literature on informational risk in market making (e.g., alpha signals, quote-dependent adverse selection, price reading)
underscores that dealers’ pricing choices can affect both the volume and the toxicity of the flow they attract (Cartea and Wang [2020](#bib.bib9), Barzykin et al. [2025](#bib.bib3)).

Despite this rich literature, two practical dimensions remain underdeveloped:

* •

  Endogenous rejection policy design. Dealers often choose rejection logic (e.g., a symmetric “validity band”) as a dynamic risk-control policy that varies by market conditions, inventory, or relationship.
  Much of the academic work either analyzes rejection as a static protocol feature (optionality/effective costs) or embeds slippage tolerance into market-making models with parameters fixed.
  A natural step is to treat rejection decision – subject to fairness/protocol constraints – as an optimizable state-dependent control alongside quoting.
* •

  Intertemporal feedback from rejection decisions to future order flow. Real OTC relationships are not memoryless: frequent rejections can reduce subsequent client engagement, routing priority, or hit rates.
  Industry discussions emphasize transparency and appropriate use precisely because clients respond to perceived “unfair” or overly discretionary LL (GFXC [2024](#bib.bib12)).
  Yet most tractable models do not include a reputational state variable that couples the current rejection decision to future flow intensity.

In this paper, we propose a tractable stochastic-control framework for D2C market making with latency that builds on the Avellaneda-Stoikov tradition, enhanced by optimal slippage tolerance with rejection feedback in response to latency risk.
We apply this framework to unconstrained rejection decisions and to one of the fair protocols, proposed by Oomen ([2017b](#bib.bib17)), under strict zero hold-time policy (immediate decision upon request).
We also suggest an efficient adiabatic-quadratic approximation providing closed-form solutions, particularly in a simple but practically important case of
constant adverse selection slippage.

## 2 Unconstrained rejection as an arrival-time binary decision

### 2.1 Problem setup

Let St\displaystyle S\_{t} denote the reference mid price and assume that it undergoes the Brownian motion Wt\displaystyle W\_{t} so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=σ​d​Wt,dS\_{t}=\sigma dW\_{t}, |  | (1) |

with constant volatility σ>0\displaystyle\sigma>0 on a finite operational horizon [0,T]\displaystyle[0,T] of the market maker (MM).
The MM streams OTC quotes to clients for a finite set of trade sizes {zn}n=1N⊂ℕ\displaystyle\{z\_{n}\}\_{n=1}^{N}\subset\mathbb{N} (Avellaneda and Stoikov [2008](#bib.bib1), Bergault and Guéant [2021](#bib.bib5)).
For each bucket n\displaystyle n and side i∈{b,a}\displaystyle i\in\{b,a\} (bid/ask), the MM controls the quote offsets δtn,i\displaystyle\delta\_{t}^{n,i}, so the executable quotes are

|  |  |  |  |
| --- | --- | --- | --- |
|  | Stn,i=St∓δtn,i,i∈{b,a}.S\_{t}^{n,i}=S\_{t}\mp\delta\_{t}^{n,i},\qquad i\in\{b,a\}. |  | (2) |

Client requests arrive according to counting processes Mtn,i\displaystyle M^{n,i}\_{t} with intensities
111Exponential intensity is a natural assumption, but sigmoid is also used, particularly for RFQ (Barzykin et al. [2023](#bib.bib2)).

|  |  |  |  |
| --- | --- | --- | --- |
|  | λtn,i=g​(Rt)​Λ0n​e−κn​δtn,i,\lambda^{n,i}\_{t}=g(R\_{t})\Lambda^{n}\_{0}\,e^{-\kappa\_{n}\delta^{n,i}\_{t}}, |  | (3) |

where Λ0n>0\displaystyle\Lambda^{n}\_{0}>0, κn>0\displaystyle\kappa\_{n}>0 and g:[0,1]→ℝ+\displaystyle g:[0,1]\to\mathbb{R}^{+} is a decreasing function of a rejection-score variable Rt\displaystyle R\_{t} (a reputation proxy) constructed as an
exponentially weighted moving average (EMA) of past rejects.222One can easily verify whether the effect is present in the system by regressing the number of requests over a period of time (say, one hour) versus the average realized rejection rate over the previous period.

A request of type (n,i)\displaystyle(n,i) arriving at time t\displaystyle t is a response to a quote δ\displaystyle\delta that is τn\displaystyle\tau\_{n} old.
Let Ytn,i​(δ)\displaystyle Y^{n,i}\_{t}(\delta) denote the sign-adjusted mid-price change over that latency window (positive move is in the dealer’s favour).
We assume a Gaussian mark with a quote-dependent mean:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ytn,i​(δ)=mn​(δ)+νn​ξ,ξ∼𝒩​(0,1),νn:=σ​τn.Y^{n,i}\_{t}(\delta)=m\_{n}(\delta)+\nu\_{n}\xi,\qquad\xi\sim\mathcal{N}(0,1),\qquad\nu\_{n}:=\sigma\sqrt{\tau\_{n}}. |  | (4) |

where mn​(δ)\displaystyle m\_{n}(\delta) is a measurable function encoding adverse selection.333Exponential saturation is a natural default (Barzykin et al. [2025](#bib.bib3)).
In what follows, we assume side-symmetric latency marks: the conditional law of Ytn,i\displaystyle Y^{n,i}\_{t} depends on the side only through the sign convention used to define favourable and adverse moves, while the functions mn​(⋅)\displaystyle m\_{n}(\cdot) and νn\displaystyle\nu\_{n} are common to bid and ask.
The mark is observed by the MM prior to accepting or rejecting the trade.
Hereinafter, we assume zero hold time by the dealer, i.e., the decision ℓtn,i∈{0,1}\displaystyle\ell^{n,i}\_{t}\in\{0,1\} is made as soon as the trade request is received.
Here ℓ=1\displaystyle\ell=1 denotes acceptance and ℓ=0\displaystyle\ell=0 rejection.
Reputation (rejection score) is updated per request

|  |  |  |  |
| --- | --- | --- | --- |
|  | R+=(1−ρ)​R+ρ​(1−ℓ),ρ∈(0,1),R^{+}=(1-\rho)R+\rho(1-\ell),\qquad\rho\in(0,1), |  | (5) |

with maps

|  |  |  |  |
| --- | --- | --- | --- |
|  | Racc​(R)=(1−ρ)​R,Rrej​(R)=(1−ρ)​R+ρ.R\_{\text{acc}}(R)=(1-\rho)R,\qquad R\_{\text{rej}}(R)=(1-\rho)R+\rho. |  | (6) |

Thus Rt∈[0,1]\displaystyle R\_{t}\in[0,1] whenever R0∈[0,1]\displaystyle R\_{0}\in[0,1].
444An alternative way to define the reputation variable is via an Ornstein-Uhlenbeck process driven by rejections.

Let qt∈ℤ\displaystyle q\_{t}\in\mathbb{Z} denote inventory and Xt∈ℝ\displaystyle X\_{t}\in\mathbb{R} cash.
When a bid request is accepted the MM buys zn\displaystyle z\_{n} at St−δtn,b\displaystyle S\_{t}-\delta^{n,b}\_{t}; when an ask request is accepted the MM sells zn\displaystyle z\_{n} at St+δtn,a\displaystyle S\_{t}+\delta^{n,a}\_{t}.
Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​qt=∑n=1Nzn​ℓtn,b​d​Mtn,b−∑n=1Nzn​ℓtn,a​d​Mtn,a,dq\_{t}=\sum\_{n=1}^{N}z\_{n}\ell^{n,b}\_{t}\,dM^{n,b}\_{t}-\sum\_{n=1}^{N}z\_{n}\ell^{n,a}\_{t}\,dM^{n,a}\_{t}, |  | (7) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=−∑n=1Nℓtn,b​zn​(St−δtn,b)​d​Mtn,b+∑n=1Nℓtn,a​zn​(St+δtn,a)​d​Mtn,a.dX\_{t}=-\sum\_{n=1}^{N}\ell^{n,b}\_{t}z\_{n}(S\_{t}-\delta^{n,b}\_{t})\,dM^{n,b}\_{t}+\sum\_{n=1}^{N}\ell^{n,a}\_{t}z\_{n}(S\_{t}+\delta^{n,a}\_{t})\,dM^{n,a}\_{t}. |  | (8) |

The dealer aims to maximize expected terminal mark-to-market wealth penalized by running inventory risk (Cartea et al. [2014](#bib.bib6)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | supδ,ℓ𝔼​[XT+qT​ST−12​γ​σ2​∫0Tqt2​𝑑t],γ>0,\sup\_{\delta,\ell}\mathbb{E}\left[X\_{T}+q\_{T}S\_{T}-\frac{1}{2}\gamma\sigma^{2}\int\_{0}^{T}q\_{t}^{2}dt\right],\qquad\gamma>0, |  | (9) |

possibly with a terminal penalty.

### 2.2 HJB and optimal controls

Define the value function on the full state U​(t,x,q,R,S)\displaystyle U(t,x,q,R,S).
The corresponding Hamilton-Jacobi-Bellman (HJB) equation reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=∂tU+12​σ2​∂S​SU−12​γ​σ2​q2+∑i∈{b,a}∑n=1Nsupδn,iλn,i​𝔼​[supℓ(U0n,i​(ℓ)−U)],0=\partial\_{t}U+\frac{1}{2}\sigma^{2}\partial\_{SS}U-\frac{1}{2}\gamma\sigma^{2}q^{2}+\sum\_{i\in\{b,a\}}\sum\_{n=1}^{N}\sup\_{\delta^{n,i}}\lambda^{n,i}\mathbb{E}\left[\sup\_{\ell}\big(U^{n,i}\_{0}(\ell)-U\big)\right], |  | (10) |

where U0n,i​(ℓ)\displaystyle U^{n,i}\_{0}(\ell) denotes the value immediately after processing the request of type (n,i)\displaystyle(n,i) under decision ℓ\displaystyle\ell and expectation
is over the Gaussian mark Yn,i​(δ)\displaystyle Y^{n,i}(\delta).

Since the objective is linear in cash and mark-to-market wealth, we employ the affine ansatz

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(t,x,q,R,S)=x+q​S+V​(t,q,R)U(t,x,q,R,S)=x+qS+V(t,q,R) |  | (11) |

for the reduced value function V\displaystyle V.
This removes the mid-price state from the HJB.
For a request of size bucket n\displaystyle n, acceptance generates incremental value

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δaccn,i=zn​(δ+Yn,i​(δn,i)−𝒟±n​V​(t,q,R))\Delta\_{\text{acc}}^{n,i}=z\_{n}\left(\delta+Y^{n,i}(\delta^{n,i})-\mathcal{D}^{n}\_{\pm}V(t,q,R)\right) |  | (12) |

while rejection generates

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δrejn,i=𝒥R​V​(t,q,R),\Delta\_{\text{rej}}^{n,i}=\mathcal{J}\_{R}V(t,q,R), |  | (13) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | pn,i​(t,q,R)≡𝒟±n​V​(t,q,R):=V​(t,q,R)−V​(t,q±zn,Racc​(R))zn,p^{n,i}(t,q,R)\equiv\mathcal{D}^{n}\_{\pm}V(t,q,R):=\frac{V\big(t,q,R\big)-V\big(t,q\pm z\_{n},R\_{\text{acc}}(R)\big)}{z\_{n}}, |  | (14) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,q,R)≡𝒥R​V​(t,q,R):=V​(t,q,Rrej​(R))−V​(t,q,R).J(t,q,R)\equiv\mathcal{J}\_{R}V(t,q,R):=V(t,q,R\_{\text{rej}}(R))-V(t,q,R). |  | (15) |

Thus, the optimal decision induces a pointwise maximum.
Hence, the reduced HJB for V​(t,q,R)\displaystyle V(t,q,R) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=∂tV−12​γ​σ2​q2+g​(R)​∑i∈{b,a}∑n=1Nsupδn,iΛ0n​e−κn​δn,i​𝔼​[max⁡(Δaccn,i,Δrejn,i)],0=\partial\_{t}V-\frac{1}{2}\gamma\sigma^{2}q^{2}+g(R)\sum\_{i\in\{b,a\}}\sum\_{n=1}^{N}\sup\_{\delta^{n,i}}\Lambda^{n}\_{0}\,e^{-\kappa\_{n}\delta^{n,i}}\mathbb{E}\left[\max\Big(\Delta\_{\text{acc}}^{n,i},\Delta\_{\text{rej}}^{n,i}\Big)\right], |  | (16) |

with terminal condition V​(T,q,R)=𝒯​(q,R)\displaystyle V(T,q,R)=\mathcal{T}(q,R).555We are primarily interested in the near-stationary solution, so the terminal condition can be set to zero.
Note that since g​(R)\displaystyle g(R) is decreasing and a rejection moves the score from R\displaystyle R to Rrej​(R)≥R\displaystyle R\_{\text{rej}}(R)\geq R, it is natural to expect the value function to be non-increasing in R\displaystyle R.
Under this monotonicity, J​(t,q,R)≤0\displaystyle J(t,q,R)\leq 0.
We can interpret J\displaystyle J as the continuation loss from worsening reputation.

Let Φ\displaystyle\Phi and ϕ\displaystyle\phi denote the standard normal CDF and PDF, respectively, and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψn​(μ):=𝔼​[(𝒩​(μ+νn​ξ))+]=νn​ϕ​(μ/νn)+μ​Φ​(μ/νn).\Psi\_{n}(\mu):=\mathbb{E}\left[\big(\mathcal{N}(\mu+\nu\_{n}\xi)\big)\_{+}\right]=\nu\_{n}\phi(\mu/\nu\_{n})+\mu\Phi(\mu/\nu\_{n}). |  | (17) |

Using max⁡(A,B)=B+(A−B)+\displaystyle\max(A,B)=B+(A-B)\_{+}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[max⁡(zn​(δ+Y−p),J)]=J+zn​Ψn​(δ+mn−p−Jzn)\mathbb{E}\left[\max\Big(z\_{n}(\delta+Y-p),J\Big)\right]=J+z\_{n}\Psi\_{n}\left(\delta+m\_{n}-p-\frac{J}{z\_{n}}\right) |  | (18) |

when Y∼N​(mn,νn2)\displaystyle Y\sim N(m\_{n},\nu\_{n}^{2}).
Here the second term can be identified as the value of exercising the accept option, as illustrated in Figure [1](#S2.F1 "Figure 1 ‣ 2.2 HJB and optimal controls ‣ 2 Unconstrained rejection as an arrival-time binary decision ‣ Dynamic slippage control and rejection feedback in spot FX market making").
If we define for each size bucket n\displaystyle n the bid/ask Hamiltonians

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hn​(p,J):=supδ∈ℝΛ0n​e−κn​δ​[J+zn​Ψn​(δ+mn​(δ)−p−Jzn)],H^{n}(p,J):=\sup\_{\delta\in\mathbb{R}}\Lambda\_{0}^{n}e^{-\kappa\_{n}\delta}\left[J+z\_{n}\Psi\_{n}\left(\delta+m\_{n}(\delta)-p-\frac{J}{z\_{n}}\right)\right], |  | (19) |

we can further transform the reduced HJB to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=∂tV−12​γ​σ2​q2+g​(R)​∑i∈{b,a}∑n=1NHn​(pn,i​(t,q,R),J​(t,q,R)).0=\partial\_{t}V-\frac{1}{2}\gamma\sigma^{2}q^{2}+g(R)\sum\_{i\in\{b,a\}}\sum\_{n=1}^{N}H^{n}\left(p^{n,i}(t,q,R),J(t,q,R)\right). |  | (20) |

![Refer to caption](2603.07752v1/x1.png)


Figure 1: 
Latency mark Y∼𝒩​(mn​(δ),νn2)\displaystyle Y\sim\mathcal{N}(m\_{n}(\delta),\nu\_{n}^{2}) and embedded-option view of request-level payoff for unrestricted rejection policy.
Red dashed line depicts optimal decision threshold: the request is accepted when Y>=y∗n​(q,R)\displaystyle Y>=y\_{\*}^{n}(q,R).

For each (n,i)\displaystyle(n,i), optimal quotes solve the supδ\displaystyle\sup\_{\delta} in HJB:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ∗n,i​(t,q,R)=arg​maxδ⁡Λ0n​e−κn​δ​[J​(t,q,R)+zn​Ψn​(δ+mn​(δ)−pn,i​(t,q,R)−J​(t,q,R)zn)].\delta^{n,i}\_{\*}(t,q,R)=\text{arg}\max\_{\delta}\Lambda^{n}\_{0}e^{-\kappa\_{n}\delta}\left[J(t,q,R)+z\_{n}\Psi\_{n}\left(\delta+m\_{n}(\delta)-p^{n,i}(t,q,R)-\frac{J(t,q,R)}{z\_{n}}\right)\right]. |  | (21) |

For an interior maximizer δ∗=δn∗​(p,J)\displaystyle\delta^{\*}=\delta^{\*}\_{n}(p,J), the first-order condition (FOC) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | zn​Φ​(μn​(δ∗;p,J)νn)​(1+mn′​(δ∗))=κn​(J+zn​Ψn​(μn​(δ∗;p,J))),z\_{n}\Phi\left(\frac{\mu\_{n}(\delta^{\*};p,J)}{\nu\_{n}}\right)\left(1+m^{\prime}\_{n}(\delta^{\*})\right)=\kappa\_{n}\left(J+z\_{n}\Psi\_{n}\big(\mu\_{n}(\delta^{\*};p,J)\big)\right), |  | (22) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | μn​(δ;p,J)=δ+mn​(δ)−p−Jzn.\mu\_{n}(\delta;p,J)=\delta+m\_{n}(\delta)-p-\frac{J}{z\_{n}}. |  | (23) |

When J≡0\displaystyle J\equiv 0 and mn≡0\displaystyle m^{n}\equiv 0 and νn→0\displaystyle\nu\_{n}\to 0, the model collapses to the standard OTC HJB (without rejection control) and the familiar
δ∗n,i=1/κn+𝒟±n​V\displaystyle\delta^{n,i}\_{\*}=1/\kappa\_{n}+\mathcal{D}^{n}\_{\pm}V regime (Guéant et al. [2013](#bib.bib13)).

The optimal decision arises from the comparison of the accept vs. reject value increments:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ∗n,i=1iffzn​(δ∗n,i+Yn,i​(δ∗n,i)−pn,i)≥J​(t,q,R).\ell^{n,i}\_{\*}=1\quad\text{iff}\quad z\_{n}\left(\delta^{n,i}\_{\*}+Y^{n,i}(\delta^{n,i}\_{\*})-p^{n,i}\right)\geq J(t,q,R). |  | (24) |

### 2.3 Adiabatic quadratic approximation

In our practical definition, the rejection score R\displaystyle R is an EMA of the rejection indicator and, therefore, tracks the rejection probability.
It is intentionally filtered and is expected to change slowly, maintaining stationarity.
The full problem thus couples a fast inventory control with a slow reputation state.
In the adiabatic regime, we approximate R\displaystyle R as quasi-static over the quoting horizon, set g(R)=:g\displaystyle g(R)=:g and drop R\displaystyle R-dependence from the value function.
In the self-consistent closure, we replace the continuation difference by a constant J≤0\displaystyle J\leq 0 calibrated to match the corresponding rejection rate.
HJB becomes inventory-only.

Following Bergault et al. ([2021](#bib.bib4)) we expand the Hamiltonians in p\displaystyle p up to the second order

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hn​(p,J)≃Hn​(0,J)+Hpn​(0,J)​p+12​Hp​pn​(0,J)​p2,H^{n}(p,J)\simeq H^{n}(0,J)+H^{n}\_{p}(0,J)p+\frac{1}{2}H^{n}\_{pp}(0,J)p^{2}, |  | (25) |

and assume a standard symmetric quadratic ansatz for the value function

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,q)=−A​(t)​q2−C​(t).V(t,q)=-A(t)q^{2}-C(t). |  | (26) |

Substituting into HJB and matching the coefficients of q2\displaystyle q^{2} yields the Riccati ODE for A​(t)\displaystyle A(t):

|  |  |  |  |
| --- | --- | --- | --- |
|  | A′​(t)+12​γ​σ2=4​g​A​(t)2​Σ​(J),Σ​(J):=∑n=1NHp​pn​(0,J).A^{\prime}(t)+\frac{1}{2}\gamma\sigma^{2}=4gA(t)^{2}\Sigma(J),\qquad\Sigma(J):=\sum\_{n=1}^{N}H^{n}\_{pp}(0,J). |  | (27) |

In the stationary (long-horizon) limit A​(t)′=0\displaystyle A(t)^{\prime}=0, the concave branch gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | A=γ​σ28​g​Σ​(J).A=\sqrt{\frac{\gamma\sigma^{2}}{8g\Sigma(J)}}. |  | (28) |

A free constant does not influence the controls.
Given A\displaystyle A, one can compute pn,i​(q)=A​(zn±2​q)\displaystyle p^{n,i}(q)=A(z\_{n}\pm 2q) and obtain quotes by solving FOC.

#### Special case: constant slippage

We now specialize the adiabatic-quadratic approximation to constant (quote-independent) slippage:

|  |  |  |  |
| --- | --- | --- | --- |
|  | mn​(δ)≡−θn,θn≥0,m\_{n}(\delta)\equiv-\theta\_{n},\qquad\theta\_{n}\geq 0, |  | (29) |

which yields explicit forms for Hamiltonian derivatives and particularly simple controls.
In this case,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hn​(p,J)=Λ0n​e−κn​δ​[J+zn​Ψn​(δ−θn−p−Jzn)].H^{n}(p,J)=\Lambda\_{0}^{n}e^{-\kappa\_{n}\delta}\left[J+z\_{n}\Psi\_{n}\left(\delta-\theta\_{n}-p-\frac{J}{z\_{n}}\right)\right]. |  | (30) |

Setting u=δ−p\displaystyle u=\delta-p yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hn​(p,J)=e−κn​p​Hn​(0,J),H^{n}(p,J)=e^{-\kappa\_{n}p}H^{n}(0,J), |  | (31) |

and, therefore, the maximizer satisfies the exact shift rule

|  |  |  |  |
| --- | --- | --- | --- |
|  | δn∗​(p,J)=δ¯n​(J)+p,δ¯n​(J):=δn∗​(0,J).\delta^{\*}\_{n}(p,J)=\bar{\delta}\_{n}(J)+p,\qquad\bar{\delta}\_{n}(J):=\delta^{\*}\_{n}(0,J). |  | (32) |

Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ¯n​(J):=δ¯n​(J)−θn−Jzn,μ~n​(J):=μ¯n​(J)νn.\bar{\mu}\_{n}(J):=\bar{\delta}\_{n}(J)-\theta\_{n}-\frac{J}{z\_{n}},\qquad\tilde{\mu}\_{n}(J):=\frac{\bar{\mu}\_{n}(J)}{\nu\_{n}}. |  | (33) |

The myopic optimizer at p=0\displaystyle p=0 satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(μ~n)=κn​(Jzn+νn​(ϕ​(μ~n)+μ~n​Φ​(μ~n))),\Phi(\tilde{\mu}\_{n})=\kappa\_{n}\left(\frac{J}{z\_{n}}+\nu\_{n}\big(\phi(\tilde{\mu}\_{n})+\tilde{\mu}\_{n}\Phi(\tilde{\mu}\_{n})\big)\right), |  | (34) |

and once solved for μ~n\displaystyle\tilde{\mu}\_{n},

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ¯n​(J)=θn+Jzn+νn​μ~n​(J).\bar{\delta}\_{n}(J)=\theta\_{n}+\frac{J}{z\_{n}}+\nu\_{n}\tilde{\mu}\_{n}(J). |  | (35) |

Using the FOC at the optimizer, we find

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hp​pn​(0,J)=Λ0n​e−κn​δ¯n​(J)​zn​κn​Φ​(μ~n​(J)).H^{n}\_{pp}(0,J)=\Lambda^{n}\_{0}e^{-\kappa\_{n}\bar{\delta}\_{n}(J)}z\_{n}\kappa\_{n}\Phi\big(\tilde{\mu}\_{n}(J)\big). |  | (36) |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ​(J)=∑n=1NΛ0n​e−κn​δ¯n​(J)​zn​κn​Φ​(μ~n​(J)).\Sigma(J)=\sum\_{n=1}^{N}\Lambda\_{0}^{n}e^{-\kappa\_{n}\bar{\delta}\_{n}(J)}z\_{n}\kappa\_{n}\Phi\big(\tilde{\mu}\_{n}(J)\big). |  | (37) |

By the shift rule, the adiabatic optimal quotes become explicit

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ∗n,i=δ¯n​(J)+A​(zn±2​q),\delta^{n,i}\_{\*}=\bar{\delta}\_{n}(J)+A(z\_{n}\pm 2q), |  | (38) |

and for trade acceptance/rejection controls we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ∗n,i=1iffYn,i≥y∗n,i:=Jzn−δ¯n​(J).\ell^{n,i}\_{\*}=1\quad\text{iff}\quad Y^{n,i}\geq y^{n,i}\_{\*}:=\frac{J}{z\_{n}}-\bar{\delta}\_{n}(J). |  | (39) |

#### Calibration of J\displaystyle J by average rejection rate

At p=0\displaystyle p=0, the reject probability under the optimal quote in size bucket n\displaystyle n is 1−Φ​(μ~n​(J))\displaystyle 1-\Phi\big(\tilde{\mu}\_{n}(J)\big).
A natural intensity-weighted average rejection rate is, therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | r¯​(J)=∑n=1NΛ0n​e−κn​δ¯n​(J)​(1−Φ​(μ~n​(J)))∑n=1NΛ0n​e−κn​δ¯n​(J).\bar{r}(J)=\frac{\sum\_{n=1}^{N}\Lambda\_{0}^{n}e^{-\kappa\_{n}\bar{\delta}\_{n}(J)}\left(1-\Phi\big(\tilde{\mu}\_{n}(J)\big)\right)}{\sum\_{n=1}^{N}\Lambda\_{0}^{n}e^{-\kappa\_{n}\bar{\delta}\_{n}(J)}}. |  | (40) |

Then we set J\displaystyle J such that r¯​(J)=R\displaystyle\bar{r}(J)=R.
Interpretationally, J\displaystyle J plays the role of a shadow continuation loss associated with a rejection.
Under slow reputation dynamics, we solve the fast inventory-control problem at frozen R\displaystyle R, compute the resulting stationary reject frequency r¯​(J)\displaystyle\bar{r}(J),
and choose J\displaystyle J so that this stationary reject frequency matches the current reputation level.
This provides a self-consistent local closure linking the fast control problem to the slow reputation state.

![Refer to caption](2603.07752v1/x2.png)


Figure 2: 
Top of book (z=z1\displaystyle z=z\_{1}) spread and rejection probability of optimal MM facing toxic flow with unrestricted rejection and no reputation feedback as a function of latency.
The top dashed line corresponds to the spread with toxic flow, but no rejection, and the bottom dashed line shows the spread without toxicity and without rejection.
Parameters in the text.

![Refer to caption](2603.07752v1/x3.png)


Figure 3: 
Bid and ask unrestricted rejection thresholds for trade requests of size z1\displaystyle z\_{1} as functions of inventory for optimal MM facing flow with toxicity function
mn​(δ)=−0.1​exp⁡(−0.5​δ)\displaystyle m\_{n}(\delta)=-0.1\exp(-0.5\delta) and latency window τn=0.5\displaystyle\tau\_{n}=0.5 s.
Other parameters in the text.

### 2.4 Numerical examples

As an illustration, consider a standard size-ladder of Δn=(1,2,5,10,20)\displaystyle\Delta^{n}=(1,2,5,10,20) M notional and an exponential intensity function
with Λ0n=(2000,800,600,400,100)\displaystyle\Lambda\_{0}^{n}=(2000,800,600,400,100) day-1 and κn=(3.0,2.5,2.0,1.5,1.0)\displaystyle\kappa\_{n}=(3.0,2.5,2.0,1.5,1.0) bp-1.
Here bp stands for basis points.666This implies GBM while we deal here with simple Brownian motion.
The difference is negligible in FX market making due to short trading horizons.
This set of parameters corresponds to a liquid currency pair with a daily turnover of ≃4\displaystyle\simeq 4 billion notional and a top-of-book spread of ≃0.7\displaystyle\simeq 0.7 bp.
We also assume a daily volatility of 100\displaystyle 100 bp and a risk aversion coefficient of γ=10−3\displaystyle\gamma=10^{-3} bp-1 M-1.

We begin without rejection feedback and set a small constant toxicity of θn=0.1\displaystyle\theta\_{n}=0.1 bp across sizes.
Figure [2](#S2.F2 "Figure 2 ‣ Calibration of 𝐽 by average rejection rate ‣ 2.3 Adiabatic quadratic approximation ‣ 2 Unconstrained rejection as an arrival-time binary decision ‣ Dynamic slippage control and rejection feedback in spot FX market making") demonstrates that if the quote-to-received-request latency is capped at 100 ms, there is no point for the dealer to reject at these parameters.
777The corresponding one-dimensional HJB is solved numerically.
Understandably, the optimal spread is wider than without toxicity.
With increasing latency, the MM starts rejecting, and the spread tightens, a well-known phenomenon (Oomen [2017a](#bib.bib16), [b](#bib.bib17), Cartea et al. [2019](#bib.bib8)).
Rejection thresholds are not sensitive to inventory in this constant-toxicity setting.
To introduce inventory dependence, we next use a quote-dependent toxicity specification mn​(δ)=−θn​e−βn​δ\displaystyle m\_{n}(\delta)=-\theta\_{n}e^{-\beta\_{n}\delta},
and set βn=0.5\displaystyle\beta\_{n}=0.5 bp-1, as shown in Figure [3](#S2.F3 "Figure 3 ‣ Calibration of 𝐽 by average rejection rate ‣ 2.3 Adiabatic quadratic approximation ‣ 2 Unconstrained rejection as an arrival-time binary decision ‣ Dynamic slippage control and rejection feedback in spot FX market making").
Rejection thresholds remain relatively deep, indicating that even an unconstrained MM does not reject immediately upon observing adverse slippage.

![Refer to caption](2603.07752v1/x4.png)


Figure 4: 
Optimal top of book spread and rejection probability as functions of the rejection score R\displaystyle R for zero inventory.
Parameters in the text.

![Refer to caption](2603.07752v1/x5.png)


Figure 5: 
Stationary top of book spread and rejection probability as functions of the rejection score decay parameter ρg\displaystyle\rho\_{g}, such that g​(R)=exp⁡(−ρg​R)\displaystyle g(R)=\exp(-\rho\_{g}R).
Parameters in the text.

Now consider optimal market making with rejection feedback.
We set EMA smoothing parameter to ρ=0.01\displaystyle\rho=0.01 and let g​(R)=exp⁡(−ρg​R)\displaystyle g(R)=\exp(-\rho\_{g}R) with ρg=0.1\displaystyle\rho\_{g}=0.1.
We also assume that τn=0.5\displaystyle\tau\_{n}=0.5 s and βn=0.3\displaystyle\beta\_{n}=0.3 bp-1.
All other parameters are the same as defined above.
Figure [4](#S2.F4 "Figure 4 ‣ 2.4 Numerical examples ‣ 2 Unconstrained rejection as an arrival-time binary decision ‣ Dynamic slippage control and rejection feedback in spot FX market making") illustrates a mechanism that may appear counter-intuitive at first: when the rejection score R\displaystyle R is high, the dealer tightens spreads yet becomes more selective ex post.
The reason is that, under adiabatic approximation, a higher R\displaystyle R reduces future flow through g​(R)\displaystyle g(R), while the continuation loss from an additional rejection becomes smaller in magnitude.
Tighter quoting then helps restore reputation faster through a higher arrival rate and hence a faster dilution of past rejections in calendar time.
This “repair-exploit” incentive to tighten in order to restore reputation faster while using the optionality of unconditional rejection to filter losses is a
structural feature of the model and provides a motivation for considering fair protocols that attenuate the embedded one-sided option value.
888Changing R\displaystyle R to be driven by rejections alone can help as well.

At the same time, fast reputation repair implies staying close to stationarity.
From the EMA update, the conditional mean change per request is ρ​(r¯−R)\displaystyle\rho(\bar{r}-R), where r¯\displaystyle\bar{r} is the intensity-weighted reject probability.
Thus in calendar time R˙≈ρ​λ​(q,R)​(r¯​(q,R)−R)\displaystyle\dot{R}\approx\rho\lambda(q,R)\left(\bar{r}(q,R)-R\right) with λ​(q,R)=∑λn,i​(q,R)\displaystyle\lambda(q,R)=\sum\lambda^{n,i}(q,R).
Stationary reputation levels satisfy the fixed-point relation (for fixed inventory q\displaystyle q)

|  |  |  |  |
| --- | --- | --- | --- |
|  | R∗=r¯​(q,R∗),R^{\*}=\bar{r}(q,R^{\*}), |  | (41) |

which is independent of λ\displaystyle\lambda, while λ​ρ\displaystyle\lambda\rho controls the speed of convergence to R∗\displaystyle R^{\*}.
Figure [5](#S2.F5 "Figure 5 ‣ 2.4 Numerical examples ‣ 2 Unconstrained rejection as an arrival-time binary decision ‣ Dynamic slippage control and rejection feedback in spot FX market making") demonstrates that in the stationary state, the rejection probability actually decreases and the spread widens
when we increase the reputation-induced flow decay parameter ρg\displaystyle\rho\_{g}, as expected.
In other words, the dealer will try to avoid rejection on average, even unconditionally, in the presence of reputation feedback.

Finally, we check the validity of the adiabatic quadratic approximation.
For our parameter set (with ρg=0.1\displaystyle\rho\_{g}=0.1), the equilibrium reputation level is R∗≃0.03\displaystyle R^{\*}\simeq 0.03.
This is the value we use to evaluate pricing in Figure [6](#S2.F6 "Figure 6 ‣ 2.4 Numerical examples ‣ 2 Unconstrained rejection as an arrival-time binary decision ‣ Dynamic slippage control and rejection feedback in spot FX market making").
The accuracy is reasonable, particularly for small inventories (comparison is only demonstrated for the smallest size bucket z1\displaystyle z\_{1}).
We have also verified rejection thresholds and found a good correspondence (not shown).

![Refer to caption](2603.07752v1/x6.png)


Figure 6: 
Optimal pricing as a function of inventory under a stationary rejection score.
Parameters in the text.
Lighter colour shades correspond to larger values of zn\displaystyle{z\_{n}} in the ladder.
Dashed lines show adiabatic quadratic approximation for size z1\displaystyle z\_{1}.

## 3 Towards fair execution

Reputation feedback ensures that excessive rejection practice is penalized.
One can even introduce dedicated reputation-dependent penalties into the utility function to gain more control.
However, the question of rejection fairness will still remain because the decision is with the dealer while the opportunity cost is with the client,
particularly if the dealer rejects adverse selection but harvests favorable selection.
A number of protocols have been discussed in detail by Oomen ([2017b](#bib.bib17)) offering fairness via decision symmetry and/or fill price adjustments.
Under certain scenarios, the benefit of rejection can totally disappear, at least theoretically,999For example, under quadratic inventory penalty and symmetric rejection boundary without adverse selection, as demonstrated by Olding ([2022](#bib.bib15)).
so the modelling framework is as important as the policy design.

So far, we have defined slippage tolerance as a function of the reference mid-price move over the latency window.
The approach is aligned with “fairness” narratives, yet in most OTC FX implementations, the price check is expressed
against the dealer’s own price stream.
This is precisely the object used in standard protocol definitions (Oomen [2017a](#bib.bib16)).
The goal of this section is to replace mid-move marks by dealer-quote-move marks and embed fair execution protocols into the
dynamic control framework with reputation feedback and inventory risk.

We begin by introducing the sign-adjusted quote move

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ytn,i:=±(Stn,i−St−τnn,i),Y^{n,i}\_{t}:=\pm\left(S^{n,i}\_{t}-S^{n,i}\_{t-\tau\_{n}}\right), |  | (42) |

so that Y>0\displaystyle Y>0 means the move is in the dealer’s favour, as before.
We retain the Gaussian-mark assumption (now interpreted as a distribution for own-quote revisions):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yn,i​(δ)=mn​(δ)+νn​ξ,ξ∼𝒩​(0,1),νn=σ​τn.Y^{n,i}(\delta)=m\_{n}(\delta)+\nu\_{n}\xi,\qquad\xi\sim\mathcal{N}(0,1),\qquad\nu\_{n}=\sigma\sqrt{\tau\_{n}}. |  | (43) |

At this point, one should note that the quote move may in principle contain both exogenous market motion and endogenous quote revisions generated by the dealer’s own policy updates.
In the present tractable formulation, we treat the valudation mark Ytn,i\displaystyle Y^{n,i}\_{t} as an exogenous effective quote-revision variable with conditional law mn​(δ)+νn​ξ\displaystyle m\_{n}(\delta)+\nu\_{n}\xi.
Equivalently, one may view Sn,i\displaystyle S^{n,i} here as the reference quote stream used for validation,101010Desks often maintain reference streams. with the control frozen over the latency window on the decision scale.
This approximation preserves the dynamic-programming structure while aligning the validation rule with standard OTC protocol definitions.
All the reputation/inventory machinery from the previous section remains unchanged; only the economic mapping from Y\displaystyle Y to execution P&L
is modified to reflect the chosen protocol.

### 3.1 Symmetric tolerance with capped slippage

Following Oomen ([2017b](#bib.bib17)), we consider the execution policy with symmetric tolerance ϵ\displaystyle\epsilon:

* •

  Reject if Y<−ϵ\displaystyle Y<-\epsilon .
* •

  Accept on-rate if −ϵ≤Y≤ϵ\displaystyle-\epsilon\leq Y\leq\epsilon (dealer keeps the realized slippage).
* •

  Accept with rebate if Y>ϵ\displaystyle Y>\epsilon (dealer’s favourable slippage is capped at ϵ\displaystyle\epsilon).

Equivalently, conditional on acceptance, the dealer’s slippage term becomes min⁡(Y,ϵ)\displaystyle\min(Y,\epsilon) with
ϵ\displaystyle\epsilon being one of the dealer’s controls.
This protocol is not statistically symmetric in the realized slippage, but it is economically symmetric in the sense that extreme favorable slippage is rebated while extreme adverse slippage leads to rejection.
It is therefore comparatively easy to communicate and defend, while remaining rich enough to illustrate the optimal-control and embedded-option viewpoints, as shown in Figure [7](#S3.F7 "Figure 7 ‣ 3.1 Symmetric tolerance with capped slippage ‣ 3 Towards fair execution ‣ Dynamic slippage control and rejection feedback in spot FX market making").

![Refer to caption](2603.07752v1/x7.png)


Figure 7: 
Latency mark Y∼𝒩​(mn​(δ),νn2)\displaystyle Y\sim\mathcal{N}(m\_{n}(\delta),\nu\_{n}^{2}) and embedded-option view of request-level payoff for fair rejection policy as described in the text.
For clarity, side indices are suppressed in the figure; in the model, the corresponding marginal value pn,i​(t,q,R)\displaystyle p^{n,i}(t,q,R) remains side dependent.
Red dashed lines depict optimal decision thresholds: the request is rejected when Y<−ϵn​(q,R)\displaystyle Y<-\epsilon^{n}(q,R); when Y>ϵn​(q,R)\displaystyle Y>\epsilon^{n}(q,R),
the request is accepted with price improvement for the client.

At state (t,q,R)\displaystyle(t,q,R) we define, as before, J=J​(t,q,R)=V​(t,q,Rrej​(R))−V​(t,q,R)\displaystyle J=J(t,q,R)=V(t,q,R\_{\text{rej}}(R))-V(t,q,R) and p=pn,i​(t,q,R)\displaystyle p=p^{n,i}(t,q,R)
being the appropriate accept marginals 𝒟±n​V​(t,q,R)\displaystyle\mathcal{D}^{n}\_{\pm}V(t,q,R).
Given (δ,ϵ)\displaystyle(\delta,\epsilon), a single request contribution (inside the intensity-weighted Hamiltonian) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | J⋅𝟏Y<−ϵ+zn​(δ−p+min⁡(Y,ϵ))⋅𝟏Y≥−ϵ.J\cdot\mathbf{1}\_{Y<-\epsilon}+z\_{n}\left(\delta-p+\min(Y,\epsilon)\right)\cdot\mathbf{1}\_{Y\geq-\epsilon}. |  | (44) |

Define the standardized cutoffs

|  |  |  |  |
| --- | --- | --- | --- |
|  | an=−ϵ−mnνn,bn=ϵ−mnνna\_{n}=\frac{-\epsilon-m\_{n}}{\nu\_{n}},\qquad b\_{n}=\frac{\epsilon-m\_{n}}{\nu\_{n}} |  | (45) |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Y<−ϵ)=Φ​(an),ℙ​(−ϵ≤Y≤ϵ)=Φ​(bn)−Φ​(an),ℙ​(Y>ϵ)=1−Φ​(bn),\mathbb{P}(Y<-\epsilon)=\Phi(a\_{n}),\qquad\mathbb{P}(-\epsilon\leq Y\leq\epsilon)=\Phi(b\_{n})-\Phi(a\_{n}),\qquad\mathbb{P}(Y>\epsilon)=1-\Phi(b\_{n}), |  | (46) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Y⋅𝟏−ϵ≤Y≤ϵ]=mn​(Φ​(bn)−Φ​(an))+νn​(ϕ​(an)−ϕ​(bn)).\mathbb{E}\left[Y\cdot\mathbf{1}\_{-\epsilon\leq Y\leq\epsilon}\right]=m\_{n}\left(\Phi(b\_{n})-\Phi(a\_{n})\right)+\nu\_{n}\left(\phi(a\_{n})-\phi(b\_{n})\right). |  | (47) |

So the closed-form expected increment is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒢n​(δ,ϵ;p,J)=J​Φ​(an)+zn​(δ−p)​Bn+zn​Cn,\mathcal{G}\_{n}(\delta,\epsilon;p,J)=J\Phi(a\_{n})+z\_{n}(\delta-p)B\_{n}+z\_{n}C\_{n}, |  | (48) |

where we have introduced

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bn=1−Φ​(an),Cn=mn​(Φ​(bn)−Φ​(an))+νn​(ϕ​(an)−ϕ​(bn))+ϵ​(1−Φ​(bn)).B\_{n}=1-\Phi(a\_{n}),\qquad C\_{n}=m\_{n}\left(\Phi(b\_{n})-\Phi(a\_{n})\right)+\nu\_{n}\left(\phi(a\_{n})-\phi(b\_{n})\right)+\epsilon\left(1-\Phi(b\_{n})\right). |  | (49) |

The bucket Hamiltonian becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hn​(p,J):=supδ∈ℝ,ϵ≥0Λ0n​e−κn​δ​𝒢n​(δ,ϵ;p,J),H^{n}(p,J):=\sup\_{\delta\in\mathbb{R},\epsilon\geq 0}\Lambda\_{0}^{n}e^{-\kappa\_{n}\delta}\mathcal{G}\_{n}(\delta,\epsilon;p,J), |  | (50) |

to be substituted into the reduced HJB of Eq. [20](#S2.E20 "In 2.2 HJB and optimal controls ‣ 2 Unconstrained rejection as an arrival-time binary decision ‣ Dynamic slippage control and rejection feedback in spot FX market making").

### 3.2 Adiabatic quadratic approximation and constant slippage

The logic is the same as with unconstrained rejections.
We freeze reputation and replace the state-dependent reject jump J​(t,q,R)\displaystyle J(t,q,R) by a constant J≤0\displaystyle J\leq 0 defined with self-consistent adiabatic closure.
This yields an inventory-only HJB, which is solved using second-order Hamiltonian expansion and quadratic ansatz for the value function.
Main findings remain the same.
Under constant slippage, mn​(δ)≡−θn\displaystyle m\_{n}(\delta)\equiv-\theta\_{n}, we observe significant simplifications:

* •

  Translational invariance in the shadow price p\displaystyle p (hence a shift rule for optimal quotes).
* •

  Closed-form relations for Hamiltonian derivatives in terms of the myopic optimizer at p=0\displaystyle p=0.

For fixed ϵ\displaystyle\epsilon and p\displaystyle p, the bucket objective is

|  |  |  |  |
| --- | --- | --- | --- |
|  | fn​(δ,ϵ;p,J)=Λ0n​e−κn​δ​𝒢n​(δ,ϵ;p,J),f\_{n}(\delta,\epsilon;p,J)=\Lambda^{n}\_{0}e^{-\kappa\_{n}\delta}\mathcal{G}\_{n}(\delta,\epsilon;p,J), |  | (51) |

which is the exponential intensity multiplied by an affine function of δ\displaystyle\delta.
Its interior maximizer is explicit:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δn∗​(p,ϵ,J)=p+δ¯n​(ϵ,J)=p+(1κn−J​Φ​(an​(ϵ))+zn​Cn​(ϵ)zn​Bn​(ϵ)).\delta^{\*}\_{n}(p,\epsilon,J)=p+\bar{\delta}\_{n}(\epsilon,J)=p+\left(\frac{1}{\kappa\_{n}}-\frac{J\Phi\big(a\_{n}(\epsilon)\big)+z\_{n}C\_{n}(\epsilon)}{z\_{n}B\_{n}(\epsilon)}\right). |  | (52) |

Substituting δ=δn∗(0,ϵ,J)=:δ¯n(ϵ,J)\displaystyle\delta=\delta^{\*}\_{n}(0,\epsilon,J)=:\bar{\delta}\_{n}(\epsilon,J) into the objective yields a one-dimensional maximization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ϵ¯n​(J),δ¯n​(J))∈arg​maxϵ≥0⁡fn​(δ¯n​(ϵ,J),ϵ,0,J),δ¯n​(J):=δ¯n​(ϵ¯n​(J),J).\left(\bar{\epsilon}\_{n}(J),\bar{\delta}\_{n}(J)\right)\in\text{arg}\max\_{\epsilon\geq 0}f\_{n}\left(\bar{\delta}\_{n}(\epsilon,J),\epsilon,0,J\right),\qquad\bar{\delta}\_{n}(J):=\bar{\delta}\_{n}(\bar{\epsilon}\_{n}(J),J). |  | (53) |

There is generally no closed form for ϵ¯n​(J)\displaystyle\bar{\epsilon}\_{n}(J), but numerical 1D maximization is cheap.

Because mn\displaystyle m\_{n}, Cn\displaystyle C\_{n} and Bn\displaystyle B\_{n} do not depend on δ\displaystyle\delta, the Hamiltonian depends on p\displaystyle p only through the combination u=δ−p\displaystyle u=\delta-p.
Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hn​(p,J)=e−κn​p​Hn​(0,J),H^{n}(p,J)=e^{-\kappa\_{n}p}H^{n}(0,J), |  | (54) |

as before.
Moreover, using FOC at the optimizer yields a particularly simple identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hp​pn​(0,J)=Λ0n​e−κn​δ¯n​(J)​zn​κn​Bn​(ϵ¯n​(J)).H^{n}\_{pp}(0,J)=\Lambda^{n}\_{0}e^{-\kappa\_{n}\bar{\delta}\_{n}(J)}z\_{n}\kappa\_{n}B\_{n}(\bar{\epsilon}\_{n}(J)). |  | (55) |

This is a direct analogue of the earlier formula for unconstrained rejections, with the acceptance probability Φ​(μ~n)\displaystyle\Phi(\tilde{\mu}\_{n})
replaced by the protocol acceptance probability Bn​(ϵ¯n)\displaystyle B\_{n}(\bar{\epsilon}\_{n}).
With this substitution, optimal quotes are still given by Eq. [38](#S2.E38 "In Special case: constant slippage ‣ 2.3 Adiabatic quadratic approximation ‣ 2 Unconstrained rejection as an arrival-time binary decision ‣ Dynamic slippage control and rejection feedback in spot FX market making"), and fair control is a symmetric tolerance

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵn∗=ϵ¯n​(J).\epsilon^{\*}\_{n}=\bar{\epsilon}\_{n}(J). |  | (56) |

In order to ensure self-consistency for reputation under the protocol, we note that with multiple buckets, a natural closure is the intensity-weighted
average rejection probability at the myopic point p=0\displaystyle p=0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | r¯​(J)=∑n=1NΛ0ne−κn​δ¯n​(J)rn(J))∑n=1NΛ0n​e−κn​δ¯n​(J),rn​(J):=ℙ​(Y<−ϵ¯n​(J))=Φ​(an​(ϵ¯n​(J))).\bar{r}(J)=\frac{\sum\_{n=1}^{N}\Lambda^{n}\_{0}e^{-\kappa\_{n}\bar{\delta}\_{n}(J)}r\_{n}(J))}{\sum\_{n=1}^{N}\Lambda^{n}\_{0}e^{-\kappa\_{n}\bar{\delta}\_{n}(J)}},\qquad r\_{n}(J):=\mathbb{P}(Y<-\bar{\epsilon}\_{n}(J))=\Phi(a\_{n}(\bar{\epsilon}\_{n}(J))). |  | (57) |

J\displaystyle J is calibrated by solving r¯​(J)=R\displaystyle\bar{r}(J)=R, as before.

![Refer to caption](2603.07752v1/x8.png)


Figure 8: 
Optimal stationary value function V​(0,q,R)\displaystyle V(0,q,R) for symmetric tolerance with capped slippage protocol and rejection feedback.
Parameters in the text.

### 3.3 Numerical examples

Here we consider the same basic parameter set as earlier, with specifics: θn=0.1\displaystyle\theta\_{n}=0.1 bp, τn≡τ=0.5\displaystyle\tau\_{n}\equiv\tau=0.5 s, ρ=0.01\displaystyle\rho=0.01, ρg=0.1\displaystyle\rho\_{g}=0.1.
The dealer controls (δ,ϵ)\displaystyle(\delta,\epsilon).
Figure [8](#S3.F8 "Figure 8 ‣ 3.2 Adiabatic quadratic approximation and constant slippage ‣ 3 Towards fair execution ‣ Dynamic slippage control and rejection feedback in spot FX market making") illustrates the corresponding stationary value function.
The gradient toward reducing inventory and improving reputation is very clear.
Table [1](#S3.T1 "Table 1 ‣ 3.3 Numerical examples ‣ 3 Towards fair execution ‣ Dynamic slippage control and rejection feedback in spot FX market making") further compares different optimal protocols with and without reputation feedback for an intentionally large latency setting of τ=1\displaystyle\tau=1 s and a constant slippage of θn=0.1\displaystyle\theta\_{n}=0.1 bp (except the reference entry with no adverse selection where θn=0\displaystyle\theta\_{n}=0).
The results were obtained by numerically solving the corresponding HJB.
We observe that adverse selection significantly harms performance, and the MM responds by widening spreads.
With unconstrained rejections, the utility improves, but clearly at the expense of a high reject rate.
The symmetric protocol results in a materially lower reject ratio and a smaller utility improvement due to rebates.
It is important to note that the optimal threshold level is very reasonable in this case and corresponds to approximately half the top-of-book spread.
Reputation feedback causes both protocols to reduce rejections dramatically.

| Model | ρg\displaystyle\rho\_{g} | Spread (bp) | Threshold (bp) | Rejection | Utility111111V​(0,0,R∗)\displaystyle V(0,0,R^{\*}). |
| --- | --- | --- | --- | --- | --- |
| no rejection, no adverse selection | 0\displaystyle 0 | 0.69\displaystyle 0.69 | ∞\displaystyle\infty | 0\displaystyle 0 | 235.4\displaystyle 235.4 |
| no rejection | 0\displaystyle 0 | 0.89\displaystyle 0.89 | ∞\displaystyle\infty | 0\displaystyle 0 | 195.1\displaystyle 195.1 |
| unconstrained | 0\displaystyle 0 | 0.53\displaystyle 0.53 | 0.25\displaystyle 0.25 | 0.33\displaystyle 0.33 | 201.7\displaystyle 201.7 |
|  | 0.05\displaystyle 0.05 | 0.64\displaystyle 0.64 | 0.40\displaystyle 0.40 | 0.22\displaystyle 0.22 | 199.5\displaystyle 199.5 |
|  | 0.10\displaystyle 0.10 | 0.72\displaystyle 0.72 | 0.54\displaystyle 0.54 | 0.15\displaystyle 0.15 | 198.3\displaystyle 198.3 |
|  | 0.15\displaystyle 0.15 | 0.76\displaystyle 0.76 | 0.67\displaystyle 0.67 | 0.10\displaystyle 0.10 | 197.4\displaystyle 197.4 |
|  | 0.20\displaystyle 0.20 | 0.80\displaystyle 0.80 | 0.79\displaystyle 0.79 | 0.06\displaystyle 0.06 | 196.9\displaystyle 196.9 |
| symmetric | 0\displaystyle 0 | 0.71\displaystyle 0.71 | 0.43\displaystyle 0.43 | 0.17\displaystyle 0.17 | 199.4\displaystyle 199.4 |
|  | 0.05\displaystyle 0.05 | 0.75\displaystyle 0.75 | 0.49\displaystyle 0.49 | 0.13\displaystyle 0.13 | 198.2\displaystyle 198.2 |
|  | 0.10\displaystyle 0.10 | 0.78\displaystyle 0.78 | 0.55\displaystyle 0.55 | 0.09\displaystyle 0.09 | 197.4\displaystyle 197.4 |
|  | 0.15\displaystyle 0.15 | 0.81\displaystyle 0.81 | 0.61\displaystyle 0.61 | 0.07\displaystyle 0.07 | 196.9\displaystyle 196.9 |
|  | 0.20\displaystyle 0.20 | 0.83\displaystyle 0.83 | 0.68\displaystyle 0.68 | 0.05\displaystyle 0.05 | 196.5\displaystyle 196.5 |

Table 1: Comparison of optimal trade acceptance/rejection protocols.
“Threshold” denotes the optimal one-sided rejection cutoff in the unconstrained model and the optimal symmetric tolerance ϵ\displaystyle\epsilon in the fair protocol.
Parameters are given in the text.

#### Simulation

Finally, we provide a Monte Carlo simulation of market making with adverse selection and reputation feedback under a stationary optimal policy.
We consider constant slippage here and assume that the mechanism is driven by endogenous adverse quote selection.
The simulator steps in units of latency τ\displaystyle\tau and models a single step as Δ​S∼𝒩​(0,σ2​τ)\displaystyle\Delta S\sim\mathcal{N}(0,\sigma^{2}\tau).
RFQs are then chosen with tilted intensities

|  |  |  |  |
| --- | --- | --- | --- |
|  | λn,i​(Δ​S)=λbasen,i​exp⁡(−αn​Yi),\lambda^{n,i}(\Delta S)=\lambda^{n,i}\_{\text{base}}\exp(-\alpha\_{n}Y^{i}), |  | (58) |

where Yi=±Δ​S\displaystyle Y^{i}=\pm\Delta S and
αn=θn/(σ2​τ)\displaystyle\alpha\_{n}=\theta\_{n}/(\sigma^{2}\tau) so that Y|RFQ∼𝒩​(−θn,σ2​τ)\displaystyle Y|\text{RFQ}\sim\mathcal{N}(-\theta\_{n},\sigma^{2}\tau).
In order to keep the unconditional RFQ rate unchanged, we include the intensity rescaling

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ0,adjn=Λ0n​exp⁡(−12​αn2​σ2​τ).\Lambda^{n}\_{0,\text{adj}}=\Lambda^{n}\_{0}\exp\left(-\frac{1}{2}\alpha\_{n}^{2}\sigma^{2}\tau\right). |  | (59) |

This rescaling exactly offsets the Gaussian exponential tilt because, under the untilted law, 𝔼​[exp⁡(−αn​Yi)]=exp⁡(12​αn2​σ2​τ)\displaystyle\mathbb{E}\left[\exp\left(-\alpha\_{n}Y^{i}\right)\right]=\exp\left(\tfrac{1}{2}\alpha^{2}\_{n}\sigma^{2}\tau\right).
Hence the unconditional RFQ arrival rate remains equal to the original baseline level.
The algorithm uses exact stationary controls obtained by numerically solving the corresponding HJB
and supports both the unrestricted and fair protocols.

![Refer to caption](2603.07752v1/x9.png)


Figure 9: 
Relaxation of the simulated rejection score (rejection-rate EMA) to the stationary state.
The mean rejection rate is optimal from the start, with the standard deviation decreasing as the stationary state is approached.
Parameters in the text.

![Refer to caption](2603.07752v1/x10.png)


Figure 10: 
Inventory risk adjusted P&L (optimization objective) as a function of the realized rejection rate at T=2.4\displaystyle T=2.4 hours.
Circles are averages of a thousand consecutive sorted realizations.
The dashed line corresponds to the stationary state.
Parameters in the text.

Simulation was run for the fair acceptance/rejection protocol with latency τn=0.5\displaystyle\tau\_{n}=0.5 s, constant slippage θn=0.1\displaystyle\theta\_{n}=0.1 bp and reputation parameters ρ=ρg=0.01\displaystyle\rho=\rho\_{g}=0.01, a total of 5⋅104\displaystyle 5\cdot 10^{4} trajectories.
Optimal controls from the HJB solution were passed to the simulator with initial conditions q=0\displaystyle q=0, R=0\displaystyle R=0.
Figure [9](#S3.F9 "Figure 9 ‣ Simulation ‣ 3.3 Numerical examples ‣ 3 Towards fair execution ‣ Dynamic slippage control and rejection feedback in spot FX market making") illustrates relaxation of the reputation variable to the stationary state as the dealer maintains the optimal rejection rate from the start.
Initially, with a low rejection score (small R\displaystyle R), the dealer is more flexible in their decision, as evidenced by the high standard deviation.
Figure [10](#S3.F10 "Figure 10 ‣ Simulation ‣ 3.3 Numerical examples ‣ 3 Towards fair execution ‣ Dynamic slippage control and rejection feedback in spot FX market making") demonstrates how the value function (inventory risk adjusted P&L) depends on the realized rejection rate.
This kind of plot can be verified empirically.

## 4 Concluding remarks

FX dealers respond to latency risk with spread widening and rejection protocols.
So far, these protocols have been a matter of design rather than optimization, with fairness and transparency being in the spotlight (GFXC [2024](#bib.bib12)).
In this paper, we provide a tractable framework that builds on the Avellaneda-Stoikov tradition ([2008](#bib.bib1)) and treats the rejection decision –
subject to fairness or protocol constraints – as an optimizable state-dependent control alongside quoting.
Optimal thresholds are found to be conservative, even in the presence of toxic flow, although the actual values depend on market conditions.
We have also introduced the so-called rejection-score feedback mechanism to model how frequent rejections can reduce subsequent client engagement.
Rejection-score-aware control makes the dealer even less inclined to reject in order to protect the flow.
An adiabatic quadratic approximation with self-consistent closure was suggested as a simple, practical way to calculate optimal controls.

## Acknowledgments

The author is grateful to Eric Mathew John (HSBC) for fruitful discussions and to Richard Anthony (HSBC) for support throughout the project and valuable comments.
The views expressed are those of the author and do not necessarily reflect the views or practices at HSBC.

## References

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
  Optimal quoting under adverse selection and price reading, arXiv:2508.20225 [q-fin.TR], 2025.
* Bergault et al. (2021)

  Bergault, P., Evangelista, D., Guéant, O. and Vieira, D.,
  Closed-form approximations in multi-asset market making.
  Appl. Math. Finance, 2021, 28, 101–142.
* Bergault and Guéant (2021)

  Bergault, P. and Guéant, O.,
  Size matters for otc market makers: general results and dimensionality reduction techniques.
  Math. Finance, 2021, 31, 279–322.
* Cartea et al. (2014)

  Cartea, Á, Jaimungal, S. and Ricci, J.,
  Buy low, sell high: A high frequency trading perspective.
  SIAM J. Financ. Math., 2014, 5, 415–444.
* Cartea et al. (2015)

  Cartea, Á, Jaimungal, S. and Penalva, J.,
  Algorithmic and High Frequency Trading, 2015
  (Cambridge University Press: Cambridge, United Kingdom).
* Cartea et al. (2019)

  Cartea, Á, Jaimungal, S. and Walton, J.,
  Foreign exchange markets with last look.
  Math. Financ. Econ., 2019, 13, 1–30.
* Cartea and Wang (2020)

  Cartea, Á and Wang, Y.,
  Market making with alpha signals.
  Int. J. Theor. Appl. Finance, 2020, 23, 2050016.
* Cartea and Sánchez-Betancourt (2021)

  Cartea, Á and Sánchez-Betancourt, L.,
  The shadow price of latency: Improving intraday fill ratios in foreign exchange markets.
  SIAM J. Financ. Math., 2021, 12, 254–294.
* Cartea et al. (2021)

  Cartea, Á, Jaimungal, S. and Sánchez-Betancourt, L.,
  Latency and liquidity risk.
  Int. J. Theor. Appl. Finance, 2021, 24, 2150035.
* GFXC (2024)

  Global Foreign Exchange Committee (GFXC),
  FX Global Code, 2024.
* Guéant et al. (2013)

  Guéant, O., Lehalle, C.-A. and Fernandez-Tapia, J.,
  Dealing with the inventory risk: a solution to the market making problem.
  Math. Financ. Econ., 2013, 7, 477–507.
* Guéant (2016)

  Guéant, O.,
  The Financial Mathematics of Market Liquidity: From optimal execution to market making, 2016
  (Chapman and Hall/CRC: Boca Raton, FL).
* Olding (2022)

  Olding, K.,
  Market making with and without last look. PhD thesis. University of Bath, United Kingdom, 2022.
* Oomen (2017a)

  Oomen, R.,
  Execution in an aggregator.
  Quant. Finance, 2017, 17, 383–404.
* Oomen (2017b)

  Oomen, R.,
  Last look.
  Quant. Finance, 2017, 17, 1057–1070.
* Stevenson (2016)

  Stevenson, J.,
  The value of millisecond expiry options in spot foreign exchange markets.
  J. Gov.  Regul., 2016, 5, 85–89.

BETA