---
authors:
- Yihan Hong
- Hengxiang Feng
- Yinghan Wang
- Boxuan Li
doc_id: arxiv:2512.12815v1
family_id: arxiv:2512.12815
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against
  Traditional Assets
url_abs: http://arxiv.org/abs/2512.12815v1
url_html: https://arxiv.org/html/2512.12815v1
venue: arXiv q-fin
version: 1
year: 2025
---


Yihan Hong
  
Olin Business School
  
Washington University in St. Louis
  
&Hengxiang Feng
  
Olin Business School
  
Washington University in St. Louis
  
&Yinghan Wang
  
Olin Business School
  
Washington University in St. Louis
  
&Boxuan Li
  
Olin Business School
  
Washington University in St. Louis

###### Abstract

The approval of the Bitcoin Spot ETF in January 2024 marked a transformative event in cryptocurrency markets, signaling increased institutional adoption and integration into traditional finance. This study examines Bitcoin’s changing relationships with traditional assets, including equities, gold, and fiat currencies, following this milestone. Using rolling correlation analysis, Chow tests, and DCC-GARCH models, we found that Bitcoin’s correlation with the S&P 500 increased significantly post-ETF approval, indicating stronger alignment with equities. Its relationship with gold stabilized near zero, while its correlation with the U.S. Dollar Index remained consistently negative. These findings offer insights into Bitcoin’s evolving role in portfolios, implications for market stability, and future research opportunities on cryptocurrency integration into traditional financial systems.

*Keywords* Bitcoin Spot ETF ⋅\cdot
Cryptocurrency ⋅\cdot
Hedging Properties ⋅\cdot
Rolling Correlation ⋅\cdot
DCC-GARCH

## 1 Introduction

