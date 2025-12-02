---
authors:
- Kundan Mukhia
- Buddha Nath Sharma
- Salam Rabindrajit Luwang
- Md. Nurujjaman
- Chittaranjan Hens
- Suman Saha
- Tanujit Chakraborty
doc_id: arxiv:2512.00893v1
family_id: arxiv:2512.00893
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic
  Behavior Around the 2024 U.S. Election'
url_abs: http://arxiv.org/abs/2512.00893v1
url_html: https://arxiv.org/html/2512.00893v1
venue: arXiv q-fin
version: 1
year: 2025
---


\fnmKundan \surMukhia
  
\fnmBuddha Nath \surSharma
  
\fnmSalam Rabindrajit \surLuwang
  
\fnmMd. \surNurujjaman
  
\fnmChittaranjan \surHens
  
\fnmSuman \surSaha
  


[tanujit.chakraborty@sorbonne.ae](mailto:tanujit.chakraborty@sorbonne.ae)
[
[
[
[
[

###### Abstract

We study how the 2024 U.S. presidential election, viewed as a major political risk event, affected cryptocurrency markets by distinguishing human-driven peer-to-peer stablecoin transactions from automated algorithmic activity. Using structural break analysis, we find that human-driven Ethereum Request for Comment 20 (ERC-20) transactions shifted on November 3, two days before the election, while exchange trading volumes reacted only on Election Day. Automated smart-contract activity adjusted much later, with structural breaks appearing in January 2025. We validate these shifts using surrogate-based robustness tests. Complementary energy-spectrum analysis of Bitcoin and Ethereum identifies pronounced post-election turbulence, and a structural vector autoregression confirms a regime shift in stablecoin dynamics. Overall, human-driven stablecoin flows act as early-warning indicators of political stress, preceding both exchange behavior and algorithmic responses.

###### keywords:

Political uncertainty, Cryptocurrency markets, Stablecoins, Human–Algorithmic divergence, Structural breaks, Early warning system

## 1 Introduction

Exogenous events such as political elections, geopolitical conflicts, pandemics, and macroeconomic policy announcements are widely recognized as powerful forces that disrupt complex systems, including stock markets, commodity markets, and global economies [zhang2009estimating, cutler1988moves, beber2010cannot, corbet2020impact, mukhia2024complex]. Financial markets often react sharply to such events, reflecting changes in investor sentiment, expectations, and perceptions of risk. Theoretical frameworks establish that markets are frequently dominated by political discourse, where news about government actions and electoral prospects significantly influences asset prices [pastor2013political]. These studies highlight that political uncertainty can generate both short-term volatility and long-term structural shifts in financial systems [zhang2009estimating, bloom2009impact]. It is observed that over 36% of stock market movements are driven by political news as compared to 23% from macroeconomic news and 11% from corporate earnings [bialkowski2022high]. This evidence suggests that financial markets are not only driven by fundamentals but are highly sensitive to evolving political narratives. As financial systems become more globally integrated and information-driven, political shocks now propagate more rapidly, amplifying volatility and uncertainty across asset classes.

In recent years, the emergence of cryptocurrency markets has added a new dimension to the interaction between politics and finance. Decentralized digital assets operate outside traditional institutional boundaries, yet they increasingly exhibit sensitivity to macroeconomic and political developments [chen2020blockchain, omrane2025exploring, corbet2020cryptocurrency]. The global reach of cryptocurrencies and the speed of information flow through online and social platforms create conditions under which political narratives can immediately influence trading and investment behavior [shiller2020narrative]. Stablecoins such as Tether (USDT) and USD Coin (USDC) have become key components of the cryptocurrency market. By combining blockchain efficiency with fiat currency stability [ante2021influence], stablecoins mitigate the volatility of major cryptocurrencies like Bitcoin (BTC) and Ethereum(ETH) [dyhrberg2016bitcoin, katsiampa2017volatility]. They play an essential role in liquidity provision, trading pairs, and market stability [lyons2023keeps, coinmarketcap2025stablecoin]. However, despite their design for stability, stablecoins remain exposed to systemic risks from external shocks, particularly political uncertainty, which can affect their pegs, transaction volumes, and user behavior.

Some of the key contributions relevant to this direction are discussed. De Blasis et al. (2023) investigate the May 2022 collapse of USDT using Baba, Engle, Kraft, and Kroner (1990) (BEKK) models, finding that design differences among stablecoins significantly influence the direction, magnitude, and duration of their responses to the crisis [de2023intelligent]. Grobys and Huynh (2022) examine whether jumps in USDT Granger-cause Bitcoin returns, finding that positive jumps in USDT significantly predict subsequent negative Bitcoin price changes, highlighting inefficiencies in the cryptocurrency market [grobys2022tether]. Y-H Lee et al. (2025) develop predictive models to assess the risk of stablecoin depegging, focusing on the top four USD-pegged stablecoins. Their findings highlight that major cryptocurrency fluctuations (BTC and ETH) significantly influence stablecoin stability, while sentiment variables add limited predictive power [lee2025stablecoin]. Gadzinski et al. (2024) analyze the co-instability of stablecoins by detecting structural breaks and spillover effects using Dynamic Time Warping and (Dynamic Conditional Correlation) DCC-GARCH models. They show that algorithmic stablecoins were most vulnerable during crashes, while fiat-backed tokens displayed greater resilience [gregory2024break]. Eichengreen et al. (2025) analyze the devaluation risk of stablecoins by constructing market-based measures of run risk from Tether spot and futures prices. They find that partial default risk can reach up to 12% points, driven largely by Bitcoin volatility, transaction velocity, and redemption activity [eichengreen2025stablecoin]. Recently, the role of political signal quality in predicting cryptocurrency returns has been examined, focusing on the “crypto president” narrative during the 2024 U.S. presidential election. This study found that political news influences cryptocurrency prices in the short term and that sentiment-based measures outperform historical cryptocurrency data in predictive power [jabeur2025crypto].

However, these studies mainly rely on exchange-based data and text sentiment analysis, leaving a gap in understanding how blockchain-based transaction patterns, especially those separating human and algorithmic activity, respond to political shocks. Building on this evidence, our study extends the analysis by moving beyond price-based and sentiment-driven perspectives to explore how political uncertainty is transmitted through blockchain-based activity. Specifically, we investigate how political shocks affect blockchain transaction behavior, distinguishing between human-driven and algorithmic activity, and examine whether these behavioral patterns can serve as early indicators of market turbulence. In this study, we address this gap by examining the 2024 U.S. Presidential Election as a major political shock and analyzing its impact on cryptocurrency market dynamics through ERC-20 blockchain data. Our analysis captures the temporal sequence of human versus automated responses to political uncertainty, providing a new perspective on how behavioral and structural patterns develop during periods of market stress.

The contribution of our study can be summarized as follows.

* •

  We distinguish between Externally Owned Account (EOA–EOA) transactions, which capture human-driven behavior, and Smart Contract (SC–SC) transactions, which represent automated algorithmic activity, in the context of political shocks.
* •

  We employ a multi-method approach combining structural break analysis, Hilbert-Huang Transform, and structural vector autoregression to identify both the timing and transmission mechanisms of election-induced shocks.
* •

  We demonstrate that human-driven blockchain activity serves as a leading indicator for subsequent market turbulence, providing an early indicator before exchange-based trading reacts and months before automated systems recalibrate. The 2024 U.S. election serves as a critical example validating the human-driven signal as a component of the early warning system for the politically induced financial stress.

These findings have practical implications for investors, risk managers, and policymakers navigating periods of political uncertainty in cryptocurrency markets. For the investors, this early signal offers a clear, data-driven insight for making timely portfolio adjustments. For risk managers, it helps to improve the market prediction model by adding real-time blockchain data. For policymakers, it provides the crucial understanding of how political stress spreads in the financial system, which is vital to make effective policies and maintaining a stable economy.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2512.00893v1#S2 "2 Problem definition and data description ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election") explains the data sources and preprocessing steps. Section [3](https://arxiv.org/html/2512.00893v1#S3 "3 Methodology ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election") describes the methodological framework used in the analysis. Section [4](https://arxiv.org/html/2512.00893v1#S4 "4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election") reports the main empirical results, including the structural break tests, Hilbert spectrum analysis, and structural vector autoregression. Section [5](https://arxiv.org/html/2512.00893v1#S5 "5 Conclusion and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election") concludes with the key findings and their implications for investors, policymakers, and future research.

## 2 Problem definition and data description

In this study, we analyze one year of ERC-20 blockchain transaction data, covering the period from March 2024 to February 2025 [zhang2009estimating, mukhia2025universal, xblock2025eth]. This one-year timeframe was selected to capture both pre-election and post-election market dynamics surrounding the 2024 U.S. Presidential election. The ERC-20 transaction dataset contains nine columns, each providing specific information about ERC-20 token transfers. Each column is summarized in Table [1](https://arxiv.org/html/2512.00893v1#S2.T1 "Table 1 ‣ 2 Problem definition and data description ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election"). For our analysis, we utilize the following columns: timeStamp, tokenAddress, fromIsContract, toIsContract, and value.

Table 1: Data description of ERC-20 blockchain transaction dataset columns and their descriptions. The dataset records detailed information for each token transfer, including the block timestamp, token contract address, sender and receiver accounts, and transfer amount.

|  |  |
| --- | --- |
| Column | Description |
| timeStamp | The time when the block was created; all transactions within the same block share this timestamp. |
| tokenAddress | The hash value of the ERC-20 token’s contract, which serves as its unique identifier. |
| from | The Ethereum address of the sender of the ERC-20 token. |
| to | The Ethereum address of the receiver of the ERC-20 token. |
| fromIsContract | Indicates whether the sender is an SC (1) or an EOA (0). |
| toIsContract | Indicates whether the receiver is an SC (1) or an EOA (0). |
| value | The amount of tokens transferred, in the token’s base unit. |
| \botrule |  |

We first pre-processed the ERC-20 blockchain transaction dataset before conducting the analysis. On the Ethereum blockchain, there are thousands of ERC-20 tokens, including both stablecoins and non-stable assets. Among these, we focused on the two largest stablecoins by market share, USDT and USDC, which together account for more than 80% of the total stablecoin market capitalization [coinmarketcap2025stablecoin]. Each token was identified by its verified contract address on Etherscan [etherscan2025eth]:

* •

  USDT: 0xdac17f958d2ee523a2206206994597c13d831ec7
* •

  USDC: 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48

In the ERC-20 framework, two types of accounts exist. EOAs are controlled by individuals through public-private key pairs and represent human users [chen2020traveling, mukhia2025universal]. Whereas SCs are governed by executable code stored within the blockchain account itself [szabo1997idea, kolvart2016smart]. These account types are indicated in the dataset by the columns fromIsContract and toIsContract, summarized in Table [1](https://arxiv.org/html/2512.00893v1#S2.T1 "Table 1 ‣ 2 Problem definition and data description ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election"). A transaction is labeled as EOA–EOA (human-driven) when fromIsContract = 0 and toIsContract = 0, while SC–SC transactions are identified when fromIsContract = 1 and toIsContract = 1. Each transaction in the ERC-20 data set is recorded with a timestamp in UTC format [wikipedia2025unixtime]. For example, the value 1715385600 corresponds to 2024-11-05, based on the Unix epoch starting from 1970-01-01 00:00:00 UTC. In this study, we converted these UTC timestamps into a human-readable format (YYYY-MM-DD) for analysis. To capture how human-driven and automated execution responded to the U.S. Presidential Election shock, we focus on two transaction categories: EOA–EOA and SC–SC. Table [2](https://arxiv.org/html/2512.00893v1#S2.T2 "Table 2 ‣ 2 Problem definition and data description ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election") summarizes the distribution of these transaction types.

Table 2: Summary of ERC-20 transaction types based on sender and receiver account classification. Transactions are divided into human-driven (EOA–EOA) and automated (SC–SC) categories using the fromIsContract and toIsContract. This classification helps us to distinguish between human-initiated transfers and code-executed activities on the Ethereum blockchain, providing a foundation for analyzing behavioral and algorithmic responses to political shocks.

|  |  |  |  |
| --- | --- | --- | --- |
| fromIsContract | toIsContract | Transaction Type | Number of Transactions |
| 0 | 0 | EOA–EOA (Human-driven) | 50,597,281 |
| 1 | 1 | SC–SC (Automated code-driven) | 24,393,131 |
| Total Transactions | | | 102,575,812 |
| \botrule |  |  |  |

On the Ethereum blockchain, the value of USDT and USDC is stored in their smallest indivisible unit, not directly in U.S. dollars (USD). Both tokens use six decimal places, which means that the raw number in the value column is the actual amount multiplied by 10610^{6}. To convert this into the real transaction amount in USD, we divide the raw value by 10610^{6}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | USD Value=value106\text{USD Value}=\frac{\texttt{value}}{10^{6}} |  | (1) |

For example, a recorded value of 1,000,000 corresponds to 1.0 USD. Duplicate, failed, and zero-value transactions were removed to reduce noise. Finally, daily transaction volumes were aggregated separately for EOA–EOA and SC–SC activities, forming two time series that represent human-driven and automated blockchain behavior. These time series were merged with daily trading volume data for USDT and USDC, as well as closing prices for BTC and Ethereum ETH, to align blockchain activity with broader market conditions around the 2024 US presidential election. This allows us to correlate changes in blockchain transaction behavior with shifts in market-wide liquidity, trading activity, and the prices of major digital assets, particularly around the 2024 U.S. Presidential election.

## 3 Methodology

To study how the 2024 U.S. Presidential election affected cryptocurrency market dynamics, we applied several complementary analytical methods. We employed several statistical tests, such as the Bai-Perron test, to identify significant regime changes in stablecoin ERC-20 blockchain transactions and trading volumes, and the Augmented Dickey-Fuller test for stationarity check. We then applied the Hilbert–Huang Transform to detect extreme events and quantify market turbulence in major cryptocurrencies. Next, we implemented Amplitude-Adjusted Fourier Transform surrogate testing to validate the statistical significance of the identified breakpoints against noise. Finally, we applied structural vector autoregression with Wald tests to analyze volatility spillovers and confirm structural changes between pre- and post-election periods. Further details on each of these techniques are discussed below.

### 3.1 Statistical tests

In this section, we employ various statistical tests to determine key time series properties. The Augmented Dickey-Fuller test assesses stationarity, the Bai-Perron test detects structural breaks, which are sudden shifts in the time series mean, with the SupF test validating their statistical significance, as presented below.

#### 3.1.1 Augmented Dickey-Fuller test

The Augmented Dickey–Fuller (ADF) test is a widely used statistical test for examining the stationarity of time series data [amarasinghe2015dynamic, paramati2011empirical, yang2020novel]. This test is the extended form of the original Dickey–Fuller (DF) test, which models the time series as an autoregressive process of order one, AR(1) [dickey1981likelihood]. To address the problem of autocorrelation in the DF test, Said and Dickey introduced the ADF test by incorporating additional lagged terms of the dependent variable into the regression [said1984testing, herranz2017unit].

Let’s say yty\_{t} follows an autoregressive process. The ADF regression can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​yt=β+γ​t+α​yt−1+∑j=1nψj​Δ​yt−j+εt,\Delta y\_{t}=\beta+\gamma t+\alpha y\_{t-1}+\sum\_{j=1}^{n}\psi\_{j}\Delta y\_{t-j}+\varepsilon\_{t}, |  | (2) |

where Δ\Delta is the first-difference operator, β\beta is a constant, γ\gamma captures a deterministic trend, and εt\varepsilon\_{t} is white noise.

The ADF test is used to determine whether a time series contains a unit root, which would suggest that the series is non-stationary. In this model, the null hypothesis assumes the presence of a unit root in the series, while the alternative hypothesis assumes that the time series is stationary and does not have a unit root [paparoditis2018asymptotic]. The hypotheses for the ADF test are

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0:α=1⇒yt∼I​(1)H\_{0}:\alpha=1\;\;\Rightarrow\;\;y\_{t}\sim I(1) |  | (3) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | H1:|α|<1⇒yt∼I​(0)H\_{1}:|\alpha|<1\;\;\Rightarrow\;\;y\_{t}\sim I(0) |  | (4) |

The test statistic is based on the least squares estimate of Eq. [2](https://arxiv.org/html/2512.00893v1#S3.E2 "In 3.1.1 Augmented Dickey-Fuller test ‣ 3.1 Statistical tests ‣ 3 Methodology ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election"), expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | tα=1=α^−1S​E​(α)t\_{\alpha=1}=\frac{\hat{\alpha}-1}{SE(\alpha)} |  | (5) |

where α^\hat{\alpha} is the least squares estimate and S​E​(α)SE(\alpha) denotes its standard error.

The ADF test reports the tt-statistic, pp-value, and critical values at different significance levels. Since the distribution of tαt\_{\alpha} under the null is non-standard, critical values have been provided by DF (1979) and refined by MacKinnon (1996) [mackinnon1996numerical]. If the computed statistic is smaller than the critical value, the null hypothesis of a unit root is rejected, and the series is considered stationary. Otherwise, the series is deemed non-stationary and must be differenced to achieve stationarity [kim2017unit]. In our study, we used the ADF test to verify the stationarity conditions required before estimating the structural vector autoregression model and conducting Hilbert Spectrum extreme event analysis.

#### 3.1.2 Bai-Perron test

Financial time series often exhibit sudden shifts in their statistical properties due to various economic, political, or market-related events [sengupta2025forecasting, besher5705079modeling]. Examples include financial crises, policy interventions, elections, and global shocks, all of which can lead to changes in the underlying data-generating process [mahata2020identification, chaudhuri2003random, worthington2007gold]. Identifying such structural changes is crucial for understanding market dynamics, evaluating risk, and accurately modeling financial behavior [chakraborty2025neural].

To detect these shifts, we employ the multiple structural break methodology proposed by Bai and Perron (BP) [bai1998estimating, bai2003computation], which provides an endogenous framework for identifying unknown breakpoints in time series without requiring prior knowledge of their locations. The BP test jointly estimates the number and timing of breaks as well as the model parameters associated with each regime by minimizing the global sum of squared residuals (SSR).

Consider a multiple structural change regression model with mm breakpoints

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=xt′​β+zt′​δj+ut,t=Tj−1+1,…,Tj,j=1,…,m+1,y\_{t}=x\_{t}^{\prime}\beta+z\_{t}^{\prime}\delta\_{j}+u\_{t},\quad t=T\_{j-1}+1,\dots,T\_{j},\quad j=1,\dots,m+1, |  | (6) |

where yty\_{t} is the observed dependent variable, xt∈ℝpx\_{t}\in\mathbb{R}^{p} and zt∈ℝqz\_{t}\in\mathbb{R}^{q} are vectors of covariates, β\beta and δj\delta\_{j} are coefficient vectors, and utu\_{t} is the error term. . The index jj identifies the different regimes in the time series, with each regime j=1,…,m+1j=1,\dots,m+1 covering the observations between two successive break dates. The break dates (T1,…,Tm)(T\_{1},\dots,T\_{m}) are unknown and estimated directly from the data.

For a given partition (T1,…,Tm)(T\_{1},\dots,T\_{m}), the least-squares estimators β^\hat{\beta} and δ^j\hat{\delta}\_{j} are obtained by minimizing the sum of squared residuals(SSR)

|  |  |  |  |
| --- | --- | --- | --- |
|  | SSR​(T1,…,Tm)=∑i=1m+1∑t=Ti−1+1Ti(yt−xt′​β−zt′​δi)2.\text{SSR}(T\_{1},\dots,T\_{m})=\sum\_{i=1}^{m+1}\sum\_{t=T\_{i-1}+1}^{T\_{i}}\left(y\_{t}-x\_{t}^{\prime}\beta-z\_{t}^{\prime}\delta\_{i}\right)^{2}. |  | (7) |

The optimal break dates are then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {T^1,…,T^m}=arg⁡min(T1,…,Tm)⁡SSR​(T1,…,Tm),\{\hat{T}\_{1},\dots,\hat{T}\_{m}\}=\arg\min\_{(T\_{1},\dots,T\_{m})}\text{SSR}(T\_{1},\dots,T\_{m}), |  | (8) |

where the minimization is subject to a trimming parameter to ensure sufficient observations within each regime.

A dynamic programming algorithm [bai2003computation] is used to evaluate all possible partitions efficiently and select the global minimum of the SSR. This approach provides consistent estimates of both the break dates and the associated regime-specific model parameters.

In this study, we use log-transformed data and model it as a mean-shift process

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=μj+ut,t=Tj−1+1,…,Tj,j=1,…,m+1,y\_{t}=\mu\_{j}+u\_{t},\quad t=T\_{j-1}+1,\dots,T\_{j},\quad j=1,\dots,m+1, |  | (9) |

where yty\_{t} is the log-value at time tt, μj\mu\_{j} is the regime-specific mean,
utu\_{t} is the error term, TjT\_{j} are the breakpoints, and mm is the number of
estimated breaks. A breakpoint indicates a shift from one mean level μj\mu\_{j}
to another μj+1\mu\_{j+1}, capturing structural changes in the series.

To validate whether the breakpoints identified by the BP procedure represent statistically significant structural changes rather than random fluctuations, we implement the SupF hypothesis tests. This test verifies parameter stability and confirms the significance of detected regime shifts.

#### 3.1.3 SupF test

The SupF test [bai1998estimating, bai2003critical] is used to examine whether at least one structural break exists within the time series. The hypotheses for the SupF test can be stated as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H0\displaystyle H\_{0} | :No structural break exists,\displaystyle:\text{No structural break exists}, |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H1\displaystyle H\_{1} | :At least one structural break exists.\displaystyle:\text{At least one structural break exists}. |  | (11) |

The SupF statistic is computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | SupF=maxτ∈Λ⁡F​(τ),\text{SupF}=\max\_{\tau\in\Lambda}F(\tau), |  | (12) |

where F​(τ)F(\tau) is the F-statistic testing parameter stability at break fraction τ\tau, and Λ=[τmin,τmax]\Lambda=[\tau\_{\text{min}},\tau\_{\text{max}}] represents the set of all possible break fractions within the trimmed time series.

The F-statistic for a candidate break fraction τ\tau is calculated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(τ)=(S​S​R0−S​S​R1)/qS​S​R1/(T−2​q),F(\tau)=\frac{(SSR\_{0}-SSR\_{1})/q}{SSR\_{1}/(T-2q)}, |  | (13) |

where S​S​R0SSR\_{0} is the sum of squared residuals under H0H\_{0}, S​S​R1SSR\_{1} is the sum of squared residuals under H1H\_{1}, qq is the number of parameters subject to change, and TT is the total number of observations.

We reject H0H\_{0} at the 5% significance level if the p-value associated with the SupF statistic is less than 0.05, concluding that at least one structural break is present. In our mean-shift model, this corresponds to a statistically significant change in the average level of the log-transformed series. We used the BP test together with the SupF test to identify and validate structural shifts in stablecoin and cryptocurrency markets around the 2024 U.S. election.

### 3.2 Transformation methods

After establishing the presence of structural breaks, this section presents the methodologies to detect, validate, and analyze these breaks. With the Hilbert spectrum, we detect the timing of the sudden change. The Amplitude-Adjusted Fourier Transform then provides the statistical validation of the BP test and Hilbert spectrum findings. Subsequently, structural vector autoregression analyzes the dynamic relationships between the time series across regimes. Finally, the Wald test is applied to the pre- and post-breakpoint regimes of the structural vector autoregression analyses to quantify the significance of the structural change, as presented in detail in the following subsections.

#### 3.2.1 Hilbert–Huang Transform (HHT)

The Empirical Mode Decomposition (EMD) technique is widely applied to decompose nonlinear and nonstationary time series data by separating the signal into a set of Intrinsic Mode Functions (IMFs). Each IMF is associated with a distinct time scale [huang1998empirical, huang2003applications, mahata2020identification].

A time series signal component is considered an IMF when the following two conditions are satisfied

* •

  The number of extrema and zero-crossings should be the same, or differ by one.
* •

  The mean of the envelopes formed by the local maxima and minima should be zero.

The steps for decomposing a time series signal into IMFs are discussed below.

1. 1.

   For a input time series dataset DtD\_{t}, construct the upper envelope (U​EtUE\_{t}) from its local maxima and the lower envelope (L​EtLE\_{t}) from its local minima using spline fitting.
2. 2.

   Calculate the mean of the upper and lower envelopes,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | mt=U​Et+L​Et2,m\_{t}=\frac{UE\_{t}+LE\_{t}}{2}, |  | (14) |

   and subtract this mean from the original time series signal to obtain the updated time series.

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | N​Dt=Dt−mt.ND\_{t}=D\_{t}-m\_{t}. |  | (15) |
3. 3.

   Repeat the process on N​DtND\_{t} until it satisfies the two IMF conditions. When these conditions are satisfied, the resulting time series is considered as the first IMF, denoted by I​M​F1IMF\_{1}.
4. 4.

   For the next IMF, calculate the residual

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Nt=Dt−I​M​F1,N\_{t}=D\_{t}-IMF\_{1}, |  | (16) |

   and apply the same step to NtN\_{t}.
5. 5.

   The decomposition process continues until the final residual becomes monotonic, which is consider to as the residue. The residue show the overall trend of the original dataset.
6. 6.

   The original dataset can then be reconstructed as the sum of all IMFs and the residue

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Dt=∑j=1nI​M​Fj+residue,D\_{t}=\sum\_{j=1}^{n}IMF\_{j}+\text{residue}, |  | (17) |

   where nn is the total number of IMFs.

For each IMF, the instantaneous frequency ω\omega is obtained by applying the Hilbert transform, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(t)=1π​P.V.​∫−∞∞IMF​(τ)t−τ​𝑑τ,H(t)=\dfrac{1}{\pi}\,\text{P.V.}\int\_{-\infty}^{\infty}\dfrac{\text{IMF}(\tau)}{t-\tau}\,d\tau, |  | (18) |

where P.V. represents the Cauchy principal value. The instantaneous phase ϕ​(t)\phi(t) is expressed as [huang1998empirical]

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(t)=tan−1⁡(H​(t)IMF​(t)),\phi(t)=\tan^{-1}\left(\dfrac{H(t)}{\text{IMF}(t)}\right), |  | (19) |

and the instantaneous frequency ω\omega is obtained from

|  |  |  |  |
| --- | --- | --- | --- |
|  | ω=d​ϕd​t.\omega=\dfrac{d\phi}{dt}. |  | (20) |

The Hilbert spectrum H​(t,ω)H(t,\omega) (HS), which represents the time-frequency distribution of the time series signal, is calculated using

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(t,ω)=ℜ⁡{∑iKi​(t)​ej​∫ω​(t)​𝑑t},H(t,\omega)=\Re\left\{\sum\_{i}K\_{i}(t)\,e^{j\int\omega(t)\,dt}\right\}, |  | (21) |

where Ki​(t)K\_{i}(t) is the instantaneous amplitude and ℜ⁡{⋅}\Re\{\cdot\} denotes the real part.

The instantaneous energy, denoted as I​E​(t)IE(t), can be calculated from the Hilbert spectrum and is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​E​(t)=∫ωH2​(t,ω)​𝑑ω.IE(t)=\int\_{\omega}H^{2}(t,\omega)\,d\omega. |  | (22) |

The normalized instantaneous energy I​EN​(t)IE\_{N}(t) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​EN​(t)=I​E​(t)max⁡[I​E​(t)].IE\_{N}(t)=\dfrac{IE(t)}{\max\left[IE(t)\right]}. |  | (23) |

An event is classified as an EE if I​EN​(t)IE\_{N}(t) exceeds a threshold value. The threshold energy Et​hE\_{th} is determined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Et​h=Eμ+B​σ,E\_{th}=E\_{\mu}+B\sigma, |  | (24) |

where EμE\_{\mu} is the average energy, σ\sigma is the standard deviation, and BB is a constant parameter. For the present analysis, we set B=4B=4. To ensure that the detected points are not just random fluctuations, we present the Amplitude-Adjusted Fourier Transform to provide us with the statistical validation.

In this study, we applied Eq. ([21](https://arxiv.org/html/2512.00893v1#S3.E21 "In 3.2.1 Hilbert–Huang Transform (HHT) ‣ 3.2 Transformation methods ‣ 3 Methodology ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")) to compute H​(t,ω)H(t,\omega) for the combined IMFs. By locating the regions of maximum energy concentration in the H​(t,ω)H(t,\omega) spectrum, the occurrence time of an Extreme Event (EE) or sudden price change can be identified.
To quantify an EE, we evaluate the instantaneous energy of the combined IMFs using Eq. ([22](https://arxiv.org/html/2512.00893v1#S3.E22 "In 3.2.1 Hilbert–Huang Transform (HHT) ‣ 3.2 Transformation methods ‣ 3 Methodology ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")). In our case, this method allows us to pinpoint extreme post-election movements in BTC and ETH and link them to stress originating from stablecoin activity.

#### 3.2.2 Amplitude-Adjusted Fourier Transform (AAFT)

Surrogate data methods provide a statistical framework for testing whether observed structures in a time series reflect genuine nonlinear dynamics or arise from random linear processes [schreiber2000surrogate, lancaster2018surrogate]. Among the common algorithms for surrogate generation, the Fourier Transform (FT) method represents the earliest restricted implementation [theiler1992testing]. The FT algorithm proceeds as follows.

Given original time series data x​(t)x(t), we perform the Fourier transformation to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | X​(f)=A​(f)​ei​ϕ​(f)X(f)=A(f)e^{i\phi(f)} |  | (25) |

where A​(f)A(f) is the amplitude and ϕ​(f)\phi(f) is the phase. We then multiply by ei​φ​(f)e^{i\varphi(f)} to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | X~​(f)=A​(f)​ei​[ϕ​(f)+φ​(f)]\tilde{X}(f)=A(f)e^{i[\phi(f)+\varphi(f)]} |  | (26) |

where φ​(f)\varphi(f) is a random phase obeying independent uniform distribution on [0,2​π][0,2\pi]. Finally, the Fourier inverse transformation gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | x~​(t)=ℱ−1​{X~​(f)}=ℱ−1​{X​(f)​ei​φ​(f)}\tilde{x}(t)=\mathcal{F}^{-1}\{\tilde{X}(f)\}=\mathcal{F}^{-1}\{X(f)e^{i\varphi(f)}\} |  | (27) |

The resulting x~​(t)\tilde{x}(t) represents the surrogate data generated by the FT algorithm.

However, standard FT surrogates assume Gaussian distributions and fail to preserve the amplitude distribution of non-Gaussian real-world data. The Amplitude-Adjusted Fourier Transform (AAFT) method extends the FT approach to preserve both the power spectrum and the amplitude distribution [theiler1992testing, kugiumtzis1999test]. The AAFT algorithm proceeds through the following steps.

1. 1.

   Generate Gaussian white noise n​(t)n(t) with the same ordering (ranks) as the original data x​(t)x(t).
2. 2.

   Apply the FT algorithm to generate surrogate data n~​(t)\tilde{n}(t) from the Gaussian white noise.
3. 3.

   Reorder the original data x​(t)x(t) according to the rank order of n~​(t)\tilde{n}(t) to obtain the final surrogate data x~​(t)\tilde{x}(t).

The null hypothesis assumes that the observed time series is generated by a rescaled linear Gaussian process, i.e., a stationary linear Gaussian system passed through an invertible measurement function.

|  |  |  |  |
| --- | --- | --- | --- |
|  | sn=h​(xn),xn=∑i=1Mai​xn−i+∑i=0Nbi​ηn−i,s\_{n}=h(x\_{n}),\quad x\_{n}=\sum\_{i=1}^{M}a\_{i}x\_{n-i}+\sum\_{i=0}^{N}b\_{i}\eta\_{n-i}, |  | (28) |

where h​(⋅)h(\cdot) is the invertible measurement function, and ηn\eta\_{n} represents Gaussian white noise.

The AAFT method ensures that the surrogate datasets preserve the linear autocorrelation structure through the Fourier spectrum and retain the original amplitude distribution through rank-based remapping. This dual preservation makes AAFT particularly suitable for testing nonlinearity in financial and economic time series, which often exhibit non-Gaussian characteristics such as heavy tails and skewness.

In this study, we employ AAFT surrogate analysis with 1000 iterations to verify that the structural breaks identified by the BP test and the extreme events detected through the HS are not the result of noise or autocorrelation. This ensures that the observed changes reflect genuine structural shifts in the time series. Once the structural breaks are confirmed, we then proceed with structural vector autoregression to model their economic impact.

### 3.3 Structural Vector Autoregression (SVAR)

Structural vector autoregressive (SVAR) models are fundamental tools for empirical analysis in macroeconomics, finance, and related fields [kilian2017structural, lutkepohl2013introduction, sims1980macroeconomics]. Originally developed by Sims (1980) [sims1980macroeconomics], vector autoregressive (VAR) models have become a standard tool for analyzing dynamic relationships among economic variables and identifying structural shocks [stock2016dynamic]. In this study, we employ an SVAR framework to identify contemporaneous causal relationships and volatility spillovers between USDT and USDC stablecoin flows, with particular focus on changes induced by the 2024 U.S. Presidential election.

Let Yt=[y1,t,y2,t]′Y\_{t}=[y\_{1,t},y\_{2,t}]^{\prime} denote a 2-dimensional vector of stationary time series representing daily stablecoin transaction volumes. The reduced-form VAR(pp) model is written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt=c+∑i=1pΦi​Yt−i+ut,Y\_{t}=c+\sum\_{i=1}^{p}\Phi\_{i}Y\_{t-i}+u\_{t}, |  | (29) |

where, cc is a vector of constants, Φi\Phi\_{i} are 2×22\times 2 coefficient matrices for lag ii and utu\_{t} is a vector of serially uncorrelated reduced-form innovations with covariance matrix Σu=𝔼​[ut​ut′]\Sigma\_{u}=\mathbb{E}[u\_{t}u\_{t}^{\prime}].

#### 3.3.1 Identification of structural break

The reduced-form innovations utu\_{t} are linear combinations of mutually orthogonal structural shocks εt\varepsilon\_{t}, which satisfy 𝔼​[εt​εt′]=I\mathbb{E}[\varepsilon\_{t}\varepsilon\_{t}^{\prime}]=I. The structural form is

|  |  |  |  |
| --- | --- | --- | --- |
|  | A0​ut=εt⇒ut=A0−1​εt,A\_{0}u\_{t}=\varepsilon\_{t}\quad\Rightarrow\quad u\_{t}=A\_{0}^{-1}\varepsilon\_{t}, |  | (30) |

which implies the covariance relationship

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σu=A0−1​(A0−1)′.\Sigma\_{u}=A\_{0}^{-1}(A\_{0}^{-1})^{\prime}. |  | (31) |

To achieve identification, we impose a recursive (Cholesky) structure by restricting A0−1A\_{0}^{-1} to be lower triangular [bernanke2005measuring]. This allows unique recovery of the structural impact matrix via Cholesky decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σu=P​P′⇒A0−1^=P,\Sigma\_{u}=PP^{\prime}\quad\Rightarrow\quad\widehat{A\_{0}^{-1}}=P, |  | (32) |

where PP is the lower-triangular Cholesky factor. The variable ordering Yt=[USDCt,USDTt]′Y\_{t}=[\text{USDC}\_{t},\text{USDT}\_{t}]^{\prime} reflects the identifying assumption that structural shocks to USDC can affect USDT contemporaneously, while shocks to USDT affect USDC only with a one-period lag.

We address the non-stationarity of financial time series by applying a logarithmic transformation with first-differencing to USDC and USDT volumes. This dual transformation converts the series to stationary percentage changes while handling zero volumes through the log(1+x) formulation. For lag selection, we employ the Akaike Information Criterion (AIC). This approach ensures we capture meaningful dynamics without overfitting, providing a balanced representation of the temporal relationships between stablecoin flows. In our analysis, the SVAR model enables us to examine how shock transmission between USDC and USDT changes across regimes, providing evidence that the 2024 U.S. election produced a structural shift in their contemporaneous interactions.

#### 3.3.2 Wald test

To formally test for election-induced structural breaks, we implement a Wald test comparing parameter estimates obtained from the pre-election and post-election [wald1943tests]. Let θ^pre\hat{\theta}\_{\text{pre}} and θ^post\hat{\theta}\_{\text{post}} denote the vectors of estimated model parameters from the two periods. The parameter vector θ\theta consists of the VAR autoregressive coefficients, which capture the lagged interaction dynamics between USDC and USDT. Accordingly, θ^pre\hat{\theta}\_{\text{pre}} and θ^post\hat{\theta}\_{\text{post}} represent the stacked lag coefficients estimated separately for the pre-election and post-election periods.

We test the one-sided hypothesis that election-induced uncertainty increases volatility and spillover strength, which corresponds to an increase in the magnitude of the dynamic coefficients:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0:θ^post≤θ^pre,H1:θ^post>θ^pre.H\_{0}:\hat{\theta}\_{\text{post}}\leq\hat{\theta}\_{\text{pre}},\qquad H\_{1}:\hat{\theta}\_{\text{post}}>\hat{\theta}\_{\text{pre}}. |  | (33) |

The Wald statistic for testing this hypothesis is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | W=(θ^post−θ^pre)′​(Σ^pre+Σ^post)−1​(θ^post−θ^pre),W=(\hat{\theta}\_{\text{post}}-\hat{\theta}\_{\text{pre}})^{\prime}\left(\widehat{\Sigma}\_{\text{pre}}+\widehat{\Sigma}\_{\text{post}}\right)^{-1}(\hat{\theta}\_{\text{post}}-\hat{\theta}\_{\text{pre}}), |  | (34) |

where Σ^pre\widehat{\Sigma}\_{\text{pre}} and Σ^post\widehat{\Sigma}\_{\text{post}} denote the covariance matrices of the estimated parameters from the two time series subsamples. Under the null hypothesis of no structural change, the Wald statistic follows a χ2\chi^{2} distribution with degrees of freedom equal to the number of parameters being tested. A statistically significant Wald statistic leads to rejection of H0H\_{0}, indicating that the 2024 U.S. Presidential election induced a structural shift in the dynamic relationships between USDC and USDT transaction flows.

## 4 Results and Discussion

In this section, we discuss the results of our analysis examining how the 2024 U.S. Presidential election affected cryptocurrency market behavior through multiple analytical frameworks. Existing studies mainly depend on exchange-based prices and sentiment, leaving the transmission of political uncertainty through blockchain-based activity largely unexplored. To address this gap, we distinguish between human-driven (EOA–EOA) and automated (SC–SC) transactions on the Ethereum blockchain. Our findings show a clear temporal pattern. Human activity responds first in anticipation of election-related uncertainty, while algorithmic systems react later as market conditions evolve. This pattern indicates that human-driven blockchain behavior acts an early signal of emerging market turbulence, offering insights not captured by traditional market data.

### 4.1 Stationarity test

We conducted stationarity tests on the ERC-20 blockchain transaction and the trading data of USDT and USDC, along with the trading data of BTC and ETH, using the ADF test as described in Section [3.1.1](https://arxiv.org/html/2512.00893v1#S3.SS1.SSS1 "3.1.1 Augmented Dickey-Fuller test ‣ 3.1 Statistical tests ‣ 3 Methodology ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election"). For a time series to be stationary, the test statistic should be less than the 5% critical value, and the pp-value should fall below the 5% significance level, thereby rejecting the null hypothesis of a unit root. If the test statistic exceeds the 5% critical value and the pp-value is greater than the significance threshold, the null hypothesis cannot be rejected, indicating that the time series is non-stationary. In this study, the ADF test was applied to verify the preconditions required for SVAR and HS analyses. Table [3](https://arxiv.org/html/2512.00893v1#S4.T3 "Table 3 ‣ 4.1 Stationarity test ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election") presents the ADF test statistics, p-values, and 5% critical values for blockchain and trading datasets. The results show that all log-transformed series are non-stationary in levels but become stationary after first differencing. This confirms that they are integrated in order one, I​(1)I(1). The differenced series of USDT and USDC are therefore employed in the SVAR estimation, while for BTC and ETH, the non-stationary log-transformed trading series are retained in their original form, as HS analysis can directly accommodate non-stationary processes. This methodology ensures that the SVAR model operates on stationary time series, allowing us to accurately assess how election-induced shocks alter the regime dynamics between USDT and USDC, while the HS method utilizes the non-stationary time series of BTC and ETH prices to detect extreme events without violating its modelling assumptions. This framework provides a consistent basis for linking statistical changes in the data to real market behavior, illustrating how the 2024 U.S. election contributed to heightened volatility and accelerated spillovers across stablecoin flows and major cryptocurrency markets.

Table 3: The table reports Augmented Dickey–Fuller test statistics, p-values, and 5% critical values for blockchain and trading datasets. The null hypothesis of a unit root is rejected when the test statistic is less than the 5% critical value. All log-transformed series are non-stationary in levels but become stationary after first differencing, confirming that the series are integrated of order one, I​(1)I(1).

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Category | Asset | Transformation | Test Stat. | p-value | Critical (5%) | Result |
| Blockchain Data: EOA–EOA | | | | | | |
| USDT | EOA–EOA | Level | -1.7760 | 0.3925 | -2.864 | Non-stationary |
|  |  | First Difference | -5.9891 | 0.0000 | -2.864 | Stationary |
| USDC | EOA–EOA | Level | -1.6344 | 0.4652 | -2.864 | Non-stationary |
|  |  | First Difference | -8.6408 | 0.0000 | -2.864 | Stationary |
| Blockchain Data: SC–SC | | | | | | |
| USDT | SC–SC | Level | -1.9222 | 0.3217 | -2.864 | Non-stationary |
|  |  | First Difference | -6.4756 | 0.0000 | -2.864 | Stationary |
| USDC | SC–SC | Level | -0.3638 | 0.9160 | -2.864 | Non-stationary |
|  |  | First Difference | -7.2497 | 0.0000 | -2.864 | Stationary |
| Trading Data (Exchange) | | | | | | |
| USDT-USD | Volume | Level | -1.9571 | 0.3057 | -2.864 | Non-stationary |
|  |  | First Difference | -5.8145 | 0.0000 | -2.864 | Stationary |
| USDC-USD | Volume | Level | -2.6411 | 0.0848 | -2.864 | Non-stationary |
|  |  | First Difference | -6.4122 | 0.0000 | -2.864 | Stationary |
| BTC-USD | Close | Level | -1.2957 | 0.6312 | -2.864 | Non-stationary |
|  |  | First Difference | -20.2909 | 0.0000 | -2.864 | Stationary |
| ETH-USD | Close | Level | -1.8143 | 0.3734 | -2.864 | Non-stationary |
|  |  | First Difference | -19.3631 | 0.0000 | -2.864 | Stationary |
| \botrule |  |  |  |  |  |  |

### 4.2 Structural Break Analysis (SBA)

In this section, we employ the Bai-Perron test [bai1998estimating, bai2003computation] to detect the break dates in the time series. To ensure the identified breakpoints represent genuine structural changes rather than random fluctuations in autocorrelated time series, we complement the BP test with AAFT surrogate analysis. This rigorous validation method preserves both the linear autocorrelation structure and amplitude distribution of the original time series while randomizing phase information, providing a robust null hypothesis against which to test statistical significance.

The purpose of this test is to examine whether the 2024 U.S. Presidential election triggered structural changes in ERC-20 blockchain transaction data and in the trading data of two major stablecoins: USDT and USDC, as well as two major cryptocurrencies, BTC and ETH. We apply the BP test across three categories of transactions:

* •

  ERC-20 blockchain transactions between EOA–EOA.
* •

  ERC-20 blockchain transactions between SC–SC.
* •

  Trading data:Stablecoins: USDT and USDC and Cryptocurrencies: BTC and ETH.

Figures [1](https://arxiv.org/html/2512.00893v1#S4.F1 "Figure 1 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(a), [2](https://arxiv.org/html/2512.00893v1#S4.F2 "Figure 2 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(a), [3](https://arxiv.org/html/2512.00893v1#S4.F3 "Figure 3 ‣ 4.3.1 Structural breaks in stablecoin trading volumes ‣ 4.3 Hilbert Spectrum: extreme event in cryptocurrency ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election"), and [4](https://arxiv.org/html/2512.00893v1#S4.F4 "Figure 4 ‣ 4.4 Structural breaks in automated SC–SC transactions ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election") illustrate the SBA results, with structural breakpoints identified using the BP test. The brown line in these figures represents the 20-day rolling mean, showing the underlying trend. The dashed blue line marks the statistically significant structural breakpoints, while the dashed red line denotes the 2024 U.S. election day: 05-Nov-2024. Table [4](https://arxiv.org/html/2512.00893v1#S4.T4 "Table 4 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election") presents the identified structural break dates with the corresponding test statistics for both blockchain and trading data of stablecoins and cryptocurrencies. These structural breaks suggest that the U.S. election introduced a shock to the market, leading to adjustments in both blockchain activity and trading patterns. The timing of these changes reflects how the market participants responded to political uncertainty.

The transaction activity between EOA–EOA represents a direct measure of human-driven behavior on the blockchain. Unlike SC-SC transaction activity, which is run by the bots or automated algorithms, EOA–EOA interactions capture the real-time behavior of individual users, traders, and investors. As such, EOA–EOA transaction activity can be viewed as a behavioral signal, offering insights into how participants adjust their actions in response to election-induced events. In this section, we focus on the EOA–EOA blockchain transactions of USDT and USDC to examine whether election-induced events, i.e., the 2024 U.S. Presidential election, trigger structural changes in human-driven activity in the cryptocurrency ecosystem.

From Figs. [1](https://arxiv.org/html/2512.00893v1#S4.F1 "Figure 1 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(a) and [2](https://arxiv.org/html/2512.00893v1#S4.F2 "Figure 2 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(a), we see that the BP test identified a significant structural breakpoint for EOA–EOA transactions on 03 November 2024, just two days before the U.S. Presidential election, for both USDT and USDC in human-driven EOA-EOA transactions. To validate the statistical significance of the identified breakpoints, we employed two Bai-Perron SupF tests and AAFT surrogate analysis. First, we applied the Bai-Perron SupF test for detecting unknown break dates, where the null hypothesis assumes no structural break. The results reported in Table [4](https://arxiv.org/html/2512.00893v1#S4.T4 "Table 4 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election") strongly reject the null hypothesis for both stablecoins, with SupF statistics of 34.63 for USDC and 76.82 for USDT, both exceeding conventional significance thresholds. To further validate the robustness of these findings against autocorrelated noise, we conducted AAFT surrogate analysis. The results show p-values < 0.001 for both tokens, indicating that the probability of observing similar structural breaks within a ±3-day window by random chance is extremely low. This dual validation confirms that the identified breakpoints are both statistically significant and non-trivial. These results provide clear and robust evidence that both ERC-20 blockchain transaction USDT and USDC data experienced significant structural breaks around early November 2024, coinciding with the period just before the 2024 U.S. Presidential election. The consistent evidence confirms a robust structural break for both stablecoins, ruling out random fluctuations and indicating a significant shift in market behavior.

![Refer to caption](x1.png)


Figure 1: 
The figure illustrates the structural breakpoint, Hilbert spectrum, and instantaneous energy for blockchain USDT BTC trading data. (a) Logarithm of the daily trading volume in USD, log⁡(VUSD)\log(V\_{\mathrm{USD}}). The brown line represents the rolling mean of the trading volume, the red dashed line indicates the U.S. Presidential election Day 2024, and the blue dashed line marks the structural breakpoint. (b) Hilbert Spectrum for BTC, showing the instantaneous frequency (ω\omega) over time. A period of high energy is observed during the U.S. Presidential election. (c) Normalized instantaneous energy for BTC. A sudden energy surge occurs after the election period begins, peaking on November 10, 2024. This peak exceeds the statistical threshold energy level, defined as Eth=Eμ+4​σE\_{\mathrm{th}}=E\_{\mu}+4\sigma.

![Refer to caption](x2.png)


Figure 2: 
The figure illustrates the structural breakpoint, Hilbert spectrum, and instantaneous energy for blockchain USDC and ETH trading data. (a) Logarithm of the daily trading volume in USD, log⁡(VUSD)\log(V\_{\mathrm{USD}}). The brown line represents the rolling mean of the trading volume, the red dashed line indicates the U.S. Presidential election Day 2024, and the blue dashed line marks the structural breakpoint. (b) Hilbert Spectrum for ETH, showing the instantaneous frequency (ω\omega) over time. A period of high energy is observed during the U.S. Presidential election. (c) Normalized instantaneous energy for ETH. A sudden energy surge occurs after the election period begins, peaking on November 7, 2024. This peak exceeds the statistical threshold energy level, defined as Eth=Eμ+4​σE\_{\mathrm{th}}=E\_{\mu}+4\sigma.

The timing of the identified break date using the BP test is critical, as it indicates a shift in user behavior in anticipation of the election outcome, rather than as a reaction to the announced results. The identified structural break in human-driven, EOA-to-EOA transactions suggests a fundamental change in the dynamics of stablecoin activity. This shift likely reflects a period of precautionary reallocation, wherein investors moved capital from more volatile cryptocurrencies into stablecoins as a hedge against potential election-induced uncertainty. This pattern aligns with established safe-haven behavior during periods of political stress [wei2018impact, bianchi2020stablecoins], where market participants enter a "wait-and-watch" phase and reduce exposure to high-risk assets. The pronounced response in human-driven activity further suggests that election-induced uncertainty exerted direct behavioral influence on individual participants, who typically demonstrate greater sensitivity to political and macroeconomic shocks.

Table 4: Structural break test results for stablecoins and major cryptocurrencies. All breaks identified by the Bai–Perron SupF test show significant p-values, providing strong evidence against the null hypothesis of no structural break. AAFT surrogate testing (1000 iterations) confirms these breaks are non-trivial. ∗∗∗ denotes statistical significance at the 0.001 level.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Asset | Break Date | SupF Statistic | AAFT p-value | Comment |
| Blockchain Data: EOA–EOA | | | | |
| USDC | 2024-11-03 | 34.63∗∗∗ | <0.001 | Early human-driven response before election day. |
| USDT | 2024-11-03 | 76.82∗∗∗ | <0.001 | Early human-driven response before election day. |
| Trading Data (Exchange) | | | | |
| USDC-USD | 2024-11-05 | 79.04∗∗∗ | <0.001 | Immediate market reaction on election day. |
| USDT-USD | 2024-11-05 | 315.23∗∗∗ | <0.001 | Immediate market reaction on election day. |
| BTC-USD | 2024-11-09 | 3049.02∗∗∗ | <0.001 | Spillover to broader crypto markets after election. |
| ETH-USD | 2024-11-06 | 137.60∗∗∗ | <0.001 | Spillover to broader crypto markets after election. |
| Blockchain Data: SC–SC | | | | |
| USDC | 2025-01-02 | 266.45∗∗∗ | <0.001 | Delayed adjustment in automated contract activity. |
| USDT | 2025-01-16 | 57.00∗∗∗ | <0.001 | Delayed adjustment in automated contract activity. |
| \botrule |  |  |  |  |

### 4.3 Hilbert Spectrum: extreme event in cryptocurrency

The election-induced anticipatory shift in Human-driven EOA-EOA stablecoin blockchain transactions raises the question of whether it was subsequently followed by notable volatility in the broader cryptocurrency market. To investigate this, we employ the HHT, based on EMD, to assess whether the structural break observed in EOA–EOA transactions signals impending shifts in broader cryptocurrency market dynamics. This method provides a time–frequency representation of price behavior, enabling the detection of sudden changes in the cryptocurrency market during the election period. The HS, H​(t,ω)H(t,\omega) is estimated by averaging across all IMFs derived from the closing price time series of BTC and ETH, as described in Section [3.2.1](https://arxiv.org/html/2512.00893v1#S3.SS2.SSS1 "3.2.1 Hilbert–Huang Transform (HHT) ‣ 3.2 Transformation methods ‣ 3 Methodology ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election"). Equal weighting of IMFs ensures that the final spectrum captures the overall energy distribution without bias toward any single component.

Figures [1](https://arxiv.org/html/2512.00893v1#S4.F1 "Figure 1 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(b) and [2](https://arxiv.org/html/2512.00893v1#S4.F2 "Figure 2 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(b) display the HS for BTC and ETH closing prices. Both reveal concentrated regions of high instantaneous energy, coinciding with the U.S. Presidential election. These intense energy patches signify abrupt market adjustments and increased volatility, corresponding to a positive extreme event as BTC and ETH prices rose sharply during this period. The normalized instantaneous energy I​EN​(t)IE\_{N}(t) plots in Figures [1](https://arxiv.org/html/2512.00893v1#S4.F1 "Figure 1 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(c) and [2](https://arxiv.org/html/2512.00893v1#S4.F2 "Figure 2 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(c) further support this interpretation. The peak in I​EN​(t)IE\_{N}(t) exceeds the statistical threshold Et​h=Eμ+4​σE\_{th}=E\_{\mu}+4\sigma, confirming that the election week triggered statistically significant extreme events. Prior studies identify 4​σ4\sigma exceedance as a hallmark of extreme events, and its occurrence here directly links the volatility burst to the election shock.
Along with the HS, the BP test detects structural breaks on 06-Nov-2024 for ETH and 09-Nov-2024 for BTC as present in Table [4](https://arxiv.org/html/2512.00893v1#S4.T4 "Table 4 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election"). These breakpoints align with the concentrated energy regions in the Hilbert spectra, reinforcing evidence of major structural adjustments in response to election-induced uncertainty. Overall, the sentiment shift captured by stablecoin blockchain activity on 03 November preceded the election-driven volatility, which subsequently manifested as structural breaks and positive extreme events in BTC and ETH, providing strong evidence of the predictive value of stablecoin flows for market-wide shocks.

#### 4.3.1 Structural breaks in stablecoin trading volumes

![Refer to caption](x3.png)


Figure 3: Structural break analysis of stablecoin trading volumes. The BP test detects significant structural breaks in (a) USDT and (b) USDC trading volumes on 5 November 2024, coinciding with the U.S. Presidential election. The red dashed line marks the election date, and the blue line would indicate the break date; however, because the two coincide, only the red dashed line is visible. These synchronized breaks confirm that the blockchain anticipatory signal was followed by a broad market adjustment in centralized exchange activity.

The anticipatory shift in human-driven, EOA–EOA stablecoin transactions identified on 03-Nov-2024 served as a leading indicator. We now examine whether this blockchain signal was followed by a corresponding structural break in the broader market, as reflected in the trading volume on centralized exchanges (CEX). Figures [3](https://arxiv.org/html/2512.00893v1#S4.F3 "Figure 3 ‣ 4.3.1 Structural breaks in stablecoin trading volumes ‣ 4.3 Hilbert Spectrum: extreme event in cryptocurrency ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(a) and [3](https://arxiv.org/html/2512.00893v1#S4.F3 "Figure 3 ‣ 4.3.1 Structural breaks in stablecoin trading volumes ‣ 4.3 Hilbert Spectrum: extreme event in cryptocurrency ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(b) identified a structural break in the trading volume for both the USDT and USDC on 05-Nov-2024, the same day of the U.S. Presidential election. As shown in Table [4](https://arxiv.org/html/2512.00893v1#S4.T4 "Table 4 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election"), these breakpoints are statistically significant, with SupF statistics of 79.04 for USDC and 315.23 for USDT. The robustness of these findings is further confirmed by AAFT surrogate analysis, which gives p-values of <0.001<0.001 for both stablecoins, indicating that the identified breaks are statistically significant. In this analysis, we use trading volume rather than USD price because stablecoins are pegged to the dollar; thus, volume is a more meaningful indicator of shifts in market activity and capital flows.

The sequence of structural breaks reveals an important pattern. The break in EOA–EOA transactions on 03-Nov-2024 indicates a precautionary shift, with investors moving capital to blockchain, likely to hedge against election uncertainty. This blockchain activity was the first measurable sign of changing user behavior. The subsequent break in CEX trading volume on 05-Nov-2024 marks the point of market-wide realization, where the unfolding election results triggered a surge in trading activity. Critically, this volatility subsequently spilled over into major cryptocurrencies. The BP test detects significant structural breaks on 06-Nov-2024 for ETH and 09-Nov-2024 for BTC, aligning with the period of intense market adjustment identified by the HS. This sequential pattern from a blockchain behavioral shift, to a surge in stablecoin trading and finally to structural breaks in major cryptocurrencies, demonstrates how election-induced anticipation culminated in a broad market reaction. The consistent sequence across stablecoins and major cryptocurrencies confirms the 2024 U.S. election was a significant structural shock and underscores the value of blockchain data as a leading indicator of sentiment. Together, these results further support the role of human-driven blockchain activity as an effective early warning system, revealing emerging market stress days before it becomes visible in exchange trading or price dynamics.

### 4.4 Structural breaks in automated SC–SC transactions

In this section, we discuss how the automated, code-driven SC-SC blockchain transaction responded to the election-induced effect different way than a human-driven one. It is essential to distinguish the nature of these transactions. SC–SC interactions represent automated, pre-programmed operations executed by bots without direct human intervention, whereas EOA–EOA transactions are initiated by human users from their personal wallets. As shown in Figures [4](https://arxiv.org/html/2512.00893v1#S4.F4 "Figure 4 ‣ 4.4 Structural breaks in automated SC–SC transactions ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(a) and [4](https://arxiv.org/html/2512.00893v1#S4.F4 "Figure 4 ‣ 4.4 Structural breaks in automated SC–SC transactions ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election")(b), the BP test identified that the structural breaks for USDT and USDC occurred months after the election, on 16-Jan-2025 and 02-Jan-2025, respectively. These breaks are statistically robust, with high SupF statistics of 57.00 for USDT and 266.45 for USDC. The identified break date is also confirmed by AAFT surrogate testing with <0.001<0.001, as detailed in Table [4](https://arxiv.org/html/2512.00893v1#S4.T4 "Table 4 ‣ 4.2 Structural Break Analysis (SBA) ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election"). This delayed response shows a clear difference from the immediate, precautionary shift seen in human-driven (EOA–EOA) transactions just before the election. This timing difference indicates a key finding that the 2024 U.S. election was primarily a behavioral shock that immediately affected human participants, but only later triggered adjustments in automated systems. The January 2025 breaks likely reflect algorithmic recalibrations to the new, post-election market environment, such as updated trading strategies or protocol changes, once the new market conditions have stabilized. This confirms that bot-driven SC–SC activity is less sensitive to sudden exogenous political events in real-time, instead reacting to more established trends. These results clearly demonstrate the fundamental difference between human-driven and code-driven activity, as humans react in real time and exhibit herding behaviour that cannot be replicated by automated SC. This result strengthens the importance of our earlier findings. It shows that human-driven EOA–EOA blockchain activity is a unique and valuable indicator, capturing immediate sentiment shifts that precede both exchange trading volumes and the subsequent adjustments of automated systems.

![Refer to caption](x4.png)


Figure 4: Structural Break Analysis of Automated SC–SC Stablecoin Transactions. The Bai–Perron test identifies significant post-election structural breaks in automated SC–SC transaction volumes for (a) USDT on 16 January 2025, and (b) USDC on 2 January 2025. The red dashed line marks the 2024 U.S. election date, while the blue line indicates the respective break dates. These delayed adjustments indicate that bot-driven systems responded only after market stabilization, contrasting with the immediate, human-driven shifts observed before the election.

### 4.5 Structural VAR-based analysis

In this section, we study whether the 2024 U.S. Presidential election triggered a regime shift in stablecoin markets by analyzing volatility spillovers between USDT and USDC. To examine this, we employ SVAR analysis to investigate how election-induced uncertainty affected the dynamic relationships between stablecoins. This framework enables us to move beyond simple correlations to assess both the magnitude and direction of causal volatility spillovers between USDT and USDC. To identify the structural model, we utilize a Cholesky decomposition [pourahmadi2007cholesky], which requires imposing a specific ordering on the variables to orthogonalize the shocks. We present results under two distinct identification schemes to test the robustness of the spillover dynamics and to understand the sensitivity of our conclusions to different assumptions about market leadership. The analysis is conducted using both blockchain transaction data, EOA-EOA transactions, and exchange-based trading volume data. This ensures that it captures spillover dynamics across different market segments. To assess changes over time, we examine the SVAR across three periods: the full sample, the pre-election period defined as up to 04-Nov-2024, and the post-election period defined as from 05-Nov-2024 onward. This division allows for a direct comparison of relationship dynamics before and after the election event.

Table 5: Wald test results for structural breaks in blockchain and trading data. The high test statistics (p < 0.0001) provide strong evidence of regime change, with trading data displaying substantially larger breaks (Wald = 5381.56) than the blockchain transaction series.

|  |  |  |  |
| --- | --- | --- | --- |
| Identification Ordering | Wald Statistic | P-value | Decision |
| Blockchain Data (EOA–EOA) | | | |
| USDC-First | 295.21 | <<0.0001 | Significant regime change. |
| USDT-First | 138.78 | <<0.0001 | Significant regime change. |
| Trading Data | | | |
| USDT-First | 876.24 | <<0.0001 | Significant regime change. |
| USDC-First | 5381.56 | <<0.0001 | Significant regime change. |
| \botrule |  |  |  |




Table 6: Impact matrices for blockchain and trading data under alternative identification schemes. All values are reported in their original 0-1 scale and are not multiplied by 100. The post-election period shows a 28–48% increase in volatility spillovers, with USDT emerging as the dominant transmission channel of election-induced stress across both blockchain and exchange markets.

|  |  |  |  |
| --- | --- | --- | --- |
| Response | Full Sample | Pre-Election | Post-Election |
| Blockchain Data (EOA–EOA): USDC Precedes USDT | | | |
| USDC to USDC Shock | 0.3441 | 0.3232 | 0.4410 |
| USDT to USDC Shock | 0.1881 | 0.1620 | 0.2399 |
| USDT to USDT Shock | 0.1952 | 0.1645 | 0.2334 |
| Blockchain Data (EOA–EOA): USDT Precedes USDC | | | |
| USDT to USDT Shock | 0.2711 | 0.2309 | 0.3347 |
| USDC to USDT Shock | 0.2388 | 0.2268 | 0.3161 |
| USDC to USDC Shock | 0.2478 | 0.2303 | 0.3075 |
| Trading Data: USDT Precedes USDC | | | |
| USDT to USDT Shock | 0.2474 | 0.2175 | 0.2782 |
| USDC to USDT Shock | 0.2632 | 0.2373 | 0.3077 |
| USDC to USDC Shock | 0.1042 | 0.0969 | 0.1133 |
| Trading Data: USDC Precedes USDT | | | |
| USDC to USDC Shock | 0.2831 | 0.2564 | 0.3279 |
| USDT to USDC Shock | 0.2300 | 0.2013 | 0.2611 |
| USDT to USDT Shock | 0.0911 | 0.0822 | 0.0962 |
| \botrule |  |  |  |

Table [6](https://arxiv.org/html/2512.00893v1#S4.T6 "Table 6 ‣ 4.5 Structural VAR-based analysis ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election") presents the estimated impact matrices. The ordering assumption implies that a variable placed first can contemporaneously affect the second, but the second can only affect the first with a lag. The results show that all elements increase in the post-election period for both blockchain and trading data and under both identification orderings. This indicates higher volatility and stronger spillover effects. A closer look at the values reveals that USDT’s responses are particularly notable. For instance, in blockchain data under the USDT-first ordering, the USDT own-shock effect jumps from 0.2309 to 0.3347, while in trading data, it rises from 0.2175 to 0.2782. Cross-effects are also stronger when USDT is the leading variable, for example, USDC to USDT shocks in trading grow from 0.2373 to 0.3077. The own-shock effects rise by 28–45% in the post-election period compared with the pre-election period, suggesting a significant increase in intrinsic volatility following the election. The cross-stablecoin spillover effects also rise sharply in the post-election period, with the contemporaneous spillover parameters increasing by 39–48% across both data sources and identification orderings. These results suggest that USDT plays a disproportionately important role in driving post-election volatility. This pattern aligns with the fact that USDT exhibits higher market capitalization and deeper liquidity as compared to USDC. The findings, therefore, indicate that election-induced stress was transmitted more strongly through USDT, amplifying its role as the primary channel of spillovers in stablecoin markets. Table [5](https://arxiv.org/html/2512.00893v1#S4.T5 "Table 5 ‣ 4.5 Structural VAR-based analysis ‣ 4 Results and Discussion ‣ Early-Warning Signals of Political Risk in Stablecoin Markets: Human and Algorithmic Behavior Around the 2024 U.S. Election") reports the Wald test results for both blockchain EOA–EOA and trading data. The results show large and highly significant statistics with pp < 0.0001, confirming clear structural breaks in blockchain data and even stronger shifts in trading data, suggesting that election-induced changes were more pronounced in exchange-based activity. The SVAR results confirm a clear regime change in stablecoin dynamics following the 2024 U.S. Presidential election, characterized by amplified volatility and deeper interconnectedness between USDT and USDC after the election. Together with the structural break tests, these findings provide strong evidence that the 2024 U.S. Presidential election triggered fundamental regime shifts in the cryptocurrency ecosystem. They indicate that political uncertainty can temporarily alter the transmission of volatility, tighten linkages between stablecoins, and accelerate the spread of shocks across markets. These patterns also suggest that shifts in blockchain activity and trading responses form a coordinated adjustment process during major political events.

## 5 Conclusion and Discussion

This study establishes that human-driven blockchain transaction activity serves as an early warning system for financial market stress during periods of political uncertainty. The 2024 U.S. Presidential election provided a clear natural experiment that revealed a sequential pattern of reactions across the cryptocurrency ecosystem. Our analysis demonstrates that human-driven activity, reflected in EOA–EOA stablecoin blockchain transfers, was the first to react to political uncertainty, with structural breaks identified on November 3, 2024, two days before the election. This signals a precautionary shift into stablecoins ahead of anticipated volatility due to the election. These early human-led adjustments, confirmed through Amplitude-Adjusted Fourier Transform surrogate testing with p < 0.001, emerged before any breaks appeared in exchange-based trading activity or automated SC–SC transactions. This sequence shows that human-driven blockchain behavior provides a clear early warning signal, preceding reactions observed in centralized markets and algorithmic systems. The subsequent structural breaks in exchange-based trading volumes on election day (November 5) and the extreme price movements in BTC and ETH identified through Hilbert Spectrum analysis, with both exceeding the Et​h=Eμ+4​σE\_{th}=E\_{\mu}+4\sigma extreme event threshold, confirm that these initial blockchain early signals accurately anticipated broader market turbulence. A clear behavioral divergence was observed between human and algorithmic responses to the political stress. Human-driven activity adjusted rapidly to pre-election uncertainty, whereas automated SC–SC transactions exhibited delayed responses, with structural breaks appearing only in January 2025. This pattern suggests that human sentiment and intentional decisions dominate short-term adjustments, while algorithmic systems adapt more gradually once new equilibrium conditions emerge. Structural vector autoregression analysis confirms a post-election regime shift, with volatility and spillover effects between USDT and USDC rising by 28–48% relative to the pre-election period. Wald test results with p < 0.0001 verify the statistical significance of this shift, underscoring how political events can reshape stablecoin dynamics.

Overall, these findings demonstrate that distinguishing between human and algorithmic blockchain behavior provides an early warning framework for market stress. Human-driven EOA–EOA activity reacts first to political uncertainty and offers advanced signals that appear before changes in exchange trading or automated smart contract activity. This early response improves our understanding of how political shocks transmit through decentralized markets and reveals a clear sequence in behavioral adjustments. These findings also have important practical implications for investors, risk managers, and policymakers who must make decisions during periods of political uncertainty in cryptocurrency markets. For investors, early human-driven signals provide clear, data-backed guidance that can help them adjust their portfolios before volatility fully unfolds. For risk managers, integrating real-time blockchain activity strengthens short-term stress monitoring and improves the accuracy of market risk models, and policymakers can gain clearer insights into how political events influence stablecoin flows and financial stability.

Our analysis is limited to ERC-20 blockchain transactions and does not capture stablecoin activity occurring on other blockchain platforms. In the future, we plan to extend this analysis across multiple blockchain ecosystems, incorporate machine learning techniques for regime detection, and examine whether similar early warning patterns emerge during other geopolitical or macroeconomic events.

\bmhead

Acknowledgements
We acknowledge NIT Sikkim for providing doctoral fellowships to Kundan Mukhia, Salam Rbindrajit Luwang and Buddha Nath Sharma.