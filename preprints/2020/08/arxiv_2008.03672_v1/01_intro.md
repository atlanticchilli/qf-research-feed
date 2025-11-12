---
authors:
- Thilini V. Mahanama
- Abootaleb Shirvani
doc_id: arxiv:2008.03672v1
family_id: arxiv:2008.03672
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2008.03672] A Natural Disasters Index'
url_abs: http://arxiv.org/abs/2008.03672v1
url_html: https://ar5iv.org/html/2008.03672v1
venue: arXiv q-fin
version: 1
year: 2020
---


Thilini V. Mahanama
Texas Tech University, Department of Mathematics
& Statistics, Lubbock TX 79409-1042, U.S.A., thilini.v.mahanama@ttu.edu (Corresponding
Author).
  
Abootaleb Shirvani
Texas Tech University, Department of Mathematics
& Statistics, Lubbock TX 79409-1042, U.S.A., abootaleb.shirvani@ttu.edu.

###### Abstract

Natural disasters, such as tornadoes, floods, and wildfire pose risks to life and property, requiring the intervention of insurance corporations. One of the most visible consequences of changing climate is an increase in the intensity and frequency of extreme weather events. The relative strengths of these disasters are far beyond the habitual seasonal maxima, often resulting in subsequent increases in property losses. Thus, insurance policies should be modified to endure increasingly volatile catastrophic weather events. We propose a Natural Disasters Index (NDI) for the property losses caused by natural disasters in the United States based on the “Storm Data” published by the National Oceanic and Atmospheric Administration. The proposed NDI is an attempt to construct a financial instrument for hedging the intrinsic risk. The NDI is intended to forecast the degree of future risk that could forewarn the insurers and corporations allowing them to transfer insurance risk to capital market investors. This index could also be modified to other regions and countries.

Keywords: Natural Disasters Index (NDI), Index-based Catastrophe Derivatives, Option Pricing, Risk Budgeting, Stress Testing.

## 1 Introduction

