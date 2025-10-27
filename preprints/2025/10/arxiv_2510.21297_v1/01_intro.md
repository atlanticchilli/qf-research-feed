---
authors:
- Francis Liu
- Natalie Packham
- Artur Sepp
doc_id: arxiv:2510.21297v1
family_id: arxiv:2510.21297
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Jump risk premia in the presence of clustered jumps
url_abs: http://arxiv.org/abs/2510.21297v1
url_html: https://arxiv.org/html/2510.21297v1
venue: arXiv q-fin
version: 1
year: 2025
---


Francis Liu
Natalie Packham
Artur Sepp
Department of Business and Economics, Berlin School of Economics and Law, Badensche Str. 52, 10825 Berlin, Germany.
Blockchain Research Center, Humboldt-Universität zu Berlin, Germany.
International Research Training Group 1792, Humboldt-Universität zu Berlin, Germany.
E-mail: francisliutfp@gmail.com.
Department of Business and Economics, Berlin School of Economics and Law, Badensche Str. 52, 10825 Berlin, Germany.
International Research Training Group 1792, Humboldt-Universität zu Berlin, Germany.
E-mail: packham@hwr-berlin.de.LGT Bank (Schweiz) AG
E-mail: artursepp@gmail.com.

###### Abstract

This paper presents an option pricing model that incorporates clustered jumps using a bivariate Hawkes process. The process captures both self- and cross-excitation of positive and negative jumps, enabling the model to generate return dynamics with asymmetric, time-varying skewness and to produce positive or negative implied volatility skews. This feature is especially relevant for assets such as cryptocurrencies, so-called “meme” stocks, G-7 currencies, and certain commodities, where implied volatility skews may change sign depending on prevailing sentiment.
We introduce two additional parameters, namely the positive and negative jump premia, to model the market risk preferences for positive and negative jumps, inferred from options data. This enables the model to flexibly match observed skew dynamics. Using Bitcoin (BTC) options, we empirically demonstrate how inferred jump risk premia exhibit predictive power for both the cost of carry in BTC futures and the performance of delta-hedged option strategies.

JEL classification: D81, G13

Keywords: Volatility risk premium, clustered jumps, Hawkes process, cryptocurrencies

## 1 Introduction

Jumps are acknowledged as an important risk factor in asset pricing, derivatives pricing, and risk management. Although there is a large body of literature investigating jumps in financial markets for traditional assets, the emergence of option markets for cryptocurrencies and retail-driven trading activity in options on “meme” stocks provide a new environment for this field of study. In this paper, we focus on the dynamics and options market for cryptocurrencies and, specifically, for Bitcoin (BTC).

Empirically, ℙ\mathbb{P}-dynamics of BTC exhibit both large positive and negative jumps, while option prices under ℚ\mathbb{Q}-dynamics exhibit changes in implied volatility skew from negative (when demand for protective put options increases) to positive (when demand for upside leverage rises).

