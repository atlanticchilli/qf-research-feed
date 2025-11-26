---
authors:
- Levon Mahseredjian
doc_id: arxiv:2511.18117v1
family_id: arxiv:2511.18117
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Diffusive Limit of Hawkes Driven Order Book Dynamics With Liquidity Migration
url_abs: http://arxiv.org/abs/2511.18117v1
url_html: https://arxiv.org/html/2511.18117v1
venue: arXiv q-fin
version: 1
year: 2025
---


Levon Sarkis Mahseredjian

(October 2025)

###### Abstract

This paper develops a theoretical mesoscopic model of the limit order book driven by multivariate Hawkes processes, designed to capture temporal self-excitation and the spatial propagation of order flow across price levels. In contrast to classical zero-intelligence or Poisson based queueing models, the proposed framework introduces mathematically defined migration events between neighbouring price levels, whose intensities are themselves governed by the underlying Hawkes structure. This provides a principled stochastic mechanism for modeling interactions between order arrivals, cancellations, and liquidity movement across adjacent queues.

Starting from a microscopic specification of Hawkes driven order flow, we derive a diffusion approximation which yields a reflected mesoscopic stochastic differential equation (SDE) system for queue volumes. The limiting generator is obtained through a Taylor expansion of the microscopic generator, demonstrating how temporal excitation together with spatial migration determine the drift and diffusion structure of the limit order book in the mesoscopic regime. The resulting model extends existing diffusion limits by incorporating correlated excitations and price level to price level liquidity movement within a unified Hawkes based formulation.

By establishing this diffusive limit, the paper provides a mathematically consistent bridge between high frequency event based models and macroscopic stochastic descriptions of market microstructure. The work is entirely theoretical and lays a foundation for future analytical and numerical developments without relying on empirical calibration.

Keywords: Limit Order Book, Hawkes Processes, Functional Central Limit Theorem, Market Microstructure, Stochastic Modelling.

## 1 Introduction

The limit order book (LOB) is a discrete queuing system that records all outstanding buy and sell orders awaiting execution. Each order specifies both a price and a quantity, and transactions occur when compatible buy and sell orders meet. The limit order book thus provides a detailed and dynamic representation of market liquidity.

#### 

In this work, we focus on the first-in, first-out (FIFO) queuing rule, which prioritises orders by their time of submission. Although alternative, more complicated, mechanisms such as Pro-Rata exist, the FIFO structure remains the standard in most modern electronic exchanges. Modelling the LOB is a central problem in computational finance, as it enables the study of market microstructure, price formation, and execution dynamics. A significant class of limit order book models emerges from the perfect-rationality approach, in which market participants are assumed to behave strategically and optimise their order placement decisions. These models treat order submission, cancellation, and execution as the outcome of agents maximising expected utility under market frictions and informational constraints. This framework, pioneered in the economics literature, provides a microstructure consistent explanation for observed order book shapes and trading behaviours. A comprehensive survey of these models is provided by Parlour and Seppi [2]. Institutions such as hedge funds and market making firms regularly use such models to design and test algorithmic trading strategies. In contrast, the zero-intelligence approach models the limit order book as a purely stochastic system, where order arrivals, cancellations, and executions are treated as exogenous random events rather than the outcome of strategic optimisation. This framework replaces behavioural assumptions with mathematically tractable probabilistic structures, often using Poisson processes or Markovian queueing dynamics to describe the evolution of liquidity across price levels. We adopt a zero-intelligence modelling framework, where order flow is represented as a sequence of random events rather than as the outcome of perfectly rational agent decisions. This approach is utilised in this paper and allows for analytical tractability while still reproducing key empirical regularities observed in high frequency market data.

### 1.1 Limit Order Book

A limit order book operates as a double auction mechanism in which buy and sell orders are matched based on price and time via a matching algorithm. The bid side aggregates all buy limit orders, arranged in descending order of price, while the ask side aggregates all sell limit orders, arranged in ascending order of price. The highest bid and the lowest ask define the best bid and best ask prices, respectively, and their difference is known as the bid ask spread which is what market makers and other market participants seek to profit from.

New orders arriving to the book may either: add liquidity (limit orders) by joining the queue at a given price level;
remove liquidity (market orders) by executing immediately against standing orders; or
cancel existing liquidity(cancellations), thereby modifying the depth at a price level.

The stochastic evolution of these order types governs both price movements and liquidity fluctuations. Consequently, realistic LOB models must capture the statistical dependencies between such events. This motivates the use of Hawkes processes, as a more effective point process for modeling the self-exciting and mutually-exciting nature of high frequency order flow which has been shown empirically is many such papers, for instance in [3]. Another important feature of the limit order book is the tick size. A *tick* is the minimum allowable price increment in the order book. The bid ask spread is always an
integer number of ticks.

### 1.2 Literature Review

The modeling of limit order book dynamics has undergone a substantial evolution over the past two decades. Early stochastic models such as those developed by Cont and de Larrard [4] established that simple queueing mechanisms with Poisson order flow can reproduce several stylised empirical features of electronic markets, including average depth profiles and the distribution of times to price changes. These models offered analytical tractability and clear structural interpretation, but the assumption of independent Poisson arrivals limited their capacity to represent the pronounced temporal clustering observed in high frequency markets.

#### 

A major advancement came from the introduction of multivariate Hawkes processes. The empirical work of Bacry, Muzy and collaborators [5] demonstrated that order submissions, cancellations and market orders exhibit strong self-excitation and cross-excitation, revealing that modern markets are highly endogenous systems in which activity propagates across event types and between buy and sell sides. This insight motivated a new generation of microscopic order book models in which each event type is governed by a Hawkes intensity.
The question of how such microscopic Hawkes driven systems behave under scaling limits has been addressed in several recent studies. The work of Horst and Paul [6] considered a high frequency limit in which queue sizes are rescaled diffusively. They showed that a Hawkes driven birth death mechanism at each price level converges to a reflected diffusion whose drift and volatility depend explicitly on the underlying Hawkes kernels. Their framework provides a rigorous bridge between self-exciting microscopic order flow and mesoscopic stochastic differential equations. Hambly and Ledger [7] pursued a complementary perspective by studying the behaviour of the order book when the number of price levels grows and the tick size tends to zero. Their analysis led to reflected stochastic partial differential equations describing the evolution of the order book as a continuum in price space. Together, these works reveal the usefulness of scaling limits in connecting high frequency market microstructure with more tractable diffusion style models.

#### 

Additional insight into Hawkes modulated order flow is provided by the doctoral work of Chen [8], who investigated the interaction between excitation in order flow and short term price predictability. Chen’s analysis highlighted the role of cross-excitation between order types and the relationship between local imbalance and subsequent price movements. This empirical and modelling evidence further strengthens the argument that excitation must be incorporated directly into realistic models of queue dynamics.

Earlier theoretical work, such as that of Abergel et al [9], studied the propagation of liquidity and the relationship between order flow events and price formation from a more structural perspective. Although these models were not constructed around Hawkes processes, they emphasised the need for a mechanistic understanding of how order book events at one level influence neighbouring levels and eventually drive observable price changes.

