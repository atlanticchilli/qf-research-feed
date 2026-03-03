---
authors:
- Adir Saly-Kaufmann
- Kieran Wood
- Jan Peter-Calliess
- Stefan Zohren
doc_id: arxiv:2603.01820v1
family_id: arxiv:2603.01820
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted
  Performance1footnote 11footnote 1Code is available upon request.'
url_abs: http://arxiv.org/abs/2603.01820v1
url_html: https://arxiv.org/html/2603.01820v1
venue: arXiv q-fin
version: 1
year: 2026
---


Adir Saly-Kaufmann1,
Kieran Wood1,2,
Jan Peter-Calliess1,
Stefan Zohren1
  
  
1Machine Learning Research Group, Department of Engineering Science, University of Oxford
  
2Oxford-Man Institute of Quantitative Finance, University of Oxford
  
  
adir.saly-kaufmann@eng.ox.ac.uk, kieran.wood@eng.ox.ac.uk
  
janpeter.calliess@eng.ox.ac.uk, stefan.zohren@eng.ox.ac.uk

###### Abstract

We present a large-scale benchmark of modern deep learning architectures for a financial time-series prediction and position sizing task, with a primary focus on Sharpe-ratio optimization. Evaluating linear models, recurrent networks, transformer-based architectures, state-space models, and recent sequence-representation approaches, we assess out-of-sample performance on a daily futures dataset spanning commodities, equity indices, bonds, and FX spanning 2010–2025.
Our evaluation goes beyond average returns and includes statistical significance, downside and tail-risk measures, breakeven transaction-cost analysis, robustness to random seed selection, and computational efficiency. We find that models explicitly designed to learn rich temporal representations consistently outperform linear benchmarks and generic deep learning models, which often lead the ranking in standard time-series benchmarks. Hybrid models such as
*VSN + LSTM*, a combination of Variable Selection Networks (VSN) and LSTMs, achieves the highest overall Sharpe ratio, while *VSN+xLSTM* and *LSTM+PatchTST* exhibit superior downside-adjusted characteristics. *xLSTM* demonstrates the largest breakeven transaction cost buffer, indicating improved robustness to trading frictions.

## 1 Introduction

![Refer to caption](2603.01820v1/Images/FlowChart.png)


Figure 1: End-to-end portfolio optimization pipeline: Statistical and technical indicators are extracted from historical close prices, serving as the predictive model’s inputs. The model outputs are transformed into portfolio weights via a linear projection followed by a hyperbolic tangent activation. Training is performed by minimizing the negative Sharpe Ratio.

