---
authors:
- Sandeep Neela
doc_id: arxiv:2512.17185v1
family_id: arxiv:2512.17185
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash
  Prediction'
url_abs: http://arxiv.org/abs/2512.17185v1
url_html: https://arxiv.org/html/2512.17185v1
venue: arXiv q-fin
version: 1
year: 2025
---


###### Abstract

Financial crises emerge when structural vulnerabilities accumulate across sectors, markets, and investor behavior. Predicting these systemic transitions is challenging because they arise from evolving interactions between market participants, not isolated price movements. We present Systemic Risk Radar (SRR), a framework that models financial markets as multi-layer graphs to detect early signs of systemic fragility and crash-regime transitions.

We evaluate SRR across three major crises: the Dot-com crash, the Global Financial Crisis, and the COVID-19 shock. Our experiments compare snapshot GNNs, a simplified temporal GNN prototype, and standard baselines (logistic regression and Random Forest). Results show that structural network information provides useful early-warning signals compared to feature-based models alone.

This correlation-based instantiation of SRR demonstrates that graph-derived features capture meaningful changes in market structure during stress events. The findings motivate extending SRR with additional graph layers (sector/factor exposure, sentiment) and advanced temporal architectures (LSTM/GRU or Transformer encoders) to better handle diverse crisis types.

## 1 Introduction

Financial markets are interconnected. Price formation, liquidity, and volatility reflect sector-wide and cross-asset feedback effects. Large market declines over the last two decades—the Dot-com crash (2000–2002), the global financial crisis (2008–2010), and the COVID-19 crash (2020)—were not triggered by single shocks. They emerged from accumulated fragility: rising correlations, leverage amplification, deteriorating liquidity, and cross-market contagion.

Most market prediction tools focus on individual assets or sector-wise indicators. Factor models, volatility indexes, and macroeconomic indicators struggle to capture systemic interactions. They predict whether specific assets or sectors will decline, not whether the broader market is approaching a systemic risk regime. This requires understanding the connectivity and temporal evolution of market structure.

We introduce a modeling approach based on a simple observation: systemic instability shows up in the structure of the market before it shows up in prices. When correlations spike, volatility clusters spread, and sectors synchronize, the system becomes vulnerable. These structural signals precede actual drawdowns and can warn of impending regime shifts.

Recent research has explored complementary approaches at finer levels of granularity.
Structural price decomposition methods have been proposed to extract explainable market
behavior at the individual instrument level, while multimodal frameworks have been used
to identify manipulation and anomaly patterns by aligning market data with social signals
(neela2025spa; neela2025aimm).
However, these approaches operate primarily at the micro or event level and do not model
how localized stress accumulates and propagates across the broader market system.
SRR is designed to address this gap by modeling systemic risk as an emergent property of
market-wide structure rather than isolated signals.

Past work shows that systemic fragility emerges through the build-up of network connectivity and amplification effects, not isolated price shocks  (battiston2012debtrank; mantegna1999hierarchical; haldane2011systemic).
Traditional forecasting models miss these structural dependencies and network-mediated channels of contagion  (laloux2000random; acemoglu2015systemic).

Recent work on contagion in financial networks further highlights how localized shocks can propagate system-wide through balance sheet and funding linkages  (glasserman2015contagion; elliott2014financial; gai2010contagion).

### 1.1 Motivation

SRR addresses two problems. First, systemic risk is a macro-level phenomenon that single-variable predictors cannot explain. Second, traditional models do not exploit recent advances in graph neural networks, which can learn representations of evolving networks. Our key insight: model financial markets as dynamically evolving graphs, where nodes represent instruments and edges represent relationships like correlation, co-volatility, or sentiment co-movement.

### 1.2 Gaps in Prior Approaches

Prior work relies on historical time series, macro signals, or factor models. These methods do not capture multi-sector connectivity or allow representations to evolve over time. Even correlation matrices and rolling covariance compress market structure into static snapshots, losing temporal dynamics.

### 1.3 Contributions

This paper makes the following contributions:

* •

  We introduce a multi-layer graph representation for market states, capturing correlation, sector similarity, and sentiment connectivity.
* •

  We propose a temporal GNN framework for modeling systemic risk evolution and implement a simplified prototype using GCN encoders with GRU-based sequence aggregation.
* •

  We provide methods for interpretability and scenario simulation designed to help practitioners understand model decisions.
* •

  We demonstrate that SRR provides meaningful early-warning behavior relative to baselines.
* •

  We analyze how different stress regimes expose distinct structural limitations of correlation-based GNNs.

Unlike prior micro-level approaches, SRR explicitly targets system-wide risk dynamics and cross-asset propagation.

### 1.4 Empirical Findings

Preliminary empirical analysis shows that graph-based representations provide meaningful early-warning signals of systemic fragility. In particular, simple snapshot GNN models, a simplified temporal GNN prototype, and traditional baselines (logistic regression and Random Forest) capture shifts in correlation structure and volatility clustering during known crisis events. The evaluated temporal model uses only the correlation layer and short graph sequences, but still demonstrates that market topology carries predictive information. These results provide preliminary support for the SRR framework and motivate training the full multi-layer temporal architecture with richer inputs.

## 2 Related Work

Network-based contagion modeling has been widely studied in systemic risk research
 (battiston2012debtrank; haldane2011systemic; acemoglu2015systemic), while correlation
networks and random matrix theory have been used to characterize market structure and
instability  (mantegna1999hierarchical; laloux2000random). More recently, graph-based
and temporal neural architectures have been applied to financial prediction tasks
 (huang2020financialgnn; feng2019temporalgnn), but their use for macro-level systemic regime detection remains limited.

Systemic risk modeling spans early-warning systems, network-based contagion models, and deep learning for financial forecasting. Traditional early-warning systems use macroeconomic indicators like credit spreads, volatility indexes, and interest rate slopes. These identify broad stress but miss structural market dynamics.

Network models analyze contagion in interbank lending and credit networks through exposure networks, overlapping portfolios, and counterparty risk. Correlation networks proxy market connectivity, and rising correlation precedes instability. But correlation-only approaches produce a single market representation and miss other forms of connectivity.

Deep learning methods (RNNs, hybrid sentiment-market models) forecast volatility and stress but focus on asset-level dynamics, not systemic transitions.

Graph neural networks appear in portfolio optimization and risk propagation but temporal GNNs for systemic regime detection are rare. We know of no prior work combining heterogeneous multi-layer graphs with temporal sequence modeling for systemic risk prediction.

In parallel, the graph neural network literature has developed rapidly, from early graph convolutional networks  (kipf2017semi) and graph attention architectures  (velivckovic2018graph) to broader surveys of GNN methods  (wu2020comprehensive). These models form a natural foundation for learning over financial network structures.

## 3 Data and Feature Engineering

We utilize publicly available market and macroeconomic data, including:

* •

  Equity index and sector ETF prices,
* •

  Volatility indexes such as VIX (available but not used in current experiments),
* •

  Treasury yields and credit spread proxies (future work),
* •

  Sentiment and news-derived indicators (future work).

From these sources, we construct seven daily node-level features: daily returns, 20-day and 60-day rolling volatility, 20-day and 60-day drawdowns, and 10-day and 30-day momentum indicators. Macro overlays reflecting economic conditions are included as graph-level context features. Feature engineering is performed using rolling windows to ensure no future information is inadvertently incorporated.

