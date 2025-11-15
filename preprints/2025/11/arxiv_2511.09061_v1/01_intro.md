---
authors:
- Hasib Uddin Molla
- Antony Ware
- Ilnaz Asadzadeh
- Nelson Mesquita Fernandes
doc_id: arxiv:2511.09061v1
family_id: arxiv:2511.09061
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Generative Pricing of Basket Options via Signature-Conditioned Mixture Density
  Networks
url_abs: http://arxiv.org/abs/2511.09061v1
url_html: https://arxiv.org/html/2511.09061v1
venue: arXiv q-fin
version: 1
year: 2025
---


Hasib Uddin Molla
Corresponding author: <mdhasibuddin.molla@ucalgary.ca>
Department of Mathematics and Statistics, University of Calgary, Calgary, Canada

Antony Ware
Department of Mathematics and Statistics, University of Calgary, Calgary, Canada

Ilnaz Asadzadeh
BMO Capital Markets, Toronto, Canada

Nelson Mesquita Fernandes
BMO Capital Markets, Toronto, Canada

###### Abstract

We present a generative framework for pricing European-style basket options by learning the conditional terminal distribution of the log arithmetic-weighted basket return. A Mixture Density Network (MDN) maps time-varying market inputs—encoded via truncated path signatures—to the full terminal density in a single forward pass. Traditional approaches either impose restrictive assumptions or require costly re-simulation whenever inputs change, limiting real-time use. Trained on Monte Carlo (MC) under GBM with time-varying volatility or local volatility, the MDN acts as a reusable surrogate distribution: once trained, it prices new scenarios by integrating the learned density. Across maturities, correlations, and basket weights, the learned densities closely match MC (low KL) and produce small pricing errors, while enabling *train-once, price-anywhere* reuse at inference-time latency.

Keywords: Mixture Density Networks, Option pricing, Conditional distribution, Geometric Brownian motion, Local volatility, Time-varying volatility, Time-varying rates, Path signatures.

## 1 Introduction

Accurate and efficient option pricing is fundamental to risk management and trading strategies in modern financial markets, particularly for institutional investors. Traditional pricing methods, such as the Black–Scholes model or numerical techniques like Monte Carlo simulations, remain widely used but exhibit notable limitations. Closed-form models often rely on restrictive assumptions, while numerical methods can be computationally expensive and struggle to capture complex market features, particularly in multi-asset portfolios or models with local volatility and time-varying parameters.

A promising alternative is to learn the terminal density of basket returns across a range of market inputs and then compute prices using risk-neutral expectations. However, this requires an accurate representation of the conditional probability density function (PDF) of the underlying asset under realistic dynamics—including time-dependent interest rates, dividend yields, local volatility surfaces, and asset correlations. In such cases, a closed-form expression for the probability density function of the underlying distribution is not available. In some cases, a semi-closed-form formula is available but requires additional complex computations. Furthermore, these solutions are typically limited to a single set of model parameters, which restricts their practicality in dynamic or data-driven settings.

To address these limitations, recent advances in deep learning offer a promising avenue. In particular, deep neural networks—when trained across a suitably chosen parameter space—can approximate the underlying asset’s density function with high flexibility and generalization capability. This transforms the pricing task into a “single solve” problem, meaning that once the model is trained, it can be used to price options for arbitrary combinations of input parameters, enabling efficient and scalable valuation across various market regimes.

### 1.1 From Risk-Neutral Expectation to Density Learning

Consider an asset price process S​(t;ϑ)S(t;\bm{\vartheta}), defined on the time interval t∈[0,T]t\in[0,T], where ϑ\bm{\vartheta} denotes the set of model parameters. For a given payoff function f​(S​(T;ϑ),K)f(S(T;\bm{\vartheta}),K), representing an option with maturity TT and strike price KK, the corresponding option price P​(T,K;ϑ)P(T,K;\bm{\vartheta}) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(T,K;ϑ)=DT​𝔼​[f​(S​(T;ϑ);K)],P(T,K;\bm{\vartheta})=D\_{T}\mathbb{E}\big[f(S(T;\bm{\vartheta});K)\big], |  | (1.1) |

where DT=e−r​TD\_{T}=e^{-rT} denotes the discount factor under constant interest rate rr.

If p​(y|ϑ,t)p(y|\bm{\vartheta},t) denotes the conditional probability density function of S​(t;ϑ)S(t;\bm{\vartheta}), then the expectation can be equivalently expressed as the integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(T,K;ϑ)=DT​∫f​(y;K)​p​(y|ϑ,T)​𝑑y.P(T,K;\bm{\vartheta})=D\_{T}\int f(y;K)p(y|\bm{\vartheta},T)dy. |  | (1.2) |

Hence, once the terminal conditional density p​(y|ϑ,T)p(y|\bm{\vartheta},T) of the underlying asset is known or accurately approximated, the option price can be computed for arbitrary parameters directly from this integral representation.

### 1.2 Mixture Density Networks for Distribution Approximation

Mixture models provide a flexible framework for approximating complex distributions by representing them as convex combinations of simpler components, typically Gaussian. Such mixtures capture multimodality, skewness, and other nonlinear features observed in empirical return distributions. A Mixture Density Network (MDN) extends this idea by using a neural network to output both the mixture weights and component parameters, allowing the learned model to represent highly flexible conditional distributions.

MDNs have proven effective in modelling stochastic systems across diverse fields, from acoustic modelling [Zen\_2014\_MDNAcousticModeling] and bioinformatics [Ji\_2005\_BetaMixtureBioinfo] to probabilistic forecasting [Zhang\_2020\_RegionalWindMDN] and volatility estimation. Several studies have also explored the financial applications of MDNs. Schittenkopf and Dorffner [Schittenkopf\_2001\_RND\_MDNet] extended the MDN framework to extract risk-neutral densities from observed option prices, while Schittenkopf et al. [Schittenkopf\_1998\_MDNVolatility] utilized MDNs to estimate and forecast stock market volatility. Li et al. [Li\_2024\_XRMDN] introduced a recurrent MDN architecture for demand forecasting in high-volatility mobility-on-demand systems.

Nevertheless, most existing work focuses on static settings, leaving open the challenge of incorporating time-varying and path-dependent features—such as evolving interest rates and dividend yields—into a unified probabilistic pricing framework.

### 1.3 Signature-Conditioned MDNs for Basket Option Pricing

In this work, we propose a signature-conditioned Mixture Density Network for generative pricing of European-style basket options. The model learns to approximate the conditional terminal distribution of basket returns under realistic market dynamics. These conditions include local volatility, asset correlations, and time-dependent interest rates and dividend yields.

A key modelling challenge is encoding time-varying parameters in a format suitable for deep learning. The use of truncated path signatures from rough path theory addresses this by providing a finite-dimensional and scalable feature representation that captures the essential temporal information of parameter trajectories. When combined with the MDN, they allow the model to efficiently and robustly learn mappings from dynamic market trajectories to the terminal distribution of the basket return.

Once trained, the model produces accurate option prices by integrating the learned density against the payoff function of European call and put options. This positions the MDN as a generative surrogate that replaces re-simulation at inference time. Empirical results demonstrate that our method achieves pricing accuracy comparable to benchmark Monte Carlo simulations while offering substantial computational speedups.

Relation to Generative Models in Finance: The Mixture density network approach for conditional density approximation belongs to the broader class of generative models. MDNs directly model p​(y|x)p(y|\textbf{x}) as a finite mixture and train via exact negative log-likelihood (NLL). In one-dimensional settings, this yields a lightweight, numerically stable, and inherently multi-modal representation. By contrast, variational autoencoders (VAEs) optimize an evidence-lower-bound (ELBO) surrogate [Kingma2014VAE, Rezende2014StochasticBackprop] and introduce additional encoder-decoder structures; while flexible, they add unnecessary latent complexity for 1D conditionals and are prone to posterior collapse. Normalizing flows provide exact likelihoods [Papamakarios2017MAF, Durkan2019NSF, Papamakarios2021NFJMLR] and excel in high-dimensional outputs, but are often over-parameterized for 1D tasks unless carefully constrained. Finally, diffusion and score-based models [Ho2020DDPM, Song2021SDE] offer state-of-the-art generative fidelity but require multi-step sampling and heavy conditioning, leading to higher computational cost. For the univariate conditional densities considered in this study, the MDN strikes the best balance between fidelity, numerical stability, and deployment cost. Nevertheless, flow- or diffusion-based frameworks remain promising candidates for future multivariate extensions, where richer joint structures among asset components become critical.

### 1.4 Background on Path Signatures

The signature of a path, introduced by Chen [chen\_1957\_IntgofPaths, chen\_1977\_ItePathIntg], is defined as an infinite sequence of iterated integrals of the path over increasing tensor orders. In practice, one often works with a truncated signature, and this truncation is theoretically justified by the fact that any path of finite pp-variation is uniquely determined by its signature truncated at order ⌊p⌋\lfloor p\rfloor (see Chapter 7 of [Friz\_2010\_RoughPaths]). Its ability to capture the essential characteristics of time series in a non-parametric manner has led to successful applications in various domains. In financial time series analysis, signatures have been effectively employed for both classification and prediction tasks [GyurkoLyons\_2014\_Extracting\_signature\_financial\_data, LyonsNi\_2014\_feature\_set\_financialdata], demonstrating their utility in handling complex, high-frequency data. Beyond predictive modelling, signatures have been applied to solve forward-backward stochastic differential equations (FBSDEs) numerically [QiFeng\_2023\_DeepSignatureFBSDEAlgo], particularly in non-Markovian settings where path-dependence plays a critical role.