The present work builds on and extends these strands of literature. In contrast to existing mesoscopic Hawkes driven models, which primarily treat each queue level as an isolated birth death process, I incorporate a microscopic mechanism for liquidity migration between neighbouring price levels. This migration is governed by Hawkes modulated intensities and, under diffusive scaling, produces a discrete Laplacian term in the limiting generator. The resulting mesoscopic dynamics therefore combine temporal self-excitation with a diffusion like spatial coupling between queue levels, reflecting the empirically observed spread of liquidity across adjacent depths. Furthermore, by deriving the limiting generator explicitly and connecting the diffusion covariance matrix to the Hawkes branching structure through a functional central limit theorem, my model retains a direct and interpretable link between microscopic excitation and macroscopic variability. Existing models either omit spatial liquidity propagation or introduce it in an ad hoc manner, whereas in my framework it arises naturally from the underlying Hawkes structure.

By integrating endogenous Hawkes excitation with liquidity migration and by establishing a rigorous diffusive limit that yields a reflected multi-dimensional SDE with Laplacian coupling, this work advances the literature toward a more complete and empirically faithful description of limit order book dynamics. It offers a mesoscopic model that remains grounded in microscopic market mechanics while providing a tractable analytical structure suitable for theoretical analysis, simulation and empirical calibration.

## 2 Hawkes Driven Order Flow

In this section, we introduce the Hawkes process, a stochastic framework designed to capture the self-exciting and mutually-exciting dynamics of event arrivals in high frequency financial markets.

Through this formulation, Hawkes processes provide a flexible framework to represent key stylised facts of limit order book dynamics. They naturally capture self-excitation, whereby a surge in buy (or sell) orders raises the short-term probability of additional activity of the same type; cross-excitation, where actions on one side of the book influence behaviour on the opposite side (for instance, a sell side cancellation may encourage more buy side limit orders); and temporal decay, reflecting the gradual fading of such effects over a characteristic timescale.

These mechanisms collectively explain a range of empirical phenomena observed in high frequency data, including volatility clustering, order flow imbalance persistence, and long range dependence in event arrivals. Consequently, Hawkes processes serve as a natural and tractable foundation for modeling order flow in both microscopic and mesoscopic representations of the limit order book.

### 2.1 Point Processes and Conditional Intensity

The definitions in this section follow standard Hawkes process theory, I refer readers to [4] [5] if they seek more detail.

A point process on ℝ+\mathbb{R}\_{+} is a sequence of random event times (Tk)k∈ℕ(T\_{k})\_{k\in\mathbb{N}} such that 0<T1<T2<…0<T\_{1}<T\_{2}<\dots. The associated counting process is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​(t)=∑k≥1𝟏{Tk≤t},t≥0,N(t)=\sum\_{k\geq 1}\mathbf{1}\_{\{T\_{k}\leq t\}},\quad t\geq 0, |  | (1) |

which counts the number of events up to time tt.
The conditional intensity function λ​(t)\lambda(t) characterizes the instantaneous event rate given the past filtration ℱt\mathcal{F}\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​(t):=limΔ→0𝔼​[N​(t+Δ)−N​(t)∣ℱt]Δ.\lambda(t):=\lim\_{\Delta\to 0}\frac{\mathbb{E}[N(t+\Delta)-N(t)\mid\mathcal{F}\_{t}]}{\Delta}. |  | (2) |

This quantity determines the expected rate of arrivals at time tt conditional on all prior events.
A univariate Hawkes process is a point process N​(t)N(t) whose intensity depends linearly on its own history:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​(t)=μ+∫0tϕ​(t−s)​𝑑N​(s),\lambda(t)=\mu+\int\_{0}^{t}\phi(t-s)\,dN(s), |  | (3) |

where μ>0\mu>0 is the baseline intensity, and ϕ:ℝ+→ℝ+\phi:\mathbb{R}\_{+}\to\mathbb{R}\_{+} is the kernel function describing how past events excite future ones.
Intuitively, each arrival increases the conditional intensity for a period of time determined by the kernel ϕ\phi. A common choice is the exponential kernel,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(t)=α​e−β​t,α,β>0,\phi(t)=\alpha e^{-\beta t},\quad\alpha,\beta>0, |  | (4) |

which implies that excitation decays exponentially with rate β\beta. The parameters α\alpha and β\beta respectively control the magnitude and persistence of self-excitation.

### 2.2 Multivariate Hawkes Process

To capture interactions between different types of events (e.g., buy/sell, limit/cancel/market orders), the model is extended to a dd-dimensional vector of counting processes N​(t)=(N1​(t),…,Nd​(t))N(t)=(N\_{1}(t),\dots,N\_{d}(t)). Each component has its own intensity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λi​(t)=μi+∑j=1d∫0tϕi​j​(t−s)​𝑑Nj​(s),i=1,…,d,\lambda\_{i}(t)=\mu\_{i}+\sum\_{j=1}^{d}\int\_{0}^{t}\phi\_{ij}(t-s)\,dN\_{j}(s),\quad i=1,\dots,d, |  | (5) |

where μi\mu\_{i} is the baseline intensity of process ii, and ϕi​j\phi\_{ij} encodes how events of type jj influence the future rate of type ii events.
The matrix Φ​(t)=[ϕi​j​(t)]i,j=1d\Phi(t)=[\phi\_{ij}(t)]\_{i,j=1}^{d} is called the kernel matrix, and the process can be compactly written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​(t)=μ+∫0tΦ​(t−s)​𝑑N​(s).\lambda(t)=\mu+\int\_{0}^{t}\Phi(t-s)\,dN(s). |  | (6) |

### 2.3 Stationarity and Stability

Define the integrated kernel matrix K=∫0∞Φ​(s)​𝑑sK=\int\_{0}^{\infty}\Phi(s)\,ds.
The multivariate Hawkes process is stable and stationary if the spectral radius ρ​(K)<1\rho(K)<1.
In that case, the expected intensity vector is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ=(I−K)−1​μ,\Lambda=(I-K)^{-1}\mu, |  | (7) |

where Λi=𝔼​[λi​(t)]\Lambda\_{i}=\mathbb{E}[\lambda\_{i}(t)] is the long run mean event rate of type ii.
This condition ensures that excitation remains bounded and that event clusters do not lead to explosive growth in intensity.

## 3 Microscopic Model of The Limit Order Book (Static Setting)

We model each side of the limit order book as a vector of integer valued queues indexed
by their distance (in ticks) from the mid. Throughout this section, the mid price is held fixed
and the bid ask spread is assumed to be two ticks. Let N∈ℕN\in\mathbb{N} be the maximum depth
we track on each side (in ticks from the mid, excluding the best quote queues themselves).

### 3.1 State, indexing and unit vectors

While our definition of the microscopic structure remains standard our contribution appears in the mesoscopic scaling limit, a Laplacian smoothing term across price levels. We begin by fixing the bid ask spread to be constantly equal to two ticks. This assumption is
appropriate for large tick assets, where the best bid and best ask typically remain stably one
tick away from the mid price. Mathematically, a fixed spread ensures that the queue indices
correspond to fixed tick distances from the mid price, so that the microscopic state space has
constant dimension. Without this assumption, the best bid and best ask queues would shift
position as the spread fluctuates, causing the queue vectors to change dimension over time and
violating the regularity and tightness conditions required for the scaling limit theorem.
Maintaining a constant spread therefore guarantees that the rescaled birth death dynamics evolve
on a stable, fixed coordinate system, which is essential for deriving a diffusion-type limit. We consider two classes of queue vectors, one for the bid side and one for the ask side.
For the bid side, define

