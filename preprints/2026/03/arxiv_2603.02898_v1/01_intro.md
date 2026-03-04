---
authors:
- Bo Pieter Johannes Andrée
doc_id: arxiv:2603.02898v1
family_id: arxiv:2603.02898
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from
  Local Food Price Data'
url_abs: http://arxiv.org/abs/2603.02898v1
url_html: https://arxiv.org/html/2603.02898v1
venue: arXiv q-fin
version: 1
year: 2026
---


Bo Pieter Johannes Andrée

(January, 2026)

###### Abstract

Range-based volatility estimators are widely used in financial econometrics to quantify risk and market stress, yet their application to local commodity markets remains limited. This paper shows how open–high–low–close (OHLC) volatility estimators can be adapted to monitor localized market distress across diverse development contexts, including conflict-affected settings, climate-exposed regions, remote and thinly traded markets, and import- and logistics-constrained urban hubs. Using monthly food price data from the World Bank’s Real-Time Prices dataset, several volatility measures—including the Parkinson, Garman–Klass, Rogers–Satchell, and Yang–Zhang estimators—are constructed and evaluated against independently documented disruption timelines. Across settings, elevated volatility aligns with episodes linked to insecurity and market fragmentation, extreme weather and disaster shocks, policy and fuel-cost adjustments, and global supply-chain and trade disruptions. Volatility also detects stress that standard momentum indicators such as the relative strength index (RSI) can miss, including symmetric or rapidly reversing shocks in which offsetting supply and demand disturbances dampen net directional price movements while amplifying intra-period dispersion. Overall, OHLC-based volatility indicators provide a robust and interpretable signal of market disruptions and complement price-level monitoring for applications spanning financial risk, humanitarian early warning, and trade.111\*†{\dagger}Bo Pieter Johannes Andrée, The World Bank, Development Economics, Data Group, can be contacted at bandree(at)worldbank.org. Funding by the World Bank’s Food Systems 2030 (FS2030) Multi-Donor Trust Fund program (TF0C7822) and the Umbrella Facility for Trade Multi-Donor Trust Fund 2.0 (TF074184) is gratefully acknowledged. The findings, interpretations, and conclusions expressed in this paper are entirely those of the author. They do not necessarily represent the views of the World Bank and its affiliated organizations, or those of the Executive Directors of the World Bank or the governments they represent.
  
  
JEL: C01, C14, C22, C53, Q11.
  
  
Keywords: Volatility estimation, Range-based estimators, Market stress indicators, Price monitoring, OHLC data.

## 1 Introduction

