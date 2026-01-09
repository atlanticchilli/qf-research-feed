---
authors:
- Salam Rabindrajit Luwang
- Kundan Mukhia
- Buddha Nath Sharma
- Md. Nurujjaman
- Anish Rai
- Filippo Petroni
doc_id: arxiv:2601.04959v1
family_id: arxiv:2601.04959
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations
  Through Markov Analysis
url_abs: http://arxiv.org/abs/2601.04959v1
url_html: https://arxiv.org/html/2601.04959v1
venue: arXiv q-fin
version: 1
year: 2026
---


Salam Rabindrajit Luwang
[salamrabindrajit@gmail.com](mailto:salamrabindrajit@gmail.com)

Kundan Mukhia
[kundanmukhia07@gmail.com](mailto:kundanmukhia07@gmail.com)

Buddha Nath Sharma
[bnsharma09@yahoo.com](mailto:bnsharma09@yahoo.com)

Md. Nurujjaman
[md.nurujjaman@nitsikkim.ac.in](mailto:md.nurujjaman@nitsikkim.ac.in)

Anish Rai
[anishrai412@gmail.com](mailto:anishrai412@gmail.com)

Filippo Petroni
[fpetroni@luiss.it](mailto:fpetroni@luiss.it)

###### Abstract

A quantitative understanding of the stochastic dynamics in limit order price changes is essential for meaningful advances in market microstructure research and effective execution strategy design. This paper presents the first comprehensive empirical analysis of intraday limit order price change transition dynamics, treating ask and bid orders separately across different market capitalization tiers. Using high-frequency tick data from NASDAQ100 stocks, we employ a discrete-time Markov chain framework to analyze the evolution of price adjustments throughout the trading day. We categorize consecutive price changes into nine distinct states and estimate transition probability matrices (TPMs) for six intraday intervals across High (𝙷𝙼𝙲\mathtt{HMC}), Medium (𝙼𝙼𝙲\mathtt{MMC}), and Low (𝙻𝙼𝙲\mathtt{LMC}) market capitalization stocks. Elememt-wise comparison of TPMs reveals systematic intraday patterns: price inertia i.e. self-transition probability, peaks during opening and closing hours, stabilizing at lower levels during midday. A pronounced capitalization gradient is also observed: 𝙷𝙼𝙲\mathtt{HMC} stocks exhibit the strongest price inertia, while 𝙻𝙼𝙲\mathtt{LMC} stocks demonstrate significantly lower stability and pronounced bid-ask spread. Markov chain metrics, including spectral gap, entropy rate, and mean recurrence times quantify these dynamics. Clustering analysis identifies three distinct temporal phases on the bid side – Opening, Midday, and Closing and four phases on the ask side – Opening, Midday, Pre-Close, and Close, indicating that sellers initiate end-of-day positioning strategies earlier than buyers. Stationary distributions reveal that limit order dynamics are predominantly characterized by neutral and mild price changes. Furthermore, Jensen-Shannon divergence computed between stationary distributions across time-intervals confirms the closing hour as the most distinct phase, with capitalization modulating the intensity of temporal contrasts and the degree of bid-ask asymmetry. These findings advance the understanding of evolving intraday limit order pricing behavior, offering direct applications for capitalization-aware and time-adaptive execution algorithms and risk management frameworks.

###### keywords:

Limit orders , Markov chains , Intraday dynamics , Market capitalization , Bid-ask asymmetry , Clustering , Jensen-Shannon divergence

\affiliation

[label1]organization=Department of Physics, National Institute of Technology Sikkim,
city=Ravangla,
postcode=737139,
state=Sikkim,
country=India

\affiliation

[label2]organization=Chennai Mathematical Institute,
city=Kelambakkam,
postcode=603103,
state=Tamil Nadu,
country=India

\affiliation

[label3]organization=Department of Economics, University G. d’Annunzio of Chieti-Pescara,
city=Pescara,
postcode=65127,
state=Abruzzo,
country=Italy

## 1 Introduction

