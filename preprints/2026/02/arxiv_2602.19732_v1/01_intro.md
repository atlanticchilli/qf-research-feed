---
authors:
- Fabrizio Cipollini
- Giulia Cruciani
- Giampiero M. Gallo
- Alessandra Insana
- Edoardo Otranto
- Fabio Spagnolo
doc_id: arxiv:2602.19732v1
family_id: arxiv:2602.19732
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: VOLatility Archive for Realized Estimates (VOLARE)
url_abs: http://arxiv.org/abs/2602.19732v1
url_html: https://arxiv.org/html/2602.19732v1
venue: arXiv q-fin
version: 1
year: 2026
---


Fabrizio Cipollinia,
Giulia Crucianib,
Giampiero M. Galloc, e,
  
Alessandra Insanab,
Edoardo Otrantod, e,
Fabio Spagnolob

###### Abstract

VOLARE (VOLatility Archive for Realized Estimates – <https://volare.unime.it>) is an open research infrastructure providing standardized realized
volatility and covariance measures constructed from ultra-high-frequency financial data. The platform processes tick-level observations across equities, exchange rates, and futures using an asset-specific pipeline that addresses heterogeneous trading calendars, microstructure noise, and timestamp precision. For equities, price series are cleaned using a documented outlier detection procedure and sampled at regular intervals.

VOLARE delivers a comprehensive set of realized estimators, including realized variance, range-based measures, bipower variation, semivariances, realized quarticity, realized kernels, and multivariate covariance measures, ensuring methodological consistency and cross-asset comparability. In addition to bulk dataset download, the platform supports interactive
visualization and real-time estimation of established volatility models such as HAR and MEM specifications.

11footnotetext: DiSIA, University of Florence, Italy22footnotetext: Department of Economics, University of Messina, Italy33footnotetext: NYU in Florence44footnotetext: Department of Social and Economic Sciences, Sapienza University of Rome, Italy55footnotetext: CRENoS

Keywords: ultra high-frequency data; financial econometrics; open-access database; realized measures; MEM; HAR.

## 1 Introduction

Measuring and modelling market volatility is fundamental to financial econometrics, as it is essential for forecasting market movements, quantifying tail risks, and supporting portfolio allocation decisions. Understanding how volatility evolves over time and across assets provides essential insights into market dynamics, liquidity conditions, and systemic risk. Since the introduction of the Autoregressive Conditional Heteroskedasticity (ARCH) model by Engle ([1982](https://arxiv.org/html/2602.19732v1#bib.bib34 "Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation")) and its generalization (GARCH) by Bollerslev ([1986](https://arxiv.org/html/2602.19732v1#bib.bib20 "Generalized autoregressive conditional heteroskedasticity")), volatility modelling has been an essential component of empirical finance, forming the basis for derivative pricing, risk management, and financial stability analysis.

A major step forward in this field came with the development of realized volatility measures. Engle ([2000](https://arxiv.org/html/2602.19732v1#bib.bib71 "The econometrics of ultra-high-frequency data")), introduces the notion of *ultra* high-frequency data (UHFD) as recording detailed information about market activity across financial instruments.

Introduced by Andersen and Bollerslev ([1998](https://arxiv.org/html/2602.19732v1#bib.bib1 "Answering the skeptics: yes, standard volatility models do provide accurate forecasts")), realized variance computes the ex-post variation in prices as the sum of squared intraday returns. Compared with daily GARCH-type models-which infer latent conditional variance from squared daily returns, realized measures offer a more accurate and less noisy assessment of market variability. Moreover, realized volatility retains key empirical properties such as volatility clustering and long memory (Andersen et al., [2003](https://arxiv.org/html/2602.19732v1#bib.bib2 "Modeling and forecasting realized volatility")), while serving as a benchmark for evaluating the forecasting performance of econometric models.

Subsequent methodological advances have broadened the scope of realized measures, extending the original plain vanilla realized variance, allowing the incorporation of various features of the return series, such as microstructure noise, jump components, and asymmetries in price movements. In particular, the realized kernel (Barndorff-Nielsen et al., [2008](https://arxiv.org/html/2602.19732v1#bib.bib14 "Designing realized kernels to measure the ex post variation of equity prices in the presence of noise")) provides robust estimators under noisy conditions, while the realized semivariances (Barndorff‐Nielsen et al., [2010](https://arxiv.org/html/2602.19732v1#bib.bib16 "Measuring downside risk – realized semivariance")) capture asymmetric responses to positive and negative returns. These developments have made realized measures the foundation for modern volatility modelling and forecasting frameworks, including both univariate and multivariate settings.

UHFD are inherently complex: they comprise millions of tick-level observations per asset per year and require significant computational and methodological effort to clean, filter, and aggregate these data. Moreover, for many a researcher, the usage is hindered by the cost of access. Historically, the Realized Library of the Oxford-Man Institute (Heber et al., [2009](https://arxiv.org/html/2602.19732v1#bib.bib52 "Oxford-Man Institute’s realized library")) represented a valuable reference resource, offering various daily measures of realized volatility, along with open, high, low, and close prices related to several market indices from North American, European, and Asian exchanges. However, since its discontinuation in mid-2022, no open-access databases providing comparable data coverage or regular updates are available, despite their theoretical and practical importance. As a result, researchers and practitioners face significant barriers when attempting to replicate empirical findings, test new models, or conduct volatility forecasting exercises using realized data.

VOLARE (VOLatility Archive for Realized Estimates) aims at filling this gap by developing a comprehensive and openly accessible database of realized volatility and covariance measures derived from UHFD (source: <http://www.kibot.com>). Within VOLARE, we will refer to:

* •

  A library where we process tick-level observations for stocks, exchange rates and futures, applying rigorous filtering, aggregation, and outlier detection procedures to produce clean and accurate series. Here, we integrate advanced econometric methodologies – including the Brownlees and Gallo ([2006](https://arxiv.org/html/2602.19732v1#bib.bib25 "Financial econometric analysis at ultra-high frequency: data handling concerns")) outlier detection procedure and the Barndorff-Nielsen et al. ([2009](https://arxiv.org/html/2602.19732v1#bib.bib15 "Realized kernels in practice: trades and quotes")) realized kernel framework – ensuring methodological consistency and comparability across assets and time.
* •

  A research infrastructure where we estimate and compare a wide range of volatility models, such as the Heterogeneous Autoregressive (HAR) model (Corsi, [2009](https://arxiv.org/html/2602.19732v1#bib.bib32 "A simple approximate long-memory model of realized volatility")), its quarticity-augmented extension HAR-Q (Bollerslev et al., [2016](https://arxiv.org/html/2602.19732v1#bib.bib24 "Exploiting the errors: a simple approach for improved volatility forecasting")), and the Multiplicative Error Model (MEM) family (Engle, [2002](https://arxiv.org/html/2602.19732v1#bib.bib37 "New frontiers for ARCH models"); Engle and Gallo, [2006](https://arxiv.org/html/2602.19732v1#bib.bib38 "A multiple indicators model for volatility using intra-daily data")), including asymmetric specifications (AMEM). The platform enables consistent estimation, validation, and forecasting of volatility dynamics, similar to some of the features of the volatility analysis page in Engle’s V-Lab at NYU Stern (<https://vlab.stern.nyu.edu/volatility>).
* •

  A data visualization facility (platform) with an innovative user-oriented design. The platform integrates a back-end pipeline for large-scale data acquisition and cleaning with a web-based front-end for visualization, download, model estimation, and forecast dissemination. Users can access realized volatility and covariance time series, perform econometric modelling directly within the interface, and generate short- and medium-term forecasts, thereby bridging the gap between methodological research and applied financial analysis.

This paper provides a technical documentation and a justification for some of the choices made, both from the point of view of the econometric measures computed and of the architecture of data organization and back-end to front-end interaction.

The rest of this paper is structured as follows. [Section 2](https://arxiv.org/html/2602.19732v1#S2 "2 The Raw Data from Kibot ‣ VOLatility Archive for Realized Estimates (VOLARE)") describes the characteristics of the raw data used in the project, focusing on the Kibot database and the procedures adopted to assess data quality. [Section 3](https://arxiv.org/html/2602.19732v1#S3 "3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)") examines the impact of odd-lot trades on UHFD. [Section 4](https://arxiv.org/html/2602.19732v1#S4 "4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)") details the construction of the VOLARE library, covering the downloading, cleaning, and
aggregation procedures: that includes the outlier detection procedure and the conversion of unevenly spaced tick data into regularly sampled series. [Section 5](https://arxiv.org/html/2602.19732v1#S5 "5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)") presents the realized measures computed within VOLARE, encompassing both univariate series ([subsection 5.1](https://arxiv.org/html/2602.19732v1#S5.SS1 "5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)")) and multivariate covariance
measures ([subsection 5.2](https://arxiv.org/html/2602.19732v1#S5.SS2 "5.2 Multivariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)")). [Section 6](https://arxiv.org/html/2602.19732v1#S6 "6 The VOLARE Front-end: Architecture and User Experience ‣ VOLatility Archive for Realized Estimates (VOLARE)") illustrates the system integration between the back-end and the user interface. Overall, VOLARE makes advanced volatility analysis operational: its research infrastructure comprises a real-time capability of estimating, evaluating, and forecasting several popular univariate econometric models, discussed in detail in [Section 7](https://arxiv.org/html/2602.19732v1#S7 "7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"). Some concluding remarks synthesize the contribution and lie the ground for future developments. The final appendix provides the complete list of assets available on the VOLARE platform and presents an empirical application of the volatility models implemented therein.

## 2 The Raw Data from Kibot

The raw data used to construct VOLARE were obtained from Kibot, a provider offering data for stocks, ETFs, futures, exchange rates, indices, and OTC securities at various levels of
temporal aggregation: from end-of-day (EOD) series, to intraday minute bars, down to tick-level data. For transaction data, Kibot offers two tick formats: tickms, with millisecond-precision timestamps, and tick, with second-level timestamps; the former is the closest available approximation to the original Trades and Quotes (TAQ) data, which carry nanosecond-precision timestamps.111When comparing TAQ and tickms, despite the timestamp truncation from nanoseconds to milliseconds, the two datasets show nearly identical record counts. In contrast, tick excludes odd lots in addition to truncating timestamps to the second, resulting in substantially fewer records. For quotes data, Kibot analogously provides tickbidaskms with
millisecond timestamps and tickbidask with second-level timestamps.

Before estimating daily realized variance, we conducted an exploratory analysis of the Kibot data, with a particular focus on listed stocks at the tick level, available with millisecond precision since 2015. To assess data quality, we ran a preliminary side-by-side comparison with a small snapshot of intra-daily stock data available on the NYSE Trade and Quote database222TAQ, accessed through the Wharton Research Data Services – WRDS <https://www.wrds.wharton.upenn.edu>, revealing a strong match.

A further, more detailed comparison was conducted between daily prices and volumes (as they result from more granular Kibot data processing) and daily adjusted data from Yahoo Finance333<https://www.yahoo.com> and CRSP444Center for Research in Security Prices (CRSP), available within WRDS.. To that end, we focus on one year of Kibot tick data for Microsoft (MSFT), from 2023-01-03 to 2023-12-29. Transactions were first aggregated by timestamp to remove duplicates, ensuring that millisecond-level prices were consolidated before any further analysis. We then examined how different pre-processing choices, such as excluding trades after 16:00 (MSFT1600\text{MSFT}\_{1600}) or extending the trading window to 16:05555Brownlees and Gallo ([2006](https://arxiv.org/html/2602.19732v1#bib.bib25 "Financial econometric analysis at ultra-high frequency: data handling concerns")) had found that considering an extra five minutes - typically populated by trades with large volumes - could help capture the closing price, possibly recorded with a delay. (MSFT1605\text{MSFT}\_{1605}), affect daily price and volume measures. Daily prices were computed as the last available trade of each day (i.e., 16:00 or 16:05), while daily volumes were obtained by summing all intraday transactions.

### 2.1 Price Analysis

[Table 1](https://arxiv.org/html/2602.19732v1#S2.T1 "Table 1 ‣ 2.1 Price Analysis ‣ 2 The Raw Data from Kibot ‣ VOLatility Archive for Realized Estimates (VOLARE)") shows that the daily-aggregated tick-level series (MSFT1600 and MSFT1605) reveals that both aggregation schemes produce virtually identical price levels. The high-frequency series are fully coherent with the daily reference data from Yahoo Finance (MSFTY) and Kibot (MSFTK), showing no material discrepancies.

Examining the absolute percentage error666The absolute percentage error between x1x\_{1} and x2x\_{2} is computed as PE=|x1−x2x2|×100\text{PE}=\left|\frac{x\_{1}-x\_{2}}{x\_{2}}\right|\times 100. statistics ([Table 2](https://arxiv.org/html/2602.19732v1#S2.T2 "Table 2 ‣ 2.1 Price Analysis ‣ 2 The Raw Data from Kibot ‣ VOLatility Archive for Realized Estimates (VOLARE)")) and the corresponding box plots ([Figure 1](https://arxiv.org/html/2602.19732v1#S2.F1 "Figure 1 ‣ 2.1 Price Analysis ‣ 2 The Raw Data from Kibot ‣ VOLatility Archive for Realized Estimates (VOLARE)")), most deviations are extremely small, typically below 0.1% on average, with a few isolated outliers, further confirming the coherence of the price information across datasets and preprocessing choices.

| Price comparison | | | | |
| --- | --- | --- | --- | --- |
|  | High-Frequency (HF) | | Daily Reference (EOD) | |
|  | MSFT1600 | MSFT1605\text{MSFT}\_{1605} | MSFTY\text{MSFT}\_{Y} | MSFTK\text{MSFT}\_{K} |
| Count | 250 | 250 | 250 | 250 |
| Min | 219.10 | 219.10 | 219.16 | 219.10 |
| 25% | 279.75 | 280.07 | 279.68 | 279.74 |
| Median | 321.71 | 321.71 | 321.72 | 321.73 |
| 75% | 334.81 | 334.82 | 334.79 | 334.80 |
| Max | 380.62 | 380.57 | 380.62 | 380.62 |
| Mean | 311.04 | 311.16 | 311.03 | 311.04 |
| Std | 41.28 | 41.19 | 41.29 | 41.28 |

Table 1: Descriptive statistics for one year (2023-01-03 to 2023-12-29) daily MSFT prices across high-frequency aggregated series (MSFT1600, MSFT1605) and daily reference series (Yahoo Finance – MSFTY, Kibot – MSFTK).

| Price Absolute Percentage error | | | | |
| --- | --- | --- | --- | --- |
|  | Mean | Std | Min | Max |
| MSFT1600 vs MSFT1605\text{MSFT}\_{1605} | 0.12 | 0.52 | 0.00 | 5.03 |
| MSFT1600 vs MSFTY\text{MSFT}\_{Y} | 0.01 | 0.04 | 0.00 | 0.53 |
| MSFT1600 vs MSFTK\text{MSFT}\_{K} | 0.00 | 0.01 | 0.00 | 0.09 |
| MSFT1605\text{MSFT}\_{1605} vs MSFTY\text{MSFT}\_{Y} | 0.12 | 0.55 | 0.00 | 5.35 |
| MSFT1605\text{MSFT}\_{1605} vs MSFTK\text{MSFT}\_{K} | 0.12 | 0.54 | 0.00 | 5.30 |
| MSFTY\text{MSFT}\_{Y} vs MSFTK\text{MSFT}\_{K} | 0.02 | 0.04 | 0.00 | 0.53 |

Table 2: Absolute percentage errors analysis between high-frequency aggregated series (MSFT, MSFT1605\text{MSFT}\_{1605}) and daily price series (MSFTY\text{MSFT}\_{Y}, MSFTK\text{MSFT}\_{K}). One year of data (2023-01-03 to 2023-12-29).

![[Uncaptioned image]](x1.png)

Figure 1: Boxplot of absolute percentage errors across MSFT price series. One year of data (2023-01-03 to 2023-12-29).

### 2.2 Volume Analysis

In contrast to prices, trading volumes exhibit larger discrepancies across datasets.
High-frequency aggregated series (MSFT1600, MSFT1605), as well as daily aggregated Kibot volume (MSFTK), report systematically lower volumes than what is available in the daily references (MSFTY from Yahoo Finance, and MSFTC from CRSP): for individual trading days we show some examples in [Table 3](https://arxiv.org/html/2602.19732v1#S2.T3 "Table 3 ‣ 2.2 Volume Analysis ‣ 2 The Raw Data from Kibot ‣ VOLatility Archive for Realized Estimates (VOLARE)") and we present some descriptive statistics over the one year full sample (2023-01-03 to 2023-12-29) in [Table 4](https://arxiv.org/html/2602.19732v1#S2.T4 "Table 4 ‣ 2.2 Volume Analysis ‣ 2 The Raw Data from Kibot ‣ VOLatility Archive for Realized Estimates (VOLARE)").
To investigate whether extending the aggregation window can reconcile these differences, in the same table, we include also MSFTall, which aggregates tickms-level volumes over the entire 24-hour trading period, including both regular hours and overnight sessions.

According to the Kibot’s documentation, these issues in part arise because odd-lot transactions (i.e., trades smaller than 100 shares, or 1,000 for low-priced securities; see below for a more detailed discussion) are excluded from the tick-level dataset, whereas they have been included in official exchange-reported volumes since October 2013, when U.S. exchanges began reporting odd-lot trades to the Consolidated Tape777The SEC approved including odd-lot transactions in the Consolidated Tape in October 2013 (Securities Exchange Act Release No. 70794), and the amendment became operative on December 9, 2013. <https://www.sec.gov/files/rules/sro/nms/2013/34-70794.pdf>. As a result, Kibot’s end-of-day volumes tend to underestimate total trading activity.

Extending the aggregation window to 16:05 (MSFT1605) increases the recorded volume and brings it closer to the Yahoo and CRSP benchmarks, suggesting that a small fraction of after-close trades contributes meaningfully to total reported volume.
Further extending the aggregation to the full 24-hour period (MSFTall) yields volumes nearly identical to the daily reference datasets, confirming that overnight trading activity, while typically representing a small fraction of total volume, fully accounts for the remaining discrepancy between high-frequency aggregations and the benchmark figures.

Finally, [Table 5](https://arxiv.org/html/2602.19732v1#S2.T5 "Table 5 ‣ 2.2 Volume Analysis ‣ 2 The Raw Data from Kibot ‣ VOLatility Archive for Realized Estimates (VOLARE)") and [Figure 2](https://arxiv.org/html/2602.19732v1#S2.F2 "Figure 2 ‣ 2.2 Volume Analysis ‣ 2 The Raw Data from Kibot ‣ VOLatility Archive for Realized Estimates (VOLARE)") summarize percentage differences across series. Mean errors exceed 20% when comparing Kibot with Yahoo or CRSP, while discrepancies drop to around 4% for the extended 16:05 window and to 0% if we consider volume in the whole day period (MSFTall). These results show that minor timing and filtering differences, particularly related to odd-lot exclusion, can substantially affect volume-based analyses.

| Volume comparison | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
|  | High-Frequency (HF) | | | Daily Reference (EOD) | | |
| Date | MSFT1600 | MSFT1605 | MSFTall | MSFTY | MSFTC | MSFTK |
| 2023-01-03 | 21,118,749 | 25,547,937 | 25,740,036 | 25,740,000 | 25,723,760 | 20,138,969 |
| 2023-01-04 | 44,396,551 | 49,392,966 | 50,623,394 | 50,623,400 | 50,564,994 | 40,103,297 |
| 2023-01-05 | 34,614,037 | 39,007,843 | 39,585,623 | 39,585,600 | 39,541,865 | 32,111,249 |
| 2023-01-06 | 36,697,134 | 42,411,714 | 43,613,574 | 43,613,600 | 43,569,634 | 34,702,600 |
| 2023-01-09 | 22,138,100 | 26,330,882 | 27,369,784 | 27,369,800 | 27,334,038 | 20,896,326 |
| 2023-01-10 | 21,648,976 | 26,549,791 | 27,033,881 | 27,033,900 | 27,007,110 | 20,580,790 |
| 2023-01-11 | 22,458,390 | 27,854,506 | 28,669,331 | 28,669,300 | 28,626,526 | 21,781,322 |

Table 3: Example of daily trading volumes for selected days in January 2023 across high-frequency and daily reference MSFT datasets.



| Volume comparison | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
|  | High-Frequency (HF) | | | Daily Reference (EOD) | | |
|  | MSFT1600 | MSFT1605 | MSFTall | MSFTY | MSFTC | MSFTK |
| Count | 250 | 250 | 250 | 250 | 250 | 250 |
| Min | 9,220,482 | 9,220,792 | 10,176,649 | 10,176,600 | 10,114,326 | 6,808,578 |
| 25% | 16,283,579 | 20,133,018 | 21,196,236 | 21,186,475 | 21,164,668 | 15,049,934 |
| Median | 19,400,878 | 24,139,587 | 25,051,003 | 25,052,750 | 25,021,355 | 18,439,643 |
| 75% | 24,006,690 | 28,610,068 | 29,960,577 | 29,960,600 | 29,922,746 | 22,178,547 |
| Max | 62,270,435 | 67,060,589 | 78,502,324 | 78,478,200 | 77,755,324 | 55,725,298 |
| Mean | 21,791,418 | 26,389,321 | 27,680,595 | 27,675,559 | 27,616,578 | 20,358,245 |
| Std | 8,662,096 | 9,899,126 | 10,642,406 | 10,640,234 | 10,614,316 | 8,321,219 |

Table 4: Descriptive statistics for one year of data (2023-01-03 to 2023-12-29): MSFT daily trading volumes based on high-frequency aggregation (MSFT1600, MSFT1605, , MSFTall) and daily reference datasets (Yahoo Finance, CRSP, Kibot).

| Volume Percentage error | | | | |
| --- | --- | --- | --- | --- |
|  | Mean | Std | Min | Max |
| MSFT1600 vs MSFT1605 | 17.64 | 6.09 | 0.00 | 48.25 |
| MSFT1600 vs MSFTall | 21.18 | 7.26 | 2.79 | 57.34 |
| MSFT1600 vs MSFTY | 21.16 | 7.27 | 2.79 | 57.32 |
| MSFT1600 vs MSFTC | 20.99 | 7.27 | 2.69 | 56.93 |
| MSFT1600 vs MSFTK | 10.44 | 6.83 | 0.04 | 38.15 |
| MSFT1605 vs MSFTall | 4.37 | 4.01 | 0.10 | 22.25 |
| MSFT1605 vs MSFTY | 4.35 | 4.01 | 0.02 | 22.25 |
| MSFT1605 vs MSFTC | 4.15 | 4.03 | 0.04 | 22.05 |
| MSFT1605 vs MSFTK | 31.14 | 7.30 | 2.86 | 61.37 |
| MSFTall vs MSFTY | 0.02 | 0.06 | 0.00 | 0.58 |
| MSFTall vs MSFTC | 0.28 | 0.32 | 0.00 | 3.64 |
| MSFTall vs MSFTK | 37.32 | 8.69 | 20.84 | 76.40 |
| MSFTY vs MSFTC | 0.27 | 0.32 | 0.00 | 3.63 |
| MSFTY vs MSFTK | 37.30 | 8.69 | 20.84 | 76.40 |
| MSFTC vs MSFTK | 37.00 | 8.66 | 20.57 | 76.11 |

Table 5: Summary statistics of percentage differences in daily trading volumes across one year MSFT datasets. One year of data (2023-01-03 to 2023-12-29).

![[Uncaptioned image]](x2.png)

Figure 2: Boxplot of percentage errors across MSFT volume series. One year of data (2023-01-03 to 2023-12-29).

## 3 Some Insights on Odd-Lot Trades

Odd-lot transactions, defined as trades involving fewer than 100 shares (or fewer than 1,000 shares for low-priced securities), represent a distinct category of equity market activity. Historically, such trades were primarily associated with small investors and considered peripheral to price formation. However, in modern electronic markets, odd-lot activity has expanded dramatically and now accounts for a substantial fraction of total trades, particularly in high-frequency and algorithmic environments. (O’Hara et al., [2014](https://arxiv.org/html/2602.19732v1#bib.bib60 "What’s not there: odd lots and market data"))

The treatment of odd-lot transactions varies considerably across data providers. In the Kibot dataset, they are excluded from the tick and fixed-interval intraday data (e.g., minute bars), but they are included in the higher-frequency tickms raw data.

The academic investigation of odd-lot trading can be traced to early contributions such as Wu ([1972](https://arxiv.org/html/2602.19732v1#bib.bib67 "Odd-lot trading in the stock market and its market impact")) who provides one of the earliest systematic analyses, documenting the persistence of odd-lot activity in U.S. equity markets and its relationship with investor behavior and market microstructure. In the post-decimalization period, Johnson ([2014](https://arxiv.org/html/2602.19732v1#bib.bib54 "Odd lot trades: the behavior, characteristics, and information content, over time")) show that the informational role of odd-lot trades increased markedly, as small-volume transactions became more closely tied to informed trading and algorithmic execution. O’Hara et al. ([2014](https://arxiv.org/html/2602.19732v1#bib.bib60 "What’s not there: odd lots and market data")) demonstrate that excluding odd-lot trades from consolidated datasets such as TAQ can lead to systematic biases in measures of order imbalance, liquidity, and informational efficiency. More recently, Bartlett et al. ([2023](https://arxiv.org/html/2602.19732v1#bib.bib18 "The market inside the market: odd-lot quotes")) reveal that odd-lot quotes often constitute an ”inside market” offering better prices than the National Best Bid and Offer (NBBO), and therefore contribute materially to liquidity provision and price discovery.

As announced in October 2013, following U.S. Securities and Exchange Commission (SEC)
orders approving amendments to the UTP Plan and the CTA Plan,888See SEC Release
No.34–70793 (UTP Plan) and SEC Release No.34–70794 (CTA Plan), October 31, 2013, available at <https://www.sec.gov/files/rules/sro/nms/2013/34-70793.pdf> and
<https://www.sec.gov/files/rules/sro/nms/2013/34-70794.pdf>.
Nasdaq and NYSE have officially incorporated odd-lot volume into their reported daily trading statistics, effective December 9, 2013.
Nevertheless, exchange rules stipulate that odd-lot trades cannot determine the official last price and therefore do not directly influence the daily open, high, low, or close (OHLC) values. The persistence of odd-lot activity, combined with heterogeneous vendor practices, introduces potential discrepancies in empirical datasets and may significantly affect intraday analyses that rely on unfiltered trade-level data. (O’Hara et al., [2014](https://arxiv.org/html/2602.19732v1#bib.bib60 "What’s not there: odd lots and market data"))

|  | Yearly Trading Activity | | Odd Lots (Vol << 100) | |
| --- | --- | --- | --- | --- |
| Symbol | Observations | Volume | Obs (%) | Volume (%) |
| MSFT | 49,949,252 | 3,601,591,734 | 79.44 | 13.48 |
| JNJ | 13,859,636 | 1,230,836,830 | 71.93 | 11.54 |
| GE | 9,471,261 | 1,134,489,532 | 63.86 | 8.85 |
| MAT | 3,189,595 | 643,844,407 | 52.44 | 4.65 |
| LOCO | 543,523 | 56,608,498 | 69.14 | 9.61 |

Table 6: One year of high-frequency data from 2024-01-02 to 2024-12-31. Percentage of observations with a volume of less than 100 shares and their corresponding total volume percentage.

After aggregating tick-level data recorded at the same millisecond, in [Table 6](https://arxiv.org/html/2602.19732v1#S3.T6 "Table 6 ‣ 3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)") we report some summary statistics about the number
of high-frequency observations (and the corresponding overall volume) across one year (2024-01-02 to 2024-12-31) for five representative stocks. Interestingly, the majority of intraday trades are odd-lot transactions, accounting for 52-79% of the observations, depending on the stock. However, their contribution to total trading volume is substantially smaller (5-13%), highlighting a large discrepancy between transaction count and volume impact.

|  | Daily Trading Activity | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Observations | | | | | Volume | | | | |
| Symbol | Min | Q1 | Med | Q3 | Max | Min | Q1 | Med | Q3 | Max |
| MSFT | 79,340 | 167,946 | 186,966 | 215,314 | 515,694 | 6.0M | 11.0M | 13.1M | 16.0M | 40.9M |
| JNJ | 28,992 | 48,046 | 54,082 | 60,071 | 93,759 | 2.5M | 3.8M | 4.6M | 5.6M | 12.2M |
| GE | 17,506 | 30,034 | 34,804 | 41,146 | 111,160 | 1.8M | 3.0M | 4.0M | 5.1M | 17.6M |
| MAT | 6,069 | 10,155 | 12,164 | 13,846 | 74,792 | 666K | 1.6M | 2.1M | 2.8M | 33.7M |
| LOCO | 992 | 1,616 | 1,962 | 2,567 | 11,582 | 62K | 135K | 187K | 250K | 3.1M |
|  | Odd Lots (Vol << 100) | | | | | | | | | |
|  | Observations (%) | | | | | Volume (%) | | | | |
| Symbol | Min | Q1 | Med | Q3 | Max | Min | Q1 | Med | Q3 | Max |
| MSFT | 69.61 | 77.60 | 79.80 | 81.50 | 87.08 | 7.42 | 12.56 | 14.05 | 15.36 | 18.59 |
| JNJ | 59.36 | 69.56 | 72.40 | 75.01 | 82.00 | 6.90 | 10.32 | 11.98 | 13.48 | 20.82 |
| GE | 47.70 | 60.87 | 64.85 | 68.65 | 78.95 | 4.04 | 8.09 | 9.58 | 11.07 | 16.22 |
| MAT | 25.36 | 48.57 | 55.03 | 59.13 | 75.08 | 1.34 | 4.30 | 5.50 | 6.62 | 12.72 |
| LOCO | 39.33 | 62.17 | 70.55 | 76.88 | 88.77 | 2.20 | 8.28 | 10.44 | 14.29 | 28.15 |

Table 7: Daily distribution of trading activity over 252 trading days in 2024. Top panel: total observations and volume. Bottom panel: odd lots (volume << 100 shares) as percentage of total.

Daily statistics ([Table 7](https://arxiv.org/html/2602.19732v1#S3.T7 "Table 7 ‣ 3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)")) confirm that odd-lot prevalence is coherent across the sample period. For each stock, we compute the daily incidence of odd-lot trades and their volume contribution, then report their distribution. The median daily percentages show that odd-lots typically represent 55% (MAT) to 79% (MSFT) of all trades, while contributing only 5-14% of total volume. The narrow interquartile ranges indicate that these patterns are stable from day to day rather than driven by specific periods.

[Figures˜3](https://arxiv.org/html/2602.19732v1#S3.F3 "In 3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)") and [4](https://arxiv.org/html/2602.19732v1#S3.F4 "Figure 4 ‣ 3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)") display both the original and the adjusted (i.e., removing odd-lots) series for MSFT and JNJ, respectively. The four panels correspond to intervals with a different detail.

We then constructed two parallel datasets (original and adjusted) for each stock, regularly-sampled at multiple time intervals (1, 5, 10, 15, and 20 minutes), using the last available price within each interval as representative for that period. The percentage difference between the two series is computed as (Priceadjusted−Priceoriginal)/Priceoriginal×100{(\text{Price}\_{\text{adjusted}}-\text{Price}\_{\text{original}})}/{\text{Price}\_{\text{original}}}\times 100. The resulting box plots ([Figures˜6](https://arxiv.org/html/2602.19732v1#S3.F6 "In 3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)") and [5](https://arxiv.org/html/2602.19732v1#S3.F5 "Figure 5 ‣ 3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)")) illustrate the magnitude of the aggregation error attributable to the exclusion of odd-lot transactions.
The median error is generally close to zero, indicating that excluding odd-lot trades has a minimal impact on the aggregated prices for most stocks. However, larger discrepancies are more pronounced for less liquid securities and shorter intra-daily sampling intervals, demonstrating that odd-lot trades can occasionally generate significant deviations in what is taken as the intraday prices. Overall, these plots confirm that while excluding odd-lot transactions has limited effects on highly liquid equities, it should be carefully considered when analyzing low-liquidity stocks or constructing high-frequency time series.

![Refer to caption](x3.png)


Figure 3: Intraday price dynamics for MSFT, with and without odd-lot transactions (volume << 100), displayed for different time windows at various trading times on December 30, 2022.

![Refer to caption](x4.png)


Figure 4: Intraday price dynamics for JNJ, with and without odd-lot transactions (volume << 100), displayed for different time windows at various trading times on November 20, 2024.



![Refer to caption](VOLARE_figure/aggroddLots_error_1y_MSFT.png)

![Refer to caption](VOLARE_figure/aggroddLots_error_1y_JNJ.png)

![Refer to caption](VOLARE_figure/aggroddLots_error_1y_GE.png)

![Refer to caption](VOLARE_figure/aggroddLots_error_1y_MAT.png)

![Refer to caption](VOLARE_figure/aggroddLots_error_1y_LOCO.png)

Figure 5: Percentage difference between original and odd-lot-adjusted price series for MSFT, JNJ, GE, MAT and LOCO over the period 2024-01-02 to 2024-12-31. Both series were sampled at 1, 5, 10, 15, and 20-minute intervals using the last available price.



![Refer to caption](x5.png)

![Refer to caption](x6.png)

![Refer to caption](x7.png)

![Refer to caption](x8.png)

![Refer to caption](x9.png)

Figure 6: Percentage difference between original and odd-lot-adjusted price series for MSFT, JNJ, GE, MAT and LOCO on 2024-11-20. Both series were sampled at 1, 5, 10, 15, and 20-minute intervals using the last available price.

## 4 The VOLARE Back-end: Data Preparation

As mentioned before, the high-frequency financial datasets were sourced from Kibot, which provides data for a wide range of financial instruments; we focus on three major asset classes: stocks, exchange rates, and futures.These datasets are stored on a dedicated server, providing the necessary components for computing realized variance and covariance measures over the sample period of interest, as well as additional market variables such as open, high, low, and close prices, trading volume, and the number of trades. The complete list of securities included in the library is reported in [Tables˜A.1](https://arxiv.org/html/2602.19732v1#A1.T1 "In A.1 Asset list ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)"), [A.2](https://arxiv.org/html/2602.19732v1#A1.T2 "Table A.2 ‣ A.1 Asset list ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)") and [A.3](https://arxiv.org/html/2602.19732v1#A1.T3 "Table A.3 ‣ A.1 Asset list ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)") in [Appendix A](https://arxiv.org/html/2602.19732v1#A1 "Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)").

Each asset class presents distinct characteristics, mainly because of the market features (e.g., trading hours), but also for the format of the original data and the presence of outliers.
In what follows, we describe the specific feature of each asset class and the preprocessing procedures implemented to ensure the coherence and comparability.

### 4.1 Asset Classes

##### Stocks

The stock component of VOLARE is fed by unadjusted tickms. Regular trading hours for U.S. equities officially run from 9:30 to 16:00 Eastern Time (ET), but we extend data collection to 16:05 following Brownlees and Gallo ([2006](https://arxiv.org/html/2602.19732v1#bib.bib25 "Financial econometric analysis at ultra-high frequency: data handling concerns")), who found that including an additional five minutes beyond the official market close helps capture the closing price and associated trading volume, which are often recorded with a delay, as we show in our empirical analysis in [Section 2](https://arxiv.org/html/2602.19732v1#S2 "2 The Raw Data from Kibot ‣ VOLatility Archive for Realized Estimates (VOLARE)"). On certain pre-holiday sessions, such as the days preceding Christmas, Independence Day999In certain years, the U.S. stock market closes at 13:00 on July 3rd ahead of Independence Day (July 4th). However, when July 4th falls on a weekend (Saturday or Sunday), the holiday is observed on the previous Friday or the following Monday, respectively, and no early market closure occurs. Likewise, if July 4th falls on a Monday, that day is observed as a full holiday with no early closure on the preceding Friday., and the day following Thanksgiving, the market closes early at 13:00. For these sessions, any observation after 13:00 is treated as pertaining to overnight activity and is excluded from the intraday sample.
Before computing realized measures, the raw tick data undergo a cleaning procedure to identify and remove outliers. This operation follows the methodology of Brownlees and Gallo ([2006](https://arxiv.org/html/2602.19732v1#bib.bib25 "Financial econometric analysis at ultra-high frequency: data handling concerns")), which provides a robust framework for filtering anomalous price movements in high-frequency financial data (c.f [subsection 4.3](https://arxiv.org/html/2602.19732v1#S4.SS3 "4.3 Data Cleaning Procedure for High-Frequency Prices ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)") for details on the cleaning procedure).

##### Exchange Rates

The exchange rates dataset used in VOLARE is constructed from tickbidask. We deliberately refrain from using millisecond-level observations, as the timestamps provided by Kibot correspond to the moments when trades were received by their system, rather than the precise execution times. This asynchrony between trade execution and data ingestion could otherwise distort the fine-scale temporal structure of the series.

Due to the overlap of global trading centers across different time zones, exchange rate markets are, in principle, continuously active five days a week, from Sunday at 17:00 ET to Friday at 17:00 ET; however, we excluded periods of limited or irregular trading activity from the sample. In fact, weekend trading is sporadic and limited to a few currency pairs, resulting in incomplete and incoherent data coverage. Similarly, during major global holidays (e.g., Christmas, New Year’s Day), trading activity is markedly reduced or absent for several currency pairs.
To ensure temporal coherence and liquidity comparability, all periods with abnormally low activity are omitted.

Since tickbidask data is not based on transaction prices, no outlier-filtering procedure is applied. In fact, using mid-quote prices (the average of bid and ask) for subsequent processing naturally mitigates the impact of transient anomalies or recording errors, and the resulting series are sufficiently regular and robust without the need for additional cleaning.

##### Futures

The futures dataset is derived from tickbidask as well. Although millisecond timestamps are technically available, CME Group’s official documentation indicates that the “Trade Time” field uses the HHMMSS format without milliseconds. Consequently, millisecond-level data offer no additional precision compared to second-resolution data, and their use could create misleading assumptions about timing accuracy. For this reason, all futures contracts in the VOLARE dataset are based on timestamps at the one-second resolution.

Futures contracts are traded on various exchanges, including NYMEX, COMEX, and CME. These markets operate nearly continuously from Sunday at 18:00 ET to Friday at 17:00 ET, with a daily maintenance break from 17:00 to 18:00 ET. Trading hours and holiday schedules vary across contract types and exchanges. To ensure temporal consistency and comparability, periods with no trading activity, such as weekends and major global holidays, are excluded from the sample.

As with the exchange rates, the subsequent use of mid-quote prices reduces the impact of transient anomalies; therefore, no outlier-filtering procedure is applied.

A summary of some relevant aspects of the different asset classes is reported in [Table 8](https://arxiv.org/html/2602.19732v1#S4.T8 "Table 8 ‣ Futures ‣ 4.1 Asset Classes ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)").

| Asset Type | Starting Date | Frequency | Outlier Detection |
| --- | --- | --- | --- |
| Stocks | 2015-01-02 | tickms | yes |
| Exchange Rates | 2009-09-25 | tickbidask | no |
| Futures | 2009-09-28 | tickbidask | no |

Table 8: Summary of some relevant aspects by asset class: starting date, data frequency, and outlier detection procedure.

### 4.2 Download Raw Data

The raw high-frequency datasets used to build the VOLARE library are obtained via a custom download script interfacing with the Kibot API. The script accepts input parameters such as start and end dates, trading hours, and desired frequency (e.g., tickms for stocks and tickbidask for exchange rates and futures).

When multiple records within the same trading day share the same timestamp, the data are aggregated while preserving trade information by adding an additional column to the dataset. For stocks, aggregation computes the volume-weighted average price (VWAP), sums the total traded volume, and counts the number of trades101010For stocks, the trade count accurately reflects the number of individual trades. However, for exchange rates and futures, trade and volume-related fields provided by the data source do not correspond to actual executed transactions. In particular, foreign exchange markets are decentralized and do not provide transaction-level volume information; any such fields typically reflect quote updates rather than traded quantities. For this reason, volume and trade counts are not included in the final datasets for exchange rates and futures, although they are retained at the download stage for traceability.. For exchange rates and futures, aggregation is performed using the median of price-related variables, namely price, bid, and ask. In this context, the price variable does not play a distinctive role beyond bid and ask quotes and is included solely for coherence across asset classes. Volume and number of trades are excluded from the final datasets for these asset classes.
For each asset type, a dedicated folder is created; within it, each symbol has its own subfolder containing daily parquet files named according to the corresponding trading date. The organization of the raw data directories is illustrated in [Figure 7](https://arxiv.org/html/2602.19732v1#S4.F7 "Figure 7 ‣ 4.2 Download Raw Data ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)"). For stocks, each file contains at least Time, Price, Volume, and Trades; for exchange rates and futures, files include at least Time, Price, Bid, Ask, Volume, and Trades.

For housekeeping purposes, adjustment information (e.g., dividends or splits) is stored in an adjustments.txt file within each symbol folder and is updated incrementally upon download to preserve a complete record; to be clear, all realized measures computations are conducted using non-adjusted data. Additionally, a log file records metadata about the download process, allowing us to track any issues encountered.

The parquet format was chosen because it provides substantial storage savings compared to plain text files. For example, storing tick-level stock data in .parquet rather than .txt reduces storage requirements by over 60% ([Table 9](https://arxiv.org/html/2602.19732v1#S4.T9 "Table 9 ‣ 4.2 Download Raw Data ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)")) while preserving full data fidelity. In addition, parquet files, being columnar, allow efficient access to individual columns and faster analytical processing, which is particularly important when working with large high-frequency datasets.

|  |
| --- |
| /data/ |
| |-- stocks/ |
| |--|-- AAPL/ |
| |--|--|-- 2025\_03\_10.parquet |
| |--|--|-- 2025\_03\_11.parquet |
| |--|--|-- ... |
| |--|--|-- adjustments.txt |
| |--|-- MSFT/ |
| |--|-- TSLA/ |
| |-- exchange rates/ |
| |-- futures/ |

Figure 7: Structure of the raw data directory of the VOLARE library, organized by asset class and security.

| Storage | | |
| --- | --- | --- |
|  | .txt | .parquet |
| MSFT | 2.11 GB | 594.3 MB |
| JNJ | 575.2 MB | 181.2 MB |
| GE | 402.5 MB | 133.8 MB |
| XOM | 790.6 MB | 237.1 MB |
| KHC | 295 MB | 97.3 MB |
| Total | 4.17 GB | 1.24 GB |

Table 9: File size comparison of .txt and .parquet formats for one year of raw data.

### 4.3 Data Cleaning Procedure for High-Frequency Prices

Each trading day can generate millions of observations at uneven intervals, often influenced by noise from human input errors, system glitches, delayed reporting of block trades, or genuine market anomalies. These irregularities can lead to outliers that, if left unaddressed, may distort realized variance measures.

Effective cleaning requires balancing data preservation with correction: excessive filtering may remove small but informative price movements (“over-cleaning”), while insufficient cleaning may retain spurious observations that inflate noise (“under-cleaning”). This balance is particularly challenging without exchange-provided trade condition flags, as some sources like ours do not offer metadata to identify cancelled or out-of-sequence trades, making data-driven cleaning procedures essential.

Widely adopted methods were proposed by Brownlees and Gallo ([2006](https://arxiv.org/html/2602.19732v1#bib.bib25 "Financial econometric analysis at ultra-high frequency: data handling concerns")) and Barndorff-Nielsen et al. ([2009](https://arxiv.org/html/2602.19732v1#bib.bib15 "Realized kernels in practice: trades and quotes")). The Brownlees and Gallo ([2006](https://arxiv.org/html/2602.19732v1#bib.bib25 "Financial econometric analysis at ultra-high frequency: data handling concerns")) algorithm identifies anomalous observations based on their deviation from neighboring prices using a trimmed mean and standard deviation within a local time window. The Barndorff-Nielsen et al. ([2009](https://arxiv.org/html/2602.19732v1#bib.bib15 "Realized kernels in practice: trades and quotes")) method employs a rolling median filter, discarding prices deviating by more than ten mean absolute deviations (MAD) from a centered window of fifty observations. By using the median and MAD instead of the mean and standard deviation, this approach provides a non-parametric, highly robust filter that
minimizes the influence of extreme values.

The VOLARE library employs the robust, data-driven cleaning procedure on the UHF stock price data based on the Brownlees and Gallo ([2006](https://arxiv.org/html/2602.19732v1#bib.bib25 "Financial econometric analysis at ultra-high frequency: data handling concerns")) proposal.

The method relies on local information around each observation to identify and remove values that deviate excessively from their surrounding neighborhood. Specifically, a price observation pip\_{i} is flagged as an outlier when

|  |  |  |
| --- | --- | --- |
|  | |pi−p¯i​(k)|≥3​si​(k)+γ|p\_{i}-\bar{p}\_{i}(k)|\geq 3\,s\_{i}(k)+\gamma |  |

where p¯i​(k)\bar{p}\_{i}(k) denotes the δ\delta-trimmed mean and si​(k)s\_{i}(k) the corresponding trimmed standard deviation computed over a symmetric neighborhood of kk observations around ii. The parameter γ\gamma is a granularity constant that prevents false detections when prices remain constant for several ticks (e.g., during periods of low liquidity).

The procedure is applied as follows.

1. 1.

   Neighborhood definition. For each price pip\_{i}, a neighborhood Ni​(k)N\_{i}(k) of kk observations around ii is extracted, excluding the observation at index ii. Specifically:

   * •

     If i<k/2i<k/2, Ni​(k)N\_{i}(k) includes the first k+1k+1 prices of the series.
   * •

     If i≥n−k/2i\geq n-k/2, Ni​(k)N\_{i}(k) includes the last k+1k+1 prices.
   * •

     Otherwise, Ni​(k)N\_{i}(k) is symmetric around ii, from i−k/2i-k/2 to i+k/2+1i+k/2+1.
2. 2.

   Trimmed mean and standard deviation. The δ\delta-trimmed mean p¯i​(k)\overline{p}\_{i}(k) and standard deviation si​(k)s\_{i}(k) are computed on the observations belonging to Ni​(k)N\_{i}(k). The trim count (used to exclude the lowest and largest observations of Ni​(k)N\_{i}(k) from the mean and standard deviation calculation) is determined as the integer value of (length of​Ni​(k))×δ/2(\text{length of}N\_{i}(k))\times\delta/2 as ⌊(length of ​Ni​(k))×δ/2⌋\lfloor(\text{length of }N\_{i}(k))\times\delta/2\rfloor, where ⌊⋅⌋\lfloor\cdot\rfloor denotes the floor function.
3. 3.

   Outlier detection rule. pip\_{i} is flagged as an outlier if it deviates from p¯i​(k)\overline{p}\_{i}(k) by more than 3​si​(k)+γ3\,s\_{i}(k)+\gamma. All detected outliers are recorded, and a cleaned series is obtained by marking these values.
4. 4.

   Outlier treatment. Prior to the outlier detection procedure, a new column is added to the original dataframe to store a flag for each observation. This column captures the status of each price as follows:

   * •

     Prices outside regular trading hours are assigned a value of 0.
   * •

     Observations identified as outliers are set to NaN.
   * •

     Valid prices are set to 1.

   During subsequent preprocessing for the computation of realized variance and covariance, each outlier is replaced by the mean of the two preceding and two following valid prices.

The parameters of the Brownlees and Gallo ([2006](https://arxiv.org/html/2602.19732v1#bib.bib25 "Financial econometric analysis at ultra-high frequency: data handling concerns")) procedure are kk (neighborhood size), δ\delta (trimming proportion), and γ\gamma (granularity threshold):
kk controls local smoothness, with small windows being more sensitive to short-term fluctuations;
δ\delta regulates the proportion of extreme values trimmed from each neighborhood;
γ\gamma, which turns out to be the most influential, determines the size of the filtering window, with higher values resulting in fewer observations removed.

To illustrate the effect of the procedure, we applied it to five representative stocks: Microsoft (MSFT), Johnson & Johnson (JNJ), General Electric (GE), Mattel (MAT), and El Pollo Loco (LOCO), using the fixed configuration k=60k=60, δ=0.1\delta=0.1, and γ=0.06\gamma=0.06. The number of detected outliers for these assets is reported in [Table 10](https://arxiv.org/html/2602.19732v1#S4.T10 "Table 10 ‣ 4.3 Data Cleaning Procedure for High-Frequency Prices ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)"), while [Figures 8](https://arxiv.org/html/2602.19732v1#S4.F8 "In 4.3 Data Cleaning Procedure for High-Frequency Prices ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)") to [12](https://arxiv.org/html/2602.19732v1#S4.F12 "Figure 12 ‣ 4.3 Data Cleaning Procedure for High-Frequency Prices ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)") visually compare the original and cleaned price series, showing how the filter effectively removes spurious spikes while preserving genuine market dynamics.

| Symbol | Mkt. Cap. (USD) | Date | N. Obs. | N. Outliers |
| --- | --- | --- | --- | --- |
| MSFT | 3.07 T | 2022-12-30 | 140,653 | 434 |
| JNJ | 374.38 B | 2024-11-20 | 46,069 | 191 |
| GE | 193.40 B | 2024-11-20 | 29,269 | 181 |
| MAT | 6,18 B | 2024-11-20 | 13,823 | 20 |
| LOCO | 0.36 B | 2024-11-05 | 3,400 | 1 |

Table 10: Number of detected outliers for stocks of different market capitalizations, analyzed considering k=60k=60, δ=0.1\delta=0.1, and γ=0.06\gamma=0.06.

On the same stocks and trading days, we conducted a sensitivity analysis by varying kk (i.e., 60 and 80) and γ\gamma over a range of values to examine how the number of identified outliers changes under different parameter settings ([Figure 13](https://arxiv.org/html/2602.19732v1#S4.F13 "Figure 13 ‣ 4.3 Data Cleaning Procedure for High-Frequency Prices ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)")). The results show that the parameter γ\gamma predominantly controls the aggressiveness of the filter, as reflected by the substantial variation in the number of detected outliers, while changes in kk have a comparatively limited impact on the overall removal rate.

Based on these findings, we applied across all stocks of the VOLARE library the parameter configuration k=60k=60, δ=0.1\delta=0.1, and γ=0.06\gamma=0.06. The overall impact of the outlier detection on the complete dataset (2015-01-02 to 2026-01-30) is summarized in [Table 11](https://arxiv.org/html/2602.19732v1#S4.T11 "Table 11 ‣ 4.3 Data Cleaning Procedure for High-Frequency Prices ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)").
The procedure removes a modest proportion of observations while improving the quality and reliability of the high-frequency price series used for realized variance calculations.

![Refer to caption](x10.png)


Figure 8: Original and cleaned daily price series for MSFT on December 30, 2022, with zoomed-in views of selected sub-periods to highlight the impact of outliers.

![Refer to caption](x11.png)


Figure 9: Original and cleaned daily price series for JNJ on November 20, 2024, with zoomed-in views of selected sub-periods to highlight the impact of outliers.

![Refer to caption](x12.png)


Figure 10: Original and cleaned daily price series for GE on November 20, 2024, with zoomed-in views of selected sub-periods to highlight the impact of outliers.

![Refer to caption](x13.png)


Figure 11: Original and cleaned daily price series for MAT on November 20, 2024, with zoomed-in views of selected sub-periods to highlight the impact of outliers.

![Refer to caption](x14.png)


Figure 12: Original and cleaned daily price series for LOCO on November 05, 2024, with zoomed-in views of selected sub-periods to highlight the impact of outliers.

![Refer to caption](VOLARE_figure/BG_sensitivity_gamma.png)


Figure 13: Number of outliers detected for different stocks as a function of the parameter γ\gamma, for two values of kk (60 and 80). The plot highlights how the number of outliers decreases as γ\gamma increases, and compares stocks with different levels of market capitalization.



| Outlier Detection | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Symbol | Days | Avg | Avg (%) | Min | Max | Median |
| AAPL | 2786 | 698.03 | 0.24 | 0 | 14247 | 289.5 |
| ADBE | 2786 | 126.38 | 0.29 | 0 | 2020 | 49 |
| AMD | 2786 | 440.89 | 0.18 | 0 | 10178 | 97 |
| AMGN | 2786 | 53.75 | 0.21 | 0 | 1197 | 24 |
| AMZN | 2786 | 791.85 | 0.48 | 4 | 10975 | 370 |
| AXP | 2786 | 60.50 | 0.18 | 0 | 1283 | 16 |
| BA | 2786 | 134.53 | 0.22 | 0 | 2575 | 52 |
| CAT | 2786 | 75.83 | 0.23 | 0 | 1674 | 26 |
| CRM | 2786 | 158.45 | 0.26 | 0 | 3416 | 49 |
| CSCO | 2786 | 39.41 | 0.06 | 0 | 1915 | 16 |
| CVX | 2786 | 113.18 | 0.18 | 0 | 2925 | 41 |
| DIS | 2786 | 110.61 | 0.16 | 0 | 2574 | 54 |
| GE | 2786 | 78.80 | 0.17 | 0 | 2692 | 15 |
| GOOGL | 2786 | 525.10 | 0.49 | 3 | 11254 | 165.5 |
| GS | 2786 | 83.43 | 0.25 | 0 | 1876 | 25 |
| HD | 2786 | 112.86 | 0.27 | 0 | 2460 | 50 |
| HON | 2786 | 41.84 | 0.15 | 0 | 1221 | 16 |
| IBM | 2786 | 74.83 | 0.18 | 0 | 2316 | 11 |
| JNJ | 2786 | 100.86 | 0.17 | 0 | 1835 | 43 |
| JPM | 2786 | 162.75 | 0.21 | 0 | 3247 | 56 |
| KO | 2786 | 37.34 | 0.05 | 0 | 1459 | 13 |
| MCD | 2786 | 75.50 | 0.21 | 0 | 1715 | 29 |
| META | 2786 | 545.47 | 0.33 | 0 | 17873 | 146.5 |
| MMM | 2786 | 44.46 | 0.15 | 0 | 1187 | 18 |
| MRK | 2786 | 71.21 | 0.13 | 0 | 1940 | 24 |
| MSFT | 2786 | 645.50 | 0.31 | 0 | 15051 | 239 |
| NFLX | 2786 | 271.17 | 0.34 | 0 | 8358 | 104.5 |
| NKE | 2786 | 82.81 | 0.14 | 0 | 2826 | 33 |
| NVDA | 2786 | 1023.77 | 0.21 | 0 | 18109 | 157 |
| ORCL | 2786 | 220.48 | 0.20 | 0 | 9097 | 15 |
| PG | 2786 | 80.65 | 0.16 | 0 | 1705 | 32 |
| PM | 2786 | 39.86 | 0.12 | 0 | 1469 | 10 |
| SHW | 2786 | 37.43 | 0.29 | 0 | 676 | 16 |
| TRV | 2786 | 16.92 | 0.11 | 0 | 370 | 5 |
| TSLA | 2786 | 1053.67 | 0.24 | 0 | 38548 | 311 |
| UNH | 2786 | 186.01 | 0.29 | 0 | 8559 | 43 |
| V | 2786 | 153.02 | 0.25 | 0 | 3329 | 57 |
| VZ | 2786 | 26.63 | 0.04 | 0 | 1094 | 14 |
| WMT | 2786 | 107.12 | 0.14 | 0 | 3310 | 32 |
| XOM | 2786 | 111.00 | 0.14 | 0 | 2727 | 36.5 |

Table 11: Daily outlier detection summary by symbol (2015-01-02 to 2026-01-30). The table reports the daily average number of outliers and the average daily percentage of records identified as outliers during regular trading hours. Day-to-day variability is captured via minimum, maximum, median, and standard deviation. Outliers are detected using the Brownlees and Gallo ([2006](https://arxiv.org/html/2602.19732v1#bib.bib25 "Financial econometric analysis at ultra-high frequency: data handling concerns")) procedure with k=60k=60, δ=0.1\delta=0.1, γ=0.06\gamma=0.06.

### 4.4 From Tick Data to Regular Intervals

To address the challenge of the unevenly spaced time of financial tick data, it is necessary to transform the series into a regular interval series. This facilitates analysis and helps in reducing the impact of market microstructure noise (Gençay et al., [2001](https://arxiv.org/html/2602.19732v1#bib.bib43 "An introduction to high-frequency finance"); Hansen and Lunde, [2006](https://arxiv.org/html/2602.19732v1#bib.bib49 "Realized variance and market microstructure noise"); Bandi and Russell, [2008](https://arxiv.org/html/2602.19732v1#bib.bib8 "Microstructure noise, realized variance, and optimal sampling")).
In the VOLARE library we consider a clock-based sampling approach, which organizes price data into fixed time intervals, such as one-minute or five-minute windows. Among various approaches proposed in the literature, we adopt the previous-tick approach, which selects the last observed price before or at the end of each fixed-time interval. If no price is recorded within a given interval, the price from the previous interval is carried forward.(Barndorff-Nielsen et al., [2009](https://arxiv.org/html/2602.19732v1#bib.bib15 "Realized kernels in practice: trades and quotes")). The resulting series spans from 9:30:00.000 (the first recorded price after the market opens) to 16:05:00.000 (by convention the last price), with a recorded price for each fixed-time interval. Each interval is labeled using the right endpoint, ensuring that the upper boundary of the interval is included in the aggregation.

## 5 The VOLARE Back-end: Realized Measures

### 5.1 Univariate Series

The VOLARE library provides several indicators of market activity, such as well-established realized variance measures, widely popular in high-frequency financial econometrics, and realized quarticity ([Table 12](https://arxiv.org/html/2602.19732v1#S5.T12 "Table 12 ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)")). In addition to these, the dataset provides the ticker symbol, date, high price (HH), low price (LL), open price (OO), close price (CC)111111We select HH and LL values from all tick data of the day, including odd lots. For OO and CC prices, we use the first and last available prices of the day’s series, excluding odd lots., and, for stocks, total number of trades (NN), and traded volume (VOL).

All realized measures are computed using returns on equally-spaced intervals, typically at 1-minute or 5-minute frequencies. For the realized kernel, we use returns sampled every second, as this estimator is designed to effectively mitigate market microstructure noise.
Together, these estimators capture different dimensions of intraday return variability, such as overall variation, jump components, and asymmetric features of high-frequency data.

| Measure | Reference | Acronym | Subsampling |
| --- | --- | --- | --- |
| Parkinson Range | Parkinson ([1980](https://arxiv.org/html/2602.19732v1#bib.bib62 "The extreme value method for estimating the variance of the rate of return")) | pr | - |
| Garman-Klass Range | Garman and Klass ([1980](https://arxiv.org/html/2602.19732v1#bib.bib42 "On the estimation of security price volatilities from historical data")) | gkr | - |
| Realized Range | Martens and Van Dijk ([2007](https://arxiv.org/html/2602.19732v1#bib.bib57 "Measuring volatility with the realized range")) | rr5 | - |
|  | Christensen and Podolskij ([2007](https://arxiv.org/html/2602.19732v1#bib.bib33 "Realized range-based estimation of integrated variance")) |  |  |
| Realized Variance | Andersen and Bollerslev ([1998](https://arxiv.org/html/2602.19732v1#bib.bib1 "Answering the skeptics: yes, standard volatility models do provide accurate forecasts")) | rv1, rv5 | rv5\_ss |
|  | Andersen et al. ([2003](https://arxiv.org/html/2602.19732v1#bib.bib2 "Modeling and forecasting realized volatility")) |  |  |
| Realized Quarticity | Barndorff-Nielsen and Shephard ([2002](https://arxiv.org/html/2602.19732v1#bib.bib9 "Econometric analysis of realized volatility and its use in estimating stochastic volatility models")) | rq1, rq5 | rq5\_ss |
| Bipower Variation | Barndorff-Nielsen and Shephard ([2004c](https://arxiv.org/html/2602.19732v1#bib.bib12 "Power and bipower variation with stochastic volatility and jumps")) | bv1, bv5 | bv5\_ss |
| Realized Semivariances (pos e neg) | Barndorff‐Nielsen et al. ([2010](https://arxiv.org/html/2602.19732v1#bib.bib16 "Measuring downside risk – realized semivariance")) | rsp1, rsp5, rsn1, rsn5 | rsp5\_ss, rsn5\_ss |
| Median Realized Variance | Andersen et al. ([2012](https://arxiv.org/html/2602.19732v1#bib.bib4 "Jump-robust volatility estimation using nearest neighbor truncation")) | medrv1, medrv5 | medrv5\_ss |
| Minimum Realized Variance | Andersen et al. ([2012](https://arxiv.org/html/2602.19732v1#bib.bib4 "Jump-robust volatility estimation using nearest neighbor truncation")) | minrv1, minrv5 | minrv5\_ss |
| Realized Kernel | Barndorff-Nielsen et al. ([2009](https://arxiv.org/html/2602.19732v1#bib.bib15 "Realized kernels in practice: trades and quotes")) | rk | - |

Table 12: Realized measures available in the VOLARE library. The number following the acronym indicates the time interval used to sample the series at equally spaced times (e.g., rv1 refers to the realized variance sampling prices at 1-minute intervals). For each subsampled realized measure (suffix s​sss), we evaluate it using 5 subsample sets, each shifted by 1 minute.

To ensure estimation reliability, realized measures are computed only for trading days with at least 40 intraday observations or with trading activity spanning less than two hours.

We also provide subsampled versions of several estimators (Zhou, [1996](https://arxiv.org/html/2602.19732v1#bib.bib70 "High-frequency data and volatility in foreign-exchange rates"); Zhang et al., [2005](https://arxiv.org/html/2602.19732v1#bib.bib68 "A tale of two time scales: determining integrated volatility with noisy high-frequency data")). The subsampling technique computes realized measures on multiple, slightly shifted sampling grids and averages the resulting estimates. In practice, we start from a fixed sampling frequency (every 5 minutes in our library) and we create several subsamples by shifting the grid by a fraction of that interval (in our case, one minute). Each realized measure is computed separately for each subsample, and the final estimator is obtained by averaging the subsample results. Compared to the corresponding estimator computed on a single, fixed sampling grid, this procedure improves estimator efficiency by reducing both variance and bias, while balancing the trade-off between high-frequency sampling (more but noisier information), and low-frequency sampling (less noise but it relies on fewer observations).

#### 5.1.1 Parkinson Range (pr)

The Parkinson variance range (Parkinson, [1980](https://arxiv.org/html/2602.19732v1#bib.bib62 "The extreme value method for estimating the variance of the rate of return"))
is calculated as

|  |  |  |
| --- | --- | --- |
|  | pr=14​ln⁡(2)ln(HL)2.pr=\frac{1}{4\ln(2)}\ln\left(\frac{H}{L}\right)^{2}. |  |

#### 5.1.2 Garman-Klass Range (gkr)

The Garman-Klass variance range (Garman and Klass, [1980](https://arxiv.org/html/2602.19732v1#bib.bib42 "On the estimation of security price volatilities from historical data"))
is computed as

|  |  |  |
| --- | --- | --- |
|  | gkr=12ln(HL)2−(2ln(2)−1)ln(CO)2.gkr=\frac{1}{2}\ln\left(\frac{H}{L}\right)^{2}-(2\ln(2)-1)\ln\left(\frac{C}{O}\right)^{2}. |  |

#### 5.1.3 Realized Range (rr)

The Realized Range, introduced by Martens and Van Dijk ([2007](https://arxiv.org/html/2602.19732v1#bib.bib57 "Measuring volatility with the realized range")) and Christensen and Podolskij ([2007](https://arxiv.org/html/2602.19732v1#bib.bib33 "Realized range-based estimation of integrated variance")), is obtained as

|  |  |  |
| --- | --- | --- |
|  | rr=14​ln⁡(2)∑i=1mln(HiLi)2,rr=\frac{1}{4\ln(2)}\sum\_{i=1}^{m}\ln\left(\frac{H\_{i}}{L\_{i}}\right)^{2}, |  |

where HiH\_{i} and LiL\_{i} are the highest and the lowest prices, respectively, of the ii-th intraday interval, and mm is the number of such intervals.

#### 5.1.4 Realized Variance (rv)

The plain vanilla realized variance (Andersen and Bollerslev, [1998](https://arxiv.org/html/2602.19732v1#bib.bib1 "Answering the skeptics: yes, standard volatility models do provide accurate forecasts"); Andersen et al., [2003](https://arxiv.org/html/2602.19732v1#bib.bib2 "Modeling and forecasting realized volatility"))
is defined as

|  |  |  |
| --- | --- | --- |
|  | r​v=∑i=1mri2,rv=\sum\_{i=1}^{m}r\_{i}^{2}, |  |

where ri=ln⁡(pi/pi−1)r\_{i}=\ln(p\_{i}/p\_{i-1}) denotes the return of the ii-th interval.
Under the assumption of no jumps, it provides a consistent estimator of the integrated variance I​V=∫0Tσu2​𝑑uIV=\int\_{0}^{T}\sigma\_{u}^{2}du as the sampling frequency increases.

#### 5.1.5 Realized Quarticity (rq)

Following Barndorff-Nielsen and Shephard ([2002](https://arxiv.org/html/2602.19732v1#bib.bib9 "Econometric analysis of realized volatility and its use in estimating stochastic volatility models")), the realized quarticity is defined as

|  |  |  |
| --- | --- | --- |
|  | r​q=m3​∑i=1mri4.rq=\frac{m}{3}\sum\_{i=1}^{m}r\_{i}^{4}\,. |  |

The factor m/3m/3 acts as a normalization constant that adjusts for the sampling frequency and ensures that r​qrq is an unbiased estimator of the integrated quarticity I​Q=∫0Tσu4​𝑑uIQ=\int\_{0}^{T}\sigma\_{u}^{4}du.

#### 5.1.6 Bipower Variation (bv)

The Bipower Variation (Barndorff-Nielsen and Shephard, [2004c](https://arxiv.org/html/2602.19732v1#bib.bib12 "Power and bipower variation with stochastic volatility and jumps")) is a robust volatility estimator that captures the continuous component of price movements. It is defined as

|  |  |  |
| --- | --- | --- |
|  | b​v=π2​∑i=2m|ri|​|ri−1|.bv=\frac{\pi}{2}\sum\_{i=2}^{m}|r\_{i}||r\_{i-1}|. |  |

#### 5.1.7 Realized Semivariances (rsp, rsn)

Realized semivariances (Barndorff‐Nielsen et al., [2010](https://arxiv.org/html/2602.19732v1#bib.bib16 "Measuring downside risk – realized semivariance")) decompose price volatility into its upside and downside components, providing critical insight into the asymmetric nature of financial market fluctuations. The downside (upside) realized semivariance r​s−rs^{-} (r​s+rs^{+})
captures the variance contribution from negative (positive) returns, as defined by

|  |  |  |
| --- | --- | --- |
|  | r​s−=∑i=1mri2​I[ri<0]r​s+=∑i=1mri2​I[ri>0].rs^{-}=\sum\_{i=1}^{m}r\_{i}^{2}\;I\_{[r\_{i}<0]}\qquad rs^{+}=\sum\_{i=1}^{m}r\_{i}^{2}\;I\_{[r\_{i}>0]}. |  |

The indicators I[ri<0]I\_{[r\_{i}<0]} and I[ri>0]I\_{[r\_{i}>0]}
ensure that only negative or positive returns, respectively, contribute to each measure. The two components sum to the total realized variance, i.e.
r​v=r​s++r​s−rv=rs^{+}+rs^{-}.

#### 5.1.8 Median Realized Variance (medrv)

Median realized variance (Andersen et al., [2012](https://arxiv.org/html/2602.19732v1#bib.bib4 "Jump-robust volatility estimation using nearest neighbor truncation")) provides a robust alternative to standard realized variance estimators by effectively filtering out jumps in the price process. It uses the median of three consecutive squared returns to minimize the impact of outliers and price discontinuities, making it particularly valuable for distinguishing between continuous volatility components and jump variations. Formally, the median realized variance is computed as

|  |  |  |
| --- | --- | --- |
|  | medRV=π6−4​3+π⋅mm−2​∑i=2m−1med​(|ri−1|,|ri|,|ri+1|)2,\text{medRV}=\frac{\pi}{6-4\sqrt{3}+\pi}\cdot\frac{m}{m-2}\sum\_{i=2}^{m-1}\text{med}(|r\_{i-1}|,|r\_{i}|,|r\_{i+1}|)^{2}, |  |

where med​(⋅)\text{med}(\cdot) denotes the median operator.
The scaling factor π6−4​3+π\frac{\pi}{6-4\sqrt{3}+\pi} ensures consistency toward the integrated variance, while the mm−2\frac{m}{m-2} term provides a small-sample bias adjustment.

#### 5.1.9 Minimum Realized Variance (minrv)

Minimum realized variance (Andersen et al., [2012](https://arxiv.org/html/2602.19732v1#bib.bib4 "Jump-robust volatility estimation using nearest neighbor truncation")) is another robust estimator of realized variance designed to mitigate the impact of jumps. It is based on the minimum of two adjacent squared returns, effectively filtering out large price movements that might represent jumps, rather than continuous volatility. The estimator is defined as

|  |  |  |
| --- | --- | --- |
|  | minRV=ππ−2⋅mm−1∑i=2mmin(|ri−1|,|ri|)2,\text{minRV}=\frac{\pi}{\pi-2}\cdot\frac{m}{m-1}\sum\_{i=2}^{m}\min(|r\_{i-1}|,|r\_{i}|)^{2}, |  |

where the scaling factor ππ−2\frac{\pi}{\pi-2} ensures consistency toward the integrated variance, while mm−1\frac{m}{m-1} provides a finite-sample bias adjustment.

#### 5.1.10 Realized Kernel (rk)

The realized kernel variance estimator, introduced by Barndorff-Nielsen et al. ([2008](https://arxiv.org/html/2602.19732v1#bib.bib14 "Designing realized kernels to measure the ex post variation of equity prices in the presence of noise"), [2009](https://arxiv.org/html/2602.19732v1#bib.bib15 "Realized kernels in practice: trades and quotes")), provides a consistent and efficient way to estimate the integrated variance in presence of market microstructure noise. Denoting with rir\_{i} a generic high-frequency return, the realized kernel estimator is

|  |  |  |
| --- | --- | --- |
|  | r​k=γ0+2​∑h=1Hk​(hH+1)​γh,rk=\gamma\_{0}+2\sum\_{h=1}^{H}k\left(\frac{h}{H+1}\right)\gamma\_{h}, |  |

where γ0\gamma\_{0} is the plain vanilla realized variance, and γh=∑i=h+1mri​ri−h\gamma\_{h}=\sum\_{i=h+1}^{m}r\_{i}r\_{i-h} are the autocovariances of order h,h≥0h,\ h\geq 0,
k​(⋅)k(\cdot) is a kernel function, and HH is the bandwidth parameter.
The choice of kernel function k​(⋅)k(\cdot) is crucial for the estimator’s properties. In our calculations, we employ the Parzen kernel due to its excellent balance between efficiency and robustness.121212Barndorff-Nielsen et al. ([2009](https://arxiv.org/html/2602.19732v1#bib.bib15 "Realized kernels in practice: trades and quotes")) show that the Parzen kernel fulfills all necessary conditions to guarantee the positivity of the estimator and consistent estimation of integrated variance in the presence of microstructure noise. Its expression is:

|  |  |  |
| --- | --- | --- |
|  | k​(x)={1−6​x2+6​x30≤x≤1/22​(1−x)31/2<x≤10x>1.k(x)=\begin{cases}1-6x^{2}+6x^{3}&0\leq x\leq 1/2\\ 2(1-x)^{3}&1/2<x\leq 1\\ 0&x>1.\end{cases} |  |

We select the bandwidth as

|  |  |  |
| --- | --- | --- |
|  | H∗=c∗​ξ4/5​m3/5,H^{\*}=c^{\*}\xi^{4/5}m^{3/5}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | c∗={k′′​(0)2k0,0}1/5,c^{\*}=\left\{\frac{k^{\prime\prime}(0)^{2}}{k\_{0,0}}\right\}^{1/5}, |  |

with k′′​(0)2k^{\prime\prime}(0)^{2} representing the squared second derivative of the kernel function evaluated at zero, and k0,0=‖k‖22=∫01k​(x)2​𝑑xk\_{0,0}=\|k\|\_{2}^{2}=\int\_{0}^{1}k(x)^{2}dx is the squared L2L^{2}-norm of the kernel function over its support.131313For our Parzen kernel, c∗=((12)2/0.269)1/5=3.5134c^{\*}=((12)^{2}/0.269)^{1/5}=3.5134.

The term ξ2\xi^{2} is a function of the variance ω2\omega^{2} of the market microstructure noise contaminating observed prices, and the integrated quarticity:

|  |  |  |
| --- | --- | --- |
|  | ξ2=ω2(T⋅I​Q)1/2≈ω2I​V,\xi^{2}=\frac{{\omega}^{2}}{({T\cdot IQ})^{1/2}}\approx\frac{{\omega}^{2}}{{{IV}}}, |  |

where we justify the approximation (T⋅I​Q)1/2≈I​V({T\cdot IQ})^{1/2}\approx IV on the grounds that with moderate volatility variation, I​Q≈I​V2/TIQ\approx IV^{2}/T.141414Barndorff-Nielsen et al. ([2009](https://arxiv.org/html/2602.19732v1#bib.bib15 "Realized kernels in practice: trades and quotes")) note that this simplification is reasonable in practical applications and makes bandwidth selection more stable, as estimating I​VIV is significantly simpler than estimating IQ.

We estimate the numerator and denominator of ξ2\xi^{2} as follows.

##### Noise variance.

Following Barndorff-Nielsen et al. ([2009](https://arxiv.org/html/2602.19732v1#bib.bib15 "Realized kernels in practice: trades and quotes"), p. C5), building on Zhang et al. ([2005](https://arxiv.org/html/2602.19732v1#bib.bib68 "A tale of two time scales: determining integrated volatility with noisy high-frequency data")) and Bandi and Russell ([2008](https://arxiv.org/html/2602.19732v1#bib.bib8 "Microstructure noise, realized variance, and optimal sampling")), we estimate the noise variance as realized variance computed using 2-minute returns, R​V2’RV\_{\text{2'}}, divided by the number of non-zero returns, nn:

|  |  |  |
| --- | --- | --- |
|  | ω^2=R​V2’2​n\hat{\omega}^{2}=\frac{RV\_{\text{2'}}}{2n} |  |

##### Integrated variance.

Following (Barndorff-Nielsen et al., [2009](https://arxiv.org/html/2602.19732v1#bib.bib15 "Realized kernels in practice: trades and quotes"), p. C4), we compute sparse realized variances based on 20-minute returns, on pp windows, each adding one second and dropping one second (hence p=20×60=1200p=20\times 60=1200 subsamples). More specifically, if RV(j)\text{RV}^{(j)} represents the realized variance computed from the jj-th subsample, then the estimated I​VIV is the average of the pp sparse realized variances

|  |  |  |
| --- | --- | --- |
|  | IV^=RVsparse=1p​∑j=1pRV(j).\widehat{\text{IV}}=\text{RV}\_{\text{sparse}}=\frac{1}{p}\sum\_{j=1}^{p}\text{RV}^{(j)}. |  |

##### End effect.

Boundary treatment plays a crucial role in realized kernel estimation, as bias tends to accumulate at the edges of the sampling period. Barndorff-Nielsen et al. ([2009](https://arxiv.org/html/2602.19732v1#bib.bib15 "Realized kernels in practice: trades and quotes")) suggest using jittering techniques and endpoint corrections to address boundary effects. These methods involve adjusting the first and last observations before sampling prices, using the average of the two preceding and two succeeding prices to mitigate any edge-related bias.

### 5.2 Multivariate Series

A key challenge in estimating realized covariance from high-frequency financial data is the lack of synchronicity between price observations across assets. There are two popular approaches to address this issue: (i) the “previous-tick” method, which uses a regularly spaced time grid and set the price of each asset to the last observed before each grid time (Zhang, [2011](https://arxiv.org/html/2602.19732v1#bib.bib69 "Estimating covariation: epps effect, microstructure noise")); (ii) the refresh time scheme, which considers irregularly spaced data where each time is the instant at which all assets have been traded at least once from the previous time (Barndorff-Nielsen et al., [2011](https://arxiv.org/html/2602.19732v1#bib.bib17 "Multivariate realised kernels: consistent positive semi-definite estimators of the covariation of equity prices with noise and non-synchronous trading")).

We adopt the previous-tick method, using the most recent transaction price available before each time of a 1-minute grid. This procedure yields a synchronized, regularly spaced return series across all assets, allowing the use of standard realized covariance estimators.

When applying the previous-tick synchronization to futures contracts, an additional complication arises from heterogeneous trading schedules across exchanges. Unlike equities or exchange rates that typically share common trading hours, futures contracts trade on different exchanges (NYMEX, COMEX, CBOT, CME) with varying session structures.
  
On days when trading hours differ substantially across contracts, for instance, when corn trades only during evening hours (19:00–23:59 ET) while other futures operate continuously, we assign zero returns to the asset with limited hours during non-overlapping periods. This may introduce a downward bias in the estimated covariances between contracts with misaligned trading schedules, particularly affecting pairs involving CBOT agricultural contracts.
These non-synchronous trading episodes occur on a limited number of days in our sample, primarily during exchange-specific holidays or restricted trading sessions.

Considering NN assets observed at mm equally-spaced intervals during a single trading day, we denote as ri,kr\_{i,k} the return of the ii-th asset during the kk-th intraday interval (i=1,2,…,Ni=1,2,\ldots,N, k=1,2,…,mk=1,2,\ldots,m), and as 𝐫k=[r1,k,r2,k,…,rN,k]\mathbf{r}\_{k}=[r\_{1,k},r\_{2,k},\ldots,r\_{N,k}] the vector of returns in the interval.
We provide realized covariance matrices for groups of assets categorized by type (e.g., stocks, exchange rates, and futures).

[Table 13](https://arxiv.org/html/2602.19732v1#S5.T13 "Table 13 ‣ 5.2 Multivariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)") summarizes the covariance measures calculated.

| Measure | Reference | Acronym |
| --- | --- | --- |
| Realized Covariance | Barndorff-Nielsen and Shephard ([2004b](https://arxiv.org/html/2602.19732v1#bib.bib11 "Econometric analysis of realized covariation: high frequency based covariance, regression, and correlation in financial economics")) | rcov |
| Bipower Covariance | Barndorff-Nielsen and Shephard ([2004a](https://arxiv.org/html/2602.19732v1#bib.bib13 "Measuring the impact of jumps in multivariate price processes using bipower covariation")) | rbpcov |
| Realized Semicovariances | Bollerslev et al. ([2020](https://arxiv.org/html/2602.19732v1#bib.bib23 "Realized semicovariances")) | rscov\_p, rscov\_n, |
| (pos, neg, mixed) |  | rscov\_mp, rscov\_mn |

Table 13: Covariance measures provided in the VOLARE library. For all estimates, we to obtain equally spaced, 1-minute data using the “previous-tick” method.

#### 5.2.1 Realized Covariance (rcov)

Following Barndorff-Nielsen and Shephard ([2004b](https://arxiv.org/html/2602.19732v1#bib.bib11 "Econometric analysis of realized covariation: high frequency based covariance, regression, and correlation in financial economics")), the realized covariance between two assets ii and jj over a single trading day is defined as the sum of the products of their synchronized intraday returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rci,j=∑k=1mri,k⋅rj,k.\text{rc}\_{i,j}=\sum\_{k=1}^{m}r\_{i,k}\cdot r\_{j,k}. |  | (1) |

For a set of NN assets, the realized covariance matrix aggregates all pairwise covariances into the N×NN\times N matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐫𝐜=∑k=1m𝐫k​𝐫k′.\mathbf{rc}=\sum\_{k=1}^{m}\mathbf{r}\_{k}\mathbf{r}\_{k}^{\prime}. |  | (2) |

#### 5.2.2 Realized Bipower Covariance (rbpcov)

The realized bipower covariance is a robust estimator of integrated covariance that is less sensitive to jumps compared to the standard realized covariance. Following Barndorff-Nielsen and Shephard ([2004a](https://arxiv.org/html/2602.19732v1#bib.bib13 "Measuring the impact of jumps in multivariate price processes using bipower covariation")), the bipower covariance between assets ii and jj is defined as:

|  |  |  |
| --- | --- | --- |
|  | bci,j=μ1−24​∑k=2m(|ri,k−1+rj,k−1|⋅|ri,k+rj,k|−|ri,k−1−rj,k−1|⋅|ri,k−rj,k|).\text{bc}\_{i,j}=\frac{\mu\_{1}^{-2}}{4}\sum\_{k=2}^{m}\biggl(\left|r\_{i,k-1}+r\_{j,k-1}\right|\cdot\left|r\_{i,k}+r\_{j,k}\right|-\left|r\_{i,k-1}-r\_{j,k-1}\right|\cdot\left|r\_{i,k}-r\_{j,k}\right|\biggr). |  |

with μ1=2/π≈0.7979\mu\_{1}=\sqrt{2/\pi}\approx 0.7979 being the first moment of the absolute value of a standard normal random variable
When i=ji=j, this formulation simplifies to the standard realized bipower variation of asset ii.

#### 5.2.3 Realized Semicovariances (rscov)

Realized semicovariances extend the traditional covariance framework by decomposing co-movements between assets based on the signs of their returns, thereby uncovering asymmetric dependence structures that vary across market conditions.

Following Bollerslev et al. ([2020](https://arxiv.org/html/2602.19732v1#bib.bib23 "Realized semicovariances")), we decompose the realized covariance matrix into four components based on the signs of the underlying high-frequency returns. We first define the signed return vectors as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐫k+\displaystyle\mathbf{r}\_{k}^{+} | =𝐫k⊙𝟏​{𝐫k>𝟎},\displaystyle=\mathbf{r}\_{k}\odot\mathbf{1}\{\mathbf{r}\_{k}>\mathbf{0}\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐫k−\displaystyle\mathbf{r}\_{k}^{-} | =𝐫k⊙𝟏​{𝐫k≤𝟎},\displaystyle=\mathbf{r}\_{k}\odot\mathbf{1}\{\mathbf{r}\_{k}\leq\mathbf{0}\}, |  |

where ⊙\odot denotes element-wise multiplication and 𝟏​{⋅}\mathbf{1}\{\cdot\} is the indicator function applied element-wise. The four daily realized semicovariance matrices are then defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐫𝐬++\displaystyle\mathbf{rs^{++}} | =∑k=1m𝐫k+​(𝐫k+)′,(concordant positive)\displaystyle=\sum\_{k=1}^{m}\mathbf{r}\_{k}^{+}(\mathbf{r}\_{k}^{+})^{\prime},\quad\text{(concordant positive)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐫𝐬−−\displaystyle\mathbf{rs^{--}} | =∑k=1m𝐫k−​(𝐫k−)′,(concordant negative)\displaystyle=\sum\_{k=1}^{m}\mathbf{r}\_{k}^{-}(\mathbf{r}\_{k}^{-})^{\prime},\quad\text{(concordant negative)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐫𝐬+−\displaystyle\mathbf{rs^{+-}} | =∑k=1m𝐫k+​(𝐫k−)′,(mixed/discordant positive-negative)\displaystyle=\sum\_{k=1}^{m}\mathbf{r}\_{k}^{+}(\mathbf{r}\_{k}^{-})^{\prime},\quad\text{(mixed/discordant positive-negative)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐫𝐬−+\displaystyle\mathbf{rs^{-+}} | =∑k=1m𝐫k−​(𝐫k+)′,(mixed/discordant negative-positive)\displaystyle=\sum\_{k=1}^{m}\mathbf{r}\_{k}^{-}(\mathbf{r}\_{k}^{+})^{\prime},\quad\text{(mixed/discordant negative-positive)} |  |

The positive semicovariance 𝐫𝐬++\mathbf{rs^{++}} captures co-movement during periods when assets experience positive returns, reflecting synchronized upward movements. The negative semicovariance matrix 𝐫𝐬−−\mathbf{rs^{--}} measures co-movement during joint downward movements, which is particularly relevant for risk management and portfolio diversification analysis. The mixed semicovariance matrices 𝐫𝐬+−\mathbf{rs^{+-}} and 𝐫𝐬−+\mathbf{rs^{-+}} capture the co-movement when assets move in opposite directions.

By construction, the standard realized covariance matrix can be decomposed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐫𝐜=𝐫𝐬+++𝐫𝐬−−+𝐫𝐬+−+𝐫𝐬−+.\mathbf{rc}=\mathbf{rs^{++}}+\mathbf{rs^{--}}+\mathbf{rs^{+-}}+\mathbf{rs^{-+}}. |  | (3) |

Notice that while 𝐫𝐬++\mathbf{rs^{++}} and 𝐫𝐬−−\mathbf{rs^{--}} are symmetric and positive semidefinite, the mixed semicovariance matrices 𝐫𝐬+−\mathbf{rs^{+-}} and 𝐫𝐬−+\mathbf{rs^{-+}} are generally asymmetric, with zero diagonal elements by construction.

## 6 The VOLARE Front-end: Architecture and User Experience

The VOLARE platform integrates a structured back-end infrastructure, with a user-centered front-end interface.

The back-end forms the operational core of the system, automating the entire data lifecycle: from the initial download of high-frequency market data, via the Kibot API, to the documented operations leading to the computation of realized variance and covariance measures. All raw and processed data are stored in a MinIO-based data lake, while final statistical outputs are housed in a PostgreSQL relational database, ensuring full traceability, coherence, and streamlined data retrieval. Efficient storage and indexing enable fast query response times, while the infrastructure setup involves automated monthly updates and regular monitored backups, to guarantee continuity and rapid recovery in case of failures. Future extensions across assets and classes of assets would maintain the same design.

The VOLARE front-end, developed in React, is designed to provide users with an intuitive interface for accessing and exploring high-frequency financial data.

### 6.1 Homepage

The Homepage serves as the entry point to the platform, welcoming users with a presentation of VOLARE’s purpose and capabilities. It provides an access to comprehensive realized volatility and covariance measures derived from high-frequency financial data, contextualizing the project within financial econometrics research.

From the Homepage, users can access the platform’s two core functionalities through prominent action buttons: Download Data for direct dataset access and Visualize Data for the Interactive Dashboard. This dual-path design acknowledges different user workflows: some prefer downloading complete datasets for offline analysis, while others benefit from interactive web-based exploration tools.

Additional information pages are accessible through the navigation bar:

##### Documentation

The page provides comprehensive insight into the technical and methodological foundations of the platform, detailing the complete data processing pipeline from high-frequency tick data acquisition through the Kibot API to the computation of realized measures. Users can access detailed explanations of data sources and coverage, cleaning and preprocessing procedures, and statistical methodologies employed for computing realized variance and covariance measures.

##### About

The page presents VOLARE’s foundational mission and motivations. VOLARE (VOLatility Archive for Realized Estimates) was created to address a fundamental challenge in financial research: making high-quality, research-grade realized volatility data accessible to financial researchers, quantitative analysts, and academics. The page articulates the platform’s origin story, explaining how direct experience with the complexity of processing, cleaning, and extracting meaningful volatility estimates from ultra-high-frequency data drove the creation of VOLARE.

##### FAQ

The Frequently Asked Questions page addresses common questions regarding platform usage, data access, and methodology, offering concise answers about VOLARE’s features.

### 6.2 Download Data: Direct Dataset Access

For users who prefer working by themselves outside the VOLARE platform, the Download section offers direct access to pre-organized data packages. This section provides a catalog of available datasets organized by asset type (stocks, exchange rates, futures), allowing users to download complete historical series in standardized formats. Each dataset comes with a README file that documents asset type and data type (variance or covariance), temporal coverage with date range and total number of records, the list of included assets with their symbols, and all available measures. This structured documentation ensures that users have complete metadata for proper integration into their analytical environments and suitable citation in research outputs.

### 6.3 Visualize Data: The Core Analytical Interface

Accessible via the Visualize Data button on the Homepage, the Interactive Dashboard is the heart of the VOLARE platform’s exploratory analysis capabilities. The dashboard guides users through a sequential workflow with the following steps:

* •

  Asset Type Selection: Users select the category of financial instruments to analyze (Stocks, Exchange Rates, or Futures)
* •

  Symbol Selection: Users can either search for a specific symbol or choose from the list of available assets within the selected category
* •

  Date Range Selection: Users can define the temporal scope of the analysis by selecting a custom date range. If no range is specified, the system will automatically set the date range to eleven months from the current date to ensure data availability (e.g., on November 13, 2025, the default range would be from October 13, 2024, to October 13, 2025)
* •

  Measure Selection: Users specify which realized volatility or covariance statistics to analyze from the available measures

Upon completing the workflow, the platform transitions to the Results page, where requested data is presented through an interactive visualization environment designed to facilitate both exploratory analysis and formal statistical investigation. The centerpiece is a dynamic graphing system with zoom and functionality for detailed temporal inspection and hover tooltips displaying values and dates.

Alongside the graphical display, a panel provides key statistical summary metrics computed in real-time: average volatility, volatility of volatility, average returns, average volume.

Moving beyond standard visualization, the platform provides advanced analytical features that enhance exploratory research. Users can add additional measures to the current view for multi-measure comparison without returning to the configuration workflow, enabling side-by-side evaluation of different volatility estimators. As presented in detail in [Section 7](https://arxiv.org/html/2602.19732v1#S7 "7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"), the platform offers integration with established volatility forecasting models including: HAR, HAR-Q, MEM(1,1), AMEM(1,1), and AMEM(2,1), allowing users to overlay model forecasts onto historical data and assess forecast accuracy through visual inspection and quantitative metrics.

Recognizing that users often need to continue analysis outside the web platform, VOLARE provides comprehensive export capabilities including high-resolution graph export of current visualizations and raw data downloads ready for import into statistical software.

## 7 The VOLARE Front-end: Volatility Models

Volatility modeling plays a central role in financial econometrics, with applications ranging from risk management and derivatives pricing to portfolio allocation. Over the years, a variety of models have been developed to capture the persistence and dynamics of financial market volatility (see, e.g., Andersen and Bollerslev ([1998](https://arxiv.org/html/2602.19732v1#bib.bib1 "Answering the skeptics: yes, standard volatility models do provide accurate forecasts")); Hansen and Lunde ([2005](https://arxiv.org/html/2602.19732v1#bib.bib48 "A forecast comparison of volatility models: does anything beat a GARCH(1,1)?")); Bollerslev et al. ([2016](https://arxiv.org/html/2602.19732v1#bib.bib24 "Exploiting the errors: a simple approach for improved volatility forecasting")); Cipollini and Gallo ([2025](https://arxiv.org/html/2602.19732v1#bib.bib29 "Multiplicative Error Models: 20 years on"))).

For realized volatility forecasting, two popular frameworks are the Heterogeneous Autoregressive (HAR) model (Corsi, [2009](https://arxiv.org/html/2602.19732v1#bib.bib32 "A simple approximate long-memory model of realized volatility")) and the Multiplicative Error Model (MEM) family (Engle, [2002](https://arxiv.org/html/2602.19732v1#bib.bib37 "New frontiers for ARCH models"); Engle and Gallo, [2006](https://arxiv.org/html/2602.19732v1#bib.bib38 "A multiple indicators model for volatility using intra-daily data")). VOLARE currently supports HAR and HAR-Q specifications, as well as MEM, Asymmetric MEM (AMEM), and AMEM(2,1) models. Users can estimate these models with a variety of realized variance measures, including Parkinson range, Garman–Klass, realized range, realized variance, bipower variation, median realized variance, minimum-variance, and realized kernel.

In practice, users may specify the sample period, asset ticker, and volatility measure of interest. The selected data is first visualized, after which a model can be chosen for estimation. Model estimation is performed only if the chosen range contains at least 750 observations (corresponding roughly to three years of daily data). Once this condition is met, VOLARE reports parameter estimates, together with standard diagnostic checks on the residuals.
Moreover, when enough data past the selected window for estimation are available, one-step-ahead forecasts are generated for at least five and up to twenty-two out-of-sample periods. The graphical output overlays both the in-sample estimates and the out-of-sample forecasts on the volatility series. Confidence intervals are provided only for the forecasts, together with evaluation metrics, enabling users to assess predictive accuracy against observed outcomes.

Before delving into the details of model estimation, it is important to clarify some aspects regarding the scales adopted for estimation and forecasting.
HAR models are estimated on daily variance measures, to preserve the linear structure of the model; in contrast, MEM family are estimated using annualized volatility, calculated as 252×variance×100\sqrt{252\times\text{variance}}\times 100. Accordingly, the reported parameter estimates refer to such scales.
In the graphical outputs, however, both model families display results on the annualized volatility scale to facilitate comparison.

The following sections introduce the models considered and describe the procedures employed for their estimation and forecasting. An example of the analysis of the estimated volatility models across different realized variance measures for assets in different classes is provided in Appendix [A.2](https://arxiv.org/html/2602.19732v1#A1.SS2 "A.2 Volatility Analysis across Assets: A Test Run ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)").

### 7.1 Heterogeneous Autoregressive Models

#### 7.1.1 HAR

The Heterogeneous Autoregressive (HAR) model, introduced by Corsi ([2009](https://arxiv.org/html/2602.19732v1#bib.bib32 "A simple approximate long-memory model of realized volatility")), makes the current variance measure to linearly depend on its own past, up to one month, by means of suitably restricted coefficients.
Formally, the model can be specified as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=ω+αd​yt−1+αw​yt−1(w)+αm​yt−1(m)+εt,y\_{t}=\omega+\alpha\_{d}y\_{t-1}+\alpha\_{w}y\_{t-1}^{(w)}+\alpha\_{m}y\_{t-1}^{(m)}+\varepsilon\_{t}, |  | (4) |

where yty\_{t} denotes the daily variance measure, yt−1(w)y\_{t-1}^{(w)} and yt−1(m)y\_{t-1}^{(m)} are the weekly and monthly components defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt−1\displaystyle y\_{t-1} | (daily component) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | yt−1(w)\displaystyle y^{(w)}\_{t-1} | =14​∑i=25yt−i(weekly component)\displaystyle=\frac{1}{4}\sum\_{i=2}^{5}y\_{t-i}\quad\text{(weekly component)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | yt−1(m)\displaystyle y^{(m)}\_{t-1} | =116​∑i=622yt−i(monthly component)\displaystyle=\frac{1}{16}\sum\_{i=6}^{22}y\_{t-i}\quad\text{(monthly component)} |  |

The weekly component starts from i=2i=2 to avoid overlap with the daily term, while the monthly component is computed over days t−6t-6 to t−22t-22 so as to exclude the lags already used in the daily and weekly components. This construction ensures that each component (daily, weekly, and monthly) contributes distinct and non-redundant information to the model, thereby enhancing clarity and interpretability.

#### 7.1.2 HAR-Q

The HAR-Q model (Bollerslev et al., [2016](https://arxiv.org/html/2602.19732v1#bib.bib24 "Exploiting the errors: a simple approach for improved volatility forecasting")) extends the HAR specification for realized variance measures, by incorporating realized quarticity (rq) as a proxy for the conditional variance of measurement errors. The specification is

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=ω+(αd+αQ​r​qt−11/2)​yt−1+αw​yt−1(w)+αm​yt−1(m)+εt,y\_{t}=\omega+\left(\alpha\_{d}+\alpha\_{Q}rq\_{t-1}^{1/2}\right)y\_{t-1}+\alpha\_{w}y\_{t-1}^{(w)}+\alpha\_{m}y\_{t-1}^{(m)}+\varepsilon\_{t}, |  | (5) |

where r​qt−11/2rq\_{t-1}^{1/2} is the square root of the lagged realized quarticity ([5.1.5](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS5 "5.1.5 Realized Quarticity (rq) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"))
demeaned for interpretability. The time-varying coefficient on the daily lag becomes α1,t=αd+αQ​r​qt−11/2\alpha\_{1,t}=\alpha\_{d}+\alpha\_{Q}rq\_{t-1}^{1/2}.

#### 7.1.3 Parameter Estimation Procedure

Once the functional form of the model HAR or HAR-Q is specified, parameter estimation proceeds via Ordinary Least Squares (OLS).

1. 1.

   Estimation. The parameters ω,αd,αw,αm\omega,\alpha\_{d},\alpha\_{w},\alpha\_{m}, and αQ\alpha\_{Q} are obtained by regressing the variance measure on its daily, weekly, and monthly components, as well as the HAR-Q interaction term.
2. 2.

   Inference. To ensure valid inference in the presence of possible heteroskedasticity and serial correlation, robust standard errors are computed using the Heteroskedasticity and Autocorrelation Consistent (HAC) covariance estimator of Newey and West ([1987](https://arxiv.org/html/2602.19732v1#bib.bib58 "A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix")). The automatic lag selection rule of Newey and West ([1994](https://arxiv.org/html/2602.19732v1#bib.bib59 "Automatic lag selection in covariance matrix estimation")) is employed:

   |  |  |  |
   | --- | --- | --- |
   |  | maxlags=⌊4⋅(T100)2/9⌋,\text{maxlags}=\left\lfloor 4\cdot\left(\frac{T}{100}\right)^{2/9}\right\rfloor, |  |

   where TT denotes the sample size.
   This procedure adjusts the covariance matrix in a data-driven manner, providing reliable standard errors without requiring explicit distributional assumptions.
3. 3.

   Residual diagnostic. The adequacy of the model is further assessed by analyzing the residuals ε^t\hat{\varepsilon}\_{t}. The Ljung–Box test (Ljung and Box, [1978](https://arxiv.org/html/2602.19732v1#bib.bib55 "On a measure of lack of fit in time series models")) is applied to residuals and squared residuals (5 lags) to detect potential autocorrelation and conditional heteroskedasticity. In addition, Engle’s ARCH test (Engle, [1982](https://arxiv.org/html/2602.19732v1#bib.bib34 "Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation")) with 5 lags is used to formally test for remaining autoregressive conditional heteroskedasticity.

### 7.2 The Multiplicative Error Models (MEM)

The Multiplicative Error Model (MEM), introduced by Engle ([2002](https://arxiv.org/html/2602.19732v1#bib.bib37 "New frontiers for ARCH models")) and extended by Engle and Gallo ([2006](https://arxiv.org/html/2602.19732v1#bib.bib38 "A multiple indicators model for volatility using intra-daily data")), is designed to model non-negative time series such as realized volatility, trading volume, or durations. The key idea is to decompose the observed variable into the product of a deterministic conditional mean and a non-negative innovation,

|  |  |  |
| --- | --- | --- |
|  | yt=μt⋅εt,εt​∼i.i.d​D+​(1,σ2),y\_{t}=\mu\_{t}\cdot\varepsilon\_{t},\quad\varepsilon\_{t}\overset{\text{i.i.d}}{\sim}D^{+}(1,\sigma^{2}), |  |

where μt\mu\_{t} denotes the conditional mean of yty\_{t} given past information ℐt−1\mathcal{I}\_{t-1}, and εt\varepsilon\_{t} is a non-negative innovation term.
Common choices for the distribution D+D^{+} include Gamma and Lognormal distributions.

#### 7.2.1 MEM(1,1)

The conditional mean μt\mu\_{t} is typically modeled through a dynamic autoregressive structure analogous to a GARCH(1,1) process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt=ω+α1​yt−1+β1​μt−1.\mu\_{t}=\omega+\alpha\_{1}\,y\_{t-1}+\beta\_{1}\,\mu\_{t-1}. |  | (6) |

The parameters of the model must satisfy

* •

  ω>0\omega>0,
* •

  α1≥0\alpha\_{1}\geq 0,
* •

  0≤β1<10\leq\beta\_{1}<1,
* •

  persistence == α1+β1<1\alpha\_{1}+\beta\_{1}<1

to guarantee non-negativity and covariance stationarity.

#### 7.2.2 Asymmetric MEM (AMEM)

The Asymmetric Multiplicative Error Model (AMEM) (Engle and Gallo, [2006](https://arxiv.org/html/2602.19732v1#bib.bib38 "A multiple indicators model for volatility using intra-daily data"); Cipollini et al., [2021](https://arxiv.org/html/2602.19732v1#bib.bib28 "Realized volatility forecasting: robustness to measurement errors")) extends the MEM by allowing for asymmetric effects of past shocks on current volatility. Empirical evidence suggests that negative returns often trigger stronger volatility responses than positive returns of the same magnitude, a phenomenon referred to as the leverage effect.

##### AMEM(1,1)

The specification of the conditional mean is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt=ω+α1​yt−1+β1​μt−1+γ1​yt−1(−),\mu\_{t}=\omega+\alpha\_{1}\,y\_{t-1}+\beta\_{1}\,\mu\_{t-1}+\gamma\_{1}\,y^{(-)}\_{t-1}, |  | (7) |

where yt−1(−)=yt−1⋅𝕀​(rt−1<0)y^{(-)}\_{t-1}=y\_{t-1}\cdot\mathbb{I}(r\_{t-1}<0) captures the asymmetric component linked to negative returns, and rt−1r\_{t-1} denotes the return at time t−1t-1.

To ensure positivity and covariance stationarity, the parameters are restricted as follows

* •

  ω>0\omega>0,
* •

  α1,γ1≥0\alpha\_{1},\gamma\_{1}\geq 0,
* •

  0≤β1<10\leq\beta\_{1}<1,
* •

  persistence == α1+β1+γ12<1\alpha\_{1}+\beta\_{1}+\frac{\gamma\_{1}}{2}<1.

##### AMEM(2,1)

This is an extension of the AMEM allowing for two lags of the dependent variable,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μt\displaystyle\mu\_{t} | =ω+α1​yt−1+α2​yt−2+β1​μt−1+γ1​yt−1(−).\displaystyle=\omega+\alpha\_{1}\,y\_{t-1}+\alpha\_{2}\,y\_{t-2}+\beta\_{1}\,\mu\_{t-1}+\gamma\_{1}\,y^{(-)}\_{t-1}. |  | (8) |

In this case, to ensure positivity and stationarity the following parameter restrictions are imposed

* •

  ω>0\omega>0,
* •

  α1≥0\alpha\_{1}\geq 0, α1+γ1≥0\alpha\_{1}+\gamma\_{1}\geq 0,
* •

  0≤β1<10\leq\beta\_{1}<1,
* •

  α2+α1​β1≥0\alpha\_{2}+\alpha\_{1}\beta\_{1}\geq 0, α2+(α1+γ1)​β1≥0\alpha\_{2}+(\alpha\_{1}+\gamma\_{1})\beta\_{1}\geq 0,
* •

  persistence =α1+α2+β1+γ12<1=\alpha\_{1}+\alpha\_{2}+\beta\_{1}+\frac{\gamma\_{1}}{2}<1.

#### 7.2.3 Parameter Estimation Procedure

Once the functional form of the conditional mean and the distributional assumption for the multiplicative error are specified, parameter estimation proceeds via quasi maximum likelihood (QML). The procedure is inherently recursive: for each candidate parameter vector θ\theta, the sequence of conditional means {μt}t=1T\{\mu\_{t}\}\_{t=1}^{T} must be generated to evaluate the quasi log-likelihood. The steps are as follows.

1. 1.

   Initialization.
   Initial values for the parameter vector θ\theta are directly assigned so as to satisfy admissibility conditions (non-negativity and stationarity).
   The initial conditional mean is set to the unconditional mean implied by the model, e.g. μ0=ω/(1−α1−β1)\mu\_{0}=\omega/(1-\alpha\_{1}-\beta\_{1}) in a MEM(1,1). Parameter values are initialized as follows: the intercept ω\omega is chosen to match the sample mean y¯\bar{y} via ω=y¯⋅(1−persistence)\omega=\bar{y}\cdot(1-\text{persistence}); the autoregressive coefficient is set to β1≈0.6\beta\_{1}\approx 0.6; the innovation coefficient to α1≈0.1\alpha\_{1}\approx 0.1; and, for extended models, additional parameters, such as α2\alpha\_{2} and γ1\gamma\_{1}, are initialized at zero.
2. 2.

   Filtering step.
   For a given candidate θ\theta, the dynamic equation is used to recursively compute the path of conditional means. For example, in a MEM(1,1)

   |  |  |  |
   | --- | --- | --- |
   |  | μt=ω+α1​yt−1+β1​μt−1.\mu\_{t}=\omega+\alpha\_{1}y\_{t-1}+\beta\_{1}\mu\_{t-1}. |  |
3. 3.

   Log-likelihood evaluation.
   Given μt\mu\_{t}, the current multiplicative residual is εt=yt/μt\varepsilon\_{t}=y\_{t}/\mu\_{t}, so that the quasi log-likelihood is proportional to

   |  |  |  |
   | --- | --- | --- |
   |  | ℓ​(𝜽)∝∑t=1T[log⁡(εt)−εt+1].\ell(\boldsymbol{\theta})\propto\sum\_{t=1}^{T}\left[\log\left(\varepsilon\_{t}\right)-\varepsilon\_{t}+1\right]\,. |  |
4. 4.

   Likelihood maximization.
   Numerical optimization (implemented via a Sequential Least Squares Programming routine) iteratively updates θ\theta, recomputes {μt}\{\mu\_{t}\} and the quasi-log-likelihood, and adjusts parameters until convergence. Non-negativity constraints and stationarity restrictions are enforced throughout.
5. 5.

   Estimation of the error variance.
   The estimator of σ2\sigma^{2} is

   |  |  |  |
   | --- | --- | --- |
   |  | σ^2=1T​∑t=1T(ε^t−1)2,\hat{\sigma}^{2}=\frac{1}{T}\sum\_{t=1}^{T}(\hat{\varepsilon}\_{t}-1)^{2}, |  |

   where
   ε^t=yt/μ^t\widehat{\varepsilon}\_{t}=y\_{t}/\widehat{\mu}\_{t}, and μ^t\widehat{\mu}\_{t} is the conditional mean evaluated at the estimated θ^\widehat{\theta}.
6. 6.

   Inference.
   Following Brownlees et al. ([2012](https://arxiv.org/html/2602.19732v1#bib.bib26 "Multiplicative Error Models")), the asymptotic covariance matrix is estimated by

   |  |  |  |
   | --- | --- | --- |
   |  | 𝐕^​(𝜽^)=σ^2​[∑t=1Tμt2​∂μt∂𝜽​∂μt∂𝜽′|𝜽=𝜽^]−1,\hat{\mathbf{V}}(\hat{\boldsymbol{\theta}})=\hat{\sigma}^{2}\left[\sum\_{t=1}^{T}{\mu\_{t}^{2}}\frac{\partial\mu\_{t}}{\partial\boldsymbol{\theta}}\frac{\partial\mu\_{t}}{\partial\boldsymbol{\theta}^{\prime}}\Big|\_{\boldsymbol{\theta}=\widehat{\boldsymbol{\theta}}}\right]^{-1}, |  |

   so that standard errors are obtained as

   |  |  |  |
   | --- | --- | --- |
   |  | se​(θ^j)=[𝐕^​(𝜽^)]j​j,\text{se}(\hat{\theta}\_{j})=\sqrt{[\hat{\mathbf{V}}(\hat{\boldsymbol{\theta}})]\_{jj}}\,, |  |

   with corresponding zz-statistics

   |  |  |  |
   | --- | --- | --- |
   |  | zj=θ^j/se​(θ^j).z\_{j}=\hat{\theta}\_{j}/\text{se}(\hat{\theta}\_{j}). |  |

   Under standard regularity conditions, 𝜽^j\widehat{\boldsymbol{\theta}}\_{j} is asymptotically standard normal, so that two-sided pp-values can be computed as

   |  |  |  |
   | --- | --- | --- |
   |  | p​-valuej=2​[1−Φ​(|zj|)],p\text{-value}\_{j}=2[1-\Phi(|z\_{j}|)]\,, |  |

   where Φ​(⋅)\Phi(\cdot) denotes the standard normal cumulative distribution function.
7. 7.

   Residual diagnostics.
   Model adequacy is evaluated using the zero-mean residuals u^t=ε^t−1\widehat{u}\_{t}=\hat{\varepsilon}\_{t}-1. The Ljung–Box test (Ljung and Box, [1978](https://arxiv.org/html/2602.19732v1#bib.bib55 "On a measure of lack of fit in time series models")) is applied to both u^t\widehat{u}\_{t} and u^t2\widehat{u}\_{t}^{2} (typically with 5 lags) to detect serial correlation and conditional heteroskedasticity. In addition, Engle’s ARCH test (Engle, [1982](https://arxiv.org/html/2602.19732v1#bib.bib34 "Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation")) with 5 lags provides another check for residual heteroskedasticity.

### 7.3 The Forecasting Setup

Following the standard approach in volatility forecasting, we perform out-of-sample evaluation by comparing one-step ahead forecasts to the "true" realized measure (Hansen and Lunde, [2005](https://arxiv.org/html/2602.19732v1#bib.bib48 "A forecast comparison of volatility models: does anything beat a GARCH(1,1)?"); Patton, [2011](https://arxiv.org/html/2602.19732v1#bib.bib63 "Volatility forecast comparison using imperfect volatility proxies"); Bollerslev et al., [2016](https://arxiv.org/html/2602.19732v1#bib.bib24 "Exploiting the errors: a simple approach for improved volatility forecasting"); Cipollini et al., [2021](https://arxiv.org/html/2602.19732v1#bib.bib28 "Realized volatility forecasting: robustness to measurement errors"))

The sample is split into two parts: an estimation (in-sample) period, from the beginning of the series up to a time TT, and a forecasting (out-of-sample) period of length HH, covering observations t=T+1,…,T+Ht=T+1,\ldots,T+H. Model parameters 𝜽^\hat{\boldsymbol{\theta}} are estimated once using only the in-sample data and are kept fixed throughout the forecasting exercise. One-step-ahead forecasts are then generated sequentially, conditioning on the information set available at time t−1t-1.

##### Forecast uncertainty.

Prediction intervals are constructed using a non-parametric approach based on the empirical distribution of in-sample residuals.

For HAR models, residuals are defined as forecast errors
e^t=yt−y^t\hat{e}\_{t}=y\_{t}-\hat{y}\_{t}.
The 95% confidence interval is obtained by adding the empirical quantiles of e^t\hat{e}\_{t} to the point forecast:

|  |  |  |
| --- | --- | --- |
|  | C​I95%​(yt|t−1)=[y^t|t−1+q0.025​(e^),y^t|t−1+q0.975​(e^)],CI\_{95\%}(y\_{t|t-1})=\left[\hat{y}\_{t|t-1}+q\_{0.025}(\hat{e}),\;\hat{y}\_{t|t-1}+q\_{0.975}(\hat{e})\right], |  |

where yt|t−1y\_{t|t-1} represents the forecasted value at time tt, conditional on the information available at time t−1t-1,
with the lower bound possibly truncated at zero to preserve non-negativity.

For MEM specifications, residuals are given by the multiplicative innovations
ε^t=yt/μ^t\hat{\varepsilon}\_{t}=y\_{t}/\hat{\mu}\_{t}.
The 95% confidence interval is then obtained by scaling the point forecast with the empirical quantiles of ε^t\hat{\varepsilon}\_{t}:

|  |  |  |
| --- | --- | --- |
|  | C​I95%​(yt|t−1)=[μ^t|t−1⋅q0.025​(ε^),μ^t|t−1⋅q0.975​(ε^)].CI\_{95\%}(y\_{t|t-1})=\left[\hat{\mu}\_{t|t-1}\cdot q\_{0.025}(\hat{\varepsilon}),\;\hat{\mu}\_{t|t-1}\cdot q\_{0.975}(\hat{\varepsilon})\right]. |  |

##### Forecast evaluation.

Predictive accuracy is assessed using two standard loss functions, the Mean Squared Error (MSE) and the Quasi-Likelihood (QLIKE), both consistent à la Patton ([2011](https://arxiv.org/html/2602.19732v1#bib.bib63 "Volatility forecast comparison using imperfect volatility proxies")), computed over HH out-of-sample horizon

|  |  |  |
| --- | --- | --- |
|  | M​S​E=1H​∑t=T+1T+H(yt−y^t|t−1)2,MSE=\frac{1}{H}\sum\_{t=T+1}^{T+H}\left(y\_{t}-\hat{y}\_{t|t-1}\right)^{2}, |  |

|  |  |  |
| --- | --- | --- |
|  | Q​L​I​K​E=1H​∑t=T+1T+H(yty^t|t−1−log⁡(yty^t|t−1)−1).QLIKE=\frac{1}{H}\sum\_{t=T+1}^{T+H}\left(\frac{y\_{t}}{\hat{y}\_{t|t-1}}-\log\left(\frac{y\_{t}}{\hat{y}\_{t|t-1}}\right)-1\right). |  |

## 8 Concluding Remarks

VOLARE was conceived and implemented as a research infrastructure designed to restore and extend open access to high-quality realized volatility and covariance measures in financial econometrics. In a context where ultra-high-frequency (UHF) data are costly, computationally demanding, and methodologically delicate to process, VOLARE provides a transparent, reproducible, and academically rigorous pipeline transforming raw tick-level
observations into validated daily realized measures across multiple asset classes.

The fundamental contribution of the initiative lies in three interconnected dimensions.

First, at the methodological level, VOLARE operationalizes state-of-the-art econometric procedures within a coherent and fully documented framework. The
implementation of the cleaning algorithm for stock data and the computation of a comprehensive set of realized measures ensure that the resulting series are not merely
convenient datasets, but carefully engineered research objects. The platform transforms millions of unevenly spaced tick observations into regularly sampled, microstructure-aware volatility measures suitable for econometric modelling and forecasting.

Second, at the infrastructure level, VOLARE integrates a robust back-end pipeline, covering data acquisition, cleaning, computation, and storage, with a web-based front-end designed for research usability. This dual access structure, full dataset extraction on the one hand, and real-time visualization and model estimation on the other, lowers the entry barrier to high-frequency volatility research while preserving methodological transparency.

Third, at the scientific ecosystem level, VOLARE was designed as a public good. By making daily realized variances and covariances available for a representative set of equities, exchange rates, and futures contracts, the platform facilitates replication,
comparative evaluation of models, and methodological innovation. In addition, by embedding real-time estimation of HAR- and MEM-type volatility models, VOLARE provides a unified environment where measurement and modelling coexist. This integration shortens the distance between raw data, econometric specification, diagnostic evaluation, and forecasting, encouraging experimentation and pedagogical use.

Beyond its current configuration, VOLARE is intrinsically expandable. The modular structure of the back-end allows for additional assets, and sampling frequencies; new realized measures can be incorporated with limited friction. Similarly, the modeling layer can be enriched with multivariate frameworks,
nonlinear specifications, or machine-learning-based volatility predictors.

## Acknowledgments

This work was carried out as part of the ForVARD project (part of the project GRINS - Growing Resilient, INclusive and Sustainable; grant GRINS PE00000018) funded by the European Union - Next Generation EU. However, the views and opinions expressed are solely those of the authors and do not necessarily reflect those of the European Union or the European Commission. Neither the European Union nor the European Commission can be held responsible for them. Without implicating, we are grateful to Demetrio Lacava and Luca Scaffidi Domianello, for useful suggestions on this paper. We also thank participants in the Conferences 2nd Workshop on Sustainable Finance – Spoke 4 GRINS held in Venice, on December 2–3, 2024, Intermediate workshop of the ForVARD – Forecasting Volatility and Risk Dynamics project held in Messina, on March 11, 2025, New Perspectives in Mathematical and Statistical Methods for Actuarial Sciences and Finance, Waiting for MAF held in Salerno, on June 27-28, 2025, Methodological
and Computational Challenges in Large-Scale Time Series Models for Economics and Finance, held in Frascati on September 11–12, 2025, End of the PRIN 2022 Project: What’s Next? Insights, Ideas, and Future Collaborations, held in Messina on January 12, 2026, and Volatility and Liquidity Workshop, held in Pavia on January 22-23, 2026.

## References

* T. G. Andersen, T. Bollerslev, F. X. Diebold, and P. Labys (2003)
  Modeling and forecasting realized volatility.
  Econometrica 71 (2),  pp. 579–625.
  External Links: [Document](https://dx.doi.org/10.1111/1468-0262.00418)
  Cited by: [§1](https://arxiv.org/html/2602.19732v1#S1.p3.1 "1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§5.1.4](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS4.p1.4 "5.1.4 Realized Variance (rv) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.7.6.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* T. G. Andersen and T. Bollerslev (1998)
  Answering the skeptics: yes, standard volatility models do provide accurate forecasts.
  International Economic Review 39 (4),  pp. 885–905.
  External Links: ISSN 00206598, 14682354,
  [Document](https://dx.doi.org/10.2307/2527343)
  Cited by: [§1](https://arxiv.org/html/2602.19732v1#S1.p3.1 "1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§5.1.4](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS4.p1.4 "5.1.4 Realized Variance (rv) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.6.5.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7](https://arxiv.org/html/2602.19732v1#S7.p1.1 "7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* T. G. Andersen, D. Dobrev, and E. Schaumburg (2012)
  Jump-robust volatility estimation using nearest neighbor truncation.
  Journal of Econometrics 169 (1),  pp. 75–93.
  Note: Recent Advances in Panel Data, Nonlinear and Nonparametric Models: A Festschrift in Honor of Peter C.B. Phillips
  External Links: ISSN 0304-4076,
  [Document](https://dx.doi.org/10.1016/j.jeconom.2012.01.011)
  Cited by: [§5.1.8](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS8.p1.4 "5.1.8 Median Realized Variance (medrv) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§5.1.9](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS9.p1.3 "5.1.9 Minimum Realized Variance (minrv) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.11.10.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.12.11.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* F. M. Bandi and J. R. Russell (2008)
  Microstructure noise, realized variance, and optimal sampling.
  The Review of Economic Studies 75 (2),  pp. 339–369.
  Cited by: [§4.4](https://arxiv.org/html/2602.19732v1#S4.SS4.p1.1 "4.4 From Tick Data to Regular Intervals ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§5.1.10](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS10.Px1.p1.2 "Noise variance. ‣ 5.1.10 Realized Kernel (rk) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* O. E. Barndorff-Nielsen, P. R. Hansen, A. Lunde, and N. Shephard (2009)
  Realized kernels in practice: trades and quotes.
  The Econometrics Journal 12 (3),  pp. C1–C32.
  External Links: ISSN 13684221, 1368423X,
  [Document](https://dx.doi.org/10.1111/j.1368-423X.2008.00275.x)
  Cited by: [1st item](https://arxiv.org/html/2602.19732v1#S1.I1.i1.p1.1 "In 1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§4.3](https://arxiv.org/html/2602.19732v1#S4.SS3.p3.1 "4.3 Data Cleaning Procedure for High-Frequency Prices ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§4.4](https://arxiv.org/html/2602.19732v1#S4.SS4.p1.1 "4.4 From Tick Data to Regular Intervals ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§5.1.10](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS10.Px1.p1.2 "Noise variance. ‣ 5.1.10 Realized Kernel (rk) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§5.1.10](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS10.Px2.p1.6 "Integrated variance. ‣ 5.1.10 Realized Kernel (rk) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§5.1.10](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS10.Px3.p1.1 "End effect. ‣ 5.1.10 Realized Kernel (rk) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§5.1.10](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS10.p1.1 "5.1.10 Realized Kernel (rk) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.13.12.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [footnote 12](https://arxiv.org/html/2602.19732v1#footnote12 "In 5.1.10 Realized Kernel (rk) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [footnote 14](https://arxiv.org/html/2602.19732v1#footnote14 "In 5.1.10 Realized Kernel (rk) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* O. E. Barndorff-Nielsen, P. R. Hansen, A. Lunde, and N. Shephard (2011)
  Multivariate realised kernels: consistent positive semi-definite estimators of the covariation of equity prices with noise and non-synchronous trading.
  Journal of Econometrics 162 (2),  pp. 149–169.
  External Links: [Document](https://dx.doi.org/10.1016/j.jeconom.2010.07.009)
  Cited by: [§5.2](https://arxiv.org/html/2602.19732v1#S5.SS2.p1.1 "5.2 Multivariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* O. E. Barndorff-Nielsen and N. Shephard (2002)
  Econometric analysis of realized volatility and its use in estimating stochastic volatility models.
  Journal of the Royal Statistical Society Series B: Statistical Methodology 64 (2),  pp. 253–280.
  Cited by: [§5.1.5](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS5.p1.4 "5.1.5 Realized Quarticity (rq) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.8.7.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* O. E. Barndorff-Nielsen and N. Shephard (2004a)
  Measuring the impact of jumps in multivariate price processes using bipower covariation.
  Technical report
   Discussion paper, Nuffield College, Oxford University.
  Cited by: [§5.2.2](https://arxiv.org/html/2602.19732v1#S5.SS2.SSS2.p1.2 "5.2.2 Realized Bipower Covariance (rbpcov) ‣ 5.2 Multivariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 13](https://arxiv.org/html/2602.19732v1#S5.T13.1.1.3.2.2 "In 5.2 Multivariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* O. E. Barndorff-Nielsen, P. R. Hansen, A. Lunde, and N. Shephard (2008)
  Designing realized kernels to measure the ex post variation of equity prices in the presence of noise.
  Econometrica 76 (6),  pp. 1481–1536.
  External Links: [Document](https://dx.doi.org/10.3982/ECTA6495)
  Cited by: [§1](https://arxiv.org/html/2602.19732v1#S1.p4.1 "1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§5.1.10](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS10.p1.1 "5.1.10 Realized Kernel (rk) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* O. E. Barndorff-Nielsen and N. Shephard (2004b)
  Econometric analysis of realized covariation: high frequency based covariance, regression, and correlation in financial economics.
  Econometrica 72 (3),  pp. 885–925.
  External Links: ISSN 00129682, 14680262
  Cited by: [§5.2.1](https://arxiv.org/html/2602.19732v1#S5.SS2.SSS1.p1.2 "5.2.1 Realized Covariance (rcov) ‣ 5.2 Multivariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 13](https://arxiv.org/html/2602.19732v1#S5.T13.1.1.2.1.2 "In 5.2 Multivariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* O. E. Barndorff-Nielsen and N. Shephard (2004c)
  Power and bipower variation with stochastic volatility and jumps.
  Journal of Financial Econometrics 2 (1),  pp. 1–37.
  External Links: ISSN 1479-8409,
  [Document](https://dx.doi.org/10.1093/jjfinec/nbh001)
  Cited by: [§5.1.6](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS6.p1.1 "5.1.6 Bipower Variation (bv) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.9.8.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* O. E. Barndorff‐Nielsen, S. Kinnebrock, and N. Shephard (2010)
  Measuring downside risk – realized semivariance.
  In Volatility and Time Series Econometrics: Essays in Honor of Robert Engle,
  External Links: ISBN 9780199549498,
  [Document](https://dx.doi.org/10.1093/acprof%3Aoso/9780199549498.003.0007)
  Cited by: [§1](https://arxiv.org/html/2602.19732v1#S1.p4.1 "1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§5.1.7](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS7.p1.2 "5.1.7 Realized Semivariances (rsp, rsn) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.10.9.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* R. P. Bartlett, J. McCrary, and M. O’Hara (2023)
  The market inside the market: odd-lot quotes.
  The Review of Financial Studies 38 (3),  pp. 661–711.
  External Links: ISSN 0893-9454,
  [Document](https://dx.doi.org/10.1093/rfs/hhad074)
  Cited by: [§3](https://arxiv.org/html/2602.19732v1#S3.p3.1 "3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* T. Bollerslev, J. Li, A. J. Patton, and R. Quaedvlieg (2020)
  Realized semicovariances.
  Econometrica 88 (4),  pp. 1515–1551.
  External Links: [Document](https://dx.doi.org/10.3982/ECTA17056)
  Cited by: [§5.2.3](https://arxiv.org/html/2602.19732v1#S5.SS2.SSS3.p2.3 "5.2.3 Realized Semicovariances (rscov) ‣ 5.2 Multivariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 13](https://arxiv.org/html/2602.19732v1#S5.T13.1.1.4.3.2 "In 5.2 Multivariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* T. Bollerslev, A. J. Patton, and R. Quaedvlieg (2016)
  Exploiting the errors: a simple approach for improved volatility forecasting.
  Journal of Econometrics 192 (1),  pp. 1–18.
  External Links: [Document](https://dx.doi.org/10.1016/j.jeconom.2015.10.007)
  Cited by: [2nd item](https://arxiv.org/html/2602.19732v1#S1.I1.i2.p1.1 "In 1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7.1.2](https://arxiv.org/html/2602.19732v1#S7.SS1.SSS2.p1.3 "7.1.2 HAR-Q ‣ 7.1 Heterogeneous Autoregressive Models ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7.3](https://arxiv.org/html/2602.19732v1#S7.SS3.p1.1 "7.3 The Forecasting Setup ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7](https://arxiv.org/html/2602.19732v1#S7.p1.1 "7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* T. Bollerslev (1986)
  Generalized autoregressive conditional heteroskedasticity.
  Journal of Econometrics 31 (3),  pp. 307–327.
  External Links: ISSN 0304-4076,
  [Document](https://dx.doi.org/10.1016/0304-4076%2886%2990063-1)
  Cited by: [§1](https://arxiv.org/html/2602.19732v1#S1.p1.1 "1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* C.T. Brownlees and G.M. Gallo (2006)
  Financial econometric analysis at ultra-high frequency: data handling concerns.
  Computational Statistics & Data Analysis 51 (4),  pp. 2232–2245.
  External Links: ISSN 0167-9473,
  [Document](https://dx.doi.org/10.1016/j.csda.2006.09.030)
  Cited by: [1st item](https://arxiv.org/html/2602.19732v1#S1.I1.i1.p1.1 "In 1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§4.1](https://arxiv.org/html/2602.19732v1#S4.SS1.SSS0.Px1.p1.1 "Stocks ‣ 4.1 Asset Classes ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§4.3](https://arxiv.org/html/2602.19732v1#S4.SS3.p3.1 "4.3 Data Cleaning Procedure for High-Frequency Prices ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§4.3](https://arxiv.org/html/2602.19732v1#S4.SS3.p4.1 "4.3 Data Cleaning Procedure for High-Frequency Prices ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§4.3](https://arxiv.org/html/2602.19732v1#S4.SS3.p7.6 "4.3 Data Cleaning Procedure for High-Frequency Prices ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 11](https://arxiv.org/html/2602.19732v1#S4.T11 "In 4.3 Data Cleaning Procedure for High-Frequency Prices ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [footnote 5](https://arxiv.org/html/2602.19732v1#footnote5 "In 2 The Raw Data from Kibot ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* C. T. Brownlees, F. Cipollini, and G. M. Gallo (2012)
  Multiplicative Error Models.
  In Volatility Models and Their Applications,
   pp. 223–247.
  External Links: ISBN 9781118272039,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1002/9781118272039.ch9)
  Cited by: [item 6](https://arxiv.org/html/2602.19732v1#S7.I5.i6.p1.5 "In 7.2.3 Parameter Estimation Procedure ‣ 7.2 The Multiplicative Error Models (MEM) ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* K. Christensen and M. Podolskij (2007)
  Realized range-based estimation of integrated variance.
  Journal of Econometrics 141 (2),  pp. 323–349.
  External Links: ISSN 0304-4076,
  [Document](https://dx.doi.org/10.1016/j.jeconom.2006.06.012)
  Cited by: [§5.1.3](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS3.p1.5 "5.1.3 Realized Range (rr) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.5.4.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* F. Cipollini, G. M. Gallo, and E. Otranto (2021)
  Realized volatility forecasting: robustness to measurement errors.
  International Journal of Forecasting 37 (1),  pp. 44–57.
  External Links: [Document](https://dx.doi.org/10.1016/j.ijforecast.2020.02.009)
  Cited by: [§7.2.2](https://arxiv.org/html/2602.19732v1#S7.SS2.SSS2.p1.1 "7.2.2 Asymmetric MEM (AMEM) ‣ 7.2 The Multiplicative Error Models (MEM) ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7.3](https://arxiv.org/html/2602.19732v1#S7.SS3.p1.1 "7.3 The Forecasting Setup ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* F. Cipollini and G. M. Gallo (2025)
  Multiplicative Error Models: 20 years on.
  Econometrics and Statistics 33,  pp. 209–229.
  External Links: ISSN 2452-3062,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.ecosta.2022.05.005)
  Cited by: [§7](https://arxiv.org/html/2602.19732v1#S7.p1.1 "7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* F. Corsi (2009)
  A simple approximate long-memory model of realized volatility.
  Journal of Financial Econometrics 7 (2),  pp. 174–196.
  Cited by: [2nd item](https://arxiv.org/html/2602.19732v1#S1.I1.i2.p1.1 "In 1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7.1.1](https://arxiv.org/html/2602.19732v1#S7.SS1.SSS1.p1.7 "7.1.1 HAR ‣ 7.1 Heterogeneous Autoregressive Models ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7](https://arxiv.org/html/2602.19732v1#S7.p2.1 "7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* R. F. Engle and G. M. Gallo (2006)
  A multiple indicators model for volatility using intra-daily data.
  Journal of econometrics 131 (1-2),  pp. 3–27.
  Cited by: [2nd item](https://arxiv.org/html/2602.19732v1#S1.I1.i2.p1.1 "In 1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7.2.2](https://arxiv.org/html/2602.19732v1#S7.SS2.SSS2.p1.1 "7.2.2 Asymmetric MEM (AMEM) ‣ 7.2 The Multiplicative Error Models (MEM) ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7.2](https://arxiv.org/html/2602.19732v1#S7.SS2.p1.6 "7.2 The Multiplicative Error Models (MEM) ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7](https://arxiv.org/html/2602.19732v1#S7.p2.1 "7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* R. F. Engle (1982)
  Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation.
  Econometrica 50 (4),  pp. 987–1007.
  External Links: ISSN 00129682, 14680262
  Cited by: [§1](https://arxiv.org/html/2602.19732v1#S1.p1.1 "1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [item 3](https://arxiv.org/html/2602.19732v1#S7.I1.i3.p1.1 "In 7.1.3 Parameter Estimation Procedure ‣ 7.1 Heterogeneous Autoregressive Models ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [item 7](https://arxiv.org/html/2602.19732v1#S7.I5.i7.p1.3 "In 7.2.3 Parameter Estimation Procedure ‣ 7.2 The Multiplicative Error Models (MEM) ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* R. F. Engle (2002)
  New frontiers for ARCH models.
  Journal of Applied Econometrics 17,  pp. 425–446.
  Cited by: [2nd item](https://arxiv.org/html/2602.19732v1#S1.I1.i2.p1.1 "In 1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7.2](https://arxiv.org/html/2602.19732v1#S7.SS2.p1.6 "7.2 The Multiplicative Error Models (MEM) ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7](https://arxiv.org/html/2602.19732v1#S7.p2.1 "7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* R. F. Engle (2000)
  The econometrics of ultra-high-frequency data.
  Econometrica 68 (1),  pp. 1–22.
  Cited by: [§1](https://arxiv.org/html/2602.19732v1#S1.p2.1 "1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* M. B. Garman and M. J. Klass (1980)
  On the estimation of security price volatilities from historical data.
  Journal of business,  pp. 67–78.
  External Links: [Link](http://www.jstor.org/stable/2352358)
  Cited by: [§5.1.2](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS2.p1.1 "5.1.2 Garman-Klass Range (gkr) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.3.2.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* R. Gençay, M. Dacorogna, U. A. Muller, O. Pictet, and R. Olsen (2001)
  An introduction to high-frequency finance.
   Elsevier.
  Cited by: [§4.4](https://arxiv.org/html/2602.19732v1#S4.SS4.p1.1 "4.4 From Tick Data to Regular Intervals ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* P. R. Hansen and A. Lunde (2005)
  A forecast comparison of volatility models: does anything beat a GARCH(1,1)?.
  Journal of Applied Econometrics 20 (7),  pp. 873–889.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1002/jae.800)
  Cited by: [§7.3](https://arxiv.org/html/2602.19732v1#S7.SS3.p1.1 "7.3 The Forecasting Setup ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7](https://arxiv.org/html/2602.19732v1#S7.p1.1 "7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* P. R. Hansen and A. Lunde (2006)
  Realized variance and market microstructure noise.
  Journal of Business & Economic Statistics 24 (2),  pp. 127–161.
  External Links: [Document](https://dx.doi.org/10.1198/073500106000000071)
  Cited by: [§4.4](https://arxiv.org/html/2602.19732v1#S4.SS4.p1.1 "4.4 From Tick Data to Regular Intervals ‣ 4 The VOLARE Back-end: Data Preparation ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* G. Heber, A. Lunde, N. Shephard, and K. Sheppard (2009)
  Oxford-Man Institute’s realized library.
  Version 0.1, Oxford-Man Institute, University of Oxford.
  Cited by: [§1](https://arxiv.org/html/2602.19732v1#S1.p5.1 "1 Introduction ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* H. Johnson (2014)
  Odd lot trades: the behavior, characteristics, and information content, over time.
  Financial Review 49 (4),  pp. 669–684.
  External Links: [Document](https://dx.doi.org/10.1111/fire.12052)
  Cited by: [§3](https://arxiv.org/html/2602.19732v1#S3.p3.1 "3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* G. M. Ljung and G. E. P. Box (1978)
  On a measure of lack of fit in time series models.
  Biometrika 65 (2),  pp. 297–303.
  External Links: ISSN 0006-3444,
  [Document](https://dx.doi.org/10.1093/biomet/65.2.297)
  Cited by: [item 3](https://arxiv.org/html/2602.19732v1#S7.I1.i3.p1.1 "In 7.1.3 Parameter Estimation Procedure ‣ 7.1 Heterogeneous Autoregressive Models ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [item 7](https://arxiv.org/html/2602.19732v1#S7.I5.i7.p1.3 "In 7.2.3 Parameter Estimation Procedure ‣ 7.2 The Multiplicative Error Models (MEM) ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* M. Martens and D. Van Dijk (2007)
  Measuring volatility with the realized range.
  Journal of Econometrics 138 (1),  pp. 181–207.
  External Links: [Document](https://dx.doi.org/10.1016/j.jeconom.2006.05.019)
  Cited by: [§5.1.3](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS3.p1.5 "5.1.3 Realized Range (rr) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.4.3.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* W. K. Newey and K. D. West (1987)
  A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix.
  Econometrica 55 (3),  pp. 703–708.
  Cited by: [item 2](https://arxiv.org/html/2602.19732v1#S7.I1.i2.p1.2 "In 7.1.3 Parameter Estimation Procedure ‣ 7.1 Heterogeneous Autoregressive Models ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* W. K. Newey and K. D. West (1994)
  Automatic lag selection in covariance matrix estimation.
  The Review of Economic Studies 61 (4),  pp. 631–653.
  External Links: ISSN 00346527, 1467937X
  Cited by: [item 2](https://arxiv.org/html/2602.19732v1#S7.I1.i2.p1.2 "In 7.1.3 Parameter Estimation Procedure ‣ 7.1 Heterogeneous Autoregressive Models ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* M. O’Hara, C. Yao, and M. Ye (2014)
  What’s not there: odd lots and market data.
  The Journal of Finance 69 (5),  pp. 2199–2236.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1111/jofi.12185)
  Cited by: [§3](https://arxiv.org/html/2602.19732v1#S3.p1.1 "3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§3](https://arxiv.org/html/2602.19732v1#S3.p3.1 "3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§3](https://arxiv.org/html/2602.19732v1#S3.p4.1 "3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* M. Parkinson (1980)
  The extreme value method for estimating the variance of the rate of return.
  Journal of business 53,  pp. 61–65.
  External Links: ISSN 00219398, 15375374,
  [Link](http://www.jstor.org/stable/2352357)
  Cited by: [§5.1.1](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS1.p1.1 "5.1.1 Parkinson Range (pr) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [Table 12](https://arxiv.org/html/2602.19732v1#S5.T12.3.1.2.1.2 "In 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* A. J. Patton (2011)
  Volatility forecast comparison using imperfect volatility proxies.
  Journal of Econometrics 160 (1),  pp. 246–256.
  Note: Realized Volatility
  External Links: ISSN 0304-4076,
  [Document](https://dx.doi.org/10.1016/j.jeconom.2010.03.034)
  Cited by: [§7.3](https://arxiv.org/html/2602.19732v1#S7.SS3.SSS0.Px2.p1.1 "Forecast evaluation. ‣ 7.3 The Forecasting Setup ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§7.3](https://arxiv.org/html/2602.19732v1#S7.SS3.p1.1 "7.3 The Forecasting Setup ‣ 7 The VOLARE Front-end: Volatility Models ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* H. Wu (1972)
  Odd-lot trading in the stock market and its market impact.
  The Journal of Financial and Quantitative Analysis 7 (1),  pp. 1321–1341.
  External Links: ISSN 00221090, 17566916,
  [Document](https://dx.doi.org/10.2307/2330066)
  Cited by: [§3](https://arxiv.org/html/2602.19732v1#S3.p3.1 "3 Some Insights on Odd-Lot Trades ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* L. Zhang, P. A. Mykland, and Y. Aït-Sahalia (2005)
  A tale of two time scales: determining integrated volatility with noisy high-frequency data.
  Journal of the American Statistical Association 100 (472),  pp. 1394–1411.
  Cited by: [§5.1.10](https://arxiv.org/html/2602.19732v1#S5.SS1.SSS10.Px1.p1.2 "Noise variance. ‣ 5.1.10 Realized Kernel (rk) ‣ 5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)"),
  [§5.1](https://arxiv.org/html/2602.19732v1#S5.SS1.p4.1 "5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* L. Zhang (2011)
  Estimating covariation: epps effect, microstructure noise.
  Journal of Econometrics 160 (1),  pp. 33–47.
  External Links: [Document](https://dx.doi.org/10.1016/j.jeconom.2010.03.012)
  Cited by: [§5.2](https://arxiv.org/html/2602.19732v1#S5.SS2.p1.1 "5.2 Multivariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").
* B. Zhou (1996)
  High-frequency data and volatility in foreign-exchange rates.
  Journal of Business & Economic Statistics 14 (1),  pp. 45–52.
  External Links: ISSN 07350015,
  [Document](https://dx.doi.org/10.1080/07350015.1996.10524628)
  Cited by: [§5.1](https://arxiv.org/html/2602.19732v1#S5.SS1.p4.1 "5.1 Univariate Series ‣ 5 The VOLARE Back-end: Realized Measures ‣ VOLatility Archive for Realized Estimates (VOLARE)").

## Appendix A Appendix

### A.1 Asset list

| Symbol | Name | Sector | First date |
| --- | --- | --- | --- |
| AAPL \* | Apple Inc. | Information Technology | 2015-01-02 |
| ADBE | Adobe Inc. | Information Technology | 2015-01-02 |
| AMD | Advanced Micro Devices | Information Technology | 2015-01-02 |
| AMGN \* | Amgen Inc. | Health Care | 2015-01-02 |
| AMZN \* | Amazon | Consumer Discretionary | 2015-01-02 |
| AXP \* | American Express | Finance | 2015-01-02 |
| BA \* | Boeing | Industrials | 2015-01-02 |
| CAT \* | Caterpillar Inc. | Industrials | 2015-01-02 |
| CRM \* | Salesforce Inc. | Information Technology | 2015-01-02 |
| CSCO \* | Cisco | Information Technology | 2015-01-02 |
| CVX \* | Chevron Corporation | Energy | 2015-01-02 |
| DIS \* | Walt Disney Company (The) | Communication Services | 2015-01-02 |
| GE | GE Aerospace | Industrials | 2015-01-02 |
| GOOGL | Alphabet Inc. (Class A) | Communication Services | 2015-01-02 |
| GS \* | Goldman Sachs | Finance | 2015-01-02 |
| HD \* | Home Depot | Consumer Discretionary | 2015-01-02 |
| HON \* | Honeywell International Inc. | Industrials | 2015-01-02 |
| IBM \* | IBM | Information Technology | 2015-01-02 |
| JNJ \* | Johnson & Johnson | Health Care | 2015-01-02 |
| JPM \* | JPMorgan Chase | Finance | 2015-01-02 |
| KO \* | Coca-Cola Company (The) | Consumer Staples | 2015-01-02 |
| MCD \* | McDonald’s | Consumer Discretionary | 2015-01-02 |
| META | Meta Platforms | Communication Services | 2015-01-02 |
| MMM \* | 3M | Industrials | 2015-01-02 |
| MRK \* | Merck & Company Inc. | Health Care | 2015-01-02 |
| MSFT \* | Microsoft | Information Technology | 2015-01-02 |
| NFLX | Netflix, Inc. | Communication Services | 2015-01-02 |
| NKE \* | Nike, Inc. | Consumer Discretionary | 2015-01-02 |
| NVDA \* | Nvidia | Information Technology | 2015-01-02 |
| ORCL | Oracle Corporation | Information Technology | 2015-01-02 |
| PG \* | Procter & Gamble | Consumer Staples | 2015-01-02 |
| PM | Philip Morris International | Consumer Staples | 2015-01-02 |
| SHW \* | Sherwin-Williams Company | Consumer Discretionary | 2015-01-02 |
| TRV \* | The Travelers Companies Inc. | Finance | 2015-01-02 |
| TSLA | Tesla, Inc. | Consumer Discretionary | 2015-01-02 |
| UNH \* | Unitedhealth Group Inc. | Health Care | 2015-01-02 |
| V \* | Visa Inc. | Finance | 2015-01-02 |
| VZ \* | Verizon Communications Inc. | Public Utilities | 2015-01-02 |
| WMT \* | Walmart | Consumer Staples | 2015-01-02 |
| XOM | ExxonMobil | Energy | 2015-01-02 |

Table A.1: Stocks Data Availability. It includes the stocks from the Dow 30 (marked with \*) along with ten stocks from the S&P 100.



| Symbol | Name | First date |
| --- | --- | --- |
| AUDUSD | Australian dollar / US dollar | 2009-09-25 |
| EURUSD | Euro / US dollar | 2009-09-25 |
| GBPUSD | British pound / US dollar | 2009-09-25 |
| USDCAD | US dollar / Canadian dollar | 2009-09-25 |
| USDJPY | US dollar / Japanese yen | 2009-09-28 |

Table A.2: Exchange Rates Data Availability



| Symbol | Name | Sector | Exchange | First date |
| --- | --- | --- | --- | --- |
| CL | Crude Oil | Energy | NYMEX | 2009-09-28 |
| NG | Natural Gas | Energy | NYMEX | 2009-09-28 |
| GC | Gold | Metals | COMEX | 2009-09-28 |
| C | Corn | Agricultural | CME | 2009-09-28 |
| ES | E-mini S&P 500 | Equity Index | CME | 2009-09-28 |

Table A.3: Futures Data Availability

### A.2 Volatility Analysis across Assets: A Test Run

In this section, we present the summary statistics and univariate estimation results obtained in different asset classes.

As mentioned earlier, we evaluate five model specifications: HAR, HAR-Q, MEM(1,1), AMEM(1,1), and AMEM(2,1). For this empirical analysis, we rely on a larger dataset, comprising 109 stocks, 13 exchange rates, and 13 futures contracts, a dataset that extends beyond the sample currently displayed in the graphical interface.

The models are estimated using several realized variance (RV) measures, namely rv1, rv5, bv1, bv5, and rk.
The estimates were evaluated using the entire available time series for each asset151515For stocks, the series typically range from 2015-01-02 to 2026-01-30; for exchange rates and futures, from 2009-09-25 to 2026-01-30.
The discussion below focuses primarily on results based on the rv1 measure, followed by a comparison of parameter estimates obtained from the other realized variance measures.

[Tables A.4](https://arxiv.org/html/2602.19732v1#A1.T4 "In A.2 Volatility Analysis across Assets: A Test Run ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)") to [A.6](https://arxiv.org/html/2602.19732v1#A1.T6 "Table A.6 ‣ A.2 Volatility Analysis across Assets: A Test Run ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)") report the cross-sectional summary statistics for the estimated parameters161616Although t-statistics are reported in these tables for consistency with standard practice, inference should be interpreted with caution for the MEM family. Several parameters in the MEM specifications are subject to non-negativity constraints to ensure positive conditional variances: the scale parameter (ω\omega), the ARCH coefficients (αi\alpha\_{i}), and the GARCH coefficients (βi\beta\_{i}). When a parameter is constrained to be non-negative, the standard two-sided significance test (H0:θ=0H\_{0}:\theta=0 vs. H1:θ≠0H\_{1}:\theta\neq 0) is not formally valid, as the parameter space excludes negative values by construction. Under such constraints, the usual asymptotic distribution of the t-statistic no longer holds, and inference based on standard critical values may be misleading. For parameters at or near boundary values, one-sided tests or alternative inference procedures (such as bootstrap methods) would be more appropriate.. Overall, the estimated parameters display the expected signs and magnitudes across all model classes.
For the MEM(1,1), both the α1\alpha\_{1} and the β1\beta\_{1} coefficients vary notably across asset classes. In the equity market, the average α1≈0.51\alpha\_{1}\approx 0.51, is greater than the average β1≈0.39\beta\_{1}\approx 0.39, suggesting that stock volatility is more responsive to lagged volatility. Regarding exchange rates, the average β1≈0.69\beta\_{1}\approx 0.69 is much bigger than the average α1≈0.28\alpha\_{1}\approx 0.28, with remarkably low cross-sectional dispersion, indicating homogeneous volatility dynamics across currency pairs.
The futures market exhibits the highest heterogeneity, with β1\beta\_{1} ranging from 0.35 to 0.81 and α1\alpha\_{1} from 0.16 to 0.59, reflecting the diverse nature of underlying commodities and financial contracts.

The asymmetric extension (AMEM(1,1)) introduces the leverage parameter (γ1\gamma\_{1}), which captures differential responses of volatility to positive and negative shocks. This parameter is generally small and weakly significant across markets: statistically significant in 50% of stocks, but only in 31% of exchange rates and 38% of futures contracts. The stronger asymmetric effect in equities is consistent with the well-documented leverage effect, whereby negative returns tend to increase volatility more than positive returns of the same magnitude, a phenomenon observed across financial markets but particularly pronounced in stock returns.

The AMEM(2,1) model adds a short-term component (α2\alpha\_{2}), which enhances the model’s ability to capture transient volatility spikes and their rapid decay.
This parameter is systematically negative across all markets, with mean values of -0.36 for stocks, -0.24 for exchange rates, and -0.20 for futures, and is significant in 99% , 100%, and 85%, and of cases, respectively. The more pronounced mean-reversion in equities reflects the tendency of stock volatility to exhibit sharper but shorter-lived spikes following market shocks.

For the HAR and HAR-Q models, the daily component (αd\alpha\_{d}) typically dominates the weekly (αw\alpha\_{w}) and monthly (αm\alpha\_{m}) components, reflecting the greater importance of recent volatility in forecasting.
However, the monthly component (αm\alpha\_{m}) frequently lacks statistical significance, particularly in the equity market where only 9% of stocks show significant estimates, compared to 77% for exchange rates and 54% for futures.
The realized quarticity term (αQ\alpha\_{Q}) in the HAR-Q model is typically negative (mean values: -11.3 for stocks, -37.9 for exchange rates, -65.1 for futures), implying that higher realized noise, captured by quarticity measures, tends to reduce conditional volatility forecasts, consistent with the view that elevated measurement error should be discounted in forward-looking estimates.

Model adequacy diagnostics are summarized in [Table A.7](https://arxiv.org/html/2602.19732v1#A1.T7 "Table A.7 ‣ A.2 Volatility Analysis across Assets: A Test Run ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)"), which reports the percentage of assets passing Ljung–Box and ARCH tests. MEM-type models exhibit the highest pass rates, with 85-95% of assets passing the Ljung–Box test on squared standardized residuals (LB2) and ARCH tests across all three markets, confirming substantial absence of residual autocorrelation and conditional heteroskedasticity. By contrast, HAR-type models show comparatively weaker performance, with pass rates of only 19% for stocks, 38% for both exchange rates and futures, giving clues of some misspecification. Notably, the AMEM(2,1) model demonstrates substantial improvement over simpler MEM specifications in capturing residual dynamics, particularly for equities, where the pass rate for the Ljung–Box test on standardized residuals jumps from 6-8% (MEM/AMEM) to 76%, reflecting the model’s enhanced ability to capture short-term volatility fluctuations through the α2\alpha\_{2}
parameter.

The boxplots in [Figures A.2](https://arxiv.org/html/2602.19732v1#A1.F2 "In A.2 Volatility Analysis across Assets: A Test Run ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)") to [A.3](https://arxiv.org/html/2602.19732v1#A1.F3 "Figure A.3 ‣ A.2 Volatility Analysis across Assets: A Test Run ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)"), illustrate the cross-sectional distribution of the estimated parameters for the MEM and HAR model families across the three asset classes, using the same realized variance measure (rv1).
Each boxplot represents the empirical distribution of a given parameter across all assets within an asset class.
The central line corresponds to the sample median, the box spans the interquartile range (IQR, 25th-75th percentiles), and the whiskers extend to the most extreme data points within 1.5 ×\times IQR from the lower and upper quartiles.
Observations outside this range are plotted individually to emphasize values that deviate substantially from the central distribution.
For the MEM-type specifications, the coefficients α1\alpha\_{1} and β1\beta\_{1} are consistently positive and display limited dispersion across assets, confirming the strong and homogeneous persistence of conditional volatility in all markets.
The leverage parameter γ1\gamma\_{1} in the AMEM specification is close to zero in most cases, with slightly higher variability for stocks, suggesting that asymmetry effects are generally mild and more relevant for equity returns.
The additional short-term component α2\alpha\_{2} in the AMEM(2,1) model exhibits the expected negative sign, capturing short-lived mean-reversion dynamics.
Conversely, the HAR and HAR-Q models show the typical heterogeneous-memory structure: the coefficients associated with the daily component (αd\alpha\_{d}) dominate those of the weekly (αw\alpha\_{w}) and monthly (αm\alpha\_{m}) components, and this pattern holds consistently across stock, exchange rates, and futures.
Overall, these parameter distributions indicate that volatility reacts promptly to new information but remains highly persistent over time, with only moderate cross-sectional variation.

Finally, [Figures˜A.7](https://arxiv.org/html/2602.19732v1#A1.F7 "In A.2 Volatility Analysis across Assets: A Test Run ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)"), [A.8](https://arxiv.org/html/2602.19732v1#A1.F8 "Figure A.8 ‣ A.2 Volatility Analysis across Assets: A Test Run ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)") and [A.9](https://arxiv.org/html/2602.19732v1#A1.F9 "Figure A.9 ‣ A.2 Volatility Analysis across Assets: A Test Run ‣ Appendix A Appendix ‣ VOLatility Archive for Realized Estimates (VOLARE)") show the stability of volatility persistence estimates for MEM-type models across different realized variance measures (rv1, rv5, bv1, bv5, rk).
The estimated persistence, computed as α1+β1\alpha\_{1}+\beta\_{1} for MEM(1,1), α1+β1+γ1/2\alpha\_{1}+\beta\_{1}+\gamma\_{1}/2 for AMEM(1,1), and α1+α2+β1+γ1/2\alpha\_{1}+\alpha\_{2}+\beta\_{1}+\gamma\_{1}/2 for AMEM(2,1), remains consistently high across all asset classes and remarkably stable across sampling frequencies and variance estimators.
This robustness is evident in all three markets.
Among stocks, persistence is strong and lies predominantly in the range [0.84,0.98][0.84,0.98], with greater cross-sectional dispersion attributable to idiosyncratic company-specific effects, though the pattern across RV measures remains consistent within each ticker.
In exchange rates, persistence values are tightly clustered in the range [0.95,0.99][0.95,0.99], with minimal dispersion across both currency pairs and RV measures, confirming the highly persistent nature of volatility in currency markets.
Futures contracts exhibit persistence values tightly concentrated near unity across almost all contracts and RV measures, typically falling in the range [0.93,1.00][0.93,1.00], with only a few isolated exceptions that do not alter the overall picture.
These findings confirm that long-memory behavior in volatility is an intrinsic feature of financial time series, largely independent of the sampling interval (1-minute vs. 5-minute returns) or the particular realized-variance estimator used (standard RV vs. jump-robust bipower variation vs. realized kernel), thereby reinforcing the empirical robustness of the MEM-type specifications implemented within the Volare platform.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Stocks | | | | | | | |
| Parameter | N | Mean | Std | Min | Median | Max | Signif.(%) |
| MEM(1,1) | | | | | | | |
| ω\omega | 109 | 2.134 | 0.776 | 0.621 | 2.004 | 4.450 | 100 |
| α1\alpha\_{1} | 109 | 0.516 | 0.056 | 0.370 | 0.519 | 0.648 | 100 |
| β1\beta\_{1} | 109 | 0.392 | 0.069 | 0.228 | 0.390 | 0.580 | 100 |
| AMEM(1,1) | | | | | | | |
| ω\omega | 109 | 2.099 | 0.753 | 0.538 | 1.990 | 4.450 | 100 |
| α1\alpha\_{1} | 109 | 0.497 | 0.056 | 0.335 | 0.502 | 0.636 | 100 |
| β1\beta\_{1} | 109 | 0.402 | 0.069 | 0.247 | 0.399 | 0.598 | 100 |
| γ1\gamma\_{1} | 109 | 0.021 | 0.012 | -0.000 | 0.020 | 0.063 | 50 |
| AMEM(2,1) | | | | | | | |
| ω\omega | 109 | 0.552 | 0.314 | 0.138 | 0.517 | 2.479 | 97 |
| α1\alpha\_{1} | 109 | 0.536 | 0.046 | 0.418 | 0.540 | 0.638 | 100 |
| α2\alpha\_{2} | 109 | -0.360 | 0.083 | -0.551 | -0.365 | -0.106 | 99 |
| β1\beta\_{1} | 109 | 0.792 | 0.069 | 0.572 | 0.798 | 0.924 | 100 |
| γ1\gamma\_{1} | 109 | 0.014 | 0.008 | -0.004 | 0.013 | 0.037 | 52 |
| HAR | | | | | | | |
| ω⋅1000\omega\cdot 1000 | 109 | 0.061 | 0.048 | 0.016 | 0.048 | 0.336 | 96 |
| αd\alpha\_{d} | 109 | 0.410 | 0.169 | 0.065 | 0.426 | 0.853 | 85 |
| αw\alpha\_{w} | 109 | 0.346 | 0.110 | 0.016 | 0.351 | 0.629 | 88 |
| αm\alpha\_{m} | 109 | 0.027 | 0.070 | -0.098 | 0.013 | 0.250 | 9 |
| HAR-Q | | | | | | | |
| ω⋅1000\omega\cdot 1000 | 109 | 0.028 | 0.038 | -0.076 | 0.022 | 0.248 | 33 |
| αd\alpha\_{d} | 109 | 0.717 | 0.157 | 0.305 | 0.710 | 1.167 | 98 |
| αQ\alpha\_{Q} | 109 | -11.289 | 9.762 | -60.027 | -8.125 | 2.968 | 77 |
| αw\alpha\_{w} | 109 | 0.217 | 0.097 | -0.101 | 0.211 | 0.498 | 70 |
| αm\alpha\_{m} | 109 | 0.000 | 0.062 | -0.156 | -0.008 | 0.193 | 11 |

Table A.4: Parameter estimates for volatility models on 109 stocks using rv1 realized variance measure. For each parameter: N is the number of observations, Mean is the average parameter value across assets, Std is the cross-sectional standard deviation, Min/Median/Max are the distribution quantiles, Signif.(%) represents percentage of estimates statistically significant at 5% level.



|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Exchange Rates | | | | | | | |
| Parameter | N | Mean | Std | Min | Median | Max | Signif.(%) |
| MEM(1,1) | | | | | | | |
| ω\omega | 13 | 0.265 | 0.089 | 0.107 | 0.258 | 0.400 | 100 |
| α1\alpha\_{1} | 13 | 0.285 | 0.064 | 0.153 | 0.289 | 0.391 | 100 |
| β1\beta\_{1} | 13 | 0.689 | 0.071 | 0.564 | 0.678 | 0.819 | 100 |
| AMEM(1,1) | | | | | | | |
| ω\omega | 13 | 0.260 | 0.091 | 0.107 | 0.254 | 0.400 | 100 |
| α1\alpha\_{1} | 13 | 0.279 | 0.066 | 0.153 | 0.285 | 0.385 | 100 |
| β1\beta\_{1} | 13 | 0.691 | 0.071 | 0.566 | 0.678 | 0.826 | 100 |
| γ1\gamma\_{1} | 13 | 0.008 | 0.010 | -0.000 | 0.003 | 0.030 | 31 |
| AMEM(2,1) | | | | | | | |
| ω\omega | 13 | 0.093 | 0.040 | 0.020 | 0.086 | 0.179 | 85 |
| α1\alpha\_{1} | 13 | 0.388 | 0.074 | 0.232 | 0.405 | 0.478 | 100 |
| α2\alpha\_{2} | 13 | -0.245 | 0.066 | -0.337 | -0.253 | -0.115 | 100 |
| β1\beta\_{1} | 13 | 0.849 | 0.022 | 0.812 | 0.846 | 0.879 | 100 |
| γ1\gamma\_{1} | 13 | -0.002 | 0.014 | -0.022 | 0.000 | 0.022 | 62 |
| HAR | | | | | | | |
| ω⋅1000\omega\cdot 1000 | 13 | 0.013 | 0.011 | 0.002 | 0.009 | 0.044 | 100 |
| αd\alpha\_{d} | 13 | 0.328 | 0.180 | 0.067 | 0.371 | 0.612 | 92 |
| αw\alpha\_{w} | 13 | 0.244 | 0.072 | 0.122 | 0.241 | 0.348 | 92 |
| αm\alpha\_{m} | 13 | 0.178 | 0.092 | 0.011 | 0.176 | 0.337 | 77 |
| HAR-Q | | | | | | | |
| ω⋅1000\omega\cdot 1000 | 13 | 0.010 | 0.009 | 0.002 | 0.007 | 0.033 | 85 |
| αd\alpha\_{d} | 13 | 0.495 | 0.157 | 0.127 | 0.519 | 0.705 | 100 |
| αQ\alpha\_{Q} | 13 | -37.993 | 43.502 | -132.750 | -21.437 | -0.199 | 62 |
| αw\alpha\_{w} | 13 | 0.190 | 0.081 | 0.038 | 0.207 | 0.311 | 92 |
| αm\alpha\_{m} | 13 | 0.140 | 0.089 | -0.007 | 0.141 | 0.296 | 69 |

Table A.5: Parameter estimates for volatility models on 13 exchange rates using rv1 realized variance measure. For each parameter: N is the number of observations, Mean is the average parameter value across assets, Std is the cross-sectional standard deviation, Min/Median/Max are the distribution quantiles, Signif.(%) represents percentage of estimates statistically significant at 5% level.



|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Futures | | | | | | | |
| Parameter | N | Mean | Std | Min | Median | Max | Signif.(%) |
| MEM(1,1) | | | | | | | |
| ω\omega | 13 | 0.590 | 0.402 | 0.075 | 0.570 | 1.232 | 77 |
| α1\alpha\_{1} | 13 | 0.348 | 0.157 | 0.160 | 0.285 | 0.587 | 100 |
| β1\beta\_{1} | 13 | 0.622 | 0.170 | 0.347 | 0.675 | 0.812 | 100 |
| AMEM(1,1) | | | | | | | |
| ω\omega | 13 | 0.584 | 0.394 | 0.075 | 0.570 | 1.232 | 77 |
| α1\alpha\_{1} | 13 | 0.319 | 0.125 | 0.160 | 0.285 | 0.554 | 100 |
| β1\beta\_{1} | 13 | 0.639 | 0.147 | 0.404 | 0.675 | 0.812 | 100 |
| γ1\gamma\_{1} | 13 | 0.026 | 0.040 | -0.000 | 0.006 | 0.113 | 38 |
| AMEM(2,1) | | | | | | | |
| ω\omega | 13 | 0.297 | 0.199 | 0.021 | 0.329 | 0.640 | 77 |
| α1\alpha\_{1} | 13 | 0.394 | 0.107 | 0.221 | 0.381 | 0.575 | 100 |
| β1\beta\_{1} | 13 | 0.785 | 0.102 | 0.582 | 0.841 | 0.886 | 100 |
| α2\alpha\_{2} | 13 | -0.202 | 0.078 | -0.334 | -0.221 | -0.090 | 85 |
| γ1\gamma\_{1} | 13 | 0.017 | 0.034 | -0.010 | 0.007 | 0.090 | 46 |
| HAR | | | | | | | |
| ω⋅1000\omega\cdot 1000 | 13 | 0.116 | 0.144 | 0.001 | 0.068 | 0.451 | 77 |
| αd\alpha\_{d} | 13 | 0.284 | 0.230 | -0.000 | 0.285 | 0.649 | 85 |
| αw\alpha\_{w} | 13 | 0.234 | 0.119 | -0.001 | 0.247 | 0.398 | 85 |
| αm\alpha\_{m} | 13 | 0.156 | 0.163 | -0.031 | 0.121 | 0.523 | 54 |
| HAR-Q | | | | | | | |
| ω⋅1000\omega\cdot 1000 | 13 | 0.090 | 0.119 | 0.001 | 0.056 | 0.406 | 54 |
| αd\alpha\_{d} | 13 | 0.525 | 0.259 | 0.175 | 0.510 | 1.046 | 92 |
| αQ\alpha\_{Q} | 13 | -65.043 | 132.183 | -422.905 | -2.878 | -0.017 | 69 |
| αw\alpha\_{w} | 13 | 0.177 | 0.094 | -0.001 | 0.188 | 0.348 | 85 |
| αm\alpha\_{m} | 13 | 0.126 | 0.144 | -0.037 | 0.083 | 0.436 | 54 |

Table A.6: Parameter estimates for volatility models on 13 futures using rv1 realized variance measure. For each parameter: N is the number of observations, Mean is the average parameter value across assets, Std is the cross-sectional standard deviation, Min/Median/Max are the distribution quantiles, Signif.(%) represents percentage of estimates statistically significant at 5% level.



| Stocks | | | | |
| --- | --- | --- | --- | --- |
| Model | N | LB Test | LB2 Test | ARCH Test |
| MEM(1,1) | 109 | 8% | 95% | 95% |
| AMEM(1,1) | 109 | 6% | 96% | 96% |
| AMEM(2,1) | 109 | 76% | 94% | 94% |
| HAR | 109 | 10% | 19% | 19% |
| HAR-Q | 109 | 14% | 35% | 35% |
| Exchange Rates | | | | |
| Model | N | LB Test | LB2 Test | ARCH Test |
| MEM(1,1) | 13 | 0% | 85% | 85% |
| AMEM(1,1) | 13 | 0% | 85% | 85% |
| AMEM(2,1) | 13 | 8% | 85% | 85% |
| HAR | 13 | 77% | 38% | 38% |
| HAR-Q | 13 | 38% | 46% | 46% |
| Futures | | | | |
| Model | N | LB Test | LB2 Test | ARCH Test |
| MEM(1,1) | 13 | 23% | 92% | 92% |
| AMEM(1,1) | 13 | 23% | 92% | 92% |
| AMEM(2,1) | 13 | 54% | 92% | 92% |
| HAR | 13 | 38% | 38% | 38% |
| HAR-Q | 13 | 38% | 38% | 38% |

Table A.7: Percentage of assets passing diagnostic tests for model adequacy (rv1 measure). Ljung-Box test for autocorrelation in standardized residuals (LB Test); Test Ljung-Box test for autocorrelation in squared standardized residuals (LB2 test); ARCH test for remaining conditional heteroskedasticity. Pass rates indicate the percentage of assets where the null hypothesis (no misspecification) is not rejected at 5% significance level.

![Refer to caption](VOLARE_figure/stocks_fig1a_boxplots_MEM.png)


Figure A.1: Distribution of parameter estimates for MEM family models across 109 stocks using rv1 measure. Boxes display the interquartile range (IQR) with median line; whiskers extend to
±1.5×\pm 1.5\timesIQR; observations beyond this range shown as circles.

![Refer to caption](VOLARE_figure/stocks_fig1b_boxplots_HAR.png)


Figure A.2: Distribution of parameter estimates for HAR family models across 109 stocks using rv1 measure. Boxes display the interquartile range (IQR) with median line; whiskers extend to
±1.5×\pm 1.5\timesIQR; observations beyond this range shown as circles.

![Refer to caption](VOLARE_figure/forex_fig1a_boxplots_MEM.png)


Figure A.3: Distribution of parameter estimates for MEM family models across 13 exchange rates using rv1 measure. Boxes display the interquartile range (IQR) with median line; whiskers extend to
±1.5×\pm 1.5\timesIQR; observations beyond this range shown as circles.

![Refer to caption](VOLARE_figure/forex_fig1b_boxplots_HAR.png)


Figure A.4: Distribution of parameter estimates for HAR family models across 13 exchange rates using rv1 measure. Boxes display the interquartile range (IQR) with median line; whiskers extend to
±1.5×\pm 1.5\timesIQR; observations beyond this range shown as circles.

![Refer to caption](VOLARE_figure/futures_fig1a_boxplots_MEM.png)


Figure A.5: Distribution of parameter estimates for MEM family models across 13 futures using rv1 measure. Boxes display the interquartile range (IQR) with median line; whiskers extend to
±1.5×\pm 1.5\timesIQR; observations beyond this range shown as circles.

![Refer to caption](VOLARE_figure/futures_fig1b_boxplots_HAR.png)


Figure A.6: Distribution of parameter estimates for HAR family models across 13 futures using rv1 measure. Boxes display the interquartile range (IQR) with median line; whiskers extend to
±1.5×\pm 1.5\timesIQR; observations beyond this range shown as circles.

![Refer to caption](VOLARE_figure/stocks_fig3_persistence_by_measure_flipped.png)


Figure A.7: Robustness of total persistence across RV measures for stocks. Persistence for MEM(1,1) =α1+β1=\alpha\_{1}+\beta\_{1}, for AMEM(1,1) =α1+β1+γ1/2=\alpha\_{1}+\beta\_{1}+\gamma\_{1}/2, AMEM(2,1) =α1+α2+β1+γ1/2=\alpha\_{1}+\alpha\_{2}+\beta\_{1}+\gamma\_{1}/2. Each dot represents the persistence estimate for one asset using a specific RV measure (rv1, rv5, bv1, bv5, rk), with colors distinguishing the five estimators.

![Refer to caption](VOLARE_figure/forex_fig3_persistence_by_measure_flipped.png)


Figure A.8: Robustness of total persistence across RV measures for echange rates. Persistence for MEM(1,1) =α1+β1=\alpha\_{1}+\beta\_{1}, for AMEM(1,1) =α1+β1+γ1/2=\alpha\_{1}+\beta\_{1}+\gamma\_{1}/2, AMEM(2,1) =α1+α2+β1+γ1/2=\alpha\_{1}+\alpha\_{2}+\beta\_{1}+\gamma\_{1}/2. Each dot represents the persistence estimate for one asset using a specific RV measure (rv1, rv5, bv1, bv5, rk), with colors distinguishing the five estimators.

![Refer to caption](VOLARE_figure/futures_fig3_persistence_by_measure_flipped.png)


Figure A.9: Robustness of total persistence across RV measures for futures contracts. Persistence for MEM(1,1) =α1+β1=\alpha\_{1}+\beta\_{1}, for AMEM(1,1) =α1+β1+γ1/2=\alpha\_{1}+\beta\_{1}+\gamma\_{1}/2, AMEM(2,1) =α1+α2+β1+γ1/2=\alpha\_{1}+\alpha\_{2}+\beta\_{1}+\gamma\_{1}/2. Each dot represents the persistence estimate for one asset using a specific RV measure (rv1, rv5, bv1, bv5, rk), with colors distinguishing the five estimators.