---
authors:
- Baris Arat
- Hasan Fehmi Ates
- Emre Sefer
doc_id: arxiv:2602.18572v1
family_id: arxiv:2602.18572
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite
  Radar and News Sentiment
url_abs: http://arxiv.org/abs/2602.18572v1
url_html: https://arxiv.org/html/2602.18572v1
venue: arXiv q-fin
version: 1
year: 2026
---


Baris Arat
Ozyegin University, Istanbul, Turkey
  
baris.arat@ozu.edu.tr, hasan.ates@ozyegin.edu.tr, emre.sefer@ozyegin.edu.tr

Hasan Fehmi Ates
Ozyegin University, Istanbul, Turkey
  
baris.arat@ozu.edu.tr, hasan.ates@ozyegin.edu.tr, emre.sefer@ozyegin.edu.tr

Emre Sefer
Corresponding author.
Ozyegin University, Istanbul, Turkey
  
baris.arat@ozu.edu.tr, hasan.ates@ozyegin.edu.tr, emre.sefer@ozyegin.edu.tr

###### Abstract

Reliable real estate price indicators are typically published at city level and low frequency, limiting their use for neighborhood-scale monitoring and long-horizon planning. We study whether sub-city price indices can be forecasted at weekly frequency by combining physical development signals from satellite radar with market narratives from news text. Using over 350,000 transactions from Dubai Land Department (2015–2025), we construct weekly price indices for 19 sub-city regions and evaluate forecasts from 2 to 34 weeks ahead. Our framework fuses regional transaction history with Sentinel-1 SAR backscatter, news sentiment combining lexical tone and semantic embeddings, and macroeconomic context. Results are strongly horizon dependent: at horizons up to 10 weeks, price history alone matches multimodal configurations, but beyond 14 weeks sentiment and SAR become critical. At long horizons (26–34 weeks), the full multimodal model reduces mean absolute error from 4.48 to 2.93 (35% reduction), with gains statistically significant across regions. Nonparametric learners consistently outperform deep architectures in this data regime. These findings establish benchmarks for weekly sub-city index forecasting and demonstrate that remote sensing and news sentiment materially improve predictability at strategically relevant horizons.

Preprint. Under review.

Keywords: time series forecasting, multimodal learning, urban analytics, remote sensing, sentiment analysis

## 1 Introduction

Real estate markets are fundamental to economic stability and investment allocation, yet the price indices used to monitor them persistently suffer from temporal and spatial aggregation. Most widely used indices are published monthly or quarterly at national to city level [[38](https://arxiv.org/html/2602.18572v1#bib.bib8 "Construction of property price indices: temporal aggregation and accuracy of various index methods"), [39](https://arxiv.org/html/2602.18572v1#bib.bib7 "Construction and application of property price indices")]. This restricts their utility for neighborhood-scale monitoring, timely risk assessment, and long-horizon urban planning. The forecasting literature has developed largely under these constraints. Much of the work relies on univariate time-series baselines or parametric multivariate econometric models that incorporate macroeconomic fundamentals, while more recent work increasingly explores machine learning approaches [[42](https://arxiv.org/html/2602.18572v1#bib.bib15 "Forecasting the U.S. real house price index"), [30](https://arxiv.org/html/2602.18572v1#bib.bib27 "Evaluating Alternative Methods of Forecasting House Prices: A Post-Crisis Reassessment"), [32](https://arxiv.org/html/2602.18572v1#bib.bib21 "The Importance of Economic Variables on London Real Estate Market: A Random Forest Approach")].

Meanwhile, studies on property appraisal that integrate street imagery, satellite views, and textual descriptions outperform transaction-only baselines for individual property valuation [[26](https://arxiv.org/html/2602.18572v1#bib.bib14 "Multimodal Machine Learning for Real Estate Appraisal: A Comprehensive Survey"), [47](https://arxiv.org/html/2602.18572v1#bib.bib17 "AI-based on machine learning methods for urban real estate prediction: a systematic survey")]. These findings suggest that physical and textual signals encode information not present in transaction records alone. Yet this multimodal paradigm has not transferred to index-level forecasting as much, where the prediction target is an aggregate time series rather than individual property values. This gap motivates our central question: can urban development patterns (observable from satellite imagery), combined with shifts in market sentiment (detectable in news text), improve long-horizon forecasting of sub-city price indices?

There is a strong conceptual basis for this hypothesis. Construction activity and infrastructure development alter the physical landscape before completed projects appear in transaction records, while news coverage of regulatory changes and market sentiment may signal shifts before they materialize in prices. Both sources therefore act as potential leading indicators. However, testing this hypothesis faces a data constraint. Satellite imagery with consistent global coverage from the Copernicus Sentinel missions extends back only to 2014. Combined with the low frequency of published indices, this leaves insufficient observations for robust multimodal evaluation.

We address this constraint by constructing weekly sub-city indices from granular transaction records. The Dubai Land Department (DLD) provides individual transaction data with date, location, and price since 2004 [[16](https://arxiv.org/html/2602.18572v1#bib.bib58 "Dubai land department open data: real estate data")]. This underlying transaction data retain sufficient granularity to support re-aggregation at finer temporal and spatial resolutions than published indices. We focus on 2015–2025 to align with Sentinel-1 availability and construct weekly price indices for 19 sub-city regions defined by master project boundaries. The resulting dataset contains approximately 500 weekly observations per region derived from over 350,000 transactions. As an exploratory analysis, Figure [1](https://arxiv.org/html/2602.18572v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") illustrates clearly visible divergence from the citywide aggregate.

![Refer to caption](figures/indexed_prices_all_regions_global.png)


Figure 1: Weekly price indices for 19 Dubai sub-city regions (2015–2025, rebased to 100). Regional trajectories diverge substantially from the citywide aggregate (bold).

This experimental design offers both methodological and practical value. Methodologically, the combination of regions, weekly frequency, and decade-long coverage provides sufficient variation to evaluate multimodal contributions through systematic ablation while avoiding overfitting to a single aggregate series. Practically, sub-city weekly indices address a genuine information gap in regional dynamics which is relevant to developers, investors, and urban planners.

Our framework integrates four signal types: regional transaction history (prices and volumes), city-level news sentiment derived from GDELT, region-level Sentinel-1 synthetic aperture radar (SAR) backscatter, and macroeconomic context via interbank interest rates. For the textual modality, we combine lexical tone scores with semantic embeddings to capture topical structure beyond simple positive-negative polarity. For the spatial modaility, we prioritize Sentinel-1 SAR because, unlike optical imagery, radar supports consistent observation of built-up areas and highlights the structural and geometric changes associated with urban development [[46](https://arxiv.org/html/2602.18572v1#bib.bib40 "Mapping and Monitoring Urban Environment through Sentinel-1 SAR Data: A Case Study in the Veneto Region (Italy)")]. Despite their widespread use in urban monitoring, such remote sensing signals have rarely been integrated into real estate price forecasting models. All data sources in this setting are publicly accessible so that this pipeline is applicable to other markets with similar transaction transparency, or partially applicable through globally available news sentiment and satellite imagery.

We evaluate forecasts across nine horizons from 2 to 34 weeks using rolling time-series cross-validation and benchmark multiple model families through systematic ablations. The results reveal a horizon-dependent modality contribution. At short horizons up to 10 weeks, transaction history alone performs comparably to multimodal configurations where autoregressive patterns dominate. Beyond 14 weeks, however, price-based models decay while multimodal configurations maintain accuracy. At long horizons, the full multimodal specification reduces mean absolute error by 35% relative to price-only baselines, with improvements statistically significant across regions. Nonparametric learners such as K-nearest neighbors and random forest consistently outperform both linear models and recurrent neural networks in this data regime, likely because local similarity-based retrieval adapts naturally to regime shifts without requiring sufficient examples of each regime for parametric estimation.

These findings make four contributions:

* •

  We propose a multimodal framework for sub-city index forecasting that integrates transaction data with remote sensing, news sentiment, and macroeconomic indicators under a modular architecture that enables systematic ablation analysis.
* •

  We establish empirical benchmarks for weekly long-horizon prediction using indices constructed from over 350,000 transactions across 19 Dubai regions, with evaluation across nine forecast horizons and multiple model families.
* •

  We quantify modality contributions through ablation experiments. We identify the horizons at which sentiment and SAR improve forecasts and measure the magnitude of improvement.
* •

  We provide methodological findings on feature design: semantic embeddings outperform lexical sentiment, SAR outperforms optical indices, and nonparametric learners outperform deep architectures in this regime.

## 2 Related Work

Real estate forecasting has evolved from univariate autoregressive methods toward models that incorporate exogenous predictors, though sub-city prediction remains underexplored. Early work established that aggregate house price indices can be forecast with meaningful accuracy over extended horizons using historical prices with macroeconomic predictors. Plakandaras et al. [[42](https://arxiv.org/html/2602.18572v1#bib.bib15 "Forecasting the U.S. real house price index")] apply ensemble empirical mode decomposition with support vector regression to the U.S. real house price index. Subsequent studies demonstrate that macroeconomic augmentation improves accuracy under specific conditions. Larson [[30](https://arxiv.org/html/2602.18572v1#bib.bib27 "Evaluating Alternative Methods of Forecasting House Prices: A Post-Crisis Reassessment")] shows that error-correction models that incorporate income and rent outperform univariate specifications for California housing, particularly during the 2006 downturn when fundamental imbalances preceded price corrections. Levantesi and Piscopo [[32](https://arxiv.org/html/2602.18572v1#bib.bib21 "The Importance of Economic Variables on London Real Estate Market: A Random Forest Approach")] find that population dynamics dominate in demand-driven markets such as London. Studies on the Dubai market have employed classical time-series methods at city level. ARIMA models applied to monthly indices [[23](https://arxiv.org/html/2602.18572v1#bib.bib23 "Forecasting future trends in Dubai housing market by using Box‐Jenkins autoregressive integrated moving average")] and cointegration analyses that link prices to gold and macroeconomic variables [[24](https://arxiv.org/html/2602.18572v1#bib.bib22 "Relationship between residential property price index and macroeconomic indicators in dubai housing market")] establish baseline relationships but do not address sub-city dynamics. Recent work confirms that U.S. interest rate changes propagate to Dubai housing market activity [[43](https://arxiv.org/html/2602.18572v1#bib.bib24 "The US monetary conditions and Dubai’s real estate market: twist or tango?")]. On the other hand, few studies attempt sub-city forecasting. Ge et al. [[18](https://arxiv.org/html/2602.18572v1#bib.bib20 "An Integrated Model for Urban Subregion House Price Forecasting: A Multi-source Data Perspective")] forecast monthly prices across subregion grids in New York and Beijing and find substantial cross-regional variation. Their results suggest that neighborhood-level dynamics contain information lost in city-level aggregation. This observation aligns with index construction literature that shows regional indices diverge systematically from citywide aggregates [[6](https://arxiv.org/html/2602.18572v1#bib.bib26 "Missing the Mark: House Price Index Accuracy and Mortgage Credit Modeling")].

Multimodal learning has been explored in both property appraisal and index-style forecasting, but the two settings differ in data availability and modality richness. Broader surveys of ML in real estate confirm that most studies still rely on structured tabular data from institutional sources, with few incorporating visual or textual modalities [[47](https://arxiv.org/html/2602.18572v1#bib.bib17 "AI-based on machine learning methods for urban real estate prediction: a systematic survey")]. In property appraisal, recent work has explored incorporating descriptive text, interior imagery [[22](https://arxiv.org/html/2602.18572v1#bib.bib11 "A Multi-Modal Deep Learning Based Approach for House Price Prediction")] and neighborhood-level visual context using satellite imagery [[29](https://arxiv.org/html/2602.18572v1#bib.bib13 "A Comparison of Multi-View Learning Strategies for Satellite Image-Based Real Estate Appraisal")], while an appraisal survey confirms added modalities improve accuracy across studies [[26](https://arxiv.org/html/2602.18572v1#bib.bib14 "Multimodal Machine Learning for Real Estate Appraisal: A Comprehensive Survey")]. On the index-style forecasting side, Wang [[52](https://arxiv.org/html/2602.18572v1#bib.bib12 "HouseTS: A Large-Scale, Multimodal Spatiotemporal U.S. Housing Dataset")] addresses house price index forecasting at the ZIP-code level using aggregated regional price series. The study incorporates satellite imagery and applies large language models to generate textual descriptions of visual change, and reports mixed gains on predictive accuracy. Jiang et al. [[28](https://arxiv.org/html/2602.18572v1#bib.bib18 "Modeling Real Estate Dynamics Using Temporal Encoding")] use a transformer encoder to represent neighborhood-level price history and combine it with Census features to predict multiclass hotspot tiers based on future price appreciation. Together, these studies show that additional signals beyond transaction records can be useful, although their value varies with the prediction target and aggregation level, consistent with the task-dependent nature of modality relevance in multimodal learning [[34](https://arxiv.org/html/2602.18572v1#bib.bib19 "Foundations & Trends in Multimodal Machine Learning: Principles, Challenges, and Open Questions")].

Sentiment signals for real estate prediction can be derived from surveys or automated text analysis. Cheung et al. [[13](https://arxiv.org/html/2602.18572v1#bib.bib9 "The effect of sentiment on commercial real estate returns: investor and occupier perspectives")] construct investor and occupier sentiment indices from commercial property surveys and demonstrate predictive value for Australian property returns, with investor confidence particularly informative. Survey-based approaches offer reliability but are limited to low frequency and narrow geographic coverage. Recent work extracts sentiment directly from news. Xu [[54](https://arxiv.org/html/2602.18572v1#bib.bib16 "A Real Estate Price Index Forecasting Scheme Based on Online News Sentiment Analysis")] generates city-level sentiment indices using BERT-based classification of Chinese real estate news and shows that sentiment improves monthly vector autoregression forecasts, though effect sizes vary across cities and sources. Chen et al. [[11](https://arxiv.org/html/2602.18572v1#bib.bib25 "Research on sentiment index and real estate demand forecasting based on BERT-BiLSTM and ADL-MIDAS models")] study high-frequency real estate sentiment from Chinese Weibo using a BERT-BiLSTM classifier and evaluate its predictive value with an ADL-MIDAS framework. These studies suggest that automated text sentiment can provide predictive information beyond price history, although the gains depend on the text source, the target variable, and the sampling frequency. However, current sentiment representations have limitations. Most approaches rely on lexicon-based polarity scores or domain-specific transformer sentiment models adapted to financial text [[2](https://arxiv.org/html/2602.18572v1#bib.bib34 "FinBERT: Financial Sentiment Analysis with Pre-trained Language Models")]. Such methods may miss real estate specific semantic structure. Discussions of construction delays, regulatory changes, or infrastructure investments may carry predictive content that positive-negative classification cannot capture. Additionally, applications remain at monthly frequency.

Remote sensing provides direct observation of physical urban development. Sentinel-1 synthetic aperture radar offers consistent monitoring of built-up areas through strong backscatter responses that are robust to cloud cover and illumination constraints [[48](https://arxiv.org/html/2602.18572v1#bib.bib47 "GMES Sentinel-1 mission"), [46](https://arxiv.org/html/2602.18572v1#bib.bib40 "Mapping and Monitoring Urban Environment through Sentinel-1 SAR Data: A Case Study in the Veneto Region (Italy)"), [50](https://arxiv.org/html/2602.18572v1#bib.bib41 "Built-up area mapping using Sentinel-1 SAR data")]. Time-series analyses show that Sentinel-1 captures meaningful urban structural change through built-up expansion and change detection [[36](https://arxiv.org/html/2602.18572v1#bib.bib43 "Spatio-temporal change detection of built-up areas with sentinel-1 sar data using random forest classification for arnavutköy istanbul")]. Recent work also suggests that SAR contributes structural and geometric cues for built-up mapping that are not fully captured by optical spectral bands alone [[33](https://arxiv.org/html/2602.18572v1#bib.bib42 "Extraction of Built-Up Areas Using Sentinel-1 and Sentinel-2 Data with Automated Training Data Sampling and Label Noise Robust Cross-Fusion Neural Networks")]. These properties allow SAR to reflect construction activity and land transformation before completed structures appear in transaction records. Despite this potential, to our knowledge, SAR has seen limited adoption in real estate price forecasting.

An earlier conference version of this work explored short-horizon real estate forecasting using multi-context data and neural network models [[3](https://arxiv.org/html/2602.18572v1#bib.bib3 "Multi-context real estate market prediction")].

## 3 Methods

This section describes the forecasting framework and the feature set. As a reference, Figure [2](https://arxiv.org/html/2602.18572v1#S3.F2 "Figure 2 ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") summarizes the experiment pipeline and Table [1](https://arxiv.org/html/2602.18572v1#S3.T1 "Table 1 ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") defines modalities and tags. We construct a weekly panel of six feature sets: prices (PP) and transaction counts (CC) from DLD open data, news sentiment (SS) from curated outlets based on GDELT, Sentinel-1 SAR backscatter (BB) from Copernicus, interbank rates (II) from CBUAE, and citywide aggregates (GG) derived from regional series. All series are aligned to Sunday-ending weekly calendar. Experiments take modular combinations of feature blocks through an additive tag system summarized in Table [1](https://arxiv.org/html/2602.18572v1#S3.T1 "Table 1 ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"). For any weekly series xr,tx\_{r,t}, we define a causal lag block of length LL as:

|  |  |  |
| --- | --- | --- |
|  | 𝐱r,t(L)=(xr,t−1,…,xr,t−L)⊤.\mathbf{x}\_{r,t}^{(L)}=\bigl(x\_{r,t-1},\ldots,x\_{r,t-L}\bigr)^{\top}. |  |

Transaction history enters via 12-lag blocks:

|  |  |  |
| --- | --- | --- |
|  | 𝐏r,t=(Pr,t−1,…,Pr,t−12)⊤∈ℝ12,𝐂r,t=(Cr,t−1,…,Cr,t−12)⊤∈ℝ12,\mathbf{P}\_{r,t}=(P\_{r,t-1},\ldots,P\_{r,t-12})^{\top}\in\mathbb{R}^{12},\quad\mathbf{C}\_{r,t}=(C\_{r,t-1},\ldots,C\_{r,t-12})^{\top}\in\mathbb{R}^{12}, |  |

while interbank rates enter via 𝐈t=(It−1,…,It−12)⊤∈ℝ12\mathbf{I}\_{t}=(I\_{t-1},\ldots,I\_{t-12})^{\top}\in\mathbb{R}^{12}. We append a citywide market context block:

|  |  |  |
| --- | --- | --- |
|  | 𝐆t=(Pt−1G,…,Pt−12G,Ct−1G,…,Ct−12G)⊤∈ℝ24.\mathbf{G}\_{t}=\bigl(P^{G}\_{t-1},\ldots,P^{G}\_{t-12},\,C^{G}\_{t-1},\ldots,C^{G}\_{t-12}\bigr)^{\top}\in\mathbb{R}^{24}. |  |

News sentiment features St∈ℝ15S\_{t}\in\mathbb{R}^{15} and SAR features 𝐁r,t∈ℝ15\mathbf{B}\_{r,t}\in\mathbb{R}^{15} are constructed in Sections [3.1.2](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS2 "3.1.2 News-Based Sentiment ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") and [3.1.3](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS3 "3.1.3 Satellite SAR Features ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"). All features are constructed from information available up to the end of week tt. Since the minimum horizon is h=2h=2, week-tt summaries do not leak future targets. Rolling statistics use trailing windows and winsorization thresholds are shifted by one period to exclude the current observation. At decision time tt and region rr, the feature vector for a given modality tag M⊆{P,C,S,B,I,G}M\subseteq\{P,C,S,B,I,G\} is

|  |  |  |
| --- | --- | --- |
|  | 𝐗r,t(M)=[𝐏r,t​|𝐂r,t|​St​|𝐁r,t|​𝐈t|𝐆t],\mathbf{X}\_{r,t}^{(M)}=\bigl[\,\mathbf{P}\_{r,t}\;\big|\;\mathbf{C}\_{r,t}\;\big|\;S\_{t}\;\big|\;\mathbf{B}\_{r,t}\;\big|\;\mathbf{I}\_{t}\;\big|\;\mathbf{G}\_{t}\,\bigr], |  |

with blocks omitted when their modality is not in MM. The features are horizon-invariant, while the prediction target varies with the forecast horizon: yr,t(h)=Pr,t+hy\_{r,t}^{(h)}=P\_{r,t+h}. We evaluate nine forward horizons, ℋ={2, 6, 10, 14, 18, 22, 26, 30, 34}\mathcal{H}=\{2,\,6,\,10,\,14,\,18,\,22,\,26,\,30,\,34\} consisting of short, medium, and long-term forecasts.

![Refer to caption](figures/method-diagram.png)


Figure 2: Overview of the multimodal forecasting framework integrating transaction data, news sentiment, SAR imagery, and interest rates for sub-city price index prediction.




Table 1: Additive modality tags and included feature blocks.

| Tag | Included modalities (feature blocks) |
| --- | --- |
| P | Prices (1212 lags) |
| PC | Prices (1212) + Counts (1212) |
| PCS | Prices (1212) + Counts (1212) + Sentiment (1515) |
| PCSB | Prices (1212) + Counts (1212) + Sentiment (1515) + SAR (1515) |
| PCSBI | Prices (1212) + Counts (1212) + Sentiment (1515) + SAR (1515) + Interest Rates (1212) |
| PCSBIG | Prices (1212) + Counts (1212) + Sentiment (1515) + SAR (1515) + Interest Rates (1212) + Global context (12+1212{+}12) |

### 3.1 Datasets and Feature Constructions

#### 3.1.1 Price Index and Volumes

Regarding index construction methodology, median-based indices are simple and transparent, while repeat-sales and hedonic approaches aim to control for quality and compositional change but require stronger data support [[24](https://arxiv.org/html/2602.18572v1#bib.bib22 "Relationship between residential property price index and macroeconomic indicators in dubai housing market")]. We adopt the median approach because our sub-city regions lack the attribute consistency required for hedonic estimation at weekly frequency.

The weekly regional price index Pr,tP\_{r,t} is derived from DLD transaction records containing transaction date, area, size, and Master Project based location labels. We focus on the 2015–2025 period and collect 19 Master Projects with consistent transaction history and spatial boundaries. We also construct a citywide “Global” aggregate by pooling all selected projects and use it only as a global context feature block rather than as an additional forecasting target. Project polygons were derived from public boundary definitions and manually checked for consistency with published district maps. Figure [3](https://arxiv.org/html/2602.18572v1#S3.F3 "Figure 3 ‣ 3.1.1 Price Index and Volumes ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") shows the spatial distribution of selected regions. Filtering the raw data for the study window and selected projects yields over 350,000 transactions after standard outlier handling. For each region, index construction proceeds as follows. Per-m2m^{2} transaction prices are first trimmed using fixed percentile cutoffs. A rolling median over the most recent 200 transactions is computed, the last value of each day is selected, and daily values are aggregated to weekly medians. The resulting series is aligned to a complete weekly grid and smoothed through forward filling of rare missing weeks, a trailing 4-week mean, winsorization of weekly changes exceeding ±3×\pm 3\times the 52-week rolling MAD. The final series is rebased to 100 at the first week. The Global series pools all selected projects and follows the same construction steps, using a larger rolling window of 600 transactions and winsorizing weekly changes at ±2​σ\pm 2\sigma, where σ\sigma is computed from a trailing 52-week window of weekly changes. The implications of alternative smoothing choices are examined separately through robustness diagnostics.

![Refer to caption](figures/dubai_regions_map_final.png)


Figure 3: Spatial distribution of selected Master Projects in Dubai.

##### Quantile trimming and robustness.

Weekly sub-city indices constructed from transaction records are sensitive to heterogeneous unit mixes and occasional extreme transactions, particularly in regions with limited weekly volume. To obtain stable and comparable monitoring signals across regions, we apply percentile-based trimming to per-m2m^{2} prices prior to aggregation, using fixed cutoffs estimated from the initial training window and applied uniformly thereafter. Figure [4](https://arxiv.org/html/2602.18572v1#S3.F4 "Figure 4 ‣ Quantile trimming and robustness. ‣ 3.1.1 Price Index and Volumes ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") summarizes robustness diagnostics under two trimming schemes. At the citywide level (left), relaxed trimming ([5th, 95th]) aligns more closely with the UAE residential property price index from FRED (BIS) [[4](https://arxiv.org/html/2602.18572v1#bib.bib56 "Residential property prices for the united arab emirates")], while aggressive trimming ([25th, 85th]) yields a smoother long cycle. At the regional level (right), relaxed trimming induces higher volatility and deeper drawdowns, whereas aggressive trimming produces a smoother signal that follows a similar trajectory. Since our objective is cross-region stabilization and reliable weekly monitoring rather than appraisal-grade valuation, we adopt the [25th, 85th] trimming in the main analysis.

![Refer to caption](figures/quantile_trimming_global.png)


(a) Citywide diagnostic: transaction-derived indices under alternative trimming compared to the macro benchmark.

![Refer to caption](figures/regional_index_robustness_dubai_marina.png)


(b) Regional diagnostic: a representative region illustrating stability differences under alternative indexing.

Figure 4: Quantile trimming diagnostics for transaction-based index construction. Relaxed trimming ([5th, 95th]) improves citywide cycle fidelity relative to a macro benchmark, while more aggressive trimming ([25th, 85th]) yields a smoother regional monitoring signal with reduced sensitivity to idiosyncratic transactions.

#### 3.1.2 News-Based Sentiment

We construct weekly city-level sentiment features from economic and real estate related news using a pipeline that combines source selection, domain filtering, and applies lexical tone and semantic embedding representation. We query GDELT GKG records [[31](https://arxiv.org/html/2602.18572v1#bib.bib59 "GDELT: global data on events, language, and tone, 1979–2012")] from 2015 to 2025 for articles tagged with the housing theme. Source filtering restricts the corpus to English language outlets from a curated whitelist of 80 international and regional sources, including Gulf business press (e.g., Gulf News, Khaleej Times, Arabian Business), major wire services (Reuters, AP), and established financial media (Bloomberg, CNBC, WSJ). We retrieve full article text using Trafilatura [[5](https://arxiv.org/html/2602.18572v1#bib.bib57 "Trafilatura: A web scraping library and command-line tool for text discovery and extraction")], yielding approximately 27,000 articles with content. To ensure economic and real estate relevance, we apply keyword filtering using a comprehensive lexicon including macroeconomic terms (e.g., “inflation,” “interest rate,” “monetary policy,” “GDP”), real estate terms (e.g., “housing market,” “mortgage,” “construction,” “developer,” “vacancy”), and numerical markers. Articles lacking any lexicon match are excluded. For each retained article, we compute a Numerical Sentiment Index (NSI) from GDELT tone fields.

|  |  |  |
| --- | --- | --- |
|  | NSIi=positive​\_​scorei−negative​\_​scoreipositive​\_​scorei+negative​\_​scorei,\mathrm{NSI}\_{i}=\frac{\mathrm{positive\\_score}\_{i}-\mathrm{negative\\_score}\_{i}}{\mathrm{positive\\_score}\_{i}+\mathrm{negative\\_score}\_{i}}, |  |

Weekly NSI is computed as the median of article-level values within each week and smoothed using a 4-week rolling mean to reduce high-frequency noise.

We construct a 7-dimensional tone feature vector sttone=(NSIt,Δ​NSIt,volt,MAt,EMAt,NSIt−1,NSIt−4)∈ℝ7s^{\text{tone}}\_{t}=\bigl(\mathrm{NSI}\_{t},\;\Delta\mathrm{NSI}\_{t},\;\mathrm{vol}\_{t},\;\mathrm{MA}\_{t},\;\mathrm{EMA}\_{t},\;\mathrm{NSI}\_{t-1},\;\mathrm{NSI}\_{t-4}\bigr)\in\mathbb{R}^{7}, where Δ​NSIt\Delta\mathrm{NSI}\_{t} is the weekly change, volt\mathrm{vol}\_{t} is the 4-week rolling standard deviation, and MAt\mathrm{MA}\_{t} and EMAt\mathrm{EMA}\_{t} denote 4-week simple and exponential moving averages. To capture topical structure beyond lexical polarity, we encode article text using Sentence-BERT embeddings [[44](https://arxiv.org/html/2602.18572v1#bib.bib4 "Sentence-BERT: sentence embeddings using siamese BERT-networks")] with a MiniLM implementation [[53](https://arxiv.org/html/2602.18572v1#bib.bib61 "MiniLM: deep self-attention distillation for task-agnostic compression of pre-trained transformers")]. Weekly embeddings are computed as the mean of article embeddings within each week, then reduced via PCA to 8 components. To avoid representation leakage, PCA is fit once using weekly embeddings from the initial training window of the rolling cross-validation procedure, and the learned projection is applied to all weeks without refitting. Component count is kept limited to prevent overfitting given the limited time series depth. Each component is exponentially smoothed (α=0.3\alpha=0.3) to reduce week-to-week noise, and we denote the resulting vector by 𝐩𝐜𝐚t=(PCt,1,…,PCt,8)∈ℝ8\mathbf{pca}\_{t}=(\mathrm{PC}\_{t,1},\ldots,\mathrm{PC}\_{t,8})\in\mathbb{R}^{8}. The final weekly sentiment block concatenates lexical and semantic features as St=[sttone∣𝐩𝐜𝐚t]∈ℝ15S\_{t}=\bigl[\,s^{\text{tone}}\_{t}\mid\mathbf{pca}\_{t}\,\bigr]\in\mathbb{R}^{15}. Figure [5](https://arxiv.org/html/2602.18572v1#S3.F5 "Figure 5 ‣ 3.1.2 News-Based Sentiment ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") shows the weekly NSI series alongside the correlation structure between lexical and semantic features. The NSI captures major market shifts, including sharp negative sentiment during early 2020 and following recovery. Lexical and semantic features exhibit low cross-correlation which suggests that components capture distinct narrative structure beyond aggregate tone.

![Refer to caption](figures/nsi_trend_plot.png)


(a) Weekly NSI, rolling mean. 13-week mean is for visualization only.

![Refer to caption](figures/nsi_feature_heatmap.png)


(b) Lexical-semantic feature correlations.

Figure 5: Sentiment feature diagnostics. (a) Weekly NSI captures market sentiment shifts including the COVID-19 period. (b) Low correlation between lexical NSI features and semantic PCA components confirms complementary information.

#### 3.1.3 Satellite SAR Features

We use Sentinel-1 C-band SAR [[48](https://arxiv.org/html/2602.18572v1#bib.bib47 "GMES Sentinel-1 mission")] because it captures meaningful urban structural change through consistent observations independent of cloud cover and illumination, which is critical for weekly monitoring [[46](https://arxiv.org/html/2602.18572v1#bib.bib40 "Mapping and Monitoring Urban Environment through Sentinel-1 SAR Data: A Case Study in the Veneto Region (Italy)"), [50](https://arxiv.org/html/2602.18572v1#bib.bib41 "Built-up area mapping using Sentinel-1 SAR data"), [20](https://arxiv.org/html/2602.18572v1#bib.bib48 "Sentinel-1 and Sentinel-2 Data Fusion for Urban Change Detection Using a Dual Stream U-Net"), [36](https://arxiv.org/html/2602.18572v1#bib.bib43 "Spatio-temporal change detection of built-up areas with sentinel-1 sar data using random forest classification for arnavutköy istanbul")]. Sentinel-1 GRD scenes (VV, VH) for 2015–2025 are retrieved via Google Earth Engine [[19](https://arxiv.org/html/2602.18572v1#bib.bib49 "Google Earth Engine: Planetary-scale geospatial analysis for everyone")], which provides calibrated, terrain-corrected backscatter in decibels. The resulting regional time series are resampled to a weekly grid and smoothed with a trailing 4-week mean to mitigate noise. Rare missing weeks in the base SAR series are addressed using forward filling only, and lagged SAR features are constructed strictly causally from past observations. To capture structural changes at multiple temporal scales, we augment the SAR statistics with lagged values at 4, 8, 12, and 20 weeks. These lags are chosen to span from short to medium-term development dynamics while ensuring full feature availability over the aligned study window. Let 𝐛r,t(ℓ)∈ℝ3\mathbf{b}\_{r,t}^{(\ell)}\in\mathbb{R}^{3} denote the smoothed VV, VH, and VV/VH ratio at offset t−ℓt-\ell. The SAR feature vector for region rr at week tt is 𝐁r,t=(𝐛r,t(0),𝐛r,t(4),𝐛r,t(8),𝐛r,t(12),𝐛r,t(20))∈ℝ15\mathbf{B}\_{r,t}=\bigl(\mathbf{b}\_{r,t}^{(0)},\,\mathbf{b}\_{r,t}^{(4)},\,\mathbf{b}\_{r,t}^{(8)},\,\mathbf{b}\_{r,t}^{(12)},\,\mathbf{b}\_{r,t}^{(20)}\bigr)\in\mathbb{R}^{15}.

#### 3.1.4 Interest Rates

EIBOR interbank rates (CBUAE) [[9](https://arxiv.org/html/2602.18572v1#bib.bib60 "EIBOR rates")] are aggregated to weekly frequency and included via a 12-lag block 𝐈t=(It−1,…,It−12)\mathbf{I}\_{t}=(I\_{t-1},\ldots,I\_{t-12}) to capture delayed monetary policy effects on housing markets [[10](https://arxiv.org/html/2602.18572v1#bib.bib6 "Experimental research on the impact of interest rate on real estate market transactions"), [51](https://arxiv.org/html/2602.18572v1#bib.bib5 "Interest rates and real estate prices: a panel study")].

### 3.2 Forecasting Framework

The forecasting task is to estimate the regional price index yr,t(h)=Pr,t+hy^{(h)}\_{r,t}=P\_{r,t+h} at horizon hh weeks ahead using multimodal explanatory inputs 𝐗r,t(M)\mathbf{X}\_{r,t}^{(M)}, where MM denotes a selected subset of modalities. Rolling time-series cross-validation is applied over 2015–2025 using 5-year training and 6-month validation windows advanced in 6-month steps. This procedure yields ten folds for all horizons except the longest h=34h{=}34 weeks, for which nine folds are available because target observations end earlier. For each forecast horizon h∈ℋh\in\mathcal{H}, region rr, and model ff, we fit a separate predictor fh,r(M)f\_{h,r}^{(M)} using features 𝐗r,t(M)\mathbf{X}\_{r,t}^{(M)} and target yr,t(h)=Pr,t+hy^{(h)}\_{r,t}=P\_{r,t+h}. Performance is evaluated using mean absolute error (MAE) on each validation window and reported as a macro-average across regions and folds:

|  |  |  |
| --- | --- | --- |
|  | MAEmacro​(h,f,M)=1R​Kh​∑r=1R∑k=1KhMAEr,k​(h,f,M),\text{MAE}\_{\text{macro}}(h,f,M)=\frac{1}{R\,K\_{h}}\sum\_{r=1}^{R}\sum\_{k=1}^{K\_{h}}\text{MAE}\_{r,k}(h,f,M), |  |

where R=19R=19 and KhK\_{h} is the number of admissible CV folds for horizon hh. We report MAE​(h)\text{MAE}(h) curves across horizons and fold-level standard deviations to assess robustness.

#### 3.2.1 Model Families

Baselines.
We include two univariate reference baselines operating on prices only.
The Naive-12Mean baseline forecasts region rr at horizon hh as the 12-week rolling mean of past prices:

|  |  |  |
| --- | --- | --- |
|  | y^r,t,Naive(h)=112​∑i=112Pr,t−i.\hat{y}^{(h)}\_{r,t,\text{Naive}}=\frac{1}{12}\sum\_{i=1}^{12}P\_{r,t-i}. |  |

As a classical parametric reference, we fit a non-seasonal ARIMA [[7](https://arxiv.org/html/2602.18572v1#bib.bib55 "Time series analysis: forecasting and control")] model on the price-only series (P). For each region and fold, the ARIMA order (p,d,q)(p,d,q) is selected on the fold’s training window by minimizing AIC over a bounded grid (p∈{0,…,3}p\in\{0,\ldots,3\}, d∈{0,1}d\in\{0,1\}, q∈{0,…,3}q\in\{0,\ldots,3\}). The ARIMA pipeline considers only converged fits with stationarity and invertibility enforced. Validation follows a rolling-origin protocol: for each decision week in the validation window, we refit ARIMA on all observations available up to that week using the selected order, then forecast forward and score the prediction at horizon hh.

Learning models.
Beyond univariate baselines, we benchmark five learning model families of increasing flexibility. Ridge regression is fit with an L2L\_{2} penalty. Random Forest [[8](https://arxiv.org/html/2602.18572v1#bib.bib44 "Random forests")] models use 300 trees with maximum depth 5 and minimum leaf size 1. XGBoost [[12](https://arxiv.org/html/2602.18572v1#bib.bib53 "XGBoost: a scalable tree boosting system")] is implemented as a gradient-boosted tree ensemble trained on the same flat feature representation. A single fixed configuration is used across all regions, horizons, folds, and modality tags, with 600 trees, maximum depth 4, learning rate 0.05, subsample ratio 0.9, column subsample ratio 0.9, and L2L\_{2} regularization λ=1.0\lambda=1.0. K-Nearest Neighbors [[14](https://arxiv.org/html/2602.18572v1#bib.bib45 "Nearest neighbor pattern classification")] regression uses k=7k=7 with Manhattan distance on standardized feature. The LSTM [[25](https://arxiv.org/html/2602.18572v1#bib.bib46 "Long short-term memory")] operates on 12-step input windows aligned with the lag-based feature design and consists of three bidirectional LSTM layers with hidden size 32 and layer normalization, followed by two fully connected layers and a linear output head. Optimization is performed using AdamW [[35](https://arxiv.org/html/2602.18572v1#bib.bib62 "Decoupled weight decay regularization")].

#### 3.2.2 Statistical Testing

We assess the statistical significance of performance differences using nonparametric tests. All tests are conducted at h≥26h\geq 26 horizons, where multimodal effects are most pronounced. For each region and modality configuration, MAE is first averaged across the long-horizon set to obtain a single summary error per region. These region-level summaries constitute the paired samples used for statistical testing. First, within each model family, we apply the Friedman test to evaluate whether MAE differs across the six modality configurations (P, PC, PCS, PCSB, PCSBI, PCSBIG). If the Friedman test rejects the null hypothesis of equal performance (p<0.05p<0.05), we perform post hoc Wilcoxon signed-rank tests on marginal differences (e.g., PC→\rightarrowPCS, PCS→\rightarrowPCSB) to identify which modalities produce significant changes. Multiple testing is controlled using Bonferroni correction over the five tests performed for each modality addition. As a separate evaluation, we also test learning model differences. For this case, each model is represented by its best-performing modality configuration, and paired Wilcoxon signed-rank tests are conducted across regions to assess differences in best performances between models.

#### 3.2.3 Training and Implementation

All experiments are implemented in Python using scikit-learn for Ridge, Random Forest, and KNN [[41](https://arxiv.org/html/2602.18572v1#bib.bib35 "Scikit-learn: machine learning in python")], xgboost for gradient-boosted trees [[12](https://arxiv.org/html/2602.18572v1#bib.bib53 "XGBoost: a scalable tree boosting system")], statsmodels[[45](https://arxiv.org/html/2602.18572v1#bib.bib54 "Statsmodels: econometric and statistical modeling with python")] for ARIMA [[7](https://arxiv.org/html/2602.18572v1#bib.bib55 "Time series analysis: forecasting and control")] baselines, and PyTorch for the LSTM network [[40](https://arxiv.org/html/2602.18572v1#bib.bib36 "PyTorch: An Imperative Style, High-Performance Deep Learning Library")]. Data preprocessing and visualization relied on NumPy [[21](https://arxiv.org/html/2602.18572v1#bib.bib37 "Array programming with NumPy")], Pandas [[37](https://arxiv.org/html/2602.18572v1#bib.bib39 "Data structures for statistical computing in Python")], and Matplotlib [[27](https://arxiv.org/html/2602.18572v1#bib.bib51 "Matplotlib: A 2D Graphics Environment")]. Feature scaling is fit on training folds only to avoid leakage. Hyperparameters for Ridge, Random Forest, KNN, and the LSTM are selected via small grid searches on rolling CV splits using a subset of regions and horizons. ARIMA uses per-fold AIC-based order selection on training windows as described in Section [3.2.1](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS1 "3.2.1 Model Families ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"), while XGBoost uses the fixed specification described here.

## 4 Results and Discussion

The central finding is that sentiment and SAR provide limited benefit at short horizons but become the main driver for accurate long-horizon forecasting. Figure [6](https://arxiv.org/html/2602.18572v1#S4.F6 "Figure 6 ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") illustrates this pattern on KNN. At horizons up to 10 weeks, the price-only KNN performs comparably to the best multimodal configurations, with MAE differences typically small relative to long-horizon gaps. Beyond 14 weeks, the price-only model loses predictive power steadily while multimodal configurations remain stable. Table [2](https://arxiv.org/html/2602.18572v1#S4.T2 "Table 2 ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") summarizes MAE across models, modality configurations, and horizon groups. For KNN, long-horizon MAE decreases from 4.476 (prices only) to 2.929 (full multimodal), a 34.6% reduction. Random Forest shows a similar pattern (4.310 to 3.260), and XGBoost is competitive (4.417 to 3.139). Ridge regression achieves the lowest short-horizon MAE but does not benefit from additional modalities. LSTM underperforms across all configurations, likely due to limited training data in the weekly regime.

The univariate baselines provide useful reference points. Naive-12Mean performs competitively at short horizons but degrades rapidly as the forecast horizon increases, while ARIMA exhibits consistently higher error across all horizon groups. This behavior reveals the difficulty of long-horizon index forecasting using price history alone.

Figure [7](https://arxiv.org/html/2602.18572v1#S4.F7 "Figure 7 ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") shows long-horizon MAE distributions across regions. Nonparametric learners, KNN and Random Forest, achieve lower median errors and tighter dispersion, which indicates more consistent performance across regions under multimodal configurations. Direct comparison of these results with prior work is limited because existing studies using the same transaction dataset focus on different index constructions [[23](https://arxiv.org/html/2602.18572v1#bib.bib23 "Forecasting future trends in Dubai housing market by using Box‐Jenkins autoregressive integrated moving average")], methods such as macroeconomic cointegration [[24](https://arxiv.org/html/2602.18572v1#bib.bib22 "Relationship between residential property price index and macroeconomic indicators in dubai housing market")], and unit-level prediction [[17](https://arxiv.org/html/2602.18572v1#bib.bib28 "Comparative analysis of machine learning algorithms for predicting Dubai property prices")]. Our results therefore establish initial benchmarks for long-horizon, multimodal sub-city index forecasting.

![Refer to caption](figures/main_KNN_per_horizon_lines_labeled.png)


Figure 6: Per-horizon KNN performance by modality configuration. Lines show mean MAE across 19 regions. Beyond 14 weeks, multimodal configurations stabilize while price-only models deteriorate. Dashed lines show Naive-12Mean and ARIMA(P) baselines.




Table 2: Mean ±\pm std MAE across regions by horizon group, modality configuration, and model. Values are averaged over regions and horizons within each group, after averaging MAE across cross-validation folds. Groups: Short (2, 6, 10 weeks), Medium (14, 18, 22 weeks), Long (26, 30, 34 weeks). Bold: best configuration per model-group pair. Shaded: best across all models. Naive-12Mean and ARIMA are univariate price-only baselines reported as single summary rows. Modality codes: P=prices, C=counts, S=sentiment, B=SAR backscatter, I=interest rates, G=global context.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model | Group | P | PC | PCS | PCSB | PCSBI | PCSBIG |
| Ridge | Short | 1.988 ±\pm 1.269 | 2.248 ±\pm 1.448 | 2.260 ±\pm 1.435 | 2.446 ±\pm 1.544 | 2.608 ±\pm 1.634 | 2.912 ±\pm 1.836 |
|  | Medium | 3.426 ±\pm 1.704 | 4.005 ±\pm 1.968 | 3.987 ±\pm 1.829 | 4.254 ±\pm 1.818 | 4.428 ±\pm 1.818 | 4.687 ±\pm 1.820 |
|  | Long | 4.373 ±\pm 2.130 | 5.135 ±\pm 2.525 | 5.055 ±\pm 2.208 | 5.097 ±\pm 2.220 | 5.324 ±\pm 2.065 | 5.278 ±\pm 1.980 |
| RF | Short | 2.905 ±\pm 1.771 | 2.887 ±\pm 1.738 | 2.876 ±\pm 1.707 | 2.796 ±\pm 1.560 | 2.949 ±\pm 1.666 | 2.839 ±\pm 1.574 |
|  | Medium | 3.858 ±\pm 1.884 | 3.687 ±\pm 1.829 | 3.560 ±\pm 1.821 | 3.376 ±\pm 1.686 | 3.484 ±\pm 1.773 | 3.218 ±\pm 1.557 |
|  | Long | 4.310 ±\pm 2.253 | 3.928 ±\pm 1.936 | 3.738 ±\pm 1.850 | 3.486 ±\pm 1.789 | 3.583 ±\pm 1.902 | 3.260 ±\pm 1.580 |
| KNN | Short | 3.104 ±\pm 1.760 | 3.309 ±\pm 1.782 | 3.224 ±\pm 1.712 | 3.161 ±\pm 1.611 | 3.090 ±\pm 1.609 | 3.022 ±\pm 1.566 |
|  | Medium | 4.031 ±\pm 2.077 | 3.749 ±\pm 1.916 | 3.463 ±\pm 1.755 | 3.146 ±\pm 1.588 | 3.002 ±\pm 1.618 | 2.910 ±\pm 1.551 |
|  | Long | 4.476 ±\pm 2.461 | 4.030 ±\pm 2.177 | 3.603 ±\pm 1.876 | 3.185 ±\pm 1.708 | 3.120 ±\pm 1.817 | 2.929 ±\pm 1.504 |
| LSTM | Short | 4.746 ±\pm 2.956 | 5.258 ±\pm 3.291 | 6.028 ±\pm 3.638 | 5.741 ±\pm 3.429 | 5.615 ±\pm 3.129 | 5.883 ±\pm 3.591 |
|  | Medium | 5.189 ±\pm 3.325 | 5.462 ±\pm 3.404 | 5.893 ±\pm 3.601 | 5.864 ±\pm 3.906 | 5.702 ±\pm 3.615 | 5.603 ±\pm 3.216 |
|  | Long | 5.541 ±\pm 3.594 | 5.399 ±\pm 3.317 | 6.138 ±\pm 4.030 | 5.958 ±\pm 4.056 | 5.905 ±\pm 3.822 | 5.820 ±\pm 3.853 |
| XGB | Short | 3.075 ±\pm 1.799 | 3.004 ±\pm 1.780 | 2.935 ±\pm 1.687 | 2.859 ±\pm 1.591 | 2.940 ±\pm 1.648 | 2.822 ±\pm 1.576 |
|  | Medium | 3.955 ±\pm 1.939 | 3.649 ±\pm 1.833 | 3.428 ±\pm 1.775 | 3.248 ±\pm 1.616 | 3.316 ±\pm 1.706 | 3.056 ±\pm 1.516 |
|  | Long | 4.417 ±\pm 2.330 | 3.976 ±\pm 2.071 | 3.644 ±\pm 1.894 | 3.385 ±\pm 1.780 | 3.493 ±\pm 1.942 | 3.139 ±\pm 1.530 |
| ARIMA | All | 3.582 (Short) / 4.404 (Medium) / 5.116 (Long) | | | | | |
| Naive-12Mean | All | 2.489 (Short) / 3.387 (Medium) / 4.183 (Long) | | | | | |

![Refer to caption](figures/main_long_all_models_boxplots.png)


Figure 7: Long-horizon MAE distributions across sub-city regions. Horizontal gray lines indicate Naive-12Mean baseline. KNN and Random Forest show the largest multimodal gains with tighter regional dispersion.

We assess whether performance differences represent genuine improvements using nonparametric tests across all 19 regions at long horizons (h≥26h\geq 26). Table [3](https://arxiv.org/html/2602.18572v1#S4.T3 "Table 3 ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") reports within-model tests for modality additions. Overall variation across modality configurations is significant for all evaluated learning models, including Ridge (p=0.00606p=0.00606), LSTM (p=8.82×10−4p=8.82\times 10^{-4}), and the nonparametric and ensemble methods (p<0.001p<0.001 for KNN, RF, and XGB). The pattern of gains differs by model. KNN shows the clearest and most consistent multimodal response: adding sentiment yields a significant improvement (PC→\rightarrowPCS, pcorr=0.00261p\_{\text{corr}}=0.00261), and adding SAR produces a further strong reduction in error (PCS→\rightarrowPCSB, pcorr=5.7×10−5p\_{\text{corr}}=5.7\times 10^{-5}). Random Forest benefits significantly from SAR (PCS→\rightarrowPCSB, pcorr=0.00134p\_{\text{corr}}=0.00134) and from adding global context (PCSBI→\rightarrowPCSBIG, pcorr=0.00483p\_{\text{corr}}=0.00483). XGBoost exhibits significant improvements at multiple stages, including sentiment (PC→\rightarrowPCS, pcorr=2.67×10−4p\_{\text{corr}}=2.67\times 10^{-4}), SAR (PCS→\rightarrowPCSB, pcorr=0.00210p\_{\text{corr}}=0.00210), and global context (PCSBI→\rightarrowPCSBIG, pcorr=0.00586p\_{\text{corr}}=0.00586). Ridge improves only when transaction counts are added to prices (P→\rightarrowPC, pcorr=0.00483p\_{\text{corr}}=0.00483), with no further significant multimodal gains. LSTM shows a statistically significant improvement only for sentiment addition (PC→\rightarrowPCS, pcorr=0.00847p\_{\text{corr}}=0.00847), but remains substantially less accurate than nonparametric methods in Table [2](https://arxiv.org/html/2602.18572v1#S4.T2 "Table 2 ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").

Table 3: Within-model significance tests across modality configurations (h≥26h\geq 26). Friedman tests assess overall variation; Wilcoxon signed-rank tests with Bonferroni correction assess adjacent transitions. “n.s.” denotes non-significant after correction.

| Model | Friedman | Significant Transitions (Bonferroni-corrected pp) |
| --- | --- | --- |
| Ridge | p=0.00606p=0.00606 | P→\rightarrowPC: 0.00483; others n.s. |
| RF | p<0.001p<0.001 | PCS→\rightarrowPCSB: 0.00134; PCSBI→\rightarrowPCSBIG: 0.00483 |
| KNN | p<0.001p<0.001 | PC→\rightarrowPCS: 0.00261; PCS→\rightarrowPCSB: 5.7×10−55.7\times 10^{-5} |
| LSTM | p=8.82×10−4p=8.82\times 10^{-4} | PC→\rightarrowPCS: 0.00847; others n.s. |
| XGB | p<0.001p<0.001 | PC→\rightarrowPCS: 0.00027; PCS→\rightarrowPCSB: 0.00210; PCSBI→\rightarrowPCSBIG: 0.00586 |

### 4.1 Model Diagnostics

To understand why multimodal inputs improve KNN but not LSTM, we examine model behavior at the longest horizon (h=34h=34). We compare price-only (P) and full multimodal (PCSBIG) configurations using three metrics: percentage MAE reduction, mean fraction of shared nearest neighbors, and baseline MAE.

#### 4.1.1 KNN

Regions with the largest long-horizon improvements under multimodal inputs (e.g., Jumeirah Village Triangle, International City Phase 1, Mudon) exhibit relatively stable nearest-neighbor structures when moving from price-only to full multimodal features. We quantify neighborhood stability by the mean overlap between the kk nearest neighbors selected by KNN using price-only features and those selected under the full multimodal representation at h=34h=34. Across regions, mean neighbor overlap ranges from approximately 0.49 to 0.73, which reflects heterogeneity in nearest-neighbor selection under multimodal features. Across regions, the association between neighbor overlap and percentage MAE reduction is positive but modest (Pearson r=0.19r=0.19, Spearman ρ=0.24\rho=0.24). In contrast, baseline price-only error exhibits a somewhat stronger correlation with relative improvement (Pearson r=0.35r=0.35, Spearman ρ=0.28\rho=0.28), suggesting that multimodal gains depend both on local neighborhood stability and on the underlying predictability of the regional price series. Taken together, these diagnostics indicate that multimodal improvements in KNN result from modifications to nearest-neighbor sets rather than complete replacement, and that neighborhood stability alone is insufficient to explain cross-regional variation in gains.

#### 4.1.2 LSTM

To assess whether the LSTM transforms multimodal inputs into predictive representations, we apply linear probes [[1](https://arxiv.org/html/2602.18572v1#bib.bib52 "Understanding intermediate layers using linear classifier probes")] to frozen hidden states at h=34h=34. Each probe is a linear model mapping the final hidden representation to each modality’s input features. All modalities exhibit high linear recoverability (R2>0.94R^{2}>0.94, ranging from 0.9440.944 for sentiment to 0.9830.983 for interest rates), indicating that the LSTM explicitly encodes multimodal inputs rather than discarding or abstracting them. Despite this high-fidelity encoding, the LSTM does not achieve improved long-horizon accuracy. This diagnostic suggests that its underperformance stems from ineffective utilization of encoded signals rather than missing information.

### 4.2 Decomposing Signal Contributions

In this section we expand the additive tag system beyond the six main configurations in Table [1](https://arxiv.org/html/2602.18572v1#S3.T1 "Table 1 ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") to conduct ablations. Tags remain defined as subsets of modalities {P,C,S,B,I,G}\{P,C,S,B,I,G\}, but instead of evaluating only the single additive chain (e.g., PC→\rightarrowPCS→\rightarrowPCSB), we also evaluate additional combinations obtained by adding or removing specific modality blocks. All Δ\DeltaMAE values in the contribution analysis are averaged across all horizons, regions, and rolling cross-validation folds.

#### 4.2.1 Marginal Contributions over Transactional Baselines

Figure [8](https://arxiv.org/html/2602.18572v1#S4.F8 "Figure 8 ‣ 4.2.1 Marginal Contributions over Transactional Baselines ‣ 4.2 Decomposing Signal Contributions ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") reports changes in MAE when exogenous modalities are added to three transaction-based baselines: prices only (P), prices plus counts (PC), and prices, counts, and global context (PCG). For each baseline, sentiment (SS), SAR backscatter (BB), and interest rates (II) are added individually and in combination, and Δ\DeltaMAE is reported relative to the corresponding baseline. Across all baselines, SAR provides the largest single-modality improvement, while sentiment and interest rates yield smaller but consistent gains. The strongest reductions arise when sentiment, SAR, and interest rates are combined. Relative to P, the best configuration reduces MAE by 0.77 (approximately 20%). Relative to PC, the best enrichment achieves a 0.61 point reduction (16.5%). When global context is already included (PCG), additional gains are more modest (0.21 points, 6.8%), indicating diminishing marginal returns once higher-level market structure is incorporated.

![Refer to caption](figures/knn_transactional_baselines_enrichment.png)


Figure 8: Modality contributions relative to transaction baselines (KNN). Panels show incremental additions of sentiment, SAR, and interest rates. Negative Δ\DeltaMAE indicates improvement; largest gains arise from combined sentiment and SAR.

#### 4.2.2 Exogenous-Only Signals

Figure [9](https://arxiv.org/html/2602.18572v1#S4.F9 "Figure 9 ‣ 4.2.2 Exogenous-Only Signals ‣ 4.2 Decomposing Signal Contributions ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") evaluates configurations that exclude regional price history, using subsets of counts (CC), sentiment (SS), SAR (BB), and global context (GG). Relative to the price-only baseline, single-modality inputs perform poorly, and neither sentiment nor SAR alone is sufficient to match autoregressive performance. However, combining sentiment and SAR yields moderate improvements over prices, with the SB and CSB configurations reducing MAE by approximately 0.38 and 0.34 points, respectively. Despite these gains, all exogenous-only configurations perform worse than the full multimodal model. Relative to the PCSBIG configuration, errors increase by 0.5 to 2.5 MAE points. This confirms that while exogenous signals can partially substitute for transaction history at long horizons when combined, they cannot replace regional price dynamics, and the strongest performance arises from their integration with transactional data.

![Refer to caption](figures/knn_exogenous_only_enrichment.png)


Figure 9: Ablations excluding regional price history (KNN). (a) Δ\DeltaMAE relative to price-only baseline. (b) Δ\DeltaMAE relative to full multimodal configuration. Sentiment and SAR provide value primarily when combined with transaction data.

### 4.3 Alternative Representations of Sentiment and Built Environment

Beyond establishing that sentiment and remote sensing signals improve long-horizon forecasts, we examine how alternative representations of the same underlying factors affect predictive performance. We focus on two cases: (i) lexical versus semantic representations of news-derived sentiment, and (ii) radar versus optical representations of the built environment.

#### 4.3.1 Sentiment: Lexical versus Semantic Representations

We decompose the sentiment signal to assess whether predictive value derives primarily from lexical tone or semantic content. Table [4](https://arxiv.org/html/2602.18572v1#S4.T4 "Table 4 ‣ 4.3.2 Urban Environment: SAR versus Optical Indices ‣ 4.3 Alternative Representations of Sentiment and Built Environment ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") (top panel) compares three sentiment configurations for the PC→\rightarrowPCS transition: NSI-only (lexical), PCA-only (semantic), and the full block that combines both. All comparisons are conducted on long horizons (h≥26h\geq 26) using paired tests across regions. Lexical NSI features yield a modest but statistically significant reduction in MAE. Aggregate tone alone therefore contains predictive information at long horizons. Semantic PCA features, however, produce a larger and more consistent improvement. Topical structure captured by embeddings provides richer market-relevant signals than polarity alone. The full sentiment block achieves the largest MAE reduction, though its advantage over the PCA-only configuration is incremental. Most of the predictive value therefore arises from semantic components. These results demonstrate that lexical tone contributes marginally to forecast accuracy, but long-horizon gains depend primarily on semantic representations.

#### 4.3.2 Urban Environment: SAR versus Optical Indices

We next compare Sentinel-1 SAR backscatter [[48](https://arxiv.org/html/2602.18572v1#bib.bib47 "GMES Sentinel-1 mission")] against Sentinel-2 NDBI [[55](https://arxiv.org/html/2602.18572v1#bib.bib10 "Use of normalized difference built-up index in automatically mapping urban areas from TM imagery"), [15](https://arxiv.org/html/2602.18572v1#bib.bib50 "Sentinel-2: ESA’s Optical High-Resolution Mission for GMES Operational Services")] as alternative representations of urban-environment dynamics. Figure [10](https://arxiv.org/html/2602.18572v1#S4.F10 "Figure 10 ‣ 4.3.2 Urban Environment: SAR versus Optical Indices ‣ 4.3 Alternative Representations of Sentiment and Built Environment ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") provides a qualitative comparison across three major subregions over time. SAR backscatter shows consistent sensitivity to structural changes associated with urban development. NDBI, by contrast, exhibits greater variability due to atmospheric conditions and illumination effects. Table [4](https://arxiv.org/html/2602.18572v1#S4.T4 "Table 4 ‣ 4.3.2 Urban Environment: SAR versus Optical Indices ‣ 4.3 Alternative Representations of Sentiment and Built Environment ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") (bottom panel) reports paired one-sided tests that compare SAR and NDBI against no-BB baselines at long horizons (h≥26h\geq 26). For the PCS→\rightarrowPCSB transition, SAR yields a large and highly significant reduction in MAE (mean Δ\DeltaMAE =−0.43=-0.43, p=1.8×10−4p=1.8\times 10^{-4}). NDBI produces no improvement under this configuration.

Table 4: Representation ablations for sentiment and built-environment modalities (KNN, h≥26h\geq 26). Reported values are mean Δ\DeltaMAE relative to the no-modality baseline for each transition, with one-sided paired tests.

|  |  |  |
| --- | --- | --- |
| Feature Variant | Mean Δ\DeltaMAE | pp-value |
| Sentiment (PC→\rightarrowPCS) | | |
| NSI only (lexical) | −0.124-0.124 | 0.03480.0348 |
| PCA only (semantic) | −0.193-0.193 | 0.00690.0069 |
| Full sentiment block | −0.264-0.264 | 0.00470.0047 |
| Built environment (PCS→\rightarrowPCSB) | | |
| SAR backscatter | −0.429-0.429 | 1.8×10−41.8\times 10^{-4} |
| Optical NDBI | +0.058+0.058 | 0.940.94 (n.s.) |

![Refer to caption](figures/sar_ndbi_3x4_panel_annotated_a4.png)


Figure 10: SAR and NDBI comparison across three Dubai subregions (2016 vs. 2025). SAR backscatter (left columns) shows consistent sensitivity to built-up development, while optical NDBI (right columns) exhibits greater variability.

### 4.4 Out-of-Sample Forecast Behavior

Figure [11](https://arxiv.org/html/2602.18572v1#S4.F11 "Figure 11 ‣ 4.4 Out-of-Sample Forecast Behavior ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment") presents out-of-sample predictions for the Dubai Marina sub-city price index at 34 weeks ahead. The forecast series is constructed by stitching non-overlapping validation windows. The price-only model exhibits pronounced oscillations and delayed responses around turning points. The multimodal configuration, in contrast, tracks the realized series more smoothly over the 2022–2025 period. It captures medium-term acceleration and deceleration phases more consistently than the price-only model. Improvements are particularly visible during high-volatility intervals. Multimodal forecasts reduce persistent gaps relative to observed prices in these periods. These results are consistent with the autoregressive limitations and multimodal stabilization effects found earlier.

![Refer to caption](figures/predictions_KNN_Dubai_Marina_h34_P-PCSBIG.png)


Figure 11: Out-of-sample 34-week forecasts for the Dubai Marina price index (2022–2025). The price-only model displays higher volatility and delayed trend response, while the multimodal configuration produces smoother forecasts that track realized values more closely.

## 5 Conclusion

This study asked whether satellite imagery and news sentiment can reveal real estate market dynamics that transaction records alone cannot capture. Using weekly price indices for Dubai sub-city regions constructed from over 350,000 transactions, we find that the answer is affirmative but horizon dependent. At short horizons (up to 10 weeks ahead), transaction history alone performs strongly as autoregressive patterns dominate. Beyond 14 weeks, however, price-driven patterns decay and non-traditional signals provide significant gains that preserve predictability. At long horizons (26–34 weeks ahead), integrating Sentinel-1 SAR backscatter and news sentiment reduces forecast error by roughly one third compared to price-only baselines, with improvements statistically significant across regions.

Three findings are particularly notable. First, nonparametric learners (KNN and Random Forest) consistently outperform both linear models and LSTM in this weekly sample regime. This suggests that the forecasting challenge depends more on feature engineering than architectural complexity. Second, semantic news embeddings carry more predictive value than lexical sentiment scores. Topical structure matters more than aggregate positive-negative tone. Third, SAR backscatter significantly outperforms optical NDBI as a built-environment proxy, likely because radar captures surface changes from construction activity that precede transaction records and does this more reliably than optical imagery over time.

As a result, we show that sub-city dynamics are predictable at strategically relevant horizons and frequency when transaction records are combined with signals reflecting physical development and market sentiment. The modular framework and systematic ablations we introduced establish reproducible benchmarks for multimodal index forecasting and clarify when non-traditional signals add value. The framework’s applicability beyond Dubai remains to be tested. Markets with sparse reporting or slower development may exhibit different signal dynamics. For future work, cross-regional dependencies modeled through graph representations offer a natural extension [[56](https://arxiv.org/html/2602.18572v1#bib.bib1 "MugRep: A Multi-Task Hierarchical Graph Representation Learning Framework for Real Estate Appraisal"), [49](https://arxiv.org/html/2602.18572v1#bib.bib2 "Financial asset price prediction with graph neural network-based temporal deep learning models")]. A second direction to explore is topic-aware sentiment models tailored to real estate discourse as a path toward more interpretable market factors.

## Data and Code Availability

The code repository and all processed features used in modeling (the weekly aligned feature matrices) will be released upon acceptance. All raw data sources used in this study are publicly accessible: transaction records from the Dubai Land Department (Open Data License), news metadata from the GDELT Project (article text retrieved independently is not redistributed, instead aggregated sentiment features are provided), Sentinel-1 and Sentinel-2 satellite imagery from the Copernicus Programme, and interest rates from the Central Bank of the UAE.

## References

* [1]
  G. Alain and Y. Bengio (2018)
  Understanding intermediate layers using linear classifier probes.
  External Links: 1610.01644,
  [Link](https://arxiv.org/abs/1610.01644)
  Cited by: [§4.1.2](https://arxiv.org/html/2602.18572v1#S4.SS1.SSS2.p1.4 "4.1.2 LSTM ‣ 4.1 Model Diagnostics ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [2]
  D. Araci (2019-08)
  FinBERT: Financial Sentiment Analysis with Pre-trained Language Models.
   arXiv (en).
  Note: arXiv:1908.10063 [cs]Comment: This thesis is submitted in partial fulfillment for the degree of Master of Science in Information Studies: Data Science, University of Amsterdam. June 25, 2019
  External Links: [Link](http://arxiv.org/abs/1908.10063),
  [Document](https://dx.doi.org/10.48550/arXiv.1908.10063)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p3.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [3]
  B. Arat, H. F. Ateş, and E. Sefer (2025)
  Multi-context real estate market prediction.
  In 2025 33rd Signal Processing and Communications Applications Conference (SIU),
  Vol. ,  pp. 1–4.
  External Links: [Document](https://dx.doi.org/10.1109/SIU66497.2025.11112013)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p5.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [4]
  Bank for International Settlements (2025)
  Residential property prices for the united arab emirates.
  Note: Federal Reserve Economic Data (FRED)Series ID: QAEN628BIS
  External Links: [Link](https://fred.stlouisfed.org/series/QAEN628BIS)
  Cited by: [§3.1.1](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS1.Px1.p1.1 "Quantile trimming and robustness. ‣ 3.1.1 Price Index and Volumes ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [5]
  A. Barbaresi (2021-08)
  Trafilatura: A web scraping library and command-line tool for text discovery and extraction.
  In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing: System Demonstrations, H. Ji, J. C. Park, and R. Xia (Eds.),
  Online,  pp. 122–131.
  External Links: [Link](https://aclanthology.org/2021.acl-demo.15/),
  [Document](https://dx.doi.org/10.18653/v1/2021.acl-demo.15)
  Cited by: [§3.1.2](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS2.p1.1 "3.1.2 News-Based Sentiment ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [6]
  A. Bogin, W. M. Doerner, and W. Larson (2016-09)
  Missing the Mark: House Price Index Accuracy and Mortgage Credit Modeling.
  FHFA Working Paper
  Technical Report 16-04, Federal Housing Finance Agency (en).
  External Links: [Link](https://ssrn.com/abstract=3416895),
  [Document](https://dx.doi.org/10.2139/ssrn.3416895)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p1.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [7]
  G. E. P. Box, G. M. Jenkins, G. C. Reinsel, and G. M. Ljung (2015)
  Time series analysis: forecasting and control.
  5th edition, Wiley.
  Cited by: [§3.2.1](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS1.p1.7 "3.2.1 Model Families ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§3.2.3](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS3.p1.1 "3.2.3 Training and Implementation ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [8]
  L. Breiman (2001)
  Random forests.
  Machine Learning 45 (1),  pp. 5–32.
  Cited by: [§3.2.1](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS1.p2.4 "3.2.1 Model Families ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [9]
  Central Bank of the UAE (2025)
  EIBOR rates.
  Note: WebsiteAccessed 2025-07-20
  External Links: [Link](https://www.centralbank.ae/en/forex-eibor/eibor-rates/)
  Cited by: [§3.1.4](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS4.p1.1 "3.1.4 Interest Rates ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [10]
  C. Chen, H. Zhai, Z. Wang, S. Ma, J. Sun, C. Wu, and Y. Zhang (2022)
  Experimental research on the impact of interest rate on real estate market transactions.
  Discrete Dynamics in Nature and Society 2022 (1),  pp. 9946703.
  Cited by: [§3.1.4](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS4.p1.1 "3.1.4 Interest Rates ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [11]
  M. Chen, J. Wang, F. Zhao, and G. Jiang (2025-08)
  Research on sentiment index and real estate demand forecasting based on BERT-BiLSTM and ADL-MIDAS models.
  Scientific Reports 15 (1),  pp. 30240 (en).
  External Links: ISSN 2045-2322,
  [Link](https://www.nature.com/articles/s41598-025-16153-8),
  [Document](https://dx.doi.org/10.1038/s41598-025-16153-8)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p3.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [12]
  T. Chen and C. Guestrin (2016-08)
  XGBoost: a scalable tree boosting system.
  In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining,
  KDD ’16,  pp. 785–794.
  External Links: [Link](http://dx.doi.org/10.1145/2939672.2939785),
  [Document](https://dx.doi.org/10.1145/2939672.2939785)
  Cited by: [§3.2.1](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS1.p2.4 "3.2.1 Model Families ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§3.2.3](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS3.p1.1 "3.2.3 Training and Implementation ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [13]
  K. S. Cheung and J. Lee (2021-09)
  The effect of sentiment on commercial real estate returns: investor and occupier perspectives.
  Journal of Property Investment & Finance 39 (6),  pp. 561–589 (en).
  External Links: ISSN 1463-578X,
  [Link](http://www.emerald.com/jpif/article/39/6/561-589/235479),
  [Document](https://dx.doi.org/10.1108/JPIF-01-2020-0010)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p3.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [14]
  T. M. Cover and P. E. Hart (1967)
  Nearest neighbor pattern classification.
  IEEE Transactions on Information Theory 13 (1),  pp. 21–27.
  Cited by: [§3.2.1](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS1.p2.4 "3.2.1 Model Families ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [15]
  M. Drusch, U. Del Bello, S. Carlier, O. Colin, V. Fernandez, F. Gascon, B. Hoersch, C. Isola, P. Laberinti, P. Martimort, A. Meygret, F. Spoto, O. Sy, F. Marchese, and P. Bargellini (2012-05)
  Sentinel-2: ESA’s Optical High-Resolution Mission for GMES Operational Services.
  Remote Sensing of Environment 120,  pp. 25–36 (en).
  External Links: ISSN 00344257,
  [Link](https://linkinghub.elsevier.com/retrieve/pii/S0034425712000636),
  [Document](https://dx.doi.org/10.1016/j.rse.2011.11.026)
  Cited by: [§4.3.2](https://arxiv.org/html/2602.18572v1#S4.SS3.SSS2.p1.6 "4.3.2 Urban Environment: SAR versus Optical Indices ‣ 4.3 Alternative Representations of Sentiment and Built Environment ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [16]
  Dubai Land Department (2025)
  Dubai land department open data: real estate data.
  Note: Open data portalAccessed 2025-07-20
  External Links: [Link](https://dubailand.gov.ae/en/open-data/real-estate-data/)
  Cited by: [§1](https://arxiv.org/html/2602.18572v1#S1.p4.1 "1 Introduction ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [17]
  A. Elnaeem Balila and A. B. Shabri (2024-02)
  Comparative analysis of machine learning algorithms for predicting Dubai property prices.
  Frontiers in Applied Mathematics and Statistics 10,  pp. 1327376 (en).
  External Links: ISSN 2297-4687,
  [Link](https://www.frontiersin.org/articles/10.3389/fams.2024.1327376/full),
  [Document](https://dx.doi.org/10.3389/fams.2024.1327376)
  Cited by: [§4](https://arxiv.org/html/2602.18572v1#S4.p3.1 "4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [18]
  C. Ge, Y. Wang, X. Xie, H. Liu, and Z. Zhou (2019-11)
  An Integrated Model for Urban Subregion House Price Forecasting: A Multi-source Data Perspective.
  In 2019 IEEE International Conference on Data Mining (ICDM),
  Beijing, China,  pp. 1054–1059 (en).
  External Links: ISBN 978-1-7281-4604-1,
  [Link](https://ieeexplore.ieee.org/document/8970751/),
  [Document](https://dx.doi.org/10.1109/ICDM.2019.00123)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p1.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [19]
  N. Gorelick, M. Hancher, M. Dixon, S. Ilyushchenko, D. Thau, and R. Moore (2017-12)
  Google Earth Engine: Planetary-scale geospatial analysis for everyone.
  Remote Sensing of Environment 202,  pp. 18–27 (en).
  External Links: ISSN 00344257,
  [Link](https://linkinghub.elsevier.com/retrieve/pii/S0034425717302900),
  [Document](https://dx.doi.org/10.1016/j.rse.2017.06.031)
  Cited by: [§3.1.3](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS3.p1.5 "3.1.3 Satellite SAR Features ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [20]
  S. Hafner, A. Nascetti, H. Azizpour, and Y. Ban (2022)
  Sentinel-1 and Sentinel-2 Data Fusion for Urban Change Detection Using a Dual Stream U-Net.
  IEEE Geoscience and Remote Sensing Letters 19,  pp. 1–5 (en).
  External Links: ISSN 1545-598X, 1558-0571,
  [Link](https://ieeexplore.ieee.org/document/9570476/),
  [Document](https://dx.doi.org/10.1109/LGRS.2021.3119856)
  Cited by: [§3.1.3](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS3.p1.5 "3.1.3 Satellite SAR Features ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [21]
  C. R. Harris, K. J. Millman, S. J. Van Der Walt, R. Gommers, P. Virtanen, D. Cournapeau, E. Wieser, J. Taylor, S. Berg, N. J. Smith, R. Kern, M. Picus, S. Hoyer, M. H. Van Kerkwijk, M. Brett, A. Haldane, J. F. Del Río, M. Wiebe, P. Peterson, P. Gérard-Marchant, K. Sheppard, T. Reddy, W. Weckesser, H. Abbasi, C. Gohlke, and T. E. Oliphant (2020-09)
  Array programming with NumPy.
  Nature 585 (7825),  pp. 357–362 (en).
  External Links: ISSN 0028-0836, 1476-4687,
  [Link](https://www.nature.com/articles/s41586-020-2649-2),
  [Document](https://dx.doi.org/10.1038/s41586-020-2649-2)
  Cited by: [§3.2.3](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS3.p1.1 "3.2.3 Training and Implementation ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [22]
  M. H. Hasan, M. A. Jahan, M. E. Ali, Y. Li, and T. Sellis (2024-09)
  A Multi-Modal Deep Learning Based Approach for House Price Prediction.
   arXiv (en).
  Note: arXiv:2409.05335 [cs]Comment: 22 pages
  External Links: [Link](http://arxiv.org/abs/2409.05335),
  [Document](https://dx.doi.org/10.48550/arXiv.2409.05335)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p2.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [23]
  A. Hepşen and M. Vatansever (2011-08)
  Forecasting future trends in Dubai housing market by using Box‐Jenkins autoregressive integrated moving average.
  International Journal of Housing Markets and Analysis 4 (3),  pp. 210–223 (en).
  External Links: ISSN 1753-8270,
  [Link](http://www.emerald.com/ijhma/article/4/3/210-223/127611),
  [Document](https://dx.doi.org/10.1108/17538271111153004)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p1.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§4](https://arxiv.org/html/2602.18572v1#S4.p3.1 "4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [24]
  A. Hepşen and M. Vatansever (2012)
  Relationship between residential property price index and macroeconomic indicators in dubai housing market.
  International Journal of Strategic Property Management 16 (1),  pp. 71–84.
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p1.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§3.1.1](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS1.p1.1 "3.1.1 Price Index and Volumes ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§4](https://arxiv.org/html/2602.18572v1#S4.p3.1 "4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [25]
  S. Hochreiter and J. Schmidhuber (1997)
  Long short-term memory.
  Neural Computation 9 (8),  pp. 1735–1780.
  Cited by: [§3.2.1](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS1.p2.4 "3.2.1 Model Families ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [26]
  C. Huang, Z. Li, F. Chen, and B. Liang (2025-03)
  Multimodal Machine Learning for Real Estate Appraisal: A Comprehensive Survey.
   arXiv (en).
  Note: arXiv:2503.22119 [cs]Comment: 13 pages, 5 figures
  External Links: [Link](http://arxiv.org/abs/2503.22119),
  [Document](https://dx.doi.org/10.48550/arXiv.2503.22119)
  Cited by: [§1](https://arxiv.org/html/2602.18572v1#S1.p2.1 "1 Introduction ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§2](https://arxiv.org/html/2602.18572v1#S2.p2.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [27]
  J. D. Hunter (2007)
  Matplotlib: A 2D Graphics Environment.
  Computing in Science & Engineering 9 (3),  pp. 90–95 (en).
  External Links: ISSN 1521-9615,
  [Link](http://ieeexplore.ieee.org/document/4160265/),
  [Document](https://dx.doi.org/10.1109/MCSE.2007.55)
  Cited by: [§3.2.3](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS3.p1.1 "3.2.3 Training and Implementation ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [28]
  C. Jiang, J. Li, W. Wang, and W. Ku (2021-11)
  Modeling Real Estate Dynamics Using Temporal Encoding.
  In Proceedings of the 29th International Conference on Advances in Geographic Information Systems,
  Beijing China,  pp. 516–525 (en).
  External Links: ISBN 978-1-4503-8664-7,
  [Link](https://dl.acm.org/doi/10.1145/3474717.3484254),
  [Document](https://dx.doi.org/10.1145/3474717.3484254)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p2.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [29]
  J. Kucklick and O. Müller (2021-05)
  A Comparison of Multi-View Learning Strategies for Satellite Image-Based Real Estate Appraisal.
   arXiv (en).
  Note: arXiv:2105.04984 [cs]Comment: Presented at: The AAAI-21 Workshop on Knowledge Discovery from Unstructured Data in Financial Services
  External Links: [Link](http://arxiv.org/abs/2105.04984),
  [Document](https://dx.doi.org/10.48550/arXiv.2105.04984)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p2.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [30]
  W. D. Larson (2010-11)
  Evaluating Alternative Methods of Forecasting House Prices: A Post-Crisis Reassessment.
  (en).
  Note: Available at SSRN
  External Links: [Link](https://ssrn.com/abstract=1709647),
  [Document](https://dx.doi.org/10.2139/ssrn.1709647)
  Cited by: [§1](https://arxiv.org/html/2602.18572v1#S1.p1.1 "1 Introduction ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§2](https://arxiv.org/html/2602.18572v1#S2.p1.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [31]
  K. Leetaru and P. A. Schrodt (2013)
  GDELT: global data on events, language, and tone, 1979–2012.
  In ISA Annual Convention,
  San Francisco, CA.
  External Links: [Link](http://data.gdeltproject.org/documentation/ISA.2013.GDELT.pdf)
  Cited by: [§3.1.2](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS2.p1.1 "3.1.2 News-Based Sentiment ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [32]
  S. Levantesi and G. Piscopo (2020-10)
  The Importance of Economic Variables on London Real Estate Market: A Random Forest Approach.
  Risks 8 (4),  pp. 112 (en).
  External Links: ISSN 2227-9091,
  [Link](https://www.mdpi.com/2227-9091/8/4/112),
  [Document](https://dx.doi.org/10.3390/risks8040112)
  Cited by: [§1](https://arxiv.org/html/2602.18572v1#S1.p1.1 "1 Introduction ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§2](https://arxiv.org/html/2602.18572v1#S2.p1.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [33]
  Y. Li, P. Matgen, and M. Chini (2024)
  Extraction of Built-Up Areas Using Sentinel-1 and Sentinel-2 Data with Automated Training Data Sampling and Label Noise Robust Cross-Fusion Neural Networks.
   SSRN (en).
  External Links: [Link](https://www.ssrn.com/abstract=4903268),
  [Document](https://dx.doi.org/10.2139/ssrn.4903268)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p4.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [34]
  P. P. Liang, A. Zadeh, and L. Morency (2024-10)
  Foundations & Trends in Multimodal Machine Learning: Principles, Challenges, and Open Questions.
  ACM Computing Surveys 56 (10),  pp. 1–42 (en).
  External Links: ISSN 0360-0300, 1557-7341,
  [Link](https://dl.acm.org/doi/10.1145/3656580),
  [Document](https://dx.doi.org/10.1145/3656580)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p2.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [35]
  I. Loshchilov and F. Hutter (2019)
  Decoupled weight decay regularization.
  External Links: 1711.05101,
  [Link](https://arxiv.org/abs/1711.05101)
  Cited by: [§3.2.1](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS1.p2.4 "3.2.1 Model Families ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [36]
  H. B. Makineci (2023)
  Spatio-temporal change detection of built-up areas with sentinel-1 sar data using random forest classification for arnavutköy istanbul.
  Niğde Ömer Halisdemir Üniversitesi Mühendislik Bilimleri Dergisi 12 (2),  pp. 626–636.
  External Links: [Document](https://dx.doi.org/10.28948/ngumuh.1203301)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p4.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§3.1.3](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS3.p1.5 "3.1.3 Satellite SAR Features ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [37]
  W. McKinney (2010)
  Data structures for statistical computing in Python.
  In Proceedings of the 9th Python in Science Conference (SciPy 2010), S. van der Walt and J. Millman (Eds.),
  Austin, Texas,  pp. 56–61.
  External Links: [Document](https://dx.doi.org/10.25080/Majora-92bf1922-00a),
  [Link](https://doi.org/10.25080/Majora-92bf1922-00a)
  Cited by: [§3.2.3](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS3.p1.1 "3.2.3 Training and Implementation ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [38]
  A. Owusu-Ansah (2013)
  Construction of property price indices: temporal aggregation and accuracy of various index methods.
  Property Management 31 (2),  pp. 115–131.
  Cited by: [§1](https://arxiv.org/html/2602.18572v1#S1.p1.1 "1 Introduction ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [39]
  A. Owusu-Ansah (2018)
  Construction and application of property price indices.
  1 edition, Routledge, London.
  External Links: [Document](https://dx.doi.org/10.1201/9781315102085),
  ISBN 9781315102085
  Cited by: [§1](https://arxiv.org/html/2602.18572v1#S1.p1.1 "1 Introduction ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [40]
  A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, A. Desmaison, A. Köpf, E. Yang, Z. DeVito, M. Raison, A. Tejani, S. Chilamkurthy, B. Steiner, L. Fang, J. Bai, and S. Chintala (2019-12)
  PyTorch: An Imperative Style, High-Performance Deep Learning Library.
   arXiv (en).
  Note: arXiv:1912.01703 [cs]Comment: 12 pages, 3 figures, NeurIPS 2019
  External Links: [Link](http://arxiv.org/abs/1912.01703),
  [Document](https://dx.doi.org/10.48550/arXiv.1912.01703)
  Cited by: [§3.2.3](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS3.p1.1 "3.2.3 Training and Implementation ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [41]
  F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and É. Duchesnay (2011)
  Scikit-learn: machine learning in python.
  Journal of Machine Learning Research 12 (85),  pp. 2825–2830.
  External Links: [Link](http://jmlr.org/papers/v12/pedregosa11a.html)
  Cited by: [§3.2.3](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS3.p1.1 "3.2.3 Training and Implementation ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [42]
  V. Plakandaras, R. Gupta, P. Gogas, and T. Papadimitriou (2015-02)
  Forecasting the U.S. real house price index.
  Economic Modelling 45,  pp. 259–267 (en).
  External Links: ISSN 02649993,
  [Link](https://linkinghub.elsevier.com/retrieve/pii/S0264999314004143),
  [Document](https://dx.doi.org/10.1016/j.econmod.2014.10.050)
  Cited by: [§1](https://arxiv.org/html/2602.18572v1#S1.p1.1 "1 Introduction ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§2](https://arxiv.org/html/2602.18572v1#S2.p1.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [43]
  A. S. Rashad and M. Farghally (2024-08)
  The US monetary conditions and Dubai’s real estate market: twist or tango?.
  International Journal of Housing Markets and Analysis 17 (5),  pp. 1225–1242 (en).
  External Links: ISSN 1753-8270, 1753-8270,
  [Link](http://www.emerald.com/ijhma/article/17/5/1225-1242/1225266),
  [Document](https://dx.doi.org/10.1108/IJHMA-03-2023-0035)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p1.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [44]
  N. Reimers and I. Gurevych (2019)
  Sentence-BERT: sentence embeddings using siamese BERT-networks.
  External Links: 1908.10084,
  [Link](https://arxiv.org/abs/1908.10084)
  Cited by: [§3.1.2](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS2.p2.8 "3.1.2 News-Based Sentiment ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [45]
  S. Seabold and J. Perktold (2010)
  Statsmodels: econometric and statistical modeling with python.
  SciPy 2010.
  External Links: [Document](https://dx.doi.org/10.25080/Majora-92bf1922-011),
  [Link](https://doi.org/10.25080/Majora-92bf1922-011)
  Cited by: [§3.2.3](https://arxiv.org/html/2602.18572v1#S3.SS2.SSS3.p1.1.3 "3.2.3 Training and Implementation ‣ 3.2 Forecasting Framework ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [46]
  A. Semenzato, S. E. Pappalardo, D. Codato, U. Trivelloni, S. De Zorzi, S. Ferrari, M. De Marchi, and M. Massironi (2020-06)
  Mapping and Monitoring Urban Environment through Sentinel-1 SAR Data: A Case Study in the Veneto Region (Italy).
  ISPRS International Journal of Geo-Information 9 (6),  pp. 375 (en).
  External Links: ISSN 2220-9964,
  [Link](https://www.mdpi.com/2220-9964/9/6/375),
  [Document](https://dx.doi.org/10.3390/ijgi9060375)
  Cited by: [§1](https://arxiv.org/html/2602.18572v1#S1.p6.1 "1 Introduction ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§2](https://arxiv.org/html/2602.18572v1#S2.p4.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§3.1.3](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS3.p1.5 "3.1.3 Satellite SAR Features ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [47]
  S. C. K. Tekouabou, Ş. C. Gherghina, E. D. Kameni, Y. Filali, and K. I. Gartoumi (2024)
  AI-based on machine learning methods for urban real estate prediction: a systematic survey.
  Archives of Computational Methods in Engineering 31 (2),  pp. 1079–1095.
  External Links: [Document](https://dx.doi.org/10.1007/s11831-023-10010-5)
  Cited by: [§1](https://arxiv.org/html/2602.18572v1#S1.p2.1 "1 Introduction ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§2](https://arxiv.org/html/2602.18572v1#S2.p2.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [48]
  R. Torres, P. Snoeij, D. Geudtner, D. Bibby, M. Davidson, E. Attema, P. Potin, B. Rommen, N. Floury, M. Brown, I. N. Traver, P. Deghaye, B. Duesmann, B. Rosich, N. Miranda, C. Bruno, M. L’Abbate, R. Croci, A. Pietropaolo, M. Huchler, and F. Rostan (2012-05)
  GMES Sentinel-1 mission.
  Remote Sensing of Environment 120,  pp. 9–24 (en).
  External Links: ISSN 00344257,
  [Link](https://linkinghub.elsevier.com/retrieve/pii/S0034425712000600),
  [Document](https://dx.doi.org/10.1016/j.rse.2011.05.028)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p4.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§3.1.3](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS3.p1.5 "3.1.3 Satellite SAR Features ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§4.3.2](https://arxiv.org/html/2602.18572v1#S4.SS3.SSS2.p1.6 "4.3.2 Urban Environment: SAR versus Optical Indices ‣ 4.3 Alternative Representations of Sentiment and Built Environment ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [49]
  Y. Uygun and E. Sefer (2025-10)
  Financial asset price prediction with graph neural network-based temporal deep learning models.
  Neural Computing and Applications 37 (30),  pp. 25445–25471.
  External Links: ISSN 1433-3058,
  [Link](https://doi.org/10.1007/s00521-025-11586-8),
  [Document](https://dx.doi.org/10.1007/s00521-025-11586-8)
  Cited by: [§5](https://arxiv.org/html/2602.18572v1#S5.p3.1 "5 Conclusion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [50]
  A. Verma, A. Bhattacharya, S. Dey, C. López-Martínez, and P. Gamba (2023-09)
  Built-up area mapping using Sentinel-1 SAR data.
  ISPRS Journal of Photogrammetry and Remote Sensing 203,  pp. 55–70 (en).
  External Links: ISSN 09242716,
  [Link](https://linkinghub.elsevier.com/retrieve/pii/S0924271623002009),
  [Document](https://dx.doi.org/10.1016/j.isprsjprs.2023.07.019)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p4.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment"),
  [§3.1.3](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS3.p1.5 "3.1.3 Satellite SAR Features ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [51]
  J. Vonlanthen (2023)
  Interest rates and real estate prices: a panel study.
  Swiss Journal of Economics and Statistics 159 (1),  pp. 6.
  Cited by: [§3.1.4](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS4.p1.1 "3.1.4 Interest Rates ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [52]
  S. Wang, Y. Sun, F. Chen, L. Wang, N. Ramakrishnan, C. Lu, and Y. Chen (2025-06)
  HouseTS: A Large-Scale, Multimodal Spatiotemporal U.S. Housing Dataset.
   arXiv (en).
  Note: arXiv:2506.00765 [cs]
  External Links: [Link](http://arxiv.org/abs/2506.00765),
  [Document](https://dx.doi.org/10.48550/arXiv.2506.00765)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p2.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [53]
  W. Wang, F. Wei, L. Dong, H. Bao, N. Yang, and M. Zhou (2020)
  MiniLM: deep self-attention distillation for task-agnostic compression of pre-trained transformers.
  External Links: 2002.10957,
  [Link](https://arxiv.org/abs/2002.10957)
  Cited by: [§3.1.2](https://arxiv.org/html/2602.18572v1#S3.SS1.SSS2.p2.8 "3.1.2 News-Based Sentiment ‣ 3.1 Datasets and Feature Constructions ‣ 3 Methods ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [54]
  T. Xu, Y. Zhao, and J. Yu (2025-01)
  A Real Estate Price Index Forecasting Scheme Based on Online News Sentiment Analysis.
  Systems 13 (1),  pp. 42 (en).
  External Links: ISSN 2079-8954,
  [Link](https://www.mdpi.com/2079-8954/13/1/42),
  [Document](https://dx.doi.org/10.3390/systems13010042)
  Cited by: [§2](https://arxiv.org/html/2602.18572v1#S2.p3.1 "2 Related Work ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [55]
  Y. Zha, J. Gao, and S. Ni (2003-01)
  Use of normalized difference built-up index in automatically mapping urban areas from TM imagery.
  International Journal of Remote Sensing 24 (3),  pp. 583–594 (en).
  External Links: ISSN 0143-1161, 1366-5901,
  [Link](https://www.tandfonline.com/doi/full/10.1080/01431160304987),
  [Document](https://dx.doi.org/10.1080/01431160304987)
  Cited by: [§4.3.2](https://arxiv.org/html/2602.18572v1#S4.SS3.SSS2.p1.6 "4.3.2 Urban Environment: SAR versus Optical Indices ‣ 4.3 Alternative Representations of Sentiment and Built Environment ‣ 4 Results and Discussion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").
* [56]
  W. Zhang, H. Liu, L. Zha, H. Zhu, J. Liu, D. Dou, and H. Xiong (2021-08)
  MugRep: A Multi-Task Hierarchical Graph Representation Learning Framework for Real Estate Appraisal.
  In Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining,
   pp. 3937–3947 (en).
  Note: arXiv:2107.05180 [cs]
  External Links: [Link](http://arxiv.org/abs/2107.05180),
  [Document](https://dx.doi.org/10.1145/3447548.3467187)
  Cited by: [§5](https://arxiv.org/html/2602.18572v1#S5.p3.1 "5 Conclusion ‣ Sub-City Real Estate Price Index Forecasting at Weekly Horizons Using Satellite Radar and News Sentiment").