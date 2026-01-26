---
authors:
- Alessio Brini
- Ekaterina Seregina
doc_id: arxiv:2601.16274v1
family_id: arxiv:2601.16274
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency
  Data
url_abs: http://arxiv.org/abs/2601.16274v1
url_html: https://arxiv.org/html/2601.16274v1
venue: arXiv q-fin
version: 1
year: 2026
---


Alessio Brinia
Ekaterina Sereginab


alessio.brini@duke.edu
eseregin@colby.edu

###### Abstract

We propose Mixed-Panels-Transformer Encoder (MPTE), a novel framework for estimating factor models in panel datasets with mixed frequencies and nonlinear signals. Traditional factor models rely on linear signal extraction and require homogeneous sampling frequencies, limiting their applicability to modern high-dimensional datasets where variables are observed at different temporal resolutions. Our approach leverages Transformer-style attention mechanisms to enable context-aware signal construction through flexible, data-dependent weighting schemes that replace fixed linear combinations with adaptive reweighting based on similarity and relevance. We extend classical principal component analysis (PCA) to accommodate general temporal and cross-sectional attention matrices, allowing the model to learn how to aggregate information across frequencies without manual alignment or pre-specified weights. For linear activation functions, we establish consistency and asymptotic normality of factor and loading estimators, showing that our framework nests Target PCA as a special case while providing efficiency gains through transfer learning across auxiliary datasets. The nonlinear extension uses a Transformer architecture to capture complex hierarchical interactions while preserving the theoretical foundations. In simulations, MPTE demonstrates superior performance in nonlinear environments, and in an empirical application to 13 macroeconomic forecasting targets using a selected set of 48 monthly and quarterly series from the FRED-MD and FRED-QD databases, our method achieves competitive performance against established benchmarks. We further analyze attention patterns and systematically ablate model components to assess variable importance and temporal dependence. The resulting patterns highlight which indicators and horizons are most influential for forecasting.

aDuke University Pratt School of Engineering, 305 Teer Engineering Building, Box 90271, Durham, NC 27708, USA

bDepartment of Economics, Colby College, 5205 Mayflower Hill Dr, Waterville, ME 04901, USA

Keywords: Mixed-frequency, Factor models, Transformers, Attention,
  
        Macroeconomic forecasting, Nonlinearity

## 1 Introduction

