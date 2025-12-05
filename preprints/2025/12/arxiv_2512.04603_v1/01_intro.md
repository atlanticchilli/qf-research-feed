---
authors:
- Alexander Barzykin
- Robert Boyce
- Eyal Neuman
doc_id: arxiv:2512.04603v1
family_id: arxiv:2512.04603
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: FX Market Making with Internal Liquidity
url_abs: http://arxiv.org/abs/2512.04603v1
url_html: https://arxiv.org/html/2512.04603v1
venue: arXiv q-fin
version: 1
year: 2025
---


Alexander Barzykin
HSBC

Robert Boyce
HSBC
Department of Mathematics, Imperial College London

Eyal Neuman
Department of Mathematics, Imperial College London

###### Abstract

As the FX markets continue to evolve, many institutions have started offering passive access to their internal liquidity pools.
Market makers act as principal and have the opportunity to fill those orders as part of their risk management, or they may choose to adjust pricing to their external OTC franchise to facilitate the matching flow.
It is, a priori, unclear how the strategies managing internal liquidity should depend on market condions, the market maker’s risk appetite, and the placement algorithms deployed by participating clients.
The market maker’s actions in the presence of passive orders are relevant not only for their own objectives, but also for those liquidity providers who have certain expectations of the execution speed.
In this work, we investigate the optimal multi-objective strategy of a market maker with an option to take liquidity on an internal exchange, and draw important qualitative insights for real-world trading.

## 1 Introduction

