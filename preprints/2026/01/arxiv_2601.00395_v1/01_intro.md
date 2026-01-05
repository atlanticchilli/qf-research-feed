---
authors:
- Kundan Mukhia
- Imran Ansari
- S R Luwang
- Md Nurujjaman
doc_id: arxiv:2601.00395v1
family_id: arxiv:2601.00395
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional
  P-Threshold Mutual Information Approach'
url_abs: http://arxiv.org/abs/2601.00395v1
url_html: https://arxiv.org/html/2601.00395v1
venue: arXiv q-fin
version: 1
year: 2026
---


Kundan Mukhia
[kundanmukhia07@gmail.com](mailto:kundanmukhia07@gmail.com)

Imran Ansari
[imranansari@iisc.ac.in](mailto:imranansari@iisc.ac.in)

S R Luwang
[salamrabindrajit@gmail.com](mailto:salamrabindrajit@gmail.com)

Md Nurujjaman
[md.nurujjaman@nitsikkim.ac.in](mailto:md.nurujjaman@nitsikkim.ac.in)

###### Abstract

This study investigates how financial market structure reorganizes during the COVID-19 crash using a conditional p-threshold mutual information (MI) based Minimum Spanning Tree (MST) network framework. We analyze nonlinear dependencies among the largest stocks from four geographically and economically diverse QUAD countries: the United States, Japan, Australia, and India. The crash period is identified using the Hellinger distance and further characterized by the Hilbert spectrum. A crash is defined when the Hellinger distance exceeds the threshold HD=μH+2​σHH\_{D}=\mu\_{H}+2\sigma\_{H}, enabling the segmentation of the data into pre-crash, crash, and post-crash periods. To isolate direct stock-level dependencies, the conditional p-threshold MI approach filters out common market effects and applies permutation-based significance testing. The resulting statistically validated dependencies are used to construct MST networks, allowing consistent comparison across market periods. The network analysis reveals common crisis-related dynamics across all markets. During the crash, networks become more integrated, with shorter path lengths and higher centrality, while algebraic connectivity declines, indicating increased structural fragility. A clear reorganization of the core–periphery structure is observed, with declining core concentration and increasing periphery fragility, supported by disassortative mixing that facilitates shock transmission. In the post-crash period, network topology shows only partial recovery, suggesting persistent structural effects. This interpretation is further supported by an aftershock analysis based on the Gutenberg–Richter law, which indicates a higher relative frequency of large volatility events following the crash. The consistency of these findings across all four markets highlights the effectiveness of the conditional p-threshold MI framework for capturing nonlinear interdependencies and systemic vulnerability in financial markets.

\affiliation

[inst1]organization=Department of Physics, National Institute of Technology,
postcode=737139,
state=Sikkim,
country=India

\affiliation

[inst2]organization=Department of Management Studies, Indian Institute of Science,
postcode=560012,
state=Bengaluru,
country=India

## 1 Introduction

Financial markets are complex adaptive systems where the collective behavior of numerous interacting assets gives rise to emergent phenomena, including periods of stability, bubbles, and systemic crashes. Understanding the structure and dynamics of these interactions is fundamental to financial stability analysis and risk management. Network theory has emerged as a powerful model for this purpose, transforming multivariate time series of stock returns into graphs that reveal the underlying structure of financial systems mantegna1999hierarchical, Yang2008, mukhia2024complex, tumminello2007correlation, ansari2025comprehensive, Tse2010. The most established approach involves constructing networks from correlation matrices, with filtering techniques like the Minimum Spanning Tree (MST), planar maximally filtered graph (PMFG) and threshold-based filtering method, used to distill meaningful, sparse topologies from dense correlation structures mantegna1999hierarchical, tumminello2005tool, boginski2005statistical, Heiberger2014. These methods have successfully mapped hierarchical organization, sectoral clustering and core–periphery and community structures in financial networks Onnela2003, Boginski2006, pawanesh2025exploring, ansari2025novel.

Periods of financial crisis expose latent vulnerabilities in market structure and often trigger abrupt reorganization of asset interdependencies han2019network, pawanesh2025exploring, ansari2025novel, li2019portfolio. The COVID-19 pandemic-induced crash of March 2020, like the global financial crisis of 2008, represents an extreme stress episode marked by heightened volatility, synchronized market movements, and large-scale capital reallocation across asset classes pawanesh2025exploring, ansari2025novel, peng2024global. During such periods, pairwise correlations across assets rise sharply and tend to converge, leading to dense and homogeneous correlation networks in which meaningful structural information is lost kenett2010dominating, pozzi2013spread, longin1995correlation. As a result, correlation-based network approaches struggle to distinguish genuine channels of contagion from spurious dependencies induced by common market-wide factors gopikrishnan2001quantifying, pan2007collective. Although noise-filtering techniques applied to correlation matrices can partially recover global organization and sectoral structure macmahon2015community, jiang2014structure, ansari2025comprehensive, many traditional crisis-analysis frameworks based on volatility measures, raw correlations, or standard econometric models remain limited in their ability to isolate intrinsic stock-to-stock interactions under extreme stress pozzi2013spread, han2019network, tumminello2007correlation, pozzi2007dynamical. To address these limitations, mutual information (MI) has been proposed as a more general, model-free measure of dependence that captures both linear and nonlinear relationships among financial assets fiedor2014networks, sharma2019mutual. However, MI estimates from finite samples are themselves sensitive to noise and are strongly influenced by market-wide co-movement during crises, highlighting the need for conditioning and statistically grounded filtering procedures to extract direct and meaningful dependencies.

Existing empirical studies applying network methods to finance have largely focused on economically homogeneous groups of markets. Examples include analyses of the G7 countries korkusuz2023complex, polat2020frequency, regionally and institutionally integrated blocs such as BRICS vizgunov2013comparative, dong2020research, as well as sector-wise network studies within individual national stock markets that examine industry-level or firm-level interactions under normal and crisis conditions pozzi2013spread, huang2009network, bielinskyi2022high, rabindrajit2024high. Although these studies offer useful insights, their emphasis on relatively homogeneous economic groupings makes it difficult to assess whether observed crisis-induced network patterns, particularly changes in core–periphery organization, reflect universal properties of financial systems or are specific to economically integrated regions. Comparative evidence from geographically and economically diverse markets that are not bound by formal economic pacts remains limited.

In this context, the QUAD countries, namely the United States, Japan, Australia, and India, offer a distinctive and underexplored setting. Unlike economic alliances such as the G7 or BRICS, the QUAD is not an economic pact but a strategic grouping encompassing markets with markedly different levels of development, financial structures, and economic drivers quadrilateral\_security\_dialogue. It includes a dominant global financial market (USA), a mature Asian economy (Japan), a developed commodity-oriented market (Australia), and a large emerging economy (India). This heterogeneity provides a natural testbed for examining whether crisis-induced network reorganization, particularly in terms of core–periphery structure, exhibits universal characteristics across fundamentally different market environments.

In this study, we address these methodological and empirical gaps by proposing a conditional p-threshold MI framework to analyze stock market dynamics before, during, and after the COVID-19 crash across the QUAD countries. First, we identify the crash period using the rolling Hellinger distance(HD), which detects statistically significant shifts in the cross-sectional return distribution, and validate the intensity and persistence of the crash using Hilbert spectrum(HS) analysis. This allows us to divide the time series into pre-crash, crash, and post-crash periods. Second, we compute MI between stock returns after removing market-wide effects through regression on the corresponding market index. We then apply permutation-based significance testing to retain only statistically significant and direct nonlinear dependencies. Finally, these validated dependencies are mapped into MST networks to ensure sparse, comparable topologies across different periods.

Our results show a consistent pattern across all four markets. During the COVID-19 crash, financial networks experienced a clear core–periphery reorganization, with reduced core concentration and increased periphery fragility, indicating a more integrated but structurally fragile market state. Post-crash networks exhibit only partial recovery, suggesting persistent structural aftershocks, a finding further supported by the Gutenberg–Richter law. The similarity of these patterns across the diverse QUAD markets highlights the ability of the conditional p-threshold MI framework to capture universal features of systemic vulnerability.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2601.00395v1#S2 "2 Method of Analysis ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") describes the methodology employed in this study, while Section [3](https://arxiv.org/html/2601.00395v1#S3 "3 Data Description ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") presents the data used for the analysis. Section [4](https://arxiv.org/html/2601.00395v1#S4 "4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") reports and discusses the empirical results. Finally, Section [6](https://arxiv.org/html/2601.00395v1#S6 "6 Conclusion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") concludes the paper and outlines directions for future research.

## 2 Method of Analysis

To study the evolution of dependency structures and network organization in QUAD countries’ stock markets during the COVID-19 crash, we applied several methods. Initially, we detect the COVID-19 stock market crash using the HD method and further characterize it through the HS. Based on the identified crash regions, we divide the data into pre-crash, crash, and post-crash periods. Next, we remove the market effect from individual stock returns using a CAPM-based regression framework kisman2015m. After removing the market effect, we estimate the MI among stocks to capture nonlinear dependencies. A conditional p-threshold MI approach based on permutation testing is used to filter statistically significant dependencies. Using this conditional p-threshold MI, an MST method is applied to construct the stock market network. Finally, we perform a comprehensive topological analysis using network metrics, including core concentration, periphery fragility, centrality distributions, and modularity, to quantify structural reconfiguration and systemic vulnerability across the different market periods.

### 2.1 Crash detection

In this subsection, we discuss the methodology used to identify and characterize stock market crash periods. First, crash events are detected using the HD, which quantifies abrupt, systemic shifts in the cross-sectional distribution of stock returns, enabling the simultaneous identification of a market-wide crash. Second, the detected crash regions are further characterized using the HS, allowing for a time-frequency-energy analysis of market volatility. The combined use of these two methods ensures robust identification of crash periods by integrating both statistical distance measures and spectral characteristics. Detailed descriptions of each technique are provided in the following subsubsections.

#### 2.1.1 Hellinger-Distance

The Hellinger distance (HD) is a measure of dissimilarity between probability distributions deza2009encyclopedia, gibbs2002choosing. The HD has been successfully applied in change detection, concept drift analysis, and fault detection aggoune2016change, ditzler2011hellinger, tang2009sketch. In this study, we used the HD as an indicator to detect the crash periods and structural stress in market data.

Let Pt,iP\_{t,i} denote the closing price of stock ii on trading day tt. We define the log-return of stock ii as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt,i=log⁡Pt,i−log⁡Pt−1,i,t=2,…,T,i=1,…,N.r\_{t,i}=\log P\_{t,i}-\log P\_{t-1,i},\qquad t=2,\dots,T,\quad i=1,\dots,N. |  | (1) |

At each time tt, the cross-section of returns is denoted by rt=(rt,1,…,rt,N){r}\_{t}=(r\_{t,1},\dots,r\_{t,N}).

To characterise the normal market state at time tt, we construct a reference distribution from a rolling window of length WW:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫0​(t)={rτ,i:τ=t−W,…,t−1,i=1,…,N}.\mathcal{P}\_{0}(t)=\big\{r\_{\tau,i}:\tau=t-W,\dots,t-1,\;i=1,\dots,N\big\}. |  | (2) |

This set aggregates all returns observed in the WW days prior to tt across all assets and serves as a representation for the recent cross-sectional behaviour of the market. The corresponding cross-sectional state is represented by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫1​(t)={rt,i:i=1,…,N}.\mathcal{P}\_{1}(t)=\big\{r\_{t,i}:i=1,\dots,N\big\}. |  | (3) |

