---
authors:
- Junwei Yang
doc_id: arxiv:2512.08000v1
family_id: arxiv:2512.08000
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Analysis of Contagion in China’s Stock Market: A Hawkes Process Perspective'
url_abs: http://arxiv.org/abs/2512.08000v1
url_html: https://arxiv.org/html/2512.08000v1
venue: arXiv q-fin
version: 1
year: 2025
---


Junwei Yang111Junwei Yang is at school of statistics and data science, Shanghai University of Finance and Economics(SUFE). I would like to thank my supervisor Professor Hongbiao Zhao and members of my dissertation committee, Professor Ning Chang, Professor Jianhua Hu, Professor Xin He for their helpful comments and advice. I also thank Professor Haibo Shi and Professor Yuan Zhang, for their kind guidance and useful discussion. Any errors or omissions are the sole responsibility of the author.

(This version: May 18, 2023 )

###### Abstract

This study explores contagion in the Chinese stock market using Hawkes processes to analyze autocorrelation and cross-correlation in multivariate time series data. We examine whether market indices exhibit trending behavior and whether sector indices influence one another. By fitting self-exciting and inhibitory Hawkes processes to daily returns of indices like the Shanghai Composite, Shenzhen Component, and ChiNext, as well as sector indices (CSI Consumer, Healthcare, and Financial), we identify long-term dependencies and trending patterns, including upward, downward, and oversold rebound trends. Results show that during high trading activity, sector indices tend to sustain their trends, while low activity periods exhibit strong sector rotation. This research models stock price movements using spatiotemporal Hawkes processes, leveraging conditional intensity functions to explain sector rotation, advancing the understanding of financial contagion.

Keywords: Hawkes Process, Financial Contagion, Sector Rotation

## Introduction

### Research Background

The 2008 subprime crisis triggered a ”tsunami” in the U.S. financial markets, leading to a domino effect. Financial contagion focuses on discussing the interactions between different entities under the special structure of financial markets. Contagion manifests in different patterns, including temporal dependencies, such as seasonal river water levels, earthquakes and their aftershocks, and spatial dependencies, such as social network relationships and supply chain relationships. In the stock market, the phenomenon of ”sector rotation” describes the alternating rise and fall of different industry stock prices, showing temporal differences and spatial rotation characteristics similar to the temporal and spatial contagion mentioned above. A class of stochastic processes called Hawkes processes provides tools for characterizing the contagion of risk events and has been widely applied in fields such as earthquake prediction. Introducing Hawkes processes into financial markets to describe the interactions of risk, returns, volatility, and other elements between financial markets, institutions, and assets provides a new perspective for explaining financial market. This paper uses multivariate Hawkes processes to examine contagion in China’s secondary stock market and to analyze stock market sector rotation phenomena.

### Literature Review

This section introduces asset price predictability, temporal and spatial dependency research, and related research findings of Hawkes models in finance.

#### 1.2.1 Asset Price Predictability

Whether stock prices have the nature of temporal correlation is a controversial issue. The introduction of Dow Theory in the late 19th century initiated a wave of trend analysis as technical analysis for stock investment. Corresponding to trend analysis is the random walk theory of stock prices, with bachelier1900theorie studying the randomness of stock price changes from the perspective of Brownian motion. In 1965, economist fama1965behavior found empirical evidence supporting the hypothesis of independent stock price increments, followed by Roberts1967 proposing three forms of efficient markets. Based on this, fama1970efficient summarized the Efficient Market Hypothesis, stating that stock prices in an efficient market reflect all available information about assets, becoming a fundamental assumption for portfolio theory, CAPM model, option pricing, and other models.

Nevertheless, the random walk model cannot explain extraordinary stock price volatility, such as the 1987 U.S. stock market crash; much evidence suggests long-term correlation in stock prices (see mandelbrot1971can; greene1977long). Furthermore, jegadeesh1993returns discovered momentum effects in stock prices, and the variance ratio test proposed by lo1989size rejected the random walk hypothesis for stock prices. New theories continue to emerge, with peters1994fractal proposing the Fractal Market Hypothesis based on the research of Hurst, Mandelbrot, and others, introducing chaos theory to financial markets and allowing for long-term memory. Meanwhile, delong1990noise, lakonishok1992impact, and others proposed theories such as herd behavior and noise traders from a behavioral finance perspective to refute the rational person assumption in the Efficient Market Hypothesis, explaining large asset price fluctuations and trend effects. Some studies indicate that China’s stock market has not yet achieved weak-form efficiency (see jia2003empirical; chen2003weak; xiao2004empirical). Based on the perspective that asset prices exhibit trends, this paper will study financial contagion from the correlation in the time series of the same type of events and the influence between different types of events.

#### 1.2.2 Characterization of Time Series, Spatial Structure, and Their Dependencies

For time series data, many methods have been developed to handle different types of data including stationary, non-stationary, seasonal trends, and conditional heteroscedasticity, such as ARMA, ARIMA, Holt’s method, GARCH, and Hidden Markov models. The Vector Autoregression (VAR) framework proposed by sims1980macroeconomics extends autoregressive models to capture interactions between multiple time series. On the other hand, graph models and network models provide methods for capturing spatial structures and are widely applied in transportation communications, social networks, epidemiology, and other research (newman2018networks).

