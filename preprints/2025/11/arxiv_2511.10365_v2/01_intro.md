---
authors:
- Yilong Zeng
- Boyan Tang
- Xuanhao Ren
- Sherry Zhefang Zhou
- Jianghua Wu
- Raymond Lee
doc_id: arxiv:2511.10365v2
family_id: arxiv:2511.10365
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting'
url_abs: http://arxiv.org/abs/2511.10365v2
url_html: https://arxiv.org/html/2511.10365v2
venue: arXiv q-fin
version: 2
year: 2025
---


Yilong Zeng

Boyan Tang

Xuanhao Ren

Sherry Zhefang Zhou
[sherryzhou@uic.edu.cn](mailto:sherryzhou@uic.edu.cn)

Jianghua Wu

Raymond Lee
[raymondshtlee@uic.edu.cn](mailto:raymondshtlee@uic.edu.cn)

###### Abstract

This paper introduces the Fractal-Chaotic Oscillation Co-driven (FCOC) framework, a novel paradigm for financial volatility forecasting that systematically resolves the dual challenges of feature fidelity and model responsiveness. FCOC synergizes two core innovations: our novel Fractal Feature Corrector (FFC), engineered to extract high-fidelity fractal signals, and a bio-inspired Chaotic Oscillation Component (COC) that replaces static activations with a dynamic processing system. Empirically validated on the S&P 500 and DJI, the FCOC framework demonstrates profound and generalizable impact. The framework fundamentally transforms the performance of previously underperforming architectures, such as the Transformer, while achieving substantial improvements in key risk-sensitive metrics for state-of-the-art models like Mamba. These results establish a powerful co-driven approach, where models are guided by superior theoretical features and powered by dynamic internal processors, setting a new benchmark for risk-aware forecasting.

###### keywords:

Volatility Forecasting , Intelligent Systems , Deep Learning , Multifractal Analysis , Chaotic Activation Function

††journal: Information Sciences

\affiliation

[1]organization=Faculty of Science and Technology, Beijing Normal-Hong Kong Baptist University,
city=Zhuhai,
postcode=519087,
country=China
\affiliation[2]organization=Guangdong Provincial Key Laboratory of Interdisciplinary Research and Application for Data Science, Beijing Normal-Hong Kong Baptist University,
city=Zhuhai,
postcode=519087,
country=China
\affiliation[3]organization=The Shenzhen Research Institute of Big Data, The Chinese University of Hong Kong, Shenzhen,
city=Shenzhen,
postcode=518000,
country=China

{highlights}

Proposes a novel FCOC framework to resolve dual bottlenecks in volatility forecasting.

Introduces a Fractal Feature Corrector (FFC) for high-fidelity market signals.

Deploys a Chaotic Oscillation Component (COC) to resolve model complexity mismatch.

Establishes a co-driven paradigm synergizing fractal features and chaotic dynamics.

## 1 Introduction

The forecasting of financial market volatility, as the second moment of asset returns, is a cornerstone of modern finance, crucial for risk management, option pricing, and portfolio allocation [taylor2011asset]. While deep learning methods have shown immense potential in this domain due to their powerful nonlinear pattern recognition capabilities [kim2018forecasting, liu2019novel], their full potential remains constrained by two fundamental and often-overlooked bottlenecks in the standard modeling pipeline.

The first bottleneck is feature fidelity. Financial time series, as typical complex systems, possess an intrinsic structure that traditional statistical features cannot fully capture. The Fractal Market Hypothesis (FMH) from econophysics [peters1994fractal] points out that long-range memory and multifractal properties are key dynamical characteristics of the market. This makes fractal analysis a powerful and theoretically grounded tool for our investigation. However, the application of these advanced tools faces significant limitations. First, their analytical framework is often limited to a single time series, largely failing to consider the cross-asset risk transmission mechanisms, thus ignoring the asymmetric cross-correlation phenomenon that is at the core of systemic risk [longin2001extreme, ang2002asymmetric, ding2011asymmetric]. Second, the standard implementation of these methods has inherent instability, is prone to introducing spurious noise, and thus harms the fidelity of the extracted features [bashan2008comparison]. These two problems together lead to a situation where the input information the model relies on is, at its source, a distorted representation of the market’s true state.

The second, and more fundamental, bottleneck lies in model responsiveness. The core processing units widely adopted in deep learning models—static activation functions such as ReLU—reveal their inherent design limitations when processing highly dynamic and non-stationary financial signals. This limitation stems from a complexity mismatch [wang2021chaotic]: a simple, fixed-logic processor is used to analyze an essentially chaotic and dynamic complex signal. This bottleneck means that even with perfect input features, the model’s rigid internal processing mechanism cannot provide an effective dynamic response, ultimately leading to information decay and loss during internal transmission [lee2019chaotic].

In fact, these two bottlenecks are not mutually independent; they are two facets of the same underlying challenge posed by chaotic systems. In nonlinear dynamics, the long-term behavior of a chaotic system is governed by a strange attractor, which possesses an intricate fractal geometry. From this perspective, the challenge of feature fidelity is about accurately quantifying the geometric properties (i.e., the multifractal spectrum) of the market’s underlying strange attractor. The challenge of model responsiveness, in turn, is about having an internal processor that can dynamically react to this geometric information. This intrinsic link between chaos and fractals provides the theoretical backbone for our proposed solution.

To systematically address these two theoretically unified challenges, this paper proposes the Fractal-Chaotic Oscillation Co-driven (FCOC) framework, a novel paradigm for volatility forecasting. The FCOC framework is built upon two synergistic innovative pillars:

* 1.

  A Fractal Feature Corrector (FFC), designed to provide a high-fidelity market complexity metric by capturing systemic asymmetric cross-correlations and rectifying the stability deficiencies of standard fractal analysis.
* 2.

  A Chaotic Oscillation Component (COC), which replaces static activation functions with a bio-inspired dynamic system to resolve the critical complexity mismatch within the model.

The core contributions of this study can be summarized as follows:

* 1.

  We propose the FCOC, a new framework that systematically addresses the dual bottlenecks at both the feature level and the model level in financial forecasting.
* 2.

  We introduce the FFC, centered on a robust OSW-MF-ADCCA implementation, which significantly improves the stability and fidelity of multifractal feature extraction.
* 3.

  We deploy the COC, a dynamic activation system which, through a systematic exploration of the parameter space, includes two novel configurations (T9 and T10) proposed to adapt to financial dynamics.
* 4.

  Through systematic empirical analysis, we demonstrate that the co-driven synergy between FFC and COC achieves significant performance gains over a range of benchmark models and establishes a new design philosophy for intelligent systems in complex financial environments.

