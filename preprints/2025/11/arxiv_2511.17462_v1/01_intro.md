---
authors:
- Ryan Engel
- Yu Chen
- Pawel Polak
- Ioana Boier
doc_id: arxiv:2511.17462v1
family_id: arxiv:2511.17462
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware
  Factor Selection
url_abs: http://arxiv.org/abs/2511.17462v1
url_html: https://arxiv.org/html/2511.17462v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ryan Engel
[Ryan.m.engel@stonybrook.edu](mailto:Ryan.m.engel@stonybrook.edu)
Stony Brook UniversityDepartment of Computer ScienceUSA
, 
Yu Chen
[Yu.Chen.7@stonybrook.edu](mailto:Yu.Chen.7@stonybrook.edu)
Stony Brook UniversityDepartment of Applied Mathematics and StatisticsUSA
, 
Pawel Polak
[Pawel.Polak@stonybrook.edu](mailto:Pawel.Polak@stonybrook.edu)
Stony Brook UniversityDepartment of Applied Mathematics and StatisticsUSA
 and 
Ioana Boier
[iboier@nvidia.com](mailto:iboier@nvidia.com)
NVIDIA CorporationUSA

(2025)

###### Abstract.

Conditional Autoencoders (CAEs) offer a flexible, interpretable approach for estimating latent asset-pricing factors from firm characteristics. However, existing studies usually limit the latent factor dimension to around K=5K=5 due to concerns that larger KK can degrade performance. To overcome this challenge, we propose a scalable framework that couples a high-dimensional CAE with an uncertainty-aware factor selection procedure. We employ three models for quantile prediction: zero-shot Chronos, a pretrained time-series foundation model (ZS-Chronos), gradient-boosted quantile regression trees using XGBoost and RAPIDS (Q-Boost), and an I.I.D bootstrap-based sample mean model (IID-BS). For each model, we rank factors by forecast uncertainty and retain the top-κ\kappa most predictable factors for portfolio construction, where κ\kappa denotes the selected subset of factors. This pruning strategy delivers substantial gains in risk-adjusted performance across all forecasting models. Furthermore, due to each model’s uncorrelated predictions, a performance-weighted ensemble consistently outperforms individual models with higher Sharpe, Sortino, and Omega ratios.

Portfolio Optimization, Asset Pricing, Uncertainty Quantification, Conditional Autoencoders, Gradient Boosted Trees, Chronos Time-Series Foundation Model

††journalyear: 2025††copyright: acmlicensed††conference: 6th ACM International
Conference on AI in Finance; November 15–18, 2025; Singapore, Singapore††booktitle: 6th ACM International Conference on AI in Finance (ICAIF ’25),
November 15–18, 2025, Singapore, Singapore††doi: 10.1145/3768292.3770415††isbn: 979-8-4007-2220-2/2025/11††ccs: Computing methodologies Learning latent representations††ccs: Computing methodologies Classification and regression trees††ccs: Computing methodologies Artificial intelligence††ccs: Computing methodologies Uncertainty quantification
![Refer to caption](x1.png)


Figure 1. Architecture for Uncertainty-Aware Factor Selection. First, a CAE model extracts high-dimensional latent factor portfolios from firm characteristics. Next, time-series forecasting models generate point and quantile predictions for each factor, which are used for uncertainty quantification. Factors are then ranked by uncertainty, and the most predictable subset is selected for tangency portfolio optimization in factor space before projection to tradable asset weights.

## 1. Introduction

Understanding the cross-section of asset returns remains a central problem in empirical finance. Classical linear factor models—such as the Arbitrage Pricing Theory (APT) or Fama–French specifications—assume that asset returns are driven by a small number of latent or observable risk factors with fixed loadings across firms. While such models are theoretically elegant and provide economic interpretability, they rely on strong assumptions about linearity and stationarity, and often ignore the rich heterogeneity present in firm characteristics and evolving market regimes. Recent studies in (neuhierl2022structural), (giglio2021asset) have highlighted limitations of these approaches, especially their inability to capture dynamic, nonlinear dependencies or time-varying exposures.

To overcome these limitations, we build upon the CAE model proposed in (gu2020autoencoder), which generalizes linear factor models by allowing the factor loadings to depend nonlinearly on firm-specific lagged characteristics. The CAE jointly learns both the latent factors and characteristic-based exposures through a neural network architecture, enabling a more expressive representation of the return-generating process. This structure enhances the signal-to-noise ratio of latent factor returns and improves their out-of-sample predictive stability. Recent advances in deep latent factor models confirm the importance of modeling interactions between firm-level variables and latent risks, especially in high-dimensional financial environments (wei2025deeplatent; neuhierl2022structural).

A central modeling choice in CAEs concerns the dimensionality KK of the latent factor space. Conventional implementations typically restrict KK to small values (e.g., K≈5K\approx 5) to maintain interpretability and limit overfitting. In contrast, we operate in a high-dimensional regime (up to K=50K=50) and introduce a post-hoc filtering procedure that selects latent portfolios according to their out-of-sample predictability. For each latent factor, multiple forecasting models produce predictive distributions from which we quantify forecast uncertainty. Factors are subsequently ranked by their predictive stability, and only those with the most reliable forecasts are retained. This uncertainty-aware selection leverages the expressive capacity of high-dimensional latent representations while controlling estimation risk. By ranking factors based on predictive confidence, the procedure explicitly minimizes expected out-of-sample utility loss and thereby aligns factor selection with the downstream goal of portfolio optimization—contrasting with traditional approaches that determine KK through purely statistical reconstruction criteria.

Our contributions are both methodological and empirical. First, we introduce a novel uncertainty-aware framework for factor portfolio selection, integrating high-dimensional latent portfolios extracted via CAEs with predictive signals from multiple advanced forecasting models. Second, we show that high-dimensional CAEs, when coupled with forecast-driven factor selection, significantly outperform conventional low-dimensional factor models, achieving notably higher Sharpe, Sortino, and Omega ratios while maintaining maximum drawdowns below 10%. Third, we demonstrate that forecasts generated by zero-shot pretrained models such as Chronos (ansari2024chronos) and quantile gradient-boosted regression trees provide complementary predictive signals that substantially augment the baseline IID-based predictions typically used in CAE-based frameworks. Consequently, ensembles of these diverse forecasts yield robust, market-neutral portfolios with superior and stable out-of-sample performance. Our findings underscore the value of forecast uncertainty as a practical indicator for factor predictability, and validate the effectiveness of deep latent models combined with state-of-the-art forecasting techniques in modern asset pricing applications.

## 2. Methodology

We adopt a two-stage procedure: (i) latent factor portfolios are extracted using a CAE model trained on firm-level characteristics—such as market equity, asset growth, and past return momentum—alongside asset returns; and (ii) the time series of each latent factor is forecasted using multiple models, with forecast uncertainty guiding the selection of portfolios with predictable returns.

Let ri,s∈ℝr\_{i,s}\in\mathbb{R} denote the excess return of asset ii at time ss, and let zi,s−1∈ℝPz\_{i,s-1}\in\mathbb{R}^{P} represent its lagged firm characteristics. The CAE models asset returns as:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | ri,s=βi​(zi,s−1)⊤​fs+ui,s,r\_{i,s}=\beta\_{i}(z\_{i,s-1})^{\top}f\_{s}+u\_{i,s}, |  |