Table [1](https://arxiv.org/html/2512.17185v1#S3.T1 "Table 1 ‣ 3 Data and Feature Engineering ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") summarizes the dataset. The crisis periods selected for evaluation—the Dot-com crash, global financial crisis, and COVID shock—represent structurally different regimes, testing SRR’s generality.

Table 1: Summary of crisis periods and dataset characteristics used in our experiments.

| Crisis | Period | Trading Days | # Stocks |
| --- | --- | --- | --- |
| Dot-com Bubble | 1998–2003 | 1,565 | 44 |
| Global Financial Crisis | 2006–2011 | 1,565 | 44 |
| COVID–19 Pandemic | 2018–2021 | 1,045 | 44 |

## 4 Multi-Layer Graph Model

Empirical work shows that changes in network topology and connectivity precede large market dislocations (haldane2011systemic; fouque2013systemic).

SRR’s premise: systemic fragility is encoded in market structure, not isolated asset movements. We represent the market as a dynamically evolving multi-layer graph. Each layer corresponds to a different relationship type between financial assets, and each layer evolves over time as market conditions change.

### 4.1 Graph Construction

Let Gt=(V,Et)G\_{t}=(V,E\_{t}) be the market graph at time tt, where VV is the set of nodes representing instruments and EtE\_{t} is the set of edges capturing connectivity. We consider three primary edge types:

* •

  Correlation Layer: edges represent historical return correlations, computed over a sliding window.
* •

  Sector/Factor Layer: edges link entities belonging to the same sector or factor exposure.
* •

  Sentiment Co-movement Layer (optional): edges represent co-movement in social-media or sentiment signals.

Each layer is represented by a separate adjacency or edge set, allowing the model to disentangle different forms of connectivity.

Formally, the multi-layer graph is:

|  |  |  |
| --- | --- | --- |
|  | 𝒢t={𝒢t1,𝒢t2,…,𝒢tM}.\mathcal{G}\_{t}=\{\mathcal{G}\_{t}^{1},\mathcal{G}\_{t}^{2},\dots,\mathcal{G}\_{t}^{M}\}. |  |

#### Layers Used in This Version.

Although SRR is designed to incorporate multiple risk channels
(correlation, sector/factor exposure, sentiment co-movement), the current
experiments use only the correlation layer. This choice ensures experimental
stability and focuses evaluation on the predictive value of structural
dependencies alone. Evaluating the full multi-layer graph is part of future work.

### 4.2 Why Multiple Layers?

Market stress propagates through different channels. During crises, correlations rise sharply, sectors move together, and sentiment amplifies volatility. A single graph layer cannot capture these mechanisms.

The multiple layers serve different analytical functions:

* •

  The correlation layer measures temporal dependencies.
* •

  The sector/factor layer models structural exposure.
* •

  The sentiment layer captures behavioral amplification.

Multiple layers allow the model to isolate distinct causes of systemic fragility rather than treating the market as homogeneous.

### 4.3 Node Features

Node features include a combination of micro-level and macro-level variables:

|  |  |  |
| --- | --- | --- |
|  | Xt​(i)=[return features,volatility,drawdowns,macro indicators].X\_{t}(i)=[\text{return features},\text{volatility},\text{drawdowns},\text{macro indicators}]. |  |

These features provide the local information required by the GNN to evaluate node-level and sector-level behavior.

### 4.4 Edge Dynamics

Edges are allowed to evolve as the market evolves. For instance, the correlation layer updates at each time step using a rolling window. Similarly, the sector layer may remain relatively stable, while the sentiment layer may change rapidly in periods of elevated news or social activity.

Thus, SRR captures two important mechanisms:

* •

  short-term dynamics from the correlation layer,
* •

  structural or long-term effects from the sector and factor layers.

### 4.5 Interpretability Benefits

Interpretability matters for systemic-risk applications. Multi-layer graphs support interpretability naturally. During stress periods, certain layers dominate. Correlation spikes precede crashes; sector clustering intensifies during prolonged downturns. The model can compare or isolate contributions from different layers for practical attribution of systemic risk.

This multi-layer representation is aligned with theoretical models of financial networks in which the topology of exposures plays a central role in determining the severity of contagion  (elliott2014financial; glasserman2015contagion).

Correlation layerSector / factor layerSentiment layerABTechFinancialsRedditNews


Figure 1: Illustrative multi-layer graph for SRR. The correlation layer captures return co-movement, the sector/factor layer captures structural exposure, and the sentiment layer captures behaviorally driven co-movement. Multiple edge types enable the model to disentangle different forms of market connectivity.

## 5 Temporal GNN Architecture and Mathematical Framework

Prior work applies temporal and graph-based neural architectures to financial risk prediction  (huang2020financialgnn; feng2019temporalgnn). SRR extends this by combining multi-layer structural information with regime-oriented targets for systemic risk.

SRR combines multi-layer graph learning with temporal representation learning to identify transitions into systemic risk regimes. This section describes the core architecture, mathematical formulation, and training objective. Instead of forecasting individual price movements, the model estimates when risk states emerge by learning how market structure evolves.

### 5.1 Node and Graph Embeddings

Given a market graph 𝒢t=(V,Et)\mathcal{G}\_{t}=(V,E\_{t}) at time tt, let Xt∈ℝN×dX\_{t}\in\mathbb{R}^{N\times d} denote the node features. A graph neural network encoder fθf\_{\theta} maps the graph to a latent embedding:

|  |  |  |
| --- | --- | --- |
|  | Zt=fθ​(𝒢t,Xt).Z\_{t}=f\_{\theta}(\mathcal{G}\_{t},X\_{t}). |  |

This embedding summarizes structural properties of the market at time tt and is computed for every multi-layer graph.

The encoder can use different GNN layers. We consider multiple variants to avoid restricting SRR to one architecture.

### 5.2 GAT-based Encoder

In the GAT variant, node embeddings are computed using attention coefficients:

|  |  |  |
| --- | --- | --- |
|  | hi′=σ​(∑j∈𝒩​(i)αi​j​W​hj)h^{\prime}\_{i}=\sigma\left(\sum\_{j\in\mathcal{N}(i)}\alpha\_{ij}Wh\_{j}\right) |  |

where the attention score is:

|  |  |  |
| --- | --- | --- |
|  | αi​j=softmaxj​(a⊤​[W​hi∥W​hj]).\alpha\_{ij}=\text{softmax}\_{j}(a^{\top}[Wh\_{i}\parallel Wh\_{j}]). |  |

This mechanism assigns importance to different nodes and edges, useful when connectivity spikes during crises.

### 5.3 Transformer-based Encoder

Alternatively, the graph encoder can use Transformer-style aggregation:

|  |  |  |
| --- | --- | --- |
|  | H′=MultiHeadSelfAttention​(H)+H.H^{\prime}=\text{MultiHeadSelfAttention}(H)+H. |  |

This captures higher-order and global dependencies beyond local neighborhood aggregation.

We use a general formulation so the same temporal modeling framework applies regardless of the GNN block choice.

### 5.4 Temporal Modeling

Systemic instability manifests over time. SRR obtains a sequence of graph embeddings:

|  |  |  |
| --- | --- | --- |
|  | (Zt−k,…,Zt).(Z\_{t-k},\dots,Z\_{t}). |  |

We apply a temporal encoder gϕg\_{\phi} that learns evolving market dynamics:

|  |  |  |
| --- | --- | --- |
|  | ht=gϕ​(Zt−k,…,Zt)h\_{t}=g\_{\phi}(Z\_{t-k},\dots,Z\_{t}) |  |

where gϕg\_{\phi} can be:

* •

  an LSTM for sequence-level information,
* •

  a GRU for shorter-term dependencies,
* •

  a Transformer for long-range patterns.

These choices let the model generalize across applications and datasets.

### 5.5 Prediction Layer

The temporal representation is used for crash-regime estimation:

|  |  |  |
| --- | --- | --- |
|  | y^t=σ​(W​ht+b).\hat{y}\_{t}=\sigma(Wh\_{t}+b). |  |

We optimize:

|  |  |  |
| --- | --- | --- |
|  | ℒ=−∑t(yt​log⁡y^t+(1−yt)​log⁡(1−y^t)).\mathcal{L}=-\sum\_{t}\big(y\_{t}\log\hat{y}\_{t}+(1-y\_{t})\log(1-\hat{y}\_{t})\big). |  |

### 5.6 Interpretability

SRR is interpretable: both GAT attention maps and Transformer attention weights can be inspected. During stress periods, certain nodes or sectors become dominant:

|  |  |  |
| --- | --- | --- |
|  | αi​j→1​ for nodes contributing to fragility.\alpha\_{ij}\to 1\text{ for nodes contributing to fragility.} |  |

We can then perform attribution and scenario simulation in downstream analysis.

Gt−kG\_{t-k}Gt−k+1G\_{t-k+1}GtG\_{t}zt−kz\_{t-k}zt−k+1z\_{t-k+1}ztz\_{t}Graph encoder fθf\_{\theta}Temporal encoder(LSTM / GRU / Transformer)y^t\hat{y}\_{t}


Figure 2: Temporal GNN view of SRR. Each graph snapshot Gt−k,…,GtG\_{t-k},\ldots,G\_{t} is encoded into a latent vector zt−k,…,ztz\_{t-k},\ldots,z\_{t} by a graph encoder fθf\_{\theta}. A temporal encoder aggregates these embeddings and produces a crash-regime probability y^t\hat{y}\_{t}.

### 5.7 Model Objective

Instead of minimizing prediction error on individual returns, the model estimates whether the future horizon contains a systemic risk event. SRR detects transitions even when price movements have not yet materialized.

### 5.8 Snapshot GNN Architecture Used in Experiments

The snapshot GNN evaluated in the experiments is a two-layer GCN with ReLU
activation and global mean pooling. The architecture configuration is:

* •

  Layer 1: GCNConv(FF, 32)
* •

  Layer 2: GCNConv(32, 32)
* •

  Pooling: GlobalMeanPool
* •

  Classifier: 2-layer MLP (32 → 16 → 1)

For this baseline, we use only the correlation layer of the graph
(i.e., 𝒢t1\mathcal{G}\_{t}^{1}). The sector/factor and sentiment layers are excluded
to isolate the predictive value of structural correlation networks. This snapshot
model serves as the primary graph-based baseline for comparison to the
simplified temporal GNN.

### 5.9 Temporal GNN Prototype Used in Experiments.

The temporal SRR model used in the experiments is a simplified prototype rather than the full architecture described earlier. It reuses the snapshot GCN encoder from Section 5.8 to produce graph embeddings for a short sequence of daily correlation graphs and then applies a single recurrent layer (implemented as a GRU in the codebase) to aggregate these embeddings into a sequence representation. A logistic output layer maps the temporal hidden state to a crash-regime probability.

Importantly, this prototype:

* •

  Uses only the correlation layer Gt1G\_{t}^{1} of the multi-layer graph.
* •

  Operates on relatively short sequences.
* •

  Does not yet incorporate the additional sector/factor or sentiment layers.

The goal of this model is to provide a first temporal baseline on top of correlation networks, rather than a fully validated implementation of the complete SRR design.

## 6 Algorithms and Pipeline

SRR is designed as a modular system that ingests raw market data, constructs multi-layer graphs, learns structural representations using a graph encoder, and uses a temporal model to forecast transitions into systemic risk regimes. This section describes the end-to-end workflow and the algorithms used in each stage.

### 6.1 End-to-End Pipeline

The pipeline consists of four major components:

1. 1.

   Data ingestion and preprocessing.
2. 2.

   Multi-layer graph construction.
3. 3.

   Graph and temporal representation learning.
4. 4.

   Crash-regime prediction and interpretation.

These steps are executed sequentially during training and periodically during inference.

### 6.2 Multi-Layer Graph Construction

To operationalize SRR, we construct a time-indexed sequence of graphs
{𝒢t}\{\mathcal{G}\_{t}\} capturing short-horizon market structure. Although the full SRR
architecture supports multiple layers, our empirical study focuses on the correlation
layer in order to isolate the contribution of graph topology.

#### Rolling Window and Correlation Edges.

At each time step tt, we compute log returns and apply a short rolling window
(seven days in our implementation) to estimate pairwise Spearman correlations.
Edges are created according to

|  |  |  |
| --- | --- | --- |
|  | (i,j)∈Etiff|ρi​j​(t)|≥τ,(i,j)\in E\_{t}\quad\text{iff}\quad|\rho\_{ij}(t)|\geq\tau, |  |

with τ=0.5\tau=0.5. This produces sparse yet expressive correlation networks that
respond quickly to changes in market co-movement.

#### Node Features.

Each node is augmented with a small set of features including daily returns, rolling
volatility, drawdown indicators, and momentum. These lightweight features allow
the experiments to emphasize the role of graph structure rather than complex
feature design.

#### Graph Sequences for Temporal Modeling.

For snapshot GNN experiments, only 𝒢t\mathcal{G}\_{t} is used. For the temporal
prototype, a fixed-length buffer collects the most recent kk graphs
(k=5k=5 in our experiments). This yields sequences
(𝒢t−k+1,…,𝒢t)(\mathcal{G}\_{t-k+1},\dots,\mathcal{G}\_{t}) that serve as input to the GRU-based
temporal encoder described in Section 5.

Algorithm 1  Multi-Layer Graph Construction

1:Market data stream DD, window size WW

2:for each time tt do

3:  Extract returns and indicators.

4:  Compute correlation matrix over window WW.

5:  Construct correlation layer 𝒢t1\mathcal{G}\_{t}^{1}.

6:  Construct sector/factor layer 𝒢t2\mathcal{G}\_{t}^{2}.

7:  (Optional) Build sentiment layer 𝒢t3\mathcal{G}\_{t}^{3}.

8:  Form multi-layer graph 𝒢t={𝒢t1,𝒢t2,𝒢t3}\mathcal{G}\_{t}=\{\mathcal{G}\_{t}^{1},\mathcal{G}\_{t}^{2},\mathcal{G}\_{t}^{3}\}.

9:end for

### 6.3 Training Procedure

Training SRR models requires generating forward-looking labels and ensuring
chronological integrity in evaluation.

#### Label Definition.

A node-day (i,t)(i,t) is labeled as a crash indicator if instrument ii experiences a
drawdown exceeding a fixed threshold within the next 60 days. This provides an
early-warning target and avoids using information contemporaneous with the graph.

#### Snapshot GNN Training.

The snapshot model is trained on individual graphs using binary cross-entropy loss,
Adam optimization (learning rate 10−310^{-3}), and mini-batches of size 8. A
chronological 80/20 train–test split is used to prevent lookahead bias. This setup
provides a simple baseline for understanding the predictive value of correlation
network structure.

#### Temporal Prototype Training.

The temporal GNN prototype trains on short sequences of graphs rather than
single snapshots. For each tt, we extract a sequence window of the most recent
kk graphs and apply the GRU-based temporal encoder to the sequence of GCN
embeddings. Hyperparameters mirror the snapshot model to maintain comparability.

#### Evaluation.

Models are evaluated using AUROC, AUPRC, precision, recall, accuracy, and FPR.
Because crisis periods are short and imbalanced, we do not apply class
balancing or calibration; this allows the experiments to reveal natural behaviors
of correlation-based GNNs under different stress regimes.

Algorithm 2  SRR Training

1:Graph sequence (𝒢t−k,…,𝒢t)(\mathcal{G}\_{t-k},\dots,\mathcal{G}\_{t})

2:for each minibatch do

3:  Compute graph embeddings Zt−i=fθ​(𝒢t−i,Xt−i)Z\_{t-i}=f\_{\theta}(\mathcal{G}\_{t-i},X\_{t-i}).

4:  Form temporal sequence (Zt−k,…,Zt)(Z\_{t-k},\dots,Z\_{t}).

5:  Compute prediction y^t=σ​(W​ht+b)\hat{y}\_{t}=\sigma(Wh\_{t}+b).

6:  Evaluate loss ℒ\mathcal{L}.

7:  Update model parameters using gradient descent.

8:end for

### 6.4 Inference Mode

During inference, the model receives the latest graph window and outputs the probability of entering a systemic state:

|  |  |  |
| --- | --- | --- |
|  | y^t=SRR​(𝒢t−k,…,𝒢t).\hat{y}\_{t}=\text{SRR}(\mathcal{G}\_{t-k},\dots,\mathcal{G}\_{t}). |  |

The output may be converted into a warning index or binary alert:

|  |  |  |
| --- | --- | --- |
|  | y^t>γ⇒Systemic Risk Warning.\hat{y}\_{t}>\gamma\Rightarrow\text{Systemic Risk Warning}. |  |

### 6.5 Model Complexity

By design, SRR separates representation into two components:

* •

  Graph embeddings: complexity depends on number of nodes and layers.
* •

  Temporal encoder: complexity depends on sequence length.

This modular design enables scalability across:

* •

  larger universes of instruments,
* •

  longer historical windows,
* •

  additional graph layers.

### 6.6 Practical Advantages

Beyond predictive performance, SRR exhibits several practical design advantages. The algorithmic structure of SRR has two advantages:

1. 1.

   It preserves the temporal ordering of market structure changes.
2. 2.

   It decouples micro, meso, and macro drivers, which is essential when analyzing systemic risk.

By combining graph-level structure and temporal evolution, the pipeline captures macro fragility more effectively than models that operate on single assets or aggregate statistics.
Figure [3](https://arxiv.org/html/2512.17185v1#S6.F3 "Figure 3 ‣ 6.6 Practical Advantages ‣ 6 Algorithms and Pipeline ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") provides an overview of the end-to-end SRR pipeline.

Preprocessing& featuresMarket &macro dataMulti-layergraph builderGraph encoder(GCN / GAT)TemporalencoderSRR outputrisk score


Figure 3: High-level SRR pipeline. Raw market and macro data are transformed into features, used to construct multi-layer graphs, encoded with a GNN, and fed into a temporal encoder that produces a systemic risk score or warning.

We present the high-level SRR architecture and a summary of model performance across crises in Figure [4](https://arxiv.org/html/2512.17185v1#S6.F4 "Figure 4 ‣ 6.6 Practical Advantages ‣ 6 Algorithms and Pipeline ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction").

Market Data(yfinance)Macro Data(FRED, VIX)Sentiment(News)Feature EngineeringF=7F=7 node featuresGraph ConstructionN=44N=44, τ=0.5\tau=0.5Label Generation10% drawdownBaselineLogistic Reg.Random Forest∼\sim300-50K params
Static GNN2-layer GCNGlobal Pool4,737 params
Temporal GNNGCN Encoder+ GRU29,697 params
Evaluation: AUROC, Precision, Recall
DATA LAYERFEATURE ENGINEERINGMODELSEVALUATION

| Crisis | Model | AUROC | Prec. | Rec. | Acc. |
| --- | --- | --- | --- | --- | --- |
| Dot-com (1998-2003) | Logistic Reg. | 0.463 | 0.592 | 0.438 | 0.470 |
| Random Forest | 0.291 | 0.601 | 0.948 | 0.581 |
| Static GNN | 0.412 | 0.613 | 1.000 | 0.613 |
| Temporal GNN | 0.589 | 0.607 | 1.000 | 0.607 |
| GFC (2006-2011) | Logistic Reg. | 0.738 | 0.824 | 0.977 | 0.808 |
| Random Forest | 0.529 | 0.827 | 1.000 | 0.827 |
| Static GNN | 0.248 | 0.823 | 1.000 | 0.823 |
| Temporal GNN | 0.232 | 0.820 | 1.000 | 0.820 |
| COVID-19 (2018-2021) | Logistic Reg. | — | 1.000 | 0.823 | 0.823 |
| Random Forest | — | 1.000 | 0.967 | 0.967 |
| Static GNN | 0.000 | 1.000 | 1.000 | 1.000 |
| Temporal GNN | 0.000 | 1.000 | 1.000 | 1.000 |

Figure 4: System architecture and performance summary. Top: Data is transformed
into features, multi-layer graphs, and evaluated using baseline ML, snapshot
GNN, and Temporal GNN models. Bottom: The temporal GNN prototype shows improved AUROC on the Dot-com period relative to the snapshot GNN, while performance in other crises reflects the limitations of correlation-only
temporal modeling.

## 7 Experiments and Evaluation

This section evaluates the ability of SRR-style graph models to detect systemic risk regimes across major historical stress periods. The goal of the experimental design is not to forecast individual returns, but to measure the ability of simple graph-based models to provide early warning signals of market-wide fragility.

#### Clarification on the Temporal GNN.

In this work, the “Temporal GNN” appearing in the results refers to a simplified prototype model consisting of a two-layer GCN encoder followed by a single-layer GRU applied over short graph sequences (5 days). This model is included to illustrate the potential benefits of incorporating temporal structure. It is not the full SRR temporal architecture, which additionally includes multi-layer graph fusion, longer-range sequence modeling, and attention-based aggregation. The full SRR temporal model is part of ongoing work and is not evaluated in this version of the paper. All results reported here correspond to the simplified temporal baseline.

### 7.1 Datasets

We evaluate the models on publicly available historical equity and index data, focusing on three crisis periods that differ in origin and market structure:

* •

  Dot-com crash (2000–2002),
* •

  Global Financial Crisis (2008–2010),
* •

  COVID shock (2020).

For each crisis period, we construct daily features for a universe of sector exchange-traded funds (ETFs) and large, liquid stocks. Node-level features include returns, rolling volatility, drawdowns, and momentum indicators, combined with macro overlays such as credit spreads and yield-curve proxies. Labels are defined using forward drawdowns: a node-day is labelled as “crisis” if its price experiences a drawdown larger than a fixed percentage threshold within a specified future horizon (e.g., 20 days). This design allows us to test whether changes in graph structure precede large losses.

### 7.2 Baselines and Current SRR Prototype

We compare four model families:

* •

  Logistic regression on hand-engineered node features and macro indicators,
* •

  Random Forest on the same feature set,
* •

  Snapshot GNN: the two-layer GCN encoder described in Section 5.8 applied to
  single-day correlation graphs,
* •

  Temporal GNN prototype: the simplified SRR instantiation described in
  Section 5.9, which applies a GRU over short sequences of snapshot GNN embeddings.

The snapshot and temporal GNNs share the same correlation-based graph representation but differ in how they aggregate information over time. The temporal model is an *implemented prototype* of SRR: it adds sequence modeling to correlation graphs but omits sector/factor and sentiment layers and advanced temporal variants (Transformer encoders, multi-horizon heads) that the full SRR framework includes. All *Temporal GNN* results use this prototype configuration. Future work will extend experiments to the complete multi-layer temporal SRR model.

Our baselines align with prior systemic risk and contagion modeling studies  (battiston2012debtrank; acemoglu2015systemic; brunnermeier2009liquidity), which emphasize capturing both local and system-wide indicators.

### 7.3 Evaluation Metrics

We evaluate classification performance using a standard set of metrics:

|  |  |  |
| --- | --- | --- |
|  | AUROC,AUPRC,Precision,Recall,Accuracy.\text{AUROC},\quad\text{AUPRC},\quad\text{Precision},\quad\text{Recall},\quad\text{Accuracy}. |  |

Since early detection is more important than overall accuracy, we also compute the lead-time of warnings relative to realized drawdowns. For each detected warning, the lead-time is defined as the number of days between the warning and the onset of the subsequent crash window. We summarize this distribution across all warnings and crisis periods.

### 7.4 Quantitative Results

Table 2: summarizes the performance of each model across the three crisis periods. AUROC is reported when it is well-defined for the corresponding dataset; when label imbalance makes the ROC curve degenerate, we omit AUROC and focus on precision, recall, and accuracy.

| Crisis | Model | AUROC | Precision | Recall | Accuracy |
| --- | --- | --- | --- | --- | --- |
| Dot-com | Logistic Regression | 0.463 | 0.592 | 0.438 | 0.470 |
| Dot-com | Random Forest | 0.291 | 0.601 | 0.948 | 0.581 |
| Dot-com | GNN | 0.412 | 0.613 | 1.000 | 0.613 |
| GFC | Logistic Regression | 0.738 | 0.824 | 0.977 | 0.808 |
| GFC | Random Forest | 0.529 | 0.827 | 1.000 | 0.827 |
| GFC | GNN | 0.248 | 0.823 | 1.000 | 0.823 |
| COVID-19 | Logistic Regression | – | 1.000 | 0.823 | 0.823 |
| COVID-19 | Random Forest | – | 1.000 | 0.967 | 0.967 |
| COVID-19 | GNN | 0.000 | 1.000 | 1.000 | 1.000 |

The results show that no single model dominates across all crises. Logistic regression achieves reasonable AUROC during the global financial crisis, while Random Forest tends to produce higher recall at the cost of more false positives. The snapshot GNN baseline performs comparably to these methods in most settings but does not yet capture temporal dynamics, which we expect to be important for full SRR.

Figure [5](https://arxiv.org/html/2512.17185v1#S7.F5 "Figure 5 ‣ 7.4 Quantitative Results ‣ 7 Experiments and Evaluation ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") compares baseline and GNN-based models across the three crisis regimes.

![Refer to caption](figures/model_comparison.png)


Figure 5: Aggregate comparison of logistic regression, Random Forest, and a snapshot GNN baseline across crisis periods. Bars summarize AUROC, precision, recall, and accuracy for each model.

### 7.5 Error Analysis

To better understand the trade-offs between sensitivity and false alarms, we examine confusion matrices and error statistics. The Random Forest model achieves high recall but at the cost of non-trivial false positive rates, which may be acceptable in early-warning applications but would require careful calibration for practical deployment. See Appendix [D](https://arxiv.org/html/2512.17185v1#A4 "Appendix D Detailed Error Analysis ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") for detailed confusion matrices, error counts, and false positive rate analysis.

### 7.6 ROC and Precision–Recall Curves

To visualize the trade-off between detection quality and false alarms, we plot ROC and precision–recall curves derived from the experiments.

We report ROC curves for each model and crisis period in Figure [6](https://arxiv.org/html/2512.17185v1#S7.F6 "Figure 6 ‣ 7.6 ROC and Precision–Recall Curves ‣ 7 Experiments and Evaluation ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction").

![Refer to caption](figures/roc_curves.png)


Figure 6: ROC curves comparing baseline models across crisis periods. Curves illustrate the trade-off between hit rate and false alarms.

Figure [7](https://arxiv.org/html/2512.17185v1#S7.F7 "Figure 7 ‣ 7.6 ROC and Precision–Recall Curves ‣ 7 Experiments and Evaluation ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") shows the corresponding precision–recall curves.

![Refer to caption](figures/pr_curves.png)


Figure 7: Precision–recall curves for crash-regime classification, highlighting performance in the imbalanced label setting.

### 7.7 Cross-Crisis Performance Differences

The GNN models obtain AUROC = 0.000 during the COVID–19 period, reflecting a structural mismatch between correlation-only graph representations and the exogenous, policy-driven dynamics of the COVID–19 shock. This failure highlights the importance of incorporating additional SRR layers to capture sectoral exposure and sentiment-driven cascades. Appendix [E](https://arxiv.org/html/2512.17185v1#A5 "Appendix E Why the GNN Fails on the COVID–19 Crisis ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") analyzes why correlation-based GNNs fail on COVID–19.

### 7.8 Lead-Time Analysis

For many events, warnings precede realized drawdowns by several days to weeks. However, there are also late warnings and missed events, underscoring the need for richer temporal modelling—one of the main motivations for the full SRR architecture. Figure [8](https://arxiv.org/html/2512.17185v1#S7.F8 "Figure 8 ‣ 7.8 Lead-Time Analysis ‣ 7 Experiments and Evaluation ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") shows the empirical distribution of lead-times for the Random Forest and GNN baselines, aggregated over the different crisis periods. Appendix [D](https://arxiv.org/html/2512.17185v1#A4 "Appendix D Detailed Error Analysis ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") provides detailed false positive rate analysis across models and crises.

We analyze the distribution of lead times in Figure [8](https://arxiv.org/html/2512.17185v1#S7.F8 "Figure 8 ‣ 7.8 Lead-Time Analysis ‣ 7 Experiments and Evaluation ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction").

![Refer to caption](figures/lead_time_analysis.png)


Figure 8: Lead-time distribution for early-warning signals produced by the Random Forest and GNN baselines. Longer lead-times indicate that warnings occur earlier before large drawdowns.

### 7.9 Risk Timeline and Qualitative Behavior

We examine how warning signals evolve over time. Figure [9](https://arxiv.org/html/2512.17185v1#S7.F9 "Figure 9 ‣ 7.9 Risk Timeline and Qualitative Behavior ‣ 7 Experiments and Evaluation ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") shows model scores and realized crises during a selected period spanning the GFC and COVID episodes. During Dot-com and GFC periods, model scores rise gradually as correlations intensify, consistent with structural fragility accumulation. In contrast, COVID–19 exhibits sharp, irregular spikes reflecting its exogenous nature. Appendix [F](https://arxiv.org/html/2512.17185v1#A6 "Appendix F Extended Qualitative Analysis ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") provides extended analysis of signal stability patterns and threshold considerations.

![Refer to caption](figures/risk_timeline.png)


Figure 9: Example of model warning scores over time, with shaded regions denoting realized crisis windows. Elevated model scores tend to cluster around periods of heightened market stress.

An additional plot (Figure [10](https://arxiv.org/html/2512.17185v1#S7.F10 "Figure 10 ‣ 7.9 Risk Timeline and Qualitative Behavior ‣ 7 Experiments and Evaluation ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction")) disaggregates the predictions and highlights how warnings intensify as systemic stress accumulates.

Figure [10](https://arxiv.org/html/2512.17185v1#S7.F10 "Figure 10 ‣ 7.9 Risk Timeline and Qualitative Behavior ‣ 7 Experiments and Evaluation ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") visualizes the daily prediction scores during the test window.

![Refer to caption](figures/prediction_timeline.png)


Figure 10: Prediction timeline for a representative subset of instruments, showing how predicted risk increases as the system transitions into and out of crisis regimes.

### 7.10 Interpretability and Feature Influence

To better understand what drives the models, we analyze feature importance and graph-based attribution. Figure [11](https://arxiv.org/html/2512.17185v1#S7.F11 "Figure 11 ‣ 7.10 Interpretability and Feature Influence ‣ 7 Experiments and Evaluation ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") shows a global feature importance ranking for the Random Forest model. Nodes corresponding to highly liquid sector ETFs receive elevated attention weights in the GNN, suggesting focus on broad market structure rather than idiosyncratic volatility. Appendix [G](https://arxiv.org/html/2512.17185v1#A7 "Appendix G Interpretability and Attribution Analysis ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") discusses interpretability patterns across crisis regimes and attention-based attribution analysis.

![Refer to caption](figures/feature_importance.png)


Figure 11: Feature importance scores for the Random Forest baseline. Volatility, drawdown, and correlation-derived features play a prominent role in most crisis periods.

We now summarize the key empirical findings.

### 7.11 Results Summary

Empirically, these preliminary experiments support three observations:

1. 1.

   Simple graph-based models are competitive with standard baselines and offer a natural foundation for systemic risk analysis.
2. 2.

   Different crisis periods favor different models, suggesting that no single scalar metric is sufficient to evaluate early-warning systems.
3. 3.

   There is clear room for improvement through temporal and multi-layer modeling, which is exactly the direction pursued by the full SRR framework.

Together, these results provide an initial validation that structural market information encoded in graphs carries useful signal for systemic risk detection, and they motivate the ongoing development of SRR as a temporal, multi-layer extension of these baselines.

### 7.12 Cross-Crisis Generalization

Systemic fragility arises from different mechanisms in different crises (e.g.,
the Dot-com bubble was driven by sector-specific overvaluation, whereas the
GFC reflected credit contagion). Therefore, strong out-of-sample generalization
across crisis regimes is not necessarily expected. However, such tests provide
important robustness diagnostics. In future work we plan to evaluate SRR models
trained on one crisis (e.g., GFC) and tested on another (e.g., COVID-19) to assess
transferability across structurally distinct stress events.

## 8 Integration with SPA and AIMM

SRR was motivated in part by two earlier research systems: the Stock Pattern Assistant (SPA  (neela2025spa)) and the AI-based Market Manipulation Model (AIMM  (neela2025aimm)). These systems focus on micro-level market structure and abnormal sentiment windows. SRR extends these approaches to macro-level systemic fragility.

### 8.1 Complementary Perspectives on Risk

SPA  (neela2025spa) detects structural price patterns and local momentum regimes. These patterns are highly predictive of short-term continuation or reversal events, but they do not attempt to characterize market-wide instability.
AIMM  (neela2025aimm) captures a different class of signals by detecting abnormal sentiment and manipulation windows. This is useful in environments where shocks are driven by news or social amplification instead of traditional financial triggers.

SRR introduces a third perspective:

* •

  SPA: micro-level pattern dynamics,
* •

  AIMM: sentiment and manipulation activity,
* •

  SRR: structural macro fragility.

Together, they represent a multi-scale framework for studying financial risk.

SPA  (neela2025spa) and AIMM  (neela2025aimm) capture micro- and meso-level dynamics, respectively, while SRR focuses on macro structural fragility. Together they form a multi-scale view of instability that spans patterns, sentiment, and systemic
structure.

### 8.2 A Multi-Scale Architecture for Market Events

The three systems address different layers of market behavior:

* •

  Micro level (SPA): pattern, momentum, and structural runs.
* •

  Meso level (AIMM): sentiment-driven abnormal coordination.
* •

  Macro level (SRR): cross-sector and system-wide fragility.

This multi-scale view is consistent with empirical studies of financial crises, which show that instability emerges from interactions across time horizons and information channels.

### 8.3 Information Flow Between Systems

While each system functions independently, the outputs can feed one another. For example:

* •

  SRR can provide a macro regime indicator to AIMM or SPA,
* •

  SPA can detect micro patterns that evolve into systemic risk,
* •

  AIMM can identify sentiment shocks that propagate into the system.

The three systems collectively define a hierarchical modeling pipeline that captures different forms of market stress.

### 8.4 Practical Applications

Such a multi-model system has relevance not only for academic research but also for practical applications such as:

* •

  early-warning tools for regulators and financial institutions,
* •

  macro trading or risk hedging strategies,
* •

  real-time stress monitoring platforms.

In this context, SRR fills a gap in existing approaches by identifying structural transitions before they are visible in price movements alone.

## 9 Limitations

SRR has several limitations in its current form:

* •

  Snapshot and simplified temporal GNN only. We evaluate a snapshot GNN baseline and a simplified temporal prototype, not the full temporal SRR architecture. The experiments do not reflect the full benefits of sequence modeling central to complete SRR design.
* •

  Crisis-specific sensitivity. Model performance varies across crisis regimes (Dot-com, GFC, COVID), indicating that structural drivers differ by period. Further robustness testing is needed.
* •

  Label imbalance. Some crisis intervals show imbalance between crash and non-crash labels, making AUROC unreliable. Precision–recall metrics help but more advanced imbalance-aware methods would be better.
* •

  No sentiment or cross-asset inputs yet. SRR is designed for multi-layer graphs (sentiment, credit spreads, cross-asset linkages) but current experiments use only correlation graphs with a snapshot GCN and simplified temporal GNN prototype. This validates graph-derived structure and a first temporal extension but does not test the full multi-layer SRR architecture with sector/factor and sentiment layers. Current evidence is preliminary and correlation-focused. Full SRR validation requires experiments with all layers and temporal variants.
* •

  Limited horizon diversity. We use a single prediction horizon. Multi-horizon experiments (5-, 10-, 20-day windows) are needed to assess SRR’s temporal sensitivity.
* •

  No out-of-crisis generalization tests. Models are evaluated within each crisis window, not across crises (e.g., train on GFC → test on COVID). Cross-crisis transfer tests are needed to understand generalization.

These limitations reflect early-stage empirical evaluation, not fundamental framework weaknesses. Addressing them is the focus of planned extensions in future work.

## 10 Reproducibility

To encourage transparent evaluation and future research, we adopt the following reproducibility practices:

* •

  We avoid look-ahead bias and ensure that training and prediction windows do not overlap.
* •

  We publish hyperparameters, rolling windows, training procedure, and validation approach.
* •

  All preprocessing and feature extraction steps are deterministic and documented.
* •

  The data sources used are publicly available and reproducible.

These guidelines are aligned with current recommendations for reproducible AI and financial forecasting research.

## 11 Ethical Considerations

This work focuses on systemic risk measurement and analysis, not on trading, portfolio construction, or automated decision-making. SRR is designed as a research tool for understanding structural fragility in financial markets, and its outputs should not be used directly for investment or risk-taking decisions.

Predictive models in finance can influence behavior if misinterpreted or deployed without proper safeguards. In particular, false positives may create unnecessary concern, while false negatives may lead to overconfidence during periods of elevated market vulnerability. To mitigate these risks, SRR emphasizes interpretability and transparency, allowing practitioners to inspect feature attributions, network connectivity patterns, and underlying assumptions.

The data used in this research consists solely of publicly available market and macroeconomic time series. No personally identifiable information (PII) or private institutional data is used, and no model decisions affect individuals or protected groups. However, systemic risk models may indirectly affect market participants if used in risk governance. For that reason, SRR should complement human expertise, regulatory oversight, and established macro-financial stress-testing frameworks rather than replace them.

Continued ethical development requires careful validation across markets, explicit communication of uncertainty, and avoidance of overstated confidence in model predictions. SRR aims to support responsible adoption of AI in systemic risk research by providing interpretable tools that encourage informed, cautious analysis rather than automated decision-making.

This work is intended solely for research and educational purposes and is not a trading or investment advisory system. Any use of the SRR outputs in practice should be embedded within formal risk-governance processes and human oversight.

## 12 Broader Impact

Systemic risk is a defining challenge for modern financial systems, where tightly coupled markets, automated trading, and rapid information diffusion can amplify stress far beyond individual institutions. Tools that can identify emerging fragility therefore have potential value for regulators, risk managers, and researchers working to promote financial stability. The SRR framework contributes to this effort by providing a transparent and modular approach to analyzing structural dependencies in market behavior.

While SRR is not designed or intended for trading applications, its insights could support early-warning analysis, scenario design, and stress-testing frameworks. By emphasizing explainability—through attribution, feature influence, and graph-based interpretation—SRR also encourages responsible use of machine learning in finance, where opaque models can complicate oversight and risk governance.

At the same time, any model that produces risk assessments or alerts must be used with care. Overreliance on model outputs, inappropriate deployment in high-stakes environments, or misinterpretation of warnings could introduce unintended consequences, including unnecessary market reactions. For this reason, SRR should be viewed as a research tool that complements, rather than replaces, domain expertise, regulatory judgment, and traditional macro-financial analysis.

The broader societal impact of SRR lies in its potential to improve understanding of systemic dynamics, encourage the development of transparent and interpretable financial AI, and provide a foundation for future research into market stability and early-warning systems. Continued work is needed to evaluate robustness across assets, geographies, and data regimes, and to ensure that models such as SRR are applied ethically and responsibly.

## 13 Conclusion and Future Work

We introduced Systemic Risk Radar (SRR), a framework for forecasting systemic fragility using multi-layer market graphs. Instead of modeling individual price movements, SRR tracks structural evolution—correlations, sector linkages, behavioral co-movements—that precede instability.

Our experiments show that simple graph-based baselines (two-layer GCN snapshots, simplified temporal GNN prototypes) capture meaningful early-warning signals across the Dot-com crash, Global Financial Crisis, and COVID-19 shock. This supports SRR’s premise: structural market information predicts systemic transitions, and graph representations form a natural foundation for early-warning tools.

The results also reveal limitations. Snapshot GNNs ignore temporal dependencies and perform inconsistently across crisis types. The full SRR architecture—with temporal sequence modeling (LSTM/GRU) and multi-layer attention—should improve stability, reduce false alarms, and detect fragility earlier.

SRR offers a modular, interpretable framework for systemic risk research. Integrating graph structure, temporal dynamics, and explainability moves toward practical early-warning systems for financial stability monitoring.

This version of SRR should be interpreted as a proposal paper with
preliminary empirical evidence demonstrating the value of graph-derived
structural features. A full evaluation of the complete SRR architecture—
including multi-layer integration and advanced temporal modeling—is left for
subsequent work.

### Future Work

Future extensions of this research will focus on:

* •

  Temporal SRR model evaluation: Training and benchmarking the full temporal SRR architecture with LSTM/GRU or Transformer encoders to quantify improvements over snapshot GNN baselines.
* •

  Sentiment layer integration: Incorporating Reddit, news, or Twitter sentiment to enrich the multi-layer graph representation and analyze behavioral contagion channels.
* •

  Multi-horizon prediction: Expanding the prediction task to 5-, 10-, and 20-day windows to capture short-, medium-, and long-term systemic risk behavior.
* •

  Cross-crisis generalization: Evaluating models trained on one crisis (e.g., GFC) and tested on another (e.g., COVID) to measure robustness and transferability.
* •

  Temporal attention explainability: Analyzing attention patterns from temporal encoders to identify early signals of fragility and key points of structural transition.

## Appendix

## Appendix A Extended Mathematical Formulation

For completeness, we provide additional mathematical details and notational variants of the architecture. Let 𝒢t\mathcal{G}\_{t} denote a multi-layer graph with layers {𝒢t1,…,𝒢tM}\{\mathcal{G}\_{t}^{1},\dots,\mathcal{G}\_{t}^{M}\} and node features XtX\_{t}.

The GNN encoder produces:

|  |  |  |
| --- | --- | --- |
|  | Zt=fθ​(𝒢t,Xt).Z\_{t}=f\_{\theta}(\mathcal{G}\_{t},X\_{t}). |  |

The temporal encoder takes the form:

|  |  |  |
| --- | --- | --- |
|  | ht=gϕ​(Zt−k:t).h\_{t}=g\_{\phi}(Z\_{t-k:t}). |  |

Alternative loss formulations may include focal loss to account for class imbalance:

|  |  |  |
| --- | --- | --- |
|  | ℒfocal=−∑t(1−y^t)γ​yt​log⁡y^t,\mathcal{L}\_{\text{focal}}=-\sum\_{t}(1-\hat{y}\_{t})^{\gamma}y\_{t}\log\hat{y}\_{t}, |  |

which we leave for future work.

## Appendix B Complexity Notes

Let NN be the number of nodes, LL the number of GNN layers, and TT the sequence length. The cost of the encoder is approximately:

|  |  |  |
| --- | --- | --- |
|  | 𝒪​(T⋅L⋅|E|),\mathcal{O}(T\cdot L\cdot|E|), |  |

where |E||E| is the aggregated number of edges across layers.

Temporal encoder cost depends on the architecture:

|  |  |  |
| --- | --- | --- |
|  | 𝒪​(T2)​ for Transformer,𝒪​(T)​ for LSTM/GRU.\mathcal{O}(T^{2})\text{ for Transformer},\quad\mathcal{O}(T)\text{ for LSTM/GRU}. |  |

## Appendix C Additional Details for Reproducibility

In addition to the main text, we highlight the following implementation details that support reproducibility:

* •

  Rolling window selection and label construction are implemented using simple, deterministic procedures.
* •

  Hyperparameters are selected using a validation set and are fixed before testing on each crisis period.
* •

  Data splits are aligned with calendar dates to avoid overlapping training and evaluation windows.

## Appendix D Detailed Error Analysis

### D.1 Confusion Matrices and Error Statistics

Table [3](https://arxiv.org/html/2512.17185v1#A4.T3 "Table 3 ‣ D.1 Confusion Matrices and Error Statistics ‣ Appendix D Detailed Error Analysis ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") reports detailed counts of true positives (TP), false positives (FP), true negatives (TN), and false negatives (FN), together with false positive rate (FPR) and false negative rate (FNR) for the Random Forest baseline during the Dot-com and GFC periods.

Table 3: Detailed error analysis for the Random Forest baseline across crisis periods.

| Crisis | TP | FP | TN | FN | FPR | FNR |
| --- | --- | --- | --- | --- | --- | --- |
| Dot-com | 164 | 63 | 65 | 21 | 0.492 | 0.114 |
| GFC | 229 | 23 | 28 | 33 | 0.451 | 0.126 |

Figure [12](https://arxiv.org/html/2512.17185v1#A4.F12 "Figure 12 ‣ D.1 Confusion Matrices and Error Statistics ‣ Appendix D Detailed Error Analysis ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") visualizes the confusion matrices for selected crisis periods.

![Refer to caption](figures/confusion_matrices.png)


Figure 12: Confusion matrices for baseline models across crisis periods. Darker cells correspond to higher counts.

### D.2 False Positive Rate Analysis for GNN Models

Table [4](https://arxiv.org/html/2512.17185v1#A4.T4 "Table 4 ‣ D.2 False Positive Rate Analysis for GNN Models ‣ Appendix D Detailed Error Analysis ‣ Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Prediction") reports the false positive rates (FPR) for the snapshot and temporal GNNs across all crisis periods.

Table 4: False Positive Rates (FPR) for GNN models across crisis periods.

| Crisis | Model | TP | FP | TN | FN | FPR |
| --- | --- | --- | --- | --- | --- | --- |
| Dot-com | Static GNN | 38 | 24 | 0 | 0 | 1.0000 |
| Dot-com | Temporal GNN | 37 | 24 | 0 | 0 | 1.0000 |
| GFC | Static GNN | 51 | 11 | 0 | 0 | 1.0000 |
| GFC | Temporal GNN | 50 | 11 | 0 | 0 | 1.0000 |
| COVID–19 | Static GNN | 41 | 0 | 0 | 0 | N/A |
| COVID–19 | Temporal GNN | 41 | 0 | 0 | 0 | N/A |

In both the Dot-com and GFC crises, the GNN models achieve perfect recall (1.0) but at the cost of high false positive rates, yielding FPR = 1.0. This occurs because the models assign the positive (crash) label to nearly all samples, reflecting a highly conservative early-warning behavior.

During the COVID–19 period, the GNNs again predict the positive class for all evaluation samples. However, because the evaluation window contains no non-crash days (TN = FP = 0), the FPR is undefined (reported as N/A). This highlights that correlation-only graph representations fail to capture the exogenous, policy-driven, and sentiment-driven nature of the COVID crash.

## Appendix E Why the GNN Fails on the COVID–19 Crisis

The GNN models obtain AUROC = 0.000 during the COVID–19 period, indicating a complete failure to distinguish crash versus non-crash days. This outcome is not simply poor performance but reflects a structural mismatch between the correlation-only graph representation and the dynamics of the COVID–19 shock.

Unlike the Dot-com and GFC crises—both of which involved gradual buildup of correlation structure and sector-level synchronization—the COVID–19 crash was dominated by exogenous shocks, including sudden policy interventions, liquidity disruptions, and global uncertainty spikes. These dynamics do not manifest through rising pairwise correlations prior to the drawdown, which is the only information captured by 𝒢t1\mathcal{G}\_{t}^{1}.

Consequently, the snapshot and simplified temporal GNNs receive no structural signal to anticipate the crash, leading to random or inverted decision boundaries and a formal AUROC of 0.000. This failure highlights the importance of the other SRR layers (𝒢t2\mathcal{G}\_{t}^{2} and 𝒢t3\mathcal{G}\_{t}^{3}), which are explicitly designed to capture sectoral exposure patterns and sentiment-driven cascades—two factors that played central roles in the COVID–19 market collapse.

### E.1 Implications for Multi-Layer Graph Design

The COVID–19 failure motivates the full multi-layer SRR architecture:

* •

  The sector/factor layer (𝒢t2\mathcal{G}\_{t}^{2}) can capture structural exposure shifts that occur independently of return correlations.
* •

  The sentiment layer (𝒢t3\mathcal{G}\_{t}^{3}) can detect rapid behavioral changes reflected in social media, news sentiment, and risk perception indicators.
* •

  Multi-layer fusion allows the model to detect crises driven by any combination of structural, behavioral, or exogenous factors.

These extensions are critical for building early-warning systems that generalize across different types of market stress.

## Appendix F Extended Qualitative Analysis

### F.1 Signal Stability and Threshold Considerations

Beyond aggregate metrics such as AUROC or lead-time, the temporal evolution of warning scores offers important qualitative insight. During the Dot-com and GFC periods, model scores tend to rise gradually as correlations intensify and volatility clusters propagate through the market. This behavior is consistent with the hypothesis that structural fragility accumulates before major dislocations, even when price movements are still relatively muted.

In contrast, the COVID–19 period exhibits sharp and irregular score spikes with limited persistence. This pattern reflects the exogenous and policy-driven nature of the shock: systemic stress emerges almost instantaneously, leaving little room for gradual buildup. The warning timeline therefore serves as a diagnostic tool for distinguishing between structurally-driven and event-driven crises, highlighting the conditions under which correlation-only GNNs are effective and when they fail.

### F.2 Cross-Crisis Signal Characteristics

In addition to distinguishing structurally-driven versus event-driven crises, the warning timeline also reveals differences in signal stability. During Dot-com and GFC, model scores exhibit relatively smooth transitions, suggesting that correlation-based representations capture gradual buildup patterns consistently across instruments. In contrast, the COVID–19 window displays high-frequency volatility in warning scores, indicating low structural signal-to-noise ratio and reduced threshold stability.

Such instabilities underscore the difficulty of designing fixed alert thresholds and further motivate multi-layer extensions that can incorporate sentiment or macro shocks when correlation structure alone is insufficient.

### F.3 Interpretable Early-Warning Signals

Finally, the temporal progression of risk scores offers a complementary perspective to aggregate metrics: while AUROC summarizes discrimination at a single threshold, score trajectories illuminate how model confidence accumulates or dissipates over time, providing an interpretable early-warning signal for practitioners. This temporal view enables risk managers to track not just whether a warning is issued, but how the underlying risk assessment evolves leading up to stress events.

## Appendix G Interpretability and Attribution Analysis

### G.1 Feature Attribution Across Crisis Regimes

For GNN models, we use attention-based mechanisms or gradient sensitivity analysis for interpretability. The snapshot GNN reveals which nodes and connections dominate during stress periods. Nodes corresponding to highly liquid sector ETFs receive elevated attention weights, suggesting the model focuses on broad market structure rather than idiosyncratic volatility.

From a systemic-risk perspective, interpretability serves two purposes. First, practitioners can identify which market components contribute most strongly to model warnings, providing transparency for risk-governance workflows. Second, it helps distinguish structurally meaningful signals from spurious short-term noise. As SRR incorporates sentiment and multi-layer dependencies, attention patterns may reveal cross-layer contagion pathways, improving diagnostic power of early-warning tools.

### G.2 Cross-Layer Attribution Patterns

Interpretability patterns differ across crisis regimes. During Dot-com and GFC, feature and attention attributions emphasize broad structural factors: average correlation, volatility clustering, and sector co-movement. These align with gradual systemic buildup. In contrast, attribution patterns in the COVID–19 period appear diffuse and inconsistent, reflecting the absence of structural precursors.

This contrast highlights the value of interpretability not only for understanding model behavior when the models succeed but also for diagnosing the structural blind spots of correlation-only GNNs. As additional graph layers are incorporated into SRR, attribution tools can reveal cross-layer contagion pathways and help identify whether fragility is driven by structural, behavioral, or macroeconomic components.

### G.3 Future Directions for Explainability

We leave a full quantitative study of temporal attention patterns and multi-layer graph attributions to future work, once the complete SRR model with sequence modelling has been trained across all crisis windows. Key areas for investigation include:

* •

  Temporal attention weights to identify critical transition points
* •

  Cross-layer importance analysis to determine which graph layers dominate in different crisis types
* •

  Node-level attribution to identify systemically important institutions
* •

  Edge-level analysis to track contagion pathways