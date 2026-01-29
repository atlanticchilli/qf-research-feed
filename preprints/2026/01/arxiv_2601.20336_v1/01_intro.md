---
authors:
- Murad Farzulla
doc_id: arxiv:2601.20336v1
family_id: arxiv:2601.20336
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency
  Factor Analysis
url_abs: http://arxiv.org/abs/2601.20336v1
url_html: https://arxiv.org/html/2601.20336v1
venue: arXiv q-fin
version: 1
year: 2026
---


Murad Farzulla1
  
1 King’s College London
  
[ORCID: 0009-0002-7164-8704](https://orcid.org/0009-0002-7164-8704)

(January 2026
  
Corresponding Author: [murad@dissensus.ai](mailto:murad@dissensus.ai))

###### Abstract

Cryptocurrency projects articulate their value propositions through whitepapers, making foundational claims about functionality, use cases, and technical capabilities. This study investigates whether these narrative claims align with empirically observed market behavior. We construct a novel pipeline combining natural language processing (NLP) with tensor decomposition to compare three representational spaces: (1) a claims matrix derived from zero-shot classification of 24 whitepapers across 10 semantic categories using BART-MNLI, (2) a market statistics matrix capturing 7 financial metrics for 49 cryptocurrency assets over two years of hourly data (17,543 timestamps), and (3) latent factors extracted via CP tensor decomposition (rank 2, explaining 92.45% of variance). Using Procrustes rotation and Tucker’s congruence coefficient (ϕ\phi), we test alignment between narrative and market spaces across 23 common entities.

Results indicate weak alignment: claims–statistics (ϕ=0.341\phi=0.341, p=0.332p=0.332), claims–factors (ϕ=0.077\phi=0.077, p=0.747p=0.747; a less conservative non-padded estimate yields ϕ≈0.31\phi\approx 0.31 in matched dimensions, see Appendix [E](https://arxiv.org/html/2601.20336v1#A5 "Appendix E Per-Dimension Alignment Values ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis")), and statistics–factors (ϕ=0.197\phi=0.197, p<0.001p<0.001). Critically, the statistics–factors significance (p<0.001p<0.001) validates our methodology: since both matrices derive from the same market data, significant alignment confirms the Procrustes pipeline detects relationships when present, establishing that the narrative null result represents observed weak alignment rather than measurement failure. Inter-model validation using DeBERTa-v3 yields 32% exact agreement (Cohen’s κ=0.14\kappa=0.14) but 67% relaxed (top-3) agreement, indicating models capture similar semantic neighborhoods with different decision boundaries. Cross-sectional analysis reveals NEAR, MKR, and ATOM exhibit modest positive alignment contributions, while ENS, UNI, and Bitcoin show the largest divergence. Excluding Bitcoin (n=22n=22) yields ϕ=0.081\phi=0.081 for claims–factors, confirming the null result is not driven by Bitcoin’s dominant market position.

We interpret these findings as consistent with weak alignment between whitepaper narratives and realized market factor structure. Limited statistical power (n=23n=23) precludes distinguishing weak alignment from no alignment, but we can confidently reject strong alignment (ϕ≥0.70\phi\geq 0.70). Implications for narrative economics, market efficiency, and investment analysis are discussed.

Keywords: Cryptocurrency, Tensor Decomposition, NLP, Factor Analysis, Procrustes Rotation, Tucker’s Congruence Coefficient, Zero-Shot Classification

JEL Codes: G14, G12, C38, C45

Acknowledgements. The author acknowledges Claude (Anthropic) for assistance with pipeline development, mathematical exposition, and technical writing. All errors, omissions, and interpretive limitations remain the author’s responsibility.

Data & Code Availability. Reproducible code and data are available at <https://github.com/studiofarzulla/tensor-defi>.

## 1 Introduction

Cryptocurrency markets present a unique laboratory for studying the relationship between narrative and price. Unlike traditional equities, where value propositions emerge gradually through earnings reports and analyst coverage, cryptocurrency projects typically articulate comprehensive visions at inception through whitepapers. These foundational documents make explicit claims about functionality, use cases, and technical architecture—claims that should, in principle, relate to how assets behave in markets.

The efficient market hypothesis suggests that asset prices reflect available information (Fama, [1970](https://arxiv.org/html/2601.20336v1#bib.bib1 "Efficient capital markets: a review of theory and empirical work")). If whitepapers constitute meaningful information about project characteristics, we might expect narrative claims to align with market behavior. Conversely, Shiller ([2017](https://arxiv.org/html/2601.20336v1#bib.bib4 "Narrative economics")) argues that “narrative economics” drives market dynamics through stories that spread virally, potentially decoupling prices from fundamentals. Recent work has begun examining this in cryptocurrency markets, with Aste ([2019](https://arxiv.org/html/2601.20336v1#bib.bib23 "Cryptocurrency market structure: connecting emotions and economics")) documenting significant correlations between prices and sentiment across nearly two thousand cryptocurrencies. Shiller’s framework emphasizes how narratives propagate and influence aggregate behavior; we adapt this insight to test a related but distinct hypothesis about structural alignment between project-level narratives and market factor structure.

This tension motivates our central research question: Do whitepaper claims predict market behavior? Specifically, do the functional narratives articulated in project whitepapers align with empirically observed market factor structure? We emphasize that our methodology measures contemporaneous structural alignment between representational spaces rather than predictive relationships; the term “predict” in our research question should be understood as “exhibit structural correspondence with” rather than temporal forecasting.

We address this question through a novel methodological pipeline combining natural language processing with tensor decomposition. Our approach constructs three distinct representational spaces:

1. 1.

   A claims matrix 𝐂∈ℝN×K\mathbf{C}\in\mathbb{R}^{N\times K} derived from zero-shot classification of whitepaper text across K=10K=10 semantic categories
2. 2.

   A market statistics matrix 𝐒∈ℝM×J\mathbf{S}\in\mathbb{R}^{M\times J} capturing J=7J=7 financial metrics across M=49M=49 assets
3. 3.

   Latent factors 𝐅∈ℝM×R\mathbf{F}\in\mathbb{R}^{M\times R} extracted from a high-dimensional market tensor via CP decomposition

Using Procrustes rotation and Tucker’s congruence coefficient, we then test whether these spaces align—whether assets that make similar claims exhibit similar market behavior.

Our findings reveal weak alignment across comparisons (ϕ<0.35\phi<0.35), with one notable exception: the statistics–factors comparison achieves statistical significance (p<0.001p<0.001) despite weak magnitude, indicating systematic correspondence between market metrics and tensor-derived factors that narrative claims fail to capture. Infrastructure tokens (NEAR, MKR, ATOM) show modest positive alignment, while ENS, UNI, and Bitcoin exhibit the largest narrative-market divergence. This result is robust to temporal variation, subsample perturbation, decomposition method (CP vs Tucker), and rank selection.

Contributions. This paper makes four contributions: (1) we introduce a reproducible pipeline for comparing textual and market representational spaces in cryptocurrency research, (2) we provide detailed methodological exposition of tensor decomposition for factor extraction, (3) we deliver rigorous empirical evidence on the (mis)alignment between project narratives and market behavior, and (4) we demonstrate that null results in this domain constitute valid findings with implications for narrative economics.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2601.20336v1#S2 "2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") reviews related work. Section [3](https://arxiv.org/html/2601.20336v1#S3 "3 Data ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") describes our data sources. Section [4](https://arxiv.org/html/2601.20336v1#S4 "4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") provides detailed methodology with full mathematical exposition. Section [5](https://arxiv.org/html/2601.20336v1#S5 "5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") presents comprehensive results including sensitivity analyses. Section [6](https://arxiv.org/html/2601.20336v1#S6 "6 Discussion ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") interprets findings, and Section [7](https://arxiv.org/html/2601.20336v1#S7 "7 Conclusions ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") concludes.

## 2 Related Work

### 2.1 Cryptocurrency Narratives and Sentiment

Research on cryptocurrency narratives spans social media analysis, whitepaper studies, and sentiment measurement. Chen et al. ([2019](https://arxiv.org/html/2601.20336v1#bib.bib5 "Bitcoin price prediction using machine learning: an approach to sample dimension engineering")) show that Twitter sentiment predicts Bitcoin returns at short horizons, while Ante ([2023](https://arxiv.org/html/2601.20336v1#bib.bib6 "How Elon Musk’s Twitter activity moves cryptocurrency markets")) find that Elon Musk’s tweets generate significant abnormal returns for mentioned cryptocurrencies. Haykir and Yağlı ([2022](https://arxiv.org/html/2601.20336v1#bib.bib7 "Speculative bubbles and herding in cryptocurrencies")) document speculative bubbles driven by herding behavior across crypto assets. Liu and Tsyvinski ([2021](https://arxiv.org/html/2601.20336v1#bib.bib18 "Risks and returns of cryptocurrency")) establish that cryptocurrency returns exhibit momentum, size effects, and exposure to market-wide factors distinct from traditional assets.

Whitepaper analysis has received comparatively less attention. Howell et al. ([2020](https://arxiv.org/html/2601.20336v1#bib.bib8 "Initial coin offerings: financing growth with cryptocurrency token sales")) examine ICO whitepaper quality as a signal of project legitimacy, finding that technical depth correlates with fundraising success. Fisch ([2019](https://arxiv.org/html/2601.20336v1#bib.bib9 "Initial coin offerings (ICOs) to finance new ventures")) show that whitepaper informativeness predicts ICO outcomes, and Florysiak and Schandlbauer ([2022](https://arxiv.org/html/2601.20336v1#bib.bib36 "Experts or charlatans? ICO analysts and white paper informativeness")) find that analyst assessments of whitepaper quality correlate with funding success. However, these studies focus on cross-sectional prediction at issuance rather than ongoing alignment between narrative and market behavior. Indeed, Suriano et al. ([2025](https://arxiv.org/html/2601.20336v1#bib.bib35 "Information theory quantifiers in cryptocurrency time series analysis")) find that clustering cryptocurrencies by whitepaper content does not yield significant differences in time series dynamics, suggesting narratives may matter for initial fundraising but not long-term price behavior. Recent high-profile failures illustrate the gap between whitepaper claims and realized outcomes: Briola et al. ([2022](https://arxiv.org/html/2601.20336v1#bib.bib30 "Anatomy of a stablecoin’s failure: the Terra-Luna case")) analyze the Terra-Luna collapse, demonstrating how algorithmic stablecoin mechanisms failed despite elaborate whitepaper specifications, while Vidal-Tomás et al. ([2023](https://arxiv.org/html/2601.20336v1#bib.bib31 "FTX’s downfall and Binance’s consolidation: the fragility of centralized digital finance")) document how centralized exchange fragility propagates through cryptocurrency markets.

Narrative Economics Framework. Shiller ([2017](https://arxiv.org/html/2601.20336v1#bib.bib4 "Narrative economics")) provides the theoretical foundation for studying how narratives shape economic outcomes, emphasizing how stories spread virally and influence collective behavior. Applied to cryptocurrency, this framework suggests that project narratives—embodied in whitepapers—should influence investor beliefs and thus market prices. Our study tests a related hypothesis: whether project narratives exhibit structural alignment with market factor structure. This differs from Shiller’s focus on narrative contagion dynamics; we examine whether the content of narratives corresponds to realized market behavior, finding limited support for such correspondence. This complements information-theoretic approaches (Keskin and Aste, [2020](https://arxiv.org/html/2601.20336v1#bib.bib24 "Information-theoretic measures for nonlinear causality detection: application to social media sentiment and cryptocurrency prices")) that find nonlinear causality between social sentiment and cryptocurrency returns.

Natural Language Processing in Finance. The application of NLP to financial text has grown substantially, with transformer-based models enabling sophisticated document analysis. Zero-shot classification, as employed here, allows categorization without domain-specific training data (Lewis et al., [2020](https://arxiv.org/html/2601.20336v1#bib.bib17 "BART: denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension")). Bartolucci et al. ([2020](https://arxiv.org/html/2601.20336v1#bib.bib32 "The butterfly “affect”: impact of development practices on cryptocurrency prices")) demonstrate that sentiment extracted from developer communications (GitHub) predicts cryptocurrency price movements, validating NLP approaches in this domain. However, the trade-off between scalability and domain expertise remains an open question. Our use of BART-MNLI represents a middle ground—leveraging powerful pre-trained representations while acknowledging potential limitations in cryptocurrency-specific semantics.

Cryptocurrency Market Microstructure. Beyond sentiment, cryptocurrency markets exhibit distinctive microstructure features: 24/7 trading, global fragmentation across exchanges, varying levels of market manipulation, and high correlation with Bitcoin. These features may dominate narrative effects. Pappalardo et al. ([2018](https://arxiv.org/html/2601.20336v1#bib.bib33 "Blockchain inefficiency in the Bitcoin peers network")) document inefficiencies in Bitcoin’s peer-to-peer network that diverge from whitepaper ideals of decentralization. Farzulla ([2025](https://arxiv.org/html/2601.20336v1#bib.bib19 "Market reaction asymmetry: infrastructure disruption dominance over regulatory uncertainty in cryptocurrency volatility")) demonstrate that infrastructure disruption events generate significantly larger volatility responses than regulatory announcements, suggesting market participants weight technical fundamentals over policy uncertainty. This asymmetry—where operational failures matter more than regulatory shifts—implies that whitepaper claims about technical capabilities may warrant particular attention in volatility modeling. Our inclusion of multiple market statistics (volatility, liquidity, drawdown) attempts to capture this microstructure, but residual factors may remain.

### 2.2 Factor Models in Cryptocurrency

Traditional asset pricing employs factor models to explain cross-sectional return variation. Fama and French ([1993](https://arxiv.org/html/2601.20336v1#bib.bib2 "Common risk factors in the returns on stocks and bonds")) established the theoretical foundation for factor-based explanations of cross-sectional returns. Livan et al. ([2011](https://arxiv.org/html/2601.20336v1#bib.bib26 "Fine structure of spectral properties for random correlation matrices: an application to financial markets")) demonstrate how random matrix theory can distinguish signal from noise in financial correlation matrices—a perspective we extend to narrative-factor comparisons. Caccioli et al. ([2018](https://arxiv.org/html/2601.20336v1#bib.bib34 "Network models of financial systemic risk: a review")) provide a comprehensive review of network-based approaches to financial systemic risk, complementing factor-based perspectives with topological analysis. In cryptocurrency, factor model development remains nascent but growing.

Liu and Tsyvinski ([2021](https://arxiv.org/html/2601.20336v1#bib.bib18 "Risks and returns of cryptocurrency")) propose a three-factor model for cryptocurrency returns: market, size, and momentum. They find that these factors explain substantial cross-sectional variation, analogous to the Fama-French factors for equities. Our tensor decomposition implicitly captures similar factors—Factor 1 (dominated by Bitcoin) resembles their market factor, while Factor 2 may capture size or sector effects.

Recent work has explored additional factors specific to cryptocurrency: network effects (measured by active addresses), tokenomics (supply schedule, staking yields), and on-chain activity (transaction volume, developer commits). These factors may mediate narrative-market relationships in ways our current analysis does not capture.

Multi-Way Data in Finance. Financial data naturally exhibits multi-way structure: assets ×\times time ×\times features. While matrix methods (PCA, factor analysis) collapse this structure, tensor decomposition preserves it. Our work contributes to the emerging literature applying tensor methods to financial data, demonstrating both their utility (interpretable factors) and limitations (modest alignment despite high explanatory power).

### 2.3 Tensor Methods in Finance

Tensor decomposition provides a natural framework for analyzing multi-way financial data. Kolda and Bader ([2009](https://arxiv.org/html/2601.20336v1#bib.bib10 "Tensor decompositions and applications")) provide a comprehensive review of tensor decomposition methods, establishing the theoretical foundations for CP and Tucker decomposition. In finance, Chen et al. ([2022](https://arxiv.org/html/2601.20336v1#bib.bib11 "Factor models for high-dimensional tensor time series")) develop factor models for high-dimensional tensor time series, establishing the statistical foundations for tensor factor analysis. Fan et al. ([2013](https://arxiv.org/html/2601.20336v1#bib.bib12 "Large covariance estimation by thresholding principal orthogonal complements")) introduce the POET estimator for high-dimensional covariance estimation with factor structure.

CP (CANDECOMP/PARAFAC) decomposition decomposes a tensor into rank-one components, extracting interpretable latent factors (Harshman, [1970](https://arxiv.org/html/2601.20336v1#bib.bib13 "Foundations of the PARAFAC procedure: models and conditions for an “explanatory” multimodal factor analysis")). For market data structured as (time ×\times asset ×\times feature), CP decomposition yields asset-level factor loadings analogous to principal component analysis but preserving multi-way structure. Tucker decomposition offers an alternative with mode-specific ranks and a core tensor capturing interactions.

### 2.4 Factor Comparison Methods

Comparing factor structures across studies or datasets requires methods that account for rotational indeterminacy. Procrustes rotation (Schönemann, [1966](https://arxiv.org/html/2601.20336v1#bib.bib14 "A generalized solution of the orthogonal Procrustes problem")) finds the optimal orthogonal transformation aligning one factor matrix to another. Tucker’s congruence coefficient (ϕ\phi) then measures similarity between aligned factors (Tucker, [1951](https://arxiv.org/html/2601.20336v1#bib.bib15 "A method for synthesis of factor analysis studies"); Lorenzo-Seva and ten Berge, [2006](https://arxiv.org/html/2601.20336v1#bib.bib16 "Tucker’s congruence coefficient as a meaningful index of factor similarity")).

Lorenzo-Seva and ten Berge ([2006](https://arxiv.org/html/2601.20336v1#bib.bib16 "Tucker’s congruence coefficient as a meaningful index of factor similarity")) establish interpretation thresholds: |ϕ|≥0.95|\phi|\geq 0.95 indicates factor equivalence, |ϕ|≥0.85|\phi|\geq 0.85 indicates fair similarity, |ϕ|≥0.65|\phi|\geq 0.65 indicates moderate similarity, and |ϕ|<0.65|\phi|<0.65 indicates weak or no similarity. These thresholds guide our interpretation of narrative-market alignment.

## 3 Data

### 3.1 Market Data

We collect hourly OHLCV (open, high, low, close, volume) data from Binance for 49 cryptocurrency assets spanning January 1, 2023 to December 31, 2024, yielding 17,543 timestamps per asset. Asset selection follows liquidity and data availability criteria, including major cryptocurrencies (BTC, ETH) and a diverse set of DeFi, infrastructure, and utility tokens.

Table [1](https://arxiv.org/html/2601.20336v1#S3.T1 "Table 1 ‣ 3.1 Market Data ‣ 3 Data ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") summarizes the dataset dimensions.

Table 1: Dataset Summary

| Dimension | Value |
| --- | --- |
| Assets (market data) | 49 |
| Assets (whitepapers) | 24 |
| Assets (common intersection) | 23 |
| Time period | Jan 2023 – Dec 2024 |
| Timestamps (hourly) | 17,543 |
| Market features (OHLCV) | 5 |
| Derived statistics | 7 |
| Narrative categories | 10 |

### 3.2 Whitepaper Corpus

We collect whitepapers for 24 assets where official foundational documents are publicly available: AAVE, ADA, ALGO, AR, ARB, ATOM, AVAX, BTC, COMP, DOT, ENS, ETH, FIL, GRT, ICP, LINK, MKR, NEAR, SC, SOL, STORJ, UNI, XMR, and ZEC. Documents include original whitepapers, consensus papers, protocol specifications, and technical documentation. PDF text is extracted using PyPDF2 with sentence-level tokenization; for assets without extractable PDFs, we use official documentation in markdown format. Table [2](https://arxiv.org/html/2601.20336v1#S3.T2 "Table 2 ‣ 3.2 Whitepaper Corpus ‣ 3 Data ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") summarizes corpus statistics for selected assets.

Table 2: Whitepaper Corpus Statistics (Selected)

|  |  |  |  |
| --- | --- | --- | --- |
| Asset | Pages | Year | Type |
| ZEC | 229 | 2020 | Protocol Spec |
| STORJ | 90 | 2018 | Storage WP |
| ADA | 48 | 2020 | Consensus |
| ICP | 45 | 2021 | Tech Overview |
| LINK | 38 | 2017 | Oracle WP |
| FIL | 36 | 2017 | Tech Report |
| ETH | 36 | 2014 | Original WP |
| SOL | 32 | 2018 | Original WP |
| NEAR | 23 | 2020 | Sharding |
| MKR | 21 | 2017 | Stablecoin |
| XMR | 20 | 2013 | CryptoNote |
| + 13 additional documents (see Appendix) | | | |

The intersection of whitepaper and market data yields 23 common assets for alignment analysis (AR lacks sufficient market data coverage in our sample).

## 4 Methodology

Our pipeline proceeds in five stages: (1) tensor construction, (2) tensor decomposition, (3) NLP claims extraction, (4) market statistics computation, and (5) Procrustes alignment with congruence testing.

### 4.1 Tensor Construction

###### Definition 4.1 (Market Tensor).

A market tensor 𝒳∈ℝT×V×A×F\mathcal{X}\in\mathbb{R}^{T\times V\times A\times F} is a 4-way array with modes:

* •

  Time (T=17,543T=17,543 hourly timestamps)
* •

  Venue (V=1V=1, Binance)
* •

  Asset (A=49A=49 cryptocurrencies)
* •

  Feature (F=5F=5, OHLCV)

With a single venue, the effective structure is 3-way: 𝒳∈ℝT×A×F\mathcal{X}\in\mathbb{R}^{T\times A\times F}. Each entry xt​a​fx\_{taf} represents the value of feature ff for asset aa at time tt.

### 4.2 Tensor Decomposition

#### 4.2.1 CP Decomposition

###### Definition 4.2 (CP Decomposition).

The CANDECOMP/PARAFAC (CP) decomposition approximates a tensor as a sum of rank-one tensors:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒳≈∑r=1Rλr​𝐚r∘𝐛r∘𝐜r\mathcal{X}\approx\sum\_{r=1}^{R}\lambda\_{r}\,\mathbf{a}\_{r}\circ\mathbf{b}\_{r}\circ\mathbf{c}\_{r} |  | (1) |

where ∘\circ denotes outer product, λr\lambda\_{r} are weights, and 𝐚r∈ℝT\mathbf{a}\_{r}\in\mathbb{R}^{T}, 𝐛r∈ℝA\mathbf{b}\_{r}\in\mathbb{R}^{A}, 𝐜r∈ℝF\mathbf{c}\_{r}\in\mathbb{R}^{F} are mode-specific factor vectors.

The factor matrices are:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐀\displaystyle\mathbf{A} | =[𝐚1​|⋯|​𝐚R]∈ℝT×R(time factors)\displaystyle=[\mathbf{a}\_{1}|\cdots|\mathbf{a}\_{R}]\in\mathbb{R}^{T\times R}\quad\text{(time factors)} |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐁\displaystyle\mathbf{B} | =[𝐛1​|⋯|​𝐛R]∈ℝA×R(asset factors)\displaystyle=[\mathbf{b}\_{1}|\cdots|\mathbf{b}\_{R}]\in\mathbb{R}^{A\times R}\quad\text{(asset factors)} |  | (3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐂\displaystyle\mathbf{C} | =[𝐜1​|⋯|​𝐜R]∈ℝF×R(feature factors)\displaystyle=[\mathbf{c}\_{1}|\cdots|\mathbf{c}\_{R}]\in\mathbb{R}^{F\times R}\quad\text{(feature factors)} |  | (4) |

The asset factor matrix 𝐁\mathbf{B} provides latent loadings for alignment testing.

#### 4.2.2 Alternating Least Squares

CP decomposition is computed via alternating least squares (ALS):

Algorithm 1: CP-ALS

|  |  |
| --- | --- |
| 1: | Initialize 𝐀\mathbf{A}, 𝐁\mathbf{B}, 𝐂\mathbf{C} randomly |
| 2: | repeat |
| 3: | 𝐀←𝐗(1)​(𝐂⊙𝐁)​(𝐂⊤​𝐂∗𝐁⊤​𝐁)†\mathbf{A}\leftarrow\mathbf{X}\_{(1)}(\mathbf{C}\odot\mathbf{B})(\mathbf{C}^{\top}\mathbf{C}\*\mathbf{B}^{\top}\mathbf{B})^{\dagger} |
| 4: | 𝐁←𝐗(2)​(𝐂⊙𝐀)​(𝐂⊤​𝐂∗𝐀⊤​𝐀)†\mathbf{B}\leftarrow\mathbf{X}\_{(2)}(\mathbf{C}\odot\mathbf{A})(\mathbf{C}^{\top}\mathbf{C}\*\mathbf{A}^{\top}\mathbf{A})^{\dagger} |
| 5: | 𝐂←𝐗(3)​(𝐁⊙𝐀)​(𝐁⊤​𝐁∗𝐀⊤​𝐀)†\mathbf{C}\leftarrow\mathbf{X}\_{(3)}(\mathbf{B}\odot\mathbf{A})(\mathbf{B}^{\top}\mathbf{B}\*\mathbf{A}^{\top}\mathbf{A})^{\dagger} |
| 6: | until convergence |

where 𝐗(n)\mathbf{X}\_{(n)} is mode-nn matricization, ⊙\odot is Khatri-Rao product, ∗\* is Hadamard product, and †\dagger denotes pseudoinverse.

#### 4.2.3 Rank Selection

We select rank RR to achieve target explained variance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | EV​(R)=1−‖𝒳−𝒳^R‖F2‖𝒳−x¯‖F2\text{EV}(R)=1-\frac{\|\mathcal{X}-\hat{\mathcal{X}}\_{R}\|\_{F}^{2}}{\|\mathcal{X}-\bar{x}\|\_{F}^{2}} |  | (5) |

With target EV≥0.90\text{EV}\geq 0.90, we obtain R=2R=2 (EV = 92.45%).111Standard PCA on mode-2 (asset) matricization yields nearly identical alignment (ϕ=0.060\phi=0.060, vs CP ϕ=0.060\phi=0.060), confirming that preserving tensor structure does not alter our findings. We retain the tensor framework for interpretability of multi-way temporal dynamics and consistency with recent financial tensor methods (Chen et al., [2022](https://arxiv.org/html/2601.20336v1#bib.bib11 "Factor models for high-dimensional tensor time series")).

#### 4.2.4 Tucker Decomposition

For robustness, we also implement Tucker decomposition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒳≈𝒢×1𝐀×2𝐁×3𝐂\mathcal{X}\approx\mathcal{G}\times\_{1}\mathbf{A}\times\_{2}\mathbf{B}\times\_{3}\mathbf{C} |  | (6) |

where 𝒢∈ℝR1×R2×R3\mathcal{G}\in\mathbb{R}^{R\_{1}\times R\_{2}\times R\_{3}} is the core tensor and ×n\times\_{n} denotes mode-nn product.

### 4.3 NLP Claims Extraction

#### 4.3.1 Zero-Shot Classification

We employ BART-large-MNLI (Lewis et al., [2020](https://arxiv.org/html/2601.20336v1#bib.bib17 "BART: denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension")) for zero-shot text classification via the HuggingFace Transformers library.222Model: facebook/bart-large-mnli. BART-large fine-tuned on Multi-Genre Natural Language Inference (MNLI; Williams et al. [2018](https://arxiv.org/html/2601.20336v1#bib.bib21 "A broad-coverage challenge corpus for sentence understanding through inference")) for natural language inference. Whitepapers are segmented into 500-word chunks (n=2,056n=2{,}056 across 24 entities); this chunk size balances computational efficiency with context preservation, following common practice in large-scale text classification. Each chunk is classified against ten domain-relevant categories. Zero-shot classification follows the entailment approach of Yin et al. ([2019](https://arxiv.org/html/2601.20336v1#bib.bib20 "Benchmarking zero-shot text classification: datasets, evaluation and entailment approach")), constructing hypotheses of the form “This text is about [category]” for each candidate label.

Given a text segment tt and candidate labels {l1,…,lK}\{l\_{1},\ldots,l\_{K}\}, the model computes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(lk|t)=exp⁡(sk)∑j=1Kexp⁡(sj)P(l\_{k}|t)=\frac{\exp(s\_{k})}{\sum\_{j=1}^{K}\exp(s\_{j})} |  | (7) |

where sks\_{k} is the entailment score for label lkl\_{k}. Rather than argmax classification, we compute probability-weighted category profiles for each entity, providing smoother estimates that account for semantic ambiguity in technical prose.

#### 4.3.2 Semantic Taxonomy

Our taxonomy comprises K=10K=10 categories capturing core blockchain functionality (Table [3](https://arxiv.org/html/2601.20336v1#S4.T3 "Table 3 ‣ 4.3.2 Semantic Taxonomy ‣ 4.3 NLP Claims Extraction ‣ 4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis")).

Table 3: Semantic Category Taxonomy

| Category | Description |
| --- | --- |
| Store of Value | Digital gold, inflation hedge, wealth preservation |
| Medium of Exchange | Payment system, transactions, currency |
| Smart Contracts | Programmable contracts, automation, trustless execution |
| Decentralized Finance | Lending, borrowing, yield, liquidity provision |
| Governance | Voting, DAOs, community decision-making |
| Scalability | High throughput, low latency, Layer 2 solutions |
| Privacy | Anonymous transactions, zero-knowledge proofs |
| Interoperability | Cross-chain communication, bridges, multi-chain |
| Data Storage | Decentralized storage, file systems, permanence |
| Oracle Services | External data feeds, real-world information |

#### 4.3.3 Model Validation

We assess classification reliability through inter-model agreement using DeBERTa-v3 (He et al., [2021](https://arxiv.org/html/2601.20336v1#bib.bib29 "DeBERTa: decoding-enhanced BERT with disentangled attention")) as an alternative classifier.333Model: cross-encoder/nli-deberta-v3-small. On a random sample of 200 chunks, exact top-1 agreement is 32% (Cohen’s κ=0.14\kappa=0.14), reflecting known sensitivity of zero-shot NLI to model-specific category boundaries. However, relaxed agreement—where the alternative model’s top prediction appears in the primary model’s top-3—reaches 67%, suggesting models capture similar semantic neighborhoods with different decision thresholds. Recent advances in financial sentiment estimation using large language models (Kirtac and Germano, [2025](https://arxiv.org/html/2601.20336v1#bib.bib25 "Large language models in finance: what is financial sentiment?")) suggest alternative approaches for future work.

Bootstrap 95% confidence intervals on aggregate category proportions (1,000 resamples) yield tight bounds: Smart Contracts 26.3–30.1%, Scalability 18.4–22.1%, Governance 14.7–17.9%, indicating stable estimates at the corpus level despite chunk-level uncertainty.

#### 4.3.4 Aggregation

For each asset nn, we aggregate probability-weighted classification scores across text chunks:

|  |  |  |  |
| --- | --- | --- | --- |
|  | cn​k=1|Tn|​∑t∈TnP​(lk|t)c\_{nk}=\frac{1}{|T\_{n}|}\sum\_{t\in T\_{n}}P(l\_{k}|t) |  | (8) |

yielding claims matrix 𝐂∈ℝN×K\mathbf{C}\in\mathbb{R}^{N\times K}.

#### 4.3.5 Institutional Corpus (Snapshot)

To test whether broader institutional narratives improve alignment beyond static whitepapers, we construct a supplementary corpus capturing evolving utility positioning. This corpus includes official documentation, foundation updates, governance forum posts, and project blogs. For this analysis we use a February 2025 snapshot covering 14 assets (AAVE, ADA, AR, ARB, AVAX, BTC, ETH, FIL, IMX, LINK, MKR, OP, SOL, UNI), yielding 627 documents and 367,071 words. Of these, 12 have sufficient market data coverage for rolling window alignment analysis (AR and IMX excluded due to incomplete hourly data). We classify these documents using the same taxonomy to build an institutional claims matrix. With a single snapshot, the claims matrix is held constant across rolling market windows; future work extends this to multi-period narrative drift analysis.

### 4.4 Market Statistics

We compute seven z-normalized summary statistics for each asset:

1. 1.

   Mean return: r¯a=1T​∑tra​t\bar{r}\_{a}=\frac{1}{T}\sum\_{t}r\_{at}
2. 2.

   Volatility: σa=1T−1​∑t(ra​t−r¯a)2\sigma\_{a}=\sqrt{\frac{1}{T-1}\sum\_{t}(r\_{at}-\bar{r}\_{a})^{2}}
3. 3.

   Sharpe ratio444We use 252 trading days following traditional finance conventions for comparability with academic literature, though cryptocurrency markets operate continuously.: SRa=r¯aσa⋅252⋅24\text{SR}\_{a}=\frac{\bar{r}\_{a}}{\sigma\_{a}}\cdot\sqrt{252\cdot 24}
4. 4.

   Max drawdown: MDDa=mint⁡Pt−maxs≤t⁡Psmaxs≤t⁡Ps\text{MDD}\_{a}=\min\_{t}\frac{P\_{t}-\max\_{s\leq t}P\_{s}}{\max\_{s\leq t}P\_{s}}
5. 5.

   Avg volume: V¯a=1T​∑tVa​t\bar{V}\_{a}=\frac{1}{T}\sum\_{t}V\_{at}
6. 6.

   Vol-of-vol: σσ,a\sigma\_{\sigma,a} (rolling volatility std)
7. 7.

   Trend: βa\beta\_{a} from Pt=α+β​t+ϵP\_{t}=\alpha+\beta t+\epsilon

This yields statistics matrix 𝐒∈ℝM×7\mathbf{S}\in\mathbb{R}^{M\times 7}.

### 4.5 Procrustes Alignment

#### 4.5.1 Problem Formulation

###### Definition 4.3 (Orthogonal Procrustes Problem).

Given matrices 𝐀,𝐁∈ℝn×p\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times p}, find orthogonal 𝐐∈ℝp×p\mathbf{Q}\in\mathbb{R}^{p\times p} minimizing:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐐⊤​𝐐=𝐈⁡‖𝐀𝐐−𝐁‖F2\min\_{\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}}\|\mathbf{A}\mathbf{Q}-\mathbf{B}\|\_{F}^{2} |  | (9) |

#### 4.5.2 SVD Solution

###### Theorem 4.1 (Schönemann [1966](https://arxiv.org/html/2601.20336v1#bib.bib14 "A generalized solution of the orthogonal Procrustes problem")).

The optimal rotation is 𝐐∗=𝐕𝐔⊤\mathbf{Q}^{\*}=\mathbf{V}\mathbf{U}^{\top} where 𝐔​𝚺​𝐕⊤=SVD​(𝐀⊤​𝐁)\mathbf{U}\bm{\Sigma}\mathbf{V}^{\top}=\text{SVD}(\mathbf{A}^{\top}\mathbf{B}).

###### Proof.

See Appendix [A](https://arxiv.org/html/2601.20336v1#A1 "Appendix A Procrustes Solution Derivation ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
∎

#### 4.5.3 Dimension Handling

When comparing matrices of different column dimensions, we zero-pad the smaller matrix to match dimensions before alignment. For example, comparing the 10-dimensional claims matrix to the 2-dimensional factor matrix requires padding the factor matrix with 8 zero columns. This approach preserves all information in both matrices but introduces a potential downward bias in ϕ\phi: zero-padded dimensions contribute nothing to the numerator but may affect the Procrustes rotation. We prefer this conservative approach to the alternative of PCA-reducing the claims matrix, which would discard potentially informative narrative dimensions.

### 4.6 Tucker’s Congruence Coefficient

###### Definition 4.4 (Tucker’s ϕ\phi).

The congruence coefficient between vectors 𝐱,𝐲∈ℝn\mathbf{x},\mathbf{y}\in\mathbb{R}^{n} is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(𝐱,𝐲)=∑i=1nxi​yi∑i=1nxi2⋅∑i=1nyi2\phi(\mathbf{x},\mathbf{y})=\frac{\sum\_{i=1}^{n}x\_{i}y\_{i}}{\sqrt{\sum\_{i=1}^{n}x\_{i}^{2}\cdot\sum\_{i=1}^{n}y\_{i}^{2}}} |  | (10) |

This equals cosine similarity without mean-centering, appropriate for factor comparison where sign and magnitude both carry meaning.

#### 4.6.1 Matrix Congruence

For matrices 𝐀,𝐁\mathbf{A},\mathbf{B} after Procrustes alignment, we compute per-column ϕ\phi values and report mean absolute ϕ\phi:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ¯=1p​∑j=1p|ϕ​(𝐚j,𝐛j)|\bar{\phi}=\frac{1}{p}\sum\_{j=1}^{p}|\phi(\mathbf{a}\_{j},\mathbf{b}\_{j})| |  | (11) |

#### 4.6.2 Interpretation Thresholds

Following Lorenzo-Seva and ten Berge ([2006](https://arxiv.org/html/2601.20336v1#bib.bib16 "Tucker’s congruence coefficient as a meaningful index of factor similarity")):555These thresholds were developed for comparing factor solutions derived from similar data (e.g., across samples or rotation methods). Their application to heterogeneous spaces—comparing NLP-derived claims to market-derived factors—extends beyond the original validation context. We apply them as rough benchmarks while acknowledging this limitation.

* •

  |ϕ|≥0.95|\phi|\geq 0.95: Factor equivalence
* •

  |ϕ|≥0.85|\phi|\geq 0.85: Fair similarity
* •

  |ϕ|≥0.65|\phi|\geq 0.65: Moderate similarity
* •

  |ϕ|<0.65|\phi|<0.65: Weak/no similarity

### 4.7 Statistical Inference

#### 4.7.1 Power Considerations

With n=23n=23 common entities, statistical power to detect alignment is limited. Monte Carlo simulation (500 iterations per effect size, 200 permutations each) reveals approximate power at α=0.05\alpha=0.05:

| True ϕ\phi | Power |
| --- | --- |
| 0.30 | 14% |
| 0.50 | 45% |
| 0.65 | 70% |
| 0.70 | 90% |

This analysis indicates our study is adequately powered (>>80%) to detect only strong alignment (ϕ≥0.70\phi\geq 0.70). The “moderate similarity” threshold of ϕ=0.65\phi=0.65 falls near our detection limit. Consequently, our null findings should be interpreted cautiously: we can confidently reject strong alignment but cannot distinguish weak alignment (ϕ≈0.3\phi\approx 0.3) from no alignment. The non-significant p-values for claims-based comparisons are consistent with both no alignment and insufficient power to detect weak effects.

#### 4.7.2 Permutation Test

We assess significance via one-sided permutation test (implemented in Python using scipy.stats and numpy):

1. 1.

   Compute observed ϕ∗\phi^{\*}
2. 2.

   For b=1,…,Bb=1,\ldots,B permutations: permute rows of 𝐁\mathbf{B}, compute ϕ(b)\phi^{(b)}
3. 3.

   pp-value =1B​∑b=1B𝟏​[ϕ(b)≥ϕ∗]=\frac{1}{B}\sum\_{b=1}^{B}\mathbf{1}[\phi^{(b)}\geq\phi^{\*}] (one-sided, testing H0H\_{0}: ϕ≤ϕrandom\phi\leq\phi\_{\text{random}})

#### 4.7.3 Bootstrap Confidence Intervals

We construct 95% CIs via percentile bootstrap (B=1000B=1000 resamples). However, bootstrap resampling with replacement on small samples (n=23n=23) exhibits known pathologies when combined with Procrustes-based alignment: duplicate entities in resampled data artificially inflate ϕ\phi by increasing effective weights on well-aligned pairs. Our bootstrap distributions show substantial upward bias (bootstrap mean exceeds point estimate by 29% for claims–statistics, 37% for claims–factors), with moderate right-skewness (skewness ≈0.45\approx 0.45). Consequently, percentile CIs may be conservative for upper bounds but unreliable for lower bounds. Given this bias, reported confidence intervals should be interpreted as indicative rather than precise. We report these intervals for completeness while acknowledging their limitations.

## 5 Results

### 5.1 Tensor Decomposition

CP decomposition with rank 2 explains 92.45% of tensor variance. Figure [1](https://arxiv.org/html/2601.20336v1#S5.F1 "Figure 1 ‣ 5.1 Tensor Decomposition ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") visualizes a cross-sectional slice of the market tensor.

![Refer to caption](x1.png)


Figure 1: Market tensor slice (asset ×\times feature) at mid-sample timestamp. Values are z-normalized. Structure reveals asset clusters and feature correlations.

Factor loadings reveal BTC as a massive outlier (Factor 1 loading = 28.5, compared to mean ≈0\approx 0). Figure [2](https://arxiv.org/html/2601.20336v1#S5.F2 "Figure 2 ‣ 5.1 Tensor Decomposition ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") shows assets in factor space.

![Refer to caption](x2.png)


Figure 2: Assets in CP factor space (rank 2). BTC, GALA, and SC are statistical outliers (>2​σ>2\sigma). Colors indicate clusters from cross-sectional analysis.

### 5.2 Claims Matrix

Figure [3](https://arxiv.org/html/2601.20336v1#S5.F3 "Figure 3 ‣ 5.2 Claims Matrix ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") displays the claims matrix heatmap. Bitcoin emphasizes Store of Value (28%) and Medium of Exchange (24%), reflecting its foundational monetary focus. Ethereum shows the strongest Smart Contracts concentration (42%), while Solana and NEAR distribute emphasis more evenly across Smart Contracts, Scalability, and Governance claims. Privacy-focused Monero predictably scores highest on Privacy (31%) with notable Medium of Exchange emphasis (18%).

![Refer to caption](x3.png)


Figure 3: Claims matrix: Zero-shot classification scores across selected assets and 10 functional categories. Full corpus includes 24 assets; subset shown for readability.

### 5.3 Primary Alignment Tests

Table [4](https://arxiv.org/html/2601.20336v1#S5.T4 "Table 4 ‣ 5.3 Primary Alignment Tests ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") reports alignment results for three comparisons.

Table 4: Primary Alignment Test Results (n=23n=23)

| Comparison | ϕ\bm{\phi} | 95% CI | p-value | Interpretation |
| --- | --- | --- | --- | --- |
| Claims–Statistics | 0.341 | [0.34, 0.55] | 0.332 | Weak |
| Claims–Factors† | 0.077 | [0.07, 0.16] | 0.747 | Weak |
| Statistics–Factors | 0.197 | [0.16, 0.24] | <<0.001 | Weak\* |

\*Statistically significant but see Section [6](https://arxiv.org/html/2601.20336v1#S6 "6 Discussion ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") on mechanical coupling.
  
†Zero-padded alignment (10D claims vs 2D factors). Non-padded estimates in Appendix [E](https://arxiv.org/html/2601.20336v1#A5 "Appendix E Per-Dimension Alignment Values ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
  
Note: Bootstrap percentile confidence intervals are indicative rather than precise due to documented upward bias with small-sample Procrustes resampling (see Section [4.7.1](https://arxiv.org/html/2601.20336v1#S4.SS7.SSS1 "4.7.1 Power Considerations ‣ 4.7 Statistical Inference ‣ 4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis")).

All three comparisons yield weak alignment (ϕ<0.35\phi<0.35). Notably, the statistics–factors comparison achieves statistical significance (p<0.001p<0.001) despite weak magnitude. Statistical significance indicates the alignment is reliably above chance (non-random coupling), while weak magnitude (ϕ=0.197\phi=0.197, well below the 0.65 threshold) indicates this coupling is substantively negligible for practical inference. Importantly, both statistics and factors derive from the same underlying market data—summary statistics aggregate temporal behavior, while tensor factors capture latent structure—so the statistics–factors alignment serves as a calibration check: significant alignment (p<0.001p<0.001) confirms our Procrustes pipeline successfully detects mathematical relationships when they exist, validating the methodology and establishing that the null result for claims represents a true negative rather than measurement failure. The key finding is that narrative claims show no such systematic relationship: claims-based comparisons yield both weak magnitude and non-significant p-values (p=0.332p=0.332 and p=0.747p=0.747), indicating that whatever market-data coupling exists does not extend to whitepaper content. We note that non-padded per-dimension analysis (Appendix [E](https://arxiv.org/html/2601.20336v1#A5 "Appendix E Per-Dimension Alignment Values ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis")) reveals higher alignment within matched dimensions (ϕ≈0.31\phi\approx 0.31 for claims–factors), though this value still falls below the 0.65 threshold for moderate similarity; the conservative zero-padded estimates reported in Table [4](https://arxiv.org/html/2601.20336v1#S5.T4 "Table 4 ‣ 5.3 Primary Alignment Tests ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") reflect our methodological choice to penalize dimension mismatch rather than present inflated alignment figures.

### 5.4 Rank Sensitivity Analysis

Figure [4](https://arxiv.org/html/2601.20336v1#S5.F4 "Figure 4 ‣ 5.4 Rank Sensitivity Analysis ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") shows how alignment varies with CP rank.

![Refer to caption](x4.png)


Figure 4: Rank sensitivity: Explained variance and alignment ϕ\phi vs CP rank. Variance jumps at rank 2; alignment improves gradually.

Table [5](https://arxiv.org/html/2601.20336v1#S5.T5 "Table 5 ‣ 5.4 Rank Sensitivity Analysis ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") details rank sensitivity results.

Table 5: Rank Sensitivity Analysis (Claims–Factors). Values reflect alignment during rank selection on non-padded matrices; final alignment (Table [4](https://arxiv.org/html/2601.20336v1#S5.T4 "Table 4 ‣ 5.3 Primary Alignment Tests ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis")) applies zero-padding before Procrustes rotation, which dilutes ϕ\phi for dimension-mismatched comparisons.

| Rank | Explained Variance | ϕ\bm{\phi} |
| --- | --- | --- |
| 1 | 79.4% | 0.031 |
| 2 | 92.5% | 0.060 |
| 3 | 92.5% | 0.093 |
| 4 | 98.1% | 0.086 |
| 5 | 98.1% | 0.087 |

Note: Displayed variance values rounded to one decimal place.

Alignment peaks at rank 3 (ϕ=0.093\phi=0.093) then slightly declines, suggesting diminishing returns from additional factors. Even at optimal rank, alignment remains well below the 0.65 threshold for moderate similarity.

### 5.5 Tucker vs CP Comparison

Table [6](https://arxiv.org/html/2601.20336v1#S5.T6 "Table 6 ‣ 5.5 Tucker vs CP Comparison ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") compares decomposition methods.

Table 6: Tucker vs CP Decomposition Comparison

| Method | Ranks | Explained Variance | ϕ\bm{\phi} |
| --- | --- | --- | --- |
| CP | 2 | 92.45% | 0.060 |
| Tucker | [5,2,2] | 92.46% | 0.063 |

Both methods achieve nearly identical variance explained and alignment. Tucker yields marginally higher alignment (ϕ=0.063\phi=0.063 vs 0.0600.060), but both indicate negligible narrative-factor correspondence, confirming robustness to decomposition choice.

### 5.6 Temporal Stability

Figure [5](https://arxiv.org/html/2601.20336v1#S5.F5 "Figure 5 ‣ 5.6 Temporal Stability ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") shows alignment evolution across six rolling windows.

![Refer to caption](x5.png)


Figure 5: Temporal evolution of alignment coefficient across 6-month rolling windows (3-month stride).

Mean ϕ=0.183±0.009\phi=0.183\pm 0.009 (mean ±\pm SD across windows). Alignment remains remarkably stable throughout the sample period, ranging from ϕ=0.168\phi=0.168 (early 2023) to ϕ=0.196\phi=0.196 (mid-2023).

### 5.7 Institutional Corpus Alignment

Figure [6](https://arxiv.org/html/2601.20336v1#S5.F6 "Figure 6 ‣ 5.7 Institutional Corpus Alignment ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") reports alignment using the institutional snapshot corpus (February 2025) across rolling market windows. Mean ϕ=0.203±0.013\phi=0.203\pm 0.013 across six windows using 12 assets with complete market coverage (AAVE, ADA, ARB, AVAX, BTC, ETH, FIL, LINK, MKR, OP, SOL, UNI), closely tracking the whitepaper-based temporal alignment. This suggests that broader institutional narratives—official documentation, governance posts, foundation updates—do not materially improve alignment under a single-period snapshot. The limitation is that true narrative drift is not yet observed; a multi-period corpus would be required to test whether narrative repositioning precedes changes in market factor structure.

![Refer to caption](x6.png)


Figure 6: Institutional corpus alignment (February 2025 snapshot) across rolling market windows. Limited alignment persists (ϕ=0.203±0.013\phi=0.203\pm 0.013), consistent with whitepaper-based results.

### 5.8 Entity-Level Analysis

Figure [7](https://arxiv.org/html/2601.20336v1#S5.F7 "Figure 7 ‣ 5.8 Entity-Level Analysis ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") shows leave-one-out entity impact.

![Refer to caption](x7.png)


Figure 7: Entity impact on alignment (n=23n=23). Infrastructure tokens (NEAR, MKR, ATOM) modestly help alignment; DeFi tokens (ENS, UNI, AAVE) and major assets (BTC, ETH) hurt alignment.

Table [7](https://arxiv.org/html/2601.20336v1#S5.T7 "Table 7 ‣ 5.8 Entity-Level Analysis ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") provides entity rankings for the top and bottom contributors.

Table 7: Entity Impact Analysis (Top/Bottom)

| Asset | Impact | Interpretation |
| --- | --- | --- |
| NEAR | +0.009+0.009 | Helps alignment |
| MKR | +0.008+0.008 | Helps alignment |
| ATOM | +0.007+0.007 | Helps alignment |
| GRT | +0.003+0.003 | Helps alignment |
| XMR | −0.009-0.009 | Hurts alignment |
| BTC | −0.010-0.010 | Hurts alignment |
| SC | −0.012-0.012 | Hurts alignment |
| ETH | −0.013-0.013 | Hurts alignment |
| AAVE | −0.014-0.014 | Hurts alignment |
| UNI | −0.017-0.017 | Hurts alignment |
| ENS | −0.035-0.035 | Hurts alignment |

Notably, Bitcoin now hurts alignment (−0.010-0.010), reversing prior expectations. ENS shows the largest negative impact (−0.035-0.035), followed by UNI (−0.017-0.017). Infrastructure-focused tokens (NEAR, MKR, ATOM) show modest positive contributions (+0.007 to +0.009), suggesting their technical whitepapers exhibit marginally higher alignment contributions than major DeFi and store-of-value assets, though these impacts remain at noise level.

### 5.9 Feature Importance

Figure [7](https://arxiv.org/html/2601.20336v1#footnote7 "footnote 7 ‣ Figure 8 ‣ 5.9 Feature Importance ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") shows ablation-based feature importance.

![Refer to caption](x8.png)


Figure 8: Feature importance via ablation. Scalability and Governance claims contribute most to alignment; Security claims show largest negative impact.777Ablation analysis uses an 8-category preliminary taxonomy for computational tractability; results are qualitatively consistent with the 10-category classification.

Table [8](https://arxiv.org/html/2601.20336v1#S5.T8 "Table 8 ‣ 5.9 Feature Importance ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") details importance values.

Table 8: Feature Importance (Ablation)

| Category | Impact on ϕ\phi |
| --- | --- |
| Scalability | +0.014+0.014 |
| Governance | +0.010+0.010 |
| Privacy | +0.007+0.007 |
| Consensus | +0.006+0.006 |
| Interoperability | +0.003+0.003 |
| Tokenomics | 0.0000.000 |
| Technology | 0.0000.000 |
| Security | −0.022-0.022 |

Scalability and Governance claims contribute most to alignment, while Security claims—despite their prominence in whitepapers—hurt alignment (−0.022-0.022). This counterintuitive finding admits multiple interpretations: security claims may be ubiquitous across projects (most whitepapers emphasize cryptographic security) providing little discriminative signal, actual security-related market events (hacks, exploits) may create idiosyncratic volatility orthogonal to stated claims, or—as a methodological caveat—BART-MNLI may conflate security-specific terminology with general technical descriptions, introducing classification noise.

### 5.10 Robustness Checks

#### 5.10.1 Subsample Stability

Bootstrap resampling (100 iterations, 80% subsample) yields mean ϕ=0.317±0.029\phi=0.317\pm 0.029 with 95% CI [0.270,0.389][0.270,0.389]. The subsample mean is slightly below the full-sample result (ϕ=0.341\phi=0.341), indicating stable estimates robust to entity perturbation. Both values remain firmly in the “weak” range, with the upper confidence bound well below the 0.65 threshold for moderate similarity.

#### 5.10.2 Bitcoin-Excluded Sensitivity

Bitcoin’s exceptional position in the factor space (Factor 1 loading = 28.5, compared to mean ≈0\approx 0, representing >5​σ>5\sigma deviation) raises the question of whether our null result is driven by this single outlier. To address this concern, we re-estimate alignment excluding Bitcoin from the entity set (n=22n=22).

Table [9](https://arxiv.org/html/2601.20336v1#S5.T9 "Table 9 ‣ 5.10.2 Bitcoin-Excluded Sensitivity ‣ 5.10 Robustness Checks ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") compares full-sample and Bitcoin-excluded results.

Table 9: Robustness: Bitcoin-Excluded Alignment

| Comparison | Full (n=23n=23) | No BTC (n=22n=22) | Change |
| --- | --- | --- | --- |
| Claims–Factors | ϕ=0.077\phi=0.077 | ϕ=0.081\phi=0.081 | +4.6%+4.6\% |
| Statistics–Factors | ϕ=0.197\phi=0.197 | ϕ=0.173\phi=0.173 | −12.3%-12.3\% |
| Claims–Statistics | ϕ=0.341\phi=0.341 | ϕ=0.355\phi=0.355 | +4.1%+4.1\% |

Excluding Bitcoin yields ϕ=0.081\phi=0.081 for claims–factors alignment (vs ϕ=0.077\phi=0.077 with the full sample, p=0.724p=0.724). The modest increase suggests Bitcoin marginally hurts alignment, consistent with our entity-level analysis. The statistics–factors alignment weakens modestly (ϕ=0.173\phi=0.173 vs 0.1970.197) but remains significant (p=0.008p=0.008), suggesting Bitcoin contributes to but does not solely determine the latent factor structure. Importantly, all claims-based results remain firmly in the “weak” range—well below the 0.65 threshold—confirming that our null finding is not an artifact of Bitcoin’s dominant market position but rather reflects observed weak alignment between whitepaper narratives and market factor structure across the cryptocurrency ecosystem.

## 6 Discussion

### 6.1 Interpreting the Null Result

Our central finding is negative: whitepaper claims do not meaningfully predict market factor structure. This null result admits several interpretations.

First, whitepapers may represent aspirational narratives rather than realized functionality. Projects articulate visions at inception that evolve, pivot, or fail to materialize. Bitcoin’s “peer-to-peer electronic cash” framing diverged significantly from its “digital gold” market reality.

Second, market behavior may be driven by factors orthogonal to functional claims. Speculation, liquidity provision, correlation with Bitcoin, and macroeconomic factors dominate cryptocurrency price dynamics (Liu and Tsyvinski, [2021](https://arxiv.org/html/2601.20336v1#bib.bib18 "Risks and returns of cryptocurrency")), potentially swamping any signal from project-specific narratives.

Third, our NLP pipeline may fail to capture narrative nuance. Zero-shot classification, while scalable, may miss domain-specific semantics that differentiate projects.

### 6.2 Bitcoin’s Reversal

Bitcoin now hurts alignment (−0.010-0.010), which we interpret as reflecting a fundamental regime difference rather than statistical anomaly. Bitcoin has transcended its whitepaper claims (“peer-to-peer electronic cash”) to become a macro asset trading on “digital gold” narratives orthogonal to functional utility claims. Our alignment framework captures functional asset dynamics—the correspondence between what projects claim to do and how their tokens behave—but Bitcoin increasingly operates in a different narrative regime entirely, one dominated by macroeconomic positioning, institutional adoption narratives, and store-of-value framing that bear no relationship to its original functional claims. The expanded corpus (23 entities vs 12 previously) now includes more specialized assets (NEAR, MKR, ATOM) whose technical whitepapers predict their niche market behaviors, making Bitcoin’s regime divergence more apparent.

### 6.3 DeFi Divergence

Application-layer tokens (ENS, UNI, AAVE) show the largest narrative-market gaps (−0.014-0.014 to −0.035-0.035). ENS’s extreme divergence (−0.035-0.035) reflects the disconnect between naming service utility and market dynamics. This pattern suggests a structural distinction: infrastructure tokens (NEAR, ATOM) may be priced on technical specifications—sharding, throughput, interoperability—the very dimensions whitepapers emphasize, while application tokens (UNI, ENS, AAVE) may be priced on usage metrics (TVL, fee revenue, governance participation) that whitepapers cannot anticipate. We note that the magnitude of these entity-level impacts (0.007–0.035) remains modest relative to overall alignment levels, so this interpretation should be treated as exploratory rather than definitive.

### 6.4 Feature Importance Patterns

Scalability and Governance claims contribute most to alignment (+0.014+0.014 and +0.010+0.010 respectively), while Security claims show the largest negative impact (−0.022-0.022). This counterintuitive finding admits multiple interpretations: security claims may be ubiquitous across projects (most whitepapers emphasize cryptographic security) providing little discriminative signal, actual security-related market events (hacks, exploits) may create idiosyncratic volatility orthogonal to stated claims, or the BART-MNLI classifier may conflate security-specific terminology with general technical descriptions. Projects emphasizing scalability and governance differentiation show better narrative-market correspondence, perhaps because these claims map more directly to observable protocol characteristics (throughput metrics, voting mechanisms) that markets can assess.

### 6.5 Theoretical Implications

Our findings contribute to the growing literature on narrative economics (Shiller, [2017](https://arxiv.org/html/2601.20336v1#bib.bib4 "Narrative economics")) by providing quantitative evidence on the limits of narrative-market coupling in cryptocurrency markets. Three theoretical implications emerge:

Narrative Dissociation Hypothesis. The weak alignment we document is consistent with what we term “narrative dissociation”—an observed weak correspondence between stated project intentions and realized market behavior. We emphasize that our limited sample size (n=23n=23) provides insufficient power to definitively distinguish weak alignment from no alignment; we can confidently reject strong alignment (ϕ≥0.70\phi\geq 0.70), but this framing represents a working hypothesis rather than a demonstrated finding. If genuine, narrative dissociation would contrast with efficient market theory, which predicts that informative narratives are rapidly incorporated into prices. The evolving dependency structures in cryptocurrency markets (Briola and Aste, [2022](https://arxiv.org/html/2601.20336v1#bib.bib27 "Dependency structures in cryptocurrency market from high to low frequency")) and the documented role of social media in price dynamics (Burnie et al., [2020](https://arxiv.org/html/2601.20336v1#bib.bib28 "Analysing social media forums to discover potential causes of phasic shifts in cryptocurrency price series")) suggest narrative-market relationships may be more complex than our static alignment tests capture. Our findings suggest that either narratives contain little price-relevant information, or markets systematically ignore such information—though we cannot adjudicate between these explanations with present data.

Factor Structure Independence. The orthogonality of narrative space to market factor space implies that the latent factors driving cryptocurrency returns are fundamentally different from the functional dimensions projects emphasize. Market factors appear to capture systemic exposures (Bitcoin correlation, liquidity risk, macro sensitivity) rather than project-specific functionality. This has implications for portfolio construction: diversification along narrative dimensions may not reduce factor exposure.

Bounded Rationality in Crypto Markets. The persistence of elaborate whitepaper narratives despite their apparent irrelevance to market outcomes suggests bounded rationality among market participants. Investors may allocate attention to narratives as heuristics, even when such narratives lack predictive power. This parallels findings in behavioral finance on the role of stories in investment decisions (Barberis and Thaler, [2003](https://arxiv.org/html/2601.20336v1#bib.bib3 "A survey of behavioral finance")).

### 6.6 Practical Implications

For practitioners, our findings suggest several actionable insights:

For Investors. Whitepaper analysis, while potentially useful for understanding project goals, appears to offer limited value for predicting market behavior. Investment strategies based on narrative classification (e.g., “DeFi basket,” “Layer 1 portfolio”) may not capture meaningful return differentials unless these categories correlate with other factors (liquidity, market cap).

For Project Teams. The attenuated narrative-market coupling suggests that market success depends on factors beyond whitepaper messaging. Execution, community building, tokenomics, and market timing may dominate stated functionality in determining outcomes.

For Regulators. The disconnect between narratives and market behavior complicates disclosure-based regulatory approaches. Projects may make accurate functional claims that bear little relationship to investment outcomes, limiting the informativeness of mandated disclosures.

### 6.7 Limitations

Several limitations warrant acknowledgment:

* •

  Small sample size (n=23n=23) is a critical constraint. With only 23 common entities, statistical power is limited to detecting strong alignment (ϕ≥0.70\phi\geq 0.70); we cannot reliably distinguish weak alignment from no alignment. While our expanded corpus (24 whitepapers, 23 common entities) substantially improves over prior work, expanding to 50+ projects would enable both adequate power for moderate effects and subsample analysis by sector.
* •

  Whitepapers represent static documents that may not reflect current project status. Dynamic narrative analysis (social media, forum posts, governance proposals) may capture narrative evolution.
* •

  Our functional taxonomy, while motivated by literature, remains somewhat arbitrary. Alternative taxonomies may reveal alignment in different dimensions.
* •

  Two years of data may be insufficient to capture long-term alignment dynamics.
* •

  Zero-shot classifiers trained on general-domain NLI corpora exhibit domain shift when applied to specialized cryptocurrency discourse (Gururangan et al., [2020](https://arxiv.org/html/2601.20336v1#bib.bib22 "Don’t stop pretraining: adapt language models to domains and tasks")). While BART-MNLI captures broad semantic categories, crypto-specific terminology (“sharding,” “AMM,” “tokenomics”) may not receive accurate treatment. Beyond acknowledging this limitation, we interpret it as a substantive methodological finding: the “Semantic Gap” between general-purpose NLP and crypto-native discourse represents a measurement challenge that future researchers must address. Our security ablation result—where security claims hurt alignment (−0.022-0.022) despite security being technically salient—provides empirical evidence of this gap, likely reflecting BART-MNLI conflating cryptographic security (“zero-knowledge proofs,” “trusted execution environments”) with general safety concepts. This finding carries practical implications: off-the-shelf LLMs should not be deployed for cryptocurrency auditing or regulatory classification without domain adaptation via continued pretraining on cryptocurrency corpora.
* •

  Single exchange (Binance) data may not represent broader market dynamics.

## 7 Conclusions

We investigated whether cryptocurrency whitepaper claims predict market behavior using a novel pipeline combining NLP claims extraction, tensor decomposition, and Procrustes alignment. Our analysis yields nuanced results: while narrative-market alignment remains weak (ϕ<0.35\phi<0.35), the statistics–factors comparison achieves statistical significance (p<0.001p<0.001), suggesting market metrics systematically relate to tensor-derived factors even as narrative claims remain decoupled.

### 7.1 Summary of Findings

Our investigation across 24 whitepapers and 23 common entities produced the following key findings:

1. 1.

   Weak Narrative Alignment. Tucker’s congruence coefficient between claims and market statistics (ϕ=0.341\phi=0.341, p=0.332p=0.332), and claims and tensor factors (ϕ=0.077\phi=0.077, p=0.747p=0.747), both fall well below the 0.65 threshold for moderate similarity and fail to achieve statistical significance.
2. 2.

   Significant Statistics–Factors Link. The statistics–factors comparison (ϕ=0.197\phi=0.197, p<0.001p<0.001) achieves statistical significance despite modest magnitude, indicating market summary statistics systematically relate to latent factor structure.
3. 3.

   Infrastructure Token Alignment. NEAR, MKR, and ATOM show modest positive alignment contributions (+0.007 to +0.009), while major assets (BTC, ETH) and DeFi tokens (ENS, UNI, AAVE) hurt alignment.
4. 4.

   Bitcoin Robustness. Excluding Bitcoin (n=22n=22) yields ϕ=0.081\phi=0.081 for claims–factors, confirming the null result is not driven by Bitcoin’s dominant market position.
5. 5.

   NLP Validation. Inter-model agreement (BART vs DeBERTa) reaches 67% at relaxed (top-3) threshold, with bootstrap CIs indicating stable category estimates despite 32% exact agreement (κ=0.14\kappa=0.14).
6. 6.

   Institutional Corpus. Using a February 2025 institutional corpus (official documentation, foundation updates, governance posts, project blogs; 12 assets with complete market data), alignment remains weak (ϕ=0.203±0.013\phi=0.203\pm 0.013), indicating that broader narratives beyond whitepapers do not materially improve alignment.

### 7.2 Contributions

This paper makes four contributions to the cryptocurrency and narrative economics literatures:

Methodological. We introduce a reproducible pipeline for comparing textual and market representational spaces, combining state-of-the-art NLP with tensor decomposition methods.

Technical. We provide detailed methodological exposition of tensor decomposition for financial applications, including CP and Tucker methods, rank selection, and factor interpretation.

Empirical. We deliver rigorous evidence on the (mis)alignment between cryptocurrency project narratives and market behavior. Our comprehensive robustness checks strengthen the validity of our null result.

Conceptual. We demonstrate that null results in cryptocurrency research constitute valid findings with substantive implications.

### 7.3 Future Work

Several extensions could strengthen and extend this work:

* •

  Dynamic Narratives. Analyze social media content to capture narrative evolution.
* •

  Expanded Corpus. Extend whitepaper analysis to 50+ projects.
* •

  Alternative NLP. Fine-tune transformer models on cryptocurrency text.
* •

  Event Studies. Examine market reactions to whitepaper updates and narrative pivots.
* •

  Cross-Chain Analysis. Compare alignment across blockchain ecosystems.
* •

  Longer Horizons. Extend analysis to 5+ years as data becomes available.

### 7.4 Final Remarks

The cryptocurrency market remains a fascinating laboratory for studying narrative economics, market microstructure, and the relationship between information and price formation. Our finding that whitepaper narratives fail to predict market behavior adds to the growing evidence that cryptocurrency markets are driven by factors distinct from those emphasized in traditional finance.

Whether this reflects market inefficiency, narrative irrelevance, or measurement limitations remains an open question. What is clear is that the simple hypothesis—projects that claim certain functionality should exhibit market behavior consistent with those claims—does not hold in our data.

## References

* L. Ante (2023)
  How Elon Musk’s Twitter activity moves cryptocurrency markets.
  Technological Forecasting and Social Change 186,  pp. 122112.
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p1.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* T. Aste (2019)
  Cryptocurrency market structure: connecting emotions and economics.
  Digital Finance 1,  pp. 5–21.
  Cited by: [§1](https://arxiv.org/html/2601.20336v1#S1.p2.1 "1 Introduction ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* N. Barberis and R. Thaler (2003)
  A survey of behavioral finance.
  Handbook of the Economics of Finance 1,  pp. 1053–1128.
  Cited by: [§6.5](https://arxiv.org/html/2601.20336v1#S6.SS5.p4.1 "6.5 Theoretical Implications ‣ 6 Discussion ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* S. Bartolucci, G. Destefanis, M. Ortu, N. Uras, M. Marchesi, and R. Tonelli (2020)
  The butterfly “affect”: impact of development practices on cryptocurrency prices.
  EPJ Data Science 9 (1),  pp. 21.
  External Links: [Document](https://dx.doi.org/10.1140/epjds/s13688-020-00239-6)
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p4.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* A. Briola and T. Aste (2022)
  Dependency structures in cryptocurrency market from high to low frequency.
  Entropy 24 (11),  pp. 1548.
  Cited by: [§6.5](https://arxiv.org/html/2601.20336v1#S6.SS5.p2.2 "6.5 Theoretical Implications ‣ 6 Discussion ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* A. Briola, D. Vidal-Tomás, Y. Wang, and T. Aste (2022)
  Anatomy of a stablecoin’s failure: the Terra-Luna case.
  Finance Research Letters 51,  pp. 103358.
  External Links: [Document](https://dx.doi.org/10.1016/j.frl.2022.103358)
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p2.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* A. Burnie, E. Yilmaz, and T. Aste (2020)
  Analysing social media forums to discover potential causes of phasic shifts in cryptocurrency price series.
  Frontiers in Blockchain 3,  pp. 610231.
  External Links: [Document](https://dx.doi.org/10.3389/fbloc.2020.610231)
  Cited by: [§6.5](https://arxiv.org/html/2601.20336v1#S6.SS5.p2.2 "6.5 Theoretical Implications ‣ 6 Discussion ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* F. Caccioli, P. Barucca, and T. Kobayashi (2018)
  Network models of financial systemic risk: a review.
  Journal of Computational Social Science 1 (1),  pp. 81–114.
  External Links: [Document](https://dx.doi.org/10.1007/s42001-017-0008-3)
  Cited by: [§2.2](https://arxiv.org/html/2601.20336v1#S2.SS2.p1.1 "2.2 Factor Models in Cryptocurrency ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* R. Chen, D. Yang, and C. Zhang (2022)
  Factor models for high-dimensional tensor time series.
  Journal of the American Statistical Association 117 (537),  pp. 94–116.
  External Links: [Document](https://dx.doi.org/10.1080/01621459.2021.1912757)
  Cited by: [§2.3](https://arxiv.org/html/2601.20336v1#S2.SS3.p1.1 "2.3 Tensor Methods in Finance ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis"),
  [footnote 1](https://arxiv.org/html/2601.20336v1#footnote1 "In 4.2.3 Rank Selection ‣ 4.2 Tensor Decomposition ‣ 4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* Z. Chen, C. Li, and W. Sun (2019)
  Bitcoin price prediction using machine learning: an approach to sample dimension engineering.
  Journal of Computational and Applied Mathematics 365,  pp. 112395.
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p1.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* E. F. Fama and K. R. French (1993)
  Common risk factors in the returns on stocks and bonds.
  Journal of Financial Economics 33 (1),  pp. 3–56.
  Cited by: [§2.2](https://arxiv.org/html/2601.20336v1#S2.SS2.p1.1 "2.2 Factor Models in Cryptocurrency ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* E. F. Fama (1970)
  Efficient capital markets: a review of theory and empirical work.
  The Journal of Finance 25 (2),  pp. 383–417.
  Cited by: [§1](https://arxiv.org/html/2601.20336v1#S1.p2.1 "1 Introduction ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* J. Fan, Y. Liao, and M. Mincheva (2013)
  Large covariance estimation by thresholding principal orthogonal complements.
  Journal of the Royal Statistical Society Series B: Statistical Methodology 75 (4),  pp. 603–680.
  External Links: [Document](https://dx.doi.org/10.1111/rssb.12016)
  Cited by: [§2.3](https://arxiv.org/html/2601.20336v1#S2.SS3.p1.1 "2.3 Tensor Methods in Finance ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* M. Farzulla (2025)
  Market reaction asymmetry: infrastructure disruption dominance over regulatory uncertainty in cryptocurrency volatility.
  SSRN Electronic Journal.
  External Links: [Document](https://dx.doi.org/10.2139/ssrn.5788082)
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p5.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* C. Fisch (2019)
  Initial coin offerings (ICOs) to finance new ventures.
  Journal of Business Venturing 34 (1),  pp. 1–22.
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p2.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* D. Florysiak and A. Schandlbauer (2022)
  Experts or charlatans? ICO analysts and white paper informativeness.
  Journal of Banking & Finance 139,  pp. 106476.
  External Links: [Document](https://dx.doi.org/10.1016/j.jbankfin.2022.106476)
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p2.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* S. Gururangan, A. Marasović, S. Swayamdipta, K. Lo, I. Beltagy, D. Downey, and N. A. Smith (2020)
  Don’t stop pretraining: adapt language models to domains and tasks.
  In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics,
   pp. 8342–8360.
  External Links: [Document](https://dx.doi.org/10.18653/v1/2020.acl-main.740)
  Cited by: [5th item](https://arxiv.org/html/2601.20336v1#S6.I1.i5.p1.1 "In 6.7 Limitations ‣ 6 Discussion ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* R. A. Harshman (1970)
  Foundations of the PARAFAC procedure: models and conditions for an “explanatory” multimodal factor analysis.
  UCLA Working Papers in Phonetics 16,  pp. 1–84.
  Cited by: [§2.3](https://arxiv.org/html/2601.20336v1#S2.SS3.p2.2 "2.3 Tensor Methods in Finance ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* O. Haykir and İ. Yağlı (2022)
  Speculative bubbles and herding in cryptocurrencies.
  Financial Innovation 8 (1),  pp. 1–33.
  External Links: [Document](https://dx.doi.org/10.1186/s40854-022-00383-0)
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p1.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* P. He, X. Liu, J. Gao, and W. Chen (2021)
  DeBERTa: decoding-enhanced BERT with disentangled attention.
  In International Conference on Learning Representations,
  Cited by: [§4.3.3](https://arxiv.org/html/2601.20336v1#S4.SS3.SSS3.p1.1 "4.3.3 Model Validation ‣ 4.3 NLP Claims Extraction ‣ 4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* S. T. Howell, M. Niessner, and D. Yermack (2020)
  Initial coin offerings: financing growth with cryptocurrency token sales.
  The Review of Financial Studies 33 (9),  pp. 3925–3974.
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p2.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* Z. Keskin and T. Aste (2020)
  Information-theoretic measures for nonlinear causality detection: application to social media sentiment and cryptocurrency prices.
  Royal Society Open Science 7 (9),  pp. 200863.
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p3.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* K. Kirtac and G. Germano (2025)
  Large language models in finance: what is financial sentiment?.
  arXiv preprint.
  Cited by: [§4.3.3](https://arxiv.org/html/2601.20336v1#S4.SS3.SSS3.p1.1 "4.3.3 Model Validation ‣ 4.3 NLP Claims Extraction ‣ 4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* T. G. Kolda and B. W. Bader (2009)
  Tensor decompositions and applications.
  SIAM Review 51 (3),  pp. 455–500.
  Cited by: [§2.3](https://arxiv.org/html/2601.20336v1#S2.SS3.p1.1 "2.3 Tensor Methods in Finance ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* M. Lewis, Y. Liu, N. Goyal, M. Ghazvininejad, A. Mohamed, O. Levy, V. Stoyanov, and L. Zettlemoyer (2020)
  BART: denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension.
  arXiv preprint arXiv:1910.13461.
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p4.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis"),
  [§4.3.1](https://arxiv.org/html/2601.20336v1#S4.SS3.SSS1.p1.1 "4.3.1 Zero-Shot Classification ‣ 4.3 NLP Claims Extraction ‣ 4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* Y. Liu and A. Tsyvinski (2021)
  Risks and returns of cryptocurrency.
  The Review of Financial Studies 34 (6),  pp. 2689–2727.
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p1.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis"),
  [§2.2](https://arxiv.org/html/2601.20336v1#S2.SS2.p2.1 "2.2 Factor Models in Cryptocurrency ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis"),
  [§6.1](https://arxiv.org/html/2601.20336v1#S6.SS1.p3.1 "6.1 Interpreting the Null Result ‣ 6 Discussion ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* G. Livan, S. Alfarano, and E. Scalas (2011)
  Fine structure of spectral properties for random correlation matrices: an application to financial markets.
  Physical Review E 84 (1),  pp. 016113.
  Cited by: [§2.2](https://arxiv.org/html/2601.20336v1#S2.SS2.p1.1 "2.2 Factor Models in Cryptocurrency ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* U. Lorenzo-Seva and J. M. ten Berge (2006)
  Tucker’s congruence coefficient as a meaningful index of factor similarity.
  Methodology 2 (2),  pp. 57–64.
  Cited by: [§2.4](https://arxiv.org/html/2601.20336v1#S2.SS4.p1.1 "2.4 Factor Comparison Methods ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis"),
  [§2.4](https://arxiv.org/html/2601.20336v1#S2.SS4.p2.4 "2.4 Factor Comparison Methods ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis"),
  [§4.6.2](https://arxiv.org/html/2601.20336v1#S4.SS6.SSS2.p1.1 "4.6.2 Interpretation Thresholds ‣ 4.6 Tucker’s Congruence Coefficient ‣ 4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* G. Pappalardo, T. Di Matteo, G. Caldarelli, and T. Aste (2018)
  Blockchain inefficiency in the Bitcoin peers network.
  EPJ Data Science 7 (1),  pp. 1–14.
  External Links: [Document](https://dx.doi.org/10.1140/epjds/s13688-018-0159-3)
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p5.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* P. H. Schönemann (1966)
  A generalized solution of the orthogonal Procrustes problem.
  Psychometrika 31 (1),  pp. 1–10.
  Cited by: [§2.4](https://arxiv.org/html/2601.20336v1#S2.SS4.p1.1 "2.4 Factor Comparison Methods ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis"),
  [Theorem 4.1](https://arxiv.org/html/2601.20336v1#S4.Thmtheorem1 "Theorem 4.1 (Schönemann 1966). ‣ 4.5.2 SVD Solution ‣ 4.5 Procrustes Alignment ‣ 4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* R. J. Shiller (2017)
  Narrative economics.
  American Economic Review 107 (4),  pp. 967–1004.
  Cited by: [§1](https://arxiv.org/html/2601.20336v1#S1.p2.1 "1 Introduction ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis"),
  [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p3.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis"),
  [§6.5](https://arxiv.org/html/2601.20336v1#S6.SS5.p1.1 "6.5 Theoretical Implications ‣ 6 Discussion ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* M. Suriano, L. F. Caram, C. Caiafa, H. D. Merlino, and O. A. Rosso (2025)
  Information theory quantifiers in cryptocurrency time series analysis.
  Entropy 27 (4),  pp. 450.
  External Links: [Document](https://dx.doi.org/10.3390/e27040450)
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p2.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* L. R. Tucker (1951)
  A method for synthesis of factor analysis studies.
  Personnel Research Section Report (984).
  Cited by: [§2.4](https://arxiv.org/html/2601.20336v1#S2.SS4.p1.1 "2.4 Factor Comparison Methods ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* D. Vidal-Tomás, A. Briola, and T. Aste (2023)
  FTX’s downfall and Binance’s consolidation: the fragility of centralized digital finance.
  Physica A: Statistical Mechanics and its Applications 625,  pp. 129044.
  External Links: [Document](https://dx.doi.org/10.1016/j.physa.2023.129044)
  Cited by: [§2.1](https://arxiv.org/html/2601.20336v1#S2.SS1.p2.1 "2.1 Cryptocurrency Narratives and Sentiment ‣ 2 Related Work ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* A. Williams, N. Nangia, and S. Bowman (2018)
  A broad-coverage challenge corpus for sentence understanding through inference.
  In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers),
   pp. 1112–1122.
  External Links: [Document](https://dx.doi.org/10.18653/v1/N18-1101)
  Cited by: [footnote 2](https://arxiv.org/html/2601.20336v1#footnote2 "In 4.3.1 Zero-Shot Classification ‣ 4.3 NLP Claims Extraction ‣ 4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").
* W. Yin, J. Hay, and D. Roth (2019)
  Benchmarking zero-shot text classification: datasets, evaluation and entailment approach.
  In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP),
   pp. 3914–3923.
  External Links: [Document](https://dx.doi.org/10.18653/v1/D19-1404)
  Cited by: [§4.3.1](https://arxiv.org/html/2601.20336v1#S4.SS3.SSS1.p1.1 "4.3.1 Zero-Shot Classification ‣ 4.3 NLP Claims Extraction ‣ 4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis").

## Appendix A Procrustes Solution Derivation

###### Theorem A.1.

The orthogonal Procrustes problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐐⊤​𝐐=𝐈⁡‖𝐀𝐐−𝐁‖F2\min\_{\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}}\|\mathbf{A}\mathbf{Q}-\mathbf{B}\|\_{F}^{2} |  | (12) |

has solution 𝐐∗=𝐕𝐔⊤\mathbf{Q}^{\*}=\mathbf{V}\mathbf{U}^{\top} where 𝐔​𝚺​𝐕⊤=SVD​(𝐀⊤​𝐁)\mathbf{U}\bm{\Sigma}\mathbf{V}^{\top}=\text{SVD}(\mathbf{A}^{\top}\mathbf{B}).

###### Proof.

Expanding the objective:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖𝐀𝐐−𝐁‖F2\displaystyle\|\mathbf{A}\mathbf{Q}-\mathbf{B}\|\_{F}^{2} | =tr​[(𝐀𝐐−𝐁)⊤​(𝐀𝐐−𝐁)]\displaystyle=\text{tr}[(\mathbf{A}\mathbf{Q}-\mathbf{B})^{\top}(\mathbf{A}\mathbf{Q}-\mathbf{B})] |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =tr​[𝐐⊤​𝐀⊤​𝐀𝐐]−2​tr​[𝐐⊤​𝐀⊤​𝐁]+tr​[𝐁⊤​𝐁]\displaystyle=\text{tr}[\mathbf{Q}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{Q}]-2\text{tr}[\mathbf{Q}^{\top}\mathbf{A}^{\top}\mathbf{B}]+\text{tr}[\mathbf{B}^{\top}\mathbf{B}] |  | (14) |

Since 𝐐\mathbf{Q} is orthogonal, tr​[𝐐⊤​𝐀⊤​𝐀𝐐]=tr​[𝐀⊤​𝐀]\text{tr}[\mathbf{Q}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{Q}]=\text{tr}[\mathbf{A}^{\top}\mathbf{A}] is constant. Thus we maximize:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝐐⊤​𝐐=𝐈⁡tr​[𝐐⊤​𝐀⊤​𝐁]\max\_{\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}}\text{tr}[\mathbf{Q}^{\top}\mathbf{A}^{\top}\mathbf{B}] |  | (15) |

Let 𝐀⊤​𝐁=𝐔​𝚺​𝐕⊤\mathbf{A}^{\top}\mathbf{B}=\mathbf{U}\bm{\Sigma}\mathbf{V}^{\top}. Then:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | tr​[𝐐⊤​𝐔​𝚺​𝐕⊤]\displaystyle\text{tr}[\mathbf{Q}^{\top}\mathbf{U}\bm{\Sigma}\mathbf{V}^{\top}] | =tr​[𝐕⊤​𝐐⊤​𝐔​𝚺]=tr​[𝐙​𝚺]\displaystyle=\text{tr}[\mathbf{V}^{\top}\mathbf{Q}^{\top}\mathbf{U}\bm{\Sigma}]=\text{tr}[\mathbf{Z}\bm{\Sigma}] |  | (16) |

where 𝐙=𝐕⊤​𝐐⊤​𝐔\mathbf{Z}=\mathbf{V}^{\top}\mathbf{Q}^{\top}\mathbf{U} is orthogonal.

By von Neumann’s trace inequality, tr​[𝐙​𝚺]≤∑iσi\text{tr}[\mathbf{Z}\bm{\Sigma}]\leq\sum\_{i}\sigma\_{i} with equality when 𝐙=𝐈\mathbf{Z}=\mathbf{I}. Thus 𝐐∗=𝐕𝐔⊤\mathbf{Q}^{\*}=\mathbf{V}\mathbf{U}^{\top}.
∎

## Appendix B Tucker’s Congruence Properties

###### Proposition B.1.

Tucker’s ϕ\phi has the following properties:

1. 1.

   Bounded: −1≤ϕ≤1-1\leq\phi\leq 1
2. 2.

   Scale invariant: ϕ​(c​𝐱,𝐲)=sign​(c)⋅ϕ​(𝐱,𝐲)\phi(c\mathbf{x},\mathbf{y})=\text{sign}(c)\cdot\phi(\mathbf{x},\mathbf{y})
3. 3.

   Not mean-centered (unlike Pearson correlation)
4. 4.

   ϕ=1\phi=1 iff 𝐱=c​𝐲\mathbf{x}=c\mathbf{y} for c>0c>0

## Appendix C Full Asset List

The complete list of 49 cryptocurrency assets includes: BTC, ETH, SOL, XMR, ADA, AVAX, DOT, LINK, ATOM, ALGO, FIL, ICP, AAVE, UNI, MKR, COMP, CRV, SNX, YFI, SUSHI, ENS, GRT, LDO, OP, ARB, APT, AXS, BAND, EGLD, ENJ, FTM, GALA, HBAR, IMX, LIT, LPT, MANA, NEAR, OCEAN, POL, RENDER, RPL, SAND, SC, STORJ, SUI, TRB, API3, ZEC.

## Appendix D Whitepaper Corpus Details

Documents were obtained from official project sources, academic repositories (arXiv), and GitHub. Sources include original whitepapers (BTC, ETH, SOL, AVAX), academic papers (ADA, NEAR, GRT from arXiv), protocol specifications (ZEC, LINK), DeFi protocol documentation (AAVE, COMP, MKR, UNI), storage whitepapers (FIL, STORJ, SC, AR), and technical documentation (ICP, ARB, XMR).

## Appendix E Per-Dimension Alignment Values

Table [10](https://arxiv.org/html/2601.20336v1#A5.T10 "Table 10 ‣ Appendix E Per-Dimension Alignment Values ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") reports Tucker’s ϕ\phi for each dimension after Procrustes rotation. Zero values indicate zero-padded dimensions (see Section [4.5.3](https://arxiv.org/html/2601.20336v1#S4.SS5.SSS3 "4.5.3 Dimension Handling ‣ 4.5 Procrustes Alignment ‣ 4 Methodology ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis")). The mean ϕ\phi reported in Table [4](https://arxiv.org/html/2601.20336v1#S5.T4 "Table 4 ‣ 5.3 Primary Alignment Tests ‣ 5 Results ‣ Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis") averages across all dimensions including zeros, which can substantially dilute alignment magnitude when comparing spaces of different dimensionality.

Table 10: Per-Dimension Congruence Coefficients

|  |  |  |  |
| --- | --- | --- | --- |
| Dim | Claims–Stats | Claims–Factors | Stats–Factors |
| 1 | 0.342 | 0.309 | 0.690 |
| 2 | 0.397 | 0.310 | 0.693 |
| 3 | 0.345 | 0.000 | 0.000 |
| 4 | 0.454 | 0.000 | 0.000 |
| 5 | 0.529 | 0.000 | 0.000 |
| 6 | 0.302 | 0.000 | 0.000 |
| 7 | 0.360 | 0.000 | 0.000 |
| 8 | 0.285 | 0.000 | 0.000 |
| 9 | 0.318 | 0.000 | 0.000 |
| 10 | 0.000 | 0.000 | 0.000 |
| Mean (all) | 0.333 | 0.062 | 0.138 |
| Mean (non-zero) | 0.370 | 0.310 | 0.691 |

Notably, the statistics–factors comparison shows moderate alignment (ϕ≈0.69\phi\approx 0.69) within the two non-padded dimensions, suggesting genuine correspondence between market statistics and tensor factors that is obscured by the mean across all dimensions. Claims-based comparisons remain limited even within non-padded dimensions (ϕ≈0.31\phi\approx 0.31 for claims–factors).

## Appendix F Methodological Extensions for Future Work

Several methodological refinements could strengthen future iterations of this analysis:

Alternative Alignment Measures. The zero-padding approach for dimension-mismatched Procrustes comparison is conservative but nonstandard. Future work should implement: (i) canonical correlation analysis (CCA) to find maximally correlated linear combinations across spaces; (ii) the RV coefficient or HSIC for rotation-invariant dependence measures; (iii) principal angles between subspaces via Grassmannian distance; and (iv) representational similarity analysis (RSA) or Mantel tests common in cross-modal ML.

Taxonomy Validation. The ten-category taxonomy, while grounded in cryptocurrency discourse, would benefit from domain validation through expert labeling or data-driven topic discovery (e.g., BERTopic, LDA). Ablations with alternative taxonomies and finer-grained categories (L1 vs L2, DeFi subcategories, oracle networks) could reveal whether coarser groupings obscure economically salient distinctions.

Enhanced NLP Calibration. Given the low inter-model agreement (κ=0.14\kappa=0.14), future work should include: human adjudication on a labeled subset to calibrate zero-shot accuracy; domain-adapted few-shot prompting with chain-of-thought rationale; and sentence embedding clustering to derive data-driven categories aligned post-hoc to hypothesized domains.

Expanded Market Features. The seven aggregate statistics omit crypto-native fundamentals that may mediate narrative-market links: on-chain activity metrics (active addresses, transaction counts), token supply mechanics (inflation schedules, unlock events), total value locked (TVL) for DeFi protocols, staking yields, and developer activity (GitHub commits, contributor counts). Multi-venue data consolidation could also reduce venue-specific microstructure noise.

Dynamic Narrative Analysis. The temporal mismatch between static whitepapers (often 2017–2020) and the 2023–2024 market window may understate alignment. Rolling-window analysis with contemporaneous narrative sources (governance proposals, blog posts, Discord announcements) could test whether narrative-market coupling strengthens when narratives are temporally matched to market regimes.