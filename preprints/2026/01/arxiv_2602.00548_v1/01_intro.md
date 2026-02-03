---
authors:
- Tetsuya Takaishi
doc_id: arxiv:2602.00548v1
family_id: arxiv:2602.00548
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: The Impact of Trump-Era Tariffs on Financial Market Efficiency
url_abs: http://arxiv.org/abs/2602.00548v1
url_html: https://arxiv.org/html/2602.00548v1
venue: arXiv q-fin
version: 1
year: 2026
---


Tetsuya Takaishi

###### Abstract

This study examines the effects of Trump-era tariffs on financial market efficiency by applying multifractal detrended fluctuation analysis to the return and absolute return time series of six major financial assets: the S&P 500, SSEC, VIX, BTC/USD, EUR/USD, and Gold. Using the Hurst exponent h​(2)h(2) and multifractal strength, we assess how market dynamics responded to two major global shocks: the COVID-19 pandemic and the implementation of the Trump tariff policy in 2025. The results show that COVID-19 induced substantial changes in both the Hurst exponent and multifractal strength, particularly for the S&P 500, BTC/USD, EUR/USD, and Gold. In contrast, the effects of the Trump tariffs were more moderate but still observable across all examined time series. The Chinese market index (SSEC) remained largely unaffected by either event, apart from a distinct response to domestic stimulus measures. In addition, the VIX exhibited anti-persistent behavior with h​(2)<0.5h(2)<0.5, consistent with the rough volatility framework. These findings underscore the usefulness of multifractal analysis in capturing structural shifts in market efficiency under geopolitical and systemic shocks.

###### keywords:

Hurst exponent, Multifractality, Rough volatility, COVID-19, Trump tariffs, Market efficiency

## 1 Introduction

