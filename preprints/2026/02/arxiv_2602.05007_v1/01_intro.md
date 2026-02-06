---
authors:
- Sasha Stoikov
- Aadityaa Singla
- Umu Cetin
- Luis Alonso Cendra Villalobos
doc_id: arxiv:2602.05007v1
family_id: arxiv:2602.05007
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Music as an Asset Class
url_abs: http://arxiv.org/abs/2602.05007v1
url_html: https://arxiv.org/html/2602.05007v1
venue: arXiv q-fin
version: 1
year: 2026
---


Sasha Stoikov
ORIE, Cornell University

Aadityaa Singla
Computer Science, Cornell University

Umu Cetin
ORIE, Cornell University

Luis Alonso Cendra Villalobos
ORIE, Cornell University

###### Abstract

In the streaming era, music revenues distributed to rights holders have become more transparent. However, it is not yet clear how to quantify the risk and return characteristics of music royalty assets, as is done with equities. In this paper, we fit three discounted cashflow models to transactions on the Royalty Exchange platform. We use our best model to backtest the one year and five year performance of music royalty assets, after transaction costs. We find that Life of Rights (LOR) music assets had risk and return characteristics comparable to stocks in the S&P500, when held over 5 years. Since the performance of stocks and music assets are likely to be uncorrelated, this result may help investors assess this asset class within the context of a more traditional stock and bond portfolio.

## 1 Introduction

The market for music royalties is illiquid: transactions are rare, there is significant information asymmetry and transaction costs are high. This poses significant challenges for pricing assets fairly and fitting models to past transactions. Without a model calibrated to transactions, it is impossible to estimate fluctuations in the value of an asset from one year to the other, using only song revenues data.

As Shot Tower Capital, a firm that specializes in facilitating music transactions, states in their 2025 report 111Shot Tower Capital. 2024 Annual Report. Baltimore: Shot Tower Capital, 2025., “The key valuation methodology for music catalogs and companies is a discounted cash flow analysis cross-checked against comparable market transactions”. The first method, discounted cashflow analysis, takes into account past cash flows to estimate future cashflows. Though very popular and grounded in standard finance theory, this method can use a variety of potential factors (such as genre, age, vintage, or country) in a rather ad-hoc manner. The second method, comparing to recent market transactions, seems reasonable in theory. However it is challenging in practice since there are limited transaction data available for comparable artists.

Both these valuation methods, although useful for buyers and sellers to converge on a fair transaction price, don’t say much about how good or bad an investment a music royalty asset is. Therefore, there is a pressing need for robust pricing models that can estimate the past returns of music royalties, even when market transactions are relatively sparse.

In this paper, we fit three simple DCF models to 1295 transactions on the Royalty Exchange platform. With these calibrated models, we can use historical revenue data to estimate annual returns. We compute the expected return of an asset

|  |  |  |
| --- | --- | --- |
|  | ri=pi+1+ci−pi−tipir\_{i}=\frac{p\_{i+1}+c\_{i}-p\_{i}-t\_{i}}{p\_{i}} |  |

where pip\_{i} and pi+1p\_{i+1} are prices, tit\_{i} is the transaction costs that the platform enacts ($500 buyer fee and 8% seller commission), and cic\_{i} is the cashflow collected between period ii and i+1i+1. The cashflows are usually observable on a quarterly basis, but the prices pip\_{i} are typically not observable, since transactions are rare.

In section 2, we describe the Royalty Exchange data and highlight some of the stylized facts that differentiate music royalties from traditional assets like stocks and bonds. In section 3, we introduce three DCF models. We calibrate each model to actual transactions to fit the parameters.
In section 4, we use the best fitting model to backtest the risk/return characteristics of music royalties over a one year and five year period and compare them to equities over the same period.
In section 5, we conclude with some limitations of our approach and suggestions for future work.

## 2 Data

Royalty Exchange is a transparent market for music royalty transactions. Before a rights holder sells on the platform, they must provide a history of past cashflows from a collection agency like ASCAP or BMI, and after some due diligence, buyers compete in a standard auction. After a primary sale happens, the asset may be traded in a secondary market with lower transaction costs. In our dataset, 1295 trades of which 1134 deals were primary sales were traded since 2017, for a face value of $97M.

There are two main categories of data that Royalty Exchange publishes on the platform: deals and revenues. At the deal level, we know the price of the transaction, the LTM (last twelve months revenue), the LTY (last three years revenue, annualized), the age of the catalog and the deal terms (10Y, 30Y or LOR — Life of Rights). On the revenues side, we have a time series of quarterly revenues preceding each sale.

