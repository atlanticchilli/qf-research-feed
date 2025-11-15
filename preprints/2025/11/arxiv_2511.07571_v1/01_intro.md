---
authors:
- Chen Jin
- Ankush Agarwal
doc_id: arxiv:2511.07571v1
family_id: arxiv:2511.07571
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Forecasting implied volatility surface with generative diffusion models1footnote
  11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm
url_abs: http://arxiv.org/abs/2511.07571v1
url_html: https://arxiv.org/html/2511.07571v1
venue: arXiv q-fin
version: 1
year: 2025
---


Chen JIN
Department of Statistical and Actuarial Sciences, University of Western Ontario, London, ON, Canada. Email: cjin94@uwo.ca; aagarw93@uwo.ca
  
Ankush AGARWAL22footnotemark: 2

###### Abstract

We introduce a conditional Denoising Diffusion Probabilistic Model (DDPM) for
generating arbitrage-free implied volatility (IV) surfaces, offering a more stable and accurate
alternative to existing GAN-based approaches. To capture the path-dependent nature of
volatility dynamics, our model is conditioned on a rich set of market variables, including
exponential weighted moving averages (EWMAs) of historical surfaces, returns and squared
returns of underlying asset, and scalar risk indicators like VIX. Empirical results demonstrate our
model significantly outperforms leading GAN-based models in capturing the stylized facts of IV
dynamics. A key challenge is that historical data often contains small arbitrage opportunities in
the earlier dataset for training, which conflicts with the goal of generating arbitrage-free
surfaces. We address this by incorporating a standard arbitrage penalty into the loss function,
but apply it using a novel, parameter-free weighting scheme based on the signal-to-noise ratio
(SNR) that dynamically adjusts the penalty’s strength across the diffusion process. We
also show a formal analysis of this trade-off and provide a proof of convergence showing that
the penalty introduces a small, controllable bias that steers the model toward the manifold of
arbitrage-free surfaces while ensuring the generated distribution remains close to the real-world data.

Keywords: Implied volatility; Generative diffusion models; Volatility surface; Arbitrage; Forecasting.

## 1 Introduction

The implied volatility (IV) surface summarizes the market’s expectation of future asset price uncertainty, it is central to quantitative finance and risk management. However, modelling and forecasting the IV surface is challenging. A valid surface is not an arbitrary collection of points but must satisfy strict no-arbitrage conditions, such as convexity in strike and non-decreasing behavior in time-to-maturity. These constraints mean that valid IV surfaces form a complex, non-linear, low-dimensional manifold embedded within a high-dimensional Euclidean space. An effective generative model must therefore not only capture the complex stochastic dynamics of the surface but also learn the geometry of this arbitrage-free manifold.

Traditional parametric models such as Heston model (Heston\_1993), often impose rigid structural assumptions that fail to capture the full range of shapes observed in the market. With the availability of more computing resources, recent research has turned to deep generative models to learn the IV surface distribution in a data-driven way. These models are highly capable but can be challenging to train, and may suffer from mode collapse, or can struggle to generate statistically reliable uncertainty estimates. Furthermore, they often require carefully designed loss functions to prevent the generation of financially implausible surfaces with obvious arbitrage.

In this paper, we propose a new framework for this task based on Denoising Diffusion Probabilistic Models (DDPMs). DDPMs, which have demonstrated state-of-the-art performance in high-fidelity image generation, are naturally well-suited for this problem. Their stable training process and ability to learn complex data distributions make them an attractive alternative to generative adversarial networks (GANs). We frame the task of forecasting the one-day-ahead IV surface as a conditional generation problem. We adapt the continuous-time generalization of DDPMs, first proposed by DBLP:journals/corr/abs-2011-13456, by selecting a Variance Preserving (VP) SDE, which is a natural choice for modelling bounded, normalized volatility data. Our model, based on a U-Net architecture (pmlr-v37-sohl-dickstein15), learns to approximate the score function of the data distribution, conditioned on previous market information, including the prior day’s IV surface and scalar market drivers.

Our primary contribution is the design and application of a novel conditional diffusion model (DDPM) for forecasting the implied volatility surface. A key innovation of this model is its composite loss function, which combines the standard noise-matching objective with an explicit financial arbitrage penalty. This penalty is dynamically weighted by the Signal-to-Noise Ratio (SNR) of the current diffusion step. This weighting scheme prevents erratic gradients from high-noise samples from destabilizing training, while still strongly enforcing no-arbitrage constraints as the model generates the clean surface.

Our comprehensive empirical study shows this approach is highly effective. Compared to a GAN based benchmark, our model not only achieves a lower overall Mean Absolute Percentage Error (MAPE) but also produces better uncertainty estimates. The 90% confidence intervals from our model are well-calibrated, with breach rates hovering near the theoretical 10% target, and it generates qualitatively smoother surfaces free of the shape artifacts seen in the output of the GAN based benchmark.

Recent applications of diffusion models to implied volatility surfaces (Hu\_2024\_tech), have demonstrated their potential using synthetic data from models like Heston. These studies leverage clean, abundant Monte Carlo samples from the model to focus on unconditional generation or completion tasks, providing valuable insights into the method’s capabilities. We move beyond using Monte Carlo samples from a specific model to a more challenging problem of one-day-ahead conditional forecasting with real market data and conditions, a more natural SNR-weighted arbitrage penalty, which yields stable and financially valid forecasts in real-world settings.

Second, we provide a theoretical convergence guarantee for our proposed penalized loss function. We show that for a sufficiently small penalty weight λ\lambda, the bias introduced by the arbitrage term is bounded, and the effective score-matching error LeffL^{\text{eff}} converges to the base model error LL with an added bias term of order O​(λ2)O(\lambda^{2}). This result, which leverages a conditional Girsanov theorem and a local strong convexity assumption, provides a convergence proof for a DDPM trained with an explicit financial constraint. This theoretical backing is further supported by recent work from Tang\_Lin\_Yang\_2024, which proves that such conditional models are minimax-optimal for distribution estimation on manifolds.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2511.07571v1#S2 "2 Generative modelling on the Manifold of Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") introduces the generative modelling framework, discussing the manifold of implied volatility surfaces, the forward perturbation process, and the reverse generative SDE. Section [3](https://arxiv.org/html/2511.07571v1#S3 "3 Derivation of the Training Objective ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") provides a formal derivation of the training objective, connecting the theoretical goal via Girsanov’s theorem to a practical noise-prediction loss. Section [4](https://arxiv.org/html/2511.07571v1#S4 "4 Convergence of DDPM with Arbitrage Penalty ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") presents our main theoretical contribution: a convergence proof for the DDPM trained with our explicit arbitrage penalty. Section [5](https://arxiv.org/html/2511.07571v1#S5 "5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") details the practical implementation of our model, including data pre-processing, the conditional U-Net architecture, and our novel SNR-weighted loss function. Section [6](https://arxiv.org/html/2511.07571v1#S6 "6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") provides a comprehensive empirical analysis, comparing our model’s forecasting performance against the VolGAN benchmark in terms of qualitative, quantitative, and distributional fidelity. Section [7](https://arxiv.org/html/2511.07571v1#S7 "7 Conclusion ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") sums up the paper in the nutshell.

## 2 Generative modelling on the Manifold of Implied Volatility Surfaces

### 2.1 The Manifold of Arbitrage-Free Implied Volatility Surfaces

An implied volatility (IV) surface can be represented as a point in a high-dimensional Euclidean space. For a discrete grid of NmN\_{m} moneyness points and NτN\_{\tau} tenors, a single surface is an element x∈ℝNm×Nτx\in\mathbb{R}^{N\_{m}\times N\_{\tau}}. However, this ambient space also contains surfaces that are financially unviable. A valid IV surface must satisfy a set of no-arbitrage conditions, primarily ensuring convexity in strike (to prevent butterfly arbitrage) and non-decreasing behavior in time-to-maturity (to prevent calendar spread arbitrage) (Gatheral\_Jacquier\_2014). These no-arbitrage conditions are given below.

* •

  No Butterfly Arbitrage (Convexity in Strike): The price of a butterfly spread must be non-negative. This implies that call prices must be a convex function of the strike price. For call price c​(m,τ)c(m,\tau) with moneyness mm and time to maturity τ\tau, this continuous theoretical condition is:

  |  |  |  |
  | --- | --- | --- |
  |  | ∂2c​(m,τ)∂m2≥0.\frac{\partial^{2}c(m,\tau)}{\partial m^{2}}\geq 0. |  |

  For a discrete grid of moneyness and time-to-maturity (mi,τj)(m\_{i},\tau\_{j}), this is implemented using a finite-difference approximation to check for convexity:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | c​(mi+1,τj)−c​(mi,τj)mi+1−mi≥c​(mi,τj)−c​(mi−1,τj)mi−mi−1∀i,j.\frac{c(m\_{i+1},\tau\_{j})-c(m\_{i},\tau\_{j})}{m\_{i+1}-m\_{i}}\geq\frac{c(m\_{i},\tau\_{j})-c(m\_{i-1},\tau\_{j})}{m\_{i}-m\_{i-1}}\quad\forall i,j. |  | (1) |
* •

  No Calendar Spread Arbitrage (Non-decreasing in Tenor): The price of a call option must not decrease as time-to-maturity increases. This ensures that a long-dated option is always at least as valuable as a short-dated one with the same strike. The continuous condition is:

  |  |  |  |
  | --- | --- | --- |
  |  | ∂c​(m,τ)∂τ≥0.\frac{\partial c(m,\tau)}{\partial\tau}\geq 0. |  |

  On our discrete grid, this translates to the simple condition:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | c​(mi,τj)≤c​(mi,τj+1)∀i,j​ (where ​τj+1>τj​).c(m\_{i},\tau\_{j})\leq c(m\_{i},\tau\_{j+1})\quad\forall i,j\text{ (where }\tau\_{j+1}>\tau\_{j}\text{)}. |  | (2) |

Clearly, these constraints imply that the set of all valid, arbitrage-free IV surfaces does not fill the ambient space. Instead, they form a lower-dimensional, non-linear manifold, which we denote as ℳ\mathcal{M}, embedded within the higher-dimensional space ℝNm×Nτ\mathbb{R}^{N\_{m}\times N\_{\tau}}. Thus, any generative model must learn the complex geometry of the data manifold ℳ\mathcal{M} while being able to accurately model the stochastic evolution of surfaces on this manifold. Denoising Diffusion Probabilistic Models (DDPMs) provide a powerful, data-driven framework for solving this challenge. The popularity of their application to model complex data distributions is because the model convergence is supported by a theoretical foundation. This convergence was recently established under mild assumptions in the work of (Nakano\_2025).

### 2.2 The Forward Diffusion Process: Perturbation from the Manifold

The first component of a DDPM is the forward process, a fixed procedure that systematically perturbs a data point x0∈ℳx\_{0}\in\mathcal{M} away from the manifold. This process gradually transforms the highly structured data point into a sample from a simple, known prior distribution, typically a standard Gaussian that covers the entire ambient space. The forward process is defined as a discrete-time Markov chain of length TT. At each step t≤Tt\leq T, a small amount of Gaussian noise is added to the data from the previous step, xt−1x\_{t-1}, according to a pre-defined variance schedule {βt}t=1T∈(0,1)\{\beta\_{t}\}\_{t=1}^{T}\in(0,1):

|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(xt|xt−1)=𝒩​(xt;1−βt​xt−1,βt​𝐈).q(x\_{t}|x\_{t-1})=\mathcal{N}(x\_{t};\sqrt{1-\beta\_{t}}x\_{t-1},\beta\_{t}\mathbf{I}). |  | (3) |

A key property of this process is that we can sample xtx\_{t} at any arbitrary timestep tt directly from the initial data point x0x\_{0} in a single step. Letting αt=1−βt\alpha\_{t}=1-\beta\_{t} and α¯t=∏i=1tαi\bar{\alpha}\_{t}=\prod\_{i=1}^{t}\alpha\_{i}, the closed-form relationship is given as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt=α¯t​x0+1−α¯t​ϵ,whereϵ∼𝒩​(0,𝐈).x\_{t}=\sqrt{\bar{\alpha}\_{t}}x\_{0}+\sqrt{1-\bar{\alpha}\_{t}}\bm{\epsilon},\quad\text{where}\quad\bm{\epsilon}\sim\mathcal{N}(0,\mathbf{I}). |  | (4) |

This property is crucial for an efficient training procedure as it allows for random sampling of timesteps without iterating through the entire chain. As t→Tt\to T, the distribution of xTx\_{T} converges to a standard normal distribution since α¯t→0\bar{\alpha}\_{t}\to 0. This effectively erases all information about the original manifold structure.

![Refer to caption](fig/diffusion_process_grid.png)


Figure 1: Diffusion process of the implied volatility.

#### 2.2.1 Terminal Distribution and Approximation Error

A key step in the DDPM framework is the assumption that the terminal distribution of the forward process p​(xT)p(x\_{T}) can be perfectly replaced by a standard isotropic Gaussian, pprior​(xT)=𝒩​(0,𝐈)p\_{\text{prior}}(x\_{T})=\mathcal{N}(0,\mathbf{I}). Here, we quantify the error introduced by this approximation. For a fixed initial data point x0x\_{0}, the true distribution at the final step TT is P1=p​(xT|x0)=𝒩​(α¯T​x0,(1−α¯T)​𝐈)P\_{1}=p(x\_{T}|x\_{0})=\mathcal{N}(\sqrt{\bar{\alpha}\_{T}}x\_{0},(1-\bar{\alpha}\_{T})\mathbf{I}). We compare this to the prior distribution P2=𝒩​(𝟎,𝐈)P\_{2}=\mathcal{N}(\mathbf{0},\mathbf{I}) using the Kullback-Leibler (KL) divergence. The KL divergence between two multivariate Gaussian distributions is given by:

|  |  |  |
| --- | --- | --- |
|  | DK​L​(P1∥P2)=12​(log⁡det𝚺2det𝚺1−d+tr​(𝚺2−1​𝚺1)+(𝝁2−𝝁1)⊤​𝚺2−1​(𝝁2−𝝁1)).D\_{KL}(P\_{1}\|P\_{2})=\frac{1}{2}\left(\log\frac{\det\bm{\Sigma}\_{2}}{\det\bm{\Sigma}\_{1}}-d+\text{tr}(\bm{\Sigma}\_{2}^{-1}\bm{\Sigma}\_{1})+(\bm{\mu}\_{2}-\bm{\mu}\_{1})^{\top}\bm{\Sigma}\_{2}^{-1}(\bm{\mu}\_{2}-\bm{\mu}\_{1})\right). |  |

Substituting the means and covariances of P1P\_{1} and P2P\_{2}, the KL divergence for a given x0x\_{0} is:

|  |  |  |
| --- | --- | --- |
|  | DK​L​(p​(xT|x0)∥pprior​(xT))=d2​(−log⁡(1−α¯T)−α¯T)+α¯T2​‖x0‖2.D\_{KL}(p(x\_{T}|x\_{0})\|p\_{\text{prior}}(x\_{T}))=\frac{d}{2}\left(-\log(1-\bar{\alpha}\_{T})-\bar{\alpha}\_{T}\right)+\frac{\bar{\alpha}\_{T}}{2}\|x\_{0}\|^{2}. |  |

To find the overall expected error, we average this quantity over the entire data distribution pdata​(x0)p\_{\text{data}}(x\_{0}):

|  |  |  |
| --- | --- | --- |
|  | 𝔼x0​[DK​L]=d2​(−log⁡(1−α¯T)−α¯T)+α¯T2​𝔼x0​[‖x0‖2].\mathbb{E}\_{x\_{0}}[D\_{KL}]=\frac{d}{2}\left(-\log(1-\bar{\alpha}\_{T})-\bar{\alpha}\_{T}\right)+\frac{\bar{\alpha}\_{T}}{2}\mathbb{E}\_{x\_{0}}[\|x\_{0}\|^{2}]. |  |

For a sufficiently long diffusion process, α¯T\bar{\alpha}\_{T} is very small. Using the Taylor expansion −log⁡(1−x)−x≈x2/2-\log(1-x)-x\approx x^{2}/2 for small xx, the first term is of order 𝒪​(d​α¯T2)\mathcal{O}(d\bar{\alpha}\_{T}^{2}). If the data is standardized to have approximately unit variance per dimension, then 𝔼​[‖x0‖2]≈d\mathbb{E}[\|x\_{0}\|^{2}]\approx d, making the second term of order 𝒪​(d​α¯T)\mathcal{O}(d\bar{\alpha}\_{T}). The linear term dominates, so the expected KL divergence is bounded by 𝔼x0​[DK​L]≈𝒪​(d​α¯T)\mathbb{E}\_{x\_{0}}[D\_{KL}]\approx\mathcal{O}(d\bar{\alpha}\_{T}).

Finally, applying Pinsker’s inequality, which relates the Total Variation (TV) distance to the KL divergence (DT​V≤12​DK​LD\_{TV}\leq\sqrt{\frac{1}{2}D\_{KL}}), gives the final bound on the terminal error:

|  |  |  |
| --- | --- | --- |
|  | ErrorTerminal=DT​V​(p​(xT),pprior)≤12​𝒪​(d​α¯T)=𝒪​(d​α¯T).\text{Error}\_{\text{Terminal}}=D\_{TV}(p(x\_{T}),p\_{\text{prior}})\leq\sqrt{\frac{1}{2}\mathcal{O}(d\bar{\alpha}\_{T})}=\mathcal{O}(\sqrt{d\bar{\alpha}\_{T}}). |  |

This shows that for a well-designed variance schedule where α¯T→0\bar{\alpha}\_{T}\to 0, the approximation error is controllable and can be made arbitrarily small, thus justifying the use of a standard normal prior in the reverse process.

### 2.3 Continuous-Time Generalization via SDEs

As shown by DBLP:journals/corr/abs-2011-13456, this discrete-step process can be generalized into a more powerful continuous-time framework. When the number of steps T→∞T\to\infty, the discrete chain converges to the solution of a specific Stochastic Differential Equation (SDE). This SDE describes the continuous evolution of the data distribution over time t∈[0,T]t\in[0,T]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝐱=𝐟​(𝐱,t)​d​t+g​(t)​d​𝐰.\displaystyle d\mathbf{x}=\mathbf{f}(\mathbf{x},t)dt+g(t)d\mathbf{w}. |  | (5) |

Here, 𝐟​(𝐱,t)\mathbf{f}(\mathbf{x},t) is the drift coefficient and g​(t)g(t) is the diffusion coefficient. The specific forms of these functions are chosen by the modeler to define the forward process. The two most prominent formulations are:

* •

  Variance Preserving (VP) SDE: This is the direct continuous-time generalization of the DDPM formulation. The drift and diffusion coefficients are defined by a continuous noise schedule β​(t)∈(0,1)\beta(t)\in(0,1) as:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝐟​(𝐱,t)=−12​β​(t)​𝐱andg​(t)=β​(t).\mathbf{f}(\mathbf{x},t)=-\frac{1}{2}\beta(t)\mathbf{x}\quad\text{and}\quad g(t)=\sqrt{\beta(t)}. |  |

  This results in the SDE:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | d​𝐱=−12​β​(t)​𝐱​d​t+β​(t)​d​𝐰.\displaystyle d\mathbf{x}=-\frac{1}{2}\beta(t)\mathbf{x}dt+\sqrt{\beta(t)}d\mathbf{w}. |  | (6) |

  This SDE is designed to keep the variance of the perturbed data bounded.
