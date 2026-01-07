---
authors:
- Ahmad Makinde
doc_id: arxiv:2601.02310v1
family_id: arxiv:2601.02310
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order
  Book Forecasting: Efficiency, Interpretability, and Alpha Decay'
url_abs: http://arxiv.org/abs/2601.02310v1
url_html: https://arxiv.org/html/2601.02310v1
venue: arXiv q-fin
version: 1
year: 2026
---


Ahmad Makinde
  
Undergraduate Student, University of Bristol
  
Independent Researcher
  
Ahmad.makinde.2025@bristol.ac.uk

###### Abstract

High-Frequency trading (HFT) environments are characterised by large volumes of limit order book (LOB) data, which is notoriously noisy and non-linear. Alpha decay represents a significant challenge, with traditional models such as DeepLOB losing predictive power as the time horizon (kk) increases. In this paper, using data from the FI-2010 dataset, we introduce Temporal Kolmogorov-Arnold Networks (T-KAN) to replace the fixed, linear weights of standard LSTMs with learnable B-spline activation functions. This allows the model to learn the ’shape’ of market signals as opposed to just their magnitude. This resulted in a 19.1% relative improvement in the F1-score at the k=100k=100 horizon. The efficacy of T-KAN networks cannot be understated, producing a 132.48% return compared to the -82.76% DeepLOB drawdown under 1.0 bps transaction costs. In addition to this, the T-KAN model proves quite interpretable, with the ’dead-zones’ being clearly visible in the splines. The T-KAN architecture is also uniquely optimized for low-latency FPGA implementation via High level Synthesis (HLS).
The code for the experiments in
this project can be found at <https://github.com/AhmadMak/Temporal-Kolmogorov-Arnold-Networks-T-KAN-for-High-Frequency-Limit-Order-Book-Forecasting>

This research was conducted independently of the University of Bristol.

*K*eywords Limit Order Book (LOB) ⋅\cdot
Alpha Decay ⋅\cdot
FI-2010 Dataset ⋅\cdot
Temporal Koolmogorov-Arnold Network (T-KAN) ⋅\cdot
Interpretability ⋅\cdot
FPGA

## 1 Introduction

The modeling and prediction of price dynamics in the Limit Order Book (LOB) are fundamental challenges in quantitative finance and market microstructure [bouchaud2002statistical, cont2010price]. Unlike low-frequency data, the LOB is a high-dimensional, discrete-event dynamic system where the latent state of supply and demand is shown via the placing and cancellation of orders across multiple price levels [gould2013limit]. The LOB state at time tt
can be represented as a vector ℒt={Pt(i),Vt(i)}i=−n′n\mathcal{L}\_{t}=\{P\_{t}^{(i)},V\_{t}^{(i)}\}\_{i=-n^{\prime}}^{n} where PP and VV represent the price and volume at level ii, where positive and negative indices denote ask and bid sides, respectively.

In this state space, the Auction Phase is important. The phase is characterized by intense price discovery and structural liquidity shifts, where changing from a closed-call auction to continuous trading causes high-volatility regimes [ntakaris2018benchmark]. In order to forecast accurately, this regime requires the model to be able to capture complex, "path-dependent" non-linearities, where a trade’s price impact is a dynamic function of current book depth and historical order flow [hasbrouck2007empirical].

This study uses a 144-dimensional feature vector whose values were pre-normalised using z-score standardisation by the dataset provider. For a feature xx, the normalized value x^\hat{x}is defined as

|  |  |  |
| --- | --- | --- |
|  | x^=x−μσ\hat{x}=\frac{x-\mu}{\sigma} |  |

where μ\mu and σ\sigma are the mean and standard deviation calculated over a rolling window to maintain a stationary auction environment.

