---
authors:
- Leonardo Baggiani
- Martin Herdegen
- Leandro Sanchez-Betancourt
doc_id: arxiv:2603.09669v1
family_id: arxiv:2603.09669
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Competition between DEXs through Dynamic Fees
url_abs: http://arxiv.org/abs/2603.09669v1
url_html: https://arxiv.org/html/2603.09669v1
venue: arXiv q-fin
version: 1
year: 2026
---


Leonardo Baggiani
Corresponding author: leonardo.baggiani@warwick.ac.ukDepartment of Statistics, University of Warwick
  
Martin Herdegen
Department of Mathematics, University of Stuttgart
  
Leandro Sánchez-Betancourt
Mathematical Institute and Oxford-Man Institute of Quantitative Finance, University of Oxford

###### Abstract

We find an approximate Nash equilibrium to a game between decentralised exchanges (DEXs) that compete for order flow by setting dynamic trading fees. We characterise the equilibrium via a coupled system of partial differential equations and derive tractable, approximate closed-form expressions for the equilibrium fees. Our analysis shows that the two-regime structure found in monopoly models persists under competition: pools alternate between raising fees to deter arbitrage and lowering fees to attract noise trading and increase volatility. Under competition, however, the switching boundary shifts from the oracle price to a weighted average of the oracle and the competitors’ exchange rates. Our numerical experiments show that, holding total liquidity fixed, an increase in the number of competing DEXs reduces execution slippage for strategic liquidity takers and lowers fee revenue per DEX. Finally, the effect on noise traders’ slippage depends on market activity: they are worse off in low-activity markets but better off in high-activity ones.

*Keywords:* decentralized finance, automated market makers, optimal fees, arbitrageurs, noise trading.

  

*Mathematics Subject Classification (2020):* 93E20, 91B70.

*JEL Classification:* C61, G23, D53.

## 1 Introduction