The remainder of this paper is structured as follows. Section [2](https://arxiv.org/html/2511.10365v2#S2 "2 Related Work ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting") reviews the related work. Section [3](https://arxiv.org/html/2511.10365v2#S3 "3 The FCOC Framework and Methodology ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting") provides a detailed exposition of the FCOC framework’s methodology. Section [4](https://arxiv.org/html/2511.10365v2#S4 "4 Problem Formulation and Experiments ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting") outlines the problem formulation and the experimental setup. Section [5](https://arxiv.org/html/2511.10365v2#S5 "5 Empirical Analysis ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting") presents the empirical results and provides an in-depth discussion of the findings. Finally, Section [6](https://arxiv.org/html/2511.10365v2#S6 "6 Conclusion ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting") concludes the paper.

## 2 Related Work

Our research is situated at the intersection of deep learning for finance, econophysics, and computational neuroscience.

### 2.1 Deep Learning Models for Financial Time Series Forecasting

Modern financial forecasting methods have widely adopted deep learning architectures. Recurrent Neural Networks (RNNs), particularly Long Short-Term Memory (LSTM) [kim2018forecasting, liu2019novel] and Gated Recurrent Units (GRU) [chen2019forecasting], are commonly used for their ability to handle temporal dependencies. In recent years, more advanced architectures such as the Transformer [vaswani2017attention] and state-space models like Mamba have also been explored. For instance, Lu and Xu [lu2024trnn] proposed an efficient Time-series Recurrent Neural Network (TRNN) to improve training efficiency. Chen et al. [chen2024improved] developed a hybrid model combining a Temporal Convolutional Network (TCN) with BiGRU for new energy stock index forecasting. While these works have made significant progress in model architecture, they almost universally rely on traditional static activation functions, thus failing to fundamentally address the internal model responsiveness problem.

### 2.2 Multifractal Analysis of Financial Time Series

To overcome the informational limitations of raw time series, a more theoretically profound approach originates from econophysics. This discipline aims to uncover the intrinsic physical laws of the market, with the multifractal nature of financial time series being a key insight that reveals the non-uniformity of volatility across different time scales [kantelhardt2002multifractal].

In response, econophysics has developed an evolving toolkit of methods, progressing from Detrended Fluctuation Analysis (DFA) [peters1994fractal] to Multifractal DFA (MF-DFA) [kantelhardt2002multifractal]. A significant advance came with the recognition of market asymmetry, leading to Asymmetric MF-DFA (A-MFDFA) [lee2017asymmetric, lee2018asymmetric]. However, these methods were long confined to single-asset analysis, overlooking the systemic interactions of the market as a whole. In fact, asymmetric cross-correlations between different assets are a key driver of systemic market risk, especially during downturns [longin2001extreme, ang2002asymmetric, ding2011asymmetric]. Recent work has continued to validate this, with Yu et al. [yu2022novel] successfully combining multifractal analysis with GRU networks and Wang and Lee [wang2023stock] applying modified MF-ADCCA to forecast stock index volatility. Although subsequent research began to address cross-correlations with more complex techniques, they commonly inherited a persistent technical flaw from earlier methods: the use of non-overlapping segmentation, which has been shown to introduce spurious fluctuations and compromise the stability of fractal measurements [bashan2008comparison]. Our Fractal Feature Corrector (FFC) is designed to solve both of these historical problems simultaneously. By using Multifractal Asymmetric Detrended Cross-Correlation Analysis (MF-ADCCA) [cao2014detrended] as its core to capture systemic interactions, and employing a robust Overlapping Sliding Window (OSW) implementation to correct for instability [tang2019research], the FFC aims to provide a more reliable and higher-fidelity set of complexity features than previously available.

### 2.3 Dynamic and Chaotic Activation Functions

The concept of enhancing neural networks with internal dynamic components originates from computational neuroscience. Unlike standard neural networks, the biological brain is believed to operate based on continuous and chaotic neural oscillations [freeman2000neurodynamics]. Inspired by this, academia has begun to explore replacing static activation functions with dynamic systems [wang2021chaotic]. This direction also aligns with cutting-edge paradigms in econophysics, which posit that financial markets can be viewed as a dynamic energy field where assets behave like interacting, chaotic oscillators. From this perspective, an oscillator with excitatory and inhibitory mechanisms is not merely a computational tool but a physical analogy for the fundamental push-pull dynamics of market forces.

Therefore, our adoption of the Chaotic Oscillation Component (COC) is dually motivated: computationally, it solves the complexity mismatch problem; physically, it provides a more plausible model for the phenomena we aim to forecast. Our COC is built upon the foundational work on the Lee oscillator [lee2004transient]. While generative models like the VAR-VAE proposed by Leushuis [leushuis2025probabilistic] have started to incorporate probabilistic dynamics in latent spaces, our work focuses on a different, complementary goal: embedding dynamics directly into the neuron’s fundamental activation process. Our core contribution in this area is not only the systematic application of this concept to financial volatility forecasting but also the engineering of two novel oscillator configurations (T9 and T10) through parameter space exploration, specifically to better capture the unique dynamics of financial markets, such as abrupt regime switching.

## 3 The FCOC Framework and Methodology

The proposed FCOC framework addresses the dual challenges of robust feature extraction and dynamic model responsiveness. The overall architecture of the framework is depicted in Figure [1](https://arxiv.org/html/2511.10365v2#S3.F1 "Figure 1 ‣ 3 The FCOC Framework and Methodology ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting"). This section provides a comprehensive technical exposition of the two innovative pillars that constitute the framework. First, we detail the FFC, whose core is our novel OSW-MF-ADCCA algorithm, designed to generate high-fidelity fractal features. Second, we elaborate on the COC, which fundamentally upgrades the network’s internal processing units from static activation functions to a dynamic chaotic system.

![Refer to caption](FCOC_Flowchart.png)


Figure 1: Conceptual Architecture of the FCOC Framework.

### 3.1 Fractal Feature Corrector (FFC)

The Fractal Feature Corrector is designed to address the feature fidelity bottleneck by resolving the two fundamental limitations of prior fractal analyses identified in our introduction: their confinement to single-asset analysis and their inherent measurement instability. At its core is our robust OSW-MF-ADCCA algorithm, a technique that quantifies the asymmetric and multifractal cross-correlations between two non-stationary time series. Its core procedure involves analyzing the cumulative deviation profiles of the series through systematically overlapping sub-intervals. For two time series, rx​(t)r\_{x}(t) and ry​(t)r\_{y}(t) (for t=1,…,Nt=1,\dots,N), the detailed implementation steps are as follows:

Step 1: Profile Construction
  
The cumulative deviation series, denoted as profiles 𝒫x​(k)\mathcal{P}\_{x}(k) and 𝒫y​(k)\mathcal{P}\_{y}(k), are first generated from the original series:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫x​(k)=∑t=1k(rx​(t)−μx),k=1,…,N\mathcal{P}\_{x}(k)=\sum\_{t=1}^{k}(r\_{x}(t)-\mu\_{x}),\quad k=1,\dots,N |  | (1) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫y​(k)=∑t=1k(ry​(t)−μy),k=1,…,N\mathcal{P}\_{y}(k)=\sum\_{t=1}^{k}(r\_{y}(t)-\mu\_{y}),\quad k=1,\dots,N |  | (2) |

where μx\mu\_{x} and μy\mu\_{y} represent the mean values of the entire series rxr\_{x} and ryr\_{y}, respectively. To facilitate the asymmetry analysis, the primary market return series, rx​(t)r\_{x}(t), is designated as the proxy for the local market trend.

Step 2: Overlapping Segmentation
  
The profiles are partitioned into segments of length ss using a sliding window. The window advances with a stride of ss​t​e​ps\_{step}, which is governed by an overlap ratio ρ\rho (0≤ρ<10\leq\rho<1):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ss​t​e​p=⌊s⋅(1−ρ)+0.5⌋s\_{step}=\lfloor s\cdot(1-\rho)+0.5\rfloor |  | (3) |

This process yields Ns​e​g=⌊(N−s)/ss​t​e​p⌋+1N\_{seg}=\lfloor(N-s)/s\_{step}\rfloor+1 overlapping segments. In this work, an overlap ratio of ρ=1/3\rho=1/3 is used, a choice that strikes a balance between enhancing statistical stability and maintaining computational efficiency, consistent with practices in related studies [tang2019research].

Step 3: Local Detrending and Trend Discrimination
  
For each segment jj (j=1,…,Ns​e​gj=1,\dots,N\_{seg}), a polynomial of order m=2m=2 is fitted to remove the local trend. The choice of a quadratic polynomial (m=2m=2) offers a robust balance, effectively removing complex non-linear local trends common in financial series without overfitting to short-term noise. Let px(j)​(i)p\_{x}^{(j)}(i) and py(j)​(i)p\_{y}^{(j)}(i) be the polynomial fits for the segment. The local detrended fluctuation, Fs​e​g2​(s,j)F^{2}\_{seg}(s,j), is calculated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fs​e​g2​(s,j)=1s​∑i=1s|(𝒫x​(i)−px(j)​(i))⋅(𝒫y​(i)−py(j)​(i))|F^{2}\_{seg}(s,j)=\frac{1}{s}\sum\_{i=1}^{s}|(\mathcal{P}\_{x}(i)-p\_{x}^{(j)}(i))\cdot(\mathcal{P}\_{y}(i)-p\_{y}^{(j)}(i))| |  | (4) |

Within the same segment, the slope of a linear fit to the index proxy series, denoted as βj\beta\_{j}, is used to identify the trend’s direction. A positive trend corresponds to βj>0\beta\_{j}>0, and a negative trend otherwise.

Step 4: Directional qq-order Fluctuation Functions
  
Fluctuation functions are then computed by averaging over segments with positive and negative trends separately. For a given order qq, these directional functions are defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fq+​(s)=[1Np​o​s​∑j=1Ns​e​g1+sgn​(βj)2​[Fs​e​g2​(s,j)]q/2]1/qF\_{q}^{+}(s)=\left[\frac{1}{N\_{pos}}\sum\_{j=1}^{N\_{seg}}\frac{1+\text{sgn}(\beta\_{j})}{2}[F^{2}\_{seg}(s,j)]^{q/2}\right]^{1/q} |  | (5) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fq−​(s)=[1Nn​e​g​∑j=1Ns​e​g1−sgn​(βj)2​[Fs​e​g2​(s,j)]q/2]1/qF\_{q}^{-}(s)=\left[\frac{1}{N\_{neg}}\sum\_{j=1}^{N\_{seg}}\frac{1-\text{sgn}(\beta\_{j})}{2}[F^{2}\_{seg}(s,j)]^{q/2}\right]^{1/q} |  | (6) |

where Np​o​sN\_{pos} and Nn​e​gN\_{neg} are the total counts of segments with positive and negative trends, respectively. The separation is achieved using the sign function, sgn​(βj)\text{sgn}(\beta\_{j}), which returns +1+1 for a positive local trend slope (βj>0\beta\_{j}>0), −1-1 for a negative slope, and 0 otherwise. This makes the term (1+sgn​(βj))/2(1+\text{sgn}(\beta\_{j}))/2 an indicator that equals 11 only for positive-trend segments, while (1−sgn​(βj))/2(1-\text{sgn}(\beta\_{j}))/2 acts as an indicator for negative-trend segments. For the special case of q=0q=0, the averaging is performed in the logarithmic domain to avoid singularities. The fluctuation function is calculated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F0​(s)=exp⁡(12​Ns​e​g​∑j=1Ns​e​gln⁡[Fs​e​g2​(s,j)])F\_{0}(s)=\exp\left(\frac{1}{2N\_{seg}}\sum\_{j=1}^{N\_{seg}}\ln[F^{2}\_{seg}(s,j)]\right) |  | (7) |

with analogous definitions for the directional cases F0+​(s)F\_{0}^{+}(s) and F0−​(s)F\_{0}^{-}(s) by applying the respective indicator functions within the summation.

Step 5: Estimation of Generalized Hurst Exponents
  
The existence of long-range power-law cross-correlations is indicated if the fluctuation functions scale with the segment size ss as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fq​(s)∝sH​(q);Fq+​(s)∝sH+​(q);Fq−​(s)∝sH−​(q)F\_{q}(s)\propto s^{H(q)};\quad F\_{q}^{+}(s)\propto s^{H^{+}(q)};\quad F\_{q}^{-}(s)\propto s^{H^{-}(q)} |  | (8) |

where the exponents H​(q)H(q), H+​(q)H^{+}(q), and H−​(q)H^{-}(q) are the generalized Hurst exponents. They are determined from the slope of a log-log plot of the fluctuation function versus segment size ss. Our analysis focuses on the case of q=2q=2. This choice is standard in the econophysics literature for analyzing volatility persistence, as it directly relates to the second moment (variance) of the fluctuations and provides a measure analogous to the classical Hurst exponent for long-range correlations [kantelhardt2002multifractal, podobnik2008detrended]. Here, H​(2)>0.5H(2)>0.5 suggests persistent cross-correlations and H​(2)<0.5H(2)<0.5 suggests anti-persistent cross-correlations.

Step 6: Rolling Window Feature Generation
  
To capture the temporal dynamics of market correlations, the Hurst exponents are calculated not once, but continuously over time. A rolling-window approach is implemented, where the exponent is calculated for each day using data from the preceding TT days. This methodology generates time-varying feature vectors. The entire procedure is formalized in Algorithm [1](https://arxiv.org/html/2511.10365v2#alg1 "Algorithm 1 ‣ 3.1 Fractal Feature Corrector (FFC) ‣ 3 The FCOC Framework and Methodology ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting").

Algorithm 1  Rolling Window Feature Generation via OSW-MF-ADCCA

1:

2:Primary time series rXr\_{X} of length NN

3:Secondary time series rYr\_{Y} of length NN

4:Rolling window size TT

5:Step size for window sliding kk

6:Overlap ratio ρ\rho

7:

8:Hurst exponent series ℋo​v​e​r​a​l​l,ℋp​o​s​i​t​i​v​e,ℋn​e​g​a​t​i​v​e\mathcal{H}\_{overall},\mathcal{H}\_{positive},\mathcal{H}\_{negative}

9:

10:function Generate\_Hurst\_Features(rX,rY,T,k,ρr\_{X},r\_{Y},T,k,\rho)

11:  Initialize ℋa​l​l,ℋp​o​s,ℋn​e​g←empty lists\mathcal{H}\_{all},\mathcal{H}\_{pos},\mathcal{H}\_{neg}\leftarrow\text{empty lists}

12:  Nw←⌊(N−T)/k⌋+1N\_{w}\leftarrow\lfloor(N-T)/k\rfloor+1 ⊳\triangleright Number of windows

13:  for i=0i=0 to Nw−1N\_{w}-1 do

14:   s​t​a​r​t←i×kstart\leftarrow i\times k

15:   e​n​d←s​t​a​r​t+Tend\leftarrow start+T

16:   sX←rX​[s​t​a​r​t​…​e​n​d]s\_{X}\leftarrow r\_{X}[start\dots end]

17:   sY←rY​[s​t​a​r​t​…​e​n​d]s\_{Y}\leftarrow r\_{Y}[start\dots end]

18:   ⊳\triangleright Calculate exponents for the sub-window

19:   H,H+,H−←Calc\_Hurst(sX,sY,q=2,ρ)H,H^{+},H^{-}\leftarrow\text{Calc\\_Hurst}(s\_{X},s\_{Y},q=2,\rho)

20:   Append HH to ℋa​l​l\mathcal{H}\_{all}

21:   Append H+H^{+} to ℋp​o​s\mathcal{H}\_{pos}

22:   Append H−H^{-} to ℋn​e​g\mathcal{H}\_{neg}

23:  end for

24:  return ℋa​l​l,ℋp​o​s,ℋn​e​g\mathcal{H}\_{all},\mathcal{H}\_{pos},\mathcal{H}\_{neg}

25:end function

### 3.2 Chaotic Oscillation Component (COC)

The second pillar of the FCOC framework, the Chaotic Oscillation Component, addresses a fundamental limitation within deep learning models: the dynamic inertness of conventional activation functions. To overcome this deficiency, we fundamentally upgrade the activation function to a dynamic chaotic micro-system. The process involves two primary stages: first, distilling the complex behavior of multiple oscillators into a library of candidate functions, and second, adaptively selecting from this library to produce a final activation value.

#### 3.2.1 Core Engine: Lee Oscillator with Retrograde Signaling (LORS)

The decision to replace a static activation function with a dynamic oscillator represents a fundamental paradigm shift grounded in both econophysics and neuroscience. Classical neural networks, with their simple neuron models, have been criticized for being far simpler than their biological counterparts. Modern neuroscience reveals that the brain does not operate on a simple feed-forward firing of static units; rather, it functions on a substrate of continuous and chaotic oscillations known as brainwaves [freeman2000neurodynamics]. It is this underlying oscillatory dynamic that gives rise to complex cognitive functions like memory and perception. Inspired by this, we consider that financial markets, as complex adaptive systems driven by collective human behavior, are more faithfully modeled as a field of interacting oscillators than as a system mapped by static functions.

The Lee oscillator, with its design rooted in emulating biologically plausible neural dynamics such as Progressive Memory Recall [lee2006progressive], provides the ideal computational primitive for this paradigm. It allows a system to perform gradual feedback and self-correction when faced with incomplete or noisy inputs through transient chaotic behavior, a mechanism strikingly similar to how market participants adapt to new information. Specifically, this study employs an advanced variant: the Lee Oscillator with Retrograde Signaling. This model enhances the original design [lee2004transient] by incorporating retrograde signaling mechanisms observed in neuroscience [levitan2002neuron, wong2008wind], further boosting its biological plausibility. The neural architecture of the LORS is depicted in Figure [2](https://arxiv.org/html/2511.10365v2#S3.F2 "Figure 2 ‣ 3.2.1 Core Engine: Lee Oscillator with Retrograde Signaling (LORS) ‣ 3.2 Chaotic Oscillation Component (COC) ‣ 3 The FCOC Framework and Methodology ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting").

![Refer to caption](LORS.png)


Figure 2: Neural architecture of the Lee Oscillator with Retrograde Signaling (LORS).

Its dynamic behavior is strictly governed by the following set of equations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(μ;x)\displaystyle f(\mu;x) | =tanh⁡(μ​x)\displaystyle=\tanh(\mu x) |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Et+1\displaystyle E\_{t+1} | =f​(a1​LORSt+a2​Et−a3​It+a4​St−ξE)\displaystyle=f(a\_{1}\text{LORS}\_{t}+a\_{2}E\_{t}-a\_{3}I\_{t}+a\_{4}S\_{t}-\xi\_{E}) |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | It+1\displaystyle I\_{t+1} | =f​(b1​LORSt−b2​Et−b3​It+b4​St−ξI)\displaystyle=f(b\_{1}\text{LORS}\_{t}-b\_{2}E\_{t}-b\_{3}I\_{t}+b\_{4}S\_{t}-\xi\_{I}) |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | St\displaystyle S\_{t} | =i+e⋅tanh⁡(i)\displaystyle=i+e\cdot\tanh(i) |  | (12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ωt+1\displaystyle\Omega\_{t+1} | =f​(St)\displaystyle=f(S\_{t}) |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | LORSt\displaystyle\text{LORS}\_{t} | =[Et−It]⋅e−k​St2+Ωt\displaystyle=[E\_{t}-I\_{t}]\cdot e^{-kS^{2}\_{t}}+\Omega\_{t} |  | (14) |

where EtE\_{t} and ItI\_{t} represent the states of the excitatory and inhibitory neurons, respectively. The term ii is the base input stimulus (i.e., the pre-activation value from the neural network layer), which is modulated into the external stimulus StS\_{t} via the ratio ee. The term Ωt\Omega\_{t} represents the retrograde signal itself. The parameters aia\_{i} and bib\_{i} are weights governing the internal connections, while ξE\xi\_{E} and ξI\xi\_{I} are the corresponding threshold biases. kk is an attenuation factor, μ\mu is a gain parameter, and LORSt\text{LORS}\_{t} is the oscillator’s final output at time step tt. The hyperbolic tangent (tanh\tanh) is used as the base non-linearity f​(μ;x)f(\mu;x) due to its bounded and sigmoidal nature, which is well-suited for modeling neural firing rates.

A key aspect of our work is the utilization of a diverse set of ten parameterized Lee oscillators. The initial eight types, rigorously derived from systematic studies of the oscillator’s bifurcation behavior [lee2019chaotic], already provide a broad range of dynamics. These include simple bifurcations (e.g., T1, T4), dense chaotic regions (T2, T3), and more complex structures with periodic windows (T5, T7). To better capture the specific topological features inherent in financial market dynamics, we extend this set through a systematic exploration of the parameter space. This leads to the design of two additional configurations, T9 and T10, which were empirically identified through parameter space exploration to better capture the unique dynamics of financial markets.

The most notable feature of T9 is its multi-modal and highly complex structure around the center, which appears not as a single chaotic cloud but as multiple distinct ”lobes” or sub-regimes (see Figure [3](https://arxiv.org/html/2511.10365v2#S3.F3 "Figure 3 ‣ 3.2.1 Core Engine: Lee Oscillator with Retrograde Signaling (LORS) ‣ 3.2 Chaotic Oscillation Component (COC) ‣ 3 The FCOC Framework and Methodology ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting")). This is specifically designed to be analogous to a market that not only exhibits volatility but can abruptly switch between different types of volatile behavior. Conversely, the main characteristic of T10 is its extremely wide and dense chaotic region around the zero-input stimulus. Compared to T2 or T3, it represents a state of generalized and persistent uncertainty, where a much wider range of small input perturbations results in highly unpredictable outcomes.

The inclusion of these two targeted configurations enriches the COC’s library, providing a more comprehensive set of dynamic responses to better model the varied and shifting states of financial volatility. The specific parameter settings are detailed in Table [1](https://arxiv.org/html/2511.10365v2#S3.T1 "Table 1 ‣ 3.2.1 Core Engine: Lee Oscillator with Retrograde Signaling (LORS) ‣ 3.2 Chaotic Oscillation Component (COC) ‣ 3 The FCOC Framework and Methodology ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting"), and their corresponding bifurcation patterns are visually illustrated in Figure [3](https://arxiv.org/html/2511.10365v2#S3.F3 "Figure 3 ‣ 3.2.1 Core Engine: Lee Oscillator with Retrograde Signaling (LORS) ‣ 3.2 Chaotic Oscillation Component (COC) ‣ 3 The FCOC Framework and Methodology ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting").

Table 1: Parameter settings for the 10 types of Lee Oscillators used in experiments.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 |
| a1a\_{1} | 0.0 | 0.5 | 0.5 | -0.5 | -0.9 | -0.9 | -5.0 | -5.0 | 1.0 | 3.0 |
| a2a\_{2} | 5.0 | 0.55 | 0.6 | 0.55 | 0.9 | 0.9 | 5.0 | 5.0 | -1.0 | 3.0 |
| a3a\_{3} | 5.0 | 0.55 | 0.55 | 0.55 | 0.9 | 0.9 | 5.0 | 5.0 | -1.0 | 3.0 |
| a4a\_{4} | 1.0 | -0.5 | 0.5 | -0.5 | -0.9 | -0.9 | -5.0 | -5.0 | -1.0 | 2.0 |
| b1b\_{1} | 0.0 | 0.5 | -0.5 | -0.5 | 0.9 | 0.9 | 1.0 | 1.0 | -1.0 | 0.45 |
| b2b\_{2} | -1.0 | -0.55 | -0.6 | -0.55 | -0.9 | -0.9 | -1.0 | -1.0 | 2.0 | -0.45 |
| b3b\_{3} | 1.0 | -0.55 | -0.55 | -0.55 | -0.9 | -0.9 | -1.0 | -1.0 | 2.0 | -0.45 |
| b4b\_{4} | 0.0 | -0.5 | 0.5 | 0.5 | 0.9 | 0.9 | 1.0 | 1.0 | -1.0 | 1.0 |
| μ\mu | 5 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| kk | 500 | 50 | 50 | 50 | 50 | 300 | 50 | 300 | 50 | 50 |
| ee | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |

![Refer to caption](10_LORS.png)


Figure 3: Bifurcation diagrams for the ten LORS types, showcasing the diverse dynamic behaviors.

#### 3.2.2 Stage 1: Distillation into a Meta-Activation Library

While the LORS provides a wealth of dynamic information, its 100-step temporal trajectory output is architecturally incompatible with standard neural network layers. To bridge this gap, we design a critical processing stage: Max-over-Time (MoT) Pooling. This process is not a mere dimensionality reduction but a fundamental distillation. It transforms the entire dynamic trajectory of an oscillator into a single and salient scalar value, effectively creating a unique, static, yet highly nonlinear meta-activation function.

The procedure, formalized in Algorithm [2](https://arxiv.org/html/2511.10365v2#alg2 "Algorithm 2 ‣ 3.2.2 Stage 1: Distillation into a Meta-Activation Library ‣ 3.2 Chaotic Oscillation Component (COC) ‣ 3 The FCOC Framework and Methodology ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting"), is applied to each of the ten oscillator types for a given pre-activation value xx. The result is a library of ten distinct meta-activation functions, {fT1​(x),…,fT10​(x)}\{f\_{\text{T1}}(x),\dots,f\_{\text{T10}}(x)\}, as visualized in Figure [4](https://arxiv.org/html/2511.10365v2#S3.F4 "Figure 4 ‣ 3.2.2 Stage 1: Distillation into a Meta-Activation Library ‣ 3.2 Chaotic Oscillation Component (COC) ‣ 3 The FCOC Framework and Methodology ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting"). This library forms the foundation for the subsequent adaptive selection stage.

Algorithm 2  Meta-Activation Generation via Max-over-Time (MoT) Pooling

1:

2:Pre-activation value x∈ℝx\in\mathbb{R}

3:Set of M=10M=10 Lee oscillator parameter configurations, 𝒞\mathcal{C}

4:Number of oscillator steps, N=100N=100

5:

6:A vector of MM scalar meta-activation values 𝐀​(x)\mathbf{A}(x)

7:

8:function GenerateMetaActivations(x,𝒞x,\mathcal{C})

9:  Initialize 𝐀​(x)←empty vector of size ​M\mathbf{A}(x)\leftarrow\text{empty vector of size }M

10:  for i=1i=1 to MM do

11:   Ctype←𝒞​[i]C\_{\text{type}}\leftarrow\mathcal{C}[i]

12:   LORSraw\_traj←Run\_Oscillator​(x,Ctype,steps=N)\text{LORS}\_{\text{raw\\_traj}}\leftarrow\text{Run\\_Oscillator}(x,C\_{\text{type}},\text{steps}=N)

13:   LORSdynamics←LORSraw\_traj[1:]\text{LORS}\_{\text{dynamics}}\leftarrow\text{LORS}\_{\text{raw\\_traj}}[1:]

14:   ftype​(x)←max⁡(LORSdynamics)f\_{\text{type}}(x)\leftarrow\max(\text{LORS}\_{\text{dynamics}})

15:   𝐀​(x)​[i]←ftype​(x)\mathbf{A}(x)[i]\leftarrow f\_{\text{type}}(x)

16:  end for

17:  return 𝐀​(x)\mathbf{A}(x)

18:end function

![Refer to caption](MOT_10_LORS.png)


Figure 4: The ten distinct meta-activation functions, ftype​(x)f\_{\text{type}}(x), generated by applying Max-over-Time (MoT) pooling.

#### 3.2.3 Stage 2: Final Activation via Maximum Response Selection

Once the library of ten meta-activation functions is generated for a given input xx (producing the vector 𝐀​(x)\mathbf{A}(x) as per Algorithm [2](https://arxiv.org/html/2511.10365v2#alg2 "Algorithm 2 ‣ 3.2.2 Stage 1: Distillation into a Meta-Activation Library ‣ 3.2 Chaotic Oscillation Component (COC) ‣ 3 The FCOC Framework and Methodology ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting")), the final step is to produce a single activation output. For this, we adopt the Maximum Response Selection (Max-Select) strategy. This choice is not arbitrary but is deliberately grounded in the Winner-Takes-All (WTA) principle, a computational mechanism with deep roots in theoretical neuroscience and continued relevance in modern cognitive science. The WTA concept, foundational to the theory of efficient neural coding [barlow1972single], posits that from a group of competing processing units, only the one with the strongest response should determine the final output. This principle is considered a cornerstone of models explaining decision-making and perception [heathcote2022winner].

The theoretical justification for using Max-Select is twofold. First, from a neuro-computational perspective, each of our ten oscillators represents a distinct potential dynamic regime (e.g., stable, bifurcating, wide-band chaotic). For any given input stimulus xx, it is plausible that one specific dynamic regime is predominantly responsible for the system’s subsequent behavior. The Max-Select strategy, by implementing a hard form of WTA, identifies and propagates the response from this single, most dominant regime. An alternative like averaging would dilute this salient signal by mixing it with weaker, less relevant dynamic responses, thereby obscuring the critical information.

Second, from a modeling perspective, Max-Select offers a robust, parameter-free alternative to more complex, learnable mechanisms like an attention layer. While an attention mechanism could learn to weigh the oscillators, it would introduce additional parameters and computational overhead, increasing the risk of overfitting. In contrast, our principled, biologically-inspired approach is both efficient and highly effective, as confirmed by our extensive empirical validation.

|  |  |  |  |
| --- | --- | --- | --- |
|  | fLee​(x)=max⁡(𝐀​(x))=max⁡(fT1​(x),…,fT10​(x))f\_{\text{Lee}}(x)=\max\left(\mathbf{A}(x)\right)=\max\left(f\_{\text{T1}}(x),\dots,f\_{\text{T10}}(x)\right) |  | (15) |

This approach allows us to leverage a diverse set of dynamic behaviors through a decisive selection mechanism rather than a blended compromise.

## 4 Problem Formulation and Experiments

This section formally defines the volatility forecasting problem and details the empirical validation of the FCOC framework. We begin by describing the dataset and feature generation process, and subsequently outline the complete experimental setup, including model configurations, evaluation metrics, and training protocols.

### 4.1 Data Description and Feature Generation

In this study, we use the 5-minute intraday returns and daily log-returns for two major U.S. stock market indices: the Standard & Poor’s (S&P) 500 Index and the Dow Jones Index (DJI). The data are obtained from
the Wind Economics Database of China. The sample data consists of calculated RV data for the S&P 500 and the DJI, spanning from December 13, 2005 to February 7, 2025, and from October 9, 2009 to February 7, 2025, respectively, which reflects the availability of the sampled high-frequency data for both indices. This combined time frame allows for a comprehensive analysis covering a wide range of market conditions, including the aftermath of the 2008 financial crisis, the subsequent period of quantitative easing, and the 2020 COVID-19 crash.

We employ the daily realized volatility (RV) as the proxy of the true latent volatility, as it is nearly unbiased and efficient [andersen2003modeling]. For a given trading day tt with MM intraday returns, RV is formally defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​Vt=∑j=1Mrt,j2RV\_{t}=\sum\_{j=1}^{M}r\_{t,j}^{2} |  | (16) |

where rt,jr\_{t,j} is the jj-th intraday log return in percentage on day tt. The use of high-frequency data to construct RV offers a significant advantage over traditional low-frequency estimators (e.g., squared daily returns), as it provides a much more precise and less noisy measure of daily price variation. In this analysis, our primary objective is to forecast the one-day-ahead RV for both indices.

To generate the fractal features via OSW-MF-ADCCA for each index, we construct two primary input series from the high-frequency data. The first is the daily log return (rtr\_{t}) in percentage:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=100×(ln⁡(Pt)−ln⁡(Pt−1))r\_{t}=100\times(\ln(P\_{t})-\ln(P\_{t-1})) |  | (17) |

where PtP\_{t} is the closing price on day tt.

The second input series is the volatility increment (vtv\_{t}), which captures the dynamics of volatility changes. It is constructed using the realized bipower variation (B​P​VtBPV\_{t}), a measure known for its robustness to price jumps [barndorff2004power]. For a day tt with MM intraday returns rt,jr\_{t,j}, BPV is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​P​Vt=μ1−2​∑j=2M|rt,j|​|rt,j−1|BPV\_{t}=\mu\_{1}^{-2}\sum\_{j=2}^{M}|r\_{t,j}||r\_{t,j-1}| |  | (18) |

where μ1=2/π\mu\_{1}=\sqrt{2/\pi}. We then define the volatility increment vtv\_{t} as the log-difference of the square root of BPV:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt=ln⁡(B​P​Vt)−ln⁡(B​P​Vt−1)v\_{t}=\ln(\sqrt{BPV\_{t}})-\ln(\sqrt{BPV\_{t-1}}) |  | (19) |

The distinction between using a BPV-derived measure for feature engineering and RV as the forecast target is a deliberate methodological choice. While BPV and RV are closely related, BPV’s jump-robust nature allows our fractal analysis to capture the underlying persistence of the continuous component of volatility, providing a cleaner and more stable signal of the market’s memory state. Our forecast target, however, is the RV, as it represents the complete price variation, including jumps, and is therefore of greater practical and economic importance for risk management and option pricing. This approach avoids trivializing the forecasting task while leveraging the best possible signal for feature extraction.

The characteristics of these key time series are presented visually in Figure [5](https://arxiv.org/html/2511.10365v2#S4.F5 "Figure 5 ‣ 4.1 Data Description and Feature Generation ‣ 4 Problem Formulation and Experiments ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting") and statistically in Table [2](https://arxiv.org/html/2511.10365v2#S4.T2 "Table 2 ‣ 4.1 Data Description and Feature Generation ‣ 4 Problem Formulation and Experiments ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting"). The plots visually confirm the rationale for focusing on RV; while log returns appear highly noisy, the RV series for both indices exhibit clear structural patterns like volatility clustering, making them more statistically tractable targets. The descriptive statistics further confirm the stylized facts of financial data. For both indices, the RV and rtr\_{t} series exhibit extremely high kurtosis and significant Jarque-Bera (JB) statistics, rejecting normality and indicating fat-tailed distributions. Furthermore, the Augmented Dickey-Fuller (ADF) and KPSS tests confirm that the input series (rtr\_{t} and vtv\_{t}) are stationary, validating their direct use in our models. These properties motivate the use of advanced architectures for capturing such complex dynamics.

![Refer to caption](SP500_Log_Return_Plot.png)


(a) S&P 500 Daily Log Return (rtr\_{t}).

![Refer to caption](DJI_Log_Return_Plot.png)


(b) DJI Daily Log Return (rtr\_{t}).

![Refer to caption](SP500_Realized_Volatility_Plot.png)


(c) S&P 500 Realized Volatility (RV).

![Refer to caption](DJI_Realized_Volatility_Plot.png)


(d) DJI Realized Volatility (RV).

Figure 5: Comparison of Log Return and Realized Volatility series for the S&P 500 and DJI.




Table 2: Descriptive statistics for key time series of the S&P 500 and DJI

| Index | Variable | Mean | Max | Min | Std. Dev. | Kurtosis | JB | ADF | KPSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S&P 500 | RV | 0.8538 | 59.4474 | 0.0088 | 2.2696 | 175.02 | 5903183.63\*\*\* | -7.326\*\*\* | 0.5817 |
| rtr\_{t} | 0.0317 | 10.7811 | -12.7652 | 1.2453 | 12.01 | 27556.77\*\*\* | -17.113\*\*\* | 0.2214 |
| vtv\_{t} | 0.0002 | 1.4818 | -1.1975 | 0.3375 | 0.55 | 72.84\*\*\* | -16.745\*\*\* | 0.0167 |
| DJI | RV | 0.5665 | 40.1264 | 0.0155 | 1.6341 | 266.12 | 10733939.86\*\*\* | -10.191\*\*\* | 0.2405 |
| rtr\_{t} | 0.0380 | 10.7639 | -13.8418 | 1.0431 | 21.06 | 66928.69\*\*\* | -12.722\*\*\* | 0.0173 |
| vtv\_{t} | 0.0001 | 1.4191 | -1.4339 | 0.3281 | 0.60 | 67.66\*\*\* | -15.807\*\*\* | 0.0159 |

* Note: \*, \*\*, and \*\*\* denote rejection of the null hypothesis at the 10%, 5%, and 1% significance levels, respectively.

Using the OSW-MF-ADCCA algorithm, we compute the time-varying asymmetric Hurst exponents for each index by applying a rolling window of T=252T=252 days (i.e., number of trading days in a year) to their respective (rt,vtr\_{t},v\_{t}) pairs. This process generates the core feature set for our models.

### 4.2 Experimental Setup

Our experimental design is structured to rigorously evaluate the performance and generalizability of the FCOC framework. The primary objective is to forecast the one-day-ahead realized volatility (R​Vt+1RV\_{t+1}) for both the S&P 500 and DJI indices. To ensure a robust out-of-sample evaluation, each dataset is chronologically divided into training, validation, and test sets according to an approximate 7:1:2 ratio, respectively. This results in three distinct and non-overlapping periods dedicated to model learning, hyperparameter optimization, and final performance assessment.

Prior to training, all input features undergo Min-Max normalization to scale them into a consistent [0, 1] range, a standard procedure to stabilize the learning process. The transformation is defined by the formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x′=x−xminxmax−xminx^{\prime}=\frac{x-x\_{\min}}{x\_{\max}-x\_{\min}} |  | (20) |

where xminx\_{\min} and xmaxx\_{\max} represent the minimum and maximum values of a feature over the training set, respectively. Crucially, for each dataset, these scaling parameters are computed only on its respective training set and are then applied to its validation and testing sets to prevent any data leakage.

For the training process, all models are optimized by minimizing the Mean Squared Error (MSE) loss function using the Adam optimizer. The MSE is chosen as the training objective due to its stability and its property of heavily penalizing large prediction errors. For hyperparameter tuning on the validation set, we adopt a holistic evaluation approach. While all four performance metrics - MSE, Mean Absolute Error (MAE), the Coefficient of Determination (R²), and the Quasi-Likelihood (QLIKE) - are considered to ensure a well-rounded performance, we place a particular emphasis on the QLIKE loss [patton2011volatility]. As a robust loss function for comparing volatility models under noisy conditions, QLIKE serves as a key criterion for final model selection, ensuring that our chosen configurations are both accurate and superior from a risk-management perspective. Key hyperparameters, such as the learning rate (with a primary value of 0.001) and number of hidden neurons, are tuned via the grid search, with a fixed look-back window of 60 days and a batch size of 64.

To ensure the robustness of our findings, we apply the Model Confidence Set (MCS) procedure [hansen2011model] to identify an optimal set of models with predictive advantages, considering that multiple models can be considered the best with the equal predictive accuracy. The MCS test is applied to a pool of models comprising the benchmark models and their variants enhanced with either the standard MF-ADCCA or our proposed OSW-MF-ADCCA features. This comparison allows us to statistically validate the effectiveness of our feature engineering approach before integrating it into the final FCOC framework. At a 25% significance level, we conduct the procedure with 10,000 bootstrap resamples and a block length of 30 to generate the MCS p-values.

## 5 Empirical Analysis

To validate the robustness and generalizability of the FCOC framework, we conduct a comprehensive study on forecasting the RV of two of the world’s most prominent stock market indices: the S&P 500 and the DJI. While both represent the mature U.S. market, they differ significantly in their composition and weighting methodology, providing a robust testbed for our methodology. All experiments are implemented in Python 3.10 using the PyTorch 2.0 framework with CUDA 11.8 acceleration on a system equipped with an NVIDIA RTX 3060 GPU, an Intel i7-11800H CPU, and 32GB of RAM.

### 5.1 Performance of the Fractal Feature Corrector (FFC)

We first evaluate the effectiveness of the FFC component by comparing benchmark models against variants enhanced with fractal features. Table [3](https://arxiv.org/html/2511.10365v2#S5.T3 "Table 3 ‣ 5.1 Performance of the Fractal Feature Corrector (FFC) ‣ 5 Empirical Analysis ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting") details the performance of models augmented with standard MF-ADCCA and our proposed OSW-MF-ADCCA. The results consistently show that enriching models with fractal features improves forecasting accuracy. Notably, the OSW-MF-ADCCA variant, which mitigates spurious fluctuations through overlapping segmentation, generally yields the best performance across all model families and datasets. For example, it boosts the Transformer’s R² on the S&P 500 from 0.1234 to 0.3829, a 210% increase.

To statistically validate this choice, we conducted a Model Confidence Set (MCS) test, with results presented in Table [4](https://arxiv.org/html/2511.10365v2#S5.T4 "Table 4 ‣ 5.1 Performance of the Fractal Feature Corrector (FFC) ‣ 5 Empirical Analysis ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting"). The OSW-MF-ADCCA configuration achieves a p-value of 1.0000 across all scenarios, indicating that it is the sole member of the superior set of models at a 25% significance level. This confirms the robustness of our feature extraction method and justifies its use as the core of the FFC.

Table 3: Comparative performance of FFC-enhanced models on the S&P 500 and DJI indices. Best results within each model family and index are in bold.

| Model Family | Method | S&P 500 | | | | Dow Jones Industrial Average | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R² (↑\uparrow) | QLIKE (↓\downarrow) | MAE (↓\downarrow) | MSE (↓\downarrow) | R² (↑\uparrow) | QLIKE (↓\downarrow) | MAE (↓\downarrow) | MSE (↓\downarrow) |
| LSTM | Benchmark | 0.4460 | 0.2238 | 0.2782 | 0.3030 | 0.4618 | 0.1687 | 0.1936 | 0.1453 |
| MF-ADCCA | 0.4556 | 0.2064 | 0.2784 | 0.2978 | 0.4794 | 0.1602 | 0.1922 | 0.1405 |
| OSW-MF-ADCCA | 0.4643 | 0.2066 | 0.2774 | 0.2930 | 0.4968 | 0.1508 | 0.1906 | 0.1358 |
| GRU | Benchmark | 0.4335 | 0.2371 | 0.2787 | 0.3099 | 0.3549 | 0.2062 | 0.2113 | 0.1741 |
| MF-ADCCA | 0.4121 | 0.2590 | 0.2850 | 0.3216 | 0.3948 | 0.2095 | 0.2059 | 0.1633 |
| OSW-MF-ADCCA | 0.4687 | 0.2056 | 0.2757 | 0.2906 | 0.4051 | 0.1867 | 0.2037 | 0.1606 |
| Mamba | Benchmark | 0.4099 | 0.2686 | 0.2861 | 0.3228 | 0.2632 | 0.1602 | 0.2648 | 0.1989 |
| MF-ADCCA | 0.4176 | 0.2616 | 0.2864 | 0.3186 | 0.3197 | 0.1529 | 0.2193 | 0.1836 |
| OSW-MF-ADCCA | 0.4593 | 0.2159 | 0.2811 | 0.2958 | 0.4365 | 0.1498 | 0.2080 | 0.1521 |
| Transformer | Benchmark | 0.1234 | 0.1993 | 0.3793 | 0.4816 | 0.3700 | 0.1693 | 0.2698 | 0.1701 |
| MF-ADCCA | 0.1411 | 0.2034 | 0.3824 | 0.4719 | -1.0111 | 0.2194 | 0.4321 | 0.5428 |
| OSW-MF-ADCCA | 0.3829 | 0.1995 | 0.3083 | 0.3375 | 0.4045 | 0.1445 | 0.2188 | 0.1607 |




Table 4: Model Confidence Set (MCS) p-values at 25% Significance Level.

| Index | Model | Benchmark | MF-ADCCA | OSW-MF-ADCCA |
| --- | --- | --- | --- | --- |
| S&P 500 | LSTM | 0.0130 | 0.0430 | 1.0000 |
| GRU | 0.0130 | 0.0130 | 1.0000 |
| Mamba | 0.0090 | 0.0060 | 1.0000 |
| Transformer | 0.0120 | 0.0130 | 1.0000 |
| DJI | LSTM | 0.0250 | 0.0250 | 1.0000 |
| GRU | 0.0480 | 0.0600 | 1.0000 |
| Mamba | 0.0130 | 0.1510 | 1.0000 |
| Transformer | 0.2480 | 0.0200 | 1.0000 |

### 5.2 Ablation Study and Synergistic Gains of the FCOC Framework

Having validated the effectiveness of the FFC, we now conduct a comprehensive ablation study to dissect the individual contribution of the Chaotic Oscillation Component (COC) and demonstrate the synergistic power of the full FCOC framework. We compare four configurations: (1) Benchmark (Base Features + ReLU), (2) COC-only (Base Features + COC), (3) FFC-only (Fractal Features + ReLU), and (4) the Full FCOC framework (Fractal Features + COC). The complete results are presented in Table [5](https://arxiv.org/html/2511.10365v2#S5.T5 "Table 5 ‣ 5.2 Ablation Study and Synergistic Gains of the FCOC Framework ‣ 5 Empirical Analysis ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting").

The results provide direct and powerful evidence for our central thesis. The ”COC-only” configuration demonstrates significant performance gains over the benchmark across all tested architectures, strongly validating our hypothesis of a fundamental complexity mismatch between static processors and dynamic financial signals. This effect is most pronounced in the case of the Transformer on the S&P 500, where merely replacing the static ReLU with our dynamic COC causes its R² to surge from a dismal 0.1234 to a competitive 0.4413—a dramatic improvement of over 250%. This proves the standalone novelty and value of the COC.

Ultimately, the full FCOC framework consistently delivers the best overall performance, revealing a powerful synergistic effect. In nearly every case, the full framework (4) outperforms not only the benchmark (1) but also both single-component configurations (2 and 3). For example, on the DJI, the FCOC-Mamba achieves an R² of 0.5066, substantially higher than both the FFC-only (0.4365) and COC-only (0.4913) versions. This confirms that the highest-fidelity signals from the FFC are most effectively leveraged by the commensurately complex processor of the COC, validating our co-driven design philosophy. The visual forecasts in Figure [6](https://arxiv.org/html/2511.10365v2#S5.F6 "Figure 6 ‣ 5.2 Ablation Study and Synergistic Gains of the FCOC Framework ‣ 5 Empirical Analysis ‣ FCOC: A Fractal-Chaotic Co-driven Framework for Financial Volatility Forecasting") further corroborate the superior accuracy of the full FCOC models.

Table 5: Comprehensive Ablation Study of FCOC Framework Components on S&P 500 and DJI Test Sets.

| Dataset | Model | (1) Benchmark | | | | (2) COC-only | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R² (↑\uparrow) | QLIKE (↓\downarrow) | MAE (↓\downarrow) | MSE (↓\downarrow) | R² (↑\uparrow) | QLIKE (↓\downarrow) | MAE (↓\downarrow) | MSE (↓\downarrow) |
| S&P 500 | LSTM | 0.4460 | 0.2238 | 0.2782 | 0.3030 | 0.4738 | 0.1920 | 0.2713 | 0.2591 |
| GRU | 0.4335 | 0.2371 | 0.2787 | 0.3099 | 0.4633 | 0.2032 | 0.2652 | 0.2643 |
| Mamba | 0.4099 | 0.2686 | 0.2861 | 0.3228 | 0.4726 | 0.2008 | 0.2668 | 0.2597 |
| Transformer | 0.1234 | 0.1993 | 0.3793 | 0.4816 | 0.4413 | 0.1912 | 0.2866 | 0.2751 |
| DJI | LSTM | 0.4618 | 0.1687 | 0.1936 | 0.1453 | 0.4849 | 0.1512 | 0.1941 | 0.1401 |
| GRU | 0.3549 | 0.2062 | 0.2113 | 0.1741 | 0.4339 | 0.1953 | 0.2008 | 0.1540 |
| Mamba | 0.2632 | 0.1602 | 0.2648 | 0.1989 | 0.4913 | 0.1506 | 0.1959 | 0.1384 |
| Transformer | 0.3700 | 0.1693 | 0.2698 | 0.1701 | 0.4717 | 0.1595 | 0.1990 | 0.1437 |
| Dataset | Model | (3) FFC-only | | | | (4) Full FCOC Framework | | | |
| R² (↑\uparrow) | QLIKE (↓\downarrow) | MAE (↓\downarrow) | MSE (↓\downarrow) | R² (↑\uparrow) | QLIKE (↓\downarrow) | MAE (↓\downarrow) | MSE (↓\downarrow) |
| S&P 500 | LSTM | 0.4643 | 0.2066 | 0.2774 | 0.2930 | 0.4950 | 0.1872 | 0.2822 | 0.2774 |
| GRU | 0.4687 | 0.2056 | 0.2757 | 0.2906 | 0.4848 | 0.1906 | 0.2877 | 0.2831 |
| Mamba | 0.4593 | 0.2159 | 0.2811 | 0.2958 | 0.4762 | 0.1899 | 0.2921 | 0.2865 |
| Transformer | 0.3829 | 0.1995 | 0.3083 | 0.3375 | 0.4733 | 0.1920 | 0.2980 | 0.2881 |
| DJI | LSTM | 0.4968 | 0.1508 | 0.1906 | 0.1358 | 0.5061 | 0.1400 | 0.1946 | 0.1333 |
| GRU | 0.4051 | 0.1867 | 0.2037 | 0.1606 | 0.4621 | 0.1545 | 0.2053 | 0.1452 |
| Mamba | 0.4365 | 0.1498 | 0.2080 | 0.1521 | 0.5066 | 0.1384 | 0.2031 | 0.1332 |
| Transformer | 0.4045 | 0.1445 | 0.2188 | 0.1607 | 0.4851 | 0.1590 | 0.1919 | 0.1390 |

* \*

  Note: Best results for each metric within each (Dataset, Model) group are highlighted in bold.



![Refer to caption](Mamba_Osc9_max.png)


(a) Mamba-FCOC Forecast (S&P 500)

![Refer to caption](Transformer_Osc9_max.png)


(b) Transformer-FCOC Forecast (S&P 500)

![Refer to caption](DJIMamba_Osc9_max.png)


(c) Mamba-FCOC Forecast (DJI)

![Refer to caption](DJITransformer_Osc10_max.png)


(d) Transformer-FCOC Forecast (DJI)

Figure 6: Comparative out-of-sample forecasting performance for representative FCOC models on the S&P 500 and DJI test sets.

### 5.3 Discussion

The comprehensive empirical results do more than simply demonstrate superior forecasting accuracy; they provide deep insights into the architectural synergies of our co-driven framework and reveal fundamental limitations in current deep learning approaches to financial forecasting. The framework’s impact is perhaps most vividly demonstrated by resolving what we term the Transformer Paradox. While the benchmark Transformer fails on noisy financial data due to its unconstrained attention mechanism, the FCOC framework orchestrates a dramatic recovery. The ablation study proves unequivocally that the Chaotic Oscillation Component (COC) is the decisive factor, as its introduction alone is sufficient to fix the Transformer’s core weakness by providing a dynamic processing unit whose complexity matches the signal. While the framework serves as a corrective measure for such architectures, for models with strong sequential priors like LSTM and Mamba, it acts as a powerful empowerment layer. Here, the synergy of our framework’s two pillars shines: the Fractal Feature Corrector (FFC) provides a direct, high-fidelity signal of the market’s memory state, which is then processed by the COC’s dynamic engine. The spectacular 92.5% R² improvement for the FCOC-Mamba model on the DJI dataset is the definitive evidence of this co-driven synergy, unlocking the full potential of advanced architectures.

Beyond these performance gains, our findings point toward deeper principles and promising new research frontiers. An intriguing finding is the models’ architectural affinity for specific chaotic dynamics, such as the preference of S&P 500 models for the multi-modal T9 oscillator. We speculate that this is not arbitrary, but rather evidence of a ”dynamic resonance” between the model’s internal structure and the data’s topological properties. This suggests a future research direction beyond one-size-fits-all activations toward architecture-dynamics co-design. From a practical standpoint, the nuanced behavior of the error metrics further underscores the framework’s value. The marked improvements in MSE and QLIKE, even with slight degradation in MAE in some cases, are not a trade-off but a desirable feature for risk management. It demonstrates that our framework excels at mitigating catastrophic risk during market turmoil by heavily penalizing large errors, a highly favorable characteristic for any real-world financial application.

## 6 Conclusion

This paper introduces the FCOC framework, a novel architecture designed to address the dual bottlenecks of feature fidelity and model responsiveness in volatility forecasting. By synergistically combining our novel Fractal Feature Corrector with a dynamic Chaotic Oscillation Component, our framework significantly enhances the predictive power of advanced deep learning models. Our comprehensive empirical study on the S&P 500 and DJI demonstrates the framework’s robustness and generalizability. The findings reveal that FCOC not only empowers sequential models like LSTM by providing explicit market-state information but also offers a path to resolving the Transformer Paradox by equipping its attention mechanism with a crucial inductive bias. This work validates a new co-driven paradigm, showing that the synergy between superior theoretical features and dynamic internal processors is a key factor in unlocking the full potential of deep learning in complex financial environments. Future research should focus on both deepening the theoretical underpinnings of this approach—for instance, by using nonlinear time series and topological data analysis to quantitatively compare the market’s attractor reconstruction with the oscillators’ phase space structures—and extending its practical applications to extreme settings like cryptocurrency markets and domains such as algorithmic trading and portfolio optimization.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## CRediT authorship contribution statement

Yilong Zeng: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Writing – Original Draft.
Boyan Tang: Methodology, Software, Data Curation.
Xuanhao Ren: Visualization, Investigation.
Sherry Zhefang Zhou: Conceptualization, Supervision, Writing – Review & Editing, Funding acquisition.
Jianghua Wu: Supervision, Project administration.
Raymond Lee: Conceptualization, Supervision, Writing – Review & Editing, Funding acquisition.

## Acknowledgments

This work was supported in part by the Guangdong Provincial Key Laboratory of IRADS (2022B1212010006) and the Shenzhen Research Institute of Big Data (J00220240006).

## Data availability statement

The data that support the findings of this study are available from Wind. Restrictions apply to the availability of these data, which are used under license for this study. Data are available from https://www.wind.com.cn/