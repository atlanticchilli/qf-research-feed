---
authors:
- Tetsuya Takaishi
doc_id: arxiv:2511.03314v1
family_id: arxiv:2511.03314
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Multifractality and sample size influence on Bitcoin volatility patterns
url_abs: http://arxiv.org/abs/2511.03314v1
url_html: https://arxiv.org/html/2511.03314v1
venue: arXiv q-fin
version: 1
year: 2025
---


Tetsuya Takaishi
[tt-taka@hue.ac.jp](mailto:tt-taka@hue.ac.jp)

###### Abstract

The finite sample effect on the Hurst exponent (HE) of realized volatility time series
is examined using Bitcoin data.
This study finds that the HE decreases as the sampling period Δ\Delta increases and a simple finite sample ansatz closely fits the HE data.
We obtain values of the HE as Δ→0\Delta\rightarrow 0, which are smaller than 1/2, indicating rough volatility.
The relative error is found to be 1%1\% for the widely used five-minute realized volatility.
Performing a multifractal analysis, we find the multifractality in the realized volatility time series, smaller than that of the price-return time series.

###### keywords:

Rough volatility , Hurst exponent , Finite sample effect , Multifractality

\affiliation

organization=Hiroshima University of Economics,addressline=,
city=Hiroshima,
postcode=731-0192,
state=,
country=JAPAN

## 1 Introduction

