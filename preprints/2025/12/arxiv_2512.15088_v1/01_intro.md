---
authors:
- Xianglin Wu
- Chiheb Ben Hammouda
- Cornelis W. Oosterlee
doc_id: arxiv:2512.15088v1
family_id: arxiv:2512.15088
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'SigMA: Path Signatures and Multi-head Attention for Learning Parameters in
  fBm-driven SDEs'
url_abs: http://arxiv.org/abs/2512.15088v1
url_html: https://arxiv.org/html/2512.15088v1
venue: arXiv q-fin
version: 1
year: 2025
---


Xianglin Wu
Corresponding Author. Email: 1210202Z1003@smail.swufe.edu.cn
School of Mathematics, Southwestern University of Finance and Economics, Chengdu, 611130, China

Chiheb Ben Hammouda
Mathematical Institute, Utrecht University, 3584 CD Utrecht, the Netherlands

Cornelis W. Oosterlee
Mathematical Institute, Utrecht University, 3584 CD Utrecht, the Netherlands

###### Abstract

Stochastic differential equations (SDEs) driven by fractional Brownian motion (fBm) are increasingly used to model systems with rough dynamics and long-range dependence, such as those arising in quantitative finance and reliability engineering. However, these processes are non-Markovian and lack a semimartingale structure, rendering many classical parameter estimation techniques inapplicable or computationally intractable beyond very specific cases. This work investigates two central questions: (i) whether integrating path signatures into deep learning architectures can improve the trade-off between estimation accuracy and model complexity, and (ii) what constitutes an effective architecture for leveraging signatures as feature maps.

We introduce SigMA (Signature Multi-head Attention), a neural architecture that integrates path signatures with multi-head self-attention, supported by a convolutional preprocessing layer and a multilayer perceptron for effective feature encoding. SigMA learns model parameters from synthetically generated paths of fBm-driven SDEs, including fractional Brownian motion, fractional Ornstein–Uhlenbeck, and rough Heston models, with a particular focus on estimating the Hurst parameter and on joint multi-parameter inference, and it generalizes robustly to unseen trajectories. Extensive experiments on synthetic data and two real-world datasets (i.e., equity-index realized volatility and Li-ion battery degradation) show that SigMA consistently outperforms CNN, LSTM, vanilla Transformer, and Deep Signature baselines in accuracy, robustness, and model compactness. These results demonstrate that combining signature transforms with attention-based architectures provides an effective and scalable framework for parameter inference in stochastic systems with rough or persistent temporal structure.

Keywords: fractional Brownian motion; Stochastic differential equations; non-Markovian processes; parameter estimation; Hurst parameter; path signatures; self-attention; deep learning.

## 1 Introduction

Stochastic differential equations (SDEs) driven by fractional Brownian motion (fBm) arise in domains characterized by long-range dependence as well as pathwise roughness. Such applications include rough volatility modeling in quantitative finance [gatheral2018volatility] and degradation dynamics in engineering systems such as Li-ion batteries [shao2021degradation, boros2024deep]. A central quantity in models driven by fBm is the Hurst parameter H∈(0,1)H\in(0,1), which governs temporal memory, self-similarity, and the local regularity of sample paths. Accurate estimation of this parameter from observed time series is critical, but challenging due to the non-Markovian nature of fBm-driven models. Moreover, in many applications, multiple parameters must be estimated jointly, such as the Hurst exponent, volatility of volatility, correlation, and/or mean-reversion parameters in rough volatility models. This is especially relevant in settings where pricing and risk sensitivities depend on combinations of these parameters [bayer2016pricing, el2019characteristic].

For H≠12H\neq\tfrac{1}{2}, fBm-driven processes are inherently non-Markovian and do not admit a semimartingale structure. As a result, many classical parameter estimation techniques become inapplicable or computationally intractable beyond very specific settings. These challenges motivate the development of data-driven architectures that can extract path-level features robustly across a wide range of parameter regimes. Recent machine learning techniques, including deep feedforward neural networks (FNNs) [mukherjee2023hurst], convolutional neural networks (CNNs) [stone2020calibrating], and long short-term memory (LSTM) [boros2024deep], have been proposed to address these limitations. However, these approaches often lack robustness across different path regimes or do not exploit the intrinsic geometric structure of long-memory paths.

Path signatures, arising from rough path theory [lyons2014rough], offer a principled way to represent continuous-time trajectories in a coordinate-free manner. Signature features have been shown to form an expressive and universal representation for path-dependent functionals, and have been used successfully in classification, forecasting, and medical time series [Lyons\_2019\_DeepSignature, morrill2021neural]. Recent efforts have also combined signatures with transformer architectures for time series modeling [moreno2024rough]. However, existing approaches typically focus on prediction or classification, rather than on parameter inference in fractional stochastic models.

In this work, we investigate two main questions in the context of fBm-driven processes:

* •

  whether integrating path signatures into deep learning architectures improves the trade-off between estimation accuracy and model complexity, and
* •

  what constitutes an effective architecture for leveraging signatures as feature maps.

To this end, we propose SigMA (Signature Multi-head Attention), a neural architecture that integrates path signature features with multi-head self-attention, enhanced by convolutional preprocessing and multilayer perceptron (MLP) layers. Unlike prior methods such as Deep Signature Networks [Lyons\_2019\_DeepSignature], LSTM-based estimators [boros2024deep], or vanilla Transformers [vaswani\_2017], SigMA is specifically designed for parameter estimation in fBm-driven SDEs, across both rough and long-memory regimes.

We evaluate SigMA on both synthetic and empirical datasets. Synthetic experiments consider parameter estimation from simulated paths of fBm, fractional Ornstein–Uhlenbeck (fOU) and rough Heston (rHeston) processes. Empirical case studies include:

* •

  Estimating the Hurst parameter from historic realized volatility in financial markets;
* •

  Quantifying long-range dependence in Li-ion battery degradation data [boros2024deep].

Through extensive numerical and statistical evaluation, we demonstrate that SigMA outperforms existing benchmarks—CNNs [stone2020calibrating], LSTMs [boros2024deep], deep signature models [Lyons\_2019\_DeepSignature], and vanilla Transformers [vaswani\_2017]—in terms of accuracy, robustness, and model compactness. Our findings support that path signatures, when integrated with attention-based architectures, offer a robust and scalable solution to parameter estimation in stochastic systems with rough or persistent temporal behavior.

The remainder of this paper is organized as follows. In Section [2](https://arxiv.org/html/2512.15088v1#S2 "2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), we formulate the problem of interest and give a brief introduction to the considered stochastic processes, path signature tools and self-attention mechanism that will be used in this paper. The specific architecture of the SigMA is clarified in Section [3](https://arxiv.org/html/2512.15088v1#S3 "3 Methodology ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").
In Section [4](https://arxiv.org/html/2512.15088v1#S4 "4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), we begin with numerical examples to explore the optimal architecture of the SigMA model, then we conduct rich examples to verify its performance, comparing it with several well-known benchmark models. Finally, we conclude with Section [5](https://arxiv.org/html/2512.15088v1#S5 "5 Conclusion ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").

## 2 Problem setting and framework

In this section, we establish a framework for parameter estimation from observed sample paths of fBm-driven stochastic processes. We begin by formalizing the estimation task (learning problem) in Section [2.1](https://arxiv.org/html/2512.15088v1#S2.SS1 "2.1 Problem formulation ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"). Subsequently, we introduce the relevant stochastic processes in Section [2.2](https://arxiv.org/html/2512.15088v1#S2.SS2 "2.2 Stochastic processes ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") and review the core components of the approach: the self-attention mechanism and the path signature transform in Sections [2.3](https://arxiv.org/html/2512.15088v1#S2.SS3 "2.3 Self-attention mechanism ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") and [2.4](https://arxiv.org/html/2512.15088v1#S2.SS4 "2.4 Path signatures ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").

### 2.1 Problem formulation

Let 𝐗(n):=(X0,X1,…,Xn−1)∈ℝn×d\mathbf{X}^{(n)}:=(X\_{0},X\_{1},\dots,X\_{n-1})\in\mathbb{R}^{n\times d} denote a discrete observation of a dd–dimensional stochastic process, where n∈ℕn\in\mathbb{N} is the sequence length and d∈ℕd\in\mathbb{N} is the dimensionality of each observation. The law of the underlying continuous–time process depends on an unknown parameter vector 𝜽𝒱∈ℝd𝒱\boldsymbol{\theta}\_{\mathcal{V}}\in\mathbb{R}^{d\_{\mathcal{V}}} that we wish to estimate.

To this end, we introduce a parametric predictor model

|  |  |  |
| --- | --- | --- |
|  | ℳ​(⋅;𝜽ℳ):ℝn×d→ℝd𝒱,\mathcal{M}(\cdot\,;\boldsymbol{\theta}\_{\mathcal{M}})\colon\mathbb{R}^{n\times d}\to\mathbb{R}^{d\_{\mathcal{V}}}, |  |

with learnable model parameters 𝜽ℳ\boldsymbol{\theta}\_{\mathcal{M}}. The model ℳ\mathcal{M} takes the observed path 𝐗(n)\mathbf{X}^{(n)} as input and outputs an estimate of 𝜽𝒱\boldsymbol{\theta}\_{\mathcal{V}}.

We adopt a supervised learning framework in which the model ℳ\mathcal{M} is trained on a synthetic dataset {(𝐗(n))(i),𝜽𝒱(i))}i=1Ntrain\{(\mathbf{X}^{(n)})^{(i)},\boldsymbol{\theta}\_{\mathcal{V}}^{(i)})\}\_{i=1}^{N\_{\text{train}}}, where each path (𝐗(n))(i)(\mathbf{X}^{(n)})^{(i)} is generated from a known stochastic model with known parameter 𝜽𝒱(i)\boldsymbol{\theta}\_{\mathcal{V}}^{(i)}. The model parameters 𝜽ℳ\boldsymbol{\theta}\_{\mathcal{M}} are learned by minimizing a loss function ℒ:ℝd𝒱×ℝd𝒱→ℝ+\mathcal{L}:\mathbb{R}^{d\_{\mathcal{V}}}\times\mathbb{R}^{d\_{\mathcal{V}}}\to\mathbb{R}\_{+}:

|  |  |  |
| --- | --- | --- |
|  | 𝜽^ℳ=arg⁡min𝜽ℳ⁡1M​∑i=1Ntrainℒ​(ℳ​((𝐗(n))(i);𝜽ℳ),𝜽𝒱(i)).\widehat{\boldsymbol{\theta}}\_{\mathcal{M}}=\arg\min\_{\boldsymbol{\theta}\_{\mathcal{M}}}\;\frac{1}{M}\sum\_{i=1}^{N\_{\text{train}}}\mathcal{L}\big(\mathcal{M}((\mathbf{X}^{(n)})^{(i)};\boldsymbol{\theta}\_{\mathcal{M}}),\,\boldsymbol{\theta}\_{\mathcal{V}}^{(i)}\big). |  |

Once trained, the learned map ℳ^:=ℳ​(⋅;𝜽^ℳ)\widehat{\mathcal{M}}:=\mathcal{M}(\cdot;\widehat{\boldsymbol{\theta}}\_{\mathcal{M}}) is subsequently deployed on unseen paths (observations), including real‐world data.

### 2.2 Stochastic processes

In this section, we provide a brief formulation of the stochastic processes we study, namely the fractional Brownian motion (fBm), and two fBm-driven models: the fractional Ornstein–Uhlenbeck (fOU), and the rough Heston (rHeston) processes.

We work on a fixed filtered probability space (Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}) that supports all stochastic processes under consideration. In abstract form, we consider a class of stochastic differential equations (SDEs) of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​X​(t)=μ​(X​(t),𝜽𝒱)​d​t+σ​(X​(t),𝜽𝒱)​d​BH​(t),X​(0)=x0∈ℝd,\mathrm{d}X(t)=\mu\big(X(t),\boldsymbol{\theta}\_{\mathcal{V}}\big)\,\mathrm{d}t+\sigma\big(X(t),\boldsymbol{\theta}\_{\mathcal{V}}\big)\,\mathrm{d}B^{H}(t),\quad X(0)=x\_{0}\in\mathbb{R}^{d}, |  | (1) |