Since music royalty asset prices can vary significantly for different values of the LTM, market participants typically divide prices by the LTM to normalize transactions and express them in terms of
a price-to-LTM ratio (also called a “multiplier” or ”multiple”).
In Figure [1](https://arxiv.org/html/2602.05007v1#S2.F1 "Figure 1 ‣ 2 Data ‣ Music as an Asset Class"), we display the multipliers for 10Y and LOR as a function of LTM/LTY.

![Refer to caption](volatility.png)


Figure 1:  Multipliers for 10Y and Life of Rights contracts as a function of LTM/LTY

For the LOR and 10Y contracts, we see that the market gives a premium to assets whose revenues are stable and the ratio of LTM/LTY is close to 1, compared to assets where recent revenues have been growing or shrinking. This suggests that in the context of a DCF model, there could be a risk-adjusted discount factor at play. In other words, the discount rate applied to cashflows that are more volatile is likely to be higher than for cashflows that are stable, where LTM and LTY are close to each other.

In Figure [2](https://arxiv.org/html/2602.05007v1#S2.F2 "Figure 2 ‣ 2 Data ‣ Music as an Asset Class"), we display the multipliers for 10Y and LOR as a function of the age of the catalog. Note that the multipliers are increasing in the age of a song.

![Refer to caption](age.png)


Figure 2:  Multipliers for 10Y and Life of Rights contracts as a function of song age

## 3 Model

To price an nn-year royalty asset, we use a general discounted cashflow formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pn=∑i=1nC(1+R)iP^{n}=\sum\_{i=1}^{n}\frac{C}{(1+R)^{i}} |  | (1) |

where CC is the expected yearly cashflow and RR is the discount rate. Different assumptions on CC and RR lead to different pricing models. In particular, we consider the following three models:

###### Model 1

-
Expected music revenues will stay flat and the discount rate is constant.

|  |  |  |
| --- | --- | --- |
|  | C=L​T​M\displaystyle C=LTM |  |

|  |  |  |
| --- | --- | --- |
|  | R=r\displaystyle R=r |  |

|  |  |  |
| --- | --- | --- |
|  | M=PnL​T​M=∑i=1N1(1+r)iM=\frac{P^{n}}{LTM}=\sum\_{i=1}^{N}\frac{1}{(1+r)^{i}} |  |

###### Model 2

-
Discount rates are risk adjusted and cashflows are expected to stabilize at a level lower than the LTM.

|  |  |  |
| --- | --- | --- |
|  | C=L​T​M∗a\displaystyle C=LTM\*a |  |

|  |  |  |
| --- | --- | --- |
|  | R=r+k×|L​T​M/L​T​Y−1|\displaystyle R=r+k\times|LTM/LTY-1| |  |

|  |  |  |
| --- | --- | --- |
|  | M=PnL​T​M=∑i=1Na(1+r+k×|L​T​M/L​T​Y−1|)iM=\frac{P^{n}}{LTM}=\sum\_{i=1}^{N}\frac{a}{(1+r+k\times|LTM/LTY-1|)^{i}} |  |

###### Model 3

-
There is a premium for older songs

|  |  |  |
| --- | --- | --- |
|  | C=L​T​M∗(a+b×a​g​e)\displaystyle C=LTM\*(a+b\times age) |  |

|  |  |  |
| --- | --- | --- |
|  | R=r+k×|L​T​M/L​T​Y−1|\displaystyle R=r+k\times|LTM/LTY-1| |  |

|  |  |  |
| --- | --- | --- |
|  | M=PnL​T​M=∑i=1Na+b×a​g​e(1+r+k×|L​T​M/L​T​Y−1|)iM=\frac{P^{n}}{LTM}=\sum\_{i=1}^{N}\frac{a+b\times age}{(1+r+k\times|LTM/LTY-1|)^{i}} |  |

Note that Model 1 has a single parameter θ1=(r)\theta\_{1}=(r), Model 2 has 3 parameters θ2=(r,a,k)\theta\_{2}=(r,a,k) and Model 3 has 4 parameters θ3=(r,a,k,b)\theta\_{3}=(r,a,k,b). Since each transaction has a traded multiplier, we may optimize over these parameters to obtain the least square error.

In other words, we run the following optimization

|  |  |  |
| --- | --- | --- |
|  | minθ​∑i=11295(Mt​r​a​d​e​di−Mi​(θ))2\min\_{\theta}\sum\_{i=1}^{1295}(M\_{traded}^{i}-M^{i}(\theta))^{2} |  |

and display the results in Table [1](https://arxiv.org/html/2602.05007v1#S3.T1 "Table 1 ‣ 3 Model ‣ Music as an Asset Class").

Table 1: Model Paramter Optimization

| model | MSE | r | a | k | b |
| --- | --- | --- | --- | --- | --- |
| 1 | 8.8 | 14.0% |  |  |  |
| 2 | 7.7 | 7.6% | 0.69 | 0.071 |  |
| 3 | 5.7 | 8.3% | 0.61 | 0.058 | 0.0098 |

In the sequel, we use model 3, as it has a significantly lower mean squared error, compared to the simpler models. If we re-price all assets using model 3, we obtain Figure [3](https://arxiv.org/html/2602.05007v1#S3.F3 "Figure 3 ‣ 3 Model ‣ Music as an Asset Class"), which is qualitatively quite similar to Figure [1](https://arxiv.org/html/2602.05007v1#S2.F1 "Figure 1 ‣ 2 Data ‣ Music as an Asset Class"). Furthermore, this model also leads to higher multipliers for older songs, see Figure [4](https://arxiv.org/html/2602.05007v1#S3.F4 "Figure 4 ‣ 3 Model ‣ Music as an Asset Class"), similar to the result in Figure [2](https://arxiv.org/html/2602.05007v1#S2.F2 "Figure 2 ‣ 2 Data ‣ Music as an Asset Class")

![Refer to caption](volatility_model.png)


Figure 3:  Multipliers for 10Y and Life of Rights contracts as a function of LTM/LTY, for the model 3

![Refer to caption](age_model.png)


Figure 4:  Multipliers for 10Y and Life of Rights contracts as a function of age, for model 3

## 4 Backtesting

How do the risk and return characteristics of a portfolio of songs compare to those of a portfolio of stocks? As mentioned in the introduction, transaction costs for songs on a platform like Royalty Exchange are around 8%, much higher than the transaction costs of equities, which are typically expressed in basis points. Moreover, music assets have dividends that are often in the double digits, while stocks have negligible dividends. Finally, music assets tend to depreciate as revenues often decay, particularly for 10 year contracts that have a value of zero at expiry. However, in periods like 2017-2022, when the streaming grew steadily, Life of Rights assets have often appreciated, leading their investors to win on both counts, with high dividends and positive returns.

We now return to our formula in the introduction:

|  |  |  |
| --- | --- | --- |
|  | ri=pi+1+ci−pi−tipir\_{i}=\frac{p\_{i+1}+c\_{i}-p\_{i}-t\_{i}}{p\_{i}} |  |

where pip\_{i} and pi+1p\_{i+1} can now be computed using the model.
We decompose the returns into dividends:

|  |  |  |
| --- | --- | --- |
|  | di=cipid\_{i}=\frac{c\_{i}}{p\_{i}} |  |

pure asset returns:

|  |  |  |
| --- | --- | --- |
|  | ei=pi+1−pipie\_{i}=\frac{p\_{i+1}-p\_{i}}{p\_{i}} |  |

and transaction costs

|  |  |  |
| --- | --- | --- |
|  | fi=tipif\_{i}=\frac{t\_{i}}{p\_{i}} |  |

Comparing the LOR and 10Y returns in Tables [2](https://arxiv.org/html/2602.05007v1#S4.T2 "Table 2 ‣ 4 Backtesting ‣ Music as an Asset Class") and [3](https://arxiv.org/html/2602.05007v1#S4.T3 "Table 3 ‣ 4 Backtesting ‣ Music as an Asset Class"), we find that the 10Y assets have high dividends and depreciate fast, while the LOR assets appreciate slightly, but offer lower dividends. This contrast highlights the fundamental tradeoff: 10Y contracts deliver yield up front but erode in value, while LOR contracts are longer-duration and more sensitive to discount rates, but can capture modest appreciation over time.

The backtesting methodology simulates a one-year and 5 year buy-and-hold strategy. We assume an investor purchases an asset at time tt at the model-implied price ptp\_{t}, calculated using only information available at that time (specifically, the LTM, the LTY and the age of the catalog). The investor then collects four quarters of actual realized cashflows ctc\_{t} and sells the asset at time t+4t+4 at the model-implied price pt+4p\_{t+4}, which is recalculated using the updated revenue information available at the end of the holding period. We incorporate transaction costs, tit\_{i}, in the form of a $500 buyer fee (fixed) and an 8% seller commission, which are deducted from returns to emulate the requirements of the Royalty Exchange platform. The five-year backtest follows a similar methodology to the one-year analysis: investors purchase at the model price in 2017, collect 20 quarters of actual cashflows, and sell at the model price in 2022.

Table 2: Life of Rights Assets

| Metric (%) | 2017 | 2018 | 2019 | 2020 | 2021 | 5-yr (total) | 5-yr (annualized) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| d - Median Dividends | 12.4% | 11.3% | 12.1% | 11.8% | 13.2% | 62.3% |  |
| e - Median Capital Gains | 10.7% | 6.2% | 6.1% | 3.9% | 8.4% | 25.4% |  |
| f - Median TC | 8.9% | 8.5% | 8.5% | 8.3% | 8.7% | 10.0% |  |
| r - Median Return | 12.5% | 7.1% | 9.0% | 10.6% | 12.9% | 82.64% | 12.8% |
| 90th Percentile Return | 77.6% | 72.4% | 66.5% | 47.9% | 81.2% | 279.7% | 30.6% |
| 10th Percentile Return | -23.1% | -42.8% | -28.3% | -42.5% | -25.5% | -7.84% | -1.6% |




Table 3: 10-Year Assets

| Metric (%) | 2017 | 2018 | 2019 | 2020 | 2021 | 5-yr (total) | 5-yr (annualized) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| d - Median Dividends | 16.7% | 17.3% | 14.8% | 13.1% | 16.2% | 90.3% |  |
| e - Median Capital Gains | 3.3% | -3.2% | -1.6% | -10.7% | 6.4% | -40.5% |  |
| f - Median TC | 8.3% | 7.7% | 7.9% | 7.1% | 8.5% | 4.8% |  |
| r - Median Return | 8.1% | 2.0% | 5.0% | -7.1% | 9.5% | 42.5% | 7.3% |
| 90th Percentile Return | 64.2% | 44.5% | 42.1% | 28.0% | 51.1% | 155.1% | 20.6 % |
| 10th Percentile Return | -28.5% | -27.5% | -32.2% | -37.7% | -21.5% | -59.9% | -21.3% |




Table 4: S&P500 stocks

| Metric (%) | 2017 | 2018 | 2019 | 2020 | 2021 | 5-yr (total) | 5-yr (annualized) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Median Return | 22.5% | -3.3% | 32.4% | 13.2% | 30.6% | 77.7 % | 12.2% |
| 90th Percentile Return | 58.1% | 23.9% | 64.5% | 56.4% | 67.31% | 257.2 % | 29.0% |
| 10th Percentile Return | -3.2% | -30.3% | 4.6% | -17.3% | 0.2% | -15.3 % | -3.3% |

Both music asset types exhibit substantial spread between the top and bottom deciles, reflecting the unpredictable nature of music royalty performance. The return dispersion across the 10th and 90th percentiles is illustrated in the tables for LOR and 10Y assets.

For life of rights contracts, the median annual return across 2017–2021 is 12.8%, driven primarily by consistent dividend yields (11–13% annually) and modest capital appreciation (typically between 4–11% annually). This performance highlights that the majority of LOR returns come from recurring cashflows rather than speculative price movements. Ten year contracts exhibit lower median returns of roughly 7.3% annually. These returns are primarily composed of higher dividend income (13–17%) but are offset by frequent price depreciation as contracts approach expiration. This contrast highlights the structural differences in payout and resale profiles between perpetual and term-limited royalty assets.

Finally, we compare these results with the median returns in the S&P 500. To avoid survivorship bias, we selected the stocks in the index at the befinning of each backtest period and display the results in Table [4](https://arxiv.org/html/2602.05007v1#S4.T4 "Table 4 ‣ 4 Backtesting ‣ Music as an Asset Class"). Note that the medians, 10th and 90th percentiles are comparable to the performance of LOR assets, over the course of a 5 year period, after transaction costs. However, from one year to the next, the median returns of LOR assets are much more stable, while the equity median returns change significantly from year to year. Indeed, one of the most often mentioned features of music assets is that they tend to be uncorrelated to financial markets. Our backtests are consistent with this idea.

## 5 Conclusion

Music royalties exhibit low correlation with equities, making them a potentially valuable addition to diversified portfolios. In this paper, we introduced three discounted cash flow models for valuing music royalty assets and demonstrated how they can be calibrated to observed transactions. Using these models, we backtested the performance of median music assets over one- and five-year horizons.

Our models, while useful, have important limitations. They do not explicitly incorporate characteristics such as genre, popularity, volatility, or industry growth. We also assumed constant interest rates. Another concern is that our backtests are in-sample: model parameters were estimated using all transactions through 2025, whereas a real investor in, say, 2018 would not have had access to this information.

Despite these caveats, our analysis suggests that Life of Rights assets outperform shorter-horizon 10-Year assets and, when held for five years, achieve risk-return profiles broadly comparable to equities. For music to mature as a true asset class, pricing models will need to move beyond financial history and incorporate measures of musical quality and cultural relevance. Ultimately, the drivers of over- or under-performance are not just financial, but artistic: how good the songs are, and how likely they are to expand their audience over time.

## References