---
authors:
- Stanisław Drożdż
- Robert Kluszczyński
- Jarosław Kwapień
- Marcin Wątorek
doc_id: arxiv:2510.13785v1
family_id: arxiv:2510.13785
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2510.13785v1
url_html: https://arxiv.org/html/2510.13785v1
venue: arXiv q-fin
version: 1
year: 2025
---

###### Abstract

Multifractality in time series analysis characterizes the presence of multiple scaling exponents, indicating heterogeneous temporal structures and complex dynamical behaviors beyond simple monofractal models. In the context of digital currency markets, multifractal properties arise due to the interplay of long-range temporal correlations and heavy-tailed distributions of returns, reflecting intricate market microstructure and trader interactions. Incorporating multifractal analysis into the modeling of cryptocurrency price dynamics enhances the understanding of market inefficiencies, may improve volatility forecasting and facilitate the detection of critical transitions or regime shifts. Based on the multifractal cross-correlation analysis (MFCCA) whose spacial case is the multifractal detrended fluctuation analysis (MFDFA), as the most commonly used practical tools for quantifying multifractality, in the present contribution a recently proposed method of disentangling sources of multifractality in time series was applied to the most representative instruments from the digital market. They include Bitcoin (BTC), Ethereum (ETH), decentralized exchanges (DEX) and non-fungible tokens (NFT). The results indicate the significant role of heavy tails in generating a broad multifractal spectrum. However, they also clearly demonstrate that the primary source of multifractality are temporal correlations in the series, and without them, multifractality fades out. It appears characteristic that these temporal correlations, to a large extent, do not depend on the thickness of the tails of the fluctuation distribution. These observations, made here in the context of the digital currency market, provide a further strong argument for the validity of the proposed methodology of disentangling sources of multifractality in time series.

###### keywords:

complexity; time series analysis; nonlinear correlations; multifractality; singularity spectra; qq-Gaussian distributions; digital financial instruments

\pubvolume

1
\issuenum1
\articlenumber0
\datereceived
\dateaccepted
\datepublished
\hreflinkhttps://doi.org/
\TitleMultifractality and its sources in the digital currency market
\TitleCitationMultifractality sources
\AuthorStanisław Drożdż 1,2,‡\orcidA, Robert Kluszczyński 2,3,‡\orcidB, Jarosław Kwapień 2,‡\orcidC and Marcin Wątorek 1,‡\orcidD\AuthorNamesStanisław Drożdż, Robert Kluszczyński, Jarosław Kwapień and Marcin Wątorek\AuthorCitationDrożdż, S.; Kluszczyński. R.; Kwapień. J.: Wątorek. M.
\corresCorrespondence: jaroslaw.kwapien@ifj.edu.pl (J.K.)
\secondnoteThese authors contributed equally to this work.

## 1 Introduction