Panel datasets with large cross-sectional and temporal dimensions are common in macroeconomics, finance, and other social sciences. Such datasets are often well characterized by an approximate factor structure, in which a few latent factors capture most of the comovement across units. Traditionally, these latent factors are estimated directly from the panel of primary interest, referred to as the target data. However, in modern empirical settings, there are often additional or auxiliary panels that share relevant information or common factors with the target panel. Integrating information across such panels can improve the quality of factor estimation for the target data and improve downstream tasks such as forecasting. Moreover, auxiliary panels can help identify factors that influence only a limited subset of units or that are otherwise undetectable due to sparsity or missing data in the target sample. This idea of leveraging auxiliary datasets to enhance inference for a specific target dataset is closely related to the concept of transfer learning, which has proven effective in modern machine learning (Weiss et al. ([2016](https://arxiv.org/html/2601.16274v1#bib.bib50 "A survey of transfer learning"))).

Sharing relevant information across target and auxiliary datasets also arises in a wide range of applied settings. A prominent example is mixed-frequency data, which we examine empirically in this paper. High-frequency information can be exploited to improve inference for lower-frequency target variables (Forni and Lippi ([2001](https://arxiv.org/html/2601.16274v1#bib.bib51 "The generalized dynamic factor model: representation theory")), Ghysels et al. ([2007](https://arxiv.org/html/2601.16274v1#bib.bib39 "MIDAS regressions: further results and new directions"))). Related information-sharing structures arise naturally in firm-level and macro-financial panels, where cross-sectional and aggregate data jointly inform economic dynamics (Stock and Watson ([2002](https://arxiv.org/html/2601.16274v1#bib.bib52 "Forecasting using principal components from a large number of predictors")), Kelly et al. ([2019](https://arxiv.org/html/2601.16274v1#bib.bib53 "Characteristics are covariances: a unified model of risk and return"))). Similar challenges arise in energy and climate applications, which involve large, heterogeneous panels observed at different temporal and spatial resolutions (Grassi et al. ([2017](https://arxiv.org/html/2601.16274v1#bib.bib54 "The key role of forests in meeting climate targets requires science for credible mitigation"))).
To illustrate, many macroeconomic variables, such as Gross Domestic Product (GDP), are observed only at quarterly or lower frequencies, whereas others are available at higher frequencies. When some of the factors driving higher-frequency indicators are correlated with macroeconomic dynamics, information from the high-frequency data can be exploited to infer higher-frequency factors and forecast future values of the target series in the target panel.

However, classical factor models and principal component analysis (PCA) techniques are typically designed under the assumptions of homogeneous sampling frequencies and linear signal extraction. Such assumptions limit their applicability to mixed-frequency settings, where data are observed at uneven temporal resolutions across variables. In practice, high-frequency information is often collapsed into coarse aggregates, such as monthly or quarterly averages, prior to estimating the factor model. While convenient, this aggregation procedure inevitably discards valuable cross-sectional and temporal heterogeneity in the original high-frequency data. As a result, the estimated factors may fail to capture short-term dynamics, asynchronous adjustments, or heterogeneous responses across units, leading to biased or inefficient inference in mixed-frequency settings.

In this paper, we propose the Mixed-Panels-Transformer Encoder (MPTE), which overcomes the aforementioned limitations of classical factor models. We summarize our contributions as follows. First, we use attention mechanisms to enable context-aware signal construction through flexible, input-dependent weighting schemes. Second, we embed these attention mechanisms within a Transformer Encoder architecture, allowing the model to capture nonlinear signals through stacked attention and feedforward layers111By “feedforward layer”, we refer to the position-wise fully connected subnetwork commonly used in Transformer models, also known as a multilayer perceptron (MLP).
Third, for the case of linear activation functions, we develop an inferential theory and establish consistency, efficiency, and asymptotic normality for factor and loading estimators based on attended inputs.

A growing body of econometric and machine-learning literature applies selective weighting across the cross-section that is conceptually analogous to modern attention mechanisms. In classical factor models, Projected PCA (Fan et al., [2016](https://arxiv.org/html/2601.16274v1#bib.bib28 "Projected principal component analysis in factor models")) introduces a kernel matrix that reweighs units according to observable characteristics, effectively implementing a similarity-based cross-sectional smoothing that is conceptually analogous to attention mechanisms. Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")) propose Target PCA, an extension of standard PCA that jointly estimates signals for target and auxiliary panels. This framework provides direct motivation for our approach. They apply PCA to the weighted average of the second-moment matrices of the two panels, where the optimal weighting coefficient is a scalar chosen to ensure consistent and efficient estimation of the target factors. Connor et al. ([2012](https://arxiv.org/html/2601.16274v1#bib.bib37 "Efficient semiparametric estimation of the fama–french model and extensions")) rely on kernel weight matrices that assign higher weights to units sharing similar covariates, a mechanism conceptually related to attention scores. Related approaches include weighted and sparse PCA methods (Zou et al., [2006](https://arxiv.org/html/2601.16274v1#bib.bib38 "Sparse principal component analysis")), which modify the eigen-decomposition by imposing sparsity and correspond to hard cross-sectional attention. Gu et al. ([2021](https://arxiv.org/html/2601.16274v1#bib.bib1 "Autoencoder asset pricing models")) propose an autoencoder-based stochastic discount factor estimator that learns feature-specific scaling functions, which serve as data-dependent attention weights across assets.

In mixed-frequency and Mixed-Data Sampling (MIDAS) regressions (Ghysels et al. ([2007](https://arxiv.org/html/2601.16274v1#bib.bib39 "MIDAS regressions: further results and new directions")), Foroni et al. ([2015](https://arxiv.org/html/2601.16274v1#bib.bib40 "Unrestricted mixed data sampling (midas): midas regressions with unrestricted lag polynomials"))) high-frequency observations enter through parametrized lag weights that selectively emphasize the most informative time periods, closely resembling temporal attention scores. Distributed lag and kernel-smoothing estimators (Nadaraya, [1964](https://arxiv.org/html/2601.16274v1#bib.bib33 "On estimating regression"); Fan et al., [1996](https://arxiv.org/html/2601.16274v1#bib.bib41 "A study of variable bandwidth selection for local polynomial regression")) apply localized temporal weights, effectively focusing estimation on nearby or relevant points, in a manner conceptually analogous to attention over sequences. Stock and Watson ([2016](https://arxiv.org/html/2601.16274v1#bib.bib42 "Dynamic factor models, factor-augmented vector autoregressions, and structural vector autoregressions in macroeconomics")) provide an extensive review of the literature on dynamic factor models, in which information is reweighted over time through stochastic volatility, state-dependent dynamics, or regime switching, which can be interpreted as adaptive temporal attention.

There are also a limited number of papers that weigh both the cross-sectional and time dimensions. Wang et al. ([2019](https://arxiv.org/html/2601.16274v1#bib.bib43 "Factor models for matrix-valued high-dimensional time series")) apply kernel-weighting to cross-sectional and time dimensions.Bai and Wang ([2015](https://arxiv.org/html/2601.16274v1#bib.bib44 "Identification and bayesian estimation of dynamic factor models")) use time-varying loadings and cross-sectional smoothing. Chen et al. ([2022](https://arxiv.org/html/2601.16274v1#bib.bib45 "Factor models for high-dimensional tensor time series")) employ separate weights along each mode in tensor factor models, which is conceptually analogous to multi-head attention across dimensions.

More broadly, recent work interprets Transformer attention as a normalized kernel smoother (Tsai et al., [2019](https://arxiv.org/html/2601.16274v1#bib.bib46 "Transformer dissection: an unified understanding for transformer’s attention via the lens of kernel"); Katharopoulos et al., [2020](https://arxiv.org/html/2601.16274v1#bib.bib47 "Transformers are rnns: fast autoregressive transformers with linear attention")), strengthening the conceptual link between attention mechanisms and econometric approaches that selectively weigh cross-sectional information.

Building on these selective weighting ideas, we propose a factor framework with general cross-sectional and temporal attention matrices that explicitly accommodates rich heterogeneity in both the target and auxiliary panels. In many empirical settings, auxiliary data are informative for the target task only selectively, for example, when only subsets of units, periods, or factor directions in an auxiliary panel carry signals about the target outcomes, while others contribute primarily noise. Such heterogeneity may arise from differences in economic relevance across units, time-varying predictive content, partial alignment between auxiliary and target factor spaces, or structured heteroskedasticity in idiosyncratic errors. Standard block-based approaches, including Target PCA by Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")), implicitly treat units and periods symmetrically within each block and therefore cannot exploit these forms of selective informativeness without prior dimension reduction or ad hoc preprocessing. By contrast, our attention-based formulation allows the data to determine which cross-sectional units and time periods are most informative for the target task, yielding an effective sample size that reflects relevance rather than raw dimension. This flexibility enables first-order efficiency gains from auxiliary information in genuine transfer-learning regimes, while still preserving a clear notion of target-specific factors identified by the target block. As a result, our framework strictly generalizes existing target-focused PCA methods and is particularly well suited for applications with heterogeneous relevance, structured noise, and partial factor overlap across datasets.

An important distinction between our framework and existing target-focused PCA methods is its adaptivity to heterogeneous relevance across units and time. Conceptually, our approach is analogous to adaptive thresholding and shrinkage procedures in high-dimensional statistics, which improve efficiency by learning which components carry signal rather than imposing fixed selection rules. While Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")) rely on block-level structure and uniform weighting to ensure robustness when the target panel may be partially observed, they cannot adjust to varying degrees of informativeness within or across blocks. By contrast, the attention matrices in our framework allow the estimator to adaptively reweight cross-sectional units and time periods based on their relevance for the target task.

Our work contributes to three different streams of literature. First, we contribute to the literature on large-dimensional factor models. Our paper provides a context-aware nonlinear generalization of Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")). We allow nonlinear signals and enable the model to learn the context by modifying the inputs through cross-sectional and temporal weighting matrices. The former allows the model to learn the context by using contemporaneous information about all series, while the latter helps the model learn temporal context by using information from all past embeddings. The machine learning literature has long acknowledged the close relationship between autoencoders and principal component analysis (PCA) (e.g., Baldi and Hornik ([1989](https://arxiv.org/html/2601.16274v1#bib.bib32 "Neural networks and principal component analysis: learning from examples without local minima"))), and by extension their connection to latent factor models in asset pricing (Gu et al., [2021](https://arxiv.org/html/2601.16274v1#bib.bib1 "Autoencoder asset pricing models")). In particular, a linear autoencoder with a hidden layer of KK neurons is a linear factor model with KK latent factors. Our paper uses this connection to build a theory for the case of linear activation functions, to allow direct comparison with the methodology of Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")), while keeping the flexibility of nonlinear signals for simulations and empirical applications.

Second, we contribute to the literature on nonparametric techniques (such as kernel regression, Nadaraya ([1964](https://arxiv.org/html/2601.16274v1#bib.bib33 "On estimating regression"))) and attention mechanisms. In traditional factor models and regression models, each input contributes to the output through fixed weights. Attention mechanisms replace these with data-dependent weights that adapt to context. The model “attends” more to informative observations and less to irrelevant ones. In this context, attention acts as a learned smoothing kernel that reweighs observations based on similarity. In contrast to a traditional kernel, it is fully data-driven and is less affected by the curse of dimensionality. In fact, this interpretation extends beyond factor models. Recent work has established connections between classical regression methods, such as ordinary least squares (OLS), and attention mechanisms. Coulombe ([2025](https://arxiv.org/html/2601.16274v1#bib.bib34 "Ordinary least squares as an attention mechanism")) show that OLS can be reinterpreted as a special case of an attention mechanism. Specifically, when OLS is viewed as selecting similarities in a transformed regressor space, rather than as purely estimating coefficients via partial correlations, the resulting solution is analogous to a query–key–value structure in attention. In this paper, we establish a connection between traditional factor models estimated using PCA and attention mechanisms. To the best of our knowledge, this is the first work to study the theoretical properties of PCA under “attended” inputs.

Finally, we contribute to the literature on mixed-frequency data. Our paper can be interpreted as a nonlinear and context-aware generalization of MIDAS methods. When the predictors, XtX\_{t}, and targets, YtY\_{t}, are sampled at different frequencies, traditional approaches typically require manual alignment, while MIDAS specifies a parametric weighting structure over the high-frequency lags. Our framework embeds both XtX\_{t} and YtY\_{t} in a unified sequence for the Transformer encoder architecture. The model learns how to aggregate information across frequencies via attention, without resampling or pre-specified weight schemes. A small number of applied papers augment the MIDAS framework with nonlinearities. Lin and Michailidis ([2024](https://arxiv.org/html/2601.16274v1#bib.bib4 "A multi-task encoder-dual-decoder framework for mixed frequency data prediction")) propose a neural network approach that handles mixed-frequency data through a shared encoder and dual decoders; Dai et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib14 "FreqFormer: frequency-aware transformer for lightweight image super-resolution")) introduce FreqFormer, a frequency-aware Transformer developed for image super-resolution; Ji et al. ([2025](https://arxiv.org/html/2601.16274v1#bib.bib15 "A novel probabilistic carbon price prediction model: integrating the transformer framework with mixed-frequency modeling at different quartiles")) develop QRTransformer–MIDAS, which integrates quantile regression into a Transformer with MIDAS-based high-frequency preprocessing. In contrast, our approach adopts an encoder-only Transformer architecture, is designed explicitly for mixed-frequency time-series panels, and learns cross-frequency aggregation directly through attention, without relying on MIDAS-style preprocessing or decoder-based generative structures.

Our framework builds on recent advances in Transformer-based models and offers a novel approach to estimating factor models with mixed-frequency data. We shift the focus from averaging information, as commonly done in classical factor models, to attending to information. We also provide an extensive ablation study that examines the role of each component of MPTE in both simulations and empirical applications. Specifically, we study the role of attention mechanisms, nonlinearities, the use of high-frequency data for forecasting low-frequency targets, and additional architectural components such as temporal encoding.

To the best of our knowledge, this is the first paper to disentangle and interpret the cross-sectional and temporal aggregation patterns learned by a transformer in macroeconomic forecasting, and to link them to economically interpretable sources of predictive power. By averaging attention weights across variables and across time, we recover target-specific measures of variable importance and lag relevance that vary systematically with model architecture and forecast target. We show that nonlinear transformations and explicit temporal encoding allow the model to place disciplined weight on state-dependent indicators and medium- to long-horizon dynamics, while simpler specifications rely predominantly on short-run fluctuations and diffuse cross-sectional signals. These results suggest that attention-based models can do more than improve forecast accuracy: they provide a transparent, data-driven framework for assessing which economic variables and horizons are most relevant for forecasting particular macroeconomic outcomes, with direct implications for policy monitoring and analysis.

The rest of the paper is structured as follows. Section [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") introduces the MPTE framework and formalizes the attention-based aggregation of cross-sectional and temporal information. Section [3](https://arxiv.org/html/2601.16274v1#S3 "3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") develops the inferential theory for the linear version of the model and establishes consistency and asymptotic properties of the resulting estimators. Section [4](https://arxiv.org/html/2601.16274v1#S4 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") extends the framework to nonlinear signal structures.
Section [5](https://arxiv.org/html/2601.16274v1#S5 "5 Implementation of MPTE with nonlinear signals and mixed frequencies ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") describes the Transformer encoder implementation of MPTE and discusses practical considerations for handling nonlinearities and mixed frequencies. Section [6](https://arxiv.org/html/2601.16274v1#S6 "6 Simulation evidence on attention-based mixed-frequency estimation ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") presents simulation evidence assessing the performance of attention-based mixed-frequency estimation under linear and nonlinear signal structures. Section [7](https://arxiv.org/html/2601.16274v1#S7 "7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") provides an empirical application to U.S. macroeconomic data. Section [8](https://arxiv.org/html/2601.16274v1#S8 "8 Conclusions and Discussion ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") concludes.

## 2 Methodology

This section presents MPTE and its associated estimator, which integrates target and auxiliary datasets through cross-sectional and temporal attention operators. We discuss the connection to Target PCA and show in Section [4](https://arxiv.org/html/2601.16274v1#S4 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") that Target PCA arises as a special case of a Transformer encoder.

### 2.1 Model setup

The target panel dataset Y has TyT\_{y} time periods and NyN\_{y} cross-sectional units. Y∈ℝTy×NyY\in\mathbb{R}^{T\_{y}\times N\_{y}} has the following signal-plus-noise structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt​j=(Ψy)t​j⏟signal+(ey)t​j⏟noise,t=1,…,Ty,j=1,…,Ny,Y\_{tj}=\underbrace{(\Psi\_{y})\_{tj}}\_{\text{signal}}+\underbrace{(e\_{y})\_{tj}}\_{\text{noise}},\quad t=1,\ldots,T\_{y},\ j=1,\ldots,N\_{y}, |  | (2.1) |

where Yt​jY\_{tj} denotes the data for the jj-th cross-sectional unit at time tt, (Ψy)t​j(\Psi\_{y})\_{tj} and (ey)t​j(e\_{y})\_{tj} are the common and idiosyncratic components of Yt​jY\_{tj}, respectively. Equation ([2.1](https://arxiv.org/html/2601.16274v1#S2.E1 "Equation 2.1 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) can be written in a matrix notation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y⏟Ty×Ny=Ψy+ey.\underbrace{Y}\_{T\_{y}\times N\_{y}}=\Psi\_{y}+e\_{y}. |  | (2.2) |

In addition, an auxiliary panel dataset X is available that has TxT\_{x} time periods and NxN\_{x} cross-sectional units. X∈ℝTx×NxX\in\mathbb{R}^{T\_{x}\times N\_{x}} has the following signal-plus-noise structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt​i=(Ψx)t​i⏟signal+(ex)t​i⏟noise,t=1,…,Tx,i=1,…,Nx,X\_{ti}=\underbrace{(\Psi\_{x})\_{ti}}\_{\text{signal}}+\underbrace{(e\_{x})\_{ti}}\_{\text{noise}},\quad t=1,\ldots,T\_{x},\ i=1,\ldots,N\_{x}, |  | (2.3) |

where Xt​iX\_{ti} denotes the data for the ii-th cross-sectional unit at time tt, (Ψx)t​i(\Psi\_{x})\_{ti} and (ex)t​i(e\_{x})\_{ti} are the common and idiosyncratic components of Xt​iX\_{ti}, respectively. Equation ([2.3](https://arxiv.org/html/2601.16274v1#S2.E3 "Equation 2.3 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) can be written in a matrix notation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | X⏟Tx×Nx=Ψx+ex.\underbrace{X}\_{T\_{x}\times N\_{x}}=\Psi\_{x}+e\_{x}. |  | (2.4) |

Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")) use a linear factor model for signal components of YY and XX, with the number of latent factors denoted kyk\_{y} and kxk\_{x}, respectively. Specifically, they assume Ψy=Fy​(ΛyY)⊤\Psi\_{y}=F\_{y}(\Lambda\_{y}^{Y})^{\top} and Ψx=Fx​(ΛxX)⊤\Psi\_{x}=F\_{x}(\Lambda\_{x}^{X})^{\top}, where FyF\_{y} and FxF\_{x} are Ty×kyT\_{y}\times k\_{y} and Tx×kxT\_{x}\times k\_{x} matrices of latent factors, and ΛyY\Lambda\_{y}^{Y} and ΛxX\Lambda\_{x}^{X} are Ny×kyN\_{y}\times k\_{y} and Nx×kxN\_{x}\times k\_{x} matrices of factor loadings. Under linear signal structures and assuming Tx=Ty=TT\_{x}=T\_{y}=T, equations ([2.2](https://arxiv.org/html/2601.16274v1#S2.E2 "Equation 2.2 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) and ([2.4](https://arxiv.org/html/2601.16274v1#S2.E4 "Equation 2.4 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) become:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | Y=Fy⏟T×ky​(ΛyY)⊤⏟ky×Ny+ey\displaystyle Y=\underbrace{F\_{y}}\_{T\times k\_{y}}\underbrace{(\Lambda\_{y}^{Y})^{\top}}\_{k\_{y}\times N\_{y}}+e\_{y} |  | (2.5) |
|  |  | X=Fx⏟T×kx​(ΛxX)⊤⏟kx×Nx+ex\displaystyle X=\underbrace{F\_{x}}\_{T\times k\_{x}}\underbrace{(\Lambda\_{x}^{X})^{\top}}\_{k\_{x}\times N\_{x}}+e\_{x} |  |

They use the union of the factors in YY and XX, concatenated in a matrix F≡[Fx,Fy]F\equiv[F\_{x},F\_{y}], and apply PCA to the weighted average of the second moment matrices of both panels by solving the following optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minF,Λx,Λy⁡∑i=1Nx∑t=1Tx(Xt​i−(Ft)T​(Λx)i)2⏟auxiliary error+γ⋅∑j=1Ny∑t=1Ty(Yt​j−(Ft)T​(Λy)j)2⏟target error,\min\_{F,\Lambda\_{x},\Lambda\_{y}}\underbrace{\sum\_{i=1}^{N\_{x}}\sum\_{t=1}^{T\_{x}}\Big(X\_{ti}-(F\_{t})^{T}(\Lambda\_{x})\_{i}\Big)^{2}}\_{\text{auxiliary error}}+\gamma\cdot\underbrace{\sum\_{j=1}^{N\_{y}}\sum\_{t=1}^{T\_{y}}\Big(Y\_{tj}-(F\_{t})^{T}(\Lambda\_{y})\_{j}\Big)^{2}}\_{\text{target error}}, |  | (2.6) |

where Λy\Lambda\_{y} and Λx\Lambda\_{x} are Ny×kN\_{y}\times k and Nx×kN\_{x}\times k matrices of factor loadings.
The weighting parameter γ\gamma is selected to ensure consistent and efficient estimation of target factors. Let Zγ≡[Xγ​Y]Z^{\gamma}\equiv[X\quad\sqrt{\gamma}Y], then ([2.6](https://arxiv.org/html/2601.16274v1#S2.E6 "Equation 2.6 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) can be viewed as applying PCA to (Zγ)⊤​Zγ(Z^{\gamma})^{\top}Z^{\gamma}.

We augment the framework in ([2.2](https://arxiv.org/html/2601.16274v1#S2.E2 "Equation 2.2 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")), ([2.4](https://arxiv.org/html/2601.16274v1#S2.E4 "Equation 2.4 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")), and ([2.6](https://arxiv.org/html/2601.16274v1#S2.E6 "Equation 2.6 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) in three respects: (i) we use cross-sectional and temporal attention mechanisms to enable context-aware signal construction; (ii) we allow nonlinear signals Ψy\Psi\_{y} and Ψx\Psi\_{x}; (iii) we relax the assumption Tx=Ty=TT\_{x}=T\_{y}=T required in Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")).

### 2.2 Attention mechanism and context-aware signal construction

At the core of the Transformer architecture is the attention mechanism that was originally developed as a complement to recurrent neural networks (RNNs) for machine translation (Bahdanau et al., [2014](https://arxiv.org/html/2601.16274v1#bib.bib24 "Neural machine translation by jointly learning to align and translate")). However, it was later shown to be effective as a standalone architecture even without the recurrent structure (Vaswani et al., [2017](https://arxiv.org/html/2601.16274v1#bib.bib23 "Attention is all you need")).

Let Z≡[XY]Z\equiv[X\quad Y]. The goal of attention is to map inputs ZZ to a new set of inputs Z~\widetilde{Z} in a new embedding222An embedding refers to a learned vector representation of the data in which relevant structure is preserved for comparison, aggregation, or prediction. In attention-based models, embeddings provide the space in which similarity and relevance across observations are computed, without imposing a probabilistic or structural interpretation.
space that captures a richer structure. Enhancing the inputs helps extract better signals for target and auxiliary datasets in ([2.2](https://arxiv.org/html/2601.16274v1#S2.E2 "Equation 2.2 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) and ([2.4](https://arxiv.org/html/2601.16274v1#S2.E4 "Equation 2.4 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")). For now, let Tx=Ty=TT\_{x}=T\_{y}=T. We show in Section [5](https://arxiv.org/html/2601.16274v1#S5 "5 Implementation of MPTE with nonlinear signals and mixed frequencies ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") that this assumption is not necessary for implementing our approach; however, since Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")) impose this restriction to solve ([2.6](https://arxiv.org/html/2601.16274v1#S2.E6 "Equation 2.6 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")), we maintain it here to draw parallels with their method. Consider the simplest form of attention:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~=A​Z,\widetilde{Z}=AZ, |  | (2.7) |

where A∈ℝT×TA\in\mathbb{R}^{T\times T}. When A=ITA=I\_{T}, where ITI\_{T} is a T×TT\times T identity matrix, this corresponds to the case without attention. When A=Z​Z⊤A=ZZ^{\top}, the resulting weights correspond to an unnormalized similarity matrix based on inner products, measuring pairwise similarity between observations.

Attention acts as a learned, data-driven smoothing kernel that reweighs information based on similarity. In contrast to traditional models, where inputs contribute through fixed weights, attention assigns data-dependent weights that adapt to context, allowing the model to attend more to informative observations and less to irrelevant ones.

Vaswani et al. ([2017](https://arxiv.org/html/2601.16274v1#bib.bib23 "Attention is all you need")) introduce terminology from information retrieval to provide a more granular interpretation of ([2.7](https://arxiv.org/html/2601.16274v1#S2.E7 "Equation 2.7 ‣ 2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")). In particular, inputs are linearly transformed into three objects: keys, values, and queries. Keys are defined as K=Z​WkK=ZW^{k} and summarize the attributes of each unit through a linear transformation of the inputs using transformation weights WkW^{k}. Values are defined as V=Z​WvV=ZW^{v} and represent the information associated with each unit that is aggregated through attention using weights WvW^{v}. Queries are defined as Q=Z​WqQ=ZW^{q} and encode which attributes are relevant for forming the weighted combination of values using weights WqW^{q}. In the simplest case, the transformation matrices are identity matrices, so that Q=K=V=ZQ=K=V=Z.

Using this terminology, the goal of attention is to measure the degree of match between queries and keys and use it to weigh the influence of the value matrix on the updated set of inputs Z~\widetilde{Z}. We can rewrite ([2.7](https://arxiv.org/html/2601.16274v1#S2.E7 "Equation 2.7 ‣ 2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~=softmax​(Q​K⊤)​V,\widetilde{Z}=\text{softmax}(QK^{\top})V, |  | (2.8) |

where attention is computed as a row-wise normalized dot product between queries and keys, A=softmax​(Q​K⊤)A=\text{softmax}(QK^{\top}).

Our first contribution is to allow general temporal and cross-sectional attention matrices when learning signals in the target dataset. We consider the following transformation of the data matrix:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~=B​[XY]​Az,\widetilde{Z}=B\begin{bmatrix}X&Y\end{bmatrix}A\_{z}, |  | (2.9) |

where B∈ℝT×TB\in\mathbb{R}^{T\times T} is a temporal attention matrix, and Az∈ℝ(Nx+Ny)×(Nx+Ny)A\_{z}\in\mathbb{R}^{(N\_{x}+N\_{y})\times(N\_{x}+N\_{y})} is a cross-sectional attention matrix.
The approach in Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")) can be viewed as a special case with B=ITB=I\_{T} and Az=diag​(INx,γ​INy)A\_{z}=\text{diag}(I\_{N\_{x}},\gamma I\_{N\_{y}}). In contrast, we allow both BB and AzA\_{z} to be data-driven and, in the linear case, study the restrictions required to ensure consistent estimation of the signal components in ([2.2](https://arxiv.org/html/2601.16274v1#S2.E2 "Equation 2.2 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) and ([2.4](https://arxiv.org/html/2601.16274v1#S2.E4 "Equation 2.4 ‣ 2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")).

The factor model for Z~=B​[XY]​Az\widetilde{Z}=B\begin{bmatrix}X&Y\end{bmatrix}A\_{z} can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~=B​F⏟F(B)​[Λx⊤Λy⊤]​Az⏟(Λ(A))⊤+B​[exey]​Az⏟e~,\widetilde{Z}=\underbrace{BF}\_{F^{(B)}}\underbrace{[\Lambda\_{x}^{\top}\quad\Lambda\_{y}^{\top}]A\_{z}}\_{(\Lambda^{(A)})^{\top}}+\underbrace{B[e\_{x}\quad e\_{y}]A\_{z}}\_{\widetilde{e}}, |  | (2.10) |

where F(B):=B​FF^{(B)}:=BF denotes the temporally transformed latent factor process, and Ft(B)F\_{t}^{(B)} denotes its tt-th row. Define the concatenated idiosyncratic error matrix

|  |  |  |
| --- | --- | --- |
|  | e≡[exey]∈ℝT×(Nx+Ny).e\equiv\bigl[e\_{x}\ \ e\_{y}\bigr]\in\mathbb{R}^{T\times(N\_{x}+N\_{y})}. |  |

Given a cross-sectional attention matrix AzA\_{z},
define the cross-sectionally transformed idiosyncratic component by

|  |  |  |
| --- | --- | --- |
|  | e(A)≡e​Az∈ℝT×(Nx+Ny),e^{(A)}\equiv eA\_{z}\in\mathbb{R}^{T\times(N\_{x}+N\_{y})}, |  |

and let ei(A)≡(e(A)):i∈ℝTe\_{i}^{(A)}\equiv(e^{(A)})\_{:i}\in\mathbb{R}^{T} denote the ii-th transformed idiosyncratic error series.
With temporal attention B∈ℝT×TB\in\mathbb{R}^{T\times T}, the fully transformed idiosyncratic component is

|  |  |  |
| --- | --- | --- |
|  | e~≡e(A,B)≡B​e(A)=B​[exey]​Az,\widetilde{e}\equiv e^{(A,B)}\equiv Be^{(A)}=B[e\_{x}\ \ e\_{y}]A\_{z}, |  |

so that (B​ei(A))t=e~t​i(Be\_{i}^{(A)})\_{t}=\widetilde{e}\_{ti}. Let et:=(ex,t⊤,ey,t⊤)⊤∈ℝNx+Nye\_{t}:=(e\_{x,t}^{\top},\,e\_{y,t}^{\top})^{\top}\in\mathbb{R}^{N\_{x}+N\_{y}} denote the stacked idiosyncratic vector at time tt,
where ex,t⊤e\_{x,t}^{\top} and ey,t⊤e\_{y,t}^{\top} are the ttth rows of exe\_{x} and eye\_{y}, respectively.

If AzA\_{z} is block diagonal,

|  |  |  |
| --- | --- | --- |
|  | Az=[A100A2],A\_{z}=\begin{bmatrix}A\_{1}&0\\ 0&A\_{2}\end{bmatrix}, |  |

we get the framework of Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")) if we set A1=[INx0]A\_{1}=\begin{bmatrix}I\_{N\_{x}}\\
0\end{bmatrix} and A2=[0γ​INy]A\_{2}=\begin{bmatrix}0\\
\gamma I\_{N\_{y}}\end{bmatrix}. Then Z~\widetilde{Z} can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~=B​F⏟F(B)​[Λx⊤​A1Λy⊤​A2]⏟(Λ(A))⊤+B​[ex​A1ey​A2]⏟e(A,B)=F(B)​Λ(A)⊤+e(A,B).\widetilde{Z}=\underbrace{BF}\_{F^{(B)}}\underbrace{[\Lambda\_{x}^{\top}A\_{1}\quad\Lambda\_{y}^{\top}A\_{2}]}\_{(\Lambda^{(A)})^{\top}}+\underbrace{B[e\_{x}A\_{1}\quad e\_{y}A\_{2}]}\_{e^{(A,B)}}=F^{(B)}\Lambda^{(A)\top}+e^{(A,B)}. |  | (2.11) |

We propose to apply PCA to the second moment matrix of the “attended” inputs Z~\widetilde{Z} in ([2.10](https://arxiv.org/html/2601.16274v1#S2.E10 "Equation 2.10 ‣ 2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")). The PCA objective function is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minB​F,Λx,Λy⁡trace​(Az⊤​[X⊤Y⊤]​B⊤−Az⊤​[ΛxΛy]​F⊤​B)​(B​[XY]​Az−B​F​[Λx⊤Λy⊤]​Az).\min\_{BF,\Lambda\_{x},\Lambda\_{y}}\text{trace}\Bigg(A\_{z}^{\top}\begin{bmatrix}X^{\top}\\ Y^{\top}\end{bmatrix}B^{\top}-A\_{z}^{\top}\begin{bmatrix}\Lambda\_{x}\\ \Lambda\_{y}\end{bmatrix}F^{\top}B\Bigg)\Big(B\begin{bmatrix}X&Y\end{bmatrix}A\_{z}-BF\begin{bmatrix}\Lambda\_{x}^{\top}&\Lambda\_{y}^{\top}\end{bmatrix}A\_{z}\Big). |  | (2.12) |

We call the aforementioned framework used to estimate the signals using ([2.12](https://arxiv.org/html/2601.16274v1#S2.E12 "Equation 2.12 ‣ 2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) MPTE. The encoding is achieved through PCA estimation of the signal under linear activations. The extension to nonlinear activations through Transformer architecture as well as theoretical equivalence between an autoencoder with kk hidden layers and a linear factor model with kk latent factors is studied in Section [4](https://arxiv.org/html/2601.16274v1#S4 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").

Equation ([2.12](https://arxiv.org/html/2601.16274v1#S2.E12 "Equation 2.12 ‣ 2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | minF(B),Λ(A)⁡‖Z~−F(B)​Λ(A)⊤‖F2.\min\_{F^{(B)},\Lambda^{(A)}}\left\lVert\widetilde{Z}-F^{(B)}\Lambda^{(A)\top}\right\rVert^{2}\_{F}. |  | (2.13) |

With the identifying assumption Λ(A)⊤​Λ(A)/(Nx+Ny)=Ik\Lambda^{(A)\top}\Lambda^{(A)}/(N\_{x}+N\_{y})=I\_{k}, we can concentrate out F(B)F^{(B)} and obtain the following objective function:

|  |  |  |
| --- | --- | --- |
|  | maxΛ(A)⁡trace​(Λ(A)⊤​(Z~⊤​Z~)​Λ(A)).\max\_{\Lambda^{(A)}}\text{trace}\Big(\Lambda^{(A)\top}(\widetilde{Z}^{\top}\widetilde{Z})\Lambda^{(A)}\Big). |  |

We assume BB preserves the factor space such that the spectrum of k×kk\times k matrix T−1​F⊤​B⊤​B​FT^{-1}F^{\top}B^{\top}BF is bounded away from zero and infinity. That is, there exist constants 0<c<C<∞0<c<C<\infty such that c≤λmin​(T−1​F⊤​B⊤​B​F)≤λmax​(T−1​F⊤​B⊤​B​F)≤Cc\leq\lambda\_{\text{min}}(T^{-1}F^{\top}B^{\top}BF)\leq\lambda\_{\text{max}}(T^{-1}F^{\top}B^{\top}BF)\leq C. This ensures the temporally attended signal B​FBF spans the same kk-dimensional space as FF up to well-conditioned scaling. We can estimate Λ(A)\Lambda^{(A)} by applying PCA to Z~⊤​Z~\widetilde{Z}^{\top}\widetilde{Z}. Factors F(B)F^{(B)} are obtained by regressing Z~\widetilde{Z} on the estimated loadings Λ^(A)\widehat{\Lambda}^{(A)}.

We design the above methodology to exploit auxiliary information without compromising the structure of the target block. Conceptually, the target variables determine the latent directions that are relevant for the object of interest, while auxiliary variables, when appropriately weighted, can improve the precision with which these latent components are estimated. This separation allows the model to borrow strength across heterogeneous panels without allowing auxiliary information to redefine the target structure. Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")) and our approach address related but distinct problems. Target PCA is developed to recover target factors and fill in missing target observations, which naturally leads to strong homogeneity assumptions and a limited role for auxiliary variables. Our framework instead targets forecasting environments in which auxiliary variables are plentiful, heterogeneous, and potentially more informative than the target block. This difference in objectives motivates a design that accommodates cross-sectional heterogeneity and enables transfer learning, allowing auxiliary data to improve estimation precision without redefining the target factor structure. The theoretical results in the next section formalize how these design choices lead to efficiency gains relative to target-only procedures whenever auxiliary information is informative.

## 3 Inferential theory

The inferential theory in this section is derived under linear activation functions. Sections [4](https://arxiv.org/html/2601.16274v1#S4 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") and [5](https://arxiv.org/html/2601.16274v1#S5 "5 Implementation of MPTE with nonlinear signals and mixed frequencies ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") provide conceptual and implementation details for nonlinear signals. Similarly to Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")), we work under a framework of general assumptions for approximate factor models.

### 3.1 Assumptions

We lay out the first set of assumptions, which we refer to as baseline assumptions.

* A.1

  (Normalization and temporal attention regularity)
  {Ft}\{F\_{t}\} is strictly stationary with 𝔼​[Ft]=0\mathbb{E}[F\_{t}]=0 and
  𝔼​[Ft​Ft⊤]=ΣF≻0\mathbb{E}[F\_{t}F\_{t}^{\top}]=\Sigma\_{F}\succ 0. The temporal attention matrix B∈ℝT×TB\in\mathbb{R}^{T\times T}
  satisfies

  |  |  |  |
  | --- | --- | --- |
  |  | ‖B‖F2/T=𝒪​(1),\|B\|\_{F}^{2}/T=\mathcal{O}(1), |  |

  and there exist constants 0<c<C<∞0<c<C<\infty such that

  |  |  |  |
  | --- | --- | --- |
  |  | c≤λmin​(T−1​F⊤​B⊤​B​F)≤λmax​(T−1​F⊤​B⊤​B​F)≤C.c\leq\lambda\_{\min}\!\left(T^{-1}F^{\top}B^{\top}BF\right)\leq\lambda\_{\max}\!\left(T^{-1}F^{\top}B^{\top}BF\right)\leq C. |  |
* A.2

  (Temporal dependence) The sequence {(Ft,et)}\{(F\_{t},e\_{t})\} is strictly stationary and α\alpha-mixing with coefficients α​(k)\alpha(k) satisfying
  ∑k=1∞α​(k)δ/(2+δ)<∞\sum\_{k=1}^{\infty}\alpha(k)^{\delta/(2+\delta)}<\infty for some δ>0\delta>0.
* A.3

  (Moments) supt𝔼​‖Ft‖4+δ<∞\sup\_{t}\mathbb{E}\left\lVert F\_{t}\right\rVert^{4+\delta}<\infty and supt,i𝔼​|ei​t|4+δ<∞\sup\_{t,i}\mathbb{E}|e\_{it}|^{4+\delta}<\infty.
* A.4

  (Orthogonality) 𝔼​[Ft​et⊤]=0\mathbb{E}[F\_{t}e\_{t}^{\top}]=0 for all tt.
* A.5

  (Idiosyncratic control) Let Σe=𝔼​[et​et⊤]\Sigma\_{e}=\mathbb{E}[e\_{t}e\_{t}^{\top}]. Require ‖Az⊤​Σe​Az‖≤C\left\lVert A\_{z}^{\top}\Sigma\_{e}A\_{z}\right\rVert\leq C,
    
  supi∑j|(Az⊤​Σe​Az)i​j|≤C\sup\_{i}\sum\_{j}|(A\_{z}^{\top}\Sigma\_{e}A\_{z})\_{ij}|\leq C, and the uniform 8th-moment bound for the transformed idiosyncratic entries supi,t𝔼​|(B​ei(A))t|8<∞\sup\_{i,t}\mathbb{E}|(Be\_{i}^{(A)})\_{t}|^{8}<\infty. AzA\_{z} and BB are deterministic operators with at most polynomial growth so that applying them preserves mixing/moment conditions.
* A.6

  (Loadings) 1Nx+Ny​(Λ​Az)⊤​(Λ​Az)→ΣΛ(A)≻0\frac{1}{N\_{x}+N\_{y}}(\Lambda A\_{z})^{\top}(\Lambda A\_{z})\rightarrow\Sigma\_{\Lambda}^{(A)}\succ 0 and supi‖(Λ​Az)i‖<∞\sup\_{i}\left\lVert(\Lambda A\_{z})\_{i}\right\rVert<\infty.
* A.7

  (Spectral scaling) Let N=Nx+NyN=N\_{x}+N\_{y}. There exist α,β≥0\alpha,\beta\geq 0 such that tr​(Az⊤​Az)=𝒪​(Nα)\text{tr}(A\_{z}^{\top}A\_{z})=\mathcal{O}(N^{\alpha}), ‖Az⊤​Az‖F2=𝒪​(Nβ)\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}=\mathcal{O}(N^{\beta}) with α+β<1\alpha+\beta<1.

The attention matrices BB and AzA\_{z} are treated as deterministic sequences that may depend on (Nx+Ny,T)(N\_{x}+N\_{y},T)
but are independent of the underlying randomness in (Ft,et)(F\_{t},e\_{t}).
This ensures that applying (B,Az)(B,A\_{z}) preserves the mixing and moment properties in Assumptions A.2–A.3.

Assumption A.1 ensures temporal attention does not distort the latent factor space: the transformation BB has bounded energy and preserves the rank-kk span of the factors up to a well-conditioned linear transformation. Assumptions A.2–A.4 correspond to the standard dependence and orthogonality conditions in approximate factor models; since BB and AzA\_{z} are deterministic linear operators with bounded operator norms, applying them preserves the mixing and moment properties of (Ft,et)(F\_{t},e\_{t}). Assumption A.5 controls the behavior of the idiosyncratic component after cross-sectional and temporal attention, ensuring that the transformed noise does not explode in operator norm and satisfies the moment conditions needed for the CLTs. Assumption A.6 guarantees pervasiveness of the attention-weighted loadings, so that the cross-sectional law of large numbers holds after applying AzA\_{z}. Assumption A.7 imposes spectral growth bounds on the attention matrix AzA\_{z}, and ensures that the factor estimation error rate is oP​(1)o\_{P}(1).

### 3.2 Consistency

The loadings and factors can be consistently estimated if BB and AzA\_{z} are chosen properly.

###### Theorem 1 (Consistency under general cross-sectional attention).

Let

|  |  |  |
| --- | --- | --- |
|  | α¯=tr​(Az⊤​Az)​‖Az⊤​Az‖F2N⋅‖B‖F4T2.\bar{\alpha}=\frac{\mathrm{tr}(A\_{z}^{\top}A\_{z})\,\|A\_{z}^{\top}A\_{z}\|\_{F}^{2}}{N}\cdot\frac{\|B\|\_{F}^{4}}{T^{2}}. |  |

Under Assumptions A.1–A.7, as T,Nx,Ny→∞T,N\_{x},N\_{y}\to\infty, there exists an orthogonal r×rr\times r
rotation matrix H(A)H^{(A)} such that

|  |  |  |
| --- | --- | --- |
|  | 1Nx+Ny​∑i=1Nx+Ny‖Λ^i(A)−H(A)​Λi(A)‖2=𝒪p​(α¯)=𝒪P​(Nα+β−1)=oP​(1),\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\|\widehat{\Lambda}\_{i}^{(A)}-H^{(A)}\Lambda\_{i}^{(A)}\|^{2}=\mathcal{O}\_{p}(\bar{\alpha})=\mathcal{O}\_{P}(N^{\alpha+\beta-1})=o\_{P}(1), |  |

and

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=1T‖F^t(B)−H(A)​Ft(B)‖2=𝒪p​(α¯)=𝒪P​(Nα+β−1)=oP​(1).\frac{1}{T}\sum\_{t=1}^{T}\|\widehat{F}\_{t}^{(B)}-H^{(A)}F\_{t}^{(B)}\|^{2}=\mathcal{O}\_{p}(\bar{\alpha})=\mathcal{O}\_{P}(N^{\alpha+\beta-1})=o\_{P}(1). |  |

Hence both the estimated loadings and the estimated common components
are consistent.

Theorem [1](https://arxiv.org/html/2601.16274v1#Thmthm1 "Theorem 1 (Consistency under general cross-sectional attention). ‣ 3.2 Consistency ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") establishes consistency of the estimated loadings and factors under general cross-sectional and temporal attention matrices, and generalizes Theorem 1 of Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")) to a fully attention-weighted setting.

The convergence rate α¯\bar{\alpha} is primarily governed by the
cross-sectional attention matrix AzA\_{z} and depends on both the total magnitude of attention weights, captured by tr​(Az⊤​Az)\mathrm{tr}(A\_{z}^{\top}A\_{z}), and their concentration across variables, captured by ‖Az⊤​Az‖F2\|A\_{z}^{\top}A\_{z}\|\_{F}^{2}. In
particular, Assumption A.7 imposes growth-rate restrictions
tr​(Az⊤​Az)=𝒪​(Nα)\mathrm{tr}(A\_{z}^{\top}A\_{z})=\mathcal{O}(N^{\alpha}) and
‖Az⊤​Az‖F2=𝒪​(Nβ)\|A\_{z}^{\top}A\_{z}\|\_{F}^{2}=\mathcal{O}(N^{\beta}), which together imply
α¯=𝒪​(Nα+β−1)\bar{\alpha}=\mathcal{O}(N^{\alpha+\beta-1}).
A crucial step in establishing consistency is Assumption A.7, which controls the dispersion of cross-sectional attention weights. This condition is easily satisfied in several empirically relevant cases. First, when attention is normalized and evenly spread across variables—for example, when each column of AzA\_{z} has squared Euclidean norm of order 1/(Nx+Ny)1/(N\_{x}+N\_{y})—we obtain tr​(Az⊤​Az)=𝒪​(1)\mathrm{tr}(A\_{z}^{\top}A\_{z})=\mathcal{O}(1) and ‖Az⊤​Az‖F2≪Nx+Ny\|A\_{z}^{\top}A\_{z}\|\_{F}^{2}\ll N\_{x}+N\_{y}, ensuring α¯=o​(1)\bar{\alpha}=o(1). Second, when cross-sectional attention is sparse and concentrates on a subset of m≪Nx+Nym\ll N\_{x}+N\_{y} variables with unit column norm, we have tr​(Az⊤​Az)≈m\mathrm{tr}(A\_{z}^{\top}A\_{z})\approx m and
‖Az⊤​Az‖F2≈m\|A\_{z}^{\top}A\_{z}\|\_{F}^{2}\approx m, which still yields consistency provided mm grows sufficiently slowly relative to Nx+NyN\_{x}+N\_{y}.
In contrast, if attention weights are excessively concentrated so that
Assumption A.7 is violated, the convergence rate deteriorates and consistency of the factor and loading estimators may fail.
The temporal attention matrix BB enters the rate only through the factor ‖B‖F2/T\|B\|\_{F}^{2}/T. Under mild regularity conditions—such as boundedness, smoothness, or sparsity of temporal attention—we naturally have ‖B‖F2/T=𝒪​(1)\|B\|\_{F}^{2}/T=\mathcal{O}(1), so temporal attention does not affect the consistency rate.

### 3.3 Asymptotic normality

To derive asymptotic normality for the target component YY, it is not enough to know that the estimated factor space is overall consistent (Theorem [1](https://arxiv.org/html/2601.16274v1#Thmthm1 "Theorem 1 (Consistency under general cross-sectional attention). ‣ 3.2 Consistency ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")). We must also identify which coordinates of the global kk-dimensional factor space correspond to the YY-strong factors that drive the target block. This requires additional structural conditions. Assumptions B.1–B.3 and Lemma [1](https://arxiv.org/html/2601.16274v1#Thmlem1 "Lemma 1. ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") establish identification conditions formally and allow us to isolate the YY-strong subspace for inference.

Recall the attention-weighted panel in ([2.9](https://arxiv.org/html/2601.16274v1#S2.E9 "Equation 2.9 ‣ 2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~t=[Xt(A)Yt(A)]=[Λx(A)Λy(A)]​Ft(B)+et(A,B),t=1,⋯,T.\widetilde{Z}\_{t}=\begin{bmatrix}X\_{t}^{(A)}\\ Y\_{t}^{(A)}\end{bmatrix}=\begin{bmatrix}\Lambda\_{x}^{(A)}\\ \Lambda\_{y}^{(A)}\end{bmatrix}F\_{t}^{(B)}+e\_{t}^{(A,B)},\ t=1,\cdots,T. |  | (3.1) |

Here Z~t∈ℝNx+Ny\widetilde{Z}\_{t}\in\mathbb{R}^{N\_{x}+N\_{y}} denotes the (Nx+Ny)(N\_{x}+N\_{y})-dimensional cross section at time tt, obtained by stacking the XX- and YY-components. Ft(B)∈ℝkF\_{t}^{(B)}\in\mathbb{R}^{k} are the common factors, Λx(A)∈ℝNx×k\Lambda\_{x}^{(A)}\in\mathbb{R}^{N\_{x}\times k}, Λy(A)∈ℝNy×k\Lambda\_{y}^{(A)}\in\mathbb{R}^{N\_{y}\times k} are the attention-weighted loadings, and et(A,B)e\_{t}^{(A,B)} are idiosyncratic terms.

Partition the factor vector and loadings as

|  |  |  |
| --- | --- | --- |
|  | Ft(B)=[Fy,tSFtR],Λy(A)=(Λys(A),Λy,R(A)),Λx(A)=(Λx,ys(A),Λx,R(A)),F\_{t}^{(B)}=\begin{bmatrix}F\_{y,t}^{S}\\ F\_{t}^{R}\end{bmatrix},\ \Lambda\_{y}^{(A)}=(\Lambda\_{y\_{s}}^{(A)},\Lambda\_{y,R}^{(A)}),\ \Lambda\_{x}^{(A)}=(\Lambda\_{x,y\_{s}}^{(A)},\Lambda\_{x,R}^{(A)}), |  |

where we decompose k=kys+kRk=k\_{y\_{s}}+k\_{R}, with kysk\_{y\_{s}} denoting the number of YY-strong factors and kRk\_{R} collecting the remaining factors.
Fy,tS∈ℝkysF\_{y,t}^{S}\in\mathbb{R}^{k\_{y\_{s}}} denotes the YY-strong factors, FtRF\_{t}^{R} collects all remaining factors (XX-only, and shared but weak in YY), Λys(A)∈ℝNy×kys\Lambda\_{y\_{s}}^{(A)}\in\mathbb{R}^{N\_{y}\times k\_{y\_{s}}} are the YY-loadings on YY-strong factors, Λx,ys(A)∈ℝNx×kys\Lambda\_{x,y\_{s}}^{(A)}\in\mathbb{R}^{N\_{x}\times k\_{y\_{s}}} are the XX-loadings on YY-strong factors, Λy,R(A)∈ℝNy×kR\Lambda\_{y,R}^{(A)}\in\mathbb{R}^{N\_{y}\times k\_{R}} and Λx,R(A)∈ℝNx×kR\Lambda\_{x,R}^{(A)}\in\mathbb{R}^{N\_{x}\times k\_{R}} collect the remaining loadings on YY and XX, respectively. Intuitively, YY-strong factors are those with non-vanishing cross-sectional signal in the YY block, whereas the remaining factors are either XX-only or have vanishing (weak) loadings in YY. Define the block-specific loading covariance matrices

|  |  |  |
| --- | --- | --- |
|  | Σys,y(A)≡limNy,eff→∞1Ny,eff​Λys(A)⊤​Λys(A),Σys,x(A)≡limNx,eff→∞1Nx,eff​Λx,ys(A)⊤​Λx,ys(A).\Sigma\_{y\_{s},y}^{(A)}\equiv\lim\_{N\_{y,\mathrm{eff}}\to\infty}\frac{1}{N\_{y,\mathrm{eff}}}\Lambda\_{y\_{s}}^{(A)\top}\Lambda\_{y\_{s}}^{(A)},\qquad\Sigma\_{y\_{s},x}^{(A)}\equiv\lim\_{N\_{x,\mathrm{eff}}\to\infty}\frac{1}{N\_{x,\mathrm{eff}}}\Lambda\_{x,y\_{s}}^{(A)\top}\Lambda\_{x,y\_{s}}^{(A)}. |  |

Let

|  |  |  |
| --- | --- | --- |
|  | Px≡[INx000]Py≡[000INy]P\_{x}\equiv\begin{bmatrix}I\_{N\_{x}}&0\\ 0&0\end{bmatrix}\quad P\_{y}\equiv\begin{bmatrix}0&0\\ 0&I\_{N\_{y}}\end{bmatrix} |  |

be the coordinate projections onto the original XX and YY blocks. The effective cross-sectional sizes are

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Nx,eff≡tr​(Az⊤​Px​Az)=‖Px​Az‖F2,\displaystyle N\_{\text{x,eff}}\equiv\text{tr}(A\_{z}^{\top}P\_{x}A\_{z})=\left\lVert P\_{x}A\_{z}\right\rVert\_{F}^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Ny,eff≡tr​(Az⊤​Py​Az)=‖Py​Az‖F2,\displaystyle N\_{\text{y,eff}}\equiv\text{tr}(A\_{z}^{\top}P\_{y}A\_{z})=\left\lVert P\_{y}A\_{z}\right\rVert\_{F}^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Neff≡tr​(Az⊤​Az)=‖Az‖F2=Nx,eff+Ny,eff.\displaystyle N\_{\text{eff}}\equiv\text{tr}(A\_{z}^{\top}A\_{z})=\left\lVert A\_{z}\right\rVert\_{F}^{2}=N\_{\text{x,eff}}+N\_{\text{y,eff}}. |  |

When AzA\_{z} is block-diagonal, we have Nx,eff≡tr​(A1⊤​A1)N\_{\text{x,eff}}\equiv\text{tr}(A\_{1}^{\top}A\_{1}) and Ny,eff≡tr​(A2⊤​A2)N\_{\text{y,eff}}\equiv\text{tr}(A\_{2}^{\top}A\_{2}).

We impose the following additional assumptions, which we refer to as strong-factor structure and attention scaling conditions:

* B.1

  (YY-strong factors in the YY block)
  The YY-block loadings on the YY-strong factors satisfy

  |  |  |  |
  | --- | --- | --- |
  |  | ΣΛys(A)≡limNy,eff→∞1Ny,eff​Λys(A)⊤​Λys(A)≻0,\Sigma\_{\Lambda\_{y\_{s}}}^{(A)}\equiv\lim\_{N\_{y,\mathrm{eff}}\to\infty}\frac{1}{N\_{y,\mathrm{eff}}}\Lambda\_{y\_{s}}^{(A)\top}\Lambda\_{y\_{s}}^{(A)}\succ 0, |  |

  so that the YY block alone identifies the kysk\_{y\_{s}}-dimensional YY-strong
  factor subspace.
  Moreover, any remaining factor directions within the YY block generate
  eigenvalues of strictly smaller order than Ny,effN\_{y,\mathrm{eff}}.
* B.2

  (Attention scaling and relative block growth)

  (i) For g∈{x,y}g\in\{x,y\},

  |  |  |  |
  | --- | --- | --- |
  |  | 1Ng​tr⁡(Az⊤​Pg​Az)→cA,g∈(0,∞),1Ng2​‖Az⊤​Pg​Az‖F2=𝒪​(1),\frac{1}{N\_{g}}\operatorname{tr}(A\_{z}^{\top}P\_{g}A\_{z})\to c\_{A,g}\in(0,\infty),\qquad\frac{1}{N\_{g}^{2}}\|A\_{z}^{\top}P\_{g}A\_{z}\|\_{F}^{2}=\mathcal{O}(1), |  |

  so that Nx,eff≍NxN\_{\text{x,eff}}\asymp N\_{x} and Ny,eff≍NyN\_{\text{y,eff}}\asymp N\_{y}.

  (ii) The target block is not asymptotically negligible:

  |  |  |  |
  | --- | --- | --- |
  |  | NyNx+Ny→c∈(0,1)(equivalently, under (i), ​Ny,effNeff→cy∈(0,1)​).\frac{N\_{y}}{N\_{x}+N\_{y}}\to c\in(0,1)\quad\text{(equivalently, under (i), }\frac{N\_{\text{y,eff}}}{N\_{\text{eff}}}\to c\_{y}\in(0,1)\text{)}. |  |
* B.3

  (Auxiliary XX is informative for, but does not fully span, the YY-strong factor space)

  1. (i)

     (YY-block identification)
     Σys,y(A)≻0\Sigma\_{y\_{s},y}^{(A)}\succ 0, so the YY block alone identifies the
     kysk\_{y\_{s}}-dimensional YY-strong factor subspace.
  2. (ii)

     (Auxiliary informativeness)
     Σys,x(A)\Sigma\_{y\_{s},x}^{(A)} exists and is nonzero:

     |  |  |  |
     | --- | --- | --- |
     |  | Σys,x(A)≠0,\Sigma\_{y\_{s},x}^{(A)}\neq 0, |  |

     so the XX block carries non-negligible signal in at least one
     YY-strong direction.
  3. (iii)

     (No full spanning by XX)

     |  |  |  |
     | --- | --- | --- |
     |  | rank​(Σys,x(A))<kys,\mathrm{rank}\!\big(\Sigma\_{y\_{s},x}^{(A)}\big)<k\_{y\_{s}}, |  |

     so the XX block does not fully span the YY-strong factor space.
  4. (iv)

     (Comparable effective sizes)
     The effective cross-sectional sizes satisfy

     |  |  |  |
     | --- | --- | --- |
     |  | Nx,effNy,eff→cx​y∈(0,∞),\frac{N\_{x,\mathrm{eff}}}{N\_{y,\mathrm{eff}}}\to c\_{xy}\in(0,\infty), |  |

     so that the auxiliary information in XX is asymptotically non-negligible.
* B.4

  (Zero cross-sectional score / orthogonality)
  The cross-sectional score driving factor estimation is asymptotically
  uncorrelated with the time-series score driving loading estimation, so that
  for any fixed ii and tt,

  |  |  |  |
  | --- | --- | --- |
  |  | Cov​(Λys,i(A)⊤​1Neff​∑j=1NΛj,ys(A)​ej,t(A,B),((Hys(A)⊤)−1​Fy,tS)⊤​1T​∑s=1TFy,sS​ei,s(A,B))→0.\text{Cov}\!\Big(\Lambda\_{y\_{s},i}^{(A)\top}\frac{1}{\sqrt{N\_{\mathrm{eff}}}}\sum\_{j=1}^{N}\Lambda\_{j,y\_{s}}^{(A)}e\_{j,t}^{(A,B)},\;\big((H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\big)^{\top}\frac{1}{\sqrt{T}}\sum\_{s=1}^{T}F\_{y,s}^{S}e\_{i,s}^{(A,B)}\Big)\to 0. |  |

Assumptions B.1–B.3 formalize the structure required to identify the YY-strong factor subspace within the global factor space after attention weighting. Assumption B.1 states that the YY block of the attention-weighted panel contains kysk\_{y\_{s}} strong factors whose associated eigenvalues grow at rate Ny,effN\_{\text{y,eff}}, while all remaining factors contribute only lower-order eigenvalues to the YY-block covariance. This restriction concerns only the residual factor directions within the YY
block and does not preclude the auxiliary XX block from carrying non-negligible signal about the YY-strong factors (Assumption B.3). Although Assumption B.1 normalizes the strength of the YY-strong factors using
Ny,effN\_{y,\mathrm{eff}}, the convergence rates in Theorems [2](https://arxiv.org/html/2601.16274v1#Thmthm2 "Theorem 2 (Asymptotic distribution of loadings and factors under general cross-sectional attention). ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")–[3](https://arxiv.org/html/2601.16274v1#Thmthm3 "Theorem 3 (Asymptotic distribution of the common component for the 𝑌-strong block under general cross-sectional attention). ‣ Comparison with classical PCA and Target PCA. ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") are governed by NeffN\_{\mathrm{eff}}, reflecting the fact that factor estimation exploits information from the full attention-weighted panel, while identification of the YY-strong subspace relies solely on the YY block. In contrast to Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")), where both identification and estimation precision are driven solely by the size of the target block, our framework separates the two roles: the YY block alone identifies the YY-strong factor subspace, while the full attention-weighted panel determines the estimation rate via NeffN\_{\mathrm{eff}}.

Assumption B.2 ensures that the cross-sectional attention matrix does not distort the effective cross-sectional sizes, so that Nx,effN\_{\text{x,eff}} and Ny,effN\_{\text{y,eff}} grow proportionally to NxN\_{x} and NyN\_{y}, respectively, so attention redistributes information across units without concentrating mass on a vanishing subset or artificially amplifying cross-sectional signal. Assumption B.3 formalizes a transfer-learning setting in which the target block YY
identifies the Y-strong factor subspace, while the auxiliary block
XX provides additional but incomplete information that improves estimation efficiency without altering the target-specific nature of the factors. Assumption B.4 is a standard orthogonality condition ensuring that the
cross-sectional variation used to estimate factors is asymptotically uncorrelated with the time-series variation used to estimate loadings. This condition eliminates interaction terms in the asymptotic distribution of the estimated common component and simplifies inference in the mixed regime.

Our Assumption B.3 strengthens the “no full spanning” condition (Condition G.1) of Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")) by additionally requiring the auxiliary panel
XX to carry non-negligible signal in the YY-strong factor directions. While Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")) only require that
XX does not fully span the
YY-strong space, a minimal condition needed for identification when the target panel
YY may be partially observed, our transfer-learning setting explicitly focuses on efficiency gains from auxiliary information. Consequently, we allow XX to be informative, but not fully identifying, for the
YY-strong factors. Target PCA arises as a special case of our framework when XX carries no signal in the YY-strong directions.

Let ΣZ(A)=𝔼​[Z~t​Z~t⊤]\Sigma\_{Z}^{(A)}=\mathbb{E}[\widetilde{Z}\_{t}\widetilde{Z}\_{t}^{\top}] denote the population covariance of the attention-weighted panel, and let 𝒮Y\mathcal{S}\_{Y} denote the column space of Λys(A)\Lambda\_{y\_{s}}^{(A)}:

|  |  |  |
| --- | --- | --- |
|  | 𝒮Y≡span​{columns of ​Λys(A)}⊂ℝNy.\mathcal{S}\_{Y}\equiv\text{span}\{\text{columns of }\Lambda\_{y\_{s}}^{(A)}\}\subset\mathbb{R}^{N\_{y}}. |  |

###### Lemma 1.

Let ΣY​Y(A)≡𝔼​[Yt(A)​Yt(A)⊤]\Sigma\_{YY}^{(A)}\equiv\mathbb{E}[Y\_{t}^{(A)}Y\_{t}^{(A)\top}].

* (a)

  (YY-strong eigen-structure in the YY block)
  Under Assumption B.1, ΣY​Y(A)\Sigma\_{YY}^{(A)} has exactly kysk\_{y\_{s}} eigenvalues of
  order Ny,effN\_{y,\mathrm{eff}}, and the associated eigenspace equals 𝒮Y\mathcal{S}\_{Y}.
* (b)

  (Uniqueness of the YY-strong factor coordinates up to rotation)
  Let H(A)∈ℝk×kH^{(A)}\in\mathbb{R}^{k\times k} be any orthogonal rotation matrix such that
  the rotated factors F^t(B)\widehat{F}\_{t}^{(B)} and loadings Λ^(A)\widehat{\Lambda}^{(A)}
  satisfy the same asymptotic properties as in Theorem [1](https://arxiv.org/html/2601.16274v1#Thmthm1 "Theorem 1 (Consistency under general cross-sectional attention). ‣ 3.2 Consistency ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"). Partition

  |  |  |  |
  | --- | --- | --- |
  |  | H(A)=[Hys(A)HR(A)],k=kys+kR,H^{(A)}=\begin{bmatrix}H\_{y\_{s}}^{(A)}\\ H\_{R}^{(A)}\end{bmatrix},\qquad k=k\_{y\_{s}}+k\_{R}, |  |

  conformably with the population decomposition
  Ft(B)=(Fy,tS,FtR)F\_{t}^{(B)}=(F\_{y,t}^{S},\,F\_{t}^{R}) and Λy(A)=(Λys(A),Λy,R(A))\Lambda\_{y}^{(A)}=(\Lambda\_{y\_{s}}^{(A)},\,\Lambda\_{y,R}^{(A)}).
  Then the effect of H(A)H^{(A)} on the YY block is identified only up to an
  orthogonal rotation within the kysk\_{y\_{s}}-dimensional YY-strong subspace: if
  H~(A)\widetilde{H}^{(A)} is another orthogonal matrix yielding the same limiting
  YY-block eigenspace 𝒮Y\mathcal{S}\_{Y}, then there exists a kys×kysk\_{y\_{s}}\times k\_{y\_{s}}
  orthogonal matrix QQ such that

  |  |  |  |
  | --- | --- | --- |
  |  | H~ys(A)=Q​Hys(A).\widetilde{H}\_{y\_{s}}^{(A)}=Q\,H\_{y\_{s}}^{(A)}. |  |

  Equivalently, the YY-strong factor coordinates are unique up to rotation within
  the kysk\_{y\_{s}}-dimensional subspace.

Lemma [1](https://arxiv.org/html/2601.16274v1#Thmlem1 "Lemma 1. ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") explains how the target block YY identifies economically relevant factors within the globally estimated factor space. While PCA applied to the attended panel Z~\widetilde{Z} consistently recovers the kk-dimensional factor space, it does not by itself determine which factor directions drive variation in YY. Part (a) shows that, under block-specific strength conditions, the YY-block covariance exhibits exactly kysk\_{y\_{s}} eigenvalues diverging at rate Ny,effN\_{y,\mathrm{eff}}, ensuring that the associated eigenspace coincides with the span of the YY-strong loadings. Part  (b) then establishes that the corresponding factor coordinates are unique up to an orthogonal rotation within the kysk\_{y\_{s}}-dimensional subspace. Together, these results provide the key identification step needed for inference on the target component.

Theorem [2](https://arxiv.org/html/2601.16274v1#Thmthm2 "Theorem 2 (Asymptotic distribution of loadings and factors under general cross-sectional attention). ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") shows the asymptotic distribution of estimated YY-strong factors and loadings.

###### Theorem 2 (Asymptotic distribution of loadings and factors under general cross-sectional attention).

Assume A.1–A.7 and B.1–B.3 hold. Also, suppose
T​Nα+β−1→0TN^{\alpha+\beta-1}\to 0 and 3​α2+β<1\frac{3\alpha}{2}+\beta<1, which corresponds to T​α¯→0T\bar{\alpha}\to 0 and Neff​α¯→0\sqrt{N\_{\mathrm{eff}}}\bar{\alpha}\to 0.

Let ΣF,y(B)=𝔼​[Fy,tS​Fy,tS⊤]\Sigma\_{F,y}^{(B)}=\mathbb{E}[F\_{y,t}^{S}F\_{y,t}^{S\top}] and let
Sy=[Ikys​  0]S\_{y}=[I\_{k\_{y\_{s}}}\;\;0] so that Fy,tS=Sy​Ft(B)F\_{y,t}^{S}=S\_{y}F\_{t}^{(B)}.
For each i∈{1,…,N}i\in\{1,\ldots,N\}, let Λi,ys(A)≡Sy​Λi(A)\Lambda\_{i,y\_{s}}^{(A)}\equiv S\_{y}\Lambda\_{i}^{(A)}
denote the loading vector on the YY-strong factors.

* (a)

  For a YY-unit i∈{1,…,Ny}i\in\{1,\ldots,N\_{y}\}, and the block of loadings on the YY-strong factors, Λys,i(A)∈ℝkys\Lambda\_{y\_{s},i}^{(A)}\in\mathbb{R}^{k\_{y\_{s}}}, we have

  |  |  |  |
  | --- | --- | --- |
  |  | T​(Λ^ys,i(A)−Hys(A)​Λys,i(A))→𝑑𝒩​(0,VΛ,y,i(A,B)),\sqrt{T}\Big(\widehat{\Lambda}\_{y\_{s},i}^{(A)}-H\_{y\_{s}}^{(A)}\Lambda\_{y\_{s},i}^{(A)}\Big)\xrightarrow[]{d}\mathcal{N}\big(0,V\_{\Lambda,y,i}^{(A,B)}\big), |  |

  where the asymptotic covariance is

  |  |  |  |
  | --- | --- | --- |
  |  | VΛ,y,i(A,B)=(ΣF,y(B))−1​Ωy,i(A,B)​(ΣF,y(B))−1,V\_{\Lambda,y,i}^{(A,B)}=(\Sigma\_{F,y}^{(B)})^{-1}\,\Omega\_{y,i}^{(A,B)}\,(\Sigma\_{F,y}^{(B)})^{-1}, |  |

  with

  |  |  |  |
  | --- | --- | --- |
  |  | Ωy,i(A,B)=limT→∞Var⁡(1T​∑t=1TFy,tS​ei,t(A,B)).\Omega\_{y,i}^{(A,B)}=\lim\_{T\to\infty}\operatorname{Var}\!\Big(\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}F\_{y,t}^{S}\,e\_{i,t}^{(A,B)}\Big). |  |
* (b)

  For any fixed tt, the estimator of the YY-strong factors satisfies

  |  |  |  |
  | --- | --- | --- |
  |  | Neff​(F^y,tS−(Hys(A)⊤)−1​Fy,tS)→𝑑𝒩​(0,VF,t(A,B)),\sqrt{N\_{\text{eff}}}\Big(\widehat{F}\_{y,t}^{S}-(H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\Big)\xrightarrow{d}\mathcal{N}\big(0,V\_{F,t}^{(A,B)}\big), |  |

  where

  |  |  |  |
  | --- | --- | --- |
  |  | VF,t(A,B)=(ΣΛ,ys(A))−1​Ξys,t(A,B)​(ΣΛ,ys(A))−1,ΣΛ,ys(A)=limNeff→∞1Neff​∑i=1NΛi,ys(A)​Λi,ys(A)⊤,V\_{F,t}^{(A,B)}=(\Sigma\_{\Lambda,y\_{s}}^{(A)})^{-1}\,\Xi\_{y\_{s},t}^{(A,B)}\,(\Sigma\_{\Lambda,y\_{s}}^{(A)})^{-1},\qquad\Sigma\_{\Lambda,y\_{s}}^{(A)}=\lim\_{N\_{\text{eff}}\to\infty}\frac{1}{N\_{\text{eff}}}\sum\_{i=1}^{N}\Lambda\_{i,y\_{s}}^{(A)}\Lambda\_{i,y\_{s}}^{(A)\top}, |  |

  and

  |  |  |  |
  | --- | --- | --- |
  |  | Ξys,t(A,B)=limNeff→∞Var​(1Neff​∑i=1NΛi,ys(A)​ei,t(A,B)).\Xi\_{y\_{s},t}^{(A,B)}=\lim\_{N\_{\text{eff}}\to\infty}\text{Var}\!\Big(\frac{1}{\sqrt{N\_{\text{eff}}}}\sum\_{i=1}^{N}\Lambda\_{i,y\_{s}}^{(A)}e\_{i,t}^{(A,B)}\Big). |  |

Ωy,i(A,B)\Omega\_{y,i}^{(A,B)} and Ξt(A,B)\Xi\_{t}^{(A,B)} are long-run covariance matrices, allowing for temporal and cross-sectional dependence induced by attention weighting. The identification of Theorem [2](https://arxiv.org/html/2601.16274v1#Thmthm2 "Theorem 2 (Asymptotic distribution of loadings and factors under general cross-sectional attention). ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") is ensured by Assumptions B.1–B.3 and Lemma [1](https://arxiv.org/html/2601.16274v1#Thmlem1 "Lemma 1. ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), which separates the YY-strong subspace from the rest of the factor space. Although the YY-strong factors are identified by the YY-block covariance, their estimation exploits auxiliary information from XX through joint regression, leading to Neff\sqrt{N\_{\text{eff}}} convergence under non-negligible cross-block signal.

#### Comparison with classical PCA and Target PCA.

The growth conditions in Theorem [2](https://arxiv.org/html/2601.16274v1#Thmthm2 "Theorem 2 (Asymptotic distribution of loadings and factors under general cross-sectional attention). ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") imply T=o​(N1−(α+β))T=o(N^{1-(\alpha+\beta)}).These conditions are a natural extension of those in
classical approximate factor models. In Bai ([2003](https://arxiv.org/html/2601.16274v1#bib.bib25 "Inferential theory for factor models of large dimensions")), consistency and inference are obtained under the regime T=o​(N)T=o(N), reflecting the requirement
that effective cross-sectional information dominates the time dimension. Our conditions recover this classical case when the cross-sectional attention matrix is diffuse, so that tr​(Az⊤​Az)≍N\mathrm{tr}(A\_{z}^{\top}A\_{z})\asymp N and
‖Az⊤​Az‖F2=𝒪​(N)\|A\_{z}^{\top}A\_{z}\|\_{F}^{2}=\mathcal{O}(N), implying α¯=𝒪​(1/N)\bar{\alpha}=\mathcal{O}(1/N) and hence T​α¯→0T\bar{\alpha}\to 0 reduces to T=o​(N)T=o(N). When attention concentrates mass on
a lower-dimensional subset of units, the effective cross-sectional size
Neff=tr​(Az⊤​Az)N\_{\mathrm{eff}}=\mathrm{tr}(A\_{z}^{\top}A\_{z}) grows more slowly than NN, and the admissible growth rate of TT adjusts accordingly. This trade-off is analogous
to the bias–variance balance induced by regularization or projection in high-dimensional estimation and is intrinsic to attention-weighted designs.
Relative to Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")), which enforces a fixed projection structure and primarily exploits the target block to recover strong factors, our framework allows auxiliary units to contribute at the Neff\sqrt{N\_{\mathrm{eff}}} scale
without altering identification, yielding inference conditions that
interpolate smoothly between classical PCA and targeted factor extraction. In this sense, the proposed growth conditions are not restrictive but rather endogenously determined by the degree of cross-sectional concentration induced by attention.

Define the true and estimated YY-strong common component as

|  |  |  |
| --- | --- | --- |
|  | Cy,i,t≡Λys,i(A)⊤​Fy,tS,C^y,i,t≡Λ^ys,i(A)⊤​F^y,tS.C\_{y,i,t}\equiv\Lambda\_{y\_{s},i}^{(A)\top}F\_{y,t}^{S},\qquad\widehat{C}\_{y,i,t}\equiv\widehat{\Lambda}\_{y\_{s},i}^{(A)\top}\widehat{F}\_{y,t}^{S}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | C^y,i,t−Cy,i,t=Λys,i(A)⊤​(F^y,tS−(Hys(A)⊤)−1​Fy,tS)⏟ΔF,i​t+(Λ^ys,i(A)−Hys(A)​Λys,i(A))⊤​(Hys(A)⊤)−1​Fy,tS⏟ΔΛ,i​t+ri,t,\widehat{C}\_{y,i,t}-C\_{y,i,t}=\underbrace{\Lambda\_{y\_{s},i}^{(A)\top}\Big(\widehat{F}\_{y,t}^{S}-(H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\Big)}\_{\Delta\_{F,it}}+\underbrace{\Big(\widehat{\Lambda}\_{y\_{s},i}^{(A)}-H\_{y\_{s}}^{(A)}\Lambda\_{y\_{s},i}^{(A)}\Big)^{\top}(H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}}\_{\Delta\_{\Lambda,it}}+r\_{i,t}, |  |

with ri,t=op​(Neff−1/2+T−1/2)r\_{i,t}=o\_{p}(N\_{\mathrm{eff}}^{-1/2}+T^{-1/2}).

Let VΛ,y,i(A,B)V\_{\Lambda,y,i}^{(A,B)} and VF,t(A,B)V\_{F,t}^{(A,B)} be the asymptotic covariance
matrices in Theorem [2](https://arxiv.org/html/2601.16274v1#Thmthm2 "Theorem 2 (Asymptotic distribution of loadings and factors under general cross-sectional attention). ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"). Define

|  |  |  |
| --- | --- | --- |
|  | σC,i​t,F2≡Λys,i(A)⊤​VF,t(A,B)​Λys,i(A),σC,i​t,Λ2≡((Hys(A)⊤)−1​Fy,tS)⊤​VΛ,y,i(A,B)​((Hys(A)⊤)−1​Fy,tS).\sigma^{2}\_{C,it,F}\equiv\Lambda\_{y\_{s},i}^{(A)\top}V\_{F,t}^{(A,B)}\Lambda\_{y\_{s},i}^{(A)},\qquad\sigma^{2}\_{C,it,\Lambda}\equiv\big((H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\big)^{\top}V\_{\Lambda,y,i}^{(A,B)}\big((H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\big). |  |

Theorem [3](https://arxiv.org/html/2601.16274v1#Thmthm3 "Theorem 3 (Asymptotic distribution of the common component for the 𝑌-strong block under general cross-sectional attention). ‣ Comparison with classical PCA and Target PCA. ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") establishes the asymptotic distribution of Cy,i,tC\_{y,i,t} for three different regimes that depend on the relative growth of NeffN\_{\text{eff}} and TT.

###### Theorem 3 (Asymptotic distribution of the common component for the YY-strong block under general cross-sectional attention).

Assume A.1–A.7, B.1–B.3, Lemma [1](https://arxiv.org/html/2601.16274v1#Thmlem1 "Lemma 1. ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), and the conditions of Theorem [2](https://arxiv.org/html/2601.16274v1#Thmthm2 "Theorem 2 (Asymptotic distribution of loadings and factors under general cross-sectional attention). ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") hold.
In addition, assume Assumption B.4 (score orthogonality).

Fix a YY-unit i∈{1,…,Ny}i\in\{1,\ldots,N\_{y}\} and a time index tt.

* (i)

  FF-dominant regime.
  If Neff/T→0N\_{\mathrm{eff}}/T\to 0, then

  |  |  |  |
  | --- | --- | --- |
  |  | Neff​(C^y,i,t−Cy,i,t)=Neff​ΔF,i​t+op​(1)→𝑑𝒩​(0,σC,i​t,F2).\sqrt{N\_{\mathrm{eff}}}\big(\widehat{C}\_{y,i,t}-C\_{y,i,t}\big)=\sqrt{N\_{\mathrm{eff}}}\Delta\_{F,it}+o\_{p}(1)\xrightarrow{d}\mathcal{N}\big(0,\sigma^{2}\_{C,it,F}\big). |  |
* (ii)

  Λ\Lambda-dominant regime.
  If T/Neff→0T/N\_{\mathrm{eff}}\to 0, then

  |  |  |  |
  | --- | --- | --- |
  |  | T​(C^y,i,t−Cy,i,t)=T​ΔΛ,i​t+op​(1)→𝑑𝒩​(0,σC,i​t,Λ2).\sqrt{T}\big(\widehat{C}\_{y,i,t}-C\_{y,i,t}\big)=\sqrt{T}\Delta\_{\Lambda,it}+o\_{p}(1)\xrightarrow{d}\mathcal{N}\big(0,\sigma^{2}\_{C,it,\Lambda}\big). |  |
* (iii)

  Mixed regime.
  If Neff/T→c∈(0,∞)N\_{\mathrm{eff}}/T\to c\in(0,\infty), then

  |  |  |  |
  | --- | --- | --- |
  |  | T​(C^y,i,t−Cy,i,t)→𝑑𝒩​(0,σC,i​t2),\sqrt{T}\big(\widehat{C}\_{y,i,t}-C\_{y,i,t}\big)\xrightarrow{d}\mathcal{N}\big(0,\sigma^{2}\_{C,it}\big), |  |

  where

  |  |  |  |
  | --- | --- | --- |
  |  | σC,i​t2=σC,i​t,Λ2+c​σC,i​t,F2.\sigma^{2}\_{C,it}=\sigma^{2}\_{C,it,\Lambda}+c\,\sigma^{2}\_{C,it,F}. |  |

The asymptotic behavior of the YY-common component reflects the relative
informativeness of the cross-sectional and time-series dimensions after
attention weighting.

In regime (i), where Neff/T→0N\_{\mathrm{eff}}/T\to 0, the time dimension is large
relative to the effective cross section, so factor estimation error dominates
the asymptotic distribution of the common component. In regime (ii), where
T/Neff→0T/N\_{\mathrm{eff}}\to 0, the effective cross section is large relative to the
time dimension, and loading estimation error is the primary source of
uncertainty. Regime (iii) covers scenarios in which neither dimension is
asymptotically dominant, and both factor and loading estimation errors
contribute to the limiting distribution. This mixed regime naturally
accommodates balanced panels in which NeffN\_{\mathrm{eff}} and TT grow at
comparable rates.

###### Remark 1 (Efficiency gains from transfer learning).

Consider the YY-strong common component
Cy,i,t=Λys,i(A)⊤​Fy,tSC\_{y,i,t}=\Lambda\_{y\_{s},i}^{(A)\top}F\_{y,t}^{S}
for a fixed YY-unit ii.
In the factor-dominant and mixed regimes of Theorem [3](https://arxiv.org/html/2601.16274v1#Thmthm3 "Theorem 3 (Asymptotic distribution of the common component for the 𝑌-strong block under general cross-sectional attention). ‣ Comparison with classical PCA and Target PCA. ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), its leading
variance contribution is

|  |  |  |
| --- | --- | --- |
|  | σC,i​t,F2=Λys,i(A)⊤​VF,t(A,B)​Λys,i(A),\sigma^{2}\_{C,it,F}=\Lambda\_{y\_{s},i}^{(A)\top}V\_{F,t}^{(A,B)}\Lambda\_{y\_{s},i}^{(A)}, |  |

where VF,t(A,B)V\_{F,t}^{(A,B)} is the asymptotic covariance of the estimated
YY-strong factors in Theorem [2](https://arxiv.org/html/2601.16274v1#Thmthm2 "Theorem 2 (Asymptotic distribution of loadings and factors under general cross-sectional attention). ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")(b).

To assess the role of auxiliary information, compare the joint estimator based on
(X,Y)(X,Y) with a YY-only analogue obtained by applying the same estimation
procedure to the YY block alone. Let
Σysjoint\Sigma\_{y\_{s}}^{\mathrm{joint}} and ΣysY\Sigma\_{y\_{s}}^{Y} denote the second-moment
matrices of the YY-strong loadings under the joint and YY-only aggregations,
respectively, and let Ξys,tjoint\Xi\_{y\_{s},t}^{\mathrm{joint}} and Ξys,tY\Xi\_{y\_{s},t}^{Y} be the
corresponding long-run covariance matrices of the attention-weighted
idiosyncratic scores. Then

|  |  |  |
| --- | --- | --- |
|  | VF,tjoint=(Σysjoint)−1​Ξys,tjoint​(Σysjoint)−1,VF,tY=(ΣysY)−1​Ξys,tY​(ΣysY)−1.V\_{F,t}^{\mathrm{joint}}=(\Sigma\_{y\_{s}}^{\mathrm{joint}})^{-1}\Xi\_{y\_{s},t}^{\mathrm{joint}}(\Sigma\_{y\_{s}}^{\mathrm{joint}})^{-1},\qquad V\_{F,t}^{Y}=(\Sigma\_{y\_{s}}^{Y})^{-1}\Xi\_{y\_{s},t}^{Y}(\Sigma\_{y\_{s}}^{Y})^{-1}. |  |

Under Assumption B.3, the auxiliary block contributes nonzero signal only on a
proper subspace
𝒮X≡Range​(Σys,x(A))⊊ℝkys,\mathcal{S}\_{X}\equiv\mathrm{Range}(\Sigma\_{y\_{s},x}^{(A)})\subsetneq\mathbb{R}^{k\_{y\_{s}}},
so that
Σysjoint⪰ΣysY\Sigma\_{y\_{s}}^{\mathrm{joint}}\succeq\Sigma\_{y\_{s}}^{Y}
and hence
(Σysjoint)−1⪯(ΣysY)−1(\Sigma\_{y\_{s}}^{\mathrm{joint}})^{-1}\preceq(\Sigma\_{y\_{s}}^{Y})^{-1}.
Moreover, suppose the auxiliary block has non-negligible effective size,
Nx,eff/Ny,eff→cx​y∈(0,∞)N\_{x,\mathrm{eff}}/N\_{y,\mathrm{eff}}\to c\_{xy}\in(0,\infty), and that the
attention-weighted idiosyncratic score variance does not increase under joint
aggregation:

|  |  |  |
| --- | --- | --- |
|  | lim supNeff→∞Var​(1Neff​∑i=1NΛi,ys(A)​ei,t(A,B))⪯lim supNy,eff→∞Var​(1Ny,eff​∑i∈YΛi,ys(A)​ei,t(A,B)).\limsup\_{N\_{\mathrm{eff}}\to\infty}\text{Var}\!\Big(\frac{1}{\sqrt{N\_{\mathrm{eff}}}}\sum\_{i=1}^{N}\Lambda\_{i,y\_{s}}^{(A)}e\_{i,t}^{(A,B)}\Big)\;\preceq\;\limsup\_{N\_{y,\mathrm{eff}}\to\infty}\text{Var}\!\Big(\frac{1}{\sqrt{N\_{y,\mathrm{eff}}}}\sum\_{i\in Y}\Lambda\_{i,y\_{s}}^{(A)}e\_{i,t}^{(A,B)}\Big). |  |

Then Ξys,tjoint⪯Ξys,tY\Xi\_{y\_{s},t}^{\mathrm{joint}}\preceq\Xi\_{y\_{s},t}^{Y} and hence
VF,tjoint⪯VF,tYV\_{F,t}^{\mathrm{joint}}\preceq V\_{F,t}^{Y}.
Moreover, the inequality is strict along directions that load on
𝒮X\mathcal{S}\_{X}: for any YY-unit ii such that
Λys,i(A)\Lambda\_{y\_{s},i}^{(A)} has a nonzero projection onto 𝒮X\mathcal{S}\_{X},

|  |  |  |
| --- | --- | --- |
|  | σC,i​t,F2​(joint)<σC,i​t,F2​(Y-only).\sigma^{2}\_{C,it,F}(\text{joint})<\sigma^{2}\_{C,it,F}(\text{$Y$-only}). |  |

Thus, even when the auxiliary block does not fully span the YY-strong factor
space, transfer learning through the joint attention-weighted estimator delivers
strict efficiency gains for those components of the target signal that overlap
with auxiliary information, while preserving identification of the
YY-strong factors.

## 4 Nonlinear signals

Sections [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") and [3](https://arxiv.org/html/2601.16274v1#S3 "3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") developed a
theoretical framework for extracting low-dimensional latent representations
from attention-weighted panels under linear signal structures.
This framework can be viewed as a solution to a representation learning problem, in which the attended data Z~\widetilde{Z} are projected onto a low-dimensional latent space that captures their dominant common components.

In many empirical applications, however, linear representations may be
restrictive. A growing literature in macroeconomics and finance documents
substantial nonlinearities in the mapping from high-dimensional predictors to latent economic states and forecasts
(Cheng and Hansen, [2015](https://arxiv.org/html/2601.16274v1#bib.bib36 "Forecasting with factor-augmented regression: a frequentist model averaging approach"); Gu et al., [2021](https://arxiv.org/html/2601.16274v1#bib.bib1 "Autoencoder asset pricing models"); Goulet Coulombe et al., [2025](https://arxiv.org/html/2601.16274v1#bib.bib35 "Panel machine learning with mixed-frequency data: monitoring state-level fiscal variables")).
Rather than abandoning the linear framework developed above, we embed it within a more general representation learning architecture that allows for nonlinear signal extraction while preserving the same latent-variable interpretation.

Recall that the target and auxiliary datasets have the following signal plus noise structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Y⏟T×Ny=Ψy+ey,\displaystyle\underbrace{Y}\_{T\times N\_{y}}=\Psi\_{y}+e\_{y}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | X⏟T×Nx=Ψx+ex.\displaystyle\underbrace{X}\_{T\times N\_{x}}=\Psi\_{x}+e\_{x}. |  |

The “attended” inputs were defined as

|  |  |  |
| --- | --- | --- |
|  | Z~=B​[XY]​Az.\widetilde{Z}=B\begin{bmatrix}X&Y\end{bmatrix}A\_{z}. |  |

Recall that in the linear case the factor model for Z~\widetilde{Z} is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~=F(B)​(Λ(A))⊤+e~,e~≡B​[exey]​Az.\widetilde{Z}=F^{(B)}(\Lambda^{(A)})^{\top}+\widetilde{e},\qquad\widetilde{e}\equiv B\,[e\_{x}\ \ e\_{y}]\,A\_{z}. |  | (4.1) |

Let D^(A)≔diag​(λ1(A),…,λk(A))\widehat{D}^{(A)}\coloneqq\mathrm{diag}(\lambda\_{1}^{(A)},\ldots,\lambda\_{k}^{(A)})
denote the diagonal matrix collecting the largest kk eigenvalues of
Z~⊤​Z~/(Nx+Ny)\widetilde{Z}^{\top}\widetilde{Z}/(N\_{x}+N\_{y}).
These eigenvalues capture the relative strength of the attention-weighted common components,
analogously to standard PCA.
Let S=diag​(s1,…,sk)S=\mathrm{diag}(s\_{1},\ldots,s\_{k}) denote the corresponding singular values, so that

|  |  |  |
| --- | --- | --- |
|  | D^(A)=S2Nx+Ny.\widehat{D}^{(A)}=\frac{S^{2}}{N\_{x}+N\_{y}}. |  |

Equivalently to the standard PCA formulation in ([2.12](https://arxiv.org/html/2601.16274v1#S2.E12 "Equation 2.12 ‣ 2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")),
a singular value decomposition (SVD) of Z~\widetilde{Z} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~=P^​S​Q^⊤,\widetilde{Z}=\widehat{P}\,S\,\widehat{Q}^{\top}, |  | (4.2) |

where P^∈ℝT×k\widehat{P}\in\mathbb{R}^{T\times k} and
Q^∈ℝ(Nx+Ny)×k\widehat{Q}\in\mathbb{R}^{(N\_{x}+N\_{y})\times k}
contain the left and right singular vectors associated with the top kk singular values collected in the diagonal matrix D^(A)\widehat{D}^{(A)}.

This representation is equivalent to a one-layer linear autoencoder with kk latent units.
Specifically, letting

|  |  |  |
| --- | --- | --- |
|  | ℰθ​(Z~t)=b(0)+W(0)​Z~t∈ℝk\mathcal{E}\_{\theta}(\widetilde{Z}\_{t})=b^{(0)}+W^{(0)}\widetilde{Z}\_{t}\in\mathbb{R}^{k} |  |

denote the *encoding map* ℰθ:ℝNx+Ny→ℝk\mathcal{E}\_{\theta}:\mathbb{R}^{N\_{x}+N\_{y}}\to\mathbb{R}^{k} that extracts
a kk-dimensional summary of the attended panel Z~t\widetilde{Z}\_{t}.

The reconstruction is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~t=b(1)+W(1)​ℰθ​(Z~t)+e~t=b(1)+W(1)​(b(0)+W(0)​Z~t)+e~t,\widetilde{Z}\_{t}=b^{(1)}+W^{(1)}\mathcal{E}\_{\theta}(\widetilde{Z}\_{t})+\widetilde{e}\_{t}=b^{(1)}+W^{(1)}\bigl(b^{(0)}+W^{(0)}\widetilde{Z}\_{t}\bigr)+\widetilde{e}\_{t}, |  | (4.3) |

where
W(0)∈ℝk×(Nx+Ny)W^{(0)}\in\mathbb{R}^{k\times(N\_{x}+N\_{y})},
W(1)∈ℝ(Nx+Ny)×kW^{(1)}\in\mathbb{R}^{(N\_{x}+N\_{y})\times k}, b(0)∈ℝkb^{(0)}\in\mathbb{R}^{k} are weight matrices, and b(1)∈ℝNx+Nyb^{(1)}\in\mathbb{R}^{N\_{x}+N\_{y}} are bias vectors.

The parameters (b(0),b(1),W(0),W(1))(b^{(0)},b^{(1)},W^{(0)},W^{(1)}) are estimated by solving

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | minθ={b,W}∑t=1T∥Z~t−(b(1)+W(1)ℰθ(Z~t)))∥2\displaystyle\min\_{{}\_{\theta=\{b,W\}}}\sum\_{t=1}^{T}\left\lVert\widetilde{Z}\_{t}-(b^{(1)}+W^{(1)}\mathcal{E}\_{\theta}(\widetilde{Z}\_{t})))\right\rVert^{2} |  | (4.4) |
|  |  | =minb,W⁡‖Z~−(ι​b(1)⊤+(ι​b(0)⊤+W(0)​Z~)​W(1)⊤)‖F2,\displaystyle=\min\_{b,W}\left\lVert\widetilde{Z}-(\iota b^{(1)\top}+(\iota b^{(0)\top}+W^{(0)}\widetilde{Z})W^{(1)\top})\right\rVert\_{F}^{2}, |  |

where ι\iota is a T×1T\times 1 vector of ones.

The next proposition, adapted from Gu et al. ([2021](https://arxiv.org/html/2601.16274v1#bib.bib1 "Autoencoder asset pricing models")), establishes the equivalence
between the linear encoder in ([4.3](https://arxiv.org/html/2601.16274v1#S4.E3 "Equation 4.3 ‣ 4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) and the PCA estimator
introduced in Section [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").

###### Proposition 4 (Linear autoencoder–PCA equivalence).

Consider the optimization problem ([4.4](https://arxiv.org/html/2601.16274v1#S4.E4 "Equation 4.4 ‣ 4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")).
Let Z~=P^​S​Q^⊤\widetilde{Z}=\widehat{P}S\widehat{Q}^{\top} be the rank-kk singular value
decomposition of Z~\widetilde{Z}.
Then the full set of global minimizers is given by

|  |  |  |
| --- | --- | --- |
|  | W^(1)=Q^​R,W^(0)=R−1​Q^⊤,\widehat{W}^{(1)}=\widehat{Q}R,\qquad\widehat{W}^{(0)}=R^{-1}\widehat{Q}^{\top}, |  |

for any nonsingular matrix R∈ℝk×kR\in\mathbb{R}^{k\times k}.

For any such choice of (W^(0),W^(1))(\widehat{W}^{(0)},\widehat{W}^{(1)}),
the bias parameters may be chosen as

|  |  |  |
| --- | --- | --- |
|  | b^(0)∈ℝk​arbitrary,b^(1)=Z~¯−W^(1)​(b^(0)+W^(0)​Z~¯),\widehat{b}^{(0)}\in\mathbb{R}^{k}\ \text{arbitrary},\qquad\widehat{b}^{(1)}=\bar{\widetilde{Z}}-\widehat{W}^{(1)}\bigl(\widehat{b}^{(0)}+\widehat{W}^{(0)}\bar{\widetilde{Z}}\bigr), |  |

where Z~¯=T−1​∑t=1TZ~t\bar{\widetilde{Z}}=T^{-1}\sum\_{t=1}^{T}\widetilde{Z}\_{t}.

###### Proof.

The result follows from the characterization of global minimizers of linear
autoencoders and their equivalence to PCA.
The argument parallels that in Gu et al. ([2021](https://arxiv.org/html/2601.16274v1#bib.bib1 "Autoencoder asset pricing models")) and is therefore omitted.
∎

Proposition [4](https://arxiv.org/html/2601.16274v1#Thmthm4 "Proposition 4 (Linear autoencoder–PCA equivalence). ‣ 4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") shows that a one-layer linear autoencoder with kk hidden
units is equivalent to a linear factor model with kk latent factors.
Up to an invertible linear transformation, the estimated latent factors and
loadings coincide with those obtained from attention-weighted PCA.
In particular, the estimated factors and loadings may be written as

|  |  |  |
| --- | --- | --- |
|  | F^(B)=P^​R−1​(Nx+Ny)1/2,Λ^(A)=Q^​R​(Nx+Ny)1/2,\widehat{F}^{(B)}=\widehat{P}R^{-1}(N\_{x}+N\_{y})^{1/2},\qquad\widehat{\Lambda}^{(A)}=\widehat{Q}R(N\_{x}+N\_{y})^{1/2}, |  |

which matches the normalization used in Section [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"). In other words, in the linear case, ℰθ​(⋅)\mathcal{E}\_{\theta}(\cdot) coincides (up to rotation and scaling) with the PCA factor extraction map.

Viewed through the lens of representation learning, the linear autoencoder
analyzed above induces an affine encoding map
ℰθ:ℝNx+Ny→ℝk\mathcal{E}\_{\theta}:\mathbb{R}^{N\_{x}+N\_{y}}\to\mathbb{R}^{k}
that extracts a kk-dimensional low-rank representation from the attended panel Z~\widetilde{Z}. This encoding map coincides, up to rotation, with PCA-based factor extraction in the linear case.
A natural extension is to enlarge the class of admissible encoding maps by
allowing for nonlinear transformations, while preserving the same low-dimensional bottleneck and representation-learning structure.

Autoencoder models are therefore more general than linear factor models, as they permit nonlinear signal extraction through compositions of nonlinear transformations of Z~\widetilde{Z}.
In particular, autoencoder architectures with MM hidden layers can be written recursively as follows.

Let K(m)K^{(m)} denote the number of neurons in layer m=1,…,Mm=1,\ldots,M.
For each layer mm, let Z~(m)∈ℝK(m)\widetilde{Z}^{(m)}\in\mathbb{R}^{K^{(m)}} denote the vector of neuron outputs, with components
Z~(m)=(Z~1(m),…,Z~K(m)(m))⊤\widetilde{Z}^{(m)}=(\widetilde{Z}^{(m)}\_{1},\ldots,\widetilde{Z}^{(m)}\_{K^{(m)}})^{\top}.
The input layer is given by Z~(0)≡Z~\widetilde{Z}^{(0)}\equiv\widetilde{Z}.

For m≥1m\geq 1, the output of layer mm is generated recursively according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~(m)=g​(b(m−1)+W(m−1)​Z~(m−1)),\widetilde{Z}^{(m)}=g\!\left(b^{(m-1)}+W^{(m-1)}\widetilde{Z}^{(m-1)}\right), |  | (4.5) |

where g​(⋅)g(\cdot) is an elementwise nonlinear activation function,
W(m−1)∈ℝK(m)×K(m−1)W^{(m-1)}\in\mathbb{R}^{K^{(m)}\times K^{(m-1)}} is a matrix of weight parameters,
and b(m−1)∈ℝK(m)b^{(m-1)}\in\mathbb{R}^{K^{(m)}} is a vector of bias parameters.
By construction, Z~(m)∈ℝK(m)\widetilde{Z}^{(m)}\in\mathbb{R}^{K^{(m)}} and Z~(m−1)∈ℝK(m−1)\widetilde{Z}^{(m-1)}\in\mathbb{R}^{K^{(m-1)}}.

The nonlinear encoding map is defined as the composition of the layer-wise
transformations,

|  |  |  |
| --- | --- | --- |
|  | ℰθ​(Z~)≡Z~(M)=(ϕM,θ∘⋯∘ϕ1,θ)​(Z~),ϕm,θ​(u)=g​(b(m−1)+W(m−1)​u),\mathcal{E}\_{\theta}(\widetilde{Z})\;\equiv\;\widetilde{Z}^{(M)}=\bigl(\phi\_{M,\theta}\circ\cdots\circ\phi\_{1,\theta}\bigr)(\widetilde{Z}),\qquad\phi\_{m,\theta}(u)=g\!\left(b^{(m-1)}+W^{(m-1)}u\right), |  |

so that ℰθ:ℝNx+Ny→ℝk\mathcal{E}\_{\theta}:\mathbb{R}^{N\_{x}+N\_{y}}\to\mathbb{R}^{k} denotes the terminal output of the
MM-layer encoder and extracts a
kk-dimensional low-rank representation from the attended panel Z~\widetilde{Z}. Here ∘\circ denotes function composition ((f∘g)​(x)=f​(g​(x))(f\circ g)(x)=f(g(x))).

When the activation function satisfies g​(x)=xg(x)=x and the encoder has a single hidden layer (M=1M=1), the encoding map ℰθ\mathcal{E}\_{\theta} reduces to the linear case and coincides, up to rotation, with attention-weighted PCA. More general choices of g​(⋅)g(\cdot) enlarge the class of admissible encoding maps, allowing ℰθ​(Z~)\mathcal{E}\_{\theta}(\widetilde{Z}) to capture nonlinear structure in Z~\widetilde{Z} while retaining the same low-dimensional bottleneck interpretation.
Figure [1](https://arxiv.org/html/2601.16274v1#S4.F1 "Figure 1 ‣ 4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") provides a schematic summary of this nesting, highlighting that the linear and nonlinear specifications differ only in the choice of the transformation g​(⋅)g(\cdot) governing the mapping of the attended panel Z~\widetilde{Z}. We implement the nonlinear encoding map ℰθ\mathcal{E}\_{\theta} using a Transformer-based architecture, which parameterizes the activation g​(⋅)g(\cdot) in ([4.5](https://arxiv.org/html/2601.16274v1#S4.E5 "Equation 4.5 ‣ 4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")). Specifically, the attended inputs Z~\widetilde{Z} are processed by a stack of
feedforward layers of the form ([4.5](https://arxiv.org/html/2601.16274v1#S4.E5 "Equation 4.5 ‣ 4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")), with attention mechanisms used to model complex cross-sectional and temporal interactions.
Implementation details of the Transformer architecture are provided in
Section [5](https://arxiv.org/html/2601.16274v1#S5 "5 Implementation of MPTE with nonlinear signals and mixed frequencies ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").

We use this architecture for representation learning because of its widespread adoption and demonstrated effectiveness in modern large-scale sequence models. In particular, Transformer encoders are the core component of recent state-of-the-art language models trained via instruction tuning and reinforcement learning from human feedback (Ouyang et al., [2022](https://arxiv.org/html/2601.16274v1#bib.bib55 "Training language models to follow instructions with human feedback")). We provide the details on the Transformer and implementation nuances in Section [5](https://arxiv.org/html/2601.16274v1#S5 "5 Implementation of MPTE with nonlinear signals and mixed frequencies ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").

The architecture described above enables us to construct a nonlinear factor extractor in which attention captures adaptive contextual dependencies and the feedforward stack captures complex hierarchical interactions. We do not develop a full inferential theory for the nonlinear encoder, as the analysis of deep nonlinear architectures remains challenging. Instead, our contribution is to show that the proposed nonlinear model is a direct generalization of the attention-weighted linear factor model studied in
Sections [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") and [3](https://arxiv.org/html/2601.16274v1#S3 "3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), sharing the same inputs, latent dimension, and reconstruction-based objective.

Inputs and attention-weighted panel
X∈ℝTx×Nx,Y∈ℝTy×NyX\in\mathbb{R}^{T\_{x}\times N\_{x}},\quad Y\in\mathbb{R}^{T\_{y}\times N\_{y}}
Attention weighting via temporal matrix BB and cross-sectional matrix AzA\_{z}
Z~=B​[X​Y]​Az\widetilde{Z}=B[X\ \ Y]A\_{z}

Same representation-learning problem
only the encoding map ℰθ\mathcal{E}\_{\theta} changes via g​(⋅)g(\cdot)

Linear encoder (theory)
Affine encoding map ℰθ:ℝNx+Ny→ℝk\mathcal{E}\_{\theta}:\mathbb{R}^{N\_{x}+N\_{y}}\to\mathbb{R}^{k}
ℰθ​(Z~t)=b(0)+W(0)​Z~t\mathcal{E}\_{\theta}(\widetilde{Z}\_{t})=b^{(0)}+W^{(0)}\widetilde{Z}\_{t},
g​(x)=xg(x)=x, single layer (M=1M=1)
Equivalent (up to rotation) to attention-weighted PCA / SVD

Nonlinear encoder (implementation)
Nonlinear encoding map ℰθ:ℝNx+Ny→ℝk\mathcal{E}\_{\theta}:\mathbb{R}^{N\_{x}+N\_{y}}\to\mathbb{R}^{k}
Layer recursion (Eq. ([4.5](https://arxiv.org/html/2601.16274v1#S4.E5 "Equation 4.5 ‣ 4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"))), m=1,…,Mm=1,\ldots,M:
Z~(m)=g​(b(m−1)+W(m−1)​Z~(m−1)),Z~(0)=Z~t\displaystyle\widetilde{Z}^{(m)}=g\!\left(b^{(m-1)}+W^{(m-1)}\widetilde{Z}^{(m-1)}\right),\qquad\widetilde{Z}^{(0)}=\widetilde{Z}\_{t}
ℰθ​(Z~t)≡Z~(M)∈ℝk\mathcal{E}\_{\theta}(\widetilde{Z}\_{t})\equiv\widetilde{Z}^{(M)}\in\mathbb{R}^{k}
e.g., Transformer-based parameterization of g​(⋅)g(\cdot)




Learned representation (embedding)
ℰθ​(Z~t)∈ℝk\mathcal{E}\_{\theta}(\widetilde{Z}\_{t})\in\mathbb{R}^{k}


Figure 1: Schematic unifying linear and nonlinear signal extraction.
Both specifications operate on the attended panel Z~=B​[X​Y]​Az\widetilde{Z}=B[X\ \ Y]A\_{z}.
The object of interest is the kk-dimensional embedding ℰθ​(Z~t)\mathcal{E}\_{\theta}(\widetilde{Z}\_{t}):
in the linear case ℰθ\mathcal{E}\_{\theta} is affine (PCA/SVD up to rotation), while in the
nonlinear case ℰθ\mathcal{E}\_{\theta} is defined by compositions of g​(⋅)g(\cdot) as in ([4.5](https://arxiv.org/html/2601.16274v1#S4.E5 "Equation 4.5 ‣ 4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")).

## 5 Implementation of MPTE with nonlinear signals and mixed frequencies

In this section, we describe how we implement MPTE in finite samples for the simulation and empirical analyses. Our goal is to implement the estimator introduced in Sections [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")–[4](https://arxiv.org/html/2601.16274v1#S4 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), while fixing the data preprocessing and input normalization conventions used throughout the remainder of the paper. The implementation nests the linear MPTE studied in the theoretical sections and extends it to nonlinear signal extraction and mixed-frequency datasets without requiring resampling or frequency-specific preprocessing.

An assumption imposed in Sections [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")–[3](https://arxiv.org/html/2601.16274v1#S3 "3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") is that Tx=Ty=TT\_{x}=T\_{y}=T, which is convenient for the theoretical analysis as it allows the panels to be concatenated as Z=[XY]Z=[X\quad Y] and standard matrix operations to be applied. This assumption is, however, restrictive in empirical applications, particularly in mixed-frequency forecasting settings where auxiliary variables are observed at higher frequencies than the target. Traditional approaches, such as MIDAS, address this issue through manual alignment or aggregation across frequencies, which may entail information loss.

In the empirical setting, we relax the restriction Tx=TyT\_{x}=T\_{y} by embedding both the target and auxiliary datasets into a unified sequence representation indexed by calendar time. This representation allows the model to aggregate information across frequencies via attention, without resampling or pre-specified aggregation weights. While the formal theoretical guarantees developed in Sections [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")–[3](https://arxiv.org/html/2601.16274v1#S3 "3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") do not extend to the mixed-frequency setting, the resulting estimator remains well defined and can be implemented straightforwardly in finite samples.

### 5.1 Sequence representation for mixed frequencies with embeddings

We represent the observations from the target panel YY and the auxiliary panel XX as a single ordered sequence indexed by calendar time. Each sequence entry corresponds to a single observed variable at a given time point and may originate from either of the two datasets. This representation allows variables sampled at heterogeneous frequencies to be embedded in a unified temporal structure, while preserving their original observation times.

Let {(vℓ,tℓ)}ℓ=1L\{(v\_{\ell},t\_{\ell})\}\_{\ell=1}^{L} denote the ordered sequence of observed variable–time pairs, where ℓ\ell indexes the position of the observation in the sequence, vℓ∈{1,…,Nx+Ny}v\_{\ell}\in\{1,\ldots,N\_{x}+N\_{y}\} is the variable identifier associated with position ℓ\ell, tℓt\_{\ell} is the calendar timestamp associated with the observation at position ℓ\ell, and LL is the total number of sequence entries. The sequence is ordered so that t1≤⋯≤tLt\_{1}\leq\cdots\leq t\_{L}, but observations may originate from different sampling frequencies, and multiple variables may appear at the same timestamp. The ordering among observations sharing the same time index is arbitrary but fixed.

For each sequence entry ℓ\ell, let rvℓ,tℓr\_{v\_{\ell},t\_{\ell}} denote the raw observed value for the variable vℓv\_{\ell} at time tℓt\_{\ell}. We standardize all raw numerical variables using sample moments computed over the available time observations for each variable,

|  |  |  |  |
| --- | --- | --- | --- |
|  | rvℓ,tℓ∗≡rvℓ,tℓ−μvℓσvℓ,r\_{v\_{\ell},t\_{\ell}}^{\*}\;\equiv\;\frac{r\_{v\_{\ell},t\_{\ell}}-\mu\_{v\_{\ell}}}{\sigma\_{v\_{\ell}}}, |  | (5.1) |

where μvℓ\mu\_{v\_{\ell}} and σvℓ\sigma\_{v\_{\ell}} are the sample mean and standard deviation of variable vℓv\_{\ell}. In the simulation and empirical analyses, we compute these normalization statistics using only the in-sample portion of the data and apply them unchanged to the out-of-sample period, in order to avoid information leakage. This standardization step ensures comparability across series and prevents scale differences from dominating the attention mechanism. Standardizing inputs is a common practice when training neural network–based models, as it improves numerical stability and optimization behavior (Goodfellow et al., [2016](https://arxiv.org/html/2601.16274v1#bib.bib48 "Deep learning")).

We then map each standardized observation into a sequence-level input representation that jointly encodes its numerical value, variable identity, and sampling frequency. Specifically, define the embedding map

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(rvℓ,tℓ∗,vℓ,fℓ)≡[rvℓ,tℓ∗evℓ(var)efℓ(freq)]∈ℝdin,\phi(r\_{v\_{\ell},t\_{\ell}}^{\*},v\_{\ell},f\_{\ell})\;\equiv\;\begin{bmatrix}r\_{v\_{\ell},t\_{\ell}}^{\*}\\ e^{(\mathrm{var})}\_{v\_{\ell}}\\ e^{(\mathrm{freq})}\_{f\_{\ell}}\end{bmatrix}\;\in\;\mathbb{R}^{d\_{\mathrm{in}}}, |  | (5.2) |

where evℓ(var)e^{(\mathrm{var})}\_{v\_{\ell}} is a learned embedding associated with variable vℓv\_{\ell},
efℓ(freq)e^{(\mathrm{freq})}\_{f\_{\ell}} is a learned embedding associated with the sampling frequency fℓf\_{\ell}, fℓf\_{\ell} denotes the sampling frequency associated with observation ℓ\ell (e.g., monthly or quarterly),
with evℓ(var)∈ℝdvare^{(\mathrm{var})}\_{v\_{\ell}}\in\mathbb{R}^{d\_{\mathrm{var}}} and
efℓ(freq)∈ℝdfreqe^{(\mathrm{freq})}\_{f\_{\ell}}\in\mathbb{R}^{d\_{\mathrm{freq}}}, so that
din=1+dvar+dfreqd\_{\mathrm{in}}=1+d\_{\mathrm{var}}+d\_{\mathrm{freq}}. We obtain the embeddings ev(var)e^{(\mathrm{var})}\_{v} and ef(freq)e^{(\mathrm{freq})}\_{f} from learnable embedding tables, and we update those parameters jointly with all other MPTE parameters during training. Conceptually, these embeddings act as learned, low-dimensional parameter vectors associated with categorical identifiers, analogous to variable-specific latent characteristics and frequency-specific effects. In the data matrix passed to the encoder, each ϕ​(rvℓ,tℓ∗,vℓ,fℓ)\phi(r\_{v\_{\ell},t\_{\ell}}^{\*},v\_{\ell},f\_{\ell}) corresponds to one row, and stacking these rows yields the input sequence.

As a further step, we project the concatenated representation into the model dimension before applying attention. This projection learns a joint representation of the standardized value, variable identity, and sampling frequency, and allows the attention mechanism described in Section [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") to operate on latent features rather than on raw inputs. Following standard Transformer architectures (Vaswani et al., [2017](https://arxiv.org/html/2601.16274v1#bib.bib23 "Attention is all you need")), we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | hℓ=Wproj​ϕ​(rvℓ,tℓ∗,vℓ,fℓ),Wproj∈ℝdmodel×din,h\_{\ell}\;=\;W\_{\mathrm{proj}}\,\phi(r\_{v\_{\ell},t\_{\ell}}^{\*},v\_{\ell},f\_{\ell}),\qquad W\_{\mathrm{proj}}\in\mathbb{R}^{d\_{\mathrm{model}}\times d\_{\mathrm{in}}}, |  | (5.3) |

where dind\_{\mathrm{in}} denotes the dimension of the concatenated representation ϕ​(⋅)\phi(\cdot), dmodeld\_{\mathrm{model}} is the fixed internal dimension of the Transformer encoder that forms part of the MPTE specification, and the projection matrix WprojW\_{\mathrm{proj}} is estimated jointly with all other encoder parameters.

Although the sequence entries are ordered by their calendar timestamps, MPTE has no intrinsic notion of temporal ordering without an explicit encoding. We therefore explicitly incorporate temporal information through a temporal encoding. Specifically, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | zℓ=hℓ+TE​(tℓ),z\_{\ell}\;=\;h\_{\ell}+\mathrm{TE}(t\_{\ell}), |  | (5.4) |

where tℓt\_{\ell} denotes a numerical time index obtained from the corresponding calendar timestamp. Here TE​(tℓ)∈ℝdmodel\mathrm{TE}(t\_{\ell})\in\mathbb{R}^{d\_{\mathrm{model}}} is a deterministic sinusoidal temporal encoding defined componentwise as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | TE2​j​(tℓ)\displaystyle\mathrm{TE}\_{2j}(t\_{\ell}) | =sin⁡(tℓ100002​j/dmodel),\displaystyle=\sin\!\left(\frac{t\_{\ell}}{10000^{2j/d\_{\mathrm{model}}}}\right), |  | (5.5) |
|  | TE2​j+1​(tℓ)\displaystyle\mathrm{TE}\_{2j+1}(t\_{\ell}) | =cos⁡(tℓ100002​j/dmodel),j=0,1,…,⌊dmodel2⌋−1,\displaystyle=\cos\!\left(\frac{t\_{\ell}}{10000^{2j/d\_{\mathrm{model}}}}\right),\qquad j=0,1,\ldots,\Big\lfloor\tfrac{d\_{\mathrm{model}}}{2}\Big\rfloor-1, |  |

as in Vaswani et al. ([2017](https://arxiv.org/html/2601.16274v1#bib.bib23 "Attention is all you need")). We add the temporal encoding rather than concatenating it so that time enters the representation as a time index governing relative relationships across sequence entries, rather than as an additional observed feature.

Stacking the sequence entries yields the encoder input matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z≡(z1,…,zL)⊤∈ℝL×dmodel.Z\;\equiv\;(z\_{1},\ldots,z\_{L})^{\top}\in\mathbb{R}^{L\times d\_{\mathrm{model}}}. |  | (5.6) |

This sequence-based representation replaces, at the implementation level, the wide stacked panel [XY][X\quad Y] used in the theoretical analysis with a corresponding ordered collection of observations that is amenable to attention-based aggregation when sampling frequencies differ.

(a) Theory: wide concatenated panel (assumes Tx=Ty=TT\_{x}=T\_{y}=T)X∈ℝT×NxX\in\mathbb{R}^{T\times N\_{x}}Y∈ℝT×NyY\in\mathbb{R}^{T\times N\_{y}}t=1,…,Tt=1,\ldots,TZ=[X​Y]∈ℝT×(Nx+Ny)Z=[X\ \ Y]\in\mathbb{R}^{T\times(N\_{x}+N\_{y})}Z~=B​[X​Y]​Az\widetilde{Z}=B[X\ \ Y]A\_{z}   (linear attention operators)

Key distinction. Theory stacks across variables at a common time index (wide panel),
whereas implementation stacks observed variable–time pairs into an ordered sequence (long format),
enabling mixed-frequency inputs without resampling.

(b) Implementation: long sequence for mixed frequencies (Tx≠TyT\_{x}\neq T\_{y})ℓ\elltℓt\_{\ell}vℓv\_{\ell}fℓf\_{\ell}rvℓ,tℓ∗r^{\*}\_{v\_{\ell},t\_{\ell}}11Q1Q\_{1}GDPQrGDP,Q1∗r^{\*}\_{\text{GDP},Q\_{1}}22M1M\_{1}CPIMrCPI,M1∗r^{\*}\_{\text{CPI},M\_{1}}⋮\vdots⋮\vdots⋮\vdots⋮\vdots⋮\vdotsLLMTM\_{T}PAYEMSMrPAYEMS,MT∗r^{\*}\_{\text{PAYEMS},M\_{T}}rvℓ,tℓ∗r^{\*}\_{v\_{\ell},t\_{\ell}}ϕ​(rvℓ,tℓ∗,vℓ,fℓ)\phi(r^{\*}\_{v\_{\ell},t\_{\ell}},v\_{\ell},f\_{\ell})hℓ=Wproj​ϕ​(⋅)h\_{\ell}=W\_{\mathrm{proj}}\phi(\cdot)zℓ=hℓ+TE​(tℓ)z\_{\ell}=h\_{\ell}+\mathrm{TE}(t\_{\ell})ϕ​(⋅)\phi(\cdot)WprojW\_{\mathrm{proj}}+TE​(tℓ)+\mathrm{TE}(t\_{\ell})Z=(z1,…,zL)⊤∈ℝL×dmodelZ=(z\_{1},\ldots,z\_{L})^{\top}\in\mathbb{R}^{L\times d\_{\mathrm{model}}}Z~att=𝒜θA​(Z)\widetilde{Z}^{\mathrm{att}}\;=\;\mathcal{A}\_{\theta\_{A}}(Z)   (data-dependent attention operator)


Figure 2: Wide-panel representation used in the theoretical analysis versus long sequence
representation used in implementation for mixed-frequency data.
Panel (a) assumes Tx=Ty=TT\_{x}=T\_{y}=T and forms Z=[X​Y]Z=[X\ \ Y].
Panel (b) constructs an ordered sequence of observed variable–time pairs
{(vℓ,tℓ)}ℓ=1L\{(v\_{\ell},t\_{\ell})\}\_{\ell=1}^{L}, embeds each entry, and stacks the resulting tokens
into Z∈ℝL×dmodelZ\in\mathbb{R}^{L\times d\_{\mathrm{model}}} for attention-based aggregation.

### 5.2 Attention-based nonlinear aggregation and prediction

Starting from the embedded sequence ZZ, we pass it through a Transformer encoder following the standard architecture of Vaswani et al. ([2017](https://arxiv.org/html/2601.16274v1#bib.bib23 "Attention is all you need")). The Transformer encoder can consist of a stack of identical encoder layers, each applying an attention operation followed by a feedforward transformation. In the simplest case, the encoder contains a single layer.

Within each encoder layer, we apply the attention mechanism to the input sequence to produce an attended representation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~att=𝒜θA​(Z),\widetilde{Z}^{\mathrm{att}}\;=\;\mathcal{A}\_{\theta\_{A}}(Z), |  | (5.7) |

where 𝒜θA​(⋅)\mathcal{A}\_{\theta\_{A}}(\cdot) denotes a data-dependent attention operator parameterized by learnable weight matrices. These parameters correspond to the linear transformations defining queries, keys, and values, as described in Section [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"). This operation is the nonlinear analogue of the attention-based reweighting studied in the theoretical analysis and induces both temporal and cross-sectional aggregation across sequence entries. Figure [2](https://arxiv.org/html/2601.16274v1#S5.F2 "Figure 2 ‣ 5.1 Sequence representation for mixed frequencies with embeddings ‣ 5 Implementation of MPTE with nonlinear signals and mixed frequencies ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") illustrates the distinction between the wide-panel representation used in the theoretical analysis and the long-sequence
representation used in implementation.
The former relies on a common time index to concatenate panels horizontally, while the latter organizes mixed-frequency observations as an ordered sequence of variable–time tokens that are embedded and processed via attention.

We then pass the attended representation Z~att\widetilde{Z}^{\mathrm{att}} through a feedforward transformation with elementwise nonlinear activation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z~(m)=g​(b(m−1)+W(m−1)​Z~att),\widetilde{Z}^{(m)}=g\!\left(b^{(m-1)}+W^{(m-1)}\widetilde{Z}^{\mathrm{att}}\right), |  | (5.8) |

which corresponds to the layerwise transformation in ([4.5](https://arxiv.org/html/2601.16274v1#S4.E5 "Equation 4.5 ‣ 4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")).
Stacking multiple encoder layers iterates this attention–nonlinearity
composition and yields a nonlinear encoding map
ℰθ​(⋅)\mathcal{E}\_{\theta}(\cdot) as defined in Section [4](https://arxiv.org/html/2601.16274v1#S4 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
The final encoder output
ℰθ​(Z)=Z~(M)\mathcal{E}\_{\theta}(Z)=\widetilde{Z}^{(M)}
provides a low-dimensional representation that captures higher-order and
context-dependent interactions across variables, sampling frequencies, and
time.

In the theoretical analysis, we decomposed attention into separate temporal (BB) and cross-sectional (AzA\_{z}) operators to clarify identification and asymptotic properties. However, in the implementation, these effects are learned jointly within MPTE through a single data-dependent attention mechanism 𝒜θA​(⋅)\mathcal{A}\_{\theta\_{A}}(\cdot) operating on the ordered sequence ZZ. The resulting attention weights endogenously determine how information is reweighted across time and across variables.

When the nonlinear activation g​(⋅)g(\cdot) is replaced by the identity function, the encoding map ℰθ\mathcal{E}\_{\theta} reduces to the linear MPTE estimator analyzed in Sections [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")–[3](https://arxiv.org/html/2601.16274v1#S3 "3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), and representation extraction coincides, up to rotation, with PCA estimation on attention-weighted inputs.
More generally, the encoder implements a nonlinear factor extractor that
preserves the estimator architecture underlying the linear theory while allowing for context-dependent signal construction. Depending on how the encoded representation ℰθ\mathcal{E}\_{\theta} is used downstream, the same framework can be applied to regression, classification, or related prediction tasks.

For the purposes of this paper, and in order to illustrate how mixed-frequency information can enhance forecasting performance, we focus on a regression setting. In the simulation and empirical analyses, we construct forecasts by applying a linear mapping to the encoder output ℰθ​(Z)\mathcal{E}\_{\theta}(Z), producing continuous-valued predictions for the target variables at the desired forecast horizons. We train MPTE by jointly estimating all model parameters, including the variable- and frequency-embedding tables, the projection layer, the Transformer encoder parameters, and the prediction head, using gradient-based optimization.

We select architectural and training hyperparameters for both the simulation and empirical exercises using Bayesian optimization, and we document the corresponding optimization procedures and selected values in Appendix [C](https://arxiv.org/html/2601.16274v1#A3 "Appendix C Hyperparameter selection ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").

###### Remark 2.

The implementation described in this section is designed to mirror the encoder structure analyzed in Sections [2](https://arxiv.org/html/2601.16274v1#S2 "2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") and
[3](https://arxiv.org/html/2601.16274v1#S3 "3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), while allowing for substantially greater
flexibility in practice.
In the theoretical analysis, attention is modeled through deterministic temporal and cross-sectional operators (B,Az)(B,A\_{z}), yielding an attention-transformed panel
Z~=B​[X​Y]​Az\widetilde{Z}=B[X\ Y]A\_{z} on which linear factor extraction is performed. This formulation isolates the role of information reweighting and permits a precise characterization of identification and asymptotic behavior.

In the implementation, the same conceptual operations are carried out using a data-dependent attention mechanism 𝒜θA​(⋅)\mathcal{A}\_{\theta\_{A}}(\cdot) acting on an embedded sequence representation.
The resulting attended sequence
Z~att=𝒜θA​(Z)\widetilde{Z}^{\mathrm{att}}=\mathcal{A}\_{\theta\_{A}}(Z)
plays a role analogous to Z~\widetilde{Z} in the theoretical model, but is generated via learned, nonlinear aggregation rather than fixed linear operators.
Subsequent feedforward layers parameterize the nonlinear encoding map
ℰθ\mathcal{E}\_{\theta} introduced in Section [4](https://arxiv.org/html/2601.16274v1#S4 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), thereby generalizing linear factor extraction.

When the activation function is linear, the encoding map ℰθ\mathcal{E}\_{\theta} reduces to the linear MPTE estimator analyzed in the theoretical sections. In this case, attention-based aggregation followed by linear extraction coincides, up to rotation, with principal component estimation on attention-weighted inputs, and
the theoretical results apply directly. The nonlinear specification can therefore be interpreted as a flexible extension
that preserves the estimator architecture underlying the theory, while expanding the class of admissible encoding maps.

## 6 Simulation evidence on attention-based mixed-frequency estimation

To assess the finite-sample performance of MPTE under controlled forms of nonlinearity and mixed-frequency information, we consider a data-generating process (DGP) inspired by Lin and Michailidis ([2024](https://arxiv.org/html/2601.16274v1#bib.bib4 "A multi-task encoder-dual-decoder framework for mixed frequency data prediction")). We model the dynamics of the latent factors using a linear VAR(2) process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft=Φ1​Ft−1+Φ2​Ft−2+εt,εt∼𝒩​(0,ΣF),Ft∈ℝq.F\_{t}=\Phi\_{1}F\_{t-1}+\Phi\_{2}F\_{t-2}+\varepsilon\_{t},\qquad\varepsilon\_{t}\sim\mathcal{N}(0,\,\Sigma\_{F}),\quad F\_{t}\in\mathbb{R}^{q}. |  | (6.1) |

The latent factor process {Ft}\{F\_{t}\} is generated at the high frequency. Each low-frequency index t′t^{\prime} is associated with the high-frequency time t=r​t′t=rt^{\prime}, corresponding to the end of the t′t^{\prime}-th low-frequency period,
where rr denotes the ratio between the high- and low-frequency sampling
intervals (e.g. r=3r=3 for monthly and quarterly frequencies). We rescale the coefficient matrices (Φ1,Φ2)(\Phi\_{1},\Phi\_{2}) to ensure stability of the latent VAR(2) process, with the spectral radius of the associated companion matrix bounded away from unity. We set the innovation covariance to ΣF=0.5​Iq\Sigma\_{F}=0.5\,I\_{q} and discard an initial burn-in period.

Conditional on the latent factor process {Ft}\{F\_{t}\}, we generate two panels of observables at different sampling frequencies, namely a high-frequency panel {Xt}\{X\_{t}\} following a VAR(LxL\_{x}) model indexed by tt, and a low-frequency panel {Yt′}\{Y\_{t^{\prime}}\} following a VAR(LyL\_{y}) model indexed by t′t^{\prime}:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Xt\displaystyle X\_{t} | =∑ℓ=1LxAℓ​Xt−ℓ+∑j=0qf​xΛx,j​g​(Ft−j)+ηt,\displaystyle=\sum\_{\ell=1}^{L\_{x}}A\_{\ell}X\_{t-\ell}+\sum\_{j=0}^{q\_{fx}}\Lambda\_{x,j}\,g(F\_{t-j})+\eta\_{t}, |  | ηt∼tν​(0,ΣX),Xt∈ℝNx\displaystyle\eta\_{t}\sim t\_{\nu}(0,\,\Sigma\_{X}),\ X\_{t}\in\mathbb{R}^{N\_{x}} |  | (6.2) |
|  | Yt′\displaystyle Y\_{t^{\prime}} | =∑ℓ=1LyCℓ​Yt′−ℓ+∑j=0qf​yΛy,j​g​(Fr​t′−j)+ξt′,\displaystyle=\sum\_{\ell=1}^{L\_{y}}C\_{\ell}Y\_{t^{\prime}-\ell}+\sum\_{j=0}^{q\_{fy}}\Lambda\_{y,j}\,g(F\_{rt^{\prime}-j})+\xi\_{t^{\prime}}, |  | ξt′∼𝒩​(0,ΣY),Yt′∈ℝNy.\displaystyle\xi\_{t^{\prime}}\sim\mathcal{N}(0,\,\Sigma\_{Y}),\ Y\_{t^{\prime}}\in\mathbb{R}^{N\_{y}}. |  |

We rescale the autoregressive coefficient matrices {Aℓ}ℓ=1Lx\{A\_{\ell}\}\_{\ell=1}^{L\_{x}} and {Cℓ}ℓ=1Ly\{C\_{\ell}\}\_{\ell=1}^{L\_{y}} so that the spectral radius of the associated companion matrices does not exceed pre-specified block-specific thresholds, allowing for different degrees of persistence across high- and low-frequency variables. We generate the factor loading matrices Λx,j\Lambda\_{x,j} and Λy,j\Lambda\_{y,j} using Almon polynomial lag weights to induce decaying factor effects across lags smoothly. We also scale the noise variances to ensure comparable signal-to-noise ratios across simulation designs.

To control the degree of nonlinearity in the factor–observable relationship, we specify the latent transformation g​(⋅)g(\cdot) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(Ft)={Ft,linear case,(exp⁡(−γ​∥Ft−ck∥2)σk)k=1K,nonlinear case,g(F\_{t})=\begin{cases}F\_{t},&\text{linear case},\\[3.99994pt] \left(\dfrac{\exp\!\big(-\gamma\lVert F\_{t}-c\_{k}\rVert^{2}\big)}{\sigma\_{k}}\right)\_{k=1}^{K},&\text{nonlinear case},\end{cases} |  | (6.3) |

where ∥⋅∥\lVert\cdot\rVert denotes the Euclidean norm, and σk\sigma\_{k} denotes the sample standard deviation of the kk-th RBF component computed over time, so that each RBF feature is standardized to have unit variance. The centers {ck}k=1K⊂ℝq\{c\_{k}\}\_{k=1}^{K}\subset\mathbb{R}^{q} of the radial basis function (RBF) are drawn i.i.d. from 𝒩​(0,Iq)\mathcal{N}(0,I\_{q}), and the bandwidth parameter γ\gamma is set using a median-distance heuristic based on the centers.

We consider three simulation regimes. In the linear design, we set g​(⋅)g(\cdot) equal to the identity map. In the nonlinear designs, we use the RBF specification in ([6.3](https://arxiv.org/html/2601.16274v1#S6.E3 "Equation 6.3 ‣ 6 Simulation evidence on attention-based mixed-frequency estimation ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) and vary the number of basis functions KK to control the degree of nonlinearity. Specifically, we set K=6K=6 in the mildly nonlinear case and K=12K=12 in the highly nonlinear case, where KK denotes both the number of RBF centers and the resulting number of basis functions, holding all other aspects of the DGP fixed across regimes.

Across all simulation regimes, we generate 5,000 high-frequency observations, using the first 4,000 after burn-in for training, with 10% of the sample reserved for validation and the remaining 1,000 for out-of-sample evaluation. We report results for the first low-frequency target series Y1Y\_{1}. Since all low-frequency variables are generated from the same DGP and differ only through their factor loadings and idiosyncratic shocks, forecasting other targets yields qualitatively similar results333The implementation used for the simulation exercises in this section, as well as for the empirical analysis in the next section, is based on a unified codebase available at <https://github.com/Alessiobrini/mixed-panels-transformer-encoder>..

We compare the performance of MPTE against two benchmark models: (i) a univariate autoregressive model (AR), for which we select the order using the Bayesian Information Criterion (BIC), and (ii) an unrestricted linear MIDAS specification in which high-frequency predictors enter through unrestricted distributed lags, without nonlinear transformations or parametric lag-weighting functions. In addition, we evaluate the following ablation variants of MPTE to isolate the contribution of individual architectural components:

* •

  AB1: Absence of nonlinear transformations in the Transformer encoder architecture (feedforward layers without activation functions).
* •

  AB2: Absence of the attention mechanism, with the encoder architecture reducing to a stack of feedforward layers.
* •

  AB3: Absence of both nonlinear transformations and the attention mechanism.
* •

  AB4: Absence of temporal encoding.
* •

  AB5: Low-frequency block only, excluding high-frequency inputs.

We report forecasting performance using root mean squared error (RMSE), mean absolute error (MAE), and directional accuracy (DA), defined as the fraction of periods in which the predicted and actual values of the target series share the same sign. We train all MPTE specifications and ablation variants using automated hyperparameter optimization. We report the full details on the optimization procedure and search spaces used in the simulation experiments in Appendix [C](https://arxiv.org/html/2601.16274v1#A3 "Appendix C Hyperparameter selection ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").

Table [1](https://arxiv.org/html/2601.16274v1#S6.T1 "Table 1 ‣ 6 Simulation evidence on attention-based mixed-frequency estimation ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") summarizes forecasting performance across linear, mildly nonlinear, and highly nonlinear designs. In the linear setting, MPTE does not outperform MIDAS and yields comparable or slightly inferior accuracy, which is expected since MIDAS is itself a linear model and is well suited for learning purely linear relationships without introducing unnecessary model complexity. In contrast, MPTE delivers clear gains over both MIDAS and AR in the mildly and highly nonlinear designs. These results underscore the benefits of combining nonlinear signal extraction with mixed-frequency information.

The ablation results provide additional insight into the role of individual architectural components. Removing nonlinear transformations (AB1) deteriorates performance in the nonlinear designs but has limited impact in the linear case, confirming that nonlinear feature construction is beneficial primarily when warranted by the underlying DGP. Similarly, disabling attention (AB2) or both attention and nonlinearity (AB3) leads to notable performance losses in the nonlinear settings, indicating that attention-based aggregation plays a key role in selectively combining information across time and variables when signals are nonlinear. In the linear design, however, attention does not systematically improve performance and may even introduce mild overfitting, consistent with the fact that linear dynamics can be adequately captured by simpler aggregation schemes.

Temporal encoding also proves important across all designs. The absence of temporal encoding (AB4) leads to inferior performance in both linear and nonlinear settings, underscoring the importance of explicitly encoding temporal order when applying Transformer-based models to sequential data. Finally, restricting the model to low-frequency information only (AB5) results in higher forecast errors relative to the full MPTE specification, reflecting the efficiency gains from incorporating high-frequency predictors that share common latent factors with the target series. This finding mirrors empirical macroeconomic settings in which monthly indicators provide valuable information for forecasting quarterly aggregates through shared underlying economic drivers.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Linear | | | Mildly Nonlinear | | | Highly Nonlinear | | |
|  | RMSE | MAE | DA | RMSE | MAE | DA | RMSE | MAE | DA |
| MPTE | 1.2990 | 1.0231 | 0.6355 | \cellcolorbestgreen1.3995 | \cellcolorbestgreen1.1134 | \cellcolorbestgreen0.6777 | \cellcolorbestgreen1.1579 | \cellcolorbestgreen0.9345 | \cellcolorsecondgreen0.5964 |
| AR | 1.3832 | 1.0930 | 0.3283 | 1.7798 | 1.4361 | 0.1235 | 1.2906 | 1.0234 | 0.0301 |
| MIDAS | \cellcolorbestgreen1.2631 | \cellcolorbestgreen0.9733 | \cellcolorbestgreen0.6807 | 1.5162 | 1.2112 | 0.6355 | 1.2857 | 1.0527 | 0.5873 |
| AB1 | 1.2872 | 1.0099 | 0.6476 | \cellcolorsecondgreen1.4063 | \cellcolorsecondgreen1.1268 | \cellcolorsecondgreen0.6657 | 1.2157 | 0.9773 | 0.5392 |
| AB2 | 1.2967 | 1.0312 | 0.6506 | 1.4261 | 1.1472 | 0.6596 | 1.3084 | 1.0407 | 0.5090 |
| AB3 | \cellcolorsecondgreen1.2679 | \cellcolorsecondgreen0.9933 | \cellcolorsecondgreen0.6747 | 1.4365 | 1.1422 | 0.6566 | \cellcolorsecondgreen1.1965 | \cellcolorsecondgreen0.9606 | 0.5693 |
| AB4 | 1.3634 | 1.0707 | 0.6687 | 1.7394 | 1.4103 | 0.5843 | 1.3066 | 1.0413 | 0.5693 |
| AB5 | 1.3488 | 1.0415 | 0.6596 | 1.4149 | 1.1414 | 0.6536 | 1.2018 | 0.9706 | \cellcolorbestgreen0.5994 |

Table 1: Forecasting accuracy for the first low-frequency target series Y1Y\_{1} across linear, mildly nonlinear, and highly nonlinear simulation designs. Each design includes 30 high-frequency regressors and 5 low-frequency targets, with Y1Y\_{1} predicted using the remaining regressors. Results are reported for MPTE, AR, MIDAS, and ablation variants of MPTE. Dark green indicates the best-performing method and light green
the second-best within each column.

## 7 Empirical evidence from U.S. macroeconomic data

To evaluate the empirical performance of MPTE in a realistic mixed-frequency forecasting environment, we apply the model to a large quarterly–monthly macroeconomic dataset. Mixed-frequency structures arise naturally in macroeconomic applications, where key aggregates are observed at low frequency while a broad set of indicators is available at higher frequency. We therefore consider the macroeconomic database of McCracken and Ng ([2016](https://arxiv.org/html/2601.16274v1#bib.bib26 "FRED-MD: a monthly database for macroeconomic research")) (FRED-QD and FRED-MD), which provides a comprehensive panel of U.S. macroeconomic time series at quarterly and monthly frequencies.

We study the period from 1959:Q1 to 2025:Q1, corresponding to 1959:M1–2025:M3, using the current vintage as of 2025:M3. From this database, we select thirteen quarterly variables as forecast targets: GDPC1, GPDIC1, PCECC96, DPIC96, OUTNFB, UNRATE, PCECTPI, PCEPILFE, CPIAUCSL, CPILFESL, FPIx, EXPGSC1, and IMPGSC1. The complete list of monthly and quarterly regressors used in the empirical analysis, together with brief descriptions and their category, is reported in Appendix [D](https://arxiv.org/html/2601.16274v1#A4 "Appendix D List of monthly and quarterly variables ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").

We conduct the forecasting exercise at a quarterly frequency. For each target observation, we construct an input sequence for the model comprising all available monthly and quarterly observations within a fixed two-year context window, ending at the most recent observed quarter preceding the forecasted quarter. This context window defines the information set supplied to MPTE and may include both high- and low-frequency variables, as described in Section [5](https://arxiv.org/html/2601.16274v1#S5 "5 Implementation of MPTE with nonlinear signals and mixed frequencies ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"). The task is to predict the next quarterly realization of the target series. The fixed two-year context window can be viewed as a finite-sample analogue of the temporal operator BB studied in the theoretical analysis, in that it restricts the attention mechanism to operate on a local time neighborhood while allowing the model to learn how to allocate weighs within that neighborhood.

As in the simulation exercises, we split the sample sequentially to preserve the temporal ordering of the data. We use the first 80% of the available observations for model training, and we reserve the final 10% of this training sample for validation. We hold out the remaining 20% of the data for out-of-sample evaluation. As in Section [6](https://arxiv.org/html/2601.16274v1#S6 "6 Simulation evidence on attention-based mixed-frequency estimation ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), we select model hyperparameters using automated optimization conducted separately for each target variable and model specification (see Appendix [C](https://arxiv.org/html/2601.16274v1#A3 "Appendix C Hyperparameter selection ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")).

We compare MPTE with the same benchmark models used in the simulation study, namely a univariate AR model and an unrestricted linear MIDAS specification. In addition, we include other competing models: OLS, eXtreme Gradient Boosting (XGB) (Chen and Guestrin, [2016](https://arxiv.org/html/2601.16274v1#bib.bib49 "XGBoost: a scalable tree boosting system")), and a feedforward neural network (NN). Since OLS, XGB, and NN do not natively support mixed-frequency inputs, we estimate these models using only quarterly predictors. For comparability across models, we aggregate the monthly variables to the quarterly frequency by taking the last value of the quarter, so that all competing models are trained on a common quarterly information set.

Consistent with the simulation analysis, we evaluate forecasting performance using the same metrics as in Section [6](https://arxiv.org/html/2601.16274v1#S6 "6 Simulation evidence on attention-based mixed-frequency estimation ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"): RMSE, MAE, and DA. We construct all subsamples based on forecast timestamps to assess the stability of forecasting performance around the COVID-19 period. The full evaluation period spans from June 2012 to March 2025. We further split this period into a pre-COVID subsample, covering forecasts dated up to June 2019, and a COVID and post-COVID subsample, covering forecasts dated after June 2019. We apply these splits consistently across all models and performance metrics. In addition to point forecast accuracy metrics, we report pairwise forecast comparison tests based on the Diebold–Mariano test, as well as Model Confidence Set (MCS) results in Appendix [B](https://arxiv.org/html/2601.16274v1#A2 "Appendix B Diebold–Mariano tests and Model Confidence Set results ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").

Tables [2](https://arxiv.org/html/2601.16274v1#S7.T2 "Table 2 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") and [3](https://arxiv.org/html/2601.16274v1#S7.T3 "Table 3 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") report out-of-sample forecasting performance at the individual target level, grouped according to whether MPTE achieves the lowest RMSE over the full sample period. Table [2](https://arxiv.org/html/2601.16274v1#S7.T2 "Table 2 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") focuses on target series for which MPTE attains the lowest RMSE, while Table [3](https://arxiv.org/html/2601.16274v1#S7.T3 "Table 3 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") reports results for series where alternative models outperform MPTE. Table [4](https://arxiv.org/html/2601.16274v1#S7.T4 "Table 4 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") provides a complementary summary by counting, for each model, the number of target series for which it delivers the best performance under RMSE, MAE, and DA, across the full sample and the pre- and post-COVID subsamples. The relative counts in Table [4](https://arxiv.org/html/2601.16274v1#S7.T4 "Table 4 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") are sensitive to the set of competing models. In particular, excluding XGB from the comparison increases the number of target series for which MPTE achieves the lowest RMSE, consistent with XGB being a particularly strong benchmark in this empirical setting.Figure [3](https://arxiv.org/html/2601.16274v1#S7.F3 "Figure 3 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") illustrates selected out-of-sample forecasts for GDPC1 and OUTNFB, showing how MPTE and competing models track the realized series over the pre-COVID window and the full evaluation period.

Over the full evaluation period, MPTE exhibits strong RMSE performance. As shown in Table [2](https://arxiv.org/html/2601.16274v1#S7.T2 "Table 2 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), MPTE delivers the lowest RMSE for several real activity and price-related series, including OUTNFB, PCECTPI, PCEPILFE, CPIAUCSL, and GDPC1. The relative RMSE ranking is broadly stable across subsamples, although the magnitude varies between the pre- and post-COVID periods.

Table [3](https://arxiv.org/html/2601.16274v1#S7.T3 "Table 3 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") shows that MPTE does not uniformly outperform competing models across all target series. In particular, for several income and trade-related variables, such as DPIC96, EXPGSC1, FPIx, and IMPGSC1, MIDAS or tree-based methods achieve lower RMSE. These series tend to exhibit relatively smooth quarterly dynamics and limited incremental variation at the monthly frequency, which is consistent with more limited gains from explicitly modeling mixed-frequency interactions.

Differences across models are more nuanced when considering DA. As summarized in Table [4](https://arxiv.org/html/2601.16274v1#S7.T4 "Table 4 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), MIDAS attains the highest DA for a larger number of target series, particularly in the Post-COVID subsample. However, Tables [2](https://arxiv.org/html/2601.16274v1#S7.T2 "Table 2 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") and [3](https://arxiv.org/html/2601.16274v1#S7.T3 "Table 3 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") indicate that DA differences between MIDAS and MPTE are often modest at the series level, even when MIDAS ranks first. This pattern suggests that both approaches capture directional movements reasonably well, with MPTE’s advantages emerging more clearly in level forecast accuracy as measured by RMSE rather than sign prediction.

Finally, comparisons with models that incorporate monthly variables only through their end-of-quarter values, rather than modeling within-quarter dynamics, such as OLS, XGB, and NN, indicate that strong forecasting performance can often be achieved without explicitly modeling mixed-frequency inputs. In particular, XGB performs competitively across several target series and subsamples. At the same time, MPTE remains competitive in terms of RMSE across evaluation periods and achieves superior performance for a subset of targets, suggesting that explicitly incorporating high-frequency information can be beneficial when such signals provide incremental predictive content. Overall, the results indicate that the gains from mixed-frequency modeling are context dependent and vary across target series and data regimes.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Full | | | Pre-COVID | | | Post-COVID | | |
|  | RMSE | MAE | DA | RMSE | MAE | DA | RMSE | MAE | DA |
| OUTNFB |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorbestgreen0.0180 | \cellcolorbestgreen0.0081 | \cellcolorbestgreen0.6000 | \cellcolorbestgreen0.0042 | \cellcolorbestgreen0.0035 | \cellcolorbestgreen0.5714 | \cellcolorbestgreen0.0270 | 0.0142 | \cellcolorbestgreen0.6190 |
| AR | 0.0205 | \cellcolorsecondgreen0.0083 | 0.2800 | \cellcolorsecondgreen0.0049 | \cellcolorsecondgreen0.0038 | 0.5000 | 0.0307 | \cellcolorsecondgreen0.0141 | 0.0000 |
| MIDAS | \cellcolorsecondgreen0.0202 | 0.0114 | \cellcolorsecondgreen0.5600 | 0.0103 | 0.0082 | \cellcolorsecondgreen0.5357 | \cellcolorsecondgreen0.0285 | 0.0157 | \cellcolorsecondgreen0.5714 |
| OLS | 0.1537 | 0.0832 | 0.5400 | 0.0682 | 0.0532 | 0.5000 | 0.2205 | 0.1226 | \cellcolorsecondgreen0.5714 |
| XGB | 0.0191 | \cellcolorbestgreen0.0081 | 0.5200 | 0.0052 | 0.0044 | \cellcolorbestgreen0.5714 | \cellcolorsecondgreen0.0285 | \cellcolorbestgreen0.0130 | 0.4762 |
| NN | 0.0956 | 0.0635 | 0.5000 | 0.0487 | 0.0380 | \cellcolorbestgreen0.5714 | 0.1344 | 0.0970 | 0.3810 |
| PCECTPI |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorsecondgreen0.0039 | \cellcolorsecondgreen0.0030 | 0.6078 | \cellcolorbestgreen0.0030 | \cellcolorbestgreen0.0021 | \cellcolorbestgreen0.7143 | 0.0049 | 0.0040 | 0.4545 |
| AR | \cellcolorbestgreen0.0036 | \cellcolorbestgreen0.0028 | 0.5882 | \cellcolorsecondgreen0.0031 | \cellcolorsecondgreen0.0025 | \cellcolorbestgreen0.7143 | \cellcolorbestgreen0.0041 | \cellcolorbestgreen0.0032 | 0.4545 |
| MIDAS | 0.0040 | \cellcolorsecondgreen0.0030 | \cellcolorbestgreen0.7647 | 0.0032 | 0.0026 | \cellcolorsecondgreen0.6786 | \cellcolorsecondgreen0.0048 | \cellcolorsecondgreen0.0036 | \cellcolorbestgreen0.8636 |
| OLS | 0.0325 | 0.0192 | 0.4902 | 0.0138 | 0.0109 | 0.5357 | 0.0463 | 0.0298 | 0.4091 |
| XGB | 0.0068 | 0.0041 | \cellcolorsecondgreen0.6863 | 0.0042 | 0.0027 | 0.6429 | 0.0091 | 0.0059 | \cellcolorsecondgreen0.7727 |
| NN | 0.1070 | 0.0719 | 0.6471 | 0.0513 | 0.0369 | \cellcolorsecondgreen0.6786 | 0.1501 | 0.1162 | 0.5909 |
| PCEPILFE |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorbestgreen0.0024 | \cellcolorbestgreen0.0016 | 0.5294 | 0.0015 | \cellcolorbestgreen0.0011 | 0.4286 | \cellcolorbestgreen0.0033 | \cellcolorbestgreen0.0023 | \cellcolorbestgreen0.6364 |
| AR | \cellcolorbestgreen0.0024 | \cellcolorsecondgreen0.0018 | 0.2941 | \cellcolorbestgreen0.0013 | \cellcolorsecondgreen0.0012 | 0.4643 | \cellcolorsecondgreen0.0034 | \cellcolorsecondgreen0.0025 | 0.0909 |
| MIDAS | 0.0075 | 0.0034 | \cellcolorbestgreen0.6471 | 0.0020 | 0.0016 | \cellcolorbestgreen0.6786 | 0.0110 | 0.0056 | \cellcolorbestgreen0.6364 |
| OLS | 0.0260 | 0.0146 | 0.5098 | 0.0107 | 0.0086 | \cellcolorsecondgreen0.5714 | 0.0372 | 0.0221 | 0.4545 |
| XGB | \cellcolorsecondgreen0.0025 | \cellcolorsecondgreen0.0018 | \cellcolorsecondgreen0.5490 | \cellcolorsecondgreen0.0014 | \cellcolorbestgreen0.0011 | 0.4643 | \cellcolorsecondgreen0.0034 | \cellcolorsecondgreen0.0025 | \cellcolorbestgreen0.6364 |
| NN | 0.1618 | 0.0991 | \cellcolorsecondgreen0.5490 | 0.0687 | 0.0540 | 0.5357 | 0.2307 | 0.1561 | \cellcolorsecondgreen0.5455 |
| CPIAUCSL |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorbestgreen0.0054 | \cellcolorsecondgreen0.0043 | 0.6275 | 0.0052 | 0.0041 | \cellcolorsecondgreen0.6786 | \cellcolorbestgreen0.0058 | \cellcolorbestgreen0.0044 | \cellcolorsecondgreen0.5455 |
| AR | \cellcolorbestgreen0.0054 | \cellcolorbestgreen0.0039 | 0.5686 | \cellcolorbestgreen0.0043 | \cellcolorbestgreen0.0034 | 0.6429 | \cellcolorsecondgreen0.0065 | \cellcolorsecondgreen0.0045 | 0.5000 |
| MIDAS | \cellcolorsecondgreen0.0062 | 0.0048 | \cellcolorsecondgreen0.7059 | \cellcolorsecondgreen0.0050 | \cellcolorsecondgreen0.0037 | 0.6429 | 0.0075 | 0.0061 | \cellcolorbestgreen0.7727 |
| OLS | 0.0379 | 0.0220 | 0.5686 | 0.0156 | 0.0135 | 0.5714 | 0.0543 | 0.0326 | \cellcolorsecondgreen0.5455 |
| XGB | 0.0117 | 0.0064 | \cellcolorbestgreen0.7647 | 0.0068 | \cellcolorsecondgreen0.0037 | \cellcolorbestgreen0.7857 | 0.0158 | 0.0098 | \cellcolorbestgreen0.7727 |
| NN | 0.1425 | 0.0948 | 0.5882 | 0.0934 | 0.0800 | 0.6071 | 0.1869 | 0.1134 | \cellcolorsecondgreen0.5455 |
| GDPC1 |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorsecondgreen0.0152 | 0.0077 | 0.4510 | \cellcolorbestgreen0.0038 | \cellcolorbestgreen0.0029 | 0.3929 | \cellcolorsecondgreen0.0225 | 0.0138 | 0.5000 |
| AR | 0.0165 | \cellcolorbestgreen0.0066 | 0.2745 | \cellcolorsecondgreen0.0040 | \cellcolorsecondgreen0.0032 | 0.5000 | 0.0244 | \cellcolorsecondgreen0.0109 | 0.0000 |
| MIDAS | \cellcolorbestgreen0.0116 | 0.0075 | \cellcolorbestgreen0.5882 | 0.0078 | 0.0062 | 0.5357 | \cellcolorbestgreen0.0151 | \cellcolorbestgreen0.0091 | \cellcolorbestgreen0.6364 |
| OLS | 0.1240 | 0.0627 | \cellcolorsecondgreen0.5686 | 0.0483 | 0.0417 | \cellcolorbestgreen0.6071 | 0.1784 | 0.0891 | 0.5000 |
| XGB | 0.0153 | \cellcolorsecondgreen0.0071 | 0.5098 | 0.0042 | 0.0036 | \cellcolorsecondgreen0.5714 | 0.0226 | 0.0114 | 0.4091 |
| NN | 0.1575 | 0.0726 | 0.4902 | 0.0342 | 0.0255 | 0.4286 | 0.2336 | 0.1320 | \cellcolorsecondgreen0.5455 |

Table 2: Out-of-sample forecasting performance for target series where MPTE achieves the lowest RMSE over the full sample. The table reports RMSE, MAE and DA for MPTE and competing models over the full evaluation period, as well as the pre-COVID and post-COVID subsamples. Dark green indicates the best-performing method and light green
the second-best within each column.



|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Full | | | Pre-COVID | | | Post-COVID | | |
|  | RMSE | MAE | DA | RMSE | MAE | DA | RMSE | MAE | DA |
| DPIC96 |  |  |  |  |  |  |  |  |  |
| MPTE | 0.0271 | 0.0138 | 0.5098 | \cellcolorsecondgreen0.0105 | 0.0061 | \cellcolorbestgreen0.7143 | 0.0389 | 0.0236 | 0.2273 |
| AR | \cellcolorsecondgreen0.0262 | \cellcolorsecondgreen0.0130 | 0.0000 | 0.0109 | \cellcolorsecondgreen0.0059 | 0.0000 | \cellcolorsecondgreen0.0375 | \cellcolorsecondgreen0.0219 | 0.0000 |
| MIDAS | \cellcolorbestgreen0.0138 | \cellcolorbestgreen0.0087 | \cellcolorbestgreen0.6471 | \cellcolorbestgreen0.0077 | \cellcolorsecondgreen0.0059 | \cellcolorsecondgreen0.6429 | \cellcolorbestgreen0.0189 | \cellcolorbestgreen0.0122 | \cellcolorbestgreen0.6818 |
| OLS | 0.1470 | 0.0799 | 0.4510 | 0.0462 | 0.0398 | 0.3929 | 0.2149 | 0.1305 | \cellcolorsecondgreen0.5000 |
| XGB | 0.0266 | \cellcolorsecondgreen0.0130 | 0.4902 | 0.0109 | \cellcolorbestgreen0.0058 | 0.5357 | 0.0381 | 0.0222 | 0.4545 |
| NN | 0.1186 | 0.0662 | \cellcolorsecondgreen0.5294 | 0.0383 | 0.0313 | 0.6071 | 0.1731 | 0.1102 | 0.4545 |
| EXPGSC1 |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorsecondgreen0.0389 | 0.0231 | \cellcolorbestgreen0.6275 | 0.0194 | \cellcolorsecondgreen0.0165 | \cellcolorbestgreen0.6071 | \cellcolorsecondgreen0.0543 | \cellcolorsecondgreen0.0315 | \cellcolorbestgreen0.6364 |
| AR | 0.0418 | \cellcolorsecondgreen0.0210 | 0.0000 | \cellcolorbestgreen0.0140 | \cellcolorbestgreen0.0124 | 0.0000 | 0.0609 | 0.0319 | 0.0000 |
| MIDAS | 0.0792 | 0.0444 | 0.5294 | 0.0345 | 0.0283 | \cellcolorsecondgreen0.5357 | 0.1126 | 0.0649 | 0.5000 |
| OLS | 0.3296 | 0.2165 | \cellcolorsecondgreen0.5490 | 0.1892 | 0.1536 | 0.5000 | 0.4477 | 0.2959 | \cellcolorsecondgreen0.5909 |
| XGB | \cellcolorbestgreen0.0339 | \cellcolorbestgreen0.0196 | \cellcolorsecondgreen0.5490 | \cellcolorsecondgreen0.0190 | 0.0169 | 0.5000 | \cellcolorbestgreen0.0462 | \cellcolorbestgreen0.0231 | \cellcolorsecondgreen0.5909 |
| NN | 0.2105 | 0.1455 | 0.4510 | 0.1363 | 0.1067 | 0.5000 | 0.2771 | 0.1944 | 0.4091 |
| FPIx |  |  |  |  |  |  |  |  |  |
| MPTE | 0.0199 | 0.0123 | 0.5098 | 0.0094 | 0.0078 | \cellcolorsecondgreen0.5714 | 0.0281 | 0.0180 | 0.4545 |
| AR | \cellcolorbestgreen0.0171 | \cellcolorbestgreen0.0096 | \cellcolorsecondgreen0.5882 | \cellcolorbestgreen0.0073 | \cellcolorbestgreen0.0058 | 0.5357 | \cellcolorbestgreen0.0245 | \cellcolorbestgreen0.0145 | \cellcolorbestgreen0.6364 |
| MIDAS | 0.0499 | 0.0237 | \cellcolorbestgreen0.6078 | 0.0131 | 0.0113 | \cellcolorbestgreen0.6786 | 0.0735 | 0.0393 | 0.5455 |
| OLS | 0.3206 | 0.1554 | \cellcolorsecondgreen0.5882 | 0.1058 | 0.0881 | \cellcolorsecondgreen0.5714 | 0.4673 | 0.2403 | \cellcolorsecondgreen0.5909 |
| XGB | \cellcolorsecondgreen0.0177 | \cellcolorsecondgreen0.0110 | 0.4706 | \cellcolorsecondgreen0.0078 | \cellcolorsecondgreen0.0065 | 0.4286 | \cellcolorsecondgreen0.0252 | \cellcolorsecondgreen0.0166 | 0.5000 |
| NN | 0.1734 | 0.1069 | 0.4902 | 0.0935 | 0.0711 | 0.4643 | 0.2387 | 0.1520 | 0.5000 |
| CPILFESL |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorsecondgreen0.0036 | \cellcolorsecondgreen0.0021 | \cellcolorsecondgreen0.6078 | \cellcolorsecondgreen0.0015 | \cellcolorsecondgreen0.0012 | \cellcolorbestgreen0.7143 | \cellcolorsecondgreen0.0052 | \cellcolorsecondgreen0.0033 | \cellcolorsecondgreen0.5000 |
| AR | \cellcolorsecondgreen0.0036 | \cellcolorsecondgreen0.0021 | 0.4902 | \cellcolorsecondgreen0.0015 | \cellcolorsecondgreen0.0012 | 0.5714 | \cellcolorsecondgreen0.0052 | \cellcolorsecondgreen0.0033 | 0.3636 |
| MIDAS | 0.0094 | 0.0051 | \cellcolorsecondgreen0.6078 | 0.0038 | 0.0031 | 0.5357 | 0.0135 | 0.0076 | \cellcolorbestgreen0.7273 |
| OLS | 0.0197 | 0.0109 | 0.4314 | 0.0080 | 0.0062 | 0.3571 | 0.0282 | 0.0169 | \cellcolorsecondgreen0.5000 |
| XGB | \cellcolorbestgreen0.0034 | \cellcolorbestgreen0.0019 | \cellcolorbestgreen0.6471 | \cellcolorbestgreen0.0014 | \cellcolorbestgreen0.0011 | 0.5714 | \cellcolorbestgreen0.0048 | \cellcolorbestgreen0.0030 | \cellcolorbestgreen0.7273 |
| NN | 0.1249 | 0.0921 | 0.5098 | 0.0945 | 0.0761 | \cellcolorsecondgreen0.6071 | 0.1549 | 0.1122 | 0.4091 |
| IMPGSC1 |  |  |  |  |  |  |  |  |  |
| MPTE | 0.0412 | 0.0229 | 0.5098 | 0.0157 | 0.0128 | \cellcolorsecondgreen0.5357 | 0.0593 | 0.0356 | \cellcolorsecondgreen0.5000 |
| AR | \cellcolorsecondgreen0.0392 | \cellcolorbestgreen0.0197 | 0.0000 | \cellcolorbestgreen0.0102 | \cellcolorbestgreen0.0086 | 0.0000 | \cellcolorsecondgreen0.0579 | \cellcolorsecondgreen0.0337 | 0.0000 |
| MIDAS | 0.1346 | 0.0518 | \cellcolorbestgreen0.6078 | 0.0411 | 0.0337 | 0.5000 | 0.1971 | 0.0746 | \cellcolorbestgreen0.7273 |
| OLS | 0.4452 | 0.2757 | 0.3922 | 0.1672 | 0.1339 | 0.3929 | 0.6426 | 0.4544 | 0.4091 |
| XGB | \cellcolorbestgreen0.0382 | \cellcolorsecondgreen0.0203 | \cellcolorsecondgreen0.5686 | \cellcolorsecondgreen0.0133 | \cellcolorsecondgreen0.0112 | \cellcolorbestgreen0.6429 | \cellcolorbestgreen0.0554 | \cellcolorbestgreen0.0318 | \cellcolorsecondgreen0.5000 |
| NN | 0.2723 | 0.2034 | 0.4706 | 0.2436 | 0.1790 | 0.5000 | 0.3046 | 0.2341 | 0.4091 |

Table 3: Out-of-sample forecasting performance for target series where MPTE does not achieve the lowest RMSE over the full sample. The table reports RMSE, MAE, and DA for MPTE and competing models over the full evaluation period, as well as the pre-COVID and Post-COVID subsamples. Dark green indicates the best-performing method and light green
the second-best within each column.



|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Full | | | Pre-COVID | | | Post-COVID | | |
|  | RMSE | MAE | DA | RMSE | MAE | DA | RMSE | MAE | DA |
| MPTE | 4 | 3 | 2 | 3 | 5 | 6 | 3 | 2 | 3 |
| MIDAS | 4 | 3 | 8 | 4 | 2 | 4 | 5 | 5 | 8 |
| XGB | 5 | 7 | 2 | 6 | 6 | 2 | 5 | 6 | 1 |
| OLS | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |

Table 4: Number of target series for which each model achieves the best forecasting performance relative to competitors. Counts are reported for RMSE, MAE, and DA over the full evaluation period, as well as the pre-COVID and Post-COVID subsamples. Higher counts indicate superior relative performance.



![Refer to caption](x1.png)

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

Figure 3: Out-of-sample forecasts for GDPC1 (top row) and OUTNFB (bottom row). Left panels report forecasts over the pre-COVID evaluation window, while right panels show forecasts over the full out-of-sample period.

### 7.1 Empirical ablation analysis

This subsection examines the empirical relevance of the main architectural components of MPTE by analyzing the same set of ablation variants introduced in Section [6](https://arxiv.org/html/2601.16274v1#S6 "6 Simulation evidence on attention-based mixed-frequency estimation ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
Tables [5](https://arxiv.org/html/2601.16274v1#S7.T5 "Table 5 ‣ 7.1 Empirical ablation analysis ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") and [6](https://arxiv.org/html/2601.16274v1#S7.T6 "Table 6 ‣ 7.1 Empirical ablation analysis ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") report out-of-sample forecasting performance for the same target series as in Tables [2](https://arxiv.org/html/2601.16274v1#S7.T2 "Table 2 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") and [3](https://arxiv.org/html/2601.16274v1#S7.T3 "Table 3 ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), with target series grouped according to whether the full MPTE achieves the lowest RMSE over the full evaluation period in the comparison with competing models reported earlier. We also report the statistical comparison results in Appendix [B](https://arxiv.org/html/2601.16274v1#A2 "Appendix B Diebold–Mariano tests and Model Confidence Set results ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").

Across target series for which MPTE achieves the lowest RMSE relative to competing models, the impact of removing individual model components varies substantially across targets. For OUTNFB, the full MPTE specification consistently outperforms all ablation variants in terms of RMSE across subsamples, consistent with joint modeling of nonlinearities, attention, and mixed-frequency inputs being particularly valuable for this series.

In contrast, for GDPC1, most ablation variants achieve comparable or lower RMSE than the full model, with AB5, corresponding to a specification that retains only end-of-quarter monthly observations, performing best over the full evaluation period. This pattern suggests that high-frequency inputs provide limited incremental predictive content for this target.

For price-related series such as PCECTPI and CPIAUCSL, no single specification uniformly dominates across all ablations. However, models that retain nonlinear components tend to outperform their linear counterparts, whereas removing attention mechanisms has a comparatively smaller effect on RMSE. This evidence indicates that modest nonlinear transformations can be beneficial for forecasting smoother macroeconomic series, whereas attention-based cross-frequency aggregation appears less critical in these settings. Overall, the ablation results highlight that the relevance of individual model components is target specific and depends on the underlying data characteristics, rather than yielding uniform gains across series.

Table [6](https://arxiv.org/html/2601.16274v1#S7.T6 "Table 6 ‣ 7.1 Empirical ablation analysis ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") reports ablation results for target series where MPTE does not achieve the lowest RMSE relative to competing models. Also in these cases, the relative performance of MPTE and its ablation variants varies across targets, and no single architectural component systematically accounts for underperformance.

For some series, such as EXPGSC1, the full MPTE specification outperforms all ablation variants, indicating that removing individual components leads to a deterioration in RMSE performance. In contrast, for targets such as FPIx, specific ablations perform comparably to or slightly better than the full model; in particular, the variant without nonlinear components attains marginally lower RMSE, consistent with limited gains from additional model expressiveness.

For CPILFESL, performance differences across ablations are negligible, with RMSE values differing only at the level of numerical rounding. This near invariance across specifications is consistent with the pronounced smoothness of the series, for which nonlinearities and attention mechanisms appear to provide little incremental benefit.

Overall, the empirical ablation results indicate that the relevance of individual architectural components is highly target dependent and closely related to the amount and structure of information present in each series. In settings where mixed-frequency or nonlinear signals are informative, removing components such as nonlinear transformations or attention tends to degrade forecasting performance, while for smoother series the effects of additional model expressiveness are limited. Motivated by this heterogeneity, we next examine the internal behavior of MPTE by analyzing its attention weights and cross-frequency aggregation patterns, with the goal of better understanding how the model allocates information across variables and time.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Full | | | Pre-COVID | | | Post-COVID | | |
|  | RMSE | MAE | DA | RMSE | MAE | DA | RMSE | MAE | DA |
| OUTNFB |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorbestgreen0.0180 | \cellcolorsecondgreen0.0081 | \cellcolorsecondgreen0.6000 | \cellcolorbestgreen0.0042 | \cellcolorbestgreen0.0035 | \cellcolorsecondgreen0.5714 | \cellcolorbestgreen0.0270 | 0.0142 | 0.6190 |
| AB1 | \cellcolorsecondgreen0.0197 | \cellcolorbestgreen0.0080 | 0.5000 | \cellcolorsecondgreen0.0045 | \cellcolorsecondgreen0.0037 | 0.4286 | 0.0295 | \cellcolorbestgreen0.0137 | 0.5714 |
| AB2 | \cellcolorsecondgreen0.0197 | 0.0093 | 0.5600 | 0.0058 | 0.0045 | 0.5357 | \cellcolorsecondgreen0.0293 | 0.0156 | 0.6190 |
| AB3 | 0.0205 | 0.0088 | 0.5400 | 0.0053 | 0.0043 | \cellcolorsecondgreen0.6429 | 0.0307 | 0.0149 | 0.3810 |
| AB4 | 0.0205 | 0.0095 | 0.5200 | 0.0057 | 0.0046 | 0.3929 | 0.0305 | 0.0160 | \cellcolorbestgreen0.7143 |
| AB5 | 0.0204 | 0.0091 | \cellcolorbestgreen0.6200 | 0.0050 | 0.0041 | \cellcolorsecondgreen0.5714 | 0.0305 | 0.0156 | \cellcolorsecondgreen0.6667 |
| PCECTPI |  |  |  |  |  |  |  |  |  |
| MPTE | 0.0039 | \cellcolorsecondgreen0.0030 | \cellcolorbestgreen0.6078 | \cellcolorbestgreen0.0030 | \cellcolorbestgreen0.0021 | \cellcolorsecondgreen0.7143 | 0.0049 | 0.0040 | 0.4545 |
| AB1 | 0.0047 | 0.0037 | \cellcolorsecondgreen0.5294 | 0.0042 | 0.0035 | 0.4643 | 0.0053 | 0.0039 | 0.6364 |
| AB2 | \cellcolorbestgreen0.0036 | \cellcolorbestgreen0.0028 | 0.4902 | \cellcolorsecondgreen0.0031 | \cellcolorsecondgreen0.0025 | 0.3571 | \cellcolorbestgreen0.0041 | \cellcolorbestgreen0.0032 | \cellcolorsecondgreen0.6818 |
| AB3 | \cellcolorbestgreen0.0036 | \cellcolorbestgreen0.0028 | \cellcolorsecondgreen0.5294 | \cellcolorsecondgreen0.0031 | \cellcolorsecondgreen0.0025 | 0.3929 | \cellcolorbestgreen0.0041 | \cellcolorbestgreen0.0032 | \cellcolorbestgreen0.7273 |
| AB4 | \cellcolorbestgreen0.0036 | \cellcolorbestgreen0.0028 | 0.5098 | \cellcolorsecondgreen0.0031 | \cellcolorsecondgreen0.0025 | 0.5357 | \cellcolorbestgreen0.0041 | \cellcolorbestgreen0.0032 | 0.4545 |
| AB5 | \cellcolorsecondgreen0.0037 | \cellcolorbestgreen0.0028 | \cellcolorbestgreen0.6078 | \cellcolorbestgreen0.0030 | \cellcolorsecondgreen0.0025 | \cellcolorbestgreen0.7500 | \cellcolorsecondgreen0.0043 | \cellcolorsecondgreen0.0033 | 0.4091 |
| PCEPILFE |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorbestgreen0.0024 | \cellcolorbestgreen0.0016 | 0.5294 | 0.0015 | \cellcolorbestgreen0.0011 | 0.4286 | \cellcolorbestgreen0.0033 | \cellcolorbestgreen0.0023 | \cellcolorbestgreen0.6364 |
| AB1 | \cellcolorbestgreen0.0024 | \cellcolorsecondgreen0.0018 | \cellcolorsecondgreen0.5686 | \cellcolorbestgreen0.0013 | \cellcolorsecondgreen0.0012 | \cellcolorsecondgreen0.5714 | \cellcolorbestgreen0.0033 | \cellcolorsecondgreen0.0025 | \cellcolorsecondgreen0.5455 |
| AB2 | \cellcolorbestgreen0.0024 | \cellcolorsecondgreen0.0018 | \cellcolorsecondgreen0.5686 | \cellcolorbestgreen0.0013 | \cellcolorsecondgreen0.0012 | \cellcolorbestgreen0.6786 | \cellcolorsecondgreen0.0034 | \cellcolorsecondgreen0.0025 | 0.4091 |
| AB3 | \cellcolorsecondgreen0.0025 | \cellcolorsecondgreen0.0018 | \cellcolorbestgreen0.5882 | \cellcolorsecondgreen0.0014 | \cellcolorsecondgreen0.0012 | 0.6071 | \cellcolorsecondgreen0.0034 | 0.0026 | \cellcolorsecondgreen0.5455 |
| AB4 | \cellcolorsecondgreen0.0025 | 0.0019 | 0.5490 | \cellcolorsecondgreen0.0014 | 0.0013 | 0.4643 | \cellcolorsecondgreen0.0034 | 0.0026 | \cellcolorbestgreen0.6364 |
| AB5 | 0.0027 | 0.0019 | 0.4314 | \cellcolorbestgreen0.0013 | \cellcolorsecondgreen0.0012 | \cellcolorsecondgreen0.5714 | 0.0038 | 0.0028 | 0.2727 |
| CPIAUCSL |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorsecondgreen0.0054 | 0.0043 | \cellcolorsecondgreen0.6275 | 0.0052 | 0.0041 | \cellcolorsecondgreen0.6786 | \cellcolorbestgreen0.0058 | \cellcolorbestgreen0.0044 | 0.5455 |
| AB1 | \cellcolorbestgreen0.0049 | \cellcolorsecondgreen0.0037 | 0.6078 | \cellcolorsecondgreen0.0038 | \cellcolorsecondgreen0.0032 | \cellcolorbestgreen0.7143 | \cellcolorsecondgreen0.0061 | \cellcolorbestgreen0.0044 | 0.4545 |
| AB2 | \cellcolorsecondgreen0.0054 | 0.0039 | 0.4706 | 0.0043 | 0.0034 | 0.3571 | 0.0065 | \cellcolorsecondgreen0.0045 | \cellcolorbestgreen0.6364 |
| AB3 | 0.0055 | 0.0038 | 0.5294 | 0.0044 | 0.0033 | 0.4643 | 0.0065 | \cellcolorsecondgreen0.0045 | \cellcolorbestgreen0.6364 |
| AB4 | 0.0055 | 0.0038 | 0.4706 | 0.0044 | 0.0033 | 0.4643 | 0.0065 | \cellcolorsecondgreen0.0045 | 0.5000 |
| AB5 | \cellcolorbestgreen0.0049 | \cellcolorbestgreen0.0036 | \cellcolorbestgreen0.6471 | \cellcolorbestgreen0.0034 | \cellcolorbestgreen0.0026 | \cellcolorsecondgreen0.6786 | 0.0063 | 0.0049 | \cellcolorsecondgreen0.5909 |
| GDPC1 |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorsecondgreen0.0152 | 0.0077 | 0.4510 | \cellcolorsecondgreen0.0038 | \cellcolorsecondgreen0.0029 | 0.3929 | \cellcolorsecondgreen0.0225 | 0.0138 | 0.5000 |
| AB1 | 0.0166 | 0.0081 | 0.5294 | 0.0045 | 0.0034 | 0.4643 | 0.0244 | 0.0140 | \cellcolorsecondgreen0.5909 |
| AB2 | 0.0162 | 0.0080 | \cellcolorsecondgreen0.5490 | 0.0043 | 0.0034 | \cellcolorsecondgreen0.5714 | 0.0238 | 0.0137 | 0.5000 |
| AB3 | 0.0165 | \cellcolorsecondgreen0.0072 | 0.3725 | 0.0041 | 0.0033 | 0.3214 | 0.0244 | \cellcolorsecondgreen0.0122 | 0.4545 |
| AB4 | 0.0164 | \cellcolorbestgreen0.0071 | \cellcolorbestgreen0.6078 | \cellcolorbestgreen0.0035 | \cellcolorbestgreen0.0027 | \cellcolorsecondgreen0.5714 | 0.0244 | 0.0128 | \cellcolorbestgreen0.6818 |
| AB5 | \cellcolorbestgreen0.0141 | 0.0081 | \cellcolorsecondgreen0.5490 | 0.0068 | 0.0055 | 0.4286 | \cellcolorbestgreen0.0197 | \cellcolorbestgreen0.0114 | \cellcolorbestgreen0.6818 |

Table 5: Out-of-sample forecasting performance for target series where MPTE achieves the lowest RMSE over the full sample. The table reports RMSE, MAE, and DA for MPTE and its ablation variants over the full evaluation period, as well as the pre-COVID and Post-COVID subsamples. Dark green indicates the best-performing method and light green
the second-best within each column.



|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Full | | | Pre-COVID | | | Post-COVID | | |
|  | RMSE | MAE | DA | RMSE | MAE | DA | RMSE | MAE | DA |
| DPIC96 |  |  |  |  |  |  |  |  |  |
| MPTE | 0.0271 | 0.0138 | 0.5098 | \cellcolorsecondgreen0.0105 | \cellcolorsecondgreen0.0061 | \cellcolorsecondgreen0.7143 | 0.0389 | 0.0236 | 0.2273 |
| AB1 | 0.0263 | 0.0140 | \cellcolorbestgreen0.5490 | 0.0108 | 0.0071 | 0.5357 | 0.0377 | 0.0226 | \cellcolorbestgreen0.5909 |
| AB2 | \cellcolorsecondgreen0.0262 | 0.0134 | \cellcolorbestgreen0.5490 | 0.0109 | 0.0069 | 0.5714 | \cellcolorsecondgreen0.0374 | \cellcolorsecondgreen0.0215 | \cellcolorsecondgreen0.5000 |
| AB3 | \cellcolorsecondgreen0.0262 | \cellcolorsecondgreen0.0131 | 0.4510 | 0.0107 | 0.0065 | 0.3571 | \cellcolorsecondgreen0.0374 | \cellcolorsecondgreen0.0215 | \cellcolorbestgreen0.5909 |
| AB4 | \cellcolorbestgreen0.0260 | 0.0132 | \cellcolorsecondgreen0.5294 | 0.0109 | 0.0062 | 0.6071 | \cellcolorbestgreen0.0372 | 0.0219 | 0.4545 |
| AB5 | 0.0270 | \cellcolorbestgreen0.0125 | \cellcolorbestgreen0.5490 | \cellcolorbestgreen0.0102 | \cellcolorbestgreen0.0055 | \cellcolorbestgreen0.7500 | 0.0389 | \cellcolorbestgreen0.0213 | 0.3182 |
| EXPGSC1 |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorbestgreen0.0389 | 0.0231 | \cellcolorbestgreen0.6275 | 0.0194 | 0.0165 | \cellcolorsecondgreen0.6071 | \cellcolorbestgreen0.0543 | 0.0315 | \cellcolorbestgreen0.6364 |
| AB1 | 0.0416 | 0.0223 | \cellcolorsecondgreen0.5490 | 0.0171 | 0.0152 | \cellcolorsecondgreen0.6071 | 0.0595 | 0.0313 | 0.4545 |
| AB2 | 0.0413 | \cellcolorsecondgreen0.0198 | 0.4510 | \cellcolorsecondgreen0.0127 | \cellcolorsecondgreen0.0109 | 0.4286 | 0.0604 | 0.0310 | \cellcolorsecondgreen0.5000 |
| AB3 | 0.0408 | \cellcolorbestgreen0.0179 | 0.4902 | \cellcolorbestgreen0.0108 | \cellcolorbestgreen0.0084 | 0.5714 | 0.0601 | \cellcolorbestgreen0.0298 | 0.3636 |
| AB4 | 0.0424 | 0.0227 | 0.4118 | 0.0185 | 0.0162 | 0.3929 | 0.0602 | \cellcolorsecondgreen0.0308 | 0.4545 |
| AB5 | \cellcolorsecondgreen0.0404 | 0.0233 | \cellcolorsecondgreen0.5490 | 0.0188 | 0.0164 | \cellcolorbestgreen0.6786 | \cellcolorsecondgreen0.0570 | 0.0320 | 0.4091 |
| FPIx |  |  |  |  |  |  |  |  |  |
| MPTE | 0.0199 | \cellcolorbestgreen0.0123 | 0.5098 | \cellcolorbestgreen0.0094 | \cellcolorsecondgreen0.0078 | 0.5714 | 0.0281 | \cellcolorbestgreen0.0180 | \cellcolorsecondgreen0.4545 |
| AB1 | \cellcolorbestgreen0.0191 | \cellcolorsecondgreen0.0132 | \cellcolorsecondgreen0.5294 | 0.0111 | \cellcolorbestgreen0.0075 | \cellcolorsecondgreen0.6429 | \cellcolorbestgreen0.0258 | 0.0203 | 0.4091 |
| AB2 | \cellcolorsecondgreen0.0194 | \cellcolorsecondgreen0.0132 | \cellcolorsecondgreen0.5294 | \cellcolorsecondgreen0.0098 | 0.0083 | \cellcolorbestgreen0.6786 | \cellcolorsecondgreen0.0270 | \cellcolorsecondgreen0.0195 | 0.3636 |
| AB3 | 0.0249 | 0.0195 | 0.4510 | 0.0188 | 0.0167 | 0.4643 | 0.0308 | 0.0230 | \cellcolorsecondgreen0.4545 |
| AB4 | 0.0228 | 0.0164 | 0.4902 | 0.0117 | 0.0091 | 0.5714 | 0.0317 | 0.0257 | 0.4091 |
| AB5 | 0.0223 | 0.0184 | \cellcolorbestgreen0.5882 | 0.0178 | 0.0153 | 0.6071 | \cellcolorsecondgreen0.0270 | 0.0223 | \cellcolorbestgreen0.5909 |
| CPILFESL |  |  |  |  |  |  |  |  |  |
| MPTE | \cellcolorbestgreen0.0036 | \cellcolorbestgreen0.0021 | \cellcolorbestgreen0.6078 | \cellcolorbestgreen0.0015 | \cellcolorbestgreen0.0012 | \cellcolorbestgreen0.7143 | \cellcolorbestgreen0.0052 | \cellcolorbestgreen0.0033 | \cellcolorsecondgreen0.5000 |
| AB1 | \cellcolorbestgreen0.0036 | \cellcolorbestgreen0.0021 | 0.4902 | \cellcolorbestgreen0.0015 | \cellcolorbestgreen0.0012 | 0.4286 | \cellcolorbestgreen0.0052 | \cellcolorbestgreen0.0033 | \cellcolorbestgreen0.5909 |
| AB2 | \cellcolorbestgreen0.0036 | \cellcolorbestgreen0.0021 | 0.4706 | \cellcolorbestgreen0.0015 | \cellcolorbestgreen0.0012 | 0.4643 | \cellcolorbestgreen0.0052 | \cellcolorbestgreen0.0033 | \cellcolorsecondgreen0.5000 |
| AB3 | \cellcolorbestgreen0.0036 | \cellcolorbestgreen0.0021 | 0.5294 | \cellcolorbestgreen0.0015 | \cellcolorbestgreen0.0012 | \cellcolorsecondgreen0.6429 | \cellcolorbestgreen0.0052 | \cellcolorbestgreen0.0033 | 0.4091 |
| AB4 | \cellcolorbestgreen0.0036 | \cellcolorbestgreen0.0021 | 0.5098 | \cellcolorbestgreen0.0015 | \cellcolorbestgreen0.0012 | 0.6071 | \cellcolorbestgreen0.0052 | \cellcolorbestgreen0.0033 | 0.4091 |
| AB5 | \cellcolorbestgreen0.0036 | \cellcolorbestgreen0.0021 | \cellcolorsecondgreen0.5490 | \cellcolorbestgreen0.0015 | \cellcolorbestgreen0.0012 | \cellcolorsecondgreen0.6429 | \cellcolorbestgreen0.0052 | \cellcolorbestgreen0.0033 | 0.4545 |
| IMPGSC1 |  |  |  |  |  |  |  |  |  |
| MPTE | 0.0412 | 0.0229 | 0.5098 | 0.0157 | 0.0128 | \cellcolorbestgreen0.5357 | 0.0593 | 0.0356 | 0.5000 |
| AB1 | \cellcolorbestgreen0.0380 | 0.0229 | \cellcolorsecondgreen0.5294 | 0.0201 | 0.0164 | \cellcolorsecondgreen0.5000 | \cellcolorbestgreen0.0525 | \cellcolorbestgreen0.0310 | \cellcolorsecondgreen0.5909 |
| AB2 | 0.0393 | \cellcolorsecondgreen0.0194 | \cellcolorsecondgreen0.5294 | \cellcolorsecondgreen0.0092 | \cellcolorsecondgreen0.0068 | \cellcolorbestgreen0.5357 | 0.0581 | 0.0352 | 0.5455 |
| AB3 | \cellcolorsecondgreen0.0390 | \cellcolorbestgreen0.0188 | 0.4902 | \cellcolorbestgreen0.0084 | \cellcolorbestgreen0.0063 | \cellcolorbestgreen0.5357 | \cellcolorsecondgreen0.0579 | \cellcolorsecondgreen0.0347 | 0.4545 |
| AB4 | 0.0411 | 0.0247 | \cellcolorbestgreen0.6078 | 0.0188 | 0.0167 | \cellcolorbestgreen0.5357 | 0.0580 | 0.0349 | \cellcolorbestgreen0.6818 |
| AB5 | 0.0410 | 0.0233 | 0.5098 | 0.0145 | 0.0118 | \cellcolorsecondgreen0.5000 | 0.0594 | 0.0379 | 0.5455 |

Table 6: Out-of-sample forecasting performance for target series where MPTE does not achieve the lowest RMSE over the full sample. The table reports RMSE, MAE, and DA for MPTE and its ablation variants over the full evaluation period, as well as the pre-COVID and Post-COVID subsamples.

### 7.2 Attention-based aggregation patterns

Motivated by the target-specific nature of the empirical ablation results, we examine how MPTE allocates information internally across variables and time. We study the learned attention weights to assess whether differences in predictive performance are associated with systematic differences in cross-sectional and temporal aggregation.

A key advantage of MPTE is interpretability through its learned attention weights. To interpret the attention heatmaps, it is useful to distinguish two complementary summaries of the attention matrix. Averaging attention weights over variables yields a distribution over time indices within the context window, which provides an empirical analogue of the temporal weighting operator BB studied in the theoretical analysis. Conversely, averaging attention weights over time yields variable-specific importance weights, corresponding to the cross-sectional aggregation induced by the matrix AzA\_{z}. In practice, we compute these summaries by averaging attention weights over all input sequences in the out-of-sample evaluation period. When the optimized model for a given target includes multiple attention heads, we further average the attention weights across heads.

Figures [4](https://arxiv.org/html/2601.16274v1#S7.F4 "Figure 4 ‣ 7.2 Attention-based aggregation patterns ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") and [5](https://arxiv.org/html/2601.16274v1#S7.F5 "Figure 5 ‣ 7.2 Attention-based aggregation patterns ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") report heatmaps of the cross-sectional attention matrix AzA\_{z} for selected target series. For each target, we compare the full MPTE specification with the AB1 ablation, which removes nonlinear transformations from the encoder while preserving the attention mechanism. The horizontal axis indexes attending variables, while the vertical axis indexes attended variables.

Figure [4](https://arxiv.org/html/2601.16274v1#S7.F4 "Figure 4 ‣ 7.2 Attention-based aggregation patterns ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") shows that introducing nonlinear transformations substantially alters the cross-sectional aggregation structure learned by the model for targets where MPTE achieves lower RMSE than competing approaches. For GDPC1, the full model places pronounced attention weight on variables such as CUMFNS, while the AB1 specification shifts attention toward indicators such as M2REAL and TB6MS. This reallocation is economically intuitive. When nonlinear transformations are available, the model can better capture state-dependent effects in real activity indicators, making capacity utilization in manufacturing (CUMFNS) particularly informative for forecasting GDP growth. In the absence of nonlinearities, such nonlinear effects cannot be captured effectively, and the model instead places greater weight on variables such as the real M2 money stock (M2REAL) and short-term interest rates (TB6MS), whose influence on output is more readily approximated by linear relationships.

A similar pattern emerges for OUTNFB. In both the full model and the AB1 ablation, several quarterly variables receive high attention weight, reflecting a pronounced low-frequency component of nonfarm business output. However, the presence of nonlinear transformations modifies how monthly and quarterly information is combined. Under the full specification, variables such as CPILFESL and IMPGSC1 receive greater attention, consistent with nonlinear interactions between prices and trade-related quantities that provide incremental information for forecasting real activity. In contrast, without nonlinear transformations, the model concentrates attention on income-related aggregates such as GPDIC1 and DPIC96, alongside CPILFESL, consistent with a more linear cross-sectional aggregation strategy.

The reallocation of attention toward capacity utilization when nonlinear transformations are introduced is consistent with a large macroeconomic literature emphasizing state-dependent real activity dynamics. Measures such as manufacturing capacity utilization are known to exhibit regime-dependent and threshold-type effects, becoming particularly informative during expansions and near capacity constraints, while appearing weakly predictive when averaged linearly across business-cycle states (e.g., Hamilton ([1989](https://arxiv.org/html/2601.16274v1#bib.bib56 "A new approach to the economic analysis of nonstationary time series and the business cycle")); Stock and Watson ([1999](https://arxiv.org/html/2601.16274v1#bib.bib57 "Forecasting inflation"), [2003](https://arxiv.org/html/2601.16274v1#bib.bib58 "Forecasting output and inflation: the role of asset prices"))). In contrast, monetary aggregates and short-term interest rates summarize average financial conditions and are more readily approximated by linear relationships, explaining their prominence in the ablation without nonlinear features. Similar nonlinear aggregation mechanisms have been documented for low-frequency output measures, where interactions between prices and trade-related quantities provide incremental forecasting power only when nonlinearities are allowed (Giannone et al. ([2008](https://arxiv.org/html/2601.16274v1#bib.bib59 "Nowcasting: the real-time informational content of macroeconomic data")); Kilian ([2009](https://arxiv.org/html/2601.16274v1#bib.bib60 "Not all oil price shocks are alike: disentangling demand and supply shocks in the crude oil market"))).

These results are compatible with MPTE delivering strong predictive performance relative to competing models, as in the cases of GDPC1 and OUTNFB, the estimated AzA\_{z} matrix exhibits structured and interpretable patterns rather than diffuse attention. While the specific variables emphasized differ across ablations, attention remains concentrated on economically meaningful subsets of predictors, suggesting that the model is exploiting cross-sectional structure in a systematic manner.

In contrast, Figure [5](https://arxiv.org/html/2601.16274v1#S7.F5 "Figure 5 ‣ 7.2 Attention-based aggregation patterns ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") shows that for CPILFESL, a target for which MPTE does not consistently achieve lower RMSE than competing approaches, the cross-sectional attention patterns are substantially less structured. Both the full model and the AB1 ablation distribute attention more broadly across variables, with no clearly dominant predictors emerging. This behavior is consistent with the smooth dynamics of core inflation measures, where incremental nonlinear or mixed-frequency information is limited. In such settings, the model appears unable to extract a clear cross-sectional signal, which is associated with more diffuse attention weights and correspondingly weaker gains from additional architectural complexity.

Overall, the AzA\_{z} heatmaps are aligned with the empirical findings from the forecasting and ablation exercises. When meaningful nonlinear or mixed-frequency relationships are present in the data, MPTE learns structured cross-sectional aggregation patterns that differ systematically from those of simpler specifications. When such relationships are weak or absent, attention becomes more dispersed, reflecting the limited scope for informative cross-sectional reweighting.

![Refer to caption](x5.png)

![Refer to caption](x6.png)

![Refer to caption](x7.png)

![Refer to caption](x8.png)

Figure 4: Cross-sectional attention (AzA\_{z}) heatmaps. The top row shows GDPC1 and the bottom row OUTNFB. For each target, the left panel reports MPTE and the right panel reports the AB1 ablation. The horizontal axis indexes attending variables, while the vertical axis indexes attended variables.

We next examine the temporal attention matrices BB, which govern how the model aggregates information across time within the input sequence. Figure [6](https://arxiv.org/html/2601.16274v1#S7.F6 "Figure 6 ‣ 7.2 Attention-based aggregation patterns ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") reports the estimated BB matrices for GDPC1 and OUTNFB for the full MPTE and the AB1 ablation, which removes nonlinear transformations in the encoder. Each matrix summarizes attention weights across a two-year context window, corresponding to 24 monthly lags, where attention flows from earlier to later time steps. Across both targets, temporal attention exhibits clear target-specific structure, and the presence of nonlinearities substantially alters how information from different lags is weighted. For GDPC1, the full MPTE assigns non-negligible attention to older lags, indicating that longer-horizon information contributes to forecasting output growth when nonlinear transformations are available. In contrast, under the AB1 ablation, attention concentrates primarily on the most recent one or two lags, suggesting that in the absence of nonlinear feature extraction the model relies more heavily on short-horizon dynamics.

A similar, though less pronounced, pattern emerges for OUTNFB. When nonlinearities are present, the temporal attention matrix displays a recurring structure consistent with quarterly spacing in the lag index, with relatively higher weights assigned to lags corresponding to multiples of three months. Moreover, the influence of these lags appears to increase with distance into the past, indicating that medium- to longer-horizon dynamics play a role in forecasting nonfarm business output. When nonlinearities are removed, this structure becomes weaker, and attention shifts toward more recent observations. The broader temporal support under the full MPTE specification is economically intuitive. Many macroeconomic forces relevant for output growth, such as capacity constraints, investment cycles, and pricing pressures, evolve gradually and affect outcomes only once certain thresholds are reached. Nonlinear transformations allow the model to convert these slowly moving signals into predictive states, thereby increasing the relevance of longer-horizon information. In contrast, linear encoders are unable to capture such state dependence and therefore rely more heavily on short-horizon dynamics.

Figure [7](https://arxiv.org/html/2601.16274v1#S7.F7 "Figure 7 ‣ 7.2 Attention-based aggregation patterns ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") illustrates the effect of removing temporal encoding altogether, corresponding to the AB4 ablation. In this case, temporal attention becomes substantially more diffuse for both GDPC1 and OUTNFB. The model assigns weights with smaller, more uniform magnitudes across lags, with little discrimination among time positions. This pattern reflects the absence of explicit temporal information, which limits the model’s ability to differentiate the relevance of past observations based on their position within the sequence.

Taken together, these results indicate that MPTE endogenously adapts the effective memory of the forecasting model in a target-specific and economically meaningful manner. When nonlinear transformations are available, the model assigns nontrivial weight to medium- and longer-horizon lags, consistent with the presence of slowly evolving macroeconomic forces that influence output growth only once certain thresholds are reached. In contrast, when nonlinear feature extraction is removed, attention collapses toward the most recent observations, reflecting reliance on short-run dynamics that are more readily captured by linear representations. Explicit temporal encoding further sharpens this structure by allowing the model to discriminate among lag positions within the input window. When it is removed, temporal attention becomes diffuse and largely uninformative. Overall, these patterns suggest that nonlinear transformations and temporal encoding jointly enable MPTE to exploit structured temporal dependencies in a disciplined way, rather than mechanically emphasizing either short- or long-horizon information. Unlike MIDAS regressions, which either impose parametric lag polynomials or require selecting a finite lag truncation ex ante, MPTE learns both the relevant temporal horizon and the weighting of individual lags endogenously from the data. This flexibility allows the effective memory length to vary across targets and model specifications.

![Refer to caption](x9.png)

![Refer to caption](x10.png)

Figure 5: Cross-sectional attention (AzA\_{z}) heatmaps for CPILFESL. The left panel reports MPTE and the right panel reports the AB1 ablation. The horizontal axis indexes attending variables, while the vertical axis indexes attended variables.



![Refer to caption](x11.png)

![Refer to caption](x12.png)

![Refer to caption](x13.png)

![Refer to caption](x14.png)

Figure 6: Temporal attention (BB) heatmaps. The top row shows GDPC1 and the bottom row OUTNFB. For each target, the left panel reports MPTE and the right panel reports the AB1 ablation. Both axes index time positions in the input sequence, illustrating how attention weights are distributed across temporal lags.



![Refer to caption](x15.png)

![Refer to caption](x16.png)

Figure 7: Temporal attention (BB) heatmaps for GDPC1 (left) and OUTNFB (right) under the AB4 ablation, which removes the temporal encoding. Both axes index time positions in the input sequence.

## 8 Conclusions and Discussion

This paper introduces MPTE, a novel framework that extends classical factor models to handle mixed-frequency data and nonlinear signals through attention mechanisms. Our approach addresses fundamental limitations of traditional methods that require homogeneous sampling frequencies and rely on linear signal extraction, making it particularly relevant for modern high-dimensional economic and financial datasets.

Our main theoretical contribution establishes consistency and asymptotic normality of factor, loading, and common-component estimators in the linear case under general cross-sectional and temporal attention. We show that Target PCA (Duan et al., [2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")) arises as a special case of our framework when attention reduces to fixed block-level projections, while the general attention-based formulation accommodates rich forms of heterogeneity across units, time periods, and datasets. Unlike target-focused PCA methods that impose uniform weighting within blocks, our approach allows the data to determine which cross-sectional units and time periods are informative for the target task. This adaptivity yields an effective sample size that reflects relevance rather than raw dimension and enables genuine transfer-learning
gains: auxiliary data can improve estimation precision at the first order without altering identification of the target factor space. The resulting asymptotic theory clarifies how factor and loading uncertainty interact across different regimes and shows that efficiency gains are endogenously determined by the concentration of attention. Conceptually, the attention mechanism plays a role analogous to adaptive shrinkage or thresholding in high-dimensional statistics, replacing fixed linear combinations with data-driven weights that focus on informative observations while down-weighting irrelevant or noisy ones. As a result, our framework strictly generalizes existing Target PCA approaches and is particularly well suited for forecasting environments characterized by heterogeneous relevance, structured noise, and partial factor overlap across datasets.

The empirical applications demonstrate the practical value of our approach. In controlled simulations, MPTE exhibits superior performance in nonlinear environments while remaining competitive in linear settings. The macroeconomic forecasting exercise using 48 mixed-frequency series across 13 target variables shows that our method achieves competitive performance against established benchmarks, with the model remaining robust across different evaluation periods and metrics.

Beyond forecasting accuracy, MPTE offers interpretability through attention weights that reveal target-specific variable importance and effective memory length. By separately aggregating attention across variables and time, we show that the model learns economically meaningful cross-sectional and temporal dependencies endogenously, rather than imposing fixed lag structures. Nonlinear feature extraction shifts attention toward state-dependent indicators and medium- to long-horizon dynamics, while simpler specifications emphasize short-run fluctuations and diffuse signals. This provides a transparent link between predictive gains and their underlying economic sources, offering a data-driven framework for policy-relevant interpretation.

Several avenues for future research emerge from this work. First, extending the theoretical analysis to cover nonlinear activation functions would provide formal guarantees for the full MPTE framework. Second, while the attention mechanisms studied here are adaptive in the sense that they learn heterogeneous relevance across units and time within a stable environment, allowing them to evolve endogenously in response to structural breaks or regime changes would further improve performance in nonstationary economic settings. Third, instead of producing point forecasts, the model could be extended using probabilistic deep learning methods to learn the full predictive distribution of the target variable and provide direct uncertainty quantification. The framework also opens possibilities for applications beyond macroeconomic forecasting. Financial risk management, climate modeling, and energy forecasting all involve mixed-frequency data where our approach could prove valuable.

## References

* D. Bahdanau, K. Cho, and Y. Bengio (2014)
  Neural machine translation by jointly learning to align and translate.
  arXiv preprint arXiv:1409.0473.
  Cited by: [§2.2](https://arxiv.org/html/2601.16274v1#S2.SS2.p1.1 "2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* J. Bai and P. Wang (2015)
  Identification and bayesian estimation of dynamic factor models.
  Journal of Business & Economic Statistics 33 (2),  pp. 221–240.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p7.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* J. Bai (2003)
  Inferential theory for factor models of large dimensions.
  Econometrica 71 (1),  pp. 135–171.
  Cited by: [Appendix A](https://arxiv.org/html/2601.16274v1#A1.p1.5 "Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§3.3](https://arxiv.org/html/2601.16274v1#S3.SS3.SSS0.Px1.p1.11 "Comparison with classical PCA and Target PCA. ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* P. Baldi and K. Hornik (1989)
  Neural networks and principal component analysis: learning from examples without local minima.
  Neural networks 2 (1),  pp. 53–58.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p11.2 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* R. Chen, D. Yang, and C. Zhang (2022)
  Factor models for high-dimensional tensor time series.
  Journal of the American Statistical Association 117 (537),  pp. 94–116.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p7.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* T. Chen and C. Guestrin (2016)
  XGBoost: a scalable tree boosting system.
  In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining,
   pp. 785–794.
  External Links: [Document](https://dx.doi.org/10.1145/2939672.2939785)
  Cited by: [§7](https://arxiv.org/html/2601.16274v1#S7.p5.1 "7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* X. Cheng and B. E. Hansen (2015)
  Forecasting with factor-augmented regression: a frequentist model averaging approach.
  Journal of Econometrics 186 (2),  pp. 280–293.
  Cited by: [§4](https://arxiv.org/html/2601.16274v1#S4.p2.1 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* G. Connor, M. Hagmann, and O. Linton (2012)
  Efficient semiparametric estimation of the fama–french model and extensions.
  Econometrica 80 (2),  pp. 713–754.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p5.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* P. G. Coulombe (2025)
  Ordinary least squares as an attention mechanism.
  arXiv preprint arXiv:2504.09663.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p12.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* T. Dai, J. Wang, H. Guo, J. Li, J. Wang, and Z. Zhu (2024)
  FreqFormer: frequency-aware transformer for lightweight image super-resolution.
  In Proceedings of the International Joint Conference on Artificial Intelligence,
   pp. 731–739.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p13.4 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* J. Duan, M. Pelger, and R. Xiong (2024)
  Target pca: transfer learning large dimensional panel data.
  Journal of Econometrics 244 (2),  pp. 105521.
  Cited by: [Appendix A](https://arxiv.org/html/2601.16274v1#A1.p1.5 "Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§1](https://arxiv.org/html/2601.16274v1#S1.p10.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§1](https://arxiv.org/html/2601.16274v1#S1.p11.2 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§1](https://arxiv.org/html/2601.16274v1#S1.p5.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§1](https://arxiv.org/html/2601.16274v1#S1.p9.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§2.1](https://arxiv.org/html/2601.16274v1#S2.SS1.p3.15 "2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§2.1](https://arxiv.org/html/2601.16274v1#S2.SS1.p5.3 "2.1 Model setup ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§2.2](https://arxiv.org/html/2601.16274v1#S2.SS2.p12.1 "2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§2.2](https://arxiv.org/html/2601.16274v1#S2.SS2.p2.4 "2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§2.2](https://arxiv.org/html/2601.16274v1#S2.SS2.p6.6 "2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§2.2](https://arxiv.org/html/2601.16274v1#S2.SS2.p8.4 "2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§3.2](https://arxiv.org/html/2601.16274v1#S3.SS2.p2.1 "3.2 Consistency ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§3.3](https://arxiv.org/html/2601.16274v1#S3.SS3.SSS0.Px1.p1.11 "Comparison with classical PCA and Target PCA. ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§3.3](https://arxiv.org/html/2601.16274v1#S3.SS3.p5.16 "3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§3.3](https://arxiv.org/html/2601.16274v1#S3.SS3.p7.9 "3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§3](https://arxiv.org/html/2601.16274v1#S3.p1.1 "3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§8](https://arxiv.org/html/2601.16274v1#S8.p2.1 "8 Conclusions and Discussion ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* J. Fan, I. Gijbels, T. Hu, and L. Huang (1996)
  A study of variable bandwidth selection for local polynomial regression.
  Statistica Sinica,  pp. 113–127.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p6.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* J. Fan, Y. Liao, and W. Wang (2016)
  Projected principal component analysis in factor models.
  Annals of statistics 44 (1),  pp. 219.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p5.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* M. Forni and M. Lippi (2001)
  The generalized dynamic factor model: representation theory.
  Econometric theory 17 (6),  pp. 1113–1141.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p2.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* C. Foroni, M. Marcellino, and C. Schumacher (2015)
  Unrestricted mixed data sampling (midas): midas regressions with unrestricted lag polynomials.
  Journal of the Royal Statistical Society Series A: Statistics in Society 178 (1),  pp. 57–82.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p6.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* E. Ghysels, A. Sinko, and R. Valkanov (2007)
  MIDAS regressions: further results and new directions.
  Econometric reviews 26 (1),  pp. 53–90.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p2.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§1](https://arxiv.org/html/2601.16274v1#S1.p6.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* D. Giannone, L. Reichlin, and D. Small (2008)
  Nowcasting: the real-time informational content of macroeconomic data.
  Journal of monetary economics 55 (4),  pp. 665–676.
  Cited by: [§7.2](https://arxiv.org/html/2601.16274v1#S7.SS2.p6.1 "7.2 Attention-based aggregation patterns ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* I. Goodfellow, Y. Bengio, A. Courville, and Y. Bengio (2016)
  Deep learning.
  Vol. 1, MIT press Cambridge.
  Cited by: [§5.1](https://arxiv.org/html/2601.16274v1#S5.SS1.p3.7 "5.1 Sequence representation for mixed frequencies with embeddings ‣ 5 Implementation of MPTE with nonlinear signals and mixed frequencies ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* P. Goulet Coulombe, M. Marcellino, and D. Stevanovic (2025)
  Panel machine learning with mixed-frequency data: monitoring state-level fiscal variables.
  Technical report
   University of Quebec in Montreal’s.
  Cited by: [§4](https://arxiv.org/html/2601.16274v1#S4.p2.1 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* G. Grassi, J. House, F. Dentener, S. Federici, M. Den Elzen, and J. Penman (2017)
  The key role of forests in meeting climate targets requires science for credible mitigation.
  Nature Climate Change 7 (3),  pp. 220–226.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p2.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* S. Gu, B. Kelly, and D. Xiu (2021)
  Autoencoder asset pricing models.
  Journal of Econometrics 222 (1),  pp. 429–450.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p11.2 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§1](https://arxiv.org/html/2601.16274v1#S1.p5.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§4](https://arxiv.org/html/2601.16274v1#S4.1.p1.1 "Proof. ‣ 4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§4](https://arxiv.org/html/2601.16274v1#S4.p2.1 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§4](https://arxiv.org/html/2601.16274v1#S4.p9.1 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* J. D. Hamilton (1989)
  A new approach to the economic analysis of nonstationary time series and the business cycle.
  Econometrica: Journal of the econometric society,  pp. 357–384.
  Cited by: [§7.2](https://arxiv.org/html/2601.16274v1#S7.SS2.p6.1 "7.2 Attention-based aggregation patterns ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* M. Ji, J. Du, P. Du, T. Niu, and J. Wang (2025)
  A novel probabilistic carbon price prediction model: integrating the transformer framework with mixed-frequency modeling at different quartiles.
  Applied Energy 391,  pp. 125951.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p13.4 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* A. Katharopoulos, A. Vyas, N. Pappas, and F. Fleuret (2020)
  Transformers are rnns: fast autoregressive transformers with linear attention.
  In International conference on machine learning,
   pp. 5156–5165.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p8.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* B. T. Kelly, S. Pruitt, and Y. Su (2019)
  Characteristics are covariances: a unified model of risk and return.
  Journal of Financial Economics 134 (3),  pp. 501–524.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p2.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* L. Kilian (2009)
  Not all oil price shocks are alike: disentangling demand and supply shocks in the crude oil market.
  American economic review 99 (3),  pp. 1053–1069.
  Cited by: [§7.2](https://arxiv.org/html/2601.16274v1#S7.SS2.p6.1 "7.2 Attention-based aggregation patterns ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* J. Lin and G. Michailidis (2024)
  A multi-task encoder-dual-decoder framework for mixed frequency data prediction.
  International Journal of Forecasting 40 (3),  pp. 942–957.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p13.4 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§6](https://arxiv.org/html/2601.16274v1#S6.p1.9 "6 Simulation evidence on attention-based mixed-frequency estimation ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* M. W. McCracken and S. Ng (2016)
  FRED-MD: a monthly database for macroeconomic research.
  Journal of Business & Economic Statistics 34 (4),  pp. 574–589.
  External Links: [Document](https://dx.doi.org/10.1080/07350015.2015.1086655),
  [Link](https://doi.org/10.1080/07350015.2015.1086655),
  https://doi.org/10.1080/07350015.2015.1086655
  Cited by: [§7](https://arxiv.org/html/2601.16274v1#S7.p1.1 "7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* E. A. Nadaraya (1964)
  On estimating regression.
  Theory of Probability & Its Applications 9 (1),  pp. 141–142.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p12.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§1](https://arxiv.org/html/2601.16274v1#S1.p6.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. (2022)
  Training language models to follow instructions with human feedback.
  Advances in neural information processing systems 35,  pp. 27730–27744.
  Cited by: [§4](https://arxiv.org/html/2601.16274v1#S4.p17.1 "4 Nonlinear signals ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* J. H. Stock and M. W. Watson (1999)
  Forecasting inflation.
  Journal of monetary economics 44 (2),  pp. 293–335.
  Cited by: [§7.2](https://arxiv.org/html/2601.16274v1#S7.SS2.p6.1 "7.2 Attention-based aggregation patterns ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* J. H. Stock and M. W. Watson (2002)
  Forecasting using principal components from a large number of predictors.
  Journal of the American statistical association 97 (460),  pp. 1167–1179.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p2.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* J. H. Stock and M. W. Watson (2003)
  Forecasting output and inflation: the role of asset prices.
  Journal of economic literature 41 (3),  pp. 788–829.
  Cited by: [§7.2](https://arxiv.org/html/2601.16274v1#S7.SS2.p6.1 "7.2 Attention-based aggregation patterns ‣ 7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* J. H. Stock and M. W. Watson (2016)
  Dynamic factor models, factor-augmented vector autoregressions, and structural vector autoregressions in macroeconomics.
  In Handbook of macroeconomics,
  Vol. 2,  pp. 415–525.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p6.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* Y. H. Tsai, S. Bai, M. Yamada, L. Morency, and R. Salakhutdinov (2019)
  Transformer dissection: an unified understanding for transformer’s attention via the lens of kernel.
  In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), K. Inui, J. Jiang, V. Ng, and X. Wan (Eds.),
  Hong Kong, China,  pp. 4344–4353.
  External Links: [Link](https://aclanthology.org/D19-1443/),
  [Document](https://dx.doi.org/10.18653/v1/D19-1443)
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p8.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin (2017)
  Attention is all you need.
  Advances in neural information processing systems 30.
  Cited by: [§2.2](https://arxiv.org/html/2601.16274v1#S2.SS2.p1.1 "2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§2.2](https://arxiv.org/html/2601.16274v1#S2.SS2.p4.7 "2.2 Attention mechanism and context-aware signal construction ‣ 2 Methodology ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§5.1](https://arxiv.org/html/2601.16274v1#S5.SS1.p5.5 "5.1 Sequence representation for mixed frequencies with embeddings ‣ 5 Implementation of MPTE with nonlinear signals and mixed frequencies ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§5.1](https://arxiv.org/html/2601.16274v1#S5.SS1.p6.4 "5.1 Sequence representation for mixed frequencies with embeddings ‣ 5 Implementation of MPTE with nonlinear signals and mixed frequencies ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"),
  [§5.2](https://arxiv.org/html/2601.16274v1#S5.SS2.p1.1 "5.2 Attention-based nonlinear aggregation and prediction ‣ 5 Implementation of MPTE with nonlinear signals and mixed frequencies ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* D. Wang, X. Liu, and R. Chen (2019)
  Factor models for matrix-valued high-dimensional time series.
  Journal of econometrics 208 (1),  pp. 231–248.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p7.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* K. Weiss, T. M. Khoshgoftaar, and D. Wang (2016)
  A survey of transfer learning.
  Journal of Big data 3 (1),  pp. 9.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p1.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").
* H. Zou, T. Hastie, and R. Tibshirani (2006)
  Sparse principal component analysis.
  Journal of computational and graphical statistics 15 (2),  pp. 265–286.
  Cited by: [§1](https://arxiv.org/html/2601.16274v1#S1.p5.1 "1 Introduction ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").

Supplemental Appendix to
  
“A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"

## Appendix A Proofs

As defined in the main text, let D^(A)≔diag​(λ1(A),…,λk(A))\widehat{D}^{(A)}\coloneqq\text{diag}(\lambda\_{1}^{(A)},\ldots,\lambda\_{k}^{(A)}) be a diagonal matrix of top kk eigenvalues of Z~​Z~T/(Nx+Ny)\widetilde{Z}\widetilde{Z}^{T}/(N\_{x}+N\_{y}), and H(A)H^{(A)} is an invertible k×kk\times k rotation matrix. Theorem 1 is based on the identity used in Bai ([2003](https://arxiv.org/html/2601.16274v1#bib.bib25 "Inferential theory for factor models of large dimensions")) and Duan et al. ([2024](https://arxiv.org/html/2601.16274v1#bib.bib3 "Target pca: transfer learning large dimensional panel data")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ^i(A)−Hi(A)​Λi(A)=1Nx+Ny​(D^(A))−1​∑j=1Nx+Ny(Λ^j(A)​ηi​j+Λ^j(A)​ξi​j+Λ^j(A)​ζi​j+Λ^i(A)​γ​(i,j)),\widehat{\Lambda}\_{i}^{(A)}-H\_{i}^{(A)}\Lambda\_{i}^{(A)}=\frac{1}{N\_{x}+N\_{y}}(\widehat{D}^{(A)})^{-1}\sum\_{j=1}^{N\_{x}+N\_{y}}\Big(\widehat{\Lambda}\_{j}^{(A)}\eta\_{ij}+\widehat{\Lambda}\_{j}^{(A)}\xi\_{ij}+\widehat{\Lambda}\_{j}^{(A)}\zeta\_{ij}+\widehat{\Lambda}\_{i}^{(A)}\gamma(i,j)\Big), |  | (A.1) |

where

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | ηi​j=1T​∑t(Λi(A))⊤​Ft(B)​(B​ej(A))t,\displaystyle\eta\_{ij}=\frac{1}{T}\sum\_{t}(\Lambda\_{i}^{(A)})^{\top}F\_{t}^{(B)}(Be\_{j}^{(A)})\_{t}, |  | ξi​j=1T​∑t(Λj(A))⊤​Ft(B)​(B​ei(A))t,\displaystyle\xi\_{ij}=\frac{1}{T}\sum\_{t}(\Lambda\_{j}^{(A)})^{\top}F\_{t}^{(B)}(Be\_{i}^{(A)})\_{t}, |  | (A.2) |
|  |  | γ​(i,j)=1T​∑t𝔼​[(B​ei(A))t​(B​ej(A))t],\displaystyle\gamma(i,j)=\frac{1}{T}\sum\_{t}\mathbb{E}[(Be\_{i}^{(A)})\_{t}(Be\_{j}^{(A)})\_{t}], |  | ζi​j=1T​∑t(B​ei(A))t​(B​ej(A))t−γ​(i,j).\displaystyle\zeta\_{ij}=\frac{1}{T}\sum\_{t}(Be\_{i}^{(A)})\_{t}(Be\_{j}^{(A)})\_{t}-\gamma(i,j). |  |

To analyze each term above, we need the following lemma.

###### Lemma A.1.

Under Assumptions A.1 - A.8, let α¯=tr​(Az⊤​Az)​‖Az⊤​Az‖F2(Nx+Ny)​‖B‖F4T2\bar{\alpha}=\frac{\text{tr}(A\_{z}^{\top}A\_{z})\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})}\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}, then as T,Nx,Ny→∞T,N\_{x},N\_{y}\rightarrow\infty:

1. 1.

   1(Nx+Ny)2​∑i,j=1Nx+Nyηi​j2=𝒪P​(α¯)\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\eta\_{ij}^{2}=\mathcal{O}\_{P}(\bar{\alpha});
2. 2.

   1(Nx+Ny)2​∑i,j=1Nx+Nyξi​j2=𝒪P​(α¯)\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\xi\_{ij}^{2}=\mathcal{O}\_{P}(\bar{\alpha});
3. 3.

   1(Nx+Ny)2​∑i,j=1Nx+Nyζi​j2=𝒪P​(‖B‖F4T2⋅‖Az⊤​Az‖F2(Nx+Ny)2)\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\zeta\_{ij}^{2}=\mathcal{O}\_{P}\Big(\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}\cdot\frac{\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})^{2}}\Big);
4. 4.

   1(Nx+Ny)2​∑i,j=1Nx+Nyγ2​(i,j)=𝒪P​(‖B‖F4T2⋅‖Az⊤​Az‖F2(Nx+Ny)2)\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\gamma^{2}(i,j)=\mathcal{O}\_{P}\Big(\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}\cdot\frac{\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})^{2}}\Big).

###### Proof.

1. By assumptions A.1-A.8, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[1(Nx+Ny)2​∑i,j=1Nx+Nyηi​j2]\displaystyle\mathbb{E}\Bigg[\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\eta\_{ij}^{2}\Bigg] | =1(Nx+Ny)2​∑i,j=1Nx+Ny𝔼​[(Λi(A))T​1T​∑tFt(B)​(B​ej(A))t]2\displaystyle=\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\mathbb{E}\Bigg[(\Lambda\_{i}^{(A)})^{T}\frac{1}{T}\sum\_{t}F\_{t}^{(B)}(Be\_{j}^{(A)})\_{t}\Bigg]^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤1Nx+Ny​∑i=1Nx+Ny𝔼​‖(Λi(A))T‖2⋅1Nx+Ny​∑j=1Nx+Ny𝔼​‖1T​∑tFt(B)​(B​ej(A))t‖2\displaystyle\leq\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\mathbb{E}\left\lVert(\Lambda\_{i}^{(A)})^{T}\right\rVert^{2}\cdot\frac{1}{N\_{x}+N\_{y}}\sum\_{j=1}^{N\_{x}+N\_{y}}\mathbb{E}\left\lVert\frac{1}{T}\sum\_{t}F\_{t}^{(B)}(Be\_{j}^{(A)})\_{t}\right\rVert^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | [by A.6 and bounded eigenvalues ofΛ⊤​ΛNx+Ny,\displaystyle\Big[\text{by A.6 and bounded eigenvalues of}\ \frac{\Lambda^{\top}\Lambda}{N\_{x}+N\_{y}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | we have∑i=1Nx+Ny𝔼​‖(Λi(A))T‖2Nx+Ny]≤C⋅tr(Az⊤Az)]\displaystyle\text{we have}\ \frac{\sum\_{i=1}^{N\_{x}+N\_{y}}\mathbb{E}\left\lVert(\Lambda\_{i}^{(A)})^{T}\right\rVert^{2}}{N\_{x}+N\_{y}}\Big]\leq C\cdot\text{tr}(A\_{z}^{\top}A\_{z})\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝒪​(tr​(AzT​Az))⋅𝒪​(‖B‖F4⋅‖AzT​Az‖F2T2⋅(Nx+Ny))\displaystyle=\mathcal{O}\Big(\text{tr}(A\_{z}^{T}A\_{z})\Big)\cdot\mathcal{O}\Big(\frac{\left\lVert B\right\rVert^{4}\_{F}\cdot\left\lVert A\_{z}^{T}A\_{z}\right\rVert\_{F}^{2}}{T^{2}\cdot(N\_{x}+N\_{y})}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝒪​(‖B‖F4T2⋅‖AzT​Az‖F2​tr​(AzT​Az)(Nx+Ny))\displaystyle=\mathcal{O}\Big(\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}\cdot\frac{\left\lVert A\_{z}^{T}A\_{z}\right\rVert\_{F}^{2}\text{tr}(A\_{z}^{T}A\_{z})}{(N\_{x}+N\_{y})}\Big) |  |

Hence, under the assumption A.1 that requires ‖B‖F2/T=𝒪​(1)\left\lVert B\right\rVert\_{F}^{2}/T=\mathcal{O}(1),
it holds that 1(Nx+Ny)2​∑i,j=1Nx+Nyηi​j2=𝒪P​(α¯)\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\eta\_{ij}^{2}=\mathcal{O}\_{P}(\bar{\alpha}).

2. By the same arguments, we can show that 1(Nx+Ny)2​∑i,j=1Nx+Nyξi​j2=𝒪P​(α¯)\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\xi\_{ij}^{2}=\mathcal{O}\_{P}(\bar{\alpha}).

3. Using assumptions A.1-A.8, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[1(Nx+Ny)2​∑i,j=1Nx+Nyζi​j2]\displaystyle\mathbb{E}\Bigg[\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\zeta\_{ij}^{2}\Bigg] | =1(Nx+Ny)2​∑i,j=1Nx+Ny𝔼​[1T​∑t((B​ei(A))t​(B​ej(A))t−𝔼​((B​ei(A))t​(B​ej(A))t))]2\displaystyle=\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\mathbb{E}\Bigg[\frac{1}{T}\sum\_{t}\Big((Be\_{i}^{(A)})\_{t}(Be\_{j}^{(A)})\_{t}-\mathbb{E}((Be\_{i}^{(A)})\_{t}(Be\_{j}^{(A)})\_{t})\Big)\Bigg]^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤1(Nx+Ny)2​∑i,j=1Nx+Ny1T​∑t𝔼​((B​ei(A))t​(B​ej(A))t)2\displaystyle\leq\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\frac{1}{T}\sum\_{t}\mathbb{E}\Big((Be\_{i}^{(A)})\_{t}(Be\_{j}^{(A)})\_{t}\Big)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1(Nx+Ny)2​1T​𝔼​‖Az⊤​e⊤​B⊤​B​e​Az‖F2\displaystyle=\frac{1}{(N\_{x}+N\_{y})^{2}}\frac{1}{T}\mathbb{E}\left\lVert A\_{z}^{\top}e^{\top}B^{\top}BeA\_{z}\right\rVert\_{F}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝒪​(‖B‖F4T2⋅‖Az⊤​Az‖F2(Nx+Ny)2),\displaystyle=\mathcal{O}\Big(\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}\cdot\frac{\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})^{2}}\Big), |  |

where the last equality follows from Assumption A.5 and the bounded 8th moments of the transformed errors, which imply 𝔼​‖Az⊤​e⊤​B⊤​B​e​Az‖F2=𝒪​(‖Az⊤​Az‖F2)\mathbb{E}\left\lVert A\_{z}^{\top}e^{\top}B^{\top}BeA\_{z}\right\rVert\_{F}^{2}=\mathcal{O}\Big(\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}\Big).

4. Using assumptions A.1 and A.5, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1(Nx+Ny)2​∑i,j=1Nx+Nyγ2​(i,j)\displaystyle\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\gamma^{2}(i,j) | =1(Nx+Ny)2​∑i,j=1Nx+Ny1T2​(∑t𝔼​[(B​ei(A))t​(B​ej(A))t])2\displaystyle=\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\frac{1}{T^{2}}\Big(\sum\_{t}\mathbb{E}[(Be\_{i}^{(A)})\_{t}(Be\_{j}^{(A)})\_{t}]\Big)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1(Nx+Ny)2​1T2​‖𝔼​[Az⊤​e⊤​B⊤​B​e​Az]‖F2\displaystyle=\frac{1}{(N\_{x}+N\_{y})^{2}}\frac{1}{T^{2}}\left\lVert\mathbb{E}[A\_{z}^{\top}e^{\top}B^{\top}BeA\_{z}]\right\rVert\_{F}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝒪​(‖B‖F4T2⋅‖Az⊤​Az‖F2(Nx+Ny)2).\displaystyle=\mathcal{O}\Big(\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}\cdot\frac{\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})^{2}}\Big). |  |

∎

### A.1 Proof of Theorem 1

(1) Let us first prove 1Nx+Ny​∑i=1Nx+Ny‖Λ^i(A)−H(A)​Λi(A)‖2=𝒪P​(α¯)\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert\widehat{\Lambda}\_{i}^{(A)}-H^{(A)}\Lambda\_{i}^{(A)}\right\rVert^{2}=\mathcal{O}\_{P}(\bar{\alpha}). We have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1Nx+Ny​∑i=1Nx+Ny‖Λ^i(A)−H(A)​Λi(A)‖2\displaystyle\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert\widehat{\Lambda}\_{i}^{(A)}-H^{(A)}\Lambda\_{i}^{(A)}\right\rVert^{2} | ≤1Nx+Ny​∑i=1Nx+Ny‖Λ^i(A)−Hi(A)​Λi(A)‖2\displaystyle\leq\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert\widehat{\Lambda}\_{i}^{(A)}-H\_{i}^{(A)}\Lambda\_{i}^{(A)}\right\rVert^{2} |  | (A.3) |
|  |  | +1Nx+Ny​∑i=1Nx+Ny‖(Hi(A)−H(A))​Λi(A)‖2.\displaystyle+\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert\Big(H\_{i}^{(A)}-H^{(A)}\Big)\Lambda\_{i}^{(A)}\right\rVert^{2}. |  |

To bound the first term on the RHS of ([A.3](https://arxiv.org/html/2601.16274v1#A1.E3 "Equation A.3 ‣ A.1 Proof of Theorem 1 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) we use decomposition ([A.1](https://arxiv.org/html/2601.16274v1#A1.E1 "Equation A.1 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) to get:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 1Nx+Ny​∑i=1Nx+Ny‖Λ^i(A)−H(A)​Λi(A)‖2\displaystyle\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert\widehat{\Lambda}\_{i}^{(A)}-H^{(A)}\Lambda\_{i}^{(A)}\right\rVert^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤4∥(D(A))−1∥2⋅1Nx+Ny∑i=1Nx+Ny1(Nx+Ny)2(∥∑j=1Nx+NyΛ^j(A)ηi​j∥2+∥∑j=1Nx+NyΛ^j(A)ξij∥2\displaystyle\leq 4\left\lVert(D^{(A)})^{-1}\right\rVert^{2}\cdot\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\frac{1}{(N\_{x}+N\_{y})^{2}}\Bigg(\left\lVert\sum\_{j=1}^{N\_{x}+N\_{y}}\widehat{\Lambda}\_{j}^{(A)}\eta\_{ij}\right\rVert^{2}+\left\lVert\sum\_{j=1}^{N\_{x}+N\_{y}}\widehat{\Lambda}\_{j}^{(A)}\xi{ij}\right\rVert^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∥∑j=1Nx+NyΛ^j(A)ζi​j∥2+∥∑j=1Nx+NyΛ^j(A)γ(i,j)∥2)\displaystyle+\left\lVert\sum\_{j=1}^{N\_{x}+N\_{y}}\widehat{\Lambda}\_{j}^{(A)}\zeta\_{ij}\right\rVert^{2}+\left\lVert\sum\_{j=1}^{N\_{x}+N\_{y}}\widehat{\Lambda}\_{j}^{(A)}\gamma(i,j)\right\rVert^{2}\Bigg) |  |

Let ϕi​j=ηi​j,ξi​j,ζi​j,γ​(i,j)\phi\_{ij}=\eta\_{ij},\xi\_{ij},\zeta\_{ij},\gamma(i,j). We bound each term on the RHS using

|  |  |  |
| --- | --- | --- |
|  | 1Nx+Ny​∑i=1Nx+Ny1(Nx+Ny)2​‖∑j=1Nx+NyΛ^j(A)​ϕi​j‖2≤1Nx+Ny​∑j=1Nx+Ny‖Λ^j(A)‖2⏟𝒪P​(1)⋅1(Nx+Ny)2​∑i,j=1Nx+Nyϕi​j2.\displaystyle\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\frac{1}{(N\_{x}+N\_{y})^{2}}\left\lVert\sum\_{j=1}^{N\_{x}+N\_{y}}\widehat{\Lambda}\_{j}^{(A)}\phi\_{ij}\right\rVert^{2}\leq\underbrace{\frac{1}{N\_{x}+N\_{y}}\sum\_{j=1}^{N\_{x}+N\_{y}}\left\lVert\widehat{\Lambda}\_{j}^{(A)}\right\rVert^{2}}\_{\mathcal{O}\_{P}(1)}\cdot\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\phi\_{ij}^{2}. |  |

Hence, using Lemma A.1 and ‖(D(A))−1‖=𝒪​(1)\left\lVert(D^{(A)})^{-1}\right\rVert=\mathcal{O}(1), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1Nx+Ny​∑i=1Nx+Ny‖Λ^i(A)−H(A)​Λi(A)‖2\displaystyle\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert\widehat{\Lambda}\_{i}^{(A)}-H^{(A)}\Lambda\_{i}^{(A)}\right\rVert^{2} | =𝒪(1)⋅(𝒪P(tr​(Az⊤​Az)​‖Az⊤​Az‖F2(Nx+Ny)⋅‖B‖F4T2)\displaystyle=\mathcal{O}(1)\cdot\Big(\mathcal{O}\_{P}\Big(\frac{\text{tr}(A\_{z}^{\top}A\_{z})\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})}\cdot\frac{\|B\|\_{F}^{4}}{T^{2}}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝒪P(‖Az⊤​Az‖F2(Nx+Ny)2⋅‖B‖F4T2))\displaystyle+\mathcal{O}\_{P}\Big(\frac{\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})^{2}}\cdot\frac{\|B\|\_{F}^{4}}{T^{2}}\Big)\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝒪P​(tr​(Az⊤​Az)​‖Az⊤​Az‖F2(Nx+Ny)⋅‖B‖F4T2).\displaystyle=\mathcal{O}\_{P}\Big(\frac{\text{tr}(A\_{z}^{\top}A\_{z})\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})}\cdot\frac{\|B\|\_{F}^{4}}{T^{2}}\Big). |  |

To bound the second term on the RHS of ([A.3](https://arxiv.org/html/2601.16274v1#A1.E3 "Equation A.3 ‣ A.1 Proof of Theorem 1 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) we use decomposition ([A.1](https://arxiv.org/html/2601.16274v1#A1.E1 "Equation A.1 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) to get:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 1Nx+Ny​∑i=1Nx+Ny‖(Hi(A)−H(A))​Λi(A)‖2\displaystyle\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert\Big(H\_{i}^{(A)}-H^{(A)}\Big)\Lambda\_{i}^{(A)}\right\rVert^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1Nx+Ny∑i=1Nx+Ny∥D(A))−1∑j=1Nx+NyΛ^j(A)(Λj(A))T1T(∑tFt(B)(Ft(B))T−Ft(Ft)⊤)Λj(A)∥2\displaystyle=\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert D^{(A)})^{-1}\sum\_{j=1}^{N\_{x}+N\_{y}}\widehat{\Lambda}\_{j}^{(A)}(\Lambda\_{j}^{(A)})^{T}\frac{1}{T}\Big(\sum\_{t}F\_{t}^{(B)}(F\_{t}^{(B)})^{T}-F\_{t}(F\_{t})^{\top}\Big)\Lambda\_{j}^{(A)}\right\rVert^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖(D(A))−1‖2⏟𝒪​(1)⋅(1Nx+Ny​∑j=1Nx+Ny‖Λ^j(A)‖2)⏟𝒪P​(1)⋅\displaystyle\leq\underbrace{\left\lVert(D^{(A)})^{-1}\right\rVert^{2}}\_{\mathcal{O}(1)}\cdot\underbrace{\Big(\frac{1}{N\_{x}+N\_{y}}\sum\_{j=1}^{N\_{x}+N\_{y}}\left\lVert\widehat{\Lambda}\_{j}^{(A)}\right\rVert^{2}\Big)}\_{\mathcal{O}\_{P}(1)}\cdot |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 1(Nx+Ny)2​∑i,j=1Nx+Ny‖Λi(A)‖2​‖Λj(A)‖2⋅‖1T​(∑tFt(B)​(Ft(B))⊤−Ft​(Ft)⊤)‖⏟𝒪P​(tr​(Az⊤​Az)​‖Az⊤​Az‖F2(Nx+Ny)​‖B‖F4T2).\displaystyle\underbrace{\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i,j=1}^{N\_{x}+N\_{y}}\left\lVert\Lambda\_{i}^{(A)}\right\rVert^{2}\left\lVert\Lambda\_{j}^{(A)}\right\rVert^{2}\cdot\left\lVert\frac{1}{T}\Big(\sum\_{t}F\_{t}^{(B)}(F\_{t}^{(B)})^{\top}-F\_{t}(F\_{t})^{\top}\Big)\right\rVert}\_{\mathcal{O}\_{P}\Big(\frac{\text{tr}(A\_{z}^{\top}A\_{z})\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})}\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}\Big)}. |  |

Hence, we conclude that 1Nx+Ny​∑i=1Nx+Ny‖(Hi(A)−H(A))​Λi(A)‖2=𝒪P​(tr​(Az⊤​Az)​‖Az⊤​Az‖F2(Nx+Ny)​‖B‖F4T2)=𝒪P​(α¯)\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert\Big(H\_{i}^{(A)}-H^{(A)}\Big)\Lambda\_{i}^{(A)}\right\rVert^{2}=\mathcal{O}\_{P}\Big(\frac{\text{tr}(A\_{z}^{\top}A\_{z})\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})}\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}\Big)=\mathcal{O}\_{P}(\bar{\alpha}).

Combining the derivations for the two terms, we get 1Nx+Ny​∑i=1Nx+Ny‖Λ^i(A)−H(A)​Λi(A)‖2=𝒪P​(tr​(Az⊤​Az)​‖Az⊤​Az‖F2(Nx+Ny)​‖B‖F4T2)\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert\widehat{\Lambda}\_{i}^{(A)}-H^{(A)}\Lambda\_{i}^{(A)}\right\rVert^{2}=\mathcal{O}\_{P}\Big(\frac{\text{tr}(A\_{z}^{\top}A\_{z})\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})}\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}\Big) as claimed.

Let tr​(Az⊤​Az)=𝒪​(Nα)\text{tr}(A\_{z}^{\top}A\_{z})=\mathcal{O}(N^{\alpha}), and ‖Az⊤​Az‖F2=𝒪​(Nβ)\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}=\mathcal{O}(N^{\beta}). To ensure 𝒪P​(tr​(Az⊤​Az)​‖Az⊤​Az‖F2(Nx+Ny)​‖B‖F4T2)=oP​(1)\mathcal{O}\_{P}\Big(\frac{\text{tr}(A\_{z}^{\top}A\_{z})\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{(N\_{x}+N\_{y})}\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}\Big)=o\_{P}(1), we require α+β<1\alpha+\beta<1. This condition is easily satisfied for low-rank or smooth attention matrices. Furthermore, it allows some spreading among the entries of attention matrix, where the rates are controlled by α\alpha and β\beta.

(2) Let us now prove 1T​∑t=1T‖Ft^(B)−H(A)​Ft(B)‖2=𝒪p​(α¯)\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\widehat{F\_{t}}^{(B)}-H^{(A)}F\_{t}^{(B)}\right\rVert^{2}=\mathcal{O}\_{p}(\bar{\alpha}). Since H(A)H^{(A)} is orthogonal, (H(A)⊤)−1=H(A)(H^{(A)\top})^{-1}=H^{(A)}, it is equivalent to show that 1T​∑t=1T‖Ft^(B)−(H(A)⊤)−1​Ft(B)‖2=𝒪p​(α¯)\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\widehat{F\_{t}}^{(B)}-(H^{(A)\top})^{-1}F\_{t}^{(B)}\right\rVert^{2}=\mathcal{O}\_{p}(\bar{\alpha}).

The estimated factors Ft^(B)\widehat{F\_{t}}^{(B)} are obtained by regressing Z~t​i\widetilde{Z}\_{ti} on the estimated loadings Λ^i(A)\widehat{\Lambda}\_{i}^{(A)}:

|  |  |  |
| --- | --- | --- |
|  | Ft^(B)=(∑i=1Nx+NyΛ^i(A)​(Λ^i(A))⊤)−1​(∑i=1Nx+NyZ~t​i​Λ^i(A)),t=1,⋯,T.\widehat{F\_{t}}^{(B)}=\Bigg(\sum\_{i=1}^{N\_{x}+N\_{y}}\widehat{\Lambda}\_{i}^{(A)}(\widehat{\Lambda}\_{i}^{(A)})^{\top}\Bigg)^{-1}\Bigg(\sum\_{i=1}^{N\_{x}+N\_{y}}\widetilde{Z}\_{ti}\widehat{\Lambda}\_{i}^{(A)}\Bigg),\ t=1,\cdots,T. |  |

Because H(A)H^{(A)} is orthogonal, pre-multiplying by H(A)H^{(A)} preserves Euclidian norms. Define the rotated estimator

|  |  |  |
| --- | --- | --- |
|  | Ft^(B)⁣∗≡H(A)​Ft^(B).\widehat{F\_{t}}^{(B)\*}\equiv H^{(A)}\widehat{F\_{t}}^{(B)}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | ‖Ft^(B)−(H(A)⊤)−1​Ft(B)‖=‖H(A)​Ft^(B)−Ft(B)‖=‖Ft^(B)⁣∗−Ft(B)‖.\left\lVert\widehat{F\_{t}}^{(B)}-(H^{(A)\top})^{-1}F\_{t}^{(B)}\right\rVert=\left\lVert H^{(A)}\widehat{F\_{t}}^{(B)}-F\_{t}^{(B)}\right\rVert=\left\lVert\widehat{F\_{t}}^{(B)\*}-F\_{t}^{(B)}\right\rVert. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=1T‖Ft^(B)−(H(A)⊤)−1​Ft(B)‖2=1T​∑t=1T‖Ft^(B)⁣∗−Ft(B)‖2.\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\widehat{F\_{t}}^{(B)}-(H^{(A)\top})^{-1}F\_{t}^{(B)}\right\rVert^{2}=\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\widehat{F\_{t}}^{(B)\*}-F\_{t}^{(B)}\right\rVert^{2}. |  |

It is therefore sufficient to show

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=1T‖Ft^(B)⁣∗−Ft(B)‖2=𝒪p​(α¯).\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\widehat{F\_{t}}^{(B)\*}-F\_{t}^{(B)}\right\rVert^{2}=\mathcal{O}\_{p}(\bar{\alpha}). |  |

Using the regression representation:

|  |  |  |
| --- | --- | --- |
|  | Z~t​i=Λi(A)⊤​Ft(B)+(B​ei(A))t,\widetilde{Z}\_{ti}=\Lambda\_{i}^{(A)\top}F\_{t}^{(B)}+(Be\_{i}^{(A)})\_{t}, |  |

we define the empirical loadings covariance matrix

|  |  |  |
| --- | --- | --- |
|  | Σ^Λ(A)≡1Nx+Ny​∑i=1Nx+NyΛ^i(A)​Λ^i(A)⊤,ΣΛ(A)≡1Nx+Ny​∑i=1Nx+NyΛi(A)​Λi(A)⊤.\widehat{\Sigma}\_{\Lambda}^{(A)}\equiv\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\widehat{\Lambda}\_{i}^{(A)}\widehat{\Lambda}\_{i}^{(A)\top},\quad\Sigma\_{\Lambda}^{(A)}\equiv\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\Lambda\_{i}^{(A)}\Lambda\_{i}^{(A)\top}. |  |

By Lemma 1 and the eigenvalue separation assumption:

|  |  |  |
| --- | --- | --- |
|  | ‖Σ^Λ(A)−H(A)​ΣΛ(A)​H(A)⊤‖=𝒪p​(α¯),λmin​(ΣΛ(A))>c>0,\left\lVert\widehat{\Sigma}\_{\Lambda}^{(A)}-H^{(A)}\Sigma\_{\Lambda}^{(A)}H^{(A)\top}\right\rVert=\mathcal{O}\_{p}(\bar{\alpha}),\ \lambda\_{\text{min}}(\Sigma\_{\Lambda}^{(A)})>c>0, |  |

so Σ^Λ(A)\widehat{\Sigma}\_{\Lambda}^{(A)} is invertible and its inverse is uniformly bounded in probability.

We can write

|  |  |  |
| --- | --- | --- |
|  | Ft^(B)⁣∗−Ft(B)=M1(A)⋅1Nx+Ny​∑i=1Nx+NyΛi(A)​(B​ei(A))t+M2(A)⋅1Nx+Ny​∑i=1Nx+Ny(Λ^i(A)−H(A)​Λi(A))​Z~t​i,\widehat{F\_{t}}^{(B)\*}-F\_{t}^{(B)}=M\_{1}^{(A)}\cdot\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\Lambda\_{i}^{(A)}(Be\_{i}^{(A)})\_{t}+M\_{2}^{(A)}\cdot\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}(\widehat{\Lambda}\_{i}^{(A)}-H^{(A)}\Lambda\_{i}^{(A)})\widetilde{Z}\_{ti}, |  |

where M1(A)M\_{1}^{(A)} and M2(A)M\_{2}^{(A)} are random k×kk\times k matrices with bounded operator norms ‖M1(A)‖=𝒪P​(1)\left\lVert M\_{1}^{(A)}\right\rVert=\mathcal{O}\_{P}(1) and ‖M2(A)‖=𝒪P​(1)\left\lVert M\_{2}^{(A)}\right\rVert=\mathcal{O}\_{P}(1).

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Ft^(B)⁣∗−Ft(B)‖≤C​(‖1Nx+Ny​∑i=1Nx+NyΛi(A)​(B​ei(A))t‖+‖1Nx+Ny​∑i=1Nx+Ny(Λ^i(A)−H(A)​Λi(A))​Z~t​i‖),\left\lVert\widehat{F\_{t}}^{(B)\*}-F\_{t}^{(B)}\right\rVert\leq C\Bigg(\left\lVert\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\Lambda\_{i}^{(A)}(Be\_{i}^{(A)})\_{t}\right\rVert+\left\lVert\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}(\widehat{\Lambda}\_{i}^{(A)}-H^{(A)}\Lambda\_{i}^{(A)})\widetilde{Z}\_{ti}\right\rVert\Bigg), |  | (A.4) |

hence

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=1T‖Ft^(B)⁣∗−Ft(B)‖2≤C​(I1+I2),\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\widehat{F\_{t}}^{(B)\*}-F\_{t}^{(B)}\right\rVert^{2}\leq C(I\_{1}+I\_{2}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | I1≡1T​∑t=1T‖1Nx+Ny​∑i=1Nx+NyΛi(A)​(B​ei(A))t⏟Qt‖2,I2≡1T​∑t=1T‖1Nx+Ny​∑i=1Nx+Ny(Λ^i(A)−H(A)​Λi(A))​Z~t​i‖2.I\_{1}\equiv\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\underbrace{\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\Lambda\_{i}^{(A)}(Be\_{i}^{(A)})\_{t}}\_{Q\_{t}}\right\rVert^{2},\ I\_{2}\equiv\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}(\widehat{\Lambda}\_{i}^{(A)}-H^{(A)}\Lambda\_{i}^{(A)})\widetilde{Z}\_{ti}\right\rVert^{2}. |  |

We now bound I1I\_{1} and I2I\_{2} separately. To bound the idiosyncratic error term QtQ\_{t} in I1I\_{1}, we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖Qt‖2\displaystyle\mathbb{E}\left\lVert Q\_{t}\right\rVert^{2} | =∑r=1k1(Nx+Ny)2​∑i=1Nx+Ny∑j=1Nx+Ny𝔼​[Λi​r(A)​Λj​r(A)]​𝔼​[(B​ei(A))t​(B​ej(A))t]\displaystyle=\sum\_{r=1}^{k}\frac{1}{(N\_{x}+N\_{y})^{2}}\sum\_{i=1}^{N\_{x}+N\_{y}}\sum\_{j=1}^{N\_{x}+N\_{y}}\mathbb{E}[\Lambda\_{ir}^{(A)}\Lambda\_{jr}^{(A)}]\mathbb{E}[(Be\_{i}^{(A)})\_{t}(Be\_{j}^{(A)})\_{t}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝒪​(tr​(Az⊤​Az)​‖Az⊤​Az‖F2Nx+Ny⋅‖B‖F4T2),\displaystyle=\mathcal{O}\Big(\frac{\text{tr}(A\_{z}^{\top}A\_{z})\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{N\_{x}+N\_{y}}\cdot\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}\Big), |  |

under the moment and weak cross-sectional / time-series dependence assumptions on ei(A)e\_{i}^{(A)} and the growth conditions on the attention matrices AzA\_{z} and BB (Assumptions A.1 - A.8). Hence,

|  |  |  |
| --- | --- | --- |
|  | I1=1T​∑t=1T𝔼​‖Qt‖2=𝒪​(tr​(Az⊤​Az)​‖Az⊤​Az‖F2Nx+Ny⋅‖B‖F4T2).I\_{1}=\frac{1}{T}\sum\_{t=1}^{T}\mathbb{E}\left\lVert Q\_{t}\right\rVert^{2}=\mathcal{O}\Big(\frac{\text{tr}(A\_{z}^{\top}A\_{z})\left\lVert A\_{z}^{\top}A\_{z}\right\rVert\_{F}^{2}}{N\_{x}+N\_{y}}\cdot\frac{\left\lVert B\right\rVert\_{F}^{4}}{T^{2}}\Big). |  |

For the second term in ([A.4](https://arxiv.org/html/2601.16274v1#A1.E4 "Equation A.4 ‣ A.1 Proof of Theorem 1 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")), I2I\_{2}, apply the Cauchy-Schwarz inequality:

|  |  |  |
| --- | --- | --- |
|  | I2≤1T​∑t=1T[1Nx+Ny​∑i=1Nx+NyZ~t​i2]​[1Nx+Ny​∑i=1Nx+Ny‖Λi(A)−H(A)​Λi(A)‖2].I\_{2}\leq\frac{1}{T}\sum\_{t=1}^{T}\Big[\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\widetilde{Z}\_{ti}^{2}\Big]\Big[\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert\Lambda\_{i}^{(A)}-H^{(A)}\Lambda\_{i}^{(A)}\right\rVert^{2}\Big]. |  |

By the factor structure with attention and Assumptions A.1 - A.8, the first bracket is bounded in probability uniformly in tt, and it has the same order as the bound for I1I\_{1}. By Lemma 1:

|  |  |  |
| --- | --- | --- |
|  | 1Nx+Ny​∑i=1Nx+Ny‖Λi(A)−H(A)​Λi(A)‖2=𝒪P​(α¯).\frac{1}{N\_{x}+N\_{y}}\sum\_{i=1}^{N\_{x}+N\_{y}}\left\lVert\Lambda\_{i}^{(A)}-H^{(A)}\Lambda\_{i}^{(A)}\right\rVert^{2}=\mathcal{O}\_{P}(\bar{\alpha}). |  |

Hence, we have I2=𝒪P(α)¯I\_{2}=\mathcal{O}\_{P}(\bar{\alpha)}.

Combining the two bounds bounds, we have

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=1T‖Ft^(B)⁣∗−Ft(B)‖2≤C​(I1+I2)=𝒪p​(α¯).\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\widehat{F\_{t}}^{(B)\*}-F\_{t}^{(B)}\right\rVert^{2}\leq C(I\_{1}+I\_{2})=\mathcal{O}\_{p}(\bar{\alpha}). |  |

Since

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=1T‖Ft^(B)−(H(A)⊤)−1​Ft(B)‖2=1T​∑t=1T‖Ft^(B)⁣∗−Ft(B)‖2,\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\widehat{F\_{t}}^{(B)}-(H^{(A)\top})^{-1}F\_{t}^{(B)}\right\rVert^{2}=\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\widehat{F\_{t}}^{(B)\*}-F\_{t}^{(B)}\right\rVert^{2}, |  |

we conclude 1T​∑t=1T‖Ft^(B)−(H(A)⊤)−1​Ft(B)‖2=𝒪p​(α¯)\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\widehat{F\_{t}}^{(B)}-(H^{(A)\top})^{-1}F\_{t}^{(B)}\right\rVert^{2}=\mathcal{O}\_{p}(\bar{\alpha}) as claimed.

### A.2 Proof of Lemma 1

###### Proof.

Proof of part (a).
Recall that

|  |  |  |
| --- | --- | --- |
|  | Yt(A)=Λy(A)​Ft(B)+ey,t(A,B),Y\_{t}^{(A)}=\Lambda\_{y}^{(A)}F\_{t}^{(B)}+e\_{y,t}^{(A,B)}, |  |

so that the YY-block covariance matrix admits the decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΣY​Y(A)≡𝔼​[Yt(A)​Yt(A)⊤]=Λy(A)​ΣF(B)​Λy(A)⊤+Σe,Y(A,B).\Sigma\_{YY}^{(A)}\equiv\mathbb{E}\!\big[Y\_{t}^{(A)}Y\_{t}^{(A)\top}\big]=\Lambda\_{y}^{(A)}\Sigma\_{F}^{(B)}\Lambda\_{y}^{(A)\top}+\Sigma\_{e,Y}^{(A,B)}. |  | (A.5) |

Partition Λy(A)=(Λys(A),Λy,R(A))\Lambda\_{y}^{(A)}=(\Lambda\_{y\_{s}}^{(A)},\,\Lambda\_{y,R}^{(A)}) and
Ft(B)=(Fy,tS,FtR)F\_{t}^{(B)}=(F\_{y,t}^{S},\,F\_{t}^{R}) conformably with k=kys+kRk=k\_{y\_{s}}+k\_{R}. Writing
ΣF(B)\Sigma\_{F}^{(B)} in block form yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λy(A)​ΣF(B)​Λy(A)⊤\displaystyle\Lambda\_{y}^{(A)}\Sigma\_{F}^{(B)}\Lambda\_{y}^{(A)\top} | =Λys(A)​ΣF,yS​Λys(A)⊤+Λys(A)​ΣF,y​R​Λy,R(A)⊤\displaystyle=\Lambda\_{y\_{s}}^{(A)}\Sigma\_{F,y}^{S}\Lambda\_{y\_{s}}^{(A)\top}+\Lambda\_{y\_{s}}^{(A)}\Sigma\_{F,yR}\Lambda\_{y,R}^{(A)\top} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +Λy,R(A)​ΣF,R​y​Λys(A)⊤+Λy,R(A)​ΣF,R​Λy,R(A)⊤.\displaystyle\quad+\Lambda\_{y,R}^{(A)}\Sigma\_{F,Ry}\Lambda\_{y\_{s}}^{(A)\top}+\Lambda\_{y,R}^{(A)}\Sigma\_{F,R}\Lambda\_{y,R}^{(A)\top}. |  | (A.6) |

Leading eigenvalues.
Let

|  |  |  |
| --- | --- | --- |
|  | Ay≡Λys(A)​(ΣF,yS)1/2.A\_{y}\equiv\Lambda\_{y\_{s}}^{(A)}(\Sigma\_{F,y}^{S})^{1/2}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | Λys(A)​ΣF,yS​Λys(A)⊤=Ay​Ay⊤,\Lambda\_{y\_{s}}^{(A)}\Sigma\_{F,y}^{S}\Lambda\_{y\_{s}}^{(A)\top}=A\_{y}A\_{y}^{\top}, |  |

whose nonzero eigenvalues coincide with those of

|  |  |  |
| --- | --- | --- |
|  | Ay⊤​Ay=(ΣF,yS)1/2​Λys(A)⊤​Λys(A)​(ΣF,yS)1/2.A\_{y}^{\top}A\_{y}=(\Sigma\_{F,y}^{S})^{1/2}\Lambda\_{y\_{s}}^{(A)\top}\Lambda\_{y\_{s}}^{(A)}(\Sigma\_{F,y}^{S})^{1/2}. |  |

By Assumption B.1,

|  |  |  |
| --- | --- | --- |
|  | 1Ny,eff​Λys(A)⊤​Λys(A)→ΣΛys(A)≻0,\frac{1}{N\_{y,\mathrm{eff}}}\Lambda\_{y\_{s}}^{(A)\top}\Lambda\_{y\_{s}}^{(A)}\;\to\;\Sigma\_{\Lambda\_{y\_{s}}}^{(A)}\succ 0, |  |

and ΣF,yS≻0\Sigma\_{F,y}^{S}\succ 0 by assumption. Hence,
Ay⊤​AyA\_{y}^{\top}A\_{y} has exactly kysk\_{y\_{s}} eigenvalues of order Ny,effN\_{y,\mathrm{eff}},
and therefore so does
Λys(A)​ΣF,yS​Λys(A)⊤\Lambda\_{y\_{s}}^{(A)}\Sigma\_{F,y}^{S}\Lambda\_{y\_{s}}^{(A)\top}.

Remainder terms.
By Assumption B.1, the remaining factor directions in the YY block generate eigenvalues of strictly smaller order than Ny,effN\_{y,\mathrm{eff}}. Consequently,
the cross terms and the weak-factor term in ([A.2](https://arxiv.org/html/2601.16274v1#A1.Ex26 "Proof. ‣ A.2 Proof of Lemma 1 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) satisfy

|  |  |  |
| --- | --- | --- |
|  | ‖Λys(A)​ΣF,y​R​Λy,R(A)⊤+Λy,R(A)​ΣF,R​y​Λys(A)⊤+Λy,R(A)​ΣF,R​Λy,R(A)⊤‖op=o​(Ny,eff).\big\|\Lambda\_{y\_{s}}^{(A)}\Sigma\_{F,yR}\Lambda\_{y,R}^{(A)\top}+\Lambda\_{y,R}^{(A)}\Sigma\_{F,Ry}\Lambda\_{y\_{s}}^{(A)\top}+\Lambda\_{y,R}^{(A)}\Sigma\_{F,R}\Lambda\_{y,R}^{(A)\top}\big\|\_{\mathrm{op}}=o(N\_{y,\mathrm{eff}}). |  |

Moreover, by Assumption A.5, the idiosyncratic covariance
Σe,Y(A,B)\Sigma\_{e,Y}^{(A,B)} has eigenvalues uniformly bounded in NN, and thus

|  |  |  |
| --- | --- | --- |
|  | ‖Σe,Y(A,B)‖op=o​(Ny,eff).\|\Sigma\_{e,Y}^{(A,B)}\|\_{\mathrm{op}}=o(N\_{y,\mathrm{eff}}). |  |

Combining with ([A.5](https://arxiv.org/html/2601.16274v1#A1.E5 "Equation A.5 ‣ Proof. ‣ A.2 Proof of Lemma 1 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")), we obtain

|  |  |  |
| --- | --- | --- |
|  | ΣY​Y(A)=Λys(A)​ΣF,yS​Λys(A)⊤+RY,‖RY‖op=o​(Ny,eff).\Sigma\_{YY}^{(A)}=\Lambda\_{y\_{s}}^{(A)}\Sigma\_{F,y}^{S}\Lambda\_{y\_{s}}^{(A)\top}+R\_{Y},\qquad\|R\_{Y}\|\_{\mathrm{op}}=o(N\_{y,\mathrm{eff}}). |  |

Eigenspace identification.
It follows that

|  |  |  |
| --- | --- | --- |
|  | λkys​(ΣY​Y(A))≍Ny,eff,λkys+1​(ΣY​Y(A))=o​(Ny,eff).\lambda\_{k\_{y\_{s}}}\!\big(\Sigma\_{YY}^{(A)}\big)\asymp N\_{y,\mathrm{eff}},\qquad\lambda\_{k\_{y\_{s}}+1}\!\big(\Sigma\_{YY}^{(A)}\big)=o(N\_{y,\mathrm{eff}}). |  |

By the Courant–Fischer min–max theorem, the eigenspace associated with the
kysk\_{y\_{s}} largest eigenvalues of ΣY​Y(A)\Sigma\_{YY}^{(A)} coincides with

|  |  |  |
| --- | --- | --- |
|  | 𝒮Y≡span⁡(Λys(A)).\mathcal{S}\_{Y}\equiv\operatorname{span}\!\big(\Lambda\_{y\_{s}}^{(A)}\big). |  |

This proves part (a).

Proof of part (b).
Let H(A)∈ℝk×kH^{(A)}\in\mathbb{R}^{k\times k} be any orthogonal matrix and partition

|  |  |  |
| --- | --- | --- |
|  | H(A)=[Hys(A)HR(A)],k=kys+kR.H^{(A)}=\begin{bmatrix}H\_{y\_{s}}^{(A)}\\ H\_{R}^{(A)}\end{bmatrix},\qquad k=k\_{y\_{s}}+k\_{R}. |  |

Under rotation, the YY-loadings become
Λy(A)​H(A)⊤\Lambda\_{y}^{(A)}H^{(A)\top}, and the YY-loadings on the first kysk\_{y\_{s}}
coordinates span

|  |  |  |
| --- | --- | --- |
|  | span⁡(Λy(A)​Hys(A)⊤).\operatorname{span}\!\big(\Lambda\_{y}^{(A)}H\_{y\_{s}}^{(A)\top}\big). |  |

Suppose H(A)H^{(A)} yields the same limiting YY-strong eigenspace
𝒮Y\mathcal{S}\_{Y} as in part (a). Then

|  |  |  |
| --- | --- | --- |
|  | span⁡(Λy(A)​Hys(A)⊤)=𝒮Y=span⁡(Λys(A)).\operatorname{span}\!\big(\Lambda\_{y}^{(A)}H\_{y\_{s}}^{(A)\top}\big)=\mathcal{S}\_{Y}=\operatorname{span}\!\big(\Lambda\_{y\_{s}}^{(A)}\big). |  |

Since Λys(A)\Lambda\_{y\_{s}}^{(A)} has rank kysk\_{y\_{s}}, this implies that the row space
of Hys(A)H\_{y\_{s}}^{(A)} is uniquely determined.

Now let H~(A)\widetilde{H}^{(A)} be another orthogonal matrix yielding the same
limiting YY-strong eigenspace. Then

|  |  |  |
| --- | --- | --- |
|  | row⁡(H~ys(A))=row⁡(Hys(A)).\operatorname{row}\!\big(\widetilde{H}\_{y\_{s}}^{(A)}\big)=\operatorname{row}\!\big(H\_{y\_{s}}^{(A)}\big). |  |

Because both matrices have orthonormal rows, there exists an orthogonal
kys×kysk\_{y\_{s}}\times k\_{y\_{s}} matrix QQ such that

|  |  |  |
| --- | --- | --- |
|  | H~ys(A)=Q​Hys(A).\widetilde{H}\_{y\_{s}}^{(A)}=Q\,H\_{y\_{s}}^{(A)}. |  |

Thus, the YY-strong factor coordinates are identified uniquely up to an orthogonal rotation within the kysk\_{y\_{s}}-dimensional subspace, completing the proof.
∎

### A.3 Proof of Theorem 2

###### Proof.

Proof of Part (a):
Fix a YY-unit i∈{1,⋯,Ny}i\in\{1,\cdots,N\_{y}\}. By definition of the transformed model, we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zi,t(A,B)=Λys,i(A)⊤​Fy,tS+ei,t(A,B),t=1,⋯,T.Z\_{i,t}^{(A,B)}=\Lambda\_{y\_{s},i}^{(A)\top}F\_{y,t}^{S}+e\_{i,t}^{(A,B)},\ t=1,\cdots,T. |  | (A.7) |

Here ei,t(A,B)e\_{i,t}^{(A,B)} collects the transformed idiosyncratic error plus any components associated with other factors that are orthogonal to Fy,tSF\_{y,t}^{S}. By the usual orthogonality/identification conditions we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(Fy,tS​ei,t(A,B))=0.\mathbb{E}(F\_{y,t}^{S}e\_{i,t}^{(A,B)})=0. |  |

The estimator Λ^ys,i(A)\widehat{\Lambda}\_{y\_{s},i}^{(A)} is obtained by regressing the transformed series Zi,t(A,B)Z\_{i,t}^{(A,B)} on the estimated YY-strong factor block F^y,tS\widehat{F}\_{y,t}^{S}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ^ys,i(A)=(1T​∑t=1TF^y,tS​F^y,tS⊤)−1​(1T​∑t=1TF^y,tS​Zi,t(A,B)).\widehat{\Lambda}\_{y\_{s},i}^{(A)}=\Big(\frac{1}{T}\sum\_{t=1}^{T}\widehat{F}\_{y,t}^{S}\widehat{F}\_{y,t}^{S\top}\Big)^{-1}\Big(\frac{1}{T}\sum\_{t=1}^{T}\widehat{F}\_{y,t}^{S}Z\_{i,t}^{(A,B)}\Big). |  | (A.8) |

Define the rotated loading estimator:

|  |  |  |
| --- | --- | --- |
|  | Λ~ys,i(A)≡(Hys(A))−1​Λ^ys,i(A),\widetilde{\Lambda}\_{y\_{s},i}^{(A)}\equiv(H\_{y\_{s}}^{(A)})^{-1}\widehat{\Lambda}\_{y\_{s},i}^{(A)}, |  |

and the rotated factor estimator

|  |  |  |
| --- | --- | --- |
|  | F~y,tS=Hys(A)⊤​F^y,tS.\widetilde{F}\_{y,t}^{S}=H\_{y\_{s}}^{(A)\top}\widehat{F}\_{y,t}^{S}. |  |

Since OLS is invariant to non-singular linear transformations of the regressors, ([A.7](https://arxiv.org/html/2601.16274v1#A1.E7 "Equation A.7 ‣ Proof. ‣ A.3 Proof of Theorem 2 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ~ys,i(A)=(1T​∑t=1TF~y,tS​F~y,tS⊤)−1​(1T​∑t=1TF~y,tS​Zi,t(A,B)).\widetilde{\Lambda}\_{y\_{s},i}^{(A)}=\Big(\frac{1}{T}\sum\_{t=1}^{T}\widetilde{F}\_{y,t}^{S}\widetilde{F}\_{y,t}^{S\top}\Big)^{-1}\Big(\frac{1}{T}\sum\_{t=1}^{T}\widetilde{F}\_{y,t}^{S}Z\_{i,t}^{(A,B)}\Big). |  | (A.9) |

From Theorem [1](https://arxiv.org/html/2601.16274v1#Thmthm1 "Theorem 1 (Consistency under general cross-sectional attention). ‣ 3.2 Consistency ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), we know that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T​∑t=1T‖F~y,tS−Fy,tS‖2=𝒪P​(α¯),α¯→0,\frac{1}{T}\sum\_{t=1}^{T}\left\lVert\widetilde{F}\_{y,t}^{S}-F\_{y,t}^{S}\right\rVert^{2}=\mathcal{O}\_{P}(\bar{\alpha}),\ \bar{\alpha}\rightarrow 0, |  | (A.10) |

and that the original rotation has been chosen such that

|  |  |  |
| --- | --- | --- |
|  | F^y,tS≈(Hys(A)⊤)−1​Fy,tS,Λ^ys,i(A)≈Hys(A)​Λys,i(A).\widehat{F}\_{y,t}^{S}\approx(H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S},\ \widehat{\Lambda}\_{y\_{s},i}^{(A)}\approx H\_{y\_{s}}^{(A)}\Lambda\_{y\_{s},i}^{(A)}. |  |

Moreover, by Theorem [1](https://arxiv.org/html/2601.16274v1#Thmthm1 "Theorem 1 (Consistency under general cross-sectional attention). ‣ 3.2 Consistency ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") we may choose the rotation Hys(A)H\_{y\_{s}}^{(A)}
such that F~y,tS=Fy,tS+Δt\widetilde{F}\_{y,t}^{S}=F\_{y,t}^{S}+\Delta\_{t} with
1T​∑t=1T‖Δt‖2=𝒪p​(α¯)\frac{1}{T}\sum\_{t=1}^{T}\|\Delta\_{t}\|^{2}=\mathcal{O}\_{p}(\bar{\alpha}).
We will only use this mean-square rate (rather than a uniform bound).

Under Assumptions A.1-A.6, we have the usual law of large numbers (LLN) for the factors:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T​∑t=1TFy,tS​Fy,tS⊤→𝑝ΣF,y(B),\frac{1}{T}\sum\_{t=1}^{T}F\_{y,t}^{S}F\_{y,t}^{S\top}\xrightarrow[]{p}\Sigma\_{F,y}^{(B)}, |  | (A.11) |

with ΣF,y(B)\Sigma\_{F,y}^{(B)} positive definite.

Substituting ([A.7](https://arxiv.org/html/2601.16274v1#A1.E7 "Equation A.7 ‣ Proof. ‣ A.3 Proof of Theorem 2 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) into ([A.9](https://arxiv.org/html/2601.16274v1#A1.E9 "Equation A.9 ‣ Proof. ‣ A.3 Proof of Theorem 2 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ~ys,i(A)=(1T​∑t=1TF~y,tS​F~y,tS⊤)(−1)​(1T​∑t=1TF~y,tS​Fy,tS⊤​Λys,i(A)+1T​∑t=1TF~y,tS​ei,t(A,B)).\widetilde{\Lambda}\_{y\_{s},i}^{(A)}=\Big(\frac{1}{T}\sum\_{t=1}^{T}\widetilde{F}\_{y,t}^{S}\widetilde{F}\_{y,t}^{S\top}\Big)^{(-1)}\Big(\frac{1}{T}\sum\_{t=1}^{T}\widetilde{F}\_{y,t}^{S}F\_{y,t}^{S\top}\Lambda\_{y\_{s},i}^{(A)}+\frac{1}{T}\sum\_{t=1}^{T}\widetilde{F}\_{y,t}^{S}e\_{i,t}^{(A,B)}\Big). |  | (A.12) |

Let

|  |  |  |
| --- | --- | --- |
|  | Σ^F,y(T)≡1T​∑t=1TF~y,tS​F~y,tS⊤,C^i(T)≡1T​∑t=1TF~y,tS​ei,t(A,B).\widehat{\Sigma}\_{F,y}^{(T)}\equiv\frac{1}{T}\sum\_{t=1}^{T}\widetilde{F}\_{y,t}^{S}\widetilde{F}\_{y,t}^{S\top},\ \widehat{C}\_{i}^{(T)}\equiv\frac{1}{T}\sum\_{t=1}^{T}\widetilde{F}\_{y,t}^{S}e\_{i,t}^{(A,B)}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | Λ~ys,i(A)=Σ^F,y(T)−1​(1T​∑t=1TF~y,tS​Fy,tS⊤​Λys,i(A)+C^i(T)).\widetilde{\Lambda}\_{y\_{s},i}^{(A)}=\widehat{\Sigma}\_{F,y}^{(T)-1}\Bigg(\frac{1}{T}\sum\_{t=1}^{T}\widetilde{F}\_{y,t}^{S}F\_{y,t}^{S\top}\Lambda\_{y\_{s},i}^{(A)}+\widehat{C}\_{i}^{(T)}\Bigg). |  |

Add and subtract ΣF,y(B)​Λys,i(A)\Sigma\_{F,y}^{(B)}\Lambda\_{y\_{s},i}^{(A)}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ~ys,i(A)−Λys,i(A)=Σ^F,y(T)−1​C^i(T)+[Σ^F,y(T)−1​(1T​∑t=1TF~y,tS​Fy,tS⊤−ΣF,y(B))+(Σ^F,y(T)−1−(ΣF,y(B))−1)​ΣF,y(B)]​Λys,i(A).\widetilde{\Lambda}\_{y\_{s},i}^{(A)}-\Lambda\_{y\_{s},i}^{(A)}=\widehat{\Sigma}\_{F,y}^{(T)-1}\widehat{C}\_{i}^{(T)}+\Bigg[\widehat{\Sigma}\_{F,y}^{(T)-1}\Big(\frac{1}{T}\sum\_{t=1}^{T}\widetilde{F}\_{y,t}^{S}F\_{y,t}^{S\top}-\Sigma\_{F,y}^{(B)}\Big)+\Big(\widehat{\Sigma}\_{F,y}^{(T)-1}-(\Sigma\_{F,y}^{(B)})^{-1}\Big)\Sigma\_{F,y}^{(B)}\Bigg]\Lambda\_{y\_{s},i}^{(A)}. |  | (A.13) |

Write F~y,tS=Fy,tS+Δt\widetilde{F}\_{y,t}^{S}=F\_{y,t}^{S}+\Delta\_{t}. Then

|  |  |  |
| --- | --- | --- |
|  | C^i(T)=1T​∑t=1TFy,tS​ei,t(A,B)+1T​∑t=1TΔt​ei,t(A,B).\widehat{C}\_{i}^{(T)}=\frac{1}{T}\sum\_{t=1}^{T}F\_{y,t}^{S}e\_{i,t}^{(A,B)}+\frac{1}{T}\sum\_{t=1}^{T}\Delta\_{t}e\_{i,t}^{(A,B)}. |  |

Similarly,

|  |  |  |
| --- | --- | --- |
|  | Σ^F,y(T)=1T​∑t=1TFy,tS​Fy,tS⊤+1T​∑t=1T(Fy,tS​Δt⊤+Δt​Fy,tS⊤+Δt​Δt⊤).\widehat{\Sigma}\_{F,y}^{(T)}=\frac{1}{T}\sum\_{t=1}^{T}F\_{y,t}^{S}F\_{y,t}^{S\top}+\frac{1}{T}\sum\_{t=1}^{T}\left(F\_{y,t}^{S}\Delta\_{t}^{\top}+\Delta\_{t}F\_{y,t}^{S\top}+\Delta\_{t}\Delta\_{t}^{\top}\right). |  |

Under Assumptions A.1–A.6 and Theorem [1](https://arxiv.org/html/2601.16274v1#Thmthm1 "Theorem 1 (Consistency under general cross-sectional attention). ‣ 3.2 Consistency ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), the perturbation terms are
op​(1)o\_{p}(1) in operator norm, hence Σ^F,y(T)−1=ΣF,y(B)−1+op​(1)\widehat{\Sigma}\_{F,y}^{(T)-1}=\Sigma\_{F,y}^{(B)-1}+o\_{p}(1).
Moreover,

|  |  |  |
| --- | --- | --- |
|  | T​‖1T​∑t=1TΔt​ei,t(A,B)‖≤(1T​∑t=1T‖Δt‖2)1/2​(1T​∑t=1T|ei,t(A,B)|2)1/2=op​(1),\sqrt{T}\Big\|\frac{1}{T}\sum\_{t=1}^{T}\Delta\_{t}e\_{i,t}^{(A,B)}\Big\|\leq\Big(\frac{1}{T}\sum\_{t=1}^{T}\|\Delta\_{t}\|^{2}\Big)^{1/2}\Big(\frac{1}{T}\sum\_{t=1}^{T}|e\_{i,t}^{(A,B)}|^{2}\Big)^{1/2}=o\_{p}(1), |  |

provided T​α¯1/2→0\sqrt{T}\,\bar{\alpha}^{1/2}\to 0.
Therefore,

|  |  |  |
| --- | --- | --- |
|  | T​(Λ~ys,i(A)−Λys,i(A))=ΣF,y(B)−1​(1T​∑t=1TFy,tS​ei,t(A,B))+op​(1).\sqrt{T}\left(\widetilde{\Lambda}\_{y\_{s},i}^{(A)}-\Lambda\_{y\_{s},i}^{(A)}\right)=\Sigma\_{F,y}^{(B)-1}\Big(\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}F\_{y,t}^{S}e\_{i,t}^{(A,B)}\Big)+o\_{p}(1). |  |

Using (i) consistency and rate for F~y,tS\widetilde{F}\_{y,t}^{S} in ([A.10](https://arxiv.org/html/2601.16274v1#A1.E10 "Equation A.10 ‣ Proof. ‣ A.3 Proof of Theorem 2 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")), (ii) moment bounds on Fy,tSF\_{y,t}^{S} and ei,t(A,B)e\_{i,t}^{(A,B)}, and (iii) the growth conditions on α¯\bar{\alpha} imposed by Theorem [1](https://arxiv.org/html/2601.16274v1#Thmthm1 "Theorem 1 (Consistency under general cross-sectional attention). ‣ 3.2 Consistency ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), we obtain ri,T=oP​(1)r\_{i,T}=o\_{P}(1).

Therefore, we have the key stochastic expansion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​(Λ~ys,i(A)−Λys,i(A))=(ΣF,y(B))−1​(1T​∑t=1TFy,tS​ei,t(A,B))+oP​(1).\sqrt{T}(\widetilde{\Lambda}\_{y\_{s},i}^{(A)}-\Lambda\_{y\_{s},i}^{(A)})=(\Sigma\_{F,y}^{(B)})^{-1}\Big(\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}F\_{y,t}^{S}e\_{i,t}^{(A,B)}\Big)+o\_{P}(1). |  | (A.14) |

By assumptions on the time-series dependence (strong mixing, finite moments, and suitable long-run variance), we have

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=1TFy,tS​ei,t(A,B)→𝑑𝒩​(0,Ωy,i(A,B)),\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}F\_{y,t}^{S}e\_{i,t}^{(A,B)}\xrightarrow[]{d}\mathcal{N}(0,\Omega\_{y,i}^{(A,B)}), |  |

where Ωy,i(A,B)=limT→∞Var​(1T​∑t=1TFy,tS​ei,t(A,B))\Omega\_{y,i}^{(A,B)}=\lim\_{T\rightarrow\infty}\text{Var}\Big(\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}F\_{y,t}^{S}e\_{i,t}^{(A,B)}\Big). Combining this with the linearization ([A.14](https://arxiv.org/html/2601.16274v1#A1.E14 "Equation A.14 ‣ Proof. ‣ A.3 Proof of Theorem 2 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​(Λ~ys,i(A)−Λys,i(A))→𝑑𝒩​(0,(ΣF,y(B))−1​Ωy,i(A,B)​(ΣF,y(B))−1).\sqrt{T}(\widetilde{\Lambda}\_{y\_{s},i}^{(A)}-\Lambda\_{y\_{s},i}^{(A)})\xrightarrow[]{d}\mathcal{N}(0,(\Sigma\_{F,y}^{(B)})^{-1}\Omega\_{y,i}^{(A,B)}(\Sigma\_{F,y}^{(B)})^{-1}). |  | (A.15) |

Recall, Λ~ys,i(A)≡(Hys(A))−1​Λ^ys,i(A)\widetilde{\Lambda}\_{y\_{s},i}^{(A)}\equiv(H\_{y\_{s}}^{(A)})^{-1}\widehat{\Lambda}\_{y\_{s},i}^{(A)}. Hence

|  |  |  |
| --- | --- | --- |
|  | T​(Λ^ys,i(A)−Hys(A)​Λys,i(A))=Hys(A)​T​(Λ~ys,i(A)−Λys,i(A)).\sqrt{T}(\widehat{\Lambda}\_{y\_{s},i}^{(A)}-H\_{y\_{s}}^{(A)}\Lambda\_{y\_{s},i}^{(A)})=H\_{y\_{s}}^{(A)}\sqrt{T}(\widetilde{\Lambda}\_{y\_{s},i}^{(A)}-\Lambda\_{y\_{s},i}^{(A)}). |  |

The non-random, full-rank matrix Hys(A)H\_{y\_{s}}^{(A)} just applies a linear transformation to the limiting normal distribution. Therefore, the asymptotic distribution is

|  |  |  |
| --- | --- | --- |
|  | T​(Λ^ys,i(A)−Hys(A)​Λys,i(A))→𝑑𝒩​(0,(ΣF,y(B))−1​Ωy,i(A,B)​(ΣF,y(B))−1).\sqrt{T}(\widehat{\Lambda}\_{y\_{s},i}^{(A)}-H\_{y\_{s}}^{(A)}\Lambda\_{y\_{s},i}^{(A)})\xrightarrow[]{d}\mathcal{N}(0,(\Sigma\_{F,y}^{(B)})^{-1}\Omega\_{y,i}^{(A,B)}(\Sigma\_{F,y}^{(B)})^{-1}). |  |

This concludes the proof of Part (a).

###### Proof of Part (b).

Fix tt. Consider the pooled OLS estimator of the factor vector based on the
transformed panel {Zi,t(A,B)}i=1N\{Z\_{i,t}^{(A,B)}\}\_{i=1}^{N}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^t(B)=(1Neff​∑i=1NΛ^i(A)​Λ^i(A)⊤)−1​(1Neff​∑i=1NΛ^i(A)​Zi,t(A,B)).\widehat{F}\_{t}^{(B)}=\Bigg(\frac{1}{N\_{\mathrm{eff}}}\sum\_{i=1}^{N}\widehat{\Lambda}\_{i}^{(A)}\widehat{\Lambda}\_{i}^{(A)\top}\Bigg)^{-1}\Bigg(\frac{1}{N\_{\mathrm{eff}}}\sum\_{i=1}^{N}\widehat{\Lambda}\_{i}^{(A)}Z\_{i,t}^{(A,B)}\Bigg). |  | (A.16) |

Define the rotated estimators

|  |  |  |
| --- | --- | --- |
|  | F~t(B)≡H(A)⊤​F^t(B),Λ~i(A)≡(H(A))−1​Λ^i(A).\widetilde{F}\_{t}^{(B)}\equiv H^{(A)\top}\widehat{F}\_{t}^{(B)},\qquad\widetilde{\Lambda}\_{i}^{(A)}\equiv(H^{(A)})^{-1}\widehat{\Lambda}\_{i}^{(A)}. |  |

By invariance of OLS to nonsingular linear transformations of the regressors,
([A.16](https://arxiv.org/html/2601.16274v1#A1.E16 "Equation A.16 ‣ Proof of Part (b). ‣ Proof. ‣ A.3 Proof of Theorem 2 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | F~t(B)=(1Neff​∑i=1NΛ~i(A)​Λ~i(A)⊤)−1​(1Neff​∑i=1NΛ~i(A)​Zi,t(A,B)).\widetilde{F}\_{t}^{(B)}=\Bigg(\frac{1}{N\_{\mathrm{eff}}}\sum\_{i=1}^{N}\widetilde{\Lambda}\_{i}^{(A)}\widetilde{\Lambda}\_{i}^{(A)\top}\Bigg)^{-1}\Bigg(\frac{1}{N\_{\mathrm{eff}}}\sum\_{i=1}^{N}\widetilde{\Lambda}\_{i}^{(A)}Z\_{i,t}^{(A,B)}\Bigg). |  | (A.17) |

Using the transformed factor representation

|  |  |  |
| --- | --- | --- |
|  | Zi,t(A,B)=Λi(A)⊤​Ft(B)+ei,t(A,B),Z\_{i,t}^{(A,B)}=\Lambda\_{i}^{(A)\top}F\_{t}^{(B)}+e\_{i,t}^{(A,B)}, |  |

substituting into ([A.17](https://arxiv.org/html/2601.16274v1#A1.E17 "Equation A.17 ‣ Proof of Part (b). ‣ Proof. ‣ A.3 Proof of Theorem 2 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | F~t(B)=Σ^Λ(N)−1​(1Neff​∑i=1NΛ~i(A)​Λi(A)⊤​Ft(B)+1Neff​∑i=1NΛ~i(A)​ei,t(A,B)),\widetilde{F}\_{t}^{(B)}=\widehat{\Sigma}\_{\Lambda}^{(N)-1}\Bigg(\frac{1}{N\_{\mathrm{eff}}}\sum\_{i=1}^{N}\widetilde{\Lambda}\_{i}^{(A)}\Lambda\_{i}^{(A)\top}F\_{t}^{(B)}+\frac{1}{N\_{\mathrm{eff}}}\sum\_{i=1}^{N}\widetilde{\Lambda}\_{i}^{(A)}e\_{i,t}^{(A,B)}\Bigg), |  | (A.18) |

where

|  |  |  |
| --- | --- | --- |
|  | Σ^Λ(N)≡1Neff​∑i=1NΛ~i(A)​Λ~i(A)⊤.\widehat{\Sigma}\_{\Lambda}^{(N)}\equiv\frac{1}{N\_{\mathrm{eff}}}\sum\_{i=1}^{N}\widetilde{\Lambda}\_{i}^{(A)}\widetilde{\Lambda}\_{i}^{(A)\top}. |  |

By Theorem [1](https://arxiv.org/html/2601.16274v1#Thmthm1 "Theorem 1 (Consistency under general cross-sectional attention). ‣ 3.2 Consistency ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") and the cross-sectional law of large numbers,

|  |  |  |
| --- | --- | --- |
|  | Σ^Λ(N)→𝑝ΣΛ(A),Σ^Λ(N)−1→𝑝ΣΛ(A)−1.\widehat{\Sigma}\_{\Lambda}^{(N)}\xrightarrow{p}\Sigma\_{\Lambda}^{(A)},\qquad\widehat{\Sigma}\_{\Lambda}^{(N)-1}\xrightarrow{p}\Sigma\_{\Lambda}^{(A)-1}. |  |

Assumption B.3(i) guarantees identification of the YY-strong factor subspace
from the YY block, while Assumptions B.3(ii)–(iv) imply that the auxiliary
XX block contributes non-negligibly to the YY-strong loading covariance at
the NeffN\_{\mathrm{eff}} scale without fully spanning that space.

Let SyS\_{y} denote the selection matrix extracting the YY-strong block, and define

|  |  |  |
| --- | --- | --- |
|  | F~y,tS=Sy​F~t(B),Fy,tS=Sy​Ft(B),Λi,ys(A)=Sy​Λi(A).\widetilde{F}\_{y,t}^{S}=S\_{y}\widetilde{F}\_{t}^{(B)},\qquad F\_{y,t}^{S}=S\_{y}F\_{t}^{(B)},\qquad\Lambda\_{i,y\_{s}}^{(A)}=S\_{y}\Lambda\_{i}^{(A)}. |  |

Premultiplying ([A.18](https://arxiv.org/html/2601.16274v1#A1.E18 "Equation A.18 ‣ Proof of Part (b). ‣ Proof. ‣ A.3 Proof of Theorem 2 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) by SyS\_{y} and adding and subtracting
ΣΛ,ys(A)​Fy,tS\Sigma\_{\Lambda,y\_{s}}^{(A)}F\_{y,t}^{S}, where

|  |  |  |
| --- | --- | --- |
|  | ΣΛ,ys(A)=limNeff→∞1Neff​∑i=1NΛi,ys(A)​Λi,ys(A)⊤,\Sigma\_{\Lambda,y\_{s}}^{(A)}=\lim\_{N\_{\mathrm{eff}}\to\infty}\frac{1}{N\_{\mathrm{eff}}}\sum\_{i=1}^{N}\Lambda\_{i,y\_{s}}^{(A)}\Lambda\_{i,y\_{s}}^{(A)\top}, |  |

we obtain the stochastic expansion

|  |  |  |  |
| --- | --- | --- | --- |
|  | Neff​(F~y,tS−Fy,tS)=(ΣΛ,ys(A))−1​(1Neff​∑i=1NΛi,ys(A)​ei,t(A,B))+op​(1),\sqrt{N\_{\mathrm{eff}}}\bigl(\widetilde{F}\_{y,t}^{S}-F\_{y,t}^{S}\bigr)=(\Sigma\_{\Lambda,y\_{s}}^{(A)})^{-1}\Bigg(\frac{1}{\sqrt{N\_{\mathrm{eff}}}}\sum\_{i=1}^{N}\Lambda\_{i,y\_{s}}^{(A)}e\_{i,t}^{(A,B)}\Bigg)+o\_{p}(1), |  | (A.19) |

under the growth condition Neff​α¯→0\sqrt{N\_{\mathrm{eff}}}\,\bar{\alpha}\to 0.

By the cross-sectional central limit theorem in Assumptions A.1–A.8,

|  |  |  |
| --- | --- | --- |
|  | 1Neff​∑i=1NΛi,ys(A)​ei,t(A,B)→𝑑𝒩​(0,Ξys,t(A,B)).\frac{1}{\sqrt{N\_{\mathrm{eff}}}}\sum\_{i=1}^{N}\Lambda\_{i,y\_{s}}^{(A)}e\_{i,t}^{(A,B)}\xrightarrow{d}\mathcal{N}\!\bigl(0,\Xi\_{y\_{s},t}^{(A,B)}\bigr). |  |

Combining this with ([A.19](https://arxiv.org/html/2601.16274v1#A1.E19 "Equation A.19 ‣ Proof of Part (b). ‣ Proof. ‣ A.3 Proof of Theorem 2 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) and using
F~y,tS=Hys(A)⊤​F^y,tS\widetilde{F}\_{y,t}^{S}=H\_{y\_{s}}^{(A)\top}\widehat{F}\_{y,t}^{S}, we conclude that

|  |  |  |
| --- | --- | --- |
|  | Neff​(F^y,tS−(Hys(A)⊤)−1​Fy,tS)→𝑑𝒩​(0,VF,t(A,B)),\sqrt{N\_{\mathrm{eff}}}\Big(\widehat{F}\_{y,t}^{S}-(H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\Big)\xrightarrow{d}\mathcal{N}\!\bigl(0,V\_{F,t}^{(A,B)}\bigr), |  |

where

|  |  |  |
| --- | --- | --- |
|  | VF,t(A,B)=(ΣΛ,ys(A))−1​Ξys,t(A,B)​(ΣΛ,ys(A))−1.V\_{F,t}^{(A,B)}=(\Sigma\_{\Lambda,y\_{s}}^{(A)})^{-1}\Xi\_{y\_{s},t}^{(A,B)}(\Sigma\_{\Lambda,y\_{s}}^{(A)})^{-1}. |  |

This completes the proof.
∎

∎

### A.4 Proof of Theorem 3

###### Proof.

Fix a YY-unit i∈{1,…,Ny}i\in\{1,\ldots,N\_{y}\} and a time index tt.
Recall the definitions

|  |  |  |
| --- | --- | --- |
|  | Cy,i,t≡Λys,i(A)⊤​Fy,tS,C^y,i,t≡Λ^ys,i(A)⊤​F^y,tS.C\_{y,i,t}\equiv\Lambda\_{y\_{s},i}^{(A)\top}F\_{y,t}^{S},\qquad\widehat{C}\_{y,i,t}\equiv\widehat{\Lambda}\_{y\_{s},i}^{(A)\top}\widehat{F}\_{y,t}^{S}. |  |

By the usual add-and-subtract argument and Lemma 1 (rotation alignment), we obtain the linear expansion

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^y,i,t−Cy,i,t=ΔF,i​t+ΔΛ,i​t+ri,t,\widehat{C}\_{y,i,t}-C\_{y,i,t}=\Delta\_{F,it}+\Delta\_{\Lambda,it}+r\_{i,t}, |  | (A.20) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΔF,i​t\displaystyle\Delta\_{F,it} | ≡Λys,i(A)⊤​(F^y,tS−(Hys(A)⊤)−1​Fy,tS),\displaystyle\equiv\Lambda\_{y\_{s},i}^{(A)\top}\Big(\widehat{F}\_{y,t}^{S}-(H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\Big), |  | (A.21) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΔΛ,i​t\displaystyle\Delta\_{\Lambda,it} | ≡(Λ^ys,i(A)−Hys(A)​Λys,i(A))⊤​(Hys(A)⊤)−1​Fy,tS,\displaystyle\equiv\Big(\widehat{\Lambda}\_{y\_{s},i}^{(A)}-H\_{y\_{s}}^{(A)}\Lambda\_{y\_{s},i}^{(A)}\Big)^{\top}(H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}, |  | (A.22) |

and the remainder term collects the product of the two estimation errors:

|  |  |  |
| --- | --- | --- |
|  | ri,t=(Λ^ys,i(A)−Hys(A)​Λys,i(A))⊤​(F^y,tS−(Hys(A)⊤)−1​Fy,tS).r\_{i,t}=\Big(\widehat{\Lambda}\_{y\_{s},i}^{(A)}-H\_{y\_{s}}^{(A)}\Lambda\_{y\_{s},i}^{(A)}\Big)^{\top}\Big(\widehat{F}\_{y,t}^{S}-(H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\Big). |  |

Using Theorem [2](https://arxiv.org/html/2601.16274v1#Thmthm2 "Theorem 2 (Asymptotic distribution of loadings and factors under general cross-sectional attention). ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data") and bounded moments of Λys,i(A)\Lambda\_{y\_{s},i}^{(A)} and
Fy,tSF\_{y,t}^{S}, we have

|  |  |  |
| --- | --- | --- |
|  | ΔF,i​t=𝒪p​(Neff−1/2),ΔΛ,i​t=𝒪p​(T−1/2),\Delta\_{F,it}=\mathcal{O}\_{p}(N\_{\mathrm{eff}}^{-1/2}),\qquad\Delta\_{\Lambda,it}=\mathcal{O}\_{p}(T^{-1/2}), |  |

and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri,t=𝒪p​(T−1/2)⋅𝒪p​(Neff−1/2)=op​(T−1/2+Neff−1/2).r\_{i,t}=\mathcal{O}\_{p}(T^{-1/2})\cdot\mathcal{O}\_{p}(N\_{\mathrm{eff}}^{-1/2})=o\_{p}(T^{-1/2}+N\_{\mathrm{eff}}^{-1/2}). |  | (A.23) |

Limits of the two leading terms.
From Theorem [2](https://arxiv.org/html/2601.16274v1#Thmthm2 "Theorem 2 (Asymptotic distribution of loadings and factors under general cross-sectional attention). ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")(b) and linearity,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Neff​ΔF,i​t=Λys,i(A)⊤​Neff​(F^y,tS−(Hys(A)⊤)−1​Fy,tS)→𝑑𝒩​(0,σC,i​t,F2),\sqrt{N\_{\mathrm{eff}}}\,\Delta\_{F,it}=\Lambda\_{y\_{s},i}^{(A)\top}\sqrt{N\_{\mathrm{eff}}}\Big(\widehat{F}\_{y,t}^{S}-(H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\Big)\xrightarrow{d}\mathcal{N}\big(0,\sigma^{2}\_{C,it,F}\big), |  | (A.24) |

where σC,i​t,F2≡Λys,i(A)⊤​VF,t(A,B)​Λys,i(A)\sigma^{2}\_{C,it,F}\equiv\Lambda\_{y\_{s},i}^{(A)\top}V\_{F,t}^{(A,B)}\Lambda\_{y\_{s},i}^{(A)}.
Similarly, Theorem [2](https://arxiv.org/html/2601.16274v1#Thmthm2 "Theorem 2 (Asymptotic distribution of loadings and factors under general cross-sectional attention). ‣ 3.3 Asymptotic normality ‣ 3 Inferential theory ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")(a) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​ΔΛ,i​t=((Hys(A)⊤)−1​Fy,tS)⊤​T​(Λ^ys,i(A)−Hys(A)​Λys,i(A))→𝑑𝒩​(0,σC,i​t,Λ2),\sqrt{T}\,\Delta\_{\Lambda,it}=\Big((H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\Big)^{\top}\sqrt{T}\Big(\widehat{\Lambda}\_{y\_{s},i}^{(A)}-H\_{y\_{s}}^{(A)}\Lambda\_{y\_{s},i}^{(A)}\Big)\xrightarrow{d}\mathcal{N}\big(0,\sigma^{2}\_{C,it,\Lambda}\big), |  | (A.25) |

where

|  |  |  |
| --- | --- | --- |
|  | σC,i​t,Λ2≡((Hys(A)⊤)−1​Fy,tS)⊤​VΛ,y,i(A,B)​((Hys(A)⊤)−1​Fy,tS).\sigma^{2}\_{C,it,\Lambda}\equiv\Big((H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\Big)^{\top}V\_{\Lambda,y,i}^{(A,B)}\Big((H\_{y\_{s}}^{(A)\top})^{-1}F\_{y,t}^{S}\Big). |  |

Proof of Part (i) (FF-dominant regime).
Assume Neff/T→0N\_{\mathrm{eff}}/T\to 0. Multiply ([A.20](https://arxiv.org/html/2601.16274v1#A1.E20 "Equation A.20 ‣ Proof. ‣ A.4 Proof of Theorem 3 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) by Neff\sqrt{N\_{\mathrm{eff}}}:

|  |  |  |
| --- | --- | --- |
|  | Neff​(C^y,i,t−Cy,i,t)=Neff​ΔF,i​t+Neff​ΔΛ,i​t+Neff​ri,t.\sqrt{N\_{\mathrm{eff}}}\,(\widehat{C}\_{y,i,t}-C\_{y,i,t})=\sqrt{N\_{\mathrm{eff}}}\Delta\_{F,it}+\sqrt{N\_{\mathrm{eff}}}\Delta\_{\Lambda,it}+\sqrt{N\_{\mathrm{eff}}}r\_{i,t}. |  |

Since ΔΛ,i​t=𝒪p​(T−1/2)\Delta\_{\Lambda,it}=\mathcal{O}\_{p}(T^{-1/2}), we have
Neff​ΔΛ,i​t=𝒪p​(Neff/T)=op​(1)\sqrt{N\_{\mathrm{eff}}}\Delta\_{\Lambda,it}=\mathcal{O}\_{p}(\sqrt{N\_{\mathrm{eff}}/T})=o\_{p}(1).
Moreover, by ([A.23](https://arxiv.org/html/2601.16274v1#A1.E23 "Equation A.23 ‣ Proof. ‣ A.4 Proof of Theorem 3 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")),

|  |  |  |
| --- | --- | --- |
|  | Neff​ri,t=op​(1+Neff/T)=op​(1).\sqrt{N\_{\mathrm{eff}}}r\_{i,t}=o\_{p}\!\Big(1+\sqrt{N\_{\mathrm{eff}}/T}\Big)=o\_{p}(1). |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | Neff​(C^y,i,t−Cy,i,t)=Neff​ΔF,i​t+op​(1),\sqrt{N\_{\mathrm{eff}}}\,(\widehat{C}\_{y,i,t}-C\_{y,i,t})=\sqrt{N\_{\mathrm{eff}}}\Delta\_{F,it}+o\_{p}(1), |  |

and the conclusion follows from ([A.24](https://arxiv.org/html/2601.16274v1#A1.E24 "Equation A.24 ‣ Proof. ‣ A.4 Proof of Theorem 3 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) and Slutsky’s theorem.

Proof of Part (ii) (Λ\Lambda-dominant regime).
Assume T/Neff→0T/N\_{\mathrm{eff}}\to 0. Multiply ([A.20](https://arxiv.org/html/2601.16274v1#A1.E20 "Equation A.20 ‣ Proof. ‣ A.4 Proof of Theorem 3 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) by T\sqrt{T}:

|  |  |  |
| --- | --- | --- |
|  | T​(C^y,i,t−Cy,i,t)=T​ΔF,i​t+T​ΔΛ,i​t+T​ri,t.\sqrt{T}\,(\widehat{C}\_{y,i,t}-C\_{y,i,t})=\sqrt{T}\Delta\_{F,it}+\sqrt{T}\Delta\_{\Lambda,it}+\sqrt{T}r\_{i,t}. |  |

Since ΔF,i​t=𝒪p​(Neff−1/2)\Delta\_{F,it}=\mathcal{O}\_{p}(N\_{\mathrm{eff}}^{-1/2}), we have
T​ΔF,i​t=𝒪p​(T/Neff)=op​(1)\sqrt{T}\Delta\_{F,it}=\mathcal{O}\_{p}(\sqrt{T/N\_{\mathrm{eff}}})=o\_{p}(1).
Also, by ([A.23](https://arxiv.org/html/2601.16274v1#A1.E23 "Equation A.23 ‣ Proof. ‣ A.4 Proof of Theorem 3 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")),

|  |  |  |
| --- | --- | --- |
|  | T​ri,t=op​(T/Neff+1)=op​(1).\sqrt{T}r\_{i,t}=o\_{p}\!\Big(\sqrt{T/N\_{\mathrm{eff}}}+1\Big)=o\_{p}(1). |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | T​(C^y,i,t−Cy,i,t)=T​ΔΛ,i​t+op​(1),\sqrt{T}\,(\widehat{C}\_{y,i,t}-C\_{y,i,t})=\sqrt{T}\Delta\_{\Lambda,it}+o\_{p}(1), |  |

and the conclusion follows from ([A.25](https://arxiv.org/html/2601.16274v1#A1.E25 "Equation A.25 ‣ Proof. ‣ A.4 Proof of Theorem 3 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) and Slutsky’s theorem.

Proof of Part (iii) (mixed regime).
Assume Neff/T→c∈(0,∞)N\_{\mathrm{eff}}/T\to c\in(0,\infty) and impose Assumption B.4, so that
the leading factor score and loading score are asymptotically orthogonal.
Multiplying ([A.20](https://arxiv.org/html/2601.16274v1#A1.E20 "Equation A.20 ‣ Proof. ‣ A.4 Proof of Theorem 3 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")) by T\sqrt{T} gives

|  |  |  |
| --- | --- | --- |
|  | T​(C^y,i,t−Cy,i,t)=T​ΔΛ,i​t+T​ΔF,i​t+T​ri,t.\sqrt{T}\,(\widehat{C}\_{y,i,t}-C\_{y,i,t})=\sqrt{T}\Delta\_{\Lambda,it}+\sqrt{T}\Delta\_{F,it}+\sqrt{T}r\_{i,t}. |  |

Under Neff/T→cN\_{\mathrm{eff}}/T\to c, we can rewrite

|  |  |  |
| --- | --- | --- |
|  | T​ΔF,i​t=TNeff​(Neff​ΔF,i​t)⇒𝒩​(0,c​σC,i​t,F2),\sqrt{T}\Delta\_{F,it}=\sqrt{\frac{T}{N\_{\mathrm{eff}}}}\,\Big(\sqrt{N\_{\mathrm{eff}}}\Delta\_{F,it}\Big)\;\Rightarrow\;\mathcal{N}\Big(0,\,c\,\sigma^{2}\_{C,it,F}\Big), |  |

and by ([A.23](https://arxiv.org/html/2601.16274v1#A1.E23 "Equation A.23 ‣ Proof. ‣ A.4 Proof of Theorem 3 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")), T​ri,t=op​(1)\sqrt{T}r\_{i,t}=o\_{p}(1). By ([A.25](https://arxiv.org/html/2601.16274v1#A1.E25 "Equation A.25 ‣ Proof. ‣ A.4 Proof of Theorem 3 ‣ Appendix A Proofs ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data")),
T​ΔΛ,i​t⇒𝒩​(0,σC,i​t,Λ2)\sqrt{T}\Delta\_{\Lambda,it}\Rightarrow\mathcal{N}(0,\sigma^{2}\_{C,it,\Lambda}).
Assumption B.4 implies the asymptotic covariance between
T​ΔF,i​t\sqrt{T}\Delta\_{F,it} and T​ΔΛ,i​t\sqrt{T}\Delta\_{\Lambda,it} is zero.
Therefore, by the Cramér–Wold device,

|  |  |  |
| --- | --- | --- |
|  | T​(C^y,i,t−Cy,i,t)⇒𝒩​(0,σC,i​t,Λ2+c​σC,i​t,F2),\sqrt{T}\,(\widehat{C}\_{y,i,t}-C\_{y,i,t})\Rightarrow\mathcal{N}\big(0,\sigma^{2}\_{C,it,\Lambda}+c\,\sigma^{2}\_{C,it,F}\big), |  |

which is the claim in Part (iii).
∎

## Appendix B Diebold–Mariano tests and Model Confidence Set results

| Target | MIDAS | AR | OLS | XGB | NN |
| --- | --- | --- | --- | --- | --- |
| GDPC1 | 1.26 | -0.79 | -1.43 | -0.16 | -1.91 |
| GPDIC1 | -1.11 | 0.40 | -1.81 | 0.12 | -1.85 |
| PCECC96 | 1.68 | 0.77 | -1.38 | 1.62 | -1.69 |
| DPIC96 | 1.98 | 1.09 | -2.20 | 0.39 | -2.37 |
| OUTNFB | -0.71 | -1.27 | -1.66 | -0.72 | -3.23 |
| UNRATE | 1.37 | -0.40 | -2.29 | 0.45 | -0.35 |
| PCECTPI | -0.06 | 1.01 | -2.53 | -1.79 | -3.43 |
| PCEPILFE | -1.38 | 0.06 | -1.68 | -0.45 | -2.99 |
| CPIAUCSL | -0.96 | 0.08 | -2.07 | -2.06 | -2.29 |
| CPILFESL | -1.39 | -0.29 | -1.82 | 1.86 | -3.76 |
| FPIx | -1.66 | 0.89 | -1.43 | 1.20 | -2.01 |
| EXPGSC1 | -1.54 | -0.42 | -2.24 | 0.97 | -2.63 |
| IMPGSC1 | -1.02 | 0.22 | -2.65 | 0.69 | -4.71 |

Table 7: Diebold–Mariano test statistics comparing MPTE against competing models. Each entry reports the Diebold–Mariano statistic for the null hypothesis of equal predictive accuracy between MPTE and the corresponding competing model for the given target series. Negative values indicate lower forecast loss for MPTE relative to the competing model, while positive values indicate superior performance of the competing model.




Table 8: MCS inclusion for baseline models

| target | MPTE | MIDAS | AR | OLS | XGB | NN |
| --- | --- | --- | --- | --- | --- | --- |
| GDPC1 | ✓ | ✓ | – | ✓ | ✓ | ✓ |
| GPDIC1 | ✓ | ✓ | – | ✓ | ✓ | ✓ |
| PCECC96 | ✓ | ✓ | – | ✓ | ✓ | ✓ |
| DPIC96 | ✓ | ✓ | – | ✓ | ✓ | ✓ |
| OUTNFB | ✓ | ✓ | – | ✓ | ✓ | ✓ |
| UNRATE | ✓ | ✓ | – | ✓ | ✓ | ✓ |
| PCECTPI | ✓ | ✓ | – | ✓ | ✓ | – |
| PCEPILFE | ✓ | ✓ | – | ✓ | ✓ | ✓ |
| CPIAUCSL | ✓ | – | – | ✓ | ✓ | ✓ |
| CPILFESL | ✓ | ✓ | – | ✓ | ✓ | – |
| FPIx | ✓ | ✓ | – | ✓ | ✓ | ✓ |
| EXPGSC1 | ✓ | ✓ | – | ✓ | ✓ | ✓ |
| IMPGSC1 | ✓ | ✓ | – | ✓ | ✓ | – |

Table 9: Model Confidence Set (MCS) inclusion for MPTE and competing models across target series at the 95% confidence level. A checkmark indicates that the corresponding model is included in the MCS for the given target, while “–” denotes exclusion.




Table 10: Diebold–Mariano tests: Transformer vs ablations

| Target | AB1 | AB2 | AB3 | AB4 | AB5 |
| --- | --- | --- | --- | --- | --- |
| GDPC1 | -0.96 | -0.99 | -0.92 | -0.88 | 1.09 |
| GPDIC1 | 1.76 | 0.40 | 0.41 | -0.01 | -0.61 |
| PCECC96 | 1.29 | -0.08 | 1.04 | 1.26 | 0.49 |
| DPIC96 | 1.03 | 1.62 | 1.60 | 1.07 | 0.06 |
| OUTNFB | -1.06 | -1.31 | -1.34 | -1.42 | -1.27 |
| UNRATE | 1.18 | 3.23 | -0.89 | 0.09 | 0.08 |
| PCECTPI | -1.66 | 0.98 | 1.00 | 1.04 | 0.73 |
| PCEPILFE | 0.10 | 0.08 | -0.08 | -0.16 | -0.99 |
| CPIAUCSL | 1.11 | 0.07 | -0.00 | -0.02 | 1.40 |
| CPILFESL | -0.39 | -0.39 | -1.14 | -0.26 | -0.77 |
| FPIx | 0.21 | 0.35 | -1.23 | -1.05 | -0.88 |
| EXPGSC1 | -0.45 | -0.35 | -0.29 | -0.56 | -0.57 |
| IMPGSC1 | 1.18 | 0.24 | 0.27 | 0.01 | 0.13 |

Table 11: Diebold–Mariano test statistics comparing MPTE against ablation models. Each entry reports the Diebold–Mariano statistic for the null hypothesis of equal predictive accuracy between MPTE and the corresponding ablation for the given target series. Negative values indicate lower forecast loss for MPTE relative to the ablation, while positive values indicate superior performance of the ablation.



| target | MPTE | AB1 | AB2 | AB3 | AB4 | AB5 |
| --- | --- | --- | --- | --- | --- | --- |
| GDPC1 | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| GPDIC1 | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| PCECC96 | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| DPIC96 | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| OUTNFB | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| UNRATE | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| PCECTPI | ✓ | – | ✓ | ✓ | – | ✓ |
| PCEPILFE | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| CPIAUCSL | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| CPILFESL | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| FPIx | ✓ | ✓ | ✓ | – | – | ✓ |
| EXPGSC1 | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| IMPGSC1 | ✓ | ✓ | ✓ | ✓ | – | ✓ |

Table 12: Model Confidence Set (MCS) inclusion for MPTE and its ablation variants across target series at the 95% confidence level. A checkmark indicates that the corresponding specification is included in the MCS for the given target, while “–” denotes exclusion.

## Appendix C Hyperparameter selection

We select hyperparameters for MPTE using automated hyperparameter optimization implemented through the Optuna framework.444<https://optuna.org/> Optuna employs a tree-structured Parzen estimator to explore the hyperparameter space efficiently by iteratively proposing configurations that are more likely to improve validation performance. We perform hyperparameter tuning separately for each forecast target and, when applicable, for each ablation variant. In all cases, the optimization objective is the mean squared error computed on a validation subsample extracted from the training set using a temporal split, and we apply early stopping to mitigate overfitting.

The set of hyperparameters subject to optimization is the same across experimental settings, simulated and empirical, while the admissible ranges and the number of optimization trials differ. For the simulation exercises in Section [6](https://arxiv.org/html/2601.16274v1#S6 "6 Simulation evidence on attention-based mixed-frequency estimation ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data"), we adopt a broad search space that spans both low- and high-capacity architectures in order to assess model performance across a wide range of configurations. In this setting, we optimize the model dimension, the number of attention heads, the number of transformer layers, the dropout rate, the learning rate, the embedding dimensions for variables and frequencies, the feedforward network size, and the activation function. For the empirical analysis, we restrict the search space to higher-capacity architectures and increase the number of optimization trials to ensure adequate exploration of the parameter space. We make informed design choices in defining this search space. In particular, we limit the range of dropout rates, as excessive regularization can be detrimental in relatively short macroeconomic samples, and we do not optimize the embedding dimensions for variables and frequencies. Instead, we set them deterministically as a logarithmic function of the corresponding vocabulary sizes, ensuring that embedding dimensions remain comparable across targets and ablation variants while avoiding additional tuning parameters that could confound the interpretation of attention patterns.

|  |  |
| --- | --- |
| Hyperparameter | Search Space |
| dmodeld\_{\text{model}} | {16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512} |
| Number of heads (nheadn\_{\text{head}}) | {1, 2, 4, 8} |
| Number of layers | {1, 2, 3, 4} |
| Dropout | {0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5} |
| Learning rate | {1e-5, 3e-5, 1e-4, 3e-4, 5e-4, 1e-3} |
| dfreqd\_{\text{freq}} | {2, 4, 8, 16, 32, 128} |
| dvard\_{\text{var}} | {4, 8, 16, 32, 64, 128} |
| Feedforward dimension | {32, 64, 128, 256} |
| Activation function | {relu, gelu} |
| Number of trials | 20 |

Table 13: Hyperparameter search space used in the simulation exercises.



| Hyperparameter | Search Space |
| --- | --- |
| dmodeld\_{\text{model}} | {128, 192, 256, 384, 512, 1024} |
| Number of heads (nheadn\_{\text{head}}) | {1, 2, 4, 8, 16} |
| Number of layers | {1, 2, 3} |
| Dropout | {0.0, 0.05, 0.1, 0.15} |
| Learning rate | {1e-5, 3e-5, 1e-4, 3e-4, 5e-4} |
| Feedforward dimension | {8, 16, 32, 64, 128, 256, 512, 1024} |
| Activation function | {relu, gelu} |
| Number of trials | 500 |

Table 14: Hyperparameter search space used in the empirical forecasting exercises (full MPTE).

For the ablation experiments, we deliberately restrict hyperparameter optimization to preserve architectural comparability across model variants. We re-optimize only training-related hyperparameters, namely the learning rate and the dropout rate, using the same candidate values considered in the empirical analysis, while fixing all remaining architectural parameters at the values selected for the corresponding full MPTE. We limit the number of optimization trials to a small budget to avoid introducing additional variability across ablations. This design choice ensures that differences in performance and attention patterns across ablations reflect the removal of specific model components rather than changes in overall model capacity. In particular, fixing the embedding dimensions, attention configuration, and network depth preserves the scale and structure of the attention matrices, allowing for a meaningful comparison of attention-based aggregation mechanisms across model variants, which we do in Section [7](https://arxiv.org/html/2601.16274v1#S7 "7 Empirical evidence from U.S. macroeconomic data ‣ A Nonlinear Target-Factor Model with Attention Mechanism for Mixed-Frequency Data").

For the competing benchmark models, we adopt standard and model-specific tuning procedures that reflect common practice in the forecasting literature. We estimate the AR model separately for each target series, with the lag order selected in-sample using the BIC. The MIDAS specification is estimated without hyperparameter optimization: we fix the lag structure ex ante (4 lags for each regressor), and we obtain the model parameters by nonlinear least squares using the default estimation routine in the midasr R package. Increasing the number of lags in a data-scarce setting, such as macroeconomics, would quickly undermine estimation reliability, as the resulting proliferation of parameters would exceed the effective information content of the available sample.
For the single-frequency machine-learning benchmarks, we apply limited validation-based hyperparameter selection on a per-target basis. In particular, for XGB we tune the number of trees, tree depth, and learning rate over a small predefined search space using a temporally ordered validation split. For the feedforward neural network, we analogously tune the learning rate and hidden-layer widths over a small set of candidate configurations, again selecting the specification that minimizes validation loss.

## Appendix D List of monthly and quarterly variables

| Mnemonic | Category | Description |
| --- | --- | --- |
| RPI | Output | Real Personal Income |
| INDPRO | Output | Industrial Production Index |
| CUMFNS | Output | Capacity Utilization: Manufacturing |
| HWI | Labor | Help-Wanted Index |
| CLF16OV | Labor | Civilian Labor Force |
| CE16OV | Labor | Civilian Employment |
| UEMPMEAN | Labor | Average Duration of Unemployment |
| CLAIMSx | Labor | Initial Unemployment Claims |
| PAYEMS | Labor | Total Nonfarm Payroll Employment |
| CES0600000007 | Labor | Avg. Weekly Hours, Goods-Producing |
| CES0600000008 | Labor | Avg. Hourly Earnings, Goods-Producing |
| CES2000000008 | Labor | Avg. Hourly Earnings, Construction |
| CES3000000008 | Labor | Avg. Hourly Earnings, Manufacturing |
| AWOTMAN | Labor | Avg. Weekly Overtime Hours, Manufacturing |
| AWHMAN | Labor | Avg. Weekly Hours, Manufacturing |
| HOUST | Housing | Housing Starts |
| DPCERA3M086SBEA | Consumption | Real Personal Consumption Expenditures |
| BUSINVx | Inventories | Total Business Inventories |
| RETAILx | Consumption | Retail and Food Services Sales |
| CMRMTSPLx | Output | Real Manufacturing and Trade Sales |
| M2REAL | Money | Real M2 Money Stock |
| TOTRESNS | Money | Total Reserves of Depository Institutions |
| BUSLOANS | Credit | Commercial and Industrial Loans |
| NONREVSL | Credit | Nonrevolving Consumer Credit |
| FEDFUNDS | Rates | Effective Federal Funds Rate |
| GS1 | Rates | 1-Year Treasury Yield |
| GS10 | Rates | 10-Year Treasury Yield |
| BAA | Rates | Moody’s Baa Corporate Bond Yield |
| PCEPI | Prices | PCE Price Index |
| WPSFD49207 | Prices | PPI: Finished Goods |
| OILPRICEx | Prices | Crude Oil Price (WTI, Spliced) |
| S&P 500 | Financial | S&P 500 Stock Index |
| S&P PE ratio | Financial | S&P 500 Price–Earnings Ratio |
| TB3MS | Rates | 3-Month Treasury Bill Rate |
| TB6MS | Rates | 6-Month Treasury Bill Rate |

Table 15: Monthly macroeconomic regressors used in the empirical analysis. Variable definitions follow standard FRED descriptions.



| Mnemonic | Category | Description |
| --- | --- | --- |
| GDPC1 | Output | Real Gross Domestic Product |
| GPDIC1 | Investment | Real Gross Private Domestic Investment |
| PCECC96 | Consumption | Real Personal Consumption Expenditures |
| DPIC96 | Income | Real Disposable Personal Income |
| OUTNFB | Output | Nonfarm Business Sector Output |
| UNRATE | Labor | Civilian Unemployment Rate |
| PCECTPI | Prices | PCE Chain-Type Price Index |
| PCEPILFE | Prices | PCE Price Index Less Food and Energy |
| CPIAUCSL | Prices | CPI for All Urban Consumers |
| CPILFESL | Prices | CPI Less Food and Energy |
| FPIx | Prices | Fixed Investment Price Index |
| EXPGSC1 | Trade | Real Exports of Goods and Services |
| IMPGSC1 | Trade | Real Imports of Goods and Services |

Table 16: Quarterly macroeconomic variables used as targets and predictors. Variable definitions follow standard FRED descriptions.