|  |  |  |
| --- | --- | --- |
|  | Znb​(t)=(Znb,1​(t),…,Znb,N−1​(t))∈ℤ+N−1.Z^{b}\_{n}(t)=\big(Z^{b,1}\_{n}(t),\ldots,Z^{b,N-1}\_{n}(t)\big)\in\mathbb{Z}\_{+}^{\,N-1}. |  |

For the ask side, define

|  |  |  |
| --- | --- | --- |
|  | Zna​(t)=(Zna,1​(t),…,Zna,N−1​(t))∈ℤ+N−1.Z^{a}\_{n}(t)=\big(Z^{a,1}\_{n}(t),\ldots,Z^{a,N-1}\_{n}(t)\big)\in\mathbb{Z}\_{+}^{\,N-1}. |  |

Here Znb,i​(t)Z^{b,i}\_{n}(t) (resp. Zna,i​(t)Z^{a,i}\_{n}(t)) denotes the number of outstanding buy (resp. sell)
limit orders posted at the price level m−im-i (resp. m+im+i), where mm is the mid price. We
assume that all order and cancellation sizes equal one. At any price level ii on the bid side,
the quantity Znb,i​(t)Z^{b,i}\_{n}(t) increases by one upon the arrival of a buy limit order and decreases
by one following the arrival of a sell market order or a cancellation of an existing buy limit
order. Analogous dynamics hold for Zna,i​(t)Z^{a,i}\_{n}(t) on the ask side.

For i∈{1,…,N−1}i\in\{1,\ldots,N-1\}, we let ei∈ℝN−1e\_{i}\in\mathbb{R}^{N-1} denote the ii-th standard basis
vector.

### 3.2 Microscopic Dynamics

We now describe the microscopic dynamics governing the bid-side queue
process Znb=(Znb,1,…,Znb,N−1)Z^{b}\_{n}=(Z^{b,1}\_{n},\dots,Z^{b,N-1}\_{n}).
At the discrete level, the volume at each price level evolves through a
collection of elementary jumps corresponding to order arrivals, cancellations,
and reallocations of volume between neighbouring price levels.

Each of these elementary mechanisms is represented by an *independent*
Poisson process whose intensity may depend on the current state of the order
book. We denote by eie\_{i} the ii-th canonical basis vector of
ℝN−1\mathbb{R}^{N-1}, and we adopt the convention e0=eN=0e\_{0}=e\_{N}=0.

#### Bid-side dynamics.

For the bid side, the microscopic transitions are as follows:

#### 1. Limit order arrivals.

For every level i∈{1,…,N−1}i\in\{1,\dots,N-1\}, the queue increases by one unit,

|  |  |  |
| --- | --- | --- |
|  | Znb⟶Znb+ei,Z^{b}\_{n}\longrightarrow Z^{b}\_{n}+e\_{i}, |  |

at the arrival rate according
according to the Hawkes process Nb,n,i1​(t)N^{1}\_{b,n,i}(t) with intensity

|  |  |  |  |
| --- | --- | --- | --- |
|  | λb,n,i1​(t)\displaystyle\lambda^{1}\_{b,n,i}(t) | =μb,n,i1​(Znb,i​(t−))+∫0tαb,n,i11​e−βb,n,i11​(t−s)​𝑑Nb,n,i1​(s)+∫0tαb,n,i12​e−βb,n,i12​(t−s)​𝑑Nb,n,i2​(s)\displaystyle=\mu^{1}\_{b,n,i}\!\big(Z^{b,i}\_{n}(t^{-})\big)+\int\_{0}^{t}\alpha^{11}\_{b,n,i}e^{-\beta^{11}\_{b,n,i}(t-s)}\,dN^{1}\_{b,n,i}(s)+\int\_{0}^{t}\alpha^{12}\_{b,n,i}e^{-\beta^{12}\_{b,n,i}(t-s)}\,dN^{2}\_{b,n,i}(s) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫0tαb,n,i14​e−βb,n,i14​(t−s)​𝑑Nb,n,i4​(s).\displaystyle\hskip 72.5001pt+\int\_{0}^{t}\alpha^{14}\_{b,n,i}e^{-\beta^{14}\_{b,n,i}(t-s)}\,dN^{4}\_{b,n,i}(s). |  | (8) |

#### 2. Cancellations and market order removals.

For every level i∈{1,…,N−1}i\in\{1,\dots,N-1\}, one unit is removed from the queue,

|  |  |  |
| --- | --- | --- |
|  | Znb⟶Znb−ei,Z^{b}\_{n}\longrightarrow Z^{b}\_{n}-e\_{i}, |  |

at the arrival rate according to the Hawkes process Nb,n,i2​(t)N^{2}\_{b,n,i}(t) with intensity

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λb,n,i2​(t)\displaystyle\lambda^{2}\_{b,n,i}(t) | =(μb,n,i2​(Znb,i​(t−))+∫0tαb,n,i21​e−βb,n,i21​(t−s)​𝑑Nb,n,i1​(s)+∫0tαb,n,i22​e−βb,n,i22​(t−s)​𝑑Nb,n,i2​(s))​ 1{Znb,i​(t−)>0}.\displaystyle=\Bigg(\mu^{2}\_{b,n,i}\!\big(Z^{b,i}\_{n}(t^{-})\big)+\int\_{0}^{t}\alpha^{21}\_{b,n,i}e^{-\beta^{21}\_{b,n,i}(t-s)}\,dN^{1}\_{b,n,i}(s)+\int\_{0}^{t}\alpha^{22}\_{b,n,i}e^{-\beta^{22}\_{b,n,i}(t-s)}\,dN^{2}\_{b,n,i}(s)\Bigg)\,\mathbf{1}\_{\{Z^{b,i}\_{n}(t^{-})>0\}}. |  | (9) |

#### 3. Volume reallocation: migration from level ii to level i−1i-1.

Each unit of volume sitting at level ii independently attempts to jump one
tick closer to the midprice. Consequently, the queue updates according to

|  |  |  |
| --- | --- | --- |
|  | Znb⟶Znb+ei−1−ei,Z^{b}\_{n}\longrightarrow Z^{b}\_{n}+e\_{i-1}-e\_{i}, |  |

the total migration rate is Hawkes modulated and proportional to the
current queue size:

|  |  |  |
| --- | --- | --- |
|  | λb,ni→i−1​(t)=anb,i​(t)​Znb,i​(t−),\lambda^{i\to i-1}\_{b,n}(t)\;=\;a^{b,i}\_{n}(t)\,Z^{b,i}\_{n}(t-), |  |

where the symmetric Hawkes per unit migration intensity is given by

|  |  |  |
| --- | --- | --- |
|  | anb,i​(t)=ηnb,i+∑ℓ∈{1,2,4}∫0tκℓb,i​e−ρℓb,i​(t−s)​𝑑Nb,n,iℓ​(s).a^{b,i}\_{n}(t)\;=\;\eta^{b,i}\_{n}+\sum\_{\ell\in\{1,2,4\}}\int\_{0}^{t}\kappa^{b,i}\_{\ell}\,e^{-\rho^{b,i}\_{\ell}(t-s)}\,dN^{\ell}\_{b,n,i}(s). |  |

