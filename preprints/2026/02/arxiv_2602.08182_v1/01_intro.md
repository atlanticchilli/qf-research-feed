---
authors:
- Hiromu Ozai
- Kei Nakagawa
doc_id: arxiv:2602.08182v1
family_id: arxiv:2602.08182
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY'
url_abs: http://arxiv.org/abs/2602.08182v1
url_html: https://arxiv.org/html/2602.08182v1
venue: arXiv q-fin
version: 1
year: 2026
---


Hiromu Ozai
  
Kei Nakagawa

###### Abstract

Modeling time series with long- or short-memory characteristics is a fundamental challenge in many scientific and engineering domains. While fractional Brownian motion has been widely used as a noise source to capture such memory effects, its incompatibility with Itô calculus limits its applicability in neural stochastic differential equation (SDE) frameworks.
In this paper, we propose a novel class of noise, termed Neural Network-kernel ARMA-type noise (NA-noise), which is an Itô-process-based alternative capable of capturing both long- and short-memory behaviors. The kernel function defining the noise structure is parameterized via neural networks and decomposed into a product form to preserve the Markov property. Based on this noise process, we develop NANSDE-Net, a generative model that extends Neural SDEs by incorporating NA-noise. We prove the theoretical existence and uniqueness of the solution under mild conditions and derive an efficient backpropagation scheme for training.
Empirical results on both synthetic and real-world datasets demonstrate that NANSDE-Net matches or outperforms existing models, including fractional SDE-Net, in reproducing long- and short-memory features of the data, while maintaining computational tractability within the Itô calculus framework.

## 1 Introduction