Bitcoin has historically been discussed as a potential hedge asset, theoretically similar to gold and government bonds, largely due to its decentralized nature and independence from traditional financial systems Bouri et al. ([2017](https://arxiv.org/html/2512.12815v1#bib.bib1)). The premise that Bitcoin can serve as a safe haven is predicated on its historically low correlation with traditional assets such as stocks and bonds, particularly during periods of market turbulence. Several empirical studies have examined Bitcoin’s role in financial portfolios, concluding that it possesses the potential to hedge against inflation, currency devaluation, and economic crises Corbet et al. ([2018](https://arxiv.org/html/2512.12815v1#bib.bib2)). However, unlike traditional physical assets, Bitcoin is digital and highly volatile, which has led to ongoing debates regarding its reliability as a consistent hedge Klein et al. ([2018](https://arxiv.org/html/2512.12815v1#bib.bib3)). The central question remains whether Bitcoin can maintain this independence as it becomes increasingly financialized and integrated into global capital markets.

The regulatory environment for Bitcoin in the United States has undergone a significant evolution, culminating in a paradigm shift in early 2024. The U.S. Securities and Exchange Commission (SEC) initially approached cryptocurrencies with caution, focusing on prosecuting fraud in 2013 and rejecting the first Bitcoin ETF applications in 2017 due to concerns over market manipulation and lack of surveillance agreements with regulated markets. While a futures-based ETF was approved in 2021, the market long awaited a spot product that would allow for direct price exposure. The pivotal moment arrived in January 2024, when the SEC approved several Bitcoin Spot ETFs, allowing institutional investors to gain exposure to Bitcoin without direct ownership Gensler ([2024](https://arxiv.org/html/2512.12815v1#bib.bib4)). This approval introduced strict transparency and surveillance requirements, signaling Bitcoin’s maturation as a regulated financial asset Uyeda ([2024](https://arxiv.org/html/2512.12815v1#bib.bib5)).

This regulatory milestone provides a unique opportunity to re-evaluate Bitcoin’s market behavior. As institutional capital flows into the market through regulated channels, the asset’s correlation dynamics may fundamentally change. Existing literature suggests that integration into mainstream financial systems could erode Bitcoin’s independence, potentially increasing its correlation with equities Wang and Wang ([2021](https://arxiv.org/html/2512.12815v1#bib.bib6)). This phenomenon is often observed in emerging asset classes that transition from niche to mainstream. This study aims to fill the research gap by systematically analyzing the impact of the ETF approval on Bitcoin’s correlation with traditional hedge assets (Gold, U.S. Dollar) and equities (S&P 500). By employing a combination of rolling correlations, structural break tests, and dynamic conditional correlation models, we provide a comprehensive assessment of whether Bitcoin’s role as a "digital gold" or safe haven has been altered by its integration into traditional finance.

## 2 Literature Review

### 2.1 Theoretical Foundation of Safe-Haven Assets

The concept of safe-haven assets is rooted in behavioral finance theories from the 1990s. Tversky and Kahneman (1991) introduced reference-dependent models explaining that investors exhibit heightened sensitivity to losses during economic turbulence Tversky and Kahneman ([1991](https://arxiv.org/html/2512.12815v1#bib.bib7)). Building on this foundation, Baur and Lucey (2009) formally defined safe-haven assets as those that provide a hedging effect against systemic risks during extreme market volatility. These assets typically exhibit little to no correlation, or even a negative correlation, with the overall market trend during distress periods Baur and Lucey ([2009](https://arxiv.org/html/2512.12815v1#bib.bib8)). Understanding the theoretical underpinnings of safe havens is crucial for evaluating whether a novel asset class like cryptocurrency can fulfill this role.

### 2.2 Traditional Safe-Haven Assets and Limitations

Scholars have traditionally identified gold, government bonds, and specific fiat currencies as mainstream safe havens. Baur and McDermott (2010) demonstrated that gold exhibits strong safe-haven properties in most developed markets during financial crises Baur and McDermott ([2010](https://arxiv.org/html/2512.12815v1#bib.bib9)). Similarly, regarding government bonds, Flavin and Morley (2014) argued that long-term bonds meet the definition of safe-haven assets as they effectively reduce risk during turbulence, primarily due to the "flight to quality" phenomenon Flavin and Morley ([2014](https://arxiv.org/html/2512.12815v1#bib.bib11)). In the currency markets, Ranaldo and Söderlind (2010) identified the Swiss franc as a significant hedge against U.S. stock market downturns Ranaldo and Söderlind ([2010](https://arxiv.org/html/2512.12815v1#bib.bib12)). However, the effectiveness of these traditional assets is not static. Lucey and Li (2013) found that gold’s properties vary over time, and recent studies by Chang and McAleer (2020) indicate that correlations between traditional safe havens and market volatility have increased in the post-COVID era, potentially diminishing their protective utility Chang and McAleer ([2020](https://arxiv.org/html/2512.12815v1#bib.bib15)).

### 2.3 Bitcoin: The "Digital Gold" Debate

The academic community remains divided on Bitcoin’s classification as a safe haven. Proponents, such as Bouri and Molnar (2017), refer to Bitcoin as "digital gold" due to its fixed supply and decentralization. Bouri and Shahzad (2020) further argued that Bitcoin offers superior independence compared to gold and commodities because it is not tied to any central bank or geopolitical entity Bouri and Shahzad ([2020](https://arxiv.org/html/2512.12815v1#bib.bib17)). Conversely, skeptics highlight its extreme volatility as a disqualifying factor. Smales (2019) found that Bitcoin’s lower liquidity and significantly higher volatility compared to traditional assets make it currently unsuitable as a safe haven Smales ([2019](https://arxiv.org/html/2512.12815v1#bib.bib18)). Furthermore, Choi and Shin (2022) observed that Bitcoin prices fluctuate significantly with financial uncertainty, behaving more like a speculative asset than a reliable hedge Choi and Shin ([2022](https://arxiv.org/html/2512.12815v1#bib.bib19)). This ongoing debate underscores the need to re-examine Bitcoin’s properties specifically in light of recent market structural changes.

### 2.4 The Impact of Bitcoin ETF Approval

The approval of Bitcoin Spot ETFs represents a significant structural change that may resolve or exacerbate these debates. Gensler (2024) noted that this approval enhances the legitimacy of the Bitcoin market, potentially reducing the reputational risk for institutional investors. According to Foley & Lardner LLP (2024), ETFs increase market transparency and security, simplifying the investment process for institutions Foley and Lardner LLP ([2024](https://arxiv.org/html/2512.12815v1#bib.bib22)). While this attracts liquidity, as noted by Uyeda (2024), it also integrates Bitcoin more tightly with traditional markets. Lee and Lee (2024) pointed out that while liquidity improved, the correlation between Bitcoin and traditional assets like the stock market increased post-approval Lee and Lee ([2024](https://arxiv.org/html/2512.12815v1#bib.bib25)). This suggests that the "financialization" of Bitcoin through ETFs might be altering its fundamental hedging characteristics, transitioning it from an idiosyncratic asset to a systemic one.

## 3 Methodology

To thoroughly investigate the impact of the ETF approval, we adopt a multi-layered econometric approach. We begin with a visual inspection of trends, proceed to statistical verification of structural breaks, and conclude with a robust dynamic model to account for volatility clustering.

### 3.1 Forward Rolling Correlation

Our analysis begins with Forward Rolling Correlation to provide an intuitive, time-varying perspective on the relationship between Bitcoin and traditional assets. By calculating correlations over moving windows (30-day and 60-day), we can capture short-to-medium-term fluctuations that a static correlation measure would miss. The coefficient is calculated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | corrx​y,t=∑i=t−N+1t(xi−x¯)​(yi−y¯)∑i=t−N+1t(xi−x¯)2​∑i=t−N+1t(yi−y¯)2\text{corr}\_{xy,t}=\frac{\sum\_{i=t-N+1}^{t}(x\_{i}-\bar{x})(y\_{i}-\bar{y})}{\sqrt{\sum\_{i=t-N+1}^{t}(x\_{i}-\bar{x})^{2}\sum\_{i=t-N+1}^{t}(y\_{i}-\bar{y})^{2}}} |  | (1) |

where NN represents the window size. This method allows us to visually identify potential shifts in correlation trends around the event date, serving as a preliminary diagnostic tool for structural changes.

### 3.2 Chow Test for Structural Breaks

While rolling correlations offer visual evidence, they do not provide statistical confirmation of a regime change. To address this, we employ the Chow Test to scientifically detect structural mutations in the regression parameters before and after the ETF approval date (Jan 10, 2024). We apply this test to verify if the linear relationship (YB​T​C=α+β​X+ϵY\_{BTC}=\alpha+\beta X+\epsilon) underwent a statistically significant shift. The test statistic is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Chow Statistic=(R​S​Sp​o​o​l​e​d−(R​S​S1+R​S​S2))/k(R​S​S1+R​S​S2)/(N1+N2−2​k)\text{Chow Statistic}=\frac{(RSS\_{pooled}-(RSS\_{1}+RSS\_{2}))/k}{(RSS\_{1}+RSS\_{2})/(N\_{1}+N\_{2}-2k)} |  | (2) |

A significant result here would confirm that the ETF approval acted as a structural breakpoint in the market dynamics, indicating that the fundamental pricing mechanism of Bitcoin relative to other assets has shifted.

### 3.3 ARMA-DCC-GARCH Model

Rolling correlations have limitations, such as the arbitrary choice of window size and the equal weighting of observations. Furthermore, financial time series, particularly cryptocurrencies, exhibit heteroskedasticity (volatility clustering). To overcome these limitations and provide a robust analysis of long-term dynamic correlations, we employ the Dynamic Conditional Correlation (DCC) GARCH model. First, we estimate univariate GARCH(1,1) models for each asset to standardize residuals. Then, we compute the dynamic correlation matrix RtR\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=diag​(Qt)−1/2​Qt​diag​(Qt)−1/2R\_{t}=\text{diag}(Q\_{t})^{-1/2}Q\_{t}\text{diag}(Q\_{t})^{-1/2} |  | (3) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qt=(1−a−b)​Q¯+a​ϵt−1​ϵt−1T+b​Qt−1Q\_{t}=(1-a-b)\bar{Q}+a\epsilon\_{t-1}\epsilon\_{t-1}^{T}+bQ\_{t-1} |  | (4) |

This model allows us to isolate the true correlation dynamics from the noise of volatility spikes, offering a clearer picture of how Bitcoin’s integration with traditional markets has evolved post-ETF.

## 4 Experiments

### 4.1 Data Selection, Stationarity, and Descriptive Statistics

This research analyzes daily adjusted closing prices for Bitcoin, the S&P 500 (representing equities), Gold (a traditional safe haven), and the U.S. Dollar Index (DXY). The dataset, sourced from Yahoo Finance, is carefully segmented into two distinct periods centered around the ETF approval date of January 10, 2024. The \*\*Pre-Event\*\* period spans from October 1, 2023, to January 9, 2024, while the \*\*Post-Event\*\* period extends from January 11, 2024, to April 30, 2024.

Before proceeding with time-series modeling, it is critical to ensure the data is stationary. We conducted the Augmented Dickey-Fuller (ADF) test on the excess returns of all four assets. As shown in Table [1](https://arxiv.org/html/2512.12815v1#S4.T1 "Table 1 ‣ 4.1 Data Selection, Stationarity, and Descriptive Statistics ‣ 4 Experiments ‣ The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against Traditional Assets"), the ADF statistics for Bitcoin (-41.4453), S&P 500 (-20.2299), Gold (-71.0724), and DXY (-71.6057) are all highly significant with p-values of 0.0000. This confirms that the return series are stationary, satisfying the prerequisite conditions for ARMA-GARCH modeling.

Table 1: ADF Test on Excess Return of Four Assets

|  | Bitcoin | S&P 500 | Gold | DXY |
| --- | --- | --- | --- | --- |
| ADF Statistics | -41.4453 | -20.2299 | -71.0724 | -71.6057 |
| p-value | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

The descriptive statistics, summarized in Table [2](https://arxiv.org/html/2512.12815v1#S4.T2 "Table 2 ‣ 4.1 Data Selection, Stationarity, and Descriptive Statistics ‣ 4 Experiments ‣ The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against Traditional Assets"), reveal a dramatic shift in Bitcoin’s market behavior following the regulatory approval. Post-event, Bitcoin’s mean price surged from approximately 26,328 to 60,503, accompanied by a significant increase in volatility, with the standard deviation rising from 7,034.9 to 9,919.4. In terms of excess returns, Bitcoin showed marked improvement, shifting from a negative mean return of -0.0008 to a positive 0.0018. In stark contrast, traditional assets exhibited stability. The S&P 500 saw a reduction in volatility, with its standard deviation decreasing from 280.8 to 182.9, while the U.S. Dollar Index remained the least volatile asset, reinforcing its role as a stable store of value.

Table 2: Descriptive Statistics of Closing Prices and Returns (Pre vs Post Event)

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Pre-Event (2023.10.01 - 2024.01.09) | | | | Post-Event (2024.01.11 - 2024.04.30) | | | |
| Asset | Mean Price | Std Dev | Mean Ret | Std Ret | Mean Price | Std Dev | Mean Ret | Std Ret |
| Bitcoin | 26,328 | 7,035 | -0.0008 | 0.0322 | 60,503 | 9,919 | 0.0018 | 0.0323 |
| S&P 500 | 4,183 | 280 | -0.0019 | 0.0171 | 5,141 | 182 | 0.0012 | 0.0070 |
| Gold | 1,880 | 116 | -0.0020 | 0.0164 | 2,214 | 142 | 0.0012 | 0.0095 |
| DXY | 104.9 | 3.1 | -0.0025 | 0.0132 | 104.5 | 0.9 | 0.0003 | 0.0032 |

### 4.2 Rolling Correlation Analysis

To capture the dynamic evolution of market integration, we computed 30-day and 60-day rolling correlations. The results indicate a fundamental transition in Bitcoin’s relationship with equities. Prior to the ETF approval, the correlation between Bitcoin and the S&P 500 was volatile and generally trending downwards, often behaving idiosyncratically. However, immediately following January 2024, the correlation coefficient shifted to a sharp upward trend. This reversal suggests that the approval of the Bitcoin Spot ETF acted as a catalyst, transforming Bitcoin from an isolated asset into one that moves in tandem with traditional equities. As shown in Figure [1(a)](https://arxiv.org/html/2512.12815v1#S4.F1.sf1 "In Figure 1 ‣ 4.2 Rolling Correlation Analysis ‣ 4 Experiments ‣ The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against Traditional Assets"), the post-event trajectory implies that institutional investors are increasingly treating Bitcoin as a "risk-on" asset similar to technology stocks, rather than a diversified hedge.

Conversely, the relationship between Bitcoin and traditional safe havens did not exhibit a similar structural strengthening. The correlation with Gold (Figure [1(b)](https://arxiv.org/html/2512.12815v1#S4.F1.sf2 "In Figure 1 ‣ 4.2 Rolling Correlation Analysis ‣ 4 Experiments ‣ The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against Traditional Assets")), while fluctuating, remained relatively low and did not show a significant positive shift after the ETF launch. This finding challenges the "digital gold" narrative, suggesting that despite its scarcity features, Bitcoin does not yet behave like a substitute for gold in institutional portfolios. Similarly, the correlation with the U.S. Dollar Index (Figure [1(c)](https://arxiv.org/html/2512.12815v1#S4.F1.sf3 "In Figure 1 ‣ 4.2 Rolling Correlation Analysis ‣ 4 Experiments ‣ The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against Traditional Assets")) remained consistently negative or negligible throughout the observation period. This indicates that Bitcoin’s price discovery remains largely independent of fiat currency strength, even after its integration into regulated financial markets.

![Refer to caption](fig1_rolling_sp500.png)


(a) Bitcoin vs S&P 500 (30-day & 60-day)

![Refer to caption](fig2_rolling_gold.png)


(b) Bitcoin vs Gold

![Refer to caption](fig3_rolling_dxy.png)


(c) Bitcoin vs DXY

Figure 1: Rolling Correlation Analysis across Assets.

### 4.3 Structural Break Verification (Chow Test)

Visual inspection of correlation plots provides intuitive evidence, but statistical rigor is required to confirm regime changes. We employed the Chow Test to detect structural breaks at the January 10, 2024 breakpoint. The results revealed a nuanced and critical distinction between the stability of return coefficients and the structural shift in correlation trends.

First, we examined the \*\*Pairwise OLS Regression\*\* on excess returns (Table [3](https://arxiv.org/html/2512.12815v1#S4.T3 "Table 3 ‣ 4.3 Structural Break Verification (Chow Test) ‣ 4 Experiments ‣ The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against Traditional Assets")). Interestingly, for the S&P 500, the Chow statistic (0.1427) yielded a p-value of 0.8670, indicating no structural break in the \*linear regression coefficient\* itself. However, for Gold (p=0.0991) and DXY (p=0.0002), the null hypothesis was rejected, confirming a break. This suggests that while the instantaneous beta of Bitcoin to the S&P 500 might not have shifted abruptly on day one, the relationship with safe-haven assets did.

Table 3: Chow Test Results Based on Pairwise OLS Regression

| Independent Variable | Chow Statistics | P-value | Break Confirmed? |
| --- | --- | --- | --- |
| S&P 500 Excess Return | 0.1427 | 0.8670 | No |
| Gold Excess Return | 2.3225\* | 0.0991 | Yes |
| DXY Excess Return | 8.7886\*\*\* | 0.0002 | Yes |

However, the most definitive evidence of a paradigm shift comes from the Chow Test on the \*\*Rolling Correlation Series\*\* (Table [4](https://arxiv.org/html/2512.12815v1#S4.T4 "Table 4 ‣ 4.3 Structural Break Verification (Chow Test) ‣ 4 Experiments ‣ The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against Traditional Assets")). Here, the results were unequivocal. The test statistics for Bitcoin’s correlation with the S&P 500 (139.42 for 30-day), Gold (135.96 for 30-day), and DXY (105.86 for 30-day) all yielded p-values of 0.0000, statistically significant at the 1% level. This confirms that the \*correlation structure\*—representing the sustained, moving relationship between assets—underwent a massive mutation. While the pairwise regression captures a snapshot, the rolling correlation captures the trend, and this trend unmistakably broke from its historical pattern upon the ETF approval.

Table 4: Chow Test Results on Rolling Correlation Series (OLS with Constant)

| Dependent Variable | Chow Statistic | P-value | Structural Break? |
| --- | --- | --- | --- |
| Corr BTC-S&P 500 (30-day) | 139.42 | 0.0000 | Yes |
| Corr BTC-S&P 500 (60-day) | 269.30 | 0.0000 | Yes |
| Corr BTC-Gold (30-day) | 135.96 | 0.0000 | Yes |
| Corr BTC-DXY (30-day) | 105.86 | 0.0000 | Yes |

The visualizations of these structural breaks (Figure [2](https://arxiv.org/html/2512.12815v1#S4.F2 "Figure 2 ‣ 4.3 Structural Break Verification (Chow Test) ‣ 4 Experiments ‣ The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against Traditional Assets")) clearly show the divergence. The S&P 500 correlation exhibits a distinct upward shift in the fitted line post-break, whereas the Gold and DXY correlations show different structural adjustments, further differentiating Bitcoin’s integration with risk assets versus safe havens.

![Refer to caption](fig4_1_break_sp500.png)


(a) BTC vs S&P 500

![Refer to caption](fig4_3_break_gold.png)


(b) BTC vs Gold

![Refer to caption](fig4_5_break_dxy.png)


(c) BTC vs DXY

Figure 2: Structural Break Visualizations (Chow Test). The red dashed line marks the ETF approval date. Note the upward trend shift for S&P 500.

### 4.4 Dynamic Conditional Correlation (DCC-GARCH) Analysis

To account for the time-varying volatility inherent in cryptocurrency markets, we utilized the DCC-GARCH model. The estimation results for the ARMA-GARCH model (Table [5](https://arxiv.org/html/2512.12815v1#S4.T5 "Table 5 ‣ 4.4 Dynamic Conditional Correlation (DCC-GARCH) Analysis ‣ 4 Experiments ‣ The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against Traditional Assets")) confirm the validity of this approach. The ARCH term (α1=0.1184\alpha\_{1}=0.1184) and GARCH term (β1+β2≈0.49\beta\_{1}+\beta\_{2}\approx 0.49) are significant, indicating the presence of volatility clustering which simple OLS would miss.

Table 5: Coefficients in the Volatility Equation of the ARMA-GARCH Model for Bitcoin

|  |  |  |  |
| --- | --- | --- | --- |
| Parameter | Coef | T Statistics | P-value |
| Omega | 2.4025\*\* | 2.197 | 0.0281 |
| Alpha 1 | 0.1184\* | 1.874 | 0.0609 |
| Alpha 2 | 0.1683 | 1.454 | 0.146 |
| Beta 1 | 0.1399 | 0.575 | 0.565 |
| Beta 2 | 0.3563 | 1.588 | 0.112 |
| Note: \*\* denotes significance at 5%; \* denotes significance at 10%. | | | |
| --- | --- | --- | --- |

The dynamic correlation results provide a sophisticated view of the post-ETF dynamics. Immediately following the approval, we observed a sharp drop in dynamic correlations across all asset pairs. This phenomenon can be attributed to the "dispersion effect", where the market experienced a short-term shock as investor structures adjusted and speculative capital rotated. The entry of new institutional participants initially caused divergent trading strategies, leading to this temporary decoupling as price discovery mechanisms reset.

However, subsequent to this initial dispersion, the dynamic correlation between Bitcoin and the S&P 500 rebounded significantly (Figure [3(a)](https://arxiv.org/html/2512.12815v1#S4.F3.sf1 "In Figure 3 ‣ 4.4 Dynamic Conditional Correlation (DCC-GARCH) Analysis ‣ 4 Experiments ‣ The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against Traditional Assets")). This rebound confirms the "portfolio reallocation" hypothesis, where investors, driven by optimistic sentiment, began to allocate capital simultaneously to both Bitcoin and equities. In contrast, the dynamic correlation with Gold (Figure [3(b)](https://arxiv.org/html/2512.12815v1#S4.F3.sf2 "In Figure 3 ‣ 4.4 Dynamic Conditional Correlation (DCC-GARCH) Analysis ‣ 4 Experiments ‣ The Impact of Bitcoin ETF Approval on Bitcoin’s Hedging Properties Against Traditional Assets")) exhibited a mild downward trend. This supports the "fund diversion effect," where capital that might have previously sought refuge in gold is now being diverted to Bitcoin, but for speculative rather than hedging purposes. The competitive effect between these two assets suggests that Bitcoin’s integration into the ETF framework is further decoupling it from gold’s performance, weakening its potential utility as a safe haven in the traditional sense.

![Refer to caption](fig5_1_dcc_sp500.png)


(a) DCC: BTC vs S&P 500

![Refer to caption](fig5_2_dcc_gold.png)


(b) DCC: BTC vs Gold

![Refer to caption](fig5_3_dcc_dxy.png)


(c) DCC: BTC vs DXY

Figure 3: Smoothed DCC-GARCH Dynamic Correlations showing post-ETF trends.

## 5 Conclusion

This study provides robust empirical evidence that the approval of the Bitcoin Spot ETF was a pivotal event that structurally altered Bitcoin’s role in financial markets. Our analysis confirms that the "financialization" of Bitcoin has led to a paradigm shift in its correlation dynamics. Specifically, the significant increase in Bitcoin’s correlation with the S&P 500 indicates a transition from an independent, speculative hedge to a conventional risk asset that moves in tandem with global equity markets. Conversely, the relationship with Gold and the U.S. Dollar remained stable or independent, challenging the popular narrative that the ETF approval would solidify Bitcoin’s status as "digital gold". The statistical confirmation of structural breaks suggests that the pricing models for Bitcoin prior to 2024 may no longer be applicable in this new regulated regime.

For investors, these findings have profound implications for portfolio construction. The increasing correlation with equities suggests that Bitcoin’s effectiveness as a diversifier against stock market downturns is diminishing. While it still offers high potential returns, it can no longer be relied upon as an uncorrelated safe haven during systemic equity shocks. Portfolio managers must now account for the higher beta and synchronization with the S&P 500 when calculating Value at Risk (VaR) and optimal allocation weights. The data suggests that Bitcoin should be treated as a high-growth technology proxy rather than a defensive asset in the current market environment.

From a regulatory and systemic risk perspective, the integration of Bitcoin into mainstream finance introduces new channels for risk transmission. The stronger linkage between crypto markets and traditional finance means that volatility in one sector is more likely to spill over into the other. Policymakers should be aware that the "walled garden" of crypto is effectively gone; shocks in the crypto market now have a direct transmission mechanism to institutional balance sheets via ETFs. Future research should focus on the long-term persistence of these correlations and explore whether the "fund diversion effect" from gold becomes a permanent feature of the investment landscape.

## References

* Bouri et al. (2017)

  Bouri, E., et al. (2017). On the Hedge and Safe Haven Properties of Bitcoin. Finance Research Letters, 20, 192-198.
* Corbet et al. (2018)

  Corbet, S., et al. (2018). Exploring the Dynamic Relationships between Cryptocurrencies and Other Financial Assets. Economics Letters, 165, 28-34.
* Klein et al. (2018)

  Klein, T., et al. (2018). Bitcoin Is Not the New Gold. International Review of Financial Analysis, 59, 105-116.
* Gensler (2024)

  Gensler, G. (2024). Statement on Approval of Bitcoin Spot ETFs. SEC.
* Uyeda (2024)

  Uyeda, C. (2024). Institutional Participation and Market Maturity. Journal of Financial Regulation, 10(1), 1-19.
* Wang and Wang (2021)

  Wang, J., & Wang, X. (2021). Bitcoin’s Safe Haven Properties.
* Tversky and Kahneman (1991)

  Tversky, A., & Kahneman, D. (1991). Loss Aversion in Riskless Choice. QJE, 106(4).
* Baur and Lucey (2009)

  Baur, D. G., & Lucey, B. M. (2009). Is Gold a Hedge or a Safe Haven? Financial Review, 45(2).
* Baur and McDermott (2010)

  Baur, D. G., & McDermott, T. K. (2010). Is Gold a Safe Haven? International Evidence. JBF, 34(8).
* Akhtaruzzaman and Boubaker (2021)

  Akhtaruzzaman, M., & Boubaker, S. (2021). Financial Contagion during COVID-19. Finance Research Letters, 38.
* Flavin and Morley (2014)

  Flavin, T. J., & Morley, J. (2014). When Is a Government Bond Not a Safe Haven? IJFE, 19(3).
* Ranaldo and Söderlind (2010)

  Ranaldo, A., & Söderlind, P. (2010). Safe Haven Currencies. Review of Finance, 14(3).
* Kopyl and Lee (2016)

  Kopyl, K., & Lee, J. (2016). Safe Haven Currencies Revisited. Pacific-Basin Finance Journal, 40.
* Lucey and Li (2013)

  Lucey, B. M., & Li, S. (2013). What Precious Metals Act as Safe Havens? Applied Economics Letters, 20(8).
* Chang and McAleer (2020)

  Chang, C. L., & McAleer, M. (2020). Gold, Oil, and Stock Market Volatility. IRFA, 74.
* Umar and Su (2021)

  Umar, Z., & Su, C. K. M. (2021). Are Safe-Haven Assets Really Safe? Review of Behavioral Finance, 13(1).
* Bouri and Shahzad (2020)

  Bouri, E., & Shahzad, S. J. H. (2020). Safe Haven Properties of Bitcoin and Gold. Resources Policy, 65.
* Smales (2019)

  Smales, L. A. (2019). Bitcoin as a Safe Haven? Finance Research Letters, 3.
* Choi and Shin (2022)

  Choi, K., & Shin, K. (2022). Bitcoin and Uncertainty. Journal of Financial Markets, 58.
* Shahzad and Bouri (2019)

  Shahzad, S. J. H., & Bouri, E. (2019). Is Bitcoin a Better Safe-Haven Investment Than Gold? IRFA, 63.
* Bossman and Gubareva (2024)

  Bossman, A., & Gubareva, E. (2024). Financial Market Interconnectedness. Global Finance Journal.
* Foley and Lardner LLP (2024)

  Foley & Lardner LLP. (2024). Legal Analysis of Bitcoin ETF Regulation.
* Liu and Yang (2024)

  Liu, J., & Yang, Y. (2024). Liquidity and Volatility Post-ETF. Journal of Alternative Investments, 27(1).
* Seungju and Jaewook (2024)

  Seungju, K., & Jaewook, L. (2024). Bitcoin ETF Approval and Impact. JBEF.
* Lee and Lee (2024)

  Lee, C., & Lee, S. (2024). Market Sentiment and Correlation Shifts. Journal of Empirical Finance, 72.