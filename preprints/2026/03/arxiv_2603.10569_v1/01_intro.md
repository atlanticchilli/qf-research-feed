---
authors:
- Alexander Barzykin
doc_id: arxiv:2603.10569v1
family_id: arxiv:2603.10569
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic
  control model'
url_abs: http://arxiv.org/abs/2603.10569v1
url_html: https://arxiv.org/html/2603.10569v1
venue: arXiv q-fin
version: 1
year: 2026
---


Alexander Barzykin111HSBC, 8 Canada Square, Canary Wharf, London E14 5HQ, United Kingdom, alexander.barzykin@hsbc.com.

###### Abstract

We study market making in aggregator-routed RFQ markets where platform routing depends on slowly varying dealer performance scores.
We propose a two-tier stochastic control model that separates RFQ-level price competition from a macro routing layer:
tier A represents aggregator flow whose opportunity intensity is multiplied by a promotion gate driven by the dealer’s win score,
while tier B captures background flow that is not gated and does not update the score.
RFQs arrive in multiple sizes and the dealer chooses a size-ladder of bid/ask offsets; conditional on winning, trades earn spread minus an
adverse selection correction and contribute to inventory risk.
The resulting Hamilton-Jacobi-Bellman equation admits a reduced Bergault-Guéant operator form with explicit win/lose branches for the score on tier A.
Using the envelope-theorem argument, we express optimal controls through derivatives of the one-dimensional reduced Hamiltonians, yielding an interpretable mapping from optimal win probabilities to optimal offsets.
In the long-memory regime, we derive an adiabatic approximation that separates fast inventory dynamics from slow score dynamics.
A quadratic inventory ansatz and quadratic Hamiltonian expansion lead to a quasi-stationarity inventory-curvature scaling and a one-dimensional score drift field.
For steep (logistic) promotion gates, the score dynamics can exhibit fold bifurcations, bistability, and hysteresis, producing an endogenous “campaign vs. harvest” pattern in optimal quoting.
Numerical experiments confirm this behaviour and highlight the stabilizing role of background flow in maintaining inventory-mixing capacity even when the dealer is weakly promoted.

Key words: Market Making, Stochastic Optimal Control, Adverse Selection, Win Ratio, RFQ, Bifurcation, Bistability

## 1 Introduction

Multi-dealer request-for-quote (RFQ) protocols are central to dealer-to-client execution in several over-the-counter (OTC) markets, including foreign exchange (FX).
In an RFQ, a client requests prices from multiple liquidity providers (LPs) and either trades with one LP or does not trade at all.
In modern FX workflows, RFQs are frequently routed through aggregators that consolidate quotes and automate selection, creating an interaction between micro-level price competition inside each RFQ and macro-level flow allocation rules that determine which LPs are invited to compete and how frequently.

