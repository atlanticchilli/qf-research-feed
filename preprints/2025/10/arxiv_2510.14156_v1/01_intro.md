---
authors:
- Jan Kwiatkowski
- Jarosław A. Chudziak
doc_id: arxiv:2510.14156v1
family_id: arxiv:2510.14156
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'On Evaluating Loss Functions for Stock Ranking: An Empirical Analysis With
  Transformer Model'
url_abs: http://arxiv.org/abs/2510.14156v1
url_html: https://arxiv.org/html/2510.14156v1
venue: arXiv q-fin
version: 1
year: 2025
---


[Jan Kwiatkowski](https://orcid.org/0009-0006-6071-1607)
  
Institute of Computer Science, Warsaw University of Technology
  
jan.kwiatkowski.stud@pw.edu.pl
  
&[Jarosław A. Chudziak](https://orcid.org/0000-0003-4534-8652)
  
Institute of Computer Science, Warsaw University of Technology
  
jaroslaw.chudziak@pw.edu.pl

###### Abstract

Quantitative trading strategies rely on accurately ranking stocks to identify profitable investments. Effective portfolio management requires models that can reliably order future stock returns. Transformer models are promising for understanding financial time series, but how different training loss functions affect their ability to rank stocks well is not yet fully understood.
Financial markets are challenging due to their changing nature and complex relationships between stocks. Standard loss functions, which aim for simple prediction accuracy, often aren’t enough. They don’t directly teach models to learn the correct order of stock returns. While many advanced ranking losses exist from fields such as information retrieval, there hasn’t been a thorough comparison to see how well they work for ranking financial returns, especially when used with modern Transformer models for stock selection.
This paper addresses this gap by systematically evaluating a diverse set of advanced loss functions including pointwise, pairwise, listwise for daily stock return forecasting to facilitate rank-based portfolio selection on S&\&P 500 data. We focus on assessing how each loss function influences the model’s ability to discern profitable relative orderings among assets.
Our research contributes a comprehensive benchmark revealing how different loss functions impact a model’s ability to learn cross-sectional and temporal patterns crucial for portfolio selection, thereby offering practical guidance for optimizing ranking-based trading strategies.

*Keywords* Loss Functions ⋅\cdot
Stock Ranking ⋅\cdot
Quantitative Trading ⋅\cdot
Transformer Architecture ⋅\cdot
Portfolio Optimization ⋅\cdot
Deep Learning

## 1 Introduction

Quantitative trading strategies now use advanced machine learning models to find profitable investment opportunities in financial markets (Lucas Coelho e Silva, [2024](https://arxiv.org/html/2510.14156v1#bib.bib1); Zhang et al., [2024](https://arxiv.org/html/2510.14156v1#bib.bib2)). These models help traders make better decisions by analyzing complex market data and predicting which stocks will perform well.
One key task in portfolio management (Bańka and Chudziak, [2025a](https://arxiv.org/html/2510.14156v1#bib.bib3)) is ranking stocks based on how well they are expected to perform in the future (Ma and Tan, [2022](https://arxiv.org/html/2510.14156v1#bib.bib4)). Getting this ranking right is crucial because it directly affects how money is allocated across different stocks. This allocation decision determines both the profits and risks of the final portfolio (Perrin and Roncalli, [2019](https://arxiv.org/html/2510.14156v1#bib.bib5)).
Traditional statistical models, such as ARIMA, have been used for financial time series analysis and forecasting for many years (Siami-Namini and Namin, [2018](https://arxiv.org/html/2510.14156v1#bib.bib6)). However, deep learning models, especially Transformer architectures (Vaswani et al., [2023](https://arxiv.org/html/2510.14156v1#bib.bib7)), offer new possibilities. They excel in capturing complex patterns and long-range dependencies in sequential data (Liu and Wang, [2024](https://arxiv.org/html/2510.14156v1#bib.bib8)). This makes them well suited for analyzing financial time series data, where it is important to understand trends and relationships between different assets (Lim et al., [2020](https://arxiv.org/html/2510.14156v1#bib.bib9)).

Financial markets are difficult to predict because they are noisy, relationships between assets change over time, and the patterns that drive stock prices are subtle and constantly evolving (Tsay, [2005](https://arxiv.org/html/2510.14156v1#bib.bib10); de Prado, [2018](https://arxiv.org/html/2510.14156v1#bib.bib11); Wang et al., [2025](https://arxiv.org/html/2510.14156v1#bib.bib12)). Therefore, to successfully apply Transformers to financial forecasting, both the structure of the model and the way the model learns from the data must be carefully designed.

The way a model learns is controlled by its loss function (Wang et al., [2022a](https://arxiv.org/html/2510.14156v1#bib.bib13)). This function defines the prediction error that the model tries to minimize during training. For stock ranking tasks, correctly identifying which stocks will outperform others is more important than predicting exact future returns with perfect accuracy (Wang et al., [2022b](https://arxiv.org/html/2510.14156v1#bib.bib14)). A model that makes small prediction errors but gets the ranking wrong may be less useful than one that makes larger errors but correctly identifies the best investment opportunities.
While advanced ranking-oriented loss functions categorized as pointwise, pairwise, and listwise have been extensively studied and successfully applied in fields like information retrieval (Liu, [2009](https://arxiv.org/html/2510.14156v1#bib.bib15)) and more recently in tasks like Neural Architecture Search (NAS) performance prediction (Ji et al., [2024a](https://arxiv.org/html/2510.14156v1#bib.bib16)), their evaluation and adaptation for financial stock ranking using Transformer models remain underexplored.

To address this gap, we conduct a comprehensive study of different loss functions for training Transformer based architecture (PortfolioMASTER, inspired by Li et al. ([2023](https://arxiv.org/html/2510.14156v1#bib.bib17))) for daily stock return ranking on S&\&P 500 data. Our goal is to understand how different loss functions affect the model’s ability to learn patterns in stock data and generate profitable rankings.
This investigation contributes a comprehensive benchmark of pointwise, pairwise, listwise, and weighted ranking loss functions for Transformer based stock selection. The results offer insights into how different loss functions influence the model’s ability to leverage cross-sectional relationships between stocks and temporal patterns for effective portfolio selection.
By clarifying the relationship between loss function choice and portfolio performance, this study provides clearer direction for developing more effective deep learning models for quantitative finance.

## 2 Related work

This research intersects with several key areas: deep learning for financial forecasting, the application of Transformer models to time series, Learning-to-Rank (LTR) methodologies, and the role of specific loss functions in ranking tasks.

The use of deep learning for financial market prediction has seen significant growth. Initial explorations involved models such as Recurrent Neural Networks (RNNs), Long Short-Term Memory networks (LSTMs) (Fischer and Krauss, [2018](https://arxiv.org/html/2510.14156v1#bib.bib18)), and Convolutional Neural Networks (CNNs) (Ding et al., [2015](https://arxiv.org/html/2510.14156v1#bib.bib19); Lu et al., [2021](https://arxiv.org/html/2510.14156v1#bib.bib20)) for tasks like stock price prediction (Soni et al., [2022](https://arxiv.org/html/2510.14156v1#bib.bib21)). More recently, Transformer architectures (Vaswani et al., [2023](https://arxiv.org/html/2510.14156v1#bib.bib7)), originally designed for natural language processing, have been successfully adapted for general time series forecasting (Zhou et al., [2021](https://arxiv.org/html/2510.14156v1#bib.bib22); Fan and Shen, [2024](https://arxiv.org/html/2510.14156v1#bib.bib23); Liu et al., [2024](https://arxiv.org/html/2510.14156v1#bib.bib24); Liu and Wang, [2024](https://arxiv.org/html/2510.14156v1#bib.bib8)). Consequently, a growing body of work is now exploring the application of these Transformer models specifically within the financial domain (Bańka and Chudziak, [2025b](https://arxiv.org/html/2510.14156v1#bib.bib25); Szydłowski and Chudziak, [2024a](https://arxiv.org/html/2510.14156v1#bib.bib26); Zhao et al., [2025](https://arxiv.org/html/2510.14156v1#bib.bib27); Szydłowski and Chudziak, [2024b](https://arxiv.org/html/2510.14156v1#bib.bib28); Ji et al., [2024b](https://arxiv.org/html/2510.14156v1#bib.bib29); Li et al., [2025](https://arxiv.org/html/2510.14156v1#bib.bib30)).

Learning-to-Rank (LTR), a field predominantly developed for information retrieval (IR) tasks such as document ranking for search engines (Liu, [2009](https://arxiv.org/html/2510.14156v1#bib.bib15); Li, [2011](https://arxiv.org/html/2510.14156v1#bib.bib31)), offers three main strategies: pointwise, pairwise, and listwise. The pointwise approach treats ranking as a regression or classification problem on individual items, predicting a score for each, which then dictates the final order (Cossock and Zhang, [2006](https://arxiv.org/html/2510.14156v1#bib.bib32)). In contrast, the pairwise approach focuses on the relative order of item pairs. The model learns to predict whether item ii should be ranked higher than item jj. Loss functions like RankNet (Burges et al., [2005](https://arxiv.org/html/2510.14156v1#bib.bib33)), Margin Ranking Loss (Herbrich et al., [2000](https://arxiv.org/html/2510.14156v1#bib.bib34)), and Bayesian Personalized Ranking (BPR) (Rendle et al., [2012](https://arxiv.org/html/2510.14156v1#bib.bib35)) fall into this category. Finally, the listwise approach considers the entire list of items as a single instance for training and directly optimizes a measure of the quality of the entire ranked list (Saha et al., [2021](https://arxiv.org/html/2510.14156v1#bib.bib36)), with examples such as ListNet (Cao et al., [2007](https://arxiv.org/html/2510.14156v1#bib.bib37)) and ListMLE (Xia et al., [2008](https://arxiv.org/html/2510.14156v1#bib.bib38)).

The critical role of the loss function in ranking tasks extends beyond IR. For instance, in Neural Architecture Search (NAS), performance predictors are used to estimate the effectiveness of candidate neural architectures. Recent studies have shown Ji et al. ([2024a](https://arxiv.org/html/2510.14156v1#bib.bib16)) that replacing standard Mean Squared Error (MSE) with pairwise or listwise ranking losses significantly improves the predictors ability to identify top performing architectures. Ji et al. ([2024a](https://arxiv.org/html/2510.14156v1#bib.bib16)) benchmarked 11 ranking losses for NAS, concluding that the choice of loss function affects predictor quality and that rank metrics are strong indicators for discovering optimal architectures.

Furthermore, specialized loss functions like WARP loss (Weston et al., [2011](https://arxiv.org/html/2510.14156v1#bib.bib39)) and LambdaLoss (Wang et al., [2018](https://arxiv.org/html/2510.14156v1#bib.bib40)) have been developed in IR to improve how models rank results, showing that choosing the right loss function for the task can improve performance. Our work aims to bridge the gap by systematically evaluating a range of these ranking loss functions for Transformer based stock selection.

## 3 Methodology

In this chapter, we explain the methodological approach for our study. We begin by defining the stock ranking task, then describe the Transformer architecture used for prediction, and finally, we present the different loss functions we tested, which are the core subject of this analysis.

Table 1: Overview of Investigated Loss Functions and their Key Components. For Combined Losses, LPairwiseComp.L\_{\text{PairwiseComp.}} is shown, which is used in Eq. [2](https://arxiv.org/html/2510.14156v1#S3.E2 "In 3.3 Investigated Loss Functions ‣ 3 Methodology ‣ On Evaluating Loss Functions for Stock Ranking: An Empirical Analysis With Transformer Model"). Normalization over pairs (e.g., 1/|Pvalid|1/|P\_{\text{valid}}|) is applied. Let si​j=sign​(yi−yj)s\_{ij}=\text{sign}(y\_{i}-y\_{j}).

|  |  |  |  |
| --- | --- | --- | --- |
| Loss Name | Category | Core Component Formula | Tunable Params |
| MSE (Baseline) | Pointwise | LMSE​(𝐲^,𝐲)L\_{\text{MSE}}(\hat{\mathbf{y}},\mathbf{y}) (see Eq. [1](https://arxiv.org/html/2510.14156v1#S3.E1 "In 3.3 Investigated Loss Functions ‣ 3 Methodology ‣ On Evaluating Loss Functions for Stock Ranking: An Empirical Analysis With Transformer Model")) | None |
| Combined Losses (Pairwise Component LPairwiseComp.L\_{\text{PairwiseComp.}} shown) | | | |
| Hinge | Pointwise + Pairwise | ∑(i,j)∈Pvalidmax⁡(0,m−si​j​(y^i−y^j))\sum\_{(i,j)\in P\_{\text{valid}}}\max(0,m-s\_{ij}(\hat{y}\_{i}-\hat{y}\_{j})) | λ\lambda, margin mm |
| Margin | Pointwise + Pairwise | ∑(i,j)∈Pvalidmax⁡(0,−si​j​(y^i−y^j)+m)\sum\_{(i,j)\in P\_{\text{valid}}}\max(0,-s\_{ij}(\hat{y}\_{i}-\hat{y}\_{j})+m) | λ\lambda, margin mm |
| BPR | Pointwise + Pairwise | ∑{(i,j)∣yi>yj}log⁡(1+exp⁡(−(y^i−y^j)))\sum\_{\{(i,j)\mid y\_{i}>y\_{j}\}}\log(1+\exp(-(\hat{y}\_{i}-\hat{y}\_{j}))) | λ\lambda |
| RankNet | Pointwise + Pairwise | ∑(i,j)∈Pvalidlog⁡(1+exp⁡(−α⋅si​j​(y^i−y^j)))\sum\_{(i,j)\in P\_{\text{valid}}}\log(1+\exp(-\alpha\cdot s\_{ij}(\hat{y}\_{i}-\hat{y}\_{j}))) | λ\lambda, scale α\alpha |
| WHR1/WHR2 | Pointwise + Pairwise (Weighted Hinge) | ∑(i,j)∈Pvalidwi​wj​max⁡(0,m−si​j​(y^i−y^j))\sum\_{(i,j)\in P\_{\text{valid}}}w\_{i}w\_{j}\max(0,m-s\_{ij}(\hat{y}\_{i}-\hat{y}\_{j}))   where wkWHR1/2w\_{k}^{\text{WHR1/2}} based on rank | λ\lambda, margin mm |
|  |  | where wkWHR1/2w\_{k}^{\text{WHR1/2}} based on rank |  |
| Listwise Loss | | | |
| ListNet | Listwise | LListNet​(𝐲^,𝐲;τ)L\_{\text{ListNet}}(\hat{\mathbf{y}},\mathbf{y};\tau) (see Eq. [4](https://arxiv.org/html/2510.14156v1#S3.E4 "In 3.3 Investigated Loss Functions ‣ 3 Methodology ‣ On Evaluating Loss Functions for Stock Ranking: An Empirical Analysis With Transformer Model")) | Temperature τ\tau |

### 3.1 Problem Definition

Quantitative portfolio selection aims to optimize asset allocation by predicting future stock returns and then ranking stocks from best to worst based on their expected performance. The predictive model is trained to capture temporal and cross-sectional stock behaviors by minimizing a specific loss function, LjL\_{j}. The choice of LjL\_{j} fundamentally shapes how the model interprets error and what relationships it prioritizes. However, while many advanced ranking losses exist, their effectiveness in training modern Transformer models for this specific task remains underexplored. This paper addresses this gap by investigating the impact of various ranking loss functions on the performance of a Transformer based model for rank based stock selection.

Our core task is stock return forecasting formulated as a ranking problem Wang et al. ([2022b](https://arxiv.org/html/2510.14156v1#bib.bib14)); Xia et al. ([2024](https://arxiv.org/html/2510.14156v1#bib.bib41)). We consider a universe of NN assets. For each trading day tt, the input to our model is Xt∈ℝT×N×FX\_{t}\in\mathbb{R}^{T\times N\times F}, where TT is the lookback window, NN the number of assets, and FF the number of input features. The model, PortfolioMASTER, learns fθ,Lj:ℝT×N×F→ℝNf\_{\theta,L\_{j}}:\mathbb{R}^{T\times N\times F}\rightarrow\mathbb{R}^{N}, mapping XtX\_{t} to predicted returns R^t+1=[r^1t+1,…,r^Nt+1]\hat{R}\_{t+1}=[\hat{r}\_{1}^{t+1},\dots,\hat{r}\_{N}^{t+1}]. The parameters θ\theta are optimized by minimizing LjL\_{j} from a set of investigated losses (Section [3.3](https://arxiv.org/html/2510.14156v1#S3.SS3 "3.3 Investigated Loss Functions ‣ 3 Methodology ‣ On Evaluating Loss Functions for Stock Ranking: An Empirical Analysis With Transformer Model")). The ground truth target rit+1r\_{i}^{t+1} is the next day return for stock sis\_{i}: rit+1=(pit+1−pit)/pitr\_{i}^{t+1}=(p\_{i}^{t+1}-p\_{i}^{t})/p\_{i}^{t}, where pitp\_{i}^{t} is the closing price.

Based on R^t+1\hat{R}\_{t+1} from a model trained with LjL\_{j}, we rank stocks and select the top-kk for an equally weighted portfolio held during day t+1t+1, with daily rebalancing Xia et al. ([2024](https://arxiv.org/html/2510.14156v1#bib.bib41)). This allows isolating the influence of LjL\_{j} on portfolio performance.

### 3.2 Model Architecture

The experiments utilize the PortfolioMASTER model architecture, inspired by Li et al. ([2023](https://arxiv.org/html/2510.14156v1#bib.bib17)), adapted for stock return forecasting.
PortfolioMASTER employs alternating blocks of temporal self-attention (processing each stock’s history independently) and spatial self-attention (modeling cross-stock relationships at each time step). The input features (daily return and turnover) for each stock over a lookback window TT are first projected to a model dimension DD. Positional encoding is added before the input passes through spatio-temporal encoder layers. A final attention based temporal aggregation mechanism, characteristic of MASTER, produces a representation for each stock, which is then decoded to predict next day returns. Key hyperparameters, including model dimension, number of encoder layers, and attention heads, were selected based on performance across a predefined grid of values, tuned separately for each loss function.

### 3.3 Investigated Loss Functions

We evaluate a diverse set of loss functions to train our model, categorized as pointwise, combined pointwise-pairwise, and listwise. Let 𝐲=[y1,…,yN]\mathbf{y}=[y\_{1},\dots,y\_{N}] be the true next-day returns and 𝐲^=[y^1,…,y^N]\hat{\mathbf{y}}=[\hat{y}\_{1},\dots,\hat{y}\_{N}] the model’s predictions. An overview of these functions is presented in Table [1](https://arxiv.org/html/2510.14156v1#S3.T1 "Table 1 ‣ 3 Methodology ‣ On Evaluating Loss Functions for Stock Ranking: An Empirical Analysis With Transformer Model").

The baseline pointwise loss is Mean Squared Error (MSE):

|  |  |  |  |
| --- | --- | --- | --- |
|  | LMSE​(𝐲^,𝐲)=1N​∑i=1N(y^i−yi)2.L\_{\text{MSE}}(\hat{\mathbf{y}},\mathbf{y})=\frac{1}{N}\sum\_{i=1}^{N}(\hat{y}\_{i}-y\_{i})^{2}. |  | (1) |

Combined losses integrate MSE with a pairwise component LPairwiseComponentL\_{\text{PairwiseComponent}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | LCombined=(1−λ)⋅LMSE+λ⋅LPairwiseComponent,L\_{\text{Combined}}=(1-\lambda)\cdot L\_{\text{MSE}}+\lambda\cdot L\_{\text{PairwiseComponent}}, |  | (2) |

where λ∈[0,1]\lambda\in[0,1] is a weighting hyperparameter. Pairwise components are typically summed over the set of valid pairs Pvalid={(i,j)∣i≠j,yi≠yj}P\_{\text{valid}}=\{(i,j)\mid i\neq j,y\_{i}\neq y\_{j}\} and then normalized by dividing by |Pvalid||P\_{\text{valid}}|.
The specific pairwise components investigated include Hinge, Margin Ranking, Bayesian Personalized Ranking (BPR), and RankNet. Additionally, we explore two Weighted Hinge variants (WHR1/WHR2), which assign greater importance to top-ranked stocks by applying weights based on rank wkw\_{k} to the Hinge loss terms; WHR1 uses a linear weighting scheme based on rank, while WHR2 uses an exponential one.
Detailed formulas for these components are in Table [1](https://arxiv.org/html/2510.14156v1#S3.T1 "Table 1 ‣ 3 Methodology ‣ On Evaluating Loss Functions for Stock Ranking: An Empirical Analysis With Transformer Model").

The listwise approach, ListNet, calculates cross-entropy between softmax-transformed true and predicted scores. First, for both the true scores 𝐲\mathbf{y} and predicted scores 𝐲^\hat{\mathbf{y}}, probability distributions are computed. For a generic score vector 𝐱\mathbf{x} (which will be either 𝐲\mathbf{y} or 𝐲^\hat{\mathbf{y}}), the probability of item kk is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P𝐱​(k;τ)=exp⁡(xk/τ)∑j=1Nexp⁡(xj/τ),P\_{\mathbf{x}}(k;\tau)=\frac{\exp(x\_{k}/\tau)}{\sum\_{j=1}^{N}\exp(x\_{j}/\tau)}, |  | (3) |

where τ\tau is a temperature parameter. The ListNet loss is then the cross-entropy between P𝐲​(k;τ)P\_{\mathbf{y}}(k;\tau) and P𝐲^​(k;τ)P\_{\hat{\mathbf{y}}}(k;\tau):

|  |  |  |  |
| --- | --- | --- | --- |
|  | LListNet​(𝐲^,𝐲;τ)=−∑k=1NP𝐲​(k;τ)​log⁡(P𝐲^​(k;τ)).L\_{\text{ListNet}}(\hat{\mathbf{y}},\mathbf{y};\tau)=-\sum\_{k=1}^{N}P\_{\mathbf{y}}(k;\tau)\log(P\_{\hat{\mathbf{y}}}(k;\tau)). |  | (4) |

An overview of all investigated functions and their specific pairwise components is presented in Table [1](https://arxiv.org/html/2510.14156v1#S3.T1 "Table 1 ‣ 3 Methodology ‣ On Evaluating Loss Functions for Stock Ranking: An Empirical Analysis With Transformer Model").

## 4 Experimental Setup

Dataset and Features. We use daily stock market data for N=110N=110 S&\&P 500 stocks, selected as the top 10 by market capitalization from each of the 11 GICS sectors. The data spans from 2015-01-03 to 2024-12-03. The input features (F=2F=2) for each stock are its daily return and daily turnover (volume/price), normalized per stock using scalers from the training set. We use a lookback window of T=20T=20 trading days.

Training and Evaluation. The data is split chronologically: 70% for training, 15% for validation, and 15% for testing.
Models are trained for up to 50 epochs using the AdamW optimizer with weight decay, employing early stopping based on validation loss and a learning rate scheduler. For each investigated loss function, hyperparameters (including model parameters like dropout, dm​o​d​e​ld\_{model}, df​fd\_{ff}, learning rate, and loss specific parameters like λ\lambda, margin mm, scale α\alpha, or temperature TT) were tuned via grid search, minimizing the respective loss on the validation set.

Portfolio Simulation and Metrics. We simulate a daily rebalanced, long only, top-kk portfolio (k=5k=5) with equal weighting. Performance is evaluated using:

* •

  Portfolio Metrics: Cumulative Return (CR), Annualized Return (AR), Annualized Volatility (AV), Annualized Sharpe Ratio (SR, with a risk-free rate of 4.3%), and Maximum Drawdown (MDD).
* •

  Predictive Quality Metrics: Mean daily cross sectional Spearman Information Coefficient (IC Spearman), its Information Ratio (ICIR Spearman) and Precision@5 (P@5, fraction of top-5 predicted stocks with positive actual returns). The test set loss (MSE) is also reported.

## 5 Results and Discussion

Table 2: Performance Metrics for PortfolioMASTER Trained with Different Loss Functions on the S&\&P 500 Test Set (Top-5 Stocks).

| Loss Function | CR(%) | AR(%) | AV(%) | SR | MDD(%) | IC(Sp.) | Std IC(Sp.) | ICIR(Sp.) | P@5 | TestLoss(MSE) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MSE | 79.28 | 14.78 | 15.79 | 0.6637 | -19.58 | 0.0754 | 0.0994 | 8.8076 | 0.3576 | 0.00286 |
| Hinge | 82.90 | 15.33 | 15.79 | 0.6984 | -19.58 | 0.0762 | 0.0991 | 8.8432 | 0.3586 | 0.00301 |
| Margin | 89.07 | 16.23 | 15.85 | 0.7529 | -18.33 | 0.0758 | 0.0989 | 8.8520 | 0.3593 | 0.00632 |
| BPR | 85.68 | 15.74 | 15.89 | 0.7200 | -15.77 | 0.0733 | 0.1005 | 8.6915 | 0.3578 | 0.01145 |
| RankNet | 80.78 | 15.01 | 15.82 | 0.6771 | -18.97 | 0.0767 | 0.0991 | 8.8422 | 0.3586 | 0.01909 |
| WHR1 | 82.40 | 15.25 | 15.78 | 0.6938 | -19.54 | 0.0763 | 0.0991 | 8.8448 | 0.3593 | 0.00352 |
| WHR2 | 81.84 | 15.17 | 15.83 | 0.6866 | -19.74 | 0.0764 | 0.0991 | 8.8470 | 0.3582 | 0.00300 |
| ListNet | 87.41 | 16.00 | 15.79 | 0.7407 | -18.36 | 0.0761 | 0.0990 | 8.8482 | 0.3595 | 1.01212 |

We evaluated the PortfolioMASTER model trained with eight different loss function configurations on the S&P 500 test set. Table [2](https://arxiv.org/html/2510.14156v1#S5.T2 "Table 2 ‣ 5 Results and Discussion ‣ On Evaluating Loss Functions for Stock Ranking: An Empirical Analysis With Transformer Model") summarizes the portfolio performance and predictive quality metrics.

Portfolio Performance Analysis.
Our results show that the choice of loss function significantly impacts portfolio performance. The Margin loss achieved the highest Annualized Return (16.23%) and Sharpe Ratio (0.7529). ListNet also performed strongly, with an AR of 16.00% and SR of 0.7407, along with the lowest Annualized Volatility (15.79%).
Notably, BPR yielded the lowest Maximum Drawdown (-15.77%), suggesting that models trained with this objective offer better risk control, despite a slightly lower SR (0.7200). The baseline MSE performed reasonably, but was outperformed by several ranking oriented losses in terms of risk adjusted returns. The weighted hinge variants (WHR1, WHR2) and the standard Hinge loss offered incremental improvements over MSE but did not reach the overall portfolio profitability of Margin, ListNet, or BPR for this top-5 strategy.

Predictive Quality vs. Portfolio Outcomes.
An interesting finding is that the predictive quality metrics were quite consistent across most loss functions. For instance, IC Spearman (measure of ranking quality) hovered around 0.073-0.077, and P@5 was consistently near 0.358-0.359. RankNet achieved the highest IC Spearman (0.0767), yet its portfolio AR and SR were only moderate. Conversely, Margin and ListNet, which excelled in portfolio metrics, did not show markedly superior ICs scores. This suggests that while a certain level of predictive ranking ability is necessary, the specific design of the loss function plays a crucial role in translating these predictive signals into profitable portfolio decisions. This is particularly true regarding how the loss function penalizes different types of ranking errors or which parts of the rank distribution it emphasizes. The high test set loss (MSE) for ListNet is expected, as it does not directly optimize for the accuracy of return value predictions but rather for the quality of the entire ranked list.

Impact of Loss Function Design.
Pairwise losses that explicitly model preferences or margins between stocks (Margin, BPR) appear to be effective. The Margin loss, by enforcing a margin for correctly ranked pairs, might encourage the model to make more confident distinctions between stocks, leading to better top-k selections. ListNet, by considering the entire list, may capture more global ranking patterns that are beneficial for portfolio construction. The effectiveness of BPR in reducing draw downs could stem from its focus on correctly ordering preferred (better-performing) items, potentially leading to more stable top-k selections during volatile market periods.

## 6 Conclusion

Our research shows that the choice of specific loss function used to train Transformer model for ranking stocks affects how well an investment portfolio performs. While standard MSE loss offers a good starting point, more advanced loss functions designed for ranking especially Margin, ListNet and BPR can achieve better returns when considering risk, and also offer improved protection against large losses.

We observed that strong portfolio performance does not always directly correlate with the highest scores on standard predictive quality metrics. This highlights that the loss function’s ability to shape decision making for top-k selection is paramount.
We contribute a comprehensive benchmark that clearly demonstrates how different loss functions impact a Transformer model’s ability to learn and translate predictive signals into profitable, rank based stock selection strategies. These findings offer practical guidance for both researchers and practitioners: carefully choosing and adjusting ranking-specific loss functions is a vital step in creating more effective quantitative trading strategies using Transformer models.

Future work could extend this analysis in several key directions. This includes investigating a wider range of listwise loss functions and developing methods for the automated tuning of weights in combined loss functions. Furthermore, the generalizability of our findings should be validated on a larger dataset, such as the full list of S&\&P 500 stocks, and tested under different market conditions or with different rules for building portfolios.

## 7 GenAI Usage Disclosure

The authors acknowledge the use of generative AI tools (specifically ChatGPT and Gemini models) during the preparation of this manuscript for assistance with text generation, code adaptation, and language refinement. All generated content was reviewed and edited by the authors to ensure accuracy and alignment with the research presented.

## References

* Lucas Coelho e Silva [2024]

  Paulo Andre L. Castro Lucas Coelho e Silva, Gustavo de Freitas Fonseca.
  Transformers and attention-based networks in quantitative trading: a comprehensive survey, 2024.
* Zhang et al. [2024]

  Zhaofeng Zhang, Banghao Chen, Shengxin Zhu, and Nicolas Langrené.
  Quantformer: from attention to profit with a quantitative transformer trading strategy, 2024.
  URL <https://arxiv.org/abs/2404.00424>.
* Bańka and Chudziak [2025a]

  Feliks Bańka and Jarosław A. Chudziak.
  Deltahedge: A multi-agent framework for portfolio options optimization.
  In *PACIS 2025 Proceedings*, number 25, 2025a.
  URL <https://aisel.aisnet.org/pacis2025/aiandml/aiandml/25>.
  Available at AIS Electronic Library (AISeL).
* Ma and Tan [2022]

  Tao Ma and Ying Tan.
  Stock ranking with multi-task learning.
  *Expert Systems with Applications*, 199:116886, 2022.
  ISSN 0957-4174.
  doi:[https://doi.org/10.1016/j.eswa.2022.116886](https://doi.org/https://doi.org/10.1016/j.eswa.2022.116886).
  URL <https://www.sciencedirect.com/science/article/pii/S0957417422003293>.
* Perrin and Roncalli [2019]

  Sarah Perrin and Thierry Roncalli.
  Machine learning optimization algorithms and portfolio allocation, 2019.
  URL <https://arxiv.org/abs/1909.10233>.
* Siami-Namini and Namin [2018]

  Sima Siami-Namini and Akbar Siami Namin.
  Forecasting economics and financial time series: Arima vs. lstm, 2018.
  URL <https://arxiv.org/abs/1803.06386>.
* Vaswani et al. [2023]

  Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin.
  Attention is all you need, 2023.
  URL <https://arxiv.org/abs/1706.03762>.
* Liu and Wang [2024]

  Xinhe Liu and Wenmin Wang.
  Deep time series forecasting models: A comprehensive survey, 05 2024.
* Lim et al. [2020]

  Bryan Lim, Sercan O. Arik, Nicolas Loeff, and Tomas Pfister.
  Temporal fusion transformers for interpretable multi-horizon time series forecasting, 2020.
  URL <https://arxiv.org/abs/1912.09363>.
* Tsay [2005]

  Ruey S. Tsay.
  *Analysis of financial time series*.
  Wiley series in probability and statistics. Wiley-Interscience, Hoboken, NJ, 2. ed. edition, 2005.
  ISBN 978-0-471-69074-0.
  URL <http://gso.gbv.de/DB=2.1/CMD?ACT=SRCHA&SRT=YOP&IKT=1016&TRM=ppn+483463442&sourceid=fbw_bibsonomy>.
* de Prado [2018]

  Marcos Lopez de Prado.
  *Advances in Financial Machine Learning*.
  Wiley Publishing, 1st edition, 2018.
  ISBN 1119482089.
* Wang et al. [2025]

  Chaoyang Wang, Guangyu Liu, and Ling Zhu.
  Diffusion model based on stochastic differential equation with transformer for stock price prediction.
  *Applied Soft Computing*, 184:113763, 2025.
  ISSN 1568-4946.
  doi:[https://doi.org/10.1016/j.asoc.2025.113763](https://doi.org/https://doi.org/10.1016/j.asoc.2025.113763).
  URL <https://www.sciencedirect.com/science/article/pii/S1568494625010762>.
* Wang et al. [2022a]

  Qi Wang, Yue Ma, Kun Zhao, and Yingjie Tian.
  A comprehensive survey of loss functions in machine learning.
  *Annals of Data Science*, 9, 04 2022a.
  doi:[10.1007/s40745-020-00253-5](https://doi.org/10.1007/s40745-020-00253-5).
* Wang et al. [2022b]

  Heyuan Wang, Tengjiao Wang, Shun Li, Jiayi Zheng, Shijie Guan, and Wei Chen.
  Adaptive long-short pattern transformer for stock investment selection, 07 2022b.
* Liu [2009]

  Tie-Yan Liu.
  Learning to rank for information retrieval.
  *Found. Trends Inf. Retr.*, 3(3):225–331, March 2009.
  ISSN 1554-0669.
  doi:[10.1561/1500000016](https://doi.org/10.1561/1500000016).
  URL <https://doi.org/10.1561/1500000016>.
* Ji et al. [2024a]

  Han Ji, Yuqi Feng, Jiahao Fan, and Yanan Sun.
  Evaluating ranking loss functions in performance predictor for NAS, 2024a.
  URL <https://openreview.net/forum?id=4o4fDJL6I7>.
* Li et al. [2023]

  Tong Li, Zhaoyang Liu, Yanyan Shen, Xue Wang, Haokun Chen, and Sen Huang.
  Master: Market-guided stock transformer for stock price forecasting, 2023.
  URL <https://arxiv.org/abs/2312.15235>.
* Fischer and Krauss [2018]

  Thomas Fischer and Christopher Krauss.
  Deep learning with long short-term memory networks for financial market predictions, 2018.
  ISSN 0377-2217.
  URL <https://www.sciencedirect.com/science/article/pii/S0377221717310652>.
* Ding et al. [2015]

  Xiao Ding, Yue Zhang, Ting Liu, and Junwen Duan.
  Deep learning for event-driven stock prediction.
  In *Proceedings of the 24th International Conference on Artificial Intelligence*, IJCAI’15, page 2327–2333. AAAI Press, 2015.
  ISBN 9781577357384.
* Lu et al. [2021]

  Wenjie Lu, Jiazheng Li, Jingyang Wang, and Lele Qin.
  A cnn-bilstm-am method for stock price prediction.
  *Neural Comput. Appl.*, 33(10):4741–4753, May 2021.
  ISSN 0941-0643.
  doi:[10.1007/s00521-020-05532-z](https://doi.org/10.1007/s00521-020-05532-z).
  URL <https://doi.org/10.1007/s00521-020-05532-z>.
* Soni et al. [2022]

  Payal Soni, Yogya Tewari, and Deepa Krishnan.
  Machine learning approaches in stock price prediction: A systematic review.
  *Journal of Physics: Conference Series*, 2161(1):012065, jan 2022.
  doi:[10.1088/1742-6596/2161/1/012065](https://doi.org/10.1088/1742-6596/2161/1/012065).
  URL <https://dx.doi.org/10.1088/1742-6596/2161/1/012065>.
* Zhou et al. [2021]

  Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong, and Wancai Zhang.
  Informer: Beyond efficient transformer for long sequence time-series forecasting, 2021.
  URL <https://arxiv.org/abs/2012.07436>.
* Fan and Shen [2024]

  Jinyong Fan and Yanyan Shen.
  Stockmixer: a simple yet strong mlp-based architecture for stock price forecasting, 2024.
  URL <https://doi.org/10.1609/aaai.v38i8.28681>.
* Liu et al. [2024]

  Yong Liu, Tengge Hu, Haoran Zhang, Haixu Wu, Shiyu Wang, Lintao Ma, and Mingsheng Long.
  itransformer: Inverted transformers are effective for time series forecasting, 2024.
  URL <https://arxiv.org/abs/2310.06625>.
* Bańka and Chudziak [2025b]

  Feliks Bańka and Jarosław A. Chudziak.
  Applying informer for option pricing: A transformer-based approach.
  In *Proceedings of the 17th International Conference on Agents and Artificial Intelligence - Volume 3: ICAART*, pages 1270–1277. INSTICC, SciTePress, 2025b.
  ISBN 978-989-758-737-5.
  doi:[10.5220/0013320900003890](https://doi.org/10.5220/0013320900003890).
* Szydłowski and Chudziak [2024a]

  Kamil Ł. Szydłowski and Jarosław A. Chudziak.
  Hidformer: Transformer-style neural network in stock price forecasting, 2024a.
  URL <https://arxiv.org/abs/2412.19932>.
* Zhao et al. [2025]

  Siqiao Zhao, Zhikang Dong, Zeyu Cao, and Raphael Douady.
  Hedge fund portfolio construction using polymodel theory and itransformer, 2025.
  URL <https://arxiv.org/abs/2408.03320>.
* Szydłowski and Chudziak [2024b]

  Kamil Ł. Szydłowski and Jarosław A. Chudziak.
  Toward predictive stock trading with hidformer integrated into reinforcement learning strategy.
  In *2024 IEEE 36th International Conference on Tools with Artificial Intelligence (ICTAI)*, pages 213–220, 2024b.
  doi:[10.1109/ICTAI62512.2024.00039](https://doi.org/10.1109/ICTAI62512.2024.00039).
* Ji et al. [2024b]

  Yi Ji, Yuxuan Luo, Aixia Lu, Duanyang Xia, Lixia Yang, and Alan Wee-Chung Liew.
  Galformer: a transformer with generative decoding and a hybrid loss function for multi-step stock market index prediction.
  *Scientific Reports*, 14(1):23762, October 2024b.
  ISSN 2045-2322.
  doi:[10.1038/s41598-024-72045-3](https://doi.org/10.1038/s41598-024-72045-3).
  URL <https://doi.org/10.1038/s41598-024-72045-3>.
* Li et al. [2025]

  Xiuyu Li, Chenrui Bian, Xiong Li, Shiyuan Yu, and Botao Jiang.
  Lamformer: Lstm-enhanced agent attention and mixture-of-experts transformer for efficient stock price prediction.
  *International Journal of Machine Learning and Cybernetics*, July 2025.
  ISSN 1868-808X.
  doi:[10.1007/s13042-025-02740-8](https://doi.org/10.1007/s13042-025-02740-8).
  URL <https://doi.org/10.1007/s13042-025-02740-8>.
* Li [2011]

  Hang Li.
  A short introduction to learning to rank.
  *IEICE Trans. Inf. Syst.*, 94-D:1854–1862, 2011.
  URL <https://api.semanticscholar.org/CorpusID:9997448>.
* Cossock and Zhang [2006]

  David Cossock and Tong Zhang.
  Subset ranking using regression.
  In *Proceedings of the 19th Annual Conference on Learning Theory*, COLT’06, page 605–619, Berlin, Heidelberg, 2006. Springer-Verlag.
  ISBN 3540352945.
  doi:[10.1007/11776420\_44](https://doi.org/10.1007/11776420_44).
  URL <https://doi.org/10.1007/11776420_44>.
* Burges et al. [2005]

  Chris Burges, Tal Shaked, Erin Renshaw, Ari Lazier, Matt Deeds, Nicole Hamilton, and Greg Hullender.
  Learning to rank using gradient descent.
  In *Proceedings of the 22nd International Conference on Machine Learning*, ICML ’05, page 89–96, New York, NY, USA, 2005. Association for Computing Machinery.
  ISBN 1595931805.
  doi:[10.1145/1102351.1102363](https://doi.org/10.1145/1102351.1102363).
  URL <https://doi.org/10.1145/1102351.1102363>.
* Herbrich et al. [2000]

  Ralf Herbrich, Thore Graepel, and Klaus Obermayer.
  Large margin rank boundaries for ordinal regression.
  *Advances in Large Margin Classifiers*, 88, 01 2000.
* Rendle et al. [2012]

  Steffen Rendle, Christoph Freudenthaler, Zeno Gantner, and Lars Schmidt-Thieme.
  Bpr: Bayesian personalized ranking from implicit feedback, 2012.
  URL <https://arxiv.org/abs/1205.2618>.
* Saha et al. [2021]

  Suman Saha, Junbin Gao, and Richard Gerlach.
  Stock ranking prediction using list-wise approach and node embedding technique.
  *IEEE Access*, 9:88981–88996, 2021.
  doi:[10.1109/ACCESS.2021.3090834](https://doi.org/10.1109/ACCESS.2021.3090834).
* Cao et al. [2007]

  Zhe Cao, Tao Qin, Tie-Yan Liu, Ming-Feng Tsai, and Hang Li.
  Learning to rank: from pairwise approach to listwise approach.
  In *Proceedings of the 24th International Conference on Machine Learning*, ICML ’07, page 129–136, New York, NY, USA, 2007. Association for Computing Machinery.
  ISBN 9781595937933.
  doi:[10.1145/1273496.1273513](https://doi.org/10.1145/1273496.1273513).
  URL <https://doi.org/10.1145/1273496.1273513>.
* Xia et al. [2008]

  Fen Xia, Tie-Yan Liu, Jue Wang, Wensheng Zhang, and Hang Li.
  Listwise approach to learning to rank - theory and algorithm.
  pages 1192–1199, 01 2008.
  doi:[10.1145/1390156.1390306](https://doi.org/10.1145/1390156.1390306).
* Weston et al. [2011]

  Jason Weston, Samy Bengio, and Nicolas Usunier.
  Wsabie: scaling up to large vocabulary image annotation.
  In *Proceedings of the Twenty-Second International Joint Conference on Artificial Intelligence - Volume Volume Three*, IJCAI’11, page 2764–2770. AAAI Press, 2011.
  ISBN 9781577355151.
* Wang et al. [2018]

  Xuanhui Wang, Cheng Li, Nadav Golbandi, Michael Bendersky, and Marc Najork.
  The lambdaloss framework for ranking metric optimization.
  In *Proceedings of the 27th ACM International Conference on Information and Knowledge Management*, CIKM ’18, page 1313–1322, New York, NY, USA, 2018. Association for Computing Machinery.
  ISBN 9781450360142.
  doi:[10.1145/3269206.3271784](https://doi.org/10.1145/3269206.3271784).
  URL <https://doi.org/10.1145/3269206.3271784>.
* Xia et al. [2024]

  Hongjie Xia, Huijie Ao, Long Li, Yu Liu, Sen Liu, Guangnan Ye, and Hongfeng Chai.
  Ci-sthpan: Pre-trained attention network for stock selection with channel-independent spatio-temporal hypergraph, 03 2024.