The remainder of this paper is organized as follows.
Section [2](https://arxiv.org/html/2511.09061v1#S2 "2 Mixture Density Networks and Path Signatures ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") reviews the theoretical foundations of Mixture Density Networks and truncated path signatures.
Section [3](https://arxiv.org/html/2511.09061v1#S3 "3 The Mechanism of Training an MDN ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") describes the model setup, data generation under Geometric Brownian Motion with local volatility and time-varying rates, and the training procedure.
Section [4](https://arxiv.org/html/2511.09061v1#S4 "4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") presents numerical experiments comparing our approach to benchmark Monte Carlo pricing.
Finally, Section [5](https://arxiv.org/html/2511.09061v1#S5 "5 Conclusion ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") concludes with key insights and directions for future research.

## 2 Mixture Density Networks and Path Signatures

In this section, we provide a brief overview of the core components of our framework: the mixture density model, the mixture density network (MDN), and path signatures.

### 2.1 Mixture Density Model (Univariate)

A mixture model represents a complex probability distribution as a weighted sum of simpler component distributions. Formally, an arbitrary probability density function p​(y)p(y) can be approximated by a finite mixture of dd component densities ϕj​(y)\phi\_{j}(y) with corresponding mixing weights πj\pi\_{j} for j=1,⋯,dj=1,\cdots,d:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(y)=∑j=1dπj​ϕj​(y|𝝀j),p(y)=\sum\_{j=1}^{d}\pi\_{j}\phi\_{j}(y|\bm{\lambda}\_{j}), |  | (2.1) |

where 𝝀j\bm{\lambda}\_{j} denotes the parameters of the jj-th component distribution, determining its shape, scale and location. When component distribution and mixing coefficients are appropriately selected, this framework can approximate a wide variety of continuous probability distributions with high fidelity. In practice, mixtures of Gaussian distributions are frequently used due to their analytical tractability and universal approximation properties.

For the univariate target distribution p​(y)p(y), we consider univariate component distributions in the mixture model. For the Gaussian mixture model (GMM) of a univariate distribution,
𝝀j=(μj,δj)\bm{\lambda}\_{j}=(\mu\_{j},\delta\_{j}) and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕj​(y|μj,δj)=12​π​δj2​e−(y−μj)22​δj2,\phi\_{j}(y|\mu\_{j},\delta\_{j})=\frac{1}{\sqrt{2\pi\delta\_{j}^{2}}}e^{-\frac{(y-\mu\_{j})^{2}}{2\delta\_{j}^{2}}}, |  | (2.2) |

where, μj\mu\_{j} are mean and δj>0\delta\_{j}>0 are standard deviation of jj-th Gaussian distribution; and πj>0\pi\_{j}>0 decides how dd-Gaussian distributions are mixed together and must satisfy the normalization condition ∑j=1dπj=1\sum\_{j=1}^{d}\pi\_{j}=1.

The flexibility of the mixture model lies in its ability to approximate arbitrary probability density functions by adjusting the means μj\mu\_{j}, standard deviations δj\delta\_{j}, and mixing coefficients πj\pi\_{j} of the component Gaussians.

### 2.2 Mixture Density Network (Maximum Likelihood)

A mixture density network (MDN) is a hybrid architecture that combines a neural network with a mixture density model to approximate complex conditional probability distributions. Given an input (conditioning) feature vector 𝐱\mathbf{x}, an univariate MDN predicts the parameters of a (Gaussian) mixture model:

* •

  Mixing coefficients π​(𝐱)=(π1​(𝐱),⋯,πd​(𝐱)),\pi(\mathbf{x})=(\pi\_{1}(\mathbf{x}),\cdots,\pi\_{d}(\mathbf{x})),
* •

  Means μ​(𝐱)=(μ1​(𝐱),⋯,μd​(𝐱)),\mu(\mathbf{x})=(\mu\_{1}(\mathbf{x}),\cdots,\mu\_{d}(\mathbf{x})),
* •

  Standard deviations δ​(𝐱)=(δ1​(𝐱),⋯,δd​(𝐱)),\delta(\mathbf{x})=(\delta\_{1}(\mathbf{x}),\cdots,\delta\_{d}(\mathbf{x})),

and finally the conditional density p​(y|𝐱)p(y|\mathbf{x}) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(y|𝐱)=∑j=1dπj​(𝐱)×ϕj​(y|μj​(𝐱),δj​(𝐱)).p(y|\mathbf{x})=\sum\_{j=1}^{d}\pi\_{j}(\mathbf{x})\times\phi\_{j}(y|\mu\_{j}(\mathbf{x}),\delta\_{j}(\mathbf{x})). |  | (2.3) |

The network takes 𝐱∈ℝm0\mathbf{x}\in\mathbb{R}^{m\_{0}} as input and produces the three parameter vectors π​(𝐱),μ​(𝐱)\pi(\mathbf{x}),\mu(\mathbf{x}) and δ​(𝐱)\delta(\mathbf{x}). These outputs are subject to specific constraints to ensure they define a valid Gaussian mixture:

* •

  Mixing coefficients πj​(𝐱)\pi\_{j}(\mathbf{x}) must be non-negative and sum to 1. This is typically enforced by applying the softmax function to the raw network outputs for π\pi.
* •

  Standard deviations δj​(𝐱)\delta\_{j}(\mathbf{x}) must be strictly positive. A common choice is the exponential function [Bishop\_1994\_MDN] to map unconstrained outputs to positive values, though alternatives such as ELU [Normandin\_2023\_LinearPretrainRMDN, Wu\_2022\_3DHumanPoseMDN, Yang\_2021\_GANMDNInverseModeling] and softplus [Goodfellow\_2016\_DeepLearning, Han\_2022\_SurvivalMDN, Hepp\_2022\_MDNIntervals, Muzakka\_2024\_RBSMDN, Razavi\_2024\_FRMDN, Wang\_2022\_LikelihoodFreeMDN] are sometimes preferred to improve numerical stability.
* •

  Means μ​(𝐱)\mu(\mathbf{x}) are unconstrained real numbers and are typically output directly without transformation.

This structure enables the MDN to learn an arbitrary conditional distribution p​(y|𝐱)p(y|\mathbf{x}) from data. A general schematic of the MDN is shown in Figure [1](https://arxiv.org/html/2511.09061v1#S2.F1 "Figure 1 ‣ 2.2 Mixture Density Network (Maximum Likelihood) ‣ 2 Mixture Density Networks and Path Signatures ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks").

![Refer to caption](MDN.png)


Figure 1: Mixture Density Network

We now describe the internal structure of the MDN. First, the input layer calculates

|  |  |  |  |
| --- | --- | --- | --- |
|  | y0=g​(𝒲0​𝐱+β0),y\_{0}=g(\mathcal{W}\_{0}\mathbf{x}+\beta\_{0}), |  | (2.4) |

where y0∈ℝmy\_{0}\in\mathbb{R}^{m}; mm is the number of neurons in each hidden layer, 𝒲0\mathcal{W}\_{0} and β0\beta\_{0} are the weight matrix and bias vector of the input layer, and gg is the activation function.

Subsequently, each hidden layer h=1,⋯,Hh=1,\cdots,H computes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yh=g​(𝒲h​yh−1+βh),y\_{h}=g(\mathcal{W}\_{h}y\_{h-1}+\beta\_{h}), |  | (2.5) |

where yh∈ℝmy\_{h}\in\mathbb{R}^{m}; 𝒲h\mathcal{W}\_{h} and βh\beta\_{h} are the weight matrices and bias vectors of the hh-th hidden layer.

The final layer outputs the parameters of the mixture model as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π\displaystyle\pi | =gπ​(𝒲π​yH+βπ),\displaystyle=g\_{\pi}(\mathcal{W}\_{\pi}y\_{H}+\beta\_{\pi}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μ\displaystyle\mu | =gμ​(𝒲μ​yH+βμ),\displaystyle=g\_{\mu}(\mathcal{W}\_{\mu}y\_{H}+\beta\_{\mu}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | δ\displaystyle\delta | =gδ​(𝒲δ​yH+βδ),\displaystyle=g\_{\delta}(\mathcal{W}\_{\delta}y\_{H}+\beta\_{\delta}), |  |

where gπ,gμg\_{\pi},g\_{\mu} and gδg\_{\delta} are activation functions chosen to ensure appropriate constraints on the output.

The hidden layers of the network apply nonlinear transformations to the input, enabling the MDN to capture complex dependencies between 𝐱\mathbf{x} and the conditional distribution p​(y|𝐱)p(y|\mathbf{x}).
The choice of network architecture and activation functions in an MDN is problem-specific and may be adapted to ensure both numerical stability and appropriate modelling behaviour. In our implementation, we further customize the activation functions to (i) impose the initial condition exactly on the PDF and (ii) regularize the density in the presence of singularities.

Training Objective (Exact Likelihood). The network is trained by negative log-likelihood (NLL) with a *LogSumExp* stabilization:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡p​(𝐲i|𝐱i)\displaystyle\log p(\mathbf{y}^{i}|\mathbf{x}^{i}) | =∑k=1Mlog⁡(∑j=1dπj​(𝐱i)×ϕj​(yi,k|μj​(𝐱i),δj​(𝐱i)))\displaystyle=\sum\_{k=1}^{M}\log\left(\sum\_{j=1}^{d}\pi\_{j}(\mathbf{x}^{i})\times\phi\_{j}(y^{i,k}|\mu\_{j}(\mathbf{x}^{i}),\delta\_{j}(\mathbf{x}^{i}))\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∑k=1Mlog⁡(∑j=1dexp⁡(log⁡πj​(𝐱i)+log⁡(ϕj​(yi,k|μj​(𝐱i),δj​(𝐱i))))),\displaystyle=\sum\_{k=1}^{M}\log\left(\sum\_{j=1}^{d}\exp{\Big(\log\pi\_{j}(\mathbf{x}^{i})+\log\big(\phi\_{j}(y^{i,k}|\mu\_{j}(\mathbf{x}^{i}),\delta\_{j}(\mathbf{x}^{i}))\big)\Big)}\right), |  | (2.6) |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒNLL\displaystyle\mathcal{L}\_{\text{NLL}} | =−1Ns​∑i=1Nslog⁡p​(𝐲i|𝐱i).\displaystyle=-\frac{1}{N\_{s}}\sum\_{i=1}^{N\_{s}}\log p(\mathbf{y}^{i}|\mathbf{x}^{i}). |  | (2.7) |

### 2.3 Path Signatures

In this work, we use the truncated signature of trajectories as features in the MDN. Let T>0T>0 be a fixed time horizon, and let m∈ℕ,0<p∈ℝm\in\mathbb{N},0<p\in\mathbb{R}. Denote by 𝒱p​([0,T];ℝm)\mathcal{V}^{p}([0,T];\mathbb{R}^{m}) the space of continuous paths X:[0,T]→ℝmX:[0,T]\rightarrow\mathbb{R}^{m} of finite pp-variation. The signature of the path XX over the interval I=[0,T]I=[0,T] is defined as the infinite sequence of its iterated integrals:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​i​g​(X)0,T:=(1,𝕏0,T1,⋯,𝕏0,Tm,𝕏0,T1,1,𝕏0,T1,2,⋯,𝕏0,Tm,m,𝕏0,T1,1,1,⋯),Sig(X)\_{0,T}:=\Big(1,\;\mathbb{X}^{1}\_{0,T},\cdots,\mathbb{X}^{m}\_{0,T},\;\mathbb{X}^{1,1}\_{0,T},\;\mathbb{X}^{1,2}\_{0,T},\cdots,\mathbb{X}^{m,m}\_{0,T},\;\mathbb{X}^{1,1,1}\_{0,T},\cdots\Big), |  | (2.8) |

where each element corresponds to a multi-indexed iterated integral of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕏0,Ti1,⋯,il:=∫0<t<T𝕏0,ti1,⋯,il−1​𝑑Xtil=∫0<tl<T⋯​∫0<t1<t2𝑑Xt1i1​⋯​𝑑Xtlil,\mathbb{X}\_{0,T}^{i\_{1},\cdots,i\_{l}}:=\int\_{0<t<T}\mathbb{X}\_{0,t}^{i\_{1},\cdots,i\_{l-1}}dX^{i\_{l}}\_{t}=\int\_{0<t\_{l}<T}\cdots\int\_{0<t\_{1}<t\_{2}}dX\_{t\_{1}}^{i\_{1}}\cdots dX\_{t\_{l}}^{i\_{l}}, |  | (2.9) |

for l≥1l\geq 1 and ij∈{1,⋯,m}i\_{j}\in\{1,\cdots,m\}.
The zeroth level of the signature is defined to be 11 by convention. The first level of the signature is the collection of mm real numbers 𝕏0,T1,⋯,𝕏0,Tm\mathbb{X}^{1}\_{0,T},\cdots,\mathbb{X}^{m}\_{0,T} and the second level is the collection of m2m^{2} real numbers 𝕏0,T1,1,⋯,𝕏0,T1,m,𝕏0,T2,1,⋯,𝕏0,Tm,m\mathbb{X}^{1,1}\_{0,T},\cdots,\mathbb{X}^{1,m}\_{0,T},\mathbb{X}^{2,1}\_{0,T},\cdots,\mathbb{X}^{m,m}\_{0,T}. More generally, the ll-th level of the signature consists of all terms 𝕏0,Ti1,⋯,il\mathbb{X}^{i\_{1},\cdots,i\_{l}}\_{0,T} over the multi-indices of length ll.

When the path (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} is of finite variation, the iterated integrals in ([2.9](https://arxiv.org/html/2511.09061v1#S2.E9 "In 2.3 Path Signatures ‣ 2 Mixture Density Networks and Path Signatures ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks")) are interpreted as Riemann-Stiltjes integrals. When (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} is a continuous semi-martingale (e.g., Brownian motion or asset price processes or other stochastic processes), the integrals in ([2.9](https://arxiv.org/html/2511.09061v1#S2.E9 "In 2.3 Path Signatures ‣ 2 Mixture Density Networks and Path Signatures ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks")) are in the Stratonovich sense, aligning with rough path theory.

The truncated signature of XX up to level ll is denoted by S​i​g​(X)0,TlSig(X)^{l}\_{0,T} and is obtained by retaining all terms in the infinite sequence in ([2.8](https://arxiv.org/html/2511.09061v1#S2.E8 "In 2.3 Path Signatures ‣ 2 Mixture Density Networks and Path Signatures ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks")) up to (and including) level ll. This truncation yields a finite-dimensional feature representation that preserves the distinguishable characteristics of the path. One can choose ll to balance fidelity vs. parameter count; in our experiments, ll around 4-5 works well.

## 3 The Mechanism of Training an MDN

Training a Mixture Density Network (MDN) to price a specific derivative product involves several key decision points. A schematic overview of the MDN training process is presented in Figure [2](https://arxiv.org/html/2511.09061v1#S3.F2 "Figure 2 ‣ 3 The Mechanism of Training an MDN ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks").

![Refer to caption](MDN_Workflow.png)


Figure 2: MDN Training Workflow

Next, we will discuss all these aspects in detail.

### 3.1 Asset Price Model

Asset price dynamics in financial markets are commonly modelled using stochastic differential equations (SDEs), with popular choices including the Geometric Brownian Motion (GBM), the Heston stochastic volatility model, and various rough volatility models. In this work, we focus on models in which the asset price evolves under a GBM framework with generalized volatility structures.

#### 3.1.1 Geometric Brownian Motion (GBM)

Let r​(t)r(t) denote the risk-free interest rate and qj​(t)q\_{j}(t) the dividend rate of asset jj. Consider a portfolio of NN assets whose price processes are denoted by S​(t)=(S1​(t),⋯,SN​(t))S(t)=(S\_{1}(t),\cdots,S\_{N}(t)). Each asset Sj​(t)S\_{j}(t) follows the SDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sj​(t)=(r​(t)−qj​(t))​Sj​(t)​d​t+σj​(t,Sj​(t))​Sj​(t)​d​Wj​(t),Sj​(0)=s0,j,dS\_{j}(t)=(r(t)-q\_{j}(t))S\_{j}(t)dt+\sigma\_{j}(t,S\_{j}(t))S\_{j}(t)dW\_{j}(t),\;S\_{j}(0)=s\_{0,j}, |  | (3.1) |

for t∈[0,T]t\in[0,T] and j=1,2,⋯,N,j=1,2,\cdots,N, where Wj​(t)W\_{j}(t) denotes the standard Brownian motion, and σj​(⋅,⋅)\sigma\_{j}(\cdot,\cdot) is the volatility function.
In this work, we consider two forms of volatility for each asset:

1. i.

   Time dependent volatility: σj​(t,Sj​(t))=σj​(t).\sigma\_{j}(t,S\_{j}(t))=\sigma\_{j}(t).
     
   In this setting, volatility varies with time but is independent of the asset’s current price. This can model market regimes where volatility follows a deterministic term structure.
2. ii.

   Local volatility: σj​(t,Sj​(t))=σj​(Sj​(t)).\sigma\_{j}(t,S\_{j}(t))=\sigma\_{j}(S\_{j}(t)).
     
   Here, volatility is a function of the asset’s spot price, allowing the model to capture empirical features such as volatility smiles and skews.

These formulations enable the modelling of more realistic market dynamics than the classical constant-volatility GBM.

#### 3.1.2 Correlation Structure of the Basket

In modelling a basket of NN assets, the correlation structure among their respective Brownian motions is an essential component. Let 𝐑∈ℝN×N\mathbf{R}\in\mathbb{R}^{N\times N} denote the correlation matrix governing the NN-dimensional Brownian motion vector:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (W1,⋯,WN)T.(W\_{1},\cdots,W\_{N})^{T}. |  | (3.2) |

Assuming that 𝐑\mathbf{R} is positive semi-definite and symmetric, it admits a Cholesky decomposition 𝐑=𝐋𝐋T\mathbf{R}=\mathbf{LL}^{T}, where 𝐋\mathbf{L} is a lower triangular matrix with strictly positive diagonal entries. Then, the correlated Brownian motion increments can be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (d​W1​(t),⋯,d​WN​(t))T=𝐋​(d​W~1​(t),⋯,d​W~N​(t))T,(dW\_{1}(t),\cdots,dW\_{N}(t))^{T}=\mathbf{L}(d\widetilde{W}\_{1}(t),\cdots,d\widetilde{W}\_{N}(t))^{T}, |  | (3.3) |

where d​W~1​(t),⋯,d​W~N​(t)d\widetilde{W}\_{1}(t),\cdots,d\widetilde{W}\_{N}(t) are independent Brownian motion increments. This construction ensures that the components of the vector (W1,⋯,WN)(W\_{1},\cdots,W\_{N}) follow the desired correlation structure specified by 𝐑\mathbf{R}.

### 3.2 Target Distribution

The structure of the option contract determines the choice of the target distribution. In this study, we consider a European-style option written on the weighted return of a basket of NN assets. Accordingly, the target is a univariate conditional distribution of the basket’s weighted return at a fixed terminal time.

The basket weights can be treated in two ways. If the basket’s composition is fixed, we may hold the weights constant throughout training. However, to enable pricing across a variety of portfolio compositions without retraining, the MDN can be parameterized to include the basket weights as part of the input. This allows the model to generalize over different weighting schemes and provides greater flexibility in practical applications.

log\log-space as the target of MDN: To improve the accuracy of the MDN approximation, we transform the target variable to log-space. Specifically, the MDN is trained to learn the distribution of the logarithm of the basket’s average return, resulting in a smoother, more stable learning target.

### 3.3 Training Data Generation

The generation of training data for the MDN is closely tied to both the choice of the underlying asset price model and the MDN’s parameterization. This section is divided into two subsections, each corresponding to a distinct volatility structure assumed under Geometric Brownian Motion (GBM) dynamics for the underlying assets. For each case, we provide a comprehensive list of model parameters along with the complete algorithm used to generate the training data.

The numerical experiments presented later in the paper are also organized according to these two cases. Before detailing the case-specific procedures, we first outline the general sampling strategies employed for the option maturity, the lower-triangular matrix 𝐋\mathbf{L} obtained from the Cholesky decomposition of the correlation matrix, and the time-varying market rates.

Sampling for maturity, TT: We define maturity TT in the interval (0,1](0,1], where T=1T=1 corresponds to one year. To ensure adequate coverage of both short- and long-term behaviours, we sample TT from [0.001,1.05][0.001,1.05], with more samples drawn near the boundaries.

Sampling of 𝐋\mathbf{L}: To generate a random sample of a valid correlation matrix 𝐑\mathbf{R}, we begin by randomly sampling a sequence of angles:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚯={α1,α2,⋯,αN​(N−1)2},αi∈(0,π),\mathbf{\Theta}=\Big\{\alpha\_{1},\alpha\_{2},\cdots,\alpha\_{\frac{N(N-1)}{2}}\Big\},\quad\alpha\_{i}\in(0,\pi), |  | (3.4) |

and define

|  |  |  |
| --- | --- | --- |
|  | ξi=sin⁡(αi),γi=cos⁡(αi).\xi\_{i}=\sin(\alpha\_{i}),\;\gamma\_{i}=\cos(\alpha\_{i}). |  |

Using these trigonometric components, we construct a lower triangular matrix 𝐋∈ℝN×N\mathbf{L}\in\mathbb{R}^{N\times N} as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐋=(100⋯0γ1ξ10⋯0γ2ξ2​γ3ξ2​ξ3⋯0⋮⋮⋮⋱⋮γNξN​γN+1ξN​ξN+1​γN+2⋯ξN​ξN+1​⋯​ξN​(N−1)2).\mathbf{L}=\begin{pmatrix}1&0&0&\cdots&0\\ \gamma\_{1}&\xi\_{1}&0&\cdots&0\\ \gamma\_{2}&\xi\_{2}\gamma\_{3}&\xi\_{2}\xi\_{3}&\cdots&0\\ \vdots&\vdots&\vdots&\ddots&\vdots\\ \gamma\_{N}&\xi\_{N}\gamma\_{N+1}&\xi\_{N}\xi\_{N+1}\gamma\_{N+2}&\cdots&\xi\_{N}\xi\_{N+1}\cdots\xi\_{\frac{N(N-1)}{2}}\end{pmatrix}. |  | (3.5) |

This construction ensures that the resulting matrix 𝐋𝐋T=𝐑\mathbf{LL}^{T}=\mathbf{R} is a valid correlation matrix—i.e., symmetric and positive semi-definite—and allows for flexible specification of inter-asset dependencies through parameterized random sampling.

Sampling of time-varying rates: As time-varying rates such as interest and dividends are parameters of the GBM model and will become the parameters of the MDN through the mixture model, we will need sample paths of the time-varying parameters to simulate the sample paths for the assets in the basket for the training of the MDN. In practice, such sample paths can be generated from historical data using resampling techniques (e.g., bootstrapping). In our experiments, we adopt the Cox-Ingersoll-Ross (CIR) process to simulate these paths:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​X​(t)=a​(b−X​(t))​d​t+c​X​(t)​d​W​(t),X​(0)=x0,dX(t)=a(b-X(t))dt+c\sqrt{X}(t)dW(t),\;X(0)=x\_{0}, |  | (3.6) |

where a,ba,b and cc are fixed, stationary parameters. For each asset jj in the basket, we generate random initial values x0,jx\_{0,j} and simulate the corresponding time-varying paths using the CIR model.

Now, we will discuss the details of the training data generation for two different volatility structures under GBM.

#### 3.3.1 GBM with Time-varying Volatility

Consider a basket of NN assets, whose price processes S​(t)=(S1​(t),⋯,SN​(t))S(t)=(S\_{1}(t),\cdots,S\_{N}(t)) follow geometric Brownian motion (GBM) dynamics with time-varying volatilities. The stochastic differential equation (SDE) for each asset j=1,⋯,Nj=1,\cdots,N is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sj​(t)=(r​(t)−qj​(t))​Sj​(t)​d​t+σj​(t)​Sj​(t)​d​Wj​(t),Sj​(0)=s0,j,dS\_{j}(t)=(r(t)-q\_{j}(t))S\_{j}(t)dt+\sigma\_{j}(t)S\_{j}(t)dW\_{j}(t),\;S\_{j}(0)=s\_{0,j}, |  | (3.7) |

where t∈[0,T]t\in[0,T]. The Brownian motions (W1​(t),⋯,WN​(t))(W\_{1}(t),\cdots,W\_{N}(t)) are correlated and correlation is specified by a correlation matrix 𝐑N×N.\mathbf{R}^{N\times N}.

Model parameters:  The completed set of model parameters for the GBM system is denoted by

|  |  |  |
| --- | --- | --- |
|  | ϑ=(r​(⋅),(qj​(⋅),σj​(⋅))j=1N,𝐋),\bm{\vartheta}=\Big(r(\cdot),\big(q\_{j}(\cdot),\sigma\_{j}(\cdot)\big)\_{j=1}^{N},\mathbf{L}\Big), |  |

where r​(⋅)r(\cdot) is the time-varying risk-free interest rate, qj​(⋅)q\_{j}(\cdot) and σj​(⋅)\sigma\_{j}(\cdot) are the time-varying dividend rate and volatility for jjth asset in the basket. 𝐋\mathbf{L} is the lower triangular matrix from the Cholesky decomposition of the correlation matrix 𝐑\mathbf{R} of the basket, that is, 𝐑=𝐋𝐋T\mathbf{R}=\mathbf{LL}^{T}. The price process S​(t)S(t) is thus parametrized by ϑ\bm{\vartheta} and denoted by S​(t;ϑ)S(t;\bm{\vartheta}).

Training set generation: The Algorithm [1](https://arxiv.org/html/2511.09061v1#alg1 "Algorithm 1 ‣ 3.3.1 GBM with Time-varying Volatility ‣ 3.3 Training Data Generation ‣ 3 The Mechanism of Training an MDN ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") below summarizes the procedure used to generate the training data for the mixture density network (MDN), where the target is the weighted return of the basket with fixed basket weights.

Algorithm 1  Training Set Generation for Time-Varying GBM with Correlated Assets

Inputs: Initial basket asset price S​(0)S(0), Basket weight ww

Output: Training dataset (𝐱m,i,𝐲m,i)i,m{(\mathbf{x}^{m,i},\mathbf{y}^{m,i})}\_{i,m}

Step 1: Sample n1n\_{1} maturity values Ti∈[0,T]T^{i}\in[0,T]

Step 2: For each i=1,…,n1i=1,\dots,n\_{1}:

for m=1:n2m=1:n\_{2} do

- Sample initial values r0m,ir\_{0}^{m,i}, q0m,iq\_{0}^{m,i}, and σ0m,i\sigma\_{0}^{m,i}

- Generate time-varying paths rm,i​(t;r0m,i)r^{m,i}(t;r\_{0}^{m,i}), qm,i​(t;q0m,i)q^{m,i}(t;q\_{0}^{m,i}), and σm,i​(t;σ0m,i)\sigma^{m,i}(t;\sigma\_{0}^{m,i}) for t∈[0,Ti]t\in[0,T^{i}] using the CIR model

- Sample a lower-triangular matrix 𝐋m,i\mathbf{L}^{m,i} to define the correlation structure

- Form the parameter set:

|  |  |  |
| --- | --- | --- |
|  | ϑm,i=(rm,i​(⋅),(qjm,i​(⋅),σjm,i​(⋅))j=1N,𝐋m,i)\bm{\vartheta}^{m,i}=\Big(r^{m,i}(\cdot),\big(q\_{j}^{m,i}(\cdot),\sigma\_{j}^{m,i}(\cdot)\big)\_{j=1}^{N},\mathbf{L}^{m,i}\Big) |  |

- Simulate MM independent paths of asset price, {Sm,i,k​(t;ϑm,i)}k=1M\Big\{S^{m,i,k}(t;\bm{\vartheta}^{m,i})\Big\}\_{k=1}^{M} over t∈[0,Ti]t\in[0,T^{i}]

Step 3: Compute MDN targets:

|  |  |  |
| --- | --- | --- |
|  | 𝐲m,i={ym,i,k=log⁡(∑j=1Nwj​Sjm,i,k​(Ti;ϑm,i)Sj​(0))}k=1M\mathbf{y}^{m,i}=\Bigg\{y^{m,i,k}=\log\bigg(\sum\_{j=1}^{N}w\_{j}\frac{S\_{j}^{m,i,k}(T^{i};\;\bm{\vartheta}^{m,i})}{S\_{j}(0)}\bigg)\Bigg\}\_{k=1}^{M} |  |

Step 4: Define MDN inputs as 𝐱m,i=(ϑm,i,Ti)\mathbf{x}^{m,i}=(\bm{\vartheta}^{m,i},T^{i})

#### 3.3.2 GBM with Local Volatility

We consider a basket consisting of NN assets whose price processes S​(t)=(S1​(t),⋯,SN​(t))S(t)=(S\_{1}(t),\cdots,S\_{N}(t)), evolve according to geometric Brownian motion (GBM) dynamics with local volatilities. The dynamics of each asset j=1,⋯,Nj=1,\cdots,N are described by the following stochastic differential equation (SDE):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sj​(t)=(r​(t)−qj​(t))​Sj​(t)​d​t+σL​(Sj​(t))​Sj​(t)​d​Wj​(t),Sj​(0)=s0,j,dS\_{j}(t)=(r(t)-q\_{j}(t))S\_{j}(t)dt+\sigma\_{L}(S\_{j}(t))S\_{j}(t)dW\_{j}(t),\;S\_{j}(0)=s\_{0,j}, |  | (3.8) |

where t∈[0,T]t\in[0,T] and σL​(⋅)\sigma\_{L}(\cdot) denote the local volatility function. The Brownian motions (W1​(t),⋯,WN​(t))(W\_{1}(t),\cdots,W\_{N}(t)) are correlated, with the correlation structure captured by a correlation matrix 𝐑N×N\mathbf{R}^{N\times N}.

Model parameters: 
Let ϑ=(r​(⋅),(qj​(⋅))j=1N,𝐋)\bm{\vartheta}=\Big(r(\cdot),\big(q\_{j}(\cdot)\big)\_{j=1}^{N},\mathbf{L}\Big), denote the set of model parameters governing the risk-free interest rate, dividend yields, and the Cholesky factor 𝐋\mathbf{L} of the correlation matrix. Together with the local volatility parameter 𝝂\bm{\nu}, the full set of parameters for the GBM model is given by (ϑ,𝝂)(\bm{\vartheta},\bm{\nu}). Accordingly, the asset price process is written as S​(t;ϑ,𝝂)S(t;\bm{\vartheta},\bm{\nu}) to reflect the dependence on both parameter sets.

Training set generations: The procedure for generating the training dataset for the mixture density network (MDN) is summarized in Algorithm [2](https://arxiv.org/html/2511.09061v1#alg2 "Algorithm 2 ‣ 3.3.2 GBM with Local Volatility ‣ 3.3 Training Data Generation ‣ 3 The Mechanism of Training an MDN ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks"). The target in this case is also the weighted return of the basket, but we include the basket weights as part of the MDN input.

Algorithm 2  Training Set Generation for local-volatility GBM with Correlated Assets

Inputs: Initial basket asset price S​(0)S(0)

Output: Training dataset (𝐱m,i,𝐲m,i)i,m{(\mathbf{x}^{m,i},\mathbf{y}^{m,i})}\_{i,m}

Step 1: Sample n1n\_{1} maturity values Ti∈[0,T]T^{i}\in[0,T]

Step 2: For each i=1,…,n1i=1,\dots,n\_{1}:

for m=1:n2m=1:n\_{2} do

- Sample initial values r0m,ir\_{0}^{m,i} and q0m,iq\_{0}^{m,i}

- Generate time-varying paths rm,i​(t;r0m,i)r^{m,i}(t;r\_{0}^{m,i}) and qm,i​(t;q0m,i)q^{m,i}(t;q\_{0}^{m,i}) for t∈[0,Ti]t\in[0,T^{i}] using the CIR model

- Sample a lower-triangular matrix 𝐋m,i\mathbf{L}^{m,i} to define the correlation structure

- Sample local-volatility function parameters al​o​cm,i,bl​o​cm,ia\_{loc}^{m,i},b\_{loc}^{m,i} and cl​o​cm,ic\_{loc}^{m,i}

- Form the parameter set:

|  |  |  |
| --- | --- | --- |
|  | ϑm,i=(rm,i​(⋅),(qjm,i​(⋅))j=1N,𝐋m,i),\bm{\vartheta}^{m,i}=\Big(r^{m,i}(\cdot),\big(q\_{j}^{m,i}(\cdot)\big)\_{j=1}^{N},\mathbf{L}^{m,i}\Big), |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝝂m,i=((al​o​c,jm,i,bl​o​c,jm,i,cl​o​c,jm,i)J=1N)\bm{\nu}^{m,i}=\Big(\Big(a\_{loc,j}^{m,i},b\_{loc,j}^{m,i},c\_{loc,j}^{m,i}\Big)\_{J=1}^{N}\Big) |  |

- Simulate MM independent paths of asset price, {Sm,i,k​(t;ϑm,i,𝝂m,i)}k=1M\Big\{S^{m,i,k}(t;\bm{\vartheta}^{m,i},\bm{\nu}^{m,i})\Big\}\_{k=1}^{M} over t∈[0,Ti]t\in[0,T^{i}]

- Generate samples of the basket weights wm,i=(w1m,i,⋯,wNm,i)w^{m,i}=\Big(w\_{1}^{m,i},\cdots,w^{m,i}\_{N}\Big)

Step 3: Compute MDN targets:

|  |  |  |
| --- | --- | --- |
|  | 𝐲m,i={ym,i,k=log⁡(∑j=1Nwjm,i​Sjm,i,k​(Ti;ϑm,i,𝝂m,i)Sj​(0))}k=1M\mathbf{y}^{m,i}=\Bigg\{y^{m,i,k}=\log\bigg(\sum\_{j=1}^{N}w^{m,i}\_{j}\frac{S\_{j}^{m,i,k}\big(T^{i};\;\bm{\vartheta}^{m,i},\;\bm{\nu}^{m,i}\big)}{S\_{j}(0)}\bigg)\Bigg\}\_{k=1}^{M} |  |

Step 4: Define MDN inputs as 𝐱m,i=(ϑm,i,𝝂m,i,Ti,wm,i)\mathbf{x}^{m,i}=(\bm{\vartheta}^{m,i},\bm{\nu}^{m,i},T^{i},w^{m,i})

### 3.4 MDN Training Algorithm

The training of the MDN proceeds via the following steps:

Step 1. Initialization: Set the learning rate η\eta and initialize the network parameters

|  |  |  |
| --- | --- | --- |
|  | Φ={𝒲0,⋯,𝒲H,𝒲π,𝒲μ,𝒲δ,β0,⋯,βH,βπ,βμ,βδ}.\Phi=\{\mathcal{W}\_{0},\cdots,\mathcal{W}\_{H},\mathcal{W}\_{\pi},\mathcal{W}\_{\mu},\mathcal{W}\_{\delta},\beta\_{0},\cdots,\beta\_{H},\beta\_{\pi},\beta\_{\mu},\beta\_{\delta}\}. |  |

Step 2. Forward Pass: For each training pair (𝐱i,𝐲i)(\mathbf{x}^{i},\mathbf{y}^{i}), compute the MDN output

|  |  |  |
| --- | --- | --- |
|  | {πj​(𝐱i),μj​(𝐱i),δj​(𝐱i)}j=1d.\big\{\pi\_{j}(\mathbf{x}^{i}),\mu\_{j}(\mathbf{x}^{i}),\delta\_{j}(\mathbf{x}^{i})\big\}\_{j=1}^{d}. |  |

Step 3. Compute Negative log\log-Likelihood Loss: The network is trained by minimizing the negative log\log-likelihood (NLL) of the conditional density p​(𝐲|𝐱)p(\mathbf{y}|\mathbf{x}), which corresponds to the maximum likelihood estimation of the mixture model parameters.

For each data point (𝐱i,𝐲i)(\mathbf{x}^{i},\mathbf{y}^{i}), the log\log-likelihood is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡p​(𝐲i|𝐱i)=∑k=1Mlog⁡(∑j=1dπj​(𝐱i)×ϕj​(yi,k|μj​(𝐱i),δj​(𝐱i))).\log p(\mathbf{y}^{i}|\mathbf{x}^{i})=\sum\_{k=1}^{M}\log\left(\sum\_{j=1}^{d}\pi\_{j}(\mathbf{x}^{i})\times\phi\_{j}(y^{i,k}|\mu\_{j}(\mathbf{x}^{i}),\delta\_{j}(\mathbf{x}^{i}))\right). |  | (3.9) |

To enhance numerical stability during training, especially in the case of Gaussian mixtures, we adopt the LogSumExp trick and express the log\log-likelihood as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡p​(𝐲i|𝐱i)=∑k=1Mlog⁡(∑j=1dexp⁡(log⁡πj​(𝐱i)+log⁡(ϕj​(yi,k|μj​(𝐱i),δj​(𝐱i))))),\log p(\mathbf{y}^{i}|\mathbf{x}^{i})=\sum\_{k=1}^{M}\log\left(\sum\_{j=1}^{d}\exp{\Big(\log\pi\_{j}(\mathbf{x}^{i})+\log\big(\phi\_{j}(y^{i,k}|\mu\_{j}(\mathbf{x}^{i}),\delta\_{j}(\mathbf{x}^{i}))\big)\Big)}\right), |  | (3.10) |

where the log\log-density of a univariate Gaussian component is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(ϕj​(yi,k|μj​(𝐱i),δj​(𝐱i)))=−log⁡δj​(𝐱i)−log⁡(2​π)2−12​(yi,k−μj​(𝐱i)δj​(𝐱i)).\log\big(\phi\_{j}(y^{i,k}|\mu\_{j}(\mathbf{x}^{i}),\delta\_{j}(\mathbf{x}^{i}))\big)=-\log\;\delta\_{j}(\mathbf{x}^{i})-\frac{\log(2\pi)}{2}-\frac{1}{2}\left(\frac{y^{i,k}-\mu\_{j}(\mathbf{x}^{i})}{\delta\_{j}(\mathbf{x}^{i})}\right). |  | (3.11) |

The total loss over the entire dataset is:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒNLL\displaystyle\mathcal{L}\_{\text{NLL}} | =−1Ns​∑i=1Nslog⁡p​(𝐲i|𝐱i).\displaystyle=-\frac{1}{N\_{s}}\sum\_{i=1}^{N\_{s}}\log p(\mathbf{y}^{i}|\mathbf{x}^{i}). |  | (3.12) |

Step 4. Gradient Computation: Compute the gradients ∂ℒ/∂Φ\partial\mathcal{L}/\partial\Phi via backpropagation using the chain rule. This requires computing the partial derivatives with respect to the mixture parameters πj,μj,δj\pi\_{j},\mu\_{j},\delta\_{j}.

Step 5. Parameter Update: Update the network parameters using an appropriate optimizer (Adam, for example).

Repeat steps 2−52-5 for multiple epochs until the training loss converges.

## 4 Numerical Experiments

In this section, we present numerical experiments of training a mixture density network (MDN) to approximate the conditional distribution of weighted basket returns for option pricing. As mentioned earlier, numerical experiments are divided into two subsections, corresponding to two distinct volatility structures considered under Geometric Brownian motion (GBM) dynamics for the underlying assets. Each subsection includes numerical experiments that evaluate the accuracy of the learned distribution and the resulting option price with the benchmark Monte Carlo.

Under both volatility structures, we consider a basket of NN assets, each following a GBM with time-varying interest and dividend rates. The option is written on the weighted price of the basket. Each asset evolves under its own set of parameters and is correlated with others via a given correlation matrix 𝐑∈ℝN×N\mathbf{R}\in\mathbb{R}^{N\times N}, which defines the joint dynamics of the underlying NN-dimensional Brownian motion. Our objective is to approximate the univariate conditional distribution of the weighted return of the basket at a fixed terminal time. To this end, we employ a mixture density network (MDN) with a parametric Gaussian mixture model. All parameters of the GBM model, including the basket’s correlation matrix and the terminal time, constitute the parameter set of the mixture model.

Before detailing numerical experiments with the two volatility structures considered, we first present the metrics used to assess distributional and pricing accuracy.

Measure of Approximation Accuracy: The accuracy of the approximations produced by the MDN can be assessed in two complementary ways:

* •

  Distributional Accuracy: We evaluate how closely the probability distribution learned by the MDN matches the empirical distribution obtained from Monte Carlo (MC) simulations. The empirical distribution is estimated using kernel density estimation (KDE) on the MC samples. The discrepancy between the MDN-predicted density pMDNp\_{\text{MDN}} and the MC-based density pMCp\_{\text{MC}} is quantified using the Kullback-Leibler (KL) divergence:

  |  |  |  |
  | --- | --- | --- |
  |  | DKL​(pMC∥pMDN)≈∑ipMC​(xi)​log⁡pMC​(xi)pMDN​(xi)⋅Δ​x,D\_{\text{KL}}(p\_{\text{MC}}\,\|\,p\_{\text{MDN}})\approx\sum\_{i}p\_{\text{MC}}(x\_{i})\log\frac{p\_{\text{MC}}(x\_{i})}{p\_{\text{MDN}}(x\_{i})}\cdot\Delta x, |  |

  where {xi}\{x\_{i}\} is a uniform grid over the support of the distribution and Δ​x\Delta x is the grid spacing.
* •

  Pricing Accuracy: Using the MDN-predicted distribution, we can compute option prices and compare them with benchmark prices obtained via Monte Carlo simulation. The accuracy of these prices is evaluated using a Huberized relative error metric:

  |  |  |  |
  | --- | --- | --- |
  |  | relative\_error=|PMDN−PMC|0.125%×PMC+0.00125,\text{relative\\_error}=\frac{\left|P\_{\text{MDN}}-P\_{\text{MC}}\right|}{0.125\%\times P\_{\text{MC}}+0.00125}, |  |

  where PMDNP\_{\text{MDN}} and PMCP\_{\text{MC}} denote the MDN-based and Monte Carlo-based option prices, respectively. The denominator is chosen to ensure stability of the metric for small values of PMCP\_{\text{MC}}.

Now, we turn to the details of our first experiment, where each asset in the basket follows a Geometric Brownian motion with time-varying volatility.

### 4.1 Basket of Assets Following GBM with Time-varying Volatility

We consider a basket of two assets (N=2N=2), where each asset has equal weight (w1=w2=0.5)(w\_{1}=w\_{2}=0.5). For the simulation of the training dataset, we set the initial asset price as S​(0)=(S1​(0),S2​(0))=(1.0,1.0)S(0)=(S\_{1}(0),S\_{2}(0))=(1.0,1.0). The time-varying parameters r​(t)r(t), q​(t)q(t) and σ​(t)\sigma(t) are simulated using the CIR model, with the corresponding parameter values and initial ranges summarized in Table [1](https://arxiv.org/html/2511.09061v1#S4.T1 "Table 1 ‣ 4.1 Basket of Assets Following GBM with Time-varying Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks").

|  | aa | bb | cc | x0x\_{0} |
| --- | --- | --- | --- | --- |
| r​(t)r(t) | 0.6 | 0.05 | 0.05 | [0.005, 0.1] |
| q​(t)q(t) | 0.6 | 0.03 | 0.02 | [0.005,0.1] |
| σ​(t)\sigma(t) | 0.75 | 0.1 | 0.2 | [0.01,0.2] |

Table 1: CIR model parameters

To construct the training dataset, we simulate n1=5000n\_{1}=5000 samples of maturity Ti;i=1,⋯,n1T^{i};i=1,\cdots,n\_{1}. For each ii, we generate further n2=4000n\_{2}=4000 independent samples of GBM model parameters ϑm,i\bm{\vartheta}^{m,i} for m=1,⋯,n2m=1,\cdots,n\_{2}. This yields a total of 20 million input samples 𝐱m,i=(ϑm,i,Ti);i=1,⋯,n1;m=1,⋯,n2\mathbf{x}^{m,i}=(\bm{\vartheta}^{m,i},T^{i});i=1,\cdots,n\_{1};m=1,\cdots,n\_{2}. For each input 𝐱m,i\mathbf{x}^{m,i}, we simulate M=30M=30 independent paths of the asset price process. The corresponding target values are

|  |  |  |
| --- | --- | --- |
|  | 𝐲m,i={log⁡(∑j=1Nwj​Sjm,i,k​(Ti;ϑm,i)Sj​(0))}k=1M.\mathbf{y}^{m,i}=\Bigg\{\log\bigg(\sum\_{j=1}^{N}w\_{j}\frac{S\_{j}^{m,i,k}(T^{i};\;\bm{\vartheta}^{m,i})}{S\_{j}(0)}\bigg)\Bigg\}\_{k=1}^{M}. |  |

Thus, each input data is associated with MM likelihood samples for training the MDN.

#### 4.1.1 Input Features

Since using the full path of time-varying parameters (e.g., r​(t),q​(t)r(t),q(t) or σ​(t)\sigma(t)), as inputs to the MDN is impractical, we instead utilize truncated signatures of these paths. For all experiments, the signatures are truncated at level ls​i​g=5l^{sig}=5.

This results in a total of 2​N+(1+2​N)​ls​i​g+2+N​(N+1)22N+(1+2N)l^{sig}+2+\frac{N(N+1)}{2} custom input features. The input vector for the MDN takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱​(ϑ,T)=\displaystyle\mathbf{x}(\bm{\vartheta},T)= | (r​(⋅)​T,q​(⋅)​T,σ​(⋅)​T,𝐋​T,T)\displaystyle\Big(r(\cdot)T,\;q(\cdot)T,\;\sigma(\cdot)T,\;\mathbf{L}\sqrt{T},\;T\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (rm​e​a​n​T,q1m​e​a​n​T,q2m​e​a​n​T,σ1m​e​a​n​T,σ2m​e​a​n​T,rs​i​g​T,q1s​i​g​T,q2s​i​g​T,σ1s​i​g​T,σ2s​i​g​T,𝐋​T,T),\displaystyle\Big(r^{mean}T,\;q\_{1}^{mean}T,\;q\_{2}^{mean}T,\;\sigma\_{1}^{mean}\sqrt{T},\;\sigma\_{2}^{mean}\sqrt{T},\;r^{sig}T,\;q\_{1}^{sig}T,\;q\_{2}^{sig}T,\;\sigma\_{1}^{sig}T,\;\sigma\_{2}^{sig}T,\;\mathbf{L}\sqrt{T},\;T\Big), |  |

where rm​e​a​nr^{mean} and rs​i​gr^{sig} denote the mean and signature terms derived from the path of r​(t)r(t) over [0,T][0,T], and likewise for q​(t)q(t) and σ​(t)\sigma(t). Since signature values at higher levels diminish rapidly in magnitude, we normalize all signature components for each sample before using them as input features.

#### 4.1.2 MDN Architecture:

The MDN used here is univariate and composed of 6 hidden layers, with the following number of neurons per layer: 320, 256, 256, 192, 128 and 80. The architecture uses the following activation and transformation functions:

|  |  |  |
| --- | --- | --- |
|  | β0=β1=⋯=β5=βμ=βδ=0,\displaystyle\beta\_{0}=\beta\_{1}=\cdots=\beta\_{5}=\beta\_{\mu}=\beta\_{\delta}=0, |  |
|  |  |  |
| --- | --- | --- |
|  | g​(𝐱)=LeakyReLU​(𝐱),\displaystyle g(\mathbf{x})=\textit{LeakyReLU}(\mathbf{x}), |  |
|  |  |  |
| --- | --- | --- |
|  | gπ​(𝐱)=softmax​(𝐱),\displaystyle g\_{\pi}(\mathbf{x})=\textit{softmax}(\mathbf{x}), |  |
|  |  |  |
| --- | --- | --- |
|  | gμ​(𝐱)=tanh⁡(𝐱),\displaystyle g\_{\mu}(\mathbf{x})={\tanh}(\mathbf{x}), |  |
|  |  |  |
| --- | --- | --- |
|  | gδ​(𝐱)=softplus​(𝐱)∗tanh2⁡(𝐱)+ε0,\displaystyle g\_{\delta}(\mathbf{x})=\textit{softplus}(\mathbf{x})\*{\tanh}^{2}(\mathbf{x})+\varepsilon^{0}, |  |

where ε0\varepsilon^{0} is a small positive constant used to ensure numerical stability in the standard deviation output.

#### 4.1.3 Model Training

We employ a mixture density network with d=10d=10 Gaussian components. The model is trained using the AdamW optimizer. In each epoch, the full training dataset of 20 million samples is processed in mini-batches of size 100,000. After each epoch, performance is evaluated on a validation set of 5 million samples. The initial learning rate is set to 0.010.01 and is adaptively reduced when validation loss stagnates over multiple epochs.

#### 4.1.4 Numerical Results

The time series of the risk-free interest rate, dividend yields, and volatilities, along with the correlation matrix, serve as inputs to the MDN.
Assume, Figure [3a](https://arxiv.org/html/2511.09061v1#S4.F3.sf1 "In Figure 3 ‣ 4.1.4 Numerical Results ‣ 4.1 Basket of Assets Following GBM with Time-varying Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") presents the time series of the risk-free interest rate, along with the dividend yields and volatilities for the two assets in the basket, simulated over a one-year horizon (252 trading days). The correlation structure among these assets is specified by the correlation matrix

|  |  |  |
| --- | --- | --- |
|  | 𝐑=(1−0.7131−0.71311).\mathbf{R}=\begin{pmatrix}1&-0.7131\\ -0.7131&1\end{pmatrix}. |  |

Then, Figure [3b](https://arxiv.org/html/2511.09061v1#S4.F3.sf2 "In Figure 3 ‣ 4.1.4 Numerical Results ‣ 4.1 Basket of Assets Following GBM with Time-varying Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") compares the resulting estimated distributions of the average return of the basket obtained using the mixture density network (MDN) and those obtained from Monte Carlo (MC) simulation, across different maturities. The label “D\_KL” beside each maturity denotes the Kullback–Leibler (KL) divergence between the MDN and MC distributions, providing a quantitative measure of how closely the MDN replicates the actual return distribution.

Under the same market conditions, we report the relative percentage errors between option prices computed from the MDN-based distribution and those from the MC-based distribution in Figure [4](https://arxiv.org/html/2511.09061v1#S4.F4 "Figure 4 ‣ 4.1.4 Numerical Results ‣ 4.1 Basket of Assets Following GBM with Time-varying Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks"). These results are shown separately for European call and put options at various strikes and maturities, offering insights into the pricing accuracy achieved by the MDN approximation.

![Refer to caption](GBM_LwR_N2CSignTV_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V3_rates_01.png)


(a)

![Refer to caption](GBM_LwR_N2CSignTV_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V3_MDNMC_01.png)


(b)

Figure 3: (a) Time-varying interest rate, dividend yields, and volatilities. (b) MDN vs. MC distributions of average basket return with KL divergence at different maturities.

![Refer to caption](GBM_LwR_N2CSignTV_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V3_price_error_01.png)


Figure 4: Relative percentage error in European call and put option prices based on MDN vs. MC pricing.

In a second scenario, the correlation matrix is changed to

|  |  |  |
| --- | --- | --- |
|  | 𝐑=(10.2190.2191),\mathbf{R}=\begin{pmatrix}1&0.219\\ 0.219&1\end{pmatrix}, |  |

while the time series of the risk-free rate, dividend yields, and volatilities are given in Figure [5a](https://arxiv.org/html/2511.09061v1#S4.F5.sf1 "In Figure 5 ‣ 4.1.4 Numerical Results ‣ 4.1 Basket of Assets Following GBM with Time-varying Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks"). Figure [5b](https://arxiv.org/html/2511.09061v1#S4.F5.sf2 "In Figure 5 ‣ 4.1.4 Numerical Results ‣ 4.1 Basket of Assets Following GBM with Time-varying Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") compares the corresponding MDN and MC return distributions, with the associated KL divergences. The resulting relative percentage pricing errors for European options are reported in Figure [6](https://arxiv.org/html/2511.09061v1#S4.F6 "Figure 6 ‣ 4.1.4 Numerical Results ‣ 4.1 Basket of Assets Following GBM with Time-varying Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks").

![Refer to caption](GBM_LwR_N2CSignTV_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V3_rates_02.png)


(a)

![Refer to caption](GBM_LwR_N2CSignTV_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V3_MDNMC_02.png)


(b)

Figure 5: (a) Time-varying interest rate, dividend yields, and volatilities. (b) MDN vs. MC distributions of average basket return with KL divergence at different maturities.

![Refer to caption](GBM_LwR_N2CSignTV_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V3_price_error_02.png)


Figure 6: Relative percentage error in European call and put option prices based on MDN vs. MC pricing.

These numerical results demonstrate that the MDN can effectively learn the conditional distribution over the parameter space with high accuracy, enabling accurate option pricing across a range of market conditions. This highlights the practical value of the approach: once trained, the MDN can efficiently approximate option prices across varying scenarios. Moreover, the use of truncated path signatures proves effective in capturing the dependence of the target distribution on time-varying model parameters.

Now, we lay out the details of our second experiment, in which each asset in the basket follows a Geometric Brownian Motion with local volatility.

### 4.2 Basket of Assets Following GBM with Local-Volatility

We consider a basket consisting of two assets (N=2N=2) with the initial prices set to S​(0)=(S1​(0),S2​(0))=(1.0,1.0)S(0)=(S\_{1}(0),S\_{2}(0))=(1.0,1.0) for the simulation of the training dataset. The time-varying parameters r​(t)r(t) and q​(t)q(t) are simulated using the CIR model as described previously, with parameter values and initial ranges summarized in Table [1](https://arxiv.org/html/2511.09061v1#S4.T1 "Table 1 ‣ 4.1 Basket of Assets Following GBM with Time-varying Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks").

To construct the training dataset, we simulate n1=5000n\_{1}=5000 samples of maturity Ti;i=1,⋯,n1T^{i};i=1,\cdots,n\_{1}. For each maturity TiT^{i}, we generate further n2=4000n\_{2}=4000 independent samples of:

* •

  GBM model parameters ϑm,i\bm{\vartheta}^{m,i},
* •

  local-volatility function parameters 𝝂m,i\bm{\nu}^{m,i} and
* •

  basket weights wm,iw^{m,i},

for m=1,⋯,n2m=1,\cdots,n\_{2}. This yields a total of 20 million input samples of the form

|  |  |  |
| --- | --- | --- |
|  | 𝐱m,i=(ϑm,i,𝝂m,i,Ti,wm,i);i=1,⋯,n1;m=1,⋯,n2.\mathbf{x}^{m,i}=(\bm{\vartheta}^{m,i},\bm{\nu}^{m,i},T^{i},w^{m,i});i=1,\cdots,n\_{1};m=1,\cdots,n\_{2}. |  |

For each input 𝐱m,i\mathbf{x}^{m,i}, we simulate M=30M=30 independent paths of the asset price process, generating the associated target outputs:

|  |  |  |
| --- | --- | --- |
|  | 𝐲m,i={ym,i,k=log⁡(∑j=1Nwjm,i​Sjm,i,k​(Ti;ϑm,i,𝝂m,i)Sj​(0))}k=1M.\mathbf{y}^{m,i}=\Bigg\{y^{m,i,k}=\log\bigg(\sum\_{j=1}^{N}w^{m,i}\_{j}\frac{S\_{j}^{m,i,k}\big(T^{i};\;\bm{\vartheta}^{m,i},\;\bm{\nu}^{m,i}\big)}{S\_{j}(0)}\bigg)\Bigg\}\_{k=1}^{M}. |  |

Thus, each input vector 𝐱m,i\mathbf{x}^{m,i} is paired with MM likelihood samples for training the mixture density network.

#### 4.2.1 Local-volatility Function σL​(⋅)\sigma\_{L}(\cdot)

We adopt the following functional form for the local volatility:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σL​(x)=cl​o​c​((x−al​o​c)2+cl​o​c)bl​o​c,\sigma\_{L}(x)=c\_{loc}\Big((x-a\_{loc})^{2}+c\_{loc}\Big)^{b\_{loc}}, |  | (4.1) |

where the parameters al​o​c,bl​o​c,cl​o​ca\_{loc},b\_{loc},c\_{loc} vary within the ranges:

|  |  |  |
| --- | --- | --- |
|  | al​o​c∈[0.5,1.5],\displaystyle a\_{loc}\in[0.5,1.5], |  |
|  |  |  |
| --- | --- | --- |
|  | bl​o​c∈[0.05,0.5],\displaystyle b\_{loc}\in[0.05,0.5], |  |
|  |  |  |
| --- | --- | --- |
|  | cl​o​c∈[0.05,0.4].\displaystyle c\_{loc}\in[0.05,0.4]. |  |

We denote the set of local volatility parameters for all assets as 𝝂=(al​o​c,j,bl​o​c,j,cl​o​c,j)j=1N\bm{\nu}=\big(a\_{loc,j},b\_{loc,j},c\_{loc,j}\big)\_{j=1}^{N}. It is important to note that this choice of functional form is not driven by modelling assumptions or calibration to market data. Instead, we aim to assess whether a mixture density network (MDN) can learn the distributional features of the average basket return from local volatility parameters.

#### 4.2.2 Input Features

The input to the mixture density network (MDN) consists of custom-engineered features derived from the model parameters, including truncated path signatures of the time-varying rates. Specifically, we truncate signatures at level ls​i​g=5.l\_{sig}=5. This will result in a total of 5​N+(1+N)​ls​i​g+2+N​(N+1)25N+(1+N)l^{sig}+2+\frac{N(N+1)}{2} input features. The final input vector for the MDN takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱​(ϑ,𝝂,T,w)=\displaystyle\mathbf{x}(\bm{\vartheta},\bm{\nu},T,w)= | (w​T,r​(⋅)​T,q​(⋅)​T,al​o​c​T,bl​o​c​T,cl​o​c​T,𝐋​T,T)\displaystyle\Big(wT,r(\cdot)T,\;q(\cdot)T,\;a\_{loc}T,\;b\_{loc}T,\;c\_{loc}T,\;\mathbf{L}\sqrt{T},\;T\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (w1T,w2T,rm​e​a​nT,q1m​e​a​nT,q2m​e​a​nT,rs​i​gT,q1s​i​gT,q2s​i​gT,al​o​c,1T,al​o​c,2T,bl​o​c,1T,bl​o​c,2T,\displaystyle\Big(w\_{1}T,w\_{2}T,r^{mean}T,\;q\_{1}^{mean}T,\;q\_{2}^{mean}T,\;r^{sig}T,\;q\_{1}^{sig}T,\;q\_{2}^{sig}T,\;a\_{loc,1}T,\;a\_{loc,2}^{T},\;b\_{loc,1}T,\;b\_{loc,2}T, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | cl​o​c,1T,cl​o​c,2T,𝐋T,T),\displaystyle\;c\_{loc,1}T,\;c\_{loc,2}T,\;\mathbf{L}\sqrt{T},\;T\Big), |  |

where rm​e​a​nr^{mean} and rs​i​gr^{sig} denote the mean and signature terms derived from the path of r​(t)r(t) over t∈[0,T]t\in[0,T], and likewise for q​(t)q(t).

#### 4.2.3 MDN Architecture

The univariate MDN employed in this setting consists of 6 hidden layers, with the following number of neurons per layer: 320, 256, 256, 192, 128 and 80, respectively. The activation and transformation functions used in the architecture are specified as follows:

|  |  |  |
| --- | --- | --- |
|  | β0=β1=⋯=β5=βμ=βδ=0,\displaystyle\beta\_{0}=\beta\_{1}=\cdots=\beta\_{5}=\beta\_{\mu}=\beta\_{\delta}=0, |  |
|  |  |  |
| --- | --- | --- |
|  | g​(𝐱)=LeakyReLU​(𝐱),\displaystyle g(\mathbf{x})=\textit{LeakyReLU}(\mathbf{x}), |  |
|  |  |  |
| --- | --- | --- |
|  | gπ​(𝐱)=softmax​(𝐱),\displaystyle g\_{\pi}(\mathbf{x})=\textit{softmax}(\mathbf{x}), |  |
|  |  |  |
| --- | --- | --- |
|  | gμ​(𝐱)=𝐱,\displaystyle g\_{\mu}(\mathbf{x})=\mathbf{x}, |  |
|  |  |  |
| --- | --- | --- |
|  | gδ​(𝐱)=softplus​(𝐱)∗tanh2⁡(𝐱)+ε0,\displaystyle g\_{\delta}(\mathbf{x})=\textit{softplus}(\mathbf{x})\*{\tanh}^{2}(\mathbf{x})+\varepsilon^{0}, |  |

where ε0\varepsilon^{0} is a small positive constant used to ensure numerical stability in the standard deviation output.

This configuration is almost the same as in our previous case, the only exception is that the activation function gμg\_{\mu} doesn’t use the tanh\tanh function, instead we use the identity function. This reflects the flexibility in architectural design—if carefully designed, other architectural choices may also work well.

#### 4.2.4 Model Training

The training procedure of the MDN follows the same method as in the previous case. Specifically, we employ a mixture density network with d=10d=10 Gaussian components and train the model using the AdamW optimizer. In each epoch, the whole training dataset of 20 million samples is processed in mini-batches of size 100,000. After each epoch, performance is evaluated on a validation set of 5 million samples.

The initial learning rate is set to 0.010.01 and is adaptively reduced when validation loss stagnates over multiple epochs. While the overall training strategy mirrors the previous case, it is worth emphasizing that tuning the learning rate upon stagnation in the validation loss involves some empirical adjustment. In practice, identifying when and how much to adjust the learning rate remains partly heuristic and can significantly impact training efficiency and convergence.

#### 4.2.5 Numerical Results

The inputs to the MDN consist of the correlation matrix of the asset basket, the local-volatility function parameters for each asset, time series of the risk-free interest rate and dividend yields, and the basket weights. We assume the correlation matrix

|  |  |  |
| --- | --- | --- |
|  | 𝐑=(10.48680.48681),\mathbf{R}=\begin{pmatrix}1&0.4868\\ 0.4868&1\end{pmatrix}, |  |

and the local-volatility function parameters for the two assets as follows

|  |  |  |
| --- | --- | --- |
|  | al​o​c=[1.155,0.95],bl​o​c=[0.263,0.387],cl​o​c=[0.077,0.145].a\_{loc}=[1.155,0.95],\;b\_{loc}=[0.263,0.387],\;c\_{loc}=[0.077,0.145]. |  |

![Refer to caption](GBM_LwR_N2CSignLVw_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V2_rates_01.png)


(a)

![Refer to caption](GBM_LwR_N2CSignLVw_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V2_MDNMC_01.jpg)


(b) w1=0.25,w2=0.75w\_{1}=0.25,w\_{2}=0.75

![Refer to caption](GBM_LwR_N2CSignLVw_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V2_MDNMC_02.jpg)


(c) w1=0.5,w2=0.5w\_{1}=0.5,w\_{2}=0.5

![Refer to caption](GBM_LwR_N2CSignLVw_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V2_MDNMC_03.jpg)


(d) w1=0.75,w2=0.25w\_{1}=0.75,w\_{2}=0.25

Figure 7: (a) Time-varying interest rates and dividend yields. (b),(c)&(d) MDN vs. MC distributions of weighted basket returns with KL divergence at different maturities for different weight configurations.

![Refer to caption](GBM_LwR_N2CSignLVw_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V2_errors_02.png)


Figure 8: Relative percentage error in European call and put option prices based on MDN vs. MC pricing.

Figure [7a](https://arxiv.org/html/2511.09061v1#S4.F7.sf1 "In Figure 7 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") shows the time series of the risk-free interest rate and the dividend yields for the two assets in the basket. Using this market condition, we analyze three different combinations of the basket weights. The resulting distributions of the basket’s weighted returns, estimated by the mixture density network (MDN), are compared with those obtained via Monte Carlo (MC) simulation in Figures [7b](https://arxiv.org/html/2511.09061v1#S4.F7.sf2 "In Figure 7 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks"), [7c](https://arxiv.org/html/2511.09061v1#S4.F7.sf3 "In Figure 7 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") and [7d](https://arxiv.org/html/2511.09061v1#S4.F7.sf4 "In Figure 7 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks"), each corresponding to different weight vectors. These comparisons are carried out across multiple maturities. For each case, the Kullback–Leibler (KL) divergence between the MDN and MC distributions is reported alongside the corresponding maturity, denoted by ”D\_KL”.

Under the same market conditions, and using the basket weight from Figure [7c](https://arxiv.org/html/2511.09061v1#S4.F7.sf3 "In Figure 7 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks"), we present the relative percentage errors between the European option prices computed from the MDN-based distribution and MC-based distribution in Figure [8](https://arxiv.org/html/2511.09061v1#S4.F8 "Figure 8 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks").

![Refer to caption](GBM_LwR_N2CSignLVw_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V2_rates_11.png)


(a)

![Refer to caption](GBM_LwR_N2CSignLVw_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V2_MDNMC_11.jpg)


(b) w1=0.25,w2=0.75w\_{1}=0.25,w\_{2}=0.75

![Refer to caption](GBM_LwR_N2CSignLVw_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V2_MDNMC_12.jpg)


(c) w1=0.5,w2=0.5w\_{1}=0.5,w\_{2}=0.5

![Refer to caption](GBM_LwR_N2CSignLVw_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V2_MDNMC_13.jpg)


(d) w1=0.75,w2=0.25w\_{1}=0.75,w\_{2}=0.25

Figure 9: (a) Time-varying interest rates and dividend yields. (b),(c)&(d) MDN vs. MC distributions of weighted basket returns with KL divergence at different maturities for different weight configurations.

![Refer to caption](GBM_LwR_N2CSignLVw_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V2_errors_11.png)


Figure 10: Relative percentage error in European call and put option prices based on MDN vs. MC pricing.

![Refer to caption](GBM_LwR_N2CSignLVw_batched_data30_l6_n_320_256_256_192_128_80_g10_20M_b100K_LReLu_V2_errors_12.png)


Figure 11: Relative percentage error in European call and put option prices based on MDN vs. MC pricing.

In a second scenario, we modify the correlation matrix to

|  |  |  |
| --- | --- | --- |
|  | 𝐑=(1−0.4849−0.48491),\mathbf{R}=\begin{pmatrix}1&-0.4849\\ -0.4849&1\end{pmatrix}, |  |

and update the local-volatility function parameters for the two assets to

|  |  |  |
| --- | --- | --- |
|  | al​o​c=[0.6775,0.7475],bl​o​c=[0.3023,0.1543],cl​o​c=[0.3951,0.1214].a\_{loc}=[0.6775,0.7475],\;b\_{loc}=[0.3023,0.1543],\;c\_{loc}=[0.3951,0.1214]. |  |

The risk-free interest rate and dividend yields for two assets are now given in Figure [9a](https://arxiv.org/html/2511.09061v1#S4.F9.sf1 "In Figure 9 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks"). For three different sets of basket weights, Figures [9b](https://arxiv.org/html/2511.09061v1#S4.F9.sf2 "In Figure 9 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks"), [9c](https://arxiv.org/html/2511.09061v1#S4.F9.sf3 "In Figure 9 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks"), and [9d](https://arxiv.org/html/2511.09061v1#S4.F9.sf4 "In Figure 9 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") present a comparison between the MDN-estimated and Monte Carlo-simulated distributions of the weighted basket return across various maturities. The associated Kullback–Leibler (KL) divergence between the two distributions is also reported for each case.

The resulting relative percentage errors in European option prices, corresponding to the basket weights used in Figure [9b](https://arxiv.org/html/2511.09061v1#S4.F9.sf2 "In Figure 9 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") and [9c](https://arxiv.org/html/2511.09061v1#S4.F9.sf3 "In Figure 9 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks"), are reported in Figure [10](https://arxiv.org/html/2511.09061v1#S4.F10 "Figure 10 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") and  [11](https://arxiv.org/html/2511.09061v1#S4.F11 "Figure 11 ‣ 4.2.5 Numerical Results ‣ 4.2 Basket of Assets Following GBM with Local-Volatility ‣ 4 Numerical Experiments ‣ Generative Pricing of Basket Options via Signature-Conditioned Mixture Density Networks") respectively.

These numerical results demonstrate that the MDN can successfully learn the conditional distribution based on the parameters of the local volatility function. Notably, the MDN is also parametrized by the basket weights, providing additional flexibility: if the basket composition changes, the trained model remains applicable for pricing options on the new weighted return, eliminating the need to retrain a separate model.

Reproducibility and Runtime: 
All experiments were conducted on an Apple M1 Pro processor with 16 GB of RAM. Training on 20 million samples (batch size = 100,000) required approximately 6.5 minutes per epoch. The average inference latency per market configuration was about 3.4 milliseconds, demonstrating the model’s suitability for real-time or large-scale pricing applications.

## 5 Conclusion

In this work, we proposed a deep learning-based framework for pricing European basket options under geometric Brownian motion (GBM) dynamics with time-varying market parameters. Our approach leverages a mixture density network (MDN) to approximate the conditional distribution of the weighted return of a basket of assets, taking as input the time series of risk-free interest rates, dividend yields, volatilities, and correlation structures.

We evaluated the method under two GBM settings—one with time-varying volatility and another with local volatility. In both cases, the MDN accurately recovered the conditional distribution across a broad range of input scenarios. Option prices computed using the learned distributions closely matched benchmark Monte Carlo (MC) estimates, with relative pricing errors typically within a few percentage points. These results demonstrate the MDN’s effectiveness as a surrogate distribution model for pricing.

A key component of our architecture is the use of truncated path signatures to represent the temporal evolution of model parameters. This feature representation enabled the MDN to generalize across diverse time-varying environments. Additionally, by incorporating basket weights as part of the input, the model can adapt to different portfolio compositions without retraining, offering practical flexibility.

Overall, the results suggest that MDNs, when paired with appropriate feature engineering and training design, provide an efficient and accurate alternative to traditional simulation-based pricing methods. Once trained, the MDN enables rapid inference, making it particularly suitable for real-time or high-frequency pricing applications.

Future research could extend this approach to modelling multivariate output distributions, more complex derivative products, or alternative market dynamics, including stochastic volatility, rough volatility, and jump processes. Additionally, the framework could be adapted with minimal changes to learn univariate distributions of other functionals of the asset paths, such as the maximum or minimum of a basket.