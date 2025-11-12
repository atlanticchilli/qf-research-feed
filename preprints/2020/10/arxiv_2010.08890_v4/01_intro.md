---
authors:
- Ioannis P. Antoniades
- Giuseppe Brandi
- L. G. Magafas
- T. Di Matteo
doc_id: arxiv:2010.08890v4
family_id: arxiv:2010.08890
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2010.08890] The use of scaling properties to detect relevant changes in financial
  time series: a new visual warning tool'
url_abs: http://arxiv.org/abs/2010.08890v4
url_html: https://ar5iv.org/html/2010.08890v4
venue: arXiv q-fin
version: 4
year: 2020
---


Ioannis P. Antoniades
Corresponding author. Email: iantoniades@auth.gr 

Giuseppe Brandi

L. G. Magafas

T. Di Matteo
Aristotle University of Thessaloniki, Physics Department, Thessaloniki,
Department of Mathematics, King’s College London, The Strand, London, WC2R 2LS, UK
Complexity Science Hub Vienna, Josefstaedter Strasse 39, A 1080 Vienna, Austria
International Hellenic University, Physics Department, Complex Systems Laboratory
American College of Thessaloniki, Division of Science & Technology

###### Abstract

The dynamical evolution of multiscaling in financial time series is investigated using time-dependent Generalized Hurst Exponents (GHE), Hqsubscript𝐻𝑞H\_{q}, for various values of the parameter q𝑞q. Using Hqsubscript𝐻𝑞H\_{q}, we introduce a new visual methodology to algorithmically detect critical changes in the scaling of the underlying complex time-series. The methodology involves the degree of multiscaling at a particular time instance, the multiscaling trend which is calculated by the Change-Point Analysis method, and a rigorous evaluation of the statistical significance of the results. Using this algorithm, we have identified particular patterns in the temporal co-evolution of the different Hqsubscript𝐻𝑞H\_{q} time-series. These GHE patterns, distinguish in a statistically robust way, not only between time periods of uniscaling and multiscaling, but also among different types of multiscaling: symmetric multiscaling (M) and asymmetric multiscaling (A). Asymmetric multiscaling can also be robustly divided into three other subcategories. We apply the visual methodology to time-series comprising of daily close prices of four stock market indices: two major ones (S&P 500 and Tokyo-NIKKEI) and two peripheral ones (Athens Stock Exchange general Index and Bombay-SENSEX). Results show that multiscaling varies greatly with time: time periods of strong multiscaling behavior and time periods of uniscaling behavior are interchanged while transitions from uniscaling to multiscaling behavior occur before critical market events, such as stock market bubbles. Moreover, particular asymmetric multiscaling patterns appear during critical stock market eras and provide useful information about market conditions. In particular, they can be used as ’fingerprints’ of a turbulent market period as well as provide warning signals for an upcoming stock market ’bubble’. The applied visual methodology also appears to distinguish between exogenous and endogenous stock market crises, based on the observed patterns before the actual events. The visual methodology is sufficiently general to be applicable for the description of the dynamical evolution of multiscaling properties of any complex system.

###### keywords:

Hurst exponent , multiscaling analysis , stock market , market forecasting , econophysics , complex time-series analysis

###### PACS:

89.75.Da , 89.65.Gh

###### MSC:

[2020] 37M10 , 37N40

††journal: Physica A††2020.This manuscript version is made available under the CC-BY-NC-ND 4.0 license

{highlights}

Visual warning tool for financial time series based on scaling analysis

Application of time-dependent Generalized Hurst Exponent method to financial timeseries

## 1 Introduction

