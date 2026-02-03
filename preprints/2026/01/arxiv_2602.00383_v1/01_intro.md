---
authors:
- Samuel W. Akingbade
doc_id: arxiv:2602.00383v1
family_id: arxiv:2602.00383
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Null-Validated Topological Signatures of Financial Market Dynamics
url_abs: http://arxiv.org/abs/2602.00383v1
url_html: https://arxiv.org/html/2602.00383v1
venue: arXiv q-fin
version: 1
year: 2026
---


Samuel W. Akingbade
Department of Mathematics, University of Michigan, Ann Arbor, MI, USA.
[sakingba@umich.edu.](mailto:sakingba@umich.edu.)
[sakingba@mail.yu.edu (permanent).](mailto:sakingba@mail.yu.edu%20(permanent).)

###### Abstract.

Financial markets exhibit temporal organization that is not fully captured by volatility measures or linear correlation structure. We study a null validated topological approach for quantifying market complexity and apply it to Bitcoin daily log returns. The analysis uses the L1L^{1} norm of persistence landscapes computed from sliding-window delay embeddings. This quantity shows strong co-movement with stochastic volatility during periods of market stress, but remains intermittently elevated during low volatility regimes, indicating dynamical structure beyond fluctuation scale. Rolling correlation analysis reveals that the dependence between geometry and volatility is not stationary. Surrogate based null models provide statistical validation of these observations. Rejection of shuffle surrogates rules out explanations based on marginal distributions alone, while departures from phase randomized surrogates indicate sensitivity to nonlinear and phase dependent temporal organization beyond linear correlations. These results demonstrate that persistence landscape norms provide complementary information about market dynamics across market conditions.

## 1. Introduction

Understanding the complex temporal dynamics of financial markets remains a central challenge in financial mathematics, quantitative finance, and econometrics. Traditional tools such as volatility estimates and linear correlation measures provide essential but limited perspectives on market behavior, particularly during periods of stress or structural change. Volatility, often modeled through stochastic processes, captures the scale of fluctuation but may fail to detect subtler dynamical features that reflect temporal organization or higher order dependencies in return series. As a result, there is growing interest in methods that can extract richer information about the geometry and temporal structure of financial time series beyond conventional statistical summaries.