Volatility is a fundamental measure of market conditions. In financial markets, elevated volatility signals uncertainty and is frequently associated with reduced liquidity and impaired market functioning (Schwert, [1989](#bib.bib54 "Why does stock market volatility change over time?"); Bollerslev et al., [1992](#bib.bib53 "ARCH modeling in finance: a review of the theory and empirical evidence"); Adrian et al., [2017](#bib.bib42 "Market liquidity after the financial crisis")). A central insight from market microstructure is that well-functioning markets support continuous price discovery around an “efficient price,” while frictions such as higher transaction costs and widening spreads distort price adjustment and amplify short-horizon dispersion (Demsetz, [1968](#bib.bib28 "The cost of transacting"); Hasbrouck, [1995](#bib.bib29 "One security, many markets: determining the contributions to price discovery"), [2002](#bib.bib36 "Stalking the “efficient price” in market microstructure specifications: an overview"); Roll, [1984](#bib.bib38 "A simple implicit measure of the effective bid-ask spread in an efficient market"); Corwin and Schultz, [2012](#bib.bib39 "A simple way to estimate bid-ask spreads from daily high and low prices")). Financial econometrics offers a rich toolkit for measuring volatility from price data, including close-to-close estimators and more efficient range-based estimators that exploit information in intra-period highs and lows (Parkinson, [1980](#bib.bib9 "The extreme value method for estimating the variance of the rate of return"); Garman and Klass, [1980](#bib.bib10 "On the estimation of security price volatilities from historical data"); Rogers and Satchell, [1991](#bib.bib11 "Estimating variance from high, low and closing prices"); Yang and Zhang, [2000](#bib.bib12 "Drift-independent volatility estimation based on high, low, open, and close prices")). These measures are widely used in risk management, derivatives pricing, and trading strategies (Andersen et al., [2003](#bib.bib55 "Modeling and forecasting realized volatility"); Baillie et al., [1996](#bib.bib13 "Fractionally integrated generalized autoregressive conditional heteroskedasticity"); Hasbrouck and Saar, [2013](#bib.bib35 "Low-latency trading")).

Despite their established role in finance, OHLC-based range estimators have seen limited systematic application in monitoring local commodity markets in developing countries. This gap is consequential. In settings exposed to conflict, climate shocks, policy disruptions, and global price transmission, volatility can reveal stress that price levels alone may not capture. Market integration can weaken even when average prices move gradually, as disruptions raise arbitrage costs, reduce trading depth, and increase uncertainty about supply and demand. While the institutional settings differ from financial markets, the economic logic is analogous: in both contexts, elevated transaction costs and reduced market depth manifest as increased short-horizon price dispersion. Dysfunction is more likely to appear as widening spreads, abrupt reversals, and elevated volatility, echoing patterns documented for stressed financial markets (Copeland and Galai, [1983](#bib.bib30 "Information effects on the bid-ask spread"); Fleming and Remolona, [1999](#bib.bib31 "Price formation and liquidity in the U.S. Treasury market: the response to public information"); Bao et al., [2011](#bib.bib32 "The illiquidity of corporate bonds")). This distinction matters for market monitoring: price levels primarily track changes in purchasing power, whereas volatility extracted from intra-period dispersion provides complementary information about frictions in market clearing and price discovery. In particular, compound shocks that simultaneously affect supply and demand can dampen net price changes while amplifying intra-period dispersion, making volatility an informative indicator of market stress.

The case for volatility monitoring is especially strong in food markets, where trading volumes and flows are unobserved and prices alone paint an incomplete picture. Food price instability is widely recognized as a macroeconomic and food-security concern (Food and Agriculture Organization of the United Nations, [2009](#bib.bib41 "The food price crisis of 2007/2008: evidence and implications for food security"); High Level Panel of Experts on Food Security and Nutrition, [2011](#bib.bib44 "Price volatility and food security"); Gilbert, [2010](#bib.bib43 "How to understand high food prices")), and empirical work links volatility to food-security outcomes and risk transmission across markets (Ben Abdallah et al., [2021](#bib.bib45 "Exploring the effect of food price volatility on food security in tunisia"); López Cabrera and Schulz, [2013](#bib.bib46 "Volatility spillovers between crude oil and food prices"); Hanif et al., [2021](#bib.bib47 "Tail dependence risk and spillovers between oil and food prices")). Yet many operational tools remain centered on price levels and trend-following momentum indicators such as RSI and MACD (moving average convergence divergence) (Appel, [1979](#bib.bib6 "The moving average convergence-divergence trading method"); Murphy, [1999](#bib.bib7 "Technical analysis of the financial markets"); Wilder, [1978](#bib.bib8 "New concepts in technical trading systems")), which can understate short-lived reversals and symmetric shocks that manifest primarily through instability rather than persistent directional movement.

The need for robust, lightweight signals is growing as global monitoring systems increasingly rely on near-real-time indicators to support decision-making. Volatility-based surveillance has long been standard practice in financial markets, where exchanges, clearing houses, and regulators routinely monitor market functionality and liquidity. Macroeconomic monitoring systems and early warning systems for food security have been slower to adopt such measures, despite operating in environments where market dysfunction carries immediate welfare consequences (Barrett, [2010](#bib.bib3 "Measuring food insecurity")). Current operational platforms integrate climate, production, market, and conflict information to guide timely assessments (Backer and Billing, [2021](#bib.bib26 "Validating famine early warning systems network projections of food security in africa, 2009–2020"); Bertetti et al., [2024](#bib.bib27 "An independent evaluation of the famine early warning systems network food security projections")), and the World Bank’s Real-Time Prices (RTP) initiative complements these efforts by harmonizing partner price observations into monthly OHLC series across dozens of countries (Development Data Group, [2021](#bib.bib33 "Monthly food price estimates by product and market"); Andrée, [2021](#bib.bib4 "Estimating food price inflation from partial surveys"); Andrée and Pape, [2023](#bib.bib5 "Machine learning imputation of high frequency price surveys in papua new guinea"))—yet volatility extracted from these series remains underutilized.

This paper demonstrates that OHLC-based volatility estimators applied to local market price series provide a robust and interpretable signal of market distress across diverse settings. We compute close-to-close and range-based estimators directly from RTP’s OHLC series, compare their operational properties, and apply a transparent threshold rule to flag stress episodes. Across the estimators considered, the Yang–Zhang measure (Yang and Zhang, [2000](#bib.bib12 "Drift-independent volatility estimation based on high, low, open, and close prices")) offers a practical balance between responsiveness and noise reduction, and the detected episodes align closely with documented shocks. We illustrate the approach through five applications spanning distinct regions, market structures, and shock profiles: Sudan (Darfur), Somalia (Baidoa), Cameroon (Far North), Haiti (Port-au-Prince), and the Philippines (Sulu). Across these settings, volatility spikes coincide with conflict dynamics, natural hazards, policy and fuel-cost shocks, and selected global transmission events, including periods in which momentum-based indicators such as RSI do not provide clear signals. As shown in Section [4](#S4 "4 Results ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"), volatility flags a substantial share of documented crisis episodes that RSI misses, particularly when price movements reverse within the observation window or when compound shocks produce offsetting directional effects. The workflow is computationally lightweight, does not require model re-estimation as new observations arrive, and is suitable for integration into automated alert systems.

The remainder of the paper proceeds as follows. Section [2](#S2 "2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") describes the data source and OHLC structure. Section [3](#S3 "3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") presents the volatility estimators and detection rule. Section [4](#S4 "4 Results ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") presents the five country case studies. Section [5](#S5 "5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") discusses implications and limitations. Section [6](#S6 "6 Conclusion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") concludes.

## 2 Data

### 2.1 Price data and OHLC structure

The data are from the World Bank Real-Time Prices (RTP) system, constructed using the methods of Andrée ([2021](#bib.bib4 "Estimating food price inflation from partial surveys")) and Andrée and Pape ([2023](#bib.bib5 "Machine learning imputation of high frequency price surveys in papua new guinea")). RTP generates high-frequency food price series by combining price observations from the World Food Programme, FAO, national statistical offices, and other partners with machine-learning-based imputation to fill gaps in space, time, and commodity coverage. The operational system currently covers dozens of fragile and conflict-affected countries, with weekly updates across hundreds of markets and staple commodities. The data have been validated against independent survey and crowdsourcing exercises (Adewopo et al., [2025](#bib.bib20 "AI-imputed and crowdsourced price data show strong agreement with traditional price surveys in data-scarce environments")) and global commodities data (Emediegwu and Rogna, [2024](#bib.bib21 "Agricultural commodities’ price transmission from international to local markets in developing countries")), and have supported country applications in Myanmar (Ecker et al., [2023](#bib.bib24 "Mitigating poverty and undernutrition through social protection: a simulation analysis of the covid-19 pandemic in bangladesh and myanmar")), Afghanistan (Gbadegesin et al., [2024](#bib.bib18 "Climate shocks and their effects on food security, prices, and agricultural wages in afghanistan")), Malawi (Kaiyatsa et al., [2023](#bib.bib25 "How do transport costs affect price dispersion of nutrient-dense foods across markets in rural Malawi?")), South Sudan (Schincariol and Chadefaux, [2024](#bib.bib22 "Temporal patterns in migration flows evidence from south sudan")), and Sudan (Bari et al., [2025](#bib.bib23 "Exploring the impact of secession on food prices: a case study of Sudan")). Recent work has also leveraged this data to forecast food-crisis risk (Andrée et al., [2020](#bib.bib48 "Predicting food crises"); Wang et al., [2020](#bib.bib49 "Stochastic modeling of food insecurity"), [2022](#bib.bib50 "Transitions into and out of food insecurity: a probabilistic approach with panel data evidence from 15 countries"); Penson et al., [2024](#bib.bib51 "A data-driven approach for early detection of food insecurity in yemen’s humanitarian crisis")).

At the core of RTP is a fractionally integrated Generalized Autoregressive Conditional Heteroskedasticity (fiGARCH) model with generalized error distribution (GED) innovations applied to partially observed and partially imputed price series, which allows the system to model long-memory volatility dynamics and to track not only the closing price but also synthetic open, high, and low prices within each aggregation period (Baillie et al., [1996](#bib.bib13 "Fractionally integrated generalized autoregressive conditional heteroskedasticity"); Andrée, [2021](#bib.bib4 "Estimating food price inflation from partial surveys")).222RTP is implemented as three sub-series: Real-Time Food Prices (RTFP) for food commodities, Real-Time Energy Prices (RTEP) for fuels, and Real-Time Foreign Exchange Rates (RTFX) for currency markets (Development Data Group, [2021](#bib.bib33 "Monthly food price estimates by product and market")). The volatility indicators developed here use the RTFP OHLC series, but the methodology extends directly to energy and exchange rate series. These OHLC estimates are stored at monthly frequency for each market–product combination. While they are model-based rather than directly observed, they summarize within-period price dispersion in a way that is compatible with standard OHLC-based volatility estimators.

The following subsections describe how the synthetic open–high–low–close (OHLC) price series are constructed from a fiGARCH model with GED innovations. The basic idea is to (i) estimate a long-memory conditional variance model for log returns, (ii) use the filtered conditional variance and innovation distribution to obtain the expected price range (a central 50% interval, 25th–75th percentiles) of the conditional price distribution within each period, and (iii) map this interval into low and high prices while treating the open as the conditional expectation and the close as the realized end-of-period price. Understanding this construction clarifies how the range-based volatility estimators presented in Section [3](#S3 "3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") relate to the underlying data-generating process.

### 2.2 fiGARCH–GED model for log returns

Let PtP\_{t} denote the price index at (monthly) time tt and xt=ln⁡Ptx\_{t}=\ln P\_{t}
its logarithm. The (log) return over one period is

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=xt−xt−1=ln⁡(PtPt−1).r\_{t}=x\_{t}-x\_{t-1}=\ln\left(\frac{P\_{t}}{P\_{t-1}}\right). |  | (1) |

In the RTP framework, log returns are modeled as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=μ+εt,εt=ht​zt,r\_{t}=\mu+\varepsilon\_{t},\qquad\varepsilon\_{t}=\sqrt{h\_{t}}\,z\_{t}, |  | (2) |

where μ\mu is a constant drift term and hth\_{t} is the conditional variance.

Let {ℱt}\{\mathcal{F}\_{t}\} denote the filtration generated by {rs:s≤t}\{r\_{s}:s\leq t\}. We assume that {zt}\{z\_{t}\} is a standardized martingale difference sequence with respect to {ℱt}\{\mathcal{F}\_{t}\}, that is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[zt∣ℱt−1]=0,𝔼​[zt2∣ℱt−1]=1a.s.\mathbb{E}[z\_{t}\mid\mathcal{F}\_{t-1}]=0,\qquad\mathbb{E}[z\_{t}^{2}\mid\mathcal{F}\_{t-1}]=1\quad\text{a.s.} |  | (3) |

Conditional on ℱt−1\mathcal{F}\_{t-1} we take ztz\_{t} to follow a standardized generalized error distribution (GED) with shape parameter ν>0\nu>0 and unit variance. Let Fν​(⋅)F\_{\nu}(\cdot) denote the corresponding cumulative distribution function.

The conditional variance process hth\_{t} follows a fiGARCH(1,d,1)(1,d,1) recursion (Baillie et al., [1996](#bib.bib13 "Fractionally integrated generalized autoregressive conditional heteroskedasticity")). A convenient representation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−β1​L)​ht=ω+[(1−β1​L)−(1−ϕ1​L)​(1−L)d]​εt2,(1-\beta\_{1}L)\,h\_{t}=\omega+\bigl[(1-\beta\_{1}L)-(1-\phi\_{1}L)(1-L)^{d}\bigr]\varepsilon\_{t}^{2}, |  | (4) |

where LL is the lag operator (L​ht=ht−1)(Lh\_{t}=h\_{t-1}), ω>0\omega>0, β1\beta\_{1} and ϕ1\phi\_{1} are non-negative parameters, and (1−L)d(1-L)^{d} is the fractional differencing operator with d∈(0,1)d\in(0,1) capturing long memory in volatility.

Given estimated parameters

|  |  |  |
| --- | --- | --- |
|  | θ=(μ,ω,β1,ϕ1,d,ν),\theta=(\mu,\omega,\beta\_{1},\phi\_{1},d,\nu), |  |

filtering the model yields sequences of conditional variances hth\_{t} and standardized residuals ztz\_{t} for t=1,…,Tt=1,\dots,T. These in turn define, for each tt, a conditional distribution for the next-period log return:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt+1∣ℱt∼μ+ht+1​zt+1,zt+1∼GED​(0,1,ν),r\_{t+1}\mid\mathcal{F}\_{t}\sim\mu+\sqrt{h\_{t+1}}\,z\_{t+1},\qquad z\_{t+1}\sim\text{GED}(0,1,\nu), |  | (5) |

where ℱt\mathcal{F}\_{t} denotes the information set up to time tt.

#### 2.2.1 Generalized error distribution and tail behavior

The GED allows the conditional variance hth\_{t} and the tail thickness (kurtosis) of returns to be modeled separately. The probability density function (pdf) of a GED with location 0, scale parameter β>0\beta>0 and shape ν\nu is

|  |  |  |  |
| --- | --- | --- | --- |
|  | fGED​(z;β,ν)=ν2​β​Γ​(1/ν)​exp⁡{−(|z|β)ν},z∈ℝ,f\_{\text{GED}}(z;\beta,\nu)=\frac{\nu}{2\beta\,\Gamma(1/\nu)}\exp\!\left\{-\left(\frac{|z|}{\beta}\right)^{\nu}\right\},\qquad z\in\mathbb{R}, |  | (6) |

where Γ​(⋅)\Gamma(\cdot) is the gamma function. The variance of this distribution is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var⁡(z)=β2​Γ​(3/ν)Γ​(1/ν).\operatorname{Var}(z)=\beta^{2}\,\frac{\Gamma(3/\nu)}{\Gamma(1/\nu)}. |  | (7) |

To obtain standardized innovations with unit variance, we set

|  |  |  |  |
| --- | --- | --- | --- |
|  | β​(ν)=(Γ​(1/ν)Γ​(3/ν))1/2,\beta(\nu)=\left(\frac{\Gamma(1/\nu)}{\Gamma(3/\nu)}\right)^{1/2}, |  | (8) |

and write

|  |  |  |  |
| --- | --- | --- | --- |
|  | zt∼GED​(0,β​(ν),ν),𝔼​[zt]=0,Var⁡(zt)=1.z\_{t}\sim\text{GED}\bigl(0,\,\beta(\nu),\,\nu\bigr),\qquad\mathbb{E}[z\_{t}]=0,\quad\operatorname{Var}(z\_{t})=1. |  | (9) |

The kurtosis of the standardized GED is

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ​(ν)=𝔼​[zt4]{Var⁡(zt)}2=Γ​(5/ν)​Γ​(1/ν)Γ​(3/ν)2.\kappa(\nu)=\frac{\mathbb{E}[z\_{t}^{4}]}{\{\operatorname{Var}(z\_{t})\}^{2}}=\frac{\Gamma(5/\nu)\,\Gamma(1/\nu)}{\Gamma(3/\nu)^{2}}. |  | (10) |

When ν=2\nu=2, the GED reduces to the Gaussian distribution and κ​(2)=3\kappa(2)=3. For ν<2\nu<2, the distribution is leptokurtic with heavier tails and κ​(ν)>3\kappa(\nu)>3, implying a higher probability of large realizations of |zt||z\_{t}| (and thus of large returns) relative to the Gaussian case. For ν>2\nu>2, the tails become lighter than Gaussian.

In the fiGARCH–GED model, the conditional variance hth\_{t} and the shape parameter ν\nu are estimated jointly. This separation has two important implications for the behavior of the OHLC series and the range-based volatility estimators:

1. 1.

   Sharp but temporary price swings. Because the innovations are heavy-tailed when ν<2\nu<2, a single large “candle” (i.e., an unusually large movement in the price index) can be accommodated by a large realization of ztz\_{t} without implying that all subsequent innovations must also be large. In the fiGARCH recursion ([4](#S2.E4 "In 2.2 fiGARCH–GED model for log returns ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data")), a large squared shock εt2=ht​zt2\varepsilon\_{t}^{2}=h\_{t}z\_{t}^{2} will enter the variance dynamics, but its impact on future ht+kh\_{t+k} depends on both the long-memory structure (through dd and the lag polynomials) and the frequency of such shocks. A single extreme return can thus be interpreted partly as a tail event in ztz\_{t} rather than as a permanent shift in the volatility regime.
2. 2.

   Persistent volatility regimes. At the same time, the fractional differencing parameter d∈(0,1)d\in(0,1) and the autoregressive structure in ([4](#S2.E4 "In 2.2 fiGARCH–GED model for log returns ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data")) allow hth\_{t} to exhibit long memory. When a sequence of large shocks occurs (for example, during a war, siege, or macroeconomic crisis), the fiGARCH recursion will propagate elevated εt2\varepsilon\_{t}^{2} forward, generating a persistent high-volatility regime. In this case, the GED tails and the long-memory variance dynamics work together: the GED captures the excess kurtosis within the regime, while fiGARCH ensures that the regime itself is persistent.

#### 2.2.2 Conditional distribution of log prices and central 50% spread

The one-step-ahead conditional log price is

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt+1=xt+rt+1.x\_{t+1}=x\_{t}+r\_{t+1}. |  | (11) |

Given ℱt\mathcal{F}\_{t}, its conditional distribution is

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt+1∣ℱt∼mt+1+ht+1​zt+1,mt+1=xt+μ,x\_{t+1}\mid\mathcal{F}\_{t}\sim m\_{t+1}+\sqrt{h\_{t+1}}\,z\_{t+1},\qquad m\_{t+1}=x\_{t}+\mu, |  | (12) |

with zt+1z\_{t+1} distributed as in Section [2.2.1](#S2.SS2.SSS1 "2.2.1 Generalized error distribution and tail behavior ‣ 2.2 fiGARCH–GED model for log returns ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").

Let Fν−1​(⋅)F\_{\nu}^{-1}(\cdot) denote the quantile function of the standardized GED. For any probability level p∈(0,1)p\in(0,1), the conditional pp-quantile of xt+1x\_{t+1} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | qp,t+1=mt+1+ht+1​ap​(ν),ap​(ν)=Fν−1​(p).q\_{p,t+1}=m\_{t+1}+\sqrt{h\_{t+1}}\,a\_{p}(\nu),\qquad a\_{p}(\nu)=F\_{\nu}^{-1}(p). |  | (13) |

We are particularly interested in the central 50% interval, defined by the 25th and 75th percentiles of the conditional log-price distribution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | q0.25,t+1=mt+1+ht+1​a0.25​(ν),q0.75,t+1=mt+1+ht+1​a0.75​(ν).q\_{0.25,t+1}=m\_{t+1}+\sqrt{h\_{t+1}}\,a\_{0.25}(\nu),\qquad q\_{0.75,t+1}=m\_{t+1}+\sqrt{h\_{t+1}}\,a\_{0.75}(\nu). |  | (14) |

Equivalently, these satisfy the probability-mass conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(xt+1≤q0.25,t+1∣ℱt)=0.25,ℙ​(xt+1≤q0.75,t+1∣ℱt)=0.75.\mathbb{P}\bigl(x\_{t+1}\leq q\_{0.25,t+1}\mid\mathcal{F}\_{t}\bigr)=0.25,\qquad\mathbb{P}\bigl(x\_{t+1}\leq q\_{0.75,t+1}\mid\mathcal{F}\_{t}\bigr)=0.75. |  | (15) |

They can be viewed as central-interval analogues of the tail integrals used in expected shortfall (Acerbi and Tasche, [2002](#bib.bib34 "On the coherence of expected shortfall")) calculations: the math is identical but instead of integrating probability mass in the tails, we delimit the central 50% of the conditional distribution.

Mapping these quantiles back to the price level gives the model-based low and high candidates,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt+1∗=exp⁡(q0.25,t+1),Ht+1∗=exp⁡(q0.75,t+1).L^{\*}\_{t+1}=\exp\bigl(q\_{0.25,t+1}\bigr),\qquad H^{\*}\_{t+1}=\exp\bigl(q\_{0.75,t+1}\bigr). |  | (16) |

The distance between these quantiles,

|  |  |  |  |
| --- | --- | --- | --- |
|  | q0.75,t+1−q0.25,t+1=ht+1​[a0.75​(ν)−a0.25​(ν)],q\_{0.75,t+1}-q\_{0.25,t+1}=\sqrt{h\_{t+1}}\bigl[a\_{0.75}(\nu)-a\_{0.25}(\nu)\bigr], |  | (17) |

is increasing in both ht+1\sqrt{h\_{t+1}} and the tail thickness implied by ν\nu (since the GED quantiles move outward as the distribution becomes more heavy-tailed).

#### 2.2.3 Definition of open, high, low and close

For each period t+1t+1, we construct OHLC prices as follows.

##### Close.

The close is taken to be the realized end-of-period price index from the partially imputed price survey system:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct+1=Pt+1=exp⁡(xt+1obs),C\_{t+1}=P\_{t+1}=\exp(x\_{t+1}^{\text{obs}}), |  | (18) |

where xt+1obsx\_{t+1}^{\text{obs}} is the end-of-month log price.

##### Open.

The open is set equal to the conditional expectation of the log price, mapped back to levels:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ot+1=exp⁡(𝔼​[xt+1∣ℱt])=exp⁡(mt+1).O\_{t+1}=\exp\bigl(\mathbb{E}[x\_{t+1}\mid\mathcal{F}\_{t}]\bigr)=\exp(m\_{t+1}). |  | (19) |

##### Model-based low and high.

Using the conditional quantiles defined above, we obtain the central 50% price interval:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt+1∗=exp⁡(mt+1+ht+1​a0.25​(ν)),Ht+1∗=exp⁡(mt+1+ht+1​a0.75​(ν)).L^{\*}\_{t+1}=\exp\bigl(m\_{t+1}+\sqrt{h\_{t+1}}\,a\_{0.25}(\nu)\bigr),\qquad H^{\*}\_{t+1}=\exp\bigl(m\_{t+1}+\sqrt{h\_{t+1}}\,a\_{0.75}(\nu)\bigr). |  | (20) |

##### Final high and low.

To ensure that the realized open and close lie within the range, and that the range always spans the most relevant parts of the modeled distribution, the final high and low are defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ht+1=max⁡{Ot+1,Ct+1,Ht+1∗},Lt+1=min⁡{Ot+1,Ct+1,Lt+1∗}.H\_{t+1}=\max\{\,O\_{t+1},\,C\_{t+1},\,H^{\*}\_{t+1}\,\},\qquad L\_{t+1}=\min\{\,O\_{t+1},\,C\_{t+1},\,L^{\*}\_{t+1}\,\}. |  | (21) |

This construction guarantees that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt+1≤min⁡{Ot+1,Ct+1}andHt+1≥max⁡{Ot+1,Ct+1},L\_{t+1}\leq\min\{O\_{t+1},C\_{t+1}\}\quad\text{and}\quad H\_{t+1}\geq\max\{O\_{t+1},C\_{t+1}\}, |  | (22) |

and that, absent extreme realizations of Ct+1C\_{t+1}, the interval [Lt+1,Ht+1][L\_{t+1},H\_{t+1}] is anchored around the central 50% of the conditional price distribution implied by the fiGARCH–GED model.

## 3 Methods

Range-based volatility estimators exploit the information contained in intra-period price extremes. Under standard diffusion models, these estimators achieve substantial efficiency gains relative to close-to-close measures, sometimes by an order of magnitude (Parkinson, [1980](#bib.bib9 "The extreme value method for estimating the variance of the rate of return"); Garman and Klass, [1980](#bib.bib10 "On the estimation of security price volatilities from historical data"); Yang and Zhang, [2000](#bib.bib12 "Drift-independent volatility estimation based on high, low, open, and close prices")). This section presents the volatility estimators, describes their relationship to the OHLC data structure, and specifies the procedure used to identify elevated volatility episodes in the empirical application.

### 3.1 Setup and notation

We observe prices at equally spaced times (t=0,1,2,…)(t=0,1,2,\dots). For each observation period (t)(t) we denote:

* •

  OtO\_{t}: opening price
* •

  HtH\_{t}: highest price during the period
* •

  LtL\_{t}: lowest price during the period
* •

  CtC\_{t}: closing price

We work with natural logarithms of price ratios. For brevity, define:

* •

  Log range: dt=ln⁡(Ht/Lt)d\_{t}=\ln(H\_{t}/L\_{t})
* •

  Log open-close return: ct=ln⁡(Ct/Ot)c\_{t}=\ln(C\_{t}/O\_{t})
* •

  “Overnight” log return (close-to-open between periods): ot=ln⁡(Ot/Ct−1)o\_{t}=\ln(O\_{t}/C\_{t-1})

As a continuous-time benchmark we assume that the efficient price follows a geometric Brownian motion,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Pt=μ​Pt​d​t+σ​Pt​d​Wt,dP\_{t}=\mu P\_{t}\,dt+\sigma P\_{t}\,dW\_{t}, |  | (23) |

so that log prices satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ln⁡Pt=(μ−12​σ2)​d​t+σ​d​Wt.d\ln P\_{t}=\left(\mu-\tfrac{1}{2}\sigma^{2}\right)dt+\sigma dW\_{t}. |  | (24) |

Let Δ​t\Delta t be the length of one observation period in years (e.g., Δ​t=1/252\Delta t=1/252 for daily data, Δ​t=1/12\Delta t=1/12 for monthly data). Then σ2​Δ​t\sigma^{2}\Delta t is the per-period variance parameter. The estimators below aim to estimate this per-period variance and then annualize it by multiplying by an annualization factor N≈1/Δ​tN\approx 1/\Delta t and taking a square root.

All estimators are computed over rolling windows of length nn periods. For a generic per-period variance estimator v^t\hat{v}\_{t} over a window ending at time tt, the corresponding annualized volatility is

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ^t=N​v^t.\hat{\sigma}\_{t}=\sqrt{N\,\hat{v}\_{t}}. |  | (25) |

### 3.2 Volatility Estimators

The following definitions present the volatility estimators used in this paper. All estimators follow the same pattern: a per-period variance component is estimated from the OHLC data over a rolling window, annualized by multiplying by an annualization factor NN, and converted to volatility by taking a square root.

###### Definition 1 (Close-to-close volatility).

The close-to-close estimator uses only closing prices and treats the returns as arithmetic rates of change,

|  |  |  |
| --- | --- | --- |
|  | rt=Ct−Ct−1Ct−1.r\_{t}=\frac{C\_{t}-C\_{t-1}}{C\_{t-1}}. |  |

Given a window of mm returns {ri}i=t−m+1t\{r\_{i}\}\_{i=t-m+1}^{t}, the sample variance is

|  |  |  |
| --- | --- | --- |
|  | Var^​(r)t=1m−1​∑i=t−m+1t(ri−r¯t)2,r¯t=1m​∑i=t−m+1tri.\widehat{\operatorname{Var}}(r)\_{t}=\frac{1}{m-1}\sum\_{i=t-m+1}^{t}\bigl(r\_{i}-\bar{r}\_{t}\bigr)^{2},\qquad\bar{r}\_{t}=\frac{1}{m}\sum\_{i=t-m+1}^{t}r\_{i}. |  |

The annualized close-to-close volatility is then

|  |  |  |
| --- | --- | --- |
|  | σ^CC,t=N​Var^​(r)t.\hat{\sigma}\_{\mathrm{CC},t}=\sqrt{N\,\widehat{\operatorname{Var}}(r)\_{t}}. |  |

In the implementation we use m=n−1m=n-1 returns corresponding to nn prices. For small period-to-period changes, arithmetic returns and log returns are numerically very close; all range-based estimators below use log price ratios exactly.

###### Definition 2 (Parkinson high-low estimator).

Parkinson’s estimator uses only the high and low within each period. For each tt, define the log range dt=ln⁡(Ht/Lt)d\_{t}=\ln(H\_{t}/L\_{t}). Under the geometric Brownian motion model with zero drift over the period and continuous trading, the log range satisfies the moment condition

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[dt2]=4​ln⁡2​σ2​Δ​t.\mathbb{E}\bigl[d\_{t}^{2}\bigr]=4\ln 2\,\sigma^{2}\Delta t. |  |

A method-of-moments estimator of the per-period variance based on this identity is

|  |  |  |
| --- | --- | --- |
|  | v^P,t=14​n​ln⁡2​∑i=t−n+1tdi2,\hat{v}\_{P,t}=\frac{1}{4n\ln 2}\sum\_{i=t-n+1}^{t}d\_{i}^{2}, |  |

and the corresponding annualized Parkinson volatility is σ^P,t=N​v^P,t\hat{\sigma}\_{P,t}=\sqrt{N\,\hat{v}\_{P,t}}.
This estimator is substantially more efficient than close-to-close when the zero-drift, continuous-trading assumptions are reasonable, but it can become biased in strongly trending markets.

###### Definition 3 (Garman-Klass estimator).

Garman and Klass ([1980](#bib.bib10 "On the estimation of security price volatilities from historical data")) derive an estimator that uses the range and the open-close return. Using dt=ln⁡(Ht/Lt)d\_{t}=\ln(H\_{t}/L\_{t}) and ct=ln⁡(Ct/Ot)c\_{t}=\ln(C\_{t}/O\_{t}), their per-period variance estimator can be written as

|  |  |  |
| --- | --- | --- |
|  | v^G​K,t=1n​∑i=t−n+1t(12​di2−(2​ln⁡2−1)​ci2).\hat{v}\_{GK,t}=\frac{1}{n}\sum\_{i=t-n+1}^{t}\left(\frac{1}{2}d\_{i}^{2}-(2\ln 2-1)\,c\_{i}^{2}\right). |  |

Under geometric Brownian motion with zero drift within each period, this is an unbiased estimator of the per-period variance σ2​Δ​t\sigma^{2}\Delta t, and is more efficient than both close-to-close and Parkinson’s range estimator. The corresponding annualized volatility is σ^G​K,t=N​v^G​K,t\hat{\sigma}\_{GK,t}=\sqrt{N\,\hat{v}\_{GK,t}}.

###### Definition 4 (Rogers-Satchell estimator).

Rogers and Satchell ([1991](#bib.bib11 "Estimating variance from high, low and closing prices")) propose an estimator that remains unbiased for variance even in the presence of non-zero drift. Let ut=ln⁡(Ht/Ot)u\_{t}=\ln(H\_{t}/O\_{t}), ℓt=ln⁡(Lt/Ot)\ell\_{t}=\ln(L\_{t}/O\_{t}), and ct=ln⁡(Ct/Ot)c\_{t}=\ln(C\_{t}/O\_{t}). One convenient equivalent form of the Rogers-Satchell contribution for period tt is

|  |  |  |
| --- | --- | --- |
|  | qt=ln⁡(HtCt)​ln⁡(HtOt)+ln⁡(LtCt)​ln⁡(LtOt).q\_{t}=\ln\left(\frac{H\_{t}}{C\_{t}}\right)\ln\left(\frac{H\_{t}}{O\_{t}}\right)+\ln\left(\frac{L\_{t}}{C\_{t}}\right)\ln\left(\frac{L\_{t}}{O\_{t}}\right). |  |

The per-period variance estimator over a window is v^R​S,t=1n​∑i=t−n+1tqi\hat{v}\_{RS,t}=\frac{1}{n}\sum\_{i=t-n+1}^{t}q\_{i}, and the annualized Rogers-Satchell volatility is σ^R​S,t=N​v^R​S,t\hat{\sigma}\_{RS,t}=\sqrt{N\,\hat{v}\_{RS,t}}.
Under the geometric Brownian motion model with arbitrary constant drift μ\mu, this estimator is unbiased for σ2​Δ​t\sigma^{2}\Delta t, making it more robust than Garman-Klass when there are strong trends.

###### Definition 5 (Garman-Klass-Yang-Zhang extension).

The Garman-Klass-Yang-Zhang (“GK-YZ”) extension (Yang and Zhang, [2000](#bib.bib12 "Drift-independent volatility estimation based on high, low, open, and close prices")) augments the Garman-Klass estimator by incorporating squared close-to-open jumps between periods. Define the “overnight” log return ot=ln⁡(Ot/Ct−1)o\_{t}=\ln(O\_{t}/C\_{t-1}), and retain dtd\_{t} and ctc\_{t} as before. The GK-YZ per-period variance estimator over a window is

|  |  |  |
| --- | --- | --- |
|  | v^G​K​Y​Z,t=1n​∑i=t−n+1t[oi2+12​di2−(2​ln⁡2−1)​ci2],\hat{v}\_{GKYZ,t}=\frac{1}{n}\sum\_{i=t-n+1}^{t}\left[o\_{i}^{2}+\frac{1}{2}d\_{i}^{2}-(2\ln 2-1)\,c\_{i}^{2}\right], |  |

with annualized volatility σ^G​K​Y​Z,t=N​v^G​K​Y​Z,t\hat{\sigma}\_{GKYZ,t}=\sqrt{N\,\hat{v}\_{GKYZ,t}}.
When between-period jumps (e.g., market closes and reopens) are important, this estimator captures both those jumps and within-period variation.

###### Definition 6 (Yang-Zhang estimator).

Yang and Zhang ([2000](#bib.bib12 "Drift-independent volatility estimation based on high, low, open, and close prices")) propose a volatility estimator that combines three components: (i) the variance of close-to-open returns oto\_{t}, (ii) the variance of open-close returns ctc\_{t}, and (iii) the intraday Rogers-Satchell variance.
The close-to-open and open-close components are computed as sample variances over the last nn periods:

|  |  |  |
| --- | --- | --- |
|  | v^o,t=Var^​(oi)i=t−n+1t,v^c,t=Var^​(ci)i=t−n+1t.\hat{v}\_{o,t}=\widehat{\operatorname{Var}}(o\_{i})\_{i=t-n+1}^{t},\qquad\hat{v}\_{c,t}=\widehat{\operatorname{Var}}(c\_{i})\_{i=t-n+1}^{t}. |  |

The Rogers-Satchell component v^R​S,t\hat{v}\_{RS,t} is as defined above. The Yang-Zhang per-period variance estimator is a weighted sum,

|  |  |  |
| --- | --- | --- |
|  | v^Y​Z,t=v^o,t+k​v^c,t+(1−k)​v^R​S,t,\hat{v}\_{YZ,t}=\hat{v}\_{o,t}+k\,\hat{v}\_{c,t}+(1-k)\,\hat{v}\_{RS,t}, |  |

with weight k∈(0,1)k\in(0,1) chosen to balance the contributions of the open-close and Rogers-Satchell components. In the implementation we use

|  |  |  |
| --- | --- | --- |
|  | k=α−1α+n+1n−1,k=\frac{\alpha-1}{\alpha+\frac{n+1}{n-1}}, |  |

with α≈1.34\alpha\approx 1.34. The annualized Yang-Zhang volatility is σ^Y​Z,t=N​v^Y​Z,t\hat{\sigma}\_{YZ,t}=\sqrt{N\,\hat{v}\_{YZ,t}}.
The Yang-Zhang estimator is designed to be drift-independent (through the use of the Rogers-Satchell intraday component) and to incorporate between-period jumps efficiently. In empirical applications it typically exhibits lower variance than simpler historical and range-based estimators (Yang and Zhang, [2000](#bib.bib12 "Drift-independent volatility estimation based on high, low, open, and close prices")).

### 3.3 Relationship to the OHLC data structure

Given the constructed OHLC series {Ot,Ht,Lt,Ct}\{O\_{t},H\_{t},L\_{t},C\_{t}\} described in Section [2.1](#S2.SS1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"), the range-based estimators can be interpreted as functions of the modeled conditional distribution over rolling windows. For each period tt, the key logarithmic components—dt=ln⁡(Ht/Lt)d\_{t}=\ln(H\_{t}/L\_{t}), ct=ln⁡(Ct/Ot)c\_{t}=\ln(C\_{t}/O\_{t}), and ot=ln⁡(Ot/Ct−1)o\_{t}=\ln(O\_{t}/C\_{t-1})—summarize, in different ways, the conditional spread and location of the modeled price distribution within each period.

Under the fiGARCH–GED specification, these quantities inherit structure from the underlying volatility process. Over a window of length nn, the range-based estimators use averages of functions of {di,ci,oi}i=t−n+1t\{d\_{i},c\_{i},o\_{i}\}\_{i=t-n+1}^{t} to estimate per-period variance, which is then annualized. For example, the Parkinson estimator uses the average of di2d\_{i}^{2}, while Garman–Klass and Rogers–Satchell combine di2d\_{i}^{2} with ci2c\_{i}^{2} and other log differences. In our setting, these estimators summarize how the modeled conditional distribution (through hth\_{t} and the GED quantiles) evolves over time, with the OHLC mapping providing a coherent bridge between the latent volatility process and observable price indices.

A key property of this setup is that the range-based estimators remain well-defined and informative even though the OHLC series are model-based rather than directly observed. The theoretical efficiency gains of range-based estimators derive from their use of within-period price extremes to reduce variance in volatility estimation. In the RTP framework, these extremes are constructed from the conditional distribution implied by the fiGARCH–GED model, which captures both the level of conditional variance (hth\_{t}) and the tail behavior of innovations (through the GED shape parameter ν\nu). The resulting high and low prices thus encode information about within-period dispersion that is consistent with the underlying volatility dynamics.

It is instructive to consider limiting cases in which the additional information in the range becomes negligible and range-based estimators effectively collapse to standard close-to-close volatility measures. These cases clarify the conditions under which the range-based approach provides meaningful incremental information.

1. 1.

   Vanishing conditional variance. If ht→0h\_{t}\to 0 for all tt (for example, in a hypothetical perfectly stable market), then q0.25,t+1≈q0.75,t+1≈mt+1q\_{0.25,t+1}\approx q\_{0.75,t+1}\approx m\_{t+1}, so that Lt+1∗≈Ht+1∗≈exp⁡(mt+1)L^{\*}\_{t+1}\approx H^{\*}\_{t+1}\approx\exp(m\_{t+1}). In the absence of large deviations of Ct+1C\_{t+1} from its expectation, we obtain Ht+1≈Lt+1≈Ot+1≈Ct+1H\_{t+1}\approx L\_{t+1}\approx O\_{t+1}\approx C\_{t+1} and thus dt=ln⁡(Ht/Lt)≈0d\_{t}=\ln(H\_{t}/L\_{t})\approx 0 for all tt. In this limit, range-based estimators contribute little beyond the information in the close-to-close returns rtr\_{t}.
2. 2.

   Open and close dominate the range. Even when hth\_{t} is not negligible, if the realized close CtC\_{t} and the conditional open OtO\_{t} lie well inside the modeled central interval, then HtH\_{t} and LtL\_{t} will typically be close to Ht∗H^{\*}\_{t} and Lt∗L^{\*}\_{t}. Conversely, if CtC\_{t} and OtO\_{t} coincide or nearly coincide (for example, in periods with very small net movement), the max/min definitions may again yield Ht≈LtH\_{t}\approx L\_{t}, shrinking dtd\_{t}. In this case, range-based estimators become numerically similar to close-to-close estimators computed from rtr\_{t} and ctc\_{t}.
3. 3.

   Degenerate OHLC construction. As an extreme thought experiment, if we were to set Ht=Lt=CtH\_{t}=L\_{t}=C\_{t} for all tt, then dt=ln⁡(Ht/Lt)=0d\_{t}=\ln(H\_{t}/L\_{t})=0 identically, and all range-based estimators reduce to functions of close-to-close (or open–close) returns alone. They no longer encode any within-period dispersion.

In practice, the fractionally integrated GARCH model with GED innovations routinely generates nontrivial conditional variance hth\_{t} in crisis-prone environments, and the OHLC mapping preserves a meaningful spread between LtL\_{t} and HtH\_{t}. In these settings, range-based volatility estimators exploit the additional information contained in the model-implied highs and lows. This yields more efficient volatility measurement than close-to-close alternatives, while remaining straightforward to compute in an operational workflow. The empirical results in Section [4](#S4 "4 Results ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") confirm that the range-based estimators produce meaningfully different signals than close-to-close measures, consistent with the OHLC structure encoding substantive within-period dispersion information.

### 3.4 Detection rule and operational implementation

In our empirical application, all volatility estimators are computed with a rolling window of length n=10n=10, and annualization assumes Δ​t=1/12\Delta t=1/12, so that N=12N=12 in all results. For operational use we employ a simple volatility shock indicator based on two threshold conditions:

1. 1.

   Relative threshold: volatility above its 12-month simple moving average,
2. 2.

   Tail threshold: volatility above a high percentile (the 85th percentile) of its historical distribution computed over the full sample, and not below a low percentile (the 20th percentile).

Months satisfying both conditions are flagged as volatility episodes.

The percentile thresholds are not highly sensitive parameters: the relative-threshold condition (above the 12-month moving average) does most of the work in identifying departures from recent baseline conditions, while the percentile bounds serve primarily as guardrails. The upper bound ensures that episodes remain flagged during elevated dispersion even as volatility recedes from its peak, avoiding false negatives during highly disrupted periods. The lower bound prevents the indicator from triggering during sustained low-volatility regimes, where minor upticks may exceed the moving average without representing meaningful stress. Using sample-wide percentiles also allows the early part of the series (including the 2007–08 global food price crisis, which falls within the initial rolling window) to be evaluated against a consistent historical benchmark. Varying the percentile thresholds within reasonable ranges (e.g., 80th–90th for the upper bound, 15th–25th for the lower bound) does not materially alter the set of flagged episodes in the applications presented below.

This rule is simple, transparent, and easy to implement in operational dashboards alongside existing indicators such as RSI and MACD (Appel, [1979](#bib.bib6 "The moving average convergence-divergence trading method"); Wilder, [1978](#bib.bib8 "New concepts in technical trading systems")). The percentile thresholds provide straightforward calibration parameters that can be tuned against historical event data. The rule is intentionally minimal: even with default settings, volatility flags episodes that momentum indicators miss.

## 4 Results

This section presents five case studies that assess OHLC-based volatility estimators against documented shocks in remote, data-scarce settings spanning Sub-Saharan Africa, the Middle East, the Caribbean, and Southeast Asia. The applications cover diverse shock types (conflict, natural hazards, policy change, global transmission) and market structures (landlocked versus coastal, import-dependent versus producer). In each case, the RTP food price index is used and flagged volatility episodes are interpreted against event timelines compiled from the literature (Appendix). Applications are presented alphabetically.

### 4.1 Al Fashir, Sudan (2007–2025)

Sudan is a demanding test case because global shocks, macroeconomic instability, and recurrent conflict overlap over long horizons, with severe impacts in Darfur. We focus on Al Fashir, the capital of North Darfur and a regional trading hub surrounded by major IDP camps including Zamzam, Abu Shouk, and Al Salam. Figure [1](#S4.F1 "Figure 1 ‣ 4.1 Al Fashir, Sudan (2007–2025) ‣ 4 Results ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") shows the six volatility estimators computed from the local OHLC series; Appendix [A](#A1 "Appendix A Additional Figures ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") presents the same figure for the other cases.

All estimators detect the main stress periods but differ in smoothness and sensitivity to within-period dispersion. Range-based measures rise earlier and remain elevated when intra-month ranges widen persistently, whereas close-to-close volatility reacts sharply to month-end jumps but can understate stress when prices fluctuate without a clear directional move. The Yang–Zhang estimator offers a practical compromise, tracking the more responsive range-based metrics while reducing noise from drift and opening-price discontinuities: it incorporates the drift-independent Rogers–Satchell component and weights the open-close and overnight components to balance responsiveness against variance. We therefore use Yang–Zhang volatility, σ^Y​Z,t\hat{\sigma}\_{YZ,t}, as the primary measure below. Figure [2](#S4.F2 "Figure 2 ‣ 4.1 Al Fashir, Sudan (2007–2025) ‣ 4 Results ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") shows the main result; the event timeline is in Appendix [B](#A2 "Appendix B Supplementary Materials: Sudan Case Study (Al Fashir) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").

The bottom panel plots σ^Y​Z,t\hat{\sigma}\_{YZ,t} and its 12-month moving average; red segments mark elevated volatility. The signals align with major disruptions, including the 2007–08 global food price crisis, the post-2011 adjustment period, the 2018–2019 bread-protests and political transition, the 2021 coup, and the SAF–RSF war from April 2023. RSI remains elevated for much of the period, consistent with chronic inflation, but does not isolate acute stress and even declines during severe disruptions. Volatility, by contrast, consistently flags conflict escalation, policy shocks, and market fragmentation. The divergence is most pronounced after April 2023, when RSI moderates while volatility signals sharp deterioration. Al Fashir illustrates how dispersion-based monitoring complements price-level indicators by separating persistent inflation from episodic market dysfunction.

![Refer to caption](2603.02898v1/SDN_plot_all.png)


Figure 1: Open, High, Low, Close food prices (index, log) in Al Fashir, Sudan, plotted on a candlestick chart together with six OHLC-based volatility metrics. In the candlestick chart (top panel), each bar represents one month: the vertical line spans the low to high, while the box spans open to close; filled (red) boxes indicate months where the close fell below the open, and hollow (green) boxes indicate months where the close exceeded the open. The dotted line shows the 12-month moving average, and the grey shading indicates Bollinger bands (two standard deviations around the moving average). Subsequent panels show close-to-close volatility and five range-based estimators (Parkinson, Garman–Klass, Rogers–Satchell, Garman–Klass–Yang–Zhang, and Yang–Zhang). All estimators identify the same broad stress periods but differ in smoothness: range-based measures respond more quickly to widening intra-period dispersion, while close-to-close volatility reacts only to month-end price jumps.

![Refer to caption](2603.02898v1/SDN_plot.png)


Figure 2: Technical setup to detect volatility shocks. Top: log food prices in Al Fashir, Sudan. Middle: RSI with 30 and 70 reference levels. Bottom: Yang–Zhang annualized volatility, its 12-month moving average, and detected high-volatility episodes (red segments).

### 4.2 Baidoa, Somalia (2007–2025)

Somalia provides a stringent test case because market conditions are repeatedly stressed by compound climate shocks, protracted insecurity, and episodic disruptions to trade and humanitarian access. We focus on Baidoa, the capital of South West State (Bay Region), a major agricultural market and relief hub highly exposed to rainfall variability and transport constraints. Figure [3](#S4.F3 "Figure 3 ‣ 4.2 Baidoa, Somalia (2007–2025) ‣ 4 Results ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") shows the result; the event timeline is provided in Appendix [C](#A3 "Appendix C Supplementary Materials: Somalia Case Study (Baidoa) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").

Volatility rises sharply during well-documented crisis windows, including the 2011 famine, renewed stress in 2014–2015 linked to poor seasonal performance and the 2016–2017 drought emergency. Later clusters coincide with COVID-19 disruptions and the concurrent desert locust upsurge in 2020, as well as the 2023–2024 Deyr and Gu flood episodes. RSI provides some signal during the 2011 crisis and the 2016–2017 drought, but remains within the 30–70 neutral band during several documented stress periods, including the 2020 compound disruption and the 2023–2024 floods, when volatility clearly flags elevated dispersion. Overall, Baidoa illustrates that volatility responds strongly during compound climate and insecurity episodes that fragment markets and disrupt supply.

![Refer to caption](2603.02898v1/SOM_plot.png)


Figure 3: Somalia (Baidoa): technical setup and detected stress episodes. Top panel: log food prices. Middle panel: RSI with 30 and 70 reference levels. Bottom panel: Yang–Zhang annualized volatility, its 12-month moving average, and detected high-volatility episodes (red segments).

### 4.3 Far North Region, Cameroon (2010–2025)

Cameroon’s Far North provides a useful test case because food markets are repeatedly exposed to overlapping security, climate, and policy shocks in a border-sensitive economy. The region lies at the intersection of trade corridors with Nigeria and Chad and has faced sustained disruption from insurgency spillovers, transport constraints, and recurrent floods that periodically impair market access. The setting is also sensitive to cross-border frictions and cost transmission, with a clear shift in volatility after 2022. Figure [4](#S4.F4 "Figure 4 ‣ 4.3 Far North Region, Cameroon (2010–2025) ‣ 4 Results ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") shows the result; the event timeline is provided in Appendix [D](#A4 "Appendix D Supplementary Materials: Cameroon Case Study (Far North) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").

The volatility signal shows multiple stress episodes consistent with insecurity, flood-related disruption, cross-border trade constraints, and cost shocks transmitted through transport and distribution margins. RSI remains within the 30–70 band for much of the period and does not register several salient disruptions, whereas volatility clearly flags episodes such as the 2017 floods and renewed attacks in 2018. After 2022 the series shifts into a higher-volatility regime driven by repeated sharp price spikes and reversals. These movements leave RSI relatively unresponsive—reflecting offsetting directional movements within the observation window—but are captured by sustained increases in dispersion and repeated flagged months. Overall, the Far North case illustrates that volatility captures both local fragmentation risks and externally driven cost transmission in a setting where logistics and border dynamics shape price formation.

![Refer to caption](2603.02898v1/CMR_plot.png)


Figure 4: Cameroon (Far North): technical setup and detected stress episodes. Top panel: log food prices. Middle panel: RSI with 30 and 70 reference levels. Bottom panel: Yang–Zhang annualized volatility, its 12-month moving average, and detected high-volatility episodes (red segments).

### 4.4 Port-au-Prince, Haiti (2007–2025)

Haiti provides a distinct test case in which volatility is driven by large, discrete disruptions in an urban, import-dependent market that concentrates political risk, infrastructure fragility, and insecurity. Port-au-Prince anchors national logistics and trade and has experienced repeated shocks that generate abrupt breaks in market functioning, including natural disasters, political disruption, fuel-access crises, and worsening security conditions. Figure [5](#S4.F5 "Figure 5 ‣ 4.4 Port-au-Prince, Haiti (2007–2025) ‣ 4 Results ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") shows the results; the event timeline is provided in Appendix [E](#A5 "Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").

![Refer to caption](2603.02898v1/HTI_plot.png)


Figure 5: Haiti (Port-au-Prince): technical setup and detected stress episodes. Top panel: log food prices. Middle panel: RSI with 30 and 70 reference levels. Bottom panel: Yang–Zhang annualized volatility, its 12-month moving average, and detected high-volatility episodes (red segments).

Volatility rises sharply around major disaster and political-disruption windows and remains elevated during later fuel and logistics shocks. The series shows strong volatility during the 2007–08 crisis and the 2010 earthquake, with renewed clusters during later disruption windows including the 2018 fuel riots, the extended *peyi lòk* period in 2019, and the 2022 fuel-access crisis associated with gang control of key infrastructure and transport corridors. Volatility remains elevated through the subsequent deterioration in security conditions. RSI and volatility sometimes co-move during price run-ups, but volatility more consistently captures disaster impacts and market dysfunction—notably the 2010 earthquake and the 2017 hurricane season—when RSI does not breach standard threshold levels.

### 4.5 Sulu, Philippines (2007–2025)

Figure [6](#S4.F6 "Figure 6 ‣ 4.5 Sulu, Philippines (2007–2025) ‣ 4 Results ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") shows the detection setup in the Philippines; the event timeline is provided in Appendix [F](#A6 "Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").

![Refer to caption](2603.02898v1/PHL_plot.png)


Figure 6: Philippines (Sulu): technical setup and detected stress episodes. Top panel: log food prices. Middle panel: RSI with 30 and 70 reference levels. Bottom panel: Yang–Zhang annualized volatility, its 12-month moving average, and detected high-volatility episodes (red segments).

The Philippines provides a complementary test of portability beyond settings defined by extremes. We focus on Sulu in the Zamboanga Peninsula, a relatively remote market shaped by localized insecurity and logistics frictions, and policy shifts affecting exposure to global staple-market conditions.

Flagged volatility segments highlight recurring stress episodes consistent with intermittent access and discontinuous price formation. In the early part of the series, the 2007–08 global food and fuel crisis does not appear as a dominant contiguous episode, suggesting muted transmission into observed dispersion relative to local dynamics. Instead, pre-2019 volatility clusters are more closely associated with domestic disruption and logistics stress, including episodes in the early-to-mid 2010s and again in 2015–2018.

A key policy discontinuity occurs in 2019 with the Rice Tariffication Law, which replaced quantitative import restrictions with a tariff-based regime and altered import incentives and price expectations. In the Sulu series this shift is not marked by a single defining spike, but it precedes a period in which externally driven disruptions become more apparent. The clearest example is COVID-19 in 2020, which coincides with the largest volatility spike in the sample, consistent with abrupt mobility and supply-chain disruption. RSI rises during the COVID-19 period but remains within the neutral band, whereas volatility clearly flags the episode as exceptional. The 2022 Russia–Ukraine shock does not register as a sharp standalone episode, although the post-2019 period exhibits more frequent clustering alongside sustained freight and inflation pressures that followed. While these labels remain ex post and partly judgment-based—especially when shocks overlap—the overall pattern supports the operational point that volatility remains informative even when policy change reshapes a market’s exposure to national and global conditions.

## 5 Discussion

### 5.1 Cross-country synthesis

Table [1](#S5.T1 "Table 1 ‣ 5.1 Cross-country synthesis ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") summarizes the main shock categories that coincide with flagged volatility episodes across the five applications. The mapping is necessarily approximate: event labels are used for ex post interpretation, and attribution depends on the granularity of available documentation and on analyst judgment when multiple drivers overlap. The objective is not to build a definitive classification, but to illustrate that the volatility workflow consistently highlights a broad and policy-relevant range of disruptions across diverse contexts.

Table 1: Summary of detected volatility episodes by shock type across five countries (based on flagged Yang–Zhang volatility segments in red).

| Shock type | Sudan | Somalia | Cameroon | Haiti | Philippines |
| --- | --- | --- | --- | --- | --- |
| Global food/fuel crisis (2007–08) | Yes | Yes | – | Yes | – |
| Global shock (2022 Ukraine) | – | – | Yes | – | – |
| Armed conflict / insecurity | Yes | Yes | Yes | Yes | Yes |
| Natural disaster (flood/drought) | – | Yes | Yes | Yes | Yes |
| Natural disaster (earthquake/volcano) | – | – | – | Yes | Yes |
| Policy shock (subsidy/trade/regime shift) | Yes | – | Yes | Yes | Yes |
| Political transition / crisis | Yes | – | – | Yes | – |
| COVID-19 | – | Yes | – | Yes | Yes |

Several patterns emerge. First, volatility responds to global-to-local transmission when the shock is large and the market is exposed. The 2007–08 food and fuel crisis appears as a distinct volatility episode in Sudan, Somalia, and Haiti, consistent with uneven pass-through of international costs into domestic staple prices in import- and fuel-exposed systems (Food and Agriculture Organization of the United Nations, [2009](#bib.bib41 "The food price crisis of 2007/2008: evidence and implications for food security"); High Level Panel of Experts on Food Security and Nutrition, [2011](#bib.bib44 "Price volatility and food security"); Gilbert, [2010](#bib.bib43 "How to understand high food prices")). By contrast, the 2022 Russia–Ukraine shock is most clearly detected in Cameroon in the plotted series, suggesting stronger transmission through energy and trade channels in that setting, while the other cases exhibit weaker or less distinct volatility responses at monthly frequency.

Second, locally generated disruptions are detected in ways that cannot be inferred from global benchmarks alone. Conflict and local insecurity coincide with flagged volatility episodes in all five settings, consistent with fragmentation of market access, higher corridor risk, and intermittency of supply. Natural hazards generate identifiable volatility regimes, including drought and flood stress (Somalia, Cameroon, Haiti, and the Philippines) and large discrete disruptions such as Haiti’s earthquake and the Philippines’ volcanic event. These patterns support volatility measures acting as a reduced-form indicator of impaired market integration and unstable price formation.

Third, the largest and most persistent volatility regimes tend to arise under compound stress, when multiple channels overlap or reinforce one another. Somalia’s famine period combines climatic stress with fragile access and market constraints. Sudan’s 2023–2025 episode reflects war-driven market dysfunction interacting with siege dynamics and macroeconomic instability. Haiti’s 2019–2024 period illustrates how repeated political disruption, fuel access constraints, and insecurity can jointly sustain elevated volatility in an urban import hub. In such settings, volatility serves as a compact summary measure of cumulative market stress rather than a one-to-one proxy for a single event.

Finally, the cross-country cases clarify why dispersion-based monitoring can complement momentum-type indicators. RSI and related measures primarily respond to persistent directional movements, whereas volatility rises under both price surges and abrupt reversals, including episodes dominated by intermittency and access constraints rather than smooth trend inflation. Conceptually, this parallels microstructure settings in which frictions and widening spreads distort price discovery and increase short-horizon dispersion even when long-run price-level adjustment is ambiguous (Hasbrouck, [2002](#bib.bib36 "Stalking the “efficient price” in market microstructure specifications: an overview"); Corwin and Schultz, [2012](#bib.bib39 "A simple way to estimate bid-ask spreads from daily high and low prices")). Across the five cases, volatility flags a meaningful share of documented stress episodes during which RSI remains within neutral bounds (30–70), including the 2020 COVID-19 disruption in Sulu, the 2023–2024 floods in Somalia, and the post-2022 cost-transmission regime in Cameroon’s Far North.

### 5.2 Implications for market monitoring

The cross-country results highlight several advantages of incorporating volatility measures into market monitoring systems. First, volatility is symmetrically sensitive to shocks. Unlike trend-based indicators such as inflation, RSI, or MACD (Appel, [1979](#bib.bib6 "The moving average convergence-divergence trading method"); Wilder, [1978](#bib.bib8 "New concepts in technical trading systems")), which primarily flag persistent directional movements, volatility responds to both price increases and decreases. This feature is particularly valuable in environments where supply and demand disruptions partially offset each other, for example when insecurity reduces production and market access while also compressing purchasing power, or when aid inflows temporarily suppress prices before sharp increases re-emerge as supplies tighten.

Second, volatility provides a compact summary of market stress. By condensing the joint effects of macro instability, policy changes, and local disruptions into a single scalar indicator, it offers a practical signal for dashboards and routine surveillance. In operational settings, classifying volatility relative to its historical distribution can support rapid triage of abnormal conditions and can complement other signals such as price levels, exchange rate movements, or conflict and weather information. Conceptually, sustained increases in dispersion are also consistent with a shift toward weaker market liquidity and higher trading frictions, in the sense that prices adjust more discontinuously when transaction costs rise and market participation becomes constrained (Adrian et al., [2017](#bib.bib42 "Market liquidity after the financial crisis"); Schwarz, [2018](#bib.bib37 "Mind the gap: disentangling credit and liquidity in risk spreads")).

Third, the estimators are computationally simple and stable. Range-based measures can be computed directly once a period’s OHLC values are observed, without the repeated re-estimation required by GARCH-type models and without backward revisions to previously reported volatility series. This stability makes them well-suited for automated monitoring, pre-defined alert thresholds, and consistent reporting across markets and time.

Fourth, the approach generalizes across contexts. The five case studies span different regions, income levels, market structures, and shock types, yet the volatility measures produce consistent signals of elevated stress around documented events. This pattern suggests that the estimators capture fundamental properties of market dysfunction under stress, rather than reflecting context-specific features of a single country or commodity.

### 5.3 Limitations

Several limitations warrant emphasis. First, the RTP OHLC series are model-based rather than directly observed. While the fiGARCH–GED framework is designed to capture realistic within-period dynamics (Baillie et al., [1996](#bib.bib13 "Fractionally integrated generalized autoregressive conditional heteroskedasticity"); Andrée, [2021](#bib.bib4 "Estimating food price inflation from partial surveys"); Andrée and Pape, [2023](#bib.bib5 "Machine learning imputation of high frequency price surveys in papua new guinea")), the quality of volatility estimates ultimately depends on the underlying model, the coverage and reliability of input data, and the imputation process. Section [3.3](#S3.SS3 "3.3 Relationship to the OHLC data structure ‣ 3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") shows that range-based estimators remain informative as long as the OHLC structure encodes meaningful within-period dispersion; when this structure collapses (e.g., when conditional variance vanishes or when high and low prices converge to the close), the estimators reduce to close-to-close measures and the incremental information from ranges disappears. The empirical results indicate that this collapse does not occur in the settings examined, but direct validation of the synthetic OHLC series against observed intra-period data, where available, would further strengthen confidence in the approach.

Second, the detection rule relies on a simple threshold defined relative to the historical distribution and recent moving averages. More adaptive approaches, including time-varying thresholds, supervised classifiers, or integration with additional covariates, may improve precision and reduce false alarms. The advantage of the current rule is transparency and ease of implementation in operational systems.

Third, volatility remains a reduced-form indicator. While the case studies show close alignment with documented shocks, elevated volatility does not identify causal mechanisms, and similar signatures may arise from different sources such as insecurity, climate shocks, macroeconomic instability, or policy interventions. Combining volatility with structural models or complementary covariates could help distinguish mechanisms and quantify the incremental contribution of volatility beyond mean price changes.

Fourth, the analysis focuses on market-level outcomes and does not trace transmission to household welfare. The literature documents strong links between food prices, nutrition, poverty, and social stability (Bellemare, [2015](#bib.bib1 "Rising food prices, food price volatility, and social unrest"); Headey and Ruel, [2023](#bib.bib19 "Food inflation and child undernutrition in low and middle income countries"); Amolegbe et al., [2021](#bib.bib2 "Food price volatility and household food security: evidence from nigeria")), but the welfare consequences of volatility specifically remain less well characterized. Linking volatility indicators to household microdata and outcome measures remains an important direction for future work, particularly for calibrating thresholds used in operational triggers.

Finally, while the five case studies provide diverse illustration, broader evaluation across the full set of markets covered by RTP would allow more systematic assessment of detection accuracy, false positive rates, and the conditions under which volatility indicators perform best. Such evaluation would benefit from integration with independent event datasets and monitoring frameworks used in practice.

## 6 Conclusion

This paper demonstrates that range-based volatility estimators from financial econometrics can be productively applied to monitor market stress across diverse development contexts. Using OHLC price data from the World Bank’s Real-Time Prices system, we show that the Yang–Zhang volatility estimator consistently captures responses to documented shocks—including global commodity crises, armed conflict, natural disasters, and policy changes—across five country case studies spanning Sub-Saharan Africa, the Middle East, the Caribbean, and Southeast Asia.

The results highlight volatility as a complement to price-level monitoring. Traditional momentum indicators such as the RSI can produce muted or misleading signals during crises where supply and demand disruptions partially offset directional price movements. By contrast, volatility captures market dysfunction that manifests in widening intra-period price dispersion, abrupt reversals, and intermittent price formation rather than sustained trends, providing information that price levels alone cannot reveal.

Beyond food markets, the approach generalizes in principle to any setting where OHLC price series are available. In financial risk management, volatility indicators can support portfolio monitoring, hedging decisions, and stress detection in commodity-linked exposures. In trade and supply-chain analysis, elevated volatility can provide early signals of disruptions related to border frictions, logistics constraints, or policy uncertainty, especially when official statistics are delayed or insufficiently granular. In macroeconomic surveillance, exchange-rate and energy-price volatility can serve as compact indicators of broader instability. In humanitarian and development operations, volatility can complement price levels and momentum measures in early-warning systems and preparedness frameworks by helping distinguish inflationary pressure from market dislocation. Finally, volatility measures can support policy evaluation by providing a transparent metric to assess whether interventions such as subsidy reforms, trade liberalization, or price controls dampen or amplify market instability.

More broadly, the methodology illustrates how techniques developed for financial markets can be translated to operational monitoring. Range-based volatility estimators are computationally simple, require no model re-estimation, and yield stable historical series that can be deployed as automated alerts against pre-defined thresholds. As real-time data systems expand and automated analytics mature, compact and interpretable indicators like volatility can help convert high-frequency price information into actionable signals. When embedded in monitoring dashboards and linked to response protocols, such measures can support faster recognition of emerging market stress and more timely, targeted policy and operational responses.

### Data and Code Availability

The RTP-based price series used in this paper are available through the World Bank’s data portals and microdata library, subject to the usual terms of use. All estimators are implemented in R. Code and data to reproduce results and figures are archived on Zenodo at <https://doi.org/10.5281/zenodo.18846560>.

## References

* C. Acerbi and D. Tasche (2002)
  On the coherence of expected shortfall.
  Journal of Banking & Finance 26 (7),  pp. 1487–1503.
  External Links: [Document](https://dx.doi.org/10.1016/S0378-4266%2802%2900283-2)
  Cited by: [§2.2.2](#S2.SS2.SSS2.p3.3 "2.2.2 Conditional distribution of log prices and central 50% spread ‣ 2.2 fiGARCH–GED model for log returns ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* J. Adewopo, B. P. J. Andrée, H. Peter, G. Solano-Hermosilla, and F. Micale (2025)
  AI-imputed and crowdsourced price data show strong agreement with traditional price surveys in data-scarce environments.
  PLoS ONE 20 (4),  pp. e0320720.
  External Links: [Document](https://dx.doi.org/10.1371/journal.pone.0320720)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* T. Adrian, M. J. Fleming, O. Shachar, and E. Vogt (2017)
  Market liquidity after the financial crisis.
  Staff Report
  Technical Report 796, Federal Reserve Bank of New York.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§5.2](#S5.SS2.p2.1 "5.2 Implications for market monitoring ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* M. Amare, K. A. Abay, L. Tiberti, and J. Chamberlin (2020)
  COVID-19 and food security in Africa: building more resilient food systems.
  Open Research Africa.
  Cited by: [Table 6](#A4.T6.6.6.4.5.1.1 "In Appendix D Supplementary Materials: Cameroon Case Study (Far North) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* Amnesty International (2014)
  Sudan: those behind unlawful killings and torture of protesters must be brought to justice.
  Technical report
   Amnesty International.
  Note: 3 September 2014
  Cited by: [Table 2](#A2.T2.6.4.2.5.1.1 "In Appendix B Supplementary Materials: Sudan Case Study (Al Fashir) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* Amnesty International (2016)
  Scorched earth, poisoned air: sudanese government forces ravage jebel marra, darfur.
  Technical report
   Amnesty International.
  Cited by: [Table 2](#A2.T2.6.7.5.5.1.1 "In Appendix B Supplementary Materials: Sudan Case Study (Al Fashir) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* K. B. Amolegbe, J. Upton, E. Bageant, and S. Blom (2021)
  Food price volatility and household food security: evidence from nigeria.
  Food Policy 102,  pp. 102061.
  External Links: ISSN 0306-9192,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.foodpol.2021.102061),
  [Link](https://www.sciencedirect.com/science/article/pii/S0306919221000397)
  Cited by: [§5.3](#S5.SS3.p4.1 "5.3 Limitations ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* T. G. Andersen, T. Bollerslev, F. X. Diebold, and P. Labys (2003)
  Modeling and forecasting realized volatility.
  Econometrica 71 (2),  pp. 579–625.
  External Links: [Document](https://dx.doi.org/10.1111/1468-0262.00418)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* B. P. J. Andrée, A. F. Chamorro Elizondo, A. C. Kraay, P. G. Spencer, and D. Wang (2020)
  Predicting food crises.
  Policy Research Working Paper
  Technical Report 9412, The World Bank, Washington, DC.
  External Links: [Document](https://dx.doi.org/10.1596/1813-9450-9412)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* B. P. J. Andrée and U. J. Pape (2023)
  Machine learning imputation of high frequency price surveys in papua new guinea.
  Policy Research Working Paper
   World Bank.
  External Links: [Document](https://dx.doi.org/10.1596/1813-9450-10559)
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§5.3](#S5.SS3.p1.1 "5.3 Limitations ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* B. P. J. Andrée (2021)
  Estimating food price inflation from partial surveys.
  Policy Research Working Paper
   World Bank.
  External Links: [Document](https://dx.doi.org/10.1596/1813-9450-9886)
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§2.1](#S2.SS1.p2.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§5.3](#S5.SS3.p1.1 "5.3 Limitations ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* G. Appel (1979)
  The moving average convergence-divergence trading method.
   Scientific Investment Systems Incorporated, Great Neck, NY.
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§3.4](#S3.SS4.p3.1 "3.4 Detection rule and operational implementation ‣ 3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§5.2](#S5.SS2.p1.1 "5.2 Implications for market monitoring ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* G. Arabi et al. (2022)
  The impact of the Russia-Ukraine war on global food security.
  Global Food Security 33,  pp. 100632.
  External Links: [Document](https://dx.doi.org/10.1016/j.gfs.2022.100632)
  Cited by: [Table 4](#A3.T4.6.8.6.5.1.1 "In Appendix C Supplementary Materials: Somalia Case Study (Baidoa) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Table 6](#A4.T6.6.8.6.5.1.1 "In Appendix D Supplementary Materials: Cameroon Case Study (Far North) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* S. O. Aremu, A. Wende, J. Mahroza, and E. H. Rizerius (2023)
  Nigeria land border closure: implication on rice smuggling and local production.
  International Journal of Humanities Education and Social Sciences 2 (5).
  External Links: [Document](https://dx.doi.org/10.55227/ijhess.v2i5.387)
  Cited by: [Table 6](#A4.T6.6.5.3.5.1.1 "In Appendix D Supplementary Materials: Cameroon Case Study (Far North) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* D. Backer and T. Billing (2021)
  Validating famine early warning systems network projections of food security in africa, 2009–2020.
  Global Food Security 29,  pp. 100510.
  External Links: ISSN 2211-9124,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.gfs.2021.100510),
  [Link](https://www.sciencedirect.com/science/article/pii/S2211912421000201)
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* R. T. Baillie, T. Bollerslev, and H. O. Mikkelsen (1996)
  Fractionally integrated generalized autoregressive conditional heteroskedasticity.
  Journal of Econometrics 74 (1),  pp. 3–30.
  External Links: [Document](https://dx.doi.org/10.1016/S0304-4076%2895%2901749-6)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§2.1](#S2.SS1.p2.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§2.2](#S2.SS2.p3.2 "2.2 fiGARCH–GED model for log returns ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§5.3](#S5.SS3.p1.1 "5.3 Limitations ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* J. Bao, J. Pan, and J. Wang (2011)
  The illiquidity of corporate bonds.
  The Journal of Finance 66 (3),  pp. 911–946.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.2011.01655.x)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* M. A. Bari, M. K. Bin Kamal, M. O. Gani, G. D. Khan, M. A. Khuram, and S. H. Shams (2025)
  Exploring the impact of secession on food prices: a case study of Sudan.
  Agricultural and Food Economics 13 (1),  pp. 52.
  External Links: ISSN 2193-7532,
  [Document](https://dx.doi.org/10.1186/s40100-025-00398-y)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* C. B. Barrett (2010)
  Measuring food insecurity.
  Science 327 (5967),  pp. 825–828.
  External Links: [Document](https://dx.doi.org/10.1126/science.1182768)
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* M. F. Bellemare (2015)
  Rising food prices, food price volatility, and social unrest.
  American Journal of Agricultural Economics 97 (1),  pp. 1–21.
  External Links: [Document](https://dx.doi.org/10.1093/ajae/aau038)
  Cited by: [§5.3](#S5.SS3.p4.1 "5.3 Limitations ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* M. Ben Abdallah, E. Rebai, and A. Chebil (2021)
  Exploring the effect of food price volatility on food security in tunisia.
  Agriculture 11 (3),  pp. 263.
  External Links: [Document](https://dx.doi.org/10.3390/agriculture11030263)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* M. Bertetti, P. Agnolucci, A. Calzadilla, and L. Capra (2024)
  An independent evaluation of the famine early warning systems network food security projections.
  External Links: 2410.09384,
  [Document](https://dx.doi.org/10.48550/arXiv.2410.09384)
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* T. Bollerslev, R. Y. Chou, and K. F. Kroner (1992)
  ARCH modeling in finance: a review of the theory and empirical evidence.
  Journal of Econometrics 52 (1-2),  pp. 5–59.
  External Links: [Document](https://dx.doi.org/10.1016/0304-4076%2892%2990064-X)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* F. Checchi, A. Testa, A. Warsame, L. Quach, and R. Burns (2023)
  Drought, armed conflict and population mortality in Somalia, 2014–2018: a statistical analysis.
  PLOS Global Public Health 3 (4),  pp. e0001136.
  External Links: [Document](https://dx.doi.org/10.1371/journal.pgph.0001136)
  Cited by: [Table 4](#A3.T4.6.5.3.5.1.1 "In Appendix C Supplementary Materials: Somalia Case Study (Baidoa) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Table 4](#A3.T4.6.6.4.5.1.1 "In Appendix C Supplementary Materials: Somalia Case Study (Baidoa) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* J. K. Cogan (2023)
  The united states arrests and charges eleven in connection with the assassination of haiti’s president.
  American Journal of International Law 117 (3),  pp. 511–516.
  External Links: [Document](https://dx.doi.org/10.1017/ajil.2023.37),
  [Link](https://www.cambridge.org/core/journals/american-journal-of-international-law/article/united-states-arrests-and-charges-eleven-in-connection-with-the-assassination-of-haitis-president/CFAEFAAA5C8152B9E66A56A108D317B6)
  Cited by: [Table 8](#A5.T8.6.9.7.5.1.1 "In Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* T. E. Copeland and D. Galai (1983)
  Information effects on the bid-ask spread.
  The Journal of Finance 38 (5),  pp. 1457–1469.
  External Links: [Document](https://dx.doi.org/10.2307/2327580)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* S. A. Corwin and P. Schultz (2012)
  A simple way to estimate bid-ask spreads from daily high and low prices.
  The Journal of Finance 67 (2),  pp. 719–760.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.2012.01729.x)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§5.1](#S5.SS1.p5.1 "5.1 Cross-country synthesis ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* D. Dawe (2010)
  The rice crisis: markets, policies and food security.
   Earthscan, London.
  Note: Prepared for the Food and Agriculture Organization of the United Nations (FAO)
  Cited by: [Table 10](#A6.T10.6.3.1.5.1.1 "In Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* H. Demsetz (1968)
  The cost of transacting.
  The Quarterly Journal of Economics 82 (1),  pp. 33–53.
  External Links: [Document](https://dx.doi.org/10.2307/1882244)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* Development Data Group (2021)
  Monthly food price estimates by product and market.
   World Bank, Development Data Group.
  Note: Data set
  External Links: [Document](https://dx.doi.org/10.48529/2ZH0-JF55)
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [footnote 2](#footnote2 "In 2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* DG ECHO and United Nations Office for the Coordination of Humanitarian Affairs (2024)
  Cameroon: floods (DG ECHO Partners, UN OCHA) — ECHO daily flash.
  Note: ReliefWeb
  External Links: [Link](https://reliefweb.int/report/cameroon/cameroon-floods-dg-echo-partners-un-ocha-echo-daily-flash-05-september-2024)
  Cited by: [Table 6](#A4.T6.6.10.8.5.1.1 "In Appendix D Supplementary Materials: Cameroon Case Study (Far North) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* O. Ecker, H. Alderman, A. R. Comstock, D. D. Headey, K. Mahrt, and A. Pradesha (2023)
  Mitigating poverty and undernutrition through social protection: a simulation analysis of the covid-19 pandemic in bangladesh and myanmar.
  Applied Economic Perspectives and Policy 45 (4),  pp. 2034–2055.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1002/aepp.13357),
  [Link](https://onlinelibrary.wiley.com/doi/abs/10.1002/aepp.13357),
  https://onlinelibrary.wiley.com/doi/pdf/10.1002/aepp.13357
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* L. E. Emediegwu and M. Rogna (2024)
  Agricultural commodities’ price transmission from international to local markets in developing countries.
  Food Policy 126,  pp. 102652.
  External Links: ISSN 0306-9192,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.foodpol.2024.102652),
  [Link](https://www.sciencedirect.com/science/article/pii/S0306919224000630)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* Famine Early Warning Systems Network (2024)
  Sudan: food security outlook.
  Technical report
   FEWS NET.
  Cited by: [Table 2](#A2.T2.6.10.8.5.1.1 "In Appendix B Supplementary Materials: Sudan Case Study (Al Fashir) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Table 2](#A2.T2.6.11.9.5.1.1 "In Appendix B Supplementary Materials: Sudan Case Study (Al Fashir) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* M. J. Fleming and E. M. Remolona (1999)
  Price formation and liquidity in the U.S. Treasury market: the response to public information.
  The Journal of Finance 54 (5),  pp. 1901–1915.
  External Links: [Document](https://dx.doi.org/10.1111/0022-1082.00172)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* Food and Agriculture Organization of the United Nations (2009)
  The food price crisis of 2007/2008: evidence and implications for food security.
  Technical report
   FAO, Rome, Italy.
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§5.1](#S5.SS1.p2.1 "5.1 Cross-country synthesis ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* Food and Agriculture Organization of the United Nations (2022)
  The importance of ukraine and the russian federation for global agricultural markets and the risks associated with the current conflict.
  Technical report
   FAO.
  External Links: [Link](https://www.fao.org/3/cb9013en/cb9013en.pdf)
  Cited by: [Table 10](#A6.T10.6.12.10.5.1.1 "In Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* M. B. Garman and M. J. Klass (1980)
  On the estimation of security price volatilities from historical data.
  Journal of Business 53 (1),  pp. 67–78.
  External Links: [Document](https://dx.doi.org/10.1086/296072)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§3](#S3.p1.1 "3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Definition 3](#Thmdefinition3.p1.2 "Definition 3 (Garman-Klass estimator). ‣ 3.2 Volatility Estimators ‣ 3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* T. K. Gbadegesin, B. P. J. Andrée, and A. Braimoh (2024)
  Climate shocks and their effects on food security, prices, and agricultural wages in afghanistan.
  Policy Research Working Paper
  Technical Report 10999, The World Bank, Washington, DC.
  External Links: [Document](https://dx.doi.org/10.1596/1813-9450-10999)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* C. L. Gilbert (2010)
  How to understand high food prices.
  Journal of Agricultural Economics 61 (2),  pp. 398–425.
  External Links: [Document](https://dx.doi.org/10.1111/j.1477-9552.2010.00248.x)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§5.1](#S5.SS1.p2.1 "5.1 Cross-country synthesis ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* W. Hanif, J. Areola Hernandez, S. J. H. Shahzad, and S. Yoon (2021)
  Tail dependence risk and spillovers between oil and food prices.
  The Quarterly Review of Economics and Finance 80,  pp. 195–209.
  External Links: ISSN 1062-9769,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.qref.2021.01.019),
  [Link](https://www.sciencedirect.com/science/article/pii/S1062976921000399)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* J. Hasbrouck and G. Saar (2013)
  Low-latency trading.
  Journal of Financial Markets 16 (4),  pp. 646–679.
  External Links: [Document](https://dx.doi.org/10.1016/j.finmar.2013.05.003)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* J. Hasbrouck (1995)
  One security, many markets: determining the contributions to price discovery.
  The Journal of Finance 50 (4),  pp. 1175–1199.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.1995.tb04054.x)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* J. Hasbrouck (2002)
  Stalking the “efficient price” in market microstructure specifications: an overview.
  Journal of Financial Markets 5 (3),  pp. 329–339.
  External Links: [Document](https://dx.doi.org/10.1016/S1386-4181%2802%2900029-4)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§5.1](#S5.SS1.p5.1 "5.1 Cross-country synthesis ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* M. Hassan and A. Kodouda (2019)
  Sudan’s uprising: the fall of a dictator.
  Journal of Democracy 30 (4),  pp. 89–103.
  External Links: [Document](https://dx.doi.org/10.1353/jod.2019.0071)
  Cited by: [Table 2](#A2.T2.6.5.3.5.1.1 "In Appendix B Supplementary Materials: Sudan Case Study (Al Fashir) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Table 2](#A2.T2.6.8.6.5.1.1 "In Appendix B Supplementary Materials: Sudan Case Study (Al Fashir) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Table 2](#A2.T2.6.9.7.5.1.1 "In Appendix B Supplementary Materials: Sudan Case Study (Al Fashir) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* D. Headey and S. Fan (2010)
  Reflections on the global food crisis: how did it happen? how has it hurt? and how can we prevent the next one?.
  IFPRI Research Report
  Technical Report 165, International Food Policy Research Institute (IFPRI).
  External Links: [Link](https://EconPapers.repec.org/RePEc:fpr:resrep:165)
  Cited by: [Table 2](#A2.T2.6.3.1.5.1.1 "In Appendix B Supplementary Materials: Sudan Case Study (Al Fashir) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Table 4](#A3.T4.6.3.1.5.1.1 "In Appendix C Supplementary Materials: Somalia Case Study (Baidoa) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Table 8](#A5.T8.6.3.1.5.1.1 "In Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* D. Headey and M. Ruel (2023)
  Food inflation and child undernutrition in low and middle income countries.
  Nature Communications 14,  pp. 5761.
  External Links: [Document](https://dx.doi.org/10.1038/s41467-023-41543-9)
  Cited by: [§5.3](#S5.SS3.p4.1 "5.3 Limitations ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* High Level Panel of Experts on Food Security and Nutrition (2011)
  Price volatility and food security.
  Technical report
   Committee on World Food Security, Rome, Italy.
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§5.1](#S5.SS1.p2.1 "5.1 Cross-country synthesis ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* Human Rights Watch (2013)
  Sudan: dozens killed during protests.
  Note: Human Rights Watch News Release27 September 2013
  Cited by: [Table 2](#A2.T2.6.6.4.5.1.1 "In Appendix B Supplementary Materials: Sudan Case Study (Al Fashir) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* International Crisis Group (2012)
  The philippines: breakthrough in mindanao.
  Technical report
  Technical Report Asia Report No. 240, International Crisis Group, Brussels.
  External Links: [Link](https://www.crisisgroup.org/asia-pacific/philippines/240-philippines-breakthrough-mindanao)
  Cited by: [Table 10](#A6.T10.6.4.2.5.1.1 "In Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* International Crisis Group (2018)
  Cameroon’s far north: a new chapter in the fight against Boko Haram.
  Technical report
  Technical Report 263, International Crisis Group.
  External Links: [Link](https://www.crisisgroup.org/africa/central-africa/cameroon/263-cameroons-far-north-new-chapter-fight-against-boko-haram)
  Cited by: [Table 6](#A4.T6.6.3.1.5.1.1 "In Appendix D Supplementary Materials: Cameroon Case Study (Far North) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* International Crisis Group (2024)
  Haiti’s gang crisis: a new approach.
  Technical report
   International Crisis Group, Brussels.
  Cited by: [Table 8](#A5.T8.6.11.9.5.1.1 "In Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* International Monetary Fund (2023a)
  Cameroon: 2023 article IV consultation—press release; staff report; and statement by the executive director for cameroon.
  Technical report
  Technical Report 2023/252, IMF Staff Country Reports, International Monetary Fund.
  External Links: [Document](https://dx.doi.org/10.5089/9798400246968.002),
  [Link](https://www.imf.org/en/Publications/CR/Issues/2023/07/11/Cameroon-2023-Article-IV-Consultation-Press-Release-Staff-Report-and-Statement-by-the-536274)
  Cited by: [Table 6](#A4.T6.6.9.7.5.1.1 "In Appendix D Supplementary Materials: Cameroon Case Study (Far North) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* International Monetary Fund (2023b)
  Philippines: 2023 article IV consultation—press release; staff report; and statement by the executive director for philippines.
  Technical report
  Technical Report 2023/414, IMF Staff Country Reports, International Monetary Fund.
  External Links: [Document](https://dx.doi.org/10.5089/9798400260551.002),
  [Link](https://www.imf.org/en/publications/cr/issues/2023/12/14/philippines-2023-article-iv-consultation-press-release-staff-report-and-statement-by-the-542518)
  Cited by: [Table 10](#A6.T10.6.13.11.5.1.1 "In Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* S. Kaiyatsa, N. V. de Sijpe, and B. Shankar (2023)
  How do transport costs affect price dispersion of nutrient-dense foods across markets in rural Malawi?.
  Technical report
   University of Sheffield.
  External Links: [Document](https://dx.doi.org/10.22004/AG.ECON.365931),
  [Link](https://doi.org/10.22004/AG.ECON.365931)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* B. López Cabrera and F. Schulz (2013)
  Volatility spillovers between crude oil and food prices.
  Energy Economics 36,  pp. 658–665.
  External Links: [Document](https://dx.doi.org/10.1016/j.eneco.2012.11.010)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* D. Maxwell and M. Fitzpatrick (2012)
  The 2011 Somalia famine: context, causes, and complications.
  Global Food Security 1 (1),  pp. 5–12.
  External Links: [Document](https://dx.doi.org/10.1016/j.gfs.2012.07.002)
  Cited by: [Table 4](#A3.T4.6.4.2.5.1.1 "In Appendix C Supplementary Materials: Somalia Case Study (Baidoa) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* N. McCulloch, D. Natalini, N. Hossain, and M. Kirchner (2022)
  An exploration of the association between fuel subsidies and fuel riots.
  World Development 157,  pp. 105935.
  External Links: [Document](https://dx.doi.org/10.1016/j.worlddev.2022.105935)
  Cited by: [Table 8](#A5.T8.6.7.5.5.1.1 "In Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* J. J. Murphy (1999)
  Technical analysis of the financial markets.
   New York Institute of Finance, New York, NY.
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* National Disaster Risk Reduction and Management Council (NDRRMC) (2020)
  Taal volcano eruption (january 2020): situation reports.
  External Links: [Link](https://ndrrmc.gov.ph/attachments/article/4141/SitRep_No_1_re_Taal_Volcano_Eruption_12JAN2020.pdf)
  Cited by: [Table 10](#A6.T10.6.10.8.5.1.1 "In Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* Official Gazette of the Republic of the Philippines (2019)
  Republic act no. 11203: an act liberalizing the importation, exportation and trading of rice.
  External Links: [Link](https://www.officialgazette.gov.ph/2019/02/14/republic-act-no-11203/)
  Cited by: [Table 10](#A6.T10.6.9.7.5.1.1 "In Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* M. Parkinson (1980)
  The extreme value method for estimating the variance of the rate of return.
  Journal of Business 53 (1),  pp. 61–65.
  External Links: [Document](https://dx.doi.org/10.1086/296071)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§3](#S3.p1.1 "3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* S. Penson, M. Lomme, Z. A. Carmichael, A. Manni, S. Shrestha, and B. P. J. Andrée (2024)
  A data-driven approach for early detection of food insecurity in yemen’s humanitarian crisis.
  Policy Research Working Paper
  Technical Report 10768, The World Bank, Washington, DC.
  External Links: [Document](https://dx.doi.org/10.1596/1813-9450-10768)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* Philippine Statistics Authority (2018)
  Selected statistics on agriculture.
  Technical report
   PSA, Manila.
  Cited by: [Table 10](#A6.T10.6.8.6.5.1.1 "In Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* L. C. G. Rogers and S. E. Satchell (1991)
  Estimating variance from high, low and closing prices.
  The Annals of Applied Probability 1 (4),  pp. 504–512.
  External Links: [Document](https://dx.doi.org/10.1214/aoap/1177005835)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Definition 4](#Thmdefinition4.p1.4 "Definition 4 (Rogers-Satchell estimator). ‣ 3.2 Volatility Estimators ‣ 3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* R. Roll (1984)
  A simple implicit measure of the effective bid-ask spread in an efficient market.
  The Journal of Finance 39 (4),  pp. 1127–1139.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.1984.tb03897.x)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* M. E. Sánchez-Martín (2020)
  For politics, people, or the planet? the political economy of fossil fuel reform, energy dependence and climate policy in Haiti.
  Energy Research & Social Science 63,  pp. 101405.
  External Links: [Document](https://dx.doi.org/10.1016/j.erss.2019.101405)
  Cited by: [Table 8](#A5.T8.6.8.6.5.1.1 "In Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* T. Schincariol and T. Chadefaux (2024)
  Temporal patterns in migration flows evidence from south sudan.
  Journal of Forecasting 44 (2),  pp. 575–588.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1002/for.3209),
  [Link](https://onlinelibrary.wiley.com/doi/abs/10.1002/for.3209),
  https://onlinelibrary.wiley.com/doi/pdf/10.1002/for.3209
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* K. Schwarz (2018)
  Mind the gap: disentangling credit and liquidity in risk spreads.
  Review of Finance 23 (3),  pp. 557–597.
  External Links: ISSN 1572-3097,
  [Document](https://dx.doi.org/10.1093/rof/rfy034),
  [Link](https://doi.org/10.1093/rof/rfy034),
  https://academic.oup.com/rof/article-pdf/23/3/557/28602693/rfy034.pdf
  Cited by: [§5.2](#S5.SS2.p2.1 "5.2 Implications for market monitoring ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* G. W. Schwert (1989)
  Why does stock market volatility change over time?.
  Journal of Finance 44 (5),  pp. 1115–1153.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.1989.tb02647.x)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* U.S. Geological Survey (2010)
  M 7.0 — haiti region earthquake (january 12, 2010).
  External Links: [Link](https://earthquake.usgs.gov/earthquakes/eventpage/us2010rja6)
  Cited by: [Table 8](#A5.T8.6.4.2.5.1.1 "In Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* UNICEF (2017)
  Cameroon: floods in far north—situation report.
  External Links: [Link](https://reliefweb.int/report/cameroon/cameroon-floods-far-north-situation-report-2017)
  Cited by: [Table 6](#A4.T6.6.4.2.5.1.1 "In Appendix D Supplementary Materials: Cameroon Case Study (Far North) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* United Nations Office for the Coordination of Humanitarian Affairs (2012)
  Philippines: typhoon bopha (pablo) situation report no. 2 (5 december 2012).
  Note: ReliefWeb
  External Links: [Link](https://reliefweb.int/report/philippines/philippines-typhoon-bopha-situation-report-no-2-5-december-2012)
  Cited by: [Table 10](#A6.T10.6.5.3.5.1.1 "In Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* United Nations Office for the Coordination of Humanitarian Affairs (2013)
  Philippines: typhoon haiyan situation report no. 10 (20 november 2013).
  Note: ReliefWeb
  External Links: [Link](https://reliefweb.int/report/philippines/philippines-typhoon-haiyan-situation-report-no-10-20-november-2013)
  Cited by: [Table 10](#A6.T10.6.6.4.5.1.1 "In Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* United Nations Office for the Coordination of Humanitarian Affairs (2017a)
  Haiti: hurricane irma situation report no. 1 (as of 8 september 2017).
  External Links: [Link](https://reliefweb.int/report/haiti/haiti-hurricane-irma-situation-report-no-1-8-september-2017)
  Cited by: [Table 8](#A5.T8.6.5.3.5.1.1 "In Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* United Nations Office for the Coordination of Humanitarian Affairs (2017b)
  Philippines: mindanao humanitarian bulletin no. 5 (june 2017).
  External Links: [Link](https://www.unocha.org/publications/report/philippines/philippines-mindanao-humanitarian-bulletin-no-5-june-2017)
  Cited by: [Table 10](#A6.T10.6.7.5.5.1.1 "In Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* United Nations Office for the Coordination of Humanitarian Affairs (2022a)
  Haiti: humanitarian situation and cholera – flash update #2 (6 october 2022).
  External Links: [Link](https://www.unocha.org/publications/report/haiti/haiti-humanitarian-situation-and-cholera-flash-update-2-6-october-2022)
  Cited by: [Table 8](#A5.T8.6.10.8.5.1.1 "In Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* United Nations Office for the Coordination of Humanitarian Affairs (2022b)
  West and central africa: weekly regional humanitarian snapshot (cameroon floods).
  External Links: [Link](https://reliefweb.int/report/world/west-and-central-africa-weekly-regional-humanitarian-snapshot-9-august-2022)
  Cited by: [Table 6](#A4.T6.6.7.5.5.1.1 "In Appendix D Supplementary Materials: Cameroon Case Study (Far North) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* United Nations Office for the Coordination of Humanitarian Affairs (2024)
  Somalia flooding: situation update (Gu season).
  External Links: [Link](https://reliefweb.int/report/somalia/somalia-flooding-situation-update-gu-2024)
  Cited by: [Table 4](#A3.T4.6.9.7.5.1.1 "In Appendix C Supplementary Materials: Somalia Case Study (Baidoa) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* United Nations (2016)
  Statement attributable to the spokesperson for the secretary-general on haiti (election postponement).
  External Links: [Link](https://www.un.org/sg/en/content/sg/statement/2016-01-25/statement-attributable-spokesperson-secretary-general-haiti)
  Cited by: [Table 8](#A5.T8.6.6.4.5.1.1 "In Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* D. Wang, B. P. J. Andrée, A. F. Chamorro, and P. G. Spencer (2022)
  Transitions into and out of food insecurity: a probabilistic approach with panel data evidence from 15 countries.
  World Development 159,  pp. 106035.
  External Links: ISSN 0305-750X,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.worlddev.2022.106035),
  [Link](https://www.sciencedirect.com/science/article/pii/S0305750X2200225X)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* D. Wang, B. P. J. Andrée, A. F. Chamorro Elizondo, and P. G. Spencer (2020)
  Stochastic modeling of food insecurity.
  Policy Research Working Paper
  Technical Report 9413, The World Bank, Washington, DC.
  External Links: [Document](https://dx.doi.org/10.1596/1813-9450-9413)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Price data and OHLC structure ‣ 2 Data ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* J. W. Wilder (1978)
  New concepts in technical trading systems.
   Trend Research, Greensboro, NC.
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§3.4](#S3.SS4.p3.1 "3.4 Detection rule and operational implementation ‣ 3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§5.2](#S5.SS2.p1.1 "5.2 Implications for market monitoring ‣ 5 Discussion ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* E. Workie, J. Mackolil, J. Nyika, and S. Ramadas (2020)
  Deciphering the impact of COVID-19 pandemic on food security, agriculture, and livelihoods: a review of the evidence from developing countries.
  Current Research in Environmental Sustainability 2,  pp. 100014.
  External Links: [Document](https://dx.doi.org/10.1016/j.crsust.2020.100014)
  Cited by: [Table 4](#A3.T4.6.7.5.5.1.1 "In Appendix C Supplementary Materials: Somalia Case Study (Baidoa) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* World Bank (2021)
  Philippines economic update, june 2021: navigating a challenging recovery.
  Technical report
   World Bank, Washington, DC.
  Note: License: CC BY 3.0 IGO
  External Links: [Document](https://dx.doi.org/10.1596/35690),
  [Link](https://hdl.handle.net/10986/35690)
  Cited by: [Table 10](#A6.T10.6.11.9.5.1.1 "In Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").
* D. Yang and Q. Zhang (2000)
  Drift-independent volatility estimation based on high, low, open, and close prices.
  Journal of Business 73 (3),  pp. 477–492.
  External Links: [Document](https://dx.doi.org/10.1086/209650)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§1](#S1.p5.1 "1 Introduction ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [§3](#S3.p1.1 "3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Definition 5](#Thmdefinition5.p1.3.3 "Definition 5 (Garman-Klass-Yang-Zhang extension). ‣ 3.2 Volatility Estimators ‣ 3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Definition 6](#Thmdefinition6.p1.3 "Definition 6 (Yang-Zhang estimator). ‣ 3.2 Volatility Estimators ‣ 3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data"),
  [Definition 6](#Thmdefinition6.p1.7.2 "Definition 6 (Yang-Zhang estimator). ‣ 3.2 Volatility Estimators ‣ 3 Methods ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data").

## Appendix A Additional Figures

This appendix provides additional figures showing the different volatility indicators in Somalia (Figure [7](#A1.F7 "Figure 7 ‣ Appendix A Additional Figures ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data")), Cameroon (Figure [8](#A1.F8 "Figure 8 ‣ Appendix A Additional Figures ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data")), Haiti (Figure [9](#A1.F9 "Figure 9 ‣ Appendix A Additional Figures ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data")), and the Philippines (Figure [10](#A1.F10 "Figure 10 ‣ Appendix A Additional Figures ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data")).

![Refer to caption](2603.02898v1/SOM_plot_all.png)


Figure 7: Open, High, Low, Close food prices (index, log) in Baidoa, Somalia, plotted on a candlestick chart together with six OHLC-based volatility metrics.

![Refer to caption](2603.02898v1/CMR_plot_all.png)


Figure 8: Open, High, Low, Close food prices (index, log) in Far North, Cameroon, plotted on a candlestick chart together with six OHLC-based volatility metrics.

![Refer to caption](2603.02898v1/HTI_plot_all.png)


Figure 9: Open, High, Low, Close food prices (index, log) in Port-au-Prince, Haiti, plotted on a candlestick chart together with six OHLC-based volatility metrics.

![Refer to caption](2603.02898v1/PHL_plot_all.png)


Figure 10: Open, High, Low, Close food prices (index, log) in Sulu, Philippines, plotted on a candlestick chart together with six OHLC-based volatility metrics.

## Appendix B Supplementary Materials: Sudan Case Study (Al Fashir)

This appendix provides an annotated timeline of major national and Darfur-specific episodes used to interpret volatility dynamics in Al Fashir. The timeline is compiled from human rights reporting, humanitarian monitoring systems, governance and political assessments, and international media coverage. The events are used solely for ex post interpretation of detected volatility segments and are not employed for causal identification.

Table 2: Al Fashir (Sudan): annotated event timeline for interpreting detected volatility episodes.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Period | Episode and context | Scale | Expected market mechanism and interpretation | Key sources |
| 2007–2008 | Global food and fuel price crisis transmitted to low-income import-dependent economies. | Global | A global import-cost shock raises staple price levels and increases within-period dispersion as pass-through varies over time and across supply channels. This can generate sustained high dispersion even when the overall price trend remains upward. | (Headey and Fan, [2010](#bib.bib56 "Reflections on the global food crisis: how did it happen? how has it hurt? and how can we prevent the next one?")) |
| 2007–2009 | Continued Darfur conflict dynamics and displacement pressures affecting market access around Al Fashir. | Darfur | Insecurity, displacement, and disrupted trade routes amplify intermittency in local supplies and raise the frequency of abrupt price movements. In volatility terms, this contributes to sustained abnormal dispersion consistent with localized market fragmentation. | (Amnesty International, [2014](#bib.bib14 "Sudan: those behind unlawful killings and torture of protesters must be brought to justice")) |
| 2010 (Apr.) | General elections under fragile national conditions and persistent insecurity in Darfur. | National & Darfur | Political uncertainty and localized insecurity can increase risk premia in trading corridors, disrupt market integration, and raise the variance of price changes even absent a discrete national macro shock. | (Hassan and Kodouda, [2019](#bib.bib84 "Sudan’s uprising: the fall of a dictator")) |
| 2011–2014 | South Sudan secession and fiscal rupture followed by austerity measures, subsidy cuts, and protest waves. | National | Macroeconomic adjustment and policy instability can produce sharp price jumps and partial reversals, increasing within-month dispersion through sudden supply interruptions and uncertainty about policy continuity. | (Human Rights Watch, [2013](#bib.bib17 "Sudan: dozens killed during protests")) |
| 2016 | Jebel Marra offensive and renewed violence in Darfur. | Darfur | Conflict intensification can disrupt rural production and access to market corridors, reducing the regularity of staple inflows and increasing intermittency in availability. | (Amnesty International, [2016](#bib.bib15 "Scorched earth, poisoned air: sudanese government forces ravage jebel marra, darfur")) |
| 2017–2019 | Deepening macroeconomic crisis culminating in bread-price protests and the fall of President Bashir (Dec. 2018–Apr. 2019). | National | A transition from chronic inflation to an acute crisis episode: shortages, depreciation, and political instability cause repeated supply breaks and abrupt corrections, increasing dispersion. | (Hassan and Kodouda, [2019](#bib.bib84 "Sudan’s uprising: the fall of a dictator")) |
| 2019–2022 | Transitional reforms under severe macro stress, followed by the October 2021 coup and renewed political uncertainty. | National | Weak policy credibility and institutional instability can sustain a high-volatility plateau through repeated repricing, shifting expectations, and enforcement discontinuities. | (Hassan and Kodouda, [2019](#bib.bib84 "Sudan’s uprising: the fall of a dictator")) |
| 2022–mid-2023 | Post-coup stagnation and mounting food-security stress preceding the outbreak of full-scale war. | National & Darfur | Chronic inflation and deteriorating terms of trade can cause volatility to drift upward, appearing as clusters of high-volatility flags consistent with incremental erosion of market functioning. | (Famine Early Warning Systems Network, [2024](#bib.bib16 "Sudan: food security outlook")) |
| mid-2023–2025 | SAF–RSF war and extended siege dynamics affecting Al Fashir; severe food-security outcomes and famine conditions. | National & Darfur (Al Fashir focus) | Physical insecurity and blockade-like conditions generate extreme within-month dispersion, sharp jumps, and partial corrections, consistent with structural market failure and fragmented price formation. | (Famine Early Warning Systems Network, [2024](#bib.bib16 "Sudan: food security outlook")) |

Table [3](#A2.T3 "Table 3 ‣ Appendix B Supplementary Materials: Sudan Case Study (Al Fashir) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") summarizes the dominant interpretation channels associated with each event class. The goal is to standardize narrative interpretation across cases while keeping the framework descriptive rather than causal.

| Event class | Typical volatility mechanism in market price data | Examples in Sudan |
| --- | --- | --- |
| Global price shock | Pass-through of international price increases can be uneven across months due to import timing, credit constraints, and heterogeneous local supply substitution. This often produces elevated dispersion beyond what level-based trend measures capture. | 2007–08 global food price crisis |
| Macroeconomic rupture / policy reform | Currency depreciation, subsidy removal, and credibility shocks can generate repeated step changes and reversals in local prices as expectations update and policy implementation fluctuates. Dispersion increases even when the average trend remains upward. | Post-2011 adjustment; reforms under transition (2019–2022) |
| Conflict escalation / corridor disruption | Insecurity and violence disrupt flows, increase transaction costs, and fragment markets. Prices become intermittent and discontinuous, often yielding sharp volatility spikes even when the direction of price changes is unclear. | Jebel Marra (2016); war and siege dynamics (2023–2025) |
| Political upheaval / institutional shocks | Transitions, coups, and governance breakdown can operate as uncertainty shocks that amplify dispersion through behavioral responses (hoarding, speculation, enforcement discontinuities) rather than through a single supply or demand lever. | 2010 elections; October 2021 coup |
| Chronic stress / deterioration | A gradual worsening of conditions may show up as clusters of smaller high-volatility flags rather than one discrete event. This pattern can matter operationally because it signals sustained fragility even without a headline trigger. | 2022–mid-2023 pre-war stress |

Table 3: Interpretation guidance for relating contextual events to detected volatility segments in Al Fashir.

## Appendix C Supplementary Materials: Somalia Case Study (Baidoa)

This appendix provides an annotated timeline of major national and subnational episodes used to interpret volatility dynamics in Baidoa. The timeline is compiled from humanitarian and food-security monitoring products, UN reporting, and public documentation. The events are used solely for ex post interpretation of detected volatility segments and are not employed for causal identification.

Table 4: Baidoa (Somalia): annotated event timeline for interpreting detected volatility episodes.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Period | Episode and context | Scale | Expected market mechanism and interpretation | Key sources |
| 2007–2008 | Global food price crisis transmitted to Somalia during a period of structural vulnerability. | Global & Somalia | A global import-cost shock raises staple price levels and increases within-period dispersion as pass-through and availability vary over time. | (Headey and Fan, [2010](#bib.bib56 "Reflections on the global food crisis: how did it happen? how has it hurt? and how can we prevent the next one?")) |
| 2011 | Severe food-security crisis and famine in parts of southern Somalia. | National & South-central | A compound shock environment contributes to sharp price dislocations and abnormal dispersion consistent with intermittent supply and breakdowns in market clearing. | (Maxwell and Fitzpatrick, [2012](#bib.bib52 "The 2011 Somalia famine: context, causes, and complications")) |
| 2014–2015 | Renewed stress associated with weak seasonal performance and disruptions affecting Bay/Bakool livelihoods and trade flows. | Subnational (Bay/Bakool) | Localized constraints reduce the regularity of inflows and raise dispersion through intermittent supply and shifting expectations. | (Checchi et al., [2023](#bib.bib66 "Drought, armed conflict and population mortality in Somalia, 2014–2018: a statistical analysis")) |
| 2016–2017 | Drought emergency and warnings of renewed famine risk; large-scale impacts mitigated by early response. | National & South-central | Drought generates elevated dispersion through production shortfalls, income losses, and shifting trade patterns, typically appearing as sustained high volatility. | (Checchi et al., [2023](#bib.bib66 "Drought, armed conflict and population mortality in Somalia, 2014–2018: a statistical analysis")) |
| 2020 | COVID-19 related disruptions coinciding with desert locust impacts. | National & regional | Simultaneous shocks affect logistics and production risk, amplifying within-month dispersion even when average price levels move gradually. | (Workie et al., [2020](#bib.bib57 "Deciphering the impact of COVID-19 pandemic on food security, agriculture, and livelihoods: a review of the evidence from developing countries")) |
| 2022 | Global price transmission following the Russia–Ukraine war. | Global & Somalia | Externally driven cost increases raise dispersion through uneven pass-through and intermittent access conditions. | (Arabi and others, [2022](#bib.bib58 "The impact of the Russia-Ukraine war on global food security")) |
| 2023–2024 | Severe flooding episodes affecting large parts of Somalia. | National & regional | Flooding disrupts transport and market functioning, producing sharp volatility spikes reflecting localized shortages and corrections as flows resume. | (United Nations Office for the Coordination of Humanitarian Affairs, [2024](#bib.bib67 "Somalia flooding: situation update (Gu season)")) |

Table [5](#A3.T5 "Table 5 ‣ Appendix C Supplementary Materials: Somalia Case Study (Baidoa) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") summarizes the dominant interpretation channels associated with each event class. The goal is to standardize narrative interpretation across cases while keeping the framework descriptive rather than causal.

| Event class | Typical volatility mechanism in market price data | Examples in Somalia |
| --- | --- | --- |
| Global price shock | Uneven pass-through of international food and fuel prices increases dispersion through import timing, exchange-rate pressures, credit frictions, and heterogeneous substitution in local markets. | 2007–08 crisis; 2022 global transmission |
| Drought / rainfall failure | Production shortfalls and income losses raise dispersion through intermittent availability, shifting trade flows, and nonlinear responses in purchasing power and demand compression. | 2011 famine context; 2016–2017 drought |
| Flood / transport disruption | Infrastructure damage and corridor disruption create localized shortages and sharp corrections as access fluctuates over time. | 2023–2024 floods |
| Compound disruption (health, pests, logistics) | Simultaneous shocks can impair both supply and logistics while raising uncertainty, generating volatility even when levels move gradually. | COVID-19 and locust upsurge (2020) |
| Localized livelihood and access stress | Subnational disruptions can appear as clusters of high-volatility flags driven by intermittency in flows to key markets and relief hubs. | Bay/Bakool stress (2014–2015) |

Table 5: Interpretation guidance for relating contextual events to detected volatility segments in Baidoa.

## Appendix D Supplementary Materials: Cameroon Case Study (Far North)

This appendix provides an annotated timeline of major episodes used to interpret volatility dynamics in Cameroon’s Far North. The timeline is compiled from conflict reporting and humanitarian monitoring, flood and emergency assessments, policy documentation, and public sources. These materials are used solely for ex post interpretation of detected volatility segments and are not employed for causal identification.

Table 6: Cameroon (Far North): annotated event timeline for interpreting detected volatility episodes.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Period | Episode and context | Scale | Expected market mechanism and interpretation | Key sources |
| 2014–2016 | Intensification of insecurity and insurgency spillovers in the Far North. | Subnational & cross-border | Insecurity increases transaction costs and intermittency of supply, contributing to higher dispersion through market fragmentation and discontinuous trading. | (International Crisis Group, [2018](#bib.bib69 "Cameroon’s far north: a new chapter in the fight against Boko Haram")) |
| 2017 | Flood-related shocks affecting livelihoods and transport access. | Subnational | Flooding disrupts production and infrastructure, creating localized shortages and unstable access that elevate dispersion. | (UNICEF, [2017](#bib.bib70 "Cameroon: floods in far north—situation report")) |
| 2019–2020 | Cross-border trade constraints associated with Nigeria’s border policy episode. | Regional & cross-border | Border frictions reduce arbitrage and raise dispersion through irregular availability and uneven pass-through. | (Aremu et al., [2023](#bib.bib88 "Nigeria land border closure: implication on rice smuggling and local production")) |
| 2020 | COVID-19 mobility restrictions and logistics disruptions. | National | Movement constraints disrupt supply chains and raise dispersion through irregular inflows and episodic repricing. | (Amare et al., [2020](#bib.bib59 "COVID-19 and food security in Africa: building more resilient food systems")) |
| 2022 | Flood emergencies and renewed climate-related disruption. | Subnational | Transport impairment and localized production losses increase intermittency in supplies and raise volatility. | (United Nations Office for the Coordination of Humanitarian Affairs, [2022b](#bib.bib71 "West and central africa: weekly regional humanitarian snapshot (cameroon floods)")) |
| 2022 | Global commodity-price and energy-cost pressures following the Russia–Ukraine shock. | Global & Cameroon | Externally driven increases in food and fuel costs transmit through import and transport channels, elevating dispersion through uneven pass-through. | (Arabi and others, [2022](#bib.bib58 "The impact of the Russia-Ukraine war on global food security")) |
| 2023 | Fuel price adjustment and cost shock to transport and distribution margins. | National | Discrete increases in energy costs generate abrupt repricing and elevated dispersion, especially in remote areas where transport margins are large. | (International Monetary Fund, [2023a](#bib.bib68 "Cameroon: 2023 article IV consultation—press release; staff report; and statement by the executive director for cameroon")) |
| 2024 | Renewed flood impacts and humanitarian access constraints. | Subnational | Flooding and access limitations sustain intermittency in supply conditions and localized market fragmentation. | (DG ECHO and United Nations Office for the Coordination of Humanitarian Affairs, [2024](#bib.bib60 "Cameroon: floods (DG ECHO Partners, UN OCHA) — ECHO daily flash")) |

Table [7](#A4.T7 "Table 7 ‣ Appendix D Supplementary Materials: Cameroon Case Study (Far North) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") summarizes the dominant interpretation channels associated with each event class. The goal is to standardize narrative interpretation across cases while keeping the framework descriptive rather than causal.

| Event class | Typical volatility mechanism in market price data | Examples in Cameroon |
| --- | --- | --- |
| Conflict / insecurity | Higher corridor risk and transaction costs fragment markets and generate intermittent supply, producing abrupt jumps and partial corrections. | Insurgency spillovers (mid-2010s) |
| Flood / transport disruption | Infrastructure damage and access constraints create localized shortages and unstable inflows, often appearing as clustered volatility flags. | Flood episodes (2017; 2022; 2024) |
| Cross-border policy disruption | Border frictions weaken arbitrage and raise dispersion through irregular availability and uneven pass-through across locations and months. | Nigeria border policy episode (2019–2020) |
| Mobility and logistics shock | Restrictions and uncertainty disrupt supply chains and distribution margins even if price levels move gradually. | COVID-19 period (2020) |
| Energy / cost transmission | Fuel and freight shocks transmit quickly through distribution margins, generating discrete repricing and elevated dispersion. | Fuel price adjustment (2023); global cost pressures (2022) |

Table 7: Interpretation guidance for relating contextual events to detected volatility segments in Cameroon’s Far North.

## Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince)

This appendix provides an annotated timeline of major episodes used to interpret volatility dynamics in Port-au-Prince. The timeline is compiled from earthquake and disaster documentation, humanitarian monitoring, governance and political reporting, and public sources. These materials are used solely for ex post interpretation of detected volatility segments and are not employed for causal identification.

Table 8: Haiti (Port-au-Prince): annotated event timeline for interpreting detected volatility episodes.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Period | Episode and context | Scale | Expected market mechanism and interpretation | Key sources |
| 2007–2008 | Global food price shock and price unrest in an import-dependent economy. | Global & Haiti | External price transmission raises levels and increases dispersion as pass-through varies with import timing and distribution constraints. | (Headey and Fan, [2010](#bib.bib56 "Reflections on the global food crisis: how did it happen? how has it hurt? and how can we prevent the next one?")) |
| 2010 (Jan.) | Catastrophic earthquake causing large-scale infrastructure damage and long-lived disruption. | National (urban core) | A structural shock to logistics and market functioning increases intermittency in supply and produces persistent abnormal dispersion. | (U.S. Geological Survey, [2010](#bib.bib72 "M 7.0 — haiti region earthquake (january 12, 2010)")) |
| 2013–2017 | Recurrent climate and hurricane impacts affecting livelihoods and access. | National | Disaster impacts disrupt trade flows and infrastructure and can generate sharp volatility spikes as corridor access fluctuates. | (United Nations Office for the Coordination of Humanitarian Affairs, [2017a](#bib.bib73 "Haiti: hurricane irma situation report no. 1 (as of 8 september 2017)")) |
| 2015–2016 | Political disruption and electoral uncertainty, including delayed or disputed electoral processes. | National | Institutional instability and uncertainty raise dispersion through expectations shocks, episodic market closures, and interruptions to commerce. | (United Nations, [2016](#bib.bib74 "Statement attributable to the spokesperson for the secretary-general on haiti (election postponement)")) |
| 2018 | Fuel price announcement and riots with major disruption to mobility and commerce. | National (urban) | Transport-cost shocks and market interruptions generate discrete repricing and elevated dispersion. | (McCulloch et al., [2022](#bib.bib86 "An exploration of the association between fuel subsidies and fuel riots")) |
| 2019 | PetroCaribe protests and *peyi lòk* lockdown disruptions. | National | Sustained disruption fragments markets and induces intermittent availability and abrupt corrections, generating prolonged elevated volatility. | (Sánchez-Martín, [2020](#bib.bib87 "For politics, people, or the planet? the political economy of fossil fuel reform, energy dependence and climate policy in Haiti")) |
| 2021 | Presidential assassination and renewed political instability. | National | Political shock amplifies uncertainty and weakens market coordination, contributing to repeated interruptions and fragile expectations. | (Cogan, [2023](#bib.bib61 "The united states arrests and charges eleven in connection with the assassination of haiti’s president")) |
| 2022 | Fuel access crisis around Terminal Varreux and worsening access constraints. | National (Port-au-Prince focus) | Control of key infrastructure creates intermittent access to fuel and goods, driving volatility via distribution breakdown and localized shortages. | (United Nations Office for the Coordination of Humanitarian Affairs, [2022a](#bib.bib75 "Haiti: humanitarian situation and cholera – flash update #2 (6 october 2022)")) |
| 2023–2024 | Escalating insecurity and corridor control; major violence surge and emergency conditions. | National (urban core) | Sustained market fragmentation generates persistent abnormal dispersion as supplies become sporadic and trading becomes discontinuous. | (International Crisis Group, [2024](#bib.bib85 "Haiti’s gang crisis: a new approach")) |

Table [9](#A5.T9 "Table 9 ‣ Appendix E Supplementary Materials: Haiti Case Study (Port-au-Prince) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") summarizes the dominant interpretation channels associated with each event class. The goal is to standardize narrative interpretation across cases while keeping the framework descriptive rather than causal.

| Event class | Typical volatility mechanism in market price data | Examples in Haiti |
| --- | --- | --- |
| Global price shock | External transmission produces uneven pass-through and abrupt repricing in import-dependent urban markets. | 2007–08 crisis |
| Major disaster / structural damage | Infrastructure collapse and logistics disruption create persistent intermittency and prolonged abnormal dispersion. | 2010 earthquake |
| Political disruption / unrest | Uncertainty, market closures, and mobility constraints generate discontinuous trading and volatility clusters. | 2015–2016 disruptions; 2019 *peyi lòk* |
| Fuel and logistics shock | Transport-cost shocks transmit quickly through distribution margins and availability, producing sharp spikes. | 2018 riots; 2022 fuel access crisis |
| Sustained insecurity / corridor control | Market fragmentation becomes structural, producing persistent high-volatility regimes rather than isolated spikes. | 2023–2024 violence surge |

Table 9: Interpretation guidance for relating contextual events to detected volatility segments in Port-au-Prince.

## Appendix F Supplementary Materials: Philippines Case Study (Sulu)

This appendix provides an annotated timeline of major episodes used to interpret volatility dynamics in selected Philippine markets. The timeline is compiled from disaster and humanitarian reporting, policy documentation, macro and cost transmission sources, and public records. These materials are used solely for ex post interpretation of detected volatility segments and are not employed for causal identification.

Table 10: Philippines (selected markets): annotated event timeline for interpreting detected volatility episodes.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Period | Episode and context | Scale | Expected market mechanism and interpretation | Key sources |
| 2007–2008 | Global food and fuel price crisis transmitted to domestic staple markets. | Global & Philippines | External price transmission raises levels and increases dispersion via uneven pass-through, procurement timing, and heterogeneous substitution and distribution margins. | (Dawe, [2010](#bib.bib62 "The rice crisis: markets, policies and food security")) |
| 2012 (Oct.) | Framework Agreement on the Bangsamoro and heightened political mobilization in Moro areas, including the Sulu archipelago. | Subnational & national | Political uncertainty and episodic security risks raise corridor premia and reduce market integration, increasing dispersion through intermittent inflows and discontinuous trading. | (International Crisis Group, [2012](#bib.bib82 "The philippines: breakthrough in mindanao")) |
| 2012 (Dec.) | Typhoon Bopha (Pablo) strikes Mindanao, causing widespread destruction and disruption to production and transport. | Subnational (Mindanao) | A disaster shock disrupts supply chains and access, creating localized shortages and abrupt price jumps with partial corrections as flows resume. | (United Nations Office for the Coordination of Humanitarian Affairs, [2012](#bib.bib83 "Philippines: typhoon bopha (pablo) situation report no. 2 (5 december 2012)")) |
| 2013 | Zamboanga crisis and Typhoon Haiyan with large displacement and logistics impacts. | National & subnational | Disasters and localized conflict disrupt supply chains, producing abrupt dislocations and volatility spikes as corridor access fluctuates and distribution resumes. | (United Nations Office for the Coordination of Humanitarian Affairs, [2013](#bib.bib76 "Philippines: typhoon haiyan situation report no. 10 (20 november 2013)")) |
| 2017 | Marawi siege with displacement and movement restrictions and broader trade spillovers. | Subnational (Mindanao) | Security disruptions fragment market access and raise dispersion through intermittent inflows, mobility constraints, and nonlinear adjustment of distribution margins. | (United Nations Office for the Coordination of Humanitarian Affairs, [2017b](#bib.bib77 "Philippines: mindanao humanitarian bulletin no. 5 (june 2017)")) |
| 2014–2018 | Energy and freight-cost volatility with renewed price pressure during the 2018 fuel upswing. | Global & Philippines | Energy and freight costs transmit through distribution margins; shifts in transport costs can generate step changes and elevated dispersion. | (Philippine Statistics Authority, [2018](#bib.bib63 "Selected statistics on agriculture")) |
| 2019 (Feb.) | Rice Tariffication Law (RA 11203) and discontinuity in the rice import regime. | National (policy) | Policy shifts alter price expectations and market structure, generating adjustment dynamics and dispersion as supply conditions re-optimize. | (Official Gazette of the Republic of the Philippines, [2019](#bib.bib78 "Republic act no. 11203: an act liberalizing the importation, exportation and trading of rice")) |
| 2020 (Jan.) | Taal volcano eruption disrupting activity and logistics. | National | Disaster shock temporarily disrupts flows and access, raising dispersion as supply conditions adjust unevenly. | (National Disaster Risk Reduction and Management Council (NDRRMC), [2020](#bib.bib79 "Taal volcano eruption (january 2020): situation reports")) |
| 2020 (Mar.) | COVID-19 pandemic and associated mobility and supply-chain disruption. | National | Movement constraints and uncertainty disrupt logistics and distribution margins, generating volatility spikes through episodic market adjustment. | (World Bank, [2021](#bib.bib64 "Philippines economic update, june 2021: navigating a challenging recovery")) |
| 2022 | Global energy and shipping-cost pressures following the Russia–Ukraine shock. | Global & Philippines | Externally driven cost shocks transmit through fuel and shipping, raising dispersion via uneven pass-through and time-varying supply conditions. | (Food and Agriculture Organization of the United Nations, [2022](#bib.bib80 "The importance of ukraine and the russian federation for global agricultural markets and the risks associated with the current conflict")) |
| 2023 | Persistently elevated inflation without a single discrete trigger. | National | Sustained cost pressures can produce clusters of high-volatility flags driven by repeated repricing and heterogeneous adjustment across markets. | (International Monetary Fund, [2023b](#bib.bib81 "Philippines: 2023 article IV consultation—press release; staff report; and statement by the executive director for philippines")) |

Table [11](#A6.T11 "Table 11 ‣ Appendix F Supplementary Materials: Philippines Case Study (Sulu) ‣ Range-Based Volatility Estimators for Monitoring Market Stress: Evidence from Local Food Price Data") summarizes the dominant interpretation channels associated with each event class. The goal is to standardize narrative interpretation across cases while keeping the framework descriptive rather than causal.

| Event class | Typical volatility mechanism in market price data | Examples in the Philippines |
| --- | --- | --- |
| Global price / cost transmission | Uneven pass-through of international food, fuel, and shipping costs raises dispersion via procurement timing and heterogeneous distribution margins. | 2007–08; 2022 |
| Disaster / logistics disruption | Infrastructure damage and mobility constraints generate discontinuous trading and sharp volatility spikes. | Haiyan (2013); Taal (2020) |
| Localized security disruption | Movement restrictions and access constraints fragment markets and produce intermittent inflows. | Marawi siege (2017) |
| Policy discontinuity | Regime changes alter expectations and supply behavior, producing adjustment dynamics and elevated dispersion. | Rice Tariffication Law (2019) |
| Persistent cost pressure | Sustained inflation can produce clustered high-volatility flags even without a single focal trigger. | 2023 inflation persistence |

Table 11: Interpretation guidance for relating contextual events to detected volatility segments in selected Philippine markets.

BETA