Both 𝒫0​(t)\mathcal{P}\_{0}(t) and 𝒫1​(t)\mathcal{P}\_{1}(t) are transformed into discrete probability distributions by histogram-based density estimation. Let [a,b][a,b] denotes the lower and upper bounds of the range used for estimation, which in practice is restricted to the central quantiles of the pooled return distribution to limit the influence of extreme outliers.This interval is partitioned into BB bins with edges {a=ξ0<ξ1<⋯<ξB=b}\{a=\xi\_{0}<\xi\_{1}<\dots<\xi\_{B}=b\}. The empirical probability assigned to bin bb for the reference window and the corresponding cross-section is
given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | pb​(t)=#​{x∈𝒫0​(t):x∈[ξb−1,ξb)}∑j=1B#​{x∈𝒫0​(t):x∈[ξj−1,ξj)},p\_{b}(t)=\frac{\#\big\{x\in\mathcal{P}\_{0}(t):x\in[\xi\_{b-1},\xi\_{b})\big\}}{\sum\_{j=1}^{B}\#\big\{x\in\mathcal{P}\_{0}(t):x\in[\xi\_{j-1},\xi\_{j})\big\}}, |  | (4) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | qb​(t)=#​{y∈𝒫1​(t):y∈[ξb−1,ξb)}∑j=1B#​{y∈𝒫1​(t):y∈[ξj−1,ξj)},q\_{b}(t)=\frac{\#\big\{y\in\mathcal{P}\_{1}(t):y\in[\xi\_{b-1},\xi\_{b})\big\}}{\sum\_{j=1}^{B}\#\big\{y\in\mathcal{P}\_{1}(t):y\in[\xi\_{j-1},\xi\_{j})\big\}}, |  | (5) |

where #​{⋅}\#\{\cdot\} denotes the cardinality operator. By construction,
∑b=1Bpb​(t)=∑b=1Bqb​(t)=1\sum\_{b=1}^{B}p\_{b}(t)=\sum\_{b=1}^{B}q\_{b}(t)=1 for all tt.

For two discrete probability distributions p​(t)=(p1​(t),…,pB​(t))p(t)=(p\_{1}(t),\dots,p\_{B}(t)) and q​(t)=(q1​(t),…,qB​(t))q(t)=(q\_{1}(t),\dots,q\_{B}(t)), the HD is given as,

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(p​(t),q​(t))=12​∑b=1B(pb​(t)−qb​(t))2.H\big(p(t),q(t)\big)=\sqrt{\frac{1}{2}\sum\_{b=1}^{B}\Big(\sqrt{p\_{b}(t)}-\sqrt{q\_{b}(t)}\Big)^{2}}. |  | (6) |

The HD lies between 0≤H​(p,q)≤10\leq H(p,q)\leq 1, with H​(p,q)=0H(p,q)=0 if and only if p≡qp\equiv q and H​(p,q)H(p,q) approaches 11 when the two distributions assign probability mass to almost disjoint regions of the support. These properties of the HD make it suitable for detecting distributional shifts.