* •

  Variance Exploding (VE) SDE: This formulation generalizes score-matching models (NCSN). It uses a zero drift and a diffusion coefficient defined by an increasing noise scale σ​(t)\sigma(t):

  |  |  |  |
  | --- | --- | --- |
  |  | 𝐟​(𝐱,t)=𝟎andg​(t)=d​[σ2​(t)]d​t.\mathbf{f}(\mathbf{x},t)=\mathbf{0}\quad\text{and}\quad g(t)=\sqrt{\frac{d[\sigma^{2}(t)]}{dt}}. |  |

  This results in the SDE:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | d​𝐱=d​[σ2​(t)]d​t​d​𝐰,\displaystyle d\mathbf{x}=\sqrt{\frac{d[\sigma^{2}(t)]}{dt}}d\mathbf{w}, |  | (7) |

  where the variance of 𝐱t\mathbf{x}\_{t} grows over time.

Here, σ​(t)\sigma(t) is an increasing function of time that defines the noise scale. This formulation is effective for data where the scale is not necessarily normalized as it focuses on matching the score at different noise levels, regardless of the data’s original variance.

The primary difference between these SDEs lies in how they perturb the data and manage the variance of the resulting distribution.

* •

  VP-SDE ([6](https://arxiv.org/html/2511.07571v1#S2.E6 "In 1st item ‣ 2.3 Continuous-Time Generalization via SDEs ‣ 2 Generative modelling on the Manifold of Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")) perturbs data such that the variance stays roughly constant. It is analogous to corrupting a clean signal with noise while rescaling it to maintain its power.
* •

  VE-SDE ([7](https://arxiv.org/html/2511.07571v1#S2.E7 "In 2nd item ‣ 2.3 Continuous-Time Generalization via SDEs ‣ 2 Generative modelling on the Manifold of Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")) only adds noise, causing the variance to increase over time. This is analogous to corrupting a clean signal with noise of a progressively larger magnitude, which eventually dominates the signal.

Despite these differences in the forward process, the insight from DBLP:journals/corr/abs-2011-13456 is that all of these forward SDEs have a corresponding reverse SDE that depends on the score of the perturbed data distribution, ∇𝐱log⁡pt​(𝐱)\nabla\_{\mathbf{x}}\log p\_{t}(\mathbf{x}). We will introduce the reverse SDE details in Section [2.4](https://arxiv.org/html/2511.07571v1#S2.SS4 "2.4 The Reverse Process: Learning the Drift Towards the Manifold ‣ 2 Generative modelling on the Manifold of Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm"). The choice between these SDE formulations is therefore a critical modelling decision, which depends on the characteristics of the application and data.
The VE-SDE is highly effective for data where the absolute scale is less significant, as it corrupts the signal by adding noise of ever-increasing magnitude. In contrast, the VP-SDE is specifically designed for data that is well-scaled or normalized to a fixed range. It perturbs the data while ensuring its overall variance remains approximately constant throughout the diffusion process.

We use VP-SDE because normalized volatilities are bounded. This simplifies training compared to VE-SDE. This allows the model to focus entirely on learning the structural features of the smile and skew, leading to a more direct and stable learning objective compared to the other choices.

### 2.4 The Reverse Process: Learning the Drift Towards the Manifold

The generative component of the model is the reverse process, which learns to reverse the diffusion. Conceptually, it learns a path from a point of pure noise in the ambient space back towards the data manifold ℳ\mathcal{M}. The model learns the score function toward the high-density regions corresponding to valid IV surfaces.

The feasibility of reversing this process Anderson\_1982 demonstrates that a forward-time SDE has a corresponding reverse-time SDE that describes the same diffusion process but evolving backwards in time. For the forward process described previously in ([5](https://arxiv.org/html/2511.07571v1#S2.E5 "In 2.3 Continuous-Time Generalization via SDEs ‣ 2 Generative modelling on the Manifold of Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")), its reverse is given by:

|  |  |  |
| --- | --- | --- |
|  | d​𝐱=[𝐟​(𝐱,t)−g​(t)2​∇𝐱log⁡pt​(𝐱)]​d​t+g​(t)​d​𝐰¯.d\mathbf{x}=[\mathbf{f}(\mathbf{x},t)-g(t)^{2}\nabla\_{\mathbf{x}}\log p\_{t}(\mathbf{x})]dt+g(t)d\bar{\mathbf{w}}. |  |

Here, d​𝐰¯d\bar{\mathbf{w}} is a standard Wiener process when time flows backwards from TT to 0. The drift term consists of the original forward drift 𝐟​(𝐱,t)\mathbf{f}(\mathbf{x},t) corrected by a crucial term: the gradient of the log-density of the perturbed data, ∇𝐱log⁡pt​(𝐱)\nabla\_{\mathbf{x}}\log p\_{t}(\mathbf{x}). This gradient is known as the score function.

While the reverse SDE provides a theoretical path for generation, it is not immediately computable because it depends on the score of the marginal distributions {pt​(𝐱)}t∈[0,T]\{p\_{t}(\mathbf{x})\}\_{t\in[0,T]}, which are unknown. The core task of the generative model is therefore to learn a time-dependent neural network, 𝐬θ​(𝐱,t)\mathbf{s}\_{\theta}(\mathbf{x},t), to approximate the true score function s∗s^{\*}. For the VP-SDE used in this work, the score function is directly related to the noise component ϵ\bm{\epsilon} from the forward process. This insight allows us to re-parameterize our score model 𝐬θ​(𝐱t,t)\mathbf{s}\_{\theta}(\mathbf{x}\_{t},t) in terms of a neural network ϵθ​(𝐱t,t)\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t) trained to predict the noise from the noisy data. This relationship is given by:

|  |  |  |
| --- | --- | --- |
|  | 𝐬θ​(𝐱t,t)=−ϵθ​(𝐱t,t)1−α¯t.\mathbf{s}\_{\theta}(\mathbf{x}\_{t},t)=-\frac{\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t)}{\sqrt{1-\bar{\alpha}\_{t}}}. |  |

This approach is not only functionally equivalent to learning the score but is often more stable in practice.

As established in the preceding sections, minimizing the KL divergence between the true and model-generated trajectories is equivalent to minimizing a weighted score-matching objective. Through the noise-prediction parameterization shown above, this objective simplifies to the following L2 loss between the true and predicted noise:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒs​i​m​p​l​e=𝔼t,𝐱0,ϵ​[‖ϵ−ϵθ​(𝐱t,t)‖2].\mathcal{L}\_{simple}=\mathbb{E}\_{t,\mathbf{x}\_{0},\bm{\epsilon}}\left[||\bm{\epsilon}-\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t)||^{2}\right]. |  | (8) |

Minimizing this objective effectively trains the score-approximating network. Once trained, the learned function ϵθ\bm{\epsilon}\_{\theta} is used to estimate the score and numerically solve the reverse SDE, generating implied volatility surfaces from pure noise.

## 3 Derivation of the Training Objective

The objective of the generative model is to learn the reverse process that transforms a simple prior distribution into the complex data distribution. This is formally achieved by minimizing the Kullback-Leibler (KL) divergence between the path distribution generated by our model, PθP\_{\theta}, and the true reverse process distribution, QQ.

### 3.1 Theoretical Objective via Girsanov’s Theorem

The KL divergence provides a natural measure of similarity between the two process distributions. For processes defined by Stochastic Differential Equations (SDEs), Girsanov’s theorem offers a direct way to compute this divergence.

Let’s consider the continuous-time reverse SDEs for the true process (driven by the true score s∗s^{\*}) and our parameterized model (driven by the learned score sθs\_{\theta}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | True Process (Q):d​𝐱\displaystyle\text{True Process (Q):}\quad d\mathbf{x} | =[𝐟​(𝐱,t)−g​(t)2​s∗​(𝐱,t)]​d​t+g​(t)​d​𝐰¯\displaystyle=\left[\mathbf{f}(\mathbf{x},t)-g(t)^{2}s^{\*}(\mathbf{x},t)\right]dt+g(t)d\bar{\mathbf{w}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Model Process (Pθ):d​𝐱\displaystyle\text{Model Process ($P\_{\theta}$):}\quad d\mathbf{x} | =[𝐟​(𝐱,t)−g​(t)2​sθ​(𝐱,t)]​d​t+g​(t)​d​𝐰¯.\displaystyle=\left[\mathbf{f}(\mathbf{x},t)-g(t)^{2}s\_{\theta}(\mathbf{x},t)\right]dt+g(t)d\bar{\mathbf{w}}. |  |

The two processes share the same diffusion term g​(t)​d​𝐰¯g(t)d\bar{\mathbf{w}} and differ only in their drift. The difference in drift is given by:

|  |  |  |
| --- | --- | --- |
|  | Drift Difference=[𝐟​(𝐱,t)−g​(t)2​sθ​(𝐱,t)]−[𝐟​(𝐱,t)−g​(t)2​s∗​(𝐱,t)]=g​(t)2​(s∗−sθ).\text{Drift Difference}=\left[\mathbf{f}(\mathbf{x},t)-g(t)^{2}s\_{\theta}(\mathbf{x},t)\right]-\left[\mathbf{f}(\mathbf{x},t)-g(t)^{2}s^{\*}(\mathbf{x},t)\right]=g(t)^{2}(s^{\*}-s\_{\theta}). |  |

Girsanov’s theorem states that the KL divergence between the path measures PθP\_{\theta} and QQ is half the expected squared norm of the drift difference, scaled by the diffusion coefficient and integrated over time:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DK​L​(Pθ∥Q)\displaystyle D\_{KL}(P\_{\theta}\|Q) | =12​𝔼​[∫0T‖g​(t)2​(s∗​(𝐱t,t)−sθ​(𝐱t,t))g​(t)‖2​𝑑t]\displaystyle=\frac{1}{2}\mathbb{E}\left[\int\_{0}^{T}\left\|\frac{g(t)^{2}(s^{\*}(\mathbf{x}\_{t},t)-s\_{\theta}(\mathbf{x}\_{t},t))}{g(t)}\right\|^{2}dt\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​𝔼​[∫0Tg​(t)2​‖s∗​(𝐱t,t)−sθ​(𝐱t,t)‖2​𝑑t].\displaystyle=\frac{1}{2}\mathbb{E}\left[\int\_{0}^{T}g(t)^{2}\|s^{\*}(\mathbf{x}\_{t},t)-s\_{\theta}(\mathbf{x}\_{t},t)\|^{2}dt\right]. |  | (9) |

This fundamental result (Revuz\_Yor\_1999) establishes that minimizing the KL divergence between the process distributions is equivalent to a continuous-time, weighted score-matching objective. This provides the core theoretical justification for the entire training procedure.

### 3.2 Practical Implementation via Noise Prediction

While Girsanov’s theorem provides the theoretically sound objective of matching the score, its practical implementation is enabled by a specific parameterization of the score model. As established in the original DDPM framework (Ho\_Jain\_Abbeel\_2020), the true score of the perturbed data distribution is directly related to the noise ϵ\bm{\epsilon} added during the forward process:

|  |  |  |
| --- | --- | --- |
|  | s∗​(𝐱t,t)=∇𝐱tlog⁡pt​(𝐱t|𝐱0)=−ϵ1−α¯t.s^{\*}(\mathbf{x}\_{t},t)=\nabla\_{\mathbf{x}\_{t}}\log p\_{t}(\mathbf{x}\_{t}|\mathbf{x}\_{0})=-\frac{\bm{\epsilon}}{\sqrt{1-\bar{\alpha}\_{t}}}. |  |

We can therefore parameterize our model’s score sθs\_{\theta} to have the same functional form, using a neural network ϵθ​(𝐱t,t)\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t) to predict the noise ϵ\bm{\epsilon} from the noisy data 𝐱t\mathbf{x}\_{t}:

|  |  |  |
| --- | --- | --- |
|  | sθ​(𝐱t,t)=−ϵθ​(𝐱t,t)1−α¯t.s\_{\theta}(\mathbf{x}\_{t},t)=-\frac{\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t)}{\sqrt{1-\bar{\alpha}\_{t}}}. |  |

Substituting these two expressions into our score-matching objective from Girsanov’s theorem connects the theoretical goal to a practical noise-prediction task. The continuous integral becomes a sum over discrete timesteps, and the objective becomes minimizing:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(θ)\displaystyle L(\theta) | ∝∑t=1Tλ​(t)​𝔼𝐱0,ϵ​[‖−ϵ1−α¯t−(−ϵθ​(𝐱t,t)1−α¯t)‖2]\displaystyle\propto\sum\_{t=1}^{T}\lambda(t)\mathbb{E}\_{\mathbf{x}\_{0},\bm{\epsilon}}\left[\left\|-\frac{\bm{\epsilon}}{\sqrt{1-\bar{\alpha}\_{t}}}-\left(-\frac{\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t)}{\sqrt{1-\bar{\alpha}\_{t}}}\right)\right\|^{2}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∑t=1Tλ​(t)​𝔼𝐱0,ϵ​[11−α¯t​‖ϵ−ϵθ​(𝐱t,t)‖2],\displaystyle=\sum\_{t=1}^{T}\lambda(t)\mathbb{E}\_{\mathbf{x}\_{0},\bm{\epsilon}}\left[\frac{1}{1-\bar{\alpha}\_{t}}\left\|\bm{\epsilon}-\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t)\right\|^{2}\right], |  | (10) |

where λ​(t)\lambda(t) is a positive weighting function derived from the SDE coefficients (e.g., related to g​(t)2g(t)^{2}). As shown by Ho\_Jain\_Abbeel\_2020, empirically dropping this complex weighting term and using a uniform weight leads to a more stable training process and excellent results. This yields the final simplified loss function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lsimple​(θ)=𝔼t,𝐱0,ϵ​[‖ϵ−ϵθ​(α¯t​𝐱0+1−α¯t​ϵ,t)‖2].L\_{\text{simple}}(\theta)=\mathbb{E}\_{t,\mathbf{x}\_{0},\bm{\epsilon}}\left[||\bm{\epsilon}-\bm{\epsilon}\_{\theta}(\sqrt{\bar{\alpha}\_{t}}\mathbf{x}\_{0}+\sqrt{1-\bar{\alpha}\_{t}}\bm{\epsilon},t)||^{2}\right]. |  | (11) |

### 3.3 Adapting for Conditional Dynamics

The unconditional framework derived above is adapted for forecasting via conditional generation. The model is directly conditioned on covariates (prior-day IV surface and scalar drivers) without an external classifier. This aligns with the conditional forward-backward diffusion models analyzed by Tang\_Lin\_Yang\_2024, who proved minimax-optimal convergence rates for such estimators under the total variation metric—extending to manifold adaptation where error bounds depend only on intrinsic data dimensions.

Practically, this is achieved by augmenting the noise prediction network, ϵθ\bm{\epsilon}\_{\theta}, to accept the conditioning vector 𝐜\mathbf{c} as an additional input: ϵθ​(𝐱t,t,𝐜)\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t,\mathbf{c}). The loss function retains its simple mean-squared error form, with the expectation now also taken over the distribution of conditions:

|  |  |  |
| --- | --- | --- |
|  | Lconditional​(θ)=𝔼t,𝐱0,ϵ,𝐜​[‖ϵ−ϵθ​(𝐱t,t,𝐜)‖2].L\_{\text{conditional}}(\theta)=\mathbb{E}\_{t,\mathbf{x}\_{0},\bm{\epsilon},\mathbf{c}}\left[||\bm{\epsilon}-\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t,\mathbf{c})||^{2}\right]. |  |

In our model, the conditioning vector 𝐜\mathbf{c} includes the previous day’s surfaces and scalar drivers derived from parametric models, which enables the model to capture stochastic evolutions on the arbitrage-free manifold. We will elaborate on the condition details later in Section [5.2](https://arxiv.org/html/2511.07571v1#S5.SS2 "5.2 Conditional U-Net Architecture and Conditioning ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm").

## 4 Convergence of DDPM with Arbitrage Penalty

The proof proceeds in three main parts:

1. 1.

   We first analyze the bias introduced by the arbitrage penalty term in the loss function, using a local strong convexity assumption.
2. 2.

   We then use a conditional version of the Girsanov theorem to relate the error in the learned score function to the KL Divergence between the generated and true data paths.
3. 3.

   Finally, we combine these results with standard DDPM error terms (discretization and terminal errors) to derive a comprehensive bound on the TV distance, leveraging Pinsker’s inequality (chen2025diffusionfactormodelsgenerating; Tsybakov\_2009).

### 4.1 Notation

* •

  Data distribution: μdata​(𝐱∣𝐜)\mu\_{\text{data}}(\mathbf{x}\mid\mathbf{c}), where 𝐱∈ℝd\mathbf{x}\in\mathbb{R}^{d} is the vectorized IV surface (d=81d=81), and 𝐜\mathbf{c} is the conditioning information.
* •

  Forward process: 𝐱t=α¯t​𝐱0+1−α¯t​ϵ\mathbf{x}\_{t}=\sqrt{\bar{\alpha}\_{t}}\mathbf{x}\_{0}+\sqrt{1-\bar{\alpha}\_{t}}\epsilon, for ϵ∼𝒩​(0,I)\epsilon\sim\mathcal{N}(0,I) and t=1,…,nt=1,\dots,n.
* •

  Model: A U-Net with parameters θ\theta that predicts noise ϵ^θ​(𝐱t,t,𝐜)\hat{\epsilon}\_{\theta}(\mathbf{x}\_{t},t,\mathbf{c}).
* •

  Score Functions: The true score is s∗​(𝐱t,t,𝐜)=∇𝐱tlog⁡pt​(𝐱t∣𝐜)s^{\*}(\mathbf{x}\_{t},t,\mathbf{c})=\nabla\_{\mathbf{x}\_{t}}\log p\_{t}(\mathbf{x}\_{t}\mid\mathbf{c}). The model’s score is sθs\_{\theta}.
* •

  Loss Function: ℒ​(θ)=ℒMSE​(θ)+λ​ℒarb​(θ)\mathcal{L}(\theta)=\mathcal{L}\_{\text{MSE}}(\theta)+\lambda\mathcal{L}\_{\text{arb}}(\theta), where ℒMSE=𝔼​[‖ϵ−ϵ^θ‖2]\mathcal{L}\_{\text{MSE}}=\mathbb{E}[\|\epsilon-\hat{\epsilon}\_{\theta}\|^{2}] and ℒarb\mathcal{L}\_{\text{arb}} is the arbitrage penalty.

### 4.2 Assumptions

The following assumptions are required for the proof to hold.

###### Assumption 4.1 (Bounded Data and Scores).

The Implied volatility data and conditioning information are bounded in Euclidean norm by constants M𝐱M\_{\mathbf{x}} and M𝐜M\_{\mathbf{c}}. The true conditional score s∗​(𝐱t,t,𝐜)s^{\*}(\mathbf{x}\_{t},t,\mathbf{c}) is KK-Lipschitz with respect to its data input 𝐱t\mathbf{x}\_{t} and exhibits at most linear growth, satisfying:

|  |  |  |
| --- | --- | --- |
|  | ‖s∗​(𝐱t,t,𝐜)‖≤K​(1+‖𝐱t‖),\|s^{\*}(\mathbf{x}\_{t},t,\mathbf{c})\|\leq K(1+\|\mathbf{x}\_{t}\|), |  |

for a positive constant KK.

###### Assumption 4.2 (Variance Schedule).

The variance schedule {βt}t=1n\{\beta\_{t}\}\_{t=1}^{n} is chosen such that βt∈(0,1)\beta\_{t}\in(0,1) for all tt, and for a sufficiently large number of steps nn, we have βt=O​(1/n)\beta\_{t}=O(1/n).

###### Assumption 4.3 (Model Capacity and Regularity).

The U-Net is designed to have sufficient capacity to approximate the true score function, such that the optimal population MSE loss, L=infθℒMSE​(θ)L=\inf\_{\theta}\mathcal{L}\_{\text{MSE}}(\theta), can be theoretically close to zero. Furthermore, the learned score function sθ​(𝐱t,t,𝐜)s\_{\theta}(\mathbf{x}\_{t},t,\mathbf{c}) is assumed to be LθL\_{\theta}-Lipschitz with respect to its data input 𝐱t\mathbf{x}\_{t}.

###### Assumption 4.4 (Arbitrage Penalty).

The penalty function ℒarb​(𝐱)\mathcal{L}\_{\text{arb}}(\mathbf{x}) is BB-Lipschitz with respect to its input 𝐱\mathbf{x}. This implies that its gradient with respect to 𝐱\mathbf{x} is bounded by a constant BB:

|  |  |  |
| --- | --- | --- |
|  | ‖∇𝐱ℒarb​(𝐱)‖≤B.\|\nabla\_{\mathbf{x}}\mathcal{L}\_{\text{arb}}(\mathbf{x})\|\leq B. |  |

Furthermore, we assume the gradient of the full penalty term with respect to the model parameters θ\theta is bounded. This gradient can be analyzed via the chain rule:

|  |  |  |
| --- | --- | --- |
|  | ∇θ𝔼​[ℒarb​(𝐱^0​(θ))]=𝔼​[∇𝐱ℒarb​(𝐱^0​(θ))⋅∇θ𝐱^0​(θ)].\nabla\_{\theta}\mathbb{E}[\mathcal{L}\_{\text{arb}}(\hat{\mathbf{x}}\_{0}(\theta))]=\mathbb{E}[\nabla\_{\mathbf{x}}\mathcal{L}\_{\text{arb}}(\hat{\mathbf{x}}\_{0}(\theta))\cdot\nabla\_{\theta}\hat{\mathbf{x}}\_{0}(\theta)]. |  |

We assume the denoised estimate 𝐱^0​(θ)\hat{\mathbf{x}}\_{0}(\theta) is LθL\_{\theta}-Lipschitz with respect to the parameters θ\theta. This allows us to bound the norm of the full gradient as:

|  |  |  |
| --- | --- | --- |
|  | ‖∇θ𝔼​[ℒarb​(𝐱^0​(θ))]‖≤𝔼​[‖∇𝐱ℒarb‖⋅‖∇θ𝐱^0‖]≤B⋅Lθ.\|\nabla\_{\theta}\mathbb{E}[\mathcal{L}\_{\text{arb}}(\hat{\mathbf{x}}\_{0}(\theta))]\|\leq\mathbb{E}[\|\nabla\_{\mathbf{x}}\mathcal{L}\_{\text{arb}}\|\cdot\|\nabla\_{\theta}\hat{\mathbf{x}}\_{0}\|]\leq B\cdot L\_{\theta}. |  |

###### Assumption 4.5 (Local Strong Convexity).

The MSE loss, ℒMSE\mathcal{L}\_{\text{MSE}}, is η\eta-strongly convex within a ball of radius RR around its minimizer θ0\theta\_{0}.

###### Theorem 4.6 (Main Convergence Result).

Under Assumptions 1 through 5, the distribution p​(𝐱0∗∣𝐜)p(\mathbf{x}\_{0}^{\*}\mid\mathbf{c}) generated by the reverse process is close to the true data distribution μdata(⋅∣𝐜)\mu\_{\text{data}}(\cdot\mid\mathbf{c}). Their Total Variation distance is bounded by:

|  |  |  |
| --- | --- | --- |
|  | DTV​(μdata,pθ)≤𝒪​(d​α¯n)⏟Terminal Error+𝒪​(n)⋅(L+O​(λ2))⏟Accumulated Score Error+𝒪​(1n)⏟Discretization Error,D\_{\text{TV}}(\mu\_{\text{data}},p\_{\theta})\leq\underbrace{\mathcal{O}(\sqrt{d\bar{\alpha}\_{n}})}\_{\text{Terminal Error}}+\underbrace{\sqrt{\mathcal{O}(n)\cdot(L+O(\lambda^{2}))}}\_{\text{Accumulated Score Error}}+\underbrace{\mathcal{O}\left(\frac{1}{n}\right)}\_{\text{Discretization Error}}, |  |

where LL is the base population MSE score error and O​(λ2)O(\lambda^{2}) is the bias introduced by the arbitrage penalty.

The probability density function (PDF) for p​(𝐱t|𝐱0)p(\mathbf{x}\_{t}|\mathbf{x}\_{0}) is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(𝐱t|𝐱0)=1(2​π​(1−α¯t))d/2​exp⁡(−‖𝐱t−α¯t​𝐱0‖22​(1−α¯t)).p(\mathbf{x}\_{t}|\mathbf{x}\_{0})=\frac{1}{(2\pi(1-\bar{\alpha}\_{t}))^{d/2}}\exp\left(-\frac{||\mathbf{x}\_{t}-\sqrt{\bar{\alpha}\_{t}}\mathbf{x}\_{0}||^{2}}{2(1-\bar{\alpha}\_{t})}\right). |  | (12) |

The conditional score function is the gradient of the log of this PDF with respect to the noisy data, 𝐱t\mathbf{x}\_{t}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∇𝐱tln⁡p​(𝐱t|𝐱0)\displaystyle\nabla\_{\mathbf{x}\_{t}}\ln p(\mathbf{x}\_{t}|\mathbf{x}\_{0}) | =∇𝐱t(const−‖𝐱t−α¯t​𝐱0‖22​(1−α¯t))\displaystyle=\nabla\_{\mathbf{x}\_{t}}\left(\text{const}-\frac{||\mathbf{x}\_{t}-\sqrt{\bar{\alpha}\_{t}}\mathbf{x}\_{0}||^{2}}{2(1-\bar{\alpha}\_{t})}\right) |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−12​(1−α¯t)⋅2​(𝐱t−α¯t​𝐱0)\displaystyle=-\frac{1}{2(1-\bar{\alpha}\_{t})}\cdot 2(\mathbf{x}\_{t}-\sqrt{\bar{\alpha}\_{t}}\mathbf{x}\_{0}) |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−𝐱t−α¯t​𝐱01−α¯t.\displaystyle=-\frac{\mathbf{x}\_{t}-\sqrt{\bar{\alpha}\_{t}}\mathbf{x}\_{0}}{1-\bar{\alpha}\_{t}}. |  | (15) |

By rearranging the forward process equation, we know that 𝐱t−α¯t​𝐱0=1−α¯t​ϵ\mathbf{x}\_{t}-\sqrt{\bar{\alpha}\_{t}}\mathbf{x}\_{0}=\sqrt{1-\bar{\alpha}\_{t}}\bm{\epsilon}. Substituting this in gives the crucial relationship between the conditional score and the noise:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇𝐱tln⁡p​(𝐱t|𝐱0)=−ϵ1−α¯t.\nabla\_{\mathbf{x}\_{t}}\ln p(\mathbf{x}\_{t}|\mathbf{x}\_{0})=-\frac{\bm{\epsilon}}{\sqrt{1-\bar{\alpha}\_{t}}}. |  | (16) |

However, in practice, a diffusion model does not know the original clean data 𝐱0\mathbf{x}\_{0} when it sees a noisy sample 𝐱t\mathbf{x}\_{t}. Therefore, the model cannot learn the conditional score. Instead, it must learn the marginal score, ∇𝐱tln⁡p​(𝐱t)\nabla\_{\mathbf{x}\_{t}}\ln p(\mathbf{x}\_{t}), which is averaged over all possible starting data points.
The marginal probability distribution of a noisy sample, p​(𝐱t)p(\mathbf{x}\_{t}), is given by integrating the conditional probability over the entire original data distribution, pdata​(𝐱0)p\_{\text{data}}(\mathbf{x}\_{0}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(𝐱t)=∫p​(𝐱t|𝐱0)​pdata​(𝐱0)​𝑑𝐱0.p(\mathbf{x}\_{t})=\int p(\mathbf{x}\_{t}|\mathbf{x}\_{0})p\_{\text{data}}(\mathbf{x}\_{0})d\mathbf{x}\_{0}. |  | (17) |

This means the probability of seeing a specific noisy sample 𝐱t\mathbf{x}\_{t} is the sum of probabilities of starting with any possible clean sample 𝐱0\mathbf{x}\_{0} and adding noise to it.

The objective of score matching is to train a network sθ​(𝐱t,t)s\_{\theta}(\mathbf{x}\_{t},t) to match the true marginal score by minimizing the expected squared error:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒscore​(θ)=𝔼t,𝐱t∼pt​(⋅)​[‖sθ​(𝐱t,t)−∇𝐱tln⁡pt​(𝐱t)‖2].\mathcal{L}\_{\text{score}}(\theta)=\mathbb{E}\_{t,\mathbf{x}\_{t}\sim p\_{t}(\cdot)}\left[||s\_{\theta}(\mathbf{x}\_{t},t)-\nabla\_{\mathbf{x}\_{t}}\ln p\_{t}(\mathbf{x}\_{t})||^{2}\right]. |  | (18) |

Expanding the squared term gives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒscore=𝔼​[‖sθ‖2]−2​𝔼​[sθ⊤​∇𝐱tln⁡pt​(𝐱t)]+𝔼​[‖∇𝐱tln⁡pt​(𝐱t)‖2].\mathcal{L}\_{\text{score}}=\mathbb{E}[||s\_{\theta}||^{2}]-2\mathbb{E}[s\_{\theta}^{\top}\nabla\_{\mathbf{x}\_{t}}\ln p\_{t}(\mathbf{x}\_{t})]+\mathbb{E}[||\nabla\_{\mathbf{x}\_{t}}\ln p\_{t}(\mathbf{x}\_{t})||^{2}]. |  | (19) |

The last term, 𝔼​[‖∇𝐱tln⁡pt​(𝐱t)‖2]\mathbb{E}[||\nabla\_{\mathbf{x}\_{t}}\ln p\_{t}(\mathbf{x}\_{t})||^{2}], does not depend on the model parameters θ\theta and can be ignored during optimization. The crucial insight of score matching is that the middle term, 𝔼​[sθ⊤​∇𝐱tln⁡pt​(𝐱t)]\mathbb{E}[s\_{\theta}^{\top}\nabla\_{\mathbf{x}\_{t}}\ln p\_{t}(\mathbf{x}\_{t})], which depends on the intractable marginal score, can be replaced with an equivalent expression that depends only on the tractable conditional score, ∇𝐱tln⁡p​(𝐱t|𝐱0)\nabla\_{\mathbf{x}\_{t}}\ln p(\mathbf{x}\_{t}|\mathbf{x}\_{0}).

We can show this by proving that both terms simplify to the same expression using integration by parts. Let’s start with the intractable marginal score term:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼𝐱t​[sθ⊤​∇𝐱tln⁡pt​(𝐱t)]\displaystyle\mathbb{E}\_{\mathbf{x}\_{t}}[s\_{\theta}^{\top}\nabla\_{\mathbf{x}\_{t}}\ln p\_{t}(\mathbf{x}\_{t})] | =∫pt​(𝐱t)​sθ​(𝐱t,t)⊤​∇𝐱tpt​(𝐱t)pt​(𝐱t)​𝑑𝐱t\displaystyle=\int p\_{t}(\mathbf{x}\_{t})s\_{\theta}(\mathbf{x}\_{t},t)^{\top}\frac{\nabla\_{\mathbf{x}\_{t}}p\_{t}(\mathbf{x}\_{t})}{p\_{t}(\mathbf{x}\_{t})}d\mathbf{x}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫sθ​(𝐱t,t)⊤​∇𝐱tpt​(𝐱t)​𝑑𝐱t.\displaystyle=\int s\_{\theta}(\mathbf{x}\_{t},t)^{\top}\nabla\_{\mathbf{x}\_{t}}p\_{t}(\mathbf{x}\_{t})d\mathbf{x}\_{t}. |  |

Applying integration by parts and assuming boundary terms vanish as ‖𝐱t‖→∞||\mathbf{x}\_{t}||\to\infty (since ptp\_{t} is a probability density), this becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | =−∫pt​(𝐱t)​∇𝐱t⋅sθ​(𝐱t,t)​𝑑𝐱t=−𝔼𝐱t​[∇𝐱t⋅sθ​(𝐱t,t)].=-\int p\_{t}(\mathbf{x}\_{t})\nabla\_{\mathbf{x}\_{t}}\cdot s\_{\theta}(\mathbf{x}\_{t},t)d\mathbf{x}\_{t}=-\mathbb{E}\_{\mathbf{x}\_{t}}[\nabla\_{\mathbf{x}\_{t}}\cdot s\_{\theta}(\mathbf{x}\_{t},t)]. |  | (20) |

where ∇⋅sθ\nabla\cdot s\_{\theta} is the divergence of the vector field sθs\_{\theta}.

Now, let’s look at the tractable conditional score term from the denoising objective:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼𝐱0,𝐱t​[sθ⊤​∇𝐱tln⁡p​(𝐱t|𝐱0)]\displaystyle\mathbb{E}\_{\mathbf{x}\_{0},\mathbf{x}\_{t}}[s\_{\theta}^{\top}\nabla\_{\mathbf{x}\_{t}}\ln p(\mathbf{x}\_{t}|\mathbf{x}\_{0})] | =∫pdata​(𝐱0)​[∫p​(𝐱t|𝐱0)​sθ​(𝐱t,t)⊤​∇𝐱tln⁡p​(𝐱t|𝐱0)​𝑑𝐱t]​𝑑𝐱0\displaystyle=\int p\_{\text{data}}(\mathbf{x}\_{0})\left[\int p(\mathbf{x}\_{t}|\mathbf{x}\_{0})s\_{\theta}(\mathbf{x}\_{t},t)^{\top}\nabla\_{\mathbf{x}\_{t}}\ln p(\mathbf{x}\_{t}|\mathbf{x}\_{0})d\mathbf{x}\_{t}\right]d\mathbf{x}\_{0} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫pdata​(𝐱0)​[∫sθ​(𝐱t,t)⊤​∇𝐱tp​(𝐱t|𝐱0)​𝑑𝐱t]​𝑑𝐱0.\displaystyle=\int p\_{\text{data}}(\mathbf{x}\_{0})\left[\int s\_{\theta}(\mathbf{x}\_{t},t)^{\top}\nabla\_{\mathbf{x}\_{t}}p(\mathbf{x}\_{t}|\mathbf{x}\_{0})d\mathbf{x}\_{t}\right]d\mathbf{x}\_{0}. |  |

Applying integration by parts to the inner integral (with respect to 𝐱t\mathbf{x}\_{t}) again gives:

|  |  |  |
| --- | --- | --- |
|  | =∫pdata​(𝐱0)​[−∫p​(𝐱t|𝐱0)​∇𝐱t⋅sθ​(𝐱t,t)​𝑑𝐱t]​𝑑𝐱0\displaystyle=\int p\_{\text{data}}(\mathbf{x}\_{0})\left[-\int p(\mathbf{x}\_{t}|\mathbf{x}\_{0})\nabla\_{\mathbf{x}\_{t}}\cdot s\_{\theta}(\mathbf{x}\_{t},t)d\mathbf{x}\_{t}\right]d\mathbf{x}\_{0} |  |
|  |  |  |
| --- | --- | --- |
|  | =−𝔼𝐱0,𝐱t​[∇𝐱t⋅sθ​(𝐱t,t)]\displaystyle=-\mathbb{E}\_{\mathbf{x}\_{0},\mathbf{x}\_{t}}[\nabla\_{\mathbf{x}\_{t}}\cdot s\_{\theta}(\mathbf{x}\_{t},t)] |  |
|  |  |  |
| --- | --- | --- |
|  | =−𝔼𝐱t​[∇𝐱t⋅sθ​(𝐱t,t)].\displaystyle=-\mathbb{E}\_{\mathbf{x}\_{t}}[\nabla\_{\mathbf{x}\_{t}}\cdot s\_{\theta}(\mathbf{x}\_{t},t)]. |  |

Since both the intractable marginal term and the tractable conditional term simplify to the same expression (Equation [20](https://arxiv.org/html/2511.07571v1#S4.E20 "In 4.2 Assumptions ‣ 4 Convergence of DDPM with Arbitrage Penalty ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")), they are equivalent. Therefore, we can replace the intractable marginal score in the loss function with the tractable conditional score, which is the key to making score matching practical.

The equivalence can be shown by starting with the practical score-matching objective, which minimizes the expected squared L2 norm between the model’s score sθs\_{\theta} and the true conditional score ∇𝐱tln⁡p​(𝐱t|𝐱0)\nabla\_{\mathbf{x}\_{t}}\ln p(\mathbf{x}\_{t}|\mathbf{x}\_{0}). Let’s denote the true score as s∗s^{\*}. The objective is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒSM​(θ)=𝔼t,𝐱0,ϵ​[‖sθ​(𝐱t,t)−s∗​(𝐱t)‖2].\mathcal{L}\_{\text{SM}}(\theta)=\mathbb{E}\_{t,\mathbf{x}\_{0},\bm{\epsilon}}\left[\|s\_{\theta}(\mathbf{x}\_{t},t)-s^{\*}(\mathbf{x}\_{t})\|^{2}\right]. |  | (21) |

We use the common parameterization for the model’s score, sθ​(𝐱t,t)=−ϵ^θ​(𝐱t,t)1−α¯ts\_{\theta}(\mathbf{x}\_{t},t)=-\frac{\hat{\bm{\epsilon}}\_{\theta}(\mathbf{x}\_{t},t)}{\sqrt{1-\bar{\alpha}\_{t}}}, and the known relationship for the true score, s∗​(𝐱t)=∇𝐱tln⁡p​(𝐱t|𝐱0)=−ϵ1−α¯ts^{\*}(\mathbf{x}\_{t})=\nabla\_{\mathbf{x}\_{t}}\ln p(\mathbf{x}\_{t}|\mathbf{x}\_{0})=-\frac{\bm{\epsilon}}{\sqrt{1-\bar{\alpha}\_{t}}}. Substituting these into the objective gives the precise relationship:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒSM​(θ)\displaystyle\mathcal{L}\_{\text{SM}}(\theta) | =𝔼t,𝐱0,ϵ​[‖−ϵ^θ1−α¯t−(−ϵ1−α¯t)‖2]\displaystyle=\mathbb{E}\_{t,\mathbf{x}\_{0},\bm{\epsilon}}\left[\left\|-\frac{\hat{\bm{\epsilon}}\_{\theta}}{\sqrt{1-\bar{\alpha}\_{t}}}-\left(-\frac{\bm{\epsilon}}{\sqrt{1-\bar{\alpha}\_{t}}}\right)\right\|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼t,𝐱0,ϵ​[‖11−α¯t​(ϵ−ϵ^θ)‖2]\displaystyle=\mathbb{E}\_{t,\mathbf{x}\_{0},\bm{\epsilon}}\left[\left\|\frac{1}{\sqrt{1-\bar{\alpha}\_{t}}}(\bm{\epsilon}-\hat{\bm{\epsilon}}\_{\theta})\right\|^{2}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼t,𝐱0,ϵ​[11−α¯t​‖ϵ−ϵ^θ‖2].\displaystyle=\mathbb{E}\_{t,\mathbf{x}\_{0},\bm{\epsilon}}\left[\frac{1}{1-\bar{\alpha}\_{t}}\|\bm{\epsilon}-\hat{\bm{\epsilon}}\_{\theta}\|^{2}\right]. |  | (22) |

Multiplying both sides by 𝔼t​[1−α¯t]\mathbb{E}\_{t}[1-\bar{\alpha}\_{t}] and recognizing that the score-matching term ℒSM\mathcal{L}\_{\text{SM}} can be written as an expectation over 𝐱t\mathbf{x}\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[(1−α¯t)​𝔼𝐱t​[‖sθ​(𝐱t,t)−s∗​(𝐱t)‖2]]=𝔼t,𝐱0,ϵ​[‖ϵ−ϵ^θ‖2].\mathbb{E}\_{t}\left[(1-\bar{\alpha}\_{t})\mathbb{E}\_{\mathbf{x}\_{t}}\left[\|s\_{\theta}(\mathbf{x}\_{t},t)-s^{\*}(\mathbf{x}\_{t})\|^{2}\right]\right]=\mathbb{E}\_{t,\mathbf{x}\_{0},\bm{\epsilon}}\left[\|\bm{\epsilon}-\hat{\bm{\epsilon}}\_{\theta}\|^{2}\right]. |  | (23) |

Let the average population score error be L=1n​∑t=1n𝔼​‖sθ−s∗‖2L=\frac{1}{n}\sum\_{t=1}^{n}\mathbb{E}\|s\_{\theta}-s^{\*}\|^{2}.
The full loss function, ℒ​(θ)=ℒMSE​(θ)+λ​ℒarb​(θ)\mathcal{L}(\theta)=\mathcal{L}\_{\text{MSE}}(\theta)+\lambda\mathcal{L}\_{\text{arb}}(\theta), contains arbitrage penalty. Note that the implied volatility dataset is not guaranteed to be arbitrage-free, minimizing ℒarb​(θ)\mathcal{L}\_{\text{arb}}(\theta) will contradict the pure MSE loss, even through the penalty is intentionally designed to guide the model towards financially plausible solutions. Now we show the size of this bias is bounded.

Let θ0\theta\_{0} be the ideal set of parameters that minimizes the pure MSE loss, and let θ∗\theta^{\*} be the actual parameters found by minimizing our full, penalized loss function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ0\displaystyle\theta\_{0} | =arg⁡minθ⁡ℒMSE​(θ),\displaystyle=\arg\min\_{\theta}\mathcal{L}\_{\text{MSE}}(\theta), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θ∗\displaystyle\theta^{\*} | =arg⁡minθ⁡ℒ​(θ)=arg⁡minθ⁡[ℒMSE​(θ)+λ​ℒarb​(θ)].\displaystyle=\arg\min\_{\theta}\mathcal{L}(\theta)=\arg\min\_{\theta}\left[\mathcal{L}\_{\text{MSE}}(\theta)+\lambda\mathcal{L}\_{\text{arb}}(\theta)\right]. |  |

We will now prove that the distance between these two parameter sets, ‖θ∗−θ0‖||\theta^{\*}-\theta\_{0}||, is small and controlled by the penalty strength λ\lambda.

###### Lemma 4.7 (Bias Bound under Local Convexity).

Let the MSE loss, ℒMSE\mathcal{L}\_{\text{MSE}}, be η\eta-strongly convex in a ball of radius RR around its minimizer θ0\theta\_{0} (Assumption 5). Let the gradient of the arbitrage penalty be bounded such that ‖∇θℒarb‖≤B​Lθ\|\nabla\_{\theta}\mathcal{L}\_{\text{arb}}\|\leq BL\_{\theta} (Assumption 4).

Then, for a sufficiently small penalty strength λ\lambda such that λ≤η​RB​Lθ\lambda\leq\frac{\eta R}{BL\_{\theta}}, the new minimizer θ∗\theta^{\*} also lies within this convex ball, and the following bound holds:

|  |  |  |
| --- | --- | --- |
|  | ‖θ∗−θ0‖≤λ​B​Lθη.\|\theta^{\*}-\theta\_{0}\|\leq\frac{\lambda BL\_{\theta}}{\eta}. |  |

###### Proof.

First, we derive a bound on the distance ‖θ∗−θ0‖\|\theta^{\*}-\theta\_{0}\| under the working assumption that θ∗\theta^{\*} lies within the η\eta-strongly convex ball around θ0\theta\_{0}. Second, we use this derived bound to demonstrate that the condition on λ\lambda given in the lemma is precisely the condition required to guarantee our working assumption holds.

The minimizers θ0\theta\_{0} and θ∗\theta^{\*} are defined by the zero-gradient condition on their respective loss functions:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∇ℒMSE​(θ0)\displaystyle\nabla\mathcal{L}\_{\text{MSE}}(\theta\_{0}) | =0,\displaystyle=0, |  | (24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∇ℒ​(θ∗)=∇ℒMSE​(θ∗)+λ​∇ℒarb​(θ∗)\displaystyle\nabla\mathcal{L}(\theta^{\*})=\nabla\mathcal{L}\_{\text{MSE}}(\theta^{\*})+\lambda\nabla\mathcal{L}\_{\text{arb}}(\theta^{\*}) | =0.\displaystyle=0. |  | (25) |

From Equation [25](https://arxiv.org/html/2511.07571v1#S4.E25 "In 4.2 Assumptions ‣ 4 Convergence of DDPM with Arbitrage Penalty ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm"), we can express the gradient of the MSE at the new optimum as:

|  |  |  |
| --- | --- | --- |
|  | ∇ℒMSE​(θ∗)=−λ​∇ℒarb​(θ∗).\nabla\mathcal{L}\_{\text{MSE}}(\theta^{\*})=-\lambda\nabla\mathcal{L}\_{\text{arb}}(\theta^{\*}). |  |

By Assumption 5, ℒMSE\mathcal{L}\_{\text{MSE}} is η\eta-strongly convex in a ball of radius RR around θ0\theta\_{0}. Assuming θ∗\theta^{\*} also lies within this ball, we can apply the definition of strong convexity with points a=θ∗a=\theta^{\*} and b=θ0b=\theta\_{0}:

|  |  |  |
| --- | --- | --- |
|  | ⟨∇ℒMSE​(θ∗)−∇ℒMSE​(θ0),θ∗−θ0⟩≥η​‖θ∗−θ0‖2.\langle\nabla\mathcal{L}\_{\text{MSE}}(\theta^{\*})-\nabla\mathcal{L}\_{\text{MSE}}(\theta\_{0}),\theta^{\*}-\theta\_{0}\rangle\geq\eta||\theta^{\*}-\theta\_{0}||^{2}. |  |

Substituting the zero-gradient condition from Equation [24](https://arxiv.org/html/2511.07571v1#S4.E24 "In 4.2 Assumptions ‣ 4 Convergence of DDPM with Arbitrage Penalty ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") and our expression for ∇ℒMSE​(θ∗)\nabla\mathcal{L}\_{\text{MSE}}(\theta^{\*}):

|  |  |  |
| --- | --- | --- |
|  | ⟨−λ​∇ℒarb​(θ∗)−0,θ∗−θ0⟩≥η​‖θ∗−θ0‖2.\langle-\lambda\nabla\mathcal{L}\_{\text{arb}}(\theta^{\*})-0,\theta^{\*}-\theta\_{0}\rangle\geq\eta||\theta^{\*}-\theta\_{0}||^{2}. |  |

Next, we apply the Cauchy-Schwarz inequality (|⟨u,v⟩|≤‖u‖⋅‖v‖|\langle u,v\rangle|\leq||u||\cdot||v||) to the left-hand side, which provides an upper bound:

|  |  |  |
| --- | --- | --- |
|  | λ​‖∇ℒarb​(θ∗)‖⋅‖θ∗−θ0‖≥|⟨−λ​∇ℒarb​(θ∗),θ∗−θ0⟩|≥η​‖θ∗−θ0‖2.\lambda||\nabla\mathcal{L}\_{\text{arb}}(\theta^{\*})||\cdot||\theta^{\*}-\theta\_{0}||\geq|\langle-\lambda\nabla\mathcal{L}\_{\text{arb}}(\theta^{\*}),\theta^{\*}-\theta\_{0}\rangle|\geq\eta||\theta^{\*}-\theta\_{0}||^{2}. |  |

Assuming a non-trivial penalty (λ>0\lambda>0 and ∇ℒarb​(θ∗)≠0\nabla\mathcal{L}\_{\text{arb}}(\theta^{\*})\neq 0), we must have θ∗≠θ0\theta^{\*}\neq\theta\_{0}. We can therefore divide the inequality by the non-zero term ‖θ∗−θ0‖||\theta^{\*}-\theta\_{0}||:

|  |  |  |
| --- | --- | --- |
|  | λ​‖∇ℒarb​(θ∗)‖≥η​‖θ∗−θ0‖.\lambda||\nabla\mathcal{L}\_{\text{arb}}(\theta^{\*})||\geq\eta||\theta^{\*}-\theta\_{0}||. |  |

Rearranging to isolate the distance and applying Assumption 4 (||∇θℒarb∥≤BLθ||\nabla\_{\theta}\mathcal{L}\_{\text{arb}}\|\leq BL\_{\theta}) gives our desired bound on the parameter shift:

|  |  |  |
| --- | --- | --- |
|  | ‖θ∗−θ0‖≤λη​‖∇ℒarb​(θ∗)‖≤λ​B​Lθη.||\theta^{\*}-\theta\_{0}||\leq\frac{\lambda}{\eta}||\nabla\mathcal{L}\_{\text{arb}}(\theta^{\*})||\leq\frac{\lambda BL\_{\theta}}{\eta}. |  |

Now, we confirm the condition under which our initial assumption—that θ∗\theta^{\*} lies within the convex ball of radius RR—is valid. This requires ‖θ∗−θ0‖≤R||\theta^{\*}-\theta\_{0}||\leq R. By substituting the bound we just derived, we find the constraint on λ\lambda:

|  |  |  |
| --- | --- | --- |
|  | λ​B​Lθη≤R⟹λ≤η​RB​Lθ.\frac{\lambda BL\_{\theta}}{\eta}\leq R\implies\lambda\leq\frac{\eta R}{BL\_{\theta}}. |  |

Therefore, for any penalty strength λ\lambda satisfying this constraint, our new optimum θ∗\theta^{\*} is guaranteed to remain in the local convex region, and the bias bound holds.
∎

###### Corollary 4.8 (Effective Score Error).

The total error we aim to bound is the expected squared distance between the score of our actual, trained model (sθ∗s\_{\theta^{\*}}) and the true score (s∗s^{\*}).

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖sθ∗−s∗‖2\displaystyle\mathbb{E}\|s\_{\theta^{\*}}-s^{\*}\|^{2} | =𝔼​‖(sθ∗−sθ0)+(sθ0−s∗)‖2\displaystyle=\mathbb{E}\|(s\_{\theta^{\*}}-s\_{\theta\_{0}})+(s\_{\theta\_{0}}-s^{\*})\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2⋅𝔼​‖sθ∗−sθ0‖2+2⋅𝔼​‖sθ0−s∗‖2.\displaystyle\leq 2\cdot\mathbb{E}\|s\_{\theta^{\*}}-s\_{\theta\_{0}}\|^{2}+2\cdot\mathbb{E}\|s\_{\theta\_{0}}-s^{\*}\|^{2}. |  |

We now analyze these two terms separately.

##### The Base Model Error

The second term, 𝔼​‖sθ0−s∗‖2\mathbb{E}\|s\_{\theta\_{0}}-s^{\*}\|^{2}, represents the error between the ideal model trained only on the MSE loss and the true score. This is, by definition, the best possible population MSE score error that the model architecture can achieve. We denote this irreducible error as LL:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖sθ0−s∗‖2:=L.\mathbb{E}\|s\_{\theta\_{0}}-s^{\*}\|^{2}:=L. |  |

##### The Bias Error

The first term, 𝔼​‖sθ∗−sθ0‖2\mathbb{E}\|s\_{\theta^{\*}}-s\_{\theta\_{0}}\|^{2}, represents the additional error introduced purely by the arbitrage penalty. It measures how far the penalty pushes our model’s solution away from the ideal MSE solution. We can bound this term using the result from our Bias Bound Lemma. The lemma states that the distance between the parameters is bounded:

|  |  |  |
| --- | --- | --- |
|  | ‖θ∗−θ0‖≤λ​B​Lθη.\|\theta^{\*}-\theta\_{0}\|\leq\frac{\lambda BL\_{\theta}}{\eta}. |  |

Furthermore, we assume our score function is KK-Lipschitz with respect to its parameters (‖sθa−sθb‖≤K​‖θa−θb‖\|s\_{\theta\_{a}}-s\_{\theta\_{b}}\|\leq K\|\theta\_{a}-\theta\_{b}\|). Applying this, we can bound the bias error in the score space:

|  |  |  |
| --- | --- | --- |
|  | ‖sθ∗−sθ0‖≤K⋅‖θ∗−θ0‖≤K⋅λ​B​Lθη.\|s\_{\theta^{\*}}-s\_{\theta\_{0}}\|\leq K\cdot\|\theta^{\*}-\theta\_{0}\|\leq K\cdot\frac{\lambda BL\_{\theta}}{\eta}. |  |

Squaring this gives the bound on the expected squared bias error:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖sθ∗−sθ0‖2≤(K​λ​B​Lθη)2.\mathbb{E}\|s\_{\theta^{\*}}-s\_{\theta\_{0}}\|^{2}\leq\left(K\frac{\lambda BL\_{\theta}}{\eta}\right)^{2}. |  |

##### Assembling the Final Bound

Finally, we substitute these two results back into our original inequality. We will absorb the constant factor of 2 into the Big-O notation for simplicity.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖sθ∗−s∗‖2\displaystyle\mathbb{E}\|s\_{\theta^{\*}}-s^{\*}\|^{2} | ≤2⋅𝔼​‖sθ0−s∗‖2⏟Base Error+2⋅𝔼​‖sθ∗−sθ0‖2⏟Bias Error\displaystyle\leq 2\cdot\underbrace{\mathbb{E}\|s\_{\theta\_{0}}-s^{\*}\|^{2}}\_{\text{Base Error}}+2\cdot\underbrace{\mathbb{E}\|s\_{\theta^{\*}}-s\_{\theta\_{0}}\|^{2}}\_{\text{Bias Error}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤L+O​((λ​B​Lθη)2​K2).\displaystyle\leq L+O\left(\left(\frac{\lambda BL\_{\theta}}{\eta}\right)^{2}K^{2}\right). |  |

We define this entire upper bound as the effective score error, LeffL^{\text{eff}}. For simplicity in the final theorem, this is often approximated as L+O​(λ2)L+O(\lambda^{2}), as the other terms are treated as constants.

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖sθ∗−s∗‖2≤L+O​((λ​B​Lθ/η)2​K2):=Leff≈L+O​(λ2).\mathbb{E}\|s\_{\theta^{\*}}-s^{\*}\|^{2}\leq L+O\left((\lambda BL\_{\theta}/\eta)^{2}K^{2}\right):=L^{\text{eff}}\approx L+O(\lambda^{2}). |  |

Having bounded the effective score error of our model, we now assemble the final convergence guarantee. Our approach is to bound the Total Variation (DTVD\_{\text{TV}}) distance between the true conditional data distribution and our generated distribution by decomposing it into three distinct sources of error, which we analyze in turn,

|  |  |  |  |
| --- | --- | --- | --- |
|  | DTV​(Pd​a​t​a,Pθ)≤ErrorTerminal+ErrorScore+ErrorDiscretization.D\_{\text{TV}}(P\_{data},P\_{\theta})\leq\text{Error}\_{\text{Terminal}}+\text{Error}\_{\text{Score}}+\text{Error}\_{\text{Discretization}}. |  | (26) |

The first term, the Terminal Error, arises because the forward process does not perfectly reach a standard normal distribution in a finite number of steps, nn. This error is bounded by the TV distance between the true distribution at step nn, q​(𝐱n∣𝐱0)q(\mathbf{x}\_{n}\mid\mathbf{x}\_{0}), and the standard normal distribution 𝒩​(0,I)\mathcal{N}(0,I) that we sample from to start the reverse process. This error is known to be bounded by 𝒪​(d​α¯n)\mathcal{O}(\sqrt{d\bar{\alpha}\_{n}}).

The second and most significant term, the Accumulated Score Error, results from the fact that our learned score function sθs\_{\theta} is only an approximation of the true score s∗s^{\*}. We connect this score error to the final distribution error using two key theoretical tools. First, the Girsanov theorem for discrete-time diffusion (stated in our lemma) relates the KL Divergence between the true and generated paths to the sum of the per-step score errors:

|  |  |  |
| --- | --- | --- |
|  | DK​L​(Pθ​‖Q∣​𝐜)≈n2​Leff.D\_{KL}(P\_{\theta}\|Q\mid\mathbf{c})\approx\frac{n}{2}L^{\text{eff}}. |  |

Second, we apply Pinsker’s inequality (DT​V≤12​DK​LD\_{TV}\leq\sqrt{\frac{1}{2}D\_{KL}}) to convert this KL divergence bound into a bound on the TV distance, which gives us:

|  |  |  |
| --- | --- | --- |
|  | ErrorScore≤12​DK​L≈n4​Leff=n4​(L+O​(λ2)).\text{Error}\_{\text{Score}}\leq\sqrt{\frac{1}{2}D\_{KL}}\approx\sqrt{\frac{n}{4}L^{\text{eff}}}=\sqrt{\frac{n}{4}(L+O(\lambda^{2}))}. |  |

The third term, the Discretization Error, arises from approximating a continuous-time process with a discrete number of steps. This error accumulates over the nn steps of the reverse chain and is typically bounded by 𝒪​(1/n)\mathcal{O}(1/n) for a well-chosen variance schedule.

## 5 Procedure to Simulate Implied Volatility Surfaces

This section details the practical implementation of our conditional diffusion model for simulating implied volatility surfaces. We outline the key procedural steps, starting with the necessary data cleaning and pre-processing. We then describe the specific conditioning variables used to guide the generation process and the methods for incorporating them. Following this, we specify the neural network architecture chosen for the score approximation. Finally, we detail the procedures adopted for training the model and sampling procedure, arbitrage-aware implied volatility surfaces.

### 5.1 Data Representation and Pre-Processing

We use the Option Prices file provided by OptionMetrics, spanning the period from January 4, 1996, to August 31, 2023. The dataset is split chronologically: the initial 80% serves as the training set, the subsequent 10% constitutes the validation set, and the final 10% is reserved as the out-of-sample test set.

For each trading day within the sample period, we construct an implied volatility (IV) surface. Following standard practice, we focus on out-of-the-money (OTM) options to mitigate the liquidity biases often present in in-the-money options. Specifically, for options where the strike price KK is less than the underlying spot price SS, we utilize put option data; conversely, where K>SK>S, we use call option data. To ensure data quality, options with zero trading volume are excluded due to potential pricing inaccuracies.

The constructed IV surfaces are defined over a discrete grid (𝐦,τ)(\mathbf{m},\mathbf{\tau}) consisting of moneyness levels

|  |  |  |
| --- | --- | --- |
|  | 𝐦∈{0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4},\displaystyle\mathbf{m}\in\{0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4\}, |  |

and times-to-maturity (in years)

|  |  |  |
| --- | --- | --- |
|  | τ∈{1/252,1/52,2/52,1/12,1/6,1/4,1/2,3/4,1},\displaystyle\mathbf{\tau}\in\{1/252,1/52,2/52,1/12,1/6,1/4,1/2,3/4,1\}, |  |

where m=K/Sm=K/S. This grid provides comprehensive coverage of the typical volatility smile and term structure.

Raw implied volatilities derived from market prices often exhibit noise and may not form a smooth surface. So, we apply a non-parametric smoothing technique based on the Vega-weighted Nadaraya-Watson kernel estimator, consistent with methodologies proposed by Cont\_Da\_Fonseca\_2002 and applied in recent generative modelling work (Vuletić\_Cont\_2024). Given observed implied volatilities σ​(m,τ)\sigma(m,\tau) and their corresponding option Greek vega, Vega​(m,τ)\text{Vega}(m,\tau) for various (m,τ)(m,\tau) pairs on a given day, the smoothed implied volatility σ^​(m′,τ′)\hat{\sigma}(m^{\prime},\tau^{\prime}) at a target grid point (m′,τ′)(m^{\prime},\tau^{\prime}) is estimated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ^​(m′,τ′)=∑m∈𝐌,τ∈𝐓Vega​(m,τ)​k​(m−m′,τ−τ′)​σ​(m,τ)∑m∈𝐌,τ∈𝐓Vega​(m,τ)​k​(m−m′,τ−τ′),\hat{\sigma}(m^{\prime},\tau^{\prime})=\frac{\sum\_{m\in\mathbf{M},\tau\in\mathbf{T}}\text{Vega}(m,\tau)k(m-m^{\prime},\tau-\tau^{\prime})\sigma(m,\tau)}{\sum\_{m\in\mathbf{M},\tau\in\mathbf{T}}\text{Vega}(m,\tau)k(m-m^{\prime},\tau-\tau^{\prime})}, |  | (27) |

where 𝐌\mathbf{M} and 𝐓\mathbf{T} represent the sets of available moneyness and tenor points for that day, respectively. The function k​(x,y)k(x,y) is a two-dimensional Gaussian kernel:

|  |  |  |  |
| --- | --- | --- | --- |
|  | k​(x,y)=12​π​exp⁡[−x22​h1−y22​h2].k(x,y)=\frac{1}{2\pi}\exp\left[-\frac{x^{2}}{2h\_{1}}-\frac{y^{2}}{2h\_{2}}\right]. |  | (28) |

The bandwidth hyperparameters, h1h\_{1} (for moneyness) and h2h\_{2} (for time-to-maturity), control the degree of smoothing, and are chosen based on the benchmark study of (Vuletić\_Cont\_2024) (h1=0.002,h2=0.046h\_{1}=0.002,h\_{2}=0.046).

##### Quantifying Arbitrage Violations.

To evaluate the financial plausibility of the surfaces and potentially penalize arbitrage during model training, we quantify arbitrage violations following Vuletić\_Cont\_2024. First, relative call prices c​(m,τ)c(m,\tau) are calculated from the implied volatilities σ​(m,τ)\sigma(m,\tau) using the Black-Scholes formula CB​SC\_{BS} normalized by the spot price SS:

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(m,τ):=1S​CB​S​(S,K,τ,σ​(m,τ),r,q)=N​(d1)−m​e−r​τ​N​(d2),c(m,\tau):=\frac{1}{S}C\_{BS}(S,K,\tau,\sigma(m,\tau),r,q)=N(d\_{1})-me^{-r\tau}N(d\_{2}), |  | (29) |

where m=K/Sm=K/S is the moneyness, rr is the risk-free rate, qq is the dividend yield (assumed zero here for simplicity), and d1,d2d\_{1},d\_{2} are the standard Black-Scholes terms incorporating σ​(m,τ)\sigma(m,\tau).

The total arbitrage penalty Φ​(σ​(𝐦,τ))\Phi(\sigma(\mathbf{m},\mathbf{\tau})) for a discrete surface is then defined as the sum of penalties for violations of calendar spread, call spread, and butterfly spread no-arbitrage conditions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(σ​(𝐦,τ))=p1​(σ​(𝐦,τ))+p2​(σ​(𝐦,τ))+p3​(σ​(𝐦,τ)),\displaystyle\Phi(\sigma(\mathbf{m},\mathbf{\tau}))=p\_{1}(\sigma(\mathbf{m},\mathbf{\tau}))+p\_{2}(\sigma(\mathbf{m},\mathbf{\tau}))+p\_{3}(\sigma(\mathbf{m},\mathbf{\tau})), |  | (30) |

where (⋅)+=max⁡(0,⋅)(\cdot)^{+}=\max(0,\cdot), and the individual penalty terms sum the magnitude of violations across the grid (i=1..Nm,j=1..Nτi=1..N\_{m},j=1..N\_{\tau}):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p1​(σ​(𝐦,τ))\displaystyle p\_{1}(\sigma(\mathbf{m},\mathbf{\tau})) | =∑i=1Nm∑j=1Nτ−1(c​(mi,τj)−c​(mi,τj+1)τj+1−τj)+,\displaystyle=\sum\_{i=1}^{N\_{m}}\sum\_{j=1}^{N\_{\tau}-1}\left(\frac{c(m\_{i},\tau\_{j})-c(m\_{i},\tau\_{j+1})}{\tau\_{j+1}-\tau\_{j}}\right)^{+}, |  | (31) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p2​(σ​(𝐦,τ))\displaystyle p\_{2}(\sigma(\mathbf{m},\mathbf{\tau})) | =∑i=1Nm−1∑j=1Nτ(c​(mi+1,τj)−c​(mi,τj)mi+1−mi)+,\displaystyle=\sum\_{i=1}^{N\_{m}-1}\sum\_{j=1}^{N\_{\tau}}\left(\frac{c(m\_{i+1},\tau\_{j})-c(m\_{i},\tau\_{j})}{m\_{i+1}-m\_{i}}\right)^{+}, |  | (32) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p3​(σ​(𝐦,τ))\displaystyle p\_{3}(\sigma(\mathbf{m},\mathbf{\tau})) | =∑i=2Nm−1∑j=1Nτ(c​(mi,τj)−c​(mi−1,τj)mi−mi−1−c​(mi+1,τj)−c​(mi,τj)mi+1−mi)+.\displaystyle=\sum\_{i=2}^{N\_{m}-1}\sum\_{j=1}^{N\_{\tau}}\left(\frac{c(m\_{i},\tau\_{j})-c(m\_{i-1},\tau\_{j})}{m\_{i}-m\_{i-1}}-\frac{c(m\_{i+1},\tau\_{j})-c(m\_{i},\tau\_{j})}{m\_{i+1}-m\_{i}}\right)^{+}. |  | (33) |

Here, p1p\_{1} measures calendar spread arbitrage (decreasing call price with time), p2p\_{2} measures call spread arbitrage (negative slope vs. strike, should be ≤0\leq 0), and p3p\_{3} measures butterfly arbitrage (lack of convexity vs. strike).

![Refer to caption](fig/arbitrage.png)


Figure 2: Arbitrage level of processed dataset from 1996-2023.

##### Data Normalization and Transformation.

Raw implied volatility surfaces exhibit specific statistical properties, such as strict positivity and varying ranges across different moneyness and tenor points, which can pose challenges for direct modelling with neural networks. To prepare the data for the diffusion model and facilitate stable and effective training, we apply a two-step transformation and normalization procedure.

First, we transform the smoothed implied volatility data into log space. Let σ^i​j(k)\hat{\sigma}\_{ij}^{(k)} denote the smoothed implied volatility at moneyness mim\_{i} and tenor τj\tau\_{j} on day kk. We compute the log-volatility zi​j(k)=log⁡(σ^i​j(k))z\_{ij}^{(k)}=\log(\hat{\sigma}\_{ij}^{(k)}) and predict the one-day ahead surfaces in the log-space. To acquire the actual surfaces, we will reverse the transformation by taking the exponential function and the exponential function naturally ensures the positivity of the generated volatilities. It also often helps in stabilizing variance and symmetrizing the distribution of volatility values across the surface, making the data more amenable to modelling assumptions implicit in the diffusion framework.

Second, we normalize the log-transformed data using grid-point-specific statistics derived from the training dataset to prevent any look-ahead bias. For each grid point (i,j)(i,j), we calculate the mean μi​j\mu\_{ij} and standard deviation σi​j\sigma\_{ij} of the log-volatilities {zi​j(k)}\{z\_{ij}^{(k)}\} across all days kk in the training set. This yields a mean surface 𝝁∈ℝNm×Nτ\bm{\mu}\in\mathbb{R}^{N\_{m}\times N\_{\tau}} and a standard deviation surface 𝝈n​o​r​m∈ℝNm×Nτ\bm{\sigma}\_{norm}\in\mathbb{R}^{N\_{m}\times N\_{\tau}} (using 𝝈n​o​r​m\bm{\sigma}\_{norm} to avoid confusion with implied volatility σ\sigma). As illustrated in Figure [3](https://arxiv.org/html/2511.07571v1#S5.F3 "Figure 3 ‣ Data Normalization and Transformation. ‣ 5.1 Data Representation and Pre-Processing ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm"), the standard deviation varies considerably across the surface, with values differing by nearly a factor of two, which strongly motivates the per-cell normalization approach. The final normalized input z~i​j(k)\tilde{z}\_{ij}^{(k)} for the diffusion model is then obtained by standardizing the log-volatility at each grid point:

|  |  |  |  |
| --- | --- | --- | --- |
|  | z~i​j(k)=zi​j(k)−μi​jσn​o​r​m,i​j.\tilde{z}\_{ij}^{(k)}=\frac{z\_{ij}^{(k)}-\mu\_{ij}}{\sigma\_{norm,ij}}. |  | (34) |

This normalization ensures that the input data for the diffusion model has approximately zero mean and unit variance at each grid point within the training set. Such standardization is standard practice in deep learning as it generally leads to more stable gradient updates and faster convergence. It also ensures that different parts of the volatility surface contribute more equally to the model’s loss function during training, preventing regions with intrinsically higher volatility from dominating the learning process. Furthermore, scaling the data to resemble a standard normal distribution aligns well with the target prior distribution of the forward diffusion process.

The same mean surface 𝝁\bm{\mu} and standard deviation surface 𝝈n​o​r​m\bm{\sigma}\_{norm} computed from the training data are subsequently used to normalize the validation and test datasets. After generating new surfaces in the normalized log-space using the trained diffusion model, the output must be transformed back to the original implied volatility scale by first multiplying by σn​o​r​m,i​j\sigma\_{norm,ij}, then adding μi​j\mu\_{ij}, and finally applying the exponential function.

![Refer to caption](fig/std.png)


Figure 3: Standard Deviation Surface calculated from log-implied volatilities in the training dataset.

![Refer to caption](fig/mean.png)


Figure 4: Mean Surface calculated from log-implied volatilities in the training dataset.

### 5.2 Conditional U-Net Architecture and Conditioning

The core of our diffusion model is the neural network ϵθ​(𝐱t,t,𝐜)\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t,\mathbf{c}) trained to predict the noise component ϵ\bm{\epsilon} from the noisy implied volatility surface 𝐱t\mathbf{x}\_{t} at timestep tt, given the conditioning information 𝐜\mathbf{c}. We employ a U-Net architecture (Ronneberger\_Fischer\_Brox\_2015), a model widely effective in image generation tasks with diffusion models (Ho\_Jain\_Abbeel\_2020; DBLP:journals/corr/abs-2011-13456). The U-Net’s structure, featuring an encoder-decoder path with skip connections, is particularly well-suited for processing the grid-like, spatial nature of our 9×99\times 9 implied volatility surfaces, allowing it to capture features at multiple scales while preserving fine-grained details necessary for reconstruction.

To enable conditional forecasting and properly account for the diffusion process, this standard U-Net architecture is augmented in two key ways: through a multi-channel input tensor incorporating historical surface data, and through the injection of temporal and scalar market context into the network’s intermediate layers.

First, instead of feeding only the single-channel noisy target surface 𝐱t\mathbf{x}\_{t} (shape 1×9×91\times 9\times 9), we provide the U-Net with richer spatial context by using a 4×9×94\times 9\times 9 input tensor. The four channels represent:

* •

  the current day’s (day kk) smoothed, transformed, and normalized IV surface 𝐳~(k)\tilde{\mathbf{z}}^{(k)},
* •

  a short-term EWMA of past surfaces (5 days span),
* •

  a long-term EWMA of past surfaces (20 days span),
* •

  the noisy target surface 𝐱t\mathbf{x}\_{t} itself.

This allows the initial convolutional layers to directly process the surface’s recent history and current state alongside the primary denoising target.

Second, the model must be informed by the current diffusion timestep tt and relevant scalar market indicators reflecting broader market dynamics. The timestep tt is first transformed into a high-dimensional embedding vector (e.g., using sinusoidal embeddings (Vaswani\_Shazeer\_Parmar\_Uszkoreit\_Jones\_Gomez\_Kaiser\_Polosukhin\_2023)). Concurrently, we construct a 5-dimensional conditioning vector 𝐜(k)\mathbf{c}^{(k)} for day kk. This vector includes four Exponentially Weighted Moving Averages (EWMAs) derived from the underlying asset’s historical daily returns (rir\_{i}) and squared returns (ri2r\_{i}^{2}), along with the daily return of the VIX index. The EWMA for a time series {yi}\{y\_{i}\} with smoothing factor α\alpha is calculated recursively as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​W​M​Ak=α⋅yk+(1−α)⋅E​W​M​Ak−1EWMA\_{k}=\alpha\cdot y\_{k}+(1-\alpha)\cdot EWMA\_{k-1} |  | (35) |

Inspired by (Gazzani\_Guyon\_2025), the specific components of 𝐜(k)\mathbf{c}^{(k)} are:

* •

  Short-term EWMA of returns (yi=riy\_{i}=r\_{i}), calculated using αt​r​e​n​d,s​h​o​r​t=0.156\alpha\_{trend,short}=0.156.
* •

  Long-term EWMA of returns (yi=riy\_{i}=r\_{i}), calculated using αt​r​e​n​d,l​o​n​g=0.118\alpha\_{trend,long}=0.118.
* •

  Short-term EWMA of squared returns (yi=ri2y\_{i}=r\_{i}^{2}), calculated using αv​o​l,s​h​o​r​t=0.3\alpha\_{vol,short}=0.3.
* •

  Long-term EWMA of squared returns (yi=ri2y\_{i}=r\_{i}^{2}), calculated using αv​o​l,l​o​n​g=0.15\alpha\_{vol,long}=0.15.
* •

  The daily percentage return of the VIX index for day kk.

These specific α\alpha values are chosen based on parameters calibrated in related literature. Before being used, these five scalar features are standardized only on the training portion of the data.

Both the time embedding and the standardized scalar conditioning vector 𝐜(k)\mathbf{c}^{(k)} are then injected into the U-Net’s hidden layers using the Feature-wise Linear Modulation (FiLM) technique (Perez\_Strub\_Vries\_Dumoulin\_Courville\_2017). Following each convolutional block in the U-Net, the time embedding and 𝐜(k)\mathbf{c}^{(k)} are jointly processed by a small feed-forward network (2 hidden layers with 10 neurons each, followed by SiLU activations). The output is linearly projected to produce two vectors, 𝜸\bm{\gamma} (scaling) and 𝜷\bm{\beta} (shifting), whose dimensions match the number of channels in the convolutional block’s output feature map 𝐅\mathbf{F}. These vectors then modulate the feature map element-wise:

|  |  |  |  |
| --- | --- | --- | --- |
|  | FiLM​(𝐅∣𝜸,𝜷)=𝜸⊙𝐅+𝜷,\text{FiLM}(\mathbf{F}\mid\bm{\gamma},\bm{\beta})=\bm{\gamma}\odot\mathbf{F}+\bm{\beta}, |  | (36) |

where ⊙\odot denotes element-wise multiplication broadcast across spatial dimensions. This mechanism allows the timestep and scalar market context to adaptively influence the feature representations at multiple levels of the network, guiding the denoising process towards a temporally consistent and market-aware IV surface prediction. The Figure [5](https://arxiv.org/html/2511.07571v1#S5.F5 "Figure 5 ‣ 5.2 Conditional U-Net Architecture and Conditioning ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") visualizes the overall architecture framework, the model inputs and output are shown in blue and yellow respectively.

![Refer to caption](fig/arch.png)


Figure 5: Architecture of the diffusion model.

For our specific implementation, the U-Net architecture is designed to map the 4-channel input tensor (4×9×94\times 9\times 9) to a single-channel output (1×9×91\times 9\times 9) representing the predicted noise. The encoder path begins with 16 encoding channels (enc\_channels), expanding to 30 channels (bottle\_channels) in the bottleneck. The sinusoidal time embedding and the scalar MLP each produce a 10-dimensional vector, which are concatenated to form a total 24-dimensional embedding (emb\_dim). The feed-forward network within the FiLM block that processes this joint embedding consists of 2 hidden layers with 10 neurons each, using a SiLU activation function. The 5 scalar conditioning features 𝐜(k)\mathbf{c}^{(k)} are constructed using the α\alpha parameters αt​r​e​n​d,s​h​o​r​t=0.156\alpha\_{trend,short}=0.156, αt​r​e​n​d,l​o​n​g=0.118\alpha\_{trend,long}=0.118, αv​o​l,s​h​o​r​t=0.3\alpha\_{vol,short}=0.3, and αv​o​l,l​o​n​g=0.15\alpha\_{vol,long}=0.15, plus the daily VIX return.

### 5.3 Training and Sampling Algorithm

This subsection outlines the specific procedures for training the conditional U-Net model and subsequently using it to generate novel implied volatility surfaces, incorporating the arbitrage penalty.

#### 5.3.1 Loss Function

The model is trained by minimizing a loss function ℒ​(θ)\mathcal{L}(\theta) with two goals: fidelity to the real data distribution and adherence to financial plausibility through no-arbitrage constraints. Simply adding a fixed arbitrage penalty to the standard Mean Squared Error (MSE) loss can lead to instabilities during training, primarily due to imbalance between the MSE loss and the arbitrage penalty term.

The loss function combines the standard Denoising Score Matching (DSM) objective with a dynamically weighted arbitrage penalty term:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(θ)=ℒMSE​(θ)+λ​ℒarb, weighted​(θ).\displaystyle\mathcal{L}(\theta)=\mathcal{L}\_{\text{MSE}}(\theta)+\lambda\mathcal{L}\_{\text{arb, weighted}}(\theta). |  | (37) |

The MSE Loss term ℒMSE​(θ)\mathcal{L}\_{\text{MSE}}(\theta) remains the standard objective focused on learning the data distribution by matching the noise added during the forward process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒMSE​(θ)=𝔼t,𝐱0,ϵ,𝐜​[‖ϵ−ϵθ​(𝐱t,t,𝐜)‖2],\displaystyle\mathcal{L}\_{\text{MSE}}(\theta)=\mathbb{E}\_{t,\mathbf{x}\_{0},\bm{\epsilon},\mathbf{c}}\left[||\bm{\epsilon}-\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t,\mathbf{c})||^{2}\right], |  | (38) |

where 𝐱0=𝐳~(k)\mathbf{x}\_{0}=\tilde{\mathbf{z}}^{(k)} is the normalized log-volatility surface, 𝐱t\mathbf{x}\_{t} is its noisy version at timestep t∈{1,…,n}t\in\{1,...,n\}, ϵ∼𝒩​(0,𝐈)\bm{\epsilon}\sim\mathcal{N}(0,\mathbf{I}) is the true noise, 𝐜\mathbf{c} is the conditioning vector, and ϵθ\bm{\epsilon}\_{\theta} is the noise predicted by the U-Net. While alternative weighting schemes for the MSE loss exist, such as min-SNR weighting (Hang\_Gu\_Li\_Bao\_Chen\_Hu\_Geng\_Guo\_2024), our empirical results indicated that the standard, unweighted MSE loss ([38](https://arxiv.org/html/2511.07571v1#S5.E38 "In 5.3.1 Loss Function ‣ 5.3 Training and Sampling Algorithm ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")) performed better for this application and required less hyperparameter tuning.

The Arbitrage Penalty term, however, requires careful consideration. This penalty is applied to the model’s estimate of the original clean surface, 𝐱^0​(θ)\hat{\mathbf{x}}\_{0}(\theta), obtained via denoising:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱^0​(θ)=1α¯t​(𝐱t−1−α¯t​ϵθ​(𝐱t,t,𝐜)).\displaystyle\hat{\mathbf{x}}\_{0}(\theta)=\frac{1}{\sqrt{\bar{\alpha}\_{t}}}\left(\mathbf{x}\_{t}-\sqrt{1-\bar{\alpha}\_{t}}\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t,\mathbf{c})\right). |  | (39) |

The reliability of this estimate 𝐱^0\hat{\mathbf{x}}\_{0} varies significantly with the timestep tt. When tt is large (i.e., at high noise levels, typically encountered early in the reverse diffusion process and frequently during training), 𝐱t\mathbf{x}\_{t} is mostly noise, and the resulting 𝐱^0\hat{\mathbf{x}}\_{0} is a highly inaccurate approximation of the true 𝐱0\mathbf{x}\_{0}. Applying the arbitrage penalty Φ\Phi (defined in Eqs. [31](https://arxiv.org/html/2511.07571v1#S5.E31 "In Quantifying Arbitrage Violations. ‣ 5.1 Data Representation and Pre-Processing ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")-[33](https://arxiv.org/html/2511.07571v1#S5.E33 "In Quantifying Arbitrage Violations. ‣ 5.1 Data Representation and Pre-Processing ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")) to the corresponding volatility surface σ^=InvTransform​(𝐱^0​(θ))\hat{\sigma}=\text{InvTransform}(\hat{\mathbf{x}}\_{0}(\theta)) in these high-noise regimes can yield large and potentially misleading penalty values. If this unreliably large penalty were added directly to the MSE loss with a fixed weight λ\lambda, it could easily overpower the MSE term, destabilizing training and diverting the model from accurately learning the underlying data distribution. The model might learn to produce noisy, low-arbitrage surfaces early on, hindering its ability to match the true data structure.

Conversely, when tt is small (low noise levels, encountered late in the reverse process and less frequently during uniform time sampling in training), the estimate 𝐱^0\hat{\mathbf{x}}\_{0} is much closer to the true clean surface. Applying the arbitrage penalty in this regime is highly meaningful, as it directly encourages the final generated surface to satisfy no-arbitrage conditions. To dynamically balance the influence of the arbitrage penalty according to the reliability of the denoised estimate, we weight the penalty term by the Signal-to-Noise Ratio (SNR) at timestep tt, defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wS​N​R​(t)=α¯t1−α¯t+ϵs​t​a​b,\displaystyle w\_{SNR}(t)=\frac{\bar{\alpha}\_{t}}{1-\bar{\alpha}\_{t}+\epsilon\_{stab}}, |  | (40) |

where ϵs​t​a​b\epsilon\_{stab} is a small constant (e.g., 10−810^{-8}) for numerical stability. The SNR is inherently high when the signal component (α¯t​𝐱0\sqrt{\bar{\alpha}\_{t}}\mathbf{x}\_{0}) dominates (small tt, low noise), and low when the noise component (1−α¯t​ϵ\sqrt{1-\bar{\alpha}\_{t}}\bm{\epsilon}) dominates (large tt, high noise). Multiplying the arbitrage penalty by wS​N​R​(t)w\_{SNR}(t) provides a natural weighting scheme: the penalty’s contribution to the total loss is strongly emphasized when the denoised estimate is reliable (low tt) and significantly down-weighted when the estimate is noisy and unreliable (high tt). This prevents the potentially large and erratic penalties from high-noise steps from dominating the training objective, allowing the MSE term to guide the learning process effectively while still ensuring that the arbitrage constraints are strongly enforced as the generation process approaches the clean data manifold. The final SNR-Weighted Arbitrage Loss term is thus defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒarb, weighted​(θ)=𝔼t,𝐱0,ϵ,𝐜​[wS​N​R​(t)⋅Φ​(InvTransform​(𝐱^0​(θ)))].\displaystyle\mathcal{L}\_{\text{arb, weighted}}(\theta)=\mathbb{E}\_{t,\mathbf{x}\_{0},\bm{\epsilon},\mathbf{c}}\left[w\_{SNR}(t)\cdot\Phi(\text{InvTransform}(\hat{\mathbf{x}}\_{0}(\theta)))\right]. |  | (41) |

The hyperparameter λ>0\lambda>0 in the total loss function ([37](https://arxiv.org/html/2511.07571v1#S5.E37 "In 5.3.1 Loss Function ‣ 5.3 Training and Sampling Algorithm ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")) then sets the overall scale of this dynamically weighted arbitrage regularization relative to the primary data-fitting objective ℒMSE\mathcal{L}\_{\text{MSE}}. It is worth noting that even when trained solely with the MSE loss (λ=0\lambda=0), the diffusion model demonstrated a capacity to generate visually plausible IV surfaces that largely respected the qualitative features expected in financial markets. This inherent structure-learning capability stands in contrast to Generative Adversarial Networks (GANs), which requires smooth function in the loss function to generate plausible surfaces. This observation suggests that DDPM is a potentially more robust choice for this application compared to GAN, even before the inclusion of explicit financial constraints. The calculation of the discrete finite differences required for the arbitrage penalties p1,p2,p3p\_{1},p\_{2},p\_{3} (Equations ([31](https://arxiv.org/html/2511.07571v1#S5.E31 "In Quantifying Arbitrage Violations. ‣ 5.1 Data Representation and Pre-Processing ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")), ([32](https://arxiv.org/html/2511.07571v1#S5.E32 "In Quantifying Arbitrage Violations. ‣ 5.1 Data Representation and Pre-Processing ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")), ([33](https://arxiv.org/html/2511.07571v1#S5.E33 "In Quantifying Arbitrage Violations. ‣ 5.1 Data Representation and Pre-Processing ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm"))) is implemented efficiently using 2D convolution operations with fixed, pre-defined kernels applied to the surface of relative call prices c​(m,τ)c(m,\tau). For instance, first-order differences along the moneyness or tenor dimension can be computed using kernels like [[−1,1]][[-1,1]] or [[−1],[1]][[-1],[1]]. Second-order differences, needed for the butterfly penalty p3p\_{3}, can be computed using kernels like [[1,−2,1]][[1,-2,1]]. This convolutional approach leverages highly optimized routines available in deep learning libraries, making the penalty calculation computationally feasible during training.

#### 5.3.2 Training Algorithm

The model is trained for a total of 2000 epochs using a batch size of 64. We employ a cosine beta schedule (Nichol\_Dhariwal\_2021) with N=500N=500 diffusion steps. The parameters θ\theta of the U-Net ϵθ\bm{\epsilon}\_{\theta} are learned by minimizing the composite loss ℒ​(θ)\mathcal{L}(\theta) ([37](https://arxiv.org/html/2511.07571v1#S5.E37 "In 5.3.1 Loss Function ‣ 5.3 Training and Sampling Algorithm ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")) with the AdamW optimizer (Loshchilov\_Hutter\_2019) and an initial learning rate of 3×10−43\times 10^{-4}. The learning rate is dynamically managed by a ReduceLROnPlateau scheduler, which reduces the rate by a factor of 0.8 if the validation loss does not improve for 300 epochs, down to a minimum learning rate of 1×10−61\times 10^{-6}. Figure [6](https://arxiv.org/html/2511.07571v1#S5.F6 "Figure 6 ‣ 5.3.2 Training Algorithm ‣ 5.3 Training and Sampling Algorithm ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") demonstrates the ReduceLROnPlateau learning rate schedule of the training process. To ensure training stability, we apply gradient clipping with a maximum L​2L2-norm of 0.15. The limited number of data samples makes the model prone to overfitting. To prevent this, we implement an early stopping criterion based on the validation loss. Furthermore, we maintain an Exponential Moving Average (EMA) of the model’s parameters, θE​M​A\theta\_{EMA}, with a decay rate of βE​M​A=0.995\beta\_{EMA}=0.995. The arbitrage penalty weights used in the loss function are λsmile=0.01\lambda\_{\text{smile}}=0.01 and λttm=0.01\lambda\_{\text{ttm}}=0.01. The training process is detailed in Algorithm [1](https://arxiv.org/html/2511.07571v1#alg1 "Algorithm 1 ‣ 5.3.2 Training Algorithm ‣ 5.3 Training and Sampling Algorithm ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm"). Figure [7](https://arxiv.org/html/2511.07571v1#S5.F7 "Figure 7 ‣ 5.3.2 Training Algorithm ‣ 5.3 Training and Sampling Algorithm ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") shows the loss curve of the training and validation process.

![Refer to caption](fig/lr_curve.png)


Figure 6: Learning rate schedule for the training process.

The parameters θ\theta of the conditional U-Net ϵθ\bm{\epsilon}\_{\theta} are learned by minimizing the composite loss ℒ​(θ)\mathcal{L}(\theta) using the AdamW optimizer (Loshchilov\_Hutter\_2019). The training process involves repeatedly sampling data points, timesteps, and noise, and updating the network weights based on the gradient of the loss. Crucially, the contribution of the arbitrage penalty to the total loss is weighted by the Signal-to-Noise Ratio (SNR) corresponding to the sampled timestep tt, defined as SNR​(t)=α¯t/(1−α¯t)\text{SNR}(t)=\bar{\alpha}\_{t}/(1-\bar{\alpha}\_{t}). This weighting scheme aims to balance the influence of the penalty across different noise levels during training. Additionally, following common practice, we maintain an Exponential Moving Average (EMA) of the model’s parameters, denoted as θE​M​A\theta\_{EMA}, using a decay rate βE​M​A\beta\_{EMA}. This EMA is crucial for DDPM, the performance of EMA model and non-EMA model are dramatically different (we used EMA weight as 0.995). Algorithm [1](https://arxiv.org/html/2511.07571v1#alg1 "Algorithm 1 ‣ 5.3.2 Training Algorithm ‣ 5.3 Training and Sampling Algorithm ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") provides the pseudocode for the training loop incorporating both SNR weighting and EMA updates.

![Refer to caption](fig/loss_curves.png)


Figure 7: Loss curves of training and validation.




Algorithm 1  Training the Conditional Diffusion Model with SNR-Weighted Arbitrage Penalty and EMA

1:Training dataset {(𝐱0(k),𝐜(k))}\{(\mathbf{x}\_{0}^{(k)},\mathbf{c}^{(k)})\} (normalized log-IV surfaces and conditions).

2:Noise schedule {βt}t=1n\{\beta\_{t}\}\_{t=1}^{n}, derived quantities {αt,α¯t}t=1n\{\alpha\_{t},\bar{\alpha}\_{t}\}\_{t=1}^{n}.

3:Arbitrage penalty weight λ\lambda.

4:Optimizer (e.g., AdamW), learning rate ηl​r\eta\_{lr}.

5:EMA decay rate βE​M​A\beta\_{EMA} (e.g., 0.995).

6:Number of training iterations Ni​t​e​rN\_{iter}.

7:Initialize model parameters θ\theta.

8:Initialize EMA parameters θE​M​A←θ\theta\_{EMA}\leftarrow\theta.

9:for iteration = 1 to Ni​t​e​rN\_{iter} do

10:  Sample a mini-batch of data (𝐱0,𝐜)(\mathbf{x}\_{0},\mathbf{c}) from the training set.

11:  Sample timestep t∼Uniform​({1,…,n})t\sim\text{Uniform}(\{1,...,n\}) for each sample.

12:  Sample noise ϵ∼𝒩​(0,𝐈)\bm{\epsilon}\sim\mathcal{N}(0,\mathbf{I}).

13:  Compute noisy input: 𝐱t=α¯t​𝐱0+1−α¯t​ϵ\mathbf{x}\_{t}=\sqrt{\bar{\alpha}\_{t}}\mathbf{x}\_{0}+\sqrt{1-\bar{\alpha}\_{t}}\bm{\epsilon}.

14:  Predict noise using the network with current parameters θ\theta: ϵ^θ=ϵθ​(𝐱t,t,𝐜)\hat{\bm{\epsilon}}\_{\theta}=\bm{\epsilon}\_{\theta}(\mathbf{x}\_{t},t,\mathbf{c}).

15:  Compute MSE loss: LMSE=‖ϵ−ϵ^θ‖2L\_{\text{MSE}}=||\bm{\epsilon}-\hat{\bm{\epsilon}}\_{\theta}||^{2} (averaged over mini-batch).

16:  Compute denoised estimate using current parameters θ\theta: 𝐱^0=1α¯t​(𝐱t−1−α¯t​ϵ^θ)\hat{\mathbf{x}}\_{0}=\frac{1}{\sqrt{\bar{\alpha}\_{t}}}(\mathbf{x}\_{t}-\sqrt{1-\bar{\alpha}\_{t}}\hat{\bm{\epsilon}}\_{\theta}).

17:  Transform 𝐱^0\hat{\mathbf{x}}\_{0} back to volatility scale: σ^=InvTransform​(𝐱^0)\hat{\sigma}=\text{InvTransform}(\hat{\mathbf{x}}\_{0}).

18:  Calculate arbitrage penalty Φ​(σ^)\Phi(\hat{\sigma}) using convolutional kernels (per sample).

19:  Calculate SNR weight for each sample’s timestep tt: wS​N​R​(t)=α¯t/(1−α¯t+ϵs​t​a​b)w\_{SNR}(t)=\bar{\alpha}\_{t}/(1-\bar{\alpha}\_{t}+\epsilon\_{stab}) (where ϵs​t​a​b\epsilon\_{stab} is a small constant for stability).

20:  Compute total loss (averaged over mini-batch): ℒ=LMSE+λ⋅mean​(wS​N​R​(t)⋅Φ​(σ^))\mathcal{L}=L\_{\text{MSE}}+\lambda\cdot\text{mean}(w\_{SNR}(t)\cdot\Phi(\hat{\sigma})).

21:  Compute gradient ∇θℒ\nabla\_{\theta}\mathcal{L}.

22:  Update parameters using optimizer: θ←OptimizerStep​(θ,∇θℒ,ηl​r)\theta\leftarrow\text{OptimizerStep}(\theta,\nabla\_{\theta}\mathcal{L},\eta\_{lr}).

23:  Update EMA parameters: θE​M​A←βE​M​A⋅θE​M​A+(1−βE​M​A)⋅θ\theta\_{EMA}\leftarrow\beta\_{EMA}\cdot\theta\_{EMA}+(1-\beta\_{EMA})\cdot\theta.

24:end for

25:return Trained EMA parameters θE​M​A\theta\_{EMA}.

#### 5.3.3 Sampling Algorithm

After training, the model with the stored EMA parameters θE​M​A\theta\_{EMA} is used to generate new IV surfaces conditioned on a specific context vector 𝐜\mathbf{c}. This is achieved by simulating the reverse diffusion process, starting from pure Gaussian noise 𝐱n∼𝒩​(0,𝐈)\mathbf{x}\_{n}\sim\mathcal{N}(0,\mathbf{I}) and iteratively denoising it using the learned EMA model. We employ the standard DDPM sampling algorithm (Ho\_Jain\_Abbeel\_2020), replacing the instantaneous model weights with the EMA weights, as detailed in Algorithm [2](https://arxiv.org/html/2511.07571v1#alg2 "Algorithm 2 ‣ 5.3.3 Sampling Algorithm ‣ 5.3 Training and Sampling Algorithm ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm").

Algorithm 2  Sampling Conditional IV Surfaces using EMA Model

1:Trained EMA model parameters θE​M​A\theta\_{EMA}.

2:Conditioning vector 𝐜\mathbf{c} for the target day.

3:Noise schedule {αt,βt,α¯t}t=1n\{\alpha\_{t},\beta\_{t},\bar{\alpha}\_{t}\}\_{t=1}^{n}.

4:Sample initial noise 𝐱n∼𝒩​(0,𝐈)\mathbf{x}\_{n}\sim\mathcal{N}(0,\mathbf{I}).

5:for t=n,n−1,…,1t=n,n-1,...,1 do

6:  Sample 𝐳∼𝒩​(0,𝐈)\mathbf{z}\sim\mathcal{N}(0,\mathbf{I}) if t>1t>1, else 𝐳=𝟎\mathbf{z}=\mathbf{0}.

7:  Predict noise using the EMA model: ϵ^θE​M​A=ϵθE​M​A​(𝐱t,t,𝐜)\hat{\bm{\epsilon}}\_{\theta\_{EMA}}=\bm{\epsilon}\_{\theta\_{EMA}}(\mathbf{x}\_{t},t,\mathbf{c}).

8:  Compute mean of the reverse conditional distribution pθE​M​A​(𝐱t−1|𝐱t)p\_{\theta\_{EMA}}(\mathbf{x}\_{t-1}|\mathbf{x}\_{t}):

|  |  |  |
| --- | --- | --- |
|  | 𝝁θE​M​A​(𝐱t,t)=1αt​(𝐱t−βt1−α¯t​ϵ^θE​M​A).\bm{\mu}\_{\theta\_{EMA}}(\mathbf{x}\_{t},t)=\frac{1}{\sqrt{\alpha\_{t}}}\left(\mathbf{x}\_{t}-\frac{\beta\_{t}}{\sqrt{1-\bar{\alpha}\_{t}}}\hat{\bm{\epsilon}}\_{\theta\_{EMA}}\right). |  |

9:  Compute variance/standard deviation of the reverse step. A common choice is σt2=β~t=1−α¯t−11−α¯t​βt\sigma\_{t}^{2}=\tilde{\beta}\_{t}=\frac{1-\bar{\alpha}\_{t-1}}{1-\bar{\alpha}\_{t}}\beta\_{t}.

10:  Perform the reverse step (sample 𝐱t−1\mathbf{x}\_{t-1}):

|  |  |  |
| --- | --- | --- |
|  | 𝐱t−1=𝝁θE​M​A​(𝐱t,t)+σt​𝐳.\mathbf{x}\_{t-1}=\bm{\mu}\_{\theta\_{EMA}}(\mathbf{x}\_{t},t)+\sigma\_{t}\mathbf{z}. |  |

11:end for

12:Obtain the final generated sample 𝐱0\mathbf{x}\_{0} (in normalized log-space).

13:Transform 𝐱0\mathbf{x}\_{0} back to the original IV scale: σ^=InvTransform​(𝐱0)\hat{\sigma}=\text{InvTransform}(\mathbf{x}\_{0}).

14:return Generated IV surface σ^\hat{\sigma}.

This procedure allows for the generation of multiple, distinct IV surface samples for the same conditioning input 𝐜\mathbf{c}, reflecting the inherent uncertainty in market dynamics, leveraging the stability benefits often provided by the EMA model weights.

#### 5.3.4 Epsilon-Prediction vs. V-Prediction and Output Clipping

A technical detail in implementing diffusion models concerns the parameterization of the network’s output and potential numerical stability issues, particularly near the beginning of the reverse process (when tt is small, corresponding to large T−tT-t in the SDE notation). In the standard epsilon-prediction formulation used throughout this paper (where the network predicts ϵθ\bm{\epsilon}\_{\theta}), calculating the denoised estimate 𝐱^0\hat{\mathbf{x}}\_{0} ([39](https://arxiv.org/html/2511.07571v1#S5.E39 "In 5.3.1 Loss Function ‣ 5.3 Training and Sampling Algorithm ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")) or the mean of the reverse step 𝝁θ​(𝐱t,t)\bm{\mu}\_{\theta}(\mathbf{x}\_{t},t) involves terms like 1/α¯t1/\sqrt{\bar{\alpha}\_{t}} and (1−αt)/1−α¯t(1-\alpha\_{t})/\sqrt{1-\bar{\alpha}\_{t}}. As t→0t\to 0, α¯t→1\bar{\alpha}\_{t}\to 1, but αt\alpha\_{t} also approaches 1. However, the term 1−α¯t\sqrt{1-\bar{\alpha}\_{t}} in the denominator approaches zero, potentially causing these coefficients to explode numerically. This can lead to instability during sampling. A common practical workaround is to clip the calculated mean 𝝁θ​(𝐱t,t)\bm{\mu}\_{\theta}(\mathbf{x}\_{t},t) or the denoised estimate 𝐱^0\hat{\mathbf{x}}\_{0} to a pre-defined range (e.g., [-1, 1] if the data was normalized to this range) to prevent extreme values.

An alternative approach, known as v-prediction (Salimans\_Ho\_2022), reparameterizes the prediction target to circumvent this issue. Instead of predicting ϵ\bm{\epsilon}, the network is trained to predict 𝐯=α¯t​ϵ−1−α¯t​𝐱0\mathbf{v}=\sqrt{\bar{\alpha}\_{t}}\bm{\epsilon}-\sqrt{1-\bar{\alpha}\_{t}}\mathbf{x}\_{0}. This target often has better scaling properties across the full range of tt, particularly near t=0t=0 and t=nt=n, potentially leading to more stable training and sampling without the need for explicit clipping. The denoising and reverse step equations are adjusted accordingly based on the predicted 𝐯\mathbf{v}.

While v-prediction offers theoretical advantages in terms of stability, our empirical investigations for modelling implied volatility surfaces found that the standard epsilon-prediction approach, combined with output clipping for the reverse step mean 𝝁θ​(𝐱t,t)\bm{\mu}\_{\theta}(\mathbf{x}\_{t},t), yielded results largely comparable to those obtained using v-prediction. Given this similarity in performance for our specific application, we opted for the epsilon-prediction framework due to its slightly simpler formulation and widespread use.

## 6 Result and Forecasting Performance

This section evaluates the performance of the proposed conditional diffusion model. We assess the quality of the generated implied volatility surfaces against the test set and compare its capabilities to a benchmark VolGAN model.

The VolGAN model is structured as a Conditional Generative Adversarial Network (CGAN). Its generator is conditioned on historical market data, the previous day’s IV surface and recent underlying returns, and is trained to output a realistic one-day-ahead increment of the log-IV surface, along with the underlying’s return. VolGAN’s approach to handling arbitrage during training is a major difference. The model does not use an explicit, direct arbitrage penalty in its loss function. Instead, it incorporates a “smoothness penalty” (a discrete Sobolev semi-norm) into the generator’s loss. This penalty encourages the model to produce regular, smooth surfaces, which indirectly reduces arbitrage violations that often stem from irregular shapes.

The evaluation focuses on quantitative accuracy, financial plausibility, and the model’s ability to capture the distributional and structural properties of the IV manifold. Since the VolGAN model has instability issue, we are using the most accurate model among 9 trained models.

### 6.1 Qualitative Plausibility of Generated Surfaces

We should examine two key stylized facts on the surfaces: the volatility smile (non-linear curvature across moneyness) and the term structure (the shape across time to maturity). The surfaces should be free of any non-financial artifacts. Figure [8](https://arxiv.org/html/2511.07571v1#S6.F8 "Figure 8 ‣ 6.1 Qualitative Plausibility of Generated Surfaces ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") presents a side-by-side comparison (January 5, 2022) from the test set. It displays the real surface, the mean surface generated by our conditional diffusion model, and the mean surface generated by the benchmark VolGAN model, all for the same conditioning data.

![Refer to caption](fig/REAL_surface_20220105.png)


(a) Real (Ground Truth).

![Refer to caption](fig/DIFFUSION_MEAN_surface_20220105.png)


(b) Diffusion Model (Mean).

![Refer to caption](fig/GAN_MEAN_surface_20220105.png)


(c) VolGAN (Mean).

Figure 8: Qualitative comparison of generated surfaces for a single test-set date (2022-01-05). The (a) real surface shows a smooth, pronounced smirk. This shape is (b) closely replicated by our diffusion model, while (c) the VolGAN surface exhibits a "crease" at the short-term, low-moneyness corner.

The ground truth surface in Panel (a) exhibits a classic volatility “smirk”, with implied volatility peaking at low moneyness (deep OTM puts) and reaching a minimum near-the-money. The entire surface is smooth and continuous. Panel (b) shows the mean surface generated by our proposed diffusion model. Visually, it provides an excellent qualitative fit. The model accurately replicates the sharp curvature of the smile, including the steep wing at low moneyness, and the entire surface remains smooth and well-behaved, consistent with the real data. Panel (c) displays the mean surface from the VolGAN benchmark. While it captures the general shape of the smile, at the front corner, corresponding to low moneyness and low time-to-maturity, the surface displays a sharp “crease” or “lip” that is not present in the real data. This artifact suggests the GAN struggled to correctly learn the manifold’s boundary constraints, resulting in an unstable or financially implausible shape in this region. Figure [8](https://arxiv.org/html/2511.07571v1#S6.F8 "Figure 8 ‣ 6.1 Qualitative Plausibility of Generated Surfaces ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") suggests that the diffusion model is more effective at learning and replicating the complex, smooth geometry of the implied volatility manifold.

### 6.2 Quantitative Check of Generated Surfaces

The qualitative inspection in the previous section suggests our model generates more plausible surfaces, this section provides a rigorous quantitative assessment of its point-wise forecasting accuracy and the reliability estimates. We analyze the model’s performance over the entire test set and directly compare it to the VolGAN benchmark.

##### Time Series Slice Analysis.

We first analyze the models’ forecasting performance beyond a static snapshot as a time series. For each day in the test set, we generate 100 conditional surfaces using both our diffusion model and the VolGAN, allowing us to compute a mean forecast and a 90% confidence interval. The lower and upper bound are defined by the 5th and 95th percentiles of the samples, respectively.

Figures [9](https://arxiv.org/html/2511.07571v1#S6.F9 "Figure 9 ‣ Time Series Slice Analysis. ‣ 6.2 Quantitative Check of Generated Surfaces ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm"), [10](https://arxiv.org/html/2511.07571v1#S6.F10 "Figure 10 ‣ Time Series Slice Analysis. ‣ 6.2 Quantitative Check of Generated Surfaces ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm"), and [11](https://arxiv.org/html/2511.07571v1#S6.F11 "Figure 11 ‣ Time Series Slice Analysis. ‣ 6.2 Quantitative Check of Generated Surfaces ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") plot these time series results for seven representative points on the IV grid: At-the-Money (ATM) 1-Day, 1-Month, and 3-Month options; In-the-Money (ITM) 1-Month and 3-Month options; and Out-of-the-Money (OTM) 1-Month and 3-Month options. For each slice, we present a direct comparison between our Diffusion Model’s forecast (left panel) and the VolGAN benchmark’s forecast (right panel). Both plots overlay the model’s mean prediction and 90% confidence interval against the same ground truth (actual) IV data.

Figure 9: Time series comparison for At-the-Money (ATM) slices. Left: Diffusion Model vs. Real. Right: VolGAN vs. Real.

![Refer to caption](ts_slice/DiffusionModel_ATM_1-Day_comparison.png)


(a) Diffusion Model (ATM 1-Day).

![Refer to caption](ts_slice/volgan_atm_1-day_ci.png)


(b) VolGAN Model (ATM 1-Day).

![Refer to caption](ts_slice/DiffusionModel_ATM_1-Month_comparison.png)


(c) Diffusion Model (ATM 1-Month).

![Refer to caption](ts_slice/volgan_atm_1-month_ci.png)


(d) VolGAN Model (ATM 1-Month).

![Refer to caption](ts_slice/DiffusionModel_ATM_3-Month_comparison.png)


(e) Diffusion Model (ATM 3-Month).

![Refer to caption](ts_slice/volgan_atm_3-month_ci.png)


(f) VolGAN Model (ATM 3-Month).




Figure 10: Time series comparison for In-the-Money (ITM) slices. Left: Diffusion Model vs. Real. Right: VolGAN vs. Real.

![Refer to caption](ts_slice/DiffusionModel_ITM_1-Month_comparison.png)


(a) Diffusion Model (ITM 1-Month).

![Refer to caption](ts_slice/volgan_itm_1-month_ci.png)


(b) VolGAN Model (ITM 1-Month).

![Refer to caption](ts_slice/DiffusionModel_ITM_3-Month_comparison.png)


(c) Diffusion Model (ITM 3-Month).

![Refer to caption](ts_slice/volgan_itm_3-month_ci.png)


(d) VolGAN Model (ITM 3-Month).




Figure 11: Time series comparison for Out-of-the-Money (OTM) slices. Left: Diffusion Model vs. Real. Right: VolGAN vs. Real.

![Refer to caption](ts_slice/DiffusionModel_OTM_1-Month_comparison.png)


(a) Diffusion Model (OTM 1-Month).

![Refer to caption](ts_slice/volgan_otm_1-month_ci.png)


(b) VolGAN Model (OTM 1-Month).

![Refer to caption](ts_slice/DiffusionModel_OTM_3-Month_comparison.png)


(c) Diffusion Model (OTM 3-Month).

![Refer to caption](ts_slice/volgan_otm_3-month_ci.png)


(d) VolGAN Model (OTM 3-Month).




Table 1: Comparison of Model Performance Metrics.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ATM | | | | OTM | | | | ITM | | | |  |
| Metric | 1-Day | 1-Week | 1-Month | 3-Month | 1-Day | 1-Week | 1-Month | 3-Month | 1-Day | 1-Week | 1-Month | 3-Month | Overall |
| VolGAN | | | | | | | | | | | | | |
| MAPE (%) | 4.8882 | 4.8595 | 4.6231 | 4.2498 | 5.5066 | 5.7265 | 5.0659 | 4.0762 | 2.9814 | 2.9420 | 2.6978 | 2.3652 | 3.7304 |
| Std. of APE (%) | 4.0258 | 4.0304 | 3.9043 | 3.5292 | 4.8518 | 4.9798 | 4.3324 | 3.5471 | 2.4231 | 2.4151 | 2.2283 | 1.8661 |  |
| Mean CI Width | 0.0158 | 0.0159 | 0.0146 | 0.0151 | 0.0726 | 0.0679 | 0.0654 | 0.0474 | 0.0347 | 0.0292 | 0.0248 | 0.0128 |  |
| Std. CI Width | 0.0073 | 0.0072 | 0.0064 | 0.0047 | 0.0172 | 0.0149 | 0.0141 | 0.0099 | 0.0091 | 0.0075 | 0.0055 | 0.0023 |  |
| CI Breach % | 44.8276 | 43.8218 | 45.6897 | 40.5172 | 1.5805 | 2.5862 | 1.0057 | 1.0057 | 31.4655 | 35.0575 | 36.7816 | 57.1839 |  |
| Diffusion | | | | | | | | | | | | | |
| MAPE (%) | 4.6907 | 4.6884 | 4.5146 | 4.0202 | 3.5264 | 3.4573 | 3.1542 | 2.4555 | 2.5129 | 2.4992 | 2.4184 | 2.2024 | 3.0026 |
| Std. of APE (%) | 4.0338 | 4.0091 | 3.8795 | 3.4909 | 2.6588 | 2.5785 | 2.3190 | 1.8739 | 2.3984 | 2.3844 | 2.2909 | 2.0393 |  |
| Mean CI Width | 0.0372 | 0.0369 | 0.0357 | 0.0327 | 0.0468 | 0.0457 | 0.0412 | 0.0311 | 0.0472 | 0.0463 | 0.0438 | 0.0384 |  |
| Std. CI Width | 0.0160 | 0.0159 | 0.0152 | 0.0134 | 0.0098 | 0.0095 | 0.0082 | 0.0057 | 0.0139 | 0.0137 | 0.0132 | 0.0124 |  |
| CI Breach % | 10.9195 | 10.4885 | 11.0632 | 10.0575 | 0.5747 | 0.7184 | 0.5747 | 1.0057 | 7.9023 | 7.9023 | 8.4770 | 7.9023 |  |

We trained 9 VolGAN models and selected the best-performing one, based on overall MAPE, as our benchmark for comparison to avoid the instability of GAN. The performance metrics, detailed in Table [1](https://arxiv.org/html/2511.07571v1#S6.T1 "Table 1 ‣ Time Series Slice Analysis. ‣ 6.2 Quantitative Check of Generated Surfaces ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm"), summarize the performance of our proposed diffusion model. A more detailed table that includes all GAN models is shown in Appendix [A](https://arxiv.org/html/2511.07571v1#A1 "Appendix A Full Performance Metrics for All Trained Models ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm").
Our diffusion model demonstrates strong predictive accuracy, achieving an Overall MAPE of 3.0026%, which is lower than the benchmark’s 3.7304%. This indicates a consistent ability to capture the central tendency of the implied volatility surface.
To evaluate the reliability of our uncertainty estimates, we measure the 90% confidence interval brach (CI Breach %) rate. This metric calculates the percentage of days in the test set where the ground-truth IV value fell outside the 90% confidence interval generated by our model (i.e., below the 5th percentile or above the 95th percentile of the 100 generated samples). For a perfectly calibrated model, this breach rate should be around 10%. Our model’s CI Breach %
for both ATM and ITM points is remarkably stable and hovers very close to the theoretical 10% target. This suggests that our model generates a well-calibrated representation of the true data distribution for the most liquid parts of the surface.
While the benchmark model also produces accurate mean forecasts, its confidence intervals for ATM and ITM points show substantially higher breach rates (e.g., 44.8% and 31.5%, respectively), suggesting a potential miscalibration in its uncertainty estimates.
The benchmark model produces narrower Mean CI Widths (e.g., 0.0158 for ATM 1-Day) compared to our model (0.0372). However, the benchmark model misses the true value inside the confidence interval more often than the desired 10%. The confidence interval generated by the diffusion model is wider in most points, but it can capture the true value at the desired 90% rate for ATM and ITM points.

An area for future refinement in our model is the calibration for OTM options. The breach rate for these points is very low (often below 1.1%), indicating that the generated confidence intervals are somewhat conservative. Future work would focus on tightening these OTM intervals while maintaining the excellent calibration already achieved for the ATM and ITM regions.
In summary, our diffusion model is capable of generating accurate point forecasts and statistically reliable confidence intervals.

Beyond analyzing individual grid points, it is critical to evaluate the model’s accuracy across the entire 9×99\times 9 surface simultaneously. A robust model should not only be accurate at key points but also maintain a low error across the whole surface structure. To measure this, we calculate the daily Mean Absolute Percentage Error (MAPE) for the mean-generated surface against the ground truth surface for each day in the test set. For a given day kk, the surface MAPE is defined as:

|  |  |  |
| --- | --- | --- |
|  | MAPEk=1d​∑i=1d|𝐱^i(k)−𝐱i(k)𝐱i(k)|,\text{MAPE}\_{k}=\frac{1}{d}\sum\_{i=1}^{d}\left|\frac{\hat{\mathbf{x}}\_{i}^{(k)}-\mathbf{x}\_{i}^{(k)}}{\mathbf{x}\_{i}^{(k)}}\right|, |  |

where d=81d=81 is the number of grid points, 𝐱(k)\mathbf{x}^{(k)} is the ground truth surface, and 𝐱^(k)\hat{\mathbf{x}}^{(k)} is the mean surface generated by the model for day kk. Figure [12](https://arxiv.org/html/2511.07571v1#S6.F12 "Figure 12 ‣ Time Series Slice Analysis. ‣ 6.2 Quantitative Check of Generated Surfaces ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") plots this daily surface MAPE over the entire test period for our conditional diffusion model.

The plot displays the median predicted MAPE (dashed line), calculated from the 100 generated samples for each day, as well as the 90% confidence interval (shaded area) of this prediction.
The model demonstrates a stable and low error baseline, with the median MAPE consistently fluctuating in the 2.5% to 5% range for long stretches of the test period. The error is not static with obvious fluctuations. The error spikes to 10-15% during the market turmoil periods.
Furthermore, the 90% confidence interval illustrates the model’s distributional uncertainty. While the upper bound of the CI can be wide during these volatile periods, indicating that some generated samples in the distribution have a higher error, the median forecast remains robust and tracks well within the low single-digit percentages.

Figure 12: Daily Surface MAPE of Mean Forecast vs. Ground Truth (Test Set).

![Refer to caption](fig/mape_timeseries_with_ci.png)

### 6.3 Financial Plausibility (Arbitrage Analysis)

Beyond point-wise accuracy, a successful generative model for financial assets must produce outputs that are financially plausible and do not systematically violate fundamental no-arbitrage conditions. We evaluate this by calculating the total arbitrage penalty Φ\Phi (as defined in Equations [31](https://arxiv.org/html/2511.07571v1#S5.E31 "In Quantifying Arbitrage Violations. ‣ 5.1 Data Representation and Pre-Processing ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")-[33](https://arxiv.org/html/2511.07571v1#S5.E33 "In Quantifying Arbitrage Violations. ‣ 5.1 Data Representation and Pre-Processing ‣ 5 Procedure to Simulate Implied Volatility Surfaces ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm")) for every generated surface in the test set. Figure [13](https://arxiv.org/html/2511.07571v1#S6.F13 "Figure 13 ‣ 6.3 Financial Plausibility (Arbitrage Analysis) ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") plots the daily mean arbitrage penalty generated by our conditional diffusion model against the ground-truth data from the test set. The plot displays the model’s mean penalty (averaged over 100 generated samples per day). This is compared directly to the arbitrage penalty of the real (smoothed) surface (black line).

Figure 13: Daily Arbitrage Penalty of the Diffusion Model on the Test Set. The mean penalty (solid line) from our model are compared to the ground-truth penalty (black line).

![Refer to caption](fig/arbitrage_timeseries_mean.png)

As shown in Figure [13](https://arxiv.org/html/2511.07571v1#S6.F13 "Figure 13 ‣ 6.3 Financial Plausibility (Arbitrage Analysis) ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm"), our model generates surfaces with relatively low arbitrage violations. The mean penalty consistently tracks the low-level penalty observed in the real test data, indicating that the model successfully captures the market’s low-arbitrage characteristics. It is crucial to contextualize this result. Our training dataset (1996-2018) is composed of older market data. In these earlier periods, market microstructure was less advanced, and algorithmic trading was not as prevalent, leading to a higher incidence of arbitrage opportunities being recorded in the data. In contrast, our test set (2019-2023) reflects a modern, highly efficient market where high-frequency trading (HFT) and sophisticated arbitrage-seeking algorithms have made such opportunities far rarer.

This discrepancy presents a significant challenge: the models are trained on a distribution that contains a non-trivial amount of arbitrage. It is notoriously difficult for a data-driven generative model to learn to be “cleaner” than the data it is trained on. Therefore, the models inevitably learn to replicate some of these observed violations. Given this context, the ability of both the diffusion model and the GAN to generate surfaces with low arbitrage. It suggests that both models, despite being trained on imperfect data, are successfully capturing the underlying, dominant manifold structure of financially plausible surfaces and are not simply overfitting to the arbitrage-laden examples in the training set.

### 6.4 Distributional and Structural Fidelity

A robust generative model must replicate the mean of the data, the full statistical distribution, and underlying covariance structure at the same time. While the previous section confirmed the accuracy of the mean forecast, we now analyze whether our diffusion model successfully learns the complete, non-Gaussian distribution and the low-dimensional manifold structure of implied volatility surfaces. To assess distributional fidelity, we compare the higher-order statistical moments of the generated data against the real data. Volatility is well-known to be non-Gaussian, often exhibiting significant skewness and fat tails. A successful model must capture these features.

We analyze the marginal distributions for several key grid points by pooling all 100 generated samples for each of the 696 test days, creating a large sample distribution for both the model and the ground truth. Table [2](https://arxiv.org/html/2511.07571v1#S6.T2 "Table 2 ‣ 6.4 Distributional and Structural Fidelity ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") compares the first four moments (Mean, Standard Deviation, Skewness, and Kurtosis) for five representative slices.

Table 2: Comparison of Statistical Moments for Key IV Slices (Test Set).

| Metric | ATM 1-Day | | ATM 1-Month | | OTM 1-Week | | OTM 3-Month | | ITM 1-Week | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Real Data | Diffusion | Real Data | Diffusion | Real Data | Diffusion | Real Data | Diffusion | Real Data | Diffusion |
| Mean | 0.1884 | 0.1868 | 0.1891 | 0.1876 | 0.1616 | 0.1622 | 0.1546 | 0.1548 | 0.3960 | 0.3914 |
| Std Dev | 0.0448 | 0.0441 | 0.0439 | 0.0431 | 0.0230 | 0.0272 | 0.0221 | 0.0241 | 0.0371 | 0.0385 |
| Skewness | 0.5487 | 0.6993 | 0.5339 | 0.6651 | 0.6318 | 0.7804 | 0.6201 | 0.6723 | 0.6887 | 0.7034 |
| Kurtosis (Fisher) | -0.5404 | 0.1520 | -0.5562 | 0.0679 | 0.2771 | 1.0518 | 0.1709 | 0.4273 | 0.0930 | 0.6775 |

Comparison of the first four statistical moments between the real data distribution and the pooled distribution of all generated samples from the diffusion model over the entire test set. Kurtosis is reported as Fisher’s kurtosis (normal=0).

##### Analysis of Distributional Moments.

The results in Table [2](https://arxiv.org/html/2511.07571v1#S6.T2 "Table 2 ‣ 6.4 Distributional and Structural Fidelity ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm") provide several crucial insights. The first two moments (Mean and Std Dev) are very closely matched, confirming the point-wise accuracy observed in the previous subsection. Furthermore, the model correctly captures the positive skewness present in all the real data slices, a key non-Gaussian feature.

The most notable discrepancy, however, appears in the kurtosis. The real data consistently exhibits smaller kurtosis, indicating a distribution with thinner tails, more stable central peak. This is visually confirmed in Figure [14](https://arxiv.org/html/2511.07571v1#S6.F14 "Figure 14 ‣ Analysis of Distributional Moments. ‣ 6.4 Distributional and Structural Fidelity ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm"), where the blue “Real Data” histograms appear wider and more rectangular. In contrast, our diffusion model generates data with a larger kurtosis. This indicates the model is producing fatter tails and a spikier central peak than the ground truth. This is also clearly visible in Figure [14](https://arxiv.org/html/2511.07571v1#S6.F14 "Figure 14 ‣ Analysis of Distributional Moments. ‣ 6.4 Distributional and Structural Fidelity ‣ 6 Result and Forecasting Performance ‣ Forecasting implied volatility surface with generative diffusion models1footnote 11footnote 1Full code available on https://github.com/Austinjinc/rep_volgan/tree/refactor/new-ddpm"), where the orange “Diffusion Model” distribution is more sharply peaked and has more mass in the extreme tails. This implies that the model, while accurate on average, tends to overestimate the frequency of extreme volatility events. For a risk-management application, this could be interpreted as a conservative bias, as the model generates more stress scenarios than are present in the smoothed historical data. Our model is overestimating the tail risks than the actual data.

Figure 14: Distributional Comparison for Key IV Slices.

![Refer to caption](fig/Dist_ATM_1-Day_histogram.png)


(a) ATM 1-Day distribution histogram plot of real data and generated data.

![Refer to caption](fig/Dist_ATM_1-Month_histogram.png)


(b) ATM 1-Month distribution histogram plot of real data and generated data.

![Refer to caption](fig/Dist_ITM_1-Week_histogram.png)


(c) ITM 1-Week distribution histogram plot of real data and generated data.

![Refer to caption](fig/Dist_OTM_1-Week_histogram.png)


(d) OTM 1-Week distribution histogram plot of real data and generated data.

## 7 Conclusion

In this paper, we introduced a conditional Denoising Diffusion Probabilistic Model (DDPM) for the one-day-ahead forecasting of implied volatility surfaces. We demonstrated that the stable training of diffusion models, combined with conditioning variables, provides a powerful and improved alternative to existing generative models like GANs.

We incorporates an explicit arbitrage penalty into the loss function that is dynamically weighted by the Signal-to-Noise Ratio (SNR). This approach successfully balances the financial plausibility, guiding the model towards the arbitrage-free manifold without destabilizing the training process given that the training data samples are not arbitrage-free. The empirical results confirmed the success of this method. Our model not only achieved a lower Overall MAPE than the VolGAN benchmark but, more critically, produced well-calibrated and statistically reliable 90% confidence intervals.

Furthermore, we provided a formal convergence guarantee for this penalized loss, proving that the bias introduced by the penalty is bounded (O​(λ2)O(\lambda^{2})) and controllable. This result places our domain-specific loss function on a firm theoretical foundation, ensuring that the model’s convergence properties are understood.

For future research, our model’s uncertainty estimates for OTM options were shown to be overly conservative (CI breach rate ≈\approx 1%). This could explore alternative loss-weighting schemes to improve calibration across the entire surface. Also, while our SNR-weighted penalty significantly reduces arbitrage, it remains a ’soft’ constraint. Exploring methods to enforce arbitrage-free conditions as a ’hard’ constraint, perhaps through a re-parameterization of the U-Net’s output, would be a valuable extension.

## Appendix A Full Performance Metrics for All Trained Models

Table 3: Full comparison of performance metrics for all 9 trained VolGAN models and the proposed Diffusion model. VolGAN 5 was selected as the benchmark for comparison in the main text due to having the lowest Overall MAPE.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ATM | | | | OTM | | | | ITM | | | |  |
| Metric | 1-Day | 1-Week | 1-Month | 3-Month | 1-Day | 1-Week | 1-Month | 3-Month | 1-Day | 1-Week | 1-Month | 3-Month | Overall |
| VolGAN 1 | | | | | | | | | | | | | |
| MAPE (%) | 7.0001 | 6.9535 | 6.5684 | 5.8614 | 9.4079 | 9.7788 | 8.6473 | 6.7865 | 4.9322 | 4.8257 | 4.2571 | 3.6685 | 6.6667 |
| Std. of APE (%) | 4.2401 | 4.2771 | 4.1018 | 3.6491 | 5.8378 | 5.9709 | 5.3908 | 4.4841 | 3.0913 | 3.0571 | 2.7487 | 2.2577 |  |
| Mean CI Width | 0.0190 | 0.0192 | 0.0177 | 0.0183 | 0.0526 | 0.0504 | 0.0489 | 0.0355 | 0.0272 | 0.0225 | 0.0191 | 0.0100 |  |
| Std. CI Width | 0.0094 | 0.0092 | 0.0083 | 0.0058 | 0.0119 | 0.0108 | 0.0104 | 0.0076 | 0.0069 | 0.0055 | 0.0042 | 0.0019 |  |
| CI Breach % | 87.2126 | 88.0747 | 88.5057 | 88.0747 | 48.2758 | 52.8735 | 48.7068 | 52.1551 | 85.1963 | 88.0747 | 89.6551 | 94.6839 |  |
| VolGAN 2 | | | | | | | | | | | | | |
| MAPE (%) | 4.2452 | 4.2468 | 4.1351 | 3.8260 | 4.3516 | 4.3417 | 4.1015 | 3.4180 | 2.5534 | 2.5314 | 2.4761 | 2.2700 | 3.1977 |
| Std. of APE (%) | 4.2435 | 4.3466 | 4.1902 | 3.8217 | 4.1809 | 4.0501 | 4.1015 | 3.4180 | 2.4646 | 2.4578 | 2.3910 | 2.1277 |  |
| Mean CI Width | 0.0063 | 0.0063 | 0.0061 | 0.0057 | 0.0071 | 0.0070 | 0.0067 | 0.0059 | 0.0042 | 0.0041 | 0.0041 | 0.0039 |  |
| CI Breach % | 32.4712 | 34.6537 | 33.7638 | 39.3090 | 41.5229 | 0.1437 | 0.5747 | 0.1437 | 35.6323 | 53.4482 | 66.2011 | 66.2011 |  |
| VolGAN 3 | | | | | | | | | | | | | |
| MAPE (%) | 4.9158 | 4.8870 | 4.7380 | 4.3006 | 5.0614 | 5.0153 | 4.7212 | 4.0155 | 3.5417 | 3.5375 | 3.0911 | 2.7011 | 4.3185 |
| Std. of APE (%) | 4.1693 | 4.2790 | 4.1503 | 3.6596 | 5.4080 | 5.4496 | 5.0528 | 4.1803 | 2.8596 | 2.8687 | 2.7667 | 2.5827 |  |
| Mean CI Width | 0.0033 | 0.0033 | 0.0032 | 0.0030 | 0.0040 | 0.0040 | 0.0038 | 0.0033 | 0.0031 | 0.0030 | 0.0028 | 0.0025 |  |
| Std. CI Width | 0.0013 | 0.0013 | 0.0012 | 0.0011 | 0.0023 | 0.0023 | 0.0022 | 0.0017 | 0.0016 | 0.0015 | 0.0013 | 0.0011 |  |
| CI Breach % | 71.2627 | 72.7011 | 74.2844 | 75.5747 | 92.9195 | 95.1150 | 95.1150 | 94.6839 | 82.3276 | 84.5229 | 94.4000 | 97.2701 |  |
| VolGAN 4 | | | | | | | | | | | | | |
| MAPE (%) | 4.9835 | 5.0119 | 4.7963 | 4.2089 | 5.3025 | 5.2542 | 4.8604 | 3.8761 | 3.2672 | 3.1011 | 2.7571 | 2.5994 | 4.2181 |
| Std. of APE (%) | 4.2251 | 4.3025 | 4.1102 | 3.5221 | 5.2530 | 5.1780 | 4.6738 | 3.7088 | 2.7575 | 2.6288 | 2.3359 | 2.2215 |  |
| Mean CI Width | 0.0101 | 0.0101 | 0.0094 | 0.0087 | 0.0221 | 0.0210 | 0.0194 | 0.0146 | 0.0118 | 0.0101 | 0.0085 | 0.0059 |  |
| Std. CI Width | 0.0058 | 0.0057 | 0.0051 | 0.0039 | 0.0068 | 0.0064 | 0.0061 | 0.0045 | 0.0037 | 0.0031 | 0.0025 | 0.0015 |  |
| CI Breach % | 62.0689 | 60.0574 | 59.1954 | 56.9080 | 46.8390 | 52.0114 | 41.2528 | 42.8160 | 53.4482 | 52.3005 | 53.0172 | 58.1609 |  |
| VolGAN 5 | | | | | | | | | | | | | |
| MAPE (%) | 4.8882 | 4.8595 | 4.6231 | 4.2498 | 5.5066 | 5.7265 | 5.0659 | 4.0762 | 2.9814 | 2.9420 | 2.6978 | 2.3652 | 3.7304 |
| Std. of APE (%) | 4.0258 | 4.0304 | 3.9043 | 3.5292 | 4.8518 | 4.9798 | 4.3324 | 3.5471 | 2.4231 | 2.4151 | 2.2283 | 1.8661 |  |
| Mean CI Width | 0.0158 | 0.0159 | 0.0146 | 0.0151 | 0.0726 | 0.0679 | 0.0654 | 0.0474 | 0.0347 | 0.0292 | 0.0248 | 0.0128 |  |
| Std. CI Width | 0.0073 | 0.0072 | 0.0064 | 0.0047 | 0.0172 | 0.0149 | 0.0141 | 0.0099 | 0.0091 | 0.0075 | 0.0055 | 0.0023 |  |
| CI Breach % | 44.8276 | 43.8218 | 45.6897 | 40.5172 | 1.5805 | 2.5862 | 1.0057 | 1.0057 | 31.4655 | 35.0575 | 36.7816 | 57.1839 |  |
| VolGAN 6 | | | | | | | | | | | | | |
| MAPE (%) | 4.5919 | 4.5842 | 4.4827 | 3.9911 | 4.9067 | 4.9871 | 4.1293 | 2.9027 | 2.9071 | 2.8081 | 2.5404 | 2.3304 | 3.5186 |
| Std. of APE (%) | 4.0725 | 4.0620 | 3.9161 | 3.4862 | 4.4363 | 4.4077 | 3.8340 | 2.7309 | 2.4116 | 2.3661 | 2.1936 | 1.9480 |  |
| Mean CI Width | 0.0012 | 0.0012 | 0.0012 | 0.0011 | 0.0052 | 0.0048 | 0.0045 | 0.0031 | 0.0016 | 0.0015 | 0.0013 | 0.0009 |  |
| Std. CI Width | 0.0003 | 0.0003 | 0.0003 | 0.0003 | 0.0016 | 0.0014 | 0.0013 | 0.0008 | 0.0004 | 0.0004 | 0.0003 | 0.0002 |  |
| CI Breach % | 97.2701 | 96.5528 | 97.5574 | 97.8448 | 98.1321 | 100 | 98.1321 | 100 | 94.1150 | 94.8275 | 94.2586 | 95.6896 |  |
| VolGAN 7 | | | | | | | | | | | | | |
| MAPE (%) | 5.2086 | 5.4404 | 5.0933 | 3.5758 | 10.2165 | 10.4572 | 5.3888 | 9.4522 | 2.7654 | 2.4677 | 2.2042 | 2.0596 | 5.1002 |
| Std. of APE (%) | 4.1430 | 4.1090 | 3.7958 | 3.0917 | 6.2425 | 5.6217 | 4.3046 | 4.5954 | 2.1034 | 1.9688 | 1.8387 | 1.9649 |  |
| Mean CI Width | 0.0023 | 0.0023 | 0.0021 | 0.0017 | 0.0066 | 0.0059 | 0.0052 | 0.0040 | 0.0020 | 0.0017 | 0.0014 | 0.0009 |  |
| Std. CI Width | 0.0005 | 0.0005 | 0.0004 | 0.0003 | 0.0022 | 0.0019 | 0.0017 | 0.0010 | 0.0004 | 0.0003 | 0.0003 | 0.0002 |  |
| CI Breach % | 96.9827 | 95.8390 | 95.5517 | 95.6954 | 95.6954 | 96.2643 | 98.8505 | 98.4195 | 91.0919 | 93.4023 | 96.1206 | 96.8390 |  |
| VolGAN 8 | | | | | | | | | | | | | |
| MAPE (%) | 9.2638 | 9.5120 | 9.5430 | 8.5866 | 5.5670 | 5.5821 | 5.1200 | 6.1042 | 4.9452 | 4.8576 | 4.8285 | 7.4301 | 6.7358 |
| Std. of APE (%) | 4.9066 | 4.9712 | 4.9123 | 4.6773 | 5.1664 | 5.1768 | 4.7981 | 4.9984 | 3.5358 | 3.4839 | 3.5117 | 4.6300 |  |
| Mean CI Width | 0.0019 | 0.0019 | 0.0018 | 0.0017 | 0.0022 | 0.0022 | 0.0020 | 0.0019 | 0.0017 | 0.0016 | 0.0016 | 0.0022 |  |
| Std. CI Width | 0.0015 | 0.0015 | 0.0015 | 0.0013 | 0.0019 | 0.0019 | 0.0017 | 0.0013 | 0.0012 | 0.0011 | 0.0012 | 0.0015 |  |
| CI Breach % | 93.5468 | 95.6954 | 95.4080 | 89.7988 | 79.5977 | 83.1609 | 83.1609 | 73.1321 | 83.5919 | 90.6609 | 98.9942 | 99.4252 |  |
| VolGAN 9 | | | | | | | | | | | | | |
| MAPE (%) | 7.0862 | 6.8310 | 6.2417 | 5.2863 | 8.0195 | 7.9536 | 7.0454 | 5.4578 | 5.1714 | 4.7146 | 3.9676 | 3.6654 | 6.0554 |
| Std. of APE (%) | 4.7099 | 4.5428 | 4.1795 | 3.5511 | 6.0827 | 5.8643 | 5.2443 | 4.1952 | 3.8229 | 3.4960 | 2.9248 | 2.6517 |  |
| Mean CI Width | 0.0069 | 0.0067 | 0.0061 | 0.0053 | 0.0128 | 0.0121 | 0.0110 | 0.0082 | 0.0093 | 0.0079 | 0.0064 | 0.0044 |  |
| Std. CI Width | 0.0022 | 0.0021 | 0.0019 | 0.0015 | 0.0043 | 0.0039 | 0.0035 | 0.0025 | 0.0029 | 0.0023 | 0.0018 | 0.0011 |  |
| CI Breach % | 90.0862 | 90.0862 | 91.0919 | 92.2356 | 94.2586 | 95.1150 | 95.1150 | 96.1206 | 90.8045 | 93.1149 | 95.8390 | 100 |  |
| Diffusion | | | | | | | | | | | | | |
| MAPE (%) | 4.6907 | 4.6884 | 4.5146 | 4.0202 | 3.5264 | 3.4573 | 3.1542 | 2.4555 | 2.5129 | 2.4992 | 2.4184 | 2.2024 | 3.0026 |
| Std. of APE (%) | 4.0338 | 4.0091 | 3.8795 | 3.4909 | 2.6588 | 2.5785 | 2.3190 | 1.8739 | 2.3984 | 2.3844 | 2.2909 | 2.0393 |  |
| Mean CI Width | 0.0372 | 0.0369 | 0.0357 | 0.0327 | 0.0468 | 0.0457 | 0.0412 | 0.0311 | 0.0472 | 0.0463 | 0.0438 | 0.0384 |  |
| Std. CI Width | 0.0160 | 0.0159 | 0.0152 | 0.0134 | 0.0098 | 0.0095 | 0.0082 | 0.0057 | 0.0139 | 0.0137 | 0.0132 | 0.0124 |  |
| CI Breach % | 10.9195 | 10.4885 | 11.0632 | 10.0575 | 0.5747 | 0.7184 | 0.5747 | 1.0057 | 7.9023 | 7.9023 | 8.4770 | 7.9023 |  |