The Efficient Market Hypothesis (EMH), introduced by Eugene Fama in 1970, is a cornerstone of modern financial economics [[1](https://arxiv.org/html/2602.00548v1#bib.bib1)]. It posits that financial markets are *informationally efficient*, meaning that asset prices fully reflect all available information at any given time. Consequently, it is impossible to consistently earn returns that outperform the market through information-based trading strategies. Under the assumption that price movements follow a random process, the EMH implies that financial time series should exhibit randomness. Therefore, evaluating the degree of randomness in market data serves as a practical approach to assessing market efficiency.

The randomness of a time series can be quantified by the Hurst exponent [[2](https://arxiv.org/html/2602.00548v1#bib.bib2)]. When H=0.5H=0.5, the series is random; values of H>0.5H>0.5 indicate persistence, whereas H<0.5H<0.5 indicate anti-persistence. Previous studies have shown that in developed stock markets, the Hurst exponent
of return time series typically approaches 0.5, suggesting market efficiency, while in emerging markets it often exceeds 0.5, implying inefficiency. Moreover, certain developed markets exhibit H<0.5H<0.5, reflecting anti-persistent dynamics [[3](https://arxiv.org/html/2602.00548v1#bib.bib3), [4](https://arxiv.org/html/2602.00548v1#bib.bib4)].

Market efficiency can fluctuate due to various factors. For example, in the early stages of the Bitcoin market, the Hurst exponent was found to be below 0.5, exhibiting anti-persistent behavior. As the market matured, however, the exponent approached 0.5, suggesting a gradual movement toward efficiency [[5](https://arxiv.org/html/2602.00548v1#bib.bib5)]. Similarly, the power-law exponent α\alpha characterizing the tails of Bitcoin return distributions was initially around 2, smaller than the canonical value of α=3\alpha=3 known for traditional assets [[6](https://arxiv.org/html/2602.00548v1#bib.bib6), [7](https://arxiv.org/html/2602.00548v1#bib.bib7)], but has since converged toward α≈3\alpha\approx 3 as the market developed [[8](https://arxiv.org/html/2602.00548v1#bib.bib8), [9](https://arxiv.org/html/2602.00548v1#bib.bib9), [10](https://arxiv.org/html/2602.00548v1#bib.bib10)].
The tail behavior of return distributions affects the values of risk measures such as Value at Risk (VaR) and Conditional Value at Risk (CVaR). When the return distribution follows a power-law, it is known that the ratio between VaR and CVaR is determined solely by the power-law exponent[[11](https://arxiv.org/html/2602.00548v1#bib.bib11)]. This implies that, under power-law distributions, VaR and CVaR are no longer independent risk metrics.

In equity markets, the existence of the leverage effect—where volatility tends to increase more following negative returns than after positive ones—is well established[[12](https://arxiv.org/html/2602.00548v1#bib.bib12), [13](https://arxiv.org/html/2602.00548v1#bib.bib13), [14](https://arxiv.org/html/2602.00548v1#bib.bib14)]. In contrast, early studies on the Bitcoin market have reported a reverse leverage effect, in which volatility responds more strongly to positive returns[[15](https://arxiv.org/html/2602.00548v1#bib.bib15), [16](https://arxiv.org/html/2602.00548v1#bib.bib16)]. However, this effect has shown temporal variation within the Bitcoin market, and recent research suggests that its intensity has diminished in recent years[[17](https://arxiv.org/html/2602.00548v1#bib.bib17), [18](https://arxiv.org/html/2602.00548v1#bib.bib18)].

Market efficiency is also sensitive to major global events. For instance, the COVID-19 pandemic—officially declared by the World Health Organization (WHO) on 11 March 2020—had a profound impact on global financial systems. Numerous studies have documented variations in both market efficiency and multifractal strength in response to the pandemic (see, e.g., [[19](https://arxiv.org/html/2602.00548v1#bib.bib19), [20](https://arxiv.org/html/2602.00548v1#bib.bib20), [21](https://arxiv.org/html/2602.00548v1#bib.bib21), [22](https://arxiv.org/html/2602.00548v1#bib.bib22), [23](https://arxiv.org/html/2602.00548v1#bib.bib23), [24](https://arxiv.org/html/2602.00548v1#bib.bib24), [25](https://arxiv.org/html/2602.00548v1#bib.bib25), [26](https://arxiv.org/html/2602.00548v1#bib.bib26), [27](https://arxiv.org/html/2602.00548v1#bib.bib27), [28](https://arxiv.org/html/2602.00548v1#bib.bib28), [29](https://arxiv.org/html/2602.00548v1#bib.bib29), [30](https://arxiv.org/html/2602.00548v1#bib.bib30), [31](https://arxiv.org/html/2602.00548v1#bib.bib31), [32](https://arxiv.org/html/2602.00548v1#bib.bib32), [33](https://arxiv.org/html/2602.00548v1#bib.bib33), [34](https://arxiv.org/html/2602.00548v1#bib.bib34)]). However, the magnitude and nature of these impacts differ across markets and data types[[33](https://arxiv.org/html/2602.00548v1#bib.bib33)]. In China, for example, the effect of COVID-19 on the efficiency of return time series appears limited, while volatility-based series exhibit distinct patterns of response.

The second Trump administration officially commenced on January 20, 2025. Shortly thereafter, on April 2, 2025, a new trade policy—widely referred to as the *Trump Tariffs*—was introduced. Under this policy, a baseline tariff of 10% was imposed on imports from nearly all countries beginning April 5, 2025. The announcement triggered significant volatility in global financial markets, with the S&P 500 index falling by approximately 11% within two days. Following subsequent bilateral negotiations, tariff rates were adjusted on a country-by-country basis, and the policy’s effects have continued to persist.

This study investigates the impact of the Trump Tariffs on financial market efficiency. To quantify efficiency, we employ the multifractal detrended fluctuation analysis (MFDFA) framework [[35](https://arxiv.org/html/2602.00548v1#bib.bib35)] to estimate the generalized Hurst exponent. The analysis covers periods affected by both COVID-19 and the Trump Tariffs, allowing for a comparative assessment of their respective impacts. Furthermore, by analyzing both return and volatility (absolute return) time series, we evaluate how the type of data influences the degree of observed effects.

## 2 Methodology

To examine the multifractal properties of financial time series, we employ the MFDFA [[35](https://arxiv.org/html/2602.00548v1#bib.bib35)]. The procedure is described as follows.

(i) We first construct the profile Y​(i)Y(i) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y​(i)=∑j=1i[r​(j)−<r>],Y(i)=\sum\_{j=1}^{i}\left[r(j)-<r>\right], |  | (1) |

where <r><r> denotes the mean of the return series.

(ii) The profile Y​(i)Y(i) is then divided into NsN\_{s} non-overlapping segments of equal length ss, where Ns≡int​(N/s)N\_{s}\equiv\mathrm{int}(N/s). Because the total length of the series is not always a multiple of ss, a short residual segment may remain at the end. To make full use of the data, the same segmentation procedure is repeated starting from the end of the profile. Thus, a total of 2​Ns2N\_{s} segments are obtained.

(iii) For each segment ν\nu (ν=1,…,Ns\nu=1,\dots,N\_{s}), we compute the local variance as

|  |  |  |  |
| --- | --- | --- | --- |
|  | F2​(ν,s)=1s​∑i=1s[Y​((ν−1)​s+i)−Pν​(i)]2,F^{2}(\nu,s)=\frac{1}{s}\sum\_{i=1}^{s}\left[Y((\nu-1)s+i)-P\_{\nu}(i)\right]^{2}, |  | (2) |

and similarly, for ν=Ns+1,…,2​Ns\nu=N\_{s}+1,\dots,2N\_{s},

|  |  |  |  |
| --- | --- | --- | --- |
|  | F2​(ν,s)=1s​∑i=1s[Y​(N−(ν−Ns)​s+i)−Pν​(i)]2,F^{2}(\nu,s)=\frac{1}{s}\sum\_{i=1}^{s}\left[Y(N-(\nu-N\_{s})s+i)-P\_{\nu}(i)\right]^{2}, |  | (3) |

where Pν​(i)P\_{\nu}(i) denotes the fitting polynomial used to remove the local trend in segment ν\nu. The polynomial is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pν​(i)=∑k=0pak​ik,P\_{\nu}(i)=\sum\_{k=0}^{p}a\_{k}i^{k}, |  | (4) |

and in this study, we employ a cubic-order polynomial (p=3p=3).

(iv) The qqth-order fluctuation function is then obtained by averaging over all segments:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fq​(s)={12​Ns​∑ν=12​Ns[F2​(ν,s)]q/2}1/q.F\_{q}(s)=\left\{\frac{1}{2N\_{s}}\sum\_{\nu=1}^{2N\_{s}}[F^{2}(\nu,s)]^{q/2}\right\}^{1/q}. |  | (5) |

(v) The generalized Hurst exponent, denoted as h​(q)h(q), is estimated from the scaling behavior of Fq​(s)F\_{q}(s). For a time series exhibiting long-range power-law correlations, Fq​(s)F\_{q}(s) scales as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fq​(s)∼sh​(q),F\_{q}(s)\sim s^{h(q)}, |  | (6) |

for sufficiently large ss.

The singularity spectrum f​(α)f(\alpha), which characterizes the multifractal nature of the time series, can be derived from h​(q)h(q) using the Legendre transform:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(α)=q​[α−h​(q)]+1,f(\alpha)=q[\alpha-h(q)]+1, |  | (7) |

where α\alpha represents the Hölder exponent or singularity strength, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | α=h​(q)+q​h′​(q).\alpha=h(q)+qh^{\prime}(q). |  | (8) |

The Hurst exponent, a measure of market efficiency, is obtained from h​(2)h(2). In this study, the range of qq is restricted to q∈[−5,5]q\in[-5,5], because for large |q||q| the moments in the fluctuation function may diverge, leading to numerical instability in the estimation of h​(q)h(q) [[36](https://arxiv.org/html/2602.00548v1#bib.bib36)].

Finally, the degree of multifractality is quantified by the width of the generalized Hurst exponent as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​h​(q)=h​(−q)−h​(q),\Delta h(q)=h(-q)-h(q), |  | (9) |

where q≠0q\neq 0. A Gaussian time series exhibits monofractal behavior with Δ​h​(q)=0\Delta h(q)=0, while a nonzero Δ​h​(q)\Delta h(q) indicates multifractality. Therefore, the magnitude of Δ​h​(q)\Delta h(q) can be interpreted as a proxy for the degree of market inefficiency.

## 3 Data

We obtain the daily closing prices P​(t)P(t) for six major financial assets: S&P 500, SSEC, VIX, BTC/USD, EUR/USD, and Gold. Table [1](https://arxiv.org/html/2602.00548v1#S3.T1 "Table 1 ‣ 3 Data ‣ The Impact of Trump-Era Tariffs on Financial Market Efficiency") summarizes the abbreviations used for each market indicator. The data are sourced from https://www.investing.com (accessed on 27 September 2025) and cover the period from 1 January 2014 to 26 September 2025, encompassing both the COVID-19 pandemic and the implementation of the Trump tariff policy.

The logarithmic return r​(t)r(t) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | r​(t)=log⁡P​(t)−log⁡P​(t−1),r(t)=\log P(t)-\log P(t-1), |  | (10) |

where P​(t)P(t) represents the asset price at time tt. The absolute return |r​(t)||r(t)| is used as a proxy for volatility, which is known to exhibit long-memory characteristics [[37](https://arxiv.org/html/2602.00548v1#bib.bib37)].

Table 1: Correspondence between abbreviations and market indicators.

| Abbreviation | Market indicator |
| --- | --- |
| S&P500 | Standard & Poor’s 500 Composite Stock Price Index |
| SSEC | Shanghai Stock Exchange Composite Index |
| VIX | CBOE Volatility Index |
| BTC/USD | Exchange rate between Bitcoin and the US Dollar |
| EUR/USD | Exchange rate between the Euro and the US Dollar |
| Gold | Gold Futures |

As representative examples, Figures 1–3 show the time series of prices, returns, and absolute returns for the S&P 500, SSEC, and VIX, respectively.

![Refer to caption](x1.png)


Figure 1: Time series of price, return, and absolute return for the S&P 500.

![Refer to caption](x2.png)


Figure 2: Time series of price, return, and absolute return for the SSEC.

![Refer to caption](x3.png)


Figure 3: Time series of price, return, and absolute return for the VIX.

## 4 Empirical Results

The generalized Hurst exponent h​(q)h(q) is estimated using the MFDFA[[35](https://arxiv.org/html/2602.00548v1#bib.bib35)], applied to both return and absolute return time series. The analysis is conducted over a rolling three-year window, with the window advanced by one trading day at each step to capture the temporal evolution of h​(q)h(q). For all assets except BTC/USD, the three-year window is defined as 750 trading days (250 days per year). Since BTC/USD is traded continuously, its annual length is set to 365 days. The multifractal strength is quantified by Δ​h​(5)\Delta h(5), representing the difference between h​(−5)h(-5) and h​(5)h(5).

Figures 4 and 5 present the time evolution of the Hurst exponent h​(2)h(2) derived from return time series. Notably, the S&P 500 and VIX exhibit immediate responses to the COVID-19 pandemic declaration, whereas the SSEC and BTC/USD show no discernible reaction. For EUR/USD and Gold, h​(2)h(2) initially declines following the pandemic announcement but subsequently trends upward, indicating partial recovery. In comparison, the impact of the Trump tariff announcement is relatively subdued. Post-announcement, h​(2)h(2) decreases for the S&P 500 and Gold, while BTC/USD and EUR/USD display slight increases.

![Refer to caption](x4.png)


Figure 4: Time evolution of the Hurst exponent h​(2)h(2) for asset returns. Top: S&P 500; middle: SSEC; bottom: VIX.
Red line: World Health Organization’s declaration of the COVID-19 pandemic (March 11, 2020);
blue line: Chinese government’s announcement of a comprehensive economic stimulus package (September 24, 2024);
green line: implementation of Trump-era tariffs (April 2, 2025).

![Refer to caption](x5.png)


Figure 5: Time evolution of the Hurst exponent h​(2)h(2) for asset returns. Top: BTC/USD; middle: EUR/USD; bottom: Gold.
The colored lines indicate the same events as in Figure [4](https://arxiv.org/html/2602.00548v1#S4.F4 "Figure 4 ‣ 4 Empirical Results ‣ The Impact of Trump-Era Tariffs on Financial Market Efficiency").

![Refer to caption](x6.png)


Figure 6: Time evolution of the Hurst exponent h​(2)h(2) for absolute returns. Top: S&P 500; middle: SSEC; bottom: VIX.
The colored lines indicate the same events as in Figure [4](https://arxiv.org/html/2602.00548v1#S4.F4 "Figure 4 ‣ 4 Empirical Results ‣ The Impact of Trump-Era Tariffs on Financial Market Efficiency").

![Refer to caption](x7.png)


Figure 7: Time evolution of the Hurst exponent h​(2)h(2) for absolute returns. Top: BTC/USD; middle: EUR/USD; bottom: Gold.
The colored lines indicate the same events as in Figure [4](https://arxiv.org/html/2602.00548v1#S4.F4 "Figure 4 ‣ 4 Empirical Results ‣ The Impact of Trump-Era Tariffs on Financial Market Efficiency").

Figures 6 and 7 depict the temporal variation of h​(2)h(2) calculated from absolute return series. In contrast to the raw return results, the S&P 500, EUR/USD, and Gold demonstrate pronounced sensitivity to the pandemic declaration.
Furthermore, an increase in h​(2)h(2) of the SSEC has also been observed following the declaration of the pandemic.
The effect of the Trump tariffs remains limited, mirroring the return-based findings; however, with the exception of EUR/USD, h​(2)h(2) increases following the announcement. For the SSEC, a marked rise in h​(2)h(2) is observed in response to the Chinese government’s economic stimulus measures, as indicated by the blue line.

Figures 8 and 9 illustrate the evolution of multifractal strength Δ​h​(5)\Delta h(5) based on return time series, while Figures 10 and 11 show the corresponding dynamics derived from absolute returns. Although fluctuations in Δ​h​(5)\Delta h(5) are substantial and not always attributable to specific events, several assets exhibit clear responses to the COVID-19 pandemic. For instance, all assets except the SSEC show immediate shifts in return-based multifractal strength following the pandemic declaration. Similarly, in the absolute return-based analysis, significant changes are observed in the S&P 500, BTC/USD, EUR/USD, and Gold.

![Refer to caption](x8.png)


Figure 8: Time evolution of the multifractal strength Δ​h​(5)\Delta h(5) for returns. Top: S&P 500; middle: SSEC; bottom: VIX.
The colored lines indicate the same events as in Figure [4](https://arxiv.org/html/2602.00548v1#S4.F4 "Figure 4 ‣ 4 Empirical Results ‣ The Impact of Trump-Era Tariffs on Financial Market Efficiency").

![Refer to caption](x9.png)


Figure 9: Time evolution of the multifractal strength Δ​h​(5)\Delta h(5) for returns. Top: BTC/USD; middle: EUR/USD; bottom: Gold.
The colored lines indicate the same events as in Figure [4](https://arxiv.org/html/2602.00548v1#S4.F4 "Figure 4 ‣ 4 Empirical Results ‣ The Impact of Trump-Era Tariffs on Financial Market Efficiency").

![Refer to caption](x10.png)


Figure 10: Time evolution of the multifractal strength Δ​h​(5)\Delta h(5) for absolute returns. Top: S&P 500; middle: SSEC; bottom: VIX.
The colored lines indicate the same events as in Figure [4](https://arxiv.org/html/2602.00548v1#S4.F4 "Figure 4 ‣ 4 Empirical Results ‣ The Impact of Trump-Era Tariffs on Financial Market Efficiency").

![Refer to caption](x11.png)


Figure 11: Time evolution of the multifractal strength Δ​h​(5)\Delta h(5) for absolute returns. Top: BTC/USD; middle: EUR/USD; bottom: Gold.
The colored lines indicate the same events as in Figure [4](https://arxiv.org/html/2602.00548v1#S4.F4 "Figure 4 ‣ 4 Empirical Results ‣ The Impact of Trump-Era Tariffs on Financial Market Efficiency").

Consistent with the h​(2)h(2) results, the influence of the Trump tariffs on multifractal strength is relatively minor. Nonetheless, observable changes are present in the S&P 500 and Gold time series. The SSEC remains largely unaffected by both global events, although a distinct response to the domestic stimulus policy announced on September 24, 2024, is evident.

The multifractal strength of EUR/USD and Gold for absolute returns shifts to negative values during the pandemic, implying h​(−5)<h​(5)h(-5)<h(5) and suggesting that h​(q)h(q) becomes an increasing function of qq under extreme market conditions.

![Refer to caption](x12.png)


Figure 12: Time evolution of the Hurst exponent and multifractal strength for VIX price time series.
The colored lines indicate the same events as in Figure [4](https://arxiv.org/html/2602.00548v1#S4.F4 "Figure 4 ‣ 4 Empirical Results ‣ The Impact of Trump-Era Tariffs on Financial Market Efficiency").

It is well established that the Hurst exponent h​(2)h(2) for stock return series typically approximates 0.5, consistent with a random walk. However, as shown in Figure 4, the VIX return series exhibits h​(2)<0.5h(2)<0.5 during non-pandemic periods, indicating anti-persistent behavior. This is characteristic of volatility indices, and aligns with prior empirical findings that volatility-based time series often display rough volatility dynamics [[38](https://arxiv.org/html/2602.00548v1#bib.bib38), [39](https://arxiv.org/html/2602.00548v1#bib.bib39), [40](https://arxiv.org/html/2602.00548v1#bib.bib40), [41](https://arxiv.org/html/2602.00548v1#bib.bib41), [42](https://arxiv.org/html/2602.00548v1#bib.bib42), [43](https://arxiv.org/html/2602.00548v1#bib.bib43), [44](https://arxiv.org/html/2602.00548v1#bib.bib44), [45](https://arxiv.org/html/2602.00548v1#bib.bib45)]. The anti-persistence in VIX returns has also been pointed out in [[46](https://arxiv.org/html/2602.00548v1#bib.bib46)].
Given that absolute returns serve as a proxy for volatility, it is reasonable to expect the VIX price series to exhibit similar statistical properties. Figure 12 confirms this, showing that the temporal evolution of h​(2)h(2) and Δ​h​(5)\Delta h(5) in the VIX price time series closely mirrors that of the absolute return series, particularly in comparison with the S&P 500.

## 5 Conclusion

This study investigated the impact of the Trump-era tariff policy on financial market efficiency by applying multifractal detrended fluctuation analysis (MFDFA) to return and absolute return time series across six major financial assets. By estimating the generalized Hurst exponent h​(q)h(q) and multifractal strength Δ​h​(5)\Delta h(5), we captured temporal variations in market dynamics in response to two significant global events: the COVID-19 pandemic and the implementation of the Trump tariffs.

Our findings reveal that the COVID-19 pandemic induced substantial shifts in both the Hurst exponent and multifractal strength, particularly in the S&P 500, BTC/USD, EUR/USD, and Gold. These changes reflect heightened market instability and structural alterations in efficiency during periods of systemic stress. In contrast, the impact of the Trump-era tariff announcement was comparatively modest, though still discernible across all examined time series.

The Chinese market index (SSEC) remained largely insulated from both global events, with the exception of a pronounced response to domestic economic stimulus measures announced on September 24, 2024. This suggests that local policy interventions may exert a more immediate influence on market structure than external geopolitical shocks.

Additionally, the observed shift to negative multifractal strength in the absolute return series of EUR/USD and Gold during the pandemic implies a reversal in the ordering of h​(−5)h(-5) and h​(5)h(5), indicating that the general Hurst exponent h​(q)h(q) became an increasing function of qq. This phenomenon underscores the sensitivity of multifractal properties to extreme market conditions.

Finally, the anti-persistent behavior observed in the VIX return time series, characterized by h​(2)<0.5h(2)<0.5, is consistent with prior empirical evidence on return volatility and supports the classification of such dynamics within the rough volatility framework. Furthermore, the statistical similarity between the VIX price time series and the absolute return series further substantiates this interpretation.

Overall, our results highlight the utility of multifractal analysis in detecting nuanced structural shifts in market efficiency and provide a comparative lens through which to assess the financial impact of geopolitical and health-related shocks.

## Acknowledgements

The numerical calculations in this study were carried out using the computer facilities of the Yukawa Institute for Theoretical Physics and the Institute of Statistical Mathematics.

## References

* [1]

  Eugene F Fama.
  Efficient capital markets: A review of theory and empirical work.
  The journal of Finance, 25(2):383–417, 1970.
* [2]

  Harold Edwin Hurst.
  Long-term storage capacity of reservoirs.
  Transactions of the American society of civil engineers, 116(1):770–799, 1951.
* [3]

  T. Di Matteo, T. Aste, and Michel M. Dacorogna.
  Long-term memories of developed and emerging markets: Using the scaling analysis to characterize their stage of development.
  Journal of Banking & Finance, 29(4):827–851, 2005.
* [4]

  Tetsuya Takaishi.
  Time evolution of market efficiency and multifractality of the Japanese stock market.
  Journal of Risk and Financial Management, 15(1):31, 2022.
* [5]

  Tetsuya Takaishi and Takanori Adachi.
  Market efficiency, liquidity, and multifractality of Bitcoin: A dynamic study.
  Asia-Pacific Financial Markets, 27:145–154, 2020.
* [6]

  Parameswaran Gopikrishnan, Martin Meyer, LA Nunes Amaral, and H Eugene Stanley.
  Inverse cubic law for the distribution of stock price variations.
  The European Physical Journal B-Condensed Matter and Complex Systems, 3(2):139–140, 1998.
* [7]

  Parameswaran Gopikrishnan, Vasiliki Plerou, Luis A Nunes Amaral, Martin Meyer, and H Eugene Stanley.
  Scaling of the distribution of fluctuations of financial market indices.
  Physical Review E, 60(5):5305, 1999.
* [8]

  Soumya Easwaran, Manu Dixit, and Sitabhra Sinha.
  Bitcoin dynamics: the inverse square law of price fluctuations and other stylized facts.
  In Econophysics and data driven modelling of market dynamics, pages 121–128. Springer, 2015.
* [9]

  Stanisław Drożdż, Robert Gȩbarowski, Ludovico Minati, Paweł Oświȩcimka, and Marcin Wa̧torek.
  Bitcoin market route to maturity? evidence from return fluctuations, temporal correlations and multiscaling effects.
  Chaos: An Interdisciplinary Journal of Nonlinear Science, 28(7):071101, 2018.
* [10]

  Tetsuya Takaishi.
  Recent scaling properties of Bitcoin price returns.
  Journal of Physics: Conference Series, 1730(1):012124, 2021.
* [11]

  Tetsuya Takaishi.
  Properties of VaR and CVaR risk measures in high-frequency domain: Long–short asymmetry and significance of the power-law tail.
  Journal of Risk and Financial Management, 16(9):391, 2023.
* [12]

  Fischer Black.
  Studies of stock market volatility changes.
  1976 Proceedings of the American Statisticsl Association, Business and Economic Statistics Section, pages 177–181, 1976.
* [13]

  Andrew A Christie.
  The stochastic behavior of common stock variances: Value, leverage and interest rate effects.
  Journal of Financial Economics, 10:407–432, 1982.
* [14]

  Guojun Wu.
  The determinants of asymmetric volatility.
  The Review of Financial Studies, 14(3):837–859, 2001.
* [15]

  Elie Bouri, Georges Azzi, and Anne Haubo Dyhrberg.
  On the return-volatility relationship in the Bitcoin market around the price crash of 2013.
  Economics: The Open-Access, Open-Assessment E-Journal, 11:1–16, 2017.
* [16]

  Stavros Stavroyiannis and Vassilios Babalos.
  Dynamic properties of the Bitcoin and the US market.
  Available at SSRN 2966998, 2017.
* [17]

  Tetsuya Takaishi.
  Statistical properties and multifractality of Bitcoin.
  Physica A, 506:507–519, 2018.
* [18]

  Tetsuya Takaishi.
  Time-varying properties of asymmetric volatility and multifractality in Bitcoin.
  Plos one, 16(2):e0246209, 2021.
* [19]

  Faheem Aslam, Saqib Aziz, Duc Khuong Nguyen, Khurrum S Mughal, and Maaz Khan.
  On the efficiency of foreign exchange markets in times of the COVID-19 pandemic.
  Technological forecasting and social change, 161:120261, 2020.
* [20]

  Leonardo HS Fernandes, Fernando HA De Araujo, Jose WL Silva, Igor EM Silva, and Benjamin Miranda Tabak.
  Evaluating the efficiency of brazilian stock market indices: The case of covid-19.
  Fractals, 30(01):2250014, 2022.
* [21]

  Jian Wang, Wei Shao, and Junseok Kim.
  Analysis of the impact of COVID-19 on the correlations between crude oil and agricultural futures.
  Chaos, Solitons & Fractals, 136:109896, 2020.
* [22]

  Na Shen and Jia Yi Chen.
  Multifractal analysis of the impact of COVID-19 on NASDAQ, CIOPI, and WTI crude oil market.
  Fluctuation and Noise Letters, 21(04):2250041, 2022.
* [23]

  Walid Mensi, Yun-Jung Lee, Xuan Vinh Vo, and Seong-Min Yoon.
  Does oil price variability affect the long memory and weak form efficiency of stock markets in top oil producers and oil consumers? evidence from an asymmetric mf-dfa approach.
  The North American Journal of Economics and Finance, 57:101446, 2021.
* [24]

  Mehrzad Alijani, Bahman Banimahd, Hashem Nikoomaram, and Ahmad Yaghobnezhad.
  Fractal analysis and the relationship between efficiency of capital market indices and COVID-19 in iran.
  Results in Physics, 25:104262, 2021.
* [25]

  Pavlos I Zitis, Shinji Kakinaka, Ken Umeno, Michael P Hanias, Stavros G Stavrinides, and Stelios M Potirakis.
  Investigating dynamical complexity and fractal characteristics of Bitcoin/US dollar and Euro/US dollar exchange rates around the COVID-19 outbreak.
  Entropy, 25(2):214, 2023.
* [26]

  Syed Ali Raza, Nida Shah, and Muhammed Tahir Suleman.
  A multifractal detrended fluctuation analysis of islamic and conventional financial markets efficiency during the COVID-19 pandemic.
  International Economics, 177:100463, 2024.
* [27]

  Deniz Erer, Elif Erer, and Selim Güngör.
  The aggregate and sectoral time-varying market efficiency during crisis periods in turkey: a comparative analysis with COVID-19 outbreak and the global financial crisis.
  Financial Innovation, 9(1):80, 2023.
* [28]

  Faheem Aslam, Wahbeeah Mohti, and Paulo Ferreira.
  Evidence of intraday multifractality in european stock markets during the recent coronavirus (covid-19) outbreak.
  International Journal of Financial Studies, 8(2):31, 2020.
* [29]

  Walid Mensi, Ahmet Sensoy, Xuan Vinh Vo, and Sang Hoon Kang.
  Impact of COVID-19 outbreak on asymmetric multifractality of gold and oil prices.
  Resources Policy, 69:101829, 2020.
* [30]

  Saba Ameer, Safwan Mohd Nor, Sajid Ali, and Nur Haiza Muhammad Zawawi.
  The impact of covid-19 on brics and msci emerging markets efficiency: Evidence from mf-dfa.
  Fractal and Fractional, 7(7):519, 2023.
* [31]

  Foued Saâdaoui.
  Skewed multifractal scaling of stock markets during the covid-19 pandemic.
  Chaos, Solitons & Fractals, 170:113372, 2023.
* [32]

  M Belén Arouxet, Aurelio F Bariviera, Verónica E Pastor, and Victoria Vampa.
  Covid-19 impact on cryptocurrencies: evidence from a wavelet-based hurst exponent.
  Physica A: Statistical Mechanics and its Applications, 596:127170, 2022.
* [33]

  Tetsuya Takaishi.
  Impact of the COVID-19 pandemic on the financial market efficiency of price returns, absolute returns, and volatility increment: Evidence from stock and cryptocurrency markets.
  Journal of Risk and Financial Management, 18(5):237, 2025.
* [34]

  Xing-Lu Gao, Zhi-Qiang Jiang, and Wei-Xing Zhou.
  Impact of the covid-19 pandemic on the intermittent behavior of the global spot markets of staple food crops.
  Journal of Management Science and Engineering, 9(4):510–521, 2024.
* [35]

  Jan W Kantelhardt, Stephan A Zschiegner, Eva Koscielny-Bunde, Shlomo Havlin, Armin Bunde, and H Eugene Stanley.
  Multifractal detrended fluctuation analysis of nonstationary time series.
  Physica A, 316(1):87–114, 2002.
* [36]

  Z.-Q. Jiang, W.-J. Xie, W.-X. Zhou, and D. Sornette.
  Multifractal analysis of financial markets.
  Rep. Prog. Phys., 82(12):125901, 2019.
* [37]

  Zhuanxin Ding, Clive WJ Granger, and Robert F Engle.
  A long memory property of stock market returns and a new model.
  Journal of empirical finance, 1(1):83–106, 1993.
* [38]

  Jim Gatheral, Thibault Jaisson, and Mathieu Rosenbaum.
  Volatility is rough.
  Quantitative Finance, 18(6):933–949, 2018.
* [39]

  Mikkel Bennedsen, Asger Lunde, and Mikko S Pakkanen.
  Decoupling the short-and long-term behavior of stochastic volatility.
  Journal of Financial Econometrics, 20(5):961–1006, 2022.
* [40]

  Giulia Livieri, Saad Mouti, Andrea Pallavicini, and Mathieu Rosenbaum.
  Rough volatility: evidence from option prices.
  IISE transactions, 50(9):767–776, 2018.
* [41]

  Tetsuya Takaishi.
  Rough volatility of Bitcoin.
  Finance Research Letters, 32:101379, 2020.
* [42]

  Fabien Le Floc’h.
  Roughness of the implied volatility.
  arXiv preprint arXiv:2207.04930, 2022.
* [43]

  Giuseppe Brandi and T Di Matteo.
  Multiscaling and rough volatility: An empirical investigation.
  International Review of Financial Analysis, 84:102324, 2022.
* [44]

  Rama Cont and Purba Das.
  Rough volatility: fact or artefact?
  Sankhya B, pages 1–33, 2024.
* [45]

  Tetsuya Takaishi.
  Multifractality and sample size influence on Bitcoin volatility patterns.
  Finance Research Letters, 74:106683, 2025.
* [46]

  Aurelio F Bariviera, Laura Fabregat-Aibar, and Maria-Teresa Sorrosal-Forradellas.
  Disentangling the impact of economic and health crises on financial markets.
  Research in International Business and Finance, 65:101928, 2023.