In equity markets, limit orders represent a critical component of the trading ecosystem, allowing traders to specify precise execution prices while contributing to market liquidity [[11](https://arxiv.org/html/2601.04959v1#bib.bib234 "Statistical properties of stock order books: empirical results and models"), [18](https://arxiv.org/html/2601.04959v1#bib.bib235 "A stochastic model for order book dynamics"), [35](https://arxiv.org/html/2601.04959v1#bib.bib236 "The market impact of a limit order"), [32](https://arxiv.org/html/2601.04959v1#bib.bib237 "Limit order books")]. Unlike market orders that execute immediately at prevailing prices, limit orders remain active in the order book until matched or canceled. This creates a dynamic environment in which the intraday evolution of limit order prices is driven by traders’ continuous strategic adjustments to liquidity conditions, information arrival, and prevailing market sentiment [[47](https://arxiv.org/html/2601.04959v1#bib.bib238 "Market microstructure: a survey"), [8](https://arxiv.org/html/2601.04959v1#bib.bib239 "Market microstructure: a survey of microfoundations, empirical results, and policy implications"), [57](https://arxiv.org/html/2601.04959v1#bib.bib240 "A dynamic model of the limit order book"), [19](https://arxiv.org/html/2601.04959v1#bib.bib124 "Statistical modeling of high-frequency financial data")]. These adjustments manifest as sequences of discrete price revisions, generating complex stochastic dynamics with systematic intraday regularities [[15](https://arxiv.org/html/2601.04959v1#bib.bib243 "Evidence on the speed of convergence to market efficiency"), [33](https://arxiv.org/html/2601.04959v1#bib.bib244 "Do liquidity measures measure liquidity?")].

The nature of these adjustments is fundamentally asymmetric: buy limit orders compete by improving prices toward the ask, while sell limit orders compete by lowering prices toward the bid, reflecting their opposing economic objectives and inventory considerations [[34](https://arxiv.org/html/2601.04959v1#bib.bib245 "Empirical market microstructure: the institutions, economics, and econometrics of securities trading"), [21](https://arxiv.org/html/2601.04959v1#bib.bib264 "Semi-markov models in high frequency finance: a review")]. Understanding how these distinct buy- and sell-side price revision mechanisms evolve over the trading day therefore represents a central challenge in market microstructure research, with direct implications for algorithmic trading design, liquidity provision, and market efficiency.

Beyond intraday temporal effects, market capitalization plays a crucial role in shaping limit order pricing behavior and the associated price change dynamics. High-capitalization stocks typically exhibit frequent but relatively small price adjustments, reflecting dense order books, intense competition among liquidity providers, and narrow bid–ask spreads [[8](https://arxiv.org/html/2601.04959v1#bib.bib239 "Market microstructure: a survey of microfoundations, empirical results, and policy implications"), [11](https://arxiv.org/html/2601.04959v1#bib.bib234 "Statistical properties of stock order books: empirical results and models"), [19](https://arxiv.org/html/2601.04959v1#bib.bib124 "Statistical modeling of high-frequency financial data")]. In such environments, traders engage in fine price shading to maintain queue priority while minimizing execution costs [[57](https://arxiv.org/html/2601.04959v1#bib.bib240 "A dynamic model of the limit order book"), [32](https://arxiv.org/html/2601.04959v1#bib.bib237 "Limit order books")]. Medium-capitalization stocks display intermediate liquidity conditions, with more pronounced variability in price changes due to less predictable order flow and reduced market depth [[18](https://arxiv.org/html/2601.04959v1#bib.bib235 "A stochastic model for order book dynamics"), [35](https://arxiv.org/html/2601.04959v1#bib.bib236 "The market impact of a limit order")]. In contrast, low-capitalization stocks are characterized by sparse order books, wider spreads, and heightened information asymmetry, leading to less frequent but larger price revisions, often triggered by liquidity shocks or information events [[33](https://arxiv.org/html/2601.04959v1#bib.bib244 "Do liquidity measures measure liquidity?"), [15](https://arxiv.org/html/2601.04959v1#bib.bib243 "Evidence on the speed of convergence to market efficiency"), [47](https://arxiv.org/html/2601.04959v1#bib.bib238 "Market microstructure: a survey")]. These capitalization-dependent features suggest that limit order price changes are governed by distinct stochastic mechanisms across market segments, thereby motivating a stratified analytical approach.

A substantial body of literature has documented intraday regularities in financial markets across multiple dimensions, including trading volume [[43](https://arxiv.org/html/2601.04959v1#bib.bib247 "Intraday trading patterns in an intelligent autonomous agent-based stock market")], transaction patterns [[37](https://arxiv.org/html/2601.04959v1#bib.bib67 "Behaviour of intra-daily stock return on an asian emerging market-hong kong")], liquidity provision [[12](https://arxiv.org/html/2601.04959v1#bib.bib72 "An analysis of depth behavior in an electronic, order-driven environment")], and bid–ask spread dynamics [[44](https://arxiv.org/html/2601.04959v1#bib.bib199 "Spreads, depths, and the impact of earnings information: an intraday analysis")]. Market microstructure studies have further emphasized the role of order types in shaping these patterns [[8](https://arxiv.org/html/2601.04959v1#bib.bib239 "Market microstructure: a survey of microfoundations, empirical results, and policy implications"), [32](https://arxiv.org/html/2601.04959v1#bib.bib237 "Limit order books"), [18](https://arxiv.org/html/2601.04959v1#bib.bib235 "A stochastic model for order book dynamics"), [35](https://arxiv.org/html/2601.04959v1#bib.bib236 "The market impact of a limit order")], stimulating extensive research on order book resilience, transaction costs, and strategic liquidity provision [[11](https://arxiv.org/html/2601.04959v1#bib.bib234 "Statistical properties of stock order books: empirical results and models"), [57](https://arxiv.org/html/2601.04959v1#bib.bib240 "A dynamic model of the limit order book")]. Within this framework, empirical evidence shows that limit order submission strategies vary systematically over the trading day [[28](https://arxiv.org/html/2601.04959v1#bib.bib74 "Order dynamics: recent evidence from the nyse"), [9](https://arxiv.org/html/2601.04959v1#bib.bib75 "An empirical analysis of the limit order book and the order flow in the paris bourse")], with distinct regimes at the market open, midday, and close [[1](https://arxiv.org/html/2601.04959v1#bib.bib68 "A theory of intraday patterns: volume and price variability"), [30](https://arxiv.org/html/2601.04959v1#bib.bib232 "Intraday liquidity costs and order execution quality in nasdaq stocks")]. The rise of high-frequency and algorithmic trading has further amplified these temporal patterns, leading to clustering in price revisions and sequential price improvement behavior [[35](https://arxiv.org/html/2601.04959v1#bib.bib236 "The market impact of a limit order"), [17](https://arxiv.org/html/2601.04959v1#bib.bib241 "The price impact of order book events"), [13](https://arxiv.org/html/2601.04959v1#bib.bib250 "Algorithmic and high-frequency trading")]. Despite this extensive literature, a critical gap remains. To the best of our knowledge, no existing study has systematically examined the intraday evolution of limit order price change transitions, treating buy and sell orders separately and jointly accounting for both intraday timing and market capitalization effects.

Addressing this gap requires a modeling framework capable of capturing the discrete, state-dependent nature of sequential price adjustments. Stochastic approaches based on Markov chains are particularly well suited for this purpose, having proven effective in the analysis of discrete financial processes [[24](https://arxiv.org/html/2601.04959v1#bib.bib253 "Can markov switching models replicate chartist profits in the foreign exchange market?"), [58](https://arxiv.org/html/2601.04959v1#bib.bib254 "Dynamics of trade-by-trade price movements: decomposition and models")] and widely applied in market microstructure settings [[16](https://arxiv.org/html/2601.04959v1#bib.bib59 "Order book dynamics in liquid markets: limit theorems and diffusion approximations"), [22](https://arxiv.org/html/2601.04959v1#bib.bib142 "A semi-markov model with memory for price changes"), [21](https://arxiv.org/html/2601.04959v1#bib.bib264 "Semi-markov models in high frequency finance: a review"), [29](https://arxiv.org/html/2601.04959v1#bib.bib32 "Thermodynamics and statistical mechanics")]. While our prior works [[56](https://arxiv.org/html/2601.04959v1#bib.bib61 "High-frequency stock market order transitions during the us–china trade war 2018: a discrete-time markov chain analysis"), [46](https://arxiv.org/html/2601.04959v1#bib.bib257 "Intraday order transitions across market capitalizations through markov analysis")] employed discrete-time Markov chains to study intraday order transitions, it treated order types in aggregate and did not explicitly focus on the dynamics of price revisions within limit orders. The present study extends this line of research by shifting the analytical focus to the intraday transition dynamics of limit order price changes themselves. Specifically, we investigate how these transitions evolve across trading hours and market capitalization tiers, and how they differ between the bid and ask sides of the order book.

Building on our established methodology [[56](https://arxiv.org/html/2601.04959v1#bib.bib61 "High-frequency stock market order transitions during the us–china trade war 2018: a discrete-time markov chain analysis"), [46](https://arxiv.org/html/2601.04959v1#bib.bib257 "Intraday order transitions across market capitalizations through markov analysis")], we develop a discrete-time Markov chain (DTMC) framework to analyze limit order price change transitions using high-frequency tick-by-tick data for NASDAQ100 stocks. Consecutive limit order price changes are classified into nine discrete states based on their magnitude and direction, yielding categorical time series that capture the sequential nature of pricing decisions. For each intraday interval τ∈{𝚃𝟷,𝚃𝟸,…,𝚃𝟼}\tau\in\{\mathtt{T\_{1},T\_{2},\ldots,T\_{6}}\} and market capitalization tier c∈{𝙷𝙼𝙲,𝙼𝙼𝙲,𝙻𝙼𝙲}c\in\{\mathtt{HMC,MMC,LMC}\}, we estimate transition probability matrices Pi​j(τ,c)P\_{ij}^{(\tau,c)} describing the likelihood of transitioning from state ii to state jj. Treating bid and ask limit orders separately allows us to explicitly account for directional asymmetries in price revision behavior.

Employing this DTMC framework, we conduct a comprehensive empirical analysis of transition probabilities, stationary distributions, and key Markov chain metrics, including spectral gap, entropy rate, and mean recurrence time. We further investigate cross-interval similarities using clustering techniques and Jensen–Shannon divergence. Our results reveal pronounced intraday regularities, with price inertia peaking at the market open and close, and a clear capitalization gradient whereby high-capitalization stocks exhibit the greatest stability and low-capitalization stocks the highest degree of dynamism. Clustering analysis uncovers distinct Opening, Midday, and Closing regimes on both sides of the book, with an additional pre-close phase emerging on the ask side. Stationary distributions indicate that limit order dynamics are dominated by neutral and mild price changes, while the closing hour stands out as the most distinct temporal regime, with capitalization modulating the intensity of intraday contrasts and bid–ask asymmetry.

The primary contribution of this paper is to provide the first data-driven Markov chain analysis of intraday limit order price change transition dynamics across market capitalization tiers. By extending existing intraday order transition frameworks to the granular pricing behavior within limit orders, our study offers new empirical insights into how time of day, market size, and order direction jointly shape limit order price dynamics. These findings have direct implications for time-adaptive and capitalization-aware execution strategies. The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2601.04959v1#S2 "2 Data ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") describes the data and intraday segmentation. Section [3](https://arxiv.org/html/2601.04959v1#S3 "3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") presents the methodological framework. Section [4](https://arxiv.org/html/2601.04959v1#S4 "4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") reports the empirical findings, while Section [5](https://arxiv.org/html/2601.04959v1#S5 "5 Discussion ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") discusses their robustness and implications. Section [6](https://arxiv.org/html/2601.04959v1#S6 "6 Conclusion ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") concludes and outlines directions for future research.

## 2 Data

### 2.1 Data Description

The availability of high-frequency, micro-level stock market data has unlocked unprecedented capabilities for granular empirical research in financial markets. We use tick-by-tick order submission data obtained from [Algoseek](https://www.algoseek.com) in this study. The data cover all order types placed from 04:00:00 to 20:00:00 Eastern Standard Time (EST) for stocks listed in the NASDAQ100 index. Each trading day typically contains hundreds of millions of records, with raw CSV files of roughly 20–40 GB. Table [1](https://arxiv.org/html/2601.04959v1#S2.T1 "Table 1 ‣ 2.1 Data Description ‣ 2 Data ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") presents the dataset structure, with eight columns: Date, Timestamp, Order ID, Event Type, Ticker Symbol, Price, Quantity, and Exchange.

Table 1: Sample dataset illustrating high-frequency tick-by-tick order data for stocks listed in the NASDAQ100.

Date
Timestamp
Order Id.
Event Type
Ticker
Price
Quantity
Exchange

2018-11-07
4:00:00.122
11872
ADD-ASK
AAPL
173.00
500
NASDAQ

2018-11-07
4:00:00.255
12654
ADD-BID
AAPL
186.99
100
NASDAQ

2018-11-07
4:00:00.123
12865
FILL-BID
XLF
0
200
NASDAQ

…
…
…
…
…
…
…
…

2018-11-07
9:30:00.145
76543
DELETE-BID
GOOGL
0
400
NASDAQ

2018-11-07
9:30:01.678
81624
CANCEL-BID
INTC
0
500
NASDAQ

…
…
…
…
…
…
…
…

2018-11-07
16:00:00.000
116752
EXECUTE-BID
AMD
0
50
NASDAQ

…
…
…
…
…
…
…
…

2018-11-06
20:00:00.000
547324
DELETE-ASK
NVDA
0
40
NASDAQ

Our empirical analysis focuses on the two event types – ADD-ASK and ADD-BID order types, which correspond to the submission of new ask (selling) and bid (buying) limit orders, respectively. For each order type, we compute price differences between consecutive orders, then categorize these differences into discrete states, as presented in Table [4](https://arxiv.org/html/2601.04959v1#S3.T4 "Table 4 ‣ 3.2 Discrete-Time Markov Chain for Limit Order Price Changes ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"), that define our Markov chain framework. The primary objective is to estimate the probabilities of transition between successive limit-order price change states, with a particular focus on their intraday dynamics and variation across different market capitalization tiers. The following subsection explains the segmentation of a trading day for the intraday analysis and selected the stocks for each market capitalization tier.

### 2.2 Stock Selection and Time-Interval Division

For each market capitalization tier – High Market Capitalization (𝙷𝙼𝙲\mathtt{HMC}), Medium Market Capitalization (𝙼𝙼𝙲\mathtt{MMC}), and Low Market Capitalization (𝙻𝙼𝙲\mathtt{LMC}), we select five stocks; extract tick data for these five stocks separately from the full raw data shown in Table [1](https://arxiv.org/html/2601.04959v1#S2.T1 "Table 1 ‣ 2.1 Data Description ‣ 2 Data ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"). The stock selection follows a stratified approach across the capitalization tiers: for 𝙷𝙼𝙲\mathtt{HMC}, we consider ranks 1s​t1^{st}–20t​h20^{th} and choose five stocks from distinct sectors to limit sector bias; similarly, we select five stocks from ranks 41s​t41^{st}–60t​h60^{th} for 𝙼𝙼𝙲\mathtt{MMC}, and 81s​t81^{st}–100t​h100^{th} 𝙻𝙼𝙲\mathtt{LMC}, as shown in Table [2](https://arxiv.org/html/2601.04959v1#S2.T2 "Table 2 ‣ 2.2 Stock Selection and Time-Interval Division ‣ 2 Data ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"). This analysis spans 12 trading days, balanced between six days where the NASDAQ100 index closed higher than its opening price (0707-1111-20182018, 1515-1111-20182018, 2828-1111-20182018, 0606-1212-20182018, 1010-1212-20182018, 2626-1212-20182018) and six days where it closed lower (0909-1111-20182018, 1212-1111-20182018, 1414-1111-20182018, 0404-1212-20182018, 0707-1212-20182018, 2121-1212-20182018), a design that mitigates the risk of our results being driven by a single market trend. The entire process of data extraction and preprocessing was performed efficiently using EmEditor, a tool capable of handling the multi-gigabyte files involved.

Table 2: Selected stocks across market capitalization tiers.

|  |  |  |
| --- | --- | --- |
| 𝙷𝙼𝙲\mathtt{HMC} (Ranks 1s​t−20t​h1^{st}-20^{th}) | 𝙼𝙼𝙲\mathtt{MMC} (Ranks 41s​t−60t​h41^{st}-60^{th}) | 𝙻𝙼𝙲\mathtt{LMC} (Ranks 81s​t−100t​h81^{st}-100^{th}) |
| Amazon.com Inc [AMZN]  (Consumer Services) | AbbVie Inc [ABBV]  (Healthcare) | Broadcom Inc [AVGO]  (Information Technology) |
| Johnson & Johnson [JNJ]  (Healthcare) | HSBC Holdings plc [HSBC]  (Finance) | Booking Holdings Inc [BKNG]  (Consumer Services) |
| JPMorgan Chase & Co [JPM]  (Finance) | Netflix Inc [NFLX]  (Consumer Services) | Bristol-Myers Squibb Co [BMY]  (Healthcare) |
| Microsoft Corp [MSFT]  (Information Technology) | Oracle Corp [ORCL]  (Information Technology) | Nike Inc [NKE]  (Consumer Goods) |
| Exxon Mobil Corp [XOM]  (Oil & Gas) | PepsiCo Inc [PEP]  (Consumer Goods) | Union Pacific Corp [UNP]  (Industrials) |

To analyze the intraday patterns of limit order price change dynamics for these stocks, we segment the trading hours i.e. 09:30:00.000−16:00:00.00009{:}30{:}00.000-16{:}00{:}00.000, into six distinct intervals as shown in Table [3](https://arxiv.org/html/2601.04959v1#S2.T3 "Table 3 ‣ 2.2 Stock Selection and Time-Interval Division ‣ 2 Data ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"). All intervals span one hour except 𝚃𝟹\mathtt{T\_{3}} and 𝚃𝟺\mathtt{T\_{4}} which are 75 minutes to accommodate the distinctive, often less volatile, patterns of the mid-day trading period.

Table 3: Time-intervals for intraday limit order price change analysis through Markov chain.

|  |  |  |
| --- | --- | --- |
| Time Interval | Timing (HH:MM:SS.000) | Duration (Minutes) |
| 𝚃𝟷\mathtt{T\_{1}} | 09:30:00.000 - 10:29:59.999 | 60 |
| 𝚃𝟸\mathtt{T\_{2}} | 10:30:00.000 - 11:29:59.999 | 60 |
| 𝚃𝟹\mathtt{T\_{3}} | 11:30:00.000 - 12:44:59.999 | 75 |
| 𝚃𝟺\mathtt{T\_{4}} | 12:45:00.000 - 13:59:59.999 | 75 |
| 𝚃𝟻\mathtt{T\_{5}} | 14:00:00.000 - 14:59:59.999 | 60 |
| 𝚃𝟼\mathtt{T\_{6}} | 15:00:00.000 - 16:00:00.000 | 60 |

The combination of time-based segmentation and
capitalization-tiered stock selection across diverse sectors and trading days creates a powerful, two-dimensional framework for comparative analysis.

## 3 Methodology

Having established the stock selection and time segmentation protocol, we now
present the methodological framework for analyzing intraday limit order price change dynamics using high-frequency tick-by-tick data.
The framework is designed to: (i) verify whether consecutive price changes exhibit short-range dependence using the G-test of independence, (ii) conditional on detecting dependencies, model the resulting state-to-state revision mechanism through a discrete-time Markov representation, and (iii) summarize and compare intraday dynamics across time intervals and market capitalization tiers, separately for bid and ask submissions.
Finally, we complement transition-based analysis with metrics, similarity-based comparisons of transition matrices, and stationary behavior to provide both local (one-step) and global (long-run) views of limit order price revision dynamics.

### 3.1 G-test of Independence

To validate the presence of memory effects in high-frequency limit order price changes, we employ the G-test of independence [[7](https://arxiv.org/html/2601.04959v1#bib.bib50 "USP: an independence test that improves on pearson’s chi-squared and the g-test"), [2](https://arxiv.org/html/2601.04959v1#bib.bib176 "Applicability of g-test in analyzing categorical variables")]. This likelihood ratio test evaluates whether consecutive price changes exhibit statistical dependence, a prerequisite for Markov chain modeling.
Operationally, the test is applied to the contingency table of consecutive state transitions constructed within each intraday time interval and capitalization tier, and performed separately for the bid and ask sides.

The test examines the null hypothesis of independence against the alternative of dependence:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H0\displaystyle H\_{0} | :Consecutive price changes are independent\displaystyle:\text{Consecutive price changes are independent} |  | (1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H1\displaystyle H\_{1} | :Consecutive price changes exhibit dependence\displaystyle:\text{Consecutive price changes exhibit dependence} |  | (2) |

The G-statistic quantifies the likelihood ratio between observed and expected frequencies under independence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | G=2​∑i,jOi​j​ln⁡(Oi​jEi​j),G=2\sum\_{i,j}O\_{ij}\ln\left(\frac{O\_{ij}}{E\_{ij}}\right), |  | (3) |

where Oi​jO\_{ij} represents observed transition frequencies from state ii to state jj, and Ei​jE\_{ij} denotes expected frequencies under independence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ei​j=(∑kOi​k)​(∑kOk​j)∑k,lOk​l.E\_{ij}=\frac{(\sum\_{k}O\_{ik})(\sum\_{k}O\_{kj})}{\sum\_{k,l}O\_{kl}}. |  | (4) |

Under H0H\_{0}, the G-statistic follows a χ2\chi^{2} distribution with (r−1)​(c−1)(r-1)(c-1) degrees of freedom, where rr and cc are the dimensions of the transition matrix. We reject H0H\_{0} at the 5% significance level if the resulting p-value falls below 0.05.
Rejection of the independence hypothesis indicates that limit order price changes exhibit statistically significant short-range dependence. Consistent with this evidence, we model the sequences using first-order Markov dynamics, where the next state depends only on the current state. This step provides a formal statistical basis for the Markov chain analysis and ensures that the subsequent estimation of transition matrices captures genuine temporal structure rather than sampling noise.

### 3.2 Discrete-Time Markov Chain for Limit Order Price Changes

Markov chain belongs to a category of stochastic processes that are highly effective in describing sequences of categorical events [[56](https://arxiv.org/html/2601.04959v1#bib.bib61 "High-frequency stock market order transitions during the us–china trade war 2018: a discrete-time markov chain analysis"), [23](https://arxiv.org/html/2601.04959v1#bib.bib160 "Markov chain modelling in finance: stock valuation and price discovery")]. We employ a discrete-time Markov Chain (DTMC) to model the dynamics of limit order price changes. A DTMC is a stochastic process comprising a series of random variables X1,X2,…,XnX\_{1},X\_{2},\ldots,X\_{n} that obeys the Markov property [[61](https://arxiv.org/html/2601.04959v1#bib.bib162 "The markovchain package: a package for easily handling discrete markov chains in r")], meaning the probability of transitioning to any future state Xn+1X\_{n+1} depends solely on the current state XnX\_{n} and is independent of all previous states [[59](https://arxiv.org/html/2601.04959v1#bib.bib163 "First and second order markov chain models for synthetic generation of wind speed time series")].
In our setting, XnX\_{n} represents the categorical state of the nn-th consecutive limit order price change for a fixed quote side, intraday interval, and capitalization tier.

To apply this framework, we first categorize limit order price changes into nine distinct states based on their percentage deviation from the previous limit order price, as defined in Table [4](https://arxiv.org/html/2601.04959v1#S3.T4 "Table 4 ‣ 3.2 Discrete-Time Markov Chain for Limit Order Price Changes ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"). The set of possible states is therefore S=S1,S2,…,S9S={S\_{1},S\_{2},\ldots,S\_{9}}.
This discretization preserves both direction and magnitude of revisions while enabling stable estimation of transition probabilities in a high-frequency setting.

Table 4: Categorization of limit order price change for Markov chain states.

|  |  |  |
| --- | --- | --- |
| Markov State | Price Change | Price Change Category |
| S1S\_{1} | >>-5.0% | A: Very Aggressive Sell |
| S2S\_{2} | -5.0% to -2.0% | B: Aggressive Sell |
| S3S\_{3} | -2.0% to -1.0% | C: Moderate Sell |
| S4S\_{4} | -1.0% to -0.01% | D: Mild Sell |
| S5S\_{5} | 0.0% | E: Neutral |
| S6S\_{6} | +0.01% to +1.0% | F: Mild Buy |
| S7S\_{7} | +1.0% to +2.0% | G: Moderate Buy |
| S8S\_{8} | +2.0% to +5.0% | H: Aggressive Buy |
| S9S\_{9} | >>+5.0% | I: Very Aggressive Buy |

The core component of the first-order DTMC is the transition probability pi​jp\_{ij}, which represents the probability of the price change transitioning from the current state SiS\_{i} to state SjS\_{j} in the next time step [[56](https://arxiv.org/html/2601.04959v1#bib.bib61 "High-frequency stock market order transitions during the us–china trade war 2018: a discrete-time markov chain analysis")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi​j=P​(Xn+1=Sj∣Xn=Si)p\_{ij}=P(X\_{n+1}=S\_{j}\mid X\_{n}=S\_{i}) |  | (5) |

The complete probability distribution of transitions between all states is concisely represented by a transition probability matrix, 𝐏\mathbf{P}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐏=(p11p12⋯p19p21p22⋯p29⋮⋮⋱⋮p91p92⋯p99)\mathbf{P}=\begin{pmatrix}p\_{11}&p\_{12}&\cdots&p\_{19}\\ p\_{21}&p\_{22}&\cdots&p\_{29}\\ \vdots&\vdots&\ddots&\vdots\\ p\_{91}&p\_{92}&\cdots&p\_{99}\end{pmatrix} |  | (6) |

This matrix is subject to the constraints:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤pi​j≤1,∀i,j∈S,\displaystyle 0\leq p\_{ij}\leq 1,\quad\forall i,j\in S, |  | (7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=19pi​j=1,∀i∈S.\displaystyle\sum\_{j=1}^{9}p\_{ij}=1,\quad\forall i\in S. |  | (8) |

To estimate the elements pi​jp\_{ij} of the matrix 𝐏\mathbf{P}, we use the Maximum Likelihood Estimation (MLE) method [[59](https://arxiv.org/html/2601.04959v1#bib.bib163 "First and second order markov chain models for synthetic generation of wind speed time series"), [48](https://arxiv.org/html/2601.04959v1#bib.bib165 "Markov chain model for the stochastic behaviors of wind-direction data")].
We estimate transition matrices separately for each intraday interval and market capitalization tier, and for each quote side. A modified MATLAB code is used for this estimation, with the original version available in Ref. [[26](https://arxiv.org/html/2601.04959v1#bib.bib45 "Data-driven stochastic modeling markov chain matlab codes")]. These matrices capture the step-by-step dynamics of limit order price adjustments and enable systematic comparisons across time intervals. To translate transition patterns into interpretable market features, we next compute metrics that summarize persistence and randomness.
This stratified estimation design isolates (i) within-day temporal effects, (ii) capitalization effects, and (iii) bid–ask asymmetries in a unified probabilistic framework.

### 3.3 Markov Chain Dynamics Metrics

Beyond transition probabilities, several metrics derived from the transition matrix 𝐏\mathbf{P} characterize the dynamics of limit order price change processes, as listed below.
We use these summaries to compare how quickly price revision behavior stabilizes, how predictable it is given the current state, and how frequently different degrees of aggressiveness occur.

#### 3.3.1 Spectral Gap and Relaxation Time

The spectral gap γ\gamma measures the convergence rate to the stationary distribution π\pi given later in Eq. [14](https://arxiv.org/html/2601.04959v1#S3.E14 "In 3.6 Stationary Distribution Analysis ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"), defined as the difference between the largest and second-largest eigenvalues of 𝐏\mathbf{P} [[25](https://arxiv.org/html/2601.04959v1#bib.bib213 "Geometric bounds for eigenvalues of markov chains"), [45](https://arxiv.org/html/2601.04959v1#bib.bib214 "Markov chains and mixing times")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ=1−|λ2|,\gamma=1-|\lambda\_{2}|, |  | (9) |

where λ1=1\lambda\_{1}=1 and λ2\lambda\_{2} is the second-largest eigenvalue in magnitude, with relaxation time τ\tau defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τrel=1γ.\tau\_{\text{rel}}=\frac{1}{\gamma}. |  | (10) |

A large spectral gap indicates rapid convergence to equilibrium with short-lived memory effects. Small gaps suggest persistent patterns and slower convergence to steady-state behavior.

#### 3.3.2 Entropy Rate

The entropy rate quantifies the average information content per transition for a stationary Markov chain, defined as [[20](https://arxiv.org/html/2601.04959v1#bib.bib90 "Elements of information theory")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(𝒳)=−∑i=19πi​∑j=19pi​j​log⁡pi​j.H(\mathcal{X})=-\sum\_{i=1}^{9}\pi\_{i}\sum\_{j=1}^{9}p\_{ij}\log p\_{ij}. |  | (11) |

High entropy rates indicate unpredictable price change sequences, while low rates suggest structured, predictable patterns given the current state.

#### 3.3.3 Mixing Rate

The mixing rate describes convergence speed to the stationary distribution π\pi in Eq. [14](https://arxiv.org/html/2601.04959v1#S3.E14 "In 3.6 Stationary Distribution Analysis ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") from arbitrary initial conditions, bounded by [[45](https://arxiv.org/html/2601.04959v1#bib.bib214 "Markov chains and mixing times"), [60](https://arxiv.org/html/2601.04959v1#bib.bib215 "Improved bounds for mixing rates of markov chains and multicommodity flow")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝐩(n)−π‖TV≤C​e−n/τrel,\|\mathbf{p}^{(n)}-\pi\|\_{\text{TV}}\leq Ce^{-n/\tau\_{\text{rel}}}, |  | (12) |

where 𝐩(n)\mathbf{p}^{(n)} is the state distribution after nn steps. Fast mixing implies rapid dissipation of initial shock effects, while slow mixing indicates persistent path-dependency in price formation.

#### 3.3.4 Mean Recurrence Time

For each state SiS\_{i}, the mean recurrence time represents the expected return interval [[53](https://arxiv.org/html/2601.04959v1#bib.bib216 "Markov chains")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μi=1πi,i=1,2,…,9.\mu\_{i}=\frac{1}{\pi\_{i}},\quad i=1,2,\ldots,9. |  | (13) |

μi\mu\_{i} values reveal typical cycles of order price aggressiveness, with small μi\mu\_{i} for neutral states indicating frequent orders at current market prices and large values for extreme states reflect rare aggressive adjustments constrained by market impact.

While these metrics effectively quantify the overall dynamic properties, they do not capture the structural similarity between entire transition matrices. To systematically group distinct trading behaviors based on their full probabilistic structure, we reduce the transition data into a lower-dimensional representation suitable for clustering, as detailed in the next subsection. Accordingly, we treat the embedding and clustering steps as complementary tools for comparing entire matrices across time intervals and quote sides, rather than as core modeling contributions.

### 3.4 Dimensionality Reduction of the TPMs

To derive low-dimensional embeddings of the 9×99\times 9 transition probability matrices (TPMs), each TPM is vectorized into 𝐱∈ℝ81\mathbf{x}\in\mathbb{R}^{81} and reduced in two stages. First, we apply Principal Component Analysis (PCA) [[41](https://arxiv.org/html/2601.04959v1#bib.bib36 "Principal component analysis: a review and recent developments")] and retain the top k=8k=8 components (capturing over 95% of the variance), which provides a compact representation and stabilizes the subsequent embedding. Second, the PCA-reduced data are mapped into two dimensions using t-Distributed Stochastic Neighbor Embedding (t-SNE) [[62](https://arxiv.org/html/2601.04959v1#bib.bib41 "Visualizing data using t-sne."), [46](https://arxiv.org/html/2601.04959v1#bib.bib257 "Intraday order transitions across market capitalizations through markov analysis")] to obtain a visualizable representation of similarities across TPMs.

### 3.5 Clustering Techniques for Dimension-Reduced TPMs

To summarize latent structures in the dimension-reduced TPM embeddings, we apply two complementary clustering algorithms using the scikit-learn library [[55](https://arxiv.org/html/2601.04959v1#bib.bib33 "Scikit-learn: machine learning in python")]. First, we use Agglomerative Hierarchical Clustering with Ward’s minimum-variance linkage [[39](https://arxiv.org/html/2601.04959v1#bib.bib44 "Dynamics of hierarchical clustering in stocks market during financial crises")] to obtain a dendrogram that highlights nested similarity patterns between time intervals. Second, we use DBSCAN [[42](https://arxiv.org/html/2601.04959v1#bib.bib25 "Spatio-temporal modeling of seismic provinces of iran using dbscan algorithm"), [46](https://arxiv.org/html/2601.04959v1#bib.bib257 "Intraday order transitions across market capitalizations through markov analysis")] to identify dense groups and potential outliers in the embedding space. These algorithms allow us to group trading time intervals into naturally occurring behavioral phases.

### 3.6 Stationary Distribution Analysis

In an ergodic Markov chain, the long-run behavior is characterized by a stationary distribution, which specifies the steady-state probability associated with each state. Denoting the long-term probability of being in state jj by πj\pi\_{j}, this stationary vector is uniquely determined and must satisfy [[38](https://arxiv.org/html/2601.04959v1#bib.bib159 "Discrete-time markov chain modelling of the ontario air quality health index"), [56](https://arxiv.org/html/2601.04959v1#bib.bib61 "High-frequency stock market order transitions during the us–china trade war 2018: a discrete-time markov chain analysis")]:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | πj\displaystyle\pi\_{j} | =∑i=19πi​pi​j(balance equation),\displaystyle=\sum\_{i=1}^{9}\pi\_{i}p\_{ij}\quad\text{(balance equation)}, |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∑j=19πj\displaystyle\sum\_{j=1}^{9}\pi\_{j} | =1(Normalization condition).\displaystyle=1\quad\text{(Normalization condition)}. |  | (15) |

The stationary probabilities πj\pi\_{j} are computed using the PyDTMC package [[5](https://arxiv.org/html/2601.04959v1#bib.bib35 "PyDTMC")]. To quantify differences between stationary distributions across time intervals, we employ the Jensen–Shannon Divergence (JSD). For two probability distributions pp and qq (each non-negative and summing to one), the JSD is defined as [[52](https://arxiv.org/html/2601.04959v1#bib.bib53 "On the jensen–shannon symmetrization of distances relying on abstract means")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | JSD(p,q)=12[KLD(p∥p+q2)+KLD(q∥p+q2)],\text{JSD}(p,q)=\frac{1}{2}\left[\text{KLD}\left(p\,\middle\|\,\frac{p+q}{2}\right)+\text{KLD}\left(q\,\middle\|\,\frac{p+q}{2}\right)\right], |  | (16) |

where the Kullback–Leibler divergence (KLD) between two discrete distributions uu and vv is

|  |  |  |  |
| --- | --- | --- | --- |
|  | KLD​(u∥v)=∑iui​log2⁡uivi.\text{KLD}(u\|v)=\sum\_{i}u\_{i}\log\_{2}\frac{u\_{i}}{v\_{i}}. |  | (17) |

In this formulation, uiu\_{i} and viv\_{i} correspond to the probabilities assigned to state ii by the distributions uu and vv, respectively. The Jensen-Shannon Divergence is symmetric by definition, takes only non-negative values, and becomes zero precisely when the two distributions coincide [[49](https://arxiv.org/html/2601.04959v1#bib.bib23 "Detecting dynamical changes in time series by using the jensen shannon divergence")].
This distributional analysis enables us to characterize the stable, long-run profile of limit order price revisions and quantify the magnitude of behavioral shifts between different trading intervals. With this comprehensive methodological framework established in Section [3](https://arxiv.org/html/2601.04959v1#S3 "3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"), we now proceed to Section [4](https://arxiv.org/html/2601.04959v1#S4 "4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") to detail the empirical findings derived from the NASDAQ100 dataset.

## 4 Results

How do price adjustments for ask and bid limit orders evolve intraday, and how are these dynamics shaped by market capitalization? To answer this central question, this section presents the empirical results from our discrete-time Markov chain framework. The findings are structured to provide a comparative analysis across the six distinct trading intervals (𝚃𝟷{\mathtt{T\_{1}}}–𝚃𝟼{\mathtt{T\_{6}}}) and the three market capitalization tiers: High (𝙷𝙼𝙲\mathtt{HMC}), Medium (𝙼𝙼𝙲\mathtt{MMC}),
and Low (𝙻𝙼𝙲\mathtt{LMC}).

We begin in Subsection [4.1](https://arxiv.org/html/2601.04959v1#S4.SS1 "4.1 G-test of independence ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") by applying the G-test of independence to validate the presence of short-term memory in price change sequences, establishing that current price adjustments depend statistically on preceding events, thereby justifying the Markov chain modeling approach. Subsection [4.2](https://arxiv.org/html/2601.04959v1#S4.SS2 "4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") examines the structure and dominant elements of the estimated transition probability matrices (TPMs), conducting systematic comparisons both temporally and cross-sectionally across the capitalization tiers. The analysis in Subsection [4.3](https://arxiv.org/html/2601.04959v1#S4.SS3 "4.3 Markov Chain Metrics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") quantifies the dynamic properties of these TPMs through key Markov chain metrics including entropy rate, spectral gap, relaxation time, and mean recurrence times, revealing how convergence speed and predictability patterns vary across temporal and capitalization-size dimensions. Subsection [4.4](https://arxiv.org/html/2601.04959v1#S4.SS4 "4.4 Clustering Analysis of Transition Dynamics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") employs dimensionality reduction techniques i.e. Principal Component Analysis and t-distributed Stochastic Neighbor Embedding, followed by clustering analysis with Hierarchical and DBSCAN algorithms to identify latent structural patterns and classifications within the high-dimensional TPMs. Finally, Subsection [4.5](https://arxiv.org/html/2601.04959v1#S4.SS5 "4.5 Stationary distribution of limit-order price changes ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") analyzes the stationary distributions of limit order price change states across time-intervals and capitalization tiers, utilizing Jensen-Shannon divergence to quantify distributional differences and assess the stability of long-term adjustment patterns.

### 4.1 G-test of independence

To validate the use of Markov chains, we test for temporal dependence by applying the G-test of independence and autocorrelation analysis separately to the ask and bid limit order price change sequences. Tables S1 and S2 in the Supplementary material present the average G-test statistics for ask and bid sequences respectively, calculated across all trading days for each market capitalization tier and time-interval combination. The results demonstrate consistently high G-statistics with p-values well below the 0.05 significance threshold (p≪0.05p\ll 0.05) across all capitalization tiers and time-intervals. These findings provide strong statistical evidence to reject the null hypothesis of independence, confirming that price changes depend significantly on preceding adjustments. This is corroborated by the autocorrelation analysis, which reveals statistically significant correlations at lags 1 and 2, with magnitudes exceeding the 1/N1/\sqrt{N} significance threshold (where NN represents the total number of price change events) [[14](https://arxiv.org/html/2601.04959v1#bib.bib62 "The holt-winters forecasting procedure")]. Although modest, these correlations decay systematically, indicating the presence of short-term memory effects consistent with first-order Markov properties [[6](https://arxiv.org/html/2601.04959v1#bib.bib63 "Statistical methods for data with long-range dependence")].

The convergent evidence from both G-test and autocorrelation analyses validates our approach using first-order discrete-time Markov chains. While higher-order dependencies may exist, the predominant lag-1 correlations justify the first-order assumption, which offers computational tractability while capturing the essential temporal dependencies in limit order price adjustment behaviors. Consequently, we proceed with Maximum Likelihood Estimation of first-order transition probability matrices and systematic comparisons of dominant elements temporally and cross-sectionally across the capitalization tiers as detailed in the following subsection. We restrict our analysis to only D, E, and F price changes as the count of price changes for A, B, C, G, H and I are very low, as shown in Fig.S1 in the supplementary material.

### 4.2 Transition Probability Matrix Analysis

We analyze limit order price changes using a discrete-time Markov chain, with a nine state space defined by the price change magnitudes, as shown in Table [4](https://arxiv.org/html/2601.04959v1#S3.T4 "Table 4 ‣ 3.2 Discrete-Time Markov Chain for Limit Order Price Changes ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"). The transition probability matrices (TPMs) for this chain are estimated via Maximum Likelihood Estimation. The analysis encompasses both bid and ask limit orders across six intraday time-intervals for each of the three market capitalization tiers – 𝙷𝙼𝙲,𝙼𝙼𝙲\mathtt{HMC,MMC}, and 𝙻𝙼𝙲\mathtt{LMC} over twelve trading days. This generates 2,160 individual 9×99\times 9 TPMs, which we aggregate to produce 36 representative matrices: 18 for ask-side changes and 18 for bid-side changes, with six matrices per capitalization tier corresponding to the six time-intervals. Fig. [1](https://arxiv.org/html/2601.04959v1#S4.F1 "Figure 1 ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") presents representative heatmap visualizations of the ask and bid transition probability matrices (TPMs) for the opening interval 𝚃𝟷\mathtt{T\_{1}}. In these matrices, rows correspond to the current price change state and columns to the subsequent state, with cell values indicating transition probabilities. For a comprehensive analysis, the complete set of ask-side TPMs across all capitalization tiers (𝙷𝙼𝙲,𝙼𝙼𝙲,𝙻𝙼𝙲\mathtt{HMC,MMC,LMC}) and time intervals (𝚃𝟷\mathtt{T\_{1}}–𝚃𝟼\mathtt{T\_{6}}) is provided in Supplementary Figures S2 and S3. The corresponding complete set of bid-side TPMs is available in Supplementary Figures S4 and S5.

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

![Refer to caption](x1.png)


(a) Ask – 𝙷𝙼𝙲\mathtt{HMC}

![Refer to caption](x2.png)


(b) Ask – 𝙼𝙼𝙲\mathtt{MMC}

![Refer to caption](x3.png)


(c) Ask – 𝙻𝙼𝙲\mathtt{LMC}

![Refer to caption](x4.png)


(d) Bid – 𝙷𝙼𝙲\mathtt{HMC}

![Refer to caption]()


(e) Bid – 𝙼𝙼𝙲\mathtt{MMC}

![Refer to caption](x6.png)


(f) Bid – 𝙻𝙼𝙲\mathtt{LMC}

Figure 1: Representative heatmap visualizations of transition probability matrices (TPMs) for the opening interval 𝚃𝟷\mathtt{T\_{1}}, displaying Ask (top) and Bid (bottom) limit order price change dynamics across 𝙷𝙼𝙲\mathtt{HMC}, 𝙼𝙼𝙲\mathtt{MMC}, and 𝙻𝙼𝙲\mathtt{LMC} capitalization tiers.

#### 4.2.1 Inertia of Limit Order Prices

Figure [2](https://arxiv.org/html/2601.04959v1#S4.F2 "Figure 2 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") illustrates the temporal variation in the probability of consecutive 0%0\% limit order price changes i.e. price inertia, on both the bid and ask sides. This metric, which captures the likelihood of limit orders maintaining an identical price across successive submissions, shows systematic variations across different time-intervals and market capitalization tiers. The analysis reveals two key empirical findings: Point [1](https://arxiv.org/html/2601.04959v1#S4.I1.i1 "item 1 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") identifies a shared intraday dynamic common to the 𝙷𝙼𝙲,𝙼𝙼𝙲\mathtt{HMC,MMC}, and 𝙻𝙼𝙲\mathtt{LMC}, while Point [2](https://arxiv.org/html/2601.04959v1#S4.I1.i2 "item 2 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") highlights the distinct characteristics for each capitalization tier.

![Refer to caption](x7.png)


Figure 2: Temporal variation of transition probability for consecutive 0%0\% limit order price changes across market capitalization tiers and time intervals.

1. 1.

   Intraday limit order price change transition dynamics: We observed a consistent temporal pattern in the transition probability for consecutive 0%0\% price changes across all market capitalization tiers for both bid and ask sides, as summarized below:

   1. (a)

      Price inertia peaks at market opening 𝚃𝟷{\mathtt{T\_{1}}} indicating a strong tendency for limit orders to be submitted consecutively at the same price. This behavior likely reflects defensive positioning at anticipated support and resistance levels. Heightened opening volatility, driven by the assimilation of overnight news and information asymmetries, creates uncertainty that encourages defensive positioning outside the spread and concentration of orders at specific price points to avoid adverse selection costs [[50](https://arxiv.org/html/2601.04959v1#bib.bib192 "An analysis of intraday patterns in bid/ask spreads for nyse stocks"), [31](https://arxiv.org/html/2601.04959v1#bib.bib155 "Bid, ask and transaction prices in a specialist market with heterogeneously informed traders")].
   2. (b)

      The inertia probability declines sharply post-open and stabilizes at a lower level throughout the midday session i.e. 𝚃𝟸{\mathtt{T\_{2}}} – 𝚃𝟻{\mathtt{T\_{5}}}. The initial decrease aligns with the dynamic price discovery process, where high volatility and fluctuating bid-ask spreads necessitate frequent limit order price adjustments, reducing the repetition of orders at the same price. As the market absorbs new information, volatility subsides and spread narrows [[4](https://arxiv.org/html/2601.04959v1#bib.bib154 "Intraday periodicity and volatility persistence in financial markets"), [50](https://arxiv.org/html/2601.04959v1#bib.bib192 "An analysis of intraday patterns in bid/ask spreads for nyse stocks")]. This post-discovery environment fosters more heterogeneous trading conditions where diverse participants employ mixed strategies, leading to dispersed order placement and a stable, lower probability of consecutive submissions at identical prices.
   3. (c)

      Finally, the inertia surges during the closing hour 𝚃𝟼{\mathtt{T\_{6}}}, often exceeding the opening peak. This resurgence is driven by intense end-of-day portfolio rebalancing, as the urgency to close positions and mitigate overnight risk prompts market participants to submit orders at key price levels to ensure execution [[54](https://arxiv.org/html/2601.04959v1#bib.bib156 "A closing call’s impact on market quality at euronext paris"), [40](https://arxiv.org/html/2601.04959v1#bib.bib157 "Closing auctions: nasdaq versus nyse")]. This strategic shift prioritizes order fulfillment over price optimization, leading to a pronounced reduction in price adjustments and a corresponding peak in the probability of consecutive submissions at the same price.
2. 2.

   Differences in price change transition dynamics between 𝙷𝙼𝙲\mathtt{HMC}, 𝙼𝙼𝙲\mathtt{MMC}, and 𝙻𝙼𝙲\mathtt{LMC} stocks: Cross-capitalization analysis reveals systematic differences in these dynamics that persist across all trading time intervals, reflecting the distinct characteristics of each market tier.

   1. (a)

      A strong capitalization gradient is observed; 𝙷𝙼𝙲\mathtt{HMC} stocks exhibit the strongest price inertia, followed by 𝙼𝙼𝙲\mathtt{MMC} and then 𝙻𝙼𝙲\mathtt{LMC} stocks. This hierarchy reflects fundamental differences in their market structure. Greater liquidity and trading volume in 𝙷𝙼𝙲\mathtt{HMC} stocks attract sophisticated participants, including market makers and high-frequency traders. These agents provide continuous liquidity by maintaining persistent limit orders at specific prices, resulting in a relatively high self-transition probabilities i.e. higher inertia. Conversely, 𝙻𝙼𝙲\mathtt{LMC} stocks exhibit the lowest probability of consecutive unchanged prices. Lower liquidity, relatively higher transaction costs, and greater information asymmetries discourage passive order placement. This necessitates dynamic order management, where participants frequently adjust prices to mitigate risk, resulting in systematically lower inertia.
   2. (b)

      A bid-ask asymmetry gradient is evident, scaling from minimal in 𝙷𝙼𝙲\mathtt{HMC} stocks to maximal in 𝙻𝙼𝙲\mathtt{LMC} stocks. For 𝙻𝙼𝙲\mathtt{LMC} stocks, ask-side transition probabilities consistently exceed bid-side probabilities across all intervals. This pattern is likely driven by three factors specific to illiquid stocks: market makers maintain persistent ask limit orders to manage inventory risk [[36](https://arxiv.org/html/2601.04959v1#bib.bib218 "Optimal dealer pricing under transactions and return uncertainty")], greater information asymmetry increases adverse selection costs on the bid side [[27](https://arxiv.org/html/2601.04959v1#bib.bib57 "Liquidity, information, and infrequently traded stocks")], and institutional frictions like short-selling costs disproportionately hinder bid-side liquidity provision [[10](https://arxiv.org/html/2601.04959v1#bib.bib219 "Which shorts are informed?")]. Collectively, these factors heighten the observed price inertia of ask-side limit orders.

In summary, these findings demonstrate that limit order price change inertia is not random but follows predictable U-shaped intraday patterns and a distinct capitalization gradient. The results show that high-capitalization stocks exhibit the greatest price stability due to deep, continuous liquidity, whereas low-capitalization stocks are characterized by lower overall stability and significant bid-ask asymmetries. For traders, this implies that execution strategies can be optimized by anticipating higher price persistence during the market opening and closing hours, particularly in 𝙷𝙼𝙲\mathtt{HMC} stocks, while accounting for both the lower stability and the dominant ask-side inertia inherent to 𝙻𝙼𝙲\mathtt{LMC} stocks.

#### 4.2.2 Directional Momentum of Limit Order Price Revisions

Figure [3](https://arxiv.org/html/2601.04959v1#S4.F3 "Figure 3 ‣ 4.2.2 Directional Momentum of Limit Order Price Revisions ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") illustrates transition probabilities from neutral i.e. 0%0\% price change, to both negative and positive price changes across market capitalization tiers and intraday intervals. We point out two key empirical findings from this analysis: Point [1](https://arxiv.org/html/2601.04959v1#S4.I2.i1 "item 1 ‣ 4.2.2 Directional Momentum of Limit Order Price Revisions ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") examines the systematic capitalization-based hierarchy in price revision intensity, while Point [2](https://arxiv.org/html/2601.04959v1#S4.I2.i2 "item 2 ‣ 4.2.2 Directional Momentum of Limit Order Price Revisions ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") analyzes subtle bid-ask asymmetries in directional transition behaviors.

![Refer to caption](x8.png)


(a) 0%0\% price change to both negative price change.

![Refer to caption](x9.png)


(b) 0%0\% price change to both negative price change.

Figure 3: Transition probabilities from neutral i.e. 0%0\% price change, to both negative and positive price changes across market capitalization tiers and intraday intervals.

1. 1.

   Hierarchy in Revision Intensity: Cross analysis reveals a systematic ordering in directional transition probabilities that persist across all trading time intervals and capitalization tiers, that reflects the distinct characteristics, as elaborated below.

   1. (a)

      Temporally, the intraday evolution patterns reveal distinctive opening hour dynamics where 𝙷𝙼𝙲\mathtt{HMC} and 𝙼𝙼𝙲\mathtt{MMC} stocks show significant increases in directional transitions: 4.0%–5.0% for defensive positioning, and 1.0%–1.5% for aggressive positioning, while 𝙻𝙼𝙲\mathtt{LMC} stocks exhibit contrarian behavior with slight decreases. This divergence suggests differential responses to opening volatility and information asymmetries, with 𝙻𝙼𝙲\mathtt{LMC} traders adopting more conservative adjustment strategies during high-uncertainty hours [[50](https://arxiv.org/html/2601.04959v1#bib.bib192 "An analysis of intraday patterns in bid/ask spreads for nyse stocks"), [4](https://arxiv.org/html/2601.04959v1#bib.bib154 "Intraday periodicity and volatility persistence in financial markets")].
   2. (b)

      In terms of capitalization asymmetry, we observed that 𝙻𝙼𝙲\mathtt{LMC} stocks exhibit the highest directional transition probabilities, demonstrating elevated limit order price revision frequencies. The elevated revision frequency in 𝙻𝙼𝙲\mathtt{LMC} stocks stems from their market microstructure: wider bid-ask spreads, higher volatility, limited liquidity, and reduced market maker presence. These conditions create larger gaps between optimal execution prices and current market levels, necessitating more frequent price adjustments to maintain execution viability [[3](https://arxiv.org/html/2601.04959v1#bib.bib185 "Illiquidity and stock returns: cross-section and time-series effects")]. On the other hand, 𝙷𝙼𝙲\mathtt{HMC} stocks exhibit the lowest revision frequencies, reflecting their stable market environment characterized by narrower spreads, higher liquidity, and greater institutional presence. The enhanced market maker activity maintains stable pricing conditions, creating extended periods of order competitiveness that reduce revision incentives [[51](https://arxiv.org/html/2601.04959v1#bib.bib34 "High frequency trading and the new market makers")].
2. 2.

   Subtle Bid-Ask Asymmetries in Directional Revisions: We identify two subtle but persistent bid-ask asymmetries, formalized as:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | P(Bid:Neutral→Negative)\displaystyle P(\text{Bid}:\text{Neutral}\to\text{Negative}) | ≳P(Ask:Neutral→Negative)\displaystyle\gtrsim P(\text{Ask}:\text{Neutral}\to\text{Negative}) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | P(Ask:Neutral→Positive)\displaystyle P(\text{Ask}:\text{Neutral}\to\text{Positive}) | ≳P(Bid:Neutral→Positive)\displaystyle\gtrsim P(\text{Bid}:\text{Neutral}\to\text{Positive}) |  |

   where ≳\gtrsim denotes a modest but persistent difference. This pattern reflect nuanced differences in trading behaviors:

   1. (a)

      The first inequality reflects a stronger value-seeking motive among buyers, who are more prone to lowering their bids to improve entry prices.
   2. (b)

      The second inequality reveals a stronger profit-maximizing motive among sellers, who are more prone to raising their asks to capture better execution.

These empirical findings provide guidance for optimizing order management for traders while navigating different market capitalization segments. The dominant capitalization hierarchy implies that static, patient order placement is a viable strategy in 𝙷𝙼𝙲\mathtt{HMC} stocks, whereas the high revision frequency in 𝙻𝙼𝙲\mathtt{LMC} stocks necessitates dynamic, adaptive strategies to manage execution risk. This contrast is sharpest at the market open, where 𝙻𝙼𝙲\mathtt{LMC} traders turn conservative, while 𝙷𝙼𝙲\mathtt{HMC} traders actively reposition. The subtle, persistent bid-ask asymmetries can be used to fine-tune price-shading logic, accounting for the slight but predictable value-seeking (bid) and profit-maximizing (ask) tendencies of other participants.

### 4.3 Markov Chain Metrics

We now compute key Markov chain metrics. While the analysis of individual transition probabilities characterize local, state-to-state transitions, these metrics quantify the global dynamic properties of the price change process.

#### 4.3.1 Spectral Gap, Relaxation and Mixing

The spectral gap γ\gamma is analyzed to measure the convergence speed to equilibrium, which serves as a proxy for price discovery efficiency. This metric exhibits a clear intraday pattern inverted relative to volatility. As shown in Table [5](https://arxiv.org/html/2601.04959v1#S4.T5 "Table 5 ‣ 4.3.1 Spectral Gap, Relaxation and Mixing ‣ 4.3 Markov Chain Metrics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"), the gap is smallest at the market open (𝚃𝟷\mathtt{T\_{1}}; γ≈0.56\gamma\approx 0.56–0.600.60), indicating the slowest convergence during high-information assimilation. It peaks midday (𝚃𝟹\mathtt{T\_{3}}–𝚃𝟺\mathtt{T\_{4}}; γ≈0.71\gamma\approx 0.71–0.740.74), reflecting the fastest convergence, before declining slightly at the close (𝚃𝟼\mathtt{T\_{6}}; γ≈0.65\gamma\approx 0.65–0.690.69). In terms of capitalization, 𝙷𝙼𝙲\mathtt{HMC} and 𝙼𝙼𝙲\mathtt{MMC} stocks exhibit slightly larger spectral gaps than 𝙻𝙼𝙲\mathtt{LMC} stocks during active trading (𝚃𝟸\mathtt{T\_{2}}–𝚃𝟻\mathtt{T\_{5}}), consistent with more efficient price discovery in higher-liquidity assets. Further, bid-ask differences in γ\gamma are modest (≲0.05\lesssim 0.05) and secondary to the primary temporal and capitalization patterns.

For completeness, we also report complementary measures: Mixing rate, λ⋆=1−γ\lambda\_{\star}=1-\gamma and the relaxation time, τ=1/γ\tau=1/\gamma in Table [5](https://arxiv.org/html/2601.04959v1#S4.T5 "Table 5 ‣ 4.3.1 Spectral Gap, Relaxation and Mixing ‣ 4.3 Markov Chain Metrics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"). As the relaxation rate is defined as κ≡1/τ=γ\kappa\equiv 1/\tau=\gamma , κ\kappa is numerically identical to the spectral gap, while λ⋆\lambda\_{\star} is a linear reparameterization. Accordingly, these metrics are all complementary: a high mixing rate corresponds to a long relaxation time and a small spectral gap, indicating slow convergence. We include these for readers who prefer those conventions rather than as distinct metrics.

Table 5: Key Markov chain metrics to quantify the global dynamic properties of the price change process.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Market-  Capitalization  Tier | Time-  Interval | Spectral Gap | | Relaxation Rate | | Entropy Rate | | Mixing Rate | |
|  |  | Ask | Bid | Ask | Bid | Ask | Bid | Ask | Bid |
| 𝙷𝙼𝙲\mathtt{HMC} | 𝚃𝟷\mathtt{T\_{1}} | 0.5620.562 | 0.5660.566 | 0.8250.825 | 0.8350.835 | 1.0321.032 | 1.0511.051 | 0.4380.438 | 0.4340.434 |
| 𝚃𝟸\mathtt{T\_{2}} | 0.7380.738 | 0.7190.719 | 1.3411.341 | 1.2681.268 | 1.0381.038 | 1.0591.059 | 0.2620.262 | 0.2810.281 |
| 𝚃𝟹\mathtt{T\_{3}} | 0.7400.740 | 0.6950.695 | 1.3451.345 | 1.1881.188 | 1.0351.035 | 1.0541.054 | 0.2600.260 | 0.3050.305 |
| 𝚃𝟺\mathtt{T\_{4}} | 0.7440.744 | 0.7150.715 | 1.3631.363 | 1.2541.254 | 1.0391.039 | 1.0461.046 | 0.2560.256 | 0.2850.285 |
| 𝚃𝟻\mathtt{T\_{5}} | 0.7250.725 | 0.6900.690 | 1.2901.290 | 1.1721.172 | 1.0301.030 | 1.0561.056 | 0.2750.275 | 0.3100.310 |
| 𝚃𝟼\mathtt{T\_{6}} | 0.6920.692 | 0.6510.651 | 1.1771.177 | 1.0531.053 | 0.9840.984 | 1.0211.021 | 0.3080.308 | 0.3490.349 |
| 𝙼𝙼𝙲\mathtt{MMC} | 𝚃𝟷\mathtt{T\_{1}} | 0.5900.590 | 0.5950.595 | 0.8910.891 | 0.9040.904 | 1.0891.089 | 1.1121.112 | 0.4100.410 | 0.4050.405 |
| 𝚃𝟸\mathtt{T\_{2}} | 0.7110.711 | 0.7160.716 | 1.2401.240 | 1.2601.260 | 1.0781.078 | 1.0811.081 | 0.2890.289 | 0.2840.284 |
| 𝚃𝟹\mathtt{T\_{3}} | 0.7270.727 | 0.7300.730 | 1.2991.299 | 1.3091.309 | 1.0741.074 | 1.0781.078 | 0.2730.273 | 0.2700.270 |
| 𝚃𝟺\mathtt{T\_{4}} | 0.7080.708 | 0.7090.709 | 1.2291.229 | 1.2351.235 | 1.0841.084 | 1.0771.077 | 0.2920.292 | 0.2910.291 |
| 𝚃𝟻\mathtt{T\_{5}} | 0.6790.679 | 0.6890.689 | 1.1351.135 | 1.1701.170 | 1.0691.069 | 1.0761.076 | 0.3210.321 | 0.3110.311 |
| 𝚃𝟼\mathtt{T\_{6}} | 0.6690.669 | 0.6710.671 | 1.1061.106 | 1.1111.111 | 1.0301.030 | 1.0411.041 | 0.3310.331 | 0.3290.329 |
| 𝙻𝙼𝙲\mathtt{LMC} | 𝚃𝟷\mathtt{T\_{1}} | 0.5620.562 | 0.5670.567 | 0.8250.825 | 0.8380.838 | 1.1521.152 | 1.1621.162 | 0.4380.438 | 0.4330.433 |
| 𝚃𝟸\mathtt{T\_{2}} | 0.6930.693 | 0.7050.705 | 1.1811.181 | 1.2221.222 | 1.1241.124 | 1.1081.108 | 0.3070.307 | 0.2950.295 |
| 𝚃𝟹\mathtt{T\_{3}} | 0.6940.694 | 0.7170.717 | 1.1851.185 | 1.2631.263 | 1.1081.108 | 1.1161.116 | 0.3060.306 | 0.2830.283 |
| 𝚃𝟺\mathtt{T\_{4}} | 0.7130.713 | 0.6950.695 | 1.2471.247 | 1.1871.187 | 1.1131.113 | 1.1051.105 | 0.2870.287 | 0.3050.305 |
| 𝚃𝟻\mathtt{T\_{5}} | 0.6980.698 | 0.6800.680 | 1.1961.196 | 1.1401.140 | 1.1051.105 | 1.1151.115 | 0.3020.302 | 0.3200.320 |
| 𝚃𝟼\mathtt{T\_{6}} | 0.6870.687 | 0.6660.666 | 1.1611.161 | 1.0971.097 | 1.0731.073 | 1.1081.108 | 0.3130.313 | 0.3340.334 |

#### 4.3.2 Entropy Rate

The entropy rate is analyzed to quantify the unpredictability of the price change sequence. As seen from Table [5](https://arxiv.org/html/2601.04959v1#S4.T5 "Table 5 ‣ 4.3.1 Spectral Gap, Relaxation and Mixing ‣ 4.3 Markov Chain Metrics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"), there is a clear capitalization hierarchy. 𝙻𝙼𝙲\mathtt{LMC} stocks consistently exhibit the highest entropy rates, followed by 𝙼𝙼𝙲\mathtt{MMC}, and 𝙷𝙼𝙲\mathtt{HMC}. This gradient confirms that price change dynamics are least predictable in 𝙻𝙼𝙲\mathtt{LMC} stocks and most structured in 𝙷𝙼𝙲\mathtt{HMC} stocks, reflecting underlying differences in market depth and information asymmetry. Temporally, entropy rates are highest at 𝚃𝟷\mathtt{T\_{1}} and generally decline toward 𝚃𝟼\mathtt{T\_{6}}, suggesting a shift from information-heavy assimilation to more orderly, execution-driven trading. Further, bid-side entropy rates are marginally higher than ask-side, indicating slightly greater unpredictability in buy-side pricing, though this effect remains secondary.

Table 6: Mean recurrence times for each limit order price change state in the Markov chain.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Market-  Capitalization  Tier | Time-  Interval | S1S\_{1} | | S2S\_{2} | | S3S\_{3} | | S4S\_{4} | | S5S\_{5} | | S6S\_{6} | | S7S\_{7} | | S8S\_{8} | | S9S\_{9} | |
|  |  | Ask | Bid | Ask | Bid | Ask | Bid | Ask | Bid | Ask | Bid | Ask | Bid | Ask | Bid | Ask | Bid | Ask | Bid |
| 𝙷𝙼𝙲\mathtt{HMC} | 𝚃𝟷\mathtt{T\_{1}} | 487.9487.9 | 297.4297.4 | 598.2598.2 | 306.1306.1 | 215.1215.1 | 139.2139.2 | 3.83.8 | 3.73.7 | 2.22.2 | 2.32.3 | 3.83.8 | 3.83.8 | 190.0190.0 | 159.7159.7 | 549.3549.3 | 352.1352.1 | 482.1482.1 | 294.0294.0 |
| 𝚃𝟸\mathtt{T\_{2}} | 750.1750.1 | 380.4380.4 | 607.8607.8 | 345.3345.3 | 216.9216.9 | 134.3134.3 | 3.63.6 | 3.63.6 | 2.32.3 | 2.42.4 | 3.63.6 | 3.63.6 | 214.1214.1 | 135.1135.1 | 597.0597.0 | 346.6346.6 | 697.2697.2 | 377.8377.8 |
| 𝚃𝟹\mathtt{T\_{3}} | 753.6753.6 | 378.4378.4 | 623.2623.2 | 393.6393.6 | 215.3215.3 | 143.1143.1 | 3.73.7 | 3.73.7 | 2.22.2 | 2.32.3 | 3.73.7 | 3.73.7 | 208.5208.5 | 146.0146.0 | 647.1647.1 | 380.9380.9 | 713.5713.5 | 380.0380.0 |
| 𝚃𝟺\mathtt{T\_{4}} | 641.3641.3 | 463.1463.1 | 495.8495.8 | 570.2570.2 | 224.8224.8 | 158.6158.6 | 3.83.8 | 3.63.6 | 2.22.2 | 2.32.3 | 3.73.7 | 3.73.7 | 216.3216.3 | 161.8161.8 | 540.6540.6 | 526.6526.6 | 604.0604.0 | 463.6463.6 |
| 𝚃𝟻\mathtt{T\_{5}} | 887.4887.4 | 368.4368.4 | 641.6641.6 | 484.4484.4 | 284.4284.4 | 140.9140.9 | 3.73.7 | 3.63.6 | 2.32.3 | 2.32.3 | 3.73.7 | 3.73.7 | 277.2277.2 | 142.4142.4 | 738.0738.0 | 442.4442.4 | 751.0751.0 | 377.9377.9 |
| 𝚃𝟼\mathtt{T\_{6}} | 620.1620.1 | 305.1305.1 | 531.7531.7 | 278.0278.0 | 328.8328.8 | 161.2161.2 | 4.14.1 | 4.14.1 | 2.02.0 | 2.02.0 | 4.14.1 | 4.24.2 | 327.7327.7 | 146.0146.0 | 552.4552.4 | 273.3273.3 | 605.1605.1 | 292.6292.6 |
| 𝙼𝙼𝙲\mathtt{MMC} | 𝚃𝟷\mathtt{T\_{1}} | 364.3364.3 | 263.2263.2 | 540.1540.1 | 377.4377.4 | 192.3192.3 | 121.4121.4 | 3.33.3 | 3.23.2 | 2.82.8 | 2.82.8 | 3.23.2 | 3.33.3 | 165.1165.1 | 133.0133.0 | 560.6560.6 | 443.6443.6 | 359.7359.7 | 274.6274.6 |
| 𝚃𝟸\mathtt{T\_{2}} | 696.5696.5 | 386.2386.2 | 446.5446.5 | 483.9483.9 | 163.8163.8 | 158.9158.9 | 3.03.0 | 3.13.1 | 3.23.2 | 3.03.0 | 3.03.0 | 3.13.1 | 167.0167.0 | 156.3156.3 | 478.3478.3 | 474.5474.5 | 685.8685.8 | 392.2392.2 |
| 𝚃𝟹\mathtt{T\_{3}} | 809.2809.2 | 402.6402.6 | 429.9429.9 | 449.2449.2 | 177.4177.4 | 179.4179.4 | 3.23.2 | 3.23.2 | 2.92.9 | 2.92.9 | 3.13.1 | 3.23.2 | 183.3183.3 | 173.7173.7 | 444.5444.5 | 403.6403.6 | 760.6760.6 | 399.6399.6 |
| 𝚃𝟺\mathtt{T\_{4}} | 845.3845.3 | 428.4428.4 | 410.6410.6 | 447.8447.8 | 140.5140.5 | 194.4194.4 | 3.23.2 | 3.23.2 | 2.92.9 | 2.82.8 | 3.13.1 | 3.23.2 | 152.3152.3 | 180.8180.8 | 480.3480.3 | 392.1392.1 | 751.9751.9 | 490.5490.5 |
| 𝚃𝟻\mathtt{T\_{5}} | 860.3860.3 | 456.9456.9 | 531.8531.8 | 510.4510.4 | 178.9178.9 | 165.0165.0 | 3.23.2 | 3.23.2 | 2.92.9 | 2.82.8 | 3.13.1 | 3.33.3 | 190.8190.8 | 151.6151.6 | 615.4615.4 | 490.2490.2 | 760.1760.1 | 513.9513.9 |
| 𝚃𝟼\mathtt{T\_{6}} | 675.6675.6 | 360.0360.0 | 577.3577.3 | 414.6414.6 | 252.8252.8 | 208.1208.1 | 3.53.5 | 3.53.5 | 2.52.5 | 2.42.4 | 3.43.4 | 3.53.5 | 241.9241.9 | 223.5223.5 | 622.9622.9 | 399.0399.0 | 645.7645.7 | 362.1362.1 |
| 𝙻𝙼𝙲\mathtt{LMC} | 𝚃𝟷\mathtt{T\_{1}} | 224.4224.4 | 267.2267.2 | 380.5380.5 | 303.3303.3 | 108.0108.0 | 84.184.1 | 3.13.1 | 2.92.9 | 3.33.3 | 3.53.5 | 2.92.9 | 3.03.0 | 101.2101.2 | 90.290.2 | 386.6386.6 | 319.1319.1 | 208.1208.1 | 266.9266.9 |
| 𝚃𝟸\mathtt{T\_{2}} | 329.5329.5 | 1051.31051.3 | 376.5376.5 | 498.4498.4 | 110.7110.7 | 119.6119.6 | 2.92.9 | 2.82.8 | 3.53.5 | 3.63.6 | 2.92.9 | 2.92.9 | 115.6115.6 | 116.0116.0 | 419.8419.8 | 438.6438.6 | 295.4295.4 | 1003.71003.7 |
| 𝚃𝟹\mathtt{T\_{3}} | 419.2419.2 | 869.1869.1 | 468.2468.2 | 399.2399.2 | 151.0151.0 | 112.2112.2 | 3.03.0 | 2.92.9 | 3.33.3 | 3.43.4 | 2.92.9 | 3.03.0 | 151.6151.6 | 108.5108.5 | 520.9520.9 | 401.5401.5 | 356.3356.3 | 727.9727.9 |
| 𝚃𝟺\mathtt{T\_{4}} | 456.1456.1 | 723.3723.3 | 443.3443.3 | 394.0394.0 | 125.9125.9 | 144.8144.8 | 3.03.0 | 2.92.9 | 3.33.3 | 3.53.5 | 2.92.9 | 2.92.9 | 129.2129.2 | 132.2132.2 | 517.7517.7 | 352.9352.9 | 375.0375.0 | 666.3666.3 |
| 𝚃𝟻\mathtt{T\_{5}} | 441.8441.8 | 581.1581.1 | 497.6497.6 | 381.7381.7 | 141.3141.3 | 120.8120.8 | 3.03.0 | 2.92.9 | 3.33.3 | 3.53.5 | 2.92.9 | 2.92.9 | 151.0151.0 | 105.9105.9 | 576.0576.0 | 356.3356.3 | 343.4343.4 | 534.4534.4 |
| 𝚃𝟼\mathtt{T\_{6}} | 373.8373.8 | 362.1362.1 | 506.7506.7 | 291.3291.3 | 189.3189.3 | 112.2112.2 | 3.23.2 | 3.13.1 | 2.82.8 | 2.92.9 | 3.23.2 | 3.23.2 | 175.9175.9 | 115.3115.3 | 505.8505.8 | 306.9306.9 | 353.6353.6 | 346.9346.9 |

#### 4.3.3 Mean Recurrence Time

Finally, we analyze the mean recurrence times (MRT), which measures the average number of steps required for the process to return to a given state. As shown in Table [6](https://arxiv.org/html/2601.04959v1#S4.T6 "Table 6 ‣ 4.3.2 Entropy Rate ‣ 4.3 Markov Chain Metrics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"), the MRTs clearly distinguish between neutral, mild, and extreme limit-order price change states across intraday intervals, market-capitalization tiers, and order side. The intraday dynamics show opposing trends at the market close: neutral-state S5S\_{5} MRTs compress, for example 𝙷𝙼𝙲\mathtt{HMC} shortens from  2.3 to 2.0 steps, due to execution urgency, while mild-states S4S\_{4} and S6S\_{6} MRTs lengthen, for example 𝙷𝙼𝙲\mathtt{HMC} from  3.7 to 4.1 steps, as price fine-tuning subsides. Extreme states are most frequent, having the shortest MRT, at the open 𝚃𝟷\mathtt{T\_{1}}, aligning with high initial volatility, a pattern most pronounced in 𝙻𝙼𝙲\mathtt{LMC} stocks, such as the Ask state S1S\_{1} MRT of 224.4.

Neutral changes, represented by state S5S\_{5}, recur most frequently with a capitalization hierarchy: 𝙷𝙼𝙲:\mathtt{HMC:} 2.0–2.4 steps, 𝙼𝙼𝙲:\mathtt{MMC:} 2.4–3.2, and 𝙻𝙼𝙲:\mathtt{LMC:} 2.8–3.6. This pattern reflects more stable order maintenance in liquid stocks, whereas thinner 𝙻𝙼𝙲\mathtt{LMC} order books require more frequent non-neutral revisions. Mild adjustments, i.e. states S4S\_{4} and S6S\_{6}, show an inverted pattern, occurring most often in 𝙻𝙼𝙲\mathtt{LMC} stocks at 2.9–3.2 steps, consistent with continuous fine-tuning under wider spreads. Moderate states i.e. S3S\_{3} and S7S\_{7} lie between these benchmarks. Extreme states S1,S2,S8S\_{1},S\_{2},S\_{8}, and S9S\_{9} are rare, with mean recurrence measured in hundreds of steps, in all the cases. Further, a pronounced bid-ask asymmetry appears, primarily in 𝙻𝙼𝙲\mathtt{LMC} extremes. For example, at 𝚃𝟸\mathtt{T\_{2}}, an extreme negative revision i.e. state S1S\_{1} recurs in 329.5 steps on the ask side versus 1051.3 steps on the bid side. This is consistent with traders posting less aggressive bid-side limit orders to avoid accumulating long inventory in illiquid stocks.

In summary, these Markov chain metrics quantify the global dynamics of limit order price change process, confirming a clear capitalization hierarchy. 𝙷𝙼𝙲\mathtt{HMC} stocks are characterized by efficient price discovery with high γ\gamma, relatively higher predictability from low HH, and stable persistence from low S5S\_{5} MRT, supporting patient, queue-joining trading strategies. Conversely, 𝙻𝙼𝙲\mathtt{LMC} stocks show a turbulent, less efficient regime with lower γ\gamma and higher HH, and a rapid recurrence of mild adjustments, evident from low S4S\_{4} and S6S\_{6} MRT, which necessitates dynamic, price-adaptive order management. The extreme bid-side scarcity in 𝙻𝙼𝙲\mathtt{LMC} further warrants more conservative bidding, while the universal compression of neutral-state recurrence times at market close requires intensified monitoring across all tiers as execution urgency increases.

### 4.4 Clustering Analysis of Transition Dynamics

We now examine the collective similarity of transition probability matrices (TPMs) through clustering. This examination identifies natural groupings in limit order price change behaviors across time intervals and market capitalization tiers. Each 9×99\times 9 TPM is flattened into an 81-dimensional vector, yielding 18 vectors per side i.e., 6 intervals ×\times 3 tiers. We then reduce the dimensionality of the TPMs using principal component analysis (PCA) where only 9 components are retain, followed by t-distributed stochastic neighbor embedding (t-SNE) for 2D visualization as shown in Fig. [4(a)](https://arxiv.org/html/2601.04959v1#S4.F4.sf1 "In Figure 4 ‣ 4.4 Clustering Analysis of Transition Dynamics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") and [4(b)](https://arxiv.org/html/2601.04959v1#S4.F4.sf2 "In Figure 4 ‣ 4.4 Clustering Analysis of Transition Dynamics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"), for ask and bid sides, respectively. We then apply hierarchical agglomerative clustering and DBSCAN to these embeddings.

![Refer to caption](x10.png)


(a) Ask-side PCA–t-SNE

![Refer to caption](x11.png)


(b) Bid-side PCA–t-SNE

Figure 4: Two-dimensional embeddings of transition probability matrices (TPM) obtained by PCA (9 components) followed by t-SNE, for (a) ask-side and (b) bid-side limit orders. Each point represents a TPM for one of the six intraday intervals, T1, T2, .., T6 and one of the three market capitalization tiers, High, Medium and Low.

Hierarchical clustering reveals significant ask-bid side differences in temporal structure, as shown in Figs. [5(a)](https://arxiv.org/html/2601.04959v1#S4.F5.sf1 "In Figure 5 ‣ 4.4 Clustering Analysis of Transition Dynamics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") and [5(b)](https://arxiv.org/html/2601.04959v1#S4.F5.sf2 "In Figure 5 ‣ 4.4 Clustering Analysis of Transition Dynamics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"). The bid side exhibits greater heterogeneity, with linkage distances ranging 0−7000-700 versus 0−4000-400 on the ask side. Despite this, the bid side shows clear temporal segmentation. Opening 𝚃𝟷\mathtt{T\_{1}} and closing 𝚃𝟼\mathtt{T\_{6}} hours form distinct clusters. Midday trading hours i.e., 𝚃𝟸\mathtt{T\_{2}}–𝚃𝟻\mathtt{T\_{5}} consolidates into a single cluster. In contrast, the ask side displays more complex temporal dynamics. Midday intervals (𝚃𝟸\mathtt{T\_{2}}–𝚃𝟺\mathtt{T\_{4}}) show extensive interleaving. The pre-closing hour i.e. 𝚃𝟻\mathtt{T\_{5}} separates from midday to cluster with the closing hour 𝚃𝟼\mathtt{T\_{6}}. This suggests that sellers initiate end-of-day positioning strategies earlier than the formal closing hour.

![Refer to caption](x12.png)


(a) Ask-side dendrogram

![Refer to caption](x13.png)


(b) Bid-side dendrogram

Figure 5: Hierarchical clustering dendrograms. The Bid tree spans a larger distance range (≈0\approx 0–≈700\approx 700) than Ask (≈0\approx 0–≈400\approx 400), indicating greater heterogeneity on Bid. In both trees, T1T\_{1}, T5T\_{5}, T6T\_{6} appear as tight triplets. Ask shows heavier interleaving among T2T\_{2}, T3T\_{3}, T4T\_{4}; Bid forms cleaner adjacent sub-blocks for T2T\_{2} and T3T\_{3}, with T4T\_{4} bridging.

DBSCAN analysis reinforces this key temporal asymmetry. The bid side produces three well-separated, dense clusters corresponding to the traditional trading sessions: Opening 𝚃𝟷\mathtt{T\_{1}}, Midday from 𝚃𝟸\mathtt{T\_{2}} to 𝚃𝟻\mathtt{T\_{5}}, and Closing 𝚃𝟼\mathtt{T\_{6}}. In contrast, the ask side yields four distinct clusters: Opening 𝚃𝟷\mathtt{T\_{1}}, Midday from 𝚃𝟸\mathtt{T\_{2}} to 𝚃𝟺\mathtt{T\_{4}}, and two separate end-of-day clusters: Pre-Close 𝚃𝟻\mathtt{T\_{5}} and Close 𝚃𝟼\mathtt{T\_{6}}. The clear separation of 𝚃𝟻\mathtt{T\_{5}} on the ask side provides data-driven evidence that sellers begin strategic preparations for the closing open positions significantly earlier than buyers.

![Refer to caption](x14.png)


(a) Ask-side DBSCAN

![Refer to caption](x15.png)


(b) Bid-side DBSCAN

Figure 6: DBSCAN on the PCA–t-SNE embeddings. With a common ε\varepsilon/minPts, Bid’s broader, more separable layout yields clearer Opening/Midday/Closing islands; Ask’s tighter layout produces more mid-interval blending unless ε\varepsilon is reduced.

In summary, these clustering patterns reveal that market dynamics are primarily driven by time-of-day and order side, with market capitalization playing a secondary role. A key finding is the greater heterogeneity of the bid side, which nonetheless organizes into a clear, three-regime structure: Opening 𝚃𝟷\mathtt{T\_{1}}, Midday 𝚃𝟸\mathtt{T\_{2}}–𝚃𝟻\mathtt{T\_{5}}, and Closing 𝚃𝟼\mathtt{T\_{6}}, that supports structured execution algorithms with predictable transition points. Conversely, the ask side, while more homogeneous, displays a more complex, four-regime structure defined by the early emergence of a 𝚃𝟻\mathtt{T\_{5}} pre-closing dynamic, implying sellers begin position unwinding earlier. For traders, this necessitates asymmetric timing: bid-side logic can follow the standard intraday pattern, while ask-side logic must anticipate this early shift to closing dynamics.

### 4.5 Stationary distribution of limit-order price changes

Having identified distinct temporal regimes through clustering, we now examine the stationary distribution π\pi to characterize the long-term equilibrium behavior of limit order price change states. This distribution, representing the equilibrium state probabilities, reveals the predominant price change tendencies and is reported in Tables S3 and S4 of the Supplementary Material. Across all configurations, the distribution is heavily concentrated with over 97% probability in three states: mild negative change π4\pi\_{4}, zero change π5\pi\_{5}, and mild positive change π6\pi\_{6}. A consistent capitalization gradient emerges – moving from 𝙷𝙼𝙲\mathtt{HMC} to 𝙻𝙼𝙲\mathtt{LMC}, π5\pi\_{5} declines substantially while π4\pi\_{4} and π6\pi\_{6} increase. This confirms that lower-capitalization stocks exhibit less price inertia and require more frequent small revisions. Furthermore, the probabilities of mild upward and downward changes remain nearly symmetric, with π4≈π6\pi\_{4}\approx\pi\_{6} within each tier.

![Refer to caption](x16.png)

![Refer to caption](x17.png)

Figure 7: Jensen–Shannon Divergence between πs\pi\_{s} of different time intervals for 𝙷𝙼𝙲\mathtt{HMC} limit order price changes: Ask on left and Bid on right.

To quantify the dissimilarity between these stationary distributions across different time intervals, we compute the Jensen-Shannon Divergence (JSD), as visualized in the heatmaps in Figs. [7](https://arxiv.org/html/2601.04959v1#S4.F7 "Figure 7 ‣ 4.5 Stationary distribution of limit-order price changes ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis")–[9](https://arxiv.org/html/2601.04959v1#S4.F9 "Figure 9 ‣ 4.5 Stationary distribution of limit-order price changes ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"). The JSD analysis reveals a robust temporal structure common to both ask and bid sides. The closing hour 𝚃𝟼\mathtt{T\_{6}} consistently emerges as the most distinct, showing the largest divergences from the midday block 𝚃𝟸\mathtt{T\_{2}}–𝚃𝟻\mathtt{T\_{5}} across all tiers. This pronounced divergence signals a fundamental shift in market participants’ objectives: as the trading session concludes, the primary incentive transitions from value-seeking price discovery to deadline-driven inventory management. The urgency to square positions and mitigate overnight risk forces a structural reconfiguration of limit order submission probabilities, creating a unique equilibrium state that differs significantly from the steady liquidity provision characterizing the midday regime. A secondary distinct shift occurs immediately post-open, with 𝚃𝟸\mathtt{T\_{2}} diverging significantly from 𝚃𝟷\mathtt{T\_{1}}, likely driven by the resolution of initial information asymmetry. In contrast, the midday period spanning 𝚃𝟸\mathtt{T\_{2}} to 𝚃𝟻\mathtt{T\_{5}} remains relatively stable, characterized by low pairwise JSD values between adjacent midday intervals. Comparing sides, the bid generally exhibits larger JSD values, particularly at the close and post-open, confirming previous findings from clustering and metrics that bid-side behavior varies more and changes more significantly between periods, while the ask side is more consistently stable during midday.

![Refer to caption](x18.png)

![Refer to caption](x19.png)

Figure 8: Jensen–Shannon Divergence between πs\pi\_{s} of different time intervals for 𝙼𝙼𝙲\mathtt{MMC} limit order price changes: Ask on left and Bid on right.

Market capitalization further modulates the temporal divergences. 𝙷𝙼𝙲\mathtt{HMC} stocks exhibit the smallest overall JSD differences with 𝚃𝟼\mathtt{T\_{6}} departures in the range of 0.040–0.049 on ask and 0.042–0.056 on bid. 𝚃𝟸\mathtt{T\_{2}}–𝚃𝟷\mathtt{T\_{1}} breaks measure approximately 0.02–0.03, reflecting greater stability across trading phases. Whereas, 𝙼𝙼𝙲\mathtt{MMC} stocks demonstrate the most pronounced closing differentiation. This pattern is particularly strong on the ask side where 𝚃𝟼\mathtt{T\_{6}} versus 𝚃𝟸\mathtt{T\_{2}} reaches 0.085. Bid-side 𝚃𝟼\mathtt{T\_{6}} gaps also remain elevated. Finally, 𝙻𝙼𝙲\mathtt{LMC} stocks feature sharp post-open adjustments. The bid-side 𝚃𝟸\mathtt{T\_{2}} versus 𝚃𝟷\mathtt{T\_{1}} divergence equals 0.0437. Closing-hour divergences are substantial though remain below 𝙼𝙼𝙲\mathtt{MMC} peaks. These systematic variations confirm that intraday phase remains the primary organizing force, while capitalization modulates both the intensity of temporal contrasts and the degree of ask–bid asymmetry. These findings necessitate capitalization-aware parameterization: tighter monitoring thresholds for 𝙻𝙼𝙲\mathtt{LMC} stocks during the post-open period i.e. between 𝚃𝟷\mathtt{T\_{1}} & 𝚃𝟸\mathtt{T\_{2}}, and the lead-up to the close i.e. between 𝚃𝟻\mathtt{T\_{5}} & 𝚃𝟼\mathtt{T\_{6}}, and more conservative bid-side risk management during phase shifts across all tiers.

![Refer to caption](x20.png)

![Refer to caption](x21.png)

Figure 9: Jensen–Shannon Divergence between πs\pi\_{s} of different time intervals for 𝙻𝙼𝙲\mathtt{LMC} limit order price changes: Ask on left and Bid on right.

In summary, the stationary distribution analysis confirms that limit order dynamics are predominantly characterized by neutral and mild price changes, with the lower probability of neutral states in 𝙻𝙼𝙲\mathtt{LMC} stocks underscoring their need for more frequent revisions. The JSD analysis provides strong quantitative evidence for the three distinct intraday phases—Open, Midday, and Close—previously identified via clustering. Crucially, it demonstrates that market capitalization systematically modulates the intensity of divergences between these phases, with 𝙷𝙼𝙲\mathtt{HMC} stocks showing the greatest stability and 𝙻𝙼𝙲\mathtt{LMC} exhibiting amplified shifts, especially post-open. These findings collectively reinforce the necessity of phase-aware and capitalization-aware trading strategies. Furthermore, the consistently higher JSD values on the bid side confirm its greater heterogeneity, warranting tighter risk controls for buy-side liquidity provision during these critical phase transitions.

To provide a holistic overview before concluding in Section [6](https://arxiv.org/html/2601.04959v1#S6 "6 Conclusion ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"), we present the overall study workflow in Fig. [10](https://arxiv.org/html/2601.04959v1#S4.F10 "Figure 10 ‣ 4.5 Stationary distribution of limit-order price changes ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") alongside a structured summary of the key empirical findings from Section [4](https://arxiv.org/html/2601.04959v1#S4 "4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").

Data Preparation


Modeling


Analysis


High-Frequency Data
(NASDAQ 100 Tick-by-tick order submissions)

Data Pre-processing

•

Extract limit orders: ADD-ASK & ADD-BID.
•

Select 5 stocks per capitalization tier c∈{𝙷𝙼𝙲,𝙼𝙼𝙲,𝙻𝙼𝙲}c\in\{\mathtt{HMC,MMC,LMC}\}.
•

Segment trading time τ\tau into 𝚃𝟷,…,𝚃𝟼\mathtt{T\_{1},\dots,T\_{6}}.

State Discretization
  
Discretize consecutive limit order price changes – 9 states.

G-Test of Independence
Assess memory for Markov validity to limit order price changes.

Discrete-Time Markov Chain

•

1st1^{\text{st}} Order time-homogeneous DTMC.
•

Estimate TPMs 𝐏(τ,c)\mathbf{P}^{(\tau,c)} via MLE.
•

Compare pi​jp\_{ij} across τ\tau and cc.

Markov Chain Metrics

•

Spectral gap.
•

Entropy rate.
•

Mean recurrence time.

Dimensionality Reduction

•

Flatten TPMs: (10×1010\times 10) →\to (1×1001\times 100).
•

PCA (Noise reduction) →\to t-SNE (2D Embedding).

Clustering Analysis
Hierarchical & DBSCAN

Equilibrium Analysis

•

Compute stationary distribution π(τ,c)\pi^{(\tau,c)}.
•

Compare πs\pi\_{s} across τ\tau via JS divergence.

Figure 10: Integrated framework flowchart illustrating: (1) Data preparation and Markov validation, (2) Transition probability estimation, and (3) Comparative analysis via Markov chain metrics, clustering and equilibrium (stationary) states.

* •

  [4.2](https://arxiv.org/html/2601.04959v1#S4.SS2 "4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"): Transition Probability Matrix Analysis

  + –

    [4.2.1](https://arxiv.org/html/2601.04959v1#S4.SS2.SSS1 "4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") Inertia of Limit Order Prices: Price inertia follows a U-shaped intraday pattern; Capitalization gradient exists where 𝙷𝙼𝙲\mathtt{HMC} stocks exhibit the strongest inertia, indicating higher price stability, while 𝙻𝙼𝙲\mathtt{LMC} stocks display lower stability.
  + –

    [4.2.2](https://arxiv.org/html/2601.04959v1#S4.SS2.SSS2 "4.2.2 Directional Momentum of Limit Order Price Revisions ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis") Directional Momentum: 𝙻𝙼𝙲\mathtt{LMC} stocks show the highest price revision frequency. Directional asymmetry is evident at the open, where 𝙷𝙼𝙲\mathtt{HMC} stocks increase revision activity for positioning, while 𝙻𝙼𝙲\mathtt{LMC} traders adopt more conservative strategies.
* •

  [4.3](https://arxiv.org/html/2601.04959v1#S4.SS3 "4.3 Markov Chain Metrics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"): Markov Chain Metrics

  + –

    Convergence & Predictability: Spectral gap is lowest at the market open and peaks during midday; 𝙷𝙼𝙲\mathtt{HMC} stocks show lower entropy rates, indicating higher predictability and faster convergence to equilibrium compared to the more stochastic 𝙻𝙼𝙲\mathtt{LMC} stocks.
  + –

    Recurrence Times: Neutral price changes recur most frequently in 𝙷𝙼𝙲\mathtt{HMC} stocks, whereas mild price adjustments recur most frequently in 𝙻𝙼𝙲\mathtt{LMC} stocks, indicating continuous fine-tuning.
* •

  [4.4](https://arxiv.org/html/2601.04959v1#S4.SS4 "4.4 Clustering Analysis of Transition Dynamics ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"): Clustering Analysis of Transition Dynamics

  + –

    Temporal Regimes: Data-driven clustering reveals that the trading time intervals organize into naturally occurring behavioral phases.
  + –

    Bid-Ask Asymmetry: Bid side follows a three-regime structure – Opening, Midday, Closing, while the ask side exhibits four regimes – Opening, Midday, Pre-Close, Closing, providing evidence that sellers initiate end-of-day positioning strategies earlier than buyers.
* •

  [4.5](https://arxiv.org/html/2601.04959v1#S4.SS5 "4.5 Stationary distribution of limit-order price changes ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"): Stationary Distribution Analysis

  + –

    Long-term Equilibrium: Equilibrium probabilities are heavily concentrated in neutral and mild price changes; the probability of neutral price change declines substantially from 𝙷𝙼𝙲\mathtt{HMC} to 𝙻𝙼𝙲\mathtt{LMC}, confirming the higher revision necessity in lower-capitalization tiers.
  + –

    Closing Dynamics: Closing hour 𝚃𝟼\mathtt{T\_{6}} forms the most distinct regime, driven by a structural shift to deadline-driven inventory management. This divergence from the stable midday phase is sharpest in 𝙻𝙼𝙲\mathtt{LMC} stocks.

## 5 Discussion

While this study provides evidence on intraday limit order price change transitions, we recognize that the empirical findings can be sensitive to modeling and sampling choices.
Our analysis focuses on NASDAQ100 stocks during a twelve-day period, employs first-order Markov chains for modeling state transitions, and divides the trading day into six unequal-duration intervals. Each of these choices, while empirically motivated, represents one among several plausible approaches. Accordingly, we explicitly assess whether the main conclusions are stable under alternative specifications, so that the documented patterns are not driven by arbitrary design decisions.

To ensure our findings reflect genuine market patterns rather than methodological artifacts, we conducted four comprehensive robustness analyses that assess the sensitivity of our conclusions. Detailed methodologies and complete results are provided in Supplementary Material Section S3.
For clarity, we summarize here the objective and outcome of each test, emphasizing the practical (rather than purely statistical) magnitude of deviations. First, we validated the time-homogeneity assumption by subdividing each interval into four sub-periods.
While formal likelihood ratio tests detected minor fluctuations (as expected under large sample sizes),
mean absolute differences remained well below the 10%10\% statistical threshold, confirming practical stability of transition probabilities within intervals.
This supports the interpretation of each intraday segment as approximately stationary in transition dynamics. Second, we evaluated our first-order Markov specification against a second-order alternative. Although the latter was statistically favored, conditional mutual information was negligible, out-of-sample predictive gains were minimal, and the second-order specification required nearly four times as many parameters, supporting our parsimonious first-order choice. In other words, higher-order dependence exists statistically but contributes little incremental explanatory or predictive content relative to the complexity it introduces in a regime-comparison setting. Third, we assessed sensitivity to interval duration by comparing pooled one-hour versus two-hour aggregations.
he resulting transition probability matrices were numerically indistinguishable at the level relevant for the metric, clustering, and divergence analyses. Fourth, we examined our unequal-duration interval specification against uniform 65-minute segmentation. The transition probabilities showed low mean absolute differences, with no statistically significant differences after multiple testing correction. Taken together, these exercises indicate that the main intraday patterns—including the capitalization gradient, the temporal clustering structure, and the bid–ask asymmetries—are not artifacts of interval design. Overall, the robustness checks support the conclusion that the documented transition dynamics reflect stable features of the underlying order submission and revision process within the scope of our dataset.

Beyond statistical validity, the results also carry direct practical implications for market participants. For execution algorithms, the distinct capitalization gradient we document suggests that static, patient execution logic is well suited for 𝙷𝙼𝙲\mathtt{HMC} stocks, where price adjustments are infrequent and stable, whereas 𝙻𝙼𝙲\mathtt{LMC} stocks require more dynamic, price-adaptive strategies to accommodate higher revision intensities. With respect to intraday regime detection, our clustering results show that market phases are better characterized by behavioral shifts such as the early onset of ask-side closing dynamics, rather than by fixed clock-based partitions, offering a data-driven approach to regime switching. Finally, liquidity provision strategies can be improved by incorporating the documented bid–ask asymmetries – in particular, market makers may tighten risk controls on the bid side for 𝙻𝙼𝙲\mathtt{LMC} stocks, where extreme negative revisions are structurally less frequent, thereby enabling more efficient inventory and spread management. The stability of the transition dynamics across alternative temporal aggregations, interval specifications, and Markov orders suggests that the behaviors documented in this study are robust within modern electronic limit order book trading.

While our methodological choices are validated within the current scope, several extensions remain valuable. Applying the framework to other markets, asset classes, and longer time horizons would enable assessment of generalizability and detection of structural changes. In particular, extending the sample beyond a short window would clarify the extent to which the identified regimes persist across volatility states, macro announcements, and market-wide liquidity conditions.
Exploring non-Markovian specifications may capture additional dependence in sequential price adjustments. For example, semi-Markov or variable-length specifications could directly account for state-dependent sojourn times and heterogeneous memory, potentially refining the characterization of intraday persistence. Finally, although our nine-state discretization captures key dynamics, alternative state definitions or continuous-state approaches may reveal further nuances in limit order price revisions. These may include state definitions anchored to tick-size constraints, queue-position proxies, or spread-conditioned revisions, which could improve interpretability in specific microstructure settings.
These extensions would help generalize and deepen the insights developed in this study.

## 6 Conclusion

This study provides the first systematic examination of intraday limit order price change transition dynamics, addressing a critical gap in market microstructure research by analyzing ask and bid orders separately across High (𝙷𝙼𝙲\mathtt{HMC}), Medium (𝙼𝙼𝙲\mathtt{MMC}), and Low (𝙻𝙼𝙲\mathtt{LMC}) market capitalization stocks. By employing a discrete-time Markov chain (DTMC) framework on high-frequency tick-by-tick NASDAQ-100 data, we have uncovered fundamental patterns that govern how traders adjust limit order prices throughout the trading day, revealing complex interactions between temporal dynamics, market capitalization, and order side.

Time-interval wise comparison of transition probability matrices reveals systematic intraday patterns in price change inertia. The probability of consecutive zero price changes exhibits a distinct temporal structure: peaking at market opening due to defensive positioning, declining and stabilizing during midday as price discovery progresses, and surging again at the close—often exceeding the opening peak—driven by execution urgency. A pronounced capitalization gradient emerges in these dynamics. 𝙷𝙼𝙲\mathtt{HMC} stocks exhibit the strongest price inertia reflecting deep liquidity, while 𝙻𝙼𝙲\mathtt{LMC} stocks demonstrate lower stability and pronounced bid-ask asymmetries. In extreme price change states, ask-side transition probabilities consistently exceed bid-side probabilities in 𝙻𝙼𝙲\mathtt{LMC} stocks, with extreme negative bid-side revisions recurring less frequently. Markov chain metrics quantify the global dynamic properties of these processes. The spectral gap, smallest at market open and peaking midday, indicates that 𝙷𝙼𝙲\mathtt{HMC} and 𝙼𝙼𝙲\mathtt{MMC} stocks converge faster to equilibrium than 𝙻𝙼𝙲\mathtt{LMC} stocks. The entropy rate reveals a clear capitalization hierarchy, with 𝙻𝙼𝙲\mathtt{LMC} stocks exhibiting the highest unpredictability. Mean recurrence times show that neutral changes recur most frequently in 𝙷𝙼𝙲\mathtt{HMC} stocks, while mild adjustments occur most often in 𝙻𝙼𝙲\mathtt{LMC} stocks. Extreme states are rare across all configurations, with pronounced bid-ask asymmetry in 𝙻𝙼𝙲\mathtt{LMC} stocks. These findings enable execution strategy optimization: patient approaches in high-capitalization stocks during midday versus dynamic strategies in low-capitalization stocks during phase shifts.

Clustering analysis reveals distinct temporal regimes differing fundamentally between order sides. The bid side organizes into three regimes—Opening, Midday, and Closing—while the ask side exhibits four—Opening, Midday, Pre-Close, and Close—providing data-driven evidence that sellers begin strategic positioning earlier than buyers. Stationary distributions show heavy concentration with over 97% probability in mild negative, zero, and mild positive change states. Zero-change probability declines substantially from 𝙷𝙼𝙲\mathtt{HMC} to 𝙻𝙼𝙲\mathtt{LMC} stocks, confirming more frequent small revisions in lower-capitalization stocks. Jensen-Shannon divergence computed between stationary distributions across time intervals reveals robust temporal structure. The closing hour emerges as the most distinct phase with largest divergences from midday, while a secondary shift occurs post-open. The bid side exhibits larger divergence values, confirming greater variability. Market capitalization modulates these contrasts: 𝙷𝙼𝙲\mathtt{HMC} stocks show smallest differences reflecting stability, MMC stocks demonstrate pronounced closing differentiation, and 𝙻𝙼𝙲\mathtt{LMC} stocks feature sharp post-open adjustments. These variations confirm intraday phase as the primary organizing force, with capitalization modulating the intensity of temporal contrasts and the degree of bid-ask asymmetry. The early emergence of ask-side closing dynamics necessitates asymmetric timing in algorithmic strategies.

This paper demonstrates that limit order price change dynamics are neither random nor homogeneous but follow systematic patterns shaped by the interplay of intraday timing, market capitalization, and order side. The DTMC framework proves effective in capturing both short-term sequential dependencies through transition probabilities and long-term equilibrium behaviors through stationary distributions. By revealing the fundamental asymmetries between ask and bid orders and quantifying how these dynamics vary across liquidity regimes, this research advances understanding of modern equity markets and provides a foundation for developing context-aware trading strategies. Future research could extend this framework by incorporating order book depth and liquidity measures to analyze how price changes interact with available liquidity at different price levels, and by examining the impact of specific news events or macroeconomic releases on transition dynamics to illuminate how information shocks propagate through limit order pricing behavior. As electronic trading continues to dominate financial markets, the insights from this study become increasingly relevant for all market participants seeking to navigate the complex, high-frequency environment of contemporary limit order books.

## Acknowledgements

We extend our gratitude to Chris Bartlett, Jodhie Cabarles, and the technical support staff of [Algoseek](https://www.algoseek.com) for generously providing the data and offering assistance with data preprocessing necessary for our analysis. The authors, SR Luwang, K Mukhia, and BN Sharma, would also like to thank the Director of our institute for allocating doctoral research fellowship.

## Declarations

Competing interests
  
The authors declare no competing interests.

Data Availability Statement
  
The full dataset that support the findings of this study are available from [Algoseek](https://www.algoseek.com). Due to licensing restrictions, the underlying tick-level data of these TPMs cannot be redistributed by the authors and requests for access should be directed to [Algoseek](https://www.algoseek.com).

Author contribution
  
SR Luwang: Conceptualization, Methodology, Data curation, Formal analysis, Visualization, Writing - original draft. K Mukhia: Data curation, Writing - review & editing. BN Sharma: Formal analysis, Writing - review & editing. Md. Nurujjaman: Supervision, Writing - review & editing. Anish Rai: Software, Writing - review & editing. Filippo Petroni: Writing - review & editing, Validation. All the authors discussed the results and approved the final manuscript.

## References

* [1]
  A. R. Admati and P. Pfleiderer (1988)
  A theory of intraday patterns: volume and price variability.
  The review of financial studies 1 (1),  pp. 3–40.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [2]
  N. A. Ahad, F. M. Alipiah, and F. Azhari (2019)
  Applicability of g-test in analyzing categorical variables.
  In AIP Conference Proceedings,
  Vol. 2138.
  Cited by: [§3.1](https://arxiv.org/html/2601.04959v1#S3.SS1.p1.1 "3.1 G-test of Independence ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [3]
  Y. Amihud (2002)
  Illiquidity and stock returns: cross-section and time-series effects.
  Journal of financial markets 5 (1),  pp. 31–56.
  Cited by: [item 1b](https://arxiv.org/html/2601.04959v1#S4.I2.i1.I1.i2.p1.3 "In item 1 ‣ 4.2.2 Directional Momentum of Limit Order Price Revisions ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [4]
  T. G. Andersen and T. Bollerslev (1997)
  Intraday periodicity and volatility persistence in financial markets.
  Journal of empirical finance 4 (2-3),  pp. 115–158.
  Cited by: [item 1b](https://arxiv.org/html/2601.04959v1#S4.I1.i1.I1.i2.p1.2 "In item 1 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [item 1a](https://arxiv.org/html/2601.04959v1#S4.I2.i1.I1.i1.p1.4 "In item 1 ‣ 4.2.2 Directional Momentum of Limit Order Price Revisions ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [5]
  T. Belluzzo (2024)
  PyDTMC.
  External Links: [Link](https://github.com/TommasoBelluzzo/PyDTMC)
  Cited by: [§3.6](https://arxiv.org/html/2601.04959v1#S3.SS6.p3.3 "3.6 Stationary Distribution Analysis ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [6]
  J. Beran (1992)
  Statistical methods for data with long-range dependence.
  Statistical science,  pp. 404–416.
  Cited by: [§4.1](https://arxiv.org/html/2601.04959v1#S4.SS1.p1.3 "4.1 G-test of independence ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [7]
  T. B. Berrett and R. J. Samworth (2021)
  USP: an independence test that improves on pearson’s chi-squared and the g-test.
  Proceedings of the Royal Society A 477 (2256),  pp. 20210549.
  Cited by: [§3.1](https://arxiv.org/html/2601.04959v1#S3.SS1.p1.1 "3.1 G-test of Independence ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [8]
  B. Biais, L. Glosten, and C. Spatt (2005)
  Market microstructure: a survey of microfoundations, empirical results, and policy implications.
  Journal of Financial Markets 8 (2),  pp. 217–264.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p1.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p3.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [9]
  B. Biais, P. Hillion, and C. Spatt (1995)
  An empirical analysis of the limit order book and the order flow in the paris bourse.
  the Journal of Finance 50 (5),  pp. 1655–1689.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [10]
  E. Boehmer, C. M. Jones, and X. Zhang (2008)
  Which shorts are informed?.
  The Journal of Finance 63 (2),  pp. 491–527.
  Cited by: [item 2b](https://arxiv.org/html/2601.04959v1#S4.I1.i2.I1.i2.p1.3 "In item 2 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [11]
  J. Bouchaud, M. Mézard, and M. Potters (2002)
  Statistical properties of stock order books: empirical results and models.
  Quantitative finance 2 (4),  pp. 251.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p1.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p3.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [12]
  P. Brockman and D. Y. Chung (1999)
  An analysis of depth behavior in an electronic, order-driven environment.
  Journal of Banking & Finance 23 (12),  pp. 1861–1886.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [13]
  Á. Cartea, S. Jaimungal, and J. Penalva (2015)
  Algorithmic and high-frequency trading.
   Cambridge University Press.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [14]
  C. Chatfield (1978)
  The holt-winters forecasting procedure.
  Journal of the Royal Statistical Society: Series C (Applied Statistics) 27 (3),  pp. 264–279.
  Cited by: [§4.1](https://arxiv.org/html/2601.04959v1#S4.SS1.p1.3 "4.1 G-test of independence ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [15]
  T. Chordia, R. Roll, and A. Subrahmanyam (2005)
  Evidence on the speed of convergence to market efficiency.
  Journal of financial economics 76 (2),  pp. 271–292.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p1.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p3.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [16]
  R. Cont and A. De Larrard (2012)
  Order book dynamics in liquid markets: limit theorems and diffusion approximations.
  arXiv preprint arXiv:1202.6412.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p5.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [17]
  R. Cont, A. Kukanov, and S. Stoikov (2014)
  The price impact of order book events.
  Journal of financial econometrics 12 (1),  pp. 47–88.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [18]
  R. Cont, S. Stoikov, and R. Talreja (2010)
  A stochastic model for order book dynamics.
  Operations research 58 (3),  pp. 549–563.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p1.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p3.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [19]
  R. Cont (2011)
  Statistical modeling of high-frequency financial data.
  IEEE Signal Processing Magazine 28 (5),  pp. 16–25.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p1.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p3.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [20]
  T. M. Cover (1999)
  Elements of information theory.
   John Wiley & Sons.
  Cited by: [§3.3.2](https://arxiv.org/html/2601.04959v1#S3.SS3.SSS2.p1.1 "3.3.2 Entropy Rate ‣ 3.3 Markov Chain Dynamics Metrics ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [21]
  G. D’Amico, F. Petroni, and F. Prattico (2013)
  Semi-markov models in high frequency finance: a review.
  arXiv e-prints.
  External Links: [Link](https://doi.org/10.48550/arXiv.1312.3894)
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p2.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p5.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [22]
  G. D’Amico and F. Petroni (2011)
  A semi-markov model with memory for price changes.
  Journal of statistical mechanics: Theory and experiment 2011 (12),  pp. P12009.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p5.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [23]
  R. De Blasis (2019)
  Markov chain modelling in finance: stock valuation and price discovery.
  Cited by: [§3.2](https://arxiv.org/html/2601.04959v1#S3.SS2.p1.5 "3.2 Discrete-Time Markov Chain for Limit Order Price Changes ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [24]
  H. Dewachter (2001)
  Can markov switching models replicate chartist profits in the foreign exchange market?.
  Journal of International Money and finance 20 (1),  pp. 25–41.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p5.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [25]
  P. Diaconis and D. Stroock (1991)
  Geometric bounds for eigenvalues of markov chains.
  The annals of applied probability,  pp. 36–61.
  Cited by: [§3.3.1](https://arxiv.org/html/2601.04959v1#S3.SS3.SSS1.p1.3 "3.3.1 Spectral Gap and Relaxation Time ‣ 3.3 Markov Chain Dynamics Metrics ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [26]
  J. Dorrestijn (2024)
  Data-driven stochastic modeling markov chain matlab codes.
  External Links: [Link](https://www.jessedorrestijn.nl/matlab/)
  Cited by: [§3.2](https://arxiv.org/html/2601.04959v1#S3.SS2.p7.2 "3.2 Discrete-Time Markov Chain for Limit Order Price Changes ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [27]
  D. Easley, N. M. Kiefer, M. O’hara, and J. B. Paperman (1996)
  Liquidity, information, and infrequently traded stocks.
  The Journal of Finance 51 (4),  pp. 1405–1436.
  Cited by: [item 2b](https://arxiv.org/html/2601.04959v1#S4.I1.i2.I1.i2.p1.3 "In item 2 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [28]
  A. Ellul, C. W. Holden, P. Jain, and R. Jennings (2007)
  Order dynamics: recent evidence from the nyse.
  Journal of Empirical Finance 14 (5),  pp. 636–661.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [29]
  R. Fitzpatrick (2020)
  Thermodynamics and statistical mechanics.
   World Scientific.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p5.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [30]
  R. Garvey and F. Wu (2007)
  Intraday liquidity costs and order execution quality in nasdaq stocks.
  Available at SSRN 969051.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [31]
  L. R. Glosten and P. R. Milgrom (1985)
  Bid, ask and transaction prices in a specialist market with heterogeneously informed traders.
  Journal of financial economics 14 (1),  pp. 71–100.
  Cited by: [item 1a](https://arxiv.org/html/2601.04959v1#S4.I1.i1.I1.i1.p1.1 "In item 1 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [32]
  M. D. Gould, M. A. Porter, S. Williams, M. McDonald, D. J. Fenn, and S. D. Howison (2013)
  Limit order books.
  Quantitative Finance 13 (11),  pp. 1709–1742.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p1.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p3.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [33]
  R. Y. Goyenko, C. W. Holden, and C. A. Trzcinka (2009)
  Do liquidity measures measure liquidity?.
  Journal of financial Economics 92 (2),  pp. 153–181.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p1.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p3.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [34]
  J. Hasbrouck (2007)
  Empirical market microstructure: the institutions, economics, and econometrics of securities trading.
   Oxford University Press.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p2.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [35]
  N. Hautsch and R. Huang (2012)
  The market impact of a limit order.
  Journal of Economic Dynamics and Control 36 (4),  pp. 501–522.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p1.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p3.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [36]
  T. Ho and H. R. Stoll (1981)
  Optimal dealer pricing under transactions and return uncertainty.
  Journal of Financial economics 9 (1),  pp. 47–73.
  Cited by: [item 2b](https://arxiv.org/html/2601.04959v1#S4.I1.i2.I1.i2.p1.3 "In item 2 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [37]
  Y. Ho and Y. Cheung (1991)
  Behaviour of intra-daily stock return on an asian emerging market-hong kong.
  Applied Economics 23 (5),  pp. 957–966.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [38]
  J. Holmes and S. Hassini (2021)
  Discrete-time markov chain modelling of the ontario air quality health index.
  Water, Air, & Soil Pollution 232,  pp. 1–13.
  Cited by: [§3.6](https://arxiv.org/html/2601.04959v1#S3.SS6.p1.2 "3.6 Stationary Distribution Analysis ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [39]
  N. Jaroonchokanan, T. Termsaithong, and S. Suwanna (2022)
  Dynamics of hierarchical clustering in stocks market during financial crises.
  Physica A: Statistical Mechanics and its Applications 607,  pp. 128183.
  Cited by: [§3.5](https://arxiv.org/html/2601.04959v1#S3.SS5.p1.1 "3.5 Clustering Techniques for Dimension-Reduced TPMs ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [40]
  N. Jegadeesh and Y. Wu (2022)
  Closing auctions: nasdaq versus nyse.
  Journal of Financial Economics 143 (3),  pp. 1120–1139.
  Cited by: [item 1c](https://arxiv.org/html/2601.04959v1#S4.I1.i1.I1.i3.p1.1 "In item 1 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [41]
  I. T. Jolliffe and J. Cadima (2016)
  Principal component analysis: a review and recent developments.
  Philosophical transactions of the royal society A: Mathematical, Physical and Engineering Sciences 374 (2065),  pp. 20150202.
  Cited by: [§3.4](https://arxiv.org/html/2601.04959v1#S3.SS4.p1.3 "3.4 Dimensionality Reduction of the TPMs ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [42]
  M. Kazemi-Beydokhti, R. Ali Abbaspour, and M. Mojarab (2017)
  Spatio-temporal modeling of seismic provinces of iran using dbscan algorithm.
  Pure and Applied Geophysics 174,  pp. 1937–1952.
  Cited by: [§3.5](https://arxiv.org/html/2601.04959v1#S3.SS5.p1.1 "3.5 Clustering Techniques for Dimension-Reduced TPMs ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [43]
  B. D. Kluger and M. E. McBride (2011)
  Intraday trading patterns in an intelligent autonomous agent-based stock market.
  Journal of Economic Behavior & Organization 79 (3),  pp. 226–245.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [44]
  C. M. Lee, B. Mucklow, and M. J. Ready (1993)
  Spreads, depths, and the impact of earnings information: an intraday analysis.
  The Review of Financial Studies 6 (2),  pp. 345–374.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [45]
  D. A. Levin and Y. Peres (2017)
  Markov chains and mixing times.
  Vol. 107, American Mathematical Soc..
  Cited by: [§3.3.1](https://arxiv.org/html/2601.04959v1#S3.SS3.SSS1.p1.3 "3.3.1 Spectral Gap and Relaxation Time ‣ 3.3 Markov Chain Dynamics Metrics ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§3.3.3](https://arxiv.org/html/2601.04959v1#S3.SS3.SSS3.p1.1 "3.3.3 Mixing Rate ‣ 3.3 Markov Chain Dynamics Metrics ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [46]
  S. R. Luwang, A. Rai, M. Nurujjaman, and F. Petroni (2025)
  Intraday order transitions across market capitalizations through markov analysis.
  The European Physical Journal Special Topics,  pp. 1–21.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p5.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p6.5 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§3.4](https://arxiv.org/html/2601.04959v1#S3.SS4.p1.3 "3.4 Dimensionality Reduction of the TPMs ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§3.5](https://arxiv.org/html/2601.04959v1#S3.SS5.p1.1 "3.5 Clustering Techniques for Dimension-Reduced TPMs ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [47]
  A. Madhavan (2000)
  Market microstructure: a survey.
  Journal of financial markets 3 (3),  pp. 205–258.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p1.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p3.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [48]
  N. Masseran (2015)
  Markov chain model for the stochastic behaviors of wind-direction data.
  Energy conversion and management 92,  pp. 266–274.
  Cited by: [§3.2](https://arxiv.org/html/2601.04959v1#S3.SS2.p7.2 "3.2 Discrete-Time Markov Chain for Limit Order Price Changes ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [49]
  D. M. Mateos, L. E. Riveaud, and P. W. Lamberti (2017)
  Detecting dynamical changes in time series by using the jensen shannon divergence.
  Chaos: An Interdisciplinary Journal of Nonlinear Science 27 (8).
  Cited by: [§3.6](https://arxiv.org/html/2601.04959v1#S3.SS6.p7.5 "3.6 Stationary Distribution Analysis ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [50]
  T. H. McInish and R. A. Wood (1992)
  An analysis of intraday patterns in bid/ask spreads for nyse stocks.
  the Journal of Finance 47 (2),  pp. 753–764.
  Cited by: [item 1a](https://arxiv.org/html/2601.04959v1#S4.I1.i1.I1.i1.p1.1 "In item 1 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [item 1b](https://arxiv.org/html/2601.04959v1#S4.I1.i1.I1.i2.p1.2 "In item 1 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [item 1a](https://arxiv.org/html/2601.04959v1#S4.I2.i1.I1.i1.p1.4 "In item 1 ‣ 4.2.2 Directional Momentum of Limit Order Price Revisions ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [51]
  A. J. Menkveld (2013)
  High frequency trading and the new market makers.
  Journal of financial Markets 16 (4),  pp. 712–740.
  Cited by: [item 1b](https://arxiv.org/html/2601.04959v1#S4.I2.i1.I1.i2.p1.3 "In item 1 ‣ 4.2.2 Directional Momentum of Limit Order Price Revisions ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [52]
  F. Nielsen (2019)
  On the jensen–shannon symmetrization of distances relying on abstract means.
  Entropy 21 (5),  pp. 485.
  Cited by: [§3.6](https://arxiv.org/html/2601.04959v1#S3.SS6.p3.3 "3.6 Stationary Distribution Analysis ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [53]
  J. R. Norris (1998)
  Markov chains.
   Cambridge university press.
  Cited by: [§3.3.4](https://arxiv.org/html/2601.04959v1#S3.SS3.SSS4.p1.1 "3.3.4 Mean Recurrence Time ‣ 3.3 Markov Chain Dynamics Metrics ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [54]
  M. S. Pagano and R. A. Schwartz (2003)
  A closing call’s impact on market quality at euronext paris.
  Journal of Financial Economics 68 (3),  pp. 439–484.
  Cited by: [item 1c](https://arxiv.org/html/2601.04959v1#S4.I1.i1.I1.i3.p1.1 "In item 1 ‣ 4.2.1 Inertia of Limit Order Prices ‣ 4.2 Transition Probability Matrix Analysis ‣ 4 Results ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [55]
  F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, et al. (2011)
  Scikit-learn: machine learning in python.
  the Journal of machine Learning research 12,  pp. 2825–2830.
  Cited by: [§3.5](https://arxiv.org/html/2601.04959v1#S3.SS5.p1.1 "3.5 Clustering Techniques for Dimension-Reduced TPMs ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [56]
  S. Rabindrajit Luwang, A. Rai, M. Nurujjaman, O. Prakash, and C. Hens (2024)
  High-frequency stock market order transitions during the us–china trade war 2018: a discrete-time markov chain analysis.
  Chaos: An Interdisciplinary Journal of Nonlinear Science 34 (1).
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p5.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p6.5 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§3.2](https://arxiv.org/html/2601.04959v1#S3.SS2.p1.5 "3.2 Discrete-Time Markov Chain for Limit Order Price Changes ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§3.2](https://arxiv.org/html/2601.04959v1#S3.SS2.p3.3 "3.2 Discrete-Time Markov Chain for Limit Order Price Changes ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§3.6](https://arxiv.org/html/2601.04959v1#S3.SS6.p1.2 "3.6 Stationary Distribution Analysis ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [57]
  I. Roşu (2009)
  A dynamic model of the limit order book.
  The Review of Financial Studies 22 (11),  pp. 4601–4641.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p1.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p3.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§1](https://arxiv.org/html/2601.04959v1#S1.p4.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [58]
  T. H. Rydberg and N. Shephard (2003)
  Dynamics of trade-by-trade price movements: decomposition and models.
  Journal of Financial Econometrics 1 (1),  pp. 2–25.
  Cited by: [§1](https://arxiv.org/html/2601.04959v1#S1.p5.1 "1 Introduction ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [59]
  A. Shamshad, M. Bawadi, W. W. Hussin, T. A. Majid, and S. Sanusi (2005)
  First and second order markov chain models for synthetic generation of wind speed time series.
  Energy 30 (5),  pp. 693–708.
  Cited by: [§3.2](https://arxiv.org/html/2601.04959v1#S3.SS2.p1.5 "3.2 Discrete-Time Markov Chain for Limit Order Price Changes ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis"),
  [§3.2](https://arxiv.org/html/2601.04959v1#S3.SS2.p7.2 "3.2 Discrete-Time Markov Chain for Limit Order Price Changes ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [60]
  A. Sinclair (1992)
  Improved bounds for mixing rates of markov chains and multicommodity flow.
  Combinatorics, probability and Computing 1 (4),  pp. 351–370.
  Cited by: [§3.3.3](https://arxiv.org/html/2601.04959v1#S3.SS3.SSS3.p1.1 "3.3.3 Mixing Rate ‣ 3.3 Markov Chain Dynamics Metrics ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [61]
  G. A. Spedicato, T. S. Kang, S. B. Yalamanchi, D. Yadav, and I. Cordón (2016)
  The markovchain package: a package for easily handling discrete markov chains in r.
  Accessed Dec.
  Cited by: [§3.2](https://arxiv.org/html/2601.04959v1#S3.SS2.p1.5 "3.2 Discrete-Time Markov Chain for Limit Order Price Changes ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").
* [62]
  L. Van der Maaten and G. Hinton (2008)
  Visualizing data using t-sne..
  Journal of machine learning research 9 (11).
  Cited by: [§3.4](https://arxiv.org/html/2601.04959v1#S3.SS4.p1.3 "3.4 Dimensionality Reduction of the TPMs ‣ 3 Methodology ‣ Intraday Limit Order Price Change Transition Dynamics Across Market Capitalizations Through Markov Analysis").

See pages - of <Supplementary_Material.pdf>