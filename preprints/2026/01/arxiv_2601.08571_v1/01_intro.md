---
authors:
- Salam Rabindrajit Luwang
- Buddha Nath Sharma
- Kundan Mukhia
- Md. Nurujjaman
- Anish Rai
- Filippo Petroni
- Luis E. C. Rocha
doc_id: arxiv:2601.08571v1
family_id: arxiv:2601.08571
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets
url_abs: http://arxiv.org/abs/2601.08571v1
url_html: https://arxiv.org/html/2601.08571v1
venue: arXiv q-fin
version: 1
year: 2026
---


S. R. Luwang
[salamrabindrajit@gmail.com](mailto:salamrabindrajit@gmail.com)

B. N. Sharma
[bnsharma09@yahoo.com](mailto:bnsharma09@yahoo.com)

K. Mukhia
[kundanmukhia07@gmail.com](mailto:kundanmukhia07@gmail.com)

Md. Nurujjaman
[md.nurujjaman@nitsikkim.ac.in](mailto:md.nurujjaman@nitsikkim.ac.in)

Anish Rai
[anishrai412@gmail.com](mailto:anishrai412@gmail.com)

Filippo Petroni
[fpetroni@luiss.it](mailto:fpetroni@luiss.it)

Luis E. C. Rocha
[luis.rocha@ugent.be](mailto:luis.rocha@ugent.be)

###### Abstract

Financial markets alternate between tranquil periods and episodes of stress, and return dynamics can change substantially across these regimes. We study regime-dependent dynamics in developed and developing equity indices using a data-driven Hilbert–Huang-based regime identification and profiling pipeline, followed by variable-length Markov modeling of categorized returns. Market regimes are identified using an Empirical Mode Decomposition-based Hilbert–Huang Transform, where instantaneous energy from the Hilbert spectrum separates Normal, High, and Extreme regimes. We then profile each regime using Holo–Hilbert Spectral Analysis, which jointly resolves carrier frequencies, amplitude-modulation frequencies, and amplitude-modulation energy (AME). AME, interpreted as volatility intensity, declines monotonically from Extreme to High to Normal regimes. This decline is markedly sharper in developed markets, while developing markets retain higher baseline volatility intensity even in Normal regimes. Building on these regime-specific volatility signatures, we discretize daily returns into five quintile states 𝚁1\mathtt{R}\_{1} to 𝚁5\mathtt{R}\_{5} and estimate Variable-Length Markov Chains via context trees within each regime. Unconditional state probabilities show tail states dominate in Extreme regimes and recede as regimes stabilize, alongside persistent downside asymmetry. Entropy peaks in High regimes, indicating maximum unpredictability during moderate-volatility periods. Conditional transition dynamics, evaluated over contexts of length up to three days from the context-tree estimates, indicate that developed markets normalize more effectively as stress subsides, whereas developing markets retain residual tail dependence and downside persistence even in Normal regimes, consistent with a coexistence of continuation and burst-like shifts. Overall, market maturity shapes both the pace of stabilization and the persistence of tail dependence, supporting tighter risk controls not only during crises but also during periods classified as stable.

###### keywords:

Hilbert-Huang Transform , Holo-Hilbert Spectral Analysis , volatility intensity , market regimes , variable-length Markov chains , context trees

\affiliation

[aff1]organization=Department of Physics, National Institute of Technology Sikkim,
postcode=737139,
country=India

\affiliation

[aff2]organization=Chennai Mathematical Institute,
postcode=603103,
country=India

\affiliation

[aff3]organization=Department of Economics, University G. d’Annunzio of Chieti-Pescara,
postcode=65127,
country=Italy

\affiliation

[aff4]organization=Department of Economics, Ghent University,
postcode=9000,
country=Belgium

\affiliation

[aff5]organization=Department of Physics and Astronomy, Ghent University,
postcode=9000,
country=Belgium

## 1 Introduction