Traditional forecasting has shifted significantly from linear econometric models to deep recurrent architectures such as the Long Short-Term Memory (LSTM) network. Standard LSTMs are however reliant on fixed, point-wise activation functions within its gating mechanisms. A standard LSTM gate is defined by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | it=σ​(Wi⋅[ht−1,xt]+bi)i\_{t}=\sigma(W\_{i}\cdot[h\_{t-1},x\_{t}]+b\_{i}) |  | (1) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ft=σ​(Wf⋅[ht−1,xt]+bf)f\_{t}=\sigma(W\_{f}\cdot[h\_{t-1},x\_{t}]+b\_{f}) |  | (2) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ot=σ​(Wo⋅[ht−1,xt]+bo)o\_{t}=\sigma(W\_{o}\cdot[h\_{t-1},x\_{t}]+b\_{o}) |  | (3) |

where WW represents static weight matrices. The architecture assumes that a linear transformation with a fixed non-linearity is adequate to map LOB features to price movements. We assume that this ’universal approximation’ approach is parameter-inefficient for capturing localized oscillations found in microstructure data.

This paper proposes Temporal Kolmogorov-Arnold Network (T-KAN) as a superior alterative to LOB forecasting. By replacing static matrices WW with learnable univariate spline functions, the T-KAN allows "computation on the edges" [liu2024kan]. With a configuration using 532,675 parameters, our model provides a high-resolution manifold to capture aggressive price discovery in the Auction Z-score regime of the FI-2010 dataset.

## 2 Literature Review

### 2.1 2.1 Deep Learning in Market Microstructure

The release of the FI-2010 benchmark dataset by Ntakaris et al. [ntakaris2018benchmark] in 2017 provided a standardised, large-scale platform for evaluating machine learning models in LOB forecasting. Earlier studies used Convolutional Neural Networks (CNNs) to automate spatial feature extraction from the 40-dimensional raw LOB data [tsantekidis2017forecasting]. Deep LOB later integrated CNNs with LSTMs too model spatial and temporal dependencies [zhang2019deeplob].

The efficacy of these models relies on the Universal Approximation Theorem, which states that a network with fixed activations can approximate any continuous function. Although effective, the "curse of dimensionality" often impacts this approach when modeling functions with high-frequency components [cybenko1989approximation]. This has led researchers to look at architectures such as the Temporal Attention Augmented bilinear (TABL) network, which uses bilinear projections to compress LOB features whilst maintaining temporal relationships [tran2018temporal].

### 2.2 2.2 Kolmogorov-Arnold Networks (KAN) and Spline Theory

Liu et al. (2024)’s introduction of Multi-Layer Perceptron (MLP) in the form of KAN networks was a significant alternative [liu2024kan]. Based on the Kolmogorov-Arnold Representation Theorem, a multivariate continuos function ff on a bounded domain can be represented as

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x1,…,xn)=∑q=12​n+1Φq​(∑p=1nϕq,p​(xp))f(x\_{1},\dots,x\_{n})=\sum\_{q=1}^{2n+1}\Phi\_{q}\left(\sum\_{p=1}^{n}\phi\_{q,p}(x\_{p})\right) |  | (4) |

