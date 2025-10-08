---
authors:
- Anoushka Harit
- Zhongtian Sun
- Jongmin Yu
doc_id: arxiv:2510.04357v1
family_id: arxiv:2510.04357
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'From News to Returns: A Granger-Causal Hypergraph Transformer on the Sphere'
url_abs: http://arxiv.org/abs/2510.04357v1
url_html: https://arxiv.org/html/2510.04357v1
venue: arXiv q-fin
version: 1
year: 2025
---


Anoushka Harit
University of CambridgeUnited Kingdom
[ah2415@cam.ac.uk](mailto:ah2415@cam.ac.uk)
, 
Zhongtian Sun
University of KentDepartment of Computer Science, University of CambridgeUnited Kingdom
[zs256@kent.ac.uk](mailto:zs256@kent.ac.uk)
 and 
Jongmin Yu
ProjectG.AISouth Korea
[jmandrewyu@gmail.com](mailto:jmandrewyu@gmail.com)

(2025)

###### Abstract.

We propose the Causal Sphere Hypergraph Transformer (CSHT), a novel architecture for interpretable financial time-series forecasting that unifies *Granger-causal hypergraph structure*, *Riemannian geometry*, and *causally masked Transformer attention*. CSHT models the directional influence of financial news and sentiment on asset returns by extracting multivariate Granger-causal dependencies, which are encoded as directional hyperedges on the surface of a hypersphere. Attention is constrained via angular masks that preserve both temporal directionality and geometric consistency. Evaluated on S&P 500 data from 2018 to 2023, including the 2020 COVID-19 shock, CSHT consistently outperforms baselines across return prediction, regime classification, and top-asset ranking tasks. By enforcing predictive causal structure and embedding variables in a Riemannian manifold, CSHT delivers both *robust generalisation across market regimes* and *transparent attribution pathways* from macroeconomic events to stock-level responses. These results suggest that CSHT is a principled and practical solution for trustworthy financial forecasting under uncertainty.

Causal hypergraphs, Spherical embeddings, Transformer models, Financial time series, Interpretable machine learning, Market forecasting

††journalyear: 2025††copyright: cc††conference: 6th ACM International Conference on AI in
Finance; November 15–18, 2025; Singapore, Singapore††booktitle: 6th ACM International Conference on AI in Finance (ICAIF ’25),
November 15–18, 2025, Singapore,
Singapore††doi: 10.1145/3768292.3770414††isbn: 979-8-4007-2220-2/2025/11††ccs: Computing methodologies Sphere neural networks††ccs: Computing methodologies Riemannian geometry††ccs: Computing methodologies Causal inference

## 1. Introduction

