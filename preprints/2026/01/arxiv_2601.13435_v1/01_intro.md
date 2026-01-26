---
authors:
- Shuozhe Li
- Du Cheng
- Leqi Liu
doc_id: arxiv:2601.13435v1
family_id: arxiv:2601.13435
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted
  Return Optimization
url_abs: http://arxiv.org/abs/2601.13435v1
url_html: https://arxiv.org/html/2601.13435v1
venue: arXiv q-fin
version: 1
year: 2026
---


Shuozhe Li∗, Du Cheng∗, and Leqi Liu
Shuozhe Li and Du Cheng contribute equally to this work.Shuozhe Li is with the Computer Science Department, University of Texas, Austin, TX 78712 USA (e-mail: shuozhe.li@utexas.edu).Du Cheng is with the College of Information Science and Engineering, Northeastern University, Shenyang 110819, China (e-mail: v6hit7cd@gmail.com).Leqi Liu is with the Information, Risk and Operations Management Department and is affiliated with the Computer Science Department, University of Texas, Austin, TX 78712 USA (e-mail: leqiliu@utexas.edu).

###### Abstract

Learning profitable intraday trading policies from financial time series is challenging due to heavy noise, non-stationarity, and strong cross-sectional dependence among related assets. We propose *WaveLSFormer*, a learnable wavelet-based long-short Transformer that jointly performs multi-scale decomposition and return-oriented decision learning. Specifically, a learnable wavelet front-end generates low-/high-frequency components via an end-to-end trained filter bank, guided by spectral regularizers that encourage stable and well-separated frequency bands. To fuse multi-scale information, we introduce a low-guided high-frequency injection (LGHI) module that refines low-frequency representations with high-frequency cues while controlling training stability. The model outputs a portfolio of long/short positions that is rescaled to satisfy a fixed risk budget, and is optimized directly with a trading objective and risk-aware regularization. Extensive experiments on five years of hourly data across six industry groups, evaluated over ten random seeds, demonstrate that WaveLSFormer consistently outperforms MLP, LSTM and Transformer backbones, with and without fixed discrete wavelet front-ends. On average in all industries, WaveLSFormer achieves a cumulative overall strategy return of 0.607±0.0450.607\pm 0.045 and a Sharpe ratio of 2.157±0.1662.157\pm 0.166, substantially improving both profitability and risk-adjusted returns over the strongest baselines.

## I Introduction

