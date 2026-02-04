---
authors:
- Zhuohan Wang
- Carmine Ventre
doc_id: arxiv:2602.03776v1
family_id: arxiv:2602.03776
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books'
url_abs: http://arxiv.org/abs/2602.03776v1
url_html: https://arxiv.org/html/2602.03776v1
venue: arXiv q-fin
version: 1
year: 2026
---


Zhuohan Wang1
  
Carmine Ventre2
  
1King’s College London
{zhuohan.wang, carmine.ventre}@kcl.ac.uk

###### Abstract

Modern generative models for limit order books (LOBs) can reproduce realistic market dynamics, but remain fundamentally passive: they either model what typically happens without accounting for hypothetical future market conditions, or they require interaction with another agent to explore alternative outcomes. This limits their usefulness for stress testing, scenario analysis, and decision-making. We propose DiffLOB, a regime-conditioned Diffusion model for controllable and counterfactual generation of LOB trajectories. DiffLOB explicitly conditions the generative process on future market regimes–including trend, volatility, liquidity, and order-flow imbalance, which enables the model to answer counterfactual queries of the form: “If the future market regime were X instead of Y, how would the limit order book evolve?” Our systematic evaluation framework for counterfactual LOB generation consists of three criteria: (1) Controllable Realism, measuring how well generated trajectories can reproduce marginal distributions, temporal dependence structure and regime variables; (2) Counterfactual validity, testing whether interventions on future regimes induce consistent changes in the generated LOB dynamics; (3) Counterfactual usefulness, assessing whether synthetic counterfactual trajectories improve downstream prediction of future market regimes.

## 1 Introduction