Figure [1](https://arxiv.org/html/2510.21297v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Jump risk premia in the presence of clustered jumps") illustrates the dynamics of Bitcoin (BTC) daily returns, at-the-money (ATM) implied volatilities and call and put skews from April 2019 to May 2024. First, we observe extreme returns ranging from −30%-30\% to 20%20\%, with significant clustering. The implied at-the-money volatility for options with maturity of one month and Black-Scholes delta of 0.50.5 ranges from 40%40\% to 140%140\%. The call skew is computed as the difference between implied volatility of a call option with 0.250.25 Black-Scholes delta and implied volatility of a call with 0.50.5 delta. The put skew is computed as the difference between implied volatility of a put option with −0.25-0.25 Black-Scholes delta and the implied volatility of a put with −0.5-0.5 delta. Positive call and put skews indicate the higher demand for calls and puts, respectively. We observe that on average both call and put skews are positive. In addition, call skews exceed put skews in most periods, indicating a higher demand for calls than for puts. This behaviour contradicts traditional patterns in options on stocks and stock indices where the call skew is negative, while the put skew is consistently positive.

Figure 1: Subplot (A) shows Bitcoin daily returns from April 2019 to May 2024 with extreme volatility and pronounced clustering during market stress periods. Subplot shows ATM Volatility daily with average of 68.3%68.3\%. Subplot (C) shows BTC 25-Delta Call/Put Skews with corresponding averages of 3.0%3.0\% and 1.7%1.7\% and with blue/pink regions corresponding to periods with relatively higher call/put skews respectively.

![Refer to caption](x1.png)

To account for empirical features of crypto options markets, we develop a derivatives pricing model that incorporates two Hawkes processes, one for positive and one for negative jumps.
These processes capture the clustering of jumps, driven by self- and cross-excitation, effectively capturing the structure of jump arrival times.
The model can be calibrated to the joint dynamics of BTC prices and of BTC implied volatility surfaces.
In particular, we explore the resulting positive and negative jump risk premia, defined as the difference in expected jump magnitudes between the statistical measure and the risk-neutral measures.

Importantly, our model accommodates changing market preferences for skewness risk, when investors shift their demands between put options to hedge the downside risk and call options to capture positive upside. The preference for call options with upside potential is consistent with evidence from the equity market literature indicating some investors’ preferences for assets offering lottery-like payoffs, see, e.g. Bali
et al. ([2011](https://arxiv.org/html/2510.21297v1#bib.bib7)), Thaler and
Ziemba ([1988](https://arxiv.org/html/2510.21297v1#bib.bib46)), Kumar ([2009](https://arxiv.org/html/2510.21297v1#bib.bib34)). In cryptocurrency option markets, such preferences for capturing the upside manifest in inflated prices of out-of-the-money call options during bullish periods, which produces positive risk premia of positive jumps.

Furthermore, the positive implied volatility skew is also present in the market data of so-called “meme” stocks.
Options activity in these stocks is characterised by strong demand and high volumes for call options and by a positive spot-volatility correlation.
Gupta and
Pascale ([2025](https://arxiv.org/html/2510.21297v1#bib.bib24)) introduce the “Equity Euphoria Indicator”, which measures the percentage of stocks with a positive implied skew ranging from 0%0\% to 100%100\%.
The most recent values, 10% as of January 2025 and 11.9% as of September 2025, are close to the levels observed during the Dot.com bubble in late 1990 and the post-Covid rally in 2021.
We notice that implied skews on “meme” stocks change sign to negative during severe bear market periods, so that structurally we cannot model the dynamics of these stocks using a stochastic volatility model with a constant correlation parameter.
Adding jumps arriving at a constant intensity rate, as for the Bates model (Bates ([1996](https://arxiv.org/html/2510.21297v1#bib.bib8))), would not improve the structural consistency of the model dynamics, unless we specify stochastic intensity rates for positive and negative jumps.
Thus, our model represents a simple construction to model the dynamics of stocks with varying signs of implied skew.
It is straightforward to incorporate stochastic volatility in our framework; however, we skip this feature to reduce the number of model parameters.

Our work contributes to the existing literature in several areas.
First, the model of the price process allows one to identify and understand the factors that drive variations in jump risk premia, in particular, how jump intensities adapt in response to the occurrence of jumps.
Extending the work of Hainaut ([2016](https://arxiv.org/html/2510.21297v1#bib.bib25), [2017](https://arxiv.org/html/2510.21297v1#bib.bib26)) on univariate Hawkes process, we assume that the dynamics of these jump intensities are governed by a bivariate Hawkes process.
Jump intensities increase with jump arrivals and decrease with time.
As such, the model accounts for changes in asset prices and option prices stemming not only from movements in the underlying price, but also from variations in jump intensities.

Second, alongside specifying the pricing model, we derive the measure change between the statistical and risk-neutral measures. This allows us to derive the jump risk premia associated with positive and negative jumps as the difference between expected jump magnitudes under the risk-neutral and statistical measures. A jump risk premium therefore quantifies the difference between market expectations (from options prices) and market realisations (from the price history) and can be interpreted as a measure of market sentiment. As option prices (under the risk-neutral measure) reflect expectations about future jumps and their intensities, in our setting, investors pay a risk premium for call options due to positive jumps if they are optimistic (positive skewness of option prices). Likewise, investors pay a risk premium for put options due to negative jumps if they are pessimistic (negative skewness of option prices).

We further develop an estimation and calibration procedure that takes into account both historical BTC price dynamics and options data. In the time period considered (May 2019 to October 2023), both positive and negative risk premia are observed, with frequent periods where the implied jump risk is higher than the realised jump risk. The last observation is consistent with the findings on the variance risk premia, e.g. (Carr and Wu, [2009](https://arxiv.org/html/2510.21297v1#bib.bib15); Granelli and
Veraart, [2016](https://arxiv.org/html/2510.21297v1#bib.bib23)).

Third, the cryptocurrency market is known to have at times a large basis or cost-of-carry in its futures prices, as well as large swings in the basis.
For example, the annualised basis of one-month BTC futures on Deribit on 5 April 2021 was 35%35\%, and – after a sell-off on 19 May 2021 – dropped to −54%-54\%.
Both positive and negative carry are regularly observed in the market.
These can only partially be explained by the funding costs associated with perpetual futures.
Therefore, we investigate the relationship between the inferred jump risk premia and the carry of one-month BTC futures to determine whether risk preferences, beyond standard funding costs from perpetual contracts, significantly influence futures pricing dynamics.

Finally, the presence of jumps imposes challenges in risk management and hedging, both in terms of the magnitude of losses and in the unpredictability of jumps. Hedging strategies in crypto markets have been investigated by (e.g. Liu
et al., [2023](https://arxiv.org/html/2510.21297v1#bib.bib38); Matic
et al., [2023](https://arxiv.org/html/2510.21297v1#bib.bib40); Lucic and
Sepp, [2024](https://arxiv.org/html/2510.21297v1#bib.bib39)). Here, we investigate whether the risk premia, which capture market participants’ forward-looking risk preferences, can be systematically earned through delta-hedged options trading strategies.

The Hawkes process, or self-exciting process, was introduced by (Hawkes, [1971](https://arxiv.org/html/2510.21297v1#bib.bib29); Hawkes and
Oakes, [1974](https://arxiv.org/html/2510.21297v1#bib.bib31)), see also
(Errais
et al., [2010](https://arxiv.org/html/2510.21297v1#bib.bib21); Hawkes, [2018](https://arxiv.org/html/2510.21297v1#bib.bib30); Bacry
et al., [2015](https://arxiv.org/html/2510.21297v1#bib.bib4); Embrechts
et al., [2011](https://arxiv.org/html/2510.21297v1#bib.bib19); Hainaut and
Moraux, [2018](https://arxiv.org/html/2510.21297v1#bib.bib28); Hainaut, [2016](https://arxiv.org/html/2510.21297v1#bib.bib25)) for reviews and applications of Hawkes processes in finance.
There is a vast literature on jump risk and jump risk premia, (e.g. Bates, [1996](https://arxiv.org/html/2510.21297v1#bib.bib8), [2000](https://arxiv.org/html/2510.21297v1#bib.bib9); Pan, [2002](https://arxiv.org/html/2510.21297v1#bib.bib42); Bakshi and
Kapadia, [2003](https://arxiv.org/html/2510.21297v1#bib.bib5); Eraker, [2004](https://arxiv.org/html/2510.21297v1#bib.bib20); Broadie
et al., [2007](https://arxiv.org/html/2510.21297v1#bib.bib12); Santa-Clara and
Yan, [2010](https://arxiv.org/html/2510.21297v1#bib.bib43); Christoffersen et al., [2012](https://arxiv.org/html/2510.21297v1#bib.bib16); Nguyen
et al., [2019](https://arxiv.org/html/2510.21297v1#bib.bib41)).
Skewness and their relation to risk premia are treated in (e.g. Bakshi
et al., [2003](https://arxiv.org/html/2510.21297v1#bib.bib6)) with a focus on the options market, and from a behavioural perspective in (Bali
et al., [2011](https://arxiv.org/html/2510.21297v1#bib.bib7), e.g.).
The literature on risk premia in cryptocurrency markets is growing (e.g. Alexander and
Imeraj, [2021](https://arxiv.org/html/2510.21297v1#bib.bib1), [2023](https://arxiv.org/html/2510.21297v1#bib.bib2); Almeida
et al., [2024](https://arxiv.org/html/2510.21297v1#bib.bib3); Dobrynskaya, [2024](https://arxiv.org/html/2510.21297v1#bib.bib18)).

The paper is organised as follows.
In Section [2](https://arxiv.org/html/2510.21297v1#S2 "2 Model specification ‣ Jump risk premia in the presence of clustered jumps"), we develop the model and derive a number of results, such as moment-generating functions and the equivalent measure change.
Section [3](https://arxiv.org/html/2510.21297v1#S3 "3 Two stage approach calibration of the model ‣ Jump risk premia in the presence of clustered jumps") introduces the estimation method that accompanies the model.
In Section [4](https://arxiv.org/html/2510.21297v1#S4 "4 Positive and negative jump risk premia ‣ Jump risk premia in the presence of clustered jumps"), we specify the jump risk premia.
Section [5](https://arxiv.org/html/2510.21297v1#S5 "5 Empirical Results ‣ Jump risk premia in the presence of clustered jumps") presents the empirical results, that is, exploring the historical jump risk premia, the relationship between the jump risk premia and the futures basis, as well as the ability of the jump risk premia to forecast one-day ahead option portfolio returns that can be used to improve hedging strategies.
All calculations in this work can be reproduced with codes available in Quantlet [![[Uncaptioned image]](qletlogo_tr.png)](https://github.com/QuantLet/HJP/tree/main/codes/).

## 2 Model specification

### 2.1 Price dynamics under ℙ\mathbb{P}-measure

Our model extends the univariate Hawks process dynamics considered by Hainaut and
Moraux ([2018](https://arxiv.org/html/2510.21297v1#bib.bib28)) (also see Hainaut ([2016](https://arxiv.org/html/2510.21297v1#bib.bib25)), Hainaut ([2017](https://arxiv.org/html/2510.21297v1#bib.bib26)), and chapter 4 of Hainaut ([2022](https://arxiv.org/html/2510.21297v1#bib.bib27)) for variants of the univariate model adapted in different situations). To account for the empirical evidence of clustered positive and negative jumps, we incorporate two jump components with self-excitement and cross-excitement.

Let (Ω,ℱ,ℙ)\left(\Omega,\ \mathcal{F},\ \mathbb{P}\right) be a probability space with information filtration (ℱt)\left(\mathcal{F}\_{t}\right). The adapted price process StS\_{t} is modeled as the sum of a continuous part driven by a Brownian motion and two jump components for positive and negative jumps, respectively. The intensities of the jump components are latent processes λt+\lambda^{+}\_{t} and λt−\lambda^{-}\_{t}.
The arrival times of positive and negative jumps are modeled by two counting processes, abbreviated by Nt(1)N^{(1)}\_{t} and Nt(2)N^{(2)}\_{t}, respectively.

We introduce the following price dynamics under the statistical ℙ\mathbb{P} measure:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​StSt−\displaystyle\frac{{\rm d}S\_{t}}{S\_{t-}} | =μ​d​t+σ​d​Wt\displaystyle=\mu\,{\rm d}t+\sigma\,{\rm d}W\_{t} |  | (1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +((𝐞J+−1)​d​Nt(1)−λt+​𝔼​(𝐞J+−1)​d​t)+((𝐞J−−1)​d​Nt(2)−λt−​𝔼​(𝐞J−−1)​d​t),\displaystyle\phantom{=\,}+\Big(({\bf e}^{J^{+}}-1)\,{\rm d}N\_{t}^{(1)}-\lambda\_{t}^{+}{\mathbb{E}}({\bf e}^{J^{+}}-1)\,{\rm d}t\Big)+\Big(({\bf e}^{J^{-}}-1)\,{\rm d}N\_{t}^{(2)}-\lambda\_{t}^{-}{\mathbb{E}}({\bf e}^{J^{-}}-1)\,{\rm d}t\Big), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (d​λt+d​λt−)\displaystyle\begin{pmatrix}{\rm d}\lambda\_{t}^{+}\\ {\rm d}\lambda\_{t}^{-}\end{pmatrix} | =(κ+​(θ+−λt+)κ−​(θ−−λt−))​d​t+(β11β12β21β22)​(J+​d​Nt(1)J−​d​Nt(2)),\displaystyle=\begin{pmatrix}\kappa^{+}(\theta^{+}-\lambda\_{t}^{+})\\ \kappa^{-}(\theta^{-}-\lambda\_{t}^{-})\end{pmatrix}\,{\rm d}t+\begin{pmatrix}\beta\_{11}&\beta\_{12}\\ \beta\_{21}&\beta\_{22}\end{pmatrix}\begin{pmatrix}J^{+}\,{\rm d}N\_{t}^{(1)}\\ J^{-}\,{\rm d}N\_{t}^{(2)}\end{pmatrix}, |  | (2) |

where μ\mu is a constant drift parameter, σ\sigma is a constant volatility parameter, WtW\_{t} is a standard Brownian motion, Nt(1)N^{(1)}\_{t} and Nt(2)N^{(2)}\_{t} are Poisson processes for the arrival of positive and negative jumps, respectively. Jump sizes J+J^{+} and J−J^{-} of positive and negative jumps with probability density functions (PDFs) ϖ+\varpi^{+} and ϖ−\varpi^{-}, respectively, given by shifted exponential distributions ϖ+\varpi^{+} and ϖ−\varpi^{-}. The jump parts in dynamics ([1](https://arxiv.org/html/2510.21297v1#S2.E1 "In 2.1 Price dynamics under ℙ-measure ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) are adjusted by deterministic jump compensators, so the expected drift is determined by μ\mu. The coefficients βi​j\beta\_{ij}, i,j=1,2i,j=1,2, determine the level of excitement induced by jumps on the intensities.
Their signs are set by β11,β21≥0\beta\_{11},\beta\_{21}\geq 0 and β12,β22≤0\beta\_{12},\beta\_{22}\leq 0, so that all jump realisations lead to jumps in intensity rates. We impose the following constraints on the jump parameters:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ+≥β11​𝔼​J++β12​𝔼​J−,κ−≥β21​𝔼​J++β22​𝔼​J−.\displaystyle\kappa^{+}\geq\beta\_{11}{\mathbb{E}}J^{+}+\beta\_{12}{\mathbb{E}}J^{-},\quad\kappa^{-}\geq\beta\_{21}{\mathbb{E}}J^{+}+\beta\_{22}{\mathbb{E}}J^{-}. |  | (3) |

These restrictions guarantee that the expected asymptotic values of the intensities are finite,
i.e., limt→∞𝔼​λt+<∞\lim\_{t\rightarrow\infty}{\mathbb{E}}\lambda^{+}\_{t}<\infty and limt→∞𝔼​λt−<∞\lim\_{t\rightarrow\infty}{\mathbb{E}}\lambda^{-}\_{t}<\infty.
For further details, we refer to Appendix [A.1](https://arxiv.org/html/2510.21297v1#A1.SS1 "A.1 Conditions for finite expected intensities ‣ Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps").

The solution to dynamics in ([1](https://arxiv.org/html/2510.21297v1#S2.E1 "In 2.1 Price dynamics under ℙ-measure ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) is given by:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | St\displaystyle S\_{t} | =S0​exp⁡((μ−σ22)​t+σ​Wt)\displaystyle=S\_{0}\,\exp\left(\left(\mu-\frac{\sigma^{2}}{2}\right)t+\sigma W\_{t}\right) |  | (4) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅exp⁡((∑j=1Nt(1)Jj−−𝔼​(𝐞J+−1)​∫0tλs+​ds)+(∑j=1Nt(2)Jj−−𝔼​(𝐞J−−1)​∫0tλs−​ds)),\displaystyle\phantom{=\,}\cdot\exp\left(\Big(\sum\_{j=1}^{N\_{t}^{(1)}}J\_{j}^{-}-{\mathbb{E}}({\bf e}^{J^{+}}-1)\int\_{0}^{t}\lambda\_{s}^{+}\,{\rm d}s\Big)+\Big(\sum\_{j=1}^{N\_{t}^{(2)}}J\_{j}^{-}-{\mathbb{E}}({\bf e}^{J^{-}}-1)\int\_{0}^{t}\lambda\_{s}^{-}\,{\rm d}s\Big)\right), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λt+\displaystyle\lambda\_{t}^{+} | =θ++𝐞−κ+​t​(λ0+−θ+)+β11​∫0t𝐞−κ+​(t−s)​Js+​dNs(1)+β12​∫0t𝐞−κ+​(t−s)​Js−​dNs(2),\displaystyle=\theta^{+}+{\bf e}^{-\kappa^{+}t}(\lambda^{+}\_{0}-\theta^{+})+\beta\_{11}\int\_{0}^{t}{\bf e}^{-\kappa^{+}(t-s)}\,J^{+}\_{s}\,{\rm d}N\_{s}^{(1)}+\beta\_{12}\int\_{0}^{t}{\bf e}^{-\kappa^{+}(t-s)}\,J^{-}\_{s}\,{\rm d}N\_{s}^{(2)}, |  | (5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λt−\displaystyle\lambda\_{t}^{-} | =θ−+𝐞−κ−​t​(λ0−−θ−)+β21​∫0t𝐞−κ−​(t−s)​Js+​dNs(1)+β22​∫0t𝐞−κ−​(t−s)​Js−​dNs(2).\displaystyle=\theta^{-}+{\bf e}^{-\kappa^{-}t}(\lambda^{-}\_{0}-\theta^{-})+\beta\_{21}\int\_{0}^{t}{\bf e}^{-\kappa^{-}(t-s)}\,J^{+}\_{s}\,{\rm d}N\_{s}^{(1)}+\beta\_{22}\int\_{0}^{t}{\bf e}^{-\kappa^{-}(t-s)}\,J^{-}\_{s}\,{\rm d}N\_{s}^{(2)}. |  | (6) |

We also specify the dynamics of the log return Xt:=ln⁡(St/S0)X\_{t}:=\ln\left(S\_{t}/S\_{0}\right) which is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=(μ−σ22)​d​t+σ​d​Wt+(J+​d​Nt(1)−λt+​𝔼​(𝐞J+−1)​d​t)+(J−​d​Nt(2)−λt−​𝔼​(𝐞J−−1)​d​t).\begin{split}{\rm d}X\_{t}&=\left(\mu-\frac{\sigma^{2}}{2}\right){\rm d}t+\sigma\,{\rm d}W\_{t}\\ &+\Big(J^{+}\,{\rm d}N\_{t}^{(1)}-\lambda\_{t}^{+}{\mathbb{E}}({\bf e}^{J^{+}}-1)\,{\rm d}t\Big)+\Big(J^{-}\,{\rm d}N\_{t}^{(2)}-\lambda\_{t}^{-}{\mathbb{E}}({\bf e}^{J^{-}}-1)\,{\rm d}t\Big).\end{split} |  | (7) |

In summary, the model incorporates three state variables (Xt,λt+,λt−)(X\_{t},\lambda^{+}\_{t},\lambda^{-}\_{t}). The model parameters include a drift μ\mu and the volatility σ\sigma of the continuous component;
eight parameters for the intensities of positive and negative jumps (κ+,θ+,β11,β12)(\kappa^{+},\ \theta^{+},\ \beta\_{11},\ \beta\_{12}) and (κ−,θ−,β21,β22)(\kappa^{-},\ \theta^{-},\ \beta\_{21},\ \beta\_{22}), respectively;
four parameters parameters for PDFs for jumps in returns: ϖ+​(j+)\varpi^{+}(j^{+}) and ϖ−​(j−)\varpi^{-}(j^{-}), as defined next.

We assume that the sizes of positive and negative jumps are driven by shifted exponential distributions with the following PDFs:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ϖ+​(j)=1η+​exp⁡(−1η+​(j−ν+))​𝟙{j>ν+},ϖ−​(j)=1η−​exp⁡(1η−​(j−ν−))​𝟙{j<ν−},\displaystyle\begin{split}&\varpi^{+}(j)=\frac{1}{\eta^{+}}\exp\left(-\frac{1}{\eta^{+}}(j-\nu^{+})\right)\mathbbm{1}\_{\{j>\nu^{+}\}},\\ &\varpi^{-}(j)=\frac{1}{\eta^{-}}\exp\left(\phantom{-}\frac{1}{\eta^{-}}(j-\nu^{-})\right)\mathbbm{1}\_{\{j<\nu^{-}\}},\end{split} | |  | (8) |

with 0<η+0<\eta^{+} and 0<η−0<\eta^{-} controlling the sizes of negative and positive jumps, respectively, and with ν+>0\nu^{+}>0 and ν−<0\nu^{-}<0 being thresholds.
The Laplace transforms of the jump size distributions (extended to ℝ−{\mathbb{R}}\_{-} for negative jumps) are given by

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ℒ(+)​(ω)\displaystyle\mathcal{L}^{(+)}(\omega) | =∫ν+∞𝐞−ω​j​ϖ+​(j)​dj=𝐞−ν+​ω1+η+​ω,\displaystyle=\int\_{\nu^{+}}^{\infty}{\bf e}^{-\omega j}\varpi^{+}(j)\,{\rm d}j=\frac{{\bf e}^{-\nu^{+}\omega}}{1+\eta^{+}\omega}, | if Re​(1/η++ω)>0\displaystyle\quad\text{ if }\text{Re}(1/\eta^{+}+\omega)>0 |  | (9) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ℒ(−)​(ω)\displaystyle\mathcal{L}^{(-)}(\omega) | =∫−∞ν−𝐞−ω​j​ϖ−​(j)​dj=𝐞−ν−​ω1−η−​ω,\displaystyle=\int\_{-\infty}^{\nu^{-}}{\bf e}^{-\omega j}\varpi^{-}(j)\,{\rm d}j=\frac{{\bf e}^{-\nu^{-}\omega}}{1-\eta^{-}\omega}, | if Re​(ω)<Re​(1/η).\displaystyle\quad\text{ if }\text{Re}(\omega)<\text{Re}(1/\eta). |  | (10) |

where ω∈ℂ\omega\in\mathbb{C} and Re​(ω)\text{Re}(\omega) denotes the real part.

Jump compensators are calculated using Equations ([9](https://arxiv.org/html/2510.21297v1#S2.E9 "In 2.1 Price dynamics under ℙ-measure ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) and ([10](https://arxiv.org/html/2510.21297v1#S2.E10 "In 2.1 Price dynamics under ℙ-measure ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(𝐞J+−1)\displaystyle{\mathbb{E}}\left({\bf e}^{J^{+}}-1\right) | =∫ν+∞(𝐞j−1)​ϖ+​(j)​dj=𝐞ν+1−η+−1,\displaystyle=\int\_{\nu^{+}}^{\infty}\left({\bf e}^{j}-1\right)\varpi^{+}(j){\rm d}j=\frac{{\bf e}^{\nu^{+}}}{1-\eta^{+}}-1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(𝐞J−−1)\displaystyle{\mathbb{E}}\left({\bf e}^{J^{-}}-1\right) | =∫−∞ν−(𝐞j−1)​ϖ−​(j)​dj=𝐞ν−1+η−−1.\displaystyle=\int^{\nu^{-}}\_{-\infty}\left({\bf e}^{j}-1\right)\varpi^{-}(j){\rm d}j=\frac{{\bf e}^{\nu^{-}}}{1+\eta^{-}}-1. |  |

We specify threshold parameters ν+\nu^{+} and ν−\nu^{-} for flexibility in defining the minimum size of jumps for empirical inference. The thresholds ν^+\hat{\nu}^{+} and ν^−\hat{\nu}^{-} can be estimated using a peak-over-threshold (POT) approach discussed in Section [3.1](https://arxiv.org/html/2510.21297v1#S3.SS1 "3.1 Time series estimation ‣ 3 Two stage approach calibration of the model ‣ Jump risk premia in the presence of clustered jumps").

### 2.2 Moment-generating function of joint dynamics

The moment generating function (MGF) of the log-return variable Xt=ln⁡(St/S0)X\_{t}=\ln(S\_{t}/S\_{0}) and jump intensities will be used for the equivalent measure change in Section [2.3](https://arxiv.org/html/2510.21297v1#S2.SS3 "2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps") and for the option pricing procedure in Section [3.2](https://arxiv.org/html/2510.21297v1#S3.SS2 "3.2 Calibration to market implied volatilities ‣ 3 Two stage approach calibration of the model ‣ Jump risk premia in the presence of clustered jumps"). The following Proposition extends Proposition 2.2. of Hainaut and
Moraux ([2018](https://arxiv.org/html/2510.21297v1#bib.bib28)) to the bivariave Hawks process.

###### Proposition 1.

The MGF of joint variables (XT,λT+,λT−)(X\_{T},\lambda^{+}\_{T},\lambda^{-}\_{T}), T≥tT\geq t, generalised to complex arguments, is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gℙ​(ω,ω+,ω−;T,x,λ+,λ−)≡𝔼ℙ​(exp⁡(ω​XT+ω+​λT++ω−​λT−)|Xt,λt+,λt−)=exp⁡(A​(t,T)+ω​Xt+C​(t,T)​λt++D​(t,T)​λt−),\begin{split}G^{\mathbb{P}}(\omega,\omega^{+},\omega^{-};T,x,\lambda^{+},\lambda^{-})&\equiv{\mathbb{E}}^{\mathbb{P}}\left(\exp(\omega X\_{T}+\omega^{+}\lambda^{+}\_{T}+\omega^{-}\lambda^{-}\_{T})\big|X\_{t},\lambda^{+}\_{t},\lambda^{-}\_{t}\right)\\ &=\exp\left(A(t,T)+\omega X\_{t}+C(t,T)\lambda\_{t}^{+}+D(t,T)\lambda\_{t}^{-}\right),\end{split} |  | (11) |

for ω,ω+,ω−∈ℂ\omega,\omega^{+},\omega^{-}\in\mathbb{C}, where the functions A,C,and ​DA,C,\text{and }D solve the following non-linear system of ordinary differential equations (ODEs):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂t​A​(t,T)=−μ​ω−σ22​(ω2−ω)−κ+​θ+​C​(t,T)−κ−​θ−​D​(t,T),∂∂t​C​(t,T)=−ℒ(+)​(−ω−C​(t,T)​β11−D​(t,T)​β21)+κ+​C​(t,T)+ω​(eν+1−η+−1)+1,∂∂t​D​(t,T)=−ℒ(−)​(−ω−C​(t,T)​β12−D​(t,T)​β22)+κ−​D​(t,T)+ω​(eν−1+η−−1)+1,\begin{split}\frac{\partial}{\partial t}A(t,T)&=-\mu\omega-\frac{\sigma^{2}}{2}\left(\omega^{2}-\omega\right)-\kappa^{+}\theta^{+}C(t,T)-\kappa^{-}\theta^{-}D(t,T),\\ \frac{\partial}{\partial t}C(t,T)&=-\mathcal{L}^{(+)}(-\omega-C(t,T)\beta\_{11}-D(t,T)\beta\_{21})+\kappa^{+}C(t,T)+\omega\Big(\frac{e^{\nu^{+}}}{1-\eta^{+}}-1\Big)+1,\\ \frac{\partial}{\partial t}D(t,T)&=-\mathcal{L}^{(-)}(-\omega-C(t,T)\beta\_{12}-D(t,T)\beta\_{22})+\kappa^{-}D(t,T)+\omega\Big(\frac{e^{\nu^{-}}}{1+\eta^{-}}-1\Big)+1,\end{split} |  | (12) |

where A​(T,T)=0A(T,T)=0, C​(T,T)=ω+C(T,T)=\omega^{+}, D​(T,T)=ω−D(T,T)=\omega^{-} with operators ℒ+\mathcal{L}^{+} and ℒ−\mathcal{L}^{-} defined in Equations [9](https://arxiv.org/html/2510.21297v1#S2.E9 "In 2.1 Price dynamics under ℙ-measure ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps") and [10](https://arxiv.org/html/2510.21297v1#S2.E10 "In 2.1 Price dynamics under ℙ-measure ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps"), respectively.

See Appendix [A](https://arxiv.org/html/2510.21297v1#A1 "Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps") for the [proof](https://arxiv.org/html/2510.21297v1#A1.SS2 "A.2 Proof of Proposition 1 ‣ Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps").

### 2.3 Equivalent risk-neutral measure ℚ\mathbb{Q}

We now construct the model dynamics under an equivalent martingale measure ℚ\mathbb{Q} such that the discounted stock
price process is a martingale. This is an extension of (Hainaut and
Moraux, [2018](https://arxiv.org/html/2510.21297v1#bib.bib28)) to a bivariate self-exiting Hawks process.
Introduce the Radon-Nikodym derivative process defined by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℚd​ℙ|ℱt=MtM0,t≥0,\displaystyle\frac{\text{d}\mathbb{Q}}{\text{d}\mathbb{P}}\Big|\mathcal{F}\_{t}=\frac{M\_{t}}{M\_{0}},\quad t\geq 0, |  | (13) |

where {Mt}t≥0\{M\_{t}\}\_{t\geq 0} is a local martingale under ℙ\mathbb{P}, specified below. By construction, we have the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[(d​ℚd​ℙ|ℱT)]=1,T≥0.\displaystyle{\mathbb{E}}^{\mathbb{P}}\left[\left(\frac{{\rm d}\mathbb{Q}}{{\rm d}\mathbb{P}}\big|\mathcal{F}\_{T}\right)\right]=1,\ T\geq 0. |  | (14) |

Define exponential processes of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mt​(ξ+,ξ−,φ)​=defexp⁡{κ1+​(ξ+)​λt++ξ+​∑j=1Nt(1)Jj++κ1−​(ξ−)​λt−+ξ−​∑j=1Nt(2)Jj−}⋅exp⁡{q2​(ξ+,ξ−)​t}⋅exp⁡{−12​∫0tφ2​(s)​𝑑s−∫0tφ​(s)​𝑑Ws},\begin{split}M\_{t}\left(\xi^{+},\xi^{-},\varphi\right)\overset{\text{def}}{=}&\exp\left\{\kappa^{+}\_{1}(\xi^{+})\lambda^{+}\_{t}+\xi^{+}\sum\_{j=1}^{N\_{t}^{(1)}}J^{+}\_{j}+\kappa^{-}\_{1}(\xi^{-})\lambda^{-}\_{t}+\xi^{-}\sum\_{j=1}^{N\_{t}^{(2)}}J^{-}\_{j}\right\}\\ &\cdot\exp\left\{q\_{2}\left(\xi^{+},\xi^{-}\right)t\right\}\\ &\cdot\exp\left\{-\frac{1}{2}\int\_{0}^{t}\varphi^{2}(s)ds-\int\_{0}^{t}\varphi(s)dW\_{s}\right\},\end{split} |  | (15) |

where ξ+,ξ−∈ℝ\xi^{+},\xi^{-}\in\mathbb{R} are two parameters that specify the risk-premia of positive and negative jumps, respectively, and that are to be estimated from options data. q1+​(ξ+),q1−​(ξ−),q2​(ξ+,ξ−)q\_{1}^{+}(\xi^{+}),q\_{1}^{-}(\xi^{-}),q\_{2}(\xi^{+},\xi^{-}) are real-valued functions, and φ​(t)\varphi(t) is an adapted process adapted to {ℱt}t≥0\{\mathcal{F}\_{t}\}\_{t\geq 0}.
In Proposition [5](https://arxiv.org/html/2510.21297v1#Thmlemma5 "Proposition 5. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps") below, we will choose

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(t)=φ+φ+​λt++φ−​λt−,\varphi(t)=\varphi+\varphi^{+}\lambda\_{t}^{+}+\varphi^{-}\lambda\_{t}^{-}, |  | (16) |

where φ,φ+,φ−∈ℝ\varphi,\varphi^{+},\varphi^{-}\in{\mathbb{R}} are constants.
We note that the process MtM\_{t} is strictly positive, so that, provided it is a martingale, the probability measures ℙ\mathbb{P} and ℚ\mathbb{Q} are absolutely continuous.
The following proposition specifies martingale conditions for {Mt}t≥0\left\{M\_{t}\right\}\_{t\geq 0}.

###### Proposition 2.

If, for any ξ+\xi^{+} and ξ−\xi^{-} ∈𝐑\in\mathbf{R}, there exists a solution specified as functions q1+​(ξ+)q\_{1}^{+}(\xi^{+}), q1−​(ξ−)q\_{1}^{-}(\xi^{-}) and q2​(ξ+,ξ−)q\_{2}(\xi^{+},\xi^{-}) of the following system:

|  |  |  |  |
| --- | --- | --- | --- |
|  | q1+​(ξ+)​κ+​θ++q1−​(ξ−)​κ−​θ−+q2​(ξ+,ξ−)=0,ℒ(+)​(−χ+)−1−q1+​(ξ+)​κ+=0,ℒ(−)​(−χ−)−1−q1−​(ξ−)​κ−=0,\begin{split}q\_{1}^{+}(\xi^{+})\kappa^{+}\theta^{+}+q\_{1}^{-}(\xi^{-})\kappa^{-}\theta^{-}+q\_{2}(\xi^{+},\xi^{-})&=0,\\ \mathcal{L}^{(+)}(-\chi^{+})-1-q\_{1}^{+}(\xi^{+})\kappa^{+}&=0,\\ \mathcal{L}^{(-)}(-\chi^{-})-1-q\_{1}^{-}(\xi^{-})\kappa^{-}&=0,\end{split} |  | (17) |

then MtM\_{t} is a local martingale. Here, we introduce new variables χ+\chi^{+} and χ−\chi^{-} as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | χ+=q1+​(ξ+)​β11+q1−​(ξ−)​β21+ξ+,χ−=q1+​(ξ+)​β12+q1−​(ξ−)​β22+ξ−.\begin{split}\chi^{+}&=q\_{1}^{+}(\xi^{+})\beta\_{11}+q\_{1}^{-}(\xi^{-})\beta\_{21}+\xi^{+},\\ \chi^{-}&=q\_{1}^{+}(\xi^{+})\beta\_{12}+q\_{1}^{-}(\xi^{-})\beta\_{22}+\xi^{-}.\end{split} |  | (18) |

See Appendix [A](https://arxiv.org/html/2510.21297v1#A1 "Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps") for the [proof](https://arxiv.org/html/2510.21297v1#A1.SS3 "A.3 Proof of Proposition 2 ‣ Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps").

We note that the system of equations in Eq.[17](https://arxiv.org/html/2510.21297v1#S2.E17 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps") is non-linear because of its variables entering into non-linear functions ℒ(+)\mathcal{L}^{(+)} and ℒ(−)\mathcal{L}^{(-)}. First, we make the following assumption that the risk-premium functions are linear.

###### Assumption 2.1.

We assume that the real-valued functions are specified by means of a linear system of equations as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | q1+​(ξ+)=c++ξ+q1−​(ξ−)=c−+ξ−q2​(ξ+,ξ−)=c+ξ++ξ−,\begin{split}q\_{1}^{+}(\xi^{+})&=c^{+}+\xi^{+}\\ q\_{1}^{-}(\xi^{-})&=c^{-}+\xi^{-}\\ q\_{2}(\xi^{+},\xi^{-})&=c+\xi^{+}+\xi^{-},\end{split} |  | (19) |

where c+,c−,c∈ℝc^{+},c^{-},c\in\mathbb{R} are internal parameters which are determined so that the system in Eq ([17](https://arxiv.org/html/2510.21297v1#S2.E17 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) is satisfied for any choice of ξ+\xi^{+} and ξ−\xi^{-}.

Second, we linearise the system of equations in ([17](https://arxiv.org/html/2510.21297v1#S2.E17 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")), by making the following assumption.

###### Assumption 2.2.

The variables χ+\chi^{+} and χ−\chi^{-} in Eq. ([18](https://arxiv.org/html/2510.21297v1#S2.E18 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) are external variables that specify the risk premium, while variables ξ+\xi^{+} and ξ−\xi^{-} become internal parameters inferred using Eq.([18](https://arxiv.org/html/2510.21297v1#S2.E18 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")).

###### Corollary 1.

The specification of the risk-premium is defined by the two external parameters χ+\chi^{+} and χ−\chi^{-}. The internal parameters of linear risk-premium functions in Eq. ([19](https://arxiv.org/html/2510.21297v1#S2.E19 "In Assumption 2.1. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")), internal risk premia ξ+\xi^{+} and ξ−\xi^{-} parameters in Eq. ([18](https://arxiv.org/html/2510.21297v1#S2.E18 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) along the martingale conditions in Eq. ([17](https://arxiv.org/html/2510.21297v1#S2.E17 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) are determined by five internal parameters (ξ+,ξ−,c+,c−,c)(\xi^{+},\xi^{-},c^{+},c^{-},c) which are obtained by solving the following linear system:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1+β11β21β11β210β121+β22β12β220κ+​θ+κ−​θ−κ+​θ+κ−​θ−11010001010)​(ξ+ξ−c+c−c)=(χ+χ−0(ℒ(+)​(−χ+)−1)/κ+(ℒ(−)​(−χ−)−1)/κ−).\begin{pmatrix}1+\beta\_{11}&\beta\_{21}&\beta\_{11}&\beta\_{21}&0\\ \beta\_{12}&1+\beta\_{22}&\beta\_{12}&\beta\_{22}&0\\ \kappa^{+}\theta^{+}&\kappa^{-}\theta^{-}&\kappa^{+}\theta^{+}&\kappa^{-}\theta^{-}&1\\ 1&0&1&0&0\\ 0&1&0&1&0\end{pmatrix}\begin{pmatrix}\xi^{+}\\ \xi^{-}\\ c^{+}\\ c^{-}\\ c\end{pmatrix}=\begin{pmatrix}\chi^{+}\\ \chi^{-}\\ 0\\ \left(\mathcal{L}^{(+)}(-\chi^{+})-1\right)\big/\kappa^{+}\\ \left(\mathcal{L}^{(-)}(-\chi^{-})-1\right)\big/\kappa^{-}\end{pmatrix}. |  | (20) |

###### Proposition 3.

The system of linear equations in Eq. ([20](https://arxiv.org/html/2510.21297v1#S2.E20 "In Corollary 1. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) in (ξ+,ξ−,c+,c−,c)(\xi^{+},\xi^{-},c^{+},c^{-},c) has a unique solution.

###### Proof.

The determinant of the coefficient matrix in Eq.([20](https://arxiv.org/html/2510.21297v1#S2.E20 "In Corollary 1. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) is equal to one, so it is invertible and a solution to the linear system exists and is unique.
∎

This chain of results establishes that the equivalent martingale measure ℚ\mathbb{Q} is fully characterised by the two external risk-premium parameters χ+\chi^{+} and χ−\chi^{-}, which can be interpreted as market-implied jump risk premia for positive and negative jumps, respectively. Given any such pair (χ+,χ−)(\chi^{+},\chi^{-}), the corresponding internal parameters (ξ+,ξ−,c+,c−,c)(\xi^{+},\xi^{-},c^{+},c^{-},c) that define the Radon-Nikodym derivative are uniquely determined by solving the linear system in Equation ([20](https://arxiv.org/html/2510.21297v1#S2.E20 "In Corollary 1. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")). The martingale property of the Radon-Nikodym derivative process MtM\_{t} is therefore always guaranteed under this construction.

Crucially, the transformation of the model from the physical measure ℙ\mathbb{P} to the risk-neutral measure ℚ\mathbb{Q} depends only on the values of χ+\chi^{+} and χ−\chi^{-}. This leads to a clean and tractable separation between the statistical and risk-neutral dynamics, which then enables model calibration and risk-premium estimation from observed option prices. As shown in Proposition [4](https://arxiv.org/html/2510.21297v1#Thmlemma4 "Proposition 4 (Jump intensity dynamics under the risk-neutral measure ℚ ). ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps"), the jump intensity dynamics under ℚ\mathbb{Q} inherit a similar structure to those under ℙ\mathbb{P}, with appropriately adjusted parameters. Thus, the model maintains internal consistency and interpretability under both measures, while enabling flexible inference of jump risk premia from market data.

###### Proposition 4 (Jump intensity dynamics under the risk-neutral measure ℚ{\mathbb{Q}} ).

Let
Nt(1),ℚN^{(1),\mathbb{Q}}\_{t} and Nt(2),ℚN^{(2),\mathbb{Q}}\_{t} be the counting processes of positive and negative jumps under the measure ℚ\mathbb{Q} with intensities

|  |  |  |  |
| --- | --- | --- | --- |
|  | λt+,ℚ=ℒ(+)​(−χ+)​λt+,λt−,ℚ=ℒ(−)​(−χ−)​λt−,\lambda^{+,\mathbb{Q}}\_{t}=\mathcal{L}^{(+)}\left(-\chi^{+}\right)\lambda^{+}\_{t},\qquad\lambda^{-,\mathbb{Q}}\_{t}=\mathcal{L}^{(-)}\left(-\chi^{-}\right)\lambda^{-}\_{t}, |  | (21) |

where χ+\chi^{+} and χ−\chi^{-} are external risk-premium parameters in Eq.([18](https://arxiv.org/html/2510.21297v1#S2.E18 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")).

The evolution of jump intensity rates λt+,ℚ\lambda^{+,\mathbb{Q}}\_{t} and λt−,ℚ\lambda^{-,\mathbb{Q}}\_{t} under ℚ\mathbb{Q} are driven by the following dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​λt+,ℚ=κ+​(θ+,ℚ−λt+,ℚ)​d​t+β11ℚ​J+,ℚ​d​Nt(1),ℚ+β12−,ℚ​J−,ℚ​d​Nt(2),ℚd​λt−,ℚ=κ−​(θ−,ℚ−λt−,ℚ)​d​t+β21ℚ​J+,ℚ​d​Nt(1),ℚ+β22ℚ​J−,ℚ​d​Nt(2),ℚ,\begin{split}{\rm d}\lambda^{+,\mathbb{Q}}\_{t}&=\kappa^{+}\left(\theta^{+,\mathbb{Q}}-\lambda^{+,\mathbb{Q}}\_{t}\right){\rm d}t+\beta^{\mathbb{Q}}\_{11}J^{+,\mathbb{Q}}\,{\rm d}N^{(1),\mathbb{Q}}\_{t}+\beta^{-,\mathbb{Q}}\_{12}J^{-,\mathbb{Q}}\,{\rm d}N^{(2),\mathbb{Q}}\_{t}\\ {\rm d}\lambda^{-,\mathbb{Q}}\_{t}&=\kappa^{-}\left(\theta^{-,\mathbb{Q}}-\lambda^{-,\mathbb{Q}}\_{t}\right){\rm d}t+\beta^{\mathbb{Q}}\_{21}J^{+,\mathbb{Q}}\,{\rm d}N^{(1),\mathbb{Q}}\_{t}+\beta^{\mathbb{Q}}\_{22}J^{-,\mathbb{Q}}\,{\rm d}N^{(2),\mathbb{Q}}\_{t},\end{split} |  | (22) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | θ+,ℚ\displaystyle\theta^{+,\mathbb{Q}} | =ℒ(+)​(−χ+)​θ+,β11ℚ=ℒ(+)​(−χ+)​β11,β12ℚ=ℒ(+)​(−χ+)​β12,\displaystyle=\mathcal{L}^{(+)}(-\chi^{+})\theta^{+},\ \beta^{\mathbb{Q}}\_{11}=\mathcal{L}^{(+)}(-\chi^{+})\beta\_{11},\ \beta^{\mathbb{Q}}\_{12}=\mathcal{L}^{(+)}(-\chi^{+})\beta\_{12}, |  | (23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | θ−,ℚ\displaystyle\theta^{-,\mathbb{Q}} | =ℒ(−)​(−χ−)​θ−,β21ℚ=ℒ(−)​(−χ−)​β21,β22ℚ=ℒ(−)​(−χ−)​β22,\displaystyle=\mathcal{L}^{(-)}(-\chi^{-})\theta^{-},\ \beta^{\mathbb{Q}}\_{21}=\mathcal{L}^{(-)}(-\chi^{-})\beta\_{21},\ \beta^{\mathbb{Q}}\_{22}=\mathcal{L}^{(-)}(-\chi^{-})\beta\_{22}, |  | (24) |

Here, J+,ℚJ^{+,\mathbb{Q}} and J−,ℚJ^{-,\mathbb{Q}} are realizations of positive and negative jumps from distributions with probability density functions(PDFs)
ϖ+,ℚ​(j+)\varpi^{+,\mathbb{Q}}(j^{+}) and ϖ−,ℚ​(j−)\varpi^{-,\mathbb{Q}}(j^{-}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϖ+,ℚ​(j)\displaystyle\varpi^{+,\mathbb{Q}}(j) | =1η+,ℚ​exp⁡(−1η+,ℚ​(j−ν+))​𝟙{j>ν+},ϖ−,ℚ​(j)=1η−,ℚ​exp⁡(1η−,ℚ​(j−ν−))​𝟙{j<ν−}\displaystyle=\frac{1}{\eta^{+,\mathbb{Q}}}\exp\left(-\frac{1}{\eta^{+,\mathbb{Q}}}(j-\nu^{+})\right)\mathbbm{1}\_{\{j>\nu^{+}\}},\ \varpi^{-,\mathbb{Q}}(j)=\frac{1}{\eta^{-,\mathbb{Q}}}\exp\left(\phantom{-}\frac{1}{\eta^{-,\mathbb{Q}}}(j-\nu^{-})\right)\mathbbm{1}\_{\{j<\nu^{-}\}} |  |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | η+,ℚ\displaystyle\eta^{+,\mathbb{Q}} | =η+1−η+​χ+,η−,ℚ=η−1+η−​χ−.\displaystyle=\frac{\eta^{+}}{1-\eta^{+}\chi^{+}},\ \eta^{-,\mathbb{Q}}=\frac{\eta^{-}}{1+\eta^{-}\chi^{-}}. |  | (25) |

See Appendix [A](https://arxiv.org/html/2510.21297v1#A1 "Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps") for the [proof](https://arxiv.org/html/2510.21297v1#A1.SS4 "A.4 Proof of Proposition 4 ‣ Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps").
The proposition [4](https://arxiv.org/html/2510.21297v1#Thmlemma4 "Proposition 4 (Jump intensity dynamics under the risk-neutral measure ℚ ). ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps") indicates that the dynamics of the intensities and the PDFs of the jump sizes are specified by the two external parameters χ+\chi^{+} and χ−\chi^{-}. Accordingly, for model calibration to implied volatility data, we need to infer a pair of value of χ+\chi^{+} and χ−\chi^{-} that provides the best fit. The following proposition specifies φ​(t)\varphi(t) such that an equivalent risk-neutral measure is obtained.

###### Proposition 5.

We introduce the adapted process φ​(t)\varphi(t) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(t)\displaystyle\varphi(t) | =μ−rσ−𝔼​(eJ+−1)−ℒ(+)​(−χ+)​𝔼ℚ​(eJ+,ℚ−1)σ​λt+−𝔼​(eJ−−1)+ℒ(−)​(−χ−)​𝔼ℚ​(eJ−,ℚ−1)σ​λt−,\displaystyle=\frac{\mu-r}{\sigma}-\frac{{\mathbb{E}}(e^{J^{+}}-1)-\mathcal{L}^{(+)}(-\chi^{+}){\mathbb{E}}^{\mathbb{Q}}(e^{J^{+,{\mathbb{Q}}}}-1)}{\sigma}\,\lambda\_{t}^{+}-\frac{{\mathbb{E}}(e^{J^{-}}-1)+\mathcal{L}^{(-)}(-\chi^{-}){\mathbb{E}}^{\mathbb{Q}}(e^{J^{-,{\mathbb{Q}}}}-1)}{\sigma}\lambda\_{t}^{-}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =μ−rσ−λt+​𝔼​(eJ+−1)−λt+,ℚ​𝔼ℚ​(eJ+,ℚ−1)σ−λt−​𝔼​(eJ−−1)−λt−,ℚ​𝔼ℚ​(eJ−,ℚ−1)σ,\displaystyle=\frac{\mu-r}{\sigma}-\frac{\lambda^{+}\_{t}{\mathbb{E}}(e^{J^{+}}-1)-\lambda^{+,\mathbb{Q}}\_{t}{\mathbb{E}}^{\mathbb{Q}}(e^{J^{+,{\mathbb{Q}}}}-1)}{\sigma}-\frac{\lambda^{-}\_{t}{\mathbb{E}}(e^{J^{-}}-1)-\lambda^{-,\mathbb{Q}}\_{t}{\mathbb{E}}^{\mathbb{Q}}(e^{J^{-,{\mathbb{Q}}}}-1)}{\sigma}, |  | (26) |

where rr is the risk free rate. Then the log return process Xt=ln⁡(St/S0)X\_{t}=\ln(S\_{t}/S\_{0}) is driven under ℚ\mathbb{Q} by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=(r−σ22)​d​t+σ​d​Wtℚ+(J+,ℚ​d​Ntℚ,(1)−λt+,ℚ​𝔼ℚ​(𝐞J+,ℚ−1)​d​t)+(J−,ℚ​d​Ntℚ,(2)−λt−,ℚ​𝔼ℚ​(𝐞J−,ℚ−1)​d​t),\begin{split}{\rm d}X\_{t}&=\left(r-\frac{\sigma^{2}}{2}\right){\rm d}t+\sigma\,{\rm d}W^{\mathbb{Q}}\_{t}\\ &+\Big(J^{+,\mathbb{Q}}\,{\rm d}N\_{t}^{\mathbb{Q},(1)}-\lambda\_{t}^{+,\mathbb{Q}}{\mathbb{E}}^{\mathbb{Q}}({\bf e}^{J^{+,\mathbb{Q}}}-1)\,{\rm d}t\Big)+\Big(J^{-,\mathbb{Q}}\,{\rm d}N\_{t}^{\mathbb{Q},(2)}-\lambda\_{t}^{-,\mathbb{Q}}{\mathbb{E}}^{\mathbb{Q}}({\bf e}^{J^{-,\mathbb{Q}}}-1)\,{\rm d}t\Big),\\ \end{split} |  | (27) |

where WℚW^{\mathbb{Q}} is a standard Brownian motion under ℚ\mathbb{Q}, and the discounted price process is a ℚ\mathbb{Q}-martingale.

See Appendix [A](https://arxiv.org/html/2510.21297v1#A1 "Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps") for the [proof](https://arxiv.org/html/2510.21297v1#A1.SS5 "A.5 Proof of Proposition 5 ‣ Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps").
The function φ​(t)\varphi(t) specifies the risk premia associated with the continuous component of the process. We will discuss the jump risk premia in Section [4](https://arxiv.org/html/2510.21297v1#S4 "4 Positive and negative jump risk premia ‣ Jump risk premia in the presence of clustered jumps").

###### Corollary 2 (MGF in Proposition [1](https://arxiv.org/html/2510.21297v1#Thmlemma1 "Proposition 1. ‣ 2.2 Moment-generating function of joint dynamics ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps") under ℚ\mathbb{Q}).

The MGF of log-return XTX\_{T} with the dynamics in Eq.([27](https://arxiv.org/html/2510.21297v1#S2.E27 "In Proposition 5. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) under ℚ\mathbb{Q} is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gℚ​(ω;T,x,λ+,ℚ,λ−,ℚ)≡𝔼ℚ​(exp⁡(ω​XT)|Xt,λt+,ℚ,λt−,ℚ)=exp⁡(A​(t,T)+ω​Xt+C​(t,T)​λt+,ℚ+D​(t,T)​λt−,ℚ)=exp⁡(ω​Xt)​E​(t,T;ω),\begin{split}G^{\mathbb{Q}}(\omega;T,x,\lambda^{+,\mathbb{Q}},\lambda^{-,\mathbb{Q}})&\equiv{\mathbb{E}}^{\mathbb{Q}}\left(\exp(\omega X\_{T})\big|X\_{t},\lambda^{+,\mathbb{Q}}\_{t},\lambda^{-,\mathbb{Q}}\_{t}\right)\\ &=\exp\left(A(t,T)+\omega X\_{t}+C(t,T)\lambda\_{t}^{+,\mathbb{Q}}+D(t,T)\lambda\_{t}^{-,\mathbb{Q}}\right)\\ &=\exp\left(\omega X\_{t}\right)E(t,T;\omega),\end{split} |  | (28) |

where functions A,C,and ​DA,C,\text{and }D solve Eq.([11](https://arxiv.org/html/2510.21297v1#S2.E11 "In Proposition 1. ‣ 2.2 Moment-generating function of joint dynamics ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) with ω+=0,ω−=0\omega^{+}=0,\ \omega^{-}=0 and with the following substitution of model parameters:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ→r,θ+→θ+,ℚ=ℒ(+)​(−χ+)​θ+,β11→β11ℚ=ℒ(+)​(−χ+)​β11,β12→β12ℚ=ℒ(+)​(−χ+)​β12,θ−→θ−,ℚ=ℒ(−)​(−χ−)​θ−,β21→β21ℚ=ℒ(−)​(−χ−)​β21,β22ℚ→β22ℚ=ℒ(−)​(−χ−)​β22,η+→η+,ℚ=η+1−η+​χ+,η−→η−,ℚ=η−1+η−​χ−.\begin{split}&\mu\rightarrow r,\\ &\theta^{+}\rightarrow\theta^{+,\mathbb{Q}}=\mathcal{L}^{(+)}(-\chi^{+})\theta^{+},\ \beta\_{11}\rightarrow\beta^{\mathbb{Q}}\_{11}=\mathcal{L}^{(+)}(-\chi^{+})\beta\_{11},\ \beta\_{12}\rightarrow\beta^{\mathbb{Q}}\_{12}=\mathcal{L}^{(+)}(-\chi^{+})\beta\_{12},\\ &\theta^{-}\rightarrow\theta^{-,\mathbb{Q}}=\mathcal{L}^{(-)}(-\chi^{-})\theta^{-},\ \beta\_{21}\rightarrow\beta^{\mathbb{Q}}\_{21}=\mathcal{L}^{(-)}(-\chi^{-})\beta\_{21},\ \beta^{\mathbb{Q}}\_{22}\rightarrow\beta^{\mathbb{Q}}\_{22}=\mathcal{L}^{(-)}(-\chi^{-})\beta\_{22},\\ &\eta^{+}\rightarrow\eta^{+,\mathbb{Q}}=\frac{\eta^{+}}{1-\eta^{+}\chi^{+}},\ \eta^{-}\rightarrow\eta^{-,\mathbb{Q}}=\frac{\eta^{-}}{1+\eta^{-}\chi^{-}}.\end{split} |  | (29) |

###### Corollary 3.

Using the Lewis-Lipton formula (Lewis ([2001](https://arxiv.org/html/2510.21297v1#bib.bib36)), Lipton ([2002](https://arxiv.org/html/2510.21297v1#bib.bib37))), the value of a call option, denoted by Uc​a​l​lU^{call}, and a put option, denoted by Up​u​tU^{put}, with strike price KK and maturity time TT is computed for log-price dynamics in Eq.([27](https://arxiv.org/html/2510.21297v1#S2.E27 "In Proposition 5. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) under the risk-neutral measure ℚ\mathbb{Q} by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uc​a​l​l​(τ,S,K)=e−r​τ​S−U​(τ,X,K),Up​u​t​(τ,S,K)=e−r​τ​K−U​(τ,X,K),\begin{split}&U^{call}(\tau,S,K)=e^{-r\tau}S-U(\tau,X,K),\\ &U^{put}(\tau,S,K)=e^{-r\tau}K-U(\tau,X,K),\end{split} |  | (30) |

where τ=T−t\tau=T-t. Here, U​(τ,X,K)U(\tau,X,K) is the price of the capped payoff min⁡(S,K)\min(S,K) which is computed by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(τ,X,K)=e−r​τ​Kπ​ℜ⁡[∫0∞e−(i​y−1/2)​X∗​1y2+1/4​E​(τ;ω=i​y−1/2)​𝑑y],\begin{split}U(\tau,X,K)&=\frac{e^{-r\tau}K}{\pi}\Re\left[\int^{\infty}\_{0}e^{-(iy-1/2)X^{\*}}\frac{1}{y^{2}+1/4}E(\tau;\omega=iy-1/2)dy\right],\end{split} |  | (31) |

where X∗=ln⁡(S/K)X^{\*}=\ln(S/K) is log-moneyness, ℜ⁡(x)\Re(x) is the real part of xx, and E​(τ;ω)E(\tau;\omega) is specified in Eq.([28](https://arxiv.org/html/2510.21297v1#S2.E28 "In Corollary 2 (MGF in Proposition 1 under ℚ). ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")).

For the proof, see the proof of Proposition 5.1. in Sepp and
Rakhmonov ([2023](https://arxiv.org/html/2510.21297v1#bib.bib45)).

For numerical implementation, the system of ODEs in Eq.([11](https://arxiv.org/html/2510.21297v1#S2.E11 "In Proposition 1. ‣ 2.2 Moment-generating function of joint dynamics ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) must be solved numerically using standard Runge-Kutta methods. Given that the computation of the MGF part E​(τ;ω)E(\tau;\omega) does not depend on the strike price of the option, the function E​(τ;ω)E(\tau;\omega) can be computed on a grid and apply for the numerical calculation of call and put options at the same maturity time with different strike prices111Github project StochVolModels provides Python code with prototype implementation of option valuation using Eqs ([30](https://arxiv.org/html/2510.21297v1#S2.E30 "In Corollary 3. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) and ([31](https://arxiv.org/html/2510.21297v1#S2.E31 "In Corollary 3. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")), see <https://github.com/ArturSepp/StochVolModels/blob/main/stochvolmodels/pricers/hawkes_jd_pricer.py>..

## 3 Two stage approach calibration of the model

We adopt the following two-stage calibration approach. First, we estimate the model parameters under statistical measure ℙ\mathbb{P} from historical price data. Then, we infer the risk premia and the model parameters under the risk-neutral measure ℚ\mathbb{Q} using the options data.

### 3.1 Time series estimation

To filter out jumps from time series of returns, we implement a POT procedure similarly to the approach in Embrechts
et al. ([2011](https://arxiv.org/html/2510.21297v1#bib.bib19)) and (Hainaut, [2022](https://arxiv.org/html/2510.21297v1#bib.bib27), Chapter 4). We consider a sample of equally-spaced log-returns observed in the time window [0,T][0,\ T].
The POT procedure labels the log-returns that exceed the threshold as jumps. The underlying assumption is that the continuous part of the price process has normally distributed log-returns which implies that sampled returns, filtered by excluding jumps, have zero skewness and zero excess kurtosis.

Let (X(ν+,ν−)):={Xt:ν−<Xt<ν+}(X^{(\nu^{+},\nu^{-})}):=\left\{X\_{t}:\nu^{-}<X\_{t}<\nu^{+}\right\} the set of log-returns bounded by ν−\nu^{-} and ν+\nu^{+}.
The estimate of the thresholds is then given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ν^+,ν^−)=argminν+,ν−​[|skew​(X(ν+,ν−))|+|kurt​(X(ν+,ν−))|],\displaystyle\left(\widehat{\nu}^{+},\ \widehat{\nu}^{-}\right)=\underset{\nu^{+},\nu^{-}}{\text{argmin}}\left[|\text{skew}(X^{(\nu^{+},\nu^{-})})|+|\text{kurt}(X^{(\nu^{+},\nu^{-})})|\right], |  | (32) |

where skew​(X)=|X|−1​∑x∈X(x−μ^X)3/σ^X3\text{skew}(X)=|X|^{-1}\sum\_{x\in X}(x-\hat{\mu}\_{X})^{3}/\hat{\sigma}\_{X}^{3},
kurt​(X)=|X|−1​∑x∈X(x−μ^X)4/σ^X4−3\text{kurt}(X)=|X|^{-1}\sum\_{x\in X}(x-\hat{\mu}\_{X})^{4}/\hat{\sigma}\_{X}^{4}-3,
μ^X\hat{\mu}\_{X} and σ^X\hat{\sigma}\_{X} are the sample mean and standard deviation, respectively, and |X|−1|X|^{-1} is the sample size.
Given estimated thresholds, we identify the set of positive jump events 𝒥+\mathcal{J}^{+} and the set of negative jump events 𝒥−\mathcal{J}^{-} respectively as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥+={J+​(s)}s≤T={Xs∈X:Xs≥ν^+​ and ​s≤T},𝒥−={J−​(s)}s≤T={Xs∈X:Xs≤ν^−​ and ​s≤T}.\begin{split}\mathcal{J}^{+}&=\left\{J^{+}(s)\right\}\_{s\leq T}=\left\{X\_{s}\in X:X\_{s}\geq\widehat{\nu}^{+}\text{ and }s\leq T\right\},\\ \mathcal{J}^{-}&=\left\{J^{-}(s)\right\}\_{s\leq T}=\left\{X\_{s}\in X:X\_{s}\leq\widehat{\nu}^{-}\text{ and }s\leq T\right\}.\end{split} |  | (33) |

We construct the counting processes for positive jumps and for the negative jumps as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | N(1)^=#​{Xs∈X:Xs≥ν^+​ and ​s≤T},N(2)^=#​{Xs∈X:Xs≤ν^−​ and ​s≤T}.\begin{split}\widehat{N^{(1)}}&=\#\left\{X\_{s}\in X:X\_{s}\geq\widehat{\nu}^{+}\text{ and }s\leq T\right\},\\ \widehat{N^{(2)}}&=\#\left\{X\_{s}\in X:X\_{s}\leq\widehat{\nu}^{-}\text{ and }s\leq T\right\}.\end{split} |  | (34) |

We denote the corresponding sequences of arrival times of positive jumps 𝒯+\mathcal{T}^{+}, of negative jumps 𝒯−\mathcal{T}^{-}, and an ordered union of jump arrival times 𝒯±\mathcal{T}^{\pm} by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯+={t∈[0,T]:Xt≥ν^+}={T1+,T2+,…,TN(1)^+},𝒯−={t∈[0,T]:Xt≤ν^−}={T1−,T2−,…,TN(2)^−},𝒯±={T[1]±,T[2]±,…,T[N(1)^+N(2)^]±}.\begin{split}&\mathcal{T}^{+}=\left\{t\in[0,\ T]:X\_{t}\geq\hat{\nu}^{+}\right\}=\left\{T^{+}\_{1},\ T^{+}\_{2},\ ...,\ T^{+}\_{\widehat{N^{(1)}}}\right\},\\ &\mathcal{T}^{-}=\left\{t\in[0,\ T]:X\_{t}\leq\hat{\nu}^{-}\right\}=\left\{T^{-}\_{1},\ T^{-}\_{2},\ ...,\ T^{-}\_{\widehat{N^{(2)}}}\right\},\\ &\mathcal{T}^{\pm}=\left\{T^{\pm}\_{[1]},\ T^{\pm}\_{[2]},\ ...,\ T^{\pm}\_{[\widehat{N^{(1)}}+\widehat{N^{(2)}}]}\right\}.\end{split} |  | (35) |

Jumps sizes are independent of other random variables and follow shifted exponential distributions.
Therefore, given the shift parameter estimates ν^+\widehat{\nu}^{+} and ν^−\widehat{\nu}^{-} from the POT procedure, the estimators of η+\eta^{+} and η−\eta^{-} are given by averaging:

|  |  |  |  |
| --- | --- | --- | --- |
|  | η^+=N(1)^−1​∑j∈𝒥+(j−ν^+),η^−=−N(2)^−1​∑j∈𝒥−(j+ν^−).\begin{split}\widehat{\eta}^{+}&=\widehat{N^{(1)}}^{-1}\sum\_{j\in\mathcal{J}^{+}}\left(j-\widehat{\nu}^{+}\right),\\ \widehat{\eta}^{-}&=-\widehat{N^{(2)}}^{-1}\sum\_{j\in\mathcal{J}^{-}}\left(j+\widehat{\nu}^{-}\right).\end{split} |  | (36) |

Next, we estimate the parameters of the intensities dynamics via the maximum likelihood estimator (MLE). We deploy a version of the multivariate log-likelihood function documented in Embrechts
et al. ([2011](https://arxiv.org/html/2510.21297v1#bib.bib19)) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡L′\displaystyle\ln L^{\prime} | =∑T+∈𝒯+ln⁡λ+​(T+−)​ϖ+​(J+​(T+))+∑T−∈𝒯−ln⁡λ−​(T−−)​ϖ−​(J−​(T−))\displaystyle=\sum\_{T^{+}\in\mathcal{T}^{+}}\ln\lambda^{+}(T^{+}-)\varpi^{+}(J^{+}(T^{+}))+\sum\_{T^{-}\in\mathcal{T}^{-}}\ln\lambda^{-}(T^{-}-)\varpi^{-}(J^{-}(T^{-})) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −∫0Tλ+​(t−)​d​t−∫0Tλ−​(t−)​d​t.\displaystyle-\int\_{0}^{T}\lambda^{+}(t-)\text{d}t-\int\_{0}^{T}\lambda^{-}(t-)\text{d}t. |  | (37) |

We note that the likelihood takes the left-continuous version (indicated by T−T-) of the intensities processes (see (Daley and
Vere-Jones, [2003](https://arxiv.org/html/2510.21297v1#bib.bib17), p. 232)). Since distributions of jumps sizes are already estimated throughout the POT procedure using Eq.([36](https://arxiv.org/html/2510.21297v1#S3.E36 "In 3.1 Time series estimation ‣ 3 Two stage approach calibration of the model ‣ Jump risk premia in the presence of clustered jumps")), we only need a partial likelihood for the intensity processes defined by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡L=∑T+∈𝒯+ln⁡λ+​(T+−)+∑T−∈𝒯−ln⁡λ−​(T−−)−∫0Tλ+​(t−)​d​t−∫0Tλ−​(t−)​d​t.\displaystyle\ln L=\sum\_{T^{+}\in\mathcal{T}^{+}}\ln\lambda^{+}(T^{+}-)+\sum\_{T^{-}\in\mathcal{T}^{-}}\ln\lambda^{-}(T^{-}-)-\int\_{0}^{T}\lambda^{+}(t-)\text{d}t-\int\_{0}^{T}\lambda^{-}(t-)\text{d}t. |  | (38) |

The relationship between the intensities and the model parameters is specified for s∈[T[k−1]±,T[k]±)s\in\left[T\_{[k-1]}^{\pm},\ T\_{[k]}^{\pm}\right) and k∈{1,2,…,N(1)^+N(2)^}k\in\left\{1,2,...,\ \widehat{N^{(1)}}+\widehat{N^{(2)}}\right\} as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λ+​(s)\displaystyle\lambda^{+}(s) | =θ++e−κ+​(s−T[k−1]±)​(λ+​(T[k−1]±)−θ+),\displaystyle=\theta^{+}+e^{-\kappa^{+}\left(s-T\_{[k-1]}^{\pm}\right)}\left(\lambda^{+}(T\_{[k-1]}^{\pm})-\theta^{+}\right), |  | (39) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λ−​(s)\displaystyle\lambda^{-}(s) | =θ−+e−κ−​(s−T[k−1]±)​(λ−​(T[k−1]±)−θ−).\displaystyle=\theta^{-}+e^{-\kappa^{-}\left(s-T\_{[k-1]}^{\pm}\right)}\left(\lambda^{-}(T\_{[k-1]}^{\pm})-\theta^{-}\right). |  | (40) |

In the event of positive jump T+∈𝒯+T^{+}\in\mathcal{T}^{+}, the intensities jump by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ+​(T+)=λ+​(T+−)+β11​J+​(T+),λ−​(T+)=λ−​(T+−)+β21​J+​(T+).\begin{split}\lambda^{+}(T^{+})&=\lambda^{+}(T^{+}-)+\beta\_{11}J^{+}(T^{+}),\\ \lambda^{-}(T^{+})&=\lambda^{-}(T^{+}-)+\beta\_{21}J^{+}(T^{+}).\end{split} |  | (41) |

In the event of a negative jump T−∈𝒯−T^{-}\in\mathcal{T}^{-}, the intensities jump by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ+​(T−)=λ+​(T−−)+β12​J−​(T−),λ−​(T−)=λ−​(T−−)+β22​J−​(T−).\begin{split}\lambda^{+}(T^{-})&=\lambda^{+}(T^{-}-)+\beta\_{12}J^{-}(T^{-}),\\ \lambda^{-}(T^{-})&=\lambda^{-}(T^{-}-)+\beta\_{22}J^{-}(T^{-}).\end{split} |  | (42) |

The integrals of the intensities in the partial likelihood Eq.([38](https://arxiv.org/html/2510.21297v1#S3.E38 "In 3.1 Time series estimation ‣ 3 Two stage approach calibration of the model ‣ Jump risk premia in the presence of clustered jumps")) can be computed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0Tλ+​(t−)​d​t=∑k=1N(1)^+N(2)^∫T[k−1]±T[k]±λ+​(t−)​d​t=∑k=1N(1)^+N(2)^θ+​(T[k]±−T[k−1]±)+(λ+​(T[k]±−)−θ+)​1−e−κ+​(T[k]±−T[k−1]±)κ+,∫0Tλ−​(t−)​d​t=∑k=1N(1)^+N(2)^θ−​(T[k]±−T[k−1]±)+(λ−​(T[k]±−)−θ−)​1−e−κ−​(T[k]±−T[k−1]±)κ−.\begin{split}\int\_{0}^{T}\lambda^{+}(t-)\text{d}t&=\sum\_{k=1}^{\widehat{N^{(1)}}+\widehat{N^{(2)}}}\int\_{T^{\pm}\_{[k-1]}}^{T^{\pm}\_{[k]}}\lambda^{+}(t-)\text{d}t\\ &=\sum\_{k=1}^{\widehat{N^{(1)}}+\widehat{N^{(2)}}}\theta^{+}(T\_{[k]}^{\pm}-T\_{[k-1]}^{\pm})+\left(\lambda^{+}(T\_{[k]}^{\pm}-)-\theta^{+}\right)\frac{1-e^{-\kappa^{+}(T\_{[k]}^{\pm}-T\_{[k-1]}^{\pm})}}{\kappa^{+}},\\ \int\_{0}^{T}\lambda^{-}(t-)\text{d}t&=\sum\_{k=1}^{\widehat{N^{(1)}}+\widehat{N^{(2)}}}\theta^{-}(T\_{[k]}^{\pm}-T\_{[k-1]}^{\pm})+\left(\lambda^{-}(T\_{[k]}^{\pm}-)-\theta^{-}\right)\frac{1-e^{-\kappa^{-}(T\_{[k]}^{\pm}-T\_{[k-1]}^{\pm})}}{\kappa^{-}}.\end{split} |  | (43) |

Therefore, given a set of model parameters, the intensities and their integrals can be computed quickly in a recursive way starting from time 0. We refer to Section 5.2 of Laub
et al. ([2021](https://arxiv.org/html/2510.21297v1#bib.bib35)) and references therein for the method of directly computing the likelihood.
We apply a numerical optimiser to obtain estimates of the jump parameters, κ^±,θ^±,{β^i​j}i,j=1,2\hat{\kappa}^{\pm},\ \hat{\theta}^{\pm},\{\hat{\beta}\_{ij}\}\_{i,j=1,2}, that maximise the likelihood.
Figure [2](https://arxiv.org/html/2510.21297v1#S3.F2 "Figure 2 ‣ 3.1 Time series estimation ‣ 3 Two stage approach calibration of the model ‣ Jump risk premia in the presence of clustered jumps") illustrates the estimation procedure applied to BTC daily returns from 2019-05-30 to 2023-10-03.

Figure 2: Subplot (A) shows BTC daily returns which are classified using the POT procedure as positive jumps (green), negative jumps (red), or non-jumps (yellow). Subplot (B) displays the model intensities estimated via MLE, calibrated using the interarrival times and magnitudes of the jumps identified by POT.

![Refer to caption](x2.png)

### 3.2 Calibration to market implied volatilities

Given a set of European option prices and corresponding set of implied volatilities, we deduce volatility σ\sigma, and risk-premia χ+\chi^{+} and χ−\chi^{-} by minimising the mean absolute percentage error (MAPE) as follows:

|  |  |  |
| --- | --- | --- |
|  | (σ^,χ^+,χ^−)=argminσ,χ+,χ−​∑i=1Iwi​|IVmarket​(τi,Ki,Oi)−IVmodel​(τi,Ki,Oi;σ,χ+,χ−)|IVmarket​(τi,Ki,Oi),\displaystyle\left(\widehat{\sigma},\ \widehat{\chi}^{+},\ \widehat{\chi}^{-}\right)=\underset{\sigma,\chi^{+},\chi^{-}}{\text{argmin}}\sum\_{i=1}^{I}w\_{i}\frac{\left|\text{IV}\_{\text{market}}\left(\tau\_{i},\ K\_{i},\ O\_{i}\right)-\text{IV}\_{\text{model}}\left(\tau\_{i},\ K\_{i},\ O\_{i};\ \sigma,\ \chi^{+},\ \chi^{-}\right)\right|}{\text{IV}\_{\text{market}}\left(\tau\_{i},\ K\_{i},\ O\_{i}\right)}, |  |

where II is the sample size, wiw\_{i} is the weight applied to the ithi^{\text{th}} option,
IVmarket​(τi,Ki,Oi)\text{IV}\_{\text{market}}\left(\tau\_{i},\ K\_{i},\ O\_{i}\right) is the Black-Scholes (BS) implied volatility of the ithi^{\text{th}} option with time-to-maturity τi\tau\_{i}, strike KiK\_{i}, and option type Oi∈{Call,Put}O\_{i}\in\left\{\text{Call},\ \text{Put}\right\}. Here,
IVmodel​(τi,Ki,Oi;σ,χ+,χ−)\text{IV}\_{\text{model}}\left(\tau\_{i},\ K\_{i},\ O\_{i};\ \sigma,\ \chi^{+},\ \chi^{-}\right) is the corresponding BS implied volatility produced by our model given σ\sigma, χ+\chi^{+}, and χ−\chi^{-}.
We take the market BS vega of each option as weight ww, thus assigning greater importance to options whose prices are more sensitive to mispricing of implied volatilities.

The computation of model implied volatilities given σ\sigma, χ+\chi^{+} and χ−\chi^{-} consists of the following steps.

1. 1.

   We compute λt±,ℚ\lambda^{\pm,\mathbb{Q}}\_{t}, κ±,ℚ\kappa^{\pm,\mathbb{Q}}, θ±,ℚ\theta^{\pm,\mathbb{Q}}, βi​jℚ\beta\_{ij}^{\mathbb{Q}} for i,j∈[1,2]i,j\in[1,2], and η±,ℚ\eta^{\pm,\mathbb{Q}} using transformation in Eq ([29](https://arxiv.org/html/2510.21297v1#S2.E29 "In Corollary 2 (MGF in Proposition 1 under ℚ). ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")).
2. 2.

   We apply the MGF under ℚ\mathbb{Q} in Eq.[28](https://arxiv.org/html/2510.21297v1#S2.E28 "In Corollary 2 (MGF in Proposition 1 under ℚ). ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps") along with risk-neutral drift rr and volatility σ\sigma to value call and put options using Eq.[30](https://arxiv.org/html/2510.21297v1#S2.E30 "In Corollary 3. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps").
3. 3.

   We infer model implied volatilities by inverting the Black-Scholes formula.

We use a numerical optimiser to estimate σ^,χ^+,χ^−\widehat{\sigma},\ \widehat{\chi}^{+},\ \widehat{\chi}^{-} that minimise the MAPE.

## 4 Positive and negative jump risk premia

Following the literature on variance risk premia (e.g. Carr and Wu, [2009](https://arxiv.org/html/2510.21297v1#bib.bib15); Bollerslev
et al., [2009](https://arxiv.org/html/2510.21297v1#bib.bib10); Almeida
et al., [2024](https://arxiv.org/html/2510.21297v1#bib.bib3)), we define jump risk premia as the difference between expected jump sizes under the statistical measure and expected jump sizes under the risk-neutral measure.

###### Corollary 4 (Using Proposition [5](https://arxiv.org/html/2510.21297v1#Thmlemma5 "Proposition 5. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")).

The positive jump risk premium denoted by γt+\gamma^{+}\_{t} and negative jump risk premium denoted γt−\gamma^{-}\_{t} are specified by:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γt+\displaystyle\gamma^{+}\_{t} | =λt+,ℚ​𝔼ℚ​(eJ+,ℚ−1)−λt+​𝔼​(eJ+−1),\displaystyle=\lambda^{+,\mathbb{Q}}\_{t}{\mathbb{E}}^{\mathbb{Q}}\big(e^{J^{+,{\mathbb{Q}}}}-1\big)-\lambda^{+}\_{t}{\mathbb{E}}\big(e^{J^{+}}-1\big), |  | (44) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γt−\displaystyle\gamma^{-}\_{t} | =λt−,ℚ​𝔼ℚ​(eJ−,ℚ−1)−λt−​𝔼​(eJ−−1).\displaystyle=\lambda^{-,\mathbb{Q}}\_{t}{\mathbb{E}}^{\mathbb{Q}}\big(e^{J^{-,{\mathbb{Q}}}}-1\big)-\lambda^{-}\_{t}{\mathbb{E}}\big(e^{J^{-}}-1\big). |  | (45) |

According to the model specification for the price process in Equation ([1](https://arxiv.org/html/2510.21297v1#S2.E1 "In 2.1 Price dynamics under ℙ-measure ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")),
the terms λt+​𝔼​(eJ+−1)\lambda\_{t}^{+}{\mathbb{E}}(e^{J^{+}}-1) and λt−​𝔼​(eJ−−1)\lambda\_{t}^{-}{\mathbb{E}}(e^{J^{-}}-1) are the compensators for positive and negative jumps under statistical measure ℙ{\mathbb{P}}, respectively. By Proposition [4](https://arxiv.org/html/2510.21297v1#Thmlemma4 "Proposition 4 (Jump intensity dynamics under the risk-neutral measure ℚ ). ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps"), the parameters χ+\chi^{+} and χ−\chi^{-} in Eq.([18](https://arxiv.org/html/2510.21297v1#S2.E18 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) specify compensators λt+,ℚ​𝔼ℚ​(eJ+,ℚ−1)\lambda^{+,\mathbb{Q}}\_{t}{\mathbb{E}}^{\mathbb{Q}}\big(e^{J^{+,{\mathbb{Q}}}}-1\big) and λt−,ℚ​𝔼ℚ​(eJ−,ℚ−1)\lambda^{-,\mathbb{Q}}\_{t}{\mathbb{E}}^{\mathbb{Q}}\big(e^{J^{-,{\mathbb{Q}}}}-1\big) under the risk-neutral measure ℚ{\mathbb{Q}}. Hereby, the parameters χ+\chi^{+} and χ−\chi^{-} are inferred from options data.

In this construction, the jump risk premia reflect the difference in forward-looking risk preferences inferred from option prices compared to risk preferences inferred from historical price dynamics. Positive γt+\gamma\_{t}^{+} and negative γt−\gamma\_{t}^{-} indicate that the market expects higher future jump risk than was observed in the past, and vice versa for negative γt+\gamma\_{t}^{+} and positive γt−\gamma\_{t}^{-}.
The jump risk premia are expressed in the same units as the drift rate μ\mu, i.e., as an annualised yield rate.

The separate treatment of positive and negative jumps is motivated by the fact that the market reacts differently to up and down moves in the price process. In particular, the left tail of the risk-neutral distribution is known to be more vulnerable to market downturns than the right tail to market upswings. This is also seen in the impulse response functions in Section [5.3](https://arxiv.org/html/2510.21297v1#S5.SS3 "5.3 Evolution of jump risk premia ‣ 5 Empirical Results ‣ Jump risk premia in the presence of clustered jumps") below, where the responses of positive and negative jump risk premia differ in magnitude and speed of decay in impact.

Figure [3](https://arxiv.org/html/2510.21297v1#S4.F3 "Figure 3 ‣ 4 Positive and negative jump risk premia ‣ Jump risk premia in the presence of clustered jumps") depicts the impact of jump risk premia on the implied volatility profiles of model-generated options with one month to maturity.
Generally, the magnitude of the jump risk premia is directly correlated with the overall level of model implied volatilities.
A higher positive jump risk premium and a lower negative jump risk premium contribute to a higher level of model implied volatilities.
However, as the panel on the top left reveals, the influence of
γ+\gamma^{+} is more pronounced on options with a moneyness greater than
1, predominantly in-the-money (ITM) call options.
The panel on the right shows the effect of the negative jump risk premium, where one has to bear in mind that a negative γ−\gamma^{-} indicates that more negative jump activity is expected under ℚ{\mathbb{Q}} than under ℙ{\mathbb{P}}. In turn, the more negative the γ−\gamma^{-} is, the higher the level of the model implied volatilities.
Similarly, this change in γ−\gamma^{-} shows a stronger impact on options with a moneyness less than 1, typically where the ITM put options are concentrated.

Figure [4](https://arxiv.org/html/2510.21297v1#S4.F4 "Figure 4 ‣ 4 Positive and negative jump risk premia ‣ Jump risk premia in the presence of clustered jumps") illustrates the impact of γ+\gamma^{+} and γ−\gamma^{-} on the risk-neutral probability density of one-month log returns. The figure reveals that γ+\gamma^{+} and γ−\gamma^{-} jointly govern the asymmetry and tail thickness of the risk-neutral density, encapsulating the market’s pricing of upward and downward jump risks.

Figure 3: 
The panels show model implied volatilities of one-month-maturity options under different positive and negative jump risk premium levels while keeping the opposite jump risk premium zero.
The levels of positive jump risk premium are indicated to the right of the corresponding model implied volatilities. The model implied volatilities in red are under zero positive and negative jump risk premia. [![Refer to caption](qletlogo_tr.png)IV\_smiles\_under\_diff\_risk\_premia\_level](https://github.com/QuantLet/HJP/tree/main/codes/jupyterNotebooks/IV_smiles_under_diff_risk_premia_level)

![Refer to caption](x3.png)



Figure 4: 
The panels display the risk-neutral probability densities of one-month log return under varying levels of the positive and negative jump risk premia, γ+\gamma^{+} and γ−\gamma^{-}. The left panel illustrates the effect of changes in risk-premia for calls γ+\gamma^{+} while holding γ−=0\gamma^{-}=0, and the right panel shows the effect of changes in risk-premia for puts γ−\gamma^{-} while holding γ+=0\gamma^{+}=0. Increasing γ+\gamma^{+} fattens the right tail of the distribution, leading to greater right-skewness in the distribution. In contrast, variation in γ−\gamma^{-} produces the opposite pattern: a fatter or thinner left tail depending on the sign of the premium. Together, γ+\gamma^{+} and γ−\gamma^{-} govern the asymmetry and tail behavior of the risk-neutral density, reflecting how markets price the risk of upward and downward jumps.

![Refer to caption](x4.png)

## 5 Empirical Results

### 5.1 Data and empirical study design

We study the options market for cryptocurrencies, with its dynamics heavily influenced by sentiment-driven jumps and severe price adjustments. In particular, we consider options on Bitcoin (BTC) which are the most liquid in cryptocurrency derivatives. We gather data on both BTC price and BTC options from Deribit, a crypto derivatives exchange established in June 2016. The exchange offers options and futures trading for both BTC and ETH and provides extensive data on BTC prices and option prices through its API. Deribit’s comparatively low fees for market makers contribute to the open interest and transaction volume for options traded on the platform.

Our sampled BTC price data spans from 2015-12-31 to 2023-10-04 with the sample of BTC opening prices at 9 am UTC. As for the BTC options data, our collection starts from 2019-05-30 to 2023-10-04. The options data consists of 9 am UTC snapshots of the bid and ask IVs of call and put options. We chose to capture these snapshots at 9 am UTC to minimise the impact of market fluctuations that often occur due to the introduction of new options and futures listings at 8 am UTC.

We split the data into two datasets based on the availability of one-month option data. The first dataset is data observed from 2015-12-31 to 2019-05-29, where 2019-05-30 is the earliest date when 1-month options became available on Deribit. The second dataset is data observed from 2019-05-30 onward.

We design the empirical study as follows.
Initially, we use BTC price data from the first dataset for the estimation of model parameters that are associated with jumps, as described in Section [3](https://arxiv.org/html/2510.21297v1#S3 "3 Two stage approach calibration of the model ‣ Jump risk premia in the presence of clustered jumps").
In this stage, we apply POT estimation to filter out arrival times and magnitudes of positive and negative jumps in the BTC price in the testing data.
In this empirical study, the training data are the daily BTC price observed from 2015-12-31 to 2019-05-29.
From the time series of BTC price, we compute the jump intensities for the training data, and then generalise the computation of intensities to the testing data based on the estimated model parameters.
The model parameters are held fixed to infer jumps intensities to enforce no look-ahead bias in our empirical results.

Once a set of model parameters is estimated and the time series of jump intensity rates are inferred, we calibrate model volatility σ\sigma, and risk-premium parameters χ+\chi^{+} and χ−\chi^{-} using options data in the second dataset.
Options data include mid quotes of implied volatilities of call and put options, specifically options with maturities that are closest to, but less than one month, and have a moneyness range between 0.8 and 1.2. These options are characterised by high open interest and high transaction volume.

The final step involves the analysis of the jump risk premia computed using Eqs [44](https://arxiv.org/html/2510.21297v1#S4.E44 "In Corollary 4 (Using Proposition 5). ‣ 4 Positive and negative jump risk premia ‣ Jump risk premia in the presence of clustered jumps") and [45](https://arxiv.org/html/2510.21297v1#S4.E45 "In Corollary 4 (Using Proposition 5). ‣ 4 Positive and negative jump risk premia ‣ Jump risk premia in the presence of clustered jumps"). Section [5.3](https://arxiv.org/html/2510.21297v1#S5.SS3 "5.3 Evolution of jump risk premia ‣ 5 Empirical Results ‣ Jump risk premia in the presence of clustered jumps") presents the evolution of jump risk premia together with the main events in the BTC market using equations. Section [5.4](https://arxiv.org/html/2510.21297v1#S5.SS4 "5.4 Jump risk premia as factors in explaining BTC futures cost-of-carry ‣ 5 Empirical Results ‣ Jump risk premia in the presence of clustered jumps") reports the relationship between the jump risk premia and the cost-of-carry of BTC futures. Section [5.5](https://arxiv.org/html/2510.21297v1#S5.SS5 "5.5 Jump risk premia realisation ‣ 5 Empirical Results ‣ Jump risk premia in the presence of clustered jumps") shows application of the jump risk premia to profit and loss of delta-hedged option strategies.

### 5.2 Goodness-of-fit

We visually assess the goodness of fit of our model to the BTC price dynamics through Q-Q plots of the inter-arrival times of unit rate Poisson processes versus the transformed inter-arrival times of observed BTC price jumps,
∫T[k−1]+T[k]+λs+​d​s\int\_{T^{+}\_{[k-1]}}^{T^{+}\_{[k]}}\lambda^{+}\_{s}\text{d}s for k=1,2,…,N(1)k=1,2,...,N^{(1)} and ∫T[k−1]−T[k]−λs−​d​s\int\_{T^{-}\_{[k-1]}}^{T^{-}\_{[k]}}\lambda^{-}\_{s}\text{d}s for k=1,2,…,N(2)k=1,2,...,N^{(2)}, where N(1)N^{(1)} and N(2)N^{(2)} are the numbers of positive and negative jumps observed until time TT.
Appendix [B](https://arxiv.org/html/2510.21297v1#A2 "Appendix B Goodness of fit assessment by Q-Q plot ‣ Jump risk premia in the presence of clustered jumps") provides further details of this approach.

Figure [5](https://arxiv.org/html/2510.21297v1#S5.F5 "Figure 5 ‣ 5.2 Goodness-of-fit ‣ 5 Empirical Results ‣ Jump risk premia in the presence of clustered jumps") presents the Q-Q plot of the model estimates. Model parameters are estimated from 2015-12-31 to 2019-05-29, as mentioned above. These estimates are applied to transform the jumps arrival times of the whole dataset from 2015-12-31 to 2023-10-04. In the Q-Q plots, data points from the first dataset are marked by circles, data points from the testing data are marked by crosses. The model estimates fit reasonably well for most of the negative jumps inter-arrival times.

Figure 5: 
The left panel shows the Q–Q plot of compensator-transformed interarrival times for positive jumps; the right panel shows the same for negative jumps. Crosses and circles represent jumps occurring before (in-sample) and after (out-of-sample) 2019-05-30, respectively. Under the model, the transformed interarrival times should follow a standard exponential distribution. The model is calibrated on data before 2019-05-30, and the estimated parameters are used to infer intensities for periods after 2019-05-30. The close agreement between theoretical and empirical quantiles indicates strong in- and out-of-sample performance.
[![Refer to caption](qletlogo_tr.png)goodness\_of\_fit\_P](https://github.com/QuantLet/HJP/tree/main/codes/jupyterNotebooks/goodness_of_fit_P)

![Refer to caption](x5.png)

### 5.3 Evolution of jump risk premia

The dynamics of jump risk premia, computed using Equations ([44](https://arxiv.org/html/2510.21297v1#S4.E44 "In Corollary 4 (Using Proposition 5). ‣ 4 Positive and negative jump risk premia ‣ Jump risk premia in the presence of clustered jumps")) and ([45](https://arxiv.org/html/2510.21297v1#S4.E45 "In Corollary 4 (Using Proposition 5). ‣ 4 Positive and negative jump risk premia ‣ Jump risk premia in the presence of clustered jumps")), from 2019-05-30 to 2023-10-04 are illustrated in Figure [6](https://arxiv.org/html/2510.21297v1#S5.F6 "Figure 6 ‣ 5.3 Evolution of jump risk premia ‣ 5 Empirical Results ‣ Jump risk premia in the presence of clustered jumps").
Overall, the jump risk premia vary strongly over time, while showing a tendency to mean-revert to a mean close to zero. In addition,
the negative jump risk premium fluctuates in the same direction as the positive jump risk premium, but with a stronger magnitude. This co-movement suggests the time-varying skewness observed in option prices. When jump premia are negative and put options have a higher demand than call options, the implied volatility skew becomes left-skewed compared to the skew inferred by the statistical measure, and vice versa.

Although Bollerslev and
Todorov ([2011](https://arxiv.org/html/2510.21297v1#bib.bib11))’s data and methodology differ significantly from ours, their findings are in line with our results. Using high-frequency data and a model-free approach to decompose volatility into continuous and jump components, they found that investors demand a significantly higher premium for downside jump risk than for upside jump risk. This asymmetry supports our observation that negative jump risk premia tend to have a greater magnitude than positive premia. When pricing longer-dated options, the extremely high jump risk premia are not expected to last very long due to the mean reversion of jump intensities.

A significant peak in premia was observed on 2021-01-16, building on the increase that started in early October 2020, a period marked by heightened institutional activity and a series of all-time high break-outs for BTC price.
The troughs and the market situations during the time include the following (i) 2020-03-22: COVID-19 outbreak starting in March 2020; (ii) 2021-05-27: environmental concerns over Bitcoin mining; (iii) 2022-06-20: 40%40\% decline in BTC caused by hawkins interest rate policy of the U.S. Federal Reserve amid high inflation rates; (iv) 2022-11-15: the FTX crisis and subsequent crash of cryptocurrencies.

Figure 6: 
The time series plots illustrate the positive and negative jump risk premia, depicted by light blue and light orange lines, respectively.
The darker lines in the plots represent the seven-day moving averages of the corresponding jump risk premia.
These moving averages reveal a more distinct pattern in the evolution of the jump risk premia.
The jump risk premia are estimated from 2019-05-30 to 2023-10-04.
[![Refer to caption](qletlogo_tr.png)jumps\_premia\_evolution](https://github.com/QuantLet/HJP/tree/main/codes/jupyterNotebooks/jumps_premia_evolution)

![Refer to caption](x6.png)

### 5.4 Jump risk premia as factors in explaining BTC futures cost-of-carry

BTC futures are a popular choice for investors seeking leveraged exposures to BTC dynamics. Here, we investigate whether jump risk premia can serve as explanatory factors for BTC futures pricing, specifically through their relationship with the cost-of-carry.
The variable of interest is the BTC basis or cost-of-carry specified as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ct=ln⁡(Ft​(τ)/St)/τ,\displaystyle c\_{t}=\ln\big(F\_{t}(\tau)/S\_{t}\big)/\tau, |  | (46) |

where Ft​(τ)F\_{t}(\tau) is the price at time tt of a futures contract with
time-to-maturity τ\tau, and StS\_{t} is the spot price of BTC.
Figure [7](https://arxiv.org/html/2510.21297v1#S5.F7 "Figure 7 ‣ 5.4 Jump risk premia as factors in explaining BTC futures cost-of-carry ‣ 5 Empirical Results ‣ Jump risk premia in the presence of clustered jumps") shows the basis ctc\_{t}, computed using the prevailing futures contract with a time-to-maturity just below one month, based on data from Deribit.
The cost-of-carry is annualized and exhibits high volatility, ranging from −20%-20\% to 80%80\%. High values of the cost-of-carry arise when investors seek leverage. A trader can monetise a high value of the cost-of-carry by selling short the futures and going long BTC through a spot market.

Figure 7: 
The time series plot shows the BTC futures basis ctc\_{t} observed in the market.
The data is calculated using the price of the future with maturity τ\tau less than, but closest to one month.
[![Refer to caption](qletlogo_tr.png)cost\_of\_carry\_factors](https://github.com/QuantLet/HJP/tree/main/codes/jupyterNotebooks/cost_of_carry_factors)

![Refer to caption](x7.png)

In addition to the jump risk premia, the number of positive and negative jumps in the previous week,
abbreviated respectively as Nt(1)−Nt−7(1)N^{(1)}\_{t}-N^{(1)}\_{t-7} and Nt(2)−Nt−7(2)N^{(2)}\_{t}-N^{(2)}\_{t-7}, and the average funding rate of the week from Deribit BTC perpetual futures, abbreviated by rt,t−7fundingr^{\text{funding}}\_{t,t-7}, are included as independent variables in order to support the analysis.
The regression of interest is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Δ​ct\displaystyle\Delta c\_{t} | =β1​Δ​γt++β2​Δ​γt−+β3​Δ​(Nt(1)−Nt−7(1))+β4​Δ​(Nt(2)−Nt−7(2))+β5​Δ​rt,t−7funding+Δ​εt.\displaystyle=\beta\_{1}\Delta\gamma^{+}\_{t}+\beta\_{2}\Delta\gamma^{-}\_{t}+\beta\_{3}\Delta\big(N^{(1)}\_{t}-N^{(1)}\_{t-7}\big)+\beta\_{4}\Delta\big(N^{(2)}\_{t}-N^{(2)}\_{t-7}\big)+\beta\_{5}\ \Delta r^{\text{funding}}\_{t,t-7}+\Delta\varepsilon\_{t}. |  | (47) |

All variables are differenced to remove potential fixed effects and to mitigate the impact of any fixed effects.
To mitigate the noise arising from daily fluctuations and the introduction of new contracts, the data selected for the regression analysis consist of market snapshots captured every Friday at 9 am UTC.
This timing is chosen because traders typically adjust their positions on Fridays to manage risk for the upcoming weekend.
Additionally, newly issued options and futures contracts typically begin trading at 8 am, allowing the 9 am UTC snapshot to incorporate the initial market responses of these new instruments.
The variables are observed every Friday at 9 am UTC from 2019-06-14 to 2023-02-17.
Table [1](https://arxiv.org/html/2510.21297v1#S5.T1 "Table 1 ‣ 5.4 Jump risk premia as factors in explaining BTC futures cost-of-carry ‣ 5 Empirical Results ‣ Jump risk premia in the presence of clustered jumps") reports the estimated coefficients, Newey-West robustified tt-statistics, and adjusted R2R^{2} coefficients of regressions of ctc\_{t} on combinations of explanatory variables.

Table 1: 
The table reports estimated coefficients, Newey-West robustified tt-statistics,
and adjusted R2R^{2} coefficients of regressions of the futures basis ct=ln⁡(Ft​(τ)/St)/τc\_{t}=\ln(F\_{t}(\tau)/S\_{t})/\tau.
The futures contract with time-to-maturity τ\tau smaller than, but closest to one month is chosen for each observation time to represent the futures market.
The regressors are defined as follows: γt+\gamma^{+}\_{t} and γt−\gamma^{-}\_{t} are the jump risk premium.
Nt(1)−Nt−7(1)N^{(1)}\_{t}-N^{(1)}\_{t-7} and Nt(2)−Nt−7(2)N^{(2)}\_{t}-N^{(2)}\_{t-7} are number of positive and negative jumps in the week prior to tt, respectively.
rt,t−7fundingr^{\text{funding}}\_{t,t-7} is the average funding rate of the week from Deribit BTC perpetual futures.
The Deribit BTC funding rate is chosen to represent the convenience yield in the crypto market.
All variables enter as first differences.
∗, ∗∗, and ∗∗∗ indicate statistical significance at the 10%, 5%, and 1% levels, respectively.
The variables are observed every Friday at 9 am UTC from 2019-06-14 to 2023-02-17.
[![[Uncaptioned image]](qletlogo_tr.png)cost\_of\_carry\_factors](https://github.com/QuantLet/HJP/tree/main/codes/jupyterNotebooks/cost_of_carry_factors)

|  | II | I​III | I​I​IIII | I​VIV | VV | V​IVI |
| --- | --- | --- | --- | --- | --- | --- |
| γt+\gamma^{+}\_{t} | 0.01570.0157\*\*\* |  |  | 0.01600.0160\*\*\* | 0.00710.0071 | 0.00750.0075\* |
|  | (2.6139)(2.6139) |  |  | (3.5339)(3.5339) | (1.2400)(1.2400) | (1.7027)(1.7027) |
| γt−\gamma^{-}\_{t} | 0.01320.0132\*\* |  |  | 0.00890.0089 | 0.01310.0131\*\* | 0.00970.0097\* |
|  | (2.2257)(2.2257) |  |  | (1.4316)(1.4316) | (2.5760)(2.5760) | (1.7995)(1.7995) |
| Nt(1)−Nt−7(1)N^{(1)}\_{t}-N^{(1)}\_{t-7} |  | 0.01020.0102\*\* |  | 0.01120.0112\*\*\* |  | 0.00730.0073\* |
|  |  | (2.1840)(2.1840) |  | (3.0709)(3.0709) |  | (1.8356)(1.8356) |
| Nt(2)−Nt−7(2)N^{(2)}\_{t}-N^{(2)}\_{t-7} |  | −0.0179-0.0179\*\*\* |  | −0.0126-0.0126\*\* |  | −0.0114-0.0114\*\* |
|  |  | (−2.8429)(-2.8429) |  | (−2.4792)(-2.4792) |  | (−2.2707)(-2.2707) |
| rt,t−7fundingr^{\text{funding}}\_{t,t-7} |  |  | 0.00240.0024\*\*\* |  | 0.00200.0020\*\*\* | 0.00180.0018\*\*\* |
|  |  |  | (4.6951)(4.6951) |  | (3.8976)(3.8976) | (3.7371)(3.7371) |
| Adj. R2R^{2} | 0.14670.1467 | 0.08660.0866 | 0.22310.2231 | 0.19560.1956 | 0.27940.2794 | 0.31070.3107 |

The results of the regression analysis reveal a significant explanatory power of jump risk premia in determining the volatile cost-of-carry for BTC futures.
In Regression I, the coefficients for jump risk premia are both positive and statistically significant.
This model yields an adjusted R2R^{2} of 14.7%, together with the significant coefficients, supporting the hypothesis that futures prices are directly proportional to the jump risk premia.

The jump risk premia explanatory power is robust against the presence of the number of jumps and the funding rate variables.
This conclusion is drawn by comparing the adjusted R2R^{2} values and coefficients from Regression I with those from Regressions IV and V.
Combining the results of Regression I with that of Regression IV side by side, which includes the number of jumps from the previous week, the coefficient of the positive jump risk premium remains significant.
Inclusion of these variables improves the adjusted R2R^{2} to 19.6%.
However, the coefficient of the negative jump risk premium decreases in magnitude and becomes statistically insignificant in this context.
A similar pattern is noted in Regression V.
When the funding rate is included in the Regression V, the coefficient of negative jump risk premium slightly diminishes while remaining significant, but
the coefficient of positive jump risk premium halves and becomes statistically insignificant.
The inclusion of the average funding rate improves the adjusted R2R^{2} to 28%.
These improvements value of R2R^{2} confirm that the number of jumps and the average funding rate provide additional information to explain the level of BTC futures cost-of-carry in addition to the jump risk premia.
However, the shrinkage of the magnitudes and loss in statistical significance observed from the coefficients are probably due to the correlation between the variables.
Empirically, the correlation between the positive jump risk premium and the funding rate is around 36.7%36.7\%; the correlation between the negative jump risk premium and the number of negative jumps is around −24%-24\%.

The interpretation of the correlations is as follows.
The positive correlation between the positive jump risk premium and the funding rate may be due to the increasing speculative demand for both call options and perpetual futures.
In contrast, the negative correlation between the negative jump risk premium and the number of negative jumps can result in higher put option prices during bearish periods with high volatility.
This interpretation is consistent with the findings of Schmeling
et al. ([2023](https://arxiv.org/html/2510.21297v1#bib.bib44)).
They attribute high cost-of-carry of BTC futures to the interaction between the trend-chasing behaviour of market traders and the scarcity of arbitrage capital that conducts cash-and-carry trade.

Regression VI offers a comprehensive overview of how jump risk premia affect BTC futures prices, taking into account all relevant variables.
This regression reaches an adjusted R2R^{2} value of 31%31\%, with each coefficient demonstrating statistical significance.
According to the regression result, a one-unit increase in the
positive jump risk premium is associated with a 0.75 basis point increase in the cost of carry of BTC futures ctc\_{t}.
Similarly, a one-unit increase in the negative jump risk premium corresponds to an increase of 0.97 basis points in ctc\_{t}.
The positive signs of both the positive and negative jump risk premia coefficients in Regression VI indicate that a positive change corresponds to (forward-looking) option and futures market being more optimistic than the price history suggests.
The different sizes of the positive and negative jump risk premia coefficients can be attributed to risk aversion, as traders and investors are more sensitive to losses than to gains.

### 5.5 Jump risk premia realisation

In the spirit of Carr and
Madan ([1998](https://arxiv.org/html/2510.21297v1#bib.bib14)) who quantifies the return variance risk premium on an asset using the market prices of options, we answer the question of how the risk premia can be realised. To this end, we investigate whether the jump risk premia defined in Equations ([44](https://arxiv.org/html/2510.21297v1#S4.E44 "In Corollary 4 (Using Proposition 5). ‣ 4 Positive and negative jump risk premia ‣ Jump risk premia in the presence of clustered jumps")) and ([45](https://arxiv.org/html/2510.21297v1#S4.E45 "In Corollary 4 (Using Proposition 5). ‣ 4 Positive and negative jump risk premia ‣ Jump risk premia in the presence of clustered jumps")) can explain the one-week-ahead returns of delta-hedged short-option strategies, following a similar empirical approach to Bakshi and
Kapadia ([2003](https://arxiv.org/html/2510.21297v1#bib.bib5)). The option strategies are constructed using the same data and approach as Lucic and
Sepp ([2024](https://arxiv.org/html/2510.21297v1#bib.bib39)), where short positions in calls, puts, straddles and strangles are delta-hedged using Black-Scholes (BS) deltas and rebalanced hourly until expiration.

All strategies are written on options expiring on the subsequent Friday at 8am UTC.
As both positive and negative jump risk premia are observed, we define simple trading signals as follows: A positive risk premium for positive jumps, which means that the market prices call options higher than implied by the historical measure, is considered an opportunity to sell call options and call spreads.
The trading decision is similar for put options and put spreads when observing a negative risk premium on negative jumps.
For portfolios involving straddle and strangles, which are combinations of call and put options, the trading strategy is to sell them if at least one of the risk premia is “active” in the sense described previously.
The trading signals for all strategies are determined on each Friday at 9am UTC, and if active, the position is created (and delta-hedged with hourly rebalancing) until expiry the following Friday.222Long positions in calls and puts are not entered if the jump risk premia are “reversed” due to the loss in time value of the options (negative theta).

Using Bakshi and
Kapadia ([2003](https://arxiv.org/html/2510.21297v1#bib.bib5))’s empirical methodology, we investigate the relationship between jump risk premia as defined above and one-week-ahead returns of the option strategy portfolios.
This is achieved by conducting a regression against the jump risk premia of the one-week-ahead log returns rt=ln⁡(Pt/Pt−1)r\_{t}=\ln(P\_{t}/P\_{t-1}) of each strategy, with PtP\_{t} the option strategy value at time tt.
The regression of interest is

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt+1=β0+β1​γt++β2​γt−+β3​Δ​γt++β4​Δ​γt−+β5​(Nt(1)−Nt−1(1))+β6​(Nt(2)−Nt−1(2)),r\_{t+1}=\beta\_{0}+\beta\_{1}\gamma^{+}\_{t}+\beta\_{2}\gamma^{-}\_{t}+\beta\_{3}\Delta\gamma^{+}\_{t}+\beta\_{4}\Delta\gamma^{-}\_{t}+\beta\_{5}(N^{(1)}\_{t}-N^{(1)}\_{t-1})+\beta\_{6}(N^{(2)}\_{t}-N^{(2)}\_{t-1}), |  | (48) |

where rt+1r\_{t+1} is the one-week-ahead options strategy return at time tt (expressed in basis points),
Δ\Delta is the first difference operator and
(Nt(1)−Nt−1(1))(N^{(1)}\_{t}-N^{(1)}\_{t-1}) and (Nt(2)−Nt−1(2))(N^{(2)}\_{t}-N^{(2)}\_{t-1}) count the number of jumps that occured within the previous week.
The option strategies of interest are delta-hedged short-option strategies of different moneyness, as follows:

1. (i)

   ATM: calls and puts with at-the-money strikes;
2. (ii)

   10D: options with delta of +0.1 for calls and -0.1 for puts;
3. (iii)

   25D: options with delta of +0.25 for calls and -0.25 for puts;
4. (iv)

   25D spread: one unit of call with delta of +0.5 (-0.5 for put) and short two units of call with +0.25 delta (-0.25 delta for put);
5. (v)

   ATM straddle: one unit of call and put each with ATM strikes;
6. (vi)

   25D strangle: one unit of call with delta +0.25 and one unit of put with delta of -0.25;
7. (vii)

   10D strangle: one unit of call with delta +0.1 and one unit of put with delta of -0.1.

Table 2: 
Regression results of one-week ahead portfolio returns (in bps) regressed on jump risk premia and jump realisations, cf. Eq.([48](https://arxiv.org/html/2510.21297v1#S5.E48 "In 5.5 Jump risk premia realisation ‣ 5 Empirical Results ‣ Jump risk premia in the presence of clustered jumps")), heteroskedasticity-robust tt-statistics in parentheses. ∗\*, ∗⁣∗\*\*, ∗⁣∗⁣∗\*\*\* indicate statistical significance at the 10%, 5% and 1% levels, respectively. Sample period: 2019-05-31 to 2023-09-29 (277 observations).

|  | straddle | 10d strangle | 25d strangle | call spread | put spread |
| --- | --- | --- | --- | --- | --- |
| const | −1.985-1.985 | −0.898-0.898 | 3.8273.827 | 7.1947.194 | −2.822-2.822 |
|  | (−0.113)(-0.113) | (−0.106)(-0.106) | (0.31)(0.31) | (0.854)(0.854) | (−0.388)(-0.388) |
| γt+\gamma^{+}\_{t} | 22.65222.652 | 23.889∗⁣∗\*\* | 26.5926.59 | 24.41∗⁣∗\*\* | 0.3090.309 |
|  | (0.968)(0.968) | (2.15)(2.15) | (1.535)(1.535) | (2.254)(2.254) | (0.027)(0.027) |
| γt−\gamma^{-}\_{t} | -53.874∗⁣∗\*\* | -33.475∗⁣∗\*\* | -42.253∗⁣∗\*\* | −15.31-15.31 | −7.908-7.908 |
|  | (−2.13)(-2.13) | (−2.541)(-2.541) | (−2.36)(-2.36) | (−1.25)(-1.25) | (−0.662)(-0.662) |
| Δ​γt+\Delta\gamma^{+}\_{t} | 1.6461.646 | -27.876∗\* | −23.075-23.075 | -28.187∗⁣∗\*\* | -12.458∗\* |
|  | (0.093)(0.093) | (−1.787)(-1.787) | (−1.458)(-1.458) | (−2.059)(-2.059) | (−1.784)(-1.784) |
| Δ​γt−\Delta\gamma^{-}\_{t} | 5.8725.872 | 35.705∗\* | 19.9719.97 | 18.34818.348 | 3.8533.853 |
|  | (0.277)(0.277) | (1.911)(1.911) | (1.133)(1.133) | (1.066)(1.066) | (0.253)(0.253) |
| Nt(1)−Nt−1(1)N^{(1)}\_{t}-N^{(1)}\_{t-1} | 8.7288.728 | 3.2493.249 | −0.518-0.518 | −3.749-3.749 | 3.2113.211 |
|  | (0.382)(0.382) | (0.325)(0.325) | (−0.031)(-0.031) | (−0.47)(-0.47) | (0.284)(0.284) |
| Nt(2)−Nt−1(2)N^{(2)}\_{t}-N^{(2)}\_{t-1} | 41.155∗\* | 7.1347.134 | 19.11819.118 | 1.5321.532 | −1.201-1.201 |
|  | (1.733)(1.733) | (0.632)(0.632) | (1.055)(1.055) | (0.299)(0.299) | (−0.122)(-0.122) |
| Adj. R2 | 0.0490.049 | 0.0450.045 | 0.030.03 | 0.0440.044 | −0.002-0.002 |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | atm call | 10d call | 25d call | atm put | 10d put | 25d put |
| const | 3.0383.038 | 0.750.75 | 4.1824.182 | 2.2222.222 | 0.7840.784 | 1.4591.459 |
|  | (0.46)(0.46) | (0.148)(0.148) | (0.769)(0.769) | (0.342)(0.342) | (0.199)(0.199) | (0.257)(0.257) |
| γt+\gamma^{+}\_{t} | 19.367∗⁣∗\*\* | 20.446∗⁣∗⁣∗\*\!\*\!\* | 22.365∗⁣∗⁣∗\*\!\*\!\* | 2.9312.931 | 2.5242.524 | 3.9923.992 |
|  | (2.234)(2.234) | (3.049)(3.049) | (3.024)(3.024) | (0.324)(0.324) | (0.461)(0.461) | (0.491)(0.491) |
| γt−\gamma^{-}\_{t} | −11.39-11.39 | -15.932∗\* | -14.445∗\* | -22.474∗⁣∗\*\* | -11.587∗⁣∗\*\* | -16.64∗\* |
|  | (−1.277)(-1.277) | (−1.744)(-1.744) | (−1.78)(-1.78) | (−2.074)(-2.074) | (−2.23)(-2.23) | (−1.793)(-1.793) |
| Δ​γt+\Delta\gamma^{+}\_{t} | −7.976-7.976 | -22.573∗\* | -19.624∗⁣∗\*\* | −1.039-1.039 | -7.417∗⁣∗\*\* | -8.926∗\* |
|  | (−1.238)(-1.238) | (−1.79)(-1.79) | (−2.267)(-2.267) | (−0.13)(-0.13) | (−2.035)(-2.035) | (−1.735)(-1.735) |
| Δ​γt−\Delta\gamma^{-}\_{t} | 10.59410.594 | 22.22222.222 | 15.60715.607 | −0.67-0.67 | 7.178∗⁣∗\*\* | 3.1873.187 |
|  | (1.513)(1.513) | (1.515)(1.515) | (1.53)(1.53) | (−0.071)(-0.071) | (2.244)(2.244) | (0.512)(0.512) |
| Nt(1)−Nt−1(1)N^{(1)}\_{t}-N^{(1)}\_{t-1} | −11.773-11.773 | −1.281-1.281 | -7.385∗\* | 11.50811.508 | 7.74∗⁣∗\*\* | 6.156.15 |
|  | (−1.605)(-1.605) | (−0.532)(-0.532) | (−1.652)(-1.652) | (1.272)(1.272) | (2.047)(2.047) | (0.958)(0.958) |
| Nt(2)−Nt−1(2)N^{(2)}\_{t}-N^{(2)}\_{t-1} | 14.153∗\* | 3.6823.682 | 7.4967.496 | 5.9045.904 | −1.132-1.132 | 2.7452.745 |
|  | (1.714)(1.714) | (1.385)(1.385) | (1.53)(1.53) | (0.733)(0.733) | (−0.221)(-0.221) | (0.406)(0.406) |
| Adj. R2 | 0.0410.041 | 0.0970.097 | 0.0710.071 | 0.0480.048 | 0.0290.029 | 0.0390.039 |

Table [2](https://arxiv.org/html/2510.21297v1#S5.T2 "Table 2 ‣ 5.5 Jump risk premia realisation ‣ 5 Empirical Results ‣ Jump risk premia in the presence of clustered jumps") shows the results of the regression on one-week-ahead returns (in basis points), with robust (HAC) tt-statistics in parentheses. The number of positive and negative jumps counted during the week are included as control variables. Recalling that a negative jump risk premium on downward jumps indicates high option prices relative to the statistical history (cf. Figure [3](https://arxiv.org/html/2510.21297v1#S4.F3 "Figure 3 ‣ 4 Positive and negative jump risk premia ‣ Jump risk premia in the presence of clustered jumps"), the mixed strategies (straddle, strangles) earn jump risk premia from downward jumps. The 10-delta strangle also earns risk premia from upward jumps as well as changes in jump risk premia. Here, a negative first difference in the upward jump risk premium indicates that the jump risk premium decreased over the course of the previous week, i.e., pricing of jump risk of out-of-the-money call options aligns better with historical jump risk. The negative coefficient persists when replacing Δ​γt+\Delta\gamma^{+}\_{t} with the residuals of Δ​γt+\Delta\gamma\_{t}^{+} regressed on γt+\gamma\_{t}^{+}, which rules out multicollinearity effects (likewise for Δ​γt−\Delta\gamma\_{t}^{-} and γt−\gamma\_{t}^{-}). Hence, Δ​γt+\Delta\gamma\_{t}^{+} and Δ​γt−\Delta\gamma\_{t}^{-}, when statistically significant, carry independent predictive performance driving the P&L. A plausible interpretation of the negative coefficient associated with Δ​γt+\Delta\gamma\_{t}^{+} is that this points to a calming market (expecting less right-tail events), which in turn makes the delta-hedge more robust and allows to earn the time-decay θ\theta inherent in the option positions. The argument is similar for Δ​γt−\Delta\gamma\_{t}^{-} and the positive coefficient.

Overall, on average the short call option strategies earn the positive jump risk premium of upward jumps and the short put option strategies earn the negative jump risk premium of downward jumps. One has to bear in mind, though, that many other factors influence the weekly returns as the adjusted R2R^{2} measures are fairly low for all strategies.

The relative pricing interpretation also aligns with the analysis done by Bakshi and
Kapadia ([2003](https://arxiv.org/html/2510.21297v1#bib.bib5)).
They demonstrate in Eq.(24) of their study that, theoretically, a more pronounced left tail in the underlying price distribution under the risk-neutral measure, as opposed to the “real” measure, enhances the performance of delta-hedged portfolios333Bakshi and
Kapadia ([2003](https://arxiv.org/html/2510.21297v1#bib.bib5)) approach the construction of delta-hedged portfolios from a direction opposite to ours. While they engage in strategies that involve buying options and selling the underlying assets, we adopt the reverse strategy, selling options and buying the underlying..

## 6 Conclusion

The cryptocurrency market provides a challenging venue for exploring jump risk premia due to its high volatility and sentiment-driven price dynamics. The dynamics of implied volatilities of cryptocurrency options exhibit varying skewness preferences. During bullish periods, the demand for call options increases and the implied skew becomes positive along with high carry costs for perpetual futures. During bearish periods, the demand for puts rises and the implied skew turns negative along with low or negative carry costs for perpetual futures. A similar regime-conditional behaviour of implied skew is present in options on the so-called “meme” stocks, which are characterised by high volumes in options driven by retail investors.

For modeling of regime-conditional implied volatility skew under the risk-neutral measure and skeweness of returns under the statistical measure, we have introduced a pricing model using Hawkes processes that incorporates the clustering of positive and negative jumps. We have further included two risk-premium parameters to model specification for modeling of regime-conditional risk-preferences. Here, one parameter is for the external specification of risk-premium for positive jumps, and one parameter is for risk-premium of negative jumps. Both parameters are inferred from the option prices observed on a given date.

For empirical investigation using our model, we have used options on Bitcoin (BTC). We have developed a sequential estimation procedure by first estimating model parameters under the statistical ℙ\mathbb{P} measure and then by inferring two risk-premium parameters from options data under the risk-neutral ℚ\mathbb{Q} measure. We have defined risk premia for positive and negative jumps as the difference between expected jumps under the risk-neutral and statistical probability measures, respectively. The implications of the jump risk premia estimated using our model are threefold.

First, the estimated jump-risk premia demonstrate preferences for skewness risk observed in implied volatilities. Specifically for BTC markets, the risk premium of positive jumps exceeded that of negative jumps on several occasions during a few strong bullish periods in BTC. In contrast, the risk premium of negative jumps dominated during bearish periods in BTC. A strong premium for positive jumps indicates that market participants significantly overpay for expected upside during bull periods by buying call options. Vice versa, a significant premium of negative jumps is associated with increased demand for put options during bear periods.

Second, jump risk premia have some explanatory power (with R2R^{2} of 15%15\%) to predict the dynamics of the cost-of-carry inferred from BTC futures.
A regression model with the recent number of jumps and BTC perpetual funding rates as control variables yields an R2R^{2} of 31%31\%, with all coefficients being significant. The findings point to interdependencies between the BTC spot, options, and futures markets.

Third, we show that jump risk premia have explanatory power for one-week-ahead profit-and-loss (P&L) of delta-hedged option strategies and portfolios. Simple decision strategies to sell short call options if the risk premium for upward jumps is positive, to sell put option if the risk premium for downward jumps is negative, or to sell straddles if either of the jump risk premia is active, can – on average – earn the respective risk premium. In all cases, the options are hedged with hourly rebalancing.

Finally, we note that the regime-conditional behaviour of the implied option skew is also characteristic of the so-called “meme” stocks, which exhibit positive and negative implied volatility skews dependent on market conditions.
In addition, the G-7 currencies tend to exhibit a variation in the sign of implied skew dependent on macro conditions.
As a result, our framework can also be applied for analysis of the implied volatility dynamics of “meme” stocks and the G-7 currencies, which we leave for future research.
In addition, we assume that the risk-premium parameters are constant for the specification of model dynamics.
We leave an extension for time-varying dynamics of model risk-premium parameters as another potential research topic.

## References

* Alexander and
  Imeraj (2021)

  Alexander, C. and A. Imeraj (2021): “The Bitcoin VIX and
  its variance risk premium,” *The Journal of Alternative Investments*,
  23, 84–109.
* Alexander and
  Imeraj (2023)

  ——— (2023): “Delta hedging bitcoin
  options with a smile,” *Quantitative Finance*, 23, 799–817.
* Almeida
  et al. (2024)

  Almeida, C., M. Grith, R. Miftachov, and Z. Wang (2024): “Risk
  Premia in the Bitcoin Market,” arXiv preprint arXiv:2410.15195.
* Bacry
  et al. (2015)

  Bacry, E., I. Mastromatteo, and J.-F. Muzy (2015): “Hawkes
  Processes in Finance,” *Market Microstructure and Liquidity*, 01.
* Bakshi and
  Kapadia (2003)

  Bakshi, G. and N. Kapadia (2003): “Delta-hedged gains and the
  negative market volatility risk premium,” *The Review of Financial
  Studies*, 16, 527–566.
* Bakshi
  et al. (2003)

  Bakshi, G., N. Kapadia, and D. Madan (2003): “Stock return
  characteristics, skew laws, and the differential pricing of individual equity
  options,” *The Review of Financial Studies*, 16, 101–143.
* Bali
  et al. (2011)

  Bali, T. G., N. Cakici, and R. F. Whitelaw (2011): “Maxing
  out: Stocks as lotteries and the cross-section of expected returns,”
  *Journal of financial economics*, 99, 427–446.
* Bates (1996)

  Bates, D. S. (1996): “Jumps and stochastic volatility:
  Exchange rate processes implicit in deutsche mark options,” *The Review
  of Financial Studies*, 9, 69–107.
* Bates (2000)

  ——— (2000): “Post-’87 crash fears in
  the S&P 500 futures option market,” *Journal of Econometrics*, 94,
  181–238.
* Bollerslev
  et al. (2009)

  Bollerslev, T., G. Tauchen, and H. Zhou (2009): “Expected
  stock returns and variance risk premia,” *The Review of Financial
  Studies*, 22, 4463–4492.
* Bollerslev and
  Todorov (2011)

  Bollerslev, T. and V. Todorov (2011): “Tails, fears, and risk
  premia,” *The Journal of Finance*, 66, 2165–2211.
* Broadie
  et al. (2007)

  Broadie, M., M. Chernov, and M. Johannes (2007): “Model
  specification and risk premia: Evidence from futures options,” *The
  Journal of Finance*, 62, 1453–1490.
* Brown and
  Nair (1988)

  Brown, T. C. and M. G. Nair (1988): “A simple proof of the
  multivariate random time change theorem for point processes,” *Journal
  of Applied Probability*, 25, 210–214.
* Carr and
  Madan (1998)

  Carr, P. and D. Madan (1998): “Towards a theory of volatility
  trading,” *Volatility: New estimation techniques for pricing
  derivatives*, 29, 417–427.
* Carr and Wu (2009)

  Carr, P. and L. Wu (2009): “Variance risk premiums,” *The
  Review of Financial Studies*, 22, 1311–1341.
* Christoffersen et al. (2012)

  Christoffersen, P., K. Jacobs, and C. Ornthanalai (2012):
  “Dynamic jump intensities and risk premiums: Evidence from S&P500
  returns and options,” *Journal of Financial Economics*, 106, 447–472.
* Daley and
  Vere-Jones (2003)

  Daley, D. J. and D. Vere-Jones (2003): *An Introduction to the
  Theory of Point Processes: Volume I: Elementary Theory and Methods*,
  Springer.
* Dobrynskaya (2024)

  Dobrynskaya, V. (2024): “Is downside risk priced in
  cryptocurrency market?” *International Review of Financial Analysis*,
  91, 102947.
* Embrechts
  et al. (2011)

  Embrechts, P., T. Liniger, and L. Lin (2011): “Multivariate
  Hawkes processes: an application to financial data,” *Journal of Applied
  Probability*, 48, 367–378.
* Eraker (2004)

  Eraker, B. (2004): “Do stock prices and volatility jump?
  Reconciling evidence from spot and option prices,” *The Journal of
  finance*, 59, 1367–1403.
* Errais
  et al. (2010)

  Errais, E., K. Giesecke, and L. R. Goldberg (2010): “Affine
  point processes and portfolio credit risk,” *SIAM Journal on Financial
  Mathematics*, 1, 642–665.
* Gerber and
  Shiu (1995)

  Gerber, H. and E. Shiu (1995): “Option pricing by Esscher
  transforms.” *Insurance Mathematics and Economics*, 3, 287.
* Granelli and
  Veraart (2016)

  Granelli, A. and A. E. D. Veraart (2016): “Modeling the
  Variance Risk Premium of Equity Indices: The Role of Dependence and
  Contagion,” *SIAM Journal on Financial Mathematics*, 7, 382–417.
* Gupta and
  Pascale (2025)

  Gupta, A. and S. Pascale (2025): “Volatility Outlook 2025,”
  *Barclays Equity Research White Paper*.
* Hainaut (2016)

  Hainaut, D. (2016): “A bivariate Hawkes process for interest
  rate modeling,” *Economic Modelling*, 57, 180–196.
* Hainaut (2017)

  ——— (2017): “Clustered Lévy
  processes and their financial applications,” *Journal of Computational
  and Applied Mathematics*, 319, 117–140.
* Hainaut (2022)

  ——— (2022): *Continuous Time Processes
  for Finance*, Springer.
* Hainaut and
  Moraux (2018)

  Hainaut, D. and F. Moraux (2018): “Hedging of options in the
  presence of jump clustering,” *Journal of Computational Finance*, 22,
  1–35.
* Hawkes (1971)

  Hawkes, A. G. (1971): “Point spectra of some mutually exciting
  point processes,” *Journal of the Royal Statistical Society: Series B
  (Methodological)*, 33, 438–443.
* Hawkes (2018)

  ——— (2018): “Hawkes processes and
  their applications to finance: a review,” *Quantitative Finance*, 18,
  193–198.
* Hawkes and
  Oakes (1974)

  Hawkes, A. G. and D. Oakes (1974): “A cluster process
  representation of a self-exciting process,” *Journal of applied
  probability*, 11, 493–503.
* Jeanblanc
  et al. (2009)

  Jeanblanc, M., M. Yor, and M. Chesney (2009): *Mathematical
  Methods for Financial Markets*, Springer Science & Business Media.
* Klebaner (2005)

  Klebaner, F. C. (2005): *Introduction to Stochastic Calculus with
  Applications*, Imperial College Press, 2nd ed.
* Kumar (2009)

  Kumar, A. (2009): “Who gambles in the stock market?” *The
  journal of finance*, 64, 1889–1933.
* Laub
  et al. (2021)

  Laub, P. J., Y. Lee, and T. Taimre (2021): *The Elements of
  Hawkes Processes*, Springer.
* Lewis (2001)

  Lewis, A. L. (2001): “A simple option formula for general
  jump-diffusion and other exponential Lévy processes,” .
* Lipton (2002)

  Lipton, A. (2002): “The vol smile problem,” *Risk*, 15,
  61–66.
* Liu
  et al. (2023)

  Liu, F., N. Packham, M.-J. Lu, and W. K. Härdle (2023):
  “Hedging cryptos with Bitcoin futures,” *Quantitative Finance*,
  23, 819–841.
* Lucic and
  Sepp (2024)

  Lucic, V. and A. Sepp (2024): “Valuation and hedging of
  cryptocurrency inverse options,” *Quantitative Finance*, 24, 851–869.
* Matic
  et al. (2023)

  Matic, J. L., N. Packham, and W. K. Härdle (2023):
  “Hedging cryptocurrency options,” *Review of Derivatives
  Research*, 26, 91–133.
* Nguyen
  et al. (2019)

  Nguyen, D. B. B., M. Prokopczuk, and C. W. Simen (2019): “The
  risk premium of gold,” *Journal of International Money and Finance*, 94,
  140–159.
* Pan (2002)

  Pan, J. (2002): “The jump-risk premia implicit in options:
  Evidence from an integrated time-series study,” *Journal of Financial
  Economics*, 63, 3–50.
* Santa-Clara and
  Yan (2010)

  Santa-Clara, P. and S. Yan (2010): “Crashes, volatility, and
  the equity premium: Lessons from S&P 500 options,” *The Review of
  Economics and Statistics*, 92, 435–451.
* Schmeling
  et al. (2023)

  Schmeling, M., A. Schrimpf, and K. Todorov (2023): “Crypto
  carry,” Tech. rep., Bank for International Settlements.
* Sepp and
  Rakhmonov (2023)

  Sepp, A. and P. Rakhmonov (2023): “Log-normal Stochastic
  Volatility Model with Quadratic Drift,” *International Journal of
  Theoretical and Applied Finance*, 26, 1–63.
* Thaler and
  Ziemba (1988)

  Thaler, R. H. and W. T. Ziemba (1988): “Anomalies: Parimutuel
  betting markets: Racetracks and lotteries,” *Journal of Economic
  perspectives*, 2, 161–174.
* Watanabe (1964)

  Watanabe, S. (1964): “On discontinuous additive functionals
  and Lévy measures of a Markov process,” in *Japanese journal of
  mathematics: transactions and abstracts*, The Mathematical Society of Japan,
  vol. 34, 53–70.

## Appendix A Proofs

### A.1 Conditions for finite expected intensities

The expected values of intensities satisfy the following system of ODEs.
For s<ts<t,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝔼​(λt+|ℱs)d​t\displaystyle\frac{\text{d}{\mathbb{E}}(\lambda^{+}\_{t}|\mathcal{F}\_{s})}{\text{d}t} | =κ+​(θ+−𝔼​(λt+|ℱs))+β11​𝔼​(λt+|ℱs)​𝔼​J++β12​𝔼​(λt−|ℱs)​𝔼​J−,𝔼​(λs+|ℱs)=λs+\displaystyle=\kappa^{+}(\theta^{+}-{\mathbb{E}}(\lambda^{+}\_{t}|\mathcal{F}\_{s}))+\beta\_{11}{\mathbb{E}}(\lambda^{+}\_{t}|\mathcal{F}\_{s}){\mathbb{E}}J^{+}+\beta\_{12}{\mathbb{E}}(\lambda^{-}\_{t}|\mathcal{F}\_{s}){\mathbb{E}}J^{-},\ {\mathbb{E}}(\lambda^{+}\_{s}|\mathcal{F}\_{s})=\lambda^{+}\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝔼​(λt−|ℱs)d​t\displaystyle\frac{\text{d}{\mathbb{E}}(\lambda^{-}\_{t}|\mathcal{F}\_{s})}{\text{d}t} | =κ−​(θ−−𝔼​(λt−|ℱs))+β21​𝔼​(λt+|ℱs)​𝔼​J++β22​𝔼​(λt−|ℱs)​𝔼​J−,𝔼​(λs−|ℱs)=λs−.\displaystyle=\kappa^{-}(\theta^{-}-{\mathbb{E}}(\lambda^{-}\_{t}|\mathcal{F}\_{s}))+\beta\_{21}{\mathbb{E}}(\lambda^{+}\_{t}|\mathcal{F}\_{s}){\mathbb{E}}J^{+}+\beta\_{22}{\mathbb{E}}(\lambda^{-}\_{t}|\mathcal{F}\_{s}){\mathbb{E}}J^{-},\ {\mathbb{E}}(\lambda^{-}\_{s}|\mathcal{F}\_{s})=\lambda^{-}\_{s}. |  |

See Errais
et al. ([2010](https://arxiv.org/html/2510.21297v1#bib.bib21)) for proofs.
Write the above system of ODEs in matrix form:
For s<ts<t,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (d​𝔼​(λt+|ℱs)d​td​𝔼​(λt−|ℱs)d​t)=Φ​(𝔼​(λt+|ℱs)𝔼​(λt−|ℱs))+C,(𝔼​(λs+|ℱs)𝔼​(λs−|ℱs))=(λs+λs−)\displaystyle\begin{pmatrix}\frac{\text{d}{\mathbb{E}}(\lambda^{+}\_{t}|\mathcal{F}\_{s})}{\text{d}t}\\ \frac{\text{d}{\mathbb{E}}(\lambda^{-}\_{t}|\mathcal{F}\_{s})}{\text{d}t}\end{pmatrix}=\Phi\begin{pmatrix}{\mathbb{E}}(\lambda^{+}\_{t}|\mathcal{F}\_{s})\\ {\mathbb{E}}(\lambda^{-}\_{t}|\mathcal{F}\_{s})\end{pmatrix}+C,\ \begin{pmatrix}{\mathbb{E}}(\lambda^{+}\_{s}|\mathcal{F}\_{s})\\ {\mathbb{E}}(\lambda^{-}\_{s}|\mathcal{F}\_{s})\end{pmatrix}=\begin{pmatrix}\lambda^{+}\_{s}\\ \lambda^{-}\_{s}\end{pmatrix} |  | (49) |

where

|  |  |  |
| --- | --- | --- |
|  | Φ​=def​(−κ++β11​𝔼​J+β12​𝔼​J−β22​𝔼​J−−κ−+β21​𝔼​J+)​ and ​C​=def​(κ+​θ+κ−​θ−).\displaystyle\Phi\overset{\text{def}}{=}\begin{pmatrix}-\kappa^{+}+\beta\_{11}{\mathbb{E}}J^{+}&\beta\_{12}{\mathbb{E}}J^{-}\\ \beta\_{22}{\mathbb{E}}J^{-}&-\kappa^{-}+\beta\_{21}{\mathbb{E}}J^{+}\end{pmatrix}\text{ and }C\overset{\text{def}}{=}\begin{pmatrix}\kappa^{+}\theta^{+}\\ \kappa^{-}\theta^{-}\end{pmatrix}. |  |

If Φ\Phi is invertible, the solution to Eq.([49](https://arxiv.org/html/2510.21297v1#A1.E49 "In A.1 Conditions for finite expected intensities ‣ Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps")) is

|  |  |  |
| --- | --- | --- |
|  | (𝔼​(λs+|ℱs)𝔼​(λs−|ℱs))=expm​(Φ​t)​(λs+λs−)+Φ−1​(expm​(Φ​t)−I)​C,\displaystyle\begin{pmatrix}{\mathbb{E}}(\lambda^{+}\_{s}|\mathcal{F}\_{s})\\ {\mathbb{E}}(\lambda^{-}\_{s}|\mathcal{F}\_{s})\end{pmatrix}=\text{expm}(\Phi t)\begin{pmatrix}\lambda^{+}\_{s}\\ \lambda^{-}\_{s}\end{pmatrix}+\Phi^{-1}\left(\text{expm}(\Phi t)-I\right)C, |  |

where expm​()\text{expm}() is the matrix exponential,
Φ−1\Phi^{-1} is the matrix inverse of Φ\Phi, and II is a 2×22\times 2 identity matrix.
The matrix exponential can be computed via eigenvectors and eigenvalues.
Let S​Λ​S−1S\Lambda S^{-1} be the eigendecomposition of Φ\Phi,
where SS is the full matrix of eigenvectors and Λ=diag​(λ1,λ2)\Lambda=\text{diag}(\lambda\_{1},\ \lambda\_{2}) is the diagonal matrix of eigenvalues of Φ\Phi, λ1\lambda\_{1} and λ2\lambda\_{2};
By the definition of matrix exponential as a sum of powers,

|  |  |  |
| --- | --- | --- |
|  | expm​(Φ​t)=∑n=0∞(Φ​t)nn!=∑n=0∞(S​Λ​S−1​t)nn!=S​expm​(Λ​t)​S−1,\text{expm}(\Phi t)=\sum\_{n=0}^{\infty}\frac{(\Phi t)^{n}}{n!}=\sum\_{n=0}^{\infty}\frac{(S\Lambda S^{-1}t)^{n}}{n!}=S\ \text{expm}(\Lambda t)S^{-1}, |  |

where expm​(Λ​t)\text{expm}(\Lambda t) is simply diag​(eλ1​t,eλ2​t)\text{diag}(e^{\lambda\_{1}t},\ e^{\lambda\_{2}t}).
It is clear that if both λ1\lambda\_{1} and λ2\lambda\_{2} are negative and real (such that limt→∞expm(Φt))=0\lim\_{t\rightarrow\infty}\text{expm}(\Phi t))=0), the asymptotic expected values of intensities is

|  |  |  |
| --- | --- | --- |
|  | limt→∞(𝔼​(λt+|ℱs)𝔼​(λt−|ℱs))=−Φ−1​C.\displaystyle\lim\_{t\rightarrow\infty}\begin{pmatrix}{\mathbb{E}}(\lambda^{+}\_{t}|\mathcal{F}\_{s})\\ {\mathbb{E}}(\lambda^{-}\_{t}|\mathcal{F}\_{s})\end{pmatrix}=-\Phi^{-1}C. |  |

By the Gershgorin circle theorem, the eigenvalues of Φ\Phi lie within

|  |  |  |
| --- | --- | --- |
|  | {z:|z−(−κ++β11​𝔼​J+)|≤|β12​𝔼​J−|}∪{z:|z−(−κ−+β22​𝔼​J−)|≤|β21​𝔼​J+|}.\displaystyle\left\{z:\left|z-(-\kappa^{+}+\beta\_{11}{\mathbb{E}}J^{+})\right|\leq\left|\beta\_{12}{\mathbb{E}}J^{-}\right|\right\}\cup\left\{z:\left|z-(-\kappa^{-}+\beta\_{22}{\mathbb{E}}J^{-})\right|\leq\left|\beta\_{21}{\mathbb{E}}J^{+}\right|\right\}. |  |

Since β12​𝔼​J−\beta\_{12}{\mathbb{E}}J^{-} and β21​𝔼​J+\beta\_{21}{\mathbb{E}}J^{+} are always positive,
the eigenvalues of Φ\Phi lie within

|  |  |  |
| --- | --- | --- |
|  | {z:|z−(−κ++β11​𝔼​J+)|≤β12​𝔼​J−}∪{z:|z−(−κ−+β22​𝔼​J−)|≤β21​𝔼​J+}.\displaystyle\left\{z:\left|z-(-\kappa^{+}+\beta\_{11}{\mathbb{E}}J^{+})\right|\leq\beta\_{12}{\mathbb{E}}J^{-}\right\}\cup\left\{z:\left|z-(-\kappa^{-}+\beta\_{22}{\mathbb{E}}J^{-})\right|\leq\beta\_{21}{\mathbb{E}}J^{+}\right\}. |  |

Therefore, the sufficient conditions for the eigenvalues of Φ\Phi being negative are

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ+≥β11​𝔼​J++β12​𝔼​J−​ and ​κ−≥β21​𝔼​J++β22​𝔼​J−.\displaystyle\kappa^{+}\geq\beta\_{11}{\mathbb{E}}J^{+}+\beta\_{12}{\mathbb{E}}J^{-}\text{ and }\kappa^{-}\geq\beta\_{21}{\mathbb{E}}J^{+}+\beta\_{22}{\mathbb{E}}J^{-}. |  | (50) |

This means that if the mean reverting rates κ+\kappa^{+} and κ−\kappa^{-} are larger than their corresponding sum of excitements from jumps which are average in size,
the asymptotic expected values of intensities are finite.

### A.2 Proof of Proposition [1](https://arxiv.org/html/2510.21297v1#Thmlemma1 "Proposition 1. ‣ 2.2 Moment-generating function of joint dynamics ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")

Let G​(t,Xt,λt+,λt−)=𝔼​(exp⁡(ω​XT+ω+​λT++ω−​λT−)|Xt,λt+,λt−)G(t,X\_{t},\lambda\_{t}^{+},\lambda\_{t}^{-})={\mathbb{E}}\left(\exp(\omega X\_{T}+\omega^{+}\lambda^{+}\_{T}+\omega^{-}\lambda^{-}\_{T})\big|X\_{t},\lambda^{+}\_{t},\lambda^{-}\_{t}\right). The process (G​(t,Xt,λt+,λt−))t≥0(G(t,X\_{t},\lambda\_{t}^{+},\lambda\_{t}^{-}))\_{t\geq 0} is a (Doob-Lévy) martingale (see e.g. Theorem 2.31 of Klebaner ([2005](https://arxiv.org/html/2510.21297v1#bib.bib33))).
By the predictable Itô formula (e.g. Sections 10.2 and 8.4.3 of (Jeanblanc
et al., [2009](https://arxiv.org/html/2510.21297v1#bib.bib32)))
and the martingale property of GG,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =Gt\displaystyle=G\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(μ−σ22−λt+𝔼(eJ+−1)−λt−𝔼(eJ−−1)Gx+σ22Gx​x\displaystyle+\left(\mu-\frac{\sigma^{2}}{2}-\lambda^{+}\_{t}{\mathbb{E}}(e^{J^{+}}-1)-\lambda^{-}\_{t}{\mathbb{E}}(e^{J^{-}}-1\right)G\_{x}+\frac{\sigma^{2}}{2}G\_{xx} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ+​(θ+−λt+)​Gλ++κ−​(θ−−λt−)​Gλ−\displaystyle+\kappa^{+}(\theta^{+}-\lambda^{+}\_{t})G\_{\lambda^{+}}+\kappa^{-}(\theta^{-}-\lambda^{-}\_{t})G\_{\lambda^{-}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λt+​[∫ℝG​(t,Xt+j+,λt++β11​j+,λt−+β21​j+)​ϖ+​(j+)​dj+−G​(t,Xt,λt+,λt−)]\displaystyle+\lambda^{+}\_{t}\left[\int\_{\mathbb{R}}G(t,X\_{t}+j^{+},\lambda\_{t}^{+}+\beta\_{11}j^{+},\lambda\_{t}^{-}+\beta\_{21}j^{+})\varpi^{+}(j^{+}){\rm d}j^{+}-G(t,X\_{t},\lambda\_{t}^{+},\lambda\_{t}^{-})\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +λt−​[∫ℝG​(t,Xt+j−,λt++β12​j−,λt−+β22​j−,T)​ϖ−​(j−)​dj−−G​(t,Xt,λt+,λt−)],\displaystyle+\lambda^{-}\_{t}\left[\int\_{\mathbb{R}}G(t,X\_{t}+j^{-},\lambda\_{t}^{+}+\beta\_{12}j^{-},\lambda\_{t}^{-}+\beta\_{22}j^{-},T)\varpi^{-}(j^{-}){\rm d}j^{-}-G(t,X\_{t},\lambda\_{t}^{+},\lambda\_{t}^{-})\right], |  | (51) |

where Gt,Gx,Gx​x,Gλ+,Gλ−G\_{t},G\_{x},G\_{xx},G\_{\lambda^{+}},G\_{\lambda^{-}} denote the partial derivatives of GG.
Assume that GG has an exponential affine form (see e.g. Errais
et al. ([2010](https://arxiv.org/html/2510.21297v1#bib.bib21))):

|  |  |  |
| --- | --- | --- |
|  | G​(t,x,λ+,λ−)=exp⁡(A​(t,T)+B​(t,T)​x+C​(t,T)​λ++D​(t,T)​λ−),G(t,x,\lambda^{+},\lambda^{-})=\exp\left(A(t,T)+B(t,T)x+C(t,T)\lambda^{+}+D(t,T)\lambda^{-}\right), |  |

where the functions A,B,C,DA,B,C,D are time dependent functions with terminal conditions: A​(T,T)=0A(T,T)=0, B​(T,T)=ωB(T,T)=\omega, C​(T,T)=ω+C(T,T)=\omega^{+}, and D​(T,T)=ω−D(T,T)=\omega^{-}.
Inserting the partial derivatives into Equation ([A.2](https://arxiv.org/html/2510.21297v1#A1.Ex17 "A.2 Proof of Proposition 1 ‣ Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =(At+Bt​Xt+Ct​λt++Dt​λt−)​G\displaystyle=\left(A\_{t}+B\_{t}X\_{t}+C\_{t}\lambda\_{t}^{+}+D\_{t}\lambda\_{t}^{-}\right)G |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(μ−σ22−λt+​𝔼​(eJ+−1)−λt−​𝔼​(eJ−−1))​B​G\displaystyle+\left(\mu-\frac{\sigma^{2}}{2}-\lambda^{+}\_{t}{\mathbb{E}}(e^{J^{+}}-1)-\lambda^{-}\_{t}{\mathbb{E}}(e^{J^{-}}-1)\right)BG |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +σ22​B2​G\displaystyle+\frac{\sigma^{2}}{2}B^{2}G |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ+​(θ+−λt+)​C+κ−​(θ−−λt−)​D​G\displaystyle+\kappa^{+}(\theta^{+}-\lambda^{+}\_{t})C+\kappa^{-}(\theta^{-}-\lambda^{-}\_{t})DG |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λt+​[∫ℝG​(t,Xt+j+,λt++β11​j+,λt−+β21​j+)​ϖ+​(j+)​dj+−G​(t,Xt,λt+,λt−)]\displaystyle+\lambda^{+}\_{t}\left[\int\_{\mathbb{R}}G(t,X\_{t}+j^{+},\lambda\_{t}^{+}+\beta\_{11}j^{+},\lambda\_{t}^{-}+\beta\_{21}j^{+})\varpi^{+}(j^{+}){\rm d}j^{+}-G(t,X\_{t},\lambda\_{t}^{+},\lambda\_{t}^{-})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λt−​[∫ℝG​(t,Xt+j−,λt++β12​j−,λt−+β22​j−)​ϖ−​(j−)​dj−−G​(t,Xt,λt+,λt−)].\displaystyle+\lambda^{-}\_{t}\left[\int\_{\mathbb{R}}G(t,X\_{t}+j^{-},\lambda\_{t}^{+}+\beta\_{12}j^{-},\lambda\_{t}^{-}+\beta\_{22}j^{-})\varpi^{-}(j^{-}){\rm d}j^{-}-G(t,X\_{t},\lambda\_{t}^{+},\lambda\_{t}^{-})\right]. |  |

Grouping terms by the state variables and dividing both sides by GG (recall G>0G>0) gives,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =At+μ​B+σ22​(B2−B)+κ+​θ+​C+κ−​θ−​D\displaystyle=A\_{t}+\mu B+\frac{\sigma^{2}}{2}\left(B^{2}-B\right)+\kappa^{+}\theta^{+}C+\kappa^{-}\theta^{-}D |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Bt​Xt\displaystyle+B\_{t}X\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λt+​[ℒ(+)​(−B−C​β11−D​β21)−1+Ct−𝔼​(eJ+−1)​B−κ+​C]\displaystyle+\lambda\_{t}^{+}\left[\mathcal{L}^{(+)}(-B-C\beta\_{11}-D\beta\_{21})-1+C\_{t}-{\mathbb{E}}(e^{J^{+}}-1)B-\kappa^{+}C\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λt−​[ℒ(−)​(−B−C​β12−D​β22)−1+Dt−𝔼​(eJ−−1)​B−κ−​D],\displaystyle+\lambda\_{t}^{-}\left[\mathcal{L}^{(-)}(-B-C\beta\_{12}-D\beta\_{22})-1+D\_{t}-{\mathbb{E}}(e^{J^{-}}-1)B-\kappa^{-}D\right], |  |

with ℒ(+)\mathcal{L}^{(+)} and ℒ(−)\mathcal{L}^{(-)} the MGFs of positive and negative jump sizes, cf. Equations ([9](https://arxiv.org/html/2510.21297v1#S2.E9 "In 2.1 Price dynamics under ℙ-measure ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")) and ([10](https://arxiv.org/html/2510.21297v1#S2.E10 "In 2.1 Price dynamics under ℙ-measure ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")).
The above equation holds for all values of the state variables, x,λ+,λ−x,\lambda^{+},\lambda^{-}, so the following system of PDEs must hold

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =At+μ​B+σ22​(B2−B)+κ+​θ+​C+κ−​θ−​D\displaystyle=A\_{t}+\mu B+\frac{\sigma^{2}}{2}\left(B^{2}-B\right)+\kappa^{+}\theta^{+}C+\kappa^{-}\theta^{-}D |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =Bt\displaystyle=B\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =ℒ(+)​(−B−C​β11−D​β21)−1+∂tC−𝔼​(eJ+−1)​B−κ+​C\displaystyle=\mathcal{L}^{(+)}(-B-C\beta\_{11}-D\beta\_{21})-1+\partial\_{t}C-{\mathbb{E}}(e^{J^{+}}-1)B-\kappa^{+}C |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =ℒ(−)​(−B−C​β12−D​β22)−1+∂tD−𝔼​(eJ−−1)​B−κ−​D.\displaystyle=\mathcal{L}^{(-)}(-B-C\beta\_{12}-D\beta\_{22})-1+\partial\_{t}D-{\mathbb{E}}(e^{J^{-}}-1)B-\kappa^{-}D. |  |

The solution of the above system of PDEs is, for t≥0t\geq 0

|  |  |  |  |
| --- | --- | --- | --- |
|  | At​(t,T)\displaystyle A\_{t}(t,T) | =−μ​ω−σ22​(ω2−ω)−κ+​θ+​C​(t,T)−κ−​θ−​D​(t,T)\displaystyle=-\mu\omega-\frac{\sigma^{2}}{2}\left(\omega^{2}-\omega\right)-\kappa^{+}\theta^{+}C(t,T)-\kappa^{-}\theta^{-}D(t,T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Bt​(t,T)\displaystyle B\_{t}(t,T) | =0,\displaystyle=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct​(t,T)\displaystyle C\_{t}(t,T) | =−ℒ(+)​(−ω−C​(t,T)​β11−D​(t,T)​β21)+1+𝔼​(eJ+−1)​ω+κ+​C​(t,T),\displaystyle=-\mathcal{L}^{(+)}(-\omega-C(t,T)\beta\_{11}-D(t,T)\beta\_{21})+1+{\mathbb{E}}(e^{J^{+}}-1)\omega+\kappa^{+}C(t,T), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt​(t,T)\displaystyle D\_{t}(t,T) | =−ℒ(−)​(−ω−C​(t,T)​β12−D​(t,T)​β22)+1+𝔼​(eJ−−1)​ω+κ−​D​(t,T),\displaystyle=-\mathcal{L}^{(-)}(-\omega-C(t,T)\beta\_{12}-D(t,T)\beta\_{22})+1+{\mathbb{E}}(e^{J^{-}}-1)\omega+\kappa^{-}D(t,T), |  |

where the terminal conditions are A​(T,T)=0A(T,T)=0, =B​(T,T)=ω=B(T,T)=\omega, C​(T,T)=ω+C(T,T)=\omega^{+}, and D​(T,T)=ω−D(T,T)=\omega^{-}.

### A.3 Proof of Proposition [2](https://arxiv.org/html/2510.21297v1#Thmlemma2 "Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")

Let mt=ln⁡(Mt)m\_{t}=\ln(M\_{t}), so

|  |  |  |  |
| --- | --- | --- | --- |
|  | mt\displaystyle m\_{t} | =q1+​(ξ+)​λt++q1−​(ξ−)​λt−+ξ+​∑j=1Nt(1)Jj++ξ−​∑j=1Nt(2)Jj−+q2​(ξ+,ξ−)​t\displaystyle=q\_{1}^{+}(\xi^{+})\lambda\_{t}^{+}+q\_{1}^{-}(\xi^{-})\lambda\_{t}^{-}+\xi^{+}\sum\_{j=1}^{N\_{t}^{(1)}}J\_{j}^{+}+\xi^{-}\sum\_{j=1}^{N\_{t}^{(2)}}J\_{j}^{-}+q\_{2}(\xi^{+},\xi^{-})t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12​∫0tφ​(s)2​ds−∫0tφ​(s)​dWs\displaystyle\phantom{=\,}-\frac{1}{2}\int\_{0}^{t}\varphi(s)^{2}\,{\rm d}s-\int\_{0}^{t}\varphi(s)\,{\rm d}W\_{s} |  |

with dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​mt\displaystyle{\rm d}m\_{t} | =q1+​(ξ+)​κ+​(θ+−λt+)​d​t+(q1+​(ξ+)​β11+ξ+)​J+​d​Nt(1)+q1+​(ξ+)​β12​J−​d​Nt(2)\displaystyle=\phantom{=}q\_{1}^{+}(\xi^{+})\kappa^{+}(\theta^{+}-\lambda\_{t}^{+})\,{\rm d}t+(q\_{1}^{+}(\xi^{+})\beta\_{11}+\xi^{+})J^{+}\,{\rm d}N\_{t}^{(1)}+q\_{1}^{+}(\xi^{+})\beta\_{12}J^{-}\,{\rm d}N\_{t}^{(2)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +q1−​(ξ−)​κ−​(θ−−λt−)​d​t+q1−​(ξ−)​β21​J+​d​Nt(1)+(q1−​(ξ−)​β22+ξ−)​J−​d​Nt(2)\displaystyle\phantom{=\,}+q\_{1}^{-}(\xi^{-})\kappa^{-}(\theta^{-}-\lambda\_{t}^{-})\,{\rm d}t+q\_{1}^{-}(\xi^{-})\beta\_{21}J^{+}\,{\rm d}N\_{t}^{(1)}+(q\_{1}^{-}(\xi^{-})\beta\_{22}+\xi^{-})J^{-}\,{\rm d}N\_{t}^{(2)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +q2​(ξ+,ξ−)​d​t−12​φ​(t)2​d​t−φ​(t)​d​Wt\displaystyle\phantom{=\,}+q\_{2}(\xi^{+},\xi^{-})\,{\rm d}t-\frac{1}{2}\varphi(t)^{2}\,{\rm d}t-\varphi(t)\,{\rm d}W\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =q1+​(ξ+)​κ+​(θ+−λt+)​d​t+χ+​J+​d​Nt(1)+q1−​(ξ−)​κ−​(θ−−λt−)​d​t+χ−​J−​d​Nt(2)\displaystyle=\phantom{=}q\_{1}^{+}(\xi^{+})\kappa^{+}(\theta^{+}-\lambda\_{t}^{+})\,{\rm d}t+\chi^{+}J^{+}\,{\rm d}N\_{t}^{(1)}+q\_{1}^{-}(\xi^{-})\kappa^{-}(\theta^{-}-\lambda\_{t}^{-})\,{\rm d}t+\chi^{-}J^{-}\,{\rm d}N\_{t}^{(2)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +q2​(ξ+,ξ−)​d​t−12​φ​(t)2​d​t−φ​(t)​d​Wt.\displaystyle\phantom{=\,}+q\_{2}(\xi^{+},\xi^{-})\,{\rm d}t-\frac{1}{2}\varphi(t)^{2}\,{\rm d}t-\varphi(t)\,{\rm d}W\_{t}. |  |

Denote the random measures of J±J^{\pm} by Ξ±\Xi^{\pm}, so that J+=∫0∞Ξ+​(d​z)J^{+}=\int\_{0}^{\infty}\Xi^{+}({\rm d}z) and J−=∫−∞0Ξ−​(d​z)J^{-}=\int\_{-\infty}^{0}\Xi^{-}({\rm d}z). Applying Ito’s Lemma for semimartingales (e.g. Section 8.10 of Klebaner, [2005](https://arxiv.org/html/2510.21297v1#bib.bib33)) to MtM\_{t} gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Mt\displaystyle{\rm d}M\_{t} | =Mt−​d​mt+12​Mt​d​[mt,mt]\displaystyle=M\_{t-}\,{\rm d}m\_{t}+\frac{1}{2}M\_{t}\,{\rm d}[m\_{t},m\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Mt−​∫0∞(𝐞χ+​z−1−χ+​z)​Ξ+​(d​z)​dNt(1)+Mt−​∫−∞0(𝐞χ−​z−1−χ−​z)​Ξ−​(d​z)​dNt(2).\displaystyle\phantom{=\,}+M\_{t-}\int\_{0}^{\infty}\left({\bf e}^{\chi^{+}z}-1-\chi^{+}z\right)\Xi^{+}({\rm d}z)\,{\rm d}N\_{t}^{(1)}+M\_{t-}\int\_{-\infty}^{0}\left({\bf e}^{\chi^{-}z}-1-\chi^{-}z\right)\Xi^{-}({\rm d}z)\,{\rm d}N\_{t}^{(2)}. |  |

Expanding the d​mt{\rm d}m\_{t}-term and compensating the jumps gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Mt\displaystyle{\rm d}M\_{t} | =Mt​(q1+​(ξ+)​κ+​θ++q1−​(ξ−)​κ−​θ−+q2​(ξ+,ξ−))​d​t−Mt​φ​(t)​d​Wt\displaystyle=M\_{t}(q\_{1}^{+}(\xi^{+})\kappa^{+}\theta^{+}+q\_{1}^{-}(\xi^{-})\kappa^{-}\theta^{-}+q\_{2}(\xi^{+},\xi^{-}))\,{\rm d}t-M\_{t}\varphi(t)\,{\rm d}W\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −Mt​λt+​(q1+​(ξ+)​κ+−∫0∞(𝐞χ+​z−1)​ϖ+​(d​z))​d​t\displaystyle\phantom{=\,}-M\_{t}\lambda\_{t}^{+}\left(q\_{1}^{+}(\xi^{+})\kappa^{+}-\int\_{0}^{\infty}\left({\bf e}^{\chi^{+}z}-1\right)\,\varpi^{+}({\rm d}z)\,\right){\rm d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −Mt​λt−​(q1−​(ξ−)​κ−−∫−∞0(𝐞χ−​z−1)​ϖ−​(d​z))​d​t\displaystyle\phantom{=\,}-M\_{t}\lambda\_{t}^{-}\left(q\_{1}^{-}(\xi^{-})\kappa^{-}-\int\_{-\infty}^{0}\left({\bf e}^{\chi^{-}z}-1\right)\,\varpi^{-}({\rm d}z)\right){\rm d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Mt−​∫0∞(𝐞χ+​z−1)​(Ξ+​(d​z)​d​Nt(1)−λt+​ϖ+​(d​z)​d​t)\displaystyle\phantom{=\,}+M\_{t-}\int\_{0}^{\infty}\left({\bf e}^{\chi^{+}z}-1\right)(\Xi^{+}({\rm d}z)\,{\rm d}N\_{t}^{(1)}-\lambda\_{t}^{+}\varpi^{+}({\rm d}z)\,{\rm d}t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Mt−​∫−∞0(𝐞χ−​z−1)​(Ξ−​(d​z)​d​Nt(2)−λt−​ϖ−​(d​z)​d​t).\displaystyle\phantom{=\,}+M\_{t-}\int\_{-\infty}^{0}\left({\bf e}^{\chi^{-}z}-1\right)\,(\Xi^{-}({\rm d}z)\,{\rm d}N\_{t}^{(2)}-\lambda\_{t}^{-}\varpi^{-}({\rm d}z)\,{\rm d}t). |  |

The drift terms vanish if the conditions hold.

### A.4 Proof of Proposition [4](https://arxiv.org/html/2510.21297v1#Thmlemma4 "Proposition 4 (Jump intensity dynamics under the risk-neutral measure ℚ ). ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")

The initial guess of the relationship between λ+\lambda^{+} and λ+,ℚ\lambda^{+,\mathbb{Q}}, and λ−\lambda^{-} and λ−,ℚ\lambda^{-,\mathbb{Q}} under the measure ℙ\mathbb{P} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | λt+,ℚ\displaystyle\lambda^{+,\mathbb{Q}}\_{t} | =ℒ(+)​(−χ+)​λt+,\displaystyle=\mathcal{L}^{(+)}(-\chi^{+})\lambda^{+}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λt−,ℚ\displaystyle\lambda^{-,\mathbb{Q}}\_{t} | =ℒ(−)​(−χ−)​λt−,t≥0.\displaystyle=\mathcal{L}^{(-)}(-\chi^{-})\lambda^{-}\_{t},\quad t\geq 0. |  |

We verify the above by comparing the MGFs under the two measures.
Start with the MGF of jump intensities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[exp⁡(ω+​λT+,ℚ+ω−​λT−,ℚ)|ℱt]=\displaystyle{\mathbb{E}}^{\mathbb{Q}}\left[\exp(\omega^{+}\lambda^{+,\mathbb{Q}}\_{T}+\omega^{-}\lambda^{-,\mathbb{Q}}\_{T})\big|\mathcal{F}\_{t}\right]= | e−m​𝔼​(exp⁡(mT+ω+​λT+,ℚ+ω−​λT−,ℚ)|λt+=λ+,λt−=λ−,mt=m)\displaystyle e^{-m}{\mathbb{E}}\left(\exp(m\_{T}+\omega^{+}\lambda^{+,\mathbb{Q}}\_{T}+\omega^{-}\lambda^{-,\mathbb{Q}}\_{T})\big|\lambda^{+}\_{t}=\lambda^{+},\lambda^{-}\_{t}=\lambda^{-},m\_{t}=m\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =def\displaystyle\overset{\text{def}}{=} | e−m​H​(t​ω+,ω−;λ+,λ−,m,T).\displaystyle e^{-m}H(t\omega^{+},\omega^{-};\lambda^{+},\lambda^{-},m,T). |  |

Focus on the form of HH that is comparable to the MGF under measure ℙ\mathbb{P} stated in Proposition [1](https://arxiv.org/html/2510.21297v1#Thmlemma1 "Proposition 1. ‣ 2.2 Moment-generating function of joint dynamics ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps"):

|  |  |  |
| --- | --- | --- |
|  | H​(t,λ+,λ−,m,T)=exp⁡(A​(t,T)+C​(t,T)​ℒ(+)​(−χ+)​λ++D​(t,T)​ℒ(−)​(−χ−)​λ−+E​(t,T)​m),\displaystyle H(t,\lambda^{+},\lambda^{-},m,T)=\exp\left(A(t,T)+C(t,T)\mathcal{L}^{(+)}(-\chi^{+})\lambda^{+}+D(t,T)\mathcal{L}^{(-)}(-\chi^{-})\lambda^{-}+E(t,T)m\right), |  |

where the functions A,CA,C and DD are defined in Proposition [1](https://arxiv.org/html/2510.21297v1#Thmlemma1 "Proposition 1. ‣ 2.2 Moment-generating function of joint dynamics ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps") and have the same terminal conditions; EE is a time-dependent function with terminal condition E​(T,T)=1E(T,T)=1.
Applying Ito’s lemma and by martingale property of conditional expectation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =Ht\displaystyle=H\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(κ1+​(ξ+)​κ+​(θ+−λ+)+κ1−​(ξ−)​κ−​(θ−−λ−)+q2​(ξ+,ξ−)−12​φ2​(t))​Hm+12​φ2​(t)​Hm​m\displaystyle+\left(\kappa^{+}\_{1}(\xi^{+})\kappa^{+}(\theta^{+}-\lambda^{+})+\kappa^{-}\_{1}(\xi^{-})\kappa^{-}(\theta^{-}-\lambda^{-})+q\_{2}(\xi^{+},\xi^{-})-\frac{1}{2}\varphi^{2}(t)\right)H\_{m}+\frac{1}{2}\varphi^{2}(t)H\_{mm} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ+​(θ+−λ+)​Hλ++κ−​(θ−−λ−)​Hλ−\displaystyle+\kappa^{+}(\theta^{+}-\lambda^{+})H\_{\lambda^{+}}+\kappa^{-}(\theta^{-}-\lambda^{-})H\_{\lambda^{-}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ+​[∫ℝH​(t,λ++β11​j+,λ−+β21​j+,m+χ+​j+,T)​ϖ+​(j+)​dj+−H​(t,λ+,λ−,m,T)]\displaystyle+\lambda^{+}\left[\int\_{\mathbb{R}}H(t,\lambda^{+}+\beta\_{11}j^{+},\lambda^{-}+\beta\_{21}j^{+},m+\chi^{+}j^{+},T)\varpi^{+}(j^{+}){\rm d}j^{+}-H(t,\lambda^{+},\lambda^{-},m,T)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ−​[∫ℝH​(t,λ++β12​j−,λ−+β22​j−,m+χ+​j−,T)​ϖ−​(j−)​dj−−H​(t,λ+,λ−,m,T)].\displaystyle+\lambda^{-}\left[\int\_{\mathbb{R}}H(t,\lambda^{+}+\beta\_{12}j^{-},\lambda^{-}+\beta\_{22}j^{-},m+\chi^{+}j^{-},T)\varpi^{-}(j^{-}){\rm d}j^{-}-H(t,\lambda^{+},\lambda^{-},m,T)\right]. |  |

By the first martingale condition of process {Mt}t≥0\left\{M\_{t}\right\}\_{t\geq 0}, Eq.([17](https://arxiv.org/html/2510.21297v1#S2.E17 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")), we simplify the above equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =Ht\displaystyle=H\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(κ1+​(ξ+)​κ+​λ++κ1−​(ξ−)​κ−​λ−+12​φ2​(t))​Hm+12​φ2​(t)​Hm​m\displaystyle-\left(\kappa^{+}\_{1}(\xi^{+})\kappa^{+}\lambda^{+}+\kappa^{-}\_{1}(\xi^{-})\kappa^{-}\lambda^{-}+\frac{1}{2}\varphi^{2}(t)\right)H\_{m}+\frac{1}{2}\varphi^{2}(t)H\_{mm} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ+​(θ+−λ+)​Hλ++κ−​(θ−−λ−)​Hλ−\displaystyle+\kappa^{+}(\theta^{+}-\lambda^{+})H\_{\lambda^{+}}+\kappa^{-}(\theta^{-}-\lambda^{-})H\_{\lambda^{-}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ+​[∫ℝH​(t,λ++β11​j+,λ−+β21​j+,m+χ+​j+,T)​ϖ+​(j+)​dj+−H​(t,λ+,λ−,m,T)]\displaystyle+\lambda^{+}\left[\int\_{\mathbb{R}}H(t,\lambda^{+}+\beta\_{11}j^{+},\lambda^{-}+\beta\_{21}j^{+},m+\chi^{+}j^{+},T)\varpi^{+}(j^{+}){\rm d}j^{+}-H(t,\lambda^{+},\lambda^{-},m,T)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ−​[∫ℝH​(t,λ++β12​j−,λ−+β22​j−,m+χ−​j−,T)​ϖ−​(j−)​dj−−H​(t,λ+,λ−,m,T)].\displaystyle+\lambda^{-}\left[\int\_{\mathbb{R}}H(t,\lambda^{+}+\beta\_{12}j^{-},\lambda^{-}+\beta\_{22}j^{-},m+\chi^{-}j^{-},T)\varpi^{-}(j^{-}){\rm d}j^{-}-H(t,\lambda^{+},\lambda^{-},m,T)\right]. |  |

Inserting the partial derivatives of HH into the above equation and dividing both sides by HH,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =At+Ct​ℒ(+)​(−χ+)​λ++Dt​ℒ(−)​(−χ−)​λ−+Et​m\displaystyle=A\_{t}+C\_{t}\,\mathcal{L}^{(+)}(-\chi^{+})\lambda^{+}+D\_{t}\,\mathcal{L}^{(-)}(-\chi^{-})\lambda^{-}+E\_{t}\,m |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(κ1+​(ξ+)​κ+​λ++κ1−​(ξ−)​κ−​λ−+12​φ2​(t))​E+12​φ2​(t)​E2\displaystyle-\left(\kappa^{+}\_{1}(\xi^{+})\kappa^{+}\lambda^{+}+\kappa^{-}\_{1}(\xi^{-})\kappa^{-}\lambda^{-}+\frac{1}{2}\varphi^{2}(t)\right)E+\frac{1}{2}\varphi^{2}(t)E^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ+​(θ+−λ+)​ℒ(+)​(−χ+)​C+κ−​(θ−−λ−)​ℒ(−)​(−χ−)​D\displaystyle+\kappa^{+}(\theta^{+}-\lambda^{+})\mathcal{L}^{(+)}(-\chi^{+})C+\kappa^{-}(\theta^{-}-\lambda^{-})\mathcal{L}^{(-)}(-\chi^{-})D |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ+​[ℒ(+)​(−C​ℒ(+)​(−χ+)​β11−D​ℒ(−)​(−χ−)​β21−E​χ+)−1]\displaystyle+\lambda^{+}\left[\mathcal{L}^{(+)}(-C\mathcal{L}^{(+)}(-\chi^{+})\beta\_{11}-D\mathcal{L}^{(-)}(-\chi^{-})\beta\_{21}-E\chi^{+})-1\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ−​[ℒ(−)​(−C​ℒ(+)​(−χ+)​β12−D​ℒ(−)​(−χ−)​β22−E​χ−)−1]\displaystyle+\lambda^{-}\left[\mathcal{L}^{(-)}(-C\mathcal{L}^{(+)}(-\chi^{+})\beta\_{12}-D\mathcal{L}^{(-)}(-\chi^{-})\beta\_{22}-E\chi^{-})-1\right] |  |

Grouping terms by the state variables, xx, λ+\lambda^{+}, and λ−\lambda^{-},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =At+12​φ2​(t)​(E2−E)+κ+​θ+​ℒ(+)​(−χ+)​C+κ−​θ−​ℒ(−)​(−χ−)​D\displaystyle=A\_{t}+\frac{1}{2}\varphi^{2}(t)(E^{2}-E)+\kappa^{+}\theta^{+}\mathcal{L}^{(+)}(-\chi^{+})C+\kappa^{-}\theta^{-}\mathcal{L}^{(-)}(-\chi^{-})D |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Et​m\displaystyle+E\_{t}\,m |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ+​[ℒ(+)​(−C​ℒ(+)​(−χ+)​β11−D​ℒ(−)​(−χ−)​β21−E​χ+)−1+Ct​ℒ(+)​(−χ+)−κ1+​(ξ+)​κ+−κ+​C​ℒ(+)​(−χ+)]\displaystyle+\lambda^{+}\left[\mathcal{L}^{(+)}(-C\mathcal{L}^{(+)}(-\chi^{+})\beta\_{11}-D\mathcal{L}^{(-)}(-\chi^{-})\beta\_{21}-E\chi^{+})-1+C\_{t}\,\mathcal{L}^{(+)}(-\chi^{+})-\kappa^{+}\_{1}(\xi^{+})\kappa^{+}-\kappa^{+}C\mathcal{L}^{(+)}(-\chi^{+})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ−​[ℒ(−)​(−C​ℒ(+)​(−χ+)​β12−D​ℒ(−)​(−χ−)​β22−E​χ−)−1+Dt​ℒ(−)​(−χ−)−κ1−​(ξ−)​κ−−κ−​D​ℒ(−)​(−χ−)]\displaystyle+\lambda^{-}\left[\mathcal{L}^{(-)}(-C\mathcal{L}^{(+)}(-\chi^{+})\beta\_{12}-D\mathcal{L}^{(-)}(-\chi^{-})\beta\_{22}-E\chi^{-})-1+D\_{t}\,\mathcal{L}^{(-)}(-\chi^{-})-\kappa^{-}\_{1}(\xi^{-})\kappa^{-}-\kappa^{-}D\mathcal{L}^{(-)}(-\chi^{-})\right] |  |

The above equation holds for all values of x,λ+x,\ \lambda^{+} and λ−\lambda^{-}, we infer

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tA​(t,T)\displaystyle\partial\_{t}A(t,T) | =−κ+​θ+​ℒ(+)​(−χ+)​C​(t,T)−κ−​θ−​ℒ(−)​(−χ−)​D​(t,T)\displaystyle=-\kappa^{+}\theta^{+}\mathcal{L}^{(+)}(-\chi^{+})C(t,T)-\kappa^{-}\theta^{-}\mathcal{L}^{(-)}(-\chi^{-})D(t,T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tC​(t,T)\displaystyle\partial\_{t}C(t,T) | =−ℒ(+)​(−C​(t,T)​ℒ(+)​(−χ+)​β11−D​(t,T)​ℒ(−)​(−χ−)​β21−χ+)ℒ(+)​(−χ+)+1+κ1+​(ξ+)​κ+ℒ(+)​(−χ+)+κ+​C​(t,T),\displaystyle=-\frac{\mathcal{L}^{(+)}(-C(t,T)\mathcal{L}^{(+)}(-\chi^{+})\beta\_{11}-D(t,T)\mathcal{L}^{(-)}(-\chi^{-})\beta\_{21}-\chi^{+})}{\mathcal{L}^{(+)}(-\chi^{+})}+\frac{1+\kappa^{+}\_{1}(\xi^{+})\kappa^{+}}{\mathcal{L}^{(+)}(-\chi^{+})}+\kappa^{+}C(t,T), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tD​(t,T)\displaystyle\partial\_{t}D(t,T) | =−ℒ(−)​(−C​(t,T)​ℒ(+)​(−χ+)​β12−D​(t,T)​ℒ(−)​(−χ−)​β22−χ−)ℒ(−)​(−χ−)+1+κ1−​(ξ−)​κ−ℒ(−)​(−χ−)+κ−​D​(t,T),\displaystyle=-\frac{\mathcal{L}^{(-)}(-C(t,T)\mathcal{L}^{(+)}(-\chi^{+})\beta\_{12}-D(t,T)\mathcal{L}^{(-)}(-\chi^{-})\beta\_{22}-\chi^{-})}{\mathcal{L}^{(-)}(-\chi^{-})}+\frac{1+\kappa^{-}\_{1}(\xi^{-})\kappa^{-}}{\mathcal{L}^{(-)}(-\chi^{-})}+\kappa^{-}D(t,T), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tE​(t,T)\displaystyle\partial\_{t}E(t,T) | =0.\displaystyle=0. |  |

The terminal conditions are A​(T,T)=0,C​(T,T)=ω+,D​(T,T)=ω−, and​E​(T,T)=1A(T,T)=0,\ C(T,T)=\omega^{+},\ D(T,T)=\omega^{-},\text{ and}E(T,T)=1.

The first term of ∂tC\partial\_{t}C, ℒ(+)​(−C​(t,T)​ℒ(+)​(−χ+)​β11−D​(t,T)​ℒ(−)​(−χ−)​β21−χ+)ℒ(+)​(−χ+)\frac{\mathcal{L}^{(+)}(-C(t,T)\mathcal{L}^{(+)}(-\chi^{+})\beta\_{11}-D(t,T)\mathcal{L}^{(-)}(-\chi^{-})\beta\_{21}-\chi^{+})}{\mathcal{L}^{(+)}(-\chi^{+})}, is in fact an Esscher transformation applied onto the positive jumps size density ϖ+\varpi^{+} with −χ+-\chi^{+} as the Esscher parameter (A general form of Esscher transform can be found in Eq. (2.6) in Gerber and
Shiu ([1995](https://arxiv.org/html/2510.21297v1#bib.bib22)).).
Similarly, the first term of ∂tD\partial\_{t}D is an Esscher transform to the negative jumps size density with −χ−-\chi^{-} as the Esscher parameter.
We denote the transformed MGFs of the jumps sizes as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ(+),ℚ​(x)\displaystyle\mathcal{L}^{(+),\mathbb{Q}}(x) | =def​ℒ(+)​(x−χ+)ℒ(+)​(−χ+)​, and\displaystyle\overset{\text{def}}{=}\frac{\mathcal{L}^{(+)}(x-\chi^{+})}{\mathcal{L}^{(+)}(-\chi^{+})}\text{, and } |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ(−),ℚ​(x)\displaystyle\mathcal{L}^{(-),\mathbb{Q}}(x) | =def​ℒ(−)​(x−χ−)ℒ(−)​(−χ−).\displaystyle\overset{\text{def}}{=}\frac{\mathcal{L}^{(-)}(x-\chi^{-})}{\mathcal{L}^{(-)}(-\chi^{-})}. |  |

On the other hand, the second terms of ∂tC\partial\_{t}C and ∂tD\partial\_{t}D can be simplified by the martingale conditions in Eq.([17](https://arxiv.org/html/2510.21297v1#S2.E17 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")).

To summarise,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tC​(t,T)\displaystyle\partial\_{t}C(t,T) | =−ℒ(+),ℚ​(−C​(t,T)​ℒ(+)​(−χ+)​β11−D​(t,T)​ℒ(−)​(−χ−)​β21)+1+κ+​C​(t,T)\displaystyle=-\mathcal{L}^{(+),\mathbb{Q}}\left(-C(t,T)\mathcal{L}^{(+)}(-\chi^{+})\beta\_{11}-D(t,T)\mathcal{L}^{(-)}(-\chi^{-})\beta\_{21}\right)+1+\kappa^{+}C(t,T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tD​(t,T)\displaystyle\partial\_{t}D(t,T) | =−ℒ(−),ℚ​(−C​(t,T)​ℒ(+)​(−χ+)​β12−D​(t,T)​ℒ(−)​(−χ−)​β22)+1+κ−​D​(t,T).\displaystyle=-\mathcal{L}^{(-),\mathbb{Q}}\left(-C(t,T)\mathcal{L}^{(+)}(-\chi^{+})\beta\_{12}-D(t,T)\mathcal{L}^{(-)}(-\chi^{-})\beta\_{22}\right)+1+\kappa^{-}D(t,T). |  |

Next, we work out the Esscher transformed densities of the jump sizes (see Eq.(2.5) of Gerber and
Shiu ([1995](https://arxiv.org/html/2510.21297v1#bib.bib22))),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϖ+,ℚ​(j)​=def​e−χ+​j​ϖ+​(j)∫ℝe−χ+​ϖ+​(y)​d​y\displaystyle\varpi^{+,\mathbb{Q}}(j)\overset{\text{def}}{=}\frac{e^{-\chi^{+}j}\varpi^{+}(j)}{\int\_{\mathbb{R}}e^{-\chi^{+}}\varpi^{+}(y)\text{d}y} | =1η+,ℚ​exp⁡(−1η+,ℚ​(j−ν+))​𝟙{j>ν+}\displaystyle=\frac{1}{\eta^{+,\mathbb{Q}}}\exp\left(-\frac{1}{\eta^{+,\mathbb{Q}}}(j-\nu^{+})\right)\mathbbm{1}\_{\{j>\nu^{+}\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ϖ−,ℚ​(j)​=def​e−χ−​j​ϖ−​(j)∫ℝe−χ−​ϖ−​(y)​d​y\displaystyle\varpi^{-,\mathbb{Q}}(j)\overset{\text{def}}{=}\frac{e^{-\chi^{-}j}\varpi^{-}(j)}{\int\_{\mathbb{R}}e^{-\chi^{-}}\varpi^{-}(y)\text{d}y} | =1η−,ℚ​exp⁡(1η−,ℚ​(j−ν−))​𝟙{j<ν−},\displaystyle=\frac{1}{\eta^{-,\mathbb{Q}}}\exp\left(\phantom{-}\frac{1}{\eta^{-,\mathbb{Q}}}(j-\nu^{-})\right)\mathbbm{1}\_{\{j<\nu^{-}\}}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | η+,ℚ=η+1−η+​χ+,and​η−,ℚ=η−1+η−​χ−.\displaystyle\eta^{+,\mathbb{Q}}=\frac{\eta^{+}}{1-\eta^{+}\chi^{+}},\ \text{and}\ \eta^{-,\mathbb{Q}}=\frac{\eta^{-}}{1+\eta^{-}\chi^{-}}. |  |

To summarise the parameter changes, the MGF of the jump intensities under the measure ℚ\mathbb{Q} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​(eω+​λT++ω−​λT−|ℱt)\displaystyle{\mathbb{E}}^{\mathbb{Q}}\left(e^{\omega^{+}\lambda^{+}\_{T}+\omega^{-}\lambda^{-}\_{T}}|\mathcal{F}\_{t}\right) | =exp⁡(A​(t,T)+C​(t,T)​ℒ(+)​(−χ+)​λt++D​(t,T)​ℒ(−)​(−χ−)​λt−)\displaystyle=\exp\left(A(t,T)+C(t,T)\mathcal{L}^{(+)}(-\chi^{+})\lambda^{+}\_{t}+D(t,T)\mathcal{L}^{(-)}(-\chi^{-})\lambda^{-}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(A​(t,T)+C​(t,T)​λt+,ℚ+D​(t,T)​λt−,ℚ),\displaystyle=\exp\left(A(t,T)+C(t,T)\lambda^{+,\mathbb{Q}}\_{t}+D(t,T)\lambda^{-,\mathbb{Q}}\_{t}\right), |  |

where the function A,CA,C and DD solve the following system of PDEs

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂tA​(t,T)\displaystyle\partial\_{t}A(t,T) | =−κ+​θ+​ℒ(+)​(−χ+)​C​(t,T)−κ−​θ−​ℒ(−)​(−χ−)​D​(t,T),\displaystyle=-\kappa^{+}\theta^{+}\mathcal{L}^{(+)}(-\chi^{+})C(t,T)-\kappa^{-}\theta^{-}\mathcal{L}^{(-)}(-\chi^{-})D(t,T), | A​(T,T)\displaystyle A(T,T) | =0\displaystyle=0 |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂tC​(t,T)\displaystyle\partial\_{t}C(t,T) | =−ℒ(+),ℚ​(−C​(t,T)​ℒ(+)​(−χ+)​β11−D​(t,T)​ℒ(−),ℚ​(−χ−)​β21)+1+κ+​C​(t,T),\displaystyle=-\mathcal{L}^{(+),\mathbb{Q}}(-C(t,T)\mathcal{L}^{(+)}(-\chi^{+})\beta\_{11}-D(t,T)\mathcal{L}^{(-),\mathbb{Q}}(-\chi^{-})\beta\_{21})+1+\kappa^{+}C(t,T), | C​(T,T)\displaystyle C(T,T) | =ω+\displaystyle=\omega^{+} |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ∂tC​(t,T)\displaystyle\partial\_{t}C(t,T) | =−ℒ(−),ℚ​(−C​(t,T)​ℒ(+)​(−χ+)​β12−D​(t,T)​ℒ(−),ℚ​(−χ−)​β22)+1+κ−​D​(t,T),\displaystyle=-\mathcal{L}^{(-),\mathbb{Q}}(-C(t,T)\mathcal{L}^{(+)}(-\chi^{+})\beta\_{12}-D(t,T)\mathcal{L}^{(-),\mathbb{Q}}(-\chi^{-})\beta\_{22})+1+\kappa^{-}D(t,T), | D​(T,T)\displaystyle D(T,T) | =ω−.\displaystyle=\omega^{-}. |  |

By comparing the above MGF under ℚ\mathbb{Q} to the MGF under ℙ\mathbb{P} in Proposition [1](https://arxiv.org/html/2510.21297v1#Thmlemma1 "Proposition 1. ‣ 2.2 Moment-generating function of joint dynamics ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps") (when ω=0\omega=0), we conclude that the measure change

* •

  alters the positive and negative jump intensities by multipliers ℒ(+)​(−χ+)\mathcal{L}^{(+)}(-\chi^{+}) and ℒ(−)​(−χ−)\mathcal{L}^{(-)}(-\chi^{-}), respectively.
* •

  shifts the rates of the positive and negative jump sizes from η+\eta^{+} to η+/(1−η+​χ+)\eta^{+}/(1-\eta^{+}\chi^{+}) and from η−\eta^{-} to η−/(1+η−​χ−)\eta^{-}/(1+\eta^{-}\chi^{-}), respectively.
* •

  preserves the mean reversion rates of jump intensities κ+\kappa^{+} and κ−\kappa^{-} and the shift parameters of jump sizes ν+\nu^{+} and ν−\nu^{-}.

### A.5 Proof of Proposition [5](https://arxiv.org/html/2510.21297v1#Thmlemma5 "Proposition 5. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")

The proof relies on comparing the the MGFs of XX under ℚ\mathbb{Q} and ℙ\mathbb{P}.
First, we derive the MGF of XX under ℚ\mathbb{Q}. Denote mt=ln⁡(Mt)m\_{t}=\ln(M\_{t}).
Given Xt=x,λt+=λ+,λt−=λ−X\_{t}=x,\lambda\_{t}^{+}=\lambda^{+},\lambda\_{t}^{-}=\lambda^{-} and mt=mm\_{t}=m, the MGF is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​(eω​XT|ℱt)\displaystyle{\mathbb{E}}^{\mathbb{Q}}\left(e^{\omega X\_{T}}\big|\mathcal{F}\_{t}\right) | =𝔼​(emT−m+ω​XT|ℱt)\displaystyle={\mathbb{E}}\left(e^{m\_{T}-m+\omega X\_{T}}\big|\mathcal{F}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e−m​𝔼​(emT+ω​XT|Xt=x,λt+=λ+,λt−=λ−,Mt=m,T),\displaystyle=e^{-m}{\mathbb{E}}\left(e^{m\_{T}+\omega X\_{T}}\big|X\_{t}=x,\lambda^{+}\_{t}=\lambda^{+},\lambda^{-}\_{t}=\lambda^{-},M\_{t}=m,T\right), |  |

where mt=l​n​(Mt)m\_{t}=ln(M\_{t}).
Let H​(t​ω;x,λ+,λ−,m,T)=𝔼​(eMT+ω​XT|Xt=x,λt+=λ+,λt−=λ−,Mt=m)H(t\omega;x,\lambda^{+},\lambda^{-},m,T)={\mathbb{E}}\left(e^{M\_{T}+\omega X\_{T}}\big|X\_{t}=x,\lambda^{+}\_{t}=\lambda^{+},\lambda^{-}\_{t}=\lambda^{-},M\_{t}=m\right). By the tower law, {H​(t)}t≥0\left\{H(t)\right\}\_{t\geq 0} is a martingale.
By Ito’s lemma and martingale property of conditional expectation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =∂tH\displaystyle=\partial\_{t}H |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(μ−σ22−λ+​𝔼​(eJ+−1)−λ−​𝔼​(eJ−−1))​∂xH+σ22​∂x2H\displaystyle+\left(\mu-\frac{\sigma^{2}}{2}-\lambda^{+}{\mathbb{E}}\left(e^{J^{+}}-1\right)-\lambda^{-}{\mathbb{E}}\left(e^{J^{-}}-1\right)\right)\partial\_{x}H+\frac{\sigma^{2}}{2}\partial^{2}\_{x}H |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(κ1+​(ξ+)​κ+​(θ+−λ+)+κ1−​(ξ−)​κ−​(θ−−λ−)+q2​(ξ+,ξ−)−12​φ2​(t))​∂mH+12​φ2​(t)​∂m2H\displaystyle+\left(\kappa^{+}\_{1}(\xi^{+})\kappa^{+}(\theta^{+}-\lambda^{+})+\kappa^{-}\_{1}(\xi^{-})\kappa^{-}(\theta^{-}-\lambda^{-})+q\_{2}(\xi^{+},\xi^{-})-\frac{1}{2}\varphi^{2}(t)\right)\partial\_{m}H+\frac{1}{2}\varphi^{2}(t)\partial^{2}\_{m}H |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −σ​φ​(t)​∂x​m2\displaystyle-\sigma\varphi(t)\partial^{2}\_{xm} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ+​(θ+−λ+)​∂+H+κ−​(θ−−λ−)​∂−H\displaystyle+\kappa^{+}(\theta^{+}-\lambda^{+})\partial\_{+}H+\kappa^{-}(\theta^{-}-\lambda^{-})\partial\_{-}H |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ+​[∫ℝH​(t,ω+,ω−;λ++β11​j+,λ−+β21​j+,m+χ+​j+,T)​ϖ+​(j+)​dj+−H​(t,ω+,ω−;λ+,λ−,m,T)]\displaystyle+\lambda^{+}\left[\int\_{\mathbb{R}}H(t,\omega^{+},\omega^{-};\lambda^{+}+\beta\_{11}j^{+},\lambda^{-}+\beta\_{21}j^{+},m+\chi^{+}j^{+},T)\varpi^{+}(j^{+}){\rm d}j^{+}-H(t,\omega^{+},\omega^{-};\lambda^{+},\lambda^{-},m,T)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ−​[∫ℝH​(t,ω+,ω−;λ++β12​j−,λ−+β22​j−,m+χ+​j−,T)​ϖ−​(j−)​dj−−H​(t,ω+,ω−;λ+,λ−,m,T)].\displaystyle+\lambda^{-}\left[\int\_{\mathbb{R}}H(t,\omega^{+},\omega^{-};\lambda^{+}+\beta\_{12}j^{-},\lambda^{-}+\beta\_{22}j^{-},m+\chi^{+}j^{-},T)\varpi^{-}(j^{-}){\rm d}j^{-}-H(t,\omega^{+},\omega^{-};\lambda^{+},\lambda^{-},m,T)\right]. |  |

By the first martingale condition of process {Mt}t≥0\left\{M\_{t}\right\}\_{t\geq 0}, Eq.([17](https://arxiv.org/html/2510.21297v1#S2.E17 "In Proposition 2. ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps")), we simplify the above equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =∂tH\displaystyle=\partial\_{t}H |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(μ−σ22−λ+​𝔼​(eJ+−1)−λ−​𝔼​(eJ−−1))​∂xH+σ22​∂x2H\displaystyle+\left(\mu-\frac{\sigma^{2}}{2}-\lambda^{+}{\mathbb{E}}\left(e^{J^{+}}-1\right)-\lambda^{-}{\mathbb{E}}\left(e^{J^{-}}-1\right)\right)\partial\_{x}H+\frac{\sigma^{2}}{2}\partial^{2}\_{x}H |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(κ1+​(ξ+)​κ+​λ++κ1−​(ξ−)​κ−​λ−+12​φ2​(t))​∂mH+12​φ2​(t)​∂m2H−σ​φ​(t)​∂x​m2\displaystyle-\left(\kappa^{+}\_{1}(\xi^{+})\kappa^{+}\lambda^{+}+\kappa^{-}\_{1}(\xi^{-})\kappa^{-}\lambda^{-}+\frac{1}{2}\varphi^{2}(t)\right)\partial\_{m}H+\frac{1}{2}\varphi^{2}(t)\partial^{2}\_{m}H-\sigma\varphi(t)\partial^{2}\_{xm} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ+​(θ+−λ+)​∂+H+κ−​(θ−−λ−)​∂−H\displaystyle+\kappa^{+}(\theta^{+}-\lambda^{+})\partial\_{+}H+\kappa^{-}(\theta^{-}-\lambda^{-})\partial\_{-}H |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ+​[∫ℝH​(t,ω+,ω−;λ++β11​j+,λ−+β21​j+,m+χ+​j+,T)​ϖ+​(j+)​dj+−H​(t,ω+,ω−;λ+,λ−,m,T)]\displaystyle+\lambda^{+}\left[\int\_{\mathbb{R}}H(t,\omega^{+},\omega^{-};\lambda^{+}+\beta\_{11}j^{+},\lambda^{-}+\beta\_{21}j^{+},m+\chi^{+}j^{+},T)\varpi^{+}(j^{+}){\rm d}j^{+}-H(t,\omega^{+},\omega^{-};\lambda^{+},\lambda^{-},m,T)\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +λ−​[∫ℝH​(t,ω+,ω−;λ++β12​j−,λ−+β22​j−,m+χ−​j−,T)​ϖ−​(j−)​dj−−H​(t,ω+,ω−;λ+,λ−,m,T)].\displaystyle+\lambda^{-}\left[\int\_{\mathbb{R}}H(t,\omega^{+},\omega^{-};\lambda^{+}+\beta\_{12}j^{-},\lambda^{-}+\beta\_{22}j^{-},m+\chi^{-}j^{-},T)\varpi^{-}(j^{-}){\rm d}j^{-}-H(t,\omega^{+},\omega^{-};\lambda^{+},\lambda^{-},m,T)\right]. |  | (52) |

Next, we write the form of HH such that it is comparable to the MGF under measure ℙ\mathbb{P} stated in Proposition [1](https://arxiv.org/html/2510.21297v1#Thmlemma1 "Proposition 1. ‣ 2.2 Moment-generating function of joint dynamics ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps"):

|  |  |  |
| --- | --- | --- |
|  | H​(t;ω,x,λ+,λ−,m,T)=exp⁡(A​(t,T)+B​(t,T)​x+C​(t,T)​ℒ(+)​(−χ+)​λ++D​(t,T)​ℒ(−)​(−χ−)+E​(t,T)​m),\displaystyle H(t;\omega,x,\lambda^{+},\lambda^{-},m,T)=\exp\left(A(t,T)+B(t,T)x+C(t,T)\mathcal{L}^{(+)}(-\chi^{+})\lambda^{+}+D(t,T)\mathcal{L}^{(-)}(-\chi^{-})+E(t,T)m\right), |  |

where functions AA, BB, CC, and DD are defined in Proposition [1](https://arxiv.org/html/2510.21297v1#Thmlemma1 "Proposition 1. ‣ 2.2 Moment-generating function of joint dynamics ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps") with terminal conditions A​(T,T)=0A(T,T)=0, B​(T,T)=ωB(T,T)=\omega, and C​(T,T)=D​(T,T)=0C(T,T)=D(T,T)=0; EE is a time-dependent function with terminal condition E​(T,T)=1E(T,T)=1.
Inserting the partial derivatives of HH into Eq.([52](https://arxiv.org/html/2510.21297v1#A1.E52 "In A.5 Proof of Proposition 5 ‣ Appendix A Proofs ‣ Jump risk premia in the presence of clustered jumps"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =∂tA+∂tB​x+∂tC​ℒ(+)​(−χ+)​λ++∂tD​ℒ(−)​(−χ−)​λ−+∂tE​m\displaystyle=\partial\_{t}A+\partial\_{t}Bx+\partial\_{t}C\mathcal{L}^{(+)}\left(-\chi^{+}\right)\lambda^{+}+\partial\_{t}D\mathcal{L}^{(-)}\left(-\chi^{-}\right)\lambda^{-}+\partial\_{t}Em |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(μ−σ22−λ+​𝔼​(eJ+−1)−λ−​𝔼​(eJ−−1))​B+σ22​B2\displaystyle+\left(\mu-\frac{\sigma^{2}}{2}-\lambda^{+}{\mathbb{E}}\left(e^{J^{+}}-1\right)-\lambda^{-}{\mathbb{E}}\left(e^{J^{-}}-1\right)\right)B+\frac{\sigma^{2}}{2}B^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(κ1+​(ξ+)​κ+​λ++κ1−​(ξ−)​κ−​λ−+12​φ2​(t))​E+12​φ2​(t)​E2\displaystyle-\left(\kappa\_{1}^{+}\left(\xi^{+}\right)\kappa^{+}\lambda^{+}+\kappa\_{1}^{-}\left(\xi^{-}\right)\kappa^{-}\lambda^{-}+\frac{1}{2}\varphi^{2}(t)\right)E+\frac{1}{2}\varphi^{2}(t)E^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ+​(θ+−λ+)​ℒ(+)​(−χ+)​C+κ−​(θ−−λ−)​ℒ(−)​(−χ−)​D\displaystyle+\kappa^{+}\left(\theta^{+}-\lambda^{+}\right)\mathcal{L}^{(+)}\left(-\chi^{+}\right)C+\kappa^{-}\left(\theta^{-}-\lambda^{-}\right)\mathcal{L}^{(-)}\left(-\chi^{-}\right)D |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −B​E​σ​φ​(t)\displaystyle-BE\sigma\varphi(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ+​[ℒ(+)​(−B−C​ℒ(+)​(−χ+)​β11−D​ℒ(−)​(−χ−)​β21−E​χ+)−1]\displaystyle+\lambda^{+}\left[\mathcal{L}^{(+)}\left(-B-C\mathcal{L}^{(+)}\left(-\chi^{+}\right)\beta\_{11}-D\mathcal{L}^{(-)}\left(-\chi^{-}\right)\beta\_{21}-E\chi^{+}\right)-1\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ−​[ℒ(−)​(−B−C​ℒ(+)​(−χ+)​β12−D​ℒ(−)​(−χ−)​β22−E​χ−)−1]\displaystyle+\lambda^{-}\left[\mathcal{L}^{(-)}\left(-B-C\mathcal{L}^{(+)}\left(-\chi^{+}\right)\beta\_{12}-D\mathcal{L}^{(-)}\left(-\chi^{-}\right)\beta\_{22}-E\chi^{-}\right)-1\right] |  |

Group terms by state variables

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =∂tA+μ​B−σ22​(B2−B)+12​φ2​(t)​(E2−E)+κ+​θ+​ℒ(+)​(−χ+)​C+κ−​θ−​ℒ(−)​(−χ−)​D−B​E​σ​φ​(t)\displaystyle=\partial\_{t}A+\mu B-\frac{\sigma^{2}}{2}(B^{2}-B)+\frac{1}{2}\varphi^{2}(t)(E^{2}-E)+\kappa^{+}\theta^{+}\mathcal{L}^{(+)}(-\chi^{+})C+\kappa^{-}\theta^{-}\mathcal{L}^{(-)}(-\chi^{-})D-BE\sigma\varphi(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∂tB​x+∂tE​m\displaystyle+\partial\_{t}Bx+\partial\_{t}Em |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ+[ℒ(+)(−B−Cℒ(+)(−χ+)β11−Dℒ(−)(−χ−)β21−Eχ+)−1\displaystyle+\lambda^{+}\Big[\mathcal{L}^{(+)}\left(-B-C\mathcal{L}^{(+)}\left(-\chi^{+}\right)\beta\_{11}-D\mathcal{L}^{(-)}\left(-\chi^{-}\right)\beta\_{21}-E\chi^{+}\right)-1 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∂tCℒ(+)(−χ+)−𝔼(eJ+−1)B−κ1+(ξ+)κ+E−κ+ℒ(+)(−χ+)C]\displaystyle\phantom{+\lambda^{+}\Big[}+\partial\_{t}C\mathcal{L}^{(+)}(-\chi^{+})-{\mathbb{E}}\left(e^{J^{+}}-1\right)B-\kappa^{+}\_{1}(\xi^{+})\kappa^{+}E-\kappa^{+}\mathcal{L}^{(+)}(-\chi^{+})C\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ−[ℒ(−)(−B−Cℒ(+)(−χ+)β12−Dℒ(−)(−χ−)β22−Eχ−)−1\displaystyle+\lambda^{-}\Big[\mathcal{L}^{(-)}\left(-B-C\mathcal{L}^{(+)}\left(-\chi^{+}\right)\beta\_{12}-D\mathcal{L}^{(-)}\left(-\chi^{-}\right)\beta\_{22}-E\chi^{-}\right)-1 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∂tDℒ(−)(−χ−)−𝔼(eJ+−1)B−κ1−(ξ−)κ−E−κ−ℒ(−)(−χ−)D].\displaystyle\phantom{+\lambda^{+}\Big[}+\partial\_{t}D\mathcal{L}^{(-)}(-\chi^{-})-{\mathbb{E}}\left(e^{J^{+}}-1\right)B-\kappa^{-}\_{1}(\xi^{-})\kappa^{-}E-\kappa^{-}\mathcal{L}^{(-)}(-\chi^{-})D\Big]. |  |

Since the above equation holds for all value of state variables, x,λ+,λ−x,\ \lambda^{+},\ \lambda^{-}, we infer for t≤Tt\leq T, ∂tB​(t,T)=∂tE​(t,T)=0\partial\_{t}B(t,T)=\partial\_{t}E(t,T)=0, and thus B​(t,T)=ωB(t,T)=\omega and E​(t,T)=1E(t,T)=1.
The above equation becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =∂tA+μ​B−σ22​(ω2−ω)+κ+​θ+​ℒ(+)​(−χ+)​C+κ−​θ−​ℒ(−)​(−χ−)​D−ω​σ​φ​(t)\displaystyle=\partial\_{t}A+\mu B-\frac{\sigma^{2}}{2}(\omega^{2}-\omega)+\kappa^{+}\theta^{+}\mathcal{L}^{(+)}(-\chi^{+})C+\kappa^{-}\theta^{-}\mathcal{L}^{(-)}(-\chi^{-})D-\omega\sigma\varphi(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ+[ℒ(+)(−ω−Cℒ(+)(−χ+)β11−Dℒ(−)(−χ−)β21−χ+)−1\displaystyle+\lambda^{+}\Big[\mathcal{L}^{(+)}\left(-\omega-C\mathcal{L}^{(+)}\left(-\chi^{+}\right)\beta\_{11}-D\mathcal{L}^{(-)}\left(-\chi^{-}\right)\beta\_{21}-\chi^{+}\right)-1 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∂tCℒ(+)(−χ+)−𝔼(eJ+−1)ω−κ1+(ξ+)κ+−κ+ℒ(+)(−χ+)C]\displaystyle\phantom{+\lambda^{+}\Big[}+\partial\_{t}C\mathcal{L}^{(+)}(-\chi^{+})-{\mathbb{E}}\left(e^{J^{+}}-1\right)\omega-\kappa^{+}\_{1}(\xi^{+})\kappa^{+}-\kappa^{+}\mathcal{L}^{(+)}(-\chi^{+})C\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ−[ℒ(−)(−ω−Cℒ(+)(−χ+)β12−Dℒ(−)(−χ−)β22−χ−)−1\displaystyle+\lambda^{-}\Big[\mathcal{L}^{(-)}\left(-\omega-C\mathcal{L}^{(+)}\left(-\chi^{+}\right)\beta\_{12}-D\mathcal{L}^{(-)}\left(-\chi^{-}\right)\beta\_{22}-\chi^{-}\right)-1 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∂tDℒ(−)(−χ−)−𝔼(eJ+−1)ω−κ1−(ξ−)κ−−κ−ℒ(−)(−χ−)D].\displaystyle\phantom{+\lambda^{+}\Big[}+\partial\_{t}D\mathcal{L}^{(-)}(-\chi^{-})-{\mathbb{E}}\left(e^{J^{+}}-1\right)\omega-\kappa^{-}\_{1}(\xi^{-})\kappa^{-}-\kappa^{-}\mathcal{L}^{(-)}(-\chi^{-})D\Big]. |  |

Recall we choose the ℱt\mathcal{F}\_{t}-adapted process as φ​(t)=φ+φ+​λt++φ−​λt−\varphi(t)=\varphi+\varphi^{+}\lambda^{+}\_{t}+\varphi^{-}\lambda^{-}\_{t}, so expanding the φ​(t)\varphi(t) term in the above equation gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =∂tA+μ​ω+σ22​(ω2−ω)+κ+​θ+​ℒ(+)​(−χ+)​C+κ−​θ−​ℒ(−)​(−χ−)​D−ω​σ​φ\displaystyle=\partial\_{t}A+\mu\omega+\frac{\sigma^{2}}{2}(\omega^{2}-\omega)+\kappa^{+}\theta^{+}\mathcal{L}^{(+)}(-\chi^{+})C+\kappa^{-}\theta^{-}\mathcal{L}^{(-)}(-\chi^{-})D-\omega\sigma\varphi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ+[ℒ(+)(−ω−Cℒ(+)(−χ+)β11−Dℒ(−)(−χ−)β21−χ+)−1\displaystyle+\lambda^{+}\big[\mathcal{L}^{(+)}\left(-\omega-C\mathcal{L}^{(+)}\left(-\chi^{+}\right)\beta\_{11}-D\mathcal{L}^{(-)}\left(-\chi^{-}\right)\beta\_{21}-\chi^{+}\right)-1 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∂tCℒ(+)(−χ+)−𝔼(eJ+−1)ω−κ1+(ξ+)κ+−κ+ℒ(+)(−χ+)C−ωσφ+]\displaystyle\phantom{+\lambda^{+}\Big[}+\partial\_{t}C\mathcal{L}^{(+)}(-\chi^{+})-{\mathbb{E}}\left(e^{J^{+}}-1\right)\omega-\kappa^{+}\_{1}(\xi^{+})\kappa^{+}-\kappa^{+}\mathcal{L}^{(+)}(-\chi^{+})C-\omega\sigma\varphi^{+}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ−[ℒ(−)(−ω−Cℒ(+)(−χ+)β12−Dℒ(−)(−χ−)β22−χ−)−1\displaystyle+\lambda^{-}\big[\mathcal{L}^{(-)}\left(-\omega-C\mathcal{L}^{(+)}\left(-\chi^{+}\right)\beta\_{12}-D\mathcal{L}^{(-)}\left(-\chi^{-}\right)\beta\_{22}-\chi^{-}\right)-1 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∂tDℒ(−)(−χ−)−𝔼(eJ+−1)ω−κ1−(ξ−)κ−−κ−ℒ(−)(−χ−)D−ωσφ−]\displaystyle\phantom{+\lambda^{+}\Big[}+\partial\_{t}D\mathcal{L}^{(-)}(-\chi^{-})-{\mathbb{E}}\left(e^{J^{+}}-1\right)\omega-\kappa^{-}\_{1}(\xi^{-})\kappa^{-}-\kappa^{-}\mathcal{L}^{(-)}(-\chi^{-})D-\omega\sigma\varphi^{-}\big] |  |

The above equation holds for all values of state variables. Together with the parameter changes stated in Proposition [4](https://arxiv.org/html/2510.21297v1#Thmlemma4 "Proposition 4 (Jump intensity dynamics under the risk-neutral measure ℚ ). ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tA\displaystyle\partial\_{t}A | =−(μ−σ​φ)​ω−σ22​(ω2−ω)−κ+​θ+,ℚ​C−κ−​θ−,ℚ​D\displaystyle=-(\mu-\sigma\varphi)\omega-\frac{\sigma^{2}}{2}(\omega^{2}-\omega)-\kappa^{+}\theta^{+,\mathbb{Q}}C-\kappa^{-}\theta^{-,\mathbb{Q}}D |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tC\displaystyle\partial\_{t}C | =−ℒ+,ℚ​(−ω−C​β11ℚ−D​β21ℚ−χ+)+1+𝔼​(eJ+−1)+σ​φ+ℒ(+)​(−χ+)​ω+κ+​C\displaystyle=-\mathcal{L}^{+,\mathbb{Q}}(-\omega-C\beta^{\mathbb{Q}}\_{11}-D\beta^{\mathbb{Q}}\_{21}-\chi^{+})+1+\frac{{\mathbb{E}}\left(e^{J^{+}}-1\right)+\sigma\varphi^{+}}{\mathcal{L}^{(+)}(-\chi^{+})}\omega+\kappa^{+}C |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tD\displaystyle\partial\_{t}D | =−ℒ−,ℚ​(−ω−C​β21ℚ−D​β22ℚ−χ−)+1+𝔼​(eJ−−1)+σ​φ−ℒ(−)​(−χ−)​ω+κ−​D\displaystyle=-\mathcal{L}^{-,\mathbb{Q}}(-\omega-C\beta^{\mathbb{Q}}\_{21}-D\beta^{\mathbb{Q}}\_{22}-\chi^{-})+1+\frac{{\mathbb{E}}\left(e^{J^{-}}-1\right)+\sigma\varphi^{-}}{\mathcal{L}^{(-)}(-\chi^{-})}\omega+\kappa^{-}D |  |

By choosing

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ\displaystyle\varphi | =σ−1​(μ−r),\displaystyle=\sigma^{-1}(\mu-r), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | φ+\displaystyle\varphi^{+} | =σ−1​[ℒ(+)​(−χ+)​𝔼ℚ​(eJ+−1)−𝔼​(eJ+−1)],\displaystyle=\sigma^{-1}\left[\mathcal{L}^{(+)}(-\chi^{+}){\mathbb{E}}^{\mathbb{Q}}\left(e^{J^{+}}-1\right)-{\mathbb{E}}\left(e^{J^{+}}-1\right)\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | φ−\displaystyle\varphi^{-} | =σ−1​[ℒ(+)​(−χ+)​𝔼ℚ​(eJ−−1)−𝔼​(eJ−−1)],\displaystyle=\sigma^{-1}\left[\mathcal{L}^{(+)}(-\chi^{+}){\mathbb{E}}^{\mathbb{Q}}\left(e^{J^{-}}-1\right)-{\mathbb{E}}\left(e^{J^{-}}-1\right)\right], |  |

the MGF of {Xt}t≥0\left\{X\_{t}\right\}\_{t\geq 0} under measure ℚ\mathbb{Q} can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​(eω​XT|ℱt)\displaystyle{\mathbb{E}}^{\mathbb{Q}}\left(e^{\omega X\_{T}}\big|\mathcal{F}\_{t}\right) | =exp⁡(A​(t,T)+ω​x+C​(t,T)​ℒ(+)​(−χ+)​λt++D​(t,T)​ℒ(−)​(−χ−)​λt−)\displaystyle=\exp\left(A(t,T)+\omega x+C(t,T)\mathcal{L}^{(+)}(-\chi^{+})\lambda^{+}\_{t}+D(t,T)\mathcal{L}^{(-)}(-\chi^{-})\lambda^{-}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(A​(t,T)+ω​x+C​(t,T)​λt+,ℚ+D​(t,T)​λt−,ℚ),\displaystyle=\exp\left(A(t,T)+\omega x+C(t,T)\lambda^{+,\mathbb{Q}}\_{t}+D(t,T)\lambda^{-,\mathbb{Q}}\_{t}\right), |  |

where the functions AA, CC, and DD solve the following system of PDEs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tA​(t,T)\displaystyle\partial\_{t}A(t,T) | =−r​ω−σ22​(ω2−ω)−κ+​θ+,ℚ​C​(t,T)−κ−​θ−,ℚ​D​(t,T)\displaystyle=-r\omega-\frac{\sigma^{2}}{2}(\omega^{2}-\omega)-\kappa^{+}\theta^{+,\mathbb{Q}}C(t,T)-\kappa^{-}\theta^{-,\mathbb{Q}}D(t,T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tC​(t,T)\displaystyle\partial\_{t}C(t,T) | =−ℒ+,ℚ​(−ω−C​(t,T)​β11ℚ−D​(t,T)​β21ℚ−χ+)+1+𝔼ℚ​(eJ+−1)​ω+κ+​C​(t,T)\displaystyle=-\mathcal{L}^{+,\mathbb{Q}}(-\omega-C(t,T)\beta^{\mathbb{Q}}\_{11}-D(t,T)\beta^{\mathbb{Q}}\_{21}-\chi^{+})+1+{\mathbb{E}}^{\mathbb{Q}}\left(e^{J^{+}}-1\right)\omega+\kappa^{+}C(t,T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tD​(t,T)\displaystyle\partial\_{t}D(t,T) | =−ℒ−,ℚ​(−ω−C​(t,T)​β21ℚ−D​(t,T)​β22ℚ−χ−)+1+𝔼ℚ​(eJ−−1)​ω+κ−​D​(t,T).\displaystyle=-\mathcal{L}^{-,\mathbb{Q}}(-\omega-C(t,T)\beta^{\mathbb{Q}}\_{21}-D(t,T)\beta^{\mathbb{Q}}\_{22}-\chi^{-})+1+{\mathbb{E}}^{\mathbb{Q}}\left(e^{J^{-}}-1\right)\omega+\kappa^{-}D(t,T). |  |

Finally, by comparing the above MGF under ℚ\mathbb{Q} to that under ℙ\mathbb{P} stated in Proposition [1](https://arxiv.org/html/2510.21297v1#Thmlemma1 "Proposition 1. ‣ 2.2 Moment-generating function of joint dynamics ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps"), we conclude that the dynamics of the log returns {Xt}t≥0\left\{X\_{t}\right\}\_{t\geq 0} under measure ℚ\mathbb{Q} can be retrieved by the substitution of model parameters stated in Eq.[29](https://arxiv.org/html/2510.21297v1#S2.E29 "In Corollary 2 (MGF in Proposition 1 under ℚ). ‣ 2.3 Equivalent risk-neutral measure ℚ ‣ 2 Model specification ‣ Jump risk premia in the presence of clustered jumps").

### A.6 Derivation of the likelihood

Suppose we observe k−1k-1 jump events and collect the following:

* •

  positive and negative jump event times 𝒯+={T[1]+,T[2]+,…,Tm+}\mathcal{T}^{+}=\left\{T^{+}\_{[1]},T^{+}\_{[2]},...,T^{+}\_{m}\right\} and 𝒯−={T[1]−,T[2]−​…,T[n]−}\mathcal{T}^{-}=\left\{T^{-}\_{[1]},T^{-}\_{[2]}...,T^{-}\_{[n]}\right\} respectively,
* •

  the corresponding jump sizes of positive and negative jump events {J+​(T[1]+),J+​(T[2]+),…,J+​(T[m]+)}\left\{J^{+}(T^{+}\_{[1]}),J^{+}(T^{+}\_{[2]}),...,J^{+}(T^{+}\_{[m]})\right\} and {J−​(T[1]−),J−​(T[2]−),…,J−​(T[n]−)}\left\{J^{-}(T^{-}\_{[1]}),J^{-}(T^{-}\_{[2]}),...,J^{-}(T^{-}\_{[n]})\right\} respectively, and,
* •

  a set of ordered set of union jump times 𝒯±=𝒯+∪𝒯−={T[1]±,T[2]±,…,T[k−1]±}\mathcal{T}^{\pm}=\mathcal{T}^{+}\cup\mathcal{T}^{-}=\left\{T^{\pm}\_{[1]},T^{\pm}\_{[2]},...,T^{\pm}\_{[k-1]}\right\},

the hazard rate of observing the kthk^{\text{th}} jump between time T[k−1]±T^{\pm}\_{[k-1]} and s>T[k−1]±s>T^{\pm}\_{[k-1]} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | F±​(s|T[k−1]±)\displaystyle F^{\pm}\big(s\big|T^{\pm}\_{[k-1]}\big) | =1−exp⁡(−∫T[k−1]±s(λt++λt−)​dt)\displaystyle=1-\exp\left(-\int\_{T^{\pm}\_{[k-1]}}^{s}(\lambda^{+}\_{t}+\lambda^{-}\_{t}){\rm d}t\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1−exp⁡(−I+​(T[k−1]±,s)−I−​(T[k−1]±,s)),\displaystyle=1-\exp\left(-I^{+}(T^{\pm}\_{[k-1]},s)-I^{-}(T^{\pm}\_{[k-1]},s)\right), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | I+​(T[k−1]±,s)\displaystyle I^{+}(T^{\pm}\_{[k-1]},s) | =∫T[k−1]±sλt+​dt=θ+​(s−T[k−1]±)+(λ+​(T[k−1]±)−θ+)​1−e−κ+​(s−T[k−1]±)κ+\displaystyle=\int\_{T^{\pm}\_{[k-1]}}^{s}\lambda^{+}\_{t}{\rm d}t=\theta^{+}(s-T^{\pm}\_{[k-1]})+(\lambda^{+}(T^{\pm}\_{[k-1]})-\theta^{+})\frac{1-e^{-\kappa^{+}(s-T^{\pm}\_{[k-1]})}}{\kappa^{+}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | I−​(T[k−1]±,s)\displaystyle I^{-}(T^{\pm}\_{[k-1]},s) | =∫T[k−1]±sλt−​dt=θ+​(s−T[k−1]±)+(λ−​(T[k−1]±)−θ+)​1−e−κ−​(s−T[k−1]±)κ−.\displaystyle=\int\_{T^{\pm}\_{[k-1]}}^{s}\lambda^{-}\_{t}{\rm d}t=\theta^{+}(s-T^{\pm}\_{[k-1]})+(\lambda^{-}(T^{\pm}\_{[k-1]})-\theta^{+})\frac{1-e^{-\kappa^{-}(s-T^{\pm}\_{[k-1]})}}{\kappa^{-}}. |  |

The pds of the inter-arrival time given the (k−1)th(k-1)^{\text{th}} jump is

|  |  |  |
| --- | --- | --- |
|  | f±​(s|T[k−1]±)=(λs++λs−)​exp⁡(−I+−I−).\displaystyle f^{\pm}\big(s\big|T^{\pm}\_{[k-1]}\big)=(\lambda^{+}\_{s}+\lambda^{-}\_{s})\exp(-I^{+}-I^{-}). |  |

Suppose the next jump happens at time T[k]±T^{\pm}\_{[k]}, the probability of this jump being a positive jump is

|  |  |  |
| --- | --- | --- |
|  | ℙ​(d​N(1)​(s)=1|s=T[k]±)=λ+​(T[k]±−)λ+​(T[k]±−)+λ−​(T[k]±−),\displaystyle\mathbb{P}\left({\rm d}N^{(1)}(s)=1\big|s=T^{\pm}\_{[k]}\right)=\frac{\lambda^{+}(T^{\pm}\_{[k]}-)}{\lambda^{+}(T^{\pm}\_{[k]}-)+\lambda^{-}(T^{\pm}\_{[k]}-)}, |  |

where d​N(1)​(s)=N(1)​(s)−N(1)​(s−){\rm d}N^{(1)}(s)=N^{(1)}(s)-N^{(1)}(s-);
And similarly for negative jump

|  |  |  |
| --- | --- | --- |
|  | ℙ​(d​N(2)​(s)=1|s=T[k]±)=λ−​(T[k]±−)λ+​(T[k]±−)+λ−​(T[k]±−).\displaystyle\mathbb{P}\left({\rm d}N^{(2)}(s)=1\big|s=T^{\pm}\_{[k]}\right)=\frac{\lambda^{-}(T^{\pm}\_{[k]}-)}{\lambda^{+}(T^{\pm}\_{[k]}-)+\lambda^{-}(T^{\pm}\_{[k]}-)}. |  |

Accordingly, the pdf of a positive jump occurring at time ss is

|  |  |  |
| --- | --- | --- |
|  | f+​(s|T[k−1]±)=f±​(s|T[k−1]±)​ℙ​(d​N(1)​(s)=1|s=T[k]±)=λs+​exp⁡(−I+−I−),\displaystyle f^{+}\big(s\big|T^{\pm}\_{[k-1]}\big)=f^{\pm}\big(s\big|T^{\pm}\_{[k-1]}\big)\mathbb{P}\left({\rm d}N^{(1)}(s)=1\big|s=T^{\pm}\_{[k]}\right)=\lambda^{+}\_{s}\exp(-I^{+}-I^{-}), |  |

and similarly for that of a negative jump

|  |  |  |
| --- | --- | --- |
|  | f−​(s|T[k−1]±)=λs−​exp⁡(−I+−I−).\displaystyle f^{-}\big(s\big|T^{\pm}\_{[k-1]}\big)=\lambda^{-}\_{s}\exp(-I^{+}-I^{-}). |  |

Therefore, the likelihood function of {λt+}t≤T[k−1]±\left\{\lambda^{+}\_{t}\right\}\_{t\leq T^{\pm}\_{[k-1]}}, {λt−}t≤T[k−1]±\left\{\lambda^{-}\_{t}\right\}\_{t\leq T^{\pm}\_{[k-1]}},
and the jumps sizes densities ϖ+\varpi^{+} and ϖ−\varpi^{-} to the observed inter-arrival times is

|  |  |  |
| --- | --- | --- |
|  | ℙ​(𝒯+,𝒯−|{λt+}t≤T[k−1]±,{λt−}t≤T[k−1]±,ϖ+,ϖ−)\displaystyle\mathbb{P}\left(\mathcal{T}^{+},\mathcal{T}^{-}\big|\left\{\lambda^{+}\_{t}\right\}\_{t\leq T^{\pm}\_{[k-1]}},\left\{\lambda^{-}\_{t}\right\}\_{t\leq T^{\pm}\_{[k-1]}},\varpi^{+},\varpi^{-}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =∏j=1mλ+​(T[m]+)​ϖ+​(J−​(T[m]+))\displaystyle=\prod\_{j=1}^{m}\lambda^{+}(T^{+}\_{[m]})\varpi^{+}(J^{-}(T^{+}\_{[m]})) |  |
|  |  |  |
| --- | --- | --- |
|  | ×∏j=1nλ−(T[n]−)ϖ−(J−(T[n]−))\displaystyle\times\prod\_{j=1}^{n}\lambda^{-}(T^{-}\_{[n]})\varpi^{-}(J^{-}(T^{-}\_{[n]})) |  |
|  |  |  |
| --- | --- | --- |
|  | ×∏j=1k−1exp(−I+(T[j]±,T[j−1]±)−I−(T[j]±,T[j−1]±)).\displaystyle\times\prod\_{j=1}^{k-1}\exp\left(-I^{+}(T^{\pm}\_{[j]},T^{\pm}\_{[j-1]})-I^{-}(T^{\pm}\_{[j]},T^{\pm}\_{[j-1]})\right). |  |

## Appendix B Goodness of fit assessment by Q-Q plot

Our assessment relies on the work by Watanabe ([1964](https://arxiv.org/html/2510.21297v1#bib.bib47)) who states that a Poisson process can be characterized by the form of its compensator, Λ​(T)=∫0Tλ​(t)​d​t\Lambda(T)=\int\_{0}^{T}\lambda(t)\text{d}t.
This characterisation is later on known as the random time change theorem, see Section 7.4 of (Daley and
Vere-Jones, [2003](https://arxiv.org/html/2510.21297v1#bib.bib17)) and reference therein.
We rewrite the multivariate random time change theorem stated in Section 9.3 of Laub
et al. ([2021](https://arxiv.org/html/2510.21297v1#bib.bib35)) in a bidimentional version to suit our purpose here.

###### Proposition 6.

Bidimensional random time change. (Theorem 9.3 of Laub
et al. ([2021](https://arxiv.org/html/2510.21297v1#bib.bib35)))
  
Suppose we observe two counting processes, N(1)​(t)N^{(1)}(t) and N(2)​(t)N^{(2)}(t), which are characterised by intensities λt+\lambda^{+}\_{t} and λt−\lambda^{-}\_{t}, respectively.
The event arrival times of the two counting processes are labelled as
{T1(1),T2(1),…}​ and ​{T1(2),T2(2),…}\left\{T^{(1)}\_{1},\ T^{(1)}\_{2},...\right\}\text{ and }\left\{T^{(2)}\_{1},\ T^{(2)}\_{2},...\right\}.
In addition, suppose λt=λt++λt−\lambda\_{t}=\lambda^{+}\_{t}+\lambda^{-}\_{t} is positive over [0,T][0,\ T] and
∫0Tλ​(t)​d​t<∞\int\_{0}^{T}\lambda(t)\text{d}t<\infty almost surely, then the transformed event arrival times

|  |  |  |
| --- | --- | --- |
|  | {∫0T1(1)λt+​d​t,∫0T2(1)λt+​d​t,…}​ and ​{∫0T1(2)λt−​d​t,∫0T2(2)λt−​d​t,…}\left\{\int\_{0}^{T^{(1)}\_{1}}\lambda^{+}\_{t}\text{d}t,\ \int\_{0}^{T^{(1)}\_{2}}\lambda^{+}\_{t}\text{d}t,...\right\}\text{ and }\left\{\int\_{0}^{T^{(2)}\_{1}}\lambda^{-}\_{t}\text{d}t,\ \int\_{0}^{T^{(2)}\_{2}}\lambda^{-}\_{t}\text{d}t,...\right\} |  |

are events arrival times of two Poisson processes with unit rate.

In order words, the transformed events inter-arrival times,

|  |  |  |
| --- | --- | --- |
|  | {∫0T1(1)λt+​d​t,∫T1(1)T2(1)λt+​d​t,∫T2(1)T3(1)λt+​d​t,…}​ and\displaystyle\left\{\int\_{0}^{T^{(1)}\_{1}}\lambda^{+}\_{t}\text{d}t,\ \int\_{T^{(1)}\_{1}}^{T^{(1)}\_{2}}\lambda^{+}\_{t}\text{d}t,\ \int\_{T^{(1)}\_{2}}^{T^{(1)}\_{3}}\lambda^{+}\_{t}\text{d}t,...\right\}\text{ and } |  |
|  |  |  |
| --- | --- | --- |
|  | {∫0T1(2)λt−​d​t,∫T1(2)T2(2)λt−​d​t,∫T2(2)T3(2)λt−​d​t,…}\displaystyle\left\{\int\_{0}^{T^{(2)}\_{1}}\lambda^{-}\_{t}\text{d}t,\ \int\_{T^{(2)}\_{1}}^{T^{(2)}\_{2}}\lambda^{-}\_{t}\text{d}t,\ \int\_{T^{(2)}\_{2}}^{T^{(2)}\_{3}}\lambda^{-}\_{t}\text{d}t,...\right\} |  |

are two random variables that follows exponential distribution with unit rate.
Note that the event of N(2)N^{(2)} can arrive between two events of N(1)N^{(1)} and vice versa, e.g. it is possible that
Tk(1)<Tj(2)<Tk+1(1)T^{(1)}\_{k}<T^{(2)}\_{j}<T^{(1)}\_{k+1} for some integers kk and jj.
The random time change theorem enables us to perform residual analysis to assess the goodness-of-fit of time-inhomogeneous Poisson processes.

###### Theorem 1.

Consider an unbounded, increasing sequence of time points {t1,t2,…}\{t\_{1},\ t\_{2},\ ...\} in (0,∞)(0,\ \infty), and a monotone, continuous function
Λ​(⋅)\Lambda(\cdot) such that limt→∞Λ​(t)=∞\lim\_{t\rightarrow\infty}\Lambda(t)=\infty almost surely.
The transformed sequence {Λ​(t1),Λ​(t2),…}\{\Lambda(t\_{1}),\ \Lambda(t\_{2}),\ ...\} is a realisation of a unit rate Poisson process if and only if the original sequence {t1,t2,…}\{t\_{1},\ t\_{2},\ ...\}
is a realisation from the point process characterised by Λ​(⋅)\Lambda(\cdot).

###### Proof.

See Brown and
Nair ([1988](https://arxiv.org/html/2510.21297v1#bib.bib13)).
∎

We refer readers to Section 9 of Laub
et al. ([2021](https://arxiv.org/html/2510.21297v1#bib.bib35)) for further details regarding the application of random time change theorem on Hawkes processes.