Using Eq. ([6](https://arxiv.org/html/2601.00395v1#S2.E6 "In 2.1.1 Hellinger-Distance ‣ 2.1 Crash detection ‣ 2 Method of Analysis ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach")), we compute a univariate time series of rolling Hellinger distances for t=W+1,…,Tt=W+1,\dots,T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ht=H​(p​(t),q​(t)).H\_{t}=H\big(p(t),q(t)\big). |  | (7) |

Under normal market conditions, HtH\_{t} fluctuates around a baseline level, while sudden changes in market behaviour, such as crashes or regime shifts, appear as pronounced spikes. To identify such periods, we define an empirical decision threshold based on the mean and standard deviation of the HD series,

|  |  |  |  |
| --- | --- | --- | --- |
|  | HD=μH+2​σH,H\_{D}=\mu\_{H}+2\sigma\_{H}, |  | (8) |

where μH\mu\_{H} and σH\sigma\_{H} denote the sample mean and standard deviation of {Ht}\{H\_{t}\}. Days for which Ht>HDH\_{t}>H\_{D} are classified as the crash region.

In this study, we interpret H​(p​(t),q​(t))H\big(p(t),q(t)\big) as a measure of how strongly the cross-sectional return distribution at time tt deviates from the reference distribution formed over the preceding WW trading days. Large values of the Hellinger distance indicate significant changes in the distributional shape. Accordingly, time periods for which HtH\_{t} exceeds the decision threshold TDT\_{D} are classified as crash regions.

#### 2.1.2 Hilbert-Huang Transform

The Hilbert–Huang Transform (HHT) is a data-driven technique designed to analyze nonlinear and nonstationary time series. Its first stage, Empirical Mode Decomposition (EMD), adaptively decomposes a signal into a finite set of oscillatory components known as Intrinsic Mode Functions (IMFs), each representing a characteristic time scale of the underlying process huang1998empirical, rai2023detection.

A component extracted from the time series is identified as an IMF if it satisfies the following criteria,

* 1.

  The number of local extrema and the number of zero crossings are equal or differ by at most one.
* 2.

  The local mean, defined as the average of the upper and lower envelopes formed by the local maxima and minima, is zero at every point.

The EMD procedure is implemented as follows. For a given input time series DtD\_{t}, the local maxima and minima are first identified, and spline interpolation is used to construct the upper envelope (U​EtUE\_{t}) and lower envelope (L​EtLE\_{t}), respectively. The local mean of these envelopes is then computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | mt=U​Et+L​Et2.m\_{t}=\frac{UE\_{t}+LE\_{t}}{2}. |  | (9) |

Removing this mean from the original signal produces an updated series,

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​Dt=Dt−mt.ND\_{t}=D\_{t}-m\_{t}. |  | (10) |

This sifting process is iteratively applied to N​DtND\_{t} until the resulting signal satisfies the IMF conditions. The extracted component is then designated as the first intrinsic mode function, I​M​F1IMF\_{1}. The residual signal is obtained as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nt=Dt−I​M​F1,N\_{t}=D\_{t}-IMF\_{1}, |  | (11) |

The same procedure is then applied iteratively to extract additional IMFs. The decomposition process continues until the remaining residual becomes a monotonic function, representing the long-term trend of the original time series. As a result, the original signal can be reconstructed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt=∑j=1nI​M​Fj+residue,D\_{t}=\sum\_{j=1}^{n}IMF\_{j}+\text{residue}, |  | (12) |

where nn denotes the total number of extracted IMFs.

In the second stage of the HHT, each IMF is analyzed using the Hilbert transform to obtain instantaneous frequency information. The Hilbert transform of an IMF is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(t)=1π​P.V.​∫−∞∞IMF​(τ)t−τ​𝑑τ,H(t)=\frac{1}{\pi}\,\text{P.V.}\int\_{-\infty}^{\infty}\frac{\text{IMF}(\tau)}{t-\tau}\,d\tau, |  | (13) |

Here, P.V. is the Cauchy principal value. We defined the instantaneous phase as huang1998empirical

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(t)=tan−1⁡(H​(t)IMF​(t)),\phi(t)=\tan^{-1}\left(\frac{H(t)}{\text{IMF}(t)}\right), |  | (14) |

and the instantaneous frequency is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ω​(t)=d​ϕ​(t)d​t.\omega(t)=\frac{d\phi(t)}{dt}. |  | (15) |

The Hilbert spectrum H​(t,ω)H(t,\omega) provides a time–frequency representation of the signal and is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(t,ω)=ℜ⁡{∑iKi​(t)​ej​∫ω​(t)​𝑑t},H(t,\omega)=\Re\left\{\sum\_{i}K\_{i}(t)\,e^{j\int\omega(t)\,dt}\right\}, |  | (16) |

Here, Ki​(t)K\_{i}(t) denotes the instantaneous amplitude and ℜ⋅\Re{\cdot} denotes the real part.

From the Hilbert spectrum, the instantaneous energy is defined by the following equation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​E​(t)=∫ωH2​(t,ω)​𝑑ω.IE(t)=\int\_{\omega}H^{2}(t,\omega)\,d\omega. |  | (17) |

To facilitate comparison across time, the instantaneous energy is normalized as

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​EN​(t)=I​E​(t)max⁡[I​E​(t)].IE\_{N}(t)=\frac{IE(t)}{\max[IE(t)]}. |  | (18) |

In our study, we apply this framework to pinpoint the crash for the QUAD countries’ stock index.

### 2.2 Methodology for Network Construction: Conditional P-Threshold Mutual Information

In this subsection, we describe the methodology used to construct stock dependency networks. Market-adjusted abnormal returns are first obtained using the Capital Asset Pricing Model (CAPM). Mutual information(MI) is then used to measure linear and non-linear dependencies between stocks, followed by permutation testing to assess statistical significance. The resulting conditional p-thresholded MI matrices are used as adjacency matrices for network analysis.

#### 2.2.1 Returns and Abnormal Returns

Let pi​(t)p\_{i}(t) denote the daily closing price of stock ii at time tt (i=1,2,…,N,t=1,2,…,T)(i=1,2,\ldots,N,t=1,2,\ldots,T). The logarithmic return ri​(t)r\_{i}(t) of stock ii over time interval Δ​t\Delta t is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri​(t)=ln⁡[pi​(t)]−ln⁡[pi​(t−Δ​t)]r\_{i}(t)=\ln[p\_{i}(t)]-\ln[p\_{i}(t-\Delta t)] |  | (19) |

In this study, we set Δ​t=1\Delta t=1, making ri​(t)r\_{i}(t) the daily return of stock ii at time tt.

However, computing MI directly from raw stock returns ri​(t)r\_{i}(t) may not accurately reflect true inter-stock dependencies. A high MI value for a given stock pair does not automatically indicate a strong direct dependence, as it may be influenced by common market movements, macroeconomic factors, or systemic events longin1995correlation, lintner1975valuation, xu2017topological. In such cases, the observed dependence may arise mainly from shared exposure to market-wide fluctuations rather than from intrinsic interactions between the stocks. To address this issue, we follow the CAPM framework and remove the systematic market component from stock returns. The resulting abnormal returns capture stock-specific behavior and allow for a more reliable analysis of pure inter-stock dependencies, reducing the impact of common market effects.

#### 2.2.2 Removal of Market Influence via CAPM Regression

To isolate stock-specific components from common market movements, we employ the CAPM frameworkxu2017topological. For each QUAD country, we use the respective benchmark market index, S&P 500 for the United States, NIKKEI 225 for Japan, ASX 200 for Australia, and NIFTY 50 for India, to model and remove systematic market effects, as overall stock sentiment in each market is predominantly driven by these indices. For each stock ii, we specify the market model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri​(t)=αi+βi​rM​(t)+εi​(t),εi​(t)∼𝒩​(0,σi2)r\_{i}(t)=\alpha\_{i}+\beta\_{i}r\_{M}(t)+\varepsilon\_{i}(t),\quad\varepsilon\_{i}(t)\sim\mathcal{N}(0,\sigma\_{i}^{2}) |  | (20) |

where, ri​(t)r\_{i}(t) is return of stock ii at time tt, rM​(t)r\_{M}(t) is the return of market index at time tt, αi\alpha\_{i} is the stock-specific intercept (Jensen’s alpha), βi\beta\_{i} is systematic risk coefficient, and εi​(t)\varepsilon\_{i}(t) is idiosyncratic error term, which is assumed to be independent and identically distributed (i.i.d.) normal.

The parameters αi\alpha\_{i} and βi\beta\_{i} are estimated using ordinary least squares (OLS) regression as

|  |  |  |  |
| --- | --- | --- | --- |
|  | (α^i,β^i)=arg⁡minαi,βi​∑t=1T[ri​(t)−αi−βi​rM​(t)]2,(\hat{\alpha}\_{i},\hat{\beta}\_{i})=\arg\min\_{\alpha\_{i},\,\beta\_{i}}\sum\_{t=1}^{T}\left[r\_{i}(t)-\alpha\_{i}-\beta\_{i}r\_{M}(t)\right]^{2}, |  | (21) |

where TT is the total number of observations.

The market-adjusted abnormal return is then defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​ri​(t)=ri​(t)−α^i−β^i​rM​(t).ar\_{i}(t)=r\_{i}(t)-\hat{\alpha}\_{i}-\hat{\beta}\_{i}r\_{M}(t). |  | (22) |

where, a​ri​(t)ar\_{i}(t) is abnormal return of stock ii at time tt and α^i,β^i\hat{\alpha}\_{i},\hat{\beta}\_{i} is the OLS estimates of CAPM parameters.

These abnormal returns represent the portion of stock returns unexplained by market movements, enabling analysis of pure stock interdependencies. We then quantify dependencies between these abnormal returns using MI, which captures both linear and non-linear relationships between stocks, as described in the following section.

#### 2.2.3 Mutual Information

Mutual information (MI) measures both linear and non-linear dependencies between random variables XiX\_{i} and XjX\_{j} representing abnormal returns of stocks ii and jj, making it superior to traditional correlation measures for capturing complex relationships in financial markets guo2018development, fiedor2014networks, lahmiri2020renyi. By applying MI to abnormal returns rather than raw returns, we ensure that the measured dependencies reflect genuine inter-stock relationships rather than spurious correlations induced by common market factors.

For two continuous random variables XX and YY, the MI is defined as kraskov2004estimating, hacine2012low, steuer2002mutual

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(X;Y)=∬ℝ2p​(x,y)​log⁡(p​(x,y)p​(x)​p​(y))​𝑑x​𝑑yI(X;Y)=\iint\_{\mathbb{R}^{2}}p(x,y)\log\left(\frac{p(x,y)}{p(x)p(y)}\right)dxdy |  | (23) |

where, p​(x,y)p(x,y) is the joint probability density function of XX and YY, p​(x),p​(y)p(x),p(y) is marginal probability density functions and log⁡(⋅)\log(\cdot) is natural logarithm.

MI can be expressed in terms of entropy as

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(X;Y)=H​(X)+H​(Y)−H​(X,Y)I(X;Y)=H(X)+H(Y)-H(X,Y) |  | (24) |

where H​(X)H(X) and H​(Y)H(Y) are marginal entropies and H​(X,Y)H(X,Y) is joint entropy.

In this study, we used a histogram-based estimator with nbins=16n\_{\text{bins}}=16 bins hacine2013new

|  |  |  |  |
| --- | --- | --- | --- |
|  | I^​(X;Y)=∑k=1nbins∑l=1nbinsp^k​l​log⁡(p^k​lp^k​p^l),\hat{I}(X;Y)=\sum\_{k=1}^{n\_{\text{bins}}}\sum\_{l=1}^{n\_{\text{bins}}}\hat{p}\_{kl}\log\left(\frac{\hat{p}\_{kl}}{\hat{p}\_{k}\hat{p}\_{l}}\right), |  | (25) |

where, p^​k​l=n​k​lN\hat{p}{kl}=\frac{n{kl}}{N} represent empirical joint probability, p^​k=∑l=1nbins​p^​k​l\hat{p}k=\sum{l=1}^{n\_{\text{bins}}}\hat{p}{kl} is the empirical marginal probability of XX, p^​l=∑k=1n​bins​p^​k​l\hat{p}l=\sum{k=1}^{n{\text{bins}}}\hat{p}{kl} is empirical marginal probability of YY, n​k​ln{kl} represent the number of observations in bin (k,l)(k,l),and NN is the total number of observations.

The bin boundaries are determined using equidistant binning over the range of observed values. This non-parametric estimator is consistent and converges to the true MI as N→∞N\to\infty.

#### 2.2.4 Significance Testing: Permutation Test

To distinguish statistically significant dependencies from random noise, we employ a non-parametric permutation test that makes minimal distributional assumptions good2005permutation.

The hypothesis framework is:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | H0\displaystyle H\_{0} | :I​(a​ri;a​rj)=0H1\displaystyle:I(ar\_{i};ar\_{j})=0\quad H\_{1} | :I​(a​ri;a​rj)>0\displaystyle:I(ar\_{i};ar\_{j})>0 |  | (26) |

For each stock pair (i,j)(i,j), the testing procedure is:

1. 1.

   Compute observed MI on abnormal returns:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Iobs=I^​(a​ri;a​rj)I\_{\text{obs}}=\hat{I}(ar\_{i};ar\_{j}) |  | (27) |
2. 2.

   Generate Nperm=100N\_{\text{perm}}=100 permuted samples by randomly shuffling one time series:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | a​ri(1),a​ri(2),…,a​ri(Nperm)∼Permutation​(a​ri){ar\_{i}^{(1)},ar\_{i}^{(2)},\ldots,ar\_{i}^{(N\_{\text{perm}})}}\sim\text{Permutation}(ar\_{i}) |  | (28) |
3. 3.

   Compute MI for each permuted sample:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Iperm(k)=I^​(a​ri(k);a​rj),k=1,…,NpermI\_{\text{perm}}^{(k)}=\hat{I}(ar\_{i}^{(k)};ar\_{j}),\quad k=1,\ldots,N\_{\text{perm}} |  | (29) |
4. 4.

   Calculate the empirical p-value:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | p=|k:Iperm(k)≥Iobs|+1Nperm+1p=\frac{\left|{k:I\_{\text{perm}}^{(k)}\geq I\_{\text{obs}}}\right|+1}{N\_{\text{perm}}+1} |  | (30) |

We reject H0H\_{0} at significance level α=0.05\alpha=0.05 if p≤αp\leq\alpha.

#### 2.2.5 Conditional P-Thresholded MI Matrix

The conditional p-threshold mutual information matrix
M​I=[m​ii​j]N×NMI=[mi\_{ij}]\_{N\times N} is constructed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | m​ii​j={I^​(a​ri;a​rj),if ​pi​j≤α,0,otherwise,mi\_{ij}=\begin{cases}\hat{I}(ar\_{i};ar\_{j}),&\text{if }p\_{ij}\leq\alpha,\\ 0,&\text{otherwise},\end{cases} |  | (31) |

where pi​jp\_{ij} denotes the permutation test pp-value for stocks ii and jj and α=0.05\alpha=0.05 is the significance level. In this study, the conditional p-thresholded MI matrix is used to construct the heatmap, which helps us to direct comparison between the unconditional MI and the conditional p-thresholded MI.

#### 2.2.6 Transformation to Distance Matrix

For network construction, the MI matrix is transformed into a distance matrix using a monotonic mapping that preserves the dependency structure.

The distance matrix D=[di​j]N×ND=[d\_{ij}]\_{N\times N} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | di​j={1m​ii​j+ϵ,if ​m​ii​j≠0,∞,if ​m​ii​j=0,d\_{ij}=\begin{cases}\dfrac{1}{mi\_{ij}+\epsilon},&\text{if }mi\_{ij}\neq 0,\\ \infty,&\text{if }mi\_{ij}=0,\end{cases} |  | (32) |

where ϵ=10−9\epsilon=10^{-9} is a small constant introduced for numerical stability.

The distance metric satisfies the following properties:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | di​j\displaystyle d\_{ij} | ≥0,\displaystyle\geq 0, |  | (33) |
|  | di​j\displaystyle d\_{ij} | =dj​i,\displaystyle=d\_{ji}, |  |
|  | di​j\displaystyle d\_{ij} | =0⇔i=j.\displaystyle=0\iff i=j. |  |

This distance formulation provides a suitable basis for MST construction, where smaller distances correspond to stronger dependencies.

#### 2.2.7 Minimum Spanning Tree

From the distance matrix DD, we construct an undirected weighted graph G=(V,E,W)G=(V,E,W) representing the stock dependency network, where V=v1,v2,…,vNV={v\_{1},v\_{2},\ldots,v\_{N}} represents the set of nodes, each corresponding to an individual stock. The edge set EE consists of all pairs (vi,vj)(v\_{i},v\_{j}) for which the distance di​jd\_{ij} is finite, indicating statistically significant dependencies between stocks. The weight set WW assigns to each edge (vi,vj)∈E(v\_{i},v\_{j})\in E a weight wi​j=di​jw\_{ij}=d\_{ij}, representing the transformed distance between the corresponding stock pair.

The graph GG may contain multiple connected components. In this study, we focus on the largest connected component to ensure network coherence.

|  |  |  |  |
| --- | --- | --- | --- |
|  | GLCC=(VLCC,ELCC,WLCC),where ​VLCC=arg⁡maxC⊆V,C∈𝒞​(G)⁡|C|.G\_{\text{LCC}}=(V\_{\text{LCC}},E\_{\text{LCC}},W\_{\text{LCC}}),\quad\text{where }V\_{\text{LCC}}=\arg\max\_{C\subseteq V,\,C\in\mathcal{C}(G)}|C|. |  | (34) |

The Minimum Spanning Tree (MST) mantegna1999hierarchical is extracted from GLCCG\_{\text{LCC}} using Prim’s algorithm dutta2014development, huda2023modified, which iteratively selects the edge with the smallest weight that connects a new node to the growing tree. This procedure ensures that all nodes in the largest connected component are spanned while minimizing the total sum of edge weights. As a result, the MST provides a sparse representation of the stock dependency network that preserves the strongest inter-stock dependencies and removes redundant connections.

Algorithm 1  Prim’s Algorithm for MST Construction

0: Connected graph G=(V,E,W)G=(V,E,W) with n=|V|n=|V| nodes

0: Minimum Spanning Tree T=(V,ET)T=(V,E\_{T})

1: Initialize ET←∅E\_{T}\leftarrow\emptyset

2: Initialize U←{v1}U\leftarrow\{v\_{1}\} (arbitrary starting node)

3: Initialize min-priority queue QQ with all edges from v1v\_{1}

4: for i=2i=2 to nn do

5:  Extract edge (u,v)(u,v) with minimum wu​vw\_{uv} from QQ where u∈Uu\in U, v∉Uv\notin U

6:  ET←ET∪{(u,v)}E\_{T}\leftarrow E\_{T}\cup\{(u,v)\}

7:  U←U∪{v}U\leftarrow U\cup\{v\}

8:  Add all edges from vv to nodes not in UU to QQ

9: end for

10: return T=(V,ET)T=(V,E\_{T})

The optimization is subject to the constraints that TT forms a tree (connected and acyclic), spans all nodes in VLCCV\_{\text{LCC}}, and has the minimum total edge weight among all possible spanning trees. This construction yields a hierarchical backbone that captures the essential dependency structure while filtering out weaker connections. Based on the resulting conditional p-threshold MST, we compute a comprehensive set of network topological metrics to quantify the structural properties and hierarchical organization of the stock dependency network across different market periods.

### 2.3 Topological features of the network

To characterize the network structure in each market period, we compute topological features on the MST. This sparse representation, extracted from the largest connected component of the conditional p-threshold MI network, preserves the strongest dependencies while ensuring a connected, acyclic structure for robust analysis.

#### 2.3.1 Average Closeness Centrality

Closeness centrality freeman1979centrality quantifies a node’s closeness to all other nodes in the network. It reflects how efficiently a node can access or disseminate information across the network, with higher values indicating a more central and well-connected position.

For a node ii, closeness centrality is defined as the reciprocal of the average shortest-path distance to all other nodes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CC​(i)=N−1∑j≠ili​j,C\_{C}(i)=\frac{N-1}{\sum\_{j\neq i}l\_{ij}}, |  | (35) |

where li​jl\_{ij} denotes the shortest-path length (in terms of number of edges) between nodes ii and jj in the MST, and NN is the total number of nodes in the connected component. The network-level average closeness centrality is then computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨CC⟩=1N​∑i=1NCC​(i).\langle C\_{C}\rangle=\frac{1}{N}\sum\_{i=1}^{N}C\_{C}(i). |  | (36) |

This measure provides insight into the overall integration and potential speed of information propagation within the network.

#### 2.3.2 Average eccentricity

Eccentricity caldarelli2007scale measures the maximum distance from a node to any other node in the network, capturing how peripheral a node is. Higher eccentricity values indicate weaker integration within the network.

The eccentricity of node ii is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ε​(i)=maxj∈V⁡li​j,\varepsilon(i)=\max\_{j\in V}l\_{ij}, |  | (37) |

and the average eccentricity is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ε⟩=1N​∑i=1Nε​(i).\langle\varepsilon\rangle=\frac{1}{N}\sum\_{i=1}^{N}\varepsilon(i). |  | (38) |

#### 2.3.3 Average eigenvector centrality

Eigenvector centrality measures bonacich1991simultaneous the influence of a node by accounting not only for its number of connections but also for the importance of its neighbors. Nodes connected to highly central nodes receive higher scores, capturing hierarchical influence patterns in the network.

Mathematically, the eigenvector centrality of node ii is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | CE​(i)=1λ​∑j=1NAi​j​CE​(j),C\_{E}(i)=\frac{1}{\lambda}\sum\_{j=1}^{N}A\_{ij}C\_{E}(j), |  | (39) |

where Ai​jA\_{ij} is the (weighted) adjacency matrix and λ\lambda is the largest eigenvalue of AA. The network-level average eigenvector centrality is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨CE⟩=1N​∑i=1NCE​(i).\langle C\_{E}\rangle=\frac{1}{N}\sum\_{i=1}^{N}C\_{E}(i). |  | (40) |

#### 2.3.4 Average weighted degree

Weighted degree measures the total strength of connections of a node by accounting for both the number of links and their associated weights. Nodes with higher weighted degree are more strongly connected to the network, reflecting their overall interaction intensity.

Mathematically, the weighted degree of node ii is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ki(w)=∑j=1Nwi​j,k\_{i}^{(w)}=\sum\_{j=1}^{N}w\_{ij}, |  | (41) |

where wi​jw\_{ij} denotes the weight of the edge between nodes ii and jj. The network-level average weighted degree is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨k(w)⟩=1N​∑i=1Nki(w).\langle k^{(w)}\rangle=\frac{1}{N}\sum\_{i=1}^{N}k\_{i}^{(w)}. |  | (42) |

#### 2.3.5 Average betweenness centrality

Betweenness centrality freeman1979centrality quantifies the extent to which a node lies on the shortest paths between other node pairs, reflecting its role as an intermediary or bridge in information transmission. Nodes with high betweenness can significantly influence the propagation of shocks across the network.

For node ii, betweenness centrality is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | CB​(i)=∑m≠n≠iσm​n​(i)σm​n,C\_{B}(i)=\sum\_{m\neq n\neq i}\frac{\sigma\_{mn}(i)}{\sigma\_{mn}}, |  | (43) |

where σm​n\sigma\_{mn} is the total number of shortest paths between nodes mm and nn and σm​n​(i)\sigma\_{mn}(i) is the number of those paths passing through node ii. The average betweenness centrality is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨CB⟩=1N​∑i=1NCB​(i).\langle C\_{B}\rangle=\frac{1}{N}\sum\_{i=1}^{N}C\_{B}(i). |  | (44) |

#### 2.3.6 Average path length

The average path length albert2002statistical measures the typical separation between node pairs in the network. Shorter path lengths imply a more compact and integrated structure.

It is computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | l¯=2N​(N−1)​∑m<nlm​n.\bar{l}=\frac{2}{N(N-1)}\sum\_{m<n}l\_{mn}. |  | (45) |

#### 2.3.7 Global efficiency

Global efficiency latora2001efficient quantifies the overall efficiency of information transfer in the network by accounting for inverse shortest path lengths. Higher values indicate faster diffusion of information across the system.

It is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Eglob=1N​(N−1)​∑i≠j1li​j.E\_{\text{glob}}=\frac{1}{N(N-1)}\sum\_{i\neq j}\frac{1}{l\_{ij}}. |  | (46) |

#### 2.3.8 Assortativity

Assortativity newman2003mixing measures the tendency of nodes to connect with other nodes of similar degree. In financial networks, negative assortativity typically indicates a core–periphery structure, where highly connected core nodes preferentially link to weakly connected peripheral nodes.

For an undirected network, the degree assortativity coefficient rr is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | r=∑i,jAi​j​ki​kj−12​m​(∑iki2)2∑iki3−12​m​(∑iki2)2,r=\frac{\sum\_{i,j}A\_{ij}k\_{i}k\_{j}-\frac{1}{2m}\left(\sum\_{i}k\_{i}^{2}\right)^{2}}{\sum\_{i}k\_{i}^{3}-\frac{1}{2m}\left(\sum\_{i}k\_{i}^{2}\right)^{2}}, |  | (47) |

where Ai​jA\_{ij} denotes the binary adjacency matrix of the minimum spanning tree (MST), with Ai​j=1A\_{ij}=1 if nodes ii and jj are directly connected and Ai​j=0A\_{ij}=0 otherwise; kik\_{i} is the degree of node ii; and mm is the total number of edges in the MST (m=N−1m=N-1 for a tree with NN nodes).

The assortativity coefficient satisfies −1≤r≤1-1\leq r\leq 1. Positive values indicate assortative mixing, where nodes preferentially connect to others with similar degree, while negative values indicate disassortative mixing, where highly connected nodes tend to link with low-degree nodes. Values close to zero imply weak or no degree of correlation. In MST-based stock networks, strongly negative rr values reflect a pronounced core–periphery topology, a characteristic feature of financial markets during periods of stress.

#### 2.3.9 Algebraic connectivity

Algebraic connectivity fiedler1973algebraic, denoted by λ2\lambda\_{2}, is defined as the second smallest eigenvalue of the weighted graph Laplacian matrix Lw=Dw−AwL\_{w}=D\_{w}-A\_{w}, where Aw​(i,j)=wi​jA\_{w}(i,j)=w\_{ij} is the weighted adjacency matrix and Dw​(i,i)=∑jwi​jD\_{w}(i,i)=\sum\_{j}w\_{ij} is the weighted degree matrix. It can be equivalently expressed through the Rayleigh quotient as

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ2=minx≠0x⟂𝟏⁡xT​Lw​xxT​x.\lambda\_{2}=\min\_{\begin{subarray}{c}x\neq 0\\ x\perp\mathbf{1}\end{subarray}}\frac{x^{T}L\_{w}x}{x^{T}x}. |  | (48) |

For the MST constructed from conditional pp-threshold mutual information, the edge weights are defined as distances wi​j=di​j=1/(m​ii​j+ϵ)w\_{ij}=d\_{ij}=1/(mi\_{ij}+\epsilon). Higher values of λ2\lambda\_{2} indicate stronger network cohesion and robustness, whereas lower values reflect increased structural fragility.

#### 2.3.10 Tree length

The tree length corresponds to the total distance of edges in the minimum spanning tree (MST) mantegna1999hierarchical, representing the backbone of the network. Shorter tree length implies stronger overall connectivity.

It is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ltree=∑(i,j)∈Tdi​j.L\_{\text{tree}}=\sum\_{(i,j)\in T}d\_{ij}. |  | (49) |

### 2.4 Core–Periphery Analysis

Core–periphery analysis provides a compact representation of market organization by distinguishing a densely connected core of influential stocks from a sparsely connected periphery of weaker stocks borgatti2000models, ansari2025uncovering, ansari2025comprehensive. In financial networks, core stocks typically correspond to large, systemically important firms that exert broad influence on market dynamics. The following measures quantify the structural concentration and fragility of the network.

#### 2.4.1 Core Concentration (Eigenvector–Closeness Ratio)

We introduce a ratio-based measure of core concentration defined as the ratio of the network-average eigenvector centrality to the network-average closeness centrality,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ccore=⟨CE⟩⟨CC⟩,C\_{\text{core}}=\frac{\langle C\_{E}\rangle}{\langle C\_{C}\rangle}, |  | (50) |

where ⟨CE⟩\langle C\_{E}\rangle and ⟨CC⟩\langle C\_{C}\rangle denote the average eigenvector and closeness centralities, respectively.

This ratio captures the relative strength of core influence compared to overall network integration. Eigenvector centrality reflects the concentration of influence through connections to highly influential nodes, thereby serving as a proxy for core dominance, while closeness centrality measures the efficiency of global connectivity and the degree of peripheral integration. Higher values of CcoreC\_{\text{core}} indicate that influence is more strongly concentrated within central nodes relative to the level of network-wide integration, consistent with a segmented core–periphery structure. Conversely, lower values suggest a more distributed influence pattern accompanied by higher integration, corresponding to a flatter and more homogeneous network hierarchy. Temporal increases in the ratio signal a strengthening of core dominance that outpaces gains in global integration, whereas decreases indicate a diffusion of core influence as the network becomes more uniformly connected.

#### 2.4.2 Periphery Fragility

Periphery fragility quantifies the vulnerability of the network’s peripheral structure. It is computed as the ratio of the absolute assortativity to algebraic connectivity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fperi=|r|λ2F\_{\text{peri}}=\frac{|r|}{\lambda\_{2}} |  | (51) |

where:

* 1.

  |r||r| is the absolute value of the assortativity coefficient newman2003mixing, which measures the tendency of nodes to connect with similar nodes. In core-periphery structures, rr is typically negative (core nodes connect to peripheral nodes), so |r||r| captures the strength of this disassortative mixing.
* 2.

  λ2\lambda\_{2} is the algebraic connectivity (second smallest eigenvalue of the Laplacian), which measures the overall robustness of the network Fiedler1973.

This ratio captures the trade-off between structural segregation (high |r||r|) and network robustness (high λ2\lambda\_{2}). Higher values indicate greater fragility, where strong core-periphery segregation coexists with weak overall connectivity. While the individual components assortativity and algebraic connectivity are well-established network metrics newman2003mixing, Fiedler1973, their combination into a fragility index specifically for financial network peripheries represents a methodological contribution of this study for assessing systemic vulnerability during market stress.

### 2.5 Gutenberg–Richter Power Law

The Gutenberg–Richter (GR) power law is a classical empirical relation in geophysics describing the statistical distribution of earthquake magnitudes gutenberg1942earthquake. It relates the cumulative number of events N​(M)N(M) with magnitude greater than or equal to MM to the magnitude itself and is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | log10⁡N​(M)=a−b​M,\log\_{10}N(M)=a-bM, |  | (52) |

where aa and bb are positive constants and bb represents the slope of the scaling relation.

In financial markets, the GR framework has been adapted to examine aftershock-like volatility dynamics following major market crashes siokis2012stock, selccuk2004financial. In this study, the market crash is treated as an exogenous mainshock and the analysis is restricted to the post-crash period. The magnitude MM of an aftershock event is defined as the absolute logarithmic price difference between consecutive local peaks and troughs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mi=|log10⁡(Ppeak,i)−log10⁡(Ptrough,i)|,M\_{i}=\left|\log\_{10}(P\_{\text{peak},i})-\log\_{10}(P\_{\text{trough},i})\right|, |  | (53) |

where Ppeak,iP\_{\text{peak},i} and Ptrough,iP\_{\text{trough},i} denote adjacent local maxima and minima in the closing price series. This extremum-based definition captures discrete post-crash volatility fluctuations without imposing arbitrary thresholds.

The parameter bb characterizes the scaling behavior of post-crash volatility events. Larger values of bb indicate a faster decay in the frequency of large-magnitude fluctuations, while smaller values suggest a relatively higher occurrence of large volatility events. The intercept aa reflects the overall number of post-crash events and is independent of their magnitude distribution.

## 3 Data Description

We analyze the top 200 stocks by market capitalization from each of the QUAD countries, the United States, Japan, Australia, and India, to examine the evolution of nonlinear dependencies during the COVID-19 market crash. Daily closing price data for the period spanning September 1, 2019, to July 15, 2020, were obtained via the yfinance Python library from Yahoo Finance yahoofinance. This interval encompasses the pre-crash, crash, and post-crash periods of the COVID-19-induced financial crisis, providing a natural stress environment to study how stock-specific dependencies reorganize under extreme market conditions after filtering out common market factors.

For each market, the constituent stocks of the respective benchmark index, S&P 500 (USA), NIKKEI 225 (Japan), ASX 200 (Australia), and NIFTY 50 (India), served as the initial set. From these, the 200 largest companies by average market capitalization over the sample period were selected to ensure liquidity and market representativeness. Daily closing prices were chosen for their stability and wide adoption in financial network analysis, and were transformed into logarithmic returns for subsequent analysis. The selection of QUAD countries provides a strategically diverse sample, with diverse economies across distinct geographical regions. This heterogeneity allows us to test whether the topological signatures of crisis identified by our conditional p-threshold MI framework represent universal patterns of systemic stress.

## 4 Results and Discussion

This section presents and discusses the empirical findings of our study, organized as follows. First, Section [4.1](https://arxiv.org/html/2601.00395v1#S4.SS1 "4.1 Market Crash Detection and Characterization ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") identifies and characterizes the COVID-19 market crash using the HD and HS, respectively, dividing the data into pre-crash, crash, and post-crash periods. Next, Section [4.2](https://arxiv.org/html/2601.00395v1#S4.SS2 "4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") compares MI with the conditional p-threshold MI, demonstrating the importance of removing market-wide effects and applying statistical filtering. Section [4.3](https://arxiv.org/html/2601.00395v1#S4.SS3 "4.3 Conditional P-Threshold Network Dynamics ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") then examines the topological evolution of the conditional p-threshold MI networks across the three periods, with particular focus on core–periphery reconfiguration. Section [5.1](https://arxiv.org/html/2601.00395v1#S5.SS1 "5.1 Aftershock in the Stock Market ‣ 5 Community Structure of Stock Market Networks ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") investigates post-crash aftershock dynamics using the GR law. Finally, Section [6](https://arxiv.org/html/2601.00395v1#S6 "6 Conclusion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") presents the conclusions of the study and outlines directions for future research.

### 4.1 Market Crash Detection and Characterization

In this section, we employ two complementary methodologies to identify and characterize market crashes across the QUAD countries during the COVID-19 period.
We first detect crash periods using a rolling HD. This HD method captures structural changes in the cross-sectional return distributions of groups of stocks. We then characterize the dynamic behavior of the market during these periods using the HS applied to the benchmark stock indices of the QUAD countries. Together, these approaches provide a robust method for detecting the COVID-19 market crash.

#### 4.1.1 Crash detection using Hellinger Distance

We identify the timing of the COVID-19-induced stock market crash of the QUAD countries, namely, the United States, Japan, Australia, and India, using the rolling HD as described in the Section [2.1.1](https://arxiv.org/html/2601.00395v1#S2.SS1.SSS1 "2.1.1 Hellinger-Distance ‣ 2.1 Crash detection ‣ 2 Method of Analysis ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"). The HD provides a distribution-based measure of market instability by quantifying the divergence between two probability distributions. Unlike pointwise measures of volatility or correlation, it captures changes in the entire cross-sectional return distribution, making it particularly suitable for detecting systemic structural breaks in financial markets. The HD at time tt measures the divergence between the cross-sectional distribution of stock returns constructed from a rolling historical window (t−60,…,t−1)(t-60,\dots,t-1) and the cross-sectional return distribution observed on day tt. A sudden increase in HD reflects an abrupt redistribution of returns across stocks, indicating heightened dispersion and synchronized extreme movements. Such behavior is characteristic of market crash periods, during which the normal cross-sectional market structure breaks down due to systemic shocks.

![Refer to caption](US_Hill_group.png)


(a) US Stocks

![Refer to caption](Japan_Hill_group.png)


(b)  Japan Stocks

![Refer to caption](Aus_hill_group.png)


(c) Australia Stocks

![Refer to caption](India_group_Hil.png)


(d) India Stocks

Figure 1: 
Rolling Hellinger distance(HD) for the top 100 market-capitalization stocks from the QUAD countries. The x-axis represents time, while the y-axis shows the HD. The red dashed line indicates the 2​σ2\sigma threshold (HD=μH+2​σHH\_{D}=\mu\_{H}+2\sigma\_{H}), with the green rectangular box showing the period when HD exceeds this threshold. Plot (a) shows the HD for 100 U.S. stocks, Plot (b) for 100 Japanese stocks, Plot (c) for 100 Australian stocks, and Plot (d) for 100 Indian stocks. All four markets exhibit a pronounced and synchronized increase in HD during February–March 2020, indicating a systemic breakdown in cross-sectional market structure, which represents the COVID-19 market crash.

Fig. [1](https://arxiv.org/html/2601.00395v1#S4.F1 "Figure 1 ‣ 4.1.1 Crash detection using Hellinger Distance ‣ 4.1 Market Crash Detection and Characterization ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") shows the rolling HD for groups of stocks across the QUAD countries. The x-axis represents time, while the y-axis denotes the magnitude of the HD.
Figs. [1(a)](https://arxiv.org/html/2601.00395v1#S4.F1.sf1 "In Figure 1 ‣ 4.1.1 Crash detection using Hellinger Distance ‣ 4.1 Market Crash Detection and Characterization ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), [1(b)](https://arxiv.org/html/2601.00395v1#S4.F1.sf2 "In Figure 1 ‣ 4.1.1 Crash detection using Hellinger Distance ‣ 4.1 Market Crash Detection and Characterization ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), [1(c)](https://arxiv.org/html/2601.00395v1#S4.F1.sf3 "In Figure 1 ‣ 4.1.1 Crash detection using Hellinger Distance ‣ 4.1 Market Crash Detection and Characterization ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") and [1(d)](https://arxiv.org/html/2601.00395v1#S4.F1.sf4 "In Figure 1 ‣ 4.1.1 Crash detection using Hellinger Distance ‣ 4.1 Market Crash Detection and Characterization ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") show the HD calculated from the top 100 market-capitalization stocks of the U.S., Japan, Australia, and Indian stock markets, respectively. To identify crash periods, we define a threshold as HD=μH+2​σHH\_{D}=\mu\_{H}+2\sigma\_{H}, where μH\mu\_{H} and σH\sigma\_{H} denote the mean and standard deviation of the rolling HD, respectively. The time interval during which the HD exceeds this threshold is classified as a market crash period. From Fig. [1](https://arxiv.org/html/2601.00395v1#S4.F1 "Figure 1 ‣ 4.1.1 Crash detection using Hellinger Distance ‣ 4.1 Market Crash Detection and Characterization ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), we see a pronounced spike in the HD values crossing the threshold during February–March 2020. This spike region is highlighted by the green rectangular box. Hence, we conclude that the HD method successfully detects the COVID-19 stock market crash across all QUAD countries. This synchronized threshold crossing indicates a sudden and statistically significant change in the cross-sectional return distributions of stocks across all markets. The peaks during this interval reflect a breakdown of normal market structure, characterized by increased return dispersion and collective extreme movements among stocks. Based on these threshold crossings, we divide the time series data into three periods: a pre-crash period, defined as the interval before HD exceeds the threshold; a crash period, defined as the interval during which HD remains above the threshold; and a post-crash period, defined as the interval after HD falls back below the threshold. This data-driven segmentation ensures a consistent event window for subsequent analysis and allows for a systematic comparison of market structure before, during, and after the crash

#### 4.1.2 Crash characterization using the Hilbert Spectrum

The rolling HD provides a robust, data-driven identification of the timing and duration of systemic market disruptions by detecting abrupt changes in cross-sectional return distributions. However, while HD effectively signals when a market-wide structural break occurs, it does not describe the internal temporal dynamics of the market during the crash period. In particular, it does not capture how the intensity, frequency and persistence of market fluctuations evolve over time. Crucially, the HD cannot distinguish between a single day of extreme dislocation and a sustained period of chaotic, high-amplitude oscillations; both would manifest as a high HD value. To characterize this internal market dynamics and to further validate the crash period identified by the HD, we employ the HHT on the benchmark stock market indices of the QUAD countries, namely S&P 500, NIKKEI 225, ASX 200 and NIFTY 50 indices. The key advantage of the HS in this context is its ability to reveal the time-varying persistence and spectral composition of extreme movements. While the HD indicates a break in the cross-sectional structure, the HS quantifies whether that break corresponds to transient volatility or a prolonged regime of high-energy, chaotic market states.

![Refer to caption](USA_index.png)


(a) S&P 500 Index

![Refer to caption](Japan_index.png)


(b) NIKKEI 225 Index

![Refer to caption](Aus_indx.png)


(c) ASX 200 Index

![Refer to caption](India_indx.png)


(d) NIFTY 50 Index

Figure 2: 
Hilbert spectrum in the top panels and normalized instantaneous energy in the bottom panels of benchmark stock market indices for the QUAD countries. Plots (a), (b), (c), and (d) represent the HS of the S&P 500 Index (USA), NIKKEI 225 Index (Japan), ASX 200 Index (Australia), and the NIFTY 50 Index (India), respectively. The x-axis represents time, while the y-axis in each subplot of the upper plot denotes the instantaneous frequency. In the lower plots, the y-axis represents the normalized instantaneous energy. A pronounced concentration of high-energy components is observed during Feb-Mar 2020 in all four indices, indicating heightened market volatility during the COVID-19 market crash.

Fig. [2](https://arxiv.org/html/2601.00395v1#S4.F2 "Figure 2 ‣ 4.1.2 Crash characterization using the Hilbert Spectrum ‣ 4.1 Market Crash Detection and Characterization ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") presents the HS and the corresponding normalized instantaneous energy for the S&P 500, NIKKEI 225, ASX 200, and NIFTY 50 indices. In each plot, the
x-axis denotes time, while the color intensity represents the magnitude of instantaneous energy. Across all four stock indices, a pronounced concentration of high instantaneous energy appears during the February–March 2020 period. This period coincides exactly with the crash period identified by the HD-based method. These high-energy regions, visible as intense red patches in the HS, indicate large-amplitude oscillations in the stocks. The normalized instantaneous energy further shows a sharp increase over this period, confirming the crash. The simultaneous energy surges across geographically distinct markets underscore the global and synchronized nature of the shock. Using the crash window identified from the HS and HD analyses, the data were divided into three periods: pre-crash (01-11-2019–14-02-2020), crash (15-02-2020–25-03-2020), and post-crash (26-03-2020–15-07-2020).

Using both HD and HS, we reliably identify the COVID-19 market crash. HD detects the onset and duration of the crash by capturing statistically significant shifts in the cross-sectional return distribution, indicating systemic structural change. HS then confirms this period by measuring the intensity and persistence of market fluctuations through instantaneous energy dynamics, confirming a sustained high-energy market state. Together, these methods provide a robust identification and characterization of the COVID-19 crash, forming a basis for subsequent network-based analysis.

### 4.2 Comparison between the MI and Condition P-threshold MI

Fig. [3](https://arxiv.org/html/2601.00395v1#S4.F3 "Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") shows the heatmap of the MI and conditional p-threshold MI among the top 25 stocks of the U.S. stock market across the pre-crash, crash, and post-crash periods using the method as described in Section[2.2.5](https://arxiv.org/html/2601.00395v1#S2.SS2.SSS5 "2.2.5 Conditional P-Thresholded MI Matrix ‣ 2.2 Methodology for Network Construction: Conditional P-Threshold Mutual Information ‣ 2 Method of Analysis ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"). In these figures, the color spectrum represents the magnitude of MI. Darker shades of red indicate stronger nonlinear dependence between stock pairs, while lighter shades correspond to weaker dependence. Figs. [3(a)](https://arxiv.org/html/2601.00395v1#S4.F3.sf1 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), [3(b)](https://arxiv.org/html/2601.00395v1#S4.F3.sf2 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), and [3(c)](https://arxiv.org/html/2601.00395v1#S4.F3.sf3 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") present the MI heatmaps calculated directly from stock returns, while Figs. [3(d)](https://arxiv.org/html/2601.00395v1#S4.F3.sf4 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), [3(e)](https://arxiv.org/html/2601.00395v1#S4.F3.sf5 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), and [3(f)](https://arxiv.org/html/2601.00395v1#S4.F3.sf6 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") show the residual-based, significance-filtered MI matrices obtained after removing the market index effect and computing MI, followed by the application of the conditional p-threshold at α=0.05\alpha=0.05. The significance testing is carried out using a permutation-based procedure with 100 permutations per stock pair to retain only statistically meaningful nonlinear dependencies.

From Figs. [3(a)](https://arxiv.org/html/2601.00395v1#S4.F3.sf1 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), [3(b)](https://arxiv.org/html/2601.00395v1#S4.F3.sf2 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), and [3(c)](https://arxiv.org/html/2601.00395v1#S4.F3.sf3 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), dense MI connectivity is observed across all three periods. The heatmap corresponding to the crash period, as shown in Fig. [3(b)](https://arxiv.org/html/2601.00395v1#S4.F3.sf2 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), exhibits the highest intensity compared to the pre-crash and post-crash periods, indicating stronger nonlinear dependence during the crash. This suggests enhanced market-wide synchronization driven by common shocks. However, similar to correlation-based measures, MI is also sensitive to overall market movements, and such dense connectivity may reflect a combination of direct stock–stock interactions and indirect dependencies induced by common market factors. Therefore, the removal of these common factors is necessary to analyze the pure relationships between stocks.

![Refer to caption](USA_Pre-Crash_RawMI.png)


(a) Pre-Crash (MI)

![Refer to caption](USA_Crash_RawMI.png)


(b) Crash (MI)

![Refer to caption](USA_Post-Crash_RawMI.png)


(c) Post-Crash (MI)

![Refer to caption](USA_Pre-Crash_ResidualSigMI.png)


(d) Pre-Crash (Cond. P-threshold MI)

![Refer to caption](USA_Crash_ResidualSigMI.png)


(e) Crash (Cond. P-threshold MI)

![Refer to caption](USA_Post-Crash_ResidualSigMI.png)


(f) Post-Crash (Cond. P-threshold MI)

Figure 3: Mutual information heatmaps for the 25 largest U.S. stocks across different market regimes. Plot (a)–(c) shows mutual information heatmaps, which are dominated by common market effects and display dense connectivity, especially during the crash. Plot (d)–(f) presents residual-based, significance-filtered MI heatmaps obtained using the conditional P-threshold method. The conditional P-threshold MI heatmaps show a sparse structure, indicating the true nonlinear dependencies between stocks after removing the market effect, which reveals the underlying direct interactions among stocks.

To identify purely dependent stock pairs, it is necessary to examine the effect of removing the influence of the market index xu2017topological. This allows us to uncover direct nonlinear relationships between stocks. In our analysis, we removed the effect of the S&P 500 market index from each stock of the U.S. After removing the market index effect, the number of significant conditional p-threshold MI links decreased across all groups, as clearly shown in Figs. [3(d)](https://arxiv.org/html/2601.00395v1#S4.F3.sf4 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"),  [3(e)](https://arxiv.org/html/2601.00395v1#S4.F3.sf5 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") and  [3(f)](https://arxiv.org/html/2601.00395v1#S4.F3.sf6 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"). This reduction in the number of significant links suggests that many dependencies identified without conditioning were driven by overall market movements rather than by direct stock–stock relationships. During the pre-crash period, the conditional p-threshold MI heatmap shown in Fig. [3(c)](https://arxiv.org/html/2601.00395v1#S4.F3.sf3 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") appears sparse, indicating that many apparent dependencies are driven by shared market influences rather than intrinsic nonlinear interactions. During the crash period, the heatmap shown in Fig. [3(e)](https://arxiv.org/html/2601.00395v1#S4.F3.sf5 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") exhibits a clear increase in intensity and the number of significant MI values, reflecting stronger nonlinear dependence among stocks under extreme market stress. This demonstrates that the conditional p-threshold approach captures the amplification of genuine nonlinear interdependencies during these periods. In the post-crash period, the heatmap shown in Fig. [3(f)](https://arxiv.org/html/2601.00395v1#S4.F3.sf6 "In Figure 3 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") shows a reduction in overall intensity relative to the crash period, while remaining higher than in the pre-crash period. This ordering,

|  |  |  |  |
| --- | --- | --- | --- |
|  | pre-crash<post-crash<crash,\text{pre-crash}<\text{post-crash}<\text{crash}, |  | (54) |

suggests that although market-wide synchronization weakens after the crash, the system does not immediately return to its pre-crisis state. These results indicate that the aftershock effects and memory effects of the main crash.

![Refer to caption](Japan_Pre-Crash_RawMI.png)


(a) Pre-Crash (MI)

![Refer to caption](Japan_Crash_RawMI.png)


(b) Crash (MI)

![Refer to caption](Japan_Post-Crash_RawMI.png)


(c) Post-Crash (MI)

![Refer to caption](Japan_Pre-Crash_ResidualSigMI.png)


(d) Pre-Crash (Cond. P-threshold MI)

![Refer to caption](Japan_Crash_ResidualSigMI.png)


(e) Crash (Cond. P-threshold MI)

![Refer to caption](Japan_Post-Crash_ResidualSigMI.png)


(f) Post-Crash (Cond. P-threshold MI)

Figure 4: Mutual information heatmaps for the 25 largest Japanese stocks across different market periods. Plot (a)–(c) shows raw mutual information (MI) heatmaps, which are dominated by common market effects and exhibit dense connectivity, particularly during the crash period. Plot (d)–(f) display residual-based, significance-filtered MI heatmaps obtained using the conditional P-threshold MI method, highlighting statistically significant and direct nonlinear dependencies. The conditional P-threshold MI heatmaps show a sparse structure, indicating the true nonlinear dependencies between stocks after removing the market effect, which reveals the underlying direct interactions among stocks.

A similar pattern is observed for the Japanese stock market, as shown in Fig. [4](https://arxiv.org/html/2601.00395v1#S4.F4 "Figure 4 ‣ 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"). The MI heatmaps display dense connectivity across all periods, with a pronounced strengthening during the crash period. After applying the conditional P-threshold MI filtering, the heatmaps become sparse across all periods, with the highest intensity observed during the crash period compared to the pre-crash and post-crash periods. We also observed a consistent behavior for the Australian and Indian stock markets. The corresponding heatmaps for the Australian and Indian stocks are provided in Appendix [9](https://arxiv.org/html/2601.00395v1#Sx2.F9 "Figure 9 ‣ Appendix ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") and Appendix [10](https://arxiv.org/html/2601.00395v1#Sx2.F10 "Figure 10 ‣ Appendix ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), respectively. The same ordering as in Eq. ([54](https://arxiv.org/html/2601.00395v1#S4.E54 "In 4.2 Comparison between the MI and Condition P-threshold MI ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach")), previously observed for the U.S. market in the post-crash period, is preserved for all markets. These indicate the presence of aftershock effects and delayed recovery dynamics.

Overall, these results demonstrate that the conditional p-threshold MI framework robustly isolates statistically significant and direct nonlinear dependencies across different market periods. Unlike MI, which is highly sensitive to market-wide factors, the conditional p-threshold approach provides a refined and economically meaningful representation of market structure. The consistent observation of crash amplification and post-crash aftershock effects across multiple equity markets highlights the suitability of this method for subsequent network construction and for identifying universal features of systemic financial stress.

### 4.3 Conditional P-Threshold Network Dynamics

We first identify statistically significant dependencies among stocks using the conditional p-threshold MI framework. In this approach, the effect of the market index is removed from individual stock returns, and MI is computed between the resulting residuals to capture direct dependencies. The conditional p-threshold plays a central role by retaining only those MI values that are statistically significant, thereby suppressing spurious connections arising from common market-wide movements. Statistical significance is assessed using a permutation-based hypothesis testing procedure, where the null hypothesis corresponds to the absence of dependence between a given stock pair. Only MI values with associated p-values below a prescribed significance level α\alpha are considered meaningful.

The filtered MI matrix obtained from this procedure defines a weighted dependency structure. To construct a sparse and comparable network topology across different market periods, we transform this weighted structure into an MST using a conditional p-threshold MI-based distance measure. The MST extracts the backbone of the conditional P-threshold MI network by retaining the most informative connections while ensuring an identical number of links across periods. All node-level and global topological measures analyzed in this study are computed from these MST networks.

In the primary analysis, we adopt a significance level of α=0.05\alpha=0.05 for constructing the conditional P-threshold MI networks. To examine robustness, we repeat the analysis using alternative significance levels of α=0.01\alpha=0.01 and α=0.10\alpha=0.10. As expected, α=0.01\alpha=0.01 thresholds yield fewer statistically significant dependencies, and when the thresholds increase to α=0.10\alpha=0.10, overall connectivity also increases. The network structure and the relative ordering of topological measures across the pre-crash, crash, and post-crash periods remain consistent across different significance levels. Therefore, α=0.05\alpha=0.05 is selected as an optimal balance between statistical reliability and network interpretability for subsequent analysis.

#### 4.3.1 Rank-Ordered Distributions of Network Metrics

![Refer to caption](MI_MST_closeness_USA_log.png)


(a) Closeness

![Refer to caption](MI_MST_eccentricity_USA_log.png)


(b) Eccentricity

![Refer to caption](MI_MST_eigenvector_USA_log.png)


(c) Eigenvector Centrality

![Refer to caption](MI_MST_weighted_degree_USA_log.png)


(d) Weighted Degree

Figure 5: 
Rank-ordered distributions of MST-based network metrics for the U.S. stock market across pre-crash, crash, and post-crash periods. Plot (a) represents closeness, Plot (b) eccentricity, Plot (c) eigenvector centrality and Plot (d) weighted degree. Stocks are ranked in ascending order for each metric. The curves correspond to the three market periods, highlighting structural reorganization and centralization during the crash period.

Figs [5](https://arxiv.org/html/2601.00395v1#S4.F5 "Figure 5 ‣ 4.3.1 Rank-Ordered Distributions of Network Metrics ‣ 4.3 Conditional P-Threshold Network Dynamics ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), [6](https://arxiv.org/html/2601.00395v1#S4.F6 "Figure 6 ‣ 4.3.1 Rank-Ordered Distributions of Network Metrics ‣ 4.3 Conditional P-Threshold Network Dynamics ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), [11](https://arxiv.org/html/2601.00395v1#Sx2.F11 "Figure 11 ‣ Appendix ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") and [12](https://arxiv.org/html/2601.00395v1#Sx2.F12 "Figure 12 ‣ Appendix ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") present the rank-ordered distributions of MST-based network metrics: closeness, eccentricity, eigenvector centrality, and weighted degree, derived from the conditional p-threshold MI-MST framework. These network metrics are computed from the sparse, statistically validated adjacency matrices that capture only direct stock-stock dependencies after removing market-wide co-movement. This methodological framework allows us to isolate genuine structural reconfiguration during crises, separating it from the common-factor-driven synchronization that dominates raw correlation or mutual information measures. Across all markets, the rank-ordered plots clearly distinguish the three market periods: pre-crash, crash and post-crash. The crash period consistently exhibits the most pronounced deviation from both pre- and post-crash periods, indicating a fundamental and systematic reorganization of the underlying network structure during the crash. This clear separation across periods, observable in all four QUAD markets, validates the sensitivity and robustness of our conditional p-threshold MI approach in detecting crisis-induced structural changes.

For the U.S. stock market, Fig. [5(a)](https://arxiv.org/html/2601.00395v1#S4.F5.sf1 "In Figure 5 ‣ 4.3.1 Rank-Ordered Distributions of Network Metrics ‣ 4.3 Conditional P-Threshold Network Dynamics ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") shows that closeness centrality, which measures how rapidly shocks can propagate through the network, increases significantly during the crash period. This increase, revealed by our filtered network, reflects a contraction of effective network distances and implies faster potential transmission of shocks during a market crash. Similarly, eigenvector centrality and weighted degree, as shown in Figs. [5(c)](https://arxiv.org/html/2601.00395v1#S4.F5.sf3 "In Figure 5 ‣ 4.3.1 Rank-Ordered Distributions of Network Metrics ‣ 4.3 Conditional P-Threshold Network Dynamics ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") and [5(d)](https://arxiv.org/html/2601.00395v1#S4.F5.sf4 "In Figure 5 ‣ 4.3.1 Rank-Ordered Distributions of Network Metrics ‣ 4.3 Conditional P-Threshold Network Dynamics ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), exhibit elevated values during the crash, indicating that dependence becomes more concentrated around a subset of influential stocks. Eccentricity, defined as the maximum shortest-path distance from a stock to any other stock in the network, decreases during the crash, reflecting network compression and increased synchronization. Importantly, these patterns emerge after removing market effects, suggesting they represent genuine changes in the fabric of stock interdependencies rather than mere reflections of common factor exposure. Following the crash, the post-crash distributions shift back toward pre-crash patterns but do not fully overlap, indicating that the market does not immediately return to its original structural state. This difference reveals persistent aftershock effects, whereby the impact of the crash continues to influence network connectivity beyond the immediate crash period. A similar systematic pattern is observed in the Japanese, Indian, and Australian markets, characterized by a crash deviation followed by partial post-crash recovery, demonstrating the universal applicability of our method.

![Refer to caption](MI_MST_closeness_Japan_log.png)


(a) Closeness

![Refer to caption](MI_MST_eccentricity_Japan_log.png)


(b) Eccentricity

![Refer to caption](MI_MST_eigenvector_Japan_log.png)


(c) Eigenvector Centrality

![Refer to caption](MI_MST_weighted_degree_Japan_log.png)


(d) Weighted Degree

Figure 6: 
Rank-ordered distributions of MST-based network metrics for the Japan stock market across pre-crash, crash, and post-crash periods. Plot (a) represents closeness, Plot (b) eccentricity, Plot (c) eigenvector centrality and Plot (d) weighted degree. Stocks are ranked in ascending order for each metric. The curves correspond to the three market periods, highlighting structural reorganization and centralization during the crash period.

The consistency of these findings across geographically and economically distinct markets underscores the robustness of the conditional p-threshold MI framework. By filtering out common factors and emphasizing statistically validated nonlinear relationships, our approach provides a clearer and more reliable representation of how stock-specific interactions reorganize during periods of financial crash. The universal detection of network compression, increased centrality concentration, and persistent aftershocks across all QUAD markets confirms that our method captures fundamental aspects of market reconfiguration that are obscured by traditional correlation-based or unfiltered MI measures. In Section [5.1](https://arxiv.org/html/2601.00395v1#S5.SS1 "5.1 Aftershock in the Stock Market ‣ 5 Community Structure of Stock Market Networks ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"), we further investigate these post-crash aftershock effects using the GR law, providing additional quantitative support for the observed persistence in network reconfiguration.

#### 4.3.2 Core–Periphery Structure of Stock Market Networks

Table 1: Table represents the core concentration and periphery fragility indices of conditional p-threshold MI–MST networks for QUAD stock markets across pre-crash, crash, and post-crash periods. Core concentration quantifies the dominance of influential stocks, while periphery fragility captures the structural vulnerability of peripheral nodes under market stress.

| Period | Country | Core Concentration | Periphery Fragility |
| --- | --- | --- | --- |
| Pre-Crash | Australia | 0.293 | 87.3 |
| India | 0.247 | 96.4 |
| Japan | 0.215 | 78.0 |
| USA | 0.194 | 64.9 |
| Crash | Australia | 0.168 | 167.5 |
| India | 0.135 | 75.3 |
| Japan | 0.162 | 281.3 |
| USA | 0.164 | 226.5 |
| Post-Crash | Australia | 0.331 | 102.4 |
| India | 0.210 | 101.9 |
| Japan | 0.192 | 100.3 |
| USA | 0.189 | 53.9 |

We further investigate the evolution of market structure during the COVID‑19 crash through the lens of core–periphery organization using the conditional p‑threshold MI–MST framework. The core–periphery structure is quantified by two complementary measures: core concentration, which measures the dominance of a cohesive central set of influential stocks, and periphery fragility, which captures the vulnerability of weakly connected peripheral stocks to shock transmission. Table [1](https://arxiv.org/html/2601.00395v1#S4.T1 "Table 1 ‣ 4.3.2 Core–Periphery Structure of Stock Market Networks ‣ 4.3 Conditional P-Threshold Network Dynamics ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") reports the evolution of both indices across the three periods. A consistent pattern emerges during the crash: core concentration declines sharply in all four markets, indicating a fragmentation of the influential core and a dispersion of network influence. Simultaneously, periphery fragility increases dramatically in the U.S., Japanese, and Australian markets, revealing that peripheral stocks become structurally more exposed and vulnerable to spillovers. The conditional p‑threshold MI framework uniquely captures this dual shift, a weakening core and an increasingly fragile periphery, as a key feature of market topology during a crash. The Indian stock presents a partial exception, with periphery fragility decreasing during the crash, suggesting country‑specific differences in market composition.

The topological factors underlying this reconfiguration are summarized in Table [2](https://arxiv.org/html/2601.00395v1#S4.T2 "Table 2 ‣ 4.3.2 Core–Periphery Structure of Stock Market Networks ‣ 4.3 Conditional P-Threshold Network Dynamics ‣ 4 Results and Discussion ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"). During the crash, all markets show a strong decline in average path length (APL), indicating a more compact and highly integrated network. At the same time, the weighted degree increases, reflecting a rise in statistically significant dependencies among stocks. However, algebraic connectivity (λ2\lambda\_{2}), a measure of network robustness, decreases, suggesting that higher integration is accompanied by greater structural fragility. This contradiction is explained by the strongly negative assortativity observed during the crash. Negative assortativity indicates that core stocks tend to connect with peripheral stocks, making the periphery a key but fragile channel for shock transmission. By removing common market effects, this disassortative structure is clearly revealed and directly accounts for the high periphery fragility observed during crisis periods. In the post-crash period, the network shows partial recovery. Core concentration increases, periphery fragility decreases, and both average path length and weighted degree move back toward their pre-crash levels. However, this recovery is neither complete nor uniform across markets. For Australia, post-crash core concentration exceeds its pre-crash value, while periphery fragility remains high, indicating a persistent change in network structure. In contrast, the U.S. and Japan exhibit lower post-crash algebraic connectivity than before the crash, suggesting continued structural vulnerability. This heterogeneous aftershock pattern, observed only in the residual, statistically validated network, demonstrates that the conditional p-threshold MI framework captures not only the crash period but also lasting structural effects that differ across markets.

Table 2: Table represents the average network topological measures of conditional p-threshold MI–MST networks for QUAD stock markets across pre-crash, crash, and post-crash periods. W.Deg denotes weighted degree, Ecc denotes eccentricity, Eff denotes global efficiency, APL denotes average path length, λ2\lambda\_{2} denotes algebraic connectivity, Tree Len denotes total tree length, and Assort denotes degree assortativity. These metrics collectively characterize changes in network integration, connectivity, and core–periphery structure across market periods.

| Period | Country | W.Deg | Ecc | Eff | APL | 𝝀𝟐\boldsymbol{\lambda\_{2}} | Tree Len | Assort |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pre-Crash | USA | 1.959 | 12.22 | 0.181 | 6.39 | 0.0059 | 197.41 | -0.383 |
| Japan | 1.979 | 11.25 | 0.176 | 6.54 | 0.0051 | 203.64 | -0.398 |
| India | 1.949 | 13.23 | 0.167 | 7.02 | 0.0044 | 202.17 | -0.424 |
| Australia | 1.910 | 15.83 | 0.157 | 8.31 | 0.0041 | 170.97 | -0.358 |
| Crash | USA | 3.333 | 8.21 | 0.161 | 4.55 | 0.0020 | 114.26 | -0.453 |
| Japan | 3.381 | 8.62 | 0.154 | 4.84 | 0.0015 | 117.16 | -0.422 |
| India | 3.479 | 6.74 | 0.178 | 3.71 | 0.0047 | 112.20 | -0.354 |
| Australia | 3.156 | 9.05 | 0.167 | 4.79 | 0.0024 | 99.45 | -0.402 |
| Post-Crash | USA | 2.073 | 12.11 | 0.174 | 6.42 | 0.0046 | 184.63 | -0.248 |
| Japan | 2.078 | 13.56 | 0.177 | 6.66 | 0.0029 | 191.35 | -0.291 |
| India | 2.077 | 12.64 | 0.172 | 6.68 | 0.0032 | 189.15 | -0.326 |
| Australia | 1.953 | 13.97 | 0.167 | 7.49 | 0.0045 | 161.56 | -0.461 |

Overall, the conditional p‑threshold MI–MST framework provides a clear view of how crisis‑induced reconfiguration operates through the core–periphery structure. The method filters out the diffuse co‑movement driven by common factors, revealing a distinct structural change: a weakened core, a weakened core, an increasingly fragile and actively connected periphery, and disassortative mixing that amplifies vulnerability. These patterns are consistent across geographically diverse markets, confirming that the approach captures universal features of crisis topology that are masked by traditional, non‑filtered network measures.

## 5 Community Structure of Stock Market Networks

![Refer to caption](modularity_comparison.png)


Figure 7: Modularity of conditional p-threshold MI–MST networks for QUAD stock markets(US, Japan, Australia and India) across pre-crash, crash, and post-crash periods. Modularity values were computed using Clauset-Newman-Moore greedy modularity maximization applied to the conditional p-threshold MI–MST network.

To analyze the community structure of stock markets during periods of financial crash, we computed network modularity using the Clauset-Newman-Moore greedy modularity maximization clauset2004finding algorithm applied to conditional p-threshold MI–MST networks. The greedy modularity maximization method starts by assigning each node to its own community and iteratively merging pairs of communities that yield the largest increase in modularity, until no further improvement is possible and a (local) maximum of the modularity function is reached. Modularity QQ clauset2004finding quantifies the strength of community structure by comparing the observed fraction of intra-community edges to that expected under a degree-preserving null model and is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q=∑c(EcE−(kc2​E)2),Q=\sum\_{c}\left(\frac{E\_{c}}{E}-\left(\frac{k\_{c}}{2E}\right)^{2}\right), |  | (55) |

where EcE\_{c} is the number of edges within community cc, EE is the total number of edges and kck\_{c} is the sum of degrees of nodes in community cc.

Fig. [7](https://arxiv.org/html/2601.00395v1#S5.F7 "Figure 7 ‣ 5 Community Structure of Stock Market Networks ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") shows that, across all four markets: the US, Japan, Australia, and India, the modularity increases systematically during the crash period compared to the pre- and post-crash period. This indicates a strengthening of community structures under market stress. During crash episodes, assets tend to exhibit heightened synchronization within economically or sectorally related groups, while inter-community interactions weaken. Such correlation clustering enhances intra-community connectivity relative to null models, leading to higher modularity values.

To evaluate the statistical significance of community structures in the financial networks across all four markets during the pre-crash, crash, and post-crash periods, we compared the observed modularity (QobsQ\_{\rm obs}) with modularity values from randomized networks (QrandQ\_{\rm rand}). The hypotheses for each market-period pair were formulated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0\displaystyle H\_{0} | :Qobs≤Qrand(no significant community structure)\displaystyle:Q\_{\rm obs}\leq Q\_{\rm rand}\quad\text{(no significant community structure)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | H1\displaystyle H\_{1} | :Qobs>Qrand(significant community structure)\displaystyle:Q\_{\rm obs}>Q\_{\rm rand}\quad\text{(significant community structure)} |  |

For the testing procedure, QobsQ\_{\rm obs} was calculated using the greedy modularity maximization method. An ensemble of N=1000N=1000 degree-preserving randomized networks was generated using double-edge swaps, and modularity QrandQ\_{\rm rand} was calculated for each randomized network. The empirical p-value was determined as:

|  |  |  |
| --- | --- | --- |
|  | p=1N​∑i=1N𝕀​(Qrand(i)≥Qobs),p=\frac{1}{N}\sum\_{i=1}^{N}\mathbb{I}\left(Q\_{\rm rand}^{(i)}\geq Q\_{\rm obs}\right), |  |

where 𝕀​(⋅)\mathbb{I}(\cdot) is the indicator function. The null hypothesis H0H\_{0} was rejected if p<0.05p<0.05.
Across all markets and periods, we observed that the modularity values were consistently high and empirical p-values were significantly small with p<0.01p<0.01, indicating that the detected community structures are highly unlikely to occur by chance. These results confirm that the financial networks possess robust and statistically significant community structures that persist across different market conditions.

### 5.1 Aftershock in the Stock Market

Fig. [8](https://arxiv.org/html/2601.00395v1#S5.F8 "Figure 8 ‣ 5.1 Aftershock in the Stock Market ‣ 5 Community Structure of Stock Market Networks ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") shows the log–log relationship between the cumulative number of post-crash volatility events N​(M)N(M) following the COVID-19 stock market crash and their corresponding magnitudes MM for major QUAD stock market indices. We fitted the data using Eq. [52](https://arxiv.org/html/2601.00395v1#S2.E52 "In 2.5 Gutenberg–Richter Power Law ‣ 2 Method of Analysis ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach"). The plots of log10⁡N​(M)\log\_{10}N(M) versus MM show good agreement with the post-crash data, indicating that peak–trough log-price fluctuations follow the GR power-law behavior. The straight line in Fig. [8](https://arxiv.org/html/2601.00395v1#S5.F8 "Figure 8 ‣ 5.1 Aftershock in the Stock Market ‣ 5 Community Structure of Stock Market Networks ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") represents the best linear fit to the data. For all the QUAD stock market indices, the cumulative log–rank distributions of peak–trough log-price fluctuations exhibit an approximately linear scaling over a broad range of magnitudes, indicating that post-crash volatility events follow a GR-type power-law relationship. Table [3](https://arxiv.org/html/2601.00395v1#S5.T3 "Table 3 ‣ 5.1 Aftershock in the Stock Market ‣ 5 Community Structure of Stock Market Networks ‣ Core-Periphery Dynamics in Market-Conditioned Financial Networks: A Conditional P-Threshold Mutual Information Approach") presents the comparison of GR scaling parameters between pre-crash and post-crash periods. We observed that across all the indices and stocks, the estimated bb-values decrease significantly in the post-crash period compared to the pre-crash period. The systematic reduction in bb-values indicates that post-crash market dynamics are characterized by a higher relative frequency of large volatility events, consistent with the persistence of market stress rather than a return to pre-crash stability. This aligns with our network topology findings, where post-crash periods show continued structural changes. Lower bb-values correspond to aftershock-like behavior where large volatility events remain more probable, reflecting ongoing market fragility despite apparent recovery. Since lower bb-values correspond to a higher relative occurrence of large volatility events, this result indicates increased persistence of large fluctuations following the crash. Together with statistically valid GR fits, these findings suggest that post-crash market dynamics are characterized by aftershock-like volatility rather than an immediate return to pre-crash conditions. This evidence supports and complements the earlier network topology analysis.

![Refer to caption](x1.png)


(a) S&P 500

![Refer to caption](x2.png)


(b) Nikkei 225

![Refer to caption](x3.png)


(c) S&P/ASX 200

![Refer to caption](x4.png)


(d) Nifty50

Figure 8: Gutenberg–Richter (GR) plots for QUAD stock market indices. Figures (a), (b), (c), and (d) represent the GR plot for the S&P 500 (US), the Nikkei 225 (Japan), the S&P/ASX 200 (Australia), and the Nifty50 (India). respectively. Each figure shows the cumulative log–rank distribution of peak–trough log-price fluctuations during the post-crash period, along with the fitted GR law.




Table 3: Table represents a comparison of Gutenberg–Richter (GR) scaling parameters between pre-crash and post-crash periods for QUAD market indices and representative stocks. A consistent decrease in bb-values (Δ​b<0\Delta b<0) is observed across all assets, indicating an increased occurrence of large volatility events and aftershock-like behavior in the post-crash period.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Category | Asset | 𝒃pre\boldsymbol{b\_{\text{pre}}} | 𝒃post\boldsymbol{b\_{\text{post}}} | 𝚫​𝒃\boldsymbol{\Delta b} | 𝑹post𝟐\boldsymbol{R^{2}\_{\text{post}}} | KS ppostp\_{\text{post}} |
| Indices | ^GSPC | 103.35 | 46.38 | −56.97-56.97 | 0.921 | 0.872 |
| ^N225 | 90.56 | 36.72 | −53.84-53.84 | 0.898 | 0.808 |
| ^NSEI | 98.98 | 34.69 | −64.29-64.29 | 0.932 | 0.538 |
| ^AXJO | 106.88 | 33.60 | −73.28-73.28 | 0.927 | 0.978 |
| Stocks | AAPL | 62.89 | 25.04 | −37.85-37.85 | 0.953 | 0.990 |
| MSFT | 93.19 | 26.58 | −66.61-66.61 | 0.920 | 1.000 |
| AMZN | 78.29 | 16.92 | −61.37-61.37 | 0.918 | 0.921 |
| NVDA | 46.75 | 18.23 | −28.52-28.52 | 0.953 | 0.983 |
| JPM | 66.76 | 14.77 | −51.99-51.99 | 0.955 | 0.952 |
| INFY.NS | 59.98 | 33.13 | −26.85-26.85 | 0.986 | 1.000 |

## 6 Conclusion

This study provides a comprehensive examination of the evolution of nonlinear dependency structures and network topology in global equity markets during the COVID-19 crisis. Using a conditional pp-threshold mutual information (MI) framework, we analyzed stock market dynamics across the QUAD economies, namely the United States, Japan, Australia, and India, by systematically comparing pre-crash, crash, and post-crash periods. The COVID-19 market crash was identified using a robust two-stage approach. First, a rolling Hellinger Distance (HD) detected statistically significant structural breaks in cross-sectional return distributions through synchronized threshold exceedances (HD>μH+2​σHH\_{D}>\mu\_{H}+2\sigma\_{H}) across all four markets. Second, the Hilbert Spectrum (HS) characterized the internal temporal dynamics of the identified crash period, revealing a sustained concentration of high instantaneous energy during February–March 2020. Together, these methods confirm that the detected event corresponds to a prolonged high-volatility market period.

A comparison between MI and conditional pp-threshold MI highlights clear differences in the resulting dependency structures. The MI matrices were found to be dense and dominated by common market-wide effects, particularly during the crash, which hide pure stock-level interactions. In contrast, conditioning on market index returns and applying permutation-based statistical filtering yielded sparse and economically interpretable dependency structures. The conditional pp-threshold MI framework thus effectively isolated direct and statistically significant nonlinear stock–stock dependencies, providing a reliable basis for network construction. Transforming these filtered dependencies into Minimum Spanning Tree (MST) networks revealed consistent and universal topological reorganization across all QUAD markets during the crash. The networks exhibited clear compression, characterized by a reduction in average path length and eccentricity alongside increases in closeness and weighted degree, implying faster potential propagation of shocks. Despite this increased integration, algebraic connectivity declined, indicating that the crash-induced connectivity was accompanied by greater structural fragility. The crisis period was also marked by a pronounced reconfiguration of the core–periphery structure. Core concentration declined systematically across all markets, indicating a fragmentation and decentralization of influence away from a stable core. At the same time, periphery fragility increased in most markets, indicating greater vulnerability of weakly connected stocks to shock transmission. This shift was reinforced by increasingly negative assortativity, reflecting preferential connections between influential core stocks and fragile peripheral nodes, thereby amplifying systemic risk. Beyond node-level and global topology, community structure analysis revealed a strengthening of modular organization during the crash. Increased modularity indicates that stocks clustered more tightly into internally cohesive groups, while inter-community connections weakened, reflecting segmentation of market interactions under stress. This clustering further contributes to the uneven transmission of shocks across the network.

In the post-crash period, the network did not fully revert to its pre-crisis configuration. Several topological measures and core–periphery indices showed only partial recovery, indicating persistent structural aftereffects. This delayed normalization was supported by an aftershock analysis based on the Gutenberg–Richter law. A systematic reduction in the scaling parameter (bb-value) across indices and representative stocks implies a higher relative frequency of large volatility events following the crash, consistent with continued market fragility rather than immediate stabilization.

Overall, the conditional pp-threshold MI–MST framework offers a refined lens for examining crisis-driven market reorganization. By filtering out common market effects and emphasizing statistically validated nonlinear dependencies, the approach uncovers universal structural signatures of financial crises, including network compression, weakened core dominance, heightened periphery vulnerability, strengthened community structure, and persistent aftershocks. These findings provide meaningful insights into systemic risk propagation and recovery dynamics across geographically distinct markets. In future work, we will extend this framework to other asset classes and crisis periods.

## Acknowledgments

The authors, Kundan Mukhia and S.R. Luwang, would like to acknowledge the National Institute of Technology Sikkim for providing doctoral research fellowships. Imran Ansari acknowledges support from the Kotak IISc AI–ML Centre (KIAC) at the Indian Institute of Science, Bengaluru, India.

## Appendix

![Refer to caption](Australia_Pre-Crash_RawMI.png)


(a) Pre-Crash (Raw MI)

![Refer to caption](Australia_Crash_RawMI.png)


(b) Crash (Raw MI)

![Refer to caption](Australia_Post-Crash_RawMI.png)


(c) Post-Crash (Raw MI)

![Refer to caption](Australia_Pre-Crash_ResidualSigMI.png)


(d) Pre-Crash (Cond. P-threshold)

![Refer to caption](Australia_Crash_ResidualSigMI.png)


(e) Crash (Cond. P-threshold)

![Refer to caption](Australia_Post-Crash_ResidualSigMI.png)


(f) Post-Crash (Cond. P-threshold)

Figure 9: Mutual information heatmaps for the 25 largest Australia stocks across different market periods. Plot (a)–(c) shows raw mutual information (MI) heatmaps, which are dominated by common market effects and exhibit dense connectivity, particularly during the crash period. Plot (d)–(f) display residual-based, significance-filtered MI heatmaps obtained using the conditional P-threshold MI method, highlighting statistically significant and direct nonlinear dependencies. The conditional P-threshold MI heatmaps show a sparse structure, indicating the true nonlinear dependencies between stocks after removing the market effect, which reveals the underlying direct interactions among stocks



![Refer to caption](India_Pre-Crash_RawMI.png)


(a) Pre-Crash (Raw MI)

![Refer to caption](India_Crash_RawMI.png)


(b) Crash (Raw MI)

![Refer to caption](India_Post-Crash_RawMI.png)


(c) Post-Crash (Raw MI)

![Refer to caption](India_Pre-Crash_ResidualSigMI.png)


(d) Pre-Crash (Cond. P-threshold)

![Refer to caption](India_Crash_ResidualSigMI.png)


(e) Crash (Cond. P-threshold)

![Refer to caption](India_Post-Crash_ResidualSigMI.png)


(f) Post-Crash (Cond. P-threshold)

Figure 10: Mutual information heatmaps for the 25 largest Indian stocks across different market periods. Plot (a)–(c) shows raw mutual information (MI) heatmaps, which are dominated by common market effects and exhibit dense connectivity, particularly during the crash period. Plot (d)–(f) display residual-based, significance-filtered MI heatmaps obtained using the conditional P-threshold MI method, highlighting statistically significant and direct nonlinear dependencies. The conditional P-threshold MI heatmaps show a sparse structure, indicating the true nonlinear dependencies between stocks after removing the market effect, which reveals the underlying direct interactions among stocks



![Refer to caption](MI_MST_closeness_Australia_log.png)


(a) Closeness

![Refer to caption](MI_MST_eccentricity_Australia_log.png)


(b) Eccentricity

![Refer to caption](MI_MST_eigenvector_Australia_log.png)


(c) Eigenvector Centrality

![Refer to caption](MI_MST_weighted_degree_Australia_log.png)


(d) Weighted Degree

Figure 11: 
Rank-ordered distributions of MST-based network metrics for the Australian stock market across pre-crash, crash and post-crash periods. Plot (a) represents closeness, Plot (b) eccentricity, Plot (c) eigenvector centrality and Plot (d) weighted degree. Stocks are ranked in ascending order for each metric. The curves correspond to the three market periods, highlighting structural reorganization and centralization during the crash period.



![Refer to caption](MI_MST_closeness_India_log.png)


(a) Closeness

![Refer to caption](MI_MST_eccentricity_India_log.png)


(b) Eccentricity

![Refer to caption](MI_MST_eigenvector_India_log.png)


(c) Eigenvector Centrality

![Refer to caption](MI_MST_weighted_degree_India_log.png)


(d) Weighted Degree

Figure 12: 
Rank-ordered distributions of MST-based network metrics for the Indian stock market across pre-crash, crash and post-crash periods. Plot (a) represents closeness, Plot (b) eccentricity, Plot (c) eigenvector centrality and Plot (d) weighted degree. Stocks are ranked in ascending order for each metric. The curves correspond to the three market periods, highlighting structural reorganization and centralization during the crash period.