Natural disasters are low-probability, high-consequence events that wreak havoc on financial security (Roth Sr and
Kunreuther, [1998](#bib.bib38)).
The National Centers for Environmental Information (NCEI) reports the United States has experienced 69 natural disasters with losses exceeding one billion dollars between 2015 and 2019.
The accumulated loss exceeds $535 billion at an average of $107.1 billion/year.
The trend of disaster frequency is expected to escalate over the years due to changes in climate which will result in deleterious losses (Lyubchich and
Gel, [2017](#bib.bib27)).
These volatile weather patterns will result in an inevitable challenge to the U.S.’s ability to sustain human and economic development (Tabuchi, [2018](#bib.bib40)).
As a result, weather risk markets need to be capable of offsetting the financial impacts of natural disasters (Varangis
et al., [2003](#bib.bib43); Dilley et al., [2005](#bib.bib14)).

The losses due to natural disasters exacerbate due to changes in population and national wealth density (Van der Vink
et al., [1998](#bib.bib42); Bell
et al., [2018](#bib.bib5)).
Roth Sr and
Kunreuther ([1998](#bib.bib38)) suggest that if insurers are to retain profitability and solvency in the event of a major catastrophe that insurers must increase their prices for catastrophe insurance and reduce their exposure to risk.
Also, reinsurers undergo severe financial stress in facilitating catastrophe insurance by offering tenable reduction for risk in large catastrophic losses (Lewis and
Murdock, [1996](#bib.bib24); Liang
et al., [2010](#bib.bib25); Zangue and
Poppo, [2016](#bib.bib45)).
However, the detrimental losses can be alleviated using protective measures such as preparedness, mitigation, and insurance (Kunreuther, [1996](#bib.bib23); Ganderton et al., [2000](#bib.bib16)).
To better protect the clients, catastrophe insurance policies should ramp-up investments in cost-effective loss reduction mechanisms by better managing the risk.

According to Barnett and
Mahul ([2007](#bib.bib4)), the weather index insurance can effectively transfer spatially covariate weather risks as it pays indemnities based on realizations of a weather index that is highly correlated with actual losses.
The securitization of losses from natural disasters provides a valuable novel source of diversification for investors.
Catastrophe risk bonds are a promising type of insurance-linked securities introduced to smooth transferring of catastrophic insurance risk from insurers and corporations to capital market investors by offering an alternative or complement of capital to the traditional reinsurance (Zangue and
Poppo, [2016](#bib.bib45)).
Cummins
et al. ([2004](#bib.bib13)) describe three types of variables that pay off in insurance-linked securities: insurer-specific catastrophe losses, insurance-industry catastrophe loss indices, and parametric indices based on the physical characteristics of catastrophic events.

Unequivocally, the catastrophe losses and related risks inherent create uncertainty over the type of disaster event (Lewis and
Murdock, [1996](#bib.bib24); NCEI, [2020a](#bib.bib35)).
For example, due to less coverage of insured assets and data latency in drought and flooding events, they tend to provide uncertain loss estimates compared to the losses of severe storm events in the United States (NCEI, [2020a](#bib.bib35); Smith and
Matthews, [2015](#bib.bib39)).
In consequence, prioritization for mitigating the risks can be diverse and complex.

We propose a Natural Disasters Index (NDI) for the United States using the property losses reported in NOAA Storm Data (NCEI, [2018](#bib.bib33)) between 1996 and 2018.
The NDI is aimed to assess the level of future systemic risk caused by natural disasters.
We follow the methods applied in Trindade
et al. ([2020](#bib.bib41)) on an ad hoc basis as a benchmark for NDI evaluation: (1) option pricing, (2) risk budgeting, and (3) stress testing.
We provide an evaluation framework for the NDI using a discrete-time generalized autoregressive conditional heteroskedasticity model to calculate the fair values of the NDI options.
Then, we simulate call and put option prices using the Monte Carlo method.
We distribute the cumulative risk attributed to our equally weighted portfolio into the risk contributions of each type of natural disaster.
Flood and flash flood are the main risk contributors in our portfolio according to our assessments using standard deviation and expected tail loss risk budgets.
Furthermore, we evaluate the portfolio risk of the NDI to mitigate risks using monthly maximum temperature and the Palmer Drought Severity Index (PDSI) as stressors.
We found the stress on maximum temperature significantly impacts the NDI compared to that of the PDSI at the highest stress level (1%).

There have been similar attempts to develop indices in the past, though many of these are no longer used because of inherent problems.
The first index-based catastrophe derivatives, CAT-futures, introduced by the Chicago Board of Trade using the ISO-Index was ineffective due to a lack of realistic models in the market (Christensen and
Schmidli, [2000](#bib.bib12)).
Secondly, the Property Claim Services (PCS) proposed the PCS-options based on the PCS-index.
Biagini
et al. ([2008](#bib.bib6)) describe that the PCS-options slowed down due to market illiquidity.
Then, the New York Mercantile Exchange (NYMEX) designed catastrophe futures and options to enhance the transparency and liquidity of the capital markets to the insurance sector (Biagini
et al., [2008](#bib.bib6)).
Kielholz and
Durrer ([1997](#bib.bib22)) further explain alternative risk transfer mechanisms within the context of natural catastrophe problems in the United States.

The proposed NDI attempts to address these shortcomings by creating a financial instrument for hedging the intrinsic risk induced by the property losses caused by natural disasters in the United States.
The vital objective of the NDI is to forecast the severity of future systemic risk attributed to natural disasters.
This provides advance warnings to the insurers and corporations allowing them to transfer insurance risk to capital market investors.
Therefore, the proposed NDI will conspicuously help to make up the shortfall between the capital and insurance markets.
The NDI identifies the potential risk contributions of each natural disaster and provides options and futures.
Furthermore, the NDI could be modified to calculate the risk in other regions or countries using a data set comparable to NOAA Storm Data NCEI ([2018](#bib.bib33)).

The contents of the rest of this paper are as follows. We provide an exploratory data analysis in section [2](#S2 "2 Construction of the Natural Disasters Index (NDI) ‣ A Natural Disasters Index") before constructing the NDI.
Section [3](#S3 "3 NDI Option Prices ‣ A Natural Disasters Index") presents the steps in option pricing and approximate call and put option prices for the NDI.
In section [4](#S4 "4 NDI Risk Budgets ‣ A Natural Disasters Index"), we provide standard deviation and expected tail loss risk budgets for natural disasters in the United States.
We assess the performance of the NDI via a stress testing analysis in section [5](#S5 "5 Stress Testing Analysis for the NDI ‣ A Natural Disasters Index").
Finally, we make concluding remarks in section [6](#S6 "6 Discussion and Conclusion ‣ A Natural Disasters Index").

## 2 Construction of the Natural Disasters Index (NDI)

The National Oceanic and Atmospheric Administration (NOAA) has published information on severe weather events occurring in the United States between 1950 and 2018 in their “Storm Data” database (Murphy, [2018](#bib.bib31)).
We utilize the property losses caused by the following 50 types of natural disasters from 1996-2018 to construct a natural disasters index:

> Avalanche, Blizzard, Coastal Flood, Cold/Wind Chill, Debris Flow, Dense Fog, Dense Smoke, Drought, Dust Devil, Dust Storm, Excessive Heat, Extreme Cold/Wind Chill, Flash Flood, Flood, Frost/Freeze, Funnel Cloud, Freezing Fog, Hail, Heat, Heavy Rain, Heavy Snow, High Surf, High Wind, Hurricane (Typhoon), Ice Storm, Lake-Effect Snow, Lakeshore Flood, Lightning, Marine Dense Fog, Marine Heavy Freezing Spray, Marine High Wind, Marine Hurricane/Typhoon, Marine Lightning, Marine Strong Wind, Marine Thunderstorm Wind, Rip Current, Seiche, Sleet, Storm Surge/Tide, Strong Wind, Thunderstorm Wind, Tornado, Tropical Depression, Tropical Storm, Tsunami, Volcanic Ash, Waterspout, Wildfire, Winter Storm, Winter Weather.

The database reports the property losses incurred by natural disasters in U.S. dollars of the given year (Murphy, [2018](#bib.bib31)).
For this study, we estimate them in U.S. dollars adjusted for inflation in 2019.
Figure [1](#S2.F1 "Figure 1 ‣ 2 Construction of the Natural Disasters Index (NDI) ‣ A Natural Disasters Index") provides examples of natural disasters between 1996 and 2018 that exemplify eccentric property losses (adjusted for inflation in 2019).

![Refer to caption](/html/2008.03672/assets/x1.png)

![Refer to caption](/html/2008.03672/assets/x2.png)

![Refer to caption](/html/2008.03672/assets/x3.png)

![Refer to caption](/html/2008.03672/assets/x4.png)

![Refer to caption](/html/2008.03672/assets/x5.png)

![Refer to caption](/html/2008.03672/assets/x6.png)

Figure 1: The monthly property losses (in billions adjusted for inflation in 2019) caused by drought, flood, winter storm, thunderstorm wind, hail, and tornado events between 1996 and 2018 generated using NOAA Storm Data (NCEI, [2018](#bib.bib33)).

Natural Disasters Index (NDI)
  
To obtain an equally spaced time series, we examine the cumulative property losses for all 50 types of natural disasters in two-week increments between 1996 and 2018. We define Ltsubscript𝐿𝑡L\_{t} as the total property loss at the t𝑡tth biweekly period. Then, we transform this time series Ltsubscript𝐿𝑡L\_{t} to a stationary time series by taking the first difference (lag-1 difference) of Lt0.1superscriptsubscript𝐿𝑡0.1L\_{t}^{0.1} ([1](#S2.E1 "In 2 Construction of the Natural Disasters Index (NDI) ‣ A Natural Disasters Index")), see Figure [2](#S2.F2 "Figure 2 ‣ 2 Construction of the Natural Disasters Index (NDI) ‣ A Natural Disasters Index"). Thus, we propose a Natural Disasters Index (NDI) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​D​It=Lt0.1−Lt−10.1,t=1,⋯,T=552.formulae-sequence𝑁𝐷subscript𝐼𝑡superscriptsubscript𝐿𝑡0.1superscriptsubscript𝐿𝑡10.1formulae-sequence𝑡  1⋯𝑇552NDI\_{t}=L\_{t}^{0.1}-L\_{t-1}^{0.1},\;\;\;\;\;\;\;\;\;\;\;\;\;\;t=1,\cdots,T=552. |  | (1) |

![Refer to caption](/html/2008.03672/assets/x7.png)


Figure 2: Our proposed Natural Disasters Index (NDI) for the United States. This NDI ([1](#S2.E1 "In 2 Construction of the Natural Disasters Index (NDI) ‣ A Natural Disasters Index")) is constructed using the property losses of natural disasters reported in NOAA Storm Data (NCEI, [2018](#bib.bib33)) between 1996 and 2018.

For stress testing in section [5](#S5 "5 Stress Testing Analysis for the NDI ‣ A Natural Disasters Index"), we utilize monthly maximum temperatures and the Palmer Drought Severity Index (PDSI) used in the U.S. Climate Extremes Index (CEI) (NCEI, [2019](#bib.bib34); Palmer, [1965](#bib.bib36); Gleason et al., [2008](#bib.bib19)).
We define the reported highest temperature for each month in the U.S. as the monthly maximum temperature (measured in Fahrenheit) (Menne
et al., [2009](#bib.bib30); Vose
et al., [2014](#bib.bib44)).
PDSI is a measurement of severity of drought in a region for a given period (Heim Jr, [2002](#bib.bib21); Alley, [1984](#bib.bib3)). We use the monthly PDSI in the U.S. that assigns a value in [-4,4] on a decreasing degree of dryness (i.e., the extremely dry condition and extremely wet condition provides -4 and 4, respectively) (Heddinghaus and
Sabol, [1991](#bib.bib20)). Figure [3](#S2.F3 "Figure 3 ‣ 2 Construction of the Natural Disasters Index (NDI) ‣ A Natural Disasters Index") depicts that the first differences of both stress testing variables yield stationary time series.

![Refer to caption](/html/2008.03672/assets/x8.png)

![Refer to caption](/html/2008.03672/assets/x9.png)

Figure 3: The first differences of the stress testing variables, (a) Maximum Temperature (Max Temp) and (b) Palmer Drought Severity Index (PDSI), yield stationary time series, generated using NCEI ([2020b](#bib.bib32)) between 1996 and 2018.

## 3 NDI Option Prices

Standard insurance and reinsurance systems encounter difficulties in reimbursing the extremely high losses caused by natural disasters.
Insurance companies seek more reliable approaches for hedging and transferring these types of intensive risks to capital market investors.
Catastrophe risk bonds (CAT bonds) are one of the most important types of Insurance-Linked-Securities used to accomplish this.
Our proposed NDI is intended to assess the degree of future systemic risk caused by natural disasters.
Therefore, we determine a proper model for pricing the NDI options in this section.

Options can be used for hedging, speculating, and gauging risk.
The Black-Scholes model, binomial option pricing model, trinomial tree, Monte Carlo simulation, and finite difference model are the conventional methods in option pricing. Recently, the discrete stochastic volatility based model was introduced to compute option prices and explain some well-known mispricing phenomena.
Furthermore, Duan ([1995](#bib.bib15)) proposes the application of discrete-time Generalized AutoRegressive Conditional Heteroskedasticity (GARCH) to price options. We extend his work by considering the standard GARCH model with Generalized Hyperbolic (GH) innovations to compute the fair values of the NDI options. We assume that the dynamic returns ([1](#S2.E1 "In 2 Construction of the Natural Disasters Index (NDI) ‣ A Natural Disasters Index")) follow the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=log⁡N​D​ItN​D​It−1=rt′+λ0​at−12​at+at​ϵt,subscript𝑅𝑡𝑁𝐷subscript𝐼𝑡𝑁𝐷subscript𝐼𝑡1subscriptsuperscript𝑟′𝑡subscript𝜆0subscript𝑎𝑡12subscript𝑎𝑡subscript𝑎𝑡subscriptitalic-ϵ𝑡R\_{t}=\log{\frac{NDI\_{t}}{NDI\_{t-1}}}=r^{\prime}\_{t}+\lambda\_{0}\sqrt{a\_{t}}-\frac{1}{2}a\_{t}+\sqrt{a\_{t}}\epsilon\_{t}, |  | (2) |

where rt′subscriptsuperscript𝑟′𝑡r^{\prime}\_{t} and ϵtsubscriptitalic-ϵ𝑡\epsilon\_{t} are the risk-less rate of return and standardized residual during the time period t𝑡t, respectively, λ0subscript𝜆0\lambda\_{0} denotes the risk premium for the NDI, and atsubscript𝑎𝑡a\_{t} is the conditional variance of returns (Rtsubscript𝑅𝑡R\_{t}) given the information set consisting of all linear functions of the past returns available during the time period t−1𝑡1t-1 (Ft−1subscript𝐹𝑡1F\_{t-1}), i.e., at=v​a​r​(Rt∣Ft−1)subscript𝑎𝑡𝑣𝑎𝑟conditionalsubscript𝑅𝑡subscript𝐹𝑡1a\_{t}=var\left(R\_{t}\mid F\_{t-1}\right). We use the standard GARCH(1,1) to model

|  |  |  |  |
| --- | --- | --- | --- |
|  | at2=m+a​at−12+b​ϵt−12,subscriptsuperscript𝑎2𝑡𝑚𝑎subscriptsuperscript𝑎2𝑡1𝑏superscriptsubscriptitalic-ϵ𝑡12a^{2}\_{t}=m+a\,a^{2}\_{t-1}+b\,\epsilon\_{t-1}^{2}, |  | (3) |

where m𝑚m (constant), a𝑎a, and b𝑏b are non-negative parameters of the model; each of these variables is to be estimated from the data. We assume the standardized residuals (ϵtsubscriptitalic-ϵ𝑡\epsilon\_{t}) are independent and identically distributed G​H​(λ,α,β,δ,μ)𝐺𝐻𝜆𝛼𝛽𝛿𝜇GH\left(\lambda,\alpha,\beta,\delta,\mu\right).
According to Blaesild ([1981](#bib.bib8)), Rtsubscript𝑅𝑡R\_{t} for given Ft−1subscript𝐹𝑡1F\_{t-1} is distributed on real world probability space (ℙ)\mathbb{P}) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt∼G​H​(λ,αat,βat,δ​at,rt′+mt+μ​at),mt=λ0​at−12​at.formulae-sequencesimilar-tosubscript𝑅𝑡𝐺𝐻𝜆𝛼subscript𝑎𝑡𝛽subscript𝑎𝑡𝛿subscript𝑎𝑡subscriptsuperscript𝑟′𝑡subscript𝑚𝑡𝜇subscript𝑎𝑡subscript𝑚𝑡subscript𝜆0subscript𝑎𝑡12subscript𝑎𝑡R\_{t}\sim GH\left(\lambda,\frac{\alpha}{\sqrt{a\_{t}}},\;\frac{\beta}{\sqrt{a\_{t}}},\;\delta\sqrt{a\_{t}},\;r^{\prime}\_{t}+m\_{t}+\mu\sqrt{a\_{t}}\right),\;\;\;\;m\_{t}=\lambda\_{0}\sqrt{a\_{t}}-\frac{1}{2}a\_{t}. |  | (4) |

The Esscher transformation given in Gerber and
Shiu ([1994](#bib.bib17)) is the conventional method of identifying an equivalent martingale measure to obtain a consistent price for options. Using the Esscher transformation, Chorro ([2012](#bib.bib10)) found that Rtsubscript𝑅𝑡R\_{t} for given Ft−1subscript𝐹𝑡1F\_{t-1} is distributed on the risk-neutral probability (ℚℚ\mathbb{Q}) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt∼G​H​(λ,αat,βat+θt,δ​at,rt′+mt+μ​at),similar-tosubscript𝑅𝑡𝐺𝐻𝜆𝛼subscript𝑎𝑡𝛽subscript𝑎𝑡subscript𝜃𝑡𝛿subscript𝑎𝑡subscriptsuperscript𝑟′𝑡subscript𝑚𝑡𝜇subscript𝑎𝑡R\_{t}\sim GH\left(\lambda,\frac{\alpha}{\sqrt{a\_{t}}},\frac{\beta}{\sqrt{a\_{t}}}+\theta\_{t},\delta\sqrt{a\_{t}},r^{\prime}\_{t}+m\_{t}+\mu\sqrt{a\_{t}}\right), |  | (5) |

where θtsubscript𝜃𝑡\theta\_{t} is the solution to M​G​F​(1+θt)=M​G​F​(θt)​ert′𝑀𝐺𝐹1subscript𝜃𝑡𝑀𝐺𝐹subscript𝜃𝑡superscript𝑒subscriptsuperscript𝑟′𝑡MGF\left(1+\theta\_{t}\right)=MGF\left(\theta\_{t}\right)\,e^{r^{\prime}\_{t}}, and M​G​F𝑀𝐺𝐹MGF is the conditional moment generating function of Rt+1subscript𝑅𝑡1R\_{t+1} given Ftsubscript𝐹𝑡F\_{t}.

We generate future values of the NDI to price its call and put options using the Monte Carlo simulations (Chorro, [2012](#bib.bib10)) as follows:

1. 1.

   Fitting GARCH(1,1) with Normal Inverse Gaussian (NIG) innovations to Lt0.1superscriptsubscript𝐿𝑡0.1L\_{t}^{0.1} and forecasting a12superscriptsubscript𝑎12a\_{1}^{2} (we set t=1𝑡1t=1).
2. 2.

   Beginning from t=2𝑡2t=2, repeat the steps (a)-(c) for t=3,4,…,T𝑡
   34…𝑇t=3,4,...,T, where T𝑇T is time to maturity of the NDI call option.

   1. (a)

      Estimating the parameter θtsubscript𝜃𝑡\theta\_{t} using M​G​F​(1+θt)=M​G​F​(θt)​ert′𝑀𝐺𝐹1subscript𝜃𝑡𝑀𝐺𝐹subscript𝜃𝑡superscript𝑒subscriptsuperscript𝑟′𝑡MGF\left(1+\theta\_{t}\right)=MGF\left(\theta\_{t}\right)\,e^{r^{\prime}\_{t}}, where M​G​F𝑀𝐺𝐹MGF is the conditional moment generating function of Rt+1subscript𝑅𝑡1R\_{t+1} given Ftsubscript𝐹𝑡F\_{t} on ℙℙ\mathbb{P}.
   2. (b)

      Finding an equivalent distribution function for ϵtsubscriptitalic-ϵ𝑡\epsilon\_{t} on ℚℚ\mathbb{Q} and generate the value of ϵt+1subscriptitalic-ϵ𝑡1\epsilon\_{t+1} under the assumption ϵt∼G​H​(λ,α,β+at​θt,δ,μ)similar-tosubscriptitalic-ϵ𝑡𝐺𝐻𝜆𝛼𝛽subscript𝑎𝑡subscript𝜃𝑡𝛿𝜇\epsilon\_{t}\sim GH(\lambda,\alpha,\beta+\sqrt{a\_{t}}\theta\_{t},\delta,\mu) on ℚℚ\mathbb{Q}.
   3. (c)

      Computing the values of Rt+1subscript𝑅𝑡1R\_{t+1} and at+1subscript𝑎𝑡1a\_{t+1} using ([2](#S3.E2 "In 3 NDI Option Prices ‣ A Natural Disasters Index")) and ([3](#S3.E3 "In 3 NDI Option Prices ‣ A Natural Disasters Index")).
3. 3.

   Generating future values of Lt0.1superscriptsubscript𝐿𝑡0.1L\_{t}^{0.1} for t=1,….,Tt=1,....,T on ℚℚ\mathbb{Q} where T𝑇T is the time to maturity. Recursively, future values of the NDI is obtained by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | N​D​It=Rt10+N​D​It−1.𝑁𝐷subscript𝐼𝑡superscriptsubscript𝑅𝑡10𝑁𝐷subscript𝐼𝑡1NDI\_{t}=R\_{t}^{10}+NDI\_{t-1}. |  | (6) |
4. 4.

   Repeating steps 2 and 3 for 10,000 (N𝑁N) times to simulate N𝑁N paths to compute future values of the NDI.

Then, the Monte Carlo averages approximate future values of the NDI at time t𝑡t for a given strike price K𝐾K to price its call and put options (C^^𝐶\hat{C} and P^^𝑃\hat{P}, respectively)

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^​(t,T,K)=1N​e−rt′​(T−t)​∑i=1N(N​D​IT(i)−K)+,^𝐶𝑡𝑇𝐾1𝑁superscript𝑒subscriptsuperscript𝑟′𝑡𝑇𝑡superscriptsubscript𝑖1𝑁subscript𝑁𝐷subscriptsuperscript𝐼𝑖𝑇𝐾\hat{C}\left(t,T,K\right)=\frac{1}{N}\,e^{-r^{\prime}\_{t}(T-t)}\sum\_{i=1}^{N}\left(NDI^{(i)}\_{T}-K\right)\_{+}\ ,\\ |  | (7) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | P^​(t,T,K)=1N​e−rt′​(T−t)​∑i=1N(K−N​D​IT(i))+.^𝑃𝑡𝑇𝐾1𝑁superscript𝑒subscriptsuperscript𝑟′𝑡𝑇𝑡superscriptsubscript𝑖1𝑁subscript𝐾𝑁𝐷subscriptsuperscript𝐼𝑖𝑇\hat{P}\left(t,T,K\right)=\frac{1}{N}\,e^{-r^{\prime}\_{t}(T-t)}\sum\_{i=1}^{N}\left(K-NDI^{(i)}\_{T}\right)\_{+}. |  | (8) |

We provide call and put option prices for the NDI (C^^𝐶\hat{C} and P^^𝑃\hat{P}) at time t𝑡t for a given strike price K𝐾K in Figure [4](#S3.F4 "Figure 4 ‣ 3 NDI Option Prices ‣ A Natural Disasters Index") and [5](#S3.F5 "Figure 5 ‣ 3 NDI Option Prices ‣ A Natural Disasters Index"), respectively.
These figures illustrate the relationship between time to maturity (T𝑇T), the strike price (K𝐾K), and option prices.
As we expected, in Figure [5](#S3.F5 "Figure 5 ‣ 3 NDI Option Prices ‣ A Natural Disasters Index") the put option price for NDI (P^^𝑃\hat{P}) increases as the strike price increases.
However, the call option price for NDI (C^^𝐶\hat{C}) increases as the strike price decreases, see Figure [4](#S3.F4 "Figure 4 ‣ 3 NDI Option Prices ‣ A Natural Disasters Index").
Figure [7](#S3.F7 "Figure 7 ‣ 3 NDI Option Prices ‣ A Natural Disasters Index") depicts the implied volatility surface against the time to maturity (T𝑇T) and moneyness (M=S/K𝑀𝑆𝐾M=S/K), where S𝑆S is the stock price.
The observed volatility surface has an inverted volatility smile which is usually seen in periods of high market stress.
Options with lower strike prices have higher implied volatilities compared to those with higher strike prices.
The highest implied volatilities of options are observed in (1.2,1.4)1.21.4(1.2,1.4) of moneyness.
The implied volatilities tend to converge to a constant as the time to maturity converges to 606060.

![Refer to caption](/html/2008.03672/assets/x10.png)


Figure 4: The call option prices ([7](#S3.E7 "In 3 NDI Option Prices ‣ A Natural Disasters Index")) for the Natural Disasters Index (NDI) at time t𝑡t for a given strike price K𝐾K using a GARCH(1,1) model with generalized hyperbolic innovations. The Monte Carlo simulations are generated using NOAA Storm Data (NCEI, [2018](#bib.bib33)) between 1996 and 2018.

![Refer to caption](/html/2008.03672/assets/x11.png)


Figure 5: The put option prices ([8](#S3.E8 "In 3 NDI Option Prices ‣ A Natural Disasters Index")) for the Natural Disasters Index (NDI) at time t𝑡t for a given strike price K𝐾K using a GARCH(1,1) model with generalized hyperbolic innovations. The Monte Carlo simulations are generated using NOAA Storm Data (NCEI, [2018](#bib.bib33)) between 1996 and 2018.

![Refer to caption](/html/2008.03672/assets/x12.png)


Figure 6: The call and put option prices for the Natural Disasters Index (NDI) at time t𝑡t for a given strike price K𝐾K using a GARCH(1,1) model with generalized hyperbolic innovations. The Monte Carlo simulations are generated using NOAA Storm Data (NCEI, [2018](#bib.bib33)) between 1996 and 2018.

![Refer to caption](/html/2008.03672/assets/x13.png)


Figure 7: The Natural Disasters Index (NDI) implied volatilities against time to maturity (T𝑇T) and moneyness (M=S/K𝑀𝑆𝐾M=S/K, where S𝑆S and K𝐾K the stock and strike prices, respectively) using a GARCH(1,1) model with generalized hyperbolic innovations. The Monte Carlo simulations are generated using NOAA Storm Data (NCEI, [2018](#bib.bib33)) between 1996 and 2018.

## 4 NDI Risk Budgets

The risk budgets help investors as they provide the risk contributions of each component in the portfolio to the aggregate portfolio risk. To accomplish this, an investor should determine the relationships among various factors. Then, the investor can envision the amount of risk exposure (as partly) depending on the behavior of each component position. The primary strategies of assessing the center risk and tail risk contributions are portfolio standard deviation (Std), Value at Risk (VaR), and Expected Tail Loss (ETL) budgets. Some recent research applied Std and VaR for portfolio risk budgeting 111See Chow and
Kritzman ([2001](#bib.bib11)), Litterman ([1996](#bib.bib26)), Maillard
et al. ([2010](#bib.bib28)), and Peterson and
Boudt ([2008](#bib.bib37)). and ETL budgets are used in Boudt
et al. ([2013](#bib.bib9)). As Std and ETL are coherent risk measures, we use them as the investment strategies for our equal-weighted portfolio.

We delineate the marginal risk and risk contribution of each asset in the portfolio. We define a risk measure, R(.)R(.), on the portfolio weight vector, w=(w1,w2,…,wn)wsubscript𝑤1subscript𝑤2…subscript𝑤𝑛\textbf{w}=(w\_{1},w\_{2},...,w\_{n}) where wi=1nsubscript𝑤𝑖1𝑛w\_{i}=\frac{1}{n} (R​(w):ℝn→ℝ:𝑅𝑤→superscriptℝ𝑛ℝR(w):\mathbb{R}^{n}\rightarrow\mathbb{R}). Then, the marginal contribution to risk (MCTR) of the i𝑖ith asset to the total portfolio risk is

|  |  |  |  |
| --- | --- | --- | --- |
|  | MCTRi​(w)=wi​∂R​(w)∂wi.subscriptMCTR𝑖wsubscript𝑤𝑖𝑅wsubscript𝑤𝑖\textit{MCTR}\_{i}(\textbf{w})=w\_{i}\frac{\partial R(\textbf{w})}{\partial w\_{i}}. |  | (9) |

The MCTR of the k𝑘kth subset is

|  |  |  |  |
| --- | --- | --- | --- |
|  | MCTRMk​(w)=∑i∈MkMCTRi​(w),subscriptMCTRsubscript𝑀𝑘wsubscript𝑖subscript𝑀𝑘subscriptMCTR𝑖w\textit{MCTR}\_{M\_{k}}(\textbf{w})=\sum\_{i\in M\_{k}}\textit{MCTR}\_{i}(\textbf{w}), |  | (10) |

where Mk⊆{1,2,…,n}subscript𝑀𝑘12…𝑛M\_{k}\,\,\subseteq\,\left\{1,2,...,n\right\} denote s𝑠s subsets of portfolio assets. The percent contribution to risk (PCTR) of the i𝑖ith asset to the total portfolio risk is

|  |  |  |  |
| --- | --- | --- | --- |
|  | PCTRi​(w)=MCTRi​(w)∑i=1nMCTRi​(w).subscriptPCTR𝑖wsubscriptMCTR𝑖wsuperscriptsubscript𝑖1𝑛subscriptMCTR𝑖w\textit{PCTR}\_{i}(\textbf{w})=\frac{\textit{MCTR}\_{i}(\textbf{w})}{\sum\_{i=1}^{n}\textit{MCTR}\_{i}(\textbf{w})}. |  | (11) |

Since a large number of observations are involved in our analysis, we use a rolling-method for risk budgeting. We use the first 400 data (biweekly loss returns) at each window as in-sample-data and the last 400 data as out-of-sample data. The results of the rolling method for finding risk contributions across the time are depicted in Figures [8](#S4.F8 "Figure 8 ‣ 4 NDI Risk Budgets ‣ A Natural Disasters Index")-[10](#S4.F10 "Figure 10 ‣ 4 NDI Risk Budgets ‣ A Natural Disasters Index").
We calculate Std and ETL for risk contributions in our portfolio. Table LABEL:tab:risk\_budget reports the estimated risk allocations within the equal-weighted portfolio. According to the results, the main center risk contributors are tornado, tropical storm, flood, ice storm, and flash flood. However, flash flood, flood, and wildfire are the main tail risk contributors at 95%percent9595\% level. Thus, flash flood and flood are the main risk contributors in our portfolio. Among center risk contributors, tornado is one of the tail risk diversifiers in our portfolio with a negative tail risk contribution at 99%percent9999\% level.

Table 1: The standard deviation (Std) and expected tail loss (ETL) (at 95% and 99% levels) risk budgets for the Natural Disasters Index (NDI). Marginal contribution to risk and the percent contribution to risk are given by MCTR ([9](#S4.E9 "In 4 NDI Risk Budgets ‣ A Natural Disasters Index")) and PCTR ([10](#S4.E10 "In 4 NDI Risk Budgets ‣ A Natural Disasters Index")), respectively.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Severe Weather Event | |  | | --- | | MCTR | | ETL (95) | | |  | | --- | | PCTR | | ETL (95) | | |  | | --- | | MCTR | | ETL (99) | | |  | | --- | | PCTR | | ETL (99) | | |  | | --- | | MCTR | | Std | | |  | | --- | | PCTR | | Std | |
| Marine Lightning | 0.0002 | 0.01% | 0.0004 | 0.02% | 0.0365 | 0.21% |
| Marine Dense Fog | 0.0003 | 0.02% | 0.0006 | 0.03% | 0.0552 | 0.32% |
| Tornado | 0.0076 | 0.49% | -0.0219 | -1.13% | 0.7692 | 4.49% |
| Blizzard | 0.0076 | 0.49% | 0.0379 | 1.96% | 0.6046 | 3.53% |
| Dense Smoke | 0.0088 | 0.57% | 0.0183 | 0.94% | 0.0562 | 0.33% |
| Volcanic Ash | 0.0104 | 0.68% | 0.0214 | 1.10% | 0.0624 | 0.36% |
| Marine Hurricane Typhoon | 0.0121 | 0.78% | 0.0241 | 1.24% | 0.1039 | 0.61% |
| Sleet | 0.0122 | 0.79% | 0.0241 | 1.24% | 0.0917 | 0.54% |
| Marine Hail | 0.0124 | 0.80% | 0.0226 | 1.16% | 0.0631 | 0.37% |
| Winter Storm | 0.0162 | 1.05% | 0.0373 | 1.92% | 0.5815 | 3.40% |
| Marine Strong Wind | 0.0166 | 1.08% | 0.0305 | 1.57% | 0.1070 | 0.62% |
| Rip Current | 0.0187 | 1.21% | 0.0301 | 1.55% | 0.0940 | 0.55% |
| Funnel Cloud | 0.0202 | 1.31% | 0.0318 | 1.64% | 0.0680 | 0.40% |
| Seiche | 0.0204 | 1.32% | 0.0359 | 1.85% | 0.1343 | 0.78% |
| High Surf | 0.0206 | 1.33% | 0.0409 | 2.11% | 0.5224 | 3.05% |
| Avalanche | 0.0223 | 1.44% | 0.0359 | 1.85% | 0.1964 | 1.15% |
| Dust Devil | 0.0233 | 1.51% | 0.0352 | 1.82% | 0.1287 | 0.75% |
| Heavy Snow | 0.0243 | 1.58% | 0.0555 | 2.86% | 0.4441 | 2.59% |
| Hail | 0.0244 | 1.58% | 0.0193 | 0.99% | 0.5757 | 3.36% |
| Thunderstorm Wind | 0.0252 | 1.63% | 0.0184 | 0.95% | 0.5072 | 2.96% |
| Ice Storm | 0.0254 | 1.64% | 0.0367 | 1.89% | 0.7052 | 4.12% |
| Freezing Fog | 0.0256 | 1.66% | 0.0436 | 2.25% | 0.1156 | 0.67% |
| Dust Storm | 0.0257 | 1.66% | 0.0281 | 1.45% | 0.2943 | 1.72% |
| Waterspout | 0.0259 | 1.68% | 0.0396 | 2.04% | 0.1509 | 0.88% |
| Strong Wind | 0.0290 | 1.88% | 0.0359 | 1.85% | 0.4462 | 2.61% |
| Marine Thunderstorm Wind | 0.0292 | 1.89% | 0.0298 | 1.54% | 0.2261 | 1.32% |
| Marine High Wind | 0.0321 | 2.08% | 0.0439 | 2.26% | 0.1578 | 0.92% |
| Excessive Heat | 0.0325 | 2.11% | 0.0486 | 2.51% | 0.1057 | 0.62% |
| Heat | 0.0325 | 2.11% | 0.0428 | 2.20% | 0.1624 | 0.95% |
| Dense Fog | 0.0337 | 2.19% | 0.0298 | 1.54% | 0.3104 | 1.81% |
| Extreme Cold Wind Chill | 0.0350 | 2.27% | 0.0462 | 2.38% | 0.1814 | 1.06% |
| Lakeshore Flood | 0.0359 | 2.33% | 0.0577 | 2.98% | 0.1130 | 0.66% |
| Lightning | 0.0361 | 2.34% | 0.0492 | 2.54% | 0.4109 | 2.40% |
| Winter Weather | 0.0384 | 2.49% | 0.0554 | 2.85% | 0.1976 | 1.15% |
| Tropical Depression | 0.0397 | 2.58% | 0.0567 | 2.92% | 0.1816 | 1.06% |
| Storm Surge Tide | 0.0398 | 2.58% | 0.0402 | 2.07% | 1.0165 | 5.94% |
| Frost Freeze | 0.0403 | 2.61% | 0.0630 | 3.25% | 0.1570 | 0.92% |
| Lake Effect Snow | 0.0405 | 2.63% | 0.0589 | 3.04% | 0.2124 | 1.24% |
| Tsunami | 0.0406 | 2.63% | 0.0678 | 3.49% | 0.1143 | 0.67% |
| Cold Wind Chill | 0.0428 | 2.77% | 0.0549 | 2.83% | 0.1072 | 0.63% |
| High Wind | 0.0437 | 2.83% | 0.0355 | 1.83% | 0.8385 | 4.90% |
| Heavy Rain | 0.0439 | 2.84% | 0.0240 | 1.24% | 0.5813 | 3.39% |
| Coastal Flood | 0.0455 | 2.95% | 0.0877 | 4.52% | 0.5504 | 3.21% |
| Debris Flow | 0.0486 | 3.15% | 0.0568 | 2.93% | 0.3216 | 1.88% |
| Hurricane Typhoon | 0.0486 | 3.15% | 0.0376 | 1.94% | 0.9643 | 5.63% |
| Drought | 0.0524 | 3.40% | 0.0416 | 2.14% | 0.4786 | 2.79% |
| Tropical Storm | 0.0598 | 3.88% | 0.0509 | 2.62% | 0.8305 | 4.85% |
| Wildfire | 0.0639 | 4.14% | 0.0678 | 3.50% | 0.5399 | 3.15% |
| Flood | 0.0752 | 4.87% | 0.0512 | 2.64% | 0.7292 | 4.26% |
| Flash Flood | 0.0766 | 4.96% | 0.0598 | 3.08% | 0.7210 | 4.21% |

![Refer to caption](/html/2008.03672/assets/x14.png)


Figure 8: The percent contribution to risk (PCTR) of the expected tail loss (ETL) risk budgets for the Natural Disasters Index (NDI) at 95% level. The legend depicts the severe weather events in ascending order of their PCTR of ETL risk budgets at 95% level. The results are generated from NOAA Storm Data (NCEI, [2018](#bib.bib33)) between 1996 and 2018.

![Refer to caption](/html/2008.03672/assets/x15.png)


Figure 9: The percent contribution to risk (PCTR) of the expected tail loss (ETL) risk budgets for the Natural Disasters Index (NDI) at 99% level. The legend depicts the severe weather events in ascending order of their PCTR of ETL risk budgets at 99% level. The results are generated from NOAA Storm Data (NCEI, [2018](#bib.bib33)) between 1996 and 2018.

![Refer to caption](/html/2008.03672/assets/x16.png)


Figure 10: The percent contribution to risk (PCTR) of the standard deviation (Std) risk budgets for the Natural Disasters Index (NDI). The legend depicts the severe weather events in ascending order of their PCTR of Std risk budgets. The results are generated from NOAA Storm Data (NCEI, [2018](#bib.bib33)) between 1996 and 2018.

## 5 Stress Testing Analysis for the NDI

In finance, stress testing is an analysis intended to determine the strength of a financial instrument and its resilience to the economic crisis. Stress testing is a form of scenario analysis used by regulators to investigate the robustness of a financial instrument is in inevitable crashes. In risk management, this helps to determine portfolio risks and serves as a tool for hedging strategies required to mitigate against potential losses.

In this section, we assess the performance of the NDI via stress testing using monthly maximum temperature (Max Temp) and the Palmer Drought Severity Index (PDSI) as stressors (refer to section [2](#S2 "2 Construction of the Natural Disasters Index (NDI) ‣ A Natural Disasters Index")).
Instead of working with each factor, we use the first differences of them as returns that yield stationary time series, see Figure [3](#S2.F3 "Figure 3 ‣ 2 Construction of the Natural Disasters Index (NDI) ‣ A Natural Disasters Index").

The two series of returns inherit serial correlation and dependence according to the results of Ljung-Box test results (p-values are less than 0.05).
Thus, to capture linear and nonlinear dependencies in data sets, we put the series through the ARMA(1,1)-GARCH(1,1) filter with Student-t innovations. Then, we consider the sample innovations obtained from the aforementioned filter for our analysis.

We fit bivariate NIG models to the joint distributions of independent and identically distributed standardized residuals of each factor and the NDI (Total Loss): Max Temp vs NDI and PSDI vs NDI.
Then, we simulate 10,000 values from the models of factors to perform the scenario analysis and to compute the systemic risk measures.
Figure [11](#S5.F11 "Figure 11 ‣ 5 Stress Testing Analysis for the NDI ‣ A Natural Disasters Index") shows the fitted contour plots from each model, overlaid with the 10,000 simulated values. The empirical correlation coefficients based on the observed data suggest a weak positive relationship between the factors and the NDI (R≃0.155)similar-to-or-equals𝑅0.155(R\simeq 0.155).

![Refer to caption](/html/2008.03672/assets/x17.png)

![Refer to caption](/html/2008.03672/assets/x18.png)

Figure 11: The generated joint densities of the returns of monthly maximum temperature (Max Temp) and the Natural Disasters Index (NDI), and the Palmer Drought Severity Index (PDSI) and the NDI (right panel) using the fitted bivariate NIG models of the joint distributions of independent and identically distributed standardized residuals. The figures depict the simulated values and the contour plots of the joint densities.

There are various measures of systemic risk used to assess the impact of negative events on the stress factors. Adrian and
Brunnermeier ([2011](#bib.bib2)) proposed Conditional Value-at-Risk (CoVaR): the change in the value at risk of the financial system conditional on an institution being under distress relative to its median state. Girardi and
Ergun ([2013](#bib.bib18)) improved the definition of financial distress from an institution being exactly at its VaR to being at most at its VaR (CoVaR). As the CoVaR is a coherent risk measure (see Acerbi and
Tasche, [2002](#bib.bib1)), changing VaR to CoVaR allows us to consider more severe distress events, back-test CoVaR, and improve its monotonicity concerning the dependence parameter. The definition of CoVaR by Girardi and
Ergun ([2013](#bib.bib18)) was based on the conditional distribution of a random variable Y𝑌Y given a stress event for a random variable X𝑋X. Mainik and
Schaanning ([2014](#bib.bib29)) defined an alternative CoVaR notion in terms of copulas. They showed that conditioning on X≤V​a​Rα​(X)𝑋𝑉𝑎subscript𝑅𝛼𝑋X\leq VaR\_{\alpha}(X) improves the response to dependence between X𝑋X and Y𝑌Y compared to conditioning on X=V​a​Rα​(X)𝑋𝑉𝑎subscript𝑅𝛼𝑋X=VaR\_{\alpha}(X). Therefore, we use the variant of CoVaR developed by Mainik and
Schaanning ([2014](#bib.bib29)) for our study.

We define the distributions of Y𝑌Y and X𝑋X are given by FYsubscript𝐹𝑌F\_{Y} and FXsubscript𝐹𝑋F\_{X}, respectively, and FY|Xsubscript𝐹conditional𝑌𝑋F\_{Y|X} is the conditional distribution of Y𝑌Y given X𝑋X. Then, CoVaR
at level q𝑞q, CoVaRqsubscriptCoVaR𝑞\text{CoVaR}\_{q} (or ξqsubscript𝜉𝑞\xi\_{q}), is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξq:=CoVaRq:=FY|X≤FX−1​(q)−1​(q)=VaRq​(Y|X≤VaRq​(X)),assignsubscript𝜉𝑞subscriptCoVaR𝑞assignsubscriptsuperscript𝐹1conditional𝑌𝑋subscriptsuperscript𝐹1𝑋𝑞𝑞subscriptVaR𝑞conditional𝑌𝑋subscriptVaR𝑞𝑋\xi\_{q}:=\text{CoVaR}\_{q}:=F^{-1}\_{Y|X\leq F^{-1}\_{X}(q)}\left(q\right)=\text{VaR}\_{q}\left(Y|X\leq\text{VaR}\_{q}(X)\right), |  | (12) |

where VaRq​(X)subscriptVaR𝑞𝑋\text{VaR}\_{q}\left(X\right) denotes the VaR of X𝑋X at level q𝑞q, which is same as the q𝑞qth quantile of X𝑋X (FX−1​(q)subscriptsuperscript𝐹1𝑋𝑞F^{-1}\_{X}(q)). In Mainik and
Schaanning ([2014](#bib.bib29)), CoVar for the closely associated Expected Shortfall (ES) is defined as the tail mean beyond VaR:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CoESq:=𝔼​(Y|Y≤ξq,X≤VaRq​(X)).assignsubscriptCoES𝑞𝔼formulae-sequenceconditional𝑌𝑌subscript𝜉𝑞𝑋subscriptVaR𝑞𝑋\text{CoES}\_{q}:=\mathbb{E}\left(Y|Y\leq\xi\_{q},X\leq\text{VaR}\_{q}(X)\right). |  | (13) |

Furthermore, Biglova
et al. ([2014](#bib.bib7)) has proposed

|  |  |  |  |
| --- | --- | --- | --- |
|  | CoETLq:=𝔼​(Y|Y≤VaRq​(Y),X≤VaRq​(X)).assignsubscriptCoETL𝑞𝔼formulae-sequenceconditional𝑌𝑌subscriptVaR𝑞𝑌𝑋subscriptVaR𝑞𝑋\text{CoETL}\_{q}:=\mathbb{E}\left(Y|Y\leq\text{VaR}\_{q}(Y),X\leq\text{VaR}\_{q}(X)\right). |  | (14) |

Table [2](#S5.T2 "Table 2 ‣ 5 Stress Testing Analysis for the NDI ‣ A Natural Disasters Index") reports the left-tail systemic risk measures on the NDI at different levels based on stressing the factors (Max Temp and PDSI).
At 5% and 10% stress levels, stress on Max Temp seems to have a marginally more meaningful impact on the NDI than the stress on PDSI. However, at the highest stress level (1%), the results show stress on Max Temp has a greater significant impact on the NDI compared to that of PDSI.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Stress Factors | Stress Levels | Risk Measure on the NDI (Left Tail) | | |
| CoVaR | CoES | CoETL |
| Max Temp | 10% | -1.868 | -2.527 | -2.027 |
| 5% | -2.472 | -3.324 | -2.469 |
| 1% | -4.568 | -5.305 | -3.756 |
| PDSI | 10% | -1.348 | -2.368 | -1.551 |
| 5% | -2.221 | -4.001 | -2.159 |
| 1% | -7.863 | -17.625 | -4.265 |

Table 2: The left-tail systemic risk measures (CoVaR, CoES, and CoETL) on the Natural Disasters Index (NDI) at different stress levels based on stressing the factors monthly maximum temperature (Max Temp) and the Palmer Drought Severity Index (PDSI).

## 6 Discussion and Conclusion

We proposed the Natural Disasters Index, NDI ([1](#S2.E1 "In 2 Construction of the Natural Disasters Index (NDI) ‣ A Natural Disasters Index")), using the United States as a model with property losses reported in NOAA Storm Data (NCEI, [2018](#bib.bib33)) between 1996 and 2018.
In order to establish the NDI, we provided an evaluation framework using three promising approaches: (1) option pricing, (2) risk budgeting, and (3) stress testing.

We determined the fair values of the NDI options using a discrete-time GARCH model with GH innovations and then simulated Monte Carlo averages to approximate call and put option prices ([7](#S3.E7 "In 3 NDI Option Prices ‣ A Natural Disasters Index")),([8](#S3.E8 "In 3 NDI Option Prices ‣ A Natural Disasters Index")).
The relationships among time to maturity, strike price, and option prices help to construct and valuate insurance-type financial instruments.
Then, we disaggregated the cumulative risk attributed to natural disasters to our equally-weighted portfolio (i.e., we investigated the risk contribution of each type of natural disaster).
The Std and ETL risk budgets for the NDI yield that flood and flash flood are the main risk contributors in our portfolio.
Finally, we assessed the performance of the NDI via a stress testing analysis using Max Temp and PDSI as stressors.
We found the stress on Max Temp significantly impacts the NDI compared to that of the PDSI at the highest stress level (1%).

The proposed NDI is an attempt to address a financial instrument for hedging the intrinsic risk induced by the property losses caused by natural disasters in the United States.
The main objective of the NDI is to forecast the degree of future systemic risk caused by natural disasters.
This information could forewarn the insurers and corporations allowing them to transfer insurance risk to capital market investors.
Hence the issuance of the NDI will conspicuously help to bridge the gap between the capital and insurance markets.
While the NDI is specifically constructed for the United States, it could be modified to calculate the risk in other regions or countries using a data set comparable to NOAA Storm Data NCEI ([2018](#bib.bib33)).

## References

* Acerbi and
  Tasche (2002)

  Acerbi, C. and D. Tasche (2002).
  Expected shortfall: a natural coherent alternative to value at risk.
  Economic notes 31(2), 379–388.
* Adrian and
  Brunnermeier (2011)

  Adrian, T. and M. K. Brunnermeier (2011).
  Covar.
  Technical report, National Bureau of Economic Research.
* Alley (1984)

  Alley, W. M. (1984).
  The palmer drought severity index: limitations and assumptions.
  Journal of climate and applied meteorology 23(7),
  1100–1109.
* Barnett and
  Mahul (2007)

  Barnett, B. J. and O. Mahul (2007).
  Weather index insurance for agriculture and rural areas in
  lower-income countries.
  American Journal of Agricultural Economics 89(5),
  1241–1247.
* Bell
  et al. (2018)

  Bell, J. E., C. L. Brown, K. Conlon, S. Herring, K. E. Kunkel, J. Lawrimore,
  G. Luber, C. Schreck, A. Smith, and C. Uejio (2018).
  Changes in extreme events and the potential impacts on human health.
  Journal of the Air & Waste Management Association 68(4), 265–287.
* Biagini
  et al. (2008)

  Biagini, F., Y. Bregman, and T. Meyer-Brandis (2008).
  Pricing of catastrophe insurance options written on a loss index with
  reestimation.
  Insurance: Mathematics and Economics 43(2), 214–222.
* Biglova
  et al. (2014)

  Biglova, A., S. Ortobelli, and F. Fabozzi (2014).
  Portfolio selection in the presence of systemic risk.
  Journal of Asset Management 15, 285–299.
* Blaesild (1981)

  Blaesild, P. (1981).
  The two-dimensional hyperbolic distribution and related distributions
  with an application to johannsen’s bean data.
  Mathematical Finance 68, 251–263.
* Boudt
  et al. (2013)

  Boudt, K., P. Carl, and B. G. Peterson (2013).
  Asset allocation with conditional value-at-risk budgets.
  Journal of Risk 15(3), 39–68.
* Chorro (2012)

  Chorro, C. (2012).
  Option pricing for garch-type models with generalized hyperbolic
  innovations.
  Quantitative Finance 12(7), 1079–1094.
* Chow and
  Kritzman (2001)

  Chow, G. and M. Kritzman (2001).
  Risk budgets.
  Journal of Portfolio Management, 56–60.
* Christensen and
  Schmidli (2000)

  Christensen, C. V. and H. Schmidli (2000).
  Pricing catastrophe insurance products based on actually reported
  claims.
  Insurance: Mathematics and Economics 27(2), 189–200.
* Cummins
  et al. (2004)

  Cummins, J. D., D. Lalonde, and R. D. Phillips (2004).
  The basis risk of catastrophic-loss index securities.
  Journal of Financial Economics 71(1), 77–111.
* Dilley et al. (2005)

  Dilley, M., R. S. Chen, U. Deichmann, A. L. Lerner-Lam, and M. Arnold (2005).
  Natural disaster hotspots: a global risk analysis.
  The World Bank.
* Duan (1995)

  Duan, J. (1995).
  The garch option pricing model.
  Mathematical Finance 5, 13–32.
* Ganderton et al. (2000)

  Ganderton, P. T., D. S. Brookshire, M. McKee, S. Stewart, and H. Thurston
  (2000).
  Buying insurance for disaster-type risks: experimental evidence.
  Journal of risk and Uncertainty 20(3), 271–289.
* Gerber and
  Shiu (1994)

  Gerber, H. U. and E. S. W. Shiu (1994).
  Option pricing by esscher transforms.
  Transactions of the Society of Actuaries 46, 99–191.
* Girardi and
  Ergun (2013)

  Girardi, G. and A. T. Ergun (2013).
  Systemic risk measurement: Multivariate garch estimation of
  coVaR.
  Journal of Banking & Finance 37(8), 3169–3180.
* Gleason et al. (2008)

  Gleason, K. L., J. H. Lawrimore, D. H. Levinson, T. R. Karl, and D. J. Karoly
  (2008).
  A revised us climate extremes index.
  Journal of climate 21(10), 2124–2137.
* Heddinghaus and
  Sabol (1991)

  Heddinghaus, T. R. and P. Sabol (1991).
  A review of the palmer drought severity index and where do we go from
  here.
  In Proc. 7th Conf. on Applied Climatology, pp.  242–246.
  American Meteorological Society Boston, MA.
* Heim Jr (2002)

  Heim Jr, R. R. (2002).
  A review of twentieth-century drought indices used in the united
  states.
  Bulletin of the American Meteorological Society 83(8), 1149–1166.
* Kielholz and
  Durrer (1997)

  Kielholz, W. and A. Durrer (1997).
  Insurance derivatives and securitization: New hedging perspectives
  for the us cat insurance market.
  Geneva Papers on Risk and Insurance. Issues and Practice,
  3–16.
* Kunreuther (1996)

  Kunreuther, H. (1996).
  Mitigating disaster losses through insurance.
  Journal of risk and Uncertainty 12(2-3), 171–187.
* Lewis and
  Murdock (1996)

  Lewis, C. M. and K. C. Murdock (1996, 12).
  The role of government contracts in discretionary reinsurance markets
  for natural disasters: Abstract.
  Journal of Risk and Insurance (1986-1998) 63(4), 567.
* Liang
  et al. (2010)

  Liang, Z., L. He, and J. Wu (2010).
  Optimal dividend and reinsurance strategy of a property insurance
  company under catastrophe risk.
  arXiv preprint arXiv:1009.1269.
* Litterman (1996)

  Litterman, R. B. (1996).
  Hot spots and hedges.
  Journal of Portfolio Management, 52–75.
* Lyubchich and
  Gel (2017)

  Lyubchich, V. and Y. Gel (2017).
  Can we weather proof our insurance?
  Environmetrics 28(2), e2433.
* Maillard
  et al. (2010)

  Maillard, S., T. Roncalli, and J. Teiletche (2010).
  On the properties of equallyweighted risk contributions portfolios.
  Journal of Portfolio Management, 52–75.
* Mainik and
  Schaanning (2014)

  Mainik, G. and E. Schaanning (2014).
  On dependence consistency of covar and some other systemic risk
  measures.
  Statistics & Risk Modeling 31(1), 49–77.
* Menne
  et al. (2009)

  Menne, M. J., C. N. Williams Jr, and R. S. Vose (2009).
  The us historical climatology network monthly temperature data,
  version 2.
  Bulletin of the American Meteorological Society 90(7), 993–1008.
* Murphy (2018)

  Murphy, J. D. (2018).
  Storm data preparation.
  National Weather Service (NWS) instruction 10-1605, National Oceanic
  and Atmospheric Administration (NOAA).
* NCEI (2020b)

  NCEI (2020b).
  Climate at a Glance: National Time Series.
  National Centers for Environmental Information (NCEI), National
  Oceanic and Atmospheric Administration (NOAA).
* NCEI (2018)

  NCEI (accessed by 2018).
  Storm Events Database.
  National Centers for Environmental Information (NCEI), National
  Oceanic and Atmospheric Administration (NOAA).
* NCEI (2019)

  NCEI (accessed by 2019).
  U.S. Climate Extremes Index (CEI).
  National Centers for Environmental Information (NCEI), National
  Oceanic and Atmospheric Administration (NOAA).
* NCEI (2020a)

  NCEI (accessed by Jul 2020a).
  Billion-Dollar Weather and Climate Disasters: Overview.
  National Centers for Environmental Information.
* Palmer (1965)

  Palmer, W. C. (1965).
  Meteorological drought, Volume 30.
  US Department of Commerce, Weather Bureau.
* Peterson and
  Boudt (2008)

  Peterson, B. and K. Boudt (2008).
  Component var for a non-normal world.
  Journal of Risk, 78–81.
* Roth Sr and
  Kunreuther (1998)

  Roth Sr, R. J. and H. Kunreuther (1998).
  Paying the price: The status and role of insurance against
  natural disasters in the United States.
  Joseph Henry Press.
* Smith and
  Matthews (2015)

  Smith, A. B. and J. L. Matthews (2015).
  Quantifying uncertainty and variable sensitivity within the us
  billion-dollar weather and climate disaster cost estimates.
  Natural Hazards 77(3), 1829–1851.
* Tabuchi (2018)

  Tabuchi, H. (2018).
  2017 Set a Record for Losses From Natural Disasters. It Could
  Get Worse.
  The New York Times.
* Trindade
  et al. (2020)

  Trindade, A. A., A. Shirvani, and X. Ma (2020).
  A socioeconomic well-being index.
  arXiv preprint arXiv:2001.01036.
* Van der Vink
  et al. (1998)

  Van der Vink, G., R. M. Allen, J. Chapin, M. Crooks, W. Fraley, J. Krantz,
  A. Lavigne, A. LeCuyer, E. K. MacColl, W. Morgan, et al. (1998).
  Why the united states is becoming more vulnerable to natural
  disasters.
  Eos, Transactions American Geophysical Union 79(44),
  533–537.
* Varangis
  et al. (2003)

  Varangis, P., J. Skees, and B. Barnett (2003).
  Weather indexes for developing countries.
  Forest 4, 3–754.
* Vose
  et al. (2014)

  Vose, R. S., S. Applequist, M. Squires, I. Durre, M. J. Menne, C. N.
  Williams Jr, C. Fenimore, K. Gleason, and D. Arndt (2014).
  Improved historical temperature and precipitation time series for us
  climate divisions.
  Journal of Applied Meteorology and Climatology 53(5),
  1232–1251.
* Zangue and
  Poppo (2016)

  Zangue, N. and J. Poppo (2016).
  Evaluating catastrophe risk and cat bonds pricing methods.
  B.S. thesis, Università Ca’Foscari Venezia.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2008.03672)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2008.03672)
[View original  
on arXiv](https://arxiv.org/abs/2008.03672)[►](javascript: void(0))