In recent years, topological data analysis (TDA) has emerged as a promising framework for studying the shape of complex data. TDA seeks to describe intrinsic structural features that persist across multiple scales, leveraging tools from algebraic topology to quantify connectivity and loops in point clouds or time series embeddings. At the heart of TDA is persistent homology, a method for tracking the birth and death of topological features such as connected components and cycles as a scale parameter varies, yielding descriptors like barcodes and persistence diagrams that summarize data shape in a multiscale manner. Persistent homology has been applied across diverse domains where structure matters, including the analysis of complex biological and dynamical signals, due to its robustness to noise and coordinate-free characterization of data geometry; see, for example, [[23](https://arxiv.org/html/2602.00383v1#bib.bib25 "Persistent homology of time-dependent functional networks constructed from coupled time series")].

In the context of time series, a common approach is to convert sequential observations into a delay or sliding window embedding that reconstructs the dynamics of the underlying process in a higher-dimensional space. This method draws on ideas related to Takens’ embedding theorem [[30](https://arxiv.org/html/2602.00383v1#bib.bib40 "Detecting strange attractors in turbulence")] and has been studied in both theoretical and applied settings; by embedding a signal into a point cloud in a reconstructed state space, one can apply persistent homology to detect recurrent geometric patterns such as loops and voids that correspond to underlying dynamical phenomena [[22](https://arxiv.org/html/2602.00383v1#bib.bib43 "Sliding windows and persistence: an application of topological methods to signal analysis")]. Practical summaries of these persistent features include persistence landscapes and their norms, which are scalar functions that quantify the prominence of topological features and enable statistical comparison across time.

Application of these methods to financial time series has grown in recent years. A major work by [[11](https://arxiv.org/html/2602.00383v1#bib.bib49 "Topological data analysis of financial time series: Landscapes of crashes")] used persistent homology to analyze major U.S. stock indices, showing that persistence landscape norms increase before and during market meltdowns, thereby providing a novel signal that goes beyond standard volatility measures. More recently, [[1](https://arxiv.org/html/2602.00383v1#bib.bib1 "Why topological data analysis detects financial bubbles?")] offered a theoretical explanation for this behavior by linking the growth of persistence landscape norms to log-periodic power law singularity dynamics, which are commonly used to model speculative bubbles and critical transitions. They showed that when a financial time series follows such dynamics, its delay coordinate embedding naturally exhibits structured oscillatory geometry, leading to the emergence of persistent loop-like features in the reconstructed state space. In a related line of work, [[10](https://arxiv.org/html/2602.00383v1#bib.bib50 "Topological recognition of critical transitions in time series of cryptocurrencies")] developed a topological framework for recognizing critical transitions in cryptocurrency markets, including Bitcoin and Ethereum, in the period leading up to the 2018 market crash. Additional studies have applied topological methods to financial time series in a variety of settings, including early warning detection, critical transitions, bubble identification, sparse portfolio and structural analysis of market dynamics; see, for example, [[4](https://arxiv.org/html/2602.00383v1#bib.bib9 "Mild explocivity, persistent homology and cryptocurrencies’ bubbles: an empirical exercise"), [19](https://arxiv.org/html/2602.00383v1#bib.bib8 "Early warning signals of financial crises using persistent homology"), [12](https://arxiv.org/html/2602.00383v1#bib.bib48 "Topological data analysis of critical transitions in financial networks"), [14](https://arxiv.org/html/2602.00383v1#bib.bib11 "Risk reduced sparse index tracking portfolio: a topological data analysis approach"), [13](https://arxiv.org/html/2602.00383v1#bib.bib12 "Sparse portfolio selection via topological data analysis based clustering"), [24](https://arxiv.org/html/2602.00383v1#bib.bib54 "Topological data analysis for portfolio management of cryptocurrencies"), [26](https://arxiv.org/html/2602.00383v1#bib.bib52 "Topological data analysis for identifying critical transitions in cryptocurrency time series")].

Subsequent research has applied topological methods to change point detection in financial markets, demonstrating that persistent homology features can align with major economic events and volatility regimes across different stock markets [[36](https://arxiv.org/html/2602.00383v1#bib.bib3 "Change point detection in financial market using topological data analysis")]. Persistence landscape norms have been shown to correlate with volatility and uncertainty in financial markets [[25](https://arxiv.org/html/2602.00383v1#bib.bib61 "Uncertainty, volatility and the persistence norms of financial time series"), [29](https://arxiv.org/html/2602.00383v1#bib.bib13 "Topological tail dependence: evidence from forecasting realized volatility")], however the dynamical origin of this signal and its dependence on temporal ordering and nonlinear structure remain largely unexplored. These contributions illustrate the potential of persistent homology to capture aspects of market dynamics that are not fully accessible via conventional statistical tools.

Despite these advances, several gaps remain in the rigorous validation and interpretation of topological summaries in financial settings. In particular, it is important to distinguish genuine temporal organization from artifacts of marginal distributions or linear correlation structure. Null model frameworks that systematically test the dependence of topological features on temporal ordering or nonlinear dynamics are less commonly explored, yet they are crucial for establishing statistical significance and interpretability. Addressing this need is especially relevant in markets characterized by regime shifts, such as cryptocurrency markets, which have been widely studied due to their pronounced volatility, behavioral effects, and rapid structural changes [[9](https://arxiv.org/html/2602.00383v1#bib.bib14 "Interactions between investors’ fear and greed sentiment and bitcoin prices"), [16](https://arxiv.org/html/2602.00383v1#bib.bib15 "Predicting cryptocurrency returns for real-world investments: a daily updated and accessible predictor"), [34](https://arxiv.org/html/2602.00383v1#bib.bib16 "A u-shaped relationship between the crypto fear-greed index and the price synchronicity of cryptocurrencies")]. Bitcoin, as the largest and most liquid cryptocurrency, provides a natural setting for examining these issues. Our work contributes to this literature by introducing a null-validated topological analysis of Bitcoin log returns that explicitly compares topological summary statistics to surrogate ensembles designed to preserve specific statistical properties of the series while destroying temporal dependence.

In this study, we investigate the geometric and temporal structure of Bitcoin log return dynamics through a topological lens, treating the L1L^{1} norm of persistence landscapes computed from sliding window delay embeddings as a quantitative summary of reconstructed state-space geometry. Rather than interpreting this quantity solely as a proxy for market stress, we examine how it relates to and differs from established scale-based models of market variability. To this end, a central contribution of this work is a systematic comparison between the persistence landscape norm and filtered stochastic volatility estimates, including an analysis of their time varying association through rolling correlations. This comparison allows us to characterize regimes in which topological structure and volatility align, as well as regimes in which they decouple.

A second central contribution is the incorporation of surrogate-based null models to rigorously assess the statistical origin of the observed topological signal. By employing both shuffle surrogates, which preserve the marginal distribution of returns while destroying temporal ordering, and phase-randomized surrogates, which preserve linear second order structure while removing nonlinear and phase-dependent dependencies, we disentangle the respective roles of marginal effects, linear correlations, and higher order temporal organization. This framework enables us to distinguish genuine geometric structure in the reconstructed dynamics from artifacts induced by distributional or linear properties of the time series.

Our results show that while the persistence landscape norm co-moves strongly with stochastic volatility during periods of market stress, the dependence between the two is not stationary. In particular, the topological signal exhibits intermittent bursts and sustained deviations from baseline even during low-volatility regimes, indicating the presence of organized temporal dynamics that are not captured by fluctuation scale or linear correlation structure alone. Together, these findings position the persistence landscape norm as a null-validated descriptor of financial time series that is sensitive to volatility and complements stochastic volatility models, providing insight into regime dependent organization in complex market dynamics.

The structure of the paper is as follows. Section [2.1](https://arxiv.org/html/2602.00383v1#S2.SS1 "2.1. Persistent homology ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics") reviews topological data analysis with a focus on persistent homology, and Section [2.2](https://arxiv.org/html/2602.00383v1#S2.SS2 "2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics") describes its application to financial time series, including Bitcoin log returns and the distribution of topological signals across sentiment regimes. Section [3](https://arxiv.org/html/2602.00383v1#S3 "3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics") compares the norm of the persistence landscape obtained from sliding window delay embeddings of log returns with filtered stochastic volatility and examines their rolling correlation. Section [4](https://arxiv.org/html/2602.00383v1#S4 "4. Construction of Surrogate Null Models ‣ Null-Validated Topological Signatures of Financial Market Dynamics") introduces surrogate-based null models for statistical validation of the persistence landscape norm as a descriptor of market dynamics beyond volatility and sentiment effects. The main contributions are presented in Sections  [3](https://arxiv.org/html/2602.00383v1#S3 "3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics") and  [4](https://arxiv.org/html/2602.00383v1#S4 "4. Construction of Surrogate Null Models ‣ Null-Validated Topological Signatures of Financial Market Dynamics"). Conclusions and future directions are presented in Section [5](https://arxiv.org/html/2602.00383v1#S5 "5. Conclusions ‣ Null-Validated Topological Signatures of Financial Market Dynamics").

## 2. Background

### 2.1. Persistent homology

In this section, we describe the topological framework used throughout the paper, based on persistent homology. The tool provides a multiscale characterization of the geometry of point clouds derived from time series and allows us to extract robust numerical summaries of their evolving structure via persistence landscapes. The mathematical foundations of persistent homology and persistence landscapes are well established; see, for example, [[8](https://arxiv.org/html/2602.00383v1#bib.bib76 "Computational topology: an introduction"), [6](https://arxiv.org/html/2602.00383v1#bib.bib32 "Statistical topological data analysis using persistence landscapes."), [5](https://arxiv.org/html/2602.00383v1#bib.bib33 "A persistence landscapes toolbox for topological statistics"), [7](https://arxiv.org/html/2602.00383v1#bib.bib34 "The persistence landscape and some of its properties")].

#### 2.1.1. Persistent homology

It associates to a finite point cloud a family of topological spaces indexed by a resolution parameter, and tracks the evolution of topological features, such as connected components and loops, across scales. Persistence landscapes provide a functional representation of this multiscale information in a Banach space, enabling numerical summaries and statistical comparison. In this work, we ultimately summarize each point cloud by a single scalar quantity given by the L1L^{1} norm of its persistence landscape.

Let

|  |  |  |
| --- | --- | --- |
|  | X={x0,x1,…,xm−1}⊂ℝNX=\{x\_{0},x\_{1},\ldots,x\_{m-1}\}\subset\mathbb{R}^{N} |  |

be a finite point cloud embedded in Euclidean space. To associate a topological space to XX, we consider the Vietoris–Rips construction. For a fixed resolution parameter t>0t>0, the *Vietoris–Rips simplicial complex* V​R​(X,t)VR(X,t) is defined by including a kk-simplex with vertices {xi0,…,xik}\{x\_{i\_{0}},\ldots,x\_{i\_{k}}\} whenever the pairwise distances between all vertices are strictly less than tt, that is,

|  |  |  |
| --- | --- | --- |
|  | dX​(xij,xij′)<tfor all ​xij,xij′∈{xi0,…,xik}.d^{X}(x\_{i\_{j}},x\_{i\_{j^{\prime}}})<t\quad\text{for all }x\_{i\_{j}},x\_{i\_{j^{\prime}}}\in\{x\_{i\_{0}},\ldots,x\_{i\_{k}}\}. |  |

Intuitively, simplices are added whenever their vertices become indistinguishable at resolution tt. As tt increases, these complexes form a nested sequence

|  |  |  |
| --- | --- | --- |
|  | V​R​(X,t)⊆V​R​(X,t′)for ​t<t′,VR(X,t)\subseteq VR(X,t^{\prime})\quad\text{for }t<t^{\prime}, |  |

which constitutes a *filtration* of simplicial complexes.

At each resolution level, we compute the simplicial *homology groups*

|  |  |  |
| --- | --- | --- |
|  | Hn​(V​R​(X,t))H\_{n}(VR(X,t)) |  |

with coefficients in a fixed field, here taken to be ℤ2\mathbb{Z}\_{2}. The generators of these groups correspond to nn-dimensional topological features: connected components for n=0n=0, loops for n=1n=1, voids for n=2n=2, and so forth. In this work we restrict attention to one-dimensional homology, n=1n=1, so that the analysis focuses exclusively on loop-like geometric structures in the embedded data.

The filtration of simplicial complexes induces a corresponding filtration of homology groups,

|  |  |  |
| --- | --- | --- |
|  | Hn​(V​R​(X,t))↪Hn​(V​R​(X,t′))for ​t<t′,H\_{n}(VR(X,t))\hookrightarrow H\_{n}(VR(X,t^{\prime}))\quad\text{for }t<t^{\prime}, |  |

via canonical homomorphisms. This is called a *persistence module*. Persistence modules are uniquely decomposable into a direct sum of interval modules up to permutations [[37](https://arxiv.org/html/2602.00383v1#bib.bib2 "Computing persistent homology")]. The collection of these
indecomposables is referred to as a barcode where the intervals are bars, each representing the
evolution of a topological feature (n-dimensional hole).

#### 2.1.2. Persistence diagrams

A homology class α∈Hn\alpha\in H\_{n} is said to be born at scale bαb\_{\alpha} if it first appears at t:=bαt:=b\_{\alpha} and is not in the image of any class from smaller scales. The class persists across intermediate resolutions and is said to die at scale dα>bαd\_{\alpha}>b\_{\alpha} if its image becomes trivial at t:=dαt:=d\_{\alpha}. Each such class is therefore associated with a birth–death pair (bα,dα)(b\_{\alpha},d\_{\alpha}), with finite multiplicity determined by the number of classes sharing the same birth and death values. The collection of all birth–death pairs arising from HnH\_{n} is encoded in the *persistence diagram* PnP\_{n}, which is a locally finite multiset of points supported on U:={(t1,t2)∈ℝ2:t1<t2}U:=\{(t\_{1},t\_{2})\in\mathbb{R}^{2}:t\_{1}<t\_{2}\} together with points on the diagonal δ​U:={(t,t)∈ℝ2}\delta U:=\{(t,t)\in\mathbb{R}^{2}\} counted with infinite multiplicity, representing trivial features. The horizontal axis corresponds to birth values and the vertical axis to death values.

#### 2.1.3. Persistence landscapes

To obtain a functional representation suitable for numerical analysis, we map persistence diagrams into a Banach space using persistence landscapes.

For each off-diagonal point (bα,dα)∈Pn(b\_{\alpha},d\_{\alpha})\in P\_{n}, we define the piecewise linear function

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | f(bα,dα)​(x)={x−bα,x∈(bα,bα+dα2],dα−x,x∈(bα+dα2,dα),0,otherwise.f\_{(b\_{\alpha},d\_{\alpha})}(x)=\begin{cases}x-b\_{\alpha},&x\in\left(b\_{\alpha},\tfrac{b\_{\alpha}+d\_{\alpha}}{2}\right],\\ d\_{\alpha}-x,&x\in\left(\tfrac{b\_{\alpha}+d\_{\alpha}}{2},d\_{\alpha}\right),\\ 0,&\text{otherwise}.\end{cases} |  |

Given a persistence diagram with finitely many off-diagonal points, the *persistence landscape* is defined as the sequence of functions

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | λn=(λn​(i))i∈ℕ,λn​(i)​(x)=imax​{f(bα,dα)​(x)∣(bα,dα)∈Pn},\lambda\_{n}=(\lambda\_{n}(i))\_{i\in\mathbb{N}},\quad\lambda\_{n}(i)(x)=i\_{\max}\{f\_{(b\_{\alpha},d\_{\alpha})}(x)\mid(b\_{\alpha},d\_{\alpha})\in P\_{n}\}, |  |

where imaxi\_{\max} denotes the ii-th largest value among the indicated functions. If the ii-th largest value does not exist, λn​(i)​(x)\lambda\_{n}(i)(x) is set to zero. The resulting object lies in the Banach space Lp​(ℕ×ℝ)L^{p}(\mathbb{N}\times\mathbb{R}) for any p≥1p\geq 1.

For a persistence landscape λn\lambda\_{n}, the *LpL^{p} norm* is defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | ‖λn‖p=(∑i=1∞‖λn​(i)‖pp)1/p,‖λn​(i)‖p=(∫ℝ|λn​(i)​(x)|p​𝑑x)1/p.\|\lambda\_{n}\|\_{p}=\left(\sum\_{i=1}^{\infty}\|\lambda\_{n}(i)\|\_{p}^{p}\right)^{1/p},\quad\|\lambda\_{n}(i)\|\_{p}=\left(\int\_{\mathbb{R}}|\lambda\_{n}(i)(x)|^{p}\,dx\right)^{1/p}. |  |

In this work, we focus exclusively on the L1L^{1} norm. For finite persistence diagrams, this norm admits the closed-form expression [[6](https://arxiv.org/html/2602.00383v1#bib.bib32 "Statistical topological data analysis using persistence landscapes.")]

|  |  |  |  |
| --- | --- | --- | --- |
| (2.4) |  | ‖λn‖1=14​∑α(dα−bα)2.\|\lambda\_{n}\|\_{1}=\frac{1}{4}\sum\_{\alpha}(d\_{\alpha}-b\_{\alpha})^{2}. |  |

In practice, we compute a numerically approximated and truncated version of this quantity by integrating the first imaxi\_{\max} landscape layers over a finite grid of scale values.

### 2.2. Application to time series

We now describe how this framework is applied to financial time series following [[1](https://arxiv.org/html/2602.00383v1#bib.bib1 "Why topological data analysis detects financial bubbles?"), [10](https://arxiv.org/html/2602.00383v1#bib.bib50 "Topological recognition of critical transitions in time series of cryptocurrencies"), [2](https://arxiv.org/html/2602.00383v1#bib.bib10 "Applications of dynamical systems in dissipative mechanics and in topological data analysis")].

Let

|  |  |  |
| --- | --- | --- |
|  | Z={z0,z1,…,zN−1}Z=\{z\_{0},z\_{1},\ldots,z\_{N-1}\} |  |

be a real valued time series of length NN. Fix an embedding dimension mm and a time delay d≥1d\geq 1. The delay-coordinate embedding produces a sequence of vectors

|  |  |  |
| --- | --- | --- |
|  | xt=(zt,zt+d,…,zt+(m−1)​d),x\_{t}=(z\_{t},z\_{t+d},\ldots,z\_{t+(m-1)d}), |  |

defined for all indices tt such that the coordinates exist.

#### 2.2.1. Choice of embedding dimension and delay.

The use of delay-coordinate embeddings in this work is motivated by classical results from nonlinear dynamical systems theory, which establish conditions under which the geometry of an underlying state space can be reconstructed from time-delayed observations.

A foundational result is *Takens’* embedding theorem [[30](https://arxiv.org/html/2602.00383v1#bib.bib40 "Detecting strange attractors in turbulence")]. Consider a discrete-time dynamical system xt+1=T​(xt)x\_{t+1}=T(x\_{t}) evolving on a compact smooth manifold MM of dimension DD, together with a smooth observation function h:M→ℝh:M\to\mathbb{R}. Let {zt}\{z\_{t}\} be the scalar time series defined by zt=h​(xt)z\_{t}=h(x\_{t}). For a fixed delay d≥1d\geq 1, define the delay-coordinate map

|  |  |  |
| --- | --- | --- |
|  | Φ:M→ℝm,Φ​(xt)=(zt,zt+d,…,zt+(m−1)​d).\Phi:M\to\mathbb{R}^{m},\qquad\Phi(x\_{t})=(z\_{t},z\_{t+d},\ldots,z\_{t+(m-1)d}). |  |

Takens’ theorem states that, provided m≥2​D+1m\geq 2D+1, it is a generic property of the pair (T,h)(T,h) that Φ\Phi is an embedding, i.e., a smooth injective map with a smooth inverse onto its image. In this sense, the delay-coordinate vectors provide a faithful geometric representation of the underlying state space.

This result was subsequently generalized by [[33](https://arxiv.org/html/2602.00383v1#bib.bib41 "Embedology")], who showed that if the dynamics admit a compact attractor A⊂MA\subset M of finite fractal dimension DD, then an embedding of the attractor can be achieved for m≥2​D+1m\geq 2D+1 under the weaker assumption of prevalence rather than genericity. This extension is particularly relevant in practical settings where the dynamics evolve on a lower dimensional invariant set.

In the present study, delay coordinate embeddings are employed not for exact state-space reconstruction, but as a geometric representation from which topological features can be extracted robustly via persistent homology. Consequently, the embedding dimension mm and delay τ\tau are chosen empirically to be sufficient for capturing loop-like geometric structure in the delay embedding while remaining computationally tractable.

#### 2.2.2. Topological summaries of Bitcoin log return dynamics

To detect temporal variation in topological signal, we apply a sliding window of length ww to the sequence {xt}\{x\_{t}\}, yielding a time-indexed family of point clouds

|  |  |  |
| --- | --- | --- |
|  | Xt={xt,xt+1,…,xt+w−1}.X^{t}=\{x\_{t},x\_{t+1},\ldots,x\_{t+w-1}\}. |  |

For each window XtX^{t}, we compute the Vietoris–Rips filtration, extract the one dimensional persistence diagram, construct the corresponding persistence landscape, and evaluate the truncated L1L^{1} landscape norm.

![Refer to caption](x1.png)


Figure 1. Bitcoin daily log returns.

Bitcoin price data from January 1, 2020 to December 20, 2025 were obtained from Yahoo Finance [[35](https://arxiv.org/html/2602.00383v1#bib.bib5 "Yahoo finance")] and used to compute daily log returns shown in Figure [1](https://arxiv.org/html/2602.00383v1#S2.F1 "Figure 1 ‣ 2.2.2. Topological summaries of Bitcoin log return dynamics ‣ 2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics"). The topological data analysis procedure described above is then applied to the standardized Bitcoin log returns.

The result is a scalar time series

|  |  |  |
| --- | --- | --- |
|  | t↦‖λt‖1,t\mapsto\|\lambda^{t}\|\_{1}, |  |

which quantifies the evolving prominence of loop-like geometric structure in the embedded dynamics.

![Refer to caption](x2.png)


Figure 2. L1 norm of the persistence landscape of Bitcoin log returns.

We show the time evolution of the L1L^{1} norm of the H1H\_{1} persistence landscape computed from sliding window delay embeddings of standardized Bitcoin log returns in Figure [2](https://arxiv.org/html/2602.00383v1#S2.F2 "Figure 2 ‣ 2.2.2. Topological summaries of Bitcoin log return dynamics ‣ 2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics"), using an embedding dimension of 44, a delay of 22 and a sliding window of length 5050.

The resulting series exhibits multiple intervals of elevated L1L^{1} values throughout the sample, reflecting the recurrence of loop-like geometric structure in the delay space across several distinct periods. These elevated intervals are interspersed with lower activity regimes, indicating that the strength of the topological signal varies over time rather than remaining uniformly high. This temporal variability motivates examining whether the observed topological signal can be explained by conventional market descriptors such as sentiment or volatility.

#### 2.2.3. Distribution of L1 norms across sentiment regimes

Having established how the L1L^{1} norm of the persistence landscape computed from sliding-window delay embeddings of Bitcoin log returns evolves over time (Figure [2](https://arxiv.org/html/2602.00383v1#S2.F2 "Figure 2 ‣ 2.2.2. Topological summaries of Bitcoin log return dynamics ‣ 2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics")), we now examine how this quantity distributes across sentiment regimes.

Sentiment data were sourced from the Crypto Fear & Greed Index via the public API provided by alternative.me [[3](https://arxiv.org/html/2602.00383v1#bib.bib6 "Alternative.me")]. This index is a composite sentiment indicator scaled between 0 (Extreme Fear) and 100 (Extreme Greed), designed to capture aggregate market sentiment by combining multiple behavioral and market-based inputs, including price momentum, volatility, trading volume, and social media activity.

Figure [3](https://arxiv.org/html/2602.00383v1#S2.F3 "Figure 3 ‣ 2.2.3. Distribution of L1 norms across sentiment regimes ‣ 2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics") summarizes the empirical distribution of the L1L^{1} norm, conditioned on contemporaneous Fear & Greed sentiment regimes. While the distributions exhibit substantial overlap, systematic differences in median and dispersion are evident across regimes. In particular, Extreme Fear and Extreme Greed are associated with elevated central tendencies relative to intermediate sentiment states, though pronounced outliers occur in all categories. Overall, the results indicate that the L1L^{1} norm of the persistence landscape varies across sentiment regimes in a distributional sense, without exhibiting a simple monotonic dependence on sentiment.

![Refer to caption](x3.png)


Figure 3. Distribution of L1L^{1} norms of the persistence landscape for Bitcoin log returns across Fear & Greed sentiment regimes.

## 3. Stochastic volatility modeling of Bitcoin log returns

### 3.1. Stochastic volatility model

We model the Bitcoin log return series using a standard stochastic volatility (SV) specification, in which the latent state corresponds to the log variance of returns. Let hth\_{t} denote the latent log variance at time tt. The model is defined by the following two equations.

#### 3.1.1. State (process) equation

The latent log variance follows a mean reverting AR(1) process,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | ht=μ+ϕ​(ht−1−μ)+ση​ηt,ηt∼iid𝒩​(0,1).h\_{t}=\mu+\phi(h\_{t-1}-\mu)+\sigma\_{\eta}\eta\_{t},\ \ \ \ \ \eta\_{t}\stackrel{{\scriptstyle\text{iid}}}{{\sim}}\mathcal{N}(0,1). |  |

where μ\mu is the long run mean of the log variance, ϕ∈(0,1)\phi\in(0,1) controls persistence, and ση>0\sigma\_{\eta}>0 governs the magnitude of stochastic shocks to the log variance.

We restrict ϕ∈(0,1)\phi\in(0,1) to ensure that the latent log variance process is strictly stationary, yielding a well defined long-run distribution for volatility. Under this formulation, crash-related volatility spikes are accommodated through the stochastic innovations ηt\eta\_{t} and magnified by the exponential mapping, rather than through a globally explosive parameterization of the latent state. This specification captures the high persistence and mean reverting behavior of volatility observed in financial markets over long horizons without implying permanent divergence from the long-run mean.

#### 3.1.2. Observation (measurement) equation

Conditional on hth\_{t}, returns are Gaussian with zero mean and variance exp⁡(ht)\exp(h\_{t}),

|  |  |  |
| --- | --- | --- |
|  | zt∣ht∼𝒩​(0,exp⁡(ht))z\_{t}\mid h\_{t}\sim\mathcal{N}(0,\exp(h\_{t})) |  |

Under this formulation, exp⁡(ht)\exp(h\_{t}) represents the conditional variance of returns and exp⁡(ht/2)\exp(h\_{t}/2) the conditional volatility. This specification corresponds to the canonical discrete-time stochastic volatility model widely used in empirical finance (e.g.,[[31](https://arxiv.org/html/2602.00383v1#bib.bib4 "Modelling financial time series"), [15](https://arxiv.org/html/2602.00383v1#bib.bib17 "Multivariate stochastic variance models"), [20](https://arxiv.org/html/2602.00383v1#bib.bib18 "Stochastic volatility: likelihood inference and comparison with arch models"), [28](https://arxiv.org/html/2602.00383v1#bib.bib19 "Statistical aspects of arch and stochastic volatility"), [17](https://arxiv.org/html/2602.00383v1#bib.bib20 "The pricing of options on assets with stochastic volatilities")]).

### 3.2. Inference and parameter estimation

The SV model is cast as a partially observed Markov process (state-space model) and fitted using likelihood methods based on Monte Carlo sampling. Inference is carried out within the pomp framework, which supports likelihood evaluation and parameter estimation via simulation for nonlinear state-space models with non Gaussian noise.

To enforce parameter constraints during optimization, the model is reparameterized internally so that ση\sigma\_{\eta} is estimated on the log scale and ϕ\phi on the logit scale, ensuring ση>0\sigma\_{\eta}>0 and ϕ∈(0,1)\phi\in(0,1) throughout estimation.

Initial parameter values are chosen heuristically. In particular, the long run mean μ\mu is initialized using the logarithm of the empirical variance of the return series, while the remaining parameters are set to plausible values reflecting high persistence in financial volatility.

Model parameters θ=(μ,ϕ,ση,h0)\theta=(\mu,\phi,\sigma\_{\eta},h\_{0}) are estimated by maximum likelihood using iterated filtering (IF2), a simulation-based algorithm for partially observed Markov processes [[18](https://arxiv.org/html/2602.00383v1#bib.bib21 "Iterated filtering"), [21](https://arxiv.org/html/2602.00383v1#bib.bib22 "Statistical inference for partially observed markov processes via the R package pomp")]. Iterated filtering repeatedly applies a particle filter while perturbing parameters via a random walk with gradually decreasing variance, allowing the algorithm to ascend the likelihood surface of the state-space model.

For robustness against local maxima and Monte Carlo variability, the estimation procedure is repeated multiple times from the same initial parameter guess. For each replicate, the log-likelihood at the final parameter estimate is evaluated several times using independent particle filters. These likelihood evaluations are aggregated using a numerically stable log-mean-exp operation, which approximates the logarithm of the average likelihood, yielding a single likelihood score per replicate. The parameter set associated with the highest aggregated likelihood is selected as the final estimate θ^\hat{\theta}.

### 3.3. Filtered latent volatility

Given the estimated parameters θ^\hat{\theta}, we apply a particle filter to
approximate the sequence of filtering distributions

|  |  |  |
| --- | --- | --- |
|  | p​(ht∣z1:t;θ^),t=1,…,n.p(h\_{t}\mid z\_{1:t};\hat{\theta}),\qquad t=1,\dots,n. |  |

The primary quantity of interest is the filtered posterior mean of the latent log variance,

|  |  |  |
| --- | --- | --- |
|  | h^t:=𝔼​[ht∣z1:t;θ^].\hat{h}\_{t}:=\mathbb{E}[h\_{t}\mid z\_{1:t};\hat{\theta}]. |  |

In practice, this expectation is approximated using the particle representation
returned by the filter,

|  |  |  |
| --- | --- | --- |
|  | h^t≈1Np​∑i=1Npht(i),\hat{h}\_{t}\approx\frac{1}{N\_{p}}\sum\_{i=1}^{N\_{p}}h\_{t}^{(i)}, |  |

where ht(i)h\_{t}^{(i)} denotes the ii-th particle at time tt after resampling.

From the filtered log variance sequence {h^t}\{\hat{h}\_{t}\}, we construct estimates
of the conditional variance and volatility as

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | V^t=exp⁡(h^t),σ^t=V^t=exp⁡(h^t2).\hat{V}\_{t}=\exp(\hat{h}\_{t}),\qquad\hat{\sigma}\_{t}=\sqrt{\hat{V}\_{t}}=\exp\!\left(\frac{\hat{h}\_{t}}{2}\right). |  |

The resulting series (h^t,V^t,σ^t)(\hat{h}\_{t},\hat{V}\_{t},\hat{\sigma}\_{t}) provides a
time-resolved estimate of latent stochastic volatility.
Figure [4](https://arxiv.org/html/2602.00383v1#S3.F4 "Figure 4 ‣ 3.3. Filtered latent volatility ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics") displays the filtered volatility series over calendar time, which serves as a latent volatility benchmark for subsequent analysis.

![Refer to caption](x4.png)


Figure 4. Filtered conditional volatility estimate σ^t\hat{\sigma}\_{t} obtained from the stochastic volatility model of Bitcoin log returns.

Having obtained a filtered estimate of latent stochastic volatility, we now empirically compare its temporal evolution with the L1L^{1} norm of the persistence landscape computed from sliding-window embeddings of Bitcoin log returns.

### 3.4. Empirical comparison with topological signal

![Refer to caption](x5.png)


Figure 5. Standardized comparison of the L1L^{1} norm of persistence landscape (blue) and filtered stochastic volatility (red).

In Figure [5](https://arxiv.org/html/2602.00383v1#S3.F5 "Figure 5 ‣ 3.4. Empirical comparison with topological signal ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics"), we present a standardized comparison between the L1L^{1} norm of the persistence landscape computed from the Bitcoin log return series {zt}\{z\_{t}\} and the filtered stochastic volatility estimate.

In early 20202020, the onset of the COVID-19 crisis is marked by an abrupt and extreme surge in stochastic volatility. During this period, the topological signal rises as well, indicating that the large amplitude fluctuations associated with the market crash are accompanied by pronounced geometric organization in the reconstructed return dynamics. This co-movement persists throughout much of 2020​–​20212020–2021, a period characterized by repeated volatility spikes and sustained market stress, during which both measures remain elevated and closely aligned.

Following these stress episodes, the series enter multiple phases of volatility compression. In mid 20202020 and again in late 20202020, the standardized volatility drops to values near −2-2, indicating unusually low volatility relative to its long-run mean. During these intervals, the topological signal also declines below its mean, but typically not to the same extent as volatility. Furthermore, following the late 20212021 to early 20222022 decline in market volatility, the stochastic volatility estimate remains suppressed, whereas the topological signal continues to display intermittent bursts and sustained deviations from baseline. This asymmetric relaxation suggests that while fluctuation amplitude contracts rapidly after major shocks, geometric organization in return dynamics decays more gradually, retaining some structure even as volatility becomes unusually subdued.

A similar but more prolonged compression regime occurs in 20232023. In standardized units, stochastic volatility remains persistently suppressed for an extended period, reaching values near −2-2 and exhibiting relatively little variation. Over the same interval, the topological signal is often negative as well, but again does not compress as strongly and continues to display intermittent excursions. This behavior indicates that periods of apparent market calm, as measured by volatility, can still be associated with nontrivial temporal organization in returns, though at a reduced level compared to crisis periods.

All these observations indicate two key features. First, during periods of severe market stress, volatility and topological signal rise together reflecting the joint presence of large fluctuations and strong geometric structure. Second, outside these regimes, particularly during volatility compression phases, the relationship becomes asymmetric: volatility often contracts more strongly and more rapidly than the topological signal. This indicates that the L1L^{1} norm is sensitive not only to fluctuation scale but also to the persistence and organization of return dynamics, which can survive, albeit in weakened form, during extended periods of low volatility.

![Refer to caption](x6.png)


Figure 6. Rolling correlation between the L1L^{1} norm and stochastic volatility (180-day window).

To quantify the evolving relationship between topological signal and volatility, we examine the rolling correlation between the L1L^{1} norm and the filtered stochastic volatility estimate over a 180-day horizon in Figure [6](https://arxiv.org/html/2602.00383v1#S3.F6 "Figure 6 ‣ 3.4. Empirical comparison with topological signal ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics"). At each time point, the curve reports the linear association between topology and volatility over the preceding six months, providing a time-resolved measure of their dependence.

During periods of heightened market stress, the rolling correlation attains sustained positive values, indicating that increases in volatility are accompanied by concurrent increases in topological signal. This behavior is consistent with the co-movement observed in Figure [5](https://arxiv.org/html/2602.00383v1#S3.F5 "Figure 5 ‣ 3.4. Empirical comparison with topological signal ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics") during crisis regimes, where large-amplitude fluctuations and strong geometric organization arise together.

In contrast, following the subsequent contraction in volatility, the rolling correlation undergoes a pronounced decline and becomes markedly unstable, with extended intervals of weak or even negative association. Although the correlation exhibits multiple local minima, changepoint detection using the Pruned Exact Linear Time (PELT) algorithm identifies a single dominant shift (indicated by the brown dashed line in Figure [6](https://arxiv.org/html/2602.00383v1#S3.F6 "Figure 6 ‣ 3.4. Empirical comparison with topological signal ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics")) in the mean level of dependence. This transition separates an earlier regime characterized by persistently strong coupling from a later regime in which the association between topology and volatility is weaker and more variable.

This behavior indicates that the dependence between topological signal and volatility is not stationary over time. While the two measures align closely during crisis periods, the topological signal may persist or exhibit intermittent intensification even as volatility subsides. This further supports the interpretation that the L1L^{1} norm captures aspects of return dynamics beyond fluctuation scale alone, reflecting changes in temporal organization that are not fully encoded by volatility.

### 3.5. Topological signal beyond volatility and sentiment

![Refer to caption](x7.png)


Figure 7. ACF of the residual L1L^{1} norm of the persistence landscape computed from Bitcoin log return embeddings after removing linear effects of stochastic volatility and sentiment.

We perform a residualization analysis to examine whether the topological signal is fully explained by stochastic volatility and variation in sentiment. In this analysis, the L1L^{1} norm of the persistence landscape computed from delay embeddings of Bitcoin log returns is regressed on contemporaneous measures of volatility and sentiment.
Specifically, we consider the linear model

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | L1​(t)=β0+β1​σ¯t+β2​F¯t+β3​St+εt,L\_{1}(t)=\beta\_{0}+\beta\_{1}\,\overline{\sigma}\_{t}+\beta\_{2}\,\overline{F}\_{t}+\beta\_{3}\,S\_{t}+\varepsilon\_{t}, |  |

where L1​(t)L\_{1}(t) denotes the L1L^{1} norm summarizing the topological signal of the log return dynamics, σ¯t\overline{\sigma}\_{t} is the rolling window mean of the filtered stochastic volatility, F¯t\overline{F}\_{t} is the rolling window mean of the Fear & Greed sentiment index, and St:=V​a​r​(Ft−L+1:t)S\_{t}:=\sqrt{Var(F\_{t-L+1:t})} denotes the rolling window standard deviation of sentiment. The coefficients β0,…,β3\beta\_{0},...,\beta\_{3} capture linear associations between the topological summary and the covariates, while the residual term εt\varepsilon\_{t} represents the component of topological variation not explained by volatility or sentiment.

The primary object of interest is the temporal dependence structure of the residual series εt\varepsilon\_{t}. Figure [7](https://arxiv.org/html/2602.00383v1#S3.F7 "Figure 7 ‣ 3.5. Topological signal beyond volatility and sentiment ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics") displays the autocorrelation function (ACF) of εt\varepsilon\_{t}, which exhibits a slow decay with statistically significant correlations persisting across many lags. This behavior is inconsistent with a white noise residual and indicates that structured temporal organization remains in the topological signal after removing linear effects of volatility and coarse sentiment statistics.

## 4. Construction of Surrogate Null Models

Let {zt}t=1N\{z\_{t}\}\_{t=1}^{N} denote the standardized Bitcoin log return series. To determine whether the L1L^{1} norm of the persistence landscape obtained from sliding window delay embeddings of {zt}\{z\_{t}\} arise from genuine temporal structure, rather than effects attributable to the marginal distribution or linear second-order dependence, we compare the resulting time series of persistence landscape norms to those obtained from two classes of surrogate Bitcoin log return processes. Each surrogate is transformed through the same embedding and persistent homology pipeline, thereby inducing a null distribution for the windowed persistence landscape norm defined in [2.1](https://arxiv.org/html/2602.00383v1#S2.SS1 "2.1. Persistent homology ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").

### 4.1. Shuffle (i.i.d.) surrogate

Let π\pi be a random permutation of {1,…,N}\{1,\dots,N\} drawn uniformly from the symmetric group SNS\_{N}.
The *shuffle surrogate* of the observed series {zt}t=1N\{z\_{t}\}\_{t=1}^{N} is defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | zts:=zπ​(t),t=1,…,N.z\_{t}^{s}:=z\_{\pi(t)},\qquad t=1,\dots,N. |  |

This construction preserves the empirical marginal distribution of {zt}\{z\_{t}\} exactly, but destroys all temporal ordering and hence all serial dependence. In probabilistic terms, this surrogate corresponds to a null in which the observed series is treated as exchangeable.

For each realization j=1,…,Nsj=1,\dots,N\_{s}, we generate an independent permutation πj\pi\_{j}, compute the corresponding surrogate series zts,jz\_{t}^{s,j},
and apply section [2.1](https://arxiv.org/html/2602.00383v1#S2.SS1 "2.1. Persistent homology ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics") to obtain a surrogate topological time series.

### 4.2. FFT phase-randomized surrogate

The second null preserves second order temporal structure while destroying nonlinear and phase dependent features.
Let z~t=zt−z¯\tilde{z}\_{t}=z\_{t}-\bar{z} denote the demeaned series, and define its discrete Fourier transform (DFT) by

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | Zk:=∑t=0N−1z~t​e−2​π​i​k​t/N,k=0,…,N−1.Z\_{k}:=\sum\_{t=0}^{N-1}\tilde{z}\_{t}\,e^{-2\pi ikt/N},\qquad k=0,\dots,N-1. |  |

Write Zk=|Zk|​ei​θkZ\_{k}=|Z\_{k}|e^{i\theta\_{k}}. A *phase randomized* surrogate is constructed by replacing the phases θk\theta\_{k} at positive frequencies with i.i.d. random variables

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | ϕk∼Unif​(0,2​π),\phi\_{k}\sim\mathrm{Unif}(0,2\pi), |  |

while retaining the magnitudes |Zk||Z\_{k}|, and enforcing conjugate symmetry so that the inverse transform is real-valued. Concretely, for k=1,…,⌊(N−1)/2⌋k=1,\dots,\lfloor(N-1)/2\rfloor, define

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | Zkfft:=|Zk|​ei​ϕk,ZN−kfft:=Zkfft¯,Z\_{k}^{\mathrm{fft}}:=|Z\_{k}|e^{i\phi\_{k}},\qquad Z\_{N-k}^{\mathrm{fft}}:=\overline{Z\_{k}^{\mathrm{fft}}}, |  |

and set Z0fft:=Z0Z\_{0}^{\mathrm{fft}}:=Z\_{0}. If NN is even, the Nyquist component k=N/2k=N/2 must be real; one may set ZN/2fft:=ZN/2Z\_{N/2}^{\mathrm{fft}}:=Z\_{N/2} (or equivalently randomize with a sign change consistent with real-valuedness).

The inverse DFT yields a surrogate demeaned series

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | z~tfft:=1N​∑k=0N−1Zkfft​e2​π​i​k​t/N,t=0,…,N−1,\tilde{z}\_{t}^{\mathrm{fft}}:=\frac{1}{N}\sum\_{k=0}^{N-1}Z\_{k}^{\mathrm{fft}}e^{2\pi ikt/N},\qquad t=0,\dots,N-1, |  |

to which the original mean z¯\bar{z} is restored via ztfft=z~tfft+z¯z\_{t}^{\mathrm{fft}}=\tilde{z}\_{t}^{\mathrm{fft}}+\bar{z}.

This procedure preserves the power spectrum (and hence the autocovariance function) asymptotically, while destroying higher-order temporal dependencies and nonlinear phase relationships [[27](https://arxiv.org/html/2602.00383v1#bib.bib23 "Surrogate time series"), [32](https://arxiv.org/html/2602.00383v1#bib.bib24 "Testing for nonlinearity in time series: the method of surrogate data")]. As before, for each realization j=1,…,Nfftj=1,\dots,N\_{\mathrm{fft}}, we apply [2.1](https://arxiv.org/html/2602.00383v1#S2.SS1 "2.1. Persistent homology ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics") to obtain a surrogate topological time series.

### 4.3. Pointwise null envelopes for persistence landscape norms

For each sliding window, and for each null model, we generate multiple surrogate realizations of the persistence landscape norm by applying the same embedding and topological pipeline in [2.1](https://arxiv.org/html/2602.00383v1#S2.SS1 "2.1. Persistent homology ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics") to surrogate versions of {zt}\{z\_{t}\}. These surrogate values form an empirical sample from the null distribution of the window-level statistic. In all experiments, null envelopes are estimated using 30 surrogate realizations per null model. The qualitative behavior of the envelopes and exceedance patterns is robust to further increases in the number of surrogate realizations.

At each window, we summarize this null distribution by computing its mean, as well as its 5th and 95th empirical percentiles. The interval defined by these two percentiles constitutes a pointwise null envelope for the persistence landscape norm at that window.

This envelope provides a marginal comparison at each window index and should not be interpreted as a simultaneous confidence band across time; in particular, it does not control the family-wise error rate over all windows.

### 4.4. Exceedance statistics

We investigate deviations of the persistence landscape norm from its surrogate-based null envelopes by examining exceedances across sliding windows. We restrict attention to windows for which both the norm computed from the Bitcoin log return series and the corresponding null quantiles are well defined.

An exceedance below the null is recorded when the persistence landscape norm falls below the lower (5th percentile) bound of the null envelope, while an exceedance above the null is recorded when it exceeds the upper (95th percentile) bound. We count the total number of such lower and upper exceedances across all valid windows.

Finally, we report the fractions of windows in which the persistence landscape norm lies below or above the null envelope, respectively. These fractions provide a concise summary of how often the observed topological signal deviates from that expected under the surrogate null models.

The empirical behavior of these envelopes and the associated exceedance frequencies are examined in section [4.5](https://arxiv.org/html/2602.00383v1#S4.SS5 "4.5. Comparison to Surrogate-based null envelopes ‣ 4. Construction of Surrogate Null Models ‣ Null-Validated Topological Signatures of Financial Market Dynamics").

### 4.5. Comparison to Surrogate-based null envelopes

#### 4.5.1. Shuffle surrogate comparison

![Refer to caption](x8.png)


Figure 8. Comparison of L1L^{1} norm of the persistence landscape (blue) to pointwise null envelopes obtained from shuffle surrogates.

In Figure [8](https://arxiv.org/html/2602.00383v1#S4.F8 "Figure 8 ‣ 4.5.1. Shuffle surrogate comparison ‣ 4.5. Comparison to Surrogate-based null envelopes ‣ 4. Construction of Surrogate Null Models ‣ Null-Validated Topological Signatures of Financial Market Dynamics"), we compare the observed time series of L1L^{1} norm of the persistence landscape to pointwise null envelopes obtained from shuffle surrogates. Because shuffle surrogates preserve the marginal distribution of returns but destroy all temporal ordering, exceedances relative to this envelope indicate sensitivity of the windowed norms to temporal dependence.

The series frequently exceeds the upper bound of the shuffle null envelope, particularly during pronounced volatility episodes in early 20212021 and mid 20222022, where the landscape norm rises well above what is expected under random reordering of returns. These excursions indicate that the topological signal captured by the sliding-window embeddings is not explained by the empirical distribution of returns alone and depends critically on temporal ordering.

At the same time, there are periods, most notably during relatively calm market regimes, where the norm of the persistence landscape falls within or below the shuffle envelope, suggesting that during these intervals the windowed topological signal is closer to that expected under weak or absent temporal dependence.

The exceedance rates confirm that a non-negligible fraction of windows lie above the 95% shuffle envelope, with rejection frequencies well above the nominal 5% level. This supports rejection of the hypothesis that the norm of the persistence landscapes arises solely from the marginal distribution of Bitcoin log returns.

#### 4.5.2. FFT phase-randomized surrogate comparison

In Figure [9](https://arxiv.org/html/2602.00383v1#S4.F9 "Figure 9 ‣ 4.5.2. FFT phase-randomized surrogate comparison ‣ 4.5. Comparison to Surrogate-based null envelopes ‣ 4. Construction of Surrogate Null Models ‣ Null-Validated Topological Signatures of Financial Market Dynamics"), we compare the observed persistence landscape norm to null envelopes generated by FFT phase randomized surrogates. These surrogates preserve the power spectrum and hence linear second order temporal structure while destroying nonlinear and phase-dependent dependencies.

Relative to this more restrictive null, the norm exhibits a different pattern. While occasional excursions above the FFT envelope occur, they are markedly fewer and more localized than in the shuffle case. In many periods, particularly after 2022, the series lies persistently below the mean of the FFT null ensemble, and often near the lower edge of the envelope.

This behavior indicates that the norm of persistent landscape is sensitive to structure beyond linear correlation alone. The suppression of the norm relative to the FFT null suggests that nonlinear temporal organization present in {zt}\{z\_{t}\} constrains the geometry of the delay embedded point clouds in a way that is not reproduced by phase randomized surrogates.

![Refer to caption](x9.png)


Figure 9. Comparison of L1L^{1} norm of the persistence landscape (blue) to null envelopes generated by FFT phase randomized surrogates.

Both of these results demonstrate that the L1L^{1} norm of the persistence landscape derived from Bitcoin log returns exhibits temporal structure that cannot be explained by either the marginal distribution alone or by linear second-order temporal dependence. The shuffle surrogate analysis establishes sensitivity to temporal ordering, while the FFT phase randomized analysis indicates structure beyond that captured by linear correlations.

## 5. Conclusions

We introduce a null-validated topological measure for quantifying market complexity and establish that it captures geometric and temporal structure in Bitcoin log return dynamics that is not reducible to sentiment or latent stochastic volatility. The analysis treats the L1L^{1} norm of the persistence landscape derived from sliding-window delay embeddings as a scalar summary of reconstructed state-space geometry and demonstrates its sensitivity to nontrivial temporal organization.

Comparison with filtered stochastic volatility estimates shows that the persistence-landscape norm and volatility encode distinct dynamical information. During high stress regimes, the two quantities exhibit strong positive association, whereas outside these regimes the dependence may weaken and become unstable. Rolling correlation analysis confirms that the coupling between topology and volatility is non-stationary, with a dominant regime shift separating periods of strong alignment from those characterized by weak or fluctuating association. The persistence of elevated topological signal during low volatility intervals implies that geometric organization in delay space is not eliminated by volatility normalization.

Surrogate based null models provide statistical validation of these observations. Rejection of shuffle surrogates demonstrates that the persistence landscape norm depends on temporal ordering and is not determined solely by the marginal distribution of Bitcoin log returns.
Departures from FFT phase randomized surrogates further indicate sensitivity to nonlinear and phase dependent temporal dependencies beyond linear second order structure. While the precise mechanisms driving pronounced peaks in the persistence landscape norm remain an open question, the surrogate-based analysis establishes that these features cannot be explained by marginal distributions or linear correlation structure alone.

Overall, the analysis establishes the L1L^{1} norm of the persistence landscape as a mathematically interpretable and statistically validated descriptor of market dynamics.
Nontrivial geometric structure persists in Bitcoin log returns even after accounting for volatility and sentiment effects.
This framework provides a principled approach for detecting regime dependent organization in financial time series and suggests that topological methods can reveal coherent dynamical structure in regimes where conventional scale-based measures indicate apparent market calm.

An important direction for future work is the application of the null validated topological framework developed here to other asset classes and financial markets, including major U.S. equity indices, fixed income instruments, and cross-asset systems such as major stock indices and commodity markets. Extending the analysis to these settings would allow for systematic comparison of geometric and temporal organization across market structures and time scales, and would help assess the generality of topological signatures observed in cryptocurrency markets. From a methodological perspective, future work may also incorporate more restrictive surrogate constructions, such as iterated amplitude adjusted Fourier transform surrogates, to further disentangle nonlinear temporal structure from linear dependence and marginal distribution effects.

## Acknowledgement

I would like to thank Marian Gidea for helpful discussions and valuable feedback.

## References

* [1]
  S. W. Akingbade, M. Gidea, M. Manzi, and V. Nateghi (2024)
  Why topological data analysis detects financial bubbles?.
  Communications in Nonlinear Science and Numerical Simulation.
  External Links: [Document](https://dx.doi.org/10.1016/j.cnsns.2023.107665)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p4.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics"),
  [§2.2](https://arxiv.org/html/2602.00383v1#S2.SS2.p1.1 "2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [2]
  S. W. Akingbade (2024)
  Applications of dynamical systems in dissipative mechanics and in topological data analysis.
  Ph.D. Thesis, Yeshiva University, New York.
  External Links: [Link](https://repository.yu.edu/server/api/core/bitstreams/5235c0f7-7a0b-4b3a-83ff-c04a3f103f32/content)
  Cited by: [§2.2](https://arxiv.org/html/2602.00383v1#S2.SS2.p1.1 "2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [3]
  Alternative.me.
  Note: <https://alternative.me/crypto/api/>Accessed December, 2025
  Cited by: [§2.2.3](https://arxiv.org/html/2602.00383v1#S2.SS2.SSS3.p2.1 "2.2.3. Distribution of L1 norms across sentiment regimes ‣ 2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [4]
  S. Arvanitis and M. Detsis (2024)
  Mild explocivity, persistent homology and cryptocurrencies’ bubbles: an empirical exercise.
  AIMS Mathematics 9 (1),  pp. 896–917.
  External Links: [Document](https://dx.doi.org/10.3934/math.2024045)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p4.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [5]
  P. Bubenik and P. Dłotko (2017)
  A persistence landscapes toolbox for topological statistics.
  Journal of Symbolic Computation 78,  pp. 91–114.
  Cited by: [§2.1](https://arxiv.org/html/2602.00383v1#S2.SS1.p1.1 "2.1. Persistent homology ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [6]
  P. Bubenik et al. (2015)
  Statistical topological data analysis using persistence landscapes..
  J. Mach. Learn. Res. 16 (1),  pp. 77–102.
  Cited by: [§2.1.3](https://arxiv.org/html/2602.00383v1#S2.SS1.SSS3.p3.3 "2.1.3. Persistence landscapes ‣ 2.1. Persistent homology ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics"),
  [§2.1](https://arxiv.org/html/2602.00383v1#S2.SS1.p1.1 "2.1. Persistent homology ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [7]
  P. Bubenik (2018)
  The persistence landscape and some of its properties.
  External Links: 1810.04963
  Cited by: [§2.1](https://arxiv.org/html/2602.00383v1#S2.SS1.p1.1 "2.1. Persistent homology ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [8]
  H. Edelsbrunner and J. L. Harer (2022)
  Computational topology: an introduction.
   American Mathematical Society.
  Cited by: [§2.1](https://arxiv.org/html/2602.00383v1#S2.SS1.p1.1 "2.1. Persistent homology ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [9]
  B. Gaies, M. S. Nakhli, J. Sahut, and D. Schweizer (2023)
  Interactions between investors’ fear and greed sentiment and bitcoin prices.
  The North American Journal of Economics and Finance 67,  pp. 101924.
  External Links: [Document](https://dx.doi.org/10.1016/j.najef.2023.101924)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p6.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [10]
  M. Gidea, D. Goldsmith, Y. Katz, P. Roldan, and Y. Shmalo (2020)
  Topological recognition of critical transitions in time series of cryptocurrencies.
  Physica A: Statistical Mechanics and its Applications 548,  pp. 123843.
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p4.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics"),
  [§2.2](https://arxiv.org/html/2602.00383v1#S2.SS2.p1.1 "2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [11]
  M. Gidea and Y. Katz (2018)
  Topological data analysis of financial time series: Landscapes of crashes.
  Physica A: Statistical Mechanics and its Applications 491,  pp. 820–834.
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p4.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [12]
  M. Gidea (2017)
  Topological data analysis of critical transitions in financial networks.
  In International conference and school on network science,
   pp. 47–59.
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p4.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [13]
  A. Goel, D. Filipović, and P. Pasricha (2025)
  Sparse portfolio selection via topological data analysis based clustering.
  Quantitative Finance 25 (8),  pp. 1261–1291.
  External Links: [Document](https://dx.doi.org/10.1080/14697688.2025.2544762)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p4.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [14]
  A. Goel, P. Pasricha, and J. Kanniainen (2026)
  Risk reduced sparse index tracking portfolio: a topological data analysis approach.
  Omega 138,  pp. 103432.
  External Links: [Document](https://dx.doi.org/10.1016/j.omega.2025.103432)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p4.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [15]
  A. C. Harvey, E. Ruiz, and N. Shephard (1994)
  Multivariate stochastic variance models.
  Review of Economic Studies 61 (2),  pp. 247–264.
  Cited by: [§3.1.2](https://arxiv.org/html/2602.00383v1#S3.SS1.SSS2.p2.2 "3.1.2. Observation (measurement) equation ‣ 3.1. Stochastic volatility model ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [16]
  M. He, L. Shen, Y. Zhang, and Y. Zhang (2023)
  Predicting cryptocurrency returns for real-world investments: a daily updated and accessible predictor.
  Finance Research Letters 58,  pp. 104406.
  External Links: [Document](https://dx.doi.org/10.1016/j.frl.2023.104406)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p6.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [17]
  J. Hull and A. White (1987)
  The pricing of options on assets with stochastic volatilities.
  The Journal of Finance 42 (2),  pp. 281–300.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.1987.tb02568.x)
  Cited by: [§3.1.2](https://arxiv.org/html/2602.00383v1#S3.SS1.SSS2.p2.2 "3.1.2. Observation (measurement) equation ‣ 3.1. Stochastic volatility model ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [18]
  E. L. Ionides, A. Bhadra, Y. Atchadé, and A. A. King (2011)
  Iterated filtering.
  Annals of Statistics 39 (3),  pp. 1776–1802.
  Cited by: [§3.2](https://arxiv.org/html/2602.00383v1#S3.SS2.p4.1 "3.2. Inference and parameter estimation ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [19]
  M. S. Ismail, M. S. Md Noorani, M. Ismail, F. Abdul Razak, and M. A. Alias (2021)
  Early warning signals of financial crises using persistent homology.
  Physica A: Statistical Mechanics and its Applications 586,  pp. 126459.
  External Links: [Document](https://dx.doi.org/10.1016/j.physa.2021.126459)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p4.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [20]
  S. Kim, N. Shephard, and S. Chib (1998)
  Stochastic volatility: likelihood inference and comparison with arch models.
  Review of Economic Studies 65 (3),  pp. 361–393.
  Cited by: [§3.1.2](https://arxiv.org/html/2602.00383v1#S3.SS1.SSS2.p2.2 "3.1.2. Observation (measurement) equation ‣ 3.1. Stochastic volatility model ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [21]
  A. A. King, D. Nguyen, and E. L. Ionides (2016)
  Statistical inference for partially observed markov processes via the R package pomp.
  Journal of Statistical Software 69 (12),  pp. 1–43.
  Cited by: [§3.2](https://arxiv.org/html/2602.00383v1#S3.SS2.p4.1 "3.2. Inference and parameter estimation ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [22]
  J. A. Perea and J. Harer (2015)
  Sliding windows and persistence: an application of topological methods to signal analysis.
  Foundations of Computational Mathematics 15 (3),  pp. 799–838.
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p3.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [23]
  T. Pereira, A. Carvalho, L. Wahl, and J. Kurths (2018)
  Persistent homology of time-dependent functional networks constructed from coupled time series.
  Chaos: An Interdisciplinary Journal of Nonlinear Science 28 (3),  pp. 033103.
  External Links: [Document](https://dx.doi.org/10.1063/1.4978997)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p2.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [24]
  R. Rivera-Castro, P. Pilyugina, and E. Burnaev (2019)
  Topological data analysis for portfolio management of cryptocurrencies.
  In 2019 International Conference on Data Mining Workshops (ICDMW),
   pp. 238–243.
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p4.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [25]
  S. Rudkin, W. Qiu, and P. Dlotko (2021)
  Uncertainty, volatility and the persistence norms of financial time series.
  arXiv preprint arXiv:2110.00098.
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p5.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [26]
  P. Saengduean, S. Noisagool, and F. Chamchod (2020)
  Topological data analysis for identifying critical transitions in cryptocurrency time series.
  In 2020 IEEE International Conference on Industrial Engineering and Engineering Management (IEEM),
  Vol. ,  pp. 933–938.
  External Links: [Document](https://dx.doi.org/10.1109/IEEM45057.2020.9309855)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p4.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [27]
  T. Schreiber and A. Schmitz (2000)
  Surrogate time series.
  Physica D: Nonlinear Phenomena 142 (3–4),  pp. 346–382.
  External Links: [Document](https://dx.doi.org/10.1016/S0167-2789%2800%2900043-9)
  Cited by: [§4.2](https://arxiv.org/html/2602.00383v1#S4.SS2.p3.1 "4.2. FFT phase-randomized surrogate ‣ 4. Construction of Surrogate Null Models ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [28]
  N. Shephard (1996)
  Statistical aspects of arch and stochastic volatility.
  In Time Series Models in Econometrics, Finance and Other Fields, D. R. Cox, D. V. Hinkley, and O. E. Barndorff-Nielsen (Eds.),
   pp. 1–67.
  Cited by: [§3.1.2](https://arxiv.org/html/2602.00383v1#S3.SS1.SSS2.p2.2 "3.1.2. Observation (measurement) equation ‣ 3.1. Stochastic volatility model ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [29]
  H. G. Souto (2023)
  Topological tail dependence: evidence from forecasting realized volatility.
  The Journal of Finance and Data Science 9,  pp. 100107.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfds.2023.100107)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p5.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [30]
  F. Takens (1981)
  Detecting strange attractors in turbulence.
  In Dynamical Systems and Turbulence, Warwick 1980, D. Rand and L. Young (Eds.),
  Berlin, Heidelberg,  pp. 366–381.
  External Links: ISBN 978-3-540-38945-3
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p3.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics"),
  [§2.2.1](https://arxiv.org/html/2602.00383v1#S2.SS2.SSS1.p2.7 "2.2.1. Choice of embedding dimension and delay. ‣ 2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [31]
  S. J. Taylor (1986)
  Modelling financial time series.
   John Wiley & Sons, Chichester.
  Cited by: [§3.1.2](https://arxiv.org/html/2602.00383v1#S3.SS1.SSS2.p2.2 "3.1.2. Observation (measurement) equation ‣ 3.1. Stochastic volatility model ‣ 3. Stochastic volatility modeling of Bitcoin log returns ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [32]
  J. Theiler, S. Eubank, A. Longtin, B. Galdrikian, and J. D. Farmer (1992)
  Testing for nonlinearity in time series: the method of surrogate data.
  Physica D: Nonlinear Phenomena 58 (1–4),  pp. 77–94.
  External Links: [Document](https://dx.doi.org/10.1016/0167-2789%2892%2990102-S)
  Cited by: [§4.2](https://arxiv.org/html/2602.00383v1#S4.SS2.p3.1 "4.2. FFT phase-randomized surrogate ‣ 4. Construction of Surrogate Null Models ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [33]
  S. Tim, A. Y. James, and C. Martin (1991)
  Embedology.
  Journal of Statistical Physics 65 (3-4),  pp. 579–616.
  Cited by: [§2.2.1](https://arxiv.org/html/2602.00383v1#S2.SS2.SSS1.p3.3 "2.2.1. Choice of embedding dimension and delay. ‣ 2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [34]
  J. Wang, H. Liu, and Y. Hsu (2024)
  A u-shaped relationship between the crypto fear-greed index and the price synchronicity of cryptocurrencies.
  Finance Research Letters 59,  pp. 104763.
  External Links: [Document](https://dx.doi.org/10.1016/j.frl.2023.104763)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p6.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [35]
  Yahoo finance.
  Note: <https://finance.yahoo.com/>Accessed December, 2025
  Cited by: [§2.2.2](https://arxiv.org/html/2602.00383v1#S2.SS2.SSS2.p3.1 "2.2.2. Topological summaries of Bitcoin log return dynamics ‣ 2.2. Application to time series ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [36]
  J. Yao, J. Li, J. Wu, M. Yang, and X. Wang (2025)
  Change point detection in financial market using topological data analysis.
  Systems 13 (10),  pp. 875.
  External Links: [Document](https://dx.doi.org/10.3390/systems13100875)
  Cited by: [§1](https://arxiv.org/html/2602.00383v1#S1.p5.1 "1. Introduction ‣ Null-Validated Topological Signatures of Financial Market Dynamics").
* [37]
  A. Zomorodian and G. Carlsson (2005)
  Computing persistent homology.
  Discrete & Computational Geometry 33 (2),  pp. 249–274.
  External Links: [Document](https://dx.doi.org/10.1007/s00454-004-1146-y)
  Cited by: [§2.1.1](https://arxiv.org/html/2602.00383v1#S2.SS1.SSS1.p4.2 "2.1.1. Persistent homology ‣ 2.1. Persistent homology ‣ 2. Background ‣ Null-Validated Topological Signatures of Financial Market Dynamics").