Here ηnb,i≥0\eta^{b,i}\_{n}\geq 0 is the baseline per unit migration rate and
(κℓb,i,ρℓb,i)(\kappa^{b,i}\_{\ell},\rho^{b,i}\_{\ell}) are the Hawkes excitation parameters.
Because migration is symmetric, the same anb,i​(t)a^{b,i}\_{n}(t) governs both inward
and outward jumps.

#### 4. Volume reallocation: migration from level ii to level i+1i+1.

Similarly, each unit of volume may jump one tick further from the midprice.
The corresponding transition is

|  |  |  |
| --- | --- | --- |
|  | Znb⟶Znb+ei+1−ei,Z^{b}\_{n}\longrightarrow Z^{b}\_{n}+e\_{i+1}-e\_{i}, |  |

occurring at total rate

|  |  |  |
| --- | --- | --- |
|  | λb,ni→i+1​(t)=anb,i​(t)​Znb,i​(t−),\lambda^{i\to i+1}\_{b,n}(t)\;=\;a^{b,i}\_{n}(t)\,Z^{b,i}\_{n}(t-), |  |

with the same symmetric Hawkes intensity anb,i​(t)a^{b,i}\_{n}(t) as above.
Symmetry means that the per-unit migration rate towards and away from
the midprice is identical:

|  |  |  |
| --- | --- | --- |
|  | anb,i,+​(t)=anb,i,−​(t)=anb,i​(t).a^{b,i,+}\_{n}(t)=a^{b,i,-}\_{n}(t)=a^{b,i}\_{n}(t). |  |

Thus, migration contributes a discrete Laplacian smoothing effect at the
mesoscopic scale while allowing the strength of reallocation to be
history dependent through Hawkes excitation

These transition rules fully characterise the microscopic bid queue dynamics.
The ask side of the book is defined analogously.

## 4 Mesoscopic Model Of the Limit Order Book

### 4.1 Scaling Limit of the Microscopic Model

We now derive the mesoscopic limit of the microscopic Hawkes driven order book.
Following the scaling arguments of Hambley et al [1], we accelerate time by a
factor of nn and renormalise queue sizes by n\sqrt{n}.
For the bid side, define the rescaled processes

|  |  |  |
| --- | --- | --- |
|  | Z~nb​(t):=Znb​(n​t)nandZ~na​(t):=Zna​(n​t)n.\widetilde{Z}^{\,b}\_{n}(t):=\frac{Z^{\,b}\_{n}(nt)}{\sqrt{n}}\qquad\text{and}\qquad\widetilde{Z}^{\,a}\_{n}(t):=\frac{Z^{\,a}\_{n}(nt)}{\sqrt{n}}. |  |

The limiting processes will form the mesoscopic (continuous volume,
discrete‐price) limit order book.

### 4.2 Scaling assumptions

We impose the following standard conditions, adapted to the Hawkes setting:

* (i)

  Hawkes stability.
  The spectral radius of the Hawkes kernel matrix is strictly less than 1,
  uniformly in nn, ensuring non-explosion and existence of stationary
  intensities.
* (ii)

  Regularity of baselines.
  The baseline functions for arrivals and cancellations satisfy global
  Lipschitz and linear growth bounds in the queue state.
* (iii)

  Moment bounds.
  The initial states satisfy
  supn𝔼​‖Xnk​(0)‖2<∞\sup\_{n}\mathbb{E}\|X^{k}\_{n}(0)\|^{2}<\infty
  for k∈{b,a}k\in\{b,a\}.
* (iv)

  Predictability and conditional independence.
  All microscopic intensities depend on the predictable left-limit
  Znk​(t−)Z^{k}\_{n}(t-), and conditioned on the filtration ℱt−\mathcal{F}\_{t-}—the
  drivers (arrival, cancellation/market, and migration processes) are
  independent.
* (v)

  Boundary behaviour.
  Migration at the boundary levels is blocked consistently with the pinning
  conditions, and Skorokhod reflection is used to preserve non-negativity.

These conditions parallel those in Hambly et al [1].

### 4.3 Limit dynamics

Let

|  |  |  |
| --- | --- | --- |
|  | Atk,i:=limn→∞ank,i​(t)A^{k,i}\_{t}:=\lim\_{n\to\infty}a^{k,i}\_{n}(t) |  |

denote the limiting Hawkes migration intensities.
Let hk,m​(i,x)h\_{k,m}(i,x) denote the drift contribution arising from Hawkes driven
arrivals and cancellations/market orders, and let σk\sigma^{k} be the diffusion
coefficient obtained from the limiting predictable quadratic variations.

The next result gives the mesoscopic reflected diffusion approximation.

###### Theorem 4.1 (Mesoscopic Reflected SDE Limit).

Under the assumptions above, the sequence
(Xnb,Xna)(X^{b}\_{n},X^{a}\_{n}) is tight in
𝔻​([0,∞);ℝN−1)2\mathbb{D}([0,\infty);\mathbb{R}^{N-1})^{2},
and any weak limit (Xb,Xa)(X^{b},X^{a}) is the unique
strong Markov process satisfying, for i=1,…,N−1i=1,\dots,N-1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xtb,i=[Atb,i​(Xtb,i+1+Xtb,i−1−2​Xtb,i)+hb,m​(i,Xtb,i)]​d​t+∑j=1N−1σi​jb​(Xt,At)​d​Wtb,j+d​ηtb,i,\boxed{\begin{aligned} dX^{b,i}\_{t}&=\Big[A^{b,i}\_{t}\,\big(X^{b,i+1}\_{t}+X^{b,i-1}\_{t}-2X^{b,i}\_{t}\big)+h\_{b,m}\!\big(i,X^{b,i}\_{t}\big)\Big]dt+\sum\_{j=1}^{N-1}\sigma^{b}\_{ij}\!\big(X\_{t},A\_{t}\big)\,dW^{b,j}\_{t}+d\eta^{b,i}\_{t},\end{aligned}} |  | (10) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xta,i=[Ata,i​(Xta,i+1+Xta,i−1−2​Xta,i)+ha,m​(i,Xta,i)]​d​t+∑j=1N−1σi​ja​(Xt,At)​d​Wta,j+d​ηta,i,\boxed{\begin{aligned} dX^{a,i}\_{t}&=\Big[A^{a,i}\_{t}\,\big(X^{a,i+1}\_{t}+X^{a,i-1}\_{t}-2X^{a,i}\_{t}\big)+h\_{a,m}\!\big(i,X^{a,i}\_{t}\big)\Big]dt+\sum\_{j=1}^{N-1}\sigma^{a}\_{ij}\!\big(X\_{t},A\_{t}\big)\,dW^{a,j}\_{t}+d\eta^{a,i}\_{t},\end{aligned}} |  | (11) |

where WbW^{b} and WaW^{a} are Brownian motions with covariance determined by the
limiting intensities, and ηtk,i\eta^{k,i}\_{t} are reflection terms enforcing
Xtk,i≥0X^{k,i}\_{t}\geq 0 and Xtk,0=Xtk,N=0X^{k,0}\_{t}=X^{k,N}\_{t}=0.

