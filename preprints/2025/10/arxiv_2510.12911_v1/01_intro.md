---
authors:
- Yasin Simsek
doc_id: arxiv:2510.12911v1
family_id: arxiv:2510.12911
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote
  11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya
  for their guidance and support. I would also like to thank Anna Cieslak, Mehmet
  Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen,
  Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics
  Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions.
  Email: yasin.simsek@duke.edu.'
url_abs: http://arxiv.org/abs/2510.12911v1
url_html: https://arxiv.org/html/2510.12911v1
venue: arXiv q-fin
version: 1
year: 2025
---


Yasin Simsek

(
This version: October 14, 2025
  
[[Click here for the latest version](https://yasin-simsek.github.io/assets/documents/jmp_last_version.pdf)]
)

###### Abstract

Spot covariance estimation is commonly based on high-frequency open-to-close return data over short time windows, but such approaches face a trade-off between statistical accuracy and localization. In this paper, I introduce a new estimation framework using high-frequency candlestick data, which include open, high, low, and close prices, effectively addressing this trade-off. By exploiting the information contained in candlesticks, the proposed method improves estimation accuracy relative to benchmarks while preserving local structure. I further develop a test for spot covariance inference based on candlesticks that demonstrates reasonable size control and a notable increase in power, particularly in small samples. Motivated by recent work in the finance literature, I empirically test the market neutrality of the iShares Bitcoin Trust ETF (IBIT) using 1-minute candlestick data for the full year of 2024. The results show systematic deviations from market neutrality, especially in periods of market stress. An event study around FOMC announcements further illustrates the new method’s ability to detect subtle shifts in response to relatively mild information events.

Keywords: Covariance estimation, high-frequency data, candlesticks, spot beta.

JEL Codes: C13, C32, C58, G11.

## 1 Introduction

The covariance matrix of asset returns is fundamental to many financial applications such as portfolio selection, risk management, and asset pricing, which has led to a large literature on its estimation. A key finding of this literature is that covariances vary substantially over time. High-frequency intraday returns provide an effective means to capture this variation and have enabled more precise estimation over shorter horizons, such as a day or a month (e.g., Aït-Sahalia and Jacod, ([2014](https://arxiv.org/html/2510.12911v1#bib.bib2)), [Bollerslev et al., 2018a](https://arxiv.org/html/2510.12911v1#bib.bib13)  and references therein). Recent evidence shows that covariances also vary significantly within a trading day (e.g., Bibinger et al., ([2019](https://arxiv.org/html/2510.12911v1#bib.bib12)), Andersen et al., ([2021](https://arxiv.org/html/2510.12911v1#bib.bib4))), creating a demand for spot covariance estimates at specific points in time. Constructing such spot estimates, however, relies on returns sampled from narrow time intervals at moderate frequencies. Therefore, it suffers from limited local information and in turn generates a trade-off between statistical precision and localization. Sampling returns at finer frequencies is a natural way to address this trade-off, but doing so introduces market microstructure noise, requiring additional modeling assumptions to form an estimator.

Building on this background, I develop a new estimation framework for spot covariances using an additional source of information to alleviate the localization-precision trade-off. Specifically, my approach leverages the richer information in high-frequency candlesticks that contain the open, high, low, and close prices within each sampling interval, moving beyond the conventional methods that rely solely on (open-to-close) returns. Importantly, this work provides a practical way to improve estimates and enable reliable inference by avoiding intricate modeling assumptions while preserving the local structure of the estimates.

This paper makes three main contributions. First, it introduces a new candlestick-based estimator for spot covariances that exploits all available price information within each interval. This estimator is defined as a weighted sum of quadratic forms based on candlestick variables within a local window. The paper also develops an econometric framework that determines the estimator’s form by minimizing a specific risk function, thereby improving efficiency relative to existing return-only method. Second, it presents a procedure for conducting inference on spot covariances using the new candlestick-based estimator, including a formal hypothesis test with asymptotically correct size. Third, the practical value of the proposed estimator is demonstrated through an empirical application to assess the market neutrality of Bitcoin.222The term “market neutrality” refers to the idea that an asset’s returns do not comove with the overall market returns. Such assets are particularly important for risk management purposes because they can provide diversification benefits. The empirical results show frequent rejections of the null hypothesis of market neutrality, challenging existing beliefs about Bitcoin’s risk exposure.

The proposed candlestick-based estimator has several desirable properties. First, it is derived by minimizing an asymptotic approximation of the risk function. Here, the asymptotic approximation is performed by taking the size of the estimation window (i.e. number of observations in the estimation sample) as a fixed, possibly small constant. As such, my approach effectively accounts for the scarcity of local information. Moreover, the estimator’s form is analytically tractable, resembling the least squares formula and does not depend on the specific sample at hand. This feature makes the estimator readily applicable to various settings without requiring further econometric procedures. I find that my estimator substantially reduces the asymptotic risk relative to the conventional estimators that only use return observations. Crucially, it attains an asymptotic risk comparable to that of standard benchmarks, even when implemented with shorter estimation windows. This makes my approach particularly useful for high-frequency event studies which require high localization for identification (e.g. [Bollerslev et al., 2018b](https://arxiv.org/html/2510.12911v1#bib.bib18) , Nakamura and Steinsson, ([2018](https://arxiv.org/html/2510.12911v1#bib.bib42))).333Specifically, Nakamura and Steinsson, ([2018](https://arxiv.org/html/2510.12911v1#bib.bib42)) exploit high-frequency bond returns over a short window around FOMC announcements to identify the effects of monetary policy shocks. [Bollerslev et al., 2018b](https://arxiv.org/html/2510.12911v1#bib.bib18)  estimate disagreement among investors by local jump regressions around news announcements.

Having established the candlestick-based spot covariance estimator, I further develop a formal procedure for inference on the spot covariance matrix. While recent studies have investigated candlestick-based inference for spot variances (e.g., Li et al., ([2024](https://arxiv.org/html/2510.12911v1#bib.bib35)); [Bollerslev et al., 2024a](https://arxiv.org/html/2510.12911v1#bib.bib14) ), inference methods for spot covariances remain underexplored. To address this gap, I develop a hypothesis test and corresponding test statistic. I show that this test statistic can be approximated by a limiting variable whose distribution can be characterized via Monte Carlo simulations under the null hypothesis. Accordingly, I determine the critical values by simulating the quantiles of the limiting variable. This inference procedure yields a test with asymptotically correct size. Moreover, a finite sample simulation study shows that the proposed test has reasonable size control and a notable increase in power, relative to the return-based test, particularly pronounced in small samples.

Motivated by the recent work of Liu and Tsyvinski, ([2021](https://arxiv.org/html/2510.12911v1#bib.bib38)), I apply the candlestick-based estimation and inference framework to examine the market neutrality of Bitcoin, a popular cryptocurrency. In recent years, cryptocurrencies have become increasingly common in both institutional and retail portfolios.444In 2017, Bitcoin futures were introduced by the Chicago Mercantile Exchange (CME). Later, several cryptocurrency ETFs were launched in January 2024, allowing the investors to gain exposure to different cryptocurrencies such as Bitcoin. However, their market exposure remains a subject of debate among academics and practitioners. Crypto advocates often frame Bitcoin as “digital gold” due to its potential hedging properties. In a similar vein, Liu and Tsyvinski, ([2021](https://arxiv.org/html/2510.12911v1#bib.bib38)) find limited evidence of systematic exposure of crypto assets to the market risk. Using the proposed candlestick-based spot estimator, I provide a more granular approach to this empirical question, offering deeper insights into the risk characteristics of crypto assets.

Specifically, I use 1-minute candlestick observations of the iShares Bitcoin Trust ETF (IBIT) and the SPDR S&P 500 ETF Trust (SPY) as proxies for Bitcoin and the overall market returns, respectively. I collect data for the full year of 2024 to construct spot covariance estimates at a 10-minute frequency.555IBIT is a relatively new financial product that has been traded on the NASDAQ since January 2024. From these, I compute candlestick-based spot beta estimates, defined as the ratio of covariance to variance. I then test the null hypothesis of market neutrality (zero beta) using the test statistics developed in this paper. The null is rejected at the 5% significance level approximately 35% of the time, revealing very different pricing dynamics in the Bitcoin market compared to prior analyses. I also find that rejection rates exceed 50% in August and September 2024, coinciding with heightened financial market turmoil, precisely when the diversification and hedging benefits are most needed.

Along with this analysis, I conduct an event study around two FOMC announcements on June 12 and September 18, 2024. In September, the Federal Reserve cut interest rates by 50 basis points which is the first reduction since the 2022 tightening cycle. Thus, this decision is perceived as a strong dovish signal. Both return-based and candlestick-based estimates reveal that IBIT’s spot beta exhibits no clear pattern before the announcement but increases sharply afterward, reaching approximately 1.5 and remaining statistically significant through the end of the trading day. By contrast, during the June meeting, these two methods responded differently. In this meeting, the Federal Reserve kept rates unchanged as expected but released a relatively hawkish dot plot which suggests less clear signals about future policy paths. Consequently, I find that candlestick-based estimates reject the null immediately after the announcement, while return-based estimates fail to do so. These results highlight the ability of candlestick-based methodology to detect shifts even in response to less informative events.

To improve the estimation, one could alternatively employ tick-level data which provides the most granular information, as it records every single transaction in the market usually at ultra-high frequencies (e.g., milliseconds). However, using tick-level data faces important limitations. First, this data is accessible only to well-resourced researchers since it requires costly subscriptions through commercial providers such as NYSE Trade and Quotes (TAQ) or TickData. Furthermore, prices sampled at such ultra high-frequencies are invariably contaminated by market microstructure noise, which necessitates imposing additional modeling assumptions on the noise structure to obtain enhanced estimates, see for example Diebold and Strasser, ([2013](https://arxiv.org/html/2510.12911v1#bib.bib26)). By contrast, candlestick data is widely accessible through many different public sources at “not-too-fine” frequencies (e.g., 1-minute or 5-minute), which naturally guards against the impact of microstructure noise. From this perspective, my paper adopts a more practical and accessible approach for improving spot covariance estimation.666Within high-frequency econometrics literature, researchers have developed models for the market microstructure noise. Notable references include Hayashi and Yoshida, ([2005](https://arxiv.org/html/2510.12911v1#bib.bib30)); Aït-Sahalia et al., ([2010](https://arxiv.org/html/2510.12911v1#bib.bib1)); Christensen et al., ([2010](https://arxiv.org/html/2510.12911v1#bib.bib21)); Barndorff-Nielsen et al., ([2011](https://arxiv.org/html/2510.12911v1#bib.bib8)). These models can be potentially integrated into my framework. However, this is beyond the scope of this paper and left for future research.

This paper contributes to multiple strands of the literature. From a technical perspective, this paper is closely related to the high-frequency econometrics literature on spot and integrated covariance estimation, see for example [Barndorff-Nielsen and Shephard, 2004a](https://arxiv.org/html/2510.12911v1#bib.bib9) ; Fan and Wang, ([2008](https://arxiv.org/html/2510.12911v1#bib.bib28)); Barndorff-Nielsen et al., ([2009](https://arxiv.org/html/2510.12911v1#bib.bib7)) among many others. These papers develop estimators primarily based on high-frequency returns from open and close prices. This work complements this literature by introducing a new class of estimators for covariances that leverage candlestick observations which extends the information set of high-frequency intervals with high and low prices. Moreover, these papers have primarily considered that the number of high-frequency observations growing asymptotically. However, my approach assumes a fixed estimation window following the recent work of Bollerslev et al., ([2021](https://arxiv.org/html/2510.12911v1#bib.bib16)).

My work is inspired by the range-based volatility estimation literature. Starting from seminal papers by Garman and Klass, ([1980](https://arxiv.org/html/2510.12911v1#bib.bib29)) and Parkinson, ([1980](https://arxiv.org/html/2510.12911v1#bib.bib43)), this literature highlights remarkable efficiency gains in estimating variances by extracting more information from candlestick prices. Notably, Christensen and Podolskij, ([2007](https://arxiv.org/html/2510.12911v1#bib.bib22)) introduces the realized-range estimator for integrated variance, constructed by high-frequency ranges. Later, it is extended to be robust to microstructure noise (Martens and Van Dijk, ([2007](https://arxiv.org/html/2510.12911v1#bib.bib41)); Christensen et al., ([2009](https://arxiv.org/html/2510.12911v1#bib.bib24))); jumps (Christensen and Podolskij, ([2012](https://arxiv.org/html/2510.12911v1#bib.bib23))) and drifts (Li et al., ([2025](https://arxiv.org/html/2510.12911v1#bib.bib36))). More recently, several papers studied spot volatility estimation using candlesticks, see for example Li et al., ([2024](https://arxiv.org/html/2510.12911v1#bib.bib35)), [Bollerslev et al., 2024a](https://arxiv.org/html/2510.12911v1#bib.bib14)  and Bollerslev et al., ([2025](https://arxiv.org/html/2510.12911v1#bib.bib15)). The main focus of these papers is to derive optimal estimation and inference frameworks for spot volatility and its functionals. This paper complements this literature by extending these ideas to multivariate settings.

Perhaps, this paper is most closely related to [Bollerslev et al., 2024a](https://arxiv.org/html/2510.12911v1#bib.bib14)  which develops a decision-theoretic framework to construct optimal estimators for volatility functionals. In their approach, the risk function is asymptotically approximated using pivotal random variables, and the asymptotic risk is minimized through Monte Carlo simulations. However, in multivariate settings, the limiting distributions are generally non-pivotal, which makes direct minimization of a traditional risk function infeasible. To overcome this challenge, I integrate the asymptotic risk to obtain an average risk function which is pivotal, allowing me to determine the optimal estimators by minimizing this objective.

Prior to this study, Brandt and Diebold, ([2006](https://arxiv.org/html/2510.12911v1#bib.bib20)) and Bannouh et al., ([2009](https://arxiv.org/html/2510.12911v1#bib.bib6)) introduced range-based covariance estimators that exploit triangular no-arbitrage conditions in currency markets. While effective in that setting, this is generally not applicable to equity markets. Similarly, Rogers and Zhou, ([2008](https://arxiv.org/html/2510.12911v1#bib.bib45)) estimated the correlation coefficient of a bivariate Brownian motion using open, high, low and close price observations. However, their analysis is conducted under a constant volatility framework. In contrast, this paper accommodates a more general Itô semimartingale environment and provides a feasible inference procedure with candlesticks which is not considered in the abovementioned papers.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2510.12911v1#S2 "2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") introduces the candlestick-based estimation methodology. Section [3](https://arxiv.org/html/2510.12911v1#S3 "3 Spot Beta Estimation and Inference with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") develops the inference procedure. Section [4](https://arxiv.org/html/2510.12911v1#S4 "4 Simulations ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") presents simulation results, and Section [5](https://arxiv.org/html/2510.12911v1#S5 "5 Empirical Application ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") provides empirical applications. Section [6](https://arxiv.org/html/2510.12911v1#S6 "6 Conclusion ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") concludes. Additional technical details and all proofs are provided in the appendices.

## 2 Spot Covariance Estimation with Candlesticks

Section [2.1](https://arxiv.org/html/2510.12911v1#S2.SS1 "2.1 Price Process ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") introduces the underlying price process. Section [2.2](https://arxiv.org/html/2510.12911v1#S2.SS2 "2.2 Observation Scheme and Candlesticks ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") presents the observation scheme and defines the candlestick returns. Section [2.3](https://arxiv.org/html/2510.12911v1#S2.SS3 "2.3 Candlestick-based Estimator ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") proposes a class of new estimators for spot covariance. Then, Section [2.4](https://arxiv.org/html/2510.12911v1#S2.SS4 "2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") solves for the optimal estimator in the proposed class. Finally, Section [2.5](https://arxiv.org/html/2510.12911v1#S2.SS5 "2.5 Discussion ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") discusses the implications.

### 2.1 Price Process

The log-price vector at time tt is denoted by 𝑿t=[X1,t,…,XN,t]⊤\boldsymbol{X}\_{t}=[X\_{1,t},...,X\_{N,t}]^{\top}. Assume that 𝑿t\boldsymbol{X}\_{t} follows an Itô semimartingale process defined on a filtered probability space (Ω,ℱ,(ℱt),ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t}),\mathbb{P}), given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝑿t=𝒃t​d​t+𝝈t​d​𝑾t,d\boldsymbol{X}\_{t}=\boldsymbol{b}\_{t}dt+\boldsymbol{\sigma}\_{t}d\boldsymbol{W}\_{t}, |  | (1) |

where 𝒃t\boldsymbol{b}\_{t} is the drift process, 𝝈t\boldsymbol{\sigma}\_{t} is N×NN\times N stochastic volatility matrix and 𝑾t\boldsymbol{W}\_{t} is an NN-dimensional vector of independent Brownian motions. The spot covariance at time tt is defined as 𝒄t≡𝝈t​𝝈t⊤\boldsymbol{c}\_{t}\equiv\boldsymbol{\sigma}\_{t}\boldsymbol{\sigma}\_{t}^{\top}, where 𝒄t\boldsymbol{c}\_{t} is an N×NN\times N matrix.

The Itô-semimartingale representation in Equation ([1](https://arxiv.org/html/2510.12911v1#S2.E1 "In 2.1 Price Process ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")) can be motivated by no-arbitrage conditions and therefore serves as a workhorse framework in the continuous-time finance literature, see for example Back, ([2010](https://arxiv.org/html/2510.12911v1#bib.bib5)). Consequently, it has become the fundamental model for analyzing high-frequency asset prices; see Jacod and Protter, ([2012](https://arxiv.org/html/2510.12911v1#bib.bib32)) and Aït-Sahalia and Jacod, ([2014](https://arxiv.org/html/2510.12911v1#bib.bib2)) for further discussions. For simplicity, I exclude jumps from the price process.777The estimators discussed in this paper are generally robust to Poisson-type jumps as they occur at vanishing probability, see Theorem 13.3.3 Jacod and Protter, ([2012](https://arxiv.org/html/2510.12911v1#bib.bib32)). Nevertheless, if jumps are a major concern, one can employ truncation (Mancini, ([2009](https://arxiv.org/html/2510.12911v1#bib.bib40))) or bi-power variation ([Barndorff-Nielsen and Shephard, 2004b](https://arxiv.org/html/2510.12911v1#bib.bib10) ) methods to explicitly account for price discontinuities. I do not pursue this direction to present the novelty of the paper with minimal technical complexity.

### 2.2 Observation Scheme and Candlesticks

Suppose that the price process 𝑿t\boldsymbol{X}\_{t} is sampled on a regular time grid, {i​Δn:i=0,1,…,n}\{i\Delta\_{n}:i=0,1,...,n\} over a fixed time span [0,T][0,T]. Here, Δn=T/n\Delta\_{n}=T/n refers to the sampling frequency and nn is the number of observations, assumed to be an integer. High-frequency intervals are denoted by 𝒯i≡[(i−1)​Δn,i​Δn]\mathcal{T}\_{i}\equiv[(i-1)\Delta\_{n},i\Delta\_{n}] for each i∈{1,…,n}i\in\{1,...,n\}. Following the standard practice in the high-frequency financial econometrics literature, I consider an in-fill asymptotic framework where Δn→0\Delta\_{n}\to 0 asymptotically, see for example Aït-Sahalia and Jacod, ([2014](https://arxiv.org/html/2510.12911v1#bib.bib2)).888The choice of Δn\Delta\_{n} is usually guided by volatility signature plots introduced in Andersen et al., ([2000](https://arxiv.org/html/2510.12911v1#bib.bib3)). Following the standard practice in high-frequency econometrics literature, I adopt moderate sampling frequencies like Δn=1,5,10\Delta\_{n}=1,5,10-min in my practical implementations, thereby avoiding ultra high-frequency observations that could be contaminated by microstructure effects.

A typical candlestick over the interval 𝒯i\mathcal{T}\_{i} consists of four observed prices:

|  |  |  |
| --- | --- | --- |
|  | 𝑿(i−1)​Δn,supt∈𝒯i𝑿t,inft∈𝒯i𝑿t,𝑿i​Δn\begin{array}[]{lccr}\boldsymbol{X}\_{(i-1)\Delta\_{n}},&\displaystyle\sup\_{t\in\mathcal{T}\_{i}}\boldsymbol{X}\_{t},&\displaystyle\inf\_{t\in\mathcal{T}\_{i}}\boldsymbol{X}\_{t},&\boldsymbol{X}\_{i\Delta\_{n}}\end{array} |  |

which are called the open, high, low, and close prices, respectively. From these prices, one can construct the following normalized variables:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓i≡𝑿i​Δn−𝑿(i−1)​ΔnΔn,𝒉i≡supt∈𝒯i𝑿t−𝑿(i−1)​ΔnΔn,ℓi≡inft∈𝒯i𝑿t−𝑿(i−1)​ΔnΔn\begin{array}[]{rcl}\boldsymbol{r}\_{i}&\equiv&\frac{\boldsymbol{X}\_{i\Delta\_{n}}-\boldsymbol{X}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}},\\[10.00002pt] \boldsymbol{h}\_{i}&\equiv&\frac{\sup\_{t\in\mathcal{T}\_{i}}\boldsymbol{X}\_{t}-\boldsymbol{X}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}},\\[10.00002pt] \boldsymbol{\ell}\_{i}&\equiv&\frac{\inf\_{t\in\mathcal{T}\_{i}}\boldsymbol{X}\_{t}-\boldsymbol{X}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\end{array} |  | (2) |

where sup\sup and inf\inf operators are applied element-wise. The first line defines the standard high-frequency (open-to-close) return, commonly employed in the literature. The second and third lines indicate the high-open and low-open returns, respectively. These returns stand as a new source of information in this framework. Thus, the bundle (𝒓i,𝒉i,ℓi)(\boldsymbol{r}\_{i},\boldsymbol{h}\_{i},\boldsymbol{\ell}\_{i}) summarizes the price dynamics within the interval 𝒯n,i\mathcal{T}\_{n,i} through the lens of candlesticks.

Following [Bollerslev et al., 2024a](https://arxiv.org/html/2510.12911v1#bib.bib14) , I also define the range and asymmetry variables:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘i≡𝒉i−ℓi,𝒂i≡𝒉i+ℓi−𝒓i.\begin{array}[]{rcl}\boldsymbol{w}\_{i}&\equiv&\boldsymbol{h}\_{i}-\boldsymbol{\ell}\_{i},\\ \boldsymbol{a}\_{i}&\equiv&\boldsymbol{h}\_{i}+\boldsymbol{\ell}\_{i}-\boldsymbol{r}\_{i}.\end{array} |  | (3) |

Figure [1](https://arxiv.org/html/2510.12911v1#S2.F1 "Figure 1 ‣ 2.2 Observation Scheme and Candlesticks ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") presents the graphical representation of the candlestick returns on a typical candlestick chart. Looking at this figure, the range 𝒘i\boldsymbol{w}\_{i} is shown as the vertical distance between the high and low prices, while the return 𝒓i\boldsymbol{r}\_{i} reflects the length of the thick body. The asymmetry 𝒂i\boldsymbol{a}\_{i} indicates the position of the returns (or the thick body) within that range. For example, if 𝒂i=0\boldsymbol{a}\_{i}=0 then the thick body of the candlestick is exactly centered between the high and low prices. On the other hand, if 𝒂i>0\boldsymbol{a}\_{i}>0 then the body is skewed towards the low price, and vice versa.

One can show that (𝒓i,𝒂i,𝒘i)(\boldsymbol{r}\_{i},\boldsymbol{a}\_{i},\boldsymbol{w}\_{i}) is a rotation (i.e., a linear transformation) of (𝒓i,𝒉i,ℓi)(\boldsymbol{r}\_{i},\boldsymbol{h}\_{i},\boldsymbol{\ell}\_{i}), implying that both vectors carry the same information. In this paper, I primarily work with the rotated set (𝒓i,𝒂i,𝒘i)(\boldsymbol{r}\_{i},\boldsymbol{a}\_{i},\boldsymbol{w}\_{i}) to facilitate the analysis, but the proposed methodology can be easily adapted to the original set.

![Refer to caption](Figures/candlestick_chart_example.png)


Figure 1: Illustration of candlestick returns: The figure shows examples of bearish (left panel) and bullish (right panel) candlesticks, illustrating the open, high, low, and close prices. Also it highlights the open-close return 𝒓i\boldsymbol{r}\_{i}, high return 𝒉i\boldsymbol{h}\_{i}, and low return ℓi\boldsymbol{\ell}\_{i} as defined in Equation ([2](https://arxiv.org/html/2510.12911v1#S2.E2 "In 2.2 Observation Scheme and Candlesticks ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")).

### 2.3 Candlestick-based Estimator

The spot covariance matrix 𝒄t\boldsymbol{c}\_{t} can be simply estimated as the local average of the outer products of high-frequency (open-to-close) returns. For any t∈[0,T]t\in[0,T], this can be formally expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1k​∑i∈ℐn,t𝒓i​𝒓i⊤.\frac{1}{k}\sum\_{i\in\mathcal{I}\_{n,t}}\boldsymbol{r}\_{i}\boldsymbol{r}\_{i}^{\top}. |  | (4) |

where ℐn,t={⌈tΔn⌉+1,…,⌈tΔn⌉+k}\mathcal{I}\_{n,t}=\{\lceil\frac{t}{\Delta\_{n}}\rceil+1,\ldots,\lceil\frac{t}{\Delta\_{n}}\rceil+k\} is the local estimation window and kk stands for the size of that window.999Here, ⌈⋅⌉\lceil\cdot\rceil denotes the ceiling function, which maps a real number to the smallest following integer. Thus, ℐn,t\mathcal{I}\_{n,t} can be interpreted as the right-sided local window that contains kk observations after time tt. Alternatively, left-sided or symmetric windows can be considered without changing the main results of the paper. This estimator represents a widely adopted method in the literature; see, among others, Fan and Wang, ([2008](https://arxiv.org/html/2510.12911v1#bib.bib28)).101010The form of the estimator in Equation ([4](https://arxiv.org/html/2510.12911v1#S2.E4 "In 2.3 Candlestick-based Estimator ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")) is slightly different from that of Fan and Wang, ([2008](https://arxiv.org/html/2510.12911v1#bib.bib28)). The standard approach is to let k=knk=k\_{n} grow with nn. However, I consider kk as a constant number, not dependent on nn.

The estimator in Equation ([4](https://arxiv.org/html/2510.12911v1#S2.E4 "In 2.3 Candlestick-based Estimator ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")) relies solely on open-to-close returns and therefore ignores potentially valuable information embedded in other candlestick returns. Thus, I introduce a flexible class of estimators for 𝒄t\boldsymbol{c}\_{t} that incorporates all candlestick returns (𝒓i,𝒂i,𝒘i)(\boldsymbol{r}\_{i},\boldsymbol{a}\_{i},\boldsymbol{w}\_{i}) and combines them through a weighted sum of quadratic forms over a local window. Formally, the estimator is defined as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒄^n,t​(λ)\displaystyle\widehat{\boldsymbol{c}}\_{n,t}(\lambda) | =1k​∑i∈ℐn,t{λ1​𝒓i​𝒓i⊤+λ2​𝒂i​𝒂i⊤+λ3​𝒘i​𝒘i⊤}\displaystyle=\frac{1}{k}\sum\_{i\in\mathcal{I}\_{n,t}}\Big\{\lambda\_{1}\boldsymbol{r}\_{i}\boldsymbol{r}\_{i}^{\top}+\lambda\_{2}\boldsymbol{a}\_{i}\boldsymbol{a}\_{i}^{\top}+\lambda\_{3}\boldsymbol{w}\_{i}\boldsymbol{w}\_{i}^{\top}\vskip-42.67912pt\Big\} |  | (5) |

where λ≡(λ1,λ2,λ3)∈ℝ3\lambda\equiv(\lambda\_{1},\lambda\_{2},\lambda\_{3})\in\mathbb{R}^{3} denote the weights assigned to each component.111111One could also include cross-product terms such as 𝒓i​𝒂i⊤\boldsymbol{r}\_{i}\boldsymbol{a}\_{i}^{\top}. Within the framework of this paper, the optimal weights on such terms turn out to be zero. This is because this set of returns (𝒓i,𝒂i,𝒘i)(\boldsymbol{r}\_{i},\boldsymbol{a}\_{i},\boldsymbol{w}\_{i}) are asymptotically orthogonal to each other. Hence, to simplify the notation, I do not include them in the estimator. The resulting estimator is always symmetric and positive semi-definite whenever λj≥0\lambda\_{j}\geq 0 for all j∈{1,2,3}j\in\{1,2,3\}. The optimal choice of λ\lambda will be determined in subsequent sections according to specific optimality criteria. Importantly, I assume that the size of the estimation window, denoted by kk, is fixed.121212This corresponds to the fixed-kk asymptotic framework introduced by Bollerslev et al., ([2021](https://arxiv.org/html/2510.12911v1#bib.bib16)) and recently extended to candlestick-based spot volatility estimation and inference by Li et al., ([2024](https://arxiv.org/html/2510.12911v1#bib.bib35)). Fixed-kk asymptotics build on coupling (or strong approximation) arguments; see Jacod et al., ([2021](https://arxiv.org/html/2510.12911v1#bib.bib31)). The key idea is that, over short intervals, an Itô semimartingale can be locally approximated by a scaled Brownian motion. This feature allows for determining the (approximate) finite-sample distribution of the estimator under diverging Δn\Delta\_{n}. Bollerslev et al., ([2021](https://arxiv.org/html/2510.12911v1#bib.bib16)) show that fixed-kk asymptotics deliver confidence intervals with more accurate coverage than conventional large-kk approximations, especially in small samples, where the latter often suffer from nontrivial size distortions.

The class of estimators defined in Equation ([5](https://arxiv.org/html/2510.12911v1#S2.E5 "In 2.3 Candlestick-based Estimator ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")) is highly flexible. For example, setting λ=(1,0,0)\lambda=(1,0,0) recovers the standard spot covariance estimator in Equation ([4](https://arxiv.org/html/2510.12911v1#S2.E4 "In 2.3 Candlestick-based Estimator ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")). Moreover, when N=1N=1, the estimator encompasses several well-known candlestick-based spot volatility estimators (e.g., Parkinson, ([1980](https://arxiv.org/html/2510.12911v1#bib.bib43)), Garman and Klass, ([1980](https://arxiv.org/html/2510.12911v1#bib.bib29)), Li et al., ([2024](https://arxiv.org/html/2510.12911v1#bib.bib35))), which have been shown to deliver substantial efficiency gains, yielding more precise estimates and reliable inference.131313For instance, Garman and Klass, ([1980](https://arxiv.org/html/2510.12911v1#bib.bib29)) propose the following estimator for spot variance, among others: c^n,t=−0.3925​ri2+0.0095​ai2+0.5015​wi2\widehat{c}\_{n,t}=-0.3925r\_{i}^{2}+0.0095a\_{i}^{2}+0.5015w\_{i}^{2} which implies λ=(−0.3925,0.0095,0.5015).\lambda=(-0.3925,0.0095,0.5015). From this perspective, the proposed estimator can be viewed as a natural multivariate extension of these univariate methods, thereby generalizing their efficiency benefits to the multivariate setting.

At a first glance, it might be surprising that moments of high and low returns are included in the covariance estimator just like the regular returns. However, there exist a tight connection between the moments of candlestick returns and the underlying correlation structure. To illustrate this, consider a price process 𝑿t\boldsymbol{X}\_{t} generated by a bivariate Brownian motion with unit volatilities and constant correlation coefficient ρ\rho.141414This special case considers N=2N=2 assets and implies following specifications for Ito-semimartingale process in Equation ([1](https://arxiv.org/html/2510.12911v1#S2.E1 "In 2.1 Price Process ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")): 𝒃t=0\boldsymbol{b}\_{t}=0 and 𝒄t\boldsymbol{c}\_{t} is unit diagonal matrix with off-diagonal elements given by ρ\rho. Denote the correlations between the candletick returns by ρr,ρa,ρw\rho\_{r},\rho\_{a},\rho\_{w}. Clearly, it holds that ρr=ρ\rho\_{r}=\rho. As shown by Rogers and Shepp, ([2006](https://arxiv.org/html/2510.12911v1#bib.bib44)), the correlation of range and asymmetry variables (ρa,ρw\rho\_{a},\rho\_{w}) are smooth and nonlinear functions of ρ\rho. Figure [2](https://arxiv.org/html/2510.12911v1#S2.F2 "Figure 2 ‣ 2.3 Candlestick-based Estimator ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") illustrates this relationship. Notably, ρw\rho\_{w} is symmetric around zero, while ρa\rho\_{a} closely follows 4545-degree line. This figure thus suggests that the cross moments of candlestick returns may contain valuable information about the underlying correlation structure.

![Refer to caption](x1.png)


Figure 2: Cross moments of candlestick returns: The figure illustrates the relationship between the correlation of open-close returns ρr\rho\_{r} (blue) and that of asymmetry ρa\rho\_{a} (red) and range ρw\rho\_{w} (green) variables, respectively. The underlying price process is assumed to be a bivariate Brownian motion with unit volatilities and constant correlation coefficient ρ\rho.

### 2.4 Finding the “Optimal” Weights

The primary objective of this paper is to construct an estimator that efficiently exploits the information contained in candlestick features. To this end, the optimal weighting scheme λ\lambda is determined by minimizing a suitably defined risk function, which serves to quantify the estimation error. In what follows, I first provide a detailed discussion of the loss criterion underlying this risk function.

#### 2.4.1 Loss Function

I adopt the following quadratic loss function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(λ;𝒄t)=‖𝝈t−1​𝒄^n,t​(λ)​𝝈t−1⊤−𝐈‖2L(\lambda;{\boldsymbol{c}}\_{t})=\left\|\boldsymbol{\sigma}\_{t}^{-1}\widehat{\boldsymbol{c}}\_{n,t}(\lambda)\boldsymbol{\sigma}\_{t}^{-1\top}-\mathbf{I}\right\|^{2} |  | (6) |

where ||⋅||||\cdot|| denotes the Frobenius norm and 𝐈\mathbf{I} is the identity matrix. Recall that 𝒄t\boldsymbol{c}\_{t} and 𝝈t\boldsymbol{\sigma}\_{t} denote the true spot covariance and volatility matrices at a fixed time point tt, respectively, and 𝒄^n,t\widehat{\boldsymbol{c}}\_{n,t} is the estimator defined in Equation ([5](https://arxiv.org/html/2510.12911v1#S2.E5 "In 2.3 Candlestick-based Estimator ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")).

The term 𝝈t−1​𝒄^n,t​𝝈t−1⊤\boldsymbol{\sigma}\_{t}^{-1}\,\widehat{\boldsymbol{c}}\_{n,t}\,\boldsymbol{\sigma}\_{t}^{-1\top} captures the multiplicative estimation error of the spot covariance matrix relative to the identity, naturally inducing a scale-invariant loss function. This property is particularly desirable, as covariance matrices represent scale parameters. In the univariate setting (N=1)(N=1), the loss reduces to

|  |  |  |
| --- | --- | --- |
|  | (c^n,tct−1)2,\left(\frac{\widehat{c}\_{n,t}}{c\_{t}}-1\right)^{2}, |  |

which corresponds to the relative squared error that has been previously analyzed in the context of volatility estimation with candlestick data by Li et al., ([2024](https://arxiv.org/html/2510.12911v1#bib.bib35)).

Accordingly, one can naturally define the risk of the estimator 𝒄^n,t\widehat{\boldsymbol{c}}\_{n,t} as the conditional expectation of the loss function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(λ;𝒄t)≡𝔼​[L​(λ;𝒄t)∣ℱt].R(\lambda;\boldsymbol{c}\_{t})\equiv\mathbb{E}\left[L(\lambda;\boldsymbol{c}\_{t})\mid\mathcal{F}\_{t}\right]. |  | (7) |

This quantifies the exact finite sample risk of an estimator. For a given λ\lambda, the risk depends on the joint distribution of (𝒓i,𝒂i,𝒘i)(\boldsymbol{r}\_{i},\boldsymbol{a}\_{i},\boldsymbol{w}\_{i}) which in turn is determined by the law of (𝒃,𝝈,𝑾)(\boldsymbol{b},\boldsymbol{\sigma},\boldsymbol{W}). Since this law is unknown, the estimation of λ\lambda with direct minimization of R​(λ;𝝈t)R(\lambda;\boldsymbol{\sigma}\_{t}) is infeasible in practice.

To simplify the analysis, I first establish, in the next subsection, an asymptotic approximation of the multiplicative estimation error 𝝈t−1​𝒄^n,t​𝝈t−1⊤\boldsymbol{\sigma}\_{t}^{-1}\widehat{\boldsymbol{c}}\_{n,t}\boldsymbol{\sigma}\_{t}^{-1\top} using coupling arguments (see, e.g., Jacod et al., ([2021](https://arxiv.org/html/2510.12911v1#bib.bib31))). This characterization is subsequently extended to the loss function and, in turn, to the risk. The resulting asymptotic risk functional is then used to determine the optimal weights 𝚲\boldsymbol{\Lambda}.

#### 2.4.2 Asymptotic Approximation for the Risk Function

The assumption below gathers a set of regularity conditions, required for the asymptotic approximation results.

###### Assumption 1.

Suppose that 𝐗t\boldsymbol{X}\_{t} has the form in Equation ([1](https://arxiv.org/html/2510.12911v1#S2.E1 "In 2.1 Price Process ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")) and there exists a sequence (Tm)m≥1(T\_{m})\_{m\geq 1} of stopping times increasing to infinity and the following conditions hold for each m≥1m\geq 1:

* (i)

  ‖𝒃t‖+‖𝝈t‖+‖𝝈t−1‖≤Km\|\boldsymbol{b}\_{t}\|+\|\boldsymbol{\sigma}\_{t}\|+\|\boldsymbol{\sigma}\_{t}^{-1}\|\leq K\_{m} for some constant KmK\_{m} for all t∈[0,Tm]t\in[0,T\_{m}];
* (ii)

  𝔼​[‖𝝈t∧Tm−𝝈s∧Tm‖2]≤Km​|t−s|\mathbb{E}\left[\|\boldsymbol{\sigma}\_{t\wedge T\_{m}}-\boldsymbol{\sigma}\_{s\wedge T\_{m}}\|^{2}\right]\leq K\_{m}|t-s| for all t,s∈[0,Tm]t,s\in[0,T\_{m}].

These conditions are quite standard in the high-frequency econometrics literature; see, for example, Jacod and Protter, ([2012](https://arxiv.org/html/2510.12911v1#bib.bib32)) for further details. The first part of the Assumption [1](https://arxiv.org/html/2510.12911v1#Thmassumption1 "Assumption 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") implies local boundedness of the drift, volatility, and inverse volatility processes while the second part ensures a degree of smoothness in the volatility process, specifically called as locally 1/21/2-Hölder continuous. These assumptions are sufficiently general to accommodate a wide range of volatility dynamics, including volatility jumps, leverage effects, and intraday seasonality. For example, they are satisfied if the volatility process is itself an Itô semimartingale or long-memory process driven by fractional Brownian motion.

The following proposition describes the key approximation result for the estimation error 𝝈t−1​𝒄^n,t​𝝈t−1⊤\boldsymbol{\sigma}\_{t}^{-1}\widehat{\boldsymbol{c}}\_{n,t}\boldsymbol{\sigma}\_{t}^{-1\top}. The proof is deferred to Appendix [A.1](https://arxiv.org/html/2510.12911v1#A1.SS1 "A.1 Proof of Proposition 1 ‣ Appendix Appendix A ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.").

###### Proposition 1.

Suppose that Assumption [1](https://arxiv.org/html/2510.12911v1#Thmassumption1 "Assumption 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") holds. Fix any t∈[0,T]t\in[0,T]. For any k≥1k\geq 1 and 𝚲\boldsymbol{\Lambda}, the following holds as Δn→0\Delta\_{n}\to 0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝝈t−1​𝒄^n,t​(𝚲)​𝝈t−⊤−Un,t​(λ)‖=op​(1)\left\|\boldsymbol{\sigma}\_{t}^{-1}\widehat{\boldsymbol{c}}\_{n,t}(\boldsymbol{\Lambda})\boldsymbol{\sigma}\_{t}^{-\top}-U\_{n,t}(\lambda)\right\|=o\_{p}(1) |  | (8) |

where Un,t​(λ)=1k​∑i∈ℐn,t{λ1​𝛇i,r​𝛇i,r⊤+λ2​𝛇i,a​𝛇i,a⊤+λ3​𝛇i,w​𝛇i,w⊤}U\_{n,t}(\lambda)=\frac{1}{k}\sum\_{i\in\mathcal{I}\_{n,t}}\Big\{\lambda\_{1}\boldsymbol{\zeta}\_{i,r}\boldsymbol{\zeta}\_{i,r}^{\top}+\lambda\_{2}\boldsymbol{\zeta}\_{i,a}\boldsymbol{\zeta}\_{i,a}^{\top}+\lambda\_{3}\boldsymbol{\zeta}\_{i,w}\boldsymbol{\zeta}\_{i,w}^{\top}\Big\} and, for any i∈ℐn,ti\in\mathcal{I}\_{n,t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜻i,r≡𝑾i​Δn−𝑾(i−1)​ΔnΔn𝜻i,a≡ϱt−1​supτ∈𝒯i​ϱt​(𝑾τ−𝑾(i−1)​ΔnΔn)+ϱt−1​infτ∈𝒯i​ϱt​(𝑾τ−𝑾(i−1)​ΔnΔn)−(𝑾i​Δn−𝑾(i−1)​ΔnΔn)𝜻i,w≡ϱt−1​supτ∈𝒯i​ϱt​(𝑾τ−𝑾(i−1)​ΔnΔn)−ϱt−1​infτ∈𝒯i​ϱt​(𝑾τ−𝑾(i−1)​ΔnΔn)\begin{array}[]{rcl}\boldsymbol{\zeta}\_{i,r}&\equiv&\frac{\boldsymbol{W}\_{i\Delta\_{n}}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\\ \boldsymbol{\zeta}\_{i,a}&\equiv&\boldsymbol{\varrho}\_{t}^{-1}\underset{\tau\in\mathcal{T}\_{i}}{\sup\>}\boldsymbol{\varrho}\_{t}\left(\frac{\boldsymbol{W}\_{\tau}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)+\boldsymbol{\varrho}\_{t}^{-1}\underset{\tau\in\mathcal{T}\_{i}}{\inf\>}\boldsymbol{\varrho}\_{t}\left(\frac{\boldsymbol{W}\_{\tau}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)-\left(\frac{\boldsymbol{W}\_{i\Delta\_{n}}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)\\ \boldsymbol{\zeta}\_{i,w}&\equiv&\boldsymbol{\varrho}\_{t}^{-1}\underset{\tau\in\mathcal{T}\_{i}}{\sup\>}\boldsymbol{\varrho}\_{t}\left(\frac{\boldsymbol{W}\_{\tau}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)-\boldsymbol{\varrho}\_{t}^{-1}\underset{\tau\in\mathcal{T}\_{i}}{\inf\>}\boldsymbol{\varrho}\_{t}\left(\frac{\boldsymbol{W}\_{\tau}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)\\ \end{array} |  | (9) |

with ϱt\boldsymbol{\varrho}\_{t} being the square root of spot correlation matrix 𝛒t\boldsymbol{\rho}\_{t}, i.e., 𝛒t=ϱt​ϱt⊤\boldsymbol{\rho}\_{t}=\boldsymbol{\varrho}\_{t}\boldsymbol{\varrho}\_{t}^{\top}.151515In explicit terms, 𝛒t=diag(𝐜t)−12𝐜tdiag(𝐜t)−12\boldsymbol{\rho}\_{t}=\operatorname{diag}(\boldsymbol{c}\_{t})^{-\frac{1}{2}}\boldsymbol{c}\_{t}\operatorname{diag}(\boldsymbol{c}\_{t})^{-\frac{1}{2}} and ϱt=diag(𝐜t)−12𝛔t\boldsymbol{\varrho}\_{t}=\operatorname{diag}(\boldsymbol{c}\_{t})^{-\frac{1}{2}}\boldsymbol{\sigma}\_{t} where diag⁡(𝐜t)\operatorname{diag}(\boldsymbol{c}\_{t}) is a diagonal matrix with the same diagonal elements as 𝐜t\boldsymbol{c}\_{t}. All inf\inf and sup\sup operators are applied element-wise.

Proposition [1](https://arxiv.org/html/2510.12911v1#Thmproposition1 "Proposition 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") establishes that the multiplicative estimation error of the spot covariance estimator 𝒄^n,t​(λ)\widehat{\boldsymbol{c}}\_{n,t}(\lambda) is asymptotically approximated by the random matrix Un,tU\_{n,t} in probability as Δn→0\Delta\_{n}\to 0. The structure of Un,tU\_{n,t} mirrors that of the original estimator, with the candlestick returns replaced by the variables 𝜻i\boldsymbol{\zeta}\_{i}s. These variables are functions of Brownian motion 𝑾\boldsymbol{W} and square root of spot correlation matrix ϱt\boldsymbol{\varrho}\_{t}. In addition, the approximation error (op​(1)o\_{p}(1) term) captures nonparametric biases arising from stochastic volatility and drift. Put differently, in the limiting case of constant volatility and vanishing drift, the relationship in Proposition [1](https://arxiv.org/html/2510.12911v1#Thmproposition1 "Proposition 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") holds exactly rather than approximately.

Using Proposition [1](https://arxiv.org/html/2510.12911v1#Thmproposition1 "Proposition 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") and the conditions stated therein, analogous approximations apply to the loss and risk functions. Since the loss function is continuous, the continuous mapping theorem implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(λ;𝒄t)=‖Un,t​(λ)−𝐈‖2+op​(1).L(\lambda;\boldsymbol{c}\_{t})=\left\|U\_{n,t}(\lambda)-\mathbf{I}\right\|^{2}+o\_{p}(1). |  | (10) |

This relation can similarly be extended to the risk function by taking the conditional expectation of both sides given ℱt\mathcal{F}\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(λ;𝒄t)=𝔼​[‖Un,t​(λ)−𝑰‖2∣ℱt]⏟R~​(λ;𝝆t)+op​(1){R}(\lambda;\boldsymbol{c}\_{t})=\underbrace{\mathbb{E}\left[\left\|U\_{n,t}(\lambda)-\boldsymbol{I}\right\|^{2}\mid\mathcal{F}\_{t}\right]}\_{\widetilde{R}(\lambda;\boldsymbol{\rho}\_{t})}+o\_{p}(1) |  | (11) |

where R~​(λ;𝝆t)\widetilde{R}(\lambda;\boldsymbol{\rho}\_{t}) is the asymptotic risk of the estimator 𝒄^n,t\widehat{\boldsymbol{c}}\_{n,t}.161616This step requires an additional uniform integrability condition to interchange the limit and expectation operators. This condition is satisfied under the assumptions stated in Assumption [1](https://arxiv.org/html/2510.12911v1#Thmassumption1 "Assumption 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."). Importantly, I switch to notation R~​(λ;𝝆t)\widetilde{R}(\lambda;\boldsymbol{\rho}\_{t}) to emphasize that the asymptotic risk depends on the spot correlation matrix 𝝆t\boldsymbol{\rho}\_{t} rather than the spot covariance matrix 𝒄t\boldsymbol{c}\_{t}. This is because the risk formula involves a term, Un,tU\_{n,t}, which depends on ϱt\boldsymbol{\varrho}\_{t}, i.e., the square root of the spot correlation matrix. The use of the Frobenius norm in the final calculation effectively considers the product ϱt​ϱt⊤\boldsymbol{\varrho}\_{t}\boldsymbol{\varrho}\_{t}^{\top}, making the risk solely dependent on 𝝆t\boldsymbol{\rho}\_{t}.

The above expressions indicate that the asymptotic risk of an estimator is determined by the ℱt\mathcal{F}\_{t}-conditional distribution of the term Un,tU\_{n,t}. In the univariate case, i.e. N=1N=1, this conditional distribution is pivotal, see Theorem 1 in Li et al., ([2024](https://arxiv.org/html/2510.12911v1#bib.bib35)). In contrast, this does not hold in the multivariate setting, as Un,tU\_{n,t} depends on 𝝆t\boldsymbol{\rho}\_{t}, a population quantity that is unknown to the researcher.

To build intuition, consider the structure of Un,tU\_{n,t}, which is derived from the variables (𝜻i,r,𝜻i,a,𝜻i,w)(\boldsymbol{\zeta}\_{i,r},\boldsymbol{\zeta}\_{i,a},\boldsymbol{\zeta}\_{i,w}). By the scaling property of Brownian motion, 𝜻i,r\boldsymbol{\zeta}\_{i,r} is standard normally distributed and therefore naturally pivotal. However, the remaining variables, 𝜻i,a\boldsymbol{\zeta}\_{i,a} and 𝜻i,w\boldsymbol{\zeta}\_{i,w}, depend on ϱt\boldsymbol{\varrho}\_{t} in a nontrivial manner. This dependence arises because the supremum and infimum operators are nonlinear, preventing the scaling by ϱt\boldsymbol{\varrho}\_{t} and its inverse from canceling. Consequently, the distribution of Un,tU\_{n,t} is generally not free from ϱt\boldsymbol{\varrho}\_{t}. In the univariate case, by contrast, the terms 𝜻i,a\boldsymbol{\zeta}\_{i,a} and 𝜻i,w\boldsymbol{\zeta}\_{i,w} reduce to functions of standard Brownian motion increments. This is because the scaling by ϱt\boldsymbol{\varrho}\_{t} and its inverse cancels, as they become scalars, allowing the distribution of these terms to be fully characterized through simulations of Brownian motion functionals. Consequently, the asymptotic risk can be computed directly from this simulated distribution. Such pivotality considerably simplifies the derivation of optimal estimators via risk minimization; see Li et al., ([2024](https://arxiv.org/html/2510.12911v1#bib.bib35)) and [Bollerslev et al., 2024a](https://arxiv.org/html/2510.12911v1#bib.bib14)  for further discussion. In this sense, the multivariate volatility estimation problem studied here departs from the standard univariate frameworks and requires a more intricate treatment.

#### 2.4.3 Average Risk Minimization

To address the non-pivotal nature of the asymptotic risk in the multivariate setting, I propose marginalizing over the unobserved quantities and working with the resulting *average risk*. This approach is directly inspired by the classical decision theory literature, see for example Lehmann and Casella, ([2006](https://arxiv.org/html/2510.12911v1#bib.bib33)), which advocates the use of integrated risk functions to handle nuisance parameters.

Let 𝒫\mathcal{P} denote the parameter space for positive semidefinite correlation matrices.171717When N=2N=2, 𝒫\mathcal{P} is simply all possible 2×22\times 2 correlation matrices. Then define the average risk R¯​(λ)\bar{R}(\lambda) by integrating R~\widetilde{R} over 𝒫\mathcal{P}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R¯​(λ)≡∫𝒫R~​(λ;𝝆)​𝑑𝝆.\bar{R}(\lambda)\equiv\int\_{\mathcal{P}}\widetilde{R}(\lambda;\boldsymbol{\rho})d\boldsymbol{\rho}. |  | (12) |

For any fixed λ\lambda, the mapping 𝝆↦R~​(λ;𝝆)\boldsymbol{\rho}\mapsto\widetilde{R}(\lambda;\boldsymbol{\rho}) can be computed via Monte Carlo simulation. This in turn allows for the determination of the weights λ\lambda by solving the following optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∗=arg⁡minλ⁡R¯​(λ).\lambda^{\*}=\arg\min\_{\lambda}\bar{R}(\lambda). |  | (13) |

The solution to this optimization problem is available in closed form. To see this, rewrite the explicit form of the average risk R¯​(λ)\bar{R}(\lambda) by applying the half-vectorization operator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫𝒫𝔼​[‖1k​∑i∈ℐn,t{λ1​vech⁡(𝜻i,r​𝜻i,r⊤)+λ2​vech⁡(𝜻i,h​𝜻i,a⊤)+λ3​vech⁡(𝜻i,w​𝜻i,w⊤)}−vech⁡(𝐈)‖2|ℱt]​𝑑ϱ\int\_{\mathcal{P}}\mathbb{E}\left[\Big\|\frac{1}{k}\sum\_{i\in\mathcal{I}\_{n,t}}\Big\{\lambda\_{1}\operatorname{vech}(\boldsymbol{\zeta}\_{i,r}\boldsymbol{\zeta}\_{i,r}^{\top})+\lambda\_{2}\operatorname{vech}(\boldsymbol{\zeta}\_{i,h}\boldsymbol{\zeta}\_{i,a}^{\top})+\lambda\_{3}\operatorname{vech}(\boldsymbol{\zeta}\_{i,w}\boldsymbol{\zeta}\_{i,w}^{\top})\Big\}-\operatorname{vech}(\mathbf{I})\Big\|^{2}|\mathcal{F}\_{t}\right]d\boldsymbol{\varrho} |  | (14) |

Next, stack the vectorized terms into a single matrix:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚷≡[⋮⋮⋮1k​∑ivech⁡(𝜻i,r​𝜻i,r⊤)1k​∑ivech⁡(𝜻i,a​𝜻i,a⊤)1k​∑ivech⁡(𝜻i,w​𝜻i,w⊤)⋮⋮⋮]\boldsymbol{\Pi}\equiv\begin{bmatrix}\vdots&\vdots&\vdots\\ \frac{1}{k}\sum\_{i}\operatorname{vech}(\boldsymbol{\zeta}\_{i,r}\boldsymbol{\zeta}\_{i,r}^{\top})&\frac{1}{k}\sum\_{i}\operatorname{vech}(\boldsymbol{\zeta}\_{i,a}\boldsymbol{\zeta}\_{i,a}^{\top})&\frac{1}{k}\sum\_{i}\operatorname{vech}(\boldsymbol{\zeta}\_{i,w}\boldsymbol{\zeta}\_{i,w}^{\top})\\ \vdots&\vdots&\vdots\end{bmatrix} |  | (15) |

where 𝚷\boldsymbol{\Pi} is a N​(N+1)2×3\frac{N(N+1)}{2}\times 3 matrix. Then, the average risk may be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R¯​(λ)=∫𝒫𝔼​[‖𝚷​λ−𝒚‖2|ℱt]​𝑑𝝆\bar{R}(\lambda)=\int\_{\mathcal{P}}\mathbb{E}\left[\Big\|\boldsymbol{\Pi}\>\lambda-\boldsymbol{y}\Big\|^{2}|\mathcal{F}\_{t}\right]d\boldsymbol{\rho} |  | (16) |

in which 𝒚=vech⁡(𝐈)\boldsymbol{y}=\operatorname{vech}(\mathbf{I}). This representation resembles a standard least-squares estimation problem, allowing for a closed-form solution. Consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∗=(∫𝒫𝔼​[𝚷⊤​𝚷|ℱt]​𝑑𝝆)−1​(∫𝒫𝔼​[𝚷⊤​𝒚|ℱt]​𝑑𝝆).\lambda^{\*}=\left(\int\_{\mathcal{P}}{\mathbb{E}}[\boldsymbol{\Pi}^{\top}\boldsymbol{\Pi}|\mathcal{F}\_{t}]d\boldsymbol{\rho}\right)^{-1}\left(\int\_{\mathcal{P}}{\mathbb{E}}[\boldsymbol{\Pi}^{\top}\boldsymbol{y}|\mathcal{F}\_{t}]d\boldsymbol{\rho}\right). |  | (17) |

Finally, the numerical computation of λ∗\lambda^{\*} proceeds as follows:

* Step 1.

  Uniformly draw 𝝆\boldsymbol{\rho} from the parameter space 𝒫\mathcal{P}.181818For N=2N=2, this corresponds to drawing the correlation coefficient ρ\rho uniformly from (−1,1)(-1,1). When N>2N>2, one can use the distribution developed by Lewandowski et al., ([2009](https://arxiv.org/html/2510.12911v1#bib.bib34)) which allows for uniform sampling of correlation matrices. The implementation of this procedure is available in the programming languages like R and Python.
* Step 2.

  For the given 𝝆\boldsymbol{\rho}, compute the conditional expectation 𝔼[⋅∣𝝆]\mathbb{E}[\cdot\mid\boldsymbol{\rho}] using Monte Carlo simulation.
* Step 3.

  Repeat Steps 1–2 over a large number of draws and average the resulting estimates to approximate R¯​(λ)\bar{R}(\lambda).
* Step 4.

  Plug the resulting approximation of R¯​(λ)\bar{R}(\lambda) into Equation ([13](https://arxiv.org/html/2510.12911v1#S2.E13 "In 2.4.3 Average Risk Minimization ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")) and solve for λ∗\lambda^{\*}.

The above numerical procedure applies for all values of kk, estimation window size, and NN, number of assets. For clarity, I focus on the case of N=2N=2 in my practical implementations. The optimal weights λ∗\lambda^{\*} for different local window sizes k∈{5,10,20}k\in\{5,10,20\} are given by in Equation ([18](https://arxiv.org/html/2510.12911v1#S2.E18 "In 2.4.3 Average Risk Minimization ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∗={(0.4106, 1.4550, 0.0013)⊤if ​k=5,(0.4725, 1.6280, 0.0002)⊤if ​k=10,(0.5176, 1.7039, 0.0001)⊤if ​k=20.\lambda^{\*}=\begin{cases}\big(0.4106,\ 1.4550,\ 0.0013\big)^{\top}&\text{if }k=5,\\[6.0pt] \big(0.4725,\ 1.6280,\ 0.0002\big)^{\top}&\text{if }k=10,\\[6.0pt] \big(0.5176,\ 1.7039,\ 0.0001\big)^{\top}&\text{if }k=20.\end{cases} |  | (18) |

### 2.5 Discussion

The resulting estimator 𝒄^n,t​(λ∗)\widehat{\boldsymbol{c}}\_{n,t}(\lambda^{\*}) aligns with the broader motivation of candlestick-based estimators to be straightforward to implement, as the weights in the linear combination can be computed once and subsequently reused across different settings without the need for complex statistical or econometric procedures.

When defining the average risk, the integration over 𝒫\mathcal{P} is performed uniformly which also induces a uniform marginal distribution for the correlation parameter. This may appear simplistic, and alternative choices including more flexible distributional assumptions or those informed by the historical data and expert judgment could be certainly considered. Nevertheless, the asymptotic risk comparisons presented in Section [4.1](https://arxiv.org/html/2510.12911v1#S4.SS1 "4.1 Asymptotic Risk of the Estimators ‣ 4 Simulations ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") reveals that this approach performs nearly as well as oracle estimators, leaving limited potential improvement through alternative specifications. Moreover, solving this optimization problem for λ\lambda does not inherently depend on uniform integration. As such, the optimal weights can be obtained for any given marginal distribution of 𝝆\boldsymbol{\rho} following the same computational steps.

An estimator of this form, a linear combination of 𝒓i​𝒓i⊤\boldsymbol{r}\_{i}\boldsymbol{r}\_{i}^{\top} and 𝒂i​𝒂i⊤\boldsymbol{a}\_{i}\boldsymbol{a}\_{i}^{\top}, was previously studied by Rogers and Zhou, ([2008](https://arxiv.org/html/2510.12911v1#bib.bib45)) for the purpose of estimating the correlation between two Brownian motions. Their analysis assumes that the price process follows a scaled Brownian motion and determines the weights by minimizing the variance of the estimation error, subject to an unbiasedness constraint under the assumption of zero correlation. By contrast, my approach is formulated within a general Itô-semimartingale framework and selects the weights by minimizing the average risk of the estimation error without imposing any restrictions on the correlation structure. Moreover, an inference procedure is developed in the next section that enables hypothesis testing for spot covariances, whereas Rogers and Zhou, ([2008](https://arxiv.org/html/2510.12911v1#bib.bib45)) focus exclusively on point estimation.

## 3 Spot Beta Estimation and Inference with Candlesticks

In this section, I study inference on spot covariances using the candlestick-based estimator introduced in the previous section. While prior work has focused on inference for spot volatilities using candlesticks (see, e.g., Li et al., ([2024](https://arxiv.org/html/2510.12911v1#bib.bib35)); [Bollerslev et al., 2024a](https://arxiv.org/html/2510.12911v1#bib.bib14) ), the problem of conducting inference on covariance terms remains unexplored. To address this gap, I propose a hypothesis testing procedure. In particular, I focus on spot betas, defined as the ratio of covariance to variance, which naturally arise as a by-product of spot covariance estimation. Focusing on betas is practically relevant as these quantities are widely employed in asset pricing and portfolio management to measure systematic risk.

### 3.1 Candlestick-Beta Estimator

To fix ideas, I focus on the N=2N=2 case and tailor the price process 𝑿t=[X1,t,X2,t]⊤\boldsymbol{X}\_{t}=[X\_{1,t},X\_{2,t}]^{\top} to the following regression representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​X1,t=νt1/2​d​W1,td​X2,t=βt​d​X1,t+ςt1/2​d​W2,t.\begin{array}[]{rcl}d{X}\_{1,t}&=&\nu\_{t}^{1/2}dW\_{1,t}\\ d{X}\_{2,t}&=&\beta\_{t}d{X}\_{1,t}+\varsigma^{1/2}\_{t}dW\_{2,t}.\end{array} |  | (19) |

where 𝑾=[W1,t,W2,t]⊤\boldsymbol{W}=[W\_{1,t},W\_{2,t}]^{\top} is a standard bivariate Brownian motion. This is also equivalent to assuming the following spot covariance structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒄t=(νtβt​νtβt​νtβt2​νt+ςt)and𝝈t=(νt1/20βt​νt1/2ςt1/2).\boldsymbol{c}\_{t}=\begin{pmatrix}\nu\_{t}&\beta\_{t}\nu\_{t}\\ \beta\_{t}\nu\_{t}&\beta\_{t}^{2}\nu\_{t}+\varsigma\_{t}\end{pmatrix}\quad\text{and}\quad\boldsymbol{\sigma}\_{t}=\begin{pmatrix}\nu\_{t}^{1/2}&0\\ \beta\_{t}\nu\_{t}^{1/2}&\varsigma\_{t}^{1/2}\end{pmatrix}. |  | (20) |

Through the lens of factor models in asset pricing literature (e.g., Sharpe, ([1964](https://arxiv.org/html/2510.12911v1#bib.bib47)); Lintner, ([1965](https://arxiv.org/html/2510.12911v1#bib.bib37)); Fama and French, ([1992](https://arxiv.org/html/2510.12911v1#bib.bib27))), one can consider the first asset as the market portfolio and the second asset as a risky asset. Then, νt\nu\_{t} and ςt\varsigma\_{t} refer to the market and idiosyncratic variances, respectively. Finally, βt\beta\_{t} indicates the market beta of the risky asset.

From the above, it is clear that βt=𝒄12,t𝒄11,t\beta\_{t}=\frac{\boldsymbol{c}\_{12,t}}{\boldsymbol{c}\_{11,t}} and therefore, naturally suggesting the spot beta estimator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β^n,t​(𝚲)=[𝒄^n,t​(𝚲)]12[𝒄^n,t​(𝚲)]11.\widehat{\beta}\_{n,t}(\boldsymbol{\Lambda})=\frac{\left[\widehat{\boldsymbol{c}}\_{n,t}(\boldsymbol{\Lambda})\right]\_{12}}{\left[\widehat{\boldsymbol{c}}\_{n,t}(\boldsymbol{\Lambda})\right]\_{11}}. |  | (21) |

where the notation [⋅]i​j[\cdot]\_{ij} refers to the (i,j)(i,j)-th entry of a matrix. This defines a candlestick-based spot beta estimator, hereafter referred to as the *candlestick-beta* estimator.

### 3.2 Testing on Spot Beta

I consider the following test statistics:

|  |  |  |
| --- | --- | --- |
|  | T^n=k−1​(β^n,t−βt)ς^n,t/ν^n,t\widehat{T}\_{n}=\frac{\sqrt{k-1}\left(\widehat{\beta}\_{n,t}-\beta\_{t}\right)}{\sqrt{\widehat{\varsigma}\_{n,t}/\widehat{\nu}\_{n,t}}} |  |

where ν^n,t=[𝒄^n,t​(𝚲)]11\widehat{\nu}\_{n,t}=[\widehat{\boldsymbol{c}}\_{n,t}(\boldsymbol{\Lambda})]\_{11} and ς^n,t=[𝒄^n,t​(𝚲)]22−[𝒄^n,t​(𝚲)]122[𝒄^n,t​(𝚲)]11\widehat{\varsigma}\_{n,t}=[\widehat{\boldsymbol{c}}\_{n,t}(\boldsymbol{\Lambda})]\_{22}-\frac{[\widehat{\boldsymbol{c}}\_{n,t}(\boldsymbol{\Lambda})]\_{12}^{2}}{[\widehat{\boldsymbol{c}}\_{n,t}(\boldsymbol{\Lambda})]\_{11}}.

Similar to spot covariance estimation, one can establish an asymptotic approximation to T^n\widehat{T}\_{n} using the coupling variable Un,tU\_{n,t} defined in Proposition [1](https://arxiv.org/html/2510.12911v1#Thmproposition1 "Proposition 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."). This result is summarized in the following proposition. Proof is provided in Appendix [A.2](https://arxiv.org/html/2510.12911v1#A1.SS2 "A.2 Proof of Proposition 2 ‣ Appendix Appendix A ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.").

###### Proposition 2.

Suppose that the conditions of Proposition 1 holds and 𝐗t\boldsymbol{X}\_{t} follows Equation ([19](https://arxiv.org/html/2510.12911v1#S3.E19 "In 3.1 Candlestick-Beta Estimator ‣ 3 Spot Beta Estimation and Inference with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")). Then, for any fixed k≥2k\geq 2 and λ\lambda, the following holds as Δn→0\Delta\_{n}\to 0:

|  |  |  |
| --- | --- | --- |
|  | |T^n−T~n|=op​(1)whereT~n≡k−1​[Un,t−1]12[Un,t−1]11​[Un,t−1]22−[Un,t−1]122.|\widehat{T}\_{n}-\widetilde{T}\_{n}|=o\_{p}(1)\quad\text{where}\quad\widetilde{T}\_{n}\equiv\frac{\sqrt{k-1}[U\_{n,t}^{-1}]\_{12}}{\sqrt{[U\_{n,t}^{-1}]\_{11}[U\_{n,t}^{-1}]\_{22}-[U\_{n,t}^{-1}]\_{12}^{2}}}. |  |

This proposition shows that T^n\widehat{T}\_{n} can be asymptotically approximated by T~n\widetilde{T}\_{n}, which is a function of the matrix Un,tU\_{n,t} defined in Proposition [1](https://arxiv.org/html/2510.12911v1#Thmproposition1 "Proposition 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."). Consequently, the distributional properties of the limiting variable T~n\widetilde{T}\_{n} can be exploited to test the null hypothesis βt=β0\beta\_{t}=\beta\_{0} or to construct confidence intervals.

Accordingly, [Bollerslev et al., 2024b](https://arxiv.org/html/2510.12911v1#bib.bib17)  demonstrate that T^n\widehat{T}\_{n} follows a Student’s tt distribution with k−1k-1 degrees of freedom when the beta estimator is based solely on return observations, that is, when λ=(1,0,0)⊤\lambda=(1,0,0)^{\top}, which makes inference straightforward. The key complication arises when the beta estimator incorporates the other candlestick returns, i.e., when λ≠(1,0,0)⊤\lambda\neq(1,0,0)^{\top}. In this case, as discussed in Section [2.4.2](https://arxiv.org/html/2510.12911v1#S2.SS4.SSS2 "2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."), Un,tU\_{n,t} and hence T~n\widetilde{T}\_{n} depend on population quantities in a non-trivial manner, generally resulting in a non-pivotal distribution, thereby complicating inference.

Meanwhile, under the null hypothesis H0:βt=0H\_{0}:\beta\_{t}=0, the limiting distribution of T~n\widetilde{T}\_{n} becomes pivotal and hence allows for feasible inference. The reason is that under this null hypothesis, the covariance matrix 𝒄t\boldsymbol{c}\_{t} defined in Equation ([20](https://arxiv.org/html/2510.12911v1#S3.E20 "In 3.1 Candlestick-Beta Estimator ‣ 3 Spot Beta Estimation and Inference with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")) simplifies to a diagonal matrix and consequently the ϱt\boldsymbol{\varrho}\_{t} terms in the coupling returns provided in Equation ([9](https://arxiv.org/html/2510.12911v1#S2.E9 "In Proposition 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")) cancel out, leaving the limiting variable as a function of the Brownian motion functionals only. Therefore, the distribution of T~n\widetilde{T}\_{n} can be characterized by Monte Carlo simulations.

Based on this simulated distribution, one can easily determine the critical values for the test. Specifically, for a given significance level α\alpha, I define constants Bα+B^{+}\_{\alpha} and Bα−B^{-}\_{\alpha} such that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Bα−<T~n<Bα+)=1−α.\mathbb{P}\left(B^{-}\_{\alpha}<\widetilde{T}\_{n}<B^{+}\_{\alpha}\right)=1-\alpha. |  | (22) |

These constants serve as the lower and upper critical values for this test. By construction, this procedure delivers asymptotically correct size under the null hypothesis H0:βt=0H\_{0}:\beta\_{t}=0.

Table [1](https://arxiv.org/html/2510.12911v1#S3.T1 "Table 1 ‣ 3.2 Testing on Spot Beta ‣ 3 Spot Beta Estimation and Inference with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") reports the critical values for various combinations of kk and α\alpha, computed using 10,00010{,}000 Monte Carlo simulations. Since infinitely many pairs can satisfy this condition, I select the highest density interval (HDI), which is the narrowest interval containing the desired probability mass. For comparison, I also report the critical values corresponding to the return-based beta estimator. These are derived analytically from the Student’s tt-distribution, following [Bollerslev et al., 2024b](https://arxiv.org/html/2510.12911v1#bib.bib17) . Finally, I present the interval widths, defined as Bα+−Bα−B^{+}\_{\alpha}-B^{-}\_{\alpha}, for both estimators to highlight efficiency gains achieved by the new candlestick-based method. From this table, it is evident that the critical values are tighter for the candlestick-based beta estimator compared to the return-based estimator, across all values of kk and α\alpha. Specifically, the difference in interval widths becomes more pronounced as kk decreases. This highlights the usefulness of my estimator, particularly in limited data scenarios.

Table 1: Critical values for the beta estimators: This table reports the critical values for the hypothesis test of H0:βt=0H\_{0}:\beta\_{t}=0 at significance levels α∈{5%,10%}\alpha\in\{5\%,10\%\} and for different local window sizes k∈{5,10,20}k\in\{5,10,20\}. The left panel shows the critical values for the return-based beta estimator derived from the Student’s tt-distribution with k−1k-1 degrees of freedom. The right panel presents the critical values for the candlestick-based beta estimator computed via Monte Carlo simulations. The interval width is defined as Bα+−Bα−B^{+}\_{\alpha}-B^{-}\_{\alpha}.

Return

Candlestick

𝒌\boldsymbol{k}
Bα−B\_{\alpha}^{-}
Bα+B\_{\alpha}^{+}
Width

Bα−B\_{\alpha}^{-}
Bα+B\_{\alpha}^{+}
Width

Panel A: α=5%\alpha=5\%

5
-2.776
2.776
5.552

-1.657
1.415
3.072

10
-2.262
2.262
4.524

-1.430
1.460
2.890

20
-2.093
2.093
4.186

-1.429
1.383
2.812

Panel B: α=10%\alpha=10\%

5
-2.132
2.132
4.264

-1.204
1.262
2.466

10
-1.383
1.383
2.766

-1.203
1.199
2.402

20
-1.328
1.328
2.656

-1.103
1.244
2.347

## 4 Simulations

This section examines the performance of the candlestick-based spot covariance estimator and the associated inference procedure through a series of Monte Carlo experiments. The analysis proceeds in two parts. First, I investigate the efficiency of the proposed estimator by comparing its asymptotic risk against an oracle estimator and a return-based estimator. Second, I evaluate the power of the hypothesis test for spot betas introduced in Section [3](https://arxiv.org/html/2510.12911v1#S3 "3 Spot Beta Estimation and Inference with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.").

### 4.1 Asymptotic Risk of the Estimators

To assess the effectiveness of the new approach, I compare the asymptotic risk of the estimator against two natural benchmarks. The first is an infeasible oracle estimator that minimizes the asymptotic risk under knowledge of the true correlation structure. The second benchmark is the return-based estimator, which relies solely on (open-to-close) returns. This comparison highlights the efficiency gains achieved by incorporating the additional information contained in the candlestick features.

The asymptotic risk R~​(λ;𝝆t)\widetilde{R}(\lambda;\boldsymbol{\rho}\_{t}) can be computed via Monte Carlo simulations for any λ\lambda and kk if the correlation structure is known. As in the previous numerical implementations, I focus on the case of N=2N=2 assets. Table [2](https://arxiv.org/html/2510.12911v1#S4.T2 "Table 2 ‣ 4.1 Asymptotic Risk of the Estimators ‣ 4 Simulations ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") reports the asymptotic risk values for various configurations. I consider 3 different levels of correlation, ρ∈{0,0.2,0.6}\rho\in\{0,0.2,0.6\}.191919This numbers represent the 10,50,9010,50,90 percentiles of cross-section of pairwise correlations among the S&P 500 stocks. Moreover, the size of the local estimation window is set to k∈{5,10,20}k\in\{5,10,20\}. All results are based on 10,000 Monte Carlo simulations.

Table 2: Asymptotic Risk of Estimators for Different ρ\rho Values: The table presents the asymptotic risk of three estimators: the return-based estimator, the candlestick-based estimator, and an oracle estimator that minimizes asymptotic risk with knowledge of the true correlation structure. The results are shown for various local window sizes k∈{5,10,20}k\in\{5,10,20\} and correlation levels ρ∈{0,0.2,0.6}\rho\in\{0,0.2,0.6\}. The asymptotic risk is computed via Monte Carlo simulations.

|  |  | 𝝆=𝟎\boldsymbol{\rho=0} | | 𝝆=0.2\boldsymbol{\rho=0.2} | | 𝝆=0.6\boldsymbol{\rho=0.6} | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 𝒌\boldsymbol{k} | Return | Candlestick | Oracle | Candlestick | Oracle | Candlestick | Oracle |
| 5 | 1.212 | 0.427 | 0.384 | 0.429 | 0.384 | 0.440 | 0.391 |
| 10 | 0.599 | 0.240 | 0.222 | 0.241 | 0.221 | 0.249 | 0.224 |
| 20 | 0.297 | 0.128 | 0.119 | 0.128 | 0.118 | 0.134 | 0.119 |

Table [2](https://arxiv.org/html/2510.12911v1#S4.T2 "Table 2 ‣ 4.1 Asymptotic Risk of the Estimators ‣ 4 Simulations ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") provides several key insights. First, my estimator achieves asymptotic risk levels that are very close to those of the oracle estimator across all values of kk and ρ\rho, implying roughly 8−9%8-9\% efficiency loss. This indicates that the proposed approach effectively addresses complications arising from the distribution of the estimator being non-pivotal, resulting in an estimator that performs nearly as well as the infeasible oracle estimator. Second, the proposed estimator consistently demonstrates a significant reduction in asymptotic risk compared to the return-based estimator, particularly for smaller values of kk. That is, for k=5k=5, the candlestick-based estimator’s risk is roughly 65% lower than that of the return-based estimator, and this difference is about 55%55\% for k=20k=20. This suggests that my approach effectively leverages the candlestick prices and yields more efficient estimators. With only k=5k=5 observations, the proposed estimator achieves a lower risk than the return-based estimator using k=10k=10 observations, demonstrating its superior efficiency in extracting information from limited data. This advantage is particularly valuable in high-frequency event studies, where identification often relies on short time intervals and data are inherently limited.

Overall, these results show that incorporating candlestick information substantially improves efficiency, providing a powerful and practical alternative to traditional return-based methods and approaching the performance of the infeasible oracle benchmark.

### 4.2 Power of the Test

Next, I evaluate the properties of the hypothesis test for spot betas discussed in Section [3](https://arxiv.org/html/2510.12911v1#S3 "3 Spot Beta Estimation and Inference with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."). To this end, I consider the data-generating process (DGP) employed in [Bollerslev et al., 2024b](https://arxiv.org/html/2510.12911v1#bib.bib17) .202020This DGP is built on the univariate setup originally proposed by Bollerslev and Todorov, ([2011](https://arxiv.org/html/2510.12911v1#bib.bib19)). Later, it is implemented by a number of subsequent studies (e.g., Bollerslev et al., ([2021](https://arxiv.org/html/2510.12911v1#bib.bib16)); Li et al., ([2024](https://arxiv.org/html/2510.12911v1#bib.bib35))). Specifically, this DGP assume a two-factor structure for the market variance process: νt=V1,t+V2,t\nu\_{t}=V\_{1,t}+V\_{2,t} where V1,tV\_{1,t} and V2,tV\_{2,t} follow the processes:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | d​V1,t=0.0128​(0.4068−V1,t)​d​t+0.0954​V1,t​(γ​d​W1,t+1−γ2​d​B1,t),\displaystyle dV\_{1,t}=0128\left(0.4068-V\_{1,t}\right)dt+0954\sqrt{V\_{1,t}}\left(\gamma dW\_{1,t}+\sqrt{1-\gamma^{2}}dB\_{1,t}\right), |  | (23) |
|  |  | d​V2,t=0.6930​(0.4068−V2,t)​d​t+0.7023​V2,t​(γ​d​W1,t+1−γ2​d​B2,t).\displaystyle dV\_{2,t}=6930\left(0.4068-V\_{2,t}\right)dt+7023\sqrt{V\_{2,t}}\left(\gamma dW\_{1,t}+\sqrt{1-\gamma^{2}}dB\_{2,t}\right). |  |

Here, B1,tB\_{1,t} and B2,tB\_{2,t} are independent Brownian motions that are also independent of W1,tW\_{1,t} and W2,tW\_{2,t}. The parameter γ\gamma is set to −0.7-0.7, capturing the well-documented leverage effect in financial markets. The coefficients are set so that the first volatility factor is highly persistent, showing 2.52.5 months half-life, while the second factor reverts to mean quickly, with a half-life of a day. This allows the DGP to capture both short-term fluctuations and long-term trends in volatility.

The idiosyncratic variance ςt\varsigma\_{t} and the spot beta are assumed to follow:

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt=1+0.25sin(t)2,ςt=(1.5+0.25sin(t)2)νt\beta\_{t}=1+0.25\sin(t)^{2},\quad\varsigma\_{t}=\left(1.5+0.25\sin(t)^{2}\right)\nu\_{t} |  | (24) |

where βt\beta\_{t} fluctuates between 11 and 1.251.25 over time and ςt\varsigma\_{t} is set to be proportional to the market variance νt\nu\_{t}. Finally, the price processes are generated using the representation provided in Equation ([19](https://arxiv.org/html/2510.12911v1#S3.E19 "In 3.1 Candlestick-Beta Estimator ‣ 3 Spot Beta Estimation and Inference with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")).

I simulate the price path using an Euler scheme on a one-second grid. Then I sample the prices at one-minute frequency to construct the candlestick data, implying Δn=1/390\Delta\_{n}=1/390 and n=390n=390 intraday observations. This setup mimics the empirical applications involving high-frequency financial data. As in the previous section, I consider three different values for the local window size, k∈{5,10,20}k\in\{5,10,20\}. For each configuration, I conduct 10,000 Monte Carlo simulations to compute the empirical rejection rates at significance levels of 1%,5%,1\%,5\%, and 10%10\%. The results are summarized in Table [3](https://arxiv.org/html/2510.12911v1#S4.T3 "Table 3 ‣ 4.2 Power of the Test ‣ 4 Simulations ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."). I also report the rejection rates for the return-based beta estimator for comparison.212121Note that the return-based test is developed by [Bollerslev et al., 2024b](https://arxiv.org/html/2510.12911v1#bib.bib17) . As discussed in Section [3](https://arxiv.org/html/2510.12911v1#S3 "3 Spot Beta Estimation and Inference with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."), the corresponding test statistic is shown to be Student’s t distributed.

Table 3: Power of Tests Derived from Return and Candlestick Estimators (%): The table reports the rejection rates (in percent) for the hypothesis test of H0:βt=0H\_{0}:\beta\_{t}=0 at significance levels α∈{1%,5%,10%}\alpha\in\{1\%,5\%,10\%\} and for different local window sizes k∈{5,10,20}k\in\{5,10,20\} based on simulated data. The left panel shows the rejection rates for the return-based beta estimator, while the right panel presents the rejection rates for the candlestick-based beta estimator.

|  | Return | | |  | Candlestick | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 𝒌\boldsymbol{k} | 1% | 5% | 10% |  | 1% | 5% | 10% |
| 55 | 8.84 | 28.02 | 42.11 |  | 31.49 | 58.82 | 65.67 |
| 1010 | 32.53 | 59.98 | 72.66 |  | 60.46 | 84.81 | 91.22 |
| 2020 | 73.99 | 90.32 | 94.80 |  | 94.95 | 99.15 | 99.44 |

Table [3](https://arxiv.org/html/2510.12911v1#S4.T3 "Table 3 ‣ 4.2 Power of the Test ‣ 4 Simulations ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") reports the rejection rates (in percent) for the two competing inference procedures at significance levels of 1%1\%, 5%5\%, and 10%10\%. Across all scenarios, the candlestick-based test consistently rejects false null hypotheses more frequently than the return-based test. This gap widens as the local window size decreases. For instance, when k=20k=20 and α=5%\alpha=5\%, the difference in rejection rates is approximately 9%9\%, increasing to 25%25\% for k=10k=10 and α=5%\alpha=5\%. These results demonstrate a substantial reduction in false negatives, highlighting the improved power of the candlestick-based procedure.

To further illustrate the power advantage of the proposed test, Figure [3](https://arxiv.org/html/2510.12911v1#S4.F3 "Figure 3 ‣ 4.2 Power of the Test ‣ 4 Simulations ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") presents the power curves for both tests as a function of the true βt\beta\_{t} value. In this analysis, I use the same DGP as before but set βt\beta\_{t} to be constant, varying from 0 to 22. The null hypothesis is that βt=0\beta\_{t}=0, and the empirical rejection rates are computed at a 5%5\% significance level using 10,00010,000 Monte Carlo simulations. The local window size is fixed at k=10k=10.

![Refer to caption](x2.png)


Figure 3: Power Curves of Return-based and Candlestick-based Tests. The figure plots the empirical power of the two tests as a function of the true βt\beta\_{t} value (assumed to be constant), with k=10k=10 and a significance level of 5%5\%. The power is computed using 10,000 Monte Carlo simulations for each βt\beta\_{t} value.

Figure [3](https://arxiv.org/html/2510.12911v1#S4.F3 "Figure 3 ‣ 4.2 Power of the Test ‣ 4 Simulations ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") displays two panels. The top panel shows the rejection rates for both tests, while the bottom panel illustrates the difference in rejection rates between the candlestick-based and return-based tests. The x-axis shows how far βt\beta\_{t} is from the null value of 0. Looking at the leftmost point where βt\beta\_{t} is set to zero, the return-based test appears to correctly maintain the size at approximately 5%5\%, while the candlestick-based test slightly over-rejects at around 6%6\%. At the right-end where βt\beta\_{t} is far from the null, unsurprisingly, both tests achieve a power close to 100%100\%. As βt\beta\_{t} deviates from zero, the power of both tests increases, with the candlestick-based test exhibiting a notably steeper increase. For example, when βt\beta\_{t} is around 11, the candlestick-based test achieves a power of approximately 85%85\%, while the return-based test is around 60%60\%, indicating a 25%25\% difference.

Overall, these results show that the candlestick-based inference for spot betas greatly improves power, especially when the true βt\beta\_{t} is near the null, highlighting its practical value for more accurate inference on measures of the systematic risk.

## 5 Empirical Application

In this section, I apply the candlestick-beta estimator and the associated inference procedure to analyze Bitcoin’s market exposure, i.e., its market beta. Given the growing role of crypto assets in institutional and retail portfolios, this empirical question has important implications for risk management and portfolio selection.222222Recent years have seen several developments that facilitated investment in crypto assets. In 2017, the Chicago Mercantile Exchange (CME) launched Bitcoin futures contracts, followed by the introduction of Bitcoin options in 2020. More recently, in January 2024, the U.S. Securities and Exchange Commission (SEC) approved the first Bitcoin exchange-traded fund (ETF). Although crypto advocates often describe these assets as “digital gold”, suggesting potential hedging benefits against aggregate market risk, empirical evidence on their risk characteristics remains limited.

To gain a deeper understanding of Bitcoin’s market exposure, I estimate the spot beta and then test the null of market neutrality, i.e, zero beta, at a 5%5\% significance level using the new candlestick-based framework proposed in Section [3](https://arxiv.org/html/2510.12911v1#S3 "3 Spot Beta Estimation and Inference with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."). This analysis employs 11-minute price observations from two prominent ETFs: SPY and IBIT. While the former is a well-known ETF that tracks the S&P 500 index and commonly used in empirical studies, the latter is a newly launched (as of January 2024) iShares Bitcoin Trust ETF designed to track the performance of Bitcoin.232323Cryptocurrency ETFs are designed to provide investors with exposure to the price movements in crypto markets. The IBIT has been the most traded one since its launch and its net asset value exceeds $\mathdollar70 billion as of 2025. The sample spans the entire year 2024, covering 250250 trading days and standard trading hours from 9:309:30 to 16:0016:00. Spot beta estimates are computed using a local window of k=10k=10 one-minute candlesticks, yielding 3939 spot estimates per trading day.

I start by assessing the monthly rejection rates (in terms of percentage) of the null hypothesis of market neutrality. The results are presented in Figure [4](https://arxiv.org/html/2510.12911v1#S5.F4 "Figure 4 ‣ 5 Empirical Application ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."). The figure shows that the rejection rates are around 10%10\% in the first two months of 2024, later increasing to 40%40\% in mid-2024 and ending the year with a similar rate. Notably, the rejection rates are more pronounced in August and September, reaching around 60%60\%. These months also coincide with a number of crucial economic events. Particularly, the first week of September was marked by a series of weak production and labor market data releases, raising concerns about a potential economic slowdown.242424The first week of September brought a sequence of weak data: the ISM manufacturing index on the 3rd, the ADP jobs report on the 5th, and the non-farm payrolls on the 6th, all of which came in below expectations. These developments led to a sharp sell-off in equities and a spike in volatility, as reflected in the VIX index.

![Refer to caption](x3.png)


Figure 4: Monthly Rejection Rates of the Null Hypothesis of Zero Beta for IBIT. The figure shows the monthly rejection rates of the null hypothesis of zero beta for IBIT using candlestick-based inference framework. The sample covers the entire 2024 year, a total of 250250 days, and usual trading hours from 9:309:30 to 16:0016:00.

Figure [5](https://arxiv.org/html/2510.12911v1#S5.F5 "Figure 5 ‣ 5 Empirical Application ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") presents the spot beta estimates and corresponding confidence intervals for September 3–6. This figure reveals that the null hypothesis of zero beta is rejected in a substantial portion of the intraday intervals, approximately 65%65\% of the time. For instance, looking at the bottom right panel, the null is rejected in 2727 out of 3939 intervals on September 6. On that day, the NFP report was released at 8:30 AM, prior to market open, and spot beta estimates were already significant and around 1.51.5 at the opening. Similar patterns are observed on the other days of that week. These results indicate that the Bitcoin ETF IBIT exhibited significant positive exposure to market risk during this turbulent week, precisely the periods when such instruments may be most valuable for risk management purposes.

![Refer to caption](x4.png)


Figure 5: Spot Beta of IBIT on September 3-6, 2024. The figure shows the spot beta estimates of IBIT with respect to SPY using 1010 1−m​i​n1-min candlestick observations in 10−m​i​n10-min frequency. The vertical lines indicate the 95% confidence intervals.

To illustrate the advantages of the proposed candlestick-based framework relative to conventional return-based methods, I conduct an event study analysis around two Federal Open Market Committee (FOMC) meetings on June 12, 2024, and September 18, 2024.252525The literature widely recognizes FOMC announcements as among the most influential scheduled events, showing immediate and significant impacts on financial markets, see for example, Bernanke and Kuttner, ([2005](https://arxiv.org/html/2510.12911v1#bib.bib11)); Savor and Wilson, ([2014](https://arxiv.org/html/2510.12911v1#bib.bib46)); Lucca and Moench, ([2015](https://arxiv.org/html/2510.12911v1#bib.bib39)); Cieslak et al., ([2019](https://arxiv.org/html/2510.12911v1#bib.bib25)). Figure [6](https://arxiv.org/html/2510.12911v1#S5.F6 "Figure 6 ‣ 5 Empirical Application ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") reports the estimation results for these two events. The top panels display the prices of IBIT and SPY, while the bottom panels present the corresponding spot beta estimates for IBIT over a two-hour window surrounding the FOMC rate decision, with time zero aligned to the announcement (indicated by the vertical dashed line). Candlestick-based estimates are depicted by blue circles, while return-based estimates are shown by red triangles, with vertical bars representing the 95%95\% confidence intervals.

![Refer to caption](x5.png)


Figure 6: Spot Beta of IBIT Around FOMC Meetings. The figure shows the spot beta estimates of IBIT with respect to SPY using 1010 11-min candlestick observations in 1010-min frequency around two FOMC meetings: June 12, 2024 (left panels) and September 18, 2024 (right panels). The top panels display the price movements of IBIT and SPY, while the bottom panels present the corresponding spot beta estimates. Candlestick-based estimates are indicated by blue circles and return-based estimates by red triangles. The vertical lines indicate the 95% confidence intervals, and the vertical dashed line marks the time of the FOMC announcement.

On September 18, 2024, the FOMC announced a 50-basis-point rate cut at 2:00 PM, which markets interpreted as a strong dovish signal, triggering increases in SPY and IBIT prices (see the top-right panel of Figure [6](https://arxiv.org/html/2510.12911v1#S5.F6 "Figure 6 ‣ 5 Empirical Application ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")). Following the announcement, spot beta estimates increased from below 0.50.5 to around 1.51.5 and remained consistently positive and statistically significant for nearly an hour. In this case, the signal is strong, and both the candlestick-based and return-based methods rejected the null hypothesis, although small differences arise in the pre-announcement period.

In contrast, the June 12, 2024 FOMC meeting reflects a weaker informational shock. The Fed kept rates unchanged but released a relatively hawkish dot plot, prompting declines in SPY and IBIT prices (see the top-left panel). Here, the candlestick-based estimates still detect a significant positive exposure to market risk immediately after the release, whereas the return-based method fails to reject the null. Particularly, the return-based estimates exhibit wider confidence intervals, reflecting greater uncertainty around the estimates. This comparison is consistent with the simulation results in Section [4](https://arxiv.org/html/2510.12911v1#S4 "4 Simulations ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."), demonstrating the superior power properties of the candlestick-based approach. Consequently, these findings underscore the usefulness and robustness of the proposed approach in empirical settings.

## 6 Conclusion

This paper develops a new framework for estimating and conducting inference on spot covariance matrices using high-frequency candlestick data which consist of open, high, low and close prices for each interval. The approach builds on the idea of minimizing a well-defined estimation risk to optimally combine the information from all four prices. The resulting candlestick-based estimator has a simple form and is easy to implement. Monte Carlo experiments demonstrate that the candlestick-based estimator attains asymptotic risk levels close to those of an infeasible oracle benchmark, while substantially outperforming return-based estimators, exhibiting markedly higher power (up to 25% improvement), reducing false negatives in hypothesis testing.

In an empirical study with 1-minute candlestick data of SPY (S&P 500 ETF) and IBIT (iShares Bitcoin Trust ETF), the method reveals significant positive market exposure of the Bitcoin ETF, especially during turbulent periods, challenging popular “digital gold” narrative for risk management. Moreover, in an event study around FOMC meetings, the candlestick-based approach detects significant market betas that the return-based method fails to do so. Overall, this work highlights the value of utilizing candlestick data for more accurate and powerful estimation and inference of spot covariance structures in financial markets.

## References

* Aït-Sahalia et al., (2010)

  Aït-Sahalia, Y., Fan, J., and Xiu, D. (2010).
  High-frequency covariance estimates with noisy and asynchronous
  financial data.
  Journal of the American Statistical Association,
  105(492):1504–1517.
* Aït-Sahalia and Jacod, (2014)

  Aït-Sahalia, Y. and Jacod, J. (2014).
  High-frequency financial econometrics.
  Princeton University Press.
* Andersen et al., (2000)

  Andersen, T., Bollerslev, T., Diebold, F., and Labys, P. (2000).
  Great realizations.
  RISK, 13:105–108.
* Andersen et al., (2021)

  Andersen, T. G., Thyrsgaard, M., and Todorov, V. (2021).
  Recalcitrant betas: Intraday variation in the cross-sectional
  dispersion of systematic risk.
  Quantitative Economics, 12(2):647–682.
* Back, (2010)

  Back, K. (2010).
  Asset pricing and portfolio choice theory.
  Oxford University Press.
* Bannouh et al., (2009)

  Bannouh, K., Van Dijk, D., and Martens, M. (2009).
  Range-based covariance estimation using high-frequency data: The
  realized co-range.
  Journal of Financial Econometrics, 7(4):341–372.
* Barndorff-Nielsen et al., (2009)

  Barndorff-Nielsen, O., Hansen, P. R., Lunde, A., and Shephard, N. (2009).
  Realized kernels in practice: Trades and quotes.
  The Econometrics Journal, 12(3):C1–C32.
* Barndorff-Nielsen et al., (2011)

  Barndorff-Nielsen, O. E., Hansen, P. R., Lunde, A., and Shephard, N. (2011).
  Multivariate realised kernels: Consistent positive semi-definite
  estimators of the covariation of equity prices with noise and non-synchronous
  trading.
  Journal of Econometrics, 162(2):149–169.
* (9)

  Barndorff-Nielsen, O. E. and Shephard, N. (2004a).
  Econometric analysis of realized covariation: High frequency based
  covariance, regression, and correlation in financial economics.
  Econometrica, 72(3):885–925.
* (10)

  Barndorff-Nielsen, O. E. and Shephard, N. (2004b).
  Power and bipower variation with stochastic volatility and jumps.
  Journal of Financial Econometrics, 2(1):1–37.
* Bernanke and Kuttner, (2005)

  Bernanke, B. S. and Kuttner, K. N. (2005).
  What explains the stock market’s reaction to federal reserve policy?
  The Journal of Finance, 60(3):1221–1257.
* Bibinger et al., (2019)

  Bibinger, M., Hautsch, N., Malec, P., and Reiss, M. (2019).
  Estimating the spot covariation of asset prices—statistical theory
  and empirical evidence.
  Journal of Business & Economic Statistics, 37(3):419–435.
* (13)

  Bollerslev, T., Hood, B., Huss, J., and Pedersen, L. H. (2018a).
  Risk everywhere: Modeling and managing volatility.
  Review of Financial Studies, 31(7):2729–2773.
* (14)

  Bollerslev, T., Li, J., and Li, Q. (2024a).
  Optimal nonparametric range-based volatility estimation.
  Journal of Econometrics, 238(1):105548.
* Bollerslev et al., (2025)

  Bollerslev, T., Li, J., Li, Q., and Li, Y. (2025).
  Optimal candlestick-based spot volatility estimation: New tricks and
  feasible inference procedures.
  Available at SSRN 5046917.
* Bollerslev et al., (2021)

  Bollerslev, T., Li, J., and Liao, Z. (2021).
  Fixed-k inference for volatility.
  Quantitative Economics, 12(4):1053–1084.
* (17)

  Bollerslev, T., Li, J., and Ren, Y. (2024b).
  Optimal inference for spot regressions.
  American Economic Review, 114(3):678–708.
* (18)

  Bollerslev, T., Patton, A. J., and Quaedvlieg, R. (2018b).
  Modeling and forecasting (un) reliable realized covariances for more
  reliable financial decisions.
  Journal of Econometrics, 207(1):71–91.
* Bollerslev and Todorov, (2011)

  Bollerslev, T. and Todorov, V. (2011).
  Estimation of jump tails.
  Econometrica, 79(6):1727–1783.
* Brandt and Diebold, (2006)

  Brandt, M. W. and Diebold, F. X. (2006).
  A no-arbitrage approach to range-based estimation of return
  covariances and correlations.
  Journal of Business, 79(1):61–74.
* Christensen et al., (2010)

  Christensen, K., Kinnebrock, S., and Podolskij, M. (2010).
  Pre-averaging estimators of the ex-post covariance matrix in noisy
  diffusion models with non-synchronous data.
  Journal of Econometrics, 159(1):116–133.
* Christensen and Podolskij, (2007)

  Christensen, K. and Podolskij, M. (2007).
  Realized range-based estimation of integrated variance.
  Journal of Econometrics, 141(2):323–349.
* Christensen and Podolskij, (2012)

  Christensen, K. and Podolskij, M. (2012).
  Asymptotic theory of range-based multipower variation.
  Journal of Financial Econometrics, 10(3):417–456.
* Christensen et al., (2009)

  Christensen, K., Podolskij, M., and Vetter, M. (2009).
  Bias-correcting the realized range-based variance in the presence of
  market microstructure noise.
  Finance and Stochastics, 13:239–268.
* Cieslak et al., (2019)

  Cieslak, A., Morse, A., and Vissing-Jorgensen, A. (2019).
  Stock returns over the fomc cycle.
  The Journal of Finance, 74(5):2201–2248.
* Diebold and Strasser, (2013)

  Diebold, F. X. and Strasser, G. (2013).
  On the correlation structure of microstructure noise: A financial
  economic approach.
  Review of Economic Studies, 80(4):1304–1337.
* Fama and French, (1992)

  Fama, E. F. and French, K. R. (1992).
  The cross-section of expected stock returns.
  The Journal of Finance, 47(2):427–465.
* Fan and Wang, (2008)

  Fan, J. and Wang, Y. (2008).
  Spot volatility estimation for high-frequency data.
  Statistics and its Interface, 1(2):279–288.
* Garman and Klass, (1980)

  Garman, M. B. and Klass, M. J. (1980).
  On the estimation of security price volatilities from historical
  data.
  Journal of Business, pages 67–78.
* Hayashi and Yoshida, (2005)

  Hayashi, T. and Yoshida, N. (2005).
  On covariance estimation of non-synchronously observed diffusion
  processes.
  Bernoulli, 11(2):359–379.
* Jacod et al., (2021)

  Jacod, J., Li, J., and Liao, Z. (2021).
  Volatility coupling.
  The Annals of Statistics, 49(4):1982–1998.
* Jacod and Protter, (2012)

  Jacod, J. and Protter, P. (2012).
  Discretization of Processes.
  Springer.
* Lehmann and Casella, (2006)

  Lehmann, E. L. and Casella, G. (2006).
  Theory of point estimation.
  Springer Science & Business Media.
* Lewandowski et al., (2009)

  Lewandowski, D., Kurowicka, D., and Joe, H. (2009).
  Generating random correlation matrices based on vines and extended
  onion method.
  Journal of Multivariate Analysis, 100(9):1989–2001.
* Li et al., (2024)

  Li, J., Wang, D., and Zhang, Q. (2024).
  Reading the candlesticks: An ok estimator for volatility.
  Review of Economics and Statistics, 106(4):1114–1128.
* Li et al., (2025)

  Li, Y., Nolte, I., Nolte, S., and Yu, S. (2025).
  Realized candlestick wicks.
  Journal of Econometrics, 250:106014.
* Lintner, (1965)

  Lintner, J. (1965).
  Security prices, risk, and maximal gains from diversification.
  The Journal of Finance, 20(4):587–615.
* Liu and Tsyvinski, (2021)

  Liu, Y. and Tsyvinski, A. (2021).
  Risks and returns of cryptocurrency.
  The Review of Financial Studies, 34(6):2689–2727.
* Lucca and Moench, (2015)

  Lucca, D. O. and Moench, E. (2015).
  The pre-fomc announcement drift.
  The Journal of Finance, 70(1):329–371.
* Mancini, (2009)

  Mancini, C. (2009).
  Non-parametric threshold estimation for models with stochastic
  diffusion coefficient and jumps.
  Scandinavian Journal of Statistics, 36(2):270–296.
* Martens and Van Dijk, (2007)

  Martens, M. and Van Dijk, D. (2007).
  Measuring volatility with the realized range.
  Journal of Econometrics, 138(1):181–207.
* Nakamura and Steinsson, (2018)

  Nakamura, E. and Steinsson, J. (2018).
  High-frequency identification of monetary non-neutrality: the
  information effect.
  The Quarterly Journal of Economics, 133(3):1283–1330.
* Parkinson, (1980)

  Parkinson, M. (1980).
  The extreme value method for estimating the variance of the rate of
  return.
  Journal of Business, pages 61–65.
* Rogers and Shepp, (2006)

  Rogers, L. and Shepp, L. (2006).
  The correlation of the maxima of correlated brownian motions.
  Journal of Applied Probability, 43(3):880–883.
* Rogers and Zhou, (2008)

  Rogers, L. C. and Zhou, F. (2008).
  Estimating correlation from high, low, opening and closing prices.
  Annals of Applied Probability, 18(2):813–823.
* Savor and Wilson, (2014)

  Savor, P. and Wilson, M. (2014).
  Asset pricing: A tale of two days.
  Journal of Financial Economics, 113(2):171–201.
* Sharpe, (1964)

  Sharpe, W. F. (1964).
  Capital asset prices: A theory of market equilibrium under conditions
  of risk.
  The Journal of Finance, 19(3):425–442.

## Appendix Appendix A

### A.1 Proof of Proposition [1](https://arxiv.org/html/2510.12911v1#Thmproposition1 "Proposition 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")

In this section, I provide the proof of Proposition [1](https://arxiv.org/html/2510.12911v1#Thmproposition1 "Proposition 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") which builds on the coupling techniques developed in Jacod et al., ([2021](https://arxiv.org/html/2510.12911v1#bib.bib31)) and Bollerslev et al., ([2021](https://arxiv.org/html/2510.12911v1#bib.bib16)). The former studies the approximation of the estimation error for the spot covariance estimator when kk increases with nn, whereas the latter focuses on coupling the spot volatility estimator in a fixed-kk framework. As noted in the main text, I consider a fixed-kk setup and thus my work is in the same spirit as Bollerslev et al., ([2021](https://arxiv.org/html/2510.12911v1#bib.bib16)). To ensure consistency with the existing literature, I closely follow the notation introduced in the aforementioned papers.

I rewrite the Assumption [1](https://arxiv.org/html/2510.12911v1#Thmassumption1 "Assumption 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") and Proposition [1](https://arxiv.org/html/2510.12911v1#Thmproposition1 "Proposition 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") here for convenience:

###### Assumption 1.

Suppose that 𝐗t\boldsymbol{X}\_{t} has the form in Equation ([1](https://arxiv.org/html/2510.12911v1#S2.E1 "In 2.1 Price Process ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")) and there exists a sequence (Tm)m≥1(T\_{m})\_{m\geq 1} of stopping times increasing to infinity and the following conditions hold for each m≥1m\geq 1:

* (i)

  ‖𝒃t‖+‖𝝈t‖+‖𝝈t−1‖≤Km\|\boldsymbol{b}\_{t}\|+\|\boldsymbol{\sigma}\_{t}\|+\|\boldsymbol{\sigma}\_{t}^{-1}\|\leq K\_{m} for some constant KmK\_{m} for all t∈[0,Tm]t\in[0,T\_{m}];
* (ii)

  𝔼​[‖𝝈t∧Tm−𝝈s∧Tm‖2]≤Km​|t−s|\mathbb{E}\left[\|\boldsymbol{\sigma}\_{t\wedge T\_{m}}-\boldsymbol{\sigma}\_{s\wedge T\_{m}}\|^{2}\right]\leq K\_{m}|t-s| for all t,s∈[0,Tm]t,s\in[0,T\_{m}].

###### Proposition 1.

Suppose that Assumption [1](https://arxiv.org/html/2510.12911v1#Thmassumption1 "Assumption 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") holds. Fix any t∈[0,T]t\in[0,T]. For any k≥1k\geq 1 and 𝚲\boldsymbol{\Lambda}, the following holds as Δn→0\Delta\_{n}\to 0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝝈t−1​𝒄^n,t​(λ)​𝝈t−⊤−Un,t‖=op​(1)\left\|\boldsymbol{\sigma}\_{t}^{-1}\widehat{\boldsymbol{c}}\_{n,t}(\lambda)\boldsymbol{\sigma}\_{t}^{-\top}-U\_{n,t}\right\|=o\_{p}(1) |  | (A.1) |

where Un,t=1k​∑i∈ℐn,t{λ1​𝛇i,r​𝛇i,r⊤+λ2​𝛇i,h​𝛇i,a⊤+λ3​𝛇i,ℓ​𝛇i,w⊤}U\_{n,t}=\frac{1}{k}\sum\_{i\in\mathcal{I}\_{n,t}}\Big\{\lambda\_{1}\boldsymbol{\zeta}\_{i,r}\boldsymbol{\zeta}\_{i,r}^{\top}+\lambda\_{2}\boldsymbol{\zeta}\_{i,h}\boldsymbol{\zeta}\_{i,a}^{\top}+\lambda\_{3}\boldsymbol{\zeta}\_{i,\ell}\boldsymbol{\zeta}\_{i,w}^{\top}\Big\} and, for any i∈ℐn,ti\in\mathcal{I}\_{n,t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜻i,r≡𝑾i​Δn−𝑾(i−1)​ΔnΔn𝜻i,a≡ϱt−1​supτ∈𝒯i​ϱt​(𝑾τ−𝑾(i−1)​ΔnΔn)+ϱt−1​infτ∈𝒯i​ϱt​(𝑾τ−𝑾(i−1)​ΔnΔn)−(𝑾i​Δn−𝑾(i−1)​ΔnΔn)𝜻i,w≡ϱt−1​supτ∈𝒯i​ϱt​(𝑾τ−𝑾(i−1)​ΔnΔn)−ϱt−1​infτ∈𝒯i​ϱt​(𝑾τ−𝑾(i−1)​ΔnΔn)\begin{array}[]{rcl}\boldsymbol{\zeta}\_{i,r}&\equiv&\frac{\boldsymbol{W}\_{i\Delta\_{n}}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\\ \boldsymbol{\zeta}\_{i,a}&\equiv&\boldsymbol{\varrho}\_{t}^{-1}\underset{\tau\in\mathcal{T}\_{i}}{\sup\>}\boldsymbol{\varrho}\_{t}\left(\frac{\boldsymbol{W}\_{\tau}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)+\boldsymbol{\varrho}\_{t}^{-1}\underset{\tau\in\mathcal{T}\_{i}}{\inf\>}\boldsymbol{\varrho}\_{t}\left(\frac{\boldsymbol{W}\_{\tau}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)-\left(\frac{\boldsymbol{W}\_{i\Delta\_{n}}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)\\ \boldsymbol{\zeta}\_{i,w}&\equiv&\boldsymbol{\varrho}\_{t}^{-1}\underset{\tau\in\mathcal{T}\_{i}}{\sup\>}\boldsymbol{\varrho}\_{t}\left(\frac{\boldsymbol{W}\_{\tau}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)-\boldsymbol{\varrho}\_{t}^{-1}\underset{\tau\in\mathcal{T}\_{i}}{\inf\>}\boldsymbol{\varrho}\_{t}\left(\frac{\boldsymbol{W}\_{\tau}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)\\ \end{array} |  | (A.2) |

with ϱt\boldsymbol{\varrho}\_{t} being the square root of spot correlation matrix 𝛒t\boldsymbol{\rho}\_{t}, i.e., 𝛒t=ϱt​ϱt⊤\boldsymbol{\rho}\_{t}=\boldsymbol{\varrho}\_{t}\boldsymbol{\varrho}\_{t}^{\top}. In explicit terms, 𝛒t=diag(𝐜t)−12𝐜tdiag(𝐜t)−12\boldsymbol{\rho}\_{t}=\operatorname{diag}(\boldsymbol{c}\_{t})^{-\frac{1}{2}}\boldsymbol{c}\_{t}\operatorname{diag}(\boldsymbol{c}\_{t})^{-\frac{1}{2}} and ϱt=diag(𝐜t)−12𝛔t\boldsymbol{\varrho}\_{t}=\operatorname{diag}(\boldsymbol{c}\_{t})^{-\frac{1}{2}}\boldsymbol{\sigma}\_{t} where diag⁡(𝐜t)\operatorname{diag}(\boldsymbol{c}\_{t}) is a diagonal matrix with the same diagonal elements as 𝐜t\boldsymbol{c}\_{t}.

###### Proof.

Fix k≥1k\geq 1 and λ\lambda. Let KK denote a generic positive constant. As is common in the spot estimation literature, one can strengthen Assumption [1](https://arxiv.org/html/2510.12911v1#Thmassumption1 "Assumption 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") by assuming the conditions hold with Tm=∞T\_{m}=\infty, which can be justified by a standard localization argument (see Jacod and Protter, ([2012](https://arxiv.org/html/2510.12911v1#bib.bib32)) for details).

I begin by writing out the explicit expressions for the candlestick returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓i≡Δn−12​(∫(i−1)​Δni​Δn𝒃s​𝑑s+∫(i−1)​Δni​Δn𝝈s​𝑑𝑾s)𝒉i≡Δn−12​(supt∈𝒯n,i(∫(i−1)​Δnt𝒃s​𝑑s+∫(i−1)​Δnt𝝈s​𝑑𝑾s))ℓi≡Δn−12​(inft∈𝒯n,i(∫(i−1)​Δnt𝒃s​𝑑s+∫(i−1)​Δnt𝝈s​𝑑𝑾s))\begin{array}[]{rcl}\boldsymbol{r}\_{i}&\equiv&\Delta\_{n}^{-\frac{1}{2}}\left(\int\_{(i-1)\Delta\_{n}}^{i\Delta\_{n}}\boldsymbol{b}\_{s}ds+\int\_{(i-1)\Delta\_{n}}^{i\Delta\_{n}}\boldsymbol{\sigma}\_{s}d\boldsymbol{W}\_{s}\right)\vskip 10.00002pt\\ \boldsymbol{h}\_{i}&\equiv&\Delta\_{n}^{-\frac{1}{2}}\left(\sup\_{t\in\mathcal{T}\_{n,i}}\left(\int\_{(i-1)\Delta\_{n}}^{t}\boldsymbol{b}\_{s}ds+\int\_{(i-1)\Delta\_{n}}^{t}\boldsymbol{\sigma}\_{s}d\boldsymbol{W}\_{s}\right)\right)\vskip 10.00002pt\\ \boldsymbol{\ell}\_{i}&\equiv&\Delta\_{n}^{-\frac{1}{2}}\left(\inf\_{t\in\mathcal{T}\_{n,i}}\left(\int\_{(i-1)\Delta\_{n}}^{t}\boldsymbol{b}\_{s}ds+\int\_{(i-1)\Delta\_{n}}^{t}\boldsymbol{\sigma}\_{s}d\boldsymbol{W}\_{s}\right)\right)\end{array} |  | (A.3) |

I also introduce the following definitions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓i′≡𝝈(i−1)​Δn​(𝑾i​Δn−𝑾(i−1)​ΔnΔn)𝒉i′≡supt∈𝒯n,i𝝈(i−1)​Δn​(𝑾t−𝑾(i−1)​ΔnΔn)ℓi′≡inft∈𝒯n,i𝝈(i−1)​Δn​(𝑾t−𝑾(i−1)​ΔnΔn)\begin{array}[]{rcl}\boldsymbol{r}\_{i}^{\prime}&\equiv&\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}}\left(\frac{\boldsymbol{W}\_{i\Delta\_{n}}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)\vskip 10.00002pt\\ \boldsymbol{h}\_{i}^{\prime}&\equiv&\sup\_{t\in\mathcal{T}\_{n,i}}\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}}\left(\frac{\boldsymbol{W}\_{t}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)\vskip 10.00002pt\\ \boldsymbol{\ell}\_{i}^{\prime}&\equiv&\inf\_{t\in\mathcal{T}\_{n,i}}\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}}\left(\frac{\boldsymbol{W}\_{t}-\boldsymbol{W}\_{(i-1)\Delta\_{n}}}{\sqrt{\Delta\_{n}}}\right)\end{array} |  | (A.4) |

which serve as the coupling variables for the candlestick returns. Similar variables can be defined for the range and asymmetry variables:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒂i′≡𝒉i′+ℓi′−𝒓i′𝒘i′≡𝒉i′−ℓi′\begin{array}[]{rcl}\boldsymbol{a}\_{i}^{\prime}&\equiv&\boldsymbol{h}\_{i}^{\prime}+\boldsymbol{\ell}\_{i}^{\prime}-\boldsymbol{r}\_{i}^{\prime}\\ \boldsymbol{w}\_{i}^{\prime}&\equiv&\boldsymbol{h}\_{i}^{\prime}-\boldsymbol{\ell}\_{i}^{\prime}\end{array} |  | (A.5) |

The proof consists of two steps. The first step controls how well the coupling returns in Equation ([A.4](https://arxiv.org/html/2510.12911v1#A1.E4 "In A.1 Proof of Proposition 1 ‣ Appendix Appendix A ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")) approximate the candlestick returns in Equation ([A.3](https://arxiv.org/html/2510.12911v1#A1.E3 "In A.1 Proof of Proposition 1 ‣ Appendix Appendix A ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")). The second step combines these results with the continuous mapping theorem to reach the desired conclusion. Before proceeding to the first step, I derive useful intermediate results.

By Assumption [1](https://arxiv.org/html/2510.12911v1#Thmassumption1 "Assumption 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."), it is easy to see that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∫(i−1)​Δni​Δn𝒃s​𝑑s‖≤∫(i−1)​Δni​Δn‖𝒃s‖​𝑑s=Op​(Δn).\left\|\int\_{(i-1)\Delta\_{n}}^{i\Delta\_{n}}\boldsymbol{b}\_{s}ds\right\|\leq\int\_{(i-1)\Delta\_{n}}^{i\Delta\_{n}}\|\boldsymbol{b}\_{s}\|ds=O\_{p}(\Delta\_{n}). |  | (A.6) |

Moreover, the Burkholder-Davis-Gundy inequality and Assumption [1](https://arxiv.org/html/2510.12911v1#Thmassumption1 "Assumption 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") imply that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖∫(i−1)​Δni​Δn(𝝈s−𝝈(i−1)​Δn)​𝑑𝑾s‖2]≤K​Δn​𝔼​[∫(i−1)​Δni​Δn‖𝝈s−𝝈(i−1)​Δn‖2​𝑑s]≤K​Δn2.\begin{array}[]{rcl}\mathbb{E}\left[\left\|\int\_{(i-1)\Delta\_{n}}^{i\Delta\_{n}}(\boldsymbol{\sigma}\_{s}-\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}})d\boldsymbol{W}\_{s}\right\|^{2}\right]&\leq&K\Delta\_{n}\mathbb{E}\left[\int\_{(i-1)\Delta\_{n}}^{i\Delta\_{n}}\|\boldsymbol{\sigma}\_{s}-\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}}\|^{2}ds\right]\\ &\leq&K\Delta\_{n}^{2}.\end{array} |  | (A.7) |

Further, we can deduce that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supt∈𝒯n,i‖∫(i−1)​Δnt(𝝈s−𝝈(i−1)​Δn)​𝑑𝑾s‖=Op​(Δn).\sup\_{t\in\mathcal{T}\_{n,i}}\left\|\int\_{(i-1)\Delta\_{n}}^{t}(\boldsymbol{\sigma}\_{s}-\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}})d\boldsymbol{W}\_{s}\right\|=O\_{p}(\Delta\_{n}). |  | (A.8) |

Step 1: We now establish approximation results for 𝒓i\boldsymbol{r}\_{i}, 𝒉i\boldsymbol{h}\_{i} and ℓi\boldsymbol{\ell}\_{i} separately. We start with the return:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝒓i−𝒓i′‖≤‖Δn−12​∫(i−1)​Δni​Δn𝒃s​𝑑s‖+‖Δn−12​∫(i−1)​Δni​Δn(𝝈s−𝝈(i−1)​Δn)​𝑑𝑾s‖=Op​(Δn12).\begin{array}[]{rcl}\|\boldsymbol{r}\_{i}-\boldsymbol{r}\_{i}^{\prime}\|&\leq&\left\|\Delta\_{n}^{-\frac{1}{2}}\int\_{(i-1)\Delta\_{n}}^{i\Delta\_{n}}\boldsymbol{b}\_{s}ds\right\|+\left\|\Delta\_{n}^{-\frac{1}{2}}\int\_{(i-1)\Delta\_{n}}^{i\Delta\_{n}}(\boldsymbol{\sigma}\_{s}-\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}})d\boldsymbol{W}\_{s}\right\|\vskip 10.00002pt\\ &=&O\_{p}(\Delta\_{n}^{\frac{1}{2}}).\end{array} |  | (A.9) |

where the first line directly follows from the triangle inequality and the second line uses above intermediate results in Equation ([A.6](https://arxiv.org/html/2510.12911v1#A1.E6 "In A.1 Proof of Proposition 1 ‣ Appendix Appendix A ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")) and ([A.8](https://arxiv.org/html/2510.12911v1#A1.E8 "In A.1 Proof of Proposition 1 ‣ Appendix Appendix A ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")). For the high return, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝒉i−𝒉i′‖≡Δn−12∥supt∈𝒯n,i(∫(i−1)​Δnt𝒃s​𝑑s+∫(i−1)​Δnt𝝈s​𝑑𝑾s)−supt∈𝒯n,i𝝈(i−1)​Δn(𝑾t−𝑾(i−1)​Δn)∥≤Δn−12​supt∈𝒯n,i‖∫(i−1)​Δnt𝒃s​𝑑s+∫(i−1)​Δnt(𝝈s−𝝈(i−1)​Δn)​𝑑𝑾s‖≤Δn−12​∫(i−1)​Δni​Δn‖𝒃s‖​𝑑s+supt∈𝒯n,i‖∫(i−1)​Δnt(𝝈s−𝝈(i−1)​Δn)​𝑑𝑾s‖=Op​(Δn12).\begin{array}[]{rcl}\left\|\boldsymbol{h}\_{i}-\boldsymbol{h}\_{i}^{\prime}\right\|&\equiv&\Delta\_{n}^{-\frac{1}{2}}\Big\|\sup\_{t\in\mathcal{T}\_{n,i}}\Big(\int\_{(i-1)\Delta\_{n}}^{t}\boldsymbol{b}\_{s}ds+\int\_{(i-1)\Delta\_{n}}^{t}\boldsymbol{\sigma}\_{s}d\boldsymbol{W}\_{s}\Big)\\ &&\qquad-\sup\_{t\in\mathcal{T}\_{n,i}}\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}}(\boldsymbol{W}\_{t}-\boldsymbol{W}\_{(i-1)\Delta\_{n}})\Big\|\vskip 10.00002pt\\ &\leq&\Delta\_{n}^{-\frac{1}{2}}\sup\_{t\in\mathcal{T}\_{n,i}}\left\|\int\_{(i-1)\Delta\_{n}}^{t}\boldsymbol{b}\_{s}ds+\int\_{(i-1)\Delta\_{n}}^{t}(\boldsymbol{\sigma}\_{s}-\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}})d\boldsymbol{W}\_{s}\right\|\vskip 10.00002pt\\ &\leq&\Delta\_{n}^{-\frac{1}{2}}\int\_{(i-1)\Delta\_{n}}^{i\Delta\_{n}}\|\boldsymbol{b}\_{s}\|ds+\sup\_{t\in\mathcal{T}\_{n,i}}\left\|\int\_{(i-1)\Delta\_{n}}^{t}(\boldsymbol{\sigma}\_{s}-\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}})d\boldsymbol{W}\_{s}\right\|\vskip 10.00002pt\\ &=&O\_{p}(\Delta\_{n}^{\frac{1}{2}}).\end{array} |  | (A.10) |

The first two lines are obviously implications of sup\sup definition. Similarly, the last line follows from Equation [A.6](https://arxiv.org/html/2510.12911v1#A1.E6 "In A.1 Proof of Proposition 1 ‣ Appendix Appendix A ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") and [A.8](https://arxiv.org/html/2510.12911v1#A1.E8 "In A.1 Proof of Proposition 1 ‣ Appendix Appendix A ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."). Finally, one can deduce the same inequality for the low return:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ℓi−ℓi′‖=Op​(Δn12),\left\|\boldsymbol{\ell}\_{i}-\boldsymbol{\ell}\_{i}^{\prime}\right\|=O\_{p}(\Delta\_{n}^{\frac{1}{2}}), |  | (A.11) |

and also for the asymmetry and range variables:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝒂i−𝒂i′‖≤‖𝒉i−𝒉i′‖+‖ℓi−ℓi′‖+‖𝒓i−𝒓i′‖=Op​(Δn12)‖𝒘i−𝒘i′‖≤‖𝒉i−𝒉i′‖+‖ℓi−ℓi′‖=Op​(Δn12).\begin{array}[]{rcl}\|\boldsymbol{a}\_{i}-\boldsymbol{a}\_{i}^{\prime}\|&\leq&\|\boldsymbol{h}\_{i}-\boldsymbol{h}\_{i}^{\prime}\|+\|\boldsymbol{\ell}\_{i}-\boldsymbol{\ell}\_{i}^{\prime}\|+\|\boldsymbol{r}\_{i}-\boldsymbol{r}\_{i}^{\prime}\|=O\_{p}(\Delta\_{n}^{\frac{1}{2}})\vskip 10.00002pt\\ \|\boldsymbol{w}\_{i}-\boldsymbol{w}\_{i}^{\prime}\|&\leq&\|\boldsymbol{h}\_{i}-\boldsymbol{h}\_{i}^{\prime}\|+\|\boldsymbol{\ell}\_{i}-\boldsymbol{\ell}\_{i}^{\prime}\|=O\_{p}(\Delta\_{n}^{\frac{1}{2}}).\end{array} |  | (A.12) |

Furthermore, I claim that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝝈t−1​𝒓i′−𝜻i,r‖=Op​(Δn1/2)‖𝝈t−1​𝒂i′−𝜻i,a‖=Op​(Δn1/2)‖𝝈t−1​𝒘i′−𝜻i,w‖=Op​(Δn1/2).\begin{array}[]{rcl}\Big\|\boldsymbol{\sigma}\_{t}^{-1}\boldsymbol{r}\_{i}^{{}^{\prime}}-\boldsymbol{\zeta}\_{i,r}\Big\|&=&O\_{p}(\Delta\_{n}^{1/2})\vskip 10.00002pt\\ \Big\|\boldsymbol{\sigma}\_{t}^{-1}\boldsymbol{a}\_{i}^{{}^{\prime}}-\boldsymbol{\zeta}\_{i,a}\Big\|&=&O\_{p}(\Delta\_{n}^{1/2})\vskip 10.00002pt\\ \Big\|\boldsymbol{\sigma}\_{t}^{-1}\boldsymbol{w}\_{i}^{{}^{\prime}}-\boldsymbol{\zeta}\_{i,w}\Big\|&=&O\_{p}(\Delta\_{n}^{1/2}).\end{array} |  | (A.13) |

The first line directly follows from Assumption [1](https://arxiv.org/html/2510.12911v1#Thmassumption1 "Assumption 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."). Note that |i​Δn−t|→0|i\Delta\_{n}-t|\to 0 for any i∈ℐn,ti\in\mathcal{I}\_{n,t} as Δn→0\Delta\_{n}\to 0 and this implies ‖𝝈t−𝝈(i−1)​Δn‖=Op​(Δn1/2)\|\boldsymbol{\sigma}\_{t}-\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}}\|=O\_{p}(\Delta\_{n}^{1/2}). For notational convenience, I only consider the third line and the same steps can be adopted for the second line as well. Specifically, one can write:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝝈t−1​𝒘i′−𝜻i,w‖≤‖𝝈t−1‖⋅‖𝒘i′−𝝈t​𝜻i,w‖=∥𝝈t−1∥⋅∥𝒘i′−diag(𝒄t)1/2supτ,s∈𝒯n,iϱt(𝑾τ−𝑾sΔn)∥=‖𝝈t−1‖⋅‖𝒘i′−supτ,s∈𝒯n,i𝝈t​(𝑾τ−𝑾sΔn)‖=‖𝝈t−1‖⋅‖supτ,s∈𝒯n,i(𝝈t−𝝈(i−1)​Δn)​(𝑾τ−𝑾sΔn)‖=Op​(Δn1/2)\begin{array}[]{rcl}\|\boldsymbol{\sigma}^{-1}\_{t}\boldsymbol{w}\_{i}^{{}^{\prime}}-\boldsymbol{\zeta}\_{i,w}\|&\leq&\|\boldsymbol{\sigma}\_{t}^{-1}\|\cdot\|\boldsymbol{w}\_{i}^{{}^{\prime}}-\boldsymbol{\sigma}\_{t}\boldsymbol{\zeta}\_{i,w}\|\vskip 10.00002pt\\ &=&\|\boldsymbol{\sigma}\_{t}^{-1}\|\cdot\Big\|\boldsymbol{w}\_{i}^{{}^{\prime}}-\operatorname{diag}(\boldsymbol{c}\_{t})^{1/2}\sup\_{\tau,s\in\mathcal{T}\_{n,i}}\boldsymbol{\varrho}\_{t}\left(\frac{\boldsymbol{W}\_{\tau}-\boldsymbol{W}\_{s}}{\sqrt{\Delta\_{n}}}\right)\Big\|\vskip 10.00002pt\\ &=&\|\boldsymbol{\sigma}\_{t}^{-1}\|\cdot\Big\|\boldsymbol{w}\_{i}^{{}^{\prime}}-\sup\_{\tau,s\in\mathcal{T}\_{n,i}}\boldsymbol{\sigma}\_{t}\left(\frac{\boldsymbol{W}\_{\tau}-\boldsymbol{W}\_{s}}{\sqrt{\Delta\_{n}}}\right)\Big\|\vskip 10.00002pt\\ &=&\|\boldsymbol{\sigma}\_{t}^{-1}\|\cdot\Big\|\sup\_{\tau,s\in\mathcal{T}\_{n,i}}(\boldsymbol{\sigma}\_{t}-\boldsymbol{\sigma}\_{(i-1)\Delta\_{n}})\left(\frac{\boldsymbol{W}\_{\tau}-\boldsymbol{W}\_{s}}{\sqrt{\Delta\_{n}}}\right)\Big\|\vskip 10.00002pt\\ &=&O\_{p}(\Delta\_{n}^{1/2})\\ \end{array} |  | (A.14) |

where the first line follows from sub-multiplicative property of matrix norm, the second and third lines use the definition of 𝜻i,w\boldsymbol{\zeta}\_{i,w} and ϱt\boldsymbol{\varrho}\_{t}, the fourth line is a direct implication of sup\sup definition and the last line uses Assumption [1](https://arxiv.org/html/2510.12911v1#Thmassumption1 "Assumption 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.") and properties of Brownian motion.

Step 2: Rewrite the main statement of the proposition as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝝈t−1​𝒄^n,t​(λ)​𝝈t−⊤−Un,t‖\displaystyle\left\|\boldsymbol{\sigma}\_{t}^{-1}\widehat{\boldsymbol{c}}\_{n,t}(\lambda)\boldsymbol{\sigma}\_{t}^{-\top}-U\_{n,t}\right\| | =∥1k∑i∈ℐn,t{λ1(𝝈t−1𝒓i)(𝝈t−1𝒓i)⊤−𝜻i,r𝜻i,r⊤}\displaystyle=\Bigg\|\frac{1}{k}\sum\_{i\in\mathcal{I}\_{n,t}}\left\{\lambda\_{1}(\boldsymbol{\sigma}\_{t}^{-1}\boldsymbol{r}\_{i})(\boldsymbol{\sigma}\_{t}^{-1}\boldsymbol{r}\_{i})^{\top}-\boldsymbol{\zeta}\_{i,r}\boldsymbol{\zeta}\_{i,r}^{\top}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1k​∑i∈ℐn,t{λ2​(𝝈t−1​𝒂i)​(𝝈t−1​𝒂i)⊤−𝜻i,a​𝜻i,a⊤}\displaystyle\quad+\frac{1}{k}\sum\_{i\in\mathcal{I}\_{n,t}}\left\{\lambda\_{2}(\boldsymbol{\sigma}\_{t}^{-1}\boldsymbol{a}\_{i})(\boldsymbol{\sigma}\_{t}^{-1}\boldsymbol{a}\_{i})^{\top}-\boldsymbol{\zeta}\_{i,a}\boldsymbol{\zeta}\_{i,a}^{\top}\right\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1k∑i∈ℐn,t{λ3(𝝈t−1𝒘i)(𝝈t−1𝒘i)⊤−𝜻i,w𝜻i,w⊤}∥\displaystyle\quad+\frac{1}{k}\sum\_{i\in\mathcal{I}\_{n,t}}\left\{\lambda\_{3}(\boldsymbol{\sigma}\_{t}^{-1}\boldsymbol{w}\_{i})(\boldsymbol{\sigma}\_{t}^{-1}\boldsymbol{w}\_{i})^{\top}-\boldsymbol{\zeta}\_{i,w}\boldsymbol{\zeta}\_{i,w}^{\top}\right\}\Bigg\| |  | (A.15) |

Using the results from Step 1, it follows that the terms in curly brackets are Op​(Δn1/2)O\_{p}(\Delta\_{n}^{1/2}) for any i∈ℐn,ti\in\mathcal{I}\_{n,t} and fixed λ=(λ1,λ2,λ3)⊤\lambda=(\lambda\_{1},\lambda\_{2},\lambda\_{3})^{\top}. Therefore, the entire expression is Op​(Δn1/2)=op​(1)O\_{p}(\Delta\_{n}^{1/2})=o\_{p}(1). This completes the proof.

∎

### A.2 Proof of Proposition [2](https://arxiv.org/html/2510.12911v1#Thmproposition2 "Proposition 2. ‣ 3.2 Testing on Spot Beta ‣ 3 Spot Beta Estimation and Inference with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu.")

Now, I provide the proof of Proposition [2](https://arxiv.org/html/2510.12911v1#Thmproposition2 "Proposition 2. ‣ 3.2 Testing on Spot Beta ‣ 3 Spot Beta Estimation and Inference with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."), which establishes the coupling result for the test statistic defined as:

|  |  |  |
| --- | --- | --- |
|  | T^n=k−1​(β^n,t−βt)ς^n,t/ν^n,t.\widehat{T}\_{n}=\frac{\sqrt{k-1}\left(\widehat{\beta}\_{n,t}-\beta\_{t}\right)}{\sqrt{\widehat{\varsigma}\_{n,t}/\widehat{\nu}\_{n,t}}}. |  |

The proof is based on the algebraic manipulations of the previous proposition. For convenience, I restate the proposition here:

###### Proposition 2.

Under the conditions of Proposition 1, for any fixed k≥2k\geq 2 and λ\lambda, the following holds as Δn→0\Delta\_{n}\to 0:

|  |  |  |
| --- | --- | --- |
|  | |T^n−T~n|=op​(1)whereT~n≡k−1​[Un,t−1]12[Un,t−1]11​[Un,t−1]22−[Un,t−1]122.|\widehat{T}\_{n}-\widetilde{T}\_{n}|=o\_{p}(1)\quad\text{where}\quad\widetilde{T}\_{n}\equiv\frac{\sqrt{k-1}[U\_{n,t}^{-1}]\_{12}}{\sqrt{[U\_{n,t}^{-1}]\_{11}[U\_{n,t}^{-1}]\_{22}-[U\_{n,t}^{-1}]\_{12}^{2}}}. |  |

###### Proof.

Fix k≥2k\geq 2 and λ\lambda. By Proposition [1](https://arxiv.org/html/2510.12911v1#Thmproposition1 "Proposition 1. ‣ 2.4.2 Asymptotic Approximation for the Risk Function ‣ 2.4 Finding the “Optimal” Weights ‣ 2 Spot Covariance Estimation with Candlesticks ‣ Beyond Returns: A Candlestick-Based Approach to Spot Covariance Estimation1footnote 11footnote 1I am very grateful to Andrew J. Patton, Tim Bollerslev and Anna Bykhovskaya for their guidance and support. I would also like to thank Anna Cieslak, Mehmet Caner, Peter R. Hansen, Ilze Kalnina, Raul Guarini Riva, Adam Rosen, George Tauchen, Christopher Walker and seminar participants at Duke University, 2025 Triangle Econometrics Conference, and 2025 Annual Meeting of SoFiE for their helpful comments and suggestions. Email: yasin.simsek@duke.edu."), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝝈t−1​𝒄^n,t​(λ)​𝝈t−⊤−Un,t‖=op​(1).\left\|\boldsymbol{\sigma}\_{t}^{-1}\widehat{\boldsymbol{c}}\_{n,t}(\lambda)\boldsymbol{\sigma}\_{t}^{-\top}-U\_{n,t}\right\|=o\_{p}(1). |  | (A.16) |

Note that both 𝝈t−1​𝒄^n,t​(λ)​𝝈t−⊤\boldsymbol{\sigma}\_{t}^{-1}\widehat{\boldsymbol{c}}\_{n,t}(\lambda)\boldsymbol{\sigma}\_{t}^{-\top} and Un,tU\_{n,t} are positive definite matrices. Therefore, by the continuity of matrix inversion operator on the set of positive definite matrices, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(𝝈t−1​𝒄^n,t​(λ)​𝝈t−1⊤)−1−Un,t−1‖=op​(1).\left\|(\boldsymbol{\sigma}\_{t}^{-1}\widehat{\boldsymbol{c}}\_{n,t}(\lambda)\boldsymbol{\sigma}\_{t}^{-1\top})^{-1}-U\_{n,t}^{-1}\right\|=o\_{p}(1). |  | (A.17) |

This implies that each element of the matrix (𝝈t−1​𝒄^n,t​(λ)​𝝈t−⊤)−1(\boldsymbol{\sigma}\_{t}^{-1}\widehat{\boldsymbol{c}}\_{n,t}(\lambda)\boldsymbol{\sigma}\_{t}^{-\top})^{-1} converges to the corresponding element of Un,t−1U\_{n,t}^{-1} in probability. These relations can be written in explicit forms as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |(νtν^n,t+νt​(βt−β^n,t)2ς^n,t)−[Un,t−1]11|\displaystyle\left|\left(\frac{\nu\_{t}}{\widehat{\nu}\_{n,t}}+\frac{\nu\_{t}(\beta\_{t}-\widehat{\beta}\_{n,t})^{2}}{\widehat{\varsigma}\_{n,t}}\right)-[U\_{n,t}^{-1}]\_{11}\right| | =op​(1)\displaystyle=o\_{p}(1) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |(νt1/2​ςt1/2​(βt−β^n,t)ς^n,t)−[Un,t−1]12|\displaystyle\left|\left(\frac{\nu\_{t}^{1/2}\varsigma\_{t}^{1/2}(\beta\_{t}-\widehat{\beta}\_{n,t})}{\widehat{\varsigma}\_{n,t}}\right)-[U\_{n,t}^{-1}]\_{12}\right| | =op​(1)\displaystyle=o\_{p}(1) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |ςtς^n,t−[Un,t−1]22|\displaystyle\left|\frac{\varsigma\_{t}}{\widehat{\varsigma}\_{n,t}}-[U\_{n,t}^{-1}]\_{22}\right| | =op​(1).\displaystyle=o\_{p}(1). |  |

Using the second and third lines, one can write:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |(β^n,t−βt)ςn,t/νn,t−[Un,t−1]12[Un,t−1]22|=op​(1).\left|\frac{(\widehat{\beta}\_{n,t}-\beta\_{t})}{\sqrt{{\varsigma}\_{n,t}/{\nu}\_{n,t}}}-\frac{[U\_{n,t}^{-1}]\_{12}}{[U\_{n,t}^{-1}]\_{22}}\right|=o\_{p}(1). |  | (A.18) |

Moreover, from all three lines, one can deduce that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |νtν^n,t−([Un,t−1]11−[Un,t−1]122[Un,t−1]22)|=op​(1).\left|\frac{\nu\_{t}}{\widehat{\nu}\_{n,t}}-\left([U\_{n,t}^{-1}]\_{11}-\frac{[U\_{n,t}^{-1}]\_{12}^{2}}{[U\_{n,t}^{-1}]\_{22}}\right)\right|=o\_{p}(1). |  | (A.19) |

Finally, combining the above equations yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |k−1​(β^n,t−βt)ς^n,t/ν^n,t−k−1​[Un,t−1]12[Un,t−1]11​[Un,t−1]22−[Un,t−1]122|=op​(1).\left|\frac{\sqrt{k-1}(\widehat{\beta}\_{n,t}-\beta\_{t})}{\sqrt{\widehat{\varsigma}\_{n,t}/\widehat{\nu}\_{n,t}}}-\frac{\sqrt{k-1}[U\_{n,t}^{-1}]\_{12}}{\sqrt{[U\_{n,t}^{-1}]\_{11}[U\_{n,t}^{-1}]\_{22}-[U\_{n,t}^{-1}]\_{12}^{2}}}\right|=o\_{p}(1). |  | (A.20) |

as required.

∎