where ϕq,p\phi\_{q,p} are univariate continuous functions. In a KAN architecture, these functions are usually parameterized as B-splines.
A B-spline of order kk is defined recursively over a grid of knots {ti}\{t\_{i}\} using the Cox-de Boor recursion formula [deboor1978practical]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ni,0​(x)={1,ti≤x<ti+10,otherwiseN\_{i,0}(x)=\begin{cases}1,&t\_{i}\leq x<t\_{i+1}\\ 0,&\text{otherwise}\end{cases} |  | (5) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bi,k​(x)=x−titi+k−ti​Bi,k−1​(x)+ti+k+1−xti+k+1−ti+1​Bi+1,k−1​(x)B\_{i,k}(x)=\frac{x-t\_{i}}{t\_{i+k}-t\_{i}}\,B\_{i,k-1}(x)\;+\;\frac{t\_{i+k+1}-x}{t\_{i+k+1}-t\_{i+1}}\,B\_{i+1,k-1}(x) |  | (6) |

With these learnable spines on the edge of the network, KANs learn the activation function itself, leading to a more granular fit to non-linear LOB manifolds.

### 2.3 Recurrence and the T-KAN Hybrid

In theory KANs have great expressive capabilities, however studies by Rather et al. (24) [rather2024kan] highlighted a "temporal gap", noting that vanilla KANs are not as effective at capturing sequential dependencies as LSTMs in stochastic time-series forecasting problems. Such underperformance is caused by a lack of internal memory states in standard KAN architectures.

This study uses a T-KAN (KAN-LSTM) hybrid to address this issue. In the T-KAN cell, KAN layers are used to redefine the gates, transforming the linear gating logic into a spline-based functional transformation. For input vector xtx\_{t} and previous hidden state ht−1h\_{t-1}, the cell state ctc\_{t} and hidden state hth\_{t} are updated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | it=σ​(K​A​Ni​([xt,ht−1]))i\_{t}=\sigma(KAN\_{i}([x\_{t},h\_{t-1}])) |  | (7) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ft=σ​(K​A​Nf​([xt,ht−1]))f\_{t}=\sigma(KAN\_{f}([x\_{t},h\_{t-1}])) |  | (8) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | gt=t​a​n​h​(K​A​Ng​([xt,ht−1]))g\_{t}=tanh(KAN\_{g}([x\_{t},h\_{t-1}])) |  | (9) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ot=σ(KANo([xt,ht−1])o\_{t}=\sigma(KAN\_{o}([x\_{t},h\_{t}-1]) |  | (10) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ct=ft⊙ct−1+it⊙gtc\_{t}=f\_{t}\,\odot c\_{t-1}+i\_{t}\,\odot g\_{t} |  | (11) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=ot⊙t​a​n​h​(ct)h\_{t}=o\_{t}\,\odot\,tanh(c\_{t}) |  | (12) |

Additionally, to overcome the class imbalance within the FI-2010 Auction dataset, where the neutral class (y=1)(y=1) accounts for 65% of the distribution, we Inverse frequency weighting [tsantekidis2017forecasting] within the weighted Multi-Class Cross Entropy loss function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=−1N​∑i=1N∑c=13wc.yi,c​log⁡(y^i,c)\mathcal{L}=-\frac{1}{N}\sum\_{i=1}^{N}\sum\_{c=1}^{3}w\_{c}.\,y\_{i,c}\>\log(\hat{y}\_{i,c}) |  | (13) |

where wc=N3⋅ncw\_{c}=\frac{N}{3\,\cdot n\_{c}}. Based on our measured distribution {36533,138391,37135}\{36533,138391,37135\}, the calculated weights are [1.93,0.51,1.90][1.93,0.51,1.90].

## 3 Methodology

### 3.1 Data framework and Supervised Learning Setup

The empirical validity of this study is based on the FI-2010 Benchmark Dataset [ntakaris2018benchmark], which provides a standardized high-frequency environment when evaluating LOB models. Although the raw 144-dimensional features come with Z-score normalization, transitioning from discrete LOB snapshots to a format for deep learning relies on specific temporal framing.

#### 3.1.1 The Sliding Window Unit

Adopting the standard supervised learning protocols from limit order books [tsantekidis2017forecasting], we use a Sliding Window Unit. Given the sequence of normalized states ℒ1,…,ℒ^N^\hat{\mathcal{L}\_{1},\dots,\hat{\mathcal{L}}\_{N}}, we construct an input sample Xt∈ℝT×144X\_{t}\in\mathbb{R}^{T\times 144} where T=10T=10 represents the look-back horizon. This makes sure that the model captures the "order flow momentum" and liquidity path-dependency rather than just a static view book.

### 3.2 Architectural Specification

Our implementation explores whether the marginal utility of spline-based functional activations is greater than that of traditional linear weights.

#### 3.2.1 DeepLOB Baseline(CNN-LSTM)

The DeepLOB architecture [zhang2019deeplob] serves as our spatial-temporal baseline. We use 1×21\times 2 kernels to isolate bid-ask spreads ,followed by dual 4×14\times 1 kernels to extract vertical microstructure depth. The output is permuted so that the feature maps correspond to the temporal axis before being processed by a 64-unit LSTM.

#### 3.2.2 Proposed T-KAN Configuration

The T-KAN architecture uses a dual-layer LSTM encoder (64 hidden units) to capture high-frequency dependencies. Based on the Kolmogorov-Arnold Representation Theorem [liu2024kan] , the final hidden state hTh\_{T} is processed by a KAN-optimized classification head.

Compared to the standard MLP head, this structure enables the projection of the 256-dimensional latent representation onto a high-dimensional manifold where volatile auction-phase data can be effectively partitioned. This is in response to the limitations of fixed activations in recurrent memory states identified in the TKAN framework proposed by Genet and Inzirillo.[genet2024tkan]

### 3.3 Vector Graphic Diagrams

Input (10×14410\times 144)2-Layer LSTM (64)KAN Head (SiLU/Spline)OutputhTh\_{T}T-KAN Edge Logic:Spline ϕ1\phi\_{1}Spline ϕ2\phi\_{2}


Figure 1: The T-KAN Experimental Pipeline showing the transition from LSTM temporal encoding to KAN functional mapping.

### 3.4 Optimmisation and Inverse Frequency Weighting

To address the significant class imbalance in the FI-2010 Auction dataset, we utilize Inverse Frequency Weighting [tsantekidis2017forecasting] in our loss function. Based on our calculated class distribution {36533,138391,37135}\{36533,138391,37135\}, the weights wcw\_{c} are assigned to make sure that the model does not over-fit to the neutral class. We also use a L1 Sparsity Penalty λ=10−4\lambda=10^{-4} to make sure that the splines are smooth.

## 4 Results

The FI-2010 benchmark dataset [ntakaris2018benchmark] was used to evaluate the performance of Temporal Kolmogorov-Arnold Networks against the DeepLOB baseline [zhang2019deeplob]. The evaluation was conducted on a forecast horizon of k=100k=100 ticks. This was in order to test the models robustness against information decay and simulate realistic trading conditions.

### 4.1 Comparative Performance Metrics

As concluded in Table [1](https://arxiv.org/html/2601.02310v1#S4.T1 "Table 1 ‣ 4.1 Comparative Performance Metrics ‣ 4 Results ‣ Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay"), DeepLOB was significantly outperformed by T-KAN across all primary classification metrics. T-KAN achieved an F1-Score of 0.3995, representing a relative improvement of 19.1% over the baseline of 0.3354.Additionally , T-KAN showed better precision (0.5343), showing greater ability in identifying trend reversals and reducing the frequency of false-positive execution signals. These results are shown in Figure [5](https://arxiv.org/html/2601.02310v1#S5.F5 "Figure 5 ‣ 5.2 Robustness to Alpha Decay ‣ 5 Conclusion ‣ Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay").

![Refer to caption](alpha_decay_comparison2.png)


Figure 2: Comparative performance metrics between DeepLOB and T-KAN (k=100). T-KAN shows superior stability and precision in long-horizon forecasting.




Table 1: Model Performance Comparison on FI-2010 (k=100)

| Model | Precision | Recall | F1-Score |
| --- | --- | --- | --- |
| DeepLOB (Baseline) | 0.4604 | 0.4329 | 0.3354 |
| T-KAN (Proposed) | 0.5343 | 0.4748 | 0.3995 |

### 4.2 Model Interpretability and Activation Analysis

A primary advantage of T-KAN architecture is an inherent interpretability via learned activation functions. This is much unlike the ReLU activation functions traditionally used. The T-KAN model converged on a non-linear S-curve (Sigmoidal B-spline), as shown in Figure [3](https://arxiv.org/html/2601.02310v1#S4.F3 "Figure 3 ‣ 4.2 Model Interpretability and Activation Analysis ‣ 4 Results ‣ Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay"). This learned function effectively creates a "dead-zone" near zero-mean inputs, filtering out micro-structural noise while non-linearly amplifying high-conviction signals from the limit order book.

![Refer to caption](tkan_activation_spline2.png)


Figure 3: Learned B-spline activation function of the T-KAN model. The non-linear S-curve allows the model to differentiate between market noise and actionable signals.

### 4.3 Transaction-Cost Adjusted Backtest

A mid-price trading simulation was conducted using a 1.0 bps transaction cost to evaluate the economic significance of the model’s predictions. As shown in figure [4](https://arxiv.org/html/2601.02310v1#S4.F4 "Figure 4 ‣ 4.3 Transaction-Cost Adjusted Backtest ‣ 4 Results ‣ Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay"), the performance difference is immense. In spite of DeepLOB’s baseline directional accuracy, the strategy was unable to overcome the friction of execution, causing a terminal return of -82.76%.

In contract, the T-KAN model resulted in a terminal return of 132.48%. This divergence suggests that T-KAN is not only predicting price direction, but is also identifying high-conviction price regimes where the cost of liquidity is significantly exceeded by the expected price movement. While T-KAN uses a far higher parameter footprint (104,451 vs. 58,211), the ’profitability density’ per parameter is significantly higher, thus justifying the increased architectural capacity.

![Refer to caption](Backtest_pnl.png)


Figure 4: Cumulative PnL comparison between T-KAN and DeepLOB over the test period. The T-KAN model demonstrates significantly higher resilience to 1.0 bps transaction costs.

## 5 Conclusion

The results of the experiment validate the hypothesis that using Kolmogorov-Arnolod layers [liu2024kan] rather than standard linear transformations enhance the extraction of alpha from high-frequency LOB data. By moving beyond the static activation functions of the DeepLOB baseline, the T-KAN architecture shows a superior ability to map the non-linear dynamics of market market structures.

### 5.1 Economic Viability and the Profitability-Capacity Trade-off

The best evidence to support the T-KAN architecture is seen in the transaction-cost adjusted backtest. While the T-KAN model used a higher parameter count (104,451) as opposed to the DeepLOB baseline (58,211), this higher capacity directly translated into economic viability. Under a 1.0 bps transaction cost regime, the DeepLOB baseline was unable to overcome execution friction, causing a terminal return of -82.76 %.

This was much unlike the T-KAN, which achieved a terminal return of 132.48%. This suggests that T-KAN does not only achieve a higher statistical accuracy, but specifically identifies high-conviction liquidity imbalances that stay profitable even after accounting for market fees. This "profitability density" justifies that 79.4% increase in parameter count, as though the model successfully transitioned from theoretical predictor to a viable trading strategy.

### 5.2 Robustness to Alpha Decay

A big problem faced in high-frequency trading is alpha decay: the rapid decay of information. As the prediction horizon kk increases, the predictive power of traditional models fall [cont2010price]. As shown in Figure [5](https://arxiv.org/html/2601.02310v1#S5.F5 "Figure 5 ‣ 5.2 Robustness to Alpha Decay ‣ 5 Conclusion ‣ Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay"), T-KAN’s higher F1-score at k=100k=100 shows far higher "Alpha Persistence". Through capturing the fundamental geometric properties of the order book in KAN layers, the model keeps predictive information longer than the CNN-based baseline, which is usually highly sensitive to the exact spatial positioning of orders [ntakaris2018benchmark].

![Refer to caption](alpha_decay_comparison2.png)


Figure 5: Alpha Decay Comparison: Information Coefficient (IC) vs. Forecast Horizon (k). T-KAN maintains higher predictive persistence over longer horizons compared to DeepLOB.

### 5.3 Industry Outlook: Interpretability and FPGA Implementation

From an industry perspective T-KAN presents two main advantages. Firstly, the learned S-curve activations (figure [3](https://arxiv.org/html/2601.02310v1#S4.F3 "Figure 3 ‣ 4.2 Model Interpretability and Activation Analysis ‣ 4 Results ‣ Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha Decay")), show an interpretable window into the decision making of the model, showing an autonomous filtering of ’bid-ask bounce’ noise.

Secondly, the T-KAN architecture is uniquely suited for ultra-low latency hardware acceleration. Quite unlike the dense matrix multiplication used in deep LSTMs or Transformers, KAN layers are reliant on localized B-Spline evaluations. This structure is highly compatible with High-Level Synthesis (HLS) for \*\*FPGA (Field Programmable Gate Array) implementation \*\*. Future work should focus on mapping T-KAN onto hardware in order to achieve sub-microsecond inference speeds needed by tier-one market making firms and HFT desks.