Complex systems such as the stock market rarely move along one smooth and simple path. They typically alternate between distinct regimes – periods of relatively stable conditions and episodes of rapid growth or sudden collapse Hamilton [[1990](https://arxiv.org/html/2601.08571v1#bib.bib1 "Analysis of time series subject to changes in regime")], Ang and Timmermann [[2012](https://arxiv.org/html/2601.08571v1#bib.bib2 "Regime changes and financial markets")]. During stable regimes in the stock market, volatility remains low, asset returns are moderate, and liquidity is abundant. On the other hand, turbulent regimes are marked by sharp price swings, widening bid-ask spreads, and heightened probabilities of extreme outcomes – losses or gains Engle [[2004](https://arxiv.org/html/2601.08571v1#bib.bib3 "Risk and volatility: econometric models and financial practice")], Longin [[1996](https://arxiv.org/html/2601.08571v1#bib.bib4 "The asymptotic distribution of extreme stock market returns")]. These unique statistical profiles influence how returns transition between categories – such as extreme losses, minor fluctuations, or substantial gains, within a regime Rey et al. [[2014](https://arxiv.org/html/2601.08571v1#bib.bib5 "Detection of high and low states in stock market returns with mcmc method in a markov switching model")], Hamilton [[1989](https://arxiv.org/html/2601.08571v1#bib.bib69 "A new approach to the economic analysis of nonstationary time series and the business cycle")], BenSaïda [[2015](https://arxiv.org/html/2601.08571v1#bib.bib7 "The frequency of regime switching in financial market volatility")]. Consequently, investment strategies and risk management calibrated for one regime may perform poorly or become risky when market conditions shift Ang and Timmermann [[2012](https://arxiv.org/html/2601.08571v1#bib.bib2 "Regime changes and financial markets")], Kritzman et al. [[2012](https://arxiv.org/html/2601.08571v1#bib.bib13 "Regime shifts: implications for dynamic strategies (corrected)")], Nystrup et al. [[2015](https://arxiv.org/html/2601.08571v1#bib.bib17 "Regime-based versus static asset allocation: letting the data speak")]. These considerations highlight the importance of identifying market regimes and analyzing return dynamics within each regime to manage risks better and improve portfolio decisions, which are key steps for navigating the uncertain nature of stock markets.

A broad literature has examined stock market return dynamics using diverse methodological frameworks Ang and Bekaert [[2007](https://arxiv.org/html/2601.08571v1#bib.bib36 "Stock return predictability: is it there?")], Flannery and Protopapadakis [[2002](https://arxiv.org/html/2601.08571v1#bib.bib37 "Macroeconomic factors do influence aggregate stock returns")], Marquering and Verbeek [[2004](https://arxiv.org/html/2601.08571v1#bib.bib39 "The economic value of predicting stock index returns and volatility")], Avramov and Chordia [[2006](https://arxiv.org/html/2601.08571v1#bib.bib38 "Predicting stock returns")], Rabindrajit Luwang et al. [[2024](https://arxiv.org/html/2601.08571v1#bib.bib52 "High-frequency stock market order transitions during the us–china trade war 2018: a discrete-time markov chain analysis")]. Markov-based models have shown to be particularly effective in capturing regime-dependent behavior. Existing studies have used Markov regime-switching specifications to model shifts in conditional variance Chang [[2009](https://arxiv.org/html/2601.08571v1#bib.bib51 "Do macroeconomic variables have regime-dependent effects on stock return dynamics? evidence from the markov regime switching model")], Markov-chain formulations to test persistence and deviations from the random-walk hypothesis McQueen and Thorley [[1991](https://arxiv.org/html/2601.08571v1#bib.bib99 "Are stock returns predictable? a test using markov chains")], and forecasting frameworks based on regular and absorbing Markov chains Huang et al. [[2017](https://arxiv.org/html/2601.08571v1#bib.bib42 "Applying a markov chain for the stock pricing of a novel forecasting model")]. Extensions that incorporate memory effects, including semi-Markov and indexed Markov formulations, further enrich this line of work by allowing history-dependent and duration-dependent dynamics, with particular relevance for high-frequency financial data D’Amico et al. [[2019](https://arxiv.org/html/2601.08571v1#bib.bib91 "Change point dynamics for financial data: an indexed markov chain approach")], D’Amico and Petroni [[2018](https://arxiv.org/html/2601.08571v1#bib.bib92 "Copula based multivariate semi-markov models with applications in high-frequency finance"), [2012](https://arxiv.org/html/2601.08571v1#bib.bib21 "Weighted-indexed semi-markov models for modeling financial returns"), [2011](https://arxiv.org/html/2601.08571v1#bib.bib93 "A semi-markov model with memory for price changes")]. Related applications also examine asymmetric transmission channels such as the impact of oil price shocks on stock returns Reboredo [[2010](https://arxiv.org/html/2601.08571v1#bib.bib41 "Nonlinear effects of oil shocks on stock returns: a markov-switching approach")]. Despite these advances, many Markov-based approaches still impose a fixed conditioning structure on transitions, including fixed order, prescribed indexing, or parametric kernels, which can limit their ability to capture complex and adaptive temporal dependencies in return dynamics. Variable-length Markov chain (VLMC), which allow the effective memory length to vary according to statistically significant contexts, offers a flexible alternative. However, to the best of our knowledge, VLMCs have not yet been employed to analyze transitions between return categories such as extreme losses, minor fluctuations, and substantial gains across distinct market regimes.

To analyze regime-specific transition dynamics between return categories, market regimes must first be reliably identified and differentiated. In this paper, we employ the Empirical mode decomposition-based Hilbert-Huang Transform (HHT) framework for regime identification Rai et al. [[2023](https://arxiv.org/html/2601.08571v1#bib.bib22 "Detection and forecasting of extreme events in stock price triggered by fundamental, technical, and external factors")]. While index return series are often weakly stationary Cont [[2001](https://arxiv.org/html/2601.08571v1#bib.bib113 "Empirical properties of asset returns: stylized facts and statistical issues")], their volatility dynamics are highly time-varying and exhibit intermittent bursts, particularly during periods of market stress Mandelbrot and others [[1963](https://arxiv.org/html/2601.08571v1#bib.bib8 "The variation of certain speculative prices")], Schwert [[1989](https://arxiv.org/html/2601.08571v1#bib.bib9 "Why does stock market volatility change over time?")]. Abrupt changes in fluctuation intensity and short-lived episodes of elevated activity are therefore central features of financial returns rather than rare anomalies Lux and Marchesi [[2000](https://arxiv.org/html/2601.08571v1#bib.bib14 "Volatility clustering in financial markets: a microsimulation of interacting agents")], Engle and Patton [[2007](https://arxiv.org/html/2601.08571v1#bib.bib15 "What good is a volatility model?")]. Standard volatility measures, including rolling standard deviations or GARCH-type conditional variances, provide smoothed and model-dependent estimates of risk intensity and are primarily designed to capture gradual volatility clustering Andersen and Bollerslev [[1998](https://arxiv.org/html/2601.08571v1#bib.bib10 "Answering the skeptics: yes, standard volatility models do provide accurate forecasts")], Mikosch and Stărică [[2004](https://arxiv.org/html/2601.08571v1#bib.bib11 "Nonstationarities in financial time series, the long-range dependence, and the igarch effects")], Gatheral [[2011](https://arxiv.org/html/2601.08571v1#bib.bib12 "The volatility surface: a practitioner’s guide")]. In contrast, the HHT framework offers an adaptive, data-driven time-frequency representation that is sensitive to rapid changes in oscillatory amplitude. By decomposing the return series into intrinsic mode functions and applying the Hilbert Transform, HHT yields instantaneous amplitudes, frequencies, and energies (squared instantaneous amplitudes) Rai et al. [[2023](https://arxiv.org/html/2601.08571v1#bib.bib22 "Detection and forecasting of extreme events in stock price triggered by fundamental, technical, and external factors")], Mahata et al. [[2021](https://arxiv.org/html/2601.08571v1#bib.bib23 "Characteristics of 2020 stock market crash: the covid-19 induced extreme event")]. The resulting instantaneous energy captures the time-localized concentration of oscillatory activity and serves as a natural proxy for the intensity of market fluctuations. Using this instantaneous energy, we identify three market regimes – Normal, High, and Extreme.

Identifying regimes from instantaneous energy provides an initial segmentation of market states. However, this does not explain how the regimes differ internally. We therefore examine whether the identified regimes exhibit distinct volatility structure by quantifying regime-specific volatility intensity, defined as the magnitude of volatility fluctuations over time, using Holo-Hilbert Spectral Analysis (HHSA) Huang et al. [[2016](https://arxiv.org/html/2601.08571v1#bib.bib59 "On holo-hilbert spectral analysis: a full informational spectral representation for nonlinear and non-stationary data")]. HHSA extends the HHT framework by capturing amplitude-modulation dynamics across intrinsic scales. In this representation, the carrier frequency corresponds to dominant oscillatory time scales of price dynamics, while the amplitude-modulation frequency describes temporal variations in oscillation strength, reflecting volatility clustering and cross-scale feedback. The squared amplitude of the modulation component, integrated over time, yields the amplitude-modulation energy. We interpret this energy as a scale-resolved proxy for volatility intensity, enabling differentiation of regimes through their volatility signatures and providing empirical support that the regimes display distinct internal dynamics. This, in turn, strengthens the motivation for subsequently investigating intra-regime return dynamics using VLMC. While HHT has been applied in financial contexts Rai et al. [[2023](https://arxiv.org/html/2601.08571v1#bib.bib22 "Detection and forecasting of extreme events in stock price triggered by fundamental, technical, and external factors")], Mahata et al. [[2021](https://arxiv.org/html/2601.08571v1#bib.bib23 "Characteristics of 2020 stock market crash: the covid-19 induced extreme event")], the use of HHSA for regime profiling and volatility quantification remains largely unexplored in finance Chang et al. [[2022](https://arxiv.org/html/2601.08571v1#bib.bib67 "Evaluating the different stages of parkinson’s disease using electroencephalography with holo-hilbert spectral analysis")], Zheng et al. [[2023](https://arxiv.org/html/2601.08571v1#bib.bib89 "Multiscale three-dimensional holo–hilbert spectral entropy: a novel complexity-based early fault feature representation method for rotating machinery")], Lee et al. [[2022](https://arxiv.org/html/2601.08571v1#bib.bib88 "The full informational spectral analysis for auditory steady-state responses in human brain using the combination of canonical correlation analysis and holo-hilbert spectral analysis")], Ying et al. [[2024](https://arxiv.org/html/2601.08571v1#bib.bib94 "Order-frequency holo-hilbert spectral analysis for machinery fault diagnosis under time-varying operating conditions")].

Following regime identification and regime profiling, we analyze regime-specific return dynamics across developed and developing markets. We use daily return data from January 2000 to April 2025 for twenty stock market indices, comprising ten developed and ten developing economies. Returns are discretized into five categories: extreme loss (𝚁1\mathtt{R}\_{1}), mild loss (𝚁2\mathtt{R}\_{2}), no change (𝚁3\mathtt{R}\_{3}), mild gain (𝚁4\mathtt{R}\_{4}), and extreme gain (𝚁5\mathtt{R}\_{5}). VLMC is then employed to model transitions between these five states within each regime. We compare unconditional state probabilities using tail ratios and Shannon entropy, and analyze conditional transition dynamics through order-specific metrics. Self-persistence and Mean-reversion capture first-order dynamics, while Continuation, Exhaustion, Zigzag Alternation, and Burst-from-Calm capture higher-order transition behavior.

The main contributions of this paper are: First, we pioneer the application of Holo-Hilbert Spectral Analysis to finance by using amplitude-modulation energy to quantify the volatility intensity of stock market regimes. Second, we introduce Variable-length Markov chains into financial regime analysis to decode intra-regime return dynamics, and define novel metrics to quantify higher-order transition behavior. Third, we provide a comparative analysis of developed and developing markets, revealing systematic differences in regime-dependent return dynamics with implications for risk management.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2601.08571v1#S2 "2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") presents the data & return categorization and overall the methodological framework. Section [3](https://arxiv.org/html/2601.08571v1#S3 "3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") presents the empirical results. In Section [4](https://arxiv.org/html/2601.08571v1#S4 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"), we discuss the merits of our methodological framework and evaluates the robustness of the thresholds employed for regime identification. Section [5](https://arxiv.org/html/2601.08571v1#S5 "5 Conclusions ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") concludes the study.

## 2 Methodology

In this section, we describe the data and the methodological pipeline used in this study. We first introduce the stock-index data set and the construction of daily log returns. We then present the Empirical Mode Decomposition based Hilbert–Huang Transform framework used for regime identification via instantaneous energy, followed by Holo–Hilbert Spectral Analysis for profiling the identified regimes through their cross-frequency volatility signatures. Finally, we describe the regime-specific return-dynamics analysis, where returns are discretized into quintile-based states and modeled using Variable-Length Markov Chains estimated via context trees, together with the metrics used to summarize the inferred transition structure across regimes.

### 2.1 Data

We analyze daily closing prices of the standard stock market indices for twenty countries—ten developed and ten developing economies, as classified by the World Economic Situation and Prospects 2025 (United Nations) report  of Economic and DESA) [[2025](https://arxiv.org/html/2601.08571v1#bib.bib86 "World economic situation and prospects 2025")], Fantom and Serajuddin [[2016](https://arxiv.org/html/2601.08571v1#bib.bib97 "The world bank’s classification of countries by income")]. The daily data is analyzed from January 2000 to April 2025. The list of the indices can be seen from Table [1](https://arxiv.org/html/2601.08571v1#S2.T1 "Table 1 ‣ 2.1 Data ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"). All of these data are downloaded from and freely available at [Yahoo Finance](https://finance.yahoo.com/).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Developed economies | | | Developing economies | | |
| Country | Index | Ticker | Country | Index | Ticker |
| Australia | S&P/ASX 200 | AXJO | Brazil | Bovespa | BVSP |
| Belgium | BEL 20 | BFX | Indonesia | Jakarta Composite | JKSE |
| France | CAC 40 | FCHI | Argentina | MERVAL | MERV |
| United Kingdom | FTSE 100 | FTSE | Mexico | IPC | MXX |
| Germany | DAX | GDAXI | Thailand | SET | SET.BK |
| Spain | IBEX 35 | IBEX | Singapore | Straits Times | STI |
| South Korea | KOSPI | KS11 | Saudi Arabia | TASI | TASI.SR |
| Japan | Nikkei 225 | N225 | Taiwan | TAIEX | TWII |
| United States | NYSE Composite | NYA | China | SSE Composite | 000001.SS |
| Switzerland | SMI | SSMI | Hong Kong | HSI | 0388.HK |

Table 1: Stock market indices in developed and developing economies, selected for this study.

For each index, let PtP\_{t} denote the closing price on trading day tt. We compute the one-day continuously compounded return as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚛t=ln⁡(PtPt−1),\mathtt{r}\_{t}=\ln\!\left(\frac{P\_{t}}{P\_{t-1}}\right), |  | (1) |

so that the return series {𝚛t}\{\mathtt{r}\_{t}\} is defined for all trading days after the first observation.

To analyze return dynamics in a discrete state space, we discretize {𝚛t}\{\mathtt{r}\_{t}\} into five quintile-based states 𝚁1,𝚁2,𝚁3,𝚁4,𝚁5\mathtt{R}\_{1},\mathtt{R}\_{2},\mathtt{R}\_{3},\mathtt{R}\_{4},\mathtt{R}\_{5}. For each index separately, we compute the empirical quintile cutoffs q0.2,q0.4,q0.6,q0.8q\_{0.2},q\_{0.4},q\_{0.6},q\_{0.8} from the full-sample distribution of {𝚛t}\{\mathtt{r}\_{t}\} over January 2000 to April 2025. Each trading day tt is then assigned to exactly one state according to

|  |  |  |
| --- | --- | --- |
|  | 𝚁1:𝚛t≤q0.2,𝚁2:q0.2<𝚛t≤q0.4,𝚁3:q0.4<𝚛t≤q0.6,𝚁4:q0.6<𝚛t≤q0.8,𝚁5:𝚛t>q0.8.\mathtt{R}\_{1}\!:\!\mathtt{r}\_{t}\!\leq\!q\_{0.2},\quad\mathtt{R}\_{2}\!:\!q\_{0.2}\!<\!\mathtt{r}\_{t}\!\leq\!q\_{0.4},\quad\mathtt{R}\_{3}\!:\!q\_{0.4}\!<\!\mathtt{r}\_{t}\!\leq\!q\_{0.6},\quad\mathtt{R}\_{4}\!:\!q\_{0.6}\!<\!\mathtt{r}\_{t}\!\leq\!q\_{0.8},\quad\mathtt{R}\_{5}\!:\!\mathtt{r}\_{t}\!>\!q\_{0.8}. |  |

𝚁1\mathtt{R}\_{1} contains the lowest 20%20\% of returns, which correspond to the most negative outcomes in the sample, 𝚁2\mathtt{R}\_{2} contains the next 20%20\%, and so on up to 𝚁5\mathtt{R}\_{5}, which contains the highest 20%20\% of returns, corresponding to the most positive outcomes. Thus, 𝚁1\mathtt{R}\_{1} and 𝚁5\mathtt{R}\_{5} represent the lower and upper tails of the unconditional return distribution for that index, while 𝚁3\mathtt{R}\_{3} represents the central part. We use fixed full-sample quintile cutoffs for each index so that regime-specific state probabilities and transition behavior are comparable across regimes.

### 2.2 Brock - Dechert - Scheinkman test

Brock–Dechert–Scheinkman (BDS) test is a non-parametric method of testing for nonlinear patterns in time series. This test has its origins in deterministic nonlinear dynamics and chaos theory Broock et al. [[1996](https://arxiv.org/html/2601.08571v1#bib.bib56 "A test for independence based on the correlation dimension")], Grassberger and Procaccia [[1983](https://arxiv.org/html/2601.08571v1#bib.bib66 "Measuring the strangeness of strange attractors")].

The null hypothesis is that data in a time series is independently and identically distributed (iid). According to Takens Takens [[2006](https://arxiv.org/html/2601.08571v1#bib.bib65 "Detecting strange attractors in turbulence")], the method of delays can be used to embed a scalar time series {xi},i=1,2,3,…,N\{x\_{i}\},i=1,2,3,...,N into a m-dimensional space as
follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x→=i(xi,xi+t,…,xi+(m−1)​t),x→∈iℝm\vec{x}{{}\_{i}}=(x\_{i},x\_{i+t},\dots,x\_{i+(m-1)t}),\quad\vec{x}{{}\_{i}}\in\mathbb{R}^{m} |  | (2) |

where tt is the index lag.

Correlation integral measures the fractal dimension of deterministic data, i.e., the frequency with which temporal patterns are repeated in the data Grassberger and Procaccia [[1983](https://arxiv.org/html/2601.08571v1#bib.bib66 "Measuring the strangeness of strange attractors")]. The correlation integral at the embedding dimension m is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | C(m,N,r)=2M​(M−1)∑1≤i<j≤MΘ(r−∥x→−ix→∥j),r>0,C(m,N,r)=\frac{2}{M(M-1)}\sum\_{1\leq i<j\leq M}\Theta\bigl(r-\|\vec{x}{{}\_{i}}-\vec{x}{{}\_{j}}\|\bigr),\quad r>0, |  | (3) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Θ​(a)={0,a<01,a≥0.\Theta(a)=\begin{cases}0,&a<0\\ 1,&a\geq 0.\end{cases} |  | (4) |

Here, NN is the size of the data sets, M=N−(m−1)​tM=N-(m-1)t is the number of embedded points in m-dimensional space, and ∥⋅∥\|\cdot\| denotes the sup-norm. C​(m,N,r)C(m,N,r) measures the fraction of the pairs of points x→,ii=1,2,3,…,M\vec{x}{{}\_{i}},i=1,2,3,...,M, whose sup-norm separation is not greater than r. If the limit of C​(m,N,r)C(m,N,r) as N→∞N\rightarrow\infty exists for each r, we write of all state vector points that are within r of each other as C​(m,r)=limN→∞C​(m,N,r)C(m,r)=\lim\_{N\to\infty}C(m,N,r).

If the data is generated by a strictly stationary stochastic process that is absolutely regular, then this limit exists:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(m,r)=∬Θ​(r−‖x→−y→‖)​𝑑F​(x→)​𝑑F​(y→),r>0C(m,r)=\iint\Theta\bigl(r-\|\vec{x}-\vec{y}\|\bigr)\,dF(\vec{x})\,dF(\vec{y}),\quad r>0 |  | (5) |

When the process is iid, and since Θ​(r−‖x→−y→‖)=∏k=1mΘ​(r−|xk−yk|)\Theta\bigl(r-\|\vec{x}-\vec{y}\|\bigr)\ =\displaystyle\prod\_{k=1}^{m}\Theta\bigl(r-|x\_{k}-y\_{k}|\bigr), it implies that C​(m,r)=Cm​(1,r)C(m,r)=C^{m}(1,r). Also,
C​(m,r)−Cm​(1,r)C(m,r)-C^{m}(1,r) has asymptotic normal distribution, with zero mean and variance as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(m,M,r)4=m​(m−1)​C2​(m−1)​(K−C2)+Km−C2​m+2​∑i=1m−1[C2​i​(Km−i−C2​(m−i))−m​C2​(m−i)​(K−C2)]\begin{split}\frac{\sigma^{2}(m,M,r)}{4}&=m(m-1)\,C^{2(m-1)}\bigl(K-C^{2}\bigr)+K^{m}-C^{2m}\\[6.0pt] &\quad+2\sum\_{i=1}^{m-1}\Bigl[C^{2i}\bigl(K^{m-i}-C^{2(m-i)}\bigr)-m\,C^{2(m-i)}\bigl(K-C^{2}\bigr)\Bigr]\end{split} |  | (6) |

We can consistently estimate the constants C by C(1, r) and K by

|  |  |  |  |
| --- | --- | --- | --- |
|  | K(m,N,r)=6M​(M−1)​(M−2)∑1≤i<j≤M[Θ(r−∥x→−ix→∥j)Θ(r−∥x→−ix→∥j)]K(m,N,r)=\frac{6}{M(M-1)(M-2)}\sum\_{1\leq i<j\leq M}\bigl[\Theta\bigl(r-\|\vec{x}{{}\_{i}}-\vec{x}{{}\_{j}}\|\bigr)\Theta\bigl(r-\|\vec{x}{{}\_{i}}-\vec{x}{{}\_{j}}\|\bigr)\bigr] |  | (7) |

Under the (null) iid hypothesis, the BDS statistic for m>1m>1 is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | BDS​(m,N,r)=Mσ​[C​(m,r)−Cm​(1,r)]\mathrm{BDS}(m,N,r)=\frac{\sqrt{M}}{\sigma}\bigl[C(m,r)-C^{m}(1,r)\bigr] |  | (8) |

It has a limiting standard normal distribution under the null hypothesis of iid as M→∞M\rightarrow\infty and obtains the critical values using the standard normal distribution. With this test, we examine the non-linearity feature in each of the return time series. In practice, the indicator of nonlinearity is the BDS test statistic BDS​(m,N,r)\mathrm{BDS}(m,N,r), equivalently its associated pp-value, computed for selected embedding dimensions m>1m>1 and distance thresholds rr. Rejection of the iid null hypothesis, that is, statistically significant BDS​(m,N,r)\mathrm{BDS}(m,N,r) values across a range of (m,r)(m,r), is taken as evidence of nonlinear dependence in the return series.

### 2.3 Hilbert-Huang Transform and Holo-Hilbert Spectral Analysis

A non-linear time series can have both amplitude and frequency modulations generated by two different mechanisms: linear additive or nonlinear multiplicative processes Huang et al. [[2016](https://arxiv.org/html/2601.08571v1#bib.bib59 "On holo-hilbert spectral analysis: a full informational spectral representation for nonlinear and non-stationary data")]. Holo-Hilbert Spectral Analysis (HHSA) accommodates all the processes: additive and multiplicative, intra and inter-mode, stationary and nonstationary, linear and nonlinear interactions Huang et al. [[2016](https://arxiv.org/html/2601.08571v1#bib.bib59 "On holo-hilbert spectral analysis: a full informational spectral representation for nonlinear and non-stationary data")], Nguyen et al. [[2019](https://arxiv.org/html/2601.08571v1#bib.bib60 "Unraveling nonlinear electrophysiologic processes in the human visual system with full dimension spectral analysis")]. With the Holo-Hilbert spectrum (HHS), both the carrier frequencies ωc\omega\_{c} and the amplitude modulation frequencies ωa​m\omega\_{am} can be examined simultaneously, together with amplitude modulation energy.

To obtain the Hilbert spectrum from the Hilbert-Huang Transform (HHT) for regime identification and the HHS from HHSA for regime profiling, we proceed as follows. First, the original signal x​(t)x(t) is decomposed into Intrinsic Mode Functions (IMFs) cj​(t)c\_{j}(t) using Empirical Mode Decomposition (EMD), and is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | x​(t)=∑j=1ncj​(t)+qn=∑j=1naj​(t)​cos⁡θj​(t)+qn,x(t)=\sum\_{j=1}^{n}c\_{j}(t)+q\_{n}=\sum\_{j=1}^{n}a\_{j}(t)\cos\theta\_{j}(t)+q\_{n}, |  | (9) |

where {cj​(t)}\{c\_{j}(t)\} are the first-layer IMFs and qnq\_{n} is the residual. To avoid confusion in terminology, we refer to the instantaneous frequency obtained from the first-layer EMD as the carrier frequency ωc\omega\_{c}. Next, the direct quadrature (DQ) method is applied to estimate instantaneous frequencies and amplitudes of the IMFs Huang et al. [[2009](https://arxiv.org/html/2601.08571v1#bib.bib61 "On instantaneous frequency")]. This step yields the time–frequency representation of the signal, namely the Hilbert spectrum, and the squared instantaneous amplitudes provide an instantaneous energy measure.

Since the magnitude of instantaneous energy can differ across indices, we normalize the energy series before applying regime thresholds. Let I​Aj​(t)IA\_{j}(t) denote the instantaneous amplitude of the jjth IMF from HHT. We compute the raw instantaneous energy as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Eraw​(t)=∑j=1nI​Aj​(t)2,E\_{\mathrm{raw}}(t)=\sum\_{j=1}^{n}IA\_{j}(t)^{2}, |  | (10) |

and apply max-normalization,

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(t)=Eraw​(t)maxt⁡[Eraw​(t)].E(t)=\frac{E\_{\mathrm{raw}}(t)}{\max\_{t}\!\left[E\_{\mathrm{raw}}(t)\right]}. |  | (11) |

so that E​(t)∈[0,1]E(t)\in[0,1] for each index. The regime thresholds are then computed using the sample mean μ\mu and sample standard deviation σ\sigma of the normalized series {E​(t)}\{E(t)\}, and regimes are identified using cutoffs at μ+σ\mu+\sigma and μ+6​σ\mu+6\sigma.

To obtain the amplitude function of each IMF as defined by Huang et al. Huang et al. [[2009](https://arxiv.org/html/2601.08571v1#bib.bib61 "On instantaneous frequency"), [2013](https://arxiv.org/html/2601.08571v1#bib.bib64 "The uniqueness of the instantaneous frequency based on intrinsic mode function"), [2016](https://arxiv.org/html/2601.08571v1#bib.bib59 "On holo-hilbert spectral analysis: a full informational spectral representation for nonlinear and non-stationary data")], we take the absolute value of the IMF, identify the maxima of the absolute-valued IMF, and assemble the envelope by employing a natural spline through these maxima. The second-layer EMD is then obtained by applying masking EMD to the amplitude function aj​(t)a\_{j}(t), giving

|  |  |  |  |
| --- | --- | --- | --- |
|  | aj​(t)=∑k=1mcj​k​(t)+Qj​m=∑k=1maj​k​(t)​cos⁡Θj​k​(t)+Qj​m,a\_{j}(t)=\sum\_{k=1}^{m}c\_{jk}(t)+Q\_{jm}=\sum\_{k=1}^{m}a\_{jk}(t)\cos\Theta\_{jk}(t)+Q\_{jm}, |  | (12) |

where cj​k​(t)c\_{jk}(t) are the second-layer IMFs, aj​k​(t)a\_{jk}(t) are the second-layer amplitude functions, Θj​k​(t)\Theta\_{jk}(t) are the second-layer phase functions, and Qj​mQ\_{jm} are the trends of each second-layer IMF. The resulting two-layer expansion can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | x​(t)=∑j=1n[∑k=1maj​k​(t)​cos⁡Θj​k​(t)+Qj​m]​cos⁡θj​(t)+qn.x(t)=\sum\_{j=1}^{n}\Bigl[\sum\_{k=1}^{m}a\_{jk}(t)\cos\Theta\_{jk}(t)+Q\_{jm}\Bigr]\cos\theta\_{j}(t)+q\_{n}. |  | (13) |

The DQ method is again applied to these second-layer IMFs to determine the instantaneous frequency and amplitude of amplitude modulation, denoted by ωa​m\omega\_{am}. The instantaneous frequency and amplitude of this two-layer decomposition are projected to (ωa​m,ωc,t)(\omega\_{am},\omega\_{c},t) space to obtain the 3-D HHS, which characterizes cross-frequency dynamics varying with time. To aid interpretability, the 3-D HHS is integrated over time to obtain a 2-D HHS, in which the y-axis represents ωc\omega\_{c}, the x-axis represents ωa​m\omega\_{am}, and the color intensity represents the amplitude modulation energy. This energy metric is computed as the time average of the squared second-layer amplitude functions aj​k​(t)a\_{jk}(t), namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T​∫0T|aj​k​(t)|2​𝑑t,\frac{1}{T}\int\_{0}^{T}|a\_{jk}(t)|^{2}\,dt, |  | (14) |

where TT denotes the total time period.

The 2-D HHS obtained through HHSA provides a comprehensive representation of cross-frequency dynamics Huang et al. [[2016](https://arxiv.org/html/2601.08571v1#bib.bib59 "On holo-hilbert spectral analysis: a full informational spectral representation for nonlinear and non-stationary data")], Nguyen et al. [[2019](https://arxiv.org/html/2601.08571v1#bib.bib60 "Unraveling nonlinear electrophysiologic processes in the human visual system with full dimension spectral analysis")], simultaneously capturing carrier frequencies (ωc\omega\_{c}) and amplitude-modulation frequencies (ωa​m\omega\_{am}). In economic terms, ωc\omega\_{c} reflects the dominant time scale of price adjustments: higher ωc\omega\_{c} indicates faster, more frequent price movements consistent with active trading and rapid information incorporation, whereas lower ωc\omega\_{c} indicates slower, more persistent movements. The modulation frequency ωa​m\omega\_{am} describes how rapidly the strength of these price oscillations varies over time, providing a scale-resolved representation of volatility clustering and the temporal instability of risk; higher ωa​m\omega\_{am} corresponds to rapidly changing volatility intensity, while lower ωa​m\omega\_{am} corresponds to more slowly varying volatility conditions. Crucially, the amplitude-modulation energy quantifies the magnitude of volatility intensity at each (ωc,ωa​m)(\omega\_{c},\omega\_{am}) coordinate. This joint (ωc,ωa​m)(\omega\_{c},\omega\_{am}) representation, together with the associated energy, enables the profiling of market regimes through distinct and economically interpretable volatility signatures.

After the Hilbert–Huang-based regime identification and volatility-signature profiling, we turn to modeling how return categories evolve within each regime. Specifically, we use Variable-length Markov chains to capture intra-regime transition dynamics, as described next.

### 2.4 Variable-length Markov chain

Variable-length Markov chains (VLMC) are sparse high-order Markov chains. They model discrete-valued time series in which short memory is sufficient in some situations, while longer memory is needed in others. A collection of past states that determines the next-step transition probabilities is called a context Bühlmann and Wyner [[1999](https://arxiv.org/html/2601.08571v1#bib.bib49 "Variable length markov chains")], Zanin Zambom et al. [[2022](https://arxiv.org/html/2601.08571v1#bib.bib40 "Variable length markov chain with exogenous covariates")].

Let X1,X2,⋯,Xn,⋯X\_{1},X\_{2},\cdots,X\_{n},\cdots be a sequence of random variables on a finite state space SS. The sequence is a VLMC if there is a maximal order ℓmax\ell\_{\max} and a function ℓ:Sℓmax⟶{0,1,…,ℓmax}\ell:S^{\ell\_{\max}}\;\longrightarrow\;\{0,1,\dots,\ell\_{\max}\} such that for all n>ℓmaxn>\ell\_{\max},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | P(Xn=xn|Xn−1=xn−1,Xn−2=xn−2,…,X1=x1)\displaystyle P\Bigl(X\_{n}=x\_{n}\,\Bigm|\,X\_{n-1}=x\_{n-1},X\_{n-2}=x\_{n-2},\dots,X\_{1}=x\_{1}\Bigr) |  | (15) |
|  |  | =P(Xn=xn|Xn−1=xn−1,…,Xn−ℓ​(xn−ℓmax,…,xn−1)=xn−ℓ​(xn−ℓmax,…,xn−1)).\displaystyle\qquad=P\Bigl(X\_{n}=x\_{n}\,\Bigm|\,X\_{n-1}=x\_{n-1},\dots,X\_{\,n-\ell(x\_{n-\ell\_{\max}},\dots,x\_{n-1})}=x\_{\,n-\ell(x\_{n-\ell\_{\max}},\dots,x\_{n-1})}\bigr). |  |

In other words, the memory length (order) is variable and given by ℓ​(xn−ℓmax,…,xn−1)\ell(x\_{n-\ell\_{\max}},\dots,x\_{n-1}). The memory-length function generates a context function cc that retains the relevant suffix of the past needed to obtain the conditional distribution. Specifically, cc is a function from Sℓmax⟶⋃k=0ℓmaxSk\displaystyle S^{\ell\_{\max}}\longrightarrow\bigcup\_{k=0}^{\ell\_{\max}}S^{k} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(xn−ℓmax,…,xn−1)=(xn−ℓ,…,xn−1),ℓ=ℓ​(xn−ℓmax,…,xn−1).c\bigl(x\_{n-\ell\_{\max}},\dots,x\_{n-1}\bigr)=\bigl(x\_{n-\ell},\dots,x\_{n-1}\bigr),\qquad\ell=\ell(x\_{n-\ell\_{\max}},\dots,x\_{n-1}). |  | (16) |

The image by cc of SℓmaxS^{\ell\_{\max}} is the set of contexts of the VLMC, which is entirely specified by ℓ\ell, with one conditional distribution associated with each unique context Bühlmann and Wyner [[1999](https://arxiv.org/html/2601.08571v1#bib.bib49 "Variable length markov chains")], Zanin Zambom et al. [[2022](https://arxiv.org/html/2601.08571v1#bib.bib40 "Variable length markov chain with exogenous covariates")].

#### Toy example: Interpreting a VLMC context tree and the pruning rule

A VLMC is conveniently represented by a context tree. Each node is labeled by a return state, and each displayed probability vector gives the conditional distribution of the next-day state. The root node marked by ∗\ast reports unconditional probabilities P​(Xt+1=𝚁i)P(X\_{t+1}=\mathtt{R}\_{i}), i=1,…,5i=1,\dots,5. Nodes one level below the root correspond to conditioning on the most recent observation, Day−1-1. Deeper nodes add older lags. For instance, the path 𝚁5→𝚁1\mathtt{R}\_{5}\rightarrow\mathtt{R}\_{1} represents the two-day context Day−2=𝚁5-2=\mathtt{R}\_{5} followed by Day−1=𝚁1-1=\mathtt{R}\_{1}. The context length equals the number of states along the path from the root to the node, excluding the root. Hence, ℓ​(𝚁1)=1\ell(\mathtt{R}\_{1})=1 and ℓ​(𝚁5​𝚁1)=2\ell(\mathtt{R}\_{5}\mathtt{R}\_{1})=2.

To illustrate, consider the simplified toy tree below. Each node shows the next-day conditional distribution in the order (𝚁1,𝚁2,𝚁3,𝚁4,𝚁5)(\mathtt{R}\_{1},\mathtt{R}\_{2},\mathtt{R}\_{3},\mathtt{R}\_{4},\mathtt{R}\_{5}):

\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed∗\ast(0.20, 0.20, 0.20, 0.20, 0.20)𝚁1\mathtt{R}\_{1}(0.30, 0.15, 0.20, 0.10, 0.25)𝚁5\mathtt{R}\_{5}(0.48, 0.02, 0.10, 0.10, 0.30)𝚁3\mathtt{R}\_{3}(0.18, 0.22, 0.30, 0.18, 0.12)

The node labeled 𝚁1\mathtt{R}\_{1} corresponds to the one-day context c=𝚁1c=\mathtt{R}\_{1} and represents

|  |  |  |
| --- | --- | --- |
|  | P​(Xt+1=𝚁i∣Xt=𝚁1)=p​(𝚁i∣𝚁1),i=1,…,5.P(X\_{t+1}=\mathtt{R}\_{i}\mid X\_{t}=\mathtt{R}\_{1})=p(\mathtt{R}\_{i}\mid\mathtt{R}\_{1}),\qquad i=1,\dots,5. |  |

The deeper node 𝚁5\mathtt{R}\_{5} as a child of 𝚁1\mathtt{R}\_{1} corresponds to the two-day context c=𝚁5​𝚁1c=\mathtt{R}\_{5}\mathtt{R}\_{1} and represents

|  |  |  |
| --- | --- | --- |
|  | P(Xt+1=𝚁i∣Xt=𝚁1,Xt−1=𝚁5)=p(𝚁i∣𝚁5𝚁1),i=1,…,5.P(X\_{t+1}=\mathtt{R}\_{i}\mid X\_{t}=\mathtt{R}\_{1},\;X\_{t-1}=\mathtt{R}\_{5})=p(\mathtt{R}\_{i}\mid\mathtt{R}\_{5}\mathtt{R}\_{1}),\qquad i=1,\dots,5. |  |

Thus, the tree encodes variable memory: for some histories the next-day distribution depends only on Day−1-1, whereas for others a longer suffix is retained because it changes transition probabilities in a statistically meaningful way. In this study, VLMC context trees are estimated using the mixvlmc package in R Rossi et al. [[2025](https://arxiv.org/html/2601.08571v1#bib.bib85 "Mixvlmc: variable length markov chains with covariates")].

In the mixvlmc estimation procedure, deeper branches are retained only when the conditional distribution at a candidate child node differs sufficiently from that of its parent. This is enforced via a likelihood-ratio pruning rule based on Kullback–Leibler divergence. Let P^c\widehat{P}\_{c} denote the estimated next-state distribution at context cc and let P^suffix​(c)\widehat{P}\_{\mathrm{suffix}(c)} denote the distribution at the parent context given by the one-step shorter suffix. The branching decision is based on

|  |  |  |
| --- | --- | --- |
|  | Λ​(c)=2​nc​DKL​(P^c∥P^suffix​(c)),\Lambda(c)=2\,n\_{c}\,D\_{\mathrm{KL}}\!\left(\widehat{P}\_{c}\;\|\;\widehat{P}\_{\mathrm{suffix}(c)}\right), |  |

where ncn\_{c} is the number of occurrences of context cc in the data. Under standard large-sample arguments, Λ​(c)\Lambda(c) is compared to a χ2\chi^{2} cutoff with degrees of freedom |S|−1|S|-1. In our study, |S|=5|S|=5, hence the reference degrees of freedom are 44. If Λ​(c)\Lambda(c) exceeds the cutoff, the branch is retained and the longer context is kept as a distinct leaf with its own conditional distribution. If not, the branch is pruned and the child inherits the parent distribution, which controls overfitting by retaining only statistically meaningful distributional divergence. This criterion governs all branching decisions in the context trees presented in the Results section.

#### VLMC metrics

To compare regime-specific transition behavior across different effective Markov orders, we define metrics derived from the VLMC context-tree probabilities. Order-11 metrics summarize one-day persistence and paired reversals, while order-k≥2k\geq 2 metrics summarize how multi-day contexts modify continuation, tail switching, and the likelihood of extreme moves following calm sequences.

Order-1 metrics: We define two metrics.

1. Self-persistence (𝙼i\mathtt{M}\_{i}): Probability of remaining in state 𝚁i\mathtt{R}\_{i} after one step

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝙼i=pi​(𝚁i),i=1,…,5.\mathtt{M}\_{i}=p\_{i}(\mathtt{R}\_{i}),\qquad i=1,\dots,5. |  | (17) |

Higher 𝙼i\mathtt{M}\_{i} indicates short-run inertia in that return category. In particular, elevated 𝙼1\mathtt{M}\_{1} and 𝙼5\mathtt{M}\_{5} reflect clustering of tail outcomes, consistent with heightened short-horizon tail exposure and tighter risk constraints. By contrast, larger 𝙼2\mathtt{M}\_{2}–𝙼4\mathtt{M}\_{4} suggests stable conditions.

2. Reversal intensity (𝚅i\mathtt{V}\_{i}): We measure paired reversals using

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚅1=12​(p5​(𝚁1)+p1​(𝚁5)),𝚅2=12​(p4​(𝚁2)+p2​(𝚁4)).\mathtt{V}\_{1}=\frac{1}{2}\left(p\_{5}(\mathtt{R}\_{1})+p\_{1}(\mathtt{R}\_{5})\right),\qquad\mathtt{V}\_{2}=\frac{1}{2}\left(p\_{4}(\mathtt{R}\_{2})+p\_{2}(\mathtt{R}\_{4})\right). |  | (18) |

Here, 𝚅1\mathtt{V}\_{1} captures tail reversals between 𝚁1\mathtt{R}\_{1} and 𝚁5\mathtt{R}\_{5}, while 𝚅2\mathtt{V}\_{2} captures moderate reversals between 𝚁2\mathtt{R}\_{2} and 𝚁4\mathtt{R}\_{4}. Economically, larger 𝚅1\mathtt{V}\_{1} indicates stronger tail-to-tail flipping, which is a key feature of turbulent conditions and whipsaw-type corrections. A higher 𝚅2\mathtt{V}\_{2} indicates milder back-and-forth movement around typical trading conditions, consistent with progressive normalization.

Order ≥2\geq 2 metrics: We define four metrics.

1. Continuation (𝙲k\mathtt{C}\_{k}): 𝙲k\mathtt{C}\_{k} is a count-weighted average of “run continuation” probabilities over homogeneous kk-day runs.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝙲k=∑i=15(n𝚁𝚒​𝚁𝚒​…​𝚁𝚒∑c∈𝒞knc⋅pi𝚁𝚒​𝚁𝚒​…​𝚁𝚒)⋅𝕀{𝚁𝚒​𝚁𝚒​…​𝚁𝚒∈𝒞k},\mathtt{C}\_{k}=\sum\_{i=1}^{5}\left(\frac{n\_{\mathtt{R\_{i}R\_{i}\ldots R\_{i}}}}{\sum\limits\_{c\in\mathcal{C}\_{k}}n\_{c}}\cdot p\_{i}^{\mathtt{R\_{i}R\_{i}\ldots R\_{i}}}\right)\cdot\mathbb{I}\_{\{\mathtt{R\_{i}R\_{i}\ldots R\_{i}}\in\mathcal{C}\_{k}\}}, |  | (19) |

where 𝒞k\mathcal{C}\_{k} denotes all observed contexts of length kk, ncn\_{c} is the number of observations for a context c∈𝒞kc\in\mathcal{C}\_{k}, n𝚁𝚒​𝚁𝚒​…​𝚁𝚒n\_{\mathtt{R\_{i}R\_{i}\ldots R\_{i}}} is the count of the homogeneous context 𝚁𝚒​𝚁𝚒​…​𝚁𝚒\mathtt{R\_{i}R\_{i}\ldots R\_{i}}, and pi𝚁𝚒​𝚁𝚒​…​𝚁𝚒p\_{i}^{\mathtt{R\_{i}R\_{i}\ldots R\_{i}}} is the probability of 𝚁i\mathtt{R}\_{i} after that context, and 𝕀{𝚁𝚒​𝚁𝚒​…​𝚁𝚒∈𝒞k}\mathbbm{I}\_{\{\mathtt{R\_{i}R\_{i}\ldots R\_{i}}\in\mathcal{C}\_{k}\}} denotes the indicator function (1 if the context exists, 0 otherwise). Economically, high 𝙲k\mathtt{C}\_{k} indicates multi-day run persistence, which can prolong stress episodes when the run occurs in tail states. In calmer regimes, continuation primarily reflects persistence within middle states and more orderly dynamics.

2. Exhaustion (𝙴k\mathtt{E}\_{k}): 𝙴k\mathtt{E}\_{k} measures the tendency to switch between extremes after homogeneous extreme contexts.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝙴k=12​(p5𝚁𝟷​𝚁𝟷​…​𝚁𝟷+p1𝚁𝟻​𝚁𝟻​…​𝚁𝟻),\mathtt{E}\_{k}=\frac{1}{2}\left(p\_{5}^{\mathtt{R\_{1}R\_{1}\ldots R\_{1}}}+p\_{1}^{\mathtt{R\_{5}R\_{5}\ldots R\_{5}}}\right), |  | (20) |

where p5𝚁𝟷​𝚁𝟷​…​𝚁𝟷p\_{5}^{\mathtt{R\_{1}R\_{1}\ldots R\_{1}}} and p1𝚁𝟻​𝚁𝟻​…​𝚁𝟻p\_{1}^{\mathtt{R\_{5}R\_{5}\ldots R\_{5}}} are the probabilities of switching to 𝚁5\mathtt{R}\_{5} after kk consecutive 𝚁1\mathtt{R}\_{1} outcomes and to 𝚁1\mathtt{R}\_{1} after kk consecutive 𝚁5\mathtt{R}\_{5} outcomes, respectively. Large 𝙴k\mathtt{E}\_{k} indicates sharp tail-to-tail reversals following kk-day extreme runs, consistent with abrupt corrections after sustained selling or buying pressure.

3. Zigzag Alternation (𝚉k\mathtt{Z}\_{k}): The tendency to alternate between 𝚁1\mathtt{R}\_{1} and 𝚁5\mathtt{R}\_{5} over an alternating context of length kk, measured as continuation of the alternation pattern:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚉k=12​(p5𝚁𝟷​𝚁𝟻​𝚁𝟷​…+p1𝚁𝟻​𝚁𝟷​𝚁𝟻​…).\mathtt{Z}\_{k}=\frac{1}{2}\left(p\_{5}^{\mathtt{R\_{1}R\_{5}R\_{1}\ldots}}+p\_{1}^{\mathtt{R\_{5}R\_{1}R\_{5}\ldots}}\right). |  | (21) |

Here, 𝚁𝟷​𝚁𝟻​𝚁𝟷​…\mathtt{R\_{1}R\_{5}R\_{1}\ldots} denotes the length-kk alternating context that ends in 𝚁1\mathtt{R}\_{1}, so p5𝚁𝟷​𝚁𝟻​𝚁𝟷​…p\_{5}^{\mathtt{R\_{1}R\_{5}R\_{1}\ldots}} is the probability that the next state is 𝚁5\mathtt{R}\_{5} (i.e., the alternation continues). Likewise, 𝚁𝟻​𝚁𝟷​𝚁𝟻​…\mathtt{R\_{5}R\_{1}R\_{5}\ldots} denotes the length-kk alternating context that ends in 𝚁5\mathtt{R}\_{5}, so p1𝚁𝟻​𝚁𝟷​𝚁𝟻​…p\_{1}^{\mathtt{R\_{5}R\_{1}R\_{5}\ldots}} is the probability that the next state is 𝚁1\mathtt{R}\_{1}. Economically, high 𝚉k\mathtt{Z}\_{k} indicates whipsaw markets with rapid sign switching, often associated with low depth, high uncertainty, and frequent liquidity-taking.

4. Burst from Calm (𝙱k\mathtt{B}\_{k}): 𝙱k\mathtt{B}\_{k} measures burst of extreme returns 𝚁1\mathtt{R}\_{1} and 𝚁5\mathtt{R}\_{5} after calm contexts built from 𝚁2\mathtt{R}\_{2}, 𝚁3\mathtt{R}\_{3} and 𝚁4\mathtt{R}\_{4}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝙱k=∑c∈𝒞kcalm(nc∑c′∈𝒞knc′⋅(p1c+p5c)),\mathtt{B}\_{k}=\sum\_{\begin{subarray}{c}c\in\mathcal{C}\_{k}^{\text{calm}}\end{subarray}}\left(\frac{n\_{c}}{\sum\limits\_{c^{\prime}\in\mathcal{C}\_{k}}n\_{c^{\prime}}}\cdot\left(p\_{1}^{c}+p\_{5}^{c}\right)\right), |  | (22) |

where 𝒞kcalm⊂𝒞k\mathcal{C}\_{k}^{\text{calm}}\subset\mathcal{C}\_{k} denotes the calm contexts (composed exclusively of returns 𝚁2,𝚁3,𝚁4\mathtt{R}\_{2},\mathtt{R}\_{3},\mathtt{R}\_{4}) of length kk,
ncn\_{c} is the number of observations for a specific calm context c∈𝒞kcalmc\in\mathcal{C}\_{k}^{\text{calm}},
∑c′∈𝒞knc′\sum\limits\_{c^{\prime}\in\mathcal{C}\_{k}}n\_{c^{\prime}} is the total number of observations for all contexts of length kk (calm or not),
p1cp\_{1}^{c} is the probability of extreme negative return 𝚁1\mathtt{R}\_{1} occurring after context cc,
and p5cp\_{5}^{c} is the probability of extreme positive return 𝚁5\mathtt{R}\_{5} occurring after context cc. Economically, high 𝙱k\mathtt{B}\_{k} indicates that tail events can emerge directly from apparently stable conditions, consistent with latent fragility, news shocks, or sudden liquidity withdrawal.

Figure [1](https://arxiv.org/html/2601.08571v1#S2.F1 "Figure 1 ‣ VLMC metrics ‣ 2.4 Variable-length Markov chain ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") summarizes the complete methodological framework, detailing the progression from regime identification and characterization to the modeling of intra-regime return dynamics.

Regime Discovery & Characterization


Dynamics Modeling


Comparative Analysis


Daily Return Data – 2000 to 2025
(20 Indices: 10 Developed, 10 Developing)

BDS Test
(Confirm Non-linearity of Returns)

Regime Identification with HHT


•

EMD on daily returns →\to Intrinsic Mode Functions (IMFs).
•

Hilbert Transform on IMFs →\to Inst. Energy (IE).
•

Identify Extreme, High, Normal regimes via IE thresholds μ+σ\mu+\sigma & μ+6​σ\mu+6\sigma.

Regime Characterization with HHSA


•

2nd2^{\text{nd}}-layer EMD on HHT IMFs →\to 2nd2^{\text{nd}}-layer IMFs.
•

Hilbert Transform on 2nd2^{\text{nd}}-layer IMFs →\to AM Energy (AME).
•

Characterize regimes via AME as Volatility Intensity.

Return State Discretization

Discretize daily returns into quintiles – 5 states.
𝚁1\mathtt{R}\_{1} (Extreme Loss) …\dots 𝚁5\mathtt{R}\_{5} (Extreme Gain)

Variable-Length Markov Chain (VLMC)


•

Transitions between states within each regime via context trees.
•

Compare intra-regime return dynamics for developed & developing markets.

Unconditional Analysis


•

State probabilities.
•

Tail ratio.
•

Shannon entropy.

Conditional Dynamics Metrics


•

Order 1: Self-persistence, reversal intensity.
•

Order 2 & 3: Continuation, exhaustion, zigzag alternation, burst from calm.

Figure 1: Methodological flowchart illustrating the pipeline of the study: Daily returns data, checking non-linearity via BDS test, identifying and profiling market regimes via Empirical mode decomposition (EMD)-based Hilbert–Huang Transform (HHT) and Holo-Hilbert Spectral Analysis (HHSA), followed by intra-regime return dynamics modeling using Variable-Length Markov Chains (VLMC) and analysis with metrics.

## 3 Results

In this section, we present the results of our study. We begin in Subsection [3.1](https://arxiv.org/html/2601.08571v1#S3.SS1 "3.1 BDS test ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") by applying the Brock–Dechert–Scheinkman test to confirm the nonlinear nature of the return time series. We then identify three market regimes for all indices in both developed and developing markets within an Empirical Mode Decomposition-based Hilbert–Huang Transform framework. Subsection [3.2](https://arxiv.org/html/2601.08571v1#S3.SS2 "3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") uses instantaneous energy from the Hilbert spectrum to separate Normal, High, and Extreme regimes. For each one-year regime segment, it reports the corresponding Holo–Hilbert spectrum (HHS). The HHS jointly resolves carrier frequencies associated with price movements and amplitude-modulation frequencies capturing volatility fluctuations. This representation highlights regime-wise modulation-energy differences. Finally, Subsection [3.3](https://arxiv.org/html/2601.08571v1#S3.SS3 "3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") investigates regime-specific transition dynamics among discretized daily return states using a variable-length Markov chain (VLMC) approach, enabling a comparative assessment of return-state dependence across regimes and between developed and developing markets.

### 3.1 BDS test

The Brock–Dechert–Scheinkman (BDS) test is carried out to examine departures from independent and identically distributed behavior in the daily return series. Table [8](https://arxiv.org/html/2601.08571v1#A1.T8 "Table 8 ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") in the Appendix reports the BDS test statistics and corresponding pp-values for embedding dimensions m=2m=2 and m=3m=3. We focus on these low dimensions because, in finite samples, the BDS statistic becomes less stable and less powerful as mm increases due to the rapid sparsity of close pairs in higher-dimensional embeddings Broock et al. [[1996](https://arxiv.org/html/2601.08571v1#bib.bib56 "A test for independence based on the correlation dimension")], Brock et al. [[1991](https://arxiv.org/html/2601.08571v1#bib.bib58 "Nonlinear dynamics, chaos, and instability: statistical theory and economic evidence")]. Using m=2m=2 and m=3m=3 therefore provides a reliable and widely used diagnostic for nonlinear dependence while avoiding over-embedding. For the neighborhood size, we set ε=0.5​σ\varepsilon=0.5\sigma, where σ\sigma is the sample standard deviation of returns. This follows the common practice of scaling ε\varepsilon by σ\sigma so that the neighborhood is comparable across indices and remains sufficiently local to retain good power without making the correlation integral too sparse Broock et al. [[1996](https://arxiv.org/html/2601.08571v1#bib.bib56 "A test for independence based on the correlation dimension")], Hsieh [[1991](https://arxiv.org/html/2601.08571v1#bib.bib57 "Chaos and nonlinear dynamics: application to financial markets")].

For both developed and developing markets, every index is significant at the 5%5\% level at one or both embedding dimensions, with the exception of BVSP whose pp-values of 0.420.42 (m=2m=2) and 0.080.08 (m=3m=3) provide no evidence against iid behavior at ε=0.5​σ\varepsilon=0.5\sigma. Overall, daily returns for almost all indices display clear nonlinear dependence. Therefore, the subsequent analyses employ methods that accommodate nonlinear features in return dynamics.

### 3.2 Regime identification and profiling

Accommodating the non-linear feature of the return time-series of the indices, Empirical mode decomposition-based Hilbert–Huang Transform (HHT) and Holo-Hilbert Spectral Analysis (HHSA) are used in this study for regime identification and profiling the identified regimes, respectively.

![Refer to caption](x1.png)


Figure 2: Regime classification for the NYSE Composite index NYA. Panel (a) shows the daily log-returns of the closing price. Panel (b) shows the 2D Hilbert spectrum from the Hilbert–Huang Transform, with carrier frequency on the vertical axis and time on the horizontal axis, and color indicating amplitude. Panel (c) shows the normalized instantaneous energy E​(t)E(t) computed from the instantaneous amplitudes associated with the Hilbert spectrum. Points are color-coded using energy thresholds, with green denoting Normal for E​(t)≤μ+σE(t)\leq\mu+\sigma, orange denoting High for μ+σ<E​(t)≤μ+6​σ\mu+\sigma<E(t)\leq\mu+6\sigma, and red denoting Extreme for E​(t)>μ+6​σE(t)>\mu+6\sigma. Dashed horizontal lines mark μ+σ\mu+\sigma and μ+6​σ\mu+6\sigma, where μ\mu and σ\sigma are the sample mean and standard deviation of the normalized energy series.

Figures [2](https://arxiv.org/html/2601.08571v1#S3.F2 "Figure 2 ‣ 3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets")(a) – (c) show the daily log returns of the NYSE Composite Index (NYA), its Hilbert spectrum from HHT, and the corresponding instantaneous energy plot. Based on the statistical thresholds Rai et al. [[2023](https://arxiv.org/html/2601.08571v1#bib.bib22 "Detection and forecasting of extreme events in stock price triggered by fundamental, technical, and external factors")] of the instantaneous energy distribution, we classify three distinct market regimes: (a) Extreme [E​(t)>μ+6​σE(t)>\mu+6\sigma] marked by red points, (b) High [μ+σ<E​(t)≤μ+6​σ\mu+\sigma<E(t)\leq\mu+6\sigma] marked by orange points, and (c) Normal [E​(t)≤μ+σE(t)\leq\mu+\sigma] marked by green points. Here, E​(t)E(t) denotes the normalized instantaneous energy at time tt, and μ\mu and σ\sigma represent its sample mean and standard deviation, respectively.

For the Extreme regime, the extreme movements are concentrated within a few months of 2008 and 2020. However, we select one-year windows representative of each regime in order to capture the broader market dynamics including anticipatory moves preceding the extreme movements and aftershock effects following them Lillo and Mantegna [[2003](https://arxiv.org/html/2601.08571v1#bib.bib82 "Power-law relaxation in a complex system: omori law after a financial market crash")], Scheffer et al. [[2009](https://arxiv.org/html/2601.08571v1#bib.bib83 "Early-warning signals for critical transitions")], Rai et al. [[2022](https://arxiv.org/html/2601.08571v1#bib.bib84 "Statistical properties of the aftershocks of stock market crashes revisited: analysis based on the 1987 crash, financial-crisis-2008 and covid-19 pandemic")]. To ensure consistent analysis and comparability across all regimes, we similarly consider both the High and Normal regimes for one-year periods. Table [9](https://arxiv.org/html/2601.08571v1#A1.T9 "Table 9 ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") presents the identified one-year periods for developed market indices. For this group, the representative years consistently associated with each regime are 2008 and 2020 for Extreme, 2015 and 2022 for High, and 2005 and 2017 for Normal. Similarly, Table [10](https://arxiv.org/html/2601.08571v1#A1.T10 "Table 10 ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") displays the corresponding periods for developing markets. The common regime years are 2008 and 2020 for Extreme, 2002 and 2004 for High, and 2017 and 2023 for Normal.

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

Figure 3: Holo–Hilbert spectra (HHS) for the NYSE Composite index (NYA) over one-year windows selected to represent the three regimes identified from the instantaneous energy series in Fig. [2](https://arxiv.org/html/2601.08571v1#S3.F2 "Figure 2 ‣ 3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"): (a) Extreme regime year 2008, corresponding to the red-coded energy points, (b) High regime year 2011, corresponding to the orange-coded energy points, and (c) Normal regime year 2005, corresponding to the green-coded energy points. In each panel, the vertical axis is the carrier frequency ωc\omega\_{c} and the horizontal axis is the amplitude-modulation frequency ωa​m\omega\_{am}, while the color scale indicates amplitude-modulation energy (volatility intensity).

Figures [3](https://arxiv.org/html/2601.08571v1#S3.F3 "Figure 3 ‣ 3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets")(a) – (c) compare the Holo-Hilbert spectrum (HHS)-based volatility signatures across the three market regimes, thereby profiling each regime’s cross-frequency volatility structure, with NYA as an illustrative example. The corresponding HHS panels for BVSP are provided in the Appendix [5](https://arxiv.org/html/2601.08571v1#A1.F5 "Figure 5 ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") to illustrate the same Extreme–High–Normal contrast for a representative developing index. In each HHS, the y-axis represents the carrier frequencies (ωc\omega\_{c}), while the x-axis represents the amplitude modulation frequencies (ωa​m\omega\_{am}). The color intensity depicts the amplitude modulation energy, indicating the magnitude of volatility intensity at each (ωc,ωa​m)(\omega\_{c},\omega\_{am}) coordinate. From these HHS, we observed that the volatility intensity sharply decreases from Extreme to High to Normal regimes. Due to this sharp decrease, the energies and corresponding (ωc\omega\_{c}, ωa​m\omega\_{am}) pairs are not clearly visible in the High and Normal regimes. To enable meaningful cross-market comparison, we profile each regime numerically using peak amplitude modulation energy (PAME) values and the 95th95^{\text{th}} percentile carrier and amplitude-modulation frequencies (ωc\omega\_{c}, ωa​m\omega\_{am}), presented numerically in Tables [2](https://arxiv.org/html/2601.08571v1#S3.T2 "Table 2 ‣ 3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") and [3](https://arxiv.org/html/2601.08571v1#S3.T3 "Table 3 ‣ 3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") for developed and developing markets respectively.

Table 2: Peakamplitude modulation energy (PAME, ×10−5\times 10^{-5}), 95th95^{\text{th}}-percentile carrier frequency (ωc\omega\_{c}) and 95th95^{\text{th}}-percentile amplitude-modulated frequency (ωa​m\omega\_{am})—for developed-market indices under Extreme, High and Normal regimes.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Index | Extreme | | | High | | | Normal | | |
| PAME | ωc\omega\_{c} | ωa​m\omega\_{am} | PAME | ωc\omega\_{c} | ωa​m\omega\_{am} | PAME | ωc\omega\_{c} | ωa​m\omega\_{am} |
| AXJO | 2.343 | 0.221 | 0.108 | 0.746 | 0.202 | 0.104 | 0.189 | 0.243 | 0.106 |
| BFX | 3.838 | 0.235 | 0.077 | 1.187 | 0.209 | 0.094 | 0.246 | 0.254 | 0.082 |
| FCHI | 4.171 | 0.222 | 0.103 | 1.155 | 0.220 | 0.113 | 0.225 | 0.231 | 0.109 |
| FTSE | 3.274 | 0.194 | 0.120 | 0.607 | 0.251 | 0.125 | 0.178 | 0.224 | 0.120 |
| GDAXI | 4.988 | 0.230 | 0.125 | 1.280 | 0.221 | 0.122 | 0.309 | 0.239 | 0.116 |
| IBEX | 5.504 | 0.228 | 0.105 | 1.230 | 0.202 | 0.101 | 0.401 | 0.234 | 0.108 |
| KS11 | 6.264 | 0.211 | 0.065 | 0.937 | 0.220 | 0.074 | 0.675 | 0.226 | 0.080 |
| N225 | 7.599 | 0.249 | 0.115 | 1.448 | 0.256 | 0.127 | 0.715 | 0.208 | 0.119 |
| NYA | 7.218 | 0.308 | 0.115 | 1.003 | 0.194 | 0.118 | 0.130 | 0.246 | 0.127 |
| SSMI | 3.662 | 0.167 | 0.127 | 1.060 | 0.251 | 0.132 | 0.166 | 0.230 | 0.128 |
| Average | 4.886 | 0.227 | 0.106 | 1.065 | 0.223 | 0.111 | 0.324 | 0.234 | 0.110 |

Table [2](https://arxiv.org/html/2601.08571v1#S3.T2 "Table 2 ‣ 3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") highlights a sharp reduction in modulation energy for developed markets as they shift from Extreme to Normal regimes. The average PAME\mathrm{PAME} plummets from 4.89×10−54.89\times 10^{-5} in the Extreme regime to just 0.32×10−50.32\times 10^{-5} in the Normal regime, accompanied by only modest shifts in ωc\omega\_{c} and ωa​m\omega\_{am}. In contrast, Table [3](https://arxiv.org/html/2601.08571v1#S3.T3 "Table 3 ‣ 3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") indicates a smoother decline for developing markets. Here, the PAME\mathrm{PAME} decreases from 4.08×10−54.08\times 10^{-5} in the Extreme to 0.61×10−50.61\times 10^{-5} in the Normal. Notably, while the energy drops in both cases, developing markets maintain a significantly higher baseline energy in the Normal regime compared to developed markets.

Table 3: Peak amplitude modulation energy (PAME, ×10−5\times 10^{-5}), 95th95^{\text{th}}-percentile carrier frequency (ωc\omega\_{c}) and 95th95^{\text{th}}-percentile amplitude-modulated frequency (ωa​m\omega\_{am})—for developing-market indices under Extreme, High and Normal regimes.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Index | Extreme | | | High | | | Normal | | |
| PAME | ωc\omega\_{c} | ωa​m\omega\_{am} | PAME | ωc\omega\_{c} | ωa​m\omega\_{am} | PAME | ωc\omega\_{c} | ωa​m\omega\_{am} |
| BVSP | 9.393 | 0.234 | 0.110 | 2.150 | 0.233 | 0.104 | 1.155 | 0.255 | 0.103 |
| JKSE | 3.115 | 0.259 | 0.102 | 1.010 | 0.256 | 0.115 | 0.312 | 0.231 | 0.111 |
| MERV | 4.873 | 0.208 | 0.148 | 1.790 | 0.210 | 0.147 | 1.303 | 0.199 | 0.139 |
| MXX | 6.011 | 0.208 | 0.064 | 1.800 | 0.208 | 0.054 | 0.498 | 0.223 | 0.068 |
| SET.BK | 7.492 | 0.185 | 0.081 | 0.991 | 0.238 | 0.096 | 0.232 | 0.203 | 0.081 |
| STI | 2.873 | 0.211 | 0.065 | 0.901 | 0.198 | 0.077 | 0.190 | 0.211 | 0.059 |
| TASI.SR | 0.009 | 0.109 | 0.273 | 0.001 | 0.183 | 0.263 | 0.001 | 0.025 | 0.266 |
| TWII | 1.835 | 0.233 | 0.088 | 1.710 | 0.216 | 0.081 | 0.272 | 0.244 | 0.080 |
| 000001.SS | 1.061 | 0.220 | 0.155 | 0.422 | 0.206 | 0.165 | 0.085 | 0.252 | 0.167 |
| 0388.HK | 4.157 | 0.232 | 0.123 | 1.990 | 0.249 | 0.122 | 2.029 | 0.227 | 0.122 |
| Average | 4.082 | 0.210 | 0.121 | 1.276 | 0.220 | 0.122 | 0.608 | 0.207 | 0.120 |

Interpreting these numerical profiles, we observe that while both market types show reduced volatility intensity as measured by amplitude modulation energy moving from Extreme to Normal regimes, the contrast is significantly more pronounced in developed markets. The spectral parameters – (ωc\omega\_{c}), and (ωa​m\omega\_{am}) further highlight fundamental structural differences. In developed markets, price movements are fastest in the Normal regime while volatility fluctuations are slowest, a pattern consistent with deeper liquidity and more efficient price discovery in stable periods. In contrast, developing markets exhibit their fastest price movements in the High regime with persistently faster volatility fluctuations across all regimes, suggesting a greater sensitivity to external shocks that transmit volatility more readily. Even in Normal regimes, developing markets maintain substantially higher baseline PAME\mathrm{PAME}, i.e. more frequent volatility fluctuations than developed markets. These variations – price dynamics (ωc\omega\_{c}) and volatility behavior (ωa​m\omega\_{am}), along with volatility intensity (PAME\mathrm{PAME}) – point to divergent regime-dependent dynamics that are strongly conditioned by market maturity, whether a market is developed or developing.

### 3.3 Regime-dependent return dynamics

Following HHT-based regime identification, HHSA-based profiling reveals distinct volatility signatures across Extreme, High, and Normal regimes, establishing clear regime dependence in the underlying return environment. We now examine how this regime dependence is reflected in the day-to-day evolution of returns by studying intra-regime transition dynamics. To analyze these dynamics, we first categorize daily index returns into quintiles 𝚁1,𝚁2,𝚁3,𝚁4​and​𝚁5\mathtt{R}\_{1},\mathtt{R}\_{2},\mathtt{R}\_{3},\mathtt{R}\_{4}\hskip 2.0pt\text{and}\hskip 2.0pt\mathtt{R}\_{5} based on their magnitude – where 𝚁1\mathtt{R}\_{1} represents the lowest 20% of returns and 𝚁5\mathtt{R}\_{5} the highest. With these quintiles as the discrete states, we model regime-specific return transitions using the Variable-length Markov Chain (VLMC) framework and the associated metrics defined in Section [2.4](https://arxiv.org/html/2601.08571v1#S2.SS4.SSSx2 "VLMC metrics ‣ 2.4 Variable-length Markov chain ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").

\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed \* (0.395, 0.091, 0.087, 0.138, 0.289)𝚁1\mathtt{R}\_{1}(0.350, 0.080, 0.120, 0.120, 0.330)𝚁5\mathtt{R}\_{5}(0.483, 0, 0.069, 0.103, 0.345)𝚁4\mathtt{R}\_{4}(0.400, 0.143, 0.086, 0.086, 0.286)𝚁3\mathtt{R}\_{3}(0.200, 0.200, 0.400, 0.200, 0)𝚁5\mathtt{R}\_{5}(0.403, 0.125, 0.056, 0.139, 0.278)𝚁1\mathtt{R}\_{1}(0.364, 0.121, 0, 0.182, 0.333)𝚁2\mathtt{R}\_{2}(0, 0.667, 0, 0, 0.333)𝚁3\mathtt{R}\_{3}(0, 0, 0.333, 0.667, 0)
UnconditionalProbability1-Day prior1/2-Days prior1/2/3-Days prior

Figure 4: Extreme (2008) regime context tree for NYSE Composite (NYA) index. The root node (\*) with a rectangular box in bold border shows unconditional probabilities of 𝚁1,𝚁2,𝚁3,𝚁4​and​𝚁5\mathtt{R}\_{1},\mathtt{R}\_{2},\mathtt{R}\_{3},\mathtt{R}\_{4}\hskip 2.0pt\text{and}\hskip 2.0pt\mathtt{R}\_{5}. First-level nodes represent conditioning on the most recent day (Day−1-1). Deeper nodes represent longer context sequences by adding older lags (Day−2-2, Day−3-3, etc.); e.g., the child node 𝚁5\mathtt{R}\_{5} under 𝚁1\mathtt{R}\_{1} corresponds to the two-day context [Day−2=𝚁5-2=\mathtt{R}\_{5}] and [Day−1=𝚁1-1=\mathtt{R}\_{1}].

Figure [4](https://arxiv.org/html/2601.08571v1#S3.F4 "Figure 4 ‣ 3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") displays the context tree for the NYSE Composite (NYA) index during the Extreme regime (2008). The topmost node marked with ∗\ast and enclosed in a rectangular box represents the unconditional probabilities of return states, explicitly labeled on the left side. Below this root level, subsequent tiers capture conditional probabilities at increasing orders kk. Throughout, contexts are written from older to newer states. At k=1k=1, nodes summarize one-day conditioning on the most recent state. The 𝚁1\mathtt{R}\_{1} node represents the transition probabilities conditioned solely on the most recent state being 𝚁1\mathtt{R}\_{1}. This gives the conditional distribution:

|  |  |  |
| --- | --- | --- |
|  | P​(next state∣𝚁1)={𝚁1:35.00%𝚁2:8.00%𝚁3:12.00%𝚁4:12.00%𝚁5:33.00%\displaystyle P(\text{next state}\mid\mathtt{R}\_{1})=\begin{cases}\mathtt{R}\_{1}:&35.00\%\\ \mathtt{R}\_{2}:&8.00\%\\ \mathtt{R}\_{3}:&12.00\%\\ \mathtt{R}\_{4}:&12.00\%\\ \mathtt{R}\_{5}:&33.00\%\end{cases} |  |

This indicates that after an 𝚁1\mathtt{R}\_{1} day, returns most commonly persist in 𝚁1\mathtt{R}\_{1} (35%) or jump to 𝚁5\mathtt{R}\_{5} (33%). At k=2k=2, nodes represent two-day contexts. The 𝚁5\mathtt{R}\_{5} child node under 𝚁1\mathtt{R}\_{1} corresponds to the two-day context 𝚁5​𝚁1\mathtt{R}\_{5}\mathtt{R}\_{1}. This yields a fundamentally different transition distribution compared to the one-day context 𝚁1\mathtt{R}\_{1}:

|  |  |  |
| --- | --- | --- |
|  | P​(next∣𝚁5​𝚁1)={𝚁1:48.28%𝚁2:0.00%𝚁3:6.90%𝚁4:10.34%𝚁5:34.48%\displaystyle P(\text{next}\mid\mathtt{R}\_{5}\mathtt{R}\_{1})=\begin{cases}\mathtt{R}\_{1}:&48.28\%\\ \mathtt{R}\_{2}:&0.00\%\\ \mathtt{R}\_{3}:&6.90\%\\ \mathtt{R}\_{4}:&10.34\%\\ \mathtt{R}\_{5}:&34.48\%\end{cases} |  |

Notably, the probability of reverting back to 𝚁1\mathtt{R}\_{1} increases from 35.0% to 48.3%, and transitions to 𝚁2\mathtt{R}\_{2} become impossible, dropping from 8.0% to 0%. Deeper branches in Fig. [4](https://arxiv.org/html/2601.08571v1#S3.F4 "Figure 4 ‣ 3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") correspond to additional two-day and three-day contexts retained by the estimation procedure. In the context tree estimation, we set the likelihood ratio cutoff to 3.372 (corresponding to the 0.15 quantile of the χ2\chi^{2} distribution) to retain only context branches exhibiting statistically significant distributional divergence. This ensures that we capture only meaningful dynamics while preventing overfitting by pruning insignificant branches. For example, the distinct context 𝚁5​𝚁1\mathtt{R}\_{5}\mathtt{R}\_{1} exists exclusively because its log-likelihood ratio statistic, 2​nseq​DKL​(P^𝚁5​𝚁1∥P^𝚁1)2\,n\_{\text{seq}}\,D\_{\mathrm{KL}}\!\bigl(\widehat{P}\_{\mathtt{R}\_{5}\mathtt{R}\_{1}}\;\|\;\widehat{P}\_{\mathtt{R}\_{1}}\bigr), exceeds ϵχ2=3.372\epsilon\_{\chi^{2}}=3.372, confirming its power to provide statistically significant new information about next-day distributions. On the other hand, contexts sharing the same suffix 𝚁1\mathtt{R}\_{1} but not exceeding this threshold remain unbranched and inherit their transition distributions directly from the 𝚁1\mathtt{R}\_{1} node. This likelihood ratio criterion uniformly governs all branching decisions: every node in the tree represents a sequence where transition probabilities diverge significantly from its parent context.

To generalize context patterns, we aggregate all contexts across stock indices, retaining only those with frequency >2>2 and computing their averaged conditional probabilities. Table [4](https://arxiv.org/html/2601.08571v1#S3.T4 "Table 4 ‣ 3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") shows these aggregated contexts during the Extreme regime, for developed stock market indices.

Table 4: Contexts with Count >2>2 for developed stock market indices during Extreme regimes.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Context | Count | Probability to after (State) | | | | |
| P(𝚁1)(\mathtt{R}\_{1}) | P(𝚁2)(\mathtt{R}\_{2}) | P(𝚁3)(\mathtt{R}\_{3}) | P(𝚁4)(\mathtt{R}\_{4}) | P(𝚁5)(\mathtt{R}\_{5}) |
| 𝚁1\mathtt{R}\_{1} | 18 | 0.303 | 0.117 | 0.108 | 0.135 | 0.338 |
| 𝚁1​𝚁1\mathtt{R}\_{1}\mathtt{R}\_{1} | 6 | 0.307 | 0.115 | 0.106 | 0.065 | 0.407 |
| 𝚁1​𝚁1​𝚁1\mathtt{R}\_{1}\mathtt{R}\_{1}\mathtt{R}\_{1} | 4 | 0.128 | 0.257 | 0.130 | 0.130 | 0.355 |
| 𝚁1​𝚁3\mathtt{R}\_{1}\mathtt{R}\_{3} | 3 | 0.185 | 0.201 | 0.245 | 0.160 | 0.209 |
| 𝚁1​𝚁4\mathtt{R}\_{1}\mathtt{R}\_{4} | 3 | 0.161 | 0.138 | 0.199 | 0.088 | 0.414 |
| 𝚁1​𝚁5\mathtt{R}\_{1}\mathtt{R}\_{5} | 9 | 0.368 | 0.073 | 0.061 | 0.108 | 0.391 |
| 𝚁1​𝚁5​𝚁4\mathtt{R}\_{1}\mathtt{R}\_{5}\mathtt{R}\_{4} | 3 | 0.063 | 0.167 | 0.188 | 0.417 | 0.167 |
| 𝚁2\mathtt{R}\_{2} | 12 | 0.284 | 0.174 | 0.135 | 0.165 | 0.242 |
| 𝚁2​𝚁1\mathtt{R}\_{2}\mathtt{R}\_{1} | 4 | 0.588 | 0.067 | 0.092 | 0.148 | 0.104 |
| 𝚁2​𝚁2\mathtt{R}\_{2}\mathtt{R}\_{2} | 4 | 0.520 | 0.088 | 0.073 | 0.257 | 0.061 |
| 𝚁2​𝚁3\mathtt{R}\_{2}\mathtt{R}\_{3} | 4 | 0.177 | 0.377 | 0.070 | 0.176 | 0.200 |
| 𝚁2​𝚁4\mathtt{R}\_{2}\mathtt{R}\_{4} | 4 | 0.084 | 0.117 | 0.285 | 0.415 | 0.100 |
| 𝚁3\mathtt{R}\_{3} | 12 | 0.285 | 0.186 | 0.147 | 0.165 | 0.216 |
| 𝚁3​𝚁1\mathtt{R}\_{3}\mathtt{R}\_{1} | 4 | 0.451 | 0.057 | 0.099 | 0.179 | 0.214 |
| 𝚁3​𝚁2\mathtt{R}\_{3}\mathtt{R}\_{2} | 4 | 0.175 | 0.163 | 0.192 | 0.229 | 0.242 |
| 𝚁3​𝚁3\mathtt{R}\_{3}\mathtt{R}\_{3} | 6 | 0.150 | 0.114 | 0.313 | 0.087 | 0.336 |
| 𝚁4\mathtt{R}\_{4} | 13 | 0.321 | 0.232 | 0.126 | 0.115 | 0.206 |
| 𝚁4​𝚁1\mathtt{R}\_{4}\mathtt{R}\_{1} | 4 | 0.510 | 0.178 | 0.026 | 0.144 | 0.143 |
| 𝚁5\mathtt{R}\_{5} | 13 | 0.319 | 0.172 | 0.111 | 0.136 | 0.262 |
| 𝚁5​𝚁1\mathtt{R}\_{5}\mathtt{R}\_{1} | 6 | 0.329 | 0.145 | 0.091 | 0.079 | 0.356 |
| 𝚁5​𝚁2\mathtt{R}\_{5}\mathtt{R}\_{2} | 5 | 0.273 | 0.383 | 0.105 | 0.154 | 0.086 |
| 𝚁5​𝚁3\mathtt{R}\_{5}\mathtt{R}\_{3} | 3 | 0.143 | 0.125 | 0.280 | 0.167 | 0.286 |
| 𝚁5​𝚁5\mathtt{R}\_{5}\mathtt{R}\_{5} | 4 | 0.351 | 0.190 | 0.112 | 0.121 | 0.225 |
| 𝚁5​𝚁5​𝚁4\mathtt{R}\_{5}\mathtt{R}\_{5}\mathtt{R}\_{4} | 3 | 0.000 | 0.317 | 0.000 | 0.583 | 0.100 |

As a comparison reference for the Extreme-regime context tree, analogous NYA context trees for the High (2022) and Normal (2005) regimes are reported in Figs. [6](https://arxiv.org/html/2601.08571v1#A1.F6 "Figure 6 ‣ Sensitivity analysis of regime thresholds ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") and [7](https://arxiv.org/html/2601.08571v1#A1.F7 "Figure 7 ‣ Sensitivity analysis of regime thresholds ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") in the Appendix. The corresponding aggregated context tables for developed stock market indices are provided in Tables [12](https://arxiv.org/html/2601.08571v1#A1.T12 "Table 12 ‣ Sensitivity analysis of regime thresholds ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") and [12](https://arxiv.org/html/2601.08571v1#A1.T12 "Table 12 ‣ Sensitivity analysis of regime thresholds ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"). For developing stock market indices, the aggregated context tables for the Extreme, High, and Normal regimes are reported in Tables [15](https://arxiv.org/html/2601.08571v1#A1.T15 "Table 15 ‣ Sensitivity analysis of regime thresholds ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"), [15](https://arxiv.org/html/2601.08571v1#A1.T15 "Table 15 ‣ Sensitivity analysis of regime thresholds ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"), and [15](https://arxiv.org/html/2601.08571v1#A1.T15 "Table 15 ‣ Sensitivity analysis of regime thresholds ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"), respectively, in the Appendix.

We compare the unconditional probabilities of 𝚁1,𝚁2,𝚁3,𝚁4​and​𝚁5\mathtt{R}\_{1},\mathtt{R}\_{2},\mathtt{R}\_{3},\mathtt{R}\_{4}\hskip 2.0pt\text{and}\hskip 2.0pt\mathtt{R}\_{5}, the tail ratio
  
(P​(𝚁1)+P​(𝚁5)P​(𝚁2)+P​(𝚁3)+P​(𝚁4))\Bigg(\displaystyle\frac{P(\mathtt{R}\_{1})+P(\mathtt{R}\_{5})}{P(\mathtt{R}\_{2})+P(\mathtt{R}\_{3})+P(\mathtt{R}\_{4})}\Bigg), and Shannon entropy (−∑iP​(𝚁i)​log2⁡P​(𝚁i))\Big(\displaystyle-\sum\_{i}P(\mathtt{R}\_{i})\log\_{2}P(\mathtt{R}\_{i})\Big) across regimes, as shown in Table [5](https://arxiv.org/html/2601.08571v1#S3.T5 "Table 5 ‣ 3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"). In Extreme regimes, both markets show elevated tail risks. For developed markets, 𝚁1=31.15%\mathtt{R}\_{1}=31.15\% and 𝚁5=27.13%\mathtt{R}\_{5}=27.13\%, while for developing markets, 𝚁1=29.91%\mathtt{R}\_{1}=29.91\% and 𝚁5=23.99%\mathtt{R}\_{5}=23.99\%. These are accompanied by suppressed middle states. In developed markets, 𝚁2=15.91%\mathtt{R}\_{2}=15.91\%, 𝚁3=12.14%\mathtt{R}\_{3}=12.14\%, and 𝚁4=13.67%\mathtt{R}\_{4}=13.67\%, while in developing markets, 𝚁2=16.84%\mathtt{R}\_{2}=16.84\%, 𝚁3=14.22%\mathtt{R}\_{3}=14.22\%, and 𝚁4=15.02%\mathtt{R}\_{4}=15.02\%. This indicates high susceptibility to large price swings. This tail risk decreases as the regime changes from Extreme to High to then Normal, signaling market stability where extreme outcomes become less frequent.

Across both markets, left-tail risk 𝚁1\mathtt{R}\_{1} consistently exceeds right-tail risk 𝚁5\mathtt{R}\_{5}, signaling a persistent downside-risk asymmetry. The magnitude of that asymmetry, however, varies by regime. In Extreme regimes, developing markets show greater downside risk, with a 5.92% spread compared to 4.02% in developed markets, suggesting that panic-driven accelerated sell-offs are more prevalent in developing economies, in line with earlier findings Li and Rose [[2009](https://arxiv.org/html/2601.08571v1#bib.bib105 "The tail risk of emerging stock markets")], Pereda [[2025](https://arxiv.org/html/2601.08571v1#bib.bib104 "Systemic risk and default cascades in global equity markets: extending the gai-kapadia framework with stochastic simulations and network analysis")]. In Normal regimes too, the asymmetry remains pronounced, with a 2.33% spread compared to 0.15% in developed markets. This may indicate the fragmented nature of developing markets where there are information delays and liquidity constraints, leading to amplification of negative shocks even when volatility is low, as documented in Lesmond [[2005](https://arxiv.org/html/2601.08571v1#bib.bib68 "Liquidity of emerging markets")]. However, the pattern reverses in High regimes. Developed markets show the greater spread, at 5.30% versus 2.86% in developing markets. One likely reason for this is that institutional investors hedge heavily, and their protective trades can add extra downside risk, as documented empirically in these studies Garleanu et al. [[2008](https://arxiv.org/html/2601.08571v1#bib.bib53 "Demand-based option pricing")], Coval and Stafford [[2007](https://arxiv.org/html/2601.08571v1#bib.bib54 "Asset fire sales (and purchases) in equity markets")].

The tail ratio also decreases sharply from Extreme to Normal regimes in both markets, but the attenuation is more pronounced in developed markets, falling from 1.3969 to 0.2552, an 81.7% decrease, than in developing markets, falling from 1.1697 to 0.3457, a 70.5% decrease. Developing markets exhibit a 35% higher tail ratio during Normal periods, quantifying their persistent tail risk exposure. Entropy peaks in High regimes, with 2.3071 in developed markets and 2.3059 in developing markets, indicating maximum unpredictability during High regimes, and declines in Extreme and Normal regimes. Thus, Extreme regimes concentrate tail risks, High regimes maximize uncertainty, and Normal regimes minimize extremes, with developing markets demonstrating systematically higher residual tail risk.

Table 5: Unconditional Probabilities with Tail Ratio and Shannon Entropy

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Market | Regime | Unconditional probabilities | | | | | Tail ratio | Shannon  entropy |
| P(𝚁1\mathtt{R}\_{1}) | P(𝚁2\mathtt{R}\_{2}) | P(𝚁3\mathtt{R}\_{3}) | P(𝚁4\mathtt{R}\_{4}) | P(𝚁5\mathtt{R}\_{5}) |
| Developed | Extreme | 0.312 | 0.159 | 0.121 | 0.137 | 0.271 | 1.397 | 2.219 |
| High | 0.251 | 0.198 | 0.162 | 0.191 | 0.198 | 0.816 | 2.307 |
| Normal | 0.102 | 0.283 | 0.278 | 0.235 | 0.101 | 0.255 | 2.191 |
| Developing | Extreme | 0.299 | 0.168 | 0.142 | 0.150 | 0.240 | 1.170 | 2.259 |
| High | 0.248 | 0.192 | 0.174 | 0.167 | 0.219 | 0.877 | 2.306 |
| Normal | 0.140 | 0.251 | 0.276 | 0.217 | 0.117 | 0.346 | 2.250 |

Following the unconditional probability analysis, we examine conditional probabilities at different orders kk. For k=1k=1, where the next return depends only on the most recent return state, we summarize the context-tree transitions using two metrics defined in Section [2.4](https://arxiv.org/html/2601.08571v1#S2.SS4.SSSx2 "VLMC metrics ‣ 2.4 Variable-length Markov chain ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"): self-persistence 𝙼\mathtt{M}, capturing one-step repetition 𝚁i→𝚁i\mathtt{R}\_{i}\to\mathtt{R}\_{i}, and reversal intensity 𝚅\mathtt{V}, capturing paired flips. Table [6](https://arxiv.org/html/2601.08571v1#S3.T6 "Table 6 ‣ 3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") reports these k=1k=1 metrics across regimes and markets.

In developed markets, tail persistence peaks in the Extreme regime, with 𝙼1=0.303\mathtt{M}\_{1}=0.303 and 𝙼5=0.263\mathtt{M}\_{5}=0.263, and then declines through High to Normal, where 𝙼1=0.278\mathtt{M}\_{1}=0.278 and 𝙼5=0.202\mathtt{M}\_{5}=0.202 in High and 𝙼1=0.182\mathtt{M}\_{1}=0.182 and 𝙼5=0.105\mathtt{M}\_{5}=0.105 in Normal. Mid-range persistence across 𝙼2\mathtt{M}\_{2}–𝙼4\mathtt{M}\_{4} rises sharply, most notably 𝙼3\mathtt{M}\_{3}, which increases from 0.1470.147 in Extreme to 0.2700.270 in Normal. The same stabilization pattern is also observed in developing markets as regimes transition from Extreme to High to Normal. However, developing markets show higher downside persistence across all regimes, with 𝙼1=0.336\mathtt{M}\_{1}=0.336 in Extreme, 𝙼1=0.295\mathtt{M}\_{1}=0.295 in High, and 𝙼1=0.254\mathtt{M}\_{1}=0.254 in Normal, each exceeding the corresponding developed-market values. This confirms chronic downside stickiness, in which negative states persist longer in developing markets.

For reversal intensity, developed markets show the strongest tail-to-tail flipping in the Extreme regime, with 𝚅1=0.329\mathtt{V}\_{1}=0.329, which then declines through High to Normal, where 𝚅1=0.232\mathtt{V}\_{1}=0.232 in High and 𝚅1=0.106\mathtt{V}\_{1}=0.106 in Normal. In contrast, moderate reversals strengthen as regimes stabilize, with 𝚅2=0.199\mathtt{V}\_{2}=0.199 in Extreme, 𝚅2=0.214\mathtt{V}\_{2}=0.214 in High, and 𝚅2=0.283\mathtt{V}\_{2}=0.283 in Normal. Developing markets exhibit the same qualitative pattern but with distinct magnitudes. In the Extreme regime, tail flips are weaker in developing markets, with 𝚅1=0.267\mathtt{V}\_{1}=0.267 versus 0.3290.329 in developed markets, indicating that large tail-to-tail corrections occur less frequently in extremely volatile periods for developing indices. In Normal regimes, the pattern reverses: developing markets show stronger tail reversals, with 𝚅1=0.132\mathtt{V}\_{1}=0.132 versus 0.1060.106, consistent with greater sensitivity to liquidity frictions and information asymmetry prevalent in developing economies.

Overall, the k=1k=1 patterns indicate progressive stabilization from Extreme to Normal regimes in both markets. However, developing markets exhibit persistent downside stickiness, with higher downside persistence across all regimes, indicating more prolonged vulnerability to negative shocks. They also show asymmetric tail reversals: tail-to-tail flipping is weaker in Extreme regimes yet comparatively stronger in Normal regimes, relative to developed markets. This reflects structural weaknesses such as thinner liquidity and information delays in developing markets. Market participants must therefore recognize these vulnerabilities and strategies should be adapted accordingly — expect slower price reversals during extreme volatility periods, prepare for extended downturns requiring greater patience, and tailor risk management to address persistent negative states.

Table 6: Context‐tree metrics for order k=1k=1.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Market | Regime | Self‐persistence (𝙼\mathtt{M}) | | | | | Reversal intensity (𝚅\mathtt{V}) | |
| 𝙼1\mathtt{M}\_{1} | 𝙼2\mathtt{M}\_{2} | 𝙼3\mathtt{M}\_{3} | 𝙼4\mathtt{M}\_{4} | 𝙼5\mathtt{M}\_{5} | 𝚅1\mathtt{V}\_{1} | 𝚅2\mathtt{V}\_{2} |
| Developed | Extreme | 0.303 | 0.174 | 0.147 | 0.115 | 0.263 | 0.329 | 0.199 |
| High | 0.278 | 0.170 | 0.177 | 0.185 | 0.202 | 0.232 | 0.214 |
| Normal | 0.182 | 0.260 | 0.270 | 0.210 | 0.105 | 0.106 | 0.283 |
| Developing | Extreme | 0.336 | 0.188 | 0.168 | 0.171 | 0.253 | 0.267 | 0.182 |
| High | 0.295 | 0.185 | 0.156 | 0.179 | 0.225 | 0.230 | 0.176 |
| Normal | 0.254 | 0.242 | 0.281 | 0.180 | 0.145 | 0.132 | 0.267 |

Extending the conditional analysis beyond k=1k=1, we examine higher-order dependence at k=2k=2 and k=3k=3, where the next return state depends on the previous two or three states. Table [7](https://arxiv.org/html/2601.08571v1#S3.T7 "Table 7 ‣ 3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets") reports the corresponding context-tree metrics defined in Section [2.4](https://arxiv.org/html/2601.08571v1#S2.SS4.SSSx2 "VLMC metrics ‣ 2.4 Variable-length Markov chain ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"): Continuation (𝙲k\mathtt{C}\_{k}), Exhaustion (𝙴k\mathtt{E}\_{k}), Zigzag alternation 𝚉k\mathtt{Z}\_{k}, and Burst-from-calm (𝙱k\mathtt{B}\_{k}).

For k=2k=2 in developed markets, continuation is highest in the Extreme regime with 𝙲2=0.063\mathtt{C}\_{2}=0.063, drops in the High regime to 𝙲2=0.033\mathtt{C}\_{2}=0.033, and rebounds in the Normal regime to 𝙲2=0.058\mathtt{C}\_{2}=0.058. This pattern indicates that two-day runs are most persistent under stress, weaken during High regimes, and partially re-emerge in Normal conditions, which may suggest restored confidence where orderly price discovery allows trend-following behavior to regain momentum. Exhaustion declines with stabilization, from 𝙴2=0.379\mathtt{E}\_{2}=0.379 in the Extreme regime to 𝙴2=0.271\mathtt{E}\_{2}=0.271 in the Normal regime, consistent with fewer sharp tail-to-tail corrections outside the most turbulent periods. In other words, the abrupt reversals associated with panic-driven sell-offs and subsequent rebound buying become less dominant as markets stabilize. Zigzag alternation also drops strongly, from 𝚉2=0.362\mathtt{Z}\_{2}=0.362 in the Extreme regime to 𝚉2=0.100\mathtt{Z}\_{2}=0.100 in the Normal regime, showing that tail-to-tail whipsaw dynamics become substantially less pronounced as volatility conditions normalize. In contrast, burst-from-calm strengthens outside Extreme regimes, with 𝙱2=0.117\mathtt{B}\_{2}=0.117 in the Extreme regime and 𝙱2=0.140\mathtt{B}\_{2}=0.140 in the Normal regime, indicating that tail moves can still arise from calm sequences even when overall volatility is low.

Developing markets exhibit both similarities to, and clear departures from, developed markets at k=2k=2. In common with developed markets, continuation is weakest in the High regime, with 𝙲2=0.031\mathtt{C}\_{2}=0.031, and burst-from-calm is larger outside the Extreme regime, rising from 𝙱2=0.106\mathtt{B}\_{2}=0.106 in the Extreme regime to 𝙱2=0.142\mathtt{B}\_{2}=0.142 in the Normal regime. These patterns indicate that, in both developed and developing markets, two-day run continuation weakens in the intermediate High regime and tail events can still emerge from calm sequences as regimes move toward Normal conditions. The differences are most apparent in the Normal regime. Continuation becomes substantially stronger in developing markets, with 𝙲2=0.110\mathtt{C}\_{2}=0.110 versus 0.0580.058 in developed markets, indicating more pronounced two-day run persistence even under minimal-volatility conditions. Exhaustion is also markedly higher, with 𝙴2=0.401\mathtt{E}\_{2}=0.401 versus 0.2710.271 in developed markets, suggesting that tail-to-tail switching after extreme runs remains more prevalent in developing markets during stable periods, consistent with shallower liquidity conditions. Zigzag alternation likewise remains elevated, with 𝚉2=0.225\mathtt{Z}\_{2}=0.225 in the Normal regime compared with 0.1000.100 in developed markets, pointing to more persistent tail switching and noisier short-horizon dynamics. Overall, these contrasts indicate that developing markets retain stronger higher-order tail dependence and greater residual fragility even when regimes are classified as Normal.

Table 7: Context‐tree metrics for order k=2,3k=2,3.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Market | Regime | k=2k=2 | | | | k=3k=3 | | | |
| 𝙲2\mathtt{C}\_{2} | 𝙴2\mathtt{E}\_{2} | 𝚉2\mathtt{Z}\_{2} | 𝙱2\mathtt{B}\_{2} | 𝙲3\mathtt{C}\_{3} | 𝙴3\mathtt{E}\_{3} | 𝚉3\mathtt{Z}\_{3} | 𝙱3\mathtt{B}\_{3} |
| Developed | Extreme | 0.063 | 0.379 | 0.362 | 0.117 | 0.018 | 0.490 | 0.233 | ≪0.001\ll 0.001 |
| High | 0.033 | 0.250 | 0.296 | 0.139 | ≪0.001\ll 0.001 | ≪0.001\ll 0.001 | 0.083 | ≪0.001\ll 0.001 |
| Normal | 0.058 | 0.271 | 0.100 | 0.140 | ≪0.001\ll 0.001 | ≪0.001\ll 0.001 | ≪0.001\ll 0.001 | 0.259 |
| Developing | Extreme | 0.072 | 0.275 | 0.298 | 0.106 | 0.008 | 0.250 | 0.125 | 0.060 |
| High | 0.031 | 0.285 | 0.212 | 0.079 | ≪0.001\ll 0.001 | 0.196 | ≪0.001\ll 0.001 | 0.029 |
| Normal | 0.110 | 0.401 | 0.225 | 0.142 | 0.033 | 0.250 | ≪0.001\ll 0.001 | 0.124 |

For k=3k=3, developed markets show three-day dependence primarily in the Extreme regime. Continuation is detectable with 𝙲3=0.018\mathtt{C}\_{3}=0.018, and exhaustion is elevated with 𝙴3=0.490\mathtt{E}\_{3}=0.490, while zigzag alternation remains sizeable with 𝚉3=0.233\mathtt{Z}\_{3}=0.233. Together, these results indicate that three-day patterns are most evident under stress, where multi-day sequences can persist and then flip sharply. In the High regime, three-day dependence largely vanishes, with only a modest zigzag signal 𝚉3=0.083\mathtt{Z}\_{3}=0.083. In the Normal regime, continuation and tail switching are negligible, yet burst-from-calm becomes dominant with 𝙱3=0.259\mathtt{B}\_{3}=0.259, indicating that long calm sequences can still mask the risk of a sudden extreme move.

Developing markets retain more three-day structure. In the Extreme regime, 𝙲3=0.008\mathtt{C}\_{3}=0.008, 𝙴3=0.250\mathtt{E}\_{3}=0.250, 𝚉3=0.125\mathtt{Z}\_{3}=0.125, and 𝙱3=0.060\mathtt{B}\_{3}=0.060 are all present, mirroring the qualitative profile of developed markets but at lower magnitudes. In the High regime, exhaustion remains detectable with 𝙴3=0.196\mathtt{E}\_{3}=0.196 and burst-from-calm persists with 𝙱3=0.029\mathtt{B}\_{3}=0.029, indicating that higher-order tail switching does not fully disappear. In the Normal regime, continuation reappears with 𝙲3=0.033\mathtt{C}\_{3}=0.033, exhaustion remains at 𝙴3=0.250\mathtt{E}\_{3}=0.250, and burst-from-calm rises to 𝙱3=0.124\mathtt{B}\_{3}=0.124, implying that multi-day persistence and tail switching can coexist with non-negligible burst risk even under minimal-volatility conditions. Overall, relative to developed markets, developing markets exhibit more persistent higher-order dependence and a stronger tendency for tail-related dynamics to remain active in Normal regimes.

## 4 Discussion

Financial market conditions are rarely uniform over time. Periods of routine trading with moderate fluctuations alternate with episodes of heightened stress marked by sharp price swings. Classical regime frameworks describe this alternation as shifts between low-volatility and high-volatility or calm and stressed market states Hamilton [[1989](https://arxiv.org/html/2601.08571v1#bib.bib69 "A new approach to the economic analysis of nonstationary time series and the business cycle")], Ang and Timmermann [[2012](https://arxiv.org/html/2601.08571v1#bib.bib2 "Regime changes and financial markets")], Guidolin and Timmermann [[2007](https://arxiv.org/html/2601.08571v1#bib.bib16 "Asset allocation under multivariate regime switching")]. This alternation motivates the need for an indicator that can detect regime shifts reliably in financial data. Standard volatility measures, including rolling standard deviations and GARCH-type conditional variances, provide useful summaries of volatility levels Engle [[1982](https://arxiv.org/html/2601.08571v1#bib.bib111 "Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation")], Bollerslev [[1986](https://arxiv.org/html/2601.08571v1#bib.bib112 "Generalized autoregressive conditional heteroskedasticity")]. However, they are backward-looking by construction. As a result, they can adjust slowly when volatility changes abruptly. Structural breaks may then appear as spurious persistence in GARCH dynamics Lamoureux and Lastrapes [[1990](https://arxiv.org/html/2601.08571v1#bib.bib108 "Persistence in variance, structural change, and the garch model")]. Predictive performance can also deteriorate when the data-generating process shifts sharply during crises Hillebrand and Medeiros [[2010](https://arxiv.org/html/2601.08571v1#bib.bib55 "The benefits of bagging for forecast models of realized volatility")].

To address these limitations, we operationalize regime identification using instantaneous energy from the Hilbert–Huang Transform. In addition, GARCH-based indicators require parametric specifications for volatility evolution and innovation distributions, whereas the HHT-based energy measure is obtained through a data-driven decomposition and remains informative when volatility is shaped by liquidity stress and feedback mechanisms Brunnermeier [[2009](https://arxiv.org/html/2601.08571v1#bib.bib109 "Deciphering the liquidity and credit crunch 2007–2008")], Shleifer and Vishny [[2011](https://arxiv.org/html/2601.08571v1#bib.bib110 "Fire sales in finance and macroeconomics")]. We use thresholds at μ+σ\mu+\sigma and μ+6​σ\mu+6\sigma, where μ\mu and σ\sigma denote the mean and standard deviation of instantaneous energy. The μ+σ\mu+\sigma cutoff marks sustained departures from baseline energy levels and separates calm conditions from periods of elevated volatility, while μ+6​σ\mu+6\sigma is deliberately conservative and isolates only the most extreme energy realizations. When E​(t)>μ+6​σE(t)>\mu+6\sigma, oscillatory activity becomes sharply amplified across intrinsic time scales, consistent with severe stress dynamics such as liquidity withdrawal, widening bid–ask spreads, forced liquidations, and adverse feedback loops Brunnermeier [[2009](https://arxiv.org/html/2601.08571v1#bib.bib109 "Deciphering the liquidity and credit crunch 2007–2008")], Shleifer and Vishny [[2011](https://arxiv.org/html/2601.08571v1#bib.bib110 "Fire sales in finance and macroeconomics")]. These cutoffs act as scale-normalized separators in a heavy-tailed financial system rather than Gaussian tail-probability statements Cont [[2001](https://arxiv.org/html/2601.08571v1#bib.bib113 "Empirical properties of asset returns: stylized facts and statistical issues")], Embrechts et al. [[2013](https://arxiv.org/html/2601.08571v1#bib.bib107 "Modelling extremal events: for insurance and finance")]. The resulting regimes align with classical interpretations. Normal corresponds to low-volatility liquid conditions. High corresponds to sustained elevated volatility in functioning markets. Extreme corresponds to rare stress episodes with severe dislocations. Robustness is assessed via sensitivity analysis under alternative threshold specifications, as detailed in [A](https://arxiv.org/html/2601.08571v1#A1.SSx1 "Sensitivity analysis of regime thresholds ‣ Appendix A Appendix ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"). The findings of the sensitivity analysis reported in Figshare at [10.6084/m9.figshare.30982552](https://doi.org/10.6084/m9.figshare.30982552) show that qualitative conclusions are unchanged under reasonable variations.

Beyond regime detection, HHSA is introduced to complement the HHT-based segmentation and to justify the subsequent VLMC analysis by providing an independent, scale-resolved description of within-regime volatility organization. While instantaneous energy identifies when markets enter higher-activity states, it does not describe how volatility is structured across time scales inside each state. HHSA addresses this by resolving cross-frequency dynamics and extracting carrier frequencies ωc\omega\_{c} and amplitude-modulation frequencies ωa​m\omega\_{am} Huang et al. [[2016](https://arxiv.org/html/2601.08571v1#bib.bib59 "On holo-hilbert spectral analysis: a full informational spectral representation for nonlinear and non-stationary data")], Nguyen et al. [[2019](https://arxiv.org/html/2601.08571v1#bib.bib60 "Unraveling nonlinear electrophysiologic processes in the human visual system with full dimension spectral analysis")]. This regime-level volatility profiling provides empirical evidence that the regimes identified by instantaneous energy differ not only in level but also in internal volatility structure. Consistent with this interpretation, amplitude-modulation energy declines by a factor of 1515 from Extreme to Normal regimes in developed markets, compared to ≈7\approx 7-fold in developing markets, indicating systematic differences in how markets dissipate stress across regimes. Taken together, HHT provides a time-localized basis for regime segmentation, HHSA quantifies within-regime volatility structure, and VLMC is then applied to examine how return-category transitions evolve conditionally on these empirically distinct regimes.

## 5 Conclusions

Financial markets exhibit abrupt transitions between tranquil and stressed periods, and return dynamics can change across such regimes. Identifying these regimes and quantifying how return dynamics differ across them is important for risk management and portfolio allocation, especially when tail events cluster and volatility conditions vary by market maturity. This study examines regime-dependent return dynamics in developed and developing equity indices by combining Hilbert–Huang based regime identification and profiling with a Variable-Length Markov Chain analysis of categorized returns.

Market regimes are first identified using Empirical Mode Decomposition based Hilbert–Huang Transform. Following regime identification, we profile each regime using Holo–Hilbert Spectral Analysis. The profiles show systematic regime-dependent shifts in price dynamics and volatility behavior that differ fundamentally between developed and developing markets, thus providing empirical support for examining return-state transitions separately within each regime. To examine regime-dependent return dynamics, daily index returns are categorized into discrete states and analyzed using variable-length Markov chains. The unconditional probabilities reveal that while the prevalence of extreme returns recedes as regimes stabilize, a persistent downside asymmetry remains across all regimes. The reduction in extreme outcomes is significantly more pronounced in developed markets. In contrast, developing markets retain persistent tail exposure even under minimal-volatility conditions. Furthermore, market unpredictability is observed to peak during moderate volatility periods. Conditional transition dynamics indicate progressive stabilization from Extreme to Normal regimes in both markets, though developing markets retain clear downside persistence. Reversal intensity is observed to be regime-dependent, characterized by weaker tail-to-tail transitions in Extreme regimes and stronger tail reversals in Normal regimes. Higher-order dependence further differentiates the two market groups. Developed markets exhibit a pronounced reduction in tail alternation as regimes normalize, consistent with the efficient dissipation of whipsaw-type dynamics. In contrast, developing markets maintain elevated exhaustion and zigzag alternation, indicating that higher-order tail dependence remains active even under low-volatility conditions.

Overall, the findings show that regime dependence is present in both developed and developing markets, but the nature of stabilization differs materially with market maturity. Developed markets transition toward more ordered conditional dynamics and weaker tail-dependent structure as regimes normalize. Developing markets retain residual fragility, with persistent higher-order tail dynamics and non-negligible burst risk even in Normal regimes. These results imply that developing markets may require targeted safeguards and risk controls not only during crises but also during stable periods, reflecting structural frictions such as thinner liquidity and slower information incorporation. The findings are consistent with prior evidence on tail-risk asymmetries and crisis amplification, liquidity-friction effects across market maturity, and volatility–return dynamics shaped by investor demand and intermediary constraints Li and Rose [[2009](https://arxiv.org/html/2601.08571v1#bib.bib105 "The tail risk of emerging stock markets")], Pereda [[2025](https://arxiv.org/html/2601.08571v1#bib.bib104 "Systemic risk and default cascades in global equity markets: extending the gai-kapadia framework with stochastic simulations and network analysis")], Lesmond [[2005](https://arxiv.org/html/2601.08571v1#bib.bib68 "Liquidity of emerging markets")], Garleanu et al. [[2008](https://arxiv.org/html/2601.08571v1#bib.bib53 "Demand-based option pricing")], Coval and Stafford [[2007](https://arxiv.org/html/2601.08571v1#bib.bib54 "Asset fire sales (and purchases) in equity markets")].

A limitation of the present analysis is that the estimated context trees condition only on past return states and do not incorporate observable external drivers that may influence transitions. Future work can extend this framework by incorporating exogenous drivers through covariate-dependent variable-length Markov models, allowing transition probabilities and context selection to vary with economic conditions. Suitable covariates include realized volatility and volume, liquidity proxies such as bid–ask spreads, policy and macro indicators, and global risk indicators, thereby linking regime-dependent dynamics more directly to measurable market drivers.

## Acknowledgements

The authors, S. R. Luwang, K. Mukhia, and B. N. Sharma, would like to thank the National Institute of Technology Sikkim, for allocating doctoral research fellowships.

## Data and Code Availability Statement

The data that support the findings of this study are publicly available from [Yahoo Finance](https://finance.yahoo.com/). The code used for regime identification and profiling using HHT and HHSA is provided in the form of Jupyter notebooks in Figshare at [10.6084/m9.figshare.30982552](https://doi.org/10.6084/m9.figshare.30982552). The code used for intra-regime return-dynamics analysis via VLMC context trees is also provided in Figshare at [10.6084/m9.figshare.30982552](https://doi.org/10.6084/m9.figshare.30982552) and is implemented using the mixvlmc package in R.

## References

* T. G. Andersen and T. Bollerslev (1998)
  Answering the skeptics: yes, standard volatility models do provide accurate forecasts.
  International economic review,  pp. 885–905.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p3.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* A. Ang and G. Bekaert (2007)
  Stock return predictability: is it there?.
  The Review of Financial Studies 20 (3),  pp. 651–707.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* A. Ang and A. Timmermann (2012)
  Regime changes and financial markets.
  Annu. Rev. Financ. Econ. 4 (1),  pp. 313–337.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p1.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§4](https://arxiv.org/html/2601.08571v1#S4.p1.1 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* D. Avramov and T. Chordia (2006)
  Predicting stock returns.
  Journal of Financial Economics 82 (2),  pp. 387–415.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* A. BenSaïda (2015)
  The frequency of regime switching in financial market volatility.
  Journal of Empirical Finance 32,  pp. 63–79.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p1.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* T. Bollerslev (1986)
  Generalized autoregressive conditional heteroskedasticity.
  Journal of econometrics 31 (3),  pp. 307–327.
  Cited by: [§4](https://arxiv.org/html/2601.08571v1#S4.p1.1 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* W. A. Brock, D. A. Hsieh, and B. D. LeBaron (1991)
  Nonlinear dynamics, chaos, and instability: statistical theory and economic evidence.
   MIT press.
  Cited by: [§3.1](https://arxiv.org/html/2601.08571v1#S3.SS1.p1.10 "3.1 BDS test ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* W. A. Broock, J. A. Scheinkman, W. D. Dechert, and B. LeBaron (1996)
  A test for independence based on the correlation dimension.
  Econometric reviews 15 (3),  pp. 197–235.
  Cited by: [§2.2](https://arxiv.org/html/2601.08571v1#S2.SS2.p1.1 "2.2 Brock - Dechert - Scheinkman test ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§3.1](https://arxiv.org/html/2601.08571v1#S3.SS1.p1.10 "3.1 BDS test ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* M. K. Brunnermeier (2009)
  Deciphering the liquidity and credit crunch 2007–2008.
  Journal of Economic perspectives 23 (1),  pp. 77–100.
  Cited by: [§4](https://arxiv.org/html/2601.08571v1#S4.p2.7 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* P. Bühlmann and A. J. Wyner (1999)
  Variable length markov chains.
  The Annals of Statistics 27 (2),  pp. 480–513.
  Cited by: [§2.4](https://arxiv.org/html/2601.08571v1#S2.SS4.p1.1 "2.4 Variable-length Markov chain ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§2.4](https://arxiv.org/html/2601.08571v1#S2.SS4.p5.3 "2.4 Variable-length Markov chain ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* K. Chang (2009)
  Do macroeconomic variables have regime-dependent effects on stock return dynamics? evidence from the markov regime switching model.
  Economic Modelling 26 (6),  pp. 1283–1299.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* K. Chang, I. T. French, W. Liang, Y. Lo, Y. Wang, M. Cheng, N. E. Huang, H. Wu, S. Lim, C. Chen, et al. (2022)
  Evaluating the different stages of parkinson’s disease using electroencephalography with holo-hilbert spectral analysis.
  Frontiers in aging neuroscience 14,  pp. 832637.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p4.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* R. Cont (2001)
  Empirical properties of asset returns: stylized facts and statistical issues.
  Quantitative finance 1 (2),  pp. 223.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p3.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§4](https://arxiv.org/html/2601.08571v1#S4.p2.7 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* J. Coval and E. Stafford (2007)
  Asset fire sales (and purchases) in equity markets.
  Journal of Financial Economics 86 (2),  pp. 479–512.
  Cited by: [§3.3](https://arxiv.org/html/2601.08571v1#S3.SS3.p8.2 "3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§5](https://arxiv.org/html/2601.08571v1#S5.p3.1 "5 Conclusions ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* G. D’Amico, A. Lika, and F. Petroni (2019)
  Change point dynamics for financial data: an indexed markov chain approach.
  Annals of Finance 15 (2),  pp. 247–266.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* G. D’Amico and F. Petroni (2011)
  A semi-markov model with memory for price changes.
  Journal of statistical mechanics: Theory and experiment 2011 (12),  pp. P12009.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* G. D’Amico and F. Petroni (2012)
  Weighted-indexed semi-markov models for modeling financial returns.
  Journal of statistical mechanics: theory and experiment 2012 (07),  pp. P07015.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* G. D’Amico and F. Petroni (2018)
  Copula based multivariate semi-markov models with applications in high-frequency finance.
  European Journal of Operational Research 267 (2),  pp. 765–777.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* P. Embrechts, C. Klüppelberg, and T. Mikosch (2013)
  Modelling extremal events: for insurance and finance.
  Vol. 33, Springer Science & Business Media.
  Cited by: [§4](https://arxiv.org/html/2601.08571v1#S4.p2.7 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* R. F. Engle and A. J. Patton (2007)
  What good is a volatility model?.
  In Forecasting volatility in the financial markets,
   pp. 47–63.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p3.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* R. F. Engle (1982)
  Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation.
  Econometrica: Journal of the econometric society,  pp. 987–1007.
  Cited by: [§4](https://arxiv.org/html/2601.08571v1#S4.p1.1 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* R. Engle (2004)
  Risk and volatility: econometric models and financial practice.
  American economic review 94 (3),  pp. 405–420.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p1.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* N. J. Fantom and U. Serajuddin (2016)
  The world bank’s classification of countries by income.
  World Bank Policy Research Working Paper (7528).
  Cited by: [§2.1](https://arxiv.org/html/2601.08571v1#S2.SS1.p1.1 "2.1 Data ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* M. J. Flannery and A. A. Protopapadakis (2002)
  Macroeconomic factors do influence aggregate stock returns.
  The review of financial studies 15 (3),  pp. 751–782.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* N. Garleanu, L. H. Pedersen, and A. M. Poteshman (2008)
  Demand-based option pricing.
  The Review of Financial Studies 22 (10),  pp. 4259–4299.
  Cited by: [§3.3](https://arxiv.org/html/2601.08571v1#S3.SS3.p8.2 "3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§5](https://arxiv.org/html/2601.08571v1#S5.p3.1 "5 Conclusions ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* J. Gatheral (2011)
  The volatility surface: a practitioner’s guide.
   John Wiley & Sons.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p3.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* P. Grassberger and I. Procaccia (1983)
  Measuring the strangeness of strange attractors.
  Physica D: nonlinear phenomena 9 (1-2),  pp. 189–208.
  Cited by: [§2.2](https://arxiv.org/html/2601.08571v1#S2.SS2.p1.1 "2.2 Brock - Dechert - Scheinkman test ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§2.2](https://arxiv.org/html/2601.08571v1#S2.SS2.p3.1 "2.2 Brock - Dechert - Scheinkman test ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* M. Guidolin and A. Timmermann (2007)
  Asset allocation under multivariate regime switching.
  Journal of Economic Dynamics and Control 31 (11),  pp. 3503–3544.
  Cited by: [§4](https://arxiv.org/html/2601.08571v1#S4.p1.1 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* J. D. Hamilton (1989)
  A new approach to the economic analysis of nonstationary time series and the business cycle.
  Econometrica: Journal of the econometric society,  pp. 357–384.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p1.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§4](https://arxiv.org/html/2601.08571v1#S4.p1.1 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* J. D. Hamilton (1990)
  Analysis of time series subject to changes in regime.
  Journal of econometrics 45 (1-2),  pp. 39–70.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p1.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* E. Hillebrand and M. C. Medeiros (2010)
  The benefits of bagging for forecast models of realized volatility.
  Econometric Reviews 29 (5-6),  pp. 571–593.
  Cited by: [§4](https://arxiv.org/html/2601.08571v1#S4.p1.1 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* D. A. Hsieh (1991)
  Chaos and nonlinear dynamics: application to financial markets.
  The journal of finance 46 (5),  pp. 1839–1877.
  Cited by: [§3.1](https://arxiv.org/html/2601.08571v1#S3.SS1.p1.10 "3.1 BDS test ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* J. Huang, W. Huang, P. Chu, W. Lee, H. Pai, C. Chuang, and Y. Wu (2017)
  Applying a markov chain for the stock pricing of a novel forecasting model.
  Communications in Statistics-theory and Methods 46 (9),  pp. 4388–4402.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* N. E. Huang, K. Hu, A. C. Yang, H. Chang, D. Jia, W. Liang, J. R. Yeh, C. Kao, C. Juan, C. K. Peng, et al. (2016)
  On holo-hilbert spectral analysis: a full informational spectral representation for nonlinear and non-stationary data.
  Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 374 (2065),  pp. 20150206.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p4.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§2.3](https://arxiv.org/html/2601.08571v1#S2.SS3.p1.2 "2.3 Hilbert-Huang Transform and Holo-Hilbert Spectral Analysis ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§2.3](https://arxiv.org/html/2601.08571v1#S2.SS3.p5.1 "2.3 Hilbert-Huang Transform and Holo-Hilbert Spectral Analysis ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§2.3](https://arxiv.org/html/2601.08571v1#S2.SS3.p7.10 "2.3 Hilbert-Huang Transform and Holo-Hilbert Spectral Analysis ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§4](https://arxiv.org/html/2601.08571v1#S4.p3.4 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* N. E. Huang, Z. Wu, S. R. Long, K. C. Arnold, X. Chen, and K. Blank (2009)
  On instantaneous frequency.
  Advances in adaptive data analysis 1 (02),  pp. 177–229.
  Cited by: [§2.3](https://arxiv.org/html/2601.08571v1#S2.SS3.p2.5 "2.3 Hilbert-Huang Transform and Holo-Hilbert Spectral Analysis ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§2.3](https://arxiv.org/html/2601.08571v1#S2.SS3.p5.1 "2.3 Hilbert-Huang Transform and Holo-Hilbert Spectral Analysis ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* N. E. Huang, V. YOUNG, M. LO, Y. H. WANG, C. Peng, X. Chen, G. Wang, J. Deng, and Z. Wu (2013)
  The uniqueness of the instantaneous frequency based on intrinsic mode function.
  Advances in adaptive data analysis 5 (03),  pp. 1350011.
  Cited by: [§2.3](https://arxiv.org/html/2601.08571v1#S2.SS3.p5.1 "2.3 Hilbert-Huang Transform and Holo-Hilbert Spectral Analysis ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* M. Kritzman, S. Page, and D. Turkington (2012)
  Regime shifts: implications for dynamic strategies (corrected).
  Financial Analysts Journal 68 (3),  pp. 22–39.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p1.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* C. G. Lamoureux and W. D. Lastrapes (1990)
  Persistence in variance, structural change, and the garch model.
  Journal of Business & Economic Statistics 8 (2),  pp. 225–234.
  Cited by: [§4](https://arxiv.org/html/2601.08571v1#S4.p1.1 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* P. Lee, T. Lee, W. Lee, N. N. Chu, Y. E. Shelepin, H. Hsu, and H. Chang (2022)
  The full informational spectral analysis for auditory steady-state responses in human brain using the combination of canonical correlation analysis and holo-hilbert spectral analysis.
  Journal of Clinical Medicine 11 (13),  pp. 3868.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p4.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* D. A. Lesmond (2005)
  Liquidity of emerging markets.
  Journal of financial economics 77 (2),  pp. 411–452.
  Cited by: [§3.3](https://arxiv.org/html/2601.08571v1#S3.SS3.p8.2 "3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§5](https://arxiv.org/html/2601.08571v1#S5.p3.1 "5 Conclusions ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* X. Li and L. C. Rose (2009)
  The tail risk of emerging stock markets.
  Emerging markets review 10 (4),  pp. 242–256.
  Cited by: [§3.3](https://arxiv.org/html/2601.08571v1#S3.SS3.p8.2 "3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§5](https://arxiv.org/html/2601.08571v1#S5.p3.1 "5 Conclusions ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* F. Lillo and R. N. Mantegna (2003)
  Power-law relaxation in a complex system: omori law after a financial market crash.
  Physical Review E 68 (1),  pp. 016119.
  Cited by: [§3.2](https://arxiv.org/html/2601.08571v1#S3.SS2.p3.1 "3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* F. M. Longin (1996)
  The asymptotic distribution of extreme stock market returns.
  Journal of business,  pp. 383–408.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p1.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* T. Lux and M. Marchesi (2000)
  Volatility clustering in financial markets: a microsimulation of interacting agents.
  International journal of theoretical and applied finance 3 (04),  pp. 675–702.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p3.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* A. Mahata, A. Rai, M. Nurujjaman, O. Prakash, and D. Prasad Bal (2021)
  Characteristics of 2020 stock market crash: the covid-19 induced extreme event.
  Chaos: An Interdisciplinary Journal of Nonlinear Science 31 (5).
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p3.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§1](https://arxiv.org/html/2601.08571v1#S1.p4.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* B. Mandelbrot et al. (1963)
  The variation of certain speculative prices.
  Journal of business 36 (4),  pp. 394.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p3.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* W. Marquering and M. Verbeek (2004)
  The economic value of predicting stock index returns and volatility.
  Journal of Financial and Quantitative Analysis 39 (2),  pp. 407–429.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* G. McQueen and S. Thorley (1991)
  Are stock returns predictable? a test using markov chains.
  The Journal of Finance 46 (1),  pp. 239–263.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* T. Mikosch and C. Stărică (2004)
  Nonstationarities in financial time series, the long-range dependence, and the igarch effects.
  Review of Economics and Statistics 86 (1),  pp. 378–390.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p3.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* K. T. Nguyen, W. Liang, V. Lee, W. Chang, N. G. Muggleton, J. Yeh, N. E. Huang, and C. Juan (2019)
  Unraveling nonlinear electrophysiologic processes in the human visual system with full dimension spectral analysis.
  Scientific reports 9 (1),  pp. 16919.
  Cited by: [§2.3](https://arxiv.org/html/2601.08571v1#S2.SS3.p1.2 "2.3 Hilbert-Huang Transform and Holo-Hilbert Spectral Analysis ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§2.3](https://arxiv.org/html/2601.08571v1#S2.SS3.p7.10 "2.3 Hilbert-Huang Transform and Holo-Hilbert Spectral Analysis ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§4](https://arxiv.org/html/2601.08571v1#S4.p3.4 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* P. Nystrup, B. W. Hansen, H. Madsen, and E. Lindström (2015)
  Regime-based versus static asset allocation: letting the data speak.
  Journal of Portfolio Management 42 (1),  pp. 103.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p1.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* U. N. D. of Economic and S. A. (. DESA) (2025)
  World economic situation and prospects 2025.
  Note: Accessed: 2025-07-01
  External Links: [Link](https://desapublications.un.org/publications/world-economic-situation-and-prospects-2025)
  Cited by: [§2.1](https://arxiv.org/html/2601.08571v1#S2.SS1.p1.1 "2.1 Data ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* A. I. Pereda (2025)
  Systemic risk and default cascades in global equity markets: extending the gai-kapadia framework with stochastic simulations and network analysis.
  arXiv preprint arXiv:2504.01969.
  Cited by: [§3.3](https://arxiv.org/html/2601.08571v1#S3.SS3.p8.2 "3.3 Regime-dependent return dynamics ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§5](https://arxiv.org/html/2601.08571v1#S5.p3.1 "5 Conclusions ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* S. Rabindrajit Luwang, A. Rai, M. Nurujjaman, O. Prakash, and C. Hens (2024)
  High-frequency stock market order transitions during the us–china trade war 2018: a discrete-time markov chain analysis.
  Chaos: An Interdisciplinary Journal of Nonlinear Science 34 (1).
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* A. Rai, S. R. Luwang, M. Nurujjaman, C. Hens, P. Kuila, and K. Debnath (2023)
  Detection and forecasting of extreme events in stock price triggered by fundamental, technical, and external factors.
  Chaos, Solitons & Fractals 173,  pp. 113716.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p3.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§1](https://arxiv.org/html/2601.08571v1#S1.p4.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§3.2](https://arxiv.org/html/2601.08571v1#S3.SS2.p2.7 "3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* A. Rai, A. Mahata, M. Nurujjaman, and O. Prakash (2022)
  Statistical properties of the aftershocks of stock market crashes revisited: analysis based on the 1987 crash, financial-crisis-2008 and covid-19 pandemic.
  International Journal of Modern Physics C 33 (02),  pp. 2250019.
  Cited by: [§3.2](https://arxiv.org/html/2601.08571v1#S3.SS2.p3.1 "3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* J. C. Reboredo (2010)
  Nonlinear effects of oil shocks on stock returns: a markov-switching approach.
  Applied Economics 42 (29),  pp. 3735–3744.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p2.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* C. Rey, S. Rey, and J. Viala (2014)
  Detection of high and low states in stock market returns with mcmc method in a markov switching model.
  Economic Modelling 41,  pp. 145–155.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p1.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* F. Rossi, H. Le Picard, and G. Joubioux (2025)
  Mixvlmc: variable length markov chains with covariates.
   CRAN.
  Note: R package Version 0.2.1.9000
  External Links: [Link](https://github.com/fabrice-rossi/mixvlmc)
  Cited by: [§2.4](https://arxiv.org/html/2601.08571v1#S2.SS4.SSSx1.p3.6 "Toy example: Interpreting a VLMC context tree and the pruning rule ‣ 2.4 Variable-length Markov chain ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* M. Scheffer, J. Bascompte, W. A. Brock, V. Brovkin, S. R. Carpenter, V. Dakos, H. Held, E. H. Van Nes, M. Rietkerk, and G. Sugihara (2009)
  Early-warning signals for critical transitions.
  Nature 461 (7260),  pp. 53–59.
  Cited by: [§3.2](https://arxiv.org/html/2601.08571v1#S3.SS2.p3.1 "3.2 Regime identification and profiling ‣ 3 Results ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* G. W. Schwert (1989)
  Why does stock market volatility change over time?.
  The journal of finance 44 (5),  pp. 1115–1153.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p3.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* A. Shleifer and R. Vishny (2011)
  Fire sales in finance and macroeconomics.
  Journal of economic perspectives 25 (1),  pp. 29–48.
  Cited by: [§4](https://arxiv.org/html/2601.08571v1#S4.p2.7 "4 Discussion ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* F. Takens (2006)
  Detecting strange attractors in turbulence.
  In Dynamical Systems and Turbulence, Warwick 1980: proceedings of a symposium held at the University of Warwick 1979/80,
   pp. 366–381.
  Cited by: [§2.2](https://arxiv.org/html/2601.08571v1#S2.SS2.p2.1 "2.2 Brock - Dechert - Scheinkman test ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* W. Ying, J. Zheng, W. Huang, J. Tong, H. Pan, and Y. Li (2024)
  Order-frequency holo-hilbert spectral analysis for machinery fault diagnosis under time-varying operating conditions.
  ISA transactions 146,  pp. 472–483.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p4.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* A. Zanin Zambom, S. Kim, and N. Lopes Garcia (2022)
  Variable length markov chain with exogenous covariates.
  Journal of Time Series Analysis 43 (2),  pp. 312–328.
  Cited by: [§2.4](https://arxiv.org/html/2601.08571v1#S2.SS4.p1.1 "2.4 Variable-length Markov chain ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets"),
  [§2.4](https://arxiv.org/html/2601.08571v1#S2.SS4.p5.3 "2.4 Variable-length Markov chain ‣ 2 Methodology ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").
* J. Zheng, W. Ying, J. Tong, and Y. Li (2023)
  Multiscale three-dimensional holo–hilbert spectral entropy: a novel complexity-based early fault feature representation method for rotating machinery.
  Nonlinear Dynamics 111 (11),  pp. 10309–10330.
  Cited by: [§1](https://arxiv.org/html/2601.08571v1#S1.p4.1 "1 Introduction ‣ Regime Discovery and Intra-Regime Return Dynamics in Global Equity Markets").

## Appendix A Appendix

Table 8: BDS test results (embedding dimensions m=2,3m=2,3; ε=0.5​σ\varepsilon=0.5\,\sigma) for developed and developing market indices. Statistics and p-values are reported separately for each dimension.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Economic  Condition | Market  Index | BDS test results (at m=2,3m=2,3; ε=0.5​σ\varepsilon=0.5\sigma) | | | |
|  |  | m = 2  Statistic | m = 2  p-value | m = 3  Statistic | m = 3  p-value |
| Developed | AXJO | 2.422 | 0.015 | 3.867 | <0.001<0.001 |
|  | BFX | 3.588 | 0.000 | 6.036 | <0.001<0.001 |
|  | FCHI | 2.674 | 0.008 | 4.896 | <0.001<0.001 |
|  | FTSE | 3.159 | 0.002 | 5.445 | <0.001<0.001 |
|  | GDAXI | 2.909 | 0.004 | 5.534 | <0.001<0.001 |
|  | IBEX | 2.558 | 0.011 | 4.752 | <0.001<0.001 |
|  | KS11 | 2.454 | 0.014 | 4.919 | <0.001<0.001 |
|  | N225 | 1.283 | 0.199 | 2.630 | <0.01<0.01 |
|  | NYA | 3.083 | 0.002 | 6.443 | <0.001<0.001 |
|  | SSMI | 2.826 | 0.005 | 4.702 | <0.001<0.001 |
| Developing | BVSP | 0.814 | 0.416 | 1.753 | 0.08 |
|  | JKSE | 2.547 | 0.011 | 4.533 | <0.001<0.001 |
|  | MERV | 2.160 | 0.031 | 4.027 | <0.001<0.001 |
|  | MXX | 2.256 | 0.024 | 3.940 | <0.001<0.001 |
|  | SET.BK | 2.548 | 0.011 | 4.865 | <0.001<0.001 |
|  | STI | 3.012 | 0.003 | 5.219 | <0.001<0.001 |
|  | TASI.SR | 2.994 | 0.003 | 5.866 | <0.001<0.001 |
|  | TWII | 1.627 | 0.104 | 3.365 | <0.001<0.001 |
|  | 000001.SS | 1.882 | 0.060 | 3.705 | <0.001<0.001 |
|  | 0388.HK | 2.956 | 0.003 | 4.920 | <0.001<0.001 |



![Refer to caption](x5.png)

![Refer to caption](x6.png)

![Refer to caption](x7.png)

Figure 5: Holo–Hilbert spectra (HHS) for the Bovespa index (BVSP) over one-year windows selected to represent the three regimes identified from the instantaneous energy series: (a) Extreme regime year 2008, corresponding to the red-coded energy points, (b) High regime year 2011, corresponding to the orange-coded energy points, and (c) Normal regime year 2005, corresponding to the green-coded energy points. In each panel, the vertical axis is the carrier frequency ωc\omega\_{c} and the horizontal axis is the amplitude-modulation frequency ωa​m\omega\_{am}, while the color scale indicates amplitude-modulation energy, used here as a measure of volatility intensity.



|  |  |  |  |
| --- | --- | --- | --- |
| Index | Regime | | |
|  | Extreme | High | Normal |
| AXJO | 2008, 2020 | 2000, 2001, 2007, 2009, 2010, 2011, 2013, 2015, 2016, 2022, 2025 | 2002, 2003, 2004, 2005, 2006, 2012, 2014, 2017, 2018, 2019, 2021, 2023, 2024 |
| BFX | 2003, 2008, 2010, 2020 | 2000, 2001, 2002, 2007, 2009, 2011, 2015, 2016, 2022, 2025 | 2004, 2005, 2006, 2012, 2013, 2014, 2017, 2018, 2019, 2021, 2023, 2024 |
| FCHI | 2002, 2008, 2009, 2010, 2020 | 2000, 2001, 2003, 2011, 2012, 2015, 2016, 2021, 2022, 2025 | 2004, 2005, 2006, 2007, 2013, 2014, 2017, 2018, 2019, 2023, 2024 |
| FTSE | 2008, 2020 | 2000, 2001, 2002, 2003, 2007, 2009, 2010, 2011, 2015, 2016, 2022, 2025 | 2004, 2005, 2006, 2012, 2013, 2014, 2017, 2018, 2019, 2021, 2023, 2024 |
| GDAXI | 2002, 2008, 2020 | 2000, 2001, 2003, 2009, 2010, 2011, 2012, 2013, 2015, 2016, 2022, 2025 | 2004, 2005, 2006, 2007, 2014, 2017, 2018, 2019, 2021, 2023, 2024 |
| IBEX | 2008, 2010, 2016, 2020 | 2000, 2001, 2002, 2003, 2009, 2011, 2012, 2015, 2022, 2023, 2025 | 2004, 2005, 2006, 2007, 2013, 2014, 2017, 2018, 2019, 2021, 2024 |
| KS11 | 2000, 2001, 2008, 2020 | 2002, 2003, 2004, 2007, 2009, 2011, 2021, 2023, 2024, 2025 | 2005, 2006, 2010, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2022 |
| N225 | 2008, 2011, 2024, 2025 | 2000, 2001, 2002, 2003, 2007, 2009, 2010, 2013, 2014, 2015, 2016, 2018, 2020, 2022 | 2004, 2005, 2006, 2012, 2017, 2019, 2021, 2023 |
| NYA | 2008, 2020 | 2000, 2001, 2002, 2007, 2009, 2010, 2011, 2015, 2016, 2018, 2022, 2025 | 2003, 2004, 2005, 2006, 2012, 2013, 2014, 2017, 2019, 2021, 2023, 2024 |
| SSMI | 2001, 2008, 2020 | 2000, 2002, 2003, 2007, 2009, 2010, 2011, 2015, 2016, 2022, 2025 | 2004, 2005, 2006, 2012, 2013, 2014, 2017, 2018, 2019, 2021, 2023, 2024 |

Table 9: Regime years for developed stock market indices.



|  |  |  |  |
| --- | --- | --- | --- |
| Index | Regime | | |
|  | Extreme | High | Normal |
| 000001.SS | 2001, 2007, 2008, 2015 | 2000, 2002, 2003, 2004, 2005, 2006, 2009, 2010, 2012, 2013, 2014, 2016, 2018, 2019, 2020, 2022, 2024, 2025 | 2011, 2017, 2021, 2023 |
| 0388.HK | 2001, 2007, 2008, 2015, 2024 | 2000, 2002, 2003, 2004, 2006, 2009, 2010, 2011, 2012, 2014, 2016, 2018, 2020, 2021, 2022, 2025 | 2005, 2013, 2017, 2019, 2023 |
| BVSP | 2008, 2020 | 2000, 2001, 2002, 2004, 2006, 2007, 2009, 2011, 2014, 2016, 2017, 2021 | 2003, 2005, 2010, 2012, 2013, 2015, 2018, 2019, 2022, 2023, 2024, 2025 |
| JKSE | 2002, 2004, 2006, 2007, 2008, 2011, 2020, 2025 | 2000, 2001, 2003, 2005, 2009, 2010, 2012, 2013, 2015, 2018, 2022 | 2014, 2016, 2017, 2019, 2021, 2023, 2024 |
| MERV | 2019 | 2001, 2002, 2004, 2008, 2011, 2014, 2018, 2020, 2023, 2024, 2025 | 2000, 2003, 2005, 2006, 2007, 2009, 2010, 2012, 2013, 2015, 2016, 2017, 2021, 2022 |
| MXX | 2000, 2008 | 2001, 2002, 2004, 2006, 2007, 2009, 2011, 2016, 2018, 2020, 2024, 2025 | 2003, 2005, 2010, 2012, 2013, 2014, 2015, 2017, 2019, 2021, 2022, 2023 |
| SET.BK | 2006, 2008, 2020 | 2000, 2001, 2002, 2004, 2007, 2009, 2010, 2011, 2013, 2015, 2016, 2025 | 2003, 2005, 2012, 2014, 2017, 2018, 2019, 2021, 2022, 2023, 2024 |
| STI | 2000, 2008, 2020 | 2001, 2002, 2003, 2006, 2007, 2009, 2010, 2011, 2015, 2016, 2018, 2024, 2025 | 2004, 2005, 2012, 2013, 2014, 2017, 2019, 2021, 2022, 2023 |
| TASI.SR | 2006, 2008, 2015 | 2003, 2004, 2005, 2007, 2009, 2010, 2011, 2014, 2018, 2020, 2025 | 2000, 2001, 2002, 2012, 2013, 2016, 2017, 2019, 2021, 2022, 2023, 2024 |
| TWII | 2000, 2008, 2009, 2020, 2024, 2025 | 2001, 2002, 2003, 2004, 2006, 2007, 2010, 2011, 2015, 2016, 2018, 2021, 2022 | 2005, 2012, 2013, 2014, 2017, 2019, 2023 |

Table 10: Regime years for developing stock market indices.

### Sensitivity analysis of regime thresholds

Regime identification in this study is based on thresholding the normalized instantaneous energy series E​(t)E(t) obtained from the Hilbert–Huang Transform. The baseline specification classifies observations using two cutoffs,

|  |  |  |
| --- | --- | --- |
|  | τ1=μ+σ,τ2=μ+6​σ,\tau\_{1}=\mu+\sigma,\qquad\tau\_{2}=\mu+6\sigma, |  |

where μ\mu and σ\sigma denote the sample mean and standard deviation of E​(t)E(t), respectively. Observations are assigned to Normal, High, and Extreme regimes according to

|  |  |  |
| --- | --- | --- |
|  | Normal: ​E​(t)≤τ1,High: ​τ1<E​(t)≤τ2,Extreme: ​E​(t)>τ2.\text{Normal: }E(t)\leq\tau\_{1},\qquad\text{High: }\tau\_{1}<E(t)\leq\tau\_{2},\qquad\text{Extreme: }E(t)>\tau\_{2}. |  |

To assess robustness to threshold choice, we perform a grid-based sensitivity analysis by perturbing both cutoffs via multiplicative factors aa and bb:

|  |  |  |
| --- | --- | --- |
|  | τ1​(a)=μ+a​σ,τ2​(b)=μ+b​σ,\tau\_{1}(a)=\mu+a\sigma,\qquad\tau\_{2}(b)=\mu+b\sigma, |  |

and re-running the regime assignment for each (a,b)(a,b) pair in the grid

|  |  |  |
| --- | --- | --- |
|  | a∈{0.75, 1.00, 1.25},b∈{4.5, 6.0, 7.5},b>a.a\in\{0.75,\,1.00,\,1.25\},\qquad b\in\{4.5,\,6.0,\,7.5\},\qquad b>a. |  |

This design retains the baseline case (a,b)=(1,6)(a,b)=(1,6) while spanning both a less conservative and a more conservative separation of regimes. For each index and each (a,b)(a,b) pair, daily observations are first classified into regimes by τ1​(a)\tau\_{1}(a) and τ2​(b)\tau\_{2}(b). The corresponding regime years are then defined as the set of calendar years that contain at least one day assigned to that regime. To ensure that each year belongs to only one regime for a given index, overlaps are removed by a severity rule: if a year is flagged as Extreme, it is excluded from High and Normal; if a year is flagged as High, it is excluded from Normal.

Sensitivity is evaluated separately for developed and developing market panels. For each (a,b)(a,b) configuration and regime, we compute the intersection of regime-year sets across indices within a panel. When the intersection is empty for a regime, we report a fallback set consisting of the two most frequently occurring regime years across indices in that panel. Robustness is then assessed by comparing the regime-year sets obtained under each (a,b)(a,b) configuration to those under the baseline thresholds. We summarize similarity using set-overlap measures such as the Jaccard similarity, and by verifying that the qualitative ordering of regimes is preserved, namely that Extreme years remain concentrated in crisis episodes, High years correspond to sustained elevated volatility periods, and Normal years correspond to comparatively tranquil conditions. Detailed results of the sensitivity analysis are available on Figshare at [10.6084/m9.figshare.30982552](https://doi.org/10.6084/m9.figshare.30982552). Consistency of these conclusions across the threshold grid supports the stability of the regime identification procedure.

\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed \* (0.347, 0.171, 0.080, 0.143, 0.259)𝚁1\mathtt{R}\_{1}(0.391, 0.253, 0.092, 0.092, 0.172)𝚁1\mathtt{R}\_{1}(0.441, 0.265, 0.088, 0.030, 0.177)𝚁5\mathtt{R}\_{5}(0.5, 0, 0, 0, 0.5)𝚁2\mathtt{R}\_{2}(0.310, 0.024, 0.024, 0.238, 0.405)𝚁4\mathtt{R}\_{4}(0.306, 0.139, 0.139, 0.139, 0.278)𝚁4\mathtt{R}\_{4}(0.8, 0, 0, 0, 0.2)𝚁5\mathtt{R}\_{5}(0.323, 0.185, 0.077, 0.154, 0.262)𝚁2\mathtt{R}\_{2}(0.235, 0.177, 0.059, 0.294, 0.235)𝚁1\mathtt{R}\_{1}(0.333, 0.25, 0, 0.167, 0.25)𝚁2\mathtt{R}\_{2}(0, 0, 0, 0, 1)𝚁4\mathtt{R}\_{4}(0.4, 0.4, 0.1, 0.1, 0)𝚁5\mathtt{R}\_{5}(0.353, 0.118, 0.059, 0.059, 0.412)𝚁2\mathtt{R}\_{2}(0, 0, 0, 0, 1.0)
UnconditionalProbability1-Day prior1/2-Days prior1/2/3-Days prior1/2/3/4-Days prior

Figure 6: High (2022) regime context tree for NYSE Composite (NYA) index. The root node (\*) a the bold square border shows unconditional probabilities of 𝚁1,𝚁2,𝚁3,𝚁4​and​𝚁5\mathtt{R}\_{1},\mathtt{R}\_{2},\mathtt{R}\_{3},\mathtt{R}\_{4}\hskip 2.0pt\text{and}\hskip 2.0pt\mathtt{R}\_{5}.



\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed\pgfqpointtransformed \* (0.183, 0.234, 0.202, 0.258, 0.123)𝚁1\mathtt{R}\_{1}(0.217, 0.174, 0.217, 0.217, 0.174)𝚁3\mathtt{R}\_{3}(0.143, 0.143, 0.143, 0.286, 0.286)𝚁2\mathtt{R}\_{2}(0, 0.4, 0, 0.6, 0)𝚁2\mathtt{R}\_{2}(0.138, 0.138, 0.345, 0.224, 0.155)𝚁5\mathtt{R}\_{5}(0.3, 0.3, 0.2, 0, 0.2)𝚁3\mathtt{R}\_{3}(0.275, 0.255, 0.157, 0.196, 0.118)𝚁4\mathtt{R}\_{4}(0.5, 0.5, 0, 0, 0)𝚁5\mathtt{R}\_{5}(0.143, 0.714, 0.143, 0, 0)𝚁4\mathtt{R}\_{4}(0.139, 0.308, 0.092, 0.369, 0.092)
UnconditionalProbability1-Day prior1/2-Days prior1/2/3-Days prior

Figure 7: Normal (2005) regime context tree for NYSE Composite (NYA) index. The root node (\*) a the bold square border shows unconditional probabilities of 𝚁1,𝚁2,𝚁3,𝚁4​and​𝚁5\mathtt{R}\_{1},\mathtt{R}\_{2},\mathtt{R}\_{3},\mathtt{R}\_{4}\hskip 2.0pt\text{and}\hskip 2.0pt\mathtt{R}\_{5}.



|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Table 11: Contexts with Count >2>2 for developed stock market indices during High regimes.  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | Context | Count | Probabilities to after (State) | | | | | | P(𝚁1)(\mathtt{R}\_{1}) | P(𝚁2)(\mathtt{R}\_{2}) | P(𝚁3)(\mathtt{R}\_{3}) | P(𝚁4)(\mathtt{R}\_{4}) | P(𝚁5)(\mathtt{R}\_{5}) | | 𝚁1\mathtt{R}\_{1} | 13 | 0.277 | 0.196 | 0.137 | 0.163 | 0.227 | | 𝚁1​𝚁1\mathtt{R}\_{1}\mathtt{R}\_{1} | 5 | 0.282 | 0.169 | 0.151 | 0.182 | 0.216 | | 𝚁1​𝚁1​𝚁5\mathtt{R}\_{1}\mathtt{R}\_{1}\mathtt{R}\_{5} | 3 | 0.250 | 0.163 | 0.150 | 0.188 | 0.250 | | 𝚁1​𝚁3\mathtt{R}\_{1}\mathtt{R}\_{3} | 4 | 0.312 | 0.327 | 0.102 | 0.161 | 0.099 | | 𝚁1​𝚁4\mathtt{R}\_{1}\mathtt{R}\_{4} | 6 | 0.231 | 0.362 | 0.085 | 0.119 | 0.203 | | 𝚁2\mathtt{R}\_{2} | 12 | 0.262 | 0.170 | 0.143 | 0.206 | 0.220 | | 𝚁2​𝚁1\mathtt{R}\_{2}\mathtt{R}\_{1} | 3 | 0.078 | 0.171 | 0.279 | 0.075 | 0.398 | | 𝚁2​𝚁4\mathtt{R}\_{2}\mathtt{R}\_{4} | 8 | 0.254 | 0.188 | 0.226 | 0.264 | 0.068 | | 𝚁2​𝚁5\mathtt{R}\_{2}\mathtt{R}\_{5} | 5 | 0.156 | 0.296 | 0.183 | 0.109 | 0.256 | | 𝚁3\mathtt{R}\_{3} | 9 | 0.230 | 0.218 | 0.177 | 0.210 | 0.166 | | 𝚁3​𝚁3\mathtt{R}\_{3}\mathtt{R}\_{3} | 3 | 0.204 | 0.256 | 0.098 | 0.238 | 0.204 | | 𝚁4\mathtt{R}\_{4} | 17 | 0.224 | 0.221 | 0.189 | 0.185 | 0.181 | | 𝚁4​𝚁1\mathtt{R}\_{4}\mathtt{R}\_{1} | 6 | 0.266 | 0.072 | 0.109 | 0.191 | 0.362 | | 𝚁4​𝚁2\mathtt{R}\_{4}\mathtt{R}\_{2} | 7 | 0.312 | 0.090 | 0.177 | 0.246 | 0.175 | | 𝚁4​𝚁3\mathtt{R}\_{4}\mathtt{R}\_{3} | 6 | 0.266 | 0.210 | 0.190 | 0.169 | 0.165 | | 𝚁4​𝚁4\mathtt{R}\_{4}\mathtt{R}\_{4} | 5 | 0.283 | 0.252 | 0.208 | 0.137 | 0.119 | | 𝚁5\mathtt{R}\_{5} | 12 | 0.238 | 0.197 | 0.182 | 0.182 | 0.202 | | 𝚁5​𝚁1\mathtt{R}\_{5}\mathtt{R}\_{1} | 4 | 0.253 | 0.167 | 0.155 | 0.209 | 0.218 | | 𝚁5​𝚁2\mathtt{R}\_{5}\mathtt{R}\_{2} | 5 | 0.191 | 0.219 | 0.102 | 0.281 | 0.207 | | 𝚁5​𝚁3\mathtt{R}\_{5}\mathtt{R}\_{3} | 3 | 0.268 | 0.292 | 0.250 | 0.036 | 0.155 | | 𝚁5​𝚁4\mathtt{R}\_{5}\mathtt{R}\_{4} | 4 | 0.102 | 0.323 | 0.142 | 0.320 | 0.113 | | 𝚁5​𝚁5\mathtt{R}\_{5}\mathtt{R}\_{5} | 3 | 0.284 | 0.123 | 0.145 | 0.270 | 0.179 | | Table 12: Contexts with Count >2>2 for developed stock market indices during Normal regimes.  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | Context | Count | Probability to after (State) | | | | | | P(𝚁1)(\mathtt{R}\_{1}) | P(𝚁2)(\mathtt{R}\_{2}) | P(𝚁3)(\mathtt{R}\_{3}) | P(𝚁4)(\mathtt{R}\_{4}) | P(𝚁5)(\mathtt{R}\_{5}) | | 𝚁1\mathtt{R}\_{1} | 8 | 0.182 | 0.244 | 0.194 | 0.214 | 0.166 | | 𝚁1​𝚁1\mathtt{R}\_{1}\mathtt{R}\_{1} | 3 | 0.083 | 0.188 | 0.000 | 0.188 | 0.542 | | 𝚁1​𝚁2\mathtt{R}\_{1}\mathtt{R}\_{2} | 4 | 0.098 | 0.320 | 0.120 | 0.365 | 0.097 | | 𝚁2\mathtt{R}\_{2} | 15 | 0.117 | 0.260 | 0.260 | 0.257 | 0.106 | | 𝚁2​𝚁1\mathtt{R}\_{2}\mathtt{R}\_{1} | 3 | 0.108 | 0.000 | 0.125 | 0.558 | 0.208 | | 𝚁2​𝚁2\mathtt{R}\_{2}\mathtt{R}\_{2} | 10 | 0.138 | 0.249 | 0.229 | 0.269 | 0.116 | | 𝚁2​𝚁3\mathtt{R}\_{2}\mathtt{R}\_{3} | 3 | 0.119 | 0.192 | 0.335 | 0.204 | 0.151 | | 𝚁2​𝚁4\mathtt{R}\_{2}\mathtt{R}\_{4} | 6 | 0.148 | 0.258 | 0.230 | 0.256 | 0.109 | | 𝚁3\mathtt{R}\_{3} | 15 | 0.105 | 0.295 | 0.270 | 0.232 | 0.098 | | 𝚁3​𝚁2\mathtt{R}\_{3}\mathtt{R}\_{2} | 3 | 0.069 | 0.228 | 0.229 | 0.330 | 0.144 | | 𝚁3​𝚁3\mathtt{R}\_{3}\mathtt{R}\_{3} | 4 | 0.200 | 0.172 | 0.201 | 0.254 | 0.173 | | 𝚁3​𝚁4\mathtt{R}\_{3}\mathtt{R}\_{4} | 9 | 0.156 | 0.367 | 0.252 | 0.178 | 0.048 | | 𝚁3​𝚁5\mathtt{R}\_{3}\mathtt{R}\_{5} | 5 | 0.027 | 0.246 | 0.280 | 0.358 | 0.089 | | 𝚁4\mathtt{R}\_{4} | 15 | 0.095 | 0.309 | 0.295 | 0.209 | 0.093 | | 𝚁4​𝚁2\mathtt{R}\_{4}\mathtt{R}\_{2} | 5 | 0.176 | 0.308 | 0.189 | 0.225 | 0.104 | | 𝚁4​𝚁2​𝚁3\mathtt{R}\_{4}\mathtt{R}\_{2}\mathtt{R}\_{3} | 3 | 0.200 | 0.333 | 0.000 | 0.233 | 0.233 | | 𝚁4​𝚁4\mathtt{R}\_{4}\mathtt{R}\_{4} | 4 | 0.137 | 0.381 | 0.168 | 0.237 | 0.077 | | 𝚁4​𝚁5\mathtt{R}\_{4}\mathtt{R}\_{5} | 6 | 0.048 | 0.487 | 0.376 | 0.078 | 0.012 | | 𝚁5\mathtt{R}\_{5} | 7 | 0.046 | 0.247 | 0.316 | 0.286 | 0.105 | |



|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Table 13: Contexts with Count >2>2 for developing stock market indices during Extreme regimes.  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | Context | Count | Probabilities to after (State) | | | | | | P(𝚁1\mathtt{R}\_{1}) | P(𝚁2\mathtt{R}\_{2}) | P(𝚁3\mathtt{R}\_{3}) | P(𝚁4\mathtt{R}\_{4}) | P(𝚁5\mathtt{R}\_{5}) | | 𝚁1\mathtt{R}\_{1} | 19 | 0.336 | 0.139 | 0.131 | 0.137 | 0.258 | | 𝚁1​𝚁1\mathtt{R}\_{1}\mathtt{R}\_{1} | 6 | 0.399 | 0.094 | 0.074 | 0.139 | 0.295 | | 𝚁1​𝚁2\mathtt{R}\_{1}\mathtt{R}\_{2} | 7 | 0.228 | 0.117 | 0.283 | 0.142 | 0.231 | | 𝚁1​𝚁3\mathtt{R}\_{1}\mathtt{R}\_{3} | 6 | 0.386 | 0.272 | 0.128 | 0.072 | 0.142 | | 𝚁1​𝚁4\mathtt{R}\_{1}\mathtt{R}\_{4} | 9 | 0.396 | 0.207 | 0.133 | 0.136 | 0.128 | | 𝚁1​𝚁5\mathtt{R}\_{1}\mathtt{R}\_{5} | 6 | 0.343 | 0.123 | 0.127 | 0.135 | 0.272 | | 𝚁2\mathtt{R}\_{2} | 13 | 0.286 | 0.188 | 0.161 | 0.154 | 0.211 | | 𝚁2​𝚁1\mathtt{R}\_{2}\mathtt{R}\_{1} | 3 | 0.304 | 0.149 | 0.201 | 0.126 | 0.220 | | 𝚁2​𝚁2\mathtt{R}\_{2}\mathtt{R}\_{2} | 3 | 0.188 | 0.283 | 0.351 | 0.000 | 0.178 | | 𝚁2​𝚁4\mathtt{R}\_{2}\mathtt{R}\_{4} | 3 | 0.504 | 0.159 | 0.115 | 0.124 | 0.099 | | 𝚁3\mathtt{R}\_{3} | 9 | 0.239 | 0.192 | 0.168 | 0.191 | 0.210 | | 𝚁3​𝚁3\mathtt{R}\_{3}\mathtt{R}\_{3} | 4 | 0.153 | 0.104 | 0.086 | 0.124 | 0.533 | | 𝚁3​𝚁5\mathtt{R}\_{3}\mathtt{R}\_{5} | 3 | 0.022 | 0.262 | 0.484 | 0.118 | 0.115 | | 𝚁4\mathtt{R}\_{4} | 13 | 0.272 | 0.211 | 0.133 | 0.171 | 0.213 | | 𝚁4​𝚁3\mathtt{R}\_{4}\mathtt{R}\_{3} | 3 | 0.283 | 0.257 | 0.179 | 0.260 | 0.023 | | 𝚁4​𝚁4\mathtt{R}\_{4}\mathtt{R}\_{4} | 4 | 0.000 | 0.077 | 0.375 | 0.307 | 0.241 | | 𝚁4​𝚁5\mathtt{R}\_{4}\mathtt{R}\_{5} | 3 | 0.321 | 0.177 | 0.033 | 0.067 | 0.403 | | 𝚁5\mathtt{R}\_{5} | 18 | 0.276 | 0.174 | 0.163 | 0.134 | 0.253 | | 𝚁5​𝚁1\mathtt{R}\_{5}\mathtt{R}\_{1} | 8 | 0.326 | 0.199 | 0.129 | 0.095 | 0.252 | | 𝚁5​𝚁1​𝚁1\mathtt{R}\_{5}\mathtt{R}\_{1}\mathtt{R}\_{1} | 4 | 0.431 | 0.000 | 0.049 | 0.361 | 0.160 | | 𝚁5​𝚁3\mathtt{R}\_{5}\mathtt{R}\_{3} | 4 | 0.175 | 0.270 | 0.160 | 0.036 | 0.360 | | 𝚁5​𝚁5\mathtt{R}\_{5}\mathtt{R}\_{5} | 6 | 0.255 | 0.181 | 0.127 | 0.144 | 0.294 | | Table 14: Contexts with Count >2>2 for developing stock market indices during High regimes.  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | Context | Count | Probabilities to after (State) | | | | | | P(𝚁1\mathtt{R}\_{1}) | P(𝚁2\mathtt{R}\_{2}) | P(𝚁3\mathtt{R}\_{3}) | P(𝚁4\mathtt{R}\_{4}) | P(𝚁5\mathtt{R}\_{5}) | | 𝚁1\mathtt{R}\_{1} | 18 | 0.295 | 0.166 | 0.161 | 0.144 | 0.235 | | 𝚁1​𝚁1\mathtt{R}\_{1}\mathtt{R}\_{1} | 4 | 0.195 | 0.357 | 0.060 | 0.046 | 0.342 | | 𝚁1​𝚁2\mathtt{R}\_{1}\mathtt{R}\_{2} | 4 | 0.336 | 0.213 | 0.208 | 0.096 | 0.147 | | 𝚁1​𝚁3\mathtt{R}\_{1}\mathtt{R}\_{3} | 6 | 0.401 | 0.071 | 0.239 | 0.167 | 0.122 | | 𝚁1​𝚁4\mathtt{R}\_{1}\mathtt{R}\_{4} | 5 | 0.145 | 0.238 | 0.182 | 0.263 | 0.172 | | 𝚁1​𝚁5\mathtt{R}\_{1}\mathtt{R}\_{5} | 4 | 0.238 | 0.195 | 0.330 | 0.080 | 0.157 | | 𝚁2\mathtt{R}\_{2} | 13 | 0.278 | 0.185 | 0.184 | 0.139 | 0.214 | | 𝚁2​𝚁1\mathtt{R}\_{2}\mathtt{R}\_{1} | 4 | 0.239 | 0.177 | 0.174 | 0.148 | 0.263 | | 𝚁2​𝚁3\mathtt{R}\_{2}\mathtt{R}\_{3} | 4 | 0.091 | 0.210 | 0.301 | 0.162 | 0.237 | | 𝚁2​𝚁5\mathtt{R}\_{2}\mathtt{R}\_{5} | 5 | 0.208 | 0.193 | 0.243 | 0.149 | 0.207 | | 𝚁3\mathtt{R}\_{3} | 8 | 0.293 | 0.143 | 0.156 | 0.170 | 0.237 | | 𝚁3​𝚁2\mathtt{R}\_{3}\mathtt{R}\_{2} | 4 | 0.208 | 0.055 | 0.345 | 0.144 | 0.249 | | 𝚁4\mathtt{R}\_{4} | 13 | 0.225 | 0.212 | 0.170 | 0.178 | 0.214 | | 𝚁4​𝚁1\mathtt{R}\_{4}\mathtt{R}\_{1} | 3 | 0.174 | 0.000 | 0.278 | 0.261 | 0.288 | | 𝚁4​𝚁2\mathtt{R}\_{4}\mathtt{R}\_{2} | 6 | 0.081 | 0.254 | 0.175 | 0.412 | 0.078 | | 𝚁4​𝚁3\mathtt{R}\_{4}\mathtt{R}\_{3} | 3 | 0.127 | 0.360 | 0.267 | 0.083 | 0.163 | | 𝚁4​𝚁5\mathtt{R}\_{4}\mathtt{R}\_{5} | 5 | 0.287 | 0.194 | 0.245 | 0.130 | 0.144 | | 𝚁5\mathtt{R}\_{5} | 15 | 0.225 | 0.187 | 0.170 | 0.194 | 0.225 | | 𝚁5​𝚁1\mathtt{R}\_{5}\mathtt{R}\_{1} | 3 | 0.303 | 0.303 | 0.101 | 0.106 | 0.187 | | 𝚁5​𝚁2\mathtt{R}\_{5}\mathtt{R}\_{2} | 4 | 0.214 | 0.113 | 0.218 | 0.155 | 0.301 | | 𝚁5​𝚁3\mathtt{R}\_{5}\mathtt{R}\_{3} | 7 | 0.165 | 0.165 | 0.329 | 0.240 | 0.101 | | 𝚁5​𝚁4\mathtt{R}\_{5}\mathtt{R}\_{4} | 5 | 0.200 | 0.231 | 0.155 | 0.307 | 0.108 | | 𝚁5​𝚁5\mathtt{R}\_{5}\mathtt{R}\_{5} | 5 | 0.228 | 0.122 | 0.179 | 0.159 | 0.313 | | 𝚁5​𝚁5​𝚁5\mathtt{R}\_{5}\mathtt{R}\_{5}\mathtt{R}\_{5} | 3 | 0.393 | 0.322 | 0.000 | 0.286 | 0.000 | |
| Table 15: Contexts with Count >2>2 for developing stock market indices during Normal regimes.  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | Context | Count | Probabilities to after (State) | | | | | | P(𝚁1\mathtt{R}\_{1}) | P(𝚁2\mathtt{R}\_{2}) | P(𝚁3\mathtt{R}\_{3}) | P(𝚁4\mathtt{R}\_{4}) | P(𝚁5\mathtt{R}\_{5}) | | 𝚁1\mathtt{R}\_{1} | 8 | 0.254 | 0.161 | 0.190 | 0.248 | 0.147 | | 𝚁2\mathtt{R}\_{2} | 14 | 0.142 | 0.242 | 0.282 | 0.238 | 0.096 | | 𝚁2​𝚁2\mathtt{R}\_{2}\mathtt{R}\_{2} | 6 | 0.072 | 0.328 | 0.215 | 0.221 | 0.165 | | 𝚁2​𝚁3\mathtt{R}\_{2}\mathtt{R}\_{3} | 5 | 0.119 | 0.265 | 0.255 | 0.260 | 0.102 | | 𝚁2​𝚁4\mathtt{R}\_{2}\mathtt{R}\_{4} | 3 | 0.094 | 0.266 | 0.255 | 0.229 | 0.156 | | 𝚁2​𝚁5\mathtt{R}\_{2}\mathtt{R}\_{5} | 3 | 0.176 | 0.307 | 0.327 | 0.042 | 0.149 | | 𝚁3\mathtt{R}\_{3} | 14 | 0.140 | 0.260 | 0.281 | 0.201 | 0.118 | | 𝚁3​𝚁1\mathtt{R}\_{3}\mathtt{R}\_{1} | 6 | 0.130 | 0.247 | 0.270 | 0.188 | 0.165 | | 𝚁3​𝚁2\mathtt{R}\_{3}\mathtt{R}\_{2} | 5 | 0.121 | 0.202 | 0.164 | 0.153 | 0.360 | | 𝚁3​𝚁3\mathtt{R}\_{3}\mathtt{R}\_{3} | 7 | 0.045 | 0.229 | 0.504 | 0.184 | 0.039 | | 𝚁3​𝚁3​𝚁4\mathtt{R}\_{3}\mathtt{R}\_{3}\mathtt{R}\_{4} | 3 | 0.320 | 0.368 | 0.215 | 0.097 | 0.000 | | 𝚁3​𝚁4\mathtt{R}\_{3}\mathtt{R}\_{4} | 3 | 0.159 | 0.183 | 0.369 | 0.203 | 0.086 | | 𝚁3​𝚁5\mathtt{R}\_{3}\mathtt{R}\_{5} | 3 | 0.333 | 0.217 | 0.159 | 0.068 | 0.222 | | 𝚁4\mathtt{R}\_{4} | 10 | 0.147 | 0.295 | 0.252 | 0.180 | 0.126 | | 𝚁4​𝚁2\mathtt{R}\_{4}\mathtt{R}\_{2} | 4 | 0.163 | 0.301 | 0.198 | 0.188 | 0.150 | | 𝚁4​𝚁3\mathtt{R}\_{4}\mathtt{R}\_{3} | 4 | 0.137 | 0.226 | 0.226 | 0.266 | 0.146 | | 𝚁5\mathtt{R}\_{5} | 8 | 0.118 | 0.200 | 0.302 | 0.236 | 0.145 | | 𝚁5​𝚁2\mathtt{R}\_{5}\mathtt{R}\_{2} | 3 | 0.143 | 0.182 | 0.521 | 0.057 | 0.098 | | 𝚁5​𝚁3\mathtt{R}\_{5}\mathtt{R}\_{3} | 3 | 0.186 | 0.183 | 0.195 | 0.344 | 0.091 | | |