Time series generation using deep learning has become an active area of research, particularly in modeling complex real-world dynamics.
This is especially true in fields such as physics and finance, where it is important to model continuous-time dynamics in a natural way. One promising approach is the Neural Ordinary Differential Equation (Neural ODE) model [[4](https://arxiv.org/html/2602.08182v1#bib.bib4)], which combines differential equations with deep learning. Neural ODE views ResNet [[9](https://arxiv.org/html/2602.08182v1#bib.bib9)] as the limit of infinitely deep networks and models time evolution as a continuous process using ODEs.
A new family of Neural ODEs was proposed to model various dynamic systems, allowing for flexible representation of complex temporal patterns [[12](https://arxiv.org/html/2602.08182v1#bib.bib12), [6](https://arxiv.org/html/2602.08182v1#bib.bib6)].

However, real-world time series often include random fluctuations due to measurement noise or external shocks. To address this, the Neural Stochastic Differential Equation (Neural SDE) model has been proposed [[11](https://arxiv.org/html/2602.08182v1#bib.bib11), [10](https://arxiv.org/html/2602.08182v1#bib.bib10)]. It extends Neural ODE by introducing randomness using Brownian motion (Bm), allowing the model to generate stochastic trajectories.
Building on this framework, several variants of Neural SDEs have been developed to model various stochastic systems [[16](https://arxiv.org/html/2602.08182v1#bib.bib16), [15](https://arxiv.org/html/2602.08182v1#bib.bib15)].
Still, a limitation of Neural SDE is that it assumes the Bm as the noise process. The Bm is a Gaussian process with independent and stationary increments, but many real-world systems show long- (resp. short-)memory or non-Markovian behavior111Long-memory refers to persistent statistical dependence across long time lags, in contrast to short-memory where correlations decay quickly. Non-Markovian behavior implies that the future evolution of a system depends not only on its current state but also on its entire history.
, which Bm cannot model well.
For example, in financial markets or natural phenomena, past events often influence future behavior for a long (resp. short) time [[5](https://arxiv.org/html/2602.08182v1#bib.bib5), [14](https://arxiv.org/html/2602.08182v1#bib.bib14), [7](https://arxiv.org/html/2602.08182v1#bib.bib7)].

To handle this, researchers have used fractional Brownian motion (fBm) [[8](https://arxiv.org/html/2602.08182v1#bib.bib8), [13](https://arxiv.org/html/2602.08182v1#bib.bib13)], which can represent long- (resp. short-)memory when the Hurst index H>(resp.<)0.5H>(\rm{resp}.<)0.5.
However, fBm is not an Itô process, so standard stochastic calculus methods cannot be applied. As a result, it is challenging to perform gradient-based optimization or derive closed-form representations for learning and inference.

To overcome this issue, [[2](https://arxiv.org/html/2602.08182v1#bib.bib2), [3](https://arxiv.org/html/2602.08182v1#bib.bib3)] proposed a class of AR(∞\infty)-type Gaussian processes, also known as AutoRegressive and Moving Average (ARMA)-type noise.
These processes have stationary increments and memory, and they are also Itô processes. This means they can model long- (resp. short-)memory and still be analyzed using stochastic calculus.
However, the main difficulty is that their kernel function ℓ​(s,u)\ell(s,u), which determines the structure of the process, is hard to express explicitly in general.

In this paper, we propose a new type of ARMA-type noise called Neural Network (NN)-kernel ARMA-type noise (NA-noise), where the kernel function ℓ​(s,u)\ell(s,u) is approximated by neural networks. Specifically, we express the NN kernel as a product ℓ​(s,u)=ℓ1​(s)​ℓ2​(u)\ell(s,u)=\ell\_{1}(s)\ell\_{2}(u) and use NNs to learn ℓ1\ell\_{1} and ℓ2\ell\_{2}. This allows us to keep the process Markovian and make training easier.

We then build a new stochastic differential equation model driven by this NA-noise, which we call NANSDE (Neural Arma-type Noise SDE), and implement a generative model called NANSDE-Net.
Our NANSDE is written in the Itô form, so it guarantees existence and uniqueness of the solution and can be solved numerically using methods like Euler–Maruyama.

From a theoretical perspective, we review known results for explicit kernel forms (Proposition [2](https://arxiv.org/html/2602.08182v1#Thmproposition2 "Proposition 2([2, 3]) ‣ 2.1 Gaussian Processes with Stationary Increments and the Semimartingale Property ‣ 2 Preliminaries ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY")) and extend them to NN kernels.
We show that NANSDE-Net can reproduce both long- and short-memory behavior, similar to or better than fSDE-Net, while still being compatible with Itô calculus.
In experiments, NANSDE-Net performs well on both H>0.5H>0.5 and H<0.5H<0.5 cases, unlike traditional models that struggle with one or the other.

Our construction guarantees Itô form and a Markov augmentation that facilitate both simulation and training; it does not, in general, enforce stationary increments of the learned noise nor guarantee a prescribed asymptotic decay of autocorrelations associated with rigorous long-memory theory. Designing neural parameterizations that simultaneously ensure Gaussianity, stationary increments, and targeted long-memory asymptotics remains an open direction. Likewise, broad comparisons with state-of-the-art sequence generators and architecture search are outside our present scope. The present work should therefore be read as an Itô-compatible, proof-of-concept alternative to fBm-based approaches, clarifying when and how memory can be introduced into Neural SDEs without abandoning standard stochastic calculus.

## 2 Preliminaries

This section introduces the noise process employed in this study.
In the works by [[2](https://arxiv.org/html/2602.08182v1#bib.bib2)] and [[3](https://arxiv.org/html/2602.08182v1#bib.bib3)], a class of Gaussian processes was proposed that possesses stationary increments and memory, while also being semimartingales.
fBm is commonly used as a Gaussian process with stationary increments.
However, since fBm is not a semimartingale, standard tools of stochastic calculus cannot be applied, making it analytically intractable in many cases.
To address this limitation, [[2](https://arxiv.org/html/2602.08182v1#bib.bib2)] and [[3](https://arxiv.org/html/2602.08182v1#bib.bib3)] introduced a new class of noise processes specifically designed to overcome such difficulties.
Building upon this framework, the present study adopts a modified version of the noise process proposed in those works.

### 2.1 Gaussian Processes with Stationary Increments and the Semimartingale Property

We assume that the process Z​(⋅)Z(\cdot) is a continuous process with stationary increments such that Z​(0)=0Z(0)=0, and satisfies one of the following continuous-time AR(∞\infty)-type equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Zd​t​(t)+∫−∞ta​(t−s)​d​Zd​t​(s)​𝑑s=d​Wd​t​(t).\frac{dZ}{dt}(t)+\int\_{-\infty}^{t}a(t-s)\frac{dZ}{dt}(s)ds=\frac{dW}{dt}(t). |  | (1) |

(see equation (2.10) and (2.17) in [[2](https://arxiv.org/html/2602.08182v1#bib.bib2)] for their precise formulation), where {W​(t)}t∈ℝ\{W(t)\}\_{t\in\mathbb{R}} is a one-dimensional standard Bm defined on (Ω,ℱ,P)(\Omega,\mathcal{F},P) satisfying W​(0)=0W(0)=0, and d​Z/d​tdZ/dt and d​W/d​tdW/dt are the derivatives of Z​(⋅)Z(\cdot) and W​(⋅)W(\cdot) respectively in the random distribution sense.
The kernel a​(⋅)a(\cdot) is a nonnegative decreasing function with some adequate conditions to be specified in [[2](https://arxiv.org/html/2602.08182v1#bib.bib2)]. The case a​(⋅)=0a(\cdot)=0 yields the usual white noise.

As is clear from the definition, {Z​(t)}t∈ℝ\{Z(t)\}\_{t\in\mathbb{R}} does not have independent increments. In other words, it is a stochastic process with memory.
Under appropriate conditions related to a​(⋅)a(\cdot) (see [[2](https://arxiv.org/html/2602.08182v1#bib.bib2), [3](https://arxiv.org/html/2602.08182v1#bib.bib3)]), Z​(⋅)Z(\cdot) has the following MA(∞\infty)-type representation.
In the proposition below, a short range memory type kernel is used for a​(⋅)a(\cdot).

###### Proposition 1([[2](https://arxiv.org/html/2602.08182v1#bib.bib2), [3](https://arxiv.org/html/2602.08182v1#bib.bib3)])

For real parameter q∈ℝq\in\mathbb{R} and positive parameter p∈ℝ>0p\in\mathbb{R}\_{>0} that satisfy p>qp>q, determine a:(0,∞)→ℝa:(0,\infty)\to\mathbb{R} in ([1](https://arxiv.org/html/2602.08182v1#S2.E1 "In 2.1 Gaussian Processes with Stationary Increments and the Semimartingale Property ‣ 2 Preliminaries ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY")) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​(t):=q​e−(p−q)​t.a(t):=qe^{-(p-q)t}. |  | (2) |

Then, {Z​(t)}t∈ℝ\{Z(t)\}\_{t\in\mathbb{R}} in ([1](https://arxiv.org/html/2602.08182v1#S2.E1 "In 2.1 Gaussian Processes with Stationary Increments and the Semimartingale Property ‣ 2 Preliminaries ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY")) has the following MA(∞\infty)-type representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z​(t)=W​(t)−∫0t{∫−∞sc​(s−u)​𝑑W​(u)}​𝑑s,t∈ℝZ(t)=W(t)-\int\_{0}^{t}\left\{\int\_{-\infty}^{s}c(s-u)dW(u)\right\}ds,\quad t\in\mathbb{R} |  | (3) |

Where c:(0,∞)→ℝc:(0,\infty)\to\mathbb{R} is expressed in the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(t)=q​e−p​tc(t)=qe^{-pt} |  | (4) |

Furthermore, by transforming it according to the filtering theory, we obtain the representation of the Ito process of {Z​(t)}t≥0\{Z(t)\}\_{t\geq 0} shown below.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z​(t)=W^​(t)−∫0t{∫0sℓ​(s,u)​𝑑W^​(u)}​𝑑s,t≥0.Z(t)=\hat{W}(t)-\int\_{0}^{t}\left\{\int\_{0}^{s}\ell(s,u)d\hat{W}(u)\right\}ds,\quad t\geq 0. |  | (5) |

where ℓ​(s,u)\ell(s,u) is a deterministic function and {W^​(t)}t≥0\{\hat{W}(t)\}\_{t\geq 0} denotes the innovation process defined below, which is a one-dimensional Brownian motion.

|  |  |  |  |
| --- | --- | --- | --- |
|  | W^(t)=Z(t)+∫0tE[∫−∞sc(s−u)dW(u)|ℱs]ds,t≥0,\hat{W}(t)=Z(t)+\int\_{0}^{t}E\left[\int\_{-\infty}^{s}c(s-u)dW(u)\middle|\mathcal{F}\_{s}\right]ds,\quad t\geq 0, |  | (6) |

To use this {Z​(t)}t≥0\{Z(t)\}\_{t\geq 0} as noise, we need to find the specific form of the Volterra kernel ℓ​(s,u)\ell(s,u).
The explicit form of this kernel was made available for the first time thanks to the results of [[2](https://arxiv.org/html/2602.08182v1#bib.bib2)] and [[3](https://arxiv.org/html/2602.08182v1#bib.bib3)].
The explicit form of ℓ​(s,u)\ell(s,u) can be obtained from the following proposition.

###### Proposition 2([[2](https://arxiv.org/html/2602.08182v1#bib.bib2), [3](https://arxiv.org/html/2602.08182v1#bib.bib3)])

We take c​(⋅)c(\cdot) in the form of equation ([4](https://arxiv.org/html/2602.08182v1#S2.E4 "In Proposition 1([2, 3]) ‣ 2.1 Gaussian Processes with Stationary Increments and the Semimartingale Property ‣ 2 Preliminaries ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY")).
Then ℓ​(s,u)\ell(s,u) in ([5](https://arxiv.org/html/2602.08182v1#S2.E5 "In 2.1 Gaussian Processes with Stationary Increments and the Semimartingale Property ‣ 2 Preliminaries ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY")) has the following closed-form representation:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℓ​(s,u)\displaystyle\ell(s,u) | =e−p​s​ℓ​(u),s>u>0,\displaystyle=e^{-ps}\ell(u),\qquad s>u>0, |  | (7) |
|  | ℓ​(u)\displaystyle\ell(u) | :=q​ep​u​{1−2​q​(p−q)(2​p−q)2​e2​(p−q)​u−q2},u>0.\displaystyle=qe^{pu}\left\{1-\frac{2q(p-q)}{(2p-q)^{2}e^{2(p-q)u}-q^{2}}\right\},\quad u>0. |  |

By explicitly determining the shape of ℓ\ell in this way, the Itô process representation of {Z​(t)}t≥0\{Z(t)\}\_{t\geq 0} can be specifically determined, making it possible to treat {Z​(t)}t≥0\{Z(t)\}\_{t\geq 0} as driving noise within the scope of Itô calculus.
We refer to this type of noise as ARMA-type noise.
Furthermore, although {Z​(t)}t≥0\{Z(t)\}\_{t\geq 0} itself is not a Markov process, it can be embedded as a component of a Markov process because ℓ​(s,u)\ell(s,u) can be decomposed into functions of ss and uu.
That is, if K​(⋅)K(\cdot) is defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | K​(t):=∫0tℓ​(s)​𝑑W^​(s),t≥0,K(t):=\int\_{0}^{t}\ell(s)d\hat{W}(s),\quad t\geq 0, |  | (8) |

(Z​(t),K​(t))⊤(Z(t),K(t))^{\top} is described as a solution to the following Markov-type SDE [[1](https://arxiv.org/html/2602.08182v1#bib.bib1)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Z​(t)=−e−p​t​K​(t)​d​t+d​W^​(t),d​K​(t)=ℓ​(t)​d​W^​(t).\left\{\,\begin{aligned} &dZ(t)=-e^{-pt}K(t)dt+d\hat{W}(t),\\ &dK(t)=\ell(t)d\hat{W}(t).\end{aligned}\right. |  | (9) |

This makes it possible to use numerical calculation methods, such as the Euler–Maruyama method.

### 2.2 ARMA-Type noise with the kernel approximated by a neural network

The kernel in equation ([2](https://arxiv.org/html/2602.08182v1#S2.E2 "In Proposition 1([2, 3]) ‣ 2.1 Gaussian Processes with Stationary Increments and the Semimartingale Property ‣ 2 Preliminaries ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY")) has been shown to represent a short-memory structure (see [[2](https://arxiv.org/html/2602.08182v1#bib.bib2)]).
To reproduce long-memory data, it is necessary to employ a kernel that exhibits long range memory characteristics. [[2](https://arxiv.org/html/2602.08182v1#bib.bib2)] introduces such a kernel in the form a​(t)=p(t+1)p+1,t>0a(t)=\frac{p}{(t+1)^{p+1}},t>0.
However, an explicit expression for the corresponding ℓ​(s,u)\ell(s,u) in this case has not yet been obtained, which remains an open problem.
Therefore, in this paper, we adopt a method that approximates the kernel using neural networks in order to capture long-memory behavior.
To ensure the Markov property, we adopt the form ℓ​(s,u)=ℓ1​(s)​ℓ2​(u)\ell(s,u)=\ell\_{1}(s)\ell\_{2}(u).
The noise process used in this study takes the following form.

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Z​(t)=−ℓ1​(t)​K​(t)​d​t+d​W​(t),d​K​(t)=ℓ2​(t)​d​W​(t).\left\{\,\begin{aligned} &dZ(t)=-\ell\_{1}(t)K(t)dt+dW(t),\\ &dK(t)=\ell\_{2}(t)dW(t).\end{aligned}\right. |  | (10) |

Where ℓ1\ell\_{1} and ℓ2\ell\_{2} are deterministic functions represented by neural networks and WW is a one-dimensional Wiener process.
While ZZ is indeed a Gaussian process, its increments are not guaranteed to be stationary.
We refer to this type of noise as NN-kernel ARMA-Type noise (abbreviated as NA-noise).

### 2.3 SDE Driven by NN-kernel ARMA-Type Noise

To implement NN-kernel ARMA-Type Noise SDE-Net (abbreviated as NANSDE-Net), we study SDEs where the standard Bm is replaced by NA-noise.
We consider SDEs driven by NA-noise ([10](https://arxiv.org/html/2602.08182v1#S2.E10 "In 2.2 ARMA-Type noise with the kernel approximated by a neural network ‣ 2 Preliminaries ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY")) of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Xt=X0+∫0tb​(s,Xs)​𝑑s+∫0tσ​(s,Xs)​𝑑Z​(s)=X0+∫0t{b​(s,Xs)−ℓ1​(s)​σ​(s,Xs)​K​(s)}​𝑑s+∫0tσ​(s,Xs)​𝑑W​(s),Kt=∫0tℓ2​(s)​𝑑W​(s),\left\{\,\begin{aligned} X\_{t}&=X\_{0}+\int\_{0}^{t}b(s,X\_{s})ds+\int\_{0}^{t}\sigma(s,X\_{s})dZ(s)\\ &=X\_{0}+\int\_{0}^{t}\{b(s,X\_{s})-\ell\_{1}(s)\sigma(s,X\_{s})K(s)\}ds\\ &\qquad\qquad\qquad+\int\_{0}^{t}\sigma(s,X\_{s})dW(s),\\ K\_{t}&=\int\_{0}^{t}\ell\_{2}(s)dW(s),\end{aligned}\right. |  | (11) |

where W​(t)W(t) is standard Bm.
Note that when ℓ2​(u)\ell\_{2}(u) is 0, NANSDE-Net becomes SDE-Net. Therefore, NANSDE-Net can be regarded as an extension of SDE-Net. Furthermore, ([11](https://arxiv.org/html/2602.08182v1#S2.E11 "In 2.3 SDE Driven by NN-kernel ARMA-Type Noise ‣ 2 Preliminaries ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY")) is an Itô process, the results of conventional stochastic calculus can be applied to determine the existence and uniqueness of solutions. Furthermore, the Euler–Maruyama method can be used for numerical calculations.

## 3 Generative Modeling of Time Series Using NANSDE-Net

In [[8](https://arxiv.org/html/2602.08182v1#bib.bib8)], to compare the ability of different noise processes to reproduce long-memory effects, the authors deliberately limit the expressive power of the drift and diffusion terms.
Specifically, time tt is not used as an input to the functions bb and σ\sigma.
To conduct experiments under the same setting as in [[8](https://arxiv.org/html/2602.08182v1#bib.bib8)], in the following, we assume that the time evolution of a stochastic process X={Xt}t≥0X=\{X\_{t}\}\_{t\geq 0} is described by the following NANSDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Xt={b​(Xt,θ)−ℓ1​(t,θ)​σ​(Xt,θ)​K​(t,θ)}​d​t+σ​(Xt,θ)​d​Wt,d​K​(t,θ)=ℓ2​(t,θ)​d​Wt.\left\{\,\begin{aligned} &dX\_{t}=\{b(X\_{t},\theta)-\ell\_{1}(t,\theta)\sigma(X\_{t},\theta)K(t,\theta)\}dt\\ &\qquad\qquad\qquad+\sigma(X\_{t},\theta)dW\_{t},\\ &dK(t,\theta)=\ell\_{2}(t,\theta)dW\_{t}.\end{aligned}\right. |  | (12) |

where the drift term bb, the diffusion term σ\sigma, the kernel ℓ1\ell\_{1} and ℓ2\ell\_{2} are parameterized by NN.
Hereafter, we optimize bb, σ\sigma, ℓ1\ell\_{1} and ℓ2\ell\_{2} with respect to the NN-parameters θ\theta.

### 3.1 Network Architecture

To estimate drift, volatility and kernel functions of ([12](https://arxiv.org/html/2602.08182v1#S3.E12 "In 3 Generative Modeling of Time Series Using NANSDE-Net ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY")) by neural networks, we use LL-layer multi-layer perceptron (MLP) as network architecture222We use merely MLP for simplicity. We note that we can expect the improvement of fitting by optimizing network architecture.:

|  |  |  |
| --- | --- | --- |
|  | hiℓ=∑j=1Nℓ−1wi​jℓ−1​xjℓ−1+biℓ−1,xiℓ=φ​(hiℓ)h^{\ell}\_{i}=\sum\_{j=1}^{N\_{\ell-1}}w\_{ij}^{\ell-1}x^{\ell-1}\_{j}+b^{\ell-1}\_{i},\quad x^{\ell}\_{i}=\varphi(h^{\ell}\_{i}) |  |

for each ℓ=1,…,L\ell=1,\ldots,L and each i=1,…,Nℓi=1,\ldots,N\_{\ell}. In this case x0x^{0} and xLx^{L} be input and output data and NN function is such that xL=fθ​(x0)x^{L}=f\_{\theta}(x^{0}) where θ={wi​jℓ,biℓ}i,j,ℓ\theta=\{w\_{ij}^{\ell},b^{\ell}\_{i}\}\_{i,j,\ell}.
In the sequel, let Θ\Theta be the space of NN parameters on which θ\theta takes values. Then existence and uniqueness of NANSDE, and precision assurance of numerical solutions are established as follows.

###### Theorem 3.1(Informal)

The NANSDE-Net generator ([12](https://arxiv.org/html/2602.08182v1#S3.E12 "In 3 Generative Modeling of Time Series Using NANSDE-Net ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY")) whose network architecture is given by MLP with tanh\mathrm{tanh} activation function has a unique solution, which can be numerically solved by the explicit Euler scheme.

###### Proof

Note that the activation function tanh\mathrm{tanh} is smooth and its derivatives of any order are bounded.
Thus, noting that the composition of functions preserves regularity and boundedness, we conclude that the NANSDE ([12](https://arxiv.org/html/2602.08182v1#S3.E12 "In 3 Generative Modeling of Time Series Using NANSDE-Net ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY")), whose drift, volatility, and kernel are parameterized by multilayer perceptrons fθf\_{\theta}, satisfies the Lipschitz continuity and linear growth conditions. Therefore, the solution exists uniquely, and the Euler–Maruyama method is applicable.

### 3.2 Algorithm

The generation procedure of NANSDE-Net is summarized in Algorithm [1](https://arxiv.org/html/2602.08182v1#alg1 "Algorithm 1 ‣ 3.2 Algorithm ‣ 3 Generative Modeling of Time Series Using NANSDE-Net ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY").
This algorithm follows the same procedure as Algorithm in Section V of [[8](https://arxiv.org/html/2602.08182v1#bib.bib8)]. For further details, please refer to [[8](https://arxiv.org/html/2602.08182v1#bib.bib8)].

Algorithm 1  Optimization of NANSDE-Net generator

{X0,…,XT}\{X\_{0},\ldots,X\_{T}\} - a realized path of a stochastic process until time horizon TT, sample size MM, learning rate η\eta, number of optimization steps kk

(θb,θσ,θℓ1,θℓ2)(\theta\_{b},\theta\_{\sigma},\theta\_{\ell\_{1}},\theta\_{\ell\_{2}}) - the optimized parameter for NANSDE-Net generator

while not converged do

for kk steps do

Let {X^0(i),…​X^T(i)}i=1M\{\hat{X}^{(i)}\_{0},\ldots\hat{X}^{(i)}\_{T}\}\_{i=1}^{M} be the realization of generated paths of size MM and let pt​(θ,⋅)p\_{t}(\theta,\cdot) be the probability density function of log-difference process, which is estimated from generated values {r^t(i)}i=1M\{\hat{r}^{(i)}\_{t}\}\_{i=1}^{M} where r^t(i)=log⁡(X^t+1(i)/X^t(i))\hat{r}^{(i)}\_{t}=\log(\hat{X}^{(i)}\_{t+1}/\hat{X}^{(i)}\_{t}).

Compute the gradient of loss function

|  |  |  |
| --- | --- | --- |
|  | ℒ​(θ)=−1T​∑t=0Tlog⁡pθ​(t,rt).\mathcal{L}(\theta)=-\frac{1}{T}\sum\_{t=0}^{T}\log p\_{\theta}(t,r\_{t}). |  |

Descent parameters: θ←θ−η​∇θℒ​(θ)\theta\leftarrow\theta-\eta\nabla\_{\theta}\mathcal{L}(\theta).

end for

end while

## 4 Experiments

We evaluate our models on synthetic and real time series, and generate sample paths from each trained model.
For fair comparison, we follow the dataset choices and settings of [[8](https://arxiv.org/html/2602.08182v1#bib.bib8)].
Readers can consult [[8](https://arxiv.org/html/2602.08182v1#bib.bib8)] for additional dataset details.

#### 4.0.1 Synthetic data

We simulate fractional Brownian motion (fBm) with Hurst indices H∈{0.2, 0.3}H\in\{0.2,\,0.3\} to represent short-memory (anti-persistent) dynamics.
Each path is discretized over [0,1][0,1] into 1000 equal steps (Δ​t=10−3\Delta t=10^{-3}).

#### 4.0.2 Real data

We evaluate on six real-world time series that cover both long- and short-memory behaviors:
SPX (S&P 500), TPX (TOPIX), and SX5E (Euro Stoxx 50) daily closing prices;
NileMin (annual minimum Nile levels at the Roda gauge, 622–1281);
ethernetTraffic (LAN traffic at Bellcore); and
NhemiTemp (monthly Northern Hemisphere temperature anomalies, 1854–1989, CRU/UEA).
The equity index series are obtained from Bloomberg.
The other datasets are from the CRAN package longmemo (<https://cran.r-project.org/web/packages/longmemo/index.html>), which also provides detailed descriptions.

Table 1: Numerical results for each performance metric and generative model for fBm and other types of data from the real world. Bold indicates the best performance.

| Data | Method | Hurst Index | Marginal Distribution | ACF | Weighted ACF | R2R^{2} Score |
| --- | --- | --- | --- | --- | --- | --- |
| fBm(H=0.2) | Original | 0.2 (True value) | - | - | - | - |
| RNN | 0.464 ±\pm 0.111 | 0.615 ±\pm 0.024 | 1.215 | 0.633 | -1.086 ±\pm 0.180 |
| SDE | 0.463 ±\pm 0.132 | 1.058 ±\pm 0.024 | 1.220 | 0.639 | -0.121 ±\pm 0.044 |
| fSDE | 0.581 ±\pm 0.144 | 1.518 ±\pm 0.013 | 1.220 | 0.638 | -0.017 ±\pm 0.018 |
|  | NANSDE | 0.453 ±\pm 0.133 | 1.094 ±\pm 0.070 | 1.276 | 0.727 | -0.109 ±\pm 0.049 |
| fBm(H=0.3) | Original | 0.3 (True value) | - | - | - | - |
| RNN | 0.463 ±\pm 0.121 | 0.475 ±\pm 0.024 | 1.217 | 0.666 | -1.139 ±\pm 0.168 |
| SDE | 0.489 ±\pm 0.157 | 0.567 ±\pm 0.199 | 1.995 | 1.279 | -0.513 ±\pm 0.237 |
| fSDE | 0.581 ±\pm 0.130 | 1.186 ±\pm 0.069 | 1.429 | 0.845 | -0.069 ±\pm 0.037 |
|  | NANSDE | 0.422 ±\pm 0.177 | 0.561 ±\pm 0.191 | 1.995 | 1.415 | -0.716 ±\pm 0.320 |
| SPX | Original | 0.614 | - | - | - | - |
| RNN | 0.471 ±\pm 0.097 | 0.704 ±\pm 0.011 | 2.717 | 1.340 | -6.376 ±\pm 0.605 |
| SDE | 0.510 ±\pm 0.117 | 0.204 ±\pm 0.045 | 2.762 | 1.430 | -2.362 ±\pm 0.946 |
| fSDE | 0.591 ±\pm 0.112 | 0.248 ±\pm 0.043 | 2.716 | 1.343 | -1.170 ±\pm 0.293 |
|  | NANSDE | 0.472 ±\pm 0.115 | 0.202 ±\pm 0.058 | 2.804 | 1.404 | -1.481 ±\pm 0.575 |
| TPX | Original | 0.396 | - | - | - | - |
| RNN | 0.455 ±\pm 0.098 | 0.327 ±\pm 0.012 | 1.889 | 0.829 | -1.524 ±\pm 0.183 |
| SDE | 0.451 ±\pm 0.098 | 0.223 ±\pm 0.024 | 1.900 | 0.842 | -3.471 ±\pm 0.832 |
| fSDE | 0.590 ±\pm 0.137 | 0.261 ±\pm 0.018 | 1.894 | 0.833 | -1.053 ±\pm 0.249 |
|  | NANSDE | 0.396 ±\pm 0.139 | 0.152 ±\pm 0.038 | 2.018 | 0.972 | -2.371 ±\pm 0.653 |
| SX5E | Original | 0.328 | - | - | - | - |
| RNN | 0.468 ±\pm 0.102 | 0.744 ±\pm 0.011 | 2.479 | 1.269 | -2.940 ±\pm 0.277 |
| SDE | 0.464 ±\pm 0.121 | 0.277 ±\pm 0.042 | 2.609 | 1.343 | -5.410 ±\pm 1.291 |
| fSDE | 0.575 ±\pm 0.130 | 0.277 ±\pm 0.128 | 2.893 | 1.514 | -1.616 ±\pm 0.435 |
|  | NANSDE | 0.449 ±\pm 0.130 | 0.351 ±\pm 0.168 | 3.018 | 1.717 | -1.606 ±\pm 0.582 |
| NileMin | Original | 0.973 | - | - | - | - |
| RNN | 0.477 ±\pm 0.121 | 0.554 ±\pm 0.040 | 1.482 | 0.948 | -4.900 ±\pm 0.702 |
| SDE | 0.455 ±\pm 0.145 | 1.211 ±\pm 0.102 | 1.527 | 0.997 | -29.771 ±\pm 8.093 |
| fSDE | 0.646 ±\pm 0.151 | 0.233 ±\pm 0.051 | 1.511 | 0.967 | -1.543 ±\pm 0.410 |
|  | NANSDE | 0.952 ±\pm 0.182 | 0.435 ±\pm 0.192 | 2.938 | 2.463 | -2.837 ±\pm 3.714 |
| ethernetTraffic | Original | 0.750 | - | - | - | - |
| RNN | 0.442 ±\pm 0.100 | 1.400 ±\pm 0.009 | 1.646 | 1.124 | -9.297 ±\pm 0.398 |
| SDE | 0.668 ±\pm 0.138 | 0.980 ±\pm 0.043 | 3.902 | 2.562 | -0.753 ±\pm 0.320 |
| fSDE | 0.761 ±\pm 0.134 | 0.931 ±\pm 0.218 | 3.485 | 2.577 | -0.880 ±\pm 0.508 |
|  | NANSDE | 0.677 ±\pm 0.135 | 0.801 ±\pm 0.037 | 3.224 | 1.827 | -0.739 ±\pm 0.148 |
| NhemiTemp | Original | 1.066 | - | - | - | - |
| RNN | 0.463 ±\pm 0.120 | 0.652 ±\pm 0.023 | 2.069 | 1.343 | -6.973 ±\pm 0.614 |
| SDE | 0.603 ±\pm 0.075 | 0.172 ±\pm 0.023 | 2.092 | 1.348 | -2.290 ±\pm 0.296 |
| fSDE | 0.599 ±\pm 0.161 | 0.965 ±\pm 0.187 | 2.575 | 1.890 | -17.534 ±\pm 6.263 |
|  | NANSDE | 1.025 ±\pm 0.235 | 0.455 ±\pm 0.239 | 4.804 | 3.258 | -1.677 ±\pm 2.245 |

### 4.1 Experimental Setup

In the following, we quantitatively evaluate the performance of the NANSDE-Net using a specified criterion.
For comparison, existing time series generators—including recurrent neural networks (RNN), SDE-Net, and fSDE-Net with H>1/2H>1/2 are used in place of NANSDE-Net.
For the network architecture, we employ a two-layer MLP with 20 hidden units for SDE-Net, fSDE-Net, and NANSDE-Net, while a vanilla RNN with 40 hidden units is used for the RNN generator.

![Refer to caption](figures/NhemiTemp_path_original.png)

![Refer to caption](figures/NhemiTemp_path_RNN.png)

![Refer to caption](figures/NhemiTemp_path_SDE.png)

![Refer to caption](figures/NhemiTemp_path_fSDE.png)

![Refer to caption](figures/NhemiTemp_path_NNKernelArmaSDE.png)

Figure 1: Figure showing the paths of the original data and generated data for NhemiTemp (Data showing long-memory). Synthetic time series are generated after calibration by RNN (upper center), SDE-Net (upper right), fSDE-Net with H>1/2H>1/2 (lower left) and NANSDE-Net(lower center). The NANSDE-Net model successfully reproduces the characteristics of long-memory in NhemiTemp data.



![Refer to caption](figures/SPX_histogram_RNN.png)

![Refer to caption](figures/SPX_histogram_SDE.png)

![Refer to caption](figures/SPX_histogram_fSDE.png)

![Refer to caption](figures/SPX_histogram_NNKernelArmaSDE.png)

Figure 2: Comparison of the histogram of the log return process for both synthetic and actual S&P 500 index data. The synthetic time series are generated after calibration by RNN, SDE-Net, fSDE-Net, and NANSDE-Net, from left to right, respectively.

### 4.2 Performance Metrics

We prioritize the Hurst index as the primary measure of memory fidelity, reflecting our goal of capturing long- and short-memory behavior.

As secondary checks, we report:

(i) Marginal distribution (total variation).
Let {Bk}k=1K\{B\_{k}\}\_{k=1}^{K} be fixed bins. Define empirical frequencies

|  |  |  |
| --- | --- | --- |
|  | pk=1T​∑t=1T𝟏​{rt∈Bk},p^k=1M​T​∑i=1M∑t=1T𝟏​{r^t(i)∈Bk}.p\_{k}=\frac{1}{T}\sum\_{t=1}^{T}\mathbf{1}\{r\_{t}\in B\_{k}\},\qquad\hat{p}\_{k}=\frac{1}{MT}\sum\_{i=1}^{M}\sum\_{t=1}^{T}\mathbf{1}\{\hat{r}^{(i)}\_{t}\in B\_{k}\}. |  |

The discrepancy is

|  |  |  |
| --- | --- | --- |
|  | TV=12​∑k=1K|pk−p^k|∈[0,1](0=identical, 1=maximally different).\mathrm{TV}=\frac{1}{2}\sum\_{k=1}^{K}|p\_{k}-\hat{p}\_{k}|\in[0,1]\quad(0=\text{identical},\ 1=\text{maximally different}). |  |

(ii) Time dependence (ACF scores).
Write r0:T=(r1,…,rT)r\_{0:T}=(r\_{1},\ldots,r\_{T}) and let γ​(τ)=Corr​(|rt|,|rt+τ|)\gamma(\tau)=\mathrm{Corr}(|r\_{t}|,|r\_{t+\tau}|) for lags τ=1,…,S\tau=1,\ldots,S.
Set C​(r0:T)=(γ​(1),…,γ​(S))∈[−1,1]SC(r\_{0:T})=(\gamma(1),\ldots,\gamma(S))\in[-1,1]^{S} and define the score

|  |  |  |
| --- | --- | --- |
|  | ACF=‖C​(r0:T)−1M​∑i=1MC​(r^0:T(i))‖2,\mathrm{ACF}=\Big\|\,C(r\_{0:T})-\frac{1}{M}\sum\_{i=1}^{M}C(\hat{r}^{(i)}\_{0:T})\,\Big\|\_{2}, |  |

where ∥⋅∥2\|\cdot\|\_{2} is the Euclidean norm. A weighted variant emphasizes long lags:

|  |  |  |
| --- | --- | --- |
|  | ACFw=‖C​(r0:T)∘w−1M​∑i=1MC​(r^0:T(i))∘w‖2,\mathrm{ACF}\_{w}=\Big\|\,C(r\_{0:T})\circ w-\frac{1}{M}\sum\_{i=1}^{M}C(\hat{r}^{(i)}\_{0:T})\circ w\,\Big\|\_{2}, |  |

with Hadamard product ∘\circ and weights wτ=2​τ/(S+1)w\_{\tau}=2\tau/(S+1) (unit-mean).

(iii) Predictive accuracy (R2R^{2}).
Using an 80%/20% train/test split, let r~t\tilde{r}\_{t} be one-step-ahead predictions on the test set 𝒯test\mathcal{T}\_{\text{test}} and
r¯test\bar{r}\_{\text{test}} its mean. Report

|  |  |  |
| --- | --- | --- |
|  | R2=1−∑t∈𝒯test(rt−r~t)2∑t∈𝒯test(rt−r¯test)2.R^{2}=1-\frac{\sum\_{t\in\mathcal{T}\_{\text{test}}}(r\_{t}-\tilde{r}\_{t})^{2}}{\sum\_{t\in\mathcal{T}\_{\text{test}}}(r\_{t}-\bar{r}\_{\text{test}})^{2}}. |  |

For fair comparison, we follow the metric definitions and settings in [[8](https://arxiv.org/html/2602.08182v1#bib.bib8)].

### 4.3 Results

Table [1](https://arxiv.org/html/2602.08182v1#S4.T1 "Table 1 ‣ 4.0.2 Real data ‣ 4 Experiments ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY") shows results for the above performance metrics after 1000 iteration steps with 200 early stops where Adam with learning rate 0.004 is used as the optimizer.
Examining the results for data with high Hurst indices, such as NileMin, ethernetTraffic, NBSdiff and NhemiTemp, it can be seen from the table that NANSDE-Net achieves results that are equivalent to or better than those of fSDE-Net. This suggests that NANSDE-Net can reproduce noise exhibiting long-memory with H>1/2H>1/2.
As shown in Figure [1](https://arxiv.org/html/2602.08182v1#S4.F1 "Figure 1 ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY"), for NhemiTemp paths with long-memory, NANSDE-Net performs as well as or better than fSDE-Net. Moreover, unlike SDE-Net, it more accurately captures the characteristic features of the paths. This indicates that NA-noise, unlike Brownian motion, possesses the ability to capture long-memory characteristics.
Moreover, for datasets such as SPX, NileMin, and Ethernet, NANSDE-Net generates superior marginal distributions compared to SDE-Net.
However, from an overall perspective, focusing on performance metrics related to marginal distributions and autocorrelation functions (ACF), it cannot be conclusively stated that NANSDE-Net clearly outperforms the other methods [2](https://arxiv.org/html/2602.08182v1#S4.F2 "Figure 2 ‣ 4.1 Experimental Setup ‣ 4 Experiments ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY").
Furthermore, looking at the results for data with small Hurst indices such as fBm, TPX and SX5E, RNN shows good results overall, but NANSDE-Net shows better results than other neural SDE methods such as SDE-Net and fSDE-Net.
This demonstrates the superiority of NA-noise over other types of noise in data with H<1/2H<1/2. This shows that NANSDE-Net can reproduce not only H>1/2H>1/2 data but also H<1/2H<1/2 data.
However, for data with H<1/2H<1/2, SDE-Net also achieves sufficiently good results, and thus NANSDE-Net cannot be said to perform significantly better.

## 5 Conclusion

Our contributions are as follows:

* •

  We introduce NANSDE-Net, an extension of SDE-Net that incorporates NN-kernel ARMA-type noise.
  The proposed approach is based on the theoretical results presented in [[2](https://arxiv.org/html/2602.08182v1#bib.bib2)] and [[3](https://arxiv.org/html/2602.08182v1#bib.bib3)].
* •

  We prove that the solution of NANSDE exists uniquely under standard Lipschitz and growth conditions, and derive a backpropagation formula for efficient gradient-based training.
* •

  The experimental results demonstrate the ability of NANSDE-Net to accurately reproduce the estimate of the Hurst index and the distribution characteristics of the original time series, particularly in the context of long-memory data.
  Our code is available at <https://github.com/ozhr/ArmaNoise-SDE-Net>.

### Further Study

Since our primary focus is on investigating the role of the noise process in capturing memory characteristics, we deliberately adopt a simple neural network architecture, without attempting to optimize the network design or improve training efficiency.
Accordingly, the experimental performance could potentially be enhanced by employing more advanced network architectures or by designing more effective loss functions.

As discussed in Section [2](https://arxiv.org/html/2602.08182v1#S2 "2 Preliminaries ‣ NANSDE-Net: A NEURAL SDE FRAMEWORK FOR GENERATING TIME SERIES WITH MEMORY"), kernels of the form a​(t)=p(t+1)p+1a(t)=\frac{p}{(t+1)^{p+1}} satisfy the conditions for long-memory.
However, the explicit expression of the corresponding function ℓ​(s,u)\ell(s,u) remains unknown.
Identifying this function constitutes an important direction for future research.
In the present study, we instead approximate ℓ​(s,u)\ell(s,u) by decomposing it as ℓ​(s,u)=ℓ1​(s)​ℓ2​(u)\ell(s,u)=\ell\_{1}(s)\ell\_{2}(u) and learning each component via neural networks.
Nevertheless, this decomposition does not ensure that the resulting process Z​(t)Z(t) has stationary increments.
Therefore, developing neural architectures that can enforce the stationary increment property remains a critical challenge.
If such stationarity is guaranteed, it becomes possible to construct a noise process that is Gaussian, possesses stationary increments, and exhibits memory effects—thus offering a viable alternative to fBm.

Moreover, we observed that NANSDE-Net did not perform well on datasets characterized by very low Hurst indices.
Addressing this issue requires a more comprehensive investigation into the general relationship between ARMA-type noise kernels a​(⋅)a(\cdot) and the Hurst index.
The ultimate goal of this line of research is to identify kernel structures that enable the generation of sample paths, even for time series with low regularity.

### Broader Impact

Fractional Brownian motion (fBm) has traditionally been employed as the primary noise source with memory for modeling time series data exhibiting long- and short-memory behavior across various domains.
However, the findings of this study reveal that alternative noise processes can also capture such memory characteristics. This raises a new question as to whether fBm is indeed the most suitable choice for modeling long- and short-memory phenomena.
In particular, by appropriately designing the kernel function ℓ​(s,u)\ell(s,u) to satisfy stationarity conditions, we demonstrate the existence of stationary-increment Gaussian processes with memory that are distinct from fBm.

{credits}

#### 5.0.1 Acknowledgements

This work was supported by JST BOOST, Japan Grant Number JPMJBS2424.

#### 5.0.2 \discintname

The authors have no competing interests to declare that are relevant to the content of this article.

## References

* [1]

  A. Inoue, S. Moriuchi, Y.N.: A vasicek-type short rate model with memory effect. Stochastic Analysis and Applications 33, 1068–1082 (2015)
* [2]

  Anh, V., Inoue, A.: Financial markets with memory i: Dynamic models. Stochastic Analysis and Applications 23, 275–300 (2005)
* [3]

  Anh, V., Inoue, A.: Financial markets with memory ii: Innovation processes and expected utility maximization. Stochastic Analysis and Applications 23, 301–328 (2005)
* [4]

  Chen, R.T., Rubanova, Y., Bettencourt, J., Duvenaud, D.: Neural ordinary differential equations. In: Advances in Neural Information Processing Systems. pp. 6572–6583 (2018)
* [5]

  Cont, R.: Empirical properties of asset returns: stylized facts and statistical issues. Quantitative finance 1(2),  223 (2001)
* [6]

  Dang, T., Dimitriadis, A., Wu, J., Sethu, V., Ambikairajah, E.: Constrained dynamical neural ode for time series modelling: A case study on continuous emotion prediction. In: ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). pp. 1–5. IEEE (2023)
* [7]

  Gatheral, J., Jaisson, T., Rosenbaum, M.: Volatility is rough. In: Commodities, pp. 659–690. Chapman and Hall/CRC (2022)
* [8]

  Hayashi, K., Nakagawa, K.: Fractional sde-net: Generation of time series data with long-term memory. In: In Proceedings of IEEE International Conference on Data Science and Advanced Analytics. IEEE (2022)
* [9]

  He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image recognition. In: Proceedings of the IEEE conference on computer vision and pattern recognition. pp. 770–778 (2016)
* [10]

  Kidger, P., Foster, J., Li, X., Oberhauser, H., Lyons, T.: Neural sdes as infinite-dimensional gans. arXiv preprint arXiv:2102.03657 (2021)
* [11]

  Kong, L., Sun, J., Zhang, C.: Sde-net: Equipping deep neural networks with uncertainty estimates. In: International Conference on Machine Learning. pp. 5405–5415. PMLR (2020)
* [12]

  Luo, Z., Kamata, S.i., Sun, Z., Zhou, W.: Deep neural networks with flexible complexity while training based on neural ordinary differential equations. In: ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). pp. 1690–1694. IEEE (2021)
* [13]

  Nakagawa, K., Hayashi, K.: Lf-net: Generating fractional time-series with latent fractional-net. In: 2024 International Joint Conference on Neural Networks (IJCNN). pp. 1–8. IEEE (2024)
* [14]

  Strogatz, S.H.: Nonlinear dynamics and chaos: with applications to physics, biology, chemistry, and engineering. CRC press (2018)
* [15]

  Sun, Z., El-Laham, Y., Vyetrenko, S.: Neural stochastic differential equations with change points: A generative adversarial approach. In: ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). pp. 6965–6969. IEEE (2024)
* [16]

  Wu, S., Shi, Z.: Itôwave: Itô stochastic differential equation is all you need for wave generation. In: ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). pp. 8422–8426. IEEE (2022)