Internalisation has long been a key component of efficient algorithmic execution in foreign exchange (FX) markets, primarily due to its reduced visibility and consequently minimal market impact. Traditional internalisation typically involves client-to-client matching, where a liquidity provider acts as a neutral intermediary. This mechanism, classified as Internalisation Type A by the Foreign Exchange Professionals Association (FXPA) [[15](https://arxiv.org/html/2512.04603v1#bib.bib15)], offers certain advantages but also inherent limitations, as matching opportunities tend to be scarce.

Since FX trading remains largely over-the-counter (OTC), interaction with OTC liquidity is expected to be the primary driver of internalisation. The FXPA defines Internalisation Type B as the offsetting of commercial flow by a liquidity provider. This naturally involves client algorithms trading against a market maker’s pricing stream, benefitting from ultra-low latency and potentially tighter spreads due to inventory skew.

Recently, several institutions have begun offering passive access to internal liquidity, either through conventional limit or pegged orders. Dynamic orders are typically pegged to an internally maintained fair reference price, allowing client algorithms to communicate in the “high-frequency language” of the market maker, without requiring high-frequency order management. Market makers may fill these orders to meet their risk management objectives; importantly, they can also adjust pricing in their OTC franchise to facilitate such fills. In this way, client algorithms can interact with deep OTC liquidity through the internalisation mechanism.

One might tacitly assume that market makers directly transfer pegged order quantities onto their pricing ladder at the same price and then immediately fill them upon receiving an opposing trade. However, such a naïve approach would clearly be detrimental to the market maker’s risk management and would reduce potential P&L. In practice, market makers must instead solve an optimal market-making problem in the presence of an additional liquidity source, be it a single limit order or, more generally, a limit order book on an internal exchange.

Understanding the underlying mathematical formulation of this problem can improve the transparency of internalisation, in line with recent FXPA guidance. Orders on the internal exchange cannot be taken for granted: they may be cancelled, be of finite but unknown size, or follow an unpredictable strategy and thus may not always be available. Moreover, the market-making desk may prefer to fill client orders on the internal exchange, as doing so supports the firm’s client algo desk, which manages those orders, and ultimately provides better service to clients. The market-making desk therefore faces a complex and multifaceted trade-off.

The mathematical finance literature on market making originates from the model of Avellaneda and Stoikov [[12](https://arxiv.org/html/2512.04603v1#bib.bib12)], later solved in closed form by Guéant et al. [[8](https://arxiv.org/html/2512.04603v1#bib.bib8)]. Subsequent extensions include the linear–quadratic framework of Cartea et al [[13](https://arxiv.org/html/2512.04603v1#bib.bib13)], influential order effects in Cartea et al. [[1](https://arxiv.org/html/2512.04603v1#bib.bib1)], continuous hedging in Barzykin et al. [[5](https://arxiv.org/html/2512.04603v1#bib.bib5)], and competition among market makers in Boyce et al. [[11](https://arxiv.org/html/2512.04603v1#bib.bib11)]. Interactions between market makers and clients have also been explored, notably through the game-theoretic approach of Cartea and Sánchez-Betancourt [[4](https://arxiv.org/html/2512.04603v1#bib.bib4)], while internalisation has been examined in various contexts, including the FX market in Butz and Oomen [[6](https://arxiv.org/html/2512.04603v1#bib.bib6)].
Since Avellaneda and Stoikov [[12](https://arxiv.org/html/2512.04603v1#bib.bib12)], financial markets and the role of market makers have evolved substantially. A key recent innovation is the emergence of internal exchanges, enabling clients to provide liquidity directly to market makers. This remains largely unexplored, with the exception of Morimoto [[3](https://arxiv.org/html/2512.04603v1#bib.bib3)], who study optimal execution under unlimited internal liquidity with price impact. Relatedly, passive impact has attracted renewed attention, most notably in Chahdi et al. [[9](https://arxiv.org/html/2512.04603v1#bib.bib9)].

In this work, we present the first quantitative investigation of internal exchange management from the market maker’s perspective. We develop a model in which the market maker continuously streams a price ladder of multiple sizes to external, liquidity-taking clients while optimally timing trades with liquidity-providing clients on an internal exchange. The market maker aims to maximise P&L while remaining averse to large inventory positions and unfilled internal orders. Internal exchange orders are transient, that is they may be cancelled, executed, or reappear later, capturing realistic client execution patterns such as iceberg, TWAP, or full-amount strategies. From a mathematical perspective, our formulation of the market maker’s problem leads to a stochastic control problem over external prices, consistent with classical market-making frameworks [[12](https://arxiv.org/html/2512.04603v1#bib.bib12), [7](https://arxiv.org/html/2512.04603v1#bib.bib7)], combined with repeated optimal stopping decisions for the timing of internal trades, as in the optimal execution framework of [[2](https://arxiv.org/html/2512.04603v1#bib.bib2), [3](https://arxiv.org/html/2512.04603v1#bib.bib3)]. The resulting Hamilton–Jacobi–Bellman quasi-variational inequality (HJBQVI) is then solved numerically.

We derive practical insights with direct relevance to real-world trading. In particular, we demonstrate that there exists an execution threshold, i.e. the inventory level beyond which the market maker will instantaneously fill the limit order. Otherwise, the market maker will adjust pricing to external OTC clients accelerating the move towards the execution threshold, thus facilitating the fill of the limit order. The degree of price skew and the execution threshold level depend on the market maker’s risk aversion, limit order depth and expected placement strategy, as well as on flow facilitation initiatives. Importantly, the optimal strategy significantly outperforms a naïve benchmark strategy that directly incorporates internal exchange orders into the OTC pricing ladder.

## 2 The model

Let T>0T>0 denote the trading period. We fix a filtered probability space (Ω,ℱ,𝔽={ℱt}t∈[0,T],ℙ)(\Omega,\mathcal{F},\mathbb{F}=\{\mathcal{F}\_{t}\}\_{t\in[0,T]},\mathbb{P}) satisfying the usual hypothesis. Let (St)t≥0(S\_{t})\_{t\geq 0} be the price process of a risky asset such that St=S0+σ​WtS\_{t}=S\_{0}+\sigma W\_{t}, where WW is a standard Brownian motion and S0,σS\_{0},\,\sigma are positive constants. We consider a market maker who continuously provides liquidity on both sides of the order book, quoting bid and ask prices (Sb,z,Sa,z)(S^{b,z},S^{a,z}) that are streamed and adjusted according to the clients’ order sizes 𝒵={zk, 1≤k≤K}\mathcal{Z}=\{z\_{k},\,1\leq k\leq K\}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Stb,z=St−δtb,zandSta,z=St+δta,z,0≤t≤T,z∈𝒵.S^{b,z}\_{t}=S\_{t}-\delta^{b,z}\_{t}\qquad\text{and}\qquad S^{a,z}\_{t}=S\_{t}+\delta^{a,z}\_{t},\quad 0\leq t\leq T,\quad z\in\mathcal{Z}. |  | (2.1) |

Note that the half-spreads (δb,z,δa,z)(\delta^{b,z},\delta^{a,z}) are controlled by the market maker and chosen from the set of admissible half-spreads

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟={δ:δ​ progressively measurable s.t. ​𝔼​[∫0Tδt2​𝑑t]<∞}.\mathcal{D}=\left\{\delta:\delta\text{ progressively measurable s.t. }\mathbb{E}\left[\int\_{0}^{T}\delta^{2}\_{t}dt\right]<\infty\right\}. |  | (2.2) |

Market buy and sell orders of OTC clients are modelled by independent counting processes Na,z=(Nta,z)t≥0N^{a,z}=(N\_{t}^{a,z})\_{t\geq 0} and Nb,z=(Ntb,z)t≥0N^{b,z}=(N\_{t}^{b,z})\_{t\geq 0} for any order size z∈𝒵z\in\mathcal{Z}, with intensities

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λb/a,z​(δtb/a,z)=λb/a,z​exp⁡(−κz​δtb/a,z)0≤t≤T.\Lambda^{b/a,z}(\delta^{b/a,z}\_{t})=\lambda^{b/a,z}\exp\Big(-\kappa^{z}\delta^{b/a,z}\_{t}\Big)\qquad 0\leq t\leq T. |  | (2.3) |

Here λb/a,z\lambda^{b/a,z} and κz\kappa^{z} are positive constants.

We assume that, in the internal exchange, the client has placed a limit order on one side of the book. Without loss of generality, we take this to be an ask limit order with an initial size of ℓ¯\overline{\ell}; that is, the client intends to sell, and the dealer would buy if a trade occurs.

The order size at any time tt, denoted by {Lt}0,T\{L\_{t}\}\_{0,T} which is a càdlàg process that determines the liquidity in the internal exchange and it is given by,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt=ℓ¯−ℓ¯​∫0t𝟙{Ls>0}​𝑑Cs+ℓ¯​∫0t𝟙{Ls≤0}​𝑑As+ℓ¯​Rt−Mt,0≤t≤T,L\_{t}=\overline{\ell}-\overline{\ell}\int\_{0}^{t}\mathbbm{1}\_{\{L\_{s}>0\}}dC\_{s}+\overline{\ell}\int\_{0}^{t}\mathbbm{1}\_{\{L\_{s}\leq 0\}}dA\_{s}+\overline{\ell}R\_{t}-M\_{t},\quad 0\leq t\leq T, |  | (2.4) |

Note that ℓ¯>0\overline{\ell}>0 corresponds to an order being present at time t=0t=0, whereas ℓ¯≤0\overline{\ell}\leq 0 indicates the absence of an order. Moreover, larger magnitudes of ℓ¯\overline{\ell} decrease the likelihood of the order appearing, since liquidity can be consumed by the market maker only when Lt>0L\_{t}>0 in ([2.4](https://arxiv.org/html/2512.04603v1#S2.E4 "In 2 The model ‣ FX Market Making with Internal Liquidity")). The processes (A,C,M,R)(A,C,M,R) are defined and characterized below.

* •

  (Ct)t≥0(C\_{t})\_{t\geq 0} represents the cancellation of the order by the client and is modelled as an independent Poisson process with intensity ν\nu and unit jump size. An order can be cancelled by the client only if it is present, so jumps of CC affect LL only when liquidity is available at that time.
* •

  (At)t≥0(A\_{t})\_{t\geq 0} represents the arrival of new orders and may also be interpreted as the non-instantaneous replenishment of a previously filled limit order. It is modelled as a Poisson process with intensity μ\mu and unit jump size. While, in practice, a new order could arrive while another is still active, such events are sufficiently rare that we restrict arrivals to occur only when no order is currently present. This assumption is consistent with the behaviour of a TWAP placement algorithm.
* •

  (Mt)t≥0(M\_{t})\_{t\geq 0}
  represents the cumulative market orders submitted by the dealer. We assume that these orders occur at jump times, which are 𝔽\mathbb{F}-stopping times {τn}n≥1\{\tau\_{n}\}\_{n\geq 1} controlled by the market maker, and that each transaction is of unit size. Market orders can only occur at times when Lt>0L\_{t}>0, and are zero otherwise. Hence, they are chosen from the class

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝕋={τ:τ​ is an ​𝔽​-stopping time and ​Lτ−≥1}.\mathbb{T}=\left\{\tau:\tau\text{ is an }\mathbb{F}\text{-stopping time and }L\_{\tau-}\geq 1\right\}. |  | (2.5) |

  We then define Mt=∑n≥1𝟙{τn≤t}.M\_{t}=\sum\_{n\geq 1}\mathbbm{1}\_{\{\tau\_{n}\leq t\}}.
* •

  (Rt)t≥0(R\_{t})\_{t\geq 0} represents the replenishment process of an order immediately after the dealer consumes the last unit of liquidity. We assume that Rt=∑n=1∞χn​𝟙{τn≤t}​𝟙{Lτn=0},R\_{t}=\sum\_{n=1}^{\infty}\chi\_{n}\mathbbm{1}\_{\{\tau\_{n}\leq t\}}\mathbbm{1}\_{\{L\_{\tau\_{n}}=0\}},
  where (χn)n≥1(\chi\_{n})\_{n\geq 1} is a sequence of i.i.d. Bernoulli random variables with parameter p∈[0,1]p\in[0,1]. Replenishment typically occurs when an internal exchange order is part of a larger iceberg order.

The pricing offset of the internal exchange order relative to the mid-price is denoted by the parameter ρ\rho, which can be positive or negative. The price at which the market maker can trade is given by,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pt={St+ρ if ​Lt>0∞ if ​Lt≤0.P\_{t}=\begin{dcases}S\_{t}+\rho&\text{ if }L\_{t}>0\\ \infty&\text{ if }L\_{t}\leq 0.\end{dcases} |  | (2.6) |

The dealer receives an infinitely unfavorable price when trading is impossible. In practice, internal exchange orders may yield a small fee for the client. From the modeling perspective this can be incorporated by letting ρ=ρ~−ξ\rho=\tilde{\rho}-\xi, where ρ~\tilde{\rho} is the price offset relative to the mid chosen by the client, and ξ>0\xi>0 is a constant representing the fee per unit. Throughout the paper, we work directly with ρ\rho.

The dealer’s position and cash processes are given by,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qt=∑z∈𝒵z​(Ntb,z−Nta,z)+Mt,Q\_{t}=\sum\_{z\in\mathcal{Z}}z\left(N^{b,z}\_{t}-N^{a,z}\_{t}\right)+M\_{t}, |  | (2.7) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=∑z∈𝒵z​(∫0tSsa,z​𝑑Nsa,z−∫0tSsb,z​𝑑Nsb,z)−∫0tPs​𝑑Ms,X\_{t}=\sum\_{z\in\mathcal{Z}}z\left(\int\_{0}^{t}S^{a,z}\_{s}dN^{a,z}\_{s}-\int\_{0}^{t}S^{b,z}\_{s}dN^{b,z}\_{s}\right)-\int\_{0}^{t}P\_{s}dM\_{s}, |  | (2.8) |

respectively. The value function of the maker maker is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,s,q,x,l)=supδb,δa,(τn)n≥1𝔼​[XT+QT​ST−α​QT2−ϕ​∫tTQs2​𝑑s−ψ​∫tT(Ls)+​𝑑s|ℱt],\begin{split}v(t,s,q,x,l)=\sup\_{\delta^{b},\delta^{a},(\tau\_{n})\_{n\geq 1}}\mathbb{E}\Bigg[X\_{T}+Q\_{T}S\_{T}-\alpha Q^{2}\_{T}-\phi\int\_{t}^{T}Q^{2}\_{s}ds-\psi\int\_{t}^{T}(L\_{s})^{+}ds\bigg|\,\mathcal{F}\_{t}\Bigg],\end{split} |  | (2.9) |

were the supremum is taken over δb,δa∈𝒟\delta^{b},\delta^{a}\in\mathcal{D} and τn∈𝕋\tau\_{n}\in\mathbb{T} (see ([2.2](https://arxiv.org/html/2512.04603v1#S2.E2 "In 2 The model ‣ FX Market Making with Internal Liquidity")) and ([2.5](https://arxiv.org/html/2512.04603v1#S2.E5 "In 3rd item ‣ 2 The model ‣ FX Market Making with Internal Liquidity"))). The constants α,ϕ,ψ\alpha,\phi,\psi are nonnegative and (⋅)+(\cdot)^{+} is the positive part function. The first two terms on the right-hand side of ([2.9](https://arxiv.org/html/2512.04603v1#S2.E9 "In 2 The model ‣ FX Market Making with Internal Liquidity")) represent the terminal value of the market maker’s portfolio; that is, the cash position plus the risky asset position valued at mid. The third and fourth terms implement penalties on the terminal and running positions respectively. The fifth term implements a running penalty on unfilled internal exchange orders.

Using the mathematical argument in [[14](https://arxiv.org/html/2512.04603v1#bib.bib14), Chapter 11,Theorem 11.1], the dynamic programming principle yields that the value function vv satisfies the following Hamilton-Jacobi-Bellman quasi-variational inequality (HJBQVI),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 0=max{∂v∂t(t,s,q,x,l)+σ22∂2v∂s2(t,s,q,x,l)−ϕq2−ψ⋅(l)+\displaystyle 0=\max\Bigg\{\frac{\partial v}{\partial t}(t,s,q,x,l)+\frac{\sigma^{2}}{2}\frac{\partial^{2}v}{\partial s^{2}}(t,s,q,x,l)-\phi q^{2}-\psi\cdot(l)^{+} |  | (2.10) |
|  |  | +∑z∈𝒵,i∈{b,a}(supδi,z​(λi,z​e−κz​δi,z​(v​(t,s,q±z,x−z​s+z​δi,z,l)−v​(t,s,q,x,l))))\displaystyle\quad+\sum\_{z\in\mathcal{Z},i\in\{b,a\}}\left(\underset{\delta^{i,z}}{\sup}\left(\lambda^{i,z}e^{-\kappa^{z}\delta^{i,z}}\left(v(t,s,q\pm z,x-zs+z\delta^{i,z},l)-v(t,s,q,x,l)\right)\right)\right) |  |
|  |  | +ν​(v​(t,s,q,x,l−ℓ¯)−v​(t,s,q,x,l))​𝟙{l>0}+μ​(v​(t,s,q,x,l+ℓ¯)−v​(t,s,q,x,l))​𝟙{l≤0},\displaystyle\quad+\nu\left(v(t,s,q,x,l-\overline{\ell})-v(t,s,q,x,l)\right)\mathbbm{1}\_{\{l>0\}}+\mu\left(v(t,s,q,x,l+\overline{\ell})-v(t,s,q,x,l)\right)\mathbbm{1}\_{\{l\leq 0\}}\mathbf{,} |  |
|  |  | 𝟙{l>1}​(v​(t,s,q+1,x−s−ρ,l−1))\displaystyle\qquad\mathbbm{1}\_{\{l>1\}}\left(v(t,s,q+1,x-s-\rho,l-1)\right) |  |
|  |  | +𝟙{l≤1}(pv(t,s,q+1,x−s−(ρ𝟙{l>0}+∞𝟙{l≤0}),l−1+ℓ¯)\displaystyle\quad+\mathbbm{1}\_{\{l\leq 1\}}\big(p\,v\left(t,s,q+1,x-s-(\rho\mathbbm{1}\_{\{l>0\}}+\infty\mathbbm{1}\_{\{l\leq 0\}}),l-1+\overline{\ell}\right) |  |
|  |  | +(1−p)v(t,s,q+1,x−s−(ρ𝟙{l>0}+∞𝟙{l≤0}),l−1))−v(t,s,q,x,l)},\displaystyle\qquad\quad+(1-p)\,v\left(t,s,q+1,x-s-(\rho\mathbbm{1}\_{\{l>0\}}+\infty\mathbbm{1}\_{\{l\leq 0\}}),l-1\right)\big)-v(t,s,q,x,l)\Bigg\}, |  |

with terminal condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(T,s,q,x,l)=x+q​s−α​q2.v(T,s,q,x,l)=x+qs-\alpha q^{2}. |  | (2.11) |

The terms on the first argument of the maximum in ([2.9](https://arxiv.org/html/2512.04603v1#S2.E9 "In 2 The model ‣ FX Market Making with Internal Liquidity")) arise from Itô’s formula for jump diffusions. The second part of the maximum relates to times where an internal exchange order is traded. In particular, when there is no internal exchange standing liquidity, this term evaluates to −∞-\infty and thus the first part of the maximum is larger. The ±\pm sign in ([2.10](https://arxiv.org/html/2512.04603v1#S2.E10 "In 2 The model ‣ FX Market Making with Internal Liquidity")) relates to terms indexed by bb (aa) having a plus (minus) sign, respectively.
By using the ansatz

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,s,q,x,l)=x+q​s+h​(t,q,l),v(t,s,q,x,l)=x+qs+h(t,q,l), |  | (2.12) |

we can reduce the dimension of ([2.10](https://arxiv.org/html/2512.04603v1#S2.E10 "In 2 The model ‣ FX Market Making with Internal Liquidity")). Solving the Hamiltonians in feedback form then yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=max{∂h∂t​(t,q,l)−ϕ​q2−ψ⋅(l)++∑z∈𝒵,i∈{b,a}(z​λi,z​e−1κz​exp⁡(κzz​(h​(t,q±z,l)−h​(t,q,l))))+ν​(h​(t,q,l−ℓ¯)−h​(t,q,l))​𝟙{l>0}+μ​(h​(t,q,l+ℓ¯)−h​(t,q,l))​𝟙{l≤0},(p​h​(t,q+1,l−1+ℓ¯)+(1−p)​h​(t,q+1,l−1))​𝟙{l≤1}+h(t,q+1,l−1)𝟙{l>1}−h(t,q,l)−(ρ𝟙{l>0}+∞𝟙{l≤0})}\begin{split}0=\max\Bigg\{&\frac{\partial h}{\partial t}(t,q,l)-\phi q^{2}-\psi\cdot(l)^{+}\\ &+\sum\_{z\in\mathcal{Z},i\in\{b,a\}}\left(\frac{z\lambda^{i,z}e^{-1}}{\kappa^{z}}\exp\left(\frac{\kappa^{z}}{z}\left(h(t,q\pm z,l)-h(t,q,l)\right)\right)\right)\\ &+\nu\left(h(t,q,l-\overline{\ell})-h(t,q,l)\right)\mathbbm{1}\_{\{l>0\}}+\mu\left(h(t,q,l+\overline{\ell})-h(t,q,l)\right)\mathbbm{1}\_{\{l\leq 0\}},\\ &\left(p\,h(t,q+1,l-1+\overline{\ell})+(1-p)\,h(t,q+1,l-1)\right)\mathbbm{1}\_{\{l\leq 1\}}\\ &+h(t,q+1,l-1)\mathbbm{1}\_{\{l>1\}}-h(t,q,l)-\left(\rho\mathbbm{1}\_{\{l>0\}}+\infty\mathbbm{1}\_{\{l\leq 0\}}\right)\Bigg\}\end{split} |  | (2.13) |

with terminal condition h​(T,q,l)=−α​q2h(T,q,l)=-\alpha q^{2}.
The optimal depths are given by,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | δi,z​(t,q,l)=1κz+1z​(h​(t,q,l)−h​(t,q±z,l)), for ​i∈{b,a},\displaystyle\delta^{i,z}(t,q,l)=\frac{1}{\kappa^{z}}+\frac{1}{z}\left(h(t,q,l)-h(t,q\pm z,l)\right),\qquad\text{ for }i\in\{b,a\}, |  | (2.14) |

and the optimal execution times (τn)n≥0(\tau\_{n})\_{n\geq 0} are the times such that the maximum in ([2.13](https://arxiv.org/html/2512.04603v1#S2.E13 "In 2 The model ‣ FX Market Making with Internal Liquidity")) evaluates as the second term. We refer to the subspace where this holds as the execution region.

## 3 Optimal strategy

In this section, we investigate the behaviour of the optimal strategy obtained by numerically solving ([2.13](https://arxiv.org/html/2512.04603v1#S2.E13 "In 2 The model ‣ FX Market Making with Internal Liquidity")) using a backward Euler scheme.
An anonymised subsample of HSBC GBPUSD trade data was used to calibrate the intensities λa,z\lambda^{a,z} and λb,z\lambda^{b,z}, as well as the sensitivity of fill probabilities to quotes, κz\kappa^{z}, for z∈𝒵={1,5,10}z\in\mathcal{Z}=\{1,5,10\}.
Specifically, we set κ1=1.5\kappa^{1}=1.5, κ5=1.0\kappa^{5}=1.0, κ10=0.5\kappa^{10}=0.5, λb,1=λa,1=0.2\lambda^{b,1}=\lambda^{a,1}=0.2, λb,5=λa,5=0.005\lambda^{b,5}=\lambda^{a,5}=0.005, and λb,10=λa,10=0.001\lambda^{b,10}=\lambda^{a,10}=0.001.
Each κ\kappa is measured in bps-1, and each λa,z\lambda^{a,z}, λb,z\lambda^{b,z} in seconds-1.
The inventory penalties are given by ϕ=α=0.001\phi=\alpha=0.001, and the penalty for unfilled internal exchange orders is ψ=0.01\psi=0.01.
The time horizon is T=300T=300 seconds, which represents a reasonable high-frequency risk management period.
We consider a range of client prices ρ~\tilde{\rho} and three parameter configurations for ([2.4](https://arxiv.org/html/2512.04603v1#S2.E4 "In 2 The model ‣ FX Market Making with Internal Liquidity")) corresponding to different client algos.

* •

  Iceberg. The client executes without interruption, but the total size of the order is never visible. As such, when the order is filled by the market maker, it is immediately replenished. At some point, the client finishes executing, and the order is no longer renewed. To represent this, the replenishment probability is set to p=0.9p=0.9, meaning there is a 10% chance that, after liquidity is taken, it is not renewed. Additionally, there is a small probability that the order is spontaneously cancelled by the client, given by ν=0.001\nu=0.001 s-1. For simplicity, we do not allow new orders after the iceberg order finishes executing, so μ=0\mu=0. We let the order size be one million notional, and therefore set ℓ¯=1\overline{\ell}=1.
* •

  TWAP. The client executes at a constant pace, but orders arrive with pauses of random lengths from the perspective of the market maker. There is no instantaneous replenishment, so we set p=0p=0. The arrival process AA represents the renewal of the order some time after it has been consumed, and we set its intensity to μ=0.05\mu=0.05 s-1. As in the case of the iceberg strategy, we let ν=0.001\nu=0.001 s-1 and ℓ¯=1\overline{\ell}=1.
* •

  Full Amount. The client places their entire order at once and never updates it, except for the possibility of cancellation. Therefore, there is no instantaneous replenishment (p=0p=0) and no arrivals (μ=0\mu=0). However, the initial order size is larger than one, and we set ℓ¯=10\overline{\ell}=10. As before, the cancellation rate is ν=0.001\nu=0.001 s-1.

### 3.1 Optimal quotes

In Figure [1](https://arxiv.org/html/2512.04603v1#S3.F1 "Figure 1 ‣ 3.1 Optimal quotes ‣ 3 Optimal strategy ‣ FX Market Making with Internal Liquidity") we plot the optimal bid-depths δb,z\delta^{b,z} and ask-depths δa,z\delta^{a,z} at t=0t=0 for z∈𝒵z\in\mathcal{Z} for different inventory positions of the market maker, in the case where client orders are placed at mid price (ρ~=0\tilde{\rho}=0). We chose the snapshot at t=0t=0 as the strategy is approximately stationary away form the terminal time TT.

![Refer to caption](figures/iceberg_deltas_vs_q.png)

![Refer to caption](figures/TWAP_deltas_vs_q.png)

Figure 1: Ask and bid depths, δb,z​(0,q,1)\delta^{b,z}(0,q,1) and δa,z​(0,q,1)\delta^{a,z}(0,q,1), when an internal exchange order is present (dashed lines), and when it is not (solid lines), for z∈𝒵z\in\mathcal{Z}, in the presence of an iceberg (left) and TWAP (right) client algorithm in the internal exchange.
Bid (ask) depths are shown in blue (red), with lighter shades corresponding to larger values of zz.
Dashed lines corresponding to cases where the internal exchange order is available are shown only for values of qq outside the execution region, where the internal exchange order is taken.
The area to the left of the green line indicates the region where the market maker trades with the internal exchange.

We observe in Figure [1](https://arxiv.org/html/2512.04603v1#S3.F1 "Figure 1 ‣ 3.1 Optimal quotes ‣ 3 Optimal strategy ‣ FX Market Making with Internal Liquidity") (left panel) that, in the iceberg scenario, the ask-side quotes are lower near the execution region (i.e., when the market maker has a short position greater than one unit, q<−1q<-1) and the limit order is present (dashed lines), compared with the classical Avellaneda-Stoikov benchmark (solid lines). This occurs because the market maker is more willing to accumulate inventory, given the possibility of closing the position through the limit order if necessary. The effect becomes more pronounced with larger ask sizes and weaker with larger bid sizes, forming a substantial passive impact on both bid and ask prices. In contrast, this effect is marginal in the presence of a TWAP order due to the time intervals between successive renewals of the client’s orders (see right panel).

In Figure [2](https://arxiv.org/html/2512.04603v1#S3.F2 "Figure 2 ‣ 3.1 Optimal quotes ‣ 3 Optimal strategy ‣ FX Market Making with Internal Liquidity"), we show the full (one-time) client order scenario for an outstanding order of 10 units (left) and one unit remaining (right). Prices adjust much more relative to the no-internal-order case when the order is full at L=10L=10, since greater available liquidity allows larger positions to be closed internally.
Note that the trading region here is now q<5q<5 due to the fact that the order will not repeat itself and the market maker can mitigate the internal execution urgency term (the fifth term on the right-hand side of ([2.9](https://arxiv.org/html/2512.04603v1#S2.E9 "In 2 The model ‣ FX Market Making with Internal Liquidity"))) by taking the liquidity. This happens both when L=10L=10 and L=1L=1 due to the linearity of the penalty for positive LL.

We therefore conclude that the type and magnitude of order determines the extent of price adjustment due to internal exchange orders, which can be perceived externally as passive price impact. The pricing adjustments are more pronounced when the expected remaining liquidity on the internal exchange is high.
Since clients rarely disclose their trading strategies, a data-driven approach may be needed to infer internal order properties and decide on external price adjustments, initially assuming a standalone order and updating quotes after the first fill.

![Refer to caption](figures/FA_deltas_vs_q_10.png)

![Refer to caption](figures/FA_deltas_vs_q_1.png)

Figure 2: Ask and bid depths when then internal exchange order is present as in Figure [1](https://arxiv.org/html/2512.04603v1#S3.F1 "Figure 1 ‣ 3.1 Optimal quotes ‣ 3 Optimal strategy ‣ FX Market Making with Internal Liquidity"), now for when the internal exchange order is of full amount type with 10 (left) and 1 (right) units remaining.

### 3.2 When to trade with the internal exchange

In Figure [1](https://arxiv.org/html/2512.04603v1#S3.F1 "Figure 1 ‣ 3.1 Optimal quotes ‣ 3 Optimal strategy ‣ FX Market Making with Internal Liquidity"), we observed that, for the chosen parameters, it was optimal to trade with the internal exchange whenever the position was negative in the TWAP case, and when the position was sufficiently negative in the iceberg case. In contrast, in Figure [2](https://arxiv.org/html/2512.04603v1#S3.F2 "Figure 2 ‣ 3.1 Optimal quotes ‣ 3 Optimal strategy ‣ FX Market Making with Internal Liquidity"), it was optimal to trade when the position was already positive. This indicates that the optimal execution boundary depends on the model parameters. Figure [3](https://arxiv.org/html/2512.04603v1#S3.F3 "Figure 3 ‣ 3.2 When to trade with the internal exchange ‣ 3 Optimal strategy ‣ FX Market Making with Internal Liquidity") illustrates how this boundary changes with the client’s price ρ\rho in the iceberg and TWAP cases. Recall that, in this section, there is no fee (ξ=0\xi=0), so ρ=ρ~\rho=\tilde{\rho}.

We observe that when the client posts aggressively, with a price below the mid (ρ~<0\tilde{\rho}<0), the market maker may be willing to trade with the internal exchange order even if doing so worsens their position (a behaviour known as risk increasing). This pattern reflects a trade-off between optimising P&L, managing inventory costs, and accommodating the urgency of executing internal orders (as described below ([2.9](https://arxiv.org/html/2512.04603v1#S2.E9 "In 2 The model ‣ FX Market Making with Internal Liquidity"))). Owing to the quadratic inventory risk term, holding a small position is penalised less per unit than holding a large one; hence, the market maker may prefer to hold a small negative position rather than always remain non-negative when ρ~\tilde{\rho} is large.

One of the main conclusions from Figure [3](https://arxiv.org/html/2512.04603v1#S3.F3 "Figure 3 ‣ 3.2 When to trade with the internal exchange ‣ 3 Optimal strategy ‣ FX Market Making with Internal Liquidity") is that clients can expect the time required to fill their orders to be more sensitive to their price offset from the mid when using a TWAP strategy than when using an iceberg order. We demonstrate this result quantitatively in Table [2](https://arxiv.org/html/2512.04603v1#S4.T2 "Table 2 ‣ 4 Naïve benchmark and performance comparison ‣ FX Market Making with Internal Liquidity") in Section [4](https://arxiv.org/html/2512.04603v1#S4 "4 Naïve benchmark and performance comparison ‣ FX Market Making with Internal Liquidity"). The main reason for the difference in trading regions between the iceberg and TWAP scenarios for aggressive client orders (ρ~<0\tilde{\rho}<0) is that, at these prices, iceberg orders effectively represent a batch of existing orders that the market maker can use to make an immediate profit and to close a short position when needed. Therefore, the market maker tends to postpone consuming them until holding a sufficiently negative inventory. In contrast, TWAP orders arrive at an exponential rate and are only placed when there are no outstanding client orders. Hence, it is more profitable to consume them immediately regardless of inventory, as otherwise new orders will not arrive.

![Refer to caption](figures/execution_boundaries_rho.png)


Figure 3: The largest position at which it is optimal to fill the internal exchange order vs. as the client’s price offset ρ~\tilde{\rho}. The blue line illustrates the iceberg order scenario, while the orange line shows TWAP case.

## 4 Naïve benchmark and performance comparison

In this section, we compare the performance and behaviour of the optimal strategy obtained by solving the HJBQVI ([2.13](https://arxiv.org/html/2512.04603v1#S2.E13 "In 2 The model ‣ FX Market Making with Internal Liquidity")) and using the optimal depths ([2.14](https://arxiv.org/html/2512.04603v1#S2.E14 "In 2 The model ‣ FX Market Making with Internal Liquidity")), with common heuristic benchmark strategies. We use the same parameters as in Section [3](https://arxiv.org/html/2512.04603v1#S3 "3 Optimal strategy ‣ FX Market Making with Internal Liquidity"). Moreover, due to the 24-hour nature of the FX market, we evaluate the optimal strategy at time t=0t=0 to neglect terminal inventory constraints in our comparison. This assumption is justified, as the strategy becomes time-independent when sufficiently far from the end of the time horizon. The following algorithm describes the naïve benchmark strategy.

Algorithm 1  Naïve benchmark strategy

Initiate Set t=0t=0 and L0=ℓ¯≥0L\_{0}=\bar{\ell}\geq 0 in ([2.4](https://arxiv.org/html/2512.04603v1#S2.E4 "In 2 The model ‣ FX Market Making with Internal Liquidity")).

while t≤Tt\leq T do

if the available liquidity Lt≤0L\_{t}\leq 0 then

Use Avellaneda–Stoikov quotes (i.e. ([2.3](https://arxiv.org/html/2512.04603v1#S2.E3 "In 2 The model ‣ FX Market Making with Internal Liquidity")) at time zero with L≡0L\equiv 0),

else

if Qt<0Q\_{t}<0 then

Purchase the internal exchange outstanding order and update Lt+Δ←Lt−1L\_{t+\Delta}\leftarrow L\_{t}-1

else

Use Avellaneda-Stoikov bid quotes and adjusted ask quotes in ([4.2](https://arxiv.org/html/2512.04603v1#S4.E2 "In 4 Naïve benchmark and performance comparison ‣ FX Market Making with Internal Liquidity")).

Set t←t+Δt\leftarrow t+\Delta.

In Algorithm [1](https://arxiv.org/html/2512.04603v1#alg1 "Algorithm 1 ‣ 4 Naïve benchmark and performance comparison ‣ FX Market Making with Internal Liquidity") when the market maker’s position is negative and an internal exchange order is present, it is filled111In reality, this may depend on the client’s posted price ρ~\tilde{\rho}; however, this is reasonable for aggressive and mildly passive pricing.. If no such order exists, prices are set using the Avellaneda-Stoikov model, that is the case when there is no internal exchange (L≡0L\equiv 0). Prices on the ask side are adjusted according to a hubristic rule which is described below.

We let δa,zk,A​S​(0,q)\delta^{a,z\_{k},AS}(0,q) denote the optimal half-spreads at t=0t=0 in the Avellaneda–Stoikov model, i.e., those corresponding to our model with L≡0L\equiv 0 and allowing for multiple order sizes (see [[7](https://arxiv.org/html/2512.04603v1#bib.bib7)]).
In the presence of a client’s sell order of size ll at a price ρ~\tilde{\rho} above the mid-price, the market maker inserts an order on the ask side of their pricing ladder with size ll at a price ρ~+ι\tilde{\rho}+\iota above mid, where ι>0\iota>0 is the margin introduced by the dealer. We then compute a new volume-weighted average price (VWAP) to obtain the naïve strategy’s half-spreads.

Let the order sizes z1<z2,…z\_{1}<z\_{2},... and let zi=min⁡{z∈𝒵:ρ~+ι<δa,z,A​S​(0,q)}z\_{i}=\min\{z\in\mathcal{Z}:\tilde{\rho}+\iota<\delta^{a,z,AS}(0,q)\}. The naïve strategy’s half-spreads when there is an order on the internal exchange are then given by
δ~a,zj,B​M​(0,q,l)=δa,zj,A​S​(0,q)\tilde{\delta}^{a,z\_{j},BM}(0,q,l)=\delta^{a,z\_{j},AS}(0,q) if δa,zj,A​S​(0,q)<ρ~+ι\delta^{a,z\_{j},AS}(0,q)<\tilde{\rho}+\iota, which is when j<ij<i, and for j≥ij\geq i,

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ~a,zj,B​M​(0,q,l)=1zj(l(ρ~+ι)+zi−1δa,zi−1,A​S(t,q)++l​∑r=i+1j((zr−1​δa,zr−1,A​S​(t,q)−zr−2​δa,zr−2,A​S​(t,q)zr−1−zr−2))+∑r=ij((zr−zr−1−l)(zr​δa,zr,A​S​(t,q)−zr−1​δa,zr−1,A​S​(t,q)zr−zr−1)))\begin{split}\tilde{\delta}^{a,z\_{j},BM}(0,q,l)=&\frac{1}{z\_{j}}\Bigg(l\left(\tilde{\rho}+\iota\right)+z\_{i-1}\delta^{a,z\_{i-1},AS}(t,q)+\\ &\qquad+l\sum\_{r=i+1}^{j}\left(\left(\frac{z\_{r-1}\delta^{a,z\_{r-1},AS}(t,q)-z\_{r-2}\delta^{a,z\_{r-2},AS}(t,q)}{z\_{r-1}-z\_{r-2}}\right)\right)\\ &\qquad+\sum\_{r=i}^{j}\left(\left(z\_{r}-z\_{r-1}-l\right)\left(\frac{z\_{r}\delta^{a,z\_{r},AS}(t,q)-z\_{r-1}\delta^{a,z\_{r-1},AS}(t,q)}{z\_{r}-z\_{r-1}}\right)\right)\Bigg)\end{split} |  | (4.1) |

To summarise, the prices quoted by the market maker are,

|  |  |  |  |
| --- | --- | --- | --- |
|  | δa,zj,B​M​(0,q,l)={δ~a,zj,B​M​(0,q,l) if ​l>0,δa,zj,A​S​(0,q) if ​l≤0.\delta^{a,z\_{j},BM}(0,q,l)=\begin{dcases}\tilde{\delta}^{a,z\_{j},BM}(0,q,l)&\text{ if }l>0,\\ \delta^{a,z\_{j},AS}(0,q)&\text{ if }l\leq 0.\end{dcases} |  | (4.2) |

The prices on the bid-side remain unchanged in the presence of the client’s order, that is δa,zj,B​M​(0,q,l)=δa,zj,A​S​(0,q)\delta^{a,z\_{j},BM}(0,q,l)=\delta^{a,z\_{j},AS}(0,q) (see Algorithm [1](https://arxiv.org/html/2512.04603v1#alg1 "Algorithm 1 ‣ 4 Naïve benchmark and performance comparison ‣ FX Market Making with Internal Liquidity")).222Alternatively, one can consider removing equivalent size from the bid ladder.

In Table [1](https://arxiv.org/html/2512.04603v1#S4.T1 "Table 1 ‣ 4 Naïve benchmark and performance comparison ‣ FX Market Making with Internal Liquidity"), we compare the mean and standard deviation of the simulated P&L, defined as P&L=XT+QT​STP\&L=X\_{T}+Q\_{T}S\_{T} (see ([2.9](https://arxiv.org/html/2512.04603v1#S2.E9 "In 2 The model ‣ FX Market Making with Internal Liquidity"))), across different types of client orders and client pricing levels: aggressive (ρ=−0.2\rho=-0.2), mid (ρ=0\rho=0), and passive (ρ=0.2\rho=0.2). In all cases, the market maker’s initial position is zero, fees are set to ξ=0\xi=0, the time step is Δ=0.3\Delta=0.3 s, the time horizon is T=300T=300 seconds, and the number of simulated trajectories is 5,0005{,}000. We compare the performance of the optimal strategy with that of the naïve benchmark strategy using a margin of ι=0.1\iota=0.1.
We observe that the optimal strategy consistently outperforms the naïve benchmark, and that the market maker’s profits are slightly more sensitive to the client’s pricing offset ρ~\tilde{\rho} in the TWAP and full-amount cases than in the iceberg case.

In Table [2](https://arxiv.org/html/2512.04603v1#S4.T2 "Table 2 ‣ 4 Naïve benchmark and performance comparison ‣ FX Market Making with Internal Liquidity"), we observe that the expected first fill times of internal client orders under the naïve benchmark strategy are generally shorter than those under the optimal strategy. This results from the naïve strategy’s more aggressive pricing adjustments and its execution rule of always taking when the inventory is negative. In particular, the market maker readily goes short and therefore fills internal exchange orders more frequently.
We also observe that the change in the mean time to first fill under the optimal strategy is more sensitive to the client’s pricing offset ρ~\tilde{\rho} when a TWAP order is used than when an iceberg order is used. Finally, when a full-amount order is used, the time to first fill is always zero under the optimal strategy, as the initial position of zero lies within the region where the market maker trades with the internal exchange (see Figure [2](https://arxiv.org/html/2512.04603v1#S3.F2 "Figure 2 ‣ 3.1 Optimal quotes ‣ 3 Optimal strategy ‣ FX Market Making with Internal Liquidity")).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| P&L (K$) | | | | |
|  |  | Aggressive: ρ=−0.2\rho=-0.2 | At mid: ρ=0\rho=0 | Passive: ρ=0.2\rho=0.2 |
| Iceberg | Optimal | 3.788 (1.62) | 3.677 (1.6) | 3.603 (1.6) |
| Naïve | 3.384 (1.69) | 3.36 (1.69) | 3.347 (1.69) |
| TWAP | Optimal | 3.84 (1.65) | 3.708 (1.61) | 3.673 (1.59) |
| Naïve | 3.381 (1.5) | 3.399 (1.53) | 3.405 (1.56) |
| FA | Optimal | 3.744 (2.0) | 3.547 (2.0) | 3.354 (2.0) |
| Naïve | 3.452 (1.6) | 3.433 (1.58) | 3.404 (1.57) |

Table 1: Mean (standard deviation) of P&L in thousand $, in the presence of different client algos with passive, at mid, and aggressive placement for iceberg, TWAP and full amount (FA) scenarios.



|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Time to First Fill (seconds) | | | | |
|  |  | Aggressive: ρ=−0.2\rho=-0.2 | At mid: ρ=0\rho=0 | Passive: ρ=0.2\rho=0.2 |
| Iceberg | Optimal | 21.133 (31.57) | 47.965 (53.67) | 56.681 (63.16) |
| Naïve | 5.147 (6.5) | 7.59 (10.36) | 12.145 (18.64) |
| TWAP | Optimal | Always zero | 24.518 (34.69) | 68.221 (68.3) |
| Naïve | 5.571 (7.7) | 7.797 (10.24) | 12.507 (18.12) |
| FA | Optimal | Always zero | Always zero | Always zero |
| Naïve | 5.309 (6.7) | 7.402 (9.82) | 12.063 (17.34) |

Table 2: Mean (standard deviation) of time to fill for the first internal exchange order in seconds, in the presence of different client algos with passive, at mid, and aggressive placement for iceberg, TWAP and full amount (FA) scenarios.

Although execution times under the optimal strategy are slower than those of the naïve strategy, the latter substantially reduces the market maker’s P&L. To sustain internal flow without harming performance, an additional compensation mechanism is required.
Figure [4](https://arxiv.org/html/2512.04603v1#S4.F4 "Figure 4 ‣ 4 Naïve benchmark and performance comparison ‣ FX Market Making with Internal Liquidity") shows the impact of fees ξ\xi and margins ι\iota on P&L (left) and fill rate (right). Margins are the least effective option: while they improve the naïve strategy’s P&L similarly to fees, they also reduce the volume of internal exchange executions. Fully compensating the naïve strategy would require a large fee, which could in practice discourage internal exchange participation, an effect not captured by the model.
In contrast, the optimal strategy benefits from fees, improving both P&L and turnover.

![Refer to caption](figures/pnl_fee_margin.png)

![Refer to caption](figures/volume_fee_margin.png)

Figure 4: 
P&L (left) and internal exchange volume per second MTT\frac{M\_{T}}{T} (right) for optimal market maker’s strategy (blue) and naïve benchmark strategy (red) in the presence of an iceberg as functions of fee (solid lines) or margin (dashed lines). Reference P&L using Avellaneda-Stoikov pricing without an internal exchange is shown for comparison (orange).

## 5 Conclusion

We have introduced a model in which a market maker continuously streams prices to clients while also having the option to take liquidity from dynamic passive orders on an internal exchange. We solve for the optimal strategy using an HJBQVI and demonstrate its superior performance compared to a heuristic benchmark strategy that directly incorporates internal exchange orders into the OTC pricing ladder.

The optimal strategy defines an inventory-dependent execution threshold beyond which the market maker is willing to immediately take the internal exchange order. Otherwise, the market maker skews prices to facilitate the opposing flow. The degree of skew and the positioning of the execution threshold depend on the market maker’s risk aversion, client order depth and placement strategy, as well as on flow facilitation initiatives.

Notably, the skew mechanism revealed in our analysis highlights a potential origin of passive market impact: clients place passive orders on the internal exchange, prompting the market maker to skew prices for their OTC clients. As described in [[10](https://arxiv.org/html/2512.04603v1#bib.bib10)], these clients may then extract alpha from the resulting skew, leading the market to move.

## Acknowledgments

The views expressed are those of the authors and do not necessarily reflect the views and practices at HSBC.
The authors are grateful to Richard Anthony (HSBC) for helpful discussions and support throughout the project.

## References

* Cartea et al. [2014]

  Á.  Cartea, S.  Jaimungal, and J.  Ricci.
  Buy Low Sell High: A High Frequency Trading Perspective.
  *SIAM J. Financ. Math.*, 5(1):415–444, 2014
* Cartea and Jaimungal [2015]

  Á.  Cartea, and S.  Jaimungal.
  Optimal Execution with Limit and Market Orders.
  *Quant Finance.*, 15(8):1279–1291, 2015.
* Morimoto [2024]

  Y.  Morimoto.
  Optimal Execution Strategies Incorporating Internal Liquidity Through Market Making.
  Preprint, available at SSRN:5074405, 2024.
* Cartea and Sánchez-Betancourt [2025]

  Á.  Cartea, and L.  Sánchez-Betancourt.
  Brokers and informed traders: dealing with toxic flow and extracting trading signals.
  *SIAM J. Financ. Math.*, 16(2):243–270 2025
* Barzykin et al. [2023]

  A. Barzykin, P. Bergault, and O. Guéant.
  Algorithmic market making in dealer markets with hedging and market
  impact.
  *Mathematical Finance*, 33(1):41–79,
  2024/06/11 2023.
* Butz and Oomen [2019]

  M. Butz and R. Oomen.
  Internalisation by electronic fx spot dealers.
  *Quant Finance.*, 19(1):35–56, 01
  2019.
* Bergault and Guéant [2021]

  P.  Bergault, and O.  Guéant.
  Size matters for OTC market makers: General results and dimensionality reduction techniques
  *Math Financ.*, 31 (1): 279-322., 2021.
* Guéant et al. [2013]

  O.  Guéant, C-A.  Lehalle, and J.  Fernandez-Tapia.
  Dealing with the inventory risk: a solution to the market making problem
  *Math. Financ. Econ.*, 7 (4): 477–507., 2013.
* Chahdi et al. [2024]

  Y.O.  Chahdi, M.  Rosenbaum, G.  Szymanski.
  A theory of passive market impact
  Preprint, available at arXiv:2412.07461, 2024.
* Barzykin et al. [2025]

  A. Barzykin, P. Bergault, O.  Guéant, and M. Lemmel.
  Optimal Quoting under Adverse Selection and Price Reading
  Preprint, available at arXiv:2508.20225, 2025.
* Boyce et al. [2025]

  R. Boyce, M. Herdegen, and L. Sánchez-Betancourt.
  Market making with exogenous competition.
  *SIAM J. Financ. Math.*, 16(2):692–706, 2025.
* Avellaneda and Stoikov [2008]

  M. Avellaneda and S. Stoikov.
  High-frequency trading in a limit order book
  *Quantitative Finance*,
  8(3):217–224, 2008.
* Cartea et al [2015]

  Á. Cartea, S. Jamingual, and J. Penalva.
  Algorithmic and High Frequency Trading
  *Cambridge University Press, Cambridge, United Kingdom, 2015*
  ISBN 9781107091146
* Øksendal and Sulem [2019]

  B. Øksendal, and A. Sulem.
  Applied Stochastic Control of Jump Diffusions
  *Springer, Berlin, Germany, 2019*
  ISBN 3540140239
* [15]


  FXPA Guidance: Definitions & Best Practices for FX Internalisation in Algo Execution
  Published by the Foreign Exchange Professionals Association (FXPA), July 2025.