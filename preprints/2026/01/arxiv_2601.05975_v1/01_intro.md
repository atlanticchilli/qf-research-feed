---
authors:
- Kieran Wood
- Stephen J. Roberts
- Stefan Zohren
doc_id: arxiv:2601.05975v1
family_id: arxiv:2601.05975
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management'
url_abs: http://arxiv.org/abs/2601.05975v1
url_html: https://arxiv.org/html/2601.05975v1
venue: arXiv q-fin
version: 1
year: 2026
---


Kieran Wood
  
Oxford-Man Institute &
  
Machine Learning Research Group
  
University of Oxford
  
kieran.wood@eng.ox.ac.uk
  
  
Stephen J. Roberts
  
Machine Learning Research Group
  
University of Oxford
  
stephen.roberts@eng.ox.ac.uk
  
&Stefan Zohren
  
Machine Learning Research Group
  
University of Oxford
  
stefan.zohren@eng.ox.ac.uk

###### Abstract

We propose DeePM (Deep Portfolio Manager), a structured deep-learning macro portfolio manager trained end-to-end to maximize a robust, risk-adjusted utility. DeePM addresses three fundamental challenges in financial learning: (1) it resolves the asynchronous “ragged filtration” problem via a *Directed Delay* (*Causal Sieve*) mechanism that prioritizes causal impulse-response learning over information freshness; (2) it combats low signal-to-noise ratios via a *Macroeconomic Graph Prior*, regularizing cross-asset dependence according to economic first principles; and (3) it optimizes a *distributionally robust objective* where a smooth worst-window penalty serves as a differentiable proxy for Entropic Value-at-Risk (EVaR) – a *window-robust* utility encouraging strong performance in the most adverse historical subperiods.
In large-scale backtests from 2010–2025 on 50 diversified futures with highly realistic transaction costs, DeePM attains net risk-adjusted returns that are roughly twice those of classical trend-following strategies and passive benchmarks, solely using daily closing prices. Furthermore, DeePM improves upon the state-of-the-art Momentum Transformer architecture by roughly fifty percent. The model demonstrates structural resilience across the 2010s “CTA (Commodity Trading Advisor) Winter” and the post-2020 volatility regime shift, maintaining consistent performance through the pandemic, inflation shocks, and the subsequent higher-for-longer environment. Ablation studies confirm that strictly lagged cross-sectional attention, graph prior, principled treatment of transaction costs, and robust minimax optimization are the primary drivers of this generalization capability.

*Keywords* Systematic Macro ⋅\cdot
Portfolio Management ⋅\cdot
Deep Learning ⋅\cdot
Attention ⋅\cdot
Graph Neural Networks ⋅\cdot
Transaction Costs ⋅\cdot
Robust Optimization ⋅\cdot
Risk Measures

## 1 Introduction

