---
authors:
- Johannes Muhle-Karbe
- Youssef Ouazzani Chahdi
- Mathieu Rosenbaum
- Grégoire Szymanski
doc_id: arxiv:2601.23172v2
family_id: arxiv:2601.23172
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A unified theory of order flow, market impact, and volatility1footnote 11footnote
  1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge
  support from the ILB Chair Artificial Intelligence and Quantitative Methods for
  Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and
  Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also
  grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on
  order flow modeling, and thank BMLL Technologies for providing the historical market
  data used in this study.
url_abs: http://arxiv.org/abs/2601.23172v2
url_html: https://arxiv.org/html/2601.23172v2
venue: arXiv q-fin
version: 2
year: 2026
---


Johannes Muhle-Karbe222Department of Mathematics, Imperial College London,
j.muhle-karbe@imperial.ac.uk
  
Youssef Ouazzani Chahdi333MICS, CentraleSupélec, youssef.ouazzani-chahdi@centralesupelec.fr
  
Mathieu Rosenbaum444Ceremade, Université Paris Dauphine-PSL, mathieu.rosenbaum@dauphine.psl.eu
  
Grégoire Szymanski555DMATH, Université du Luxembourg, gregoire.szymanski@uni.lu

###### Abstract

We propose a microstructural model for the order flow in financial markets that distinguishes between core orders and reaction flow, both modeled as Hawkes processes. This model has a natural scaling limit that reconciles a number of salient empirical properties: persistent signed order flow, rough trading volume and volatility, and power-law market impact. In our framework, all these quantities are pinned down by a single statistic H0H\_{0}, which measures the persistence of the core flow. Specifically, the signed flow converges to the sum of a fractional process with Hurst index H0H\_{0} and a martingale, while the limiting traded volume is a rough process with Hurst index H0−1/2H\_{0}-1/2. No-arbitrage constraints imply that volatility is rough, with Hurst parameter 2​H0−3/22H\_{0}-3/2, and that the price impact of trades follows a power law with exponent 2−2​H02-2H\_{0}.
The analysis of signed order flow data yields an estimate H0≈3/4H\_{0}\approx 3/4. This is not only consistent with the square-root law of market impact, but also turns out to match estimates for the roughness of traded volumes and volatilities remarkably well.

Keywords: Trading volume, order flow, core order flow, rough volatility, market impact, long memory, market microstructure, Hawkes processes, mixed fractional Brownian motion, limit theorems, criticality.

Mathematics Subject Classification (2020): 60F05, 60G22, 60G55, 62P05, 91G15, 91G80

## 1 Introduction