The rapid evolution of digital currency markets that has followed introduction of Bitcoin in 2009 — the first asset entirely based on the then newly introduced blockchain technology Nakamoto ([2008](https://arxiv.org/html/2510.13785v1#bib.bib1)) — has substantially influenced the global financial landscape Wątorek et al. ([2021](https://arxiv.org/html/2510.13785v1#bib.bib2)). As decentralized technologies challenge traditional monetary frameworks, cryptocurrencies such as Bitcoin, Ethereum, and thousands of altcoins have introduced new dynamics characterized by extreme volatility Corbet et al. ([2022](https://arxiv.org/html/2510.13785v1#bib.bib3)); Evrim Mandaci and Cagli ([2022](https://arxiv.org/html/2510.13785v1#bib.bib4)); Nguyen et al. ([2023](https://arxiv.org/html/2510.13785v1#bib.bib5)), heavy-tailed distributions Drożdż et al. ([2018](https://arxiv.org/html/2510.13785v1#bib.bib6)); Stosic et al. ([2018](https://arxiv.org/html/2510.13785v1#bib.bib7)); James et al. ([2021](https://arxiv.org/html/2510.13785v1#bib.bib8)); Drożdż et al. ([2023](https://arxiv.org/html/2510.13785v1#bib.bib9)), and long-range temporal correlations Drożdż et al. ([2018](https://arxiv.org/html/2510.13785v1#bib.bib6)); Takaishi ([2018](https://arxiv.org/html/2510.13785v1#bib.bib10)); Takaishi and Adachi ([2020](https://arxiv.org/html/2510.13785v1#bib.bib11)); James ([2021](https://arxiv.org/html/2510.13785v1#bib.bib12)); James and Menzies ([2022](https://arxiv.org/html/2510.13785v1#bib.bib13)); Wątorek et al. ([2022](https://arxiv.org/html/2510.13785v1#bib.bib14)); Brouty and Garcin ([2024](https://arxiv.org/html/2510.13785v1#bib.bib15)); Bui et al. ([2025](https://arxiv.org/html/2510.13785v1#bib.bib16)). These dynamics render conventional econometric models insufficient, necessitating more sophisticated tools to understand the intrinsic complexity of digital asset price behavior Kwapień and Drożdż ([2012](https://arxiv.org/html/2510.13785v1#bib.bib17)); Wątorek et al. ([2021](https://arxiv.org/html/2510.13785v1#bib.bib2)); James et al. ([2021](https://arxiv.org/html/2510.13785v1#bib.bib8)); Manavi et al. ([2020](https://arxiv.org/html/2510.13785v1#bib.bib18)); Spurr and Ausloos ([2021](https://arxiv.org/html/2510.13785v1#bib.bib19)); James and Menzies ([2022](https://arxiv.org/html/2510.13785v1#bib.bib20)). One such tool is multifractal analysis Jiang et al. ([2019](https://arxiv.org/html/2510.13785v1#bib.bib21)), a framework that extends beyond linear descriptions to capture variability in scaling properties across time and magnitudes of fluctuations.

Multifractality, or multifractal scaling, refers to the presence of multiple scaling exponents in a time series, indicating heterogeneity in local singularities Halsey et al. ([1986](https://arxiv.org/html/2510.13785v1#bib.bib22)). Unlike monofractal processes, which exhibit uniform scaling behavior, multifractal processes capture a spectrum of exponents that reflect the system’s complexity across scales. In financial contexts, this translates to the convoluted periods of high and low volatility Farmer et al. ([2004](https://arxiv.org/html/2510.13785v1#bib.bib23)), the related clustering of extreme events Mandelbrot ([1963](https://arxiv.org/html/2510.13785v1#bib.bib24)), and long-range dependences Ausloos and Ivanova ([2002](https://arxiv.org/html/2510.13785v1#bib.bib25)); Kutner and Świtała ([2004](https://arxiv.org/html/2510.13785v1#bib.bib26)); Cont ([2007](https://arxiv.org/html/2510.13785v1#bib.bib27)); Oh et al. ([2008](https://arxiv.org/html/2510.13785v1#bib.bib28)). These features are prominently observable in digital currency markets, where trading occurs globally, continuously, and with limited regulation Wątorek et al. ([2021](https://arxiv.org/html/2510.13785v1#bib.bib2)). Yet, despite widespread recognition of multifractality in financial data, its sources remain a subject of ongoing debate Zhou ([2009](https://arxiv.org/html/2510.13785v1#bib.bib29)); Barunik et al. ([2012](https://arxiv.org/html/2510.13785v1#bib.bib30)); Green et al. ([2014](https://arxiv.org/html/2510.13785v1#bib.bib31)); Morales et al. ([2014](https://arxiv.org/html/2510.13785v1#bib.bib32)); Klamut et al. ([2020](https://arxiv.org/html/2510.13785v1#bib.bib33)); Kutner et al. ([2019](https://arxiv.org/html/2510.13785v1#bib.bib34)); Kwapień et al. ([2023](https://arxiv.org/html/2510.13785v1#bib.bib35)).

A recent study by Kluszczyński et al. Kluszczyński et al. ([2025](https://arxiv.org/html/2510.13785v1#bib.bib36)) addresses this issue on a fully quantitative level by rigorously examining the relative role of the two allegedly principal sources of multifractality: (1) temporal correlations, particularly long-range nonlinear correlations, and (2) heavy-tailed probability distribution functions (PDFs) of fluctuations. Their findings ultimately disqualify the dichotomy still appearing in the literature that treats these sources as independent contributors. Using a combination of synthetic cascades and empirical data, they demonstrate that true multifractality requires temporal correlations — heavy tails alone cannot produce multifractal spectra unless such correlations are present. In fact, fat-tailed distributions, modeled via qq-Gaussian frameworks, were found to merely modulate the width of the multifractal spectrum, but only in the presence of underlying correlations, as already indicated by earlier published works Drożdż et al. ([2009](https://arxiv.org/html/2510.13785v1#bib.bib37)); Zhou ([2012](https://arxiv.org/html/2510.13785v1#bib.bib38)); Kwapień et al. ([2023](https://arxiv.org/html/2510.13785v1#bib.bib35)).

This insight has direct relevance to digital currency markets. Cryptocurrencies are notorious for their non-Gaussian returns, often displaying kurtosis even exceeding that of traditional financial assets Wątorek et al. ([2021](https://arxiv.org/html/2510.13785v1#bib.bib39)). However, the findings of Ref. Kluszczyński et al. ([2025](https://arxiv.org/html/2510.13785v1#bib.bib36)) imply that such statistical events do not, on their own, confirm multifractality. To discern whether the multifractal behavior in crypto markets is genuine or an artifact of finite sample size and fat tails, one must isolate and analyze the role of correlation structure. This can be done by applying multifractal detrended fluctuation analysis (MFDFA) Kantelhardt et al. ([2002](https://arxiv.org/html/2510.13785v1#bib.bib40)) as the central tool, alongside reshuffling and qq-Gaussian filtering techniques, to distinguish between sources of multifractal complexity.

For the global digital currency markets, this methodological rigor is especially crucial. The presence of algorithmic trading Makarov and Schoar ([2020](https://arxiv.org/html/2510.13785v1#bib.bib41)); Cohen and Qadan ([2022](https://arxiv.org/html/2510.13785v1#bib.bib42)); Fang et al. ([2022](https://arxiv.org/html/2510.13785v1#bib.bib43)); Cohen ([2023](https://arxiv.org/html/2510.13785v1#bib.bib44)); Wątorek et al. ([2023](https://arxiv.org/html/2510.13785v1#bib.bib45)), speculative bubbles Gerlach et al. ([2019](https://arxiv.org/html/2510.13785v1#bib.bib46)); Huber and Sornette ([2022](https://arxiv.org/html/2510.13785v1#bib.bib47)), and geopolitical shocks Bouri et al. ([2022](https://arxiv.org/html/2510.13785v1#bib.bib48)); Hong and Yoon ([2022](https://arxiv.org/html/2510.13785v1#bib.bib49)); Khalfaoui et al. ([2023](https://arxiv.org/html/2510.13785v1#bib.bib50)); Wątorek et al. ([2023](https://arxiv.org/html/2510.13785v1#bib.bib51)); Fang et al. ([2024](https://arxiv.org/html/2510.13785v1#bib.bib52)) introduces complex dependencies that may mimic or obscure genuine multifractal behavior. Also, social media influence on investor behavior can be substantial Poongodi et al. ([2021](https://arxiv.org/html/2510.13785v1#bib.bib53)); Aharon et al. ([2022](https://arxiv.org/html/2510.13785v1#bib.bib54)) with the NFT market being particularly susceptible to this effect as a single message may cause a significant increase in volatility Szydło et al. ([2024](https://arxiv.org/html/2510.13785v1#bib.bib55)); Wątorek et al. ([2024](https://arxiv.org/html/2510.13785v1#bib.bib56)). By leveraging the framework developed in Kluszczyński et al. ([2025](https://arxiv.org/html/2510.13785v1#bib.bib36)), this paper aims to systematically assess the multifractal properties of major cryptocurrencies across global exchanges. In particular, we examine how the singularity spectrum widths and asymmetries evolve with market maturity, regulation, and technological development.

Our present contribution is twofold. First, we apply advanced multifractal analysis techniques to a comprehensive dataset of global digital currency price series, including Bitcoin (BTC), Ethereum (ETH), also from the decentralized trading, and emerging non-fungible token market, spanning several years and exchanges. Second, by adopting the disentangling approach Kluszczyński et al. ([2025](https://arxiv.org/html/2510.13785v1#bib.bib36)), we present evidence that observed multifractality is driven by temporal correlations — indicative of market memory and structure — and, when such temporal correlations related to volatility clustering are present, the distributional features such as fat tails and extreme events significantly broaden the singularity spectrum. This inspection provides deeper insight into the dynamics of digital asset markets and offers a more solid foundation for modeling them.

## 2 Materials and Methods

### 2.1 Data and its characteristics

In this study, we examine high-frequency data obtained from Binance [Binance](https://arxiv.org/html/2510.13785v1#bib.bib57) , the largest cryptocurrency exchange by daily trading volume [CoinMarketCap](https://arxiv.org/html/2510.13785v1#bib.bib58) . Specifically, we analyze the price time series {p​(ti)}i=1T\{p(t\_{i})\}\_{i=1}^{T} for two major cryptocurrencies: BTC and ETH, expressed in USDT. The data were sampled at regular intervals of Δ​t=1\Delta t=1 min, where Δ​t=ti+1−ti\Delta t=t\_{i+1}-t\_{i} and i=1,…,T−1i=1,\ldots,T-1. The chosen 1-minute resolution is the highest possible to minimize the number of zero log-returns (such returns usually distort results of a multifractal analysis at small time scales comparable with the average zero-return interval). Reducing the resolution by taking larger Δ​t\Delta t would reduce the thickness of the distribution’s tails Wątorek et al. ([2021](https://arxiv.org/html/2510.13785v1#bib.bib39)).

Given that cryptocurrency markets operate continuously, 24 hours a day, 7 days a week, our dataset spanning the period from January 1, 2018, to December 31, 2024 includes 2557 consecutive trading days with a total of T=3,682,080T=3,682,080 data points. This time frame covers the most dynamic periods — including the Covid-19 pandemic James et al. ([2021](https://arxiv.org/html/2510.13785v1#bib.bib8)); Nguyen et al. ([2022](https://arxiv.org/html/2510.13785v1#bib.bib59)); Ammy-Driss and Garcin ([2023](https://arxiv.org/html/2510.13785v1#bib.bib60)) — in the evolution of the two most important cryptocurrencies, i.e., BTC and ETH. From these time series, the logarithmic price returns R​(ti)=ln⁡p​(ti+1)−ln⁡p​(ti)R(t\_{i})=\ln p(t\_{i+1})-\ln p(t\_{i}) are calculated. In terms of the cumulative log-returns R^​(ti)=∑k=1k=iR​(tk){\hat{R}}(t\_{i})=\sum\_{k=1}^{k=i}R(t\_{k}), the relative price changes of these two cryptocurrencies are illustrated in Fig.( [1](https://arxiv.org/html/2510.13785v1#S2.F1 "Figure 1 ‣ 2.1 Data and its characteristics ‣ 2 Materials and Methods")). Such a representation allows us for direct tracking of relative changes in these financial instruments. In the present case of BTC and ETH, the overall trend of their price changes is seen to go largely in parallel in the period considered.

The period before 2018 was not included in the analysis because, as shown in our previous work Drożdż et al. ([2018](https://arxiv.org/html/2510.13785v1#bib.bib6)); Wątorek et al. ([2021](https://arxiv.org/html/2510.13785v1#bib.bib2)), sufficient scaling to determine the characteristics of multifractality has been being observed only since mid-2017. Moreover, the selected data range corresponds to their availability at the appropriate frequency on the Binance exchange, which became the most frequently traded only in 2018 Kwapień et al. ([2022](https://arxiv.org/html/2510.13785v1#bib.bib61)).

![Refer to caption](Figs/szeregiR.eps)


Figure 1: Evolution of the cumulative log-returns R^​(t)\hat{R}(t) of the BTC and ETH over the time period from Jan 1, 2018 to Dec 31, 2024.

The heterogeneity of the cryptocurrency market dynamics over this 7-year period is evident in the distributions of fluctuations in the corresponding 1-min return rates in subsequent 1-year periods, as shown in Fig. [2](https://arxiv.org/html/2510.13785v1#S2.F2 "Figure 2 ‣ 2.1 Data and its characteristics ‣ 2 Materials and Methods"). Of course, these distributions are always fat-tailed, but the tail thickness changes quite significantly in relation to the two reference distributions, which can here be considered, i.e., the stretched exponential P​(X>x)∼exp⁡(−xβ)P(X>x)\sim\exp(-x^{\beta}) and the inverse-cubic power law P​(X>x)∼x−γP(X>x)\sim x^{-\gamma}. As it can be seen, the thickest tails of these distributions, both for BTC and ETH, are observed in 2020, the year of greatest anxiety related to the Covid-19 pandemic. The fitting exponents of the distributions for each year are presented in Tab. [1](https://arxiv.org/html/2510.13785v1#S2.T1 "Table 1 ‣ 2.1 Data and its characteristics ‣ 2 Materials and Methods").

![Refer to caption](Figs/rozkladyR.eps)


Figure 2: Cumulative distribution function for BTC and ETH by year together with Gaussian, power-law (with γ=3\gamma=3) and stretched exponential distributions (with β=0.4\beta=0.4).

Another basic characteristics of the return time series is the autocorrelation function (ACF) defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(τ)=1/T​∑i=1T−1[R​(ti)−⟨R​(ti)⟩ti]​[R​(ti+τ)−⟨R​(ti)⟩ti]σx2,A(\tau)={1/T\sum\_{i=1}^{T-1}\left[R(t\_{i})-\langle R(t\_{i})\rangle\_{t\_{i}}\right]\left[R(t\_{i}+\tau)-\langle R(t\_{i})\rangle\_{t\_{i}}\right]\over\sigma^{2}\_{x}}, |  | (1) |

where σx\sigma\_{x} is the estimated standard deviation of the considered time series, ⟨⋅⟩\langle\cdot\rangle represents the estimated mean, and τ\tau is the time lag expressed in minutes. The ACF calculated from the moduli of log-returns for the same two series and likewise broken down by years are shown in log-log scale in Fig. [3](https://arxiv.org/html/2510.13785v1#S2.F3 "Figure 3 ‣ 2.1 Data and its characteristics ‣ 2 Materials and Methods"). Clearly, they reveal long-range power-law correlations up to 103−10410^{3}-10^{4} minutes, after which the power-law decay ends and the autocorrelation function falls to noise level. The fitting exponents of the autocorrelation functions for each year are presented in Tab/ [1](https://arxiv.org/html/2510.13785v1#S2.T1 "Table 1 ‣ 2.1 Data and its characteristics ‣ 2 Materials and Methods"). Interestingly, the range of such correlations is seen to be larger in 2018 as compared to the more recent years Kwapień et al. ([2022](https://arxiv.org/html/2510.13785v1#bib.bib61)). This may be related to the fact that, over the years, transaction frequency has been increasing on the BTC and ETH markets. This frequency together with a larger information inflow on the market have been a principal factor behind a well-documented observation that some market characteristics like the autocorrelation decay time or the log-return pdf tail index behave as if time flow accelerated when going from past to present Drożdż et al. ([2002](https://arxiv.org/html/2510.13785v1#bib.bib62), [2007](https://arxiv.org/html/2510.13785v1#bib.bib63)). This time flow may be identified as an internal market clock which operates at a non-uniform pace; the distinction between it and universal time is a well known concept in financial econometrics Clark ([1973](https://arxiv.org/html/2510.13785v1#bib.bib64)). (When time becomes to flow faster, everything that used to take place at a given characteristic time scale with a given intensity before, can now be observed with the same intensity at a shorter time scale – for example, the autocorrelation function reaching noise level.)

![Refer to caption](Figs/ACF.eps)


Figure 3: The Pearson autocorrelation function calculated from the return moduli for BTC and ETH broken by year.




Table 1: Basic statistics of the BTC and ETH exchange rate time series considered in this study: the average inter-transaction time δ​t\delta t, the power-law exponent γ\gamma and stretched exponential function parameter β\beta least-square-fitted to the empirical return distributions presented in Fig. [2](https://arxiv.org/html/2510.13785v1#S2.F2 "Figure 2 ‣ 2.1 Data and its characteristics ‣ 2 Materials and Methods") and to empirical autocorrelation functions presented in Fig. [3](https://arxiv.org/html/2510.13785v1#S2.F3 "Figure 3 ‣ 2.1 Data and its characteristics ‣ 2 Materials and Methods").

| year | ⟨δ​t⟩\langle\delta t\rangle [s] | | P​(X>|x|)P(X>|x|) exponents | | ACF γ\gamma exponents | |
| --- | --- | --- | --- | --- | --- | --- |
|  | BTC | ETH | BTC | ETH | BTC | ETH |
| 2018 | 0.361 | 0.604 | β=0.48\beta=0.48 | β=0.48\beta=0.48 | -0.10 | -0.13 |
| 2019 | 0.241 | 0.562 | γ=−2.44\gamma=-2.44, β=0.36\beta=0.36 | γ=−2.58\gamma=-2.58, β=0.39\beta=0.39 | -0.18 | -0.23 |
| 2020 | 0.101 | 0.257 | γ=−2.23\gamma=-2.23 | γ=−2.18\gamma=-2.18 | -0.16 | -0.18 |
| 2021 | 0.047 | 0.065 | γ=−2.58\gamma=-2.58 | γ=−2.66\gamma=-2.66 | -0.16 | -0.14 |
| 2022 | 0.026 | 0.096 | γ=−2.83\gamma=-2.83 | γ=−2.76\gamma=-2.76, β=0.39\beta=0.39 | -0.16 | -0.15 |
| 2023 | 0.034 | 0.145 | γ=−2.44\gamma=-2.44 | γ=−2.37\gamma=-2.37 | -0.23 | -0.25 |
| 2024 | 0.045 | 0.069 | γ=−3.12\gamma=-3.12 | γ=−3\gamma=-3 | -0.19 | -0.21 |

### 2.2 Multifractal formalism

Among the various methods available for fractal analysis of time series, MFDFA Kantelhardt et al. ([2002](https://arxiv.org/html/2510.13785v1#bib.bib40)) has been recognized as one of the most robust and reliable techniques Oświęcimka et al. ([2006](https://arxiv.org/html/2510.13785v1#bib.bib65)). This method is specifically designed to handle nonstationary data by systematically removing trends across multiple time scales and analyzing the statistical characteristics of the resulting fluctuations. An extension of this approach, known as the multifractal cross-correlation analysis (MFCCA Oświęcimka et al. ([2014](https://arxiv.org/html/2510.13785v1#bib.bib66))), enables the detection of multiscale cross-correlations between two concurrent nonstationary time series Podobnik and Stanley ([2008](https://arxiv.org/html/2510.13785v1#bib.bib67)); Zhou ([2008](https://arxiv.org/html/2510.13785v1#bib.bib68)); Horvatic et al. ([2011](https://arxiv.org/html/2510.13785v1#bib.bib69)). In the following, we provide a brief overview of the MFCCA methodology.

Consider two nonstationary time series, X={Xi}i=1T{\rm X}=\{X\_{i}\}\_{i=1}^{T} and Y={Yi}i=1TY=\{Y\_{i}\}\_{i=1}^{T}, uniformly sampled at intervals of Δ​t\Delta t. To begin the analysis, each series is divided into Ms=2​⌊T/s⌋M\_{s}=2\lfloor T/s\rfloor non-overlapping segments of length ss, where the division is performed from both the beginning (i=1i=1) and the end (i=Ti=T) of the series. Here, ⌊⋅⌋\lfloor\cdot\rfloor denotes the floor function. Within each segment, the time series is integrated, and a polynomial trend Pνm​(j)P\_{\nu}^{m}(j) of degree mm is subsequently removed from the integrated signal:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xj​(s,ν)=∑k=1jXj​(ν−1)+k−Pνm​(j),j=1,…,s,ν=1,…,Ms.x\_{j}(s,\nu)=\sum\_{k=1}^{j}X\_{j(\nu-1)+k}-P\_{\nu}^{m}(j),\quad j=1,...,s,\quad\nu=1,...,M\_{s}. |  | (2) |

Usually, a polynomial of degree m=2m=2 constitutes a reasonable choice Oświęcimka et al. ([2013](https://arxiv.org/html/2510.13785v1#bib.bib70)). Thus, in each segment, a detrended covariance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fXY2​(s,ν)=1s​∑j=1s[xj​(s,ν)−⟨xj​(s,ν)⟩j]​[yj​(s,ν)−⟨yj​(s,ν)⟩j],f\_{\rm XY}^{2}(s,\nu)={1\over s}\sum\_{j=1}^{s}\left[x\_{j}(s,\nu)-\langle x\_{j}(s,\nu)\rangle\_{j}\right]\left[y\_{j}(s,\nu)-\langle y\_{j}(s,\nu)\rangle\_{j}\right], |  | (3) |

is calculated, where ⟨⋅⟩j\langle\cdot\rangle\_{j} denotes the averaging over jj. The covariances in all segments and then the signed moments of order rr are calculated. These are called the bivariate fluctuation functions of ss:

|  |  |  |  |
| --- | --- | --- | --- |
|  | FrXY​(s)={1Ms​∑ν=1Mssign​[fXY2​(s,ν)]​|fXY2​(s,ν)|r/2}1/r.F\_{r}^{\rm XY}(s)=\big\{{1\over M\_{s}}\sum\_{\nu=1}^{M\_{s}}{\rm sign}[f\_{\rm XY}^{2}(s,\nu)]|f\_{\rm XY}^{2}(s,\nu)|^{r/2}\big\}^{1/r}. |  | (4) |

Because covariances can take negative values, using their absolute value ensures that FrXYF\_{r}^{\rm XY} remains real-valued, while the inclusion of the sign function preserves the consistency of the analysis Oświęcimka et al. ([2014](https://arxiv.org/html/2510.13785v1#bib.bib66)). The nature of the functional dependence of FrXYF\_{r}^{\rm XY} on the scale ss enables one to differentiate between fractal time series and those lacking such properties. Of particular interest are time series for which the fluctuation functions display power-law scaling over a sufficient range of moments rr and scales ss:

|  |  |  |  |
| --- | --- | --- | --- |
|  | FrXY​(s)∼sλ​(r),F\_{r}^{\rm XY}(s)\sim s^{\lambda(r)}, |  | (5) |

Here, λ​(r)\lambda(r) serves as the bivariate generalized Hurst exponent. In the case of monofractal cross-correlations, λ​(r)\lambda(r) remains constant for all values of rr, i.e., λ​(r)=const\lambda(r)=\mathrm{const}. Conversely, multifractal cross-correlations are characterized by a monotonically decreasing λ​(r)\lambda(r) as a function of rr.

A special case of FrXYF\_{r}^{\rm XY} arises when X=Y{\rm X}={\rm Y}, in which the detrended cross-correlations reduce to detrended autocorrelations. In this situation, both the sign function and the absolute value in Eq. ([4](https://arxiv.org/html/2510.13785v1#S2.E4 "In 2.2 Multifractal formalism ‣ 2 Materials and Methods")) can be omitted, as the detrended variance fX2f\_{\rm X}^{2} is always non-negative. Consequently, the MFCCA reduces to the standard MFDFA, yielding univariate fluctuation functions FrXX​(s)F\_{r}^{\rm XX}(s) and FrYY​(s)F\_{r}^{\rm YY}(s). Here, the detrended cross-correlation function represents the mean covariance, while FrXXF\_{r}^{\rm XX} and FrYYF\_{r}^{\rm YY} correspond to the mean variances. If these univariate fluctuation functions follow a power-law scaling with respect to ss, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | FrXX​(s)∼shX​(r)FrYY​(s)∼shY​(r),F\_{r}^{\rm XX}(s)\sim s^{h\_{\rm X}(r)}\\ \\ \\ \\ \ \ \ \ \ \ \ \ F\_{r}^{\rm YY}(s)\sim s^{h\_{\rm Y}(r)}, |  | (6) |

the exponents hX​(r)h\_{\rm X}(r) and hY​(r)h\_{\rm Y}(r) are identified as the generalized Hurst exponents. For r=2r=2, they reduce to the classical Hurst exponent HH.

A standard approach to characterize the multifractality of data is through the singularity spectrum f​(α)f(\alpha). It is obtained from h​(r)h(r) via the Legendre transform:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | α\displaystyle\alpha | =\displaystyle= | h​(r)+r​h′​(r),\displaystyle h(r)+rh^{\prime}(r), |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | f​(α)\displaystyle f(\alpha) | =\displaystyle= | r​[α−h​(r)]+1,\displaystyle r\left[\alpha-h(r)\right]+1, |  | (7) |

where α\alpha quantifies the intensity of a local singularity and corresponds to the Hölder exponent Halsey et al. ([1986](https://arxiv.org/html/2510.13785v1#bib.bib22)). Geometrically, f​(α)f(\alpha) represents the fractal dimension of the subset of the data whose Hölder exponent equals α\alpha. For a monofractal time series, (α,f​(α))(\alpha,f(\alpha)) collapses to a single point, whereas for a multifractal, it forms a concave curve with downward-pointing shoulders. The broader the spectrum, the stronger the multifractality, making it a useful measure of time series complexity. Its quantitative extent is often expressed by the spectrum width:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​α:=αmax−αmin=α​(rmin)−α​(rmax).\Delta\alpha:=\alpha\_{\rm max}-\alpha\_{\rm min}=\alpha(r\_{\rm min})-\alpha(r\_{\rm max}). |  | (8) |

Alternatively, these properties can be described by the scaling function τ​(r)\tau(r), defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ​(r)=r​h​(r)−1.\tau(r)=rh(r)-1. |  | (9) |

In the monofractal case, τ​(r)\tau(r) varies linearly with rr (since h​(r)h(r) is constant), whereas for multifractal series, it becomes nonlinear.

While for synthetic series f​(α)f(\alpha) is typically symmetric, in realistic cases it may also appear distorted and asymmetric, indicating that data points of different magnitudes possess distinct hierarchical organization Ohashi et al. ([2003](https://arxiv.org/html/2510.13785v1#bib.bib71)); Cao et al. ([2013](https://arxiv.org/html/2510.13785v1#bib.bib72)); Drożdż and Oświęcimka ([2015](https://arxiv.org/html/2510.13785v1#bib.bib73)); Gómez-Gómez et al. ([2021](https://arxiv.org/html/2510.13785v1#bib.bib74)).
Thus, another characteristic of the multifractal spectrum is its asymmetry, which reveals additional aspects of the data temporal organization. The related asymmetry parameter is defined Drożdż and Oświęcimka ([2015](https://arxiv.org/html/2510.13785v1#bib.bib73)) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Aα=(Δ​αL−Δ​αR)/(Δ​αL+Δ​αR)​ ,A\_{\alpha}=(\Delta\alpha\_{\textrm{L}}-\Delta\alpha\_{\textrm{R}})/(\Delta\alpha\_{\textrm{L}}+\Delta\alpha\_{\textrm{R}})\textrm{ ,} |  | (10) |

where Δ​αL=α0−αmin\Delta\alpha\_{\textrm{L}}=\alpha\_{0}-\alpha\_{\textrm{min}} and Δ​αR=αmax−α0\Delta\alpha\_{\textrm{R}}=\alpha\_{\textrm{max}}-\alpha\_{0}. α0\alpha\_{0} denotes α\alpha for which f​(α)f(\alpha) reaches maximum.
Left-sided asymmetry indicates that multifractality is dominated more by large events and the small ones are contracted more towards noise. The opposite applies to right-sided asymmetry where multifractality is dominated by small events; large ones lose hierarchical organization.

### 2.3 Detrended cross-correlation coefficient

Having calculated all fluctuation functions, one can then also introduce the qq-dependent detrended cross-correlation coefficient ρq​(s)\rho\_{q}(s) Kwapień et al. ([2015](https://arxiv.org/html/2510.13785v1#bib.bib75)) defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρr​(s)=FrXY​(s)FrXX​(s)​FrYY​(s).\rho\_{r}(s)={F\_{r}^{\rm XY}(s)\over\sqrt{F\_{r}^{\rm XX}(s)F\_{r}^{\rm YY}(s)}}. |  | (11) |

This quantity can be considered as the counterpart of the Pearson cross-correlation coefficient for non-stationary signals. Both coefficients assume values in the range [-1,1] with ρr​(s)=1\rho\_{r}(s)=1 for perfectly correlated time series, ρr​(s)=0\rho\_{r}(s)=0 for independent time series, and ρr​(s)=−1\rho\_{r}(s)=-1 for perfectly anticorrelated time series. It should be noted that, in order to calculate ρr​(s)\rho\_{r}(s), the time series do not have to be fractal Kwapień et al. ([2015](https://arxiv.org/html/2510.13785v1#bib.bib75)).

### 2.4 Decomposing sources of multifractality

Obtaining reliable numerical outcomes using the MFDFA algorithm described above is inherently challenging. The risk of overestimation and misinterpretation is high, particularly when working with relatively short time series. Standard techniques for generating free surrogate data — such as shuffling original series with only a few thousand data points — may misleadingly exhibit multifractal scaling. In such cases, the apparent multifractality arises not from genuine structural features, but from residual correlations Kwapień et al. ([2023](https://arxiv.org/html/2510.13785v1#bib.bib35)). This issue becomes especially prominent when the time series displays heavy-tailed fluctuation distributions as in the present case of digital market instruments. In these scenarios, only sufficiently long datasets can reveal the true absence of multifractality. In practice, short time series with heavy-tailed fluctuations often produce spurious indications of multifractal behavior Drożdż et al. ([2009](https://arxiv.org/html/2510.13785v1#bib.bib37)). A recent approach Kluszczyński et al. ([2025](https://arxiv.org/html/2510.13785v1#bib.bib36)) offers a more systematic validation of multifractality by attenuating heavy-tailed fluctuations while preserving correlation structures. This method involves a ranking-based probability density transformation that reprojects the data, retaining their temporal order while progressively reshaping the fluctuation distribution toward a Gaussian form Kluszczyński et al. ([2025](https://arxiv.org/html/2510.13785v1#bib.bib36)).

qq-Gaussian distributions provide a highly practical analytical framework for modeling this class of probability distributions. They serve as a natural extension of the standard Gaussian distribution, analogous to how the Tsallis entropy SqS\_{q} extends the classical Boltzmann—Gibbs entropy SS Umarov et al. ([2008](https://arxiv.org/html/2510.13785v1#bib.bib76)); Tsallis et al. ([1995](https://arxiv.org/html/2510.13785v1#bib.bib77)). The qq-Gaussian distribution 𝒢​q\mathcal{G}q is characterized by two parameters: a shape parameter q∈(−∞,3)q\in(-\infty,3) and a scale (width) parameter β>0\beta>0. Its probability density function (PDF) takes the form Umarov et al. ([2008](https://arxiv.org/html/2510.13785v1#bib.bib76)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | pq​(x)=βCq​eq​(−β​x2),p\_{q}(x)=\frac{\sqrt{\beta}}{C\_{q}}e\_{q}(-\beta x^{2}), |  | (12) |

where eq​(x)e\_{q}(x) denotes the qq-exponential function, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | eq​(x)={(1+(1−q)​x)1/(1−q)if ​q≠1​ and ​1+(1−q)​x>00if ​q≠1​ and ​1+(1−q)​x≤0exif ​q=1,e\_{q}(x)=\begin{cases}(1+(1-q)x)^{1/(1-q)}&\text{if }q\neq 1\text{ and }1+(1-q)x>0\\ 0&\text{if }q\neq 1\text{ and }1+(1-q)x\leq 0\\ e^{x}&\text{if }q=1,\end{cases} |  | (13) |

and Cq=∫−∞∞​eq​(x2),d​xC\_{q}=\int{-\infty}^{\infty}e\_{q}(x^{2}),dx is a normalization constant.

The persistence of well-defined multifractality characteristics in the limit q=1q=1, which corresponds to the Gaussian distribution, is a strong indicator that the observed multifractality stems from genuine correlations. It is expected and important to note that heavy-tailed distributions can enhance multifractality, but only when temporal correlations are present. In the absence of such correlations, the system typically exhibits monofractal behavior, or in more extreme cases, bifractality, particularly when the fluctuation dynamics fall within the Lévy-stable regime Kwapień et al. ([2023](https://arxiv.org/html/2510.13785v1#bib.bib35)).

## 3 Results

### 3.1 Multifractal characteristics of BTC and ETH in the years 2018-2024

The validity of the assumption about the preservation of temporal correlations when converting fluctuation distributions to distributions with varying tail thickness, as modeled here with the qq-Gaussians, is illustrated in Fig. [4](https://arxiv.org/html/2510.13785v1#S3.F4 "Figure 4 ‣ 3.1 Multifractal characteristics of BTC and ETH in the years 2018-2024 ‣ 3 Results") for the year 2024 as an example from Fig. [3](https://arxiv.org/html/2510.13785v1#S2.F3 "Figure 3 ‣ 2.1 Data and its characteristics ‣ 2 Materials and Methods"). Indeed, starting from empirical data (best fitted with q≈1.5q\approx 1.5) and then projecting then onto qq-Gaussians for qq staring from q=1.4q=1.4 towards a Gaussian (q=1)(q=1) and further down to q=0.2q=0.2, which corresponds to an almost uniform distribution, it is clearly seen that the form of A​(τ)A(\tau) remains practically unchanged. This even includes a sharp drop to zero around the 103−10410^{3}-10^{4} timescale, meaning that for larger time distances, fluctuations become uncorrelated. Interestingly, this process begins slightly earlier for higher capitalization BTC (slightly above 10310^{3}) than for ETH (closer to 10410^{4}). From a more general perspective these results provide a further strong argument for the validity of the methodology proposed by Kluszczyński et al. Kluszczyński et al. ([2025](https://arxiv.org/html/2510.13785v1#bib.bib36)) that temporal correlations measured by the Pearson coefficient and distributions of fluctuations can be disentangled.

![Refer to caption](Figs/ACF24.eps)


Figure 4: The Pearson autocorrelation function calculated from the return moduli for BTC and ETH in 2024 with their original PDFs replaced by the qq-Gaussian distributions with different values of qq.

At the same time, the corresponding univariate fluctuation functions calculated for −4≤r≤4-4\leq r\leq 4 for the same 2024 year and shown in Fig. [5](https://arxiv.org/html/2510.13785v1#S3.F5 "Figure 5 ‣ 3.1 Multifractal characteristics of BTC and ETH in the years 2018-2024 ‣ 3 Results") display scaling for both BTC and ETH. This scaling is rr-dependent, though not very strongly, for q=1q=1 and smaller, to become clearly multifractal already for q=1.2q=1.2, and even more so for q=1.4q=1.4, with the strongest qq-dependence for the empirical data considered. It should be noted, however, that in the case of BTC, the uniform scaling of Fr​(s)F\_{r}(s) breaks down slightly around 2×1032\times 10^{3}, while for ETH the uniform scaling persists over the entire interval ss shown. Such observations correspond well to the relative behavior of the autocorrelation function A​(τ)A(\tau) discussed above, where the one for ETH remains positive for a longer period.

![Refer to caption](Figs/BTC_ETH_Fq24o.eps)


Figure 5: Fluctuation functions Fr​(s)F\_{r}(s) for BTC and ETH in 2024 with their original PDFs replaced by the qq-Gaussian distributions with different values of qq. Start of the scaling range, in which a power-law form of Fr​(s)F\_{r}(s) is observed for a range of values of qq, is denoted by a vertical red dashed line.

The scaling characteristics are most clearly revealed in the singularity spectrum representation (also called multifractal spectrum) which, for the cases shown in Fig. [5](https://arxiv.org/html/2510.13785v1#S3.F5 "Figure 5 ‣ 3.1 Multifractal characteristics of BTC and ETH in the years 2018-2024 ‣ 3 Results") are presented in Fig. [6](https://arxiv.org/html/2510.13785v1#S3.F6 "Figure 6 ‣ 3.1 Multifractal characteristics of BTC and ETH in the years 2018-2024 ‣ 3 Results"). A distinct multifractal shape is visible already at the smallest analyzed values of qq, as reflected by the widths of the Δ​(α)\Delta(\alpha) spectra. They change very slowly as qq increases from 0.2 to 1.0, after which they begin to grow increasingly faster, reaching values exceeding 0.3 for the empirical series. This increase is clearly caused by the increasing thickness of the tails of the PDFs. However, it should be emphasized again that this result is possible because there are temporal correlations in the analyzed series, which are visible in the autocorrelation functions above. Destroying these correlations, for example, by reshuffling the time series reduces these spectra to points, which indicates monofractality. These effects can be seen here because the considered time series are sufficiently long to ensure convergence Drożdż et al. ([2009](https://arxiv.org/html/2510.13785v1#bib.bib37)); Zhou ([2012](https://arxiv.org/html/2510.13785v1#bib.bib38)); Kwapień et al. ([2023](https://arxiv.org/html/2510.13785v1#bib.bib35)). Thus, the thickness of the PDF tails has a large constructive importance for the width of multifractal spectra, but without time correlations, multifractality has no support to exist. Another related significant effect, which draws attention, is the asymmetry of the multifractal spectra as defined by Eq. ([10](https://arxiv.org/html/2510.13785v1#S2.E10 "In 2.2 Multifractal formalism ‣ 2 Materials and Methods")). The corresponding numbers are listed in Fig. [6](https://arxiv.org/html/2510.13785v1#S3.F6 "Figure 6 ‣ 3.1 Multifractal characteristics of BTC and ETH in the years 2018-2024 ‣ 3 Results"). The spectra for the original empirical data have the most pronounced left-side character, which is rather typical for financial series and reflects the fat-tailed shape of the corresponding PDFs. In both cases, the asymmetry parameter AαA\_{\alpha} is relatively large, but it is even significantly larger for ETH than for BTC (0.48 vs. 0.81). This corresponds to the thicker tails of the log-return distributions in the ETH case and is consistent with the higher frequency of extreme events in 2024 visible in Fig. [2](https://arxiv.org/html/2510.13785v1#S2.F2 "Figure 2 ‣ 2.1 Data and its characteristics ‣ 2 Materials and Methods"). (It is worthwhile to recall here the bifractal property of the Lévy flight process pdfs that results in a two-point f​(α)f(\alpha) spectrum Nakao ([2000](https://arxiv.org/html/2510.13785v1#bib.bib78)). This property is sometimes “sensed” by data with thinner pdf tails, which leads to smearing of the singularity spectrum left shoulder over a disproportionately large range of α\alpha’s Drożdż et al. ([2009](https://arxiv.org/html/2510.13785v1#bib.bib37)).) At the same time, it can be seen that, by replacing the original empirical PDFs with qq-Gaussians with decreasing qq, AαA\_{\alpha} quickly and systematically decreases and it reaches a clearly negative value for q=1q=1, indicating a right-sided asymmetry. Finally, for q=0.2q=0.2, AαA\_{\alpha} takes on a value of -1, indicating the presence of only the right wing in f​(α)f(\alpha). Such a systematic change in the shape of the multifractal spectrum from the left-sided to the right-sided form with decreasing qq can actually be expected, because small qq correspond to increasingly more homogeneous PDFs and, therefore, to a lower probability of small values of the Hölder exponents determining α\alpha.

![Refer to caption](Figs/spektra24a.eps)


Figure 6: Multifractal spectra for BTC and ETH in 2024 with their original PDFs replaced by the qq-Gaussian distributions with different values of qq.

As it can be seen in Fig. [2](https://arxiv.org/html/2510.13785v1#S2.F2 "Figure 2 ‣ 2.1 Data and its characteristics ‣ 2 Materials and Methods"), the BTC and ETH PDFs calculated separately for the years 2018-2024 are dispersed quite clearly in relation to the inverse cubic power-law (black dashed line). The corresponding univariate fluctuation functions calculated for −4⩽r⩽4-4\leqslant r\leqslant 4 for the same sequence of years are shown in Fig. [7](https://arxiv.org/html/2510.13785v1#S3.F7 "Figure 7 ‣ 3.1 Multifractal characteristics of BTC and ETH in the years 2018-2024 ‣ 3 Results"). They display scaling for both assets, but with a slightly varying intensity of dependence on rr across different years. Of course, this also results in varying widths Δ​α\Delta\alpha of the multifractal spectra and their asymmetry coefficients, all displayed in Fig. [8](https://arxiv.org/html/2510.13785v1#S3.F8 "Figure 8 ‣ 3.1 Multifractal characteristics of BTC and ETH in the years 2018-2024 ‣ 3 Results"). f​(α)f(\alpha) corresponding to the Gaussianized PDFs (q=1q=1), but with preserved temporal correlations, are also shown in the corresponding right panels. They are significantly narrower, indicating a significant role of the PDFs. However, it should be emphasized again that destroying temporal correlations by shuffling the time series reduces Δ​α\Delta\alpha to practically zero also for the original data — the ones with the broad distributions.

![Refer to caption](Figs/Fq_BTC_ETHu.eps)


Figure 7: Univariate fluctuation functions Fr​(s)F\_{r}(s) for BTC and ETH across different years. Start of the scaling range, in which a power-law form of Fr​(s)F\_{r}(s) is observed for a range of values of qq, is denoted by a vertical red dashed line.

![Refer to caption](Figs/spektraall4u.eps)


Figure 8: Multifractal spectra for BTC and ETH across different years.

### 3.2 Cross-correlations between BTC and ETH

The general MFCCA formalism outlined in Sect. [2.2](https://arxiv.org/html/2510.13785v1#S2.SS2 "2.2 Multifractal formalism ‣ 2 Materials and Methods"), via Eq. ([3](https://arxiv.org/html/2510.13785v1#S2.E3 "In 2.2 Multifractal formalism ‣ 2 Materials and Methods")) also allows us to quantitatively address the question of possible multifractal cross-correlations between two multifractal series, the ones representing the BTC and ETH returns in the present case. The corresponding cross-correlation functions are shown in Fig. [9](https://arxiv.org/html/2510.13785v1#S3.F9 "Figure 9 ‣ 3.2 Cross-correlations between BTC and ETH ‣ 3 Results"). They are displayed for those values of rr for which scaling of these functions is identifiable. As it can be seen, a relatively good scaling occurs for positive values of rr, which amplify contribution from periods of large fluctuations. On the negative side of rr, scaling typically terminates slightly below r≈−1.5r\approx-1.5 for the data considered here. This means that, for the component corresponding to periods of small-amplitude noise, there are no fractal cross-correlations. An analogous result after Gaussianizing the same time series according to the procedure described in Sect. [2.4](https://arxiv.org/html/2510.13785v1#S2.SS4 "2.4 Decomposing sources of multifractality ‣ 2 Materials and Methods") gives the result shown in Fig. [10](https://arxiv.org/html/2510.13785v1#S3.F10 "Figure 10 ‣ 3.2 Cross-correlations between BTC and ETH ‣ 3 Results"). The scaling is preserved over similar ranges of rr, but it becomes definitely of the monofractal type, i.e. with a weak dependence on rr.

![Refer to caption](Figs/BTCzETHcc_org.eps)


Figure 9: Bivariate fluctuation functions FXY​(r,s)F\_{\rm XY}(r,s) for BTC and ETH across different years. The minimum values of rr vary among the years and are explicitly listed, while the maximum values are fixed at r=4r=4. Start of the scaling range, in which a power-law form of FXY​(r,s)F\_{\rm XY}(r,s) is observed for a range of values of qq, is denoted by a vertical red dashed line (if applicable).

![Refer to caption](Figs/BTCzETHcc_G.eps)


Figure 10: Bivariate fluctuation functions FXY​(r,s)F\_{\rm XY}(r,s) for BTC and ETH across different years after Gaussianizing the corresponding PDFs. Start of the scaling range, in which a power-law form of FXY​(r,s)F\_{\rm XY}(r,s) is observed for a range of values of qq, is denoted by a vertical red dashed line (if applicable).

A fully quantitative estimation of the character of cross-correlations between time series is obtained in terms of the relation between λ​(r)\lambda(r) and hx​y​(r)=(hx​(r)+hy​(r))/2h\_{x}y(r)=(h\_{x}(r)+h\_{y}(r))/2 introduced in Sect. [2.2](https://arxiv.org/html/2510.13785v1#S2.SS2 "2.2 Multifractal formalism ‣ 2 Materials and Methods"). The existence and similarity of these two quantities reflects the degree and quality of multifractal cross-correlations Oświęcimka et al. ([2014](https://arxiv.org/html/2510.13785v1#bib.bib66)). For the BTC and ETH time series considered above, these two quantities are compared in Fig. [11](https://arxiv.org/html/2510.13785v1#S3.F11 "Figure 11 ‣ 3.2 Cross-correlations between BTC and ETH ‣ 3 Results") but only for r⩾0r\geqslant 0, because for r<0r<0 the scaling is less pronounced or even disappears (see Fig [9](https://arxiv.org/html/2510.13785v1#S3.F9 "Figure 9 ‣ 3.2 Cross-correlations between BTC and ETH ‣ 3 Results")). From this perspective, a majority of the years 2018-2024 show convincing multifractal cross-correlations as both λ​(r)\lambda(r) and hx​y​(r)h\_{x}y(r) are rr-dependent and similar to each other. We remember, however, that this effect is visible for r⩾0r\geqslant 0 corresponding to the periods of large fluctuations. The similarity between these two quantities is the weakest in the pandemic year 2020 due to larger estimation errors. This means that the time series, although each multifractal, were less cross-correlated. For completeness, Fig. [9](https://arxiv.org/html/2510.13785v1#S3.F9 "Figure 9 ‣ 3.2 Cross-correlations between BTC and ETH ‣ 3 Results") also shows the same quantities for the time series after Gaussianization of their PDFs (q=1q=1). The rr-dependence becomes much weaker here, although, admittedly, scaling still holds and both λ​(r)\lambda(r) and hx​y​(r)h\_{x}y(r) can be determined. The lack of a clear dependence on rr, however, indicates that the cross-correlation is monofractal here. It should be noted at the same time that the destruction of the autocorrelations by independent reshuffling of the BTC and ETH returns leads to a complete disappearance of any scaling associated with the cross-correlation.

![Refer to caption](Figs/lambda_hsred_rdodatnie.eps)


Figure 11: The bivariate scaling exponent λ​(r)\lambda(r) and the average generalized univariate Hurst exponent hx​y​(r)h\_{xy}(r) estimated from the fluctuations functions presented in Fig. [9](https://arxiv.org/html/2510.13785v1#S3.F9 "Figure 9 ‣ 3.2 Cross-correlations between BTC and ETH ‣ 3 Results") (left panels) and Fig. [10](https://arxiv.org/html/2510.13785v1#S3.F10 "Figure 10 ‣ 3.2 Cross-correlations between BTC and ETH ‣ 3 Results") (right panels).

### 3.3 Detrended cross-correlation

A related but to some extent complementary description of the cross-correlation between the detrended time series can be obtained by using the coefficient ρr​(s)\rho\_{r}(s) defined in Sect. [2.3](https://arxiv.org/html/2510.13785v1#S2.SS3 "2.3 Detrended cross-correlation coefficient ‣ 2 Materials and Methods") by Eq. ([11](https://arxiv.org/html/2510.13785v1#S2.E11 "In 2.3 Detrended cross-correlation coefficient ‣ 2 Materials and Methods")), which allows for resolving cross-correlations on a particular scale ss with respect to the size of the fluctuation amplitude. For the time series of BTC and ETH considered here, the values of ρr​(s)\rho\_{r}(s) and their dependence on the scale ss for r=2r=2 and r=4r=4 are displayed in Fig. [12](https://arxiv.org/html/2510.13785v1#S3.F12 "Figure 12 ‣ 3.3 Detrended cross-correlation ‣ 3 Results"). The former case, r=2r=2, corresponds to the periods of typical medium-size fluctuations (which dominate the PDF) while the latter, r=4r=4, retains the periods of more extreme fluctuations and, effectively, filters out both the periods of small fluctuations and the periods of average fluctuations. These coefficients are calculated for the original data (left side of Fig. [12](https://arxiv.org/html/2510.13785v1#S3.F12 "Figure 12 ‣ 3.3 Detrended cross-correlation ‣ 3 Results")) as well as for their Gaussianized substitutes (right side). For the original data, the detrended cross-correlations are clear and quite similar in magnitude across the years considered. On average, they are slightly stronger for r=2r=2 than for r=4r=4, but in the latter case the dependence on year is much stronger. In particular, in 2020, the year of the Covid-19 pandemic, such cross-correlations at larger scales ss are even stronger for r=4r=4 than for r=2r=2, which seems understandable in light of the fact that price changes were more sudden then. Gaussianization significantly weakens this particular case, which confirms the role of large fluctuations in generating cross-correlations in 2020. In the other cases, Gaussianization generally weakens cross-correlations, although to a lesser extent.

![Refer to caption](Figs/pq_BTCzETHq2q4.eps)


Figure 12: Detrended cross-correlation coefficient for BTC and ETH across different years: the original time series (left panels) and after their Gaussianization (right panels).

### 3.4 ETH from decentralized exchange

In contrast to traditional centralized exchanges (CEXs), such as Binance or Coinbase, where a single intermediary manages liquidity, order matching, and user access, decentralized exchanges (DEXs) like Uniswap rely on community-driven infrastructure and smart contracts to facilitate trading without intermediaries. While CEXs offer higher liquidity, ease of use, and established security procedures, DEXs provide greater anonymity and access to a wider set of tokens but often face challenges of lower liquidity, higher technical complexity, and exposure to contract-related risks. An analysis of Ethereum trading from June 2023 to June 2024 Wątorek et al. ([2024](https://arxiv.org/html/2510.13785v1#bib.bib79)) revealed that, despite these limitations, Uniswap already exhibited convincing signs of multifractality in its price and volume dynamics. However, unlike Binance, where multifractal patterns were more balanced and mature, the multifractal spectra on Uniswap were strongly left-skewed, indicating that multifractality originated primarily from periods of large fluctuations, with periods of small and average fluctuations behaving more like uncorrelated noise. Interestingly, the multifractality was more pronounced in transaction volumes than in returns, and cross-correlations between volatility and volume, though present, remained weaker than those observed on centralized platforms, underscoring the comparatively less mature yet evolving state of decentralized markets Wątorek et al. ([2024](https://arxiv.org/html/2510.13785v1#bib.bib79)).

![Refer to caption](Figs/Uniswap/rozkladyR1minallETH.eps)![Refer to caption](Figs/Uniswap/ACF_R_1minETH.eps)![Refer to caption](Figs/Uniswap/Fq_R_ETH_1min.eps)![Refer to caption](Figs/Uniswap/spektraETH_1min.eps)

Figure 13: Selected characteristics of ETH returns from Binance and Uniswap v3 with 0.05 provision covering the period from Jul 2024 to March 2025: a) - cumulative distribution function, b) - Pearson autocorrelation function, c) - fluctuation functions, d) - multifractal spectra. Start of the scaling range, in which a power-law form of Fr​(s)F\_{r}(s) is observed for a range of values of qq, is denoted by a vertical red dashed line in c).

As an extension of those studies, here we present a summary of the multifractal characteristics of the return time series for ETH on both markets (CEX from Binance and DEX from Uniswap v3 with 0.05 provision) in parallel. For this purpose, one-minute ETH returns covering the period from July 2024 to March 2025 are analyzed within the present extended methodology. The results are summarized in Fig. [13](https://arxiv.org/html/2510.13785v1#S3.F13 "Figure 13 ‣ 3.4 ETH from decentralized exchange ‣ 3 Results") for the fluctuation PDFs (upper left), the autocorrelation function (upper right), the univariate fluctuation function (lower left) and the resulting multifractal spectra (lower right). It is worth noting that the ETH return PDFs have clearly thicker tails here than before, which refers even to those from the CEX market. A possible reason is that the DEX market, perhaps because it is less mature, fluctuates more rapidly, resulting in thicker tails. The CEX market, on the other hand, cannot be much different in this regard, as it would generate immediate arbitrage opportunities, meaning risk-free profits. Therefore, it is quite natural in this context to assume that the price dynamics on the CEX market is somewhat catching up and becoming more similar to that on the DEX market. Such a scenario would confirm the fact that the autocorrelation functions A​(τ)A(\tau) appear almost identical in both markets. As a result, Fr​(s)F\_{r}(s) for ETH from both markets show quite good and similar scaling, although the range of visible slopes (on a log-log scale — the lower left panel) for r⩾0r\geqslant 0 is slightly larger on the DEX market than on the CEX market. This is reflected in the shapes of the multifractal spectra. Both are left-sided asymmetric, but the degree of asymmetry is clearly greater for the DEX market than for the CEX one. This fact is consistent with the presence of several larger events in the PDF corresponding to DEX with respect to CEX (see the upper left panel in Fig. [13](https://arxiv.org/html/2510.13785v1#S3.F13 "Figure 13 ‣ 3.4 ETH from decentralized exchange ‣ 3 Results")). Finally, Gaussianization of these time series leads to an almost identical result with a spectrum that is still clearly multifractal but right-sided due to the suppression of the periods with large events.

Due to the fact that both the CEX and DEX time series show multifractal scaling, a natural further step is to consider their detrended cross-correlations as quantified by the bivariate fluctuation functions FXY​(r,s)F\_{\rm XY}(r,s) and the coefficient ρr​(s)\rho\_{r}(s). First, let us look at the former quantities, which are shown in the upper left panels of Fig. [14](https://arxiv.org/html/2510.13785v1#S3.F14 "Figure 14 ‣ 3.4 ETH from decentralized exchange ‣ 3 Results"). Unlike the data from the centralized market of Binance discussed in Sect. [3.2](https://arxiv.org/html/2510.13785v1#S3.SS2 "3.2 Cross-correlations between BTC and ETH ‣ 3 Results"), the fluctuation functions representing the original time series reveal scaling over the full range of the considered values of rr, which is quite a remarkable result given the nature of each market is different. This may suggest that the cross-market arbitrage may play a crucial role in this case leading to a strong coupling between ETH returns on both markets. This is especially evident for r⩾0r\geqslant 0 in the upper right panels of Fig. [14](https://arxiv.org/html/2510.13785v1#S3.F14 "Figure 14 ‣ 3.4 ETH from decentralized exchange ‣ 3 Results"), which show the relation between λ​(r)\lambda(r) and hXY​(r)h\_{\rm XY}(r): both quantities converge to each other in this range of scales. What is even more convincing, ρr​(s)\rho\_{r}(s) assumes values that are close to 1 already for a half-a-day-long time scale for r=2r=2 (i.e., the periods of average fluctuations dominate) — it is a much stronger coupling than it was reported in Sect. [3.2](https://arxiv.org/html/2510.13785v1#S3.SS2 "3.2 Cross-correlations between BTC and ETH ‣ 3 Results") for the Binance data (see Fig. [11](https://arxiv.org/html/2510.13785v1#S3.F11 "Figure 11 ‣ 3.2 Cross-correlations between BTC and ETH ‣ 3 Results")). For the periods of large fluctuations r=4r=4 this picture remains qualitatively analogous with the exception that the coupling becomes stronger for higher scales than for r=2r=2. If the time series have been Gaussianized, the multifractal nature of data is still observed, although the variability of λ​(r)\lambda(r) and hXY​(r)h\_{\rm XY}(r) decrease, which indicates narrowing of the f​(α)f(\alpha) spectra in terms of Δ​α\Delta\alpha. Also in this case there is no statistically significant difference between both these measures for positive values of rr. However, for the Gaussianized time series, we observe evident weakening of the detrended cross-correlations, which assume values similar to those observed for the centralized market.

![Refer to caption](Figs/Uniswap/Fqxy1min.eps)![Refer to caption](Figs/Uniswap/lambda_hsred_1min.eps)![Refer to caption](Figs/Uniswap/pq1min.eps)

Figure 14: Multiscale measures for time series of ETH returns collected from Binance and Uniswap v3 with 0.05 provision over the period Jul 2024 — March 2025: the bivariate fluctuation function FXY​(r,s)F\_{\rm XY}(r,s) (top left), the generalized bivariate Hurst exponent λ​(r)\lambda(r) and the average generalized univariate Hurst exponent hXY​(r)h\_{\rm XY}(r) (top right), as well as the detrended cross-correlation coefficient ρr​(s)\rho\_{r}(s) (bottom). The results for the original time series and their Gaussianized counterparts are presented in each case.

### 3.5 NFT tokens

Another blockchain technology product of interest in light of the research conducted here is the non-fungible token (NFT) market. This market is a relatively new branch of blockchain-based finance that emerged in 2017, gaining mainstream attention with projects like CryptoKitties and marketplaces such as OpenSea. Unlike cryptocurrencies, which are interchangeable, each NFT is unique, representing ownership of digital or physical assets such as art, collectibles, and in-game items. The market experienced explosive growth during the COVID-19 pandemic, peaking in late 2021 with record-high trading volumes, before cooling down in subsequent years. Despite the NFT-market young age and volatility, research shows that NFT trading already displays statistical patterns similar to traditional financial markets, though with distinct features tied to low liquidity, token rarity, and speculative behavior Szydło et al. ([2024](https://arxiv.org/html/2510.13785v1#bib.bib55)); Wątorek et al. ([2024](https://arxiv.org/html/2510.13785v1#bib.bib56)).

Trading on the NFT market differs from traditional financial markets in several important ways. Each token is unique, and its price often depends on rarity and individual traits rather than uniform value, making collections highly heterogeneous. Transactions are relatively infrequent, with long waiting times between trades, and activity tends to surge shortly after a collection’s launch before stabilizing. Instead of relying on last transaction prices, the NFT market often uses the floor price — the lowest ask price within a collection — as a key valuation metric, which makes it resemble an auction market. Recent study Szydło et al. ([2024](https://arxiv.org/html/2510.13785v1#bib.bib55)); Wątorek et al. ([2024](https://arxiv.org/html/2510.13785v1#bib.bib56)) shows that NFT floor prices, although less variable as compared to traditional asset prices, already carry complex internal dynamics similar to the other financial markets, with both non-linear correlations and heterogeneous behavior across scales.

As the last example, the Famous Fox Federation (FF) collection is subjected to a similar analysis as the ones above. This collection consists of 7,777 tokens on the Solana blockchain, each represented by digital images of stylized cartoon foxes with varying characteristics. The collection was developed by a group of Solana network users to build an ecosystem of blockchain-related tools and is associated with the FOXY token. In the statistical analysis Szydło et al. ([2024](https://arxiv.org/html/2510.13785v1#bib.bib55)); Wątorek et al. ([2024](https://arxiv.org/html/2510.13785v1#bib.bib56)), the FF collection displayed heavy-tailed distributions in capitalization increments and transaction volumes, with some evidence of power-law scaling. Its trading activity also showed persistent correlations in capitalization and transaction volume, while floor price returns tended to be slightly antipersistent, reflecting the broader inefficiencies of the NFT market. In the current contribution, the FF price changes from the 2-year period between October 2021 and September 2023 were used and the results in a form analogous to the previous subsections are shown in Fig. [15](https://arxiv.org/html/2510.13785v1#S3.F15 "Figure 15 ‣ 3.5 NFT tokens ‣ 3 Results"). The insets on its right side show the PDFs and the autocorrelation function A​(τ)A(\tau) for the original data and for their Gaussianized variants, respectively. The fluctuation functions (left panels) show multifractal scaling which translates into a wide (Δ​α=0.65)(\Delta\alpha=0.65) multifractal spectrum (right panel, main) and substantially less asymmetric than for the time series analyzed in previous sections. It is interesting to note that the maximum of f​(α)f(\alpha) occurs slightly below α=0.5\alpha=0.5, which is an alternative manifestation of anti-persistence in NFT (here FF) returns. Gaussianization significantly reduces the f​(α)f(\alpha) width (Δ​α=0.16)(\Delta\alpha=0.16) but leaves it clearly in the multifractal region.

![Refer to caption](Figs/NFT/FqFF.eps)![Refer to caption](Figs/NFT/NFT_FF.eps)

Figure 15: The Famous Fox NFT collection floor price returns vs. their PDF-Gaussianized substitutes. Main panels: the univariate fluctuation functions F​(r,s)F(r,s) (left) and the multifractal spectra f​(α)f(\alpha) (right) calculated for the Famous Fox NFT collection floor price returns covering the period October 2021 – September 2023. Insets: the PDFs (left) and the Pearson autocorrelation function (right) for the same data.

## 4 Discussion and conclusions

Our study examined the multifractal properties of digital asset markets, focusing on Bitcoin, Ethereum, decentralized exchanges, and NFT tokens, by using the multifractal detrended cross-correlation analysis (MFCCA), the multifractal detrended fluctuation analysis (MFDFA) as its special case, and the related techniques. The results show convincingly that temporal correlations — particularly the long-range memory — constitute the fundamental source of multifractality in cryptocurrency price dynamics. While heavy-tailed return distributions play a complementary role by broadening the multifractal spectrum, they cannot by themselves generate multifractal behavior in the absence of correlations. Eliminating temporal correlations by shuffling the original time series leads to the disappearance of multifractality regardless of the thickness of the tails, while the singularity spectra are simply reduced to points, which confirms previously known results Drożdż et al. ([2009](https://arxiv.org/html/2510.13785v1#bib.bib37)); Zhou ([2012](https://arxiv.org/html/2510.13785v1#bib.bib38)); Kwapień et al. ([2023](https://arxiv.org/html/2510.13785v1#bib.bib35)). Importantly, the temporal length of the digital market time series studied here is long enough to allow convergence to such a result. This finding strengthens the argument that genuine multifractality in financial time series reflects the persistent structural organization rather than statistical artifacts.

Across the seven-year period analyzed in this work (2018–2024), both BTC and ETH exhibited strong multifractal scaling, with notable variation during episodes of heightened uncertainty such as the COVID-19 pandemic. Their cross-correlations also displayed multifractal features, particularly for periods of large fluctuations, underlining the interconnectedness of the major cryptoassets. The comparative study of centralized (Binance) and decentralized (Uniswap) exchanges revealed that while both markets show multifractality, decentralized markets exhibit stronger left-skewed spectra driven by periods of large fluctuations, consistent with their relative immaturity and lower liquidity. Extending the analysis to the NFT sector represented here by the Famous Fox collection highlighted that even young, heterogeneous markets can already show developed multifractal scaling, even more symmetric as compared to cryptocurrencies. This may indicate that the uncorrelated noise component in NFTs is smaller than in cryptocurrencies.

Taken together, these results reinforce the importance of applying multifractal frameworks to digital markets. They offer practical insights for volatility forecasting, systemic risk monitoring, and understanding the maturation of blockchain-based financial ecosystems. For example, the strong correlations between BTC and ETH on various time scales can be used in optimal portfolio construction Zhao et al. ([2018](https://arxiv.org/html/2510.13785v1#bib.bib80)). The decay of the autocorrelation function, which indicates the average size of the volatility cluster Drożdż et al. ([2009](https://arxiv.org/html/2510.13785v1#bib.bib37)), may also be used in risk management. The consistency of the log-return tail distributions with the inverse cubic power-law allows for the selection of appropriate distributions in various risk mitigation methods, such as Value-at-Risk. Moreover, the greater hierarchical dependence of correlations at the level of larger fluctuations compared to smaller ones, documented by left-sided asymmetry of the multifractal spectra, may potentially allow for extending risk management strategies to include fluctuation-specific correlation patterns. The direct link between multifractality and risk management is an interesting subject for further studies.

On a more general level, the disentangling methodology used here — separating distributional effects from temporal correlations — provides a robust foundation for future research, enabling a clearer distinction between genuine complexity and spurious effects. As digital finance continues to expand, multifractal analysis can serve as a valuable tool for interpreting its evolving dynamics, informing both academic inquiry and market practice.

\authorcontributions

Conceptualization, S.D., R.K, J.K. and M.W.; methodology, S.D., R.K., J.K. and M.W.; software, R.K. and M.W.; validation, S.D., J.K. and M.W.; formal analysis, R.K. and M.W.; investigation, S.D., J.K. and M.W.; resources, M.W.; data curation, M.W.; writing—original draft preparation, S.D. ; writing—review and editing, J.K. and M.W.; visualization, M.W.; supervision, S.D. All authors have read and agreed to the published version of the manuscript.

\funding

This research received no external funding.

\dataavailability

Data available freely from Binance [Binance](https://arxiv.org/html/2510.13785v1#bib.bib57) .

\conflictsofinterest

The authors declare no conflicts of interest.

\reftitle

References

## References

* Nakamoto (2008)

  Nakamoto, S.
  Bitcoin: A Peer-to-Peer Electronic Cash System.
  <http://bitcoin.org/bitcoin.pdf>.
* Wątorek et al. (2021)

  Wątorek, M.; Drożdż, S.; Kwapień, J.; Minati, L.; Oświęcimka, P.; Stanuszek, M.
  Multiscale characteristics of the emerging global cryptocurrency market.
  Physics Reports 2021, 901, 1–82.
* Corbet et al. (2022)

  Corbet, S.; Hou, Y.G.; Hu, Y.; Larkin, C.; Lucey, B.; Oxley, L.
  Cryptocurrency liquidity and volatility interrelationships during the COVID-19 pandemic.
  Finance Research Letters 2022, 45, 102137.
* Evrim Mandaci and Cagli (2022)

  Evrim Mandaci, P.; Cagli, E.C.
  Herding intensity and volatility in cryptocurrency markets during the COVID-19.
  Finance Research Letters 2022, 46, 102382.
* Nguyen et al. (2023)

  Nguyen, A.P.N.; Mai, T.T.; Bezbradica, M.; Crane, M.
  Volatility and returns connectedness in cryptocurrency markets: Insights from graph-based methods.
  Physica A 2023, 632, 129349.
* Drożdż et al. (2018)

  Drożdż, S.; Gębarowski, R.; Minati, L.; Oświęcimka, P.; Wątorek, M.
  Bitcoin market route to maturity? Evidence from return fluctuations, temporal correlations and multiscaling effects.
  Chaos 2018, 28, 071101.
* Stosic et al. (2018)

  Stosic, D.; Stosic, D.; Ludermir, T.B.; Stosic, T.
  Collective behavior of cryptocurrency price changes.
  Physica A 2018, 507, 499–509.
* James et al. (2021)

  James, N.; Menzies, M.; Chan, J.
  Changes to the extreme and erratic behaviour of cryptocurrencies during COVID-19.
  Physica A 2021, 565, 125581.
* Drożdż et al. (2023)

  Drożdż, S.; Kwapień, J.; Wątorek, M.
  What is mature and what is still emerging in the cryptocurrency market?
  Entropy 2023, 25.
* Takaishi (2018)

  Takaishi, T.
  Statistical properties and multifractality of Bitcoin.
  Physica A 2018, 506, 507–519.
* Takaishi and Adachi (2020)

  Takaishi, T.; Adachi, T.
  Market efficiency, liquidity, and multifractality of Bitcoin: A dynamic study.
  Asia-Pacific Financial Markets 2020, 27, 145–154.
* James (2021)

  James, N.
  Dynamics, behaviours, and anomaly persistence in cryptocurrencies and equities surrounding COVID-19.
  Physica A 2021, 570, 125831.
* James and Menzies (2022)

  James, N.; Menzies, M.
  Collective correlations, dynamics, and behavioural inconsistencies of the cryptocurrency market over time.
  Nonlinear Dynamics 2022, 107, 4001–4017.
* Wątorek et al. (2022)

  Wątorek, M.; Kwapień, J.; Drożdż, S.
  Multifractal cross-correlations of bitcoin and ether trading characteristics in the post-COVID-19 time.
  Future Internet 2022, 14.
* Brouty and Garcin (2024)

  Brouty, X.; Garcin, M.
  Fractal properties, information theory, and market efficiency.
  Chaos, Solitons & Fractals 2024, 180, 114543.
* Bui et al. (2025)

  Bui, H.Q.; Schinckus, C.; Al-Jaifi, H.
  Long-range correlations in cryptocurrency markets: A multi-scale DFA approach.
  Physica A 2025, 661, 130417.
* Kwapień and Drożdż (2012)

  Kwapień, J.; Drożdż, S.
  Physical approach to complex systems.
  Physics Reports 2012, 515, 115–226.
* Manavi et al. (2020)

  Manavi, S.A.; Jafari, G.; Rouhani, S.; Ausloos, M.
  Demythifying the belief in cryptocurrencies decentralized aspects. A study of cryptocurrencies time cross-correlations with common currencies, commodities and financial indices.
  Physica A: Statistical Mechanics and its Applications 2020, 556, 124759.
* Spurr and Ausloos (2021)

  Spurr, A.; Ausloos, M.
  Challenging practical features of Bitcoin by the main altcoins.
  Quality & Quantity 2021, 55, 1541–1559.
* James and Menzies (2022)

  James, N.; Menzies, M.
  Collective correlations, dynamics, and behavioural inconsistencies of the cryptocurrency market over time.
  Nonlinear Dynamics 2022, 107, 4001–4017.
* Jiang et al. (2019)

  Jiang, Z.Q.; Xie, W.J.; Zhou, W.X.; Sornette, D.
  Multifractal analysis of financial markets: a review.
  Reports on Progress in Physics 2019, 82, 125901.
* Halsey et al. (1986)

  Halsey, T.C.; Jensen, M.H.; Kadanoff, L.P.; Procaccia, I.; Shraimant, B.I.
  Fractal measures and their singularities: The characterization of strange sets.
  Physical Review A 1986, 33, 1141–1151.
* Farmer et al. (2004)

  Farmer, J.D.; Gillemot, L.; Lillo, F.; Mike, S.; Sen, A.
  What really causes large price changes?
  Quantitative finance 2004, 4, 383–397.
* Mandelbrot (1963)

  Mandelbrot, B.
  The variation of certain speculative prices.
  The Journal of Business 1963, 36, 394–419.
* Ausloos and Ivanova (2002)

  Ausloos, M.; Ivanova, K.
  Multifractal nature of stock exchange prices.
  Computer Physics Communications 2002, 147, 582–585.
* Kutner and Świtała (2004)

  Kutner, R.; Świtała, F.
  Remarks on the possible universal mechanism of the non-linear long-term autocorrelations in financial time-series.
  Physica A 2004, 344, 244–251.
  Applications of Physics in Financial Analysis 4 (APFA4).
* Cont (2007)

  Cont, R., Volatility Clustering in Financial Markets: Empirical Facts and Agent-Based Models.
  In Long Memory in Economics; Teyssière, G.; Kirman, A.P., Eds.; Springer Berlin Heidelberg: Berlin, Heidelberg, 2007; pp. 289–309.
* Oh et al. (2008)

  Oh, G.; Kim, S.; Eom, C.
  Long-term memory and volatility clustering in high-frequency price changes.
  Physica A 2008, 387, 1247–1254.
* Zhou (2009)

  Zhou, W.X.
  The components of empirical multifractality in financial returns.
  EPL 2009, 88, 28004.
* Barunik et al. (2012)

  Barunik, J.; Aste, T.; Di Matteo, T.; Liu, R.
  Understanding the source of multifractality in financial markets.
  Physica A 2012, 391, 4234–4251.
* Green et al. (2014)

  Green, D.; Hanan, W.R.; Heffernan, S.
  The origins of multifractality in financial time series and the effect of extreme events.
  The European Physical Journal B 2014, 87, 171.
* Morales et al. (2014)

  Morales, R.; Di Matteo, T.; Aste, T.
  Dependency structure and scaling properties of financial markets.
  The European Physical Journal B 2014, 87, 168.
* Klamut et al. (2020)

  Klamut, J.; Kutner, R.; Gubiec, T.; Struzik, Z.R.
  Multibranch multifractality and the phase transitions in time series of mean interevent times.
  Physical Review E 2020, 101, 063303.
* Kutner et al. (2019)

  Kutner, R.; Ausloos, M.; Grech, D.; Matteo, T.D.; Schinckus, C.; Stanley, H.E.
  Econophysics and sociophysics: Their milestones & challenges.
  Physica A 2019, 516, 240–253.
* Kwapień et al. (2023)

  Kwapień, J.; Blasiak, P.; Drożdż, S.; Oświęcimka, P.
  Genuine multifractality in time series is due to temporal correlations.
  Physical Review E 2023, 107, 034139.
* Kluszczyński et al. (2025)

  Kluszczyński, R.; Drożdż, S.; Kwapień, J.; Stanisz, T.; Wątorek, M.
  Disentangling sources of multifractality in time series.
  Mathematics 2025, 13, 205.
* Drożdż et al. (2009)

  Drożdż, S.; Kwapień, J.; Oświęcimka, P.; Rak, R.
  Quantitative features of multifractal subtleties in time series.
  EPL 2009, 88, 60003.
* Zhou (2012)

  Zhou, W.X.
  Finite-size effect and the components of multifractality in financial volatility.
  Chaos, Solitons & Fractals 2012, 45, 147–155.
* Wątorek et al. (2021)

  Wątorek, M.; Kwapień, J.; Drożdż, S.
  Financial return distributions: Past, present, and COVID-19.
  Entropy 2021, 23.
* Kantelhardt et al. (2002)

  Kantelhardt, J.W.; Zschiegner, S.A.; Koscielny-Bunde, E.; Havlin, S.; Bunde, A.; Stanley, H.E.
  Multifractal detrended fluctuation analysis of nonstationary time series.
  Physica A 2002, 316, 87–114.
* Makarov and Schoar (2020)

  Makarov, I.; Schoar, A.
  Trading and arbitrage in cryptocurrency markets.
  Journal of Financial Economics 2020, 135, 293–319.
* Cohen and Qadan (2022)

  Cohen, G.; Qadan, M.
  The complexity of cryptocurrencies algorithmic trading.
  Mathematics 2022, 10, 2037.
* Fang et al. (2022)

  Fang, F.; Ventre, C.; Basios, M.; Kanthan, L.; Martinez-Rego, D.; Wu, F.; Li, L.
  Cryptocurrency trading: a comprehensive survey.
  Financial Innovation 2022, 8, 13.
* Cohen (2023)

  Cohen, G.
  Intraday algorithmic trading strategies for cryptocurrencies.
  Review of Quantitative Finance and Accounting 2023, 61, 395–409.
* Wątorek et al. (2023)

  Wątorek, M.; Skupień, M.; Kwapień, J.; Drożdż, S.
  Decomposing cryptocurrency high-frequency price dynamics into recurring and noisy components.
  Chaos 2023, 33, 083146.
* Gerlach et al. (2019)

  Gerlach, J.C.; Demos, G.; Sornette, D.
  Dissection of Bitcoin’s multiscale bubble history from January 2012 to February 2018.
  Royal Society open science 2019, 6, 180643.
* Huber and Sornette (2022)

  Huber, T.A.; Sornette, D.
  Boom, bust, and bitcoin: bitcoin-bubbles as innovation accelerators.
  Journal of Economic Issues 2022, 56, 113–136.
* Bouri et al. (2022)

  Bouri, E.; Gupta, R.; Vo, X.V.
  Jumps in Geopolitical Risk and the Cryptocurrency Market: The Singularity of Bitcoin.
  Defence and Peace Economics 2022, 33, 150–161.
* Hong and Yoon (2022)

  Hong, M.Y.; Yoon, J.W.
  The impact of COVID-19 on cryptocurrency markets: A network analysis based on mutual information.
  PLoS ONE 2022, 17.
* Khalfaoui et al. (2023)

  Khalfaoui, R.; Gozgor, G.; Goodell, J.W.
  Impact of Russia-Ukraine war attention on cryptocurrency: Evidence from quantile dependence analysis.
  Finance Research Letters 2023, 52, 103365.
* Wątorek et al. (2023)

  Wątorek, M.; Kwapień, J.; Drożdż, S.
  Cryptocurrencies are becoming part of the world global financial market.
  Entropy 2023, 25, 377.
* Fang et al. (2024)

  Fang, Y.; Tang, Q.; Wang, Y.
  Geopolitical Risk and Cryptocurrency Market Volatility.
  Emerging Markets Finance and Trade 2024, 60, 3254–3270.
* Poongodi et al. (2021)

  Poongodi, M.; Nguyen, T.N.; Hamdi, M.; Cengiz, K.
  Global cryptocurrency trend prediction using social media.
  Information Processing and Management 2021, 58, 102708.
* Aharon et al. (2022)

  Aharon, D.Y.; Demir, E.; Lau, C.K.M.; Zaremba, A.
  Twitter-Based uncertainty and cryptocurrency returns.
  Research in International Business and Finance 2022, 59, 101546.
* Szydło et al. (2024)

  Szydło, P.; Wątorek, M.; Kwapień, J.; Drożdż, S.
  Characteristics of price related fluctuations in non-fungible token (NFT) market.
  Chaos 2024, 34, 013108.
* Wątorek et al. (2024)

  Wątorek, M.; Szydło, P.; Kwapień, J.; Drożdż, S.
  Correlations versus noise in the NFT market.
  Chaos 2024, 34, 073112.
* (57)

  Binance.
  <https://www.binance.com/>.
* (58)

  CoinMarketCap.
  <https://coinmarketcap.com>.
* Nguyen et al. (2022)

  Nguyen, A.P.N.; Mai, T.T.; Bezbradica, M.; Crane, M.
  The Cryptocurrency Market in Transition before and after COVID-19: An Opportunity for Investors?
  Entropy 2022, 24.
* Ammy-Driss and Garcin (2023)

  Ammy-Driss, A.; Garcin, M.
  Efficiency of the financial markets during the COVID-19 crisis: Time-varying parameters of fractional stable dynamics.
  Physica A 2023, 609, 128335.
* Kwapień et al. (2022)

  Kwapień, J.; Wątorek, M.; Bezbradica, M.; Crane, M.; Tan Mai, T.; Drożdż, S.
  Analysis of inter-transaction time fluctuations in the cryptocurrency market.
  Chaos 2022, 32, 083142.
* Drożdż et al. (2002)

  Drożdż, S.; Kwapień, J.; Gümmer, F.; Ruf, F.; Speth, J.
  Are the contemporary financial fluctuations sooner converging to normal?
  Acta Physica Polonica B 2002, 34, 4293–4306.
* Drożdż et al. (2007)

  Drożdż, S.; Forczek, M.; Kwapień, J.; Oświęcimka, P.; Rak, R.
  Stock market return distributions: From past to present.
  Physica A 2007, 383, 59–64.
* Clark (1973)

  Clark, P.K.
  A subordinated stochastic process model with finite variance for speculative prices.
  Econometrica: journal of the Econometric Society 1973, pp. 135–155.
* Oświęcimka et al. (2006)

  Oświęcimka, P.; Kwapień, J.; Drożdż, S.
  Wavelet versus detrended fluctuation analysis of multifractal structures.
  Physical Review E 2006, 74, 016103.
* Oświęcimka et al. (2014)

  Oświęcimka, P.; Drożdż, S.; Forczek, M.; Jadach, S.; Kwapień, J.
  Detrended cross-correlation analysis consistently extended to multifractality.
  Physical Review E 2014, 89, 023305.
* Podobnik and Stanley (2008)

  Podobnik, B.; Stanley, H.E.
  Detrended cross-correlation analysis: A new method for analyzing two nonstationary time series.
  Physical Review Letters 2008, 100, 1–4.
* Zhou (2008)

  Zhou, W.X.
  Multifractal detrended cross-correlation analysis for two nonstationary signals.
  Physical Review E 2008, 77, 066211.
* Horvatic et al. (2011)

  Horvatic, D.; Stanley, H.E.; Podobnik, B.
  Detrended cross-correlation analysis for non-stationary time series with periodic trends.
  Europhysics Letters 2011, 94, 18007.
* Oświęcimka et al. (2013)

  Oświęcimka, P.; Drożdż, S.; Kwapień, J.; Górski, A.
  Effect of detrending on multifractal characteristics.
  Acta Physica Polonica A 2013, 123, 597–603.
* Ohashi et al. (2003)

  Ohashi, K.; Amaral, L.A.; Natelson, B.H.; Yamamoto, Y.
  Asymmetrical singularities in real-world signals.
  Physical Review E 2003, 68.
* Cao et al. (2013)

  Cao, G.; Cao, J.; Xu, L.
  Asymmetric multifractal scaling behavior in the Chinese stock market: Based on asymmetric MF-DFA.
  Physica A 2013, 392, 797–807.
* Drożdż and Oświęcimka (2015)

  Drożdż, S.; Oświęcimka, P.
  Detecting and interpreting distortions in hierarchical organization of complex time series.
  Physical Review E 2015, 91, 030902(R).
* Gómez-Gómez et al. (2021)

  Gómez-Gómez, J.; Carmona-Cabezas, R.; Ariza-Villaverde, A.B.; Gutiérrez de Ravé, E.; Jiménez-Hornero, F.J.
  Multifractal detrended fluctuation analysis of temperature in Spain (1960–2019).
  Physica A 2021, 578, 126118.
* Kwapień et al. (2015)

  Kwapień, J.; Oświęcimka, P.; Drożdż, S.
  Detrended fluctuation analysis made flexible to detect range of cross-correlated fluctuations.
  Physical Review E 2015, 92, 052815.
* Umarov et al. (2008)

  Umarov, S.; Tsallis, C.; Steinberg, S.
  On a q-Central Limit Theorem Consistent with Nonextensive Statistical Mechanics.
  Milan Journal of Mathematics 2008, 76, 307–328.
* Tsallis et al. (1995)

  Tsallis, C.; Levy, S.V.F.; Souza, A.M.C.; Maynard, R.
  Statistical-Mechanical Foundation of the Ubiquity of Lévy Distributions in Nature.
  Physical Review Letters 1995, 75, 3589–3593.
* Nakao (2000)

  Nakao, H.
  Multi-scaling properties of truncated Levy flights.
  Physics Letters A 2000, 266, 282–289.
* Wątorek et al. (2024)

  Wątorek, M.; Królczyk, M.; Kwapień, J.; Stanisz, T.; Drożdż, S.
  Approaching multifractal complexity in decentralized cryptocurrency trading.
  Fractal and Fractional 2024, 8, 652.
* Zhao et al. (2018)

  Zhao, L.; Li, W.; Fenu, A.; Podobnik, B.; Wang, Y.; Stanley, H.E.
  The q-dependent detrended cross-correlation analysis of stock market.
  Journal of Statistical Mechanics: Theory and Experiment 2018, 2018, 023402.