In recent years, many new deep learning architectures have emerged in the context of time-series forecasting, with
Transformer-based architectures [[1](#bib.bib1)] drawing particular attention [[2](#bib.bib2)].
Several theoretical extensions and adaptations have been proposed, such as iTransformer [[3](#bib.bib3)], PatchTST [[4](#bib.bib4)], and the Temporal Fusion Transformer [[5](#bib.bib5)].
Each of these models aims to address different challenges encountered in real-world forecasting.
For example, PatchTST improves robustness by bundling data points and interpreting features independently, whereas iTransformer focuses on learning relationships between features without relying on temporal order.

State Space Models have also presented an alternative to transformer-based architectures.
In particular, Mamba2 [[6](#bib.bib6)] claims to achieve a mathematically principled architecture with linear-attention-like behavior [[7](#bib.bib7)] while supporting arbitrarily large lookback windows.
More broadly, State Space Models have evolved from the theory of HiPPO (High-order Polynomial Projection Operators) matrices [[8](#bib.bib8)], which maintain compressed representations of past information as the model evolves.

Historically, recurrent neural networks (RNNs) [[9](#bib.bib9)] have been the most widely used deep-learning architectures for time-series forecasting [[10](#bib.bib10)], especially LSTMs [[11](#bib.bib11)].
More recently, the xLSTM architecture [[12](#bib.bib12)] has been introduced as a new state-of-the-art model, with additional gains demonstrated by PsLSTM [[13](#bib.bib13)].
xLSTM replaces LSTM’s traditional sigmoid gating with exponential gating and a normalization term, while also employing a memory matrix rather than a scalar value.
PsLSTM further integrates patching (similar to PatchTST) into the xLSTM architecture.

Several benchmark studies have explored deep-learning models for time-series forecasting [[14](#bib.bib14)], focusing on applications such as weather prediction, electricity transformer temperatures, and transportation data.
These studies indicate that simple architectures such as DLinear [[15](#bib.bib15)] can perform comparably to more complex transformer-based models.
Similarly, [[15](#bib.bib15)] has shown that NLinear performs slightly better in some settings.
However, these datasets exhibit strong seasonality and a high signal-to-noise ratio, in contrast to financial time series [[16](#bib.bib16)].

Forecasting financial time series essentially reduces to performing auto-regressive modeling [[17](#bib.bib17)], typically formulated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt+1=f​(xt,xt−1,xt−2,…)x\_{t+1}=f(x\_{t},x\_{t-1},x\_{t-2},...) |  | (1) |

for each 0≤t<T0\leq t<T, where xtx\_{t} is the value of the process at time tt, TT is the last time-step to predict, and f​(⋅)f(\cdot) denotes a model-dependent forecasting function that maps past observations to a one-step-ahead prediction. For example, in A​R​(p)AR(p) it is of the form:

|  |  |  |
| --- | --- | --- |
|  | f​(xt,…,xt−p)=∑i=0pϕi​xt−i,f(x\_{t},\dots,x\_{t-p})=\sum\_{i=0}^{p}\phi\_{i}x\_{t-i}, |  |

where {ϕi}\{\phi\_{i}\} are fixed coefficients [[17](#bib.bib17)] and in L​S​T​MLSTM [[11](#bib.bib11)], ff is instead represented by a nonlinear recurrent mapping with learnable gating mechanisms and hidden states [B.4](#A2.SS4 "B.4 LSTM-based models ‣ Appendix B Architecture Components ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.").

Financial return series are characterized by strong noise, weak and time-varying predictability, and pronounced non-stationarity. These properties imply that predictive success hinges less on raw model capacity than on the ability to recover economically meaningful signals from highly volatile data. In this context, a successful model must simultaneously (i) improve the signal-to-noise ratio by filtering out transient fluctuations, (ii) learn asset-specific dynamics rather than imposing homogeneous temporal structures, and (iii) embed temporal dependencies in a manner that remains stable across market regimes [[18](#bib.bib18), [19](#bib.bib19)]. Several of the benchmarked architectures incorporate explicit design choices aimed at enhancing one or more of these properties, including feature selection, structured state representations, and temporal aggregation mechanisms [[20](#bib.bib20)]. We evaluate both the incremental value of such architectural enhancements and their performance relative to models that natively embed these characteristics, with particular emphasis on robustness across time and economic regimes.

#### Contributions.

This paper presented a unified benchmark of modern deep learning architectures for financial time-series prediction under a Sharpe-ratio optimization framework. Using 15 years of data spanning multiple asset classes and market regimes, we evaluated linear models, recurrent networks, transformer-based architectures, state-space models, and recent sequence-representation approaches across return, risk, robustness, and computational dimensions.

Linear dynamics alone appear insufficient.
While linear models occasionally performed competitively in specific high-volatility subperiods, they failed to deliver stable performance across time and provided limited incremental value relative to a passive benchmark. This supports the view that financial returns exhibit structural features not fully captured by linear autoregression.

Architectural inductive bias is decisive.
Nonlinear models improved average performance, but outcomes varied substantially across architectures. Generic transformers and state-space models displayed heterogeneous, regime-sensitive behavior. In contrast, VLSTM—designed to learn structured temporal representations—delivered consistently strong and stable risk-adjusted returns, suggesting that representation compression, adaptive memory, and temporal abstraction are particularly valuable in low signal-to-noise environments.

Robustness and risk control matter as much as returns.
Downside exposure, tail behavior, and stability under reduced seed aggregation materially affected model suitability. VLSTM-based strategies combined competitive returns with moderate drawdowns and remained stable under weaker experimental budgets, indicating that performance was not driven solely by favorable seed selection.

Asymptotic efficiency does not guarantee empirical superiority.
Although state-space models offer attractive theoretical complexity, empirical effectiveness depended more strongly on inductive bias than on asymptotic scaling alone.

Overall, the results suggest that effective financial forecasting models benefit from jointly denoising returns, learning asset-specific and regime-aware dynamics, and encoding temporal structure in a stable and adaptive manner. While the conclusions remain conditional on the dataset and backtesting protocol employed, this benchmark provides a transparent reference point for future research in deep learning for finance.

## 2 Architectures

### 2.1 Problem Setup

Let {xt}t=1T\{x\_{t}\}\_{t=1}^{T}, xt∈ℝdx\_{t}\in\mathbb{R}^{d}, denote a multivariate time series of end of day features derived from commodity futures, foreign-exchange (FX) futures, bonds, index, and energy products, including prices, returns, and technical indicators.

Given a fixed lookback window of length LL, the objective is to learn a function

|  |  |  |  |
| --- | --- | --- | --- |
|  | fθ:ℝL×d→[−1,1],f\_{\theta}:\mathbb{R}^{L\times d}\rightarrow[-1,1], |  | (2) |

mapping historical observations

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐗t=[xt−L+1,…,xt]\mathbf{X}\_{t}=[x\_{t-L+1},\dots,x\_{t}] |  | (3) |

to a scalar forecast or trading signal used to construct daily positions,where 1 is the upper bound for a full long position and -1 is the lower bound for a full short position.

#### Trading Signal Generation

To systematically benchmark different deep learning paradigms, we structure the function fθf\_{\theta} as a modular, two-stage pipeline. The first stage consists of a candidate sequence architecture gϕg\_{\phi} (e.g., LSTM, PatchTST, or Mamba2), which processes the input window to extract a temporal state representation of fixed hidden dimension HH:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=gϕ​(𝐗t),ht∈ℝH.h\_{t}=g\_{\phi}(\mathbf{X}\_{t}),\quad h\_{t}\in\mathbb{R}^{H}. |  | (4) |

The second stage is a unified projection head applied to the terminal hidden state hth\_{t}. This consists of a linear transformation followed by a hyperbolic tangent (tanh\tanh) activation function to bound the output:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y^t=tanh⁡(wlin⊤​ht+blin),\hat{y}\_{t}=\tanh(w\_{\mathrm{lin}}^{\top}h\_{t}+b\_{\mathrm{lin}}), |  | (5) |

where wlin∈ℝHw\_{\mathrm{lin}}\in\mathbb{R}^{H} and blin∈ℝb\_{\mathrm{lin}}\in\mathbb{R} are learnable weights.
All models are trained using rolling windows and evaluated in a fully out-of-sample trading framework. We added ticker embeddings to all the models to enhance the learning per individual ticker/asset [[21](#bib.bib21)].

#### Portfolio Construction

The scalar output y^t,k∈[−1,1]\hat{y}\_{t,k}\in[-1,1] generated by the projection head represents the model’s directional conviction for asset kk at time tt. Because financial assets exhibit vastly different baseline volatilities, we employ a volatility targeting framework to equalize risk contributions across the universe [[22](#bib.bib22), [23](#bib.bib23), [24](#bib.bib24)]. We estimate the ex-ante conditional volatility σt,k\sigma\_{t,k} for each asset using an Exponentially Weighted Moving Average (EWMA) estimator (detailed in Appendix [A](#A1 "Appendix A Data Construction and Exploratory Analysis ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.")). This estimation induces a time-varying leverage factor, defined as vs\_factort,k=1σt,k\text{vs\\_factor}\_{t,k}=\frac{1}{\sigma\_{t,k}}, which dynamically scales position sizes in response to shifting market regimes.
Given a constant target portfolio volatility σtgt\sigma\_{\text{tgt}} (set to 10% in our empirical evaluation), the realized portfolio weight wt,kw\_{t,k} allocated to asset kk is obtained by scaling the neural network’s signal by this leverage factor:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt,k=y^t,k​(σtgtσt,k)=y^t,k⋅σtgt⋅vs\_factort,kw\_{t,k}=\hat{y}\_{t,k}\left(\frac{\sigma\_{\text{tgt}}}{\sigma\_{t,k}}\right)=\hat{y}\_{t,k}\cdot\sigma\_{\text{tgt}}\cdot\text{vs\\_factor}\_{t,k} |  | (6) |

Given these target weights, the daily gross strategy return for a specific asset kk realized at time t+1t+1 is the product of the position taken at the end of day tt and the subsequent asset return rt+1,kr\_{t+1,k}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt+1,k=wt,k⋅rt+1,kR\_{t+1,k}=w\_{t,k}\cdot r\_{t+1,k} |  | (7) |

Assuming an equal risk capital allocation across the KK active assets, the aggregate daily gross portfolio return Rt+1portR\_{t+1}^{\text{port}} is the cross-sectional average of the individual strategy returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt+1port=1K​∑k=1KRt+1,kR\_{t+1}^{\text{port}}=\frac{1}{K}\sum\_{k=1}^{K}R\_{t+1,k} |  | (8) |

#### End-to-end Optimization

Unlike traditional forecasting models that minimize predictive errors, our framework directly optimizes for risk-adjusted economic performance [[24](#bib.bib24)]. To train the parameters θ\theta of the network fθf\_{\theta}, we compute the Sharpe Ratio over a given training sequence of length TT. Let 𝐑port={R1port,…,RTport}\mathbf{R}^{\text{port}}=\{R\_{1}^{\text{port}},\dots,R\_{T}^{\text{port}}\} represent the sequence of daily portfolio returns. We define the sample estimators for the expected return 𝔼^​[R]\hat{\mathbb{E}}[R] and variance Var^​[R]\hat{\text{Var}}[R] of the portfolio as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | 𝔼^​[R]\displaystyle\hat{\mathbb{E}}[R] | =1T​∑t=1TRtport,\displaystyle=\frac{1}{T}\sum\_{t=1}^{T}R\_{t}^{\text{port}}, |  | (9a) |
|  | Var^​[R]\displaystyle\hat{\mathrm{Var}}[R] | =1T​∑t=1T(Rtport−𝔼^​[R])2.\displaystyle=\frac{1}{T}\sum\_{t=1}^{T}\left(R\_{t}^{\text{port}}-\hat{\mathbb{E}}[R]\right)^{2}. |  | (9b) |

The loss function ℒ​(θ)\mathcal{L}(\theta) is defined as the negative differentiable annualized Sharpe Ratio:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(θ)=−SR^​[R]=−𝔼^​[R]Var^​[R]+ϵ​252.\mathcal{L}(\theta)=-\,\widehat{\mathrm{SR}}[R]=-\,\frac{\hat{\mathbb{E}}[R]}{\sqrt{\hat{\mathrm{Var}}[R]+\epsilon}}\sqrt{252}. |  | (10) |

where 252252 represents the approximate number of trading days in a year, and ϵ\epsilon is a small constant added for numerical stability. By minimizing this loss, the network explicitly learns representations that maximize expected returns while heavily penalizing variance. Following the regime-robust DeePM framework [[25](#bib.bib25)], we compute the Sharpe ratio objective on *pooled* portfolio returns concatenating all sequences in the batch, following their argument that this is the best proxy for optimising out-of-sample Sharpe ratio. See the end-to-end optimization pipeline in Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.").

#### Net Returns and Breakeven Transaction Costs

To account for implementation frictions, the net portfolio return Rt+1netR\_{t+1}^{\text{net}} is defined by deducting the costs associated with portfolio turnover:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt+1net=Rt+1port−1K​∑k=1Kck​|wt,k−wt−1,k|R\_{t+1}^{\text{net}}=R\_{t+1}^{\text{port}}-\frac{1}{K}\sum\_{k=1}^{K}c\_{k}|w\_{t,k}-w\_{t-1,k}| |  | (11) |

where ckc\_{k} represents the proportional transaction cost per unit of traded weight for asset kk. Because realistic execution costs vary drastically across the asset universe (e.g., highly liquid short-term interest rates versus illiquid agricultural commodities), imposing static ex-ante assumptions for ckc\_{k} can severely distort cross-sectional performance metrics. Therefore, for model optimization and primary evaluation, we set ck=0c\_{k}=0 for all kk to assess the pure predictive efficacy of the architectures (gross returns). To evaluate resilience to trading frictions without relying on arbitrary assumptions, we conduct a post-hoc, asset-level breakeven transaction cost analysis. For each asset, we compute the breakeven cost ck∗c\_{k}^{\*}, which represents the maximum constant friction that specific asset’s strategy can endure before its cumulative PnL is driven to zero. The formal mathematical definition of ck∗c\_{k}^{\*} and the comprehensive per-asset breakeven results are detailed in Appendix [E](#A5 "Appendix E Asset-level Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request."). As detailed by [[25](#bib.bib25)], we ensemble the positions of the top SS seeds based on validation loss to reduce turnover and improve robustness to transactions costs.

### 2.2 Linear Baselines

We include a set of linear models as classical and modern baselines to contextualize the performance of deep architectures. The mathematical background can be found in [B.1](#A2.SS1 "B.1 Linear Baselines ‣ Appendix B Architecture Components ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.")

#### Autoregressive Model (AR1x).

The AR1x model [[17](#bib.bib17)] serves as a minimal temporal benchmark, capturing short-term autocorrelation in returns. This model applies AR(1) per feature, since the input has multiple features. Its performance provides a lower bound on the benefit of incorporating temporal context and highlights whether short-horizon dependence alone is sufficient for profitable trading.

#### DLinear and NLinear.

DLinear and NLinear [[15](#bib.bib15)] are non-recurrent linear models that apply learned linear mappings to fixed-length input windows. DLinear explicitly decomposes the input into trend and seasonal components, while NLinear operates on normalized inputs. These models have shown strong performance on data with pronounced linear structure or seasonality.

### 2.3 Transformer-Based Architectures Without Explicit Recurrence

Within the Transformer [B.2](#A2.SS2 "B.2 Transformer Background ‣ Appendix B Architecture Components ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") temporal context, i.e., context window, the model learns relative temporal importance.
However, it does not explicitly encode a temporal state representation and is therefore susceptible to overfitting to outliers.

Transformer-based models are known to perform well in many tasks, but often struggle with financial time-series forecasting [[26](#bib.bib26), [27](#bib.bib27)]. In the implementation of the following models, we use parallel offset streams so we obtain dense per-timestep outputs, similar to the output of the other models.

#### iTransformer.

The inverted Transformer [[3](#bib.bib3)] applies attention across feature dimensions rather than time, treating each feature as a token. While this design improves parameter efficiency, it removes explicit temporal recurrence and relies solely on attention to capture dynamics.

#### PatchTST.

PatchTST [[4](#bib.bib4)] segments the input sequence into temporal patches, which are embedded and processed via self-attention. Representing the data in patches inherently smooths the financial time-series and has shown to improve the performance in long-term forecasting [[28](#bib.bib28)]. The receptive field is increased to fully exploit the temporal context captured by the patch-based architecture.

### 2.4 State-Space and Implicitly Recurrent Models

#### Mamba and Mamba2.

Mamba models [[29](#bib.bib29), [6](#bib.bib6)] belong to the class of selective state-space models (SSMs) [B.3](#A2.SS3 "B.3 State-Space Model Details ‣ Appendix B Architecture Components ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request."), which maintain a latent state that is updated recursively over time. Unlike attention-based architectures, SSMs provide an implicit temporal recurrence with linear-time complexity, making them well-suited for long sequences and noisy environments such as financial time series.

At a high level, these models update a hidden state, often based on High-order Polynomial Projection Operators (HiPPO) [[8](#bib.bib8)], which summarizes past information and produces outputs conditioned on the current state. The parameters governing the state evolution are dynamically modulated by neural networks conditioned on the input, enabling adaptive temporal dynamics while preserving computational efficiency.

Mamba2 refines this formulation by simplifying the state transition structure and increasing head dimensionality, leading to improved numerical stability and throughput. In our implementation, we use a static HiPPO-based state transition matrix with a fixed horizon, rather than per-step adaptive horizon jitter. This design choice improves noise tolerance [[30](#bib.bib30)] and stabilizes learning in the presence of heavy-tailed returns and regime shifts, which are common in financial markets.

### 2.5 Recurrent Models

#### LSTM.

Long Short-Term Memory (LSTM) [B.4](#A2.SS4 "B.4 LSTM-based models ‣ Appendix B Architecture Components ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") networks maintain an explicit recurrent state, consisting of a hidden state and a memory cell, that is updated sequentially over time, enabling the model to capture temporal dependencies, but with an exponentially decaying long-horizon temporal state [[11](#bib.bib11)]. This architecture has proven to be useful in many cases in finance [[18](#bib.bib18)].

#### xLSTM.

xLSTM [[12](#bib.bib12)] extends the classical LSTM by introducing exponential gating and stabilized memory normalization to improve long-range information retention and gradient flow [B.4](#A2.SS4 "B.4 LSTM-based models ‣ Appendix B Architecture Components ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request."). While standard LSTMs rely on sigmoid gates that may saturate and induce premature forgetting, xLSTM replaces these with exponentiated gate activations followed by normalization, yielding approximately linear behavior over a wider dynamic range. This modification mitigates vanishing memory effects and allows the model to retain rare but economically meaningful signals.

xLSTM comprises two variants: scalar LSTM (sLSTM), which maintains a scalar memory state updated via normalized exponential gates, and matrix LSTM (mLSTM), which generalizes the memory state to a matrix-valued representation, enabling higher memory capacity and associative recall through key–value storage mechanisms. This design increases representational richness and improves scalability compared to classical recurrent architectures.

From a financial perspective, the ability to preserve temporally distant but informative signals and adaptively revise memory states is particularly relevant in low signal-to-noise and regime-dependent environments [[31](#bib.bib31)].

#### Patch sLSTM (PsLSTM).

Patch sLSTM [[13](#bib.bib13)] integrates the patching strategy of PatchTST with the recurrent inductive bias of sLSTM. Given a multivariate time series of length LL with dd channels, each channel is treated as an independent univariate sequence and segmented into non-overlapping temporal patches:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x~p(i)=Patch​(xt:t+ℓ−1(i)),(i=1,…,d)\tilde{x}\_{p}^{(i)}=\text{Patch}\left(x\_{t:t+\ell-1}^{(i)}\right),\quad(i=1,\dots,d) |  | (12) |

where ℓ\ell denotes the patch length.

Each patch embedding x~p(i)\tilde{x}\_{p}^{(i)} is then processed by an sLSTM, with *shared parameters across channels*:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hp(i)=sLSTM​(hp−1(i),x~p(i)).h\_{p}^{(i)}=\text{sLSTM}(h\_{p-1}^{(i)},\tilde{x}\_{p}^{(i)}). |  | (13) |

This design preserves channel independence while enforcing parameter sharing, preventing premature feature mixing and improving generalization.

By operating at the patch level, PsLSTM reduces sensitivity to high-frequency noise and allows the recurrent mechanism to focus on medium-term temporal structure. The exponential gating of sLSTM further enhances memory persistence across patches, enabling the model to capture regime-level dynamics and rare events. After recurrent processing, hidden states across channels are flattened and projected to form the final prediction.

Patch sLSTM thus combines the noise robustness and efficiency of patch-based modeling with the long-range memory advantages of exponential-gated recurrence, which may be advantageous in financial time series characterized by non-stationary and bad signal-to-noise ratio.

### 2.6 Hybrids

Several hybrid architectures are considered to improve robustness in financial time series by enhancing the signal-to-noise ratio and stabilizing temporal state updates [B.5](#A2.SS5 "B.5 Hybrid Architecture Details ‣ Appendix B Architecture Components ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.").

Variable Selection Networks (VSNs) [B.5](#A2.SS5.SSS0.Px1 "Variable Selection Network (VSN) ‣ B.5 Hybrid Architecture Details ‣ Appendix B Architecture Components ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request."), inspired by the Temporal Fusion Transformer, are used to perform feature-wise nonlinear embedding and dynamic soft selection of relevant covariates at each time step. This mechanism adaptively suppresses noisy or uninformative features.

Another strategy to improve robustness is the inclusion of an LSTM-based temporal encoder prior to the main model. By explicitly maintaining a recurrent state, this preprocessing stage filters high-frequency noise and stabilizes downstream representations.

#### VSN+LSTM (VLSTM).

VLSTM combines a VSN with an LSTM encoder to construct a compact temporal state representation. This was the core component of the X-Trend architecture used for constructing sequence representations for few-shot learning in financial time series [[32](#bib.bib32)].
The VSN produces dynamically weighted feature embeddings, which are then processed sequentially by an LSTM to aggregate long-range temporal information.

#### VSN–Mamba2.

This hybrid augments Mamba2 with a VSN to separate feature selection from temporal modeling. The VSN filters noisy covariates before passing the selected representation to the recurrent state-space model, improving robustness in noisy financial environments.

#### LSTM + PatchTST (LPatchTST).

This architecture combines explicit recurrence with attention by using an LSTM as a channel-wise temporal denoiser prior to PatchTST. The LSTM stabilizes per-channel representations, while PatchTST aggregates medium- and long-range dependencies across denoised temporal patches.

#### VSN + xLSTM (VxLSTM).

In this hybrid, VSN-selected representations are directly fed into an xLSTM. The matrix-valued memory of xLSTM enables the model to capture higher-order temporal interactions and long-range dependencies beyond the capacity of vector-based recurrent architectures.

### 2.7 Complete Structured Model

#### Temporal Fusion Transformer (TFT).

TFT [[5](#bib.bib5)] integrates gated recurrent layers with interpretable attention mechanisms. A recurrent encoder captures local temporal dynamics, where LSTM is used as the recurrent encoder, while multi-head attention aggregates information across time:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y^t=Attn​(LSTM​(x1:t)).\hat{y}\_{t}=\text{Attn}(\text{LSTM}(x\_{1:t})). |  | (14) |

Variable selection networks, static covariate encoders, and gating mechanisms further improve robustness, making TFT a strong benchmark for time-series forecasting and specifically financial forecasting [[33](#bib.bib33)].

## 3 Empirical Results

This section presents a comprehensive evaluation of the out-of-sample performance of the considered models across multiple market regimes, performance metrics, and computational dimensions, Appendix [D.1](#A4.SS1 "D.1 Return and Risk-Adjusted Performance ‣ Appendix D Performance Metrics and Evaluation Criteria ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request."). We focus on (i) risk-adjusted returns across subperiods, (ii) aggregate return performance and statistical significance, (iii) downside and tail-risk characteristics, (iv) robustness to seed selection and experimental budget, and (v) the trade-off between predictive performance and computational complexity.

### 3.1 Data Description

Our empirical analysis was conducted on a diversified cross-asset futures and currency dataset [[34](#bib.bib34)]. The futures data comprises of instruments from five asset classes: bonds, commodities, energy, foreign exchange, and equity indices. Daily closing prices were used to construct returns and predictive features. For futures, we use continuous contracts formed by linking adjacent maturities using a ratio-adjusted backwards methodology (i.e., back-adjusted to remove roll-induced price jumps).
A detailed description of data construction and exploratory analysis is provided in Appendix [A](#A1 "Appendix A Data Construction and Exploratory Analysis ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.").

The dataset [[34](#bib.bib34)] exhibits several well-documented stylized facts of financial time series, including heavy-tailed return distributions, volatility clustering, and strong deviations from Gaussianity. These properties are illustrated formally in Appendix [A](#A1 "Appendix A Data Construction and Exploratory Analysis ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request."), where we reported distributional diagnostics (e.g., QQ-plots) and volatility dynamics. As such, the dataset provides a realistic and challenging benchmark for evaluating nonlinear forecasting architectures in a cross-asset setting.

Although the empirical evidence is robust within our cross-asset benchmark, the results should be interpreted as conditional on the specific dataset and period considered. Extending the analysis to alternative markets and sampling frequencies would further clarify the external validity of the findings.

### 3.2 Performance Across Market Regimes

Table 1: Out-of-sample Sharpe Ratio by subperiod. Annual Sharpe Ratio in Table [11](#A6.T11 "Table 11 ‣ Appendix F Annual Sharpe Ratio ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.")

| Strategy | 2010-2025 | 2015-2025 | 2010-2015 | 2015-2020 | 2020-2025 |
| --- | --- | --- | --- | --- | --- |
| AR1x | 0.77 | 0.70 | 0.74 | 0.06 | 1.35 |
| ARnnx | 0.63 | 0.55 | 0.70 | -0.01 | 1.11 |
| DLinear | 0.64 | 0.64 | 0.60 | 0.00 | 1.28 |
| LSTM | 1.48 | 1.33 | 1.83 | 1.60 | 1.07 |
| VLSTM | 2.40 | 2.25 | 2.57 | 2.61 | 1.88 |
| Mamba2 | 0.78 | 0.86 | 0.54 | 0.18 | 1.54 |
| VSN+Mamba2 | 1.10 | 1.14 | 0.95 | 0.54 | 1.74 |
| PatchTST | 0.76 | 0.80 | 0.59 | 0.57 | 1.03 |
| LPatchTST | 2.31 | 2.22 | 2.33 | 2.11 | 2.34 |
| PsLSTM | 1.74 | 1.74 | 1.60 | 1.84 | 1.68 |
| TFT | 2.27 | 2.08 | 2.47 | 2.08 | 2.08 |
| VxLSTM | 1.69 | 1.61 | 1.56 | 1.48 | 1.74 |
| xLSTM | 1.79 | 1.84 | 1.46 | 1.68 | 1.99 |
| iTransformer | 0.38 | 0.28 | 0.60 | 0.06 | 0.50 |
| Mamba | 0.64 | 0.28 | 0.51 | -0.01 | 0.56 |
| NLinear | 0.66 | 0.68 | 0.60 | 0.14 | 1.23 |

Table [1](#S3.T1 "Table 1 ‣ 3.2 Performance Across Market Regimes ‣ 3 Empirical Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") reports out-of-sample Sharpe ratios aggregated over multiple overlapping horizons from 2010 to 2024, while Table [11](#A6.T11 "Table 11 ‣ Appendix F Annual Sharpe Ratio ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") presents annual Sharpe ratios. Taken together, these results enable an evaluation of year-to-year variability and medium-horizon robustness across distinct market regimes, including the post-GFC recovery, the low-volatility expansion of the mid-2010s, and the elevated-uncertainty environment following 2020.

Several systematic patterns emerge.

First, deep nonlinear sequence models substantially outperform linear benchmarks on most aggregated horizons. While linear specifications such as AR1x, ARnnx, DLinear, and NLinear occasionally achieve strong single-year Sharpe ratios—particularly during high-volatility years such as 2020—their performance is highly variable across time. Their long-horizon averages over 2010–2025 remain materially below those of the strongest nonlinear architectures. This instability is consistent with the limited representational flexibility of linear dynamics in environments characterized by non-stationarity, regime shifts, and low signal-to-noise ratios.

In contrast, gated recurrent and hybrid sequence models exhibit both higher average Sharpe ratios and greater intertemporal consistency. The LSTM already delivers strong performance (1.48 over 2010–2025), but its variance across years remains non-negligible. Enhanced recurrent architectures improve further. In particular, VLSTM achieves a 2010–2025 Sharpe ratio of 2.40 and maintains strong performance across subperiods, including 2.25 over 2015–2025 and 1.88 over 2020–2025. Similarly, LPatchTST achieves 2.31 over 2010–2025 and remains stable across all aggregated windows, including 2.34 in the post-2020 regime. The Temporal Fusion Transformer (TFT) also demonstrates robust performance, with 2.27 over 2010–2025 and consistent strength across medium-horizon splits.

These results suggest that architectures combining adaptive gating, representation compression, and structured temporal abstraction are better suited to financial data than either purely linear models or attention-only baselines. The year-by-year breakdown further reveals that top-performing models rarely collapse entirely in adverse years; rather, performance degrades moderately while remaining economically meaningful. This robustness is particularly visible during volatile periods such as 2020–2022.

State-space models such as Mamba and Mamba2 display more heterogeneous behavior. While certain years exhibit strong Sharpe ratios (notably 2020 and 2022 for Mamba2), their aggregated performance remains moderate (0.78 and 0.64 over 2010–2025 for Mamba2 and Mamba, respectively). Augmenting Mamba2 with a Variable Selection Network improves medium-horizon averages (1.10 over 2010–2025), indicating that explicit feature conditioning partially mitigates instability, though it does not close the gap to the strongest recurrent or hybrid models.

Transformer-based patching approaches show mixed results. PatchTST achieves moderate long-run averages (0.76 over 2010–2025), but exhibits higher sensitivity to specific years. In contrast, LPatchTST, which augments patching with stronger sequence modeling, delivers consistently superior and more stable results, suggesting that patch segmentation alone is insufficient without robust temporal state encoding.

Finally, xLSTM-based architectures demonstrate a compelling balance between performance and stability. The xLSTM achieves a Sharpe ratio of 1.79 over 2010–2025, improving to 1.99 in the 2020–2025 period. VxLSTM yields comparable results (1.69 over 2010–2025), while PsLSTM achieves 1.74. Importantly, these models maintain Sharpe ratios near or above 1.5 across most aggregated horizons, indicating resilience to changing volatility regimes. Their year-level profiles show fewer extreme drawdowns relative to classical LSTM, consistent with the hypothesis that enriched state representations and alternative gating mechanisms enhance adaptability in non-stationary environments.

Taken together, the annual and aggregated results reinforce the central hypothesis of the paper: successful financial forecasting architectures benefit from adaptive memory mechanisms, representation compression, and temporally stable state evolution. Models that incorporate structured gating and persistent state representations dominate both linear baselines and generic state-space formulations across nearly all evaluation horizons. As emphasized throughout, these conclusions remain conditional on the dataset and evaluation framework considered; nevertheless, the consistency across multiple temporal aggregations provides evidence that the observed performance differentials are not driven solely by isolated years or singular market events.

### 3.3 Aggregate Return Performance and Statistical Significance

Table [2](#S3.T2 "Table 2 ‣ 3.3 Aggregate Return Performance and Statistical Significance ‣ 3 Empirical Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") reports full-sample out-of-sample performance under a volatility-targeting constraint of 10%, presenting compound annual growth rates (CAGR) [[35](#bib.bib35)], annualized returns (Ann. Ret.), Sharpe Ratio (SR) [[36](#bib.bib36)], heteroskedasticity and autocorrelation consistent tt-statistics
(tt HAC) [[37](#bib.bib37)], hit rate (Hit) [[38](#bib.bib38)], turnover, turnover as a multiple of gross market value (xGMV) [[23](#bib.bib23)], and additional diagnostics relative to a passive long-only benchmark: the information ratio (Info. Ratio), HAC tt-statistic relative to passive (tt HAC v Passive), and correlation with passive returns (Corr. v Passive). Collectively, these measures capture economic magnitude, statistical reliability, trading intensity, and incremental value relative to buy-and-hold exposure (see Appendix [D](#A4 "Appendix D Performance Metrics and Evaluation Criteria ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.")), see Appendix [D](#A4 "Appendix D Performance Metrics and Evaluation Criteria ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.").

VLSTM delivers the strongest overall performance within this framework. It achieves a 23.9% annualized return with a Sharpe ratio of 2.39, exceeding both linear and alternative deep learning benchmarks. Its HAC-adjusted tt-statistic of 8.81 indicates high statistical reliability under heteroskedasticity- and autocorrelation-consistent inference. The hit rate of 58.8% suggests persistent directional accuracy. Relative to the passive benchmark, VLSTM attains an information ratio of 0.854 and an HAC tt-statistic of 3.31, indicating statistically distinguishable excess performance. Its correlation with passive returns (0.404) implies partial independence from broad market exposure and meaningful diversification potential.

The hybrid LPatchTST model achieves comparable economic performance, with a Sharpe ratio of 2.32 and a CAGR of 25.5%. Passive-relative metrics remain elevated (information ratio 0.707; tt HAC 2.75), though modestly below VLSTM. Similarly, the Temporal Fusion Transformer (TFT) delivers strong absolute and relative performance (Sharpe 2.20), reinforcing the importance of structured sequence representations and adaptive gating mechanisms. Across these leading architectures, elevated Sharpe ratios coincide with statistically significant passive-relative improvements, suggesting that gains are not merely attributable to implicit market timing or leverage effects under volatility targeting.

LSTM-based variants, including PsLSTM, VxLSTM, and xLSTM, substantially outperform linear baselines. Notably, xLSTM achieves a Sharpe ratio of 1.80 with a comparatively moderate turnover (482), resulting in one of the strongest passive-relative diagnostics (information ratio 0.798; tt HAC 2.90). This combination of competitive returns and reduced trading intensity suggests improved efficiency in signal extraction relative to classical LSTM, which requires nearly double the turnover to achieve similar Sharpe ratios. These findings are consistent with the view that enriched state representations can improve the signal-to-trade ratio in noisy financial environments.

Linear benchmarks (AR1x, ARnnx, DLinear) exhibit Sharpe ratios below one and comparatively small HAC tt-statistics. Passive-relative metrics are near zero or negative, and correlations with the buy-and-hold benchmark remain moderate. While these models occasionally benefit from favorable return persistence, their aggregate performance indicates limited capacity to extract stable predictive structure under non-stationarity.

State-space models display heterogeneous behavior. Mamba2 reduces trading intensity relative to most deep sequence models (turnover 233) but achieves only moderate economic performance (Sharpe 0.62). Augmenting with a Variable Selection Network improves both Sharpe ratio (0.97) and passive-relative metrics, indicating that explicit feature conditioning enhances stability. Nevertheless, their aggregate performance remains below that of recurrent and hybrid architectures.

The inclusion of iTransformer provides an informative contrast. It exhibits by far the lowest turnover (36) and xGMV (9.2), indicating a highly conservative trading profile with minimal portfolio rebalancing. However, this low implementation intensity coincides with weak economic performance (Sharpe 0.35) and statistically insignificant passive-relative diagnostics. This pattern suggests that extreme turnover reduction may reflect under-reactivity to evolving return signals in non-stationary markets. In the present setting, reduced trading alone does not generate economic value; rather, successful models appear to balance adaptive responsiveness with controlled trading intensity.

Figure [2](#S3.F2 "Figure 2 ‣ 3.3 Aggregate Return Performance and Statistical Significance ‣ 3 Empirical Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") visually corroborates these quantitative findings. Leading sequence-based models dominate cumulative PnL trajectories while maintaining relatively smooth performance paths, indicating that elevated Sharpe ratios reflect persistent incremental returns rather than isolated return episodes. As throughout, these findings remain conditional on the dataset and backtesting design considered.

Table 2: 2010–2025 Gross return performance, statistical significance, and passive-relative diagnostics (volatility-targeted at 10%).

| Model | CAGR | Ann. Ret. | SR | tt (HAC) | Hit | Turnover | xGMV | Info. Ratio | tt (HAC) v Passive | Corr. v Passive |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Passive | 0.0435 | 0.0476 | 0.48 | 1.65 | 0.531 | – | – | – | – | – |
| AR1x | 0.0813 | 0.0831 | 0.83 | 3.12 | 0.539 | 353.64 | 90.421 | -0.0086 | -0.0305 | 0.3533 |
| ARnnx | 0.0646 | 0.0677 | 0.68 | 2.52 | 0.538 | 280.66 | 69.525 | -0.0829 | -0.3011 | 0.4325 |
| DLinear | 0.0750 | 0.0773 | 0.77 | 2.87 | 0.539 | 278.41 | 75.282 | 0.0141 | 0.0501 | 0.2612 |
| LSTM | 0.1351 | 0.1318 | 1.32 | 4.56 | 0.554 | 948.08 | 225.769 | -0.0637 | -0.2303 | 0.2816 |
| VLSTM | 0.2632 | 0.2388 | 2.39 | 8.81 | 0.588 | 966.86 | 218.369 | 0.8539 | 3.3071 | 0.4042 |
| Mamba2 | 0.0587 | 0.0620 | 0.62 | 2.31 | 0.546 | 233.00 | 58.164 | -0.0901 | -0.3246 | 0.2220 |
| VSN+Mamba2 | 0.0967 | 0.0973 | 0.97 | 3.65 | 0.555 | 329.11 | 78.842 | 0.1091 | 0.3936 | 0.2821 |
| PatchTST | 0.0847 | 0.0864 | 0.86 | 3.29 | 0.541 | 623.88 | 198.021 | -0.2149 | -0.7848 | 0.5530 |
| LPatchTST | 0.2550 | 0.2323 | 2.32 | 8.81 | 0.577 | 959.89 | 211.514 | 0.7070 | 2.7470 | 0.3471 |
| PsLSTM | 0.1868 | 0.1763 | 1.76 | 6.83 | 0.563 | 823.07 | 185.496 | 0.3981 | 1.5410 | 0.4862 |
| TFT | 0.2398 | 0.2201 | 2.20 | 8.13 | 0.584 | 912.81 | 223.231 | 0.6665 | 2.5487 | 0.3888 |
| VxLSTM | 0.1937 | 0.1821 | 1.82 | 6.89 | 0.574 | 775.88 | 159.438 | 0.4666 | 1.6727 | 0.5069 |
| xLSTM | 0.1937 | 0.1796 | 1.80 | 6.85 | 0.568 | 482.62 | 91.924 | 0.7984 | 2.9042 | 0.6274 |
| iTransformer | 0.0308 | 0.0353 | 0.35 | 1.26 | 0.529 | 36.32 | 9.203 | -0.1539 | -0.5563 | 0.4855 |

![Refer to caption](2603.01820v1/Images/Gross_PnL.png)


Figure 2: Performance comparison across models 10% volatility-rescaled gross PnL.

### 3.4 Downside Risk and Tail Behavior

While strong average performance is economically relevant, robustness to adverse market conditions is particularly important in financial applications. Table [3](#S3.T3 "Table 3 ‣ 3.4 Downside Risk and Tail Behavior ‣ 3 Empirical Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") reported downside and tail-risk metrics, including maximum drawdown (Max DD), Calmar ratio (Calmar), worst three-month Sharpe ratio (Worst 3m Sharpe), minimum annual Sharpe ratio (Min Ann. Sharpe), and 5% conditional value at risk (CVaR 5%).

VLSTM and LPatchTST exhibited comparatively moderate drawdowns alongside relatively high Calmar ratios (1.15 and 1.47, respectively). VLSTM achieved a worst three-month Sharpe ratio of -3.68 and the lowest CVaR among the evaluated models. These results were consistent with comparatively milder tail losses within the sample period.

The smallest maximum drawdown was observed for VxLSTM (-11.8%), accompanied by the highest Calmar ratio (1.64). However, this configuration generated lower average returns relative to VLSTM in the aggregate performance analysis, suggesting a more conservative return profile within the evaluation framework.

In contrast, standard LSTM and PatchTST architectures experienced larger drawdowns and weaker worst-period performance. This pattern indicated greater sensitivity to extreme market movements during the sample period.

Overall, VLSTM combined comparatively strong average performance with moderate downside risk measures. However, LPatchTST and xLSTM were the most robust and were able to keep a favorable tail behavior. Within the dataset considered, this balance suggested a favorable trade-off between return generation and tail-risk exposure. As throughout, these findings should be interpreted as conditional on the sample period and backtesting design.

Table 3: Downside risk and tail behavior (gross returns).

| Model | Max DD | Calmar | Worst 3m Sharpe | Min Ann. Sharpe | CVaR 5% |
| --- | --- | --- | --- | --- | --- |
| AR1x | -0.167 | 0.49 | -3.92 | -0.59 | 0.0147 |
| ARnnx | -0.206 | 0.31 | -4.52 | -0.90 | 0.0148 |
| DLinear | -0.180 | 0.42 | -4.93 | -0.94 | 0.0149 |
| LSTM | -0.342 | 0.40 | -5.15 | -1.51 | 0.0143 |
| VLSTM | -0.229 | 1.15 | -3.68 | -0.10 | 0.0137 |
| Mamba2 | -0.263 | 0.22 | -4.06 | -0.71 | 0.0149 |
| VSN+Mamba2 | -0.163 | 0.59 | -4.00 | -0.63 | 0.0148 |
| PatchTST | -0.176 | 0.48 | -5.58 | -1.21 | 0.0151 |
| LPatchTST | -0.174 | 1.47 | -3.91 | 0.51 | 0.0136 |
| PsLSTM | -0.131 | 1.43 | -3.80 | -0.40 | 0.0143 |
| TFT | -0.232 | 1.03 | -3.87 | -0.14 | 0.0141 |
| VxLSTM | -0.118 | 1.64 | -3.70 | -1.31 | 0.0139 |
| xLSTM | -0.141 | 1.35 | -3.57 | -0.28 | 0.0141 |
| Passive | -0.308 | 0.14 | -6.11 | -1.53 | 0.0144 |
| iTransformer | -0.264 | 0.12 | -3.93 | -1.16 | 0.0154 |

### 3.5 Breakeven Transaction Cost

Breakeven transaction cost analysis, Appendix [E](#A5 "Appendix E Asset-level Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request."), reveals substantial cross-asset heterogeneity. The tables report annualised, volatility-rescaled gross and net returns together with annualised turnover and the implied breakeven transaction cost c∗c^{\*} in basis points.

For VLSTM, several agricultural contracts (e.g., Lumber, Oats elec, and Milk III) exhibit high gross returns but also relatively large breakeven costs (exceeding 20 bps). These contracts are comparatively illiquid therefore they are expected to have high transaction costs and scalability is limited despite their strong gross profitability.
A broad middle group demonstrates moderate profitability, with breakeven costs in the range of 5–10 bps.
At the lower end, high-turnover contracts (e.g., US 2Y Note Composite Bond and Euro Schatz Bond) display very small breakeven costs, indicating that profitability is quickly eroded by transaction costs. These are amongst the most liquid contracts; therefore, it is expected that they have tight spreads. However, they can also be traded in high volumes.
Finally, a small subset of contracts generates negative gross returns, resulting in negative c∗c^{\*}.

For xLSTM, the strongest contracts again include Lumber, Oats elec, Milk III, with even higher breakeven costs for some assets (e.g., Lumber at 33.9 bps), once again, noting that these are highly illiquid contracts. Notably, xLSTM achieves materially lower turnover for several equity and bond contracts (e.g., ES, ZN), leading to higher breakeven margins despite similar gross returns. However, the lower tail contains more negative gross performers relative to VLSTM.

Overall, xLSTM appears more transaction-cost efficient in several liquid contracts due to reduced turnover, while VLSTM delivers broader cross-sectional profitability.

### 3.6 Robustness to Seed Selection and Experimental Budget

Table [4](#S3.T4 "Table 4 ‣ 3.6 Robustness to Seed Selection and Experimental Budget ‣ 3 Empirical Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") evaluated the robustness of the main findings to a substantially reduced experimental budget. Whereas the primary results in Sections [3.3](#S3.SS3 "3.3 Aggregate Return Performance and Statistical Significance ‣ 3 Empirical Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") and [3.4](#S3.SS4 "3.4 Downside Risk and Tail Behavior ‣ 3 Empirical Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") were obtained by averaging performance over the top 10 seeds, based on validation loss, from 50 independent runs, this table reported results using only 25 random seeds and averaging over the top 5 realizations. This configuration represented a noisier and more resource-constrained evaluation regime, intended to assess whether model rankings and economic patterns persisted under weaker aggregation.

Across models, performance levels and relative ordering remained broadly stable. VLSTM again achieved the highest absolute and risk-adjusted returns, with a Sharpe ratio of 2.40 and an HAC-adjusted tt-statistic of 8.86, closely aligned with its full-budget estimates. The TFT and VxLSTM also maintained Sharpe ratios above 1.9 with statistically distinguishable HAC tt-statistics, while the linear AR1x benchmark continued to exhibit comparatively weak performance across return metrics. This stability in relative rankings was consistent with the interpretation that performance differences were not solely driven by extensive seed exploration or aggressive averaging.

Downside and tail-risk characteristics exhibited similar patterns. Maximum drawdowns, Calmar ratios, and worst three-month returns remained quantitatively comparable to those observed under the full-budget evaluation. VLSTM and VxLSTM maintained elevated Calmar ratios (1.66 and 1.88, respectively), indicating a similar balance between return generation and drawdown magnitude as in the primary specification. The 5% Conditional Value-at-Risk (CVaR) did not materially deteriorate under reduced seed averaging, suggesting that tail-risk characteristics were not highly sensitive to seed selection within the tested range.

Overall, the reduced-seed experiment suggested that both economic performance and downside risk measures were reasonably stable to substantial reductions in experimental budget. The persistence of model rankings and risk profiles under noisier evaluation conditions was consistent with the view that the observed performance differences reflected structural properties of the architectures within this benchmark, rather than purely favorable random initialization or extreme-seed selection. As throughout, these conclusions remain conditional on the specific dataset and backtesting protocol employed.

Table 4: Reduced-seed benchmark (25 runs, top 5 seeds selected).

| Return Performance | | | | | | Risk and Downside Metrics | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | CAGR | Ann. Ret. | Sharpe | tt (HAC) | Hit | Model | Max DD | Calmar | Worst 3m | Min Ann. | CVaR 5% |
| AR1 | 0.084 | 0.085 | 0.854 | 3.208 | 0.537 | AR1 | -0.165 | 0.506 | -4.068 | -0.524 | 0.0147 |
| VLSTM | 0.264 | 0.240 | 2.397 | 8.857 | 0.589 | VLSTM | -0.159 | 1.664 | -3.730 | -0.250 | 0.0139 |
| TFT | 0.251 | 0.229 | 2.290 | 8.575 | 0.586 | TFT | -0.210 | 1.196 | -3.499 | -0.175 | 0.0141 |
| VxLSTM | 0.203 | 0.190 | 1.898 | 7.236 | 0.578 | VxLSTM | -0.108 | 1.878 | -3.718 | -1.064 | 0.0138 |

### 3.7 Discussion

The empirical results presented across return, risk, tail, cost, and robustness diagnostics suggest several consistent patterns regarding the inductive biases required for successful financial time-series modeling. As emphasized throughout, these interpretations remain conditional on the dataset and evaluation framework considered, as discussed in Section [3.1](#S3.SS1 "3.1 Data Description ‣ 3 Empirical Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.").

The dataset exhibits non-stationarity, heavy tails, low signal-to-noise ratios, and pronounced deviations from Gaussianity – stylized facts widely documented in financial return series. To the extent that other financial time series share these characteristics, similar architectural considerations may apply.

First, architectures maintaining explicit recurrent state representations consistently outperformed purely attention-based models across most performance dimensions. This advantage extends beyond average Sharpe ratios to include downside protection and tail behavior. Models such as VLSTM, VxLSTM, and LPatchTST not only achieved strong full-sample Sharpe ratios, but also demonstrated superior Calmar ratios and materially higher minimum annual Sharpe ratios. In particular, LPatchTST exhibited an exceptionally stable worst-year profile, a property of practical relevance in institutional settings where drawdown control and avoidance of severely negative years are often prioritized over marginal improvements in average Sharpe.

Second, robustness must be evaluated multidimensionally. While VLSTM achieved the highest overall Sharpe ratio and strong passive-relative performance, VxLSTM and LPatchTST exhibited superior downside-adjusted characteristics in certain metrics, including Calmar ratio and minimum annual Sharpe. This distinction highlights an economically important trade-off: maximizing mean risk-adjusted return does not necessarily coincide with minimizing drawdown severity or tail exposure. The choice of architecture may therefore depend on investor preference over the mean–tail trade-off.

Third, turnover and transaction cost robustness meaningfully differentiate models. Breakeven transaction cost analysis reveals that xLSTM achieves the highest portfolio-level cost buffer, exceeding VLSTM despite slightly lower average Sharpe. This indicates greater resilience to implementation frictions and a higher signal-to-trade efficiency. Conversely, extremely low-turnover models such as iTransformer exhibit weak predictive performance, suggesting that insufficient responsiveness to evolving signals can be as detrimental as excessive trading. Successful architectures appear to strike a balance between adaptive state updating and controlled portfolio rebalancing.

Fourth, robustness to seed selection and experimental budget strengthens the credibility of the main findings. Performance rankings remain largely preserved under reduced seed aggregation, indicating that the reported differences are not artifacts of favorable initialization. This stability is particularly important in low signal-to-noise financial environments, where variance across runs can otherwise confound interpretation.

Fifth, state-space models and purely linear benchmarks exhibit heterogeneous and regime-sensitive behavior. While linear models occasionally perform well in high-volatility subperiods, they fail to deliver consistent cross-metric robustness. State-space architectures offer computational efficiency but require additional structure—such as feature selection or enriched state dynamics—to achieve competitive economic performance.

Taken together, the evidence suggests – though does not definitively establish – that successful financial forecasting architectures benefit from: (i) persistent and adaptively gated state representations, (ii) mechanisms for representation compression or feature conditioning, (iii) controlled trading intensity that preserves implementation robustness, and (iv) stability under adverse market realizations. Importantly, the most economically attractive models are not necessarily those with the highest average Sharpe, but those that jointly balance return, drawdown control, tail resilience, and transaction cost tolerance within realistic deployment constraints.

### 3.8 Computational Efficiency and Model Complexity

Table [5](#S3.T5 "Table 5 ‣ 3.8 Computational Efficiency and Model Complexity ‣ 3 Empirical Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") reported parameter counts as well as asymptotic runtime and memory complexities across models. The final number of trainable parameters and the corresponding hyperparameter ranges are provided in Appendix [C](#A3 "Appendix C Model Configurations and Hyperparameter Selection ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request."). Linear models exhibited minimal computational costs in terms of both parameterization and asymptotic complexity, although their empirical performance in previous subsections was comparatively weaker within this benchmark.

Among nonlinear architectures, VLSTM combined competitive empirical performance with linear memory complexity in sequence length and without quadratic attention terms. Relative to transformer-based models such as PatchTST or TFT, this resulted in lower asymptotic memory growth with respect to sequence length. Mamba and Mamba2 offered comparable asymptotic efficiency, though their empirical performance in this study was more heterogeneous across evaluation metrics.

Hybrid architectures, including LPatchTST and VSN-enhanced variants, involved higher parameter counts and additional computational overhead. Within the present evaluation, these increases in complexity were not uniformly associated with proportional performance improvements. This pattern suggested that asymptotic complexity alone did not determine empirical effectiveness, and that architectural inductive bias may play an important role in financial time-series modeling. As with all preceding results, these observations are conditional on the specific dataset, sequence lengths, and implementation choices considered.

| Model | Number of Parameters | Runtime Complexity | Memory Complexity |
| --- | --- | --- | --- |
| TFT | O​(C​H2+ℓ​H2)O(CH^{2}+\ell H^{2}) | O​(L2​H+L​C​H2)O(L^{2}H+LCH^{2}) | O​(L2+L​H)O(L^{2}+LH) |
| VLSTM | O​(C​H2+H2)O(CH^{2}+H^{2}) | O​(L​C​H2+L​H2)O(LCH^{2}+LH^{2}) | O​(L​H)O(LH) |
| Mamba | O​(ℓ​H2)O(\ell H^{2}) | O​(L​H2)O(LH^{2}) | O​(L​H)O(LH) |
| Mamba2 | O​(ℓ​H2)O(\ell H^{2}) | O​(L​H2)O(LH^{2}) | O​(L​H)O(LH) |
| VSN + Mamba2 | O​(C​H2+ℓ​H2)O(CH^{2}+\ell H^{2}) | O​(L​C​H2+L​H2)O(LCH^{2}+LH^{2}) | O​(L​H)O(LH) |
| AR1x | 𝐎​(𝟏)\mathbf{O(1)} | 𝐎​(𝐋)\mathbf{O(L)} | 𝐎​(𝟏)\mathbf{O(1)} |
| LSTM | O​(H2+C​H){\color[rgb]{.5,.5,.5}\definecolor[named]{pgfstrokecolor}{rgb}{.5,.5,.5}\pgfsys@color@gray@stroke{.5}\pgfsys@color@gray@fill{.5}O(H^{2}+CH)} | O​(L​H2)O(LH^{2}) | O​(L​H)O(LH) |
| NLinear | O​(L​C)¯\underline{O(LC)} | O​(L​C)¯\underline{O(LC)} | O​(L​C)¯\underline{O(LC)} |
| DLinear | O​(L​C)¯\underline{O(LC)} | O​(L​C)¯\underline{O(LC)} | O​(L​C)¯\underline{O(LC)} |
| xLSTM | O​(H2+C​H){\color[rgb]{.5,.5,.5}\definecolor[named]{pgfstrokecolor}{rgb}{.5,.5,.5}\pgfsys@color@gray@stroke{.5}\pgfsys@color@gray@fill{.5}O(H^{2}+CH)} | O​(L​H2)O(LH^{2}) | O​(L​H)O(LH) |
| Patch sLSTM | O​(P​C​H+H2)O(PCH+H^{2}) | O​(N​H2){\color[rgb]{.5,.5,.5}\definecolor[named]{pgfstrokecolor}{rgb}{.5,.5,.5}\pgfsys@color@gray@stroke{.5}\pgfsys@color@gray@fill{.5}O(NH^{2})} | O​(N​H){\color[rgb]{.5,.5,.5}\definecolor[named]{pgfstrokecolor}{rgb}{.5,.5,.5}\pgfsys@color@gray@stroke{.5}\pgfsys@color@gray@fill{.5}O(NH)} |
| VSN + xLSTM | O​(H2​(C+H))O(H^{2}(C+H)) | O​(L​H2)O(LH^{2}) | O​(L​H2)O(LH^{2}) |
| PatchTST | O​(P​C​H+ℓ​H2)O(PCH+\ell H^{2}) | O​(N2​H){\color[rgb]{.5,.5,.5}\definecolor[named]{pgfstrokecolor}{rgb}{.5,.5,.5}\pgfsys@color@gray@stroke{.5}\pgfsys@color@gray@fill{.5}O(N^{2}H)} | O​(N2+N​H)O(N^{2}+NH) |
| LSTM + PatchTST | O​(H2+P​C​H+ℓ​H2)O(H^{2}+PCH+\ell H^{2}) | O​(L​H2+N2​H)O(LH^{2}+N^{2}H) | O​(L​H+N2)O(LH+N^{2}) |
| iTransformer | O​(ℓ​H2)O(\ell H^{2}) | O​(C2​H+L​C​H)O(C^{2}H+LCH) | O​(C2+L​C)O(C^{2}+LC) |

Table 5: Comparison of parameter count, runtime complexity, and memory complexity for different time-series forecasting models. The emphasis on order of results is as follows: best, second\_best, t​h​i​r​d​\_​b​e​s​t{\color[rgb]{.5,.5,.5}\definecolor[named]{pgfstrokecolor}{rgb}{.5,.5,.5}\pgfsys@color@gray@stroke{.5}\pgfsys@color@gray@fill{.5}third\\_best}. The forecasting horizon is fixed to one. LL=sequence length, CC=number of input features, HH=hidden dimension, NN=L−SL-S=number of patches (for shifted versions adjusted for each time step), PP=patch length, SS=stride, KK=convolution kernel size, ℓ\ell=number of layers, MM=number of attention heads.

## 4 Conclusions

This paper presented a comprehensive benchmark of deep learning architectures for financial time-series prediction under a unified experimental framework spanning 15 years, multiple asset classes, heterogeneous market regimes, and a broad set of economic and statistical diagnostics. Models were evaluated not only on average risk-adjusted returns, but also on downside risk, tail exposure, transaction cost robustness, implementation intensity, and sensitivity to random initialization.

Several robust patterns emerged:

First, purely linear models exhibited occasional regime-specific competitiveness but failed to deliver stable multi-metric performance. Their limited adaptability to non-stationarity and structural change constrained their long-horizon effectiveness.

Second, architectures explicitly designed to learn structured and adaptively gated temporal representations consistently outperformed generic attention-based and state-space alternatives. VLSTM achieved the highest overall Sharpe ratio and strong passive-relative performance. However, models such as VxLSTM and LPatchTST demonstrated superior downside-adjusted robustness, including stronger Calmar ratios and more stable worst-year outcomes. These results highlight that mean risk-adjusted return and drawdown resilience need not coincide, and that investor objectives may favor different architectural trade-offs.

Third, transaction cost robustness meaningfully differentiates models. xLSTM achieved the highest breakeven cost buffer at the portfolio level, indicating improved signal-to-trade efficiency. Extremely low-turnover architectures, such as iTransformer, exhibited limited predictive strength, suggesting that insufficient responsiveness to evolving signals may undermine economic performance. Effective models appear to balance adaptive state updating with disciplined trading intensity.

Fourth, performance rankings remained largely stable under reduced seed aggregation and experimental budgets, reinforcing that observed differences are not artifacts of favorable initialization or excessive tuning.

Collectively, the evidence suggests that successful financial forecasting architectures benefit from persistent and adaptively gated state representations, representation compression or feature conditioning mechanisms, and efficient translation of predictive signals into implementable portfolio decisions. Importantly, the most economically attractive models are those that jointly balance average return, drawdown control, tail robustness, and implementation feasibility.
  
The conclusions remain conditional on the dataset, market universe, and backtesting assumptions employed. Nevertheless, by evaluating models under realistic non-stationarity, heavy tails, volatility clustering, and transaction cost constraints, this benchmark aims to reflect the statistical and economic challenges inherent to practical financial forecasting. We hope it provides a transparent empirical reference point for future research and encourages architectural development guided not only by computational considerations, but also by the distinctive structural properties of financial markets.

## Acknowledgments

Kieran Wood would like to thank the Oxford-Man Institute of Quantitative Finance for its generous support.

## References

* Vaswani et al. [2017]

  Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin.
  Attention is all you need.
  In *Advances in Neural Information Processing Systems*, volume 30, 2017.
* Islam et al. [2024]

  Saidul Islam, Hanae Elmekki, Ahmed Elsebai, Jamal Bentahar, Najat Drawel, Gaith Rjoub, and Witold Pedrycz.
  A comprehensive survey on applications of transformers for deep learning tasks.
  *Expert Systems with Applications*, 241:122666, 2024.
  doi: 10.1016/j.eswa.2023.122666.
* Liu et al. [2024]

  Yong Liu, Tengge Hu, Haoran Zhang, Haixu Wu, Shiyu Wang, Lintao Ma, and Mingsheng Long.
  iTransformer: Inverted transformers are effective for time series forecasting.
  In *International Conference on Learning Representations (ICLR)*, 2024.
  doi: 10.48550/arXiv.2310.06625.
  URL <https://openreview.net/forum?id=JePfAI8fah>.
* Nie et al. [2023]

  Yuqi Nie, Nam H. Nguyen, Phanwadee Sinthong, and Jayant Kalagnanam.
  A time series is worth 64 words: Long-term forecasting with transformers.
  In *International Conference on Learning Representations (ICLR)*, 2023.
  doi: 10.48550/arXiv.2211.14730.
  URL <https://openreview.net/forum?id=Jbdc0vTOcol>.
* Lim et al. [2021]

  Bryan Lim, Sercan Ö. Arık, Nicolas Loeff, and Tomas Pfister.
  Temporal fusion transformers for interpretable multi-horizon time series forecasting.
  *International Journal of Forecasting*, 37(4):1748–1764, 2021.
  doi: 10.1016/j.ijforecast.2021.03.012.
  URL <https://doi.org/10.1016/j.ijforecast.2021.03.012>.
* Dao and Gu [2024]

  Tri Dao and Albert Gu.
  Transformers are SSMs: Generalized models and efficient algorithms through structured state space duality, 2024.
  URL <https://arxiv.org/abs/2405.21060>.
* Katharopoulos et al. [2020]

  Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and François Fleuret.
  Transformers are RNNs: Fast autoregressive transformers with linear attention.
  In *Proceedings of the 37th International Conference on Machine Learning (ICML)*, volume 119 of *Proceedings of Machine Learning Research*, 2020.
  doi: 10.48550/arXiv.2006.16236.
  URL <https://arxiv.org/abs/2006.16236>.
* Gu et al. [2020]

  Albert Gu, Tri Dao, Stefano Ermon, Atri Rudra, and Christopher Ré.
  HiPPO: Recurrent memory with optimal polynomial projections.
  In *Advances in Neural Information Processing Systems*, volume 33, pages 1474–1487, 2020.
  URL <https://arxiv.org/abs/2008.07669>.
* Feng et al. [2024]

  Leo Feng, Felix Tung, Mostofa O. Ahmed, Yoshua Bengio, and Houd Hajimirsadeghi.
  Were RNNs all we needed?, 2024.
  URL <https://arxiv.org/abs/2410.01201>.
* Hewamalage et al. [2021]

  Hansika Hewamalage, Christoph Bergmeir, and Kasun Bandara.
  Recurrent neural networks for time series forecasting: Current status and future directions.
  *International Journal of Forecasting*, 37(1):388–427, 2021.
  doi: 10.1016/j.ijforecast.2020.06.008.
  URL <https://arxiv.org/abs/1909.00590>.
* Hochreiter and Schmidhuber [1997]

  Sepp Hochreiter and Jürgen Schmidhuber.
  Long short-term memory.
  *Neural Computation*, 9(8):1735–1780, 1997.
  doi: 10.1162/neco.1997.9.8.1735.
* Beck et al. [2024]

  Maximilian Beck, Konstantin Pöppel, Markus Spanring, Andreas Auer, Olga Prudnikova, Michael Kopp, Günter Klambauer, Johannes Brandstetter, and Sepp Hochreiter.
  xLSTM: Extended long short-term memory.
  In *Advances in Neural Information Processing Systems*, volume 37, 2024.
  doi: 10.48550/arXiv.2405.04517.
  URL <https://arxiv.org/abs/2405.04517>.
* Kong et al. [2025]

  Yaxuan Kong, Zepu Wang, Yuqi Nie, Tian Zhou, Stefan Zohren, Yuxuan Liang, Peng Sun, and Qingsong Wen.
  Unlocking the power of LSTM for long term time series forecasting.
  In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 39, pages 11968–11976, 2025.
  doi: 10.1609/aaai.v39i11.33303.
  URL <https://ojs.aaai.org/index.php/AAAI/article/view/33303>.
* Wang et al. [2024]

  Yuxuan Wang, Haixu Wu, Jiaxiang Dong, Yong Liu, Chen Wang, Mingsheng Long, and Jianmin Wang.
  Deep time series models: A comprehensive survey and benchmark, 2024.
  URL <https://arxiv.org/abs/2407.13278>.
* Zeng et al. [2023]

  Ailing Zeng, Muxi Chen, Lei Zhang, and Qiang Xu.
  Are transformers effective for time series forecasting?
  In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 37, pages 11121–11128, 2023.
  doi: 10.1609/aaai.v37i9.26317.
  URL <https://ojs.aaai.org/index.php/AAAI/article/view/26317>.
* Cont [2001]

  Rama Cont.
  Empirical properties of asset returns: Stylized facts and statistical issues.
  *Quantitative Finance*, 1(2):223–236, 2001.
  doi: 10.1080/713665670.
* Yule [1927]

  George Udny Yule.
  On a method of investigating periodicities in disturbed series, with special reference to wolfer’s sunspot numbers.
  *Philosophical Transactions of the Royal Society of London. Series A*, 226:267–298, 1927.
  doi: 10.1098/rsta.1927.0007.
  URL <https://www.jstor.org/stable/91170>.
* Sezer et al. [2019]

  Omer Berat Sezer, Mehmet Ugur Gudelek, and Ahmet Mert Ozbayoglu.
  Financial time series forecasting with deep learning: A systematic literature review: 2005–2019, 2019.
  URL <https://arxiv.org/abs/1911.13288>.
* Liu and Wang [2024]

  Xinhe Liu and Wenmin Wang.
  Deep time series forecasting models: A comprehensive survey.
  *Mathematics*, 12(10):1504, 2024.
  doi: 10.3390/math12101504.
  URL <https://www.mdpi.com/2227-7390/12/10/1504>.
* Buczyński et al. [2023]

  Mateusz Buczyński, Marcin Chlebus, Katarzyna Kopczewska, and Marcin Zajenkowski.
  Financial time series models—comprehensive review of deep learning approaches and practical recommendations.
  *Engineering Proceedings*, 39(1):79, 2023.
  doi: 10.3390/engproc2023039079.
  URL <https://www.mdpi.com/2673-4591/39/1/79>.
* Guo and Berkhahn [2016]

  Cheng Guo and Felix Berkhahn.
  Entity embeddings of categorical variables.
  *arXiv preprint arXiv:1604.06737*, 2016.
  URL <https://arxiv.org/abs/1604.06737>.
* Moskowitz et al. [2012]

  Tobias J. Moskowitz, Yao Hua Ooi, and Lasse Heje Pedersen.
  Time series momentum.
  *Journal of Financial Economics*, 104(2):228–250, 2012.
  doi: 10.1016/j.jfineco.2011.11.003.
  URL <https://www.sciencedirect.com/science/article/pii/S0304405X11002613>.
* Harvey et al. [2018]

  Campbell R. Harvey, Edward Hoyle, Rohit Korgaonkar, Sandy Rattray, Matthew Sargaison, and Otto Van Hemert.
  The impact of volatility targeting.
  *The Journal of Portfolio Management*, 45(1):14–33, 2018.
  doi: 10.3905/jpm.2018.45.1.014.
* Lim et al. [2019]

  Bryan Lim, Stefan Zohren, and Stephen Roberts.
  Enhancing time-series momentum strategies using deep neural networks.
  *The Journal of Financial Data Science*, 1(4):19–38, 2019.
  doi: 10.3905/jfds.2019.1.015.
* Wood et al. [2026]

  Kieran Wood, Stephen J. Roberts, and Stefan Zohren.
  DeePM: Regime-robust deep learning for systematic macro portfolio management, 2026.
  URL <https://arxiv.org/abs/2601.05975>.
* Zhou et al. [2025]

  Yufa Zhou, Yixiao Wang, Surbhi Goel, and Anru R. Zhang.
  Why do transformers fail to forecast time series in-context?, 2025.
  URL <https://arxiv.org/abs/2510.09776>.
* Liu et al. [2022]

  Yong Liu, Haixu Wu, Jianmin Wang, and Mingsheng Long.
  Non-stationary transformers: Exploring the stationarity in time series forecasting, 2022.
  URL <https://arxiv.org/abs/2205.14415>.
* Oliveira and Ramos [2024]

  José M. Oliveira and Pedro Ramos.
  Evaluating the effectiveness of time series transformers for demand forecasting.
  *Mathematics*, 12(17):2728, 2024.
  doi: 10.3390/math12172728.
  URL <https://www.mdpi.com/2227-7390/12/17/2728>.
* Gu and Dao [2024]

  Albert Gu and Tri Dao.
  Mamba: Linear-time sequence modeling with selective state spaces.
  In *Proceedings of the First Conference on Language Modeling (COLM)*, 2024.
  doi: 10.48550/arXiv.2312.00752.
  URL <https://openreview.net/forum?id=tEYskw1VY2>.
* Gu et al. [2022]

  Albert Gu, Karan Goel, and Christopher Ré.
  Efficiently modeling long sequences with structured state spaces.
  In *International Conference on Learning Representations (ICLR)*, 2022.
  doi: 10.48550/arXiv.2111.00396.
  URL <https://openreview.net/forum?id=uYLFoz1vlAC>.
* Fjellström [2022]

  Carl Fjellström.
  Long short-term memory neural network for financial time series, 2022.
  URL <https://arxiv.org/abs/2201.08218>.
* Wood et al. [2024]

  Kieran Wood, Samuel Kessler, Stephen J. Roberts, and Stefan Zohren.
  Few-shot learning patterns in financial time series for trend-following strategies.
  *The Journal of Financial Data Science*, 6(2):88–115, 2024.
  doi: 10.3905/jfds.2024.1.157.
* Wood et al. [2021]

  Kieran Wood, Sven Giegerich, Stephen Roberts, and Stefan Zohren.
  Trading with the momentum transformer: An intelligent and interpretable architecture, 2021.
  URL <https://arxiv.org/abs/2112.08534>.
* [34]

  Pinnacle Data Corp.
  Pinnacle data corp. CLC database.
  Website.
  URL <https://pinnacledata2.com/clc.html>.
* Elton et al. [2014]

  Edwin J. Elton, Martin J. Gruber, Stephen J. Brown, and William N. Goetzmann.
  *Modern Portfolio Theory and Investment Analysis*.
  John Wiley & Sons, 9 edition, 2014.
* Sharpe [1994]

  William F. Sharpe.
  The sharpe ratio.
  *Journal of Portfolio Management*, 21(1):49–58, 1994.
* Newey and West [1987]

  Whitney K. Newey and Kenneth D. West.
  A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix.
  *Econometrica*, 55(3):703–708, 1987.
* Pesaran and Timmermann [1992]

  M. Hashem Pesaran and Allan Timmermann.
  A simple nonparametric test of predictive performance.
  *Journal of Business & Economic Statistics*, 10(4):461–465, 1992.
* Zhang et al. [2023]

  Cheng Zhang, Nilam Nur Amir Sjarif, and Roslina Ibrahim.
  Deep learning models for price forecasting of financial time series: A review of recent advancements (2020–2022), 2023.
  URL <https://arxiv.org/abs/2304.11228>.
* Bucci [2020]

  Andrea Bucci.
  Realized volatility forecasting with neural networks.
  *Journal of Financial Econometrics*, 18(3):502–531, 2020.
  doi: 10.1093/jjfinec/nbaa008.
  URL <https://academic.oup.com/jfec/article/18/3/502/5856840>.
* Kohonen [1972]

  Teuvo Kohonen.
  Correlation matrix memories.
  *IEEE Transactions on Computers*, C-21(4):353–359, 1972.
  doi: 10.1109/TC.1972.5008975.
* Anderson [1972]

  James A. Anderson.
  A simple neural network generating an interactive memory.
  *Mathematical Biosciences*, 14:197–220, 1972.
  doi: 10.1016/0025-5564(72)90075-2.
* Nakano [1972]

  K. Nakano.
  Associatron—a model of associative memory.
  *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-2(3):380–388, 1972.
  doi: 10.1109/TSMC.1972.4309133.
* Anderson et al. [1977]

  John R. Anderson, James W. Silverstein, Steven A. Ritz, and Randall S. Jones.
  Distinctive features, categorical perception, and probability learning: Some applications of a neural model.
  *Psychological Review*, 84(5):413–451, 1977.
  doi: 10.1037/0033-295X.84.5.413.
* Kingma and Ba [2015]

  Diederik P. Kingma and Jimmy Ba.
  Adam: A method for stochastic optimization.
  In *International Conference on Learning Representations*, 2015.

## Appendix A Data Construction and Exploratory Analysis

This appendix documents the construction of all variables used in the empirical analysis and provides detailed evidence on their distributional properties.

### A.1 Raw Data and Return Construction

The raw dataset consists of daily observations with three fields: date, ticker, and closing price. From these, daily returns are computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=Pt−Pt−1Pt−1,r\_{t}=\frac{P\_{t}-P\_{t-1}}{P\_{t-1}}, |  | (15) |

where PtP\_{t} denotes the closing price at time tt.

### A.2 Volatility Estimation

Daily volatility is estimated using an exponentially weighted moving average (EWMA) estimator. Let λ=2span+1\lambda=\frac{2}{\text{span}+1}. The conditional mean and variance evolve according to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μt\displaystyle\mu\_{t} | =λ​rt+(1−λ)​μt−1,\displaystyle=\lambda r\_{t}+(1-\lambda)\mu\_{t-1}, |  | (16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σt2\displaystyle\sigma\_{t}^{2} | =λ​(rt−μt)2+(1−λ)​σt−12.\displaystyle=\lambda(r\_{t}-\mu\_{t})^{2}+(1-\lambda)\sigma\_{t-1}^{2}. |  | (17) |

### A.3 Distribution of Returns and Volatility

![Refer to caption](2603.01820v1/Images/data_daily_returns.png)


Figure 3: Distribution of daily returns. To make the central mass visible, the figure focuses on the bulk of the distribution; tail behavior is examined separately.

![Refer to caption](2603.01820v1/Images/data_daily_vol.png)


Figure 4: Distribution of daily realized volatility (log scale). Volatility exhibits strong right skewness and a long upper tail.

Figure [3](#A1.F3 "Figure 3 ‣ A.3 Distribution of Returns and Volatility ‣ Appendix A Data Construction and Exploratory Analysis ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") reports the empirical distribution of daily returns across all assets. The distribution is sharply peaked around zero and exhibits pronounced leptokurtosis. Figure [4](#A1.F4 "Figure 4 ‣ A.3 Distribution of Returns and Volatility ‣ Appendix A Data Construction and Exploratory Analysis ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") shows the distribution of realized volatility on a logarithmic scale, highlighting strong right skewness and a long upper tail.

Figure [5](#A1.F5 "Figure 5 ‣ A.3 Distribution of Returns and Volatility ‣ Appendix A Data Construction and Exploratory Analysis ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") presents a quantile–quantile plot against the normal distribution together with the tail behavior of absolute returns. Both figures indicate substantial deviations from Gaussianity and slow tail decay.

![Refer to caption](2603.01820v1/Images/data_vs_normal.png)


Figure 5: Left: Quantile–quantile plot against the normal distribution. Right: Tail behavior of daily returns. The figures indicate substantial deviations from Gaussianity and heavy-tailed return dynamics.

### A.4 Predictive Features

Normalized returns are constructed over multiple horizons (1 day, 1 week, 1 month, 3 months, 6 months, and 1 year) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt,hnorm=rt,hσt​h,r^{\text{norm}}\_{t,h}=\frac{r\_{t,h}}{\sigma\_{t}\sqrt{h}}, |  | (18) |

where hh denotes the horizon in trading days.

Momentum indicators are further augmented using volatility-normalized and regime-adjusted Moving Average Convergence Divergence (MACD) signals:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | MACDt\displaystyle\operatorname{MACD}\_{t} | =EWMAh​(Ts)(P)t−EWMAh​(Tl)(P)t,\displaystyle=\operatorname{EWMA}\_{h(T\_{s})}(P)\_{t}-\operatorname{EWMA}\_{h(T\_{l})}(P)\_{t}, |  | (19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | qt\displaystyle q\_{t} | =MACDtStd63(P)t,\displaystyle=\frac{\operatorname{MACD}\_{t}}{\operatorname{Std}\_{63}(P)\_{t}}, |  | (20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Signalt\displaystyle\operatorname{Signal}\_{t} | =qtStd252(q)t.\displaystyle=\frac{q\_{t}}{\operatorname{Std}\_{252}(q)\_{t}}. |  | (21) |

The empirical distributions of these features are approximately symmetric and concentrated within the interval [−2,2][-2,2], with nearly all observations contained in [−4,4][-4,4], as shown in Figure [6](#A1.F6 "Figure 6 ‣ A.4 Predictive Features ‣ Appendix A Data Construction and Exploratory Analysis ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.").

![Refer to caption](2603.01820v1/Images/data_mom_features.png)


Figure 6: Distribution of Momentum Features.

### A.5 Volatility-Scaled Exposure and Target Variable

Volatility targeting induces a time-varying exposure factor defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | vs\_factort=1σt.\text{vs\\_factor}\_{t}=\frac{1}{\sigma\_{t}}. |  | (22) |

The empirical distribution of v​s​\_​f​a​c​t​o​rvs\\_factor exhibits pronounced right skewness, Figure [7](#A1.F7 "Figure 7 ‣ A.5 Volatility-Scaled Exposure and Target Variable ‣ Appendix A Data Construction and Exploratory Analysis ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request."). A large share of the mass is concentrated at relatively low values, while a long right tail corresponds to regimes or contracts characterized by unusually low realized volatility. These extreme realizations arise endogenously from the volatility-scaling mechanism itself and do not primarily reflect structural market dislocations or persistent risk premia.

From a modeling perspective, this feature is consequential. Linear specifications that treat volatility-scaled exposure as approximately proportional to changes in volatility may fail to capture the asymmetric response of leverage across regimes. Flexible nonlinear architectures are better suited to accommodate the threshold-like behavior induced by volatility targeting, especially in settings where exposure amplification during low-volatility periods magnifies the effect of predictive signals, while exposure compression during high-volatility episodes dampens their impact.

![Refer to caption](2603.01820v1/Images/data_vs_factor.png)


Figure 7: Induced Exposure by Volatility Targeting.

The learning target is constructed as the volatility-scaled next-period return,

|  |  |  |  |
| --- | --- | --- | --- |
|  | targett=clip⁡(rt+1σt,−20,20),\text{target}\_{t}=\operatorname{clip}\left(\frac{r\_{t+1}}{\sigma\_{t}},-20,20\right), |  | (23) |

where clipping is applied to limit the influence of extreme realizations during training.

### A.6 Stylized Facts of Returns and Volatility

Daily returns exhibit strong deviations from Gaussianity, with heavy tails and excess kurtosis that imply substantial downside risk and state dependence. Realized volatility is highly skewed and persistent, reflecting clustering and regime-dependent risk dynamics. These features challenge linear predictive models that rely on homoskedastic or symmetric error assumptions.

### A.7 Formal Statistical Diagnostics

To formally substantiate the distributional characteristics suggested by the graphical evidence, we conduct standard diagnostic tests.

First, normality of returns is rejected at conventional significance levels using the Jarque–Bera test across the majority of instruments, consistent with the heavy tails observed in Figure [5](#A1.F5 "Figure 5 ‣ A.3 Distribution of Returns and Volatility ‣ Appendix A Data Construction and Exploratory Analysis ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request."). Excess kurtosis and skewness statistics further confirm substantial deviations from Gaussianity.

Second, we test for non-stationarity in price levels using augmented Dickey–Fuller tests. As expected for financial price series, unit roots cannot generally be rejected in levels, while returns exhibit stationarity. This is consistent with the standard representation of asset prices as integrated processes with stationary increments.

Third, volatility persistence is assessed via autocorrelation of squared returns and realized volatility. We observe slow decay in the autocorrelation function, confirming volatility clustering and regime dependence.

Taken together, these diagnostics confirm that the dataset exhibits canonical stylized facts of financial time series: heavy tails, conditional heteroskedasticity, and non-stationarity in levels.

### A.8 Implications for Modeling

Taken together, the distributional evidence highlights a fundamental feature of the data. While the input predictors are largely bounded, symmetric, and well-behaved, the target variable—realized returns—exhibits extreme kurtosis, heavy tails, and strong state dependence. This mismatch implies that the primary modeling challenge lies not in stabilizing the inputs, but in accurately capturing the conditional distribution of returns given these inputs.

These empirical properties motivate the use of flexible nonlinear architectures that can accommodate interactions, threshold effects, and regime-dependent behavior. Nonlinear dependencies and regime changes are frequently observed in financial time series and are captured most effectively by nonlinear models [[39](#bib.bib39)]. Neural network architectures such as LSTMs have shown superior performance in capturing complex nonlinear patterns in volatility and return dynamics [[40](#bib.bib40)]. In environments where small changes in predictors can, under certain conditions, lead to disproportionately large changes in outcomes, models that adapt their functional form across the state space are particularly well suited.

### A.9 Scope and External Validity

While the dataset exhibits statistical properties commonly observed in financial markets, the conclusions drawn in this study are, strictly speaking, conditional on the data considered. As with any empirical investigation, it is not possible to establish universal generality beyond the sampled instruments and time period.

That said, the presence of heavy-tailed returns, volatility clustering, and regime-dependent dynamics suggests that the dataset captures structural characteristics typical of many financial time series. For this reason, we view the benchmark as representative of a broad class of cross-asset forecasting problems. Nevertheless, extending the analysis to alternative markets, frequencies, or macroeconomic environments remains an important direction for future research.

## Appendix B Architecture Components

### B.1 Linear Baselines

#### Autoregressive Model (AR1x).

We consider an AR(1) process

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=ϕ​yt−1+εt,εt∼𝒩​(0,σ2),y\_{t}=\phi y\_{t-1}+\varepsilon\_{t},\quad\varepsilon\_{t}\sim\mathcal{N}(0,\sigma^{2}), |  | (24) |

which captures short-term autocorrelation. This model assumes 1 one input feature. AR1x simply applies AR(1) to each feature independently (for multiple input features).

#### DLinear and NLinear.

DLinear and NLinear [[15](#bib.bib15)] apply linear mappings to the input window:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y^t=W​𝐗t+b.\hat{y}\_{t}=W\mathbf{X}\_{t}+b. |  | (25) |

DLinear decomposes the input into trend and seasonal components, while NLinear operates on normalized inputs. Both models lack temporal state and serve as non-recurrent linear baselines.

### B.2 Transformer Background

Transformer architectures [[1](#bib.bib1)] compute self-attention quadratically as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Attn​(Q,K,V)=softmax​(Q​K⊤dk)​V.\text{Attn}(Q,K,V)=\text{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d\_{k}}}\right)V. |  | (26) |

Therefore, Transformer-based models have a large number of trainable parameters.

### B.3 State-Space Model Details

Mamba models [[29](#bib.bib29), [6](#bib.bib6)] implement selective state-space models of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=At​ht−1+Bt​xt,yt=Ct​ht,h\_{t}=A\_{t}h\_{t-1}+B\_{t}x\_{t},\qquad y\_{t}=C\_{t}h\_{t}, |  | (27) |

where hth\_{t} denotes the latent state, xtx\_{t} the input, and yty\_{t} the output. The matrices AtA\_{t}, BtB\_{t}, and CtC\_{t} are initialized using HiPPO LegS matrices [[8](#bib.bib8)], which provide a principled discretization of continuous-time linear dynamical systems.

In Mamba2, the state transition matrix is replaced with a scaled identity, and the architecture incorporates a form of linear attention [[7](#bib.bib7)], improving efficiency and numerical stability.

In this work, we employ a static HiPPO transition matrix and a fixed low-rank parameterization of the step size Δ\Delta, resulting in a fixed temporal horizon. This modification reduces sensitivity to noise and improves robustness when modeling financial time series.

### B.4 LSTM-based models

The LSTM architecture is included as a canonical gated recurrent model that addresses the vanishing gradient limitations of standard RNNs through an additive memory cell and multiplicative gating. The forget and input gates enable adaptive control over memory retention and update, effectively implementing a data-dependent filtering mechanism.

The LSTM [[11](#bib.bib11)] updates are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ft\displaystyle f\_{t} | =σ​(Wf​xt+Uf​ht−1+bf),\displaystyle=\sigma(W\_{f}x\_{t}+U\_{f}h\_{t-1}+b\_{f}), |  | (28) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | it\displaystyle i\_{t} | =σ​(Wi​xt+Ui​ht−1+bi),\displaystyle=\sigma(W\_{i}x\_{t}+U\_{i}h\_{t-1}+b\_{i}), |  | (29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ot\displaystyle o\_{t} | =σ​(Wo​xt+Uo​ht−1+bo),\displaystyle=\sigma(W\_{o}x\_{t}+U\_{o}h\_{t-1}+b\_{o}), |  | (30) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ct\displaystyle c\_{t} | =ft⊙ct−1+it⊙tanh⁡(Wc​xt),\displaystyle=f\_{t}\odot c\_{t-1}+i\_{t}\odot\tanh(W\_{c}x\_{t}), |  | (31) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ht\displaystyle h\_{t} | =ot⊙tanh⁡(ct),\displaystyle=o\_{t}\odot\tanh(c\_{t}), |  | (32) |

where ftf\_{t}, iti\_{t}, and oto\_{t} denote the forget, input, and output gates, respectively. Such adaptive memory is particularly relevant in financial time series, where structural breaks and regime shifts render fixed-memory models suboptimal. The gating mechanism allows the model to dynamically adjust the effective time horizon over which past information is retained.

Moreover, the nonlinear hidden-state representation provides a flexible mechanism for extracting predictive structure from low signal-to-noise and non-Gaussian data, making LSTMs a natural and widely adopted baseline in financial forecasting tasks.

#### xLSTM.

We provide a concise technical description of xLSTM following [[12](#bib.bib12)] (Eq. 8–17).

##### Exponential Gating.

In contrast to classical LSTMs, which employ sigmoid gates ft=σ​(⋅)f\_{t}=\sigma(\cdot) and it=σ​(⋅)i\_{t}=\sigma(\cdot), xLSTM replaces sigmoid activations with exponential gating followed by normalization. Let

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f~t\displaystyle\tilde{f}\_{t} | =Wf​xt+Rf​ht−1+bf,\displaystyle=W\_{f}x\_{t}+R\_{f}h\_{t-1}+b\_{f}, |  | (33) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | i~t\displaystyle\tilde{i}\_{t} | =Wi​xt+Ri​ht−1+bi,\displaystyle=W\_{i}x\_{t}+R\_{i}h\_{t-1}+b\_{i}, |  | (34) |

which are the pre-activation gates, similar to LSTM. The raw gates are exponentiated,

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^t=exp⁡(f~t),i^t=exp⁡(i~t),\hat{f}\_{t}=\exp(\tilde{f}\_{t}),\qquad\hat{i}\_{t}=\exp(\tilde{i}\_{t}), |  | (35) |

and subsequently normalized to ensure numerical stability and controlled memory growth. In log-domain form, this normalization is implemented via a running maximum term to prevent overflow (see [[12](#bib.bib12)], Eq. 15–17). The resulting gates satisfy a convex combination structure analogous to classical LSTM gating but without sigmoid saturation.

##### sLSTM (Scalar LSTM).

The scalar variant maintains a single memory state per unit. The update equations are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | c~t\displaystyle\tilde{c}\_{t} | =tanh⁡(Wz​xt+Rz​ht−1+bz),\displaystyle=\tanh(W\_{z}x\_{t}+R\_{z}h\_{t-1}+b\_{z}), |  | (36) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ct\displaystyle c\_{t} | =ft⊙ct−1+it⊙c~t,\displaystyle=f\_{t}\odot c\_{t-1}+i\_{t}\odot\tilde{c}\_{t}, |  | (37) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | nt\displaystyle n\_{t} | =ft⊙nt−1+it,\displaystyle=f\_{t}\odot n\_{t-1}+i\_{t}, |  | (38) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ht\displaystyle h\_{t} | =ot⊙ctnt,\displaystyle=o\_{t}\odot\frac{c\_{t}}{n\_{t}}, |  | (39) |

where ftf\_{t}, iti\_{t}, and oto\_{t} denote normalized exponential forget, input, and output gates, respectively, and ntn\_{t} is a stabilizing normalizer. The division by ntn\_{t} ensures scale control of the memory state.

##### mLSTM (Matrix LSTM).

The matrix variant generalizes the memory to a matrix-valued state Ct∈ℝd×dC\_{t}\in\mathbb{R}^{d\times d}. At each step, key–value vectors kt,vt∈ℝdk\_{t},v\_{t}\in\mathbb{R}^{d} are generated and stored via a gated outer-product update:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct=ft⊙Ct−1+it⊙(vt​kt⊤).C\_{t}=f\_{t}\odot C\_{t-1}+i\_{t}\odot(v\_{t}k\_{t}^{\top}). |  | (40) |

The hidden state is retrieved through a query vector qtq\_{t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=Ct​qt,h\_{t}=C\_{t}q\_{t}, |  | (41) |

This Bidirectional Associative Memory (BAM) [[41](#bib.bib41), [42](#bib.bib42), [43](#bib.bib43), [44](#bib.bib44)] setting yields high separability between stored patterns and allows efficient recall of past information. Importantly, mLSTM removes state compression recurrence but still has temporal dependency in memory accumulation. It is more parallelizable, but not fully parallel.

#### Patch sLSTM (PsLSTM).

Given a multivariate time series X∈ℝL×dX\in\mathbb{R}^{L\times d}, each channel is treated independently and segmented into non-overlapping patches of length ℓ\ell:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x~p(i)=Patch​(x(p−1)​ℓ+1:p​ℓ(i)),i=1,…,d.\tilde{x}\_{p}^{(i)}=\mathrm{Patch}\left(x\_{(p-1)\ell+1:p\ell}^{(i)}\right),\quad i=1,\dots,d. |  | (42) |

Each patch embedding is processed by an sLSTM with shared parameters across channels:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hp(i)=sLSTM​(hp−1(i),x~p(i)).h\_{p}^{(i)}=\mathrm{sLSTM}(h\_{p-1}^{(i)},\tilde{x}\_{p}^{(i)}). |  | (43) |

Parameter sharing preserves channel independence while reducing model complexity and mitigating overfitting.

### B.5 Hybrid Architecture Details

The hybrids are designed to improve robustness in noisy financial time series by enhancing the signal-to-noise ratio, enabling adaptive feature selection, and stabilizing temporal state updates.

#### Variable Selection Network (VSN)

The Variable Selection Network (VSN), inspired by the Temporal Fusion Transformer [[5](#bib.bib5)], performs feature-wise nonlinear embedding followed by dynamic soft selection of relevant covariates at each time step.

Given an input vector xt∈ℝCx\_{t}\in\mathbb{R}^{C} consisting of CC covariates, each variable is embedded independently:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht,i=ϕi​(xt,i),i=1,…,C,h\_{t,i}=\phi\_{i}(x\_{t,i}),\quad i=1,\dots,C, |  | (44) |

where ϕi​(⋅)\phi\_{i}(\cdot) denotes a learnable nonlinear embedding function.

The embeddings are concatenated and passed through a gating network to compute feature importance weights:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αt=softmax​(Wg​[ht,1,…,ht,C]+bg),\alpha\_{t}=\text{softmax}\left(W\_{g}[h\_{t,1},\dots,h\_{t,C}]+b\_{g}\right), |  | (45) |

where WgW\_{g} and bgb\_{g} are learnable parameters.

The selected representation is computed as a weighted sum:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x~t=∑i=1Cαt,i​ht,i.\tilde{x}\_{t}=\sum\_{i=1}^{C}\alpha\_{t,i}h\_{t,i}. |  | (46) |

This mechanism enables adaptive suppression of noisy or uninformative covariates and improves robustness in non-stationary environments.

#### VSN+LSTM (VLSTM)

The VSN+LSTM (VLSTM) model combines VSN-based feature selection with recurrent temporal encoding. At each time step, the input vector is processed by a VSN to produce a dynamically weighted feature representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x~t=VSN​(xt).\tilde{x}\_{t}=\mathrm{VSN}(x\_{t}). |  | (47) |

The resulting sequence {x~t}t=1L\{\tilde{x}\_{t}\}\_{t=1}^{L} is then passed through an LSTM to construct a compact temporal state:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ht,ct)=LSTM​(x~t,ht−1,ct−1).(h\_{t},c\_{t})=\mathrm{LSTM}(\tilde{x}\_{t},h\_{t-1},c\_{t-1}). |  | (48) |

For one-step-ahead forecasting, the prediction is obtained from the final hidden state:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y^L+1=Wo​hL+bo.\hat{y}\_{L+1}=W\_{o}h\_{L}+b\_{o}. |  | (49) |

#### VSN–Mamba2

In the VSN–Mamba2 hybrid, feature selection and temporal modeling are explicitly decoupled. Given an input xt∈ℝdx\_{t}\in\mathbb{R}^{d}, the VSN computes feature-wise importance weights:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αt=softmax​(g​(xt)),x~t=αt⊙xt,\alpha\_{t}=\text{softmax}(g(x\_{t})),\qquad\tilde{x}\_{t}=\alpha\_{t}\odot x\_{t}, |  | (50) |

where g​(⋅)g(\cdot) denotes a learnable gating network and ⊙\odot denotes element-wise multiplication.

The filtered input x~t\tilde{x}\_{t} is then passed to the Mamba2 state-space block:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=A​ht−1+B​x~t,h\_{t}=Ah\_{t-1}+B\tilde{x}\_{t}, |  | (51) |

where AA and BB denote the state transition and input matrices, respectively. This design improves robustness by reducing the influence of noisy covariates prior to temporal state updates.

#### LSTM + PatchTST

This hybrid architecture combines explicit recurrence with attention by using an LSTM as a channel-wise temporal denoiser prior to PatchTST. Each input channel is processed independently using a shared LSTM backbone:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht(i)=LSTM​(xt(i),ht−1(i)),i=1,…,d,h\_{t}^{(i)}=\mathrm{LSTM}(x\_{t}^{(i)},h\_{t-1}^{(i)}),\quad i=1,\dots,d, |  | (52) |

where xt(i)x\_{t}^{(i)} denotes the ii-th feature.

The resulting hidden states are segmented into temporal patches and passed to PatchTST, which applies self-attention over patches:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h~p=PatchTST​({ht(i)}t∈𝒫p),\tilde{h}\_{p}=\mathrm{PatchTST}(\{h\_{t}^{(i)}\}\_{t\in\mathcal{P}\_{p}}), |  | (53) |

where 𝒫p\mathcal{P}\_{p} denotes the set of time steps belonging to patch pp.

This separation of concerns allows the LSTM to stabilize local temporal structure while PatchTST aggregates medium- and long-range dependencies.

#### VSN + xLSTM

In the VSN + xLSTM hybrid, the sequence of VSN-selected representations is directly fed into an xLSTM. The model maintains a matrix-valued memory state Mt∈ℝH×HM\_{t}\in\mathbb{R}^{H\times H}, which is updated recursively:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Mt,st)=xLSTM​(x~t,Mt−1),(M\_{t},s\_{t})=\mathrm{xLSTM}(\tilde{x}\_{t},M\_{t-1}), |  | (54) |

where st∈ℝHs\_{t}\in\mathbb{R}^{H} denotes the output state.
The matrix-valued memory enables modeling of higher-order temporal interactions and long-range dependencies beyond the capacity of vector-based recurrent architectures.

### B.6 Temporal Fusion Transformer Details

TFT combines recurrent encoding with attention-based aggregation. Given an input sequence {xt}t=1L\{x\_{t}\}\_{t=1}^{L}, a recurrent encoder produces latent states

|  |  |  |
| --- | --- | --- |
|  | ht=LSTM​(xt,ht−1).h\_{t}=\mathrm{LSTM}(x\_{t},h\_{t-1}). |  |

Multi-head attention is then applied to aggregate information across time:

|  |  |  |
| --- | --- | --- |
|  | y^t=Attn​(h1:t).\hat{y}\_{t}=\mathrm{Attn}(h\_{1:t}). |  |

Variable selection networks, gating layers, and static covariate encoders further modulate the representations to improve interpretability and robustness.

## Appendix C Model Configurations and Hyperparameter Selection

To ensure a fair and systematic comparison across architectures, we define structured hyperparameter search spaces tailored to each model family. All models are evaluated under comparable training budgets, with architecture-specific parameters varied only where structurally relevant. Tables [6](#A3.T6 "Table 6 ‣ Model Capacity Considerations. ‣ Appendix C Model Configurations and Hyperparameter Selection ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") and [7](#A3.T7 "Table 7 ‣ Model Capacity Considerations. ‣ Appendix C Model Configurations and Hyperparameter Selection ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") summarizes the general configuration ranges.

#### General Training Configuration.

For each model, we tune the batch size, hidden dimensionality (HH), learning rate, and input sequence length. Learning rates are selected from logarithmic ranges between 10−410^{-4} and 10−210^{-2} or from discrete sets {10−3,5×10−4,10−4}\{10^{-3},5\times 10^{-4},10^{-4}\} depending on architectural stability. Sequence lengths are chosen to reflect short- and medium-horizon dependencies (e.g., 64–512 timesteps), while maintaining comparability across models.

#### Architecture-Specific Hyperparameters.

In addition to shared training parameters, each model family includes structural hyperparameters:

* •

  Transformer-based models (e.g., TFT, PatchTST) vary the number of attention heads, encoder layers, and sparsity factors.
* •

  State-space models (Mamba2 variants) tune the number of layers, convolution kernel size, SSM expansion factors, rank, and discretization parameters (e.g., Δmax\Delta\_{\max}, HiPPO scaling).
* •

  xLSTM-based models vary the number of stacked blocks, convolutional kernel sizes, and projection expansion factors.
* •

  Patch-based models additionally tune patch length and stride fraction.
* •

  Classical baselines (AR1, DLinear) are evaluated with minimal architectural tuning.

#### Search Protocol.

Hyperparameter selection is performed via grid search over the predefined discrete ranges. Each configuration is trained independently, and the best-performing setting is selected based on validation Sharpe Ratio. Importantly, the same validation procedure and performance metric are used for all architectures to avoid selection bias.

#### Training Details.

We employ the ADAM optimizer [[45](#bib.bib45)] for all models. Early stopping is applied with a patience of 20 epochs. For validation, the last 10% of the training data is reserved as a validation set. Gradient clipping based on the gradient norm is used to stabilize training.

Models are retrained every five years using a rolling-window scheme. For strategies requiring an initial lookback period, performance metrics such as the Sharpe ratio are not evaluated during the burn-in phase. In particular, for models with a fixed initialization window we use L0=21L\_{0}=21, while for sequence models the burn-in period corresponds to one quarter of the input sequence length (e.g., 21 for sequence length 84 and 128 for sequence length 512).

#### Model Capacity Considerations.

The number of trainable parameters varies substantially across models (Table [6](#A3.T6 "Table 6 ‣ Model Capacity Considerations. ‣ Appendix C Model Configurations and Hyperparameter Selection ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.")), reflecting inherent architectural differences. We do not explicitly match parameter counts, as doing so would distort the native design of certain architectures (e.g., state-space vs. attention-based models). Instead, we control for training protocol, optimization strategy, and evaluation metric to ensure comparability.

This structured configuration framework ensures that performance differences arise from architectural properties rather than inconsistent tuning practices.

Table 6: Model configurations and general hyperparameter search ranges.

Model
Trainable Params
Batch Size
Hidden Dim (H)
LR Range
Seq Len
Dropout


Mamba2+VSN
3,571,348
{32,64,128}
{32,64,128,256}
10−410^{-4}–10−210^{-2}
84
{0.1,0.2,0.3,0.4}

xLSTM
2,507,269
{128,256}
{64,128,256}
{1e-3,5e-4,1e-4}
84
{0.2,0.3,0.4,0.5}

xLSTM+VSN
6,146,368
{128,256}
{64,128,256}
{1e-3,5e-4,1e-4}
84
{0.2,0.3,0.4,0.5}

PsLSTM
1,963,841
{16,32}
{16,32,64}
{1e-3,5e-4,1e-4}
512
{0.2,0.3,0.4,0.5}

VLSTM
1,142,963
{128,256}
{64,128,256}
10−410^{-4}–10−210^{-2}
84
{0.2,0.3,0.4,0.5}

LSTM
73,729
{128,256}
{64,128,256}
10−410^{-4}–10−210^{-2}
84
{0.2,0.3,0.4,0.5}

PatchTST
1,139,739
{16,32}
{16,32,64,96}
{1e-3,5e-4}
512
{0.1,0.2,0.3,0.4,0.5}

LSTM+PatchTST
634,881
{16,32}
{16,32,64,96}
{1e-3,5e-4}
512
{0.1,0.2,0.3,0.4,0.5}

Mamba2
18,882
{32,64,128}
{32,64,128,256}
10−410^{-4}–10−210^{-2}
84
{0.1,0.2,0.3,0.4}

DLinear
2,111
{256,512,1024}
{64,128,256}
10−410^{-4}–10−210^{-2}
64
{0.1,0.2,0.3}

AR1
2,073
{128,256}
{64,128,256}
10−410^{-4}–10−210^{-2}
84
{0.2,0.3,0.4,0.5}

TFT
347,507
{128,256}
{64,128,256}
10−410^{-4}–10−210^{-2}
84
{0.2,0.3,0.4,0.5}




Table 7: Architecture-specific hyperparameter search spaces.

Architecture
Hyperparameter Search Space


Transformer-based
Heads: {1,2,4}; Layers: {3,4,5,6}; Sparsity: {2,3,4,5,6}

Mamba / SSM
Layers: {1,2,3,5}; Kernel: {2,3,5,7,9}; Conv: {2,8,16,32}


Rank: {4,8,16,32}; Δmax\Delta\_{\max}: {0.2,0.4,0.6,0.8}; HiPPO: 0.1–0.5

xLSTM
Blocks: {1–6}; Kernel: {1,2,4,6,7,9}; Projection: {1–2.5}

Patch-based
Patch Length: {4,8,16,32,64}; Stride: {0.25,0.5,1}

Classical (AR1, DLinear)
Layers: {2,3,5}

## Appendix D Performance Metrics and Evaluation Criteria

This appendix describes the performance, risk, and robustness measures used throughout the empirical evaluation. Given the low signal-to-noise ratio and heavy-tailed nature of financial returns, we rely on a broad set of complementary metrics to assess not only average performance, but also statistical significance, downside risk, trading intensity, and incremental value relative to a passive benchmark.

### D.1 Return and Risk-Adjusted Performance

#### Annualized Return.

Annualized return is computed as the mean daily portfolio return scaled by the number of trading days per year. While intuitive, this metric does not account for risk and is therefore interpreted jointly with risk-adjusted measures.

#### Compound Annual Growth Rate (CAGR).

CAGR measures the geometric average annual growth of portfolio value over the evaluation period:

|  |  |  |
| --- | --- | --- |
|  | CAGR=(VTV0)1/T−1,\text{CAGR}=\left(\frac{V\_{T}}{V\_{0}}\right)^{1/T}-1, |  |

where V0V\_{0} and VTV\_{T} denote initial and terminal portfolio values and TT is the length of the sample in years. CAGR reflects long-run capital accumulation and penalizes volatility drag.

#### Sharpe Ratio.

The Sharpe ratio is defined as the mean excess return divided by the standard deviation of returns. All reported Sharpe ratios are annualized. This is the primary optimization objective and headline performance metric throughout the study.

#### Information Ratio.

The Information Ratio measures risk-adjusted excess performance relative to a passive buy-and-hold benchmark:

|  |  |  |
| --- | --- | --- |
|  | IR=𝔼^​[rt−rtpassive]Var^​(rt−rtpassive).\text{IR}=\frac{\hat{\mathbb{E}}[r\_{t}-r\_{t}^{\text{passive}}]}{\sqrt{\hat{\text{Var}}(r\_{t}-r\_{t}^{\text{passive}})}}. |  |

This metric captures incremental value beyond market exposure.

### D.2 Statistical Significance

#### HAC-Adjusted tt-Statistics.

To assess statistical significance under serial correlation and heteroskedasticity, we report Newey–West heteroskedasticity and autocorrelation consistent (HAC) tt-statistics for mean returns and Sharpe ratios. This adjustment is critical in financial time series, where returns often exhibit time dependence.

#### HAC tt-Statistic versus Passive.

We additionally report HAC-adjusted tt-statistics for excess returns relative to the passive benchmark, testing whether observed outperformance is statistically distinguishable from zero after accounting for dependence in relative returns.

### D.3 Directional Accuracy and Trading Activity

#### Hit Rate.

The hit rate measures the fraction of periods in which the strategy correctly predicts the sign of returns. While not sufficient for profitability on its own, it provides insight into directional consistency.

#### Turnover.

Turnover is defined as the average absolute change in portfolio weights across consecutive periods. High turnover implies greater transaction costs and reduced implementability.

#### Turnover (xGMV).

Turnover expressed as a multiple of gross market value (xGMV) provides a scale-free measure of trading intensity and facilitates comparison across strategies.

### D.4 Downside Risk and Tail Behavior

#### Maximum Drawdown.

Maximum drawdown is the largest peak-to-trough decline in cumulative portfolio value. It captures worst-case capital loss and is a key risk metric for real-world deployment.

#### Calmar Ratio.

The Calmar ratio is defined as CAGR divided by maximum drawdown. It measures return efficiency relative to extreme downside risk and complements the Sharpe ratio.

#### Conditional Value-at-Risk (CVaR 5%).

CVaR at the 5% level measures the expected loss conditional on returns falling in the worst 5% of outcomes. Unlike Value-at-Risk, CVaR captures tail severity and is particularly relevant in heavy-tailed financial return distributions.

### D.5 Benchmark-Relative Diagnostics

#### Correlation versus Passive.

We report the Pearson correlation between strategy returns and the passive benchmark. Lower correlation indicates greater diversification benefits and reduced dependence on market direction.

#### Profit and Loss (PnL).

Cumulative profit and loss (PnL) curves are used for visual comparison of strategies over time. PnL trajectories provide insight into path dependence, drawdown behavior, and regime sensitivity that may not be evident from summary statistics alone.

Taken together, these metrics provide a comprehensive and economically meaningful assessment of model performance, balancing average returns, statistical reliability, downside risk, trading realism, and incremental value over a passive investment strategy.

## Appendix E Asset-level Results

This section provides a detailed breakdown of model performance at the individual asset level. The per-asset analysis presented here serves two purposes: (i) to evaluate cross-sectional robustness and (ii) to assess whether performance is concentrated in specific asset classes or broadly distributed across markets.

We use breakeven transaction cost, which is defined as the constant cost per unit of leveraged turnover that drives total gross PnL to zero. Formally,

|  |  |  |
| --- | --- | --- |
|  | c∗=∑tRtgross∑tτt,c^{\*}=\frac{\sum\_{t}R^{\text{gross}}\_{t}}{\sum\_{t}\tau\_{t}}, |  |

where τt\tau\_{t} denotes leveraged turnover. If actual trading costs remain below c∗c^{\*}, the strategy remains profitable; the ratio c∗/cactualc^{\*}/c\_{\text{actual}} measures implementation robustness.

Results are grouped by asset category (Bond, Commodity, Energy, FX, and Index futures). For each model, we report cumulative PnL trajectories per asset as well as box-and-whisker summaries of the Sharpe Ratio distributions. This allows us to examine both temporal consistency and cross-sectional dispersion.

### E.1 Asset Description

Table [8](#A5.T8 "Table 8 ‣ E.1 Asset Description ‣ Appendix E Asset-level Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") reports the full universe of tradable assets included in the empirical analysis. The cross-asset dataset spans foreign exchange, equity indices, fixed income, energy, and agricultural and metal commodities, including both pit and electronic contracts where available. This broad coverage ensures substantial cross-sectional and cross-asset heterogeneity, enabling the evaluation of model robustness across diverse liquidity conditions, macroeconomic exposures, and volatility regimes.

Table 8: Asset universe and classification.

| Ticker | Group | Description | Ticker | Group | Description | Ticker | Group | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AN | FX | Australian dollar comp | BC | Energy | Brent crude oil | BG | Energy | Brent gasoil |
| BN | FX | British pound comp | CA | Index | CAC 40 index | CADJPY | FX | CAD JPY cross |
| CB | Bond | Canada 10Y bond | CC | Comdty | Cocoa | CN | FX | Canadian dollar comp |
| CR | Comdty | CRB index | CT | Comdty | Cotton No.2 | DA | Comdty | Milk III |
| DT | Bond | Euro Bund | DX | FX | US dollar index | EN | Index | Nasdaq mini |
| ER | Index | Russell 2000 mini | ES | Index | S&P 500 mini | FB | Bond | US 5Y note comp |
| FN | Index | Euro Stoxx comp | GI | Comdty | Goldman Sachs idx | GS | Bond | UK Gilt long |
| HS | Index | Hang Seng | JN | FX | Japanese yen comp | JO | Comdty | Orange juice |
| KC | Comdty | Coffee | KW | Comdty | Wheat KC | LB | Comdty | Lumber |
| LX | Index | FTSE 100 | MD | Index | S&P 400 mini | MP | FX | Mexican peso |
| MW | Comdty | Wheat Minneapolis | NK | Index | Nikkei 225 | NOKUSD | FX | NOK USD cross |
| NR | Comdty | Rough rice | SB | Comdty | Sugar No.11 | SN | FX | Swiss franc comp |
| TU | Bond | US 2Y note comp | TY | Bond | US 10Y note comp | UB | Bond | Euro Bobl |
| US | Bond | US T-bond comp | USDNZD | FX | USD NZD cross | USDSEK | FX | USD SEK cross |
| USDSGD | FX | USD SGD cross | UZ | Bond | Euro Schatz | XU | Index | Euro Stoxx 50 |
| XX | Index | STOXX 50 | YM | Index | Mini Dow | ZA | Comdty | Palladium elec |
| ZB | Energy | RBOB elec | ZC | Comdty | Corn elec | ZF | Comdty | Feeder cattle elec |
| ZG | Comdty | Gold elec | ZI | Comdty | Silver elec | ZK | Comdty | Copper elec |
| ZL | Comdty | Soybean oil elec | ZM | Comdty | Soybean meal elec | ZN | Energy | Natural gas elec |
| ZO | Comdty | Oats elec | ZP | Comdty | Platinum elec | ZR | Comdty | Rough rice elec |
| ZS | Comdty | Soybeans elec | ZT | Comdty | Live cattle elec | ZU | Energy | Crude oil elec |
| ZW | Comdty | Wheat elec | ZZ | Comdty | Lean hogs elec |  |  |  |

### E.2 VSLTM

Figures [8](#A5.F8 "Figure 8 ‣ E.2 VSLTM ‣ Appendix E Asset-level Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.")–[12](#A5.F12 "Figure 12 ‣ E.2 VSLTM ‣ Appendix E Asset-level Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") display cumulative PnL per asset across the five asset categories. The corresponding box-and-whisker plots (Figures [13](#A5.F13 "Figure 13 ‣ E.2 VSLTM ‣ Appendix E Asset-level Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.")–[17](#A5.F17 "Figure 17 ‣ E.2 VSLTM ‣ Appendix E Asset-level Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.")) summarize the distribution of Sharpe Ratio for each instrument.

Several observations emerge. First, performance is not driven by a single dominant contract but is distributed across multiple assets within each category. Second, tail behavior, as captured in the box plots, suggests that risk-adjusted performance is primarily driven by stable median returns rather than isolated extreme gains.

Overall, the per-asset analysis indicates that VLSTM’s aggregate performance is supported by consistent cross-sectional contributions rather than concentration in a small subset of instruments.

![Refer to caption](2603.01820v1/Images/vlstm_per_asset_bond.png)


Figure 8: VLSTM PnL per asset - bond Futures

![Refer to caption](2603.01820v1/Images/vlstm_per_asset_cmdty.png)


Figure 9: VLSTM PnL per asset - Commodities Futures

![Refer to caption](2603.01820v1/Images/vlstm_per_asset_index.png)


Figure 10: VLSTM PnL per asset - Index Futures

![Refer to caption](2603.01820v1/Images/vlstm_per_asset_energy.png)


Figure 11: VLSTM PnL per asset - Energy Futures

![Refer to caption](2603.01820v1/Images/vlstm_per_asset_fx.png)


Figure 12: VLSTM PnL per asset - FX Futures

![Refer to caption](2603.01820v1/Images/vlstm_per_asset_box_bond.png)


Figure 13: VLSTM box and whisker annual Sharpe Ratio per asset - Bond Futures

![Refer to caption](2603.01820v1/Images/vlstm_per_asset_box_cmdty.png)


Figure 14: VLSTM box and whisker annual Sharpe Ratio per asset - Commodities Futures

![Refer to caption](2603.01820v1/Images/vlstm_per_asset_box_index.png)


Figure 15: VLSTM box and whisker annual Sharpe Ratio per asset - Index Futures

![Refer to caption](2603.01820v1/Images/vlstm_per_asset_box_energy.png)


Figure 16: VLSTM box and whisker annual Sharpe Ratio per asset - Energy Futures

![Refer to caption](2603.01820v1/Images/vlstm_per_asset_box_fx.png)


Figure 17: VLSTM box and whisker annual Sharpe Ratio per asset - FX Futures




Table 9: VLSTM: Annualised Volatility-Rescaled Performance and Breakeven Transaction Costs (bps)

| Ticker | Gross (ann.) | Turnover (ann.) | c∗c^{\*} (bps) | Ticker | Gross (ann.) | Turnover (ann.) | c∗c^{\*} (bps) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LB | 0.2485 | 80.58 | 30.84 | ZO | 0.2027 | 84.01 | 24.13 |
| DA | 0.2529 | 114.78 | 22.04 | ZN | 0.0618 | 45.04 | 13.73 |
| JO | 0.0986 | 74.19 | 13.29 | EN | 0.1003 | 86.69 | 11.57 |
| KC | 0.0738 | 63.92 | 11.54 | ZR | 0.1339 | 137.44 | 9.75 |
| BC | 0.0512 | 61.26 | 8.36 | ZF | 0.1279 | 157.12 | 8.14 |
| NR | 0.1086 | 137.78 | 7.88 | NK | 0.0706 | 89.77 | 7.87 |
| ES | 0.0796 | 107.12 | 7.43 | KW | 0.0686 | 93.77 | 7.32 |
| ZL | 0.0827 | 115.79 | 7.15 | ZA | 0.0558 | 82.87 | 6.74 |
| ZI | 0.0444 | 68.93 | 6.44 | ZU | 0.0381 | 64.42 | 5.91 |
| ZS | 0.0476 | 83.69 | 5.68 | MW | 0.0669 | 127.30 | 5.25 |
| XU | 0.0507 | 98.17 | 5.17 | XX | 0.0614 | 118.76 | 5.17 |
| ZK | 0.0421 | 83.07 | 5.06 | CT | 0.0421 | 91.73 | 4.59 |
| ZW | 0.0417 | 91.08 | 4.57 | SB | 0.0313 | 80.33 | 3.89 |
| MD | 0.0442 | 115.53 | 3.82 | HS | 0.0301 | 85.51 | 3.52 |
| ZC | 0.0363 | 103.71 | 3.50 | ZT | 0.0464 | 135.72 | 3.42 |
| ER | 0.0264 | 80.13 | 3.30 | CA | 0.0267 | 92.21 | 2.90 |
| CR | 0.0389 | 138.25 | 2.82 | BG | 0.0216 | 78.91 | 2.73 |
| DT | 0.0782 | 291.86 | 2.68 | MP | 0.0368 | 143.21 | 2.57 |
| ZM | 0.0215 | 83.55 | 2.57 | GI | 0.0230 | 94.01 | 2.44 |
| ZB | 0.0160 | 66.47 | 2.41 | NOKUSD | 0.0382 | 165.09 | 2.31 |
| USDSEK | 0.0419 | 188.00 | 2.23 | GS | 0.0547 | 282.39 | 1.94 |
| JN | 0.0321 | 209.92 | 1.53 | ZG | 0.0177 | 119.59 | 1.48 |
| CC | 0.0115 | 78.16 | 1.47 | USDNZD | 0.0209 | 169.47 | 1.23 |
| USDSGD | 0.0422 | 368.09 | 1.15 | UB | 0.0664 | 591.04 | 1.12 |
| ZP | 0.0110 | 101.90 | 1.08 | TY | 0.0415 | 411.13 | 1.01 |
| DX | 0.0284 | 298.04 | 0.95 | LX | 0.0101 | 109.94 | 0.91 |
| YM | 0.0085 | 106.28 | 0.80 | CN | 0.0199 | 272.83 | 0.73 |
| CB | 0.0194 | 344.26 | 0.56 | FN | 0.0130 | 233.13 | 0.56 |
| CADJPY | 0.0080 | 151.64 | 0.53 | US | 0.0104 | 198.09 | 0.52 |
| FB | 0.0281 | 689.19 | 0.41 | UZ | 0.0508 | 1940.20 | 0.26 |
| TU | 0.0094 | 2218.65 | 0.04 | ZZ | -0.0004 | 80.57 | -0.05 |
| BN | -0.0092 | 207.76 | -0.44 | AN | -0.0170 | 164.71 | -1.03 |
| SN | -0.0272 | 212.34 | -1.28 |  |  |  |  |

### E.3 xLSTM

Figures [18](#A5.F18 "Figure 18 ‣ E.3 xLSTM ‣ Appendix E Asset-level Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.")–[22](#A5.F22 "Figure 22 ‣ E.3 xLSTM ‣ Appendix E Asset-level Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") present cumulative PnL per asset for xLSTM across the five asset groups. The associated box-and-whisker plots (Figures [23](#A5.F23 "Figure 23 ‣ E.3 xLSTM ‣ Appendix E Asset-level Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.")–[27](#A5.F27 "Figure 27 ‣ E.3 xLSTM ‣ Appendix E Asset-level Results ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.")) provide distributional summaries.

Relative to VLSTM, xLSTM exhibits stronger cross-sectional homogeneity in certain categories. In higher-volatility sectors such as energy and commodities, dispersion increases, but median performance remains positive across most instruments. This suggests that the model adapts to heterogeneous volatility structures without excessive tail risk concentration.

Importantly, no systematic degradation is observed in a specific asset class, indicating that performance is not regime- or sector-dependent. The cross-asset consistency observed in the box plots further supports the robustness of the learned representations.

![Refer to caption](2603.01820v1/Images/xlstm_per_asset_bond.png)


Figure 18: xLSTM PnL per asset - bond Futures

![Refer to caption](2603.01820v1/Images/xlstm_per_asset_cmdty.png)


Figure 19: xLSTM PnL per asset - Commodities Futures

![Refer to caption](2603.01820v1/Images/xlstm_per_asset_index.png)


Figure 20: xLSTM PnL per asset - Index Futures

![Refer to caption](2603.01820v1/Images/xlstm_per_asset_energy.png)


Figure 21: xLSTM PnL per asset - Energy Futures

![Refer to caption](2603.01820v1/Images/xlstm_per_asset_fx.png)


Figure 22: xLSTM PnL per asset - FX Futures

![Refer to caption](2603.01820v1/Images/xlstm_per_asset_box_bond.png)


Figure 23: xLSTM box and whisker annual Sharpe Ratio per asset - Bond Futures

![Refer to caption](2603.01820v1/Images/xlstm_per_asset_box_cmdty.png)


Figure 24: xLSTM box and whisker annual Sharpe Ratio per asset - Commodities Futures

![Refer to caption](2603.01820v1/Images/xlstm_per_asset_box_index.png)


Figure 25: xLSTM box and whisker annual Sharpe Ratio per asset - Index Futures

![Refer to caption](2603.01820v1/Images/xlstm_per_asset_box_energy.png)


Figure 26: xLSTM box and whisker annual Sharpe Ratio per asset - Energy Futures

![Refer to caption](2603.01820v1/Images/xlstm_per_asset_box_fx.png)


Figure 27: xLSTM box and whisker annual Sharpe Ratio per asset - FX Futures




Table 10: xLSTM: Annualised Volatility-Rescaled Performance and Breakeven Transaction Costs (bps)

| Ticker | Gross (ann.) | Turnover (ann.) | c∗c^{\*} (bps) | Ticker | Gross (ann.) | Turnover (ann.) | c∗c^{\*} (bps) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LB | 0.2338 | 68.93 | 33.92 | DA | 0.2200 | 83.29 | 26.41 |
| ZO | 0.2157 | 98.88 | 21.81 | ES | 0.0501 | 26.01 | 19.25 |
| ZN | 0.0544 | 29.02 | 18.76 | CC | 0.0419 | 24.23 | 17.31 |
| EN | 0.0572 | 38.19 | 14.97 | JO | 0.1375 | 96.18 | 14.30 |
| ZR | 0.1818 | 132.86 | 13.68 | NR | 0.1489 | 135.22 | 11.01 |
| LX | 0.0430 | 40.14 | 10.72 | BG | 0.0443 | 51.13 | 8.66 |
| ZM | 0.0279 | 32.54 | 8.57 | KW | 0.0587 | 75.50 | 7.77 |
| YM | 0.0409 | 55.80 | 7.33 | MW | 0.0824 | 116.51 | 7.07 |
| ZT | 0.0919 | 131.96 | 6.96 | MP | 0.0419 | 61.25 | 6.83 |
| DT | 0.0501 | 79.15 | 6.33 | ZA | 0.0437 | 76.56 | 5.71 |
| ZW | 0.0415 | 84.22 | 4.93 | ZC | 0.0471 | 101.33 | 4.65 |
| MD | 0.0325 | 71.83 | 4.53 | JN | 0.0336 | 74.70 | 4.50 |
| ZZ | 0.0167 | 42.08 | 3.96 | ZF | 0.0580 | 161.56 | 3.59 |
| ZI | 0.0211 | 60.24 | 3.50 | ZS | 0.0121 | 38.73 | 3.12 |
| ER | 0.0163 | 52.64 | 3.09 | USDSEK | 0.0286 | 100.11 | 2.85 |
| ZL | 0.0314 | 118.88 | 2.64 | ZB | 0.0107 | 41.06 | 2.62 |
| XU | 0.0385 | 151.47 | 2.54 | UB | 0.0305 | 176.77 | 1.72 |
| XX | 0.0192 | 178.70 | 1.07 | CB | 0.0177 | 217.61 | 0.81 |
| GS | 0.0133 | 223.73 | 0.60 | NK | 0.0055 | 145.81 | 0.38 |
| ZU | 0.0011 | 38.32 | 0.29 | ZK | 0.0032 | 115.80 | 0.28 |
| UZ | 0.0145 | 584.56 | 0.25 | FB | 0.0087 | 441.46 | 0.20 |
| TU | 0.0205 | 1121.50 | 0.18 | TY | 0.0034 | 219.72 | 0.16 |
| USDSGD | 0.0010 | 208.81 | 0.05 | NOKUSD | -0.0028 | 102.23 | -0.27 |
| CN | -0.0106 | 193.52 | -0.55 | US | -0.0086 | 101.15 | -0.85 |
| CADJPY | -0.0144 | 166.63 | -0.86 | GI | -0.0072 | 54.74 | -1.31 |
| DX | -0.0359 | 270.55 | -1.33 | BN | -0.0143 | 95.74 | -1.49 |
| CA | -0.0167 | 110.31 | -1.52 | SB | -0.0084 | 41.65 | -2.01 |
| HS | -0.0103 | 45.01 | -2.30 | FN | -0.0193 | 77.30 | -2.50 |
| AN | -0.0371 | 131.94 | -2.81 | ZP | -0.0301 | 100.81 | -2.99 |
| ZG | -0.0190 | 63.04 | -3.02 | USDNZD | -0.0386 | 92.40 | -4.17 |
| CT | -0.0397 | 92.56 | -4.29 | KC | -0.0218 | 43.61 | -4.99 |
| SN | -0.0737 | 125.71 | -5.86 | BC | -0.0126 | 19.67 | -6.40 |

#### Cross-Sectional Robustness.

Taken together, the complementary results reinforce the conclusions drawn in the main text. Aggregate Sharpe ratios are not driven by isolated outliers but reflect broadly distributed performance across asset classes. Differences between models are manifested not only in overall portfolio metrics but also in dispersion characteristics and category-level stability.

This granular evaluation is particularly relevant in financial forecasting, where apparent portfolio-level improvements may otherwise mask instability or concentration risk at the instrument level.

## Appendix F Annual Sharpe Ratio

Table [11](#A6.T11 "Table 11 ‣ Appendix F Annual Sharpe Ratio ‣ Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance1footnote 11footnote 1Code is available upon request.") reports annual out-of-sample Sharpe ratios for all benchmark strategies over the period 2010–2024. The year-by-year decomposition complements the aggregated results in the main text by providing a finer assessment of temporal stability and regime dependence. Several patterns emerge. First, performance is not concentrated in a single favorable subperiod: the leading deep sequence models exhibit consistently positive Sharpe ratios across a broad range of market environments, including the post-crisis recovery, the low-volatility mid-2010s expansion, and the high-uncertainty period following 2020. Second, while cross-sectional performance rankings vary from year to year—as expected given structural shifts in volatility and cross-asset correlations—the top-performing architectures remain competitive in most years and avoid persistent underperformance. Third, classical linear benchmarks display greater sensitivity to adverse regimes, with more frequent negative annual Sharpe ratios. Overall, the annual breakdown confirms that the superior aggregated performance documented in the main text is not driven by isolated episodes, but rather reflects sustained risk-adjusted returns across heterogeneous market conditions.

Table 11: Annual Sharpe Ratios by Strategy (2010–2024)

| Strategy | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AR1x | 1.45 | -0.07 | -0.11 | 0.23 | 2.97 | -0.02 | 0.05 | 0.67 | -0.59 | 0.18 | 3.02 | 0.63 | 1.37 | 1.45 | 0.30 |
| ARnnx | 1.60 | 0.06 | -0.25 | 0.06 | 2.51 | 0.22 | -0.17 | 0.30 | -0.90 | 0.48 | 2.07 | 0.90 | 1.64 | 1.11 | -0.16 |
| DLinear | 1.21 | -0.11 | -0.43 | -0.29 | 2.89 | 0.33 | -0.19 | 0.42 | -0.28 | -0.27 | 3.22 | 0.35 | 1.45 | 2.30 | -0.94 |
| LSTM | 3.58 | 0.29 | 2.47 | 0.74 | 1.81 | 2.09 | 2.19 | -1.19 | 1.72 | 3.20 | -1.51 | 1.12 | 3.44 | 1.22 | 1.06 |
| VLSTM | 3.96 | 1.48 | 3.92 | 1.13 | 3.03 | 1.90 | 4.03 | 1.06 | 1.33 | 4.74 | 0.10 | 2.81 | 3.82 | 2.76 | -0.10 |
| Mamba2 | 0.88 | -0.38 | -0.71 | 0.07 | 3.22 | 0.18 | 0.15 | 0.68 | -0.05 | 0.00 | 3.15 | 1.33 | 2.27 | 1.43 | -0.49 |
| VSN+Mamba2 | 1.48 | 0.27 | -0.12 | -0.00 | 3.43 | 0.65 | 0.54 | 1.31 | -0.05 | 0.23 | 3.31 | 1.92 | 2.64 | 1.45 | -0.63 |
| PatchTST | 2.69 | 0.48 | 0.61 | -1.21 | 0.72 | 0.24 | 0.13 | -0.13 | 1.14 | 1.49 | 1.20 | 1.98 | 0.85 | 0.54 | 0.59 |
| LPatchTST | 3.90 | 1.50 | 3.04 | 0.51 | 3.40 | 1.60 | 1.72 | 2.39 | 1.55 | 3.26 | 1.13 | 3.46 | 3.24 | 2.57 | 1.31 |
| PsLSTM | 2.71 | 1.38 | 1.92 | -0.40 | 2.89 | 1.09 | 1.92 | 1.87 | 1.39 | 2.92 | 1.69 | 3.04 | 1.74 | 2.29 | -0.35 |
| TFT | 3.97 | 1.21 | 3.90 | 1.19 | 3.04 | 1.50 | 3.18 | 1.05 | 1.32 | 3.36 | -0.14 | 2.62 | 4.28 | 3.25 | 0.37 |
| VxLSTM | 2.73 | 1.34 | 1.71 | 0.22 | 3.25 | 0.11 | 1.92 | 2.82 | 0.60 | 1.95 | 3.77 | 2.24 | 2.13 | 1.88 | -1.31 |
| xLSTM | 2.64 | 1.41 | 1.72 | -0.28 | 2.91 | 0.34 | 2.29 | 2.96 | 0.46 | 2.38 | 3.83 | 2.62 | 1.55 | 1.96 | 0.02 |
| iTransformer | 1.30 | 0.20 | -1.14 | 0.19 | 2.34 | 0.70 | -0.07 | 0.65 | -1.16 | 0.21 | 1.43 | 0.95 | -1.03 | 0.68 | 0.46 |
| Mamba | 0.82 | -0.27 | -0.46 | -0.48 | 3.03 | 0.41 | 0.07 | 0.04 | -0.17 | -0.40 | 1.29 | 1.00 | -0.54 | 1.47 | -0.40 |
| NLinear | 1.18 | 0.38 | -1.20 | 0.18 | 2.60 | 0.44 | -0.22 | 0.96 | -1.12 | 0.63 | 3.02 | 0.60 | 0.09 | 1.35 | 1.07 |

BETA