---
authors:
- Runyao Yu
- Ruochen Wu
- Yongsheng Han
- Jochen L. Cremer
doc_id: arxiv:2510.12685v1
family_id: arxiv:2510.12685
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity
  Markets
url_abs: http://arxiv.org/abs/2510.12685v1
url_html: https://arxiv.org/html/2510.12685v1
venue: arXiv q-fin
version: 1
year: 2025
---


Runyao Yu12,
Ruochen Wu1,
Yongsheng Han1,
Jochen L. Cremer12

###### Abstract

Accurate probabilistic forecasting of intraday electricity prices is critical for market participants to inform trading decisions.
Existing studies rely on specific domain features, such as Volume-Weighted Average Price (VWAP) and the last price. However, the rich information in the orderbook remains underexplored.
Furthermore, these approaches are often developed within a single country and product type, making it unclear whether the approaches are generalizable.
In this paper, we extract 384 features from the orderbook and identify a set of powerful features via feature selection.
Based on selected features, we present a comprehensive benchmark using classical statistical models, tree-based ensembles, and deep learning models
across two countries (Germany and Austria) and two
product types (60-min and 15-min).
We further perform a systematic generalization study across countries and product types, from which we reveal an asymmetric generalization phenomenon.
The project page is at <https://runyao-yu.github.io/AsymGen/>.

## I Introduction