After 2010, the rise of deep learning brought a data-driven perspective to capture relationships between data. Recurrent neural networks, represented by Long Short-term Memory (LSTM), are widely used in time series modeling. In terms of spatial structure, Graph Neural Networks (GNN) are powerful tools that integrate graph models with neural networks, with numerous applications in characterizing node relationships and network information transmission. Subsequently developed spatiotemporal graph models, which combine language models for processing sequential data with graph models for processing spatial structures, are considered capable of capturing both time series and spatial structure information and can be used for multivariate time series analysis (wu2020connecting; cao2020spectral; cheng2021modeling used graph attention networks to model stock momentum spillover effects. However, deep learning methods face issues such as requiring large sample sizes for fitting and having weak model interpretability. In comparison, Hawkes processes model the intensity function of event occurrence, possess excellent statistical properties, and offer stronger interpretability. Multivariate Hawkes processes can also be used to capture relationships both within and between time series.

#### 1.2.3 Applications of Hawkes Processes in Finance

The Hawkes process, introduced by hawkes1971spectra, is used to characterize a class of point processes with self-exciting properties and is widely applied in high-frequency financial data analysis (bacry2015hawkes). For example, it explains volatility clustering, with Filimonov\_2012 applying it to analyze the endogenous nature of stock price volatility, forming an early warning framework for extreme events. dassios2011dynamic extended the Hawkes and Cox models, proposing a dynamic contagion model that can capture both self-excitement and external excitement. ait2015modeling used mutually exciting jump processes to model financial contagion. Building on the basic Hawkes model, zhu2013nonlinear discussed the statistical properties and estimation methods of nonlinear Hawkes models. wang2016isotonic proposed Isotonic Hawkes Processes for modeling nonlinear effects. mei2017neural combined neural networks with Hawkes processes, using LSTM model hidden variables to drive the conditional intensity function of Hawkes processes, proposing Neural Hawkes Processes. The combination of statistical models and deep learning methods greatly enhanced the model’s expressive ability, enabling it to characterize various features such as nonlinearity and self-inhibition.

Various methods have also been developed for model parameter estimation. For example, embrechts2011multivariate adopted maximum likelihood estimation, bacry2013modelling proposed a nonparametric estimation method based on spectral decomposition, fonseca2014hawkes adopted generalized method of moments for parameter estimation, and xiao2017modeling used neural networks to fit the intensity function of point processes. Given the excellent statistical properties of Hawkes models, this paper applies them to modeling contagion in China’s stock market.

### Research Approach and Paper Structure

This paper applies Hawkes processes to model financial contagion in China’s stock market, assuming that asset return is driven by its own internal rules and may be influenced by price movements in other sectors. First, we use self-exciting Hawkes processes to model stock indices to test whether A-share market indices exhibit trends. Second, we extend Hawkes processes to the mutual influence between multiple sector indices to detect sector index contagion.

Part One is the introduction, presenting the research background of applying Hawkes processes to financial contagion and reviewing related domestic and international research status. Part Two covers theoretical foundations, introducing basic concepts of Hawkes processes and statistical inference methods. Part Three presents empirical analysis, describing two experiments on market index predictability and sector index contagion and their respective results. Part Four contains experimental conclusions and discussion, summarizing the conclusions drawn from the experiments.

## Theory

### Hawkes Process

#### 2.1.1 Basics of Hawkes Process

The Hawkes process is a self-exciting counting process used to model the subsequent effects of extreme events. Its core concept is that the occurrence of extreme events increases the likelihood of similar events occurring afterward, similar to how aftershocks frequently follow major earthquakes. Mathematically, this influence is reflected in changes to the conditional intensity function of the counting process.

Let {N​(t):t≥0}\{N(t):t\geq 0\} be a counting process. Given the history ℋ​(t)\mathcal{H}(t) up to time tt, it satisfies:

|  |  |  |
| --- | --- | --- |
|  | P​(N​(t+h)−N​(t)=m|ℋ​(t))={1−λ∗​(t)​h+o​(h),m=0λ∗​(t)​h+o​(h),m=1o​(h),m≥2P(N(t+h)-N(t)=m|\mathcal{H}(t))=\begin{cases}1-\lambda^{\*}(t)h+o(h),&m=0\\ \lambda^{\*}(t)h+o(h),&m=1\\ o(h),&m\geq 2\end{cases} |  |

where λ∗​(t)\lambda^{\*}(t) is the conditional intensity function given the historical sequence. For convenience, the asterisk notation denotes conditioning on history, i.e., λ∗​(t)=λ​(t|ℋ​(u),u<t)\lambda^{\*}(t)=\lambda(t|\mathcal{H}(u),u<t). The same notation applies to conditional density function f∗​(t)f^{\*}(t) and conditional distribution function F∗​(t)F^{\*}(t). The conditional intensity function represents the expected rate of event arrival:

|  |  |  |
| --- | --- | --- |
|  | λ∗​(t)=limh→0E​(N​(t+h)−N​(t)|ℋ​(t))h.\lambda^{\*}(t)=\lim\_{h\rightarrow 0}\frac{E(N(t+h)-N(t)|\mathcal{H}(t))}{h}. |  |

###### Definition 1 (Hawkes Process)

A Hawkes process is a self-exciting point process N​(t)N(t) with conditional intensity function λ∗​(t)\lambda^{\*}(t) defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∗​(t)=μ+∫0tϕ​(t−u)​𝑑N​(u).\lambda^{\*}(t)=\mu+\int\_{0}^{t}\phi(t-u)dN(u). |  | (1) |

where μ>0\mu>0 is the baseline intensity, and ϕ:(0,∞)→[0,∞)\phi:(0,\infty)\rightarrow[0,\infty) is the excitation function. The Itô integral with respect to counting process N​(u)N(u) is defined as:

|  |  |  |
| --- | --- | --- |
|  | ∫0tϕ​(u)​𝑑N​(u)=∑0<u≤tϕ​(u)​Δ​N​(u),Δ​N​(u)=N​(u)−N​(u−).\int\_{0}^{t}\phi(u)dN(u)=\sum\_{0<u\leq t}\phi(u)\Delta N(u),\quad\Delta N(u)=N(u)-N(u^{-}). |  |

The excitation function ϕ​(⋅)\phi(\cdot) is typically chosen to be exponentially decaying, such as ϕ​(t)=α⋅ω​e−ω​(t−ti)\phi(t)=\alpha\cdot\omega e^{-\omega(t-t\_{i})}, yielding:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∗​(t)=μ+∑ti<tα⋅ω​e−ω​(t−ti)\lambda^{\*}(t)=\mu+\sum\_{t\_{i}<t}\alpha\cdot\omega e^{-\omega(t-t\_{i})} |  | (2) |

where α>0\alpha>0 represents the jump size in intensity due to each event, and ω>0\omega>0 determines the decay rate of the excitation. The stability condition for exponential kernels is α<1\alpha<1.

##### Multivariate Hawkes Process

In multivariate Hawkes processes, events are categorized into different types, each with its own conditional intensity function that may be influenced by both its own occurrences and events of other types. For an mm-type Hawkes process, let {(t1,d1),(t2,d2),…,(tN​(T),dN​(T))}\{(t\_{1},d\_{1}),(t\_{2},d\_{2}),\ldots,(t\_{N(T)},d\_{N(T)})\} be the observed event sequence up to time T, where tit\_{i} denotes the time of the ii-th event and di∈{1,2,…,m}d\_{i}\in\{1,2,\ldots,m\} represents its type.

Let {Nk​(t):t≥0,k=1,2,…,m}\{N\_{k}(t):t\geq 0,k=1,2,\ldots,m\} be the point process for type kk events, with conditional intensity function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λk∗​(t)=μk+∑j=1m∫0tϕk​j​(t−u)​𝑑Nj​(u),\lambda\_{k}^{\*}(t)=\mu\_{k}+\sum\_{j=1}^{m}\int\_{0}^{t}\phi\_{kj}(t-u)dN\_{j}(u), |  | (3) |

where μk\mu\_{k} is the background intensity for type k events, and ϕk​j​(⋅)\phi\_{kj}(\cdot) is the excitation function describing the influence of type j events on type k events.

###### Definition 2 (Multivariate Hawkes Process)

For an mm-type Hawkes process, let {(t1,d1),(t2,d2),…,(tN​(T),dN​(T))}\{(t\_{1},d\_{1}),(t\_{2},d\_{2}),\\
\ldots,(t\_{N(T)},d\_{N(T)})\} be the observed event sequence, where tit\_{i} denotes the time of the ii-th event and di∈{1,2,…,m}d\_{i}\in\{1,2,\ldots,m\} represents its type.

Let {Nk​(t):t≥0,k=1,2,…,m}\{N\_{k}(t):t\geq 0,k=1,2,\ldots,m\} be the point process for type kk events, with conditional intensity function:

|  |  |  |
| --- | --- | --- |
|  | λk∗​(t)=μk+∑j=1m∫0tϕk​j​(t−u)​𝑑Nj​(u)\lambda\_{k}^{\*}(t)=\mu\_{k}+\sum\_{j=1}^{m}\int\_{0}^{t}\phi\_{kj}(t-u)dN\_{j}(u) |  |

where: μk>0\mu\_{k}>0 is the background intensity for type kk events, ϕk​j​(⋅)\phi\_{kj}(\cdot) is the excitation function describing the influence of type jj events on type kk events.

For m-type multivariate Hawkes processes with exponential decay kernels, the vector form of the conditional intensity function is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝀∗​(t)=𝝁+∑(ti,di):ti<t𝜶di​𝝎​e−𝝎​(t−ti),\bm{\lambda}^{\*}(t)=\bm{\mu}+\sum\_{(t\_{i},d\_{i}):t\_{i}<t}\bm{\alpha}\_{d\_{i}}\bm{\omega}e^{-\bm{\omega}(t-t\_{i})}, |  | (4) |

where 𝝀∗​(t),𝝁,𝜶di,𝝎\bm{\lambda}^{\*}(t),\bm{\mu},\bm{\alpha}\_{d\_{i}},\bm{\omega} are m×1m\times 1 vectors.
The stationarity condition for a multivariate Hawkes process requires that the spectral radius of the impact matrix, denoted as ρ​(A)\rho(A), satisfies: ρ​(A)​=def​maxi⁡|λi|<1\rho(A)\overset{\text{def}}{=}\max\_{i}|\lambda\_{i}|<1,
where λi\lambda\_{i} are the eigenvalues of the impact matrix AA.

![Refer to caption](figures/int-00.png)


Figure 1: This figure illustrates intensity functions corresponding to a three-dimensional Hawkes process. Here, the impact matrix is configured as an upper triangle, where type 0 events are influenced by both type 1 and type 2 events. Conversely, type 2 events only receive signals from within their own type.

##### Nonlinear Hawkes Process

To capture inhibitory effects and nonlinear influences, the Hawkes process can be extended using link functions. By employing an appropriate link function, we avoid setting constraints on μ\mu and α\alpha to be positive. The conditional intensity function takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∗​(t)=g​(λ∗¯​(t))\lambda^{\*}(t)=g(\overline{\lambda^{\*}}(t)) |  | (5) |

where g​(⋅):ℝ→ℝ+g(\cdot):\mathbb{R}\rightarrow\mathbb{R}^{+} is the link function, and λ∗¯​(⋅):ℝ+→ℝ\overline{\lambda^{\*}}(\cdot):\mathbb{R}^{+}\rightarrow\mathbb{R} could take negative values. Common link functions include the softplus function g​(x)=log⁡(1+ex)g(x)=\log(1+e^{x}) and the ReLU function g​(x)=max⁡(x,0)g(x)=\max(x,0).

#### 2.1.2 Statistical Inference for Hawkes Processes

##### Parameter Estimation

This paper employs the estimation method of optimizing the likelihood function using stochastic gradient, focusing on Maximum Likelihood Estimation and stochastic gradient optimization methods.
Given event times {t1,t2,…,tN​(T)}\{t\_{1},t\_{2},\ldots,t\_{N(T)}\} on [0,T][0,T], the likelihood function L​(θ;T)L(\theta;T) for a univariate Hawkes process is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(θ;T)=[∏i=1N​(T)f∗​(ti)]​(1−F∗​(T)).L(\theta;T)=\left[\prod\_{i=1}^{N(T)}f^{\*}(t\_{i})\right](1-F^{\*}(T)). |  | (6) |

Using the relationship between conditional intensity and density functions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∗​(t)=f∗​(t)1−F∗​(t).\lambda^{\*}(t)=\frac{f^{\*}(t)}{1-F^{\*}(t)}. |  | (7) |

The likelihood function can be expressed as (shown in appendix):

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(θ;T)=[∏i=1N​(T)λ∗​(ti)]​e−∫0Tλ∗​(s)​𝑑s.L(\theta;T)=\left[\prod\_{i=1}^{N(T)}\lambda^{\*}(t\_{i})\right]e^{-\int\_{0}^{T}\lambda^{\*}(s)ds}. |  | (8) |

Denote Λj​(T)=∫0Tλj∗​(s)​𝑑s\Lambda\_{j}(T)=\int\_{0}^{T}\lambda\_{j}^{\*}(s)ds,
for m-type multivariate Hawkes processes, the likelihood function becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(θ;T)=[∏i=1N​(T)λdi∗​(ti)]​e−∑j=1mΛj​(T).L(\theta;T)=\left[\prod\_{i=1}^{N(T)}\lambda\_{d\_{i}}^{\*}(t\_{i})\right]e^{-\sum\_{j=1}^{m}\Lambda\_{j}(T)}. |  | (9) |

The log-likelihood is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡L​(θ;T)=∑ilog⁡λdi∗​(ti)−∑j=1m∫0tλj∗​(s)​𝑑s.\log L(\theta;T)=\sum\_{i}\log\lambda\_{d\_{i}}^{\*}(t\_{i})-\sum\_{j=1}^{m}\int\_{0}^{t}\lambda\_{j}^{\*}(s)ds. |  | (10) |

The main challenge lies in computing the second term ∫0tλj∗​(s)​𝑑s\int\_{0}^{t}\lambda\_{j}^{\*}(s)ds in the above equation. A Monte Carlo method can be employed to obtain an unbiased estimate of ∫0Tλj∗​(s)​𝑑s\int\_{0}^{T}\lambda\_{j}^{\*}(s)ds, which subsequently leads to an unbiased estimate of the gradient. This is possible because:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0Tλj∗​(s)​𝑑s=T​∫0Tλj∗​(s)T​𝑑s=T​𝔼s​(λj∗​(s))\int\_{0}^{T}\lambda\_{j}^{\*}(s)ds=T\int\_{0}^{T}\frac{\lambda\_{j}^{\*}(s)}{T}ds=T\mathbb{E}\_{s}(\lambda\_{j}^{\*}(s)) |  | (11) |

where 𝔼s​(⋅)\mathbb{E}\_{s}(\cdot) denotes the expectation with respect to the random variable ss following a uniform distribution U​(0,T)U(0,T). This allows us to randomly sample s1,…,sNs\_{1},\ldots,s\_{N} from U​(0,T)U(0,T), compute the mean of λj∗​(sk)\lambda\_{j}^{\*}(s\_{k}), and update the parameters using the back-propagation (BP) algorithm by mei2017neural. In summary, our estimation approach employs the negative log-likelihood as the objective function and utilizes stochastic gradient descent for parameter updates, as demonstrated in [1](https://arxiv.org/html/2512.08000v1#alg1 "Algorithm 1 ‣ Parameter Estimation ‣ 2.1.2 Statistical Inference for Hawkes Processes ‣ Hawkes Process ‣ Theory ‣ Analysis of Contagion in China’s Stock Market: A Hawkes Process Perspective").

Algorithm 1  Stochastic Gradient Descent Based on Monte Carlo Method

0: Hawkes model parameters AA, μ\mu, ω\omega; event sequence H​(t)H(t); batch size NN; observation time TT

1: for each event type mm do

2:  Generate NN samples Tm=[t1,t2,…,tN]T\_{m}=[t\_{1},t\_{2},\dots,t\_{N}], where ti∼𝒰​(0,T)t\_{i}\sim\mathcal{U}(0,T).

3:  Compute conditional intensities [λm∗​(t1),λm∗​(t2),…,λm∗​(tN)][\lambda\_{m}^{\*}(t\_{1}),\lambda\_{m}^{\*}(t\_{2}),\dots,\lambda\_{m}^{\*}(t\_{N})] using H​(t)H(t) and current model parameters.

4:  Estimate ∫0Tλm∗​(s)​𝑑s\int\_{0}^{T}\lambda\_{m}^{\*}(s)\,ds using Monte Carlo integration:
Im=∑i=1Nλm∗​(ti)N×TI\_{m}=\frac{\sum\_{i=1}^{N}\lambda\_{m}^{\*}(t\_{i})}{N}\times T.

5:  Compute the negative log-likelihood (NLL) estimate:
NLL=−∑ti∈H​(t)log⁡λdi∗​(ti)+∑j=1mIm\text{NLL}=-\sum\_{t\_{i}\in H(t)}\log\lambda\_{d\_{i}}^{\*}(t\_{i})+\sum\_{j=1}^{m}I\_{m}.

6:  Perform backpropagation: NLL.backward().

7:  Update model parameters using gradient descent.

8: end for

8: Updated model parameters AA, μ\mu, ω\omega

## Empirical Analysis

### Self-Exciting Properties of Market Indices

Experiment 1 uses daily return series of individual market indices to fit multivariate Hawkes processes, examining the self-exciting properties of daily returns for three indices: Shanghai Composite Index, Shenzhen Component Index, and ChiNext Index(Nasdaq-style Growth Enterprise Index).

#### 3.1.1 Dataset

The experiment uses time series data of stock indices, including daily returns of Shanghai Composite Index, Shenzhen Component Index, and ChiNext Index. The time period spans from February 2013 to March 2023, with a sample size of 2,452. We display the descriptive statistics and cumulative return rates of those indices.

Table 1: Descriptive Statistics of Daily Index Returns

| Index Name | Count | Mean | Std | Min | Median | Max | Skew | Kurtosis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shanghai Composite | 2452 | 0.021 | 1.32 | -8.491 | 0.051 | 5.764 | -0.927 | 6.71 |
| Shenzhen Component | 2452 | 0.02 | 1.601 | -8.446 | 0.036 | 6.454 | -0.683 | 3.727 |
| ChiNext | 2452 | 0.06 | 1.944 | -8.91 | 0.045 | 7.159 | -0.378 | 2.034 |

![Refer to caption](figures/desc-ind0.png)


Figure 2: Cumulative return rates of major Chinese market indices (Shanghai Stock Exchange Composite Index(SSE), Shenzhen Component Index(SZI), and Growth Enterprise Index(GEI)) from February 26, 2013 to March 2023. The base value is normalized to 1.0 on February 26, 2013.

During the study period, Shenzhen Component Index and ChiNext Index showed higher volatility. ChiNext Index returns exhibited characteristics of high mean and high volatility, while Shanghai Composite Index displayed left-skewed, leptokurtic features. The statistical properties indicate different market styles, closely related to their constituent stocks. The Shanghai Composite Index(SSE) mainly comprises traditional industries such as finance, real estate, and consumption, while Shenzhen Component(SZI) and ChiNext(GEI) indices include many healthcare and information technology companies.

#### 3.1.2 Experimental Design and Results

Following embrechts2011multivariate, daily returns were divided into three segments based on the 10th and 90th percentiles of the Shanghai Composite Index return history: sharp decline, normal range, and sharp rise. When returns fall into either the sharp decline or sharp rise range, it is recorded as a special event occurrence. The return series was transformed into sequences of two types of event occurrences, fitting a bivariate Hawkes model. 85% of the time series was used as the training set (2,084 samples) and 15% as the validation set (368 samples). Sharp rise events were labeled as type 0, sharp decline events as type 1. An exponential kernel Hawkes model was fitted using Python’s tick module for parameter estimation, yielding:

Impact matrix and baseline intensity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A=[αi​j]=[0.3820.3870.2180.343],μ=[0.0240.044]A=[\alpha\_{ij}]=\begin{bmatrix}0.382&0.387\\ 0.218&0.343\end{bmatrix},\ \mu=[0.024\quad 0.044] |  | (12) |

The decay rate ω\omega was set as a hyperparameter, assuming consistent decay rates for both event types. Grid search determined ω=0.1\omega=0.1.
In the impact matrix, αi​j\alpha\_{ij} represents the influence of the occurrence of the jth type of event on the intensity function of the ith type of event. It is noted that regardless of the occurrence of significant upward events (first column of the impact matrix) or significant downward events (second column of the impact matrix), the impact on the conditional intensity function of significant upward events is higher than that of significant downward events. This indicates that the likelihood of the stock index maintaining growth after a significant increase is higher than after a significant decrease, while there is a greater possibility of a rebound after a significant decrease; however, the possibility of further decline is also considerable. Among the four values in the impact matrix, only the transmission impact of significant upward events on significant downward events is relatively small, which to some extent reflects the rationality of chasing gains and cutting losses. The relatively large values of α00\alpha\_{00} and α11\alpha\_{11} demonstrate the continuity of upward or downward trends. Additionally, the relatively large value of α01\alpha\_{01} indicates that the Shanghai Composite Index is prone to experiencing ”oversold rebounds.” The conditional intensity functions of the two types of events are depicted below.

![Refer to caption](figures/int0.png)


Figure 3: Conditional density functions and barplots of defined extreme events in the SSE Index (2013-2021), where Type 0 and Type 1 represent large upward and downward movements, respectively. The market was very active in 2014-2015, followed by a period of relative stability from 2016 to 2018.

Using the same method for Shenzhen Component Index and ChiNext Index daily returns, the quantiles and estimates are:

Table 2: Parameter Comparison of Three Major Indices

| Index Name | 0.1, 0.9 quantile (%) | ω\omega | Baseline μ\mu | Impact Matrix AA |
| --- | --- | --- | --- | --- |
| Shanghai Composite | [-1.285 1.481] | 0.1 | [0.024;0.044][0.024;0.044] | [0.3820.3870.2180.343]\begin{bmatrix}0.382&0.387\\ 0.218&0.343\end{bmatrix} |
| Shenzhen Component | [-1.701 1.891] | 0.1 | [0.038;0.047][0.038;0.047] | [0.1750.4510.1550.381]\begin{bmatrix}0.175&0.451\\ 0.155&0.381\end{bmatrix} |
| ChiNext | [-2.105 2.502] | 0.1 | [0.034;0.05][0.034;0.05] | [0.280.3850.1540.348]\begin{bmatrix}0.28&0.385\\ 0.154&0.348\end{bmatrix} |

### Hawkes Process Variants: Inhibition and Nonlinear Effects

A variant of Hawkes processes allows for self-inhibition or mutual inhibition characteristics, for example, by allowing αi​j<0\alpha\_{ij}<0 in the exponential kernel form while ensuring the conditional intensity function λ∗​(t)\lambda^{\*}(t) remains non-negative. A more generalized form allows event impacts to propagate nonlinearly through link functions. Experiment 2 uses extended Hawkes processes to explore market sector rotation effects.

#### 3.2.1 Dataset

Experiment 2 data includes three sector indices: CSI Consumer Index (000932), CSI Healthcare Index (000933), and CSI Finance & Real Estate Index (000934) daily return series, spanning from March 2013 to March 2023, with 2,452 samples.

Table 3: Descriptive Statistics of Sector Index Daily Returns

| Index Name | Count | Mean | Std | Min | Median | Max | Skew | Kurtosis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CSI Consumer | 2452 | 0.067 | 1.648 | -8.325 | 0.061 | 7.214 | -0.361 | 2.753 |
| CSI Healthcare | 2452 | 0.035 | 1.659 | -8.484 | 0.067 | 7.909 | -0.395 | 2.67 |
| CSI Fin&RE | 2452 | 0.023 | 1.557 | -9.363 | -0.034 | 8.918 | -0.086 | 5.173 |

![Refer to caption](figures/exp2-0.png)


Figure 4: Normalized returns across three sectors (consumption, medical industry, and financial) in Chinese stock markets, 2013-2023. The baseline return is normalized to unity on February 26, 2013. The figure illustrates the relative performance and temporal evolution of these sectors over a decade-long period.

#### 3.2.2 Experimental Design and Results

Given the time-sensitive nature of sector rotation, we initially segmented the sample sequence into 15 periods, with each period comprising 150 trading days. Following previous conventions, extreme upward and downward movements are considered as two distinct event types. With three sectors under consideration, this results in six different event categories, enabling us to model the contagion effects using a six-dimensional Hawkes process.
We assume the conditional intensity function takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ∗​(t)=g​(λ∗¯​(t)).λ∗¯​(t)=μ+α​ω​e−ω​t,μ∈ℝ,α∈ℝ,ω>0.g​(x)=max⁡(x,0.01).\lambda^{\*}(t)=g(\overline{\lambda^{\*}}(t)).\ \overline{\lambda^{\*}}(t)=\mu+\alpha\omega e^{-\omega t},\mu\in\mathbb{R},\alpha\in\mathbb{R},\omega>0.\ g(x)=\max(x,0.01). |  | (13) |

In this setting, we remove the non-negativity constraints on both the background intensity μ\mu and the influence matrix parameter α\alpha to model inhibitory effects. The link function g​(⋅)g(\cdot) ensures the non-negativity of conditional intensity.

Parameter estimation is conducted via algorithms presented in section [2.1.2](https://arxiv.org/html/2512.08000v1#S2.SS1.SSS2.Px1 "Parameter Estimation ‣ 2.1.2 Statistical Inference for Hawkes Processes ‣ Hawkes Process ‣ Theory ‣ Analysis of Contagion in China’s Stock Market: A Hawkes Process Perspective"). Representative periods 3(2014.12 to 2015.08) and periods 5(2016.03 to 2016.11) are selected for analysis based on market activity levels:

* •

  Period 3 (2014-12 to 2015-08): a structural bull market with higher frequencies of significant upward movements compared to downward movements.
* •

  Period 5 (2016-03 to 2016-11): pessimistic sentiment, characterized by reduced trading activity and notably lower frequencies of both substantial gains and losses compared to previous periods.

The estimated model parameters are given in table [4](https://arxiv.org/html/2512.08000v1#S3.T4 "Table 4 ‣ 3.2.2 Experimental Design and Results ‣ Hawkes Process Variants: Inhibition and Nonlinear Effects ‣ Empirical Analysis ‣ Analysis of Contagion in China’s Stock Market: A Hawkes Process Perspective").

Table 4: Estimated parameters for the Hawkes process model ([13](https://arxiv.org/html/2512.08000v1#S3.E13 "In 3.2.2 Experimental Design and Results ‣ Hawkes Process Variants: Inhibition and Nonlinear Effects ‣ Empirical Analysis ‣ Analysis of Contagion in China’s Stock Market: A Hawkes Process Perspective")): activation rate (Ai​jA\_{ij}), background intensity (μ\mu), and decay rate (ω\omega) for Period 3 and Period 5. Category 0-5 represents event type: cons-up, med-up, fin-up, cons-down, med-down, fin-down respectively. The element Ai​jA\_{ij} represents the excitation effect of type j
event on type i.

(a) Influence matrix of Period 3(2014.12-2015.08)

| Ai​jA\_{ij} | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.161 | 0.240 | 0.253 | -0.335 | -0.469 | -0.154 |
| 1 | 0.157 | 1.143 | -0.238 | -0.230 | -0.173 | -0.208 |
| 2 | -0.105 | -0.298 | 1.313 | -0.371 | -0.474 | -0.425 |
| 3 | 0.109 | 0.093 | 0.002 | 0.671 | 0.420 | -0.067 |
| 4 | 0.037 | -0.191 | -0.005 | 0.460 | 0.831 | 0.078 |
| 5 | -0.366 | -0.100 | -0.136 | 0.071 | 0.033 | 1.092 |

(b) Influence matrix of Period 5(2016.03-2016.11)

| Ai​jA\_{ij} | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | -0.317 | -0.536 | -0.323 | -0.340 | -0.424 | -0.452 |
| 1 | -0.375 | -0.437 | -0.315 | -0.478 | -0.379 | -0.600 |
| 2 | -0.564 | -0.314 | -0.136 | -0.408 | -0.574 | -0.577 |
| 3 | -0.576 | -0.452 | -0.427 | -0.265 | -0.470 | -0.517 |
| 4 | -0.405 | -0.505 | -0.396 | -0.406 | -0.346 | -0.401 |
| 5 | -0.203 | -0.535 | -0.418 | -0.334 | -0.403 | -0.338 |

(c) Background Intensity μ\mu and Decay Parameter ω\omega

| Period | μ\mu | ω\omega |
| --- | --- | --- |
| 3 | [-0.226, -0.200, -0.341, -0.079, -0.024, -0.095] | 0.702 |
| 5 | [0.089, 0.093, 0.058, 0.091, 0.091, 0.061] | 0.004 |

The (6×6)(6\times 6) influence matrix, partitioned into four (3×3)(3\times 3) blocks
[A3×3B3×3C3×3D3×3]\begin{bmatrix}A\_{3\times 3}&B\_{3\times 3}\\
C\_{3\times 3}&D\_{3\times 3}\end{bmatrix}. Block AA indicates upward trend; Block BB represents oversold rebound; Block CC manifests pullback and Block DD displays the downward trend.

During active trading periods, such as period 3, the generalized Hawkes model identified evidence of both upward and downward trend continuity, which is underscored by the presence of diagonal elements in the estimated influence matrix.

Comparison of off-diagonal blocks exposes cross-trend influences. Greater intensity within these blocks suggests a swifter rotation of market focus. In contrast, during market dormancy, exemplified by period 5, the disparity between diagonal and off-diagonal values diminishes, suggesting potential sector rotation phenomenon. A reduced decay parameter during a stagnant market phase signifies market inertia.

## Conclusions

In the first experiment, this study examined the self-exciting characteristics of three major market indices—Shanghai Composite Index, Shenzhen Component Index, and ChiNext Index—through multivariate Hawkes processes. The evidence supported the existence of both upward and downward trends in the Shanghai Composite Index, as well as oversold rebounds.

In the second experiment, we modeled the contagion effects among Consumption, Healthcare, and Financial sector indices using Hawkes processes that incorporated inhibition and nonlinear effects. The findings revealed that Hawkes processes can effectively investigate market styles across different periods. During the high-trading-volume period from January 2015 to March 2016, trend continuation was evident in both structural bull and bear trend. Conversely, during the low-trading-volume period from March 2016 to August 2016, the market exhibited sector rotation patterns.

## Appendix A Supplementary Derivations for Statistical Inference of Hawkes Process in Chapter 2, Section 2

### Proof of λ∗​(t)=f∗​(t)1−F∗​(t).\lambda^{\*}(t)=\frac{f^{\*}(t)}{1-F^{\*}(t)}.

###### Proof of equation ([7](https://arxiv.org/html/2512.08000v1#S2.E7 "In Parameter Estimation ‣ 2.1.2 Statistical Inference for Hawkes Processes ‣ Hawkes Process ‣ Theory ‣ Analysis of Contagion in China’s Stock Market: A Hawkes Process Perspective")).

Since P​(N​(t+h)−N​(t)≥2|ℋ​(t))=o​(h)P(N(t+h)-N(t)\geq 2|\mathcal{H}(t))=o(h), and assuming i−1i-1 events have occurred at time tt, i.e., N​(t)=i−1N(t)=i-1, and letting X(i)X\_{(i)} denote the occurrence time of the ii-th event, we have:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λ∗​(t)\displaystyle\lambda^{\*}(t) | =limh→0E​(N​(t+h)−N​(t)|ℋ​(t))h\displaystyle=\lim\_{h\rightarrow 0}\frac{E(N(t+h)-N(t)|\mathcal{H(}t))}{h} |  | (14) |
|  |  | =limh→0P​(Xi∈(t,t+h)​|Xi>​t)h\displaystyle=\lim\_{h\rightarrow 0}\frac{P(X\_{i}\in(t,t+h)|X\_{i}>t)}{h} |  |
|  |  | =limh→0F∗​(t+h)−F∗​(t)(1−F∗​(t))​h\displaystyle=\lim\_{h\rightarrow 0}\frac{F^{\*}(t+h)-F^{\*}(t)}{\left(1-F^{\*}(t)\right)h} |  |
|  |  | =f∗​(t)1−F∗​(t)\displaystyle=\frac{f^{\*}(t)}{1-F^{\*}(t)} |  |

∎

### Proof of f∗​(ti)=λ∗​(ti)​exp⁡(−∫ti−1tiλ∗​(s)​𝑑s)f^{\*}(t\_{i})=\lambda^{\*}(t\_{i})\exp(-\int\_{t\_{i-1}}^{t\_{i}}\lambda^{\*}(s)ds)

###### Proof.

From the result in Appendix A.1, λ∗​(t)=f∗​(t)1−F∗​(t)=−d​ln⁡(1−F∗​(t))\lambda^{\*}(t)=\frac{f^{\*}(t)}{1-F^{\*}(t)}=-d\ln(1-F^{\*}(t)). Integrating t from ti−1t\_{i-1} to tit\_{i}, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ti−1tiλ∗​(t)​𝑑t=−(l​n​(1−F∗​(ti))−l​n​(1−F∗​(ti−1)))\int\_{t\_{i-1}}^{t\_{i}}\lambda^{\*}(t)dt=-(ln(1-F^{\*}(t\_{i}))-ln(1-F^{\*}(t\_{i-1}))) |  | (15) |

Under the simple point process assumption, the probability of multiple events occurring at the same instant is zero, thus F∗​(ti−1)=0F^{\*}(t\_{i-1})=0. Therefore:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ti−1tiλ∗​(t)​𝑑t=−l​n​(1−F∗​(ti))\int\_{t\_{i-1}}^{t\_{i}}\lambda^{\*}(t)dt=-ln(1-F^{\*}(t\_{i})) |  | (16) |

Substituting

|  |  |  |
| --- | --- | --- |
|  | 1−F∗​(ti)=λ∗​(ti)​f∗​(ti),1-F^{\*}(t\_{i})=\lambda^{\*}(t\_{i})f^{\*}(t\_{i}), |  |

we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f∗​(ti)=λ∗​(ti)​exp⁡(−∫ti−1tiλ∗​(s)​𝑑s)f^{\*}(t\_{i})=\lambda^{\*}(t\_{i})\exp(-\int\_{t\_{i-1}}^{t\_{i}}\lambda^{\*}(s)ds) |  | (17) |

∎

### Proof of L​(θ;T)=[∏i=1n​(T)λ∗​(ti)]​e−∫0Tλ∗​(s)​𝑑sL(\theta;T)=\left[\prod\_{i=1}^{n(T)}\lambda^{\*}(t\_{i})\right]e^{-\int\_{0}^{T}\lambda^{\*}(s)ds}

###### Proof of equation ([8](https://arxiv.org/html/2512.08000v1#S2.E8 "In Parameter Estimation ‣ 2.1.2 Statistical Inference for Hawkes Processes ‣ Hawkes Process ‣ Theory ‣ Analysis of Contagion in China’s Stock Market: A Hawkes Process Perspective")).

Since

|  |  |  |
| --- | --- | --- |
|  | L​(θ;T)=[∏i=1N​(T)f∗​(ti)]​(1−F∗​(T))and​ 1−F∗​(T)=exp⁡(−∫tN​(T)Tλ∗​(s)​𝑑s)L(\theta;T)=\left[\prod\_{i=1}^{N(T)}f^{\*}(t\_{i})\right](1-F^{\*}(T))\ \ \text{and}\ \ 1-F^{\*}(T)=\exp(-\int\_{t\_{N(T)}}^{T}\lambda^{\*}(s)ds) |  |

Substituting the result from equation ([17](https://arxiv.org/html/2512.08000v1#A1.E17 "In Proof of 𝑓^∗⁢(𝑡_𝑖)=𝜆^∗⁢(𝑡_𝑖)⁢exp(-∫_𝑡_{𝑖-1}^𝑡_𝑖{𝜆^∗⁢(𝑠)⁢𝑑𝑠}) ‣ Appendix A Supplementary Derivations for Statistical Inference of Hawkes Process in Chapter 2, Section 2 ‣ Analysis of Contagion in China’s Stock Market: A Hawkes Process Perspective")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | f∗​(ti)=[∏i=1N​(T)λ∗​(ti)]​exp⁡(−∑i=1N​(T)∫ti−1tiλ∗​(s)​𝑑s−∫tN​(T)Tλ∗​(s)​𝑑s)\displaystyle f^{\*}(t\_{i})=\left[\prod\_{i=1}^{N(T)}\lambda^{\*}(t\_{i})\right]\exp\left(-\sum\_{i=1}^{N(T)}\int\_{t\_{i-1}}^{t\_{i}}\lambda^{\*}(s)ds-\int\_{t\_{N(T)}}^{T}\lambda^{\*}(s)ds\right) |  | (18) |

Therefore:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(θ;T)=[∏i=1N​(T)λ∗​(ti)]​e−∫0Tλ∗​(s)​𝑑sL(\theta;T)=\left[\prod\_{i=1}^{N(T)}\lambda^{\*}(t\_{i})\right]e^{-\int\_{0}^{T}\lambda^{\*}(s)ds} |  | (19) |

∎

## Appendix B Goodness-of-Fit Testing

###### Theorem 1 (Random Time Change Theorem)

Given a point process realization {t1,t2,…,tk}\{t\_{1},t\_{2},\ldots,t\_{k}\} on [0,T][0,T], if the conditional intensity function satisfies λ∗​(t)>0\lambda^{\*}(t)>0, t∈[0,T]t\in[0,T] and compensator Λ​(T)=∫0Tλ∗​(s)​𝑑s<∞\Lambda(T)=\int\_{0}^{T}\lambda^{\*}(s)ds<\infty almost everywhere, then the time points {Λ​(t1),Λ​(t2),…,Λ​(tk)}\{\Lambda(t\_{1}),\Lambda(t\_{2}),\ldots,\Lambda(t\_{k})\} follow a unit-rate Poisson process. Conversely, {t1,t2,…,tk}\{t\_{1},t\_{2},\ldots,t\_{k}\} is a realization of a point process with conditional intensity function λ∗​(t)\lambda^{\*}(t) if and only if {Λ​(t1),Λ​(t2),…,Λ​(tk)}\{\Lambda(t\_{1}),\Lambda(t\_{2}),\ldots,\Lambda(t\_{k})\} follows a unit-rate Poisson process.

If the λ∗​(t)\lambda^{\*}(t) is correctly specified, the sequence of compensator Λ​(ti){\Lambda(t\_{i})} follows a unit-rate Poisson process. For multivariate Hawkes processes, we can verify whether the transformed sequences {Λk​(t1),Λk​(t2),…,Λk​(tk)}\{\Lambda\_{k}(t\_{1}),\Lambda\_{k}(t\_{2}),\ldots,\Lambda\_{k}(t\_{k})\}, k=1,2,…,mk=1,2,\ldots,m, follow unit-rate Poisson processes. Q-Q plots can be used to check the relationship between empirical and theoretical quantiles. For testing independence in Poisson processes, we can examine the scatter plot of transformed intervals τi+1−τi\tau\_{i+1}-\tau\_{i}, where τi=Λ​(ti+1)−Λ​(ti)\tau\_{i}=\Lambda(t\_{i+1})-\Lambda(t\_{i}). The absence of obvious patterns suggests temporal independence.

In the fitting tests, a homogeneous Poisson process was used as the baseline model to fit the sequence data, comparing results with the Hawkes process.

(A) Homogeneous Poisson Process Fitting and Testing

Under the homogeneous Poisson process assumption, inter-event times follow an exponential distribution. Using moment estimation λ^=1∑iΔ​tin\hat{\lambda}=\frac{1}{\sum\_{i}\frac{\Delta t\_{i}}{n}}
where Δ​ti\Delta t\_{i} is the iith interval time, nn is the total number of events. For period between 2013.02 and 2022.03,

|  |  |  |
| --- | --- | --- |
|  | λ^t​r​a​i​n=[0.100,0.101],\hat{\lambda}\_{train}=[0.100,0.101], |  |

For period between 2022.03 and 2023.03:
λ^t​e​s​t=[0.067,0.082].\hat{\lambda}\_{test}=[0.067,0.082].
λ^t​e​s​t<λ^t​r​a​i​n\hat{\lambda}\_{test}<\hat{\lambda}\_{train} indicates that the average interval between extreme events has increased in the past year, suggesting a scheme change in market structure.

![Refer to caption](figures/gof0-pos.png)


Figure 5: Q-Q Plot under homogeneous Poisson assumption.

(B) Hawkes Process Fitting Tests

According to Theorem [1](https://arxiv.org/html/2512.08000v1#Thmtheorem1 "Theorem 1 (Random Time Change Theorem) ‣ Appendix B Goodness-of-Fit Testing ‣ Analysis of Contagion in China’s Stock Market: A Hawkes Process Perspective"), Q-Q plots were used to test whether time intervals Δ​Λ​(ti)\Delta\Lambda(t\_{i}) follow an exponential distribution with scale parameter 1.

![Refer to caption](figures/gof1-haw.png)


Figure 6: Q-Q Plot under Hawkes process assumption.

![Refer to caption](figures/gof3.png)


Figure 7: Scatter plot of transformed inter-event time intervals (Λt+1−Λt,Λt−Λt−1)(\Lambda\_{t+1}-\Lambda\_{t},\Lambda\_{t}-\Lambda\_{t-1}). The absence of discernible patterns suggests the statistical independence of consecutive time intervals, as expected under the time transformation theorem for point processes.