The study of scaling in financial systems has been a field of investigation for many years now ([[1](#bib.bib1)], [[2](#bib.bib2)], [[3](#bib.bib3)], [[4](#bib.bib4)], [[5](#bib.bib5)], [[6](#bib.bib6)], [[7](#bib.bib7)], [[8](#bib.bib8)], [[9](#bib.bib9)], [[10](#bib.bib10)], [[11](#bib.bib11)], [[12](#bib.bib12)], [[13](#bib.bib13)], [[14](#bib.bib14)], [[15](#bib.bib15)],[[16](#bib.bib16)],[[17](#bib.bib17)],[[18](#bib.bib18)],[[19](#bib.bib19)]). These studies have shown that financial series, especially from stock-markets, display multiscaling, which is nowadays widely accepted as empirical stylized fact of financial time series. The (multi)scaling property of time series is particularly important in risk management, especially when the model used assumes independence of asset returns. In fact, the lack of this assumption to hold, may severely bias risk measures, especially if there is long-range dependence and this is acting with a different degree across the time series statistical moments. In recent years, multiscaling has been adopted as a formalism in two different branches of quantitative finance, i.e. econophysics and mathematical finance. The former devoted most of the attention to price and returns series in order to understand the source of multiscaling from an empirical and theoretical point of view [[20](#bib.bib20), [21](#bib.bib21), [7](#bib.bib7), [1](#bib.bib1), [5](#bib.bib5), [22](#bib.bib22), [23](#bib.bib23), [2](#bib.bib2), [24](#bib.bib24)] and has recently identified a new stylized fact which relates (non-linearly) the strength of multiscaling and the dependence between stocks [[24](#bib.bib24)]. The latter instead builds on the work of [[25](#bib.bib25)] on rough volatility and has been used to construct stochastic models with anti-persistent volatility dynamics [[25](#bib.bib25), [26](#bib.bib26), [27](#bib.bib27), [28](#bib.bib28)]. Although these research fields try to answer different research questions, it is important to recognize the relevance that multiscaling has attained in finance. Multiscaling has been understood to originate from one or more phenomena related to trading dynamics. In particular, it can be attributed to (i) the fat tails in price change distributions, (ii) the auto-correlation of the absolute value of log-returns, (iii) liquidity dynamics, or (iv) (non-linear) correlation between high and low returns generated by the different time horizon of traders and the consequent volumes traded. It can also be caused by the endogeneity of markets for which a given order generates many other orders. The latter occurs especially in markets where algorithmic trading is prevalent [[29](#bib.bib29)].
However, scaling in a financial time series has also been shown to vary with time. For example, there have been studies trying to link this variation with dynamical elements in the underlying title such as, for instance, the level of stability of a firm ([[30](#bib.bib30)]). In [[31](#bib.bib31)] and [[32](#bib.bib32)] the authors discuss, by using Multi-Fractal Detrended Fluctuation Analysis method (MF-DFA), the dynamical evolution of the f​(α)𝑓𝛼f(\alpha) vs. α𝛼\alpha multifractal spectrum in financial and other types of time-series, not only in terms of its width Δ​α=αm​a​x−αm​i​nΔ𝛼subscript𝛼𝑚𝑎𝑥subscript𝛼𝑚𝑖𝑛\Delta\alpha=\alpha\_{max}-\alpha\_{min} but also in terms of its ’asymmetry’, i.e. looking at the evolution of the shape (skewness) of the spectrum and relating it to market events and underling dynamics. Other studies have tried to associate a time-varying Hurst exponent as a measure of the dynamically changing scaling of a financial time-series, with the development of stock-market bubbles ([[33](#bib.bib33)], [[34](#bib.bib34)] and references therein), trading signals ([[35](#bib.bib35)]) and predictability of an index [[36](#bib.bib36)], raising the question whether scaling analysis can be used as a signaling tool for financial markets ([[37](#bib.bib37)],[[38](#bib.bib38)],[[39](#bib.bib39)]).

In the present study, we aim to contribute towards this discussion by studying the dynamical evolution of multiscaling using the structure function approach, also known as the Generalized Hurst exponent (GHE) method [[3](#bib.bib3), [1](#bib.bib1), [18](#bib.bib18)], on time-series from four stock market indices, two major ones, S&P 500 and Tokyo-NIKKEI), and two from peripheral markets, Athens Stock Exchange General Index (ASE) and Bombay-SENSEX. Employing the GHE method, the generalized Hurst exponents, Hqsubscript𝐻𝑞H\_{q}, are calculated for various values of the parameter q𝑞q corresponding to time scaling of the q𝑞q-moment of the series difference distribution for a time delay τ𝜏\tau. In the time-dependent GHE approach, time-series of Hqsubscript𝐻𝑞H\_{q} are generated for a range of q𝑞q values, by partitioning the underlying time-series into (usually overlapping) time segments and calculating the Hqsubscript𝐻𝑞H\_{q} values for each segment. Looking at the relative values of the Hqsubscript𝐻𝑞H\_{q} for the various q𝑞q at a particular time segment, one can evaluate the degree of multiscaling during that period. Alternative methods to GHE can also be used to extract the scaling exponent from time series, such as Rescaled range (R/S) analysis ([[40](#bib.bib40), [18](#bib.bib18)]), MF-DFA ([[41](#bib.bib41)]) and the Wavelet Transform Modulus Maxima (WTMM) introduced by [[42](#bib.bib42), [43](#bib.bib43)]. A more complete discussion on the use and misuse of various Hurst exponent estimation methods is given by Serinaldi [[44](#bib.bib44)], suggesting caution on the method used depending on the type of time-series considered. Recently, [[24](#bib.bib24)] showed that the results retrieved by GHE methodology and MF-DFA are qualitatively equivalent while [[16](#bib.bib16)] showed empirically that the GHE approach outperforms the other methods under different data specifications. For this reason, throughout this work we will use the GHE methodology.

The scope of this work is threefold: (i) At a given time period, to detect differences among the GHE temporal profiles of a time-series and the respective profiles of a surrogate randomly generated time-series of similar volatility temporal profile as the original series, using the exact same estimation method for both. (ii) To detect temporal changes in the GHE profiles of a time-series. We are thus interested in detecting statistically significant differences, rather than absolute values, of GHE’s relative to a specific reference series (the surrogate series) and the temporal evolution of these differences. (iii) to identify recurrent patterns in the temporal profiles that may correspond to particular market conditions. These patterns could characteristically emerge before or after critical time periods such as a stock-market bubble. In the first case, they can be used as warning signals for a particular future market event. In order to provide a rigorous definition of such patterns in GHE profiles and a systematic way to detect them, we introduce a visual methodology to algorithmically detect critical changes in the scaling of the underlying complex time-series. The methodology involves the strength of multiscaling at a particular time instance, the multiscaling trend, which is calculated by the Change-Point Analysis method, and a rigorous evaluation of the statistical significance of the identified patterns, by comparing to the output of the same analysis applied to randomly generated surrogate time-series that are constructed so that they have the same volatility temporal profile as the real series. Using this algorithm, we have identified particular patterns in the temporal co-evolution of the different GHE time-series. These patterns, that we call GHE Temporal Patterns (TP), distinguish in a statistically robust way, not only between time periods of uniscaling and multiscaling, but also among different types of multiscaling: symmetric multiscaling and asymmetric multiscaling. The later type is characterized by a time asymmetric dynamic of the scaling exponents for the extreme q𝑞q values, q1subscript𝑞1q\_{1} and q2subscript𝑞2q\_{2}. The methodology shows that asymmetric multiscaling itself can be robustly divided into three subcategories that correspond to different dynamics. By applying the above visual methodology to historical data of the four indices mentioned above, we find that critical events are preceded by asymmetric multiscaling patterns thus highlighting a warning signal. We also find that such behaviour is in general stronger for endogenous crisis as the Dot.com bubble, the 1991 Japanese bubble, or the 2000 Athens bubble, but much weaker for exogenous generated ones, such as the 2008 global financial crisis. Furthermore, we discuss the physical connection of the multiscaling TP’s to underlying market trading dynamics.

The paper is structured as follows. Section [2](#S2 "2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") is devoted to the presentation of the methods and implementation used in the paper, section [3](#S3 "3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") shows results of an empirical application of the methodology to stock market indices, while sections [4](#S4 "4 Discussion ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") and [5](#S5 "5 Conclusions ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") are devoted to the discussion of the results, conclusions and future work for the further development of the method used in this study and its possible application to financial time series or time series of other complex systems.

## 2 Description of methods

### 2.1 Generalized Hurst Exponents

The Hurst exponent ([[40](#bib.bib40)], [[45](#bib.bib45)]) is a well-known tool used to study the scaling behavior of time series coming from any dynamical process. To compute the scaling exponents, it is necessary to study the q𝑞q-order moments of the absolute value of the increments of the stochastic process [[1](#bib.bib1)]. In particular, the process (Xt)subscript𝑋𝑡(X\_{t}) with stationary increments is analysed through

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ξ​(τ,q)=𝔼​[|X(t+τ)−Xt|q]∼Kq​τq​Hq,Ξ𝜏𝑞𝔼delimited-[]superscriptsubscript𝑋𝑡𝜏subscript𝑋𝑡𝑞similar-tosubscript𝐾𝑞superscript𝜏𝑞subscript𝐻𝑞\Xi(\tau,q)=\mathbb{E}\left[|X\_{(t+\tau)}-X\_{t}|^{q}\right]\sim K\_{q}\tau^{qH\_{q}}, |  | (1) |

where q={q1,q2,…,qM}𝑞subscript𝑞1subscript𝑞2…subscript𝑞𝑀q=\{q\_{1},q\_{2},\dots,q\_{M}\} is the set of evaluated moments, τ={τ1,τ2,…,τN}𝜏subscript𝜏1subscript𝜏2…subscript𝜏𝑁\tau=\{\tau\_{1},\tau\_{2},\dots,\tau\_{N}\} is the set of time aggregation used to compute the process increments, Kqsubscript𝐾𝑞K\_{q} is the q𝑞q-moment for τ=1𝜏1\tau=1 and Hqsubscript𝐻𝑞H\_{q} is the so called generalized Hurst exponent, which is a function of q𝑞q. The function q​Hq𝑞subscript𝐻𝑞qH\_{q} is concave [[4](#bib.bib4), [14](#bib.bib14)] and codifies the scaling exponents of the process. A multiscaling proxy can be obtained by fitting the measured scaling exponents with a second degree polynomial ([[24](#bib.bib24), [46](#bib.bib46)]) of the form222Technical details of the choice of this functional form can be found in [[24](#bib.bib24), [46](#bib.bib46)].

|  |  |  |  |
| --- | --- | --- | --- |
|  | q​Hq=A​q+B​q2,𝑞subscript𝐻𝑞𝐴𝑞𝐵superscript𝑞2qH\_{q}=Aq+Bq^{2}, |  | (2) |

or equivalently [[29](#bib.bib29)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hq=A+B​q,subscript𝐻𝑞𝐴𝐵𝑞H\_{q}=A+Bq, |  | (3) |

where A𝐴A and B𝐵B are two constants. In this setting, the measured B𝐵B, B^^𝐵\widehat{B}, represents the curvature of q​Hq𝑞subscript𝐻𝑞qH\_{q}. If B^=0^𝐵0\widehat{B}=0, Hqsubscript𝐻𝑞H\_{q} does not depend on q𝑞q, i.e. Hq=Hsubscript𝐻𝑞𝐻H\_{q}=H for all q𝑞q, hence the process is uniscaling, while if B^≠0^𝐵0\widehat{B}\neq 0, the process is multiscaling [[1](#bib.bib1), [29](#bib.bib29), [24](#bib.bib24), [46](#bib.bib46)]. For q=1𝑞1q=1, the GHE is equivalent to the original Hurst exponent. Notice also that for q=2𝑞2q=2, Ξ​(τ,2)Ξ𝜏2\Xi(\tau,2) is proportional to the auto-correlation function of Xtsubscript𝑋𝑡X\_{t}. For H1=0.5subscript𝐻10.5H\_{1}=0.5, the evolution of the system in state-space is equivalent to a random walk, i.e. the underlying process is purely stochastic (diffusive). For a single variable time series, this is equivalent to saying that at any given time, the value of the series is equally likely to go up as it is to go down. For H1>0.5subscript𝐻10.5H\_{1}>0.5, the system evolves faster than stochastic diffusion (super-diffusive process), which implies that -for a single-variable series- if a change occurs in one direction (up or down), it is more likely that the next change will be in the same direction rather than in the opposite. In such a case, the underlying process is characterized as a persistent process. Finally, for H1<0.5subscript𝐻10.5H\_{1}<0.5, the system evolves slower than stochastic diffusion (sub-diffusive process). For a single-variable series, this implies that, if a change occurs in one direction (up or down), it is more likely that the next change will be in the opposite direction. In the latter case, the process is characterized as an anti-persistent process. For the calculation of GHE’s of higher and more positive values of q𝑞q, the largest differences in a series are weighted more than smaller differences in ([1](#S2.E1 "In 2.1 Generalized Hurst Exponents ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) and therefore large-q𝑞q GHE’s emphasize the tails of the distribution of differences. Conversely, lower (less positive) values of q𝑞q weigh small differences more than large ones. Computing a broad spectrum of GHE’s, for several spread-out values of q𝑞q, provides a more detailed ’signature’ of the underlying dynamics of the system compared to considering only the original Hurst exponent. However, using high values of q𝑞q can bias the results if the data analysed is characterised by distributions with fat tails. In particular, for q>α𝑞𝛼q>\alpha, where α𝛼\alpha is the tail exponent of the distribution of the data, the q𝑞q-moments are not well defined. This introduces a bias on the expected value which in turn, produces a bias in the GHE estimation. Since financial time series are generally fat tailed, the choice of q𝑞q is relevant.

### 2.2 Weighted GHE’s

Recently, Morales & Di Matteo in [[30](#bib.bib30)] have proposed a modification of the GHE, the weighted GHE (wGHE), by modifying the way the time averaging is carried out in Equation ([1](#S2.E1 "In 2.1 Generalized Hurst Exponents ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")). Specifically, while taking the sum within a time interval [t−Δ​t,t]𝑡Δ𝑡𝑡[t-\Delta t,t] of length Δ​tΔ𝑡\Delta t, each term of the time series is weighed by a factor that depends on how far back from the present time t𝑡t the term lies: the farther in the past, the less this term is weighed, so that more recent times have a higher contribution to the calculation of the moments in Equation ([1](#S2.E1 "In 2.1 Generalized Hurst Exponents ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")). Thus, the averaging in Equation ([1](#S2.E1 "In 2.1 Generalized Hurst Exponents ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) is replaced by the following definition: For any function f𝑓f of a dynamic variable Xtsubscript𝑋𝑡X\_{t}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[f​(Xt)]θ=∑s=0Δ​t−1ws​(θ)​f​(X(t−s)),𝔼subscriptdelimited-[]𝑓subscript𝑋𝑡𝜃superscriptsubscript𝑠0Δ𝑡1subscript𝑤𝑠𝜃𝑓subscript𝑋𝑡𝑠\mathbb{E}\left[f\left(X\_{t}\right)\right]\_{\theta}=\sum\_{s=0}^{\Delta t-1}w\_{s}\left(\theta\right)f\left(X\_{(t-s)}\right), |  | (4) |

where the weighting factor wssubscript𝑤𝑠w\_{s} is an exponentially decaying function of time defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ws​(θ)=wo​(θ)​e−sθ,subscript𝑤𝑠𝜃subscript𝑤𝑜𝜃superscript𝑒𝑠𝜃w\_{s}\left(\theta\right)=w\_{o}\left(\theta\right)e^{-\frac{s}{\theta}}, |  | (5) |

where θ𝜃\theta is the characteristic time for which w𝑤w drops to 1/e1𝑒1/e and wo=wo​(θ)=1−e−1θ1−e−Δ​tθsubscript𝑤𝑜subscript𝑤𝑜𝜃1superscript𝑒1𝜃1superscript𝑒Δ𝑡𝜃w\_{o}=w\_{o}\left(\theta\right)=\frac{1-e^{-\frac{1}{\theta}}}{1-e^{-\frac{\Delta t}{\theta}}} is a normalization constant that ensures that the sum of all weights w𝑤w within the interval Δ​tΔ𝑡\Delta t equals 1. Thus, Equation ([1](#S2.E1 "In 2.1 Generalized Hurst Exponents ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) is now replaced by its weighted sum equivalent:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ξ​(τ,q,θ)=𝔼​[|X(t+τ)−Xt|q]θ∼Kq​τq​Hq(θ),Ξ𝜏𝑞𝜃𝔼subscriptdelimited-[]superscriptsubscript𝑋𝑡𝜏subscript𝑋𝑡𝑞𝜃similar-tosubscript𝐾𝑞superscript𝜏𝑞superscriptsubscript𝐻𝑞𝜃\Xi(\tau,q,\theta)=\mathbb{E}\left[|X\_{(t+\tau)}-X\_{t}|^{q}\right]\_{\theta}\sim K\_{q}\tau^{qH\_{q}^{(\theta)}}, |  | (6) |

where Hq(θ)superscriptsubscript𝐻𝑞𝜃H\_{q}^{(\theta)} is the wGHE corresponding to a characteristic time θ𝜃\theta. Throughout the rest of this paper we will use the wGHE version as defined above. Its main advantage is that it allows one to use a fixed window Δ​tΔ𝑡\Delta t for all calculations, varying only the characteristic time θ𝜃\theta in order to increase or decrease the weighting of the short-term past relative to the long-term past. This provides enough data to obtain accurate estimates for wGHE’s and at the same time gives flexibility in setting the characteristic weighting time scale, thus adjusting smoothly the importance of recent past to distant past in GHE computation.
Besides wGHE’s, we also estimated the time evolution of the volatility of an index, defined as the standard deviation of the weighted log returns over a time window equal to Δ​tΔ𝑡\Delta t. For volatility calculation, the averaging was again carried out as a weighted average with a characteristic time θ𝜃\theta using Equation ([4](#S2.E4 "In 2.2 Weighted GHE’s ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t)=σ​(l​o​g​(Xτ+1Xτ)​wt​(θ))Δ​t,𝑉𝑡𝜎subscript𝑙𝑜𝑔subscript𝑋𝜏1subscript𝑋𝜏subscript𝑤𝑡𝜃Δ𝑡V(t)=\sigma\left(log\left(\frac{X\_{\tau+1}}{X\_{\tau}}\right)w\_{t}\left(\theta\right)\right)\_{\Delta t}, |  | (7) |

where l​o​g​(…)𝑙𝑜𝑔…log(...) is the natural logarithm, σ​(…)Δ​t𝜎subscript…Δ𝑡\sigma(...)\_{\Delta t} denotes standard deviation of the series for τ=1​…​Δ​t−1𝜏1…Δ𝑡1\tau=1...\Delta t-1 and the time weighting factor w𝑤w is given by Equation ([5](#S2.E5 "In 2.2 Weighted GHE’s ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")).

### 2.3 Surrogate stock market indices

In order to make sure that our results are not numerical artefacts of the finite data sizes due to the relatively short time windows used in the wGHE computations, we applied the same calculations on surrogate time series. In order to produce such series, we did not apply the ’shuffling’ method often used for this purpose, according to which the surrogate is constructed by a random permutation of the original time-series percentage differences, in order to destroy any long-term correlations of the original data. Instead, for each market index studied, we created a respective surrogate index as follows: Starting at the actual close price of the particular index at an initial date (the first date for which data was available), closing prices of all subsequent dates were artificially generated by a ’random walk’ procedure, in which the day-to-day log price change was picked from a normal distribution with mean equal to zero and variance equal to the weighted average volatility V​(t)𝑉𝑡V(t) of the actual index at that particular date t𝑡t. In this way, the surrogate index day-to-day relative price changes are randomly chosen, but the volatility variation of the surrogate index (i.e. the average magnitude of the relative daily changes) matches the temporal volatility profile of the actual index.
The reason for making this choice is that, in the present study, the surrogate series merely serve as reference series for the purpose of subtracting the effect in multiscaling properties that are solely due to the finite-sized (short length) data segments used in calculations from any wGHE temporal variations of the real index that are the cause of the underlying market dynamics. In other words, the surrogate index serves as a measure of the ”noise level” for the wGHE of the real indices, which, after being subtracted, will enable a more accurate quantitative evaluation of the departure of observed multiscaling behavior from a randomly generated finite data set whose distribution of differences is normal, by construction. Randomly shuffling a real index, on the other hand, destroys any temporal correlations but maintains the precise distribution of changes intact. Therefore, comparisons of the wGHE temporal profiles of the real index with the respective profiles of a shuffled surrogate, does not seclude the effect of the non-normal character of real price distributions, an effect that we want to measure. Another obvious choice for a surrogate index would be a randomly generated index with price changes picked from a normal distribution of uniform variance in time (i.e. ignoring the effect of a time-varying market volatility). In the present study, we chose to include the effects of the volatility variation with time, in order to subtract any residual effect it may have on the wGHE’s. In this way, we are sure to measure the effects on the wGHE’s profiles coming from the departure of the price change distributions from being normal (although with time-varying variance), as well as any temporal correlations within the close price time series themselves.

## 3 Results

### 3.1 Data description

For our analysis, we have used 4 stock market indices: New York stock exchange index (S&P 500), Tokyo stock exchange index (NIKKEI), Athens Stock Exchange general index (ASE) and the Bombay stock index (SENSEX). Table [1](#S3.T1 "Table 1 ‣ 3.1 Data description ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") shows the time period in which the data is analysed and the number of trading days in each series.

|  |  |  |
| --- | --- | --- |
| Market | Time period | Trading days |
| S&P 500 | 1927-2020 | 23138 |
| NIKKEI | 1969-2020 | 13068 |
| ASE | 1991-2020 | 7146 |
| SENSEX | 2001-2020 | 5450 |

Table 1: Time periods and the number of trading days analysed for each stock market.

For each data series Xtsubscript𝑋𝑡X\_{t}, we used daily log prices, which is defined as the natural logarithm of the closing price of the index at each day, i.e. Xt=l​o​g​(Pt)subscript𝑋𝑡𝑙𝑜𝑔subscript𝑃𝑡X\_{t}=log(P\_{t}), where Ptsubscript𝑃𝑡P\_{t} is the closing price of the index at time t𝑡t.

### 3.2 Standardized GHE, multiscaling proxies and parameter definition

We use a convenient normalization for Hqsubscript𝐻𝑞H\_{q} defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hq(θ)′=Hq(θ)−H∗σ​(Hqs​u​r​r​(θ)),H\_{q}^{{}^{\prime}(\theta)}=\frac{H\_{q}^{(\theta)}-H^{\*}}{\sigma\left(H\_{q}^{surr(\theta)}\right)}, |  | (8) |

where H∗superscript𝐻H^{\*} is the value of Hurst exponent expected for a perfectly random series (H∗=0.5superscript𝐻0.5H^{\*}=0.5) and σ​(Hqs​u​r​r​(θ))𝜎subscriptsuperscript𝐻𝑠𝑢𝑟𝑟𝜃𝑞\sigma\left(H^{surr(\theta)}\_{q}\right) is the standard deviation of Hθs​u​r​r​(q)subscriptsuperscript𝐻𝑠𝑢𝑟𝑟𝜃𝑞H^{surr}\_{\theta}(q), the wGHE of the respective surrogate series calculated over the entire timeline, which is computed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(Hqs​u​r​r)=∑τ=1N(Hqs​u​r​r​(τ)−𝔼​[Hqs​u​r​r])2N−1,𝜎subscriptsuperscript𝐻𝑠𝑢𝑟𝑟𝑞superscriptsubscript𝜏1𝑁superscriptsubscriptsuperscript𝐻𝑠𝑢𝑟𝑟𝑞𝜏𝔼delimited-[]subscriptsuperscript𝐻𝑠𝑢𝑟𝑟𝑞2𝑁1\sigma\left(H^{surr}\_{q}\right)=\sqrt{\frac{\sum\_{\tau=1}^{N}\left(H^{surr}\_{q}(\tau)-\mathbb{E}\left[H^{surr}\_{q}\right]\right)^{2}}{N-1}}, |  | (9) |

where 𝔼​[Hqs​u​r​r]𝔼delimited-[]subscriptsuperscript𝐻𝑠𝑢𝑟𝑟𝑞\mathbb{E}\left[H^{surr}\_{q}\right] is the average of the series:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Hqs​u​r​r]=1N​∑t=1NHqs​u​r​r​(t),𝔼delimited-[]subscriptsuperscript𝐻𝑠𝑢𝑟𝑟𝑞1𝑁superscriptsubscript𝑡1𝑁subscriptsuperscript𝐻𝑠𝑢𝑟𝑟𝑞𝑡\mathbb{E}\left[H^{surr}\_{q}\right]=\frac{1}{N}\sum\_{t=1}^{N}H^{surr}\_{q}(t), |  | (10) |

and N𝑁N is the total number of points in the time-series. This type of normalized GHE (to which we will refer, from now on, as the ’standardized’ GHE in order to distinguish it from usual normalized versions that contain the standard deviation of the real series itself) has a convenient interpretation: a value of Hq(θ)′≈0H\_{q}^{{}^{\prime}(\theta)}\approx 0 signifies an underlying time-series with the same behavior as a random series. For other values, Hq(θ)′H\_{q}^{{}^{\prime}(\theta)} is equal to the number of standard deviations of Hqs​u​r​r​(θ)superscriptsubscript𝐻𝑞𝑠𝑢𝑟𝑟𝜃H\_{q}^{surr(\theta)} that the real index Hq(θ)superscriptsubscript𝐻𝑞𝜃H\_{q}^{(\theta)} is above 0.5. The standard deviation of Hqs​u​r​r​(θ)superscriptsubscript𝐻𝑞𝑠𝑢𝑟𝑟𝜃H\_{q}^{surr(\theta)} is a measure of the variability of the Hqsubscript𝐻𝑞H\_{q} series of a random index and thus conveniently measures the degree of ’noise level’, i.e. the variability of any Hqsubscript𝐻𝑞H\_{q} series that is due to finite data size effects and not to the actual underlying dynamics (apart from the dynamical changes in volatility which -in the present work- are included in the generation of the random surrogate). Therefore, division by the standard deviation of the surrogate series, enables a quantification of the statistical strength of the observed persistent, anti-persistent or uniscaling/multiscaling behavior of the real time-series at each time period, compared to a random signal for which the wGHE’s are computed with the same window size Δ​tΔ𝑡\Delta t and characteristic weighting factor θ𝜃\theta.

In order to assess multiscaling, we use two alternative measures:

* 1.

  Multiscaling width Wq1,q2subscript𝑊
  subscript𝑞1subscript𝑞2W\_{q\_{1},q\_{2}}
* 2.

  Multiscaling curvature (or depth) B𝐵B of Equation [3](#S2.E3 "In 2.1 Generalized Hurst Exponents ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool").

The multiscaling width Wq1,q2subscript𝑊

subscript𝑞1subscript𝑞2W\_{q\_{1},q\_{2}} is computed as the difference between the Hq1subscript𝐻subscript𝑞1H\_{q\_{1}} and Hq2subscript𝐻subscript𝑞2H\_{q\_{2}}, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wq1,q2=Hq1−Hq2,subscript𝑊  subscript𝑞1subscript𝑞2subscript𝐻subscript𝑞1subscript𝐻subscript𝑞2W\_{q\_{1},q\_{2}}=H\_{q\_{1}}-H\_{q\_{2}}, |  | (11) |

and conveys information on the span of the Hqsubscript𝐻𝑞H\_{q} parameter. Conversely, the multiscaling curvature B𝐵B is computed as the linear fit between q𝑞q and Hq(θ)superscriptsubscript𝐻𝑞𝜃H\_{q}^{(\theta)}, as described in Equation ([3](#S2.E3 "In 2.1 Generalized Hurst Exponents ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) ([[29](#bib.bib29), [24](#bib.bib24)]). If the process is uniscaling, both measures should be approximately zero as Hq(θ)superscriptsubscript𝐻𝑞𝜃H\_{q}^{(\theta)} doesn’t depend on q𝑞q. In order to run our procedure, we have to specify some input parameters, i.e. τ𝜏\tau, q𝑞q, and Δ​tΔ𝑡\Delta t and θ𝜃\theta in Equation [6](#S2.E6 "In 2.2 Weighted GHE’s ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"). Regarding the maximum τ𝜏\tau, we use 19 days, as prescribed in [[3](#bib.bib3), [2](#bib.bib2)]. Similarly to the standardized Hqsubscript𝐻𝑞H\_{q}, in order to detect statistically significant multiscaling at time t𝑡t, the ’width’ of the wGHE q𝑞q-spectrum for extreme q𝑞q values, q1subscript𝑞1q\_{1} and q2subscript𝑞2q\_{2} in respect, is also standardized as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wq1,q2′​(t)=W0.1,4​(t)σ​(Wq1,q2s​u​r​r),subscriptsuperscript𝑊′  subscript𝑞1subscript𝑞2𝑡subscript𝑊  0.14𝑡𝜎subscriptsuperscript𝑊𝑠𝑢𝑟𝑟  subscript𝑞1subscript𝑞2W^{\prime}\_{q\_{1},q\_{2}}(t)=\frac{W\_{0.1,4}(t)}{\sigma\left(W^{surr}\_{q\_{1},q\_{2}}\right)}, |  | (12) |

where σ​(Wq1,q2s​u​r​r)𝜎subscriptsuperscript𝑊𝑠𝑢𝑟𝑟

subscript𝑞1subscript𝑞2\sigma\left(W^{surr}\_{q\_{1},q\_{2}}\right) is the pooled standard deviation of the difference between surrogate series Hq1s​u​r​r​(t)subscriptsuperscript𝐻𝑠𝑢𝑟𝑟subscript𝑞1𝑡H^{surr}\_{q\_{1}}(t) and Hq2s​u​r​r​(t)subscriptsuperscript𝐻𝑠𝑢𝑟𝑟subscript𝑞2𝑡H^{surr}\_{q\_{2}}(t) given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(Wq1,q2s​u​r​r)=σ​(Hq1s​u​r​r)2+σ​(Hq2s​u​r​r)2,𝜎subscriptsuperscript𝑊𝑠𝑢𝑟𝑟  subscript𝑞1subscript𝑞2𝜎superscriptsubscriptsuperscript𝐻𝑠𝑢𝑟𝑟subscript𝑞12𝜎superscriptsubscriptsuperscript𝐻𝑠𝑢𝑟𝑟subscript𝑞22\sigma\left(W^{surr}\_{q\_{1},q\_{2}}\right)=\sqrt{\sigma\left(H^{surr}\_{q\_{1}}\right)^{2}+\sigma\left(H^{surr}\_{q\_{2}}\right)^{2}}, |  | (13) |

Finally, in order to compute the series of B​(t)𝐵𝑡B(t), we use the series Hq​(t)subscript𝐻𝑞𝑡H\_{q}(t) for several values of q𝑞q within a range q1′−q2′subscriptsuperscript𝑞′1subscriptsuperscript𝑞′2q^{\prime}\_{1}-q^{\prime}\_{2}. The number of q𝑞q values affects the accuracy of determining B​(t)𝐵𝑡B(t) by the least squares linear fit to Hqsubscript𝐻𝑞H\_{q} vs. q𝑞q data for each time t𝑡t. A number of about 20 q𝑞q are adequate for a good quality fit, yielding ’p-values’, on the average, above 0.98, and in the worst case (rare outliers) 0.85. Similar to W0.1,4′​(t)subscriptsuperscript𝑊′

0.14𝑡W^{\prime}\_{0.1,4}(t), we standardize B𝐵B by using the standard deviation of B𝐵B computed on the surrogate data, σ​(Bs​u​r​r)𝜎superscript𝐵𝑠𝑢𝑟𝑟\sigma\left(B^{surr}\right):

|  |  |  |  |
| --- | --- | --- | --- |
|  | B′​(t)=B​(t)σ​(Bs​u​r​r).superscript𝐵′𝑡𝐵𝑡𝜎superscript𝐵𝑠𝑢𝑟𝑟B^{\prime}(t)=\frac{B(t)}{\sigma\left(B^{surr}\right)}. |  | (14) |

σ​(Bs​u​r​r)𝜎superscript𝐵𝑠𝑢𝑟𝑟\sigma\left(B^{surr}\right) is calculated via Equation ([9](#S3.E9 "In 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) replacing Hq​(τ)subscript𝐻𝑞𝜏H\_{q}(\tau) by Bs​u​r​r​(τ)superscript𝐵𝑠𝑢𝑟𝑟𝜏B^{surr}(\tau).

Regarding the choice of the extreme values of q𝑞q, we used two sets: For the multiscaling width Wq1,q2subscript𝑊

subscript𝑞1subscript𝑞2W\_{q\_{1},q\_{2}}, we used a large span, q1=0.1subscript𝑞10.1q\_{1}=0.1 and q2=4subscript𝑞24q\_{2}=4, in order to capture the strong ’biasing’ effect of the tails of the price change distributions as it has been reported elsewhere [[24](#bib.bib24), [29](#bib.bib29)] for financial time-series. We want to include this ”biased” version of the width in order to capture the dynamics of such bias and spot any transitions it may reveal in time. For the multiscaling proxy B𝐵B, on the other hand, we used a short span q1′=0.1subscriptsuperscript𝑞′10.1q^{\prime}\_{1}=0.1 and q2′=1subscriptsuperscript𝑞′21q^{\prime}\_{2}=1 with a step of Δ​q=0.04Δ𝑞0.04\Delta q=0.04 in order to concentrate on the small q𝑞q values that mostly weigh the small price changes and thus emphasize the center of the price change distributions. The step of Δ​q=0.04Δ𝑞0.04\Delta q=0.04 provides 23 Hqsubscript𝐻𝑞H\_{q} values for each point in time t𝑡t, and thus the quality of the linear fit yielding B𝐵B is very good.

#### 3.2.1 Choice of Δ​tΔ𝑡\Delta t and θ𝜃\theta

One of the most important issues concerning the time-dependent wGHE’s is the choice of the Δ​tΔ𝑡\Delta t and θ𝜃\theta parameters which represent the size of the time window and the time weighting parameter within that window that directly pertain to the wGHE’s calculations. The optimum choice should be the result of a trade-off between reducing the finite-size effects (that increase the smaller Δ​tΔ𝑡\Delta t and θ𝜃\theta are), and capturing the short-term changes in multiscaling and wGHE’s, a task for which the smaller Δ​tΔ𝑡\Delta t and θ𝜃\theta, the better. If the time window length and time weighting parameter are too short, finite size effects will overwhelm the amount of multiscaling caused by the real dynamics. If, on the other hand, they are too large, finite size effects are ameliorated, but possible short-term multiscaling variations in the real dynamics are lost because they are averaged out in time. Moreover, the averaging-out effect may lead to another undesirable effect: to obtain spurious multiscaling estimation for the time period immediately after some extreme tail event which biases the width of the wGHE spectrum, especially for the large q𝑞q values. For example, if one picks Δ​t=750Δ𝑡750\Delta t=750 trading days, then a large tail event will cause a bias in the wGHE’s for a period of approximately 750 days (the characteristic decay time of the bias also depends on θ𝜃\theta). For a choice of Δ​t=120Δ𝑡120\Delta t=120 trading days instead, the forward in time ’contamination’ of the wGHE spectrum will have a much shorter duration, but finite-size effects will rise considerably for such small Δ​tΔ𝑡\Delta t. In order to make a proper choice, first of all we set Δ​t=θΔ𝑡𝜃\Delta t=\theta. This choice is arbitrary, but, without loss of generality, corresponds to a time window for which the last day in the past is weighted by a factor 1/e1𝑒1/e less than the most recent day. Then, Δ​tΔ𝑡\Delta t is determined by the rule that it should be: i) as small as possible (in order to capture short-term dynamical changes and avoid long-term ’contamination’ of multiscaling due to large tail events) and ii) sufficiently large that the noise level due to finite-size effects is satisfactorily low. In order to make a plausible choice meeting the above criteria, we calculated the width W1,4​(t)subscript𝑊

14𝑡W\_{1,4}(t) time-series with a range of Δ​tΔ𝑡\Delta t from 60-1250 trading days for the S&P 500 index as well as its random surrogate. Then, for each Δ​tΔ𝑡\Delta t, we calculate the average value of the width of the time-series and plot it v​s.𝑣𝑠vs. Δ​tΔ𝑡\Delta t in figure [1](#S3.F1 "Figure 1 ‣ 3.2.1 Choice of Δ⁢𝑡 and 𝜃 ‣ 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"). For the real index, error bars correspond to the standard error of the average, whereas for the surrogate index the error bars correspond to the standard deviation of the surrogate W1,4subscript𝑊

14W\_{1,4} time-series. We see that the average width decreases with Δ​tΔ𝑡\Delta t, both for the real index and the surrogate, as finite-size effects are reduced as Δ​tΔ𝑡\Delta t rises. For the real index, the average width naturally reaches a plateau that corresponds to the actual multiscaling strength (on the average) of the index, whereas for the random surrogate the width slowly drops to zero, the theoretical value for a random series. The dashed horizontal line in the figure shows the value of the plateau calculated as the average of the widths for Δ​t=250,375,500,750,1000Δ𝑡

2503755007501000\Delta t=250,375,500,750,1000 and 125012501250. We see that already for Δ​t∼250similar-toΔ𝑡250\Delta t\sim 250 the finite size effects have considerably reduced and the value of the average width of the real index has reached the plateau value well within standard error. We also see that ∼250similar-toabsent250\sim 250 is the smallest value of Δ​tΔ𝑡\Delta t for which the width of the real series is above at one standard deviation of the surrogate series average width, which means that for this value of Δ​tΔ𝑡\Delta t, the observed multiscaling is statistically strong (above the ’noise’ level). Finally, for each of the depicted values of Δ​tΔ𝑡\Delta t, we plot the rate of % improvement of the average width of the real series per day, if Δ​tΔ𝑡\Delta t is increased beyond each specific value shown. We observe that for the lowest values of Δ​tΔ𝑡\Delta t the rate of improvement is high. Again, Δ​t∼250similar-toΔ𝑡250\Delta t\sim 250 is the smallest value for which this rate significantly drops, which means that if Δ​tΔ𝑡\Delta t is increased beyond ∼250similar-toabsent250\sim 250 trading days, the improvement in noise level reduction is not significant. For all the above reasons we chose Δ​t=θ=250Δ𝑡𝜃250\Delta t=\theta=250 trading days as our optimum window size and time weighting factor.

![Refer to caption](/html/2010.08890/assets/FIGURES/OptimumTheta.png)


Figure 1:  Average width W1,4subscript𝑊

14W\_{1,4} of real S&P 500 and a random surrogate of the same data length as S&P 500 for various values of Δ​tΔ𝑡\Delta t. For calculations Δ​t=θΔ𝑡𝜃\Delta t=\theta. Error bars for the real series correspond to the standard error of the mean. Error bars for the surrogate series correspond to the standard deviation of the surrogate series W0.1,4subscript𝑊

0.14W\_{0.1,4}. The horizontal line shows the plateau the of the S&P 500 width. The % rate of reduction of the deviation of the width from the plateau value per one day increase in Δ​tΔ𝑡\Delta t is shown on the right axis.

### 3.3 wGHE’s vs. time

Before we proceed with our main analysis of the GHE time-series and the introduction of the scaling pattern identification methodology, we present in figure [2](#S3.F2 "Figure 2 ‣ 3.3 wGHE’s vs. time ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), the raw (not-standardized) time series of H0.1(θ)superscriptsubscript𝐻0.1𝜃H\_{0.1}^{(\theta)} and H4(θ)superscriptsubscript𝐻4𝜃H\_{4}^{(\theta)} for the S&P 500 index log prices and Δ​t=θ=250Δ𝑡𝜃250\Delta t=\theta=250 trading days together with the wGHE’s of the respective S&P 500 surrogate series. For comparison, in figure [3](#S3.F3 "Figure 3 ‣ 3.3 wGHE’s vs. time ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), we show the same quantities for Δ​t=θ=750Δ𝑡𝜃750\Delta t=\theta=750 trading days.333Throughout this paper, when we refer to the ’surrogate series’ of a particular stock market index, we mean the randomly generated index according to the procedure highlighted in section [2.3](#S2.SS3 "2.3 Surrogate stock market indices ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), where the surrogate series matches the temporal profile of the volatility of the real index. The width of each line shown corresponds to the uncertainty of the wGHE’s, which is equal to one standard deviation above and below the mean value of the wGHE’s, as determined by the fitting procedure in the GHE algorithm. This error depends on finite-size effects and varies significantly for each time segment considered based on the quality of the least squares fit in the GHE algorithm for a particular time segment. The error is larger the smaller the values of Δ​tΔ𝑡\Delta t (and θ𝜃\theta) and is also larger the bigger q𝑞q is, because high-q𝑞q GHE’s are more strongly affected by rare and large events. The average error for H1250subscriptsuperscript𝐻2501H^{250}\_{1} for the entire time-line is 0.028±0.014plus-or-minus0.0280.0140.028\pm 0.014 and the respective error for H4250subscriptsuperscript𝐻2504H^{250}\_{4} is 0.034±0.017plus-or-minus0.0340.0170.034\pm 0.017. As it is evident from figures [2](#S3.F2 "Figure 2 ‣ 3.3 wGHE’s vs. time ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") and [3](#S3.F3 "Figure 3 ‣ 3.3 wGHE’s vs. time ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), the two wGHE’s of the randomly generated surrogates are evenly distributed around 0.5, the expected value for a random series, whereas the the two wGHE’s of the real S&P 500 data clearly depart from these values. We also notice that, for the surrogate series, H1(θ)superscriptsubscript𝐻1𝜃H\_{1}^{(\theta)} and H4(θ)superscriptsubscript𝐻4𝜃H\_{4}^{(\theta)} evolve almost parallel to each other and are close to each other at all times, as expected for a uniscaling series. However, the two wGHE’s of the real time-series clearly differ at certain time periods and, at some periods, they even follow completely different trends. Notice that there are certain points in the series where H4(θ)subscriptsuperscript𝐻𝜃4H^{(\theta)}\_{4} shows an abrupt drop relative to H0.1(θ)subscriptsuperscript𝐻𝜃0.1H^{(\theta)}\_{0.1}, a drop which decays with a characteristic time that is proportional to θ𝜃\theta. These correspond (as we will discuss later in this paper) to large tail events (big rises or drops) that bias the value of the high q𝑞q wGHE. This biasing effect carries on in the future for a characteristic time proportional to Δ​tΔ𝑡\Delta t, the length of the averaging window for the wGHE calculations and is also dependent on θ𝜃\theta. This fact demonstrates why it is highly desirable to choose a Δ​tΔ𝑡\Delta t value as small as possible so that we avoid masking the true multiscaling for a prolonged time in the future of such large tail events, as long as finite size effects are also kept at an acceptably low level.

![Refer to caption](/html/2010.08890/assets/FIGURES/FIG1_SP500_RAW_theta=250.png)


Figure 2:  Time series of wGHE’s for q=0.1𝑞0.1q=0.1 and q=4𝑞4q=4 and θ=250𝜃250\theta=250 trading days of (a) the SP500 index log close prices and (b) the SP500 surrogate index log close prices. The width of each line is equal to two standard errors of Hqsubscript𝐻𝑞H\_{q} as determined by the least squares fitting performed by the GHE algorithm in [[30](#bib.bib30)].

![Refer to caption](/html/2010.08890/assets/FIGURES/FIG1_SP500_RAW_theta=750.png)


Figure 3:  Time series of wGHE’s for q=0.1𝑞0.1q=0.1 and q=4𝑞4q=4 and θ=250𝜃250\theta=250 trading days of (a) the SP500 index log close prices and (b) the SP500 surrogate index log close prices.

Table [2](#S3.T2 "Table 2 ‣ 3.3 wGHE’s vs. time ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") shows the mean values of H1subscript𝐻1H\_{1} and the extreme wGHE’s, H0.1subscript𝐻0.1H\_{0.1} and H4subscript𝐻4H\_{4}, as well as 𝔼​[|W0.1,4|]𝔼delimited-[]subscript𝑊

0.14\mathbb{E}\left[|W\_{0.1,4}|\right], the mean of the absolute value of the difference between the extreme-q𝑞q wGHE’s of the S&P 500 series and its respective surrogate. The mean values are calculated over the entire history of S&P 500 (≈1929absent1929\approx 1929 until Feb. 14, 2020) using Equations ([10](#S3.E10 "In 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) and ([11](#S3.E11 "In 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")). The standard error of the mean which depends on the uncertainty of determining each value of the exponent Hq​(t)subscript𝐻𝑞𝑡H\_{q}(t) from the GHE method is also shown preceded by ±plus-or-minus\pm sign. The standard deviations of the S&P 500 and its respective surrogate time-series, calculated by Equation ([9](#S3.E9 "In 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")), are also reported on a separate line together with their standard errors. The higher the value of 𝔼​[|W0.1,4|]𝔼delimited-[]subscript𝑊

0.14\mathbb{E}\left[|W\_{0.1,4}|\right] or B𝐵B, the more multiscaling the financial time-series is (on the overall). We see that the mean values of wGHE for q=1𝑞1q=1 of the real S&P 500 data are higher than 0.5 within standard error. The mean values of wGHE for q=4𝑞4q=4 are lower than 0.5 within standard error. Also, the mean absolute value of W0.1,4subscript𝑊

0.14W\_{0.1,4} and B𝐵B are also greater than 0, within standard error. All the above imply that, on the average, the S&P 500 index, during in its entire historical time span is characterised by multiscaling. Also, the fact that H1subscript𝐻1H\_{1} is also statistically greater than 0.5, suggests that S&P 500 has been, historically and on the average, a slightly persistent market. On the other hand, the average values of the respective quantities for the randomly generated surrogate S&P 500 time-series show that, on the average, all the Hurst exponents of a random time series with a varying volatility profile that matches that of the real series, shows neutral behavior. The above results agree with previous studies of the Hurst exponent of the S&P 500.

Table 2:  Statistics of wGHE’s for the SP500 index: comparison between real and surrogate data. θ=750𝜃750\theta=750 days.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | H0.1(θ)superscriptsubscript𝐻0.1𝜃H\_{0.1}^{(\theta)} | H1(θ)superscriptsubscript𝐻1𝜃H\_{1}^{(\theta)} | H4(θ)superscriptsubscript𝐻4𝜃H\_{4}^{(\theta)} | 𝔼​[|W0.1,4|]𝔼delimited-[]subscript𝑊  0.14\mathbb{E}\left[|W\_{0.1,4}|\right] | B𝐵B |
| S&P 500 | 0.55110.55110.5511  ±4.7​x​10−4plus-or-minus4.7𝑥superscript104\pm 4.7x10^{-4} | 0.52440.52440.5244  ±3.2​x​10−4plus-or-minus3.2𝑥superscript104\pm 3.2x10^{-4} | 0.44540.44540.4454  ±4.9​x​10−4plus-or-minus4.9𝑥superscript104\pm 4.9x10^{-4} | 0.10580.10580.1058  ±6.8​x​10−4plus-or-minus6.8𝑥superscript104\pm 6.8x10^{-4} | −0.029510.02951-0.02951  ±8.2​x​10−6plus-or-minus8.2𝑥superscript106\pm 8.2x10^{-6} |
| (Standard deviation) | 0.061010.061010.06101  ±7.1​x​10−6plus-or-minus7.1𝑥superscript106\pm 7.1x10^{-6} | 0.056710.056710.05671  ±4.8​x​10−6plus-or-minus4.8𝑥superscript106\pm 4.8x10^{-6} | 0.066230.066230.06623  ±8.8​x​10−6plus-or-minus8.8𝑥superscript106\pm 8.8x10^{-6} | 0.090030.090030.09003  ±1.1​x​10−5plus-or-minus1.1𝑥superscript105\pm 1.1x10^{-5} | 0.0200280.0200280.020028  ±2.0​x​10−7plus-or-minus2.0𝑥superscript107\pm 2.0x10^{-7} |
| Surrogate data | 0.49430.49430.4943  ±3.7​x​10−4plus-or-minus3.7𝑥superscript104\pm 3.7x10^{-4} | 0.49400.49400.4940  ±2.5​x​10−4plus-or-minus2.5𝑥superscript104\pm 2.5x10^{-4} | 0.48530.48530.4853  ±3.1​x​10−4plus-or-minus3.1𝑥superscript104\pm 3.1x10^{-4} | 0.00890.00890.0089  ±4.8​x​10−4plus-or-minus4.8𝑥superscript104\pm 4.8x10^{-4} | −0.0019760.001976-0.001976  ±4.8​x​10−7plus-or-minus4.8𝑥superscript107\pm 4.8x10^{-7} |
| (Standard deviation) | 0.036150.036150.03615  ±5.7​x​10−6plus-or-minus5.7𝑥superscript106\pm 5.7x10^{-6} | 0.034720.034720.03472  ±2.0​x​10−5plus-or-minus2.0𝑥superscript105\pm 2.0x10^{-5} | 0.043240.043240.04324  ±5.0​x​10−6plus-or-minus5.0𝑥superscript106\pm 5.0x10^{-6} | 0.056360.056360.05636  ±7.6​x​10−6plus-or-minus7.6𝑥superscript106\pm 7.6x10^{-6} | 0.0169430.0169430.016943  ±3.2​x​10−7plus-or-minus3.2𝑥superscript107\pm 3.2x10^{-7} |

Turning to the temporal evolution of Hqsubscript𝐻𝑞H\_{q} for various values of q𝑞q, it is already apparent from figures  [2](#S3.F2 "Figure 2 ‣ 3.3 wGHE’s vs. time ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") and [3](#S3.F3 "Figure 3 ‣ 3.3 wGHE’s vs. time ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") that persistence and multiscaling may vary with time as there are time periods when the index seems to be persistent, others when it is neutral and others when it is anti-persistent. Similarly, there are time periods when it is multiscaling and others where it is uniscaling indicated by the relative deviation between the H0.1subscript𝐻0.1H\_{0.1} and H4subscript𝐻4H\_{4}. There are also some time periods where H0.1subscript𝐻0.1H\_{0.1} and H4subscript𝐻4H\_{4} seem to evolve with similar local trend and some time periods where they seem to follow different or even opposite trends. The later signifies an anomalous kind of Hqsubscript𝐻𝑞H\_{q} profile evolution that is probably related to particular changes in the underlying dynamics of the market. In order to investigate these matters in more detail, we perform the analysis described in the next paragraphs.

First, we apply a 2nd-order polynomial smoothing filter to Hq(θ)′H\_{q}^{{}^{\prime}(\theta)} data for a time window of length equal to 240 trading days (  1 year) in order to reduce the noise and more clearly identify the underlying temporal patterns in the GHE spectra.

Next we inspect the smoothed Hq(θ)′H\_{q}^{{}^{\prime}(\theta)} series for S&P 500 log prices, and the five values q=0.1,1,2,3,4𝑞

0.11234q=0.1,1,2,3,4, as shown in figure [4](#S3.F4 "Figure 4 ‣ 3.3 wGHE’s vs. time ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"). We identify several distinct Temporal Patterns (TP) in the co-evolution of the series of the extreme q𝑞q’s (q=0.1,4𝑞

0.14q=0.1,4) based on:

1. 1.

   The standardized ’width’ W0.1,4′subscriptsuperscript𝑊′
   0.14W^{\prime}\_{0.1,4} of the wGHE q𝑞q-spectrum, as defined in Equation ([12](#S3.E12 "In 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")), which, as already said, is a measure of the multiscaling of the index at time t𝑡t. Looking at the co-evolution of the five Hq′subscriptsuperscript𝐻′𝑞H^{\prime}\_{q}’s shown in figure [4](#S3.F4 "Figure 4 ‣ 3.3 wGHE’s vs. time ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), we distinguish time periods where the five Hq′subscriptsuperscript𝐻′𝑞H^{\prime}\_{q}’s are very close to each other (signifying strongly uniscaling behavior), time periods where the five Hq′subscriptsuperscript𝐻′𝑞H^{\prime}\_{q}’s are clearly apart (signifying time periods of multiscaling) and time periods where they are strongly diverging, i.e. time periods where multiscaling is stronger. Therefore, we define three different levels of multiscaling by comparing W0.1,4′subscriptsuperscript𝑊′
   0.14W^{\prime}\_{0.1,4} to two threshold values ϕitalic-ϕ\phi: ϕLsubscriptitalic-ϕ𝐿\phi\_{L} and ϕHsubscriptitalic-ϕ𝐻\phi\_{H} which correspond to the low and high threshold values. If W0.1,4′​(t)>ϕHsubscriptsuperscript𝑊′
   0.14𝑡subscriptitalic-ϕ𝐻W^{\prime}\_{0.1,4}(t)>\phi\_{H} we consider that the index is characterized by strong multiscaling (denoted either by letter M or A), while, for small widths W0.1,4′​(t)≲ϕLless-than-or-similar-tosubscriptsuperscript𝑊′
   0.14𝑡subscriptitalic-ϕ𝐿W^{\prime}\_{0.1,4}(t)\lesssim\phi\_{L}), it is characterized as uniscaling (denoted by letter ’S’). For intermediate widths ϕL≲W0.1,4′​(t)≲ϕHless-than-or-similar-tosubscriptitalic-ϕ𝐿subscriptsuperscript𝑊′
   0.14𝑡less-than-or-similar-tosubscriptitalic-ϕ𝐻\phi\_{L}\lesssim W^{\prime}\_{0.1,4}(t)\lesssim\phi\_{H} we characterise it as ’weak multiscaling’ and denote it with the letter ML (or AL). Similarly, in the case we measure multiscaling by using the B𝐵B-proxy instead of W𝑊W, we use the standardized value B′superscript𝐵′B^{\prime} as defined in Equation ([14](#S3.E14 "In 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) and compare it to ϕLsubscriptitalic-ϕ𝐿\phi\_{L} and ϕHsubscriptitalic-ϕ𝐻\phi\_{H}. B′>ϕHsuperscript𝐵′subscriptitalic-ϕ𝐻B^{\prime}>\phi\_{H} denotes a strong multiscaling pattern (M or A) and B′<ϕLsuperscript𝐵′subscriptitalic-ϕ𝐿B^{\prime}<\phi\_{L} a uniscaling S pattern, whereas ϕL≲W0.1,4′​(t)≲ϕHless-than-or-similar-tosubscriptitalic-ϕ𝐿subscriptsuperscript𝑊′
   0.14𝑡less-than-or-similar-tosubscriptitalic-ϕ𝐻\phi\_{L}\lesssim W^{\prime}\_{0.1,4}(t)\lesssim\phi\_{H} a ’weak multiscaling’ ML or AL pattern.
2. 2.

   The difference between the ’local trends’ of the extreme wGHE curves H0.1′​(t)subscriptsuperscript𝐻′0.1𝑡H^{\prime}\_{0.1}(t) and H4′​(t)subscriptsuperscript𝐻′4𝑡H^{\prime}\_{4}(t) at time t𝑡t. The local trends could be defined as the time derivative of the wGHE series at time t𝑡t, but in order to get a statistically significant measure we use the Change Point Analysis method (CPA), as will described later in the paper. We denote by letter M (stands for ’muliscaling’) or ML (stands for ’low’ multiscaling), a wide TP, as determined by the procedure described in the previous point, for which the local trends are statistically equal. In an M (or ML) pattern, the extreme Hqsubscript𝐻𝑞H\_{q} time-series move parallel to each other and thus the width W𝑊W remains statistically unchanged. Conversely, we denote by letter A (or AL) (stands for ’asymmetric’ multiscaling) a wide TP, in which the extreme wGHE’s evolve in statistically different directions and/or different rates.
3. 3.

   The ’asymmetry’ in local trends: ’A’ patterns can come in the following three variations: (i) an A-: a TP in which H4subscript𝐻4H\_{4} drops at a rate faster than H0.1subscript𝐻0.1H\_{0.1} either drops or rises; (ii) A+: a TP in which H0.1subscript𝐻0.1H\_{0.1} rises at a rate faster than H4subscript𝐻4H\_{4} either drops or rises; (iii) A0 a TP in which H0.1subscript𝐻0.1H\_{0.1} rises at approximately the same rate as H4subscript𝐻4H\_{4} drops; (iv) mA- is a pattern in which H4subscript𝐻4H\_{4} rises at a rate faster than H0.1subscript𝐻0.1H\_{0.1} either drops or rises444The prefix m𝑚m stands for mirror image of the pattern.; (v) mA+ is a pattern in which H0.1subscript𝐻0.1H\_{0.1} drops at a rate faster than H4subscript𝐻4H\_{4} either drops or rises; (vi) mA0 is a pattern in which H0.1subscript𝐻0.1H\_{0.1} drops at approximately the same rate as H4subscript𝐻4H\_{4} rises. For the ’weakly multiscaling’ asymmetric TP’s AL, we do not define any ’+’ or ’-’ TP’s, just the diverging TP AL and the converging (mirror) TP m​AL𝑚superscript𝐴𝐿mA^{L}.
4. 4.

   The relative variation among the GHE’s across the q𝑞q values, e.g. the ordering of the GHE’s vs. q𝑞q at a particular time instance. Specifically, in some time periods the concavity relation can be violated giving way to a ’reversed’ TP, in which wGHE’s of higher q𝑞q’s are larger than wGHE’s of smaller q𝑞q’s. We denote such TPs by attaching the prefix ’r’ to the symbols of any of the above TPs. It is important to highlight that ’reversal’ is a particularly rare phenomenon as it entails the effect for which dependence would be stronger for tail events than for common events. ’Reversal’, however, is realistically expected for severe crisis periods, where the price change distribution strongly deviates from a Gaussian distribution and tail events are very frequent and highly correlated.
5. 5.

   The transition state from a uniscaling period to a multiscaling period and vice-versa. In case we have a weakly multiscaling TP for which the extreme wGHE’s seem to diverge tending to turn into a multiscaling pattern, then, if at a particular time t𝑡t, W0.1,4′>ϕLsubscriptsuperscript𝑊′
   0.14subscriptitalic-ϕ𝐿W^{\prime}\_{0.1,4}>\phi\_{L} (or B′>ϕLsuperscript𝐵′subscriptitalic-ϕ𝐿B^{\prime}>\phi\_{L}) and the local trends of the extreme wGHE’s are statistically diverging, we define a ’transition’, weakly-multiscaling TP, that we denote by AL. If, on the other hand, the local trends of the extreme wGHE’s are statistically converging, then define a ’transition’ weakly-multiscaling TP that we denote by m​AL𝑚superscript𝐴𝐿mA^{L}, i.e. the ’mirror’ AL.

In figure [5](#S3.F5 "Figure 5 ‣ 3.3 wGHE’s vs. time ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") we summarize and schematically present the TP’s described above.

![Refer to caption](/html/2010.08890/assets/FIGURES/Fig02_SP500_PATTERN_DEFINITION_W0_14.png)


Figure 4:  Temporal patterns in wGHE time-series for the S&P 500 index for the period Jan. 2, 1970 to Jan. 2, 2013.

![Refer to caption](/html/2010.08890/assets/FIGURES/patterns_recognition.png)


Figure 5:  Schematic depiction of GHE TP’s. In the upper plot, a schematic representation of two Hqsubscript𝐻𝑞H\_{q} time-series is shown for the extreme q′​ssuperscript𝑞′𝑠q^{\prime}s. Blue color represents the minimum q𝑞q series and the red color the maximum q𝑞q series. In the lower plot, the respective TP’s are labeled.

### 3.4 TP identification algorithmic procedure

In this section we present the algorithmic procedure to extract the TPs from wGHE’s series in a statistically rigorous way. The procedure contains the following steps:

1. 1.

   First, select the standardized metric γ′superscript𝛾′\gamma^{\prime} to be used as a measure of multiscaling: γ′=Wq1,q2′superscript𝛾′subscriptsuperscript𝑊′
   subscript𝑞1subscript𝑞2\gamma^{\prime}=W^{\prime}\_{q\_{1},q\_{2}} or γ′=Bq1′,q2′′superscript𝛾′subscriptsuperscript𝐵′
   subscriptsuperscript𝑞′1subscriptsuperscript𝑞′2\gamma^{\prime}=B^{\prime}\_{q^{\prime}\_{1},q^{\prime}\_{2}}, as well as the respective pair of extreme Hq1′subscriptsuperscript𝐻′subscript𝑞1H^{\prime}\_{q\_{1}} and Hq2′subscriptsuperscript𝐻′subscript𝑞2H^{\prime}\_{q\_{2}} time-series that will be used for determining the local trends. Select a θ𝜃\theta value and a sliding window length Δ​tΔ𝑡\Delta t and compute the relative wGHE’s for both the real series and a random surrogate, with log-returns drawn from a normal distribution standard deviation equal to the volatility profile of the real series. Compute the relevant standard deviations of the surrogate series from Equations ([9](#S3.E9 "In 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) and ([13](#S3.E13 "In 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) and obtain the standardized series from Equations ([8](#S3.E8 "In 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")), ([12](#S3.E12 "In 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) or ([14](#S3.E14 "In 3.2 Standardized GHE, multiscaling proxies and parameter definition ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")). If γ′superscript𝛾′\gamma^{\prime} is set equal to Bq1′,q2′′subscriptsuperscript𝐵′
   subscriptsuperscript𝑞′1subscriptsuperscript𝑞′2B^{\prime}\_{q^{\prime}\_{1},q^{\prime}\_{2}}, then compute several series Hqsubscript𝐻𝑞H\_{q} between the chosen extreme values. In this work we calculated a set of Hqsubscript𝐻𝑞H\_{q}’s in the range q=0.1−1𝑞0.11q=0.1-1 with extreme series the ones for q1′=0.1subscriptsuperscript𝑞′10.1q^{\prime}\_{1}=0.1 and q2′=1subscriptsuperscript𝑞′21q^{\prime}\_{2}=1. Then, for each each time t𝑡t, apply a linear least squares fit to the data Hq​(t)subscript𝐻𝑞𝑡H\_{q}(t) vs. q𝑞q, the slope of which is equal to B​(t)𝐵𝑡B(t). For γ′=Wq1,q4′superscript𝛾′subscriptsuperscript𝑊′
   subscript𝑞1subscript𝑞4\gamma^{\prime}=W^{\prime}\_{q\_{1},q\_{4}}, we chose q1=0.1subscript𝑞10.1q\_{1}=0.1 and q4=4subscript𝑞44q\_{4}=4, in the present work.
2. 2.

   Smooth out the computed raw standardized series using a 2nd order polynomial smoothing function. We used a smoothing window of 48 data points which (for a skipping window of 5 trading days that we used for wGHE calculations) corresponds to 240 trading days, i.e. approximately one calendar year.
3. 3.

   Apply the Change Point Analysis algorithm (CPA) ([[47](#bib.bib47)]) to the two extreme series Hq1′subscriptsuperscript𝐻′subscript𝑞1H^{\prime}\_{q\_{1}} and Hq2′subscriptsuperscript𝐻′subscript𝑞2H^{\prime}\_{q\_{2}}, in order to get time intervals characterized by the same local trend (rate of increase of the wGHE’s) as well as to obtain the values of the trends. The same or different segment limits can be chosen (same ’binning’) for the two series. If the same binning is selected (we chose this option in the present work), then, in practice, CPA is applied to one of the two series (or alternatively to the γ𝛾\gamma series), and the automatically extracted bin limits are then enforced on the application of CPA to the other series. The CPA analysis breaks the series into a set of several segments of potentially different lengths {Δ​ti}Δsubscript𝑡𝑖\{\Delta t\_{i}\}, and outputs a unique slope value, βiq1superscriptsubscript𝛽𝑖subscript𝑞1\beta\_{i}^{q\_{1}} and βiq2superscriptsubscript𝛽𝑖subscript𝑞2\beta\_{i}^{q\_{2}} for each segment i𝑖i and for the respective standardized wGHE series for q1subscript𝑞1q\_{1} and q2subscript𝑞2q\_{2}.
4. 4.

   For each data point at time t𝑡t, statistically determine the degree of multiscaling by checking the statistical significance of γ′superscript𝛾′\gamma^{\prime} against the predefined threshold value ϕLsubscriptitalic-ϕ𝐿\phi\_{L} and ϕHsubscriptitalic-ϕ𝐻\phi\_{H}: if γ′>ϕHsuperscript𝛾′subscriptitalic-ϕ𝐻\gamma^{\prime}>\phi\_{H}, then the dynamics of the underlying series is multiscaling (M-type or the various A-type TP’s), else if γ′<ϕLsuperscript𝛾′subscriptitalic-ϕ𝐿\gamma^{\prime}<\phi\_{L}, it is characterised as uniscaling (S), else it is characterised as ’weakly multiscaling’ (ML-type or AL/m​AL𝑚superscript𝐴𝐿mA^{L}-type TP’s). ϕLsubscriptitalic-ϕ𝐿\phi\_{L} should, in general be much smaller than 1 and ϕHsubscriptitalic-ϕ𝐻\phi\_{H} greater than 1. In the present work, we use ϕL=0.32subscriptitalic-ϕ𝐿0.32\phi\_{L}=0.32 and ϕH=1.64subscriptitalic-ϕ𝐻1.64\phi\_{H}=1.64 as threshold values, which correspond to the 25t​hsuperscript25𝑡ℎ25^{th} and 95t​hsuperscript95𝑡ℎ95^{th} percentile of the Gaussian distribution in respect. Other choices are of course possible. The rationale behind the particular choices is that the limit for true uniscaling should be considerably lower than the ’noise level’ of W𝑊W, as defined by 1 standard deviation of the random surrogate, while the limit for strong multiscaling should be significantly higher than the noise level. Therefore, ϕL=0.32subscriptitalic-ϕ𝐿0.32\phi\_{L}=0.32 signifies that only 25% of the widths W′superscript𝑊′W^{\prime} in a random time-series are below this threshold and thus the scaling of the real series at any point in time for which W′superscript𝑊′W^{\prime} is smaller than this value can be characterized as uniscaling in a statistically significant manner. Similarly, ϕH=1.64subscriptitalic-ϕ𝐻1.64\phi\_{H}=1.64 signifies that only 5% of the widths in the random time-series are above this limit, therefore the scaling of the real series at any point in time for which W′superscript𝑊′W^{\prime} is greater than this value can be characterized as multiscaling in a statistically significant manner. Finally, for times when W′superscript𝑊′W^{\prime} values are between these values the scaling is characterized as ”weak’ multiscaling.
5. 5.

   For each data point on day t𝑡t, compare the relative slopes of the extreme wGHE series, as extracted by CPA, at the time bin i𝑖i to which t𝑡t belongs, in order to detect the different forms of multiscaling, i.e. to identify whether the TP is an M-type or an A-type. In particular, to designate an A pattern, we require that the absolute difference in the slopes should be ϕSsubscriptitalic-ϕ𝑆\phi\_{S} standard deviations above 0, i.e.:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | |βiq1−βiq2|σ​(|βs​u​r​rq1−βs​u​r​rq2|)>ϕS,superscriptsubscript𝛽𝑖subscript𝑞1superscriptsubscript𝛽𝑖subscript𝑞2𝜎superscriptsubscript𝛽𝑠𝑢𝑟𝑟subscript𝑞1superscriptsubscript𝛽𝑠𝑢𝑟𝑟subscript𝑞2subscriptitalic-ϕ𝑆\frac{|\beta\_{i}^{q\_{1}}-\beta\_{i}^{q\_{2}}|}{\sigma(|\beta\_{surr}^{q\_{1}}-\beta\_{surr}^{q\_{2}}|)}>\phi\_{S}, |  | (15) |

   where βiq1superscriptsubscript𝛽𝑖subscript𝑞1\beta\_{i}^{q\_{1}}, βiq2superscriptsubscript𝛽𝑖subscript𝑞2\beta\_{i}^{q\_{2}} are the slopes of Hq1subscript𝐻subscript𝑞1H\_{q\_{1}} and Hq2subscript𝐻subscript𝑞2H\_{q\_{2}} at bin i𝑖i, and βs​u​r​rq1superscriptsubscript𝛽𝑠𝑢𝑟𝑟subscript𝑞1\beta\_{surr}^{q\_{1}}, βs​u​r​rq2superscriptsubscript𝛽𝑠𝑢𝑟𝑟subscript𝑞2\beta\_{surr}^{q\_{2}} is the respective pair of slopes computed on the surrogate data, σ​(…)𝜎…\sigma(...) denotes the standard deviation of the series and ϕSsubscriptitalic-ϕ𝑆\phi\_{S} is the threshold of the evaluation.555In general, one could use different thresholds ϕitalic-ϕ\phi between the width test involved in multiscaling vs. uniscaling characterizations, and the slope tests involved in the type of multiscaling characterizations. In the present work, we chose the same value ϕS=1.64subscriptitalic-ϕ𝑆1.64\phi\_{S}=1.64 (as ϕHsubscriptitalic-ϕ𝐻\phi\_{H}) for all tests. In other words, this formulation returns an ’A’ pattern only if it is statistically greater than the variability of the local trends of the surrogate index, as measured by applying a similar CPA procedure to the extreme series, Hq1subscript𝐻subscript𝑞1H\_{q\_{1}} and Hq2subscript𝐻subscript𝑞2H\_{q\_{2}} of the random surrogate data. In practice, one can use the same binning on the surrogate data as determined by the CPA of the real data, which is what we did in the present work.
6. 6.

   If Wq1,q2′>ϕHsubscriptsuperscript𝑊′
   subscript𝑞1subscript𝑞2subscriptitalic-ϕ𝐻W^{\prime}\_{q\_{1},q\_{2}}>\phi\_{H}, then distinguish among the various A𝐴A-type multiscaling TP’s. At first, compare the absolute value of the difference of absolute values of the local trends βiq1superscriptsubscript𝛽𝑖subscript𝑞1\beta\_{i}^{q\_{1}} and βiq1superscriptsubscript𝛽𝑖subscript𝑞1\beta\_{i}^{q\_{1}}. We check its statistical significance by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ||βtq1|−|βtq2|σ​(|βs​u​r​rq1|−|βs​u​r​rq2|)|>ϕS.superscriptsubscript𝛽𝑡subscript𝑞1superscriptsubscript𝛽𝑡subscript𝑞2𝜎superscriptsubscript𝛽𝑠𝑢𝑟𝑟subscript𝑞1superscriptsubscript𝛽𝑠𝑢𝑟𝑟subscript𝑞2subscriptitalic-ϕ𝑆\left\lvert\frac{|\beta\_{t}^{q\_{1}}|-|\beta\_{t}^{q\_{2}}|}{\sigma(|\beta\_{surr}^{q\_{1}}|-|\beta\_{surr}^{q\_{2}}|)}\right\rvert>\phi\_{S}. |  | (16) |

   If this condition is false, then the TP is an A0. If it is true, then it is either an A- or A+ or one of their respective mirrors mA-, mA+. In the later case, in order to determine which one of the four, compare the absolute values of the two β𝛽\beta’s and also use the sign of each β𝛽\beta. Specifically:

   * i

     if |βtq1|<|βtq2|superscriptsubscript𝛽𝑡subscript𝑞1superscriptsubscript𝛽𝑡subscript𝑞2|\beta\_{t}^{q\_{1}}|<|\beta\_{t}^{q\_{2}}| and βtq2<0superscriptsubscript𝛽𝑡subscript𝑞20\beta\_{t}^{q\_{2}}<0, it is A-,
   * ii

     if |βtq1|<|βtq2|superscriptsubscript𝛽𝑡subscript𝑞1superscriptsubscript𝛽𝑡subscript𝑞2|\beta\_{t}^{q\_{1}}|<|\beta\_{t}^{q\_{2}}| and βtq2>0superscriptsubscript𝛽𝑡subscript𝑞20\beta\_{t}^{q\_{2}}>0, it is mA-,
   * iii

     if |βtq1|>|βtq2|superscriptsubscript𝛽𝑡subscript𝑞1superscriptsubscript𝛽𝑡subscript𝑞2|\beta\_{t}^{q\_{1}}|>|\beta\_{t}^{q\_{2}}| and βtq2>0superscriptsubscript𝛽𝑡subscript𝑞20\beta\_{t}^{q\_{2}}>0, it is A+
   * iv

     |βtq1|>|βtq2|superscriptsubscript𝛽𝑡subscript𝑞1superscriptsubscript𝛽𝑡subscript𝑞2|\beta\_{t}^{q\_{1}}|>|\beta\_{t}^{q\_{2}}| and βtq2<0superscriptsubscript𝛽𝑡subscript𝑞20\beta\_{t}^{q\_{2}}<0, it is mA+.
7. 7.

   If ϕL<Wq1,q2′<ϕHsubscriptitalic-ϕ𝐿subscriptsuperscript𝑊′
   subscript𝑞1subscript𝑞2subscriptitalic-ϕ𝐻\phi\_{L}<W^{\prime}\_{q\_{1},q\_{2}}<\phi\_{H}, then distinguish between the AL TP and the m​AL𝑚superscript𝐴𝐿mA^{L} TP, the first corresponding to diverging weakly multiscaling asymmetric patterns and the second to a converging one. The first often precedes a transition between an uniscaling state (S) to an M or ML multiscaling state. The second precedes the reverse transition, i.e. from a multiscaling to a uniscaling state. The condition is that the relative trends βtq1superscriptsubscript𝛽𝑡subscript𝑞1\beta\_{t}^{q\_{1}} and βtq2superscriptsubscript𝛽𝑡subscript𝑞2\beta\_{t}^{q\_{2}} are sufficiently different, i.e. they satisfy condition ([15](#S3.E15 "In item 5 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) and:

   * i

     βtq1>βtq2superscriptsubscript𝛽𝑡subscript𝑞1superscriptsubscript𝛽𝑡subscript𝑞2\beta\_{t}^{q\_{1}}>\beta\_{t}^{q\_{2}}, then the TP is an AL else
   * ii

     βtq1>βtq2superscriptsubscript𝛽𝑡subscript𝑞1superscriptsubscript𝛽𝑡subscript𝑞2\beta\_{t}^{q\_{1}}>\beta\_{t}^{q\_{2}}, then it is an m​AL𝑚superscript𝐴𝐿mA^{L}.
8. 8.

   In case of ’reversal’, i.e. if Hq1′<Hq2′subscriptsuperscript𝐻′subscript𝑞1subscriptsuperscript𝐻′subscript𝑞2H^{\prime}\_{q\_{1}}<H^{\prime}\_{q\_{2}}: then one must simply interchange H0.1′subscriptsuperscript𝐻′0.1H^{\prime}\_{0.1} with H4′subscriptsuperscript𝐻′4H^{\prime}\_{4} in the equations presented in all the above points. The resulting TP’s will be the ’reverse’ TP denoted by an extra letter ’r’ in front of the respective TP symbol.

The results of the TP identification analysis presented above, as applied to the S&P 500, NIKKEI, ASE and SENSEX indices are shown in figures [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")-[9](#S3.F9 "Figure 9 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"). In each of these figures the following are plotted: In (a) the weighted volatility series of the index (left axis), calculated by Equation ([7](#S2.E7 "In 2.2 Weighted GHE’s ‣ 2 Description of methods ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")), and the index close prices (right axis); in (b) the normalized wGHE’s H′​(q)superscript𝐻′𝑞H^{\prime}(q) time-series of the index for q=0.1,1.2.3.4𝑞

0.11.2.3.4q=0.1,1.2.3.4, where we have marked the identified TP’s by setting γ′=W0.1,4′superscript𝛾′subscriptsuperscript𝑊′

0.14\gamma^{\prime}=W^{\prime}\_{0.1,4} and using H0.1′subscriptsuperscript𝐻′0.1H^{\prime}\_{0.1} and H4′subscriptsuperscript𝐻′4H^{\prime}\_{4} for the extreme wGHE’s. TP’s are marked by color mapping; in (c) the time evolution of the normalized wGHE width W0.1,4′subscriptsuperscript𝑊′

0.14W^{\prime}\_{0.1,4} together with the width of the respective surrogate index; in (d) the H′​(q)superscript𝐻′𝑞H^{\prime}(q) time-series for q=0.1,0.5,1𝑞

0.10.51q=0.1,0.5,1 with the identified TPs by setting γ=−B𝛾𝐵\gamma=-B and using H0.1′subscriptsuperscript𝐻′0.1H^{\prime}\_{0.1} and H1′subscriptsuperscript𝐻′1H^{\prime}\_{1} for the extreme wGHE’s. TPs are also marked by the same color mapping as in plots (b). Finally, in (e) we show the B proxy time-series of the real index together with the respective B proxy of the surrogate index.

By examining figures [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") - [9](#S3.F9 "Figure 9 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), we notice several interesting facts:

1. 1.

   As clearly seen from plots (b) and (c), the scaling of the various indexes varies significantly with time: there are certain time periods when W0.1,4′subscriptsuperscript𝑊′
   0.14W^{\prime}\_{0.1,4} is much higher than the average width of the GHE spectrum of the surrogate index, signifying a definite multiscaling structure of the underlying dynamics, while there are time periods when W0.1,4′subscriptsuperscript𝑊′
   0.14W^{\prime}\_{0.1,4} is very small, signifying a uniscaling structure. Moreover, the transition between a period of multiscaling behavior to a period of uniscaling behavior can be rather sharp, a fact that alludes to the existence of transition occurring in the underlying index dynamics.
2. 2.

   There are time periods of persistent behaviour (H1(θ)′>0H\_{1}^{{}^{\prime}(\theta)}>0), time periods of anti-persistent behavior (H1(θ)′<0H\_{1}^{{}^{\prime}(\theta)}<0) and time periods of neutral behavior (H1(θ)′≈0H\_{1}^{{}^{\prime}(\theta)}\approx 0). If one generalizes the notion of ’persistence’ to include GHE’s of q𝑞q values different from 1, then there are time periods when the small q𝑞q GHE’s rise or stay approximately the same, while H4′subscriptsuperscript𝐻′4H^{\prime}\_{4} is dropping, i.e. moving in the opposite direction to a more ’anti-persistent’ scaling. This behavior, which is characterised by A0 or A- TPs, is connected to one or more isolated, large price change events (tail events) that occur in a direction opposite to the local market trend (e.g. a large price drop in an otherwise rising market or vice-versa). A notable example is the ’Black Monday’ event that occurred on Monday, Oct. 19th 1987 (and Tuesday Oct. 20 in some markets), where S&P 500 (arrow 6), for example, lost more than 20% in one day. The event was followed by a large rise in the next day and the index made up for all the losses soon after. ’Black Monday’ occurred amidst a bullish market period and was similarly followed by a rising trend. A single tail event of this size causes a large bias, especially in the high q𝑞q wGHE’s, hence the pronounced A- TP is observed, as appears in figures [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")b and [7](#S3.F7 "Figure 7 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")b for both S&P 500 and NIKKEI (arrow No 4). Such TP’s are also seen after the ’Asian’ and the ’Russian’ related crises drops in 1997 and 1998666For the related dates of these isolated market drops, see table [3](#S3.T3 "Table 3 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"). in respect, which also occurred amidst a rising market and in several other occasions along the index price timeline such as, for example: (i) S&P 500: April, 16-17, 1935 when a ≈9%absentpercent9\approx 9\% drop is followed by a ≈9%absentpercent9\approx 9\% rise, May, 16-17, 1935 when a ≈7%absentpercent7\approx 7\% drop was followed by a ≈9.4%absentpercent9.4\approx 9.4\% rise and August 16,19, 1935, when a ≈8%absentpercent8\approx 8\% drop was followed by a ≈7%absentpercent7\approx 7\% rise (arrow No 1 in figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")). (ii) NIKKEI: June, 26-27, 1972 when a ≈8%absentpercent8\approx 8\% drop was followed by a ≈5.3%absentpercent5.3\approx 5.3\% rise (arrow No 2 in figure [7](#S3.F7 "Figure 7 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")), Jun., 26-27, 1972 when a ≈+4%absentpercent4\approx+4\% rise occurs amidst a dropping trend (arrow No 3 in figure [7](#S3.F7 "Figure 7 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")). Notably, these A- patterns are not present in the B-proxy series shown in plots (d) of the said figures, since the small q𝑞q wGHE’s are not so much affected by tail events, except for the 1935 large A- TP for S&P 500 which appears there too, because that particular TP was caused by several more than one big tail events over an extended period of time. However, there are time periods when the small q𝑞q wGHE’s show a sharp rise while the H4′subscriptsuperscript𝐻′4H^{\prime}\_{4} drops or is almost unchanged (a behavior that yields an A+ TP). This behavior hints to a situation where a one or more large events occur in the same direction as the current market trend, meaning that they give a large ’persistent’ boost in the small q𝑞q Hq′subscriptsuperscript𝐻′𝑞H^{\prime}\_{q}’s. An example of the latter behavior is in the 2008 real estate crisis (arrow No 9 in figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")), an exogenous to stock-market event, where large index price drops occurred amidst a period of a rapidly falling market, evidence of persistent ’herding’ behavior following the 2008 crash. These few large drops cause a sharp rise in H0.1′subscriptsuperscript𝐻′0.1H^{\prime}\_{0.1} and H1′subscriptsuperscript𝐻′1H^{\prime}\_{1}, rather than a drop in H4′subscriptsuperscript𝐻′4H^{\prime}\_{4}. The same pattern is seen in 2012 for S&P 500, where the observed A+limit-from𝐴A+ TP is a result of big daily rises amidst a rising market period. One more example of an A+ TP coming from several big rising events amidst a period of rising rising market trend is the one shown by arrow No 4 in figure  [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), in period May, 1955-Sep. 1956. Finally, there are other time periods when the scaling is consistently persistent (or anti-persistent, or neutral) for all values of q𝑞q, meaning that either the period is void of large rising or dropping events and/or that both large and small events follow the same scaling behavior.
3. 3.

   Multiscaling behavior is not necessarily correlated with periods of increased index volatility or periods of persistent scaling: there are time periods showing both high volatility and multiscaling/persistent behaviour, as well as time periods with low-volatility and multiscaling/anti-persistent behaviour. Time periods when volatility and multiscaling are positively correlated, include those which contain a single extreme market drop tail event, which is sufficiently large to impact both volatility and GHE calculations. An example of this fact is seen in the period 1987-1988, following ’Black Monday’. As an example of a period showing a large increase in multiscaling strength, while volatility remains low, we mention the first semester of 1993 for S&P 500. During this period, we observe a type of asymmetric multiscaling which is the product of a sequence of smaller tail events, distributed over a longer period of time and also depends on how these events are temporarily correlated. Notice also, that A- TP’s caused by a single tail event (that necessarily leads to a sharp volatility rise as well) and A- TP’s caused by temporal correlations and tail events distributed over an extended period of time, also have different shapes: in the first case, the width of the TP decays (following the characteristic rate that depends on the choice of θ𝜃\theta), whereas, in the second case, it does not decay immediately, but remains wide for a longer time while the variation of its width does not depend on the choice of θ𝜃\theta.
4. 4.

   At the beginning of a bubble, a strong uniscaling behaviour is observed at which the investor heterogeneity seems to be low. Whilst the market starts to grow, the complexity of the time series appears to increase in both measures of multiscaling through an asymmetric TP (usually A- or AL) and then comes back to uniscaling or moderate multiscaling after the bubble has exploded. This is apparent in both Dot.com bubble and the US real estate bubble, but also in ASE 2000 bubble, in ASE 1990 crash as well as the Japanese 1991 bubble. It is even apparent before the ’Black Monday’ crash, both for NIKKEI and S&P 500, when we notice a clear transition from uniscaling to strong multiscaling via an AL TP starting back in 1986. In general, before any critical event we necessarily have a transition from uniscaling to multiscaling ranging from a few months to a couple of years before the beginning of the bubble break or crash. It must be noted that the A-/AL/A0 type TP’s that we encounter in these transitions are not the ’after-effect’ of single large tail market events, but rather the consequence of a transition to multiscaling behavior due to smaller tail events occurring over a prolonged period. Examples of such TP’s are: (i) S&P 500 1956-1957 (arrow No 5 in figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")), an AL TP followed by a an A0 TP which was actually followed by a small crash (micro-bubble) at the last quarter of 1957, (ii) S&P 500 1961, an A- TP that was followed by a small crash in 1962, (iii) ASE: the pronounced A--A0-A+-A0 sequence before the ASE big 2000 bubble, as well as the A--A0 TP before the 1990 crash. (iv) The AL TP’s just before the 2000 ’dot.com’ bubble in S&P 500 (arrow No 8 in figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")), NIKKEI (arrow No 5 in figure [7](#S3.F7 "Figure 7 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) and SENSEX (arrow No 1 in figure [9](#S3.F9 "Figure 9 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")). (v) The AL TP’s just before the 2008 US real-estate crisis in S&P 500 (arrow No 9 in figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")), NIKKEI (arrow No 6 in figure [7](#S3.F7 "Figure 7 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")), ASE (arrow No 6 in figure [8](#S3.F8 "Figure 8 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")) and SENSEX (arrow No 3 in figure [9](#S3.F9 "Figure 9 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")). See also, the plots in the Appendix, showing zoomed versions of some particular time periods for S&P 500 and NIKKEI.
5. 5.

   The multiscaling width W0.1,4subscript𝑊
   0.14W\_{0.1,4} and multiscaling depth B𝐵B convey different information in some cases. For example, during the 2008 great financial crisis, W0.1,4subscript𝑊
   0.14W\_{0.1,4} doesn’t increase too much while B𝐵B increases sharply. This is because W0.1,4subscript𝑊
   0.14W\_{0.1,4} better captures the heterogeneity in the market, which is, to some extent, lower when all investors go in the same direction (selling orders), while B𝐵B measures the complexity of such heterogeneity, as the distribution of Hqsubscript𝐻𝑞H\_{q} inside a range of q’s matters instead of only its boundary values, as we also mentioned above.
6. 6.

   Multiscaling does not necessarily imply bad market conditions. When we have multiscaling of type M, it usually reflects good market conditions, even if there is increased heterogeneity (and complexity) in the market.
7. 7.

   Multiscaling time periods detected by the GHE spectrum curvature B𝐵B is on the overall in line with the ones detected with W𝑊W. However, some differences are observed in specific time periods. In particular, during crisis events, the B𝐵B is more symmetrically multiscaling while W𝑊W shows many more asymmetries. This is due to the fact that W𝑊W is affected by the tails of price change distributions considerably more than B𝐵B. In general, it is useful to look at both measures of multiscaling as they emphasize the opposite ends of the price change distribution (small large changes) and thus are complementary to each other.

![Refer to caption](/html/2010.08890/assets/FIGURES/SP500_final_arrow.png)


Figure 6:  SP500 index price time-series and scaling TPs: (a) Index closing prices and weighted volatility (b) Normalized wGHE’s for q=0.1,1,2,3,4𝑞

0.11234q=0.1,1,2,3,4 with identified TPs using H​(0.1)𝐻0.1H(0.1), H​(4)𝐻4H(4) and γ=W0​.1,4𝛾

subscript𝑊0.14\gamma=W\_{0}.1,4. (c) Width W0.1,4′subscriptsuperscript𝑊′

0.14W^{\prime}\_{0.1,4} of the S&P 500 normalized GHE’s for the real index data and the respective surrogate data. (d) Normalized wGHE’s for q=0.1,0.5,1𝑞

0.10.51q=0.1,0.5,1 with identified TPs using H​(0.1)𝐻0.1H(0.1), H​(1)𝐻1H(1) and γ=−B𝛾𝐵\gamma=-B. (e) B𝐵B proxy of the S&P 500 normalized GHE’s for the real index data and the respective surrogate data. Numbered arrows show particular market events, as referenced in text.

We now elaborate on some events on each of the indexes analysed. Regarding S&P 500, depicted in figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), we can highlight the following facts:

1. 1.

   The Hurst exponent, H1subscript𝐻1H\_{1} has a positive trend up to 1971, when it reverses to a long-term negative trend, moving from a persistent signal to a more random signal. This coincides with the end of the Bretton Wood system.
2. 2.

   Before the Black Monday of October 1987, the time series presents a uniscaling pattern followed by a moderate asymmetric pattern which is then followed by strong multiscaling. At the same time, the volatility is quite low, meaning that the increased complexity is not driven by a single event but by the market structure.
3. 3.

   Before the Dot.com bubble burst on the second quarter of 2000, we have for both Wq1,q2subscript𝑊
   subscript𝑞1subscript𝑞2W\_{q\_{1},q\_{2}} and B𝐵B a sequence of patterns, i.e. converging moderate multiscaling - uniscaling - diverging moderate multiscaling - strong multiscaling. This is accompanied by relatively low but increasing volatility. This is a signal that the market is going to saturate and a probable drop is expected. It can be attributed to the fact that the increasing multiscaling along with a rising volatility increases the market heterogeneity, which is becoming driven by turbulence in trading patterns.

![Refer to caption](/html/2010.08890/assets/FIGURES/NIKKEI_final_arrow.png)


Figure 7:  NIKKEI index price time-series and scaling TPs: (a),(b),(c),(d) and (e) exactly as described in caption of figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"). Numbered arrows show particular market events, as referenced in text.

In figure [7](#S3.F7 "Figure 7 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") we show another major index, the NIKKEI. Some particular features of this index are:

1. 1.

   An uniscaling behaviour at the beginning of 1986 which evolves to an asymmetric multiscaling behaviour of type A0 and A- and then evolves to a persistent multiscaling, even after the bubble has exploded in 1991.
2. 2.

   After the bubble exploded in 1991, the market follows an anomalous scaling. In fact, the market remains moderately multiscaling. This reflects the heterogeneity generated by the monetary policies adopted by the central bank of Japan.
3. 3.

   The series appears persistent from 1970 up to the bubble explosion, when a mix of neutral and anti-persistent behaviour are then more present. This behaviour persists up to 2007.

![Refer to caption](/html/2010.08890/assets/FIGURES/ASE_final_arrow.png)


Figure 8:  ASE index price time-series and scaling TPs: (a),(b),(c),(d) and (e) exactly as described in caption of figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"). Numbered arrows show particular market events, as referenced in text.

In figure [8](#S3.F8 "Figure 8 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") we report the analysis related to the Athens stock market. The plots show:

1. 1.

   Before the 2000 bubble, an asymmetric multiscaling period is identified, which is a signature of a turbulent period. This is retrieved both using the W and B metrics which remains quite high for the consequent period. This is a combination of the global turbulence in the 1997 and 1998 and the Dot.com bubble which was going to break.
2. 2.

   From 2005 to the third quarter of 2008 we have a succession of uniscaling and moderate multiscaling patterns which is then followed by a long period of moderate multiscaling pattern, suggesting that a the inception of the global financial crisis a complex dynamic with stronger heterogeneity is taking place.
3. 3.

   The B𝐵B proxy agrees almost perfectly with the multiscaling width. This is mainly because, apart from the Dot.com bubble, the turbulent time periods were generated by complex dynamics which increase the heterogeneity of the process in a symmetric way rather than by extreme tail events.

![Refer to caption](/html/2010.08890/assets/FIGURES/SENSEX_final_arrow.png)


Figure 9:  SENSEX index price time-series and scaling TPs: (a),(b),(c),(d) and (e) exactly as described in caption of figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"). Numbered arrows show particular market events, as referenced in text.

Finally, we report in Figure [9](#S3.F9 "Figure 9 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") the plots for the Bombay stock market (SENSEX). We observe the following:

1. 1.

   Between the third quarter of 2003 and first quarter of 2004 we see a short uniscaling behaviour followed by a strong multiscaling behaviour. This corresponds to the election of Sonia Gandhi’s communist coalition in May 2004 (arrow No 2) which generated a market drop of 15.52% and a consequent market heterogeneity in market conditions. In particular, it is possible to notice that the highest and lowest Hq(θ)′H\_{q}^{{}^{\prime}(\theta)} for the W0.01,4subscript𝑊
   0.014W\_{0.01,4} go in opposite directions, resulting in a A0 type of pattern.
2. 2.

   H1(θ)′H\_{1}^{{}^{\prime}(\theta)} is always higher than 0, which implies a persistent behaviour while H4(θ)′H\_{4}^{{}^{\prime}(\theta)} is, apart few local exceptions, always negative, implying an antipersistent behaviour.
3. 3.

   For this index, the B𝐵B and the W𝑊W multiscaling proxies disagree in most of the cases. In fact, it is possible notice that in time periods of high width as 2001-2003 and 2011-2012, we have a relatively low B𝐵B, which, together with the high volatility of the series, makes clear that the high width is due more to tail events than temporal correlations.

It is important to notice that major indices are affected by global events which also spill-over to the peripheral ones, while the opposite is not always true. In fact, it is possible to notice that ’Black Monday’, the Japanese bubble and the Dot.com bubble generated a scaling change also in markets different from the ones in which they originated. In contrast, the main shifting events in peripheral indices, do not affect main ones. Given the results depicted in  [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") - [9](#S3.F9 "Figure 9 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), we conclude that a transition from a uniscaling to a multiscaling pattern (usually through an asymmetric pattern of type A- (strongly multiscaling and asymmetric) or AL (more weakly multiscaling and asymmetric) in combination with a relatively low (but rising) volatility is a warning signal that the market is becoming saturated and a turbulent period can follow with a possible crash.

### 3.5 Robustness of TP’s as warning signals

Having noted all the above, the indication that temporal evolution of multiscaling strength, in both its symmetric and asymmetric forms, as described by the TP’s that were defined above and identified by the algorithmic procedure presented in this work, provides possible signals for future market behavior should be further investigated. In order to take the next step, we must first distinguish between the effect on multiscaling coming from the biasing of wGHE values caused by tail events which is observed immediately after these events, and the effect on multiscaling coming from either tail events or temporal correlations in price changes that occur prior to a market crisis, such as a stock market bubble under development, or before a market crash. The first is an ’after-effect’ of single and extreme market events, the second is a signal preceding an actual critical event. In an attempt to address the issue, we deleted one or more single trading days from the index time-series that correspond to specific events and recalculated the Hq′subscriptsuperscript𝐻′𝑞H^{\prime}\_{q} profiles of the modified index. More specifically, we deleted some key trading days in S&P 500, NIKKEI, ASE and SENSEX that are directly related to one or more of these critical events: (i) ’Black Monday’, (ii) the 1997 ’Asian’ crisis, (iii) the 1998 ’Russian’ crisis (iv) the I. Ghandi election in India in 2004. The exact trading dates that were erased for each index are shown in Table [3](#S3.T3 "Table 3 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") together with the corresponding % close price changes. Cells containing a dash denote that these dates were not deleted for the particular index. Notice that for each event, we deleted possibly different days and different number of days per index. This is because each market reacted differently to the particular crisis. In particular we wanted to capture and remove the ’instantaneous’ effect of a single market event on the GHE computations and the resulting multiscaling, not its possible short or long-term after-effects on the actual market dynamics. Therefore, we deleted just 1 up to 4 trading days that were directly associated with the single market event, usually a large drop followed by a big rise or other smaller rises/drops.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Deleted dates | Market event | S&P 500 | NIKKEI | ASE | SENSEX |
| 19-Oct-1987 | B. M. | -20.47% | - | - | - |
| 20-Oct-1987 | B. M. | +5.33% | -14.90% | - | - |
| 21-Oct-1987 | B. M. | +9.10% | +9.30% | - | - |
| 22-Oct-1987 | B. M. | -3.92% | - | - | - |
| 23-Oct-1987 | B. M. | - | -4.93% | - | - |
| 26-Oct-1987 | B. M. | - | -4.30% | - | - |
| 27-Oct-1997 | A. C. | -6.87% | - | - | - |
| 28-Oct-1997 | A. C. | - |  | - | - |
| 31-Oct-1997 | A. C. | - | - | -4.02% | - |
| 04-Nov-1997 | A. C. | - | - | +4.72% | - |
| 06-Nov-1997 | A. C. | - | - | -4.23% | - |
| 28-Aug-1998 | R. C. | - | -3.46% | - | - |
| 31-Aug-1998 | R. C. | -6.80% | - | - | - |
| 01-Sep-1998 | R. C. | - | - | -3.81% | - |
| 02-Sep-1998 | R. C. | - | - | +5.15% | - |
| 14-May-2004 | G. E. | - | - | - | -0.0610 % |
| 17-May-2004 | G. E. | - | - | - | -11.14% |
| 18-May-2004 | G. E. | - | - | - | +8.25% |

Table 3: Deleted dates for modified indices, the corresponding market event and the % close price change of that date per index. Cells with a ’-’ correspond to dates that were not deleted for the particular index in the respective column. ’B.M.’ stands for ’Black Monday’, ’A.C.’ for ’Asian Crisis’, ’R.C.’ for ’Russian Crisis’ and ’G.E.’ for Gandhi 2004 Election’.

In figures [10](#S3.F10 "Figure 10 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") - [13](#S3.F13 "Figure 13 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool") a comparison between the wGHE time series, γ𝛾\gamma time-series and identified TP’s of the real indices and the respective modified indices are shown, focusing on the time periods around the market events mentioned in Table [3](#S3.T3 "Table 3 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"). For S&P 500 and NIKKEI we observe that after B.M., the strong ’post-event’ A- TP that exists in the real index data after Oct. 1987 (figures [10](#S3.F10 "Figure 10 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), [11](#S3.F11 "Figure 11 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")b) and is directly related to the strong biasing induced to the tails of the price change distribution exclusively due to the four deleted days, is almost eliminated in the modified index W0.1,4′subscriptsuperscript𝑊′

0.14W^{\prime}\_{0.1,4} TP’s (figures [10](#S3.F10 "Figure 10 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), [11](#S3.F11 "Figure 11 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")c). However, the pre-event ’warning’ A0 TP and AL TP signals corresponding to a transition from a uniscaling to multiscaling starting in 1986, well before the B.M. event are still present. Notice also, that an AL pattern well after the ’black Monday’ event is still seen in the modified index TP’s for NIKKEI, well before 1991. This suggests that the ’warning’ A𝐴A-type TP’s observed well after Oct. 1987, are not an artefact of the B.M. event, but a consequence of market trading patterns before the NIKKEI 1991 bubble break-down. Similarly, the A- type TP before the year 2000 dot.com bubble is destroyed after in S&P 500 after the deletion of the A.C. and R.C. related extreme tail events but there is a clear uniscaling to multiscaling transition via an AL TP well before the bubble break-down. The same AL TP is seen in NIKKEI, before 2000. Again, this suggests that the A𝐴A-type warning signal in the period 1997-1998 is not exclusively an ’after-effect’ product of the 1997 ’Asian crisis’ and 1998 ’Russian crisis’ events, but a product of trading dynamics of an extended period jut before the year 2000 bubble break-down.

![Refer to caption](/html/2010.08890/assets/FIGURES/SP500_final_zoom.png)


Figure 10:  SP500 index price time-series and scaling TPs in period 1985-2001: Comparison between TPs obtained from SP500 close prices (real index TP’s) and TPs obtained after removing the ’black Monday’, ’1997 Asian crisis and ’1998 Russian crisis’ critical trading days (modified index TP’s): (a) SP500 close prices, (b) real index W14subscript𝑊14W\_{14} TP’s, (c) modified index W14subscript𝑊14W\_{14} TP’s, (d) real index B𝐵B-proxy TP’s and (e) modified index B𝐵B-proxy TP’s. The ’warning’ A𝐴A-type TP’s before 19th of October 1987 are maintained in the modified index results.

![Refer to caption](/html/2010.08890/assets/FIGURES/NIKKEI_final_zoom.png)


Figure 11:  NIKKEI index price time-series and scaling TPs in period 1985-2001: Comparison between TPs obtained from NIKKEI close prices (real index TP’s) and TPs obtained after removing the ’black Monday’, ’1997 Asian crisis and ’1998 Russian crisis’ critical trading days (modified index TP’s): (a) Index close prices (b) real index TP’s for W14subscript𝑊14W\_{14} (c) W14subscript𝑊14W\_{14} modified index TP’s, (d) B𝐵B-proxy real index TP’s and (e) B𝐵B-proxy modified index TP’s.

![Refer to caption](/html/2010.08890/assets/FIGURES/ASE_final_zoom.png)


Figure 12:  ASE index price time-series and scaling TPs in period 1995-2001: As in figure [11](#S3.F11 "Figure 11 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"), comparison between real index TP’s and modified index TP’s of ASE log close price Hqsubscript𝐻𝑞H\_{q}’s. The later are obtained after removing 1997 ’Asian crisis’ and 1998 ’Russian crisis’ critical trading days. (a), (b), (c), (d), (e) as in figure [11](#S3.F11 "Figure 11 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool").

![Refer to caption](/html/2010.08890/assets/FIGURES/SENSEX_final_zoom.png)


Figure 13:  SENSEX index price time-series and scaling TPs in period 1985-2001: Comparison between TPs obtained from SENSEX close prices (real index TP’s) and TPs obtained after removing the 2006 ’Ghandi election’ crisis (modified index TP’s): (a) S&P 500 close prices (b) real index TP’s for W14subscript𝑊14W\_{14} (c) W14subscript𝑊14W\_{14} modified index TP’s, (d) B𝐵B-proxy real index TP’s and (e) B𝐵B-proxy modified index TP’s.

The same conclusion can be drawn by looking at the ’warning’ A- and A0 types of TPs before the year 2000 ASE bubble in figure [12](#S3.F12 "Figure 12 ‣ 3.5 Robustness of TP’s as warning signals ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool"). These patterns are maintained, almost intact, in the modified index TPs, after removing A.C. and the R.C. related trading days from ASE. Again, this means that A𝐴A-type patterns seen in the real index TPs are not just a product of ’after-effects’ of one or two isolated big market events, but a product of an extended period of market trading patterns, well before a bubble bursts. This fact is particularly pronounced for the ASE 2000 bubble which was well under development in the period where the Asian and Russian crises occurred, since the the A- ’warning’ TP’s were barely affected by the removal of the few trading days related to these crises. However, the removal of the respective trading days before the break of the S&P 500 ’dot.com’ bubble has had a different effect. We observe that the existing A- TP has almost disappeared and the dynamics approximately two years before the break of the bubble is uniscaling. However, even here, the dynamics undergoes a clear uniscaling to multiscaling transition almost a year before the bubble burst through and asymmetric AL TP.

## 4 Discussion

By examining the GHE results for all these indices, we confirm that there are common elements among many of them especially in critical time periods, like a stock-market bubble or financial crisis. However, each index also has unique features indicating that the corresponding markets have different underling dynamics which can be related to global events for major stock indices and to local phenomena. In particular, we notice that critical events are usually driven by a uniscaling behaviour which is then followed by a usually sharp transition to multiscaling via ’asymmetric’ multiscaling patterns.

In some time periods one clearly sees that the w𝑤wGHE’s for higher values of q𝑞q show a sharp drop towards strongly anti-persistent behavior, whereas the respective small q𝑞q w𝑤wGHE’s are almost constant or rising, depicting neutral or persistent behavior. This behavior can be caused by two types of market changes: either (i) due to a critical single market event such as a market crash (e.g. Black Monday on Oct. 19, 1987 when S&P 500 lost 20.4% in one day), or (ii) a more extended critical period where the market behaves in a bullish way for small day-to-day price changes but shows anti-persistent behavior for large price changes (fig. [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool")). In case (i), the large change is a single extreme tail point in the price change distributions taken within the particular time-window where the GHE’s are calculated, a tail point that mostly affects the large q𝑞q GHE’s causing a sharp drop. The volatility also shows a sharp rise at that date, followed by a gradual decay. The time duration of the effect of this single market event on the GHE time-series, as well as volatility, is in the order of Δ​tΔ𝑡\Delta t, the time window length used for calculating the price change distribution moments, and θ𝜃\theta and leads to a pronounced A- pattern extended in time, although the actual scaling within this time window may be different. Subtracting this single event, would largely destroy the pattern, as it was seen, for instance, for the B.M. event in S&P 500 and NIKKEI. In case (ii), we have shown that these patterns are a consequence of the increase of tail events that occur in a turbulent market period and the way they are correlated. For example, during a critical period (of a developing bubble, for example) there is increased frequency of large market drop tail events that are immediately followed (usually in the next trading day) by an equivalent rise. This combination of events occurring amidst a rising market trend, causes a sharp drop in the high-q𝑞q wGHE’s while the small q𝑞q wGHE’s are not so much affected. This type of market behavior that leads to market transition from a more ’regular’ and efficient market (uniscaling behavior) to a more ’nervous’ market has a plausible justification: when the majority of traders are afraid of or get the ’gut feeling’ that the market becomes saturated and a crash is imminent, they are more likely to revert to rapid sales (in order to secure profits) that drive the market down by large amount during a single day. As the market is still in a rising trend, this sales spree is likely to be reversed and followed by a buying spree the next day in anticipation for a continued market rise. This sort of ’nervous’ behavior was particularly notable with the ASE 2000 bubble, where the very pronounced asymmetric multiscaling patterns in the period 1997-1998 were not at all a result of just the Asian or Russian crises that took place within that period. In fact, one may argue, that even the large drops (followed by large rises) that are due to some justified market event (such as the A.C. and R.C. crises) are just a ’pretext’ for a saturated market during a bubble development to correct itself. It is also a notable fact that the S&P 500 changed from a rather long uniscaling (or very weakly multiscaling) period during the seventies to mid-eighties to a multiscaling period (transition is via an AL TP), starting in 1986 more than a year before Black Monday, a clear stock-market historical event that remains completely unexplained by the economic surroundings of the preceding period. In a large survey carried out by Shiller [[48](#bib.bib48)] over a sample of more than 800 investors, when interviewed, the most frequent answer they gave to the question why they behaved the way they did during that day, was that they had a ’gut-feeling’ that there was an impeding crash. This ’gut-feeling’ was captured by wGHE’s measuring the market scaling transition that occurred long before the event, as these traders developed particular trading habits which, over a rather long period before the crash, lead to a sequence of tail events that would spark an AL TP and multiscaling behavior seen in 1986-1987.

In conclusion, case (i) ’A’ patterns caused by large single events can be distinguished from extended time (case (ii)) ’A’ patterns, by the fact that the first follow a crash or a bubble-break, whereas the second are preceding a possible crash or bubble-break. In this sense, ’A’ patterns, especially when they follow a period of uniscaling behavior, can be used as warning signals for critical market time periods.

We also noticed some differences between major and peripheral markets. In particular, in major stock indices, more abrupt transitions between patterns are observed during critical time periods, while for peripheral markets they are much smoother. This is probably due to the number of market participants and the amount of information available to them. In fact, in a global market the market shift due to ’bad news’ can completely alter market dynamics in a relatively small amount of time. A second difference lies in the fact that for major indices, multiscaling is not associated directly to period of a of recession or crisis while it is mostly the case for peripheral markets. This is probably due to the fact that in peripheral markets there isn’t enough liquidity to absorb the huge heterogeneity generated by the market participants.

## 5 Conclusions

In this paper, we have presented for the first time how different temporal patterns can emerge from the dynamics of the time-dependent generalized Hurst exponents (GHE). In particular, we proposed several patterns which differentiate uniscaling from multiscaling and further differentiate two forms of multiscaling, i.e. symmetric and asymmetric multiscaling in the temporal evolution of GHE timeseries. These temporal patterns combined with the analysis of the multiscaling width W𝑊W and the multiscaling depth B𝐵B (and their dynamics) offer an important set of tools to signal critical events in financial time series and not only. We also introduced a completely algorithmic and general procedure to identify such patterns in any time-series of GHE’s, which allows one to determine these patterns in a statistically significant manner. Regarding the calculation of the GHE time-series, we also addressed the important issue of choosing a proper sliding time window length Δ​tΔ𝑡\Delta t and provided an empirical rule that is based on minimising the noise due to finite-size effects in the GHE calculations and at the same time capturing the actual local dynamical changes of the scaling over short time scales.

Results showed very interesting patterns among major and peripheral markets. We found similar patterns among the market considered but also differences related to local behaviors. One of the common features is the existence of a (usually sharp) transition from an
uniscaling to multiscaling pattern in the rising period, before a stock market bubble breaks, such as the 2000 bubble in S&P 500 and ASE or the 1991 bubble for NIKKEI. ASE, being a small and peripheral market with low liquidity, had a much more pronounced and robust ’asymmetric’ multiscaling warning pattern before its large 2000 bubble, than major indices like S&P 500 and NIKKEI. This feature is also present in stock market crises that are externally caused, such as the 2008 real-estate market crisis, but in a significantly weaker form. For example, for ASE, whereas the 2000 and 1990 crashes showed very pronounced and clear A- patterns, the 2008 crash showed a weaker AL pattern. Another feature is that there exists some kind of notable scaling transition shortly before or after the break-down of a bubble, usually a change from a strong asymmetric multiscaling to either an uniscaling or moderate multiscaling TP. It should be stressed that the transition to an asymmetric multiscaling TP is manifested by past data sufficiently prior to the bubble breakdown so that this feature could be used as a ’warning’ signal of a bubble in development, in particular, if the strong multiscaling is accompanied to relatively low (and maybe rising) volatility. In general, transitions always occur at some critical date when there is either the beginning of a new period of development or the end of some type of crisis. However, if we are talking about a global crisis, various stock markets are affected in significantly different ways. The differences are pronounced if major indices, that highly correlate to global events are compared to peripheral or developing markets which are mostly affected by local events. Indeed, major market crashes also affect the scaling behaviour of peripheral markets, while the reverse is not true. For several indices there are extended time periods of uniscaling behavior and time periods of clear multiscaling behavior, while some indices are, on the overall, more multiscaling than others. The rich variety of information that can be conveyed by the newly introduced scaling patterns can be used as a valuable tool to obtain the ’fingerprint’ of a possible turbulent market period and also issue warning signals for impeding market crashes or other critical events.

Finally, as the defined scaling temporal patterns are clearly related to the details of the underlying complex dynamics of the physical system in a physically justifiable way, they offer (together with the algorithmic identification procedure presented in this work) a tool to characterise the dynamical evolution of scaling of any complex system. Of particular interest would be to apply the temporal pattern analysis presented in this work to low-dimensional complex systems that contain, apart from fat-tailed change difference distributions, enhanced temporal correlations. These systems would be optimal test-beds for testing the ’predicting power’ of GHE’s for the future evolution of the system, especially for critical events. Future work will be devoted to disentangling the effect of fat tails and correlation to the various forms of multiscaling in a robust statistical manner. A second extension to this work will be in the direction of the quantification of the asymmetries (based on empirically defined metrics that would depend on the GHE temporal profiles) in order to algorithmically detect strong asymmetries in scaling which can be used by market participants for trading strategies, e.g. issue a sell order when the asymmetry is higher than the long term asymmetry during specific market conditions such as a bullish market. The construction of a total ’market risk’ indicator that could depend on these GHE metrics is another very interesting possibility for future work. Such an indicator would be a very useful tool in the hands of investors and policy makers in order to detect and quantifiably assess financial risk.

## References

* Di Matteo [2007]

  T. Di Matteo,
  Multi-scaling in finance,
  Quantitative Finance 7
  (2007) 21–36.
  doi:[10.1080/14697680600969727](http://dx.doi.org/10.1080/14697680600969727).
* Matteo et al. [2005]

  T. D. Matteo, T. Aste,
  M. Dacorogna,
  Long-term memories of developed and emerging markets:
  Using the scaling analysis to characterize their stage of development,
  Journal of Banking & Finance 29
  (2005) 827–851.
* Matteo et al. [2003]

  T. D. Matteo, T. Aste,
  M. Dacorogna,
  Scaling behaviors in differently developed markets,
  Physica A: Statistical Mechanics and its
  Applications 324 (2003)
  183––188.
* Mandelbrot [1963]

  B. Mandelbrot,
  The variation of certain speculative prices.,
  The journal of business 36
  (1963) 394–419.
* Calvet and Fisher [2002]

  L. Calvet, A. Fisher,
  Multifractality in asset returns: theory and
  evidence,
  Review of Economics and Statistics
  84 (2002) 381–406.
* Bouchaud et al. [2000]

  J. Bouchaud, M. Potters,
  M. Meyer,
  Apparent multifractality in financial time series.,
  The European Physical Journal B-Condensed Matter
  and Complex Systems 13 (2000)
  595–599.
* Mantegna and Stanley [1995]

  R. Mantegna, H. Stanley,
  Scaling behaviour in the dynamics of an economic
  index.,
  Nature 376
  (1995) 46–49.
* LeBaron [2001]

  B. LeBaron,
  Stochastic volatility as a simple generator of
  apparent financial power laws and long memory.,
  Quantitative Finance 1
  (2001) 621–631.
* Kaizoji [2003]

  T. Kaizoji,
  Scaling behavior in land markets,
  Physica A 326
  (2003) 256–264.
* Scalas [1998]

  E. Scalas,
  Scaling in the market of futures.,
  Physica A 253
  (1998) 394–402.
* Bartolozzi et al. [2007]

  M. Bartolozzi, C. Mellen,
  T. D. Matteo, T. Aste,
  Multi-scale correlations in different futures
  markets,
  European Physical Journal B 58
  (2007) 207–220.
* Liu et al. [2007]

  R. Liu, T. Lux, T. D.
  Matteo,
  True and apparent scaling: The proximities of the
  markov-switching multifractal model to long-range dependence,
  Physica A 383
  (2007) 35–42.
* Liu et al. [2008]

  R. Liu, T. D. Matteo,
  T. Lux,
  Multifractality and long-range dependence of asset
  returns: The scaling behaviour of the markov-switching multifractal model
  with lognormal volatility components,
  Advances in Complex Systems 11
  (2008) 669–684.
* Mandelbrot [1997]

  B. Mandelbrot, Fractals and scaling in
  finance: discontinuity, concentration, risk., Springer
  Verlag, 1997.
* Miloş et al. [2020]

  L. Miloş, B. Haţiegan,
  C. Botoc,
  Multifractal detrended fluctuation analysis (mf-dfa)
  of stock market indexes. empirical evidence from seven central and eastern
  european markets,
  Sustainability 12
  (2020) 535.
  doi:[10.3390/su12020535](http://dx.doi.org/10.3390/su12020535).
* Barunik and Kristoufek [2010]

  J. Barunik, L. Kristoufek,
  On hurst exponent estimation under heavy-tailed
  distributions,
  Physica A: Statistical Mechanics and its
  Applications 389 (2010)
  3844–3855.
* Kristoufek [2011]

  L. Kristoufek,
  Multifractal height cross-correlation analysis: A new
  method for analyzing long-range cross-correlations,
  EPL (Europhysics Letters) 95
  (2011) 68001.
* Jiang et al. [2019]

  Z.-Q. Jiang, W.-J. Xie,
  W.-X. Zhou, D. Sornette,
  Multifractal analysis of financial markets: a
  review,
  Reports on Progress in Physics
  82 (2019) 125901.
* Barunik et al. [2012]

  J. Barunik, T. Aste,
  T. Di Matteo, R. Liu,
  Understanding the source of multifractality in
  financial markets,
  Physica A: Statistical Mechanics and its
  Applications 391 (2012)
  4234–4251.
* Mantegna and Stanley [1999]

  R. N. Mantegna, H. E. Stanley,
  Introduction to Econophysics: Correlations and Complexity in
  Finance, Cambridge University Press,
  1999. URL: <https://books.google.co.uk/books?id=SzgXWCS7Nr8C>.
* Dacorogna et al. [2001]

  M. M. Dacorogna, R. Gençay,
  U. A. Müller, R. B. Olsen,
  O. V. Pictet, An Introduction to
  High-Frequency Finance, Academic Press,
  San Diego, 2001. URL: <http://www.sciencedirect.com/science/article/pii/B9780122796715500058>.
* Lux [2004]

  T. Lux,
  Detecting multi-fractal properties in asset returns:
  The failure of the scaling estimator,
  International Journal of Modern Physics C
  15 (2004) 481–491.
  URL: <http://www.worldscientific.com/doi/abs/10.1142/S0129183104005887>.
  doi:[10.1142/S0129183104005887](http://dx.doi.org/10.1142/S0129183104005887).
  [arXiv:http://www.worldscientific.com/doi/pdf/10.1142/S0129183104005887](http://arxiv.org/abs/http://www.worldscientific.com/doi/pdf/10.1142/S0129183104005887).
* Lux and Marchesi [1999]

  T. Lux, M. Marchesi,
  Scaling and criticality in a stochastic multi-agent
  model of a financial market,
  Nature 397
  (1999) 498.
* Buonocore et al. [2020]

  R. Buonocore, G. Brandi,
  R. Mantegna, T. Di Matteo,
  On the interplay between multiscaling and stock
  dependence,
  Quantitative Finance 20
  (2020) 133–145.
* Gatheral et al. [2018]

  J. Gatheral, T. Jaisson,
  M. Rosenbaum,
  Volatility is rough,
  Quantitative Finance 18
  (2018) 933–949.
* Takaishi [2019]

  T. Takaishi,
  Rough volatility of bitcoin,
  Finance Research Letters (2019)
  101379.
* Fukasawa et al. [2019]

  M. Fukasawa, T. Takabatake,
  R. Westphal,
  Is volatility rough?,
  arXiv preprint arXiv:1905.04852
  (2019).
* Livieri et al. [2018]

  G. Livieri, S. Mouti,
  A. Pallavicini, M. Rosenbaum,
  Rough volatility: evidence from option prices,
  IISE transactions 50
  (2018) 767–776.
* Brandi and Di Matteo [2020]

  G. Brandi, T. Di Matteo,
  On the statistics of scaling exponents and the
  multiscaling value at risk,
  Submitted to the European Journal of Finance
  (2020).
* Morales et al. [2011]

  R. Morales, T. Di Matteo,
  R. Gramatica, T. Aste,
  Dynamical hurst exponent as a tool to monitor
  unstable periods in financial time series,
  Physica A: Statistical Mechanics and its
  Applications 391 (2011).
  doi:[10.1016/j.physa.2012.01.004](http://dx.doi.org/10.1016/j.physa.2012.01.004).
* Drożdż et al. [2018]

  S. Drożdż, R. Kowalski,
  P. Oswiecimka, R. Rak,
  R. Gebarowski,
  Dynamical variety of shapes in financial
  multifractality,
  Complexity 2018
  (2018) 7015721. URL: <https://doi.org/10.1155/2018/7015721>.
  doi:[10.1155/2018/7015721](http://dx.doi.org/10.1155/2018/7015721).
* Drożdż and Oświecimka [2015]

  S. Drożdż, P. Oświecimka,
  Detecting and interpreting distortions in
  hierarchical organization of complex time series,
  Physical Review E 91
  (2015). URL: <http://dx.doi.org/10.1103/PhysRevE.91.030902>.
  doi:[10.1103/physreve.91.030902](http://dx.doi.org/10.1103/physreve.91.030902).
* Yalamova and Mckelvey [2011]

  R. Yalamova, B. Mckelvey,
  Using power laws and the Hurst exponent to identify stock
  market trading bubbles, 1st ed.,
  Taylor & Francis Group, 2011, pp.
  85–105. doi:[10.1201/9781315585444](http://dx.doi.org/10.1201/9781315585444).
* Fernandez-Martineza et al. [2017]

  M. Fernandez-Martineza,
  M. Sanchez-Granerob, M. J.
  Munoz Torrecillas, B. McKelvey,
  A comparison among three hurst exponent approaches to
  predict nascent bubbles in s&p500 company stocks,
  Fractals: Complex Geometry, Patterns, and Scaling
  in Nature and Society 25 (2017).
  doi:[10.1142/S0218348X17500062](http://dx.doi.org/10.1142/S0218348X17500062).
* Kroha. and Škoula. [2018]

  P. Kroha., M. Škoula.,
  Hurst exponent and trading signals derived from
  market time series,
  in: Proceedings of the 20th International
  Conference on Enterprise Information Systems - Volume 1: ICEIS,,
  INSTICC, SciTePress,
  2018, pp. 371–378.
  doi:[10.5220/0006667003710378](http://dx.doi.org/10.5220/0006667003710378).
* Caporale et al. [2017]

  G. M. Caporale, L. A. Gil-Ala,
  A. Plastun, Long memory and data frequency
  in financial markets, DIW Discussion Papers
  1647, Berlin, 2017.
  URL: <http://hdl.handle.net/10419/156139>.
* Grech and Mazur [2004]

  D. Grech, Z. Mazur,
  Can one make any crash prediction in finance using
  the local hurst exponent idea?,
  Physica A: Statistical Mechanics and its
  Applications 336 (2004)
  133–145. URL: <http://dx.doi.org/10.1016/j.physa.2004.01.018>.
  doi:[10.1016/j.physa.2004.01.018](http://dx.doi.org/10.1016/j.physa.2004.01.018).
* Grech and Pamuła [2008]

  D. Grech, G. Pamuła,
  The local hurst exponent of the financial time series
  in the vicinity of crashes on the polish stock exchange market,
  Physica A: Statistical Mechanics and its
  Applications 387 (2008)
  4299 – 4308. URL: <http://www.sciencedirect.com/science/article/pii/S0378437108001660>.
  doi:[https://doi.org/10.1016/j.physa.2008.02.007](http://dx.doi.org/https://doi.org/10.1016/j.physa.2008.02.007).
* Mitra [2012]

  S. Mitra,
  Is hurst exponent value useful in forecasting
  financial time series?,
  Asian Social Science 8
  (2012). doi:[10.5539/ass.v8n8p111](http://dx.doi.org/10.5539/ass.v8n8p111).
* Hurst [1951]

  H. Hurst,
  Long-term storage capacity of reservoirs,
  Transactions of the American Society of Civil
  Engineers 116 (1951) 770.
* Kantelhardt et al. [2002]

  J. Kantelhardt, S. Zschiegner,
  E. Koscielny-Bunde, A. Bunde,
  S. Havlin, H. Stanley,
  Multifractal detrended fluctuation analysis of
  nonstationary time series,
  Physica A: Statistical Mechanics and its
  Applications 316 (2002).
  doi:[10.1016/S0378-4371(02)01383-3](http://dx.doi.org/10.1016/S0378-4371(02)01383-3).
* Muzy et al. [1991]

  J.-F. Muzy, E. Bacry,
  A. Arneodo,
  Wavelets and multifractal formalism for singular
  signals: Application to turbulence data,
  Physical review letters 67
  (1991) 3515.
* Muzy et al. [1993]

  J.-F. Muzy, E. Bacry,
  A. Arneodo,
  Multifractal formalism for fractal signals: The
  structure-function approach versus the wavelet-transform modulus-maxima
  method,
  Physical review E 47
  (1993) 875.
* Serinaldi [2010]

  F. Serinaldi,
  Use and misuse of some hurst parameter estimators
  applied to stationary and non-stationary financial time series,
  Physica A: Statistical Mechanics and its
  Applications 389 (2010)
  2770–2781. doi:[10.1016/j.physa.2010.02.044](http://dx.doi.org/10.1016/j.physa.2010.02.044).
* Hurst et al. [1965]

  H. Hurst, R. Black,
  Y. Simaika, Long-term storage: an
  experimental study, Constable, 1965.
* Buonocore et al. [2016]

  R. J. Buonocore, T. Aste,
  T. Di Matteo,
  Measuring multiscaling in financial time-series,
  Chaos, Solitons & Fractals 88
  (2016) 38–47.
* Killick et al. [2012]

  R. Killick, P. Fearnhead,
  I. A. Eckley,
  Optimal detection of changepoints with a linear
  computational cost,
  Journal of the American Statistical Association
  107 (2012) 1590–1598.
* Shiller [1988]

  R. J. Shiller,
  Portfolio insurance and other investor fashions as
  factors in the 1987 stock market crash,
  NBER Macroeconomics Annual 389
  (1988) 287–297.
  doi:[10.1086/654091](http://dx.doi.org/10.1086/654091).

## 6 Appendix

![Refer to caption](/html/2010.08890/assets/FIGURES/SP500_final_zoom_33_50.png)


Figure 14:  S&P 500 blow-up of period 1933-1950: (a),(b),(c),(d) and (e) exactly as described in caption of figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool").

![Refer to caption](/html/2010.08890/assets/FIGURES/SP500_final_zoom_50_63.png)


Figure 15:  S&P 500 blow-up of period 1950-1963: (a),(b),(c),(d) and (e) exactly as described in caption of figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool").

![Refer to caption](/html/2010.08890/assets/FIGURES/NIKKEI_final_zoom70_80.png)


Figure 16:  NIKKEI blow-up of period 1970-1980: (a),(b),(c),(d) and (e) exactly as described in caption of figure [6](#S3.F6 "Figure 6 ‣ 3.4 TP identification algorithmic procedure ‣ 3 Results ‣ The use of scaling properties to detect relevant changes in financial time series: a new visual warning tool").

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2010.08890)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2010.08890)
[View original  
on arXiv](https://arxiv.org/abs/2010.08890)[►](javascript: void(0))