where X​(t)∈ℝdX(t)\in\mathbb{R}^{d} is the state variable, 𝜽𝒱∈ℝd𝒱\boldsymbol{\theta}\_{\mathcal{V}}\in\mathbb{R}^{d\_{\mathcal{V}}} is the unknown parameter vector to be estimated, and {BtH}t≥0\{B^{H}\_{t}\}\_{t\geq 0} is a dd-dimensional fBm with Hurst parameter H∈(0,1)H\in(0,1). When H=12H=\frac{1}{2}, BHB^{H} reduces to the standard Brownian motion and ([1](https://arxiv.org/html/2512.15088v1#S2.E1 "In 2.2 Stochastic processes ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")) becomes an Itô SDE. In general, however, BHB^{H} is not a semimartingale unless H=12H=\frac{1}{2}.

We focus on three representative classes of fBm-driven processes:

#### 2.2.1 Fractional Brownian motion

The simplest case is X​(t)=BH​(t)X(t)=B^{H}(t), with 𝜽𝒱=H\boldsymbol{\theta}\_{\mathcal{V}}=H. This process is centered Gaussian, HH-self-similar, and has stationary increments, with a covariance function

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[BsH​BtH]=12​(s2​H+t2​H−|t−s|2​H),s,t≥0.\mathbb{E}[B^{H}\_{s}B^{H}\_{t}]=\tfrac{1}{2}\big(s^{2H}+t^{2H}-|t-s|^{2H}\big),\quad s,t\geq 0. |  |

For H>12H>\tfrac{1}{2}, the increments exhibit long-range dependence; for H<12H<\tfrac{1}{2}, they exhibit rough anti-persistence. Almost surely, the sample paths are Hölder continuous of any order γ<H\gamma<H [biagini2008stochastic, nualart2006malliavin].

There are different integral representations of fBm, in particular the characterisation provided by [mandelbrot\_1968\_fbm] as

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | BtH\displaystyle B\_{t}^{H} | =\displaystyle= | 1Γ​(12+H)​∫−∞0((t−s)H−12−(−s)H−12)​𝑑Bs\displaystyle\frac{1}{\Gamma\left(\frac{1}{2}+H\right)}\int\_{-\infty}^{0}((t-s)^{H-\frac{1}{2}}-(-s)^{H-\frac{1}{2}})dB\_{s} |  | (2) |
|  |  | +\displaystyle+ | 1Γ​(12+H)​∫0t(t−s)H−12​𝑑Bs,t∈[0,T]\displaystyle\frac{1}{\Gamma\left(\frac{1}{2}+H\right)}\int\_{0}^{t}(t-s)^{H-\frac{1}{2}}dB\_{s},\quad t\in[0,T] |  |

where {Bt}t≥0\{B\_{t}\}\_{t\geq 0} is a standard Brownian motion and Γ​(⋅)\Gamma(\cdot) is the standard Gamma function.

#### 2.2.2 Fractional Ornstein–Uhlenbeck process

The fOU process [kleptsyna2002statistical, cheridito2003fractional] is the fractional analogue of the OU process, where the process, {Xtf​O​U}t≥0\{X^{fOU}\_{t}\}\_{t\geq 0}, solves

|  |  |  |
| --- | --- | --- |
|  | d​Xtf​O​U=−α​(Xtf​O​U−μ)​d​t+σ​d​BtH,X0f​O​U=x0,dX^{fOU}\_{t}=-\alpha(X^{fOU}\_{t}-\mu)\,dt+\sigma\,dB^{H}\_{t},\quad X^{fOU}\_{0}=x\_{0}, |  |

where α>0\alpha>0, σ>0\sigma>0, μ∈ℝ\mu\in\mathbb{R}, and {BtH}t≥0\{B^{H}\_{t}\}\_{t\geq 0} is an fBm with Hurst index H∈(0,1)H\in(0,1).
The integral solution is given by

|  |  |  |
| --- | --- | --- |
|  | Xtf​O​U=μ+e−α​t​(x0−μ)+σ​∫0te−α​(t−s)​𝑑BsH.X^{fOU}\_{t}=\mu+e^{-\alpha t}(x\_{0}-\mu)+\sigma\int\_{0}^{t}e^{-\alpha(t-s)}\,dB^{H}\_{s}. |  |

In this case, the parameter vector to estimate in Section [2.1](https://arxiv.org/html/2512.15088v1#S2.SS1 "2.1 Problem formulation ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") is 𝜽𝒱=(H,α,μ,σ)\boldsymbol{\theta}\_{\mathcal{V}}=(H,\alpha,\mu,\sigma).

#### 2.2.3 Rough Heston process

The rHeston model [el2019characteristic], a non-Markovian extension of the classical Heston model, is another popular rough stochastic volatility model. It is a mean-reverting process that effectively captures both the volatility skew and volatility smiles observed in financial markets. In this model, the variance process, {XtrH}t≥0\{X\_{t}^{\mathrm{rH}}\}\_{t\geq 0}, satisifies

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Xtr​H\displaystyle X\_{t}^{rH} | =\displaystyle= | X0r​H+1Γ​(12+H)​∫0t(t−s)H−12​κ1​(θ−Xsr​H)​𝑑s\displaystyle X\_{0}^{rH}+\frac{1}{\Gamma\left(\frac{1}{2}+H\right)}\int\_{0}^{t}(t-s)^{H-\frac{1}{2}}\kappa\_{1}(\theta-X\_{s}^{rH})\,ds |  | (3) |
|  |  | +\displaystyle+ | 1Γ​(12+H)​∫0t(t−s)H−12​κ2​Xsr​H​𝑑Bs,t∈[0,T],\displaystyle\frac{1}{\Gamma\left(\frac{1}{2}+H\right)}\int\_{0}^{t}\left(t-s\right)^{H-\frac{1}{2}}\kappa\_{2}\sqrt{X\_{s}^{rH}}\,dB\_{s},\quad t\in[0,T], |  |

where H∈(0,12)H\in(0,\,\frac{1}{2}), X0r​H∈ℝ+X\_{0}^{rH}\in\mathbb{R}^{+} is the initial value and κ1,κ2,θ>0\kappa\_{1},\,\kappa\_{2},\,\theta>0.

Equivalently, defining the fractional kernel KH​(t):=tH−12/Γ​(H+12)K\_{H}(t):=t^{H-\frac{1}{2}}/\Gamma(H+\frac{1}{2}), we may rewrite ([3](https://arxiv.org/html/2512.15088v1#S2.E3 "In 2.2.3 Rough Heston process ‣ 2.2 Stochastic processes ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")) as

|  |  |  |
| --- | --- | --- |
|  | XtrH=X0r​H+κ1​∫0tKH​(t−s)​(θ−XsrH)​𝑑s+κ2​∫0tKH​(t−s)​XsrH​𝑑Bs.X\_{t}^{\mathrm{rH}}=X\_{0}^{rH}+\kappa\_{1}\int\_{0}^{t}K\_{H}(t-s)(\theta-X\_{s}^{\mathrm{rH}})\,ds+\kappa\_{2}\int\_{0}^{t}K\_{H}(t-s)\sqrt{X\_{s}^{\mathrm{rH}}}\,dB\_{s}. |  |

In this case, the parameter vector to estimate in Section [2.1](https://arxiv.org/html/2512.15088v1#S2.SS1 "2.1 Problem formulation ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") is 𝜽𝒱=(H,κ1,κ2,θ)\boldsymbol{\theta}\_{\mathcal{V}}=(H,\kappa\_{1},\kappa\_{2},\theta).

### 2.3 Self-attention mechanism

Self-attention is a core component of Transformer architectures [vaswani\_2017] and provides a mechanism for modeling dependencies between elements in a sequence, regardless of their relative positions. Formally, given an input sequence 𝐗(n)=(X0,…,Xn−1)∈ℝn×d\mathbf{X}^{(n)}=(X\_{0},\ldots,X\_{n-1})\in\mathbb{R}^{n\times d}, the attention mechanism computes a new representation for each element based on a weighted aggregation of the entire sequence.

We define the self-attention map as a function

|  |  |  |
| --- | --- | --- |
|  | 𝒜:ℝn×d→ℝn×datt,\mathcal{A}:\mathbb{R}^{n\times d}\to\mathbb{R}^{n\times d\_{\text{att}}}, |  |

parametrized by three learnable projection matrices WQ,WK,WV∈ℝd×dattW\_{Q},W\_{K},W\_{V}\in\mathbb{R}^{d\times d\_{\text{att}}} (typically d>datt∈ℕ+d>d\_{\text{att}}\in\mathbb{N}^{+}), and the self-attention map is then defined as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒜​(𝐗(n);WQ,WK,WV)\displaystyle\mathcal{A}(\mathbf{X}^{(n)};\;\,W\_{Q},\,W\_{K},\,W\_{V}) | :=softmax​(Q​KTdatt)​V∈ℝn×datt\displaystyle:=\text{softmax}\left(\frac{QK^{T}}{\sqrt{d\_{\text{att}}}}\right)V\in\mathbb{R}^{n\times d\_{\text{att}}} |  | (4) |

where Q:=𝐗(n)​WQ,K:=𝐗(n)​WK,V:=𝐗(n)​WVQ:=\mathbf{X}^{(n)}W\_{Q},\;K:=\mathbf{X}^{(n)}W\_{K},\;V:=\mathbf{X}^{(n)}W\_{V} are the query, key, and value matrices, and the softmax in ([4](https://arxiv.org/html/2512.15088v1#S2.E4 "In 2.3 Self-attention mechanism ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")) is applied row-wise. Each output row is a weighted sum of all value vectors, where weights are determined by the similarity between the query and key vectors.111Each input vector xi∈ℝdx\_{i}\in\mathbb{R}^{d} is projected into three latent vectors: qi:=WQ​xi,ki:=WK​xi,vi:=WV​xiq\_{i}:=W\_{Q}x\_{i},\;k\_{i}:=W\_{K}x\_{i},\;v\_{i}:=W\_{V}x\_{i}. The attention output corresponding to xix\_{i} is given by

Attn​(xi)=∑j=1nαi​j​vj,withαi​j=exp⁡(⟨qi,kj⟩/datt)∑j′=1nexp⁡(⟨qi,kj′⟩/datt),\mathrm{Attn}(x\_{i})=\sum\_{j=1}^{n}\alpha\_{ij}v\_{j},\quad\text{with}\quad\alpha\_{ij}=\frac{\exp\left(\langle q\_{i},k\_{j}\rangle/\sqrt{d\_{\text{att}}}\right)}{\sum\_{j^{\prime}=1}^{n}\exp\left(\langle q\_{i},k\_{j^{\prime}}\rangle/\sqrt{d\_{\text{att}}}\right)},
where ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle denotes the standard Euclidean inner product, and αi​j\alpha\_{ij} are the attention weights obtained via a softmax normalization.

Instead of performing a single self-attention function, it is often beneficial to apply a multi-head self-attention function, which performs self-attention functions in parallel to the different components of 𝐗(n)\mathbf{X}^{(n)} and then linearly projects the concatenated outputs into an appropriate space.

Specifically, for h∈ℕ+h\in\mathbb{N}^{+} parallel heads, we introduce distinct projection matrices for each head i∈{1,…,h}i\in\{1,\dots,h\}:

|  |  |  |
| --- | --- | --- |
|  | Qi:=𝐗i(n)​WQi,Ki:=𝐗i(n)​WKi,Vi:=𝐗i(n)​WVi,Q\_{i}:=\mathbf{X}^{(n)}\_{i}W\_{Q\_{i}},\quad K\_{i}:=\mathbf{X}^{(n)}\_{i}W\_{K\_{i}},\quad V\_{i}:=\mathbf{X}^{(n)}\_{i}W\_{V\_{i}}, |  |

with 𝐗i(n)\mathbf{X}^{(n)}\_{i} denotes the input to head ii, obtained via linear projection and WQi,WKi,WVi∈ℝd×datt,iW\_{Q\_{i}},W\_{K\_{i}},W\_{V\_{i}}\in\mathbb{R}^{d\times d\_{\text{att},i}}.

Each head computes its own attention output (using Equation ([4](https://arxiv.org/html/2512.15088v1#S2.E4 "In 2.3 Self-attention mechanism ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"))):

|  |  |  |
| --- | --- | --- |
|  | headi=𝒜​(𝐗i(n);WQi,WKi,WVi)∈ℝn×datt,i,\text{head}\_{i}=\mathcal{A}(\mathbf{X}\_{i}^{(n)};W\_{Q\_{i}},W\_{K\_{i}},W\_{V\_{i}})\in\mathbb{R}^{n\times d\_{\text{att},i}}, |  |

and the outputs of all heads are concatenated and projected back to the original feature dimension via a learned matrix WO∈ℝh​datti×dW\_{O}\in\mathbb{R}^{h\;d\_{\text{att}\_{i}}\times d}, which results in the multi-head self-attention function, defined as

|  |  |  |
| --- | --- | --- |
|  | Multi-Head​(𝐗(n);WQ1,…,WQh,WK1,…,WKh,WV1,…,WVh,WO)\displaystyle\text{Multi-Head}(\mathbf{X}^{(n)};\,W^{Q\_{1}},\,\ldots,\,W^{Q\_{h}},\,W^{K\_{1}},\,\ldots,\,W^{K\_{h}},\,W^{V\_{1}},\,\ldots,\,W^{V\_{h}},\,W^{O}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | :=Concat​(head1,…,headh)​WO,\displaystyle:=\text{Concat}(\text{head}\_{1},\,\ldots,\,\text{head}\_{h})W^{O}, |  | (5) |

Multi-head self-attention mechanisms allow the model to jointly attend to information from different representation subspaces at different positions whereas a single-head mechanism restricts the model to one sub-space.

In the architecture, self-attention is applied to path features encoded by the signature transform (see Section [2.4](https://arxiv.org/html/2512.15088v1#S2.SS4 "2.4 Path signatures ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")), acting as a non-local feature aggregator over time.

### 2.4 Path signatures

A path signature transform [Lyons\_1998\_decay] is a feature extraction technique for sequential data, particularly effective for multivariate time series analysis.
It characterizes a path X={xt|xt=(xt1,…,xtd)∈ℝd,t∈[a,b]}X=\{x\_{t}|x\_{t}=(x\_{t}^{1},\ldots,x\_{t}^{d})\in\mathbb{R}^{d},\,t\in[a,\,b]\}, a,b∈ℝa,\,b\in\mathbb{R} through a sequence of iterated integrals, capturing complex temporal dependencies and interactions between different dimensions of the data.
Formally, the signature in the Stratonovich sense is defined as follows

|  |  |  |
| --- | --- | --- |
|  | Sig​(X):=(1,Sig1​(X),Sig2​(X),…,Sigi​(X),…),\displaystyle\text{Sig}(X):=\left(1,\,\text{Sig}\_{1}(X),\,\text{Sig}\_{2}(X),\,\ldots,\,\text{Sig}\_{i}(X),\,\ldots\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Sigi(X)=∫⋯​∫a<t1<⋯<ti<b∘dxt1⊗⋯⊗∘dxti,i=1, 2,…,\displaystyle\text{Sig}\_{i}(X)=\underset{a<t\_{1}<\cdots<t\_{i}<b}{\int\cdots\int}\circ dx\_{t\_{1}}\otimes\cdots\otimes\circ dx\_{t\_{i}},\quad i=1,\,2,\,\ldots, |  | (6) |

where ∘\circ denotes the Stratonovich integral and ⊗\otimes denotes the tensor product.
Here, the ”zeroth” term Sig0​(X)\text{Sig}\_{0}(X), by convention, is set to 1.
Moreover, we denote the truncated signature SigN​(X)=(1,Sig1N​(X),…,SigNN​(X))\text{Sig}^{N}(X)=\left(1,\,\text{Sig}^{N}\_{1}(X),\,\ldots,\,\text{Sig}^{N}\_{N}(X)\right) with the truncation order N∈ℕ+N\in\mathbb{N}^{+}.

We summarize two properties of signatures that make them attractive in learning from paths and we present these here without any proof.

###### Proposition 2.1 (Uniqueness ([Lyons\_2010\_uniqueness])).

Let 𝐗(n)=(X0,…,Xn−1)T∈ℝn×d\mathbf{X}^{(n)}={(X\_{0},\,\ldots,\,X\_{n-1})}^{T}\in\mathbb{R}^{n\times d} be a path stream, and define its time-augmented version as 𝐗^(n):=((X0,t0),…,(Xn−1,tn−1))T∈ℝn×(d+1)\mathbf{\widehat{X}}^{(n)}:={((X\_{0},\,t\_{0}),\,\ldots,\,(X\_{n-1},\,t\_{n-1}))}^{T}\in\mathbb{R}^{n\times(d+1)}.
Then the signature Sig​(𝐗^(n))\text{Sig}(\mathbf{\widehat{X}}^{(n)}) can uniquely determine 𝐗(n)\mathbf{X}^{(n)} up to a translation.

Proposition [2.1](https://arxiv.org/html/2512.15088v1#S2.Thmproposition1 "Proposition 2.1 (Uniqueness ([Lyons_2010_uniqueness])). ‣ 2.4 Path signatures ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") implies that there is no information lost in the signature transform.
The time-augmented path is necessary because the signature transform is invariant to time reparameterizations, meaning it encodes only the data arrival order, not the precise timing.

###### Proposition 2.2 (Factorial decay ([Lyons\_1998\_decay])).

There exists a constant C​(𝐗(n))C(\mathbf{X}^{(n)}) depending on the path stream 𝐗(n)\mathbf{X}^{(n)} such that

|  |  |  |
| --- | --- | --- |
|  | ‖Sigi​(𝐗(n))‖≤C​(𝐗(n))ii!,\left\|\text{Sig}\_{i}(\mathbf{X}^{(n)})\right\|\leq\frac{C(\mathbf{X}^{(n)})^{i}}{i!}, |  |

where ∥⋅∥\left\|\cdot\right\| is any tensor norm on (ℝd)⊗i{(\mathbb{R}^{d})}^{\otimes i}.

Proposition [2.2](https://arxiv.org/html/2512.15088v1#S2.Thmproposition2 "Proposition 2.2 (Factorial decay ([Lyons_1998_decay])). ‣ 2.4 Path signatures ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") indicates that the terms of the signature decay factorially in size. This ensures that the most significant contributions are given by the lower order terms which justifies the use of truncated signatures.

## 3 Methodology

In this section, we describe the architecture of the SigMA model, as shown in Figure [1](https://arxiv.org/html/2512.15088v1#S3.F1 "Figure 1 ‣ 3 Methodology ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"); the rationale behind these design choices is discussed in Section [4.2](https://arxiv.org/html/2512.15088v1#S4.SS2 "4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").

![Refer to caption](x1.png)


Figure 1: Architecture of the SigMA model.

### 3.1 Convolutional feature extraction

Consider a data stream 𝐗(n)=(X0,…,Xn−1)T∈ℝn×d\mathbf{X}^{(n)}={(X\_{0},\,\ldots,\,X\_{n-1})}^{T}\in\mathbb{R}^{n\times d}, interpreted as a discretized path. It is beneficial to apply a feature mapping before computing the signature transform (see [Lyons\_2019\_DeepSignature]). Therefore, at the input of SigMA, a convolutional layer Φ​(𝐗(n);WΦ,BΦ):ℝn×d↦ℝn~×d~\Phi(\mathbf{X}^{(n)};\,W^{\Phi},B^{\Phi}):\mathbb{R}^{n\times d}\mapsto\mathbb{R}^{\widetilde{n}\times\widetilde{d}} with kernel size k∈ℕ+k\in\mathbb{N}^{+} and stride s∈ℕ+s\in\mathbb{N}^{+} is applied to perform the feature mapping

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(𝐗(n);WΦ,BΦ)=WΦ⋆𝐗(n)+𝟏n~​BΦ,\Phi(\mathbf{X}^{(n)};\,W^{\Phi},B^{\Phi})=W^{\Phi}\star\mathbf{X}^{(n)}+\mathbf{1}\_{\widetilde{n}}B^{\Phi}, |  | (7) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | (WΦ⋆𝐗(n))i,j=∑i1=1k∑i2=1dWj,i1,i2Φ​𝐗s​(i−1)+i1,i2(n),i=1,…,n~,j=1,…,d~,(W^{\Phi}\star\mathbf{X}^{(n)})\_{i,j}=\sum\limits\_{i\_{1}=1}^{k}\sum\limits\_{i\_{2}=1}^{d}W^{\Phi}\_{j,i\_{1},i\_{2}}\mathbf{X}^{(n)}\_{s(i-1)+i\_{1},i\_{2}},\quad i=1,\,\ldots,\,\widetilde{n},\,j=1,\,\ldots,\,\widetilde{d}, |  | (8) |

where WΦ∈ℝd~×k×dW^{\Phi}\in\mathbb{R}^{\widetilde{d}\times k\times d} and BΦ∈ℝd~B^{\Phi}\in\mathbb{R}^{\widetilde{d}} are the weights and biases of this convolutional layer, respectively, while n~∈ℕ+\widetilde{n}\in\mathbb{N}^{+} and d~∈ℕ+\widetilde{d}\in\mathbb{N}^{+} represent the dimensions of outputs.
We denote ⋆\star as the valid cross-correlation operator and 𝟏n~∈ℝn~\mathbf{1}\_{\widetilde{n}}\in\mathbb{R}^{\widetilde{n}} is an all-ones column vector. This convolutional layer is shown in Section [4.2.3](https://arxiv.org/html/2512.15088v1#S4.SS2.SSS3 "4.2.3 Ablation: convolutional and MLP layers ‣ 4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") to improve the accuracy of the SigMA model. After the feature mapping, according to Proposition [2.1](https://arxiv.org/html/2512.15088v1#S2.Thmproposition1 "Proposition 2.1 (Uniqueness ([Lyons_2010_uniqueness])). ‣ 2.4 Path signatures ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), it is beneficial to augment the output with time before taking the signature transform.

### 3.2 Signature transform on lifted paths

Taking the signature transform can extract the geometric features from original paths while filtering out irrelevant information, however, it will consume the stream-like nature of the input data (see [Lyons\_2019\_DeepSignature]).
Let us consider a stream of data 𝐘(n~)=(Y0,…,Yn~−1)T∈ℝn~×d~\mathbf{Y}^{(\widetilde{n})}={(Y\_{0},\,\ldots,\,Y\_{\widetilde{n}-1})}^{T}\in\mathbb{R}^{\widetilde{n}\times\widetilde{d}}, which is the output of the convolutional layer and has been augmented.
Here, d~\widetilde{d} denotes the number of features, n~\widetilde{n} denotes the length of the sequence and is assumed to be even.

We lift the data with the stride equals to half of the sequence length before taking the signature transform as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | l​(𝐘(n~)):=(𝐘0:n~2(n~),𝐘0:n~(n~)),l(\mathbf{Y}^{(\widetilde{n})}):=(\mathbf{Y}^{(\widetilde{n})}\_{0:\frac{\widetilde{n}}{2}},\,\mathbf{Y}^{(\widetilde{n})}\_{0:\widetilde{n}}), |  | (9) |

where 𝐘0:i(n~)=(Y0,…,Yi−1)T∈ℝi×d~\mathbf{Y}^{(\widetilde{n})}\_{0:i}={(Y\_{0},\,\ldots,\,Y\_{i-1})}^{T}\in\mathbb{R}^{i\times\widetilde{d}} for i=n~2,n~i=\frac{\widetilde{n}}{2},\,\widetilde{n}. Here, the stride controls the overlap between successive lifted segments, and each element in the lifted data l​(𝐘(n~))l(\mathbf{Y}^{(\widetilde{n})}) is sequential data.
Then the output of taking the signature transform with this lifted data becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | SigN​(l​(𝐘(n~)))=(SigN​(𝐘0:n~2(n~)),SigN​(𝐘0:n~(n~)))T.\text{Sig}^{N}(l(\mathbf{Y}^{(\widetilde{n})}))={(\text{Sig}^{N}(\mathbf{Y}^{(\widetilde{n})}\_{0:\frac{\widetilde{n}}{2}}),\,\text{Sig}^{N}(\mathbf{Y}^{(\widetilde{n})}\_{0:\widetilde{n}}))}^{T}. |  | (10) |

It should be noted that setting the stride equal to half the sequence length in Equation ([9](https://arxiv.org/html/2512.15088v1#S3.E9 "In 3.2 Signature transform on lifted paths ‣ 3 Methodology ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")) represents a validated trade-off between model accuracy and complexity, as we have investigated the effect of stride values on both the accuracy and complexity of the neural network models in Section [4.2.1](https://arxiv.org/html/2512.15088v1#S4.SS2.SSS1 "4.2.1 Sensitivity to the stride parameter ‣ 4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").

### 3.3 Multi-head self-attention on signature features

Recall that the signature transform can be considered as a feature mapping which helps to extract the information from the input data while filtering out irrelevant information. The signature transform yields a high-dimensional feature representation that typically requires additional processing. A common approach is to use a FNN, as in Deep Signature Networks [Lyons\_2019\_DeepSignature]. In addition to an FNN, we incorporate a self-attention layer, which is particularly effective for joint multi-parameter estimation.

Consider the output obtained by taking the signature transform as follows222The matrix stacks signature terms across truncation levels and lifted subpaths.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | SigN​(l​(𝐘(n~)))\displaystyle\text{Sig}^{N}(l(\mathbf{Y}^{(\widetilde{n})})) | =\displaystyle= | (SigN​(𝐘0:n~2(n~)),SigN​(𝐘0:n~(n~)))T\displaystyle{(\text{Sig}^{N}(\mathbf{Y}^{(\widetilde{n})}\_{0:\frac{\widetilde{n}}{2}}),\,\text{Sig}^{N}(\mathbf{Y}^{(\widetilde{n})}\_{0:\widetilde{n}}))}^{T} |  | (11) |
|  |  | =\displaystyle= | (Sig1N​(𝐘0:n~2(n~))⋯SigNN​(𝐘0:n~2(n~))Sig1N​(𝐘0:n~(n~))⋯SigNN​(𝐘0:n~(n~)))2×d~N+1−d~d~−1.\displaystyle{\begin{pmatrix}\text{Sig}\_{1}^{N}(\mathbf{Y}^{(\widetilde{n})}\_{0:\frac{\widetilde{n}}{2}})&\cdots&\text{Sig}\_{N}^{N}(\mathbf{Y}^{(\widetilde{n})}\_{0:\frac{\widetilde{n}}{2}})\\ \ \text{Sig}\_{1}^{N}(\mathbf{Y}^{(\widetilde{n})}\_{0:\widetilde{n}})&\cdots&\text{Sig}\_{N}^{N}(\mathbf{Y}^{(\widetilde{n})}\_{0:\widetilde{n}})\end{pmatrix}}\_{2\times\frac{\widetilde{d}^{N+1}-\widetilde{d}}{\widetilde{d}-1}}. |  |

We then apply a self-attention function, as shown in Equation ([4](https://arxiv.org/html/2512.15088v1#S2.E4 "In 2.3 Self-attention mechanism ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")), resulting in the output Self-Attention​(SigN​(l​(𝐘(n~))))\text{Self-Attention}(\text{Sig}^{N}(l(\mathbf{Y}^{(\widetilde{n})}))), where we omit the weight matrices for simplicity.

As discussed in Section [2.3](https://arxiv.org/html/2512.15088v1#S2.SS3 "2.3 Self-attention mechanism ‣ 2 Problem setting and framework ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), which is also verified in Section [4.2.2](https://arxiv.org/html/2512.15088v1#S4.SS2.SSS2 "4.2.2 Effect of signature truncation order ‣ 4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), using a multi-head attention mechanism is empirically beneficial instead of a single-head one.
Therefore, we employ an NN-head self-attention function, with each head corresponding to a distinct signature level, as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | Multi-Head​(SigN​(l​(𝐘(n~))))=Concat​(head1,…,headN)​W~O,\text{Multi-Head}(\text{Sig}^{N}(l(\mathbf{Y}^{(\widetilde{n})})))=\text{Concat}(\text{head}\_{1},\,\ldots,\,\text{head}\_{N})\widetilde{W}\_{O}, |  | (12) |

where headi=Self-Attention​((SigiN​(𝐘0:n~2(n~)),SigiN​(𝐘0:n~(n~)))T)\text{head}\_{i}=\text{Self-Attention}({(\text{Sig}\_{i}^{N}(\mathbf{Y}^{(\widetilde{n})}\_{0:\frac{\widetilde{n}}{2}}),\,\text{Sig}\_{i}^{N}(\mathbf{Y}^{(\widetilde{n})}\_{0:\widetilde{n}}))}^{T}) for i=1,…,Ni=1,\,\ldots,\,N.
Here we also omit all the weight matrix except the linear projection matrix W~O\widetilde{W}\_{O} for the output.
After the NN-head self-attention layer, we need to project the output to an appropriate dimension using another MLP architecture, which has been shown to be important for the robustness of the SigMA model in Section [4.2.3](https://arxiv.org/html/2512.15088v1#S4.SS2.SSS3 "4.2.3 Ablation: convolutional and MLP layers ‣ 4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").

Now we can clarify the specific architecture of the SigMA as below:

* •

  a convolutional layer with 3 channels and kernel size 3;
* •

  augmentation with time and original values;
* •

  lifting performed as Equation ([9](https://arxiv.org/html/2512.15088v1#S3.E9 "In 3.2 Signature transform on lifted paths ‣ 3 Methodology ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")) with stride equal to half of the sequence length;
* •

  taking the signature transform with truncation order N=3N=3;
* •

  a multi-head self-attention layer with the number of heads h=N=3h=N=3 and each different head corresponds to a different signature level;
* •

  a MLP with 5 hidden layers, each of size 32 and ReLU activation;
* •

  a non-linear transform with sigmoid function.

## 4 Numerical and empirical experiments

In this section, we conduct experiments to verify the advantages of the architecture described in Section [3](https://arxiv.org/html/2512.15088v1#S3 "3 Methodology ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") and motivate the architectural choices. To this end, we compare SigMA333Source code is available on <https://github.com/changanluoxue/SigMA.git> with four other neural network-based models.
The first model is a CNN proposed by [stone2020calibrating].444Source code is available on <https://github.com/henrymstone/rough-calibration-using-CNNS>
The second model is a signature-based (DeepSigNet) model proposed by [Lyons\_2019\_DeepSignature].555Source code is available on <https://github.com/patrick-kidger/Deep-Signature-Transforms>
The third model is a modified Transformer based on [vaswani\_2017].
The fourth model is a LSTM model proposed by [csanady2024parameter].666Source code is available on <https://github.com/aielte-research/LMSParEst>
The specific architectures of these four models are detailed in Appendix [A](https://arxiv.org/html/2512.15088v1#A1 "Appendix A Architectural details of baseline and signature-based neural networks ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").

This section is divided into five subsections. Firstly, we clarify the synthetic data generation and some implementation details.
In Section [4.1](https://arxiv.org/html/2512.15088v1#S4.SS1 "4.1 Data generation and implementation details ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), we perform sensitivity analysis to determine the optimal architecture of the SigMA model.
Next, we discuss the single and multiple parameters estimation problems in Sections [4.3](https://arxiv.org/html/2512.15088v1#S4.SS3 "4.3 Hurst parameter estimation ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") and  [4.4](https://arxiv.org/html/2512.15088v1#S4.SS4 "4.4 Joint multi-parameter estimation ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").
Finally, in Section [4.5](https://arxiv.org/html/2512.15088v1#S4.SS5 "4.5 Empirical applications on real-world datasets ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), we present two empirical studies: one using realized volatility data from financial markets and another employing Li-ion battery degradation data.

### 4.1 Data generation and implementation details

Before conducting the experiments, we detail the generation of the synthetic paths used in the study and provide implementation specifics to ensure full reproducibility of the results.
To generate datasets containing paths with varying characteristics, we first sample five Hurst parameters, HH, from two different probability distributions: the Uniform distribution777The set of possible HH values for fBm is {0.14,0.23,0.56,0.67,0.89}\{0.14,0.23,0.56,0.67,0.89\}, whereas the fOU employs another set of {0.55,0.66,0.72,0.85,0.94}\{0.55,0.66,0.72,0.85,0.94\}. on (0,1)(0,1) and (0.5,1)(0.5,1) and the Beta (1,9)(1,9) distribution.888The set of possible HH values for rHeston is {0.04,0.08,0.11,0.16,0.21}\{0.04,0.08,0.11,0.16,0.21\}, consistent with its theoretical construction in the rough regime.
Paths with HH from the Beta distribution are rougher than those from the Uniform distribution, while extending the Uniform’s support to H>12H>\frac{1}{2} induces long memory.
Using these different HH values, we simulate fBm, fOU, and rHeston paths with varying numbers of time steps {100,500,1000,1500}\{100,500,1000,1500\}, with each training/test data set containing 3000/1000 samples.

We use the Cholesky decomposition to simulate fBm and subsequently generate fOU paths with α=0.5\alpha=0.5, μ=0.15\mu=0.15, σ=0.2\sigma=0.2, and X0f​O​U=0.01X\_{0}^{fOU}=0.01.
For simulating rHeston paths, we apply the fast algorithm proposed by [ma\_2022\_fast], using the parameters κ1=0.1\kappa\_{1}=0.1, κ2=0.03\kappa\_{2}=0.03, θ=0.3\theta=0.3, and X0r​H=0.01X\_{0}^{rH}=0.01.

We use the adaptive moment estimation (Adam) optimizer to train the different neural network models, with a batch size of 60, trained for 150150 epochs, and a learning rate of 10−410^{-4}. The root mean squared error (RMSE) is used as a loss function.
All experiments were run on a system with CUDA 12.8, utilizing GPU acceleration. The specific versions of the key libraries were: PyTorch 2.8.0, Python 3.10.12.

The full implementation, data-generation scripts, and examples are available at [[GitHub link]](https://github.com/changanluoxue/SigMA.git).

### 4.2 Sensitivity analysis of the SigMA architecture

We first perform a sensitivity analysis on the stride and signature truncation order to identify the optimal configuration of the SigMA model, balancing accuracy with computational complexity.
We then present illustrative examples to validate the effectiveness of both the convolutional layer and MLP components within the model.

#### 4.2.1 Sensitivity to the stride parameter

As discussed in Section [3.2](https://arxiv.org/html/2512.15088v1#S3.SS2 "3.2 Signature transform on lifted paths ‣ 3 Methodology ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), the lifting operation before taking the signature transform can preserve the stream-like nature of the data and then improve the performance of the SigMA model.
The lifting operation with a smaller stride increases the frequency of the signature transform, which is time-consuming, and also extends the input length of the subsequent multi-head self-attention layer, thereby increasing the number of model parameters.
Since the lifting operation increases the complexity of the SigMA model, it is crucial to determine an optimal stride that balances the model complexity with performance, which is the aim of this section.

In this example, we use the simulated paths from Section [4.1](https://arxiv.org/html/2512.15088v1#S4.SS1 "4.1 Data generation and implementation details ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") to explore the optimal stride for paths of varying lengths.
The stride of the lifting operation is adjusted from 11 to n2\frac{n}{2} (e.g., half the input sequence length), while other settings remain consistent with Section [4.1](https://arxiv.org/html/2512.15088v1#S4.SS1 "4.1 Data generation and implementation details ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").
It should be noted that stride=input length\textit{stride}=\textit{input length} effectively means that no lifting is applied, thus the maximum possible stride for a path stream is half its length.

We present the test RMSEs for estimating the Hurst parameter across different stochastic processes using the SigMA model with varying stride in Table [1](https://arxiv.org/html/2512.15088v1#S4.T1 "Table 1 ‣ 4.2.1 Sensitivity to the stride parameter ‣ 4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").
From the results, two conclusions can be drawn.
Firstly, the complex stochastic processes (i.e. the fOU and rHeston) tend to use small strides to achieve high accuracy.
This observed sensitivity likely stems from the drift term in the fOU and rHeston, which the fBm does not include.
Secondly, decreasing the stride significantly increases the number of parameters of the NN with negligible benefit in terms of accuracy for all models.
This suggests that a larger stride (stride=n2\textit{stride}=\frac{n}{2}) should be chosen to strike a balance, as the slight improvement in model performance comes with a sharp increase in complexity.

Table 1: Test RMSEs for Hurst estimation across stochastic processes of varying lengths (100-1500), obtained using the SigMA model with strides varying from 11 to n2\frac{n}{2}, are averaged over 3 training runs. Here, H∼Uniform​(0, 1)H\sim\text{Uniform}(0,\,1) for the fBm, H∼Uniform​(0.5, 1)H\sim\text{Uniform}(0.5,\,1) for the fOU, and H∼Beta​(1, 9)H\sim\text{Beta}(1,\,9) for the rHeston. The best accuracies across different strides are in bold.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Input lengths | Strides | Stochastic processes | | | #\#Params |
| fBm | fOU | rHeston |
| 100 | 1 | 1.94e-2 | 2.51e-2 | 4.92e-2 | 573306 |
| 10 | 1.49e-2 | 2.73e-2 | 5.07e-2 | 126906 |
| 50 | 1.58e-2 | 2.67e-2 | 5.25e-2 | 87226 |
| 500 | 50 | 8.71e-3 | 1.72e-2 | 1.06e-2 | 126906 |
| 250 | 8.45e-3 | 1.87e-2 | 1.09e-2 | 87226 |
| 1000 | 50 | 1.08e-2 | 2.37e-2 | 8.13e-3 | 176506 |
| 500 | 6.05e-3 | 1.72e-2 | 7.48e-3 | 87226 |
| 1500 | 50 | 7.81e-3 | 2.08e-2 | 7.18e-3 | 226106 |
| 750 | 2.71e-2 | 2.05e-2 | 7.61e-3 | 87226 |

#### 4.2.2 Effect of signature truncation order

In this section, we aim to explore the effects of varying signature truncation orders on the accuracy of the SigMA model.
In this experiment, we use the simulated paths from Section [4.1](https://arxiv.org/html/2512.15088v1#S4.SS1 "4.1 Data generation and implementation details ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") with lengths from {100, 500}\{100,\,500\} and we vary the signature truncation order from {1, 3, 5}\{1,\,3,\,5\}, while keeping other settings consistent with those in Section [4.1](https://arxiv.org/html/2512.15088v1#S4.SS1 "4.1 Data generation and implementation details ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").
In addition to the SigMA model, we introduce a simpler version with a single-head self-attention layer, called SigSA (details in Appendix [A](https://arxiv.org/html/2512.15088v1#A1 "Appendix A Architectural details of baseline and signature-based neural networks ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")).
We also present results for the DeepSigNet model because it also incorporates the signature transform.
Based on the finding from the previous section, we set a large stride as half of the input length.

The results are presented in Figure [2](https://arxiv.org/html/2512.15088v1#S4.F2 "Figure 2 ‣ 4.2.2 Effect of signature truncation order ‣ 4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") with details in Table [2](https://arxiv.org/html/2512.15088v1#S4.T2 "Table 2 ‣ 4.2.2 Effect of signature truncation order ‣ 4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").
From the results, there are three conclusions to be drawn.
Firstly, there are benefits for accuracy to increase the signature truncation order, particularly at low orders (11 to 33).
However, when the truncation order is sufficiently high (33 to 55), the accuracy gains become negligible and overfitting issues may emerge. The complex stochastic processes (i.e. the fOU and rHeston) require higher optimal truncation orders compared to the simpler one (i.e. the fBm), which explains why the overfitting issues tend to occur in the fBm case.
Furthermore, increasing the truncation order significantly increases the model complexity.
Secondly, a higher truncation order does not improve the performance of the SigSA model for the fOU paths. We attribute this to the single-head self-attention layer in the SigSA model, which is less effective at extracting information from the path signature compared to the multi-head self-attention layer.
Thirdly, signature-based models with multi-head self-attention layers exhibit similar performance when the signature truncation order is set to 1, since the underlying stochastic processes are path-dependent and cannot be adequately represented by first-order increments alone.
Notably, under such configurations, these models may even outperform the SigSA model, which is attributed to the limited capacity of a single-head self-attention mechanism to capture intricate path-dependent structures.
This suggests that we should select a signature truncation order of 33 for the SigMA and DeepSigNet models to balance the accuracy and complexity.

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

(a) The input lengths equal to 100100

![Refer to caption](x5.png)

![Refer to caption](x6.png)

![Refer to caption](x7.png)

(b) The input lengths equal to 500500

Figure 2: Test RMSE trends for Hurst estimation across stochastic processes (Left: fBms; Middle: fOU; Right: rHeston) of varying lengths (100-500), obtained using the signature-based NN models with varying signature truncation orders (1-5), are averaged over 3 training runs. Here, H∼Uniform​(0, 1)H\sim\text{Uniform}(0,\,1) for the fBm, H∼Uniform​(0.5, 1)H\sim\text{Uniform}(0.5,\,1) for the fOU, and H∼Beta​(1, 9)H\sim\text{Beta}(1,\,9) for the rHeston.




Table 2: Test RMSEs for Hurst estimation across stochastic processes of varying lengths (100-500), obtained using the signature-based NN models with varying signature truncation orders (1-5), are averaged over 3 training runs. Here, H∼Uniform​(0, 1)H\sim\text{Uniform}(0,\,1) for the fBm, H∼Uniform​(0.5, 1)H\sim\text{Uniform}(0.5,\,1) for the fOU, and H∼Beta​(1, 9)H\sim\text{Beta}(1,\,9) for the rHeston. The best accuracies across different signature truncation orders are in bold.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Models | Test RMSE for input length 100100 | | | Test RMSE for input length 500500 | | | #\#Params | Truncation order |
| fBm | fOU | rHeston | fBm | fOU | rHeston |
| DeepSigNet | 9.52e-2 | 1.34e-1 | 5.89e-2 | 9.32e-2 | 1.37e-1 | 5.92e-2 | 4461 | 1 |
| 1.72e-2 | 3.34e-2 | 5.81e-2 | 8.41e-3 | 2.18e-2 | 5.03e-2 | 9261 | 3 |
| 1.34e-2 | 3.41e-2 | 5.78e-2 | 4.53e-2 | 2.93e-2 | 3.44e-2 | 129261 | 5 |
| SigMA | 1.18e-1 | 1.34e-1 | 5.89e-2 | 1.26e-1 | 1.37e-1 | 5.92e-2 | 4726 | 1 |
| 1.51e-2 | 2.96e-2 | 5.44e-2 | 8.89e-3 | 1.59e-2 | 1.02e-2 | 87226 | 3 |
| 1.06e-2 | 2.44e-2 | 3.48e-2 | 8.24e-2 | 1.26e-2 | 1.01e-2 | 46024726 | 5 |
| SigSA | 2.85e-1 | 1.36e-1 | 1.15e-1 | 2.74e-1 | 1.39e-1 | 7.59e-2 | 15 | 1 |
| 1.32e-1 | 1.35e-1 | 5.89e-2 | 1.33e-1 | 1.39e-1 | 5.92e-2 | 603 | 3 |
| 1.09e-1 | 1.35e-1 | 5.89e-2 | 1.08e-1 | 1.39e-1 | 5.92e-2 | 11595 | 5 |

#### 4.2.3 Ablation: convolutional and MLP layers

In this section, we investigate the impact of the convolutional and MLP layers in the SigMA model. It is noted in
[tong\_2023\_SigFormer] that the Transformer in their model can extract representations from signatures without using a convolutional layer.
Therefore, we aim to determine whether including the convolutional and MLP layers in the SigMA model improves accuracy and stability during training.
We compare SigMA to three different architectures, varying the inclusion of these layers (details in Appendix [A](https://arxiv.org/html/2512.15088v1#A1 "Appendix A Architectural details of baseline and signature-based neural networks ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")).

The results are summarized in Table [3](https://arxiv.org/html/2512.15088v1#S4.T3 "Table 3 ‣ 4.2.3 Ablation: convolutional and MLP layers ‣ 4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), and a representative loss curve is shown in Figure [3](https://arxiv.org/html/2512.15088v1#S4.F3 "Figure 3 ‣ 4.2.3 Ablation: convolutional and MLP layers ‣ 4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").
These results demonstrate that the SigMA architecture outperforms the one used in [tong\_2023\_SigFormer] (i.e., SigMA without convolutional layer & MLP) in terms of test error accuracy.
This superiority extends across various stochastic processes and different training data settings (i.e., length and sampling of HH).
Figure [3](https://arxiv.org/html/2512.15088v1#S4.F3 "Figure 3 ‣ 4.2.3 Ablation: convolutional and MLP layers ‣ 4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") further suggests that SIGMA’s architecture exhibits stable training dynamics.
Notably, the inclusion of the MLP appears to contribute significantly to this robustness, making the SigMA model stable and accurate. Architectures without the MLP achieve good training and test accuracy in some cases but lack consistency and can be erratic.
By contrast, adding a convolutional layer appears to improve training accuracy.

![Refer to caption](x8.png)


Figure 3: Loss curve from a typical training run for Hurst estimation of the fBm process with a sequence length of 500.




Table 3: Test RMSEs for Hurst estimation across stochastic processes of varying lengths (100-1500), obtained using the SigMA model and its variants, are averaged over 3 training runs. Here, H∼Uniform​(0, 1)H\sim\text{Uniform}(0,\,1) for the fBm, H∼Uniform​(0.5, 1)H\sim\text{Uniform}(0.5,\,1) for the fOU, and H∼Beta​(1, 9)H\sim\text{Beta}(1,\,9) for the rHeston. The best accuracies across SigMA and its variants are in bold.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Models | Input lengths | Stochastic processes | | | #\#Params |
| fBm | fOU | rHeston |
| SigMA | 100 | 1.50e-2 | 2.81e-2 | 5.20e-2 | 87226 |
| 500 | 8.30e-3 | 1.68e-2 | 1.20e-2 | 87226 |
| 1000 | 1.03e-2 | 1.71e-2 | 7.23e-3 | 87226 |
| 1500 | 2.49e-2 | 2.20e-2 | 7.10e-3 | 87226 |
| SigMA without convolutional layer | 100 | 1.06e-1 | 1.31e-1 | 5.88e-2 | 5647 |
| 500 | 1.05e-1 | 1.33e-1 | 5.91e-2 | 5647 |
| 1000 | 1.05e-1 | 1.34e-1 | 5.90e-2 | 5647 |
| 1500 | 1.02e-1 | 1.32e-1 | 5.99e-2 | 5647 |
| SigMA without MLP | 100 | 1.15e-1 | 7.08e-2 | 3.80e-2 | 73328 |
| 500 | 1.39e-1 | 7.73e-2 | 1.82e-2 | 73328 |
| 1000 | 1.80e-1 | 7.72e-2 | 1.83e-2 | 73328 |
| 1500 | 2.44e-1 | 7.93e-2 | 1.88e-2 | 73328 |
| SigMA without convolutional layer & MLP1 | 100 | 1.68e-1 | 1.33e-1 | 5.85e-2 | 491 |
| 500 | 1.64e-1 | 1.36e-1 | 5.88e-2 | 491 |
| 1000 | 1.72e-1 | 1.35e-1 | 5.82e-2 | 491 |
| 1500 | 1.61e-1 | 1.33e-1 | 5.92e-2 | 491 |

* 1

  SigMA without convolutional layer & MLP actually has the same architecture as the SigFormer model used in [tong\_2023\_SigFormer].

### 4.3 Hurst parameter estimation

The analysis in Section [4.2](https://arxiv.org/html/2512.15088v1#S4.SS2 "4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") provides a reference for the architecture of the SigMA model, which we will evaluate using single-parameter estimation problems in this section.
To this end, we train a variety of neural network models, as mentioned in the beginning of Section [4](https://arxiv.org/html/2512.15088v1#S4 "4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), to perform the estimation using synthetic paths from Section [4.1](https://arxiv.org/html/2512.15088v1#S4.SS1 "4.1 Data generation and implementation details ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").
That is, we aim to learn the mapping 𝐗(n)↦H\mathbf{X}^{(n)}\mapsto H.
All the settings remain the same as described in Section [4.1](https://arxiv.org/html/2512.15088v1#S4.SS1 "4.1 Data generation and implementation details ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").

To present the results clearly, we plot them in Figure [4](https://arxiv.org/html/2512.15088v1#S4.F4 "Figure 4 ‣ 4.3 Hurst parameter estimation ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), and the details can be found in Table [4](https://arxiv.org/html/2512.15088v1#S4.T4 "Table 4 ‣ 4.3 Hurst parameter estimation ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").
From these results, there are three conclusions to be drawn.
Firstly, the SigMA model tends to achieve the best accuracy for the case of fOU and rHeston and it also achieve good accuracy, comparing with the competing models, for the case of fBm.
Moreover, both the SigMA and DeepSigNet achieve high accuracy with significantly lower complexity than competing models, a performance improvement we attribute to the signature transform integrated into their architectures.
In fact, the signature transform can extract core patterns from sequences, thereby filtering noise while preserving critical information for further processing.
Secondly, both the SigMA and DeepSigNet models offer a significant advantage: their complexity, measured by the number of parameters, does not increase with input length. This excellent feature arises from the introduction of the signature transform, where the length of the path signature depends only on the number of features.
Notably, the lifting operation before taking the signature transform would violate this advantage, therefore, as discussed in Section [4.2.1](https://arxiv.org/html/2512.15088v1#S4.SS2.SSS1 "4.2.1 Sensitivity to the stride parameter ‣ 4.2 Sensitivity analysis of the SigMA architecture ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), we choose the stride equal to half the input length to avoid this issue.
Thirdly, for pure fBm the test error of SigMA slightly deteriorates when increasing the number of time steps from 1000 to 1500 (Figure [4(a)](https://arxiv.org/html/2512.15088v1#S4.F4.sf1 "In Figure 4 ‣ 4.3 Hurst parameter estimation ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")), a behaviour also observed for the Transformer baseline.
We attribute this to the combination of the strong self-similarity of fBm and the fixed-dimensional signature/attention bottleneck in the architecture: as the path length grows, a larger number of highly correlated increments must be compressed into a signature of fixed order, so that additional observations become largely redundant and may even degrade generalization.
Similar non-monotone finite-sample effects with respect to sample size have been reported for classical Hurst estimators in long-memory settings.
By contrast, the fOU and rHeston models possess additional drift and volatility structure; for these processes longer paths carry genuinely more information, and SigMA’s performance continues to improve (at least does not deteriorate) as the input length increases (Figures [4(b)](https://arxiv.org/html/2512.15088v1#S4.F4.sf2 "In Figure 4 ‣ 4.3 Hurst parameter estimation ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")-[4(c)](https://arxiv.org/html/2512.15088v1#S4.F4.sf3 "In Figure 4 ‣ 4.3 Hurst parameter estimation ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs")).

![Refer to caption](x9.png)


(a) fBm

![Refer to caption](x10.png)


(b) fOU

![Refer to caption](x11.png)


(c) rHeston

Figure 4: Test RMSE trends for Hurst estimation across stochastic processes of varying lengths (100-1500), obtained using various NN models, are averaged over 3 training runs. Here, H∼Uniform​(0, 1)H\sim\text{Uniform}(0,\,1) for the fBm, H∼Uniform​(0.5, 1)H\sim\text{Uniform}(0.5,\,1) for the fOU, and H∼Beta​(1, 9)H\sim\text{Beta}(1,\,9) for the rHeston.




Table 4: Test RMSEs for Hurst estimation across stochastic processes of varying lengths (100100-15001500), obtained using various NN models, are averaged over 3 training runs. Here, H∼Uniform​(0, 1)H\sim\text{Uniform}(0,\,1) for the fBm, H∼Uniform​(0.5, 1)H\sim\text{Uniform}(0.5,\,1) for the fOU, and H∼Beta​(1, 9)H\sim\text{Beta}(1,\,9) for the rHeston. The best accuracies across different NN models are in bold.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Models | Input lengths | Stochastic processes | | | #\#Params |
| fBm | fOU | rHeston |
| Transformer1 | 100 | 1.90e-2 | 9.22e-2 | 5.72e-2 | 573906 |
| 500 | 4.68e-2 | 8.93e-2 | 5.24e-2 | 2557906 |
| 1000 | 7.75e-2 | 9.53e-2 | 4.37e-2 | 5037906 |
| 1500 | 8.94e-2 | 9.24e-2 | 4.25e-2 | 7517906 |
| CNN2 | 100 | 1.05e-1 | 4.30e-2 | 8.05e-2 | 255073 |
| 500 | 1.07e-1 | 4.05e-2 | 7.65e-2 | 500833 |
| 1000 | 1.12e-1 | 4.01e-2 | 6.60e-2 | 812129 |
| 1500 | 1.10e-1 | 3.85e-2 | 5.79e-2 | 1107041 |
| LSTM3 | 100 | 7.70e-2 | 9.22e-2 | 7.25e-2 | 1829634 |
| 500 | 5.35e-2 | 4.69e-2 | 6.29e-2 | 8383234 |
| 1000 | 3.83e-2 | 3.19e-2 | 6.16e-2 | 16575234 |
| 1500 | 3.89e-2 | 3.46e-2 | 6.11e-2 | 24767234 |
| SigMA | 100 | 1.60e-2 | 2.82e-2 | 4.78e-2 | 87226 |
| 500 | 9.02e-3 | 1.61e-2 | 1.01e-2 | 87226 |
| 1000 | 6.84e-3 | 2.03e-2 | 7.23e-3 | 87226 |
| 1500 | 3.13e-2 | 2.28e-2 | 7.06e-3 | 87226 |
| DeepSigNet4 | 100 | 1.66e-2 | 3.51e-2 | 5.77e-2 | 9261 |
| 500 | 8.51e-3 | 3.01e-2 | 5.13e-2 | 9261 |
| 1000 | 8.16e-3 | 2.96e-2 | 1.97e-2 | 9261 |
| 1500 | 1.09e-2 | 2.51e-2 | 9.05e-3 | 9261 |

* 1

  The Transformer proposed by [vaswani\_2017].
* 2

  The CNN proposed by [stone2020calibrating].
* 3

  The LSTM proposed by [csanady2024parameter].
* 4

  The DeepSigNet proposed by [Lyons\_2019\_DeepSignature].

### 4.4 Joint multi-parameter estimation

In the previous example, we observed that the SigMA model tends to outperform competing models in many complex single-parameter estimation problems. Therefore, it is natural to consider extending the SigMA model to multiple-parameter estimation problems.

#### 4.4.1 Implementation details

To generate the datasets for multiple-parameter estimation problems, we first sample different values of α,μ,σ,κ1,κ2\alpha,\,\mu,\,\sigma,\,\kappa\_{1},\,\kappa\_{2} and θ\theta from the distribution shown in Table [5](https://arxiv.org/html/2512.15088v1#S4.T5 "Table 5 ‣ 4.4.1 Implementation details ‣ 4.4 Joint multi-parameter estimation ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").
We then simulate fOU and rHeston paths using these parameters, along with H∼Uniform​(0.5, 1)H\sim\text{Uniform}(0.5,\,1) and H∼Beta​(1, 9)H\sim\text{Beta}(1,\,9), respectively, to generate two corresponding training/test datasets of the same size as shown in Section [4.1](https://arxiv.org/html/2512.15088v1#S4.SS1 "4.1 Data generation and implementation details ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), and all these paths are simulated with 500500 steps.
The first dataset consists of fOU paths with varying values of α,μ,σ\alpha,\,\mu,\,\sigma and HH, while the second dataset contains rHeston paths with varying κ1,κ2,θ\kappa\_{1},\,\kappa\_{2},\,\theta and HH.
All other settings remain the same as in Section [4.1](https://arxiv.org/html/2512.15088v1#S4.SS1 "4.1 Data generation and implementation details ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").

Table 5: Distributions for sampling parameters.

|  |  |
| --- | --- |
| Parameters | Distributions |
| α\alpha | Uniform​(0, 5)\text{Uniform}(0,\,5) |
| μ\mu | Uniform​(0, 0.5)\text{Uniform}(0,\,0.5) |
| σ\sigma | Uniform​(0, 3)\text{Uniform}(0,\,3) |
| κ1\kappa\_{1} | Uniform​(0, 5)\text{Uniform}(0,\,5) |
| κ2\kappa\_{2} | Uniform​(0, 3)\text{Uniform}(0,\,3) |
| θ\theta | Uniform​(0, 0.5)\text{Uniform}(0,\,0.5) |

#### 4.4.2 Numerical results

We perform two different multiple-parameter estimation experiments: the first involves simultaneous estimation of four parameters H,α,μH,\,\alpha,\,\mu and θ\theta for the fOU process, and the second involves simultaneous estimation of H,κ1,κ2H,\,\kappa\_{1},\,\kappa\_{2} and θ\theta for the rHeston process.
These two experiments represent joint estimation under conditions of long-range dependence and extreme roughness, respectively.
For the sake of exposition, we report the average RMSE999Let {(xi,yi)i=1,…,n:xi,yi∈ℝd}\{(x\_{i},y\_{i})\_{i=1,\ldots,n}:x\_{i},y\_{i}\in\mathbb{R}^{d}\} be a dataset of nn samples, each with dd features. The average RMSE is then defined as 1d​1n​∑i=1n‖xi−yi‖22\frac{1}{d}\sqrt{\frac{1}{n}\sum\limits\_{i=1}^{n}\|x\_{i}-y\_{i}\|\_{2}^{2}}, where ∥⋅∥2\|\cdot\|\_{2} denotes the Euclidean norm. for all parameters combined, rather than presenting the individual RMSE values for each parameter.
Furthermore, to compare the robustness of these models, we also compute the ranked average root squared error (RSE)101010Similarly, the average RSE of each sample is defined as 1d​‖xi−yi‖2\frac{1}{d}\|x\_{i}-y\_{i}\|\_{2} for i=1,…,ni=1,\ldots,n. on the test dataset samples, presenting the maximum, 75%75\% quantiles and 25%25\% quantiles of the ranked average RSE for all parameters.
All the results are shown in Table [6](https://arxiv.org/html/2512.15088v1#S4.T6 "Table 6 ‣ 4.4.2 Numerical results ‣ 4.4 Joint multi-parameter estimation ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").

In both multiple-parameter estimation problems, the SigMA model achieves the best average RMSE with relatively fewer model parameters.
Notably, the DeepSigNet exhibits an abnormally large maximum average RSE in estimating the fOU process, indicating the presence of outliers.
This suggests that the model may have difficulty handling certain extreme cases in the data, leading to greater result variability.
By contrast, the SigMA model exhibits superior consistency across all percentiles, demonstrating its enhanced robustness and reduced risk of overfitting in diverse scenarios.

Moreover, Figure [5](https://arxiv.org/html/2512.15088v1#S4.F5 "Figure 5 ‣ 4.4.2 Numerical results ‣ 4.4 Joint multi-parameter estimation ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") presents the distribution of the average RSEs’ probability density, providing an overview of the errors.
The higher peak of the SigMA model’s probability density function (PDF) indicates a more concentrated error distribution, demonstrating greater robustness than competing models.
Additionally, the leftward shift of the PDF peak suggests that SigMA attains a smaller median error relative to the other models.
However, the DeepSigNet, which also employs a signature transform, exhibits considerable instability and low accuracy in estimating the fOU.
This demonstrates that the additional structure of the SigMA effectively enhances the stability and accuracy of joint estimations.
Ultimately, the SigMA model achieves these superior results while using significantly fewer parameters than the Transformer, LSTM and CNN model, making it an appealing choice for problems where computational efficiency and model simplicity are crucial.

![Refer to caption](x12.png)


(a) fOU

![Refer to caption](x13.png)


(b) rHeston

Figure 5: Probability density distribution of average RSEs for multiple parameters estimation across stochastic processes with length 500, obtained using various NN models, are based on 1010 training runs.




Table 6: Test results for multiple parameters estimation across stochastic processes with length 500, obtained using various NN models, are based on 1010 training runs. Here, beyond the average RMSEs for all samples, we also rank the average RSEs for every samples in test data set and present the maximum, 75%75\% quantiles and 25%25\% quantiles, respectively. The best accuracies across different NN models are in bold and models are sorted by ascending average RMSEs.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Models | Stochastic processes | Average RMSEs | Average RSEs | | | #\#Params |
| max | q75% | q25% |
| SigMA | fOU | 0.416 | 1.360 | 0.399 | 0.207 | 87341 |
| Transformer | 0.436 | 3.830 | 0.408 | 0.208 | 2558005 |
| CNN | 0.489 | 1.388 | 0.506 | 0.275 | 501220 |
| LSTM | 0.594 | 2.369 | 0.598 | 0.278 | 8383299 |
| DeepSigNet | 0.855 | 21.757 | 0.545 | 0.298 | 9360 |
| SigMA | rHeston | 0.391 | 1.286 | 0.402 | 0.161 | 87341 |
| DeepSigNet | 0.398 | 1.332 | 0.415 | 0.164 | 9360 |
| Transformer | 0.406 | 1.258 | 0.413 | 0.168 | 2558005 |
| CNN | 0.499 | 1.061 | 0.525 | 0.247 | 501220 |
| LSTM | 0.612 | 1.691 | 0.634 | 0.312 | 8383299 |

### 4.5 Empirical applications on real-world datasets

#### 4.5.1 Calibration to equity-index realized volatility

All the previous examples are based on simulated paths, in this example, we follow [stone2020calibrating] to calibrate the Ho¨\ddot{\rm o}lder (Hurst) exponent of historic realized volatility data from the Oxford–Man Institute of Quantitative Finance.
Since the log-volatility behaves essentially as a fBm with the Hurst exponent HH of order 0.10.1 (see [gatheral2018volatility]), we generate the training and evaluation datasets using the rHeston process with H∼Beta​(1, 9)H\sim\text{Beta}(1,\,9), and set the sequence length to 100100, as illustrated in Section [4.1](https://arxiv.org/html/2512.15088v1#S4.SS1 "4.1 Data generation and implementation details ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").
We take a sample of 1010 different indices; for each index we then used a time series of 200200 sequential data points to create 1111 vectors of length 100100 (entries 11 to 100100, 1111 to 110110 and so on) to predict the Ho¨\ddot{\rm o}lder exponent for each index.
We compute the RMSE between the models’ predictions and the least squares prediction, and the standard deviation of the difference between these predictions, see Table [7](https://arxiv.org/html/2512.15088v1#S4.T7 "Table 7 ‣ 4.5.1 Calibration to equity-index realized volatility ‣ 4.5 Empirical applications on real-world datasets ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"). The SigMA model achieves the lowest RMSE and a favorable standard deviation among all models, while maintaining a reasonable level of model complexity. By contrast, although other models also show reasonable accuracy, they either require much more parameters or exhibit higher errors and standard deviations, indicating a trade-off between complexity and performance.
Therefore, we can state that the SigMA model is precise enough to be used in practice, offering an efficient and reliable solution for real-world applications.

Table 7: Ho¨\ddot{\rm o}lder exponent estimation results for historic realized volatility data, obtained using various NN models. The best results across different NN models are in bold and models are sorted by ascending RMSEs.

|  |  |  |  |
| --- | --- | --- | --- |
| Models | Errors | | #\#Params |
| RMSE | Std. |
| SigMA | 1.75e-2 | 3.07e-4 | 87226 |
| Transformer | 2.05e-2 | 2.59e-4 | 573906 |
| DeepSigNet | 3.48e-2 | 6.17e-4 | 9261 |
| LSTM | 3.66e-2 | 9.77e-4 | 1829634 |
| CNN | 6.97e-2 | 2.54e-3 | 255073 |

#### 4.5.2 Application to Li-ion battery degradation

In this example, we consider the degradation of Li-ion batteries over charge-discharge cycles using capacity loss data from the NASA Prognostics Center of Excellence (PCoE) repository.111111<https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/> We present the obtained series data in Figure [6](https://arxiv.org/html/2512.15088v1#S4.F6 "Figure 6 ‣ 4.5.2 Application to Li-ion battery degradation ‣ 4.5 Empirical applications on real-world datasets ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs").

![Refer to caption](x14.png)


Figure 6: Capacity losses caused by structural degradation of Li-ion batteries.

In order to quantify the long-range dependence in the degradation dynamics, we use the Higuchi method
and the rescaled range (R/S) analysis for statistical benchmarks [csanady2024parameter].
Similar to Section [4.5.1](https://arxiv.org/html/2512.15088v1#S4.SS5.SSS1 "4.5.1 Calibration to equity-index realized volatility ‣ 4.5 Empirical applications on real-world datasets ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"), we use the series data of the battery capacity proportion to create 4646 vectors of length 100100-cycles (entries 0-cycle to 9999-cycle, 1010-cycle to 109109-cycle and so on) to predict the Hurst parameter.

The degradation series in Figure [6](https://arxiv.org/html/2512.15088v1#S4.F6 "Figure 6 ‣ 4.5.2 Application to Li-ion battery degradation ‣ 4.5 Empirical applications on real-world datasets ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") exhibits a global downward trend, local step-changes, and several regime shifts.
Such behaviour violates the stationarity and self-similarity assumptions that underlie classical Hurst-exponent analysis.
Consequently, the H-values reported in Table [8](https://arxiv.org/html/2512.15088v1#S4.T8 "Table 8 ‣ 4.5.2 Application to Li-ion battery degradation ‣ 4.5 Empirical applications on real-world datasets ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") and Figure [7](https://arxiv.org/html/2512.15088v1#S4.F7 "Figure 7 ‣ 4.5.2 Application to Li-ion battery degradation ‣ 4.5 Empirical applications on real-world datasets ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") should be interpreted as local indicators of persistent path memory rather than as true Hurst exponents in the sense of fractional Brownian motion.

The Higuchi method yields a mean value of 0.83300.8330, while the R/S analysis resulted in 0.95980.9598, indicating persistent long-memory behavior in the degradation process.

Assuming the series data of the battery capacity proportion follows fBm, based on the obtained data series, we employ the neural networks trained by the fBm paths with H∼Uniform​(0,1)H\sim\text{Uniform}(0,1) to estimate its Hurst parameter.
The results, together with statistical benchmarks, are shown in Table [8](https://arxiv.org/html/2512.15088v1#S4.T8 "Table 8 ‣ 4.5.2 Application to Li-ion battery degradation ‣ 4.5 Empirical applications on real-world datasets ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs") and Figure [7](https://arxiv.org/html/2512.15088v1#S4.F7 "Figure 7 ‣ 4.5.2 Application to Li-ion battery degradation ‣ 4.5 Empirical applications on real-world datasets ‣ 4 Numerical and empirical experiments ‣ SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs"). The closest result to the R/S benchmark (0.9598) is from the SigMA (0.9239), while the closest result to Higuchi benchmark (0.8330) is from the DeepSigNet (0.8712). The results from LSTM and CNN exhibit significant deviations from both statistical benchmarks.

Across sliding windows of 100 cycles (with 90-cycle overlap), SigMA and DeepSigNet provide stable and relatively smooth estimates, consistently ranging between the Higuchi and R/S values. This behaviour is expected as:

* •

  the R/S method is well-known to overestimate H in the presence of linear or slowly varying trends, which explains the values close to 1 observed here;
* •

  the Higuchi estimator, while less trend-sensitive, exhibits substantial fluctuations on short windows and irregular signals;
* •

  by contrast, the signature-based ML models primarily exploit the structure of local increments and are therefore less affected by non-stationarity and short-window artifacts than classical methods.

Among neural architectures, LSTM and CNN produce highly variable estimates with large cycle-to-cycle jumps, whereas SigMA and DeepSigNet yield the most stable behaviour.
The Transformer baseline tends to underestimate H and remains almost flat, likely reflecting its tendency to average over the strong underlying trend.
It is important to note that the choice of window length and overlap materially affects all estimators: using 100-cycle windows provides limited scaling information, and the 90% overlap induces high autocorrelation between adjacent estimates.
Longer or multiscale windows, or detrended fluctuation methods, could improve interpretability and robustness but fall outside the present scope.
Nevertheless, the results demonstrate that signature-based learning, in particular SIGMA, captures persistent path memory properties of degradation trajectories more faithfully than conventional deep learning models.

Table 8: Hurst estimation results for the battery capacity proportion series from NN models and statistical benchmarks (in bold), sorted by ascending H-value.

|  |  |  |  |
| --- | --- | --- | --- |
| Models/Methods | H-estimates | 95% confidence intervals | #\#Params |
| LSTM | 0.3779 | (0.3373, 0.4183) | 1829634 |
| CNN | 0.6151 | (0.6129, 0.6172) | 255073 |
| Transformer | 0.7425 | (0.7414, 0.7434) | 573906 |
| Higuchi | 0.8330 | (0.8120, 0.8539) | - |
| DeepSigNet | 0.8712 | (0.8704, 0.8720) | 9261 |
| SigMA | 0.9239 | (0.9224, 0.9252) | 87226 |
| R/S | 0.9598 | (0.9460, 0.9735) | - |

![Refer to caption](x15.png)


Figure 7: Hurst exponent estimates for battery capacity degradation series (50 to 500 cycles), obtained from NN models and statistical benchmarks. Results are based on 100-cycle sliding windows with 90-cycle overlap.

## 5 Conclusion

In this work, we proposed SigMA (Signature Multi-head Attention), a neural architecture for parameter estimation in stochastic differential equations driven by fractional Brownian motion. Motivated by the non-Markovian and non-semimartingale nature of fBm-driven models, which limits the applicability of classical inference techniques, SigMA combines path signature representations with multi-head self-attention, complemented by convolutional preprocessing and multilayer perceptron components. This design explicitly targets the extraction of informative, path-level features while maintaining a compact and scalable model structure.

Through extensive numerical experiments, we demonstrated that SigMA achieves consistently strong performance across a range of estimation tasks, including Hurst parameter estimation and joint multi-parameter inference for fBm, fractional Ornstein–Uhlenbeck, and rough Heston models. In particular, the integration of signature transforms enables SigMA to decouple model complexity from input path length, while the attention mechanism effectively aggregates information across signature levels. Sensitivity and ablation studies further confirmed that the convolutional and MLP components play an important role in improving both accuracy and training stability. Across all synthetic benchmarks, SigMA outperformed CNN, LSTM, vanilla Transformer, and Deep Signature baselines in terms of accuracy, robustness, and parameter efficiency.

The empirical case studies further highlight the practical relevance of the proposed approach. In the calibration of equity-index realized volatility, SigMA provided accurate and stable estimates of the Hurst (Hölder) exponent with significantly lower model complexity than competing architectures. In the analysis of Li-ion battery degradation data, SigMA captured persistent long-memory effects more reliably than conventional deep learning models, producing stable estimates that align well with classical statistical benchmarks while being less sensitive to non-stationarity and short-window artifacts.

From a broader perspective, this work illustrates how signature-based representations and attention mechanisms can be effectively combined for parameter inference in non-Markovian stochastic systems. While our focus has been on fBm-driven models, the methodology is not tied to a specific stochastic process and may be extended to other classes of path-dependent dynamics.

A number of potential directions for future research arise from this work. In particular, extending the proposed framework to multivariate and coupled stochastic systems would be of interest, especially in high-dimensional finance and engineering applications. In addition, incorporating uncertainty quantification such as predictive intervals or Bayesian variants of SigMA could enhance interpretability.

##### Code and Data Availability

The code used in this work is publicly available [[GitHub link]](https://github.com/changanluoxue/SigMA.git).

## Appendix A Architectural details of baseline and signature-based neural networks

This appendix provides detailed descriptions of all neural network architectures used throughout the numerical experiments, including both baseline benchmark models (CNN, LSTM, Transformer, DeepSigNet) and the proposed signature-based variants (SigMA’s ablations).

* •

  The architecture of CNN model:

  + -

    a convolutional layer with 32 channels and kernel size 20;
  + -

    the leaky ReLu transform with negative slope 0.1;
  + -

    a max pooling layer with size 3;
  + -

    a dropout layer with rate 0.25;
  + -

    a convolutional layer with 64 channels and kernel size 20;
  + -

    the leaky ReLu transform with negative slope 0.3;
  + -

    a max pooling layer with size 3;
  + -

    a dropout layer with rate 0.25;
  + -

    a convolutional layer with 128 channels and kernel size 20;
  + -

    the leaky ReLu transform with negative slope 0.1;
  + -

    a max pooling layer with size 3;
  + -

    a dropout layer with rate 0.4;
  + -

    a dense layer with 128 units;
  + -

    the leaky ReLu transform with negative slope 0.1;
  + -

    a dropout layer with rate 0.3;
  + -

    a dense layer with 1 units;
  + -

    a non-linear transform with sigmoid function.
* •

  The architecture of DeepSigNet model:

  + -

    a convolutional layer with 3 channels and kernel size 3;
  + -

    augmentation with time and original values;
  + -

    a signature transform with truncation order N=3N=3;
  + -

    a fully connected feedforward neural network with 5 hidden layers, each of size 32 and ReLU activation;
  + -

    a non-linear transform with sigmoid function.
* •

  The architecture of Transformer model:

  + -

    a convolutional layer with 153 channels and kernel size 3;
  + -

    augmentation with time and original values;
  + -

    a multi-head self-attention layer with the number of heads h=N=3h=N=3;
  + -

    a fully connected feedforward neural network with 5 hidden layers, each of size 32 and ReLU activation;
  + -

    a non-linear transform with sigmoid function.
* •

  The architecture of LSTM model:

  + -

    a standardizing layer to transform the sequence to its increments;
  + -

    a standardization on the increments;
  + -

    a two-layer stacked LSTM with 128 hidden units per layer;
  + -

    a fully connected feedforward neural network with 2 hidden layers of sizes 128 and 64, and PReLU activation.

* •

  The architecture of SigSA model:

  + -

    augmentation with time;
  + -

    a signature transform with truncation order N=3N=3;
  + -

    a single-head self-attention layer;
  + -

    a non-linear transform with sigmoid function.
* •

  The architecture of SigMA without convolutional layer:

  + -

    augmented with time;
  + -

    taking the signature transform with truncation order N=3N=3;
  + -

    the multi-head self-attention layer with the number of heads h=N=3h=N=3 and each different head corresponds to a different signature level;
  + -

    a fully connected feedforward neural network with 5 hidden layers, each of size 32 and ReLU activation;
  + -

    a non-linear transform with sigmoid function.
* •

  The architecture of SigMA without MLP:

  + -

    a convolutional layer with 3 channels and kernel size 3;
  + -

    augmentation with time and original values;
  + -

    a signature transform with truncation order N=3N=3;
  + -

    a multi-head self-attention layer with the number of heads h=N=3h=N=3 and each different head corresponds to a different signature level;
  + -

    a linear transform to appropriate dimension.
* •

  The architecture of SigMA without convolutional layer & MLP:

  + -

    augmentation with time;
  + -

    a signature transform with truncation order N=3N=3;
  + -

    a multi-head self-attention layer with the number of heads h=N=3h=N=3 and each different head corresponds to a different signature level;
  + -

    a linear transform to appropriate dimension.