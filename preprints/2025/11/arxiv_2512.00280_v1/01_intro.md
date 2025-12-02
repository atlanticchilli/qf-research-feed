---
authors:
- Domonkos F. Vamossy
doc_id: arxiv:2512.00280v1
family_id: arxiv:2512.00280
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Retail Investor Horizon and Earnings Announcements
url_abs: http://arxiv.org/abs/2512.00280v1
url_html: https://arxiv.org/html/2512.00280v1
venue: arXiv q-fin
version: 1
year: 2025
---


Domonkos F. Vamossy
Department of Economics, University of Pittsburgh, d.vamossy@pitt.edu.

(November 29, 2025)

We examine whether retail investor investment horizons explain earnings-related return patterns. Using StockTwits posts (2010–2021), we classify stocks as long- or short-horizon prior to earnings. We find horizon composition strongly predicts price paths: long-horizon stocks exhibit larger immediate reactions and pronounced post-announcement drift compared to short-horizon stocks. A strategy buying long-horizon and shorting short-horizon stocks generates 0.43% monthly alpha. Additionally, elevated pre-event sentiment predicts weaker subsequent performance, particularly for short-horizon stocks. These results confirm that retail horizon composition provides a useful dimension for summarizing systematic variation in earnings returns and extracting information from retail activity.

Keywords: Investment horizon; dispersed information; NLP; earnings announcements.

JEL Codes: G14, G41.

## 1 Introduction

> ”The stock market is a device for transferring money from the impatient to the patient.”

— Warren Buffett

Building on Buffett’s insight into the virtues of patience, this paper investigates how the investment horizon of investors influences stock price reactions to earnings surprises. How different investor time-horizons shape price discovery is a question of both theoretical and practical importance, as it reveals how trading patience influences stock reactions and informs our understanding of market efficiency.

We leverage social media data from StockTwits, a platform akin to Twitter but tailored for investors, to measure investment horizons among retail investors. By analyzing users’ self-reported holding periods, we classify retail investors as either short-term or long-term. For each stock, we tally the unique count of these investors who engage in discussions within the [−90,−1][-90,-1] day window prior to an earnings announcement, calculating the proportion of long-term investors within this group. If this proportion exceeds 50%, we designate the stock as being predominantly associated with long-term retail investors.

We then examine how investment horizon at the security level affects stock price reactions to earnings surprises. Using earnings data from I/B/E/S and COMPUSTAT, we focus on quarterly earnings announcements for which at least one analyst provides an earnings forecast in the 30 days before the announcement. We define the earnings surprise as the difference between the earnings announcement and the consensus earnings forecast, scaled by the price per share as in dellavigna:2009.

Horizon composition meaningfully shapes earnings-announcement returns. Relative to short-horizon names, stocks predominantly followed by long-horizon investors exhibit stronger immediate reactions (about +0.21+0.21 pp over days 0–1 in fully controlled specifications) and a larger, more persistent post-announcement drift. Long-horizon stocks earn an additional +2.08+2.08 pp over days 2–75, resulting in a total outperformance of +2.31+2.31 pp over the full 0–75 day window. These differentials are robust to firm fixed and year-quarter effects and matching. A simple monthly long–short drift strategy formed within earnings-surprise bins delivers economically large, factor-adjusted alphas, approximately 30 basis points per month for the overall portfolio and nearly 40 basis points when restricting to the top three surprise bins.

The existing literature highlights several channels explaining the role of short-horizon institutional investors in stock price behavior, including demand pressure or demand shock mechanisms gompers:2001; hotchkiss:2003; cella:2013, informational advantages ke:2006; yan:2009, and corporate governance influences gaspar:2005. However, these mechanisms may not fully capture the dynamics of stock price reactions to earnings surprises in a landscape increasingly shaped by retail investors.

Recent research indicates that retail investors’ behavior can significantly impact stock prices, especially around high-news events barber2008retail; vamossy2021investor; vamossy2023social; barber2023resolving; friedman2024retail. Retail investors’ horizons vary widely; some pursue longer-term “buy and hold” strategies, while others are inclined toward frequent trading in response to recent news or social sentiment. This behavioral divergence may reflect underlying factors that influence stock price reactions, and the holding patterns of retail investors could serve as a proxy for these unobserved variables.

This paper connects and extends several strands of the literature. Prior work highlights how short-horizon institutional ownership can influence prices via demand pressure and shocks (gompers:2001; hotchkiss:2003; cella:2013), information advantages (ke:2006; yan:2009), and governance channels (gaspar:2005). At the same time, a growing literature shows that retail trading shapes prices around high-news events and in attention-driven settings (barber2008retail; barber2023resolving; friedman2024retail). We add a retail-horizon perspective to classic work on horizon heterogeneity and trading by institutions (lakonishok:1992; grinblatt:1995; wermers:1999; nofsinger:1999; gompers:2001; grinblatt:2000; cohen:2002; hotchkiss:2003), showing that the composition of retail horizons is a powerful cross-sectional predictor of both the immediate and delayed components of earnings-related returns.