Accurate probabilistic forecasting of intraday electricity price plays a vital role in enhancing decision-making for market participants under uncertainties [[19](https://arxiv.org/html/2510.12685v1#bib.bibx19)]. In continuous intraday (CID) markets, several studies have identified the volume-weighted average price (VWAP) from the most recent 15 minutes as a strong predictor of the future price index (ID3) [[16](https://arxiv.org/html/2510.12685v1#bib.bibx16), [18](https://arxiv.org/html/2510.12685v1#bib.bibx18), [21](https://arxiv.org/html/2510.12685v1#bib.bibx21)]. Previous works even argue that the last price already reflects past information, assuming weak-form efficiency [[8](https://arxiv.org/html/2510.12685v1#bib.bibx8)], and report that incorporating fundamental features, such as day-ahead forecasts of renewable generation and load, offers no or very limited improvement [[17](https://arxiv.org/html/2510.12685v1#bib.bibx17), [2](https://arxiv.org/html/2510.12685v1#bib.bibx2), [11](https://arxiv.org/html/2510.12685v1#bib.bibx11), [22](https://arxiv.org/html/2510.12685v1#bib.bibx22), [10](https://arxiv.org/html/2510.12685v1#bib.bibx10), [9](https://arxiv.org/html/2510.12685v1#bib.bibx9)], thereby motivating that using only the last price as input may suffice.
However, this assumption does not consider the rich information available in the orderbook. A wide range of orderbook features, such as price percentiles, price momentum, and traded volumes, are not explored and could potentially enhance forecasting performance.

In the context of intraday electricity price forecasting, prior works primarily rely on classical statistical methods, such as linear regression and its variants [[21](https://arxiv.org/html/2510.12685v1#bib.bibx21), [2](https://arxiv.org/html/2510.12685v1#bib.bibx2), [22](https://arxiv.org/html/2510.12685v1#bib.bibx22), [18](https://arxiv.org/html/2510.12685v1#bib.bibx18)], while more recent studies explore deep learning approaches, such as Multi-Layer Perceptron (MLP), Long Short-Term Memory (LSTM), and Transformer variants [[11](https://arxiv.org/html/2510.12685v1#bib.bibx11), [7](https://arxiv.org/html/2510.12685v1#bib.bibx7), [20](https://arxiv.org/html/2510.12685v1#bib.bibx20), [13](https://arxiv.org/html/2510.12685v1#bib.bibx13), [23](https://arxiv.org/html/2510.12685v1#bib.bibx23)], to better capture non-linear patterns in electricity prices. Most of these works have primarily focused on the German market, motivated by its high liquidity and large market size [[21](https://arxiv.org/html/2510.12685v1#bib.bibx21), [9](https://arxiv.org/html/2510.12685v1#bib.bibx9)]. Concurrently, there has been a notable shift in research focus from hourly (60-minute) products to quarter-hourly (15-minute) products [[2](https://arxiv.org/html/2510.12685v1#bib.bibx2), [7](https://arxiv.org/html/2510.12685v1#bib.bibx7), [9](https://arxiv.org/html/2510.12685v1#bib.bibx9), [10](https://arxiv.org/html/2510.12685v1#bib.bibx10)], which provide finer temporal resolution. However, existing studies typically focus on a single type of model, country, and product type, resulting in a fragmented view of model performance. This highlights the need for a unified benchmarking study that systematically compares various machine learning models across countries and product types.

![Refer to caption](x1.png)


Figure 1: 
Visualization of 60-min and 15-min ID3 from Germany and Austria.
(a)–(d) Histograms of ID3. The price indices exhibit high skewness and dispersion during the energy crisis in 2022, gradually reverting to a more stable distribution in 2023 and 2024.
(e)–(f) ID3 trajectories in 2024 (range limited to [–500, 1000] €/MWh for better visual comparison). Volatility increases in the order: AT, 60-min << DE, 60-min << AT, 15-min << DE, 15-min.

As most prior studies focus on a single country and product type, it remains unclear whether the selected features and trained models generalize well across different settings. For example, a feature set optimized for the Austrian market may not perform equally well in Germany, and a model trained on 15-min products may fail to capture the dynamics of 60-min prices. This raises important questions about cross-country and cross-product-type generalization. Thus, a systematic investigation into such generalizability is necessary to understand the robustness of derived features, support the transferable development of trained models, and offer actionable insights to stakeholders operating across multiple European markets.

In this paper, we extract 384 features from the orderbook and select the optimal features (Section [III](https://arxiv.org/html/2510.12685v1#S3 "III Feature Extraction and Selection ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets")). Then, we provide a comprehensive benchmarking study using classical statistical models, tree-based ensembles, and deep learning models
(Section [IV](https://arxiv.org/html/2510.12685v1#S4 "IV Model Comparison ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets")).
Lastly, we assess the cross-country and cross-product-type generalization of the derived optimal features and trained models (Section [V](https://arxiv.org/html/2510.12685v1#S5 "V Generalization Assessment ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets")). We reveal an asymmetric phenomenon: while the optimal feature set and trained model derived from a more liquid market transfer well to a less liquid one, the reverse does not hold. Our main contributions are summarized as follows:

* •

  We extract an exhaustive set of 384 statistical features from the orderbook, including price percentiles, extreme prices, and VWAPs, and reveal a set of powerful features.
* •

  We present a comprehensive benchmark of probabilistic forecasting performance using multiple machine learning models across two countries (Germany and Austria) and two product types (60-min and 15-min).
* •

  We systematically assess the generalizability across countries and product types. Our analysis reveals an asymmetric generalization phenomenon.

## II Preliminary

The forecasting target is the widely used ID3, visualized in Fig. [1](https://arxiv.org/html/2510.12685v1#S1.F1 "Figure 1 ‣ I Introduction ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets"). The ID3\mathrm{ID}\_{3} is defined as the VWAP of trades executed within a specific time window before delivery:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ID3=∑s∈S∑t∈𝒯fPts​Vts∑s∈S∑t∈𝒯fVts,\mathrm{ID}\_{3}\;=\;\frac{\sum\limits\_{s\in S}\sum\limits\_{t\in\mathcal{T}\_{f}}P^{s}\_{t}\,V^{s}\_{t}}{\sum\limits\_{s\in S}\sum\limits\_{t\in\mathcal{T}\_{f}}V^{s}\_{t}}, |  | (1) |

where the market side s∈S={+,−}s\in S=\{+,-\} corresponds to buy and sell orders, respectively.
The forecasting time is defined as tf=td−Δt\_{f}=t\_{d}-\Delta, with tdt\_{d} denoting the delivery time and Δ=180​min\Delta=180\,\mathrm{min} representing the lead time specific to ID3\mathrm{ID}\_{3}.
The transaction time is defined as t∈𝒯f=[tf,td−δm]t\in\mathcal{T}\_{f}=[t\_{f},\ t\_{d}-\delta\_{m}], where 𝒯f\mathcal{T}\_{f} is the forecasting (trading) window, and δm\delta\_{m} is a market-specific parameter set by EPEX Spot 111For Germany, δm=30\delta\_{m}=30 minutes; for Austria, δm=0\delta\_{m}=0 minutes. For other countries, δm\delta\_{m} can be retrieved from [EPEX Spot download center](https://www.epexspot.com/)..
Here, PtsP^{s}\_{t} and VtsV^{s}\_{t} denote the price and traded volume, respectively.

## III Feature Extraction and Selection

### III-A Feature Extraction

We extract an exhaustive set of features from both the buy (++) and sell (−-) sides across multiple look-back windows
𝒯w=[tf−δw,tf]\mathcal{T}\_{w}=[t\_{f}-\delta\_{w},\,t\_{f}], where δw∈{1,5,15,60,180,∞}\delta\_{w}\in\{1,5,15,60,180,\infty\} (in minutes), and ∞\infty denotes the full available trading history.
The full list of extracted features is summarized in Table [I](https://arxiv.org/html/2510.12685v1#S3.T1 "TABLE I ‣ III-A Feature Extraction ‣ III Feature Extraction and Selection ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets").
If no trades are recorded within a given window (e.g., δw=1\delta\_{w}=1), we fall back to the next longer window (e.g., δw=5\delta\_{w}=5) to extract features.
If no trades are observed within the full history window (δw=∞\delta\_{w}=\infty), the corresponding sample is discarded.
Feature types include price and volume statistics (e.g., min, max, mean, percentiles), with percentile levels
p∈𝒫={10%,25%,45%,50%,55%,75%,90%}p\in\mathcal{P}=\{10\%,25\%,45\%,50\%,55\%,75\%,90\%\}.

TABLE I: Extracted features and definitions.

| Feature | Mathematical Definition |
| --- | --- |
| Price Percentile|𝒯w,ps\;\big|^{s}\_{\mathcal{T}\_{w},\,p} | percentilet∈𝒯w,pPts\operatorname\*{percentile}\limits\_{t\in\mathcal{T}\_{w},p}P^{s}\_{t} |
| Min Price|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | mint∈𝒯w⁡Pts\min\limits\_{t\in\mathcal{T}\_{w}}P^{s}\_{t} |
| Max Price|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | maxt∈𝒯w⁡Pts\max\limits\_{t\in\mathcal{T}\_{w}}P^{s}\_{t} |
| First Price|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | firstt∈𝒯wPts\operatorname\*{first}\limits\_{t\in\mathcal{T}\_{w}}P^{s}\_{t} |
| Last Price|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | lastt∈𝒯wPts\operatorname\*{last}\limits\_{t\in\mathcal{T}\_{w}}P^{s}\_{t} |
| Mean Price|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | P¯𝒯ws\bar{P}^{s}\_{\mathcal{T}\_{w}} |
| Price Volatility|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | 1n𝒯ws​∑t∈𝒯w(Pts−P¯𝒯ws)2\sqrt{\dfrac{1}{n^{s}\_{\mathcal{T}\_{w}}}\sum\limits\_{t\in\mathcal{T}\_{w}}\big(P^{s}\_{t}-\bar{P}^{s}\_{\mathcal{T}\_{w}}\big)^{2}} |
| Delta Price|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | lastt∈𝒯wPts−firstt∈𝒯wPts\operatorname\*{last}\limits\_{t\in\mathcal{T}\_{w}}P^{s}\_{t}-\operatorname\*{first}\limits\_{t\in\mathcal{T}\_{w}}P^{s}\_{t} |
| Volume Percentile|𝒯w,ps\;\big|^{s}\_{\mathcal{T}\_{w},\,p} | percentilet∈𝒯w,pVts\operatorname\*{percentile}\limits\_{t\in\mathcal{T}\_{w},p}V^{s}\_{t} |
| Min Volume|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | mint∈𝒯w⁡Vts\min\limits\_{t\in\mathcal{T}\_{w}}V^{s}\_{t} |
| Max Volume|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | maxt∈𝒯w⁡Vts\max\limits\_{t\in\mathcal{T}\_{w}}V^{s}\_{t} |
| First Volume|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | firstt∈𝒯wVts\operatorname\*{first}\limits\_{t\in\mathcal{T}\_{w}}V^{s}\_{t} |
| Last Volume|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | lastt∈𝒯wVts\operatorname\*{last}\limits\_{t\in\mathcal{T}\_{w}}V^{s}\_{t} |
| Mean Volume|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | V¯𝒯ws\bar{V}^{s}\_{\mathcal{T}\_{w}} |
| Volume Volatility|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | 1n𝒯ws​∑t∈𝒯w(Vts−V¯𝒯ws)2\sqrt{\dfrac{1}{n^{s}\_{\mathcal{T}\_{w}}}\sum\limits\_{t\in\mathcal{T}\_{w}}\big(V^{s}\_{t}-\bar{V}^{s}\_{\mathcal{T}\_{w}}\big)^{2}} |
| Delta Volume|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | lastt∈𝒯wVts−firstt∈𝒯wVts\operatorname\*{last}\limits\_{t\in\mathcal{T}\_{w}}V^{s}\_{t}-\operatorname\*{first}\limits\_{t\in\mathcal{T}\_{w}}V^{s}\_{t} |
| Sum Volume|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | ∑t∈𝒯wVts\sum\limits\_{t\in\mathcal{T}\_{w}}V^{s}\_{t} |
| Trade Count|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | n𝒯wsn^{s}\_{\mathcal{T}\_{w}} |
| VWAP|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | ∑t∈𝒯wPts​Vts∑t∈𝒯wVts\dfrac{\sum\limits\_{t\in\mathcal{T}\_{w}}P^{s}\_{t}\,V^{s}\_{t}}{\sum\limits\_{t\in\mathcal{T}\_{w}}V^{s}\_{t}} |
| Momentum|𝒯ws\;\big|^{s}\_{\mathcal{T}\_{w}} | lastt∈𝒯wPts−VWAPsVWAPs\dfrac{\operatorname\*{last}\limits\_{t\in\mathcal{T}\_{w}}P^{s}\_{t}-\mathrm{VWAP}^{s}}{\mathrm{VWAP}^{s}} |

### III-B Feature Selection

The extracted feature set may contain redundant or noisy features that harm generalization.
Following prior works in utilizing ℓ1\ell\_{1}-penalized linear regression, also known as Least Absolute Shrinkage and Selection Operator (LASSO), to encourage sparse feature sets for pointwise prediction [[22](https://arxiv.org/html/2510.12685v1#bib.bibx22)],
we extend this idea to the probabilistic forecasting setting by applying ℓ1\ell\_{1}-penalized Linear Quantile Regression (LQR).

Given an input feature matrix Xi∈ℝN×DX\_{i}\in\mathbb{R}^{N\times D} and target quantile vector yi,τ∈ℝNy\_{i,\tau}\in\mathbb{R}^{N}, we estimate the coefficient vector 𝜷∈ℝD\boldsymbol{\beta}\in\mathbb{R}^{D} by solving the following optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜷^=arg⁡min𝜷⁡Lτ​(yi,τ,Xi​𝜷)+α​‖𝜷‖1\hat{\boldsymbol{\beta}}=\arg\min\_{\boldsymbol{\beta}}\;L\_{\tau}(y\_{i,\tau},X\_{i}\boldsymbol{\beta})+\alpha\|\boldsymbol{\beta}\|\_{1} |  | (2) |

where Lτ​(⋅)L\_{\tau}(\cdot) denotes the quantile loss:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lτ​(yi,τ,Xi​𝜷)=∑n=1N(yi,τ(n)−Xi(n)​𝜷)⋅(τ−𝕀​{yi,τ(n)<Xi(n)​𝜷})L\_{\tau}(y\_{i,\tau},X\_{i}\boldsymbol{\beta})=\sum\_{n=1}^{N}\left(y\_{i,\tau}^{(n)}-X\_{i}^{(n)}\boldsymbol{\beta}\right)\cdot\left(\tau-\mathbb{I}\{y\_{i,\tau}^{(n)}<X\_{i}^{(n)}\boldsymbol{\beta}\}\right) |  | (3) |

The hyperparameter α>0\alpha>0 controls the degree of sparsity by penalizing the absolute magnitudes of the coefficients and is optimized based on validation (quantile) loss. After optimization, only features with non-zero coefficient magnitudes are retained, yielding a reduced sparse feature matrix Xi(ℓ1)∈ℝN×D(ℓ1)X\_{i}^{(\ell\_{1})}\in\mathbb{R}^{N\times D\_{(\ell\_{1})}}, where D(ℓ1)≪DD\_{(\ell\_{1})}\ll D, that serves as the input to downstream quantile forecasting models.

TABLE II: Hyperparameter search range.

| Model | Search Range |
| --- | --- |
| LQR | |  | | --- | | ℓ1\ell\_{1} regularization: [1e-8, 1] | |
| QKNN | |  | | --- | | n\_neighbors: [5, 100] | | distance\_metric: {euclidean, manhattan} | | weights: {uniform, distance} | |
| QLGBM | |  | | --- | | n\_estimators: [50, 500] | | max\_depth: [3, 12] | | learning\_rate: [1e-3, 1e-1] | | subsample: [0.5, 1.0] | | colsample\_by\_tree: [0.5, 1.0] | | reg\_lambda: [0.0, 10.0] | |
| QXGB | |  | | --- | | n\_estimators: [50, 500] | | max\_depth: [3, 12] | | learning\_rate: [1e-3, 1e-1] | | reg\_alpha: [0.0, 5.0] | | reg\_lambda: [0.0, 10.0] | |
| QMLP | |  | | --- | | hidden\_size: [32, 1024] | | n\_layers: [2, 6] | | dropout\_rate: [0.0, 0.5] | | learning\_rate: [1e-5, 1e-1] | | batch\_size: [64, 1024] | |
| QKAN | |  | | --- | | kan\_units: [32, 1024] | | n\_layers: [2, 6] | | grid\_intervals: [5, 16] | | spline\_order: [2, 4] | | learning\_rate: [1e-5, 1e-1] | | batch\_size: [64, 1024] | |

## IV Model Comparison

Based on the optimal feature set identified in the previous step, we compare several machine learning models, spanning classical statistical models, tree-based ensembles, and deep learning models.
The corresponding hyperparameter search ranges are summarized in Table [II](https://arxiv.org/html/2510.12685v1#S3.T2 "TABLE II ‣ III-B Feature Selection ‣ III Feature Extraction and Selection ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets"). Each model is optimized with 100 trials using Optuna, which applies Bayesian optimization for efficient hyperparameter tuning [[1](https://arxiv.org/html/2510.12685v1#bib.bibx1)].

### IV-A Classical Statistical Models

* •

  Linear Quantile Regression (LQR).
  LQR models conditional quantiles as linear functions of the input variables. It is highly interpretable and computationally efficient, making it well-suited for high-frequency forecasting tasks [[14](https://arxiv.org/html/2510.12685v1#bib.bibx14)]. LQR has been widely adopted in the context of intraday electricity price forecasting due to its simplicity and fast training time.
* •

  Quantile K-Nearest Neighbors (QKNN).
  QKNN performs non-parametric quantile regression by computing empirical quantiles from the nearest neighbors in feature space. It makes no assumptions about the underlying data distribution and is capable of capturing strong local nonlinearities, which can be useful in modeling complex market dynamics [[3](https://arxiv.org/html/2510.12685v1#bib.bibx3)].

### IV-B Tree-Based Ensemble Learning Models

* •

  Quantile LightGBM (QLGBM).
  QLGBM extends LightGBM to support quantile regression via gradient boosting and histogram-based tree construction. It efficiently handles large-scale data and captures complex feature interactions [[12](https://arxiv.org/html/2510.12685v1#bib.bibx12)]. QLGBM is a widely used model for day-ahead electricity price forecasting due to its speed and robustness across diverse feature sets.
* •

  Quantile XGBoost (QXGB).
  QXGB adapts XGBoost for quantile objectives using regularized decision tree ensembles. It is highly effective at modeling non-linear relationships and capturing long-range dependencies [[5](https://arxiv.org/html/2510.12685v1#bib.bibx5)]. XGBoost is also a commonly used model for day-ahead electricity price forecasting.

### IV-C Deep Learning Models

* •

  Quantile Multi–layer Perceptron (QMLP).
  QMLP applies feedforward neural networks to directly estimate conditional quantiles. It learns complex non-linear mappings and scales well with high-dimensional inputs [[4](https://arxiv.org/html/2510.12685v1#bib.bibx4)]. QMLP has become a common deep learning baseline for intraday electricity price forecasting.
* •

  Quantile Kolmogorov–Arnold Networks (QKAN).
  QKAN is a recent neural architecture based on the Kolmogorov–Arnold representation theorem, which approximates multivariate functions using compositions of univariate functions. It is designed to learn highly expressive, structured representations [[15](https://arxiv.org/html/2510.12685v1#bib.bibx15)]. To the best of our knowledge, this work represents the first application of QKAN in intraday electricity price forecasting.

### IV-D Evaluation Metrics

Model performance is evaluated using probabilistic and pointwise metrics. For probabilistic forecasting, we employ the Average Quantile Loss (AQL) and the Average Quantile Crossing Rate (AQCR). For pointwise forecasting, we report the Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and the Coefficient of Determination (R2\text{R}^{2}).

* •

  Average Quantile Loss (AQL).
  AQL is employed to jointly evaluate the accuracy of multiple quantiles [[23](https://arxiv.org/html/2510.12685v1#bib.bibx23)]. It aggregates the quantile loss over all quantile levels:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | AQL=1N​|𝒬|​∑i=1N∑τ∈𝒬Lτ​(yi,y^i,τ),\mathrm{AQL}=\frac{1}{N|\mathcal{Q}|}\sum\_{i=1}^{N}\sum\_{\tau\in\mathcal{Q}}L\_{\tau}(y\_{i},\hat{y}\_{i,\tau}), |  | (4) |

  where yiy\_{i} is the true price, y^i,τ\hat{y}\_{i,\tau} denotes the predicted quantile, and the pinball loss LτL\_{\tau} is defined as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Lτ​(yi,y^i,τ)={τ⋅(yi−y^i,τ),if ​yi≥y^i,τ,(1−τ)⋅(y^i,τ−yi),otherwise.L\_{\tau}(y\_{i},\hat{y}\_{i,\tau})=\begin{cases}\tau\cdot(y\_{i}-\hat{y}\_{i,\tau}),&\text{if }y\_{i}\geq\hat{y}\_{i,\tau},\\ (1-\tau)\cdot(\hat{y}\_{i,\tau}-y\_{i}),&\text{otherwise}.\end{cases} |  | (5) |

  The quantile loss penalizes underestimation more heavily at higher quantiles and overestimation more heavily at lower quantiles.
* •

  Average Quantile Crossing Rate (AQCR).
  AQCR quantifies the frequency of quantile crossing violations [[6](https://arxiv.org/html/2510.12685v1#bib.bibx6)], i.e., instances where a lower quantile prediction exceeds a higher quantile prediction. For each sample ii, and any quantile pair (τl,τu)(\tau\_{l},\tau\_{u}) with τl<τu\tau\_{l}<\tau\_{u}, the crossing indicator is defined as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Cτl,τu​(y^l,i,y^u,i)=𝕀​(y^l,i>y^u,i),C\_{\tau\_{l},\tau\_{u}}(\hat{y}\_{l,i},\hat{y}\_{u,i})=\mathbb{I}(\hat{y}\_{l,i}>\hat{y}\_{u,i}), |  | (6) |

  where 𝕀​(⋅)\mathbb{I}(\cdot) is the indicator function. The overall AQCR is then computed as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | AQCR=1N​∑i=1NCτl,τu​(y^l,i,y^u,i).\text{AQCR}=\frac{1}{N}\sum\_{i=1}^{N}C\_{\tau\_{l},\tau\_{u}}(\hat{y}\_{l,i},\hat{y}\_{u,i}). |  | (7) |

  A lower AQCR indicates better consistency of quantile predictions, with fewer violations across quantile levels.
* •

  Root Mean Squared Error (RMSE).
  RMSE evaluates the overall predictive quality and is sensitive to outliers:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | RMSE=1N​∑i=1N(yi−y^i)2.\text{RMSE}=\sqrt{\frac{1}{N}\sum\_{i=1}^{N}(y\_{i}-\hat{y}\_{i})^{2}}. |  | (8) |
* •

  Mean Absolute Error (MAE).
  MAE measures the average magnitude of the prediction errors:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | MAE=1N​∑i=1N|yi−y^i|.\text{MAE}=\frac{1}{N}\sum\_{i=1}^{N}|y\_{i}-\hat{y}\_{i}|. |  | (9) |
* •

  Coefficient of Determination (R2\text{R}^{2}).
  The R2\text{R}^{2} score quantifies the proportion of variance in the target variable explained by the model:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | R2=1−∑i=1N(yi−y^i)2∑i=1N(yi−y¯)2,\text{R}^{2}=1-\frac{\sum\_{i=1}^{N}(y\_{i}-\hat{y}\_{i})^{2}}{\sum\_{i=1}^{N}(y\_{i}-\bar{y})^{2}}, |  | (10) |

  where y¯\bar{y} is the mean of the true values.

TABLE III: Top 5 features per market, product type, and quantile.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Market | Product Type | Quantile |  |  | Top 5 features |  |  |
| DE | 60-min | 0.1 | Min P.|𝒯15+\;\big|^{+}\_{\mathcal{T}\_{15}} | Min P.|𝒯60+\;\big|^{+}\_{\mathcal{T}\_{60}} | Min P.|𝒯∞+\;\big|^{+}\_{\mathcal{T}\_{\infty}} | Max P.|𝒯∞−\;\big|^{-}\_{\mathcal{T}\_{\infty}} | First P.|𝒯1−\;\big|^{-}\_{\mathcal{T}\_{1}} |
|  |  | 0.5 | P. Pctl.|𝒯5, 90%−\;\big|^{-}\_{\mathcal{T}\_{5},\,90\%} | P. Pctl.|𝒯15, 10%+\;\big|^{+}\_{\mathcal{T}\_{15},\,10\%} | P. Pctl.|𝒯15, 75%−\;\big|^{-}\_{\mathcal{T}\_{15},\,75\%} | Min P.|𝒯15+\;\big|^{+}\_{\mathcal{T}\_{15}} | P. Pctl.|𝒯5, 10%+\;\big|^{+}\_{\mathcal{T}\_{5},\,10\%} |
|  |  | 0.9 | Max P.|𝒯15−\;\big|^{-}\_{\mathcal{T}\_{15}} | P. Pctl.|𝒯∞, 10%+\;\big|^{+}\_{\mathcal{T}\_{\infty},\,10\%} | P. Pctl.|𝒯5, 10%+\;\big|^{+}\_{\mathcal{T}\_{5},\,10\%} | Max P.|𝒯60−\;\big|^{-}\_{\mathcal{T}\_{60}} | Max P.|𝒯180−\;\big|^{-}\_{\mathcal{T}\_{180}} |
|  | 15-min | 0.1 | Min P.|𝒯60+\;\big|^{+}\_{\mathcal{T}\_{60}} | Min P.|𝒯180+\;\big|^{+}\_{\mathcal{T}\_{180}} | Max P.|𝒯1−\;\big|^{-}\_{\mathcal{T}\_{1}} | Mean P.|𝒯5−\;\big|^{-}\_{\mathcal{T}\_{5}} | Min P.|𝒯15+\;\big|^{+}\_{\mathcal{T}\_{15}} |
|  |  | 0.5 | P. Pctl.|𝒯60, 10%+\;\big|^{+}\_{\mathcal{T}\_{60},\,10\%} | P. Pctl.|𝒯15, 90%−\;\big|^{-}\_{\mathcal{T}\_{15},\,90\%} | Min P.|𝒯15+\;\big|^{+}\_{\mathcal{T}\_{15}} | P. Pctl.|𝒯60, 45%−\;\big|^{-}\_{\mathcal{T}\_{60},\,45\%} | P. Pctl.|𝒯60, 25%+\;\big|^{+}\_{\mathcal{T}\_{60},\,25\%} |
|  |  | 0.9 | Max P.|𝒯60−\;\big|^{-}\_{\mathcal{T}\_{60}} | P. Pctl.|𝒯60, 90%−\;\big|^{-}\_{\mathcal{T}\_{60},\,90\%} | Min P.|𝒯1+\;\big|^{+}\_{\mathcal{T}\_{1}} | Max P.|𝒯15−\;\big|^{-}\_{\mathcal{T}\_{15}} | Max P.|𝒯180−\;\big|^{-}\_{\mathcal{T}\_{180}} |
| AT | 60-min | 0.1 | Min P.|𝒯15+\;\big|^{+}\_{\mathcal{T}\_{15}} | Min P.|𝒯∞+\;\big|^{+}\_{\mathcal{T}\_{\infty}} | P. Pctl.|𝒯5, 45%−\;\big|^{-}\_{\mathcal{T}\_{5},\,45\%} | Min P.|𝒯5−\;\big|^{-}\_{\mathcal{T}\_{5}} | First P.|𝒯5−\;\big|^{-}\_{\mathcal{T}\_{5}} |
|  |  | 0.5 | Last P.|𝒯∞−\;\big|^{-}\_{\mathcal{T}\_{\infty}} | Min P.|𝒯5+\;\big|^{+}\_{\mathcal{T}\_{5}} | P. Pctl.|𝒯5, 45%−\;\big|^{-}\_{\mathcal{T}\_{5},\,45\%} | Last P.|𝒯∞+\;\big|^{+}\_{\mathcal{T}\_{\infty}} | Max P.|𝒯1−\;\big|^{-}\_{\mathcal{T}\_{1}} |
|  |  | 0.9 | Max P.|𝒯180−\;\big|^{-}\_{\mathcal{T}\_{180}} | P. Pctl.|𝒯60, 75%+\;\big|^{+}\_{\mathcal{T}\_{60},\,75\%} | Max P.|𝒯1−\;\big|^{-}\_{\mathcal{T}\_{1}} | First P.|𝒯15+\;\big|^{+}\_{\mathcal{T}\_{15}} | P. Pctl.|𝒯1, 10%−\;\big|^{-}\_{\mathcal{T}\_{1},\,10\%} |
|  | 15-min | 0.1 | Min P.|𝒯1−\;\big|^{-}\_{\mathcal{T}\_{1}} | P. Pctl.|𝒯180, 10%+\;\big|^{+}\_{\mathcal{T}\_{180},\,10\%} | Min P.|𝒯15+\;\big|^{+}\_{\mathcal{T}\_{15}} | P. Pctl.|𝒯∞, 10%+\;\big|^{+}\_{\mathcal{T}\_{\infty},\,10\%} | Min P.|𝒯180+\;\big|^{+}\_{\mathcal{T}\_{180}} |
|  |  | 0.5 | Mean P.|𝒯∞+\;\big|^{+}\_{\mathcal{T}\_{\infty}} | Last P.|𝒯∞−\;\big|^{-}\_{\mathcal{T}\_{\infty}} | VWAP|𝒯1+\;\big|^{+}\_{\mathcal{T}\_{1}} | VWAP|𝒯180−\;\big|^{-}\_{\mathcal{T}\_{180}} | Mean P.|𝒯15+\;\big|^{+}\_{\mathcal{T}\_{15}} |
|  |  | 0.9 | Max P.|𝒯1+\;\big|^{+}\_{\mathcal{T}\_{1}} | Max P.|𝒯180+\;\big|^{+}\_{\mathcal{T}\_{180}} | Max P.|𝒯180−\;\big|^{-}\_{\mathcal{T}\_{180}} | Max P.|𝒯1−\;\big|^{-}\_{\mathcal{T}\_{1}} | Max P.|𝒯∞+\;\big|^{+}\_{\mathcal{T}\_{\infty}} |




TABLE IV: Performance comparison of machine learning models.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Market | Product Type | Model | AQL ↓\downarrow | AQCR ↓\downarrow | RMSE ↓\downarrow | MAE ↓\downarrow | R2 ↑\uparrow |  |
| DE | 60-min | LQR† | 3.42±0.00 | 0.05±0.00 | 27.94±0.00 | 10.05±0.00 | 0.87±0.00 |  |
|  |  | QKNN† | 3.51±0.00 | 0.06±0.02 | 28.41±0.00 | 10.33±0.00 | 0.86±0.00 |  |
|  |  | QLGBM | 3.62±0.00 | 0.14±0.03 | 29.88±0.14 | 11.45±0.29 | 0.85±0.01 |  |
|  |  | QXGB | 3.59±0.00 | 0.08±0.03 | 28.75±0.36 | 10.95±0.10 | 0.86±0.01 |  |
|  |  | QMLP | 3.30±0.01 | 0.01±0.00 | 27.67±0.24 | 10.02±0.02 | 0.87±0.00 |  |
|  |  | QKAN | 3.32±0.02 | 0.01±0.00 | 27.69±0.17 | 10.06±0.05 | 0.87±0.00 |  |
|  | 15-min | LQR† | 6.79±0.00 | 0.09±0.00 | 52.68±0.00 | 18.41±0.00 | 0.69±0.00 |  |
|  |  | QKNN† | 6.80±0.00 | 0.10±0.00 | 52.78±0.00 | 18.56±0.00 | 0.69±0.00 |  |
|  |  | QLGBM | 6.82±0.05 | 0.19±0.09 | 52.93±0.37 | 18.37±0.20 | 0.69±0.01 |  |
|  |  | QXGB | 6.75±0.04 | 0.14±0.05 | 52.40±0.41 | 17.97±0.33 | 0.70±0.01 |  |
|  |  | QMLP | 6.56±0.03 | 0.01±0.00 | 50.40±0.32 | 17.84±0.28 | 0.72±0.00 |  |
|  |  | QKAN | 6.56±0.02 | 0.01±0.00 | 50.42±0.27 | 17.88±0.09 | 0.72±0.00 |  |
| AT | 60-min | LQR† | 4.33±0.00 | 0.05±0.00 | 28.61±0.00 | 11.91±0.00 | 0.80±0.00 |  |
|  |  | QKNN† | 4.46±0.00 | 0.04±0.00 | 29.29±0.00 | 12.23±0.00 | 0.79±0.00 |  |
|  |  | QLGBM | 4.49±0.05 | 0.10±0.04 | 29.41±0.42 | 12.14±0.17 | 0.78±0.01 |  |
|  |  | QXGB | 4.45±0.03 | 0.04±0.01 | 28.90±0.38 | 11.97±0.10 | 0.79±0.01 |  |
|  |  | QMLP | 4.20±0.01 | 0.01±0.00 | 28.33±0.23 | 11.69±0.06 | 0.80±0.00 |  |
|  |  | QKAN | 4.19±0.01 | 0.01±0.00 | 28.27±0.14 | 11.75±0.10 | 0.80±0.00 |  |
|  | 15-min | LQR† | 6.44±0.00 | 0.04±0.00 | 52.99±0.00 | 17.82±0.00 | 0.57±0.00 |  |
|  |  | QKNN† | 6.44±0.00 | 0.09±0.00 | 52.02±0.00 | 17.84±0.00 | 0.57±0.00 |  |
|  |  | QLGBM | 6.38±0.11 | 0.05±0.01 | 51.97±0.24 | 17.42±0.18 | 0.57±0.01 |  |
|  |  | QXGB | 6.47±0.08 | 0.07±0.02 | 51.67±0.18 | 17.32±0.15 | 0.58±0.01 |  |
|  |  | QMLP | 6.22±0.06 | 0.01±0.00 | 51.24±0.22 | 17.18±0.21 | 0.58±0.00 |  |
|  |  | QKAN | 6.22±0.08 | 0.01±0.00 | 51.15±0.11 | 17.09±0.14 | 0.58±0.00 |  |

## V Generalization Assessment

To assess the model’s generalizability across countries and product types, we conduct two sets of experiments: (1) cross-country generalization, where the model is transferred between DE and AT; and (2) cross-product-type generalization, where the model is transferred between 60-min and 15-min products.
For both experiments, the following three transfer strategies are applied:

* •

  A →\rightarrow A: Use the optimal feature set derived from domain A; train and optimize the model on data from domain A; test it on domain A.
* •

  B →\rightarrow A: Use the optimal feature set derived from domain B; train and optimize the model on data from domain B; test on domain A.
* •

  A + B →\rightarrow A: Use the union of optimal feature sets from both domains A and B; train and optimize the model on combined data from A and B; test on domain A.

Furthermore, we introduce two measures to quantify the phenomenon of asymmetric generalization: the *loss ratio* ℒ\mathcal{L} and the *trade-count ratio* 𝒞\mathcal{C}, defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=AQL​(B→A)AQL​(A→A),\mathcal{L}\;=\;\frac{\mathrm{AQL}(\text{B}\!\to\!\text{A})}{\mathrm{AQL}(\text{A}\!\to\!\text{A})}, |  | (11) |

where AQL​(B→A)\mathrm{AQL}(\text{B}\!\to\!\text{A}) and AQL​(A→A)\mathrm{AQL}(\text{A}\!\to\!\text{A}) are testing loss and can be retrieved from Table [V](https://arxiv.org/html/2510.12685v1#S6.T5 "TABLE V ‣ VI-A Feature Extraction and Selection ‣ VI Experiment ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets"). A higher value of ℒ\mathcal{L} indicates that a model transferred from domain B performs worse on domain A than a model trained directly on domain A;

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞=NBNA,\mathcal{C}\;=\;\frac{N\_{\text{B}}}{N\_{\text{A}}}, |  | (12) |

where NAN\_{\text{A}} and NBN\_{\text{B}} represent the average count of matched trades across testing samples for domains A and B, respectively. These values reflect the market liquidity and are illustrated in Fig. [3](https://arxiv.org/html/2510.12685v1#S7.F3 "Figure 3 ‣ VII Conclusion ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets") (a), where DE 60-min exhibits the highest trade count (most liquid), and AT 15-min the lowest (least liquid). A higher value of 𝒞\mathcal{C} indicates that transfer learning is performed from a more liquid domain to a less liquid one.

### V-A Cross-Country Generalization

In this setting, domains A and B refer to countries. Specifically, A can be either DE or AT, and B is the other. We evaluate model generalization across countries for the 60-min and 15-min product types, respectively.

### V-B Cross-Product-Type Generalization

In this setting, domains A and B refer to product types. Specifically, A can be either the 60-min or 15-min product, and B is the other. We evaluate model generalization across product types for the DE and AT markets, respectively.

## VI Experiment

The orderbook is split into training (2022-01-01 to 2024-01-01), validation (2024-01-01 to 2024-07-01), and testing (2024-07-01 to 2025-01-01) periods. The testing window is chosen to examine the model’s performance on more recent, up-to-date data.
For the 60-min and 15-min products, a prediction is generated every 60 minutes and 15 minutes, respectively.

![Refer to caption](x2.png)


Figure 2: 
Analysis of feature selection and its impact on forecasting performance.
a–c Distribution of absolute feature importance by feature type, look-back window size, and market side, respectively.
d Testing loss (AQL) for different feature sets across countries and resolutions.

### VI-A Feature Extraction and Selection

We retain features with non-zero coefficients and analyze their importance by summing the absolute coefficient magnitudes across feature type, look-back window size, and market side, respectively. As shown in Fig. [2](https://arxiv.org/html/2510.12685v1#S6.F2 "Figure 2 ‣ VI Experiment ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets") (a), the most important feature types are price percentiles (29.9%), minimum prices (26.3%), and maximum prices (21.9%), while the volume-based features do not contribute much in terms of coefficient magnitude.
In Fig. [2](https://arxiv.org/html/2510.12685v1#S6.F2 "Figure 2 ‣ VI Experiment ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets") (b), features extracted from the last 15 and 60 minutes contribute the most (23.4% and 20.6%). Surprisingly, the last 1-minute window contributes only 11.3% of total importance. This may be due to the volatility and noise in short-term trading activity. Fig. [2](https://arxiv.org/html/2510.12685v1#S6.F2 "Figure 2 ‣ VI Experiment ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets") (c) shows that buy-side features slightly dominate sell-side features, although the difference is marginal.

To evaluate the impact of feature selection on performance, we rank all features by their absolute coefficient values per market, product type, and quantile. The LQR models are retrained using: only the top 1 feature; the top 5 features; and all the selected features. Additionally, we include two previously reported strong predictors as benchmarks: VWAP over the last 15 minutes (Naive1) and the last price (Naive2). As shown in Fig. [2](https://arxiv.org/html/2510.12685v1#S6.F2 "Figure 2 ‣ VI Experiment ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets") (d), the selected full feature set significantly outperforms both naive baselines, achieving on average 10.53% and 11.87% lower testing loss compared to Naive1 and Naive2, respectively. Moreover, the top 5 features are often sufficient to match the performance of the full set, indicating redundancy among weaker features. While the top 1 feature yields comparable performance to the top 5 in the 15-minute product in DE, it performs worse in other settings. Therefore, we proceed by using the top 5 features, revealed in Table [III](https://arxiv.org/html/2510.12685v1#S4.T3 "TABLE III ‣ IV-D Evaluation Metrics ‣ IV Model Comparison ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets"), for the downstream forecasting task.

TABLE V: Cross-domain generalization performance.

| Cross-Country Generalization | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Product Type | Trans. Strategy | AQL ↓\downarrow | AQCR ↓\downarrow | RMSE ↓\downarrow | MAE ↓\downarrow | R2 ↑\uparrow |
| 60-min | DE →\rightarrow DE | 3.30±0.01 | 0.01±0.00 | 27.67±0.24 | 10.02±0.01 | 0.87±0.00 |
|  | AT →\rightarrow DE | \cellcolororange23.84±13.34 | 0.41±0.10 | 35.60±9.64 | 11.60±1.61 | 0.78±0.12 |
|  | DE ++ AT →\rightarrow DE | 3.47±0.02 | 0.01±0.00 | 27.91±0.09 | 10.12±0.04 | 0.86±0.01 |
|  | AT →\rightarrow AT | 4.20±0.01 | 0.01±0.00 | 28.33±0.23 | 11.69±0.06 | 0.80±0.00 |
|  | DE →\rightarrow AT | \cellcolorcustombeige4.20±0.01 | 0.02±0.00 | 28.85±0.06 | 11.98±0.04 | 0.80±0.00 |
|  | DE ++ AT →\rightarrow AT | 4.15±0.01 | 0.01±0.00 | 28.23±0.05 | 11.55±0.07 | 0.80±0.00 |
| 15-min | DE →\rightarrow DE | 6.56±0.03 | 0.01±0.00 | 50.40±0.32 | 17.84±0.28 | 0.72±0.00 |
|  | AT →\rightarrow DE | \cellcolororange80.15±11.23 | 0.08±0.01 | 88.99±8.16 | 39.48±2.84 | 0.12±0.16 |
|  | DE ++ AT →\rightarrow DE | 8.89±0.41 | 0.06±0.04 | 55.29±2.08 | 21.94±1.33 | 0.66±0.03 |
|  | AT →\rightarrow AT | 6.22±0.06 | 0.01±0.00 | 51.24±0.22 | 17.18±0.21 | 0.58±0.00 |
|  | DE →\rightarrow AT | \cellcolorcustombeige6.27±0.12 | 0.02±0.04 | 52.89±0.13 | 17.79±0.19 | 0.58±0.00 |
|  | DE ++ AT →\rightarrow AT | 6.20±0.03 | 0.00±0.00 | 51.00±0.04 | 17.04±0.09 | 0.58±0.00 |
| Cross-Product-Type Generalization | | | | | | |
| Market | Trans. Strategy | AQL ↓\downarrow | AQCR ↓\downarrow | RMSE ↓\downarrow | MAE ↓\downarrow | R2 ↑\uparrow |
| DE | 60-min →\rightarrow 60-min | 3.30±0.01 | 0.01±0.00 | 27.67±0.24 | 10.02±0.01 | 0.87±0.00 |
|  | 15-min →\rightarrow 60-min | \cellcolororange4.45±0.42 | 0.04±0.03 | 28.90±0.07 | 10.34±0.11 | 0.86±0.00 |
|  | 60-min ++ 15-min →\rightarrow 60-min | 3.57±0.01 | 0.02±0.00 | 27.98±0.12 | 10.13±0.06 | 0.87±0.00 |
|  | 15-min →\rightarrow 15-min | 6.56±0.03 | 0.01±0.00 | 50.40±0.32 | 17.84±0.28 | 0.72±0.00 |
|  | 60-min →\rightarrow 15-min | \cellcolorcustombeige6.59±0.28 | 0.02±0.00 | 50.83±2.39 | 17.89±0.35 | 0.72±0.00 |
|  | 60-min ++ 15-min →\rightarrow 15-min | 6.33±0.02 | 0.01±0.00 | 50.10±0.36 | 17.63±0.07 | 0.72±0.00 |
| AT | 60-min →\rightarrow 60-min | 4.20±0.01 | 0.01±0.00 | 28.33±0.23 | 11.69±0.06 | 0.80±0.00 |
|  | 15-min →\rightarrow 60-min | \cellcolororange8.17±3.90 | 0.13±0.23 | 29.99±0.24 | 12.41±0.10 | 0.78±0.00 |
|  | 60-min ++ 15-min →\rightarrow 60-min | 4.46±0.04 | 0.02±0.00 | 29.47±0.03 | 12.16±0.04 | 0.79±0.00 |
|  | 15-min →\rightarrow 15-min | 6.22±0.06 | 0.01±0.00 | 51.24±0.22 | 17.18±0.21 | 0.58±0.00 |
|  | 60-min →\rightarrow 15-min | \cellcolorcustombeige6.22±0.09 | 0.01±0.00 | 52.18±0.25 | 17.59±0.11 | 0.58±0.00 |
|  | 60-min ++ 15-min →\rightarrow 15-min | 6.21±0.05 | 0.00±0.00 | 51.15±0.05 | 17.05±0.05 | 0.58±0.00 |

### VI-B Model Comparison

The results of the model comparison are illustrated in Table [IV](https://arxiv.org/html/2510.12685v1#S4.T4 "TABLE IV ‣ IV-D Evaluation Metrics ‣ IV Model Comparison ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets"), where all metrics are reported as mean±standard deviation over 5 independent runs.
The best results are in bold. Models marked with † lack random-seed control; thus, the standard deviation is zero.
The units of AQL, RMSE, and MAE are expressed in €/MWh, and AQCR in %. We observe substantial variation in AQL across probabilistic forecasting scenarios. Specifically,
the difficulty in probabilistic forecasting is in the order: DE, 60-min << AT, 60-min << AT, 15-min << DE, 15-min, as indicated by the average AQL across models.
This order contradicts the volatility order: AT, 60-min << DE, 60-min << AT, 15-min << DE, 15-min, as observed from Fig. [1](https://arxiv.org/html/2510.12685v1#S1.F1 "Figure 1 ‣ I Introduction ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets").
One possible explanation is that the higher liquidity in the DE market provides richer and more stable predictive features for 60-min products, partially offsetting the impact of volatility. In contrast, the AT 60-min product combines lower volatility with lower liquidity compared to the DE 60-min product, and the lower liquidity increases the difficulty of probabilistic forecasting.

Among the six models compared, the deep learning approaches consistently outperform classical statistical models and tree-based ensembles. In particular, QMLP achieves on average 3.45% and 4.59% lower AQL than LQR and QKNN, respectively, when averaged across markets and product types.
Furthermore, QLGBM and QXGB result in 5.08% and 4.83% higher AQL on average compared to QMLP.
In addition, the classical statistical methods and tree-based ensembles exhibit higher AQCR values, ranging from 0.04% to 0.19%, indicating more unreliable probabilistic forecasting. This issue is expected to be further magnified when predicting additional quantiles.
We also note that QMLP and QKAN perform nearly identically across all metrics.
However, QKAN requires approximately 9.7 times longer training time per epoch due to its neural decomposition and multivariate integration structure. Therefore, QMLP offers the best trade-off between computational efficiency and predictive performance and is selected for the downstream generalization assessment.

### VI-C Generalization Assessment

In the cross-country experiments, models trained on the DE market generalize well to the AT market, while the reverse direction results in substantial degradation of performance, as observed from Table [V](https://arxiv.org/html/2510.12685v1#S6.T5 "TABLE V ‣ VI-A Feature Extraction and Selection ‣ VI Experiment ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets").
In both 60-min and 15-min settings, separate training achieves the best performance across all metrics when predicting DE prices, while joint training leads to the best or equivalent performance when predicting AT prices.
Notably, when directly transferring a model trained on AT orderbook data, the AQL increases drastically from 3.30 to 23.84 for the 60-min product and from 6.56 to 80.15 for the 15-min product (highlighted in orange in the table).
In contrast, DE-trained models maintain similar performance when applied directly to the AT market (highlighted in gray in the table). These results highlight a clear asymmetric phenomenon: the higher liquidity of the DE market supports generalization toward the less liquid AT market.

In the cross-product-type experiments, models trained on the 60-min product generalize well to the 15-min product, while the reverse direction again leads to inferior performance, as observed from Table [V](https://arxiv.org/html/2510.12685v1#S6.T5 "TABLE V ‣ VI-A Feature Extraction and Selection ‣ VI Experiment ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets").
In both DE and AT markets, separate training yields the best results across all metrics when predicting 60-min prices, whereas joint training improves or maintains performance when predicting 15-min prices.
Notably, directly transferring a model trained on 15-min data results in AQL increases from 3.30 to 4.45 in DE and from 4.20 to 8.17 in AT (highlighted in orange in the table).
Meanwhile, transferring from 60-min to 15-min retains similar performance compared to separate training (highlighted in gray in the table). These results again highlight that the asymmetric phenomenon is caused by liquidity, as 60-min products contain more trades. In contrast, 15-min products are sparser and more volatile, limiting their generalizability to coarser timescales.

Fig. [3](https://arxiv.org/html/2510.12685v1#S7.F3 "Figure 3 ‣ VII Conclusion ‣ Orderbook Feature Learning and Asymmetric Generalization in Intraday Electricity Markets") (b) shows the scatter of (𝒞,ℒ)(\mathcal{C},\mathcal{L}) and its empirical fitting curve. For 𝒞≥1\mathcal{C}\geq 1, where transfer learning is performed from a more liquid domain to a less liquid one, the loss ratio remains at ℒ=1\mathcal{L}=1, indicating performance equivalent to training directly on the target domain. In contrast, for 𝒞<1\mathcal{C}<1, where transfer occurs from a less liquid domain to a more liquid one, a clear exponential trend is observed: as 𝒞\mathcal{C} decreases, the loss ratio ℒ\mathcal{L} increases sharply, indicating worse performance compared to target-only training. These observations confirm the role of liquidity in transfer performance and support the emergence of the asymmetric generalization phenomenon.

## VII Conclusion

In this paper, we developed a comprehensive feature set consisting of 384 orderbook features and revealed that price percentiles and extreme prices outperform the previously reported powerful features such as VWAP and last price. Moreover, through model comparison, we find that deep learning models consistently outperform classical statistical models and tree-based ensembles. In particular, QMLPs emerge as a strong baseline for probabilistic forecasting when using domain features. Finally, our generalization assessment uncovers a pronounced asymmetry in transferability: models trained on more liquid markets or products generalize well to less liquid domains, while the reverse transfer leads to substantial performance degradation. These findings underscore the importance of market liquidity in designing better models for probabilistic intraday electricity price forecasting.

![Refer to caption](x3.png)


Figure 3: 
Analysis of model performance against market liquidity.
(a) Comparison of market liquidity.
(b) Loss ratio versus trade-count ratio.

## VIII Limitation and Future Work

First, the extracted features in this study are empirical and may benefit from exploring a broader feature set in future work. Second, as markets become more efficient, simpler indicators such as the last price may become sufficient. We will monitor such developments, particularly as electricity markets transition to full quarter-hourly resolution. Third, the hyperparameters are tuned empirically. Additional hyperparameter tuning and a larger number of trials may further improve performance, potentially enabling tree-based models to match the performance of deep learning models. Lastly, this work focuses on the central regions in Europe; extending the analysis to Nordic markets is worth exploring.

## References

* [1]
  Takuya Akiba et al.
  “Optuna: A Next-generation Hyperparameter Optimization Framework”
  In *Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, KDD ’19
  Anchorage, AK, USA: Association for Computing Machinery, 2019, pp. 2623–2631
  DOI: [10.1145/3292500.3330701](https://dx.doi.org/10.1145/3292500.3330701)
* [2]
  José R Andrade, Jorge Filipe, Marisa Reis and Ricardo J Bessa
  “Probabilistic price forecasting for day-ahead and intraday markets: Beyond the statistical model”
  In *Sustainability* 9.11
  MDPI, 2017, pp. 1990
* [3]
  Pallab K Bhattacharya and Ashis K Gangopadhyay
  “Kernel and nearest-neighbor estimation of a conditional quantile”
  In *The Annals of Statistics*
  JSTOR, 1990, pp. 1400–1415
* [4]
  Christopher M. Bishop
  “Neural Networks for Pattern Recognition”
  Oxford University Press, 1995
* [5]
  Tianqi Chen and Carlos Guestrin
  “XGBoost: A Scalable Tree Boosting System”
  In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, KDD ’16
  San Francisco, California, USA: Association for Computing Machinery, 2016, pp. 785–794
  DOI: [10.1145/2939672.2939785](https://dx.doi.org/10.1145/2939672.2939785)
* [6]
  Victor Chernozhukov, Iván Fernández-Val and Alfred Galichon
  “Quantile and Probability Curves Without Crossing”
  In *Econometrica* 78.3, 2010, pp. 1093–1125
  DOI: [https://doi.org/10.3982/ECTA7880](https://dx.doi.org/https://doi.org/10.3982/ECTA7880)
* [7]
  Eike Cramer, Dirk Witthaut, Alexander Mitsos and Manuel Dahmen
  “Multivariate probabilistic forecasting of intraday electricity prices using normalizing flows”
  In *Applied Energy* 346
  Elsevier, 2023, pp. 121370
* [8]
  Eugene F Fama
  “Efficient capital markets”
  In *Journal of finance* 25.2, 1970, pp. 383–417
* [9]
  Simon Hirsch and Florian Ziel
  “Multivariate simulation-based forecasting for intraday power markets: Modeling cross-product price effects”
  In *Applied Stochastic Models in Business and Industry*
  Wiley Online Library, 2024
* [10]
  Simon Hirsch and Florian Ziel
  “Simulation-based forecasting for intraday power markets: Modelling fundamental drivers for location, shape and scale of the price distribution”
  In *The Energy Journal* 45.3
  SAGE Publications Sage CA: Los Angeles, CA, 2024, pp. 107–144
* [11]
  Tim Janke and Florian Steinke
  “Forecasting the price distribution of continuous intraday electricity trading”
  In *Energies* 12.22
  MDPI, 2019, pp. 4262
* [12]
  Guolin Ke et al.
  “LightGBM: A Highly Efficient Gradient Boosting Decision Tree”
  In *Advances in Neural Information Processing Systems* 30
  Curran Associates, Inc., 2017
  URL: <https://proceedings.neurips.cc/paper_files/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Paper.pdf>
* [13]
  Deniz Kenan Kılıç, Peter Nielsen and Amila Thibbotuwawa
  “Intraday Electricity Price Forecasting via LSTM and Trading Strategy for the Power Market: A Case Study of the West Denmark DK1 Grid Region”
  In *Energies* 17.12, 2024
  DOI: [10.3390/en17122909](https://dx.doi.org/10.3390/en17122909)
* [14]
  Roger Koenker and Gilbert Bassett
  “Regression quantiles”
  In *Econometrica* 46.1
  JSTOR, 1978, pp. 33–50
* [15]
  Ziming Liu et al.
  “KAN: Kolmogorov–Arnold Networks”
  In *The Thirteenth International Conference on Learning Representations*, 2025
  URL: <https://openreview.net/forum?id=Ozo7qJ5vZi>
* [16]
  Grzegorz Marcjasz, Bartosz Uniejewski and Rafał Weron
  “Beating the Naïve—Combining LASSO with Naïve Intraday Electricity Price Forecasts”
  In *Energies* 13.7, 2020
  DOI: [10.3390/en13071667](https://dx.doi.org/10.3390/en13071667)
* [17]
  Claudio Monteiro, Ignacio J Ramirez-Rosado, L Alfredo Fernandez-Jimenez and Pedro Conde
  “Short-term price forecasting models based on artificial neural networks for intraday sessions in the Iberian electricity market”
  In *Energies* 9.9
  MDPI, 2016, pp. 721
* [18]
  Michał Narajewski and Florian Ziel
  “Econometric modelling and forecasting of intraday electricity prices”
  In *Journal of Commodity Markets* 19
  Elsevier, 2020, pp. 100107
* [19]
  Michał Narajewski and Florian Ziel
  “Ensemble forecasting for intraday electricity prices: Simulating trajectories”
  In *Applied Energy* 279
  Elsevier, 2020, pp. 115801
* [20]
  Christoph Scholz, Malte Lehna, Katharina Brauns and André Baier
  “Towards the Prediction of Electricity Prices at the Intraday Market Using Shallow and Deep-Learning Methods”
  In *Mining Data for Financial Applications*
  Cham: Springer International Publishing, 2021, pp. 101–118
* [21]
  Tomasz Serafin, Grzegorz Marcjasz and Rafał Weron
  “Trading on short-term path forecasts of intraday electricity prices”
  In *Energy Economics* 112
  Elsevier, 2022, pp. 106125
* [22]
  Bartosz Uniejewski, Grzegorz Marcjasz and Rafał Weron
  “Understanding intraday electricity markets: Variable selection and very short-term price forecasting using LASSO”
  In *International Journal of Forecasting* 35.4, 2019, pp. 1533–1547
  DOI: [https://doi.org/10.1016/j.ijforecast.2019.02.001](https://dx.doi.org/https://doi.org/10.1016/j.ijforecast.2019.02.001)
* [23]
  Runyao Yu et al.
  “OrderFusion: Encoding Orderbook for End-to-End Probabilistic Intraday Electricity Price Prediction”
  In *arXiv preprint arXiv:2502.06830*, 2025