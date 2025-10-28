---
authors:
- Avirup Chakraborty
doc_id: arxiv:2510.22341v1
family_id: arxiv:2510.22341
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Understanding Carbon Trade Dynamics: A European Union Emissions Trading System
  Perspective'
url_abs: http://arxiv.org/abs/2510.22341v1
url_html: https://arxiv.org/html/2510.22341v1
venue: arXiv q-fin
version: 1
year: 2025
---


Avirup Chakraborty
  
Indian Statistical Institute, Kolkata
  
[avirupchakraborty358@gmail.com](mailto:avirupchakraborty358@gmail.com)
I thank Prof. Diganta Mukherjee for his continuous guidance and advice.

###### Abstract

The European Union Emissions Trading System (EU ETS), the world’s first and largest cap-and-trade carbon market, is a cornerstone of EU climate policy. This study provides a comprehensive empirical analysis of the EU carbon market’s efficiency, price dynamics, and structural network from 2010 to 2020. First, we identify significant price clustering and short-term return predictability using an AR-GARCH model, achieving 60.05% directional accuracy and a 70.78% hit rate within forecasted confidence intervals. These observed patterns motivate a deeper exploration of market structure. Second, leveraging this insight, a weighted network analysis of inter-country transactions uncovers a concentrated market where a few registries dominate high-value flows and exert disproportionate influence. Finally, building upon the network findings, country-specific log-log regressions of price on traded quantity reveal heterogeneous and sometimes counter-intuitive elasticities; in several cases, positive elasticities exceed unity, indicating that trading volumes rise with prices, a deviation from conventional demand behavior that highlights potential inefficiencies driven by speculation, strategic behavior, or policy distortions. Collectively, these results point to persistent inefficiencies within the EU ETS, including partial predictability, asymmetric market power, and anomalous price-volume relationships, implying that while the system has driven decarbonization, its trading and pricing mechanisms remain imperfect.

Key Words: EU ETS, Carbon market, Volatility clustering, AR-GARCH, Network analysis, Price elasticity, Market inefficiency.

## 1  Introduction

The European Union Emissions Trading System (EU ETS) is a central component of the European Union’s climate policy framework, designed to reduce greenhouse gas (GHG) emissions in a cost-effective and market-oriented manner. Launched in 2005, the EU ETS was the first large-scale carbon market in the world and has since become the largest emissions trading system globally in terms of both value and volume. It currently applies to energy producers, energy-intensive manufacturing industries, and intra-European aviation, covering sectors that are collectively responsible for nearly 50% of the EU’s total CO2 emissions. In 2019, the total emission cap set approximately at 1.8 billion tons of CO2.

At the core of the EU ETS lies a cap-and-trade mechanism, which sets a maximum limit (cap) on the total amount of greenhouse gases that can be emitted by all participating entities. Within this cap, a finite number of EU Allowances (EUAs) are distributed,partly through free allocation based on historical benchmarks, and partly through auctioning. Each EUA grants the right to emit one ton of CO2 equivalent and is freely tradable on the carbon market, allowing firms to buy and sell allowances according to their emission levels and abatement costs.

Compliance under the EU ETS requires installations to monitor, report, and verify their annual emissions, and to surrender a corresponding number of allowances. Firms that emit more than their allocated allowances must purchase additional EUAs from the market, while those that emit less may sell their surplus. This market-based design promotes emission reductions where they are most economically efficient, thereby encouraging investment in low-carbon technologies while limiting the need for heavy-handed regulatory intervention. A central challenge for the European Union Emissions Trading System (EU ETS) is the persistence of inefficiencies in market functioning, despite its success as the flagship cap-and-trade mechanism for reducing greenhouse gas emissions. Market efficiency is critical for ensuring that allowance prices reflect underlying fundamentals rather than speculative or strategic behavior. Inefficiencies, however, may arise from volatility clustering, market concentration, or anomalous price-volume relationships, all of which can distort the intended cost-effective allocation of emissions reductions.