where βi​(zi,s−1)∈ℝK\beta\_{i}(z\_{i,s-1})\in\mathbb{R}^{K} is a nonlinear function mapping characteristics to factor loadings, fs∈ℝKf\_{s}\in\mathbb{R}^{K} is a vector of latent factors shared across assets, and ui,s∈ℝu\_{i,s}\in\mathbb{R} is an idiosyncratic error term. The mapping βi​(⋅)\beta\_{i}(\cdot) is parameterized as a feedforward neural network with ReLU activations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2) |  | zi,s−1(0)\displaystyle z^{(0)}\_{i,s-1} | =zi,s−1,\displaystyle=z\_{i,s-1}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3) |  | zi,s−1(ℓ)\displaystyle z^{(\ell)}\_{i,s-1} | =ReLU​(W(ℓ−1)​zi,s−1(ℓ−1)+b(ℓ−1)),ℓ=1,…,Lβ,\displaystyle=\mathrm{ReLU}\left(W^{(\ell-1)}z^{(\ell-1)}\_{i,s-1}+b^{(\ell-1)}\right),\quad\ell=1,\dots,L\_{\beta}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4) |  | βi​(zi,s−1)\displaystyle\beta\_{i}(z\_{i,s-1}) | =W(L)​zi,s−1(L)+b(L).\displaystyle=W^{(L)}z^{(L)}\_{i,s-1}+b^{(L)}. |  |

The latent factors fs∈ℝKf\_{s}\in\mathbb{R}^{K} are extracted via a cross-sectional projection of returns onto firm characteristics:

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | fs=Wf​((Zs−1⊤​Zs−1)−1​Zs−1⊤​rs),f\_{s}=W\_{f}\left((Z\_{s-1}^{\top}Z\_{s-1})^{-1}Z\_{s-1}^{\top}r\_{s}\right), |  |

where Zs−1∈ℝN×PZ\_{s-1}\in\mathbb{R}^{N\times P} denotes the matrix of lagged characteristics and Wf∈ℝK×PW\_{f}\in\mathbb{R}^{K\times P} is a time-varying projection matrix. This construction aggregates firm-level information into a small number of tradable, low-noise latent portfolios. The CAE parameters Θ={W(ℓ),b(ℓ),Wf}\Theta=\{W^{(\ell)},b^{(\ell)},W\_{f}\} are estimated jointly by minimizing the cross-sectional pricing loss over the training period:

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | minΘ​∑s=1t∑i=1N(ri,s−βi​(zi,s−1)⊤​fs)2.\min\_{\Theta}\sum\_{s=1}^{t}\sum\_{i=1}^{N}\left(r\_{i,s}-\beta\_{i}(z\_{i,s-1})^{\top}f\_{s}\right)^{2}. |  |

Once trained, the CAE produces a time series {fs(κ)}s=1t\{f\_{s}^{(\kappa)}\}\_{s=1}^{t} for each latent factor κ=1,…,K\kappa=1,\dots,K, which we use to generate one-step-ahead forecasts f^t+1(κ)∈ℝ\hat{f}\_{t+1}^{(\kappa)}\in\mathbb{R}. In addition to point forecasts, we construct a set of quantile predictions {f^t+1(κ,α)}α∈𝒬\{\hat{f}\_{t+1}^{(\kappa,\alpha)}\}\_{\alpha\in\mathcal{Q}}, where 𝒬⊂(0,1)\mathcal{Q}\subset(0,1) is a model-dependent collection of quantile levels. Forecast uncertainty for each factor κ\kappa at time t+1t+1 is then defined as the average absolute deviation of the quantile forecasts from the central prediction:

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | Ut+1,κ(κ)=1|𝒬|​∑α∈𝒬|f^t+1(κ,α)−f^t+1(κ)|.U\_{t+1,\kappa}^{(\kappa)}=\frac{1}{|\mathcal{Q}|}\sum\_{\alpha\in\mathcal{Q}}\left|\hat{f}\_{t+1}^{(\kappa,\alpha)}-\hat{f}\_{t+1}^{(\kappa)}\right|. |  |

This general formulation accommodates all forecasting models under consideration.