Automated market makers (AMMs) are the dominant trading mechanism within decentralised exchanges (DEXs). As of February 2026, AMM-based DEXs process approximately $6 billion in daily trading volume, accounting for roughly 6.5% of the total DeFi traded volume.111CoinGecko, “Decentralized Exchanges (DEX) by Trading Volume,” <https://www.coingecko.com/en/exchanges/decentralized> (accessed 20 February 2026). In an AMM, liquidity providers are compensated through trading fees paid by liquidity takers. Trading fees play a central role in AMM design and performance. Work such Milionis et al. ([2024](#bib.bib3 "Automated market making and arbitrage profits in the presence of fees"), [2022a](#bib.bib4 "Automated market making and loss-versus-rebalancing"), [2022b](#bib.bib5 "Quantifying loss in automated market makers")) and Bichuch and Feinstein ([2025](#bib.bib8 "The price of liquidity: implied volatility of automated market maker fees")) show that fees are required to compensate liquidity providers for adverse-selection costs such as loss-versus-rebalancing (LVR), i.e., the systematic losses incurred by liquidity providers when arbitrageurs trade against stale pool prices. Moreover, as shown in Hasbrouck et al. ([2022](#bib.bib2 "The need for fees at a dex: how increases in fees can increase dex trading volume")), higher trading fees increase total trading volume by incentivizing liquidity provision, which in turn reduces price impact and makes the venue more attractive to liquidity takers.
  
  
Given the foundational role of trading fees as a core building block of AMMs, it is a natural question to ask: what fee level is optimal from the perspective of a liquidity provider? This question is well posed in light of recent innovations that make fees a configurable choice rather than an exogenous parameter. In particular, with the introduction of Uniswap v4, liquidity providers can deploy and customise their own pools and, through *hooks*, they are able to specify fee designs directly at the smart-contract level, allowing fee schedules that are dynamic and depend on external information, such as the asset’s price on a centralised exchange (e.g., Binance) or the asset price in another liquidity pool.
  
  
There is a growing literature that studies optimal fee setting in automated market makers from the liquidity provider’s perspective. Evans et al. ([2021](#bib.bib6 "Optimal fees for geometric mean market makers")) studies optimal fees in geometric mean market makers. Fritsch ([2021](#bib.bib11 "A note on optimal fees for constant function market makers")) determines optimal fees across multiple pools that compete with each other and relates the fee level to the depth of the pool. He et al. ([2024](#bib.bib7 "Optimal design of automated market makers on decentralized exchanges")) derives an optimal fee for a liquidity provider who decides how to allocate their liquidity between a DEX and a centralised exchange (CEX). 222There are numerous treatments of the CEX-DEX trading problem from the liquidity taker’s perspective; see Cartea et al. ([2023](#bib.bib21 "Execution and statistical arbitrage with signals in multiple automated market makers")); Jaimungal et al. ([2023](#bib.bib24 "Optimal trading in automatic market makers with deep learning")); He et al. ([2025](#bib.bib22 "Arbitrage on decentralized exchanges")); Bergault et al. ([2026](#bib.bib9 "Trading in cexs and dexs with priority fees and stochastic delays")); Capponi et al. ([2026](#bib.bib25 "Optimal trading in automated market makers")). For the liquidity provider’s perspective see Bayraktar et al. ([2024](#bib.bib28 "DEX specs: a mean field approach to defi currency exchanges")) and Drissi et al. ([2025](#bib.bib23 "Equilibrium liquidity and risk offsetting in decentralised markets")). All of these contributions differ from this work in that they consider static fees, whereas here we study the case of dynamic fees.
  
  
Recent work argues that fee schedules should be state-dependent rather than fixed. Cao et al. ([2023](#bib.bib10 "A structural model of automated market making")) develops and estimates a structural model of an AMM and shows that fixed fees are inefficient. Nadkarni et al. ([2024](#bib.bib13 "Adaptive curves for optimally efficient market making")) and Cartea et al. ([2024](#bib.bib26 "Strategic bonding curves in automated market makers")) propose to adapt AMM bonding curves (which is equivalent to setting dynamic fees) deriving a range of an optimal adaptive curves that minimizes arbitrage losses while remaining competitive. Campbell et al. ([2025](#bib.bib12 "Optimal fees for liquidity provision in automated market makers")) studies LP profitability in a dynamic model with a parallel CEX and endogenous order routing, and characterizes the optimal fee as a function of market conditions such as volatility and trading volume, suggesting a threshold-type dynamic fee schedule that is stable in normal conditions and changes with volatility. Finally, Baggiani et al. ([2025](#bib.bib1 "Optimal dynamic fees in automated market makers")) determines optimal dynamic fees in a constant function market maker. They find two distinct regimes (higher fees to deter arbitrageurs and lower fees to attract noise traders), and show that fee rules that are linear in inventory and sensitive to external price changes provide a good approximation to the optimal fee structure.
  
  
In practice, however, liquidity is not monopolised by a single pool. The same pair is typically traded across multiple pools (often across multiple fee tiers or venues), and liquidity takers can route orders to the pool offering the most attractive execution. This introduces a strategic interaction: each pool’s fee decision affects not only its own quoted prices and inventory dynamics, but also the dynamics of the order flow across competing pools.
  
  
In this paper, we build on Baggiani et al. ([2025](#bib.bib1 "Optimal dynamic fees in automated market makers")) to extend the market-making framework of Avellaneda and Stoikov ([2008](#bib.bib14 "High-frequency trading in a limit order book"))333For broader background on market making models we refer to the books of Cartea et al. ([2015](#bib.bib15 "Algorithmic and high-frequency trading")) and Guéant ([2016](#bib.bib16 "The financial mathematics of market liquidity: from optimal execution to market making")). to a multi-agent setting. The goal is that fee setting becomes a competitive interaction with multiple liquidity providers rather than a single-agent control problem. There are a number of papers that are close to this work within a limit order book (LOB) setup. Boyce et al. ([2025](#bib.bib17 "Market making with exogenous competition")) considers a reference market maker facing a parametrized competition and Chilenje et al. ([2025](#bib.bib18 "Market making with competition: a stackelberg equilibrium")) extend their analysis to find the Stackelberg equilibrium. Baldacci et al. ([2023](#bib.bib29 "A mean-field game of market-making against strategic traders")) study a mean field of competing market makers against strategic takers, Guo and Jin ([2025](#bib.bib19 "Macroscopic market making games")) develops a stochastic-game formulation of macroscopic market making with price competition and, Luo and Zheng ([2021](#bib.bib20 "Dynamic equilibrium of market making with price competition")) models market making with price competition and incomplete information as a nonzero-sum stochastic differential game.
  
  
To do this we build a finite-horizon model of fee competition between constant-function market makers (CFMMs) trading the same two assets. Each pool ii chooses two predictable fee processes: a fee for selling the risky asset {𝔭ti}t∈[0,T]\{\mathfrak{p}^{i}\_{t}\}\_{t\in[0,T]}, and a fee for buying it {𝔪ti}t∈[0,T]\{\mathfrak{m}^{i}\_{t}\}\_{t\in[0,T]}; these processes are stochastic and, at any time tt, they may depend on all available information just before time tt. In contrast to the monopoly setting, the feedback representation of optimal fees will no longer be one-dimensional objects because we expect them to depend both on the agent and the competitors inventories (and hence quoted exchange rates). For the case of two venues {a,b}\{a,b\} order flow to venue i∈{a,b}i\in\{a,b\} is driven by two types of traders.
Arbitrageurs become more active when venue ii’s effective quote (with fees) is misaligned with the CEX price and with the other venue’s quote. At the same time, noise traders generate a baseline stream of orders that is largely
unrelated to price dislocations. This structure aims to capture the increased order flow due to CEX–DEX arbitrage and pool mispricing. Each pool maximises expected cumulative fee revenue taking the competitors’ fee policies as given. We characterise an approximate Nash equilibrium via a coupled system of dynamic programming equations on the joint inventory grid and derive equilibrium fee formulae as a generalization of the structure obtained in the monopoly problem.
  
  
Our analysis delivers three main insights. First, the *two-regime* structure of optimal fees persists under competition: pools still alternate between deterring arbitrage and stimulating noise trading. The key difference is that the switching boundary is no longer pinned to the oracle price alone; instead, it shifts to a weighted average of the oracle price and competitors’ exchange rates, reflecting that the relevant “outside option” for a liquidity taker is a combination of external execution and execution in rival pools. Second, equilibrium fees exhibit an approximately linear dependence on both own and rivals’ inventories over economically relevant regions, suggesting that a linear approximation of the fees (which lower the gas cost) remain effective even in multi-venue environments. Third, competition has welfare implications: as the number of competing venues increases, the ability of strategic liquidity takers to route to the best quotes improves, while fee revenues per venue decline and can become too small to justify entry when fixed participation costs are present.
  
  
The remainder of the paper is organised as follows. Section [2](#S2 "2 Two-player model ‣ Competition between DEXs through Dynamic Fees") introduces the two-player model, defines fee-dependent quotes, and specifies the controlled order-flow intensities. Section [3](#S3 "3 Numerical results ‣ Competition between DEXs through Dynamic Fees") presents numerical equilibrium fee schedules and comparative statics in the duopoly. Section [4](#S4 "4 Simulations ‣ Competition between DEXs through Dynamic Fees") studies execution outcomes and revenue comparisons across fee rules and against the monopoly benchmark. For readability the main body develops the mathematics for two players and Appendix [A](#A1 "Appendix A Multiple-player model ‣ Competition between DEXs through Dynamic Fees") extends the framework to MM competing players. Lastly, Appendix [B](#A2 "Appendix B Simulations ‣ Competition between DEXs through Dynamic Fees") reports the corresponding results for the multi-player case.

## 2 Two-player model

We study the problem of two pools competing with each other in a finite horizon T>0T>0. We assume that every pool is a CFMM and trades the same two assets: a riskless asset XX and a risky asset YY. We will denote the two players (pools) as player aa and player bb. For i∈{a,b}i\in\{a,b\}, let (0​p​ti)2(0pt^{i})^{2} denote the depth of pool ii and let fi:ℝ+×ℝ+→ℝ+f^{i}:\mathbb{R}\_{+}\times\mathbb{R}\_{+}\to\mathbb{R}\_{+} be its trading function, with associated level function φi:ℝ+→ℝ+\varphi^{i}:\mathbb{R}\_{+}\to\mathbb{R}\_{+} defined such that fi​(φi​(y),y)=(0​p​ti)2f^{i}(\varphi^{i}(y),y)=(0pt^{i})^{2}. Here, all trading functions are strictly increasing and twice differentiable in both arguments. For each pool we assume that the quantity of asset YY (and consequently of asset XX) takes values in a finite grid given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {yi,−Ni,…,yi,0,…,yi,Ni}i∈{a,b}.\displaystyle\{y^{i,-N^{i}},\dots,y^{i,0},\dots,y^{i,N^{i}}\}\quad\quad i\in\{a,b\}. |  | (2.1) |

Let y¯i:=yi,−Ni\underline{y}^{i}:=y^{i,-N^{i}} and y¯i:=yi,Ni\overline{y}^{i}:=y^{i,N^{i}} be the reserve constraints such that 0<y¯i<yi,0<y¯i<+∞0<\underline{y}^{i}<y^{i,0}<\overline{y}^{i}<+\infty.
Consequently, the quantity of asset XX in the pools takes values in the grid

|  |  |  |
| --- | --- | --- |
|  | {xi,−Ni:=φi​(yi,−Ni),…,xi,0:=φi​(yi,0),…,xi,Ni:=φi​(yi,Ni)}i∈{a,b}.\big\{x^{i,-N^{i}}:=\varphi^{i}(y^{i,-N^{i}}),\dots,x^{i,0}:=\varphi^{i}(y^{i,0}),\dots,x^{i,N^{i}}:=\varphi^{i}(y^{i,N^{i}})\big\}\quad\quad i\in\{a,b\}. |  |

Note that the monotonicity of the grids for the two assets are opposite to each other: the grid for asset YY is increasing, whereas the grid for asset XX is decreasing.
The notation yi,jy^{i,j} refers to the jj-th element of player ii’s grid.

For each pool there are three basic exchange rates to be considered. Let yi,jy^{i,j} denote the quantity of asset YY in the pool i∈{a,b}i\in\{a,b\} before a trade of a liquidity taker, and let φ˙\dot{\varphi} denote the derivative of φ\varphi. We define the following exchange rates.

1. (a)

   The *marginal exchange rate* describes the price of an infinitesimal trade and is given by

   |  |  |  |
   | --- | --- | --- |
   |  | Zi​(yi,j):=−φ˙i​(yi,j)j∈{−Ni,…,Ni}.Z^{i}(y^{i,j}):=-\dot{\varphi}^{i}(y^{i,j})\qquad j\in\{-N^{i},\dots,N^{i}\}. |  |
2. (b)

   The *exchange rate for buying* (taking out asset YY from the pool) Δ−i​(yi,j):=yi,j−yi,j−1\Delta^{i}\_{-}(y^{i,j}):=y^{i,j}-y^{i,j-1} units of asset YY with j∈{−Ni,…,Ni}j\in\{-N^{i},\dots,N^{i}\} is given by

   |  |  |  |
   | --- | --- | --- |
   |  | Z−i​(yi,j):=φi​(yi,j−1)−φi​(yi,j)Δ−i​(yi,j).Z\_{-}^{i}(y^{i,j}):=\frac{\varphi^{i}(y^{i,j-1})-\varphi^{i}(y^{i,j})}{\Delta^{i}\_{-}(y^{i,j})}. |  |

   The quantity Z−i​(yi,j)Z\_{-}^{i}(y^{i,j}) takes values in the grid

   |  |  |  |
   | --- | --- | --- |
   |  | {Z−i,−Ni+1:=Z−i​(yi,−Ni+1),…,Z−i,0:=Z−i​(yi,0),…,Z−i,Ni:=Z−i​(yi,Ni)}.\left\{Z\_{-}^{i,-N^{i}+1}:=Z\_{-}^{i}(y^{i,-N^{i}+1}),\dots,Z\_{-}^{i,0}:=Z\_{-}^{i}(y^{i,0}),\dots,Z\_{-}^{i,N^{i}}:=Z\_{-}^{i}(y^{i,N^{i}})\right\}. |  |
3. (c)

   The *exchange rate for selling* (depositing asset YY in the pool) Δ+i​(yi,j):=yi,j−yi,j+1\Delta^{i}\_{+}(y^{i,j}):=y^{i,j}-y^{i,j+1} units of asset YY with j∈{−Ni,…,Ni}j\in\{-N^{i},\dots,N^{i}\} is given by

   |  |  |  |
   | --- | --- | --- |
   |  | Z+i​(yi,j):=φi​(yi,j)−φi​(yi,j+1)Δ+i​(yi,j).Z\_{+}^{i}(y^{i,j}):=\frac{\varphi^{i}(y^{i,j})-\varphi^{i}(y^{i,j+1})}{\Delta^{i}\_{+}(y^{i,j})}. |  |

   The quantity Z+i​(yi,j)Z\_{+}^{i}(y^{i,j}) takes values in the grid

   |  |  |  |
   | --- | --- | --- |
   |  | {Z+i,−Ni:=Z+i​(yi,−Ni),…,Z+i,0:=Z+i​(yi,0),…,Z+i,Ni−1:=Z+i​(yi,Ni−1)}.\left\{Z\_{+}^{i,-N^{i}}:=Z\_{+}^{i}(y^{i,-N^{i}}),\dots,Z\_{+}^{i,0}:=Z\_{+}^{i}(y^{i,0}),\dots,Z\_{+}^{i,N^{i}-1}:=Z\_{+}^{i}(y^{i,N^{i}-1})\right\}. |  |

For each player, exchange rates for buying and selling satisfy the identity

|  |  |  |
| --- | --- | --- |
|  | Z−i,j=Z+i,j−1,j∈{−Ni+1,…,0,…​Ni},i∈{a,b}.Z\_{-}^{i,j}=Z\_{+}^{i,j-1},\quad j\in\{-N^{i}+1,\dots,0,\dots N^{i}\},\quad\quad\quad i\in\{a,b\}. |  |

The quantities Z+​(y)Z\_{+}(y) and Z−​(y)Z\_{-}(y) represent the bid and ask prices in the limit order book, respectively, while Z​(y)Z(y) denotes the midprice. Thus, we have the ordering

|  |  |  |
| --- | --- | --- |
|  | Z+​(y)<Z​(y)<Z−​(y).Z\_{+}(y)<Z(y)<Z\_{-}(y). |  |

Moreover, as the spread Δ​(y)\Delta(y) tends to zero,

|  |  |  |
| --- | --- | --- |
|  | limΔ​(y)→0Z−​(y)=limΔ​(y)→0Z+​(y)=Z​(y).\lim\_{\Delta(y)\to 0}Z\_{-}(y)=\lim\_{\Delta(y)\to 0}Z\_{+}(y)=Z(y). |  |

We add fees to the trading mechanism, using the functions

|  |  |  |
| --- | --- | --- |
|  | 𝔪i,𝔭i:{yi,−Ni,…,yi,0,…,yi,Ni}×{yj,−Nj,…,yj,0,…,yj,Nj}→ℝ.\mathfrak{m}^{i},\mathfrak{p}^{i}:\{y^{i,-N^{i}},\dots,y^{i,0},\dots,y^{i,N^{i}}\}\times\{y^{j,-N^{j}},\dots,y^{j,0},\dots,y^{j,N^{j}}\}\to\mathbb{R}. |  |

Here, 𝔪\mathfrak{m} denotes the fee for buying while 𝔭\mathfrak{p} the one for selling.
The fees are collected in units of the riskless asset XX and are deposited outside of the pool. The fees depend on inventory and, consequently, on the exchange rates quoted by both players. This contrasts with the monopoly case, where fees are one-dimensional. The associated (fee-dependent) exchange rates are therefore two-dimensional and are described as follows. Let yi,hy^{i,h} and yj,sy^{j,s} denote the quantities of asset YY in pools ii and jj, respectively, immediately before a trade.

1. (a)

   If h−1≥−Nih-1\geq-N^{i}, the *exchange rate with fee structure 𝔪i\mathfrak{m}^{i} for buying* (taking out asset YY from the pool) Δ−i​(yi,h):=yi,h−yi,h−1\Delta^{i}\_{-}(y^{i,h}):=y^{i,h}-y^{i,h-1} units of asset YY is given by

   |  |  |  |
   | --- | --- | --- |
   |  | Z−i,𝔪i​(yi,h):=(1+𝔪i​(yi,h,yj,s))​Z−i​(yi,h).Z\_{-}^{i,\mathfrak{m}^{i}}(y^{i,h}):=(1+\mathfrak{m}^{i}(y^{i,h},y^{j,s}))Z\_{-}^{i}(y^{i,h}). |  |
2. (b)

   If h+1≤Nih+1\leq N^{i}, the *exchange rate with fee structure 𝔭i\mathfrak{p}^{i} for selling* (depositing asset YY in the pool) Δ+i​(yi,h):=yi,h+1−yi,h\Delta^{i}\_{+}(y^{i,h}):=y^{i,h+1}-y^{i,h} units of asset YY is given by

   |  |  |  |
   | --- | --- | --- |
   |  | Z+i,𝔭i​(yi,h):=(1−𝔭i​(yi,h,yj,s))​Z+i​(yi,h).Z\_{+}^{i,\mathfrak{p}^{i}}(y^{i,h}):=(1-\mathfrak{p}^{i}(y^{i,h},y^{j,s}))Z\_{+}^{i}(y^{i,h}). |  |

The AMM’s mechanism is independent of the fee schedule: the fee revenues are routed to an external cash account and redistributed later.

Our model aims to study how different pools compete in setting fees dynamically to maximize revenue coming from the order flow. We work in a probability space (Ω,ℱ,𝔽={ℱt}t∈[0,T],ℙ𝔭,𝔪)(\Omega,\mathcal{F},\mathbb{F}=\{\mathcal{F}\_{t}\}\_{t\in[0,T]},\mathbb{P}^{\mathfrak{p},\mathfrak{m}}) supporting all the processes we use below. We model one representative liquidity taker (LT) and assume that their buy and sell order arrivals to each pool i∈{a,b}i\in\{a,b\} are described by point processes {Ni,−,𝔪t}t∈[0,T]\{N^{i,-,\mathfrak{m}\_{t}}\}\_{t\in[0,T]} and {Ni,+,𝔭t}t∈[0,T]\{N^{i,+,\mathfrak{p}\_{t}}\}\_{t\in[0,T]} where 𝔪:=(𝔪a,𝔪b)\mathfrak{m}:=(\mathfrak{m}^{a},\mathfrak{m}^{b}), 𝔭:=(𝔭a,𝔭b)\mathfrak{p}:=(\mathfrak{p}^{a},\mathfrak{p}^{b}) and 𝔪i\mathfrak{m}^{i} and 𝔭i\mathfrak{p}^{i} are assumed to be predictable for each i∈{a,b}i\in\{a,b\}. We include the fees processes 𝔭ti\mathfrak{p}\_{t}^{i} and 𝔪ti\mathfrak{m}\_{t}^{i} in the subscript of {Ni,−,𝔪t}t∈[0,T]\{N^{i,-,\mathfrak{m}\_{t}}\}\_{t\in[0,T]} and {Ni,+,𝔭t}t∈[0,T]\{N^{i,+,\mathfrak{p}\_{t}}\}\_{t\in[0,T]} to draw attention to the controlled stochastic intensities under the probability measure ℙ𝔭,𝔪\mathbb{P}^{\mathfrak{p},\mathfrak{m}}. In this work, the depths of the pools 0​p​ti0pt^{i} are fixed throughout [0,T][0,T], that is, TT is small enough so that LPs do not add or remove liquidity from the pool. This allows us to study liquidity taking and optimal fees in isolation.
This assumption can be relaxed by allowing the total depth of each pool to evolve on a fixed grid over [0,T][0,T]. In that setting, changes in liquidity may arise either exogenously, due to noise liquidity providers, or endogenously, from strategic liquidity providers responding to market conditions. We leave the analysis of both extensions for future research.

Next, we model the intensity of liquidity taking orders arriving to each pool. Let us denote by 𝒜\mathcal{A} the space of 𝔽\mathbb{F}-predictable and bounded processes and let 𝔣i:=(𝔪i,𝔭i)∈𝒜\mathfrak{f}^{i}:=(\mathfrak{m}^{i},\mathfrak{p}^{i})\in\mathcal{A} for i∈{a,b}i\in\{a,b\}. The quantity of asset YY in the pool ii at time t∈[0,T]t\in[0,T] is given by

|  |  |  |
| --- | --- | --- |
|  | Yti,𝔣:=yNti,+,𝔭−Nti,+,𝔪,Y\_{t}^{i,\mathfrak{f}}:=y^{N^{i,+,\mathfrak{p}}\_{t}-N^{i,+,\mathfrak{m}}\_{t}}, |  |

where 𝔣:=(𝔣a,𝔣b)\mathfrak{f}:=(\mathfrak{f}^{a},\mathfrak{f}^{b}).
For each i∈{a,b}i\in\{a,b\} and j∈{a,b}j\in\{a,b\}, j≠ij\neq i the controlled intensities of {Ni,−,𝔪t}t∈[0,T]\{N^{i,-,\mathfrak{m}\_{t}}\}\_{t\in[0,T]} and {Ni,+,𝔭t}t∈[0,T]\{N^{i,+,\mathfrak{p}\_{t}}\}\_{t\in[0,T]} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | λti,−,𝔣\displaystyle\lambda\_{t}^{i,-,\mathfrak{f}} | :=λi,−​exp⁡(ki,0​((St−ζ)−Z−i,𝔪i​(Yti,𝔣))​Δ−i​(Yti,𝔣)+ki,j​(Z−j​(Ytj,𝔣)−Z−i,𝔪i​(Yti,𝔣))​Δ−i​(Yti,𝔣))​𝟙{Yti,𝔣>y¯i},\displaystyle:=\lambda^{i,-}\exp{\left(k^{i,0}((S\_{t}-\zeta)-Z\_{-}^{i,\mathfrak{m}^{i}}(Y\_{t}^{i,\mathfrak{f}}))\Delta\_{-}^{i}(Y\_{t}^{i,\mathfrak{f}})+k^{i,j}(Z\_{-}^{j}(Y\_{t}^{j,\mathfrak{f}})-Z\_{-}^{i,\mathfrak{m}^{i}}(Y\_{t}^{i,\mathfrak{f}}))\Delta\_{-}^{i}(Y\_{t}^{i,\mathfrak{f}})\right)}\mathbbm{1}\_{\{Y\_{t}^{i,\mathfrak{f}}>\underline{y}^{i}\}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λti,+,𝔣\displaystyle\lambda\_{t}^{i,+,\mathfrak{f}} | :=λi,+​exp⁡(ki,0​(Z+i,𝔭i​(Yti,𝔣)−(St+ζ))​Δ+i​(Yti,𝔣)+ki,j​(Z+i,𝔭i​(Yti,𝔣)−Z+j​(Ytj,𝔣))​Δ+i​(Yti,𝔣))​𝟙{Yti,𝔣<y¯i}.\displaystyle:=\lambda^{i,+}\exp{\left(k^{i,0}(Z\_{+}^{i,\mathfrak{p}^{i}}(Y\_{t}^{i,\mathfrak{f}})-(S\_{t}+\zeta))\Delta\_{+}^{i}(Y\_{t}^{i,\mathfrak{f}})+k^{i,j}(Z\_{+}^{i,\mathfrak{p}^{i}}(Y\_{t}^{i,\mathfrak{f}})-Z\_{+}^{j}(Y\_{t}^{j,\mathfrak{f}}))\Delta\_{+}^{i}(Y\_{t}^{i,\mathfrak{f}})\right)}\mathbbm{1}\_{\{Y\_{t}^{i,\mathfrak{f}}<\overline{y}^{i}\}}. |  |

Here, λi,−\lambda^{i,-} and λi,+\lambda^{i,+} are some baseline intensities, ki,0k^{i,0} and ki,jk^{i,j} are positive exponential decay parameters,444Note that different pools get different parameters because there could be external factors (depth) that influence the trading flows in the pool. {St}t∈[0,T]\{S\_{t}\}\_{t\in[0,T]} denotes the midprice in a centralised exchange (outside of the pool) of asset YY in terms of the riskless asset XX, the so-called *oracle price*, and ζ>0\zeta>0 is the corresponding half-spread in the centralised exchange. For simplicity, {St}t∈[0,T]\{S\_{t}\}\_{t\in[0,T]} has dynamics given by

|  |  |  |
| --- | --- | --- |
|  | St=S0+σ​Wt,S\_{t}=S\_{0}+\sigma W\_{t}, |  |

where {Wt}t∈[0,T]\{W\_{t}\}\_{t\in[0,T]} is a Brownian motion. Notice that we recover the model from the monopoly case studied in Baggiani et al. ([2025](#bib.bib1 "Optimal dynamic fees in automated market makers")) by setting the parameters ki,j=0k^{i,j}=0.

The controlled stochastic intensities λti,−,𝔣\lambda\_{t}^{i,-,\mathfrak{f}} and λti,+,𝔣\lambda\_{t}^{i,+,\mathfrak{f}} model that when Z−i,𝔪ti​(Yt−𝔣)<St−ζZ\_{-}^{i,\mathfrak{m}^{i}\_{t}}(Y\_{t-}^{\mathfrak{f}})<S\_{t}-\zeta, buying Δ−i​(yi,j)\Delta^{i}\_{-}(y^{i,j}) units to the pool and selling the same amount from the external venue is profitable to arbitrageurs, in a similar way when Z−i,𝔪ti​(Yt−i,𝔣)<Z+j​(Yt−j,𝔣)Z\_{-}^{i,\mathfrak{m}^{i}\_{t}}(Y\_{t-}^{i,\mathfrak{f}})<Z\_{+}^{j}(Y\_{t-}^{j,\mathfrak{f}}) arbitrageurs can do a roundtrip trade between the two pools. These two effects make the buy intensity increase. There is a similar effect on the sell intensity. In order to make the notation simpler we set ζ=0\zeta=0. The mathematical results can all be obtained for ζ>0\zeta>0.

For each i∈{a,b}i\in\{a,b\} the cumulative fees {ℭti,𝔣i}t∈[0,T]\{\mathfrak{C}\_{t}^{i,\mathfrak{f}^{i}}\}\_{t\in[0,T]} collected by the pools are in turn given by

|  |  |  |
| --- | --- | --- |
|  | ℭti,𝔣i:=∫0t𝔭ui​Z+i,𝔭ui​(Yui,𝔣)​Δ+i​(Yti,𝔣)​dNui,+,𝔭i+∫0t𝔪ui​Z−i,𝔪ui​(Yui,𝔣)​Δ−i​(Yti,𝔣)​dNui,+,𝔪i,t∈[0,T].\mathfrak{C}\_{t}^{i,\mathfrak{f}^{i}}:=\int\_{0}^{t}\mathfrak{p}\_{u}^{i}Z\_{+}^{i,\mathfrak{p}\_{u}^{i}}(Y\_{u}^{i,\mathfrak{f}})\Delta\_{+}^{i}(Y\_{t}^{i,\mathfrak{f}})\,\mathrm{d}N^{i,+,\mathfrak{p}^{i}}\_{u}+\int\_{0}^{t}\mathfrak{m}^{i}\_{u}Z\_{-}^{i,\mathfrak{m}^{i}\_{u}}(Y\_{u}^{i,\mathfrak{f}})\Delta\_{-}^{i}(Y\_{t}^{i,\mathfrak{f}})\,\mathrm{d}N^{i,+,\mathfrak{m}^{i}}\_{u},\quad\quad t\in[0,T]. |  |

The LPs seek to solve the control problems

|  |  |  |  |
| --- | --- | --- | --- |
|  | va​(t,s,𝔠a,ya,yb)\displaystyle v^{a}(t,s,\mathfrak{c}^{a},y^{a},y^{b}) | :=sup(𝔪a,𝔭a)∈𝒜tv(a,𝔪,𝔭)​(t,s,𝔠,ya,yb),\displaystyle:=\sup\_{(\mathfrak{m}^{a},\mathfrak{p}^{a})\in\mathcal{A}\_{t}}v^{(a,\mathfrak{m},\mathfrak{p})}(t,s,\mathfrak{c},y^{a},y^{b}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | vb​(t,s,𝔠b,ya,yb)\displaystyle v^{b}(t,s,\mathfrak{c}^{b},y^{a},y^{b}) | :=sup(𝔪b,𝔭b)∈𝒜tv(b,𝔪,𝔭)​(t,s,𝔠,ya,yb),\displaystyle:=\sup\_{(\mathfrak{m}^{b},\mathfrak{p}^{b})\in\mathcal{A}\_{t}}v^{(b,\mathfrak{m},\mathfrak{p})}(t,s,\mathfrak{c},y^{a},y^{b}), |  |

where 𝒜t\mathcal{A}\_{t} denotes the set of all 𝔽\mathbb{F}-predictable and bounded fee structure processes (𝔪ui,𝔭ui){t≤u≤T}(\mathfrak{m}\_{u}^{i},\mathfrak{p}\_{u}^{i})\_{\{t\leq u\leq T\}} and the conditional performance criterion are given by

|  |  |  |
| --- | --- | --- |
|  | v(a,𝔪,𝔭)​(t,s,ya,yb):=𝔼(t,s,𝔠a,ya,yb)(𝔪,𝔭)​[ℭT(a,t,s,ya,yb,𝔣a)],v(b,𝔪,𝔭)​(t,s,ya,yb):=𝔼(t,s,𝔠b,ya,yb)(𝔪,𝔭)​[ℭT(b,t,s,ya,yb,𝔣b)].v^{(a,\mathfrak{m},\mathfrak{p})}(t,s,y^{a},y^{b}):=\mathbb{E}\_{(t,s,\mathfrak{c}^{a},y^{a},y^{b})}^{(\mathfrak{m},\mathfrak{p})}\left[\mathfrak{C}\_{T}^{(a,t,s,y^{a},y^{b},\mathfrak{f}^{a})}\right],\quad\quad v^{(b,\mathfrak{m},\mathfrak{p})}(t,s,y^{a},y^{b}):=\mathbb{E}\_{(t,s,\mathfrak{c}^{b},y^{a},y^{b})}^{(\mathfrak{m},\mathfrak{p})}\left[\mathfrak{C}\_{T}^{(b,t,s,y^{a},y^{b},\mathfrak{f}^{b})}\right]. |  |

Here,

|  |  |  |
| --- | --- | --- |
|  | {Yu(a,t,s,𝔠a,ya,yb,𝔣a)}u∈[t,T],{Yu(b,t,s,𝔠b,ya,yb,𝔣b)}u∈[t,T]​ and ​{Su(t,s,𝔠a,𝔠b,ya,yb)}u∈[t,T]\{Y\_{u}^{(a,t,s,\mathfrak{c}^{a},y^{a},y^{b},\mathfrak{f}^{a})}\}\_{u\in[t,T]},\;\{Y\_{u}^{(b,t,s,\mathfrak{c}^{b},y^{a},y^{b},\mathfrak{f}^{b})}\}\_{u\in[t,T]}\text{ and }\{S\_{u}^{(t,s,\mathfrak{c}^{a},\mathfrak{c}^{b},y^{a},y^{b})}\}\_{u\in[t,T]} |  |

denote the (controlled) processes YaY^{a}, YbY^{b} and SS restarted at time tt with initial value 𝔠a\mathfrak{c}^{a}, 𝔠b\mathfrak{c}^{b}, yay^{a}, yby^{b} and ss, respectively. From the dynamic programming principle, we determine that the Hamilton-Jacobi-Bellman (HJB) for the value function of the player aa is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=\displaystyle 0={} | ∂tva​(t,s,ya,yb)+σ22​∂s​sva​(t,s,ya,yb)\displaystyle\partial\_{t}v^{a}(t,s,y^{a},y^{b})+\frac{\sigma^{2}}{2}\,\partial\_{ss}v^{a}(t,s,y^{a},y^{b}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +sup𝔪a∈ℝ[λa,−exp(ka(ka,0kas+ka,bkaZ−b(yb)−(1+𝔪a)Z−a(ya))Δ−a(ya))\displaystyle+\sup\_{\mathfrak{m}^{a}\in\mathbb{R}}\Bigg[\lambda^{a,-}\exp\!\Big(k^{a}\Big(\frac{k^{a,0}}{k^{a}}\,s+\frac{k^{a,b}}{k^{a}}\,Z\_{-}^{b}(y^{b})-(1+\mathfrak{m}^{a})\,Z\_{-}^{a}(y^{a})\Big)\Delta\_{-}^{a}(y^{a})\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(va(t,s,ya−Δ−a(ya),yb)−va(t,s,ya,yb)+𝔪aZ−a(ya)Δ−a(ya)) 1{ya>y¯a}]\displaystyle\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\times\Big(v^{a}(t,s,y^{a}-\Delta\_{-}^{a}(y^{a}),y^{b})-v^{a}(t,s,y^{a},y^{b})+\mathfrak{m}^{a}\,Z\_{-}^{a}(y^{a})\,\Delta\_{-}^{a}(y^{a})\Big)\mathbbm{1}\_{\{y^{a}>\underline{y}^{a}\}}\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λb,−​exp⁡(kb​(kb,0kb​s+kb,akb​Z−a​(ya)−(1+𝔪b)​Z−b​(yb))​Δ−b​(yb))\displaystyle+\lambda^{b,-}\exp\!\Big(k^{b}\Big(\frac{k^{b,0}}{k^{b}}\,s+\frac{k^{b,a}}{k^{b}}\,Z\_{-}^{a}(y^{a})-(1+\mathfrak{m}^{b})\,Z\_{-}^{b}(y^{b})\Big)\Delta\_{-}^{b}(y^{b})\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(va​(t,s,ya,yb−Δ−b​(yb))−va​(t,s,ya,yb))​ 1{yb>y¯b}\displaystyle\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\times\Big(v^{a}(t,s,y^{a},y^{b}-\Delta\_{-}^{b}(y^{b}))-v^{a}(t,s,y^{a},y^{b})\Big)\mathbbm{1}\_{\{y^{b}>\underline{y}^{b}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +sup𝔭a∈ℝ[λa,+exp(ka((1−𝔭a)Z+a(ya)−ka,0kas−ka,bkaZ+b(yb))Δ+a(ya))\displaystyle+\sup\_{\mathfrak{p}^{a}\in\mathbb{R}}\Bigg[\lambda^{a,+}\exp\!\Big(k^{a}\Big((1-\mathfrak{p}^{a})\,Z\_{+}^{a}(y^{a})-\frac{k^{a,0}}{k^{a}}\,s-\frac{k^{a,b}}{k^{a}}\,Z\_{+}^{b}(y^{b})\Big)\Delta\_{+}^{a}(y^{a})\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(va(t,s,ya+Δ+a(ya),yb)−va(t,s,ya,yb)+𝔭aZ+a(ya)Δ+a(ya)) 1{ya<y¯a}]\displaystyle\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\times\Big(v^{a}(t,s,y^{a}+\Delta\_{+}^{a}(y^{a}),y^{b})-v^{a}(t,s,y^{a},y^{b})+\mathfrak{p}^{a}\,Z\_{+}^{a}(y^{a})\,\Delta\_{+}^{a}(y^{a})\Big)\mathbbm{1}\_{\{y^{a}<\overline{y}^{a}\}}\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λb,+​exp⁡(kb​((1−𝔭b)​Z+b​(yb)−kb,0kb​s−kb,akb​Z+a​(ya))​Δ+a​(ya))\displaystyle+\lambda^{b,+}\exp\!\Big(k^{b}\Big((1-\mathfrak{p}^{b})\,Z\_{+}^{b}(y^{b})-\frac{k^{b,0}}{k^{b}}\,s-\frac{k^{b,a}}{k^{b}}\,Z\_{+}^{a}(y^{a})\Big)\Delta\_{+}^{a}(y^{a})\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(va​(t,s,ya,yb+Δ+b​(yb))−va​(t,s,ya,yb))​ 1{yb<y¯b}.\displaystyle\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\hskip 18.49988pt\times\Big(v^{a}(t,s,y^{a},y^{b}+\Delta\_{+}^{b}(y^{b}))-v^{a}(t,s,y^{a},y^{b})\Big)\mathbbm{1}\_{\{y^{b}<\overline{y}^{b}\}}. |  |

where ka=ka,0+ka,bk^{a}=k^{a,0}+k^{a,b} and kb=kb,0+kb,ak^{b}=k^{b,0}+k^{b,a}. The HJB for player bb is similar and we omit it for brevity. First order conditions on the maximizers yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔪a,∗​(t,s,ya,yb)\displaystyle\mathfrak{m}^{a,\*}(t,s,y^{a},y^{b}) | =1+ka​(va​(t,s,ya,yb)−va​(t,s,ya−Δ−a​(ya),yb))ka​Z−a​(ya)​Δ−a​(ya),\displaystyle=\frac{1+k^{a}(v^{a}(t,s,y^{a},y^{b})-v^{a}(t,s,y^{a}-\Delta\_{-}^{a}(y^{a}),y^{b}))}{k^{a}Z\_{-}^{a}(y^{a})\Delta\_{-}^{a}(y^{a})}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔭a,∗​(t,s,ya,yb)\displaystyle\mathfrak{p}^{a,\*}(t,s,y^{a},y^{b}) | =1+ka​(va​(t,s,ya,yb)−va​(t,s,ya+Δ+a​(ya),yb))ka​Z+a​(ya)​Δ+a​(ya),\displaystyle=\frac{1+k^{a}(v^{a}(t,s,y^{a},y^{b})-v^{a}(t,s,y^{a}+\Delta\_{+}^{a}(y^{a}),y^{b}))}{k^{a}Z\_{+}^{a}(y^{a})\Delta\_{+}^{a}(y^{a})}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔪b,∗​(t,s,ya,yb)\displaystyle\mathfrak{m}^{b,\*}(t,s,y^{a},y^{b}) | =1+kb​(vb​(t,s,ya,yb)−vb​(t,s,ya,yb−Δ−b​(yb)))kb​Z−b​(yb)​Δ−b​(yb),\displaystyle=\frac{1+k^{b}(v^{b}(t,s,y^{a},y^{b})-v^{b}(t,s,y^{a},y^{b}-\Delta\_{-}^{b}(y^{b})))}{k^{b}Z\_{-}^{b}(y^{b})\Delta\_{-}^{b}(y^{b})}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔭b,∗​(t,s,ya,yb)\displaystyle\mathfrak{p}^{b,\*}(t,s,y^{a},y^{b}) | =1+kb​(vb​(t,s,ya,yb)−vb​(t,s,ya,yb+Δ+b​(yb)))kb​Z+b​(yb)​Δ+b​(yb).\displaystyle=\frac{1+k^{b}(v^{b}(t,s,y^{a},y^{b})-v^{b}(t,s,y^{a},y^{b}+\Delta\_{+}^{b}(y^{b})))}{k^{b}Z\_{+}^{b}(y^{b})\Delta\_{+}^{b}(y^{b})}. |  |

Thus, the HJB for player aa turns into the following PDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=\displaystyle 0= | ∂∂t​va​(t,s,ya,yb)+σ22​∂2∂s2​va​(t,s,ya,yb)\displaystyle\frac{\partial}{\partial t}v^{a}(t,s,y^{a},y^{b})+\frac{\sigma^{2}}{2}\frac{\partial^{2}}{\partial s^{2}}v^{a}(t,s,y^{a},y^{b}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | λa,−​eka​(ka,0ka​s+ka,bka​Z−b​(yb))​Δ−a​(ya)−1ka​e−ka​Z−a​(ya)​Δ−a​(ya)​eka​(va​(t,s,ya−Δ−a​(ya),yb)−va​(t,s,ya,yb))​𝟙{ya>y¯a}+\displaystyle\frac{\lambda^{a,-}e^{k^{a}\left(\frac{k^{a,0}}{k^{a}}s+\frac{k^{a,b}}{k^{a}}Z\_{-}^{b}(y^{b})\right)\Delta^{a}\_{-}(y^{a})-1}}{k^{a}}e^{-k^{a}Z\_{-}^{a}(y^{a})\Delta\_{-}^{a}(y^{a})}e^{k^{a}(v^{a}(t,s,y^{a}-\Delta\_{-}^{a}(y^{a}),y^{b})-v^{a}(t,s,y^{a},y^{b}))}\mathbbm{1}\_{\{y^{a}>\underline{y}^{a}\}}\;+ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | λb,−​ekb​(kb,0kb​s+kb,akb​Z−a​(ya))​Δ−b​(yb)−1​e−kb​Z−b​(yb)​Δ−b​(yb)\displaystyle\lambda^{b,-}e^{k^{b}\left(\frac{k^{b,0}}{k^{b}}s+\frac{k^{b,a}}{k^{b}}Z\_{-}^{a}(y^{a})\right)\Delta^{b}\_{-}(y^{b})-1}e^{-k^{b}Z\_{-}^{b}(y^{b})\Delta\_{-}^{b}(y^{b})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ekb​(vb​(t,s,ya,yb−Δ−b​(yb))−vb​(t,s,ya,yb))​(va​(t,s,ya,yb−Δ−b​(yb))−va​(t,s,ya,yb))​𝟙{yb>y¯b}+\displaystyle\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad e^{k^{b}(v^{b}(t,s,y^{a},y^{b}-\Delta\_{-}^{b}(y^{b}))-v^{b}(t,s,y^{a},y^{b}))}\left(v^{a}(t,s,y^{a},y^{b}-\Delta\_{-}^{b}(y^{b}))-v^{a}(t,s,y^{a},y^{b})\right)\mathbbm{1}\_{\{y^{b}>\underline{y}^{b}\}}\;+ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | λa,+​e−ka​(ka,0ka​s+ka,bka​Z+b​(yb))​Δ+a​(ya)−1ka​eka​Z+a​(ya)​Δ+a​(ya)​eka​(va​(t,s,ya+Δ+a​(ya),yb)−va​(t,s,ya,yb))​𝟙{ya<y¯a}+\displaystyle\frac{\lambda^{a,+}e^{-k^{a}\left(\frac{k^{a,0}}{k^{a}}s+\frac{k^{a,b}}{k^{a}}Z\_{+}^{b}(y^{b})\right)\Delta^{a}\_{+}(y^{a})-1}}{k^{a}}e^{k^{a}Z\_{+}^{a}(y^{a})\Delta\_{+}^{a}(y^{a})}e^{k^{a}(v^{a}(t,s,y^{a}+\Delta\_{+}^{a}(y^{a}),y^{b})-v^{a}(t,s,y^{a},y^{b}))}\mathbbm{1}\_{\{y^{a}<\overline{y}^{a}\}}\;+ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | λb,+​e−kb​(kb,0kb​s+kb,akb​Z+a​(ya))​Δ+b​(yb)−1​ekb​Z+b​(yb)​Δ+b​(yb)\displaystyle\lambda^{b,+}e^{-k^{b}\left(\frac{k^{b,0}}{k^{b}}s+\frac{k^{b,a}}{k^{b}}Z\_{+}^{a}(y^{a})\right)\Delta^{b}\_{+}(y^{b})-1}e^{k^{b}Z\_{+}^{b}(y^{b})\Delta\_{+}^{b}(y^{b})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ekb​(vb​(t,s,ya,yb+Δ+b​(yb))−vb​(t,s,ya,yb))​(va​(t,s,ya,yb+Δ+b​(yb))−va​(t,s,ya,yb))​𝟙{yb<y¯b}.\displaystyle\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad e^{k^{b}(v^{b}(t,s,y^{a},y^{b}+\Delta\_{+}^{b}(y^{b}))-v^{b}(t,s,y^{a},y^{b}))}\left(v^{a}(t,s,y^{a},y^{b}+\Delta\_{+}^{b}(y^{b}))-v^{a}(t,s,y^{a},y^{b})\right)\mathbbm{1}\_{\{y^{b}<\overline{y}^{b}\}}. |  |

We now make a few simplifying assumptions to compute a closed-form solution. More precisely, we treat ss as a parameter and we assume that the change in one agent’s inventory has a negligible impact on the other player’s value function, that is

|  |  |  |
| --- | --- | --- |
|  | va​(t,s,ya,yb+Δ+b​(yb))≈va​(t,s,ya,yb),va​(t,s,ya,yb−Δ−b​(yb))≈va​(t,s,ya,yb).\displaystyle v^{a}(t,s,y^{a},y^{b}+\Delta\_{+}^{b}(y^{b}))\approx v^{a}(t,s,y^{a},y^{b}),\hskip 18.49988ptv^{a}(t,s,y^{a},y^{b}-\Delta\_{-}^{b}(y^{b}))\approx v^{a}(t,s,y^{a},y^{b}). |  |

###### Remark 2.1.

Our results indicate that the above approximation provides a good level of accuracy for the purposes of this study, particularly in good regimes where the within-venue price ZZ remains close to the centralised reference price SS.555See the project repository at <https://github.com/leonardobaggiani/amm-fees-competition> for the implementation details.

The approximated equation takes the form of

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=\displaystyle 0= | ∂∂t​va​(t,ya,yb)\displaystyle\frac{\partial}{\partial t}v^{a}(t,y^{a},y^{b}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λa,−​eka​(ka,0ka​s+ka,bka​Z−b​(yb))​Δ−a​(ya)−1ka​e−ka​Z−a​(ya)​Δ−a​(ya)​eka​(va​(t,ya−Δ−a​(ya),yb)−va​(t,ya,yb))​𝟙{ya>y¯a}\displaystyle+\frac{\lambda^{a,-}e^{k^{a}\left(\frac{k^{a,0}}{k^{a}}s+\frac{k^{a,b}}{k^{a}}Z\_{-}^{b}(y^{b})\right)\Delta^{a}\_{-}(y^{a})-1}}{k^{a}}e^{-k^{a}Z\_{-}^{a}(y^{a})\Delta\_{-}^{a}(y^{a})}e^{k^{a}(v^{a}(t,y^{a}-\Delta\_{-}^{a}(y^{a}),y^{b})-v^{a}(t,y^{a},y^{b}))}\mathbbm{1}\_{\{y^{a}>\underline{y}^{a}\}}\; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λa,+​e−ka​(ka,0ka​s+ka,bka​Z+b​(yb))​Δ+a​(ya)−1ka​eka​Z+a​(ya)​Δ+a​(ya)​eka​(va​(t,ya+Δ+a​(ya),yb)−va​(t,ya,yb))​𝟙{ya<y¯a}.\displaystyle+\frac{\lambda^{a,+}e^{-k^{a}\left(\frac{k^{a,0}}{k^{a}}s+\frac{k^{a,b}}{k^{a}}Z\_{+}^{b}(y^{b})\right)\Delta^{a}\_{+}(y^{a})-1}}{k^{a}}e^{k^{a}Z\_{+}^{a}(y^{a})\Delta\_{+}^{a}(y^{a})}e^{k^{a}(v^{a}(t,y^{a}+\Delta\_{+}^{a}(y^{a}),y^{b})-v^{a}(t,y^{a},y^{b}))}\mathbbm{1}\_{\{y^{a}<\overline{y}^{a}\}}. |  |

We make the ansatzes

|  |  |  |
| --- | --- | --- |
|  | eka​va​(t,ya,yb):=wa​(t,ya,yb),ekb​vb​(t,ya,yb):=wb​(t,ya,yb),\displaystyle e^{k^{a}v^{a}(t,y^{a},y^{b})}:=w^{a}(t,y^{a},y^{b}),\hskip 18.49988pte^{k^{b}v^{b}(t,y^{a},y^{b})}:=w^{b}(t,y^{a},y^{b}), |  |

and we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=∂∂t​wa​(t,ya,yb)\displaystyle 0=\frac{\partial}{\partial t}w^{a}(t,y^{a},y^{b}) | +λa,−​eka​(ka,0ka​s+ka,bka​Z−b​(yb))​Δ−a​(ya)−1​e−ka​Z−a​(ya)​Δ−a​(ya)​wa​(t,ya−Δ−a​(ya),yb)​𝟙{ya>y¯a}\displaystyle+\lambda^{a,-}e^{k^{a}\left(\frac{k^{a,0}}{k^{a}}s+\frac{k^{a,b}}{k^{a}}Z\_{-}^{b}(y^{b})\right)\Delta^{a}\_{-}(y^{a})-1}e^{-k^{a}Z\_{-}^{a}(y^{a})\Delta\_{-}^{a}(y^{a})}w^{a}(t,y^{a}-\Delta\_{-}^{a}(y^{a}),y^{b})\mathbbm{1}\_{\{y^{a}>\underline{y}^{a}\}}\; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λa,+​e−ka​(ka,0ka​s+ka,bka​Z+b​(yb))​Δ+a​(ya)−1​eka​Z+a​(ya)​Δ+a​(ya)​wa​(t,ya+Δ−a​(ya),yb)​𝟙{ya<y¯a}.\displaystyle+\lambda^{a,+}e^{-k^{a}\left(\frac{k^{a,0}}{k^{a}}s+\frac{k^{a,b}}{k^{a}}Z\_{+}^{b}(y^{b})\right)\Delta^{a}\_{+}(y^{a})-1}e^{k^{a}Z\_{+}^{a}(y^{a})\Delta\_{+}^{a}(y^{a})}w^{a}(t,y^{a}+\Delta\_{-}^{a}(y^{a}),y^{b})\mathbbm{1}\_{\{y^{a}<\overline{y}^{a}\}}. |  |

An explicit solution of the above PDEs is given in the following theorem.

###### Theorem 2.2.

For l∈{−Nb,…,Nb}l\in\{-N^{b},\dots,N^{b}\} and h∈{−Na,…,Na}h\in\{-N^{a},\dots,N^{a}\} define the matrices 𝐀b,l:=(𝐀i,jl)0≤i≤j≤2​N\mathbf{A}^{b,l}:=(\mathbf{A}^{l}\_{i,j})\_{0\leq i\leq j\leq 2N} and 𝐀a:=(𝐀i,la,h)0≤i≤l≤2​N\mathbf{A}^{a}:=(\mathbf{A}^{a,h}\_{i,l})\_{0\leq i\leq l\leq 2N} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐀i,ja​(yb,l)\displaystyle\mathbf{A}^{a}\_{i,j}(y^{b,l}) | :={λa,+​e−ka​(ka,0ka​s+ka,bka​Z+b​(yb,l))​Δ+a​(ya,j−Na)−1​eka​Z+a​(ya,j−Na)​Δ+a​(ya,j−Na) if ​i=j−1,λa,−​eka​(ka,0ka​s+ka,bka​Z−b​(yb,l))​Δ−a​(ya,j−Na)−1​e−ka​Z−a​(ya,j−Na)​Δ−a​(ya,j−Na) if ​i=j+10 otherwise,\displaystyle:=\begin{cases}\lambda^{a,+}e^{-k^{a}\left(\frac{k^{a,0}}{k^{a}}s+\frac{k^{a,b}}{k^{a}}Z\_{+}^{b}(y^{b,l})\right)\Delta^{a}\_{+}(y^{a,j-N^{a}})-1}e^{k^{a}Z\_{+}^{a}(y^{a,j-N^{a}})\Delta\_{+}^{a}(y^{a,j-N^{a}})}&\text{ if }i=j-1,\\ \lambda^{a,-}e^{k^{a}\left(\frac{k^{a,0}}{k^{a}}s+\frac{k^{a,b}}{k^{a}}Z\_{-}^{b}(y^{b,l})\right)\Delta^{a}\_{-}(y^{a,j-N^{a}})-1}e^{-k^{a}Z\_{-}^{a}(y^{a,j-N^{a}})\Delta\_{-}^{a}(y^{a,j-N^{a}})}&\text{ if }i=j+1\\ 0&\text{ otherwise,}\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐀i,jb​(ya,h)\displaystyle\mathbf{A}^{b}\_{i,j}(y^{a,h}) | :={λb,+​e−kb​(kb,0kb​s+kb,akb​Z+a​(ya,h))​Δ+b​(yb,j−Nb)−1​ekb​Z+b​(yb,j−Nb)​Δ+b​(yb,j−Nb) if ​i=j−1,λb,−​ekb​(kb,0kb​s+kb,akb​Z−a​(ya,h))​Δ−b​(yb,j−Nb)−1​e−kb​Z−b​(yb,j−Nb)​Δ−b​(yb,j−Nb) if ​i=j+10 otherwise.\displaystyle:=\begin{cases}\lambda^{b,+}e^{-k^{b}\left(\frac{k^{b,0}}{k^{b}}s+\frac{k^{b,a}}{k^{b}}Z\_{+}^{a}(y^{a,h})\right)\Delta^{b}\_{+}(y^{b,j-N^{b}})-1}e^{k^{b}Z\_{+}^{b}(y^{b,j-N^{b}})\Delta\_{+}^{b}(y^{b,j-N^{b}})}&\text{ if }i=j-1,\\ \lambda^{b,-}e^{k^{b}\left(\frac{k^{b,0}}{k^{b}}s+\frac{k^{b,a}}{k^{b}}Z\_{-}^{a}(y^{a,h})\right)\Delta^{b}\_{-}(y^{b,j-N^{b}})-1}e^{-k^{b}Z\_{-}^{b}(y^{b,j-N^{b}})\Delta\_{-}^{b}(y^{b,j-N^{b}})}&\text{ if }i=j+1\\ 0&\text{ otherwise.}\end{cases} |  |

Denote with 𝟏\mathbf{1} the unit vectors of ℝ2​Na+1\mathbb{R}^{2N^{a}+1} and ℝ2​Nb+1\mathbb{R}^{2N^{b}+1}. Define the functions wa:[0,T]×{ya,−Na,…,ya,Na}×{yb,−Nb,…,yb,Nb}→ℝw^{a}:[0,T]\times\{y^{a,-N^{a}},\dots,y^{a,N^{a}}\}\times\{y^{b,-N^{b}},\dots,y^{b,N^{b}}\}\to\mathbb{R} and wb:[0,T]×{ya,−Na,…,ya,Na}×{yb,−Nb,…,yb,Nb}→ℝw^{b}:[0,T]\times\{y^{a,-N^{a}},\dots,y^{a,N^{a}}\}\times\{y^{b,-N^{b}},\dots,y^{b,N^{b}}\}\to\mathbb{R} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | wa​(t,ya,i,yb,j)\displaystyle w^{a}(t,y^{a,i},y^{b,j}) | :=(exp⁡(𝐀a​(yb,j)​(T−t))​ 1)i\displaystyle:=\left(\exp\big(\mathbf{A}^{a}(y^{b,j})(T-t)\big)\,\mathbf{1}\right)\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | wb​(t,ya,i,yb,j)\displaystyle w^{b}(t,y^{a,i},y^{b,j}) | :=(exp⁡(𝐀b​(ya,i)​(T−t))​ 1)j\displaystyle:=\left(\exp\big(\mathbf{A}^{b}(y^{a,i})(T-t)\big)\,\mathbf{1}\right)\_{j} |  |

and the functions va:[0,T]×{ya,−Na,…,ya,Na}×{yb,−Nb,…,yb,Nb}×ℝ+→ℝv^{a}:[0,T]\times\{y^{a,-N^{a}},\dots,y^{a,N^{a}}\}\times\{y^{b,-N^{b}},\dots,y^{b,N^{b}}\}\times\mathbb{R}\_{+}\to\mathbb{R}, vb:[0,T]×{ya,−Na,…,ya,Na}×{yb,−Nb,…,yb,Nb}×ℝ+→ℝv^{b}:[0,T]\times\{y^{a,-N^{a}},\dots,y^{a,N^{a}}\}\times\{y^{b,-N^{b}},\dots,y^{b,N^{b}}\}\times\mathbb{R}\_{+}\to\mathbb{R} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | va​(t,ya,i,yb,j,𝔠a)\displaystyle v^{a}(t,y^{a,i},y^{b,j},\mathfrak{c}^{a}) | :=𝔠a+1ka​log⁡(wa​(t,ya,i,yb,j)),\displaystyle:=\mathfrak{c}^{a}+\frac{1}{k^{a}}\log(w^{a}(t,y^{a,i},y^{b,j})), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | vb​(t,ya,i,yb,j,𝔠b)\displaystyle v^{b}(t,y^{a,i},y^{b,j},\mathfrak{c}^{b}) | :=𝔠b+1kb​log⁡(wb​(t,ya,i,yb,j)).\displaystyle:=\mathfrak{c}^{b}+\frac{1}{k^{b}}\log(w^{b}(t,y^{a,i},y^{b,j})). |  |

Then vav^{a} and vbv^{b} solve the system of HJBs

|  |  |  |
| --- | --- | --- |
|  | {0=∂∂t​va​(t,ya,i,yb,j,𝔠a)+sup𝔪a∈ℝλa,−exp{ka(ka,0kas+ka,bkaZ−b(yb))−ka(1+𝔪a)Z−a(ya)Δ−a(ya)}(va(t,ya−Δ−a(ya),yb,𝔠a+𝔪aZ−a(ya)Δ−a(ya))−va(t,ya,yb,𝔠a)) 1{ya>y¯a}+sup𝔭a∈ℝλa,+exp{−ka(ka,0kas+ka,bkaZ+b(yb))+ka(1−𝔭a)Z+a(ya)Δ+a(ya)}(va(t,ya+Δ+a(ya),yb,𝔠a+𝔭aZ+a(ya)Δ+a(ya))−va(t,ya,yb,𝔠a)) 1{ya<y¯a},0=∂∂t​vb​(t,s,ya,yb,𝔠b)+sup𝔪b∈ℝλb,−exp{kb(kb,0kbs+kb,akbZ−a(ya))−kb(1+𝔪b)Z−b(yb)Δ−b(yb)}(vb(t,ya,yb−Δ−b(yb),𝔠b+𝔪bZ−b(yb)Δ−b(yb))−vb(t,ya,yb,𝔠b)) 1{yb>y¯b}+sup𝔭b∈ℝλb,+exp{−kb(kb,0kbs+kb,akbZ+a(ya))+kb(1−𝔭b)Z+b(yb)Δ+b(yb)}(vb(t,ya,yb+Δ+b(yb),𝔠b+𝔭bZ+b(yb)Δ+b(yb))−vb(t,ya,yb,𝔠b)) 1{yb<y¯b}\displaystyle\begin{cases}0\;=\;&\frac{\partial}{\partial t}\,v^{a}(t,y^{a,i},y^{b,j},\mathfrak{c}^{a})\\[4.0pt] &\;+\;\sup\_{\mathfrak{m}^{a}\in\mathbb{R}}\lambda^{a,-}\,\exp\Bigg\{k^{a}\!\Big(\tfrac{k^{a,0}}{k^{a}}\,s+\tfrac{k^{a,b}}{k^{a}}\,Z\_{-}^{b}(y^{b})\Big)\\ &\hskip 18.49988pt\hskip 18.49988pt-k^{a}\!\Big(1+\mathfrak{m}^{a}\Big)Z\_{-}^{a}(y^{a})\,\Delta\_{-}^{a}(y^{a})\Bigg\}\Big(v^{a}(t,y^{a}-\Delta\_{-}^{a}(y^{a}),y^{b},\mathfrak{c}^{a}+\mathfrak{m}^{a}\,Z\_{-}^{a}(y^{a})\,\Delta\_{-}^{a}(y^{a}))-v^{a}(t,y^{a},y^{b},\mathfrak{c}^{a})\Big)\,\mathbbm{1}\_{\{y^{a}>\underline{y}^{a}\}}\\[6.0pt] &\;+\;\sup\_{\mathfrak{p}^{a}\in\mathbb{R}}\lambda^{a,+}\,\exp\Bigg\{-k^{a}\!\Big(\tfrac{k^{a,0}}{k^{a}}\,s+\tfrac{k^{a,b}}{k^{a}}\,Z\_{+}^{b}(y^{b})\Big)\\ &\hskip 18.49988pt\hskip 18.49988pt+k^{a}\!\Big(1-\mathfrak{p}^{a}\Big)Z\_{+}^{a}(y^{a})\,\Delta\_{+}^{a}(y^{a})\Bigg\}\Big(v^{a}(t,y^{a}+\Delta\_{+}^{a}(y^{a}),y^{b},\mathfrak{c}^{a}+\mathfrak{p}^{a}\,Z\_{+}^{a}(y^{a})\,\Delta\_{+}^{a}(y^{a}))-v^{a}(t,y^{a},y^{b},\mathfrak{c}^{a})\Big)\,\mathbbm{1}\_{\{y^{a}<\overline{y}^{a}\}},\\[6.0pt] 0\;=\;&\frac{\partial}{\partial t}\,v^{b}(t,s,y^{a},y^{b},\mathfrak{c}^{b})\\[4.0pt] &\;+\;\sup\_{\mathfrak{m}^{b}\in\mathbb{R}}\lambda^{b,-}\,\exp\Bigg\{k^{b}\!\Big(\tfrac{k^{b,0}}{k^{b}}\,s+\tfrac{k^{b,a}}{k^{b}}\,Z\_{-}^{a}(y^{a})\Big)\\ &\hskip 18.49988pt\hskip 18.49988pt-k^{b}\!\Big(1+\mathfrak{m}^{b}\Big)Z\_{-}^{b}(y^{b})\,\Delta\_{-}^{b}(y^{b})\Bigg\}\Big(v^{b}(t,y^{a},y^{b}-\Delta\_{-}^{b}(y^{b}),\mathfrak{c}^{b}+\mathfrak{m}^{b}\,Z\_{-}^{b}(y^{b})\,\Delta\_{-}^{b}(y^{b}))-v^{b}(t,y^{a},y^{b},\mathfrak{c}^{b})\Big)\,\mathbbm{1}\_{\{y^{b}>\underline{y}^{b}\}}\\[6.0pt] &\;+\;\sup\_{\mathfrak{p}^{b}\in\mathbb{R}}\lambda^{b,+}\,\exp\Bigg\{-k^{b}\!\Big(\tfrac{k^{b,0}}{k^{b}}\,s+\tfrac{k^{b,a}}{k^{b}}\,Z\_{+}^{a}(y^{a})\Big)\\ &\hskip 18.49988pt\hskip 18.49988pt+k^{b}\!\Big(1-\mathfrak{p}^{b}\Big)Z\_{+}^{b}(y^{b})\,\Delta\_{+}^{b}(y^{b})\Bigg\}\Big(v^{b}(t,y^{a},y^{b}+\Delta\_{+}^{b}(y^{b}),\mathfrak{c}^{b}+\mathfrak{p}^{b}\,Z\_{+}^{b}(y^{b})\,\Delta\_{+}^{b}(y^{b}))-v^{b}(t,y^{a},y^{b},\mathfrak{c}^{b})\Big)\,\mathbbm{1}\_{\{y^{b}<\overline{y}^{b}\}}\\[6.0pt] \end{cases} |  |

with boundary conditions va​(T,ya,yb,𝔠b)=0v^{a}(T,y^{a},y^{b},\mathfrak{c}^{b})=0 and vb​(T,ya,yb,𝔠b)=0v^{b}(T,y^{a},y^{b},\mathfrak{c}^{b})=0, for every yay^{a} and yby^{b}. Moreover, the corresponding maximizers are independent of 𝔠a\mathfrak{c}^{a} and 𝔠b\mathfrak{c}^{b} and are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔪a,∗​(t,ya,i,yb,j)\displaystyle\mathfrak{m}^{a,\*}(t,y^{a,i},y^{b,j}) | =1ka​Z−a​(ya,i)​Δ−a​(ya,i)​(1+log⁡(wa​(t,ya,i,yb,j)wa​(t,ya,i−1,yb,j))),\displaystyle=\frac{1}{k^{a}Z\_{-}^{a}(y^{a,i})\Delta\_{-}^{a}(y^{a,i})}\left(1+\log\left(\frac{w^{a}(t,y^{a,i},y^{b,j})}{w^{a}(t,y^{a,i-1},y^{b,j})}\right)\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔭a,∗​(t,ya,i,yb,j)\displaystyle\mathfrak{p}^{a,\*}(t,y^{a,i},y^{b,j}) | =1ka​Z+a​(ya,i)​Δ+a​(ya,i)​(1+log⁡(wa​(t,ya,i,yb,j)wa​(t,ya,i+1,yb,j))),\displaystyle=\frac{1}{k^{a}Z\_{+}^{a}(y^{a,i})\Delta\_{+}^{a}(y^{a,i})}\left(1+\log\left(\frac{w^{a}(t,y^{a,i},y^{b,j})}{w^{a}(t,y^{a,i+1},y^{b,j})}\right)\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔪b,∗​(t,ya,i,yb,j)\displaystyle\mathfrak{m}^{b,\*}(t,y^{a,i},y^{b,j}) | =1kb​Z−b​(yb,j)​Δ−b​(yb,j)​(1+log⁡(wb​(t,ya,i,yb,j)wb​(t,ya,i,yb,j−1))),\displaystyle=\frac{1}{k^{b}Z\_{-}^{b}(y^{b,j})\Delta\_{-}^{b}(y^{b,j})}\left(1+\log\left(\frac{w^{b}(t,y^{a,i},y^{b,j})}{w^{b}(t,y^{a,i},y^{b,j-1})}\right)\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔭b,∗​(t,ya,i,yb,j)\displaystyle\mathfrak{p}^{b,\*}(t,y^{a,i},y^{b,j}) | =1kb​Z+b​(yb,j)​Δ+b​(yb,j)​(1+log⁡(wb​(t,ya,i,yb,j)wb​(t,ya,i,yb,j+1))).\displaystyle=\frac{1}{k^{b}Z\_{+}^{b}(y^{b,j})\Delta\_{+}^{b}(y^{b,j})}\left(1+\log\left(\frac{w^{b}(t,y^{a,i},y^{b,j})}{w^{b}(t,y^{a,i},y^{b,j+1})}\right)\right). |  |

###### Remark 2.3.

In Avellaneda and Stoikov ([2008](#bib.bib14 "High-frequency trading in a limit order book")), the optimal strategy establishes a connection between 1/κ1/\kappa and the half spread in the market (κ\kappa is a parameter in their model controlling the price sensitivity of the order flow). Similar to their paper, in our setup the quantity

|  |  |  |
| --- | --- | --- |
|  | 1/(ka​Z±a,b​Δ±a,b),1/\Big(k^{a}\,Z^{a,b}\_{\pm}\Delta^{a,b}\_{\pm}\Big)\,, |  |

establishes a connection between kak^{a} and the typical fee charged in the pool.

## 3 Numerical results

Here, we use constant product market makers, i.e., the trading functions fi:ℝ+×ℝ+→ℝ+f^{i}:\mathbb{R}\_{+}\times\mathbb{R}\_{+}\to\mathbb{R}\_{+} is fi​(x,y)=x​yf^{i}(x,y)=xy and the level functions φ:ℝ+→ℝ+\varphi:\mathbb{R}\_{+}\to\mathbb{R}\_{+} are φi​(y)=(pi)2/y\varphi^{i}(y)=(p^{i})^{2}/y, for every i∈{a,b}i\in\{a,b\}. Moreover, we set the parameters as

|  |  |  |
| --- | --- | --- |
|  | (pi)2=108/4,λi,+=λi,−=50,ki,0=ki,j=2,(p^{i})^{2}=10^{8}/4,\quad\lambda^{i,+}=\lambda^{i,-}=50,\quad k^{i,0}=k^{i,j}=2, |  |

for every i∈{a,b}i\in\{a,b\} and j∈{a,b}∖{i}j\in\{a,b\}\setminus\{i\}. Moreover, we assume that the grids for the risky asset of two players are such that after every trade the exchange rate Zi​(y)Z^{i}(y) moves by 0.10.1. Specifically, the grids are given by the formula

|  |  |  |
| --- | --- | --- |
|  | yi,j:=(pi)2Zi​(yi,0)−0.1​j, for ​i∈{a,b}​j∈{−20,…,20}.y^{i,j}:=\sqrt{\frac{(p^{i})^{2}}{Z^{i}(y^{i,0})-0.1\,j}},\quad\quad\text{ for }i\in\{a,b\}\quad j\in\{-20,\dots,20\}. |  |

Finally, the time horizon is T=1T=1, the oracle price StS\_{t} to be S0=100S\_{0}=100 for t∈[0,T]t\in[0,T] and ya,0=yb,0=500y^{a,0}=y^{b,0}=500. Figure [1](#S3.F1 "Figure 1 ‣ 3 Numerical results ‣ Competition between DEXs through Dynamic Fees") shows the optimal fees for buying (dotted red line) and selling (continuous blue line) at time t=0.5t=0.5 for player aa.
This choice of parameters is consistent with that in Baggiani et al. ([2025](#bib.bib1 "Optimal dynamic fees in automated market makers")), allowing a direct comparison with the monopoly benchmark. In the latter, all liquidity is concentrated in a single pool, whereas here we analyze a duopoly in which the same aggregate liquidity is allocated across two pools, holding constant the market’s aggregate liquidity demand (and thus total traded volume) over the horizon.
The purple line indicates the level of yay^{a} for which the instantaneous exchange rate is equal to StS\_{t} while the green line indicates the instantaneous price of player bb. In the left plot the instantaneous exchange rate of the opponent Zb​(yb)Z^{b}(y^{b}) is the same as the oracle price, i.e., Zb​(yb)=St=100Z^{b}(y^{b})=S\_{t}=100. This situation corresponds to the case yb=500y^{b}=500. In the center plot the opponent exchange rate is Zb​(yb)=99.1Z^{b}(y^{b})=99.1 corresponding to the quantity yb=502y^{b}=502. Finally, in the right plot the opponent exchange rate is Zb​(yb)=101.1Z^{b}(y^{b})=101.1, corresponding to the quantity yb=497y^{b}=497. As in the monopoly case, the fees split into two regimes: one that penalizes arbitrageurs and another that amplifies noise-trader activity (thereby increasing volatility). The difference is that the crossing of the 𝔪a,∗\mathfrak{m}^{a,\*} and 𝔭a,∗\mathfrak{p}^{a,\*} takes place at a weighted average of the oracle price and the opponent’s exchange rate (as one can see in the second and third panels).

![Refer to caption](2603.09669v1/figures/OptimalFees.png)


Figure 1: Optimal fees for selling 𝔭a∗​(t,yt−)\mathfrak{p}^{\*}\_{a}(t,y\_{t-}) (solid line) and for buying 𝔪a∗​(t,yt−)\mathfrak{m}^{\*}\_{a}(t,y\_{t-}) (dashed line) at time t=0.5t=0.5 as a function of the quantity of asset YY in the pool.

Similarly to the monopoly case, the fees exhibit an approximately linear behaviour in the player’s inventory, especially in a neighbourhood of the weighted average of the oracle price and the opponent’s exchange rate. Figure [2](#S3.F2 "Figure 2 ‣ 3 Numerical results ‣ Competition between DEXs through Dynamic Fees") shows the linear approximations of the fees in the reference agent’s inventory. Below, we compare the performance of employing these linear approximations to the optimal fee structure.

![Refer to caption](2603.09669v1/figures/LinearFees.png)


Figure 2: Linear approximation of the fees for selling 𝔭a∗​(t,yt−)\mathfrak{p}^{\*}\_{a}(t,y\_{t-}) (solid line) and for buying 𝔪a∗​(t,yt−)\mathfrak{m}^{\*}\_{a}(t,y\_{t-}) (dashed line) at time t=0.5t=0.5 as a function of the quantity of asset YY in the pool.

Below we show two surfaces of the buy (panel [3(a)](#S3.F3.sf1 "Figure 3(a) ‣ Figure 3 ‣ 3 Numerical results ‣ Competition between DEXs through Dynamic Fees")) and sell (panel [3(b)](#S3.F3.sf2 "Figure 3(b) ‣ Figure 3 ‣ 3 Numerical results ‣ Competition between DEXs through Dynamic Fees")) fees as functions of the agent’s inventory (x-axis) and the opponent’s inventory (y-axis). Here t=0.5t=0.5, St=100S\_{t}=100 and we assume that yb=500y^{b}=500 (so that Zb​(yb)=100Z^{b}(y^{b})=100)

![Refer to caption](2603.09669v1/figures/3DPlotFeeBuy.png)


(a) Optimal fees for buying.

![Refer to caption](2603.09669v1/figures/3DPlotFeeSell.png)


(b) Optimal fees for selling.

Figure 3: Plots of the optimal fees for buying and selling as a function of the agent’s inventory (x-axis) and the opponent’s inventory (y-axis).

From these plots, we observe that the fees exhibit an approximately linear dependence on both arguments. The accuracy of this approximation is further supported by the numerical results reported in Tables [1](#S4.T1 "Table 1 ‣ 4 Simulations ‣ Competition between DEXs through Dynamic Fees") and [2](#S4.T2 "Table 2 ‣ 4 Simulations ‣ Competition between DEXs through Dynamic Fees").

Next, we examine how the optimal fees respond to changes in the sensitivity parameters ka,0k^{a,0} and ka,bk^{a,b} .
Figure [4](#S3.F4 "Figure 4 ‣ 3 Numerical results ‣ Competition between DEXs through Dynamic Fees") shows the buy and sell fees when ka,b=0.1k^{a,b}=0.1.
Two patterns emerge. First, the fee schedules approach the monopoly benchmark: the switching threshold between regimes moves closer to the oracle price. Second, the overall fee levels rise. This follows from the fact that the optimal fees scale inversely with the aggregate sensitivity ka=ka,0+ka,bk^{a}=k^{a,0}+k^{a,b}, that is,

|  |  |  |
| --- | --- | --- |
|  | 𝔭a,∗,𝔪a,∗∝1ka,0+ka,b.\mathfrak{p}^{a,\*},\,\mathfrak{m}^{a,\*}\ \propto\ \frac{1}{k^{a,0}+k^{a,b}}. |  |

Thus, a reduction in either sensitivity parameter, all else being equal, produces higher fees. This can be seen in Figures [4](#S3.F4 "Figure 4 ‣ 3 Numerical results ‣ Competition between DEXs through Dynamic Fees") and [5](#S3.F5 "Figure 5 ‣ 3 Numerical results ‣ Competition between DEXs through Dynamic Fees"), where we decrease ka,bk^{a,b} and ka,0k^{a,0} to 0.10.1, respectively.

![Refer to caption](2603.09669v1/figures/OptimalFeesExpDecayOpp=0.1.png)


Figure 4: Optimal fees for selling 𝔭a∗​(t,yt−)\mathfrak{p}^{\*}\_{a}(t,y\_{t-}) (solid line) and for buying 𝔪a∗​(t,yt−)\mathfrak{m}^{\*}\_{a}(t,y\_{t-}) (dashed line) at time t=0.5t=0.5 as a function of the quantity of asset YY in the pool for ka,b=0.1k^{a,b}=0.1.

![Refer to caption](2603.09669v1/figures/OptimalFeesExpDecOrac=0.1.png)


Figure 5: Optimal fees for selling 𝔭a∗​(t,yt−)\mathfrak{p}^{\*}\_{a}(t,y\_{t-}) (solid line) and for buying 𝔪a∗​(t,yt−)\mathfrak{m}^{\*}\_{a}(t,y\_{t-}) (dashed line) at time t=0.5t=0.5 as a function of the quantity of asset YY in the pool for ka,0=0.1k^{a,0}=0.1.

Finally, we examine how the fees respond to changes in the baseline order flow.
The next plots report the buy and sell fees when λ+=λ−=100\lambda^{+}=\lambda^{-}=100.
We observe smoother fee profiles and larger extreme values.
This follows from the fact that the venue expects more orders so it can afford to charge higher fees.

![Refer to caption](2603.09669v1/figures/OptimalFeesSensLambda.png)


Figure 6: Optimal fees for selling 𝔭a∗​(t,yt−)\mathfrak{p}^{\*}\_{a}(t,y\_{t-}) (solid line) and for buying 𝔪a∗​(t,yt−)\mathfrak{m}^{\*}\_{a}(t,y\_{t-}) (dashed line) at time t=0.5t=0.5 as a function of the quantity of asset YY in the pool for λ+,a=λ−,a=100\lambda^{+,a}=\lambda^{-,a}=100.

In the following plots we show how the fees behave through time as a function of yay^{a}, keeping SS and yby^{b} fixed. The following plots show the behaviour of the fees as a function of time (xx-axis) and quantity in the pool (colorbar) for different opponent exchange rates. As expected, the fees increase over time.

![Refer to caption](2603.09669v1/figures/Optimal_fees_through_time_fct_of_Q_t.png)


(a) Optimal fees for selling 𝔭t∗​(yt−a,yt−b)\mathfrak{p}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (solid line) and for buying 𝔪t∗​(yt−a,yt−b)\mathfrak{m}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (dashed line) at time t=0.5t=0.5 as a function of the quantity of asset YY (colorbar) for yt−b=500y\_{t-}^{b}=500 and S=100S=100.

![Refer to caption](2603.09669v1/figures/Optimal_fees_through_time_fct_of_Q_t_imb1.png)


(b) Optimal fees for selling 𝔭t∗​(yt−a,yt−b)\mathfrak{p}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (solid line) and for buying 𝔪t∗​(yt−a,yt−b)\mathfrak{m}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (dashed line) at time t=0.5t=0.5 as a function of the quantity of asset YY (colorbar) for yt−b=502y\_{t-}^{b}=502 and S=100S=100.

![Refer to caption](2603.09669v1/figures/Optimal_fees_through_time_fct_of_Q_t_imb2.png)


(c) Optimal fees for selling 𝔭t∗​(yt−a,yt−b)\mathfrak{p}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (solid line) and for buying 𝔪t∗​(yt−a,yt−b)\mathfrak{m}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (dashed line) at time t=0.5t=0.5 as a function of the quantity of asset YY (colorbar) for yt−b=497y\_{t-}^{b}=497 and S=100S=100.

These results resemble the behaviour of the optimal quotes of the market making problem (see Chapter 10 of Cartea et al. ([2015](#bib.bib15 "Algorithmic and high-frequency trading"))) and confirm the findings of Baggiani et al. ([2025](#bib.bib1 "Optimal dynamic fees in automated market makers")).

Finally, we plot the behaviour of the fees at a fixed time as a function of the centralised price StS\_{t}. We observe that the optimal fees are monotone in the oracle price StS\_{t} as the buy fee 𝔪t∗\mathfrak{m}\_{t}^{\ast} increases with StS\_{t}, while the sell fee 𝔭t∗\mathfrak{p}\_{t}^{\ast} decreases.
Intuitively, when StS\_{t} rises, buy-side arbitrage/flow into the pool becomes more attractive, so the venue raises
𝔪t∗\mathfrak{m}\_{t}^{\ast} to make buying more expensive and reduce that pressure; conversely it lowers 𝔭t∗\mathfrak{p}\_{t}^{\ast}
to keep the pool competitive for incoming sell orders. The opponent’s inventory shifts the level of the curves because it changes the opponent’s quote, therefore changing the weighted average of the centralised price and the opponent’s price.
The curves can intersect at values of StS\_{t} where two different inventory states imply the same effective mispricing.

![Refer to caption](2603.09669v1/figures/Optimal_fees_fct_of_St_fct_of_Q_t.png)


(a) Optimal fees for selling 𝔭t∗​(yt−a,yt−b)\mathfrak{p}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (solid line) and for buying 𝔪t∗​(yt−a,yt−b)\mathfrak{m}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (dashed line) at time t=0.5t=0.5 as functions of the oracle price StS\_{t} and yt−ay\_{t-}^{a} (colorbar) for yt−b=500y\_{t-}^{b}=500.

![Refer to caption](2603.09669v1/figures/Optimal_fees_fct_of_St_fct_of_Q_t_imb1.png)


(b) Optimal fees for selling 𝔭t∗​(yt−a,yt−b)\mathfrak{p}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (solid line) and for buying 𝔪t∗​(yt−a,yt−b)\mathfrak{m}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (dashed line) at time t=0.5t=0.5 as functions of the oracle price StS\_{t} and yt−ay\_{t-}^{a} (colorbar) for yt−b=503y\_{t-}^{b}=503.

![Refer to caption](2603.09669v1/figures/Optimal_fees_fct_of_St_fct_of_Q_t_imb2.png)


(c) Optimal fees for selling 𝔭t∗​(yt−a,yt−b)\mathfrak{p}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (solid line) and for buying 𝔪t∗​(yt−a,yt−b)\mathfrak{m}^{\*}\_{t}(y\_{t-}^{a},y\_{t-}^{b}) (dashed line) at time t=0.5t=0.5 as functions of the oracle price StS\_{t} and yt−ay\_{t-}^{a} (colorbar) for yt−b=497y\_{t-}^{b}=497.

## 4 Simulations

We now perform numerical simulations in a two-player setting and compare the results with the monopoly case. To ensure a *fair* comparison with the monopoly case the total depth is split between the two pools, and for simplicity we assume complete symmetry between the two pools.
The grid for the exchange rate ZZ is the same in both the monopoly and duopoly cases. In this case we set ki,0=ki,j=kk^{i,0}=k^{i,j}=k, where kk is the exponential decay parameter in the monopoly case. Moreover, we impose λi,+=λ+\lambda^{i,+}=\lambda^{+} and λi,−=λ−\lambda^{i,-}=\lambda^{-}.
If we take the grid for the risky asset yy as

|  |  |  |
| --- | --- | --- |
|  | yi,j:=(pi)2Zi​(yi,0)−0.1​j,i∈{a,b},j∈{−20,…,20},y^{i,j}:=\sqrt{\frac{(p^{i})^{2}}{Z^{i}(y^{i,0})-0.1\,j}},\qquad i\in\{a,b\},\quad j\in\{-20,\dots,20\}, |  |

then the resulting trade size is roughly half that of the monopoly case.
In this scenario, each venue receives a similar number of orders as in the monopoly case; however, each order is roughly half the size, so that the total traded volume (i.e. the sum of the volume traded in the first and in the second venue) is comparable to the total volume traded in the monopoly case. Tables [1](#S4.T1 "Table 1 ‣ 4 Simulations ‣ Competition between DEXs through Dynamic Fees") and [2](#S4.T2 "Table 2 ‣ 4 Simulations ‣ Competition between DEXs through Dynamic Fees") show the results of the simulations for the monopoly and duopoly cases with the parameters above. The number of simulations is 100,000100,000 and St=100S\_{t}=100 for simplicity. We compare the Nash equilibrium against the strategies:

* (i)(i)

  the *linear* strategy where both 𝔭i∗\mathfrak{p}^{\*}\_{i} and 𝔪i∗\mathfrak{m}^{\*}\_{i} are linearized around a neighborhood of (y0,a,y0,b)(y^{0,a},y^{0,b}) and
* (i​i)(ii)

  the *constant* strategy where both players set constant fees every time tt and every quantity yy. The constants cic^{i} are chosen as the average of the optimal two fees of player ii at t=0.5t=0.5 for yi=yi,0y^{i}=y^{i,0} and yj=yj,0y^{j}=y^{j,0}, i.e.,

  |  |  |  |
  | --- | --- | --- |
  |  | ci:=𝔭i∗​(0.5,ya,0,yb,0)+𝔪i∗​(0.5,ya,0,yb,0)2.c^{i}:=\frac{\mathfrak{p}^{\*}\_{i}(0.5,y^{a,0},y^{b,0})+\mathfrak{m}^{\*}\_{i}(0.5,y^{a,0},y^{b,0})}{2}. |  |

We see that the Nash equilibrium outperforms the constant case by between 5050 and 150150 bps. We see that the linear approximation of the fees provides an almost perfect approximation, indistinguishable after integer rounding. This is because trading takes place in a neighborhood of (y0,a,y0,b)(y^{0,a},y^{0,b}), as arbitrage aligns the pool prices with the oracle price StS\_{t}.
Finally, we see that the total values are similar between the monopoly and the two-player case.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | λ=100\lambda=100 | | | | λ=150\lambda=150 | | | |
| Player | Type | Fees | Sell | Buy | Vol | Fees | Sell | Buy | Vol |
| A | Optimal | 18.22 | 36.79 | 36.78 | 1839 | 27.13 | 54.77 | 54.75 | 2737 |
| Linear | 18.22 | 36.79 | 36.78 | 1839 | 27.13 | 54.77 | 54.75 | 2737 |
| Constant | 17.99 | 37.45 | 37.46 | 1872 | 26.72 | 55.80 | 55.81 | 2790 |
| B | Optimal | 18.23 | 36.79 | 36.79 | 1839 | 27.13 | 54.77 | 54.73 | 2737 |
| Linear | 18.23 | 36.79 | 36.79 | 1839 | 27.13 | 54.77 | 54.73 | 2737 |
| Constant | 17.99 | 37.44 | 37.45 | 1872 | 26.71 | 55.78 | 55.78 | 2789 |
| Total | Optimal | 36.45 | 73.58 | 73.57 | 3678 | 54.26 | 109.54 | 109.48 | 5474 |
| Linear | 36.45 | 73.58 | 73.57 | 3678 | 54.26 | 109.54 | 109.48 | 5474 |
| Constant | 35.98 | 74.89 | 74.91 | 3744 | 53.43 | 111.58 | 111.59 | 5579 |
| Monopoly | Optimal | 35.55 | 35.89 | 35.91 | 3590 | 52.97 | 53.45 | 53.47 | 5345 |
| Linear | 35.55 | 35.88 | 35.91 | 3589 | 52.97 | 53.44 | 53.48 | 5345 |
| Constant | 35.16 | 35.15 | 35.15 | 3653 | 52.26 | 52.26 | 52.26 | 5445 |

Table 1: Average fees collected (Fees), number of sell trades (Sell), number of buy trades (Buy), and volume traded (Vol) for players AA and BB under different fee types when k=2k=2, with λ∈{100,150}\lambda\in\{100,150\}.

As discussed in Remark [2.3](#S2.Thmtheorem3 "Remark 2.3. ‣ 2 Two-player model ‣ Competition between DEXs through Dynamic Fees"), optimal fee revenues scale approximately like 1/k1/k; hence, holding everything else fixed, increasing kk from 11 to 22 leads to roughly half the fee revenue. Moreover, when λ\lambda increases there is more order flow, so it is natural that optimal fees (and revenues) increase with λ\lambda, we show this in Table [2](#S4.T2 "Table 2 ‣ 4 Simulations ‣ Competition between DEXs through Dynamic Fees").

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | λ=100\lambda=100 | | | | λ=150\lambda=150 | | | |
| Player | Type | Fees | Sell | Buy | Vol | Fees | Sell | Buy | Vol |
| A | Optimal | 36.18 | 36.37 | 36.37 | 1818 | 53.85 | 54.12 | 54.13 | 2706 |
| Linear | 36.18 | 36.37 | 36.37 | 1818 | 53.85 | 54.12 | 54.13 | 2706 |
| Constant | 36.04 | 36.62 | 36.64 | 1831 | 53.56 | 54.54 | 54.58 | 2728 |
| B | Optimal | 36.19 | 36.37 | 36.38 | 1818 | 53.84 | 54.11 | 54.11 | 2705 |
| Linear | 36.19 | 36.37 | 36.38 | 1818 | 53.84 | 54.11 | 54.11 | 2705 |
| Constant | 36.04 | 36.62 | 36.64 | 1831 | 53.54 | 54.53 | 54.55 | 2727 |
| Total | Optimal | 72.37 | 72.74 | 72.75 | 3636 | 107.69 | 108.23 | 108.24 | 5411 |
| Linear | 72.37 | 72.74 | 72.75 | 3636 | 107.69 | 108.23 | 108.24 | 5411 |
| Constant | 72.08 | 73.24 | 73.28 | 3662 | 107.10 | 109.07 | 109.13 | 5455 |
| Monopoly | Optimal | 71.46 | 35.92 | 35.94 | 3593 | 106.38 | 53.47 | 53.50 | 5348 |
| Linear | 71.46 | 35.91 | 35.95 | 3593 | 106.38 | 53.46 | 53.50 | 5348 |
| Constant | 71.22 | 35.60 | 35.62 | 3618 | 105.90 | 52.94 | 52.96 | 5390 |

Table 2: Average fees collected (Fees), number of sell trades (Sell), number of buy trades (Buy), and volume traded (Vol) for players AA and BB under different fee types when k=1k=1, with λ∈{100,150}\lambda\in\{100,150\}.

Next we analyze the benefits of competition for the different parties involved. We first consider the point of view of a liquidity taker. Our goal is to understand whether a liquidity taker is better off trading in a world with two competing *venues* (playing the Nash equilibrium of the game), each with 500500 units of asset YY, or with only one with a total of 10001000 units of asset YY.

To do so, we consider two scenarios: (i) a strategic liquidity taker wishing to execute a trade of a fixed size DD, and (ii) the liquidity takers that arrive to the venues according to the stochastic intensities of the model. For the first scenario, when there is only one venue, the liquidity taker will send the trade of size DD to the venue and pay the corresponding fee. For the second scenario, the trade of size DD is split in two trades of size D/2D/2 and either he sends both trades to the first venue, both trades to the second venue, or one trade to each venue, depending on what is more advantageous at the time of sending the trades.

Second, we compute the *average slippage*, defined as the absolute deviation of the execution quote from the marginal exchange rate divided by the total traded volume. More precisely, we have that666Equivalently, slippage is the absolute distance of the fee-adjusted bid/ask rate from the oracle price at the trade time.

|  |  |  |
| --- | --- | --- |
|  | Avg-slippage:=𝔼​[∑i∈{a,b}∫0T(Zi​(yti)−Z+i,𝔭∗​(yti))​Δ+i​(yi)​dNti,++∫0T(Z−i,𝔪∗​(yti)−Zi​(yti))​Δ−i​(yi)​dNti,−∑i∈{a,b}∫0TΔ+i​(yti)​dNti,++∫0TΔ−i​(yti)​dNti,−].\displaystyle\text{Avg-slippage}:=\mathbb{E}\left[\frac{\sum\_{i\in\{a,b\}}\int\_{0}^{T}(Z^{i}(y^{i}\_{t})-Z\_{+}^{i,\mathfrak{p}^{\*}}(y^{i}\_{t}))\Delta^{i}\_{+}(y^{i})\,\mathrm{d}N^{i,+}\_{t}+\int\_{0}^{T}(Z\_{-}^{i,\mathfrak{m}^{\*}}(y^{i}\_{t})-Z^{i}(y^{i}\_{t}))\Delta^{i}\_{-}(y^{i})\,\mathrm{d}N^{i,-}\_{t}}{\sum\_{i\in\{a,b\}}\int\_{0}^{T}\Delta^{i}\_{+}(y^{i}\_{t})\,\mathrm{d}N^{i,+}\_{t}+\int\_{0}^{T}\Delta^{i}\_{-}(y^{i}\_{t})\,\mathrm{d}N^{i,-}\_{t}}\right]. |  |

We plot both quantities as a function of the market demand for liquidity, which we hold fixed and use as the xx-axis. From Figure ([9(a)](#S4.F9.sf1 "Figure 9(a) ‣ 4 Simulations ‣ Competition between DEXs through Dynamic Fees")) we observe two phenomena. First, competition benefits *strategic* liquidity takers who decide to trade at the best available price. Second, in the two-player case, the average *best* spread decreases as traded volume increases. We explain the tightening of the *best* quote under competition through order statistics. The best ask in the duopoly is a minimum across pools, while the best bid is a maximum across pools; increasing the dispersion of cross-sectional quotes mechanically decreases the expected minimum and increases the expected maximum. This is formalized by the following remark.

###### Remark 4.1.

If XX and YY two i.i.d. random variables such that 𝔼​[|X|2]<∞\mathbb{E}[|X|^{2}]<\infty with mean μ\mu and variance σ2\sigma^{2} then the quantity 𝔼​[min⁡(X,Y)]\mathbb{E}[\min(X,Y)] (resp. 𝔼​[max⁡(X,Y)]\mathbb{E}[\max(X,Y)]) is decreasing (resp. increasing) as a function of the standard deviation σ\sigma.

The average slippage in Figure ([9(b)](#S4.F9.sf2 "Figure 9(b) ‣ 4 Simulations ‣ Competition between DEXs through Dynamic Fees")) presents two distinct features. First, we notice that we can decompose the numerator of the average slippage as the convexity charge (which is not affected by the fees),

|  |  |  |
| --- | --- | --- |
|  | ∑i∈{a,b}∫0T(Zi​(yti)−Z+i​(yti))​Δ+i​(yi)​dNti,++∫0T(Z−i​(yti)−Zi​(yti))​Δ−i​(yi)​dNti,−,\sum\_{i\in\{a,b\}}\int\_{0}^{T}\bigl(Z^{i}(y^{i}\_{t})-Z\_{+}^{i}(y^{i}\_{t})\bigr)\,\Delta^{i}\_{+}(y^{i})\,\,\mathrm{d}N^{i,+}\_{t}\;+\;\int\_{0}^{T}\bigl(Z\_{-}^{i}(y^{i}\_{t})-Z^{i}(y^{i}\_{t})\bigr)\,\Delta^{i}\_{-}(y^{i})\,\,\mathrm{d}N^{i,-}\_{t}, |  |

plus the total cash collected (which is affected by the fees and hence differs between the one- and two-player cases),

|  |  |  |
| --- | --- | --- |
|  | ∫0t𝔭ui​Z+i,𝔭ui​(Yui,𝔣)​Δ+i​(Yti,𝔣)​dNui,+,𝔭i+∫0t𝔪ui​Z−i,𝔪ui​(Yui,𝔣)​Δ−i​(Yti,𝔣)​dNui,+,𝔪i.\int\_{0}^{t}\mathfrak{p}\_{u}^{i}\,Z\_{+}^{i,\mathfrak{p}\_{u}^{i}}\!\bigl(Y\_{u}^{i,\mathfrak{f}}\bigr)\,\Delta\_{+}^{i}\!\bigl(Y\_{t}^{i,\mathfrak{f}}\bigr)\,\,\mathrm{d}N^{i,+,\mathfrak{p}^{i}}\_{u}\;+\;\int\_{0}^{t}\mathfrak{m}^{i}\_{u}\,Z\_{-}^{i,\mathfrak{m}^{i}\_{u}}\!\bigl(Y\_{u}^{i,\mathfrak{f}}\bigr)\,\Delta\_{-}^{i}\!\bigl(Y\_{t}^{i,\mathfrak{f}}\bigr)\,\,\mathrm{d}N^{i,+,\mathfrak{m}^{i}}\_{u}. |  |

We next observe that the slippage is concave with respect to the total volume traded. It is decreasing because higher volume implies higher absolute cash revenue but lower relative cash revenue. This is because more volume traded implies higher volatility, which can be beneficial for the LP up to a certain point. However, a very high-volatility regime implies that the asset reaches the boundaries more often, and the boundaries are where the AMM does not charge any fees; this explains the concavity. In the two-player case, the number of times the asset reaches the inventory is more than double that of the one-player case, so the inventory is closer to the no-trading zone. Hence, in the two-player case the two players collect less money per unit of volume traded.

![Refer to caption](2603.09669v1/figures/Bid_ask_2_players.png)


(a) Strategic Bid–ask as a function of total traded volume in the monopoly (blue line) and duopoly (red line) case.

![Refer to caption](2603.09669v1/figures/avg_slippage_2_p.png)


(b) Average slippage as a function of total traded volume in the monopoly (blue line) and duopoly (red line) case.

Finally, we analyze whether the venue and the liquidity providers benefit from competition. We consider a setting in which a single venue (e.g. Uniswap) hosts both the monopoly and the two-player configurations and collects 10%10\% of the total fees earned by the liquidity providers in each case. In our setting, the venue is essentially indifferent to competition: because it collects a fixed amount of LP fees and total fees are unchanged between monopoly and duopoly, its revenue is the same in both cases. However, total revenue for a single LP declines under competition, since trading flow (and thus fee generation) is split across the two pools rather than concentrated in a single one. Combining these results with the previous one, we find that greater competition benefits strategic liquidity takers, while noise liquidity takers bear the cost.

![Refer to caption](2603.09669v1/figures/Total_revenue_2_players.png)


(a) Total revenue of the venue computed as the sum of a fixed percentage of the fee revenue of the players in the monopoly (blue line) and two-player (red line) case.

![Refer to caption](2603.09669v1/figures/rev_per_player_diff_liq_2p.png)


(b) Revenue per player as a function of total traded volume in the monopoly (blue line), two-player (red line) when liquidity is split among all participants.

###### Remark 4.2.

This parametrization is not unique. In particular, one may use an alternative canonical calibration that yields a fair comparison with the monopoly benchmark while relying on a different choice of parameters. In this second scenario, the grid for the risky asset yy is taken to be identical in the monopoly and duopoly settings. Consequently, the induced grid for the marginal price ZZ has a step size that is twice as large as in the monopoly case. This is natural: since liquidity is now split across two pools, each pool is shallower, and therefore a trade of a given size produces a larger marginal price impact.

Under this convention, we set ki,0=ki,j=k/2k^{i,0}=k^{i,j}=k/2, where kk denotes the exponential decay parameter in the monopoly case. In addition, let λi,+=λ+/2\lambda^{i,+}=\lambda^{+}/2 and λi,−=λ−/2\lambda^{i,-}=\lambda^{-}/2. We tested the numerical results under both parameter conventions and the resulting outputs are of the same order of magnitude. We therefore omit the redundant figures and tables for brevity.777See the project repository for the corresponding code and additional numerical checks.

## 5 Conclusion

In this paper, we studied dynamic fee competition between DEXs and characterised an approximate Nash equilibrium. We found that equilibrium fees alternate between deterring arbitrage and attracting noise-driven trading, but competition shifts the threshold where this change happens from the oracle price to a weighted combination of the oracle and the competing pool’s exchange rate. Moreover, we found that these changes benefit strategic liquidity takers while harming liquidity providers; as for noise liquidity takers whether or not they are better off depends on the level of market activity.
  
Future research could extend our framework along three main directions. First, by introducing a strategic liquidity provider who jointly chooses fees and an optimal initial liquidity, adjusting provision in response to equilibrium fee schedules. Second, it would be valuable to study the infinite-player limit game, to understand how our alternating-fee equilibrium and the weighted benchmark threshold behave under near-perfect competition. Finally, an important step is to generalize the analysis to concentrated-liquidity AMMs (e.g., Uniswap V3).

## Appendix A Multiple-player model

We now extend our theory to the case where there are MM players. The players will be denoted with a number i∈{1,…,M}i\in\{1,\dots,M\}.
For each player ii the controlled intensities of the processes
{Ni,−,𝔪t}t∈[0,T]\{N^{i,-,\mathfrak{m}\_{t}}\}\_{t\in[0,T]} and {Ni,+,𝔭t}t∈[0,T]\{N^{i,+,\mathfrak{p}\_{t}}\}\_{t\in[0,T]} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | λti,−,𝔣\displaystyle\lambda\_{t}^{i,-,\mathfrak{f}} | :=λi,−​exp⁡(ki,0​((St−ζ)−Z−i,𝔪i​(Yti,𝔣))​Δ−i​(Yti,𝔣)+∑j=1j≠iMki,j​(Z−j​(Ytj,𝔣)−Z−i,𝔪i​(Yti,𝔣))​Δ−i​(Yti,𝔣))​𝟙{Yti,𝔣>y¯i}\displaystyle:=\lambda^{i,-}\exp{\left(k^{i,0}((S\_{t}-\zeta)-Z\_{-}^{i,\mathfrak{m}^{i}}(Y\_{t}^{i,\mathfrak{f}}))\Delta\_{-}^{i}(Y\_{t}^{i,\mathfrak{f}})+\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}k^{i,j}(Z\_{-}^{j}(Y\_{t}^{j,\mathfrak{f}})-Z\_{-}^{i,\mathfrak{m}^{i}}(Y\_{t}^{i,\mathfrak{f}}))\Delta\_{-}^{i}(Y\_{t}^{i,\mathfrak{f}})\right)}\mathbbm{1}\_{\{Y\_{t}^{i,\mathfrak{f}}>\underline{y}^{i}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λti,+,𝔣\displaystyle\lambda\_{t}^{i,+,\mathfrak{f}} | :=λi,+​exp⁡(ki,0​(Z+i,𝔭i​(Yti,𝔣)−(St+ζ))​Δ+i​(Yti,𝔣)+∑j=1j≠iMki,j​(Z+i,𝔭i​(Yti,𝔣)−Z+j​(Ytj,𝔣))​Δ+i​(Yti,𝔣))​𝟙{Yti,𝔣<y¯i}\displaystyle:=\lambda^{i,+}\exp{\left(k^{i,0}(Z\_{+}^{i,\mathfrak{p}^{i}}(Y\_{t}^{i,\mathfrak{f}})-(S\_{t}+\zeta))\Delta\_{+}^{i}(Y\_{t}^{i,\mathfrak{f}})+\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}k^{i,j}(Z\_{+}^{i,\mathfrak{p}^{i}}(Y\_{t}^{i,\mathfrak{f}})-Z\_{+}^{j}(Y\_{t}^{j,\mathfrak{f}}))\Delta\_{+}^{i}(Y\_{t}^{i,\mathfrak{f}})\right)}\mathbbm{1}\_{\{Y\_{t}^{i,\mathfrak{f}}<\overline{y}^{i}\}} |  |

The interpretations are the same as in the two-player case. We establish some notation, for each i∈{1,…,M}i\in\{1,\dots,M\} we call 𝔣i=(𝔪i,𝔭i)\mathfrak{f}^{i}=(\mathfrak{m}^{i},\mathfrak{p}^{i}), 𝔪=(𝔪1,…,𝔪M)\mathfrak{m}=(\mathfrak{m}^{1},\dots,\mathfrak{m}^{M}) and 𝔭=(𝔭1,…,𝔭M)\mathfrak{p}=(\mathfrak{p}^{1},\dots,\mathfrak{p}^{M}) 𝔣=(𝔣1,…​𝔣M)\mathfrak{f}=(\mathfrak{f}^{1},\dots\mathfrak{f}^{M}).

For each i∈{1,…,M}i\in\{1,\dots,M\} the cumulative fees {ℭti,𝔣i}t∈[0,T]\{\mathfrak{C}\_{t}^{i,\mathfrak{f}^{i}}\}\_{t\in[0,T]} collected by the pool ii are in turn given by

|  |  |  |
| --- | --- | --- |
|  | ℭti,𝔣i:=∫0t𝔭ui​Z+i,𝔭ui​(Yui,𝔣)​Δ+i​(Yti,𝔣)​dNui,+,𝔭i+∫0t𝔪ui​Z−i,𝔪ui​(Yui,𝔣)​Δ−i​(Yti,𝔣)​dNui,+,𝔪i,t∈[0,T],\mathfrak{C}\_{t}^{i,\mathfrak{f}^{i}}:=\int\_{0}^{t}\mathfrak{p}\_{u}^{i}Z\_{+}^{i,\mathfrak{p}\_{u}^{i}}(Y\_{u}^{i,\mathfrak{f}})\Delta\_{+}^{i}(Y\_{t}^{i,\mathfrak{f}})\,\mathrm{d}N^{i,+,\mathfrak{p}^{i}}\_{u}+\int\_{0}^{t}\mathfrak{m}^{i}\_{u}Z\_{-}^{i,\mathfrak{m}^{i}\_{u}}(Y\_{u}^{i,\mathfrak{f}})\Delta\_{-}^{i}(Y\_{t}^{i,\mathfrak{f}})\,\mathrm{d}N^{i,+,\mathfrak{m}^{i}}\_{u},\quad\quad t\in[0,T], |  |

Each pool seeks to solve the control problems

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωi​(t,s,𝔠i,y1,…,yM)\displaystyle\omega^{i}(t,s,\mathfrak{c}^{i},y^{1},\dots,y^{M}) | :=sup𝔣i∈𝒜tω(i,𝔣i)​(t,s,𝔠i,y1,…,yM)\displaystyle:=\sup\_{\mathfrak{f}^{i}\in\mathcal{A}\_{t}}\omega^{(i,\mathfrak{f}^{i})}(t,s,\mathfrak{c}^{i},y^{1},\dots,y^{M}) |  |

where 𝒜t\mathcal{A}\_{t} denotes the set of all 𝔽\mathbb{F}-predictable and bounded fee structure processes (𝔪ui,𝔭ui){t≤u≤T}(\mathfrak{m}\_{u}^{i},\mathfrak{p}\_{u}^{i})\_{\{t\leq u\leq T\}} and the conditional performance criterion are given by

|  |  |  |
| --- | --- | --- |
|  | ωi​(t,s,𝔠i,y1,…,yM):=𝔼(t,s,𝔠a,y1,…,yM)​[ℭT(i,t,s,𝔠i,y1,…,yM,𝔣i)],i∈{1,…,M}\omega^{i}(t,s,\mathfrak{c}^{i},y^{1},\dots,y^{M}):=\mathbb{E}\_{(t,s,\mathfrak{c}^{a},y^{1},\dots,y^{M})}\left[\mathfrak{C}\_{T}^{(i,t,s,\mathfrak{c}^{i},y^{1},\dots,y^{M},\mathfrak{f}^{i})}\right],\quad i\in\{1,\dots,M\} |  |

Here, for each i∈{1,…,M}i\in\{1,\dots,M\},

|  |  |  |
| --- | --- | --- |
|  | {ℭu(i,t,s,𝔠i,y1,…,yM,𝔣i)}u∈[t,T],{Yu(i,t,s,𝔠i,y1,…,yM,𝔣i)}u∈[t,T],{Su(i,t,s,𝔠i,y1,…,yM)}u∈[t,T]\big\{\mathfrak{C}\_{u}^{(i,t,s,\mathfrak{c}^{i},y^{1},\dots,y^{M},\mathfrak{f}^{i})}\big\}\_{u\in[t,T]},\quad\big\{Y\_{u}^{(i,t,s,\mathfrak{c}^{i},y^{1},\dots,y^{M},\mathfrak{f}^{i})}\big\}\_{u\in[t,T]},\quad\big\{S\_{u}^{(i,t,s,\mathfrak{c}^{i},y^{1},\dots,y^{M})}\big\}\_{u\in[t,T]} |  |

denote the (controlled) processes ℭi\mathfrak{C}^{i}, YiY^{i}, and SS restarted at time tt with initial values 𝔠i\mathfrak{c}^{i}, y1,…,yMy^{1},\dots,y^{M}, and ss, respectively. Clearly all the value functions are linear in 𝔠i\mathfrak{c}^{i} and we denote with viv^{i} the value function after the linear ansatz for 𝔠i\mathfrak{c}^{i}. From the dynamic programming principle, we determine that the Hamilton-Jacobi-Bellman (HJB) for the value function of the player ii is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=\displaystyle 0\;=\; | ∂∂t​vi​(t,s,y1,…,yM)+σ22​∂2∂s2​vi​(t,s,y1,…,yM)\displaystyle\frac{\partial}{\partial t}\,v^{i}(t,s,y^{1},\dots,y^{M})\;+\;\frac{\sigma^{2}}{2}\,\frac{\partial^{2}}{\partial s^{2}}v^{i}(t,s,y^{1},\dots,y^{M}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +sup𝔪i∈ℝλi,−​eki​(ki,0ki​s+∑j=1j≠iMki,jki​Z−j​(yj)−(1+𝔪i)​Z−i​(yi))​Δ−i​(yi)​(vi​(t,s,yi,−)−vi​(t,s,y)+𝔪i​Z−i​(yi)​Δ−i​(yi))​ 1{yi>y¯i}\displaystyle\;+\;\sup\_{\mathfrak{m}^{i}\in\mathbb{R}}\lambda^{i,-}\,e^{\,k^{i}\!\left(\tfrac{k^{i,0}}{k^{i}}s+\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\tfrac{k^{i,j}}{k^{i}}\,Z\_{-}^{j}(y^{j})-(1+\mathfrak{m}^{i})\,Z\_{-}^{i}(y^{i})\right)\Delta\_{-}^{i}(y^{i})}\,\Big(v^{i}(t,s,y^{i,-})-v^{i}(t,s,y)+\mathfrak{m}^{i}\,Z\_{-}^{i}(y^{i})\,\Delta\_{-}^{i}(y^{i})\Big)\,\mathbbm{1}\_{\{y^{i}>\underline{y}^{i}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +sup𝔭i∈ℝλi,+​eki​((1−𝔭i)​Z+i​(yi)−ki,0ki​s−∑j=1j≠iMki,jki​Z+j​(yj))​Δ+i​(yi)​(vi​(t,s,yi,+)−vi​(t,s,y)+𝔭i​Z+i​(yi)​Δ+i​(yi))​ 1{yi<y¯i}\displaystyle\;+\;\sup\_{\mathfrak{p}^{i}\in\mathbb{R}}\lambda^{i,+}\,e^{\,k^{i}\!\left((1-\mathfrak{p}^{i})\,Z\_{+}^{i}(y^{i})-\tfrac{k^{i,0}}{k^{i}}s-\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\tfrac{k^{i,j}}{k^{i}}\,Z\_{+}^{j}(y^{j})\right)\Delta\_{+}^{i}(y^{i})}\,\Big(v^{i}(t,s,y^{i,+})-v^{i}(t,s,y)+\mathfrak{p}^{i}\,Z\_{+}^{i}(y^{i})\,\Delta\_{+}^{i}(y^{i})\Big)\,\mathbbm{1}\_{\{y^{i}<\overline{y}^{i}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑j=1j≠iMλj,−​ekj​(kj,0kj​s+∑ℓ=1ℓ≠jMkj,ℓkj​Z−ℓ​(yℓ)−(1+𝔪j)​Z−j​(yj))​Δ−j​(yj)​(vi​(t,s,yj,−)−vi​(t,s,y))​ 1{yj>y¯j}\displaystyle\;+\;\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\lambda^{j,-}\,e^{\,k^{j}\!\left(\tfrac{k^{j,0}}{k^{j}}s+\sum\_{\begin{subarray}{c}\ell=1\\ \ell\neq j\end{subarray}}^{M}\tfrac{k^{j,\ell}}{k^{j}}\,Z\_{-}^{\ell}(y^{\ell})-(1+\mathfrak{m}^{j})\,Z\_{-}^{j}(y^{j})\right)\Delta\_{-}^{j}(y^{j})}\,\Big(v^{i}(t,s,y^{j,-})-v^{i}(t,s,y)\Big)\,\mathbbm{1}\_{\{y^{j}>\underline{y}^{j}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑j=1j≠iMλj,+​ekj​((1−𝔭j)​Z+j​(yj)−kj,0kj​s−∑ℓ=1ℓ≠jMkj,ℓkj​Z+ℓ​(yℓ))​Δ+j​(yj)​(vi​(t,s,yj,+)−vi​(t,s,y))​ 1{yj<y¯j}.\displaystyle\;+\;\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\lambda^{j,+}\,e^{\,k^{j}\!\left((1-\mathfrak{p}^{j})\,Z\_{+}^{j}(y^{j})-\tfrac{k^{j,0}}{k^{j}}s-\sum\_{\begin{subarray}{c}\ell=1\\ \ell\neq j\end{subarray}}^{M}\tfrac{k^{j,\ell}}{k^{j}}\,Z\_{+}^{\ell}(y^{\ell})\right)\Delta\_{+}^{j}(y^{j})}\,\Big(v^{i}(t,s,y^{j,+})-v^{i}(t,s,y)\Big)\,\mathbbm{1}\_{\{y^{j}<\overline{y}^{j}\}}. |  |

Here ki:=ki,0+∑j=1j≠iMki,jk^{i}:=k^{i,0}+\sum\_{\begin{subarray}{c}j=1\\
j\neq i\end{subarray}}^{M}k^{i,j} for each i∈{1,…,M}i\in\{1,\dots,M\}, and we use the shorthand

|  |  |  |
| --- | --- | --- |
|  | yj,−:=(y1,…,yj−Δ−j​(yj),…,yM),yj,+:=(y1,…,yj+Δ+j​(yj),…,yM).y^{j,-}:=(y^{1},\dots,y^{j}-\Delta\_{-}^{j}(y^{j}),\dots,y^{M}),\qquad y^{j,+}:=(y^{1},\dots,y^{j}+\Delta\_{+}^{j}(y^{j}),\dots,y^{M}). |  |

The terminal condition is vi​(T,s,y1,…,yM)=0v^{i}(T,s,y^{1},\dots,y^{M})=0.
  
First order condition on the maximizer yields, for every i∈{1,…​M}i\in\{1,\dots M\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔪i,∗​(t,s,y1,…,yM)\displaystyle\mathfrak{m}^{i,\*}(t,s,y^{1},\dots,y^{M}) | =1+ki​(vi​(t,s,y1,…,yM)−vi​(t,s,yi,−))ki​Z−i​(yi)​Δ−i​(yi),\displaystyle=\frac{1+k^{i}\big(v^{i}(t,s,y^{1},\dots,y^{M})-v^{i}(t,s,y^{i,-})\big)}{k^{i}\,Z\_{-}^{i}(y^{i})\,\Delta\_{-}^{i}(y^{i})}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔭i,∗​(t,s,y1,…,yM)\displaystyle\mathfrak{p}^{i,\*}(t,s,y^{1},\dots,y^{M}) | =1+ki​(vi​(t,s,y1,…,yM)−vi​(t,s,yi,+))ki​Z+i​(yi)​Δ+i​(yi).\displaystyle=\frac{1+k^{i}\big(v^{i}(t,s,y^{1},\dots,y^{M})-v^{i}(t,s,y^{i,+})\big)}{k^{i}\,Z\_{+}^{i}(y^{i})\,\Delta\_{+}^{i}(y^{i})}. |  |

plugging back into the original equation yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=\displaystyle 0\;=\; | ∂∂t​vi​(t,s,y1,…,yM)+σ22​∂2∂s2​vi​(t,s,y1,…,yM)\displaystyle\frac{\partial}{\partial t}v^{i}(t,s,y^{1},\dots,y^{M})\;+\;\frac{\sigma^{2}}{2}\,\frac{\partial^{2}}{\partial s^{2}}v^{i}(t,s,y^{1},\dots,y^{M}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λi,−​eki​(ki,0ki​s+∑j=1j≠iMki,jki​Z−j​(yj))​Δ−i​(yi)−1ki​e−ki​Z−i​(yi)​Δ−i​(yi)​eki​(vi​(t,s,yi,−)−vi​(t,s,y))​ 1{yi>y¯i}\displaystyle\;+\;\frac{\lambda^{i,-}\,e^{\,k^{i}\!\left(\tfrac{k^{i,0}}{k^{i}}s+\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\tfrac{k^{i,j}}{k^{i}}\,Z\_{-}^{j}(y^{j})\right)\Delta\_{-}^{i}(y^{i})-1}}{k^{i}}\;e^{-\,k^{i}\,Z\_{-}^{i}(y^{i})\,\Delta\_{-}^{i}(y^{i})}\;e^{\,k^{i}\,\big(v^{i}(t,s,y^{i,-})-v^{i}(t,s,y)\big)}\;\mathbbm{1}\_{\{y^{i}>\underline{y}^{i}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑j=1j≠iMλj,−​ekj​(kj,0kj​s+∑ℓ=1ℓ≠jMkj,ℓkj​Z−ℓ​(yℓ))​Δ−j​(yj)−1​e−kj​Z−j​(yj)​Δ−j​(yj)​ekj​(vj​(t,s,yj,−)−vj​(t,s,y))\displaystyle\;+\;\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\lambda^{j,-}\,e^{\,k^{j}\!\left(\tfrac{k^{j,0}}{k^{j}}s+\sum\_{\begin{subarray}{c}\ell=1\\ \ell\neq j\end{subarray}}^{M}\tfrac{k^{j,\ell}}{k^{j}}\,Z\_{-}^{\ell}(y^{\ell})\right)\Delta\_{-}^{j}(y^{j})-1}\;e^{-\,k^{j}\,Z\_{-}^{j}(y^{j})\,\Delta\_{-}^{j}(y^{j})}\;e^{\,k^{j}\,\big(v^{j}(t,s,y^{j,-})-v^{j}(t,s,y)\big)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(vi​(t,s,yj,−)−vi​(t,s,y))​ 1{yj>y¯j}\displaystyle\hskip 46.2497pt\times\big(v^{i}(t,s,y^{j,-})-v^{i}(t,s,y)\big)\;\mathbbm{1}\_{\{y^{j}>\underline{y}^{j}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λi,+​e−ki​(ki,0ki​s+∑j=1j≠iMki,jki​Z+j​(yj))​Δ+i​(yi)−1ki​eki​Z+i​(yi)​Δ+i​(yi)​eki​(vi​(t,s,yi,+)−vi​(t,s,y))​ 1{yi<y¯i}\displaystyle\;+\;\frac{\lambda^{i,+}\,e^{-\,k^{i}\!\left(\tfrac{k^{i,0}}{k^{i}}s+\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\tfrac{k^{i,j}}{k^{i}}\,Z\_{+}^{j}(y^{j})\right)\Delta\_{+}^{i}(y^{i})-1}}{k^{i}}\;e^{\,k^{i}\,Z\_{+}^{i}(y^{i})\,\Delta\_{+}^{i}(y^{i})}\;e^{\,k^{i}\,\big(v^{i}(t,s,y^{i,+})-v^{i}(t,s,y)\big)}\;\mathbbm{1}\_{\{y^{i}<\overline{y}^{i}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑j=1j≠iMλj,+​e−kj​(kj,0kj​s+∑ℓ=1ℓ≠jMkj,ℓkj​Z+ℓ​(yℓ))​Δ+j​(yj)−1​ekj​Z+j​(yj)​Δ+j​(yj)​ekj​(vj​(t,s,yj,+)−vj​(t,s,y))\displaystyle\;+\;\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\lambda^{j,+}\,e^{-\,k^{j}\!\left(\tfrac{k^{j,0}}{k^{j}}s+\sum\_{\begin{subarray}{c}\ell=1\\ \ell\neq j\end{subarray}}^{M}\tfrac{k^{j,\ell}}{k^{j}}\,Z\_{+}^{\ell}(y^{\ell})\right)\Delta\_{+}^{j}(y^{j})-1}\;e^{\,k^{j}\,Z\_{+}^{j}(y^{j})\,\Delta\_{+}^{j}(y^{j})}\;e^{\,k^{j}\,\big(v^{j}(t,s,y^{j,+})-v^{j}(t,s,y)\big)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(vi​(t,s,yj,+)−vi​(t,s,y))​ 1{yj<y¯j},\displaystyle\hskip 46.2497pt\times\big(v^{i}(t,s,y^{j,+})-v^{i}(t,s,y)\big)\;\mathbbm{1}\_{\{y^{j}<\overline{y}^{j}\}}, |  |

where ki:=ki,0+∑j=1j≠iMki,jk^{i}:=k^{i,0}+\sum\_{\begin{subarray}{c}j=1\\
j\neq i\end{subarray}}^{M}k^{i,j} for each i=1,…,Mi=1,\dots,M. We now make a few assumptions to compute an approximate solution. First, we treat the CEX price StS\_{t} as a parameter. Second, we assume that a change in one agent’s inventory has a negligible effect on any other agent’s value function at first order.
For a fixed player i∈{1,…,M}i\in\{1,\dots,M\} and any j≠ij\neq i,

|  |  |  |  |
| --- | --- | --- | --- |
|  | vi​(t,y1,…,yj+Δ+j​(yj),…,yM)\displaystyle v^{i}\bigl(t,y^{1},\dots,y^{j}+\Delta\_{+}^{j}(y^{j}),\dots,y^{M}\bigr) | ≈vi​(t,y1,…,yM),\displaystyle\approx v^{i}\bigl(t,y^{1},\dots,y^{M}\bigr), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | vi​(t,y1,…,yj−Δ−j​(yj),…,yM)\displaystyle v^{i}\bigl(t,y^{1},\dots,y^{j}-\Delta\_{-}^{j}(y^{j}),\dots,y^{M}\bigr) | ≈vi​(t,y1,…,yM).\displaystyle\approx v^{i}\bigl(t,y^{1},\dots,y^{M}\bigr). |  |

Under these assumptions, viv^{i} no longer depends on ss and we write vi​(t,y1,…,yM)v^{i}(t,y^{1},\dots,y^{M}).
Plugging the maximizers and the HJB for player ii reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =λi,−ki​exp⁡(ki​(ki,0ki​s+∑j=1j≠iMki,jki​Z−j​(yj))​Δ−i​(yi)−1)​exp⁡(−ki​Z−i​(yi)​Δ−i​(yi))\displaystyle=\frac{\lambda^{i,-}}{k^{i}}\exp\!\Big(k^{i}\Big(\tfrac{k^{i,0}}{k^{i}}\,s+\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\tfrac{k^{i,j}}{k^{i}}\,Z\_{-}^{j}(y^{j})\Big)\Delta\_{-}^{i}(y^{i})-1\Big)\,\exp\!\big(-k^{i}Z\_{-}^{i}(y^{i})\Delta\_{-}^{i}(y^{i})\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡(ki​[vi​(t,y1,…,yi−Δ−i​(yi),…,yM)−vi​(t,y1,…,yM)])​ 1{yi>y¯i}\displaystyle\qquad\times\exp\!\Big(k^{i}\big[v^{i}(t,y^{1},\dots,y^{i}-\Delta\_{-}^{i}(y^{i}),\dots,y^{M})-v^{i}(t,y^{1},\dots,y^{M})\big]\Big)\,\mathbbm{1}\_{\{y^{i}>\underline{y}^{i}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λi,+ki​exp⁡(−ki​(ki,0ki​s+∑j=1j≠iMki,jki​Z+j​(yj))​Δ+i​(yi)−1)​exp⁡(ki​Z+i​(yi)​Δ+i​(yi))\displaystyle\;+\;\frac{\lambda^{i,+}}{k^{i}}\exp\!\Big(-\,k^{i}\Big(\tfrac{k^{i,0}}{k^{i}}\,s+\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\tfrac{k^{i,j}}{k^{i}}\,Z\_{+}^{j}(y^{j})\Big)\Delta\_{+}^{i}(y^{i})-1\Big)\,\exp\!\big(k^{i}Z\_{+}^{i}(y^{i})\Delta\_{+}^{i}(y^{i})\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡(ki​[vi​(t,y1,…,yi+Δ+i​(yi),…,yM)−vi​(t,y1,…,yM)])​ 1{yi<y¯i}\displaystyle\qquad\times\exp\!\Big(k^{i}\big[v^{i}(t,y^{1},\dots,y^{i}+\Delta\_{+}^{i}(y^{i}),\dots,y^{M})-v^{i}(t,y^{1},\dots,y^{M})\big]\Big)\,\mathbbm{1}\_{\{y^{i}<\overline{y}^{i}\}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∂∂t​vi​(t,y1,…,yM).\displaystyle\;+\;\frac{\partial}{\partial t}\,v^{i}(t,y^{1},\dots,y^{M}). |  | (A.1) |

we introduce, for each i∈{1,…,M}i\in\{1,\dots,M\},

|  |  |  |
| --- | --- | --- |
|  | eki​vi​(t,y1,…,yM):=wi​(t,y1,…,yM),so thatwi​(T,y1,…,yM)=1.e^{\,k^{i}v^{i}(t,y^{1},\dots,y^{M})}\;:=\;w^{i}(t,y^{1},\dots,y^{M}),\qquad\text{so that}\qquad w^{i}(T,y^{1},\dots,y^{M})=1. |  |

With this change of variables, the HJB equation for player ii becomes linear:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=\displaystyle 0\;=\; | ∂∂t​wi​(t,y1,…,yM)\displaystyle\frac{\partial}{\partial t}\,w^{i}\!\bigl(t,y^{1},\dots,y^{M}\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λi,−​exp⁡(ki​(ki,0ki​S0+∑j=1j≠iMki,jki​Z−j​(yj))​Δ−i​(yi)−1)​exp⁡(−ki​Z−i​(yi)​Δ−i​(yi))\displaystyle\;+\;\lambda^{i,-}\;\exp\!\Biggl(k^{i}\!\left(\frac{k^{i,0}}{k^{i}}\,S\_{0}+\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\frac{k^{i,j}}{k^{i}}\,Z\_{-}^{j}(y^{j})\right)\!\Delta\_{-}^{i}(y^{i})-1\Biggr)\,\exp\!\Bigl(-k^{i}\,Z\_{-}^{i}(y^{i})\,\Delta\_{-}^{i}(y^{i})\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×wi​(t,y1,…,yi−Δ−i​(yi),…,yM)​ 1{yi>y¯i}\displaystyle\hskip 18.49988pt\times\;w^{i}\!\bigl(t,y^{1},\dots,y^{i}-\Delta\_{-}^{i}(y^{i}),\dots,y^{M}\bigr)\;\mathbbm{1}\_{\{y^{i}>\underline{y}^{i}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λi,+​exp⁡(−ki​(ki,0ki​S0+∑j=1j≠iMki,jki​Z+j​(yj))​Δ+i​(yi)−1)​exp⁡(+ki​Z+i​(yi)​Δ+i​(yi))\displaystyle\;+\;\lambda^{i,+}\;\exp\!\Biggl(-\,k^{i}\!\left(\frac{k^{i,0}}{k^{i}}\,S\_{0}+\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{M}\frac{k^{i,j}}{k^{i}}\,Z\_{+}^{j}(y^{j})\right)\!\Delta\_{+}^{i}(y^{i})-1\Biggr)\,\exp\!\Bigl(+k^{i}\,Z\_{+}^{i}(y^{i})\,\Delta\_{+}^{i}(y^{i})\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×wi​(t,y1,…,yi+Δ+i​(yi),…,yM)​ 1{yi<y¯i}.\displaystyle\hskip 18.49988pt\times\;w^{i}\!\bigl(t,y^{1},\dots,y^{i}+\Delta\_{+}^{i}(y^{i}),\dots,y^{M}\bigr)\;\mathbbm{1}\_{\{y^{i}<\overline{y}^{i}\}}. |  |

The formal result is summarized in the following theorem

###### Theorem A.1.

Fix an index h∈{1,…,M}h\in\{1,\dots,M\} and a multindex l∈⨂j=1j≠iM{−Nj,…,Nj}l\in\bigotimes\_{\begin{subarray}{c}j=1\\
j\neq i\end{subarray}}^{M}\{-N^{j},\dots,N^{j}\}. Denote with 𝐲l\mathbf{y}^{l} the vector

|  |  |  |
| --- | --- | --- |
|  | 𝐲l:=(y1,l1,…,yi−1,li−1,yi+1,li+1,…,yM,lM).\mathbf{y}^{l}:=(y^{1,l^{1}},\dots,y^{i-1,l^{i-1}},y^{i+1,l^{i+1}},\dots,y^{M,l^{M}}). |  |

Define the matrix 𝐀h,l:=(𝐀i,jl)0≤i≤j≤2​Ni\mathbf{A}^{h,l}:=(\mathbf{A}^{l}\_{i,j})\_{0\leq i\leq j\leq 2N^{i}} by

|  |  |  |
| --- | --- | --- |
|  | 𝐀i,jh​(𝐲l):={λi,+​exp⁡(−kh​(kh,0kh​S0+∑m=1m≠iMkh,mkh​Z+m​(ym,lm))​Δ+h​(yh,j−Nh)−1)×exp(khZ+h(yh,j−Nh)Δ+h(yh,j−Nh)),if i=j−1,λi,−​exp⁡(kh​(kh,0kh​S0+∑m=1m≠iMkh,mkh​Z−m​(ym,lm))​Δ−h​(yh,j−Nh)−1)×exp(−khZ−h(yh,j−Nh)Δ−h(yh,j−Nh)),if i=j+1,0,otherwise.\displaystyle\mathbf{A}^{h}\_{i,j}(\mathbf{y}^{l})\;:=\;\left\{\begin{array}[]{@{}l@{}}\lambda^{i,+}\,\exp\!\Bigg(-\,k^{h}\!\Big(\frac{k^{h,0}}{k^{h}}\,S\_{0}+\sum\_{\begin{subarray}{c}m=1\\ m\neq i\end{subarray}}^{M}\frac{k^{h,m}}{k^{h}}\,Z\_{+}^{m}(y^{m,l^{m}})\Big)\,\Delta\_{+}^{h}(y^{h,j-N^{h}})-1\Bigg)\\ \hskip 18.49988pt\times\exp\!\Big(k^{h}\,Z\_{+}^{h}(y^{h,j-N^{h}})\,\Delta\_{+}^{h}(y^{h,j-N^{h}})\Big),\qquad\text{if }i=j-1,\\[8.0pt] \lambda^{i,-}\,\exp\!\Bigg(\;\;k^{h}\!\Big(\frac{k^{h,0}}{k^{h}}\,S\_{0}+\sum\_{\begin{subarray}{c}m=1\\ m\neq i\end{subarray}}^{M}\frac{k^{h,m}}{k^{h}}\,Z\_{-}^{m}(y^{m,l^{m}})\Big)\,\Delta\_{-}^{h}(y^{h,j-N^{h}})-1\Bigg)\\ \hskip 18.49988pt\times\exp\!\Big(-\,k^{h}\,Z\_{-}^{h}(y^{h,j-N^{h}})\,\Delta\_{-}^{h}(y^{h,j-N^{h}})\Big),\qquad\text{if }i=j+1,\\[6.0pt] 0,\qquad\text{otherwise.}\end{array}\right. |  |

Denote with 𝟏\mathbf{1} the unit vectors of ℝ2​Nh+1\mathbb{R}^{2N^{h}+1}. Define the functions wh:[0,T]​⨂j=1M{yj,−Nj,…,yj,Nj}→ℝw^{h}:[0,T]\bigotimes\_{\begin{subarray}{c}j=1\end{subarray}}^{M}\{y^{j,-N^{j}},\dots,y^{j,N^{j}}\}\to\mathbb{R} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | wh​(t,yh,i,𝐲l)\displaystyle w^{h}(t,y^{h,i},\mathbf{y}^{l}) | :=(exp⁡(𝐀h​(𝐲l)​(T−t))​ 1)i\displaystyle:=\left(\exp\big(\mathbf{A}^{h}(\mathbf{y}^{l})(T-t)\big)\,\mathbf{1}\right)\_{i} |  |

and the functions vh:[0,T]​⨂j=1M{yj,−Nj,…,yj,Nj}×ℝ+→ℝv^{h}:[0,T]\bigotimes\_{\begin{subarray}{c}j=1\end{subarray}}^{M}\{y^{j,-N^{j}},\dots,y^{j,N^{j}}\}\times\mathbb{R}\_{+}\to\mathbb{R}, vb:[0,T]×{ya,−Na,…,ya,Na}×{yb,−Nb,…,yb,Nb}×ℝ+→ℝv^{b}:[0,T]\times\{y^{a,-N^{a}},\dots,y^{a,N^{a}}\}\times\{y^{b,-N^{b}},\dots,y^{b,N^{b}}\}\times\mathbb{R}\_{+}\to\mathbb{R} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | vh​(t,yh,i,𝐲l,𝔠h)\displaystyle v^{h}(t,y^{h,i},\mathbf{y}^{l},\mathfrak{c}^{h}) | :=𝔠h+1khlog(wh(t,yh,i,𝐲l).\displaystyle:=\mathfrak{c}^{h}+\frac{1}{k^{h}}\log(w^{h}(t,y^{h,i},\mathbf{y}^{l}). |  |

Then the functions vhv^{h} solve the system of HJBs

|  |  |  |
| --- | --- | --- |
|  | {0=∂∂t​vh​(t,yh,i,𝐲l)+σ22​∂2∂s2​vh​(t,yh,i,𝐲l)+sup𝔪h∈ℝλh,−exp{kh(kh,0khs+∑j=1​j≠hMkh,jkhZ−j(yj))−kh(1+𝔪h)Z−h(yh)Δ−h(yh,i)}(vh(t,yh,i−Δ−h(yh,i),𝐲l)−vh(t,yh,i,𝐲l)+𝔪hZ−h(yh)Δ−h(yh,i)) 1{yh,i>y¯h}+sup𝔭h∈ℝλh,+exp{−kh(kh,0khs+∑j=1j≠hMkh,jkhZ+j(yj))+kh(1−𝔭h)Z+h(yh)Δ+h(yh,i)}(vh(t,yh,i+Δ+h(yh,i),𝐲l)−vh(t,yh,i,𝐲l)+𝔭hZ+h(yh)Δ+h(yh,i)) 1{yh,i<y¯h}\displaystyle\begin{cases}0&\;=\;\frac{\partial}{\partial t}\,v^{h}(t,y^{h,i},\mathbf{y}^{l})\;+\;\frac{\sigma^{2}}{2}\,\frac{\partial^{2}}{\partial s^{2}}v^{h}(t,y^{h,i},\mathbf{y}^{l})\\ &\;+\;\sup\_{\mathfrak{m}^{h}\in\mathbb{R}}\lambda^{h,-}\,\exp\Bigg\{k^{h}\!\Big(\tfrac{k^{h,0}}{k^{h}}\,s+\sum\_{\begin{subarray}{c}j=1j\neq h\end{subarray}}^{M}\tfrac{k^{h,j}}{k^{h}}\,Z\_{-}^{j}(y^{j})\Big)\\ &\qquad-k^{h}\!\Big(1+\mathfrak{m}^{h}\Big)Z\_{-}^{h}(y^{h})\,\Delta\_{-}^{h}(y^{h,i})\Bigg\}\Big(v^{h}(t,y^{h,i}-\Delta\_{-}^{h}(y^{h,i}),\mathbf{y}^{l})-v^{h}(t,y^{h,i},\mathbf{y}^{l})+\mathfrak{m}^{h}\,Z\_{-}^{h}(y^{h})\,\Delta\_{-}^{h}(y^{h,i})\Big)\,\mathbbm{1}\_{\{y^{h,i}>\underline{y}^{h}\}}\\[6.0pt] &\;+\;\sup\_{\mathfrak{p}^{h}\in\mathbb{R}}\lambda^{h,+}\,\exp\Bigg\{-k^{h}\!\Big(\tfrac{k^{h,0}}{k^{h}}\,s+\sum\_{\begin{subarray}{c}j=1\\ j\neq h\end{subarray}}^{M}\tfrac{k^{h,j}}{k^{h}}\,Z\_{+}^{j}(y^{j})\Big)\\ &\qquad+k^{h}\!\Big(1-\mathfrak{p}^{h}\Big)Z\_{+}^{h}(y^{h})\,\Delta\_{+}^{h}(y^{h,i})\Bigg\}\Big(v^{h}(t,y^{h,i}+\Delta\_{+}^{h}(y^{h,i}),\mathbf{y}^{l})-v^{h}(t,y^{h,i},\mathbf{y}^{l})+\mathfrak{p}^{h}\,Z\_{+}^{h}(y^{h})\,\Delta\_{+}^{h}(y^{h,i})\Big)\,\mathbbm{1}\_{\{y^{h,i}<\overline{y}^{h}\}}\\[6.0pt] \end{cases} |  |

with boundary conditions vh​(T,yh,i,𝐲l,𝔠h)=𝔠hv^{h}(T,y^{h,i},\mathbf{y}^{l},\mathfrak{c}^{h})=\mathfrak{c}^{h} for every hh, ii and ll. Moreover, the corresponding maximizers are independent of 𝔠h\mathfrak{c}^{h} and are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔪h,∗​(t,yh,i,𝐲l)\displaystyle\mathfrak{m}^{h,\*}(t,y^{h,i},\mathbf{y}^{l}) | =1+kh​(vh​(t,yh,i,𝐲l)−vh​(t,yh,i−Δ−h​(yh,i),𝐲l))kh​Z−h​(yh,i)​Δ−h​(yh,i),\displaystyle=\frac{1+k^{h}\big(v^{h}(t,y^{h,i},\mathbf{y}^{l})-v^{h}(t,y^{h,i}-\Delta\_{-}^{h}(y^{h,i}),\mathbf{y}^{l})\big)}{k^{h}\,Z\_{-}^{h}(y^{h,i})\,\Delta\_{-}^{h}(y^{h,i})}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔭h,∗​(t,yh,i,𝐲l)\displaystyle\mathfrak{p}^{h,\*}(t,y^{h,i},\mathbf{y}^{l}) | =1+kh​(vh​(t,yh,i,𝐲l)−vh​(t,yh,i+Δ+h​(yh,i),𝐲l))kh​Z+h​(yh,i)​Δ+h​(yh,i).\displaystyle=\frac{1+k^{h}\big(v^{h}(t,y^{h,i},\mathbf{y}^{l})-v^{h}(t,y^{h,i}+\Delta\_{+}^{h}(y^{h,i}),\mathbf{y}^{l})\big)}{k^{h}\,Z\_{+}^{h}(y^{h,i})\,\Delta\_{+}^{h}(y^{h,i})}. |  |

## Appendix B Simulations

As in Section [4](#S4 "4 Simulations ‣ Competition between DEXs through Dynamic Fees") we now perform numerical simulations in a three-player setting and compare the results with the duopoly and monopoly case. The total depth is split between three pools, and for simplicity we assume complete symmetry. In order to make the comparison meaningful we assume that the total depth present in the market is the same as in the monopoly and duopoly scenario.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | λ=100\lambda=100 | | | | λ=150\lambda=150 | | | |
| Player | Type | Fees | Sell | Buy | Vol | Fees | Sell | Buy | Vol |
| Player 1 | Optimal | 12.25 | 37.09 | 37.08 | 1236.21 | 18.24 | 55.22 | 55.14 | 1839.57 |
| Linear | 12.25 | 37.06 | 37.11 | 1236.09 | 18.23 | 55.16 | 55.21 | 1839.43 |
| Constant | 12.09 | 37.75 | 37.77 | 1258.69 | 17.95 | 56.24 | 56.25 | 1874.91 |
| Player 2 | Optimal | 12.26 | 37.11 | 37.09 | 1236.69 | 18.24 | 55.24 | 55.17 | 1840.33 |
| Linear | 12.26 | 37.07 | 37.12 | 1236.59 | 18.24 | 55.18 | 55.23 | 1840.25 |
| Constant | 12.09 | 37.75 | 37.78 | 1258.84 | 17.95 | 56.24 | 56.26 | 1875.11 |
| Player 3 | Optimal | 12.25 | 37.09 | 37.08 | 1236.10 | 18.24 | 55.22 | 55.16 | 1839.83 |
| Linear | 12.25 | 37.05 | 37.11 | 1235.99 | 18.24 | 55.16 | 55.23 | 1839.74 |
| Constant | 12.09 | 37.73 | 37.76 | 1258.27 | 17.95 | 56.22 | 56.25 | 1874.57 |
| Total | Optimal | 36.76 | 111.29 | 111.25 | 3709.00 | 54.72 | 165.68 | 165.47 | 5519.73 |
| Linear | 36.76 | 111.18 | 111.34 | 3708.67 | 54.71 | 165.50 | 165.67 | 5519.42 |
| Constant | 36.27 | 113.23 | 113.31 | 3775.80 | 53.85 | 168.70 | 168.76 | 5624.59 |

Table 3: Average fees collected (Fees), number of sell trades (Sell), number of buy trades (Buy), and volume traded (Vol) for Players 1,2,3 and Total under different fee types when k=2k=2, with λ∈{100,150}\lambda\in\{100,150\}.



|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | λ=100\lambda=100 | | | | λ=150\lambda=150 | | | |
| Player | Type | Fees | Sell | Buy | Vol | Fees | Sell | Buy | Vol |
| Player 1 | Optimal | 24.22 | 36.51 | 36.52 | 1217.23 | 36.04 | 54.35 | 54.31 | 1810.96 |
| Linear | 24.22 | 36.49 | 36.54 | 1217.20 | 36.04 | 54.31 | 54.35 | 1810.94 |
| Constant | 24.12 | 36.76 | 36.80 | 1225.93 | 35.84 | 54.76 | 54.78 | 1825.60 |
| Player 2 | Optimal | 24.23 | 36.52 | 36.54 | 1217.71 | 36.06 | 54.36 | 54.34 | 1811.78 |
| Linear | 24.23 | 36.50 | 36.56 | 1217.69 | 36.05 | 54.32 | 54.38 | 1811.78 |
| Constant | 24.13 | 36.77 | 36.81 | 1226.25 | 35.85 | 54.77 | 54.81 | 1826.21 |
| Player 3 | Optimal | 24.22 | 36.51 | 36.52 | 1217.18 | 36.04 | 54.34 | 54.33 | 1811.14 |
| Linear | 24.22 | 36.49 | 36.54 | 1217.17 | 36.04 | 54.30 | 54.37 | 1811.18 |
| Constant | 24.12 | 36.75 | 36.79 | 1225.71 | 35.84 | 54.74 | 54.79 | 1825.58 |
| Total | Optimal | 72.67 | 109.54 | 109.58 | 3652.12 | 108.14 | 163.05 | 162.98 | 5433.88 |
| Linear | 72.67 | 109.48 | 109.64 | 3652.06 | 108.13 | 162.93 | 163.10 | 5433.90 |
| Constant | 72.37 | 110.28 | 110.40 | 3677.89 | 107.53 | 164.27 | 164.38 | 5477.39 |

Table 4: Average fees collected (Fees), number of sell trades (Sell), number of buy trades (Buy), and volume traded (Vol) for Players 1,2,3 and Total under different fee types when k=1k=1, with λ∈{100,150}\lambda\in\{100,150\}.

We perform analogous simulations in the three-player case and obtain qualitatively similar, but amplified, effects. First, increased competition further benefits a strategic liquidity taker: with three venues, the liquidity taker can route orders to the best available quotes and thus extract more value than in the duopoly case. Second, in low-volatility regimes this improvement is largely paid for by noise liquidity takers, who face a higher average slippage as competition intensifies. As volatility rises, however, this pattern reverses: the average slippage tends to decrease with the number of competing venues, indicating that in high-volatility regimes liquidity takers on average obtain better execution when more players compete for order flow.

![Refer to caption](2603.09669v1/figures/Bid_ask_3_players.png)


(a) Strategic Bid–ask as a function of total traded volume in the monopoly (blue line), two players (red line) and three players (green line) case.

![Refer to caption](2603.09669v1/figures/avg_slippage_3_p.png)


(b) Average slippage as a function of total traded volume in the monopoly (blue line), two players (red line) and three players (green line) case.

Finally, we plot the revenue per player and the AMM’s revenue in two cases. In the first case (left figure), we show the revenue of a single player in the monopoly (blue line), two-player (red line), and three-player (green line) scenarios, under the assumption that liquidity is split among all participants. We observe that the revenue per player decreases as the number of players increases. If the number of players continues to grow, the revenue for an individual player may eventually become too low to make participation profitable. This suggests that if an LP must pay an entrance fee to create its own pool, it will only choose to enter if the expected revenue exceeds the entrance fee, and therefore only if the number of players is not too large.

In the second case (right figure), we plot the AMM’s total revenue in a setting where all players provide the same amount of liquidity. Here, we see that total revenue decreases as the number of players increases, because LPs trade at better prices when there are more players.

![Refer to caption](2603.09669v1/figures/rev_per_player_diff_liq.png)


(a) Revenue per player as a function of total traded volume in the monopoly (blue line), two-player (red line), and three-player (green line) scenarios, when liquidity is split among all participants.

![Refer to caption](2603.09669v1/figures/rev_per_unit_of_risky_asset_same_depth.png)


(b) AMM total revenue as a function of total traded volume when all players provide the same amount of liquidity, in the monopoly (blue line), two-player (red line), and three-player (green line) scenarios.

## References

* M. Avellaneda and S. Stoikov (2008)
  High-frequency trading in a limit order book.
  Quantitative Finance 8 (3),  pp. 217–224.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees"),
  [Remark 2.3](#S2.Thmtheorem3.p1.2 "Remark 2.3. ‣ 2 Two-player model ‣ Competition between DEXs through Dynamic Fees").
* L. Baggiani, M. Herdegen, and L. Sánchez-Betancourt (2025)
  Optimal dynamic fees in automated market makers.
  arXiv preprint arXiv:2506.02869.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees"),
  [§2](#S2.p9.11 "2 Two-player model ‣ Competition between DEXs through Dynamic Fees"),
  [§3](#S3.p2.19 "3 Numerical results ‣ Competition between DEXs through Dynamic Fees"),
  [§3](#S3.p9.1 "3 Numerical results ‣ Competition between DEXs through Dynamic Fees").
* B. Baldacci, P. Bergault, and D. Possamaï (2023)
  A mean-field game of market-making against strategic traders.
  SIAM Journal on Financial Mathematics 14 (4),  pp. 1080–1112.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* E. Bayraktar, A. Cohen, and A. Nellis (2024)
  DEX specs: a mean field approach to defi currency exchanges.
  arXiv preprint arXiv:2404.09090.
  Cited by: [footnote 2](#footnote2 "In 1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* P. Bergault, Y. Hafsi, and L. Sánchez-Betancourt (2026)
  Trading in cexs and dexs with priority fees and stochastic delays.
  arXiv preprint arXiv:2602.10798.
  Cited by: [footnote 2](#footnote2 "In 1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* M. Bichuch and Z. Feinstein (2025)
  The price of liquidity: implied volatility of automated market maker fees.
  arXiv preprint arXiv:2509.23222.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* R. Boyce, M. Herdegen, and L. Sánchez-Betancourt (2025)
  Market making with exogenous competition.
  SIAM Journal on Financial Mathematics 16 (2),  pp. 692–706.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* S. Campbell, P. Bergault, J. Milionis, and M. Nutz (2025)
  Optimal fees for liquidity provision in automated market makers.
  arXiv preprint arXiv:2508.08152.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* D. Cao, L. Kogan, G. Tsoukalas, and B. Hemenway Falk (2023)
  A structural model of automated market making.
  Available at SSRN 4591447.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* A. Capponi, A. Coache, and J. Muhle-Karbe (2026)
  Optimal trading in automated market makers.
  Available at SSRN 6145286.
  Cited by: [footnote 2](#footnote2 "In 1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* Á. Cartea, F. Drissi, and M. Monga (2023)
  Execution and statistical arbitrage with signals in multiple automated market makers.
  In 2023 IEEE 43rd International Conference on Distributed Computing Systems Workshops (ICDCSW),
   pp. 37–42.
  Cited by: [footnote 2](#footnote2 "In 1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* Á. Cartea, F. Drissi, L. Sánchez-Betancourt, D. Siska, and L. Szpruch (2024)
  Strategic bonding curves in automated market makers.
  Available at SSRN 5018420.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* Á. Cartea, S. Jaimungal, and J. Penalva (2015)
  Algorithmic and high-frequency trading.
   Cambridge University Press.
  Cited by: [§3](#S3.p9.1 "3 Numerical results ‣ Competition between DEXs through Dynamic Fees"),
  [footnote 3](#footnote3 "In 1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* N. Chilenje, M. Daba, D. Feleppa, C. Fellner, and L. Sánchez-Betancourt (2025)
  Market making with competition: a stackelberg equilibrium.
  Available at SSRN 5505480.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* F. Drissi, X. Wu, and S. Jaimungal (2025)
  Equilibrium liquidity and risk offsetting in decentralised markets.
  arXiv preprint arXiv:2512.19838.
  Cited by: [footnote 2](#footnote2 "In 1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* A. Evans, G. Angeris, and T. Chitra (2021)
  Optimal fees for geometric mean market makers.
  In Financial Cryptography and Data Security. FC 2021 International Workshops,
  Lecture Notes in Computer Science.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* R. Fritsch (2021)
  A note on optimal fees for constant function market makers.
  In Proceedings of the 2021 ACM CCS Workshop on Decentralized Finance and Security,
   pp. 9–14.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* O. Guéant (2016)
  The financial mathematics of market liquidity: from optimal execution to market making.
   CRC Press.
  Cited by: [footnote 3](#footnote3 "In 1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* I. Guo and S. Jin (2025)
  Macroscopic market making games.
  Mathematical Finance.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* J. Hasbrouck, T. J. Rivera, and F. Saleh (2022)
  The need for fees at a dex: how increases in fees can increase dex trading volume.
  Available at SSRN 4192925.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* X. D. He, C. Yang, and Y. Zhou (2024)
  Optimal design of automated market makers on decentralized exchanges.
  arXiv preprint arXiv:2404.13291.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* X. D. He, C. Yang, and Y. Zhou (2025)
  Arbitrage on decentralized exchanges.
  arXiv preprint arXiv:2507.08302.
  Cited by: [footnote 2](#footnote2 "In 1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* S. Jaimungal, Y. F. Saporito, M. O. Souza, and Y. Thamsten (2023)
  Optimal trading in automatic market makers with deep learning.
  arXiv preprint arXiv:2304.02180.
  Cited by: [footnote 2](#footnote2 "In 1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* J. Luo and H. Zheng (2021)
  Dynamic equilibrium of market making with price competition.
  Dynamic Games and Applications 11 (3),  pp. 556–579.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* J. Milionis, C. C. Moallemi, T. Roughgarden, and A. L. Zhang (2022a)
  Automated market making and loss-versus-rebalancing.
  arXiv preprint arXiv:2208.06046.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* J. Milionis, C. C. Moallemi, T. Roughgarden, and A. L. Zhang (2022b)
  Quantifying loss in automated market makers.
  In Proceedings of the 2022 ACM CCS Workshop on Decentralized Finance and Security,
   pp. 71–74.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* J. Milionis, C. C. Moallemi, and T. Roughgarden (2024)
  Automated market making and arbitrage profits in the presence of fees.
  In International Conference on Financial Cryptography and Data Security,
   pp. 159–171.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").
* V. Nadkarni, S. Kulkarni, and P. Viswanath (2024)
  Adaptive curves for optimally efficient market making.
  arXiv preprint arXiv:2406.13794.
  Cited by: [§1](#S1.p1.9 "1 Introduction ‣ Competition between DEXs through Dynamic Fees").

BETA