Prices and traded quantities are the fundamental observables in any financial market. In a vast body of research initiated by Bachelier [[1](https://arxiv.org/html/2601.23172v2#bib.bib43 "Théorie de la spéculation")] and Black and Scholes [[8](https://arxiv.org/html/2601.23172v2#bib.bib93 "The pricing of options and corporate liabilities")], (semi-)martingales have emerged as the canonical model for asset prices, reflecting the absence of arbitrage and limited predictability of returns. In contrast, there is no similar standard model class for the corresponding order flow yet. A key challenge is that any such model must at the same time capture the stylized properties of traded amounts (“unsigned volumes”) and their directionality (“signed order flow”). Moreover, through the price impact of trades, order flow and price dynamics are intimately linked. A consistent model for the order flow therefore must strike a delicate balance to consistently connect the salient features of several distinct datasets. The present study sets out to do this in a principled yet parsimonious manner.

To explain more clearly what is the challenge at hand, let us first briefly review some of the statistical regularities of order flow data that are very robust across different markets, assets, and time periods:

* ∙\bullet

  Persistent order flow.
  The signed order flow exhibits significant persistence and long memory, commonly attributed to order splitting, sustained trading programs, and long-lived trading motives [[49](https://arxiv.org/html/2601.23172v2#bib.bib402 "Trading volume: definitions, data analysis, and implications of portfolio theory"), [47](https://arxiv.org/html/2601.23172v2#bib.bib455 "The long memory of the efficient market"), [10](https://arxiv.org/html/2601.23172v2#bib.bib10 "How markets slowly digest changes in supply and demand"), [48](https://arxiv.org/html/2601.23172v2#bib.bib660 "Theory for long memory in supply and demand"), [26](https://arxiv.org/html/2601.23172v2#bib.bib229 "Market efficiency and the long-memory of supply and demand: is price impact variable and permanent or fixed and temporary?"), [57](https://arxiv.org/html/2601.23172v2#bib.bib382 "Inferring microscopic financial information from the long memory in market-order flow: a quantitative test of the Lillo-Mike-Farmer model")]. Its sample paths also display a markedly smoother behavior than Brownian motion on longer timescales, cf. Figure [1](https://arxiv.org/html/2601.23172v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* ∙\bullet

  Rough traded volume.
  In contrast, the unsigned traded amounts have a much rougher temporal structure, cf. Figure [2](https://arxiv.org/html/2601.23172v2#S1.F2 "Figure 2 ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), in line with the “rough volatility models” introduced by [[29](https://arxiv.org/html/2601.23172v2#bib.bib271 "Volatility is rough")]. The similarity between trading activity and integrated variance is well established [[43](https://arxiv.org/html/2601.23172v2#bib.bib398 "The relation between price changes and trading volume: a survey"), [52](https://arxiv.org/html/2601.23172v2#bib.bib573 "Why do security prices change? A transaction-level analysis of NYSE stocks"), [63](https://arxiv.org/html/2601.23172v2#bib.bib574 "Relation between bid–ask spread, impact and volatility in order-driven markets"), [22](https://arxiv.org/html/2601.23172v2#bib.bib109 "Large tick assets: implicit spread and optimal tick size"), [44](https://arxiv.org/html/2601.23172v2#bib.bib325 "Market microstructure invariance: empirical hypotheses")], but raises the question how signed flow and unsigned volumes can be modeled consistently. Indeed, persistent order flow naturally suggests models driven by fractional Brownian motions with Hurst indices way above 1/21/2, reflecting long-range dependence. In contrast, rough volatility and unsigned volume are best captured by fractional processes with Hurst indices far below 1/21/2.

![Refer to caption](x1.png)


Figure 1: Cumulative signed order flow of the representative stock LVMH between 2021 and 2024.

![Refer to caption](x2.png)


Figure 2: Daily traded volume of the representative stock LVMH between 2021 and 2024.

This modeling challenge is exacerbated by the multiscale behavior of the signed order flow. This is illustrated in Figure [3](https://arxiv.org/html/2601.23172v2#S1.F3 "Figure 3 ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), which reports Hurst parameter estimates for the signed order flow sampled at different frequencies. At high frequencies, the estimates are close to 0.50.5, consistent with diffusive models [[32](https://arxiv.org/html/2601.23172v2#bib.bib3 "Dynamic trading volume"), [12](https://arxiv.org/html/2601.23172v2#bib.bib2 "The self-financing equation in limit order book markets")].
As the sampling frequency decreases, estimated Hurst exponents increase steadily and reach values around 0.650.65 when sampling hourly, in line with smooth fractional models. This suggests that no “pure” fractional Brownian motion model adequately captures the dynamics of the order flow.

![Refer to caption](x3.png)


Figure 3: Average Hurst exponent estimates for signed order flow over 40 stocks for the period 2021–2024, under fractional Brownian motion specification.
  
Note: The data used for the estimations throughout the paper are described in Appendix [C](https://arxiv.org/html/2601.23172v2#A3 "Appendix C Data description and stock universe ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").

Moreover, as already alluded to above, a consistent model for the order flow must not only recapture its own empirical properties but, via the price impact of trades, also remain consistent with price dynamics. More specifically, when prices are (close to) martingales and permanent price impact is linear to preclude statistical arbitrage [[37](https://arxiv.org/html/2601.23172v2#bib.bib356 "Price manipulation and quasi-arbitrage"), [30](https://arxiv.org/html/2601.23172v2#bib.bib268 "No-dynamic-arbitrage and market impact"), [61](https://arxiv.org/html/2601.23172v2#bib.bib597 "Anomalous price impact and the critical nature of liquidity in financial markets"), [27](https://arxiv.org/html/2601.23172v2#bib.bib230 "How efficiency shapes market impact"), [23](https://arxiv.org/html/2601.23172v2#bib.bib211 "A fully consistent, minimal model for non-linear market impact"), [4](https://arxiv.org/html/2601.23172v2#bib.bib76 "Market impact with multi-timescale liquidity")], then the expected future order flow also pins down prices and their volatility, as well as the price impact decay kernel that describes how the impact of each trade dissipates over time [[42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")].

Any consistent model for the order flow therefore must be consistent with the large bodies of evidence accumulated for the universal scaling properties of price volatility and price impact:

* ∙\bullet

  Rough volatility. As indicated above, volatility time series exhibit very rough sample paths. Across a very wide range of markets, this leads to estimates for Hurst parameters in a range between 0.050.05 and 0.150.15 [[29](https://arxiv.org/html/2601.23172v2#bib.bib271 "Volatility is rough"), [17](https://arxiv.org/html/2601.23172v2#bib.bib162 "Statistical inference for rough volatility: Minimax theory"), [9](https://arxiv.org/html/2601.23172v2#bib.bib110 "A GMM approach to estimate the roughness of stochastic volatility"), [19](https://arxiv.org/html/2601.23172v2#bib.bib56 "A nonparametric test for rough volatility"), [59](https://arxiv.org/html/2601.23172v2#bib.bib108 "Fractional Gaussian noise: spectral density and estimation methods"), [33](https://arxiv.org/html/2601.23172v2#bib.bib96 "On the rate of convergence of estimating the Hurst parameter of rough stochastic volatility models")].666The rough volatility paradigm sheds new light on important volatility features such as long memory [[50](https://arxiv.org/html/2601.23172v2#bib.bib399 "Long-term memory in stock market prices"), [21](https://arxiv.org/html/2601.23172v2#bib.bib176 "Long memory continuous time models"), [3](https://arxiv.org/html/2601.23172v2#bib.bib75 "Decoupling the short and long term behavior of stochastic volatility"), [45](https://arxiv.org/html/2601.23172v2#bib.bib53 "Weak identification of long memory with implications for volatility modeling")], and motivates a new generation of stochastic volatility models.
  These developments have profoundly reshaped both theoretical modeling and practical applications, with notable implications for derivatives pricing [[2](https://arxiv.org/html/2601.23172v2#bib.bib68 "Pricing under rough volatility")] and volatility forecasting [[29](https://arxiv.org/html/2601.23172v2#bib.bib271 "Volatility is rough"), [3](https://arxiv.org/html/2601.23172v2#bib.bib75 "Decoupling the short and long term behavior of stochastic volatility"), [62](https://arxiv.org/html/2601.23172v2#bib.bib344 "On the optimal forecast with the fractional Brownian motion")].
* ∙\bullet

  Universal market impact scaling.
  The average price response to a large order follows a remarkably stable scaling law: impact grows approximately as the square root of the traded size [[51](https://arxiv.org/html/2601.23172v2#bib.bib400 "Trading cost: the critical link between investment information and results"), [11](https://arxiv.org/html/2601.23172v2#bib.bib658 "Fluctuations and response in financial markets: the subtle nature of ‘random’ price changes"), [61](https://arxiv.org/html/2601.23172v2#bib.bib597 "Anomalous price impact and the critical nature of liquidity in financial markets"), [6](https://arxiv.org/html/2601.23172v2#bib.bib81 "The non-linear market impact of large trades: Evidence from buy-side order flow"), [28](https://arxiv.org/html/2601.23172v2#bib.bib401 "Trading costs"), [58](https://arxiv.org/html/2601.23172v2#bib.bib52 "Strict universality of the square-root law in price impact across stocks: a complete survey of the Tokyo stock exchange")]. This empirical regularity again appears largely invariant across markets and trading regimes.

In the present study, we build a unifying model that reconciles all of these empirical facts in a consistent yet extremely parsimonious manner. Our analysis is based on a two-layer model for the order flow that distinguishes between core flow and reaction flow. Core flow captures autonomous trading activity arising from slow-moving investment decisions, portfolio rebalancing, or fundamental information.777Note that the idea of a component of order flow that is insensitive to contemporaneous trading activity is also at the heart of [[48](https://arxiv.org/html/2601.23172v2#bib.bib660 "Theory for long memory in supply and demand")], a paper whose conclusions have recently been empirically confirmed in [[57](https://arxiv.org/html/2601.23172v2#bib.bib382 "Inferring microscopic financial information from the long memory in market-order flow: a quantitative test of the Lillo-Mike-Farmer model")]. The reaction flow, by contrast, represents responses to observed market activity, including liquidity provision, market making, and high-frequency trading. Both layers are modeled using Hawkes processes, following a now widely-used and empirically well-supported approach in market microstructure [[39](https://arxiv.org/html/2601.23172v2#bib.bib387 "Limit theorems for nearly unstable Hawkes processes"), [40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes"), [36](https://arxiv.org/html/2601.23172v2#bib.bib346 "The microstructure of stochastic volatility models with self-exciting jump dynamics")]. This modeling choice is not motivated by behavioral assumptions but primarily by statistical adequacy: Hawkes dynamics reproduce with remarkable accuracy the clustering, persistence and scaling properties of order arrivals observed in markets.888A closely related line of work is developed in [[53](https://arxiv.org/html/2601.23172v2#bib.bib29 "The subtle interplay between square-root impact, order imbalance & volatility: a unifying framework"), [54](https://arxiv.org/html/2601.23172v2#bib.bib379 "The subtle interplay between square-root impact, order imbalance & volatility II: an artificial market generator"), [55](https://arxiv.org/html/2601.23172v2#bib.bib381 "Why is the estimation of metaorder impact with public market data so challenging?")], where detailed models of metaorders and generalized propagator frameworks are constructed to reconcile long memory in order flow with price diffusivity and square-root impact. Our approach is complementary: rather than modeling the fine structure of individual metaorders, we adopt a reduced-form, statistical perspective focused on aggregate trading flows and their scaling limits.

While the resulting microstructural model is flexible enough to fit a wide range of empirical features, it a priori involves many degrees of freedom. Our key insight is that imposing the existence of a non-degenerate scaling limit drastically restricts the admissible parameter space. This leads to an extremely parsimonious limiting model.

More specifically, our first main result establishes that in a large time asymptotic, the suitably rescaled signed order flow converges to the sum of two terms: a fractional component with Hurst index H0>1/2H\_{0}>1/2, inherited from the persistence of the core flow, and a martingale component generated by the reaction flow. This limiting process is close to a “mixed fractional Brownian motion”, that is the sum of a standard Brownian motion and an independent fractional Brownian motion of [[13](https://arxiv.org/html/2601.23172v2#bib.bib9 "Mixed fractional Brownian motion")]. Deployed to model order flow, this mixed fractional structure naturally explains why Hurst exponent estimates for signed order flow are strongly scale dependent: they are close to 0.50.5 at high frequencies, where the memoryless component dominates, and increase substantially at coarser time scales, where the persistent fractional component becomes more and more visible.
As a consequence, classical roughness estimators based on a pure fractional Brownian motion specification are inherently biased in this setting, in line with the results displayed in Figure [3](https://arxiv.org/html/2601.23172v2#S1.F3 "Figure 3 ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."). By contrast, when inference procedures explicitly account for the mixed fractional structure, Hurst parameter estimates become remarkably stable across aggregation scales. Figure [4](https://arxiv.org/html/2601.23172v2#S1.F4 "Figure 4 ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") illustrates this phenomenon: for all considered sampling frequencies, the estimated Hurst exponent H0H\_{0} under mixed fractional specification lies in the narrow range 0.750.75–0.800.80.

![Refer to caption](x4.png)


Figure 4: Average Hurst exponent estimates for signed order flow over 4040 stocks for the period 2021–2024, under mixed fractional Brownian motion specification.
  
Note: For each asset and time scale Δ\Delta, the Hurst parameter of the fractional Brownian motion component is estimated using quadratic variations computed at the time scales Δ\Delta, 2​Δ2\Delta, and 4​Δ4\Delta. The estimation procedure then follows the methodology developed for mixed fractional processes in [[15](https://arxiv.org/html/2601.23172v2#bib.bib146 "Rate-optimal estimation of mixed semimartingales"), [60](https://arxiv.org/html/2601.23172v2#bib.bib670 "Asymptotic efficiency for mixed fractional Brownian motion")].

Our second main result provides the corresponding asymptotic behavior for the unsigned traded volume.
It turns out to be primarily driven by the reaction flow. Yet, the requirement of a non-trivial scaling limit imposes tight constraints on the latter, so that the memory parameter H0H\_{0} governing the persistence of the core flow also directly determines the statistical nature of the endogenous reaction intensity. More specifically, the (cumulative) unsigned volume converges to (the integral of) a rough process with Hurst exponent H0−1/2H\_{0}-1/2.
This result provides a structural explanation for the empirically observed roughness of traded volumes. On our dataset, standard autocovariance-based estimators yield Hurst exponent estimates for unsigned volume in the range 0.150.15–0.350.35, see Figure [5](https://arxiv.org/html/2601.23172v2#S1.F5 "Figure 5 ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
These empirical values match our theoretical predictions when H0H\_{0} is of order 0.750.75, which coincides remarkably well with the estimates obtained for signed order flow.

Taken together, these results provide a consistent explanation for the observed scaling properties of signed order flow and unsigned volume. But beyond this, the mixed fractional structure of the order flow also plays a crucial role in explaining the joint dynamics of order flow, market impact, and volatility. To wit, in the relevant regime H0>3/4H\_{0}>3/4, the mixed fractional Brownian motion admits a semi-martingale representation [[13](https://arxiv.org/html/2601.23172v2#bib.bib9 "Mixed fractional Brownian motion")].
This property allows us to connect order flow dynamics to price formation while preserving the martingale property of prices. Exploiting fine regularity properties of the drift component in this representation, we show that the same parameter H0H\_{0} governing the persistence of the core flow also controls the scaling behavior of both market impact and volatility.

![Refer to caption](x5.png)


Figure 5: 
Average Hurst exponent estimates for unsigned trading volume, averaged over 4040 stocks for the period 2021–2024.
  
Note: For each asset and time scale Δ\Delta, the procedure is as follows: the total traded volume is aggregated over bins of size Δ\Delta; the intraday seasonal pattern is removed multiplicatively; volume increments are computed and truncated at three times their standard deviation to mitigate the impact of outliers and exclude potential jumps in the volume intensity process; the auto-covariance function is then estimated, and the Hurst exponent is obtained using a GMM-based approach similar to [[46](https://arxiv.org/html/2601.23172v2#bib.bib446 "Generalized method of integrated moments for high-frequency data")]. The methodology closely follows the procedures developed for volatility analysis in [[16](https://arxiv.org/html/2601.23172v2#bib.bib161 "Statistical inference for rough volatility: Central limit theorems"), [18](https://arxiv.org/html/2601.23172v2#bib.bib669 "Intraday volatility dynamics")].

More precisely, following the approach in [[42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")] where prices reflect the anticipation of future order flow, no-arbitrage arguments imply that the impact function follows a power law with exponent 2−2​H02-2H\_{0}. This shape of impact then implies that volatility behaves as a rough fractional process with Hurst exponent 2​H0−3/22H\_{0}-3/2.

Thus, persistence in signed order flow, roughness of unsigned volume, roughness of volatility, and market impact exponent are not independent empirical features but are jointly determined by a single structural parameter H0H\_{0}. In the empirically relevant regime H0≈3/4H\_{0}\approx 3/4, our framework therefore recovers, in a unified and internally consistent setting, strongly persistent order flow, rough unsigned volume with Hurst exponent near 1/41/4, very rough volatility with Hurst parameter close to zero, and the square-root law of market impact. Rather than relying on finely tuned assumptions, this joint behavior emerges as a consequence of scale separation, no-arbitrage constraints, and the mixed fractional nature of aggregate order flow.

The rest of the paper is organized as follows.
Section [2](https://arxiv.org/html/2601.23172v2#S2 "2 A two-layer Hawkes model for order flow ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") introduces the two-layer Hawkes framework. Section [3](https://arxiv.org/html/2601.23172v2#S3 "3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") derives the scaling limits for the core, reaction, and aggregate order flows. Section [4](https://arxiv.org/html/2601.23172v2#S4 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") establishes the connections between order flow, market impact, and volatility.
For better readability, all proofs are collected in the appendix.

## 2 A two-layer Hawkes model for order flow

This section introduces a model that allows to consistently capture the empirical properties of signed order flow and unsigned volume and to establish a unified framework connecting them to rough volatility and power-law market impact.

To this end, we decompose the aggregate order flow into two conceptually distinct building blocks:

* •

  Core order flow: The core order flow arises from a heterogeneous mixture of of autonomous trading motives and horizons. In particular, it comprises medium and low frequency strategies, often grounded in fundamental information, long term valuation views, or trend following dynamics. Such strategies explain part of the empirically observed persistence in order flow, where the signs of trades exhibit long-range dependence. This is complemented by metaorder splitting: large institutional trades are executed incrementally over time to minimize market impact.
* •

  Reaction orders: Unlike the core flow, reaction orders are not initiated for autonomous reasons but arise as a response to other trades. This applies both to the core flow (which contains both informed trades and trading opportunities) and to other reaction orders. Such reaction orders reflect the dynamic interplay among liquidity providers, high-frequency market makers and quantitative strategies that continuously adjust their positions and inventories. The resulting feedback mechanisms generate additional layers of dependence within the order flow, complementing the persistence directly induced by the core order flow.

### 2.1 Core order flow

We model the core buy and sell orders by two independent univariate Hawkes processes, denoted by F+F^{+} and F−F^{-}, respectively. This is a very natural modeling tool for the splitting of a metaorder or a trend following strategy. For example, once a child order is submitted, the probability of observing further orders of the same sign increases, reflecting the continuation of an execution program.

Formally, both F+F^{+} and F−F^{-} have the same baseline intensity ν>0\nu>0 and the same excitation kernel φ0:ℝ+→ℝ+\varphi\_{0}\colon\mathbb{R}\_{+}\to\mathbb{R}\_{+} that governs the temporal dependence between trades. Hence, the intensities of core buy and sell orders are given by

|  |  |  |
| --- | --- | --- |
|  | λt+=ν+∫0t−φ0​(t−s)​𝑑Fs+,λt−=ν+∫0t−φ0​(t−s)​𝑑Fs−.\lambda^{+}\_{t}=\nu+\int\_{0}^{t-}\varphi\_{0}(t-s)\,dF^{+}\_{s},\qquad\lambda^{-}\_{t}=\nu+\int\_{0}^{t-}\varphi\_{0}(t-s)\,dF^{-}\_{s}. |  |

When the excitation kernel φ0\varphi\_{0} decays rapidly, the process approximates a memoryless sequence of orders, with limited interaction between successive trades. Conversely, a slowly decaying φ0\varphi\_{0} implies that each trade continues to elevate the probability of subsequent trades in the same direction over an extended horizon. This captures that large metaorders or trend-following strategies, once initiated, generate persistent streams of transactions.

The signed core order flow and unsigned core volume are in turn given by

|  |  |  |
| --- | --- | --- |
|  | Ft=Ft+−Ft−,Vt=Ft++Ft−,F\_{t}=F\_{t}^{+}-F\_{t}^{-},\qquad V\_{t}=F\_{t}^{+}+F\_{t}^{-}, |  |

which measure the directional flow and overall trading volumes due to core trading activity.

### 2.2 Reaction orders

We now turn to the market’s endogenous reaction to incoming orders. Because trading is anonymous, it is hard to discriminate autonomous core orders from other trades. Therefore, we model this reaction flow via Hawkes process driven by core and other reaction trades in the same manner. More specifically, we consider a two-dimensional Hawkes process

|  |  |  |
| --- | --- | --- |
|  | 𝐍t=(Nt+,Nt−),{\mathbf{N}}\_{t}=(N\_{t}^{+},N\_{t}^{-}), |  |

where N+N^{+} describes reaction buys and N−N^{-} models reaction sells.

The baseline intensity of 𝐍\mathbf{N} is driven by the reaction to core orders through a symmetric kernel matrix

|  |  |  |
| --- | --- | --- |
|  | ϕ=(φ1φ2φ2φ1),{\boldsymbol{\phi}}=\begin{pmatrix}\varphi\_{1}&\varphi\_{2}\\ \varphi\_{2}&\varphi\_{1}\end{pmatrix}, |  |

so that

|  |  |  |
| --- | --- | --- |
|  | 𝝁t=∫0tϕ​(t−s)⋅𝑑𝐅swhere𝐅t=(Ft+,Ft−).{\boldsymbol{\mu}}\_{t}=\int\_{0}^{t}{\boldsymbol{\phi}}(t-s)\cdot\,d\mathbf{F}\_{s}\qquad\text{where}\qquad\mathbf{F}\_{t}=(F\_{t}^{+},F\_{t}^{-}). |  |

The aggregate intensity of 𝐍\mathbf{N} is in turn given by

|  |  |  |
| --- | --- | --- |
|  | 𝝀t=𝝁t+∫0tϕ​(t−s)⋅𝑑𝐍s=∫0tϕ​(t−s)⋅d​(𝐅s+𝐍s).{\boldsymbol{\lambda}}\_{t}={\boldsymbol{\mu}}\_{t}+\int\_{0}^{t}{\boldsymbol{\phi}}(t-s)\cdot\,d\mathbf{N}\_{s}=\int\_{0}^{t}{\boldsymbol{\phi}}(t-s)\cdot\,\mathrm{d}(\mathbf{F}\_{s}+\mathbf{N}\_{s}). |  |

This structure of Hawkes process branching on Hawkes process describes the dynamics of the reaction flow:

* •

  Following a core buy order at t0t\_{0}, a wave of reaction buy orders (with intensity φ1\varphi\_{1}) is triggered on the ask side, reflecting for instance momentum strategies, while a wave of reaction sell orders (with intensity φ2\varphi\_{2}) may appear on the bid side, reflecting inventory rebalancing or contrarian liquidity provision;
* •

  The situation is symmetric for core sell orders, with φ1\varphi\_{1} and φ2\varphi\_{2} swapping roles.
* •

  Non-core orders are digested by the market through the same mechanism. This is represented by the integral term with respect to d​𝐍\mathrm{d}\mathbf{N} in the intensity of 𝐍\mathbf{N}. The market uses exactly the same kernel to process core and non-core orders as there is no way to distinguish between them.

### 2.3 Aggregate order flow

The aggregate order flow combines both core and reaction flow:

|  |  |  |
| --- | --- | --- |
|  | Ut=Ft++Ft−+Nt++Nt−,St=Ft+−Ft−+Nt+−Nt−,U\_{t}=F\_{t}^{+}+F\_{t}^{-}+N^{+}\_{t}+N^{-}\_{t},\qquad S\_{t}=F\_{t}^{+}-F\_{t}^{-}+N^{+}\_{t}-N^{-}\_{t}, |  |

where UtU\_{t} is the unsigned aggregate volume and StS\_{t} is total signed order flow.

## 3 Scaling limits of the order flows

In this section, we study the macroscopic behavior of the different order flows introduced above. We first address the scaling limits of core orders and then turn to those of reaction orders and the aggregate flow.

### 3.1 Scaling limit of the core flow

We consider the same model as in Section [2](https://arxiv.org/html/2601.23172v2#S2 "2 A two-layer Hawkes model for order flow ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), indexed with the additional parameter T>0T>0 that denotes the length of the time interval [0,T][0,T] on which the processes are observed. The goal of this section is to establish scaling limits for the core order flow process as TT goes to infinity, thus capturing its macroscopic behavior.
Following [[40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes")], we work in a nearly unstable, heavy–tailed Hawkes regime that captures both the high level of clustering of the core flow and the long memory of trading activity. We formalize this through the following assumptions.

###### Assumption A.

There exists a nonnegative sequence (a0T)T≥0(a\_{0}^{T})\_{T\geq 0} converging to one such that a0T<1a\_{0}^{T}<1 and

|  |  |  |
| --- | --- | --- |
|  | φ0T=a0T​φ0,\varphi\_{0}^{T}=a\_{0}^{T}\varphi\_{0}, |  |

for some completely monotone kernel φ0\varphi\_{0} (see [[5](https://arxiv.org/html/2601.23172v2#bib.bib655 "Sur les fonctions absolument monotones")] for definition) such that ‖φ0‖L1=1{|\kern-1.07639pt|\varphi\_{0}|\kern-1.07639pt|}\_{L^{1}}=1. Furthermore, there exists 0<α0<10<\alpha\_{0}<1 and a positive constant K0K\_{0} such that as tt tends to infinity,

|  |  |  |
| --- | --- | --- |
|  | α0​tα0​∫t∞φ0​(t)​𝑑t→K0.\alpha\_{0}t^{\alpha\_{0}}\int\_{t}^{\infty}\varphi\_{0}(t)\,dt\to K\_{0}. |  |

From a probabilistic perspective, a Hawkes process can be viewed as a population process and the norm of the corresponding self-exciting kernel. In this case, φ0\varphi\_{0} can be interpreted as the proportion of descendants in the whole population. In the financial setting, the norm ‖φ0‖L1{|\kern-1.07639pt|\varphi\_{0}|\kern-1.07639pt|}\_{L^{1}} can be seen as the proportion of orders that are subsequent to other orders in the market. Most orders fall in this category, in the sense that a large fraction of orders are follower orders. This is, for example, the case when they are part of the same metaorder or when they are reaction orders to the global flow [[34](https://arxiv.org/html/2601.23172v2#bib.bib320 "Critical reflexivity in financial markets: a Hawkes process analysis")]. In our model, this translates into the assumption that the norm of the self-exciting kernel converges to one, while remaining strictly below this threshold. In particular, the condition ‖φ0‖L1<1{|\kern-1.07639pt|\varphi\_{0}|\kern-1.07639pt|}\_{L^{1}}<1 ensures the existence of a stationary solution for the intensity. The second part of Assumption [A](https://arxiv.org/html/2601.23172v2#Thmassumption1 "Assumption A. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") imposes a heavy-tailed kernel, which captures strong clustering in order arrivals induced, e.g., due to the splitting of metaorders. Here, we assume a power-law decay, governed by the parameter α0\alpha\_{0}.

To obtain non-degenerate limits for our signed core order flow and unsigned core volume, the parameters a0Ta^{T}\_{0}, α0\alpha\_{0} and the baseline intensity νT\nu^{T} of the core flow have to be scaled appropriately:

###### Assumption B.

There exists two constants λ0,μ0>0\lambda\_{0},\mu\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | limT→∞Tα0​(1−a0T)=λ0​K0​Γ​(1−α0)α0andlimT→∞T1−α0​νT=μ0​α0K0​Γ​(1−α0),\lim\limits\_{T\to\infty}T^{\alpha\_{0}}(1-a^{T}\_{0})=\lambda\_{0}K\_{0}\frac{\Gamma(1-\alpha\_{0})}{\alpha\_{0}}\qquad\text{and}\qquad\lim\limits\_{T\to\infty}T^{1-\alpha\_{0}}\nu^{T}=\mu\_{0}\frac{\alpha\_{0}}{K\_{0}\Gamma(1-\alpha\_{0})}, |  |

where Γ\Gamma is the Gamma function.

Under these assumptions, the long-term average intensity of the Hawkes process F±,TF^{\pm,T} is given by (1−a0T)−1​νT(1-a\_{0}^{T})^{-1}\nu^{T}. Therefore the average number of trades from F±,TF^{\pm,T} on [0,T][0,T] scales as T​νT​(1−a0T)−1T\nu^{T}(1-a\_{0}^{T})^{-1}. As a result, it is natural to normalize each of the Hawkes processes by (1−a0T)−1​νT​T(1-a\_{0}^{T})^{-1}\nu^{T}T and consider the rescaled processes

|  |  |  |
| --- | --- | --- |
|  | F¯t±,T=1−a0TT​νT​Ft​T±,T.\overline{F}\_{t}^{\pm,T}=\frac{1-a^{T}\_{0}}{T\nu^{T}}F\_{tT}^{\pm,T}. |  |

For α0>0\alpha\_{0}>0 and λ0>0\lambda\_{0}>0, we define the function fα0,λ0f^{\alpha\_{0},\lambda\_{0}} by

|  |  |  |
| --- | --- | --- |
|  | fα0,λ0​(x)=λ0​xα0−1​Eα0,α0​(−λ0​xα0),f^{\alpha\_{0},\lambda\_{0}}(x)=\lambda\_{0}x^{\alpha\_{0}-1}E\_{\alpha\_{0},\alpha\_{0}}(-\lambda\_{0}x^{\alpha\_{0}}), |  |

where Eα,βE\_{\alpha,\beta} is the (α,β)(\alpha,\beta)-Mittag-Leffler function

|  |  |  |
| --- | --- | --- |
|  | Eα,β​(x)=∑k=0∞xkΓ​(α​k+β),E\_{\alpha,\beta}(x)=\sum\_{k=0}^{\infty}\frac{x^{k}}{\Gamma(\alpha k+\beta)}, |  |

see [[35](https://arxiv.org/html/2601.23172v2#bib.bib324 "Mittag-Leffler functions and their applications")].
The following theorem is proved in Appendix [B](https://arxiv.org/html/2601.23172v2#A2 "Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."):

###### Theorem 3.1.

Under Assumptions [A](https://arxiv.org/html/2601.23172v2#Thmassumption1 "Assumption A. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") and [B](https://arxiv.org/html/2601.23172v2#Thmassumption2 "Assumption B. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), the process (F¯t+,T,F¯t−,T)t∈[0,1](\overline{F}\_{t}^{+,T},\overline{F}\_{t}^{-,T})\_{t\in[0,1]} is tight for the Skorokhod topology. Furthermore, any limit point (Ft+,Ft−)(F\_{t}^{+},F\_{t}^{-})999From now on (Ft+,Ft−)(F\_{t}^{+},F\_{t}^{-}) denote the limiting processes and no longer the Hawkes processes. of (F¯t+,T,F¯t−,T)(\overline{F}\_{t}^{+,T},\overline{F}\_{t}^{-,T}) satisfies

|  |  |  |
| --- | --- | --- |
|  | Ft±=∫0ts​fα0,λ0​(t−s)​𝑑s+1μ0​λ0​∫0tfα0,λ0​(t−s)​Zs±​𝑑s,F\_{t}^{\pm}=\int\_{0}^{t}sf^{\alpha\_{0},\lambda\_{0}}(t-s)\,ds+\frac{1}{\sqrt{\mu\_{0}\lambda\_{0}}}\int\_{0}^{t}f^{\alpha\_{0},\lambda\_{0}}(t-s)Z^{\pm}\_{s}\,ds, |  |

where Z+Z^{+} and Z−Z^{-} are two independent continuous martingales with quadratic variations F+F^{+} and F−F^{-}, respectively.

When the kernel’s decay parameter satisfies α0>12\alpha\_{0}>\tfrac{1}{2}, the limiting processes identified in Theorem [3.1](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") are differentiable, and their derivatives belong to the class of rough Heston–type models developed in [[40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes"), [25](https://arxiv.org/html/2601.23172v2#bib.bib222 "The characteristic function of rough Heston models")].
By contrast, in the empirically relevant regime α0<12\alpha\_{0}<\tfrac{1}{2}, the core flow displays strong persistence and the limiting processes become non-differentiable.
Note that in this case, the asymptotic cumulated unsigned volume is a non-differentiable increasing process, which corresponds to the dynamics of the integrated volatility in “hyper-rough Heston models” introduced in [[42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")]. Determining the exact almost sure Hölder regularity of such processes is a delicate pathwise problem.
In the present setting, we are able to establish a lower bound for the almost sure Hölder exponent, but a matching upper bound remains out of reach.
However, Kolmogorov’s continuity theorem and its extensions provide a powerful link between pathwise regularity and moment estimates in LpL^{p}.
For Gaussian processes, these notions coincide [[20](https://arxiv.org/html/2601.23172v2#bib.bib169 "Quelques espaces fonctionnels associés à des processus gaussiens")]; in our case, the limiting processes are not Gaussian, although they share closely related structural features.
As a consequence, classical Gaussian arguments cannot be applied directly.
Nevertheless, by exploiting suitable moment estimates, we are able to obtain a sharp characterization of Hölder regularity in the L2L^{2} sense, together with a lower bound for the almost sure Hölder regularity of the sample paths, which we summarize in the following proposition.

###### Proposition 3.2.

For any ε>0\varepsilon>0, the processes F+F^{+} and F−F^{-} are almost surely Hölder continuous on [0,1][0,1] with exponent (1∧2​α0)−ε(1\wedge 2\alpha\_{0})-\varepsilon.
Moreover, in the case α0<12\alpha\_{0}<\tfrac{1}{2}, they are exactly 2​α02\alpha\_{0}-Hölder continuous in L2L^{2}, in the sense that there exists a constant C>0C>0 such that, for any t∈[0,1]t\in[0,1]:

|  |  |  |
| --- | --- | --- |
|  | (𝔼​|Ft+h−Ft|2)1/2=C​h2​α0+o​(h2​α0),as h→0.\bigl(\mathbb{E}|F\_{t+h}-F\_{t}|^{2}\bigr)^{1/2}=C\,h^{2\alpha\_{0}}+o\bigl(h^{2\alpha\_{0}}\bigr),\quad\mbox{as $h\to 0$.} |  |

As TT goes to infinity, the scaled signed core order flow and unsigned core volume satisfy

|  |  |  |
| --- | --- | --- |
|  | F¯t+,T+F¯t−,T⟶Ft++Ft−andF¯t+,T−F¯t−,T⟶Ft+−Ft−.\overline{F}\_{t}^{+,T}+\overline{F}\_{t}^{-,T}\longrightarrow F\_{t}^{+}+F\_{t}^{-}\qquad\text{and}\qquad\overline{F}\_{t}^{+,T}-\overline{F}\_{t}^{-,T}\longrightarrow F\_{t}^{+}-F\_{t}^{-}. |  |

From Theorem [3.1](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), we therefore obtain the following limit theorem:

###### Proposition 3.3.

Let

|  |  |  |
| --- | --- | --- |
|  | Ft=Ft++Ft−andVt=Ft+−Ft−F\_{t}=F\_{t}^{+}+F\_{t}^{-}\qquad\text{and}\qquad V\_{t}=F\_{t}^{+}-F\_{t}^{-} |  |

denote the scaling limits of the unsigned core volume and signed core flow, respectively, where F+F^{+} and F−F^{-} are given in Theorem [3.1](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."). We have

|  |  |  |
| --- | --- | --- |
|  | Ft=2​∫0ts​fα0,λ0​(t−s)​𝑑s+1μ0​λ0​∫0tfα0,λ0​(t−s)​ZsF​𝑑sF\_{t}=2\int\_{0}^{t}s\,f^{\alpha\_{0},\lambda\_{0}}(t-s)\,ds+\frac{1}{\sqrt{\mu\_{0}\,\lambda\_{0}}}\int\_{0}^{t}f^{\alpha\_{0},\lambda\_{0}}(t-s)\,Z^{F}\_{s}\,ds |  |

and

|  |  |  |
| --- | --- | --- |
|  | Vt=1μ0​λ0​∫0tfα0,λ0​(t−s)​ZsV​𝑑s,V\_{t}=\frac{1}{\sqrt{\mu\_{0}\,\lambda\_{0}}}\int\_{0}^{t}f^{\alpha\_{0},\lambda\_{0}}(t-s)\,Z^{V}\_{s}\,ds, |  |

where ZFZ^{F} and ZVZ^{V} are two continuous martingales with quadratic variation FF and quadratic covariation VV such that

|  |  |  |
| --- | --- | --- |
|  | ZF=Z++Z−andZV=Z+−Z−,Z^{F}=Z^{+}+Z^{-}\qquad\text{and}\qquad Z^{V}=Z^{+}-Z^{-}, |  |

where Z+Z^{+} and Z−Z^{-} are given in Theorem [3.1](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").

When α0<12\alpha\_{0}<\tfrac{1}{2}, the processes FF and VV are exactly 2​α02\alpha\_{0}–Hölder continuous in L2L^{2}.
Consequently, the signed core order flow and the unsigned core volume exhibit the same local regularity as a fractional Brownian motion with Hurst exponent

|  |  |  |
| --- | --- | --- |
|  | H0=2​α0.H\_{0}=2\alpha\_{0}. |  |

Moreover, in the high-frequency asymptotic regime relevant for statistical inference, their autocovariance functions coincide with those of a fractional Brownian motion with parameter H0H\_{0} [[16](https://arxiv.org/html/2601.23172v2#bib.bib161 "Statistical inference for rough volatility: Central limit theorems"), [15](https://arxiv.org/html/2601.23172v2#bib.bib146 "Rate-optimal estimation of mixed semimartingales"), [60](https://arxiv.org/html/2601.23172v2#bib.bib670 "Asymptotic efficiency for mixed fractional Brownian motion")].

### 3.2 Scaling limit of the reaction orders

Similarly as for the core flow, we augment the notations for the reaction flow from Section [2](https://arxiv.org/html/2601.23172v2#S2 "2 A two-layer Hawkes model for order flow ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") with the additional parameter TT for the time horizon. We write

|  |  |  |
| --- | --- | --- |
|  | 𝚲tT=∫0t𝝀sT​𝑑s{\boldsymbol{\Lambda}}\_{t}^{T}=\int\_{0}^{t}{\boldsymbol{\lambda}}\_{s}^{T}ds |  |

for the compensator of our Hawkes process and the associated martingale is denoted by

|  |  |  |
| --- | --- | --- |
|  | 𝐌tT=𝐍tT−𝚲tT.\mathbf{M}\_{t}^{T}=\mathbf{N}\_{t}^{T}-{\boldsymbol{\Lambda}}\_{t}^{T}. |  |

We are again interested in the macroscopic scaling behavior of the reaction orders. Therefore, in the same spirit as in [[24](https://arxiv.org/html/2601.23172v2#bib.bib219 "The microstructural foundations of leverage effect and rough volatility")], we make the following assumption that again reflects the fact that most sent orders can be seen as consequence of some earlier orders.

###### Assumption C.

There exists a nonnegative sequence (a1T)T≥0(a\_{1}^{T})\_{T\geq 0} converging to one such that a1T<1a\_{1}^{T}<1 and

|  |  |  |
| --- | --- | --- |
|  | ϕT=a1T​ϕ{\boldsymbol{\phi}}^{T}=a\_{1}^{T}{\boldsymbol{\phi}} |  |

for some matrix ϕ{\boldsymbol{\phi}} whose spectral radius satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝒮​(‖ϕ‖L1)=‖φ1‖L1+‖φ2‖L1=1.\mathcal{S}({|\kern-1.07639pt|{\boldsymbol{\phi}}|\kern-1.07639pt|}\_{L^{1}})={|\kern-1.07639pt|\varphi\_{1}|\kern-1.07639pt|}\_{L^{1}}+{|\kern-1.07639pt|\varphi\_{2}|\kern-1.07639pt|}\_{L^{1}}=1. |  |

From [[42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")], we also know that Assumption [C](https://arxiv.org/html/2601.23172v2#Thmassumption3 "Assumption C. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") is necessary in order to obtain non-trivial price impact on the market. We write k1​(t)≥k2​(t)k\_{1}(t)\geq k\_{2}(t) for the eigenvalues of ϕ​(t){\boldsymbol{\phi}}(t), i.e.,

|  |  |  |
| --- | --- | --- |
|  | k1​(t)=φ1​(t)+φ2​(t),k2​(t)=φ1​(t)−φ2​(t),k\_{1}(t)=\varphi\_{1}(t)+\varphi\_{2}(t),\quad k\_{2}(t)=\varphi\_{1}(t)-\varphi\_{2}(t), |  |

and denote by v1v\_{1}, v2v\_{2} their associated eigenvectors

|  |  |  |
| --- | --- | --- |
|  | v1=(11),v2=(1−1).v\_{1}=\begin{pmatrix}1\\ 1\end{pmatrix},\quad v\_{2}=\begin{pmatrix}1\\ -1\end{pmatrix}. |  |

The following assumption relates to the slowly decreasing behavior of the kernel matrix, that is also necessary to obtain non-trivial market impact, see [[42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")]:

###### Assumption D.

There exists 1/2<α1<11/2<\alpha\_{1}<1 and K1>0K\_{1}>0 such that

|  |  |  |
| --- | --- | --- |
|  | limt→∞α1​tα1​∫t∞k1​(s)​𝑑s→K1.\lim\limits\_{t\to\infty}\alpha\_{1}t^{\alpha\_{1}}\int\_{t}^{\infty}k\_{1}(s)\,ds\to K\_{1}. |  |

We finally need to specify an asymptotic framework similar to that in Assumption [B](https://arxiv.org/html/2601.23172v2#Thmassumption2 "Assumption B. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") to ensure our limiting processes are not degenerate. In [[24](https://arxiv.org/html/2601.23172v2#bib.bib219 "The microstructural foundations of leverage effect and rough volatility")] there is a constant baseline μT\mu^{T} and two positive constants λ1\lambda\_{1} and μ1\mu\_{1} such that

|  |  |  |
| --- | --- | --- |
|  | Tα1​(1−a1T)→λ1,andT1−α1​μT→μ1.T^{\alpha\_{1}}(1-a^{T}\_{1})\to\lambda\_{1},\qquad\text{and}\qquad T^{1-\alpha\_{1}}\mu^{T}\to\mu\_{1}. |  |

However, in our setting the baseline intensity 𝝁T\boldsymbol{\mu}^{T} is itself stochastic and time‐dependent. In [[24](https://arxiv.org/html/2601.23172v2#bib.bib219 "The microstructural foundations of leverage effect and rough volatility")], μT\mu^{T} behaves like Tα1−1T^{\alpha\_{1}-1} as T→∞T\to\infty, so that the expected number of baseline‐driven jumps on [0,T][0,T], namely T​μTT\,\mu^{T}, grows like Tα1T^{\alpha\_{1}}. In our case, the number of baseline events between 0 and TT is
FT+,T+FT−,TF\_{T}^{+,T}+F\_{T}^{-,T},
that is of order (1−a0T)−1​T​νT(1-a\_{0}^{T})^{-1}T\,\nu^{T}.
Therefore, it is natural to replace T​μTT\,\mu^{T} by T​νT​(1−a0T)−1T\nu^{T}(1-a\_{0}^{T})^{-1} and to make the following assumption:

###### Assumption E.

There exist λ1,μ1>0\lambda\_{1},\mu\_{1}>0 such that

|  |  |  |
| --- | --- | --- |
|  | Tα1​(1−a1T)→λ1andT1−α1​νT1−a0T→μ1.T^{\alpha\_{1}}(1-a^{T}\_{1})\to\lambda\_{1}\qquad\text{and}\qquad\frac{T^{1-\alpha\_{1}}\nu^{T}}{1-a\_{0}^{T}}\to\mu\_{1}. |  |

By Assumption [B](https://arxiv.org/html/2601.23172v2#Thmassumption2 "Assumption B. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), the product T​νTT\nu^{T} is of order Tα0T^{\alpha\_{0}}, which implies from Assumption [E](https://arxiv.org/html/2601.23172v2#Thmassumption5 "Assumption E. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") that 1−a0T1-a\_{0}^{T} must be of order Tα0−α1T^{\alpha\_{0}-\alpha\_{1}}. However, we already have that 1−a0T1-a\_{0}^{T} scales as T−α0T^{-\alpha\_{0}}. Hence, to accommodate both of these scalings, we necessarily need

|  |  |  |
| --- | --- | --- |
|  | α1=2​α0.\alpha\_{1}=2\,\alpha\_{0}. |  |

Note also that from Assumption [D](https://arxiv.org/html/2601.23172v2#Thmassumption4 "Assumption D. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), we have 1/4<α0<1/21/4<\alpha\_{0}<1/2. As a consequence, the existence of a nontrivial scaling limit imposes strong structural constraints on the underlying Hawkes model.

In summary, we consider the scaled processes

|  |  |  |  |
| --- | --- | --- | --- |
|  | N¯t±,T=(1−a0T)​(1−a1T)T​νT​Nt​T±,T,\displaystyle\overline{N}^{\pm,T}\_{t}=\frac{(1-a^{T}\_{0})(1-a^{T}\_{1})}{T\nu^{T}}N\_{tT}^{\pm,T}, | Λ¯t±,T=(1−a0T)​(1−a1T)T​νT​Λt​T±,T,\displaystyle\qquad\qquad\overline{\Lambda}\_{t}^{\pm,T}=\frac{(1-a^{T}\_{0})(1-a^{T}\_{1})}{T\nu^{T}}\Lambda\_{tT}^{\pm,T}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | M¯t±,T=\displaystyle\overline{M}\_{t}^{\pm,T}= | ((1−a0T)​(1−a1T)T​νT)1/2​Mt​T±,T.\displaystyle\Big(\frac{(1-a^{T}\_{0})(1-a^{T}\_{1})}{T\nu^{T}}\Big)^{1/2}M\_{tT}^{\pm,T}. |  |

We are now ready to state the convergence in distribution of these processes.

###### Theorem 3.4.

Under Assumptions [A](https://arxiv.org/html/2601.23172v2#Thmassumption1 "Assumption A. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), [B](https://arxiv.org/html/2601.23172v2#Thmassumption2 "Assumption B. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), [C](https://arxiv.org/html/2601.23172v2#Thmassumption3 "Assumption C. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), [D](https://arxiv.org/html/2601.23172v2#Thmassumption4 "Assumption D. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") and [E](https://arxiv.org/html/2601.23172v2#Thmassumption5 "Assumption E. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."):

* •

  The process (N¯+,T,N¯−,T,Λ¯+,T,Λ¯−,T,M¯+,T,M¯−,T\overline{N}^{+,T},\overline{N}^{-,T},\overline{\Lambda}^{+,T},\overline{\Lambda}^{-,T},\overline{M}^{+,T},\overline{M}^{-,T}) is C-tight for the Skorokhod topology. Moreover, each of its limit points (X,X,X,X,Z+,Z−X,X,X,X,Z^{+},Z^{-}) has the rough Heston-type dynamics

  |  |  |  |
  | --- | --- | --- |
  |  | Xt=12​∫0tfα1,λ1​(t−s)​Fs​𝑑s+12​λ1​μ1​∫0tfα1,λ1​(t−s)​Zs​𝑑s,X\_{t}=\frac{1}{2}\int\_{0}^{t}f^{\alpha\_{1},\lambda\_{1}}(t-s)F\_{s}\,ds+\frac{1}{2\sqrt{\lambda\_{1}\mu\_{1}}}\int\_{0}^{t}f^{\alpha\_{1},\lambda\_{1}}(t-s)Z\_{s}\,ds,\\ |  |

  where Z=Z++Z−Z=Z^{+}+Z^{-}, with Z+Z^{+} and Z−Z^{-} two continuous martingales with quadratic variation XX and zero quadratic covariation, and FF is given in Proposition [3.3](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."). Furthermore, XX behaves as an integrated rough process, and its derivative has Hölder regularity of order (H1−ε)(H\_{1}-\varepsilon) for any ε>0\varepsilon>0 on [0,1][0,1], where H1=α1−1/2=H0−1/2H\_{1}=\alpha\_{1}-1/2=H\_{0}-1/2.
* •

  The scaled signed reaction flow N¯+,T−N¯−,T\overline{N}^{+,T}-\overline{N}^{-,T} converges in probability to zero.

The first part of Theorem [3.4](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") suggests that the roughness of the unsigned volume originates from reaction orders. The second statement shows that under the same rescaling as for the unsigned volume, the signed reaction flow actually vanishes. This means unsigned volume and signed order flow have a different order of magnitude, which will play a crucial role in the study of the asymptotic behaviors of the global flows in the next section.

### 3.3 Scaling limits for the global order flow

We now turn to the scaling limits of the aggregate order flow processes

|  |  |  |
| --- | --- | --- |
|  | UtT=FtT,++Ft−,T+Nt+,T+Nt−,T,StT=FtT,+−Ft−,T+Nt+,T−Nt−,T.\begin{split}&U^{T}\_{t}=F\_{t}^{T,+}+F\_{t}^{-,T}+N^{+,T}\_{t}+N^{-,T}\_{t},\\ &S^{T}\_{t}=F\_{t}^{T,+}-F\_{t}^{-,T}+N^{+,T}\_{t}-N^{-,T}\_{t}.\end{split} |  |

We start with the unsigned volume, which is the easiest case as all the terms have already been fully investigated in Sections [3.1](https://arxiv.org/html/2601.23172v2#S3.SS1 "3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") and [3.2](https://arxiv.org/html/2601.23172v2#S3.SS2 "3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."). We define

|  |  |  |
| --- | --- | --- |
|  | U¯tT=(1−a0T)​(1−a1T)T​νT​Ut​TT,\overline{U}^{T}\_{t}=\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}U^{T}\_{tT}, |  |

and obtain the following result:

###### Theorem 3.5.

Under Assumptions [A](https://arxiv.org/html/2601.23172v2#Thmassumption1 "Assumption A. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), [B](https://arxiv.org/html/2601.23172v2#Thmassumption2 "Assumption B. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), [C](https://arxiv.org/html/2601.23172v2#Thmassumption3 "Assumption C. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), [D](https://arxiv.org/html/2601.23172v2#Thmassumption4 "Assumption D. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") and [E](https://arxiv.org/html/2601.23172v2#Thmassumption5 "Assumption E. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), the scaled unsigned volume U¯T\overline{U}^{T} is C-tight in the Skorokhod topology. Furthermore if UU is a limit point of U¯T\overline{U}^{T}, then UU satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ut=2​Xt=∫0tfα1,λ1​(t−s)​Fs​𝑑s+1λ1​μ1​∫0tfα1,λ1​(t−s)​Zs​𝑑s,U\_{t}=2X\_{t}=\int\_{0}^{t}f^{\alpha\_{1},\lambda\_{1}}(t-s)F\_{s}\,ds+\sqrt{\frac{1}{\lambda\_{1}\mu\_{1}}}\int\_{0}^{t}f^{\alpha\_{1},\lambda\_{1}}(t-s)Z\_{s}\,ds, |  | (1) |

where XX is defined in Theorem [3.4](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").

We see that the contribution of the core flow almost vanishes in the limit of the aggregate unsigned trading volume, which is instead essentially determined by the reaction flow.101010The only trace of the core flow is through the term FsF\_{s} in the first integral in UtU\_{t}, coming from the baseline intensity of the reaction orders. As a consequence, just like the unsigned reaction volume, the aggregate (cumulative) unsigned volume is an (integrated) rough process in that, for any ε>0\varepsilon>0, its derivative has Hölder regularity of order H1−εH\_{1}-\varepsilon with H1=α1−1/2=H0−1/2H\_{1}=\alpha\_{1}-1/2=H\_{0}-1/2.

We now turn to the signed order flow. As already observed in Theorem [3.4](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") for the reaction flow, the same scaling as for the unsigned order flow leads to a trivial limit here:

|  |  |  |
| --- | --- | --- |
|  | (1−a0T)​(1−a1T)T​νT​St​TT→0.\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}S^{T}\_{tT}\to 0. |  |

The intuition for this is provided by Theorem [3.4](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."): in the reaction flow, the buy and sell order flows have the same asymptotic scaling limits, which implies a vanishing difference. Therefore, we need to adapt the scaling for the signed order flow similarly as in [[24](https://arxiv.org/html/2601.23172v2#bib.bib219 "The microstructural foundations of leverage effect and rough volatility")]:

|  |  |  |
| --- | --- | --- |
|  | S¯tT=((1−a0T)​(1−a1T)T​νT)1/2​St​TT.\overline{S}^{T}\_{t}=\Big(\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}\Big)^{1/2}S^{T}\_{tT}. |  |

In this regime, we then obtain the following nontrivial limiting result:

###### Theorem 3.6.

Under Assumptions [A](https://arxiv.org/html/2601.23172v2#Thmassumption1 "Assumption A. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), [B](https://arxiv.org/html/2601.23172v2#Thmassumption2 "Assumption B. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), [C](https://arxiv.org/html/2601.23172v2#Thmassumption3 "Assumption C. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), [D](https://arxiv.org/html/2601.23172v2#Thmassumption4 "Assumption D. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") and [E](https://arxiv.org/html/2601.23172v2#Thmassumption5 "Assumption E. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), the scaled signed order flow S¯T\overline{S}^{T} converges in the sense of finite-dimensional laws to

|  |  |  |
| --- | --- | --- |
|  | St=λ1​μ1​(‖φ1‖1−‖φ2‖1)1−(‖φ1‖1−‖φ2‖1)​Vt+11−(‖φ1‖1−‖φ2‖1)​(Zt+−Zt−),S\_{t}=\frac{\sqrt{\lambda\_{1}\mu\_{1}}({|\kern-1.07639pt|\varphi\_{1}|\kern-1.07639pt|}\_{1}-{|\kern-1.07639pt|\varphi\_{2}|\kern-1.07639pt|}\_{1})}{1-({|\kern-1.07639pt|\varphi\_{1}|\kern-1.07639pt|}\_{1}-{|\kern-1.07639pt|\varphi\_{2}|\kern-1.07639pt|}\_{1})}V\_{t}+\frac{1}{1-(\|\varphi\_{1}\|\_{1}-\|\varphi\_{2}\|\_{1})}(Z^{+}\_{t}-Z^{-}\_{t}), |  |

where VV is given by Proposition [3.3](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), and Z+Z^{+} and Z−Z^{-} are given by Theorem [3.4](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").

Theorem [3.6](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem6 "Theorem 3.6. ‣ 3.3 Scaling limits for the global order flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") shows that the aggregate signed order flow can be decomposed into two distinct components. The first is the contribution of the core order flow. It has the same regularity as a fractional Brownian motion with Hurst exponent H0=2​α0H\_{0}=2\alpha\_{0} and therefore induces persistence in the aggregate signed flow. The second component is a martingale term, which originates from the reaction orders.

As discussed in the introduction, this decomposition is crucial to resolving the apparent lack of scale invariance in empirical order flow data. To this end, we replace the complex model from Theorem [3.6](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem6 "Theorem 3.6. ‣ 3.3 Scaling limits for the global order flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") with the simplest process with the same local behavior: a mixed fractional Brownian motion, that is, the sum of a fractional Brownian motion and an independent Brownian motion. Put differently, we use St=Wt+BtH0S\_{t}=W\_{t}+B^{H\_{0}}\_{t}, where WW is a standard Brownian motion, used as a proxy for the reaction driven martingale component, and BH0B^{H\_{0}} is a fractional Brownian motion with Hurst exponent H0=2​α0H\_{0}=2\alpha\_{0}, mirroring the regularity of the fractional component in the scaling limit of the aggregate signed flow.

We can now apply relevant estimators for H0H\_{0}
under this mixed fractional Brownian motion approximation as in [[15](https://arxiv.org/html/2601.23172v2#bib.bib146 "Rate-optimal estimation of mixed semimartingales"), [60](https://arxiv.org/html/2601.23172v2#bib.bib670 "Asymptotic efficiency for mixed fractional Brownian motion")]. Figure [3](https://arxiv.org/html/2601.23172v2#S1.F3 "Figure 3 ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") shows that when the aggregate signed order flow is approximated by a single fractional Brownian motion, the estimated Hurst exponent depends strongly on the bin size. For very fine sampling the estimate is close to 0.50.5, reflecting the dominance of the martingale term originating from reaction orders, while at larger bin sizes the estimate increases steadily as the persistent influence of core orders becomes more pronounced.
In contrast, Figure [4](https://arxiv.org/html/2601.23172v2#S1.F4 "Figure 4 ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") demonstrates that when the flow is modeled as a mixture of a fractional Brownian motion and a Brownian motion, the estimated Hurst exponent stabilizes around 0.650.65 across all bin sizes. Therefore, the testable implications of Theorem [3.6](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem6 "Theorem 3.6. ‣ 3.3 Scaling limits for the global order flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") are confirmed by the data.

## 4 From order flow to market impact and rough volatility

In this section, we go on to show that the single parameter H0H\_{0}, not only determines the statistical nature of signed order flow and unsigned volume, but also fixes the shape of the impact function and the roughness of the volatility process. This is done by adapting the arguments of [[42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")] to our setting.

The starting point of [[42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")] is to assume that prices are martingales and to enforce the absence of statistical arbitrage. Moreover, to rule out profitable roundtrips, permanent price impact is linear [[37](https://arxiv.org/html/2601.23172v2#bib.bib356 "Price manipulation and quasi-arbitrage"), [30](https://arxiv.org/html/2601.23172v2#bib.bib268 "No-dynamic-arbitrage and market impact")]. Following [[41](https://arxiv.org/html/2601.23172v2#bib.bib388 "Market impact as anticipation of the order flow imbalance"), [42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")], one can then show that the price PtP\_{t} must satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pt=P0+lims→∞κ​𝔼​[Qs+−Qs−∣𝒢t],P\_{t}=P\_{0}+\lim\limits\_{s\to\infty}\kappa\,\mathbb{E}[Q^{+}\_{s}-Q^{-}\_{s}\mid\mathcal{G}\_{t}], |  | (2) |

where κ\kappa is the permanent impact coefficient, Q+Q^{+} and Q−Q^{-} represent the cumulative buy and sell volumes up to time tt, respectively, and (𝒢t)t≥0(\mathcal{G}\_{t})\_{t\geq 0} is the natural filtration generated by the order flows (Q+,Q−)(Q^{+},Q^{-}). Price movements thus correspond to the market’s anticipation of future order flow. This relationship provides a general and model-independent link between order flow dynamics and price evolution, reconciling the strong persistence of order flow with the martingale nature of prices.

If Q+Q^{+} and Q−Q^{-} are independent Hawkes processes, then ([2](https://arxiv.org/html/2601.23172v2#S4.E2 "In 4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")) takes the explicit propagator form

|  |  |  |
| --- | --- | --- |
|  | Pt=P0+κ​∫0tξ​(t−s)​(d​Qs+−d​Qs−),P\_{t}=P\_{0}+\kappa\int\_{0}^{t}\xi(t-s)\,(dQ^{+}\_{s}-dQ^{-}\_{s}), |  |

where ξ\xi is an explicit kernel compensating the memory of the flow and that can be computed from the Hawkes excitation kernel [[41](https://arxiv.org/html/2601.23172v2#bib.bib388 "Market impact as anticipation of the order flow imbalance"), [42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")]. In this setting, it is shown in [[42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")] that there exists some β∈(0,1)\beta\in(0,1) such that the average price deviation at time tt, M​I​(t)MI(t), of a metaorder scheduled with a constant trading rate over a renormalized time interval [0,1][0,1] satisfies

|  |  |  |
| --- | --- | --- |
|  | M​I​(t)∼t1−β, for ​t≤1,MI(t)\sim t^{1-\beta},\text{ for }t\leq 1, |  |

|  |  |  |
| --- | --- | --- |
|  | M​I​(t)∼t1−β−(t−1)1−β, for ​t>1.MI(t)\sim t^{1-\beta}-{(t-1)}^{1-\beta},\text{ for }t>1. |  |

The parameter β\beta is also linked to the tail of the kernel of the Hawkes processes driving the flow: ϕ​(t)∼t−(1+β)\phi(t)\sim t^{-(1+\beta)} as tt tends to infinity, see [[42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")] for details. The celebrated square-root law of market impact corresponds to the case β=1/2\beta=1/2 in the above formulas.111111Note, however, that the exact shape of the relaxation phase is less agreed upon than that of the increasing phase of the impact, see [[53](https://arxiv.org/html/2601.23172v2#bib.bib29 "The subtle interplay between square-root impact, order imbalance & volatility: a unifying framework")].

Another implication of this framework is that the scaling limit of the price is a rough volatility model. Indeed, the volatility of the price is driven by a rough fractional process with roughness exponent β−1/2\beta-1/2, see again [[42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")].

In our case, the (asymptotic) signed order flow YY is essentially a mixed fractional Brownian motion, whose fractional component has Hurst exponent H0=2​α0H\_{0}=2\alpha\_{0}. We see from ([2](https://arxiv.org/html/2601.23172v2#S4.E2 "In 4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")) that the key part of the flow for the link with price dynamics is its predictable part. It is shown in [[13](https://arxiv.org/html/2601.23172v2#bib.bib9 "Mixed fractional Brownian motion")] that provided H0>3/4H\_{0}>3/4, YY is a semi-martingale in its natural filtration. Empirically, we find H0>3/4H\_{0}>3/4, see Figure [4](https://arxiv.org/html/2601.23172v2#S1.F4 "Figure 4 ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."). We can therefore decompose YY into an unpredictable martingale component MM and a finite-variation component AA, that is

|  |  |  |
| --- | --- | --- |
|  | Yt=Mt+At.Y\_{t}=M\_{t}+A\_{t}. |  |

To proceed, the key idea is to approximate the finite-variation process AA by the difference of two independent Hawkes processes N~a\widetilde{N}^{a} and N~b\widetilde{N}^{b} with same baseline intensity and self-exciting kernel. If this kernel decays as t−(1+α)t^{-(1+\alpha)} with α∈(1/2,1)\alpha\in(1/2,1), then the scaling limit of N~a−N~b\widetilde{N}^{a}-\widetilde{N}^{b} is continuous and its derivative has Hölder regularity of order α−1/2−ε\alpha-1/2-\varepsilon for any ε>0\varepsilon>0, see [[40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes")]. For H0>3/4H\_{0}>3/4, we know from [[14](https://arxiv.org/html/2601.23172v2#bib.bib5 "How smooth is the drift of the mixed fractional Brownian motion?")] that AtA\_{t} is differentiable and its derivative has a Hölder regularity of order 2​H0−3/2−ε2H\_{0}-3/2-\varepsilon for any ε>0\varepsilon>0. Hence the natural choice in the Hawkes approximation is to take

|  |  |  |
| --- | --- | --- |
|  | α=2​H0−1.\alpha=2H\_{0}-1. |  |

We therefore obtain the following link between the core order flow, the market impact exponent, and the roughness of price volatility.

###### Theorem 4.1.

Under the previous approximations, we have

|  |  |  |
| --- | --- | --- |
|  | M​I​(t)∼t2−2​H0, for ​t≤1,MI(t)\sim t^{2-2H\_{0}},\text{ for }t\leq 1, |  |

|  |  |  |
| --- | --- | --- |
|  | M​I​(t)∼t2−2​H0−(t−1)2−2​H0, for ​t>1.MI(t)\sim t^{2-2H\_{0}}-{(t-1)}^{2-2H\_{0}},\text{ for }t>1. |  |

Furthermore, the volatility of the price exhibits a rough behavior with a Hurst parameter 2​H0−3/22H\_{0}-3/2.

Theorem [4.1](https://arxiv.org/html/2601.23172v2#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") provides a structural relation between core order flow memory, market impact shape, and rough volatility. The square-root law corresponds to H0=3/4H\_{0}=3/4, implying zero Hurst parameter for the volatility and a roughness exponent of 1/41/4 for the unsigned volume. Hence square-root impact ariswes under moderate persistence of the core flow. The reaction flow is essential in this link because it induces the mixed fractional Brownian motion structure. Without reaction flow, a pure core-driven order flow would require H0H\_{0} close to one to generate a square-root impact.

###### Remark 4.2.

The volatility appearing in Theorem [4.1](https://arxiv.org/html/2601.23172v2#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") should be interpreted as an extraday volatility. This is because in the applied results from [[42](https://arxiv.org/html/2601.23172v2#bib.bib393 "No-arbitrage implies power-law market impact and rough volatility")], the authors establish a connection between volatility roughness and the tail behavior of the underlying Hawkes processes by studying the scaling limit of price dynamics. Therefore, the volatility under consideration here corresponds to a time scale that is long enough for prices to exhibit diffusive behavior. Extraday volatilities are known to have Hurst exponents between 0.050.05 and 0.150.15, which agrees well with our results for the value of the Hurst parameter of the volatility. Note however that forthcoming studies show that volatility is also rough at the intraday scale [[18](https://arxiv.org/html/2601.23172v2#bib.bib669 "Intraday volatility dynamics")], with Hurst exponents around 0.250.25, so larger than typical values for extraday volatility. This is in line with our findings for the intraday unsigned order flow, which is obviously tightly linked to intraday volatility, and has a Hurst exponent larger than the one of the extraday volatility in our model.

## 5 Conclusion

This paper develops a unified modeling framework for the joint dynamics of signed order flow, unsigned volume, market impact and volatility. This allows us to capture salient empirical properties of all of these quantities with a single structural parameter, inherited from the persistence of the core order flow in the model’s microfoundation:

* ∙\bullet

  Persistent signed order flow.
  The signed order flow is a mixed fractional process, with diffusive behavior at very high-frequency and persistence H0H\_{0} emerging at larger scales.
* ∙\bullet

  Power-law market impact scaling.
  The average price response to a large order follows a power law with exponent 2−2​H02-2H\_{0}.
* ∙\bullet

  Rough volatility.
  (Extraday) volatility sample paths are rough, with Hurst exponent 2​H0−3/22H\_{0}-3/2.
* ∙\bullet

  Rough traded volume.
  Unsigned traded volume exhibits a rough structure too, with Hurst parameter H0−1/2H\_{0}-1/2, close to intraday volatility dynamics.

In particular, with the values of H0≈0.75H\_{0}\approx 0.75–0.80.8 esimtated from signed order flow data, this model consistently reproduce all the stylized facts mentioned in the introduction, in line with Figures [4](https://arxiv.org/html/2601.23172v2#S1.F4 "Figure 4 ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") and [5](https://arxiv.org/html/2601.23172v2#S1.F5 "Figure 5 ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."). Interestingly, this provides fresh mathematical and econometric support for the view that financial markets are at the edge of criticality. To wit, prices are diffusive (Hurst parameter very near 1/2 to preclude arbitrage), the Hurst parameter for volatility is close to zero, and the mixed-fractional order flow is just about a semimartingale (in that its fractional part has a Hurst parameter just above 3/43/4).

On a less technical level, our findings highlight that despite the proliferation of reactive trading, the structure of financial markets continues to be governed by the slow, persistent rhythm of the core order flow.

## References

* [1]
  L. Bachelier (1900)
  Théorie de la spéculation.
  Annales Scientifiques de l’École Normale Supérieure 17,  pp. 21–86.
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p1.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [2]
  C. Bayer, P. K. Friz, and J. Gatheral (2016)
  Pricing under rough volatility.
  Quantitative Finance 16 (6),  pp. 887–904.
  Cited by: [footnote 6](https://arxiv.org/html/2601.23172v2#footnote6 "In item ∙ ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [3]
  M. Bennedsen, A. Lunde, and M. S. Pakkanen (2022)
  Decoupling the short and long term behavior of stochastic volatility.
  Journal of Financial Econometrics 20 (5),  pp. 961–1006.
  Cited by: [footnote 6](https://arxiv.org/html/2601.23172v2#footnote6 "In item ∙ ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [4]
  M. Benzaquen and J. Bouchaud (2018)
  Market impact with multi-timescale liquidity.
  Quantitative Finance 18 (11),  pp. 1781–1790.
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p4.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [5]
  S. Bernstein (1929)
  Sur les fonctions absolument monotones.
  Acta Mathematica 52,  pp. 1–66.
  External Links: [Document](https://dx.doi.org/10.1007/BF02592629)
  Cited by: [Assumption A](https://arxiv.org/html/2601.23172v2#Thmassumption1.p1.7.5 "Assumption A. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [6]
  N. Bershova and D. Rakhlin (2013)
  The non-linear market impact of large trades: Evidence from buy-side order flow.
  Quantitative Finance 13 (11),  pp. 1759–1778.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix2.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [7]
  P. Billingsley (1968)
  Convergence of Probability Measures.
   Wiley-Interscience.
  Cited by: [§B.1](https://arxiv.org/html/2601.23172v2#A2.SS1.1.p1.6 "Proof. ‣ B.1 Proof of Theorem 3.1 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [8]
  F. Black and M. Scholes (1973)
  The pricing of options and corporate liabilities.
  Journal of Political Economy 81 (3),  pp. 637–654.
  External Links: ISSN 00223808, 1537534X,
  [Link](http://www.jstor.org/stable/1831029)
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p1.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [9]
  A. E. Bolko, K. Christensen, M. S. Pakkanen, and B. Veliyev (2023)
  A GMM approach to estimate the roughness of stochastic volatility.
  Journal of Econometrics 235 (2),  pp. 745–778.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix1.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [10]
  J. Bouchaud, D. Farmer, and F. Lillo (2009)
  How markets slowly digest changes in supply and demand.
  In Handbook of financial markets: dynamics and evolution,
   pp. 57–160.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix1.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [11]
  J. Bouchaud, Y. Gefen, M. Potters, and M. Wyart (2004)
  Fluctuations and response in financial markets: the subtle nature of ‘random’ price changes.
  Quantitative Finance 4 (2),  pp. 176–190.
  External Links: [Document](https://dx.doi.org/10.1088/1469-7688/4/2/006)
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix2.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [12]
  R. Carmona and K. Webster (2019)
  The self-financing equation in limit order book markets.
  Finance and Stochastics 23 (3),  pp. 729–759.
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p3.2 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [13]
  P. Cheridito (2001)
  Mixed fractional Brownian motion.
  Bernoulli 7 (6),  pp. 913–934.
  External Links: [Document](https://dx.doi.org/10.3150/bj/1199406791)
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p10.2 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§1](https://arxiv.org/html/2601.23172v2#S1.p8.5 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§4](https://arxiv.org/html/2601.23172v2#S4.p5.8 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [14]
  P. Chigansky and M. Kleptsyna (2025)
  How smooth is the drift of the mixed fractional Brownian motion?.
  Note: Preprint
  Cited by: [§4](https://arxiv.org/html/2601.23172v2#S4.p5.20 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [15]
  C. Chong, T. Delerue, and F. Mies (2025)
  Rate-optimal estimation of mixed semimartingales.
  Annals of Statistics 153 (1),  pp. 219–244.
  Cited by: [Figure 4](https://arxiv.org/html/2601.23172v2#S1.F4.10.4.4 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [Figure 4](https://arxiv.org/html/2601.23172v2#S1.F4.5.4.4 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.1](https://arxiv.org/html/2601.23172v2#S3.SS1.p8.6 "3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.3](https://arxiv.org/html/2601.23172v2#S3.SS3.p7.3 "3.3 Scaling limits for the global order flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [16]
  C. Chong, M. Hoffmann, Y. Liu, M. Rosenbaum, and G. Szymanski (2024)
  Statistical inference for rough volatility: Central limit theorems.
  Annals of Applied Probability 34 (3),  pp. 2600–2649.
  Cited by: [Figure 5](https://arxiv.org/html/2601.23172v2#S1.F5.3.2.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [Figure 5](https://arxiv.org/html/2601.23172v2#S1.F5.6.2.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.1](https://arxiv.org/html/2601.23172v2#S3.SS1.p8.6 "3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [17]
  C. Chong, M. Hoffmann, Y. Liu, M. Rosenbaum, and G. Szymanski (2024)
  Statistical inference for rough volatility: Minimax theory.
  The Annals of Statistics 52 (4),  pp. 1277–1306.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix1.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [18]
  C. Chong, M. Hoffmann, M. Rosenbaum, and G. Szymanski (2026)
  Intraday volatility dynamics.
  Note: Preprint
  Cited by: [Figure 5](https://arxiv.org/html/2601.23172v2#S1.F5.3.2.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [Figure 5](https://arxiv.org/html/2601.23172v2#S1.F5.6.2.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [Remark 4.2](https://arxiv.org/html/2601.23172v2#S4.Thmtheorem2.p1.3.3 "Remark 4.2. ‣ 4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [19]
  C. Chong and V. Todorov (2025)
  A nonparametric test for rough volatility.
  Journal of the American Statistical Association 120 (552),  pp. 2772–2783.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix1.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [20]
  Z. Ciesielski, G. Kerkyacharian, and B. Roynette (1993)
  Quelques espaces fonctionnels associés à des processus gaussiens.
  Studia Mathematica 107,  pp. 171–204.
  Cited by: [§3.1](https://arxiv.org/html/2601.23172v2#S3.SS1.p5.4 "3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [21]
  F. Comte and E. Renault (1996)
  Long memory continuous time models.
  Journal of Econometrics 73 (1),  pp. 101–149.
  Cited by: [footnote 6](https://arxiv.org/html/2601.23172v2#footnote6 "In item ∙ ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [22]
  K. Dayri and M. Rosenbaum (2015)
  Large tick assets: implicit spread and optimal tick size.
  Market Microstructure and Liquidity 1 (01),  pp. 1550003.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix2.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [23]
  J. Donier, J. Bonart, I. Mastromatteo, and J. Bouchaud (2015)
  A fully consistent, minimal model for non-linear market impact.
  Quantitative Finance 15 (7),  pp. 1109–1121.
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p4.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [24]
  O. El Euch, M. Fukasawa, and M. Rosenbaum (2018)
  The microstructural foundations of leverage effect and rough volatility.
  Finance and Stochastics 22 (2),  pp. 241–280.
  Cited by: [§B.4](https://arxiv.org/html/2601.23172v2#A2.SS4.p1.1 "B.4 Proof of Theorem 3.4 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§B.4](https://arxiv.org/html/2601.23172v2#A2.SS4.p5.2 "B.4 Proof of Theorem 3.4 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§B.7](https://arxiv.org/html/2601.23172v2#A2.SS7.p2.1 "B.7 Proof of Theorem 3.6 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.2](https://arxiv.org/html/2601.23172v2#S3.SS2.p1.3 "3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.2](https://arxiv.org/html/2601.23172v2#S3.SS2.p4.16 "3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.2](https://arxiv.org/html/2601.23172v2#S3.SS2.p4.3 "3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.3](https://arxiv.org/html/2601.23172v2#S3.SS3.p3.2 "3.3 Scaling limits for the global order flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [25]
  O. El Euch and M. Rosenbaum (2019)
  The characteristic function of rough Heston models.
  Mathematical Finance 29 (1),  pp. 3–38.
  Cited by: [Appendix A](https://arxiv.org/html/2601.23172v2#A1.p1.1 "Appendix A Useful results about Hawkes processes ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.1](https://arxiv.org/html/2601.23172v2#S3.SS1.p5.4 "3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [26]
  D. Farmer, A. Gerig, F. Lillo, and S. Mike (2006)
  Market efficiency and the long-memory of supply and demand: is price impact variable and permanent or fixed and temporary?.
  Quantitative Finance 6 (02),  pp. 107–112.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix1.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [27]
  D. Farmer, A. Gerig, F. Lillo, and H. Waelbroeck (2013)
  How efficiency shapes market impact.
  Quantitative Finance 13 (11),  pp. 1743–1758.
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p4.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [28]
  A. Frazzini, R. Israel, and T. J. Moskowitz (2018)
  Trading costs.
  Note: Preprint
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix2.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [29]
  J. Gatheral, T. Jaisson, and M. Rosenbaum (2018)
  Volatility is rough.
  Quantitative Finance 18 (6),  pp. 933–949.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix2.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix1.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [footnote 6](https://arxiv.org/html/2601.23172v2#footnote6 "In item ∙ ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [30]
  J. Gatheral (2010)
  No-dynamic-arbitrage and market impact.
  Quantitative Finance 10 (7),  pp. 749–759.
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p4.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§4](https://arxiv.org/html/2601.23172v2#S4.p2.1 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [31]
  G. Gripenberg, S. Londen, and O. Staffans (1990)
  Volterra integral and functional equations.
  Encyclopedia of Mathematics and its Applications, Vol. 34, Cambridge University Press, Cambridge.
  External Links: [Document](https://dx.doi.org/10.1017/CBO9780511662805)
  Cited by: [§B.1](https://arxiv.org/html/2601.23172v2#A2.SS1.2.p2.6 "Proof. ‣ B.1 Proof of Theorem 3.1 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [32]
  P. Guasoni and M. Weber (2017)
  Dynamic trading volume.
  Mathematical Finance 27 (2),  pp. 313–349.
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p3.2 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [33]
  X. Han and A. Schied (2025)
  On the rate of convergence of estimating the Hurst parameter of rough stochastic volatility models.
  SIAM Journal on Financial Mathematics 16 (4),  pp. 1336–1349.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix1.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [34]
  S. J. Hardiman, N. Bercot, and J. Bouchaud (2013)
  Critical reflexivity in financial markets: a Hawkes process analysis.
  The European Physical Journal B 86,  pp. 1–9.
  Cited by: [§3.1](https://arxiv.org/html/2601.23172v2#S3.SS1.p2.4 "3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [35]
  H. J. Haubold, A. M. Mathai, and R. K. Saxena (2011)
  Mittag-Leffler functions and their applications.
  Journal of Applied Mathematics 2011,  pp. 1–51.
  External Links: [Document](https://dx.doi.org/10.1155/2011/298628),
  [Link](https://ideas.repec.org/a/hin/jnljam/298628.html)
  Cited by: [§3.1](https://arxiv.org/html/2601.23172v2#S3.SS1.p4.12 "3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [36]
  U. Horst and W. Xu (2022)
  The microstructure of stochastic volatility models with self-exciting jump dynamics.
  The Annals of Applied Probability 32 (6),  pp. 4568–4610.
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p6.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [37]
  G. Huberman and W. Stanzl (2004)
  Price manipulation and quasi-arbitrage.
  Econometrica 72 (4),  pp. 1247–1275.
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p4.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§4](https://arxiv.org/html/2601.23172v2#S4.p2.1 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [38]
  J. Jacod and A. N. Shiryaev (1987)
  Limit Theorems for Stochastic Processes.
   Springer, Berlin, Heidelberg.
  Cited by: [§B.1](https://arxiv.org/html/2601.23172v2#A2.SS1.2.p2.10 "Proof. ‣ B.1 Proof of Theorem 3.1 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [39]
  T. Jaisson and M. Rosenbaum (2015)
  Limit theorems for nearly unstable Hawkes processes.
  The Annals of Applied Probability 25 (2),  pp. 600–631.
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p6.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [40]
  T. Jaisson and M. Rosenbaum (2016)
  Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes.
  The Annals of Applied Probability 26 (5),  pp. 2860–2882.
  Cited by: [§B.1](https://arxiv.org/html/2601.23172v2#A2.SS1.1.p1.10 "Proof. ‣ B.1 Proof of Theorem 3.1 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§B.1](https://arxiv.org/html/2601.23172v2#A2.SS1.2.p2.10 "Proof. ‣ B.1 Proof of Theorem 3.1 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§B.1](https://arxiv.org/html/2601.23172v2#A2.SS1.p1.5 "B.1 Proof of Theorem 3.1 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§B.4](https://arxiv.org/html/2601.23172v2#A2.SS4.p7.3 "B.4 Proof of Theorem 3.4 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§B.4](https://arxiv.org/html/2601.23172v2#A2.SS4.p7.7 "B.4 Proof of Theorem 3.4 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§B.5](https://arxiv.org/html/2601.23172v2#A2.SS5.p1.1 "B.5 Proof of Hölder regularity in Theorem 3.4 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§B.5](https://arxiv.org/html/2601.23172v2#A2.SS5.p1.2 "B.5 Proof of Hölder regularity in Theorem 3.4 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§B.5](https://arxiv.org/html/2601.23172v2#A2.SS5.p3.9 "B.5 Proof of Hölder regularity in Theorem 3.4 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§1](https://arxiv.org/html/2601.23172v2#S1.p6.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.1](https://arxiv.org/html/2601.23172v2#S3.SS1.p1.3 "3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.1](https://arxiv.org/html/2601.23172v2#S3.SS1.p5.4 "3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§4](https://arxiv.org/html/2601.23172v2#S4.p5.20 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [41]
  T. Jaisson (2015)
  Market impact as anticipation of the order flow imbalance.
  Quantitative Finance 15 (7),  pp. 1123–1135.
  Cited by: [§4](https://arxiv.org/html/2601.23172v2#S4.p2.1 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§4](https://arxiv.org/html/2601.23172v2#S4.p3.7 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [42]
  P. Jusselin and M. Rosenbaum (2020)
  No-arbitrage implies power-law market impact and rough volatility.
  Mathematical Finance 30 (4),  pp. 1309–1336.
  Cited by: [§1](https://arxiv.org/html/2601.23172v2#S1.p11.2 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§1](https://arxiv.org/html/2601.23172v2#S1.p4.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.1](https://arxiv.org/html/2601.23172v2#S3.SS1.p5.4 "3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.2](https://arxiv.org/html/2601.23172v2#S3.SS2.p2.2 "3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.2](https://arxiv.org/html/2601.23172v2#S3.SS2.p3.1 "3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [Remark 4.2](https://arxiv.org/html/2601.23172v2#S4.Thmtheorem2.p1.3.3 "Remark 4.2. ‣ 4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§4](https://arxiv.org/html/2601.23172v2#S4.p1.1 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§4](https://arxiv.org/html/2601.23172v2#S4.p2.1 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§4](https://arxiv.org/html/2601.23172v2#S4.p3.11 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§4](https://arxiv.org/html/2601.23172v2#S4.p3.7 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§4](https://arxiv.org/html/2601.23172v2#S4.p4.1 "4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [43]
  J. M. Karpoff (1987)
  The relation between price changes and trading volume: a survey.
  Journal of Financial and Quantitative Analysis 22 (1),  pp. 109–126.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix2.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [44]
  A. S. Kyle and A. A. Obizhaeva (2016)
  Market microstructure invariance: empirical hypotheses.
  Econometrica 84 (4),  pp. 1345–1404.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix2.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [45]
  J. Li, P. C. B. Phillips, S. Shi, and J. Yu (2025)
  Weak identification of long memory with implications for volatility modeling.
  Review of Financial Studies 38,  pp. 3117–3148.
  Cited by: [footnote 6](https://arxiv.org/html/2601.23172v2#footnote6 "In item ∙ ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [46]
  J. Li and D. Xiu (2016)
  Generalized method of integrated moments for high-frequency data.
  Econometrica 84 (4),  pp. 1613–1633.
  Cited by: [Figure 5](https://arxiv.org/html/2601.23172v2#S1.F5.3.2.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [Figure 5](https://arxiv.org/html/2601.23172v2#S1.F5.6.2.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [47]
  F. Lillo and D. Farmer (2004)
  The long memory of the efficient market.
  Studies in Nonlinear Dynamics & Econometrics 8 (3).
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix1.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [48]
  F. Lillo, S. Mike, and J. D. Farmer (2005)
  Theory for long memory in supply and demand.
  Physical Review E 71,  pp. 066122.
  External Links: [Document](https://dx.doi.org/10.1103/PhysRevE.71.066122)
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix1.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [footnote 7](https://arxiv.org/html/2601.23172v2#footnote7 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [49]
  A. W. Lo and J. Wang (2000)
  Trading volume: definitions, data analysis, and implications of portfolio theory.
  Review of Financial Studies 13 (2),  pp. 257–300.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix1.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [50]
  A. W. Lo (1991)
  Long-term memory in stock market prices.
  Econometrica 59 (5),  pp. 1279–13131279–1313.
  Cited by: [footnote 6](https://arxiv.org/html/2601.23172v2#footnote6 "In item ∙ ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [51]
  T. F. Loeb (1983)
  Trading cost: the critical link between investment information and results.
  Financial Analysts Journal 39 (3),  pp. 39–44.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix2.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [52]
  A. Madhavan, M. Richardson, and M. Roomans (1997)
  Why do security prices change? A transaction-level analysis of NYSE stocks.
  Review of Financial Studies 10 (4),  pp. 1035–1064.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix2.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [53]
  G. Maitrier and J. Bouchaud (2025)
  The subtle interplay between square-root impact, order imbalance & volatility: a unifying framework.
  Note: Preprint
  Cited by: [footnote 11](https://arxiv.org/html/2601.23172v2#footnote11 "In 4 From order flow to market impact and rough volatility ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [footnote 8](https://arxiv.org/html/2601.23172v2#footnote8 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [54]
  G. Maitrier, G. Loeper, and J. Bouchaud (2025)
  The subtle interplay between square-root impact, order imbalance & volatility II: an artificial market generator.
  Note: Preprint
  Cited by: [footnote 8](https://arxiv.org/html/2601.23172v2#footnote8 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [55]
  M. Naviglio, G. Bormetti, F. Campigli, G. Rodikov, and F. Lillo (2025)
  Why is the estimation of metaorder impact with public market data so challenging?.
  Note: Preprint
  Cited by: [footnote 8](https://arxiv.org/html/2601.23172v2#footnote8 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [56]
  Y. Ouazzani Chahdi, M. Rosenbaum, and G. Szymanski (2026)
  A theory of passive market impact.
  Finance and Stochastics to appear.
  Cited by: [Appendix A](https://arxiv.org/html/2601.23172v2#A1.p1.1 "Appendix A Useful results about Hawkes processes ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [57]
  Y. Sato and K. Kanazawa (2023)
  Inferring microscopic financial information from the long memory in market-order flow: a quantitative test of the Lillo-Mike-Farmer model.
  Physical Review Letters 131 (19),  pp. 197401.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix1.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [footnote 7](https://arxiv.org/html/2601.23172v2#footnote7 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [58]
  Y. Sato and K. Kanazawa (2025-12)
  Strict universality of the square-root law in price impact across stocks: a complete survey of the Tokyo stock exchange.
  Physical Review Letters 135 (25).
  External Links: ISSN 1079-7114,
  [Link](http://dx.doi.org/10.1103/65jz-81kv),
  [Document](https://dx.doi.org/10.1103/65jz-81kv)
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix2.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [59]
  S. Shi, J. Yu, and C. Zhang (2025)
  Fractional Gaussian noise: spectral density and estimation methods.
  Journal of Time Series Analysis 46 (6),  pp. 1146–1174.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix1.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [60]
  G. Szymanski and T. Takabatake (2026)
  Asymptotic efficiency for mixed fractional Brownian motion.
  Note: Working paper
  Cited by: [Figure 4](https://arxiv.org/html/2601.23172v2#S1.F4.10.4.4 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [Figure 4](https://arxiv.org/html/2601.23172v2#S1.F4.5.4.4 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.1](https://arxiv.org/html/2601.23172v2#S3.SS1.p8.6 "3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§3.3](https://arxiv.org/html/2601.23172v2#S3.SS3.p7.3 "3.3 Scaling limits for the global order flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [61]
  B. Tóth, Y. Lemperiere, C. Deremble, J. De Lataillade, J. Kockelkoren, and J. Bouchaud (2011)
  Anomalous price impact and the critical nature of liquidity in financial markets.
  Physical Review X 1 (2),  pp. 021006.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I2.ix2.p1.1 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."),
  [§1](https://arxiv.org/html/2601.23172v2#S1.p4.1 "1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [62]
  X. Wang, J. Yu, and C. Zhang (2024)
  On the optimal forecast with the fractional Brownian motion.
  Quantitative Finance 24 (2),  pp. 337–346.
  Cited by: [footnote 6](https://arxiv.org/html/2601.23172v2#footnote6 "In item ∙ ‣ 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* [63]
  M. Wyart, J. Bouchaud, J. Kockelkoren, M. Potters, and M. Vettorazzo (2008)
  Relation between bid–ask spread, impact and volatility in order-driven markets.
  Quantitative Finance 8 (1),  pp. 41–57.
  Cited by: [item ∙\bullet](https://arxiv.org/html/2601.23172v2#S1.I1.ix2.p1.2 "In 1 Introduction ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").

## Appendix A Useful results about Hawkes processes

In this section, we summarize some useful results about Hawkes processes with time-varying baseline. The proofs are omitted for conciseness. They can however be easily adapted from the constant baseline case, see for instance [[25](https://arxiv.org/html/2601.23172v2#bib.bib222 "The characteristic function of rough Heston models"), [56](https://arxiv.org/html/2601.23172v2#bib.bib671 "A theory of passive market impact")].

###### Definition A.1.

A Hawkes process with baseline (or background rate) μ:[0,∞)→[0,∞)\mu:[0,\infty)\to[0,\infty) and self-exciting kernel φ:[0,∞)→ℝ\varphi:[0,\infty)\to\mathbb{R} is a process NN adapted to some filtration (ℱt)t(\mathcal{F}\_{t})\_{t} such that the compensator Λ\Lambda of NN has the form Λt=∫0tλs​𝑑s\Lambda\_{t}=\int\_{0}^{t}\lambda\_{s}\,ds where

|  |  |  |
| --- | --- | --- |
|  | λt=μt+∫0t−φ​(t−s)​𝑑Ns.\lambda\_{t}=\mu\_{t}+\int\_{0}^{t-}\varphi(t-s)\,dN\_{s}. |  |

###### Lemma A.2.

Define M=N−ΛM=N-\Lambda and ψ=∑k≥1φ∗k\psi=\sum\_{k\geq 1}\varphi^{\*k} where φ∗k\varphi^{\*k} stands for the kk-fold convolution of φ\varphi. Then for any 0≤t≤T0\leq t\leq T, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | λt\displaystyle\lambda\_{t} | =μt+∫0tψ​(t−s)​μs​𝑑s+∫0t−ψ​(t−s)​𝑑Ms,\displaystyle=\mu\_{t}+\int\_{0}^{t}\psi(t-s)\mu\_{s}\,ds+\int\_{0}^{t-}\psi(t-s)dM\_{s}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tλs​𝑑s\displaystyle\int\_{0}^{t}\lambda\_{s}\,ds | =∫0tμs​𝑑s+∫0tψ​(t−s)​∫0sμu​𝑑u​𝑑s+∫0tψ​(t−s)​Ms​𝑑s.\displaystyle=\int\_{0}^{t}\mu\_{s}\,ds+\int\_{0}^{t}\psi(t-s)\int\_{0}^{s}\mu\_{u}\,du\,ds+\int\_{0}^{t}\psi(t-s)M\_{s}\,ds. |  |

###### Lemma A.3.

For any 0≤t≤T0\leq t\leq T, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[λt]\displaystyle\mathbb{E}[\lambda\_{t}] | =μt+∫0tψ​(t−s)​μs​𝑑s.\displaystyle=\mu\_{t}+\int\_{0}^{t}\psi(t-s)\mu\_{s}\,ds. |  |

## Appendix B Proof of the results of Section [3](https://arxiv.org/html/2601.23172v2#S3 "3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")

### B.1 Proof of Theorem [3.1](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")

Consider a standard Hawkes process NTN^{T} with same baseline intensity νT\nu^{T} and kernel φ0T\varphi\_{0}^{T} as F±,TF^{\pm,T}. We then define

|  |  |  |
| --- | --- | --- |
|  | N¯tT=1−a0TT​νT​Nt​TT,Λ¯tT=1−a0TT​νT​Λt​TT,M¯tT=(1−a0TT​νT)1/2​Mt​TT.\begin{split}&\overline{N}^{T}\_{t}=\frac{1-a\_{0}^{T}}{T\nu^{T}}N^{T}\_{tT},\\ &\overline{\Lambda}^{T}\_{t}=\frac{1-a^{T}\_{0}}{T\nu^{T}}\Lambda^{T}\_{tT},\\ &\overline{M}^{T}\_{t}=\Big(\frac{1-a^{T}\_{0}}{T\nu^{T}}\Big)^{1/2}M^{T}\_{tT}.\end{split} |  |

The proof is then split into five parts:

* •

  Step 1: We show that the sequence (Λ¯T)(\overline{\Lambda}^{T}) is C-tight.
* •

  Step 2: We show that the sequences of martingales (X¯T−Λ¯T)(\overline{X}^{T}-\overline{\Lambda}^{T}) tends to zero in probability, uniformly on [0,1][0,1].
* •

  Step 3: Under Assumptions [A](https://arxiv.org/html/2601.23172v2#Thmassumption1 "Assumption A. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") and [B](https://arxiv.org/html/2601.23172v2#Thmassumption2 "Assumption B. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), the sequence (M¯T,X¯T)(\overline{M}^{T},\overline{X}^{T}) is tight. Furthermore, if (Z,X)(Z,X) is a limit point of (M¯T,X¯T)(\overline{M}^{T},\overline{X}^{T}), then ZZ is a continuous martingale and [Z,Z]=X[Z,Z]=X.
* •

  Step 4: We conclude the convergence of the process (N¯tT,Λ¯tT,M¯tT)(\overline{N}^{T}\_{t},\overline{\Lambda}^{T}\_{t},\overline{M}^{T}\_{t}) in distribution for the Skorokhod topology towards (X,X,Z)(X,X,Z) where XX and ZZ are given in Theorem [3.1](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").
* •

  Step 5: We prove the Hölder property for XX.

In this paper, we only prove that Λ¯T\overline{\Lambda}^{T} is tight; the remaining steps can be found in the proof of Theorem 3.1 in [[40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes")]. Let us now prove the following lemma.

###### Lemma B.1.

The sequence (Λ¯T)(\overline{\Lambda}^{T}) is C-tight.

###### Proof.

Let ψ0T=∑k≥1(φ0T)∗k\psi\_{0}^{T}=\sum\_{k\geq 1}(\varphi\_{0}^{T})^{\*k}. We know from Lemma [A.3](https://arxiv.org/html/2601.23172v2#A1.Thmtheorem3 "Lemma A.3. ‣ Appendix A Useful results about Hawkes processes ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") and Assumption [A](https://arxiv.org/html/2601.23172v2#Thmassumption1 "Assumption A. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[λtT]=νT+∫0tψ0T​(t−s)​νT​𝑑s≤νT​(1+‖ψ0T‖1)≤νT1−a0T\mathbb{E}[\lambda^{T}\_{t}]=\nu^{T}+\int\_{0}^{t}\psi\_{0}^{T}(t-s)\nu^{T}\,ds\leq\nu^{T}(1+{|\kern-1.07639pt|\psi\_{0}^{T}|\kern-1.07639pt|}\_{1})\leq\frac{\nu^{T}}{1-a\_{0}^{T}} |  |

and from Assumption [A](https://arxiv.org/html/2601.23172v2#Thmassumption1 "Assumption A. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") that ‖ψ0T‖1=(1−a0T)−1​a0T{|\kern-1.07639pt|\psi\_{0}^{T}|\kern-1.07639pt|}\_{1}=(1-a\_{0}^{T})^{-1}a\_{0}^{T}.
This implies

|  |  |  |
| --- | --- | --- |
|  | 1−a0TνT​supt𝔼​[λtT]≤1\frac{1-a^{T}\_{0}}{\nu^{T}}\sup\_{t}\mathbb{E}[\lambda\_{t}^{T}]\leq 1 |  |

and therefore

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[X¯1T]=𝔼​[Λ¯1T]≤1.\mathbb{E}[\overline{X}\_{1}^{T}]=\mathbb{E}[\overline{\Lambda}\_{1}^{T}]\leq 1. |  |

Moreover, since

|  |  |  |
| --- | --- | --- |
|  | ⟨M¯tT,M¯tT⟩=Λ¯tT\big<\overline{M}^{T}\_{t},\overline{M}^{T}\_{t}\big>=\overline{\Lambda}^{T}\_{t} |  |

the Burkholder-Davis-Gundy inequality then ensures

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt≤1|M¯tT|2]≤C\mathbb{E}[\sup\_{t\leq 1}|\overline{M}\_{t}^{T}|^{2}]\leq C |  |

for a constant C>0C>0. We now prove the tightness of Λ¯T\overline{\Lambda}^{T}. We write

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ¯tT\displaystyle\overline{\Lambda}^{T}\_{t} | =1−a0TT​νT​(νT​t​T+∫0t​Tψ0T​(t​T−s)​s​𝑑s​νT+∫0t​Tψ0T​(t​T−s)​MsT​𝑑s)\displaystyle=\frac{1-a^{T}\_{0}}{T\nu^{T}}\Big(\nu^{T}tT+\int\_{0}^{tT}\psi\_{0}^{T}(tT-s)s\,ds\nu^{T}+\int\_{0}^{tT}\psi\_{0}^{T}(tT-s)M^{T}\_{s}\,ds\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =((1−a0T)​t+T​(1−a0T)​∫0t​Tψ0T​(T​(t−s))​s​𝑑s)+1−a0TT​νT​∫0tT​ψ0T​(T​(t−s))​MT​sT​𝑑s.\displaystyle=\Big((1-a^{T}\_{0})t+T(1-a^{T}\_{0})\int\_{0}^{tT}\psi\_{0}^{T}(T(t-s))s\,ds\Big)+\frac{1-a^{T}\_{0}}{T\nu^{T}}\int\_{0}^{t}T\psi\_{0}^{T}(T(t-s))M^{T}\_{Ts}\,ds. |  |

The authors in [[40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes")] prove the uniform convergence of the first term towards the process

|  |  |  |
| --- | --- | --- |
|  | ∫0ts​fα0,λ0​(t−s)​𝑑s,\int\_{0}^{t}sf^{\alpha\_{0},\lambda\_{0}}(t-s)ds, |  |

and therefore is tight. We then focus on the second one and we set

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ~tT\displaystyle\widetilde{\Lambda}^{T}\_{t} | =1−a0TT​νT​∫0tT​ψ0T​(T​(t−s))​MT​sT​𝑑s\displaystyle=\frac{1-a^{T}\_{0}}{T\nu^{T}}\int\_{0}^{t}T\psi\_{0}^{T}(T(t-s))M^{T}\_{Ts}\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−a0TT​νT)1/2​∫0tT​ψ0T​(T​(t−s))​M¯sT​𝑑s\displaystyle=\Big(\frac{1-a^{T}\_{0}}{T\nu^{T}}\Big)^{1/2}\int\_{0}^{t}T\psi\_{0}^{T}(T(t-s))\overline{M}^{T}\_{s}\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1(1−a0T)​T​νT)1/2​∫0tρ0T​(t−s)​M¯sT​𝑑s\displaystyle=\Big(\frac{1}{(1-a^{T}\_{0})T\nu^{T}}\Big)^{1/2}\int\_{0}^{t}\rho\_{0}^{T}(t-s)\overline{M}^{T}\_{s}\,ds |  |

with

|  |  |  |
| --- | --- | --- |
|  | ρ0T​(t)=(1−a0T)​T​ψ0T​(T​t).\rho\_{0}^{T}(t)=(1-a^{T}\_{0})T\psi\_{0}^{T}(Tt). |  |

To prove the tightness of Λ~T\widetilde{\Lambda}^{T}, we use Theorem 7.3. in [[7](https://arxiv.org/html/2601.23172v2#bib.bib90 "Convergence of Probability Measures")] which states that Λ~T\widetilde{\Lambda}^{T} is tight provided the following two conditions hold:

* •

  For each η>0\eta>0, there exist a>0a>0 such that

  |  |  |  |
  | --- | --- | --- |
  |  | lim supTℙ​(|Λ~0T|≥a)≤η.\limsup\_{T}\mathbb{P}(|\widetilde{\Lambda}\_{0}^{T}|\geq a)\leq\eta. |  |
* •

  For each ε>0\varepsilon>0, we have

  |  |  |  |
  | --- | --- | --- |
  |  | limδ→0lim supTℙ​(ω​(Λ~T;δ)≥ε)=0\lim\_{\delta\to 0}\limsup\_{T}\mathbb{P}(\omega(\widetilde{\Lambda}^{T};\delta)\geq\varepsilon)=0 |  |

  where we use the notation

  |  |  |  |
  | --- | --- | --- |
  |  | ω​(x;δ)=sup|t−s|≤δ,0≤s≤t≤1|x​(t)−x​(s)|.\omega(x;\delta)=\sup\_{|t-s|\leq\delta,0\leq s\leq t\leq 1}|x(t)-x(s)|. |  |

for δ>0\delta>0. The first condition clearly holds.
We prove that Λ~T\widetilde{\Lambda}^{T} verifies the second condition. We first write for 0≤s≤t≤s+δ≤10\leq s\leq t\leq s+\delta\leq 1

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Λ~tT−Λ~sT|\displaystyle|\widetilde{\Lambda}\_{t}^{T}-\widetilde{\Lambda}\_{s}^{T}| | =|(1(1−a0T)​T​νT)1/2​∫0tρ0T​(t−u)​M¯uT​𝑑u−(1(1−a0T)​T​νT)1/2​∫0sρ0T​(s−u)​M¯uT​𝑑u|\displaystyle=\Big|\Big(\frac{1}{(1-a^{T}\_{0})T\nu^{T}}\Big)^{1/2}\int\_{0}^{t}\rho\_{0}^{T}(t-u)\overline{M}^{T}\_{u}\,du-\Big(\frac{1}{(1-a^{T}\_{0})T\nu^{T}}\Big)^{1/2}\int\_{0}^{s}\rho\_{0}^{T}(s-u)\overline{M}^{T}\_{u}\,du\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1(1−a0T)​T​νT)1/2​|∫stρ0T​(t−u)​M¯uT​𝑑u+∫0s(ρ0T​(t−u)−ρ0T​(s−u))​M¯uT​𝑑u|\displaystyle=\Big(\frac{1}{(1-a^{T}\_{0})T\nu^{T}}\Big)^{1/2}\Big|\int\_{s}^{t}\rho\_{0}^{T}(t-u)\overline{M}^{T}\_{u}\,du+\int\_{0}^{s}(\rho\_{0}^{T}(t-u)-\rho\_{0}^{T}(s-u))\overline{M}^{T}\_{u}\,du\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(1(1−a0T)​T​νT)1/2​(∫stρ0T​(t−u)​𝑑u+∫0s|ρ0T​(t−u)−ρ0T​(s−u)|​𝑑u)​supu≤1|M¯uT|.\displaystyle\leq\Big(\frac{1}{(1-a^{T}\_{0})T\nu^{T}}\Big)^{1/2}\Big(\int\_{s}^{t}\rho\_{0}^{T}(t-u)\,du+\int\_{0}^{s}|\rho\_{0}^{T}(t-u)-\rho\_{0}^{T}(s-u)|\,du\Big)\sup\_{u\leq 1}|\overline{M}^{T}\_{u}|. |  |

Under Assumption [A](https://arxiv.org/html/2601.23172v2#Thmassumption1 "Assumption A. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), the kernel φ0\varphi\_{0} is completely monotone and it follows from Theorem 5.4 in [[31](https://arxiv.org/html/2601.23172v2#bib.bib646 "Volterra integral and functional equations")] that ρ0T\rho\_{0}^{T} is decreasing. Since |t−s|≤δ|t-s|\leq\delta, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Λ~tT−Λ~sT|\displaystyle|\widetilde{\Lambda}\_{t}^{T}-\widetilde{\Lambda}\_{s}^{T}| | ≤(1(1−a0T)​T​νT)1/2​(∫0δρ0T​(u)​𝑑u+∫0s|ρ0T​(t−s+u)−ρ0T​(u)|​𝑑u)​supu≤1|M¯uT|\displaystyle\leq\Big(\frac{1}{(1-a^{T}\_{0})T\nu^{T}}\Big)^{1/2}\Big(\int\_{0}^{\delta}\rho\_{0}^{T}(u)\,du+\int\_{0}^{s}|\rho\_{0}^{T}(t-s+u)-\rho\_{0}^{T}(u)|\,du\Big)\sup\_{u\leq 1}|\overline{M}^{T}\_{u}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(1(1−a0T)​T​νT)1/2​(∫0δρ0T​(u)​𝑑u+∫0sρ0T​(u)​𝑑u−∫t−stρ0T​(u)​𝑑u)​supu≤1|M¯uT|\displaystyle\leq\Big(\frac{1}{(1-a^{T}\_{0})T\nu^{T}}\Big)^{1/2}\Big(\int\_{0}^{\delta}\rho\_{0}^{T}(u)\,du+\int\_{0}^{s}\rho\_{0}^{T}(u)\,du-\int\_{t-s}^{t}\rho\_{0}^{T}(u)\,du\Big)\sup\_{u\leq 1}|\overline{M}^{T}\_{u}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​(1(1−a0T)​T​νT)1/2​∫0δρ0T​(u)​𝑑u​supu≤1|M¯uT|.\displaystyle\leq 2\Big(\frac{1}{(1-a^{T}\_{0})T\nu^{T}}\Big)^{1/2}\int\_{0}^{\delta}\rho\_{0}^{T}(u)\,du\sup\_{u\leq 1}|\overline{M}^{T}\_{u}|. |  |

Using Markov’s inequality, we deduce that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ω​(Λ~T;δ)≥ε)≤2​ε−1​(1(1−a0T)​T​νT)1/2​∫0δρ0T​(u)​𝑑u​𝔼​[supu≤1|M¯uT|]≤C′​∫0δρ0T​(u)​𝑑u\mathbb{P}(\omega(\widetilde{\Lambda}^{T};\delta)\geq\varepsilon)\leq 2\varepsilon^{-1}\Big(\frac{1}{(1-a^{T}\_{0})T\nu^{T}}\Big)^{1/2}\int\_{0}^{\delta}\rho\_{0}^{T}(u)\,du\,\mathbb{E}[\sup\_{u\leq 1}|\overline{M}^{T}\_{u}|]\leq C^{\prime}\int\_{0}^{\delta}\rho\_{0}^{T}(u)\,du |  |

for some positive constant C′C^{\prime} and we conclude using

|  |  |  |
| --- | --- | --- |
|  | limδ→0lim supT→∞∫0δρ0T​(u)​𝑑u=0\lim\_{\delta\to 0}\limsup\_{T\to\infty}\int\_{0}^{\delta}\rho\_{0}^{T}(u)\,du=0 |  |

Furthermore, since the maximum jump size of Λ¯T\overline{\Lambda}^{T}, that is (1−a0T)​(T​νT)−1(1-a\_{0}^{T})(T\nu^{T})^{-1}, goes to zero, we conclude that Λ¯T\overline{\Lambda}^{T} is C-tight using Proposition VI-3.26 in [[38](https://arxiv.org/html/2601.23172v2#bib.bib367 "Limit Theorems for Stochastic Processes")]. The rest of the proof can be found in [[40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes")].

### B.2 Proof of Proposition [3.2](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem2 "Proposition 3.2. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")

Suppose α0<1/2\alpha\_{0}<1/2
with the convention fα0,λ0​(u)=0f^{\alpha\_{0},\lambda\_{0}}(u)=0 for u≤0u\leq 0.
We define the forward increment operator Δh​f​(t):=f​(t+h)−f​(t)\Delta\_{h}f(t):=f(t+h)-f(t) for t,h>0t,h>0 and (X,Z)(X,Z) to denote either (F+,Z+)(F^{+},Z^{+}) or (F−,Z−)(F^{-},Z^{-}). We set

|  |  |  |
| --- | --- | --- |
|  | V​(t,h):=𝔼​[(Xt+h−Xt)2].V(t,h):=\mathbb{E}\big[(X\_{t+h}-X\_{t})^{2}\big].\\ |  |

Proving Proposition [3.2](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem2 "Proposition 3.2. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") is equivalent to proving that

|  |  |  |
| --- | --- | --- |
|  | V​(t,h)=O​(h4​α0).V(t,h)=O(h^{4\alpha\_{0}}). |  |

We first decompose Xt=g​(t)+X^tX\_{t}=g(t)+\widehat{X}\_{t} where

|  |  |  |
| --- | --- | --- |
|  | g​(t):=𝔼​[Xt]=∫0ts​fα0,λ0​(t−s)​ds,g(t):=\mathbb{E}[X\_{t}]=\int\_{0}^{t}s\,f^{\alpha\_{0},\lambda\_{0}}(t-s)\,\mathrm{d}s, |  |

and

|  |  |  |
| --- | --- | --- |
|  | X^t=∫0tfα0,λ0​(t−s)​Zs​ds.\widehat{X}\_{t}=\int\_{0}^{t}f^{\alpha\_{0},\lambda\_{0}}(t-s)Z\_{s}\,\mathrm{d}s. |  |

With these notations, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,h)\displaystyle V(t,h) | =𝔼​[(Δh​g​(t)+Δh​X^t)2]=(Δh​g​(t))2+𝔼​[(Δh​X^t)2]\displaystyle=\mathbb{E}\Big[\big(\Delta\_{h}g(t)+\Delta\_{h}\widehat{X}\_{t}\big)^{2}\Big]=\big(\Delta\_{h}g(t)\big)^{2}+\mathbb{E}\big[(\Delta\_{h}\widehat{X}\_{t})^{2}\big] |  |

since 𝔼​[Δh​X^t]=Δh​𝔼​[X^t]=0\mathbb{E}[\Delta\_{h}\widehat{X}\_{t}]=\Delta\_{h}\mathbb{E}[\widehat{X}\_{t}]=0. Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δh​X^t\displaystyle\Delta\_{h}\widehat{X}\_{t} | =∫0t+hfα0,λ0​(t+h−s)​Zs​ds−∫0tfα0,λ0​(t−s)​Zs​ds\displaystyle=\int\_{0}^{t+h}f^{\alpha\_{0},\lambda\_{0}}(t+h-s)Z\_{s}\,\mathrm{d}s-\int\_{0}^{t}f^{\alpha\_{0},\lambda\_{0}}(t-s)Z\_{s}\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0t+h(fα0,λ0​(t+h−s)−fα0,λ0​(t−s))​Zs​ds\displaystyle=\int\_{0}^{t+h}\big(f^{\alpha\_{0},\lambda\_{0}}(t+h-s)-f^{\alpha\_{0},\lambda\_{0}}(t-s)\big)Z\_{s}\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0t+hΔh​fα0,λ0​(t−s)​Zs​ds.\displaystyle=\int\_{0}^{t+h}\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-s)\,Z\_{s}\,\mathrm{d}s. |  |

Thus, we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(Δh​X^t)2]\displaystyle\mathbb{E}\big[(\Delta\_{h}\widehat{X}\_{t})^{2}\big] | =∫0t+h∫0t+hΔh​fα0,λ0​(t−s)​Δh​fα0,λ0​(t−v)​𝔼​[Zs​Zv]​ds​dv\displaystyle=\int\_{0}^{t+h}\!\int\_{0}^{t+h}\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-s)\,\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-v)\,\mathbb{E}[Z\_{s}Z\_{v}]\,\mathrm{d}s\mathrm{d}v |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​∫0t+hg​(s)​Δh​fα0,λ0​(t−s)​(∫st+hΔh​fα0,λ0​(t−v)​dv)​ds.\displaystyle=2\int\_{0}^{t+h}g(s)\,\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-s)\left(\int\_{s}^{t+h}\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-v)\,\mathrm{d}v\right)\mathrm{d}s. |  |

We introduce

|  |  |  |
| --- | --- | --- |
|  | ϱα0,λ0​(x):=∫0xfα0,λ0​(y)​dy,x≥0.\varrho^{\alpha\_{0},\lambda\_{0}}(x):=\int\_{0}^{x}f^{\alpha\_{0},\lambda\_{0}}(y)\,\mathrm{d}y,\qquad x\geq 0. |  |

so that we have ∫st+hΔh​fα0,λ0​(t−v)​dv=Δh​ϱα0,λ0​(t−s)\int\_{s}^{t+h}\!\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-v)\,\mathrm{d}v=\Delta\_{h}\varrho^{\alpha\_{0},\lambda\_{0}}(t-s), and thus

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(Δh​X^t)2]=2​∫0t+hg​(s)​Δh​fα0,λ0​(t−s)​Δh​ϱα0,λ0​(t−s)​ds.\mathbb{E}\big[(\Delta\_{h}\widehat{X}\_{t})^{2}\big]=2\int\_{0}^{t+h}g(s)\,\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-s)\,\Delta\_{h}\varrho^{\alpha\_{0},\lambda\_{0}}(t-s)\,\mathrm{d}s. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,h)=(Δh​g​(t))2+2​∫0t+hg​(s)​Δh​fα0,λ0​(t−s)​Δh​ϱα0,λ0​(t−s)​ds=(Δh​g​(t))2+2​∫0tg​(t−s)​Δh​fα0,λ0​(s)​Δh​ϱα0,λ0​(s)​ds+2​∫tt+hg​(s)​Δh​fα0,λ0​(t−s)​Δh​ϱα0,λ0​(t−s)​ds.\begin{split}V(t,h)&=\big(\Delta\_{h}g(t)\big)^{2}+2\int\_{0}^{t+h}g(s)\,\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-s)\,\Delta\_{h}\varrho^{\alpha\_{0},\lambda\_{0}}(t-s)\,\mathrm{d}s\\ &=\big(\Delta\_{h}g(t)\big)^{2}+2\int\_{0}^{t}g(t-s)\,\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(s)\,\Delta\_{h}\varrho^{\alpha\_{0},\lambda\_{0}}(s)\,\mathrm{d}s\\ &\phantom{=}\;+2\int\_{t}^{t+h}g(s)\,\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-s)\,\Delta\_{h}\varrho^{\alpha\_{0},\lambda\_{0}}(t-s)\,\mathrm{d}s.\end{split} |  | (3) |

We would like to bound gg.
We have for 0≤t≤10\leq t\leq 1 and 0<h≤1−t0<h\leq 1-t,

|  |  |  |
| --- | --- | --- |
|  | |g​(t)|=|∫0ts​fα0,λ0​(t−s)​𝑑s|≤|ϱα0,λ0​(t)|≤1,|g(t)|=\Big|\int\_{0}^{t}sf^{\alpha\_{0},\lambda\_{0}}(t-s)ds\Big|\leq|\varrho^{\alpha\_{0},\lambda\_{0}}(t)|\leq 1, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Δh​g​(t)|\displaystyle|\Delta\_{h}g(t)| | =|∫0t+hs​fα0,λ0​(t+h−s)​𝑑s−∫0ts​fα0,λ0​(t−s)​𝑑s|\displaystyle=\Big|\int\_{0}^{t+h}sf^{\alpha\_{0},\lambda\_{0}}(t+h-s)ds-\int\_{0}^{t}sf^{\alpha\_{0},\lambda\_{0}}(t-s)ds\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|∫0t+h(t+h−s)​fα0,λ0​(s)​𝑑s−∫0t(t−s)​fα0,λ0​(s)​𝑑s|\displaystyle=\Big|\int\_{0}^{t+h}(t+h-s)f^{\alpha\_{0},\lambda\_{0}}(s)ds-\int\_{0}^{t}(t-s)f^{\alpha\_{0},\lambda\_{0}}(s)ds\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤h​|∫0tfα0,λ0​(s)​𝑑s|+|∫tt+h(t+h−s)​fα0,λ0​(s)​𝑑s|\displaystyle\leq h\Big|\int\_{0}^{t}f^{\alpha\_{0},\lambda\_{0}}(s)ds\Big|+\Big|\int\_{t}^{t+h}(t+h-s)f^{\alpha\_{0},\lambda\_{0}}(s)ds\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤h​ϱα0,λ0​(t)+h​|ϱα0,λ0​(t+h)−ϱα0,λ0​(t)|\displaystyle\leq h\varrho^{\alpha\_{0},\lambda\_{0}}(t)+h|\varrho^{\alpha\_{0},\lambda\_{0}}(t+h)-\varrho^{\alpha\_{0},\lambda\_{0}}(t)| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤h.\displaystyle\leq h. |  |

In particular,

|  |  |  |
| --- | --- | --- |
|  | (Δh​g​(t))2=O​(h2).\big(\Delta\_{h}g(t)\big)^{2}=O(h^{2}). |  |

Furthermore, for s∈[t,t+h]s\in[t,t+h],

|  |  |  |
| --- | --- | --- |
|  | Δh​fα0,λ0​(t−s)=fα0,λ0​(t+h−s)andΔh​ϱα0,λ0​(t−s)=ϱα0,λ0​(t+h−s).\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-s)=f^{\alpha\_{0},\lambda\_{0}}(t+h-s)\qquad\text{and}\qquad\Delta\_{h}\varrho^{\alpha\_{0},\lambda\_{0}}(t-s)=\varrho^{\alpha\_{0},\lambda\_{0}}(t+h-s). |  |

By the mean-value theorem, for each t≤st\leq s, we can write
g​(s)=g​(t)+g′​(ξt​(s))​(s−t)g(s)=g(t)+g^{\prime}(\xi\_{t}(s))(s-t)
for some t≤ξt​(s)≤st\leq\xi\_{t}(s)\leq s.
Therefore, the last term of ([3](https://arxiv.org/html/2601.23172v2#A2.E3 "In B.2 Proof of Proposition 3.2 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫tt+hg​(s)​Δh​fα0,λ0​(t−s)\displaystyle\int\_{t}^{t+h}g(s)\,\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-s)\, | Δh​ϱα0,λ0​(t−s)​d​s=g​(t)​∫tt+hfα0,λ0​(t+h−s)​ϱα0,λ0​(t+h−s)​ds\displaystyle\Delta\_{h}\varrho^{\alpha\_{0},\lambda\_{0}}(t-s)\,\mathrm{d}s=g(t)\int\_{t}^{t+h}f^{\alpha\_{0},\lambda\_{0}}(t+h-s)\varrho^{\alpha\_{0},\lambda\_{0}}(t+h-s)\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫tt+hg′​(ξt​(s))​(s−t)​fα0,λ0​(t+h−s)​ϱα0,λ0​(t+h−s)​ds.\displaystyle+\int\_{t}^{t+h}g^{\prime}(\xi\_{t}(s))(s-t)\,f^{\alpha\_{0},\lambda\_{0}}(t+h-s)\varrho^{\alpha\_{0},\lambda\_{0}}(t+h-s)\,\mathrm{d}s. |  |

A change of variables gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫tt+hfα0,λ0​(t+h−s)​ϱα0,λ0​(t+h−s)​ds\displaystyle\int\_{t}^{t+h}f^{\alpha\_{0},\lambda\_{0}}(t+h-s)\varrho^{\alpha\_{0},\lambda\_{0}}(t+h-s)\,\mathrm{d}s | =∫0hfα0,λ0​(v)​ϱα0,λ0​(v)​dv=12​ϱα0,λ0​(h)2.\displaystyle=\int\_{0}^{h}f^{\alpha\_{0},\lambda\_{0}}(v)\varrho^{\alpha\_{0},\lambda\_{0}}(v)\,\mathrm{d}v=\tfrac{1}{2}\varrho^{\alpha\_{0},\lambda\_{0}}(h)^{2}. |  |

Because Δh​g\Delta\_{h}g is bounded, g′g^{\prime} is also bounded on [0,1][0,1]. We obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∫tt+hg′(ξt(s))(s−t)fα0,λ0(t+h−s)\displaystyle\Big|\int\_{t}^{t+h}g^{\prime}(\xi\_{t}(s))(s-t)\,f^{\alpha\_{0},\lambda\_{0}}(t+h-s) | ϱα0,λ0(t+h−s)ds|\displaystyle\varrho^{\alpha\_{0},\lambda\_{0}}(t+h-s)\,\mathrm{d}s\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C′​h​∫tt+hfα0,λ0​(t+h−s)​ϱα0,λ0​(t+h−s)​ds\displaystyle\leq C^{\prime}h\int\_{t}^{t+h}f^{\alpha\_{0},\lambda\_{0}}(t+h-s)\varrho^{\alpha\_{0},\lambda\_{0}}(t+h-s)\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C′​h2​ϱα0,λ0​(h)2\displaystyle=\frac{C^{\prime}h}{2}\varrho^{\alpha\_{0},\lambda\_{0}}(h)^{2} |  |

for some constant C′>0C^{\prime}>0. Consequently,

|  |  |  |
| --- | --- | --- |
|  | ∫tt+hg​(s)​Δh​fα0,λ0​(t−s)​Δh​ϱα0,λ0​(t−s)​ds=12​ϱα0,λ0​(h)2​(1+O​(h)).\int\_{t}^{t+h}g(s)\,\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-s)\,\Delta\_{h}\varrho^{\alpha\_{0},\lambda\_{0}}(t-s)\,\mathrm{d}s=\frac{1}{2}\varrho^{\alpha\_{0},\lambda\_{0}}(h)^{2}\,\big(1+O(h)\big). |  |

We now make explicit the behavior of ϱα0,λ0​(h)\varrho^{\alpha\_{0},\lambda\_{0}}(h) as h→0h\to 0.

###### Lemma B.2.

As hh goes to 0, we have

|  |  |  |
| --- | --- | --- |
|  | ϱα0,λ0​(h)=λ0Γ​(α0+1)​hα0+O​(h2​α0).\varrho^{\alpha\_{0},\lambda\_{0}}(h)=\frac{\lambda\_{0}}{\Gamma(\alpha\_{0}+1)}h^{\alpha\_{0}}+O(h^{2\alpha\_{0}}). |  |

###### Proof.

We recall that the Mittag–Leffler density satisfies

|  |  |  |
| --- | --- | --- |
|  | fα0,λ0​(t)=λ0​tα0−1​Eα0,α0​(−λ0​tα0),ϱα0,λ0​(t)=λ0​tα0​Eα0,α0+1​(−λ0​tα0).f^{\alpha\_{0},\lambda\_{0}}(t)=\lambda\_{0}t^{\alpha\_{0}-1}E\_{\alpha\_{0},\alpha\_{0}}(-\lambda\_{0}t^{\alpha\_{0}}),\qquad\varrho^{\alpha\_{0},\lambda\_{0}}(t)=\lambda\_{0}t^{\alpha\_{0}}E\_{\alpha\_{0},\alpha\_{0}+1}(-\lambda\_{0}t^{\alpha\_{0}}). |  |

Using the series expansion of the Mittag–Leffler function

|  |  |  |
| --- | --- | --- |
|  | Eα0,β​(x)=∑n=0∞xnΓ​(α0​n+β),E\_{\alpha\_{0},\beta}(x)=\sum\_{n=0}^{\infty}\frac{x^{n}}{\Gamma(\alpha\_{0}n+\beta)}, |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | ϱα0,λ0​(t)=λ0​tα0​∑n=0∞(−λ0​tα0)nΓ​(α0​n+α0+1)=∑n=1∞(−λ0​tα0)nΓ​(α0​n+1)=1−Eα0,1​(−λ0​tα0).\varrho^{\alpha\_{0},\lambda\_{0}}(t)=\lambda\_{0}t^{\alpha\_{0}}\sum\_{n=0}^{\infty}\frac{(-\lambda\_{0}t^{\alpha\_{0}})^{n}}{\Gamma(\alpha\_{0}n+\alpha\_{0}+1)}=\sum\_{n=1}^{\infty}\frac{(-\lambda\_{0}t^{\alpha\_{0}})^{n}}{\Gamma(\alpha\_{0}n+1)}=1-E\_{\alpha\_{0},1}(-\lambda\_{0}t^{\alpha\_{0}}). |  |

From the power series expansion of Eα0,1E\_{\alpha\_{0},1} around 0,

|  |  |  |
| --- | --- | --- |
|  | Eα0,1​(−λ0​hα0)=1−λ0Γ​(α0+1)​hα0+λ02Γ​(2​α0+1)​h2​α0+O​(h3​α0),E\_{\alpha\_{0},1}(-\lambda\_{0}h^{\alpha\_{0}})=1-\frac{\lambda\_{0}}{\Gamma(\alpha\_{0}+1)}h^{\alpha\_{0}}+\frac{\lambda\_{0}^{2}}{\Gamma(2\alpha\_{0}+1)}h^{2\alpha\_{0}}+O(h^{3\alpha\_{0}}), |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | ϱα0,λ0​(h)=λ0Γ​(α0+1)​hα0+O​(h2​α0),h→0.\varrho^{\alpha\_{0},\lambda\_{0}}(h)=\frac{\lambda\_{0}}{\Gamma(\alpha\_{0}+1)}h^{\alpha\_{0}}+O(h^{2\alpha\_{0}}),\qquad h\to 0. |  |

∎

We are interested now in the second term of ([3](https://arxiv.org/html/2601.23172v2#A2.E3 "In B.2 Proof of Proposition 3.2 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")). Let

|  |  |  |
| --- | --- | --- |
|  | H​(t):=Eα0,1​(−λ0​tα0).H(t):=E\_{\alpha\_{0},1}(-\lambda\_{0}t^{\alpha\_{0}}). |  |

Then H∈C1​(ℝ+)H\in C^{1}(\mathbb{R}\_{+}), HH is continuous on (0,∞)(0,\infty) and decreasing, and

|  |  |  |
| --- | --- | --- |
|  | fα0,λ0​(t)=−H′​(t),ϱα0,λ0​(t)=1−H​(t).f^{\alpha\_{0},\lambda\_{0}}(t)=-H^{\prime}(t),\qquad\varrho^{\alpha\_{0},\lambda\_{0}}(t)=1-H(t). |  |

Consider

|  |  |  |
| --- | --- | --- |
|  | I​(t,h):=∫0tg​(t−s)​Δh​fα0,λ0​(s)​Δh​ϱα0,λ0​(s)​ds=∫0tg​(t−s)​(Δh​H′)​(s)​(Δh​H)​(s)​ds,I(t,h):=\int\_{0}^{t}g(t-s)\,\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(s)\,\Delta\_{h}\varrho^{\alpha\_{0},\lambda\_{0}}(s)\,\mathrm{d}s=\int\_{0}^{t}g(t-s)\,(\Delta\_{h}H^{\prime})(s)\,(\Delta\_{h}H)(s)\,\mathrm{d}s, |  |

Integrating by parts, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(t,h)\displaystyle I(t,h) | =[g​(t−s)​(Δh​H​(s))22]s=0s=t−12​∫0tg′​(t−s)​(Δh​H​(s))2​ds\displaystyle=\left[g(t-s)\,\frac{(\Delta\_{h}H(s))^{2}}{2}\right]\_{s=0}^{s=t}-\frac{1}{2}\int\_{0}^{t}g^{\prime}(t-s)\,(\Delta\_{h}H(s))^{2}\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−12​g​(t)​(Δh​H​(0))2−12​∫0tϱα0,λ0​(t−s)​(Δh​H​(s))2​ds,\displaystyle=-\frac{1}{2}g(t)\,(\Delta\_{h}H(0))^{2}-\frac{1}{2}\int\_{0}^{t}\varrho^{\alpha\_{0},\lambda\_{0}}(t-s)\,(\Delta\_{h}H(s))^{2}\,\mathrm{d}s, |  |

where we used g​(0)=0g(0)=0 and g′=ϱα0,λ0g^{\prime}=\varrho^{\alpha\_{0},\lambda\_{0}}. Since (Δh​H​(0))2=(Δh​ϱα0,λ0​(0))2=ϱα0,λ0​(h)2(\Delta\_{h}H(0))^{2}=(\Delta\_{h}\varrho^{\alpha\_{0},\lambda\_{0}}(0))^{2}=\varrho^{\alpha\_{0},\lambda\_{0}}(h)^{2}, the first term equals −12​g​(t)​ϱα0,λ0​(h)2-\tfrac{1}{2}g(t)\varrho^{\alpha\_{0},\lambda\_{0}}(h)^{2}. Moreover, for all δ>0\delta>0, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tϱα0,λ0​(t−s)​(Δh​H​(s))2​ds\displaystyle\int\_{0}^{t}\varrho^{\alpha\_{0},\lambda\_{0}}(t-s)\,(\Delta\_{h}H(s))^{2}\,\mathrm{d}s | ≤ϱα0,λ0​(t)​∫0t(Δh​H​(s))2​ds\displaystyle\leq\varrho^{\alpha\_{0},\lambda\_{0}}(t)\int\_{0}^{t}(\Delta\_{h}H(s))^{2}\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϱα0,λ0​(t)​{∫0δ(Δh​H​(s))2​ds+∫δt(Δh​H​(s))2​ds}.\displaystyle\leq\varrho^{\alpha\_{0},\lambda\_{0}}(t)\left\{\int\_{0}^{\delta}(\Delta\_{h}H(s))^{2}\,\mathrm{d}s+\int\_{\delta}^{t}(\Delta\_{h}H(s))^{2}\,\mathrm{d}s\right\}. |  |

Using that HH is bounded and for u,h>0u,h>0

|  |  |  |
| --- | --- | --- |
|  | (Δh​H​(s))2=(∫ss+hH′​(v)​𝑑v)2=(∫ss+hfα0,λ0​(v)​𝑑v)2≤h2​(fα0,λ0​(s))2.(\Delta\_{h}H(s))^{2}=\Big(\int\_{s}^{s+h}H^{\prime}(v)dv\Big)^{2}=\Big(\int\_{s}^{s+h}f^{\alpha\_{0},\lambda\_{0}}(v)dv\Big)^{2}\leq h^{2}(f^{\alpha\_{0},\lambda\_{0}}(s))^{2}. |  |

Moreoever, since α0<1/2\alpha\_{0}<1/2, Eα0,α0​(−s)≤1E\_{\alpha\_{0},\alpha\_{0}}(-s)\leq 1 for any positive ss, and we have that

|  |  |  |
| --- | --- | --- |
|  | (fα0,λ0​(s))2≤λ02​s2​α0−2.(f^{\alpha\_{0},\lambda\_{0}}(s))^{2}\leq\lambda\_{0}^{2}s^{2\alpha\_{0}-2}. |  |

Therefore, we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tϱα0,λ0​(t−u)​(Δh​H​(u))2​du\displaystyle\int\_{0}^{t}\varrho^{\alpha\_{0},\lambda\_{0}}(t-u)\,(\Delta\_{h}H(u))^{2}\,\mathrm{d}u | ≤ϱα0,λ0​(t)​{C​δ+h2​∫δt(fα0,λ0​(u))2​du}\displaystyle\leq\varrho^{\alpha\_{0},\lambda\_{0}}(t)\left\{C\,\delta+h^{2}\int\_{\delta}^{t}(f^{\alpha\_{0},\lambda\_{0}}(u))^{2}\,\mathrm{d}u\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϱα0,λ0​(t)​{C​δ+h2​∫δ∞(fα0,λ0​(u))2​du}\displaystyle\leq\varrho^{\alpha\_{0},\lambda\_{0}}(t)\left\{C\,\delta+h^{2}\int\_{\delta}^{\infty}(f^{\alpha\_{0},\lambda\_{0}}(u))^{2}\,\mathrm{d}u\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϱα0,λ0​(t)​{C​δ+h2​∫δ∞λ02​u2​α0−2​du}\displaystyle\leq\varrho^{\alpha\_{0},\lambda\_{0}}(t)\left\{C\,\delta+h^{2}\int\_{\delta}^{\infty}\lambda\_{0}^{2}u^{2\alpha\_{0}-2}\,\mathrm{d}u\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ϱα0,λ0​(t)​{C​δ+h2​λ02​δ2​α0−11−2​α0},\displaystyle=\varrho^{\alpha\_{0},\lambda\_{0}}(t)\left\{C\,\delta+h^{2}\,\lambda\_{0}^{2}\,\frac{\delta^{2\alpha\_{0}-1}}{1-2\alpha\_{0}}\right\}, |  |

which is finite since α0<1/2\alpha\_{0}<1/2. Choosing δ=h1/(1−α0)\delta=h^{1/(1-\alpha\_{0})} balances the two terms, giving

|  |  |  |
| --- | --- | --- |
|  | ∫0tϱα0,λ0​(t−u)​(Δh​H​(u))2​du≤C′​ϱα0,λ0​(t)​h1/(1−α0).\int\_{0}^{t}\varrho^{\alpha\_{0},\lambda\_{0}}(t-u)\,(\Delta\_{h}H(u))^{2}\,\mathrm{d}u\leq C^{\prime}\varrho^{\alpha\_{0},\lambda\_{0}}(t)\,h^{1/(1-\alpha\_{0})}. |  |

Using α0​(1−α0)≤1/4\alpha\_{0}(1-\alpha\_{0})\leq 1/4 we have 11−α0≥4​α0\tfrac{1}{1-\alpha\_{0}}\geq 4\alpha\_{0}, hence for h∈(0,1]h\in(0,1],

|  |  |  |
| --- | --- | --- |
|  | h1/(1−α0)≤h4​α0.h^{1/(1-\alpha\_{0})}\leq h^{4\alpha\_{0}}. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | I​(t,h)=12​g​(t)​ϱα0,λ0​(h)2+O​(ϱα0,λ0​(t)​h4​α0).I(t,h)=\frac{1}{2}g(t)\varrho^{\alpha\_{0},\lambda\_{0}}(h)^{2}+O\big(\varrho^{\alpha\_{0},\lambda\_{0}}(t)\,h^{4\alpha\_{0}}\big). |  |

Using Lemma ([B.2](https://arxiv.org/html/2601.23172v2#A2.Ex123 "B.2 Proof of Proposition 3.2 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")), we obtain

|  |  |  |
| --- | --- | --- |
|  | I​(t,h)=g​(t)​λ022​Γ​(α0+1)2​h2​α0+O​(h4​α0∧1).I(t,h)=\frac{g(t)\,\lambda\_{0}^{2}}{2\,\Gamma(\alpha\_{0}+1)^{2}}\,h^{2\alpha\_{0}}+O\big(h^{4\alpha\_{0}\wedge 1}\big). |  |

Hence, going back to ([3](https://arxiv.org/html/2601.23172v2#A2.E3 "In B.2 Proof of Proposition 3.2 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")), we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,h)\displaystyle V(t,h) | =(Δh​g​(t))2+2​I​(t,h)+2​∫tt+hg​(u)​Δh​fα0,λ0​(t−u)​Δh​ϱα0,λ0​(t−u)​du\displaystyle=\big(\Delta\_{h}g(t)\big)^{2}+2I(t,h)+2\int\_{t}^{t+h}g(u)\,\Delta\_{h}f^{\alpha\_{0},\lambda\_{0}}(t-u)\,\Delta\_{h}\varrho^{\alpha\_{0},\lambda\_{0}}(t-u)\,\mathrm{d}u |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =O​(h2)+2⋅g​(t)​λ022​Γ​(α0+1)2​h2​α0+2⋅12​ϱα0,λ0​(h)2​(1+O​(h))+O​(h4​α0)\displaystyle=O(h^{2})+2\cdot\frac{g(t)\,\lambda\_{0}^{2}}{2\,\Gamma(\alpha\_{0}+1)^{2}}\,h^{2\alpha\_{0}}+2\cdot\frac{1}{2}\varrho^{\alpha\_{0},\lambda\_{0}}(h)^{2}\,\big(1+O(h)\big)+O\big(h^{4\alpha\_{0}}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​λ02Γ​(α0+1)2​(1+g​(t))​h2​α0+O​(h4​α0∧1)+O​(h2).\displaystyle=\frac{2\lambda\_{0}^{2}}{\Gamma(\alpha\_{0}+1)^{2}}\,(1+g(t))\,h^{2\alpha\_{0}}+O\big(h^{4\alpha\_{0}\wedge 1}\big)+O(h^{2}). |  |

Since 2​α0<12\alpha\_{0}<1, the remainder O​(h2)O(h^{2}) is negligible with respect to h2​α0h^{2\alpha\_{0}} as hh goes to 0.
  
In summary, for α0∈(0,12)\alpha\_{0}\in(0,\tfrac{1}{2}) the following holds uniformly for t,h>0t,h>0, as hh tends to 0,

|  |  |  |
| --- | --- | --- |
|  | V​(t,h)=𝔼​[(Xt+h−Xt)2]=2​λ02Γ​(α0+1)2​(1+g​(t))​h2​α0+O​(h4​α0∧1).V(t,h)=\mathbb{E}\big[(X\_{t+h}-X\_{t})^{2}\big]=\frac{2\lambda\_{0}^{2}}{\Gamma(\alpha\_{0}+1)^{2}}\,(1+g(t))\,h^{2\alpha\_{0}}+O\big(h^{4\alpha\_{0}\wedge 1}\big). |  |

We conclude that F+F^{+} and F−F^{-} are exactly 2​α02\alpha\_{0}–Hölder continuous in L2L^{2}.
∎

### B.3 Proof of Proposition [3.3](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")

From Theorem [3.1](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") we can see that

|  |  |  |
| --- | --- | --- |
|  | Ft=Ft++Ft−=2​∫0ts​fα0,λ0​(t−s)​𝑑s+1μ0​λ0​∫0tfα0,λ0​(t−s)​ZsF​𝑑sF\_{t}=F^{+}\_{t}+F^{-}\_{t}=2\int\_{0}^{t}s\,f^{\alpha\_{0},\lambda\_{0}}(t-s)\,ds+\frac{1}{\sqrt{\mu\_{0}\,\lambda\_{0}}}\int\_{0}^{t}f^{\alpha\_{0},\lambda\_{0}}(t-s)\,Z^{F}\_{s}ds |  |

where ZF=Z++Z−Z^{F}=Z^{+}+Z^{-}. Notice that ZFZ^{F} is a continuous martingale with quadratic variation FF.
On the other hand, the process VV satisfies

|  |  |  |
| --- | --- | --- |
|  | Vt=Ft+−Ft−=1μ0​λ0​∫0tfα0,λ0​(t−s)​ZsV​𝑑sV\_{t}=F\_{t}^{+}-F\_{t}^{-}=\frac{1}{\sqrt{\mu\_{0}\,\lambda\_{0}}}\int\_{0}^{t}f^{\alpha\_{0},\lambda\_{0}}(t-s)\,Z^{V}\_{s}ds |  |

where ZV=Z+−Z−Z^{V}=Z^{+}-Z^{-}. Note also that ZVZ^{V} is a continuous martingale with quadratic variation FF.
  
We can compute the quadratic covariance of the two resulting martingales

|  |  |  |
| --- | --- | --- |
|  | <ZV,ZF>=<Z+−Z−,Z++Z−>=F+−F−=V.\displaystyle<\!Z^{V},Z^{F}\!>\,=\,<\!Z^{+}-Z^{-},Z^{+}+Z^{-}\!>\,=F^{+}-F^{-}=V. |  |

### B.4 Proof of Theorem [3.4](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")

The proof relies on replicating the findings of [[24](https://arxiv.org/html/2601.23172v2#bib.bib219 "The microstructural foundations of leverage effect and rough volatility")] with the stochastic time-varying baseline 𝝁T{\boldsymbol{\mu}}^{T}. We start by providing multiple elements needed for the proof.
  
First, note that we have

|  |  |  |
| --- | --- | --- |
|  | ∫0t𝝀sT​𝑑s=∫0t𝝁sT​𝑑s+∫0tψT​(t−s)⋅∫0s𝝁uT​𝑑u​𝑑s+∫0tψT​(t−s)⋅𝐌sT​𝑑s.\displaystyle\int\_{0}^{t}{\boldsymbol{\lambda}}\_{s}^{T}\,ds=\int\_{0}^{t}{\boldsymbol{\mu}}\_{s}^{T}\,ds+\int\_{0}^{t}\psi^{T}(t-s)\cdot\int\_{0}^{s}{\boldsymbol{\mu}}\_{u}^{T}\,du\,ds+\int\_{0}^{t}\psi^{T}(t-s)\cdot\mathbf{M}^{T}\_{s}\,ds. |  |

Now, 𝝁T=ϕT∗d​𝐅T{\boldsymbol{\mu}}^{T}=\phi^{T}\*d\mathbf{F}^{T}
and since 𝐅0T=𝟎\mathbf{F}^{T}\_{0}=\mathbf{0} we have

|  |  |  |
| --- | --- | --- |
|  | ∫0t𝝁sT​𝑑s=ϕT∗𝐅tT.\int\_{0}^{t}{\boldsymbol{\mu}}\_{s}^{T}\,ds=\phi^{T}\*\mathbf{F}^{T}\_{t}. |  |

Using also the identity ψT∗ϕT=ψT−ϕT\psi^{T}\*\phi^{T}=\psi^{T}-\phi^{T},
we obtain

|  |  |  |
| --- | --- | --- |
|  | ∫0t𝝀sT​𝑑s=∫0tψT​(t−s)⋅𝐅sT​𝑑s+∫0tψT​(t−s)⋅𝐌sT​𝑑s.\displaystyle\int\_{0}^{t}{\boldsymbol{\lambda}}\_{s}^{T}\,ds=\int\_{0}^{t}\psi^{T}(t-s)\cdot\mathbf{F}^{T}\_{s}\,ds+\int\_{0}^{t}\psi^{T}(t-s)\cdot\mathbf{M}^{T}\_{s}\,ds. |  |

In this setting, it is more suitable to work with the two-dimensional rescaled processes

|  |  |  |
| --- | --- | --- |
|  | 𝐍¯tT=(1−a0T)​(1−a1T)T​νT​𝐍t​TT,𝚲¯tT=(1−a0T)​(1−a1T)T​νT​𝚲t​TT,𝐌¯tT=((1−a0T)​(1−a1T)T​νT)1/2​𝐌t​TT.\begin{split}&\overline{\mathbf{N}}\_{t}^{T}=\frac{(1-a^{T}\_{0})(1-a^{T}\_{1})}{T\nu^{T}}\mathbf{N}\_{tT}^{T},\\ &\overline{{\boldsymbol{\Lambda}}}\_{t}^{T}=\frac{(1-a^{T}\_{0})(1-a^{T}\_{1})}{T\nu^{T}}{\boldsymbol{\Lambda}}\_{tT}^{T},\\ &\overline{\mathbf{M}}\_{t}^{T}=\Big(\frac{(1-a^{T}\_{0})(1-a^{T}\_{1})}{T\nu^{T}}\Big)^{1/2}\mathbf{M}\_{tT}^{T}.\end{split} |  |

The scaled unsigned reaction flow is then given by

|  |  |  |
| --- | --- | --- |
|  | v1t⋅𝐍¯T=N¯+,T+N¯−,T,\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{N}}^{T}=\overline{N}^{+,T}+\overline{N}^{-,T}, |  |

and the scaled signed reaction flow by

|  |  |  |
| --- | --- | --- |
|  | v2t⋅𝐍¯T=N¯+,T−N¯−,T.\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\overline{\mathbf{N}}^{T}=\overline{N}^{+,T}-\overline{N}^{-,T}. |  |

We can then write

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚲¯tT\displaystyle\overline{{\boldsymbol{\Lambda}}}\_{t}^{T} | =(1−a0T)​(1−a1T)T​νT​∫0t​T𝝀sT​𝑑s\displaystyle=\frac{(1-a^{T}\_{0})(1-a^{T}\_{1})}{T\nu^{T}}\int\_{0}^{tT}{\boldsymbol{\lambda}}\_{s}^{T}\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0tT​(1−a1T)​ψT​(T​(t−s))⋅𝐅¯sT​𝑑s+1−a0TT​νT​∫0tT​(1−a1T)​ψT​(T​(t−s))⋅𝐌s​TT​𝑑s.\displaystyle=\int\_{0}^{t}T(1-a\_{1}^{T})\psi^{T}(T(t-s))\cdot\overline{\mathbf{F}}^{T}\_{s}\,ds+\frac{1-a^{T}\_{0}}{T\nu^{T}}\int\_{0}^{t}T(1-a\_{1}^{T})\psi^{T}(T(t-s))\cdot\mathbf{M}^{T}\_{sT}\,ds. |  |

Note that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝚲¯tT]=∫0tT​(1−a1T)​ψT​(T​(t−s))⋅𝔼​[𝐅¯sT]​𝑑s,\mathbb{E}[\overline{{\boldsymbol{\Lambda}}}\_{t}^{T}]=\int\_{0}^{t}T(1-a\_{1}^{T})\psi^{T}(T(t-s))\cdot\mathbb{E}[\overline{\mathbf{F}}^{T}\_{s}]\,ds, |  |

and from Section [B.1](https://arxiv.org/html/2601.23172v2#A2.SS1 "B.1 Proof of Theorem 3.1 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), we know that 𝔼​[𝐅¯s±,T]≤1\mathbb{E}[\overline{\mathbf{F}}^{\pm,T}\_{s}]\leq 1, then

|  |  |  |
| --- | --- | --- |
|  | v1t⋅𝔼​[𝚲¯tT]≤T​(1−a1T)​v1t⋅(∫0tψT​(T​(t−s))​𝑑s)⋅v1≤(1−a1T)​ϱ​(∫0∞ψT​(s)​𝑑s)<1.\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\mathbb{E}[\overline{{\boldsymbol{\Lambda}}}\_{t}^{T}]\leq T(1-a\_{1}^{T})\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\Big(\int\_{0}^{t}\psi^{T}(T(t-s))ds\Big)\cdot v\_{1}\leq(1-a\_{1}^{T})\varrho\left(\int\_{0}^{\infty}\psi^{T}(s)ds\right)<1. |  |

Therefore, using the Burkholder-Davis-Gundy inequality, we get that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt≤1‖𝐌¯tT‖22]≤C\mathbb{E}\Big[\sup\_{t\leq 1}{\big|\kern-1.07639pt\big|\overline{\mathbf{M}}\_{t}^{T}\big|\kern-1.07639pt\big|}\_{2}^{2}\Big]\leq C |  |

for some constant C>0C>0.

For i=1,2i=1,2, viv\_{i} is the eigenvector associated with the eigenvalue kik\_{i} so we have

|  |  |  |
| --- | --- | --- |
|  | ϕT⋅vi=kiT​vi.\phi^{T}\cdot v\_{i}=k\_{i}^{T}v\_{i}. |  |

By induction,

|  |  |  |
| --- | --- | --- |
|  | viT⋅(ϕT)∗n=(kiT)∗n​viT,v\_{i}^{T}\cdot(\phi^{T})^{\*n}=(k\_{i}^{T})^{\*n}\,v\_{i}^{T}, |  |

and we define scalar kernels

|  |  |  |
| --- | --- | --- |
|  | ψiT​(x)=∑n≥1(a1T)n​(kiT)∗n​(x),ρiT​(x)=T​(1−a1T)​ψiT​(T​x),ϱiT​(t)=∫0tρiT​(s)​𝑑s.\psi\_{i}^{T}(x)=\sum\_{n\geq 1}(a\_{1}^{T})^{n}(k\_{i}^{T})^{\*n}(x),\quad\rho\_{i}^{T}(x)=T(1-a\_{1}^{T})\psi\_{i}^{T}(Tx),\quad\varrho\_{i}^{T}(t)=\int\_{0}^{t}\rho\_{i}^{T}(s)\,ds. |  |

Consequently, we have vit⋅ψT=ψiT​vit\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\psi^{T}=\psi\_{i}^{T}\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}} and

|  |  |  |
| --- | --- | --- |
|  | vit⋅𝚲¯tT=∫0tρiT​(t−s)​vit⋅𝐅¯sT​𝑑s+cT​∫0tρiT​(t−s)​vit⋅𝐌¯sT​𝑑s\displaystyle\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{{\boldsymbol{\Lambda}}}\_{t}^{T}=\int\_{0}^{t}\rho\_{i}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{\mathbf{F}}^{T}\_{s}\,ds+c^{T}\int\_{0}^{t}\rho\_{i}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{\mathbf{M}}^{T}\_{s}\,ds |  |

where

|  |  |  |
| --- | --- | --- |
|  | cT=(1−a0T)/(T​νT​(1−a1T))→1λ1​μ1.c^{T}=\sqrt{(1-a\_{0}^{T})/(T\nu^{T}(1-a\_{1}^{T}))}\to\sqrt{\frac{1}{\lambda\_{1}\mu\_{1}}}. |  |

We are interested in studying the convergence of this process for i∈{1,2}i\in\{1,2\}.

Convergence of vit⋅𝐍¯tT−vit⋅𝚲¯tT\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{\mathbf{N}}^{T}\_{t}-\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{{\boldsymbol{\Lambda}}}^{T}\_{t}. We have

|  |  |  |
| --- | --- | --- |
|  | vit⋅𝐍¯tT−vit⋅𝚲¯tT=((1−a0T)​(1−a1T)T​νT)1/2​vit⋅𝐌¯tT\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{\mathbf{N}}^{T}\_{t}-\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{{\boldsymbol{\Lambda}}}^{T}\_{t}=\Big(\frac{(1-a^{T}\_{0})(1-a^{T}\_{1})}{T\nu^{T}}\Big)^{1/2}\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{\mathbf{M}}^{T}\_{t} |  |

Using Doob’s inequality, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[supt≤1|vit⋅𝐍¯tT−vit⋅𝚲¯tT|2]\displaystyle\mathbb{E}\Big[\sup\_{t\leq 1}\Big|\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{\mathbf{N}}^{T}\_{t}-\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{{\boldsymbol{\Lambda}}}^{T}\_{t}\Big|^{2}\Big] | ≤4​((1−a0T)​(1−a1T)T​νT)​𝔼​[|vit⋅𝐌¯TT|2]\displaystyle\leq 4\Big(\frac{(1-a^{T}\_{0})(1-a^{T}\_{1})}{T\nu^{T}}\Big)\mathbb{E}[|\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{\mathbf{M}}\_{T}^{T}|^{2}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤4​((1−a0T)​(1−a1T)T​νT)​‖vi‖2​𝔼​[‖𝐌¯TT‖22]\displaystyle\leq 4\Big(\frac{(1-a^{T}\_{0})(1-a^{T}\_{1})}{T\nu^{T}}\Big){\big|\kern-1.07639pt\big|v\_{i}\big|\kern-1.07639pt\big|}^{2}\mathbb{E}[{\big|\kern-1.07639pt\big|\overline{\mathbf{M}}\_{T}^{T}\big|\kern-1.07639pt\big|}\_{2}^{2}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C′​((1−a0T)​(1−a1T)T​νT).\displaystyle\leq C^{{}^{\prime}}\Big(\frac{(1-a^{T}\_{0})(1-a^{T}\_{1})}{T\nu^{T}}\Big). |  |

Since (1−a0T)​(1−a1T)​(T​νT)−1(1-a^{T}\_{0})(1-a^{T}\_{1})(T\nu^{T})^{-1} is of the order of T−2​α1T^{-2\alpha\_{1}}, we obtain the convergence to zero in L2L^{2} and in probability of vit⋅𝐍¯tT−vit⋅𝚲¯tT\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{\mathbf{N}}^{T}\_{t}-\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{{\boldsymbol{\Lambda}}}^{T}\_{t}.

Convergence of v2t⋅𝐍¯tT\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\overline{\mathbf{N}}^{T}\_{t}. We know from [[24](https://arxiv.org/html/2601.23172v2#bib.bib219 "The microstructural foundations of leverage effect and rough volatility")] that ϱ2T\varrho\_{2}^{T} converges uniformly to zero and we write

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|∫0tρ2T​(t−s)​v2t⋅𝐅¯sT​𝑑s|]≤‖v2‖​supt≤1𝔼​[‖𝐅¯tT‖]​ϱ2​(t).\displaystyle\mathbb{E}\Big[\Big|\int\_{0}^{t}\rho\_{2}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\overline{\mathbf{F}}^{T}\_{s}\,ds\Big|\Big]\leq{\big|\kern-1.07639pt\big|v\_{2}\big|\kern-1.07639pt\big|}\sup\_{t\leq 1}\mathbb{E}[{\big|\kern-1.07639pt\big|\overline{\mathbf{F}}\_{t}^{T}\big|\kern-1.07639pt\big|}]\varrho\_{2}(t). |  |

Using the fact that 𝔼​[‖𝐅¯tT‖]\mathbb{E}[{\big|\kern-1.07639pt\big|\overline{\mathbf{F}}\_{t}^{T}\big|\kern-1.07639pt\big|}] is bounded, which has been proven in Section [B.1](https://arxiv.org/html/2601.23172v2#A2.SS1 "B.1 Proof of Theorem 3.1 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), we conclude the first integral of v2t⋅𝐍¯tT\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\overline{\mathbf{N}}^{T}\_{t} converges to zero in L1L^{1}. For the second integral, we write using an integration by parts

|  |  |  |
| --- | --- | --- |
|  | cT​∫0tρ2T​(t−s)​v2t⋅𝐌¯sT​𝑑s=cT​∫0tϱ2T​(t−s)​(v2t⋅𝐌¯sT).\displaystyle c^{T}\int\_{0}^{t}\rho\_{2}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\overline{\mathbf{M}}^{T}\_{s}\,ds=c^{T}\int\_{0}^{t}\varrho\_{2}^{T}(t-s)(\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\overline{\mathbf{M}}^{T}\_{s}). |  |

Thus, there exists a constant C′C^{{}^{\prime}} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(cT​∫0tρ2T​(t−s)​v2t⋅𝐌¯sT​𝑑s)2]≤C′​∫0t(ϱ2T​(s))2​𝑑s\displaystyle\mathbb{E}\Big[\Big(c^{T}\int\_{0}^{t}\rho\_{2}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\overline{\mathbf{M}}^{T}\_{s}\,ds\Big)^{2}\Big]\leq C^{{}^{\prime}}\int\_{0}^{t}(\varrho\_{2}^{T}(s))^{2}ds |  |

and therefore the second integral converges to 0 in L2L^{2}. Therefore we obtain that v2t⋅𝚲¯tT\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\overline{{\boldsymbol{\Lambda}}}\_{t}^{T} goes to zero in L1L^{1}. Consequently, v2t⋅𝐍T¯\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\overline{\mathbf{N}^{T}} converges to 0 in probability and in L1L^{1}.

Convergence of v1t⋅𝐍¯tT\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{N}}^{T}\_{t}. We write

|  |  |  |
| --- | --- | --- |
|  | v1t⋅𝚲¯tT=∫0tρ1T​(t−s)​v1t⋅𝐅¯sT​𝑑s+cT​∫0tρ1T​(t−s)​v1t⋅𝐌¯sT​𝑑s\displaystyle\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{{\boldsymbol{\Lambda}}}\_{t}^{T}=\int\_{0}^{t}\rho\_{1}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{F}}^{T}\_{s}\,ds+c^{T}\int\_{0}^{t}\rho\_{1}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{M}}^{T}\_{s}\,ds |  |

Using the same arguments and methodology as in Section [B.1](https://arxiv.org/html/2601.23172v2#A2.SS1 "B.1 Proof of Theorem 3.1 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), we get that v1t⋅𝚲¯T\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{{\boldsymbol{\Lambda}}}^{T} is C-tight and we conclude that (v1t⋅𝐍¯T,v1t⋅𝚲¯T,v1t⋅𝐌¯T)(\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{N}}^{T},\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{{\boldsymbol{\Lambda}}}^{T},\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{M}}^{T}) is C-tight. Furthermore, if (X,X,Z)(X,X,Z) is a limit point of (v1t⋅𝐍¯T,v1t⋅𝚲¯T,v1t⋅𝐌¯T)(\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{N}}^{T},\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{{\boldsymbol{\Lambda}}}^{T},\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{M}}^{T}), then ZZ is a continuous martingale with [Z,Z]=X[Z,Z]=X.

Moreover, we know from [[40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes")] that the sequence of measures with density ρ1T​(x)\rho\_{1}^{T}(x) converges weakly towards the measure with density λ1​xα1−1​Eα1,α1​(−λ1​x1α)\lambda\_{1}x^{\alpha\_{1}-1}E\_{\alpha\_{1},\alpha\_{1}}\left(-\lambda\_{1}x^{\alpha}\_{1}\right). In particular, over [0,1][0,1],

|  |  |  |
| --- | --- | --- |
|  | ϱ1T​(t)=∫0tρ1T​(x)​𝑑x\varrho\_{1}^{T}(t)=\int\_{0}^{t}\rho\_{1}^{T}(x)dx |  |

converges uniformly towards

|  |  |  |
| --- | --- | --- |
|  | ϱα1,λ1​(t)=∫0tfα1,λ1​(x)​𝑑x.\varrho^{\alpha\_{1},\lambda\_{1}}(t)=\int\_{0}^{t}f^{\alpha\_{1},\lambda\_{1}}(x)dx. |  |

Therefore, using the same approach as in [[40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes")] yields

|  |  |  |
| --- | --- | --- |
|  | ∫0tρ1T​(t−s)​v1t⋅𝐅¯sT​𝑑s→∫0tfα1,λ1​(t−s)​Fs​𝑑scT​∫0tρiT​(t−s)​vit⋅𝐌¯sT​𝑑s→1λ1​μ1​∫0tfα1,λ1​(t−s)​Zs​𝑑s\begin{split}&\int\_{0}^{t}\rho\_{1}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{F}}^{T}\_{s}\,ds\to\int\_{0}^{t}f^{\alpha\_{1},\lambda\_{1}}(t-s)F\_{s}\,ds\\ &c^{T}\int\_{0}^{t}\rho\_{i}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{i}}\cdot\overline{\mathbf{M}}^{T}\_{s}\,ds\to\sqrt{\frac{1}{\lambda\_{1}\mu\_{1}}}\int\_{0}^{t}f^{\alpha\_{1},\lambda\_{1}}(t-s)Z\_{s}\,ds\end{split} |  |

where FF is the scaling limit of v1t⋅𝐅¯T\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{F}}^{T} from Proposition [3.3](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.").

Convergence of (N¯+,T,N¯−,T,Λ¯+,T,Λ¯−,T,M¯+,T,M¯−,T)(\overline{N}^{+,T},\overline{N}^{-,T},\overline{\Lambda}^{+,T},\overline{\Lambda}^{-,T},\overline{M}^{+,T},\overline{M}^{-,T}). We use the fact that the sum process (v1t.𝐍¯T,v1t.𝚲¯T,v1t.𝐌¯T)(\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}.\overline{\mathbf{N}}^{T},\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}.\overline{{\boldsymbol{\Lambda}}}^{T},\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}.\overline{\mathbf{M}}^{T}) is C-tight, which implies the C-tightness of the process
  
(N¯+,T,N¯−,T,Λ¯+,T,Λ¯−,T,M¯+,T,M¯−,T)(\overline{N}^{+,T},\overline{N}^{-,T},\overline{\Lambda}^{+,T},\overline{\Lambda}^{-,T},\overline{M}^{+,T},\overline{M}^{-,T}). Furthermore, using the same arguments as in Section [B](https://arxiv.org/html/2601.23172v2#A2 "Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), the previous result, and the fact that

|  |  |  |
| --- | --- | --- |
|  | N¯+,T=12(v1t.𝐍¯T+v2t.𝐍¯T)andN¯−,T=12(v1t.𝐍¯T−v2t.𝐍¯T),\overline{N}^{+,T}=\frac{1}{2}(\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}.\overline{\mathbf{N}}^{T}+\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}.\overline{\mathbf{N}}^{T})\quad\text{and}\quad\overline{N}^{-,T}=\frac{1}{2}(\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}.\overline{\mathbf{N}}^{T}-\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}.\overline{\mathbf{N}}^{T}), |  |

if (X,X,X,X,Z+,Z−)(X,X,X,X,Z^{+},Z^{-}) is an accumulation point of (N¯+,T,N¯−,T,Λ¯+,T,Λ¯−,T,M¯+,T,M¯−,T)(\overline{N}^{+,T},\overline{N}^{-,T},\overline{\Lambda}^{+,T},\overline{\Lambda}^{-,T},\overline{M}^{+,T},\overline{M}^{-,T}), then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt\displaystyle X\_{t} | =12​∫0tfα1,λ1​(t−s)​Fs​𝑑s+12​λ1​μ1​∫0tfα1,λ1​(t−s)​Zs​𝑑sandZt=Zt++Zt−\displaystyle=\frac{1}{2}\int\_{0}^{t}f^{\alpha\_{1},\lambda\_{1}}(t-s)F\_{s}\,ds+\frac{1}{2\sqrt{\lambda\_{1}\mu\_{1}}}\int\_{0}^{t}f^{\alpha\_{1},\lambda\_{1}}(t-s)Z\_{s}\,ds\qquad\text{and}\qquad Z\_{t}=Z^{+}\_{t}+Z^{-}\_{t} |  |

where Z+Z^{+} and Z−Z^{-} are two continuous martingales with quadratic variation XX and zero quadratic covariation.
Seeing that FF is smoother than ZZ, the regularity of XX is determined by the second integral, which is (H1−ε)(H\_{1}-\varepsilon)-Holder continuous for every ε>0\varepsilon>0 on [0,1][0,1], with H1=α1−1/2H\_{1}=\alpha\_{1}-1/2.

### B.5 Proof of Hölder regularity in Theorem [3.4](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")

From the previous section, we know that:

* •

  XX is Lipschitz continuous,
* •

  ZZ is (1/2−ε)(1/2-\varepsilon)-Hölder continuous for all ε>0\varepsilon>0, since its quadratic variation, which is XX, is continuous,
* •

  FF is (2​α0−ε)(2\alpha\_{0}-\varepsilon)-Hölder continuous for all ε>0\varepsilon>0,
* •

  ZFZ^{F} is (α0−ε)(\alpha\_{0}-\varepsilon)-Hölder continuous for all ε>0\varepsilon>0.

Then for 0<γ<10<\gamma<1, we know from Proposition A.1 in [[40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes")] that

* •

  XX admits a fractional derivative of order γ\gamma and Dγ​XD^{\gamma}X is (1−γ)(1-\gamma)-Hölder regular,
* •

  If γ<2​α0=α1\gamma<2\alpha\_{0}=\alpha\_{1}, then FF admits a fractional derivative of order γ\gamma and Dγ​FD^{\gamma}F is (2​α0−γ−ε)(2\alpha\_{0}-\gamma-\varepsilon)-Hölder regular for all ε>0\varepsilon>0,
* •

  If γ<1/2\gamma<1/2, then ZZ admits a fractional derivative of order γ\gamma and Dγ​ZD^{\gamma}Z is (1/2−γ−ε)(1/2-\gamma-\varepsilon)-Hölder regular for all ε>0\varepsilon>0.

Let 1/2<γ<α11/2<\gamma<\alpha\_{1}. From Proposition 3.1 and Corollary A.2 in [[40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes")], we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt\displaystyle X\_{t} | =12​∫0tfα1,λ1​(t−s)​Fs​𝑑s+12​λ1​μ1​∫0tfα1,λ1​(t−s)​Zs​𝑑s\displaystyle=\frac{1}{2}\int\_{0}^{t}f^{\alpha\_{1},\lambda\_{1}}(t-s)F\_{s}\,ds+\frac{1}{2\sqrt{\lambda\_{1}\mu\_{1}}}\int\_{0}^{t}f^{\alpha\_{1},\lambda\_{1}}(t-s)Z\_{s}\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​∫0tDγ​fα1,λ1​(t−s)​Iγ​Fs​𝑑s+12​λ1​μ1​∫0tDγ​fα1,λ1​(t−s)​Iγ​Zs​𝑑s\displaystyle=\frac{1}{2}\int\_{0}^{t}D^{\gamma}f^{\alpha\_{1},\lambda\_{1}}(t-s)I^{\gamma}F\_{s}\,ds+\frac{1}{2\sqrt{\lambda\_{1}\mu\_{1}}}\int\_{0}^{t}D^{\gamma}f^{\alpha\_{1},\lambda\_{1}}(t-s)I^{\gamma}Z\_{s}\,ds |  |

Furthermore, FF and ZZ are fractionally differentiable and we have

|  |  |  |
| --- | --- | --- |
|  | Iγ​Fs=∫0sD1−γ​Fu​𝑑u and Iγ​Zs=∫0sD1−γ​Zu​𝑑u.I^{\gamma}F\_{s}=\int\_{0}^{s}D^{1-\gamma}F\_{u}du\quad\quad\text{ and }\quad\quad I^{\gamma}Z\_{s}=\int\_{0}^{s}D^{1-\gamma}Z\_{u}du. |  |

We rewrite the expression of XX as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=12​∫0t∫0sDγ​fα1,λ1​(t−s)​D1−γ​Fu​𝑑u​𝑑s+12​λ1​μ1​∫0t∫0sDγ​fα1,λ1​(t−s)​D1−γ​Zu​𝑑u​𝑑sX\_{t}=\frac{1}{2}\int\_{0}^{t}\int\_{0}^{s}D^{\gamma}f^{\alpha\_{1},\lambda\_{1}}(t-s)D^{1-\gamma}F\_{u}duds+\frac{1}{2\sqrt{\lambda\_{1}\mu\_{1}}}\int\_{0}^{t}\int\_{0}^{s}D^{\gamma}f^{\alpha\_{1},\lambda\_{1}}(t-s)D^{1-\gamma}Z\_{u}duds |  | (4) |

We use Fubini’s theorem and we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0t∫0sDγ​fα1,λ1​(t−s)​D1−γ​Zu​𝑑u​𝑑s\displaystyle\int\_{0}^{t}\int\_{0}^{s}D^{\gamma}f^{\alpha\_{1},\lambda\_{1}}(t-s)D^{1-\gamma}Z\_{u}duds | =∫0t∫utDγ​fα1,λ1​(t−s)​D1−γ​Zu​𝑑s​𝑑u\displaystyle=\int\_{0}^{t}\int\_{u}^{t}D^{\gamma}f^{\alpha\_{1},\lambda\_{1}}(t-s)D^{1-\gamma}Z\_{u}dsdu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0t∫utDγ​fα1,λ1​(s−u)​D1−γ​Zu​𝑑s​𝑑u\displaystyle=\int\_{0}^{t}\int\_{u}^{t}D^{\gamma}f^{\alpha\_{1},\lambda\_{1}}(s-u)D^{1-\gamma}Z\_{u}dsdu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0t∫0sDγ​fα1,λ1​(s−u)​D1−γ​Zu​𝑑u​𝑑s.\displaystyle=\int\_{0}^{t}\int\_{0}^{s}D^{\gamma}f^{\alpha\_{1},\lambda\_{1}}(s-u)D^{1-\gamma}Z\_{u}duds. |  |

Applying the same computations to the first integral in ([4](https://arxiv.org/html/2601.23172v2#A2.E4 "In B.5 Proof of Hölder regularity in Theorem 3.4 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")), we get

|  |  |  |
| --- | --- | --- |
|  | Xt=∫0tYs​𝑑sX\_{t}=\int\_{0}^{t}Y\_{s}ds |  |

with

|  |  |  |
| --- | --- | --- |
|  | Ys=12​∫0sDγ​fα1,λ1​(s−u)​D1−γ​Fu​𝑑u+12​λ1​μ1​∫0sDγ​fα1,λ1​(s−u)​D1−γ​Zu​𝑑u.Y\_{s}=\frac{1}{2}\int\_{0}^{s}D^{\gamma}f^{\alpha\_{1},\lambda\_{1}}(s-u)D^{1-\gamma}F\_{u}du+\frac{1}{2\sqrt{\lambda\_{1}\mu\_{1}}}\int\_{0}^{s}D^{\gamma}f^{\alpha\_{1},\lambda\_{1}}(s-u)D^{1-\gamma}Z\_{u}du. |  |

Since 2​α0>1/22\alpha\_{0}>1/2, we know that FF is smoother than ZZ, and thus the regularity of YY is that of its second term. From Propositions 3.1 and A.3 in [[40](https://arxiv.org/html/2601.23172v2#bib.bib389 "Rough fractional diffusions as scaling limits of nearly unstable heavy tailed Hawkes processes")], we have that the second integral has Hölder regularity (α1−γ)(\alpha\_{1}-\gamma) for 1/2<γ<11/2<\gamma<1. Thus, for every ε>0\varepsilon>0, the second integral, and therefore YY, has Hölder regularity (α1−1/2−ε)(\alpha\_{1}-1/2-\varepsilon).

### B.6 Proof of Theorem [3.5](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.3 Scaling limits for the global order flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")

First, note that F¯tT,++F¯t−,T\overline{F}\_{t}^{T,+}+\overline{F}\_{t}^{-,T} scales as T​νT​(1−a0T)−1T\nu^{T}(1-a\_{0}^{T})^{-1}. Seeing that (1−a1T)(1-a^{T}\_{1}) is of the same order as T−α1T^{-\alpha\_{1}}, we conclude that (1−a0T)​(1−a1T)​(T​νT)−1​(Ft​TT,++Ft​T−,T)(1-a\_{0}^{T})(1-a\_{1}^{T})(T\nu^{T})^{-1}(F\_{tT}^{T,+}+F\_{tT}^{-,T}) converges to zero.
  
Moreover, Theorem [3.4](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") ensures that the process

|  |  |  |
| --- | --- | --- |
|  | (1−a0T)​(1−a1T)T​νT​(Nt​T+,T+Nt​T−,T)=𝐍¯+,T+𝐍¯−,T=v1t⋅𝐍¯T\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}(N^{+,T}\_{tT}+N^{-,T}\_{tT})=\overline{\mathbf{N}}^{+,T}+\overline{\mathbf{N}}^{-,T}=\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{N}}^{T} |  |

is C-tight and it converges in distribution in the Skorokhod topology. Therefore, the same applies to U¯T\overline{U}^{T}, and if UU is a limit of v1t⋅𝐍¯T\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{1}}\cdot\overline{\mathbf{N}}^{T}, then it is also a limit of U¯T\overline{U}^{T} and it satisfies Equation ([1](https://arxiv.org/html/2601.23172v2#S3.E1 "In Theorem 3.5. ‣ 3.3 Scaling limits for the global order flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")).

### B.7 Proof of Theorem [3.6](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem6 "Theorem 3.6. ‣ 3.3 Scaling limits for the global order flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")

Notice that on the one hand, (1−a0T)​(T​νT)−1(1-a\_{0}^{T})(T\nu^{T})^{-1} is of the same order as T−2​α0=T−α1T^{-2\alpha\_{0}}=T^{-\alpha\_{1}}. But we also know that (1−a1T)(1-a\_{1}^{T}) grows like T−α1T^{-\alpha\_{1}}. Therefore, we can see that

|  |  |  |
| --- | --- | --- |
|  | ((1−a0T)​(1−a1T)T​νT)1/2and1−a0TT​νT\Big(\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}\Big)^{1/2}\qquad\text{and}\qquad\frac{1-a\_{0}^{T}}{T\nu^{T}} |  |

are of the same order. Thus, Theorem [3.1](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") guarantees that

|  |  |  |
| --- | --- | --- |
|  | ((1−a0T)​(1−a1T)T​νT)1/2​(Ft​TT,+−Ft​T−,T)→Vt\Big(\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}\Big)^{1/2}\big(F\_{tT}^{T,+}-F\_{tT}^{-,T}\big)\to V\_{t} |  |

where VV is given by Proposition [3.3](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 Scaling limit of the core flow ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."). We just need to compute the limit of

|  |  |  |
| --- | --- | --- |
|  | ((1−a0T)​(1−a1T)T​νT)1/2​(Nt​T+,T−Nt​T−,T).\Big(\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}\Big)^{1/2}\big(N\_{tT}^{+,T}-N\_{tT}^{-,T}\big). |  |

We write

|  |  |  |
| --- | --- | --- |
|  | NtT,+−Nt−,T=MtT,+−Mt−,T+ΛtT,+−Λt−,T,N\_{t}^{T,+}-N\_{t}^{-,T}=M\_{t}^{T,+}-M\_{t}^{-,T}+\Lambda\_{t}^{T,+}-\Lambda\_{t}^{-,T}, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΛtT,+−Λt−,T=v2t​𝚲tT\displaystyle\Lambda\_{t}^{T,+}-\Lambda\_{t}^{-,T}=\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}{\boldsymbol{\Lambda}}\_{t}^{T} | =∫0tψ2T​(t−s)​v2t⋅𝐅sT​𝑑s+∫0tψ2T​(t−s)​(Ms+,T−Ms−,T)​𝑑s\displaystyle=\int\_{0}^{t}\psi\_{2}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\mathbf{F}^{T}\_{s}\,ds+\int\_{0}^{t}\psi\_{2}^{T}(t-s)(M^{+,T}\_{s}-M^{-,T}\_{s})\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0tψ2T​(t−s)​v2t⋅𝐅sT​𝑑s+∫0t∫0t−sψ2T​(u)​𝑑u​d​(Ms+,T−Ms−,T)\displaystyle=\int\_{0}^{t}\psi\_{2}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\mathbf{F}^{T}\_{s}\,ds+\int\_{0}^{t}\int\_{0}^{t-s}\psi\_{2}^{T}(u)\,du\,d(M^{+,T}\_{s}-M^{-,T}\_{s}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0tψ2T​(t−s)​v2t⋅𝐅sT​𝑑s+∫0∞ψ2T​(u)​𝑑u​(Mt+,T−Mt−,T)\displaystyle=\int\_{0}^{t}\psi\_{2}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\mathbf{F}\_{s}^{T}\,ds+\int\_{0}^{\infty}\psi\_{2}^{T}(u)\,du(M^{+,T}\_{t}-M^{-,T}\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0t∫t−s∞ψ2T​(u)​𝑑u​d​(Ms+,T−Ms−,T).\displaystyle\qquad-\int\_{0}^{t}\int\_{t-s}^{\infty}\psi\_{2}^{T}(u)\,du\,d(M^{+,T}\_{s}-M^{-,T}\_{s}). |  |

Therefore we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | NtT,+−Nt−,T\displaystyle N\_{t}^{T,+}-N\_{t}^{-,T} | =∫0tψ2T​(t−s)​v2t⋅𝐅sT​𝑑s+(1+∫0∞ψ2T​(u)​𝑑u)​(Mt+,T−Mt−,T)\displaystyle=\int\_{0}^{t}\psi\_{2}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\mathbf{F}^{T}\_{s}\,ds+(1+\int\_{0}^{\infty}\psi\_{2}^{T}(u)\,du)(M^{+,T}\_{t}-M^{-,T}\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0t∫t−s∞ψ2T​(u)​𝑑u​d​(Ms+,T−Ms−,T).\displaystyle\qquad-\int\_{0}^{t}\int\_{t-s}^{\infty}\psi\_{2}^{T}(u)\,du\,d(M^{+,T}\_{s}-M^{-,T}\_{s}). |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0tψ2T​(t−s)​v2t⋅𝐅sT​𝑑s+11−a1T​(‖φ1‖1−‖φ2‖1)​(Mt+,T−Mt−,T)\displaystyle=\int\_{0}^{t}\psi\_{2}^{T}(t-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\mathbf{F}^{T}\_{s}\,ds+\frac{1}{1-a\_{1}^{T}(\|\varphi\_{1}\|\_{1}-\|\varphi\_{2}\|\_{1})}(M^{+,T}\_{t}-M^{-,T}\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0t∫t−s∞ψ2T​(u)​𝑑u​d​(Ms+,T−Ms−,T).\displaystyle\qquad-\int\_{0}^{t}\int\_{t-s}^{\infty}\psi\_{2}^{T}(u)\,du\,d(M^{+,T}\_{s}-M^{-,T}\_{s}). |  |

After rescaling, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ((1−a0T)​(1−a1T)T​νT)1/2​(Nt​T+,T−Nt​T−,T)=((1−a0T)​(1−a1T)T​νT)1/2​∫0t​Tψ2T​(T​t−s)​v2t⋅𝐅sT​𝑑s+11−a1T​(‖φ1‖1−‖φ2‖1)​(M¯t+,T−M¯t−,T)−RtT\begin{split}\Big(\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}\Big)^{1/2}\big(N\_{tT}^{+,T}-N\_{tT}^{-,T}\big)&=\Big(\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}\Big)^{1/2}\int\_{0}^{tT}\psi\_{2}^{T}(Tt-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\mathbf{F}^{T}\_{s}\,ds\\ &+\frac{1}{1-a\_{1}^{T}(\|\varphi\_{1}\|\_{1}-\|\varphi\_{2}\|\_{1})}(\overline{M}^{+,T}\_{t}-\overline{M}^{-,T}\_{t})-R^{T}\_{t}\end{split} |  | (5) |

where

|  |  |  |
| --- | --- | --- |
|  | RtT=∫0t∫T​(t−s)∞ψ2T​(u)​𝑑u​d​(M¯s+,T−M¯s−,T).R^{T}\_{t}=\int\_{0}^{t}\int\_{T(t-s)}^{\infty}\psi\_{2}^{T}(u)\,du\,d(\overline{M}^{+,T}\_{s}-\overline{M}^{-,T}\_{s}). |  |

Following the same argument as in the proof of Theorem 3.2 in [[24](https://arxiv.org/html/2601.23172v2#bib.bib219 "The microstructural foundations of leverage effect and rough volatility")], we conclude the convergence of RTR^{T} to zero in the sense of finite dimensional laws.
  
Furthermore, from Theorem [3.4](https://arxiv.org/html/2601.23172v2#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.2 Scaling limit of the reaction orders ‣ 3 Scaling limits of the order flows ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study."), we know that the second term in ([5](https://arxiv.org/html/2601.23172v2#A2.E5 "In B.7 Proof of Theorem 3.6 ‣ Appendix B Proof of the results of Section 3 ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.")) converges to

|  |  |  |
| --- | --- | --- |
|  | 11−(‖φ1‖1−‖φ2‖1)​(Zt+−Zt−).\frac{1}{1-(\|\varphi\_{1}\|\_{1}-\|\varphi\_{2}\|\_{1})}(Z^{+}\_{t}-Z^{-}\_{t}). |  |

It remains to study the first term

|  |  |  |
| --- | --- | --- |
|  | ((1−a0T)​(1−a1T)T​νT)1/2​∫0t​Tψ2T​(T​t−s)​v2t⋅𝐅sT​𝑑s.\Big(\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}\Big)^{1/2}\int\_{0}^{tT}\psi\_{2}^{T}(Tt-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\mathbf{F}^{T}\_{s}\,ds. |  |

After proper rescaling, we obtain

|  |  |  |
| --- | --- | --- |
|  | ((1−a0T)​(1−a1T)T​νT)1/2​∫0t​Tψ2T​(t​T−s)​v2t⋅FsT​𝑑s=cT​∫0tT​ψ2T​(T​(t−s))​v2t⋅F¯sT​𝑑s\displaystyle\Big(\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}\Big)^{1/2}\int\_{0}^{tT}\psi\_{2}^{T}(tT-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot F^{T}\_{s}\,ds=c^{T}\int\_{0}^{t}T\psi\_{2}^{T}(T(t-s))\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\overline{F}^{T}\_{s}\,ds |  |

where

|  |  |  |
| --- | --- | --- |
|  | cT=(T​νT​(1−a1T))/(1−a0T)→λ1​μ1.c^{T}=\sqrt{(T\nu^{T}(1-a\_{1}^{T}))/(1-a\_{0}^{T})}\to\sqrt{\lambda\_{1}\mu\_{1}}. |  |

To understand its asymptotic behavior as TT goes to infinity, one can compute the Fourier transform ψ2T(T⋅)^\widehat{\psi\_{2}^{T}(T\cdot)} of ψ2T(T⋅)\psi^{T}\_{2}(T\cdot). We have

|  |  |  |
| --- | --- | --- |
|  | ψ2T(T⋅)^​(z)=∫x∈ℝ+ψ2T​(T​x)​ei​x​z​𝑑x=1T​∑n≥1(a1T)n​(k^2​(z/T))n=a1T​k^2​(z/T)T​(1−a1T​k^2​(z/T))\widehat{\psi\_{2}^{T}(T\cdot)}(z)=\int\_{x\in\mathbb{R}\_{+}}\psi\_{2}^{T}(Tx)e^{ixz}dx=\frac{1}{T}\sum\_{n\geq 1}(a^{T}\_{1})^{n}\left(\widehat{k}\_{2}(z/T)\right)^{n}=\frac{a\_{1}^{T}\widehat{k}\_{2}(z/T)}{T\left(1-a\_{1}^{T}\widehat{k}\_{2}(z/T)\right)} |  |

As TT goes to infinity, k^j​(z/T)\widehat{k}\_{j}(z/T) tends to ‖k2‖1{|\kern-1.07639pt|k\_{2}|\kern-1.07639pt|}\_{1} and recall that ‖k2‖1<1{|\kern-1.07639pt|k\_{2}|\kern-1.07639pt|}\_{1}<1. Therefore, we see that

|  |  |  |
| --- | --- | --- |
|  | T​ψ2T(T⋅)^​(z)→‖k2‖11−‖k2‖1=‖φ1‖1−‖φ2‖11−(‖φ1‖1−‖φ2‖1)T\widehat{\psi\_{2}^{T}(T\cdot)}(z)\to\frac{{|\kern-1.07639pt|k\_{2}|\kern-1.07639pt|}\_{1}}{1-{|\kern-1.07639pt|k\_{2}|\kern-1.07639pt|}\_{1}}=\frac{{|\kern-1.07639pt|\varphi\_{1}|\kern-1.07639pt|}\_{1}-{|\kern-1.07639pt|\varphi\_{2}|\kern-1.07639pt|}\_{1}}{1-({|\kern-1.07639pt|\varphi\_{1}|\kern-1.07639pt|}\_{1}-{|\kern-1.07639pt|\varphi\_{2}|\kern-1.07639pt|}\_{1})} |  |

and consequently, if we define

|  |  |  |
| --- | --- | --- |
|  | χT​(d​t):=T​ψ2T​(T​t)​d​t\chi\_{T}(dt):=T\psi\_{2}^{T}(Tt)dt |  |

then we have

|  |  |  |
| --- | --- | --- |
|  | χT​(d​t)→‖φ1‖1−‖φ2‖11−(‖φ1‖1−‖φ2‖1)​δ0​(d​t)\chi\_{T}(dt)\to\frac{{|\kern-1.07639pt|\varphi\_{1}|\kern-1.07639pt|}\_{1}-{|\kern-1.07639pt|\varphi\_{2}|\kern-1.07639pt|}\_{1}}{1-({|\kern-1.07639pt|\varphi\_{1}|\kern-1.07639pt|}\_{1}-{|\kern-1.07639pt|\varphi\_{2}|\kern-1.07639pt|}\_{1})}\delta\_{0}(dt) |  |

Thus, we have shown that

|  |  |  |
| --- | --- | --- |
|  | ((1−a0T)​(1−a1T)T​νT)1/2​∫0t​Tψ2T​(T​t−s)​v2t⋅𝐅sT​𝑑s→λ1​μ1​(‖φ1‖1−‖φ2‖1)1−(‖φ1‖1−‖φ2‖1)​Vt.\Big(\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}\Big)^{1/2}\int\_{0}^{tT}\psi\_{2}^{T}(Tt-s)\mskip 1.0mu\prescript{\smash{\mathrm{t}}}{}{\mathstrut v\_{2}}\cdot\mathbf{F}^{T}\_{s}\,ds\to\frac{\sqrt{\lambda\_{1}\mu\_{1}}({|\kern-1.07639pt|\varphi\_{1}|\kern-1.07639pt|}\_{1}-{|\kern-1.07639pt|\varphi\_{2}|\kern-1.07639pt|}\_{1})}{1-({|\kern-1.07639pt|\varphi\_{1}|\kern-1.07639pt|}\_{1}-{|\kern-1.07639pt|\varphi\_{2}|\kern-1.07639pt|}\_{1})}V\_{t}. |  |

Eventually, we obtain

|  |  |  |
| --- | --- | --- |
|  | ((1−a0T)​(1−a1T)T​νT)1/2​St​TT→λ1​μ1​(‖φ1‖1−‖φ2‖1)1−(‖φ1‖1−‖φ2‖1)​Vt+11−(‖φ1‖1−‖φ2‖1)​(Zt+−Zt−)\Big(\frac{(1-a\_{0}^{T})(1-a\_{1}^{T})}{T\nu^{T}}\Big)^{1/2}S^{T}\_{tT}\to\frac{\sqrt{\lambda\_{1}\mu\_{1}}({|\kern-1.07639pt|\varphi\_{1}|\kern-1.07639pt|}\_{1}-{|\kern-1.07639pt|\varphi\_{2}|\kern-1.07639pt|}\_{1})}{1-({|\kern-1.07639pt|\varphi\_{1}|\kern-1.07639pt|}\_{1}-{|\kern-1.07639pt|\varphi\_{2}|\kern-1.07639pt|}\_{1})}V\_{t}+\frac{1}{1-(\|\varphi\_{1}\|\_{1}-\|\varphi\_{2}\|\_{1})}(Z^{+}\_{t}-Z^{-}\_{t}) |  |

in the sense of finite dimensional laws.

## Appendix C Data description and stock universe

This appendix describes the dataset and stock universe used to estimate the Hurst exponent of signed order flow.

Our empirical analysis is conducted on a cross-section of liquid equities listed on major exchanges. The final universe consists of large-cap stocks that are actively traded throughout the sample period. Table [1](https://arxiv.org/html/2601.23172v2#A3.T1 "Table 1 ‣ Appendix C Data description and stock universe ‣ A unified theory of order flow, market impact, and volatility1footnote 11footnote 1Youssef Ouazzani Chahdi, Mathieu Rosenbaum and Grégoire Szymanski gratefully acknowledge support from the ILB Chair Artificial Intelligence and Quantitative Methods for Finance at University Paris Dauphine-PSL. The authors thank Pavel Chigansky and Marina Kleptsyna for key input on mixed fractional Brownian motion. They are also grateful to Jean-Philippe Bouchaud and Kevin Webster for inspiring discussions on order flow modeling, and thank BMLL Technologies for providing the historical market data used in this study.") reports the list of stocks used in the analysis, together with their tickers, exchanges, and sample years.

The data consist of trade-by-trade records obtained from BMLL, covering the period from January 2021 to December 2024.
Only regular trading days are retained; weekends, holidays, and shortened trading sessions are excluded.
All timestamps are expressed in local exchange time and restricted to standard market hours.

For each stock, the dataset contains the full sequence of executed trades with precise timestamps, traded volumes, transaction sides and prices.
The time resolution of the data is at least the millisecond (or microsecond) level, allowing for a detailed reconstruction of order flow dynamics.

The signed order flow is defined as the sequence

|  |  |  |
| --- | --- | --- |
|  | εt​vt,\varepsilon\_{t}v\_{t}, |  |

where εt∈{+1,−1}\varepsilon\_{t}\in\{+1,-1\} denotes the trade sign and vtv\_{t} the traded volume at time tt. The unsigned order flow is defined similarly by taking εt=1\varepsilon\_{t}=1.

The signed and unsigned order flow series are subsequently aggregated over fixed time intervals to construct the increments used in the estimation of the Hurst exponents H0H\_{0} and H1H\_{1}.

| Stock Name | Ticker | Exchange | Region |
| --- | --- | --- | --- |
| Airbus SE | AIR | Euronext Paris | Europe |
| Kering SA | KER | Euronext Paris | Europe |
| Vinci SA | DG | Euronext Paris | Europe |
| L’Oréal SA | OR | Euronext Paris | Europe |
| AXA SA | CS | Euronext Paris | Europe |
| Schneider Electric SE | SU | Euronext Paris | Europe |
| Crédit Agricole SA | ACA | Euronext Paris | Europe |
| EssilorLuxottica SA | EL | Euronext Paris | Europe |
| LVMH Moët Hennessy Louis Vuitton SE | MC | Euronext Paris | Europe |
| TotalEnergies SE | TTE | Euronext Paris | Europe |
| Safran SA | SAF | Euronext Paris | Europe |
| Danone SA | BN | Euronext Paris | Europe |
| Sanofi SA | SAN | Euronext Paris | Europe |
| BNP Paribas SA | BNP | Euronext Paris | Europe |
| Orange SA | ORA | Euronext Paris | Europe |
| Renault SA | RNO | Euronext Paris | Europe |
| Engie SA | ENGI | Euronext Paris | Europe |
| STMicroelectronics NV | STM | Euronext Paris | Europe |
| Air Liquide SA | AI | Euronext Paris | Europe |
| Société Générale SA | GLE | Euronext Paris | Europe |
| Occidental Petroleum Corporation | OXY | NYSE | United States |
| Alibaba Group Holding Ltd. | BABA | NYSE | United States |
| Uber Technologies, Inc. | UBER | NYSE | United States |
| Exxon Mobil Corporation | XOM | NYSE | United States |
| NIKE, Inc. | NKE | NYSE | United States |
| Procter & Gamble Company | PG | NYSE | United States |
| Chevron Corporation | CVX | NYSE | United States |
| Shopify Inc. | SHOP | NYSE | United States |
| The Coca-Cola Company | KO | NYSE | United States |
| ConocoPhillips | COP | NYSE | United States |
| Pfizer Inc. | PFE | NYSE | United States |
| Citigroup Inc. | C | NYSE | United States |
| Visa Inc. | V | NYSE | United States |
| Devon Energy Corporation | DVN | NYSE | United States |
| General Motors Company | GM | NYSE | United States |
| Synchrony Financial | SYF | NYSE | United States |
| Johnson & Johnson | JNJ | NYSE | United States |
| Freeport-McMoRan Inc. | FCX | NYSE | United States |
| Carnival Corporation | CCL | NYSE | United States |
| Schlumberger Limited | SLB | NYSE | United States |

Table 1: List of stocks used in the estimation of the Hurst exponent of signed order flow.