Previous literature has shown that carbon markets, particularly the EU ETS, often display persistent inefficiencies and price distortions, largely arising from liquidity constraints and market design flaws [[3](https://arxiv.org/html/2510.22341v1#bib.bib3), [4](https://arxiv.org/html/2510.22341v1#bib.bib4)]. Recent studies confirm that these distortions remain structural rather than temporary [[2](https://arxiv.org/html/2510.22341v1#bib.bib2)]. Parallel research highlights that liquidity continues to shape price formation and return behavior in both EU and Chinese carbon markets [[7](https://arxiv.org/html/2510.22341v1#bib.bib7), [8](https://arxiv.org/html/2510.22341v1#bib.bib8)]. Moreover, [[5](https://arxiv.org/html/2510.22341v1#bib.bib5)] and [[6](https://arxiv.org/html/2510.22341v1#bib.bib6)] provide evidence that carbon price movements exhibit return predictability, influenced by energy market spillovers and nonlinear dynamics. To facilitate such investigations, [[1](https://arxiv.org/html/2510.22341v1#bib.bib1)] offer a comprehensive international transaction database supporting cross-country analyses of trading patterns and market efficiency.

Building on this foundation, our analysis provides new empirical evidence on the nature and extent of these inefficiencies from 2010 to 2020. This study is structured as follows: First, we begin with a detailed data and market overview, examining transaction patterns and price dynamics to establish the fundamental characteristics of the market and to assess the scope for return predictability. The observed variations in trading activity across registries and over time suggest that market behavior may not be uniform, motivating a deeper exploration of its underlying structure. Second, to capture this heterogeneity and the potential interdependence among participants, we conduct a network analysis of transaction values across registries. This enables us to uncover patterns of trading concentration and identify dominant countries whose interactions shape overall market coordination. Finally, building on these network insights, we focus on the top three trading nations to estimate price elasticities, investigating how transaction volumes respond to price changes and whether such relationships reveal inefficiencies within the system.

## 2  Data and Market Overview

### 2.1  EUA Transaction Data

The data for this study are collected from the European Union Transaction Log (EUTL) [[1](https://arxiv.org/html/2510.22341v1#bib.bib1)], the official registry that tracks transactions and compliance under the EU ETS. The EUTL functions as the central reporting and monitoring framework, enabling the European Commission to make key information on regulated entities’ compliance status, market participation, and allowance transfers publicly available. This data spans February 2005 to April 2020, with transaction-level records accessed through the official portal [[9](https://arxiv.org/html/2510.22341v1#bib.bib9)], which provides granular emissions and compliance data at the installation level. The dataset covers three primary domains: installations, transactions, and accounts.

Installations correspond to regulated facilities, such as power plants, industrial plants, and aviation operators where verified emissions are reported and allowances must be surrendered to ensure compliance. Transactions record the transfer of allowances between participants and are tied to the account in which they occur. These transfers include internal reallocations between installations and administrative accounts, allocations through free distribution or auction mechanisms, and surrenders undertaken to meet compliance obligations. Accounts, in turn, are categorized into three types. Operator Holding Accounts (OHAs), linked to installations, are used by regulated entities to receive, hold, and surrender allowances. Administrative Accounts are managed by competent authorities to issue, allocate, or cancel allowances as part of system operations. Finally, Person Holding Accounts (PHAs), maintained by intermediaries, financial institutions, and non-governmental organizations, are employed primarily for trading purposes but are not directly used for compliance.

The dataset records transactions of European Union Allowances (EUAs), the primary compliance instrument under the EU ETS. Established in 2005, the system has progressed through four phases: Phase I (2005–2007) as a pilot defining trading rules; Phase II (2008–2012) expanding scope and allocation; Phase III (2013–2020) introducing harmonized regulations and stricter compliance; and the ongoing Phase IV (2021–2030). Our study examines EUA transfers from January 5, 2010, to April 30, 2020, covering the end of Phase II and the entire Phase III of the EU ETS.

Figure [1](https://arxiv.org/html/2510.22341v1#S2.F1 "Figure 1 ‣ 2.1 EUA Transaction Data ‣ 2 Data and Market Overview ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective") illustrates the functioning of the EU ETS, highlighting the three types of accounts and their respective holders. These accounts are connected to various entities such as installations (OHA), administrative authorities (regulatory bodies), and third-party companies (PHA) that participate in market transactions to achieve compliance. The figure also distinguishes between internal and external transactions, clarifying how they differ across registries (countries).

![Refer to caption](plots/Account_Holder.png)


Figure 1:

Figure [2](https://arxiv.org/html/2510.22341v1#S2.F2 "Figure 2 ‣ 2.1 EUA Transaction Data ‣ 2 Data and Market Overview ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective") illustrates the cyclical procedure for maintaining compliance within each financial year. The process begins with the initial allocation or auctioning of emission allowances to installations, with the quantities determined by regulatory authorities. This is followed by the transaction phase, during which installations engage in market trading to either generate profit or ensure compliance.

![Refer to caption](plots/Allocated_free.png)


Figure 2:

The final two phases occur at the end of each financial year, managed by the regulatory bodies,these involve verifying the actual emissions and requiring installations to surrender the corresponding number of allowances. In the transaction data, the compliance rate is observed to be nearly 100%, indicating effective enforcement of the system. Since administrative transactions do not effect price dynamics, our analysis focuses exclusively on transfers between OHAs and PHAs. Figure [3](https://arxiv.org/html/2510.22341v1#S2.F3 "Figure 3 ‣ 2.1 EUA Transaction Data ‣ 2 Data and Market Overview ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective") illustrates the proportions of transaction counts and values (in EUR) across these account types during the selected period.

![Refer to caption](plots/descriptive1.png)


Figure 3:

Although Operator Holding Accounts (OHAs) are more numerous in the market (Figure [4](https://arxiv.org/html/2510.22341v1#S2.F4 "Figure 4 ‣ 2.1 EUA Transaction Data ‣ 2 Data and Market Overview ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective"), left), Person Holding Accounts (PHAs) dominate trading activity in both volume and value (Figure [3](https://arxiv.org/html/2510.22341v1#S2.F3 "Figure 3 ‣ 2.1 EUA Transaction Data ‣ 2 Data and Market Overview ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective")). This prominence suggests that PHAs, despite being fewer in number, play a more influential role in price formation and market dynamics. The distribution of these numerous OHA accounts by country is further detailed in Figure [4](https://arxiv.org/html/2510.22341v1#S2.F4 "Figure 4 ‣ 2.1 EUA Transaction Data ‣ 2 Data and Market Overview ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective") (right).

![Refer to caption](plots/descriptive2.png)


Figure 4:

The above descriptive analysis provides a comprehensive overview of market participation and transaction dynamics. From this, we infer several key observations , notably, the limited participation of OHA accounts, which may be attributed to the pre-allocation of allowances. In Figure [4](https://arxiv.org/html/2510.22341v1#S2.F4 "Figure 4 ‣ 2.1 EUA Transaction Data ‣ 2 Data and Market Overview ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective") (left), the number of unique OHA and PHA accounts corresponds to the distinct accounts engaged in OHA–PHA transactions within the dataset. Approximately 80% of all OHA accounts participated in these transactions. Thus, although OHA accounts exhibit relatively steady participation, their transaction volumes and values remain low, indicating a degree of inefficiency in market engagement. In the following section, we will now explore the dynamics of price movements in greater depth.

### 2.2  EUA Price Data

The allowance price data were collected from the International Carbon Action Partnership (ICAP), available at [[10](https://arxiv.org/html/2510.22341v1#bib.bib10)]. The dataset distinguishes between two types of markets. The primary market represents the initial issuance of allowances, typically through government auctions. In this market, spot prices are recorded weekly, with observations available every Tuesday. The secondary market, by contrast, reflects trading activity among companies, intermediaries, and other entities after allowances have been distributed in the primary market. For this market, spot price data are reported for all weekdays, excluding weekends.

![Refer to caption](plots/price.png)


Figure 5:

The backbone of the EU Emissions Trading System (EU ETS) lies in its strategic use of market dynamics to create an arbitrage-free pricing mechanism, enabling participants to adjust and reduce carbon emissions efficiently. For the analysis, we construct a weekly-aggregated price series by taking the mean of the secondary market spot prices within each calendar week. This approach smooths out short-term fluctuations that daily data often exhibit and provides a more stable trend that classical econometric methods can effectively capture. Figure [5](https://arxiv.org/html/2510.22341v1#S2.F5 "Figure 5 ‣ 2.2 EUA Price Data ‣ 2 Data and Market Overview ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective") presents the resulting weekly series (in Euros), partitioned into three distinct segments with different mean levels. These segments will later aid in identifying price clusters and examining the evolution of the market across phases.

The observed price behavior can be largely attributed to changes in EU ETS policy mechanisms over time. According to the European Commission, the surplus of allowances in the EU ETS exceeded 2.1 billion in 2013 [[11](https://arxiv.org/html/2510.22341v1#bib.bib11)]. This substantial oversupply reduced scarcity in the market, weakened demand pressures, and consequently led to a prolonged period of low EUA prices. To address this structural imbalance, the Market Stability Reserve (MSR) was agreed upon in 2015 as a long-term mechanism to correct the surplus of allowances in the EU carbon market. Designed to automatically adjust the supply of allowances and enhance the market’s resilience to future shocks, the MSR was formally established in 2018 and became operational in 2019 [[12](https://arxiv.org/html/2510.22341v1#bib.bib12)]. The implementation of the MSR effectively tightened the available supply of allowances, restoring market confidence and resulting in a notable upward shift in EUA prices from 2018 onward.

Market efficiency is inherently related to the predictability of asset returns [[13](https://arxiv.org/html/2510.22341v1#bib.bib13)].
To examine short-term return predictability, we employ the Box-Jenkins framework to model and forecast returns.
Specifically, the weekly log return is defined as

|  |  |  |
| --- | --- | --- |
|  | rt=ln⁡(ptpt−1),r\_{t}=\ln\left(\frac{p\_{t}}{p\_{t-1}}\right), |  |

where ptp\_{t} and pt−1p\_{t-1} denote the prices at time tt and t−1t-1, respectively.

![Refer to caption](plots/returns.png)


Figure 6:

Figure [6](https://arxiv.org/html/2510.22341v1#S2.F6 "Figure 6 ‣ 2.2 EUA Price Data ‣ 2 Data and Market Overview ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective") shows the resulting return series. Since we will model the return now on, we must know about the stationarity of this series. Observing the time series it is clear that the returns are mean reversion but some heteroskedasticity is also visible. So to test the mean stationarity we will use the Augmented Dickey Fuller test and to check for time-varying variance Engle’s ARCH Test, shown in Table [1](https://arxiv.org/html/2510.22341v1#S2.T1 "Table 1 ‣ 2.2 EUA Price Data ‣ 2 Data and Market Overview ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective").

Table 1: Results of Stationarity and Heteroskedasticity Tests

| Test | Test Statistic | p-value | Conclusion |
| --- | --- | --- | --- |
| ADF | -10.0 | 1.84×10−171.84\times 10^{-17} | Stationary in mean (reject H0H\_{0}) |
| Engle’s test | 54.57 | 2.15×10−72.15\times 10^{-7} | ARCH effects present (reject H0H\_{0}) |

So, the returns is mean stationary but not variance stabilized. We have plotted the ACF and PACF plots for 52 week lags in Figure [13](https://arxiv.org/html/2510.22341v1#Sx1.F13 "Figure 13 ‣ Appendix ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective") in the Appendix. The ACF plot drops to zero very rapidly, indicating that the series is stationary. The PACF plot shows significant autocorrelations at the first three lags, suggesting that an AR(3) specification would be appropriate. In contrast, the squared returns display strong autocorrelation in both the ACF and PACF plots, confirming the presence of volatility clustering and providing evidence for ARCH effects.

We performed a rolling forecast of the return series using a two-stage time series model. The mean dynamics were modeled using a fixed AR(3) model, while the conditional variance of the residuals was captured using a GARCH(1,1) model. At each step of the rolling window, the AR(3) model was fitted to a window of past observations (104 week long), and one-step-ahead forecasts were generated. Residuals from the AR model were passed to the GARCH(1,1) model to estimate forecast variances. The forecast mean, actual returns, and variance forecasts were then evaluated and the evaluation results are shown in Table [2](https://arxiv.org/html/2510.22341v1#S2.T2 "Table 2 ‣ 2.2 EUA Price Data ‣ 2 Data and Market Overview ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective").

Table 2: Forecast Evaluation Metrics

| Metric | Symbol | Value |
| --- | --- | --- |
| Mean Squared Error | MSE | 0.003149 |
| Root Mean Squared Error | RMSE | 0.056120 |
| Mean Absolute Error | MAE | 0.040455 |
| Directional Accuracy | DA | 60.01% |
| Hit Rate (within ±1​σ\pm 1\sigma band) | HR | 70.97% |

Hit rate measures the proportion of times the actual return falls within the forecasted ±1\pm 1 standard deviation band generated by the GARCH(1,1) model. A hit rate of 70.78% suggests that the model captures the time-varying nature of return volatility reasonably well. Directional accuracy represents the proportion of forecasts in which the predicted and actual return signs coincide, i.e., sign​(y^t)=sign​(yt)\text{sign}(\hat{y}\_{t})=\text{sign}(y\_{t}). With a directional accuracy of 60.05%, the AR(3) model demonstrates a modest ability to anticipate the direction of returns. In Figure [14](https://arxiv.org/html/2510.22341v1#Sx1.F14 "Figure 14 ‣ Appendix ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective"), we observe that the forecast closely tracks the actual return series, with the one–standard deviation band capturing most of the variations. This indicates a certain degree of return predictability in the weekly returns.

So far, we have provided an overview of the market, encompassing both transaction activity and price dynamics, followed by an analysis of returns. However, a key characteristic of an international market is its inherent interconnectedness, where markets tend to operate in a coordinated manner. This motivates us to examine the joint behaviour of transactions and prices in an inter-country context, both in terms of transaction value and their underlying associations. The next two sections focus on these two aspects in detail.

## 3  Inter Country Trading Dynamics

This section examines the evolution of cross-country transaction patterns through the interaction of Operator and Person Holding Accounts (OHA–PHA), which characterize core market linkages and structural shifts. The annual average transaction value (EUR) is calculated for each participating registry.

Figures [7](https://arxiv.org/html/2510.22341v1#S3.F7 "Figure 7 ‣ 3 Inter Country Trading Dynamics ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective")-[9](https://arxiv.org/html/2510.22341v1#S3.F9 "Figure 9 ‣ 3 Inter Country Trading Dynamics ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective") present the resulting transaction networks for 2010, 2015, and 2019. These years were selected as representatives from the distinct periods previously identified in the price dynamics analysis.

In the network diagrams, nodes signify domestic transactions within a country, and directed edges represent cross-border transfers from a source registry to an acquiring one. A default size is used for all nodes; however, the diameter of a node increases proportionally with its internal transaction value once a specific threshold is exceeded. To maintain visual clarity, only external links surpassing a predefined value are illustrated. Both the edge threshold and the node scaling are applied uniformly across all years to ensure consistent comparability.

![Refer to caption](plots/trade_network_2010.png)


Figure 7:

![Refer to caption](plots/trade_network_2015.png)


Figure 8:

![Refer to caption](plots/trade_network_2019.png)


Figure 9:

The network visualization highlights several notable patterns in the evolution of market participation over time. Prominently, only a handful of countries, roughly four to six-are actively engaged in high-value internal transactions, underscoring a degree of inefficiency and concentration in participation within the system. This limited engagement suggests that the trading activity is driven primarily by a small core of influential countries, while many others remain relatively inactive or peripheral.

A particularly striking observation is the decline in the United Kingdom’s node size in 2019 compared to 2010 and 2015. This reduction likely reflects the uncertainty surrounding Brexit, which diminished the UK’s integration and centrality within the EU ETS network during the transition period. In contrast, the 2019 network exhibits higher overall density and volatility, a structural shift that can be plausibly associated with the introduction of the Market Stability Reserve [[12](https://arxiv.org/html/2510.22341v1#bib.bib12)]. The MSR’s mechanism to absorb surplus allowances appears to have tightened the market, leading to stronger interconnections and more dynamic trading behavior among participants. Moreover, Germany and the Netherlands emerge as increasingly prominent nodes in 2019. Together, these trends point to a more concentrated yet more active network, shaped by both regulatory reforms and evolving national roles within the carbon market.

Since some countries exhibit particularly large internal as well as external transaction values, it is essential to quantify the relative importance of each node in the directed trade networks over time. To this end, we employ Eigenvector Centrality [[15](https://arxiv.org/html/2510.22341v1#bib.bib15)], [[16](https://arxiv.org/html/2510.22341v1#bib.bib16)], [[17](https://arxiv.org/html/2510.22341v1#bib.bib17)] to capture not only the direct connectivity of a node but also the influence it derives from its neighbors.

For a directed, weighted network with adjacency matrix 𝐀\mathbf{A}, where both edges and nodes carry intrinsic weights, we define the Eigenvector Centrality xix\_{i} of node ii as the solution to the eigenvalue problem:

|  |  |  |
| --- | --- | --- |
|  | 𝐀𝐱=λ​𝐱,\mathbf{A}\mathbf{x}=\lambda\mathbf{x}, |  |

where 𝐱=(x1,x2,…,xn)⊤\mathbf{x}=(x\_{1},x\_{2},\dots,x\_{n})^{\top} is the principal eigenvector corresponding to the largest eigenvalue λ\lambda. In our formulation, the weighted adjacency matrix 𝐀\mathbf{A} incorporates both external trade connections and internal trade capacity:

|  |  |  |
| --- | --- | --- |
|  | Ai​j={wi​jmax⁡{wk​l},if ​i≠j​ (external trade),wi​imax⁡{wk​l},if ​i=j​ (self-trade as self-loop),A\_{ij}=\begin{cases}\dfrac{w\_{ij}}{\max\{w\_{kl}\}},&\text{if }i\neq j\text{ (external trade)},\\[10.0pt] \dfrac{w\_{i}i}{\max\{w\_{kl}\}},&\text{if }i=j\text{ (self-trade as self-loop)},\end{cases} |  |

where wi​jw\_{ij} represents the trade value from country ii to country jj, wi​iw\_{i}i denotes the self-trade value of country ii, and the normalization ensures all weights lie in [0,1][0,1]. The maximum is taken over all edge weights (including self-loops) to maintain consistent scaling.

The centrality of node ii can thus be expressed as:

|  |  |  |
| --- | --- | --- |
|  | xi=1λ​∑j=1nAi​j​xj=1λ​(Ai​i​xi+∑j≠iAi​j​xj),x\_{i}=\frac{1}{\lambda}\sum\_{j=1}^{n}A\_{ij}\,x\_{j}=\frac{1}{\lambda}\left(A\_{ii}\,x\_{i}+\sum\_{j\neq i}A\_{ij}\,x\_{j}\right), |  |

where the first term Ai​i​xiA\_{ii}\,x\_{i} captures the contribution of self-trade (internal capacity), reflecting a country’s intrinsic importance through its domestic transactions, and the second term ∑j≠iAi​j​xj\sum\_{j\neq i}A\_{ij}\,x\_{j} reflects the influence derived from incoming connections, whereby a node gains importance by receiving trade from other highly central nodes. The centrality values 𝐱\mathbf{x} are estimated by solving the eigenvector problem using power iteration or other numerical eigenvalue methods, specifically computing the principal eigenvector corresponding to the dominant eigenvalue λ\lambda of the adjacency matrix 𝐀\mathbf{A}.

![Refer to caption](plots/centrality.png)


Figure 10:

Since eigenvectors are determined only up to a scalar multiple, the resulting vector 𝐱\mathbf{x} is typically normalized. To interpret the relative importance of each country, we compute the proportion of total centrality as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi=xi2,p\_{i}=x\_{i}^{2}, |  | (1) |

where pi∈[0,1]p\_{i}\in[0,1] represents the squared normalized centrality, providing a probabilistic interpretation of node is contribution to the overall network structure. This normalization ensures that ∑i=1npi=1\sum\_{i=1}^{n}p\_{i}=1, allowing direct comparison of relative influence across countries and over time. Eigenvector centrality therefore provides a nuanced measure of prominence in the network, reflecting both direct transactional activity and the broader position within the network’s structure.

Figure [10](https://arxiv.org/html/2510.22341v1#S3.F10 "Figure 10 ‣ 3 Inter Country Trading Dynamics ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective") presents the temporal evolution of Eigenvector Centrality for the leading countries in the trade network, illustrating how the relative influence of each participant evolves over time. The United Kingdom maintained a dominant position for most of the period from 2011 to 2018, contributing around 90% of the total centrality among the top trading countries. This indicates that the UK was highly connected and linked to other influential countries, giving it a central role in the network.

In 2020, however, the UK’s centrality dropped sharply, likely reflecting the economic and regulatory uncertainties associated with the Brexit protocol, which disrupted trade patterns. UK left the EU in 2021, it launched its own fully independent carbon market, the UK Emissions Trading Scheme (UK ETS) [[14](https://arxiv.org/html/2510.22341v1#bib.bib14)]. By contrast, Germany, Netherlands showed a steady increase in centrality over the period, reflecting their growing influence in the trade network through stronger connections with other central participants.

These trends highlight how structural changes in the network, driven by policy or economic events, can alter the relative influence of major trading countries over time.

## 4  Demand and Supply Analysis

Motivated by the preceding section, we now narrow our analysis to the top three countries, France, Germany, and the United Kingdom, and model the volume of allowances exchanged among them.111Limiting the analysis to three countries (i.e., a 3×33\times 3 network) ensures tractability; including additional participants would substantially increase complexity. We adopt a simple Price-Quantity model:

|  |  |  |
| --- | --- | --- |
|  | Q=a×Pb⟹log⁡Q=log⁡a+b×log⁡P,Q=a\times P^{b}\quad\implies\quad\log Q=\log a+b\times\log P, |  |

where the parameter bb can be interpreted as the price elasticity of demand (EpE\_{p}) [[18](https://arxiv.org/html/2510.22341v1#bib.bib18)]. This measures how much the quantity demanded of a good changes in response to a change in its price, holding other factors constant:

|  |  |  |
| --- | --- | --- |
|  | b=%change in quantity%change in price=d​Qd​P​PQ.b=\frac{\%\ \text{change in quantity}}{\%\ \text{change in price}}=\frac{dQ}{dP}\frac{P}{Q}. |  |

From a market efficiency perspective, these two cases have different implications:

* ∙\bullet

  If |Ep|>1|E\_{p}|>1: Elastic demand means prices serve as strong signals. Small shifts in allowance prices induce large changes in traded quantities, promoting responsiveness and innovation but also potentially increasing volatility. A positive value of EpE\_{p} in this case could reflect speculative or compliance-driven trading, where rising prices are accompanied by higher trading volumes, while a negative value indicates efficient, demand-driven adjustment.
* ∙\bullet

  If |Ep|<1|E\_{p}|<1: Inelastic demand implies greater stability and predictability, but weakens the incentive effect, since higher prices do not translate into substantial reductions in traded quantities.

Appendix Table [3](https://arxiv.org/html/2510.22341v1#Sx1.T3 "Table 3 ‣ Appendix ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective") presents the detailed model summaries. The results indicate that both OLS and LAD estimations yield comparable elasticity patterns across country pairs and periods. In the figure [11](https://arxiv.org/html/2510.22341v1#S4.F11 "Figure 11 ‣ 4 Demand and Supply Analysis ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective"), we examine the daily log of transaction quantities against the log of prices. The price variable is clustered by periods as defined earlier, represented with three distinct colors. The scatter plot displays the relationship between log⁡(P)\log(P) and log⁡(Q)\log(Q), with points color-coded by time period to highlight temporal variation. The black lines represent the Ordinary Least Square (OLS) regression fits of log⁡(Q)\log(Q) on log⁡(P)\log(P) for each period. Solid lines correspond to statistically significant fits (low p-values), while dotted lines indicate insignificant relationships.

![Refer to caption](plots/elasticity.png)


Figure 11: : Transactions of allowances among the top three countries (France, Germany, and the United Kingdom). OLS fits.

We summarize the scatterplot-based price elasticities in a graphical representation in Figure [12](https://arxiv.org/html/2510.22341v1#S4.F12 "Figure 12 ‣ 4 Demand and Supply Analysis ‣ Understanding Carbon Trade Dynamics: A European Union Emissions Trading System Perspective"). In these graphs, the nodes represent the internal price elasticity of transactions within each country, while the edges capture the external price elasticity of transactions between countries. The insignificant price elasticity estimates for external transactions are not shown in the diagram as edges. Three separate graphs are plotted, corresponding to the three time periods considered.

![Refer to caption](plots/elasticity2.png)


Figure 12:

The analysis reveals distinct phases in market responsiveness over time. During 2010-2012, the edges exhibit elastic relationships, indicating that the market was highly responsive even at relatively low price levels. This suggests that firms had access to low-cost abatement options or substitutes, enabling rapid adjustments in trading behavior in response to price changes. In contrast, between 2012 and 2018, nearly all edges appear inelastic, implying reduced responsiveness to price signals, likely reflecting inefficiencies arising from an oversupply of allowances [[11](https://arxiv.org/html/2510.22341v1#bib.bib11)], which weakened price sensitivity as discussed earlier. In the 2018–2020 period, both high price volatility and high elasticity emerge across most edges, signaling a phase of market instability [[12](https://arxiv.org/html/2510.22341v1#bib.bib12), [14](https://arxiv.org/html/2510.22341v1#bib.bib14)]. Participants reacted strongly to price movements, driven by allowance scarcity, tighter regulations, and policy uncertainty, all of which amplified trading responses.

Notably, the UK to France and France to Germany connections do not appear statistically significant (estimated elasticity ≈0\approx 0) in almost all the period, implying that traded quantities with France were largely unresponsive to price changes, potentially due to limited bilateral trading activity or structural barriers to cross-border allowance flows. Even the intra-country transactions within France showed a high positive price elasticity in initial two periods, suggesting possible market inefficiencies. As prices rose, firms traded more actively, likely driven by speculative motives rather than genuine compliance needs.

We observe a non-monotonic evolution in market behavior: an initial elastic phase driven by abundant low-cost abatement opportunities, followed by an inelastic phase marked by oversupply and weak price signals, and culminating in a highly elastic yet volatile regime shaped by regulatory reforms and supply constraints. These patterns highlight the critical role of policy design,particularly in managing allowance supply and harmonizing cross-border mechanisms, to sustain efficient and stable carbon markets. Policymakers must balance allowance scarcity to incentivize abatement with market stability to preserve investor confidence and long-term de-carbonization goals.

## 5  Conclusion

The EU Emissions Trading System (EU ETS), launched in 2005, stands as the world’s first and largest international carbon market, covering approximately 40% of the EU’s greenhouse gas emissions across power generation, manufacturing, and aviation sectors. Since its inception, the EU ETS has successfully contributed to a reduction of over 35% in emissions from covered sectors while maintaining economic competitiveness, demonstrating that market-based mechanisms can effectively balance environmental objectives with economic growth. Through iterative reforms including the introduction of the Market Stability Reserve (MSR) and progressive tightening of the emissions cap the system has evolved into a robust policy instrument that not only incentivizes low-carbon innovation but also serves as a global benchmark for emissions trading schemes worldwide.

Our analysis provides a comprehensive understanding of the dynamics within the European carbon market by examining how market behavior evolved across different policy regimes. We systematically investigate patterns of price movements, transaction dynamics, and inter-country interactions to characterize the structural evolution of the EU ETS.

The evidence from short-term return predictability analysis indicates inefficiencies, with significant autocorrelation in returns suggesting deviations from the efficient market hypothesis. These findings motivated our network-based approach to capturing the international dimension of the market. The network analysis reveals substantial structural shifts in transaction flows over time, characterized by a core-periphery structure in which a small subset of countries, predominantly the United Kingdom, Germany, France, and the Netherlands, occupy central positions as dominant trading hubs, while the majority of participating nations remain at the periphery with limited connectivity. The price elasticity analysis further elucidates heterogeneous trading responses to price fluctuations across distinct policy phases. Both intra- and inter-country trades exhibited markedly different elasticities depending on the regulatory environment, reflecting the interplay between speculative activity and compliance-driven motives. Notably, we also observe country-specific heterogeneity in elasticity patterns for major participants.

Collectively, these findings highlight the complex interplay between policy design, market structure, and trading behavior in the EU ETS, emphasizing the need for coordinated regulatory frameworks that account for national heterogeneity while promoting market integration and efficiency.

Phase 4 (2021–2030) of the EU ETS outlines an optimistic trajectory toward a decarbonized European economy. With a progressively tightening emissions cap, a refined Market Stability Reserve, and an expanded sectoral scope, it enhances price signals and fosters low-carbon investment. If effectively implemented, Phase 4 has the potential to transform the EU ETS into a resilient, innovation-driven market that efficiently drives emission reductions while supporting Europe’s long-term climate ambitions. Our analysis presents a novel perspective on market behavior within the EU ETS, offering new insights into its evolving efficiency and responsiveness. While preliminary, this study opens multiple avenues for further research, including analyses of surrender data, more advanced investigations into return predictability, and a deeper exploration of price elasticity dynamics. Such extensions would enrich the understanding of how market mechanisms can effectively support Europe’s transition toward a low-carbon future.

## References

* [1]

  Abrell, J. (2024). Database for the European Union Transaction Log. Available at <https://www.euets.info>.
* [2]

  Borri, N., Liu, Y., Tsyvinski, A., & Wu, X. (2024). Inefficiencies of Carbon Trading Markets. <https://arxiv.org/abs/2408.06497>.
* [3]

  Hintermann, B., Peterson, S., & Rickels, W. (2016). Price and Market Behavior in Phase II of the EU ETS: A Review of the Literature. Review of Environmental Economics and Policy, 10(1), 108–128.
* [4]

  Ibikunle, G., Gregoriou, A., Hoepner, A. G., & Rhodes, M. (2016). Liquidity and Market Efficiency in the World’s Largest Carbon Market. British Accounting Review, 48(4), 431–447.
* [5]

  Zhang, Z., Li, S., & Zhang, W. (2024). The Predictability of Carbon Futures Volatility: New Evidence from the Spillovers of Fossil Energy Futures Returns. Journal of Futures Markets, 44(3), 512–530.
* [6]

  Zhao, Y., Gong, X., Zhang, W., & Xu, W. (2024). Forecasting Carbon Futures Returns Using Feature Selection and Markov Chain with Sample Distribution. Energy Economics, 140, 108079.
* [7]

  Zhang, J., & Han, W. (2022). Carbon Emission Trading and Equity Markets in China: How Liquidity is Impacting Carbon Returns? Economic Research-Ekonomska Istraživanja, 35(1), 402–420.
* [8]

  Kim, J., & Park, K. (2021). Improving Liquidity in Emission Trading Schemes. Journal of Futures Markets, 41(9), 1397–1411.
* [9]

  EUETS.INFO <https://www.euets.info/download>.
* [10]

  ICAP. <https://icapcarbonaction.com/en/ets-prices>.
* [11]

  European Commission. (2025). Surplus of Allowances. Retrieved from <https://climate.ec.europa.eu/eu-action/carbon-markets/eu-emissions-trading-system-eu-ets/market-stability-reserve_en#:~:text=In%202013%2C%20the,381%20million%20allowances>
* [12]

  European Commission. (2025). Market Stability Reserve. Retrieved from <https://climate.ec.europa.eu/eu-action/carbon-markets/eu-emissions-trading-system-eu-ets/market-stability-reserve_en#:~:text=The%20Market%20Stability%20Reserve%20(MSR)%20was,2018%20and%20began%20operating%20in%202019.>
* [13]

  Döme, B. (2005). Efficiency and Return Predictability: What can we learn from stock market data? C.U. Budapest. May 2, 2005.
* [14]

  Gov UK. UK ETS <https://www.gov.uk/government/publications/uk-emissions-trading-scheme-uk-ets-policy-overview/uk-emissions-trading-scheme-uk-ets-a-policy-overview?utm_source=chatgpt.com#what-is-the-uk-ets:~:text=The%20UK%2C%20Scottish,1%20January%202021.>
* [15]

  Horvath, S. (2011). Weighted network analysis: Applications in genomics and systems biology. Springer.
* [16]

  Wasserman, S., & Faust, K. (1994). Social network analysis: Methods and applications. Cambridge University Press. <https://doi.org/10.1017/CBO9780511815478>
* [17]

  Bloch, F., Jackson, M. O., & Tebaldi, P. (2021). Centrality measures in networks. <https://arxiv.org/pdf/1608.05845>
* [18]

  Varian, H. R. (2014). Intermediate Microeconomics: A Modern Approach (9th ed.). W.W. Norton & Company.

Link to the codes used in the study: [Github](https://github.com/Avirup23/Carbon-Market-Analysis.git)

## Appendix

Table 3: OLS and LAD Regression Results: Log Quantity on Log Price by Country Pair and Period

| From | To | Period | OLS | | | | LAD | | | | N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| β^0\hat{\beta}\_{0} | pp-val | β^1\hat{\beta}\_{1} | pp-val | β^0\hat{\beta}\_{0} | pp-val | β^1\hat{\beta}\_{1} | pp-val |
| France | France | 2010–2012 | 10.70 | 0.000 | 1.15\*\*\* | 0.000 | 8.42 | 0.000 | 2.08\*\*\* | 0.000 | 495 |
| France | France | 2012–2018 | 8.63 | 0.000 | 1.74\*\*\* | 0.000 | 7.87 | 0.000 | 2.22\*\*\* | 0.000 | 843 |
| France | France | 2018–2020 | 9.55 | 0.000 | 0.65 | 0.131 | 8.08 | 0.000 | 1.09 | 0.058 | 347 |
| France | Germany | 2010–2012 | 15.84 | 0.000 | -1.72\* | 0.036 | 15.30 | 0.000 | -1.35 | 0.144 | 214 |
| France | Germany | 2012–2018 | 12.17 | 0.000 | -0.47 | 0.180 | 12.33 | 0.000 | -0.53 | 0.065 | 508 |
| France | Germany | 2018–2020 | 12.55 | 0.000 | -0.40 | 0.496 | 12.29 | 0.000 | -0.32 | 0.626 | 182 |
| France | UK | 2010–2012 | 11.23 | 0.000 | 0.42 | 0.392 | 11.11 | 0.000 | 0.55 | 0.278 | 387 |
| France | UK | 2012–2018 | 13.15 | 0.000 | -0.83\*\* | 0.002 | 13.49 | 0.000 | -1.07\*\*\* | 0.000 | 972 |
| France | UK | 2018–2020 | 9.73 | 0.000 | 0.34 | 0.490 | 10.57 | 0.000 | 0.08 | 0.875 | 201 |
| Germany | France | 2010–2012 | 18.31 | 0.000 | -2.84\*\*\* | 0.001 | 18.53 | 0.000 | -2.88\*\* | 0.009 | 179 |
| Germany | France | 2012–2018 | 12.83 | 0.000 | -0.64\* | 0.016 | 12.50 | 0.000 | -0.49 | 0.055 | 750 |
| Germany | France | 2018–2020 | 5.29 | 0.004 | 2.20\*\*\* | 0.000 | 2.64 | 0.154 | 3.11\*\*\* | 0.000 | 267 |
| Germany | Germany | 2010–2012 | 17.37 | 0.000 | -1.78\*\* | 0.002 | 19.67 | 0.000 | -2.65\*\*\* | 0.001 | 467 |
| Germany | Germany | 2012–2018 | 16.51 | 0.000 | -1.56\*\*\* | 0.000 | 16.41 | 0.000 | -1.42\*\*\* | 0.000 | 1467 |
| Germany | Germany | 2018–2020 | 15.09 | 0.000 | -0.17 | 0.427 | 15.18 | 0.000 | -0.19 | 0.431 | 581 |
| Germany | UK | 2010–2012 | 16.99 | 0.000 | -1.93\*\*\* | 0.001 | 18.50 | 0.000 | -2.45\*\*\* | 0.000 | 322 |
| Germany | UK | 2012–2018 | 15.73 | 0.000 | -0.99\*\*\* | 0.000 | 15.39 | 0.000 | -0.67\*\*\* | 0.000 | 1353 |
| Germany | UK | 2018–2020 | 17.50 | 0.000 | -1.29\*\*\* | 0.000 | 17.77 | 0.000 | -1.37\*\*\* | 0.000 | 553 |
| UK | France | 2010–2012 | 10.16 | 0.000 | 0.71 | 0.184 | 9.06 | 0.000 | 1.11 | 0.136 | 370 |
| UK | France | 2012–2018 | 11.54 | 0.000 | -0.14 | 0.627 | 11.79 | 0.000 | -0.14 | 0.646 | 1109 |
| UK | France | 2018–2020 | 10.75 | 0.000 | 0.01 | 0.978 | 11.59 | 0.000 | -0.23 | 0.605 | 310 |
| UK | Germany | 2010–2012 | 17.06 | 0.000 | -2.21\*\*\* | 0.000 | 17.42 | 0.000 | -2.35\*\*\* | 0.000 | 310 |
| UK | Germany | 2012–2018 | 13.46 | 0.000 | -0.55\* | 0.036 | 12.60 | 0.000 | -0.11 | 0.719 | 1279 |
| UK | Germany | 2018–2020 | 18.33 | 0.000 | -2.19\*\*\* | 0.000 | 21.04 | 0.000 | -3.10\*\*\* | 0.000 | 432 |
| UK | UK | 2010–2012 | 12.01 | 0.000 | 0.71 | 0.094 | 10.27 | 0.000 | 1.46\*\*\* | 0.000 | 486 |
| UK | UK | 2012–2018 | 15.92 | 0.000 | -0.77\*\*\* | 0.000 | 15.41 | 0.000 | -0.52\* | 0.022 | 1481 |
| UK | UK | 2018–2020 | 23.96 | 0.000 | -3.39\*\*\* | 0.000 | 25.84 | 0.000 | -3.94\*\*\* | 0.000 | 534 |

Note: The model is ln⁡(Quantity)=β0+β1​ln⁡(Price)+ϵ\ln(\text{Quantity})=\beta\_{0}+\beta\_{1}\ln(\text{Price})+\epsilon. OLS = ordinary least squares; LAD = least absolute deviation (median regression). β^1\hat{\beta}\_{1} represents price elasticity. Significance: \* p<0.05p<0.05, \*\* p<0.01p<0.01, \*\*\* p<0.001p<0.001. N = number of observations.

![Refer to caption](plots/acf-pacf.png)


Figure 13:

![Refer to caption](plots/forecast.png)


Figure 14: