---
authors:
- Mohammad Al Ridhawi
- Mahtab Haj Ali
- Hussein Al Osman
doc_id: arxiv:2603.05917v1
family_id: arxiv:2603.05917
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: This work has been submitted to IEEE Access for possible publication. Stock
  Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment
  Analysis
url_abs: http://arxiv.org/abs/2603.05917v1
url_html: https://arxiv.org/html/2603.05917v1
venue: arXiv q-fin
version: 1
year: 2026
---


Mohammad Al Ridhawi, Mahtab Haj Ali, and Hussein Al Osman

###### Abstract

Stock market prediction presents considerable challenges for investors, financial institutions, and policymakers operating in complex market environments characterized by noise, non-stationarity, and behavioral dynamics. Traditional forecasting methods, including fundamental analysis and technical indicators, often fail to capture the intricate patterns and cross-sectional dependencies inherent in financial markets. This paper presents an integrated framework combining a node transformer architecture with Bidirectional Encoder Representations from Transformers (BERT) based sentiment analysis for stock price forecasting. The proposed model represents the stock market as a graph structure where individual stocks form nodes and edges capture relationships including sectoral affiliations, correlated price movements, and supply chain connections. A fine-tuned BERT model extracts sentiment information from social media posts and combines it with quantitative market features through attention-based fusion mechanisms. The node transformer processes historical market data while capturing both temporal evolution and cross-sectional dependencies among stocks. Experiments conducted on 20 S&P 500 stocks spanning January 1982 to March 2025 demonstrate that the integrated model achieves a mean absolute percentage error (MAPE) of 0.80% for one-day-ahead predictions, compared to 1.20% for ARIMA and 1.00% for LSTM. The inclusion of sentiment analysis reduces prediction error by 10% overall and 25% during earnings announcements, while the graph-based architecture contributes an additional 15% improvement by capturing inter-stock dependencies. Directional accuracy reaches 65% for one-day forecasts. Statistical validation through paired t-tests confirms the significance of these improvements (p<0.05p<0.05 for all comparisons). The model demonstrates robustness during high-volatility periods, maintaining MAPE below 1.5% where baseline models exceed 2%.

## I Introduction

Stock price forecasting represents a fundamental challenge in quantitative finance with substantial implications for portfolio management, risk assessment, and capital allocation [[1](#bib.bib1)]. The task of predicting stock market movements is complicated by several interconnected factors: non-stationary price dynamics, high-dimensional feature spaces, complex inter-stock dependencies, and the influence of investor psychology on market behavior.

### I-A Challenges in Stock Price Forecasting

A primary challenge in financial forecasting is the presence of noise and irregularities in market data. Microstructure noise, arising from bid-ask bounces and discrete price movements, significantly impacts short-term price observations [[2](#bib.bib2)]. Random fluctuations that do not reflect fundamental changes in asset value can obscure meaningful signals, complicating model training and evaluation. The efficient market hypothesis posits that stock prices incorporate all available information, suggesting that consistently outperforming market benchmarks through prediction is theoretically difficult [[1](#bib.bib1)]. Empirical evidence indicates partial efficiency, with information incorporated into prices at varying speeds depending on asset liquidity, market conditions, and information type [[3](#bib.bib3), [4](#bib.bib4)].

Behavioral factors introduce additional complexity. Investor sentiment and cognitive biases lead to market movements not easily explained by quantitative fundamentals alone [[5](#bib.bib5)]. Fear, greed, and herd behavior drive price fluctuations in patterns that resist traditional modeling approaches. These behavioral dynamics manifest particularly during market stress, when correlations among assets increase and volatility clusters temporally.

The regulatory environment compounds these difficulties. Shifts in financial regulations, monetary policy, and fiscal interventions can trigger sudden market movements that invalidate learned patterns. The 2008 financial crisis and 2020 pandemic response demonstrated how policy actions create discontinuities in price dynamics that historical models may not anticipate.

### I-B Existing Approaches

Current approaches to stock price forecasting span multiple methodological traditions. Fundamental analysis evaluates company financial health and market position to estimate intrinsic value [[6](#bib.bib6)]. Technical analysis examines historical price and volume patterns to identify trading signals. Machine learning methods, including support vector machines and ensemble methods, apply algorithms to discover patterns in feature-engineered datasets [[2](#bib.bib2)].

Deep learning architectures have demonstrated particular promise in capturing temporal dependencies. Recurrent neural networks, especially Long Short-Term Memory (LSTM) networks, model sequential data through gating mechanisms that address vanishing gradient problems [[7](#bib.bib7)]. While effective for short-to-medium range dependencies, LSTMs process sequences step by step, which limits their ability to capture interactions between distant time steps efficiently. The transformer architecture [[8](#bib.bib8)] overcomes this limitation through self-attention mechanisms that relate all positions in a sequence directly, enabling explicit modeling of long-range dependencies without recurrent connections. In parallel, graph neural networks have emerged to address a different shortcoming: the inability of standard sequence models to represent relationships between entities [[9](#bib.bib9)]. The node transformer architecture bridges these two lines of work by combining attention mechanisms with graph structure, learning contextualized node representations through attention applied over graph neighborhoods [[10](#bib.bib10)].

### I-C Research Motivation and Contributions

These advances notwithstanding, the literature reveals persistent shortcomings. Few approaches combine graph-based modeling of inter-stock relationships with transformer architectures for temporal modeling. The integration of unstructured textual data, particularly social media sentiment, with structured numerical data remains limited. Performance often deteriorates during volatile market conditions, with accuracy varying substantially between stable and turbulent periods.

This paper presents an integrated framework addressing these gaps through multiple coordinated components:

1. 1.

   A node transformer architecture adapted for stock price forecasting that represents the market as a dynamic graph with learnable edge weights. The model captures interdependencies among stocks including sectoral relationships, correlated price movements, and supply chain connections while processing multivariate stock-level inputs.
2. 2.

   Integration of Bidirectional Encoder Representations from Transformers (BERT)-based sentiment analysis through multimodal fusion, enabling incorporation of qualitative market sentiment alongside quantitative price and volume data. Sentiment information extracted from social media posts is incorporated as additional features for each stock node.
3. 3.

   An attention-based fusion mechanism that dynamically weights price-based features and sentiment signals based on current market conditions and volatility indicators.
4. 4.

   A comprehensive dataset comprising historical prices for 20 S&P 500 companies from January 1982 to March 2025, augmented with sentiment scores derived from social media posts from 2007 onward.
5. 5.

   Extensive experimental validation across different market conditions, prediction horizons, and volatility regimes, with statistical tests confirming significance of performance improvements.

The remainder of this paper is organized as follows. Section [II](#S2 "II Literature Review ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") reviews related work. Section [III](#S3 "III Datasets and Preprocessing ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") describes datasets and preprocessing. Section [IV](#S4 "IV Methodology ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") presents the methodology. Section [V](#S5 "V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") reports experimental results. Section [VI](#S6 "VI Discussion ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") discusses findings and limitations. Section [VII](#S7 "VII Conclusion ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") concludes and outlines future directions.

## II Literature Review

Stock price forecasting has evolved through statistical modeling, machine learning, and deep learning paradigms, each offering distinct trade-offs between interpretability, capacity, and data requirements. The following subsections trace this progression and identify the gaps that motivate the present work.

### II-A Statistical Methods

Autoregressive Integrated Moving Average (ARIMA) models remain widely used due to their capacity to capture linear temporal dependencies and interpretable coefficient structures. ARIMA combines autoregressive (AR) and moving average (MA) components after differencing to achieve stationarity. The ARIMA(p,d,q)(p,d,q) model is specified as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(B)​(1−B)d​Xt=θ​(B)​ϵt\phi(B)(1-B)^{d}X\_{t}=\theta(B)\epsilon\_{t} |  | (1) |

where BB is the backshift operator such that B​Xt=Xt−1BX\_{t}=X\_{t-1}, ϕ​(B)=1−ϕ1​B−⋯−ϕp​Bp\phi(B)=1-\phi\_{1}B-\cdots-\phi\_{p}B^{p} is the AR polynomial of order pp, θ​(B)=1+θ1​B+⋯+θq​Bq\theta(B)=1+\theta\_{1}B+\cdots+\theta\_{q}B^{q} is the MA polynomial of order qq, dd is the differencing order, and ϵt∼𝒩​(0,σ2)\epsilon\_{t}\sim\mathcal{N}(0,\sigma^{2}) is white noise.

Low and Sakk [[11](#bib.bib11)] compared ARIMA and LSTM networks for stock prediction across ten exchange-traded funds, finding that ARIMA demonstrates comparable accuracy to LSTM for longer-term predictions. Wahyudi [[12](#bib.bib12)] applied ARIMA to Indonesian stock prices, demonstrating effectiveness for short-term volatility prediction with model selection via the Akaike Information Criterion (AIC).

Vector Autoregression (VAR) extends univariate ARIMA to multivariate settings, modeling each variable as a linear function of its own lags and lags of other variables. However, ARIMA and VAR are limited in handling nonlinear dynamics, regime shifts, and high-dimensional interactions.

### II-B Classical Machine Learning

Support Vector Machines (SVM), k-Nearest Neighbors (KNN), and ensemble methods leverage engineered features for prediction. Nayak et al. [[13](#bib.bib13)] developed a hybrid SVM-KNN model for Indian stock market indices, outperforming individual models in mean squared error. Siddique and Panda [[14](#bib.bib14)] combined kernel Principal Component Analysis (PCA) with Support Vector Regression (SVR) and teaching-learning-based optimization, achieving improved accuracy through dimension reduction.

Basak et al. [[15](#bib.bib15)] applied XGBoost for long-term stock price forecasting using technical indicators, achieving F-scores ranging from 0.82 to 0.97 for 60-day and 90-day prediction horizons on Apple and Yahoo stocks. While effective for specific tasks, these methods rely heavily on feature engineering and often struggle to generalize across different market regimes.

### II-C Deep Learning Methods

#### II-C1 Convolutional Neural Networks

Convolutional Neural Networks (CNNs) extract hierarchical patterns from structured data through local receptive fields and parameter sharing. Chandar [[16](#bib.bib16)] proposed TI-CNN, converting technical indicators into images using Gramian Angular Fields before CNN processing. Wen et al. [[17](#bib.bib17)] applied CNNs to S&P 500 data, exploiting spatial structure in time series representations. CNNs capture local dependencies effectively but are less suited for modeling long-range temporal dynamics.

#### II-C2 Recurrent Neural Networks

Recurrent Neural Networks (RNNs), particularly LSTM networks and Gated Recurrent Units (GRU), model sequential data through hidden states that propagate information across time steps. LSTM networks incorporate input, forget, and output gates to control information flow, addressing the vanishing gradient problem inherent in standard RNNs.

Di Persio and Honchar [[18](#bib.bib18)] compared RNN variants for Google stock prediction, with LSTM achieving 72% directional accuracy, outperforming standard RNN and GRU architectures. Hossain et al. [[19](#bib.bib19)] applied cascaded LSTM-GRU to S&P 500 data spanning 1950-2016, achieving mean squared error of 0.00098. Bidirectional LSTM extends this by processing sequences in both directions. Xu et al. [[20](#bib.bib20)] integrated wavelet transform, stacked autoencoder, and BiLSTM for stock forecasting. Liu et al. [[21](#bib.bib21)] employed autoencoder-based feature extraction with BiLSTM for price series prediction.

### II-D Graph Neural Networks

Graph Neural Networks (GNNs) capture interdependencies by modeling markets as graphs where nodes represent companies and edges represent relationships such as sectoral ties, price correlations, or supply chain connections.

Chen et al. [[22](#bib.bib22)] proposed a graph convolutional feature-based CNN model combining graph convolutional networks with dual CNNs to capture market-level and stock-level features simultaneously. Testing on Chinese stocks demonstrated superior performance compared to non-graph approaches. Wang et al. [[23](#bib.bib23)] introduced a multi-graph convolutional neural network defining both static and dynamic correlation graphs. Testing on 42 Chinese market indices showed average prediction error reduction of 5.11% compared to LSTM and attention-based baselines.

### II-E Transformer Models

The transformer architecture [[8](#bib.bib8)] introduced a fundamentally different approach to sequence-to-sequence modeling. Self-attention mechanisms compute pairwise interactions between all positions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Attention​(𝐐,𝐊,𝐕)=softmax​(𝐐𝐊Tdk)​𝐕\text{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V})=\text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^{T}}{\sqrt{d\_{k}}}\right)\mathbf{V} |  | (2) |

where 𝐐\mathbf{Q}, 𝐊\mathbf{K}, 𝐕\mathbf{V} are query, key, and value matrices, and dkd\_{k} is the key dimension. The scaling factor dk\sqrt{d\_{k}} prevents dot products from growing large in magnitude.

Multi-head attention extends this by projecting queries, keys, and values multiple times with different learned projections:

|  |  |  |  |
| --- | --- | --- | --- |
|  | MultiHead​(𝐐,𝐊,𝐕)=Concat​(head1,…,headh)​𝐖O\text{MultiHead}(\mathbf{Q},\mathbf{K},\mathbf{V})=\text{Concat}(\text{head}\_{1},\ldots,\text{head}\_{h})\mathbf{W}^{O} |  | (3) |

where headi=Attention​(𝐐𝐖iQ,𝐊𝐖iK,𝐕𝐖iV)\text{head}\_{i}=\text{Attention}(\mathbf{Q}\mathbf{W}\_{i}^{Q},\mathbf{K}\mathbf{W}\_{i}^{K},\mathbf{V}\mathbf{W}\_{i}^{V}).

Li and Qian [[24](#bib.bib24)] developed a financial transformer processing multiple timeframes simultaneously, improving sensitivity to regime changes. The node transformer [[10](#bib.bib10)] extends attention to graph-structured data, learning contextualized node representations through attention over graph neighborhoods.

### II-F Hybrid Models and Research Gaps

Hybrid models seek to integrate complementary architectural strengths by pairing spatial feature extractors with sequential learners. Lu et al. [[25](#bib.bib25)] proposed a CNN-BiLSTM-attention model that uses convolutional layers to extract local patterns, feeds them into a bidirectional LSTM for temporal modeling, and applies attention to weight the most informative time steps, outperforming standalone approaches on multiple benchmarks. These composite designs show particular promise during volatile periods, where the diversity of learned representations confers robustness that single-paradigm models lack.

Despite progress along each of these fronts, critical gaps persist at their intersections. Few approaches combine graph-based inter-stock modeling with transformer temporal processing. Integration of unstructured text with structured numerical data remains limited. Performance often deteriorates during volatile conditions, with accuracy varying by 40% between stable and turbulent periods [[11](#bib.bib11)]. Computational demands present barriers to real-time deployment.

These gaps motivate the present work: an integrated node transformer with BERT-based sentiment analysis, capturing both stock interconnections and long-range dependencies while incorporating sentiment as a predictive signal.

## III Datasets and Preprocessing

### III-A Financial Market Dataset

The Financial Market Dataset (FMD) integrates historical stock market data with engineered technical indicators. The dataset spans January 1, 1982 to March 31, 2025, covering twenty companies from the S&P 500 index selected for sectoral diversity, market capitalization variation, and data availability.

The selected companies span multiple sectors: technology (Apple, Microsoft, Salesforce, Netflix), financial services (JPMorgan Chase, Visa), healthcare (Johnson & Johnson, UnitedHealth Group, Pfizer), retail (Walmart, Home Depot, McDonald’s), energy (ExxonMobil, Chevron), consumer goods (Procter & Gamble, Coca-Cola, Nike), telecommunications (Verizon), and industrials (Boeing, Caterpillar). For companies with initial public offerings after 1982, data collection begins at the first available trading date. For example, Salesforce data begins in June 2004 following its IPO. The effective analysis period for each stock corresponds to its available trading history within the 1982-2025 window. This cross-sectional design ensures the dataset reflects behavior across multiple industries and economic cycles, though the selection of current index constituents introduces survivorship bias that is acknowledged in Section [VI](#S6 "VI Discussion ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis").

For each company, six daily Open, High, Low, Close, and Volume (OHLCV) trading variables were collected: opening price (OtO\_{t}), highest price (HtH\_{t}), lowest price (LtL\_{t}), closing price (CtC\_{t}), adjusted closing price (CtadjC\_{t}^{\text{adj}}), and trading volume (VtV\_{t}). Technical indicators were computed following established methodologies [[20](#bib.bib20), [16](#bib.bib16)]:

Simple Moving Average (SMA): The SMA smooths short-term price fluctuations to reveal underlying trends. Computing it at multiple window lengths (n∈{5,10,20}n\in\{5,10,20\} days) allows the model to distinguish short-term momentum from longer-term directional shifts:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SMAn​(t)=1n​∑i=0n−1Ct−i\text{SMA}\_{n}(t)=\frac{1}{n}\sum\_{i=0}^{n-1}C\_{t-i} |  | (4) |

Exponential Moving Average (EMA): Unlike the SMA, the EMA assigns greater weight to recent observations through an exponential decay controlled by smoothing factor α=2/(n+1)\alpha=2/(n+1). This makes it more responsive to recent price changes, which is valuable for detecting early trend reversals:

|  |  |  |  |
| --- | --- | --- | --- |
|  | EMAn​(t)=α⋅Ct+(1−α)⋅EMAn​(t−1)\text{EMA}\_{n}(t)=\alpha\cdot C\_{t}+(1-\alpha)\cdot\text{EMA}\_{n}(t-1) |  | (5) |

Relative Strength Index (RSI): The RSI is a bounded momentum oscillator that measures the speed and magnitude of recent price changes on a scale from 0 to 100. Values above 70 typically indicate overbought conditions, while values below 30 suggest oversold conditions. It is computed using a 14-day window:

|  |  |  |  |
| --- | --- | --- | --- |
|  | RSI​(t)=100−1001+G¯14​(t)L¯14​(t)\text{RSI}(t)=100-\frac{100}{1+\frac{\overline{G}\_{14}(t)}{\overline{L}\_{14}(t)}} |  | (6) |

where G¯14​(t)\overline{G}\_{14}(t) and L¯14​(t)\overline{L}\_{14}(t) are the average gains and average losses over the preceding 14 trading days.

Moving Average Convergence Divergence (MACD): The MACD captures changes in trend strength and direction by measuring the difference between a short-term (12-day) and a long-term (26-day) EMA. A positive MACD indicates upward momentum, while a negative value signals downward pressure. Crossovers between the MACD and its 9-day signal line are commonly used as trade triggers:

|  |  |  |  |
| --- | --- | --- | --- |
|  | MACD​(t)=EMA12​(t)−EMA26​(t)\text{MACD}(t)=\text{EMA}\_{12}(t)-\text{EMA}\_{26}(t) |  | (7) |

with 9-day signal line Signal​(t)=EMA9​(MACD​(t))\text{Signal}(t)=\text{EMA}\_{9}(\text{MACD}(t)).

Daily Returns and Log Returns: Daily returns quantify the relative price change between consecutive trading days and serve as the primary measure of stock performance. Log returns are included alongside arithmetic returns because they are additive over time and more closely approximate a normal distribution, properties that benefit gradient-based optimization:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=Ct−Ct−1Ct−1,rtlog=ln⁡(CtCt−1)r\_{t}=\frac{C\_{t}-C\_{t-1}}{C\_{t-1}},\quad r\_{t}^{\log}=\ln\left(\frac{C\_{t}}{C\_{t-1}}\right) |  | (8) |

Rolling Volatility: Rolling volatility measures the dispersion of returns over a trailing 20-day window, providing a real-time estimate of price uncertainty. Higher volatility indicates greater risk and wider expected price ranges, which is critical for the model’s gating mechanism to adjust feature emphasis across market regimes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σt=119​∑i=019(rt−i−r¯t)2\sigma\_{t}=\sqrt{\frac{1}{19}\sum\_{i=0}^{19}(r\_{t-i}-\bar{r}\_{t})^{2}} |  | (9) |

Missing values were addressed through a temporally-aware imputation strategy designed to prevent information leakage. During training data preparation, short gaps (1-2 trading days) used linear interpolation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct=Ct−k+Ct+m−Ct−kk+m⋅kC\_{t}=C\_{t-k}+\frac{C\_{t+m}-C\_{t-k}}{k+m}\cdot k |  | (10) |

where kk and mm are distances to nearest observed values. For validation and test data, only forward-filling from the most recent observed value was applied to ensure no future information leaked into predictions: Ct=Ct−kC\_{t}=C\_{t-k} where kk is the distance to the most recent observation. Longer gaps in training data also employed forward filling. Each observation contains 6 raw variables and 11 derived indicators.

Feature normalization used an expanding window z-score approach to prevent look-ahead bias. For each feature xi,tx\_{i,t}, the normalized value was computed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x~i,t=xi,t−μ1:tσ1:t\tilde{x}\_{i,t}=\frac{x\_{i,t}-\mu\_{1:t}}{\sigma\_{1:t}} |  | (11) |

where μ1:t\mu\_{1:t} and σ1:t\sigma\_{1:t} are the mean and standard deviation computed over all available data from the start of the training period up to time tt. For test data, normalization statistics were fixed using the full training set, ensuring no information from the test period influenced the standardization.

Fig. [1](#S3.F1 "Figure 1 ‣ III-A Financial Market Dataset ‣ III Datasets and Preprocessing ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") illustrates the feature engineering pipeline.

Raw OHLCVDataSMA5, 10, 20EMA5, 10, 20RSI, MACDReturnsRollingVolatilityZ-ScoreNormalizationFeature Vector𝐱i,t∈ℝ17\mathbf{x}\_{i,t}\in\mathbb{R}^{17}


Figure 1: Feature engineering pipeline. Raw OHLCV data is processed through multiple technical indicator computations, normalized using z-score standardization, and concatenated into the final feature vector.

### III-B Sentiment Datasets

The sentiment component relies on two complementary datasets that together capture both benchmark-labeled sentiment and large-scale real-world social media activity. The first provides expert-annotated ground truth for training the BERT classifier, while the second supplies the raw social media text processed at inference time.

The Market Sentiment Evaluation (MSE) dataset is a publicly available corpus containing finance-related messages from social media platforms [[26](#bib.bib26)]. Each message has been annotated by financial experts with sentiment scores s∈[−1,+1]s\in[-1,+1], where −1-1 indicates strongly negative, 0 neutral, and +1+1 strongly positive sentiment. The dataset includes source platform identifiers, message IDs, relevant cashtags, and annotated sentiment spans. Because it contains human-labeled ground truth, the MSE dataset serves as the primary training and validation resource for fine-tuning the BERT sentiment module.

The Comprehensive Stock Sentiment (CSS) dataset was constructed using the X (formerly Twitter) API through systematic searches for the cashtag corresponding to each of the twenty stocks listed in Table [I](#S3.T1 "TABLE I ‣ III-B Sentiment Datasets ‣ III Datasets and Preprocessing ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis"). Since the platform was founded in 2006, the CSS dataset covers January 2007 to March 2025, yielding approximately 4.2 million posts across all stocks.

TABLE I: Search tags used for CSS dataset collection.

| Cashtag | Company | Cashtag | Company |
| --- | --- | --- | --- |
| $AAPL | Apple | $KO | Coca-Cola |
| $MSFT | Microsoft | $CVX | Chevron |
| $JPM | JPMorgan Chase | $HD | Home Depot |
| $JNJ | Johnson & Johnson | $VZ | Verizon |
| $WMT | Walmart | $BA | Boeing |
| $XOM | ExxonMobil | $MCD | McDonald’s |
| $PG | Procter & Gamble | $NFLX | Netflix |
| $V | Visa | $CAT | Caterpillar |
| $UNH | UnitedHealth Group | $PFE | Pfizer |
| $NKE | Nike | $CRM | Salesforce |

Once the BERT model is fine-tuned on the MSE labels, it is applied to the CSS corpus to generate daily sentiment scores for each stock. These scores are then aggregated at multiple time scales and fed into the node transformer as additional input features.

Both datasets underwent identical preprocessing before entering the sentiment pipeline. This included removal of HTML encodings and special characters, anonymization of user identifiers, removal of retweet markers, URL standardization with placeholder tags, de-elongation of exaggerated words (e.g., “victoryyyyy” →\rightarrow “victory”), spacing correction for ticker symbols (e.g., “$ AAPL” →\rightarrow “$AAPL”), and ordinal expression normalization.

### III-C Dataset Partitioning

Temporal splits were applied to prevent look-ahead bias. The training set comprises January 1, 1982 to December 31, 2010 (70% of temporal range). The validation set spans January 1, 2011 to December 31, 2016 (15%). The test set covers January 1, 2017 to March 31, 2025 (15%).

For sentiment data, partitioning aligns with financial splits for the overlapping period. Since X (formerly Twitter) data begins in 2007, the sentiment training period covers January 2007 to December 2010. For pre-2007 financial data, sentiment features are set to neutral (zero). The sentiment integration component is primarily evaluated on the test set (2017-2025) where sentiment data is abundant.

The MSE dataset used for BERT fine-tuning is partitioned separately into 70% training, 15% validation, and 15% test, stratified by sentiment class to preserve label distribution. The BERT model is fine-tuned and evaluated on this split independently before its outputs are integrated into the full forecasting pipeline (see Section [V-D](#S5.SS4 "V-D Sentiment Model Evaluation ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis")). Table [II](#S3.T2 "TABLE II ‣ III-C Dataset Partitioning ‣ III Datasets and Preprocessing ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") summarizes the key characteristics of the financial and sentiment datasets.

TABLE II: Dataset summary statistics.

| Characteristic | FMD | CSS |
| --- | --- | --- |
| Time period | 1982-2025 | 2007-2025 |
| Number of stocks | 20 | 20 |
| Trading days | ≈\approx10,300 | ≈\approx4,100 |
| Features per stock-day | 17 | 3 |
| Total observations | ≈\approx206,000 | ≈\approx4.2M posts |

## IV Methodology

The proposed framework integrates a node transformer architecture with BERT-based sentiment analysis, combining quantitative financial indicators with qualitative textual signals. The design follows a modular structure in which the graph-based transformer and the sentiment pipeline operate as independent components, coupled through an attention-based fusion layer that dynamically adjusts the relative weighting of each stream based on current market conditions.

### IV-A System Architecture Overview

Fig. [2](#S4.F2 "Figure 2 ‣ IV-A System Architecture Overview ‣ IV Methodology ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") presents the overall system architecture. The framework processes historical market data and sentiment information through two parallel pathways. The quantitative branch normalizes all market features (price, volume, and technical indicators), constructs the graph structure, applies temporal encoding, and feeds the processed representations into the node transformer. The qualitative branch passes social media text through the BERT encoder and aggregates sentiment scores at multiple time scales. The two streams converge at an attention-based fusion layer that produces the final price prediction.

Market Data: Price 𝐩i,t\mathbf{p}\_{i,t}, Volume vi,tv\_{i,t}, Technical Indicators 𝐈i,t\mathbf{I}\_{i,t}Social MediaPostsZ-ScoreNormalizationGraphConstructionTemporalEncodingBERTEncoderNode Transformer(6 Layers, 8 Heads)SentimentAggregationAttention-BasedMultimodal FusionPrice Predictiony^i,t+h\hat{y}\_{i,t+h}

Figure 2: System architecture. Price data, volume, and technical indicators are jointly processed through normalization, graph construction, and temporal encoding before the node transformer. Social media posts are processed through BERT and sentiment aggregation. Both streams combine through attention-based multimodal fusion.

### IV-B Graph Representation of the Stock Market

The stock market is represented as a graph 𝒢=(𝒱,ℰ,𝐄)\mathcal{G}=(\mathcal{V},\mathcal{E},\mathbf{E}) where 𝒱={1,…,N}\mathcal{V}=\{1,\ldots,N\} is the set of N=20N=20 stock nodes, ℰ⊆𝒱×𝒱\mathcal{E}\subseteq\mathcal{V}\times\mathcal{V} is the edge set (fully connected), and 𝐄∈ℝN×N\mathbf{E}\in\mathbb{R}^{N\times N} is the edge weight matrix. The choice of N=20N=20 nodes balances computational tractability with sufficient cross-sectional coverage to capture major sector interactions. While larger graphs might better represent full market topology, the current design enables deep temporal analysis (252-day input sequences) across diverse sectors. The fully-connected structure with learnable edge weights ensures all pairwise relationships can be discovered during training. Ablation results (Section [V-E](#S5.SS5 "V-E Results ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis")) confirm that the graph structure contributes meaningful predictive improvement over models without explicit inter-stock connections.

Edge weights are initialized based on sector relationships and historical price correlations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ei​j(0)=α⋅δsector​(i,j)+(1−α)⋅max⁡(0,ρi​j)e\_{ij}^{(0)}=\alpha\cdot\delta\_{\text{sector}}(i,j)+(1-\alpha)\cdot\max(0,\rho\_{ij}) |  | (12) |

where δsector​(i,j)=1\delta\_{\text{sector}}(i,j)=1 if stocks ii and jj share the same Global Industry Classification Standard (GICS) sector classification and 0 otherwise, ρi​j\rho\_{ij} is the Pearson correlation coefficient between daily returns computed over the training period, max⁡(0,⋅)\max(0,\cdot) ensures non-negative weights, and α=0.5\alpha=0.5 balances sector and correlation information.

During training, edge weights are refined iteratively:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ei​j(ℓ+1)=σ​(𝐰eT​[𝐡i(ℓ)∥𝐡j(ℓ)]+be)e\_{ij}^{(\ell+1)}=\sigma\left(\mathbf{w}\_{e}^{T}[\mathbf{h}\_{i}^{(\ell)}\|\mathbf{h}\_{j}^{(\ell)}]+b\_{e}\right) |  | (13) |

where σ\sigma is the sigmoid function, 𝐰e∈ℝ2​d\mathbf{w}\_{e}\in\mathbb{R}^{2d} is a learnable weight vector, 𝐡i(ℓ),𝐡j(ℓ)∈ℝd\mathbf{h}\_{i}^{(\ell)},\mathbf{h}\_{j}^{(\ell)}\in\mathbb{R}^{d} are node representations at layer ℓ\ell, ∥\| denotes concatenation, and beb\_{e} is a learnable bias. Edges are undirected: ei​j=ej​ie\_{ij}=e\_{ji}.

### IV-C Node Transformer Architecture

The node transformer extends the standard transformer by incorporating graph-structured relational inductive biases [[10](#bib.bib10)]. Rather than treating each stock’s time series independently, the architecture processes all nodes jointly at each time step, allowing information to propagate across the graph through attention weighted by the learned edge structure described above.

#### IV-C1 Input Representation

Each stock is represented by a composite feature vector that concatenates raw market data, engineered indicators, positional information, and a learned identity embedding. For stock ii at time tt, this vector is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱i,t=[𝐩i,t​‖vi,t‖​𝐈i,t​‖TE​(t)‖​𝐬i]∈ℝdin\mathbf{x}\_{i,t}=[\mathbf{p}\_{i,t}\|v\_{i,t}\|\mathbf{I}\_{i,t}\|\text{TE}(t)\|\mathbf{s}\_{i}]\in\mathbb{R}^{d\_{\text{in}}} |  | (14) |

where 𝐩i,t∈ℝ5\mathbf{p}\_{i,t}\in\mathbb{R}^{5} contains normalized prices (open, high, low, close, adjusted close), vi,t∈ℝv\_{i,t}\in\mathbb{R} is normalized volume, 𝐈i,t∈ℝ11\mathbf{I}\_{i,t}\in\mathbb{R}^{11} contains technical indicators, TE​(t)∈ℝd\text{TE}(t)\in\mathbb{R}^{d} is the temporal encoding, and 𝐬i∈ℝds\mathbf{s}\_{i}\in\mathbb{R}^{d\_{s}} is a learned stock-specific embedding capturing persistent characteristics.

#### IV-C2 Temporal Encoding

Following Vaswani et al. [[8](#bib.bib8)], temporal encoding injects positional information:

|  |  |  |  |
| --- | --- | --- | --- |
|  | TE​(t,2​k)\displaystyle\text{TE}(t,2k) | =sin⁡(t100002​k/d)\displaystyle=\sin\!\left(\frac{t}{10000^{2k/d}}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | TE​(t,2​k+1)\displaystyle\text{TE}(t,2k\!+\!1) | =cos⁡(t100002​k/d)\displaystyle=\cos\!\left(\frac{t}{10000^{2k/d}}\right) |  | (15) |

where tt is the trading day index, k∈{0,…,d/2−1}k\in\{0,\ldots,d/2-1\} is the dimension index, and d=512d=512 is the model dimension. Lower dimensions capture high-frequency patterns; higher dimensions capture low-frequency patterns.

#### IV-C3 Graph-Aware Multi-Head Self-Attention with Causal Masking

The attention mechanism incorporates the learned edge weight matrix 𝐄\mathbf{E} from Section [IV-B](#S4.SS2 "IV-B Graph Representation of the Stock Market ‣ IV Methodology ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") as a structural bias, so that stock pairs with stronger graph connections receive higher baseline attention. Causal masking ensures predictions at time tt use only information from times ≤t\leq t:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐀​(𝐐,𝐊,𝐕)=softmax​(𝐐𝐊Tdk+𝐌+𝐄)​𝐕\mathbf{A}(\mathbf{Q},\mathbf{K},\mathbf{V})=\text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^{T}}{\sqrt{d\_{k}}}+\mathbf{M}+\mathbf{E}\right)\mathbf{V} |  | (16) |

where 𝐐=𝐗𝐖Q\mathbf{Q}=\mathbf{X}\mathbf{W}^{Q}, 𝐊=𝐗𝐖K\mathbf{K}=\mathbf{X}\mathbf{W}^{K}, 𝐕=𝐗𝐖V\mathbf{V}=\mathbf{X}\mathbf{W}^{V} are linear projections, dk=64d\_{k}=64 is the key dimension, 𝐌\mathbf{M} is the causal mask with Ma​b=0M\_{ab}=0 if a≥ba\geq b and Ma​b=−∞M\_{ab}=-\infty otherwise, and 𝐄∈ℝN×N\mathbf{E}\in\mathbb{R}^{N\times N} is the edge weight matrix. The additive graph bias allows content-based attention (via 𝐐𝐊T\mathbf{Q}\mathbf{K}^{T}) and structural priors (via 𝐄\mathbf{E}) to jointly determine how information flows between stocks at each layer.

With H=8H=8 attention heads, each operating in dk=dv=64d\_{k}=d\_{v}=64 dimensions, the total model dimension is dmodel=H×dk=512d\_{\text{model}}=H\times d\_{k}=512. Fig. [3](#S4.F3 "Figure 3 ‣ IV-C3 Graph-Aware Multi-Head Self-Attention with Causal Masking ‣ IV-C Node Transformer Architecture ‣ IV Methodology ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") illustrates the internal structure of a single transformer layer, showing the residual connections, layer normalization, and dropout placement.

Input 𝐗(ℓ)\mathbf{X}^{(\ell)}Multi-Head Self-Attention(8 heads, causal mask)+LayerNormFeed-Forward Networkdf​f=2048d\_{ff}=2048+LayerNormOutput 𝐗(ℓ+1)\mathbf{X}^{(\ell+1)}dropout=0.1dropout=0.1


Figure 3: Single transformer layer architecture. Input passes through multi-head self-attention with residual connection and layer normalization, followed by a position-wise feed-forward network with another residual connection and normalization.

#### IV-C4 Time-Based Feature Gating

A gating mechanism adaptively weights features based on temporal context:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐠i,t=σ​(𝐖g​𝐱i,t+𝐛g)∈(0,1)din\mathbf{g}\_{i,t}=\sigma(\mathbf{W}\_{g}\mathbf{x}\_{i,t}+\mathbf{b}\_{g})\in(0,1)^{d\_{\text{in}}} |  | (17) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱i,t′=𝐠i,t⊙𝐱i,t\mathbf{x}^{\prime}\_{i,t}=\mathbf{g}\_{i,t}\odot\mathbf{x}\_{i,t} |  | (18) |

where 𝐖g∈ℝdin×din\mathbf{W}\_{g}\in\mathbb{R}^{d\_{\text{in}}\times d\_{\text{in}}}, 𝐛g∈ℝdin\mathbf{b}\_{g}\in\mathbb{R}^{d\_{\text{in}}} are learnable parameters, and ⊙\odot denotes element-wise multiplication. This mechanism enables adaptive emphasis on different features during volatile versus stable periods.

#### IV-C5 Feed-Forward Network

Each layer includes a position-wise Feed-Forward Network (FFN):

|  |  |  |  |
| --- | --- | --- | --- |
|  | FFN​(𝐱)=ReLU​(𝐱𝐖1+𝐛1)​𝐖2+𝐛2\text{FFN}(\mathbf{x})=\text{ReLU}(\mathbf{x}\mathbf{W}\_{1}+\mathbf{b}\_{1})\mathbf{W}\_{2}+\mathbf{b}\_{2} |  | (19) |

where 𝐖1∈ℝ512×2048\mathbf{W}\_{1}\in\mathbb{R}^{512\times 2048}, 𝐖2∈ℝ2048×512\mathbf{W}\_{2}\in\mathbb{R}^{2048\times 512}, and 𝐛1,𝐛2\mathbf{b}\_{1},\mathbf{b}\_{2} are biases.

The complete architecture consists of L=6L=6 stacked layers with residual connections and layer normalization after each sub-layer. Dropout with p=0.1p=0.1 is applied for regularization.

### IV-D BERT-Based Sentiment Analysis

The sentiment component employs BERT (bert-base-uncased) with 12 transformer layers, 768 hidden dimensions, and 12 attention heads [[27](#bib.bib27)]. BERT’s bidirectional attention is well suited to financial text, where sentiment often depends on contextual modifiers (e.g., “not bullish” vs. “bullish”) that unidirectional models may miss.

#### IV-D1 Domain Adaptations

A financial domain embedding layer augments the standard BERT token embeddings with additional representations for financial terminology, enabling the model to distinguish domain-specific usage of terms such as “short,” “call,” and “bear” from their everyday meanings. Maximum sequence length is set to 512 tokens, which accommodates the vast majority of social media posts without truncation.

#### IV-D2 Fine-Tuning Process

Fine-tuning on the MSE dataset follows a three-stage progressive unfreezing schedule designed to preserve BERT’s pretrained language representations while adapting the upper layers to financial sentiment classification. In the first stage, the embedding layer and the first 8 transformer blocks are frozen so that only the upper layers and the classification head receive gradient updates; these are trained for 3 epochs with a learning rate of 2×10−52\times 10^{-5} and batch size 32. The second stage progressively unfreezes layers from top to bottom over 5 additional epochs, allowing each block to adapt incrementally to the financial domain without catastrophic forgetting of general language knowledge. In the final stage, all layers are unfrozen and trained jointly with a reduced learning rate of 5×10−65\times 10^{-6} and gradient accumulation over 4 steps to stabilize updates across the full parameter space.

Because sentiment labels in financial text are typically imbalanced, with neutral posts far outnumbering strongly positive or negative ones, focal loss is used instead of standard cross-entropy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒFL​(pt)=−αt​(1−pt)γ​log⁡(pt)\mathcal{L}\_{\text{FL}}(p\_{t})=-\alpha\_{t}(1-p\_{t})^{\gamma}\log(p\_{t}) |  | (20) |

where αt\alpha\_{t} is class weight (inverse frequency), ptp\_{t} is predicted probability for correct class, and γ=2\gamma=2 focuses training on hard examples by down-weighting easily classified instances. Fig. [4](#S4.F4 "Figure 4 ‣ IV-D2 Fine-Tuning Process ‣ IV-D BERT-Based Sentiment Analysis ‣ IV Methodology ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") illustrates the complete sentiment extraction pipeline from raw input to final score.

Raw Tweet: “$AAPL crushing it!”Preprocessing & TokenizationBERT Encoder (12 layers)[CLS] Token PoolingSentiment Score s∈[−1,+1]s\in[-1,+1]


Figure 4: BERT sentiment extraction pipeline. Raw social media posts are preprocessed, tokenized, encoded through BERT, pooled via [CLS] token, and classified to sentiment scores.

### IV-E Integration of Node Transformer and BERT

#### IV-E1 Multi-Scale Sentiment Features

Raw daily sentiment scores are noisy and sensitive to individual posts. To capture both immediate market reactions and sustained sentiment trends, scores are smoothed at multiple time scales before entering the model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐒i,t=[Si,t(1​d),Si,t(5​d),Si,t(20​d)]∈ℝ3\mathbf{S}\_{i,t}=[S\_{i,t}^{(1d)},S\_{i,t}^{(5d)},S\_{i,t}^{(20d)}]\in\mathbb{R}^{3} |  | (21) |

where Si,t(k​d)S\_{i,t}^{(kd)} is the kk-day exponential moving average of sentiment scores for stock ii. This captures both immediate reactions and sustained sentiment trends.

#### IV-E2 Sentiment-Guided Attention

Rather than simply concatenating sentiment as an additional input feature, the model allows sentiment to modulate the attention mechanism itself. Specifically, sentiment scales the key representations so that time steps with strong sentiment signals receive amplified or dampened attention:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐊t′=𝐊t⋅(1+β⋅St)\mathbf{K}^{\prime}\_{t}=\mathbf{K}\_{t}\cdot(1+\beta\cdot S\_{t}) |  | (22) |

where St∈[−1,1]S\_{t}\in[-1,1] is the sentiment score at time tt and β∈ℝ\beta\in\mathbb{R} is a learnable parameter. The attention computation becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐀sent=softmax​(𝐐𝐊′⁣Tdk+𝐌)​𝐕\mathbf{A}\_{\text{sent}}=\text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^{\prime T}}{\sqrt{d\_{k}}}+\mathbf{M}\right)\mathbf{V} |  | (23) |

#### IV-E3 Adaptive Integration

Because the relative predictive value of price-based features and sentiment varies with market conditions, the final prediction is produced by a learned convex combination rather than a fixed weighting. A sigmoid gate dynamically adjusts the balance between the node transformer output and the sentiment-based prediction:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αt=σ​(𝐰αT​[𝐯t∥S¯t]+bα)∈(0,1)\alpha\_{t}=\sigma(\mathbf{w}\_{\alpha}^{T}[\mathbf{v}\_{t}\|\bar{S}\_{t}]+b\_{\alpha})\in(0,1) |  | (24) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | y^i,t+h=αt⋅yi,t+hnode+(1−αt)⋅yi,t+hsent\hat{y}\_{i,t+h}=\alpha\_{t}\cdot y\_{i,t+h}^{\text{node}}+(1-\alpha\_{t})\cdot y\_{i,t+h}^{\text{sent}} |  | (25) |

where 𝐯t∈ℝ3\mathbf{v}\_{t}\in\mathbb{R}^{3} contains rolling volatility computed over 5, 10, and 20-day windows, S¯t\bar{S}\_{t} is mean absolute sentiment across stocks, yi,t+hnodey\_{i,t+h}^{\text{node}} is the node transformer prediction, and yi,t+hsenty\_{i,t+h}^{\text{sent}} is the sentiment-based prediction. When volatility is high and sentiment signals are strong, the gate can shift weight toward the sentiment branch; during calm periods with sparse social media activity, the node transformer dominates. Fig. [5](#S4.F5 "Figure 5 ‣ IV-E3 Adaptive Integration ‣ IV-E Integration of Node Transformer and BERT ‣ IV Methodology ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") illustrates this adaptive fusion mechanism.

yi,t+hnodey^{\text{node}}\_{i,t+h}yi,t+hsenty^{\text{sent}}\_{i,t+h}Volatility 𝐯t\mathbf{v}\_{t}Sentiment S¯t\bar{S}\_{t}αt=σ​(⋅)\alpha\_{t}=\sigma(\cdot)y^=αt​ynode+(1−αt)​ysent\hat{y}=\alpha\_{t}y^{\text{node}}+(1\!-\!\alpha\_{t})y^{\text{sent}}Final Predictiony^i,t+h\hat{y}\_{i,t+h}


Figure 5: Adaptive fusion mechanism. The weighting coefficient αt\alpha\_{t} is computed from volatility and sentiment magnitude, then used to blend node transformer and sentiment-based predictions.

### IV-F Training Objective

Training a model that is useful for both price forecasting and trading decisions requires optimizing more than point accuracy alone. The composite loss function therefore combines four terms that target complementary aspects of prediction quality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒtotal=λ1​ℒMSE+λ2​ℒDIR+λ3​ℒCORR+λ4​ℒREG\mathcal{L}\_{\text{total}}=\lambda\_{1}\mathcal{L}\_{\text{MSE}}+\lambda\_{2}\mathcal{L}\_{\text{DIR}}+\lambda\_{3}\mathcal{L}\_{\text{CORR}}+\lambda\_{4}\mathcal{L}\_{\text{REG}} |  | (26) |

The primary term is the mean squared error, which penalizes deviations between predicted and realized prices and serves as the dominant gradient signal during training:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒMSE=1N​∑i,t,h(yi,t+h−y^i,t+h)2\mathcal{L}\_{\text{MSE}}=\frac{1}{N}\sum\_{i,t,h}(y\_{i,t+h}-\hat{y}\_{i,t+h})^{2} |  | (27) |

Because minimizing magnitude error does not guarantee correct directional predictions, a binary cross-entropy term explicitly rewards the model for predicting whether prices rise or fall. Here di,t,h=𝕀​(yi,t+h>yi,t)d\_{i,t,h}=\mathbb{I}(y\_{i,t+h}>y\_{i,t}) is the true direction indicator and pi,t,hp\_{i,t,h} is the predicted probability of an increase:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒDIR=−1N​∑i,t,h[di,t,h​log⁡pi,t,h+(1−di,t,h)​log⁡(1−pi,t,h)]\mathcal{L}\_{\text{DIR}}=-\frac{1}{N}\sum\_{i,t,h}\left[d\_{i,t,h}\log p\_{i,t,h}+(1-d\_{i,t,h})\log(1-p\_{i,t,h})\right] |  | (28) |

A correlation loss encourages the model to preserve cross-sectional ranking among stocks at each time step, which is critical for portfolio construction strategies that depend on relative rather than absolute performance. It is defined as one minus the Pearson correlation ρ\rho between predicted and actual return vectors:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒCORR=1−ρ​(𝐫^t,𝐫t)\mathcal{L}\_{\text{CORR}}=1-\rho(\hat{\mathbf{r}}\_{t},\mathbf{r}\_{t}) |  | (29) |

Finally, L2 regularization on all trainable parameters θ\mathbf{\theta} prevents overfitting by penalizing large weight magnitudes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒREG=‖θ‖22\mathcal{L}\_{\text{REG}}=\|\mathbf{\theta}\|\_{2}^{2} |  | (30) |

The weights λ1=1.0\lambda\_{1}=1.0, λ2=0.5\lambda\_{2}=0.5, λ3=0.2\lambda\_{3}=0.2, and λ4=10−4\lambda\_{4}=10^{-4} were tuned on validation data. The MSE term dominates to ensure accurate price-level predictions, while the directional and correlation terms supply auxiliary gradients that improve trend detection and ranking consistency without competing with the primary objective.

### IV-G Training Process

The BERT encoder is fine-tuned separately on the MSE dataset (Section [IV-D](#S4.SS4 "IV-D BERT-Based Sentiment Analysis ‣ IV Methodology ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis")) and remains frozen throughout the forecasting pipeline, serving purely as a fixed feature extractor that produces sentiment scores. Training of the forecasting model proceeds in three stages, stabilizing the integration layers first before progressively fine-tuning the node transformer. During the first 10 epochs, the node transformer is frozen while the sentiment aggregation, fusion, and output layers are trained with a learning rate of 10−410^{-4}. This initial phase allows the fusion mechanism to learn a reasonable mapping between the transformer representations and the fixed sentiment features without disrupting the node transformer’s initialization. In the second stage, spanning 20 epochs, the top three layers of the node transformer are unfrozen and the learning rate is reduced to 5×10−55\times 10^{-5}, enabling the upper representations to adapt to the downstream task while preserving the lower-level features. The final 30 epochs unfreeze all node transformer parameters at a learning rate of 10−510^{-5}, allowing end-to-end fine-tuning of the forecasting architecture.

Throughout all three stages, optimization uses Adam with β1=0.9\beta\_{1}=0.9, β2=0.999\beta\_{2}=0.999, and ϵ=10−8\epsilon=10^{-8}. The learning rate schedule begins with a linear warmup over 4000 steps followed by cosine decay to zero. A batch size of 32 with gradient accumulation over 4 steps yields an effective batch size of 128, balancing memory constraints with gradient stability. Table [III](#S4.T3 "TABLE III ‣ IV-G Training Process ‣ IV Methodology ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") summarizes the key hyperparameters for both the node transformer and BERT components.

TABLE III: Model hyperparameters.

| Parameter | Value |
| --- | --- |
| Node transformer layers | 6 |
| Attention heads | 8 |
| Model dimension | 512 |
| FFN dimension | 2048 |
| Dropout rate | 0.1 |
| Input sequence length | 252 days |
| BERT layers | 12 |
| BERT hidden dimension | 768 |
| Batch size | 32 |
| Total training epochs | 60 |

## V Experiments and Results

### V-A Experimental Setup

Experiments used the dataset described in Section [III](#S3 "III Datasets and Preprocessing ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis"), spanning January 1982 to March 2025, a timeframe that captures multiple market cycles including the 1987 Black Monday crash, the 2000 dot-com bubble, the 2008 financial crisis, and the 2020 COVID-19 volatility spike. The temporal split allocates 1982-2010 for training, 2011-2016 for validation, and 2017-2025 for testing. Although a single temporal split is used rather than rolling retraining, the eight-year test window itself encompasses several distinct market regimes: the post-2016 bull market, the 2018 volatility correction, the 2020 pandemic crash and recovery, the 2022 inflation-driven drawdown, and the subsequent 2023-2024 rebound. This regime diversity provides a rigorous evaluation of generalization without the confound of periodic refitting.

All models were trained on NVIDIA A100 GPUs (40GB), with the full proposed model requiring approximately 18 hours to converge. To ensure unbiased assessment, all evaluation metrics reported in subsequent tables were computed exclusively on the held-out test set.

### V-B Evaluation Metrics

The prediction target yi,t+hy\_{i,t+h} is the closing price Ct+hC\_{t+h} at horizon h∈{1,5,20}h\in\{1,5,20\} trading days. Price-level prediction provides intuitive interpretation of forecast accuracy and aligns with practical trading applications. Directional accuracy is derived from the implied price movement relative to the current price. Five complementary metrics are used to assess model performance from different angles, covering magnitude accuracy, scale sensitivity, directional correctness, relative forecasting skill, and cross-sectional ranking ability.

Mean Absolute Percentage Error (MAPE) measures the average magnitude of prediction errors as a percentage of actual values, making it scale-invariant and directly interpretable across stocks with different price levels:

|  |  |  |  |
| --- | --- | --- | --- |
|  | MAPE=100N​∑i=1N|yi−y^iyi|\text{MAPE}=\frac{100}{N}\sum\_{i=1}^{N}\left|\frac{y\_{i}-\hat{y}\_{i}}{y\_{i}}\right| |  | (31) |

Root Mean Squared Error (RMSE) captures prediction accuracy in the original price units and penalizes large errors more heavily than MAPE due to the squaring operation. This makes it particularly sensitive to outlier predictions during volatile periods:

|  |  |  |  |
| --- | --- | --- | --- |
|  | RMSE=1N​∑i=1N(yi−y^i)2\text{RMSE}=\sqrt{\frac{1}{N}\sum\_{i=1}^{N}(y\_{i}-\hat{y}\_{i})^{2}} |  | (32) |

Directional Accuracy (DA) measures the proportion of correctly predicted price movement directions, independent of magnitude. For trading applications, correctly forecasting whether a stock will rise or fall is often more valuable than minimizing absolute price error, since many strategies depend on directional signals rather than precise price targets.

Theil’s U statistic benchmarks the model against a naive random walk forecast that simply predicts tomorrow’s price as today’s price. It is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | U=∑t(yt+1−y^t+1)2∑t(yt+1−yt)2U=\frac{\sqrt{\sum\_{t}(y\_{t+1}-\hat{y}\_{t+1})^{2}}}{\sqrt{\sum\_{t}(y\_{t+1}-y\_{t})^{2}}} |  | (33) |

A value of U<1U<1 indicates that the model outperforms this naive baseline, while U=1U=1 implies no improvement over persistence forecasting. This metric is especially informative for financial time series, where beating the random walk is itself a non-trivial achievement given the near-efficient nature of liquid equity markets.

The Information Coefficient (IC) is the Spearman rank correlation between predicted and realized returns across the stock universe at each time step. Unlike the other metrics, which evaluate absolute accuracy for individual stocks, the IC assesses cross-sectional ranking ability, measuring whether the model correctly orders stocks from best to worst performer on a given day. This property makes it directly relevant to long-short portfolio construction, where relative performance matters more than absolute price forecasts.

### V-C Baseline Models

Eight baseline models spanning statistical, classical machine learning, and deep learning paradigms were trained on identical data splits to ensure fair comparison. All hyperparameters were tuned via grid search on the validation set (2011-2016), with final performance reported on the held-out test set (2017-2025).

The statistical baselines include ARIMA and Vector Autoregression (VAR). ARIMA orders (p,d,q)(p,d,q) were selected via AIC with p,q∈[0,5]p,q\in[0,5] and d∈[0,2]d\in[0,2], fitting a separate model per stock. VAR extends this to the multivariate setting, modeling cross-stock dependencies with lag order selected via the Bayesian Information Criterion (BIC) up to 10 lags.

Three classical machine learning models were evaluated. Random Forest used 100 trees with maximum depth 10 and the same 17-dimensional feature vector as the proposed model. Support Vector Regression (SVR) employed a Radial Basis Function (RBF) kernel with regularization parameter CC and kernel width γ\gamma selected via grid search. XGBoost used 1000 estimators with early stopping on validation loss to prevent overfitting, and its gradient boosting framework provides a strong tree-based benchmark.

The deep learning baselines include LSTM, a Simple Transformer, and a BERT + LSTM hybrid. The LSTM used 2 layers with 128 hidden units and a 60-day lookback window, representing the most widely adopted recurrent architecture for financial time series. The Simple Transformer used 4 layers, 8 attention heads, and 256-dimensional embeddings, providing a direct comparison that isolates the contribution of graph structure and sentiment integration in the proposed model. The BERT + LSTM hybrid combined BERT-extracted sentiment features with an LSTM price model through simple concatenation, serving as an ablation baseline that tests whether the attention-based fusion mechanism in the proposed architecture provides meaningful improvement over naive feature combination.

### V-D Sentiment Model Evaluation

Before evaluating the full forecasting pipeline, the fine-tuned BERT sentiment classifier was assessed independently on the MSE dataset. The dataset was partitioned into training (70%), validation (15%), and test (15%) splits, stratified to preserve the class distribution across all three subsets. The model was fine-tuned on the training split using the progressive unfreezing schedule described in Section [IV-D](#S4.SS4 "IV-D BERT-Based Sentiment Analysis ‣ IV Methodology ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis"), with early stopping based on validation loss. All results reported in this subsection are computed on the held-out test split, which the model did not observe during training or hyperparameter selection.

Table [IV](#S5.T4 "TABLE IV ‣ V-D Sentiment Model Evaluation ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") presents per-class and aggregate classification metrics. Because the MSE dataset exhibits class imbalance, with neutral posts outnumbering positive and negative ones, macro-averaged scores are reported alongside accuracy to avoid inflating performance through the majority class.

TABLE IV: BERT sentiment classification performance on the MSE test set.

|  |  |  |  |
| --- | --- | --- | --- |
| Class / Metric | Precision | Recall | F1-Score |
| Negative | 0.83 | 0.80 | 0.81 |
| Neutral | 0.89 | 0.92 | 0.90 |
| Positive | 0.85 | 0.82 | 0.83 |
| Macro Average | 0.86 | 0.85 | 0.85 |
| Overall Accuracy | | | 0.87 |
| Cohen’s κ\kappa | | | 0.79 |

The fine-tuned model achieves 87% overall accuracy and a macro-averaged F1 of 0.85, with per-class F1 scores ranging from 0.81 (negative) to 0.90 (neutral). The neutral class benefits from a larger training sample and from the relative straightforwardness of factual financial reporting, which accounts for its higher precision and recall. The negative class exhibits the lowest recall at 0.80, a pattern consistent with prior financial NLP work: bearish language in social media frequently relies on sarcasm, hedging, or implicit phrasing (e.g., “this stock is going to the moon” used sarcastically) that poses greater classification difficulty. Cohen’s κ=0.79\kappa=0.79 falls within the substantial agreement range, confirming that the classifier discriminates sentiment beyond what class priors alone would predict. Given that the ablation study (Section [V-E](#S5.SS5 "V-E Results ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis")) attributes a 10% MAPE reduction to sentiment integration, the 13% classification error rate suggests that the node transformer’s gating mechanism is robust enough to extract predictive value even from an imperfect sentiment signal.

### V-E Results

#### V-E1 Overall Performance

Table [V](#S5.T5 "TABLE V ‣ V-E1 Overall Performance ‣ V-E Results ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") presents MAPE across prediction horizons for all models. Performance is evaluated at three horizons (1-day, 5-day, and 20-day) to assess both short-term accuracy and degradation over longer forecasting windows.

TABLE V: MAPE (%) and Theil’s U across prediction horizons. Best results in bold. Standard errors in parentheses.

| Model | 1-Day | 5-Day | 20-Day | Theil’s U |
| --- | --- | --- | --- | --- |
| Naïve Random Walk | 1.35 (0.09) | 3.40 (0.18) | 5.80 (0.28) | 1.00 |
| ARIMA | 1.20 (0.08) | 2.80 (0.15) | 4.50 (0.22) | 0.89 |
| VAR | 1.15 (0.07) | 2.60 (0.14) | 4.20 (0.20) | 0.85 |
| LSTM | 1.00 (0.06) | 2.30 (0.12) | 3.80 (0.18) | 0.74 |
| Random Forest | 1.10 (0.07) | 2.50 (0.13) | 4.00 (0.19) | 0.81 |
| SVR | 1.05 (0.06) | 2.40 (0.12) | 3.90 (0.18) | 0.78 |
| XGBoost | 0.95 (0.05) | 2.20 (0.11) | 3.50 (0.16) | 0.70 |
| Simple Transformer | 0.90 (0.05) | 2.10 (0.10) | 3.30 (0.15) | 0.67 |
| BERT + LSTM | 0.88 (0.05) | 2.00 (0.10) | 3.10 (0.14) | 0.65 |
| Proposed Model | 0.80 (0.04) | 1.80 (0.09) | 2.80 (0.13) | 0.59 |

A persistent concern in short-horizon financial forecasting is the naive persistence artifact, where a model achieves seemingly low error by tracking the previous day’s closing price (y^t+1=yt\hat{y}\_{t+1}=y\_{t}). Because daily price changes for liquid mega-cap stocks typically range between 1% and 2%, any persistence-based forecast will naturally yield MAPE in that vicinity. The naive random walk baseline in Table [V](#S5.T5 "TABLE V ‣ V-E1 Overall Performance ‣ V-E Results ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") produces a 1-day MAPE of 1.35% on our test set, and the proposed model’s Theil’s U of 0.59 confirms that it captures genuine structural patterns rather than merely lagging the current price. All learned models achieve U<1U<1, but only the proposed model reduces the random walk error by more than 40%, with the gap widening at longer horizons where persistence forecasting degrades rapidly.

The proposed model achieves 0.80% MAPE for 1-day predictions, representing 33% relative improvement over ARIMA (Δ=0.40\Delta=0.40 percentage points) and 20% improvement over LSTM (Δ=0.20\Delta=0.20 pp). Improvement margins widen at longer horizons: the 5-day gap over ARIMA grows from 0.40 to 1.00 percentage points, consistent with the model’s ability to capture structural patterns that persist beyond short-term noise.

#### V-E2 Directional Accuracy

Beyond magnitude accuracy, directional accuracy measures the proportion of correctly predicted price movement directions. Table [VI](#S5.T6 "TABLE VI ‣ V-E2 Directional Accuracy ‣ V-E Results ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") presents directional accuracy with 95% confidence intervals computed via bootstrap resampling.

TABLE VI: Directional accuracy (%) for 1-day predictions with 95% confidence intervals.

| Model | DA (%) |
| --- | --- |
| Random Baseline | 50.0 |
| ARIMA | 55.0 [53.2, 56.8] |
| VAR | 56.0 [54.2, 57.8] |
| LSTM | 58.0 [56.2, 59.8] |
| Random Forest | 57.0 [55.2, 58.8] |
| XGBoost | 60.0 [58.2, 61.8] |
| Simple Transformer | 62.0 [60.2, 63.8] |
| BERT + LSTM | 63.0 [61.2, 64.8] |
| Proposed Model | 65.0 [63.2, 66.8] |

The proposed model achieves 65% directional accuracy, exceeding the 50% random baseline by 15 percentage points and outperforming LSTM by 7 percentage points. The confidence interval [63.2, 66.8] does not overlap with the best baseline (BERT + LSTM at [61.2, 64.8]), providing evidence that the improvement is not attributable to sampling variability alone.

#### V-E3 Ablation Studies

To isolate the contribution of each architectural component, Table [VII](#S5.T7 "TABLE VII ‣ V-E3 Ablation Studies ‣ V-E Results ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") presents results from systematic ablation experiments. Each row removes a single component while keeping all others intact, allowing direct assessment of marginal contributions.

TABLE VII: Ablation study: MAPE (%) for 1-day predictions.

| Configuration | MAPE | Δ\Delta vs Full |
| --- | --- | --- |
| Full Model | 0.80 | – |
| Without Sentiment | 0.88 | +10.0% |
| Without Graph Structure | 0.92 | +15.0% |
| Without Temporal Encoding | 0.95 | +18.8% |
| Without Feature Gating | 0.84 | +5.0% |
| Price Features Only | 1.02 | +27.5% |

Graph structure contributes the second-largest improvement at 15%, confirming that explicit inter-stock relationship modeling provides predictive value beyond treating stocks independently. Sentiment integration contributes 10%, with the gap widening during information-rich periods such as earnings announcements. Temporal encoding contributes 18.8%, underscoring the importance of capturing long-range sequential dependencies in financial time series. The price-only configuration, which strips all augmentations, degrades by 27.5%, indicating that the full feature set is substantially richer than raw price data alone.

#### V-E4 Performance Across Volatility Regimes

Table [VIII](#S5.T8 "TABLE VIII ‣ V-E4 Performance Across Volatility Regimes ‣ V-E Results ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") presents MAPE across volatility regimes classified by the CBOE Volatility Index (VIX) (Low: VIX <15<15; Medium: 15≤15\leq VIX <25<25; High: VIX ≥25\geq 25).

TABLE VIII: MAPE (%) by market volatility regime.

| Model | Low VIX | Medium VIX | High VIX |
| --- | --- | --- | --- |
| ARIMA | 1.00 | 1.30 | 2.10 |
| LSTM | 0.85 | 1.10 | 1.80 |
| XGBoost | 0.80 | 1.00 | 1.60 |
| Proposed | 0.70 | 0.90 | 1.50 |

The proposed model maintains MAPE below 1.5% during high-volatility periods while baseline models exceed 1.6-2.1%. This robustness gap is most pronounced during VIX spikes accompanying earnings surprises and macroeconomic shocks, precisely the conditions where accurate forecasts carry the greatest practical value for risk management. The gating mechanism likely contributes to this resilience by increasing the weight of momentum features during volatile periods while favoring longer-term indicators during calm markets.

#### V-E5 Statistical Significance

To assess whether the observed improvements are statistically significant rather than artifacts of sampling variability, paired t-tests were conducted comparing daily absolute prediction errors between the proposed model and each baseline across the 1,580 test days. Table [IX](#S5.T9 "TABLE IX ‣ V-E5 Statistical Significance ‣ V-E Results ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") presents the results along with Cohen’s dd effect sizes.

TABLE IX: Paired t-test results (n=1,580n=1,580 test days). Negative tt indicates proposed model superiority.

| Baseline | tt-statistic | pp-value | Cohen’s dd |
| --- | --- | --- | --- |
| ARIMA | −4.25-4.25 | <0.0001<0.0001 | 0.34 |
| LSTM | −3.12-3.12 | 0.0018 | 0.25 |
| XGBoost | −2.45-2.45 | 0.0145 | 0.19 |
| Simple Transformer | −2.18-2.18 | 0.0295 | 0.17 |
| BERT + LSTM | −3.90-3.90 | 0.0001 | 0.31 |

All comparisons achieve p<0.05p<0.05, with the strongest significance observed against ARIMA (p<0.0001p<0.0001) and the weakest against the Simple Transformer (p=0.0295p=0.0295). Effect sizes (Cohen’s dd) range from 0.17 to 0.34, indicating small to medium practical effects. The larger effect sizes against ARIMA and BERT + LSTM reflect more fundamental architectural differences, while the smaller effect size against the Simple Transformer suggests that much of the improvement stems from the graph and sentiment components rather than the transformer backbone itself.

Paired t-tests assume that forecast errors are independently distributed, an assumption frequently violated in financial time series due to volatility clustering and serial dependence in prediction residuals. To account for this, we supplement the analysis with the Diebold-Mariano (DM) test [[28](#bib.bib28)], which evaluates equal predictive accuracy between two forecasting models using Newey-West heteroskedasticity and autocorrelation consistent standard errors. Table [X](#S5.T10 "TABLE X ‣ V-E5 Statistical Significance ‣ V-E Results ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") reports DM statistics computed on mean absolute error loss differentials over the 1,580-day test period, with the naive random walk included as a reference benchmark.

TABLE X: Diebold-Mariano test results (n=1,580n=1{,}580 test days, MAE loss). Negative DM-statistic indicates proposed model superiority.

| Baseline | DM-statistic | pp-value |
| --- | --- | --- |
| Naïve Random Walk | −5.82-5.82 | <0.0001<0.0001 |
| ARIMA | −3.58-3.58 | 0.0002 |
| LSTM | −2.67-2.67 | 0.0038 |
| XGBoost | −2.08-2.08 | 0.0189 |
| Simple Transformer | −1.84-1.84 | 0.0330 |
| BERT + LSTM | −3.31-3.31 | 0.0005 |

The DM statistics are uniformly attenuated relative to the paired t-test values, consistent with the inflation of standard errors once serial dependence in forecast residuals is accounted for. All comparisons remain significant at p<0.05p<0.05, though the margin against the Simple Transformer narrows (p=0.033p=0.033), reinforcing the interpretation that the graph structure and sentiment fusion are the primary drivers of improvement over a vanilla transformer backbone. The strongest DM statistic appears against the naive random walk (−5.82-5.82, p<0.0001p<0.0001), providing additional confirmation that the model captures structural dynamics beyond price persistence.

#### V-E6 Economic Significance

A long-short strategy going long on the top 5 predicted performers and short on the bottom 5 achieved gross cumulative returns of 25.3% over the 15-month evaluation period (January 2024 to March 2025), compared to 15.1% for S&P 500 buy-and-hold.

To assess whether these gains survive realistic market frictions, a proportional transaction cost of 10 basis points per trade was applied, consistent with institutional execution costs for liquid large-cap equities. The strategy exhibited an average daily portfolio turnover of 32%, reflecting the sentiment-driven rebalancing that shifts positions as new social media signals arrive. After deducting transaction costs, the net cumulative return was 18.4%, still exceeding the buy-and-hold benchmark by 3.3 percentage points. The net annualized Sharpe ratio of 1.15 (down from 1.42 gross) confirms that the model’s directional accuracy translates into viable risk-adjusted gains even under trading friction, though the sensitivity to turnover suggests that lower-frequency rebalancing schedules merit investigation for cost-sensitive applications.

## VI Discussion

### VI-A Interpretation of Results

The integrated model demonstrates consistent improvements across metrics, horizons, and market conditions, with the magnitude of gains varying by component and context in ways that illuminate the mechanisms underlying the model’s predictive advantage.

The graph-based representation captures inter-stock dependencies that independent models miss. The 15% improvement from graph structure confirms that explicit relationship modeling provides predictive value beyond treating stocks independently. Learned edge weights showed meaningful patterns: same-sector connections exhibited higher average weights (0.72 vs. 0.41 for cross-sector), while cross-sector weights increased during market-wide movements, consistent with empirical observations that correlations increase during market stress [[5](#bib.bib5)].

Sentiment integration proves valuable around information events. The 25% improvement during earnings seasons indicates that social media sentiment contains early signals not fully reflected in contemporaneous prices. Sector-level heterogeneity aligns with expectations: consumer-facing companies show stronger sentiment-price relationships (14% MAPE reduction) compared to utilities (6%), likely reflecting differential retail investor engagement.

The gating mechanism enables adaptive feature weighting that responds to market conditions. Analysis of learned gate activations showed that momentum features (RSI, MACD, short-term returns) received higher weights during volatile periods, while longer-term indicators (20-day SMA, rolling volatility) received higher weights during stable periods. This adaptive behavior aligns with the intuition that different indicators carry different predictive value depending on market regime, and it emerges naturally through training rather than being imposed through manual feature selection.

### VI-B Implications

For practitioners, the model’s directional accuracy enables more informed trading decisions, particularly for short-term strategies where predicting price direction is often more important than predicting magnitude. The enhanced ability to predict during volatile conditions helps risk management, as these are precisely the periods when forecast reliability matters most for position sizing and drawdown control. The graph structure provides interpretable inter-stock relationships useful for portfolio diversification, as the learned edge weights can reveal dependencies that traditional correlation matrices might obscure.

From a theoretical perspective, performance gains from sentiment integration suggest that markets do not fully incorporate qualitative information immediately, supporting bounded efficiency [[1](#bib.bib1)]. The 25% improvement during earnings seasons indicates that social media contains early signals about investor reactions that are not yet reflected in price. The success of graph-based modeling provides further evidence that markets function as complex, interconnected systems rather than collections of independent securities, consistent with findings in the network finance literature.

### VI-C Limitations

The findings should be interpreted in light of limitations spanning data selection, modeling assumptions, and economic validity.

The most consequential concern is survivorship bias in stock selection. The 20 stocks were chosen based on current S&P 500 membership and data availability, meaning that companies which failed, were acquired, or were delisted between 1982 and 2025 are absent from the dataset. Because the selected universe consists of companies that ultimately succeeded, reported performance may be inflated relative to what a real-time investor would experience. Results could differ on a point-in-time universe constructed from historical index constituents. Relatedly, the 20-node graph structure, while demonstrating meaningful contribution in ablation studies (15% improvement), represents a limited cross-section of the market. Larger universes might better capture complex market topology; the current design prioritizes temporal depth over cross-sectional breadth.

Beyond stock selection, data-related assumptions also affect generalizability. Edge weight initialization relies on correlations computed over the training period (1982-2010), but market correlations are inherently non-stationary. Relationships that held during this window may weaken or reverse by the test period. The learnable edge refinement mechanism partially compensates by adapting weights during training, though fundamental correlation regime shifts could still limit generalization. Similarly, X (formerly Twitter) data availability from 2007 onward means sentiment features are set to zero for the 1982-2006 training period. The sentiment component therefore receives limited training signal during most of the training window, with the model’s ability to leverage sentiment primarily developed and evaluated on post-2007 data. Sentiment analysis also relies on English-language content from a single social media platform, and changes to API access policies may affect reproducibility.

From a practical standpoint, the economic significance analysis applies a fixed 10 basis point transaction cost but does not model variable market impact or execution slippage, both of which increase with order size and decrease with liquidity. The 32% daily turnover observed in the backtest would amplify these unmodeled frictions, and the net returns reported in Section [V-E](#S5.SS5 "V-E Results ‣ V Experiments and Results ‣ This work has been submitted to IEEE Access for possible publication. Stock Market Prediction Using Node Transformer Architecture Integrated with BERT Sentiment Analysis") should be viewed as an upper bound on realizable performance. Model complexity also presents challenges for real-time high-frequency applications, as the 252-day input sequence length and multi-head attention mechanisms demand substantial computational resources. The evaluation is performed on the same 20 stocks used for model development, which limits assessment of external validity on unseen securities.

### VI-D Future Directions

Multiple directions merit investigation. Expanding the stock universe to the full S&P 500 or international markets would test whether the graph-based architecture scales effectively and whether inter-stock dependencies remain informative as the number of nodes grows. Incorporating multilingual sentiment sources and alternative platforms (Reddit, financial news, earnings call transcripts) would broaden the information base and reduce single-source dependency. On the architectural side, developing more efficient attention mechanisms, such as sparse or linear attention variants, could enable real-time deployment for higher-frequency trading applications. Regime-shift detection mechanisms that adjust model behavior during structural market transitions (e.g., policy changes or liquidity crises) represent a natural extension of the gating mechanism already present in the model. Finally, integrating the forecasting framework with portfolio optimization and formal risk management objectives could bridge the gap between prediction accuracy and realized economic value.

## VII Conclusion

This paper introduced an integrated framework that combines a node transformer architecture with BERT-based sentiment analysis for stock price forecasting. The model represents the stock market as a graph in which individual stocks serve as nodes connected by learnable edges that encode sectoral affiliations and price correlations. A fine-tuned BERT model processes social media text to extract sentiment signals, which are then merged with quantitative price features through an adaptive attention-based fusion mechanism conditioned on volatility and sentiment magnitude.

Experiments on 20 S&P 500 stocks spanning 1982 to 2025 yielded a MAPE of 0.80% for one-day-ahead predictions, compared to 1.20% for ARIMA and 1.00% for LSTM. Ablation studies isolated the contribution of each component: removing sentiment raised error by 10% (and by 25% during earnings seasons), while removing the graph structure increased error by 15%. Directional accuracy reached 65%, exceeding baselines by 7 to 10 percentage points, and both paired t-tests and Diebold-Mariano tests confirmed statistical significance across all comparisons (p<0.05p<0.05), with the latter accounting for autocorrelation in forecast residuals.

Taken together, these findings support the premise that jointly modeling inter-stock dependencies and investor sentiment yields more accurate and robust forecasts than architectures that address either dimension in isolation. Future work should extend this framework to broader equity universes, incorporate multilingual and multi-platform sentiment sources, investigate efficient attention variants for real-time deployment, and integrate the forecasting pipeline with portfolio optimization and formal risk management objectives.

## Acknowledgment

The author is grateful to Dr. Hussein Al Osman, whose mentorship and thoughtful feedback shaped the direction of this work from its earliest stages. His expertise in both the technical and conceptual aspects of this research proved invaluable.

## References

* [1]

  E. F. Fama, “Efficient capital markets: A review of theory and empirical work,” *The Journal of Finance*, vol. 25, no. 2, pp. 383–417, 1970.
* [2]

  J. Zhang, Y. Teng, and W. Chen, “Stock market prediction via deep learning techniques: A survey,” *arXiv preprint arXiv:2212.12717*, 2022.
* [3]

  I. W. R. Martin and S. Nagel, “Market efficiency in the age of big data,” *Journal of Financial Economics*, vol. 145, no. 1, pp. 154–177, 2022.
* [4]

  I. Goldstein, “Information in financial markets and its real effects,” *Review of Finance*, vol. 27, no. 1, pp. 1–32, 2023.
* [5]

  D. Kahneman and A. Tversky, “Prospect theory: An analysis of decision under risk,” *Econometrica*, vol. 47, no. 2, pp. 263–291, 1979.
* [6]

  J. J. Murphy, *Technical analysis of the financial markets: A comprehensive guide to trading methods and applications*. New York Institute of Finance, 1999.
* [7]

  T. Fischer and C. Krauss, “Deep learning with long short-term memory networks for financial market predictions,” *European Journal of Operational Research*, vol. 270, no. 2, pp. 654–669, 2018.
* [8]

  A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” in *Advances in Neural Information Processing Systems*, vol. 30, 2017, pp. 5998–6008.
* [9]

  Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and S. Y. Philip, “A comprehensive survey on graph neural networks,” *IEEE Transactions on Neural Networks and Learning Systems*, vol. 32, no. 1, pp. 4–24, 2020.
* [10]

  Q. Wu, W. Zhao, Z. Li, D. P. Wipf, and J. Yan, “Nodeformer: A scalable graph structure learning transformer for node classification,” in *Advances in Neural Information Processing Systems*, vol. 35, 2022, pp. 27 387–27 401.
* [11]

  P. R. Low and E. Sakk, “Comparison between autoregressive integrated moving average and long short-term memory models for stock price prediction,” *IAES International Journal of Artificial Intelligence*, vol. 12, no. 4, pp. 1828–1835, 2023.
* [12]

  S. T. Wahyudi, “The ARIMA model for the indonesia stock price,” *International Journal of Economics and Management*, vol. 11, pp. 223–236, 2017.
* [13]

  R. K. Nayak, D. Mishra, and A. K. Rath, “A naïve SVM-KNN based stock market trend reversal analysis for Indian benchmark indices,” *Applied Soft Computing*, vol. 35, pp. 670–680, 2015.
* [14]

  M. Siddique and D. Panda, “Prediction of stock index of Tata Steel using hybrid machine learning based optimization techniques,” *International Journal of Recent Technology and Engineering*, vol. 8, pp. 3186–3193, 2019.
* [15]

  S. Basak, S. Kar, S. Saha, L. Khaidem, and S. R. Dey, “Predicting the direction of stock market prices using tree-based classifiers,” *The North American Journal of Economics and Finance*, vol. 47, pp. 552–567, 2019.
* [16]

  S. K. Chandar, “Convolutional neural network for stock trading using technical indicators,” *Automated Software Engineering*, vol. 29, pp. 1–14, 2022.
* [17]

  M. Wen, P. Li, L. Zhang, and Y. Chen, “Stock market trend prediction using high-order information of time series,” *IEEE Access*, vol. 7, pp. 28 299–28 308, 2019.
* [18]

  L. Di Persio and O. Honchar, “Recurrent neural networks approach to the financial forecast of Google assets,” *International Journal of Mathematics and Computers in Simulation*, vol. 11, pp. 7–13, 2017.
* [19]

  M. A. Hossain, R. Karim, R. Thulasiram, N. Bruce, and Y. Wang, “Hybrid deep learning model for stock price prediction,” *IEEE Symposium Series on Computational Intelligence*, pp. 1837–1844, 2018.
* [20]

  Y. Xu, L. Chhim, B. Zheng *et al.*, “Stacked deep learning structure with bidirectional long-short term memory for stock market prediction,” in *Communications in Computer and Information Science*, vol. 1265, 2020, pp. 447–460.
* [21]

  M. Liu, H. Sheng, N. Zhang *et al.*, “A new deep network model for stock price prediction,” in *International Conference on Machine Learning for Cyber Security*, 2022, pp. 413–426.
* [22]

  W. Chen, M. Jiang, W.-G. Zhang, and Z. Chen, “A novel graph convolutional feature based convolutional neural network for stock trend prediction,” *Information Sciences*, vol. 556, pp. 67–94, 2021.
* [23]

  C. Wang, H. Liang, B. Wang, X. Cui, and Y. Xu, “MG-Conv: A spatiotemporal multi-graph convolutional neural network for stock market index trend prediction,” *Computers and Electrical Engineering*, vol. 103, p. 108285, 2022.
* [24]

  S. Li and Z. Qian, “A financial forecasting model based on transformer architecture,” *IEEE International Conference on Big Data*, pp. 5384–5386, 2019.
* [25]

  W. Lu, J. Li, J. Wang *et al.*, “A CNN-BiLSTM-AM method for stock price prediction,” *Neural Computing and Applications*, vol. 33, pp. 4741–4753, 2021.
* [26]

  K. Cortis, A. Freitas, T. Daudert, M. Huerlimann, M. Zarrouk, S. Handschuh, and B. Davis, “SemEval-2017 task 5: Fine-grained sentiment analysis on financial microblogs and news,” in *Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017)*, 2017, pp. 519–535.
* [27]

  J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-training of deep bidirectional transformers for language understanding,” in *Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics*, 2019, pp. 4171–4186.
* [28]

  F. X. Diebold and R. S. Mariano, “Comparing predictive accuracy,” *Journal of Business & Economic Statistics*, vol. 13, no. 3, pp. 253–263, 1995.

|  |  |
| --- | --- |
| [Uncaptioned image] | Mohammad Al Ridhawi received the B.A.Sc. degree in computer engineering and the M.Sc. degree in digital transformation and innovation (machine learning) from the University of Ottawa, Ottawa, Canada, in 2019 and 2021, respectively. He is currently pursuing the Ph.D. degree in electrical and computer engineering at the University of Ottawa, where he also serves as a Part-Time Engineering Professor. He has industry experience as a Senior Data Scientist and Senior Machine Learning Engineer, building production ML systems in financial and environmental domains. His research interests include deep learning, graph neural networks, natural language processing, financial time series analysis, and reinforcement learning. |



|  |  |
| --- | --- |
| [Uncaptioned image] | Mahtab Haj Ali received the M.Sc. degree in digital transformation and innovation from the University of Ottawa, Ottawa, Canada, in 2021. She is currently pursuing the Ph.D. degree in electrical and computer engineering at the University of Ottawa, with a research focus on time series forecasting and deep learning models. She works as an AI Research Engineer at the National Research Council of Canada, where she builds and evaluates large language models (LLMs) and develops AI-driven solutions for real-world industrial applications. Her work includes large-scale time series analysis, advanced feature engineering, and the application of LLMs in production environments. Her research interests include deep learning for time series analysis, deep neural networks, and applied artificial intelligence. |



|  |  |
| --- | --- |
| [Uncaptioned image] | Hussein Al Osman received the B.A.Sc., M.A.Sc., and Ph.D. degrees from the University of Ottawa, Ottawa, Canada. He is an Associate Professor and Associate Director in the School of Electrical Engineering and Computer Science at the University of Ottawa, where he leads the Multimedia Processing and Interaction Group. His research focuses on affective computing, multimodal affect estimation, human–computer interaction, serious gaming, and multimedia systems. He has produced over 50 peer-reviewed research articles, two patents, and several technology transfers to industry. |

BETA