---
authors:
- Nicola Borri
- Yukun Liu
- Aleh Tsyvinski
- Xi Wu
doc_id: arxiv:2510.14435v1
family_id: arxiv:2510.14435
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Cryptocurrency as an Investable Asset Class: Coming of Age'
url_abs: http://arxiv.org/abs/2510.14435v1
url_html: https://arxiv.org/html/2510.14435v1
venue: arXiv q-fin
version: 1
year: 2025
---


Nicola Borri, Yukun Liu, Aleh Tsyvinski, and Xi Wu
Nicola Borri is with LUISS University, Rome. Yukun Liu is with the
University of Rochester, Simon Business School. Aleh Tsyvinski is
with Yale University. Xi Wu is with University of California, Berkeley.

(October 2025)

###### Abstract

Cryptocurrencies are coming of age. We organize empirical regularities into ten stylized facts and analyze cryptocurrency through the lens of empirical asset pricing. We find important similarities with traditional markets—risk-adjusted performance is broadly comparable, and the cross-section of returns can be summarized by a small set of factors. However, cryptocurrency also has its own distinct character: jumps are frequent and large, and blockchain information helps drive prices. This common set of facts provides evidence that cryptocurrency is emerging as an investable asset class.

## 1 INTRODUCTION

This survey establishes ten key empirical regularities of cryptocurrencies motivated by the view that cryptocurrency is an asset and thus can and should be analyzed from the asset-pricing point of view and, more specifically, from the cryptocurrency asset pricing view. Although the literature is relatively young—cryptocurrencies trace back to Nakamoto ([2008](https://arxiv.org/html/2510.14435v1#bib.bib118))’s short paper on Bitcoin—it is now at the point of maturity where it is useful to establish a core of stylized facts in cryptocurrency markets that can be used for both empirical and theoretical work. This common set of facts also provides emerging evidence that cryptocurrency is becoming an investable asset class.

Money has long been a central topic in economics—for example, see classic contributions of Tobin ([1965](https://arxiv.org/html/2510.14435v1#bib.bib137)) and Friedman ([1968](https://arxiv.org/html/2510.14435v1#bib.bib65)) to more recent advances. A large literature studied why money exists and how it functions—the role of money in economies with spatially separated agents (Townsend [1980](https://arxiv.org/html/2510.14435v1#bib.bib139)), the coexistence of different types of money under different institutional restrictions (Wallace [1983](https://arxiv.org/html/2510.14435v1#bib.bib145)), search-based models (Kiyotaki & Wright, [1989](https://arxiv.org/html/2510.14435v1#bib.bib90); Trejos & Wright, [1995](https://arxiv.org/html/2510.14435v1#bib.bib141); Shi, [1995](https://arxiv.org/html/2510.14435v1#bib.bib131); Lagos & Wright, [2005](https://arxiv.org/html/2510.14435v1#bib.bib97)), mechanism-design approaches (Green & Zhou, [1998](https://arxiv.org/html/2510.14435v1#bib.bib72)), the “money-as-memory” view (Kocherlakota, [1998](https://arxiv.org/html/2510.14435v1#bib.bib91)), commodity and token money (Sargent & Wallace, [1983](https://arxiv.org/html/2510.14435v1#bib.bib125); Sargent, [2019](https://arxiv.org/html/2510.14435v1#bib.bib124)), competing currencies (Kareken & Wallace, [1981](https://arxiv.org/html/2510.14435v1#bib.bib88)), and the money-like safe assets (Gorton & Pennacchi [1990](https://arxiv.org/html/2510.14435v1#bib.bib71); Holmström & Tirole [1998](https://arxiv.org/html/2510.14435v1#bib.bib80)).

When the paper of Nakamoto ([2008](https://arxiv.org/html/2510.14435v1#bib.bib118)) introduced a permissionless blockchain that provides public record-keeping without a central authority, financed and governed by a native token, the canonical literature on money had reached a degree of maturity. Permissionless ledgers can be viewed as technologies that supply public memory, with token systems financing and governing that record—keeping, and providing histories, communication, and enforcement mechanisms that are required for credit. With the rise of cryptocurrencies, these new ideas began to emerge primarily from practice more than theory and reopened classic monetary questions—record-keeping, commitment, enforcement—but now viewed from the point of view of blockchain economics.

When practice advances faster than theory, it is natural to start asking empirical questions that can themselves later be used to shape theory. The paper of Liu & Tsyvinski ([2021](https://arxiv.org/html/2510.14435v1#bib.bib105)) is the first comprehensive analysis of cryptocurrency through the lens of empirical finance and asset pricing. A sizable literature uses an asset pricing lens to study risk exposures, cross-sectional return patterns, cash-flow-like primitives, market microstructure, and limits to arbitrage (see, for example, Makarov & Schoar [2020](https://arxiv.org/html/2510.14435v1#bib.bib111), Liu et al. [2022](https://arxiv.org/html/2510.14435v1#bib.bib107), Alvarez et al. [2023](https://arxiv.org/html/2510.14435v1#bib.bib8), Sockin & Xiong [2023a](https://arxiv.org/html/2510.14435v1#bib.bib135), von Luckner et al. [2023](https://arxiv.org/html/2510.14435v1#bib.bib144), Kogan et al. [2024](https://arxiv.org/html/2510.14435v1#bib.bib93)).

Many have viewed cryptocurrencies—and, not unjustifiably, many still view them—as hype, speculation, or fraud. When cryptocurrency first appeared it was easy to dismiss it: money engineered by an unknown author and operating outside of the traditional financial system.111Foley et al. ([2019](https://arxiv.org/html/2510.14435v1#bib.bib64)) and Griffin & Shams ([2020](https://arxiv.org/html/2510.14435v1#bib.bib73)) for early analyses documenting how cryptocurrency mainly enabled illicit activity and alleged market manipulations. It is worth noting that several important financial innovations, such as the limited-liability company and mortgage-backed securities, were also initially met with distrust before becoming part of standard finance (see, for example, Hilt [2014](https://arxiv.org/html/2510.14435v1#bib.bib79) and Lewis [2010](https://arxiv.org/html/2510.14435v1#bib.bib100)), as institutions and legal frameworks evolved to manage their risks and as research deepened understanding of these innovations.

Since then research has evolved toward a much broader agenda that increasingly resembles research on any other asset class—the market structure (Abadi & Brunnermeier [2018](https://arxiv.org/html/2510.14435v1#bib.bib1), Leshno & Strack [2020](https://arxiv.org/html/2510.14435v1#bib.bib99), Biais et al. [2019](https://arxiv.org/html/2510.14435v1#bib.bib25), Kogan et al. [2022](https://arxiv.org/html/2510.14435v1#bib.bib92), Brunnermeier et al. [2019](https://arxiv.org/html/2510.14435v1#bib.bib41), Benigno et al. [2022](https://arxiv.org/html/2510.14435v1#bib.bib24), Capponi et al. [2025](https://arxiv.org/html/2510.14435v1#bib.bib42), Jermann & Xiang [2025](https://arxiv.org/html/2510.14435v1#bib.bib86)), regulation (Cong & He [2019](https://arxiv.org/html/2510.14435v1#bib.bib47),Townsend [2020](https://arxiv.org/html/2510.14435v1#bib.bib140), Auer et al. [2025](https://arxiv.org/html/2510.14435v1#bib.bib16)), digital asset pricing and valuation (Athey et al. [2016](https://arxiv.org/html/2510.14435v1#bib.bib14), Cong et al. [2021b](https://arxiv.org/html/2510.14435v1#bib.bib49), Biais et al. [2023](https://arxiv.org/html/2510.14435v1#bib.bib26)), transaction costs (Easley et al. [2019](https://arxiv.org/html/2510.14435v1#bib.bib57), Cong et al. [2021a](https://arxiv.org/html/2510.14435v1#bib.bib48), Basu et al. [2023](https://arxiv.org/html/2510.14435v1#bib.bib21)), central bank money (Auer et al. [2022](https://arxiv.org/html/2510.14435v1#bib.bib15), Whited et al. [2023](https://arxiv.org/html/2510.14435v1#bib.bib148), Schilling et al. [2024](https://arxiv.org/html/2510.14435v1#bib.bib127)), securitization (Cong et al. [2022](https://arxiv.org/html/2510.14435v1#bib.bib50), Sockin & Xiong [2023a](https://arxiv.org/html/2510.14435v1#bib.bib135), Rogoff & You [2023](https://arxiv.org/html/2510.14435v1#bib.bib122), Goldstein et al. [2024](https://arxiv.org/html/2510.14435v1#bib.bib69)), safe assets (Ma et al. [2025](https://arxiv.org/html/2510.14435v1#bib.bib110)), international capital flow (von Luckner et al. [2023](https://arxiv.org/html/2510.14435v1#bib.bib144)), blockchain technologies and the traditional financial system (Fernández-Villaverde & Sanches [2018](https://arxiv.org/html/2510.14435v1#bib.bib62)) and market microstructure (Easley et al. [2024](https://arxiv.org/html/2510.14435v1#bib.bib58)).

We synthesize the rapidly growing empirical finance of cryptocurrencies into a set of ten stylized empirical regularities that show how cryptocurrencies behave as assets, how their markets function, and what distinguishes them from traditional asset classes. These empirical facts are also useful to evaluate and revisit both the classic and the new theories of money.

Ten Facts in Cryptocurrency Asset Pricing and Empirical Finance. Facts 1 and 2 overview the core asset-pricing characteristics of cryptocurrency markets—the risk-return trade-off and the diversification benefits. Facts 3 and 4 discuss the structure of returns in cryptocurrency—factors, or “smart-beta”, which explain the cross-section of returns and optimal portfolio shares. Fact 5 shows the importance of large, discrete price movements—jumps—and the importance of extreme events for understanding cryptocurrency risk and valuation. Fact 6 shows that the higher-order terms of a parsimonious four-factor model account for a large fraction of the cross-section of returns and provide a “glass box” alternative to the “black box” neural net models with interpretable economic factor structure. Fact 7 shows the importance of the blockchain structure and network economy phenomena for cryptocurrency prices—on-chain user adoption influences cryptocurrency returns. Facts 8 documents large and persistent market inefficiencies due to frictions that limit arbitrage, and discuss risks for arbitrageurs. Fact 9 is about the cryptocurrency futures market and funding premia, and their evolution. Finally, Fact 10 is about the importance of regulation, disclosure, and transparency. In sum, these ten facts can be viewed as providing evidence that cryptocurrency, and more broadly, digital assets are coming of age as an emerging investable asset class.

## 2 DATA

The empirical analysis is based on the most recent data aggregated from multiple sources.

First, we collect comprehensive price data on all cryptocurrencies from CoinGecko.com, covering both active and inactive coins between December 31, 2013, and September 6, 2025. The sample includes 18,622 coins listed on CoinGecko at the end of the period, as well as 29,230 inactive coins that have since been delisted but for which historical data are available. Including inactive coins allows us to avoid survivorship bias. We exclude stablecoins because they are designed to track the value of a currency, a basket of fiat currencies, or another reference asset. We also exclude wrapped tokens (such as Wrapped Ether) as they are essentially replicas of existing coins on different blockchains. Furthermore, we drop daily observations with missing or non-positive values for price, market capitalization, or trading volume. We also exclude all coins with fewer than 30 daily observations. The final dataset comprises 16,468 unique coins and approximately 9.5 million records.

Second, for the construction of the crypto carry strategy of Schmeling et al. ([2023](https://arxiv.org/html/2510.14435v1#bib.bib128)), we collect perpetual futures prices, funding rates and spot index prices for Bitcoin at the 8-hour frequency from Binance for the period August 1, 2020 to May 31, 2025. The data on new addresses are from Liu et al. ([2021](https://arxiv.org/html/2510.14435v1#bib.bib106)). Moreover, for the construction of the crypto arbitrage strategy of Borri & Shakhnov ([2022](https://arxiv.org/html/2510.14435v1#bib.bib37)), we collect Bitcoin prices against 510 pairs from 165 different centralized exchanges quoted against 49 fiat currencies from CryptoCompare.com for the period December 31, 2013 to January 30, 2025. Furthermore, for estimation of jumps in cryptocurrency we collect tick-level transaction data for Bitcoin and Ethereum from Kraken.com and measures of realized variance constructed from tick-level data for the components of the Dow Jones Industrial Average Index from the CaPiRe dataset, for the period January 1, 2015 to March 31, 2025.222Finally, we obtain price indices for the U.S. stock market, U.S. corporate and government bonds, a broad commodity index, gold, the U.S. dollar index, the Dow Jones US Real Estate Index, the U.S. constant maturity 10-year nominal and real bond yields from Bloomberg. The corresponding Bloomberg tickers are SPX Index, LUACTRUU Index, LUATTRUU Index, BCOM Index, XAU Curncy, DXY Curncy, DJUSRE Index, USGG10YR Index and GTII10 Govt.

Unless otherwise noted, we aggregate daily closing prices to construct weekly coin returns. Each year is divided into 52 weeks: the first week contains the year’s first seven days, the next 50 weeks consist of seven days each, and the final week contains the remaining days of the year. For the construction of weekly returns, we exclude coins with a market capitalization below $1 million at the formation date and winsorize returns at the 0.0025% level in both tails. We construct a cryptocurrency market return as the value-weighted return of all underlying coins. The cryptocurrency excess market return is constructed as the difference between the cryptocurrency market return and the risk-free rate measured as the 1-month T-bill rate at the weekly frequency, which we obtain from the Federal Reserve Bank of St. Louis.

Figure [1](https://arxiv.org/html/2510.14435v1#S2.F1 "Figure 1 ‣ 2 DATA ‣ Cryptocurrency as an Investable Asset Class: Coming of Age") summarizes the time-series evolution of cryptocurrency prices and market capitalization. A one-dollar investment at the start of the sample grows to about $160 in Bitcoin and $80 in the overall market. There is substantial variation over time. Market capitalization reaches nearly $4 trillion, with Bitcoin and Ethereum accounting for approximately 58% and 12% of the total at the end of the sample.

![Refer to caption](x1.png)


(a) Return

![Refer to caption](x2.png)


(b) Capitalization

Figure 1: Cryptocurrency market returns and capitalization

Panel A of the figure plots the cryptocurrency market return against Bitcoin. Panel B plots the cryptocurrency market capitalization against the top five coins by market capitalization at the end of the sample (Bitcoin, Ethereum, Ripple, Binance Coin, and Solana). For returns, the figure shows the value of investment over time for one dollar of investment starting in December 31, 2013. For market capitalization, the figure shows the value over time of the outstanding coins in US dollar billions. Data end on September 6, 2025.

## 3 THE TEN FACTS OF CRYPTOCURRENCY

We organize the main discussions of this review into the ten key stylized empirical facts on cryptocurrency markets.

### 3.1 Fact 1: High return, high volatility—normal Sharpe ratio

Fact 1: The cryptocurrency market has an order of magnitude higher returns and volatility than equities, but a broadly similar Sharpe ratio.

Popular discussion of cryptocurrencies tends to focus either on their dramatic average returns or on dramatic volatility. From the classic finance point of view, the relevant measure is, however, risk-adjusted performance—the Sharpe ratio, i.e., mean excess return per unit of volatility (Sharpe [1966](https://arxiv.org/html/2510.14435v1#bib.bib130)).

Liu & Tsyvinski ([2021](https://arxiv.org/html/2510.14435v1#bib.bib105)) establish that the aggregate cryptocurrency market exhibits returns and volatilities an order of magnitude higher than those of the aggregate stock market, but Sharpe ratios remain broadly comparable. Fact 1 revisits and confirms this finding in a longer and larger dataset up to September 2025.

Table [1](https://arxiv.org/html/2510.14435v1#S3.T1 "Table 1 ‣ 3.1 Fact 1: High return, high volatility—normal Sharpe ratio ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age"), Panel A, reports summary statistics for the sample beginning in 2014 and ending in September 2025, as well as for the samples pre-2020 and post-2020. We compare returns on the aggregate coin market, a large-cap index of the top 100 cryptocurrencies (Coin 100), Bitcoin, and the aggregate U.S. stock market. The average returns and volatilities of all cryptocurrency return series are an order of magnitude greater than those of the stock market across all sample periods. For instance, average weekly returns exceed 1% for all cryptocurrency indices, compared with less than 0.3% for the aggregate stock market. However, the weekly Sharpe ratios are similar across cryptocurrencies and equities. This, confirms that the Sharpe ratio calculated by Liu & Tsyvinski ([2021](https://arxiv.org/html/2510.14435v1#bib.bib105)) holds in the most recent sample.

Table [1](https://arxiv.org/html/2510.14435v1#S3.T1 "Table 1 ‣ 3.1 Fact 1: High return, high volatility—normal Sharpe ratio ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age"), Panel A, reports maximum drawdowns and run-ups for the four return indices. Drawdowns are important as they provide a measure of tail-risk not fully reflected by standard deviation. Drawdowns and run-ups are substantially larger for cryptocurrencies than for equities. Importantly, for all three cryptocurrency indices, maximum drawdowns and run-ups are smaller in magnitude in the post-2020 sample than in the pre-2020 sample, while the reverse holds for equities. This pattern can also be observed in the standard deviations of returns—they decline for cryptocurrencies and rise for equities in the more recent period.

Table 1: Summary statistics

| Panel A. Summary statistics returns | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Mean (%) | SD (%) | t-Stat | Sharpe | Skew | Kurt | Max DD (%) | Max RU (%) |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) |
|  | Full sample | | | | | | | |
| Coin market | 1.23 | 10.27 | 2.95 | 0.12 | 0.15 | 1.89 | -89.82 | 227.74 |
| Coin 100 | 1.24 | 10.30 | 2.98 | 0.12 | 0.15 | 1.84 | -89.23 | 224.08 |
| Bitcoin | 1.33 | 10.12 | 3.24 | 0.13 | 0.33 | 2.16 | -83.62 | 208.94 |
| Stock | 0.27 | 2.18 | 3.01 | 0.11 | -0.66 | 3.95 | -27.22 | 17.55 |
|  | Pre-2020 sample | | | | | | | |
| Coin market | 1.20 | 11.37 | 1.87 | 0.10 | 0.25 | 1.39 | -89.82 | 227.74 |
| Coin 100 | 1.20 | 11.44 | 1.86 | 0.10 | 0.23 | 1.29 | -89.23 | 224.08 |
| Bitcoin | 1.35 | 11.28 | 2.12 | 0.12 | 0.31 | 1.46 | -83.62 | 208.94 |
| Stock | 0.24 | 1.79 | 2.35 | 0.12 | -0.68 | 2.54 | -17.09 | 10.67 |
|  | Post-2020 sample | | | | | | | |
| Coin market | 1.26 | 9.00 | 2.41 | 0.13 | -0.07 | 2.34 | -77.57 | 83.62 |
| Coin 100 | 1.29 | 8.98 | 2.46 | 0.14 | -0.03 | 2.41 | -76.78 | 84.36 |
| Bitcoin | 1.30 | 8.75 | 2.56 | 0.14 | 0.32 | 3.03 | -74.94 | 95.10 |
| Stock | 0.29 | 2.53 | 2.00 | 0.10 | -0.63 | 3.47 | -27.22 | 17.55 |
| Panel B. Coin market return correlations | | | | | | | | |
| Sample | Stock | Corp | Govt | Comm | Gold | Dollar | Inflation |  |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) |  |
| Full | 0.20 | 0.08 | 0.03 | 0.14 | 0.12 | -0.06 | 0.17 |  |
|  | (4.92) | (2.04) | (0.70) | (3.60) | (2.87) | (-1.49) | (4.35) |  |
| Pre 2020 | 0.02 | 0.04 | 0.02 | 0.03 | 0.06 | -0.03 | 0.03 |  |
|  | (0.44) | (0.66) | (0.42) | (0.51) | (1.13) | (-0.48) | (0.46) |  |
| Post 2020 | 0.37 | 0.13 | 0.04 | 0.27 | 0.18 | -0.10 | 0.31 |  |
|  | (6.91) | (2.20) | (0.60) | (4.74) | (3.10) | (-1.80) | (5.66) |  |

Notes: This table summarizes the main properties of coin market return. Panel A reports weekly summary statistics of the coin market index and compares them with the value-weighted index of the top 100 coins by market capitalization (Coin 100), Bitcoin and U.S. stock market returns. Reported measures include the mean, standard deviation, tt-statistic, Sharpe ratio, skewness, kurtosis, maximum drawdown and run-up. Panel B presents pairwise correlation coefficients between coin market returns and returns on the U.S. stock market, corporate bonds, government bonds, a commodity index, gold, the dollar index, and the changes in inflation expectations. tt-statistics are reported in parentheses. The full sample covers the period from January 7, 2014 to September 6, 2025. The pre-2020 sample is the sample before Jan 1, 2020, and the post-2020 sample is the sample since Jan 1, 2020.

### 3.2 Fact 2: Cryptocurrency is a distinct asset: it moves largely on its own—but increasingly with equities, gold and commodities

Fact 2: The aggregate cryptocurrency market remains largely uncorrelated with most traditional asset classes, but its correlation with U.S. equities has increased sharply—from 2% before 2020 to 37% after 2020.

How cryptocurrencies co-move with traditional asset classes is a first-order question for asset pricing and portfolio choice (e.g., Markowitz [1952](https://arxiv.org/html/2510.14435v1#bib.bib113)). Correlations are an important determinant of diversification benefits and show whether cryptocurrency risk is distinct to that market or simply represent familiar risks from other markets. We revisit the cryptocurrency aggregate correlation structure using updated data, contrasting the pre-2020 and post-2020 return correlation.

One of the main results of Liu & Tsyvinski ([2021](https://arxiv.org/html/2510.14435v1#bib.bib105)) is that aggregate cryptocurrency returns have insignificant exposures to the returns of traditional asset classes, such as equities, bonds, commodities, and foreign exchanges. In other words, the correlation between the aggregate cryptocurrency returns and those of traditional asset classes are low. Fact 2 revisits this finding. We show that there is a rising correlation with the U.S. stock market.

Table [1](https://arxiv.org/html/2510.14435v1#S3.T1 "Table 1 ‣ 3.1 Fact 1: High return, high volatility—normal Sharpe ratio ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age"), Panel B, reports correlations of aggregate cryptocurrency returns with those of major asset classes. In the pre-2020 sample, correlations with equities, corporate bonds, government bonds, commodities, gold, and the dollar are all statistically insignificant, confirming the earlier findings of Liu & Tsyvinski ([2021](https://arxiv.org/html/2510.14435v1#bib.bib105)). In contrast, in the post-2020 sample, aggregate cryptocurrency returns become significantly correlated with equities (37%), commodities (27%), gold (18%), and corporate bonds (13%) at the 5% level. The correlation with the dollar index is negative (-10%) and significant at the 10% level. Government bonds remain the only asset class with no significant link.

The most striking change is the correlation with the U.S. stock market, which rises from only 2% before 2020 to 37% afterwards. This substantial increase is an important indicator that cryptocurrencies have become more integrated with equity markets. We also document a significant post-2020 correlation with changes in expected inflation (31%), measured as the first difference in the yield differential between nominal and inflation-indexed U.S. Treasury bonds with 10-year maturity. Since this measure incorporates an inflation risk premium, the result may reflect the same underlying risk component that drives the stronger comovement between cryptocurrencies and equities in recent years. In our view, this link with expected inflation is important, as it provides empirical evidence on the original motivation of cryptocurrencies as assets designed to hedge against the inflationary risks of government printing money.

The increase in correlation between the cryptocurrency market and traditional asset classes has been documented in recent studies, for example, Dong et al. ([2023](https://arxiv.org/html/2510.14435v1#bib.bib53)) and Jiang et al. ([2025](https://arxiv.org/html/2510.14435v1#bib.bib87)). Several mechanisms are proposed to explain this phenomenon, including monetary policy, retail investor trading, and financialization. The literature has yet to reach a consensus on the cause of this important shift in the return dynamics of the cryptocurrency market.

### 3.3 Fact 3: Significant diversification benefits from adding small amount of cryptocurrencies in investment portfolios

Fact 3: Cryptocurrency idiosyncratic risk can be significantly reduced by constructing optimal mean-variance asset portfolios that include cryptocurrencies—the inclusion of cryptocurrencies enlarges the mean-variance frontier. Optimal portfolio allocates 3.1% cryptocurrency for retail investors and 5.5% for institutional investors.

Modern finance theory, starting from Markowitz ([1952](https://arxiv.org/html/2510.14435v1#bib.bib113)), emphasizes the central insight of diversification: an asset’s covariance with the investor’s portfolio matters more than its volatility. Low correlations push the efficient frontier outward, and volatile assets can add value if their expected returns compensate for marginal risk. Since Fact 1 establishes that cryptocurrencies have low correlations with stocks and bonds, they can be effective risk diversifiers under standard portfolio-theory frameworks.

Liu & Tsyvinski ([2021](https://arxiv.org/html/2510.14435v1#bib.bib105)) show that cryptocurrencies can improve portfolio efficiency because of their historically low correlations with traditional asset classes and comparatively high expected returns. Using the Black–Litterman portfolio allocation model (Black & Litterman [1990](https://arxiv.org/html/2510.14435v1#bib.bib29)) to incorporate investor views, Liu & Tsyvinski ([2021](https://arxiv.org/html/2510.14435v1#bib.bib105)) estimate that a representative investor would optimally allocate between 1% and 6% of wealth to cryptocurrencies, depending on the strength of those views. A complementary view comes from Bayesian portfolio theory. Duchin et al. ([2025](https://arxiv.org/html/2510.14435v1#bib.bib55)) obtain similar optimal weights in the 1%–5% range. Ang et al. ([2023](https://arxiv.org/html/2510.14435v1#bib.bib11)) find much larger optimal weights when investors have a preference for positive skewness, such as under constant relative risk aversion.

Because the optimal crypto weight is sensitive to the joint return distribution—especially the correlation between cryptocurrencies and traditional assets—and because this correlation structure shifted after 2020 (see Fact 2), we re-estimate the theoretical optimal allocations using post-2020 data under the same Black–Litterman framework.

Moreover, we extend the analysis to two representative investor classes: a retail investor and an institutional investor. In calculating the theoretical optimal crypto portfolio shares for them, we differ only in their investable options. This simplification abstracts from practical complications, such as liquidity, custody, and regulatory constraints, to make the exercise tractable.

For a retail investor, we start with a baseline portfolio that is 50–50 between financial assets and real estate, with the financial portion 60–40 stocks–bonds. Based on the model, if we add an allocation to the cryptocurrency market, we would raise the portfolio’s Sharpe ratio from 0.39 to 0.52, with an optimal crypto weight of 3.1% of total wealth. As a historical counterfactual, we also compute the theoretical optimal portfolio using only pre-2020 data; the optimal crypto share is 1.4%. Mapping this to per-capita U.S. net wealth in 2019, a 1.4% allocation implies an investment of about $3,500; held from 2020 to the end of our sample, this position would have grown by roughly $52,000 (about 1,462%). This is a back-of-the-envelope, buy-and-hold calculation that assumes no rebalancing.

For an institutional investor, we consider a broader investable universe—equities, government and corporate bonds, commodities, and real estate—with baseline weights proportional to each asset class’s market capitalization. Solving for the optimal portfolio and assuming slightly greater confidence in views on cryptocurrencies than in the retail case, the model implies an increase in the portfolio’s Sharpe ratio from 0.69 to 0.95, with an optimal share of 5.5% in the cryptocurrency market.

These results show that—even with the post-2020 increase in comovement with equities—optimal allocations to cryptocurrency are sizable and in the 3–5% range, with larger weights for institutional portfolios. It is important to note that the estimations in this section are back-of-the-envelope and rely on the properties of returns that may not persist and abstract from important issues related to liquidity, custody, and regulatory risk, and therefore should be viewed as theoretical upper bounds on the potential diversification benefits of this emerging investable asset class, not as actual investment recommendations. For context, CalPERS, one of the largest U.S. pension funds, reports portfolio shares of comparable magnitude in emerging-market debt (5.3%), high-yield bonds (5.3%), private debt (3.8%), and mortgage-backed securities (5.8%) as of June 2025, indicating that the model-implied weights of cryptocurrencies are within a realistic range.

### 3.4 Fact 4: How to be “smart” in crypto—crypto-size, crypto-momentum and crypto-value

Fact 4: A small number of smart beta strategies—based on crypto-size, crypto-momentum, and crypto-value—span the cross-section of cryptocurrency returns.

A central question in asset pricing is whether systematic variation in expected returns can be explained by a parsimonious set of factors. In equities, substantial academic endeavor—most prominently by Eugene Fama and Kenneth French (e.g., Fama & French ([1992](https://arxiv.org/html/2510.14435v1#bib.bib59)))—established this approach, and factor models play a core role in modern finance practice and theory from risk management of large banks to niche hedge fund strategies. For cryptocurrencies, Liu et al. ([2022](https://arxiv.org/html/2510.14435v1#bib.bib107)) establish that a three factor model consisting of the aggregate cryptocurrency market, size, and momentum (C-3 factor model), captures a large fraction of the cross-section of expected returns. Liu et al. ([2021](https://arxiv.org/html/2510.14435v1#bib.bib106)) show that adding a value factor (C-4 factor model) further strengthens the explanatory power. We revisit this evidence using our updated sample and show that a small number of predictors drive the cross-section of cryptocurrency returns over the longer sample and post-2020.

We construct smart beta strategies by sorting coins into quintile portfolios based on three established significant predictors: market capitalization (CSIZE), past two-week returns (CMOM), and the price-to-new-address ratio (CVALUE).333Studies based on smaller samples of coins have also proposed additional predictors of cryptocurrency returns in the cross-section, including liquidity (e.g., Bianchi et al. [2022](https://arxiv.org/html/2510.14435v1#bib.bib27)), market segmentation (e.g., Borri & Shakhnov [2022](https://arxiv.org/html/2510.14435v1#bib.bib37)), and higher-order moments (e.g., Borri et al. [2022b](https://arxiv.org/html/2510.14435v1#bib.bib35); Borri & Santucci de Magistris [2022](https://arxiv.org/html/2510.14435v1#bib.bib36)). The return to each predictor is measured as the long-short spread between the highest and lowest quintiles (Portfolio 5 minus Portfolio 1).

Table [2](https://arxiv.org/html/2510.14435v1#S3.T2 "Table 2 ‣ 3.4 Fact 4: How to be “smart” in crypto—crypto-size, crypto-momentum and crypto-value ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age"), Panels A and B, report average excess returns to the quintile portfolios and the corresponding long-short strategies for the full sample and the post-2020 subsample. All three predictors generate statistically significant long-short returns in the full sample. The average long-short returns based on size and value are significantly negative and the average long-short return based on momentum is significantly positive, consistent with Liu et al. ([2022](https://arxiv.org/html/2510.14435v1#bib.bib107)). Cryptocurrency value is the weekly quintile portfolio of each bracket based on the price-to-new address ratio. High bracket is the low-value coins and low bracket is the high-value coins. The sorting is done in week tt and the returns are the value-weighted average in the following week.

Importantly, these results remain robust in the post-2020 sample, the core set of smart beta strategies in the C-3 factor model and C-4 factor model continues to explain variation in cryptocurrency returns even in the more recent period.

The C-4 structure of the crypto-market thus parallels the equity market, where a small number of equity-market factors—most notably size, value, momentum, and profitability—dominate the cross-section of expected returns. For example, Asness et al. ([2013](https://arxiv.org/html/2510.14435v1#bib.bib13)) present evidence of value and momentum in equities, bonds, currencies, and commodities. The C-4 factor model of Liu et al. ([2022](https://arxiv.org/html/2510.14435v1#bib.bib107)) and Liu et al. ([2021](https://arxiv.org/html/2510.14435v1#bib.bib106)) is the cryptocurrency counterpart of the classic 4-factor model of Fama & French ([1992](https://arxiv.org/html/2510.14435v1#bib.bib59)) and Carhart ([1997](https://arxiv.org/html/2510.14435v1#bib.bib43)) for equities. It is important to note that the predictors in cryptocurrency markets are only partly analogous to those in equity markets. CSIZE and CMOM closely resemble their equity counterparts, although crypto momentum is measured over a much shorter horizon (previous two weeks, versus the standard 12-to-2 months in equities). In contrast, there is no direct analogue to book value (Shiller [1981](https://arxiv.org/html/2510.14435v1#bib.bib132)) in cryptocurrencies, so we follow Liu et al. ([2021](https://arxiv.org/html/2510.14435v1#bib.bib106)) and proxy CVALUE with the price-to-new-address ratio.444Liu et al. ([2021](https://arxiv.org/html/2510.14435v1#bib.bib106)) show that the number of new addresses captures the network effects of cryptocurrencies and serves as a measure of their fundamental value.

Establishing the small factor structure of the cryptocurrency returns, in our view, is not only important from purely the empirical asset pricing point of view but also since it provides a set of stylized low dimensional features that capture the main insights of several important theoretical models of cryptocurrency (Cong et al. [2021b](https://arxiv.org/html/2510.14435v1#bib.bib49), Sockin & Xiong [2023a](https://arxiv.org/html/2510.14435v1#bib.bib135), [b](https://arxiv.org/html/2510.14435v1#bib.bib136)).

A related important point is that in addition to determining which betas are smart, it is equally as important to establish which betas from the factor zoo are not “smart”. Specifically, Liu et al. ([2022](https://arxiv.org/html/2510.14435v1#bib.bib107)) and Liu et al. ([2021](https://arxiv.org/html/2510.14435v1#bib.bib106)) show that—besides crypto-specific size, momentum, and value—most of the smart beta strategies from the canonical factor zoo in the equity market (Feng et al. [2020](https://arxiv.org/html/2510.14435v1#bib.bib61)) either do not generate significant hedged long-short strategy returns or are subsumed by the C-4 factor model. In Table [3](https://arxiv.org/html/2510.14435v1#S3.T3 "Table 3 ‣ 3.4 Fact 4: How to be “smart” in crypto—crypto-size, crypto-momentum and crypto-value ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age"), we study long-short strategies based on these signals post–2020. These strategies include portfolios based on long-horizon momentum, volatility, volume, and beta. We find that these long-short strategies continue not to generate significant average returns in the recent sample.555In a recent study, Fieberg et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib63)) examine 20,736 research designs for 43 sorting variables in the cryptocurrency market. They find that the most prominent cryptocurrency factors, such as size and momentum, remain consistently robust across various specifications, but the others do not. These results give evidence that the cross-section of cryptocurrency returns can be summarized by a small number of factors.

Table 2: Cryptocurrency smart beta strategies

| Panel A: Full sample | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
|  | Quintiles | | | | | |
|  | 1 | 2 | 3 | 4 | 5 | 5–1 |
| CSIZE | Low |  |  |  | High |  |
| Mean | 0.035\*\*\* | 0.015\* | 0.014\* | 0.007 | 0.012\*\*\* | -0.023\*\*\* |
| tt(Mean) | (3.27) | (1.88) | (1.76) | (0.99) | (2.59) | (-2.66) |
| CMOM | Low |  |  |  | High |  |
| Mean | -0.002 | 0.005 | 0.001 | 0.018\*\*\* | 0.024\*\*\* | 0.026\*\*\* |
| tt(Mean) | (-0.28) | (0.68) | (0.21) | (2.84) | (3.19) | (3.89) |
| CVALUE | Low |  |  |  | High |  |
| Mean | 0.034\*\*\* | 0.026\*\* | 0.018\*\* | 0.014 | -0.000 | -0.035\*\*\* |
| tt(Mean) | (2.82) | (2.24) | (2.00) | (1.61) | (-0.05) | (-3.50) |
| Panel B: Post-2020 sample | | | | | | |
|  | Quintiles | | | | | |
|  | 1 | 2 | 3 | 4 | 5 | 5–1 |
| CSIZE | Low |  |  |  | High |  |
| Mean | 0.021\*\* | 0.011 | 0.012 | 0.013 | 0.012\*\* | -0.009\* |
| tt(Mean) | (2.53) | (1.29) | (1.33) | (1.42) | (2.11) | (-1.69) |
| CMOM | Low |  |  |  | High |  |
| Mean | 0.001 | 0.001 | 0.009 | 0.016\*\* | 0.021\*\* | 0.021\*\*\* |
| tt(Mean) | (0.08) | (0.17) | (1.38) | (2.41) | (2.50) | (3.70) |
| CVALUE | Low |  |  |  | High |  |
| Mean | 0.030\*\* | 0.021\* | 0.017\*\* | 0.012\* | 0.007 | -0.023\*\* |
| tt(Mean) | (2.35) | (1.95) | (2.06) | (1.79) | (1.35) | (-2.32) |

Notes: This table reports the mean quintile portfolio returns and long-short portfolio return for crypto smart beta strategies. The smart beta predictors are market capitalization (CSIZE), past two-week return (CMOM), and price-to-new address ratio (CVALUE). The long-short portfolio is long portfolio 5 and short portfolio 1 for all predictors. The mean returns are the time-series averages of weekly value-weighted portfolio excess returns. The post-2020 sample is the sample since Jan 1, 2020. tt-statistics in parentheses are Newey-West adjusted. \*, \*\*, and \*\*\* denote significance at the 10%, 5% and 1% levels.




Table 3: Cryptocurrency smart beta strategies that are not beta

| Panel A: Full sample | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
|  | Quintiles | | | | | |
|  | 1 | 2 | 3 | 4 | 5 | 5–1 |
| MOM12 | Low |  |  |  | High |  |
| Mean | 0.015\*\* | 0.011 | 0.011\* | 0.011\* | 0.018\*\*\* | 0.003 |
| tt(Mean) | (2.11) | (1.52) | (1.73) | (1.84) | (2.83) | (0.47) |
| MOM24 | Low |  |  |  | High |  |
| Mean | 0.021\*\*\* | 0.018\*\* | 0.013\*\* | 0.016\*\* | 0.011\* | -0.009 |
| tt(Mean) | (2.81) | (2.37) | (2.22) | (2.48) | (1.96) | (-1.50) |
| VOL | Low |  |  |  | High |  |
| Mean | 0.013\*\*\* | 0.022\*\*\* | 0.014\*\* | 0.015\* | 0.011 | -0.003 |
| tt(Mean) | (2.93) | (2.86) | (2.27) | (1.95) | (1.36) | (-0.45) |
| VOLUME | Low |  |  |  | High |  |
| Mean | 0.043\*\* | 0.012\* | 0.011 | 0.013\* | 0.013\*\*\* | -0.030 |
| tt(Mean) | (2.17) | (1.66) | (1.51) | (1.84) | (2.77) | (-1.60) |
| CMKT BETA | Low |  |  |  | High |  |
| Mean | 0.009 | 0.012\*\* | 0.013\*\* | 0.016\*\* | 0.016\*\* | 0.007 |
| tt(Mean) | (1.47) | (2.17) | (2.35) | (2.50) | (2.38) | (1.34) |
| MKT BETA | Low |  |  |  | High |  |
| Mean | 0.006 | 0.012\*\* | 0.015\*\*\* | 0.018\*\* | 0.017\* | 0.011\* |
| tt(Mean) | (0.88) | (2.19) | (2.81) | (2.48) | (1.96) | (1.80) |
| Panel B: Post-2020 sample | | | | | | |
|  | 1 | 2 | 3 | 4 | 5 | 5–1 |
| MOM12 | Low |  |  |  | High |  |
| Mean | 0.009 | 0.009 | 0.011 | 0.011\* | 0.016\*\* | 0.006 |
| tt(Mean) | (1.18) | (1.15) | (1.59) | (1.84) | (2.24) | (1.30) |
| MOM24 | Low |  |  |  | High |  |
| Mean | 0.014\* | 0.011 | 0.011 | 0.013\* | 0.011\* | -0.004 |
| tt(Mean) | (1.72) | (1.52) | (1.59) | (1.90) | (1.75) | (-0.66) |
| VOL | Low |  |  |  | High |  |
| Mean | 0.012\*\* | 0.011 | 0.014\* | 0.011 | 0.005 | -0.007 |
| tt(Mean) | (2.23) | (1.61) | (1.70) | (1.26) | (0.59) | (-1.39) |
| VOLUME | Low |  |  |  | High |  |
| Mean | 0.047\* | 0.004 | 0.017 | 0.012 | 0.012\*\* | -0.035 |
| tt(Mean) | (1.69) | (0.67) | (1.60) | (1.63) | (2.16) | (-1.35) |
| CMKT BETA | Low |  |  |  | High |  |
| Mean | 0.006 | 0.013\*\* | 0.014\*\* | 0.009 | 0.014\* | 0.008 |
| tt(Mean) | (1.43) | (2.02) | (2.06) | (1.37) | (1.86) | (1.64) |
| MKT BETA | Low |  |  |  | High |  |
| Mean | 0.004 | 0.012\*\* | 0.013\*\* | 0.011\* | 0.011 | 0.007 |
| tt(Mean) | (0.61) | (2.00) | (2.00) | (1.67) | (1.27) | (1.17) |

Notes: This table reports the mean quintile portfolio returns and long-short portfolio return for crypto smart beta strategies based on insignificant predictors. The predictors are past 12-week and 24-week return (MOM12 and MOM24), past 24-week return standard deviation (VOL), past 24-week dollar trading volume (VOLUME), coin market beta (CMKT BET) and stock market beta (MKT BETA) estimated using past 24-week returns. The long-short portfolio is long portfolio 5 and short portfolio 1 for all predictors. The mean returns are the time-series averages of weekly value-weighted portfolio excess returns. The post-2020 sample is the sample since Jan 1, 2020. tt-statistics in parentheses are Newey-West adjusted. \*, \*\*, and \*\*\* denote significance at the 10%, 5% and 1% levels.

### 3.5 Fact 5: Mind the Jumps—large, sudden price moves and “common disasters”

Fact 5: Jumps are frequent and account for a large share of variation of cryptocurrency returns, far more than in equities. Thus, disasters are not rare but common.

Leibniz wrote that *natura non facit saltus*—nature makes no jumps. In economics and finance, this often means that most changes occur gradually, with only occasional discontinuities. Indeed, jumps are rare in many asset classes, and this key insight leads Black & Scholes ([1973](https://arxiv.org/html/2510.14435v1#bib.bib30)), in their celebrated option pricing paper, to model prices as Brownian motions.666Merton ([1976](https://arxiv.org/html/2510.14435v1#bib.bib115)) is aware of potential jumps in equity prices and include the feature in his paper. Rare disasters are also used as a central ingredient to explain risk-premia (e.g., Rietz ([1988](https://arxiv.org/html/2510.14435v1#bib.bib120)); Barro ([2006](https://arxiv.org/html/2510.14435v1#bib.bib20))). Cryptocurrencies are different: jumps, and hence disasters, are not “rare disasters” but are “common disasters.” Specifically, Borri & Santucci de Magistris ([2022](https://arxiv.org/html/2510.14435v1#bib.bib36)) show that 12.8% of Bitcoin’s daily variability can be attributed to jumps—large, sudden price moves—and that higher-order moments such as skewness and kurtosis explain the risk premium on Bitcoin.777See early evidence from Scaillet et al. ([2020](https://arxiv.org/html/2510.14435v1#bib.bib126)) similarly documenting very frequent jumps in Bitcoin. Fact 5 revisits and extend this finding, documenting the frequency and size of jumps in cryptocurrency and showing that those are far more relevant than for the U.S. stock market.

Table [4](https://arxiv.org/html/2510.14435v1#S3.T4 "Table 4 ‣ 3.5 Fact 5: Mind the Jumps—large, sudden price moves and “common disasters” ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age") reports the frequency and magnitude of jumps in Bitcoin and Ethereum—the two largest cryptocurrencies by market capitalization—compared with U.S. stocks. Jumps are identified as the difference between the daily realized variance of Barndorff-Nielsen & Shephard ([2002](https://arxiv.org/html/2510.14435v1#bib.bib18)) and the bi-power variation of Barndorff-Nielsen & Shephard ([2006](https://arxiv.org/html/2510.14435v1#bib.bib19)), a jump-robust measure of integrated variance. The two realized measures are constructed from tick-level data aggregated at the 5-minute frequency. For U.S. equities, the same procedure is applied, and values represent cross-sectional averages across the constituents of the Dow Jones Industrial Average. Only jumps that are statistically significant at the 0.1% confidence level according to the BNS test of Barndorff-Nielsen & Shephard ([2006](https://arxiv.org/html/2510.14435v1#bib.bib19)) are retained. For Bitcoin and Ethereum, the probability of a significant jump on a given day is around 40 percent in the pre–2020 sample and 15–20 percent in the post–2020 period. In sharp contrast, the probability of a daily jump in U.S. stocks is below 10 percent before 2020 and falls to about 3 percent thereafter. Thus, jumps are far more frequent in cryptocurrencies than in equities. Conditional on a jump occurring, however, the share of total return variation explained by the jump is broadly similar across asset classes, particularly in the post–2020 period. This shows that what sets cryptocurrencies apart is the high frequency of jumps—contrary to Leibniz’s dictum that *natura non facit saltus*, cryptocurrencies are markets where *saltus sunt regula* (jumps are the rule), rather than the exception.

These results show that higher-order moments are central to understanding cryptocurrency risk. Equity and bond markets follow relatively smooth dynamics with only rare discontinuities. Cryptocurrency markets are characterized by frequent and sizable jumps that are a defining feature of their return distribution. This prevalence of jumps, and the corresponding role of higher-order moments, means significant challenges for risk management and portfolio allocation (see, e.g., Borri [2019](https://arxiv.org/html/2510.14435v1#bib.bib31)). The implication is that we need empirical asset-pricing strategies that explicitly accommodate higher-order moments and nonlinearities (see, e.g., Kozak et al. [2020](https://arxiv.org/html/2510.14435v1#bib.bib95), Chetverikov et al. [Forthcoming](https://arxiv.org/html/2510.14435v1#bib.bib45), Borri et al. [2025](https://arxiv.org/html/2510.14435v1#bib.bib33)).

Table 4: Jumps in Cryptocurrency

|  | Pr(J) | N(J) | Quantiles of J/RV | | | |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | q(50) | q(75) | q(90) | q(95) |
| Full sample | | | | | | |
| Bitcoin | 28.005 | 946 | 31.237 | 44.322 | 58.819 | 67.419 |
| Ethereum | 25.992 | 878 | 34.420 | 56.584 | 74.992 | 85.270 |
| Stock | 5.313 | 137 | 37.743 | 44.271 | 52.009 | 57.310 |
| Pre-2020 sample | | | | | | |
| Bitcoin | 40.041 | 585 | 36.410 | 51.457 | 64.727 | 71.562 |
| Ethereum | 39.699 | 580 | 47.651 | 66.449 | 80.682 | 90.073 |
| Stock | 5.244 | 66 | 37.872 | 43.985 | 51.658 | 55.976 |
| Post-2020 sample | | | | | | |
| Bitcoin | 18.841 | 361 | 26.161 | 33.197 | 42.350 | 48.892 |
| Ethereum | 15.501 | 297 | 24.545 | 30.736 | 39.429 | 45.667 |
| Stock | 5.643 | 60 | 37.959 | 44.838 | 52.434 | 57.079 |

This table reports the probability of observing a statistically significant jump (P(J)), the number of such events (N(J)), and quantiles of the ratio of jump variation to realized variance (J/RV), conditional on a significant jump, for Bitcoin, Ethereum, and U.S. stocks. Significant jumps are identified using the BNS test with a 0.1% significance level. For U.S. equities, values are cross-sectional averages across the constituents of the Dow Jones Industrial Average. Data are from January 1, 2015 to March 31, 2025. The pre-2020 sample is the sample ending Jan 1, 2020. The post-2020 sample is the sample since Jan 1, 2020.

### 3.6 Fact 6: Few factors, higher orders—rather than machine learning: why less is more

Fact 6: In cryptocurrency, higher-order terms of the C-4 model accounts for approximately 25% of the cross-section of returns and captures most of the insights of machine learning methods.

A growing literature in finance uses machine learning methods, such as neural networks, to investigate the cross-section of returns (see, for example, Nagel [2021](https://arxiv.org/html/2510.14435v1#bib.bib116), Gu et al. [2020](https://arxiv.org/html/2510.14435v1#bib.bib74), Kelly et al. [2024](https://arxiv.org/html/2510.14435v1#bib.bib89)). Neural networks have become extremely successful in many prediction problems and moreover have the universal approximation property (Cybenko [1989](https://arxiv.org/html/2510.14435v1#bib.bib52); Hornik et al. [1989](https://arxiv.org/html/2510.14435v1#bib.bib81))—a sufficiently large neural network can approximate any continuous function—and thus, in principle, capture any features of the data. These ideas have been present in the machine learning literature for several decades, but only recently have they become dramatically successful, as computational advances enabled the estimation of very large models, essentially aligning with the core idea of the universal approximation theorem. This has led finance and economics, as well as many other fields, to develop models with a very large number of parameters. The main shortcoming of neural networks for finance is that they are “black box” models. Once millions and sometimes hundred of millions of “factors” are run through often rather complicated and delicate gradient descent-like algorithms, it is difficult to see what features are economically important, how exactly the model produces results, and if an environment changes, whether the model still continues to perform.

One alternative to neural nets is the Kolmogorov–Arnold representation theorem (Kolmogorov [1956](https://arxiv.org/html/2510.14435v1#bib.bib94); Arnold [1957](https://arxiv.org/html/2510.14435v1#bib.bib12)) introduced in finance by Borri et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib32)).888Borri et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib32)), arXiv, April 11, 2024. Kolmogorov–Arnold remarkably shows that any nonlinear function can be written *exactly* as a combination of a finite sum of univariate functions composed with a link function. This formulation is thus a representation, not an approximation. Importantly, the early machine learning literature showed how to use in theory this representation to construct a shallower and smaller network (Hecht-Nielsen [1987](https://arxiv.org/html/2510.14435v1#bib.bib78), Girosi & Poggio [1989](https://arxiv.org/html/2510.14435v1#bib.bib67), Kurkova [1991](https://arxiv.org/html/2510.14435v1#bib.bib96)). This network can be thought of as a much lower dimensional neural network where the activation functions of each neuron are being trained and adapt to the data. While theoretically this result is remarkable,999In fact, Kolmogorov and Arnold construction solved Hilbert’s thirteenth problem, one of the major open problems of mathematics of the twentieth century. it is not clear whether this approach would work on actual data because of the complexity that the theory requires for the representation of any function, and in particular, on finance data, which is both relatively small and has a very low signal-to-noise ratio. Borri et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib32)) is the first paper that shows the practical implementation and effectiveness of the Kolmogorov–Arnold architecture on actual data. Specifically, they show that this methodology enables construction of a single non-linear factor (KA factor) that captures a significant part of the variation in expected returns.101010Schmidt-Hieber ([2021](https://arxiv.org/html/2510.14435v1#bib.bib129)) is the first paper in the literature that studies quantitative properties of Kolmogorov–Arnold representation for multiple-layer neural networks and thus introduces the Kolmogorov–Arnold architecture. An early paper by Horowitz & Mammen ([2007](https://arxiv.org/html/2510.14435v1#bib.bib82)) discusses essentially a similar structure of general nonparametric regressions with an unknown link function. Subsequent to Borri et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib32)), Liu et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib108)) (arXiv, April 30, 2024) popularized Kolmogorov Arnold Networks (KAN) to the machine learning community and showed how significantly shallower neural nets built on Kolmogorov–Arnold architecture may, in some cases, outperform and bring interpretability in several science applications. Toscano et al. ([2025](https://arxiv.org/html/2510.14435v1#bib.bib138)) argue that KAN rely on computation expensive basis functions with a performance that degrades with high parameter counts, which might limit the use in these science applications. The main advantage of this approach is that the KA-factor can be thought of as a simple representation of a much more complicated and larger neural network and, in principle, captures *all* such networks, without having to consider a variety of neural networks specifications and the optimization algorithms.

Another alternative to neural networks follows the traditional finance toolbox—approximate and estimate the stochastic discount factor via a Taylor expansion. However, the Taylor approximation to the higher order generates a very large set of factors, due to the need to account for all of the interactions of the higher-order terms in the Taylor expansion. Borri et al. ([2025](https://arxiv.org/html/2510.14435v1#bib.bib33)) develop the properties of a forward-selection Fama–MacBeth (FS-FMB) method for selecting the higher-order factors and their interactions that are most important for the cross-section of returns. The method proceeds sequentially, adding one factor or interaction to the selected set at a time and, at each step, choosing the term that maximizes the Fama–MacBeth (FMB) second-step cross-sectional R-squared. The main advantage of this approach is that it is a fully “glass box” model both in terms of determining the important factors and in the process to select them that allows to map features of the data to the economic factors and their higher order interactions.111111Conceptually, these higher-order interaction terms capture conditional moments, as in systemic-risk measures such as CoVaR (Adrian & Brunnermeier, [2016](https://arxiv.org/html/2510.14435v1#bib.bib5)) and marginal expected shortfall (Acharya et al., [2017](https://arxiv.org/html/2510.14435v1#bib.bib3)). See Bell et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib22)) for an alternative “glass box” machine learning structure.

Table [5](https://arxiv.org/html/2510.14435v1#S3.T5 "Table 5 ‣ 3.6 Fact 6: Few factors, higher orders—rather than machine learning: why less is more ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age"), Panel A, reports second-step FMB results for the crypto-CAPM, or C-1, model and for the C-4 model of Liu et al. ([2021](https://arxiv.org/html/2510.14435v1#bib.bib106)). The test assets are the set of 50 portfolios formed using the smart beta strategies described in Fact 4 (see Tables [2](https://arxiv.org/html/2510.14435v1#S3.T2 "Table 2 ‣ 3.4 Fact 4: How to be “smart” in crypto—crypto-size, crypto-momentum and crypto-value ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age") and [3](https://arxiv.org/html/2510.14435v1#S3.T3 "Table 3 ‣ 3.4 Fact 4: How to be “smart” in crypto—crypto-size, crypto-momentum and crypto-value ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age")), and the CARB strategy described in Fact 8 (see Table [6](https://arxiv.org/html/2510.14435v1#S3.T6 "Table 6 ‣ 3.8 Fact 8: Young cryptocurrency markets, old inefficiencies. ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age"), Panel B). As with the classic CAPM, the C-1 model cannot account for the cross-section of average returns. By contrast, the C-4 model explains 47.3% of the cross-sectional variation, and satisfies the restriction of a zero intercept.

Table [5](https://arxiv.org/html/2510.14435v1#S3.T5 "Table 5 ‣ 3.6 Fact 6: Few factors, higher orders—rather than machine learning: why less is more ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age"), Panel B, reports the result of a specification which augments the C-4 model with the single KA-factor based on the Kolmogorov-Arnold architecture of Borri et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib32)). One can think of this factor as a stand-in that captures a variety of different neural nets. The cross-sectional R-squared increases by approximately 25 pp, and the intercept is not statistically different from zero at standard levels.

Table [5](https://arxiv.org/html/2510.14435v1#S3.T5 "Table 5 ‣ 3.6 Fact 6: Few factors, higher orders—rather than machine learning: why less is more ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age"), Panel C, reports the results from the estimation of the FS-FMB (Borri et al. [2025](https://arxiv.org/html/2510.14435v1#bib.bib33)). At each step, we augment the C-4 by one additional higher-order factor (hjh\_{j}) which maximizes the adjusted cross-sectional R-squared. Higher-order factors include the squared and cubed of the factors in the C-4 model, as well their pair-wise interactions up to order three. The procedure selects three higher-order factors. The first is CMOM cubed, resulting in an increase of the cross-sectional R-squared of approximately 15 pp. The importance of this factor is that it relates to the frequent and large jumps which are the distinct feature of cryptocurrency of Fact 5. The second and third selected factors are CMKT squared and the interaction between CMKT and CSIZE. Borri et al. ([2025](https://arxiv.org/html/2510.14435v1#bib.bib33)) show that the equity counterparts of these factors are important for the cross-section of equity returns. The cross-sectional R-squared of the FS-FMB procedure is 70%, a value very similar to that of the model including the KA-factor. In all models, the estimate of the intercept is not statistically different from zero.

These results show that the FS–FMB procedure recovers essentially the same nonlinear structure as the KA single factor. Moreover, since KA can represent any neural net, FS–FMB provides a simple, transparent, “open box” alternative to black-box models that is directly connected to the economic structure of the model and to observables characteristics.121212This is similar in spirit to Nagel ([2025](https://arxiv.org/html/2510.14435v1#bib.bib117)), who shows that return prediction with random Fourier features—which can approximate neural-networks—collapses to a recency-weighted average of past returns, i.e., a momentum-style predictor. In short, rather than estimating a neural network (or studying a particular variant of the multitude of neural networks), one can estimate the FS–FMB specification and capture the relevant nonlinearities in a parsimonious and interpretable way without relying on millions of parameters.

Table 5: Cross-Sectional Performance

| Panel A: Baseline Models | | | | |
| --- | --- | --- | --- | --- |
| # | Model | Adj. R-squared | α\alpha | t-stat (α\alpha) |
| 1 | C-1 | 0.046 | 0.012 | 1.437 |
| 2 | C-4 | 0.473 | 0.005 | 0.766 |
| Panel B: KA model | | | | |
| # | Model | Adj. R-squared | α\alpha | t-stat (α\alpha) |
| 1 | C-4 & KA | 0.723 | 0.011 | 1.494 |
| Panel C: FS-FMB procedure | | | | |
| Step | hjh\_{j} | Adj. R-squared | α\alpha | t-stat (α\alpha) |
| 1 | CMOM3 | 0.623 | 0.002 | 0.235 |
| 2 | CMKT2 | 0.663 | -0.001 | -0.140 |
| 3 | CMKT ×\times CSIZE | 0.702 | 0.001 | 0.138 |

This table reports the results from the second step of the FMB method.
Panel A refers to baseline models: the crypto-CAPM (C-1) and the C-4 model of Liu et al. ([2022](https://arxiv.org/html/2510.14435v1#bib.bib107)). The table reports the adjusted cross-sectional R-squared,
the estimate for the intercept (α\alpha) and associated t-statistic.
The t-statistics is based on Newey-West corrected standard errors. Panel B refers to the C-4 model augmented by the single KA-factor, estimated with the KA procedure of Borri et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib32)).
Panel C refers to the FS-FMB procedure. At each step, we augment the
C-4 model by one additional higher-order factor (hjh\_{j}) which maximizes
the adjusted cross-sectional R-squared. The method stops when the
improvement in the R-squared in a given step is smaller than 1 pp.

### 3.7 Fact 7: In crypto, the (block)chain drives the gain

Fact 6: Blockchain economics and information significantly affects cryptocurrency prices, on-chain user adoption accounts for about 8% of the variation in cryptocurrency returns.

Network externalities are a fundamental concept in economics because they shape markets and influence competition, regulation and technology adoption. Classic work has analyzed how networks form and evolve (Jackson & Wolinsky, [1996](https://arxiv.org/html/2510.14435v1#bib.bib85)), how pricing and competition operate on networked platforms (Rochet & Tirole, [2003](https://arxiv.org/html/2510.14435v1#bib.bib121)), and how shocks propagate through financial networks (Allen & Gale, [2000](https://arxiv.org/html/2510.14435v1#bib.bib7)). A central question common in this work is information diffusion and learning in a network (Golub & Jackson [2010](https://arxiv.org/html/2510.14435v1#bib.bib70), Acemoglu et al. [2011](https://arxiv.org/html/2510.14435v1#bib.bib2)).

One of the defining features of blockchain and one of the important innovations that it delivers is that blockchains create a continuously updated, public, and verifiable record of economic activity. Blockchains provide an observable, real-time map of user adoption and economic interactions. This makes them particularly useful for studying how information absorption affects asset values. As Metcalfe’s law put it, “the value of a network grows as the square of the number of its users.”

Empirically, Liu et al. ([2021](https://arxiv.org/html/2510.14435v1#bib.bib106)) show that on-chain user adoption—measured as new user growth—has a statistically and economically significant effect on cryptocurrency prices. Importantly, this single on-chain variable accounts for about 8% of the variation in cryptocurrency returns. In time-series tests for the largest coins, on-chain user adoption alone can account for more than 10% of the variation in their returns.

Liu et al. ([2021](https://arxiv.org/html/2510.14435v1#bib.bib106)) also examine how markets absorb this information and what conditions amplify its relevance. Event-time evidence shows a sharp price reaction when weekly adoption information is realized, with muted pre-announcement behavior and no post-announcement drift—in contrast to equities. The result gives evidence that investors fully incorporate the information at the weekly frequency.

Lastly, Liu et al. ([2021](https://arxiv.org/html/2510.14435v1#bib.bib106)) show that the crypto value measure, constructed as the price-to-new-address ratio, negatively predicts cryptocurrency returns—a result we discuss in Fact 4.

### 3.8 Fact 8: Young cryptocurrency markets, old inefficiencies.

Fact 8: The young cryptocurrency markets are still inefficient. But the origins are canonical: market segmentation and restrictions on capital flows. Cross-exchange cryptocurrency “arbitrage” is no free lunch.

A central concept in finance is the law of one price—identical securities should sell for identical prices. The law of one price, and the related concept of absence of arbitrage, is important for the existence of a discount factor (Ross [1978](https://arxiv.org/html/2510.14435v1#bib.bib123), Harrison & Kreps [1979](https://arxiv.org/html/2510.14435v1#bib.bib76)). Deviations from the law of one price have been presented as proof of irrational investor behavior (Lamont & Thaler [2003](https://arxiv.org/html/2510.14435v1#bib.bib98)), limits to arbitrage and market segmentation (Shleifer & Vishny [1997](https://arxiv.org/html/2510.14435v1#bib.bib134)), or previously overlooked risks (Cochrane [2002](https://arxiv.org/html/2510.14435v1#bib.bib46)).

One of the main features of cryptocurrency is that it is possible to trade coins simultaneously on multiple exchanges and against a number of fiat and crypto pairs. For example, an investor could buy Bitcoin on Binance or Kraken, two prominent centralized exchanges, against fiat currencies such as the U.S. dollar or the euro, or even against another cryptocurrency such as Ethereum or Tether, a stablecoin.
Makarov & Schoar ([2020](https://arxiv.org/html/2510.14435v1#bib.bib111)) and Borri & Shakhnov ([2023](https://arxiv.org/html/2510.14435v1#bib.bib38)) document sizable, persistent deviations in the dollar price of Bitcoin across exchanges and across fiat- and crypto-quoted pairs. We revisit this evidence on updated data for 510 BTC–fiat pairs traded on 165 centralized exchanges in 49 currencies. Bitcoin price discounts are computed each week relative to the dollar price on Kraken (the benchmark exchange). All quotes are converted to U.S. dollars using daily spot FX rates. In the 2014–2025 sample, the 10th and 90th percentiles of Bitcoin price discounts are –1.8% and 3.7%, respectively. These figures remain virtually unchanged in the post-2020 period (–2.1% and 3.5%). Moreover, discounts are highly persistent, with a half-life of roughly 1.1 weeks in both samples. These deviations—classic examples of market inefficiency and violations of the law of one price—are results of market segmentation induced by capital controls and idiosyncratic domestic shocks that prevent arbitrage.131313Barbon & Ranaldo ([2021](https://arxiv.org/html/2510.14435v1#bib.bib17)) compare centralized and decentralized cryptocurrency exchanges along two key dimensions—market liquidity and price efficiency—and find that decentralized exchanges exhibit lower efficiency.

Table [6](https://arxiv.org/html/2510.14435v1#S3.T6 "Table 6 ‣ 3.8 Fact 8: Young cryptocurrency markets, old inefficiencies. ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age"), Panel A, reports the properties of an “arbitrage” (CARB) strategy that attempts to exploit these price discrepancies. Each week, we sort BTC–fiat pairs by their discount and form five portfolios. The CARB return for a given pair is defined by buying Bitcoin on Kraken in week tt and selling it on the target pair in week t+1t{+}1; portfolio returns are the simple average across constituent pairs. Using weekly formation and holding periods substantially alleviates execution and timing concerns. In practice, capital controls, withdrawal limits, transaction costs, settlement latency, and venue-specific frictions prevent the cross-market trades needed to enforce the law of one price. Not surprisingly, the mean excess returns are implausibly high—on the order of 68.5% per week over 2014–2025, rising to 95% per week from 2020 onward—precisely because the required arbitrage trades are blocked or prohibitively costly. Specifically, Borri & Shakhnov ([2022](https://arxiv.org/html/2510.14435v1#bib.bib37)) shows that this seemingly exceptional performance is concentrated in the extreme portfolio that holds pairs with the highest Bitcoin price relative to the benchmark quote, where segmentation and frictions are most severe. That is, the cryptocurrency market inefficiencies reflect the classic market segmentation and trading frictions as in Shleifer & Vishny ([1997](https://arxiv.org/html/2510.14435v1#bib.bib134)).

As Sophocles writes in *Antigone*, “Nothing vast enters the life of mortals without a curse.” Early cryptocurrency investors often told a different story: that outsized returns came from cross-exchange “arbitrage.” Public interviews with Sam Bankman-Fried—the founder of the now-defunct exchange FTX—describe how Alameda Research, a hedge fund he helped run, allegedly began by focusing on such trades.141414See, for example, Bloomberg’s coverage of the so-called Kimchi premium, which denotes the fact that it was more expensive to buy Bitcoin in Korean Won than in US dollars: <https://www.bloomberg.com/news/articles/2024-11-15/south-korea-crypto-boom-what-is-the-kimchi-premium>, and Lewis ([2023](https://arxiv.org/html/2510.14435v1#bib.bib101))’s book about Sam Bankman Fried. However, Borri & Shakhnov ([2022](https://arxiv.org/html/2510.14435v1#bib.bib37)) show that implementability is limited to a narrow set of highly liquid pairs on reputable cryptocurrency exchanges without binding capital controls.

We revisit the analysis in Borri & Shakhnov ([2022](https://arxiv.org/html/2510.14435v1#bib.bib37)) and construct the CARB strategy for 226 Bitcoin pairs, traded on 96 exchanges against 11 fiat currencies (Australian dollar, Canadian dollar, Danish krone, euro, Hong Kong dollar, Israeli shekel, Japanese yen, Polish łoty, Swiss franc, British pound, and U.S. dollar). These are the pairs that are realistically investable. Table [6](https://arxiv.org/html/2510.14435v1#S3.T6 "Table 6 ‣ 3.8 Fact 8: Young cryptocurrency markets, old inefficiencies. ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age"), Panel B, documents that excess returns remain statistically significant but are *orders of magnitude smaller*: the long–short weekly return declines from about 0.680.68 to roughly 0.0380.038 in the full sample, and measures around 0.0410.041 in the post-2020 sample. In other words, where the strategy is actually implementable, the apparent “free lunch” largely vanishes. These returns are not pure arbitrage—they are compensation for risk. Borri & Shakhnov ([2022](https://arxiv.org/html/2510.14435v1#bib.bib37)) show that the expensive pairs (those priced above the benchmark) are systematically *riskier*—they depreciate more in bad times for crypto-investors, when aggregate liquidity and sentiment are low.

The collapse of Alameda Research and the failure of FTX in November 2022—only a few months after the demise of the synthetic stablecoin ecosystem Terra–Luna described in Liu et al. ([2023](https://arxiv.org/html/2510.14435v1#bib.bib103)), is the most visible manifestation of the results described in this fact.

Table 6: Cryptocurrency “Arbitrage” Strategy

| Panel A: All exchanges | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
|  | Quintiles | | | | | |
|  | 1 | 2 | 3 | 4 | 5 | 5–1 |
|  | Full sample | | | | | |
| CARB | Low |  |  |  | High |  |
| Mean | -0.011\*\* | 0.009\* | 0.012\*\* | 0.017\*\*\* | 0.674\*\*\* | 0.685\*\*\* |
| tt(Mean) | (-2.22) | (1.73) | (2.43) | (3.38) | (4.39) | (4.46) |
|  | Post-2020 sample | | | | | |
| CARB | Low |  |  |  | High |  |
| Mean | -0.014\*\* | 0.006 | 0.010\* | 0.015\*\*\* | 0.940\*\*\* | 0.954\*\*\* |
| tt(Mean) | (-2.43) | (1.01) | (1.76) | (2.75) | (3.90) | (3.97) |
| Panel B: Exchanges in open markets | | | | | | |
|  | Quintiles | | | | | |
|  | 1 | 2 | 3 | 4 | 5 | 5–1 |
|  | Full sample | | | | | |
| CARB | Low |  |  |  | High |  |
| Mean | -0.002 | 0.007 | 0.010\* | 0.014\*\*\* | 0.036\*\*\* | 0.038\*\*\* |
| tt(Mean) | (-0.39) | (1.36) | (1.94) | (2.71) | (7.66) | (12.45) |
|  | Post-2020 sample | | | | | |
| CARB | Low |  |  |  | High |  |
| Mean | -0.008 | 0.005 | 0.008 | 0.012\*\* | 0.033\*\*\* | 0.041\*\*\* |
| tt(Mean) | (-1.36) | (0.75) | (1.26) | (2.13) | (6.06) | (9.90) |

Notes: This table reports the mean quintile portfolio returns and long-short portfolio return for the “arbitrage” (CARB) investment strategy that sorts Bitcoin trading pairs by their price deviation from a benchmark Bitcoin price on Kraken. Each week, pairs are sorted into five portfolios. The long-short portfolio is long portfolio 5 and short portfolio 1. The mean returns are the time-series averages of weekly equally-weighted portfolio excess returns. Panel A uses the full sample of 510 BTC–fiat pairs traded on 165 centralized exchanges in 49 currencies. Panel B restricts to 226 BTC–fiat pairs on 96 exchanges against 11 fiat currencies, which are the most liquid fiat currencies on the most reputable exchanges in jurisdictions with minimal capital controls as in Borri & Shakhnov ([2022](https://arxiv.org/html/2510.14435v1#bib.bib37)). The post-2020 sample is the sample since Jan 1, 2020. tt-statistics in parentheses are Newey-West adjusted. \*, \*\*, and \*\*\* denote significance at the 10%, 5% and 1% levels.

### 3.9 Fact 9: When the funding dries up, we finally learn the worth of futures

Fact 9: Cryptocurrency carry trade, the defining characteristics of the futures market, used to be highly profitable, but profitability has compressed sharply since 2024.

Derivatives are a cornerstone of modern markets, enabling hedging, leverage, and price discovery across equities, interest rates, and commodities (Black & Scholes [1973](https://arxiv.org/html/2510.14435v1#bib.bib30), Merton [1973](https://arxiv.org/html/2510.14435v1#bib.bib114), Black [1976](https://arxiv.org/html/2510.14435v1#bib.bib28)).

There is widespread usage of derivatives in the cryptocurrency market, albeit with novel designs. Among all derivatives, perpetual futures are the most common derivative contract in cryptocurrency markets. For example, Schmeling et al. ([2023](https://arxiv.org/html/2510.14435v1#bib.bib128)) document that perpetual futures account for more than 98% of the Bitcoin futures volume in their sample. Perpetuals, inspired by Shiller ([1993](https://arxiv.org/html/2510.14435v1#bib.bib133)), have no maturity; positions are marked to market (typically every 8 hours) and a funding rate—positive or negative by design—flows between longs and shorts to keep futures prices anchored to spot. Ackerer et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib4)) provides the theoretical foundations for the pricing of perpetual cryptocurrency futures. The crypto-carry trade strategy of Schmeling et al. ([2023](https://arxiv.org/html/2510.14435v1#bib.bib128)) is short a perpetual futures contract and long a position in the corresponding spot market.

Figure [2](https://arxiv.org/html/2510.14435v1#S3.F2 "Figure 2 ‣ 3.9 Fact 9: When the funding dries up, we finally learn the worth of futures ‣ 3 THE TEN FACTS OF CRYPTOCURRENCY ‣ Cryptocurrency as an Investable Asset Class: Coming of Age") plots the evolution over time of one dollar invested in the crypto-carry strategy (black line, left y-axis) and in the spot Bitcoin market (red line, right y-axis). Over the full sample, which goes from 2020 to 2025, the annualized Sharpe ratio of the cryptocurrency carry is 6.45. Beginning in 2024, the Sharpe ratio falls to 4.06, and it turns negative in 2025. The profit from the cryptocurrency carry strategy is mostly driven by the funding rate, which in the full sample has a mean return of approximately 8% with a low volatility of 0.8%.

This shift in the profitability of the crypto-carry trade strategy has important implications for the crypto-industry. A growing set of crypto “yield” products—most prominently delta-neutral, funding-rate-harvesting structures (e.g., synthetic dollar projects that combine spot holdings with short perpetuals)—derive an important part of their returns from the funding rate. A prominent example is Ethena.fi, whose stablecoin uses a delta-neutral construction and relies on perpetual-funding payments. As of September 2025, Ethena’s stablecoin reached a market capitalization of about $14 billion, with its governance token ENA valued at around $4 billion. If funding premia compress or become more volatile, the economics of these strategies deteriorate and the expected yields decline. The lower profitability of the crypto-carry trade shows that funding-rate premia are neither guaranteed nor permanent and, even more importantly, raises difficult questions about the long-run sustainability of yield products built on them.

![Refer to caption](x3.png)

Figure 2: Carry Trade Cumulative Returns

The figure plots the cumulative returns from Tether Carry Trades (left axis) and from a long buy-and-hold strategy in Bitcoin (right axis). The Carry Trade is defined as in Schmeling et al. ([2023](https://arxiv.org/html/2510.14435v1#bib.bib128)). The sample goes from August 1, 2020 to May 31, 2025.

### 3.10 Fact 10: Growing up with supervision—regulation and oversight strengthen cryptocurrency markets

Fact 10: As the market matures, there is growing disclosure and transparency in cryptocurrencies.

A fundamental insight of information economics is that markets with asymmetric information can fail to allocate resources efficiently. When one party possesses superior information, such as inside information, prices may deviate from fundamentals, and capital may be misallocated (e.g., Akerlof [1970](https://arxiv.org/html/2510.14435v1#bib.bib6)). Accounting research builds directly on this and shows how disclosure, regulation, and intermediaries can reduce these frictions (Verrecchia [1983](https://arxiv.org/html/2510.14435v1#bib.bib142), Dye [1985](https://arxiv.org/html/2510.14435v1#bib.bib56), Healy & Palepu [2001](https://arxiv.org/html/2510.14435v1#bib.bib77), Verrecchia [2001](https://arxiv.org/html/2510.14435v1#bib.bib143)). However, in the absence of regulation and supervision, managers may strategically disclose for private benefits (Verrecchia [2001](https://arxiv.org/html/2510.14435v1#bib.bib143), Ma & Shleifer [2025](https://arxiv.org/html/2510.14435v1#bib.bib109)). Policymakers thus issue regulations to address these inefficiencies and to produce credible, comparable, and decision-useful information. Intermediaries, such as analysts and auditors, emerge to reduce information asymmetry by analyzing and validating information (Watts & Zimmerman [1983](https://arxiv.org/html/2510.14435v1#bib.bib146)).

Information asymmetry remains pervasive in cryptocurrency markets, though regulation and disclosure have increased in recent years. On the corporate side, public firms with material cryptocurrency exposure are now required to disclose their cryptocurrency holdings and risks. Importantly, the introduction of Accounting Standards Update (ASU) 2023-08 by the Financial Accounting Standards Board provides a coherent framework for the accounting of crypto-assets, which formally requires fair-value accounting treatment (FASB [2023](https://arxiv.org/html/2510.14435v1#bib.bib60)). Recent accounting research emphasizes measurement reliability and disclosure consistency for digital assets (Anderson et al. [2025](https://arxiv.org/html/2510.14435v1#bib.bib10)).

On the cryptocurrency side, voluntary disclosures, such as whitepapers and social media announcements, have become increasingly common (e.g., George & Patatoukas [2021](https://arxiv.org/html/2510.14435v1#bib.bib66), Liu et al. [2025](https://arxiv.org/html/2510.14435v1#bib.bib104), Du et al. [2025](https://arxiv.org/html/2510.14435v1#bib.bib54)). Howell et al. ([2020](https://arxiv.org/html/2510.14435v1#bib.bib83)) and Bourveau et al. ([2022](https://arxiv.org/html/2510.14435v1#bib.bib40)) show the importance of voluntary disclosures in the initial coin offering stage. Studies also examine information intermediaries (e.g., analysts and auditors) and find that they play an important role in this market (e.g., Bourveau et al. [2022](https://arxiv.org/html/2510.14435v1#bib.bib40), Bourveau et al. [2024](https://arxiv.org/html/2510.14435v1#bib.bib39)).

In July 2025, Congress enacted the Guiding and Establishing National Innovation for U.S. Stablecoins Act (GENIUS Act), the first comprehensive federal framework for digital asset oversight in the United States. The Act focuses primarily on payment stablecoins, aiming to improve their transparency and stability. It mandates monthly public disclosures of reserve compositions of stablecoins, and explicitly prohibits stablecoin companies from making misleading claims that their tokens are backed by the U.S. government, federally insured, or legal tender.

The recent regulations and market developments show that greater transparency in the cryptocurrency space is not only increasingly required by the regulators but is also valued by the market. The cryptocurrency market is starting to increasingly implement and value more rigorous accounting principles and slowly converging to the accounting practices of traditional asset classes, for which reliable, comparable, and verifiable disclosure is a major and perhaps the most important determinant of investor confidence and growth of an asset class.

## 4 ADDITIONAL DISCUSSIONS

The ten facts summarize key developments in cryptocurrencies through the lens of empirical asset pricing. In this section, we provide additional discussions on emerging topics, including retail investor trading in the cryptocurrency market, the non-fungible token market, and studies on the dark side of cryptocurrency usage.

Recent research increasingly examines individual investor beliefs and behavior in cryptocurrency markets and compares and contrast them with those in traditional investments. Kogan et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib93)) show that the trading behaviors of retail investors are drastically different between cryptocurrencies and traditional assets, such as stocks and gold. In particular, retail investors are contrarian in stocks and gold, but trend-chasing in cryptocurrencies. Kogan et al. ([2024](https://arxiv.org/html/2510.14435v1#bib.bib93)) conjecture that the trend-chasing behavior is due to cryptocurrency price changes affecting the likelihood of future widespread adoption, which leads retail investors to update their price expectations. Chan et al. ([2020](https://arxiv.org/html/2510.14435v1#bib.bib44)) use data from a medium-sized cryptocurrency exchange and document that investor portfolios are typically small in value, highly concentrated in a few coins, and characterized by short holding periods. Weber et al. ([2023](https://arxiv.org/html/2510.14435v1#bib.bib147)) complement this evidence using repeated large-scale surveys of U.S. households, showing that cryptocurrency investors differ systematically from other investors. Alvarez et al. ([2023](https://arxiv.org/html/2510.14435v1#bib.bib8)) provide complementary evidence on the use of cryptocurrencies as a means of payment, using the case of El Salvador—where Bitcoin was made legal tender—and show that privacy and security concerns remain key barriers to adoption. Han et al. ([2023](https://arxiv.org/html/2510.14435v1#bib.bib75)) study how social interactions and sentiments affect retail investor trading in cryptocurrency markets. Finally, Benetton & Compiani ([2024](https://arxiv.org/html/2510.14435v1#bib.bib23)) incorporate individual-level survey data into a structural characteristics-based demand model where investors can hold cryptocurrencies. They find that individual beliefs of cryptocurrency are different and are critical in explaining cryptocurrency valuation.

The bulk of this review is about fungible tokens. A significant segment of the cryptocurrency market, however, is non-fungible tokens (NFTs). Goetzmann & Nozari ([2022](https://arxiv.org/html/2510.14435v1#bib.bib68)) is the first to construct repeated sales return indices of NFTs and examine their properties. Borri et al. ([2022a](https://arxiv.org/html/2510.14435v1#bib.bib34)) provide a comprehensive analysis of the NFT market. They highlight the importance of visual features in cryptocurrency valuation and how it leads to a conspicuous consumption effect in the market. Furthermore, Borri et al. ([2022a](https://arxiv.org/html/2510.14435v1#bib.bib34)) shows that, due to the high non-fungibility of NFTs, the market is highly segmented, which has implications for returns and investor behaviors in the market. Huang & Goetzmann ([2023](https://arxiv.org/html/2510.14435v1#bib.bib84)) document that behavioral biases—such as selection neglect and extrapolative beliefs—play a significant role in NFT pricing. Oh et al. ([2025](https://arxiv.org/html/2510.14435v1#bib.bib119)) document preference-driven herding in NFT primary market sales.

A stream of work examines the so-called dark side of cryptocurrencies, especially in the early years. Foley et al. ([2019](https://arxiv.org/html/2510.14435v1#bib.bib64)) argue that in the early days, the majority of Bitcoin transactions were about illegal activities, but this is recently challenged by Makarov & Schoar ([2021](https://arxiv.org/html/2510.14435v1#bib.bib112)) that show the results of Foley et al. ([2019](https://arxiv.org/html/2510.14435v1#bib.bib64)) are largely driven by double-counting. Griffin & Shams ([2020](https://arxiv.org/html/2510.14435v1#bib.bib73)) analyze blockchain and market data to argue that Tether flows timed after market downturns are associated with large Bitcoin price increases during the 2017 boom, consistent with price manipulation. Amiram et al. ([2022](https://arxiv.org/html/2510.14435v1#bib.bib9)) show that abnormal spikes in on-chain transfers around major terrorist attacks carry predictive power for attack timing and highlight chokepoints visible in public ledgers, and Cong et al. ([2025](https://arxiv.org/html/2510.14435v1#bib.bib51)) provide an anatomy of crypto-enabled crimes. Li et al. ([2025](https://arxiv.org/html/2510.14435v1#bib.bib102)) document pervasive cryptocurrency pump-and-dump episodes that generate brief surges in prices, volume, and volatility followed by rapid reversals, with pre-event run-ups consistent with insider gains at outsiders’ expense.

## 5 CONCLUSIONS

In the 16 years since Nakamoto, cryptocurrencies have reached a certain stage of maturity: they can now be studied using the same measurement, data quality, and research rigor applied to other asset classes. The market is now worth more than four trillion dollars. Major financial firms are using cryptocurrency in their businesses.

We show that there are important similarities between cryptocurrency markets and traditional asset markets—Sharpe ratios are broadly comparable, and a small number of factors and their higher orders summarize the cross-section of returns. On the other hand, cryptocurrency also has its own character—frequent jumps and blockchain information driving prices. The cryptocurrency market has become more mature and is emerging as an asset class with its own distinct characteristics that still, however, needs more data, research, supervision, enforcement, and a better legal and regulatory framework.

Given the maturation of cryptocurrency into an asset class, this review shows that cryptocurrency should be studied the same way we study any asset. The right way to understand it is exactly through traditional finance tools—empirical asset pricing. The ten facts we present summarize the key takeaways from this view.

## DISCLOSURE STATEMENT

The authors are not aware of any affiliations, memberships, funding, or financial holdings that might be perceived as affecting the objectivity of this review. This review is for academic purposes only and should not be construed as investment or legal advice.

## References

* Abadi & Brunnermeier (2018)

  Abadi J, Brunnermeier M. 2018.
  Blockchain economics.
  Tech. rep., National Bureau of Economic Research
* Acemoglu et al. (2011)

  Acemoglu D, Dahleh MA, Lobel I, Ozdaglar A. 2011.
  Bayesian learning in social networks.
  The Review of Economic Studies 78(4):1201–1236
* Acharya et al. (2017)

  Acharya VV, Pedersen LH, Philippon T, Richardson M. 2017.
  Measuring systemic risk.
  The Review of Financial Studies 30(1):2–47
* Ackerer et al. (2024)

  Ackerer D, Hugonnier J, Jermann U. 2024.
  Perpetual futures pricing.
  Wharton Working Paper Series
* Adrian & Brunnermeier (2016)

  Adrian T, Brunnermeier MK. 2016.
  Covar.
  The American Economic Review 106(7):1705
* Akerlof (1970)

  Akerlof GA. 1970.
  The market for “lemons”: Quality uncertainty and the market mechanism.
  The Quarterly Journal of Economics 84(3):488–500
* Allen & Gale (2000)

  Allen F, Gale D. 2000.
  Financial contagion.
  Journal of Political Economy 108(1):1–33
* Alvarez et al. (2023)

  Alvarez F, Argente D, Van Patten D. 2023.
  Are cryptocurrencies currencies? Bitcoin as legal tender in El Salvador.
  Science 382(6677)
* Amiram et al. (2022)

  Amiram D, Jørgensen BN, Rabetti D. 2022.
  Coins for bombs: The predictive ability of on-chain transfers for terrorist
  attacks.
  Journal of Accounting Research 60(2):427–466
* Anderson et al. (2025)

  Anderson CM, Fang VW, Moon Jr JR, Shipman JE. 2025.
  Accounting for cryptocurrencies.
  Journal of Accounting Research
* Ang et al. (2023)

  Ang A, Morris T, et al. 2023.
  Asset allocation with crypto: Application of preferences for positive skewness.
  The Journal of Alternative Investments, Spring 25(4):7–28
* Arnold (1957)

  Arnold V. 1957.
  On functions of three variables.
  Proceedings of the USSR Academy of Sciences 114:679–681
* Asness et al. (2013)

  Asness CS, Moskowitz TJ, Pedersen LH. 2013.
  Value and momentum everywhere.
  The Journal of Finance 68(3):929–985
* Athey et al. (2016)

  Athey S, Parashkevov I, Sarukkai V, Xia J. 2016.
  Bitcoin pricing, adoption, and usage: Theory and evidence
* Auer et al. (2022)

  Auer R, Frost J, Gambacorta L, Monnet C, Rice T, Shin HS. 2022.
  Central bank digital currencies: motives, economic implications, and the
  research frontier.
  Annual Review of Economics 14(1):697–721
* Auer et al. (2025)

  Auer R, Monnet C, Shin HS. 2025.
  Distributed ledgers and the governance of money.
  Journal of Financial Economics 167:104026
* Barbon & Ranaldo (2021)

  Barbon A, Ranaldo A. 2021.
  On the quality of cryptocurrency markets: Centralized versus decentralized
  exchanges.
  arXiv preprint arXiv:2112.07386
* Barndorff-Nielsen & Shephard (2002)

  Barndorff-Nielsen OE, Shephard N. 2002.
  Econometric analysis of realized volatility and its use in estimating
  stochastic volatility models.
  Journal of the Royal Statistical Society Series B: Statistical
  Methodology 64(2):253–280
* Barndorff-Nielsen & Shephard (2006)

  Barndorff-Nielsen OE, Shephard N. 2006.
  Econometrics of testing for jumps in financial economics using bipower
  variation.
  Journal of Financial Econometrics 4(1):1–30
* Barro (2006)

  Barro RJ. 2006.
  Rare disasters and asset markets in the twentieth century.
  The Quarterly Journal of Economics 121(3):823–866
* Basu et al. (2023)

  Basu S, Easley D, O’Hara M, Sirer EG. 2023.
  Stablefees: A predictable fee market for cryptocurrencies.
  Management Science 69(11):6508–6524
* Bell et al. (2024)

  Bell S, Kakhbod A, Lettau M, Nazemi A. 2024.
  Glass box machine learning and corporate bond returns.
  University of California Berkeley Working Paper Series
* Benetton & Compiani (2024)

  Benetton M, Compiani G. 2024.
  Investors’ beliefs and cryptocurrency prices.
  Review of Asset Pricing Studies 14(2):197–236
* Benigno et al. (2022)

  Benigno P, Schilling LM, Uhlig H. 2022.
  Cryptocurrencies, currency competition, and the impossible trinity.
  Journal of International Economics 136:103601
* Biais et al. (2019)

  Biais B, Bisiere C, Bouvard M, Casamatta C. 2019.
  The blockchain folk theorem.
  The Review of Financial Studies 32(5):1662–1715
* Biais et al. (2023)

  Biais B, Bisiere C, Bouvard M, Casamatta C, Menkveld AJ. 2023.
  Equilibrium Bitcoin pricing.
  The Journal of Finance 78(2):967–1014
* Bianchi et al. (2022)

  Bianchi D, Babiak M, Dickerson A. 2022.
  Trading volume and liquidity provision in cryptocurrency markets.
  Journal of Banking & Finance 142:106547
* Black (1976)

  Black F. 1976.
  The pricing of commodity contracts.
  Journal of Financial Economics 3(1-2):167–179
* Black & Litterman (1990)

  Black F, Litterman R. 1990.
  Asset allocation: combining investor views with market equilibrium.
  Goldman Sachs Fixed Income Research 115(1):7–18
* Black & Scholes (1973)

  Black F, Scholes M. 1973.
  The pricing of options and corporate liabilities.
  Journal of Political Economy 81(3):637–654
* Borri (2019)

  Borri N. 2019.
  Conditional tail-risk in cryptocurrency markets.
  Journal of Empirical Finance 50:1–19
* Borri et al. (2024)

  Borri N, Chetverikov D, Liu Y, Tsyvinski A. 2024.
  One factor to bind the cross-section of returns.
  arXiv preprint arXiv:2404.08129 (11 Apr 2024)
* Borri et al. (2025)

  Borri N, Chetverikov D, Liu Y, Tsyvinski A. 2025.
  Forward selection Fama-MacBeth regression with higher order asset-pricing
  factors.
  Yale Working Paper Series
* Borri et al. (2022a)

  Borri N, Liu Y, Tsyvinski A, Wu X. 2022a.
  The economics of non-fungible tokens.
  Available at SSRN 4052045
* Borri et al. (2022b)

  Borri N, Massacci D, Rubin M, Ruzzi D. 2022b.
  Crypto risk premia.
  Available at SSRN 4154627
* Borri & Santucci de Magistris (2022)

  Borri N, Santucci de Magistris P. 2022.
  Crypto premium, higher-order moments and tail risk.
  Available at SSRN 3889169
* Borri & Shakhnov (2022)

  Borri N, Shakhnov K. 2022.
  The cross-section of cryptocurrency returns.
  The Review of Asset Pricing Studies 12(3):667–705
* Borri & Shakhnov (2023)

  Borri N, Shakhnov K. 2023.
  Cryptomarket discounts.
  Journal of International Money and Finance 139:102963
* Bourveau et al. (2024)

  Bourveau T, Brendel J, Schoenfeld J. 2024.
  Decentralized finance (defi) assurance: early evidence.
  Review of Accounting Studies 29(3):2209–2253
* Bourveau et al. (2022)

  Bourveau T, De George ET, Ellahie A, Macciocchi D. 2022.
  The role of disclosure and information intermediaries in an unregulated capital
  market: Evidence from initial coin offerings.
  Journal of Accounting Research 60(1):129–167
* Brunnermeier et al. (2019)

  Brunnermeier MK, James H, Landau JP. 2019.
  The digitalization of money.
  Tech. rep., National Bureau of Economic Research
* Capponi et al. (2025)

  Capponi A, Jia R, Wang KY. 2025.
  Maximal extractable value and allocative inefficiencies in public blockchains.
  Journal of Financial Economics 172:104132
* Carhart (1997)

  Carhart MM. 1997.
  On persistence in mutual fund performance.
  The Journal of Finance 52(1):57–82
* Chan et al. (2020)

  Chan Q, Ding W, Lin C, Rossi AG. 2020.
  An inside look into cryptocurrency exchanges.
  Available at SSRN 3759062
* Chetverikov et al. (Forthcoming)

  Chetverikov D, Liu Y, Tsyvinski A. Forthcoming.
  Weighted-average quantile regression.
  Journal of Econometrics
* Cochrane (2002)

  Cochrane JH. 2002.
  Stocks as money: convenience yield and the tech-stock bubble
* Cong & He (2019)

  Cong LW, He Z. 2019.
  Blockchain disruption and smart contracts.
  The Review of Financial Studies 32(5):1754–1797
* Cong et al. (2021a)

  Cong LW, He Z, Li J. 2021a.
  Decentralized mining in centralized pools.
  The Review of Financial Studies 34(3):1191–1235
* Cong et al. (2021b)

  Cong LW, Li Y, Wang N. 2021b.
  Tokenomics: Dynamic adoption and valuation.
  The Review of Financial Studies 34(3):1105–1155
* Cong et al. (2022)

  Cong LW, Li Y, Wang N. 2022.
  Token-based platform finance.
  Journal of Financial Economics 144(3):972–991
* Cong et al. (2025)

  Cong W, Harvey C, Rabetti D, Wu ZY. 2025.
  An anatomy of crypto-enabled cybercrimes.
  Management Science 71(4):3622–3633
* Cybenko (1989)

  Cybenko G. 1989.
  Approximation by superpositions of a sigmoidal function.
  Mathematics of Control, Signals and Systems 2(4):303–314
* Dong et al. (2023)

  Dong S, Fang VW, Lin W. 2023.
  Tracing contagion risk: From crypto or stock?
  Available at SSRN 4371403
* Du et al. (2025)

  Du K, Huang Y, Wu X. 2025.
  Voluntary disclosures in cryptocurrency market.
  Berkeley Working Paper Series
* Duchin et al. (2025)

  Duchin R, Solomon DH, Tu J, Wang X. 2025.
  The cryptocurrency elephant in the room.
  Review of Finance :rfaf037
* Dye (1985)

  Dye RA. 1985.
  Disclosure of nonproprietary information.
  Journal of Accounting Research :123–145
* Easley et al. (2019)

  Easley D, O’Hara M, Basu S. 2019.
  From mining to markets: The evolution of Bitcoin transaction fees.
  Journal of Financial Economics 134(1):91–109
* Easley et al. (2024)

  Easley D, O’Hara M, Yang S, Zhang Z. 2024.
  Microstructure and market dynamics in crypto markets.
  Cornell Working Paper Series
* Fama & French (1992)

  Fama EF, French KR. 1992.
  The cross-section of expected stock returns.
  The Journal of Finance 47(2):427–465
* FASB (2023)

  FASB. 2023.
  Accounting standards update no. 2023-08: Accounting for and disclosure of
  crypto assets.
  Tech. rep., Financial Accounting Standards Board.
  Issued December 2023
* Feng et al. (2020)

  Feng G, Giglio S, Xiu D. 2020.
  Taming the factor zoo: A test of new factors.
  Journal of Finance LXXV:1327–1370
* Fernández-Villaverde & Sanches (2018)

  Fernández-Villaverde J, Sanches DR. 2018.
  On the economics of digital currencies
* Fieberg et al. (2024)

  Fieberg C, Günther S, Poddig T, Zaremba A. 2024.
  Non-standard errors in the cryptocurrency world.
  International Review of Financial Analysis 92:103106
* Foley et al. (2019)

  Foley S, Karlsen JR, Putniņš TJ. 2019.
  Sex, drugs, and Bitcoin: How much illegal activity is financed through
  cryptocurrencies?
  The Review of Financial Studies 32(5):1798–1853
* Friedman (1968)

  Friedman M. 1968.
  The role of monetary policy.
  The American Economic Review 58(1):1–17
* George & Patatoukas (2021)

  George K, Patatoukas PN. 2021.
  The blockchain evolution and revolution of accounting. In Information
  for efficient decision making: Big data, blockchain and relevance. World
  Scientific, 157–172
* Girosi & Poggio (1989)

  Girosi F, Poggio T. 1989.
  Representation properties of networks: Kolmogorov’s theorem is irrelevant.
  Neural Computation 1(4):465–469
* Goetzmann & Nozari (2022)

  Goetzmann W, Nozari M. 2022.
  Non-fungible tokens
* Goldstein et al. (2024)

  Goldstein I, Gupta D, Sverchkov R. 2024.
  Utility tokens as a commitment to competition.
  The Journal of Finance 79(6):4197–4246
* Golub & Jackson (2010)

  Golub B, Jackson MO. 2010.
  Naive learning in social networks and the wisdom of crowds.
  American Economic Journal: Microeconomics 2(1):112–149
* Gorton & Pennacchi (1990)

  Gorton G, Pennacchi G. 1990.
  Financial intermediaries and liquidity creation.
  The Journal of Finance 45(1):49–71
* Green & Zhou (1998)

  Green EJ, Zhou R. 1998.
  A rudimentary random-matching model with divisible money and prices.
  Journal of Economic Theory 81(2):252–271
* Griffin & Shams (2020)

  Griffin JM, Shams A. 2020.
  Is Bitcoin really untethered?
  The Journal of Finance 75(4):1913–1964
* Gu et al. (2020)

  Gu S, Kelly B, Xiu D. 2020.
  Empirical asset pricing via machine learning.
  The Review of Financial Studies 33(5):2223–2273
* Han et al. (2023)

  Han B, Liu H, Sui P. 2023.
  Social learning and sentiment contagion in the bitcoin market.
  University of Toronto Working Paper Series
* Harrison & Kreps (1979)

  Harrison JM, Kreps DM. 1979.
  Martingales and arbitrage in multiperiod securities markets.
  Journal of Economic theory 20(3):381–408
* Healy & Palepu (2001)

  Healy PM, Palepu KG. 2001.
  Information asymmetry, corporate disclosure, and the capital markets: A review
  of the empirical disclosure literature.
  Journal of accounting and economics 31(1-3):405–440
* Hecht-Nielsen (1987)

  Hecht-Nielsen R. 1987.
  Kolmogorov’s mapping neural network existence theorem, In Proceedings
  of the international conference on Neural Networks, vol. 3, pp. 11–14,
  IEEE press New York, NY, USA
* Hilt (2014)

  Hilt E. 2014.
  Corporate governance and the development of manufacturing enterprises in
  nineteenth-century massachusetts.
  Tech. rep., National Bureau of Economic Research
* Holmström & Tirole (1998)

  Holmström B, Tirole J. 1998.
  Private and public supply of liquidity.
  Journal of Political Economy 106(1):1–40
* Hornik et al. (1989)

  Hornik K, Stinchcombe M, White H. 1989.
  Multilayer feedforward networks are universal approximators.
  Neural networks 2(5):359–366
* Horowitz & Mammen (2007)

  Horowitz JL, Mammen E. 2007.
  Rate-optimal estimation for a general class of nonparametric regression models
  with unknown link functions.
  The Annals of Statistics :2589–2619
* Howell et al. (2020)

  Howell ST, Niessner M, Yermack D. 2020.
  Initial coin offerings: Financing growth with cryptocurrency token sales.
  The Review of Financial Studies 33(9):3925–3974
* Huang & Goetzmann (2023)

  Huang D, Goetzmann WN. 2023.
  Selection-neglect in the NFT bubble.
  Yale Working Paper Series
* Jackson & Wolinsky (1996)

  Jackson MO, Wolinsky A. 1996.
  A strategic model of social and economic networks.
  Journal of economic theory 71(1):44–74
* Jermann & Xiang (2025)

  Jermann U, Xiang H. 2025.
  Tokenomics: Optimal monetary and fee policies.
  Journal of Monetary Economics :103808
* Jiang et al. (2025)

  Jiang X, Kang W, Tang K, Yang E. 2025.
  Financialization in the cryptocurrency market.
  Tsyinghua University Working Paper Series
* Kareken & Wallace (1981)

  Kareken J, Wallace N. 1981.
  On the indeterminacy of equilibrium exchange rates.
  The Quarterly Journal of Economics 96(2):207–222
* Kelly et al. (2024)

  Kelly B, Malamud S, Zhou K. 2024.
  The virtue of complexity in return prediction.
  The Journal of Finance 79(1):459–503
* Kiyotaki & Wright (1989)

  Kiyotaki N, Wright R. 1989.
  On money as a medium of exchange.
  Journal of Political Economy 97(4):927–954
* Kocherlakota (1998)

  Kocherlakota NR. 1998.
  Money is memory.
  Journal of Economic Theory 81(2):232–251
* Kogan et al. (2022)

  Kogan L, Fanti G, Viswanath P. 2022.
  Economics of proof-of-stake payment systems.
  MIT Sloan Research Paper
* Kogan et al. (2024)

  Kogan S, Makarov I, Niessner M, Schoar A. 2024.
  Are cryptos different? evidence from retail trading.
  Journal of Financial Economics 159:103897
* Kolmogorov (1956)

  Kolmogorov A. 1956.
  On the representation of continuous functions of seversal variables by
  superpositions of continuous functions of a smaller number of variables.
  Proceedings of the USSR Academy of Sciences 108:179–182
* Kozak et al. (2020)

  Kozak S, Nagel S, Santosh S. 2020.
  Shrinking the cross-section.
  Journal of Financial Economics 135(2):271–292
* Kurkova (1991)

  Kurkova V. 1991.
  Kolmogorov’s theorem is relevant.
  Neural Computation 3(4):617–622
* Lagos & Wright (2005)

  Lagos R, Wright R. 2005.
  A unified framework for monetary theory and policy analysis.
  Journal of Political Economy 113(3):463–484
* Lamont & Thaler (2003)

  Lamont OA, Thaler RH. 2003.
  Can the market add and subtract? mispricing in tech stock carve-outs.
  Journal of Political Economy 111(2):227–268
* Leshno & Strack (2020)

  Leshno JD, Strack P. 2020.
  Bitcoin: An axiomatic approach and an impossibility theorem.
  American Economic Review: Insights 2(3):269–286
* Lewis (2010)

  Lewis M. 2010.
  Liar’s poker.
  WW Norton & Company
* Lewis (2023)

  Lewis M. 2023.
  Going infinite: The rise and fall of a new tycoon.
  Random House
* Li et al. (2025)

  Li T, Shin D, Wang B. 2025.
  Cryptocurrency pump-and-dump schemes.
  Journal of Financial and Quantitative Analysis
* Liu et al. (2023)

  Liu J, Makarov I, Schoar A. 2023.
  Anatomy of a run: The terra luna crash.
  Tech. rep., National Bureau of Economic Research
* Liu et al. (2025)

  Liu Y, Sheng J, Wang W. 2025.
  How do investors value technology in cryptocurrency? Evidence from textual
  analysis.
  University of Rochester Working Paper Series
* Liu & Tsyvinski (2021)

  Liu Y, Tsyvinski A. 2021.
  Risks and returns of cryptocurrency.
  The Review of Financial Studies 34(6):2689–2727
* Liu et al. (2021)

  Liu Y, Tsyvinski A, Wu X. 2021.
  Accounting for cryptocurrency value.
  Available at SSRN 3951514
* Liu et al. (2022)

  Liu Y, Tsyvinski A, Wu X. 2022.
  Common risk factors in cryptocurrency.
  The Journal of Finance 77(2):1133–1177
* Liu et al. (2024)

  Liu Z, Wang Y, Vaidya S, Ruehle F, Halverson J, et al. 2024.
  Kan: Kolmogorov-arnold networks.
  arXiv preprint arXiv:2404.19756 (30 Apr 2024)
* Ma & Shleifer (2025)

  Ma Y, Shleifer A. 2025.
  The invention of corporate governance.
  Journal of Financial Economics :104115
* Ma et al. (2025)

  Ma Y, Zeng Y, Zhang AL. 2025.
  Stablecoin runs and the centralization of arbitrage.
  Tech. rep., National Bureau of Economic Research
* Makarov & Schoar (2020)

  Makarov I, Schoar A. 2020.
  Trading and arbitrage in cryptocurrency markets.
  Journal of Financial Economics 135(2):293–319
* Makarov & Schoar (2021)

  Makarov I, Schoar A. 2021.
  Blockchain analysis of the Bitcoin market.
  Available at SSRN 3942181
* Markowitz (1952)

  Markowitz H. 1952.
  Portfolio selection.
  Journal of Finance 7(1):77–91
* Merton (1973)

  Merton RC. 1973.
  Theory of rational option pricing.
  The Bell Journal of Economics and Management Science 4(1):141–183
* Merton (1976)

  Merton RC. 1976.
  Option pricing when underlying stock returns are discontinuous.
  Journal of Financial Economics 3(1-2):125–144
* Nagel (2021)

  Nagel S. 2021.
  Machine learning in asset pricing.
  Princeton University Press
* Nagel (2025)

  Nagel S. 2025.
  Seemingly virtuous complexity in return prediction.
  NBER Working Paper 34104, National Bureau of Economic Research
* Nakamoto (2008)

  Nakamoto S. 2008.
  Bitcoin: A peer-to-peer electronic cash system
* Oh et al. (2025)

  Oh S, Rosen S, Zhang AL. 2025.
  Preference-driven herding in the market for non-fungible tokens
* Rietz (1988)

  Rietz TA. 1988.
  The equity risk premium a solution.
  Journal of Monetary Economics 22(1):117–131
* Rochet & Tirole (2003)

  Rochet JC, Tirole J. 2003.
  Platform competition in two-sided markets.
  Journal of the European Economic Association 1(4):990–1029
* Rogoff & You (2023)

  Rogoff K, You Y. 2023.
  Redeemable platform currencies.
  The Review of Economic Studies 90(2):975–1008
* Ross (1978)

  Ross SA. 1978.
  A simple approach to the valuation of risky streams.
  Journal of business :453–475
* Sargent (2019)

  Sargent TJ. 2019.
  Commodity and token monies.
  The Economic Journal 129(619):1457–1476
* Sargent & Wallace (1983)

  Sargent TJ, Wallace M. 1983.
  A model of commodity money.
  Journal of Monetary Economics 12(1):163–187
* Scaillet et al. (2020)

  Scaillet O, Treccani A, Trevisan C. 2020.
  High-frequency jump analysis of the Bitcoin market.
  Journal of Financial Econometrics 18(2):209–232
* Schilling et al. (2024)

  Schilling L, Fernández-Villaverde J, Uhlig H. 2024.
  Central bank digital currency: When price and bank stability collide.
  Journal of Monetary Economics 145:103554
* Schmeling et al. (2023)

  Schmeling M, Schrimpf A, Todorov K. 2023.
  Crypto carry.
  Available at SSRN 4268371
* Schmidt-Hieber (2021)

  Schmidt-Hieber J. 2021.
  The kolmogorov–arnold representation theorem revisited.
  Neural networks 137:119–126
* Sharpe (1966)

  Sharpe WF. 1966.
  Mutual fund performance.
  The Journal of Business 39(1):119–138
* Shi (1995)

  Shi S. 1995.
  Money and prices: a model of search and bargaining.
  Journal of Economic Theory 67(2):467–496
* Shiller (1981)

  Shiller RJ. 1981.
  Do stock prices move too much to be justified by subsequent changes in
  dividends?
  American Economic Review 71(3):421–436
* Shiller (1993)

  Shiller RJ. 1993.
  Measuring asset values for cash settlement in derivative markets: hedonic
  repeated measures indices and perpetual futures.
  The Journal of Finance 48(3):911–931
* Shleifer & Vishny (1997)

  Shleifer A, Vishny RW. 1997.
  The limits of arbitrage.
  The Journal of Finance 52(1):35–55
* Sockin & Xiong (2023a)

  Sockin M, Xiong W. 2023a.
  Decentralization through tokenization.
  The Journal of Finance 78(1):247–299
* Sockin & Xiong (2023b)

  Sockin M, Xiong W. 2023b.
  A model of cryptocurrencies.
  Management Science 69(11):6684–6707
* Tobin (1965)

  Tobin J. 1965.
  Money and economic growth.
  Econometrica: journal of the Econometric Society :671–684
* Toscano et al. (2025)

  Toscano JD, Wang LL, Karniadakis GE. 2025.
  Kkans: Kurkova-Kolmogorov-Arnold networks and their learning dynamics.
  Neural Networks 191:107831
* Townsend (1980)

  Townsend RM. 1980.
  Models of money with spatially separated agents.
  Models of monetary economies :265–303
* Townsend (2020)

  Townsend RM. 2020.
  Distributed ledgers: Design and regulation of financial infrastructure and
  payment systems.
  MIT Press
* Trejos & Wright (1995)

  Trejos A, Wright R. 1995.
  Search, bargaining, money, and prices.
  Journal of Political Economy 103(1):118–141
* Verrecchia (1983)

  Verrecchia RE. 1983.
  Discretionary disclosure.
  Journal of Accounting and Economics 5:179–194
* Verrecchia (2001)

  Verrecchia RE. 2001.
  Essays on disclosure.
  Journal of Accounting and Economics 32(1-3):97–180
* von Luckner et al. (2023)

  von Luckner CG, Reinhart CM, Rogoff K. 2023.
  Decrypting new age international capital flows.
  Journal of Monetary Economics 138:104–122
* Wallace (1983)

  Wallace N. 1983.
  A legal restrictions theory of the demand for “money” and the role of
  monetary policy.
  Quarterly Review 7(Win)
* Watts & Zimmerman (1983)

  Watts RL, Zimmerman JL. 1983.
  Agency problems, auditing, and the theory of the firm: Some evidence.
  Journal of Law and Economics 26(3):613–633
* Weber et al. (2023)

  Weber M, Candia B, Coibion O, Gorodnichenko Y. 2023.
  Do you even crypto, bro? Cryptocurrencies in household finance.
  Tech. rep., National Bureau of Economic Research
* Whited et al. (2023)

  Whited TM, Wu Y, Xiao K. 2023.
  Will central bank digital currency disintermediate banks?
  Journal of Monetary Economics 81:111–132