On the modelling side, stochastic optimal control approaches to market making combine inventory management with quote-dependent order arrivals [[21](#bib.bib21), [2](#bib.bib2), [20](#bib.bib20), [10](#bib.bib10)].
In OTC RFQ markets, an additional structural feature is size heterogeneity: an LP typically answers a menu of quotes for different notionals.
This leads naturally to multi-size ladder controls and to Hamilton-Jacobi-Bellman (HJB) equations with non-local (jump) operators indexed by trade size [[6](#bib.bib6)].
Empirical and structural studies on multi-dealer-to-client (MD2C) platforms (notably in corporate bonds) explicitly model how hit probabilities depend on the competitive set and on the number of solicited dealers, highlighting that “how many dealers are asked” is a first-order primitive in RFQ economics [[19](#bib.bib19)].
More recently, causal interventions have been used to study counterfactual pricing and revenue questions on MD2C platforms, bridging structural RFQ models with modern discriminative learning [[22](#bib.bib22)].

In FX, protocol design layer is particularly important.
First, the presence of last look (a short post-trade window in which an LP may accept or reject) affects both spreads and selection [[24](#bib.bib24), [11](#bib.bib11)].
Second, even without last look, the aggregator itself shapes adverse selection and incentives.
Oomen [[23](#bib.bib23)] argues that the “winner’s-curse” in an aggregator can strengthen as more LPs compete: the best displayed quote is more likely to be selected precisely in states that are unfavorable to the winning LP.
This provides an economic rationale for limiting the number of LPs exposed to each RFQ and for using routing and ranking rules rather than always inviting the full pool.
Recent work on broker performance evaluation and selection highlights the practical importance of quantitatively ranking execution providers using intraday cost models [[18](#bib.bib18)].
Related FX microstructure considerations, such as internalisation versus externalisation of client flow [[9](#bib.bib9), [3](#bib.bib3)] and informational risks that accompany competitive quoting [[4](#bib.bib4)], further motivate modelling the interaction between client access, dealer incentives, and platform design.

A growing modern literature examines competition among liquidity providers and the extent to which it can be represented in tractable control or equilibrium frameworks.
One approach treats competition in reduced form: a reference market maker optimises quotes while fill probabilities depend on differences versus exogenous competing quotes, yielding approximate closed-form solutions under linear-quadratic objectives [[8](#bib.bib8)].
Other works move to explicit strategic settings (e.g., Stackelberg or Nash structures), providing equilibrium characterisations for competitive liquidity provision [[15](#bib.bib15), [14](#bib.bib14), [17](#bib.bib17)].
A parallel strand uses reinforcement learning and agent-based models to study the emergence of tacit coordination in electronic markets and in MD2C-type dealer platforms, and the role of heterogeneity in mitigating such effects [[13](#bib.bib13), [12](#bib.bib12), [1](#bib.bib1), [16](#bib.bib16)].

Across these strands, two empirical facts stand out in aggregator-routed RFQ markets: (i) the competitive set is typically a subset of all eligible LPs and is often shaped by ranking, relationship, or platform-level “top list + exploration” logic;
(ii) inclusion and rank depend on slowly varying performance scores (e.g., long-run win ratio, response quality), which in turn depend on how aggressively the LP quotes.
While the RFQ micro-link is well captured by size-ladder market making [[6](#bib.bib6)] and the macro design layer is motivated by aggregator economics [[23](#bib.bib23)], there is limited academic control literature that treats platform shortlisting driven by a slow win-score as an explicit state variable feeding back into the LP’s future opportunity intensity.

This paper proposes a minimal two-scale model that links RFQ-level market making to aggregator routing via a slow win-score.
A key modelling choice is to start from the onset with two tiers of RFQ flow:

* •

  an aggregator tier (A), whose opportunity intensity is multiplied by a gate G​(R)G(R) driven by the LP’s score and whose outcomes update the score;
* •

  a background tier (B), representing residual client flow that is not gated by the platform score and does not update it.

This decomposition is motivated by practice: (a) only a subset of the firm’s franchise is routed through ranking-based shortlists; (b) inventory risk is managed against all trading opportunities, not only the ranked stream.
Analytically, the background tier plays a stabilising role: it provides a baseline level of inventory mixing even when G​(R)G(R) is small, and it allows the model to generate a “campaign vs. harvest” trade-off in which the LP can temporarily sacrifice edge on tier A to improve future access while still managing inventory through tier B.

We derive a reduced HJB in a Bergault-Guéant operator form, with explicit “win” and “lose” branches in the score for tier A, and standard jump operators for tier B.
Using an envelope-theorem argument, we express optimal controls through derivatives of scalar reduced Hamiltonians, giving a clean inverse mapping from optimal win probabilities to optimal offsets.
In the long-memory-EMA limit, the model separates into a fast inventory-control scale and a slow reputation-dynamics scale.
A quadratic inventory ansatz and quadratic Hamiltonian expansion à la Bergault et al. [[7](#bib.bib7)] yield an LQ-like closure, stationary Riccati scaling for the inventory curvature, and a one-dimensional reduced dynamics for the score that admits phase transitions and hysteresis under steep (logistic) promotion gates.

## 2 Model

The mid-price StS\_{t} is a martingale diffusion with volatility σ>0\sigma>0, assumed constant over a finite operational horizon [0,T][0,T] of the market maker.
The LP holds inventory qtq\_{t} and cash XtX\_{t}.
RFQs arrive in multiple sizes z∈𝒵={z1,…,zK}z\in\mathcal{Z}=\{z\_{1},\ldots,z\_{K}\}.
The LP chooses size- and side-dependent offsets to mid δzi,j​(t,q,R)\delta^{i,j}\_{z}(t,q,R), where i∈{A,B}i\in\{A,B\} denotes the tier (aggregator/background) and j∈{b,a}j\in\{b,a\} denotes the side (bid/ask).222Positive offset means wider quote.
Here RR is the long-term LP rating or score, defined below.
Given an RFQ opportunity of size zz and a quoted offset δ\delta, the LP wins with probability333We keep pzp\_{z} generic; logistic and structural erfc-type forms are natural candidates for numerical work.

|  |  |  |  |
| --- | --- | --- | --- |
|  | pz​(δ)∈(0,1),pz′​(δ)<0.p\_{z}(\delta)\in(0,1),\qquad p\_{z}^{\prime}(\delta)<0. |  | (1) |

Conditional on winning an RFQ of size zz at offset δ\delta, the expected mark-to-mid edge per unit size is modelled as δ+μz​(δ)\delta+\mu\_{z}(\delta), where μz​(δ)≤0\mu\_{z}(\delta)\leq 0 is an adverse-selection correction.
To keep the analysis focused on win-score feedback, we model only latency-type adverse selection as an instantaneous expected edge correction conditional on winning the RFQ and do not include additional post-trade price jumps.
A simple benchmark is constant negative slippage μz​(δ)≡−θz\mu\_{z}(\delta)\equiv-\theta\_{z}, with θz>0\theta\_{z}>0.

For each size zz, RFQ opportunities arrive (per side) at baseline intensities Λzi>0\Lambda\_{z}^{i}>0, assumed symmetric for simplicity.
Tier A opportunities are multiplied by a macro selection factor G​(R)≥0G(R)\geq 0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λzA​(R)=ΛzA​G​(R),λzB​(R)=ΛzB.\lambda\_{z}^{A}(R)=\Lambda\_{z}^{A}\,G(R),\qquad\lambda\_{z}^{B}(R)=\Lambda\_{z}^{B}. |  | (2) |

The gate G​(R)G(R) captures ranking-based shortlisting by an aggregator.
A stylized “top list + exploration” mechanism is: the NtopN\_{\mathrm{top}} highest-score LPs are always invited (promotion), and the remaining Nselect−NtopN\_{\mathrm{select}}-N\_{\mathrm{top}} invites are sampled at random from the rest (exploration).
Thus, an LP’s long-run score influences the probability of being invited and, therefore, the RFQ opportunity intensity.
The full environment is a game: win probabilities depend on the cross-sectional distribution of competitor quotes.
In the mean-field regime, this can be represented as a single-LP stochastic control with a monotone G​(R)G(R).

Let w∈{0,1}w\in\{0,1\} denote the win indicator on a tier A RFQ opportunity.
We update the score (EMA of wins) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R↦R±​(R):=(1−α)​R+α​w,R\mapsto R\_{\pm}(R):=(1-\alpha)R+\alpha w, |  | (3) |

where α∈(0,1)\alpha\in(0,1) and ±\pm correspond to w=1w=1 and 0, respectively.444One can introduce size-weighted updates with wz=z/zmaxw\_{z}=z/z\_{\max}.
Tier B outcomes do not update RR.
When α\alpha is small, the score evolves slowly relative to inventory dynamics.

We assume a standard linear wealth objective with quadratic inventory penalties [[10](#bib.bib10)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supδ𝔼​[XT+qT​ST−η2​qT2−γ2​σ2​∫0Tqt2​dt],\sup\_{\delta}\;\mathbb{E}\Big[X\_{T}+q\_{T}S\_{T}-\frac{\eta}{2}q\_{T}^{2}-\frac{\gamma}{2}\sigma^{2}\int\_{0}^{T}q\_{t}^{2}\,\,\mathrm{d}t\Big], |  | (4) |

with η,γ≥0\eta,\gamma\geq 0.

### 2.1 Reduced HJB

Let V​(t,x,q,S,R)V(t,x,q,S,R) denote the value function.
The standard reduction V​(t,x,q,S,R)=x+q​S+v​(t,q,R)V(t,x,q,S,R)=x+qS+v(t,q,R) eliminates explicit dependence on SS, with terminal condition
v​(T,q,R)=−η2​q2v(T,q,R)=-\frac{\eta}{2}q^{2}.
Define the lose-branch decrement and win-and-trade increments for tier A:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒ​(t,q,R)\displaystyle\mathcal{L}(t,q,R) | :=v​(t,q,R−​(R))−v​(t,q,R),\displaystyle:=v(t,q,R\_{-}(R))-v(t,q,R), |  | (5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΔzA,j​(t,q,R)\displaystyle\Delta^{A,j}\_{z}(t,q,R) | :=v​(t,q±z,R+​(R))−v​(t,q,R),\displaystyle:=v(t,q\pm z,R\_{+}(R))-v(t,q,R), |  | (6) |

where plus corresponds to bids and minus to asks, respectively.
Then for each size zz, define the tier-A Bergault-Guéant operator

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋzA​(Δ)=supδ∈ℝ{pz​(δ)​(z​(δ+μz​(δ))+Δ)+(1−pz​(δ))​ℒ}=ℒ+supδ∈ℝpz​(δ)​(z​(δ+μz​(δ))+Δ−ℒ).\mathcal{H}^{A}\_{z}(\Delta)=\sup\_{\delta\in\mathbb{R}}\Big\{p\_{z}(\delta)\big(z(\delta+\mu\_{z}(\delta))+\Delta\big)+\big(1-p\_{z}(\delta)\big)\mathcal{L}\Big\}=\mathcal{L}+\sup\_{\delta\in\mathbb{R}}p\_{z}(\delta)\Big(z(\delta+\mu\_{z}(\delta))+\Delta-\mathcal{L}\Big). |  | (7) |

The first equality makes explicit the win/lose mixture: with probability pz​(δ)p\_{z}(\delta) the dealer wins and trades, receiving spread and moving to (q±z,R+)(q\pm z,R\_{+}), while with probability 1−pz​(δ)1-p\_{z}(\delta) the dealer loses and only incurs the score downgrade (q,R−)(q,R\_{-}).
Since tier B does not update RR, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔzB,j​(t,q,R):=v​(t,q±z,R)−v​(t,q,R),\Delta^{B,j}\_{z}(t,q,R):=v(t,q\pm z,R)-v(t,q,R), |  | (8) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋzB​(Δ)=supδ∈ℝpz​(δ)​(z​(δ+μz​(δ))+Δ).\mathcal{H}^{B}\_{z}(\Delta)=\sup\_{\delta\in\mathbb{R}}p\_{z}(\delta)\Big(z(\delta+\mu\_{z}(\delta))+\Delta\Big). |  | (9) |

Assuming symmetric primitives across bid/ask (same Λz,pz,μz\Lambda\_{z},p\_{z},\mu\_{z}), the reduced HJB is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=∂tv−γ2​σ2​q2+∑z∈𝒵,i∈{A,B},j∈{b,a}λzi​(R)​ℋzi​(Δzi,j).0=\partial\_{t}v-\frac{\gamma}{2}\sigma^{2}q^{2}+\sum\_{z\in\mathcal{Z},i\in\{A,B\},j\in\{b,a\}}\lambda\_{z}^{i}(R)\mathcal{H}\_{z}^{i}\big(\Delta^{i,j}\_{z}\big). |  | (10) |

### 2.2 Envelope theorem and optimal controls

Define the reduced scalar Hamiltonian

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hz​(x):=supδ∈ℝpz​(δ)​(z​(δ+μz​(δ))+x).H\_{z}(x):=\sup\_{\delta\in\mathbb{R}}\;p\_{z}(\delta)\Big(z(\delta+\mu\_{z}(\delta))+x\Big). |  | (11) |

Then ℋzA​(Δ)=ℒ+Hz​(Δ−ℒ)\mathcal{H}\_{z}^{A}(\Delta)=\mathcal{L}+H\_{z}(\Delta-\mathcal{L}) and ℋzB​(Δ)=Hz​(Δ)\mathcal{H}\_{z}^{B}(\Delta)=H\_{z}(\Delta).
Assume the maximiser δ^z​(x)\hat{\delta}\_{z}(x) in ([11](#S2.E11 "In 2.2 Envelope theorem and optimal controls ‣ 2 Model ‣ Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model")) is unique and interior.
The envelope theorem yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hz′​(x)=pz​(δ^z​(x))∈(0,1),δ^z​(x)=pz−1​(Hz′​(x)).H^{\prime}\_{z}(x)=p\_{z}\big(\hat{\delta}\_{z}(x)\big)\in(0,1),\qquad\hat{\delta}\_{z}(x)=p\_{z}^{-1}\big(H^{\prime}\_{z}(x)\big). |  | (12) |

Hence optimal win probabilities and offsets can be written directly in terms of vv.

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ^zi,j​(t,q,R)=pz−1​(y^zi,j​(t,q,R)),y^zi,j​(t,q,R)=Hz′​(xzi,j​(t,q,R)),\hat{\delta}\_{z}^{i,j}(t,q,R)=p\_{z}^{-1}\big(\hat{y}\_{z}^{i,j}(t,q,R)\big),\qquad\hat{y}\_{z}^{i,j}(t,q,R)=H^{\prime}\_{z}\big(x\_{z}^{i,j}(t,q,R)\big), |  | (13) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | xzA,j​(t,q,R):=ΔzA,j​(t,q,R)−ℒ​(t,q,R),xzB,j​(t,q,R):=ΔzB,j​(t,q,R).x\_{z}^{A,j}(t,q,R):=\Delta\_{z}^{A,j}(t,q,R)-\mathcal{L}(t,q,R),\qquad x\_{z}^{B,j}(t,q,R):=\Delta\_{z}^{B,j}(t,q,R). |  | (14) |

This representation is convenient analytically and numerically: the controls are recovered from derivatives of scalar Hamiltonians, and the dependence on the non-local value function enters only through the one-dimensional arguments xzi,jx\_{z}^{i,j}.

## 3 Adiabatic quadratic approximation

When α\alpha is small, score changes are slow relative to inventory dynamics.
Following the two-scale philosophy used in our earlier last look reputation study [[5](#bib.bib5)], we separate:
(i) a fast inventory problem conditional on quasi-static RR, and (ii) a slow score dynamics driven by the induced average win probability on tier A.

### 3.1 Fast scale: small-α\alpha expansion and quadratic ansatz

For smooth vv we have, to the first order of α\alpha,

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,q,R+)≈v​(t,q,R)+α​(1−R)​vR​(t,q,R),v​(t,q,R−)≈v​(t,q,R)−α​vR​(t,q,R).v(t,q,R\_{+})\approx v(t,q,R)+\alpha(1-R)v\_{R}(t,q,R),\qquad v(t,q,R\_{-})\approx v(t,q,R)-\alpha v\_{R}(t,q,R). |  | (15) |

Therefore, tier-A continuation admits the decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | xzA,j​(t,q,R)=v​(t,q±z,R)−v​(t,q,R)+α​((1−R)​vR​(t,q±z,R)+R​vR​(t,q,R))+O​(α2),x\_{z}^{A,j}(t,q,R)=v(t,q\pm z,R)-v(t,q,R)+\alpha\big((1-R)v\_{R}(t,q\pm z,R)+Rv\_{R}(t,q,R)\big)+O(\alpha^{2}), |  | (16) |

where we can clearly distinguish the fast inventory term and the slow score term.
The O​(α)O(\alpha) term acts as an additive reward for winning, a slowly varying “prize” for reaching higher RR.
It is proportional to the marginal value vRv\_{R} and is strongest where vRv\_{R} is large,
which in turn is tied to the steepness of the routing gate G​(R)G(R).
Tight quoting can be optimal even when locally unprofitable because it increases future tier-A access through RR.
Tier B gaps are purely fast: xzB,j​(t,q,R)=v​(t,q±z,R)−v​(t,q,R)x\_{z}^{B,j}(t,q,R)=v(t,q\pm z,R)-v(t,q,R).

In the spirit of [[7](#bib.bib7)], we assume a quadratic ansatz in inventory555No linear term due to bid/ask symmetry.

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,q,R)≈−12​A​(t,R)​q2+B​(t,R),v(t,q,R)\approx-\frac{1}{2}A(t,R)\,q^{2}+B(t,R), |  | (17) |

with A​(T,R)=ηA(T,R)=\eta, B​(T,R)=0B(T,R)=0 (since terminal condition has no RR-dependent constant term.
Then, for small qq, v​(t,q±z,R)−v​(t,q,R)≈−12​A​(t,R)​z​(z±2​q)v(t,q\pm z,R)-v(t,q,R)\approx-\frac{1}{2}A(t,R)z(z\pm 2q) and vR​(t,q,R)≈BR​(t,R)v\_{R}(t,q,R)\approx B\_{R}(t,R),
so the continuation gaps become

|  |  |  |  |
| --- | --- | --- | --- |
|  | xzA,j​(t,q,R)≈−12​A​(t,R)​z​(z±2​q)+α​BR​(t,R),xzB,j​(t,q,R)≈−12​A​(t,R)​z​(z±2​q).x\_{z}^{A,j}(t,q,R)\approx-\frac{1}{2}A(t,R)z(z\pm 2q)+\alpha B\_{R}(t,R),\qquad x\_{z}^{B,j}(t,q,R)\approx-\frac{1}{2}A(t,R)z(z\pm 2q). |  | (18) |

We further expand each HzH\_{z} around x0,zi:=xzi,j​(t,0,R)x^{i}\_{0,z}:=x\_{z}^{i,j}(t,0,R):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hz​(x)≈Hz​(x0,zi)+y0,zi​(t,R)​(x−x0,zi)+12​kzi​(t,R)​(x−x0,zi)2,H\_{z}(x)\approx H\_{z}(x\_{0,z}^{i})+y\_{0,z}^{i}(t,R)\,(x-x\_{0,z}^{i})+\frac{1}{2}k\_{z}^{i}(t,R)\,(x-x\_{0,z}^{i})^{2}, |  | (19) |

where y0,zi:=Hz′​(x0,zi)y\_{0,z}^{i}:=H^{\prime}\_{z}(x\_{0,z}^{i}) and kzi:=Hz′′​(x0,zi)≥0k\_{z}^{i}:=H^{\prime\prime}\_{z}(x\_{0,z}^{i})\geq 0.
Thus, to leading order around q=0q=0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | y^zi,j​(t,q,R)≈y0,zi​(t,R)∓kzi​(t,R)​z​q​A​(t,R),i∈{A,B}.\hat{y}^{i,j}\_{z}(t,q,R)\approx y\_{0,z}^{i}(t,R)\mp k\_{z}^{i}(t,R)\,z\,q\,A(t,R),\quad i\in\{A,B\}. |  | (20) |

Offsets follow by δ=p−1​(y)\delta=p^{-1}(y).
This shows explicitly how inventory tilts bid/ask win probabilities via the familiar z​q​A​(t,R)zqA(t,R) factor, while tier A carries an additional O​(α)O(\alpha) shift through x0,zAx\_{0,z}^{A}.

### 3.2 Ergodic curvature scaling

On the fast scale, A​(t,R)A(t,R) relaxes quickly to a quasi-stationary value at fixed RR.
Matching q2q^{2} coefficients in the reduced HJB under the quadratic Hamiltonian expansion666Details follow the standard Bergault-Guéant calculations. yields a Riccati-type relation in which the stabilizing contribution comes from both tiers.
In a stationary inner approximation, one obtains the scaling

|  |  |  |  |
| --- | --- | --- | --- |
|  | A∞​(R)≈γ​σ22​ξ​(R),ξ​(R):=∑z∈𝒵,i∈{A,B}λzi​kzi​(R)​z2.A\_{\infty}(R)\approx\sqrt{\frac{\gamma\sigma^{2}}{2\xi(R)}},\qquad\xi(R):=\sum\_{z\in\mathcal{Z},i\in\{A,B\}}\lambda\_{z}^{i}\,k\_{z}^{i}(R)\,z^{2}. |  | (21) |

This expression emphasizes the intuitive point: higher flow makes inventory easier to manage (smaller curvature).777One can reproduce familiar optimal controls in the absence of score feedback by using riskless baseline Hz′​(0)=pz​(δz0)H\_{z}^{\prime}(0)=p\_{z}(\delta\_{z}^{0}).

When kzA≈kzB≈kzk\_{z}^{A}\approx k\_{z}^{B}\approx k\_{z} (a convenient closure near q=0q=0), the only strong RR-dependence in A∞A\_{\infty} is through the intensity scale ∑z,iλzi​(R)​kz​z2\sum\_{z,i}\lambda\_{z}^{i}(R)k\_{z}z^{2}.
In particular, the presence of tier B prevents the singular A∞∝1/G​(R)A\_{\infty}\propto 1/\sqrt{G(R)} behavior that arises when all flow is gated: even at G​(R)≈GminG(R)\approx G\_{\min} curvature remains bounded thanks to baseline mixing from the background tier.

### 3.3 Slow score dynamics and phase transitions

A convenient summary of the slow dynamics is through the expected drift of RR.
Let NtAN\_{t}^{A} denote the tier-A RFQ counting process (both sides) with intensity

|  |  |  |  |
| --- | --- | --- | --- |
|  | λARFQ​(R)=∑z∈𝒵,j∈{b,a}λzA​(R)=2​G​(R)​∑z∈𝒵ΛzA,\lambda\_{A}^{\rm RFQ}(R)=\sum\_{z\in\mathcal{Z},j\in\{b,a\}}\lambda\_{z}^{A}(R)=2G(R)\sum\_{z\in\mathcal{Z}}\Lambda\_{z}^{A}, |  | (22) |

and let wk∈{0,1}w\_{k}\in\{0,1\} be the win indicator on the kk-th tier-A RFQ.
The EMA recursion in event time is Rk+1=(1−α)​Rk+α​wk⟹Δ​Rk=α​(wk−Rk)R\_{k+1}=(1-\alpha)R\_{k}+\alpha w\_{k}\Longrightarrow\Delta R\_{k}=\alpha(w\_{k}-R\_{k}).
Passing to continuous time and taking conditional expectation leads to the drift approximation

|  |  |  |  |
| --- | --- | --- | --- |
|  | R˙≈α​λARFQ​(R)​(y¯A​(R)−R),\dot{R}\approx\alpha\,\lambda\_{A}^{\rm RFQ}(R)\,\big(\bar{y}\_{A}(R)-R\big), |  | (23) |

where y¯A​(R)\bar{y}\_{A}(R) is the tier-A intensity-weighted win probability near fast equilibrium (q≈0q\approx 0):

|  |  |  |  |
| --- | --- | --- | --- |
|  | y¯A​(R):=∑z∈𝒵ΛzA​y0,zA​(R)∑z∈𝒵ΛzA=∑z∈𝒵ΛzA​pz​(δ^zA​(0,R))∑z∈𝒵ΛzA.\bar{y}\_{A}(R):=\frac{\sum\_{z\in\mathcal{Z}}\Lambda\_{z}^{A}\,y\_{0,z}^{A}(R)}{\sum\_{z\in\mathcal{Z}}\Lambda\_{z}^{A}}=\frac{\sum\_{z\in\mathcal{Z}}\Lambda\_{z}^{A}\,p\_{z}\big(\hat{\delta}\_{z}^{A}(0,R)\big)}{\sum\_{z\in\mathcal{Z}}\Lambda\_{z}^{A}}. |  | (24) |

Equilibria satisfy y¯A​(R)=R\bar{y}\_{A}(R)=R, and stability is determined by y¯A′​(R)−1\bar{y}^{\prime}\_{A}(R)-1.
A phase transition corresponds to the emergence of three fixed points (two stable separated by one unstable), producing bistability and hysteresis.
The background tier affects this picture indirectly through the fast-scale coefficients A∞​(R)A\_{\infty}(R) and hence y0,zA​(R)y\_{0,z}^{A}(R), while the score dynamics itself is driven only by tier A.

### 3.4 Logistic promotion gate and minimal phase-portrait closure

Assume a logistic gate, capturing shortlisting:

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(R)=Gmin+Δ​G​u,u:=(1+e−β​(R−R0))−1,G(R)=G\_{\textrm{min}}+\Delta G\,u,\qquad u:=\left(1+e^{-\beta(R-R\_{0})}\right)^{-1}, |  | (25) |

with steepness β\beta, midpoint R0R\_{0} and Δ​G=Gmax−Gmin\Delta G=G\_{\max}-G\_{\min}.
Then G′​(R)=β​Δ​G​u​(1−u)G^{\prime}(R)=\beta\Delta G\,u(1-u) and

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(u)=R0+1β​log⁡u1−u.R(u)=R\_{0}+\frac{1}{\beta}\log\frac{u}{1-u}. |  | (26) |

To obtain a compact scalar phase portrait, one may postulate a reduced-form closure for y¯A​(R)\bar{y}\_{A}(R):

|  |  |  |  |
| --- | --- | --- | --- |
|  | y¯A​(R)≈y¯⋆+𝒜​(1ξ​(R0)−1ξ​(R))+α​ℬ​G′​(R),\bar{y}\_{A}(R)\approx\bar{y}\_{\star}+\mathcal{A}\Big(\frac{1}{\sqrt{\xi(R\_{0})}}-\frac{1}{\sqrt{\xi(R)}}\Big)+\alpha\mathcal{B}\,G^{\prime}(R), |  | (27) |

where y¯⋆:=∑zΛzA​Hz′​(0)/∑zΛzA\bar{y}\_{\star}:=\sum\_{z}\Lambda\_{z}^{A}H^{\prime}\_{z}(0)/\sum\_{z}\Lambda\_{z}^{A} is the baseline “riskless” win rate, the second term encodes the Riccati scaling A∞​(R)∝1/ξ​(R)A\_{\infty}(R)\propto 1/\sqrt{\xi(R)}, and the last term captures the slow “promotion wedge” driven by vRv\_{R} and concentrated where the gate is steep.
Constants 𝒜,ℬ>0\mathcal{A},\mathcal{B}>0 encode microstructure features (the local curvature pzp\_{z}, slippage, and ladder composition) and can be estimated from the quadratic expansion.

Define F​(R):=y¯A​(R)−RF(R):=\bar{y}\_{A}(R)-R.
To make the fold structure explicit under a logistic gate, it is convenient to parametrize RR via u∈(0,1)u\in(0,1).
Assume for simplicity that the microstructure curvatures are frozen near the fast equilibrium, kzA≈kzB≈kzk\_{z}^{A}\approx k\_{z}^{B}\approx k\_{z}, and define ξi:=∑zΛzi​kz​z2\xi\_{i}:=\sum\_{z}\Lambda\_{z}^{i}k\_{z}z^{2}.
Then ξ​(R)=ξ​(u)=ξB+(Gmin+Δ​G​u)​ξA\xi(R)=\xi(u)=\xi\_{B}+(G\_{\min}+\Delta G\,u)\xi\_{A} and ([27](#S3.E27 "In 3.4 Logistic promotion gate and minimal phase-portrait closure ‣ 3 Adiabatic quadratic approximation ‣ Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model")) yields a scalar fixed-point equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(u)=y¯⋆+𝒜​(1ξ0−1ξB+(Gmin+Δ​G​u)​ξA)+α​ℬ​Δ​G​β​u​(1−u)−(R0+1β​log⁡u1−u)=0,F(u)=\bar{y}\_{\star}+\mathcal{A}\Big(\frac{1}{\sqrt{\xi\_{0}}}-\frac{1}{\sqrt{\xi\_{B}+(G\_{\min}+\Delta G\,u)\xi\_{A}}}\Big)+\alpha\mathcal{B}\,\Delta G\,\beta\,u(1-u)-\Big(R\_{0}+\frac{1}{\beta}\log\frac{u}{1-u}\Big)=0, |  | (28) |

where ξ0=ξ​(R0)\xi\_{0}=\xi(R\_{0}).
Fold points (hysteresis boundaries) satisfy in addition

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Fd​u=𝒜​Δ​G​ξA2​(ξB+(Gmin+Δ​G​u)​ξA)−3/2+α​ℬ​Δ​G​β​(1−2​u)−1β​(1u+11−u).\frac{\,\mathrm{d}F}{\,\mathrm{d}u}=\mathcal{A}\,\frac{\Delta G\xi\_{A}}{2}\,\big(\xi\_{B}+(G\_{\min}+\Delta Gu)\xi\_{A}\big)^{-3/2}+\alpha\mathcal{B}\,\Delta G\,\beta\,(1-2u)-\frac{1}{\beta}\Big(\frac{1}{u}+\frac{1}{1-u}\Big). |  | (29) |

At least one fixed point is guaranteed since y¯A​(R)∈(0,1)\bar{y}\_{A}(R)\in(0,1) implies F​(0)>0F(0)>0 and F​(1)<0F(1)<0.
For sufficiently steep gates, the only region where FF can overcome the linear −R-R term is near R0R\_{0}, where G′​(R)G^{\prime}(R) is maximal.
For sufficiently strong score feedback (large α\alpha and/or steep β\beta), the bell-shaped campaign term can generate two additional fixed points through a fold bifurcation, producing a hysteresis loop.
In this two-tier setting, the “permanent” low-score fixed point typically lies near the low-gate regime G​(R)≈GminG(R)\approx G\_{\min} but remains quantitatively influenced by the baseline curvature ξ​(R)\xi(R) contributed by the background tier.

## 4 Numerical examples.

As an illustration, consider a standard size-ladder of z=(1,2,5,10)z=(1,2,5,10) M notional with baseline RFQ intensities
ΛzB=(1000,800,600,400)\Lambda\_{z}^{B}=(1000,800,600,400) day-1 for the background tier and Λ¯zA=(0,0,0,50)\bar{\Lambda}\_{z}^{A}=(0,0,0,50) day-1 for the gated aggregator tier.
Individual clients often tend to have a narrow size distribution, and this is exactly the case we are capturing here.
Win probability is taken to be of a standard sigmoid shape,

|  |  |  |  |
| --- | --- | --- | --- |
|  | pz​(δ)=(1+eκz​(δ−δ¯z))−1,p\_{z}(\delta)=\left(1+e^{\kappa\_{z}(\delta-\bar{\delta}\_{z})}\right)^{-1}, |  | (30) |

with κz=(5.0,4.5,4.0,3.5)\kappa\_{z}=(5.0,4.5,4.0,3.5) bp-1 and δ¯z=(0.3,0.4,0.5,0.6)\bar{\delta}\_{z}=(0.3,0.4,0.5,0.6) for both tiers.
Here bp stands for basis points.888This implies GBM while we deal here with simple Brownian motion.
The difference is negligible in FX market making due to short trading horizons.
A constant latency slippage of θz=0.2\theta\_{z}=0.2 bp is assumed across all sizes and tiers.
We also assume a daily volatility of 100100 bp and a risk aversion coefficient of γ=10−3\gamma=10^{-3} bp-1 M-1.
This set of parameters corresponds to a daily turnover of ≈2\approx 2 billion notional and a top-of-book spread of ≈1\approx 1 bp.
The default gate parameters are Gmin=0.2G\_{\min}=0.2, R0=0.6R\_{0}=0.6, β=40\beta=40 and the EMA memory parameter is α=0.01\alpha=0.01, unless specified otherwise.

![Refer to caption](2603.10569v1/x1.png)


Figure 1: 
Heatmap of the stationary value function v​(0,q,R)v(0,q,R) for a default parameter set defined in the text.
Horizontal dotted line corresponds to R0R\_{0}.

Numerical solution of the HJB equation can be challenging, because on one hand, the time step d​tdt has to be sufficiently small for the Euler backward step to be valid,
while on the other hand, the time horizon TT has to be sufficiently long to cover score relaxation, leading to a large number of steps and increased precision requirements.
For α=0.01\alpha=0.01, EMA half-life is log⁡(0.5)/log⁡(1−α)≈70\log(0.5)/\log(1-\alpha)\approx 70 trades, so at the minimum gate value of 0.2 this is equivalent to ≈3.5\approx 3.5 days for tier A,
while the timestep has to be well below 1/∑zΛz≈301/\sum\_{z}\Lambda\_{z}\approx 30 s, which brings the number of steps to ≳106\gtrsim 10^{6}.
We can take advantage of timescale separation and choose 𝒯\mathcal{T} long enough to cater for the inventory risk relaxation alone.
Then on time interval [0,𝒯][0,\mathcal{T}] we solve HJB with terminal condition v​(𝒯,q,R)=−12​η​q2+e−ρ​𝒯​Φ​(R)v(\mathcal{T},q,R)=-\frac{1}{2}\eta q^{2}+e^{-\rho\mathcal{T}}\Phi(R), where ρ\rho is the discount rate and Φ​(R)\Phi(R) is the continuation term that propagates the slow score incentives across intervals.
Stationarity across 𝒯\mathcal{T}-intervals implies Φ​(R)=v​(0,0,R)\Phi(R)=v(0,0,R).
So Φ\Phi is determined by a fixed point: the terminal condition depends on Φ\Phi and the start-of-interval value regenerates Φ\Phi.
This approach is similar in spirit to stationary HJB, and also mimics business cycle.
Technically, we start with Φ(0)​(R)=0\Phi^{(0)}(R)=0, then for each nn solve interval HJB with terminal condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | v(n)​(𝒯,q,R)=−12​η​q2+e−ρ​𝒯​Φ(n)​(R)v^{(n)}(\mathcal{T},q,R)=-\frac{1}{2}\eta q^{2}+e^{-\rho\mathcal{T}}\Phi^{(n)}(R) |  | (31) |

and update

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ(n+1)​(R)=(1−ζ)​Φ(n)​(R)+ζ​v(n)​(0,0,R)\Phi^{(n+1)}(R)=(1-\zeta)\Phi^{(n)}(R)+\zeta v^{(n)}(0,0,R) |  | (32) |

until the absolute increment is sufficiently small.
Here ζ\zeta introduces optional damping.
This way we constrain PDE horizon to a managable number of steps but at the same time capture multi-day score incentives.
Practically, to reduce the number of iterations we also apply Anderson acceleration [[25](#bib.bib25)], which uses the last mm iterates to build a better next iterate by choosing a linear combination that minimizes the residual with ridge regression.
Numerical calculations in this paper are based on the block interval of 𝒯=0.05\mathcal{T}=0.05 days with 10410^{4} time steps (d​t≈0.5dt\approx 0.5 s).

![Refer to caption](2603.10569v1/x2.png)


Figure 2: 
Tier A optimal quote offset δ^zA\hat{\delta}\_{z}^{A} for z=10z=10 at zero inventory as a function of score RR for α=0.01\alpha=0.01 (feedback) and α=0\alpha=0 (no feedback).
Other parameters are defined in the text.
Due to bid/ask parameter symmetry, side index is omitted.
Vertical dotted line corresponds to R0R\_{0}.

![Refer to caption](2603.10569v1/x3.png)


Figure 3: 
Tier A optimal quote offset δ^zA\hat{\delta}\_{z}^{A} for z=10z=10 as a function of inventory qq for several values of score RR.
Parameters are defined in the text.
Due to bid/ask parameter symmetry, side index is omitted.

Figure [1](#S4.F1 "Figure 1 ‣ 4 Numerical examples. ‣ Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model") illustrates the heatmap of the stationary value function v​(0,q,R)v(0,q,R).
Gradients related to the inventory and score management are clearly visible.
Figure [2](#S4.F2 "Figure 2 ‣ 4 Numerical examples. ‣ Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model") demonstrates a dip in quote offset for tier A at zero inventory in the vicinity of R0R\_{0} – the signature of campaigning.
Above R0R\_{0}, the dealer would like to “harvest” and widens spread, but clearly not fully back to the level without feedback (α=0\alpha=0).
Widening too much immediately lowers the win rate y¯A​(R)\bar{y}\_{A}(R), and when y¯A​(R)<R\bar{y}\_{A}(R)<R, score decay is accelerated.
If the gate is steep, the downside of decaying across the gate is large, so the optimal policy can remain defensive even at high RR.
In other words, high score is not a riskless asset and maintenance costs.

Figure [3](#S4.F3 "Figure 3 ‣ 4 Numerical examples. ‣ Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model") shows the dependence of the quote offset for tier A as a function of inventory qq for several levels of score RR.
Campaigning around R0R\_{0} is clear across inventories.
Note that for R=0.3R=0.3, gated offset matches not just the myopic value without feedback (α=0\alpha=0) but also the offset for the background tier B, same size z=10z=10.
This is because we have selected the same parameters for the win probability pz​(δ)p\_{z}(\delta) for both tiers.

![Refer to caption](2603.10569v1/x4.png)


Figure 4: 
Logistic gate G​(R)G(R) (dashed line) and instant PnL of the gated tier at zero inventory ΠA​(0,R)\Pi\_{A}(0,R) (solid line) as functions of score RR.
Parameters are defined in the text.
Vertical dotted line corresponds to R0R\_{0}.

![Refer to caption](2603.10569v1/x5.png)


Figure 5: 
Instant PnL of the gated tier at zero inventory ΠA​(0,R)\Pi\_{A}(0,R) as a function of score drift R˙\dot{R} color coded by the value of RR.
Parameters are defined in the text.
Larger circle on the curve corresponds to R0R\_{0}.
Horizontal dotted line corresponds to ΠA​(0,0)\Pi\_{A}(0,0).

The signature of campaigning and harvesting becomes even more dramatic in instantaneous PnL, which can be defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΠA​(q,R)=2​G​(R)​∑zΛzA​pz​(δ^zA)​z​(δ^zA−θz)\Pi\_{A}(q,R)=2G(R)\sum\_{z}\Lambda\_{z}^{A}p\_{z}(\hat{\delta}\_{z}^{A})z(\hat{\delta}\_{z}^{A}-\theta\_{z}) |  | (33) |

for the gated tier, where we have dropped side dependence due to symmetry and summed up to get the factor of 2.
Here ΠA​(q,R)\Pi\_{A}(q,R) should be interpreted as the instantaneous edge-capture rate (per unit time) from tier A only, conditional on the state (q,R)(q,R) and evaluated at the optimal tier-A offsets; it excludes the running inventory penalty term and any contribution from tier B.
Figure [4](#S4.F4 "Figure 4 ‣ 4 Numerical examples. ‣ Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model") illustrates the dependence of the instantaneous PnL on the score along with the shape of the gate for comparison.
During campaigning right below R0R\_{0}, PnL drops, but then rises sharply to enjoy harvesting.
The dependence of PnL on score drift R˙\dot{R} is also very representative, as shown in Figure [5](#S4.F5 "Figure 5 ‣ 4 Numerical examples. ‣ Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model").
Campaign is characterized by positive R˙\dot{R} and low PnL while harvesting corresponds to negative R˙\dot{R} and high PnL.

![Refer to caption](2603.10569v1/x6.png)


Figure 6: 
Score phase portrait for α=0.01\alpha=0.01 (feedback) and α=0\alpha=0 (no feedback).
Other parameters are defined in the text.
Vertical dotted line corresponds to R0R\_{0}.

Phase portrait of the score can exhibit a very interesting behavior typical of a critical system, as demonstrated in Figure [6](#S4.F6 "Figure 6 ‣ 4 Numerical examples. ‣ Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model").
While the myopic model with α=0\alpha=0 exhibits a single fixed point, the score feedback can give rise to bistable behavior with three fixed points and two basins of attraction.
Figure [7](#S4.F7 "Figure 7 ‣ 4 Numerical examples. ‣ Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model") illustrates the mean-field relaxation trajectories (obtained by numerically solving the slow score ODE ([23](#S3.E23 "In 3.3 Slow score dynamics and phase transitions ‣ 3 Adiabatic quadratic approximation ‣ Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model")) with optimal controls) for different initial conditions.
Below the lower fold, campaigning is not worth it (the gate is too far, the prize is too small).
Inside the bistable region, a sufficiently aggressive campaign can push RR across the unstable fixed point into the promoted basin.
Above the upper fold, harvesting becomes optimal because the dealer remains promoted even with wider quotes.

![Refer to caption](2603.10569v1/x7.png)


Figure 7: 
Slow score relaxation for different initial conditions demonstrating two stable basins.
Parameters are defined in the text.

![Refer to caption](2603.10569v1/x8.png)


Figure 8: 
Bifurcation diagram showing the loci of the fixed points as functions of the inverse gate steepness (log scale).
Parameters are defined in the text.
The level corresponding to the stable point without score feedback (α=0\alpha=0) is also shown for reference (dotted line).

The loci of the fixed points depend on the gate contrast and smoothness.
As shown in Figure [8](#S4.F8 "Figure 8 ‣ 4 Numerical examples. ‣ Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model"), bistability is observed for sharp gates (large β\beta).
As β\beta decreases, a stable + unstable pair annihilates leaving one stable branch, which further gradually evolves to the myopic limit.

## 5 Concluding remarks

This paper introduces a minimal two-tier stochastic control model for aggregator-routed RFQ markets in which a dealer’s long-run win score feeds back into future RFQ opportunity intensity through a promotion gate.
The model separates the “micro” RFQ interaction – size-ladder quoting with adverse selection and inventory risk – from a “macro” routing layer in which the dealer is short-listed with a probability that depends on a slowly varying score.
By treating this score as an explicit state variable, the framework captures a practical feature of FX aggregator workflows: quote aggressiveness affects not only immediate edge capture but also future access to the most valuable stream of opportunities.

On the control side, we derived a reduced HJB in a Bergault-Guéant operator form with an explicit win/lose branching structure for tier A, and standard non-local jump operators for the background tier.
An envelope-theorem argument yields a convenient representation of optimal controls: optimal win probabilities are given by derivatives of a one-dimensional reduced Hamiltonian, and optimal offsets follow by inversion of the win-probability curve.
This view helps interpret the policy in economic terms and provides a numerically robust route to recovering optimal quotes in multi-size RFQ ladders.

A key qualitative implication arises in the long-memory regime of the score (small EMA parameter).
In this limit, inventory control is fast and the score evolves on a slow manifold driven by the induced equilibrium win rate.
Combining a quadratic inventory ansatz with a local quadratic expansion of the RFQ Hamiltonians yields a tractable adiabatic closure: inventory curvature relaxes rapidly to a quasi-stationary level that depends on the total (tier A + tier B) liquidity available for inventory rebalancing, while the score dynamics reduce to a one-dimensional drift field.
Under a steep logistic promotion gate, this drift can undergo a fold bifurcation, generating bistability and hysteresis.
Economically, the optimal policy can alternate between “campaigning” (temporarily tighter quoting to move the score into a promoted basin) and “harvesting” (wider quoting while accepting gradual score decay), a pattern that is visible both in optimal offsets and in the instantaneous edge capture rate.

The two-tier structure plays an important stabilizing role.
Even when the promotion gate is near its minimum, the background stream maintains a baseline of inventory-mixing opportunities, preventing pathological blow-ups in the effective inventory curvature that can occur if all flow is gated by the score.
This feature is practically relevant: in real dealer franchises, not all client flow is routed through ranking-based shortlists, yet inventory risk is borne at the consolidated-book level.
The model highlights how “residual” flow can indirectly shape optimal behavior on the ranked stream by affecting the cost of inventory imbalances.

Several extensions are natural.
First, the gate G​(R)G(R) can be endogenized further by linking it to explicit top-list + exploration rules (finite-NN shortlisting) and to cross-sectional competition, moving beyond the reduced-form mean-field representation.
Second, the adverse selection component can be enriched to include post-trade informational drift or jump risk [[4](#bib.bib4)], allowing one to study how informational asymmetry interacts with promotion incentives.
Third, the score itself could be multi-dimensional (wins, response times, hold times, reject rates) with potentially different platform weights.
Finally, from an empirical standpoint, the framework suggests a calibration program: estimate size-conditional win curves pz​(⋅)p\_{z}(\cdot), gate shapes G​(⋅)G(\cdot) and score memory parameters from RFQ logs, then test whether the predicted regions of campaigning/harvesting and the implied hysteresis align with observed regime switches in dealer quoting and flow.

## Acknowledgment

The author is grateful to Eric Mathew John (HSBC) for fruitful discussions and to Richard Anthony (HSBC) for support throughout the project and valuable comments.
The views expressed are those of the author and do not necessarily reflect the views or practices at HSBC.

## References

* [1]

  H. Assayag, A. Barzykin, R. Cont, and W. Xiong.
  Competition and learning in dealer markets.
  *SSRN working paper* 4838181, 2024.
* [2]

  M. Avellaneda and S. Stoikov.
  High-frequency trading in a limit order book.
  *Quant. Finance*, 8(3):217–224, 2008.
* [3]

  A. Barzykin, P. Bergault, and O. Guéant.
  Algorithmic market making in dealer markets with hedging and market impact.
  *Math. Finance*, 33(1):41–79, 2023.
* [4]

  A. Barzykin, P. Bergault, O. Guéant, and M. Lemmel.
  Optimal Quoting under Adverse Selection and Price Reading.
  *arXiv preprint* arXiv:2508.20225v3, 2025.
* [5]

  A. Barzykin.
  Dynamic slippage control and rejection feedback in spot FX market making.
  empharXiv preprint arXiv:2603.07752, 2026.
* [6]

  P. Bergault and O. Guéant.
  Size matters for OTC market makers: general results and dimensionality reduction techniques.
  *Math. Finance*, 31(1):279–322, 2021.
* [7]

  P. Bergault, D. Evangelista, O. Guéant, and D. Vieira.
  Closed-form approximations in multi-asset market making.
  *Appl. Math. Finance*, 28:101–142, 2021.
* [8]

  R. Boyce, M. Herdegen, and L. Sánchez-Betancourt.
  Market making with exogenous competition.
  *arXiv preprint* arXiv:2407.17393, 2024.
* [9]

  M. Butz and R. Oomen.
  Internalisation by electronic FX spot dealers.
  *Quant. Finance*, 19(1):35–56 2019.
* [10]

  Á Cartea, S. Jaimungal, and J. Ricci,
  Buy low, sell high: A high frequency trading perspective.
  *SIAM J. Financ. Math.*, 5:415–444, 2014.
* [11]

  Á. Cartea, S. Jaimungal, and J. Walton.
  Foreign exchange markets with last look.
  *Math. Financ. Econ.*, 13:1–30, 2019.
* [12]

  Á. Cartea, P. Chang, M. Mroczka, and R. Oomen.
  AI-driven liquidity provision in OTC financial markets.
  *Quant. Finance*, 22(12):2171–2204, 2022.
* [13]

  Á. Cartea, P. Chang, and J. Penalva.
  Algorithms and supracompetitive prices in electronic markets: the impact of tick size.
  *SSRN working paper* 4105954, 2022.
* [14]

  Á. Cartea, S. Jaimungal, and L. Sánchez-Betancourt.
  Nash equilibrium between brokers and traders.
  *arXiv preprint* arXiv:2407.10561, 2024.
* [15]

  N. Chilenje, M. Daba, D. Feleppa, C. Fellner, and L. Sánchez-Betancourt.
  Market making with competition: a Stackelberg equilibrium.
  *SSRN working paper* 5505480, 2025.
* [16]

  R. Cont and W. Xiong.
  A study of algorithmic collusion in multi-dealer-to-client platforms.
  *SSRN working paper* 5463594, 2024.
* [17]

  R. F. Donnelly and Z. Li.
  Liquidity competition between brokers and an informed trader.
  *SSRN working paper* 5174063, 2025 (also arXiv:2503.08287).
* [18]

  Z. Eisler and J. Muhle-Karbe.
  Optimizing broker performance evaluation through intraday modeling of execution cost.
  *arXiv preprint* arXiv:2405.18936, 2024.
* [19]

  J.-D. Fermanian, O. Guéant, and J. Pu.
  The behavior of dealers and clients on the European corporate bond market: the case of multi-dealer-to-client platforms.
  *Mark. Microstructure Liq.* 2(3):1750004, 2016.
* [20]

  O. Guéant, C.-A. Lehalle, and J. Fernández-Tapia.
  Dealing with the inventory risk: a solution to the market making problem.
  *Math. Financ. Econ.*, 7:477–507, 2013.
* [21]

  T. Ho and H. Stoll.
  Optimal dealer pricing under transactions and return uncertainty.
  *J. Financ. Econ.*, 9(1):47–73, 1981.
* [22]

  P. Marín, S. Ardanza-Trevijano, and J. Sabio.
  Causal Interventions in Bond Multi-Dealer-to-Client Platforms.
  *arXiv preprint* arXiv:2506.18147v2, 2025.
* [23]

  R. Oomen.
  Execution in an aggregator.
   *Quant. Finance*, 17(3):383–404, 2017.
* [24]

  R. Oomen.
  Last look.
  *Quant. Finance*, 17(7):1057–1070, 2017.
* [25]

  H. F. Walker and P. Ni.
  Anderson acceleration for fixed-point iterations.
  *SIAM J. Numer. Anal.*, 49(4): 1715–1735, 2011.

BETA