Financial economists have long debated whether asset prices fully reflect all available information.
The Efficient Market Hypothesis (EMH) suggests that, under rational expectations and frictionless markets, risk-adjusted excess returns should be unpredictable [[1](https://arxiv.org/html/2601.13435v1#bib.bib1)].
Nevertheless, decades of empirical evidence indicate that certain technical rules and cross-sectional patterns can yield economically meaningful profits in practice [[2](https://arxiv.org/html/2601.13435v1#bib.bib2)].
These observations motivate systematic methods for extracting tradable signals from historical prices and related market features.

With modern computing and large historical datasets, deep learning has become a central tool for modeling complex dependencies in financial time series.
A wide range of architectures, from deep feed-forward networks to recurrent models, have been explored for stock prediction and trading [[3](https://arxiv.org/html/2601.13435v1#bib.bib3), [4](https://arxiv.org/html/2601.13435v1#bib.bib4), [5](https://arxiv.org/html/2601.13435v1#bib.bib5), [6](https://arxiv.org/html/2601.13435v1#bib.bib6)].
Despite promising results, a key challenge remains: many pipelines are formulated as *forecasting* problems optimized by point-wise prediction losses, whereas real trading performance is determined by sequential *position decisions* and their accumulated P&L over time.
This objective mismatch can produce models that appear strong under regression/classification metrics yet fail to deliver robust out-of-sample strategy returns, especially when signals are weak and regimes shift.

Financial time series further complicate end-to-end learning.
Returns are noisy, heavy-tailed, and heteroskedastic, and exploitable structure may only be visible at certain temporal scales.
Moreover, assets within the same market segment are not independent: co-movements and lead-lag effects are prevalent, so effective decisions often require jointly modeling a group of related assets rather than treating each series in isolation [[4](https://arxiv.org/html/2601.13435v1#bib.bib4), [6](https://arxiv.org/html/2601.13435v1#bib.bib6)].
These characteristics motivate models that can extract stable multi-scale representations while aligning training with trading-oriented objectives.

Wavelet transforms are a natural candidate for multi-scale analysis because they provide a time-frequency decomposition that separates slow-moving trends from transient fluctuations.
Prior studies often apply fixed discrete wavelet transforms as preprocessing before downstream predictors [[7](https://arxiv.org/html/2601.13435v1#bib.bib7), [8](https://arxiv.org/html/2601.13435v1#bib.bib8), [9](https://arxiv.org/html/2601.13435v1#bib.bib9), [10](https://arxiv.org/html/2601.13435v1#bib.bib10)], and wavelet-integrated deep architectures have been surveyed more broadly [[11](https://arxiv.org/html/2601.13435v1#bib.bib11)].
In parallel, Transformers have gained popularity for time-series modeling, and wavelet-Transformer hybrids have been proposed to enhance forecasting by combining multi-scale decomposition with attention [[12](https://arxiv.org/html/2601.13435v1#bib.bib12), [13](https://arxiv.org/html/2601.13435v1#bib.bib13), [14](https://arxiv.org/html/2601.13435v1#bib.bib14)].
However, for trading, two limitations are particularly relevant: many hybrids still rely on *fixed* wavelets and emphasize forecasting accuracy rather than trading performance, and cross-frequency interactions are often handled implicitly without explicitly controlling how high-frequency information should refine low-frequency representations for stable decision learning.

To address these gaps, we propose *WaveLSFormer*, a trading policy model that outputs long/short positions for a group of related assets and is trained end-to-end with a trading-aware objective.
WaveLSFormer couples a *learnable* wavelet front-end with a Transformer backbone: the wavelet module is optimized jointly with the downstream objective to learn task-adaptive frequency bands, and we introduce a gated cross-frequency injection mechanism that injects high-frequency cues into the low-frequency branch aiming to filter the noise.
We further apply a risk-budget rescaling step so that the predicted positions satisfy a fixed risk budget, making the learning target closer to practical portfolio construction.
Our main contributions are as follows:

1. 1)

   We introduce *WaveLSFormer*, which replaces fixed wavelet preprocessing with an end-to-end learnable wavelet filter bank,
   coupled with a Transformer backbone for intraday long/short trading.
2. 2)

   We propose a stable cross-frequency fusion strategy via low-guided high-frequency injection with gated residual control,
   and integrate risk-budget rescaling to produce practical long/short positions.
3. 3)

   We conduct extensive experiments on five years of hourly U.S. equity data across multiple industries, and show that WaveLSFormer improves the overall ROI from 0.225±0.0560.225\pm 0.056 to 0.607±0.0450.607\pm 0.045 and Sharpe from 1.024±0.1221.024\pm 0.122 to 2.157±0.1662.157\pm 0.166, while also improving over the best wavelet-enhanced LSTM from 0.317±0.0500.317\pm 0.050 to 0.607±0.0450.607\pm 0.045 in ROI and from 1.879±0.1581.879\pm 0.158 to 2.157±0.1662.157\pm 0.166 in Sharpe.

## II Related work

### II-A Forecasting Models and Trading Objectives

Deep learning has been widely adopted for financial time series due to its ability to capture nonlinear dynamics, regime shifts, and complex temporal dependencies. Representative applications include CNN/LSTM-style predictors for stock forecasting [[15](https://arxiv.org/html/2601.13435v1#bib.bib15), [16](https://arxiv.org/html/2601.13435v1#bib.bib16), [17](https://arxiv.org/html/2601.13435v1#bib.bib17), [18](https://arxiv.org/html/2601.13435v1#bib.bib18), [19](https://arxiv.org/html/2601.13435v1#bib.bib19)].
However, a recurring challenge is the objective mismatch between training and deployment. Many methods optimize point-wise forecast losses like MSE or MAE, while trading performance depends on sequential position decisions, constraints, and risk exposure. As a result, sequence predictors do not necessarily intend to achieve robust strategies [[20](https://arxiv.org/html/2601.13435v1#bib.bib20)].
Transformers [[21](https://arxiv.org/html/2601.13435v1#bib.bib21)] have also become a dominant sequential modeling architecture and have been adapted to time-series forecasting, with influential variants such as Informer [[22](https://arxiv.org/html/2601.13435v1#bib.bib22)] and increasingly use in financial prediction [[23](https://arxiv.org/html/2601.13435v1#bib.bib23), [24](https://arxiv.org/html/2601.13435v1#bib.bib24)].
Yet many Transformer-based financial studies still evaluate primarily under forecasting metrics and then apply external trading rules to obtain positions, which can weaken end-to-end alignment with economic utility.

### II-B Wavelet Transformer and Frequency Fusion

Financial signals are noisy and non-stationary, motivating wavelet transforms as a time-frequency tool for denoising and multi-scale decomposition before prediction. Classic wavelet neural hybrids and wavelet-reconstruction pipelines, including combinations with ARIMA/LSTM or related deep models, have been explored to improve forecast accuracy on volatile markets [[25](https://arxiv.org/html/2601.13435v1#bib.bib25), [26](https://arxiv.org/html/2601.13435v1#bib.bib26), [7](https://arxiv.org/html/2601.13435v1#bib.bib7), [8](https://arxiv.org/html/2601.13435v1#bib.bib8), [9](https://arxiv.org/html/2601.13435v1#bib.bib9), [10](https://arxiv.org/html/2601.13435v1#bib.bib10), [27](https://arxiv.org/html/2601.13435v1#bib.bib27)], and wavelet features have also been used in trading-oriented settings such as reinforcement learning [[28](https://arxiv.org/html/2601.13435v1#bib.bib28)].
More recently, wavelet Transformer hybrids construct multi-scale inputs and use attention to aggregate patterns across time and scales [[12](https://arxiv.org/html/2601.13435v1#bib.bib12), [13](https://arxiv.org/html/2601.13435v1#bib.bib13), [14](https://arxiv.org/html/2601.13435v1#bib.bib14)]. In finance, Stockformer [[29](https://arxiv.org/html/2601.13435v1#bib.bib29)] is a recent attempt to integrate Transformer-style modeling with trading-oriented outputs, and surveys summarize wavelet-integrated deep networks for noisy time series [[11](https://arxiv.org/html/2601.13435v1#bib.bib11)].
A key modeling question is how information should flow across frequencies: simple concatenation or implicit fusion can allow unstable high-frequency components to dominate learning under noisy financial signals.
In this work, we address both the objective mismatch and the frequency-fusion challenge by learning an end-to-end wavelet filter bank jointly with a trading-oriented objective and adopting a low-guided high-frequency injection mechanism, where attention is computed from the low-frequency branch and high-frequency values are injected through a gated residual pathway for stable fusion. Empirically, we benchmark carefully matched MLP/LSTM/Transformer backbones with and without fixed or learnable wavelet front-ends under the same trading protocol.

## III Problem formulation

In this section we formalize the trading task addressed by our model. We begin by specifying the representation of multi-asset price series and returns, then describe the decision times, model inputs and outputs, and finally state the ideal trading objective that motivates our training loss and evaluation metrics.

### III-A Input Windows and Model Outputs

We consider the instruments in a given industry, including related ETFs and sector indices.
We index instruments by j∈{1,…,d}j\in\{1,\dots,d\} and hourly bars by t∈{1,…,T}t\in\{1,\dots,T\}.
For instrument jj, let O​p​e​nj,tOpen\_{j,t} and C​l​o​s​ej,tClose\_{j,t} denote the open and close prices at time tt.
The simple return and log return of bar tt are

|  |  |  |  |
| --- | --- | --- | --- |
|  | rj,t:=C​l​o​s​ej,tO​p​e​nj,t−1,ℓj,t:=log⁡(1+rj,t).r\_{j,t}:=\frac{Close\_{j,t}}{Open\_{j,t}}-1,\qquad\ell\_{j,t}:=\log(1+r\_{j,t}). |  | (1) |

In our experiments, we use the log price return ℓj,t\ell\_{j,t} defined in Eq. ([1](https://arxiv.org/html/2601.13435v1#S3.E1 "In III-A Input Windows and Model Outputs ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) and collect

|  |  |  |
| --- | --- | --- |
|  | 𝐫t=(r1,t,…,rd,t)⊤,ℓt=(ℓ1,t,…,ℓd,t)⊤∈ℝd.\mathbf{r}\_{t}=(r\_{1,t},\ldots,r\_{d,t})^{\top},\qquad\boldsymbol{\ell}\_{t}=(\ell\_{1,t},\ldots,\ell\_{d,t})^{\top}\in\mathbb{R}^{d}. |  |

We adopt a rolling-window formulation: at decision time tt the model observes

|  |  |  |
| --- | --- | --- |
|  | 𝐗t=[ℓt−L+1,…,ℓt]∈ℝd×L,\mathbf{X}\_{t}=\bigl[\boldsymbol{\ell}\_{t-L+1},\dots,\boldsymbol{\ell}\_{t}\bigr]\in\mathbb{R}^{d\times L}, |  |

with columns ordered from oldest to most recent. Additional channels (e.g., ETFs) are absorbed into dd.

Given 𝐗t\mathbf{X}\_{t}, the model outputs a scalar trading signal

|  |  |  |
| --- | --- | --- |
|  | pt=fθ​(𝐗t)∈ℝ,p\_{t}=f\_{\theta}(\mathbf{X}\_{t})\in\mathbb{R}, |  |

where fθf\_{\theta} is WaveLSFormer. We map ptp\_{t} to a bounded position via

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt=2​σ​(pt)−1=tanh⁡(pt2),w\_{t}=2\sigma(p\_{t})-1=\tanh\!\left(\frac{p\_{t}}{2}\right), |  | (2) |

so wt>0w\_{t}>0 (resp. wt<0w\_{t}<0) corresponds to long (resp. short) exposure and |wt||w\_{t}| controls position magnitude.

As discussed in Section [III-E](https://arxiv.org/html/2601.13435v1#S3.SS5 "III-E Position Rule Under a Fixed Risk Budget ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization"), using wtw\_{t} directly can confound signal quality with aggressiveness.
We therefore apply a global risk-budget scaling calibrated on the validation set and define the executable position as

|  |  |  |
| --- | --- | --- |
|  | w~t=h​(wt)∈[w~min,w~max],\tilde{w}\_{t}=h(w\_{t})\in[\tilde{w}\_{\min},\tilde{w}\_{\max}], |  |

where h​(⋅)h(\cdot) is a fixed piecewise-linear mapping that enforces a prescribed average leverage and clips extremes.
In long-short experiments we set w~min=−L\tilde{w}\_{\min}=-L and w~max=L\tilde{w}\_{\max}=L, while in long-only or short-only settings one bound is set to zero.
Section [III-E](https://arxiv.org/html/2601.13435v1#S3.SS5 "III-E Position Rule Under a Fixed Risk Budget ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization") gives the exact form of h​(⋅)h(\cdot).

### III-B Return Representation

In each experiment we select one target asset j⋆∈{1,…,d}j^{\star}\in\{1,\dots,d\} whose trading performance we evaluate, and treat the remaining instruments as auxiliary series providing contextual information. This reflects a common use case in industry-level trading, where a trader is primarily interested in a particular stock or ETF, but leverages signals from other stocks within the same sector. The single-period realized return of the trading strategy between tt and t+1t+1 is then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt+1= 1+w~t⋅rj⋆,t+1R\_{t+1}\;=\;1+\tilde{w}\_{t}\cdot r\_{j^{\star},t+1} |  | (3) |

The return on investment (ROI) of the trading strategy over an evaluation period 𝒯\mathcal{T} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​O​I𝒯=exp⁡(∑t∈𝒯log⁡(Rt))−1.{ROI}\_{\mathcal{T}}\;=\;\exp\bigl(\sum\_{t\in\mathcal{T}}\log\!\left(R\_{t}\right)\bigr)-1. |  | (4) |

### III-C Optimization Target

From a trading perspective, the goal is not to minimize a point-wise prediction error, but to control the distribution of realized strategy returns. In our setting the single–period return of the strategy between tt and t+1t+1 is Eq. ([3](https://arxiv.org/html/2601.13435v1#S3.E3 "In III-B Return Representation ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) and over an evaluation horizon 𝒯\mathcal{T}, the corresponding ROI is Eq. ([4](https://arxiv.org/html/2601.13435v1#S3.E4 "In III-B Return Representation ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")).

Maximizing return alone is not sufficient in practice, since extremely volatile strategies with large draw-downs are usually unacceptable.
A standard risk-adjusted performance measure in finance is the annualized Sharpe ratio, defined on simple returns {Rt}\{R\_{t}\} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮ann=K​𝔼​[Rt−rf/K]Var​(Rt−rf/K),K≈252×6.5,\mathcal{S}\_{\mathrm{ann}}=\sqrt{K}\,\frac{\mathbb{E}\!\left[R\_{t}-r\_{f}/K\right]}{\sqrt{\mathrm{Var}\!\left(R\_{t}-r\_{f}/K\right)}},\qquad K\approx 252\times 6.5, |  | (5) |

where rfr\_{f} is the annual risk-free rate.
In our hourly–bar backtests, RtR\_{t} is already a small return per bar. For model comparison on a fixed dataset we (i) treat the risk–free rate as negligible, like rf≈0r\_{f}\approx 0. (ii) drop the constant K\sqrt{K}, which only rescales all Sharpe values by the same factor. (iii) calculate the expectation and variation over 𝒯\mathcal{T}. Throughout the paper we therefore report a raw Sharpe ratio of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮𝒯=𝔼​[Rt]Var​(Rt),\mathcal{S}\_{\mathcal{T}}\;=\;\frac{\mathbb{E}[R\_{t}]}{\sqrt{\mathrm{Var}(R\_{t})}}, |  | (6) |

and interpret it as a scale–free, risk–adjusted score rather than a directly tradable quantity.

Ideally, we would like the learned policy to achieve a good trade–off between cumulative return and Sharpe ratio. Conceptually, this can be formulated as a multi–objective optimization problem over the model parameters θ\theta,

|  |  |  |
| --- | --- | --- |
|  | maxθ⁡(R​O​I𝒯​(θ),𝒮𝒯​(θ)),\max\_{\theta}\;\Bigl({ROI}\_{\mathcal{T}}(\theta),\;\mathcal{S}\_{\mathcal{T}}(\theta)\Bigr), |  |

The exact loss components and their implementation details are given in Section [VI-A](https://arxiv.org/html/2601.13435v1#S6.SS1 "VI-A Loss Function Design ‣ VI Training Design ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization").

### III-D Wavelet-based Signal Noise Decomposition

At short horizons, financial returns exhibit low signal-to-noise ratios. Following wavelet denoising, we decompose the target log return into a slowly varying component and a rapidly fluctuating residual,

|  |  |  |
| --- | --- | --- |
|  | ℓj⋆,t=st+nt,\ell\_{j^{\star},t}=s\_{t}+n\_{t}, |  |

where sts\_{t} captures low-frequency structure (e.g., trend) and ntn\_{t} aggregates high-frequency, largely unpredictable variations. Over an interval 𝒯\mathcal{T}, we define the effective SNR as

|  |  |  |  |
| --- | --- | --- | --- |
|  | SNR𝒯=Vart∈𝒯​[st]Vart∈𝒯​[nt]+ε,\mathrm{SNR}\_{\mathcal{T}}\;=\;\frac{\mathrm{Var}\_{t\in\mathcal{T}}[s\_{t}]}{\mathrm{Var}\_{t\in\mathcal{T}}[n\_{t}]+\varepsilon}, |  | (7) |

with a small ε>0\varepsilon>0 for numerical stability.

In WaveLSFormer, a neural wavelet front-end performs a learnable time-frequency decomposition of the raw log-return sequence {ℓj⋆,t}\{\ell\_{j^{\star},t}\} into approximations of {st}\{s\_{t}\} and {nt}\{n\_{t}\} using finite-impulse-response low-/high-pass filters. We learn filters that increase SNR\mathrm{SNR} relative to the raw series while producing features that benefit the downstream trading objective. To this end, we add frequency-domain regularizers that promote low-/high-frequency separation and encourage the filter pair to behave approximately as a tight frame; details are given in Section [V](https://arxiv.org/html/2601.13435v1#S5 "V Architecture ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization").

Given multivariate histories 𝐗t\mathbf{X}\_{t} and the next-step return ℓj⋆,t+1\ell\_{j^{\star},t+1}, our goal is to learn a mapping fθf\_{\theta} that outputs trading signals ptp\_{t} whose induced positions wtw\_{t} maximize risk-adjusted strategy performance, aided by the wavelet front-end that improves the effective SNR of the input.

### III-E Position Rule Under a Fixed Risk Budget

Equation ([2](https://arxiv.org/html/2601.13435v1#S3.E2 "In III-A Input Windows and Model Outputs ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) bounds the trading signal, so a single trade never exceeds full long/short exposure. Yet different models can induce very different distributions of wtw\_{t}: some outputs saturate near ±1\pm 1, while others concentrate around 0. Using wtw\_{t} directly would therefore confound signal quality with aggressiveness, since strategies with larger average |wt||w\_{t}| effectively take larger bets and thus realize larger gains and losses.

To normalize risk across models, we estimate a global scale on the validation set 𝒟val\mathcal{D}\_{\mathrm{val}} with length Tval=|𝒟val|T\_{\mathrm{val}}=|\mathcal{D}\_{\mathrm{val}}|. We compute the mean absolute magnitude

|  |  |  |
| --- | --- | --- |
|  | sval=1Tval​∑t∈𝒟val|wt|,s\_{\mathrm{val}}=\frac{1}{T\_{\mathrm{val}}}\sum\_{t\in\mathcal{D}\_{\mathrm{val}}}|w\_{t}|, |  |

and rescale the signal using Eq. ([8](https://arxiv.org/html/2601.13435v1#S3.E8 "In III-E Position Rule Under a Fixed Risk Budget ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | w^t=wtsval,\hat{w}\_{t}=\frac{w\_{t}}{s\_{\mathrm{val}}}, |  | (8) |

so the validation-period average of |w^t||\hat{w}\_{t}| is close to one.

To suppress tiny, noise-dominated trades, we apply a dead zone with threshold τ>0\tau>0 and set τ=0.01\tau=0.01 in all experiments. We then enforce an optional leverage cap and scale by a target average leverage L>0L>0 (we use L=1L=1), yielding the executable position in Eq. ([9](https://arxiv.org/html/2601.13435v1#S3.E9 "In III-E Position Rule Under a Fixed Risk Budget ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | w~t={0,|w^t|<τ,max⁡(−L,min⁡(L,w^t)),otherwise.\tilde{w}\_{t}=\begin{cases}0,&|\hat{w}\_{t}|<\tau,\\ \max(-L,\min(L,\hat{w}\_{t})),&\text{otherwise}.\end{cases} |  | (9) |

By construction,

|  |  |  |
| --- | --- | --- |
|  | 1Tval​∑t∈𝒟val|w~t|≈L,\frac{1}{T\_{\mathrm{val}}}\sum\_{t\in\mathcal{D}\_{\mathrm{val}}}|\tilde{w}\_{t}|\approx L, |  |

up to sparsification from the dead zone, so models are evaluated under a comparable risk budget. The scale svals\_{\mathrm{val}} is estimated once on 𝒟val\mathcal{D}\_{\mathrm{val}} and kept fixed for testing and online simulation, ensuring a consistent and implementable mapping from network outputs to positions at a pre-specified risk level.

## IV Data Construction Pipeline

Our model is designed to directly optimize a trading objective rather than minimize a point-wise forecasting error.
Therefore, we focus on economic performance, such as annualized return and Sharpe ratio, as the primary evaluation metrics, rather than MSE/MAE.

### IV-A Data Collection

We construct an intraday U.S. equity dataset from two sources. We obtain price and volume data from the commercial API provider polygon.io, and download one-hour OHLCV bars for each stock over roughly the past ten years, providing multi-year coverage at intraday resolution.

We obtain sector and industry classifications from StockAnalysis111<https://stockanalysis.com/>, which publishes curated U.S. stock lists by sector and industry. We extract symbols for each industry and use this stock-industry mapping to define the cross-sectional universe and the industry-group experiments in Section [VII](https://arxiv.org/html/2601.13435v1#S7 "VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization").

### IV-B Data Preprocessing

We consider hourly bar-based intraday trading. Each stock is represented by OHLCV bars, and at the beginning of hour tt the model observes past bars and selects the position to hold over hour t+1t{+}1, making within-bar price change a natural primitive. Because price levels vary widely across securities, we use scale-free inputs by converting prices to intraday returns: Eq. ([1](https://arxiv.org/html/2601.13435v1#S3.E1 "In III-A Input Windows and Model Outputs ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) computes the log percentage change of the close relative to the open, which stabilizes variance, partially symmetrizes gains and losses, and yields smoother dimensionless features for hourly modeling.

### IV-C Stock Selection

We build industry-level stock groups as multi-asset inputs. For each industry with a liquid U.S.-listed ETF, we collect constituent stocks traded on major U.S. exchanges and treat the ETF as an economic proxy for the sector. We quantify similarity in recent price dynamics by computing Dynamic Time Warping (DTW) distances between candidates’ historical log-change series over a fixed look-back window, where DTW is robust to local time shifts. Using the training period, we set the empirical median (50th percentile) of DTW distances as a threshold and retain stocks whose distance to the industry reference is below this value, filtering idiosyncratic outliers and preserving coherent trend shapes as illustrated in Fig. [1](https://arxiv.org/html/2601.13435v1#S4.F1 "Figure 1 ‣ IV-C Stock Selection ‣ IV Data Construction Pipeline ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization"). We then apply non-parametric Granger causality tests to the DTW-selected set and remove stocks that show no predictive relation with the target asset.

![Refer to caption](images/renewable_energy_dwt.png)


Figure 1: Stock codes selected under DWT.

### IV-D Financial Securities with Granger-type Causality

We assume that same-industry stocks exhibit co-movements and lead-lag effects. We quantify such dependencies using nonparametric Granger causality [[30](https://arxiv.org/html/2601.13435v1#bib.bib30)], where xtx\_{t} Granger-causes yty\_{t} if adding lags of xtx\_{t} significantly improves predicting yty\_{t} beyond using lags of yty\_{t} alone.

For each industry universe, we run pairwise tests on the log-change series of candidate securities to obtain a directional p-value matrix. We then apply Benjamini-Hochberg FDR control and retain securities whose adjusted p-values with respect to the target asset are below 0.050.05 in at least one direction. The retained securities form the final multi-asset input set. Fig. [2](https://arxiv.org/html/2601.13435v1#S4.F2 "Figure 2 ‣ IV-D Financial Securities with Granger-type Causality ‣ IV Data Construction Pipeline ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization") illustrates the selected stocks in Renewable Energy, and Table [I](https://arxiv.org/html/2601.13435v1#S4.T1 "TABLE I ‣ IV-D Financial Securities with Granger-type Causality ‣ IV Data Construction Pipeline ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization") reports the full adjusted p-value matrix, which reveals the directed dependence structure within each industry universe.

![Refer to caption](images/renewable_energy_granger.png)


Figure 2: Stock selected after Granger causality filter in the renewable energy industry.




TABLE I: BH-FDR-adjusted pp-value matrix for pairwise tests on hourly log-percent-change series. Smaller values indicate stronger evidence of dependence. Bold entries denote significant pairs under FDR control (padj<0.05p\_{\text{adj}}<0.05); bold tickers indicate the retained assets.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | \cellcolorgray!15AEP | ATO | \cellcolorgray!15AWK | \cellcolorgray!15CMS | \cellcolorgray!15CNP | CWEN | EIX | EVRG | IDA | \cellcolorgray!15NEE | OTTR | \cellcolorgray!15PEG | PNW | POR | \cellcolorgray!15WEC | \cellcolorgray!15XEL |
| AEP | 1 | 0.8107 | 0.7066 | 0.7824 | 1 | 0.3241 | 0.8397 | 0.9305 | 0.8041 | 0.8434 | 0.3984 | 0.4637 | 0.6562 | 0.9759 | 0.9506 | 0.8379 |
| ATO | 0.3984 | 1 | 0.3984 | 0.3241 | 0.3984 | 0.6317 | 1 | 1 | 1 | 0.8041 | 0.3812 | 1 | 0.7737 | 0.9759 | 0.3812 | 0.5568 |
| AWK | 1 | 0.7002 | 1 | 1 | 0.9759 | 0.0846 | 1 | 0.7393 | 0.8379 | 0.4262 | 0.456 | 0.8379 | 0.9305 | 0.8041 | 0.8379 | 0.6723 |
| CMS | 0.0521 | 1 | 0.3716 | 1 | 0.9506 | 0.3984 | 0.8379 | 1 | 0.8379 | 0.3835 | 0.8379 | 1 | 0.8813 | 0.6592 | 0.3812 | 0.3487 |
| CNP | 0.0505 | 0.3984 | 0.3241 | 0.4262 | 1 | 0.4262 | 0.9612 | 0.4838 | 0.7276 | 0.3984 | 0.3984 | 0.8107 | 0.3798 | 0.3984 | 0.3241 | 0.2143 |
| \cellcolorgray!15CWEN | \cellcolorgray!150.0124 | 0.0846 | \cellcolorgray!150.0326 | \cellcolorgray!150.0221 | \cellcolorgray!150.0297 | 1 | 0.0576 | 0.0648 | 0.1123 | \cellcolorgray!150.0001 | 0.7909 | \cellcolorgray!150.0326 | 0.3812 | 0.1703 | \cellcolorgray!150.0326 | \cellcolorgray!150.0345 |
| EIX | 0.3812 | 0.8107 | 0.3487 | 0.5568 | 0.296 | 0.9955 | 1 | 1 | 0.8107 | 0.3984 | 0.7025 | 0.8379 | 0.3487 | 0.4262 | 0.4262 | 0.4701 |
| EVRG | 0.0297 | 0.2143 | 0.0149 | 0.0558 | 0.1048 | 0.8107 | 0.52 | 1 | 0.3716 | 0.1719 | 0.3241 | 0.3467 | 0.2443 | 0.3812 | 0.0505 | 0.0912 |
| IDA | 0.4181 | 0.7737 | 0.4262 | 0.3812 | 0.1836 | 0.6062 | 0.8379 | 0.6235 | 1 | 0.3812 | 0.596 | 0.9759 | 0.3984 | 0.3342 | 0.3984 | 0.7409 |
| NEE | 0.7909 | 0.3449 | 0.3812 | 0.4262 | 0.6396 | 0.8107 | 0.8731 | 0.503 | 0.2482 | 1 | 0.6235 | 0.8409 | 0.5043 | 0.3812 | 0.5805 | 0.4397 |
| OTTR | 1 | 0.6062 | 0.9759 | 0.942 | 0.8379 | 0.9506 | 0.8434 | 0.296 | 0.6235 | 1 | 1 | 0.6396 | 0.6592 | 0.9759 | 0.7096 | 0.8107 |
| PEG | 0.0687 | 0.3812 | 0.0326 | 0.0846 | 0.4262 | 0.9421 | 0.5308 | 0.5006 | 0.604 | 0.0846 | 0.4106 | 1 | 0.3812 | 0.296 | 0.3984 | 0.296 |
| PNW | 0.8379 | 0.9759 | 0.7409 | 1 | 1 | 0.5985 | 0.7393 | 0.9759 | 1 | 0.3241 | 1 | 1 | 1 | 0.9759 | 0.9305 | 0.9633 |
| POR | 0.3984 | 0.8813 | 0.3161 | 0.3984 | 0.4713 | 0.9791 | 0.9759 | 0.8321 | 0.9759 | 0.2213 | 0.6988 | 0.8107 | 0.7224 | 1 | 0.3812 | 0.8321 |
| WEC | 0.531 | 1 | 0.4262 | 0.4262 | 1 | 0.3487 | 0.7909 | 0.8379 | 0.7409 | 0.4838 | 0.8379 | 0.8713 | 0.9421 | 0.9759 | 1 | 0.2443 |
| XEL | 1 | 0.9305 | 0.9573 | 0.9759 | 0.9123 | 0.3812 | 0.4397 | 0.8813 | 0.9305 | 0.8379 | 0.8321 | 0.3812 | 0.9791 | 0.9759 | 1 | 1 |

## V Architecture

WaveLSFormer combines a learnable wavelet front-end with a standard Transformer. It decomposes prices into low-frequency trends and high-frequency residuals, fuses them, and feeds a Transformer encoder for position prediction. We therefore detail the front-end—filter parameterization, regularization, and cross-frequency integration that injects high-frequency cues into the low-frequency path.

### V-A Neural Wavelet Filters

As widely known, financial data contains a low info-noise ratio that causes the training process to always be misled by high-frequency noise gradient. To deal with this issue, we implement neural wavelet blocks as roles of low-pass and high-pass filters to re-balance the proportion of input info and noise.

#### V-A1 FIR Convolution Kernels and Classical Discrete–time Filters

In our neural wavelet front-end, each learnable filter is implemented as a one-dimensional finite impulse response (FIR) convolution kernel. Let x​[n]x[n] denote a discrete-time input signal and let 𝜽=(θ0,…,θL−1)\boldsymbol{\theta}=(\theta\_{0},\dots,\theta\_{L-1}) be the convolution kernel of length LL. A standard conv1d layer with stride 1 and no dilation computes

|  |  |  |  |
| --- | --- | --- | --- |
|  | y​[n]=∑k=0L−1θk​x​[n−k],y[n]=\sum\_{k=0}^{L-1}\theta\_{k}\,x[n-k], |  | (10) |

which is exactly the input and output relation of a linear time-invariant (LTI) discrete-time filter.

For an LTI system, the sequence h​[n]h[n] is defined as the response to a discrete-time unit impulse

|  |  |  |
| --- | --- | --- |
|  | δ​[n]={1,n=0,0,n≠0\delta[n]=\begin{cases}1,&n=0,\\ 0,&n\neq 0\end{cases} |  |

Substituting x​[n]=δ​[n]x[n]=\delta[n] into Eq. ([10](https://arxiv.org/html/2601.13435v1#S5.E10 "In V-A1 FIR Convolution Kernels and Classical Discrete–time Filters ‣ V-A Neural Wavelet Filters ‣ V Architecture ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) yields

|  |  |  |
| --- | --- | --- |
|  | y​[n]=∑k=0L−1θk​δ​[n−k]=θn,y[n]=\sum\_{k=0}^{L-1}\theta\_{k}\,\delta[n-k]=\theta\_{n}, |  |

for n=0,…,L−1n=0,\dots,L-1 and y​[n]=0y[n]=0 otherwise. Hence the impulse response of the filter is h​[n]=θnh[n]=\theta\_{n}, so the FIR convolution kernel and the time-domain impulse response are the same object that the trainable parameters {θk}\{\theta\_{k}\} directly define the filter’s behavior in the time domain.

The discrete-time frequency response of an LTI filter is defined as the complex gain applied to a complex exponential input x​[n]=ej​ω​nx[n]=e^{\mathrm{j}\omega n}. Using Eq. ([10](https://arxiv.org/html/2601.13435v1#S5.E10 "In V-A1 FIR Convolution Kernels and Classical Discrete–time Filters ‣ V-A Neural Wavelet Filters ‣ V Architecture ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | y​[n]\displaystyle y[n] | =∑k=0L−1θk​ej​ω​(n−k)=ej​ω​n​∑k=0L−1θk​e−j​ω​k.\displaystyle=\sum\_{k=0}^{L-1}\theta\_{k}\,e^{\mathrm{j}\omega(n-k)}=e^{\mathrm{j}\omega n}\sum\_{k=0}^{L-1}\theta\_{k}\,e^{-\mathrm{j}\omega k}. |  |

Thus ej​ω​ne^{\mathrm{j}\omega n} is an eigenfunction of the system and the corresponding eigenvalue

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(ej​ω)=∑k=0L−1θk​e−j​ω​k=∑k=0L−1h​[k]​e−j​ω​kH(e^{\mathrm{j}\omega})=\sum\_{k=0}^{L-1}\theta\_{k}\,e^{-\mathrm{j}\omega k}=\sum\_{k=0}^{L-1}h[k]\,e^{-\mathrm{j}\omega k} |  | (11) |

is the frequency response. Eq. ([11](https://arxiv.org/html/2601.13435v1#S5.E11 "In V-A1 FIR Convolution Kernels and Classical Discrete–time Filters ‣ V-A Neural Wavelet Filters ‣ V Architecture ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) is exactly the discrete-time Fourier transform (DTFT) of the impulse response h​[n]h[n]. Therefore, for an FIR filter, the frequency response is simply the Fourier transform of the convolution kernel. This provides a direct bridge between the learnable parameters in the neural network and the classical time–frequency interpretation of digital filters.

#### V-A2 Differentiable Spectral Regularization via rFFT

Let 𝜽∈ℝL\boldsymbol{\theta}\in\mathbb{R}^{L} be a real-valued FIR kernel and 𝜽^=ℱ​(𝜽)\hat{\boldsymbol{\theta}}=\mathcal{F}(\boldsymbol{\theta}) its DFT.
In matrix form, 𝜽^=𝐅​𝜽\hat{\boldsymbol{\theta}}=\mathbf{F}\boldsymbol{\theta} with a fixed 𝐅∈ℂL×L\mathbf{F}\in\mathbb{C}^{L\times L}. Hence ℱ\mathcal{F} is linear and differentiable everywhere, with constant Jacobian 𝐅\mathbf{F}.
In practice we use rFFT, which is an optimized implementation of the same linear map specialized to real inputs (exploiting conjugate symmetry).

This enables differentiable frequency-domain regularization. A generic spectral regularizer is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒs​p​e​c​(𝜽)=∑kρ​(|θ^k|),\mathcal{L}\_{spec}(\boldsymbol{\theta})=\sum\_{k}\rho\!\left(|\hat{\theta}\_{k}|\right), |  | (12) |

where ρ​(⋅)\rho(\cdot) is differentiable. By the chain rule,

|  |  |  |
| --- | --- | --- |
|  | ∂ℒs​p​e​c∂𝜽=𝐅𝖧​∂ℒs​p​e​c∂𝜽^,\frac{\partial\mathcal{L}\_{spec}}{\partial\boldsymbol{\theta}}=\mathbf{F}^{\mathsf{H}}\,\frac{\partial\mathcal{L}\_{spec}}{\partial\hat{\boldsymbol{\theta}}}, |  |

with 𝐅𝖧\mathbf{F}^{\mathsf{H}} the Hermitian transpose (i.e., inverse DFT up to scaling). Equivalently, back-propagation through rFFT amounts to applying an inverse FFT to the frequency-domain gradient. Therefore, adding Eq. ([12](https://arxiv.org/html/2601.13435v1#S5.E12 "In V-A2 Differentiable Spectral Regularization via rFFT ‣ V-A Neural Wavelet Filters ‣ V Architecture ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) on rFFT-transformed learnable kernels preserves differentiability and allows end-to-end training with standard optimizers.

To enforce complementary low/high-frequency coverage, we penalize high-frequency energy in the low-pass filter and low-frequency energy in the high-pass filter, add an overlap term to sharpen separation, and use Parseval and shape losses to constrain energy and frequency-response form; details are in Section [VI-A7](https://arxiv.org/html/2601.13435v1#S6.SS1.SSS7 "VI-A7 Neural Wavelet Loss ‣ VI-A Loss Function Design ‣ VI Training Design ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization").

#### V-A3 Low-guided High-frequency Injection

To fuse low-frequency and high-frequency information while maintaining training stability, we introduce a low-guided high-frequency injection (LGHI) module.
Let L∈ℝT×dL\in\mathbb{R}^{T\times d} denote the low-frequency representations and H∈ℝT×dH\in\mathbb{R}^{T\times d} the corresponding high-frequency representations.
Different from standard cross-attention, where QQ comes from one sequence and K,VK,V come from the other, we compute the attention map *only* from the low-frequency branch and use it to inject high-frequency values.
Concretely, we define

|  |  |  |
| --- | --- | --- |
|  | A​(L)=softmax​((L​WQ)​(L​WK)⊤dk),Z​(L,H)=A​(L)​(H​WV)​WO,\begin{split}&A(L)=\mathrm{softmax}\!\left(\frac{(LW\_{Q})(LW\_{K})^{\top}}{\sqrt{d\_{k}}}\right),\\ &Z(L,H)=A(L)\,(HW\_{V})W\_{O},\end{split} |  |

where WQ,WK∈ℝd×dkW\_{Q},W\_{K}\in\mathbb{R}^{d\times d\_{k}} and WV∈ℝd×dvW\_{V}\in\mathbb{R}^{d\times d\_{v}} are projection matrices and
WOW\_{O} is the output projection (multi-head variants follow the standard formulation).
The final fused representation is given by a gated residual injection:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y=L+β​Z​(L,H),β=σ​(γ),Y=L+\beta\,Z(L,H),\qquad\beta=\sigma(\gamma), |  | (13) |

where γ\gamma is a learnable scalar controlling the overall scale of the injected high-frequency residual.
This design encourages the model to preserve the stable low-frequency backbone while selectively incorporating high-frequency cues, because the attention weights are determined by LL and are therefore less sensitive to noisy high-frequency fluctuations.

## VI Training Design

Training choices, such as loss, optimizer, and learning-rate schedule, strongly influence trading outcomes. Because convenient objectives may misalign with deployment metrics (return, Sharpe, draw-down), low training loss can still generalize poorly. We therefore present: (i) a differentiable surrogate objective (soft labels from future log returns + Sharpe regularization), (ii) a stabilized optimization setup for heavy-tailed financial noise, and (iii) validation/checkpoint selection based on trading performance.

### VI-A Loss Function Design

In stock trading, the ultimate objective is to maximize realized profit rather than to minimize point-wise prediction error. Therefore, the training loss should be a simple, differentiable surrogate that aligns with return optimization and provides stable gradients. In generic time-series forecasting, models are typically trained to predict the next-step target value, where MAE or MSE are standard choices. However, in financial settings, minimizing MAE/MSE on prices or returns is often weakly correlated with trading performance and thus is not well suited for learning profit-seeking decisions.

#### VI-A1 Drawbacks of Regression Losses

Many financial time-series models train neural networks as return forecasters by minimizing point-wise regression losses such as MSE or MAE. Given a future log return ℓ^t\hat{\ell}\_{t}, they learn ℓt=fθ​(xt)\ell\_{t}=f\_{\theta}(x\_{t}) via

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒr​e​g=𝔼​[l​o​s​s​(ℓt,ℓ^t)],l​o​s​s∈{MSE,MAE}.\mathcal{L}\_{reg}=\mathbb{E}\!\big[loss(\ell\_{t},\hat{\ell}\_{t})\big],\qquad loss\in\{\text{MSE},\ \text{MAE}\}. |  | (14) |

While statistically convenient, ℒr​e​g\mathcal{L}\_{reg} is misaligned with trading: performance is driven by the position w~t\tilde{w}\_{t} and the resulting P&L Rt=w~t​ℓtR\_{t}=\tilde{w}\_{t}\,\ell\_{t}, not by the numeric forecast error of ℓt\ell\_{t}. Consequently, lower regression error does not necessarily translate to higher ROI/Sharpe. The mismatch is exacerbated by the asymmetric economic cost as a wrong sign under high exposure is far more damaging than a small magnitude error on a correct trade, whereas MSE/MAE penalize deviations symmetrically.

Moreover, under noisy and non-stationary returns, minimizing ℒr​e​g\mathcal{L}\_{reg} mainly encourages approximating 𝔼​[ℓt∣xt]\mathbb{E}[\ell\_{t}\mid x\_{t}], which offers no guarantee of improved RtR\_{t} or risk-adjusted performance. Therefore, we do not treat the network as a pure forecaster. Instead, we interpret its output as a continuous trading position w~t∈[−1,1]\tilde{w}\_{t}\in[-1,1] (flat if w~t∈[−0.01,0.01]\tilde{w}\_{t}\in[-0.01,0.01]) and optimize a trading-aligned objective,

|  |  |  |
| --- | --- | --- |
|  | ℒt​r​a​d​e=−𝔼​[w~t​yt]+λ​Ω​(w~t),\mathcal{L}\_{trade}=-\,\mathbb{E}\big[\tilde{w}\_{t}y\_{t}\big]+\lambda\,\Omega(\tilde{w}\_{t}), |  |

where Ω​(⋅)\Omega(\cdot) regularizes leverage, turnover, or excessive position variability.

#### VI-A2 Stock Direction and Tanh Position Loss

The *Stock Direction* loss treats the sign of the model output as a long/short signal: go long if pt>0p\_{t}>0, short if pt<0p\_{t}<0, and optionally trade only when |pt|>τ|p\_{t}|>\tau to filter low-confidence positions. The resulting position in Eq. ([4](https://arxiv.org/html/2601.13435v1#S3.E4 "In III-B Return Representation ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) is defined in Eq. ([2](https://arxiv.org/html/2601.13435v1#S3.E2 "In III-A Input Windows and Model Outputs ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")). Following Eq. ([1](https://arxiv.org/html/2601.13435v1#S3.E1 "In III-A Input Windows and Model Outputs ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")), let rtr\_{t} and ℓt\ell\_{t} denote the simple and log returns.

To turn multiplicative ROI into additive form, we use the small-return approximation. For |rt|<0.1|r\_{t}|<0.1,

|  |  |  |
| --- | --- | --- |
|  | log⁡(1+rt)=rt−rt22+O​(rt3),\log(1+r\_{t})=r\_{t}-\frac{r\_{t}^{2}}{2}+O(r\_{t}^{3}), |  |

so ℓt≈rt\ell\_{t}\approx r\_{t} with leading error rt2/2≤0.005r\_{t}^{2}/2\leq 0.005 when |rt|≤0.1|r\_{t}|\leq 0.1. Hence we approximate

|  |  |  |
| --- | --- | --- |
|  | ROI≈exp⁡(∑tsign​(pt)​ℓt)−1,\mathrm{ROI}\approx\exp\Bigl(\sum\_{t}\mathrm{sign}(p\_{t})\,\ell\_{t}\Bigr)-1, |  |

and define the corresponding trade loss as

|  |  |  |
| --- | --- | --- |
|  | ℒt​r​a​d​e=−exp⁡(∑tsign​(pt)​ℓt).\mathcal{L}\_{trade}=-\exp\Bigl(\sum\_{t}\mathrm{sign}(p\_{t})\,\ell\_{t}\Bigr). |  |

The *Tanh position* loss replaces the all-in direction decision by a continuous position size on the target asset using tanh⁡(pt)∈[−1,1]\tanh(p\_{t})\in[-1,1] as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒt​r​a​d​e=−exp⁡(∑ttanh⁡(pt)​ℓt).\mathcal{L}\_{trade}=-\exp\Bigl(\sum\_{t}\tanh(p\_{t})\,\ell\_{t}\Bigr). |  | (15) |

#### VI-A3 Sigmoid Position Loss

Direct position optimization with the Stock Tanh loss often suffers from gradient saturation: as outputs approach the bounds, tanh′⁡(⋅)\tanh^{\prime}(\cdot) becomes small and updates vanish. We also avoid log⁡(tanh⁡(⋅))\log(\tanh(\cdot)) objectives, whose logit gradient

|  |  |  |
| --- | --- | --- |
|  | dd​pt​log⁡(tanh⁡(pt))=1−tanh2⁡(pt)tanh⁡(pt),\frac{\mathrm{d}}{\mathrm{d}p\_{t}}\log(\tanh(p\_{t}))=\frac{1-\tanh^{2}(p\_{t})}{\tanh(p\_{t})}, |  |

is ill-conditioned near the origin and still decays as |pt||p\_{t}| grows. Instead, we treat ptp\_{t} as the logit of a Bernoulli variable indicating willingness to go long and perform the signed position mapping only at inference.

Ignoring transaction costs and position constraints, the ROI-optimal policy is fully long for rt≥0r\_{t}\geq 0 and fully short otherwise, so we cast trading as a binary classification problem:

|  |  |  |
| --- | --- | --- |
|  | yt={1,rt≥0,0,rt<0.y\_{t}=\begin{cases}1,&r\_{t}\geq 0,\\ 0,&r\_{t}<0.\end{cases} |  |

We train in probability space with a weighted logistic loss, so gradients depend on the confidence gap between σ​(pt)\sigma(p\_{t}) and yty\_{t} and remain informative; at inference, we map σ​(pt)\sigma(p\_{t}) to a smooth exposure in [−1,1][-1,1] via Eq. ([2](https://arxiv.org/html/2601.13435v1#S3.E2 "In III-A Input Windows and Model Outputs ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")).

To emphasize economically significant moves, we weight each sample by the absolute log return |ℓt||\ell\_{t}| (e.g., +100%+100\% and −50%-50\% have equal |ℓt||\ell\_{t}|). The resulting Stock Sigmoid loss is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒt​r​a​d​e​(t)={−log⁡(σ​(pt))​|ℓt|,rt≥0,−log⁡(1−σ​(pt))​|ℓt|,rt<0,\mathcal{L}\_{trade}(t)=\begin{cases}-\log\big(\sigma(p\_{t})\big)\,|\ell\_{t}|,&r\_{t}\geq 0,\\[4.0pt] -\log\big(1-\sigma(p\_{t})\big)\,|\ell\_{t}|,&r\_{t}<0,\end{cases} |  | (16) |

which mitigates saturation in Stock Tanh while aligning optimization with the sign and magnitude of future returns.

#### VI-A4 Soft-Label Position Loss

Although the Stock Sigmoid loss mitigates the saturation of Stock Tanh, it still has two drawbacks: gradients are dominated by rare extreme moves, and hard binary targets remain overly sharp when returns are near zero, forcing Pt=σ​(pt)P\_{t}=\sigma(p\_{t}) toward 0 or 11 despite highly ambiguous signals, which can induce unstable updates.

We therefore replace hard labels with probabilistic soft targets that reflect directional confidence:

|  |  |  |
| --- | --- | --- |
|  | yt=σ​(k​ℓt),y\_{t}=\sigma(k\,\ell\_{t}), |  |

where k>0k>0 controls how quickly yty\_{t} departs from 0.50.5 as |ℓt||\ell\_{t}| increases. We choose kk by calibration (e.g., enforcing σ​(k​ℓt(+5%))≈0.9\sigma(k\,\ell\_{t}^{(+5\%)})\approx 0.9), which yields k≈45k\approx 45 in our setting; we fix k=45k=45 for all experiments across industries for reproducibility. Given yty\_{t} and PtP\_{t}, we use the soft-label cross-entropy

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒt​r​a​d​e​(t)=−yt​log⁡Pt−(1−yt)​log⁡(1−Pt).\mathcal{L}\_{trade}(t)=-y\_{t}\log P\_{t}-(1-y\_{t})\log(1-P\_{t}). |  | (17) |

At inference time, we map the model output to a continuous position in [−1,1][-1,1] using Eq. ([9](https://arxiv.org/html/2601.13435v1#S3.E9 "In III-E Position Rule Under a Fixed Risk Budget ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")), where the sign encodes long/short/flat and the magnitude controls position size. Overall, soft labels provide smoother gradients, reduce over-emphasis on extreme returns, and align the learned signal with probabilistic directional confidence.

Remark. Subtracting the Bernoulli entropy of yty\_{t} turns the above loss into a KL divergence and shifts the optimum to zero, but it does not affect gradients; we therefore use the standard form for simplicity.

#### VI-A5 Overfitting Penalty

Directly optimizing a profit-oriented objective can encourage unrealistic, overfit strategies with extremely large training returns. We therefore impose a soft upper bound on batch-level ROI.

For a mini-batch ℬ\mathcal{B} spanning HℬH\_{\mathcal{B}} time steps, the batch log return and ROI are

|  |  |  |
| --- | --- | --- |
|  | Lℬ=∑t∈ℬℓt,Rℬ=exp⁡(Lℬ)−1.L\_{\mathcal{B}}=\sum\_{t\in\mathcal{B}}\ell\_{t},\qquad R\_{\mathcal{B}}=\exp(L\_{\mathcal{B}})-1. |  |

We cap the annualized ROI at Rannmax=1.0R\_{\mathrm{ann}}^{\max}=1.0 and treat it as a tunable risk-control parameter. With hourly data, 252252 trading days/year and 6.56.5 hours/day, we have Hyear=1638H\_{\mathrm{year}}=1638. Assuming constant per-hour log return, the implied maximum batch log return is

|  |  |  |
| --- | --- | --- |
|  | Lℬmax=log⁡(1+Rannmax)​HℬHyear,L\_{\mathcal{B}}^{\max}=\log(1+R\_{\mathrm{ann}}^{\max})\,\frac{H\_{\mathcal{B}}}{H\_{\mathrm{year}}}, |  |

which yields the batch ROI threshold

|  |  |  |
| --- | --- | --- |
|  | Tℬ=exp⁡(Lℬmax)−1=(1+Rannmax)Hℬ/Hyear−1.T\_{\mathcal{B}}=\exp(L\_{\mathcal{B}}^{\max})-1=(1+R\_{\mathrm{ann}}^{\max})^{H\_{\mathcal{B}}/H\_{\mathrm{year}}}-1. |  |

We then penalize excess ROI using a one-sided quadratic hinge:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒp​e​n​a​l​t​y=λroi​[max⁡(Rℬ−Tℬ, 0)]2,\mathcal{L}\_{penalty}=\lambda\_{\mathrm{roi}}\bigl[\max(R\_{\mathcal{B}}-T\_{\mathcal{B}},\,0)\bigr]^{2}, |  | (18) |

where λroi\lambda\_{\mathrm{roi}} controls the penalty strength.

#### VI-A6 Sharpe Regularizer

To account for risk, we augment the trading loss with a Sharpe-ratio regularizer. Let RpR\_{p} be the per-step strategy return. The classical Sharpe is

|  |  |  |
| --- | --- | --- |
|  | S∗=𝔼​[Rp]−rfσ​(Rp−rf),S^{\ast}=\frac{\mathbb{E}[R\_{p}]-r\_{f}}{\sigma(R\_{p}-r\_{f})}, |  |

where rfr\_{f} is the risk-free rate. We omit rfr\_{f} and use

|  |  |  |
| --- | --- | --- |
|  | S=𝔼​[Rp]σ​(Rp),S=\frac{\mathbb{E}[R\_{p}]}{\sigma(R\_{p})}, |  |

with 𝔼​[⋅]\mathbb{E}[\cdot] and σ​(⋅)\sigma(\cdot) computed over a mini-batch. This is justified by our short horizon, so that rfr\_{f} is small relative to RpR\_{p}, and by rfr\_{f} being approximately constant w.r.t. model parameters, hence having negligible impact on gradient directions. For simplicity, we ignore transaction costs and assume RpR\_{p} has finite second moments.

Instead of maximizing SS directly, we use an exponentially decaying penalty with a capped Sharpe level:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒs​h​a​r​p​e=exp⁡(−α⋅min⁡(3K,𝔼​[Rp]σ​(Rp)+ε)),\mathcal{L}\_{sharpe}=\exp\!\left(-\alpha\cdot\min\!\Big(\frac{3}{\sqrt{K}},\;\frac{\mathbb{E}[R\_{p}]}{\sigma(R\_{p})+\varepsilon}\Big)\right), |  | (19) |

where KK is the annualization factor in Eq. ([5](https://arxiv.org/html/2601.13435v1#S3.E5 "In III-C Optimization Target ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")), α>0\alpha>0 controls strength, and ε\varepsilon stabilizes training. The cap 3/K3/\sqrt{K} prevents unrealistically large Sharpe values from dominating; once exceeded, this term provides no additional gradient. The exponential form smooths optimization and avoids Sharpe-driven gradients overwhelming the primary loss.

For ℒs​h​a​r​p​e\mathcal{L}\_{sharpe} we compute RpR\_{p} without position clamping as defined in Eq. ([9](https://arxiv.org/html/2601.13435v1#S3.E9 "In III-E Position Rule Under a Fixed Risk Budget ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) to preserve gradients, while all reported performance uses clamped positions.

#### VI-A7 Neural Wavelet Loss

Our low-/high-pass filters are implemented as 1D FIR convolutions. As discussed in Section [V-A1](https://arxiv.org/html/2601.13435v1#S5.SS1.SSS1 "V-A1 FIR Convolution Kernels and Classical Discrete–time Filters ‣ V-A Neural Wavelet Filters ‣ V Architecture ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization"), the convolution weights WW correspond to the impulse responses, whose discrete Fourier transform gives the frequency responses. Therefore, the rFFT of the filter parameters directly yields the spectrum on the grid

|  |  |  |
| --- | --- | --- |
|  | knfft,k∈[0,1,…,nfft2+1].\frac{k}{n\_{\mathrm{fft}}},\qquad k\in\Bigl[0,1,\ldots,\frac{n\_{\mathrm{fft}}}{2}+1\Bigr]. |  |

With hourly data, we set nfft=81n\_{\mathrm{fft}}=81 to cover month-level frequencies. We regularize the learnable filter bank in the frequency domain to encourage clear low-/high-pass separation and avoid degenerate solutions. Let |Glow|2:=∑ω|Glow​(ω)|2\lvert G\_{\text{low}}\rvert^{2}:=\sum\_{\omega}\lvert G\_{\text{low}}(\omega)\rvert^{2} and |Ghigh|2:=∑ω|Ghigh​(ω)|2\lvert G\_{\text{high}}\rvert^{2}:=\sum\_{\omega}\lvert G\_{\text{high}}(\omega)\rvert^{2} be the total spectral energies on a discrete grid ω∈[0,π]\omega\in[0,\pi]. We penalize out-of-band energy using a frequency-weighted power term with p=2p=2 in all experiments:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒl​o​w\displaystyle\mathcal{L}\_{low} | =∑ω(ω/π)p​|Glow​(ω)|2,\displaystyle=\sum\_{\omega}(\omega/\pi)^{p}\,\lvert G\_{\text{low}}(\omega)\rvert^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒh​i​g​h\displaystyle\mathcal{L}\_{high} | =∑ω(1−ω/π)p​|Ghigh​(ω)|2,\displaystyle=\sum\_{\omega}(1-\omega/\pi)^{p}\,\lvert G\_{\text{high}}(\omega)\rvert^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒo​v​e​r​l​a​p\displaystyle\mathcal{L}\_{overlap} | =|Glow|2⋅|Ghigh|2,\displaystyle=\lvert G\_{\text{low}}\rvert^{2}\cdot\lvert G\_{\text{high}}\rvert^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒp​a​r​s​e​v​a​l\displaystyle\mathcal{L}\_{parseval} | =(|Glow|2+|Ghigh|2−2)2.\displaystyle=\big(\lvert G\_{\text{low}}\rvert^{2}+\lvert G\_{\text{high}}\rvert^{2}-2\big)^{2}. |  |

To balance the two branches, we further impose an energy-ratio hinge loss. Define ρ\rho as following and penalize ρ\rho outside [ρmin,ρmax][\rho\_{\min},\rho\_{\max}]

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ=|Ghigh|2|Glow|2+ε,ℒr​a​t​i​o=max⁡(ρ−ρmax, 0)+max⁡(ρmin−ρ, 0).\begin{gathered}\rho=\frac{\lvert G\_{\text{high}}\rvert^{2}}{\lvert G\_{\text{low}}\rvert^{2}+\varepsilon},\\ \mathcal{L}\_{ratio}=\max\bigl(\rho-\rho\_{\max},\,0\bigr)+\max\bigl(\rho\_{\min}-\rho,\,0\bigr).\end{gathered} |  | (20) |

Finally, the neutal wavelet loss is a weighted sum

|  |  |  |
| --- | --- | --- |
|  | ℒw​a​v​e​l​e​t=λspec​(ℒl​o​w+ℒh​i​g​h)+ℒo​v​e​r​l​a​p+ℒp​a​r​s​e​v​a​l+ℒr​a​t​i​o,\mathcal{L}\_{wavelet}=\lambda\_{\mathrm{spec}}\bigl(\mathcal{L}\_{low}+\mathcal{L}\_{high}\bigr)+\mathcal{L}\_{overlap}+\mathcal{L}\_{parseval}+\mathcal{L}\_{ratio}, |  |

and the overall training objective is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒt​r​a​i​n=ℒt​r​a​d​e+ℒp​e​n​a​l​t​y+ℒs​h​a​r​p​e+ℒw​a​v​e​l​e​t.\mathcal{L}\_{train}=\mathcal{L}\_{trade}+\mathcal{L}\_{penalty}+\mathcal{L}\_{sharpe}+\mathcal{L}\_{wavelet}. |  | (21) |

### VI-B Validation Metric and Model Selection

We train the network by minimizing the loss in Eq. ([21](https://arxiv.org/html/2601.13435v1#S6.E21 "In VI-A7 Neural Wavelet Loss ‣ VI-A Loss Function Design ‣ VI Training Design ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")), but our goal is to maximize out-of-sample trading performance rather than validation cross-entropy. Using the probability-to-position rule in Eq. ([9](https://arxiv.org/html/2601.13435v1#S3.E9 "In III-E Position Rule Under a Fixed Risk Budget ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")), the cumulative strategy return on the validation set is

|  |  |  |
| --- | --- | --- |
|  | Rval=∑t∈𝒟valw~t​rt,R\_{\text{val}}=\sum\_{t\in\mathcal{D}\_{\text{val}}}\tilde{w}\_{t}r\_{t}, |  |

or, in the risk-adjusted setting, a Sharpe-like ratio computed from the sequence {w~t​rt}\{\tilde{w}\_{t}r\_{t}\}.

Crucially, LvalL\_{\text{val}} and RvalR\_{\text{val}} are not necessarily monotonic. The threshold-based decision rule in Eq. ([9](https://arxiv.org/html/2601.13435v1#S3.E9 "In III-E Position Rule Under a Fixed Risk Budget ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) can flip actions near boundaries with minimal change in LvalL\_{\text{val}} yet a large change in RvalR\_{\text{val}}. Moreover, cross-entropy weights samples roughly uniformly, whereas RvalR\_{\text{val}} is dominated by a small number of large moves: improving calibration on many small-return samples may reduce LvalL\_{\text{val}} with little impact on RvalR\_{\text{val}}, while better capturing large profitable moves can slightly worsen LvalL\_{\text{val}} but substantially improve RvalR\_{\text{val}}.

Therefore, we use soft-label cross-entropy as a differentiable surrogate for optimization, but perform early stopping and hyperparameter selection solely based on RvalR\_{\text{val}}. In practice, we select the checkpoint with the highest validation ROI, using LvalL\_{\text{val}} only as a diagnostic for optimization stability.

#### VI-B1 Regression Loss vs. Soft-label Loss

Motivated by the above discussion, we replace regression with a soft-label classification objective that focuses on return direction and economically relevant magnitude, while treating the output as a proxy for position.

With regression, the model minimizes Eq. ([14](https://arxiv.org/html/2601.13435v1#S6.E14 "In VI-A1 Drawbacks of Regression Losses ‣ VI-A Loss Function Design ‣ VI Training Design ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")) to predict the future log return. Trading then relies on a separate hand-designed mapping h:ℝ→[w~min,w~max]h:\mathbb{R}\!\to\![\tilde{w}\_{\min},\tilde{w}\_{\max}], such as the clamping rule in Eq. ([9](https://arxiv.org/html/2601.13435v1#S3.E9 "In III-E Position Rule Under a Fixed Risk Budget ‣ III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")), and sets w~t=h​(ℓt)\tilde{w}\_{t}=h(\ell\_{t}). As a result, LregL\_{\text{reg}} optimizes only return accuracy, whereas ROI/Sharpe depends on the untrained composite decision rule and can differ substantially even when LregL\_{\text{reg}} is similar.

To remove this layer, we form a soft target using a scaled sigmoid,

|  |  |  |
| --- | --- | --- |
|  | yt=σ​(k​ℓ^t),y\_{t}=\sigma(k\,\hat{\ell}\_{t}), |  |

where k>0k>0 controls saturation. The network outputs a logit ptp\_{t} with Pt=σ​(pt)P\_{t}=\sigma(p\_{t}) and is trained with soft-label cross-entropy. At inference, we convert ptp\_{t} to an executable position using the same squashing and risk-budget mapping described in Section [III](https://arxiv.org/html/2601.13435v1#S3 "III Problem formulation ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization"), so the optimized scalar becomes the trading signal up to a fixed monotone transform.

Soft labels offer three advantages: they penalize sign errors on large moves more than small deviations, learn a decision signal rather than a return forecast, and integrate naturally with the Sharpe-oriented regularizer in Section [VI-A](https://arxiv.org/html/2601.13435v1#S6.SS1 "VI-A Loss Function Design ‣ VI Training Design ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization").

Table [II](https://arxiv.org/html/2601.13435v1#S6.T2 "TABLE II ‣ VI-B1 Regression Loss vs. Soft-label Loss ‣ VI-B Validation Metric and Model Selection ‣ VI Training Design ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization") shows Renewable Energy results with identical architecture and optimization. We disable the Sharpe regularizer and only change the supervised loss (MSE, MAE, or soft-label). The soft-label objective yields higher ROI and Sharpe than regression despite comparable error on ℓt\ell\_{t}, supporting soft-label training for trading signals.

TABLE II: Comparison of regression losses and soft-label loss on Renewable Energy with 10 seeds. All models share the same WaveLSFormer architecture and optimization setup, the Sharpe regularizer is disabled for all rows to isolate the effect of the supervised loss.

|  |  |  |
| --- | --- | --- |
| Loss | ROI (test) | Sharpe (test) |
| MSE | 0.078±0.0390.078\pm 0.039 | 0.586±0.2750.586\pm 0.275 |
| MAE | 0.125±0.0610.125\pm 0.061 | 0.899±0.3550.899\pm 0.355 |
| Soft-label | 0.377±0.0450.377\pm 0.045 | 1.943±0.3111.943\pm 0.311 |

#### VI-B2 Tanh Loss vs. Soft-label Loss

We observed that optimizing Transformers for U.S. equity trading is highly sensitive to the loss design. When using the tanh-based objective in Eq. ([15](https://arxiv.org/html/2601.13435v1#S6.E15 "In VI-A2 Stock Direction and Tanh Position Loss ‣ VI-A Loss Function Design ‣ VI Training Design ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")), training often stagnates because the tanh nonlinearity saturates, producing near-zero gradients and effectively “deadlocking” the optimizer. We diagnosed this behavior by monitoring the ℓ2\ell\_{2} norm of parameter gradients, which frequently collapsed toward zero, and found that an overly small initial learning rate further increases the likelihood of getting trapped in poor local optima.
However, the soft-label loss overcomes this drawback and produces a stable training process.

![Refer to caption](images/gradient_vanish.png)


(a) Tanh loss function leads to gradient vanishing.

![Refer to caption](x1.png)


(b) Soft-label loss function has stable and continuous gradients.

Figure 3: Loss curve and gradient of tanh and soft-label loss functions

## VII Experiment

### VII-A Experiment Setup

#### VII-A1 Data Split and Leakage Prevention

We use five years of hourly U.S. equity data from 29.10.2020 to 29.10.2025 and adopt a temporal 70%/10%/20% split for training, validation, and test, corresponding to 5292, 756, and 1512 time steps.
Due to limited computational resources, hyperparameters are tuned manually.

To prevent leakage, all preprocessing is computed on the training period only, including industry selection by an ARR threshold, DTW-based similarity filtering, and Granger-causality filtering with BH-FDR correction.
All models use identical per-industry datasets produced by this training-only pipeline.
For efficiency, Transformer-based variants use ProbSparse attention with distillation.

#### VII-A2 Implementation and Model Selection

After forming industry-level asset groups, we compare WaveLSFormer against two baselines, LSTM and MLP.
Unless otherwise stated, WaveLSFormer uses dmodel=512d\_{\text{model}}=512, dff=1024d\_{\text{ff}}=1024, 6 encoder layers with nheads=128n\_{\text{heads}}=128, input length 96, and a 128-dimensional time2vec temporal embedding.

Each model is trained with ten random seeds for 80 epochs using batch size 256 and learning rate 10−510^{-5}.
We adopt a two-phase schedule for the neural wavelet front-end: the first 30 epochs stabilize the learnable filters under spectral regularization, and the remaining epochs select checkpoints by validation trading metrics.
For each seed, we choose the checkpoint with the highest validation ROI in the second phase and evaluate it on the test set.
We report mean±\pmstd across the ten runs, and all results are computed on the held-out test set.

### VII-B Model Performance

Among 14 candidate industries in Table [III](https://arxiv.org/html/2601.13435v1#S7.T3 "TABLE III ‣ VII-B Model Performance ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization"), we compute the industry-level annualized rate of return (ARR) of an intraday trading strategy using the training period only and retain industries with ARR ≥10%\geq 10\%. The selected set is then fixed for all subsequent experiments to avoid leakage and to focus on sectors where intraday trading is potentially profitable and sufficiently liquid. This procedure selects six industries, and we focus on Renewable Energy and Retail Consumer Goods for detailed analysis.

TABLE III: Industry-level annualized rate of return (ARR) used for sector selection. Industries with ARR ≥10%\geq 10\% are retained for subsequent experiments.

|  |  |  |
| --- | --- | --- |
| Industry | ARR (%) | Selected |
| Biotechnology | 33.98505 | Yes |
| Regional Banks | 5.706405 | No |
| Engineering Construction | 8.208481 | No |
| Electronic Components | 8.899873 | No |
| Information Technology Services | 8.718001 | No |
| Medical Devices | 12.48685 | Yes |
| Semiconductors | 14.11355 | Yes |
| Software Application | 7.635932 | No |
| Specialty Industrial Machinery | 4.412272 | No |
| Utilities Electric | 4.132072 | No |
| Real Estate REITs | 2.451229 | No |
| Renewable Energy | 10.14711 | Yes |
| Life Insurance | 12.77445 | Yes |
| Retail Consumer Goods | 11.83257 | Yes |

For each selected industry, the constituent stocks are fed into the model following the pipeline described above. During training, we choose the model checkpoint that achieves the highest return on the validation set. For evaluation, we report trading performance under three execution modes: (i) Long & Short, (ii) Long Only, and (iii) Short Only. These three modes jointly reflect the model’s ability to exploit both upward and downward price movements. Additional per-industry trading performance curves are provided in the supplementary material, Figs. S1-S4.

![Refer to caption](images/renewable_energy_trading_performance.png)


Figure 4: Strategy return curve of renewable energy

![Refer to caption](images/Retail_ConsumerGoods_trading_performance.png)


Figure 5: Strategy return curve of retail consumer goods

### VII-C Hyperparameter Sensitivity Analysis

#### VII-C1 λroi\lambda\_{\mathrm{roi}} in Overfitting Penalty

The hyperparameter λROI\lambda\_{\text{ROI}} controls the strength of the ROI-aware penalty and thus how aggressively the model is encouraged to maximize profit during training: small values make the constraint nearly inactive, whereas large values strongly discourage ROI-constraint violations.

To analyze its effect, we sweep

|  |  |  |
| --- | --- | --- |
|  | λroi∈{0.0,0.1,0.3,0.5,0.7,1.0,1.2},\lambda\_{\mathrm{roi}}\in\{0.0,0.1,0.3,0.5,0.7,1.0,1.2\}, |  |

train the model under the same configuration for each setting, and record the final training ROI over the full 4-year horizon together with the corresponding val ROI and Sharpe ratio. Results are shown in Fig. [6](https://arxiv.org/html/2601.13435v1#S7.F6 "Figure 6 ‣ VII-C1 𝜆ᵣₒᵢ in Overfitting Penalty ‣ VII-C Hyperparameter Sensitivity Analysis ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization").

We observe a clear dependence on λroi\lambda\_{\mathrm{roi}}. Too small a value yields weak regularization and overly aggressive policies that can produce inflated training ROI, while too large a value makes training overly conservative and substantially reduces ROI. In a mid-range of λroi\lambda\_{\mathrm{roi}}, training ROI stabilizes around 6 over the 4-year horizon and val ROI/Sharpe achieve their best values, which we adopt as a stable operating regime.

![Refer to caption](images/lambda_roi_val.png)


Figure 6: Sensitivity of cumulative ROI to the ROI-aware penalty coefficient λroi\lambda\_{\mathrm{roi}} on the Renewable Energy industry.
The left yy-axis shows training cumulative ROI over the training horizon, and the right yy-axis shows validation ROI and Sharpe.
All values are reported as mean±\pmstd over ten random seeds.

#### VII-C2 γ\gamma in Low-guided High-frequency Injection

This subsection analyzes the scalar gate that controls the strength of LGHI. Empirically, overly large gate values cause vanishing gradients for LSTM backbones and exploding gradients for Transformer backbones, motivating a small-gate initialization.

Let Lt∈ℝdL\_{t}\in\mathbb{R}^{d} be the low-frequency representation at time tt and HtH\_{t} the corresponding high-frequency input. LGHI produces a refinement Zt​(Lt,Ht)∈ℝdZ\_{t}(L\_{t},H\_{t})\in\mathbb{R}^{d}, and the fused output follows Eq. ([13](https://arxiv.org/html/2601.13435v1#S5.E13 "In V-A3 Low-guided High-frequency Injection ‣ V-A Neural Wavelet Filters ‣ V Architecture ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization")). Here, γ\gamma is a learnable scalar and β=σ​(γ)∈(0,1)\beta=\sigma(\gamma)\in(0,1) controls the overall contribution of LGHI: β≈0\beta\approx 0 yields an almost purely low-frequency representation, while β≈1\beta\approx 1 heavily relies on the high-frequency refinement.

The gate scales not only the forward contribution but also the backward signal to LGHI parameters θZ\theta\_{Z}. By the chain rule,

|  |  |  |
| --- | --- | --- |
|  | ∂ℒ∂θZ=∂ℒ∂Yt​∂Yt∂Zt​∂Zt∂θZ=β​∂ℒ∂Yt​∂Zt∂θZ,\frac{\partial\mathcal{L}}{\partial\theta\_{Z}}=\frac{\partial\mathcal{L}}{\partial Y\_{t}}\,\frac{\partial Y\_{t}}{\partial Z\_{t}}\,\frac{\partial Z\_{t}}{\partial\theta\_{Z}}=\beta\,\frac{\partial\mathcal{L}}{\partial Y\_{t}}\,\frac{\partial Z\_{t}}{\partial\theta\_{Z}}, |  |

where ℒ\mathcal{L} denotes the training objective. Thus, larger β\beta linearly amplifies gradients w.r.t. θZ\theta\_{Z}, while also increasing the scale of YtY\_{t} fed into the backbone.

Effect with LSTM backbones
With an LSTM backbone, YtY\_{t} enters recurrent transitions whose gates use sigmoid and tanh\tanh. As β\beta increases, the magnitude of YtY\_{t} tends to grow, pushing gate pre-activations into saturation where σ′​(x)\sigma^{\prime}(x) and 1−tanh2⁡(x)1-\tanh^{2}(x) become small. Consequently, the recurrent-step Jacobian tends to have a spectral radius below 11, and the backpropagated gradients decay through time:

|  |  |  |
| --- | --- | --- |
|  | ∂ℒ∂(ht,ct)=(∏k=tT−1Jk)​∂ℒ∂(hT,cT),\frac{\partial\mathcal{L}}{\partial(h\_{t},c\_{t})}=\Bigg(\prod\_{k=t}^{T-1}J\_{k}\Bigg)\frac{\partial\mathcal{L}}{\partial(h\_{T},c\_{T})}, |  |

leading to vanishing gradients and early training plateaus for moderately large β\beta.

Effect with Transformer backbones
In contrast, a Transformer backbone forms a deep stack of residual blocks with Layer Normalization:

|  |  |  |
| --- | --- | --- |
|  | X(ℓ+1)=LN​(X(ℓ)+F(ℓ)​(X(ℓ))).X^{(\ell+1)}=\mathrm{LN}\bigl(X^{(\ell)}+F^{(\ell)}(X^{(\ell)})\bigr). |  |

A first-order approximation yields a layer Jacobian of the form

|  |  |  |
| --- | --- | --- |
|  | J(ℓ)≈I+β​J~(ℓ).J^{(\ell)}\approx I+\beta\,\tilde{J}^{(\ell)}. |  |

Thus, increasing β\beta raises the effective layer-wise gain, and the backward signal can grow through the product of Jacobians:

|  |  |  |
| --- | --- | --- |
|  | ∂ℒ∂X(0)=(∏ℓ=0L−1J(ℓ))​∂ℒ∂X(L),\frac{\partial\mathcal{L}}{\partial X^{(0)}}=\Bigg(\prod\_{\ell=0}^{L-1}J^{(\ell)}\Bigg)\frac{\partial\mathcal{L}}{\partial X^{(L)}}, |  |

which may cause exploding gradients when the spectral radius exceeds 11 across many layers. In our experiments, setting β∈{0.01,0.1,0.5,1.0}\beta\in\{0.01,0.1,0.5,1.0\} shows stable training for small/moderate gates, while β=0.5\beta=0.5 and β=1.0\beta=1.0 quickly become numerically unstable as shown in Fig. [7](https://arxiv.org/html/2601.13435v1#S7.F7 "Figure 7 ‣ VII-C2 𝛾 in Low-guided High-frequency Injection ‣ VII-C Hyperparameter Sensitivity Analysis ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization").

![Refer to caption](x2.png)


Figure 7: Effect of the LGHI module β\beta on training loss and gradient norms for Transformer backbones. Curves correspond to β=0.01\beta=0.01 (red), β=0.1\beta=0.1 (black), β=0.5\beta=0.5 (green), and β=1.0\beta=1.0 (orange).

Initialization strategy
Across backbones, overly large gates can stall optimization by saturating LSTM gates and causing vanishing gradients, or by over-amplifying deep residual stacks in Transformers and triggering exploding gradients. Therefore, we initialize β\beta to a very small value so that LGHI starts as a weak perturbation of the low-frequency path. Specifically, we parameterize β=σ​(γ)\beta=\sigma(\gamma) and initialize γ=−5\gamma=-5, yielding β0=σ​(−5)≈0.0067\beta\_{0}=\sigma(-5)\approx 0.0067. This keeps the mapping close to the identity at initialization and avoids both LSTM saturation and excessive amplification in deep Transformer stacks. Since γ\gamma is learnable, the optimizer can increase β\beta when the refinement Zt​(Lt,Ht)Z\_{t}(L\_{t},H\_{t}) is beneficial; otherwise, β\beta remains small and the model behaves close to a purely low-frequency baseline.

#### VII-C3 λspec\lambda\_{\mathrm{spec}} in Neural Wavelet Loss

The hyperparameter λspec\lambda\_{\mathrm{spec}} weights the spectral-shaping term in the wavelet loss.
Smaller values relax frequency-domain constraints and allow more task-driven filters, while larger values enforce cleaner low-/high-pass behavior but can reduce flexibility.

We sweep

|  |  |  |
| --- | --- | --- |
|  | λspec∈{0, 0.3, 1, 3, 10, 30, 100},\lambda\_{\mathrm{spec}}\in\{0,\ 0.3,\ 1,\ 3,\ 10,\ 30,\ 100\}, |  |

keeping all other settings fixed, and evaluate validation ROI and Sharpe.
Fig. [8](https://arxiv.org/html/2601.13435v1#S7.F8 "Figure 8 ‣ VII-C3 𝜆_spec in Neural Wavelet Loss ‣ VII-C Hyperparameter Sensitivity Analysis ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization") summarizes the results on Renewable Energy.
We select λspec\lambda\_{\mathrm{spec}} using validation performance to avoid test-set leakage, and report test results with the selected value in the main results section.

![Refer to caption](images/lambda_spec_val.png)


Figure 8: Validation-set sensitivity of λspec\lambda\_{\mathrm{spec}} in the wavelet loss on the Renewable Energy industry. Bars report validation ROI on the left yy-axis, and the dashed line reports validation Sharpe ratio on the right yy-axis. All values are reported as mean±\pmstd over ten random seeds.

Overall, performance peaks in a moderate range.
Too small λspec\lambda\_{\mathrm{spec}} weakens spectral shaping and can yield less stable filters, while too large λspec\lambda\_{\mathrm{spec}} over-regularizes optimization and degrades ROI and Sharpe.
We use λspec=10\lambda\_{\mathrm{spec}}=10 as the default unless otherwise stated.

### VII-D Ablation Study

#### VII-D1 Effect of Learnable Wavelet Filters

We evaluate the proposed neural wavelet layer by replacing fixed filters in the same Transformer backbone. We compare three front-ends: (i) *Neural Wavelet*, which learns the filters jointly with the trading objective using Parseval, overlap, and pass-band regularizers; (ii) *Classic Wavelet*, a fixed wavelet transform; and (iii) *Transformer only*, which uses raw price features. As shown in Table [IV](https://arxiv.org/html/2601.13435v1#S7.T4 "TABLE IV ‣ VII-D1 Effect of Learnable Wavelet Filters ‣ VII-D Ablation Study ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization"), Neural Wavelet attains the best test ROI and Sharpe in almost all industries under matched capacity, and also yields smaller maximum draw-down and more stable performance across seeds, indicating that learnable, regularized wavelet filters extract more tradable signals than fixed transforms or no decomposition.

TABLE IV: Multi-seed, multi-industry comparison of Transformer-based backbones with different front-ends. Results are reported as mean ±\pm std over ten seeds. Best results in each row are highlighted in red.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Industry | Metric | Neural wavelet  Transformer | Classic wavelet  Transformer | Plain  Transformer |
| Biotechnology | ROI | 0.601 ±\pm 0.034 | 0.323 ±\pm 0.021 | 0.124 ±\pm 0.066 |
| Sharpe | 1.695 ±\pm 0.050 | 1.086 ±\pm 0.048 | 0.511 ±\pm 0.189 |
| Semiconductors | ROI | 1.104 ±\pm 0.053 | 0.416 ±\pm 0.021 | 0.333 ±\pm 0.021 |
| Sharpe | 2.555 ±\pm 0.081 | 1.293 ±\pm 0.071 | 1.134 ±\pm 0.035 |
| Renewable  Energy | ROI | 0.423 ±\pm 0.074 | 0.261 ±\pm 0.033 | 0.169 ±\pm 0.018 |
| Sharpe | 2.775 ±\pm 0.365 | 1.723 ±\pm 0.161 | 1.173 ±\pm 0.113 |
| Life  Insurance | ROI | 0.185 ±\pm 0.004 | 0.144 ±\pm 0.004 | 0.120 ±\pm 0.010 |
| Sharpe | 1.472 ±\pm 0.039 | 1.206 ±\pm 0.027 | 0.976 ±\pm 0.086 |
| Medical  Devices | ROI | 0.669 ±\pm 0.049 | 0.462 ±\pm 0.067 | 0.289 ±\pm 0.036 |
| Sharpe | 1.979 ±\pm 0.167 | 1.475 ±\pm 0.178 | 1.060 ±\pm 0.125 |
| Retail Consumer  Goods | ROI | 0.659 ±\pm 0.055 | 0.468 ±\pm 0.143 | 0.317 ±\pm 0.187 |
| Sharpe | 2.465 ±\pm 0.293 | 1.850 ±\pm 0.132 | 1.291 ±\pm 0.185 |
| Overall (avg.) | ROI | 0.607 ±\pm 0.045 | 0.346 ±\pm 0.048 | 0.225 ±\pm 0.056 |
| Sharpe | 2.157 ±\pm 0.166 | 1.439 ±\pm 0.103 | 1.024 ±\pm 0.122 |

#### VII-D2 Effect of Using Only a Single Frequency Branch

We evaluate whether both frequency branches are necessary by comparing the full model (Low+High) with two ablations: *Low-Freq only* and *High-Freq only*. Table [V](https://arxiv.org/html/2601.13435v1#S7.T5 "TABLE V ‣ VII-D2 Effect of Using Only a Single Frequency Branch ‣ VII-D Ablation Study ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization") shows that removing either branch consistently hurts performance. Across most industries, *Low-Freq only* outperforms *High-Freq only* in ROI and Sharpe, indicating that slowly varying trends are more informative than high-frequency residuals alone. However, Low+High achieves the best average ROI/Sharpe with lower seed variance, suggesting that the high-frequency branch provides complementary short-term refinements, whereas relying solely on high-frequency signals reduces mean performance and increases training instability.

TABLE V: Effect of two frequency branches. Results are mean ±\pm std over ten seeds. Best in each row is red.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Industry | Metric | Full  Low+High | Only  Low-Freq | Only  High-Freq |
| Biotechnology | ROI | 0.601 ±\pm 0.034 | 0.305 ±\pm 0.028 | 0.133 ±\pm 0.050 |
| Sharpe | 1.695 ±\pm 0.050 | 0.902 ±\pm 0.117 | 0.429 ±\pm 0.185 |
| Semiconductors | ROI | 1.104 ±\pm 0.053 | 0.561 ±\pm 0.052 | 0.244 ±\pm 0.092 |
| Sharpe | 2.555 ±\pm 0.081 | 1.360 ±\pm 0.176 | 0.646 ±\pm 0.279 |
| Renewable  Energy | ROI | 0.423 ±\pm 0.074 | 0.225 ±\pm 0.021 | 0.098 ±\pm 0.037 |
| Sharpe | 2.775 ±\pm 0.365 | 1.477 ±\pm 0.191 | 0.702 ±\pm 0.303 |
| Life  Insurance | ROI | 0.185 ±\pm 0.004 | 0.094 ±\pm 0.009 | 0.041 ±\pm 0.015 |
| Sharpe | 1.472 ±\pm 0.039 | 0.783 ±\pm 0.101 | 0.372 ±\pm 0.161 |
| Medical  Devices | ROI | 0.669 ±\pm 0.049 | 0.340 ±\pm 0.032 | 0.148 ±\pm 0.056 |
| Sharpe | 1.979 ±\pm 0.167 | 1.053 ±\pm 0.136 | 0.501 ±\pm 0.216 |
| Retail Consumer  Goods | ROI | 0.659 ±\pm 0.055 | 0.334 ±\pm 0.165 | 0.145 ±\pm 0.286 |
| Sharpe | 2.465 ±\pm 0.293 | 1.312 ±\pm 0.161 | 0.624 ±\pm 0.329 |
| Overall (avg.) | ROI | 0.607 ±\pm 0.045 | 0.310 ±\pm 0.051 | 0.135 ±\pm 0.089 |
| Sharpe | 2.157 ±\pm 0.166 | 1.148 ±\pm 0.147 | 0.546 ±\pm 0.246 |

#### VII-D3 Low-guided High-frequency Injection

We further examine how the low and high frequency branches should be fused. In the proposed design, the low-frequency representation attends to the high-frequency branch via a LGHI block. As a comparison, we remove the LGHI module and simply concatenate the two branches followed by a linear projection, while keeping the overall model size comparable. The multi-industry, multi-seed results are reported in Table [VI](https://arxiv.org/html/2601.13435v1#S7.T6 "TABLE VI ‣ VII-D3 Low-guided High-frequency Injection ‣ VII-D Ablation Study ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization").

TABLE VI: LGHI module vs simple concatenation. Results are mean ±\pm std over ten seeds. Best in each row is red.

|  |  |  |  |
| --- | --- | --- | --- |
| Industry | Metric | LGHI | Concat |
| Biotechnology | ROI | 0.601 ±\pm 0.034 | 0.203 ±\pm 0.037 |
| Sharpe | 1.695 ±\pm 0.050 | 0.640 ±\pm 0.040 |
| Semiconductors | ROI | 1.104 ±\pm 0.053 | 0.374 ±\pm 0.022 |
| Sharpe | 2.555 ±\pm 0.081 | 0.964 ±\pm 0.060 |
| Renewable Energy | ROI | 0.423 ±\pm 0.074 | 0.150 ±\pm 0.035 |
| Sharpe | 2.775 ±\pm 0.365 | 1.047 ±\pm 0.165 |
| Life Insurance | ROI | 0.185 ±\pm 0.004 | 0.063 ±\pm 0.012 |
| Sharpe | 1.472 ±\pm 0.039 | 0.555 ±\pm 0.034 |
| Medical Devices | ROI | 0.669 ±\pm 0.049 | 0.227 ±\pm 0.028 |
| Sharpe | 1.979 ±\pm 0.167 | 0.747 ±\pm 0.076 |
| Retail Consumer Goods | ROI | 0.659 ±\pm 0.055 | 0.222 ±\pm 0.154 |
| Sharpe | 2.465 ±\pm 0.293 | 0.930 ±\pm 0.130 |
| Overall (avg.) | ROI | 0.607 ±\pm 0.045 | 0.207 ±\pm 0.048 |
| Sharpe | 2.157 ±\pm 0.166 | 0.814 ±\pm 0.083 |

Across all industry groups, the LGHI design consistently outperforms simple concatenation in terms of both ROI and Sharpe ratio, and also exhibits smaller variance across seeds on average. This confirms that allowing the low-frequency branch to selectively attend to high-frequency details is more effective than treating the two branches as independent features.

#### VII-D4 Sharpe Regularizer Ablation

To quantify the benefit of explicitly optimizing a trading-oriented objective, we ablate the Sharpe loss term by training two WaveLSFormer variants with identical architectures, optimization settings, and data splits: (i) Soft-label only and (ii) Soft-label with a Sharpe loss computed from per-step P&L.
For each industry and seed, both variants share the same training schedule and differ only in whether the Sharpe term is included.
Table [VII](https://arxiv.org/html/2601.13435v1#S7.T7 "TABLE VII ‣ VII-D4 Sharpe Regularizer Ablation ‣ VII-D Ablation Study ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization") reports industry-level test metrics averaged over 10 seeds with checkpoints selected by validation ROI. Adding the Sharpe loss improves risk-adjusted performance and often increases ROI while reducing maximum draw-down, suggesting that prediction-only training is insufficient and that directly regularizing the mean-volatility trade-off yields more favorable risk-return profiles.

Beyond ROI and Sharpe ratio, we report maximum draw-down (MDD) on the test set as a complementary risk measure.
Let WtW\_{t} denote the cumulative wealth process. The draw-down at time tt and the maximum draw-down over the test period are

|  |  |  |
| --- | --- | --- |
|  | Dt=1−Wtmaxs≤t⁡Ws,MDD=maxt⁡Dt.D\_{t}=1-\frac{W\_{t}}{\max\_{s\leq t}W\_{s}},\qquad\mathrm{MDD}=\max\_{t}D\_{t}. |  |

![Refer to caption](images/renewable_energy_wo_sharpe.png)


Figure 9: Equity curves with and without the Sharpe loss for Renewable Energy. Top: cumulative ROI on validation and test. Bottom: cumulative market return. The model without Sharpe loss (red) shows deeper and more frequent test draw-downs, whereas the Sharpe-aware model (orange) produces a smoother equity curve with smaller draw-downs at a similar final ROI, reflecting more conservative exposure in risky periods.




TABLE VII: Sharpe loss ablation by industry on the test set. Results are reported as mean ±\pm standard deviation over 10 random seeds for ROI, Sharpe ratio and maximum draw-down (MDD, %).

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Industry | Soft-label only | | | Soft-label + Sharpe (ours) | | |
| ROI | Sharpe | MDD (%) | ROI | Sharpe | MDD (%) |
| Biotechnology | 0.511 ±\pm 0.061 | 1.187 ±\pm 0.190 | 17.203 ±\pm 2.962 | 0.601 ±\pm 0.034 | 1.695 ±\pm 0.050 | 10.658 ±\pm 1.932 |
| Semiconductors | 0.938 ±\pm 0.113 | 1.789 ±\pm 0.286 | 11.413 ±\pm 1.965 | 1.104 ±\pm 0.053 | 2.555 ±\pm 0.081 | 7.071 ±\pm 1.282 |
| Renewable Energy | 0.377 ±\pm 0.045 | 1.943 ±\pm 0.311 | 10.508 ±\pm 1.809 | 0.443 ±\pm 0.064 | 2.775 ±\pm 0.365 | 6.510 ±\pm 1.180 |
| Life Insurance | 0.157 ±\pm 0.019 | 1.030 ±\pm 0.165 | 19.810 ±\pm 3.410 | 0.185 ±\pm 0.004 | 1.472 ±\pm 0.039 | 12.273 ±\pm 2.225 |
| Medical Devices | 0.569 ±\pm 0.068 | 1.385 ±\pm 0.222 | 14.735 ±\pm 2.537 | 0.669 ±\pm 0.049 | 1.979 ±\pm 0.167 | 9.128 ±\pm 1.655 |
| Retail Consumer Goods | 0.267 ±\pm 0.032 | 1.068 ±\pm 0.171 | 19.109 ±\pm 3.290 | 0.659 ±\pm 0.055 | 2.465 ±\pm 0.293 | 11.838 ±\pm 2.146 |
| Overall (avg.) | 0.470 ±\pm 0.056 | 1.400 ±\pm 0.224 | 15.463 ±\pm 2.662 | 0.553 ±\pm 0.035 | 2.000 ±\pm 0.122 | 9.580 ±\pm 1.736 |

### VII-E Baseline Model Comparisons

#### VII-E1 Per-Industry Performance

We compare MLP, LSTM, and Transformer backbones with and without the neural wavelet front-end, using dmodel=512d\_{\text{model}}=512 for all models.
WaveLSFormer uses dff=1024d\_{\text{ff}}=1024, nheads=128n\_{\text{heads}}=128, L=6L=6 encoder layers, sequence length 9696, temporal embedding dimension 128128, and pre-layer normalization.
The MLP baseline has 10 fully connected layers with 512 hidden units, and the LSTM baseline uses a 2-layer LSTM with 512 hidden units.
We report mean±\pmstd over ten random seeds and synchronize stochastic components across models for fair comparison.

Table [VIII](https://arxiv.org/html/2601.13435v1#S7.T8 "TABLE VIII ‣ VII-E1 Per-Industry Performance ‣ VII-E Baseline Model Comparisons ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization") reports test ROI and Sharpe by industry and on average.
The wavelet front-end improves both metrics for every backbone, and LSTM-based models consistently outperform MLP, consistent with prior evidence that recurrent and attention architectures better capture long-range dependencies and regime shifts in financial time series [[16](https://arxiv.org/html/2601.13435v1#bib.bib16), [17](https://arxiv.org/html/2601.13435v1#bib.bib17), [18](https://arxiv.org/html/2601.13435v1#bib.bib18), [24](https://arxiv.org/html/2601.13435v1#bib.bib24), [23](https://arxiv.org/html/2601.13435v1#bib.bib23)].
Overall, WaveLSFormer achieves the best performance with a parameter budget comparable to LSTM variants, reaching 0.607±0.0450.607\pm 0.045 ROI and 2.157±0.1662.157\pm 0.166 Sharpe, compared with 0.225±0.0560.225\pm 0.056 ROI and 1.024±0.1221.024\pm 0.122 Sharpe for the plain Transformer.
Fig. [10](https://arxiv.org/html/2601.13435v1#S7.F10 "Figure 10 ‣ VII-E1 Per-Industry Performance ‣ VII-E Baseline Model Comparisons ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization") shows consistent gains across industries, and Fig. [11](https://arxiv.org/html/2601.13435v1#S7.F11 "Figure 11 ‣ VII-E1 Per-Industry Performance ‣ VII-E Baseline Model Comparisons ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization") shows smoother equity growth with smaller draw-downs than the strongest non-wavelet baselines in Renewable Energy and Retail Consumer Goods.

TABLE VIII: Per-industry comparison of MLP, LSTM and Transformer backbones with and without the wavelet front-end. Results are mean ±\pm std over ten seeds. The best in each row is red.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Industry | Metric | MLP | Wav.+MLP | LSTM | Wav.+LSTM | Trans. | Wav.+Trans. |
| Biotechnology | ROI | 0.041±0.0130.041\pm 0.013 | 0.092±0.0240.092\pm 0.024 | 0.106±0.0160.106\pm 0.016 | 0.173±0.0260.173\pm 0.026 | 0.124±0.0660.124\pm 0.066 | 0.601±0.0340.601\pm 0.034 |
| Sharpe | 0.405±0.1570.405\pm 0.157 | 0.553±0.0740.553\pm 0.074 | 0.823±0.2420.823\pm 0.242 | 0.934±0.1020.934\pm 0.102 | 0.511±0.1890.511\pm 0.189 | 1.695±0.0501.695\pm 0.050 |
| Semiconductors | ROI | 0.110±0.0350.110\pm 0.035 | 0.246±0.0640.246\pm 0.064 | 0.285±0.0430.285\pm 0.043 | 0.465±0.0690.465\pm 0.069 | 0.333±0.0210.333\pm 0.021 | 1.104±0.0531.104\pm 0.053 |
| Sharpe | 0.899±0.3490.899\pm 0.349 | 1.227±0.1641.227\pm 0.164 | 1.826±0.5371.826\pm 0.537 | 2.072±0.2272.072\pm 0.227 | 1.134±0.0351.134\pm 0.035 | 2.555±0.0812.555\pm 0.081 |
| Renewable Energy | ROI | 0.053±0.0200.053\pm 0.020 | 0.139±0.0130.139\pm 0.013 | 0.159±0.0170.159\pm 0.017 | 0.221±0.0220.221\pm 0.022 | 0.169±0.0180.169\pm 0.018 | 0.423±0.0740.423\pm 0.074 |
| Sharpe | 0.851±0.4310.851\pm 0.431 | 1.490±0.0541.490\pm 0.054 | 1.482±0.3661.482\pm 0.366 | 1.656±0.0611.656\pm 0.061 | 1.173±0.1131.173\pm 0.113 | 2.775±0.3652.775\pm 0.365 |
| Life Insurance | ROI | 0.040±0.0130.040\pm 0.013 | 0.089±0.0230.089\pm 0.023 | 0.103±0.0150.103\pm 0.015 | 0.168±0.0250.168\pm 0.025 | 0.120±0.0100.120\pm 0.010 | 0.185±0.0040.185\pm 0.004 |
| Sharpe | 0.774±0.3010.774\pm 0.301 | 1.056±0.1411.056\pm 0.141 | 1.572±0.4621.572\pm 0.462 | 1.783±0.1951.783\pm 0.195 | 0.976±0.0860.976\pm 0.086 | 1.472±0.0391.472\pm 0.039 |
| Medical Devices | ROI | 0.095±0.0300.095\pm 0.030 | 0.214±0.0560.214\pm 0.056 | 0.248±0.0370.248\pm 0.037 | 0.404±0.0600.404\pm 0.060 | 0.289±0.0360.289\pm 0.036 | 0.669±0.0490.669\pm 0.049 |
| Sharpe | 0.840±0.3270.840\pm 0.327 | 0.995±0.1330.995\pm 0.133 | 1.707±0.5021.707\pm 0.502 | 1.937±0.2121.937\pm 0.212 | 1.060±0.1251.060\pm 0.125 | 1.979±0.1671.979\pm 0.167 |
| Retail Consumer Goods | ROI | 0.110±0.0280.110\pm 0.028 | 0.208±0.0890.208\pm 0.089 | 0.245±0.0470.245\pm 0.047 | 0.471±0.0930.471\pm 0.093 | 0.317±0.1870.317\pm 0.187 | 0.659±0.0550.659\pm 0.055 |
| Sharpe | 1.110±0.3011.110\pm 0.301 | 1.154±0.2671.154\pm 0.267 | 2.527±0.8622.527\pm 0.862 | 2.895±0.5282.895\pm 0.528 | 1.291±0.1851.291\pm 0.185 | 2.465±0.2932.465\pm 0.293 |
| Overall (avg.) | ROI | 0.075±0.0230.075\pm 0.023 | 0.165±0.0450.165\pm 0.045 | 0.191±0.0290.191\pm 0.029 | 0.317±0.0490.317\pm 0.049 | 0.225±0.0560.225\pm 0.056 | 0.607±0.0450.607\pm 0.045 |
| Sharpe | 0.813±0.3110.813\pm 0.311 | 1.079±0.1391.079\pm 0.139 | 1.656±0.4951.656\pm 0.495 | 1.879±0.2211.879\pm 0.221 | 1.024±0.1221.024\pm 0.122 | 2.157±0.1662.157\pm 0.166 |

![Refer to caption](images/backbone_bar.png)


Figure 10: Per-industry ROI (a) and Sharpe ratio (b) for MLP, LSTM, and Transformer backbones with and without the neural wavelet front-end. Bars show mean over ten seeds and error bars denote one standard deviation, including six industries and the overall average.



![Refer to caption](images/equity_renewable_energy_backbones.png)


(a) Renewable Energy

![Refer to caption](images/equity_retail_consumer_goods_backbones.png)


(b) Retail Consumer Goods

Figure 11: Equity curves on the test period for (a) Renewable Energy and (b) Retail Consumer Goods. For each sector we compare the non-wavelet MLP and LSTM, the wavelet-enhanced MLP and LSTM, and WaveLSFormer.

#### VII-E2 Model Complexity and Overall Performance

Table [IX](https://arxiv.org/html/2601.13435v1#S7.T9 "TABLE IX ‣ VII-E2 Model Complexity and Overall Performance ‣ VII-E Baseline Model Comparisons ‣ VII Experiment ‣ A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization") reports model complexity and trading performance for each backbone with and without the neural wavelet front-end.
MLP is a lightweight reference with 8.1468.146M parameters and 3.4683.468G FLOPs, while LSTM and Transformer are substantially more expensive at 12.53812.538M/492.614492.614G and 15.92815.928M/665.921665.921G.
To rule out brute-force scaling, we report parameters and FLOPs for paired comparisons within each backbone.
The wavelet module introduces only small capacity changes, increasing parameters to 8.1518.151M for MLP, 13.29813.298M for LSTM, and 15.94315.943M for Transformer.
Its computational overhead is modest, with LSTM FLOPs increasing by 7.8%7.8\% and Transformer FLOPs slightly decreasing by 0.9%0.9\%.

At comparable complexity, the wavelet front-end consistently improves performance.
On average, MLP improves from 0.0750.075 ROI and 0.8130.813 Sharpe to 0.1650.165 and 1.0791.079, and LSTM improves from 0.1910.191 ROI and 1.6561.656 Sharpe to 0.3170.317 and 1.8791.879.
WaveLSFormer achieves the best overall ROI and Sharpe with virtually the same parameter count and slightly fewer FLOPs than the vanilla Transformer.
It also surpasses Wavelet+LSTM, improving ROI from 0.3170.317 to 0.6070.607 and Sharpe from 1.8791.879 to 2.1572.157.
These gains without disproportionate scaling suggest that the improvement is driven by the inductive bias of the neural wavelet front-end and its integration with the Transformer backbone, establishing a new Pareto frontier of performance versus complexity.

TABLE IX: Overall average performance and model complexity of all backbones with and without the wavelet front-end. Numbers are averaged over 6 industry groups and 10 random seeds. Model complexity is reported as parameter count and FLOPs per forward pass. Best ROI and Sharpe are in bold, second best are underlined.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Model | Params (M) | FLOPs (G) | Avg. ROI | Avg. Sharpe |
| MLP | 8.146 | 3.468 | 0.075±\pm0.023 | 0.813±\pm0.311 |
| MLP + Wavelet | 8.151 | 10.412 | 0.165±\pm0.045 | 1.079±\pm0.139 |
| LSTM | 12.538 | 492.614 | 0.191±\pm0.029 | 1.656±\pm0.495 |
| LSTM + Wavelet | 13.298 | 530.862 | 0.317±\pm0.049 | 1.879±\pm0.221 |
| Transformer | 15.928 | 665.921 | 0.225±\pm0.056 | 1.024±\pm0.122 |
| WaveLSformer (ours) | 15.943 | 659.742 | 0.607±\pm0.045 | 2.157±\pm0.166 |

## VIII Conclusion

In this paper, we proposed *WaveLSFormer*, a learnable wavelet-based Transformer for intraday long-short equity trading that combines a neural wavelet front-end with a Transformer backbone and outputs continuous long/short positions under a fixed risk budget.
WaveLSFormer optimizes a trading-aware objective that couples soft-label supervision with ROI- and Sharpe-oriented regularization, targeting risk-adjusted returns rather than point-wise forecasting accuracy.
Across five years of hourly U.S. equity data from 29.10.2020 to 29.10.2025 over six industry groups and ten random seeds, WaveLSFormer consistently outperforms matched MLP, LSTM, and Transformer baselines with and without wavelet front-ends.
Overall, WaveLSFormer achieves 0.607±0.0450.607\pm 0.045 ROI and 2.157±0.1662.157\pm 0.166 Sharpe, while the plain Transformer attains 0.225±0.0560.225\pm 0.056 ROI and 1.024±0.1221.024\pm 0.122 Sharpe.
Across backbones, the neural wavelet module improves profitability with modest computational overhead, and ablations confirm that learnable filters and gated cross-frequency injection drive the gains rather than backbone capacity alone.

### VIII-A Limitations

Our evaluation uses idealized trading assumptions and does not model transaction costs, slippage or market impact, bid-ask spreads, or leverage and turnover constraints.
We also study a subset of U.S. industries at a single bar frequency, so generalization to other universes, liquidity regimes, and market conditions requires further validation.

### VIII-B Future work

We will incorporate differentiable cost and constraint models to enable constrained optimization during training, and explore downside-risk-aware objectives beyond Sharpe-style regularization.
We also plan to study regime-adaptive and online learning, and evaluate the framework on broader asset universes and longer histories.

## References

* [1]

  E. F. Fama, “Efficient capital markets: A review of theory and empirical work,” *The Journal of Finance*, vol. 25, no. 2, pp. 383–417, 1970.
* [2]

  W. Brock, J. Lakonishok, and B. LeBaron, “Simple technical trading rules and the stochastic properties of stock returns,” *The Journal of finance*, vol. 47, no. 5, pp. 1731–1764, 1992.
* [3]

  N. Kohzadi, M. S. Boyd, B. Kermanshahi, and I. Kaastra, “A comparison of artificial neural network and time series models for forecasting commodity prices,” *Neurocomputing*, vol. 10, no. 2, pp. 169–181, 1996.
* [4]

  A. M. Ozbayoglu, M. U. Güdelek, and O. Sezer, “Deep learning for financial applications: A survey,” *Applied Soft Computing*, vol. 93, p. 106384, 2020.
* [5]

  C. Zhang, Z. Xu, Y. Song, and J. Wang, “Deep learning models for price forecasting of financial time series: A review of recent advancements,” *Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery*, vol. 14, no. 1, p. e1519, 2024.
* [6]

  S. Giantsidi and C. Tarantola, “Deep learning for financial forecasting: A review of recent trends,” *International Review of Financial Analysis*, 2025, in press.
* [7]

  J. Peng, Y. Huang, W. Jiang, and L. Wang, “Predicting stock movements: Using multiresolution wavelet reconstruction and deep learning in neural networks,” *Information*, vol. 12, no. 10, p. 388, 2021.
* [8]

  S. Rao, S. Mitra, and R. Kumar, “Financial time series forecasting using optimised wavelet transform and neural network models,” *International Journal of Information Technology*, vol. 14, no. 4, pp. 2231–2240, 2022.
* [9]

  J. Zhang, H. Liu, W. Bai, and X. Li, “A hybrid approach of wavelet transform, ARIMA and LSTM model for the share price index futures forecasting,” *The North American Journal of Economics and Finance*, vol. 69, p. 102022, 2024.
* [10]

  K. Ziółkowski, “Enhancing financial time series forecasting: A comparative study of discrete wavelet transform and LSTM models for selected global indices,” *Quality & Quantity*, 2025, online first.
* [11]

  J. Wu, J. Li, J. Yang, and S. Mei, “Wavelet-integrated deep neural networks: A systematic review of applications and synergistic architectures,” *Neurocomputing*, vol. 657, p. 131648, 2025.
* [12]

  L. Sasal, T. Chakraborty, and A. Hadid, “W-transformers: A wavelet-based transformer framework for univariate time series forecasting,” in *2022 IEEE 21st International Conference on Machine Learning and Applications (ICMLA)*, 2022, pp. 671–676.
* [13]

  W. Wei, Z. Wang, B. Pang, J. Wang, and X. Liu, “Wavelet transformer: An effective method on multiple periodic decomposition for time series forecasting,” *IEEE Transactions on Neural Networks and Learning Systems*, vol. 36, no. 8, pp. 14 063–14 077, 2025.
* [14]

  Y. Ping, H. Kong, and Z. Li, “Wavelet-enhanced transformer for adaptive multi-period time series forecasting,” *Preprint*, 2025, available on preprints.org.
* [15]

  E. Hoseinzade and S. Haratizadeh, “Cnnpred: Cnn-based stock market prediction using a diverse set of variables,” *Expert Systems with Applications*, vol. 129, pp. 273–285, 2019.
* [16]

  D. M. Q. Nelson, A. C. M. Pereira, and R. A. de Oliveira, “Stock market’s price movement prediction with LSTM neural networks,” in *2017 International Joint Conference on Neural Networks (IJCNN)*, 2017, pp. 1419–1426.
* [17]

  A. Moghar and M. Hamiche, “Stock market prediction using LSTM recurrent neural network,” *Procedia Computer Science*, vol. 170, pp. 1168–1173, 2020.
* [18]

  W. Bao, J. Yue, and Y. Rao, “A deep learning framework for financial time series using stacked autoencoders and long-short term memory,” *PLOS ONE*, vol. 12, no. 7, p. e0180944, 2017.
* [19]

  T. Buczyński, M. Dabrowski, and W. Kwasnicki, “Deep learning models for financial time series forecasting: A comparative study,” *Quality & Quantity*, vol. 57, no. 4, pp. 1967–1994, 2023.
* [20]

  C. Krauss, X. A. Do, and N. Huck, “Deep neural networks, gradient-boosted trees, random forests: Statistical arbitrage on the S&P 500,” *European Journal of Operational Research*, vol. 259, no. 2, pp. 689–702, 2017.
* [21]

  A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, “Attention is all you need,” *Advances in neural information processing systems*, vol. 30, 2017.
* [22]

  H. Zhou, S. Zhang, J. Peng, S. Zhang, J. Li, H. Xiong, and W. Zhang, “Informer: Beyond efficient transformer for long sequence time-series forecasting,” in *Proceedings of the AAAI Conference on Artificial Intelligence*, vol. 35, no. 12, 2021, pp. 11 106–11 115.
* [23]

  L. Mozaffari and J. Zhang, “Predictive modeling of stock prices using transformer model,” in *Proceedings of the 9th International Conference on Machine Learning Technologies (ICMLT 2024)*. Oslo, Norway: ACM, 2024, pp. 1–8.
* [24]

  M. R. Kabir, D. Bhadra, M. Ridoy, and M. Milanova, “LSTM-transformer-based robust hybrid deep learning model for financial time series forecasting,” *Sci*, vol. 7, no. 1, p. 7, 2025.
* [25]

  L. Lei, “Wavelet neural network prediction method of stock price trend based on rough set attribute reduction,” *Applied Soft Computing*, vol. 62, pp. 923–932, 2018.
* [26]

  L. Peng, K. Chen, and N. Li, “Predicting stock movements: Using multiresolution wavelet reconstruction and deep learning in neural networks,” *Information*, vol. 12, no. 10, p. 388, 2021.
* [27]

  S. K. Chandar, M. Sumathi, and S. N. Sivanandam, “Prediction of stock market price using hybrid of wavelet transform and artificial neural network,” *Indian Journal of Science and Technology*, vol. 9, no. 8, pp. 1–5, 2016, original Article.
* [28]

  J. Lee, H. Koh, and H. J. Choe, “Learning to trade in financial time series using high-frequency through wavelet transformation and deep reinforcement learning,” *Applied Intelligence*, vol. 51, no. 8, pp. 6202–6223, 2021.
* [29]

  X. Ma, Y. Chen, and P. Liu, “Stockformer: A price-volume factor stock selection model based on wavelet decomposition and multi-task self-attention,” *Expert Systems with Applications*, vol. 273, p. 126803, 2025.
* [30]

  C. Diks and V. Panchenko, “A new statistic and practical guidelines for nonparametric granger causality testing,” *Journal of Economic Dynamics and Control*, vol. 30, no. 9–10, pp. 1647–1669, 2006.