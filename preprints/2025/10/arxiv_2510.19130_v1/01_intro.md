---
authors:
- Andres Garcia-Medina
doc_id: arxiv:2510.19130v1
family_id: arxiv:2510.19130
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix
  Theory: Cryptocurrency Portfolio Applications'
url_abs: http://arxiv.org/abs/2510.19130v1
url_html: https://arxiv.org/html/2510.19130v1
venue: arXiv q-fin
version: 1
year: 2025
---


Andrés García-Medina
  
Faculty of Sciences
Email: andgarm.n@gmail.com

 Autonomous University of Baja California


 Ensenada


 22860


 Mexico

###### Abstract

Covariance matrices estimated from short, noisy, and non-Gaussian financial time series—particularly cryptocurrencies—are notoriously unstable. Empirical evidence indicates that these covariance structures often exhibit power-law scaling, reflecting complex and hierarchical interactions among assets. Building on this insight, we propose a power-law covariance model to characterize the collective dynamics of cryptocurrencies and develop a hybrid estimator that integrates Random Matrix Theory (RMT) with Residual Neural Networks (ResNets). The RMT component regularizes the eigenvalue spectrum under high-dimensional noise, while the ResNet learns data-driven corrections to recover latent structural dependencies. Monte Carlo simulations show that ResNet-based estimators consistently minimize both Frobenius and minimum-variance (MV) losses across diverse covariance models. Empirical experiments on 89 cryptocurrencies (2020–2025), using a training period ending at the local BTC maximum in November 2021 and testing through the subsequent bear market, demonstrate that a two-step estimator combining hierarchical filtering with ResNet corrections yields the most profitable and balanced portfolios, remaining robust under market regime shifts. These findings highlight the potential of combining RMT, deep learning, and power-law modeling to capture the intrinsic complexity of financial systems and enhance portfolio optimization under realistic conditions.

Keywords: RMT, ResNets, Power-law, Cryptocurrencies, Non-linear shrinkage

PACS: 89.65.Gh, 89.75.Da

## 1 Introduction