Volatility as a measure of risk is of great importance in empirical finance, especially in the risk management sector.
Forecasting future volatility is an essential task for financial institutions and practitioners
to manage financial assets safely and avoid unacceptable losses in the future.
Practically forecasting volatility is implemented by assuming models that
mimic the properties of price dynamics.
It is well-known that universal properties exist across various assets, denoted as
”stylized facts” (Cont, [2001](https://arxiv.org/html/2511.03314v1#bib.bib14)).
One of main universal properties is ”volatility clustering”.
Engle ([1982](https://arxiv.org/html/2511.03314v1#bib.bib19)) introduced the autoregressive conditional heteroscedasticity (ARCH) model
that captures the property of volatility clustering. Later the ARCH model was generalized to
GARCH model by Bollerslev ([1986](https://arxiv.org/html/2511.03314v1#bib.bib9)). Another notable property is that volatility is long-correlated, which is also related to
the fact that the absolute return |r||r| (as a proxy of volatility)
displays long autocorrelations (Ding et al., [1993](https://arxiv.org/html/2511.03314v1#bib.bib16)).
A more precise measure of volatility, realized volatility (RV) (Andersen and Bollerslev, [1998](https://arxiv.org/html/2511.03314v1#bib.bib4)), shows long-memory behavior (Andersen et al., [2001](https://arxiv.org/html/2511.03314v1#bib.bib6)).
According to these empirical findings, it is natural to include long-memory characteristics in volatility modelings.
Since long-memory time series are characterized by the Hurst exponent (HE) of H>1/2H>1/2,
the fractional volatility model (FVM)
is introduced using the fractional Brownian motion with H>1/2H>1/2(Comte and Renault, [1998](https://arxiv.org/html/2511.03314v1#bib.bib13)).

A new paradigm on volatility dynamics suggests
that ”volatility is rough.” Gatheral et al. ([2018](https://arxiv.org/html/2511.03314v1#bib.bib27))
argue that the HH of RV time series is approximately 0.1, less than 1/2.
This observation implies that volatility time series exhibit rough or anti-persistent behavior.
Considering this observation, they suggest the rough FVM (RFVM) with H<1/2H<1/2 and show that the RFVM
improves volatility forecasts.
Furthermore, several advantages to use rough volatility are indicated.
One is the volatility surface issue. In particular, it is empirically observed that the term structure of at-the-money skew is described by a negative power law, which is not easily explained
by conventional stochastic volatility models(Carr and Wu, [2003](https://arxiv.org/html/2511.03314v1#bib.bib12); Fouque et al., [2003](https://arxiv.org/html/2511.03314v1#bib.bib23); Lee, [2005](https://arxiv.org/html/2511.03314v1#bib.bib32)).
To this issue, it is shown that models based on fractional Brownian motion are capable of explaining
the negative power law(Alos et al., [2007](https://arxiv.org/html/2511.03314v1#bib.bib2); Fukasawa, [2011](https://arxiv.org/html/2511.03314v1#bib.bib24)).
Another issue is the Zumbach effect(Zumbach, [2003](https://arxiv.org/html/2511.03314v1#bib.bib43), [2009](https://arxiv.org/html/2511.03314v1#bib.bib44)) implying that
the cross-correlation function between the daily variance and squared returns
has the time-reversal asymmetry which is not derived from conventional volatility models.
Interestingly, El Euch et al. ([2020](https://arxiv.org/html/2511.03314v1#bib.bib18)) shows that the rough Heston model could explain
the Zumbach effect.
Since there exist several issues that can be explained by the rough volatility,
it can be interesting to further seek evidence solved by rough volatility.
There also exist further developments to use rough volatility models for
such as option pricing(Bayer et al., [2016](https://arxiv.org/html/2511.03314v1#bib.bib7)) and perfect hedging(Euch and Rosenbaum, [2018](https://arxiv.org/html/2511.03314v1#bib.bib20)) and
investigations of origins of roughness by the market microstructure(El Euch et al., [2018](https://arxiv.org/html/2511.03314v1#bib.bib17); Jusselin and Rosenbaum, [2020](https://arxiv.org/html/2511.03314v1#bib.bib30); Rosenbaum and Tomas, [2021](https://arxiv.org/html/2511.03314v1#bib.bib37)).

Various empirical studies, using data from the RVs of various assets, imply that volatilities confirm the roughness of volatility (Bennedsen et al., [2022](https://arxiv.org/html/2511.03314v1#bib.bib8); Livieri et al., [2018](https://arxiv.org/html/2511.03314v1#bib.bib34); Takaishi, [2020](https://arxiv.org/html/2511.03314v1#bib.bib39); Floc’h, [2022](https://arxiv.org/html/2511.03314v1#bib.bib22)).
Contrary to these empirical findings,
the roughness of volatility remains a controversial issue.
For example, Cont and Das ([2024](https://arxiv.org/html/2511.03314v1#bib.bib15)) show that
the HE is different from spot and integrated (realized) volatilities and
infer that this may arise due to measurement errors of RV.
Fukasawa et al. ([2019](https://arxiv.org/html/2511.03314v1#bib.bib25)) find that the RV is still rough using an improved estimator; even more so than the observations of previous researchers.
Brandi and Di Matteo ([2022](https://arxiv.org/html/2511.03314v1#bib.bib11)) argue that the rough Bergomi model proposed for rough volatility is inconsistent with multi-scaling properties.

In this study, we address the finite sample effect on the HE obtained from RV.
RV is constructed by summing the squared returns sampled at a certain frequency;
generally, the number of samples to construct the RV is finite.
When the number of samples is finite, the RV receives the finite sample effect and, consequently,
the distribution of returns standardized by the RV deviates from a Gaussian distribution (Peters and De Vilder, [2006](https://arxiv.org/html/2511.03314v1#bib.bib36)).
Owing to the absence of previous research on this topic, we examine impact of the finite size effect on the HE estimation of RV time series.

The HE relates to the scaling behaviour of 2nd order fluctuations or variance.
For the random time series, H=1/2H=1/2.
For H>1/2(<1/2)H>1/2(<1/2), the time series is said to be persistent (ant-persitent).
The HE can be generalized for q-th order fluctuations and
it is referred to as the generalized Hurst exponet (GHE) h​(q)h(q).
When h​(q)h(q) is constant for any qq, such time series
is said to be monofractal.
Conversely, when h​(q)h(q) varies for qq, it is multifractal.
The GHE can capture the non-linear time-correlations that can not be
measured in the HE alone.
Numerous studies on the GHE have been conducted for price-return time series
and it is found that the multifractal nature is usually present in price-return time series, e.g. see Jiang et al. ([2019](https://arxiv.org/html/2511.03314v1#bib.bib29)).

In the literature, the RV time series is considered to be monofractal (Gatheral et al., [2018](https://arxiv.org/html/2511.03314v1#bib.bib27))
and there is little attention in multifractality.
However, the possibility of multifractality in the RV
is pointed out by Takaishi ([2020](https://arxiv.org/html/2511.03314v1#bib.bib39)).
Small multifractality in the RV of stock returns is also observed (Brandi and Di Matteo, [2022](https://arxiv.org/html/2511.03314v1#bib.bib11)).
In this study, we perform a multifractal analysis for the RV time series
to clarify the existence of the multifractality in the RV.

## 2 Data and Methodology

Our data consists of Bitcoin tick data traded on Bitstamp exchange
from January 2, 2014, to June 01, 2023.
We do not use data prior to 2014 because, in the early stages of the Bitcoin market,
liquidity
was low (Takaishi and Adachi, [2020](https://arxiv.org/html/2511.03314v1#bib.bib40)),
and we can observe different market properties in ill-liquid markets.
The HE of the return time series in the early stages of the Bitcoin market
was less than 1/2, indicating the anti-persistence of the time series(Urquhart, [2016](https://arxiv.org/html/2511.03314v1#bib.bib41)).
Subsequently, the HE increased to 1/2 as the liquidity increased (Takaishi and Adachi, [2020](https://arxiv.org/html/2511.03314v1#bib.bib40)).
It is argued that the anti-persistence of returns seen in the cryptocurrency market can be attributed to the low liquidity of the market (Wei, [2018](https://arxiv.org/html/2511.03314v1#bib.bib42)).

We construct the daily RV on day tt
with Δ\Delta-minute period by

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​Vt,Δ=∑inrt,i,Δ2,RV\_{t,\Delta}=\sum\_{i}^{n}r\_{t,i,\Delta}^{2}, |  | (1) |

where rt,i,Δ,i=1,2,…,nr\_{t,i,\Delta},i=1,2,\dots,n are intraday returns
and n=1440/Δn=1440/\Delta is the number of samples in one day.

At finite Δ\Delta, the RV receives the finite sample effect that could lower the accuracy of the RV estimate.
Let us assume that the observed daily return rtr\_{t} is described by rt=σt​ϵtr\_{t}=\sigma\_{t}\epsilon\_{t},
where ϵt∼N​(0,1)\epsilon\_{t}\sim N(0,1) and σt\sigma\_{t} is the standard deviation.
Under this assumption, the distribution of rt/σtr\_{t}/\sigma\_{t} should be the standard normal distribution.
Using the RV as a proxy of σt\sigma\_{t},
Andersen et al. ([2000](https://arxiv.org/html/2511.03314v1#bib.bib5)) show that the distribution of rt¯≡rt/R​Vt1/2\bar{r\_{t}}\equiv r\_{t}/RV\_{t}^{1/2} is nearly Gaussian.
However, when nn is small,
the distribution of rt¯\bar{r\_{t}} deviates from the Gaussian distribution.
Peters and De Vilder ([2006](https://arxiv.org/html/2511.03314v1#bib.bib36)) provide the finite sample formula of
the probability distribution P​(rt¯)P(\bar{r\_{t}}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(r¯)=Γ​(n/2)π​n​Γ​((n−1)/2)​(1−r¯2n)(n−3)/2.P(\bar{r})=\frac{\Gamma(n/2)}{\sqrt{\pi}n\Gamma((n-1)/2)}\left(1-\frac{\bar{r}^{2}}{n}\right)^{(n-3)/2}. |  | (2) |

Empirical observations confirm
Eq.([2](https://arxiv.org/html/2511.03314v1#S2.E2 "In 2 Data and Methodology ‣ Multifractality and sample size influence on Bitcoin volatility patterns")) (Takaishi, [2012](https://arxiv.org/html/2511.03314v1#bib.bib38)).
The 2k-th order moments of the standardized returns are also affected by the finite sample effect as

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[r¯2​k]=nk​(2​k−1)​(2​k−3)​…​1(n+2​k−2)​(n+2​k−4)​…​n.E[\bar{r}^{2k}]=\frac{n^{k}(2k-1)(2k-3)\dots 1}{(n+2k-2)(n+2k-4)\dots n}. |  | (3) |

From Eq.([3](https://arxiv.org/html/2511.03314v1#S2.E3 "In 2 Data and Methodology ‣ Multifractality and sample size influence on Bitcoin volatility patterns")), the kurtosis at finite nn is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[r¯4]E​[r¯2]2=3​nn+2.\frac{E[\bar{r}^{4}]}{E[\bar{r}^{2}]^{2}}=\frac{3n}{n+2}. |  | (4) |

The RV time series is defined by log-volatility increments as follows.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=log⁡R​Vt−log⁡R​Vt−1.V\_{t}=\log RV\_{t}-\log RV\_{t-1}. |  | (5) |

We determine the HE (=h​(2)=h(2)) of the time series VtV\_{t}
using the multifractal detrended fluctuation analysis (MDFA), suitable for
non-stationary processes (Kantelhardt et al., [2002](https://arxiv.org/html/2511.03314v1#bib.bib31))
and widely used for investigations of time series properties (Jiang et al., [2019](https://arxiv.org/html/2511.03314v1#bib.bib29)).
The MFDFA is described as follows. For a more detailed description, see, e.g., Kantelhardt et al. ([2002](https://arxiv.org/html/2511.03314v1#bib.bib31)).

First, we determine the profile Y​(i)Y(i) from VtV\_{t}

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y​(i)=∑j=1i(Vj−⟨V⟩),Y(i)=\sum\_{j=1}^{i}(V\_{j}-\langle V\rangle), |  | (6) |

where ⟨V⟩\langle V\rangle stands for the average of VtV\_{t}.
Then, we divide the profile Y​(i)Y(i) into NsN\_{s} non-overlapping segments of an equal length ss, where Ns≡i​n​t​(N/s)N\_{s}\equiv{int}(N/s).
Since the length of the time series is not always a multiple of ss,
we repeat the same procedure, starting from the end of the profile.
Next, we calculate the variance F2F^{2}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | F2​(ν,s)=1s​∑i=1s(Y​[(ν−1)​s+i]−Pν​(i))2,F^{2}(\nu,s)=\frac{1}{s}\sum\_{i=1}^{s}(Y[(\nu-1)s+i]-P\_{\nu}(i))^{2}, |  | (7) |

for each segment ν,ν=1,…,Ns\nu,\nu=1,\dots,N\_{s} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | F2​(ν,s)=1s​∑i=1s(Y​[N−(ν−Ns)​s+i]−Pν​(i))2,F^{2}(\nu,s)=\frac{1}{s}\sum\_{i=1}^{s}(Y[N-(\nu-N\_{s})s+i]-P\_{\nu}(i))^{2}, |  | (8) |

for each segment ν,ν=Ns+1,…,2​Ns\nu,\nu=N\_{s}+1,\dots,2N\_{s}.
Pν​(i)P\_{\nu}(i) is the fitting polynomial to remove the local trend in segment ν\nu.
Averaging all segments, we obtain the qqth order fluctuation function

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fq​(s)={12​Ns​∑ν=12​Ns(F2​(ν,s))q/2}1/q.F\_{q}(s)=\left\{\frac{1}{2N\_{s}}\sum\_{\nu=1}^{2N\_{s}}(F^{2}(\nu,s))^{q/2}\right\}^{1/q}. |  | (9) |

If the time series is long-range power-law correlated,
Fq​(s)F\_{q}(s) is expected to be the following functional form for large ss:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fq​(s)∼sh​(q).F\_{q}(s)\sim s^{h(q)}. |  | (10) |

h​(q)h(q) is called the GHE and h​(2)h(2) corresponds to the HE.

## 3 Results

We determine the HE in eight-year window data using the rolling window method.
The eight-year window is rolled every five days;
in each window, we determine the HE by the MDFA
for the RV sampled at Δ=1,2,…​1440\Delta=1,2,\dots 1440, where Δ\Delta is chosen
so that 1440/Δ1440/\Delta becomes an integer.

Fig.[1](https://arxiv.org/html/2511.03314v1#S3.F1 "Figure 1 ‣ 3 Results ‣ Multifractality and sample size influence on Bitcoin volatility patterns") displays the time evolution of the HE for various Δ\Delta.

![Refer to caption](x1.png)


Figure 1: 
Time evolution of the HE (h​(2)h(2)) for various sampling frequencies.

We identify how HE tends to decrease as Δ\Delta increases.
Such decreasing behavior is also observed in (Garcin and Grasselli, [2022](https://arxiv.org/html/2511.03314v1#bib.bib26))’s study of exchange rates.

To investigate the frequency dependence of the HE,
we select three representative data periods
(see Table 1)
and plot the HE as a function of Δ\Delta in Fig.[2](https://arxiv.org/html/2511.03314v1#S3.F2 "Figure 2 ‣ 3 Results ‣ Multifractality and sample size influence on Bitcoin volatility patterns"),
indicating that the HE decreases as Δ\Delta increases.
Although we do not know the finite sample formula for the HE,
inspired by the form of Eq.([3](https://arxiv.org/html/2511.03314v1#S2.E3 "In 2 Data and Methodology ‣ Multifractality and sample size influence on Bitcoin volatility patterns")),
we examine the following ansatz and find that the ansatz fits the HE results well.

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(Δ)=H0​nn+a,H(\Delta)=H\_{0}\frac{n}{n+a}, |  | (11) |

where H0H\_{0} and aa are fitting parameters.

![Refer to caption](x2.png)


Figure 2: 
HE as a function of Δ\Delta. Red solid lines show fitting results.

The fitting results (see also Table 1 for the fitting parameters) are shown as red lines in Fig.[2](https://arxiv.org/html/2511.03314v1#S3.F2 "Figure 2 ‣ 3 Results ‣ Multifractality and sample size influence on Bitcoin volatility patterns"),
indicating that
Eq.([11](https://arxiv.org/html/2511.03314v1#S3.E11 "In 3 Results ‣ Multifractality and sample size influence on Bitcoin volatility patterns")) fits the HE data well,
except for the slight deviation at Δ\Delta = 1-minute.
The deviation at 1-minute could be related to the microstructure noise that
manifests at very high frequencies.
Fleming et al. ([2003](https://arxiv.org/html/2511.03314v1#bib.bib21)) finds that the kurtosis of standardized returns from US stocks exhibits a divergent behavior
at very high frequencies and state that the divergent is caused by the leptokurtic distribution as a mixture of normals originated from the microstructure noise (Hansen and Lunde, [2006](https://arxiv.org/html/2511.03314v1#bib.bib28); Alexander and Narayanan, [2001](https://arxiv.org/html/2511.03314v1#bib.bib1)).
However, the microstructure noise effect in Bitcoin data that we observe seems small until about Δ=\Delta=1-min.
When the microstructure noise considerably affects the HE results,
we need to fit the HE data while excluding such affects.

The parameter H0H\_{0} corresponds to HH at Δ→0\Delta\rightarrow 0. The obtained values of H0H\_{0}
listed in Table 1 are around 0.12−0.140.12-0.14 and exhibit a slight decreasing behavior as a function of time.
It is interesting to see that the parameter aa is close to an integer 3 as similar equations in Eq.([3](https://arxiv.org/html/2511.03314v1#S2.E3 "In 2 Data and Methodology ‣ Multifractality and sample size influence on Bitcoin volatility patterns"))
although there is no reason that aa should be an integer.
The relative error to H0H\_{0} at finite Δ\Delta is given by a/(n+a)a/(n+a),
shown in Fig.[3](https://arxiv.org/html/2511.03314v1#S3.F3 "Figure 3 ‣ 3 Results ‣ Multifractality and sample size influence on Bitcoin volatility patterns").
Three lines from different periods are very similar and difficult to distinguish visually.
In empirical analyses, the sampling frequency for the RV is often Δ=5\Delta=5-minute
since the five-minute RV gives a reasonable balance between the bias and the efficiency(Andersen and Bollerslev, [1997](https://arxiv.org/html/2511.03314v1#bib.bib3))
and has better performance than other RV estimates (Liu et al., [2015](https://arxiv.org/html/2511.03314v1#bib.bib33)).
The relative errors at five-minute Δ\Delta are found to be around 1%1\%,
suggesting that the finite size effect on the HE for the widely used five-minute RV is
reasonably small .
Hereafter, we use the five-minute RV for the MFDFA.

![Refer to caption](x3.png)


Figure 3: 
Relative errors to H0H\_{0} as a function of Δ\Delta.

Fig.4(a) shows the time evolution of h​(q)h(q)
for q=−3,2,3q=-3,2,3, obtained using the five-minute RV time series.
It indicates that h​(q)h(q) as a function of qq is not constant, suggesting the multifractality of the time series.

To quantify the strength of multifractality, we define the following quantity(Zunino et al., [2008](https://arxiv.org/html/2511.03314v1#bib.bib45)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​h​(k)=h​(−k)−h​(k),\Delta h(k)=h(-k)-h(k), |  | (12) |

which goes to zero for the monofractal time series.
We also define the strength of multifractality by the Taylor coefficient of h​(q)h(q).
The function h​(q)h(q) is approximated linearly around q=0q=0 as

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(q)=B0+B1​q,h(q)=B\_{0}+B\_{1}q, |  | (13) |

where B0B\_{0} and B1B\_{1} are Taylor coefficients and the strength of multifractality
is measured by B1B\_{1}, which also takes zero for the monofractal time series.
Here, we approximately obtain B1B\_{1} by −Δ​h​(3)/6-\Delta h(3)/6.

Fig.4(b) and (c) display Δ​h​(3)\Delta h(3) and −B1-B\_{1} as a function of time and
indicate that the strength of multifractality is finite and time-varying,
meaning the existence of multifractality in the RV time series.
The average value of Δ​h​(3)\Delta h(3) for whole period is 0.034.
We also perform the multifractal analysis for the price-return time series
and obtain Δ​h​(3)≃0.12\Delta h(3)\simeq 0.12, indicating a stronger multifractality than that of the RV time series.
Similarly, the average value of −B1-B\_{1} for whole period is obtained to be 0.0057,
which is consistent with the similar strength of B1B\_{1} obtained for the stock RV time series(Brandi and Di Matteo, [2022](https://arxiv.org/html/2511.03314v1#bib.bib11)).

![Refer to caption](x4.png)


Figure 4: 
(a) Time evolution of h​(−3),h​(2)h(-3),h(2) and h​(3)h(3).
(b) Multifractal strength Δ​h​(3)\Delta h(3).
(c) Multifractal strength −B1-B\_{1}.




Table 1: 
Three periods selected for analysis and fitting parameters.

| Period | H0H\_{0} | aa |
| --- | --- | --- |
| I: 20014/1/2-2022/1/2 | 0.1379(8) | 2.93(11) |
| II: 2015/1/1-2023/1/1 | 0.1308(4) | 3.02(6) |
| III: 2015/5/27-2023/5/27 | 0.1262(3) | 3.15(6) |

## 4 Conclusion

We examine the finite sample effect on the HE using Bitcoin data and
find that the HE decreases as Δ\Delta increases.

We provide a simple two-parameter ansatz that obtains the HE at Δ→0\Delta\rightarrow 0 and use ansatz to obtain the HE ∼0.12−0.14\sim 0.12-0.14, indicating
the roughness of the RV time series.
We also find that the relative error of the HE for the five-minute RV is
small (1%1\%); thus, we conclude that the five-minute RV can be used for the HE estimate without considering
the finite sample effect.
Analyzing the five-minute RV time series, we
find that its multifractality is smaller than that of price-return
and the strength of the multifractality varies over time.

Two sources of the multifractality are considered (i) non-linear time correlations
and (ii) shape of distribution (Kantelhardt et al., [2002](https://arxiv.org/html/2511.03314v1#bib.bib31)).
The previous study suggests the multifractality originates in part from the shape of distribution(Takaishi, [2020](https://arxiv.org/html/2511.03314v1#bib.bib39)).
It is important to understand which source dominates the multifractality in the time series
when we model the RV time series.
If the dominant source is the shape of distribution, one may need to
introduce the stochastic process from the distribution.
This might be similar to the scheme of the GARCH-type models
in which to accommodate the fat-tailed return distribution,
non-normal distributions
are introduced to the innovations of the GARCH model(Bollerslev, [1987](https://arxiv.org/html/2511.03314v1#bib.bib10); Nelson, [1991](https://arxiv.org/html/2511.03314v1#bib.bib35)).
If the non-linear time correlations dominate, one may need a dynamical process that generates the multifractality in time series.
Future researchers can investigate and clarify the origin of the multifractality in the RV time series.

A limitation of the study is that we examine only Bitcoin data.
Future research could investigate
whether our findings hold for other assets.
If we confirm the multifractality in the volatility time series,
it could serve as a new property that can guide to construct a reliable volatility modeling.

## Acknowledgements

The numerical calculations for this study were performed using the Yukawa Institute Computer Facility and facilities at the Institute of Statistical Mathematics.
This study was supported by
the Yu-cho Foundation (Grant-in-Aid for Research , 2024) and in part by JSPS KAKENHI, grant number JP21K01435.

## References

* Alexander and Narayanan (2001)

  Alexander, C., Narayanan, S., 2001.
  Option Pricing with Normal Mixture Returns: Modelling Excess Kurtosis and Uncertanity in Volatility.
  Technical Report. Henley Business School, University of Reading.
* Alos et al. (2007)

  Alos, E., León, J.A., Vives, J., 2007.
  On the short-time behavior of the implied volatility for jump-diffusion models with stochastic volatility.
  Finance and stochastics 11, 571–589.
* Andersen and Bollerslev (1997)

  Andersen, T.G., Bollerslev, T., 1997.
  Intraday periodicity and volatility persistence in financial markets.
  Journal of empirical finance 4, 115–158.
* Andersen and Bollerslev (1998)

  Andersen, T.G., Bollerslev, T., 1998.
  Answering the skeptics: Yes, standard volatility models do provide accurate forecasts.
  International economic review , 885–905.
* Andersen et al. (2000)

  Andersen, T.G., Bollerslev, T., Diebold, F.X., Labys, P., 2000.
  Exchange rate returns standardized by realized volatility are (nearly) gaussian.
  Multinational Finance Journal 4, 159–179.
* Andersen et al. (2001)

  Andersen, T.G., Bollerslev, T., Diebold, F.X., Labys, P., 2001.
  The distribution of realized exchange rate volatility.
  Journal of the American statistical association 96, 42–55.
* Bayer et al. (2016)

  Bayer, C., Friz, P., Gatheral, J., 2016.
  Pricing under rough volatility.
  Quantitative Finance 16, 887–904.
* Bennedsen et al. (2022)

  Bennedsen, M., Lunde, A., Pakkanen, M.S., 2022.
  Decoupling the short-and long-term behavior of stochastic volatility.
  Journal of Financial Econometrics 20, 961–1006.
* Bollerslev (1986)

  Bollerslev, T., 1986.
  Generalized autoregressive conditional heteroskedasticity.
  Journal of Econometrics 31, 307–327.
* Bollerslev (1987)

  Bollerslev, T., 1987.
  A conditionally heteroskedastic time series model for speculative prices and rates of return.
  The review of economics and statistics , 542–547.
* Brandi and Di Matteo (2022)

  Brandi, G., Di Matteo, T., 2022.
  Multiscaling and rough volatility: An empirical investigation.
  International Review of Financial Analysis 84, 102324.
* Carr and Wu (2003)

  Carr, P., Wu, L., 2003.
  The finite moment log stable process and option pricing.
  The journal of finance 58, 753–777.
* Comte and Renault (1998)

  Comte, F., Renault, E., 1998.
  Long memory in continuous-time stochastic volatility models.
  Mathematical finance 8, 291–323.
* Cont (2001)

  Cont, R., 2001.
  Empirical properties of asset returns: Stylized facts and statistical issues.
  Quantitative Finance 1, 223–236.
* Cont and Das (2024)

  Cont, R., Das, P., 2024.
  Rough volatility: fact or artefact?
  Sankhya B , 1–33.
* Ding et al. (1993)

  Ding, Z., Granger, C.W., Engle, R.F., 1993.
  A long memory property of stock market returns and a new model.
  Journal of empirical finance 1, 83–106.
* El Euch et al. (2018)

  El Euch, O., Fukasawa, M., Rosenbaum, M., 2018.
  The microstructural foundations of leverage effect and rough volatility.
  Finance and Stochastics 22, 241–280.
* El Euch et al. (2020)

  El Euch, O., Gatheral, J., Radoičić, R., Rosenbaum, M., 2020.
  The zumbach effect under rough heston.
  Quantitative finance 20, 235–241.
* Engle (1982)

  Engle, R.F., 1982.
  Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation.
  Econometrica: Journal of the Econometric Society , 987–1007.
* Euch and Rosenbaum (2018)

  Euch, O.E., Rosenbaum, M., 2018.
  Perfect hedging in rough heston models.
  The Annals of Applied Probability 28, 3813–3856.
* Fleming et al. (2003)

  Fleming, J., Kirby, C., Ostdiek, B., 2003.
  The economic value of volatility timing using “realized” volatility.
  Journal of Financial Economics 67, 473–509.
* Floc’h (2022)

  Floc’h, F.L., 2022.
  Roughness of the implied volatility.
  arXiv preprint arXiv:2207.04930 .
* Fouque et al. (2003)

  Fouque, J.P., Papanicolaou, G., Sircar, R., Solna, K., 2003.
  Multiscale stochastic volatility asymptotics.
  Multiscale Modeling & Simulation 2, 22–42.
* Fukasawa (2011)

  Fukasawa, M., 2011.
  Asymptotic analysis for stochastic volatility: martingale expansion.
  Finance and Stochastics 15, 635–654.
* Fukasawa et al. (2019)

  Fukasawa, M., Takabatake, T., Westphal, R., 2019.
  Is volatility rough.
  arXiv: Statistics Theory URL: <https://api.semanticscholar.org/CorpusID:152282243>.
* Garcin and Grasselli (2022)

  Garcin, M., Grasselli, M., 2022.
  Long versus short time scales: the rough dilemma and beyond.
  Decisions in economics and finance 45, 257–278.
* Gatheral et al. (2018)

  Gatheral, J., Jaisson, T., Rosenbaum, M., 2018.
  Volatility is rough.
  Quantitative Finance 18, 933–949.
* Hansen and Lunde (2006)

  Hansen, P.R., Lunde, A., 2006.
  Realized variance and market microstructure noise.
  Journal of Business & Economic Statistics 24, 127–161.
* Jiang et al. (2019)

  Jiang, Z.Q., Xie, W.J., Zhou, W.X., Sornette, D., 2019.
  Multifractal analysis of financial markets.
  Rep. Prog. Phys. 82, 125901.
* Jusselin and Rosenbaum (2020)

  Jusselin, P., Rosenbaum, M., 2020.
  No-arbitrage implies power-law market impact and rough volatility.
  Mathematical Finance 30, 1309–1336.
* Kantelhardt et al. (2002)

  Kantelhardt, J.W., Zschiegner, S.A., Koscielny-Bunde, E., Havlin, S., Bunde, A., Stanley, H.E., 2002.
  Multifractal detrended fluctuation analysis of nonstationary time series.
  Physica A 316, 87–114.
* Lee (2005)

  Lee, R.W., 2005.
  Implied volatility: Statics, dynamics, and probabilistic interpretation.
  Recent advances in applied probability , 241–268.
* Liu et al. (2015)

  Liu, L.Y., Patton, A.J., Sheppard, K., 2015.
  Does anything beat 5-minute RV? a comparison of realized measures across multiple asset classes.
  Journal of Econometrics 187, 293–311.
* Livieri et al. (2018)

  Livieri, G., Mouti, S., Pallavicini, A., Rosenbaum, M., 2018.
  Rough volatility: evidence from option prices.
  IISE transactions 50, 767–776.
* Nelson (1991)

  Nelson, D., 1991.
  Conditional heteroskedasticity in asset returns: A new approach.
  Econometrica 59, 347–370.
* Peters and De Vilder (2006)

  Peters, R.T., De Vilder, R.G., 2006.
  Testing the continuous semimartingale hypothesis for the s&p 500.
  Journal of Business & Economic Statistics 24, 444–454.
* Rosenbaum and Tomas (2021)

  Rosenbaum, M., Tomas, M., 2021.
  From microscopic price dynamics to multidimensional rough volatility models.
  Advances in Applied Probability 53, 425–462.
* Takaishi (2012)

  Takaishi, T., 2012.
  Finite-sample effects on the standardized returns of the Tokyo Stock Exchange.
  Procedia-Social and Behavioral Sciences 65, 968–973.
* Takaishi (2020)

  Takaishi, T., 2020.
  Rough volatility of Bitcoin.
  Finance Research Letters 32, 101379.
* Takaishi and Adachi (2020)

  Takaishi, T., Adachi, T., 2020.
  Market efficiency, liquidity, and multifractality of Bitcoin: A dynamic study.
  Asia-Pacific Financial Markets 27, 145–154.
* Urquhart (2016)

  Urquhart, A., 2016.
  The inefficiency of Bitcoin.
  Economics Letters 148, 80–82.
* Wei (2018)

  Wei, W.C., 2018.
  Liquidity and market efficiency in cryptocurrencies.
  Economics Letters 168, 21–24.
* Zumbach (2003)

  Zumbach, G., 2003.
  Volatility processes and volatility forecast with longmemory.
  Quantitative Finance 4, 70.
* Zumbach (2009)

  Zumbach, G., 2009.
  Time reversal invariance in finance.
  Quantitative Finance 9, 505–515.
* Zunino et al. (2008)

  Zunino, L., Tabak, B.M., Figliola, A., Pérez, D., Garavaglia, M., Rosso, O., 2008.
  A multifractal approach for stock market inefficiency.
  Physica A 387, 6558–6566.