Our interpretation emphasizes differences in information processing and optimism bias. Using textual analysis and sentiment extraction, we find that short-horizon investors rely heavily on technical trading cues (e.g., break, target) and exhibit higher pre-announcement sentiment volatility. In contrast, long-horizon investors focus on fundamental concepts (e.g., EPS, financials). Mechanism tests using above-median pre-EA social-media valence support an optimism-bias channel: upbeat chatter predicts subsequent giveback, especially in short-horizon stocks, while a long-horizon presence attenuates this reversal. We formalize these predictions in a simple model in Section [3](https://arxiv.org/html/2512.00280v1#S3 "3 A Model of Earnings Announcement Reactions and Investor Horizons ‣ Retail Investor Horizon and Earnings Announcements") and test them empirically.

The remainder of the paper is organized as follows. Section 2 introduces the measure for the horizon of retail investors and provides descriptive statistics highlighting the differences between the long-term and short-term securities. Section 3 presents a simple model, and Section 4 presents the methodology. Section 5 discusses the main results. Section 6 offers additional findings and probes into mechanisms. Section 7 concludes.

## 2 A measure of retail investors’ investment horizon: StockTwits Holding Period

We use data from StockTwits, a popular social networking platform for investors similar to Twitter, where users share stock opinions using “cashtags” linked to specific company ticker symbols (e.g., $AMZN). Users can tag their sentiment (bullish, bearish, or unclassified), and we can also access a sentiment score computed by StockTwits. The platform allows the tracking of likes per message, user identifiers, and user attributes like follower count.

Most users self-report their investment philosophy along two axes: Approach (technical, fundamental, momentum, value, growth, global macro) and Holding Period (day trader, swing trader, position trader, long-term investor). They also categorize their experience level as novice, intermediate, or professional. This enables us to classify firms based on the predominance of short-term or long-term traders among their investors. Specifically, we measure each firm’s retail‐investor horizon by counting unique investors, classified as short-term (day or swing traders) or long-term (position or buy-and-hold investors), who post about the stock between 90 and 1 calendar days before an earnings announcement. We then calculate the share of long-term investors in the total sample; firms with a long-term share above 50 % are designated as predominantly long-term.

### 2.1 Sample Construction

Table [1](https://arxiv.org/html/2512.00280v1#S2.T1 "Table 1 ‣ 2.1 Sample Construction ‣ 2 A measure of retail investors’ investment horizon: StockTwits Holding Period ‣ Retail Investor Horizon and Earnings Announcements") summarizes the construction of the analysis sample. We begin with 180,556 quarterly earnings announcements for 5,419 tickers in I/B/E/S. After merging these events on ticker and announcement dates with CRSP to obtain prices, returns, and firm characteristics, 142,025 announcements remain. We then apply a series of filters to ensure well-defined earnings surprises: (i) the stock price five days before the announcement must exceed $5, (ii) SUE must be non-missing, and (iii) the pre-announcement price must be at least as large as the absolute values of both the forecasted and actual EPS. These restrictions remove penny stocks and mechanically invalid denominators, yielding 130,496 announcements. We exclude firm–quarters with multiple earnings announcements and those lacking abnormal returns over the [−30,90][-30,90] window, yielding a final sample of 123,880 firm–quarter observations.

We next merge these announcements to StockTwits message activity via ticker symbols. Across the full unrestricted data, there are 51,065,435 posts by 693,965 users mentioning 5,143 tickers within the [−90,−1][-90,-1] window preceding earnings releases. Restricting to users who self-report an investment horizon, required for classifying investors as short-term or long-term, yields 20,605,979 posts from 132,958 users covering 5,082 tickers and 104,919 earnings announcements. These restrictions ensure that our horizon measure is based solely on users with explicitly stated trading styles.

Table 1: Sample Restrictions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Restriction | # of Posts | # of Users | # of Tickers | # of Announcements |
| I/B/E/S |  |  |  |  |
| Raw I/B/E/S announcements | – | – | 5,419 | 180,556 |
| Stock price available (CRSP) | – | – | 5,419 | 142,025 |
| Size, SUE, and Forecast filters | – | – | 5,419 | 130,496 |
| Dropping multiple announcements per quarter | – | – | 5,419 | 128,982 |
|  | – | – | 5,383 | 123,880 |
| StockTwits |  |  |  |  |
| Posts within [−90,−1-90,-1] of announcement | 51,065,435 | 693,965 | 5,143 | 117,389 |
| Self-reported holding period | 20,605,979 | 132,958 | 5,082 | 104,919 |

* •

  Notes: This table summarizes the construction of the final sample used in the analysis. We cover 2010 - 2021 June.

These steps show that our merge between StockTwits and I/B/E/S retains the large majority of earnings announcements, ensuring that the final sample remains broad and representative of the underlying universe of public firms. Appendix C compares the characteristics of the I/B/E/S-only and matched samples to verify this representativeness.

### 2.2 Descriptive Statistics

Table LABEL:tab:summary\_stats\_stocktwits reports descriptive statistics, including the mean, standard deviation, and key percentiles (1st, 25th, 50th, 75th, and 99th), along with sample sizes. Panel A presents the full sample (N = 104,919); Panel B splits observations by retail-investor horizon (53,354 Long-Term vs. 51,565 Short-Term announcements); and, following dellavigna:2009, Panel C groups earnings surprises into eleven quantiles, reporting each bin’s average surprise and count. Earnings surprises that are negative are allocated to quintiles 1 through 5, followed by zero surprises (quintile 6), and positive surprises (quintiles 7 through 11). The cutoffs for these groups are determined separately each quarter. Given that positive surprises are roughly twice as prevalent as negative ones, quintiles 7 through 11 contain approximately twice as many instances as quintiles 1 through 5. Within each group, we distinguish between Long-Term and Short-Term announcements. We plot the earnings surprise distribution, the day-of-the-week distribution, and the earnings surprise histogram across quantiles for Long-Term and Short-Term announcements in Figure [1](https://arxiv.org/html/2512.00280v1#S2.F1 "Figure 1 ‣ 2.2 Descriptive Statistics ‣ 2 A measure of retail investors’ investment horizon: StockTwits Holding Period ‣ Retail Investor Horizon and Earnings Announcements").

Firms with a higher share of long-term investors tend to have significantly lower market capitalization and volatility, lower institutional turnover, and lower analyst coverage compared to those dominated by short-term investors. The observation that stocks classified as long-term based on retail activity also exhibit lower churn among institutions suggests a consistency between retail and institutional investment behaviors. Additionally, long-term announcements appear more frequently later in the sample period (mean year 2016.8 vs. 2014.8). Regarding social media activity, we observe evidence consistent with an optimism bias among short-horizon investors. Stocks followed by short-term users exhibit significantly higher pre-announcement valence (0.537 vs. 0.512, tt-stat =−53.40=-53.40) and higher dispersion of opinion (SD Valence of 0.153 vs. 0.072) compared to long-term stocks. Finally, Panel C indicates that short-term announcements are disproportionately represented in the extreme tails (quantiles 1 and 11) of the earnings surprise distribution. To mitigate bias from unobserved firm characteristics, we include regressions that incorporate firm fixed effects.

Table 2: Summary Statistics

| A. CRSP/Compustat-StockTwits-I/B/E/S Sample Statistics | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Mean | Std. Dev. | 1% | 25% | 50% | 75% | 99% |  |  |  |  |  |
| Market Variables | | | | | | | | | | | | |
| Market Cap | 12,965.8 | 90,845.5 | 72.4 | 621.7 | 1,845.9 | 6,054.3 | 180,277.3 |  |  |  |  |  |
| Volatility | 0.0257 | 0.0274 | 0.0083 | 0.0154 | 0.0214 | 0.0312 | 0.0812 |  |  |  |  |  |
| Turnover | 0.2334 | 0.2661 | 0.0000 | 0.1181 | 0.1765 | 0.2600 | 2.0000 |  |  |  |  |  |
| Institutional Ownership | 0.7003 | 0.2817 | 0.0000 | 0.5599 | 0.7878 | 0.9196 | 1.0000 |  |  |  |  |  |
| Abnormal Short Interest | 0.0001 | 0.0147 | -0.0417 | -0.0031 | 0.0000 | 0.0023 | 0.0476 |  |  |  |  |  |
| Past 3-Month Return | 0.0269 | 0.2281 | -0.4921 | -0.0822 | 0.0178 | 0.1180 | 0.7181 |  |  |  |  |  |
| Earnings-Announcement and Analyst Forecast Variables | | | | | | | | | | | | |
| Earnings Surprise | 0.0001 | 0.0252 | -0.0552 | -0.0008 | 0.0005 | 0.0024 | 0.0435 |  |  |  |  |  |
| Number of Analysts | 9.0 | 7.1 | 1 | 4 | 7 | 13 | 31 |  |  |  |  |  |
| Forecast Dispersion | 0.0819 | 0.4131 | 0.0000 | 0.0100 | 0.0300 | 0.0600 | 0.8800 |  |  |  |  |  |
| BHAR [-30,-1] | -0.0068 | 0.1215 | -0.3728 | -0.0674 | -0.0069 | 0.0511 | 0.4218 |  |  |  |  |  |
| BHAR [0,1] | -0.0006 | 0.0767 | -0.2389 | -0.0376 | -0.0005 | 0.0370 | 0.2338 |  |  |  |  |  |
| BHAR [2,75] | -0.0256 | 0.2285 | -0.7392 | -0.1407 | -0.0224 | 0.0899 | 0.7222 |  |  |  |  |  |
| Social Media Information | | | | | | | | | | | | |
| Distinct Long-Term Users | 14.16 | 52.06 | 0 | 3 | 6 | 11 | 143.82 |  |  |  |  |  |
| Distinct Short-Term Users | 20.82 | 86.20 | 0 | 2 | 5 | 14 | 255 |  |  |  |  |  |
| Long-Term Posts | 88.76 | 843.27 | 0 | 9 | 23 | 47 | 1,060.82 |  |  |  |  |  |
| Short-Term Posts | 107.64 | 1,087.90 | 0 | 3 | 10 | 36 | 1,434.64 |  |  |  |  |  |
| Valence [−30,−1-30,-1] |  |  |  |  |  |  | | | | | | |
| Mean | 0.5241 | 0.0767 | 0.3420 | 0.4960 | 0.5020 | 0.5474 | 0.8171 |  |  |  |  |  |
| Std. Dev. | 0.1118 | 0.1008 | 0.0000 | 0.0053 | 0.1063 | 0.2021 | 0.3244 |  |  |  |  |  |
| Observations | 104,919 |  |  |  |  |  |  |  |  |  |  |  |
| B. Differences Between Announcements for Long-Term and Short-Term Stocks | | | | | | | | | | | | |
|  | Full sample | Long-Term | Short-Term | Norm. diff. | t-stat |  |  |  |  |  |  |  |
|  | (N = 104,919) | (N = 53,354) | (N = 51,565) |  |  |  |  |  |  |  |  |  |
| Market Cap | 12,965.8 | 7,639.1 | 18,477.2 | -0.12 | -19.35 |  | | | | | | |
| Volatility | 0.026 | 0.023 | 0.029 | -0.22 | -35.35 |  | | | | | | |
| Turnover | 0.233 | 0.198 | 0.270 | -0.27 | -43.98 |  | | | | | | |
| Institutional Ownership | 0.700 | 0.694 | 0.706 | -0.04 | -6.95 |  | | | | | | |
| Past 3-Month Return | 0.027 | 0.024 | 0.029 | -0.02 | -3.63 |  | | | | | | |
| Abnormal Short Interest | 0.000 | -0.000 | 0.000 | -0.03 | -5.12 |  | | | | | | |
| Valence [−30,−1-30,-1] |  |  |  |  |  |  | | | | | | |
| Mean | 0.524 | 0.512 | 0.537 | -0.33 | -53.40 |  | | | | | | |
| Std. Dev. | 0.112 | 0.072 | 0.153 | -0.81 | -143.84 |  | | | | | | |
| Year | 2015.799 | 2016.784 | 2014.780 | 0.63 | 107.50 |  | | | | | | |
| Earnings Surprise (SUE) | 0.000 | -0.000 | 0.000 | -0.01 | -2.07 |  | | | | | | |
| Number of Analysts | 8.958 | 6.706 | 11.288 | -0.65 | -110.89 |  | | | | | | |
| Forecast Dispersion | 0.082 | 0.064 | 0.101 | -0.09 | -14.44 |  | | | | | | |
| BHAR [0, 1] | -0.001 | 0.001 | -0.003 | 0.05 | 8.01 |  | | | | | | |
| BHAR [2, 75] | -0.026 | -0.012 | -0.040 | 0.12 | 19.90 |  | | | | | | |
| C. Average Surprise by Earnings Surprise Quantile | | | | | | | | | | | | |
|  | Quantile | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| Long-Term | Average | -0.036 | -0.006 | -0.003 | -0.001 | -0.000 | 0.000 | 0.000 | 0.001 | 0.002 | 0.004 | 0.018 |
|  | N | 3,222 | 3,680 | 3,841 | 3,879 | 3,661 | 3,995 | 5,865 | 6,248 | 6,458 | 6,517 | 5,988 |
| Short-Term | Average | -0.043 | -0.006 | -0.003 | -0.001 | -0.000 | 0.000 | 0.000 | 0.001 | 0.002 | 0.004 | 0.023 |
|  | N | 3,542 | 3,054 | 2,895 | 2,855 | 3,093 | 3,807 | 6,832 | 6,418 | 6,219 | 6,149 | 6,701 |
| Notes: Panel A provides descriptive statistics for market, I/B/E/S, and social media variables. Market variables include size (in millions), volatility, institutional ownership, institutional turnover, and abnormal short interest. Institutional ownership is the fraction of shares held by 13F firms at quarter-end tt, while turnover is the lagged churn rate calculated from holding changes between t−2t-2 and t−1t-1. Volatility is computed from 182 days before the announcement up to the day before. I/B/E/S variables include earnings surprise, number of analysts, forecast dispersion, and buy-and-hold abnormal returns at various horizons. Social media variables include posting activity by user type, as well as the mean and standard deviation of sentiment (valence). Valence is extracted following vamossy2023emtract over the window [−30,−1][-30,-1] relative to the announcement. Panel B presents differences between announcements for long-term and short-term stocks, including normalized differences and t-statistics. Earnings surprise is the difference between actual and median forecast scaled by the stock price five trading days before the announcement. The sample spans 2010–2021. | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |



![Refer to caption](x1.png)


(a) Earnings Surprise Distribution

![Refer to caption](x2.png)


(b) Day of the Week Distribution

![Refer to caption](x3.png)


(c) Earnings Surprise Histogram for Quantiles

Figure 1: Earnings Announcements by Retail Investor Horizons



Notes: The earnings surprise for an announcement is defined as the difference between the actual earnings for the quarter, as recorded by I/B/E/S, and the median analyst forecast featured in the I/B/E/S detail file within the 30 days preceding the quarterly earnings announcement. This is then scaled by the stock price 5 trading days before the announcement. Earnings announcements are divided into 11 groups: Quintiles 1 to 5 consist of five quintiles of negative earnings surprises, while quintiles 7 to 11 comprise five quintiles of positive earnings surprises. Quintile 6 includes all announcements where the earnings surprise is zero. The breakpoints are determined quarterly.

### 2.3 Measure Stability

Table [3](https://arxiv.org/html/2512.00280v1#S2.T3 "Table 3 ‣ 2.3 Measure Stability ‣ 2 A measure of retail investors’ investment horizon: StockTwits Holding Period ‣ Retail Investor Horizon and Earnings Announcements") evaluates the stability of our investor-horizon classification. Panel A examines within-event persistence by tracking whether a stock that is classified as Long-Term or Short-Term in the [−90,−1][-90,-1] window retains that status in the subsequent
[0,45][0,45] and [46,90][46,90] windows. Long-Term stocks remain Long-Term 72.2% of the time in [0,45][0,45] and 65.65% in [46,90][46,90]. Short-Term classifications are even more persistent, with 77.09% of stocks staying Short-Term in [0,45][0,45] and 77.08% in [46,90][46,90]. These high levels of within-event stability indicate that the horizon measure does not fluctuate mechanically around the announcement.

Table 3: Investor Horizon Measure Stability

|  |  |  |
| --- | --- | --- |
| Panel A: Switching Behavior | | |
| Event Time | | |
| [-90, -1] | [0, 45] | [46, 90] |
| Long Term | 72.2% | 65.65% |
| Short Term | 77.09% | 77.08% |
| Panel B: Persistence | | |
|  | Percent of time classified as | |
| ↓\downarrow Investor Horizon at t=t′t=t^{\prime} | Long-Term | Short-Term |
| Long Term | 70.1% | 29.9% |
| Short Term | 31.0% | 69.0% |

* •

  Notes: This table evaluates the stability of our measure. Panel A reports, for each announcement, the share of stocks that retain their initial “Long-Term” or “Short-Term” label when moving from the [−90,−1][-90,-1]-day pre-announcement window to the [0,45][0,45] and [46,90][46,90] windows around the event, demonstrating the within-event stability of our horizon measure. Panel B shows, for each firm, the average fraction of announcements on which its stock maintains the same initial classification, highlighting across-announcement persistence.

Panel B assesses persistence across earnings announcements at the firm level. Among firms initially classified as Long-Term, 70.1% of their announcements are also labeled Long-Term, while 29.9% fall into the Short-Term category. Conversely, firms initially classified as Short-Term remain in that category for 69.0% of their announcements. Moreover, 11.27% of firms are classified as Long-Term at every announcement, 15.10% are always Short-Term, and the remaining 73.63% switch at least once. Although the measure shows substantial persistence, there is also meaningful switching across announcements. Hence, when we include firm fixed effects in our regressions to control for time‐invariant heterogeneity, this level of persistence leaves ample within‐stock variation for identification.

## 3 A Model of Earnings Announcement Reactions and Investor Horizons

This section develops a simple rational-expectations model in which investors differ in their trading horizons. The framework is designed to capture how short- and long-term investors process earnings news differently and how these differences can translate into heterogeneous price reactions around earnings announcements. The model provides clear comparative statics that generate horizon-dependent patterns in immediate and delayed returns, guiding the empirical analysis that follows.

### Setup

We consider a market over three periods, indexed by t=1,2,3t=1,2,3, with two assets: a risk-free asset yielding a zero interest rate, normalized to have a constant price of 11; and a risky asset with an uncertain liquidation value θ\theta that is publicly revealed at date t=3t=3. The prices of the risky asset at dates t=1t=1 and t=2t=2 are denoted by p1p\_{1} and p2p\_{2}, respectively. The risky asset has a fixed supply K¯\bar{K}.

There are two types of investors with different investment horizons: Short-term investors (SS): They plan to hold the risky asset from date t=1t=1 to date t=2t=2 and may re-balance their portfolios at date t=2t=2 based on new information. Long-term investors (LL): They plan to hold the risky asset from date t=1t=1 to date t=3t=3 and do not trade at date t=2t=2. All investors are risk-averse, have mean-variance preferences, and are price-takers.

### Information Structure

At date t=1t=1, investors receive private signals about the future values of the risky asset.

#### Short-term Investors

Each short-term investor i∈Si\in S observes a private signal about the upcoming earnings announcement ee at date t=2t=2:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ziS=e+ϵiS,z\_{i}^{S}=e+\epsilon\_{i}^{S}, |  | (1) |

where ϵiS∼𝒩​(0,σS2)\epsilon\_{i}^{S}\sim\mathcal{N}(0,\sigma\_{S}^{2}) is an idiosyncratic noise term.

#### Long-term Investors

Each long-term investor j∈Lj\in L observes a private signal about the fundamental value θ\theta at date t=3t=3:

|  |  |  |  |
| --- | --- | --- | --- |
|  | zjL=θ+ϵjL,z\_{j}^{L}=\theta+\epsilon\_{j}^{L}, |  | (2) |

where ϵjL∼𝒩​(0,σL2)\epsilon\_{j}^{L}\sim\mathcal{N}(0,\sigma\_{L}^{2}) is an idiosyncratic noise term.

#### Relationship between ee and θ\theta

The earnings announcement ee is informative about the fundamental value θ\theta, but may deviate from it due to short-term fluctuations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | e=θ+η,e=\theta+\eta, |  | (3) |

where η∼𝒩​(μη,ση2)\eta\sim\mathcal{N}(\mu\_{\eta},\sigma\_{\eta}^{2}) represents transitory components or noise in earnings that are not reflective of long-term fundamentals. We assume that θ\theta, η\eta, ϵiS\epsilon\_{i}^{S}, and ϵjL\epsilon\_{j}^{L} are independent random variables.

### Investor Expectations and Biases

We assume that short-term investors’ prior belief about ee has a positive bias:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼S​[e]=e^S=e^+b,b>0,\mathbb{E}^{S}[e]=\hat{e}\_{S}=\hat{e}+b,\quad b>0, |  | (4) |

where e^\hat{e} is the consensus expectation of ee, and bb represents the optimism bias of short-term investors.111This lines up with our empirical findings, i.e., short-term investors have systematically more optimistic expectations about the earnings announcement ee compared to long-term investors and the consensus. Long-term investors and the consensus have unbiased expectations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼L​[e]=e^,𝔼L​[θ]=θ^.\mathbb{E}^{L}[e]=\hat{e},\quad\mathbb{E}^{L}[\theta]=\hat{\theta}. |  | (5) |

### Payoffs and Utility Functions

All investors have mean-variance utility functions defined over their wealth at their respective investment horizons.

#### Short-term Investors

A short-term investor ii plans to liquidate at date t=2t=2. Her utility function at date t=1t=1 is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | UiS=𝔼iS​[Wi,2]−γ2​VariS​[Wi,2],U\_{i}^{S}=\mathbb{E}\_{i}^{S}[W\_{i,2}]-\frac{\gamma}{2}\text{Var}\_{i}^{S}[W\_{i,2}], |  | (6) |

where Wi,2=kiS​p2+(1−kiS​p1)W\_{i,2}=k\_{i}^{S}p\_{2}+(1-k\_{i}^{S}p\_{1}) is the wealth at date t=2t=2, kiSk\_{i}^{S} is the number of shares held from t=1t=1 to t=2t=2, and γ\gamma is the coefficient of absolute risk aversion.

#### Long-term Investors

A long-term investor jj plans to hold until date t=3t=3. Her utility function at date t=1t=1 is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | UjL=𝔼jL​[Wj,3]−γ2​VarjL​[Wj,3],U\_{j}^{L}=\mathbb{E}\_{j}^{L}[W\_{j,3}]-\frac{\gamma}{2}\text{Var}\_{j}^{L}[W\_{j,3}], |  | (7) |

where Wj,3=kjL​θ+(1−kjL​p1)W\_{j,3}=k\_{j}^{L}\theta+(1-k\_{j}^{L}p\_{1}) is the wealth at date t=3t=3, and kjLk\_{j}^{L} is the number of shares held from t=1t=1 to t=3t=3.

### Optimization and Equilibrium at Date t=1t=1

Investors choose their holdings of the risky asset at date t=1t=1 to maximize their expected utility.

#### Short-term Investors

Maximizing UiSU\_{i}^{S} with respect to kiSk\_{i}^{S} yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | kiS=𝔼iS​[p2]−p1γ​VariS​[p2],k\_{i}^{S}=\frac{\mathbb{E}\_{i}^{S}[p\_{2}]-p\_{1}}{\gamma\text{Var}\_{i}^{S}[p\_{2}]}, |  | (8) |

where 𝔼iS​[p2]\mathbb{E}\_{i}^{S}[p\_{2}] is investor ii’s expectation of the price at date t=2t=2, conditional on their information at date t=1t=1. Short-term investors form expectations about p2p\_{2} based on their biased expectations of ee and the anticipated market reaction. Since they are optimistic about ee, they expect a higher p2p\_{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼iS​[p2]=𝔼iS​[p2|ziS,e^S]=𝔼​[p2|e=e^S+ziS−e^S],\mathbb{E}\_{i}^{S}[p\_{2}]=\mathbb{E}\_{i}^{S}[p\_{2}|z\_{i}^{S},\hat{e}\_{S}]=\mathbb{E}[p\_{2}|e=\hat{e}\_{S}+z\_{i}^{S}-\hat{e}\_{S}], |  | (9) |

where ziS−e^Sz\_{i}^{S}-\hat{e}\_{S} represents the deviation of their private signal from their biased prior.

#### Long-term Investors

Maximizing UjLU\_{j}^{L} with respect to kjLk\_{j}^{L} yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | kjL=𝔼jL​[θ]−p1γ​VarjL​[θ].k\_{j}^{L}=\frac{\mathbb{E}\_{j}^{L}[\theta]-p\_{1}}{\gamma\text{Var}\_{j}^{L}[\theta]}. |  | (10) |

Long-term investors form expectations about θ\theta based on their unbiased private signals:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​jL​[θ]=𝔼​[θ|zjL]=θ^+σ​θ2σθ2+σL2​(zjL−θ^).\mathbb{E}j^{L}[\theta]=\mathbb{E}[\theta|z\_{j}^{L}]=\hat{\theta}+\frac{\sigma{\theta}^{2}}{\sigma\_{\theta}^{2}+\sigma\_{L}^{2}}(z\_{j}^{L}-\hat{\theta}). |  | (11) |

#### Market Clearing at Date t=1t=1

The market-clearing condition at date t=1t=1 is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫i∈SkiS,d​i+∫j∈LkjL,d​j=K¯.\int\_{i\in S}k\_{i}^{S},di+\int\_{j\in L}k\_{j}^{L},dj=\bar{K}. |  | (12) |

#### Price Formation at Date t=1t=1

The equilibrium price p1p\_{1} adjusts so that the market clears. Due to the optimism bias of short-term investors, their aggregate demand is higher, putting upward pressure on p1p\_{1}.

### Events at Date t=2t=2

At date t=2t=2, the earnings announcement ee is publicly revealed. Short-term investors update their beliefs about the fundamental value θ\theta based on ee.

#### Short-term Investors

Upon observing ee, which may be lower than their optimistic expectation e^S\hat{e}\_{S}, short-term investors adjust their expectations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼iS,2​[θ]=θ^+σ​θ2σ​θ2+ση2​(e−θ^).\mathbb{E}\_{i}^{S,2}[\theta]=\hat{\theta}+\frac{\sigma{\theta}^{2}}{\sigma{\theta}^{2}+\sigma\_{\eta}^{2}}(e-\hat{\theta}). |  | (13) |

Given that ee may be lower than their biased expectation e^S\hat{e}\_{S}, short-term investors may find ee disappointing, leading to a downward revision of their expectations of θ\theta.

#### Trading Behavior at Date t=2t=2

Short-term investors decide whether to hold or sell the risky asset based on their updated expectations. If ee is lower than their optimistic expectation, they are likely to sell, exerting downward pressure on p2p\_{2}.

#### Price Reaction at Date t=2t=2

The price change from p1p\_{1} to p2p\_{2} reflects the aggregate trading behavior of investors:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p2−p1=Δ​p=1λ​(∫i∈SΔ​kiS,d​i),p\_{2}-p\_{1}=\Delta p=\frac{1}{\lambda}\left(\int\_{i\in S}\Delta k\_{i}^{S},di\right), |  | (14) |

where λ\lambda is a price impact parameter, and Δ​kiS\Delta k\_{i}^{S} is the change in holdings by short-term investor ii. Due to the short-term investors’ optimistic bias, the negative surprise (when e<e^Se<\hat{e}\_{S}) leads to larger selling pressure, causing a more negative immediate price reaction.

### Simulation

To illustrate the theoretical model and support our analytical results, we conduct a simulation replicating the market dynamics between short-term and long-term investors with different expectations. Setting b=0.5b=0.5 and γ=2.0\gamma=2.0, with standard deviations σθ=0.25\sigma\_{\theta}=0.25, ση=0.5\sigma\_{\eta}=0.5, σS=1.0\sigma\_{S}=1.0, σL=1.0\sigma\_{L}=1.0, we observe that short-term investors exhibit lower abnormal returns across all deciles due to optimism bias (see Figure [2](https://arxiv.org/html/2512.00280v1#S3.F2 "Figure 2 ‣ Simulation ‣ 3 A Model of Earnings Announcement Reactions and Investor Horizons ‣ Retail Investor Horizon and Earnings Announcements")). Additional details on the simulation setup and methodology are provided in Appendix B.

![Refer to caption](x4.png)


Figure 2: Model Simulation



Notes: This figure illustrates the results of the model simulation examining abnormal returns for stocks predominantly held by short-term versus long-term investors following earnings announcements. The simulation is based on key parameters: optimism bias b=0.5b=0.5 for short-term investors and risk aversion coefficient γ=2.0\gamma=2.0. Deciles are formed based on earnings surprises, with mean abnormal returns and standard deviations plotted for each investor type. Error bars represent the standard deviations within each decile.

### Implications

The model delivers clear predictions for how investor horizons shape price reactions to earnings news. Short-horizon investors, who over-extrapolate recent information, tend to enter the announcement with inflated expectations. As a result, negative surprises trigger sharp selling pressure, while even positive announcements may generate muted responses when they fall short of these elevated priors. Long-horizon investors, by contrast, form expectations around fundamental value and therefore react more moderately in the immediate window. Because prices partially reflect short-term optimism before the announcement, stocks held predominantly by short-horizon investors are more prone to post-announcement reversals. In contrast, stocks followed by long-horizon investors, which begin closer to fundamental value, experience a gradual upward adjustment as information is incorporated. The model therefore rationalizes asymmetric immediate reactions and horizon-dependent drift around earnings events.

## 4 Methodology

We closely follow the approach of dellavigna:2009. The earnings surprise is measured using the actual historical quarterly earnings per share and the consensus forecast of quarterly earnings per share from I/B/E/S, scaled by the historical price per share from the Center for Research in Security Prices (CRSP):

|  |  |  |  |
| --- | --- | --- | --- |
|  | st,k=et,k−e^t,kpt−5,k,s\_{t,k}=\frac{e\_{t,k}-\hat{e}\_{t,k}}{p\_{t-5,k}}, |  | (15) |

where et,ke\_{t,k} is the earnings per share announcement of company kk released on day tt; e^t,k\hat{e}\_{t,k} is the related consensus analyst forecast, defined as the median forecast among all analysts who made a forecast in the last 30 trading days prior to the earnings announcement date tt; and pt−5,kp\_{t-5,k} is the price per share for firm kk five days preceding the announcement. An interpretation of the surprise measure is the unexpected profits as a share of the total market value of the company. For example, an earnings surprise of st,k=0.01s\_{t,k}=0.01 means that the company earned unexpected profits equal to one percent of its market value.

To explore the stock reaction to earnings surprises, each announcement date is matched with stock returns, market capitalization, and trading volume from CRSP. The cumulative abnormal return (CAR) and buy-and-hold abnormal return (BHAR) is constructed for different event time windows as follows. Let Rj,kR\_{j,k} be the raw return on stock kk and RM,jR\_{M,j} the return on the value-weighted CRSP market index on trading day jj; rf,jr\_{f,j} is the one-month Treasury bill rate (continuously compounded) on the same day. Define excess returns rj,k=Rj,k−rf,jr\_{j,k}=R\_{j,k}-r\_{f,j} and rM,j=RM,j−rf,jr\_{M,j}=R\_{M,j}-r\_{f,j}. For each announcement we estimate the market model over the
pre-event window We=[t−300,t−46]W\_{e}=[\,t-300,\;t-46\,]:

|  |  |  |
| --- | --- | --- |
|  | rj,k=αk+βk​rM,j+εj,k,j∈We.r\_{j,k}=\alpha\_{k}+\beta\_{k}\,r\_{M,j}+\varepsilon\_{j,k},\qquad j\in W\_{e}. |  |

The daily abnormal return is

|  |  |  |
| --- | --- | --- |
|  | A​Rj,k=rj,k−α^k−β^k​rM,j.AR\_{j,k}=r\_{j,k}-\hat{\alpha}\_{k}-\hat{\beta}\_{k}\,r\_{M,j}. |  |

For an event window [h,H][h,H] (in trading days relative to the announcement date tt) the cumulative abnormal return is

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​A​Rkh,H=∑j=t+ht+HA​Rj,k.CAR\_{k}^{h,H}=\sum\_{j=t+h}^{t+H}AR\_{j,k}. |  | (A3) |

The buy-and-hold abnormal return is calculated on raw (gross) returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​H​A​Rkh,H=∏j=t+ht+H(1+Rj,k)−∏j=t+ht+H[1+rf,j+β^k​rM,j]BHAR\_{k}^{h,H}=\prod\_{j=t+h}^{t+H}\!(1+R\_{j,k})-\;\prod\_{j=t+h}^{t+H}\Bigl[1+r\_{f,j}+\hat{\beta}\_{k}\,r\_{M,j}\Bigr] |  | (A4) |

If the expected return is modeled with the Fama–French three factors, Carhart momentum, or the five-factor extension, replace the term β^k​rM,j\hat{\beta}\_{k}\,r\_{M,j} in (A2)–(A4) with ∑q=1Kβ^k(q)​fj(q)\displaystyle\sum\_{q=1}^{K}\hat{\beta}\_{k}^{(q)}\,f\_{j}^{(q)}, where fj(q)∈{S​M​B,H​M​L,U​M​D,R​M​W,C​M​A}f\_{j}^{(q)}\in\{SMB,HML,UMD,RMW,CMA\} and K∈{3,4,5}K\in\{3,4,5\}; the β^k(q)\hat{\beta}^{(q)}\_{k} are estimated over WeW\_{e}.

## 5 Primary Findings

In this section, we examine how stock returns respond to earnings surprises over different time horizons. Specifically, we compare the responsiveness for announcements followed by long-term retail investors to those followed by short-term investors. We present visual evidence and carry out regression analyses to support our findings.

### 5.1 Immediate Reaction

Figure [3](https://arxiv.org/html/2512.00280v1#S5.F3 "Figure 3 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements")(a) breaks down the immediate abnormal return following each announcement by whether long-term or short-term investors dominate the ensuing discussion. Across every earnings-surprise quintile, stocks with a heavier long-term investor presence see noticeably stronger initial price reactions than those led by shorter-horizon traders. To formally test this observation, we estimate the following regression model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​H​A​Rt,k0,1=α+β×𝕀t,k,Long-term=1+∑j=211[δj×𝕀t,k,Earnings Quantile=j]+γk×Xt,k+λt+ηk+ϵt,k,BHAR^{0,1}\_{t,k}=\alpha+\beta\times\mathbb{I}\_{t,k,\text{Long-term}=1}+\sum\_{j=2}^{11}\Big[\delta\_{j}\times\mathbb{I}\_{t,k,\text{Earnings Quantile}=j}\Big]+\gamma^{k}\times X\_{t,k}+\lambda\_{t}+\eta\_{k}+\epsilon\_{t,k}, |  | (15) |

In Equation ([15](https://arxiv.org/html/2512.00280v1#S5.E15 "In 5.1 Immediate Reaction ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements")), B​H​A​Rt,k0,1BHAR^{0,1}\_{t,k} denotes the buy-and-hold abnormal return for stock kk at announcement tt from the close of the day before the earnings announcement to the close of the day after the announcement (i.e., days 0 to 1). The term 𝕀t,k,Long-term=1\mathbb{I}\_{t,k,\text{Long-term}=1} is an indicator variable equal to 1 if the announcement is classified as long-term, and 0 if short-term. The variables 𝕀t,k,Earnings Quantile=j\mathbb{I}\_{t,k,\text{Earnings Quantile}=j} are indicator variables for earnings surprise quantiles jj, where j=2,…,11j=2,\ldots,11. The vector Xt,kX\_{t,k} is a set of control variables which include the size of the security, the dispersion of analysts forecasts, the number of analysts, the buy-and-hold abnormal returns [-30, -1], valence and standard deviation of valence over [-30, -1], institutional ownership & turnover, volatility, and abnormal short interest. The term λt\lambda\_{t} represents time fixed effects (e.g., quarter and year dummies), and ϵt,k\epsilon\_{t,k} is the error term. To address the concern that companies followed by long-term investors may also have unobservable features that differ from companies followed by short-term investors, we control for firm fixed effects in some regression specifications (ηk\eta\_{k}). The standard errors account for heteroskedasticity as well as the correlation of errors across securities announcing on the same day by clustering observations by firm and day of the announcement.

The coefficient β\beta captures the additional immediate return response associated with long-term announcements compared to short-term announcements. A positive and significant β\beta indicates that long-term announcements have higher immediate abnormal returns, controlling for other factors.

Table [4](https://arxiv.org/html/2512.00280v1#S5.T4 "Table 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") reports estimates of the differential price reaction between stocks predominantly followed by long- versus short-horizon retail investors. In the baseline specification without controls or fixed effects (Column 1), the coefficient on the long-horizon indicator is 0.53 percentage points (s.e. 0.05 pp; p<0.01p<0.01), indicating a meaningfully stronger two-day response for long-horizon stocks. Conditioning on the full vector of firm- and announcement-level covariates together with firm and year–quarter fixed effects (Column 2) reduces the estimate to 0.21 pp (s.e. 0.06 pp; p<0.01p<0.01). A propensity-score-matching specification (Column 3) delivers a slightly smaller estimate of 0.16 pp (s.e. 0.09 pp; p<0.10p<0.10).

The cross-sectional heterogeneity by news type is striking. For negative earnings surprises (Columns 4–6), the long-horizon coefficient becomes small and statistically indistinguishable from zero once controls and fixed effects are included (Column 5). In contrast, for positive earnings surprises (Columns 7–9), the fully saturated specification (Column 8) yields a sizeable and precisely estimated effect of 0.28 pp (s.e. 0.08 pp; p<0.01p<0.01). Thus, the differential reaction between long- and short-horizon stocks is concentrated in good-news environments, consistent with long-horizon investors reacting more strongly to favorable information.

Panel A of Table [5](https://arxiv.org/html/2512.00280v1#S5.T5 "Table 5 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") estimates the immediate price reaction separately by earnings-surprise group. Across the five negative-surprise groups, the long-horizon coefficient is uniformly small and statistically indistinguishable from zero: estimates range from 0.07 bp in group −5-5 to 19 bp in group −1-1, with standard errors between 24–35 bp. The no-surprise category exhibits a modest and statistically significant premium of 0.56 pp (s.e. 0.28 pp; p<0.10p<0.10). On the positive side, the differential reaction strengthens. The coefficient is 0.22 pp for group +1+1 (s.e. 0.15 pp), becomes statistically significant in groups +2+2 and +4+4 (0.39 pp and 0.53 pp, respectively), and remains positive in group +5+5 (0.43 pp; s.e. 0.22 pp; p<0.10p<0.10). Overall, significant long–short differences emerge only in the no-surprise and positive-surprise bins, and they increase monotonically through the middle of the positive tail.

Investor horizon predicts how quickly, and how strongly, prices incorporate earnings information. The effect is highly asymmetric: we find no significant difference in the immediate price reaction between long- and short-horizon stocks following negative news. In contrast, prices of long-horizon securities rise more on good news and react more favorably when there is no surprise. These patterns, particularly the monotonic increase in the differential premium across positive-surprise quantiles, suggest that long-horizon investors trade more aggressively around favorable information events, generating larger and more precisely estimated immediate abnormal returns for the stocks they follow.

### 5.2 Delayed Reaction

We next turn to the delayed reaction, measured as the buy-and-hold abnormal return from day 2 to day 75. Figure [3](https://arxiv.org/html/2512.00280v1#S5.F3 "Figure 3 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements")(c) plots the average drift by surprise decile and shows that the long-horizon line lies above the short-horizon line in every bin, with the gap widening in the extreme tails.

To assess post-announcement drift, we re-estimate Equation ([15](https://arxiv.org/html/2512.00280v1#S5.E15 "In 5.1 Immediate Reaction ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements")) using the buy-and-hold abnormal return from days 2 to 75 as the dependent variable. Panel B of Table [4](https://arxiv.org/html/2512.00280v1#S5.T4 "Table 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") reports the results. In the specification without controls or fixed effects (Column 1), long-horizon stocks earn a 2.83 pp higher return over the 2–75 day window (s.e. 0.22 pp; p<0.01p<0.01). Conditioning on the full set of announcement- and firm-level controls, together with firm and year–quarter fixed effects (Column 2), reduces the estimate to 2.08 pp (s.e. 0.21 pp; p<0.01p<0.01). The propensity-score–weighted specification (Column 3) yields a closely related estimate of 1.61 pp (s.e. 0.28 pp; p<0.01p<0.01). Thus, between 1.5 and 2.8 percentage points of additional drift accrues to long-horizon stocks, even after extensive conditioning.

The pattern is similar when the sample is split by news type. For negative surprises (Column 5), the fully saturated coefficient is 1.81 pp (s.e. 0.39 pp; p<0.01p<0.01). For positive surprises (Column 8), the corresponding estimate is 2.18 pp (s.e. 0.27 pp; p<0.01p<0.01). Hence, the drift differential is not concentrated exclusively in good-news events.

Panel B of Table [5](https://arxiv.org/html/2512.00280v1#S5.T5 "Table 5 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") examines drift by earnings-surprise category, re-estimating Column 2 specification of Table [4](https://arxiv.org/html/2512.00280v1#S5.T4 "Table 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements"). Long-horizon coefficients are positive in most bins and statistically significant in the moderate-to-extreme surprise groups on both sides of the distribution. Effects range from 1.47 pp in the most negative bin to 3.17 pp in the +4+4 bin, with statistical significance in more than half of the categories. The delayed-return premium for long-horizon stocks therefore appears broad-based, spanning both negative and positive surprise environments and strengthening in the tails of the distribution.

These results show that the horizon differential documented in the first two trading days does not dissipate; it widens materially over the subsequent quarter. Across specifications, long-horizon stocks earn an additional 2–3 pp of abnormal return relative to short-horizon stocks over days 2–75, and this drift emerges in both negative- and positive-surprise environments. The by-bin estimates in Panel B of Table [5](https://arxiv.org/html/2512.00280v1#S5.T5 "Table 5 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") further indicate that the premium is broad-based: coefficients are uniformly positive and become largest and most precisely estimated in the moderate-to-extreme surprise categories. Overall, the evidence points to a systematic and economically meaningful post-announcement drift in the stocks followed by long-horizon investors, consistent with prices adjusting more slowly to earnings news for these firms.

### 5.3 Total Reaction

Panel C of Table [4](https://arxiv.org/html/2512.00280v1#S5.T4 "Table 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") aggregates the immediate and delayed windows by regressing the buy-and-hold abnormal return from day 0 to day 75 on the long-term indicator. In the specification without controls or fixed effects (Column 1), securities followed predominantly by long-horizon investors earn 3.41 pp more than those followed by short-horizon investors (s.e. 0.23 pp; p<0.01p<0.01). Conditioning on the full set of covariates Xt,kX\_{t,k} together with firm and year–quarter fixed effects (Column 2) reduces the estimate to 2.31 pp (s.e. 0.23 pp; p<0.01p<0.01). The propensity-score–weighted specification (Column 3) delivers 1.81 pp(s.e. 0.31 pp; p<0.01p<0.01). When the sample is partitioned by the sign of the earnings surprise, the long-term coefficient remains positive and significant: 1.90 pp for negative surprises (Column 5; s.e. 0.42 pp; p<0.01p<0.01) and 2.56 pp for positive surprises (Column 8; s.e. 0.29 pp; p<0.01p<0.01). Thus, long-horizon stocks outperform short-horizon stocks over the full 0–75 day window in every specification and for both good- and bad-news announcements.

Panel C of Table [5](https://arxiv.org/html/2512.00280v1#S5.T5 "Table 5 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") shows that the long-term coefficient is positive in every earnings-surprise category, with magnitudes ranging from 1.40 pp in the most negative bin to 3.90 pp in the +4+4 bin. Eight of the eleven coefficients are statistically significant at conventional levels, including the −4-4, −3-3, −1-1, no-surprise, +2+2, +3+3, +4+4, and +5+5 groups. The strongest effects appear in the middle-to-upper part of the positive distribution, where estimates reach 3.06–3.90 pp. Even in the negative-surprise bins, the point estimates remain uniformly positive.

These estimates indicate that the horizon effect is not confined to the first two trading days but continues to accumulate over the full post–announcement window. Across specifications, securities followed predominantly by long–horizon retail investors earn between 1.8 and 3.4 percentage points more than those followed by short–horizon investors over days 0–75, an economically meaningful magnitude for a single quarterly earnings event. The persistence and breadth of this differential, appearing after both negative and positive surprises, echoes the classic post–earnings–announcement–drift (PEAD) pattern of slow information incorporation. In our setting, the drift is systematically stronger among firms with a longer–horizon retail investor base. One interpretation is that investor horizons shape the speed at which beliefs about future cash flows are incorporated into prices: long–horizon investors may update more gradually, generating a sustained price adjustment, whereas short–horizon investors react more immediately, leaving less scope for drift. The result is a robust and economically significant horizon–based wedge in post–announcement price dynamics.222Appendix A presents comprehensive robustness checks, including alternative risk factor models (three-, four-, and five-factor specifications), sensitivity to different post-announcement event windows, variations in propensity score matching parameters, and tests for the impact of winsorization.

### 5.4 Performance of Drift

A zero-cost portfolio that is long the long-term group and short the short-term group does not require immediate trading after the announcement. Panel (a) of Figure [4](https://arxiv.org/html/2512.00280v1#S5.F4 "Figure 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") shows that the cumulative buy-and-hold abnormal return for this portfolio drifts only mildly during the first two trading weeks, but then accelerates sharply. Between trading days 20 and 75 the strategy earns an additional three percentage points, indicating that substantial abnormal returns remain available well after the initial price response. The evidence points to a repricing process that continues over several weeks rather than concluding in the immediate aftermath of the earnings release.

We next examine whether this drift varies with the market’s prevailing tone. Using the emotion extraction procedure of (vamossy2023emtract) applied to social-media posts from the [−90,−1][-90,-1] window, we classify firms as *bullish* or *bearish* based on the sign of their average valence. Panel (b) of Figure [4](https://arxiv.org/html/2512.00280v1#S5.F4 "Figure 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") replicates the long-minus-short portfolio within each sentiment group. The drift appears exclusively among bullish firms, with little to no effect for bearish firms. This pattern suggests that favorable sentiment amplifies the delayed price adjustment, consistent with horizon-driven underreaction being stronger when the tone of investor discourse is positive.

### 5.5 Trading Strategy

We implement a simple monthly zero-cost strategy to gauge investability and the economic magnitude of the horizon channel effect. The strategy is designed to isolate the drift component by using announcement information from month t−1t-1 to predict returns in month tt. At the end of month t−1t-1, all stocks with an earnings announcement are identified and assigned to one of eleven earnings-surprise bins. Within each bin, we form a zero-cost portfolio that goes long stocks predominantly followed by Long-Term retail investors and short stocks predominantly followed by Short-Term retail investors. Each bin-level portfolio is *equal-weighted across firms*, and the aggregate strategy return is simply the equal-weighted return across all stocks in all bins. The portfolio is rebalanced monthly using the latest earnings announcements and updated horizon classifications. We then analyze the factor-adjusted alphas of the aggregate LT–ST portfolio, the portfolio restricted to the top three surprise bins, and the results for each bin separately.

Table [6](https://arxiv.org/html/2512.00280v1#S5.T6 "Table 6 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") presents Fama–French Five-Factor regressions for the horizon-sorted long–short drift portfolios. The portfolio across all bins (Column 1) displays a clear defensive profile, loading negatively on the market factor and positively on both value (HML) and profitability (RMW). These exposures indicate that long-term-investor stocks resemble more profitable and value-oriented firms, whereas short-term-investor stocks lean toward growth and lower profitability. Despite these tilts, the portfolio delivers a statistically significant alpha of roughly 30 bps per month, implying economically meaningful abnormal returns beyond standard factor compensation. The Top-3-bin portfolio (Column 2) shows nearly identical factor structure but produces an even larger and more precisely estimated alpha of nearly 40 bps per month, suggesting that concentrating weights on the bins associated with the strongest drift amplifies the signal.

Factor loadings vary substantially across the earnings-surprise bins (Columns 3–13). Many bins load positively on value and profitability, reinforcing the idea that long-term investors systematically hold higher-quality, more value-like firms. Several bins also exhibit negative market betas, reflecting a defensive component that persists throughout the cross-section. CMA loadings alternate in sign, indicating that horizon-based spreads do not line up cleanly with investment intensity across bins. Alphas at the bin level are mostly positive but imprecise, expected given the much higher noise in narrow long–short portfolios. Two bins stand out: Bin 6 and Bin 9, which generate statistically significant and economically large alphas. In contrast, the remaining bins have estimates clustered near zero with wide confidence intervals, indicating considerable heterogeneity in how investor horizons interact with earnings news.

These results show that horizon-sorted long–short drift portfolios earn positive risk-adjusted returns that are not absorbed by standard factor exposures. Long-horizon stocks resemble high-quality value firms, yet the residual alpha remains significant even after controlling for these characteristics. The performance is strongest in the bins where disagreement between long- and short-horizon investors is most pronounced, which aligns with the earlier finding that long-horizon investors react more strongly to favorable earnings news while the delayed adjustment appears in both good- and bad-news environments. Aggregating across bins, or concentrating on those with the largest ex post drift, reduces idiosyncratic noise and reveals a robust and economically meaningful return premium associated with long-term investor orientation.

![Refer to caption](x5.png)


(a) Response to Earnings Surprise from 0 to 1

![Refer to caption](x6.png)


(b) Nonlinear Earnings Response From 0 to 1

![Refer to caption](x7.png)


(c) Response to Earnings Surprise from 2 to 75

Figure 3: Immediate (a-b) and delayed (c) response to earnings surprises



Notes: Figure [3](https://arxiv.org/html/2512.00280v1#S5.F3 "Figure 3 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") illustrates the mean buy-and-hold abnormal return reactions. From January 2010 until June 2021, stocks in CRSP are matched with quarterly earnings announcements in I/B/E/S. In the timeline of the event, the day of the announcement is designated as day 0. The buy-and-hold abnormal return for each stock is the raw buy-and-hold return adjusted based on the estimated beta from the market model. The earnings surprise for an announcement is defined as the difference between the actual earnings for the quarter, as recorded by I/B/E/S, and the median analyst forecast featured in the I/B/E/S detail file within the 30 days preceding the quarterly earnings announcement. This is then scaled by the stock price 5 trading days before the announcement. Earnings announcements are divided into 11 groups: Quintiles 1 to 5 consist of five quintiles of negative earnings surprises, while quintiles 7 to 11 comprise five quintiles of positive earnings surprises. Quintile 6 includes all announcements where the earnings surprise is zero. The breakpoints are determined quarterly.



![Refer to caption](x8.png)


(a) Performance of drift at different horizons

![Refer to caption](x9.png)


(b) Performance of drift at different horizons by emotions

Figure 4: Post-earnings announcement drift at different horizons, overall (a) and by emotions (b)



Notes: Figure [4](https://arxiv.org/html/2512.00280v1#S5.F4 "Figure 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") illustrates the mean buy-and-hold abnormal return reactions. From January 2010 until June 2021, stocks in CRSP are matched with quarterly earnings declarations in I/B/E/S. In the timeline of the event, the day of the announcement is designated as day 0. The buy-and-hold abnormal return for each stock is the raw buy-and-hold return adjusted based on the estimated beta from the market model. The measure for post-earnings announcement drift for horizon hh is the average buy-and-hold abnormal return from day 2 to day hh for long-term announcements minus the average buy-and-hold abnormal return from day 2 to day hh for short-term announcements. Panel (b) estimates this Δ​BHARh\Delta\mathrm{BHAR}\_{h} separately for the subsample of stocks with predominantly bullish pre-announcement sentiment and for the subsample with predominantly bearish sentiment in the [−90,−1][-90,-1] window.




Table 4: Response to Earnings Surprise

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) |
| Panel A. Immediate Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 1 | | | | | | | |  |  |
| Long-Term | 0.0053∗∗∗ | 0.0021∗∗∗ | 0.0016∗ | 0.0045∗∗∗ | 0.0015 | -0.0002 | 0.0052∗∗∗ | 0.0028∗∗∗ | 0.0035∗∗∗ |
|  | (0.0005) | (0.0006) | (0.0009) | (0.0010) | (0.0012) | (0.0017) | (0.0007) | (0.0008) | (0.0012) |
| Constant | -0.0033∗∗∗ | 0.0110∗∗∗ | -0.0003 | -0.0299∗∗∗ | -0.0081∗ | -0.0258∗∗∗ | 0.0123∗∗∗ | 0.0178∗∗∗ | 0.0149∗∗∗ |
|  | (0.0004) | (0.0025) | (0.0005) | (0.0009) | (0.0042) | (0.0009) | (0.0006) | (0.0034) | (0.0006) |
| R2R^{2} | 0.0851 | 0.1522 | 0.2076 | 0.0083 | 0.2119 | 0.2902 | 0.0300 | 0.1464 | 0.2181 |
| Panel B. Delayed Reaction: Buy-and-Hold Abnormal Return in Event Time 2 to 75 | | | | | | | |  |  |
| Long-Term | 0.0283∗∗∗ | 0.0208∗∗∗ | 0.0161∗∗∗ | 0.0277∗∗∗ | 0.0181∗∗∗ | 0.0137∗∗∗ | 0.0283∗∗∗ | 0.0218∗∗∗ | 0.0192∗∗∗ |
|  | (0.0022) | (0.0021) | (0.0028) | (0.0034) | (0.0039) | (0.0053) | (0.0025) | (0.0027) | (0.0037) |
| Constant | -0.0400∗∗∗ | 0.0519∗∗∗ | -0.0286∗∗∗ | -0.0409∗∗∗ | 0.0606∗∗∗ | -0.0284∗∗∗ | -0.0393∗∗∗ | 0.0410∗∗∗ | -0.0289∗∗∗ |
|  | (0.0022) | (0.0077) | (0.0015) | (0.0033) | (0.0128) | (0.0027) | (0.0022) | (0.0113) | (0.0019) |
| R2R^{2} | 0.0043 | 0.1536 | 0.1778 | 0.0036 | 0.2411 | 0.2908 | 0.0046 | 0.1732 | 0.2200 |
| Panel C. Total Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 75 | | | | | | | |  |  |
| Long-Term | 0.0341∗∗∗ | 0.0231∗∗∗ | 0.0181∗∗∗ | 0.0322∗∗∗ | 0.0190∗∗∗ | 0.0132∗∗ | 0.0343∗∗∗ | 0.0256∗∗∗ | 0.0234∗∗∗ |
|  | (0.0023) | (0.0023) | (0.0031) | (0.0035) | (0.0042) | (0.0057) | (0.0027) | (0.0029) | (0.0040) |
| Constant | -0.0436∗∗∗ | 0.0643∗∗∗ | -0.0290∗∗∗ | -0.0717∗∗∗ | 0.0544∗∗∗ | -0.0547∗∗∗ | -0.0268∗∗∗ | 0.0586∗∗∗ | -0.0134∗∗∗ |
|  | (0.0023) | (0.0085) | (0.0016) | (0.0035) | (0.0138) | (0.0030) | (0.0023) | (0.0123) | (0.0020) |
| R2R^{2} | 0.0151 | 0.1603 | 0.1859 | 0.0039 | 0.2336 | 0.2894 | 0.0108 | 0.1776 | 0.2251 |
| Year-Quarter Fixed Effects |  | X | X |  | X | X |  | X | X |
| Firm Fixed Effects |  | X | X |  | X | X |  | X | X |
| Controls |  | X | X |  | X | X |  | X | X |
| Observations | 104,919 | 104,703 | 75,080 | 33,722 | 33,155 | 24,820 | 63,395 | 62,977 | 43,751 |

* •

  Notes: Table [4](https://arxiv.org/html/2512.00280v1#S5.T4 "Table 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") reports the coefficients of a regression of the immediate response of securities to earning surprises defined by the following regression:

  |  |  |  |
  | --- | --- | --- |
  |  | B​H​A​Rt,kw=α+β×𝕀t,k,Long-term=1+∑j=211[δj×𝕀t,k,Earnings Quantile=j]+γk×Xt,k+λt+ηk+ϵt,k,BHAR^{w}\_{t,k}=\alpha+\beta\times\mathbb{I}\_{t,k,\text{Long-term}=1}+\sum\_{j=2}^{11}\Big[\delta\_{j}\times\mathbb{I}\_{t,k,\text{Earnings Quantile}=j}\Big]+\gamma^{k}\times X\_{t,k}+\lambda\_{t}+\eta\_{k}+\epsilon\_{t,k}, |  |

  where B​H​A​Rt,kwBHAR^{w}\_{t,k} is defined as in Equation ([A4](https://arxiv.org/html/2512.00280v1#S4.Ex6 "In 4 Methodology ‣ Retail Investor Horizon and Earnings Announcements")). β\beta is the added response of the securities in the group followed by long-term investors; δ\delta capture the relation between the earning surprise and the immediate response; Xt,kX\_{t,k} is a set of control variables which include the size of the security, the dispersion of analysts forecasts, the number of analysts, the buy-and-hold abnormal returns [-30, -1], valence and standard deviation of valence over [-30, -1], institutional ownership & turnover, volatility, and abnormal short interest. To address the concern that companies followed by long-term investors may also have unobservable features that differ from companies followed by short-term investors, we control for firm fixed effects in most regression specifications. Finally, we also include time fixed effects by year-quarter. The standard errors account for heteroskedasticity as well as correlation of errors across securities making an announcement on the same day by clustering observations by day of announcement and by firm. Table [4](https://arxiv.org/html/2512.00280v1#S5.T4 "Table 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") reports α\alpha and β\beta. Columns (1), (4) and (7) have no controls or fixed effects; Columns (2), (5), and (8) have the full set of control as defined in Xt,kX\_{t,k} along with firm and time fixed effects; Columns (3), (6), and (9) carries out matching on the control variables, followed by a regression with matching weights and time and firm fixed effects. Columns (4-6) are focusing on negative surprises, while Columns (7-9) are focusing on positive surprises, with and without control. To mitigate the impact of outliers, the dependent variables are winsorized at the 1st and 99th percentiles. ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01.




Table 5: Regressions of Earnings Response by Earning Surprise Groups

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Earnings Surprise Group | -5 | -4 | -3 | -2 | -1 | No News | 1 | 2 | 3 | 4 | 5 |
| Panel A. Immediate Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 1 | | | | | | | | | | | |
| Long-Term | 0.0007 | -0.0024 | -0.0010 | -0.0017 | 0.0019 | 0.0056∗ | 0.0022 | 0.0039∗∗ | 0.0033 | 0.0053∗∗ | 0.0043∗ |
|  | (0.0035) | (0.0034) | (0.0032) | (0.0029) | (0.0024) | (0.0028) | (0.0015) | (0.0019) | (0.0021) | (0.0022) | (0.0022) |
| Constant | -0.0221∗ | -0.0184∗ | 0.0008 | -0.0063 | 0.0008 | 0.0181 | 0.0089 | 0.0156∗ | 0.0213∗∗ | 0.0205∗∗ | 0.0273∗∗∗ |
|  | (0.0123) | (0.0111) | (0.0114) | (0.0118) | (0.0109) | (0.0121) | (0.0070) | (0.0080) | (0.0085) | (0.0084) | (0.0079) |
| R2R^{2} | 0.3000 | 0.3663 | 0.3838 | 0.3838 | 0.3345 | 0.3276 | 0.2133 | 0.2584 | 0.2636 | 0.2800 | 0.2678 |
| Panel B. Delayed Reaction: Buy-and-Hold Abnormal Return in Event Time 2 to 75 | | | | | | | | | | | |
| Long-Term | 0.0147 | 0.0319∗∗∗ | 0.0208∗∗ | 0.0125 | 0.0109∗ | 0.0190∗∗ | 0.0040 | 0.0203∗∗∗ | 0.0270∗∗∗ | 0.0317∗∗∗ | 0.0252∗∗∗ |
|  | (0.0117) | (0.0115) | (0.0100) | (0.0097) | (0.0066) | (0.0083) | (0.0043) | (0.0054) | (0.0058) | (0.0065) | (0.0072) |
| Constant | 0.0214 | 0.0252 | 0.0401 | 0.0598 | 0.0641∗∗ | 0.0352 | 0.0295 | 0.0098 | 0.0137 | -0.0142 | 0.0593∗∗ |
|  | (0.0353) | (0.0420) | (0.0411) | (0.0430) | (0.0303) | (0.0328) | (0.0219) | (0.0258) | (0.0233) | (0.0241) | (0.0272) |
| R2R^{2} | 0.3595 | 0.3710 | 0.4041 | 0.4032 | 0.3501 | 0.3701 | 0.2492 | 0.2892 | 0.3046 | 0.3264 | 0.3077 |
| Panel C. Total Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 75 | | | | | | | | | | | |
| Long-Term | 0.0140 | 0.0294∗∗ | 0.0198∗ | 0.0071 | 0.0127∗ | 0.0253∗∗∗ | 0.0066 | 0.0245∗∗∗ | 0.0306∗∗∗ | 0.0390∗∗∗ | 0.0311∗∗∗ |
|  | (0.0126) | (0.0121) | (0.0109) | (0.0102) | (0.0072) | (0.0088) | (0.0046) | (0.0060) | (0.0062) | (0.0070) | (0.0079) |
| Constant | 0.0070 | 0.0093 | 0.0378 | 0.0577 | 0.0653∗∗ | 0.0555 | 0.0357 | 0.0256 | 0.0349 | 0.0064 | 0.0888∗∗∗ |
|  | (0.0373) | (0.0450) | (0.0438) | (0.0434) | (0.0324) | (0.0353) | (0.0233) | (0.0275) | (0.0249) | (0.0265) | (0.0303) |
| R2R^{2} | 0.3591 | 0.3650 | 0.3898 | 0.3855 | 0.3565 | 0.3605 | 0.2536 | 0.2950 | 0.3091 | 0.3215 | 0.3082 |
| Observations | 5,923 | 5,680 | 5,551 | 5,605 | 5,837 | 6,636 | 11,977 | 11,798 | 11,737 | 11,687 | 11,801 |

* •

  Notes: For each of the five positive and negative surprise categories as well as the no surprise category, kk, where kk is a earning surprise category, we run the following regression:

  |  |  |  |
  | --- | --- | --- |
  |  | BHARt,kw=α+β×[Long-term=1]++γk×Xi​t+λt+ηk+ϵi​t,k,BHAR^{w}\_{t,k}=\alpha+\beta\times[\text{Long-term}=1]++\gamma^{k}\times X\_{it}+\lambda\_{t}+\eta\_{k}+\epsilon\_{it,k}, |  |

  where B​H​A​Rt,kwBHAR^{w}\_{t,k} is defined as in Equation ([A4](https://arxiv.org/html/2512.00280v1#S4.Ex6 "In 4 Methodology ‣ Retail Investor Horizon and Earnings Announcements")). β\beta is the added response of the securities in the group followed by long-term investors; Xt,kX\_{t,k} is a set of control variables which include the size of the security, the dispersion of analysts forecasts, the number of analysts, the buy-and-hold abnormal returns [-30, -1], valence and standard deviation of valence over [-30, -1], institutional ownership & turnover, volatility, and abnormal short interest. To address the concern that companies followed by long-term investors may also have unobservable features that differ from companies followed by short-term investors, we control include firm fixed effects. Finally, we also include time fixed effects by year-quarter. The standard errors account for heteroskedasticity as well as correlation of errors across securities making an announcement on the same day by clustering observations by day of announcement and by firm. Table [5](https://arxiv.org/html/2512.00280v1#S5.T5 "Table 5 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") reports α\alpha and β\beta. To mitigate the impact of outliers, the dependent variables are winsorized at the 1st and 99th percentiles. ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01.




Table 6: Factor Regressions for Long–Short Drift Portfolios by Horizon

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) | (10) | (11) | (12) | (13) |
|  | Overall | Top 3 | Bin 1 | Bin 2 | Bin 3 | Bin 4 | Bin 5 | Bin 6 | Bin 7 | Bin 8 | Bin 9 | Bin 10 | Bin 11 |
| Mkt-RF | -0.1664∗∗∗ | -0.1732∗∗∗ | -0.0399 | 0.0444 | -0.3360∗∗∗ | -0.3427∗∗ | -0.1168 | -0.1469 | -0.1222 | -0.1462 | -0.1095 | -0.2937∗∗∗ | -0.2160 |
|  | (0.0481) | (0.0545) | (0.1938) | (0.1636) | (0.1223) | (0.1573) | (0.1185) | (0.1031) | (0.0840) | (0.1024) | (0.0809) | (0.0945) | (0.1487) |
| SMB | 0.0561 | 0.0465 | -0.3620 | -0.0314 | -0.1746 | -0.2835 | 0.0635 | 0.1681 | 0.2597∗∗ | 0.1866 | 0.0473 | -0.0233 | 0.1597 |
|  | (0.0760) | (0.0864) | (0.2884) | (0.3331) | (0.2165) | (0.2272) | (0.2336) | (0.2417) | (0.1256) | (0.1479) | (0.1140) | (0.1676) | (0.2056) |
| HML | 0.2481∗∗∗ | 0.2116∗∗∗ | -0.3989 | 0.0418 | 0.2995 | 0.0356 | 0.3336∗∗ | 0.2942∗∗ | 0.3099∗∗∗ | 0.4116∗∗∗ | 0.1806 | 0.3877∗∗∗ | 0.0550 |
|  | (0.0478) | (0.0510) | (0.3500) | (0.2095) | (0.2739) | (0.2078) | (0.1287) | (0.1260) | (0.0889) | (0.1074) | (0.1162) | (0.1232) | (0.1224) |
| RMW | 0.3280∗∗∗ | 0.3585∗∗ | 0.3309 | 0.8090∗∗ | 0.2556 | 0.0965 | 0.3082 | 0.3034 | 0.3016 | 0.4114 | 0.2002∗ | 0.4296∗∗∗ | 0.4479 |
|  | (0.1126) | (0.1422) | (0.2498) | (0.3614) | (0.3141) | (0.2345) | (0.2263) | (0.2646) | (0.1827) | (0.2704) | (0.1151) | (0.1508) | (0.3644) |
| CMA | -0.1230 | -0.1773 | 0.6834 | 0.1818 | -0.1997 | 0.3052 | -0.8694∗∗∗ | 0.2252 | -0.0779 | -0.4546∗∗ | 0.1345 | -0.5018∗∗ | -0.1275 |
|  | (0.1238) | (0.1691) | (0.5676) | (0.4531) | (0.3795) | (0.2785) | (0.2732) | (0.3205) | (0.1746) | (0.2292) | (0.2627) | (0.2064) | (0.3123) |
| α\alpha | 0.2948∗∗ | 0.3810∗∗∗ | -0.1039 | -0.3288 | 0.3422 | 0.1595 | 0.2142 | 0.8011∗ | -0.0312 | 0.0735 | 0.4784∗∗ | 0.3636 | 0.2998 |
|  | (0.1223) | (0.1363) | (0.7572) | (0.5837) | (0.4924) | (0.3070) | (0.3148) | (0.4579) | (0.1971) | (0.3208) | (0.2163) | (0.3424) | (0.3587) |
| Observations | 136 | 136 | 136 | 136 | 136 | 136 | 136 | 136 | 136 | 136 | 136 | 136 | 136 |

* •

  Notes: This table reports Fama–French Five-Factor regressions of monthly excess returns for zero-cost horizon-channel portfolios. These portfolios are constructed by going long stocks predominantly followed by Long-Term investors and shorting stocks followed by Short-Term investors, within each earnings surprise bin. Columns report results for the overall Announcement-Weighted Portfolio (Column (1)), the Top Three Bin Announcement-Weighted Portfolio (Column (2)), and the individual bin difference portfolios (Columns (3-13)). All regressions include the market factor (Mkt–RF), SMB, HML, RMW, and CMA. Standard errors (in parentheses) are heteroskedasticity- and autocorrelation-robust using Newey–West with 6 lags. Stars denote significance levels: ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01.

## 6 Discussion

Building on our main findings that long- and short-horizon retail investors respond differently to earnings announcements, this section examines how those differences manifest in pre‐announcement behavior, sentiment dynamics, and communication patterns. Rather than treating horizon groups as mechanically distinct, we explore whether they differ in the information they emphasize, the mood they express around announcements, and the way these factors translate into return patterns. By analyzing pre‐EA momentum, testing an optimism–bias mechanism, and studying both hourly sentiment and message content, we shed light on why horizon-specific return responses arise and what they reveal about investors’ expectations and information processing.

### 6.1 Momentum

One potential non-behavioral explanation for our findings is simple momentum: if long-horizon stocks earn higher returns in the month leading up to earnings announcements, their stronger post-announcement performance could mechanically reflect continuation rather than differences in information processing. To assess this possibility, Figure [5](https://arxiv.org/html/2512.00280v1#S6.F5 "Figure 5 ‣ 6.1 Momentum ‣ 6 Discussion ‣ Retail Investor Horizon and Earnings Announcements") plots cumulative buy-and-hold abnormal returns from trading day −30-30 to −1-1. The two series move closely together, with the long-horizon group only marginally ahead throughout the pre-event window. Because our regressions already control for past abnormal returns [−30,−1][-30,-1], this slight lead is absorbed in the specification and does not drive our post-announcement results. The return differentials we document therefore arise after the announcement and reflect how the two investor groups process new information rather than residual momentum. This finding shifts the focus to behavioral mechanisms, which we examine next.

![Refer to caption](x10.png)


(a) Response to Earnings Surprise from -30 to -1



Figure 5: Pre-announcement behavior before earnings surprises



Notes: Figure [5](https://arxiv.org/html/2512.00280v1#S6.F5 "Figure 5 ‣ 6.1 Momentum ‣ 6 Discussion ‣ Retail Investor Horizon and Earnings Announcements") illustrates the mean buy-and-hold abnormal return reactions. From January 2010 until June 2021, stocks in CRSP are matched with quarterly earnings declarations in I/B/E/S. In the timeline of the event, the day of the announcement is designated as day 0. The buy-and-hold abnormal return for each stock is the raw buy-and-hold return adjusted based on the estimated beta from the market model. The earnings surprise for an announcement is defined as the difference between the actual earnings for the quarter, as recorded by I/B/E/S, and the median analyst forecast featured in the I/B/E/S detail file within the 30 days preceding the quarterly earnings announcement. This is then scaled by the stock price 5 trading days before the announcement. Earnings announcements are divided into 11 groups: Quintiles 1 to 5 consist of five quintiles of negative earnings surprises, while quintiles 7 to 11 comprise five quintiles of positive earnings surprises. Quintile 6 includes all announcements where the earnings surprise is zero. The breakpoints are determined quarterly.

### 6.2 Mechanism

To evaluate whether an optimism–bias channel drives the cross-sectional differences in post-announcement returns, we augment the regression with an indicator for above-median pre-announcement valence (computed over days [−90,−1][-90,-1]) and its interaction with the long-horizon indicator (Table [7](https://arxiv.org/html/2512.00280v1#S6.T7 "Table 7 ‣ 6.2 Mechanism ‣ 6 Discussion ‣ Retail Investor Horizon and Earnings Announcements")). Although our baseline specification already includes [−30,−1][-30,-1] sentiment and its dispersion, this design isolates whether broader pre-EA enthusiasm shapes the price response and whether that effect differs by investor horizon. Under an optimism-bias mechanism, elevated pre-EA sentiment should (i) dampen the day 0–1 reaction because prices are partially bid up beforehand, and (ii) predict more negative post-EA drift as expectations revert—effects that should be strongest for short-horizon stocks and attenuated for long-horizon stocks. We formalize these predictions in Section [3](https://arxiv.org/html/2512.00280v1#S3 "3 A Model of Earnings Announcement Reactions and Investor Horizons ‣ Retail Investor Horizon and Earnings Announcements").

Across all specifications, the valence indicator loads negatively and significantly. In the immediate window (Panel A), above-median sentiment is associated with −0.31-0.31 to −0.73-0.73 pp lower B​H​A​RBHAR, consistent with partial pre-announcement run-up. The effect is much larger in the drift window (Panel B): coefficients range from −1.89-1.89 to −4.90-4.90 pp (p<0.01p<0.01 in all but one case), indicating that high pre-EA enthusiasm is followed by substantially weaker performance over days 2–75. The pattern persists in the full 0–75 window (Panel C), where valence coefficients lie between −2.65-2.65 and −5.42-5.42 pp.

The long-term×\timesvalence interaction is uniformly positive and precisely estimated in the delayed- and total-response regressions, between +1.29+1.29 and +3.25+3.25 pp in Panel B and between +1.06+1.06 and +3.25+3.25 pp in Panel C. These magnitudes offset a sizable share of the negative valence effect, implying that long-horizon investor presence meaningfully dampens the reversal that follows elevated sentiment. In the day 0–1 window (Panel A), the interaction is smaller but still positive and significant in most specifications, offsetting 0.240.24–0.540.54 pp of the immediate overreaction.

High pre-EA sentiment reliably predicts subsequent giveback, especially in stocks followed predominantly by short-horizon investors, while long-horizon presence attenuates that reversal. The cross-sectional pattern fits an optimism-bias (over-extrapolation) mechanism rather than a pure risk-based or mechanical momentum explanation.

Table 7: Response to Earnings Surprise: Mechanism

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) |
| Panel A. Immediate Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 1 | | | | | | | |  |  |
| Long-Term | 0.0028∗∗∗ | 0.0001 | -0.0001 | 0.0015 | -0.0014 | -0.0032 | 0.0032∗∗∗ | 0.0008 | 0.0017 |
|  | (0.0007) | (0.0008) | (0.0012) | (0.0014) | (0.0015) | (0.0021) | (0.0009) | (0.0010) | (0.0015) |
| Valence | -0.0047∗∗∗ | -0.0036∗∗∗ | -0.0044∗∗∗ | -0.0057∗∗∗ | -0.0064∗∗∗ | -0.0073∗∗∗ | -0.0036∗∗∗ | -0.0031∗∗∗ | -0.0044∗∗ |
|  | (0.0008) | (0.0008) | (0.0013) | (0.0014) | (0.0015) | (0.0023) | (0.0009) | (0.0010) | (0.0018) |
| Long-Term ×\times Valence 0.0030∗∗∗ | 0.0034∗∗∗ | 0.0030∗∗ | 0.0039∗∗ | 0.0049∗∗∗ | 0.0054∗∗ | 0.0024∗ | 0.0034∗∗∗ | 0.0034∗ |  |
|  | (0.0010) | (0.0010) | (0.0014) | (0.0018) | (0.0019) | (0.0026) | (0.0012) | (0.0013) | (0.0020) |
| R2R^{2} | 0.0856 | 0.1524 | 0.2080 | 0.0090 | 0.2125 | 0.2910 | 0.0303 | 0.1465 | 0.2184 |
| Panel B. Delayed Reaction: Buy-and-Hold Abnormal Return in Event Time 2 to 75 | | | | | | | |  |  |
| Long-Term | 0.0062∗∗ | 0.0083∗∗∗ | 0.0100∗∗∗ | 0.0030 | 0.0082∗ | 0.0101 | 0.0079∗∗∗ | 0.0074∗∗ | 0.0102∗∗ |
|  | (0.0026) | (0.0025) | (0.0036) | (0.0041) | (0.0047) | (0.0068) | (0.0030) | (0.0033) | (0.0048) |
| Valence | -0.0444∗∗∗ | -0.0347∗∗∗ | -0.0275∗∗∗ | -0.0490∗∗∗ | -0.0284∗∗∗ | -0.0189∗∗ | -0.0419∗∗∗ | -0.0388∗∗∗ | -0.0336∗∗∗ |
|  | (0.0024) | (0.0024) | (0.0041) | (0.0046) | (0.0048) | (0.0075) | (0.0028) | (0.0030) | (0.0054) |
| Long-Term ×\times Valence | 0.0236∗∗∗ | 0.0187∗∗∗ | 0.0078∗ | 0.0293∗∗∗ | 0.0151∗∗ | 0.0039 | 0.0207∗∗∗ | 0.0219∗∗∗ | 0.0129∗∗ |
|  | (0.0032) | (0.0031) | (0.0047) | (0.0059) | (0.0060) | (0.0086) | (0.0038) | (0.0039) | (0.0061) |
| R2R^{2} | 0.0094 | 0.1558 | 0.1801 | 0.0086 | 0.2423 | 0.2917 | 0.0097 | 0.1762 | 0.2229 |
| Panel C. Total Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 75 | | | | | | | |  |  |
| Long-Term | 0.0097∗∗∗ | 0.0088∗∗∗ | 0.0104∗∗∗ | 0.0049 | 0.0062 | 0.0066 | 0.0120∗∗∗ | 0.0094∗∗∗ | 0.0129∗∗ |
|  | (0.0027) | (0.0027) | (0.0038) | (0.0043) | (0.0050) | (0.0074) | (0.0033) | (0.0035) | (0.0051) |
| Valence | -0.0490∗∗∗ | -0.0381∗∗∗ | -0.0318∗∗∗ | -0.0542∗∗∗ | -0.0345∗∗∗ | -0.0265∗∗∗ | -0.0454∗∗∗ | -0.0416∗∗∗ | -0.0376∗∗∗ |
|  | (0.0026) | (0.0025) | (0.0043) | (0.0047) | (0.0050) | (0.0080) | (0.0031) | (0.0031) | (0.0057) |
| Long-Term ×\times Valence | 0.0263∗∗∗ | 0.0221∗∗∗ | 0.0106∗∗ | 0.0325∗∗∗ | 0.0199∗∗∗ | 0.0095 | 0.0228∗∗∗ | 0.0250∗∗∗ | 0.0155∗∗ |
|  | (0.0034) | (0.0033) | (0.0049) | (0.0062) | (0.0063) | (0.0092) | (0.0041) | (0.0042) | (0.0065) |
| R2R^{2} | 0.0204 | 0.1626 | 0.1883 | 0.0095 | 0.2352 | 0.2908 | 0.0158 | 0.1804 | 0.2282 |
| Year-Quarter Fixed Effects |  | X | X |  | X | X |  | X | X |
| Firm Fixed Effects |  | X | X |  | X | X |  | X | X |
| Controls |  | X | X |  | X | X |  | X | X |
| Observations | 104,919 | 104,703 | 75,080 | 33,722 | 33,155 | 24,820 | 63,395 | 62,977 | 43,751 |

* •

  Notes: Table [7](https://arxiv.org/html/2512.00280v1#S6.T7 "Table 7 ‣ 6.2 Mechanism ‣ 6 Discussion ‣ Retail Investor Horizon and Earnings Announcements") reports the coefficients of a regression of the immediate response of securities to earning surprises defined by the following regression:

  |  |  |  |
  | --- | --- | --- |
  |  | BHARt,kw=α+β​𝕀t,k,Long-term=1+θ​𝕀t,k,Valence>=0.5+ϕ​(𝕀t,k,Long-term=1×𝕀t,k,Valence>=0.5)+∑j=211δj​𝕀t,k,Earnings Quantile=j+γk​Xt,k+λt+ηk+ϵt,k.\mathrm{BHAR}^{w}\_{t,k}=\alpha+\beta\,\mathbb{I}\_{t,k,\text{Long-term}=1}+\theta\,\mathbb{I}\_{t,k,\text{Valence}>=0.5}+\phi\,\Big(\mathbb{I}\_{t,k,\text{Long-term}=1}\times\mathbb{I}\_{t,k,\text{Valence}>=0.5}\Big)+\sum\_{j=2}^{11}\delta\_{j}\,\mathbb{I}\_{t,k,\text{Earnings Quantile}=j}+\gamma^{k}X\_{t,k}+\lambda\_{t}+\eta\_{k}+\epsilon\_{t,k}. |  |

  where B​H​A​Rt,kwBHAR^{w}\_{t,k} is defined as in Equation ([A4](https://arxiv.org/html/2512.00280v1#S4.Ex6 "In 4 Methodology ‣ Retail Investor Horizon and Earnings Announcements")). β\beta is the added response of the securities in the group followed by long-term investors; θ\theta is the added response to above-median pre-announcement sentiment (𝕀Valence=1\mathbb{I}\_{\text{Valence}}=1) for the baseline (short-horizon) group; and ϕ\phi is the additional differential response for the long-term group, that is, how the sentiment effect changes when 𝕀Long-term=1\mathbb{I}\_{\text{Long-term}}=1. δ\delta capture the relation between the earning surprise and the immediate response; Xt,kX\_{t,k} is a set of control variables which include the size of the security, the dispersion of analysts forecasts, the number of analysts, the buy-and-hold abnormal returns [-30, -1], valence and standard deviation of valence over [-30, -1], institutional ownership & turnover, volatility, and abnormal short interest. To address the concern that companies followed by long-term investors may also have unobservable features that differ from companies followed by short-term investors, we control for firm fixed effects in most regression specifications. Finally, we also include time fixed effects by year-quarter. The standard errors account for heteroskedasticity as well as correlation of errors across securities making an announcement on the same day by clustering observations by day of announcement and by firm. Table [7](https://arxiv.org/html/2512.00280v1#S6.T7 "Table 7 ‣ 6.2 Mechanism ‣ 6 Discussion ‣ Retail Investor Horizon and Earnings Announcements") reports β\beta, θ\theta and ϕ\phi. Columns (1), (4) and (7) have no controls or fixed effects; Columns (2), (5), and (8) have the full set of control as defined in Xi​tX\_{it} along with firm and time fixed effects; Columns (3), (6), and (9) carries out matching on the control variables, followed by a regression with matching weights and time and firm fixed effects. Columns (4-6) are focusing on negative surprises, while Columns (7-9) are focusing on positive surprises, with and without control. To mitigate the impact of outliers, the dependent variables are winsorized at the 1st and 99th percentiles. ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01.

### 6.3 Mood Around Announcements

We next examine how investor sentiment evolves around earnings announcements. Specifically, we track hourly sentiment (extracted via vamossy2023emtract) in the 24 hours before and after each release. To prevent firms with exceptionally heavy message traffic from dominating the series, we first average posts at the ticker–hour level and then take the cross-sectional mean.333Averaging at the ticker–hour level first prevents firms with very high post counts from dominating the sample. Figure [6](https://arxiv.org/html/2512.00280v1#S6.F6 "Figure 6 ‣ 6.4 Information Content ‣ 6 Discussion ‣ Retail Investor Horizon and Earnings Announcements") plots the resulting sentiment paths by news type: panel (a) negative, panel (b) neutral, and panel (c) positive.

Two patterns stand out. First, stocks followed predominantly by short-horizon investors display higher pre-announcement sentiment, consistent with the optimism-bias mechanism tested above. Second, sentiment for these stocks reacts more sharply to the news itself: it rises more after good news and falls more after bad news than sentiment for stocks followed by long-horizon investors. By contrast, long-horizon sentiment shows only muted movements and reverts quickly.

These mood dynamics mirror our return results. Short-horizon investors exhibit more volatile, expectation-driven swings in sentiment, while long-horizon investors maintain a steadier outlook anchored in fundamentals. The evidence underscores how horizon-specific expectations shape both the tone of investor discourse and the corresponding price response around earnings announcements.

### 6.4 Information Content

Finally, to understand the distinct information sets used by these groups, we examine posts made from day −90-90 to day −1-1 before each earnings announcement. Word clouds built from term frequencies provide a first look. Panel (a) of Figure [7](https://arxiv.org/html/2512.00280v1#S6.F7 "Figure 7 ‣ 6.4 Information Content ‣ 6 Discussion ‣ Retail Investor Horizon and Earnings Announcements") highlights words such as financial, earnings, EPS, rating, and report for the long-term group, pointing to a focus on fundamentals. Panel (b) for the short-term group features support, volume, break, target, and stop, language typical of technical trading.

We quantify these lexical differences using a BERT-based sentence transformer model (bert-base-nli-mean-tokens). From each group, we randomly draw 20,000 posts and split them into two subsets of 10,000 messages to compute pairwise cosine similarities. Panel (c) of Figure [7](https://arxiv.org/html/2512.00280v1#S6.F7 "Figure 7 ‣ 6.4 Information Content ‣ 6 Discussion ‣ Retail Investor Horizon and Earnings Announcements") plots the similarity distributions for within-group and between-group comparisons. Two-sample Kolmogorov–Smirnov tests reject equality of the distributions at the 1 percent level: within-group similarities are significantly higher than between-group similarities. Thus, messages by long-term investors are cohesive among themselves, as are those by short-term investors, but the two groups rely on noticeably different distinct vocabularies. This linguistic divergence supports our central claim that short-horizon investors operate on technical signals and sentiment, while long-horizon investors process fundamental information.

![Refer to caption](x11.png)


(a) Negative News

![Refer to caption](x12.png)


(b) No News

![Refer to caption](x13.png)


(c) Positive News

Figure 6: Mood Surrounding Earnings Announcements by Investor Horizon



Notes: Hourly average valence for stocks associated with short-term and long-term investors, 24 hours before and after earnings announcements.



![Refer to caption](x14.png)


(a) “Long-Term” Users: Word Frequencies

![Refer to caption](x15.png)


(b) “Short-Term” Users: Word Frequencies

![Refer to caption](x16.png)


(c) Post Similarities

Figure 7: Information Content by Investor Horizon



Notes: Panels (a) and (b) display word frequencies from posts authored by long-term versus short-term users. Panel (c) shows the distribution of post similarities, illustrating differences in user communication content.
The Two-Sample Kolgomorov-Smirnov statistics for testing whether the post similarity distributions are the same are: 0.0173 (Long vs. Short), 0.0096 (Long vs. Short-Long), 0.0246 (Short vs. Short-Long), 0.0140 (Long vs. Long-Short), and 0.0305 (Short vs. Long-Short). Each test rejects the null hypothesis with a pp-value << 0.01.

The results in this section provide a coherent behavioral explanation for the horizon-based return patterns we document. Pre-announcement returns do not differ meaningfully across groups, ruling out mechanical momentum. Instead, the cross-sectional evidence points to an optimism–bias mechanism: high pre-EA sentiment leads to weaker subsequent performance, and this reversal is materially attenuated in stocks followed by long-horizon investors. Consistent with this mechanism, short-horizon investors display more elevated and more reactive sentiment around announcements, and their discussions emphasize technical trading cues rather than fundamentals. Long-horizon investors, by contrast, communicate in a more fundamentals-oriented and semantically cohesive manner and exhibit steadier sentiment dynamics.

## 7 Conclusion

This paper investigates whether the investment horizon of retail investors relates to how stock prices incorporate earnings news. By leveraging self-reported holding periods from StockTwits to classify stocks as predominantly long- or short-horizon, we document a systematic link between investor composition, information processing, and return dynamics around earnings announcements.

Our findings reveal that investor horizon is a significant predictor of post-announcement returns. Relative to stocks dominated by short-horizon traders, those followed by long-horizon investors exhibit a significantly stronger immediate price reaction—particularly to positive news—and a larger, more persistent post-announcement drift. In our fully controlled specifications, long-horizon stocks earn an additional 0.21 percentage points over the first two days and a further 2.08 percentage points over the subsequent quarter. These results challenge the view that high-frequency retail activity necessarily improves price efficiency; instead, we find that short-horizon environments are associated with sluggish information incorporation and subsequent corrections.

We propose a behavioral explanation for these patterns rooted in optimism bias and information sets. Short-horizon investors exhibit elevated pre-announcement sentiment and communicate using technical trading vocabulary (e.g., break, target, volume), behaviors that correlate with pre-event run-ups and subsequent reversals. In contrast, long-horizon investors focus on fundamental concepts (e.g., EPS, financial, report) and display steadier sentiment dynamics, a pattern consistent with dampened mispricing associated with pre-announcement euphoria. The data rule out simple momentum or flow-based explanations, suggesting instead distinct differences in how these groups form expectations and process fundamental news.

The economic magnitude of these differentials is substantial. A simple, monthly rebalanced trading strategy that goes long long-horizon stocks and shorts short-horizon stocks within earnings-surprise bins generates statistically significant risk-adjusted alphas of approximately 30 to 40 basis points per month. The strategy exhibits a defensive profile, loading negatively on market risk while tilting toward value and profitability, yet the alpha remains unexplained by standard risk factors.

Our study is subject to the caveat that identifying investor horizons relies on observational data from a single social media platform, which may proxy for correlated firm characteristics such as attention or growth narratives. However, the robustness of our results to firm fixed effects and extensive controls suggests that the horizon channel is distinct. Ultimately, these findings highlight the heterogeneity within the retail sector: ”retail” is not a monolith, and the distinction between short-term speculation and long-term conviction is central to understanding the efficiency of asset prices.

## Appendix

## Appendix A Robustness Checks

### A.1 Three-, Four-, Five-Factor Models

We repeat the analysis of Table [4](https://arxiv.org/html/2512.00280v1#S5.T4 "Table 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") after redefining buy-and-hold abnormal returns with progressively richer risk adjustments: the Fama–French three-factor model (FamaFrench1993) in Table [8](https://arxiv.org/html/2512.00280v1#A1.T8 "Table 8 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements"), the Carhart four-factor model (Carhart1997) in Table [9](https://arxiv.org/html/2512.00280v1#A1.T9 "Table 9 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements"), and the Fama–French five-factor model (FamaFrench2015) in Table [10](https://arxiv.org/html/2512.00280v1#A1.T10 "Table 10 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements"). The results are little changed.

### A.2 Alternative Event Window

Table [11](https://arxiv.org/html/2512.00280v1#A1.T11 "Table 11 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") recalculates the post-announcement drift using two shorter horizons, [2,40][2,40] and [2,60][2,60] trading days. Point estimates and significance levels remain in line with the baseline [2,75][2,75] specification, confirming that our results are robust to the choice of event window.

### A.3 Matching Sensitivity

To assess the robustness of our results to matching choices, Table [12](https://arxiv.org/html/2512.00280v1#A1.T12 "Table 12 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") reports estimates using nearest-neighbor matching with varying numbers of neighbors (5 or 10) and calipers (0.001, 0.01, 0.1), as well as alternative estimators (IPW-ATT and AIPW). The main specification in other tables employs neighbor(1) with caliper(0.01).

Comparing the main winsorized specification in Column 3 of Table [13](https://arxiv.org/html/2512.00280v1#A1.T13 "Table 13 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") to the analogous sensitivity specification with neighbor(5), caliper(0.01) in Column 2 of Table [12](https://arxiv.org/html/2512.00280v1#A1.T12 "Table 12 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") shows that the long-term coefficient changes only slightly for the immediate reaction (0.0034 vs. 0.0032, around 6% lower) but is around 15% lower for the delayed (0.0314 vs. 0.0268) and total (0.0360 vs. 0.0305) reaction windows. While the point estimates are somewhat sensitive to matching parameters and outlier treatment, all effects remain positive, statistically significant, and similar in magnitude, leaving the qualitative conclusions unchanged.

### A.4 Winsorization

Tables [13](https://arxiv.org/html/2512.00280v1#A1.T13 "Table 13 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") removes the winsorization to the dependent variables, and repeats Table [4](https://arxiv.org/html/2512.00280v1#S5.T4 "Table 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements"). Coefficient magnitudes and significance levels remain virtually unchanged, confirming that our results are not driven by extreme observations.

Table 8: Response to Earnings Surprise: Three-Factor Model

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) |
| Panel A. Immediate Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 1 | | | | | | | |  |  |
| Long-Term | 0.0052∗∗∗ | 0.0021∗∗∗ | 0.0019∗∗ | 0.0045∗∗∗ | 0.0015 | -0.0000 | 0.0051∗∗∗ | 0.0027∗∗∗ | 0.0037∗∗∗ |
|  | (0.0005) | (0.0006) | (0.0009) | (0.0010) | (0.0012) | (0.0017) | (0.0006) | (0.0008) | (0.0011) |
| Constant | -0.0034∗∗∗ | 0.0109∗∗∗ | -0.0007 | -0.0299∗∗∗ | -0.0083∗∗ | -0.0261∗∗∗ | 0.0122∗∗∗ | 0.0182∗∗∗ | 0.0145∗∗∗ |
|  | (0.0004) | (0.0024) | (0.0005) | (0.0008) | (0.0042) | (0.0009) | (0.0005) | (0.0033) | (0.0006) |
| R2R^{2} | 0.0852 | 0.1525 | 0.2078 | 0.0086 | 0.2123 | 0.2920 | 0.0293 | 0.1471 | 0.2187 |
| Panel B. Delayed Reaction: Buy-and-Hold Abnormal Return in Event Time 2 to 75 | | | | | | | |  |  |
| Long-Term | 0.0242∗∗∗ | 0.0199∗∗∗ | 0.0160∗∗∗ | 0.0266∗∗∗ | 0.0180∗∗∗ | 0.0151∗∗∗ | 0.0219∗∗∗ | 0.0183∗∗∗ | 0.0185∗∗∗ |
|  | (0.0019) | (0.0021) | (0.0028) | (0.0032) | (0.0039) | (0.0052) | (0.0021) | (0.0025) | (0.0037) |
| Constant | -0.0445∗∗∗ | 0.0414∗∗∗ | -0.0355∗∗∗ | -0.0447∗∗∗ | 0.0496∗∗∗ | -0.0337∗∗∗ | -0.0446∗∗∗ | 0.0479∗∗∗ | -0.0380∗∗∗ |
|  | (0.0017) | (0.0070) | (0.0014) | (0.0028) | (0.0124) | (0.0026) | (0.0017) | (0.0096) | (0.0018) |
| R2R^{2} | 0.0032 | 0.1265 | 0.1530 | 0.0033 | 0.2153 | 0.2689 | 0.0027 | 0.1466 | 0.2010 |
| Panel C. Total Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 75 | | | | | | | |  |  |
| Long-Term | 0.0299∗∗∗ | 0.0225∗∗∗ | 0.0183∗∗∗ | 0.0312∗∗∗ | 0.0191∗∗∗ | 0.0148∗∗∗ | 0.0278∗∗∗ | 0.0219∗∗∗ | 0.0227∗∗∗ |
|  | (0.0020) | (0.0022) | (0.0030) | (0.0033) | (0.0041) | (0.0056) | (0.0023) | (0.0028) | (0.0039) |
| Constant | -0.0484∗∗∗ | 0.0529∗∗∗ | -0.0364∗∗∗ | -0.0757∗∗∗ | 0.0416∗∗∗ | -0.0602∗∗∗ | -0.0326∗∗∗ | 0.0660∗∗∗ | -0.0230∗∗∗ |
|  | (0.0018) | (0.0076) | (0.0015) | (0.0029) | (0.0132) | (0.0028) | (0.0019) | (0.0105) | (0.0019) |
| R2R^{2} | 0.0116 | 0.1339 | 0.1617 | 0.0043 | 0.2081 | 0.2685 | 0.0064 | 0.1531 | 0.2076 |
| Year-Quarter Fixed Effects |  | X | X |  | X | X |  | X | X |
| Firm Fixed Effects |  | X | X |  | X | X |  | X | X |
| Controls |  | X | X |  | X | X |  | X | X |
| Observations | 104,919 | 104,703 | 75,080 | 33,722 | 33,155 | 24,820 | 63,395 | 62,977 | 43,751 |

* •

  Notes: Table [8](https://arxiv.org/html/2512.00280v1#A1.T8 "Table 8 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") reports the coefficients of a regression of the immediate response of securities to earning surprises defined by the following regression:

  |  |  |  |
  | --- | --- | --- |
  |  | B​H​A​Rt,kw=α+β×𝕀t,k,Long-term=1+∑j=211[δj×𝕀t,k,Earnings Quantile=j]+γk×Xt,k+λt+ηk+ϵt,k,BHAR^{w}\_{t,k}=\alpha+\beta\times\mathbb{I}\_{t,k,\text{Long-term}=1}+\sum\_{j=2}^{11}\Big[\delta\_{j}\times\mathbb{I}\_{t,k,\text{Earnings Quantile}=j}\Big]+\gamma^{k}\times X\_{t,k}+\lambda\_{t}+\eta\_{k}+\epsilon\_{t,k}, |  |

  where B​H​A​Rt,kwBHAR^{w}\_{t,k} is defined as in Equation ([A4](https://arxiv.org/html/2512.00280v1#S4.Ex6 "In 4 Methodology ‣ Retail Investor Horizon and Earnings Announcements")). β\beta is the added response of the securities in the group followed by long-term investors; δ\delta capture the relation between the earning surprise and the immediate response; Xt,kX\_{t,k} is a set of control variables which include the size of the security, the dispersion of analysts forecasts, the number of analysts, the buy-and-hold abnormal returns [-30, -1], valence and standard deviation of valence over [-30, -1], institutional ownership & turnover, volatility, and abnormal short interest. To address the concern that companies followed by long-term investors may also have unobservable features that differ from companies followed by short-term investors, we control for firm fixed effects in most regression specifications. Finally, we also include time fixed effects by year-quarter. The standard errors account for heteroskedasticity as well as correlation of errors across securities making an announcement on the same day by clustering observations by day of announcement and by firm. Table [8](https://arxiv.org/html/2512.00280v1#A1.T8 "Table 8 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") reports α\alpha and β\beta. Columns (1), (4) and (7) have no controls or fixed effects; Columns (2), (5), and (8) have the full set of control as defined in Xt,kX\_{t,k} along with firm and time fixed effects; Columns (3), (6), and (9) carries out matching on the control variables, followed by a regression with matching weights and time and firm fixed effects. Columns (4-6) are focusing on negative surprises, while Columns (7-9) are focusing on positive surprises, with and without control. To mitigate the impact of outliers, the dependent variables are winsorized at the 1st and 99th percentiles. ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01.




Table 9: Response to Earnings Surprise: Four-Factor Model

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) |
| Panel A. Immediate Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 1 | | | | | | | |  |  |
| Long-Term | 0.0053∗∗∗ | 0.0021∗∗∗ | 0.0019∗∗ | 0.0046∗∗∗ | 0.0015 | -0.0000 | 0.0051∗∗∗ | 0.0028∗∗∗ | 0.0037∗∗∗ |
|  | (0.0005) | (0.0006) | (0.0009) | (0.0010) | (0.0012) | (0.0017) | (0.0006) | (0.0008) | (0.0012) |
| Constant | -0.0034∗∗∗ | 0.0114∗∗∗ | -0.0006 | -0.0298∗∗∗ | -0.0080∗ | -0.0259∗∗∗ | 0.0122∗∗∗ | 0.0185∗∗∗ | 0.0145∗∗∗ |
|  | (0.0004) | (0.0024) | (0.0005) | (0.0008) | (0.0042) | (0.0009) | (0.0005) | (0.0034) | (0.0006) |
| R2R^{2} | 0.0847 | 0.1521 | 0.2071 | 0.0087 | 0.2118 | 0.2915 | 0.0293 | 0.1473 | 0.2190 |
| Panel B. Delayed Reaction: Buy-and-Hold Abnormal Return in Event Time 2 to 75 | | | | | | | |  |  |
| Long-Term | 0.0231∗∗∗ | 0.0198∗∗∗ | 0.0158∗∗∗ | 0.0244∗∗∗ | 0.0179∗∗∗ | 0.0143∗∗∗ | 0.0214∗∗∗ | 0.0185∗∗∗ | 0.0186∗∗∗ |
|  | (0.0019) | (0.0021) | (0.0028) | (0.0032) | (0.0039) | (0.0052) | (0.0020) | (0.0026) | (0.0037) |
| Constant | -0.0429∗∗∗ | 0.0421∗∗∗ | -0.0344∗∗∗ | -0.0420∗∗∗ | 0.0489∗∗∗ | -0.0317∗∗∗ | -0.0434∗∗∗ | 0.0463∗∗∗ | -0.0373∗∗∗ |
|  | (0.0017) | (0.0071) | (0.0014) | (0.0029) | (0.0126) | (0.0026) | (0.0017) | (0.0099) | (0.0018) |
| R2R^{2} | 0.0029 | 0.1284 | 0.1545 | 0.0028 | 0.2186 | 0.2703 | 0.0025 | 0.1480 | 0.2027 |
| Panel C. Total Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 75 | | | | | | | |  |  |
| Long-Term | 0.0288∗∗∗ | 0.0223∗∗∗ | 0.0180∗∗∗ | 0.0290∗∗∗ | 0.0189∗∗∗ | 0.0138∗∗ | 0.0273∗∗∗ | 0.0223∗∗∗ | 0.0228∗∗∗ |
|  | (0.0020) | (0.0022) | (0.0030) | (0.0033) | (0.0041) | (0.0056) | (0.0022) | (0.0028) | (0.0040) |
| Constant | -0.0467∗∗∗ | 0.0542∗∗∗ | -0.0352∗∗∗ | -0.0729∗∗∗ | 0.0417∗∗∗ | -0.0580∗∗∗ | -0.0313∗∗∗ | 0.0647∗∗∗ | -0.0223∗∗∗ |
|  | (0.0018) | (0.0077) | (0.0015) | (0.0029) | (0.0134) | (0.0028) | (0.0020) | (0.0108) | (0.0019) |
| R2R^{2} | 0.0111 | 0.1354 | 0.1626 | 0.0036 | 0.2111 | 0.2701 | 0.0064 | 0.1542 | 0.2092 |
| Year-Quarter Fixed Effects |  | X | X |  | X | X |  | X | X |
| Firm Fixed Effects |  | X | X |  | X | X |  | X | X |
| Controls |  | X | X |  | X | X |  | X | X |
| Observations | 104,919 | 104,703 | 75,080 | 33,722 | 33,155 | 24,820 | 63,395 | 62,977 | 43,751 |

* •

  Notes: Table [9](https://arxiv.org/html/2512.00280v1#A1.T9 "Table 9 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") reports the coefficients of a regression of the immediate response of securities to earning surprises defined by the following regression:

  |  |  |  |
  | --- | --- | --- |
  |  | B​H​A​Rt,kw=α+β×𝕀t,k,Long-term=1+∑j=211[δj×𝕀t,k,Earnings Quantile=j]+γk×Xt,k+λt+ηk+ϵt,k,BHAR^{w}\_{t,k}=\alpha+\beta\times\mathbb{I}\_{t,k,\text{Long-term}=1}+\sum\_{j=2}^{11}\Big[\delta\_{j}\times\mathbb{I}\_{t,k,\text{Earnings Quantile}=j}\Big]+\gamma^{k}\times X\_{t,k}+\lambda\_{t}+\eta\_{k}+\epsilon\_{t,k}, |  |

  where B​H​A​Rt,kwBHAR^{w}\_{t,k} is defined as in Equation ([A4](https://arxiv.org/html/2512.00280v1#S4.Ex6 "In 4 Methodology ‣ Retail Investor Horizon and Earnings Announcements")). β\beta is the added response of the securities in the group followed by long-term investors; δ\delta capture the relation between the earning surprise and the immediate response; Xt,kX\_{t,k} is a set of control variables which include the size of the security, the dispersion of analysts forecasts, the number of analysts, the buy-and-hold abnormal returns [-30, -1], valence and standard deviation of valence over [-30, -1], institutional ownership & turnover, volatility, and abnormal short interest. To address the concern that companies followed by long-term investors may also have unobservable features that differ from companies followed by short-term investors, we control for firm fixed effects in most regression specifications. Finally, we also include time fixed effects by year-quarter. The standard errors account for heteroskedasticity as well as correlation of errors across securities making an announcement on the same day by clustering observations by day of announcement and by firm. Table [9](https://arxiv.org/html/2512.00280v1#A1.T9 "Table 9 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") reports α\alpha and β\beta. Columns (1), (4) and (7) have no controls or fixed effects; Columns (2), (5), and (8) have the full set of control as defined in Xt,kX\_{t,k} along with firm and time fixed effects; Columns (3), (6), and (9) carries out matching on the control variables, followed by a regression with matching weights and time and firm fixed effects. Columns (4-6) are focusing on negative surprises, while Columns (7-9) are focusing on positive surprises, with and without control. To mitigate the impact of outliers, the dependent variables are winsorized at the 1st and 99th percentiles. ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01.




Table 10: Response to Earnings Surprise: Five-Factor Model

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) |
| Panel A. Immediate Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 1 | | | | | | | |  |  |
| Long-Term | 0.0053∗∗∗ | 0.0022∗∗∗ | 0.0019∗∗ | 0.0047∗∗∗ | 0.0018 | 0.0004 | 0.0051∗∗∗ | 0.0027∗∗∗ | 0.0036∗∗∗ |
|  | (0.0005) | (0.0006) | (0.0009) | (0.0010) | (0.0012) | (0.0017) | (0.0006) | (0.0008) | (0.0011) |
| Constant | -0.0034∗∗∗ | 0.0106∗∗∗ | -0.0007 | -0.0300∗∗∗ | -0.0089∗∗ | -0.0264∗∗∗ | 0.0122∗∗∗ | 0.0178∗∗∗ | 0.0146∗∗∗ |
|  | (0.0004) | (0.0024) | (0.0005) | (0.0008) | (0.0042) | (0.0009) | (0.0005) | (0.0034) | (0.0006) |
| R2R^{2} | 0.0852 | 0.1522 | 0.2079 | 0.0089 | 0.2124 | 0.2925 | 0.0291 | 0.1464 | 0.2188 |
| Panel B. Delayed Reaction: Buy-and-Hold Abnormal Return in Event Time 2 to 75 | | | | | | | |  |  |
| Long-Term | 0.0243∗∗∗ | 0.0198∗∗∗ | 0.0158 | 0.0272∗∗∗ | 0.0177∗∗∗ | 0.0160∗∗∗ | 0.0217∗∗∗ | 0.0182∗∗∗ | 0.0182∗∗∗ |
|  | (0.0019) | (0.0021) | (.) | (0.0031) | (0.0040) | (0.0052) | (0.0021) | (0.0025) | (0.0037) |
| Constant | -0.0446∗∗∗ | 0.0374∗∗∗ | -0.0355 | -0.0457∗∗∗ | 0.0425∗∗∗ | -0.0349∗∗∗ | -0.0443∗∗∗ | 0.0431∗∗∗ | -0.0379∗∗∗ |
|  | (0.0016) | (0.0069) | (.) | (0.0028) | (0.0125) | (0.0026) | (0.0017) | (0.0098) | (0.0018) |
| R2R^{2} | 0.0031 | 0.1238 | 0.1522 | 0.0033 | 0.2119 | 0.2693 | 0.0026 | 0.1432 | 0.1993 |
| Panel C. Total Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 75 | | | | | | | |  |  |
| Long-Term | 0.0301∗∗∗ | 0.0223∗∗∗ | 0.0181∗∗∗ | 0.0318∗∗∗ | 0.0189∗∗∗ | 0.0157∗∗∗ | 0.0276∗∗∗ | 0.0218∗∗∗ | 0.0222∗∗∗ |
|  | (0.0020) | (0.0022) | (0.0030) | (0.0032) | (0.0042) | (0.0057) | (0.0023) | (0.0028) | (0.0040) |
| Constant | -0.0485∗∗∗ | 0.0488∗∗∗ | -0.0364∗∗∗ | -0.0767∗∗∗ | 0.0344∗∗∗ | -0.0615∗∗∗ | -0.0322∗∗∗ | 0.0608∗∗∗ | -0.0228∗∗∗ |
|  | (0.0017) | (0.0076) | (0.0015) | (0.0028) | (0.0133) | (0.0029) | (0.0019) | (0.0107) | (0.0019) |
| R2R^{2} | 0.0117 | 0.1316 | 0.1609 | 0.0045 | 0.2050 | 0.2691 | 0.0061 | 0.1503 | 0.2063 |
| Year-Quarter Fixed Effects |  | X | X |  | X | X |  | X | X |
| Firm Fixed Effects |  | X | X |  | X | X |  | X | X |
| Controls |  | X | X |  | X | X |  | X | X |
| Observations | 104,919 | 104,703 | 75,080 | 33,722 | 33,155 | 24,820 | 63,395 | 62,977 | 43,751 |

* •

  Notes: Table [10](https://arxiv.org/html/2512.00280v1#A1.T10 "Table 10 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") reports the coefficients of a regression of the immediate response of securities to earning surprises defined by the following regression:

  |  |  |  |
  | --- | --- | --- |
  |  | B​H​A​Rt,kw=α+β×𝕀t,k,Long-term=1+∑j=211[δj×𝕀t,k,Earnings Quantile=j]+γk×Xt,k+λt+ηk+ϵt,k,BHAR^{w}\_{t,k}=\alpha+\beta\times\mathbb{I}\_{t,k,\text{Long-term}=1}+\sum\_{j=2}^{11}\Big[\delta\_{j}\times\mathbb{I}\_{t,k,\text{Earnings Quantile}=j}\Big]+\gamma^{k}\times X\_{t,k}+\lambda\_{t}+\eta\_{k}+\epsilon\_{t,k}, |  |

  where B​H​A​Rt,kwBHAR^{w}\_{t,k} is defined as in Equation ([A4](https://arxiv.org/html/2512.00280v1#S4.Ex6 "In 4 Methodology ‣ Retail Investor Horizon and Earnings Announcements")). β\beta is the added response of the securities in the group followed by long-term investors; δ\delta capture the relation between the earning surprise and the immediate response; Xt,kX\_{t,k} is a set of control variables which include the size of the security, the dispersion of analysts forecasts, the number of analysts, the buy-and-hold abnormal returns [-30, -1], valence and standard deviation of valence over [-30, -1], institutional ownership & turnover, volatility, and abnormal short interest. To address the concern that companies followed by long-term investors may also have unobservable features that differ from companies followed by short-term investors, we control for firm fixed effects in most regression specifications. Finally, we also include time fixed effects by year-quarter. The standard errors account for heteroskedasticity as well as correlation of errors across securities making an announcement on the same day by clustering observations by day of announcement and by firm. Table [10](https://arxiv.org/html/2512.00280v1#A1.T10 "Table 10 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") reports α\alpha and β\beta. Columns (1), (4) and (7) have no controls or fixed effects; Columns (2), (5), and (8) have the full set of control as defined in Xt,kX\_{t,k} along with firm and time fixed effects; Columns (3), (6), and (9) carries out matching on the control variables, followed by a regression with matching weights and time and firm fixed effects. Columns (4-6) are focusing on negative surprises, while Columns (7-9) are focusing on positive surprises, with and without control. To mitigate the impact of outliers, the dependent variables are winsorized at the 1st and 99th percentiles. ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01.




Table 11: Response to Earnings Surprise: Alternative Event Windows

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) |
| Panel A. Delayed Reaction: Buy-and-Hold Abnormal Return in Event Time 2 to 40 | | | | | | | |  |  |
| Long-Term | 0.0120∗∗∗ | 0.0086∗∗∗ | 0.0074∗∗∗ | 0.0117∗∗∗ | 0.0097∗∗∗ | 0.0049 | 0.0123∗∗∗ | 0.0082∗∗∗ | 0.0067∗∗∗ |
|  | (0.0015) | (0.0013) | (0.0018) | (0.0022) | (0.0026) | (0.0033) | (0.0017) | (0.0016) | (0.0022) |
| Constant | -0.0173∗∗∗ | 0.0187∗∗∗ | -0.0127∗∗∗ | -0.0177∗∗∗ | 0.0266∗∗∗ | -0.0107∗∗∗ | -0.0171∗∗∗ | 0.0108 | -0.0106∗∗∗ |
|  | (0.0013) | (0.0050) | (0.0009) | (0.0020) | (0.0085) | (0.0017) | (0.0013) | (0.0072) | (0.0011) |
| R2R^{2} | 0.0028 | 0.1290 | 0.1728 | 0.0026 | 0.2080 | 0.2832 | 0.0030 | 0.1598 | 0.2221 |
| Panel B. Delayed Reaction: Buy-and-Hold Abnormal Return in Event Time 2 to 60 | | | | | | | |  |  |
| Long-Term | 0.0201∗∗∗ | 0.0146∗∗∗ | 0.0111∗∗∗ | 0.0197∗∗∗ | 0.0122∗∗∗ | 0.0062 | 0.0199∗∗∗ | 0.0150∗∗∗ | 0.0128∗∗∗ |
|  | (0.0019) | (0.0017) | (0.0023) | (0.0029) | (0.0033) | (0.0045) | (0.0021) | (0.0022) | (0.0030) |
| Constant | -0.0324∗∗∗ | 0.0327∗∗∗ | -0.0230∗∗∗ | -0.0337∗∗∗ | 0.0386∗∗∗ | -0.0202∗∗∗ | -0.0315∗∗∗ | 0.0266∗∗∗ | -0.0226∗∗∗ |
|  | (0.0018) | (0.0063) | (0.0012) | (0.0028) | (0.0106) | (0.0023) | (0.0018) | (0.0091) | (0.0015) |
| R2R^{2} | 0.0033 | 0.1471 | 0.1758 | 0.0029 | 0.2293 | 0.2892 | 0.0035 | 0.1731 | 0.2234 |
| Year-Quarter Fixed Effects |  | X | X |  | X | X |  | X | X |
| Firm Fixed Effects |  | X | X |  | X | X |  | X | X |
| Controls |  | X | X |  | X | X |  | X | X |
| Observations | 104,919 | 104,703 | 75,080 | 33,722 | 33,155 | 24,820 | 63,395 | 62,977 | 43,751 |

* •

  Notes: Table [11](https://arxiv.org/html/2512.00280v1#A1.T11 "Table 11 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") reports the coefficients of a regression of the immediate response of securities to earning surprises defined by the following regression:

  |  |  |  |
  | --- | --- | --- |
  |  | B​H​A​Rt,kw=α+β×𝕀t,k,Long-term=1+∑j=211[δj×𝕀t,k,Earnings Quantile=j]+γk×Xt,k+λt+ηk+ϵt,k,BHAR^{w}\_{t,k}=\alpha+\beta\times\mathbb{I}\_{t,k,\text{Long-term}=1}+\sum\_{j=2}^{11}\Big[\delta\_{j}\times\mathbb{I}\_{t,k,\text{Earnings Quantile}=j}\Big]+\gamma^{k}\times X\_{t,k}+\lambda\_{t}+\eta\_{k}+\epsilon\_{t,k}, |  |

  where B​H​A​Rt,kwBHAR^{w}\_{t,k} is defined as in Equation ([A4](https://arxiv.org/html/2512.00280v1#S4.Ex6 "In 4 Methodology ‣ Retail Investor Horizon and Earnings Announcements")). β\beta is the added response of the securities in the group followed by long-term investors; δ\delta capture the relation between the earning surprise and the immediate response; Xt,kX\_{t,k} is a set of control variables which include the size of the security, the dispersion of analysts forecasts, the number of analysts, the buy-and-hold abnormal returns [-30, -1], valence and standard deviation of valence over [-30, -1], institutional ownership & turnover, volatility, and abnormal short interest. To address the concern that companies followed by long-term investors may also have unobservable features that differ from companies followed by short-term investors, we control for firm fixed effects in most regression specifications. Finally, we also include time fixed effects by year-quarter. The standard errors account for heteroskedasticity as well as correlation of errors across securities making an announcement on the same day by clustering observations by day of announcement and by firm. Table [11](https://arxiv.org/html/2512.00280v1#A1.T11 "Table 11 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") reports α\alpha and β\beta. Columns (1), (4) and (7) have no controls or fixed effects; Columns (2), (5), and (8) have the full set of control as defined in Xt,kX\_{t,k} along with firm and time fixed effects; Columns (3), (6), and (9) carries out matching on the control variables, followed by a regression with matching weights and time and firm fixed effects. Columns (4-6) are focusing on negative surprises, while Columns (7-9) are focusing on positive surprises, with and without control. To mitigate the impact of outliers, the dependent variables are winsorized at the 1st and 99th percentiles. ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01.




Table 12: Response to Earnings Surprise: Sensitivity

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) |
| Panel A. Immediate Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 1 | | | | | | | |  |
| Long-Term | 0.0030∗∗∗ | 0.0030∗∗∗ | 0.0030∗∗∗ | 0.0030∗∗∗ | 0.0030∗∗∗ | 0.0030∗∗∗ | 0.0016∗∗ | 0.0026∗∗∗ |
|  | (0.0010) | (0.0010) | (0.0010) | (0.0009) | (0.0009) | (0.0009) | (0.0007) | (0.0007) |
|  | 0.0153∗∗∗ | 0.0153∗∗∗ | 0.0153∗∗∗ | 0.0153∗∗∗ | 0.0153∗∗∗ | 0.0153∗∗∗ | -0.0005 |  |
|  | (0.0005) | (0.0005) | (0.0005) | (0.0005) | (0.0005) | (0.0005) | (0.0004) |  |
| R2R^{2} | 0.1930 | 0.1928 | 0.1929 | 0.1868 | 0.1867 | 0.1867 | 0.1783 | 0.1839 |
| Panel B. Delayed Reaction: Buy-and-Hold Abnormal Return in Event Time 2 to 75 | | | | | | | |  |
| Long-Term | 0.0184∗∗∗ | 0.0184∗∗∗ | 0.0184∗∗∗ | 0.0186∗∗∗ | 0.0187∗∗∗ | 0.0187∗∗∗ | 0.0155∗∗∗ | 0.0245∗∗∗ |
|  | (0.0031) | (0.0031) | (0.0031) | (0.0030) | (0.0030) | (0.0030) | (0.0023) | (0.0021) |
| Constant | -0.0299∗∗∗ | -0.0299∗∗∗ | -0.0300∗∗∗ | -0.0305∗∗∗ | -0.0305∗∗∗ | -0.0306∗∗∗ | -0.0296∗∗∗ |  |
|  | (0.0016) | (0.0016) | (0.0016) | (0.0015) | (0.0015) | (0.0015) | (0.0012) |  |
| R2R^{2} | 0.1863 | 0.1862 | 0.1862 | 0.1804 | 0.1803 | 0.1804 | 0.1402 | 0.1726 |
| Panel C. Total Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 75 | | | | | | | |  |
| Long-Term | 0.0220∗∗∗ | 0.0220∗∗∗ | 0.0220∗∗∗ | 0.0223∗∗∗ | 0.0223∗∗∗ | 0.0224∗∗∗ | 0.0173∗∗∗ | 0.0273∗∗∗ |
|  | (0.0034) | (0.0034) | (0.0034) | (0.0034) | (0.0034) | (0.0034) | (0.0024) | (0.0023) |
| Constant | -0.0141∗∗∗ | -0.0142∗∗∗ | -0.0141∗∗∗ | -0.0147∗∗∗ | -0.0147∗∗∗ | -0.0148∗∗∗ | -0.0299∗∗∗ |  |
|  | (0.0017) | (0.0017) | (0.0017) | (0.0017) | (0.0017) | (0.0017) | (0.0013) |  |
| R2R^{2} | 0.1934 | 0.1932 | 0.1932 | 0.1874 | 0.1873 | 0.1873 | 0.1499 | 0.1769 |
| Method | NN=5,cal=.001 | NN=5,cal=0.01 | NN=5,cal=0.1 | NN=10,cal=.001 | NN=10,cal=0.01 | NN=10,cal=0.1 | IPW-ATT | AIPW |
| Year-Quarter Fixed Effects | X | X | X | X | X | X | X | X |
| Firm Fixed Effects | X | X | X | X | X | X | X | X |
| Observations | 56,179 | 56,194 | 56,196 | 59,737 | 59,752 | 59,754 | 104,703 | 52,895 |

* •

  Notes: Table [4](https://arxiv.org/html/2512.00280v1#S5.T4 "Table 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") reports the coefficients of a regression of the immediate response of securities to earning surprises defined by the following regression:

  |  |  |  |
  | --- | --- | --- |
  |  | B​H​A​Rt,kw=α+β×𝕀t,k,Long-term=1+∑j=211[δj×𝕀t,k,Earnings Quantile=j]+γk×Xt,k+λt+ηk+ϵt,k,BHAR^{w}\_{t,k}=\alpha+\beta\times\mathbb{I}\_{t,k,\text{Long-term}=1}+\sum\_{j=2}^{11}\Big[\delta\_{j}\times\mathbb{I}\_{t,k,\text{Earnings Quantile}=j}\Big]+\gamma^{k}\times X\_{t,k}+\lambda\_{t}+\eta\_{k}+\epsilon\_{t,k}, |  |

  where B​H​A​Rt,kwBHAR^{w}\_{t,k} is defined as in Equation ([A4](https://arxiv.org/html/2512.00280v1#S4.Ex6 "In 4 Methodology ‣ Retail Investor Horizon and Earnings Announcements")). β\beta is the added response of the securities in the group followed by long-term investors; δ\delta capture the relation between the earning surprise and the immediate response; Xt,kX\_{t,k} is a set of control variables which include the size of the security, the dispersion of analysts forecasts, the number of analysts, the buy-and-hold abnormal returns [-30, -1], valence and standard deviation of valence over [-30, -1], institutional ownership & turnover, volatility, and abnormal short interest. To address the concern that companies followed by long-term investors may also have unobservable features that differ from companies followed by short-term investors, we control for firm fixed effects in most regression specifications. Finally, we also include time fixed effects by year-quarter. The standard errors account for heteroskedasticity as well as correlation of errors across securities making an announcement on the same day by clustering observations by day of announcement and by firm. Table [4](https://arxiv.org/html/2512.00280v1#S5.T4 "Table 4 ‣ 5.5 Trading Strategy ‣ 5 Primary Findings ‣ Retail Investor Horizon and Earnings Announcements") reports α\alpha and β\beta. Columns (1)–(6) apply nearest-neighbor matching estimators with varying numbers of neighbors (5 or 10) and calipers (0.001, 0.01, or 0.1) to assess robustness to matching parameters. Column (7) uses an Inverse Probability Weighting estimator for the Average Treatment effect on the Treated (IPW-ATT), while Column (8) implements a manual Augmented Inverse Probability Weighting (AIPW) estimator combining outcome regression and inverse-probability weighting to improve efficiency and robustness. To mitigate the impact of outliers, the dependent variables are winsorized at the 1st and 99th percentiles. ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01.




Table 13: Response to Earnings Surprise: No Winsorization

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) |
| Panel A. Immediate Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 1 | | | | | | | |  |  |
| Long-Term | 0.0051∗∗∗ | 0.0018∗∗∗ | 0.0012 | 0.0046∗∗∗ | 0.0012 | -0.0007 | 0.0049∗∗∗ | 0.0028∗∗∗ | 0.0033∗∗∗ |
|  | (0.0006) | (0.0007) | (0.0010) | (0.0011) | (0.0014) | (0.0019) | (0.0007) | (0.0009) | (0.0012) |
| Constant | -0.0031∗∗∗ | 0.0122∗∗∗ | 0.0001 | -0.0308∗∗∗ | -0.0079∗ | -0.0258∗∗∗ | 0.0133∗∗∗ | 0.0177∗∗∗ | 0.0158∗∗∗ |
|  | (0.0005) | (0.0028) | (0.0006) | (0.0010) | (0.0046) | (0.0010) | (0.0006) | (0.0038) | (0.0006) |
| R2R^{2} | 0.0778 | 0.1467 | 0.2042 | 0.0083 | 0.2176 | 0.3933 | 0.0288 | 0.1480 | 0.2192 |
| Panel B. Delayed Reaction: Buy-and-Hold Abnormal Return in Event Time 2 to 75 | | | | | | | |  |  |
| Long-Term | 0.0295∗∗∗ | 0.0191∗∗∗ | 0.0148∗∗∗ | 0.0295∗∗∗ | 0.0170∗∗∗ | 0.0131∗∗ | 0.0290∗∗∗ | 0.0181∗∗∗ | 0.0205∗∗∗ |
|  | (0.0026) | (0.0032) | (0.0036) | (0.0042) | (0.0047) | (0.0060) | (0.0028) | (0.0043) | (0.0040) |
| Constant | -0.0396∗∗∗ | 0.0695∗∗∗ | -0.0267∗∗∗ | -0.0402∗∗∗ | 0.0920∗∗∗ | -0.0257∗∗∗ | -0.0388∗∗∗ | 0.0672∗∗∗ | -0.0279∗∗∗ |
|  | (0.0026) | (0.0096) | (0.0018) | (0.0042) | (0.0169) | (0.0030) | (0.0026) | (0.0175) | (0.0020) |
| R2R^{2} | 0.0035 | 0.1690 | 0.1980 | 0.0035 | 0.2359 | 0.2751 | 0.0034 | 0.2017 | 0.2308 |
| Panel C. Total Reaction: Buy-and-Hold Abnormal Return in Event Time 0 to 75 | | | | | | | |  |  |
| Long-Term | 0.0357∗∗∗ | 0.0215∗∗∗ | 0.0167∗∗∗ | 0.0353∗∗∗ | 0.0188∗∗∗ | 0.0131∗∗ | 0.0349∗∗∗ | 0.0214∗∗∗ | 0.0250∗∗∗ |
|  | (0.0027) | (0.0034) | (0.0039) | (0.0043) | (0.0049) | (0.0063) | (0.0031) | (0.0047) | (0.0043) |
| Constant | -0.0434∗∗∗ | 0.0820∗∗∗ | -0.0270∗∗∗ | -0.0729∗∗∗ | 0.0807∗∗∗ | -0.0528∗∗∗ | -0.0257∗∗∗ | 0.0879∗∗∗ | -0.0122∗∗∗ |
|  | (0.0027) | (0.0103) | (0.0020) | (0.0043) | (0.0178) | (0.0032) | (0.0027) | (0.0187) | (0.0021) |
| R2R^{2} | 0.0111 | 0.1777 | 0.2032 | 0.0033 | 0.2371 | 0.2795 | 0.0081 | 0.2083 | 0.2358 |
| Year-Quarter Fixed Effects |  | X | X |  | X | X |  | X | X |
| Firm Fixed Effects |  | X | X |  | X | X |  | X | X |
| Controls |  | X | X |  | X | X |  | X | X |
| Observations | 104,919 | 104,703 | 75,080 | 33,722 | 33,155 | 24,820 | 63,395 | 62,977 | 43,751 |

* •

  Notes: Table [13](https://arxiv.org/html/2512.00280v1#A1.T13 "Table 13 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") reports the coefficients of a regression of the immediate response of securities to earning surprises defined by the following regression:

  |  |  |  |
  | --- | --- | --- |
  |  | B​H​A​Rt,kw=α+β×𝕀t,k,Long-term=1+∑j=211[δj×𝕀t,k,Earnings Quantile=j]+γk×Xt,k+λt+ηk+ϵt,k,BHAR^{w}\_{t,k}=\alpha+\beta\times\mathbb{I}\_{t,k,\text{Long-term}=1}+\sum\_{j=2}^{11}\Big[\delta\_{j}\times\mathbb{I}\_{t,k,\text{Earnings Quantile}=j}\Big]+\gamma^{k}\times X\_{t,k}+\lambda\_{t}+\eta\_{k}+\epsilon\_{t,k}, |  |

  where B​H​A​Rt,kwBHAR^{w}\_{t,k} is defined as in Equation ([A4](https://arxiv.org/html/2512.00280v1#S4.Ex6 "In 4 Methodology ‣ Retail Investor Horizon and Earnings Announcements")). β\beta is the added response of the securities in the group followed by long-term investors; δ\delta capture the relation between the earning surprise and the immediate response; Xt,kX\_{t,k} is a set of control variables which include the size of the security, the dispersion of analysts forecasts, the number of analysts, the buy-and-hold abnormal returns [-30, -1], valence and standard deviation of valence over [-30, -1], institutional ownership & turnover, volatility, and abnormal short interest. To address the concern that companies followed by long-term investors may also have unobservable features that differ from companies followed by short-term investors, we control for firm fixed effects in most regression specifications. Finally, we also include time fixed effects by year-quarter. The standard errors account for heteroskedasticity as well as correlation of errors across securities making an announcement on the same day by clustering observations by day of announcement and by firm. Table [13](https://arxiv.org/html/2512.00280v1#A1.T13 "Table 13 ‣ A.4 Winsorization ‣ Appendix A Robustness Checks ‣ Retail Investor Horizon and Earnings Announcements") reports α\alpha and β\beta. Columns (1), (4) and (7) have no controls or fixed effects; Columns (2), (5), and (8) have the full set of control as defined in Xt,kX\_{t,k} along with firm and time fixed effects; Columns (3), (6), and (9) carries out matching on the control variables, followed by a regression with matching weights and time and firm fixed effects. Columns (4-6) are focusing on negative surprises, while Columns (7-9) are focusing on positive surprises, with and without control. ∗ p<0.10p<0.10, ∗∗ p<0.05p<0.05, ∗∗∗ p<0.01p<0.01.

## Appendix B Model Simulation

### Setup

We simulate a market with N=100,000N=100,000 investors, each linked to a unique stock to approximate aggregate behavior. Parameters:

* •

  Optimism Bias (bb): Reflects the optimism of short-term investors about earnings announcements, set to b=0.5b=0.5.
* •

  Risk Aversion (γ\gamma): Indicates the degree of risk aversion in investors’ utility functions, set to γ=2.0\gamma=2.0.
* •

  Fundamental Values (θ\theta) and Earnings Noise (η\eta): Drawn from N​(0,σθ2)N(0,\sigma\_{\theta}^{2}) with σθ=0.25\sigma\_{\theta}=0.25, and N​(0,ση2)N(0,\sigma\_{\eta}^{2}) with ση=0.5\sigma\_{\eta}=0.5.
* •

  Earnings Announcements (e=θ+ηe=\theta+\eta): Combining fundamental value and earnings noise. σe=σθ2+ση2≈0.559\sigma\_{e}=\sqrt{\sigma\_{\theta}^{2}+\sigma\_{\eta}^{2}}\approx 0.559: Standard deviation of earnings announcement.
* •

  Signals for short-term (zS=e+ϵSz\_{S}=e+\epsilon\_{S}) and long-term investors (zL=θ+ϵLz\_{L}=\theta+\epsilon\_{L}), where ϵS∼N​(0,σS2)\epsilon\_{S}\sim N(0,\sigma\_{S}^{2}) and ϵL∼N​(0,σL2)\epsilon\_{L}\sim N(0,\sigma\_{L}^{2}), with σS=1.0\sigma\_{S}=1.0 and σL=1.0\sigma\_{L}=1.0.

### Simulation Procedure

Algorithm 1  Model Simulation Algorithm

1: Data: Set parameters bb, γ\gamma, σθ\sigma\_{\theta}, ση\sigma\_{\eta}, σS\sigma\_{S}, and σL\sigma\_{L}.

2: Result: Abnormal returns for short-term and long-term investors.

3: Generate Random Variables: Simulate θ∼N​(0,σθ2)\theta\sim N(0,\sigma\_{\theta}^{2}) and η∼N​(0,ση2)\eta\sim N(0,\sigma\_{\eta}^{2}). Calculate e=θ+ηe=\theta+\eta. Generate signals zS=e+ϵSz\_{S}=e+\epsilon\_{S} and zL=θ+ϵLz\_{L}=\theta+\epsilon\_{L}, where ϵS∼N​(0,σS2)\epsilon\_{S}\sim N(0,\sigma\_{S}^{2}) and ϵL∼N​(0,σL2)\epsilon\_{L}\sim N(0,\sigma\_{L}^{2}).

4: Update Expectations Short-term investors: EeS=b+(σe2σe2+σS2)​(zS−b)E\_{e}^{S}=b+\left(\frac{\sigma\_{e}^{2}}{\sigma\_{e}^{2}+\sigma\_{S}^{2}}\right)(z\_{S}-b) Long-term investors: EθL=σθ2σθ2+σL2⋅zLE\_{\theta}^{L}=\frac{\sigma\_{\theta}^{2}}{\sigma\_{\theta}^{2}+\sigma\_{L}^{2}}\cdot z\_{L}

5: Calculate Initial Demand (Assume p1=0p\_{1}=0) Short-term demand: kS=EeSγ​σS2\displaystyle k\_{S}=\frac{E\_{e}^{S}}{\gamma\sigma\_{S}^{2}}. Long-term demand: kL=EθLγ​σL2\displaystyle k\_{L}=\frac{E\_{\theta}^{L}}{\gamma\sigma\_{L}^{2}}.

6: Update After Earnings Announcement (t=2t=2) Short-term investors update expectations: EθS=(σθ2σθ2+ση2)​eE\_{\theta}^{S}=\left(\frac{\sigma\_{\theta}^{2}}{\sigma\_{\theta}^{2}+\sigma\_{\eta}^{2}}\right)e Update short-term holdings: kSnew=EθS−eγ​σS2k\_{S}^{\text{new}}=\frac{E\_{\theta}^{S}-e}{\gamma\sigma\_{S}^{2}}

7: Calculate Abnormal Returns Short-term abnormal return: Abnormal ReturnS=p2−EeS=e−EeS\text{Abnormal Return}\_{S}=p\_{2}-E\_{e}^{S}=e-E\_{e}^{S}. Long-term abnormal return: Abnormal ReturnL=p2−p1=e\text{Abnormal Return}\_{L}=p\_{2}-p\_{1}=e.

## Appendix C Comparison of I/B/E/S-Only and Matched Samples

This appendix compares the full set of earnings announcements available in I/B/E/S with the subset matched to StockTwits horizon classifications. Table [14](https://arxiv.org/html/2512.00280v1#A3.T14 "Table 14 ‣ Appendix C Comparison of I/B/E/S-Only and Matched Samples ‣ Retail Investor Horizon and Earnings Announcements") reports differences in firm and announcement characteristics across the two samples. Although the matched sample is smaller, the two groups are similar along most observable dimensions. Differences in institutional ownership, analyst coverage, volatility, and year are statistically significant but economically modest. These comparisons indicate that the matched sample remains broadly representative of the I/B/E/S universe, mitigating concerns that our results are driven by selection into the StockTwits-linked subsample.

Table 14: Differences Between I/B/E/S-Only and Matched Sample

|  | Matched Sample | Original Sample |  | Norm. diff. | t-stat |
| --- | --- | --- | --- | --- | --- |
|  | (N = 104,919) | (N = 123,880) |  |  |  |
| Market Cap | 12,965.8 | 12,902.8 |  | 0.00 | 0.15 |
| Volatility | 0.0260 | 0.0250 |  | 0.01 | 2.53 |
| Turnover | 0.2330 | 0.2330 |  | 0.00 | 0.42 |
| Institutional Ownership | 0.7000 | 0.6880 |  | 0.04 | 10.40 |
| Past 3-Month Return | 0.0270 | 0.0280 |  | -0.00 | -1.17 |
| Abnormal Short Interest | 0.0000 | 0.0000 |  | 0.00 | 0.18 |
| Year | 2015.799 | 2015.460 |  | 0.10 | 25.00 |
| Earnings Surprise (SUE) | 0.0000 | 0.0000 |  | 0.00 | 0.82 |
| Number of Analysts | 8.958 | 8.494 |  | 0.07 | 15.84 |
| Forecast Dispersion | 0.0820 | 0.0800 |  | 0.01 | 1.30 |