Modern financial markets are driven by automated trading systems operating on limit order books (LOBs)  (Gould et al., [2013](https://arxiv.org/html/2602.03776v1#bib.bib64 "Limit order books")). A LOB can be thought of as two priority queues collecting buy and sell orders of market participants. Each order is comprised of bid/ask price (how much one is willing to pay/get for each stock) and volume (how many stocks one wants to trade). Small changes in trend, liquidity, volatility, or order flow balance of the LOB can lead to drastically different market outcomes. As a result, stress testing, strategy design, and market surveillance all require not only accurate models of how markets behave on average, but also the ability to simulate how the market would become under hypothetical future conditions, such as fast trend change, liquidity shocks, volatility spikes, or imbalanced order flow.

However, existing approaches to LOB modeling exhibit fundamental limitations in answering counterfactual questions. Supervised LOB predictors typically focus on forecasting specific future variables, such as mid-price returns (Briola et al., [2025a](https://arxiv.org/html/2602.03776v1#bib.bib85 "Deep limit order book forecasting: a microstructural guide"), [b](https://arxiv.org/html/2602.03776v1#bib.bib86 "HLOB–information persistence and structure in limit order books")), but they do not generate full market trajectories and therefore cannot simulate how the order book would evolve over time under alternative future conditions. Recent generative models for LOBs are capable of producing highly realistic samples when conditioned on historical observations (Nagy et al., [2023](https://arxiv.org/html/2602.03776v1#bib.bib66 "Generative ai for end-to-end limit order book modelling: a token-level autoregressive generative model of message flow using a deep state space network"); Coletta et al., [2021](https://arxiv.org/html/2602.03776v1#bib.bib65 "Towards realistic market simulations: a generative adversarial networks approach"); Li et al., [2025](https://arxiv.org/html/2602.03776v1#bib.bib87 "MarS: a financial market simulation engine powered by generative foundation model")). However, to obtain counterfactual outcomes, these models usually rely on explicit interactions with trading agents. As a result, the counterfactual trajectories generated are not guaranteed as a desired future state of the market.

To address this gap, we propose DiffLOB111Our code is available at <https://github.com/ZhuoHan1998/DiffLOB>., a diffusion model-based framework specifically designed for the counterfactual generation of LOB snapshots. The proposed framework offers three main contributions:

* (1){(1)}

  We formulate counterfactual generation of LOBs as a conditional generative modeling problem and explicitly introduce future market regimes as control variables to enable controllable and counterfactual generation. We develop a novel diffusion-based architecture that conditions on past LOB trajectories, time-of-day information, and four future regime variables–trend, volatility, liquidity, and order-flow imbalance. The proposed model effectively captures key financial statistics and consistently outperforms strong baseline models across a range of evaluation metrics.
* (2){(2)}

  We empirically demonstrate that interventions on future market regimes induce consistent and interpretable changes in the generated LOB dynamics. Under extreme and hypothetical regime conditions, DiffLOB produces trajectories whose statistical properties align with the imposed regimes and closely match real markets observed under comparable conditions.
* (3){(3)}

  We show that synthetic counterfactual trajectories generated by DiffLOB provide meaningful additional information for downstream tasks. In particular, augmenting real data with counterfactual samples consistently improves the performance of models for future market regime prediction under extreme conditions, demonstrating the practical value of counterfactual LOB generation.

## 2 Related Work

Generative Modelling in LOBs.
A growing body of work applies generative models to LOBs with the goal of reproducing realistic market microstructure dynamics. Autoregressive approaches have been used to model LOB dynamics at the event level.
Hultin et al. ([2023](https://arxiv.org/html/2602.03776v1#bib.bib75 "A generative model of a limit order book using recurrent neural networks")) decompose the joint distribution of LOB transitions into conditional components using recurrent neural networks,
while Nagy et al. ([2023](https://arxiv.org/html/2602.03776v1#bib.bib66 "Generative ai for end-to-end limit order book modelling: a token-level autoregressive generative model of message flow using a deep state space network")) propose an end-to-end autoregressive model based on structured state-space models that tokenizes message streams.
GAN-based approaches, on the other hand, employ adversarial training to synthesize LOB data with high visual and statistical realism.  Coletta et al. ([2021](https://arxiv.org/html/2602.03776v1#bib.bib65 "Towards realistic market simulations: a generative adversarial networks approach")) propose a Conditional GAN framework that reacts to current market states and allows agent interaction within a simulation, showing enhanced realism and responsiveness. Recent work has also explored diffusion-based approaches for limit order book simulation. TRADES (Berti et al., [2025](https://arxiv.org/html/2602.03776v1#bib.bib90 "TRADES: generating realistic market simulations with diffusion models")) develops a diffusion-based market simulator that generates order-level LOB dynamics and supports counterfactual analysis through interaction with trading agents. DiffVolume (Wang and Ventre, [2025](https://arxiv.org/html/2602.03776v1#bib.bib88 "DiffVolume: diffusion models for volume generation in limit order books")) apply diffusion models to generate high-dimensional LOB volume snapshots across multiple price levels without capturing full LOB trajectories.  Li et al. ([2025](https://arxiv.org/html/2602.03776v1#bib.bib87 "MarS: a financial market simulation engine powered by generative foundation model")) create an order-level generative foundation model for downstream forecasting, risk detection and financial analysis. Despite their success in realism, existing generative LOB models primarily learn the observational distribution of market dynamics. They are not designed to explicitly intervene on future market regimes, and therefore cannot generate counterfactual and complete LOB trajectories corresponding to hypothetical future conditions.

#### Diffusion Models for Financial Time Series.

Diffusion models are a class of generative models inspired by thermodynamic diffusion processes, where data are progressively perturbed with Gaussian noise and generated by learning to reverse this process (Sohl-Dickstein et al., [2015](https://arxiv.org/html/2602.03776v1#bib.bib7 "Deep unsupervised learning using nonequilibrium thermodynamics"); Ho et al., [2020](https://arxiv.org/html/2602.03776v1#bib.bib3 "Denoising diffusion probabilistic models")).
This formulation is closely connected to score-based generative modeling, which learns the gradient of the data density via denoising score matching (Vincent, [2011](https://arxiv.org/html/2602.03776v1#bib.bib10 "A connection between score matching and denoising autoencoders"); Song and Ermon, [2019](https://arxiv.org/html/2602.03776v1#bib.bib2 "Generative modeling by estimating gradients of the data distribution")), and has been unified under a stochastic differential equation (SDE) framework (Song et al., [2021](https://arxiv.org/html/2602.03776v1#bib.bib1 "Score-based generative modeling through stochastic differential equations")).
Building on these advances, diffusion models have been increasingly applied to financial time series. Koa et al. ([2023](https://arxiv.org/html/2602.03776v1#bib.bib81 "Diffusion variational autoencoder for tackling stochasticity in multi-step regression stock price prediction")) employ diffusion models for multi-step stock price prediction,
while Wang and Ventre ([2024](https://arxiv.org/html/2602.03776v1#bib.bib80 "A financial time series denoiser based on diffusion models")) apply diffusion-based denoising techniques to financial time series.
More recently, Tanaka et al. ([2025](https://arxiv.org/html/2602.03776v1#bib.bib89 "CoFinDiff: controllable financial diffusion model for time series generation")) propose a controllable diffusion framework for financial time series generation and introduce normalization-based techniques to enhance controllability (Hashimoto et al., [2025](https://arxiv.org/html/2602.03776v1#bib.bib91 "Norm-salvaged embedding: improving condition alignment of synthetic time series generation in finance")).

## 3 Methodology

### 3.1 Problem Formulation

Let xt∈ℝK×Cx\_{t}\in\mathbb{R}^{K\times C} denote the state of LOB at time tt, where KK denotes the number of price levels (e.g., 10 ask price levels and 10 bid price levels) and CC represents the feature dimension (e.g., price and volume).
Given a historical LOB trajectory x1:tx\_{1:t}, our goal is to generate a future trajectory xt+1:t+τx\_{t+1:t+\tau}. We introduce future market regimes as controlling variables to enable controllable and counterfactual generation.
Specifically, we define a set of future regime variables

|  |  |  |
| --- | --- | --- |
|  | ct+1:t+τ=(ct+1:t+τtrend,ct+1:t+τvol,ct+1:t+τliq,ct+1:t+τimb),where{ct+1:t+τtrend,ct+1:t+τvol}∈ℝ,{ct+1:t+τliq,ct+1:t+τimb}∈ℝτ\begin{split}c\_{t+1:t+\tau}&=\big(c^{\text{trend}}\_{t+1:t+\tau},c^{\text{vol}}\_{t+1:t+\tau},c^{\text{liq}}\_{t+1:t+\tau},c^{\text{imb}}\_{t+1:t+\tau}\big),\\ \text{where}\ &\{c^{\text{trend}}\_{t+1:t+\tau},c^{\text{vol}}\_{t+1:t+\tau}\}\in\mathbb{R},\ \{c^{\text{liq}}\_{t+1:t+\tau},\ c^{\text{imb}}\_{t+1:t+\tau}\}\in\mathbb{R}^{\tau}\end{split} |  |

corresponding to trend, volatility, liquidity, and order-flow imbalance, respectively.
These variables characterize the macroscopic state of the market over the future horizon and are treated as *intervenable control variables* rather than observed labels. Our objective is to model the distribution

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(xt+1:t+τ∣x1:t,ct+1:t+τ),p\big(x\_{t+1:t+\tau}\mid x\_{1:t},c\_{t+1:t+\tau}\big), |  | (1) |

which enables counterfactual queries of the form:
*“How would the limit order book evolve if the future market regime conditions were different?”*
By explicitly conditioning on future regimes, DiffLOB decouples market dynamics from specific agent behaviors and provides direct control over hypothetical future market conditions.

We adopt a denoising diffusion probabilistic model (DDPM)  (Ho et al., [2020](https://arxiv.org/html/2602.03776v1#bib.bib3 "Denoising diffusion probabilistic models")) to represent the conditional distribution of future LOB trajectories. In the forward process, Gaussian noise is progressively added to the target trajectory xt+1:t+τx\_{t+1:t+\tau} over a sequence of diffusion steps. A neural network is trained to reverse this process by predicting the injected noise at each step, thereby learning to generate samples from the data distribution. Conditions on historical trajectories and future market regimes are incorporated through the denoising network, allowing the diffusion process to generate future LOB trajectories consistent with specified regimes.
We follow standard score-based diffusion modelling and refer the reader to Appendix [A](https://arxiv.org/html/2602.03776v1#A1 "Appendix A Diffusion Models Theory ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") for full technical details.

### 3.2 DiffLOB Architecture

![Refer to caption](figures/DiffLOB_Architecture.png)


Figure 1: Illustration of DiffLOB Architecture.

An overview of DiffLOB architecture is shown in Figure [1](https://arxiv.org/html/2602.03776v1#S3.F1 "Figure 1 ‣ 3.2 DiffLOB Architecture ‣ 3 Methodology ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").

#### Overall Backbone.

As illustrated in Figure [1](https://arxiv.org/html/2602.03776v1#S3.F1 "Figure 1 ‣ 3.2 DiffLOB Architecture ‣ 3 Methodology ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books")(a), DiffLOB adopts stacked Wavenet-style residual blocks  (van den Oord et al., [2016](https://arxiv.org/html/2602.03776v1#bib.bib83 "WaveNet: A Generative Model for Raw Audio")). The backbone models the structural and temporal dynamics of LOB price and volume evolution, producing residual connection R​e​siRes\_{i} and skip connection S​k​i​piSkip\_{i} at each block, where residual outputs are propagated to subsequent blocks and skip outputs are aggregated to form the final prediction of score sθs\_{\theta}. The input x~t+1:t+τ\tilde{x}\_{t+1:t+\tau} denotes the noised LOB trajectory at a given diffusion step. D​i​me​m​bDim\_{emb} is price level embedding, which enables the model to distinguish between spatially different price levels in the order book.

#### Regime Condition Encoders.

Future market regimes are encoded through a condition encoder (Figure [1](https://arxiv.org/html/2602.03776v1#S3.F1 "Figure 1 ‣ 3.2 DiffLOB Architecture ‣ 3 Methodology ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books")(b)).
We distinguish between L​o​c​a​lLocal and G​l​o​b​a​lGlobal regime information. Local conditions capture step-wise signals, including historical LOB, liquidity, imbalance, and time-of-day information, and are encoded using convolutional layers. Global conditions represent longer-horizon market characteristics, such as future trend and volatility, and are encoded using multilayer perceptrons.
This separation allows DiffLOB to model heterogeneous regime effects at different temporal scales.

#### Control Module and Dual-stage Training.

To enforce controlling over generated trajectories, DiffLOB introduces a control module inspired by ControlNet  (Zhang et al., [2023](https://arxiv.org/html/2602.03776v1#bib.bib92 "Adding conditional control to text-to-image diffusion models")), as shown in (Figure [1](https://arxiv.org/html/2602.03776v1#S3.F1 "Figure 1 ‣ 3.2 DiffLOB Architecture ‣ 3 Methodology ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books")(c)).
The condition encoder and wavenet module are first trained to model the base data distribution. Subsequently, the control module is trained while keeping the other backbone parameters frozen. Control signals are injected additively through zero-initialized 1×11\times 1 convolutional layers, whose weights and biases are initialized to zero. As a result, the control pathway has no effect at initialization and gradually learns regime-specific interventions in a stable and interpretable manner.

#### Wavenet Module with FiLM Modulation.

Each residual block follows a Wavenet-style gated architecture with residual and skip connections, as shown in Figure [1](https://arxiv.org/html/2602.03776v1#S3.F1 "Figure 1 ‣ 3.2 DiffLOB Architecture ‣ 3 Methodology ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books")(d).
Conditioning information is injected using feature-wise linear modulation (FiLM)  (Perez et al., [2018](https://arxiv.org/html/2602.03776v1#bib.bib76 "Film: visual reasoning with a general conditioning layer")).
Block activations are sequentially modulated by the diffusion timestep embedding te​m​bt\_{emb}, L​o​c​a​lLocal and G​l​o​b​a​lGlobal regime embeddings.
This sequential modulation scheme enables structured interaction between diffusion time, short-term market states, and long-horizon regime characteristics.

## 4 Experimental Setup

In this section, we provide data, preprocessing methods, as well as the training and sampling procedures.

### 4.1 Data and Preprocessing

We use the LOBSTER data222https://lobsterdata.com/ as our LOB data source  (Huang and Polak, [2011](https://arxiv.org/html/2602.03776v1#bib.bib77 "Lobster: limit order book reconstruction system")). We sample one snapshot per second. Each snapshot includes the top 10 levels on both the bid and ask sides. In particular, we train, evaluate, and test our model separately on three stocks, which are AMZN, AAPL and GOOG. For each stock, we use 16 consecutive trading days for training (1 February to 23 February 2023), 1 day for validation (24 February 2023), and the final 2 days for testing (27-28 February 2023).

#### Price Representation.

Let at(k)a\_{t}^{(k)} and bt(k)b\_{t}^{(k)} denote the ask and bid prices at level kk at time tt.
We define the mid-price as

|  |  |  |
| --- | --- | --- |
|  | mt=at(1)+bt(1)2.m\_{t}=\frac{a\_{t}^{(1)}+b\_{t}^{(1)}}{2}. |  |

To model temporal price dynamics, we use one-step mid-price difference:

|  |  |  |
| --- | --- | --- |
|  | rt=mt+1−mt.r\_{t}=m\_{t+1}-m\_{t}. |  |

In addition, we include cross-sectional price differences to capture the spatial structure of the order book:

|  |  |  |
| --- | --- | --- |
|  | Δ​at(k)=at(k)−at(k−1),Δ​st=at(1)−bt(1),Δ​bt(k)=bt(k−1)−bt(k)\Delta a\_{t}^{(k)}=a\_{t}^{(k)}-a\_{t}^{(k-1)},\quad\Delta s\_{t}=a\_{t}^{(1)}-b\_{t}^{(1)},\quad\Delta b\_{t}^{(k)}=b\_{t}^{(k-1)}-b\_{t}^{(k)} |  |

for k=2,…,Kk=2,\dots,K. The final price representation concatenates the one-step mid-price difference and the cross-sectional price differences.
This construction preserves the original dimension while removing absolute price levels, resulting in a more stable and learnable representation for generative modeling.

#### Volume Representation.

Raw volume vv exhibit heavy-tailed distributions and large scale variations.
To stabilize training, we cap volume values at the 99th percentile followed by a square-root normalization:

|  |  |  |
| --- | --- | --- |
|  | v~=vc,\tilde{v}=\frac{\sqrt{v}}{c}, |  |

where cc is a constant scaling factor.

#### Market Regimes.

Market regimes are computed from the target LOB trajectory xt+1:t+τx\_{t+1:t+\tau} and used as conditioning variables.
Specifically, we define:

* •

  Trend as the cumulative mid-price return over τ\tau:

  |  |  |  |
  | --- | --- | --- |
  |  | ct+1:t+τtrend=∑i=0τ−1r​(t+i).c^{\text{trend}}\_{t+1:t+\tau}=\sum\_{i=0}^{\tau-1}r(t+i). |  |
* •

  Volatility as the standard deviation of returns over τ\tau:

  |  |  |  |
  | --- | --- | --- |
  |  | ct+1:t+τvol=1τ​∑i=0τ−1rt+i2−(1τ​∑i=0τ−1rt+i)2.c^{\text{vol}}\_{t+1:t+\tau}=\sqrt{\frac{1}{\tau}\sum\_{i=0}^{\tau-1}r\_{t+i}^{2}-\left(\frac{1}{\tau}\sum\_{i=0}^{\tau-1}r\_{t+i}\right)^{2}}. |  |
* •

  Liquidity as the total standing volume over each timestep:

  |  |  |  |
  | --- | --- | --- |
  |  | ct+iliq=∑k=1K(vt+ia,(k)+vt+ib,(k)).c^{\text{liq}}\_{t+i}=\sum\_{k=1}^{K}\left(v\_{t+i}^{a,(k)}+v\_{t+i}^{b,(k)}\right). |  |
* •

  Order-flow imbalance as the normalized volume imbalance over each timestep:

  |  |  |  |
  | --- | --- | --- |
  |  | ct+iimb=∑k=1K(vt+ia,(k)−vt+ib,(k))∑k=1K(vt+ia,(k)+vt+ib,(k)).c^{\text{imb}}\_{t+i}=\frac{\sum\_{k=1}^{K}\left(v\_{t+i}^{a,(k)}-v\_{t+i}^{b,(k)}\right)}{\sum\_{k=1}^{K}\left(v\_{t+i}^{a,(k)}+v\_{t+i}^{b,(k)}\right)}. |  |

### 4.2 Training and Sampling

Historical length tt and generated length τ\tau are fixed to 32 for all experiments. To promote stable training and reduce overfitting, we employ early stopping and exponential moving average (EMA) of model parameters.
Early stopping is based on the validation loss and terminates training if no improvement greater than 0.0010.001 is observed over 100100 epochs.
The model is optimized using Adam (Kingma and Ba, [2015](https://arxiv.org/html/2602.03776v1#bib.bib79 "Adam: A method for stochastic optimization")) with a learning rate of 1×10−41\times 10^{-4} and a batch size of 128128. We adopt the DDPM parameterization with 100100 discrete noise levels and generate samples via ancestral sampling (Ho et al., [2020](https://arxiv.org/html/2602.03776v1#bib.bib3 "Denoising diffusion probabilistic models")).
Conditions are incorporated during training and sampling using classifier-free guidance (Ho and Salimans, [2021](https://arxiv.org/html/2602.03776v1#bib.bib60 "Classifier-free diffusion guidance")).
The network consists of 1616 residual blocks with SiLU activations applied after each convolution.
Complete training and sampling algorithm are provided in Appendix [B](https://arxiv.org/html/2602.03776v1#A2 "Appendix B Training and Sampling Algorithms ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").

## 5 Experimental Results

We evaluate DiffLOB from three complementary perspectives to assess its controllable realism, counterfactual validity, and practical usefulness. We compare DiffLOB with several baseline generative models. These include diffusion-based baselines (Diff-CSDI  (Tashiro et al., [2021](https://arxiv.org/html/2602.03776v1#bib.bib4 "CSDI: conditional score-based diffusion models for probabilistic time series imputation")) and Diff-S4 (Alcaraz and Strodthoff, [2022](https://arxiv.org/html/2602.03776v1#bib.bib17 "Diffusion-based time series imputation and forecasting with structured state space models"))), non-diffusion generative models (cGAN (Cont et al., [2023](https://arxiv.org/html/2602.03776v1#bib.bib67 "Limit order book simulation with generative adversarial networks")) and cVAE (Sohn et al., [2015](https://arxiv.org/html/2602.03776v1#bib.bib93 "Learning structured output representation using deep conditional generative models"))), and an autoregressive S4-based model AR (Nagy et al., [2023](https://arxiv.org/html/2602.03776v1#bib.bib66 "Generative ai for end-to-end limit order book modelling: a token-level autoregressive generative model of message flow using a deep state space network")). DiffLOB without the control module is also included for ablation study use. For clarity of presentation, all figures use AMZN as an illustrative example.

### 5.1 Controllable Realism

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | AMZN | | | | AAPL | | | | GOOG | | | |
| Price-Realism | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS |
| DiffLOB | 0.052384 | 0.028371 | 0.075605 | 0.017585 | 0.031695 | 0.016446 | 0.026561 | 0.005704 | 0.055462 | 0.035195 | 0.363414 | 0.037249 |
| DiffLOB w/o C | 0.212398 | 0.182775 | 0.730008 | 0.064836 | 0.079402 | 0.064358 | 0.095074 | 0.014745 | 0.103601 | 0.085803 | 0.30239 | 0.027799 |
| Diff-CSDI | 0.628793 | 64.621056 | 5.862505 | 0.306881 | 0.576959 | 68.690042 | 5.507347 | 0.286949 | 0.573082 | 47.207406 | 4.99384 | 0.261333 |
| Diff-S4 | 0.200429 | 0.155586 | 0.304272 | 0.051942 | 0.101795 | 0.0915 | 0.149292 | 0.019214 | 0.153828 | 0.06162 | 0.603084 | 0.058418 |
| CGAN | 0.053521 | 0.048909 | 0.378863 | 0.026156 | 0.830413 | 2.402774 | 9.343481 | 0.466478 | 0.28967 | 0.296793 | 1.523045 | 0.114271 |
| CVAE | 0.173396 | 0.142745 | 0.406215 | 0.053637 | 0.025862 | 0.021286 | 0.135777 | 0.013759 | 0.155807 | 0.085175 | 0.419525 | 0.050767 |
| AR | 0.118031 | 0.076163 | 0.419127 | 0.037131 | 0.173451 | 0.145696 | 0.304234 | 0.03807 | 0.107334 | 0.046178 | 0.324453 | 0.040902 |
| Volume-Realism | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS |
| DiffLOB | 0.109174 | 97.54283 | 0.111954 | 0.023297 | 0.087666 | 55.377778 | 0.071645 | 0.014677 | 0.099899 | 97.270339 | 0.086374 | 0.016609 |
| DiffLOB w/o C | 0.113053 | 117.36868 | 0.108419 | 0.022918 | 0.100573 | 72.929232 | 0.091735 | 0.019714 | 0.126238 | 132.065501 | 0.117649 | 0.023473 |
| Diff-CSDI | 0.293449 | 599243.7598 | 0.324422 | 0.052769 | 0.235838 | 587451.9702 | 0.29902 | 0.04794 | 0.256603 | 578472.3812 | 0.266948 | 0.039498 |
| Diff-S4 | 0.170321 | 161.665895 | 0.178012 | 0.036454 | 0.132301 | 104.168332 | 0.138386 | 0.025026 | 0.246833 | 279.02256 | 0.325909 | 0.060015 |
| CGAN | 0.288535 | 321.049535 | 0.500225 | 0.090229 | 0.487548 | 275.698425 | 2.956931 | 0.23594 | 0.127321 | 151.897776 | 0.137742 | 0.027589 |
| CVAE | 0.260795 | 255.043006 | 1.154918 | 0.153781 | 0.23728 | 169.905872 | 1.251494 | 0.140914 | 0.231203 | 240.882982 | 0.864015 | 0.112463 |
| AR | 0.397229 | 444.216686 | 1.172602 | 0.159319 | 0.285415 | 188.199251 | 0.669676 | 0.112751 | 0.2863 | 343.938149 | 0.724715 | 0.106982 |

Table 1: Controllable Realism on Three Stocks.

We first evaluate the realism of DiffLOB by conditioning the model on *observed* future market regimes and comparing the generated trajectories with real data.
The goal of this evaluation is to assess whether DiffLOB can faithfully reproduce key statistics of LOB dynamics.

![Refer to caption](figures/mid_price_return_AMZN.png)


(a) Mid Price Return on Different Horizons.

![Refer to caption](figures/spread_distribution_bin_AMZN.png)


(b) Spread Distribution.

![Refer to caption](figures/mid_price_return_autocorrelation_AMZN.png)


(c) Volatility Clustering.

Figure 2: Realism on Price.

Figure [2](https://arxiv.org/html/2602.03776v1#S5.F2 "Figure 2 ‣ 5.1 Controllable Realism ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") evaluates the realism of price dynamics generated by models. Figure [2(a)](https://arxiv.org/html/2602.03776v1#S5.F2.sf1 "In Figure 2 ‣ 5.1 Controllable Realism ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") shows that DiffLOB closely matches the empirical distributions of mid-price returns across multiple horizons. Figure [2(b)](https://arxiv.org/html/2602.03776v1#S5.F2.sf2 "In Figure 2 ‣ 5.1 Controllable Realism ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") reports the distribution of bid–ask spread, where DiffLOB replicates real distribution best. Figure [2(c)](https://arxiv.org/html/2602.03776v1#S5.F2.sf3 "In Figure 2 ‣ 5.1 Controllable Realism ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") compares the autocorrelation of absolute returns. DiffLOB reproduces the persistent decay pattern characteristic of volatility clustering, whereas cGAN and cVAE largely fail to capture temporal dependence and AR models underestimate long-range correlations.

![Refer to caption](figures/volume_temporal_diff_correlation_AMZN.png)


Figure 3: Temporal Difference Volume Correlation.

Figure [3](https://arxiv.org/html/2602.03776v1#S5.F3 "Figure 3 ‣ 5.1 Controllable Realism ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") is calculated from the first-order differences of the volume snapshots (vt+1−vtv\_{t+1}-v\_{t}). A notable characteristic in the temporal difference correlation structure is the negative correlation at adjacent price levels, which is captured only by DiffLOB. We also show more details about marginal volume distribution across price levels in Appendix [C](https://arxiv.org/html/2602.03776v1#A3 "Appendix C Volume Distribution ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").

Figure [4](https://arxiv.org/html/2602.03776v1#S5.F4 "Figure 4 ‣ 5.1 Controllable Realism ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") visualizes the distributions of future market regime variables under observed conditions, including trend, volatility, liquidity, and order-flow imbalance. DiffLOB accurately captures the central tendency of trend and volatility, while achieving an excellent match to the full empirical distributions of liquidity and order-flow imbalance, including both spread and tail behavior. In contrast, baseline models exhibit noticeable mismatches, such as overly concentrated distributions (AR on Trend) and shifted modes (cVAE on Liquidity, AR on Volatility, AR on Imbalance). These results further confirm that DiffLOB can faithfully reproduce regime-level statistics when conditioned on true future regimes, supporting the quantitative findings in Table [1](https://arxiv.org/html/2602.03776v1#S5.T1 "Table 1 ‣ 5.1 Controllable Realism ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").

![Refer to caption](figures/real_conditions_metrics_AMZN.png)


Figure 4: Controllable Realism Distribution..

Table [1](https://arxiv.org/html/2602.03776v1#S5.T1 "Table 1 ‣ 5.1 Controllable Realism ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") reports quantitative distributional distances between generated and real LOB trajectories under observed future regimes on the three stocks across both price-related and volume-related statistics.
We consider four distance metrics, including Kolmogorov–Smirnov (KS) statistic, Wasserstein distance, Kullback–Leibler (KL) divergence, and Jensen–Shannon (JS) divergence. Across all assets and metrics, DiffLOB consistently achieves the lowest or near-lowest distances, indicating that it best matches the empirical distributions of real data when conditioned on true future regimes. Removing the control module (DiffLOB w/o C) leads to a clear degradation in performance, highlighting the importance of explicit regime control even under observed conditions. Diffusion-based baselines (Diff-CSDI and Diff-S4) improve upon non-diffusion methods in some cases, but remain substantially less accurate than DiffLOB, showing the effectiveness of our proposed DiffLOB architecture described in Section  [3.2](https://arxiv.org/html/2602.03776v1#S3.SS2 "3.2 DiffLOB Architecture ‣ 3 Methodology ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
Non-diffusion baselines, including cGAN, cVAE, and the autoregressive model, exhibit significantly larger discrepancies, especially in Wasserstein and KL distances. Overall, these results demonstrate that DiffLOB achieves superior controllable realism across both price and volume dimensions, and that designed control module plays a critical role in accurately reproducing LOB statistics.

### 5.2 Counterfactual Validity

We next evaluate the counterfactual validity by intervening on future market regimes and examining the resulting generated trajectories. Specifically, we impose extreme hypothetical conditions, including high and low trend, volatility, liquidity, and order-flow imbalance, and assess whether the generated samples exhibit statistical properties consistent with the imposed regimes.

![Refer to caption](figures/fake_high_low_conditions_AMZN.png)


Figure 5: Counterfactual Realism Distribution.

Figure [5](https://arxiv.org/html/2602.03776v1#S5.F5 "Figure 5 ‣ 5.2 Counterfactual Validity ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") evaluates counterfactual validity under explicit regime interventions.
For each regime variable, we compare distributions generated under high and low counterfactual conditions with real trajectories in the corresponding extreme regimes (top and bottom 20%).
For trend and volatility, DiffLOB does not perfectly overlap with empirical distributions but consistently shifts in the correct direction and preserves the separation between high and low conditions.
In contrast, for liquidity and order-flow imbalance, DiffLOB closely matches the empirical distributions, indicating strong controllability for volume-driven dynamics.
Overall, these results show that DiffLOB learns an interpretable and intervention-consistent relationship between future regimes and LOB dynamics, enabling meaningful counterfactual generation.

![Refer to caption](figures/price_trends_AMZN.png)


Figure 6: Counterfactual LOB Price Trajectories.

Figure [6](https://arxiv.org/html/2602.03776v1#S5.F6 "Figure 6 ‣ 5.2 Counterfactual Validity ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") and Figure [7](https://arxiv.org/html/2602.03776v1#S5.F7 "Figure 7 ‣ 5.2 Counterfactual Validity ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") provide visualizations of counterfactual generation on price and volume trajectories.
In Figure [6](https://arxiv.org/html/2602.03776v1#S5.F6 "Figure 6 ‣ 5.2 Counterfactual Validity ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"), explicit interventions on future trend and volatility induce coherent and interpretable changes.
High-trend conditions lead to persistent upward price movements, while low-trend conditions result in declining trajectories.
Similarly, high-volatility interventions produce more volatile price paths with larger fluctuations, whereas low-volatility conditions yield smoother dynamics.

![Refer to caption](figures/volume_heatmaps_AMZN.png)


Figure 7: Counterfactual LOB Volume Trajectories.

In Figure [7](https://arxiv.org/html/2602.03776v1#S5.F7 "Figure 7 ‣ 5.2 Counterfactual Validity ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"), imposing high-liquidity conditions leads to consistently larger volume magnitudes across the LOB, while low-liquidity conditions shift the overall volume downward.
Imbalance interventions induce clear asymmetries between bid and ask sides, consistent with the imposed order-flow imbalance.
These results demonstrate that DiffLOB can generate regime-consistent dynamics beyond matching marginal distributions.

| High-Trend | KS | Wasserstein | KL | JS |
| --- | --- | --- | --- | --- |
| DiffLOB | 0.444095 | 0.522512 | 2.517532 | 0.180279 |
| DiffLOB w/o C | 0.515225 | 0.801835 | 4.879508 | 0.265181 |
| Diff-CSDI | 0.627345 | 65.274135 | 5.855148 | 0.307245 |
| Diff-S4 | 0.292354 | 0.264849 | 1.098681 | 0.092509 |
| CGAN | 0.048718 | 0.036091 | 0.422542 | 0.026361 |
| CVAE | 0.298339 | 0.225797 | 0.79771 | 0.092942 |
| AR | 0.200438 | 0.199092 | 1.210306 | 0.091039 |
| Low-Trend | KS | Wasserstein | KL | JS |
| DiffLOB | 0.425788 | 0.507738 | 3.529521 | 0.182637 |
| DiffLOB w/o C | 0.339051 | 0.36766 | 2.525023 | 0.141955 |
| Diff-CSDI | 0.755996 | 84.376958 | 6.563037 | 0.356456 |
| Diff-S4 | 0.431509 | 0.521119 | 3.855445 | 0.187511 |
| CGAN | 0.039677 | 0.044298 | 0.47366 | 0.023752 |
| CVAE | 0.38066 | 0.459526 | 2.89087 | 0.156796 |
| AR | 0.264977 | 0.296113 | 1.946188 | 0.107689 |
| High-Volatility | KS | Wasserstein | KL | JS |
| DiffLOB | 0.083474 | 0.06075 | 0.169118 | 0.03113 |
| DiffLOB w/o C | 0.292613 | 0.237796 | 1.004272 | 0.108261 |
| Diff-CSDI | 0.609586 | 59.726185 | 5.559404 | 0.286991 |
| Diff-S4 | 0.118421 | 0.12436 | 0.67194 | 0.064088 |
| CGAN | 0.178244 | 0.088973 | 0.524627 | 0.048186 |
| CVAE | 0.118761 | 0.077975 | 0.646276 | 0.071165 |
| AR | 0.083668 | 0.065337 | 0.454682 | 0.041336 |
| Low-Volatility | KS | Wasserstein | KL | JS |
| DiffLOB | 0.150047 | 0.072569 | 0.772114 | 0.061085 |
| DiffLOB w/o C | 0.163749 | 0.140627 | 1.38697 | 0.075512 |
| Diff-CSDI | 0.636904 | 59.84074 | 5.663091 | 0.293081 |
| Diff-S4 | 0.297515 | 0.160111 | 0.999069 | 0.111148 |
| CGAN | 0.16065 | 0.113201 | 1.285274 | 0.078348 |
| CVAE | 0.287089 | 0.16455 | 1.092421 | 0.100044 |
| AR | 0.244042 | 0.141 | 1.457307 | 0.09852 |
| High-Liquidity | KS | Wasserstein | KL | JS |
| DiffLOB | 0.137538 | 168.024319 | 0.208135 | 0.034988 |
| DiffLOB w/o C | 0.134555 | 179.447363 | 0.18559 | 0.03162 |
| Diff-CSDI | 0.318472 | 617445.7056 | 0.419245 | 0.05283 |
| Diff-S4 | 0.199552 | 229.470802 | 0.279902 | 0.050367 |
| CGAN | 0.389481 | 513.984844 | 1.1278 | 0.153755 |
| CVAE | 0.335492 | 365.126803 | 1.982426 | 0.229481 |
| AR | 0.422048 | 445.418425 | 1.840147 | 0.215084 |
| Low-Liquidity | KS | Wasserstein | KL | JS |
| DiffLOB | 0.126894 | 104.19346 | 0.099957 | 0.021029 |
| DiffLOB w/o C | 0.140489 | 110.790344 | 0.114877 | 0.025278 |
| Diff-CSDI | 0.311335 | 585813.0602 | 0.444758 | 0.073959 |
| Diff-S4 | 0.224048 | 142.265977 | 0.212572 | 0.048326 |
| CGAN | 0.214546 | 167.358666 | 0.315572 | 0.063397 |
| CVAE | 0.351886 | 231.117557 | 1.748266 | 0.220437 |
| AR | 0.410027 | 274.375898 | 1.572332 | 0.19979 |
| High-Imbalance | KS | Wasserstein | KL | JS |
| DiffLOB | 0.142787 | 154.156402 | 0.182522 | 0.032153 |
| DiffLOB w/o C | 0.130096 | 155.84261 | 0.181721 | 0.032042 |
| Diff-CSDI | 0.303622 | 629928.7738 | 0.363013 | 0.054523 |
| Diff-S4 | 0.163933 | 165.329592 | 0.180472 | 0.035623 |
| CGAN | 0.285831 | 342.915205 | 0.59001 | 0.095159 |
| CVAE | 0.274923 | 291.958093 | 1.485293 | 0.171144 |
| AR | 0.432061 | 397.430331 | 1.656605 | 0.202636 |
| Low-Imbalance | KS | Wasserstein | KL | JS |
| DiffLOB | 0.138717 | 147.853412 | 0.181154 | 0.034248 |
| DiffLOB w/o C | 0.153997 | 174.322966 | 0.204804 | 0.038629 |
| Diff-CSDI | 0.307549 | 593616.0608 | 0.43386 | 0.063705 |
| Diff-S4 | 0.198524 | 209.414158 | 0.253176 | 0.049452 |
| CGAN | 0.298427 | 356.49669 | 0.635989 | 0.101998 |
| CVAE | 0.290173 | 290.269725 | 1.529841 | 0.18089 |
| AR | 0.383488 | 338.46483 | 1.580578 | 0.186188 |

Table 2: Counterfactual Validity on AMZN.

Table [2](https://arxiv.org/html/2602.03776v1#S5.T2 "Table 2 ‣ 5.2 Counterfactual Validity ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") reports quantitative distances computed between counterfactual samples generated with a fixed future regime (e.g., high trend) and real market trajectories whose regime values fall into the same extreme quantile (top or bottom 20%).
cGAN performs competitively on trend-related metrics but degrades substantially for volatility, liquidity, and imbalance, indicating limited regime robustness.
DiffLOB without the control module performs relatively well under high-liquidity and high-imbalance conditions, suggesting that volume-driven regimes can be partially captured by the diffusion backbone alone, consistent with findings in (Wang and Ventre, [2025](https://arxiv.org/html/2602.03776v1#bib.bib88 "DiffVolume: diffusion models for volume generation in limit order books")).
However, across the majority of regimes and distance metrics, DiffLOB consistently achieves the lowest or near-lowest distances.
This demonstrates that explicitly modeling future regimes through the control module leads to more reliable and coherent counterfactual responses across diverse market conditions. Please see the complete table on the three stocks in Appendix  [D](https://arxiv.org/html/2602.03776v1#A4 "Appendix D Complete Counterfactual Table ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").

### 5.3 Counterfactual Usefulness

Finally, we assess the practical usefulness of counterfactual trajectories generated by DiffLOB.
We consider two tasks: trend prediction and liquidity prediction.
Trend prediction is formulated as a classification task that predicts the direction of future price movement, and is evaluated using accuracy (A​c​cAcc). Liquidity prediction is treated as a regression task that predicts future liquidity values, evaluated using the coefficient of determination (R2R^{2}).
For both tasks, models are trained on past 1 minute LOB data to predict future 1 minute regime. Models are evaluated on 1 March 2023, with performance reported separately on top 20% and bottom 20% of the regime distribution.
We compare three training settings: Real, using only real samples; Real \* 2, duplicating real data to control for dataset size; and Real+CF, augmenting real data with counterfactual trajectories to enrich extreme regime coverage.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | AMZN | | AAPL | | GOOG | |
| Trend |  |  |  |  |  |  |
| Prediction | Acc-High | Acc-Low | Acc-High | Acc-Low | Acc-High | Acc-Low |
| Real | 0.983 | 0.061 | 0.885 | 0.14 | 0.517 | 0.453 |
| Real \* 2 | 0.98 | 0.064 | 0.89 | 0.153 | 0.5 | 0.488 |
| Real + CF | 0.944 | 0.289 | 0.918 | 0.17 | 0.56 | 0.556 |
| Liquidity |  |  |  |  |  |  |
| Prediction | R^2-High | R^2-Low | R^2-High | R^2-Low | R^2-High | R^2-Low |
| Real | -1.568 | 0.086 | -2.512 | -0.184 | -0.742 | -0.039 |
| Real \* 2 | -1.656 | 0.127 | -2.525 | -0.26 | -0.796 | -0.011 |
| Real + CF | -1.509 | 0.278 | -1.432 | 0.17 | 0.017 | -0.053 |

Table 3: Counterfactual Usefulness on the three Stocks.

In Table [3](https://arxiv.org/html/2602.03776v1#S5.T3 "Table 3 ‣ 5.3 Counterfactual Usefulness ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"), we can see that augmenting real data with counterfactual samples improves performance on most high- and low-regime subsets, compared to training on real data alone.
The gains demonstrate that counterfactual trajectories provide complementary information that is scarce in real data, proving the usefulness of counterfactual trajectories generated by DiffLOB.

## 6 Conclusion

We introduce DiffLOB, a diffusion-based framework for controllable and counterfactual generation of limit order book trajectories.
By explicitly conditioning on future market regimes—including trend, volatility, liquidity, and order-flow imbalance—DiffLOB enables direct intervention on hypothetical future conditions.
Extensive experiments demonstrate that DiffLOB achieves superior controllable realism, generates coherent and regime-consistent counterfactual trajectories, and provides tangible benefits for downstream prediction tasks under extreme market regimes.
These results highlight the importance of explicit regime-aware control for realistic simulation and meaningful counterfactual analysis.

## References

* J. M. L. Alcaraz and N. Strodthoff (2022)
  Diffusion-based time series imputation and forecasting with structured state space models.
  Transactions on Machine Learning Research.
  Cited by: [§5](https://arxiv.org/html/2602.03776v1#S5.p1.1 "5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* B. D. Anderson (1982)
  Reverse-time diffusion equation models.
  Stochastic Processes and their Applications 12 (3),  pp. 313–326.
  Cited by: [Appendix A](https://arxiv.org/html/2602.03776v1#A1.p2.14 "Appendix A Diffusion Models Theory ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* L. Berti, B. Prenkaj, and P. Velardi (2025)
  TRADES: generating realistic market simulations with diffusion models.
  Proceedings of the Twenty-Eighth European Conference on Artificial Intelligence.
  Cited by: [§2](https://arxiv.org/html/2602.03776v1#S2.p1.1 "2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* A. Briola, S. Bartolucci, and T. Aste (2025a)
  Deep limit order book forecasting: a microstructural guide.
  Quantitative Finance 25 (7),  pp. 1101–1131.
  Cited by: [§1](https://arxiv.org/html/2602.03776v1#S1.p2.1 "1 Introduction ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* A. Briola, S. Bartolucci, and T. Aste (2025b)
  HLOB–information persistence and structure in limit order books.
  Expert Systems with Applications 266,  pp. 126078.
  Cited by: [§1](https://arxiv.org/html/2602.03776v1#S1.p2.1 "1 Introduction ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* A. Coletta, M. Prata, M. Conti, E. Mercanti, N. Bartolini, A. Moulin, S. Vyetrenko, and T. Balch (2021)
  Towards realistic market simulations: a generative adversarial networks approach.
  In Proceedings of the Second ACM International Conference on AI in Finance,
   pp. 1–9.
  Cited by: [§1](https://arxiv.org/html/2602.03776v1#S1.p2.1 "1 Introduction ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"),
  [§2](https://arxiv.org/html/2602.03776v1#S2.p1.1 "2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* R. Cont, M. Cucuringu, J. Kochems, and F. Prenzel (2023)
  Limit order book simulation with generative adversarial networks.
  Available at SSRN 4512356.
  Cited by: [§5](https://arxiv.org/html/2602.03776v1#S5.p1.1 "5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* M. D. Gould, M. A. Porter, S. Williams, M. McDonald, D. J. Fenn, and S. D. Howison (2013)
  Limit order books.
  Quantitative Finance 13 (11),  pp. 1709–1742.
  Cited by: [§1](https://arxiv.org/html/2602.03776v1#S1.p1.1 "1 Introduction ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* R. Hashimoto, Y. Tanaka, T. Takayanagi, Z. Piao, and K. Izumi (2025)
  Norm-salvaged embedding: improving condition alignment of synthetic time series generation in finance.
  In Proceedings of the 6th ACM International Conference on AI in Finance,
   pp. 838–846.
  Cited by: [§2](https://arxiv.org/html/2602.03776v1#S2.SS0.SSS0.Px1.p1.1 "Diffusion Models for Financial Time Series. ‣ 2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* J. Ho, A. Jain, and P. Abbeel (2020)
  Denoising diffusion probabilistic models.
  Advances in neural information processing systems 33,  pp. 6840–6851.
  Cited by: [§2](https://arxiv.org/html/2602.03776v1#S2.SS0.SSS0.Px1.p1.1 "Diffusion Models for Financial Time Series. ‣ 2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"),
  [§3.1](https://arxiv.org/html/2602.03776v1#S3.SS1.p2.1 "3.1 Problem Formulation ‣ 3 Methodology ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"),
  [§4.2](https://arxiv.org/html/2602.03776v1#S4.SS2.p1.8 "4.2 Training and Sampling ‣ 4 Experimental Setup ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* J. Ho and T. Salimans (2021)
  Classifier-free diffusion guidance.
  NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications.
  Cited by: [Appendix A](https://arxiv.org/html/2602.03776v1#A1.p3.1 "Appendix A Diffusion Models Theory ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"),
  [§4.2](https://arxiv.org/html/2602.03776v1#S4.SS2.p1.8 "4.2 Training and Sampling ‣ 4 Experimental Setup ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* R. Huang and T. Polak (2011)
  Lobster: limit order book reconstruction system.
  Available at SSRN 1977207.
  Cited by: [§4.1](https://arxiv.org/html/2602.03776v1#S4.SS1.p1.1 "4.1 Data and Preprocessing ‣ 4 Experimental Setup ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* H. Hultin, H. Hult, A. Proutiere, S. Samama, and A. Tarighati (2023)
  A generative model of a limit order book using recurrent neural networks.
  Quantitative Finance 23 (6),  pp. 931–958.
  Cited by: [§2](https://arxiv.org/html/2602.03776v1#S2.p1.1 "2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* D. P. Kingma and J. Ba (2015)
  Adam: A method for stochastic optimization.
  International Conference on Learning Representations.
  Cited by: [§4.2](https://arxiv.org/html/2602.03776v1#S4.SS2.p1.8 "4.2 Training and Sampling ‣ 4 Experimental Setup ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* K. J. Koa, Y. Ma, R. Ng, and T. Chua (2023)
  Diffusion variational autoencoder for tackling stochasticity in multi-step regression stock price prediction.
  In Proceedings of the 32nd ACM International Conference on Information and Knowledge Management,
   pp. 1087–1096.
  Cited by: [§2](https://arxiv.org/html/2602.03776v1#S2.SS0.SSS0.Px1.p1.1 "Diffusion Models for Financial Time Series. ‣ 2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* J. Li, Y. Liu, W. Liu, S. Fang, L. Wang, C. Xu, and J. Bian (2025)
  MarS: a financial market simulation engine powered by generative foundation model.
  In The Thirteenth International Conference on Learning Representations,
  Cited by: [§1](https://arxiv.org/html/2602.03776v1#S1.p2.1 "1 Introduction ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"),
  [§2](https://arxiv.org/html/2602.03776v1#S2.p1.1 "2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* P. Nagy, S. Frey, S. Sapora, K. Li, A. Calinescu, S. Zohren, and J. Foerster (2023)
  Generative ai for end-to-end limit order book modelling: a token-level autoregressive generative model of message flow using a deep state space network.
  In Proceedings of the Fourth ACM International Conference on AI in Finance,
   pp. 91–99.
  Cited by: [§1](https://arxiv.org/html/2602.03776v1#S1.p2.1 "1 Introduction ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"),
  [§2](https://arxiv.org/html/2602.03776v1#S2.p1.1 "2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"),
  [§5](https://arxiv.org/html/2602.03776v1#S5.p1.1 "5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* E. Perez, F. Strub, H. De Vries, V. Dumoulin, and A. Courville (2018)
  Film: visual reasoning with a general conditioning layer.
  In Proceedings of the AAAI conference on artificial intelligence,
  Vol. 32.
  Cited by: [§3.2](https://arxiv.org/html/2602.03776v1#S3.SS2.SSS0.Px4.p1.3 "Wavenet Module with FiLM Modulation. ‣ 3.2 DiffLOB Architecture ‣ 3 Methodology ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli (2015)
  Deep unsupervised learning using nonequilibrium thermodynamics.
  In International conference on machine learning,
   pp. 2256–2265.
  Cited by: [§2](https://arxiv.org/html/2602.03776v1#S2.SS0.SSS0.Px1.p1.1 "Diffusion Models for Financial Time Series. ‣ 2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* K. Sohn, H. Lee, and X. Yan (2015)
  Learning structured output representation using deep conditional generative models.
  Advances in neural information processing systems 28.
  Cited by: [§5](https://arxiv.org/html/2602.03776v1#S5.p1.1 "5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* Y. Song and S. Ermon (2019)
  Generative modeling by estimating gradients of the data distribution.
  Advances in neural information processing systems 32.
  Cited by: [§2](https://arxiv.org/html/2602.03776v1#S2.SS0.SSS0.Px1.p1.1 "Diffusion Models for Financial Time Series. ‣ 2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and B. Poole (2021)
  Score-based generative modeling through stochastic differential equations.
  International Conference on Learning Representations.
  Cited by: [Appendix A](https://arxiv.org/html/2602.03776v1#A1.p2.10 "Appendix A Diffusion Models Theory ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"),
  [§2](https://arxiv.org/html/2602.03776v1#S2.SS0.SSS0.Px1.p1.1 "Diffusion Models for Financial Time Series. ‣ 2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* Y. Tanaka, R. Hashimoto, T. Takayanagi, Z. Piao, Y. Murayama, and K. Izumi (2025)
  CoFinDiff: controllable financial diffusion model for time series generation.
  Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligenc.
  Cited by: [§2](https://arxiv.org/html/2602.03776v1#S2.SS0.SSS0.Px1.p1.1 "Diffusion Models for Financial Time Series. ‣ 2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* Y. Tashiro, J. Song, Y. Song, and S. Ermon (2021)
  CSDI: conditional score-based diffusion models for probabilistic time series imputation.
  Advances in Neural Information Processing Systems 34,  pp. 24804–24816.
  Cited by: [§5](https://arxiv.org/html/2602.03776v1#S5.p1.1 "5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* A. van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. W. Senior, and K. Kavukcuoglu (2016)
  WaveNet: A Generative Model for Raw Audio.
  In Proceedings of the 9th ISCA Speech Synthesis Workshop (SSW),
   pp. 125–131.
  Cited by: [§3.2](https://arxiv.org/html/2602.03776v1#S3.SS2.SSS0.Px1.p1.5 "Overall Backbone. ‣ 3.2 DiffLOB Architecture ‣ 3 Methodology ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* P. Vincent (2011)
  A connection between score matching and denoising autoencoders.
  Neural computation 23 (7),  pp. 1661–1674.
  Cited by: [§2](https://arxiv.org/html/2602.03776v1#S2.SS0.SSS0.Px1.p1.1 "Diffusion Models for Financial Time Series. ‣ 2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* Z. Wang and C. Ventre (2024)
  A financial time series denoiser based on diffusion models.
  In Proceedings of the 5th ACM International Conference on AI in Finance,
   pp. 72–80.
  Cited by: [§2](https://arxiv.org/html/2602.03776v1#S2.SS0.SSS0.Px1.p1.1 "Diffusion Models for Financial Time Series. ‣ 2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* Z. Wang and C. Ventre (2025)
  DiffVolume: diffusion models for volume generation in limit order books.
  In Proceedings of the 6th ACM International Conference on AI in Finance,
   pp. 587–595.
  Cited by: [§2](https://arxiv.org/html/2602.03776v1#S2.p1.1 "2 Related Work ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"),
  [§5.2](https://arxiv.org/html/2602.03776v1#S5.SS2.p5.1 "5.2 Counterfactual Validity ‣ 5 Experimental Results ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").
* L. Zhang, A. Rao, and M. Agrawala (2023)
  Adding conditional control to text-to-image diffusion models.
  In Proceedings of the IEEE/CVF international conference on computer vision,
   pp. 3836–3847.
  Cited by: [§3.2](https://arxiv.org/html/2602.03776v1#S3.SS2.SSS0.Px3.p1.1 "Control Module and Dual-stage Training. ‣ 3.2 DiffLOB Architecture ‣ 3 Methodology ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books").

## Appendix A Diffusion Models Theory

In the appendix, the variable tt denotes the *diffusion time step* (or noise level) used in the diffusion process, rather than the real-world market time index.
This is distinct from the notation ct+1:t+τc\_{t+1:t+\tau} in the main text, where tt refers to the current market time and t+1:t+τt+1:t+\tau denotes a future horizon.
The two uses of tt should not be confused.

DDPMs and Stochastic Differential Equations. Song et al. [[2021](https://arxiv.org/html/2602.03776v1#bib.bib1 "Score-based generative modeling through stochastic differential equations")] demonstrate that DDPMs can be understood from the perspective of stochastic differential equations (SDEs). Let {𝐱​(t)}t=0T\{\mathbf{x}(t)\}\_{t=0}^{T} be a stochastic diffusion process indexed by a continuous time variable t∈[0,T]t\in[0,T], evolving from 𝐱​(0)∼p0\mathbf{x}(0)\sim p\_{0}, the true data distribution, to 𝐱​(T)∼pT\mathbf{x}(T)\sim p\_{T}, approximately the tractable prior distribution. Denote the probability density function of 𝐱​(t)\mathbf{x}(t) by pt​(𝐱)p\_{t}(\mathbf{x}) and the transition kernel from 𝐱​(s)\mathbf{x}(s) to 𝐱​(t)\mathbf{x}(t) by ps​t​(𝐱​(t)|𝐱​(s))p\_{st}(\mathbf{x}(t)|\mathbf{x}(s)), for 0≤s<t≤T0\leq s<t\leq T. Then, we can use an SDE to represent such a forward diffusion process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝐱=𝐟​(𝐱,t)​d​t+g​(t)​d​𝐰,d\mathbf{x}=\mathbf{f}(\mathbf{x},t)\ dt+g(t)\ d\mathbf{w}, |  | (2) |

where 𝐟​(𝐱,t)​d​t\mathbf{f}(\mathbf{x},t)dt is referred to as the drift term, and g​(t)​d​𝐰g(t)d\mathbf{w} is referred to as the diffusion term. Here, 𝐰\mathbf{w} is a standard Wiener process and d​𝐰∼𝒩​(0,d​t​𝐈)d\mathbf{w}\sim\mathcal{N}(0,dt\mathbf{I}). The synthetic data generation process is the reverse process of Eq. ([2](https://arxiv.org/html/2602.03776v1#A1.E2 "In Appendix A Diffusion Models Theory ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books")), which is also an SDE Anderson [[1982](https://arxiv.org/html/2602.03776v1#bib.bib34 "Reverse-time diffusion equation models")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝐱=[𝐟​(𝐱,t)−g2​(t)​∇𝐱log⁡pt​(𝐱)]​d​t+g​(t)​d​𝐰¯,d\mathbf{x}=[\mathbf{f}(\mathbf{x},t)-g^{2}(t)\nabla\_{\mathbf{x}}\log p\_{t}(\mathbf{x})]\ dt+g(t)\ d\bar{\mathbf{w}}, |  | (3) |

where 𝐰¯\bar{\mathbf{w}} is a reverse-time Wiener process and ∇𝐱log⁡pt​(𝐱)\nabla\_{\mathbf{x}}\log p\_{t}(\mathbf{x}) is the score of the marginal distribution corresponding to each tt. It starts from an initial noise sample 𝐱​(T)∼pT\mathbf{x}(T)\sim p\_{T} and gradually denoises it step by step following Eq. ([3](https://arxiv.org/html/2602.03776v1#A1.E3 "In Appendix A Diffusion Models Theory ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books")). Theoretically, if T→∞T\rightarrow\infty, we obtain 𝐱​(0)∼p0\mathbf{x}(0)\sim p\_{0}. To estimate ∇𝐱log⁡pt​(𝐱)\nabla\_{\mathbf{x}}\log p\_{t}(\mathbf{x}), the score network 𝐬θ​(𝐱,t)\mathbf{s}\_{\mathbf{\theta}}(\mathbf{x},t) is trained using the objective function

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ(t)𝔼t𝔼𝐱​(0)𝔼𝐱​(t)|𝐱​(0)[||𝐬θ(𝐱(t),t)−∇𝐱​(t)logp0​t(𝐱(t)|𝐱(0))||22],\!\!\kappa(t)\mathbb{E}\_{t}\mathbb{E}\_{\mathbf{x}(0)}\mathbb{E}\_{\mathbf{x}(t)|\mathbf{x}(0)}\!\big[||\mathbf{s}\_{\theta}(\mathbf{x}(t),t)\!-\!\nabla\_{\mathbf{x}(t)}\!\log p\_{0t}(\mathbf{x}(t)|\mathbf{x}(0))||^{2}\_{2}\big], |  | (4) |

where κ:[0,T]→ℝ+\kappa:[0,T]\rightarrow\mathbb{R}^{+} is a positive weight and t∼𝒰​[0,T]t\sim\mathcal{U}[0,T]. Typically, the continuous form of the DDPM forward process is chosen to be

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝐱=−β​(t)2​𝐱​d​t+β​(t)​d​𝐰,d\mathbf{x}=-\frac{\beta(t)}{2}\mathbf{x}\ dt+\sqrt{\beta(t)}\ d\mathbf{w}, |  | (5) |

i.e., 𝐟​(𝐱,t)=−β​(t)2​𝐱\mathbf{f}(\mathbf{x},t)=-\frac{\beta(t)}{2}\mathbf{x} and g​(t)=β​(t)g(t)=\sqrt{\beta(t)}. Substituting 𝐟​(𝐱,t)\mathbf{f}(\mathbf{x},t) and g​(t)g(t) in ([3](https://arxiv.org/html/2602.03776v1#A1.E3 "In Appendix A Diffusion Models Theory ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books")), we can get the backward process in SDE form for DDPM.

Conditional DDPMs. How do we inject the conditioning 𝐜\mathbf{c} into the training and sampling process? Here we follow the classifier-free guidance approach Ho and Salimans [[2021](https://arxiv.org/html/2602.03776v1#bib.bib60 "Classifier-free diffusion guidance")], combining the conditional and unconditional models as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇𝐱log⁡p~​(𝐱|𝐜)=(1+ω)​∇𝐱log⁡p​(𝐱|𝐜)−ω​∇𝐱log⁡p​(𝐱),\nabla\_{\mathbf{x}}\log\tilde{p}(\mathbf{x}|\mathbf{c})=(1+\omega)\nabla\_{\mathbf{x}}\log p(\mathbf{x}|\mathbf{c})-\omega\nabla\_{\mathbf{x}}\log p(\mathbf{x}), |  | (6) |

where ∇𝐱log⁡p​(𝐱|𝐜)\nabla\_{\mathbf{x}}\log p(\mathbf{x}|\mathbf{c}) represents the conditional and ∇𝐱log⁡p​(𝐱)\nabla\_{\mathbf{x}}\log p(\mathbf{x}) represents the unconditional score, corresponding to the conditional and unconditional model distributions. Eq. ([6](https://arxiv.org/html/2602.03776v1#A1.E6 "In Appendix A Diffusion Models Theory ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books")) reduces to the unconditional score when ω=0\omega=0, or recovers the conditional score when ω=1\omega=1.

## Appendix B Training and Sampling Algorithms

Algorithm 1  Dual Stage Training Algorithm

1: Input: future trajectories 𝐱t+1:t+τ\mathbf{x}\_{t+1:t+\tau}, schedule β​(t)\beta(t)condition 𝐜=x1:t,ct+1:t+τtrend,ct+1:t+τvol,ct+1:t+τliq,ct+1:t+τimb\mathbf{c}=x\_{1:t},\,c^{\text{trend}}\_{t+1:t+\tau},\,c^{\text{vol}}\_{t+1:t+\tau},\,c^{\text{liq}}\_{t+1:t+\tau},\,c^{\text{imb}}\_{t+1:t+\tau}

2: Stage 1

3: Initialize model parameters θ={θbase,θctrl}\theta=\{\theta\_{\text{base}},\theta\_{\text{ctrl}}\}, freeze θctrl\theta\_{\text{ctrl}}

4: for each training step do

5:  Sample diffusion time t∼𝒰​(0,1)t\sim\mathcal{U}(0,1)

6:  Sample noise 𝐳∼𝒩​(𝟎,𝐈)\mathbf{z}\sim\mathcal{N}(\mathbf{0},\mathbf{I})

7:  Compute 𝐟​(𝐱,t),g​(t)\mathbf{f}(\mathbf{x},t),g(t) by β​(t)\beta(t)

8:  Get perturbed data future trajectory

9:  Update θbase\theta\_{\text{base}} by minimizing the objective in Eq. ([4](https://arxiv.org/html/2602.03776v1#A1.E4 "In Appendix A Diffusion Models Theory ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"))

10: end for

11:

12: Stage 2

13: Freeze model parameters θbase\theta\_{\text{base}}, unfreeze θctrl\theta\_{\text{ctrl}}

14: for each training step do

15:  Sample diffusion time t∼𝒰​(0,1)t\sim\mathcal{U}(0,1)

16:  Sample noise 𝐳∼𝒩​(𝟎,𝐈)\mathbf{z}\sim\mathcal{N}(\mathbf{0},\mathbf{I})

17:  Compute 𝐟​(𝐱,t),g​(t)\mathbf{f}(\mathbf{x},t),g(t) from the schedule

18:  Get perturbed data future trajectory

19:  Update θctrl\theta\_{\text{ctrl}} by minimizing the objective in Eq. ([4](https://arxiv.org/html/2602.03776v1#A1.E4 "In Appendix A Diffusion Models Theory ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"))

20: end for

21: Output: Network 𝐬θ​(𝐱,t,𝐜)\mathbf{s}\_{\theta}(\mathbf{x},t,\mathbf{c})




Algorithm 2  Sampling Algorithm

1: Input: number of steps NN, schedule β​(t)\beta(t), condition 𝐜=x1:t,ct+1:t+τtrend,ct+1:t+τvol,ct+1:t+τliq,ct+1:t+τimb\mathbf{c}=x\_{1:t},\,c^{\text{trend}}\_{t+1:t+\tau},\,c^{\text{vol}}\_{t+1:t+\tau},\,c^{\text{liq}}\_{t+1:t+\tau},\,c^{\text{imb}}\_{t+1:t+\tau}, guidance scale ww, network 𝐬θ​(𝐱,t,𝐜)\mathbf{s}\_{\theta}(\mathbf{x},t,\mathbf{c})

2: 𝐱1∼𝒩​(𝟎,𝐈)\mathbf{x}\_{1}\sim\mathcal{N}(\mathbf{0},\mathbf{I})

3: for i=N,N−1,…,1i=N,N-1,\dots,1 do

4:  Set diffusion time t←i/Nt\leftarrow i/N, step size Δ​t←1/N\Delta t\leftarrow 1/N

5:  Sample noise 𝐳∼𝒩​(𝟎,𝐈)\mathbf{z}\sim\mathcal{N}(\mathbf{0},\mathbf{I})

6:  Evaluate conditional score 𝐬c←𝐬θ​(𝐱t,t,𝐜)\mathbf{s}\_{c}\leftarrow\mathbf{s}\_{\theta}(\mathbf{x}\_{t},t,\mathbf{c})

7:  Evaluate unconditional score 𝐬∅←𝐬θ​(𝐱t,t,∅)\mathbf{s}\_{\emptyset}\leftarrow\mathbf{s}\_{\theta}(\mathbf{x}\_{t},t,\varnothing)

8:  Apply classifier-free guidance:
𝐬←(1+w)​𝐬c−w​𝐬∅\mathbf{s}\leftarrow(1+w)\mathbf{s}\_{c}-w\,\mathbf{s}\_{\emptyset}

9:  Update by ancestral sampling:

|  |  |  |
| --- | --- | --- |
|  | 𝐱t−Δ​t←𝐱t+(12​β​(t)​𝐱t+β​(t)​𝐬)​Δ​t+β​(t)​Δ​t​𝐳\mathbf{x}\_{t-\Delta t}\leftarrow\mathbf{x}\_{t}+\Big(\tfrac{1}{2}\beta(t)\mathbf{x}\_{t}+\beta(t)\mathbf{s}\Big)\Delta t+\sqrt{\beta(t)\Delta t}\,\mathbf{z} |  |

10: end for

11: Output: generated trajectory 𝐱^0←𝐱0\hat{\mathbf{x}}\_{0}\leftarrow\mathbf{x}\_{0}

![Refer to caption](figures/volume_distribution_AMZN.png)


Figure 8: Marginal Volume Distribution across Price Levels.

We adopt a two-stage training strategy to enable stable and effective regime control. During training, conditions are randomly dropped with probability 0.50.5 to enable classifier-free guidance.
In the first stage, we train the diffusion backbone together with the regime encoders while excluding the control module, allowing the model to learn the unconditional and condition-aware LOB dynamics.
In the second stage, we freeze all previously trained parameters and optimize only the control module, which injects regime-dependent intervention signals into the backbone.
This design ensures that counterfactual control is learned as a residual modification on top of a well-trained generative model, avoiding degradation of base dynamics.

At inference time, we generate LOB trajectories using an ancestral sampling procedure for the variance-preserving SDE.
Classifier-free guidance is applied during sampling by combining conditional and unconditional score estimates, enabling continuous control over the strength of regime interventions. The complete training and sampling algorithm are shown in Algorithms [1](https://arxiv.org/html/2602.03776v1#alg1 "Algorithm 1 ‣ Appendix B Training and Sampling Algorithms ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") and [2](https://arxiv.org/html/2602.03776v1#alg2 "Algorithm 2 ‣ Appendix B Training and Sampling Algorithms ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books"), respectively.

## Appendix C Volume Distribution

Figure [8](https://arxiv.org/html/2602.03776v1#A2.F8 "Figure 8 ‣ Appendix B Training and Sampling Algorithms ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") shows the marginal volume distributions across individual price levels on both the ask and bid sides. DiffLOB generally reproduces the empirical distributional shapes across depth levels, capturing both the scale and relative variation of volumes from the best quotes to deeper levels. While minor deviations remain at certain price levels, DiffLOB avoids the severe mode collapse or tail distortion observed in some baselines. In contrast, cGAN and cVAE exhibit noticeable mismatches, including shifted modes and overly concentrated densities, while the autoregressive model tends to generate excessively dispersed distributions. Overall, DiffLOB provides a more balanced approximation of marginal volume distributions across price levels.

## Appendix D Complete Counterfactual Table

Table [4](https://arxiv.org/html/2602.03776v1#A4.T4 "Table 4 ‣ Appendix D Complete Counterfactual Table ‣ DiffLOB: Diffusion Models for Counterfactual Generation in Limit Order Books") reports distributional distances between counterfactual trajectories generated under extreme regime interventions and real trajectories observed in the corresponding regimes, evaluated across three stocks. Overall, DiffLOB achieves consistently low distances across most regimes and assets, indicating stable counterfactual alignment with real market behavior. In particular, DiffLOB performs strongly under volatility, liquidity, and imbalance interventions, where it frequently attains the lowest or near-lowest Wasserstein, KL, and JS distances.

We observe that certain baselines exhibit localized strengths: cGAN achieves relatively low distances under trend interventions, while removing the control module (DiffLOB w/o C) yields competitive results in some high-liquidity and high-imbalance cases. However, these improvements are not consistent across regimes or assets. In contrast, DiffLOB maintains robust performance across different regime types and stocks, suggesting that explicit regime-aware control leads to more reliable counterfactual generation overall.

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | AMZN | | | | AAPL | | | | GOOG | | | |
| High-Trend | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS |
| DiffLOB | 0.444095 | 0.522512 | 2.517532 | 0.180279 | 0.527486 | 0.705667 | 3.79866 | 0.228299 | 0.319797 | 0.38452 | 1.943212 | 0.130711 |
| DiffLOB wo C | 0.515225 | 0.801835 | 4.879508 | 0.265181 | 0.52187 | 0.700273 | 3.706363 | 0.225847 | 0.400386 | 0.548083 | 3.015241 | 0.170459 |
| Diff-CSDI | 0.627345 | 65.274135 | 5.855148 | 0.307245 | 0.650097 | 77.661673 | 6.409168 | 0.346118 | 0.608903 | 51.355576 | 5.459767 | 0.2802 |
| Diff-S4 | 0.292354 | 0.264849 | 1.098681 | 0.092509 | 0.479872 | 0.593335 | 2.674102 | 0.19118 | 0.204638 | 0.264558 | 1.397245 | 0.087298 |
| CGAN | 0.048718 | 0.036091 | 0.422542 | 0.026361 | 0.826926 | 2.46174 | 9.609552 | 0.472167 | 0.51297 | 0.959163 | 5.462742 | 0.262343 |
| CVAE | 0.298339 | 0.225797 | 0.79771 | 0.092942 | 0.376703 | 0.440777 | 1.364931 | 0.123675 | 0.06105 | 0.035715 | 0.236427 | 0.049655 |
| AR | 0.200438 | 0.199092 | 1.210306 | 0.091039 | 0.339528 | 0.367727 | 1.093274 | 0.098998 | 0.059685 | 0.034748 | 0.21401 | 0.034285 |
| Low-Trend | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS |
| DiffLOB | 0.425788 | 0.507738 | 3.529521 | 0.182637 | 0.466021 | 0.663595 | 2.969223 | 0.18528 | 0.418144 | 0.357243 | 3.623893 | 0.174686 |
| DiffLOB wo C | 0.339051 | 0.36766 | 2.525023 | 0.141955 | 0.372399 | 0.52205 | 2.179232 | 0.141017 | 0.389908 | 0.326069 | 3.413639 | 0.161795 |
| Diff-CSDI | 0.755996 | 84.376958 | 6.563037 | 0.356456 | 0.703418 | 93.138326 | 6.243724 | 0.337338 | 0.598181 | 45.326588 | 5.281554 | 0.267412 |
| Diff-S4 | 0.431509 | 0.521119 | 3.855445 | 0.187511 | 0.226887 | 0.342775 | 1.410633 | 0.094289 | 0.43068 | 0.359478 | 3.91257 | 0.192965 |
| CGAN | 0.039677 | 0.044298 | 0.47366 | 0.023752 | 0.821983 | 2.436247 | 9.382776 | 0.462602 | 0.267701 | 0.179529 | 1.760093 | 0.108268 |
| CVAE | 0.38066 | 0.459526 | 2.89087 | 0.156796 | 0.192543 | 0.262382 | 1.078224 | 0.074031 | 0.299508 | 0.201727 | 1.934686 | 0.122522 |
| AR | 0.264977 | 0.296113 | 1.946188 | 0.107689 | 0.365958 | 0.535547 | 2.296313 | 0.139862 | 0.182677 | 0.110635 | 0.701304 | 0.061796 |
| High-Volatilty | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS |
| DiffLOB | 0.083474 | 0.06075 | 0.169118 | 0.03113 | 0.195453 | 0.170572 | 0.390789 | 0.063731 | 0.208521 | 0.162132 | 0.958381 | 0.114761 |
| DiffLOB wo C | 0.292613 | 0.237796 | 1.004272 | 0.108261 | 0.212819 | 0.188072 | 0.31742 | 0.062189 | 0.276429 | 0.18771 | 0.753739 | 0.099716 |
| Diff-CSDI | 0.609586 | 59.726185 | 5.559404 | 0.286991 | 0.585045 | 67.233425 | 5.500033 | 0.286357 | 0.573925 | 46.365704 | 5.005716 | 0.252426 |
| Diff-S4 | 0.118421 | 0.12436 | 0.67194 | 0.064088 | 0.309172 | 0.287524 | 0.65901 | 0.086488 | 0.242306 | 0.202847 | 1.323483 | 0.142103 |
| CGAN | 0.178244 | 0.088973 | 0.524627 | 0.048186 | 0.813774 | 2.573336 | 9.687475 | 0.478825 | 0.483661 | 0.512713 | 2.530705 | 0.195179 |
| CVAE | 0.118761 | 0.077975 | 0.646276 | 0.071165 | 0.277909 | 0.230906 | 0.763321 | 0.086946 | 0.204925 | 0.180972 | 1.319116 | 0.140161 |
| AR | 0.083668 | 0.065337 | 0.454682 | 0.041336 | 0.108995 | 0.103518 | 0.617903 | 0.061673 | 0.208233 | 0.161 | 0.85236 | 0.120365 |
| Low-Volatility | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS |
| DiffLOB | 0.150047 | 0.072569 | 0.772114 | 0.061085 | 0.263016 | 0.16332 | 1.228604 | 0.080622 | 0.171852 | 0.071879 | 1.067833 | 0.095288 |
| DiffLOB wo C | 0.163749 | 0.140627 | 1.38697 | 0.075512 | 0.197904 | 0.12845 | 1.387818 | 0.087776 | 0.201614 | 0.089192 | 1.05244 | 0.081389 |
| Diff-CSDI | 0.636904 | 59.84074 | 5.663091 | 0.293081 | 0.634541 | 66.696715 | 5.392071 | 0.279371 | 0.56042 | 45.873914 | 5.429973 | 0.277177 |
| Diff-S4 | 0.297515 | 0.160111 | 0.999069 | 0.111148 | 0.19326 | 0.126173 | 1.192786 | 0.086189 | 0.190067 | 0.080766 | 1.689373 | 0.118913 |
| CGAN | 0.16065 | 0.113201 | 1.285274 | 0.078348 | 0.850427 | 2.242279 | 9.860524 | 0.47597 | 0.353784 | 0.206637 | 1.998859 | 0.146298 |
| CVAE | 0.287089 | 0.16455 | 1.092421 | 0.100044 | 0.297702 | 0.188888 | 1.299558 | 0.097106 | 0.149426 | 0.08095 | 1.107241 | 0.098775 |
| AR | 0.244042 | 0.141 | 1.457307 | 0.09852 | 0.362483 | 0.292242 | 1.783818 | 0.118306 | 0.124769 | 0.070454 | 0.925041 | 0.092233 |
| High-Liquidity | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS |
| DiffLOB | 0.137538 | 168.024319 | 0.208135 | 0.034988 | 0.123554 | 93.884826 | 0.149982 | 0.025053 | 0.150165 | 184.78402 | 0.204472 | 0.033355 |
| DiffLOB wo C | 0.134555 | 179.447363 | 0.18559 | 0.03162 | 0.127951 | 105.880109 | 0.171677 | 0.02943 | 0.161624 | 194.000928 | 0.203039 | 0.036367 |
| Diff-CSDI | 0.318472 | 617445.7056 | 0.419245 | 0.05283 | 0.265748 | 611953.9495 | 0.303013 | 0.034818 | 0.282669 | 592234.437 | 0.412651 | 0.040742 |
| Diff-S4 | 0.199552 | 229.470802 | 0.279902 | 0.050367 | 0.154274 | 137.216909 | 0.22666 | 0.034013 | 0.239978 | 290.128272 | 0.467916 | 0.068077 |
| CGAN | 0.389481 | 513.984844 | 1.1278 | 0.153755 | 0.629324 | 407.898305 | 4.29376 | 0.320787 | 0.222264 | 312.509538 | 0.411387 | 0.064169 |
| CVAE | 0.335492 | 365.126803 | 1.982426 | 0.229481 | 0.327466 | 238.102708 | 2.251998 | 0.219447 | 0.262501 | 315.088815 | 1.339358 | 0.153376 |
| AR | 0.422048 | 445.418425 | 1.840147 | 0.215084 | 0.339363 | 246.09984 | 1.292155 | 0.159703 | 0.363537 | 398.86276 | 1.221241 | 0.169614 |
| Low-Liquidity | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS |
| DiffLOB | 0.126894 | 104.19346 | 0.099957 | 0.021029 | 0.084143 | 42.026082 | 0.069565 | 0.015318 | 0.092995 | 93.784744 | 0.085606 | 0.01421 |
| DiffLOB wo C | 0.140489 | 110.790344 | 0.114877 | 0.025278 | 0.107366 | 59.18505 | 0.09517 | 0.021885 | 0.119772 | 114.837243 | 0.092891 | 0.018651 |
| Diff-CSDI | 0.311335 | 585813.0602 | 0.444758 | 0.073959 | 0.241414 | 583028.0427 | 0.263493 | 0.046031 | 0.2421 | 563904.5316 | 0.257089 | 0.045014 |
| Diff-S4 | 0.224048 | 142.265977 | 0.212572 | 0.048326 | 0.156323 | 100.205219 | 0.146806 | 0.030725 | 0.284745 | 264.630407 | 0.379443 | 0.077248 |
| CGAN | 0.214546 | 167.358666 | 0.315572 | 0.063397 | 0.405366 | 194.850894 | 2.043172 | 0.201632 | 0.220858 | 195.332252 | 0.213879 | 0.047721 |
| CVAE | 0.351886 | 231.117557 | 1.748266 | 0.220437 | 0.292353 | 148.81207 | 1.759316 | 0.184381 | 0.286505 | 214.83184 | 1.315952 | 0.155636 |
| AR | 0.410027 | 274.375898 | 1.572332 | 0.19979 | 0.318566 | 162.614041 | 1.41773 | 0.178782 | 0.314595 | 235.733495 | 1.105514 | 0.145604 |
| High-Imbalance | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS |
| DiffLOB | 0.142787 | 154.156402 | 0.182522 | 0.032153 | 0.096136 | 78.177124 | 0.111676 | 0.020894 | 0.114366 | 109.782946 | 0.122575 | 0.025946 |
| DiffLOB wo C | 0.130096 | 155.84261 | 0.181721 | 0.032042 | 0.122496 | 102.745785 | 0.166532 | 0.028015 | 0.13587 | 140.918735 | 0.163554 | 0.03445 |
| Diff-CSDI | 0.303622 | 629928.7738 | 0.363013 | 0.054523 | 0.261696 | 584543.7943 | 0.267411 | 0.037983 | 0.28097 | 605229.5742 | 0.420215 | 0.0584 |
| Diff-S4 | 0.163933 | 165.329592 | 0.180472 | 0.035623 | 0.151473 | 119.539495 | 0.181243 | 0.032926 | 0.233546 | 307.169842 | 0.244487 | 0.046097 |
| CGAN | 0.285831 | 342.915205 | 0.59001 | 0.095159 | 0.484773 | 321.149662 | 2.998772 | 0.247907 | 0.206432 | 232.264564 | 0.237424 | 0.045062 |
| CVAE | 0.274923 | 291.958093 | 1.485293 | 0.171144 | 0.27594 | 206.120915 | 1.70025 | 0.170524 | 0.272183 | 284.282626 | 1.338171 | 0.156963 |
| AR | 0.432061 | 397.430331 | 1.656605 | 0.202636 | 0.309476 | 211.81121 | 1.028418 | 0.141033 | 0.342737 | 339.033016 | 1.231251 | 0.16067 |
| Low-Imbalance | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS | KS | Wasserstein | KL | JS |
| DiffLOB | 0.138717 | 147.853412 | 0.181154 | 0.034248 | 0.139123 | 81.910726 | 0.133491 | 0.025795 | 0.103865 | 100.254673 | 0.170693 | 0.026857 |
| DiffLOB wo C | 0.153997 | 174.322966 | 0.204804 | 0.038629 | 0.144674 | 88.387008 | 0.147903 | 0.031433 | 0.130511 | 131.0986 | 0.178989 | 0.032156 |
| Diff-CSDI | 0.307549 | 593616.0608 | 0.43386 | 0.063705 | 0.217315 | 577551.335 | 0.259399 | 0.04002 | 0.298334 | 673911.8064 | 0.46533 | 0.074212 |
| Diff-S4 | 0.198524 | 209.414158 | 0.253176 | 0.049452 | 0.162106 | 130.026248 | 0.229766 | 0.033792 | 0.268451 | 285.821643 | 0.493237 | 0.07783 |
| CGAN | 0.298427 | 356.49669 | 0.635989 | 0.101998 | 0.461362 | 250.252468 | 2.855038 | 0.22801 | 0.226664 | 242.115669 | 0.276046 | 0.05371 |
| CVAE | 0.290173 | 290.269725 | 1.529841 | 0.18089 | 0.278539 | 180.582864 | 1.551757 | 0.173447 | 0.266441 | 253.438419 | 1.22087 | 0.142463 |
| AR | 0.383488 | 338.46483 | 1.580578 | 0.186188 | 0.310076 | 190.853724 | 1.075461 | 0.154077 | 0.32443 | 297.557395 | 1.323793 | 0.171135 |

Table 4: Counterfactual Validity on the three Stocks.