The central goal of systematic portfolio management is to construct asset allocations that generalize out-of-sample under heavy-tailed returns, regime shifts, and significant trading frictions. While classical mean–variance optimization (Markowitz, [1952](https://arxiv.org/html/2601.05975v1#bib.bib23 "Portfolio selection")) provides a foundational framework, its practical deployment is plagued by “error maximization” (Michaud, [1989](https://arxiv.org/html/2601.05975v1#bib.bib66 "The markowitz optimization enigma: is “optimized” optimal?")), where small estimation errors in covariance matrices lead to unstable, turnover-intensive portfolios. Consequently, modern approaches have increasingly pivoted toward machine learning pipelines. However, most existing methods adopt a disjoint two-stage approach – forecasting returns first, then performing a portfolio construction step – which misaligns the training loss (Mean Squared Error) with the investor’s ultimate utility (Net Risk-Adjusted Return) (Gu et al., [2020](https://arxiv.org/html/2601.05975v1#bib.bib82 "Empirical asset pricing via machine learning"); Elmachtoub and Grigas, [2022](https://arxiv.org/html/2601.05975v1#bib.bib27 "Smart “predict, then optimize”")).

We propose DeePM, a *Structured*, *Risk-Robust* Deep-learning Portfolio Manager that learns a trading policy end-to-end. Unlike “black box” approaches that treat assets as anonymous time series, DeePM injects specific domain structures – macroeconomic graphs, realizability constraints, and robust risk measures – directly into the architecture. We train DeePM with a *window-robust* objective that emphasizes the hardest historical subperiods: a differentiable soft-min aggregation of rolling-window Sharpe ratios (defined in Sec. [5](https://arxiv.org/html/2601.05975v1#S5 "5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")).

![Refer to caption](x1.png)


Figure 1: The DeePM pipeline. (1) Temporal: Per-asset history is processed via a hybrid backbone. (2) Cross-Sectional: Assets attend to the global state using a causal Directed Delay. (3) Structural/Topological: Latent embeddings are refined via a Macro-Graph GNN. (4) Objective: The network minimizes a robust loss combining pooled Net Sharpe and a worst-window SoftMin penalty.

### 1.1 Decision Problem and Implementation Constraints

Modern systematic macro trading requires learning sequential portfolio policies from noisy, non-stationary markets while respecting strict realizability constraints, such as asynchronous global closes and path-dependent transaction costs. At each decision time tt, the agent maps a high-dimensional information set ℱt\mathcal{F}\_{t} to a vector of portfolio trading signals or weights pt∈ℝNp\_{t}\in\mathbb{R}^{N}. Unlike stylized frictionless settings, practical deployment faces three binding constraints that define the learning challenge:

1. (i)

   Asynchronous Information (Ragged Filtration):
   global macro universes are plagued by *asynchronous market closes* (e.g., Tokyo vs. New York). Naive application of standard attention mechanisms allows models to exploit spurious correlations between “stale” and “fresh” data, leading to look-ahead bias that vanishes in production (Lo and MacKinlay, [1990](https://arxiv.org/html/2601.05975v1#bib.bib30 "An econometric analysis of nonsynchronous trading")). Concretely, under asynchronous global closes, some assets’ same-day information is not available at the portfolio decision time, even though other markets have already closed. If a cross-asset module mixes *same-day* representations across all assets, it can inadvertently condition on information that would only be known later in the day for some markets, creating a subtle look-ahead that disappears in live trading. Our policy must ensure that any cross-asset features used at time tt are measurable with respect to the common information set available across *all* assets at decision time. Furthermore, learning spurious correlations instead of true causal links can lead to backtest overfit (Bailey et al., [2016](https://arxiv.org/html/2601.05975v1#bib.bib85 "The probability of backtest overfitting")).
2. (ii)

   Path-Dependent Frictions: Transaction costs are not merely a post-hoc deduction but a state-dependent penalty on turnover (|wt−wt−1||w\_{t}-w\_{t-1}|). To be viable, the policy must learn to internalize execution efficiency, filtering out high-turnover signals that do not survive costs.
3. (iii)

   Regime Fragility: objective functions based only on pooled averages, such as Sharpe-like criteria (Sharpe, [1966](https://arxiv.org/html/2601.05975v1#bib.bib53 "Mutual fund performance")), can yield seemingly strong performance while concentrating losses into a small number of adverse windows. Risk-measure theory motivates that maximizing average performance is insufficient and we should complement it with tail-sensitive criteria (Rockafellar and Uryasev, [2000](https://arxiv.org/html/2601.05975v1#bib.bib13 "Optimization of conditional value-at-risk"); Ahmadi-Javid, [2012](https://arxiv.org/html/2601.05975v1#bib.bib34 "Entropic value-at-risk: a new coherent risk measure")); we require the objective to explicitly penalize the “worst-case” windows (minimax), prioritizing survival over average-case maximization.

### 1.2 Our Approach: Structured Deep Portfolio Management

DeePM addresses these challenges via a hierarchical architecture mirroring the workflow of a discretionary macro trader. It processes data in three stages:

1. 1.

   Temporal Encoding (Hybrid VSN-LSTM-Attention): Inspired by the Momentum Transformer (Wood et al., [2023](https://arxiv.org/html/2601.05975v1#bib.bib75 "Trading with the momentum transformer: an intelligent and interpretable architecture")), we employ a specialized per-asset encoder. A Vectorized Variable Selection Network (V-VSN) first filters high-dimensional noisy features. This is followed by an LSTM (Long Short-Term Memory) (Hochreiter and Schmidhuber, [1997](https://arxiv.org/html/2601.05975v1#bib.bib101 "Long short-term memory")) backbone to model local path-dependence and denoise volatility, and a Temporal Self-Attention mechanism to capture long-range dependencies and global regime shifts.
2. 2.

   Cross-Sectional Interaction (The Causal Sieve): To resolve the asynchrony problem, we employ a Directed Delay protocol (t−1t-1) for cross-sectional attention. This transforms the attention mechanism into a differentiable “Causal Sieve,” filtering out confounding intraday co-movements to isolate predictive impulse-response signals (Transfer Entropy). As a reference point, we also explore “cascading” filtration which maximises information freshness.
3. 3.

   Structural Regularization (Macro Graph): A Graph Neural Network (GNN) projects latent representations onto a fixed Macroeconomic Prior Graph (e.g., linking Rates to Foreign Exchange (FX) via carry, or Energy to Inflation). This acts as a spectral low-pass filter, forcing the learned covariance to respect economic topology, which stabilizes performance in low-data regimes.

The entire policy is optimized against a Robust Net Sharpe objective. We introduce a SoftMin penalty on windowed performance, which we show is mathematically equivalent to minimizing the dual form of *Entropic Value-at-Risk (EVaR)* (Ahmadi-Javid, [2012](https://arxiv.org/html/2601.05975v1#bib.bib34 "Entropic value-at-risk: a new coherent risk measure")), effectively training the model against an adversarial reweighting of history ( App.[D.2](https://arxiv.org/html/2601.05975v1#A4.SS2 "D.2 Connection to KL-ball DRO and EVaR ‣ Appendix D Analysis of the Robust Objective ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")).

The proposed framework offers a unified end-to-end toolkit for practitioners, integrating three distinct inductive biases: *temporal* (learning path-dependent regimes), *cross-sectional* (isolating causal impulse-responses), and *topological* (regularizing via economic structure).

##### Contributions.

We make the following contributions:

1. 1.

   Decision-focused, cost-aware end-to-end learning.
   We train portfolio policies directly against realized risk-adjusted net returns, aligning the gradient descent landscape with the investor’s utility. This yields net risk-adjusted performance that is approximately double that of two-stage mean–variance baselines and fifty percent higher than that of the Momentum Transformer. The model further learns to naturally dampen turnover without requiring heuristic constraints.
2. 2.

   The Primacy of Causal Robustness: Through ablation studies, we show that our conservative *Directed Delay* filtration (using strictly lagged cross-sectional data) outperforms the “cascading” filtration that maximizes data freshness. This suggests that in macro trading, identifying robust causal drivers (Transfer Entropy) is more valuable than minimizing information latency.
3. 3.

   Macroeconomic Graph Regularization: We show that injecting a sparse prior of economic linkages prevents overfitting. The inclusion of the Graph GNN reduces Maximum Drawdown by 21% relative to a purely data-driven attention model, confirming the value of domain knowledge as an inductive bias.
4. 4.

   Differentiable EVaR Optimization: We bridge the gap between deep learning and coherent risk measures by implementing the SoftMin objective. Empirical results show this penalty is the single largest driver of stability, enabling the strategy to maintain positive performance during the post-2020 volatility transition.
5. 5.

   Optimising Net-of-Cost Returns: We motivate, theoretically (Sec. [5.2](https://arxiv.org/html/2601.05975v1#S5.SS2 "5.2 Ensembling and Implicit Cost Regularization ‣ 5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) and empirically, that ensembling to aggregate the trading signals across the top KK seeds improves performance net-of-cost and, crucially, training with the full transaction costs leads to suboptimal performance. Our experiments demonstrate that training with a transaction cost scaler of γ=0.5\gamma=0.5 improves net performance out of sample by approximately fifty percent, compared to the full cost training.

### 1.3 Paper roadmap

Section [2](https://arxiv.org/html/2601.05975v1#S2 "2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") reviews related work on portfolio learning under frictions, cross-sectional modelling, structured priors, and robust objectives. Section [3](https://arxiv.org/html/2601.05975v1#S3 "3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") formalizes the macroeconomic graph, decision protocol, data construction, and transaction-cost model. Section [4](https://arxiv.org/html/2601.05975v1#S4 "4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") introduces DeePM’s architecture, including filtration-respecting cross-asset conditioning and macro graph regularization. Section [5](https://arxiv.org/html/2601.05975v1#S5 "5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") presents the robust learning objective and optimization procedure. Section [6](https://arxiv.org/html/2601.05975v1#S6 "6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") details the experimental design, reports empirical results, provides ablations and discusses managerial implications. Section [8](https://arxiv.org/html/2601.05975v1#S8 "8 Conclusions and Future Work ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") concludes.

## 2 Related Literature

We situate DeePM at the intersection of deep time-series momentum, end-to-end portfolio learning, and robust optimization. For a comprehensive study of the techniques we employ in this work, please refer to Zhang and Zohren ([2025](https://arxiv.org/html/2601.05975v1#bib.bib98 "Deep learning in quantitative trading")).

### 2.1 Deep Learning for Systematic Trend

Systematic macro strategies typically exploit two primary market phenomena: *Momentum* (or Trend), the tendency for asset prices to persist in their direction over time (Jegadeesh and Titman, [1993](https://arxiv.org/html/2601.05975v1#bib.bib99 "Returns to buying winners and selling losers: implications for stock market efficiency"); Moskowitz et al., [2012](https://arxiv.org/html/2601.05975v1#bib.bib69 "Time series momentum")), and *Mean Reversion*, the tendency for prices to return to a long-term equilibrium after becoming over-extended (De Bondt and Thaler, [1985](https://arxiv.org/html/2601.05975v1#bib.bib100 "Does the stock market overreact?")).

Modern systematic trading has moved beyond linear factors toward deep sequence modelling. Lim et al. ([2019](https://arxiv.org/html/2601.05975v1#bib.bib62 "Enhancing time-series momentum strategies using deep neural networks")) introduced *Deep Momentum Networks (DMNs)*, demonstrating that LSTMs could capture non-linear volatility scaling and trend behaviors that linear *Time-series Momentum* (TSMOM) (Moskowitz et al., [2012](https://arxiv.org/html/2601.05975v1#bib.bib69 "Time series momentum")) misses. Wood et al. ([2023](https://arxiv.org/html/2601.05975v1#bib.bib75 "Trading with the momentum transformer: an intelligent and interpretable architecture")) extended this with the *Momentum Transformer*, applying multi-head attention to learn regime-switching dynamics and global temporal dependencies. Furthermore, recent advancements (Wood et al., [2022](https://arxiv.org/html/2601.05975v1#bib.bib83 "Slow momentum with fast reversion: a trading strategy using deep learning and changepoint detection")) have integrated online changepoint detection in attempt to adapt to rapid regime shifts. Whilst explicit detection is reactive, a regime-robust approach seeks to internalize these vulnerabilities during training.

While effective, these approaches typically treat assets as independent time series or rely on implicit data-driven correlations. DeePM advances this lineage by explicitly modelling the *cross-sectional* structure of the market. We combine the temporal strengths of the DMN/Transformer architectures with a *Macroeconomic Graph Prior*, regularizing the learning process against known economic linkages to prevent overfitting in low-signal regimes.

### 2.2 Machine Learning for Portfolio Construction under Frictions

Classical portfolio construction typically estimates parameters (μt,Σt)(\mu\_{t},\Sigma\_{t}) and then optimizes a static objective. For mean–variance, one solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt⋆∈arg⁡maxw∈𝒲⁡(μ^t⊤​w−η2​w⊤​Σ^t​w),\displaystyle w\_{t}^{\star}\in\arg\max\_{w\in\mathcal{W}}\left(\hat{\mu}\_{t}^{\top}w-\frac{\eta}{2}w^{\top}\hat{\Sigma}\_{t}w\right), |  | (1) |

where η>0\eta>0 represents the investor’s risk aversion coefficient. In the unconstrained case, the solution is wt⋆=η−1​Σ^t−1​μ^tw\_{t}^{\star}=\eta^{-1}\hat{\Sigma}\_{t}^{-1}\hat{\mu}\_{t}. A central difficulty is that the optimization step can *amplify* estimation error: because the solution depends on Σ^t−1\hat{\Sigma}\_{t}^{-1}, small perturbations in (μ^t,Σ^t)(\hat{\mu}\_{t},\hat{\Sigma}\_{t}) can induce large changes in wt⋆w\_{t}^{\star}. Michaud ([1989](https://arxiv.org/html/2601.05975v1#bib.bib66 "The markowitz optimization enigma: is “optimized” optimal?")) characterized this as “error maximization,” motivating shrinkage, resampling, and risk-based allocations.

To overcome this, recent works propose *end-to-end* learning. Zhang et al. ([2020](https://arxiv.org/html/2601.05975v1#bib.bib67 "Deep learning for portfolio optimization")) introduced *Deep Learning for Portfolio Optimization*, demonstrating that optimizing the Sharpe ratio directly outperforms two-stage estimation. However, such architectures often rely on stacking asset features. This approach has three limitations: (i) it ignores the natural *permutation symmetry* of the portfolio (the order of assets is arbitrary); (ii) it lacks *structural priors*, forcing the model to learn economic relationships from scratch; and (iii) it often assumes a synchronized data grid, which introduces look-ahead bias in global portfolios with asynchronous closes. DeePM addresses these by using set-invariant attention mechanisms and enforcing a filtration-respecting lag structure.

### 2.3 Cross-Sectional Modeling with Attention and Representation Learning

Cross-asset dependence can be modeled with data-dependent interactions over the tradable set 𝒰t\mathcal{U}\_{t}. A generic single-head attention layer is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hi,t(1)\displaystyle h^{(1)}\_{i,t} | =∑j∈𝒰tαi​j,t​V​hj,t(0),\displaystyle=\sum\_{j\in\mathcal{U}\_{t}}\alpha\_{ij,t}\,Vh^{(0)}\_{j,t}, |  | (2) |
|  | αi​j,t\displaystyle\alpha\_{ij,t} | =exp⁡(⟨Q​hi,t(0),K​hj,t(0)⟩)∑k∈𝒰texp⁡(⟨Q​hi,t(0),K​hk,t(0)⟩).\displaystyle=\frac{\exp\!\left(\langle Qh^{(0)}\_{i,t},Kh^{(0)}\_{j,t}\rangle\right)}{\sum\_{k\in\mathcal{U}\_{t}}\exp\!\left(\langle Qh^{(0)}\_{i,t},Kh^{(0)}\_{k,t}\rangle\right)}. |  |

where hi,t(0)h^{(0)}\_{i,t} denotes the input embedding for asset ii at time tt, hi,t(1)h^{(1)}\_{i,t} represents the output representation, αi​j,t\alpha\_{ij,t} is the attention weight quantifying the influence of asset jj on ii, Q,K,VQ,K,V are the learnable projection matrices, and ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle signifies the inner product similarity score. To capture heterogeneous market signals across different feature subspaces, this mechanism is expanded to Multi-Head Attention (MHA) by calculating multiple independent attention heads in parallel and concatenating their results into a single enriched representation.

In portfolio problems the cross-section is naturally a *set*: the ordering of assets is arbitrary, and the traded universe can change with missingness, contract rolls, or data availability. A desirable inductive bias is therefore *permutation equivariance*: if we permute the asset order, the output representations (and hence positions) permute in the same way.
Formally, let Π\Pi be a permutation matrix acting on the asset dimension of the stacked representation Ht=[h1,t(0),…,hN,t(0)]⊤H\_{t}=[h^{(0)}\_{1,t},\dots,h^{(0)}\_{N,t}]^{\top}. Set-based layers satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | Layer​(Π​Ht)=Π​Layer​(Ht),\displaystyle\mathrm{Layer}(\Pi H\_{t})=\Pi\,\mathrm{Layer}(H\_{t}), |  | (3) |

which is a standard requirement in set representation learning (Zaheer et al., [2017](https://arxiv.org/html/2601.05975v1#bib.bib46 "Deep sets"); Lee et al., [2019](https://arxiv.org/html/2601.05975v1#bib.bib65 "Set transformer: a framework for attention-based permutation-invariant neural networks")). Attention of the form ([2](https://arxiv.org/html/2601.05975v1#S2.E2 "Equation 2 ‣ 2.3 Cross-Sectional Modeling with Attention and Representation Learning ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) is permutation equivariant when applied across the asset axis, making it well suited for variable-size universes and existence masking.

Purely permutation-equivariant layers are *anonymous* across elements; in markets, however, assets have persistent identities (e.g., duration-sensitive rates vs. energy futures). DeePM incorporates this by injecting a categorical ticker embedding eie\_{i} to the per-asset state before cross-sectional interaction. This preserves equivariance in ([3](https://arxiv.org/html/2601.05975v1#S2.E3 "Equation 3 ‣ 2.3 Cross-Sectional Modeling with Attention and Representation Learning ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) (the permutation acts jointly on (h~i,t(0))i∈𝒰t(\tilde{h}^{(0)}\_{i,t})\_{i\in\mathcal{U}\_{t}}), while allowing the model to condition on asset-specific effects and long-run heterogeneity.

Permutation-equivariant attention is also a natural mechanism for transferring structure across regimes or assets by matching patterns in a context set. For example, Wood et al. ([2024](https://arxiv.org/html/2601.05975v1#bib.bib63 "Few-shot learning patterns in financial time series for trend-following strategies")) use cross-attention to adapt trend-following decisions to new regimes from a small number of examples, highlighting the usefulness of attention-based set reasoning in financial time series. Instead of conditioning on a basket of historical sequences for few-shot transfer, we use a cross-sectional context set of contemporaneous assets (or their lag-aligned histories) to transfer information across the universe.

### 2.4 Graph Priors and Economic Structure

While data-driven attention can capture arbitrary correlations, financial covariance matrices are notoriously noisy and unstable. Graph Neural Networks (GNNs) offer a mechanism to inject domain knowledge as a structural prior. By defining a sparse adjacency matrix AA based on economic fundamentals – such as supply chains, sector classifications, or macro-correlation regimes – we impose a relational inductive bias. Critically, In Graph Neural Networks, the graph topology imposes a structural constraint on where information may flow, not what is learned.

The standard Graph Convolutional Network (GCN) (Kipf and Welling, [2017](https://arxiv.org/html/2601.05975v1#bib.bib47 "Semi-supervised classification with graph convolutional networks")) implements a fixed spectral filter:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ht(2)=σ​(A~​Ht(1)​W1),H^{(2)}\_{t}=\sigma\!\left(\tilde{A}\,H^{(1)}\_{t}W\_{1}\right), |  | (4) |

where A~\tilde{A} is the normalized adjacency matrix, and σ​(⋅)\sigma(\cdot) is a non-linear activation function. This operator enforces *isotropic* smoothing – every neighbor affects the node equally (weighted by degree). In finance, however, economic linkages are time-varying; a “Safe Haven" link between Bonds and Gold may be strong in crises but weak in growth regimes.

To address this, Graph Attention Networks (GATs) (Veličković et al., [2018](https://arxiv.org/html/2601.05975v1#bib.bib48 "Graph attention networks")) introduce learnable, anisotropic attention weights αi​j\alpha\_{ij} masked by the graph structure and a message passing layer then updates node ii by aggregating over its graph neighborhood:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hi(2)\displaystyle h\_{i}^{(2)} | =σ​(∑j∈𝒩​(i)αi​j​W​hj(1)),\displaystyle=\sigma\left(\sum\_{j\in\mathcal{N}(i)}\alpha\_{ij}Wh\_{j}^{(1)}\right), |  | (5) |
|  | αi​j,tG\displaystyle\alpha^{G}\_{ij,t} | =exp⁡(⟨QG​hi,t(1),KG​hj,t(1)⟩)∑k∈𝒩​(i)exp⁡(⟨QG​hi,t(1),KG​hk,t(1)⟩),\displaystyle=\frac{\exp\!\left(\langle Q\_{G}h^{(1)}\_{i,t},\,K\_{G}h^{(1)}\_{j,t}\rangle\right)}{\sum\_{k\in\mathcal{N}(i)}\exp\!\left(\langle Q\_{G}h^{(1)}\_{i,t},\,K\_{G}h^{(1)}\_{k,t}\rangle\right)}, |  |

where 𝒩​(i)={j:Ai​j=1}\mathcal{N}(i)=\{j:A\_{ij}=1\} is defined by the (sparse) economic adjacency AA. Unlike fully connected attention (Section [2.3](https://arxiv.org/html/2601.05975v1#S2.SS3 "2.3 Cross-Sectional Modeling with Attention and Representation Learning ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")), GAT restricts attention to economically plausible pairs defined by AA, while unlike GCN, it allows the model to dynamically upweight or downweight these priors based on the current market state. Furthermore, both GCN and GAT layers retain the property of permutation equivariance (under simultaneous permutation of node features and the adjacency matrix), ensuring the model remains consistent with the set-based nature of the portfolio universe discussed in Section [2.3](https://arxiv.org/html/2601.05975v1#S2.SS3 "2.3 Cross-Sectional Modeling with Attention and Representation Learning ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"). DeePM utilizes this architecture to balance structural regularization with regime-dependent flexibility.

### 2.5 Robust Objectives and Risk Measures

Standard portfolio objectives maximize average performance (e.g., pooled Sharpe ratio), which can lead to overfitting on specific regimes or “lucky windows" while ignoring tail risks. To address this, we draw on the literature of coherent risk measures.
Conditional Value-at-Risk (CVaR) (Rockafellar and Uryasev, [2000](https://arxiv.org/html/2601.05975v1#bib.bib13 "Optimization of conditional value-at-risk")) at level α\alpha admits the variational form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CVaRα​(Z)=minη∈ℝ⁡{η+11−α​𝔼​[(Z−η)+]}.\mathrm{CVaR}\_{\alpha}(Z)=\min\_{\eta\in\mathbb{R}}\left\{\eta+\frac{1}{1-\alpha}\mathbb{E}[(Z-\eta)\_{+}]\right\}. |  | (6) |

Entropic Value-at-Risk (EVaR) (Ahmadi-Javid, [2012](https://arxiv.org/html/2601.05975v1#bib.bib34 "Entropic value-at-risk: a new coherent risk measure")) provides a strictly tighter upper bound via exponential tilting:

|  |  |  |  |
| --- | --- | --- | --- |
|  | EVaRα​(Z)=infλ>01λ​(log⁡𝔼​[eλ​Z]−log⁡α).\mathrm{EVaR}\_{\alpha}(Z)=\inf\_{\lambda>0}\frac{1}{\lambda}\left(\log\mathbb{E}[\mathrm{e}^{\lambda Z}]-\log\alpha\right). |  | (7) |

Crucially, these measures link directly to *distributionally robust optimization* (DRO) or minimax frameworks. By convex duality, minimizing EVaR is equivalent to minimizing the expected loss against an *adversarial distribution* QQ chosen from a uncertainty set defined by the Kullback-Leibler (KL) divergence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | EVaRα​(Z)=supQ≪P{𝔼Q​[Z]∣KL​(Q∥P)≤Cα},\mathrm{EVaR}\_{\alpha}(Z)=\sup\_{Q\ll P}\left\{\mathbb{E}\_{Q}[Z]\mid\mathrm{KL}(Q\|P)\leq C\_{\alpha}\right\}, |  | (8) |

where Cα=−log⁡(1−α)C\_{\alpha}=-\log(1-\alpha). DeePM’s training objective employs a SoftMin penalty, defined in Sec. [5.1](https://arxiv.org/html/2601.05975v1#S5.SS1 "5.1 Robust Objective: Pooled Sharpe with SoftMin Penalty ‣ 5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"), over windowed Sharpe111In Sec. [5.1](https://arxiv.org/html/2601.05975v1#S5.SS1 "5.1 Robust Objective: Pooled Sharpe with SoftMin Penalty ‣ 5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"), we also motivate why we use Sharpe ratio ratios. As we detail in App. [D](https://arxiv.org/html/2601.05975v1#A4 "Appendix D Analysis of the Robust Objective ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"), this is mathematically isomorphic to the dual form of EVaR. It effectively trains the policy against an implicit adversary who reweights the training windows (QQ) to emphasize the worst-performing regimes, thereby enforcing robustness against distributional shifts.

![Refer to caption](images/sharpe_emp_vs_adv.png)


Figure 2: Visualizing the Distributionally Robust Objective.
This figure illustrates the mechanics of the SoftMin penalty using a synthetic mixture model (85% Normal regime 𝒩​(1.0,0.92)\mathcal{N}(1.0,0.9^{2}), 15% Crisis regime 𝒩​(−2.0,1.42)\mathcal{N}(-2.0,1.4^{2})).
Panel A demonstrates the implicit distribution shift: while the empirical history PP (grey) has a positive mean (+0.55+0.55), the adversarial reweighting QQ (red) shifts probability mass to the left tail, resulting in a significantly lower robust utility (−4.37-4.37). This effective “hallucination” of a harsher environment forces the optimizer to prioritize survival in worst-case regimes.
Panel B displays the corresponding gradient weight function qb∝exp⁡(−SRb/τ)q\_{b}\propto\exp(-\mathrm{SR}\_{b}/\tau). The exponential decay ensures that “easy” high-Sharpe windows contribute near-zero gradient signal (Complacency), while “hard” negative-Sharpe windows dominate the parameter updates (Panic), effectively implementing a differentiable minimax curriculum.

## 3 Problem Setup and Data

### 3.1 Universe and Decision Protocol

We trade a diversified universe of N=50N=50 liquid futures and FX contracts. Each asset ii is assigned to a macro group g​(i)g(i) (e.g., Equities, Rates, Energy), which informs the structural graph prior (details in Appendix [A.2](https://arxiv.org/html/2601.05975v1#A1.SS2 "A.2 Macro Graph Topology ‣ Appendix A Universe Specifications and Methodology ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")).

Systematic macro portfolios face the challenge of *asynchronous market closes* (e.g., Nikkei closes hours before S&P 500). We evaluate two protocols to define the admissible information set ℱt\mathcal{F}\_{t}: (1) Global One-Day Lag (Primary) which enforces a strict delay, and (2) Cascading Filtration (Ablation) which maximizes information freshness. These are defined mathematically in Sec. [4.3](https://arxiv.org/html/2601.05975v1#S4.SS3 "4.3 Cross-Sectional Interaction: Filtration-Compliant Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
Unless otherwise stated, results utilize the Global One-Day Lag to prioritize structural robustness over latency.

We define the next-period arithmetic return as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri,t+1:=Pi,t+1Pi,t−1.\displaystyle r\_{i,t+1}\;=\;\frac{P\_{i,t+1}}{P\_{i,t}}-1. |  | (9) |

This convention ensures that any cross-asset operation at decision date tt uses only
{xi,t}i∈𝒰\{x\_{i,t}\}\_{i\in\mathcal{U}} computed from {Pi,u}u≤t\{P\_{i,u}\}\_{u\leq t}.

### 3.2 Portfolio Returns and Frictions

The policy network outputs raw actions a~i,t∈ℝ\tilde{a}\_{i,t}\in\mathbb{R} which are squashed to
bounded risk weights

|  |  |  |  |
| --- | --- | --- | --- |
|  | pi,t:=tanh⁡(a~i,t)∈(−1,1).\displaystyle p\_{i,t}=\tanh(\tilde{a}\_{i,t})\in(-1,1). |  | (10) |

Let σ^i,t>0\hat{\sigma}\_{i,t}>0 be an ex-ante daily volatility estimate (typically a 63-day EWMA). We define the
volatility scaling factor (ε\varepsilon being a small regularizer)

|  |  |  |  |
| --- | --- | --- | --- |
|  | vi,t:=1σ^i,t+ε.\displaystyle v\_{i,t}=\frac{1}{\hat{\sigma}\_{i,t}+\varepsilon}. |  | (11) |

The corresponding (vol-targeted) notional exposure (Moskowitz et al., [2012](https://arxiv.org/html/2601.05975v1#bib.bib69 "Time series momentum"); Harvey et al., [2018](https://arxiv.org/html/2601.05975v1#bib.bib76 "The impact of volatility targeting")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi,t:=vi,t​pi,t.\displaystyle w\_{i,t}=v\_{i,t}\,p\_{i,t}. |  | (12) |

We optimize the policy directly against *Net Portfolio Return* (RnetR^{\text{net}}). We define RnetR^{\text{net}} by deducting linear transaction costs from the gross volatility-scaled performance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt+1net:=1Nt​∑i=1Nmi,t​pi,t​yi,t+1⏟Rt+1gross−γNt​∑i=1Nmi,t​ci​|wi,t−wi,t−1|⏟Transaction CostR^{\mathrm{net}}\_{t+1}:=\underbrace{\frac{1}{N\_{t}}\sum\_{i=1}^{N}m\_{i,t}\,p\_{i,t}\,y\_{i,t+1}}\_{R^{\mathrm{gross}}\_{t+1}}-\underbrace{\frac{\gamma}{N\_{t}}\sum\_{i=1}^{N}m\_{i,t}\,c\_{i}\,\bigl|w\_{i,t}-w\_{i,t-1}\bigr|}\_{\text{Transaction Cost}} |  | (13) |

where yi,t+1y\_{i,t+1} is the vol-scaled asset return, cic\_{i} is the asset-specific cost parameter (derived in App. [A.1](https://arxiv.org/html/2601.05975v1#A1.SS1 "A.1 Data Provenance and Processing ‣ Appendix A Universe Specifications and Methodology ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")), mi,t∈{0,1}m\_{i,t}\in\{0,1\} is an availability mask indicating whether asset ii is tradable/has valid data and γ\gamma is a global scaling factor. We motivate in App. [B](https://arxiv.org/html/2601.05975v1#A2 "Appendix B Turnover Guarantees for Ensembles ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") that an intermediate value γ∈(0,1)\gamma\in(0,1) is theoretically optimal for maximizing out-of-sample net Sharpe under ensembling. This formulation ensures the model explicitly learns to balance signal strength against turnover constraints.

### 3.3 Features and Preprocessing

We construct a compact, stationarized feature vector xi,t∈ℝFx\_{i,t}\in\mathbb{R}^{F} for each asset, designed to capture multi-scale trend dynamics and tail risks. To strictly isolate the contribution of the learned structural priors and attention mechanisms, we restrict the input space to be derived *exclusively* from daily closing prices. While practical systematic macro strategies typically incorporate explicit “Carry” signals (e.g., interest rate differentials, forward points) and fundamental macroeconomic indicators (e.g., Consumer Price Index, Purchasing Managers’ Index releases), we omit these sources in this study. This constraint forces the model to extract latent risk premia and regime shifts solely from endogenous price dynamics.

##### Ex-ante Volatility.

We estimate daily return variance s^i,t2\hat{s}^{2}\_{i,t} via an exponentially weighted moving average (EWMA) with a 63-day span. This serves as the normalization factor for all inputs and notional sizing.

##### 1. Volatility-Normalized Returns.

To capture momentum across horizons (Moskowitz et al., [2012](https://arxiv.org/html/2601.05975v1#bib.bib69 "Time series momentum")), we compute returns over windows h∈{1,21,63,252}h\in\{1,21,63,252\} days (with 252 days representing a full year). Each return is scaled by ex-ante volatility to ensure distribution stability:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ri,t(h):=Pi,t/Pi,t−h−1σ^i,t​h+ε.\mathrm{R}^{(h)}\_{i,t}\;:=\;\frac{P\_{i,t}/P\_{i,t-h}-1}{\hat{\sigma}\_{i,t}\sqrt{h}+\varepsilon}. |  | (14) |

##### 2. MACD Trend Filters.

Following Appel ([1979](https://arxiv.org/html/2601.05975v1#bib.bib78 "The moving average convergence–divergence trading method")), we include Moving Average Convergence Divergence (MACD) signals to capture trend persistence. We compute the difference between fast and slow EWMAs at multiple scales (S,L)∈{(8,24),(16,48),(32,96)}(S,L)\in\{(8,24),(16,48),(32,96)\}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | MACDS,L​(i,t):=EWMS​(Pi)t−EWML​(Pi)tσ^i,t.\mathrm{MACD}\_{S,L}(i,t)\;:=\;\frac{\text{EWM}\_{S}(P\_{i})\_{t}-\text{EWM}\_{L}(P\_{i})\_{t}}{\hat{\sigma}\_{i,t}}. |  | (15) |

The resulting MACD signals are subsequently re-normalized by their own 252-day rolling standard deviation to ensure comparability across assets and time.

##### 3. Mean-Reversion

To detect over-extension and regime fragility (Harvey and Siddique, [2000](https://arxiv.org/html/2601.05975v1#bib.bib80 "Conditional skewness in asset pricing tests"); Bollinger, [2002](https://arxiv.org/html/2601.05975v1#bib.bib79 "Bollinger on bollinger bands")), we include
Price Z-Scores: ZZ-score of log-prices over rolling windows ℓ∈{21,252}\ell\in\{21,252\} to signal mean-reversion potential.

##### 4. Robust Outlier Control.

Financial data is heavy-tailed. To prevent gradient explosions, we apply a robust, no-lookahead clipping filter. For each feature fi,tf\_{i,t}, we compute a rolling median (mtm\_{t}) and Median Absolute Deviation (MADt\text{MAD}\_{t}) over 252 days. We clip values to [mt±5×1.48×MADt][m\_{t}\pm 5\times 1.48\times\mathrm{MAD}\_{t}], ensuring the model trains on the core distribution rather than artifacts. We use MADt\mathrm{MAD}\_{t} (rather than the sample standard deviation) because it is far less sensitive to heavy tails and transient price spikes, scale it by 1.481.48 to obtain a σ\sigma-comparable robust dispersion estimate under a Gaussian reference model, and, in line with the literature (Lim et al., [2019](https://arxiv.org/html/2601.05975v1#bib.bib62 "Enhancing time-series momentum strategies using deep neural networks"); Wood et al., [2023](https://arxiv.org/html/2601.05975v1#bib.bib75 "Trading with the momentum transformer: an intelligent and interpretable architecture")), use a conservative 5×5\times (approximately “5​σ5\sigma”) band so clipping targets only extreme outliers while preserving almost all typical observations.

##### 5. Feature Subsets and Parsimony.

Given the high capacity of the DeePM architecture, supplying highly correlated inputs (e.g., overlapping return windows simultaneously with MACD filters) increases the risk of noise memorization rather than generalization. To mitigate this, we do not use all features simultaneously. Instead, we evaluate two distinct, parsimonious subsets: (1) a *Raw Momentum* variant, consisting of the lagged returns (h∈{1,…,252}h\in\{1,\dots,252\}) and Z-scores; and (2) a *Signal-Based* variant, consisting only of the 1-day return (r1​dr\_{1d}), the MACD trend filters, and Z-scores. This separation forces the model to learn from orthogonal signals and reduces the likelihood of overfitting to redundant feature correlations.

### 3.4 Philosophy of the Macro-Structural Prior

In high-dimensional macro environments, pure data-driven correlation learning often fails due to low signal-to-noise ratios and non-stationarity. To mitigate this, we inject domain knowledge via a fixed *Macroeconomic Graph Prior*. We model the universe as a graph 𝒢=(𝒱,ℰ)\mathcal{G}=(\mathcal{V},\mathcal{E}), constructed deterministically from economic first principles rather than noisy return correlations.
We acknowledge that any hand-specified macro topology entails some subjectivity; accordingly, we treat 𝒢\mathcal{G} as a *structural regularizer* rather than a claim of ground-truth causality. Our design is (i) *deterministic and ex ante*, specified from broad economic transmission channels (not fit to the sample), and (ii) *coarse and interpretable*, relying only on high-level mechanisms for which there is broad agreement in macro/markets practice. The resulting construction is summarized here and specified in full in App. [A.2](https://arxiv.org/html/2601.05975v1#A1.SS2 "A.2 Macro Graph Topology ‣ Appendix A Universe Specifications and Methodology ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").

![Refer to caption](x2.png)


Figure 3: The Macro-Structural Prior Graph used to regularize cross-sectional attention. Edges encode deterministic economic linkages rather than data-driven correlations.

1. 1.

   Sectoral Homophily (Cliques): Assets within the same macro group (e.g., RATES\_US\_TREASURY) are assumed to share a single latent factor. These form fully connected sub-graphs.
2. 2.

   Supply Chain & Substitution: We encode physical dependencies, such as the input-cost relationship between Energy and Agriculture, or the substitution effect between Safe Haven FX and Precious Metals.
3. 3.

   Macro-Finance Transmission: We explicitly link disparate asset classes based on canonical transmission mechanisms. For instance, the “Carry" channel links High-Yield FX to Sovereign Rates, and the “Inflation Triangle" connects Energy, Breakeven-sensitive Rates, and Precious Metals.
4. 4.

   Regional Integration: We capture local monetary and fiscal channels by forming triangular linkages between the primary equity index, sovereign bond, and currency of the same region, enforcing consistency across local asset classes.

This graph serves as a structural scaffold applied *after* the cross-sectional attention mechanism: we require the attention-enriched representations to be smooth with respect to this economic topology, effectively regularizing the high-capacity temporal encoders.

### 3.5 Philosophy of the Transaction Cost Model

To train a policy that is deployable in practice, the training signal must deduct realistic frictions. A naive constant cost model (e.g., 1bp flat) fails to capture the heterogeneity of global liquidity. Instead, we implement a *Structural Minimum Cost Model* that synthesizes the “Tick Size Constraint" theory (Harris, [2003](https://arxiv.org/html/2601.05975v1#bib.bib91 "Trading and exchanges: market microstructure for practitioners")) with market impact models (Kyle, [1985](https://arxiv.org/html/2601.05975v1#bib.bib96 "Continuous auctions and insider trading")).

We define the transaction cost cic\_{i} for asset ii as a function of its microstructure regime:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ci≈Cstruct,i×λic\_{i}\approx C\_{\text{struct},i}\times\lambda\_{i} |  | (16) |

* •

  The Structural Floor (CstructC\_{\text{struct}}): In electronic order books, the quoted spread is lower-bounded by the exchange’s Minimum Price Variation (tick size). For liquid instruments, the cost is dominated by this quantization noise.
* •

  The Liquidity Scalar (λi\lambda\_{i}): We apply a multiplier λi≥1.0\lambda\_{i}\geq 1.0 to account for institutional size impact. For deep markets (e.g., S&P 500), λ≈1\lambda\approx 1. For “gappy" markets (where there are holes in the order book e.g., Feeder Cattle) or “Roach Motel" liquidity regimes (easy to enter, hard to exit, e.g., Palladium), λ\lambda scales significantly higher to reflect the effective spread paid to sweep the book.

The exact derivation of these bands and the asset-specific overrides are detailed in App. [A.3](https://arxiv.org/html/2601.05975v1#A1.SS3 "A.3 Transaction Cost Methodology ‣ Appendix A Universe Specifications and Methodology ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").

## 4 Method: DeePM Architecture

The architecture we used is “structured”, which we use to denote two inductive biases.
First, the cross-sectional module is *permutation equivariant* over assets: relabeling assets only relabels the corresponding outputs,
which is essential when each asset has a categorical identity embedding but the model should not depend on arbitrary ordering.
Second, we incorporate a fixed macro adjacency graph that regularizes cross-asset interactions toward economically plausible transmission channels.
Together these biases reduce overfitting and improve robustness under changing cross-asset correlation regimes.

### 4.1 Network Inputs and Context

At each decision time tt, the model processes a rolling lookback window of length LL. While the financial return targets and execution logic are defined in Section [3](https://arxiv.org/html/2601.05975v1#S3 "3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"), the neural network operates on the following specific tensor representations.

For each asset i∈𝒰i\in\mathcal{U}, we construct a feature vector xi,t∈ℝFx\_{i,t}\in\mathbb{R}^{F} (as defined in Section [3.3](https://arxiv.org/html/2601.05975v1#S3.SS3 "3.3 Features and Preprocessing ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")). Let mi,t∈{0,1}m\_{i,t}\in\{0,1\} be the existence mask indicating if asset ii is tradable at time tt. The input to the temporal backbone is the window tensor:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt:={xi,t−ℓ}i=1,…,N;ℓ=1,…,L∈ℝN×L×F.X\_{t}:=\{x\_{i,t-\ell}\}\_{i=1,\dots,N;\,\ell=1,\dots,L}\in\mathbb{R}^{N\times L\times F}. |  | (17) |

To allow the shared network weights to learn *asset-specific dynamics* (e.g., distinguishing between mean-reverting FX pairs and trending commodities), we initialize a learnable *Static Asset Embedding* ei∈ℝde\_{i}\in\mathbb{R}^{d} for each ticker ii.
This embedding serves as a persistent identifier that breaks parameter anonymity while maintaining *permutation equivariance*—since the embedding eie\_{i} is permuted alongside the asset’s dynamic features xi,tx\_{i,t}, the model output is independent of the arbitrary tensor ordering.

The embedding is concatenated with the static transaction cost parameter cic\_{i} and projected to form a unified *Static Context Vector* sis\_{i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | si=Linear​([ei;ci])∈ℝd.s\_{i}=\text{Linear}([e\_{i};c\_{i}])\in\mathbb{R}^{d}. |  | (18) |

As detailed below, this context sis\_{i} is injected at two specific locations: (1) to modulate feature selection in the V-VSN, and (2) to initialize the hidden state of the LSTM.

### 4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention

Motivated by state-of-the-art results achieved by Wood et al. ([2023](https://arxiv.org/html/2601.05975v1#bib.bib75 "Trading with the momentum transformer: an intelligent and interpretable architecture")) in the univariate setting for systematic macro, we process each asset’s time series independently to extract a latent regime embedding hi,ttemph\_{i,t}^{\text{temp}}. We process using *Channel-independence*, which is a deliberate regularization: by sharing the same temporal encoder weights across assets, the model learns a reusable dynamical feature extractor while avoiding direct cross-channel mixing at the raw-input level, which can encourage fitting to idiosyncratic cross-asset noise (Nie et al., [2023](https://arxiv.org/html/2601.05975v1#bib.bib90 "A time series is worth 64 words: long-term forecasting with transformers")). Cross-asset dependence is instead injected explicitly downstream via the Macro-Graph block (Sec. [4.4](https://arxiv.org/html/2601.05975v1#S4.SS4 "4.4 Structural Regularization: Macro Graph Prior ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")). Our backbone integrates three distinct inductive biases: sparsity (VSN), local recurrence (LSTM), and global context (Attention).

##### 1. Vectorized Variable Selection Network (V-VSN).

*Motivation:* Financial data is high-dimensional and noisy; regime changes often render specific features (e.g., momentum) irrelevant while others (e.g., mean reversion) become dominant.
To address this, we employ a *Vectorized VSN* to dynamically weight input features. Unlike sequential Gated Residual Networks (Lim et al., [2021](https://arxiv.org/html/2601.05975v1#bib.bib8 "Temporal fusion transformers for interpretable multi-horizon time series forecasting")), we implement this efficiently using grouped *1D Convolutions* (Conv1D). Here, a Conv1D with kernel size 1 acts as a time-shared linear projection applied independently to each feature channel across the sequence, enabling efficient parallelization.

We generate feature-wise gating weights via *Feature-wise Linear Modulation (FiLM)* (Perez et al., [2018](https://arxiv.org/html/2601.05975v1#bib.bib12 "FiLM: visual reasoning with a general conditioning layer")). Conditioned on the static context sis\_{i}, FiLM applies a channel-wise affine transformation (scale γ\gamma and shift β\beta) to the inputs.
For input xtx\_{t}, we compute sparse weights wt∈[0,1]Fw\_{t}\in[0,1]^{F} and transformed features vtv\_{t}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | FiLM​(xt,si)\displaystyle\text{FiLM}(x\_{t},s\_{i}) | =γ​(si)⊙xt+β​(si),\displaystyle=\gamma(s\_{i})\odot x\_{t}+\beta(s\_{i}), |  | (19) |
|  | wt\displaystyle w\_{t} | =Softmax​(Linear​(FiLM​(xt,si))),\displaystyle=\text{Softmax}(\text{Linear}(\text{FiLM}(x\_{t},s\_{i}))), |  |
|  | vt\displaystyle v\_{t} | =∑f=1Fwt,f⋅Conv1D​(xt,f),\displaystyle=\sum\_{f=1}^{F}w\_{t,f}\cdot\text{Conv1D}(x\_{t,f}), |  |

where ⊙\odot denotes element-wise multiplication. This allows the model to learn, for example, that “Trend features are less relevant for Asset A (high mean-reversion) than Asset B,” and suppress them accordingly.

##### 2. Local Recurrence (LSTM).

*Motivation:* Financial time series exhibit strong path dependence and heteroskedastic noise. Standard Transformers often struggle to filter high-frequency noise without very large datasets.
We pass the weighted feature stream vtv\_{t} through an LSTM layer. This provides a strong inductive bias for sequential processing and acts as a non-linear low-pass filter, denoising local volatility spikes that can confuse downstream attention mechanisms.

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi,0,ci,0=tanh⁡(W0​si),hi,tlstm=LSTM​(vi,t,hi,t−1lstm).h\_{i,0},c\_{i,0}=\tanh(W\_{\text{0}}s\_{i}),\;\;\;h\_{i,t}^{\text{lstm}}=\text{LSTM}(v\_{i,t},h\_{i,t-1}^{\text{lstm}}). |  | (20) |

Note that the initial state (hi,0,ci,0)(h\_{i,0},c\_{i,0}) is a projection of the asset embedding sis\_{i}, priming the recurrence with the asset’s specific identity.

##### 3. Temporal Attention with Adapter.

*Motivation:* Regime shifts (e.g., inflation shocks) may depend on events occurring months in the past, beyond the effective memory of an LSTM.
To capture these long-range dependencies, we refine the LSTM state using a causal *Temporal Transformer* (Lim et al., [2021](https://arxiv.org/html/2601.05975v1#bib.bib8 "Temporal fusion transformers for interpretable multi-horizon time series forecasting")) block (Temporal MHA).

*The ResSwiGLU Adapter:* Before entering the attention mechanism, the LSTM output is processed by a specialized adapter module 𝒜​(⋅)\mathcal{A}(\cdot). The adapter is necessary to project the LSTM’s robust local features into a richer, non-linear representation that is optimized for the subsequent attention mechanism to capture complex global dependencies. We employ a *Post-Norm* configuration with SwiGLU activation (Shazeer, [2020](https://arxiv.org/html/2601.05975v1#bib.bib15 "GLU variants improve transformer")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜​(x)=LN​(x+δ​(W2​(W1​x⊙SiLU​(V​x)))),\mathcal{A}(x)=\text{LN}\left(x+\delta\bigl(W\_{2}(W\_{1}x\odot\text{SiLU}(Vx))\bigr)\right), |  | (21) |

where W1,W2,VW\_{1},W\_{2},V are learnable weight matrices, δ\delta denotes *dropout* (Srivastava et al., [2014](https://arxiv.org/html/2601.05975v1#bib.bib68 "Dropout: a simple way to prevent neural networks from overfitting")), and LN​(⋅)\text{LN}(\cdot) is Layer Normalization. Layer-Norm stabilizes training by re-centering and scaling the hidden states to prevent gradient explosion, while Dropout randomly zeroes out neurons during training to force the model to learn robust, redundant features rather than overfitting to financial noise. The residual connection facilitates gradient flow and ensures the model can default to the robust local features extracted by the LSTM if complex non-linear adaptation is unnecessary (He et al., [2016](https://arxiv.org/html/2601.05975v1#bib.bib97 "Deep residual learning for image recognition")). The term W1​x⊙SiLU​(V​x)W\_{1}x\odot\text{SiLU}(Vx) represents SwiGLU activation, a non-linear, gated linear unit that improves gradient flow depthwise (Shazeer, [2020](https://arxiv.org/html/2601.05975v1#bib.bib15 "GLU variants improve transformer")), where SiLU:z↦z1+e−z\text{SiLU}\colon z\mapsto\frac{z}{1+\mathrm{e}^{-z}}. Unlike Pre-Norm variants (Xiong et al., [2020](https://arxiv.org/html/2601.05975v1#bib.bib18 "On layer normalization in the transformer architecture")), common in modern architectures, the normalization is applied *after* the residual connection, which we empirically found stabilizes the high-variance financial features.

*Note on Architecture Reuse:* This adapter 𝒜​(⋅)\mathcal{A}(\cdot) serves as the standard non-linear building block throughout DeePM. It is reused as the Feed-Forward Network (FFN) in both the Cross-Sectional Attention layer (Section [4.3](https://arxiv.org/html/2601.05975v1#S4.SS3 "4.3 Cross-Sectional Interaction: Filtration-Compliant Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) and the Graph Neural Network layer (Section [4.4](https://arxiv.org/html/2601.05975v1#S4.SS4 "4.4 Structural Regularization: Macro Graph Prior ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")), ensuring consistent gradient dynamics across temporal and spatial dimensions.

While the LSTM effectively filters high-frequency noise and captures local path dependence, its recursive nature suffers from fading memory over long horizons. To resolve this, the final temporal embedding is produced by applying a causal *Temporal Attention* mechanism. This allows the model to bypass the recursive bottleneck and directly attend to relevant historical regimes (e.g., a past inflation shock similar to the current state) regardless of their temporal distance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi,ttemp=TempMHA​(Q=zi,t,K=zi,≤t,V=zi,≤t),h\_{i,t}^{\text{temp}}=\text{TempMHA}(Q=z\_{i,t},K=z\_{i,\leq t},V=z\_{i,\leq t}), |  | (22) |

where zi,t=𝒜​(hi,tlstm)z\_{i,t}=\mathcal{A}(h\_{i,t}^{\text{lstm}}) and TempMHA​(⋅,⋅,⋅)\text{TempMHA}(\cdot,\cdot,\cdot) is masked to mitigate look-ahead bias. The output is subsequently processed by the adapter 𝒜​(⋅)\mathcal{A}(\cdot), yielding Ht=𝒜​(Httemp)H\_{t}=\mathcal{A}(H\_{t}^{\text{temp}}).

### 4.3 Cross-Sectional Interaction: Filtration-Compliant Attention

After temporal encoding, we have a tensor of independent asset embeddings Ht∈ℝN×dH\_{t}\in\mathbb{R}^{N\times d}. To capture cross-asset spillover (e.g., rates driving equities), we apply a *Cross-Sectional Multi-Head Attention (MHA)* layer.

*Post-Norm with ReZero Gating:* We implement this block using a Post-Norm configuration augmented with *ReZero* gating (Bachlechner et al., [2021](https://arxiv.org/html/2601.05975v1#bib.bib94 "ReZero is all you need: fast convergence at large depth")). Standard Transformer connections can suffer from signal degradation in deep networks; ReZero mitigates this by introducing a learnable scalar parameter α\alpha initialized to a small value (e.g., α≈0\alpha\approx 0). This initializes the layer as an identity map, allowing the optimizer to gradually introduce cross-sectional interactions only where they provide predictive gain.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Htattn=LN​(Ht+αcross⋅CrossMHA​(Ht,H~t,H~t)).H\_{t}^{\text{attn}}=\text{LN}\left(H\_{t}+\alpha\_{\text{cross}}\cdot\text{CrossMHA}\left(H\_{t},\tilde{H}\_{t},\tilde{H}\_{t}\right)\right). |  | (23) |

The output is subsequently processed by the adapter 𝒜​(⋅)\mathcal{A}(\cdot) defined in Section [4.2](https://arxiv.org/html/2601.05975v1#S4.SS2 "4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"), yielding Htcross=𝒜​(Htattn)H\_{t}^{\text{cross}}=\mathcal{A}(H\_{t}^{\text{attn}}).

To handle the asynchronous nature of global closes rigorously, the Key/Value context H~t\tilde{H}\_{t} is defined via the *Filtration-Compliant Context*:

1. 1.

   Directed Delay (Primary Protocol): We strictly lag the entire cross-section to the previous close, H~t=Ht−1\tilde{H}\_{t}=H\_{t-1}. This enforces a causal information gap, compelling the model to learn predictive impulse-response functions (Transfer Entropy).
2. 2.

   Cascading Filtration (Ablation): We construct a composite context, using close times tct\_{\text{c}} where asset ii sees asset jj’s state from day tt if and only if ii closes earlier than jj (e.g., US observing Japan).

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | h~j,t(i)=𝕀​(tc,j<tc,i)​hj,t+𝕀​(tc,j≥tc,i)​hj,t−1.\tilde{h}\_{j,t}^{(i)}=\mathbb{I}(t\_{\text{c},j}<t\_{\text{c},i})\,h\_{j,t}+\mathbb{I}(t\_{\text{c},j}\geq t\_{\text{c},i})\,h\_{j,t-1}. |  | (24) |

![Refer to caption](x3.png)


Figure 4: The Ragged Filtration Problem. The timeline illustrates the asynchrony of global closes relative to the portfolio decision time tt (Europe Close).
A *Cascading Filtration* (red dashed arrow) utilizes the most recent data (in our case we only use close data, but an open could be used), maximizing freshness.
DeePM’s *Directed Delay* (blue solid arrow) strictly lags cross-sectional attention to t−1t-1, enforcing a robust causal gap to isolate predictive impulse-responses.

### 4.4 Structural Regularization: Macro Graph Prior

Data-driven attention can overfit in low-signal regimes. We regularize the cross-sectional representations using a *Graph Attention Network (GAT)* constrained to the fixed *Macroeconomic Prior Graph* 𝒢=(𝒱,ℰ)\mathcal{G}=(\mathcal{V},\mathcal{E}).

##### Structure and Edge Biases.

Similar to the cross-sectional layer, we use a *Post-Norm ReZero* configuration. However, unlike standard GATs which often ignore edge strength, we strictly enforce the economic prior by injecting the adjacency weights directly into the attention mechanism. Inspired by the *Graphormer* framework (Ying et al., [2021](https://arxiv.org/html/2601.05975v1#bib.bib95 "Do transformers really perform bad for graph representation?")), instead of using a hard mask based on edges, we add a *fixed structural bias* derived from the adjacency matrix AA to the attention scores:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αi​j,t=Softmaxj((Q​hi,t)⊤​(K​h~j,t)d+ln(Ai​j),\alpha\_{ij,t}=\text{Softmax}\_{j}\left(\frac{(Qh\_{i,t})^{\top}(K\tilde{h}\_{j,t})}{\sqrt{d}}+\ln(A\_{ij}\right), |  | (25) |

where we handle Ai​j=0A\_{ij}=0 by masking non-edges, setting the corresponding logit to −∞-\infty. Since Ai​jA\_{ij} encodes the strength of the economic linkage (or 0 for no link), the term ln⁡(Ai​j)\ln(A\_{ij}) acts as a soft-masking mechanism: strong links (Ai​j≈1A\_{ij}\approx 1) pass the data-driven attention signal unhindered, while weaker or non-existent links (Ai​j→0A\_{ij}\to 0) introduce large negative penalties, effectively pruning the connection.

The GNN aggregation serves as a residual update to the embeddings. The update is as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hi,tgnn\displaystyle h\_{i,t}^{\text{gnn}} | =LN​(hi,tcross+αgnn⋅∑j∈𝒩​(i)αi​j,t​W​h~j,t),\displaystyle=\text{LN}\left(h\_{i,t}^{\text{cross}}+\alpha\_{\text{gnn}}\cdot\sum\_{j\in\mathcal{N}(i)}\alpha\_{ij,t}W\tilde{h}\_{j,t}\right), |  | (26) |
|  | hi,tfinal\displaystyle h\_{i,t}^{\text{final}} | =𝒜​(hi,tgnn),\displaystyle=\mathcal{A}(h\_{i,t}^{\text{gnn}}), |  |

where 𝒩​(i)\mathcal{N}(i) are neighbors defined by the macro graph and αgnn\alpha\_{\text{gnn}} is the ReZero gate.
To rigorously validate the necessity of this anisotropic attention mechanism, we also implement an *Isotropic GCN* ablation (Kipf and Welling, [2017](https://arxiv.org/html/2601.05975v1#bib.bib47 "Semi-supervised classification with graph convolutional networks")). In the GCN variant, the learnable attention weights αi​j,t\alpha\_{ij,t} are replaced by fixed spectral weights 1/deg​(i)​deg​(j)1/\sqrt{\text{deg}(i)\text{deg}(j)}, forcing the model to aggregate all economic neighbors equally regardless of their current predictive relevance.

### 4.5 Theoretical Interpretations

The architectural choices in DeePM can be unified under two theoretical frameworks: dynamical systems reconstruction and approximate Bayesian inference.

##### Temporal Encoder as State Space Reconstruction.

Financial markets can be viewed as high-dimensional, non-stationary dynamical processes observed through
noisy, partial measurements. Motivated by *Takens’ Embedding Theorem*
(Takens, [1981](https://arxiv.org/html/2601.05975v1#bib.bib16 "Detecting strange attractors in turbulence"); Sauer et al., [1991](https://arxiv.org/html/2601.05975v1#bib.bib88 "Embedology")), delay-coordinate histories can provide a sufficient
representation of latent state under suitable regularity conditions. Our temporal backbone
(V-VSN →\to LSTM →\to TempMHA) therefore learns a data-driven delay map
Φ​(xt−L:t)↦ht\Phi(x\_{t-L:t})\mapsto h\_{t}, projecting the observable price/return history into a latent state
space in which predictive structure is easier to model. Using volatility-normalized returns helps
stabilize scale over time and across assets (reducing heteroskedasticity), which empirically improves
the conditioning of this learned representation.

##### Graph Layer as a Bayesian Structural Prior.

Standard attention mechanisms approximate a purely data-driven posterior p​(Z∣𝒟)p(Z\mid\mathcal{D}). In finance, where the signal-to-noise ratio is low, this often leads to overfitting on spurious correlations. We rigorously interpret the Macro-Graph component as injecting a *Gaussian Markov Random Field (GMRF) Prior* over the asset embeddings, p​(Z∣𝒮)∝exp⁡(−α2​Tr⁡(Z⊤​ℒ​Z))p(Z\mid\mathcal{S})\propto\exp(-\frac{\alpha}{2}\operatorname{Tr}(Z^{\top}\mathcal{L}Z)), where ℒ=I−D−1/2​A​D−1/2\mathcal{L}=I-D^{-1/2}AD^{-1/2} is the normalized graph Laplacian (Rue and Held, [2005](https://arxiv.org/html/2601.05975v1#bib.bib86 "Gaussian markov random fields: theory and applications")). The trace term represents the *Dirichlet energy* of the signal on the graph (Chung, [1997](https://arxiv.org/html/2601.05975v1#bib.bib87 "Spectral graph theory")), which expands as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Tr⁡(Z⊤​ℒ​Z)=12​∑i,jAi​j​‖zidi−zjdj‖22.\operatorname{Tr}(Z^{\top}\mathcal{L}Z)=\frac{1}{2}\sum\_{i,j}A\_{ij}\left\|\frac{z\_{i}}{\sqrt{d\_{i}}}-\frac{z\_{j}}{\sqrt{d\_{j}}}\right\|\_{2}^{2}. |  | (27) |

Minimizing this energy forces economically linked assets (e.g., crude oil and energy equities) to have similar latent representations, scaled by their connectivity, unless the data strongly suggests otherwise. Consequently, the architecture approximates the Maximum A Posteriori (MAP) estimate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z^t≈arg⁡maxZ⁡{log⁡p​(𝒟∣Z)⏟Likelihood (Attn)−α2​Tr⁡(Z⊤​ℒ​Z)⏟ Struct. Prior (Graph)}.\hat{Z}\_{t}\approx\arg\max\_{Z}\Bigl\{\underbrace{\log p(\mathcal{D}\mid Z)}\_{\mathclap{\text{Likelihood (Attn)}}}-\underbrace{\tfrac{\alpha}{2}\operatorname{Tr}(Z^{\top}\mathcal{L}Z)}\_{\mathclap{\text{ Struct. Prior (Graph)}}}\Bigr\}. |  | (28) |

Both the GCN and GAT layers can be viewed as implementing a gradient step on this objective. In high-noise regimes, the prior dominates, smoothing representations across the economic graph to prevent overfitting. In high-signal regimes, the attention mechanism (Likelihood) can override the prior to capture novel market dynamics that deviate from historical economic structures. While a GCN uses the fixed isotropic prior ℒ\mathcal{L}, the GAT layer allows for an anisotropic refinement where the model learns to dynamically adjust the strength of specific economic linkages (Ai​jA\_{ij}) based on the current market regime.

##### Directed Delay as Information-Theoretic Filtering.

The choice of filtration protocol fundamentally alters the statistical dependency learned by the attention mechanism. A *Synchronous* approach (Ht→HtH\_{t}\to H\_{t}) effectively learns *Mutual Information* I​(Xt;Yt)I(X\_{t};Y\_{t}), which is symmetric and dominated by instantaneous co-movements. While high mutual information implies strong correlation, it provides no insight into the direction of influence, making it brittle to regime shifts where correlations break.

By enforcing the strict *Directed Delay* (Ht−1→HtH\_{t-1}\to H\_{t}), we constrain the Cross-Sectional Attention to approximate *Transfer Entropy* (Schreiber, [2000](https://arxiv.org/html/2601.05975v1#bib.bib89 "Measuring information transfer")), a non-linear generalization of Granger Causality222In the linear-Gaussian VAR setting, transfer entropy is equivalent (up to log-base/scaling constants) to Granger causality (Barnett et al., [2009](https://arxiv.org/html/2601.05975v1#bib.bib92 "Granger causality and transfer entropy are equivalent for gaussian variables")).
(Granger, [1969](https://arxiv.org/html/2601.05975v1#bib.bib25 "Investigating causal relations by econometric models and cross-spectral methods")). Transfer Entropy 𝒯j→i\mathcal{T}\_{j\to i} measures the reduction in uncertainty about asset ii’s future state given asset jj’s past, *conditional* on asset ii’s own history:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯j→i=H​(xi,t∣xi,t−1)−H​(xi,t∣xi,t−1,xj,t−1).\mathcal{T}\_{j\to i}=H(x\_{i,t}\mid x\_{i,t-1})-H(x\_{i,t}\mid x\_{i,t-1},x\_{j,t-1}). |  | (29) |

While our model optimizes a Sharpe utility rather than explicitly calculating Shannon entropy, the objectives are aligned: maximizing the Sharpe ratio requires minimizing the variance of the residual return. Under standard Gaussian assumptions333Whilst raw returns are clearly not Gaussian, we volatility-target returns to better approximate homoskedasticity; outside exogenous shocks and abrupt regime shifts, an approximately Gaussian model is a reasonable working assumption., minimizing variance is equivalent to minimizing differential entropy. Consequently, a high attention weight αi​j\alpha\_{ij} implies that the latent state of asset jj at t−1t-1 resolves uncertainty about asset ii at tt (predictive utility) that was not resolved by ii’s own temporal backbone. This asymmetry enables the model to learn structural market hierarchies (e.g., US Rates driving Emerging Market FX) rather than just phenomenological clusters. In our ablation studies (Section [7](https://arxiv.org/html/2601.05975v1#S7 "7 Empirical Findings ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")), this “Causal Sieve” property proves more valuable than the data freshness offered by the Cascading Filtration, suggesting that out-of-sample robustness relies on identifying *drivers* rather than just *peers*.

## 5 Learning Objective and Optimization

Our training process optimizes the realized *Net Portfolio Return* stream ℛ={Rb,tnet​(θ)∣b=1​…​B,t=1​…​T}\mathcal{R}=\{R^{\mathrm{net}}\_{b,t}(\theta)\mid b=1\dots B,t=1\dots T\}, representing the returns across BB independent sequences (batches) over a horizon of LL time-steps. Unlike standard supervised learning, which minimizes MSE, we maximize a differentiable utility function targeting robust risk-adjusted performance. Return premia are regime-dependent and can unwind abruptly (e.g., momentum “crashes” and fast reversals), motivating objectives that do not concentrate risk in a small number of adverse windows. (Wood et al., [2022](https://arxiv.org/html/2601.05975v1#bib.bib83 "Slow momentum with fast reversion: a trading strategy using deep learning and changepoint detection"); Daniel and Moskowitz, [2016](https://arxiv.org/html/2601.05975v1#bib.bib84 "Momentum crashes")).

We specifically focus on the *Sharpe Ratio* (Sharpe, [1966](https://arxiv.org/html/2601.05975v1#bib.bib53 "Mutual fund performance")) rather than raw returns for two reasons:

1. 1.

   Risk Adjustment: Maximizing the Sharpe ratio aligns the training objective with the mandate of a portfolio manager, who seeks to maximize returns per unit of risk rather than absolute performance.
2. 2.

   Statistical Significance: Maximizing the Sharpe Ratio (SR\mathrm{SR}) is mathematically equivalent to maximizing the tt-statistic of the strategy’s expected return444This equivalence holds under i.i.d. elliptical returns with finite variance.. For a batch of size B​LBL, the tt-statistic testing the null hypothesis of zero mean return (H0:μ=0H\_{0}:\mu=0) is given by:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | t=μ^σ^/B​L=B​L⋅μ^σ^=B​L⋅SR.t=\frac{\hat{\mu}}{\hat{\sigma}/\sqrt{BL}}=\sqrt{BL}\cdot\frac{\hat{\mu}}{\hat{\sigma}}=\sqrt{BL}\cdot\mathrm{SR}. |  | (30) |

   Since the window length B​LBL is constant during a training step, the gradient ∇θt\nabla\_{\theta}t is proportional to ∇θSR\nabla\_{\theta}\mathrm{SR}. This aligns the optimization landscape with the objective of finding statistically robust alpha, explicitly penalizing high-variance strategies that might otherwise appear profitable due to “lucky" outliers.

### 5.1 Robust Objective: Pooled Sharpe with SoftMin Penalty

Standard Sharpe maximization often yields policies that “cheat" by overfitting to specific high-return windows while ignoring latent tail risks. To mitigate this, we partition the training sequence into BB non-overlapping windows (e.g., quarterly blocks) and optimize a hybrid objective:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(θ)=−SRpool​(ℛ)⏟Long-Run−λ⋅SoftMinτ​({SRb}b=1B)⏟Robustness.\mathcal{L}(\theta)=-\underbrace{\mathrm{SR}\_{\mathrm{pool}}(\mathcal{R})}\_{\text{Long-Run}}-\lambda\cdot\underbrace{\mathrm{SoftMin}\_{\tau}\Big(\{\mathrm{SR}\_{b}\}\_{b=1}^{B}\Big)}\_{\text{Robustness}}. |  | (31) |

##### 1. Pooled Sharpe Ratio.

SRpool\mathrm{SR}\_{\mathrm{pool}} treats the entire mini-batch history (spanning BB sequences of length LL) as a single contiguous equity curve. It explicitly targets the global risk-adjusted return:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SRpool​(ℛ):=𝔼^​[ℛ]Var^​[ℛ]+ε\mathrm{SR}\_{\mathrm{pool}}(\mathcal{R}):=\frac{\hat{\mathbb{E}}[\mathcal{R}]}{\sqrt{\widehat{\mathrm{Var}}[\mathcal{R}]+\varepsilon}} |  | (32) |

where 𝔼^​[⋅]\hat{\mathbb{E}}[\cdot] and Var^​[⋅]\widehat{\mathrm{Var}}[\cdot] denote the empirical mean and variance operators over the full set of realized net returns across all BB blocks and LL time-steps. Specifically, the pooled sample mean is 𝔼^​[ℛ]:=1B​L​∑b=1B∑t=1LRb,tnet\hat{\mathbb{E}}[\mathcal{R}]:=\frac{1}{BL}\sum\_{b=1}^{B}\sum\_{t=1}^{L}R^{\mathrm{net}}\_{b,t}, with ε\varepsilon serving as a small numerical stability constant.

Mathematical Motivation (Consistency and Bias):
Assume the strategy return process is stationary and ergodic.555Financial returns are not strictly stationary over long horizons due to structural breaks and evolving market microstructure; we adopt stationarity/ergodicity as a useful idealization that justifies interpreting empirical moments as long-run expectations.
The pooled metric SRpool\mathrm{SR}\_{\mathrm{pool}} uses an effective sample size on the order of Neff≈B×LN\_{\text{eff}}\approx B\times L (up to dependence adjustments). Under ergodicity, the sample mean and variance converge to their population counterparts, and by the continuous mapping theorem SRpool\mathrm{SR}\_{\mathrm{pool}} converges (in probability) to the population Sharpe ratio as B​L→∞BL\to\infty.
In contrast, the naïve average of window-wise Sharpes,
SR¯=1B​∑b=1BSR^b\overline{\mathrm{SR}}=\frac{1}{B}\sum\_{b=1}^{B}\widehat{\mathrm{SR}}\_{b},
aggregates *ratios* computed on shorter samples and is therefore generally biased and higher-variance in finite samples (since SR^b\widehat{\mathrm{SR}}\_{b} is itself a biased ratio estimator).
Moreover, following Lo ([2002](https://arxiv.org/html/2601.05975v1#bib.bib9 "The statistics of sharpe ratios")), the variance of SR^\widehat{\mathrm{SR}} scales as O​(1/L)O(1/L) (under weak dependence); pooling increases the effective sample size, reducing gradient noise and stabilizing optimization.

##### 2. SoftMin as an Adversarial Prior.

To ensure the policy survives adverse regimes, we penalize the smooth minimum of the per-window Sharpe ratios {SRb}\{\mathrm{SR}\_{b}\}. The SoftMin function with temperature τ\tau is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SoftMinτ​({SRb}):=−τ​log⁡(1B​∑b=1Be−SRbτ).\mathrm{SoftMin}\_{\tau}(\{\mathrm{SR}\_{b}\}):=-\tau\log\left(\frac{1}{B}\sum\_{b=1}^{B}\mathrm{e}^{-\frac{\mathrm{SR}\_{b}}{\tau}}\right). |  | (33) |

As discussed in Section [2.5](https://arxiv.org/html/2601.05975v1#S2.SS5 "2.5 Robust Objectives and Risk Measures ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"), minimizing −SoftMin-\mathrm{SoftMin} is mathematically equivalent to minimizing the dual form of *Entropic Value-at-Risk (EVaR)* (Ahmadi-Javid, [2012](https://arxiv.org/html/2601.05975v1#bib.bib34 "Entropic value-at-risk: a new coherent risk measure")). This effectively trains the model against an implicit adversary who reweights the training windows to emphasize the worst-performing periods (minimax optimization).

The temperature parameter τ>0\tau>0 governs the aggressiveness of this adversary. As τ→0\tau\to 0, the function approaches the hard minimum (minb⁡SRb\min\_{b}\mathrm{SR}\_{b}), forcing the model to focus exclusively on the single worst-performing window (pure minimax). Conversely, as τ→∞\tau\to\infty, the function converges to the arithmetic mean, recovering a standard risk-neutral objective. In practice, τ\tau acts as a tunable “robustness control": lower values produce more conservative policies that prioritize survival in difficult regimes, while higher values allow the model to focus on average-case performance.

Empirically, we find that this soft adversarial mechanism significantly stabilizes training. By penalizing potential collapse in “hard" windows, the gradient descent is prevented from greedily overfitting to “easy" low-volatility regimes, a common pathology in financial deep-learning. For an in-depth analysis, including the connection to EVaR, see App. [D](https://arxiv.org/html/2601.05975v1#A4 "Appendix D Analysis of the Robust Objective ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").

### 5.2 Ensembling and Implicit Cost Regularization

Deep reinforcement learning is notoriously sensitive to initialization. We mitigate this via an ensemble of the top KK models, a practice well-supported in the literature for predictive uncertainty estimation (Lakshminarayanan et al., [2017](https://arxiv.org/html/2601.05975v1#bib.bib26 "Simple and scalable predictive uncertainty estimation using deep ensembles")). Beyond variance reduction, we prove that ensembling acts as a structural regularizer for transaction costs.

##### Proposition 1 (Convexity of Turnover Cost).

Let 𝒞​(p)=γ​∑t|Δ​wt​(p)|\mathcal{C}(p)=\gamma\sum\_{t}|\Delta w\_{t}(p)| be the proportional transaction cost function associated with a policy pp. This function is convex in pp.

##### Corollary (Jensen’s Inequality for Trading).

For an ensemble of KK independent policies {p(k)}k=1K\{p^{(k)}\}\_{k=1}^{K} and their average p¯=1K​∑p(k)\bar{p}=\frac{1}{K}\sum p^{(k)}, Jensen’s inequality implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞​(p¯)≤1K​∑k=1K𝒞​(p(k)).\mathcal{C}(\bar{p})\;\leq\;\frac{1}{K}\sum\_{k=1}^{K}\mathcal{C}(p^{(k)}). |  | (34) |

Implication: The trading cost of the ensemble is strictly upper-bounded by the average cost of its constituents. Idiosyncratic “noise trades" made by individual models tend to cancel out in the average, structurally reducing turnover and improving the net Sharpe ratio.

This theoretical guarantee informs our hyperparameter choice for the explicit turnover penalty γ\gamma (Eq. [13](https://arxiv.org/html/2601.05975v1#S3.E13 "Equation 13 ‣ 3.2 Portfolio Returns and Frictions ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")). As shown in Appendix [B](https://arxiv.org/html/2601.05975v1#A2 "Appendix B Turnover Guarantees for Ensembles ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"), the optimal training penalty γ⋆\gamma^{\star} is strictly lower for ensembles than for single models. We essentially “outsource" part of the regularization burden to the ensemble mechanism, allowing individual models to remain responsive to valid signals.

### 5.3 Optimization Protocol

We train using AdamW with a rolling window approach. To ensure the Sharpe ratio statistics in Eq. (1) are stable, we require a large effective batch size (e.g., spanning multiple years of data).
Since GPU memory is limited, we introduce *Exact Gradient Accumulation* for global statistics. We accumulate the sufficient statistics (∑Rt,∑Rt2\sum R\_{t},\sum R\_{t}^{2}) across micro-batches to compute the exact μ\mu and σ\sigma for the full logical batch before performing the backward pass, detailed in Sec. [C.2](https://arxiv.org/html/2601.05975v1#A3.SS2 "C.2 Analyatical Gradients ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"). This ensures the optimization landscape is invariant to GPU memory constraints.

Financial time series require a warm-up period for recursive states (e.g., LSTM hidden states) to stabilize. We implement a *burn-in* of L0=21L\_{0}=21 steps (approx. 1 month). During this phase, the model processes inputs to update its internal state, but gradients are masked and returns do not contribute to the loss function. This ensures that only “mature" representations, fully conditioned on the valid history, are passed to the optimizer, preventing initial state noise from corrupting the learning process.

## 6 Experimental Design

### 6.1 Benchmarks

To isolate the contributions of DeePM’s end-to-end architecture, we compare against three benchmark families: (A) passive/rule-based allocations, (B) classical trend-following signals (producing risk weights directly), and (C) two-stage “signal →\rightarrow allocation” pipelines that combine a forecast signal with a covariance-aware risk allocator.

All benchmarks are evaluated under the same execution and return accounting as DeePM. Risk weights pi,tp\_{i,t} map to vol-targeted notionals via Eq. ([12](https://arxiv.org/html/2601.05975v1#S3.E12 "Equation 12 ‣ 3.2 Portfolio Returns and Frictions ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")), and net performance is computed using the same transaction-cost model. Throughout, the covariance input Σ^t\hat{\Sigma}\_{t} to all two-stage allocators is estimated on vol-scaled daily returns using a 252-day rolling window with Ledoit–Wolf shrinkage (Ledoit and Wolf, [2004](https://arxiv.org/html/2601.05975v1#bib.bib77 "A well-conditioned estimator for large-dimensional covariance matrices")).

#### 6.1.1 Passive and Rule-Based

* •

  Passive Equal Risk: A constant long risk weight pi,t≡1p\_{i,t}\equiv 1 for all tradable assets. Under the volatility targeting framework (Eq. ([12](https://arxiv.org/html/2601.05975v1#S3.E12 "Equation 12 ‣ 3.2 Portfolio Returns and Frictions ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"))), this ensures that wi,t∝1/σ^i,tw\_{i,t}\propto 1/\hat{\sigma}\_{i,t}, representing a static risk-parity exposure to global macro risk premia without active timing.

#### 6.1.2 Classical Trend-Following

These strategies generate risk weights pi,tp\_{i,t} directly from univariate price history.

* •

  TSMOM (Time-Series Momentum): Following Moskowitz et al. ([2012](https://arxiv.org/html/2601.05975v1#bib.bib69 "Time series momentum")), positions are determined by the sign of the past 12-month return:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | pi,tTS=sign​(ri,t−252:t)=sign​(Pi,tPi,t−252−1).p^{\mathrm{TS}}\_{i,t}=\mathrm{sign}\left(r\_{i,t-252:t}\right)=\mathrm{sign}\left(\frac{P\_{i,t}}{P\_{i,t-252}}-1\right). |  | (35) |
* •

  Multi-Scale MACD: We implement a continuous trend signal using volatility-normalized Moving Average Convergence Divergence (MACD) indicators across three time-scales (S,L)∈{(8,24),(16,48),(32,96)}(S,L)\in\{(8,24),(16,48),(32,96)\}. The raw MACD values are mapped to positions via a sigmoidal response function ϕ​(x)=x​e−x2/4/0.89\phi(x)=x\mathrm{e}^{-x^{2}/4}/0.89 (Baz et al., [2015](https://arxiv.org/html/2601.05975v1#bib.bib61 "Dissecting investment strategies in the cross section and time series"); Lim et al., [2019](https://arxiv.org/html/2601.05975v1#bib.bib62 "Enhancing time-series momentum strategies using deep neural networks")) to squash outliers while maintaining linearity near zero:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | pi,tMACD=13​∑k=13ϕ​(EWMSk​(Pi)−EWMLk​(Pi)σ^i,t).p^{\mathrm{MACD}}\_{i,t}=\frac{1}{3}\sum\_{k=1}^{3}\phi\left(\frac{\text{EWM}\_{S\_{k}}(P\_{i})-\text{EWM}\_{L\_{k}}(P\_{i})}{\hat{\sigma}\_{i,t}}\right). |  | (36) |

#### 6.1.3 Two-Stage Signal–Allocation Baselines

These baselines separate forecasting from portfolio construction. First, a signal generator produces a raw cross-sectional vector st∈ℝNs\_{t}\in\mathbb{R}^{N} (representing the TSMOM or MACD values across all NN assets at time tt). Second, a covariance-aware allocator maps this vector sts\_{t} to final risk weights ptp\_{t}.

* •

  Risk Managed Trend: A scalar approach where raw trend signals sts\_{t} (from TSMOM or MACD) are normalized to unit leverage p~t=st/‖st‖1\tilde{p}\_{t}=s\_{t}/\|s\_{t}\|\_{1} and then scaled to target portfolio volatility σtgt\sigma\_{\text{tgt}} using the ex-ante covariance matrix Σ^t\hat{\Sigma}\_{t}:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | pt=σtgtp~t⊤​Σ^t​p~t​p~t.p\_{t}=\frac{\sigma\_{\text{tgt}}}{\sqrt{\tilde{p}\_{t}^{\top}\hat{\Sigma}\_{t}\tilde{p}\_{t}}}\tilde{p}\_{t}. |  | (37) |
* •

  Rolling MVO (Mean–Variance Optimization): Following the classical mean–variance form in ([1](https://arxiv.org/html/2601.05975v1#S2.E1 "Equation 1 ‣ 2.2 Machine Learning for Portfolio Construction under Frictions ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")), we proxy expected returns by the trend signal (μ^t∝st\hat{\mu}\_{t}\propto s\_{t}) and stabilize the inversion with ridge regularization. The resulting positions are

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ptMVO∝(Σ^t+λ​I)−1​st,p\_{t}^{\text{MVO}}\;\propto\;\bigl(\hat{\Sigma}\_{t}+\lambda I\bigr)^{-1}s\_{t}, |  | (38) |

  where Σ^t\hat{\Sigma}\_{t} is a rolling shrinkage covariance estimate and λ>0\lambda>0 controls conditioning. The covariance Σ^t\hat{\Sigma}\_{t} is estimated using Ledoit-Wolf shrinkage (Ledoit and Wolf, [2004](https://arxiv.org/html/2601.05975v1#bib.bib77 "A well-conditioned estimator for large-dimensional covariance matrices")) over a rolling 252-day window.
  To manage turnover, we optionally add a quadratic turnover penalty κ​‖𝐩t−𝐩t−1‖22\kappa\|\mathbf{p}\_{t}-\mathbf{p}\_{t-1}\|\_{2}^{2}, yielding an analytic update that anchors the portfolio to the previous day’s weights:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ptMVO-TP∝(Σ^t+κ​I)−1​(st+κ​pt−1).p\_{t}^{\text{MVO-TP}}\propto(\hat{\Sigma}\_{t}+\kappa I)^{-1}(s\_{t}+\kappa p\_{t-1}). |  | (39) |

  For the TSMOM two-stage pipeline, we set κ=10\kappa=10. Given that our assets are scaled to unit daily variance (σ2≈1\sigma^{2}\approx 1) and the input signals are binary (±1\pm 1), a high penalty is required to dominate the covariance term. This dampens the response to instantaneous signal flips, creating a slow-moving anchor that naturally suppresses noise and limits leverage without requiring a hard cap.
* •

  Risk Parity (ERC): An Equal Risk Contribution allocator (Maillard et al., [2010](https://arxiv.org/html/2601.05975v1#bib.bib71 "The properties of equally weighted risk contribution portfolios")). We solve for long-only weights qt∈ℝ≥0Nq\_{t}\in\mathbb{R}^{N}\_{\geq 0} such that every asset contributes equally to ex-ante portfolio risk. Formally, the risk contribution of asset ii is defined as RCi=qi​(Σ^t​qt)iqt⊤​Σ^t​qt\text{RC}\_{i}=q\_{i}\frac{(\hat{\Sigma}\_{t}q\_{t})\_{i}}{\sqrt{q\_{t}^{\top}\hat{\Sigma}\_{t}q\_{t}}}. We optimize qtq\_{t} such that RCi=RCj​∀i,j\text{RC}\_{i}=\text{RC}\_{j}\forall i,j. Finally, we impose the directionality of the original signal vector sts\_{t} via element-wise multiplication:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | pt=sign​(st)⊙qt.p\_{t}=\text{sign}(s\_{t})\odot q\_{t}. |  | (40) |

  This ensures that while the position magnitudes are determined by the optimizer to equalize risk, the direction (long or short) is strictly preserved from the trend signal.

#### 6.1.4 Learning-Based Baselines

* •

  Momentum Transformer: A variant of the architecture proposed by Wood et al. ([2023](https://arxiv.org/html/2601.05975v1#bib.bib75 "Trading with the momentum transformer: an intelligent and interpretable architecture")), which corresponds to the temporal encoder of DeePM. This serves as our primary deep learning baseline to quantify the marginal value of DeePM’s Graph and Directed Delay components (see Wood et al. ([2023](https://arxiv.org/html/2601.05975v1#bib.bib75 "Trading with the momentum transformer: an intelligent and interpretable architecture")) for comparisons of the Momentum Transformer against other simpler models). It slightly deviates from the original *Momentum Transformer* by updating components such as the adapter blocks and VSN to align with more recent developments. Additionally, for fairness, we use the same transaction cost regularizer as DeePM.

### 6.2 Ablation Study Design

To rigorously evaluate the individual contributions of DeePM’s architectural components and training objectives, we conduct a systematic ablation study. Our experimental design is structured to test four core hypotheses: (1) that the explicit macroeconomic graph structure acts as a necessary regularizer for cross-asset learning; (2) that the directed delay mechanism is crucial for learning causal rather than spurious correlations; (3) that the robust SoftMin objective provides superior stability; (4) that end-to-end internalization of transaction costs outperforms heuristic post-processing; and (5) that end-to-end internalization of transaction costs is most effective when trained with a relaxed scalar γ<1\gamma<1, as per Eqn. ([13](https://arxiv.org/html/2601.05975v1#S3.E13 "Equation 13 ‣ 3.2 Portfolio Returns and Frictions ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")), (defaulting to γ=0.5\gamma=0.5 in our standard configuration) to balance turnover penalization against signal capture. By systematically removing or replacing these components from the best-performing ensemble configuration, we aim to isolate their marginal value to the final risk-adjusted performance.

### 6.3 Evaluation Metrics

For fair comparison across strategies with different intrinsic risk profiles, all out-of-sample return series are rescaled *ex-post* to a uniform annualized volatility target of σtgt=10%\sigma\_{\text{tgt}}=10\%. Let RtR\_{t} denote the rescaled daily net return and PtP\_{t} the cumulative wealth index at time tt.

##### Performance and Risk.

* •

  Net Sharpe Ratio (SR): The primary metric for risk-adjusted return efficiency after transaction costs (Sharpe, [1966](https://arxiv.org/html/2601.05975v1#bib.bib53 "Mutual fund performance")). Defined as the annualized mean return divided by the annualized volatility:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | SR=252⋅𝔼^​[Rt]Var^​[Rt].\text{SR}=\sqrt{252}\cdot\frac{\widehat{\mathbb{E}}[R\_{t}]}{\sqrt{\widehat{\text{Var}}[R\_{t}]}}. |  | (41) |

  We also report Gross SR to quantify the “execution gap" (performance degradation due to trading frictions). This metric tests whether the strategy generates excess returns per unit of total risk.
* •

  Compound Annual Growth Rate (CAGR): The geometric rate of return, capturing the effect of volatility drag on long-term wealth accumulation:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | CAGR=(∏t=1T(1+Rt))252/T−1.\text{CAGR}=\left(\prod\_{t=1}^{T}(1+R\_{t})\right)^{252/T}-1. |  | (42) |

  This metric evaluates the final wealth multiplier available to an investor, accounting for the compounding of losses.
* •

  Maximum Drawdown (MDD): The largest peak-to-trough decline in the cumulative equity curve over the test period (Magdon-Ismail et al., [2004](https://arxiv.org/html/2601.05975v1#bib.bib10 "On the maximum drawdown of a brownian motion")), measuring the worst historical loss:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | MDD=mint∈[0,T]⁡(Ptmaxs≤t⁡Ps−1).\text{MDD}=\min\_{t\in[0,T]}\left(\frac{P\_{t}}{\max\_{s\leq t}P\_{s}}-1\right). |  | (43) |

  This tests the strategy’s tail risk and potential for capital preservation during adverse regimes.
* •

  Calmar Ratio: A tail-risk-adjusted performance measure defined as the ratio of annualized return to absolute maximum drawdown (Young, [1991](https://arxiv.org/html/2601.05975v1#bib.bib60 "Calmar ratio: a smoother tool")):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Calmar=CAGR|MDD|.\text{Calmar}=\frac{\text{CAGR}}{|\text{MDD}|}. |  | (44) |

  This metric assesses whether returns are sufficient to compensate for the psychological and financial cost of deep drawdowns.
* •

  Heteroskedasticity and Autocorrelation Consistent (HAC) tt-statistic (tt): The tt-statistic for the null hypothesis that the strategy’s mean net return is zero (H0:μ=0H\_{0}:\mu=0). To ensure valid inference under the serial correlation and heteroskedasticity typical of financial time series, we utilize Newey-West standard errors (Newey and West, [1987](https://arxiv.org/html/2601.05975v1#bib.bib56 "A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix")). This provides a statistical significance test for the existence of a positive risk premium.

##### Execution and Turnover.

* •

  Average Holding Period (Hold): A direct proxy for trading frequency and transaction cost efficiency. We define turnover τ\tau as the average daily absolute change in position weights. The implied holding period is calculated relative to the average Gross Market Value (GMV) to account for leverage scaling:

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | Hold | =2×252τ/Avg. GMV,\displaystyle=\frac{2\times 252}{\tau/\text{Avg.\ GMV}}, |  | (45) |
  |  | whereτ\displaystyle\text{where}\quad\tau | =252T​∑t=1T1Nt​∑i=1Nt|wi,t−wi,t−1|.\displaystyle=\frac{252}{T}\sum\_{t=1}^{T}\frac{1}{N\_{t}}\sum\_{i=1}^{N\_{t}}\lvert w\_{i,t}-w\_{i,t-1}\rvert. |  |

  This diagnostic checks whether the strategy’s alpha decay matches its trading horizon. Note that all strategies are long/short, meaning positions wi,tw\_{i,t} can be positive (long) or negative (short).

##### Benchmark Relative Metrics.

We compare all strategies against the *Passive Equal Risk* benchmark (RtbenchR\_{t}^{\text{bench}}).

* •

  Information Ratio (IR): The risk-adjusted active return, defined as the annualized mean of the excess return spread divided by the tracking error (standard deviation of the spread):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | IR=252⋅𝔼^​[Rt−Rtbench]Var^​[Rt−Rtbench].\text{IR}=\sqrt{252}\cdot\frac{\widehat{\mathbb{E}}[R\_{t}-R\_{t}^{\text{bench}}]}{\sqrt{\widehat{\text{Var}}[R\_{t}-R\_{t}^{\text{bench}}]}}. |  | (46) |

  This measures the consistency of the strategy’s value-add over a passive allocation.
* •

  Alpha tt-statistic (tαt\_{\alpha}): The HAC-adjusted tt-statistic testing the statistical significance of the excess return (H0:𝔼​[Rt−Rtbench]≤0H\_{0}:\mathbb{E}[R\_{t}-R\_{t}^{\text{bench}}]\leq 0). A value >2.0>2.0 usually indicates statistically significant outperformance. This confirms whether the strategy provides genuine alpha beyond the risk premia available in the benchmark.
* •

  Correlation (ρ\rho): The Pearson correlation coefficient between the strategy’s net returns and the benchmark returns:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ρ=Cov^​(Rt,Rtbench)σ^strat⋅σ^bench.\rho=\frac{\widehat{\text{Cov}}(R\_{t},R\_{t}^{\text{bench}})}{\hat{\sigma}\_{\text{strat}}\cdot\hat{\sigma}\_{\text{bench}}}. |  | (47) |

  Lower correlation implies the strategy captures unique structural alpha rather than static beta exposure.

### 6.4 Training Protocol and Data Splits

We evaluate the model using a strict *Walk-Forward Validation* scheme to prevent look-ahead bias. We partition the dataset (1990–2025) into five-year expanding blocks. For each block, the model is trained on all prior history, validated on the subsequent 10% of the window, and tested on the following 5 years. The model is fully retrained every 5 years. Scalers (volatility, costs) are fit on the training set and frozen for the test period. We report performance on the union of out-of-sample blocks from 2010–2025 (inclusive).

To ensure robustness against initialization noise, we train 50 independent seeds for each architecture. We construct the final policy by averaging the signals of the top half (K=25K=25) ranked by validation Sharpe ratio. This selection protocol (50 seeds →\to Top 25) was calibrated based on an out-of-sample study of the Momentum Transformer over the 2000–2010 period; the cross-sectional DeePM methods require the fuller history (training data up to 2010) to stabilize the learning of the graph structure and thus rely on the protocol established by the temporal baseline. Our results Sec. [7](https://arxiv.org/html/2601.05975v1#S7 "7 Empirical Findings ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") demonstrate that there is little difference in performance between K∈{10,25,50}K\in\{10,25,50\}, once we have benefited from ensembling.

We use rolling sequences of length 84 trading days. Motivated by (Wood et al., [2024](https://arxiv.org/html/2601.05975v1#bib.bib63 "Few-shot learning patterns in financial time series for trend-following strategies")), the first 21 steps of each sequence are treated as a burn-in period and are used solely to initialize the recurrent states, with the 63 days of evaluation aligning with the literature (Lim et al., [2019](https://arxiv.org/html/2601.05975v1#bib.bib62 "Enhancing time-series momentum strategies using deep neural networks")). Gradients are masked during the burn-in period to ensure that optimization is driven by stable internal representations. Additional experimental details are provided in Appendix [E](https://arxiv.org/html/2601.05975v1#A5 "Appendix E Experimental Implementation Details ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"). Excluding the burn-in steps, the training and validation data are constructed by segmenting the time series into non-overlapping sequences. We use a 90/10 chronological split for training and validation. For out-of-sample backtesting, we again use sequences of length 84, but increase the burn-in period to 63 days to provide a richer historical context for trading decisions. Importantly, we do not explicitly retrain across regimes; instead, regime variation is handled implicitly through the proposed robust loss.

The SoftMin loss hyperparameters τ=1/5\tau=1/5 and λ=0.1\lambda=0.1 were selected based on validation Sharpe, which does not include the SoftMin loss term. All other hyperparameters are listed in Appendix [E](https://arxiv.org/html/2601.05975v1#A5 "Appendix E Experimental Implementation Details ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").

## 7 Empirical Findings

### 7.1 Results

We quantify the contribution of each architectural and objective component by ablating it from the best-performing DeePM specification. The baseline is the full model trained on the proposed joint net-Sharpe objective (τ=0.5,λ=1/5\tau=0.5,\;\lambda=1/5) with macro-graph filtering (GAT), lagged cross-sectional attention, volatility scaling, top half of seeds based on validation loss, and transaction costs with training scaler γ=0.5\gamma=0.5; it achieves a normalized out-of-sample Net Sharpe of 0.93. Each ablation modifies exactly one component. For fairness, we also train the *Momentum Transformer* with transaction costs and training scaler γ=0.5\gamma=0.5. The empirical results for the 2010–2025 period are presented in Table [1](https://arxiv.org/html/2601.05975v1#S7.T1 "Table 1 ‣ 7.1 Results ‣ 7 Empirical Findings ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").

It is important to note that our evaluation focuses on the post-2010 regime and incorporates a highly realistic transaction cost model (incorporating tick-size constraints and liquidity scalars). This rigorous setting contrasts with studies that benefit from the high-trend 1990s era or assume simplified execution costs (such as the original Momentum Transformer). Our period aligns with the “CTA Winter” of the 2010s, then the post-2020 volatility transition, which we further isolate in Table [2](https://arxiv.org/html/2601.05975v1#S7.T2 "Table 2 ‣ 7.1 Results ‣ 7 Empirical Findings ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"), to assess resilience during the pandemic, inflation shocks, and the subsequent higher-for-longer regime.

Table 1: Out-of-Sample Performance 2010–2025 (end). All strategies are rescaled to 10% annualized volatility. SR: annualized Sharpe ratio. CAGR: compound annual growth rate. MDD: maximum drawdown. Calmar: CAGR/|MDD|\mathrm{CAGR}/|\mathrm{MDD}|. Hold (days): implied average holding period in days (execution/turnover efficiency proxy; ∞\infty denotes buy-and-hold). Gross metrics exclude transaction costs; Net metrics include transaction costs. vs Bench. (Net): metrics relative to Passive Equal Risk (IR: information ratio of excess return, tαt\_{\alpha}: HAC tt-statistic of excess return, ρ\rho: return correlation). tt: HAC tt-statistic of the strategy’s own net return.

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Gross | Net | | | | | Exec | vs Bench. (Net) | | |
|  | Strategy | SR | SR | tt | CAGR | Calmar | MDD | (days) | IR | tαt\_{\alpha} | ρ\rho |
|  | DeePM | 1.29 | 0.93 | 3.69 | 9.2% | 0.58 | -16.0% | 7.1 | 0.44 | 1.85 | 0.52 |
|  | DeePM (MACD features) | 1.10 | 0.84 | 3.26 | 8.2% | 0.49 | -16.9% | 10.4 | 0.38 | 1.57 | 0.61 |
| Baselines | Passive Equal Risk (Bench.) | 0.50 | 0.50 | 1.90 | 4.6% | 0.17 | -27.1% | ∞\infty | - | - | 1.00 |
| Trend (TSMOM) | 0.51 | 0.45 | 1.75 | 4.1% | 0.21 | -19.8% | 32.2 | -0.03 | -0.10 | 0.02 |
| Risk Managed Trend | 0.49 | 0.39 | 1.50 | 3.5% | 0.13 | -26.8% | 14.6 | -0.07 | -0.26 | 0.02 |
| MVO Trend | 0.55 | -0.07 | -0.26 | -1.2% | -0.02 | -51.4% | 5.1 | -0.41 | -1.56 | 0.05 |
| MVO-TP Trend | 0.59 | 0.47 | 1.79 | 4.3% | 0.15 | -28.8% | 15.1 | -0.01 | -0.05 | 0.06 |
| Risk Parity Trend | 0.35 | 0.18 | 0.75 | 1.4% | 0.04 | -32.2% | 9.9 | -0.22 | -0.83 | 0.04 |
| MACD Multi-Scale | 0.28 | 0.25 | 1.00 | 2.0% | 0.08 | -23.8% | 38.5 | -0.17 | -0.66 | -0.05 |
| Risk Managed MACD | 0.26 | 0.20 | 0.81 | 1.5% | 0.05 | -27.9% | 16.0 | -0.20 | -0.80 | -0.04 |
| MVO-TP MACD | 0.24 | 0.15 | 0.61 | 1.0% | 0.04 | -23.6% | 16.6 | -0.24 | -0.97 | 0.01 |
| Mom. Transformer (γ=0\gamma=0) | 1.10 | 0.60 | 2.44 | 5.6% | 0.21 | -26.3% | 4.0 | 0.10 | 0.42 | 0.45 |
| Mom. Transformer (γ=0.5\gamma=0.5) | 1.02 | 0.66 | 2.54 | 6.2% | 0.20 | -31.9% | 5.0 | 0.15 | 0.60 | 0.39 |
| Architecture | Cascading lag | 1.19 | 0.84 | 3.29 | 8.2% | 0.44 | -18.7% | 7.5 | 0.34 | 1.41 | 0.51 |
| Independent (No Structure) | 1.18 | 0.83 | 3.34 | 8.2% | 0.48 | -17.0% | 7.7 | 0.33 | 1.35 | 0.50 |
| No Cross-Attn (Graph Only) | 1.15 | 0.84 | 3.24 | 8.2% | 0.44 | -18.4% | 7.7 | 0.37 | 1.54 | 0.60 |
| No Graph (Cross-Attn Only) | 1.13 | 0.79 | 3.11 | 7.7% | 0.39 | -19.8% | 7.5 | 0.29 | 1.19 | 0.51 |
| Flip Graph/Cross-Attention | 1.21 | 0.87 | 3.38 | 8.5% | 0.43 | -19.8% | 7.5 | 0.39 | 1.64 | 0.58 |
| No ReZero | 0.85 | 0.71 | 2.70 | 6.8% | 0.40 | -17.0% | 14.5 | 0.26 | 1.08 | 0.70 |
| GCN (Isotropic) | 1.09 | 0.81 | 3.12 | 7.9% | 0.44 | -17.9% | 8.3 | 0.37 | 1.55 | 0.65 |
| Loss | No SoftMin (Pooled Only) | 0.79 | 0.68 | 2.70 | 6.5% | 0.50 | -13.0% | 18.4 | 0.20 | 0.84 | 0.62 |
| SoftMin τ=1\tau=1 | 1.25 | 0.85 | 3.40 | 8.3% | 0.54 | -15.5% | 6.9 | 0.34 | 1.42 | 0.49 |
| SoftMin τ=0.05\tau=0.05 | 1.17 | 0.83 | 3.33 | 8.1% | 0.48 | -16.7% | 8.1 | 0.33 | 1.38 | 0.51 |
| Zero Cost Training γ=0\gamma=0 | 1.17 | 0.56 | 2.29 | 5.2% | 0.16 | -32.1% | 4.9 | 0.05 | 0.20 | 0.33 |
| Full Cost Training γ=1\gamma=1 | 0.81 | 0.70 | 2.69 | 6.7% | 0.41 | -16.4% | 19.0 | 0.25 | 1.07 | 0.70 |
| Ensemble | Best Seed K=1K=1 | 1.11 | 0.72 | 2.88 | 7.0% | 0.41 | -16.8% | 6.6 | 0.20 | 0.79 | 0.38 |
| Top 10 Seeds K=10K=10 | 1.30 | 0.93 | 3.63 | 9.1% | 0.56 | -16.3% | 6.7 | 0.40 | 1.67 | 0.45 |
| All Seeds K=50K=50 | 1.06 | 0.86 | 3.33 | 8.4% | 0.57 | -14.7% | 10.7 | 0.44 | 1.85 | 0.68 |
| 100-seed K=50K=50 (2x both) | 1.26 | 0.93 | 3.64 | 9.2% | 0.54 | -16.9% | 7.6 | 0.46 | 1.93 | 0.57 |




Table 2: Out-of-Sample Performance 2020–2025 (end). All strategies are rescaled to 10% annualized volatility. See Table [1](https://arxiv.org/html/2601.05975v1#S7.T1 "Table 1 ‣ 7.1 Results ‣ 7 Empirical Findings ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") for the legend.

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Gross | Net | | | | | Exec | vs Bench. (Net) | | |
|  | Strategy | SR | SR | tt | CAGR | Calmar | MDD | (days) | IR | tαt\_{\alpha} | ρ\rho |
|  | DeePM | 1.07 | 0.79 | 1.84 | 7.7% | 0.56 | -13.8% | 8.0 | 0.45 | 1.16 | 0.57 |
|  | DeePM (MACD features) | 1.16 | 0.97 | 2.20 | 9.6% | 0.65 | -14.9% | 11.4 | 0.68 | 1.67 | 0.62 |
| Baselines | Passive Equal Risk (Bench.) | 0.38 | 0.37 | 0.84 | 3.2% | 0.17 | -18.8% | ∞\infty | - | - | 1.00 |
| Trend (TSMOM) | 0.43 | 0.38 | 0.89 | 3.3% | 0.18 | -18.9% | 24.5 | 0.00 | 0.01 | -0.08 |
| Risk Managed Trend | 0.29 | 0.20 | 0.47 | 1.5% | 0.07 | -21.4% | 13.0 | -0.11 | -0.26 | -0.06 |
| MVO Trend | 0.42 | -0.15 | -0.36 | -2.0% | -0.06 | -34.3% | 5.2 | -0.37 | -0.85 | 0.01 |
| MVO-TP Trend | 0.31 | 0.20 | 0.48 | 1.6% | 0.07 | -22.1% | 13.1 | -0.11 | -0.26 | -0.01 |
| Risk Parity Trend | 0.50 | 0.35 | 0.84 | 3.1% | 0.12 | -25.7% | 8.9 | -0.01 | -0.02 | -0.08 |
| MACD (Multi-Scale) | 0.29 | 0.26 | 0.65 | 2.2% | 0.09 | -24.4% | 35.9 | -0.07 | -0.17 | -0.09 |
| Risk Managed MACD | 0.10 | 0.04 | 0.09 | -0.1% | -0.00 | -27.2% | 15.7 | -0.23 | -0.52 | -0.08 |
| MVO-TP MACD | 0.11 | 0.03 | 0.08 | -0.2% | -0.01 | -23.3% | 16.3 | -0.23 | -0.56 | -0.04 |
| Mom. Transformer (γ=0\gamma=0) | 0.64 | 0.18 | 0.45 | 1.3% | 0.07 | -18.6% | 3.8 | -0.19 | -0.49 | 0.52 |
| Mom. Transformer (γ=0.5\gamma=0.5) | 0.65 | 0.38 | 0.87 | 3.3% | 0.16 | -20.7% | 5.7 | 0.01 | 0.02 | 0.62 |

![Refer to caption](images/net_pnl.png)


Figure 5: Cumulative net-of-cost wealth growth for DeePM variants versus standard systematic baselines (2010–2025). The y-axis utilizes a logarithmic scale to properly visualize long-term compounding differences.

### 7.2 Discussion of Empirical Findings

##### Economic Significance and Net Performance.

The DeePM Ensemble demonstrates statistically significant outperformance against both passive risk premia and deep learning baselines. Notably, the proposed model achieves a Net Sharpe ratio of 0.93 with a highly significant HAC tt-statistic of 3.69, confirming the existence of a robust risk premium net of transaction costs. This performance exceeds the Passive Equal Risk (0.50) and TSMOM (0.45) benchmarks by a wide margin. Crucially, it outperforms the state-of-the-art Momentum Transformer trained with the same transaction cost regularization (γ=0.5\gamma=0.5) which achieved a Net Sharpe of 0.66, highlighting the specific contribution of the structural graph prior. The strategy achieves an Information Ratio of 0.44 relative to the passive benchmark with an average holding period of 7.1 days, indicating that the model successfully identifies transient structural alpha opportunities distinct from static factor exposure (tα=1.85t\_{\alpha}=1.85). This margin is particularly notable given that the 2010–2025 test set corresponds to a historically exceptional regime of sustained asset appreciation (often termed an “Everything Bubble”), making passive risk-parity a uniquely challenging baseline to beat net of costs. Furthermore, the extended 100-seed ensemble (K=50K=50) achieves a Net Information Ratio tt-statistic of 1.93 (approximate pp-value 0.05), confirming statistical significance over this outlier passive history. The convergence between Gross (1.29) and Net (0.93) Sharpe ratios suggests that the direct optimization of transaction-adjusted returns effectively internalizes execution constraints.

##### Role of the Two Spatial Inductive Biases.

The ablation study confirms a critical interaction between the topological (Graph) and data-driven (Cross-Attention) components. Notably, neither mechanism succeeds in isolation. The *No Graph* variant (Cross-Attn Only) performs worse than the independent baseline (Net Sharpe 0.79 vs 0.83), suggesting that unconstrained attention overfits spurious correlations. Conversely, the *Graph Only* variant (Net Sharpe 0.84) offers marginal improvement, implying that static economic priors are insufficient without dynamic weighting. The full DeePM model (Net Sharpe 0.93) outperforms both. Furthermore, the ordering of these modules is significant; reversing the sequence (Graph then Cross-Attention) degrades performance to a Net Sharpe of 0.87. This supports the hypothesis that the economic graph functions best as a regularizing filter applied after the model has learned raw cross-sectional interactions, effectively “denoising” the data-driven signals and reducing Maximum Drawdown from 19.8% (flipped) to 16.0%.

##### Portfolio-Centric Supervision.

The results further highlight the superiority of portfolio-level supervision over asset-level objectives. Even the “Independent (No Structure)” ablation, which treats assets in isolation, achieves a Net Sharpe of 0.83, comfortably outperforming the “Momentum Transformer” baseline (0.66). Since both models utilize similar temporal encoders, this confirms that, with suitable optimization stability, aligning the loss function with the ultimate trading objective provides a superior optimization landscape, even in the absence of explicit cross-sectional modelling.

##### Information Latency and Causal Validity.

Comparing the “Directed Delay” protocol against the “Cascading Lag” variant reveals a preference for causal robustness over information freshness. The model utilizing strictly lagged data (t−1t-1) outperforms the variant using same-day data from earlier-closing markets (Sharpe 0.93 vs. 0.84). This finding implies that maximizing information freshness introduces non-stationary intraday noise that degrades generalization. By enforcing a strict delay, the model is compelled to learn persistent impulse response functions and transfer entropy rather than transient co-movements.

##### Optimization Stability and Addressing the Inertia Trap.

Our ablation study identifies the choice of objective function as the single most impactful component of the proposed framework, exceeding even the contribution of the graph-based architectural priors. While removing the macroeconomic graph structure degrades performance from 0.93 to 0.79 (-15%), reverting from the Robust SoftMin to a standard Pooled Sharpe objective causes a catastrophic drop to 0.68 (-27%). This hierarchy suggests that while spatial structure is beneficial, the primary challenge in financial deep learning is not merely representation learning, but optimization stability. We observed that the SoftMin loss significantly stabilized training dynamics, reducing the divergence between training and validation loss curves.

This stability is critical for complex, ratio-based objectives like the Sharpe ratio, which are prone to collapsing into degenerate local minima where the model minimizes the denominator (volatility) rather than maximizing the numerator (return). A counter-intuitive artifact of this phenomenon is that the *No SoftMin* ablation exhibits the lowest Maximum Drawdown (-13.0%). This is not a sign of robustness, but of “inertia”: without the worst-window penalty (approximating Entropic Value-at-Risk), the model retreats to a low-frequency holding pattern (18.4 days) to minimize costs, effectively becoming a slow-moving beta strategy. In contrast, the robust SoftMin objective compels the agent to trade actively (7.1 days) to defend performance during adverse regimes, accepting marginally higher volatility for vastly superior risk-adjusted returns (Sharpe 0.93).

##### Adversarial Temperature.

We further analyse the role of the adversarial temperature τ\tau, which controls the “paranoia” of the SoftMin operator (approximating EVaR). The baseline DeePM (optimized τ\tau) outperforms both the looser τ=1\tau=1 specification (Net Sharpe 0.85) and the strictly harder minimax limit τ=0.05\tau=0.05 (Net Sharpe 0.83). This confirms that a calibrated degree of robustness is required: τ=0.05\tau=0.05 approximates a hard-minimax objective that can lead to optimization instability by overfitting to the single worst historical window, while τ=1\tau=1 is closer to a simple average that fails to sufficiently penalize tail risks. The intermediate τ=0.2\tau=0.2 enables the model to focus on the tail of the distribution without discarding the signal from the body.

##### Regime Robustness and Stability.

Figure [6](https://arxiv.org/html/2601.05975v1#S7.F6 "Figure 6 ‣ Regime Robustness and Stability. ‣ 7.2 Discussion of Empirical Findings ‣ 7 Empirical Findings ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") illustrates the rolling performance stability of the DeePM Ensemble relative to classical baselines. A key deficiency of traditional trend-following (TSMOM) is its binary performance profile – it excels in sustained divergence but suffers excessively during mean-reverting or sideways markets. In contrast, DeePM demonstrates remarkable consistency across disparate regimes. By effectively navigating diverse market environments, the model proves that its learned non-linear signal processing can identify profitable opportunities even when simple persistent trends are absent, reducing the “feast-or-famine” cycle typical of systematic macro strategies.

This resilience is most distinct during the post-2020 block (Table [2](https://arxiv.org/html/2601.05975v1#S7.T2 "Table 2 ‣ 7.1 Results ‣ 7 Empirical Findings ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")), where the model delivered sustained alpha despite the transition from pandemic-induced volatility to inflationary rate shocks. While classical Trend strategies faltered (Sharpe 0.38) and passive allocation struggled (Sharpe 0.37) during this period, the DeePM framework maintained a Net Sharpe of 0.79 (0.97 with MACD features), suggesting the learned representations successfully generalized from the low-rate training era to the new high-rate regime without requiring retraining.

![Refer to caption](images/annual_sharpe_comparison.png)


Figure 6: Rolling 12-month Sharpe Ratio of DeePM versus the TSMOM baseline. The proposed model exhibits superior stability, maintaining positive performance during periods where classical trend-following suffers significant drawdowns (e.g., 2016, post-2020).

##### Cost-Aware Learning.

The results validate the necessity of end-to-end cost optimization. The convergence between Gross (1.29) and Net (0.93) Sharpe ratios suggests that the direct optimization of transaction-adjusted returns effectively internalizes execution constraints. Training with *Zero Cost* (γ=0\gamma=0) leads to over-trading (Hold 4.9 days) and a collapse in Net Sharpe to 0.56; without a penalty, the model aggressively fits high-frequency noise that appears profitable in frictionless theory but is illusory in practice. This sensitivity is markedly more acute here than in univariate frameworks like the Momentum Transformer. In a portfolio context, a zero-cost objective encourages the model to exploit spurious cross-sectional arbitrages (e.g., long Asset A vs. short Asset B based on transient noise), creating a much larger surface area for unmonetizable turnover than simple directional trend following. Conversely, *Full Cost* training (γ=1\gamma=1) results in an overly conservative policy (Hold 19.0 days, Sharpe 0.70). The optimal performance (Sharpe 0.93) is achieved with an intermediate penalty, confirming theoretical predictions that ensembling provides implicit regularization, allowing the explicit penalty to be relaxed to capture higher-frequency alpha.

##### Limitations of Two-Stage Mean-Variance Frameworks.

The comparison with MVO baselines highlights the advantages of an end-to-end approach over separated estimation and optimization. The standard two-stage MVO fails catastrophically (Sharpe -0.07) due to error maximization, where estimation noise in the covariance matrix is amplified by the optimizer. While introducing a quadratic turnover penalty (MVO-TP) stabilizes the strategy and restores positive performance (Sharpe 0.47), it remains significantly inferior to the deep learning approach. This suggests that the performance gap is not merely a function of turnover management, but stems from DeePM’s ability to learn non-linear predictive signals that two-stage linear models cannot capture.

##### Ensembling as Structural Regularization.

The results confirm that ensembling acts as an effective variance reduction technique for portfolio construction. The ensemble model improves the Net Sharpe ratio from 0.72 (single best seed) to 0.93 (Top 10 seeds). Crucially, performance remains remarkably stable beyond this initial uplift: the Baseline (K=25K=25), Top 10 (K=10K=10), and the extended 100-seed ensemble (K=50K=50) all converge to a Net Sharpe of approximately 0.93. This insensitivity indicates that the specific ensemble size is not a cherry-picked hyperparameter, provided a sufficient diversity of models is aggregated. By averaging over multiple initializations, the ensemble mitigates the idiosyncrasies of individual training runs, resulting in a smoother position path that is more efficient to execute and stable during drawdowns.

## 8 Conclusions and Future Work

This paper introduces DeePM, an end-to-end portfolio management framework that integrates macroeconomic structural priors with deep representation learning. Our empirical results demonstrate that imposing a static sector-graph structure acts as a vital regularizer, enabling the model to learn robust cross-sectional alpha that generalizes out-of-sample (Net Sharpe 0.93) where purely data-driven attention mechanisms fail (Net Sharpe 0.79). Furthermore, we show that the choice of loss function is paramount; the robust SoftMin (EVaR) objective significantly outperforms standard mean-variance and pooled objectives by preventing overfitting to low-volatility regimes and avoiding the “inertia trap.” Beyond architectural novelty, this work bridges the gap between academic deep learning and institutional practice. By rigorously modelling transaction costs, enforcing filtration-compliant delays for asynchronous global markets, and optimizing for regime-robust metrics rather than average-case performance, DeePM offers a deployable blueprint for systematic macro managers seeking to modernize legacy trend-following systems.

Future research will focus on five directions: (1) Dynamic Graph Learning, allowing the adjacency matrix to evolve over time rather than relying on fixed sector definitions; (2) Interpretability, leveraging GNN explainability techniques to map learned attention weights back to specific economic transmission channels; (3) Hierarchical Structure, extending the graph prior to explicitly model multi-level relationships across assets, sectors, and asset classes; (4) Expanded Information Sets, integrating carry and macroeconomic data to capture drivers orthogonal to pure price momentum; (5) Freshness vs. Causality, benchmarking against a fully synchronous data source to rigorously test whether the “Causal Sieve” benefit of the Directed Delay protocol outweighs the informational cost of sacrificing “instantaneous” data freshness; and (6) High-Frequency Generalization, extending the framework to intraday data to test whether the proposed inductive biases persist at higher frequencies, and determining the time-scale at which the trade-off between information freshness and causal validity inverts.

## 9 Acknowledgements

KW would like to thank the Oxford-Man Institute of Quantitative Finance for its generous support.
SR would like to thank the U.K. Royal Academy of Engineering.

## References

* A. Ahmadi-Javid (2012)
  Entropic value-at-risk: a new coherent risk measure.
  Journal of Optimization Theory and Applications 155 (3),  pp. 1105–1123.
  Cited by: [item (iii)](https://arxiv.org/html/2601.05975v1#S1.I1.ix3.p1.1 "In 1.1 Decision Problem and Implementation Constraints ‣ 1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§1.2](https://arxiv.org/html/2601.05975v1#S1.SS2.p1.2 "1.2 Our Approach: Structured Deep Portfolio Management ‣ 1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§2.5](https://arxiv.org/html/2601.05975v1#S2.SS5.p1.2 "2.5 Robust Objectives and Risk Measures ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§5.1](https://arxiv.org/html/2601.05975v1#S5.SS1.SSS0.Px2.p1.3 "2. SoftMin as an Adversarial Prior. ‣ 5.1 Robust Objective: Pooled Sharpe with SoftMin Penalty ‣ 5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* G. Appel (1979)
  The moving average convergence–divergence trading method.
   Advanced Commodity Trading Techniques, New York.
  Cited by: [§3.3](https://arxiv.org/html/2601.05975v1#S3.SS3.SSS0.Px3.p1.1 "2. MACD Trend Filters. ‣ 3.3 Features and Preprocessing ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* T. Bachlechner, B. P. Majumder, H. Mao, G. Cottrell, and J. McAuley (2021)
  ReZero is all you need: fast convergence at large depth.
  In Proceedings of the Thirty-Seventh Conference on Uncertainty in Artificial Intelligence,
  Proceedings of Machine Learning Research, Vol. 161,  pp. 1352–1361.
  External Links: [Link](https://proceedings.mlr.press/v161/bachlechner21a.html)
  Cited by: [§4.3](https://arxiv.org/html/2601.05975v1#S4.SS3.p2.2 "4.3 Cross-Sectional Interaction: Filtration-Compliant Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* D. H. Bailey, J. M. Borwein, M. López de Prado, and Q. J. Zhu (2016)
  The probability of backtest overfitting.
  Journal of Computational Finance.
  External Links: [Document](https://dx.doi.org/10.21314/JCF.2016.318)
  Cited by: [item (i)](https://arxiv.org/html/2601.05975v1#S1.I1.ix1.p1.1 "In 1.1 Decision Problem and Implementation Constraints ‣ 1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* L. Barnett, A. B. Barrett, and A. K. Seth (2009)
  Granger causality and transfer entropy are equivalent for gaussian variables.
  Physical Review Letters 103 (23),  pp. 238701.
  External Links: [Document](https://dx.doi.org/10.1103/PhysRevLett.103.238701),
  [Link](https://link.aps.org/doi/10.1103/PhysRevLett.103.238701)
  Cited by: [footnote 2](https://arxiv.org/html/2601.05975v1#footnote2 "In Directed Delay as Information-Theoretic Filtering. ‣ 4.5 Theoretical Interpretations ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* J. Baz, N. Granger, C. R. Harvey, N. Le Roux, and S. Rattray (2015)
  Dissecting investment strategies in the cross section and time series.
  Working Paper
   SSRN.
  Note: Man Group / Man AHL working paper (SSRN 2695101)
  External Links: [Document](https://dx.doi.org/10.2139/ssrn.2695101)
  Cited by: [2nd item](https://arxiv.org/html/2601.05975v1#S6.I2.i2.p1.2 "In 6.1.2 Classical Trend-Following ‣ 6.1 Benchmarks ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* J. Bollinger (2002)
  Bollinger on bollinger bands.
   McGraw-Hill New York.
  Cited by: [§3.3](https://arxiv.org/html/2601.05975v1#S3.SS3.SSS0.Px4.p1.2 "3. Mean-Reversion ‣ 3.3 Features and Preprocessing ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* S. Boucheron, G. Lugosi, and P. Massart (2013)
  Concentration inequalities: a nonasymptotic theory of independence.
   Oxford University Press.
  Cited by: [§D.1](https://arxiv.org/html/2601.05975v1#A4.SS1.1.p1.5 "Proof. ‣ D.1 SoftMin as KL-penalized DRO (Variational Form) ‣ Appendix D Analysis of the Robust Objective ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* F. R. K. Chung (1997)
  Spectral graph theory.
  CBMS Regional Conference Series in Mathematics, Vol. 92, American Mathematical Society.
  Cited by: [§4.5](https://arxiv.org/html/2601.05975v1#S4.SS5.SSS0.Px2.p1.3 "Graph Layer as a Bayesian Structural Prior. ‣ 4.5 Theoretical Interpretations ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* K. Daniel and T. J. Moskowitz (2016)
  Momentum crashes.
  Journal of Financial Economics 122 (2),  pp. 221–247.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2015.12.002)
  Cited by: [§5](https://arxiv.org/html/2601.05975v1#S5.p1.3 "5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* W. F. De Bondt and R. Thaler (1985)
  Does the stock market overreact?.
  The Journal of Finance 40 (3),  pp. 793–805.
  Cited by: [§2.1](https://arxiv.org/html/2601.05975v1#S2.SS1.p1.1 "2.1 Deep Learning for Systematic Trend ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* A. N. Elmachtoub and P. Grigas (2022)
  Smart “predict, then optimize”.
  Management Science 68 (1),  pp. 9–26.
  External Links: [Document](https://dx.doi.org/10.1287/mnsc.2020.3922)
  Cited by: [§1](https://arxiv.org/html/2601.05975v1#S1.p1.1 "1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* C. W. J. Granger (1969)
  Investigating causal relations by econometric models and cross-spectral methods.
  Econometrica 37 (3),  pp. 424–438.
  Cited by: [§4.5](https://arxiv.org/html/2601.05975v1#S4.SS5.SSS0.Px3.p2.5 "Directed Delay as Information-Theoretic Filtering. ‣ 4.5 Theoretical Interpretations ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* S. Gu, B. Kelly, and D. Xiu (2020)
  Empirical asset pricing via machine learning.
  The Review of Financial Studies 33 (5),  pp. 2223–2273.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hhaa009)
  Cited by: [§1](https://arxiv.org/html/2601.05975v1#S1.p1.1 "1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* L. Harris (2003)
  Trading and exchanges: market microstructure for practitioners.
   Oxford University Press.
  External Links: ISBN 9780195144703
  Cited by: [§3.5](https://arxiv.org/html/2601.05975v1#S3.SS5.p1.1 "3.5 Philosophy of the Transaction Cost Model ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* C. R. Harvey, E. Hoyle, R. Korgaonkar, S. Rattray, M. Sargaison, and O. Van Hemert (2018)
  The impact of volatility targeting.
  The Journal of Portfolio Management 45 (1),  pp. 14–33.
  External Links: [Document](https://dx.doi.org/10.3905/jpm.2018.45.1.014)
  Cited by: [§3.2](https://arxiv.org/html/2601.05975v1#S3.SS2.p1.4 "3.2 Portfolio Returns and Frictions ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* C. R. Harvey and A. Siddique (2000)
  Conditional skewness in asset pricing tests.
  The Journal of Finance 55 (3),  pp. 1263–1295.
  Cited by: [§3.3](https://arxiv.org/html/2601.05975v1#S3.SS3.SSS0.Px4.p1.2 "3. Mean-Reversion ‣ 3.3 Features and Preprocessing ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* K. He, X. Zhang, S. Ren, and J. Sun (2016)
  Deep residual learning for image recognition.
  In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition,
   pp. 770–778.
  External Links: [Link](https://arxiv.org/abs/1512.03385)
  Cited by: [§4.2](https://arxiv.org/html/2601.05975v1#S4.SS2.SSS0.Px3.p2.6 "3. Temporal Attention with Adapter. ‣ 4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* S. Hochreiter and J. Schmidhuber (1997)
  Long short-term memory.
  Neural computation 9 (8),  pp. 1735–1780.
  Cited by: [item 1](https://arxiv.org/html/2601.05975v1#S1.I2.i1.p1.1 "In 1.2 Our Approach: Structured Deep Portfolio Management ‣ 1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* N. Jegadeesh and S. Titman (1993)
  Returns to buying winners and selling losers: implications for stock market efficiency.
  The Journal of Finance 48 (1),  pp. 65–91.
  Cited by: [§2.1](https://arxiv.org/html/2601.05975v1#S2.SS1.p1.1 "2.1 Deep Learning for Systematic Trend ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* T. N. Kipf and M. Welling (2017)
  Semi-supervised classification with graph convolutional networks.
  In International Conference on Learning Representations (ICLR),
  External Links: 1609.02907
  Cited by: [§2.4](https://arxiv.org/html/2601.05975v1#S2.SS4.p2.3 "2.4 Graph Priors and Economic Structure ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§4.4](https://arxiv.org/html/2601.05975v1#S4.SS4.SSS0.Px1.p2.4 "Structure and Edge Biases. ‣ 4.4 Structural Regularization: Macro Graph Prior ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* A. S. Kyle (1985)
  Continuous auctions and insider trading.
  Econometrica 53 (6),  pp. 1315–1335.
  Cited by: [§3.5](https://arxiv.org/html/2601.05975v1#S3.SS5.p1.1 "3.5 Philosophy of the Transaction Cost Model ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* B. Lakshminarayanan, A. Pritzel, and C. Blundell (2017)
  Simple and scalable predictive uncertainty estimation using deep ensembles.
  In Advances in Neural Information Processing Systems,
  Vol. 30,  pp. 6402–6413.
  Cited by: [§5.2](https://arxiv.org/html/2601.05975v1#S5.SS2.p1.1 "5.2 Ensembling and Implicit Cost Regularization ‣ 5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* O. Ledoit and M. Wolf (2004)
  A well-conditioned estimator for large-dimensional covariance matrices.
  Journal of Multivariate Analysis 88 (2),  pp. 365–411.
  External Links: [Document](https://dx.doi.org/10.1016/S0047-259X%2803%2900096-4)
  Cited by: [2nd item](https://arxiv.org/html/2601.05975v1#S6.I3.i2.p1.5 "In 6.1.3 Two-Stage Signal–Allocation Baselines ‣ 6.1 Benchmarks ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§6.1](https://arxiv.org/html/2601.05975v1#S6.SS1.p2.2 "6.1 Benchmarks ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* J. Lee, Y. Lee, J. Kim, A. Kosiorek, S. Choi, and Y. W. Teh (2019)
  Set transformer: a framework for attention-based permutation-invariant neural networks.
  In International Conference on Machine Learning,
  Cited by: [§2.3](https://arxiv.org/html/2601.05975v1#S2.SS3.p2.3 "2.3 Cross-Sectional Modeling with Attention and Representation Learning ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* B. Lim, S. Ö. Arık, N. Loeff, and T. Pfister (2021)
  Temporal fusion transformers for interpretable multi-horizon time series forecasting.
  International Journal of Forecasting 37 (4),  pp. 1748–1764.
  Cited by: [§4.2](https://arxiv.org/html/2601.05975v1#S4.SS2.SSS0.Px1.p1.1 "1. Vectorized Variable Selection Network (V-VSN). ‣ 4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§4.2](https://arxiv.org/html/2601.05975v1#S4.SS2.SSS0.Px3.p1.1 "3. Temporal Attention with Adapter. ‣ 4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* B. Lim, S. Zohren, and S. Roberts (2019)
  Enhancing time-series momentum strategies using deep neural networks.
  The Journal of Financial Data Science 1 (4),  pp. 19–38.
  External Links: [Document](https://dx.doi.org/10.3905/jfds.2019.1.015)
  Cited by: [§2.1](https://arxiv.org/html/2601.05975v1#S2.SS1.p2.1 "2.1 Deep Learning for Systematic Trend ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§3.3](https://arxiv.org/html/2601.05975v1#S3.SS3.SSS0.Px5.p1.9 "4. Robust Outlier Control. ‣ 3.3 Features and Preprocessing ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [2nd item](https://arxiv.org/html/2601.05975v1#S6.I2.i2.p1.2 "In 6.1.2 Classical Trend-Following ‣ 6.1 Benchmarks ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§6.4](https://arxiv.org/html/2601.05975v1#S6.SS4.p3.1 "6.4 Training Protocol and Data Splits ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* A. W. Lo and A. C. MacKinlay (1990)
  An econometric analysis of nonsynchronous trading.
  Journal of Econometrics 45 (1-2),  pp. 181–211.
  External Links: [Document](https://dx.doi.org/10.1016/0304-4076%2890%2990098-E)
  Cited by: [item (i)](https://arxiv.org/html/2601.05975v1#S1.I1.ix1.p1.1 "In 1.1 Decision Problem and Implementation Constraints ‣ 1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* A. W. Lo (2002)
  The statistics of sharpe ratios.
  Financial Analysts Journal 58 (4),  pp. 36–52.
  Cited by: [§5.1](https://arxiv.org/html/2601.05975v1#S5.SS1.SSS0.Px1.p2.8 "1. Pooled Sharpe Ratio. ‣ 5.1 Robust Objective: Pooled Sharpe with SoftMin Penalty ‣ 5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* I. Loshchilov and F. Hutter (2019)
  Decoupled weight decay regularization.
  International Conference on Learning Representations (ICLR).
  External Links: 1711.05101
  Cited by: [§E.1](https://arxiv.org/html/2601.05975v1#A5.SS1.p1.1 "E.1 Optimization and Training Dynamics ‣ Appendix E Experimental Implementation Details ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* M. Magdon-Ismail, A. F. Atiya, A. Pratap, and Y. S. Abu-Mostafa (2004)
  On the maximum drawdown of a brownian motion.
  Journal of Risk 7 (2),  pp. 1–15.
  Cited by: [3rd item](https://arxiv.org/html/2601.05975v1#S6.I5.i3.p1.1 "In Performance and Risk. ‣ 6.3 Evaluation Metrics ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* S. Maillard, T. Roncalli, and J. Teiletche (2010)
  The properties of equally weighted risk contribution portfolios.
  The Journal of Portfolio Management 36 (4),  pp. 60–70.
  External Links: [Document](https://dx.doi.org/10.3905/jpm.2010.36.4.060)
  Cited by: [3rd item](https://arxiv.org/html/2601.05975v1#S6.I3.i3.p1.6 "In 6.1.3 Two-Stage Signal–Allocation Baselines ‣ 6.1 Benchmarks ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* H. Markowitz (1952)
  Portfolio selection.
  The Journal of Finance 7 (1),  pp. 77–91.
  Cited by: [§1](https://arxiv.org/html/2601.05975v1#S1.p1.1 "1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* R. O. Michaud (1989)
  The markowitz optimization enigma: is “optimized” optimal?.
  Financial Analysts Journal 45 (1),  pp. 31–42.
  External Links: [Document](https://dx.doi.org/10.2469/faj.v45.n1.31)
  Cited by: [§1](https://arxiv.org/html/2601.05975v1#S1.p1.1 "1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§2.2](https://arxiv.org/html/2601.05975v1#S2.SS2.p1.6 "2.2 Machine Learning for Portfolio Construction under Frictions ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* T. J. Moskowitz, Y. H. Ooi, and L. H. Pedersen (2012)
  Time series momentum.
  Journal of Financial Economics 104 (2),  pp. 228–250.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2011.11.003)
  Cited by: [§2.1](https://arxiv.org/html/2601.05975v1#S2.SS1.p1.1 "2.1 Deep Learning for Systematic Trend ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§2.1](https://arxiv.org/html/2601.05975v1#S2.SS1.p2.1 "2.1 Deep Learning for Systematic Trend ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§3.2](https://arxiv.org/html/2601.05975v1#S3.SS2.p1.4 "3.2 Portfolio Returns and Frictions ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§3.3](https://arxiv.org/html/2601.05975v1#S3.SS3.SSS0.Px2.p1.1 "1. Volatility-Normalized Returns. ‣ 3.3 Features and Preprocessing ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [1st item](https://arxiv.org/html/2601.05975v1#S6.I2.i1.p1.1 "In 6.1.2 Classical Trend-Following ‣ 6.1 Benchmarks ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* W. K. Newey and K. D. West (1987)
  A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix.
  Econometrica 55 (3),  pp. 703–708.
  Cited by: [5th item](https://arxiv.org/html/2601.05975v1#S6.I5.i5.p1.4 "In Performance and Risk. ‣ 6.3 Evaluation Metrics ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* Y. Nie, N. H. Nguyen, P. Sinthong, and J. Kalagnanam (2023)
  A time series is worth 64 words: long-term forecasting with transformers.
  arXiv preprint arXiv:2211.14730.
  Note: Accepted at ICLR 2023
  External Links: [Document](https://dx.doi.org/10.48550/arXiv.2211.14730)
  Cited by: [§4.2](https://arxiv.org/html/2601.05975v1#S4.SS2.p1.1 "4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* E. Perez, F. Strub, H. de Vries, V. Dumoulin, and A. Courville (2018)
  FiLM: visual reasoning with a general conditioning layer.
  In AAAI Conference on Artificial Intelligence (AAAI),
  Note: arXiv:1709.07871
  Cited by: [§4.2](https://arxiv.org/html/2601.05975v1#S4.SS2.SSS0.Px1.p2.6 "1. Vectorized Variable Selection Network (V-VSN). ‣ 4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* Pinnacle Data Corporation (2025)
  CLC database (continuous futures contracts).
  Note: Proprietary financial databaseAccessed via Pinnacle Data Corp.
  External Links: [Link](https://pinnacledata2.com/clc.html)
  Cited by: [§A.1](https://arxiv.org/html/2601.05975v1#A1.SS1.p1.1 "A.1 Data Provenance and Processing ‣ Appendix A Universe Specifications and Methodology ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* R. T. Rockafellar and S. Uryasev (2000)
  Optimization of conditional value-at-risk.
  Journal of Risk 2 (3),  pp. 21–41.
  Cited by: [item (iii)](https://arxiv.org/html/2601.05975v1#S1.I1.ix3.p1.1 "In 1.1 Decision Problem and Implementation Constraints ‣ 1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§2.5](https://arxiv.org/html/2601.05975v1#S2.SS5.p1.1 "2.5 Robust Objectives and Risk Measures ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* H. Rue and L. Held (2005)
  Gaussian markov random fields: theory and applications.
   Chapman and Hall/CRC.
  Cited by: [§4.5](https://arxiv.org/html/2601.05975v1#S4.SS5.SSS0.Px2.p1.3 "Graph Layer as a Bayesian Structural Prior. ‣ 4.5 Theoretical Interpretations ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* T. Sauer, J. A. Yorke, and M. Casdagli (1991)
  Embedology.
  Journal of Statistical Physics 65 (3-4),  pp. 579–616.
  Cited by: [§4.5](https://arxiv.org/html/2601.05975v1#S4.SS5.SSS0.Px1.p1.3 "Temporal Encoder as State Space Reconstruction. ‣ 4.5 Theoretical Interpretations ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* T. Schreiber (2000)
  Measuring information transfer.
  Physical Review Letters 85 (2),  pp. 461–464.
  External Links: [Document](https://dx.doi.org/10.1103/PhysRevLett.85.461)
  Cited by: [§4.5](https://arxiv.org/html/2601.05975v1#S4.SS5.SSS0.Px3.p2.5 "Directed Delay as Information-Theoretic Filtering. ‣ 4.5 Theoretical Interpretations ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* W. F. Sharpe (1966)
  Mutual fund performance.
  The Journal of Business 39 (1),  pp. 119–138.
  Cited by: [item (iii)](https://arxiv.org/html/2601.05975v1#S1.I1.ix3.p1.1 "In 1.1 Decision Problem and Implementation Constraints ‣ 1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§5](https://arxiv.org/html/2601.05975v1#S5.p2.1 "5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [1st item](https://arxiv.org/html/2601.05975v1#S6.I5.i1.p1.1 "In Performance and Risk. ‣ 6.3 Evaluation Metrics ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* N. Shazeer (2020)
  GLU variants improve transformer.
  arXiv preprint.
  Note: arXiv:2002.05202
  Cited by: [§4.2](https://arxiv.org/html/2601.05975v1#S4.SS2.SSS0.Px3.p2.1 "3. Temporal Attention with Adapter. ‣ 4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§4.2](https://arxiv.org/html/2601.05975v1#S4.SS2.SSS0.Px3.p2.6 "3. Temporal Attention with Adapter. ‣ 4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov (2014)
  Dropout: a simple way to prevent neural networks from overfitting.
  The journal of machine learning research 15 (1),  pp. 1929–1958.
  Cited by: [§4.2](https://arxiv.org/html/2601.05975v1#S4.SS2.SSS0.Px3.p2.6 "3. Temporal Attention with Adapter. ‣ 4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* F. Takens (1981)
  Detecting strange attractors in turbulence.
  In Dynamical Systems and Turbulence, Warwick 1980,
  Lecture Notes in Mathematics, Vol. 898,  pp. 366–381.
  Cited by: [§4.5](https://arxiv.org/html/2601.05975v1#S4.SS5.SSS0.Px1.p1.3 "Temporal Encoder as State Space Reconstruction. ‣ 4.5 Theoretical Interpretations ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* P. Veličković, G. Cucurull, A. Casanova, A. Romero, P. Liò, and Y. Bengio (2018)
  Graph attention networks.
  In International Conference on Learning Representations (ICLR),
  External Links: 1710.10903
  Cited by: [§2.4](https://arxiv.org/html/2601.05975v1#S2.SS4.p3.2 "2.4 Graph Priors and Economic Structure ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* K. Wood, S. Giegerich, S. Roberts, and S. Zohren (2023)
  Note: Risk.net (Cutting Edge)
  External Links: [Link](https://www.risk.net/cutting-edge/7956074/trading-with-the-momentum-transformer-an-interpretable-deep-learning-architecture)
  Cited by: [item 1](https://arxiv.org/html/2601.05975v1#S1.I2.i1.p1.1 "In 1.2 Our Approach: Structured Deep Portfolio Management ‣ 1 Introduction ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§2.1](https://arxiv.org/html/2601.05975v1#S2.SS1.p2.1 "2.1 Deep Learning for Systematic Trend ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§3.3](https://arxiv.org/html/2601.05975v1#S3.SS3.SSS0.Px5.p1.9 "4. Robust Outlier Control. ‣ 3.3 Features and Preprocessing ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§4.2](https://arxiv.org/html/2601.05975v1#S4.SS2.p1.1 "4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [1st item](https://arxiv.org/html/2601.05975v1#S6.I4.i1.p1.1 "In 6.1.4 Learning-Based Baselines ‣ 6.1 Benchmarks ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* K. Wood, S. Kessler, S. J. Roberts, and S. Zohren (2024)
  Few-shot learning patterns in financial time series for trend-following strategies.
  Journal of Financial Data Science 6 (2),  pp. 88–115.
  External Links: [Document](https://dx.doi.org/10.3905/jfds.2024.1.157)
  Cited by: [§2.3](https://arxiv.org/html/2601.05975v1#S2.SS3.p4.1 "2.3 Cross-Sectional Modeling with Attention and Representation Learning ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§6.4](https://arxiv.org/html/2601.05975v1#S6.SS4.p3.1 "6.4 Training Protocol and Data Splits ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* K. Wood, S. Roberts, and S. Zohren (2022)
  Slow momentum with fast reversion: a trading strategy using deep learning and changepoint detection.
  The Journal of Financial Data Science 4 (1),  pp. 111–129.
  External Links: [Document](https://dx.doi.org/10.3905/jfds.2021.1.081),
  ISSN 2640-3943,
  [Link](https://jfds.pm-research.com/content/4/1/111)
  Cited by: [§2.1](https://arxiv.org/html/2601.05975v1#S2.SS1.p2.1 "2.1 Deep Learning for Systematic Trend ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"),
  [§5](https://arxiv.org/html/2601.05975v1#S5.p1.3 "5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* R. Xiong, Y. Yang, D. He, K. Zheng, S. Zheng, C. Xing, H. Zhang, Y. Lan, L. Wang, and T. Liu (2020)
  On layer normalization in the transformer architecture.
  In Proceedings of the 37th International Conference on Machine Learning (ICML),
   pp. 10524–10533.
  External Links: [Link](http://proceedings.mlr.press/v119/xiong20b.html)
  Cited by: [§4.2](https://arxiv.org/html/2601.05975v1#S4.SS2.SSS0.Px3.p2.6 "3. Temporal Attention with Adapter. ‣ 4.2 Temporal Backbone: Hybrid VSN-LSTM-Attention ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* C. Ying, T. Cai, S. Luo, S. Zheng, G. Ke, D. He, Y. Shen, and T. Liu (2021)
  Do transformers really perform bad for graph representation?.
  In Advances in Neural Information Processing Systems,
  Vol. 34,  pp. 28877–28888.
  External Links: [Link](https://proceedings.neurips.cc/paper/2021/hash/f1c1592588411002af340cbaedd6fc33-Abstract.html)
  Cited by: [§4.4](https://arxiv.org/html/2601.05975v1#S4.SS4.SSS0.Px1.p1.1 "Structure and Edge Biases. ‣ 4.4 Structural Regularization: Macro Graph Prior ‣ 4 Method: DeePM Architecture ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* T. W. Young (1991)
  Calmar ratio: a smoother tool.
  Futures.
  Note: Trade magazine article introducing the Calmar ratio
  Cited by: [4th item](https://arxiv.org/html/2601.05975v1#S6.I5.i4.p1.1 "In Performance and Risk. ‣ 6.3 Evaluation Metrics ‣ 6 Experimental Design ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* M. Zaheer, S. Kottur, S. Ravanbakhsh, B. Póczos, R. Salakhutdinov, and A. J. Smola (2017)
  Deep sets.
  In Advances in Neural Information Processing Systems,
  External Links: [Link](https://papers.nips.cc/paper/6931-deep-sets)
  Cited by: [§2.3](https://arxiv.org/html/2601.05975v1#S2.SS3.p2.3 "2.3 Cross-Sectional Modeling with Attention and Representation Learning ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* Z. Zhang, S. Zohren, and S. Roberts (2020)
  Deep learning for portfolio optimization.
  The Journal of Financial Data Science 2 (4),  pp. 8–20.
  External Links: [Document](https://dx.doi.org/10.3905/jfds.2020.1.042)
  Cited by: [§2.2](https://arxiv.org/html/2601.05975v1#S2.SS2.p2.1 "2.2 Machine Learning for Portfolio Construction under Frictions ‣ 2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").
* Z. Zhang and S. Zohren (2025)
  Deep learning in quantitative trading.
  Elements in Quantitative Finance.
  Cited by: [§2](https://arxiv.org/html/2601.05975v1#S2.p1.1 "2 Related Literature ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management").

## Appendix A Universe Specifications and Methodology

This appendix details the investment universe, the macroeconomic graph topology used for structural regularization, and the transaction cost models applied during backtesting.

### A.1 Data Provenance and Processing

We source historical daily open, high, low, and close (OHLC) prices for all 50 futures and FX contracts from the Pinnacle Data Corp CLC Database [Pinnacle Data Corporation, [2025](https://arxiv.org/html/2601.05975v1#bib.bib81 "CLC database (continuous futures contracts)")]; however, for all experiments we just use close to construct features. To construct continuous return series from individual contract expirations, we utilize ratio-adjusted (“Panama”) continuous contracts.

Unlike additive adjustment methods, which shift historical prices by a fixed absolute amount and can lead to negative prices or distorted percentage returns over long horizons, ratio adjustment scales historical prices by the ratio of the new contract price to the old contract price at each roll date. This methodology rigorously preserves the relative percentage returns and volatility structure of the asset series, ensuring that the inputs to the volatility-scaling mechanism (Section 3.2) and the training returns for the network faithfully represent the realized distribution of market returns.

### A.2 Macro Graph Topology

The macroeconomic prior graph 𝒢=(𝒱,ℰ)\mathcal{G}=(\mathcal{V},\mathcal{E}) is constructed deterministically based on economic first principles. The adjacency matrix AA is formed via the union of the following edge sets:

1. 1.

   Intra-Group Cliques (Sectoral Homophily): All nodes within a specific Macro Group (e.g., COMM\_ENERGY) are fully connected, enforcing the view that assets within a sub-sector share a single latent factor.
2. 2.

   Risk-On Channel: Connects Global Equities ↔\leftrightarrow Base Metals ↔\leftrightarrow Risk FX (AUD, CAD, MXN).
3. 3.

   Inflation Channel: Connects Energy ↔\leftrightarrow US Treasuries ↔\leftrightarrow Precious Metals.
4. 4.

   Safe Haven Flows: Connects US Treasuries ↔\leftrightarrow Safe FX (JPY, CHF) ↔\leftrightarrow Precious Metals.
5. 5.

   Commodity Exporters: Connects Energy/Metals to their respective currency proxies (e.g., Oil ↔\leftrightarrow CAD/MXN, Metals ↔\leftrightarrow AUD).
6. 6.

   Regional Integration: Creates a triangular linkage between the primary Equity index, Sovereign Bond, and Currency for major economic zones (US, EU, JP, UK, CA).

### A.3 Transaction Cost Methodology

We implement a *Structural Minimum Cost Model* that synthesizes the “Tick Size Constraint" theory (Harris, 2003) with market impact estimates. The cost cic\_{i} (in basis points) is derived as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ci≈max⁡(Cfloor,Cstruct,i×λi)c\_{i}\approx\max(C\_{\text{floor}},\;C\_{\text{struct},i}\times\lambda\_{i}) |  | (48) |

where CstructC\_{\text{struct}} is the theoretical cost implied by the minimum price variation (tick size) relative to the contract value, and λi≥1.0\lambda\_{i}\geq 1.0 is a liquidity scalar.

#### A.3.1 Justification of Liquidity Scalars (λi\lambda\_{i})

While liquid electronic markets (e.g., S&P 500, US Treasuries) typically trade near their structural tick constraints (λi≈1.0−1.5\lambda\_{i}\approx 1.0-1.5), we apply significant scalers to subsets of the universe to reflect institutional execution realities that simple tick-based models miss.

The “Roach Motel" Effect (Depth vs. Spread).
Certain markets, such as Palladium (PA) or specific Softs, may exhibit tight top-of-book spreads that mask a lack of order book depth. For institutional-size execution, the “effective spread" to sweep the book is significantly wider than the quoted spread. We model this via high “Structure" scalars (e.g., Palladium λi≈2.4\lambda\_{i}\approx 2.4, Orange Juice λi≈12.6\lambda\_{i}\approx 12.6) to penalize strategies that assume they can exit large positions at the touch price during stress periods.

Volatility-Constrained Market Making.
For assets like Natural Gas or Livestock (Feeder Cattle), the exchange-mandated tick size is often non-binding. Market makers widen spreads to compensate for extreme inventory volatility. In these regimes, the cost is driven by volatility rather than quantization noise. We apply scalars (λi>2.0\lambda\_{i}>2.0) to align the modeled cost with the realized volatility-adjusted spreads observed in 2023-2024.

Regional Session Impacts.
Assets such as the Nikkei 225 often show adequate liquidity during their local session but suffer from “air pockets" during the US/EU overlap when global macro rebalancing occurs. We apply an “Impact" scalar (λi≈2.0−2.3\lambda\_{i}\approx 2.0-2.3) to represent the higher slippage associated with trading these assets out of their primary liquidity window.

High-Velocity and Arbitrage Discounts (λi<1.0\lambda\_{i}<1.0).
Conversely, certain highly efficient markets (e.g., Hang Seng, Dollar Index, FTSE 100) are assigned scalars below unity. In these cases, the exchange-mandated tick size (CstructC\_{\text{struct}}) acts as a legacy constraint that overestimates the effective cost for institutional participants. Deep spot-futures arbitrage links (e.g., between the Dollar Index future and the underlying spot FX basket) allow market makers to quote aggressive effective spreads, often facilitating execution better than the naked tick implies via block liquidity or EFP (Exchange for Physical) mechanisms.

#### A.3.2 Cost Summary Statistics

Table [3](https://arxiv.org/html/2601.05975v1#A1.T3 "Table 3 ‣ A.3.2 Cost Summary Statistics ‣ A.3 Transaction Cost Methodology ‣ Appendix A Universe Specifications and Methodology ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") summarizes the resulting cost distribution. The divergence between “Median Calc" and the “Final Band" in the high-cost tiers reflects the necessity of the λi\lambda\_{i} scalars.

Table 3: Transaction Cost Regimes: Theoretical vs. Modeled

| Final Band | Median Cs​t​r​u​c​tC\_{struct} | Mean Cs​t​r​u​c​tC\_{struct} | Mean λi\lambda\_{i} | Typical Asset Class |
| --- | --- | --- | --- | --- |
| 0.25 bps | 0.19 | 0.19 | 1.6x | Ultra-Liquid (S&P 500, US Treasuries) |
| 0.50 bps | 0.40 | 0.43 | 1.5x | Very Liquid (Bund, JPY, FTSE) |
| 0.75 bps | 0.71 | 0.81 | 1.1x | Liquid Physicals (Crude, 10Y Note) |
| 1.00 bps | 1.02 | 0.96 | 1.1x | Standard (Silver, EuroStoxx) |
| 1.50 bps | 1.30 | 1.02 | 1.6x | Mid-Liquidity (30Y Bond, Platinum) |
| 2.50 bps | 1.67 | 1.60 | 1.9x | High Cost (Grains, Nat Gas, Livestock) |
| 6.00 bps | 1.75\* | 1.75\* | 4.2x | Volatile / Thin (Palladium, Cocoa) |
| 15.0 bps | 1.19\* | 1.19\* | 12.6x | Distressed (Orange Juice) |

\*Note: For high-cost bands, the divergence between “Median Calc" and the Final Band reflects the high Liquidity Scalar required for volatile markets.

### A.4 Master Data Universe

Table LABEL:tab:master\_universe provides the granular derivation of costs for the full 50-asset universe.

* •

  Calc: The theoretical cost based on Tick Size (Cs​t​r​u​c​tC\_{struct}).
* •

  Scalar (λi\lambda\_{i}): The multiplier applied (F​i​n​a​l=C​a​l​c×λiFinal=Calc\times\lambda\_{i}).
* •

  Type: Impact (Size/Session adjustment) or Structure (Microstructure/Volatility override).

Table 4: Master Universe: Macro Groups and Transaction Cost Derivation

| Ticker | Name | Group | Calc | 𝝀𝒊\bm{\lambda\_{i}} | Final | Type / Note |
| --- | --- | --- | --- | --- | --- | --- |
| Sovereign Rates | | | | | | |
| TU | US 2yr Note | RATES\_US | 0.19 | 1.3x | 0.25 | Ultra-Liquid |
| FV | US 5yr Note | RATES\_US | 0.25 | 1.0x | 0.25 | Ultra-Liquid |
| TY | US 10yr Note | RATES\_US | 0.71 | 1.1x | 0.75 | Benchmark |
| US | US 30yr Bond | RATES\_US | 1.32 | 1.1x | 1.50 | Liquid |
| DU | Euro Schatz | RATES\_EU | 0.25 | 1.0x | 0.25 | Short-End EU |
| OE | German Bobl | RATES\_EU | 1.32 | 1.1x | 1.50 | Mid-Curve EU |
| RX | Euro Bund | RATES\_EU | 0.25 | 2.0x | 0.50 | Impact (Duration) |
| G | Long Gilt | RATES\_OTHR | 0.25 | 2.0x | 0.50 | Impact (Non-US) |
| CN | Canada 10yr | RATES\_OTHR | 0.25 | 2.0x | 0.50 | Impact (Depth) |
| Equities | | | | | | |
| ES | S&P 500 | EQUITY\_US | 0.18 | 1.4x | 0.25 | Global Benchmark |
| EN | Nasdaq 100 | EQUITY\_US | 0.05 | 5.0x | 0.25 | Floor Effect |
| YM | Dow Jones | EQUITY\_US | 0.10 | 2.5x | 0.25 | Floor Effect |
| RTY | Russell 2000 | EQUITY\_US | 0.18 | 2.8x | 0.50 | Liquid Small Cap |
| VG | EuroStoxx 50 | EQUITY\_EU | 1.04 | 1.0x | 1.00 | Standard EU Liq |
| Z | FTSE 100 | EQUITY\_EU | 0.65 | 0.8x | 0.50 | Developed Mkt |
| CF | CAC 40 | EQUITY\_EU | 0.65 | 0.8x | 0.50 | Developed Mkt |
| NK | Nikkei 225 | EQUITY\_APAC | 0.64 | 2.3x | 1.50 | Impact (Asian Session) |
| HI | Hang Seng | EQUITY\_APAC | 1.35 | 0.6x | 0.75 | High Velocity |
| Foreign Exchange | | | | | | |
| DX | Dollar Index | FX\_G10 | 0.65 | 0.8x | 0.50 | Spot Arb |
| EU | EUR/USD | FX\_G10 | 0.24 | 1.0x | 0.25 | Global Anchor |
| JY | JPY/USD | FX\_G10 | 0.39 | 1.3x | 0.50 | Impact Scaling |
| BP | GBP/USD | FX\_G10 | 0.39 | 1.3x | 0.50 | Standard G10 |
| CD | CAD/USD | FX\_G10 | 0.36 | 1.4x | 0.50 | Standard G10 |
| AD | AUD/USD | FX\_G10 | 0.40 | 1.3x | 0.50 | Standard G10 |
| SF | CHF/USD | FX\_G10 | 0.50 | 1.0x | 0.50 | Standard G10 |
| PE | Mexican Peso | FX\_EM | 1.02 | 1.0x | 1.00 | High Vol/Low Price |
| Commodities: Energy | | | | | | |
| CL | WTI Crude | COMM\_EN | 0.71 | 1.1x | 0.75 | Global Benchmark |
| CO | Brent Crude | COMM\_EN | 0.71 | 1.1x | 0.75 | Global Benchmark |
| XB | RBOB Gas | COMM\_EN | 1.30 | 1.2x | 1.50 | Product Spread |
| QS | Gasoil | COMM\_EN | 1.30 | 1.2x | 1.50 | Product Spread |
| NG | Natural Gas | COMM\_EN | 1.67 | 1.5x | 2.50 | Structure (Vol) |
| Commodities: Metals | | | | | | |
| GC | Gold | COMM\_PREC | 0.19 | 1.3x | 0.25 | Tight Book |
| SI | Silver | COMM\_PREC | 0.81 | 1.2x | 1.00 | Standard |
| PL | Platinum | COMM\_PREC | 0.53 | 2.8x | 1.50 | Structure (Wide) |
| PA | Palladium | COMM\_PREC | 2.50 | 2.4x | 6.00 | Structure (Thin) |
| HG | Copper | COMM\_BASE | 0.58 | 1.3x | 0.75 | High Efficiency |
| Commodities: Agriculture & Livestock | | | | | | |
| C | Corn | COMM\_AGRI | 2.91 | 0.9x | 2.50 | Standard Grain |
| S | Soybeans | COMM\_AGRI | 1.26 | 1.2x | 1.50 | Deep Market |
| SM | Soybean Meal | COMM\_AGRI | 1.72 | 1.5x | 2.50 | Impact (Crush) |
| BO | Soybean Oil | COMM\_AGRI | 1.30 | 1.2x | 1.50 | Crush Spread |
| W | Wheat | COMM\_AGRI | 2.27 | 1.1x | 2.50 | Volatile |
| KW | KC Wheat | COMM\_AGRI | 2.50 | 1.0x | 2.50 | Volatile |
| SB | Sugar | COMM\_SOFT | 2.38 | 1.1x | 2.50 | Standard Soft |
| KC | Coffee | COMM\_SOFT | 0.81 | 3.1x | 2.50 | Structure (Vol) |
| CC | Cocoa | COMM\_SOFT | 1.00 | 6.0x | 6.00 | Structure (Extreme) |
| CT | Cotton | COMM\_SOFT | 0.70 | 3.6x | 2.50 | Structure (Thin) |
| JO | Orange Juice | COMM\_SOFT | 1.19 | 12.6x | 15.0 | Structure (Distressed) |
| LC | Live Cattle | COMM\_LIVE | 0.68 | 2.2x | 1.50 | Structure (Gappy) |
| FC | Feeder Cattle | COMM\_LIVE | 0.49 | 5.1x | 2.50 | Structure (Gappy) |
| LH | Lean Hogs | COMM\_LIVE | 1.47 | 1.7x | 2.50 | Structure (Gappy) |

### A.5 Specific Overrides

We apply manual overrides where the theoretical tick cost underestimates institutional execution difficulty:

* •

  Floor Effect: Liquid indices like Nasdaq 100 have a structural cost <0.1<0.1 bps. We floor this at 0.25 bps to represent clearing/execution minimums.
* •

  “Roach Motel" Liquidity: Palladium is theoretically cheap but lacks depth. We scale it to 6.0 bps.
* •

  Distressed Liquidity: Orange Juice is assigned 15.0 bps to reflect “widowmaker" liquidity risks.

## Appendix B Turnover Guarantees for Ensembles

This appendix provides formal derivations regarding the convexity of the transaction cost objective and the regularization properties of the ensemble.

### B.1 Convexity of Turnover and Ensemble Guarantee

###### Proposition B.1 (Convexity of Turnover Cost).

Let 𝐩0:L\bm{p}\_{0:L} be a sequence of portfolio position vectors with 𝐩t∈ℝN\bm{p}\_{t}\in\mathbb{R}^{N}.
Assume the scaling vectors satisfy 𝐯t∈ℝ+N\bm{v}\_{t}\in\mathbb{R}^{N}\_{+} and are exogenous (i.e., do not depend on 𝐩\bm{p}).
Define

|  |  |  |
| --- | --- | --- |
|  | 𝒞​(𝒑)=γ​∑t=1L‖𝒗t⊙(𝒑t−𝒑t−1)‖1,γ≥0.\mathcal{C}(\bm{p})\;=\;\gamma\sum\_{t=1}^{L}\big\|\bm{v}\_{t}\odot(\bm{p}\_{t}-\bm{p}\_{t-1})\big\|\_{1},\qquad\gamma\geq 0. |  |

Then 𝒞​(𝐩)\mathcal{C}(\bm{p}) is convex in 𝐩0:L\bm{p}\_{0:L}.

###### Proof.

For each tt, the map 𝒑0:L↦𝒑t−𝒑t−1\bm{p}\_{0:L}\mapsto\bm{p}\_{t}-\bm{p}\_{t-1} is linear.
Elementwise scaling by a fixed 𝒗t\bm{v}\_{t} is also linear, since 𝒗t⊙𝒙=Diag​(𝒗t)​𝒙\bm{v}\_{t}\odot\bm{x}=\mathrm{Diag}(\bm{v}\_{t})\bm{x}.
Thus the composition 𝒑↦𝒗t⊙(𝒑t−𝒑t−1)\bm{p}\mapsto\bm{v}\_{t}\odot(\bm{p}\_{t}-\bm{p}\_{t-1}) is linear.
Because ∥⋅∥1\|\cdot\|\_{1} is convex and convexity is preserved under composition with an affine map,
𝒑↦‖𝒗t⊙(𝒑t−𝒑t−1)‖1\bm{p}\mapsto\|\bm{v}\_{t}\odot(\bm{p}\_{t}-\bm{p}\_{t-1})\|\_{1} is convex.
Summing over tt with nonnegative weight γ≥0\gamma\geq 0 preserves convexity, hence 𝒞\mathcal{C} is convex.
∎

###### Corollary B.2 (Ensembling Reduces Cost (Executed Mean Policy)).

Let {𝐩(k)}k=1K\{\bm{p}^{(k)}\}\_{k=1}^{K} be KK policies and define the executed mean policy
𝐩¯:=1K​∑k=1K𝐩(k)\bar{\bm{p}}:=\frac{1}{K}\sum\_{k=1}^{K}\bm{p}^{(k)} (averaged at the *position* level).
Then, by convexity of 𝒞\mathcal{C},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞​(𝒑¯)≤1K​∑k=1K𝒞​(𝒑(k)).\mathcal{C}(\bar{\bm{p}})\leq\frac{1}{K}\sum\_{k=1}^{K}\mathcal{C}(\bm{p}^{(k)}). |  | (49) |

###### Proof.

Since 𝒞\mathcal{C} is convex, Jensen’s inequality gives

|  |  |  |
| --- | --- | --- |
|  | 𝒞​(1K​∑k=1K𝒑(k))≤1K​∑k=1K𝒞​(𝒑(k)),\mathcal{C}\!\left(\frac{1}{K}\sum\_{k=1}^{K}\bm{p}^{(k)}\right)\leq\frac{1}{K}\sum\_{k=1}^{K}\mathcal{C}\!\left(\bm{p}^{(k)}\right), |  |

which is the desired result.
∎

Note: This guarantee applies when the ensemble is implemented by executing the averaged positions 𝒑¯\bar{\bm{p}}.
If instead each policy 𝒑(k)\bm{p}^{(k)} is traded separately and P&L is averaged ex post, transaction costs are incurred per-policy and the inequality need not reflect realized costs.

### B.2 Optimal Regularization under Ensembling

###### Proposition B.3 (Optimal Penalty Decreases with Ensemble Size).

Let γ≥0\gamma\geq 0 be the explicit turnover penalty strength used during training, and let KK be the ensemble size.
We model the realized Net Sharpe Ratio as

|  |  |  |
| --- | --- | --- |
|  | SRnet​(γ,K)=SRgross​(γ)−ρ​(K)​Δ​(γ),\mathrm{SR}\_{\mathrm{net}}(\gamma,K)\;=\;\mathrm{SR}\_{\mathrm{gross}}(\gamma)\;-\;\rho(K)\,\Delta(\gamma), |  |

where Δ​(γ)\Delta(\gamma) is the turnover cost and ρ​(K)\rho(K) is an ensemble-dependent cost reduction factor.

Under the standard assumptions that:

1. 1.

   Gross performance is strictly concave in regularization (SRgross′′​(γ)<0\mathrm{SR}^{\prime\prime}\_{\mathrm{gross}}(\gamma)<0):
   Intuitively, relaxing constraints yields diminishing returns; the initial units of freedom capture high-conviction opportunities, while further relaxation allows the model to chase increasingly marginal and noisy signals.
2. 2.

   Turnover cost is strictly decreasing and convex in regularization (Δ′​(γ)<0,Δ′′​(γ)>0\Delta^{\prime}(\gamma)<0,\Delta^{\prime\prime}(\gamma)>0):
   This reflects the fact that a small penalty is sufficient to eliminate the most expensive high-frequency “noise trading,” while further increases yield progressively smaller reductions in turnover as the portfolio approaches a static hold.
3. 3.

   Ensembling reduces realized turnover costs (ρ′​(K)<0\rho^{\prime}(K)<0):
   As discussed in Sec. [5.2](https://arxiv.org/html/2601.05975v1#S5.SS2 "5.2 Ensembling and Implicit Cost Regularization ‣ 5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"), independent models often make uncorrelated errors, averaging their positions cancels out idiosyncratic “noise trades,” naturally dampening turnover without requiring explicit penalties.

and assuming an interior maximizer exists, the optimal training penalty γ⋆​(K)\gamma^{\star}(K) is strictly decreasing in the ensemble size KK.

###### Lemma B.4 (Sufficient condition for an interior optimizer on (0,1)(0,1)).

Assume γ∈[0,1]\gamma\in[0,1] and Φ​(γ,ρ)\Phi(\gamma,\rho) is continuously differentiable in γ\gamma.
If

|  |  |  |
| --- | --- | --- |
|  | Φγ​(0,ρ)>0andΦγ​(1,ρ)<0,\Phi\_{\gamma}(0,\rho)>0\quad\text{and}\quad\Phi\_{\gamma}(1,\rho)<0, |  |

then there exists γ⋆∈(0,1)\gamma^{\star}\in(0,1) such that Φγ​(γ⋆,ρ)=0\Phi\_{\gamma}(\gamma^{\star},\rho)=0.

###### Proof.

By continuity of Φγ​(⋅,ρ)\Phi\_{\gamma}(\cdot,\rho) and the Intermediate Value Theorem, it must cross zero on (0,1)(0,1).
∎

Specialization to our objective.
Here Φ​(γ,ρ)=SRgross​(γ)−ρ​Δ​(γ)\Phi(\gamma,\rho)=\mathrm{SR}\_{\mathrm{gross}}(\gamma)-\rho\Delta(\gamma) and hence

|  |  |  |
| --- | --- | --- |
|  | Φγ​(γ,ρ)=SRgross′​(γ)−ρ​Δ′​(γ).\Phi\_{\gamma}(\gamma,\rho)=\mathrm{SR}^{\prime}\_{\mathrm{gross}}(\gamma)-\rho\Delta^{\prime}(\gamma). |  |

Therefore a sufficient condition for γ⋆∈(0,1)\gamma^{\star}\in(0,1) is

|  |  |  |
| --- | --- | --- |
|  | SRgross′​(0)−ρ​Δ′​(0)>0andSRgross′​(1)−ρ​Δ′​(1)<0.\mathrm{SR}^{\prime}\_{\mathrm{gross}}(0)-\rho\Delta^{\prime}(0)>0\quad\text{and}\quad\mathrm{SR}^{\prime}\_{\mathrm{gross}}(1)-\rho\Delta^{\prime}(1)<0. |  |

###### Proof of Proposition.

The objective is to maximize Φ​(γ,ρ)=SRgross​(γ)−ρ​Δ​(γ)\Phi(\gamma,\rho)=\mathrm{SR}\_{\mathrm{gross}}(\gamma)-\rho\Delta(\gamma).
Assume an interior maximizer γ⋆\gamma^{\star} exists and satisfies the second-order condition
∂2Φ∂γ2​(γ⋆,ρ)<0\frac{\partial^{2}\Phi}{\partial\gamma^{2}}(\gamma^{\star},\rho)<0.
The first-order condition (FOC) for an interior maximum is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Φ∂γ=SRgross′​(γ)−ρ​Δ′​(γ)=0.\frac{\partial\Phi}{\partial\gamma}=\mathrm{SR}^{\prime}\_{\mathrm{gross}}(\gamma)-\rho\Delta^{\prime}(\gamma)=0. |  | (50) |

To determine how the optimal γ⋆\gamma^{\star} responds to changes in the ensemble factor ρ\rho, we apply the Implicit Function Theorem.
Let

|  |  |  |
| --- | --- | --- |
|  | F​(γ,ρ)=SRgross′​(γ)−ρ​Δ′​(γ).F(\gamma,\rho)=\mathrm{SR}^{\prime}\_{\mathrm{gross}}(\gamma)-\rho\Delta^{\prime}(\gamma). |  |

Then, locally around (γ⋆,ρ)(\gamma^{\star},\rho),

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​γ⋆d​ρ=−∂F/∂ρ∂F/∂γ.\frac{d\gamma^{\star}}{d\rho}=-\frac{\partial F/\partial\rho}{\partial F/\partial\gamma}. |  | (51) |

Analyzing the components:

* •

  Numerator: ∂F∂ρ=−Δ′​(γ)\frac{\partial F}{\partial\rho}=-\Delta^{\prime}(\gamma). Since turnover decreases with penalty (Δ′​(γ)<0\Delta^{\prime}(\gamma)<0), this term is strictly positive.
* •

  Denominator: ∂F∂γ=SRgross′′​(γ)−ρ​Δ′′​(γ)\frac{\partial F}{\partial\gamma}=\mathrm{SR}^{\prime\prime}\_{\mathrm{gross}}(\gamma)-\rho\Delta^{\prime\prime}(\gamma).
  Given SRgross′′​(γ)<0\mathrm{SR}^{\prime\prime}\_{\mathrm{gross}}(\gamma)<0 and Δ′′​(γ)>0\Delta^{\prime\prime}(\gamma)>0 with ρ≥0\rho\geq 0, the entire term is strictly negative (satisfying the second-order condition for a maximum).

Substituting these signs into the sensitivity equation yields d​γ⋆d​ρ>0\frac{d\gamma^{\star}}{d\rho}>0.

Since ρ​(K)\rho(K) is a decreasing function of KK (ensembling reduces realized turnover costs), by the chain rule we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​γ⋆d​K=d​γ⋆d​ρ⋅ρ′​(K)<0.\frac{d\gamma^{\star}}{dK}=\frac{d\gamma^{\star}}{d\rho}\cdot\rho^{\prime}(K)<0. |  | (52) |

This proves that as the ensemble size increases, the optimal explicit regularization parameter γ⋆\gamma^{\star} decreases.
∎

## Appendix C Exact Gradient Accumulation for Non-Separable Objectives

Training Sharpe-ratio-maximizing portfolio models often requires a large *effective* batch size, but GPU
memory limits force microbatching. Unlike additive objectives (e.g., ∑iℓi\sum\_{i}\ell\_{i}), Sharpe-style losses are
*non-separable* because their gradients depend on *global* batch statistics. Consequently, naive
microbatch gradient accumulation (computing Sharpe per microbatch and summing gradients) generally does *not*
equal the full-batch gradient.

We therefore use an *Exact Two-Pass Microbatching* protocol: a first pass computes all global/sufficient
statistics *without* storing activations, and a second pass replays the forward pass and injects the
*analyatical* upstream gradient ∇rℒ\nabla\_{r}\mathcal{L} into autograd. This yields the same parameter gradient
as a single full-batch backward pass under the conditions stated below, while keeping activation memory constant.

### C.1 Notation and Objectives

Let the model output net portfolio returns arranged as a matrix
R∈ℝB×LR\in\mathbb{R}^{B\times L} with entries Rb,tR\_{b,t} (sample bb, time index tt). Let
N:=B​LN:=BL be the number of return entries in the batch. Let AA denote the annualization factor (e.g., A=252A=252).
We use εσ>0\varepsilon\_{\sigma}>0 for numerical stability in denominators and a variance floor
εvar>0\varepsilon\_{\mathrm{var}}>0 to prevent σ→0\sigma\!\to\!0 gradient blow-ups.

Define pooled (batch-level) statistics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μ\displaystyle\mu | =1N​∑b=1B∑t=1LRb,t,q=1N​∑b=1B∑t=1LRb,t2,\displaystyle=\frac{1}{N}\sum\_{b=1}^{B}\sum\_{t=1}^{L}R\_{b,t},\qquad q=\frac{1}{N}\sum\_{b=1}^{B}\sum\_{t=1}^{L}R\_{b,t}^{2}, |  | (53) |
|  | σ\displaystyle\sigma | =max⁡(q−μ2,εvar).\displaystyle=\sqrt{\max\!\left(q-\mu^{2},\ \varepsilon\_{\mathrm{var}}\right)}. |  |

Now, define per-sample statistics. For each sample bb,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μb\displaystyle\mu\_{b} | =1L​∑t=1LRb,t,qb=1L​∑t=1LRb,t2,\displaystyle=\frac{1}{L}\sum\_{t=1}^{L}R\_{b,t},\qquad q\_{b}=\frac{1}{L}\sum\_{t=1}^{L}R\_{b,t}^{2}, |  | (54) |
|  | σb\displaystyle\sigma\_{b} | =max⁡(qb−μb2,εvar).\displaystyle=\sqrt{\max\!\left(q\_{b}-\mu\_{b}^{2},\ \varepsilon\_{\mathrm{var}}\right)}. |  |

In implementation we use a minimum clamp on the variance; when the clamp is active, the gradient through the
variance term is zero, ensuring the 1/σ1/\sigma factors remain bounded.

##### Loss.

We optimize

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=ℒpool+λ​ℒsoft,\mathcal{L}=\mathcal{L}\_{\mathrm{pool}}+\lambda\,\mathcal{L}\_{\mathrm{soft}}, |  | (55) |

where the pooled Sharpe loss is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒpool=−A​μσ+εσ.\mathcal{L}\_{\mathrm{pool}}=-\sqrt{A}\,\frac{\mu}{\sigma+\varepsilon\_{\sigma}}. |  | (56) |

The SoftMin term ℒsoft\mathcal{L}\_{\mathrm{soft}} is defined in the main text and is chosen to
*maximize* the soft-min (smooth worst-case) per-sample Sharpe across groups. In the appendix we only require its
upstream gradient (below).

Define per-sample Sharpe

|  |  |  |  |
| --- | --- | --- | --- |
|  | SRb=A​μbσb+εσ.\mathrm{SR}\_{b}=\sqrt{A}\,\frac{\mu\_{b}}{\sigma\_{b}+\varepsilon\_{\sigma}}. |  | (57) |

Let the BB sequences be partitioned into GG groups of size KK (where B=G​KB=GK), indexed by group g∈{1,…,G}g\in\{1,\dots,G\} and within-group index k∈{1,…,K}k\in\{1,\dots,K\}. We map each sequence bb to a unique pair (g,k)(g,k). Consistent with the adversarial weights derived in App. [D](https://arxiv.org/html/2601.05975v1#A4 "Appendix D Analysis of the Robust Objective ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"), we define the group-wise SoftMin weights as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qg,k⋆=exp⁡(−SRg,k/τ)∑j=1Kexp⁡(−SRg,j/τ).q^{\star}\_{g,k}=\frac{\exp\!\left(-\mathrm{SR}\_{g,k}/\tau\right)}{\sum\_{j=1}^{K}\exp\!\left(-\mathrm{SR}\_{g,j}/\tau\right)}. |  | (58) |

For the (negative) soft-min objective used to maximize worst-case Sharpe, the upstream gradient is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂ℒsoft∂SRg,k=−1G​qg,k⋆.\frac{\partial\mathcal{L}\_{\mathrm{soft}}}{\partial\mathrm{SR}\_{g,k}}=-\frac{1}{G}\,q^{\star}\_{g,k}. |  | (59) |

### C.2 Analyatical Gradients

Differentiating ([56](https://arxiv.org/html/2601.05975v1#A3.E56 "Equation 56 ‣ Loss. ‣ C.1 Notation and Objectives ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) w.r.t. Rb,tR\_{b,t} gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂ℒpool∂Rb,t\displaystyle\frac{\partial\mathcal{L}\_{\mathrm{pool}}}{\partial R\_{b,t}} | =−A[1N​(σ+εσ)\displaystyle=-\sqrt{A}\Biggl[\frac{1}{N(\sigma+\varepsilon\_{\sigma})} |  | (60) |
|  |  | −μ​(Rb,t−μ)N​(σ+εσ)2​σ].\displaystyle\qquad\qquad-\frac{\mu\,(R\_{b,t}-\mu)}{N\,(\sigma+\varepsilon\_{\sigma})^{2}\,\sigma}\Biggr]. |  |

Differentiating ([57](https://arxiv.org/html/2601.05975v1#A3.E57 "Equation 57 ‣ Loss. ‣ C.1 Notation and Objectives ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂SRb∂Rb,t\displaystyle\frac{\partial\mathrm{SR}\_{b}}{\partial R\_{b,t}} | =A[1L​(σb+εσ)\displaystyle=\sqrt{A}\Biggl[\frac{1}{L(\sigma\_{b}+\varepsilon\_{\sigma})} |  | (61) |
|  |  | −μb​(Rb,t−μb)L​(σb+εσ)2​σb].\displaystyle\qquad\qquad-\frac{\mu\_{b}\,(R\_{b,t}-\mu\_{b})}{L\,(\sigma\_{b}+\varepsilon\_{\sigma})^{2}\,\sigma\_{b}}\Biggr]. |  |

Using ([59](https://arxiv.org/html/2601.05975v1#A3.E59 "Equation 59 ‣ Loss. ‣ C.1 Notation and Objectives ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) and the fact that SRg,k\mathrm{SR}\_{g,k} depends only on its own sample,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂ℒsoft∂Rb,t\displaystyle\frac{\partial\mathcal{L}\_{\mathrm{soft}}}{\partial R\_{b,t}} | =−1G​πg​(b),k​(b)​∂SRb∂Rb,t.\displaystyle=-\frac{1}{G}\,\pi\_{g(b),k(b)}\;\frac{\partial\mathrm{SR}\_{b}}{\partial R\_{b,t}}. |  | (62) |

The total upstream gradient, used for injection in Pass 2, is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gb,t=∂ℒ∂Rb,t=∂ℒpool∂Rb,t+λ​∂ℒsoft∂Rb,t.\displaystyle G\_{b,t}=\frac{\partial\mathcal{L}}{\partial R\_{b,t}}=\frac{\partial\mathcal{L}\_{\mathrm{pool}}}{\partial R\_{b,t}}+\lambda\,\frac{\partial\mathcal{L}\_{\mathrm{soft}}}{\partial R\_{b,t}}. |  | (63) |

For implementation via autograd, we aggregate the element-wise analyatical gradients into a microbatch-level tensor. Let ℬm\mathcal{B}\_{m} denote the set of indices for the samples contained in microbatch mm. We define the injected gradient tensor Gm∈ℝ|ℬm|×LG\_{m}\in\mathbb{R}^{|\mathcal{B}\_{m}|\times L} such that its entries correspond to the scalar gradients Gb,tG\_{b,t} derived in ([63](https://arxiv.org/html/2601.05975v1#A3.E63 "Equation 63 ‣ C.2 Analyatical Gradients ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) for all b∈ℬmb\in\mathcal{B}\_{m} and t∈{1,…,L}t\in\{1,\dots,L\}. This tensor is then passed directly to the model’s output during the second pass.

### C.3 Exact Two-Pass Microbatching Algorithm

The procedure splits the training step into two distinct passes over the data to circumvent memory bottlenecks while maintaining mathematical exactness.

Phase 1: Statistical Accumulation. The model processes the data in microbatches with autograd disabled. Since gradients are not tracked, memory usage is minimal. We aggregate the sufficient statistics—sum of returns (∑R\sum R) and sum of squared returns (∑R2\sum R^{2})—globally and per sample. These aggregates allow us to compute the exact batch-wide mean μ\mu and volatility σ\sigma, which are required to define the true gradients.

Phase 2: Gradient Injection. The model processes the data a second time with autograd enabled. Crucially, we do not compute the loss function forward. Instead, we use the pre-computed μ\mu and σ\sigma from Phase 1 to evaluate the analyatical gradient formulas derived in Section [C.2](https://arxiv.org/html/2601.05975v1#A3.SS2 "C.2 Analyatical Gradients ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"). This yields a gradient tensor GmG\_{m} for the microbatch outputs. We inject this tensor directly into the backward pass using r\_m.backward(gradient=G\_m). This propagates the exact gradient of the full-batch Sharpe ratio through the computation graph of the microbatch.

Algorithm 1  Exact Two-Pass Microbatching for Non-Separable Sharpe Objectives

1:Inputs: dataset 𝒟\mathcal{D}, microbatch size MM, model parameters θ\theta

2:Initialize pooled sums S1←0S\_{1}\leftarrow 0, S2←0S\_{2}\leftarrow 0

3:Initialize per-sample sums {S1,b}b=1B←0\{S\_{1,b}\}\_{b=1}^{B}\leftarrow 0, {S2,b}b=1B←0\{S\_{2,b}\}\_{b=1}^{B}\leftarrow 0

4:// Pass 1: Collect Statistics (No Activations)

5:for microbatch mm in 𝒟\mathcal{D} do

6:  Set deterministic RNG seed for microbatch mm

7:  Rm←Modelθ​(inputm)R\_{m}\leftarrow\text{Model}\_{\theta}(\text{input}\_{m}) ⊳\triangleright forward only

8:  Accumulate pooled: S1+=∑RmS\_{1}\mathrel{+}=\sum R\_{m}, S2+=∑Rm2S\_{2}\mathrel{+}=\sum R\_{m}^{2}

9:  Accumulate per-sample: S1,b+=∑tRb,tS\_{1,b}\mathrel{+}=\sum\_{t}R\_{b,t}, S2,b+=∑tRb,t2S\_{2,b}\mathrel{+}=\sum\_{t}R\_{b,t}^{2}

10:end for

11:Compute μ,q,σ\mu,q,\sigma from S1,S2S\_{1},S\_{2} via ([53](https://arxiv.org/html/2601.05975v1#A3.E53 "Equation 53 ‣ C.1 Notation and Objectives ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"))

12:Compute μb,qb,σb\mu\_{b},q\_{b},\sigma\_{b} from S1,b,S2,bS\_{1,b},S\_{2,b} via ([54](https://arxiv.org/html/2601.05975v1#A3.E54 "Equation 54 ‣ C.1 Notation and Objectives ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"))

13:Compute all SRb\mathrm{SR}\_{b} via ([57](https://arxiv.org/html/2601.05975v1#A3.E57 "Equation 57 ‣ Loss. ‣ C.1 Notation and Objectives ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) and SoftMin weights πg,k\pi\_{g,k} via ([58](https://arxiv.org/html/2601.05975v1#A3.E58 "Equation 58 ‣ Loss. ‣ C.1 Notation and Objectives ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"))

14:// Pass 2: Inject analyatical Upstream Gradient

15:for microbatch mm in 𝒟\mathcal{D} do

16:  Reset deterministic RNG seed for microbatch mm

17:  Rm←Modelθ​(inputm)R\_{m}\leftarrow\text{Model}\_{\theta}(\text{input}\_{m}) ⊳\triangleright forward with autograd

18:  Build GmG\_{m} using ([60](https://arxiv.org/html/2601.05975v1#A3.E60 "Equation 60 ‣ C.2 Analyatical Gradients ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")), ([61](https://arxiv.org/html/2601.05975v1#A3.E61 "Equation 61 ‣ C.2 Analyatical Gradients ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")), ([62](https://arxiv.org/html/2601.05975v1#A3.E62 "Equation 62 ‣ C.2 Analyatical Gradients ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")), ([63](https://arxiv.org/html/2601.05975v1#A3.E63 "Equation 63 ‣ C.2 Analyatical Gradients ‣ Appendix C Exact Gradient Accumulation for Non-Separable Objectives ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"))

19:  Rm.backward​(Gm)R\_{m}.\text{backward}(G\_{m}) ⊳\triangleright inject upstream gradient

20:end for

21:Optimizer.step​()\text{Optimizer.step}()

We must consider some exactness conditions. The two-pass protocol reproduces the same parameter gradient as a single full-batch backward pass *provided that*
the per-sample forward mapping is identical across passes and independent of microbatch composition. Concretely:
(i) No batch-coupled layers: the network must not contain layers whose outputs depend on microbatch
statistics (e.g., BatchNorm) or on other samples in the microbatch.
(ii) No stateful forward updates: modules that update running buffers during the forward pass must be
disabled/frozen.
(iii) Identical data order and grouping: Pass 1 and Pass 2 must iterate over the same samples in the same
order, and the SoftMin grouping/indexing used to compute πg,k\pi\_{g,k} must match the mapping used when injecting
gradients in Pass 2 (i.e., no reshuffling between passes).
(iv) Deterministic stochastic layers: any stochasticity (e.g., Dropout) must be controlled so that RmR\_{m} is
identical in both passes (handled by per-microbatch RNG reseeding above).

## Appendix D Analysis of the Robust Objective

This appendix provides a formal interpretation of the windowed *SoftMin* aggregation used in
Sec. [5.1](https://arxiv.org/html/2601.05975v1#S5.SS1 "5.1 Robust Objective: Pooled Sharpe with SoftMin Penalty ‣ 5 Learning Objective and Optimization ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"). We show that the resulting objective admits (i) a KL-penalized
distributionally robust optimization (DRO) interpretation via the Gibbs/Donsker–Varadhan variational
principle, and (ii) a connection to the coherent risk measure *Entropic Value-at-Risk (EVaR)*.

### D.1 SoftMin as KL-penalized DRO (Variational Form)

We consider BB training windows and their realized Sharpe ratios {SRb}b=1B\{\mathrm{SR}\_{b}\}\_{b=1}^{B}.
Define window *losses* Zb​(θ)≔−SRb​(θ)Z\_{b}(\theta)\coloneqq-\mathrm{SR}\_{b}(\theta), and let PP denote the
uniform empirical distribution over windows (P​(b)=1/BP(b)=1/B). For a temperature τ>0\tau>0, our SoftMin-in-Sharpe
objective is equivalently a softmax in the losses:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒsoft​(θ)\displaystyle\mathcal{L}\_{\text{soft}}(\theta) | =τ​log⁡(1B​∑b=1Bexp⁡(Zb​(θ)τ))=τ​log⁡𝔼P​[exp⁡(Zτ)].\displaystyle\!=\!\tau\log\!\left(\frac{1}{B}\sum\_{b=1}^{B}\exp\!\left(\frac{Z\_{b}(\theta)}{\tau}\right)\right)\!=\!\tau\log\mathbb{E}\_{P}\!\!\left[\exp\!\left(\frac{Z}{\tau}\right)\right]\!. |  | (64) |

As τ→0+\tau\to 0^{+}, ℒsoft​(θ)→maxb⁡Zb​(θ)=−minb⁡SRb​(θ)\mathcal{L}\_{\text{soft}}(\theta)\to\max\_{b}Z\_{b}(\theta)=-\min\_{b}\mathrm{SR}\_{b}(\theta),
recovering a worst-window (min-Sharpe) criterion; as τ→∞\tau\to\infty, it approaches the average loss.

###### Proposition D.1 (Gibbs / Donsker–Varadhan variational principle (discrete)).

The entropic aggregate in ([64](https://arxiv.org/html/2601.05975v1#A4.E64 "Equation 64 ‣ D.1 SoftMin as KL-penalized DRO (Variational Form) ‣ Appendix D Analysis of the Robust Objective ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) admits the dual representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ​log⁡𝔼P​[eZ/τ]=supQ≪P{𝔼Q​[Z]−τ​KL​(Q∥P)},\tau\log\mathbb{E}\_{P}\!\left[\mathrm{e}^{Z/\tau}\right]=\sup\_{Q\ll P}\left\{\mathbb{E}\_{Q}[Z]-\tau\,\mathrm{KL}(Q\|P)\right\}, |  | (65) |

where QQ is an adversarial reweighting over windows and Q≪PQ\ll P is automatic here since PP is uniform.

###### Proof.

The duality follows directly from the variational representation of the log-sum-exp function, a standard result in convex analysis [Boucheron et al., [2013](https://arxiv.org/html/2601.05975v1#bib.bib93 "Concentration inequalities: a nonasymptotic theory of independence")]. For completeness, we derive it for the discrete case below. Let qbq\_{b} be the weights of QQ with ∑b=1Bqb=1\sum\_{b=1}^{B}q\_{b}=1. Since P​(b)=1/BP(b)=1/B,
KL​(Q∥P)=∑b=1Bqb​log⁡(qb/(1/B))=∑b=1Bqb​log⁡(B​qb).\mathrm{KL}(Q\|P)=\sum\_{b=1}^{B}q\_{b}\log\!\big(q\_{b}/(1/B)\big)=\sum\_{b=1}^{B}q\_{b}\log(Bq\_{b}).
Consider the Lagrangian

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(q,η)=∑b=1Bqb​Zb−τ​∑b=1Bqb​log⁡(B​qb)+η​(1−∑b=1Bqb).J(q,\eta)=\sum\_{b=1}^{B}q\_{b}Z\_{b}-\tau\sum\_{b=1}^{B}q\_{b}\log(Bq\_{b})+\eta\!\left(1-\sum\_{b=1}^{B}q\_{b}\right). |  | (66) |

Stationarity gives
0=∂J/∂qb=Zb−τ​(1+log⁡(B​qb))−η,0=\partial J/\partial q\_{b}=Z\_{b}-\tau\big(1+\log(Bq\_{b})\big)-\eta,
hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | qb⋆=exp⁡(Zb/τ)∑j=1Bexp⁡(Zj/τ).q\_{b}^{\star}=\frac{\exp(Z\_{b}/\tau)}{\sum\_{j=1}^{B}\exp(Z\_{j}/\tau)}. |  | (67) |

Substituting q⋆q^{\star} into ∑bqb​Zb−τ​∑bqb​log⁡(B​qb)\sum\_{b}q\_{b}Z\_{b}-\tau\sum\_{b}q\_{b}\log(Bq\_{b}) yields
τ​log⁡(1B​∑b=1BeZb/τ)\tau\log\!\big(\frac{1}{B}\sum\_{b=1}^{B}\mathrm{e}^{Z\_{b}/\tau}\big), i.e. ([64](https://arxiv.org/html/2601.05975v1#A4.E64 "Equation 64 ‣ D.1 SoftMin as KL-penalized DRO (Variational Form) ‣ Appendix D Analysis of the Robust Objective ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")).
∎

The weights qb⋆q\_{b}^{\star} in ([67](https://arxiv.org/html/2601.05975v1#A4.E67 "Equation 67 ‣ Proof. ‣ D.1 SoftMin as KL-penalized DRO (Variational Form) ‣ Appendix D Analysis of the Robust Objective ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) provide a diagnostic: concentrated mass on a
small set of windows indicates that those regimes dominate the gradient signal and are the current
“stress scenarios” for the model.

### D.2 Connection to KL-ball DRO and EVaR

A “hard” DRO variant constrains the adversary to a KL-divergence ball of radius CC:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛC​(Z)=supQ:KL​(Q∥P)≤C𝔼Q​[Z].\mathcal{R}\_{C}(Z)=\sup\_{Q:\,\mathrm{KL}(Q\|P)\leq C}\mathbb{E}\_{Q}[Z]. |  | (68) |

By Lagrangian duality together with Proposition [D.1](https://arxiv.org/html/2601.05975v1#A4.Thmtheorem1 "Proposition D.1 (Gibbs / Donsker–Varadhan variational principle (discrete)). ‣ D.1 SoftMin as KL-penalized DRO (Variational Form) ‣ Appendix D Analysis of the Robust Objective ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management"), this is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛC​(Z)=infλ>0{λ​log⁡𝔼P​[eZ/λ]+λ​C}.\mathcal{R}\_{C}(Z)=\inf\_{\lambda>0}\left\{\lambda\log\mathbb{E}\_{P}\!\left[\mathrm{e}^{Z/\lambda}\right]+\lambda C\right\}. |  | (69) |

Choosing the divergence budget C=−log⁡(1−α)C=-\log(1-\alpha) yields *Entropic Value-at-Risk (EVaR)* at confidence
level α∈(0,1)\alpha\in(0,1):

|  |  |  |  |
| --- | --- | --- | --- |
|  | EVaRα​(Z)=infλ>0{λ​log⁡𝔼​[eZ/λ]−λ​log⁡(1−α)}.\mathrm{EVaR}\_{\alpha}(Z)=\inf\_{\lambda>0}\left\{\lambda\log\mathbb{E}\!\left[\mathrm{e}^{Z/\lambda}\right]-\lambda\log(1-\alpha)\right\}. |  | (70) |

In DeePM, the training temperature τ\tau can be viewed as selecting a particular member of this
entropic/EVaR family (i.e., evaluating ([70](https://arxiv.org/html/2601.05975v1#A4.E70 "Equation 70 ‣ D.2 Connection to KL-ball DRO and EVaR ‣ Appendix D Analysis of the Robust Objective ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")) at λ=τ\lambda=\tau, up to the additive constant
−τ​log⁡(1−α)-\tau\log(1-\alpha) when α\alpha is fixed). Thus SoftMin training implements a smooth, tail-sensitive
surrogate that emphasizes poor historical windows, while remaining differentiable and stable.

## Appendix E Experimental Implementation Details

This appendix provides the granular specifications required to reproduce the experimental results, including hyperparameter search spaces, and the specific optimization protocols employed.

### E.1 Optimization and Training Dynamics

We optimize the parameters using AdamW [Loshchilov and Hutter, [2019](https://arxiv.org/html/2601.05975v1#bib.bib55 "Decoupled weight decay regularization")] to decouple weight decay from gradient updates, which is crucial for stabilizing Transformers. We use a fixed learning rate of η=10−4\eta=10^{-4} without annealing, as the non-stationary nature of financial data often makes cyclic or decaying schedules suboptimal for continuous learning.

Given the low signal-to-noise ratio in financial time series, validation metrics can be highly volatile across epochs. To prevent premature stopping due to lucky/unlucky noise, we implement an Exponential Moving Average (EMA) on the validation metric (Sharpe Ratio).
Let SkvalS\_{k}^{\text{val}} be the raw validation Sharpe at iteration kk. The smoothed metric S~k\tilde{S}\_{k} updates as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S~k=αsmooth​Skval+(1−αsmooth)​S~k−1,\tilde{S}\_{k}=\alpha\_{\text{smooth}}S\_{k}^{\text{val}}+(1-\alpha\_{\text{smooth}})\tilde{S}\_{k-1}, |  | (71) |

with αsmooth=0.45\alpha\_{\text{smooth}}=0.45. Training terminates if S~k\tilde{S}\_{k} fails to improve by δmin=0.001\delta\_{\text{min}}=0.001 for a patience defined per architecture (see Table [5](https://arxiv.org/html/2601.05975v1#A5.T5 "Table 5 ‣ E.3 Hyperparameter Search Space ‣ Appendix E Experimental Implementation Details ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")). We employ a “burn-in" of 20 iterations before enabling the early stopping trigger to allow the optimizer to stabilize.

Models were trained on a single NVIDIA GeForce RTX 3090 (24GB) GPU.

### E.2 Existence Masking and Missingness Handling

Since the architecture is permutation equivariant, it inherently handles variable-sized sets of assets (Nt≤NN\_{t}\leq N). However, for practical training on GPUs requiring fixed tensor shapes, we construct the data tensor on a complete (i,t)(i,t) grid with forward-filling.
To prevent learning from synthetically filled values when a contract is not present, DeePM uses: (i) an existence indicator appended to dynamic inputs, (ii) a key-padding mask kpmℓ\mathrm{kpm}\_{\ell} in cross-sectional attention, and (iii) explicit zeroing of invalid node rows after spatial blocks. Finally, positions are masked via mi,tm\_{i,t} in Eq. ([13](https://arxiv.org/html/2601.05975v1#S3.E13 "Equation 13 ‣ 3.2 Portfolio Returns and Frictions ‣ 3 Problem Setup and Data ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management")).

### E.3 Hyperparameter Search Space

We perform a random grid search over the key architectural and regularization parameters. For the final ensemble, we select the top seeds from 100 random trials based on the best smoothed validation Sharpe ratio. Table [5](https://arxiv.org/html/2601.05975v1#A5.T5 "Table 5 ‣ E.3 Hyperparameter Search Space ‣ Appendix E Experimental Implementation Details ‣ DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management") details the search grid for the proposed DeePM model versus the Momentum Transformer baseline.

Table 5: Hyperparameter Search Space (DeePM vs. Baseline)

|  |  |  |
| --- | --- | --- |
| Parameter | DeePM (Proposed) | Momentum Transformer |
| Architecture | | |
| Hidden Dimension (dmodeld\_{\text{model}}) | {64,128}\{64,128\} | {64,128}\{64,128\} |
| Attention Heads | {2,4}\{2,4\} | 44 |
| Dropout | {0.3,0.4,0.5}\{0.3,0.4,0.5\} | {0.3,0.4,0.}\{0.3,0.4,0.\} |
| Optimization | | |
| Batch Size | 6464 | {64,128}\{64,128\} |
| Learning Rate | 10−410^{-4} | {10−4,3⋅10−4}\{10^{-4},3\cdot 10^{-4}\} |
| Weight Decay | {10−5,10−4,10−3}\{10^{-5},10^{-4},10^{-3}\} | {10−5,10−4,10−3}\{10^{-5},10^{-4},10^{-3}\} |
| Max Gradient Norm | {0.5,1.0}\{0.5,1.0\} | {0.5,1.0}\{0.5,1.0\} |
| Training Burn-in Steps | 50 | 5 |
| SoftMin Temp (τ\tau) | 0.2 | - |
| SoftMin Scalar (λ\lambda) | 0.1 | - |
| Training Config | | |
| Sequence Length | 8484 days | 8484 days |
| Burn-in Steps | 2121 days | 2121 days |
| Iterations | 10001000 | 200200 |
| Early Stopping Patience | 5050 | 2525 |
| Top NN Ensemble | 2525 | 2525 |