Theorem [4.1](https://arxiv.org/html/2511.18117v1#S4.Thmtheorem1 "Theorem 4.1 (Mesoscopic Reflected SDE Limit). ‣ 4.3 Limit dynamics ‣ 4 Mesoscopic Model Of the Limit Order Book ‣ Diffusive Limit of Hawkes Driven Order Book Dynamics With Liquidity Migration") shows that symmetric Hawkes migration contributes a
discrete Laplacian smoothing term whose strength is
history dependent through the Hawkes excitation dynamics.
The remaining drift and diffusion coefficients arise from the Hawke
arrival, cancellation, and market order flows.
Full proofs are provided in section 5.

## 5 Mesoscopic model

These events are driven by an underlying multivariate Hawkes process
Nn​(t)N\_{n}(t) whose components correspond to the different event types. Denote by
λn,iup​(t)\lambda^{\mathrm{up}}\_{n,i}(t), λn,idown​(t)\lambda^{\mathrm{down}}\_{n,i}(t),
λn,imig,+​(t)\lambda^{\mathrm{mig},+}\_{n,i}(t) and λn,imig,−​(t)\lambda^{\mathrm{mig},-}\_{n,i}(t)
the corresponding conditional intensities. We assume that, under an appropriate
equilibrium scaling regime, they admit the expansions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λn,iup​(t)\displaystyle\lambda^{\mathrm{up}}\_{n,i}(t) | =n2​σi2​(Z~n,ib​(t))+n​fi​(Z~n,ib​(t))+o​(n),\displaystyle=\frac{n}{2}\,\sigma\_{i}^{2}\big(\tilde{Z}^{b}\_{n,i}(t)\big)+\sqrt{n}\,f\_{i}\big(\tilde{Z}^{b}\_{n,i}(t)\big)+o(\sqrt{n}), |  | (12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λn,idown​(t)\displaystyle\lambda^{\mathrm{down}}\_{n,i}(t) | =n2​σi2​(Z~n,ib​(t))+n​gi​(Z~n,ib​(t))+o​(n),\displaystyle=\frac{n}{2}\,\sigma\_{i}^{2}\big(\tilde{Z}^{b}\_{n,i}(t)\big)+\sqrt{n}\,g\_{i}\big(\tilde{Z}^{b}\_{n,i}(t)\big)+o(\sqrt{n}), |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λn,imig,±​(t)\displaystyle\lambda^{\mathrm{mig},\pm}\_{n,i}(t) | =n​αb​Z~n,ib​(t)+o​(n),\displaystyle=\sqrt{n}\,\alpha\_{b}\,\tilde{Z}^{b}\_{n,i}(t)+o(\sqrt{n}), |  | (14) |

where the effective coefficients σi2\sigma\_{i}^{2}, fif\_{i}, gig\_{i} and αb\alpha\_{b} are
determined by the Hawkes kernels (see Section [6](https://arxiv.org/html/2511.18117v1#S6 "6 Diffusion Covariance Induced by Hawkes Structure ‣ Diffusive Limit of Hawkes Driven Order Book Dynamics With Liquidity Migration")).

### 5.1 Diffusive rescaling

We define
the rescaled process as in the previous section

|  |  |  |
| --- | --- | --- |
|  | Z~nb​(t):=Znb​(n​t)n,t≥0.\tilde{Z}^{b}\_{n}(t):=\frac{Z^{b}\_{n}(nt)}{\sqrt{n}},\qquad t\geq 0. |  |

The state space of Z~nb\tilde{Z}^{b}\_{n} is the lattice
1n​ℕN−1⊂ℝ+N−1\frac{1}{\sqrt{n}}\mathbb{N}^{N-1}\subset\mathbb{R}\_{+}^{N-1}, and each jump
of the microscopic process corresponds to a displacement of size 1/n1/\sqrt{n}
in one or two coordinates of Z~nb\tilde{Z}^{b}\_{n}.

### 5.2 Generator of the rescaled process

For a bounded function F:1n​ℕN−1→ℝF:\frac{1}{\sqrt{n}}\mathbb{N}^{N-1}\to\mathbb{R}, the infinitesimal
generator AnA\_{n} of the rescaled process Z~nb\tilde{Z}^{b}\_{n} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | An​F​(y)=∑Δrate​(y→y+Δ)​(F​(y+Δ)−F​(y))A\_{n}F(y)=\sum\_{\Delta}\text{rate}(y\to y+\Delta)\,\big(F(y+\Delta)-F(y)\big) |  | (15) |

where the sum runs over all admissible jump vectors
Δ∈1n​{0,±ei,±ei±ej}\Delta\in\frac{1}{\sqrt{n}}\{0,\pm e\_{i},\pm e\_{i}\pm e\_{j}\}.

To write AnA\_{n} in a form amenable to Taylor expansion, we introduce the
finite difference operators

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δn,kr​F​(y)\displaystyle\Delta^{r}\_{n,k}F(y) | :=n​(F​(y+ek/n)−F​(y)),\displaystyle:=\sqrt{n}\,\big(F(y+e\_{k}/\sqrt{n})-F(y)\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Δn,kl​F​(y)\displaystyle\Delta^{l}\_{n,k}F(y) | :=n​(F​(y)−F​(y−ek/n)),\displaystyle:=\sqrt{n}\,\big(F(y)-F(y-e\_{k}/\sqrt{n})\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Δn,k2​F​(y)\displaystyle\Delta^{2}\_{n,k}F(y) | :=n​(F​(y+ek/n)+F​(y−ek/n)−2​F​(y)).\displaystyle:=n\,\big(F(y+e\_{k}/\sqrt{n})+F(y-e\_{k}/\sqrt{n})-2F(y)\big). |  |

Using the microscopic dynamics and the intensity expansions (10), one checks that
An​F​(y)A\_{n}F(y) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | An​F​(y)\displaystyle A\_{n}F(y) | =∑k=1N−112​Δn,k2​F​(y)​σk2​(yk)​ 1{yk≥1/n}\displaystyle=\sum\_{k=1}^{N-1}\frac{1}{2}\,\Delta^{2}\_{n,k}F(y)\,\sigma\_{k}^{2}(y\_{k})\,\mathbf{1}\_{\{y\_{k}\geq 1/\sqrt{n}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑k=1N−1Δn,kr​F​(y)​σk2​(yk)n​ 1{yk=0}\displaystyle\quad+\sum\_{k=1}^{N-1}\Delta^{r}\_{n,k}F(y)\,\frac{\sigma\_{k}^{2}(y\_{k})}{\sqrt{n}}\,\mathbf{1}\_{\{y\_{k}=0\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑k=1N−1[Δn,kr​F​(y)​fk​(yk)−Δn,kl​F​(y)​gk​(yk)​ 1{yk≥1/n}]\displaystyle\quad+\sum\_{k=1}^{N-1}\Big[\Delta^{r}\_{n,k}F(y)\,f\_{k}(y\_{k})-\Delta^{l}\_{n,k}F(y)\,g\_{k}(y\_{k})\,\mathbf{1}\_{\{y\_{k}\geq 1/\sqrt{n}\}}\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∑k=1N−1αb​yk​(Δn,k−1r​F​(y−ek/n)+Δn,k+1r​F​(y−ek/n)−2​Δn,kl​F​(y)).\displaystyle\quad+\sum\_{k=1}^{N-1}\alpha\_{b}\,y\_{k}\,\Big(\Delta^{r}\_{n,k-1}F(y-e\_{k}/\sqrt{n})+\Delta^{r}\_{n,k+1}F(y-e\_{k}/\sqrt{n})-2\Delta^{l}\_{n,k}F(y)\Big). |  | (16) |

with the conventions y0=yN=0y\_{0}=y\_{N}=0 and Δn,0r​F=Δn,Nr​F≡0\Delta^{r}\_{n,0}F=\Delta^{r}\_{n,N}F\equiv 0.

#### Remark 5.2.1

The representation of the microscopic generator in (11)
and the rescaling procedure follow the classical diffusion approximation
framework for density dependent Markov jump processes developed by Ethier
and Kurtz; see [10].

### 5.3 Limit generator via Taylor expansion

Let F∈Cb2​(ℝ+N−1)F\in C^{2}\_{b}(\mathbb{R}\_{+}^{N-1}) be a twice continuously differentiable
function with bounded derivatives, satisfying the Neumann boundary condition
∂xkF​(x)|xk=0=0\partial\_{x\_{k}}F(x)\big|\_{x\_{k}=0}=0 for all kk. For such FF, Taylor’s
theorem yields, uniformly on compact sets,

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(x±ekn)\displaystyle F\Big(x\pm\frac{e\_{k}}{\sqrt{n}}\Big) | =F​(x)±1n​∂xkF​(x)+12​n​∂xk​xk2F​(x)+O​(n−3/2),\displaystyle=F(x)\pm\frac{1}{\sqrt{n}}\,\partial\_{x\_{k}}F(x)+\frac{1}{2n}\,\partial^{2}\_{x\_{k}x\_{k}}F(x)+O\big(n^{-3/2}\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Δn,kr​F​(x)\displaystyle\Delta^{r}\_{n,k}F(x) | =∂xkF​(x)+O​(n−1/2),\displaystyle=\partial\_{x\_{k}}F(x)+O\big(n^{-1/2}\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Δn,kl​F​(x)\displaystyle\Delta^{l}\_{n,k}F(x) | =∂xkF​(x)+O​(n−1/2),\displaystyle=\partial\_{x\_{k}}F(x)+O\big(n^{-1/2}\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Δn,k2​F​(x)\displaystyle\Delta^{2}\_{n,k}F(x) | =∂xk​xk2F​(x)+O​(n−1/2).\displaystyle=\partial^{2}\_{x\_{k}x\_{k}}F(x)+O\big(n^{-1/2}\big). |  |

A similar expansion applied to the migration combination

|  |  |  |
| --- | --- | --- |
|  | Δn,k−1r​F​(x−ek/n)+Δn,k+1r​F​(x−ek/n)−2​Δn,kl​F​(x)\Delta^{r}\_{n,k-1}F(x-e\_{k}/\sqrt{n})+\Delta^{r}\_{n,k+1}F(x-e\_{k}/\sqrt{n})-2\Delta^{l}\_{n,k}F(x) |  |

shows that

|  |  |  |
| --- | --- | --- |
|  | Δn,k−1r​F​(x−ek/n)+Δn,k+1r​F​(x−ek/n)−2​Δn,kl​F​(x)=(xk+1+xk−1−2​xk)​∂xkF​(x)+O​(n−1/2).\Delta^{r}\_{n,k-1}F(x-e\_{k}/\sqrt{n})+\Delta^{r}\_{n,k+1}F(x-e\_{k}/\sqrt{n})-2\Delta^{l}\_{n,k}F(x)=\big(x\_{k+1}+x\_{k-1}-2x\_{k}\big)\,\partial\_{x\_{k}}F(x)+O\big(n^{-1/2}\big). |  |

#### Remark 5.2.2

These Taylor expansions are standard in the analysis of weak convergence
for scaled Markov jump processes [[10](https://arxiv.org/html/2511.18117v1#bib.bib10), Ch. 7]. Very
similar generator expansions appear in the limit order book scaling limits
of Hambly and Ledger [7] and Horst and Paul [6], to which our setting is closely related.

Substituting these expansions into (10), we obtain

|  |  |  |
| --- | --- | --- |
|  | An​F​(x)=A​F​(x)+Rn​(F,x),A\_{n}F(x)=AF(x)+R\_{n}(F,x), |  |

where the *candidate limit generator* AA is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​F​(x)=∑k=1N−1[12​σk2​(xk)​∂2F∂xk2​(x)+(hk​(xk)+αb​(xk+1+xk−1−2​xk))​∂F∂xk​(x)],AF(x)=\sum\_{k=1}^{N-1}\bigg[\frac{1}{2}\,\sigma\_{k}^{2}(x\_{k})\,\frac{\partial^{2}F}{\partial x\_{k}^{2}}(x)+\Big(h\_{k}(x\_{k})+\alpha\_{b}\big(x\_{k+1}+x\_{k-1}-2x\_{k}\big)\Big)\,\frac{\partial F}{\partial x\_{k}}(x)\bigg], |  | (17) |

with hk:=fk−gkh\_{k}:=f\_{k}-g\_{k}, and the remainder satisfies

|  |  |  |
| --- | --- | --- |
|  | supx∈K|Rn​(F,x)|⟶ 0for every compact ​K⊂ℝ+N−1.\sup\_{x\in K}\,\big|R\_{n}(F,x)\big|\;\longrightarrow\;0\qquad\text{for every compact }K\subset\mathbb{R}\_{+}^{N-1}. |  |

The operator AA is understood on the domain

|  |  |  |
| --- | --- | --- |
|  | 𝒟​(A):={F∈Cb2​(ℝ+N−1):∂xkF​(x)|xk=0=0​ for all ​k},\mathcal{D}(A):=\big\{F\in C^{2}\_{b}(\mathbb{R}\_{+}^{N-1}):\partial\_{x\_{k}}F(x)\big|\_{x\_{k}=0}=0\text{ for all }k\big\}, |  |

which encodes reflection at the boundary xk=0x\_{k}=0.

#### Remark 5.2.3

The interpretation of AA as the generator of a diffusion process with
normal reflection on the boundary {xk=0}\{x\_{k}=0\} is based on the classical
framework of Lions and Sznitman for reflected stochastic differential
equations; see [11].

### 5.4 Mesoscopic reflected SDE

The generator AA in (11) is the generator of a
reflected diffusion Xb=(Xb,1,…,Xb,N−1)X^{b}=(X^{b,1},\dots,X^{b,N-1}) solving the SDE system

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xtb,i\displaystyle dX^{b,i}\_{t} | =[hi​(Xtb,i)+αb​(Xtb,i+1+Xtb,i−1−2​Xtb,i)]​d​t\displaystyle=\Big[h\_{i}\big(X^{b,i}\_{t}\big)+\alpha\_{b}\big(X^{b,i+1}\_{t}+X^{b,i-1}\_{t}-2X^{b,i}\_{t}\big)\Big]\,dt |  | (18) |
|  |  | +σi​(Xtb,i)​d​Wtb,i+d​ηtb,i,i=1,…,N−1,\displaystyle\quad+\sigma\_{i}\big(X^{b,i}\_{t}\big)\,dW^{b,i}\_{t}+d\eta^{b,i}\_{t},\qquad i=1,\dots,N-1, |  |
|  | Xtb,0\displaystyle X^{b,0}\_{t} | =Xtb,N=0,\displaystyle=X^{b,N}\_{t}=0, |  |

where Wb=(Wb,1,…,Wb,N−1)W^{b}=(W^{b,1},\dots,W^{b,N-1}) is a Brownian motion in
ℝN−1\mathbb{R}^{N-1} with covariance structure specified in
Section [6](https://arxiv.org/html/2511.18117v1#S6 "6 Diffusion Covariance Induced by Hawkes Structure ‣ Diffusive Limit of Hawkes Driven Order Book Dynamics With Liquidity Migration"), and ηb,i\eta^{b,i} are non-decreasing
processes ensuring reflection at zero:

|  |  |  |
| --- | --- | --- |
|  | Xtb,i≥0,∫0∞Xtb,i​𝑑ηtb,i=0.X^{b,i}\_{t}\geq 0,\quad\int\_{0}^{\infty}X^{b,i}\_{t}\,d\eta^{b,i}\_{t}=0. |  |

Standard results on martingale problems for reflected diffusions (see,
[11] ) imply that the martingale problem for (A,𝒟​(A))(A,\mathcal{D}(A))
is well posed. Together with the generator convergence An→AA\_{n}\to A on
𝒟​(A)\mathcal{D}(A) and the general convergence theory for Markov processes in
[[10](https://arxiv.org/html/2511.18117v1#bib.bib10)], this yields the following mesoscopic limit:

###### Theorem 5.1.

As n→∞n\to\infty, the rescaled queue process Z~nb\tilde{Z}^{b}\_{n} converges in
distribution in D​([0,∞);ℝ+N−1)D([0,\infty);\mathbb{R}\_{+}^{N-1}) to the reflected diffusion
XbX^{b} solving (12).

## 6 Diffusion Covariance Induced by Hawkes Structure

We now make explicit how the covariance structure of the Brownian motion
WbW^{b} in (12) is determined by the underlying Hawkes
kernels.

### 6.1 Multivariate Hawkes specification

We index all microscopic event types on the bid side
by a=1,…,Ma=1,\dots,M and collect them in the
MM-dimensional Hawkes process

|  |  |  |
| --- | --- | --- |
|  | N​(t)=(N1​(t),…,NM​(t))⊤.N(t)=\big(N^{1}(t),\dots,N^{M}(t)\big)^{\top}. |  |

Its intensity process λ​(t)=(λ1​(t),…,λM​(t))⊤\lambda(t)=(\lambda^{1}(t),\dots,\lambda^{M}(t))^{\top}
satisfies

|  |  |  |
| --- | --- | --- |
|  | λ​(t)=μ+∫0tΦ​(t−s)​𝑑N​(s),\lambda(t)=\mu+\int\_{0}^{t}\Phi(t-s)\,dN(s), |  |

where μ∈ℝ+M\mu\in\mathbb{R}^{M}\_{+} is the vector of baseline intensities and
Φ​(t)=(ϕi​j​(t))1≤i,j≤M\Phi(t)=\big(\phi\_{ij}(t)\big)\_{1\leq i,j\leq M} is the non-negative kernel
matrix.

Define the *integrated kernel*

|  |  |  |
| --- | --- | --- |
|  | K:=∫0∞Φ​(u)​𝑑u=(∫0∞ϕi​j​(u)​𝑑u)1≤i,j≤M,K:=\int\_{0}^{\infty}\Phi(u)\,du=\bigg(\int\_{0}^{\infty}\phi\_{ij}(u)\,du\bigg)\_{1\leq i,j\leq M}, |  |

and assume the stability condition ρ​(K)<1\rho(K)<1, where ρ​(K)\rho(K) denotes the
spectral radius of KK. Under stationarity, the mean intensity vector
Λ¯:=𝔼​[λ​(t)]\bar{\Lambda}:=\mathbb{E}[\lambda(t)] is then given by

|  |  |  |
| --- | --- | --- |
|  | Λ¯=(I−K)−1​μ.\bar{\Lambda}=(I-K)^{-1}\mu. |  |

### 6.2 Functional central limit theorem for event counts

The multivariate Hawkes FCLT( see [[12](https://arxiv.org/html/2511.18117v1#bib.bib12)])
implies that under
the diffusive scaling,

|  |  |  |
| --- | --- | --- |
|  | 1n​(N​(n​t)−n​t​Λ¯)⇒𝒩​(0,t​ΣN),\frac{1}{\sqrt{n}}\Big(N(nt)-nt\,\bar{\Lambda}\Big)\;\Rightarrow\;\mathcal{N}\big(0,\,t\,\Sigma\_{N}\big), |  |

where the asymptotic covariance matrix ΣN\Sigma\_{N} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣN=(I−K)−1​diag​(Λ¯)​(I−K)−⊤.\Sigma\_{N}=(I-K)^{-1}\,\mathrm{diag}(\bar{\Lambda})\,(I-K)^{-\top}. |  | (19) |

Equivalently, one may write

|  |  |  |
| --- | --- | --- |
|  | 1n​(N​(n​t)−n​t​Λ¯)⇒(I−K)−1​diag​(Λ¯)1/2​Wt,\frac{1}{\sqrt{n}}\Big(N(nt)-nt\,\bar{\Lambda}\Big)\;\Rightarrow\;(I-K)^{-1}\,\mathrm{diag}(\bar{\Lambda})^{1/2}\,W\_{t}, |  |

for a standard MM-dimensional Brownian motion WW, in which case
ΣN=(I−K)−1​diag​(Λ¯)​(I−K)−⊤\Sigma\_{N}=(I-K)^{-1}\mathrm{diag}(\bar{\Lambda})(I-K)^{-\top} is precisely
the covariance of the Gaussian limit.

### 6.3 Covariance of queue volumes

The (rescaled) bid side queue volumes Z~nb\tilde{Z}^{b}\_{n} are linear functionals of
the event counts NN. There exists an incidence matrix
C∈ℝ(N−1)×MC\in\mathbb{R}^{(N-1)\times M} such that

|  |  |  |
| --- | --- | --- |
|  | Z~nb​(t)=Znb​(n​t)n=C​N​(n​t)n.\tilde{Z}^{b}\_{n}(t)=\frac{Z^{b}\_{n}(nt)}{\sqrt{n}}=C\,\frac{N(nt)}{\sqrt{n}}. |  |

Each column of CC encodes the effect of a single event type on the queue
profile (for instance, a unit up-jump at level ii contributes +1+1 to row ii,
a down jump contributes −1-1, and a migration i→i+1i\to i+1 contributes −1-1 to
row ii and +1+1 to row i+1i+1).

It follows from the FCLT and linearity that

|  |  |  |
| --- | --- | --- |
|  | Znb​(n​t)−n​t​C​Λ¯n⇒𝒩​(0,t​ΣX),\frac{Z^{b}\_{n}(nt)-nt\,C\bar{\Lambda}}{\sqrt{n}}\;\Rightarrow\;\mathcal{N}\big(0,\,t\,\Sigma\_{X}\big), |  |

where the asymptotic covariance matrix of the queue volumes is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣX=C​ΣN​C⊤=C​(I−K)−1​diag​(Λ¯)​(I−K)−⊤​C⊤.\Sigma\_{X}=C\,\Sigma\_{N}\,C^{\top}=C\,(I-K)^{-1}\,\mathrm{diag}(\bar{\Lambda})\,(I-K)^{-\top}C^{\top}. |  | (20) |

Thus, in the mesoscopic SDE, one can
choose the diffusion matrix Γ​(x)\Gamma(x) such that
Γ​(x)​Γ​(x)⊤=ΣX\Gamma(x)\Gamma(x)^{\top}=\Sigma\_{X} (for instance, via a Cholesky
factorisation), and the Brownian motion WbW^{b} is related to the underlying
Hawkes fluctuations through ([20](https://arxiv.org/html/2511.18117v1#S6.E20 "In 6.3 Covariance of queue volumes ‣ 6 Diffusion Covariance Induced by Hawkes Structure ‣ Diffusive Limit of Hawkes Driven Order Book Dynamics With Liquidity Migration")). This makes explicit how
both the endogenous order flow and the self-exciting liquidity migration
mechanisms shape the covariance structure of the mesoscopic queue dynamics.

## 7 Conclusions

In this work we have developed a mesoscopic description of the bid-side
queue dynamics in a limit order book driven by a multivariate Hawkes process.
Starting from a fully microscopic specification in which individual order
arrivals, cancellations and migrations are encoded as components of a Hawkes
counting process, we introduced a diffusive rescaling under which time is
accelerated by a factor nn and queue sizes are of order n\sqrt{n}. In this
regime, and under suitable equilibrium intensity expansions, we derived the
infinitesimal generator of the rescaled queue process and showed that it
converges to the generator of a reflected diffusion on ℝ+N−1\mathbb{R}\_{+}^{N-1}.

More concretely, we obtained a mesoscopic SDE system, in which each queue level evolves as a one-dimensional
diffusion with state dependent drift and volatility, coupled across levels through
a discrete Laplacian term that encodes liquidity migration. Reflection at zero is
implemented via a Skorokhod type term ensuring non-negativity of the queues and a
Neumann boundary condition in the associated generator. This provides a rigorous
link between the underlying self-exciting order flow and an effective
interacting diffusion description of the queue dynamics.

#### 

In the second part of the analysis we made explicit how the diffusion
coefficients in the mesoscopic model are determined by the Hawkes structure.
Using a functional central limit theorem for multivariate Hawkes processes, we
expressed the asymptotic covariance matrix of the event counts in terms of the
integrated kernel and the stationary intensities. Through a
linear incidence mapping between event types and queue increments, this yields a
closed form expression for the covariance matrix of the mesoscopic queue
fluctuations and, consequently, for the diffusion matrix. In this way, the model retains a clear microscopic
interpretation while admitting a tractable diffusion limit

### 7.1 Future Research

A key next step is to calibrate the microscopic Hawkes parameters and the
resulting mesoscopic coefficients to high frequency limit order book data.
This would involve estimating the kernel matrix and baseline intensities from
event time series, constructing the corresponding branching matrix, and
comparing empirical queue fluctuations with those predicted by the diffusion
limit. One could then assess, for example, how well the Laplacian coupling
captures observed liquidity migration and how the theoretical covariance
structure compares to empirical covariances across levels and maturities.

From a computational perspective, it would be important to develop efficient
numerical schemes for simulating the reflected mesoscopic SDE, taking into account both the non-negativity
constraint and the coupling across levels. This includes the design and
analysis of discretisation methods that preserve reflection and stability,
as well as variance reduction techniques that exploit the Hawkes induced
covariance structure. Such schemes would be useful both for model validation
and for applications in optimal execution, liquidity risk management and
stress testing.

#### 

Another direction is to consider a further scaling in which the spacing
between price levels tends to zero, leading to a continuum of levels limit.
In this regime one expects the discrete Laplacian coupling to converge to a
second order spatial derivative, and the mesoscopic SDE system to approach a
stochastic partial differential equation (SPDE) for the queue density as a
function of price and time. This would provide a bridge between microscopic
Hawkes based models and macroscopic SPDE descriptions of limit order books,
and could be used to analyse large scale properties such as liquidity
profiles and volatility clustering.

Finally, the Hawkes specification itself can be enriched in several ways,
for instance by allowing cross-excitation between different levels and
event types, including state dependence in the kernel or baseline terms, or
incorporating regimes and non linear saturation effects. Each of these
extensions would induce a modified diffusion covariance structure and could
lead to qualitatively different mesoscopic behaviour. Understanding the
impact of such modeling choices on the resulting diffusion limit and on
observables such as queue correlation, imbalance dynamics and price impact
remains an interesting topic for future work.

Overall, the mesoscopic reflected diffusion derived here offers a natural
starting point for further theoretical analysis and calibration to market data.

## References

* [1]

  B. Hambly, J. Kalsi, and J. Newbury,
  “Limit order books, diffusion approximations and reflected SPDEs: from microscopic to macroscopic models,”
  arXiv:2018.
* [2]

  C. E. Parlour and D. J. Seppi,
  “Limit order markets: A survey,”
  in Handbook of Financial Intermediation and Banking,
  A. W. Thakor and A. Boot, Eds.,
  Amsterdam, Netherlands: Elsevier, 2008, pp. 63–95.
* [3]

  P. Hewlett,
  “Clustering of order arrivals, price impact and trade path optimisation,”
  Workshop on Financial Modeling with Jump Processes,
  Ecole Polytechnique, 2006, pp. 6–8.
* [4]

  R. Cont and A. de Larrard,
  “Price dynamics in a Markovian limit order market,”
  arXiv:1104.4596, 2011.
* [5]

  E. Bacry, S. Gaiffas, and J. F. Muzy,
  “Queue-reactive Hawkes processes for limit order books,”
  arXiv:1502.04592, 2015.
* [6]

  U. Horst and J. Paul,
  “A diffusion limit for a Hawkes-type limit order book model,”
  arXiv:1901.06740, 2019.
* [7]

  B. Hambly and S. Ledger,
  “A continuum limit for order book models,”
  SIAM Journal on Financial Mathematics,
  vol. 9, no. 3, pp. 865–911, 2018.
* [8]

  X. Chen,
  “Modelling order flow dynamics using Hawkes processes,”
  Ph.D. dissertation, Florida State University, 2017.
* [9]

  F. Abergel and A. Jedidi,
  “A mathematical approach to order book modeling,”
  arXiv:1104.4596, 2011.
* [10]

  S. N. Ethier and T. G. Kurtz,
  Markov Processes: Characterization and Convergence,
  Wiley, New York, 1986.
* [11]

  J.-L. Lions and A.-S. Sznitman,
  “Stochastic differential equations with reflecting boundary conditions,”
  Communications on Pure and Applied Mathematics,
  vol. 37, no. 4, pp. 511–537, 1984.
* [12]

  E. Bacry, S. Gaïffas, and J.-F. Muzy,
  “A generalized method for multivariate Hawkes processes,”
  arXiv preprint arXiv:1502.04592, 2015.