Random Matrix Theory (RMT) has played a pivotal role in elucidating complex interactions in nuclear physics [[1](https://arxiv.org/html/2510.19130v1#bib.bibx1)], revealing quantum chaos signatures [[2](https://arxiv.org/html/2510.19130v1#bib.bibx2)], and describing quantum transport phenomena [[3](https://arxiv.org/html/2510.19130v1#bib.bibx3)]. More recently, RMT has been successfully applied to denoise empirical covariance matrices and enhance optimal asset allocation in portfolio theory [[4](https://arxiv.org/html/2510.19130v1#bib.bibx4), [5](https://arxiv.org/html/2510.19130v1#bib.bibx5), [6](https://arxiv.org/html/2510.19130v1#bib.bibx6), [7](https://arxiv.org/html/2510.19130v1#bib.bibx7)]. Within this framework, several methodologies have been proposed to identify meaningful signals and suppress noise originating from the finite size of empirical samples [[4](https://arxiv.org/html/2510.19130v1#bib.bibx4), [8](https://arxiv.org/html/2510.19130v1#bib.bibx8)]. Furthermore, renewed attention has arisen in mathematical statistics, where advanced techniques grounded in free probability and deterministic equivalents have provided rigorous analytical tools for high-dimensional covariance estimation [[9](https://arxiv.org/html/2510.19130v1#bib.bibx9), [6](https://arxiv.org/html/2510.19130v1#bib.bibx6), [10](https://arxiv.org/html/2510.19130v1#bib.bibx10)].

These approaches share the common characteristic of focusing primarily on the eigenvalues of the covariance matrix, whose empirical distribution asymptotically converges to a deterministic function. In contrast, the role of eigenvectors has been largely secondary within these frameworks. In essence, RMT-based estimators improve covariance estimation by applying nonlinear shrinkage transformations to the eigenvalues while keeping the eigenvectors fixed [[11](https://arxiv.org/html/2510.19130v1#bib.bibx11), [5](https://arxiv.org/html/2510.19130v1#bib.bibx5), [12](https://arxiv.org/html/2510.19130v1#bib.bibx12)]. However, it has been demonstrated that the distance between the leading sample eigenvectors and their true population counterparts diverges without bound in high-dimensional settings [[13](https://arxiv.org/html/2510.19130v1#bib.bibx13)].

Therefore, this work proposes to exploit information contained in the eigenvectors to improve covariance matrix estimation. Our approach performs a spectral decomposition of the covariance matrix, estimating the eigenvectors through a state-of-the-art deep neural network model, while the eigenvalues are obtained via the nonlinear shrinkage method based on Random Matrix Theory (RMT) [[7](https://arxiv.org/html/2510.19130v1#bib.bibx7)]. In particular, we employ the Residual Neural Network (ResNet) architecture [[14](https://arxiv.org/html/2510.19130v1#bib.bibx14), [15](https://arxiv.org/html/2510.19130v1#bib.bibx15)], which is well-suited for deep architectures as it mitigates computational challenges by introducing shortcut connections that facilitate efficient gradient propagation toward optimal solutions.

This proposal is benchmarked against two alternative covariance estimators: one entirely based on the ResNet architecture and another fully derived from Random Matrix Theory (RMT). Additionally, we include the two-step estimator introduced in [[16](https://arxiv.org/html/2510.19130v1#bib.bibx16)], which incorporates the nested hierarchical organization of financial markets into advanced covariance estimation techniques. Since the main goal of this study is to enhance covariance matrix estimation for financial systems, we first introduce models designed to reproduce the stylized facts of market interactions. To the best of our knowledge, this is the first work to propose a power-law covariance model whose scree plot of eigenvalues follows a scaling behavior, thereby capturing the complex dynamics of financial markets. For comparison, we also consider a fully hierarchical model [[17](https://arxiv.org/html/2510.19130v1#bib.bibx17)] and a block-diagonal model [[16](https://arxiv.org/html/2510.19130v1#bib.bibx16)].

To validate the models in practice, we have considered a dataset composed of financial instruments known as cryptocurrencies. These assets are characterized by complex features that push traditional statistical methods to their limits. Specifically, cryptocurrencies do not follow a Gaussian distribution, exhibit heavy tails, abrupt jumps, asymmetry, and overall complex dynamics [[18](https://arxiv.org/html/2510.19130v1#bib.bibx18)].

Here, we carefully excluded pseudo-cryptocurrencies—i.e., coins that are merely replicas of fiat money—and retained only genuine blockchain projects or those that replicate exchange rates. Additionally, we pushed the estimators, particularly the deep learning ones, to their limits by training on a bull market period and testing on a bear market. This setup allows us to evaluate the model’s ability to handle structural changes and market regime shifts.

We find that both the nested hierarchy and power-law models adequately characterize the complex interactions within cryptocurrency markets. Moreover, both in simulations and in empirical cryptocurrency data, hybrid models—and more generally, deep learning-based models—significantly improve the estimation of the population covariance matrix on one hand, and, on the other, enhance financial metrics in out-of-sample walk-forward analyses.

Although the covariance matrix is not the only element involved in an investment strategy, its accurate estimation enables better control of volatility under different scenarios—not only within portfolio theory. For instance, one of the most recent and prestigious forecasting competitions found that the main determinant of predictive accuracy was the ability to control volatility, regardless of model complexity [[19](https://arxiv.org/html/2510.19130v1#bib.bibx19)].

On the other hand, while recent studies have explored the use of deep learning for estimating eigenvalues within invariant estimator frameworks [[20](https://arxiv.org/html/2510.19130v1#bib.bibx20)], or through reinforcement learning approaches to shrinkage estimation [[21](https://arxiv.org/html/2510.19130v1#bib.bibx21)], to the best of our knowledge, this is the first work to propose a hybrid method that integrates the theoretical robustness of RMT with the representational power of deep neural networks applied to eigenvectors, specifically leveraging the ResNet architecture.

Section 2 presents the investment strategy used to allocate capital across the set of cryptocurrencies. In Section 3, we introduce the covariance matrix estimators derived from both RMT and deep learning (ResNet), as well as the proposed hybrid and two-step estimators. Section 4 details the proposed covariance matrix models used in the simulations, highlighting that the power-law model represents a novel contribution not previously discussed in the literature. Section 5 presents and discusses the results of the simulations, while Section 6 analyzes the findings related to the cryptocurrency dataset. Finally, Section 7 concludes the study and discusses potential avenues for future research.

## 2 Asset allocation models

### 2.1 Portfolio Theory

Consider pp assets observed over nn trading days, and let si,ts\_{i,t} denote the price of asset i=1,…,pi=1,\dots,p at time t=1,…,nt=1,\dots,n. The logarithmic return ri,tr\_{i,t} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri,t=log⁡(si,tsi,t−1).r\_{i,t}=\log\left(\frac{s\_{i,t}}{s\_{i,t-1}}\right). |  | (1) |

The amount of capital invested in asset ii is represented by its portfolio weight, collected in the vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐰=(w1,…,wp)⊤.\mathbf{w}=(w\_{1},\dots,w\_{p})^{\top}. |  | (2) |

A positive weight corresponds to a *long position*, i.e., ownership of an asset, whereas a negative weight indicates a *short position*, meaning that the investor sells a borrowed asset, expecting to repurchase it later at a lower price.

Then, the portfolio return 𝐑\mathbf{R} is given by the dot product

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐑=𝐰⊤​𝐫.\mathbf{R}=\mathbf{w}^{\top}\mathbf{r}. |  | (3) |

The expected return of the portfolio, denoted by μR\mu\_{R}, is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | μR=𝔼​[𝐑]=𝐰⊤​𝔼​[𝐫]=𝐰⊤​𝝁,\mu\_{R}=\mathbb{E}[\mathbf{R}]=\mathbf{w}^{\top}\mathbb{E}[\mathbf{r}]=\mathbf{w}^{\top}\boldsymbol{\mu}, |  | (4) |

where 𝝁\boldsymbol{\mu} is the vector of expected returns for the individual assets.

The portfolio variance is expressed as a quadratic form of the population covariance matrix 𝚺\boldsymbol{\Sigma} of the asset returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σR2=𝐰⊤​𝚺​𝐰.\sigma\_{R}^{2}=\mathbf{w}^{\top}\boldsymbol{\Sigma}\mathbf{w}. |  | (5) |

Accordingly, the portfolio volatility is obtained as the square root of the variance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σR=𝐰⊤​𝚺​𝐰.\sigma\_{R}=\sqrt{\mathbf{w}^{\top}\boldsymbol{\Sigma}\mathbf{w}}. |  | (6) |

### 2.2 Minimum Variance Portfolio (MVP)

The mean–variance allocation strategy proposed by Markowitz [[22](https://arxiv.org/html/2510.19130v1#bib.bibx22)] seeks to solve the following quadratic optimization problem in order to minimize portfolio risk for a given level of expected return [[23](https://arxiv.org/html/2510.19130v1#bib.bibx23)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝐰​(ϕ)∈ℝp​𝐰⊤​𝝁−ϕ2​𝐰⊤​𝚺​𝐰subject to𝟏⊤​𝐰=1,\underset{\mathbf{w}(\phi)\in\mathbb{R}^{p}}{\max}\;\mathbf{w}^{\top}\boldsymbol{\mu}-\frac{\phi}{2}\,\mathbf{w}^{\top}\boldsymbol{\Sigma}\mathbf{w}\quad\text{subject to}\quad\mathbf{1}^{\top}\mathbf{w}=1, |  | (7) |

where ϕ\phi is interpreted as the risk-aversion parameter.

When ϕ→∞\phi\to\infty, the problem reduces to minimizing portfolio variance regardless of expected return:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐰​(∞)∈ℝp​12​𝐰⊤​𝚺​𝐰subject to𝟏⊤​𝐰=1.\underset{\mathbf{w}(\infty)\in\mathbb{R}^{p}}{\min}\;\frac{1}{2}\,\mathbf{w}^{\top}\boldsymbol{\Sigma}\mathbf{w}\quad\text{subject to}\quad\mathbf{1}^{\top}\mathbf{w}=1. |  | (8) |

The reduced problem minimizes portfolio volatility and is referred to as the Minimum Variance Portfolio (MVP). Moreover, it is possible to incorporate a no short-selling constraint by formulating the standard quadratic programming (QP) problem. In this case, the portfolio weights satisfy 𝐰≥0\mathbf{w}\geq 0, and a numerical solution is required [[24](https://arxiv.org/html/2510.19130v1#bib.bibx24)]. This constrained portfolio is also known as the long-only MVP, as it does not permit short positions or negative weights. In the following analysis, we will denote this portfolio as MVP+.

## 3 Covariance estimators

### 3.1 Random matrix denoising

A *naive estimator* of the population covariance matrix 𝚺\boldsymbol{\Sigma}, given the empirical or sample covariance matrix 𝐒\mathbf{S}, is simply

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚵naive=𝐒,\boldsymbol{\Xi}^{\text{naive}}=\mathbf{S}, |  | (9) |

which is an unbiased estimator of 𝚺\boldsymbol{\Sigma} when the number of variables pp is fixed and the number of observations n→∞n\to\infty [[25](https://arxiv.org/html/2510.19130v1#bib.bibx25)].

A non-linear shrinkage formula that minimizes the Frobenius loss has been proposed by Ledoit and Péché [[5](https://arxiv.org/html/2510.19130v1#bib.bibx5)], based on principles from RMT [[26](https://arxiv.org/html/2510.19130v1#bib.bibx26)]. In high-dimensional settings, the covariance matrix is estimated as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝚵LP\displaystyle\boldsymbol{\Xi}^{\text{LP}} | =∑k=1pξkLP​𝐯k​𝐯k⊤,where\displaystyle=\sum\_{k=1}^{p}\xi\_{k}^{\text{LP}}\,\mathbf{v}\_{k}\mathbf{v}\_{k}^{\top},\quad\text{where} |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ξkLP\displaystyle\xi^{\text{LP}}\_{k} | =limϵ→0+λk|1−q+q​λk​GS​(λk−i​ϵ)|2,\displaystyle=\lim\_{\epsilon\to 0^{+}}\frac{\lambda\_{k}}{\big|1-q+q\lambda\_{k}G\_{S}(\lambda\_{k}-i\epsilon)\big|^{2}}, |  | (11) |

and (λk,𝐯k)(\lambda\_{k},\mathbf{v}\_{k}) denote the eigenvalue–eigenvector pairs of 𝐒\mathbf{S}, and GSG\_{S} is the Stieltjes transform of 𝐒\mathbf{S}.

### 3.2 Residual Neural Network denoising

An estimator based on machine learning is proposed, employing the Residual Neural Network (ResNet) architecture [[14](https://arxiv.org/html/2510.19130v1#bib.bibx14)].
The implementation builds upon Convolutional Neural Networks (CNNs) [[27](https://arxiv.org/html/2510.19130v1#bib.bibx27)], which are designed to process grid-structured inputs and exploit strong spatial dependencies within local regions of the grid.
ResNet improves CNNs by introducing a novel neural architecture that incorporates *skip connections* [[28](https://arxiv.org/html/2510.19130v1#bib.bibx28)], allowing information from one layer to propagate to non-contiguous layers. Specifically, ResNet contains connections between layer ii and layer (i+r)(i+r) for r>1r>1, where ii is an arbitrary layer and rr denotes the skip length. Figure [1](https://arxiv.org/html/2510.19130v1#S3.F1 "Figure 1 ‣ 3.2 Residual Neural Network denoising ‣ 3 Covariance estimators ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")(a) illustrates the architecture of the residual block used for the covariance matrix denoising, setting r=2r=2.

![Refer to caption](figs/residual_block_inner_architecture_generic.jpeg)


(a)

![Refer to caption](figs/layers.png)


(b)

Figure 1: Network architecture. (a) Residual block with r=2r=2. (b) ResNet with 10 basic residual blocks.

The CNN learning process operates as follows: a *filter* is applied to the input layer to detect patterns, producing a *feature map* as the output. An activation function is then applied element-wise after each layer to introduce nonlinearity, regulate signal propagation, and constrain the output within a desired range of values.

In the residual module, the input layer consists of 64 filters of size 3×33\times 3, producing 64 feature maps with rectified linear unit (ReLU) nonlinearity. This base representation is then refined by two subsequent stacked 2D convolutional layers (Conv2D) to extract deeper features. The first Conv2D layer employs a ReLU activation function, whereas the second uses a linear activation function.
The add block implements the skip connection, combining the input (residual) with the output of the two Conv2D layers. In this way, the network learns only the residual correction rather than the full mapping, mitigating the vanishing gradient problem. The practical purpose of the skip connections is to enable effective gradient flow, allowing the learning algorithm to adaptively choose the level of nonlinearity applied to a given input.
Finally, the last block of the residual module applies a ReLU activation. The complete network architecture, shown in Figure [1](https://arxiv.org/html/2510.19130v1#S3.F1 "Figure 1 ‣ 3.2 Residual Neural Network denoising ‣ 3 Covariance estimators ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")(b), is constructed by repeating this loop and stacking ten basic residual blocks.
Using this ResNet architecture, and applying appropriate symmetrization along with a positive semidefinite (PSD) transformation, it becomes possible to learn and remove the noise present in the empirical covariance matrix. We denote the resulting estimator as 𝚵CNN\boldsymbol{\Xi}^{\text{CNN}}, reflecting the CNN-based structure of its inner layers.

We further propose a hybrid approach that leverages both the learning capabilities of the ResNet model and the theoretical properties of high-dimensional covariance estimation. The core idea is first to perform a spectral decomposition of the empirical covariance matrix:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐒=𝐕​𝚲​𝐕T\mathbf{S}=\mathbf{V}\mathbf{\Lambda}\mathbf{V}^{T} |  | (12) |

Here, 𝐕\mathbf{V} denotes the p×pp\times p matrix whose kk-th column is the eigenvector 𝐯k\mathbf{v}\_{k} of 𝐒\mathbf{S}, and 𝚲\mathbf{\Lambda} is the diagonal matrix containing the corresponding eigenvalues λ\lambdas.
The hybrid estimator applies the ResNet learning model to the eigenvectors (without symmetrization or PSD transformation), while the eigenvalues are processed using the nonlinear shrinkage RMT-based formula in Eq. ([11](https://arxiv.org/html/2510.19130v1#S3.E11 "In 3.1 Random matrix denoising ‣ 3 Covariance estimators ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")). Formally, the hybrid estimator is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚵H=𝚵CNN​(𝐕)​𝚵​(𝚲)​𝚵CNN​(𝐕)⊤,\boldsymbol{\Xi}^{H}=\boldsymbol{\Xi}^{\text{CNN}}(\mathbf{V})\,\boldsymbol{\Xi}(\mathbf{\Lambda})\,\boldsymbol{\Xi}^{\text{CNN}}(\mathbf{V})^{\top}, |  | (13) |

where 𝚵​(𝐕)\boldsymbol{\Xi}(\mathbf{V}) and 𝚵​(𝚲)\boldsymbol{\Xi}(\mathbf{\Lambda}) denote the application of the operator 𝚵\boldsymbol{\Xi} to the matrix of eigenvectors and the diagonal matrix of eigenvalues, respectively.
This hybrid approach combines the data-driven flexibility of ResNet to capture complex dependencies in the eigenvectors, while exploiting the theoretical guarantees of RMT for consistent eigenvalue estimation in high-dimensional settings.

### 3.3 Hierarchical clustering denoising

A novel approach to covariance matrix estimation was proposed by Tumminello et al. [[29](https://arxiv.org/html/2510.19130v1#bib.bibx29)] using a hierarchical clustering algorithm. The procedure begins by transforming the empirical covariance matrix 𝐒\mathbf{S} into the corresponding correlation matrix 𝐂\mathbf{C}.
Next, the transformation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃=𝟏𝟏⊤−𝐂\mathbf{D}=\mathbf{11}^{\top}-\mathbf{C} |  | (14) |

is applied, which satisfies the axioms of a distance measure, where 𝟏\mathbf{1} is a pp-dimensional vector of ones. A dendrogram is then constructed from 𝐃\mathbf{D} using Average Linkage Clustering Analysis (ALCA) [[25](https://arxiv.org/html/2510.19130v1#bib.bibx25)], and the distance ρ\rho between clusters at each hierarchical level is computed.
This procedure yields a dissimilarity matrix 𝐃​(ρ)\mathbf{D}(\rho) as a function of ρ\rho, from which the filtered covariance matrix is recovered via the inverse transformation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚵ALCA=𝐇1/2​(𝟏𝟏⊤−𝐃​(ρ))​𝐇1/2,\boldsymbol{\Xi}^{\text{ALCA}}=\mathbf{H}^{1/2}\,(\mathbf{11}^{\top}-\mathbf{D}(\rho))\,\mathbf{H}^{1/2}, |  | (15) |

where 𝐇\mathbf{H} is the diagonal matrix of variances used to rescale the correlation matrix back to the original covariance scale.

A state-of-the-art estimator designed to address both the heterogeneous structure of financial markets and the challenges of high-dimensional settings was proposed in [[16](https://arxiv.org/html/2510.19130v1#bib.bibx16)]. The core idea is to first apply our proposed single-step estimators, followed by a hierarchical filtering step. We consider the following combinations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝚵2​S​(LP)\displaystyle\boldsymbol{\Xi}^{2S(\text{LP})} | :=𝚵ALCA​(𝚵LP),\displaystyle:=\boldsymbol{\Xi}^{\text{ALCA}}\big(\boldsymbol{\Xi}^{\text{LP}}\big), |  | (16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝚵2​S​(CNN)\displaystyle\boldsymbol{\Xi}^{2S(\text{CNN})} | :=𝚵ALCA​(𝚵CNN),\displaystyle:=\boldsymbol{\Xi}^{\text{ALCA}}\big(\boldsymbol{\Xi}^{\text{CNN}}\big), |  | (17) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝚵2​S​(H)\displaystyle\boldsymbol{\Xi}^{2S(\text{H})} | :=𝚵ALCA​(𝚵H).\displaystyle:=\boldsymbol{\Xi}^{\text{ALCA}}\big(\boldsymbol{\Xi}^{H}\big). |  | (18) |

The mathematical justification for this two-step estimator is discussed in [[16](https://arxiv.org/html/2510.19130v1#bib.bibx16)] and is based on the following arguments:
(i) applying an RMT-based estimator in the first step reduces the noise and estimation error associated with the largest eigenvalues, and
(ii) applying a subsequent filtering step via hierarchical clustering mitigates the inconsistency of the top eigenvectors, which is inherently present in RMT covariance estimators [[13](https://arxiv.org/html/2510.19130v1#bib.bibx13)].
Here, this reasoning is extended to the newly proposed estimators 𝚵CNN\boldsymbol{\Xi}^{\text{CNN}} and 𝚵H\boldsymbol{\Xi}^{H}, where the second step can be interpreted as a regularization procedure to avoid overfitting.

## 4 Covariance models

To evaluate the performance of the proposed covariance matrix estimators, we consider the following data-generating process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐘=𝚺​𝐗,\mathbf{Y}=\sqrt{\boldsymbol{\Sigma}}\,\mathbf{X}, |  | (19) |

where 𝐗\mathbf{X} is a p×np\times n random matrix whose entries are independent and identically distributed according to a standard Gaussian distribution, and 𝚺\boldsymbol{\Sigma} is a p×pp\times p population covariance matrix.
Given a model specification for 𝚺\boldsymbol{\Sigma}, we can obtain the sample covariance realization as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐒=1n​𝐘𝐘T=1n​𝚺​𝐗𝐗T​𝚺,\mathbf{S}=\frac{1}{n}\mathbf{Y}\mathbf{Y}^{T}=\frac{1}{n}\sqrt{\boldsymbol{\Sigma}}\,\mathbf{X}\mathbf{X}^{T}\sqrt{\boldsymbol{\Sigma}}, |  | (20) |

which represents the noisy empirical counterpart of the true covariance matrix.
In this study, we analyze the following population models for 𝚺\boldsymbol{\Sigma}.

* (1)

  A block-diagonal correlation structure defined as

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝚺=𝐋𝐋T,\boldsymbol{\Sigma}=\mathbf{L}\mathbf{L}^{T}, |  | (21) |

  where 𝐋\mathbf{L} is a rectangular matrix of dimension p×kp\times k, with kk denoting the number of blocks.
  In particular, we set p=100p=100 and k=12k=12, with heterogeneous block sizes given by [3,3,4,5,6,7,7,9,11,13,15,17][3,3,4,5,6,7,7,9,11,13,15,17], but with equal intra-block correlation intensity γ=0.3\gamma=0.3.
  To ensure a proper correlation matrix, the diagonal entries are set to one.
  Figure [2](https://arxiv.org/html/2510.19130v1#S4.F2 "Figure 2 ‣ 4 Covariance models ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")(a) displays the population model under these specifications (left) and a finite-sample realization with n=200n=200 (right).
  This block-independent and homogeneous structure model has been previously examined in [[16](https://arxiv.org/html/2510.19130v1#bib.bibx16)].
* (2)

  A completely nested hierarchical covariance model, where using the same general structure of eq. [21](https://arxiv.org/html/2510.19130v1#S4.E21 "In item (1) ‣ 4 Covariance models ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications"), the heterogeneity is integrated through the matrix 𝐋\mathbf{L} of dimension p×pp\times p is given by

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝐋=(γγ…γγγγ…γ0⋮⋮⋱⋮⋮γγ…00γ0…00).\mathbf{L}=\begin{pmatrix}\gamma&\gamma&\dots&\gamma&\gamma\\ \gamma&\gamma&\dots&\gamma&0\\ \vdots&\vdots&\ddots&\vdots&\vdots\\ \gamma&\gamma&\dots&0&0\\ \gamma&0&\dots&0&0\\ \end{pmatrix}. |  | (22) |

  Here, we set γ=0.1\gamma=0.1.
  Figure [2](https://arxiv.org/html/2510.19130v1#S4.F2 "Figure 2 ‣ 4 Covariance models ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")(b) presents the population model under these specifications (left) with p=100p=100, and a finite-sample realization with n=200n=200 (right).
  This system was originally proposed in [[17](https://arxiv.org/html/2510.19130v1#bib.bibx17)] as a model to characterize the complex interaction structure of financial markets.
  In particular, the population eigenvalues of this system correspond to the solutions of a symmetric tridiagonal matrix and exhibit deep mathematical connections with Fibonacci and Lucas numbers [[30](https://arxiv.org/html/2510.19130v1#bib.bibx30)].
* (3)

  A power-law model of the form

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝚺=𝐎​𝚲​𝐎T,\mathbf{\Sigma}=\mathbf{O}\mathbf{\Lambda}\mathbf{O}^{T}, |  | (23) |

  where 𝐎\mathbf{O} is a random orthogonal matrix of dimension p×pp\times p, and 𝚲\mathbf{\Lambda} is a diagonal matrix of the same dimension with entries

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | λi=i−α,i=1,…,p,\lambda\_{i}=i^{-\alpha},\quad i=1,\dots,p, |  | (24) |

  representing the eigenvalues of 𝚺\mathbf{\Sigma}.
  By construction, these eigenvalues follow a power-law decay.
  Figure [2](https://arxiv.org/html/2510.19130v1#S4.F2 "Figure 2 ‣ 4 Covariance models ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")(c) displays the population model under these specifications (left), considering p=100p=100 and α=1.5\alpha=1.5, along with a finite-sample realization for n=200n=200 (right).
  To the best of our knowledge, this formulation is presented here for the first time as a covariance matrix representation of power-law interactions.

![Refer to caption](figs/model1/simulation_model1.png)


(a)

![Refer to caption](figs/complex/simulation_complex.png)


(b)

![Refer to caption](figs/powerlaw/simulation_powerlaw.png)


(c)

Figure 2: Covariance models. (a) Block diagonal correlation model. (b) Nested hierarchical model. (c) Power-law model. Left: population covariances. Right: sample realization.

Figure [3](https://arxiv.org/html/2510.19130v1#S4.F3 "Figure 3 ‣ 4 Covariance models ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications") presents the log-log scree plot of the eigenvalues for each model.
Model 1 exhibits k=12k=12 non-degenerate eigenvalues, whose magnitudes correspond to the size of each of the kk blocks (see [[16](https://arxiv.org/html/2510.19130v1#bib.bibx16)]).
Model 2 displays the intriguing property that its eigenvalue spectrum approximately follows a power-law decay.
Due to this property, it has been conjectured in [[17](https://arxiv.org/html/2510.19130v1#bib.bibx17)] that it can capture the stylized facts underlying the complex interactions of financial markets.
In the case of Model 3, the power-law behavior is imposed by construction with a slope of α=1.5\alpha=1.5, providing a further step toward characterizing the complex interactions of financial markets through their covariance structure.

![Refer to caption](figs/model1/screeplot_model1.png)


(a)

![Refer to caption](figs/complex/screeplot_complex.png)


(b)

![Refer to caption](figs/powerlaw/screeplot_powerlaw.png)


(c)

Figure 3: Scree plot of eigenvalues for (a) model 1, (c) model 2, and (e) model 3.

Figure [4](https://arxiv.org/html/2510.19130v1#S4.F4 "Figure 4 ‣ 4 Covariance models ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications") displays the dendrograms associated with each covariance model, constructed using the same methodology as the hierarchical estimator but employing the Single Linkage Clustering Algorithm (SLCA).
Model 1 exhibits a homogeneous hierarchical structure that successfully recovers the k=12k=12 blocks of the population model.
In contrast, Model 2 reveals hierarchies of increasing size, consistent with the structure imposed in the population model.
Finally, the dendrogram corresponding to Model 3 also displays an increasing degree of nested hierarchies; however, its block structure is heterogeneous due to the random signatures inherited from the orthogonal eigenvectors (see Eq. [23](https://arxiv.org/html/2510.19130v1#S4.E23 "In item (3) ‣ 4 Covariance models ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")).

![Refer to caption](figs/model1/dendogram_SLCA_model1.png)


(a)

![Refer to caption](figs/complex/dendogram_SLCA_complex.png)


(b)

![Refer to caption](figs/powerlaw/dendogram_SLCA_powerlaw.png)


(c)

Figure 4: Associated dendrogram of (a) model 1, (b) model 2, and (c) model 3. For illustrative purposes, the descendant links below a cluster node kk are equally colored if kk is the first node below the cut threshold t(=0.7)t(=0.7).

## 5 Simulations

We conduct a Monte Carlo simulation consisting of m=1000m=1000 realizations of the sample covariance matrix for each of the three population covariance models.
The sample covariance matrices are generated from finite data matrices of dimensions p=100p=100 and n=200n=200.
For each realization, the noise is filtered by applying the covariance matrix estimators introduced in Section [3](https://arxiv.org/html/2510.19130v1#S3 "3 Covariance estimators ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications").
Subsequently, we evaluate the performance of the estimators using the Frobenius (FF) and Minimum Variance (M​VMV) loss functions, computed between the filtered matrix 𝚵\mathbf{\Xi} and the true population covariance matrix 𝚺\mathbf{\Sigma}.
These loss functions are defined as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | F​(𝚵,𝚺)\displaystyle F(\mathbf{\Xi},\mathbf{\Sigma}) | =\displaystyle= | 1p​Tr⁡[(𝚵−𝚺)​(𝚵−𝚺)T],\displaystyle\frac{1}{p}\operatorname{Tr}\!\left[(\mathbf{\Xi}-\mathbf{\Sigma})(\mathbf{\Xi}-\mathbf{\Sigma})^{T}\right], |  | (25) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | M​V​(𝚵,𝚺)\displaystyle MV(\mathbf{\Xi},\mathbf{\Sigma}) | =\displaystyle= | Tr⁡(𝚺−1​𝚵​𝚺−1)/p[Tr⁡(𝚺−1)/p]2−1Tr⁡(𝚵−1)/p.\displaystyle\frac{\operatorname{Tr}(\mathbf{\Sigma}^{-1}\mathbf{\Xi}\mathbf{\Sigma}^{-1})/p}{[\operatorname{Tr}(\mathbf{\Sigma}^{-1})/p]^{2}}-\frac{1}{\operatorname{Tr}(\mathbf{\Xi}^{-1})/p}. |  | (26) |

Tables [1](https://arxiv.org/html/2510.19130v1#S5.T1 "Table 1 ‣ 5 Simulations ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications"), [2](https://arxiv.org/html/2510.19130v1#S5.T2 "Table 2 ‣ 5 Simulations ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications"), and [3](https://arxiv.org/html/2510.19130v1#S5.T3 "Table 3 ‣ 5 Simulations ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications") summarize the performance of the estimators in terms of the average FF and M​VMV loss functions over the m=1000m=1000 Monte Carlo replications, corresponding to each covariance model, respectively.
For the estimators based on the machine learning approach, the ResNet architecture was trained using the Adam optimizer with an initial learning rate of 10−310^{-3}.
The internal loss function used to penalize the difference between the predicted and target matrices was the mean squared error (MSE).
Training was performed with a batch size of 16 over 10 epochs, using a training dataset of 100 samples, with 20% reserved for validation.

Table 1: Block diagonal correlation (model 1). Performance of estimators in terms of ⟨F​(𝚺,𝚵)⟩\langle F(\mathbf{\Sigma},\mathbf{\Xi})\rangle and ⟨M​V​(𝚺,𝚵)⟩\langle MV(\mathbf{\Sigma},\mathbf{\Xi})\rangle, where ⟨⋅⟩\langle\cdot\rangle represents the average over m=1000m=1000 realizations of data samples with dimensions p=100,n=200p=100,n=200.

| Estimator | ⟨F⟩\langle F\rangle | ⟨M​V⟩\langle MV\rangle |
| --- | --- | --- |
| Ξn​a​i​v​e\Xi^{naive} | 0.507937 | 0.486611 |
| ΞL​P\Xi^{LP} | 0.065429 | 0.026864 |
| ΞC​N​N\Xi^{CNN} | 0.035051 | 0.032022 |
| ΞH\Xi^{H} | 1.054531 | 0.003001 |
| ΞA​L​C​A\Xi^{ALCA} | 0.099357 | 0.057769 |
| Ξ2​S​(L​P)\Xi^{2S(LP)} | 0.056593 | 0.017976 |
| Ξ2​S​(C​N​N)\Xi^{2S(CNN)} | 0.034521 | 0.030575 |
| Ξ2​S​(H)\Xi^{2S(H)} | 1.054501 | 0.002551 |




Table 2: Completely nested hierarchical covariance (model 2). Performance of estimators in terms of ⟨F​(𝚺,𝚵)⟩\langle F(\mathbf{\Sigma},\mathbf{\Xi})\rangle and ⟨M​V​(𝚺,𝚵)⟩\langle MV(\mathbf{\Sigma},\mathbf{\Xi})\rangle, where ⟨⋅⟩\langle\cdot\rangle represents the average over m=1000m=1000 realizations of data samples with dimensions p=100,n=200p=100,n=200.

| Estimator | ⟨F⟩\langle F\rangle | ⟨M​V⟩\langle MV\rangle |
| --- | --- | --- |
| Ξn​a​i​v​e\Xi^{naive} | 0.204916 | 0.002551 |
| ΞL​P\Xi^{LP} | 0.215718 | 0.001520 |
| ΞC​N​N\Xi^{CNN} | 0.186761 | 0.000607 |
| ΞH\Xi^{H} | 3.410518 | 0.000249 |
| ΞA​L​C​A\Xi^{ALCA} | 0.361030 | 0.009575 |
| Ξ2​S​(L​P)\Xi^{2S(LP)} | 0.370093 | 0.009559 |
| Ξ2​S​(C​N​N)\Xi^{2S(CNN)} | 0.349912 | 0.007677 |
| Ξ2​S​(H)\Xi^{2S(H)} | 3.414401 | 0.000499 |




Table 3: Power-law (model 3). Performance of estimators in terms of ⟨F​(𝚺,𝚵)⟩\langle F(\mathbf{\Sigma},\mathbf{\Xi})\rangle and ⟨M​V​(𝚺,𝚵)⟩\langle MV(\mathbf{\Sigma},\mathbf{\Xi})\rangle, where ⟨⋅⟩\langle\cdot\rangle represents the average over m=1000m=1000 realizations of data samples with dimensions p=100,n=200p=100,n=200.

| Estimator | ⟨F⟩\langle F\rangle | ⟨M​V⟩\langle MV\rangle |
| --- | --- | --- |
| Ξn​a​i​v​e\Xi^{naive} | 0.000356 | 0.001254 |
| ΞL​P\Xi^{LP} | 0.000356 | 0.000844 |
| ΞC​N​N\Xi^{CNN} | 0.004365 | 0.001281 |
| ΞH\Xi^{H} | 0.006345 | 0.000239 |
| ΞA​L​C​A\Xi^{ALCA} | 0.001992 | 0.010246 |
| Ξ2​S​(L​P)\Xi^{2S(LP)} | 0.001973 | 0.010202 |
| Ξ2​S​(C​N​N)\Xi^{2S(CNN)} | 0.004852 | 0.002135 |
| Ξ2​S​(H)\Xi^{2S(H)} | 0.006345 | 0.000238 |

For Model 1, the best-performing estimator in terms of the FF loss is 𝚵2​S​(C​N​N)\mathbf{\Xi}^{2S(CNN)}, whereas the best performance in terms of the M​VMV loss is achieved by 𝚵2​S​(H)\mathbf{\Xi}^{2S(H)}.
In the case of Model 2, the estimators 𝚵C​N​N\mathbf{\Xi}^{CNN} and 𝚵H\mathbf{\Xi}^{H} exhibit the lowest FF and M​VMV losses, respectively.
The results for Model 3 are particularly intriguing.
In this case, none of the estimators significantly outperform the naive estimator in terms of the FF loss, while in terms of the M​VMV loss, most estimators struggle to improve upon it.
The only estimators that surpass the naive benchmark are 𝚵L​P\mathbf{\Xi}^{LP}, 𝚵H\mathbf{\Xi}^{H}, and 𝚵2​S​(H)\mathbf{\Xi}^{2S(H)}, with the latter showing the overall best performance.

On the other hand, it can be observed that, in general, both 𝚵H\mathbf{\Xi}^{H} and 𝚵2​S​(H)\mathbf{\Xi}^{2S(H)} perform poorly in terms of the FF loss but substantially reduce the M​VMV loss.
This behavior can be explained by the fact that the FF loss accounts for errors in all individual entries of the covariance matrix, making it highly sensitive to small residual noise.
In contrast, the M​VMV loss captures deviations along the principal directions of variance, and can therefore exhibit significant improvement even when minor entry-wise noise remains.
Consequently, the hybrid estimators are more effective at suppressing noise in the dominant eigendirections of the covariance matrix.
This phenomenon becomes more pronounced as the degree of underlying structure increases, as observed in Models 2 and 3.

## 6 Empirical data

We analyze the daily returns of the p=89p=89 major (non-stable) cryptocurrencies by market capitalization over a five-year period, from 2020-08-02 to 2025-07-31, yielding a total of n=1825n=1825 observations. The data are retrieved using the yfinance API. The preprocessing pipeline begins by querying the top 400 cryptocurrencies by market capitalization. We then remove all coins with more than 1% of missing values and impute the remaining gaps using the last observed price (forward fill). To enhance dataset reliability, we further exclude the top 10% most volatile cryptocurrencies. This filtering step aims to mitigate distortions caused by herding behaviors such as *pump-and-dump* schemes or trader confusion arising from typographical errors in coin identifiers. Finally, we exclude all stablecoins (a total of 21), such as USDT or EURS, as their values are designed to remain pegged to fiat currencies or commodities (e.g., gold) and thus do not reflect the intrinsic dynamics of cryptocurrency markets.

In Figure [5](https://arxiv.org/html/2510.19130v1#S6.F5 "Figure 5 ‣ 6 Empirical data ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")(a), we present the empirical covariance matrix of the cryptocurrency dataset. The assets have been ordered using the seriation algorithm proposed by [[31](https://arxiv.org/html/2510.19130v1#bib.bibx31)] with a twofold objective: (i) to enhance the graphical representation by positioning assets with similar covariance patterns closer to each other, and (ii) to improve the ability of deep learning estimators to detect and learn the structural dependencies within the noisy covariance matrices. The resulting ordered covariance matrix exhibits patterns that closely resemble those generated by the power-law model, suggesting that the empirical structure of the cryptocurrency market may share similar scaling properties.
Figure [5](https://arxiv.org/html/2510.19130v1#S6.F5 "Figure 5 ‣ 6 Empirical data ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")(b) displays the scree plot of the eigenvalues of the empirical covariance matrix. The observed behavior closely resembles that of Models 2 and 3, with the exception of a few outliers in the tails. Moreover, the dendrogram presented in Figure [5](https://arxiv.org/html/2510.19130v1#S6.F5 "Figure 5 ‣ 6 Empirical data ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")(c) exhibits a hierarchical pattern qualitatively consistent with the structures observed in these two models. These results indicate that our proposed covariance models effectively capture the stylized facts present in the empirical cryptocurrency dataset.

![Refer to caption](figs/cryptos/covariance_nonstable.png)


(a)

![Refer to caption](figs/cryptos/screeplot_nonstable.png)


(b)

![Refer to caption](figs/cryptos/dendogram_SLCA_nonstable.png)


(c)

Figure 5: Cryptocurrency empirical data (a) Covariance matrix of ordered elements. (b) Scree plot of eigenvalues. (c) Dendrogram under the same methodology as the hierarchical estimator with single linkage (SLCA). For illustrative purpose the descendant links below a cluster node kk are equally colored if kk is the first node below the cut threshold t(=0.7)t(=0.7)

We split our dataset into training and testing periods. The splitting point is set to 2021-11-09, corresponding to the maximum closing value of Bitcoin (BTC) during the pandemic turmoil.111The absolute peak occurred on November 10, 2021; however, we consider the midnight value as the closing price. Following this date, prices began to decline, reaching a local minimum in November 2022 during the FTX crisis. This partition enables the model to learn under bull market conditions and to be subsequently evaluated under bear market dynamics, thereby facilitating an assessment of its robustness across contrasting market regimes.

Starting from 2021-11-09, we conducted a walk-forward analysis (rolling-window backtesting) using in-sample and out-of-sample covariance matrices computed over N=182N=182 trading days, with portfolio rebalancing performed at the same frequency. In total, the portfolio was rebalanced seven times, covering the investment period from 2021-11-09 to 2025-05-05.
Thus, we obtain the optimal portfolio allocations 𝐰\mathbf{w} by applying the MVP+ investment strategy, using as input each of the covariance estimators presented in Section [3](https://arxiv.org/html/2510.19130v1#S3 "3 Covariance estimators ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications"), computed over the in-sample data.
For the ResNet-based estimators (𝚵C​N​N\mathbf{\Xi}^{CNN}, 𝚵2​S​(C​N​N)\mathbf{\Xi}^{2S(CNN)}, 𝚵H\mathbf{\Xi}^{H}, and 𝚵2​S​(H)\mathbf{\Xi}^{2S(H)}), the model is retrained at each rebalancing point using an extended training dataset that includes the in-sample period plus approximately one additional preceding year (282 days). The rationale is to initiate training with the first observation of the complete dataset and subsequently apply a consistent rolling-window scheme, maintaining a constant number of training observations across all rebalancing scenarios.

Using a stride of 1, we thus obtain a training sample of 100 datasets, each of dimension p×Np\times N, to apply the learning process. The ResNet algorithm is configured using the same settings as in the simulation study. Next, portfolio returns are computed by multiplying the in-sample allocations 𝐰i​n\mathbf{w}\_{in} with the out-of-sample returns 𝐑o​u​t\mathbf{R}\_{out}. Figure [6](https://arxiv.org/html/2510.19130v1#S6.F6 "Figure 6 ‣ 6 Empirical data ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")(a) displays the cumulative returns for each estimator throughout the walk-forward analysis, with the rebalancing dates indicated by grey dashed vertical lines.
Figure [6](https://arxiv.org/html/2510.19130v1#S6.F6 "Figure 6 ‣ 6 Empirical data ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications")(b) shows the performance of the top 12 individual cryptocurrencies over the same period. The returns of individual cryptocurrencies exhibit greater volatility, reflecting higher risk, and consequently they can achieve higher cumulative returns compared to the diversified portfolios.

![Refer to caption](figs/cryptos/Walk_Forward_long_nonstable.png)


(a)

![Refer to caption](figs/cryptos/cumreturns_top_nonstable.png)


(b)

Figure 6: (a) Walk-forward cumulative returns on empirical data for MVP+. The weights are optimized with Ti​n=182T\_{in}=182 days, applied over To​u​t=182T\_{out}=182, and rebalancing every Δ​T=182\Delta T=182 days. (b) Cumulative returns of the top 12-performing individual cryptocurrencies under the buy-and-hold strategy. The vertical axis is on a logarithmic scale for better visualization.

Table [4](https://arxiv.org/html/2510.19130v1#S6.T4 "Table 4 ‣ 6 Empirical data ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications") presents the walk-forward portfolio performance across various financial metrics for each of the covariance estimators. As a benchmark, we also include the performance of a uniform portfolio (UU), in which capital is equally allocated across all assets.

| Estimator | Cumulative Return | Annual Return | Annual Volatility | Sharpe Ratio | Maximum Drawdown | Turnover |
| --- | --- | --- | --- | --- | --- | --- |
| UU | 0.25 | -33.00% | 66.52% | -0.5 | -84.56% | 0 |
| Ξn​a​i​v​e\Xi^{naive} | 0.88 | -3.66% | 39.10% | -0.09 | -65.63% | 1.02 |
| ΞL​P\Xi^{LP} | 0.71 | -9.24% | 43.75% | -0.21 | -73.35% | 1.13 |
| ΞC​N​N\Xi^{CNN} | 1.54 | 13.19% | 46.79% | 0.28 | -63.74% | 1.3 |
| ΞH\Xi^{H} | 1.4 | 10.17% | 54.44% | 0.19 | -76.43% | 0 |
| ΞA​L​C​A\Xi^{ALCA} | 1.09 | 2.46% | 40.71% | 0.06 | -66.24% | 1 |
| Ξ2​S​(L​P)\Xi^{2S(LP)} | 0.75 | -7.78% | 43.99% | -0.18 | -73.75% | 1.22 |
| Ξ2​S​(C​N​N)\Xi^{2S(CNN)} | 1.74 | 17.14% | 46.60% | 0.37 | -63.63% | 1.34 |
| Ξ2​S​(H)\Xi^{2S(H)} | 1.4 | 10.17% | 54.44% | 0.19 | -76.43% | 0 |

Table 4: Walk-forward portfolio performance for the cryptocurrency market under the MVP+ investment strategy. The weights are optimized with Ti​n=182T\_{in}=182 days, applied over To​u​t=182T\_{out}=182, and rebalancing every Δ​T=182\Delta T=182 days.

It can be observed that the highest cumulative portfolio return is achieved using the 𝚵2​S​(C​N​N)\mathbf{\Xi}^{2S(CNN)} estimator. By examining annualized returns, computed as the geometric mean of portfolio returns scaled by a factor of 365 to approximate yearly performance, we find that only the *ResNet*-based estimators and the *ALCA* estimator generate positive returns (see third column).

The annual portfolio volatility is measured by eq. [6](https://arxiv.org/html/2510.19130v1#S2.E6 "In 2.1 Portfolio Theory ‣ 2 Asset allocation models ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications") and also multiplied by the factor 365 to obtain a proxy. Interestingly, the *naive* estimator reaches the minimum value under this metric. Thus, an increase in mean return does not necessarily imply a decrease in standard deviation. The Sharpe Ratio, defined as the ratio between the mean and standard deviation of the portfolio return, gives us a fairer number to compare different investments. Under this measure, the most equilibrated portfolio is obtained again by the 𝚵2​S​(C​N​N)\mathbf{\Xi}^{2S(CNN)} estimator.

The maximum drawdown measures the largest peak-to-trough decline in the cumulative return of the investment portfolio expressed as a percentage. This measure represents the maximum loss presented in the investment.
Also, the 𝚵2​S​(C​N​N)\mathbf{\Xi}^{2S(CNN)} improve the loss to −63.63%-63.63\%. Yet, the improvement is marginal in relation to the *naive* estimator, which is of −65.65%-65.65\%. Finally, turnover measures the absolute difference between the asset weights at consecutive periods, normalized by the number of periods. A high value is associated with high transaction fees. This number ranges between 0 and 2, with 1 meaning that half of the assets reallocate in every rebalancing. In this case, the 𝚵H\mathbf{\Xi}^{H} and 𝚵2​S​(H)\mathbf{\Xi}^{2S(H)} estimators do not involve any reallocation. In fact, this particular strategy allocates 100% of the portfolio to BTC-USD at all times.

Figure [5](https://arxiv.org/html/2510.19130v1#S6.T5 "Table 5 ‣ 6 Empirical data ‣ Denoising Complex Covariance Matrices with Hybrid ResNet and Random Matrix Theory: Cryptocurrency Portfolio Applications") shows the equivalent financial metrics but for the buy & hold strategy of investing in individual cryptocurrencies through the walk-forward period. Notice that here, the turnover metric is not measured because we never rebalance. Interestingly, several coins surpass the performance of the combination of a state-of-the-art covariance estimator and the classical investment strategy MVP+. Even accounting for the trade-off measured by the Sharpe Ratio and the Maximum Drawdown, crypto like GT-USD outperforms all strategies.
Therefore, an important direction for future research is to integrate asset selection into the overall covariance estimation and portfolio allocation framework.

| Cryptocurrency | Cumulative Return | Annual Return | Annual Volatility | Sharpe Ratio | Maximum Drawdown |
| --- | --- | --- | --- | --- | --- |
| ZANO-USD | 3.28 | 40.50% | 134.62% | 0.30 | -92.06% |
| GT-USD | 2.90 | 35.61% | 53.50% | 0.67 | -62.41% |
| LEO-USD | 2.64 | 32.13% | 52.74% | 0.61 | -55.67% |
| VRSC-USD | 2.44 | 29.09% | 132.76% | 0.22 | -84.75% |
| TRX-USD | 2.26 | 26.28% | 65.97% | 0.40 | -59.52% |
| RENDER-USD | 2.11 | 23.87% | 129.75% | 0.18 | -95.83% |
| XRP-USD | 1.67 | 15.73% | 84.43% | 0.19 | -75.53% |
| OKB-USD | 1.62 | 14.91% | 67.45% | 0.22 | -68.81% |
| XCN-USD | 1.54 | 13.10% | 52.05% | 0.25 | -76.42% |
| MX-USD | 1.49 | 12.17% | 66.73% | 0.18 | -78.22% |
| WBTC-USD | 1.40 | 10.19% | 54.27% | 0.19 | -76.55% |
| BTC-USD | 1.40 | 10.17% | 54.44% | 0.19 | -76.43% |

Table 5: Walk-forward portfolio performance for the top 12 individual cryptocurrencies under the buy & hold strategy.

## 7 Conclusion

We found that the two-step estimator based on the ResNet architecture (𝚵2​S​(C​N​N)\mathbf{\Xi}^{2S(CNN)}) minimizes the Frobenius loss function for the block-diagonal model. For the same model, the two-step hybrid estimator (𝚵2​S​(H)\mathbf{\Xi}^{2S(H)}) attains the minimum value of the MV loss function. As the complexity of the covariance model increases, we observe that applying the second filtering step becomes unnecessary; in such cases, the single-step estimators (𝚵C​N​N\mathbf{\Xi}^{CNN}) and (𝚵H\mathbf{\Xi}^{H}) are sufficient to minimize noise with respect to the Frobenius and MV losses, respectively.
On the other hand, an interesting phenomenon arises when the covariance model follows a power-law structure: in this case, none of the state-of-the-art estimators outperform the naive one in terms of the Frobenius loss. However, regarding the MV loss, the two-step hybrid estimator achieves the lowest noise level. Overall, a consistent pattern emerges MV loss systematically decreases across all models when using the ResNet-based estimators.
The distinctive point here is that the MV loss captures deviations along the principal directions of variance and, as such, is more suitable for portfolio optimization applications.

On the other hand, when considering empirical data from the cryptocurrency market, we observe that the covariance structure, the scree plot, and the dendrogram exhibit stylized facts similar to those found in both the fully hierarchical model and the power-law model. Thus, we initially confirm the conjecture proposed in [[17](https://arxiv.org/html/2510.19130v1#bib.bibx17)], which states that the first model adequately characterizes the complex dynamics of financial instruments—this time applied to a set of cryptocurrencies. Furthermore, we extend this conjecture to a new model based on power-law behavior.

Focusing on the specific dataset analyzed, we find that the best financial metrics were generally obtained using the (𝚵2​S​(C​N​N))(\mathbf{\Xi}^{2S(CNN)}) estimator within the MVP+ portfolio framework. This result holds even under the challenging configuration of our experiment, where the training set corresponded to a bull market period, while the testing set covered a heterogeneous phase that began with a bear market trend.

Nevertheless, although these results are promising in terms of adequately characterizing the complex dynamics of cryptocurrencies and proposing a hybrid estimator that combines the advantages of state-of-the-art neural network models with the analytical foundations of random matrix theory, they are not sufficient to achieve the maximum cumulative return. When comparing with the performance of individual assets, we find that there are instruments capable of nearly tripling the initial capital while offering a better balance between risk exposure and profitability (Sharpe Ratio). Therefore, from a practical standpoint, there is still room for improvement in the search for more profitable strategies. In this regard, it would be interesting to continue combining methodologies and to incorporate the last missing ingredient—one that is uncommon within the econophysics field: asset selection and valuation from a fundamental analysis perspective [[32](https://arxiv.org/html/2510.19130v1#bib.bibx32)].
However, the challenge is substantial, as cryptocurrencies generally lack traditional fundamental metrics available in conventional financial markets.

Declaration of generative AI and AI-assisted technologies in the manuscript preparation process.
  
  
During the preparation of this work, the author used ChatGPT to assist with readability improvements and proofreading. After using this tool/service, the author reviewed and edited the content as needed and takes full responsibility for the content of the published article.

## References

* [1]
  Madan Lal Mehta
  “Random matrices”
  Elsevier, 2004
* [2]
  Oriol Bohigas, Marie-Joya Giannoni and Charles Schmit
  “Characterization of chaotic quantum spectra and universality of level fluctuation laws”
  In *Physical review letters* 52.1
  APS, 1984, pp. 1
* [3]
  Carlo WJ Beenakker
  “Random-matrix theory of quantum transport”
  In *Reviews of modern physics* 69.3
  APS, 1997, pp. 731
* [4]
  Laurent Laloux, Pierre Cizeau, Jean-Philippe Bouchaud and Marc Potters
  “Noise dressing of financial correlation matrices”
  In *Physical review letters* 83.7
  APS, 1999, pp. 1467
* [5]
  Olivier Ledoit and Sandrine Péché
  “Eigenvectors of some large sample covariance matrix ensembles”
  In *Probability Theory and Related Fields* 151.1
  Springer, 2011, pp. 233–264
* [6]
  Joël Bun, Jean-Philippe Bouchaud and Marc Potters
  “Cleaning large correlation matrices: tools from random matrix theory”
  In *Physics Reports* 666
  Elsevier, 2017, pp. 1–109
* [7]
  Olivier Ledoit and Michael Wolf
  “Analytical nonlinear shrinkage of large-dimensional covariance matrices”
  In *The Annals of Statistics* 48.5
  Institute of Mathematical Statistics, 2020, pp. 3043–3065
* [8]
  Marc Potters, Jean-Philippe Bouchaud and Laurent Laloux
  “Financial applications of random matrix theory: Old laces and new pieces”
  In *arXiv preprint physics/0507111*, 2005
* [9]
  Liusha Yang, Romain Couillet and Matthew R McKay
  “A robust statistics approach to minimum variance portfolio optimization”
  In *IEEE Transactions on Signal Processing* 63.24
  IEEE, 2015, pp. 6684–6697
* [10]
  Zdzislaw Burda and Andrzej Jarosz
  “Cleaning large-dimensional covariance matrices for correlated samples”
  In *Physical Review E* 105.3
  APS, 2022, pp. 034136
* [11]
  Olivier Ledoit and Michael Wolf
  “A well-conditioned estimator for large-dimensional covariance matrices”
  In *Journal of multivariate analysis* 88.2
  Elsevier, 2004, pp. 365–411
* [12]
  Olivier Ledoit and Michael Wolf
  “The power of (non-) linear shrinking: A review and guide to covariance matrix estimation”
  In *Journal of Financial Econometrics* 20.1
  Oxford University Press, 2022, pp. 187–218
* [13]
  David L Donoho, Matan Gavish and Iain M Johnstone
  “Optimal shrinkage of eigenvalues in the spiked covariance model”
  In *Annals of statistics* 46.4
  NIH Public Access, 2018, pp. 1742
* [14]
  Kaiming He, Xiangyu Zhang, Shaoqing Ren and Jian Sun
  “Deep residual learning for image recognition”
  In *Proceedings of the IEEE conference on computer vision and pattern recognition*, 2016, pp. 770–778
* [15]
  Fengxiang He, Tongliang Liu and Dacheng Tao
  “Why resnet works? residuals generalize”
  In *IEEE transactions on neural networks and learning systems* 31.12
  IEEE, 2020, pp. 5349–5362
* [16]
  Andrés García-Medina, Salvatore Miccichè and Rosario N Mantegna
  “Two-step estimators of high-dimensional correlation matrices”
  In *Physical Review E* 108.4
  APS, 2023, pp. 044137
* [17]
  Andrés García-Medina
  “High-dimensional covariance matrix estimators on simulated portfolios with complex structures”
  In *Physical Review E* 111.2
  APS, 2025, pp. 024316
* [18]
  Marcin Wątorek et al.
  “Multiscale characteristics of the emerging global cryptocurrency market”
  In *Physics Reports* 901
  Elsevier, 2021, pp. 1–82
  DOI: [10.1016/j.physrep.2020.10.005](https://dx.doi.org/10.1016/j.physrep.2020.10.005)
* [19]
  Spyros Makridakis, Evangelos Spiliotis and Maria Michailidis
  “Avoiding overconfidence: Evidence from the M6 financial competition”
  In *International Journal of Forecasting*
  Elsevier, 2024
* [20]
  Christian Bongiorno, Efstratios Manolakis and Rosario Nunzio Mantegna
  “End-to-End Large Portfolio Optimization for Variance Minimization with Neural Networks through Covariance Cleaning” Submitted 2 Jul 2025
  In *arXiv preprint arXiv:2507.01918*, 2025
  eprint: 2507.01918
* [21]
  Giulio Mattera and Raffaele Mattera
  “Shrinkage estimation with reinforcement learning of large variance matrices for portfolio selection”
  In *Intelligent Systems with Applications* 17
  Elsevier, 2023, pp. 200181
* [22]
  Harry Markowitz
  “Portfolio selection”
  In *The journal of finance* 7.1
  Wiley, 1952, pp. 77–91
* [23]
  Thierry Roncalli
  “Introduction to risk parity and budgeting”
  CRC Press, 2013
* [24]
  Stephen Boyd and Lieven Vandenberghe
  “Convex optimization”
  Cambridge university press, 2004
* [25]
  Richard Arnold Johnson and Dean W Wichern
  “Applied multivariate statistical analysis”
  Pearson Prentice Hall, 2002
* [26]
  Marc Potters and Jean-Philippe Bouchaud
  “A First Course in Random Matrix Theory: For Physicists, Engineers and Data Scientists”
  Cambridge University Press, 2020
* [27]
  Jason Brownlee
  “Deep learning for time series forecasting: predict the future with MLPs, CNNs and LSTMs in Python”
  Machine Learning Mastery, 2018
* [28]
  Michael A Nielsen
  “Neural networks and deep learning”
  Determination press San Francisco, CA, USA, 2015
* [29]
  Michele Tumminello, Fabrizio Lillo and Rosario N Mantegna
  “Kullback-Leibler distance as a measure of the information filtered from multivariate data”
  In *Physical Review E* 76.3
  APS, 2007, pp. 031123
* [30]
  Nathan D Cahill and Darren A Narayan
  “Fibonacci and Lucas numbers as tridiagonal matrix determinants”
  In *The Fibonacci Quarterly* 42.3
  Taylor & Francis, 2004, pp. 216–221
* [31]
  Jonathan E Atkins, Erik G Boman and Bruce Hendrickson
  “A spectral algorithm for seriation and the consecutive ones problem”
  In *SIAM Journal on Computing* 28.1
  SIAM, 1998, pp. 297–310
* [32]
  Benjamin Graham and Jason Zweig
  “The intelligent investor”
  HarperBusiness Essentials New York, 2003