Using the forecast uncertainty estimates Ut+1(κ)U\_{t+1}^{(\kappa)}, we rank all KK latent factors in increasing order of uncertainty. For each integer κ∈{1,…,K}\kappa\in\{1,\dots,K\}, we construct a tangency portfolio using the κ\kappa most predictable factors. Let μt+1∈ℝκ\mu\_{t+1}\in\mathbb{R}^{\kappa} be the vector of forecasts for the κ\kappa most predictable factors and Σf∈ℝκ×κ\Sigma\_{f}\in\mathbb{R}^{\kappa\times\kappa} be the covariance matrix associated with these factors computed using sample covariance matrix. The tangency portfolio is given by wf,t=Σf−1​μt+1𝟏⊤​Σf−1​μt+1w\_{f,t}=\frac{\Sigma\_{f}^{-1}\mu\_{t+1}}{\mathbf{1}^{\top}\Sigma\_{f}^{-1}\mu\_{t+1}} which is then mapped to asset weights using ([5](https://arxiv.org/html/2511.17462v1#S2.E5 "In 2. Methodology ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection")) via:

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | wr,t=Zt​(Zt⊤​Zt)−1​Wf(κ)⊤​wf,t.w\_{r,t}=Z\_{t}(Z\_{t}^{\top}Z\_{t})^{-1}W\_{f}^{(\kappa)\top}w\_{f,t}. |  |

where Wf(κ)∈ℝκ×PW\_{f}^{(\kappa)}\in\mathbb{R}^{\kappa\times P} are the columns of the CAE trained WfW\_{f} matrix that correspond to the κ=1,2,…,K\kappa=1,2,\ldots,K selected factors.

To implement the forecasting and uncertainty estimation defined in equations ([7](https://arxiv.org/html/2511.17462v1#S2.E7 "In 2. Methodology ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection"))–([8](https://arxiv.org/html/2511.17462v1#S2.E8 "In 2. Methodology ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection")), we consider three models: a nonparametric sample-based baseline, a supervised regression-tree method, and a zero-shot pretrained foundational sequence model (see Table [1](https://arxiv.org/html/2511.17462v1#S2.T1 "Table 1 ‣ 2. Methodology ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection")).

The first model, denoted IID-BS, is analogous to the original CAE approach except that it utilizes factor selection mechanism based on forecast uncertainty. In particular, it assumes that latent factor returns {fs(κ)}s=1t\{f\_{s}^{(\kappa)}\}\_{s=1}^{t} are drawn i.i.d. from a stationary distribution. The point forecast f^t+1(κ)\hat{f}\_{t+1}^{(\kappa)} is taken to be the sample mean, computed over a rolling window of size tt f^t+1(κ)=1t​∑s=1tfs(κ).\hat{f}\_{t+1}^{(\kappa)}=\frac{1}{t}\sum\_{s=1}^{t}f\_{s}^{(\kappa)}.

To assess predictive uncertainty, we generate BB bootstrap resamples from the window and compute empirical quantiles f^t+1(κ,α)\hat{f}\_{t+1}^{(\kappa,\alpha)} at levels α∈{0.05,0.95}\alpha\in\{0.05,0.95\}. These quantiles are then used to evaluate the forecast dispersion score Ut+1(κ)U\_{t+1}^{(\kappa)} as defined in Equation ([7](https://arxiv.org/html/2511.17462v1#S2.E7 "In 2. Methodology ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection")).

Table 1. Summary of Forecasting Models for Latent Factors

|  |  |  |
| --- | --- | --- |
| Model Abbreviation | Forecast | Uncertainty Type |
| IID-BS | IID-Based  (Sample Mean) | Mean Absolute Deviation from  the Mean across 2 Bootstrap Quantiles |
| Q-Boost | XGBoost-Based Median  (trained with RAPIDS) | Mean Absolute Deviation from  the Median across 3 Tree-Based Quantiles |
| ZS-Chronos | Chronos-Based Median  (Zero-Shot) | Mean Absolute Deviation from  the Median across 9 Chronos Quantiles |

The second model, Quantile Gradient Boosted Regression Trees (Q-Boost), estimates the conditional quantile function of each latent factor ft+1(κ)f\_{t+1}^{(\kappa)} using lagged time-series features. Let xt(κ)∈ℝdx\_{t}^{(\kappa)}\in\mathbb{R}^{d} denote the feature vector extracted from the history {fs(κ)}s=1t\{f\_{s}^{(\kappa)}\}\_{s=1}^{t} (see Section [3](https://arxiv.org/html/2511.17462v1#S3 "3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection") for details). For each quantile level α∈𝒬={0.05,0.5,0.95}\alpha\in\mathcal{Q}=\{0.05,0.5,0.95\}, we fit a separate quantile regression tree Qκ(α)Q\_{\kappa}^{(\alpha)} to obtain:
  
f^t+1(κ,α)=Qκ(α)​(xt(κ)).\hat{f}\_{t+1}^{(\kappa,\alpha)}=Q\_{\kappa}^{(\alpha)}(x\_{t}^{(\kappa)}).
The median forecast f^t+1(κ,0.5)\hat{f}\_{t+1}^{(\kappa,0.5)} serves as the point estimate, while the uncertainty score Ut+1(κ)U\_{t+1}^{(\kappa)} is computed from the predicted quantiles via Equation ([7](https://arxiv.org/html/2511.17462v1#S2.E7 "In 2. Methodology ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection")) using f^t+1(κ,0.05)\hat{f}\_{t+1}^{(\kappa,0.05)} and f^t+1(κ,0.95)\hat{f}\_{t+1}^{(\kappa,0.95)}. We restrict the model to three quantile levels to reduce computational burden, since each α\alpha requires fitting an independent learner. Despite this limitation, Q-Boost captures localized nonlinear dynamics effectively and remains computationally efficient (friedman2001greedy).

The third model, ZS-Chronos, is a 205 million parameter pretrained Time Series Foundation Model (TSFM) based on the encoder-decoder T5 architecture (ansari2024chronos). We specifically adopt the Chronos-Bolt variant due to its GPU-optimized design and improved inference speed compared to the original Chronos model. For each factor κ\kappa, we input its historical sequence {fs(κ)}s=1t\{f\_{s}^{(\kappa)}\}\_{s=1}^{t} and obtain a set of quantile forecasts {f^t+1(κ,α)}α∈𝒬\{\hat{f}\_{t+1}^{(\kappa,\alpha)}\}\_{\alpha\in\mathcal{Q}} with 𝒬={0.1,0.2,…,0.9}\mathcal{Q}=\{0.1,0.2,\dots,0.9\}. The central prediction is the median f^t+1(κ)=f^t+1(κ,0.5)\hat{f}\_{t+1}^{(\kappa)}=\hat{f}\_{t+1}^{(\kappa,0.5)}, and the uncertainty is computed as the mean absolute deviation from this value as in ([7](https://arxiv.org/html/2511.17462v1#S2.E7 "In 2. Methodology ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection")). Chronos is applied in a zero-shot (ZS) configuration without task-specific fine-tuning, leveraging pretrained knowledge to generate competitive forecasts across domains. Its effectiveness has been benchmarked on GIFT-Eval (aksu2024gifteval), where it ranks among the top models for financial and economic prediction tasks. This strong performance and high speed motivated our selection of Chronos as a core forecasting component.

Together, these models provide a rich ensemble of predictive signals that support robust portfolio construction. The IID-BS model offers a model-free benchmark; Q-Boost captures local time-series structure through supervised learning; and ZS-Chronos applies deep sequence modeling in a data-efficient, pretrained framework.

## 3. Empirical Analysis

We evaluate our methodology using monthly returns data for the 2000 largest US stocks, sorted by market equity at the end of each rolling estimation window. All returns are adjusted for dividends and stock splits. The predictive factors used within the CAE framework are constructed following (jensen2023replication), comprising 153 long–short portfolios spanning the US equity market from February 1962 through December 2024. For detailed information on factor construction, we refer readers to (jensen2023replication) and the accompanying online appendix.

To ensure methodological rigor and eliminate potential look-ahead bias, we strictly adhere to the timing conventions detailed in (jensen2023replication). Specifically, all firm-level characteristics used in factor construction are lagged by at least six months, capturing realistic data availability constraints. This lag structure ensures that factor portfolios at time tt are constructed solely from information observable no later than t−6t-6, preserving both causal interpretation and practical implementability within our forecasting framework.

Our empirical analysis employs an expanding-window forecasting scheme to closely replicate realistic investment conditions. Initially, the CAE is trained on data from February 1962 through December 1999 (38 years) to extract latent factor representations and characteristic-based exposures. Within each expanding training window, we utilize a rolling validation period of the most recent 12 years for hyperparameter tuning and early stopping. The out-of-sample evaluation spans January 2000 to December 2024 (25 years), during which CAE models are recalibrated annually using all historical data available up to the previous year’s end, and portfolio weights are rebalanced monthly.

For all performance analyses—including ensemble strategies—we restrict investments to the 300 largest optimal weights in absolute terms, applying normalization to exclude leverage and maintain approximate market neutrality. These practical constraints, combined with our monthly rebalancing and focus on liquid, large-cap equities, ensure that the reported strategies are robust, implementable, and resilient to market frictions.

We evaluate the performance of CAE-based models across multiple latent dimensions. Specifically, six CAE architectures are trained, each corresponding to a distinct number of latent factors, with K∈{5,10,20,30,40,50}K\in\{5,10,20,30,40,50\}. This design enables a systematic examination of model scalability and predictive efficacy as a function of latent complexity. For each value of KK, we apply the uncertainty-aware factor selection procedure detailed in Section [2](https://arxiv.org/html/2511.17462v1#S2 "2. Methodology ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection"), which isolates the most predictable components for portfolio construction.

To reduce estimation variance and improve robustness, we ensemble multiple CAE models initialized with distinct random weight initializations, see also (gu2020autoencoder) for analogous model construction and implementation details. The hyperparameters used for CAE training are summarized in Table [3](https://arxiv.org/html/2511.17462v1#S3.T3 "Table 3 ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection").

Table 2. Q-Boost Feature Set for Factor Returns Prediction

|  |  |  |
| --- | --- | --- |
| Feature Name | Equation | Windows/Lags |
| Lagged Returns | rκ,t−ℓr\_{\kappa,t-\ell} | ℓ∈{1,3,5,10}\ell\in\{1,3,5,10\} |
| Moving Averages | μκ,t(m)=1m​∑j=0m−1rκ,t−j\mu^{(m)}\_{\kappa,t}=\frac{1}{m}\sum\_{j=0}^{m-1}r\_{\kappa,t-j} | m∈{3,5,10,20}m\in\{3,5,10,20\} |
| Rolling Std Dev | σκ,t(m)=1m−1​∑j=0m−1(rκ,t−j−μκ,t(m))2\sigma^{(m)}\_{\kappa,t}=\sqrt{\frac{1}{m-1}\sum\_{j=0}^{m-1}(r\_{\kappa,t-j}-\mu^{(m)}\_{\kappa,t})^{2}} | m∈{3,5,10,20}m\in\{3,5,10,20\} |
| Rolling Minimum | minκ,t(m)=minj=0,…,m−1⁡rκ,t−j\min^{(m)}\_{\kappa,t}=\min\_{j=0,...,m-1}r\_{\kappa,t-j} | m∈{3,5,10,20}m\in\{3,5,10,20\} |
| Rolling Maximum | maxκ,t(m)=maxj=0,…,m−1⁡rκ,t−j\max^{(m)}\_{\kappa,t}=\max\_{j=0,...,m-1}r\_{\kappa,t-j} | m∈{3,5,10,20}m\in\{3,5,10,20\} |
| Rate of Change | ROCκ,t(ℓ)=rκ,trκ,t−ℓ−1\text{ROC}^{(\ell)}\_{\kappa,t}=\frac{r\_{\kappa,t}}{r\_{\kappa,t-\ell}}-1 | ℓ∈{1,3,5,10}\ell\in\{1,3,5,10\} |
| Z-scores | zκ,t(m)=rκ,t−μκ,t(m)σκ,t(m)z^{(m)}\_{\kappa,t}=\frac{r\_{\kappa,t}-\mu^{(m)}\_{\kappa,t}}{\sigma^{(m)}\_{\kappa,t}} | m∈{30,60,90}m\in\{30,60,90\} |
| Momentum | momκ,t=μκ,t(5)−μκ,t(20)\text{mom}\_{\kappa,t}=\mu^{(5)}\_{\kappa,t}-\mu^{(20)}\_{\kappa,t} | 5-day vs 20-day |
| Peer Lags | rκ′,t−ℓr\_{\kappa^{\prime},t-\ell} | ℓ∈{1,3,5}\ell\in\{1,3,5\}, 3 peers |

For latent factor forecasting, we apply three distinct techniques, IID-BS, Q-Boost, and ZS-Chronos, to capture a range of modeling assumptions and temporal dependencies. The IID-BS method generates bootstrap resamples of historical returns for each latent factor using the numpy library. Forecasts are formed as the sample mean, and uncertainty is quantified via empirical quantiles of the resampled distribution. This approach serves as a computationally efficient, nonparametric benchmark.

Q-Boost leverages gradient-boosted decision trees via the XGBoost framework, specifically configured for quantile regression. For each factor κ\kappa, we construct a feature vector xκ,t∈ℝdx\_{\kappa,t}\in\mathbb{R}^{d} at time tt from lagged transformations of its historical return series rκ,ss≤t−1{r\_{\kappa,s}}\_{s\leq t-1}. Our feature engineering pipeline captures a broad range of temporal patterns—including momentum effects, volatility regimes, and cross-sectional interactions with correlated peer factors. The specific mathematical formulations and parameterizations for each feature type are summarized in Table [2](https://arxiv.org/html/2511.17462v1#S3.T2 "Table 2 ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection"), resulting in d=37d=37 features per factor.

Training is accelerated using Nvidia’s GPU-based RAPIDS library (rapids2018), which provides substantial speedups over CPU execution. In contrast to Chronos’ joint sequence modeling, Q-Boost trains independent quantile regressors for each latent factor, enabling targeted learning of factor-specific dynamics.

Table 3. Model Hyperparameters for CAE and Q-Boost.

|  |  |  |  |
| --- | --- | --- | --- |
| Panel A: CAE Model | | Panel B: Q-Boost Model | |
| Parameter | Value | Parameter | Value |
| Learning Rate | 1e-3 | Learning Rate | 0.05 |
| Epochs | 200 | Iterations | 50 |
| Hidden Layers | [32, 16] | Depth | 3 |
| Batch Size | 10,000 | Bootstrap Type | Bayesian |
| L1 Regularization | 1e-5 | Task Type | GPU |
| Patience | 5 | Quantile Range | [0.05, 0.5, 0.95] |
| Number of Experts | 50 | Loss Function | Quantile Loss |
| Validation Period | 144 months |  |  |
| Retrain Frequency | 12 months |  |  |

The Q-Boost model is trained on xκ,tx\_{\kappa,t} to predict the conditional quantiles of the future return rκ,t+1r\_{\kappa,t+1}, using a quantile loss at levels α∈{0.05,0.5,0.95}\alpha\in\{0.05,0.5,0.95\}, thereby yielding probabilistic forecasts that incorporate uncertainty. The specific hyperparameters used for Q-Boost are detailed in Table [3](https://arxiv.org/html/2511.17462v1#S3.T3 "Table 3 ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection").

The ZS-Chronos model corresponds to the Chronos-Bolt Base architecture, a configuration of Chronos comprising 205 million parameters. We apply Chronos in a zero-shot setting using the official chronos library, and leveraging the ChronosBoltPipeline class, allowing direct inference on time-series sequences without additional training.

We see that integrating forecast uncertainty into latent factor selection leads to substantial improvements in portfolio performance across all model architectures, as illustrated in the risk-return frontier shown in Figure [2](https://arxiv.org/html/2511.17462v1#S3.F2 "Figure 2 ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection"). This figure presents portfolios generated under various latent factor subset sizes κ\kappa, demonstrating that models leveraging uncertainty-aware selection consistently outperform the baseline CAE models. The plotted configurations reflect all combinations generated under the K=50 setting for the IID-BS, Q-Boost, and ZS-Chronos models, as well as the configurations from the original CAE benchmarks.

![Refer to caption](Figures/combined_frontier.png)


Figure 2. Out-of-sample risk–return frontier for CAE models with K∈5,10,20,30,40,50K\in{5,10,20,30,40,50}, as well as IID-BS, Q-Boost, and ZS-Chronos (each with K=50K=50). Each point represents a model configuration constructed from a subset of κ=1,2,…,50\kappa=1,2,\ldots,50 latent factors, selected according to forecast uncertainty. The figure illustrates the trade-off between annualized return and volatility across varying κ\kappa, showing that uncertainty-aware pruning consistently improves risk-adjusted performance. The smooth, concave shape of the frontier highlights model diversity, while the gradual variation in performance with the number of included factors indicates robustness to the choice of κ\kappa.

Our analysis illustrates a smooth curvature in the frontier plot as κ\kappa changes, reflecting a stable relationship between the number of selected latent factors and portfolio performance. This behavior suggests that the procedure is not highly sensitive to small perturbations in κ\kappa, thereby reducing the risk of overfitting. The observed performance improvements are therefore attributable to the exploitation of persistent structure in the data rather than spurious variation.

Our findings indicate that strong out-of-sample performance can be achieved without utilizing the full set of latent factors. Configurations with κ<50\kappa<50 often outperform the full CAE benchmark set, with κ∈{20,…,40}\kappa\in\{20,\ldots,40\} frequently offering the best return-volatility trade-off. Our results, detailed in Table [4](https://arxiv.org/html/2511.17462v1#S3.T4 "Table 4 ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection"), demonstrate that selectively choosing predictable factors enhances portfolio efficiency by concentrating exposure on stable drivers of return while reducing exposure to high-variance components.

Table 4. Performance comparison of each model (CAE, IID-BS, Q-Boost, ZS-Chronos) and ensemble strategies over 2000–2024. Each row corresponds to a specific latent dimensionality KK and its best-performing factor subset size κ∗\kappa^{\*}. Metrics include Sortino, Sharpe, Omega ratios, annualized return, volatility, and maximum drawdown. Adaptive κ\kappa models adjust factor size based on past performance. Ensemble (A) includes SPY and achieves the best risk-adjusted metrics; Ensemble (B) excludes SPY and yields the highest total and annualized returns. Bold and underlined values indicate best overall performance.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | KK | κ∗\kappa^{\*} | Sortino Ratio | Sharpe Ratio | Omega Ratio | Ann. Ret. (%) | Ann. Vol. (%) | Max DD. (%) |
| CAE | 5 | – | 3.053 | 1.610 | 3.437 | 15.18 | 9.43 | 16.57 |
| CAE | 10 | – | 2.729 | 1.568 | 3.382 | 14.92 | 9.51 | 10.48 |
| CAE | 20 | – | 2.780 | 1.664 | 3.596 | 15.35 | 9.22 | 13.36 |
| CAE | 30 | – | 2.949 | 1.738 | 3.814 | 15.91 | 9.15 | 19.48 |
| CAE | 40 | – | 2.908 | 1.751 | 3.922 | 15.47 | 8.84 | 18.29 |
| CAE | 50 | – | 2.866 | 1.714 | 3.803 | 15.05 | 8.78 | 18.07 |
| IID-BS | 5 | 5 | 3.042 | 1.604 | 3.419 | 15.15 | 9.45 | 16.57 |
| IID-BS | 10 | 4 | 3.239 | 1.642 | 3.758 | 15.02 | 9.15 | 10.65 |
| IID-BS | 20 | 3 | 3.262 | 1.647 | 3.969 | 12.54 | 7.62 | 8.94 |
| IID-BS | 30 | 27 | 3.111 | 1.827 | 4.092 | 16.77 | 9.18 | 15.07 |
| IID-BS | 40 | 16 | 3.424 | 1.854 | 4.261 | 15.55 | 8.39 | 15.95 |
| IID-BS | 50 | 25 | 3.714 | 1.973 | 4.841 | 16.26 | 8.24 | 11.76 |
| IID-BS | 50 | Adaptive | 3.565 | 1.924 | 4.640 | 16.03 | 8.33 | 12.20 |
| Q-Boost | 5 | 3 | 2.520 | 1.520 | 3.168 | 14.14 | 9.31 | 15.16 |
| Q-Boost | 10 | 5 | 2.485 | 1.508 | 3.296 | 14.46 | 9.59 | 14.19 |
| Q-Boost | 20 | 4 | 3.073 | 1.603 | 3.574 | 11.50 | 7.18 | 7.54 |
| Q-Boost | 30 | 10 | 2.721 | 1.694 | 3.658 | 12.10 | 7.14 | 10.90 |
| Q-Boost | 40 | 17 | 2.806 | 1.599 | 3.376 | 10.68 | 6.68 | 11.52 |
| Q-Boost | 50 | 20 | 3.351 | 1.954 | 4.696 | 14.05 | 7.19 | 10.57 |
| Q-Boost | 50 | Adaptive | 3.080 | 1.700 | 3.812 | 12.80 | 7.53 | 18.92 |
| ZS-Chronos | 5 | 5 | 2.840 | 1.663 | 3.505 | 15.93 | 9.58 | 18.10 |
| ZS-Chronos | 10 | 6 | 2.876 | 1.703 | 3.629 | 15.79 | 9.27 | 13.59 |
| ZS-Chronos | 20 | 8 | 3.379 | 1.762 | 3.737 | 13.81 | 7.84 | 13.38 |
| ZS-Chronos | 30 | 15 | 3.311 | 1.808 | 4.156 | 13.73 | 7.59 | 8.49 |
| ZS-Chronos | 40 | 8 | 3.984 | 1.905 | 4.901 | 16.29 | 8.55 | 11.17 |
| ZS-Chronos | 50 | 7 | 3.847 | 1.813 | 4.608 | 15.63 | 8.62 | 9.25 |
| ZS-Chronos | 50 | Adaptive | 3.042 | 1.872 | 5.169 | 16.62 | 8.88 | 15.62 |
| Ensemble (A) | 50 | Adaptive | 4.010 | 2.204 | 5.952 | 14.37 | 6.52 | 9.22 |
| Ensemble (B) | 50 | Adaptive | 4.222 | 2.111 | 5.433 | 15.05 | 7.13 | 12.13 |

While the preceding analysis demonstrates that post-hoc selection of κ\kappa yields robust performance, it implicitly assumes future optimality of κ\kappa, limiting practical applicability. To address this limitation, we introduce an adaptive selection procedure for the number of latent factors, denoted by κt(m)⁣∗\kappa\_{t}^{(m)\*}, relying solely on information available at decision point tt. This adaptation preserves the uncertainty-aware factor selection methodology while offering realistic and implementable forecasts.

Specifically, we employ an expanding-window framework to dynamically determine κt(m)⁣∗\kappa\_{t}^{(m)\*} for each predictive model m∈{1,2,3}m\in\{1,2,3\} (IID-BS, Q-Boost, ZS-Chronos). Instead of using a fixed κ\kappa, we adaptively optimize a temporally regularized objective based on past risk-adjusted performance. We opt for the Sortino ratio, defined below, as our main selection criterion because it emphasizes downside risk and thus facilitates a more aggressive adaptive choice of κ\kappa compared to the Sharpe ratio, which penalizes both upside and downside deviations equally. While Sharpe could be an alternative, our objective is to prioritize portfolios less susceptible to negative returns.

Formally, let rt(m,κ)∈ℝHr\_{t}^{(m,\kappa)}\in\mathbb{R}^{H} denote the out-of-sample return vector for model mm with κ\kappa factors over the last HH periods. Define empirical downside deviation, mean return, and the Sortino ratio as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σt−(m,κ)\displaystyle\sigma^{-}\_{t}{}^{(m,\kappa)} | =1H​∑h=1H(min⁡{rt,h(m,κ),0})2,\displaystyle=\sqrt{\frac{1}{H}\sum\_{h=1}^{H}\left(\min\{r\_{t,h}^{(m,\kappa)},0\}\right)^{2}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μt(m,κ)\displaystyle\mu\_{t}^{(m,\kappa)} | =1H​∑h=1Hrt,h(m,κ),SoRt(m)​(κ)=μt(m,κ)σt−+(m,κ)ε,ε>0.\displaystyle=\frac{1}{H}\sum\_{h=1}^{H}r\_{t,h}^{(m,\kappa)},\quad\mathrm{SoR}\_{t}^{(m)}(\kappa)=\frac{\mu\_{t}^{(m,\kappa)}}{\sigma^{-}\_{t}{}^{(m,\kappa)}+\varepsilon},\quad\varepsilon>0. |  |

Direct maximization of the Sortino ratio over κ\kappa at each step is unstable due to high variance induced by occasional negative returns. Thus, we propose a smooth, differentiable approximation of the discrete optimization via a log-sum-exp (LSE) formulation. Introducing the latent variable θt(m)=log⁡κt(m)⁣∗\theta\_{t}^{(m)}=\log\kappa\_{t}^{(m)\*} (log-scale for positivity), the objective becomes:

|  |  |  |
| --- | --- | --- |
|  | ℒLSE(m)​(θt(m))=1λ​log​∑κ∈Kmexp⁡(λ⋅SoRt(m)​(κ)−λ​(θt(m)−log⁡κ)2),\mathcal{L}\_{\mathrm{LSE}}^{(m)}(\theta\_{t}^{(m)})=\frac{1}{\lambda}\log\sum\_{\kappa\in K\_{m}}\exp\left(\lambda\cdot\mathrm{SoR}\_{t}^{(m)}(\kappa)-\lambda(\theta\_{t}^{(m)}-\log\kappa)^{2}\right), |  |

where λ>0\lambda>0 controls smoothness, and the quadratic term penalizes deviations in log-space, providing a localizing effect that stabilizes the selection.

To enhance temporal stability, we include a regularization term encouraging gradual evolution of factor complexity over time: ℛsmooth(m)​(θt(m))=η2​(θt(m)−θt−1(m))2\mathcal{R}\_{\mathrm{smooth}}^{(m)}(\theta\_{t}^{(m)})=\frac{\eta}{2}\left(\theta\_{t}^{(m)}-\theta\_{t-1}^{(m)}\right)^{2} for η>0\eta>0. The final optimization solved at each window is
  
θt(m)⁣∗=arg⁡minθ∈ℝ⁡{−ℒLSE(m)​(θ)+ℛsmooth(m)​(θ)}\theta\_{t}^{(m)\*}=\arg\min\_{\theta\in\mathbb{R}}\left\{-\mathcal{L}\_{\mathrm{LSE}}^{(m)}(\theta)+\mathcal{R}\_{\mathrm{smooth}}^{(m)}(\theta)\right\},
from which we obtain κt(m)⁣∗=round​(exp⁡(θt(m)⁣∗))\kappa\_{t}^{(m)\*}=\mathrm{round}\left(\exp(\theta\_{t}^{(m)\*})\right).

![Refer to caption](Figures/cumulative_returns.png)


Figure 3. Cumulative returns from 2000 to 2024 for each forecasting model using adaptive κ∗\kappa^{\*} selection. The plot compares individual strategies—ZS-Chronos, Q-Boost, IID-BS, CAE (with K=5K=5)—against the SPY benchmark and two ensemble portfolios. Ensemble (A) includes SPY and achieves the highest Sharpe and Sortino ratios, while Ensemble (B), constructed from adaptive strategies only, yields the highest total return and annualized growth. All models significantly outperform SPY, demonstrating the effectiveness of uncertainty-aware latent factor selection.

![Refer to caption](Figures/end_of_year_returns.png)


Figure 4. Yearly returns of each (adaptive κ∗\kappa^{\*}) strategy during market drawdown years—defined as years when the benchmark index (SPY) posted negative annual returns. All strategies achieve positive performance during these periods, with the sole exception of ZS-Chronos, which incurred a modest loss of 1.25% in 2008.

This log-sum-exp approximation follows the smooth optimization framework of (Nesterov2005Smooth), enabling stable gradient-based optimization. Additionally, our regularization term is conceptually aligned with the Follow-The-Regularized-Leader (FTRL) method (McMahan2017FTRL; Hazan2017Survey), which imposes stability through proximity to previous solutions. In empirical analyses, we set λ=1\lambda=1, η=2\eta=2, and the lookback period H=12H=12, initializing κt(m)⁣∗\kappa\_{t}^{(m)\*} as K/2K/2 for the first 12 periods. We empirically evaluated the proposed adaptive selection method and found the results to be robust across a range of parameter choices (λ\lambda, η\eta, and HH), confirming the practical effectiveness and generalizability of our framework.

We observe that the individual adaptive strategies, IID-BS, Q-Boost, and ZS-Chronos, demonstrate consistently strong performance over the full out-of-sample period from 2000 to 2024. As shown in Figure [3](https://arxiv.org/html/2511.17462v1#S3.F3 "Figure 3 ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection"), each strategy outperforms the market (SPY) with higher cumulative returns. Their resilience is evident during market downturn periods, Figure [4](https://arxiv.org/html/2511.17462v1#S3.F4 "Figure 4 ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection") highlights that almost all models produce positive returns even in years with market drawdowns.

Despite sharing the same CAE latent factor universe (K=50K=50), the adaptive strategies exhibit low pairwise return correlations, as illustrated in Figure [5](https://arxiv.org/html/2511.17462v1#S3.F5 "Figure 5 ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection"). This diversity shows that each predictive model captures distinct signals and reacts differently to underlying factor dynamics and market conditions.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Panel A: Out-of-Sample Performance Metrics | | | | | | | |
|  | Ensemble (A) | Ensemble (B) | ZS‑Chronos | Q‑Boost | IID‑BS | CAE (K=5K=5) | SPY |
| Total Return (%) | 3274.15 | 3849.92 | 5615.46 | 2173.80 | 4890.61 | 3842.66 | 528.38 |
| CAGR (%) | 15.114 | 15.841 | 17.566 | 13.310 | 16.930 | 15.833 | 7.629 |
| Sharpe Ratio | 2.204 | 2.111 | 1.876 | 1.704 | 1.928 | 1.613 | 0.560 |
| Sortino Ratio | 4.010 | 4.222 | 3.052 | 3.090 | 3.577 | 3.064 | 0.791 |
| Omega Ratio | 5.952 | 5.433 | 5.169 | 3.812 | 4.640 | 3.437 | 1.513 |
| Annual Return (%) | 14.367 | 15.045 | 16.675 | 12.842 | 16.085 | 15.226 | 8.551 |
| Annual Volatility (%) | 6.520 | 7.127 | 8.886 | 7.538 | 8.343 | 9.440 | 15.265 |
| Max Drawdown (%) | 9.224 | 12.126 | 15.067 | 17.681 | 12.057 | 15.789 | 50.785 |
| Market (SPY) Beta | 0.051 | -0.055 | -0.100 | -0.055 | -0.031 | -0.040 | 1 |
| Market (SPY) Alpha (%) | 13.934 | 15.517 | 17.532 | 13.313 | 16.348 | 15.571 | 0 |
| Panel B: Performance with 10 Basis Points Transaction Costs | | | | | | | |
| Total Return (%) | 1773.13 | 2018.46 | 2974.48 | 1124.51 | 2501.68 | 1987.92 | – |
| CAGR (%) | 12.44 | 12.94 | 14.63 | 10.50 | 13.87 | 12.88 | – |
| Sharpe Ratio | 1.830 | 1.770 | 1.596 | 1.378 | 1.620 | 1.341 | – |
| Sortino Ratio | 3.208 | 3.478 | 2.637 | 2.445 | 2.961 | 2.473 | – |
| Omega Ratio | 4.344 | 4.106 | 4.050 | 2.959 | 3.607 | 2.800 | – |
| Annual Return (%) | 11.99 | 12.48 | 14.11 | 10.31 | 13.40 | 12.61 | – |
| Annual Volatility (%) | 6.55 | 7.05 | 8.84 | 7.48 | 8.27 | 9.40 | – |
| Max Drawdown (%) | 12.35 | 14.33 | 17.41 | 21.60 | 15.76 | 18.04 | – |
| Monthly Turnover | 1.961 | 2.092 | 2.047 | 2.080 | 2.094 | 2.110 | – |
| Panel C: Monthly Alphas from Expanding Factor Analysis | | | | | | | |
| Monthly Alpha (%) | 1.016\*\*\* | 1.078\*\*\* | 1.237\*\*\* | 0.919\*\*\* | 1.188\*\*\* | 1.106\*\*\* | – |
|  | (9.53) | (9.21) | (8.42) | (7.35) | (8.56) | (7.56) |  |
| + Mkt-RF | 0.988\*\*\* | 1.117\*\*\* | 1.287\*\*\* | 0.956\*\*\* | 1.204\*\*\* | 1.153\*\*\* | – |
|  | (9.23) | (9.55) | (8.76) | (7.63) | (8.59) | (7.87) |  |
| + SMB | 0.986\*\*\* | 1.113\*\*\* | 1.264\*\*\* | 0.964\*\*\* | 1.198\*\*\* | 1.153\*\*\* | – |
|  | (9.20) | (9.51) | (8.96) | (7.72) | (8.56) | (7.86) |  |
| + HML | 0.972\*\*\* | 1.101\*\*\* | 1.262\*\*\* | 0.952\*\*\* | 1.183\*\*\* | 1.128\*\*\* | – |
|  | (9.14) | (9.46) | (8.92) | (7.66) | (8.51) | (7.85) |  |
| + RMW | 0.896\*\*\* | 1.043\*\*\* | 1.271\*\*\* | 0.879\*\*\* | 1.119\*\*\* | 1.016\*\*\* | – |
|  | (8.28) | (8.75) | (8.71) | (6.92) | (7.84) | (6.97) |  |
| + CMA | 0.839\*\*\* | 0.985\*\*\* | 1.189\*\*\* | 0.849\*\*\* | 1.062\*\*\* | 0.960\*\*\* | – |
|  | (7.82) | (8.33) | (8.27) | (6.64) | (7.45) | (6.59) |  |
| + MOM | 0.811\*\*\* | 0.952\*\*\* | 1.148\*\*\* | 0.826\*\*\* | 1.038\*\*\* | 0.933\*\*\* | – |
|  | (7.84) | (8.25) | (8.18) | (6.50) | (7.33) | (6.46) |  |
| + STR | 0.791\*\*\* | 0.939\*\*\* | 1.154\*\*\* | 0.809\*\*\* | 1.012\*\*\* | 0.903\*\*\* | – |
|  | (7.87) | (8.39) | (8.24) | (6.63) | (7.79) | (6.95) |  |
| Final R2R^{2} | 0.222 | 0.197 | 0.202 | 0.164 | 0.230 | 0.307 | – |

Table 5. Out-of-sample performance metrics and expanding factor regressions from January 2000 to December 2024 for portfolios constructed using adaptive κ∗\kappa^{\*} selection.
Panel A reports performance statistics, including total and annualized returns, volatility, Sharpe, Sortino, and Omega ratios, as well as CAPM alpha and beta relative to the SPY benchmark.
Panel B reports performance metrics with 10 basis points transaction costs, where monthly turnover for each strategy is averaged across the out-of-sample backtest period.
Panel C presents monthly alphas from time-series regressions of excess portfolio returns on an expanding sequence of Fama–French, momentum and short-term reversal factors, computed on gross returns.
Each row adds one additional factor to the regression, and the reported alpha represents the intercept after controlling for that factor and all preceding factors in the sequence.
The ordering of factors is Market (Mkt–RF), Size (SMB), Value (HML), Profitability (RMW), Investment (CMA), Momentum (MOM), and Short-Term Reversal (STR).
tt-statistics are reported in parentheses. Significance levels: \* p<0.10p<0.10, \*\* p<0.05p<0.05, \*\*\* p<0.01p<0.01.

![Refer to caption](Figures/correlation_matrix.png)


Figure 5. Correlation matrix of out-of-sample returns from 2000 to 2024 across adaptive κ∗\kappa^{\*} strategies. Each entry represents the Pearson correlation between two models’ return series, including ZS-Chronos, Q-Boost, IID-BS, CAE (K=5K=5), SPY, and the two ensemble portfolios. The low correlations among strategies highlight their complementary predictive signals and justify ensemble construction.

Driven by the complementary performance of the individual strategies, we construct two ensemble portfolios using a tangency portfolio framework. At each rebalancing date tt, we compute the sample mean return vector μt∈ℝn\mu\_{t}\in\mathbb{R}^{n} and the sample covariance matrix Σt∈ℝn×n\Sigma\_{t}\in\mathbb{R}^{n\times n}, where nn denotes the number of constituent strategies. These estimates are derived using an expanding window of all available out-of-sample returns observed up to time tt. The portfolio weights are then determined by maximizing the Sharpe ratio, giving the tangency portfolio: wt=Σt−1​μt𝟏⊤​Σt−1​μtw\_{t}=\frac{\Sigma\_{t}^{-1}\mu\_{t}}{\mathbf{1}^{\top}\Sigma\_{t}^{-1}\mu\_{t}}, where wt∈ℝnw\_{t}\in\mathbb{R}^{n} is the vector of optimal portfolio weights among each strategy.

We consider two variants of this ensemble construction. Ensemble (A) includes the market index (SPY) alongside the adaptive strategies, while Ensemble (B) allocates exclusively among the adaptive models, thereby maintaining full market neutrality. As reported in Table [5](https://arxiv.org/html/2511.17462v1#S3.T5 "Table 5 ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection"), both ensemble strategies exhibit superior performance across a broad range of evaluation metrics. Ensemble (A) achieves the highest Sharpe ratio (2.20), and Omega ratio (5.95), as well as the lowest annualized volatility (6.52%) and lowest maximum drawdown (9.22%). Ensemble (B) achieves the highest Sortino ratio (4.22), while maintaining negative market beta.

To evaluate the performance of our model accounting for transaction costs, we compute the monthly turnover as the ℓ1\ell\_{1} norm T​Ot=∑i=1N|w(t−1),i†−wt,i|=‖𝐰t†−𝐰‖1,TO\_{t}=\sum\_{i=1}^{N}|w^{\dagger}\_{(t-1),i}-w\_{t,i}|=\|\mathbf{w}\_{t}^{\dagger}-\mathbf{w}\|\_{1}, where 𝐰t†\mathbf{w}\_{t}^{\dagger} denotes the portfolio weights immediately before rebalancing at time tt, carried forward from the previous allocation after returns have been realized. The net returns are computed using a linear transaction cost model:
Rp,tN​e​t=(1−κ​T​Ot)​(1+Rp,tG​r​o​s​s)−1,R^{Net}\_{p,t}=\left(1-\kappa\ TO\_{t}\right)\left(1+R^{Gross}\_{p,t}\right)-1,
where Rp,tG​r​o​s​sR^{Gross}\_{p,t} is the portfolio’s gross return before transaction costs and κ>0\kappa>0 is the transaction cost proportionality constant, e.g., κ=0.001\kappa=0.001 corresponds to 1010 bps costs. The investment universe consists of large-cap and mid-cap stocks within the top 2,000 by market equity, updated each month on a rolling basis. This ensures high liquidity and supports realistic transaction costs with 10 bps.

Given the portfolio’s gross exposure constraint of 2.0, the theoretical maximum monthly turnover is 4.0, corresponding to complete liquidation and reconstruction of both long and short positions. The observed average monthly turnover of approximately 2.0 indicates that models rebalance roughly half their positions each month, demonstrating moderate trading intensity relative to the maximum possible. Table [5](https://arxiv.org/html/2511.17462v1#S3.T5 "Table 5 ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection") Panel B summarizes the average monthly turnover, and performance metrics for each model after accounting for transaction costs.

### 3.1. Ablation Study of Chronos Look-Ahead Bias

Given the strong empirical performance of the ZS-Chronos model across the evaluation period, it is natural to ask whether this success might reflect any hidden biases introduced during pretraining, particularly from exposure to financial data. This concern is especially relevant for foundation models trained on broad, heterogeneous datasets where information leakage is often difficult to trace. To address this, we conduct an ablation study analyzing both the origin of the input data used in our evaluation and the detailed characteristics of the Chronos model’s pretraining data.

Notably, the inputs provided to ZS-Chronos in our framework are not raw market time series, but rather synthetic latent factor return sequences generated by the CAE model. These sequences are constructed as weighted linear combinations of stock returns using CAE-learned factor loadings, making them unique to our experimental setup. Because these latent factors are derived internally and did not exist prior to model training, there is no possibility that ZS-Chronos encountered them during pretraining.

Additionally, we analyze the specific financial data used during Chronos pretraining. As documented in (ansari2024chronos), the only financial dataset included in the training corpus was the M4 dataset, developed for the M4 Forecasting Competition. This dataset comprises 100,000 historical time series extracted from the ForeDeCk database and was finalized on December 28, 2017 (Makridakis2020M4; Makridakis2018M4). Consequently, no financial data beyond January 1, 2018 was available to the Chronos model during training, ensuring that its forecasts for our evaluation period are not influenced by any post-2017 market information.

To evaluate this, we compare the performance of ZS-Chronos and the benchmark models across two separate periods: before M4 dataset availability (2011–2017) and after (2018–2024). These two seven-year windows provide a balanced view of performance across distinct market regimes and enable us to examine whether ZS-Chronos model demonstrates degradation after the training cutoff point. If pretraining on the M4 dataset introduced any forward-looking bias, we would expect a measurable decline in performance in the post-2018 period.

Table 6. Performance Statistics Before (2011–2017) and After (2018–2024)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Period | Metric | ZS-Chronos | Q-Boost | IID-BS | CAE (K=5) |
| Before | Total Return (%) | 132.77 | 108.01 | 128.16 | 159.27 |
| CAGR (%) | 12.83 | 11.03 | 12.51 | 14.58 |
| Annual Return (%) | 12.31 | 10.65 | 12.05 | 13.95 |
| Annual Volatility (%) | 6.06 | 5.36 | 6.49 | 7.30 |
| Sharpe Ratio | 2.033 | 1.989 | 1.856 | 1.912 |
| Sortino Ratio | 3.381 | 3.591 | 3.815 | 3.900 |
| Omega Ratio | 4.481 | 4.258 | 3.760 | 3.986 |
| Max Drawdown (%) | 4.44 | 3.22 | 7.99 | 5.92 |
| Market (SPY) Beta | 0.05 | 0.02 | 0.10 | 0.02 |
| After | Total Return (%) | 124.10 | 50.17 | 85.81 | 111.19 |
| CAGR (%) | 12.22 | 5.98 | 9.25 | 11.27 |
| Annual Return (%) | 11.79 | 6.10 | 9.21 | 11.28 |
| Annual Volatility (%) | 6.46 | 7.44 | 8.08 | 10.54 |
| Sharpe Ratio | 1.826 | 0.820 | 1.140 | 1.070 |
| Sortino Ratio | 3.898 | 1.258 | 1.717 | 1.960 |
| Omega Ratio | 3.665 | 1.846 | 2.410 | 2.260 |
| Max Drawdown (%) | 12.83 | 17.68 | 12.06 | 11.09 |
| Market (SPY) Beta | -0.07 | -0.07 | -0.03 | 0.04 |



![Refer to caption](Figures/cumulative_returns_before.png)

(a) Model performance before dataset creation.

![Refer to caption](Figures/cumulative_returns_after.png)

(b) Model performance after dataset creation.



Figure 6. Comparison of model performance before and after dataset construction.

Figure  [6](https://arxiv.org/html/2511.17462v1#S3.F6 "Figure 6 ‣ 3.1. Ablation Study of Chronos Look-Ahead Bias ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection") compares the performance of each forecasting model during two distinct periods: before and after the M4 dataset release, which was employed in the pretraining of the Chronos model. In the pre-2018 period, as illustrated by Table [6](https://arxiv.org/html/2511.17462v1#S3.T6 "Table 6 ‣ 3.1. Ablation Study of Chronos Look-Ahead Bias ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection"), all models deliver comparable performance. This outcome indicates that ZS-Chronos does not possess any significant advantage over the other models before its exposure to the M4 dataset.

In contrast, a notable divergence in model performance becomes evident during the post-2018 period, as detailed in Table [6](https://arxiv.org/html/2511.17462v1#S3.T6 "Table 6 ‣ 3.1. Ablation Study of Chronos Look-Ahead Bias ‣ 3. Empirical Analysis ‣ Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection"). Specifically, ZS-Chronos attains the highest annual return (11.79%) and demonstrates superior risk-adjusted metrics, achieving a 1.826 Sharpe ratio and a 3.898 Sortino ratio. Conversely, the other forecasting models exhibit relatively weaker performance, both in terms of absolute returns and risk-adjusted measures. If pretraining on the M4 dataset had introduced any forward-looking bias, ZS-Chronos would have been expected to display artificially inflated performance relative to other models in the pre-2018 period. Instead, the reverse is observed; ZS-Chronos significantly strengthens after the dataset’s creation.

This empirical evidence robustly supports the conclusion that ZS-Chronos’s superior post-2018 performance does not stem from data leakage or hidden pretraining biases. Importantly, the model is evaluated using synthetic latent factors specifically generated within our methodological framework, ensuring that Chronos had no prior exposure to the test inputs. Thus, the improved performance after 2018 further validates our approach, confirming that the pretrained Chronos model maintains strict data independence and achieves robust generalization. These findings substantiate the methodological rigor of employing pretrained foundation models such as Chronos within forecasting pipelines, emphasizing their reliability and practical applicability.

## 4. Conclusions

This paper introduces a scalable framework for high-dimensional CAEs in asset pricing, leveraging uncertainty-aware factor selection to mitigate performance degradation associated with increased latent dimensionality. Empirically, we show that selectively using latent factors based on forecast uncertainty consistently enhances risk-adjusted returns across multiple forecasting models. Notably, the highest performance emerges from portfolios that utilize only a subset of available latent factors.

We integrate three distinct forecasting methods—IID-BS, Q-Boost, and ZS-Chronos which are yielding largely uncorrelated predictive signals. This diversity enables ensemble strategies that significantly outperform individual models, with the best-performing ensemble achieving a 2.22.2 Sharpe ratio, 4.014.01 Sortino ratio, 5.955.95 Omega ratio, and maximum drawdown below 10%10\%. Furthermore, our adaptive factor selection, guided by temporally regularized log-sum-exp optimization, demonstrates robustness and practical relevance in realistic investment scenarios.

Beyond empirical validation, our framework provides a theoretical foundation for uncertainty-based selection. In particular, predictive uncertainty acts as a sufficient statistic for the expected degradation of portfolio utility under model misspecification. This interpretation links forecast dispersion directly to estimation risk and aligns with classical results showing that predictive variance governs expected utility loss and confidence weighting in optimal portfolios (pastor2000portfolio; black1992global; avramov2010should). By explicitly ranking factors according to their forecast uncertainty, the proposed approach operationalizes this principle to achieve robust out-of-sample efficiency.

Finally, our ablation analysis rules out potential data leakage concerns related to the pretrained ZS-Chronos model, confirming that its performance is not driven by hidden biases. By relying exclusively on internally generated synthetic latent factors, we preserve full data independence and maintain evaluation integrity. Overall, our findings establish uncertainty-driven dimensionality control as essential for effectively scaling CAE models, providing a principled solution to balancing the bias–variance tradeoff inherent in high-dimensional latent factor frameworks.