Financial markets are driven by a complex interplay of information sources, including price history, macroeconomic indicators, investor sentiment, and news. Although recent deep learning models have improved financial time series forecasting, their lack of interpretability and limited alignment with economic theory limits their adoption in high-stakes settings such as risk management, regulation, and trading (Chen and Shuai, [2021](https://arxiv.org/html/2510.04357v1#bib.bib8); Barbiero et al., [2023](https://arxiv.org/html/2510.04357v1#bib.bib5)).

A core insight from behavioral finance is that investor sentiment mediates the transmission of news to asset prices (Barberis et al., [1998](https://arxiv.org/html/2510.04357v1#bib.bib4); Tetlock, [2007](https://arxiv.org/html/2510.04357v1#bib.bib32)). However, most existing models treat sentiment and news as unstructured inputs, ignoring the directional and hierarchical flow of financial information. Moreover, attention mechanisms in transformers (Vaswani et al., [2017](https://arxiv.org/html/2510.04357v1#bib.bib34)) allow unrestricted dependencies, potentially violating known causal pathways.

To address these challenges, we propose the *Causal Sphere Hypergraph Transformer* (CSHT), a novel architecture that integrates statistical causality, geometric embeddings, and structured attention. CSHT operates in three stages: (i) extract directional, multivariate dependencies using Granger causality across news, sentiment, and returns; (ii) encode these as directed hyperedges in a causal hypergraph; (iii) embed variables on a hypersphere, where attention is constrained using geodesic masks that preserve both causality and angular similarity.

Granger causality provides a statistically grounded approach for identifying temporal influence (e.g.,

|  |  |  |
| --- | --- | --- |
|  | Returnt←{Sentimentt−1,Newst−2}),\text{Return}\_{t}\leftarrow\{\text{Sentiment}\_{t-1},\text{News}\_{t-2}\}), |  |

while acknowledging that it does not imply interventional causality. Embedding variables on the hypersphere allows attention to reflect directional similarity via angular distances, offering geometric consistency under latent market structure.

Our evaluation spans 2018–2023, covering the COVID-19 shock, a major regime shift in global finance. We demonstrate that CSHT outperforms strong baselines (e.g., LSTM, VAR, transformer variants) across return prediction, regime classification, and asset ranking, while maintaining transparent, semantically aligned attention pathways.

#### Contributions.

This paper makes the following contributions:

1. (1)

   We introduce CSHT, a transformer-based model that encodes multi-way Granger dependencies as directed hypergraphs embedded on a hypersphere.
2. (2)

   We propose a geometry-aware attention mechanism that enforces causal masking via geodesic angular similarity.
3. (3)

   We demonstrate that CSHT improves predictive accuracy and interpretability, particularly during volatile market regimes such as the 2020 pandemic.

Our results highlight the promise of causally structured, geometry-aware models for interpretable and trustworthy financial forecasting.

## 2. Related Work

Granger causality (Granger, [1969](https://arxiv.org/html/2510.04357v1#bib.bib12)) is a well-established method for identifying temporal dependencies (Harit et al., [2024a](https://arxiv.org/html/2510.04357v1#bib.bib16)) in financial time series, widely used to assess how sentiment and news influence asset returns (Bollen et al., [2011](https://arxiv.org/html/2510.04357v1#bib.bib6); Nguyen et al., [2015](https://arxiv.org/html/2510.04357v1#bib.bib20)). However, traditional applications are typically pairwise, scale poorly to high-dimensional data, and are not integrated into deep learning pipelines. Recent efforts such as CI-GNN (Zheng et al., [2022](https://arxiv.org/html/2510.04357v1#bib.bib38)) and invariant risk minimisation aim to bridge causality and representation learning, but remain underexplored in finance.

Graph neural networks (GNNs) have shown promise in financial forecasting by modelling stock relationships (Feng et al., [2019](https://arxiv.org/html/2510.04357v1#bib.bib10); Wang et al., [2019](https://arxiv.org/html/2510.04357v1#bib.bib35); Hsu et al., [2021](https://arxiv.org/html/2510.04357v1#bib.bib18)), yet most rely on static or correlation-based edges and lack causal or temporal constraints. This can lead to spurious dependencies, particularly under regime shifts.

Hypergraph neural networks (Bai et al., [2021](https://arxiv.org/html/2510.04357v1#bib.bib3); Sun et al., [2023a](https://arxiv.org/html/2510.04357v1#bib.bib24); Harit et al., [2024b](https://arxiv.org/html/2510.04357v1#bib.bib17); Zhao et al., [2024](https://arxiv.org/html/2510.04357v1#bib.bib37); Sun et al., [2025b](https://arxiv.org/html/2510.04357v1#bib.bib30), [a](https://arxiv.org/html/2510.04357v1#bib.bib28); Harit and Sun, [2025](https://arxiv.org/html/2510.04357v1#bib.bib13); Harit et al., [2025b](https://arxiv.org/html/2510.04357v1#bib.bib15); Sun et al., [2025c](https://arxiv.org/html/2510.04357v1#bib.bib31)) capture higher-order relations across modalities (Sun et al., [2022a](https://arxiv.org/html/2510.04357v1#bib.bib26)), making them suitable for multi-source signals. However, their application in finance remains limited, with few methods offering causal interpretability or robustness in volatile periods.

Geometric deep learning has introduced spherical and hyperbolic embeddings to model relational or hierarchical structures (Chami et al., [2020](https://arxiv.org/html/2510.04357v1#bib.bib7); Li et al., [2022](https://arxiv.org/html/2510.04357v1#bib.bib19); Sun et al., [2023b](https://arxiv.org/html/2510.04357v1#bib.bib25); Dong et al., [2025](https://arxiv.org/html/2510.04357v1#bib.bib9); Harit et al., [2024b](https://arxiv.org/html/2510.04357v1#bib.bib17), [2025a](https://arxiv.org/html/2510.04357v1#bib.bib14); Sun and Harit, [2025](https://arxiv.org/html/2510.04357v1#bib.bib23)). These are well suited to financial domains, but are rarely integrated with causal or temporal reasoning, limiting their alignment with economic structure.

Transformer-based models have achieved strong results in financial time-series prediction (Tsantekidis et al., [2017](https://arxiv.org/html/2510.04357v1#bib.bib33); Omranpour et al., [2024](https://arxiv.org/html/2510.04357v1#bib.bib22); Zhang et al., [2022](https://arxiv.org/html/2510.04357v1#bib.bib36)), but typically rely on unconstrained attention, allowing dependencies that may contradict known causal flows. Probabilistic models like DeepAR (Flunkert et al., [2017](https://arxiv.org/html/2510.04357v1#bib.bib11)) offer uncertainty estimates but lack structural constraints.

Multi-source fusion approaches (Nti et al., [2021](https://arxiv.org/html/2510.04357v1#bib.bib21)) combine sentiment, technical indicators, and macro signals, improving predictive accuracy. However, most models remain black-box without causal grounding or geometric structure.

Our work addresses these gaps by integrating Granger-causal hypergraphs, Riemannian embeddings, and masked transformer attention. This enables structured, interpretable, and geometry-aware forecasting across volatile financial regimes.

## 3. Problem Formulation

Let 𝒟={(xt,st,rt)}t=1T\mathcal{D}=\{(x\_{t},s\_{t},r\_{t})\}\_{t=1}^{T} denote a multimodal financial time series of length TT, where:

* •

  xt∈ℝdxx\_{t}\in\mathbb{R}^{d\_{x}} is a vector of news embeddings (e.g., FinBERT-encoded headlines) at time tt,
* •

  st∈ℝdss\_{t}\in\mathbb{R}^{d\_{s}} is a vector of sentiment scores derived from xtx\_{t} or prior xt′x\_{t^{\prime}} with t′<tt^{\prime}<t,
* •

  rt∈ℝdrr\_{t}\in\mathbb{R}^{d\_{r}} is the log-return vector of drd\_{r} assets at time tt.

Our objective is to model the directional influence of past news and sentiment on future asset returns. For each asset ii, we posit the existence of a subset 𝒞i⊂{x<t,s<t,r<t}\mathcal{C}^{i}\subset\{x\_{<t},s\_{<t},r\_{<t}\} that Granger-causes rtir\_{t}^{i}, capturing the relevant causal parents from the historical information set.

![Refer to caption](Newssphere.jpg)


Figure 1. Overview of the causal forecasting problem setup.

We represent these temporal dependencies using a directed hypergraph 𝒢=(𝒱,ℰ)\mathcal{G}=(\mathcal{V},\mathcal{E}), where each node v∈𝒱v\in\mathcal{V} corresponds to a lagged variable (e.g., xt−2x\_{t-2} or st−1s\_{t-1}), and each directed hyperedge e=({v1,…,vk}→rti)∈ℰe=(\{v\_{1},...,v\_{k}\}\rightarrow r\_{t}^{i})\in\mathcal{E} encodes a multi-source Granger-causal relation toward an asset return.

Each node v∈𝒱v\in\mathcal{V} is embedded on the surface of an nn-dimensional unit hypersphere 𝕊n\mathbb{S}^{n}, and attention is computed using geodesically masked angular similarity:

|  |  |  |
| --- | --- | --- |
|  | Attention​(vi,vj)∝cos⁡(θi​j)=⟨vi,vj⟩‖vi‖⋅‖vj‖,vi,vj∈𝕊n.\text{Attention}(v\_{i},v\_{j})\propto\cos(\theta\_{ij})=\frac{\langle v\_{i},v\_{j}\rangle}{\|v\_{i}\|\cdot\|v\_{j}\|},\quad v\_{i},v\_{j}\in\mathbb{S}^{n}. |  |

The forecasting task is defined as learning a causal function ff over the hypergraph-constrained history ℋ<t\mathcal{H}\_{<t}:

|  |  |  |
| --- | --- | --- |
|  | y^t=f​(ℋ<t;𝒢)whereℋ<t={xt−k,st−k,rt−k}k=1τ.\hat{y}\_{t}=f(\mathcal{H}\_{<t};\mathcal{G})\quad\text{where}\quad\mathcal{H}\_{<t}=\{x\_{t-k},s\_{t-k},r\_{t-k}\}\_{k=1}^{\tau}. |  |

The learning objective minimises the expected prediction loss while respecting the structure encoded in 𝒢\mathcal{G}:

|  |  |  |
| --- | --- | --- |
|  | f^=arg⁡minf∈ℱ𝒢⁡𝔼t​[ℒ​(f​(ℋ<t),yt)],\hat{f}=\arg\min\_{f\in\mathcal{F}\_{\mathcal{G}}}\ \mathbb{E}\_{t}\left[\mathcal{L}(f(\mathcal{H}\_{<t}),y\_{t})\right], |  |

where ℱ𝒢\mathcal{F}\_{\mathcal{G}} is the class of functions that conform to the Granger-derived hypergraph structure, and ℒ\mathcal{L} is a suitable prediction loss (e.g., mean squared error or cross-entropy). This formulation enables structured, geometry-aware modelling of financial signals under uncertainty.

Example. A real-world instance of this setting is the 2020 COVID-19 pandemic shock, which induced abrupt changes in market regimes. During this period, sentiment signals st−1s\_{t-1} extracted from pandemic-related news embeddings xt−2x\_{t-2}, such as lockdown announcements and infection statistics, exhibited strong Granger-causal influence on sector-specific returns rtir\_{t}^{i}, particularly in healthcare, energy, and travel. CSHT captures such directional, multi-source relations by constructing hyperedges of the form:

|  |  |  |
| --- | --- | --- |
|  | {xt−2COVID,st−1fear}→rthealth.\{x\_{t-2}^{\text{COVID}},s\_{t-1}^{\text{fear}}\}\rightarrow r\_{t}^{\text{health}}. |  |

![Refer to caption](Covid.png)


Figure 2. Causal influence during the COVID-19 regime: News xt−2COVIDx\_{t-2}^{\text{COVID}} and sentiment st−1fears\_{t-1}^{\text{fear}} drive returns rthealthr\_{t}^{\text{health}}. CSHT captures such patterns via hyperspherical hyperedges and causal attention masks.††:

These relations are embedded on the hypersphere and used to define causal attention masks, constraining the prediction function ff to attend only to valid information flows. This formulation supports both short-term forecasting and regime classification by allowing the model to adapt to structural changes in 𝒢\mathcal{G} over time—for example, a surge in the influence of health-related sentiment during exogenous shocks.

## 4. Methodology

The Causal Sphere Hypergraph Transformer (CSHT) models directional market influence by combining Granger-causal structure, geometric embeddings, and constrained attention. The architecture comprises four main stages: (i) discovery of causal hypergraphs over news, sentiment, and returns; (ii) spherical embedding of variables on a Riemannian manifold; (iii) transformer-based geodesic attention with causal masking; and (iv) manifold-constrained training for financial forecasting.

![Refer to caption](StockPrediction.png)


Figure 3. CSHT architecture: Granger-causal links connect news, sentiment, and returns. Nodes are embedded on a hypersphere and processed via masked geodesic attention for interpretable forecasting.

### 4.1. Financial Causal Flow: News, Sentiment, Returns

We model financial dynamics through structured interactions among three modalities:

* •

  News embeddings xt∈ℝdxx\_{t}\in\mathbb{R}^{d\_{x}} are extracted from daily headlines using FinBERT, encoding semantic tone and topical context;
* •

  Sentiment signals st∈ℝdss\_{t}\in\mathbb{R}^{d\_{s}} are derived from temporally smoothed and aggregated news embeddings xt′x\_{t^{\prime}} for t′<tt^{\prime}<t, reflecting delayed investor response;
* •

  Returns rt∈ℝdrr\_{t}\in\mathbb{R}^{d\_{r}} are log-transformed asset returns, driven by prior news and sentiment inputs.

![Refer to caption](flow.png)


Figure 4. Illustrative causal flow: news affects sentiment, which drives index movements (SPY) and individual returns (e.g., JPM, DAL).

This induces an interpretable directional flow:

|  |  |  |
| --- | --- | --- |
|  | xt−k→st−j,st−j→rt,xt−k→rtx\_{t-k}\rightarrow s\_{t-j},\quad s\_{t-j}\rightarrow r\_{t},\quad x\_{t-k}\rightarrow r\_{t} |  |

CSHT explicitly encodes and constrains this flow via a causality-aware architecture.

### 4.2. Causal Hypergraph Construction

Given a multivariate time series 𝒟={(xt,st,rt)}t=1T\mathcal{D}=\{(x\_{t},s\_{t},r\_{t})\}\_{t=1}^{T}, we apply Granger causality tests to detect lagged directional dependencies. For each return variable rtir^{i}\_{t}, we identify a set of predictors 𝒞i⊂ℋ<t\mathcal{C}^{i}\subset\mathcal{H}\_{<t} such that:

|  |  |  |
| --- | --- | --- |
|  | ∃j∈𝒞i:ℙ(rti∣𝒞i)≠ℙ(rti∣𝒞i∖{j})\exists j\in\mathcal{C}^{i}:\quad\mathbb{P}(r^{i}\_{t}\mid\mathcal{C}^{i})\neq\mathbb{P}(r^{i}\_{t}\mid\mathcal{C}^{i}\setminus\{j\}) |  |

Each such set defines a directed hyperedge 𝒞i→rti\mathcal{C}^{i}\rightarrow r^{i}\_{t}, producing a hypergraph 𝒢=(𝒱,ℰ)\mathcal{G}=(\mathcal{V},\mathcal{E}) over lagged news, sentiment, and return variables.

Node Specification. Each node v∈𝒱v\in\mathcal{V} represents a lagged input from one of three modalities: (i) news embeddings xt−kx\_{t-k}, (ii) sentiment scores st−js\_{t-j}, or (iii) past returns rt−kr\_{t-k}. Nodes are included only where Granger causality indicates significant influence. The resulting hypergraph captures temporally indexed semantic, affective, and financial signals.

An example hyperedge:

|  |  |  |
| --- | --- | --- |
|  | {xt−2COVID,st−1fear}→rthealthcare\{x^{\text{COVID}}\_{t-2},s^{\text{fear}}\_{t-1}\}\rightarrow r^{\text{healthcare}}\_{t} |  |

illustrates a multi-source causal link from pandemic-related inputs to sector returns.

### 4.3. Spherical Riemannian Embedding

Each node v∈𝒱v\in\mathcal{V} (i.e., each lagged variable identified as causally relevant) is assigned an embedding v∈𝕊n⊂ℝn+1v\in\mathbb{S}^{n}\subset\mathbb{R}^{n+1}, lying on the unit hypersphere:

|  |  |  |
| --- | --- | --- |
|  | 𝕊n={x∈ℝn+1:‖x‖=1}\mathbb{S}^{n}=\{x\in\mathbb{R}^{n+1}:\|x\|=1\} |  |

These embeddings are initialised randomly and updated during training. The Riemannian structure imposes angular sensitivity:

|  |  |  |
| --- | --- | --- |
|  | d𝕊n​(x,y)=arccos⁡(⟨x,y⟩)d\_{\mathbb{S}^{n}}(x,y)=\arccos(\langle x,y\rangle) |  |

After each parameter update, embeddings are projected back onto the manifold to preserve geometric consistency:

|  |  |  |
| --- | --- | --- |
|  | Π​(x)=x‖x‖,x∈ℝn+1∖{0}\Pi(x)=\frac{x}{\|x\|},\quad x\in\mathbb{R}^{n+1}\setminus\{0\} |  |

This ensures that causal similarity is preserved in angular space.

### 4.4. Causal Attention with Geodesic Masking

We apply a transformer encoder over the hypergraph, using causal masks to restrict attention to Granger-derived parents. For query qiq\_{i} and key kjk\_{j}, attention is computed as:

|  |  |  |
| --- | --- | --- |
|  | Attn​(i,j)={exp⁡(λ⋅⟨qi,kj⟩)Zi,if ​vj∈𝒞i0,otherwise\text{Attn}(i,j)=\begin{cases}\frac{\exp(\lambda\cdot\langle q\_{i},k\_{j}\rangle)}{Z\_{i}},&\text{if }v\_{j}\in\mathcal{C}\_{i}\\ 0,&\text{otherwise}\end{cases} |  |

where λ\lambda is a temperature scaling factor and ZiZ\_{i} is the normalisation constant over valid causal parents of viv\_{i}. This mechanism ensures that attention remains both *geometrically constrained* (Li et al., [2022](https://arxiv.org/html/2510.04357v1#bib.bib19); Chami et al., [2020](https://arxiv.org/html/2510.04357v1#bib.bib7)) through cosine similarity in the hypersphere 𝕊n\mathbb{S}^{n} and *causally grounded* through the enforcement of Granger-derived dependencies.

### 4.5. Prediction and Riemannian Training

The output of the transformer is used to predict the financial target yty\_{t} (e.g., next-day return r^t+1\hat{r}\_{t+1} or a market regime label). The model is trained to minimise the expected loss over time, while respecting the geometry of the hyperspherical embedding:

|  |  |  |
| --- | --- | --- |
|  | ℒ=1T​∑t=1Tℓ​(f​(ℋ<t;𝒢),yt)\mathcal{L}=\frac{1}{T}\sum\_{t=1}^{T}\ell(f(\mathcal{H}\_{<t};\mathcal{G}),y\_{t}) |  |

Gradients are computed in the ambient Euclidean space ℝn+1\mathbb{R}^{n+1}, and updated embeddings are projected back onto the hypersphere to preserve Riemannian structure:

|  |  |  |
| --- | --- | --- |
|  | x(k+1)←Π​(x(k)−η​∇xℒ)x^{(k+1)}\leftarrow\Pi\left(x^{(k)}-\eta\nabla\_{x}\mathcal{L}\right) |  |

where Π​(x)=x‖x‖\Pi(x)=\frac{x}{\|x\|} denotes the projection operator, and η\eta is the learning rate.

This training scheme ensures geometric validity of representations throughout optimisation, enabling stable learning of directional causal dependencies on the manifold.

Regime Adaptation. To capture the evolving market structure, the hypergraph 𝒢\mathcal{G} is periodically updated using a sliding window strategy. This enables CSHT to adapt to structural breaks or regime shifts by dynamically reconfiguring its causal edge set ℰ\mathcal{E}, thereby supporting both robust forecasting and the detection of market phase transitions.

## 5. Experimental Setup

We evaluate the Causal Sphere Hypergraph Transformer (CSHT) on real-world financial forecasting tasks. The model aims to predict (i) next-day asset-level returns and (ii) broader market regime shifts using historical price and sentiment signals. Our hypothesis is that causally masked attention over hyperspherical embeddings improves accuracy, robustness, and interpretability relative to strong baselines.

### 5.1. Data Collection and Processing

Our dataset spans 2018–2023 and includes the COVID-19 shock (Q1–Q2 2020), offering a natural testbed for model robustness under regime shifts. This enables evaluation of the model’s adaptability to macroeconomic shocks during training and generalisation to post-pandemic regimes.

We focus on stocks in the S&P 500 index between 2018 and 2023. We retain 450 actively traded stocks after filtering out those with incomplete trading history. Historical prices and volumes are obtained from Yahoo Finance111<https://finance.yahoo.com/>.

Table 1. Statistics of historical price data

| Split | Date Range | # Days | # Stocks |
| --- | --- | --- | --- |
| Training | 01/01/2018–31/12/2020 | 756 | 450 |
| Validation | 01/01/2021–31/12/2021 | 252 | 450 |
| Test | 01/01/2022–30/06/2023 | 376 | 450 |

Daily log-returns are computed as:

|  |  |  |
| --- | --- | --- |
|  | Rit=Pit−Pit−1Pit−1R\_{i}^{t}=\frac{P\_{i}^{t}-P\_{i}^{t-1}}{P\_{i}^{t-1}} |  |

where PitP\_{i}^{t} is the adjusted close price of stock ii on day tt.

News Sentiment.
We use the Twitter Financial News Sentiment dataset222<https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment>, which includes over 500,000 financial tweets labeled as *positive*, *negative*, or *neutral*. We extract 50,000 tweets referencing S&P 500 stocks using ticker symbols and company names. FinBERT (Araci, [2019](https://arxiv.org/html/2510.04357v1#bib.bib2)) is used to compute daily average sentiment per stock. Neutral score (0) is assigned when no tweets are matched.

#### Feature Construction.

Each stock-day feature vector includes:

* •

  Market features: Log-return, 30-day realised volatility, and trading volume;
* •

  Sentiment features: Mean FinBERT sentiment polarity per day.

All features are z-normalised using training-set statistics.

### 5.2. Causal Hypergraph Construction

We apply multivariate Granger causality tests with a maximum lag of K=5K=5 to detect multi-source influences on each return variable. For each trading day tt, we construct a directed hypergraph 𝒢t=(𝒱,ℰt)\mathcal{G}\_{t}=(\mathcal{V},\mathcal{E}\_{t}):

* •

  𝒱\mathcal{V} includes lagged news, sentiment, and return variables;
* •

  ℰt\mathcal{E}\_{t} contains hyperedges 𝒞i→rti\mathcal{C}^{i}\rightarrow r\_{t}^{i} if the null hypothesis of no Granger causality is rejected at FDR-adjusted p<0.01p<0.01.

This structure is used to define attention masks in CSHT.

### 5.3. Model Configuration

Each node is embedded on the unit hypersphere 𝕊n\mathbb{S}^{n} and passed through a transformer with masked attention restricted to causal parents. Cosine similarity defines attention scores. CSHT is evaluated on:

* •

  Task 1 (Regression): Predict next-day log-return rt+1ir\_{t+1}^{i};
* •

  Task 2 (Classification): Predict market regime based on the sign of 3-day forward return of the S&P 500 index.

### 5.4. Baselines

We benchmark CSHT against six competitive models that reflect the current state of multimodal financial forecasting:

* •

  FinBERT-RNN (Araci, [2019](https://arxiv.org/html/2510.04357v1#bib.bib2)): Combines FinBERT-derived sentiment embeddings with an LSTM to forecast future returns.
* •

  CNN-LOB (Tsantekidis et al., [2017](https://arxiv.org/html/2510.04357v1#bib.bib33)): Applies convolutional layers to limit order book (LOB) snapshots for price movement prediction.
* •

  Money (Sun et al., [2023a](https://arxiv.org/html/2510.04357v1#bib.bib24)): An ensemble that integrates adversarial hypergraph learning with CNN-based feature extraction for financial events.
* •

  FinGAT (Hsu et al., [2021](https://arxiv.org/html/2510.04357v1#bib.bib18)): A graph attention network that models sentiment and temporal price dependencies to forecast directional trends.
* •

  TEANet (Zhang et al., [2022](https://arxiv.org/html/2510.04357v1#bib.bib36)): A transformer architecture that fuses historical returns and sentiment signals using multi-head attention.
* •

  Higher Order Transformer (HOT) (Omranpour et al., [2024](https://arxiv.org/html/2510.04357v1#bib.bib22)): Captures multimodal financial dependencies using a higher-order transformer over structured sequences of sentiment and market signals.

All models are trained and evaluated using the same asset universe, feature inputs (news, sentiment, price), and target definitions to ensure fair comparison.

### 5.5. Evaluation Protocol

We use a non-overlapping temporal split:

* •

  Training: 2018–2020;
* •

  Validation: 2021;
* •

  Test: 2022–mid-2023.

All models are trained using the Adam optimiser (learning rate 10−410^{-4}, batch size 32), with early stopping based on validation loss. Each experiment is repeated 5 times with different seeds.

#### Metrics.

We report:

* •

  MAE: Mean absolute error (return prediction);
* •

  Regime Accuracy: Bull/bear classification accuracy;
* •

  NDCG@10: Quality of top-10 asset recommendations;
* •

  Causal Alignment: Fraction of attended edges aligned with Granger-causal structure.

#### Robustness Analysis.

To assess generalisation across market regimes, we evaluate performance in both pandemic-era (2020) and post-pandemic test sets (2022–2023), tracking consistency of attention and causal alignment.

### 5.6. Implementation Details

All models are implemented in PyTorch and trained on an NVIDIA RTX 2080 Ti GPU. CSHT uses a 2-layer transformer with 64 hidden units, 4 attention heads, and angular scaling λ=10\lambda=10. Manifold constraints are enforced via Π​(x)=x/‖x‖\Pi(x)=x/\|x\| after each update. Hyperparameters are tuned using validation NDCG@10 (Task 2) and MAE (Task 1).

## 6. Results and Discussion

We evaluate the Causal Sphere Hypergraph Transformer (CSHT) on two primary tasks: (i) next-day return forecasting and (ii) market regime classification (bull versus bear). Our goal is to assess whether integrating directional causal structure and hyperspherical attention improves both predictive accuracy and interpretability. Experiments span 450 S&P 500 stocks over the period 2018 to 2023.

### 6.1. Quantitative Evaluation

We benchmark CSHT against five strong baselines: FinBERT-RNN(Araci, [2019](https://arxiv.org/html/2510.04357v1#bib.bib2)), CNN-LOB (Tsantekidis et al., [2017](https://arxiv.org/html/2510.04357v1#bib.bib33)), Money (Zhang et al., [2022](https://arxiv.org/html/2510.04357v1#bib.bib36)), Transformer-AN (Zhang et al., [2022](https://arxiv.org/html/2510.04357v1#bib.bib36)),FinGAT (Hsu et al., [2021](https://arxiv.org/html/2510.04357v1#bib.bib18)),and Higher Order Transformer(HOT) (Omranpour et al., [2024](https://arxiv.org/html/2510.04357v1#bib.bib22)). Evaluation metrics include: (i) MAE for next-day return prediction, (ii) Regime Accuracy for bull/bear classification, and (iii) NDCG@10 to assess top-asset recommendation quality.

Table 2. Performance on S&P 500 stocks (2018–2023). Best results in bold.

| Model | MAE ↓ | Accuracy (%) ↑ | NDCG@10 ↑ |
| --- | --- | --- | --- |
| FinBERT-RNN | 0.0213 | 65.4 | 0.612 |
| CNN-LOB | 0.0205 | 67.2 | 0.625 |
| Money | 0.0198 | 69.1 | 0.634 |
| TEANet | 0.0189 | 70.6 | 0.639 |
| FinGAT | 0.0187 | 71.3 | 0.641 |
| HOT | 0.0184 | 69.0 | 0.636 |
| CSHT (ours) | 0.0162 | 74.6 | 0.683 |

CSHT achieves the strongest results across all metrics. It reduces MAE by 13.4% relative to the strongest baseline (FinGAT), improves classification accuracy by 3.3 percentage points, and attains the highest NDCG@10—demonstrating superior ranking under volatility.

### 6.2. Causal Alignment Analysis

We compute the proportion of attention mass aligned with Granger-causal dependencies, denoted as Causal Alignment. Only models with interpretable attention (FinGAT and CSHT) are included.

Table 3. Causal alignment (%) with Granger-causal graph.

| Model | Causal Alignment (%) ↑ |
| --- | --- |
| FinGAT | 21.3 |
| CSHT (ours) | 66.4 |

CSHT exhibits substantially higher alignment with validated causal structure, confirming its semantic interpretability and robust information flow control.

### 6.3. Ablation Study: Contribution of Causal and Geometric Components

We conduct a detailed ablation study to isolate the contribution of causal masking and spherical attention in CSHT. In addition to our two main ablations, we include further variants to analyse robustness and geometric effects.

* •

  CSHT without Causal Mask: Removes Granger-based masking, allowing unconstrained attention.
* •

  CSHT without Spherical Attention: Uses standard dot-product attention in Euclidean space.
* •

  Full Mask + Spherical Attention: Applies geodesic attention over a fully connected graph, isolating the effect of hyperspherical geometry under noisy dependencies.
* •

  Causal Mask + Euclidean Attention: Uses causal masking but computes attention in Euclidean space, testing the independent value of causal structure.
* •

  CSHT + Input Noise: Adds Gaussian noise (σ=0.05\sigma=0.05) to sentiment and news embeddings, evaluating robustness under volatility.

Table 4. Ablation study on validation set (2021).

| Model Variant | MAE ↓ | Accuracy (%) ↑ |
| --- | --- | --- |
| Full Mask + Spherical Attention | 0.0171 | 72.3 |
| Causal Mask + Euclidean Attention | 0.0177 | 71.2 |
| CSHT without Causal Mask | 0.0184 | 70.1 |
| CSHT without Spherical Attention | 0.0175 | 71.4 |
| CSHT + Input Noise | 0.0172 | 73.1 |
| Full CSHT | 0.0162 | 74.6 |

Interpretation.
Causal masking enhances generalisation by filtering spurious dependencies, while spherical attention captures relational structure via angular similarity. The *Full Mask + Spherical* variant outperforms its Euclidean counterpart, confirming the benefit of geometric bias. Stable performance under input noise further demonstrates robustness to volatility (Sun et al., [2021](https://arxiv.org/html/2510.04357v1#bib.bib29)). We also tested sensitivity to hypergraph parameters (lag K∈{3,5,7}K\in\{3,5,7\} and thresholds p<{0.05,0.01,0.001}p<\{0.05,0.01,0.001\}). Performance varied by ¡3%, and key causal links (e.g., COVID sentiment → sector returns) remained stable—indicating CSHT’s resilience to graph sparsity and noise.

### 6.4. Sector-Wise Regime Classification

We report regime classification accuracy per sector on the 2022–2023 test set. CSHT consistently outperforms across all sectors, with notable gains in high-volatility domains.

Table 5. Sector-wise classification accuracy (%, 2022–2023 test period). Best in bold.

| Sector | FinBERT-RNN | CNN-LOB | Money | HOT | FinGAT | CSHT |
| --- | --- | --- | --- | --- | --- | --- |
| Technology | 61.8 | 64.3 | 68.1 | 71.0 | 69.2 | 74.8 |
| Finance | 60.9 | 65.1 | 67.5 | 70.1 | 68.9 | 75.3 |
| Energy | 63.2 | 66.7 | 69.4 | 70.9 | 70.4 | 72.9 |
| Healthcare | 59.7 | 62.5 | 66.1 | 68.3 | 66.3 | 70.2 |

The strongest gains appear in sectors influenced by macroeconomic sentiment, demonstrating the model’s capacity to trace causal signals across hierarchies.

FinBERT RNN and CNN LOB underperform due to the limited relational structure. Money and HOT benefit from hypergraph and multimodal features. FinGAT adds relational reasoning, but lacks a higher-order context. CSHT achieves the best performance by modeling directional multivariable influences with causal hyperedges and spherical embeddings.

### 6.5. Runtime and Inference Efficiency

We compare epoch-level training time and per-stock inference latency. CSHT remains efficient enough for real-time use cases, while offering stronger predictive and interpretability benefits.

Table 6. Training and inference time per epoch. Best results in bold.

| Model | Training (s) | Inference (ms) |
| --- | --- | --- |
| FinBERT RNN | 42.3 | 1.2 |
| CNN LOB | 55.6 | 1.7 |
| TEANet | 62.1 | 1.8 |
| Money | 64.3 | 2.0 |
| HOT | 66.5 | 2.0 |
| FinGAT | 68.7 | 1.6 |
| CSHT (Ours) | 73.4 | 2.1 |

![Refer to caption](RuntimeScaling.png)


Figure 5. Runtime scaling of CSHT with number of assets. The model maintains near-linear growth, ensuring scalability to large portfolios.††:

#### Runtime scaling with asset pool size.

Figure [5](https://arxiv.org/html/2510.04357v1#acmlabel2 "Figure 5 ‣ 6.5. Runtime and Inference Efficiency ‣ 6. Results and Discussion ‣ From News to Returns: A Granger-Causal Hypergraph Transformer on the Sphere") shows that CSHT scales nearly linearly with the number of assets, confirming its feasibility for large-scale portfolio forecasting. The runtime overhead remains manageable due to sparsified causal masking and efficient spherical projection layers.

### 6.6. Interpretable Attention: Case Study on Fed Rate Hike (June 2022)

We examine CSHT’s attention behaviour during the U.S. Federal Reserve’s 75 basis point rate hike in June 2022, a pivotal macroeconomic event. The causal attention matrix centred on JPMorgan Chase (JPM) reveals a coherent propagation path through semantically meaningful intermediaries.

![Refer to caption](Fedrate.png)


Figure 6. Causal attention weights for JPMorgan during the June 2022 Fed hike. Key nodes align with Granger edges; minor deviations reflect contextual cues.

The inferred chain of influence follows the pathway: Fed Rate Announcement →\rightarrow Finance Sentiment →\rightarrow Energy Sentiment →\rightarrow SPY Index →\rightarrow JPM Return. This path aligns with well-established economic transmission mechanisms, where central bank policy shocks influence investor sentiment, sectoral expectations, and downstream asset prices. CSHT assigns high attention weights to each node along this chain (e.g., 0.65 to finance sentiment, 0.55 to energy sentiment, 0.44 to SPY, and 0.72 to JPM), demonstrating its capacity to focus on economically relevant causal signals. Unlike conventional transformer-based models with diffuse or entangled attention maps, CSHT produces interpretable and directionally grounded attributions, improving the model’s transparency and actionable utility in decision-support settings.

### 6.7. Interpretable Attention: Case Study on Pandemic-Induced Crash (March 2020)

We further investigate CSHT’s response to extreme exogenous shocks by analysing the market collapse on 9 March 2020, triggered by oil price disputes and intensifying COVID-19 fears. This event offers a natural test for the model’s robustness to sudden structural breaks.

![Refer to caption](Exom.png)


Figure 7. Causal attention weights assigned by CSHT to nodes influencing ExxonMobil (COVID-19 crash, March 2020).

For ExxonMobil (XOM), the attention pathway indicates the sequence: Global COVID News →\rightarrow Energy Sentiment →\rightarrow Oil Volatility Index (OVX) →\rightarrow XOM Return. This mirrors the economic logic of oil-sensitive assets being directly affected by sentiment contagion and price turbulence. CSHT assigned high attention scores to sentiment nodes (e.g., 0.68 to energy sentiment, 0.62 to OVX) and correctly forecast a sharp decline in return (−4.5%-4.5\% predicted vs. −4.8%-4.8\% realised). This highlights CSHT’s robustness to sudden regime shifts and its capacity to isolate causally grounded, interpretable trajectories even under severe non-linear disruptions.

These case studies demonstrate how CSHT disentangles information flows across heterogeneous sources (Sun et al., [2022b](https://arxiv.org/html/2510.04357v1#bib.bib27))and aligns them with macrofinancial structure, making it suitable for transparent decision support in high-stakes domains.

### 6.8. COVID-Period Robustness

To assess model stability under market stress, we report regime classification accuracy during the COVID-19 crash period (March to June 2020), when financial conditions exhibited extreme volatility and structural breaks.

Table 7. Regime classification accuracy during COVID-19 crash (March–June 2020).

| Model | Accuracy (%) |
| --- | --- |
| FinBERT-RNN | 61.2 |
| CNN-LOB | 63.5 |
| TEANet | 67.5 |
| Money | 65.8 |
| FinGAT | 66.4 |
| HOT | 69.0 |
| CSHT (Ours) | 74.6 |

CSHT achieves the highest accuracy during this turbulent period, outperforming all baselines by a notable margin. Its structured causal masking and hyperspherical attention appear to confer greater resilience to external shocks and regime discontinuities, an essential requirement for deployment in real-world financial systems subject to macroeconomic surprises.

### 6.9. Event-Aligned Forecasts: Illustrative Predictions

We present a selection of CSHT return forecasts aligned with impactful real-world financial events. These examples illustrate the model’s capacity for directionally accurate, causally grounded predictions across sectors and market conditions.

Table 8. CSHT predictions aligned with real-world events. Forecasts include confidence intervals derived from sampled causal masks.

| Stock | Date | Predicted (%) | Actual (%) | Event / Source |
| --- | --- | --- | --- | --- |
| Apple (AAPL) | 25 Oct 2021 | +2.1±0.3+2.1\pm 0.3 | +2.3 | iPhone launch cycle (CNBC) |
| JPMorgan (JPM) | 15 Jun 2022 | −1.9±0.4-1.9\pm 0.4 | -1.8 | Fed rate hike, regulatory outlook (Reuters) |
| ExxonMobil (XOM) | 9 Mar 2020 | −4.5±0.7-4.5\pm 0.7 | -4.8 | COVID-19 oil price collapse (Bloomberg) |
| Walmart (WMT) | 17 May 2022 | −2.2±0.5-2.2\pm 0.5 | -2.4 | Earnings miss amid inflation (WSJ) |
| Tesla (TSLA) | 5 Jan 2023 | +4.3±0.6+4.3\pm 0.6 | +4.5 | Q4 delivery report (Reuters) |
| Pfizer (PFE) | 11 Nov 2021 | +1.7±0.4+1.7\pm 0.4 | +1.9 | Positive vaccine efficacy report (CNN) |

CSHT captures high-impact shifts across diverse market sectors with tight prediction intervals and correct directional movement. Each forecast results from dynamic causal paths involving sentiment, macroeconomic signals, and latent structural regimes. The confidence bounds reflect model epistemic uncertainty due to changing hyperedge configurations under causal masking.

### 6.10. Summary of Findings

CSHT achieves strong predictive performance, semantic interpretability, and robustness across regimes. Key findings include:

* •

  Predictive Superiority: CSHT outperforms competitive baselines on return prediction, regime classification, and top-kk asset ranking, supporting its suitability for high-stakes decision-making.
* •

  Robustness to Shocks: The model remains stable during volatility events (e.g., COVID crash, Fed hikes), without retraining or loss of accuracy.
* •

  Causal Transparency: Structured attention over news, sentiment, and returns yields interpretable pathways aligned with domain knowledge, including known monetary and sectoral effects.

These results highlight the benefits of combining causal reasoning with geometric learning for trustworthy financial forecasting under non-stationary conditions.

## 7. Discussion

CSHT effectively captures dynamic, multi-hop dependencies in financial markets through a causal hypergraph framework. Unlike prior models based on shallow correlations or opaque attention, CSHT yields semantically coherent influence paths that enhance both accuracy and interpretability. Case studies confirm that its attention aligns with economic reasoning during volatile events, supporting applications in trading, risk assessment, and portfolio optimization. The model remains robust to regime shifts without retraining and is adaptable to domains such as cryptocurrencies or ESG-based investing. However, CSHT infers causal structure via attention weights, which do not imply interventional causality. Future work will incorporate counterfactual modules, such as do-calculus or invariant learning, to enable stronger causal claims.

## 8. Conclusion

We have presented CSHT, a novel Causal Sphere Hypergraph Transformer that integrates geometric learning, temporal attention, and causally structured representations to predict asset returns in dynamic financial environments. Through extensive empirical evaluations and real-world case studies, we demonstrate that CSHT delivers competitive performance, strong regime robustness, and interpretable causal attributions. Our results provide compelling evidence that embedding domain-specific economic structure via hypergraphs and causal signal flow can yield trustworthy and effective financial AI models. Beyond empirical gains, CSHT offers practical value in improving decision transparency and fostering safer deployment in high-stakes financial contexts.
Future directions include integrating interventional reasoning, scaling to cross-market generalisation, and extending CSHT to simulate economic stress tests or facilitate human-AI dialogue in portfolio diagnostics. Our work contributes towards a more transparent and causally principled foundation for next-generation financial machine learning systems.

## 9. Acknowledgments

We thank Dr. Xiaowen Dong from the University of Oxford for his insightful feedback, which helped improve this work.

## References

* (1)
* Araci (2019)

  Dogu Araci. 2019.
  Finbert: Financial sentiment analysis with pre-trained language models.
  *arXiv preprint arXiv:1908.10063* (2019).
* Bai et al. (2021)

  Song Bai, Feihu Zhang, and Philip HS Torr. 2021.
  Hypergraph convolution and hypergraph attention.
  *Pattern Recognition* 110 (2021), 107637.
* Barberis et al. (1998)

  Nicholas Barberis, Andrei Shleifer, and Robert Vishny. 1998.
  A model of investor sentiment.
  *Journal of financial economics* 49, 3 (1998), 307–343.
* Barbiero et al. (2023)

  Pietro Barbiero, Gabriele Ciravegna, Francesco Giannini, Mateo Espinosa Zarlenga, Lucie Charlotte Magister, Alberto Tonda, Pietro Lió, Frederic Precioso, Mateja Jamnik, and Giuseppe Marra. 2023.
  Interpretable neural-symbolic concept reasoning. In *International Conference on Machine Learning*. PMLR, 1801–1825.
* Bollen et al. (2011)

  Johan Bollen, Huina Mao, and Xiaojun Zeng. 2011.
  Twitter mood predicts the stock market.
  *Journal of computational science* 2, 1 (2011), 1–8.
* Chami et al. (2020)

  Ines Chami, Adva Wolf, Da-Cheng Juan, Frederic Sala, Sujith Ravi, and Christopher Ré. 2020.
  Low-dimensional hyperbolic knowledge graph embeddings.
  *arXiv preprint arXiv:2005.00545* (2020).
* Chen and Shuai (2021)

  Yi-Syuan Chen and Hong-Han Shuai. 2021.
  Meta-transfer learning for low-resource abstractive summarization. In *Proceedings of the AAAI conference on artificial intelligence*, Vol. 35. 12692–12700.
* Dong et al. (2025)

  Tiansi Dong, Mateja Jamnik, and Pietro Lio. 2025.
  Neural Reasoning for Sure Through Constructing Explainable Models.
  (2025).
* Feng et al. (2019)

  Fuli Feng, Xiangnan He, Xiang Wang, Cheng Luo, Yiqun Liu, and Tat-Seng Chua. 2019.
  Temporal relational ranking for stock prediction.
  *ACM Transactions on Information Systems (TOIS)* 37, 2 (2019), 1–30.
* Flunkert et al. (2017)

  Valentin Flunkert, David Salinas, and Jan Gasthaus. 2017.
  Deepar: Probabilistic forecasting with autoregressive recurrent networks.
  *arXiv preprint arXiv:1704.04110* 23 (2017).
* Granger (1969)

  Clive WJ Granger. 1969.
  Investigating causal relations by econometric models and cross-spectral methods.
  *Econometrica: journal of the Econometric Society* (1969), 424–438.
* Harit and Sun (2025)

  Anoushka Harit and Zhongtian Sun. 2025.
  Causal Spherical Hypergraph Networks for Modelling Social Uncertainty.
  *arXiv preprint arXiv:2506.17840* (2025).
* Harit et al. (2025a)

  Anoushka Harit, Zhongtian Sun, and Noura Al Moubayed. 2025a.
  TextFold: A Geometric Hypergraph Framework for Protein Structure Prediction with Scientific Literature Integration.
  *Procedia Computer Science* 264 (2025), 309–318.
* Harit et al. (2025b)

  Anoushka Harit, Zhongtian Sun, and Suncica Hadzidedic. 2025b.
  ManifoldMind: Dynamic Hyperbolic Reasoning for Trustworthy Recommendations.
  *arXiv preprint arXiv:2507.02014* (2025).
* Harit et al. (2024a)

  Anoushka Harit, Zhongtian Sun, Jongmin Yu, and Noura Al Moubayed. 2024a.
  Monitoring Behavioral Changes Using Spatiotemporal Graphs: A Case Study on the StudentLife Dataset. In *NeurIPS 2024 Workshop on Behavioral Machine Learning*.
* Harit et al. (2024b)

  Anoushka Harit, Zhongtian Sun, Jongmin Yu, and Noura Al Moubayed. 2024b.
  Breaking Down Financial News Impact: A Novel AI Approach with Geometric Hypergraphs.
  *arXiv preprint arXiv:2409.00438* (2024).
* Hsu et al. (2021)

  Yi-Ling Hsu, Yu-Che Tsai, and Cheng-Te Li. 2021.
  FinGAT: Financial graph attention networks for recommending top-kk k profitable stocks.
  *IEEE transactions on knowledge and data engineering* 35, 1 (2021), 469–481.
* Li et al. (2022)

  Anchen Li, Bo Yang, Farookh Khadeer Hussain, and Huan Huo. 2022.
  HSR: Hyperbolic social recommender.
  *Information Sciences* 585 (2022), 275–288.
* Nguyen et al. (2015)

  Thien Hai Nguyen, Kiyoaki Shirai, and Julien Velcin. 2015.
  Sentiment analysis on social media for stock movement prediction.
  *Expert Systems with Applications* 42, 24 (2015), 9603–9611.
* Nti et al. (2021)

  Isaac Kofi Nti, Adebayo Felix Adekoya, and Benjamin Asubam Weyori. 2021.
  A novel multi-source information-fusion predictive framework based on deep neural networks for accuracy enhancement in stock market prediction.
  *Journal of Big data* 8, 1 (2021), 17.
* Omranpour et al. (2024)

  Soroush Omranpour, Guillaume Rabusseau, and Reihaneh Rabbany. 2024.
  Higher Order Transformers: Enhancing Stock Movement Prediction On Multimodal Time-Series Data.
  *arXiv preprint arXiv:2412.10540* (2024).
* Sun and Harit (2025)

  Zhongtian Sun and Anoushka Harit. 2025.
  RicciFlowRec: A Geometric Root Cause Recommender Using Ricci Curvature on Financial Graphs. In *Proceedings of the Nineteenth ACM Conference on Recommender Systems*. 1284–1289.
* Sun et al. (2023a)

  Zhongtian Sun, Anoushka Harit, Alexandra I Cristea, Jingyun Wang, and Pietro Lio. 2023a.
  Money: Ensemble learning for stock price movement prediction via a convolutional network with adversarial hypergraph model.
  *AI Open* 4 (2023), 165–174.
* Sun et al. (2023b)

  Zhongtian Sun, Anoushka Harit, Alexandra I Cristea, Jingyun Wang, and Pietro Lio. 2023b.
  A Rewiring Contrastive Patch PerformerMixer Framework for Graph Representation Learning. In *2023 IEEE International Conference on Big Data (BigData)*. IEEE Computer Society, 5930–5939.
* Sun et al. (2022a)

  Zhongtian Sun, Anoushka Harit, Alexandra I Cristea, Jialin Yu, Noura Al Moubayed, and Lei Shi. 2022a.
  Is unimodal bias always bad for visual question answering? a medical domain study with dynamic attention. In *2022 IEEE International Conference on Big Data (Big Data)*. IEEE, 5352–5360.
* Sun et al. (2022b)

  Zhongtian Sun, Anoushka Harit, Alexandra I Cristea, Jialin Yu, Lei Shi, and Noura Al Moubayed. 2022b.
  Contrastive learning with heterogeneous graph attention networks on short text classification. In *2022 International Joint Conference on Neural Networks (IJCNN)*. IEEE, 1–6.
* Sun et al. (2025a)

  Zhongtian Sun, Anoushka Harit, and Pietro Lio. 2025a.
  Actionable Interpretability via Causal Hypergraphs: Unravelling Batch Size Effects in Deep Learning.
  *arXiv preprint arXiv:2506.17826* (2025).
* Sun et al. (2021)

  Zhongtian Sun, Anoushka Harit, Jialin Yu, Alexandra I Cristea, and Noura Al Moubayed. 2021.
  A generative bayesian graph attention network for semi-supervised classification on scarce data. In *2021 International Joint Conference on Neural Networks (IJCNN)*. IEEE, 1–7.
* Sun et al. (2025b)

  Zhongtian Sun, Anoushka Harit, Jongmin Yu, Jingyun Wang, and Pietro Liò. 2025b.
  Advanced hypergraph mining for web applications using sphere neural networks. In *Companion Proceedings of the ACM on Web Conference 2025*. 1316–1320.
* Sun et al. (2025c)

  Zhongtian Sun, Jingyun Wang, Ahmed Alamri, and Alexandra Cristea. 2025c.
  Spar-gnn: Knowledge tracing with behavioural patterns and selective llm feedback. In *International Conference on Artificial Intelligence in Education*. Springer, 328–335.
* Tetlock (2007)

  Paul C Tetlock. 2007.
  Giving content to investor sentiment: The role of media in the stock market.
  *The Journal of finance* 62, 3 (2007), 1139–1168.
* Tsantekidis et al. (2017)

  Avraam Tsantekidis, Nikolaos Passalis, Anastasios Tefas, Juho Kanniainen, Moncef Gabbouj, and Alexandros Iosifidis. 2017.
  Forecasting stock prices from the limit order book using convolutional neural networks. In *2017 IEEE 19th conference on business informatics (CBI)*, Vol. 1. IEEE, 7–12.
* Vaswani et al. (2017)

  Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017.
  Attention is all you need.
  *Advances in neural information processing systems* 30 (2017).
* Wang et al. (2019)

  Xiang Wang, Xiangnan He, Yixin Cao, Meng Liu, and Tat-Seng Chua. 2019.
  Kgat: Knowledge graph attention network for recommendation. In *Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining*. 950–958.
* Zhang et al. (2022)

  Qiuyue Zhang, Chao Qin, Yunfeng Zhang, Fangxun Bao, Caiming Zhang, and Peide Liu. 2022.
  Transformer-based attention network for stock movement prediction.
  *Expert Systems with Applications* 202 (2022), 117239.
* Zhao et al. (2024)

  Zijuan Zhao, Kai Yang, and Jinli Guo. 2024.
  Heterogeneous hypergraph representation learning for link prediction.
  *The European Physical Journal B* 97, 10 (2024), 153.
* Zheng et al. (2022)

  Xin Zheng, Yi Wang, Yixin Liu, Ming Li, Miao Zhang, Di Jin, Philip S Yu, and Shirui Pan. 2022.
  Graph neural networks for graphs with heterophily: A survey.
  *arXiv preprint arXiv:2202.07082* (2022).