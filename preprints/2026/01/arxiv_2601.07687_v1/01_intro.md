---
authors:
- Efstratios Manolakis
- Christian Bongiorno
- Rosario Nunzio Mantegna
doc_id: arxiv:2601.07687v1
family_id: arxiv:2601.07687
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting
  in Financial Markets
url_abs: http://arxiv.org/abs/2601.07687v1
url_html: https://arxiv.org/html/2601.07687v1
venue: arXiv q-fin
version: 1
year: 2026
---


Efstratios Manolakis
  
Università di Catania, Dipartimento di Fisica e Astronomia “Ettore Majorana”
  
Catania, Italy
  
efstratios.manolakis@phd.unict.it
  
&Christian Bongiorno
  
Université Paris-Saclay, CentraleSupélec,
  
Mathématiques et Informatique pour la Complexité et les Systèmes,
  
91190, Gif-sur-Yvette, France
  
christian.bongiorno@centralesupelec.fr
  
  
Rosario Nunzio Mantegna
  
Università degli Studi di Palermo, Dipartimento di Fisica e Chimica "Emilio Segrè"
  
Palermo, Italy
  
Complexity Science Hub
  
Vienna, Austria
  
rosario.mantegna@unipa.it

###### Abstract

A new wave of work on covariance cleaning and nonlinear shrinkage has delivered asymptotically optimal analytical solutions for large covariance matrices. Building on this progress, these ideas have been generalized to empirical cross–covariance matrices, whose singular-value shrinkage characterizes comovements between one set of assets and another. Existing analytical cross-covariance cleaners are derived under strong stationarity and large-sample assumptions, and they typically rely on mesoscopic regularity conditions such as bounded spectra; macroscopic common modes (e.g., a global market factor) violate these conditions. When applied to real equity returns, where dependence structures drift over time and global modes are prominent, we find that these theoretically optimal formulas do not translate into robust out-of-sample performance. We address this gap by designing a random-matrix-inspired neural architecture that operates in the empirical singular-vector basis and learns a nonlinear mapping from empirical singular values to their corresponding cleaned values. By construction, the network can recover the analytical solution as a special case, yet it remains flexible enough to adapt to non-stationary dynamics and mode-driven distortions. Trained on a long history of equity returns, the proposed method achieves a more favorable bias–variance trade-off than purely analytical cleaners and delivers systematically lower out-of-sample cross–covariance prediction errors. Our results demonstrate that combining random-matrix theory with machine learning makes asymptotic theories practically effective in realistic time-varying markets.

*K*eywords Spectral Tokenization ⋅\cdot
Random Matrix Theory ⋅\cdot
Equivariant Neural Networks ⋅\cdot
Nonlinear Shrinkage ⋅\cdot
Non-Stationary Dependence

## 1 Introduction

Empirical cross–covariance matrices provide a compact way to summarize how two groups of variables move together. Consider two zero–mean random vectors, 𝐗∈ℝnx\mathbf{X}\in\mathbb{R}^{n\_{x}} and 𝐘∈ℝny\mathbf{Y}\in\mathbb{R}^{n\_{y}}, observed over a time window of length Δ​tin\Delta t\_{\textrm{in}}. Their cross–covariance matrix 𝚺X​Y\mathbf{\Sigma}\_{XY} contains the expected products between components of 𝐗\mathbf{X} and 𝐘\mathbf{Y}, and can therefore be interpreted as a linear measure of co-movement. It indicates which fluctuations in one set of variables tend to be associated with fluctuations in the other. In empirical applications, 𝚺X​Y\mathbf{\Sigma}\_{XY} is not known and must be estimated from the Δ​tin\Delta t\_{\textrm{in}} paired observations available in the window.

A fundamental challenge arises when the number of variables is not small compared to the window length. In such high–dimensional regimes, the empirical estimator is heavily affected by sampling noise where apparent relationships may emerge purely by chance, and the resulting estimate can behave unreliably when evaluated Out-Of-Sample (OOS) [[9](https://arxiv.org/html/2601.07687v1#bib.bib13 "The effect of errors in means, variances, and covariances on optimal portfolio choice")]. For standard covariance matrices, this issue has been studied extensively, and a large body of work has developed principled denoising strategies, often based on spectral methods and Random Matrix Theory (RMT), to separate stable structure from noise [[7](https://arxiv.org/html/2601.07687v1#bib.bib12 "Cleaning large correlation matrices: tools from random matrix theory")]. The cross–covariance setting is less straightforward. When nx≠nyn\_{x}\neq n\_{y}, the matrix 𝚺X​Y∈ℝnx×ny\mathbf{\Sigma}\_{XY}\in\mathbb{R}^{n\_{x}\times n\_{y}} is rectangular, so the usual eigenvalue-based tools do not apply directly. Instead, one must work with a singular value decomposition. While singular-value filtering provides a natural analogue of covariance cleaning, the corresponding theoretical framework for choosing optimal shrinkage rules is comparatively less mature, and its effectiveness, in realistic time-varying systems, remains an open question.

Related denoising results exist for additive-noise models [[17](https://arxiv.org/html/2601.07687v1#bib.bib4 "Optimal denoising of rotationally invariant rectangular matrices"), [11](https://arxiv.org/html/2601.07687v1#bib.bib9 "Optimal shrinkage of singular values")], but sample (cross-)covariances arise from products of observations and therefore call for a multiplicative-noise cleaning framework. To the best of our knowledge, the only available analytical characterization of an asymptotically optimal singular-value shrinkage for empirical cross-covariance matrices under multiplicative noise is due to Benaych-Georges, Bouchaud, and Potters (BBP) [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")]. In the high-dimensional asymptotic regime, they derive a Rotationally Invariant Estimator (RIE) that preserves the empirical singular vectors of 𝚺^X​Y\widehat{\mathbf{\Sigma}}\_{XY} while shrinking its singular values so as to minimize the asymptotic Mean Squared Error (MSE) relative to the true cross-covariance 𝚺X​Y\mathbf{\Sigma}\_{XY}. Their result is presented in two versions: a baseline setting with identity marginals (𝚺X​X=𝐈nx\mathbf{\Sigma}\_{XX}=\mathbf{I}\_{n\_{x}} and 𝚺Y​Y=𝐈ny\mathbf{\Sigma}\_{YY}=\mathbf{I}\_{n\_{y}}), which also covers the practically relevant case of whitened variables, and a more general setting that incorporates non-trivial marginal covariances into the optimal correction. The theory is validated through simulations and controlled benchmarks, but it does not consider real financial data and relies on strong stationarity assumptions that are rarely met in practice.

The impact of non-stationarity is already well documented in the simpler covariance case. Bongiorno, Challet and Loper [[3](https://arxiv.org/html/2601.07687v1#bib.bib6 "Filtering time-dependent covariance matrices using time-independent eigenvalues")] show that covariance–shrinkage estimators derived under stationarity assumptions can underperform naive asset–agnostic shrinkages when tested on real markets. In particular, they report that shrinkage-based portfolios may be dominated OOS by simple strategies such as the Average Oracle, which is calibrated on outdated returns and yet evaluated on more recent data, and that this behaviour is robust across different datasets and markets.

In the covariance setting, the mismatch between analytically optimal shrinkage rules and the empirical non-stationarity of financial data has been mitigated through physics-informed neural network architectures that embed the random-matrix solution as a limiting case [[5](https://arxiv.org/html/2601.07687v1#bib.bib7 "End-to-end large portfolio optimization for variance minimization with neural networks through covariance cleaning"), [6](https://arxiv.org/html/2601.07687v1#bib.bib8 "Neural network-driven volatility drag mitigation under aggressive leverage")]. In these approaches, the RMT shrinkage is recast as a constrained network that remains expressive enough to recover the asymptotically optimal filter under stationarity, while gaining flexibility via additional trainable degrees of freedom to operate beyond that regime. A key element is the explicit enforcement of the problem’s symmetries, notably the rotationally invariant structure implied by RMT. Trained on rolling windows, the model learns to interpolate between a denoising behavior effective in quasi-stationary periods and a predictive correction that captures persistent time variation, yielding improved OOS performance relative to purely analytical shrinkage and naive baselines. Moreover, the neural formulation naturally accommodates decision-aware training. Rather than optimizing an MSE on covariance entries, one can directly minimize an objective aligned with the downstream portfolio loss [[4](https://arxiv.org/html/2601.07687v1#bib.bib10 "Non-linear shrinkage of the price return covariance matrix is far from optimal for portfolio optimization"), [13](https://arxiv.org/html/2601.07687v1#bib.bib11 "Estimating covariance for global minimum variance portfolio: a decision-focused learning approach")], thereby linking statistical estimation to the relevant economic criterion.

In this work, we introduce a physics-informed learning framework for cross–covariance estimation that preserves the rotational invariances of RMT while operating beyond the stationarity and boundedness regimes required by existing analytical shrinkage. The key idea is to parameterize the cleaned estimator directly in the empirical singular-vector basis and to learn a dimension-agnostic nonlinear map from empirical singular values and marginal projections to cleaned singular values, so that the BBP correction is recovered as a limiting case, but additional degrees of freedom can accommodate macroscopic modes and time variation. Empirically, we observe that the analytically optimal BBP shrinkage can lose robustness on equity returns as the universe size increases in the presence of a dominant market mode, whereas the proposed symmetry-preserving estimator remains stable and yields lower OOS reconstruction error, including in OOS matrix sizes.

## 2 Two-Stream Architecture for Cross–Covariance Cleaning

We start from the empirical cross-correlation 𝐂^X​Y∈ℝnx×ny\widehat{\mathbf{C}}\_{XY}\in\mathbb{R}^{n\_{x}\times n\_{y}} computed on a window of length Δ​tin\Delta t\_{\textrm{in}}, together with the marginal empirical correlations 𝐂^X​X\widehat{\mathbf{C}}\_{XX} and 𝐂^Y​Y\widehat{\mathbf{C}}\_{YY}. Let r:=min⁡(nx,ny)r:=\min(n\_{x},n\_{y}) and write the Singular Value Decomposition (SVD)

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂^X​Y=∑k=1rs^k​𝐮^k​𝐯^k⊤.\widehat{\mathbf{C}}\_{XY}=\sum\_{k=1}^{r}\widehat{s}\_{k}\,\widehat{\mathbf{u}}\_{k}\widehat{\mathbf{v}}\_{k}^{\top}. |  | (1) |

When needed, we complete {𝐮^k}k=1r\{\widehat{\mathbf{u}}\_{k}\}\_{k=1}^{r} and {𝐯^k}k=1r\{\widehat{\mathbf{v}}\_{k}\}\_{k=1}^{r} to orthonormal bases of ℝnx\mathbb{R}^{n\_{x}} and ℝny\mathbb{R}^{n\_{y}}; the extra directions correspond to zero singular values.
A RIE keeps the empirical singular vectors {𝐮^k,𝐯^k}\{\widehat{\mathbf{u}}\_{k},\widehat{\mathbf{v}}\_{k}\} and replaces each s^k↦s~k\widehat{s}\_{k}\mapsto\widetilde{s}\_{k} by a cleaned value.

Motivated by the structure of BBP shrinkage [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")], the correction should depend on the empirical singular spectrum and on how marginal energy projects onto the corresponding singular directions. We therefore define the marginal projections

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ^k(x):=𝐮^k⊤​𝐂^X​X​𝐮^k,k=1,…,nx,γ^k(y):=𝐯^k⊤​𝐂^Y​Y​𝐯^k,k=1,…,ny,\widehat{\gamma}^{(x)}\_{k}:=\widehat{\mathbf{u}}\_{k}^{\top}\widehat{\mathbf{C}}\_{XX}\widehat{\mathbf{u}}\_{k},\qquad k=1,\ldots,n\_{x},\qquad\qquad\widehat{\gamma}^{(y)}\_{k}:=\widehat{\mathbf{v}}\_{k}^{\top}\widehat{\mathbf{C}}\_{YY}\widehat{\mathbf{v}}\_{k},\qquad k=1,\ldots,n\_{y}, |  | (2) |

and the aspect ratios qx:=nx/Δ​tinq\_{x}:=n\_{x}/\Delta t\_{\textrm{in}} and qy:=ny/Δ​tinq\_{y}:=n\_{y}/\Delta t\_{\textrm{in}}. When nx≠nyn\_{x}\neq n\_{y}, only the first rr singular values are nonzero, while the larger side retains additional marginal directions that enter BBP-type functionals.

To expose this information as a single aligned sequence, we set p:=max⁡(nx,ny)p:=\max(n\_{x},n\_{y}) and define padded scalars for k=1,…,pk=1,\ldots,p,

|  |  |  |  |
| --- | --- | --- | --- |
|  | s¯k:={s^k,k≤r,0,k>r,γ¯k(x):={γ^k(x),k≤nx,0,k>nx,γ¯k(y):={γ^k(y),k≤ny,0,k>ny.\overline{s}\_{k}:=\begin{cases}\widehat{s}\_{k},&k\leq r,\\ 0,&k>r,\end{cases}\qquad\overline{\gamma}^{(x)}\_{k}:=\begin{cases}\widehat{\gamma}^{(x)}\_{k},&k\leq n\_{x},\\ 0,&k>n\_{x},\end{cases}\qquad\overline{\gamma}^{(y)}\_{k}:=\begin{cases}\widehat{\gamma}^{(y)}\_{k},&k\leq n\_{y},\\ 0,&k>n\_{y}.\end{cases} |  | (3) |

In particular, for k>rk>r one has s¯k=0\overline{s}\_{k}=0 by construction, while γ¯k(x)\overline{\gamma}^{(x)}\_{k} (resp. γ¯k(y)\overline{\gamma}^{(y)}\_{k}) can remain nonzero up to k=nxk=n\_{x} (resp. k=nyk=n\_{y}), making the rectangular extra-marginal information explicit.

For each k∈{1,…,p}k\in\{1,\ldots,p\} we build two stream-specific tokens

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝉k(x):=[γ¯k(x),s¯k,qx]⊤,𝝉k(y):=[γ¯k(y),s¯k,qy]⊤.\boldsymbol{\tau}^{(x)}\_{k}:=\bigl[\overline{\gamma}^{(x)}\_{k},\ \overline{s}\_{k},\ q\_{x}\bigr]^{\top},\qquad\boldsymbol{\tau}^{(y)}\_{k}:=\bigl[\overline{\gamma}^{(y)}\_{k},\ \overline{s}\_{k},\ q\_{y}\bigr]^{\top}. |  | (4) |

A shared encoder EθE\_{\theta}, implemented as a token-wise two-layer Multi-Layer-Perceptron (MLP) with a 16-unit hidden layer and LeakyReLU activation, maps each token to a 2-dimensional embedding

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐞k(x)=Eθ​(𝝉k(x))∈ℝ2,𝐞k(y)=Eθ​(𝝉k(y))∈ℝ2.\mathbf{e}^{(x)}\_{k}=E\_{\theta}(\boldsymbol{\tau}^{(x)}\_{k})\in\mathbb{R}^{2},\qquad\mathbf{e}^{(y)}\_{k}=E\_{\theta}(\boldsymbol{\tau}^{(y)}\_{k})\in\mathbb{R}^{2}. |  | (5) |

Then, we fuse the two streams additively,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐳k=𝐞k(x)+𝐞k(y),k=1,…,p,\mathbf{z}\_{k}=\mathbf{e}^{(x)}\_{k}+\mathbf{e}^{(y)}\_{k},\qquad k=1,\ldots,p, |  | (6) |

and pass the sequence (𝐳1,…,𝐳p)(\mathbf{z}\_{1},\ldots,\mathbf{z}\_{p}) through a two-layer bidirectional LSTM aggregator (hidden sizes 128 and 64).
This yields context-aware states (𝐡1,…,𝐡p)(\mathbf{h}\_{1},\ldots,\mathbf{h}\_{p}) that provide each index with global spectral context [[5](https://arxiv.org/html/2601.07687v1#bib.bib7 "End-to-end large portfolio optimization for variance minimization with neural networks through covariance cleaning")].

A pointwise head gθg\_{\theta}, implemented as a token-wise two-layer MLP with a 252-unit hidden layer and LeakyReLU activation, maps each state to a scalar residual correction δk=gθ​(𝐡k)\delta\_{k}=g\_{\theta}(\mathbf{h}\_{k}). We keep only the first rr corrections and define the cleaned singular values by the additive parametrization

|  |  |  |  |
| --- | --- | --- | --- |
|  | s~k=s^k+δk,k=1,…,r.\widetilde{s}\_{k}=\widehat{s}\_{k}+\delta\_{k},\qquad k=1,\ldots,r. |  | (7) |

See Appendix [5](https://arxiv.org/html/2601.07687v1#S5 "5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") for a step-by-step derivation showing that BBP is recovered as a special case.

Alternatively, one may enforce a bounded multiplicative correction via s~k=s^k​σ​(δk)\widetilde{s}\_{k}=\widehat{s}\_{k}\,\sigma(\delta\_{k}), where σ​(⋅)\sigma(\cdot) denotes the logistic sigmoid, which guarantees 0≤s~k≤s^k0\leq\widetilde{s}\_{k}\leq\widehat{s}\_{k} (see Appendix [5.3](https://arxiv.org/html/2601.07687v1#S5.SS3 "5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") and [8.4](https://arxiv.org/html/2601.07687v1#S8.SS4 "8.4 Feasibility Diagnostic via Canonical-Correlation Boundedness ‣ 8 Market Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") for more details). In our experiments, however, this constrained parametrization led to slightly more difficult optimization, and we therefore adopt the additive form. To provide a clearer conceptual overview of the integrated components and the associated data flow, we illustrate the architecture in Figure [1](https://arxiv.org/html/2601.07687v1#S2.F1 "Figure 1 ‣ 2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").

![Refer to caption](x1.png)


Figure 1: Flowchart of the neural singular value cleaning architecture. The diagram illustrates the construction of dual-stream tokens from marginal projections γ¯\overline{\gamma} and singular values s¯\overline{s}, their transformation through a shared encoder EθE\_{\theta}, and the global context aggregation via a bidirectional LSTM and pointwise head gθg\_{\theta} to produce the final additive corrections δk\delta\_{k}.

Finally, we reconstruct the cleaned cross-covariance by plugging Eq. ([7](https://arxiv.org/html/2601.07687v1#S2.E7 "In 2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) in Eq. ([1](https://arxiv.org/html/2601.07687v1#S2.E1 "In 2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) and rescaling with the marginal sample standard deviations,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺~X​Y=𝑫^X​𝐂~X​Y​𝑫^Y.\widetilde{\boldsymbol{\Sigma}}\_{XY}=\widehat{\boldsymbol{D}}\_{X}\widetilde{\mathbf{C}}\_{XY}\widehat{\boldsymbol{D}}\_{Y}. |  | (8) |

In this work, we train in the cross-correlation domain to isolate multivariate filtering, but the same pipeline can be optimized end-to-end for cross-covariances by including the rescaling in the objective. For supervision, given an OOS target 𝐂X​YOOS\mathbf{C}^{\mathrm{OOS}}\_{XY} computed on the subsequent window of length Δ​tout\Delta t\_{\mathrm{out}}, we minimize the MSE, i,e., the squared Frobenius loss

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(θ)=1nx​ny​‖𝐂~X​Y−𝐂X​YOOS‖F2.\mathcal{L}(\theta)=\frac{1}{n\_{x}n\_{y}}\,\bigl\|\widetilde{\mathbf{C}}\_{XY}-\mathbf{C}^{\mathrm{OOS}}\_{XY}\bigr\|\_{F}^{2}. |  | (9) |

The network has 331,355331{,}355 learnable parameters, independent of (nx,ny,Δ​tin)(n\_{x},n\_{y},\Delta t\_{\textrm{in}}). It can be trained at one range of dimensions and deployed at other sizes without retraining. Moreover, it is equivariant to permutations of the XX and YY coordinates. A Python implementation is available on GitHub [[10](https://arxiv.org/html/2601.07687v1#bib.bib27 "CrossRIE")]

## 3 Validation on Synthetic and Market Data

To assess our Neural Network (NN) based estimator, we first benchmark it on synthetic datasets that reproduce the spectral regimes of finite-rank signals and heavy-tailed noise under which the BBP shrinkage is derived [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")]. These experiments therefore constitute a favorable setting for the analytical method, relying on stylized assumptions such as identity auto-covariance blocks that are mathematically convenient yet seldom satisfied in financial data. As reported in Table[1](https://arxiv.org/html/2601.07687v1#S3.T1 "Table 1 ‣ 3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"), our estimator matches the BBP performance across these validation tests, indicating that, in stationary regimes where the theoretical assumptions hold, the network can recover the optimal rotationally invariant filtration without introducing spurious structure. We further add a fourth benchmark in which a macroscopic one-factor mode is injected into the population correlation matrix 𝑪\boldsymbol{C}, thereby violating the BBP boundedness assumption [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")]; in this regime, BBP performance degrades. To confirm that this deterioration is indeed driven by the lack of boundedness, we also designed a Monte Carlo Cross-Validated (CV) BBP variant, which remains robust under the same perturbation. For details on the boundedness issue, the CV procedure, and the data-generating processes and validation protocol, we refer the reader to Appendix [6](https://arxiv.org/html/2601.07687v1#S6 "6 Cross-validated Singular-Value Shrinkage ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") and [7](https://arxiv.org/html/2601.07687v1#S7 "7 Synthetic Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Condition | Empirical (MLE) | Analytical (BBP) | Numerical (CV) | Neural Network (NN) |
| Panel A: Finite-Rank Spiked Models (varying spike % ξ\xi) | | | | |
| ξ=40%\xi=40\% | 2.00×10−32.00\times 10^{-3} | 2.46×10−42.46\times 10^{-4} | 2.46×𝟏𝟎−𝟒\mathbf{2.46\times 10^{-4}} | 2.53×10−42.53\times 10^{-4} |
| ξ=30%\xi=30\% | 2.00×10−32.00\times 10^{-3} | 1.92×10−41.92\times 10^{-4} | 1.92×𝟏𝟎−𝟒\mathbf{1.92\times 10^{-4}} | 1.95×10−41.95\times 10^{-4} |
| ξ=20%\xi=20\% | 2.00×10−32.00\times 10^{-3} | 1.34×𝟏𝟎−𝟒\mathbf{1.34\times 10^{-4}} | 1.33×𝟏𝟎−𝟒\mathbf{1.33\times 10^{-4}} | 1.34×10−41.34\times 10^{-4} |
| ξ=10%\xi=10\% | 2.00×10−32.00\times 10^{-3} | 7.03×𝟏𝟎−𝟓\mathbf{7.03\times 10^{-5}} | 7.00×𝟏𝟎−𝟓\mathbf{7.00\times 10^{-5}} | 7.12×10−57.12\times 10^{-5} |
| ξ=0%\xi=0\% | 2.00×10−32.00\times 10^{-3} | 3.73×𝟏𝟎−𝟔\mathbf{3.73\times 10^{-6}} | 3.92×10−63.92\times 10^{-6} | 9.02×10−69.02\times 10^{-6} |
| Panel B: Heavy-Tailed Bulk Models (varying tail exponent α\alpha) | | | | |
| Gaussian | 2.00×10−32.00\times 10^{-3} | 6.16×10−46.16\times 10^{-4} | 6.18×10−46.18\times 10^{-4} | 6.16×𝟏𝟎−𝟒\mathbf{6.16\times 10^{-4}} |
| α=5.0\alpha=5.0 | 2.00×10−32.00\times 10^{-3} | 6.16×10−46.16\times 10^{-4} | 6.18×10−46.18\times 10^{-4} | 6.16×𝟏𝟎−𝟒\mathbf{6.16\times 10^{-4}} |
| α=2.5\alpha=2.5 | 2.00×10−32.00\times 10^{-3} | 6.16×10−46.16\times 10^{-4} | 6.18×10−46.18\times 10^{-4} | 6.16×𝟏𝟎−𝟒\mathbf{6.16\times 10^{-4}} |
| α=1.5\alpha=1.5 | 2.00×10−32.00\times 10^{-3} | 6.19×𝟏𝟎−𝟒\mathbf{6.19\times 10^{-4}} | 6.20×10−46.20\times 10^{-4} | 6.18×𝟏𝟎−𝟒\mathbf{6.18\times 10^{-4}} |
| Panel C: White Heavy-Tailed Models (varying tail exponent α\alpha) | | | | |
| Gaussian | 2.00×10−32.00\times 10^{-3} | 5.63×𝟏𝟎−𝟒\mathbf{5.63\times 10^{-4}} | 5.64×10−45.64\times 10^{-4} | 5.64×10−45.64\times 10^{-4} |
| α=5.0\alpha=5.0 | 2.00×10−32.00\times 10^{-3} | 5.63×𝟏𝟎−𝟒\mathbf{5.63\times 10^{-4}} | 5.65×10−45.65\times 10^{-4} | 5.64×10−45.64\times 10^{-4} |
| α=2.5\alpha=2.5 | 2.00×10−32.00\times 10^{-3} | 2.50×𝟏𝟎−𝟒\mathbf{2.50\times 10^{-4}} | 2.50×𝟏𝟎−𝟒\mathbf{2.50\times 10^{-4}} | 2.51×𝟏𝟎−𝟒\mathbf{2.51\times 10^{-4}} |
| α=1.5\alpha=1.5 | 2.00×10−32.00\times 10^{-3} | 3.92×𝟏𝟎−𝟓\mathbf{3.92\times 10^{-5}} | 3.90×𝟏𝟎−𝟓\mathbf{3.90\times 10^{-5}} | 4.14×10−54.14\times 10^{-5} |
| Panel D: Gaussian Bulk Models with Common Mode (varying mode mm) | | | | |
| m=0.5m=0.5 | 1.09×10−31.09\times 10^{-3} | 7.90×10−27.90\times 10^{-2} | 7.45×𝟏𝟎−𝟒\mathbf{7.45\times 10^{-4}} | 7.42×𝟏𝟎−𝟒\mathbf{7.42\times 10^{-4}} |
| m=0.4m=0.4 | 1.42×10−31.42\times 10^{-3} | 3.29×10−23.29\times 10^{-2} | 9.25×𝟏𝟎−𝟒\mathbf{9.25\times 10^{-4}} | 9.18×𝟏𝟎−𝟒\mathbf{9.18\times 10^{-4}} |
| m=0.3m=0.3 | 1.66×10−31.66\times 10^{-3} | 9.89×10−39.89\times 10^{-3} | 9.83×𝟏𝟎−𝟒\mathbf{9.83\times 10^{-4}} | 9.84×𝟏𝟎−𝟒\mathbf{9.84\times 10^{-4}} |
| m=0.2m=0.2 | 1.85×10−31.85\times 10^{-3} | 2.23×10−32.23\times 10^{-3} | 9.84×𝟏𝟎−𝟒\mathbf{9.84\times 10^{-4}} | 9.79×𝟏𝟎−𝟒\mathbf{9.79\times 10^{-4}} |
| m=0.1m=0.1 | 1.96×10−31.96\times 10^{-3} | 8.85×10−48.85\times 10^{-4} | 8.52×𝟏𝟎−𝟒\mathbf{8.52\times 10^{-4}} | 8.56×𝟏𝟎−𝟒\mathbf{8.56\times 10^{-4}} |

Table 1: Summary of the average MSE for different estimators across three synthetic regimes over 1000 simulations. Bold marks the lowest MSE; ties are bold when a 95% percentile 100,000100,000 copies bootstrap cannot distinguish them. Panel A varies the spike percentage ξ\xi (Finite-Rank). Panel B and C vary the tail exponent α\alpha (Heavy-Tailed Bulk and White models), where a lower α\alpha implies heavier tails. Panel D is a variation of Panel B (Gaussian) with a one-factor mode injected. All simulations are performed with nx=200n\_{x}=200, ny=350n\_{y}=350, Δ​tin=500\Delta t\_{\textrm{in}}=500 [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")].

Moving to real-world data, we train and test the estimators on a universe of the top 1000 U.S. equities by market capitalization (1995-2024), filtered for liquidity and stability (see Appendix [8.1](https://arxiv.org/html/2601.07687v1#S8.SS1 "8.1 Universe Selection ‣ 8 Market Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")). To mitigate look-ahead bias, the top-1000 universe is reconstituted at each window start, so constituents vary over time.
In this regime, the non-stationarity of financial time series becomes a predominant factor. According to standard practice, we train a separate model for each calendar year and then test it on the subsequent two years, using as a target a realized OOS correlation matrix computed over a hold-out window of length Δ​tout=240\Delta t\_{\mathrm{out}}=240 trading days. Each yearly model is optimized for 50 epochs (500 gradient steps per epoch) with mini-batches of 32 samples. Each sample is generated by drawing a random date, the total number of assets n:=nx+ny∼𝒰​[50,500]n:=n\_{x}+n\_{y}\sim\mathcal{U}[50,500], and the relative dimension ν:=nx/(nx+ny)∼𝒰​[0.05,0.95]\nu:=n\_{x}/(n\_{x}+n\_{y})\sim\mathcal{U}[0.05,0.95], which enforces dimension-agnostic behavior and allows evaluation on larger shapes (n>500n>500) without retraining.

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

![Refer to caption](x5.png)

Figure 2: OOS MSE for cross-correlation estimators on financial data covering 2017–2024. For each test window, the estimator is trained on an expanding sample from 1995 up to the year immediately preceding the test period, and the reported value averages 1,000 independent runs for each out-of-sample year. The figures report also the Oracle (red dashed line), which is the lower achievable MSE by a RIE (see eq. ([35](https://arxiv.org/html/2601.07687v1#S6.E35 "In 6.2 Cross-Validation Algorithm ‣ 6 Cross-validated Singular-Value Shrinkage ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"))). The left panels preserve the chronological order between in-sample and out-of-sample windows, whereas the right panels shuffle dates. The upper panels varies the total number of assests for ν=0.25\nu=0.25, the lower panels varies the relative dimension ν\nu for n=1000n=1000. The error bars indicate a 95%95\% percentile 100,000100,000 copies bootstrap confidence interval.

Figure [2](https://arxiv.org/html/2601.07687v1#S3.F2 "Figure 2 ‣ 3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") (upper left) reports the OOS MSE as a function of the total number of assets nn for a fixed in-sample window (Δ​tin=500\Delta t\_{\textrm{in}}=500). The Maximum-Likelihood Estimator (MLE, yellow) provides the unfiltered baseline. Across both the nn- and ν\nu-sweeps, the proposed NN estimator (blue) achieves the lowest error. For small universes (e.g., n=250n=250), its performance is not statistically distinguishable from BBP (gray). However, as nn increases, BBP deteriorates sharply and can even underperform MLE, indicating that the analytical shrinkage can become harmful in this regime. We attribute this failure to the presence of a macroscopic market mode in real returns, which violates the boundedness conditions underlying BBP. This interpretation is supported by two additional diagnostics. First, the numerical CV estimator is not affected by the same degradation and remains comparable to the NN. Second, in Appendix [8.3](https://arxiv.org/html/2601.07687v1#S8.SS3 "8.3 Market-Mode Removal as a Boundedness Diagnostic ‣ 8 Market Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") we show that pre-processing the data by removing the mode, operationally defined as the daily cross-sectional mean return, eliminates the gross of the BBP underperformance. Finally, when we shuffle the time series to break potential non-stationarity between in-sample and out-of-sample periods, BBP remains unstable whereas CV continues to track the NN, further indicating that the dominant driver is the mode rather than temporal non-stationarity, see Fig. [2](https://arxiv.org/html/2601.07687v1#S3.F2 "Figure 2 ‣ 3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") (right) . Notably, the NN performance remains robust even for n>500n>500, which constitutes a fully out-of-distribution regime for the model. This region lies beyond the matrix sizes observed during training (n≤500n\leq 500), and it also corresponds to a different historical period than the data used to fit the network. To further probe this extrapolative regime, in the lower panel of Fig. [2](https://arxiv.org/html/2601.07687v1#S3.F2 "Figure 2 ‣ 3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") (lower) we unpack the n=1000n=1000 case by varying the relative dimension ν\nu, and we find that the NN gain remains stable across the full range of ν\nu, indicating that its advantage is not concentrated in a specific configuration.

Our working hypothesis is that this behavior is precisely the one targeted by the proposed architecture. In stationary settings, the network should primarily act as a noise-cleaning operator on the empirical spectrum. In contrast, when applied to non-stationary financial data, it can interpolate between denoising and a learned predictive correction that exploits persistent structure beyond sampling noise.
To confirm that this gain is derived from capturing genuine temporal signals (non-stationarity), we replicate the analysis on temporally shuffled data. Shuffling destroys the serial correlations responsible for the predictive edge, creating a purely stationary environment. Figures [2](https://arxiv.org/html/2601.07687v1#S3.F2 "Figure 2 ‣ 3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") (right) illustrate that performance degradation of BBP persists even in the shuffled regime, confirming the underlying structural driver. As expected, the CV estimator does not degrade and instead matches the NN performance indicating that in a stationary regime the NN learn how to denoise only sample noise. This interpretation is further supported by the feasibility diagnostic reported in Appendix [8.4](https://arxiv.org/html/2601.07687v1#S8.SS4 "8.4 Feasibility Diagnostic via Canonical-Correlation Boundedness ‣ 8 Market Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").

## 4 Discussion and Conclusion

Across controlled synthetic benchmarks and temporally shuffled equity returns, the proposed estimator matches the performance of the optimal rotationally invariant shrinkage, indicating that it has learned a stationary random-matrix-consistent spectral denoiser rather than introducing spurious structure. In the presence of a pronounced market mode, it also improves upon the corresponding analytic shrinkage method, which is consistent with a mode-aware generalization.

On original (unshuffled) market data, the two cleaners remain comparable for moderate universes, but their behavior diverges as nn grows. The analytical BBP shrinkage deteriorates sharply with system size and can even underperform the unfiltered MLE, consistent with sensitivity to macroscopic components (notably a market mode) that violate the boundedness conditions underlying the asymptotics. In contrast, the neural estimator remains stable and achieves lower OOS reconstruction error, including for n>500n>500 (an out-of-distribution regime relative to training). Removing the market mode substantially reduces the BBP collapse, yet a residual gap to the neural estimator persists in the chronological evaluation and largely disappears under temporal shuffling; taken together, these controls support the view that the architecture preserves the BBP symmetry constraints while using OOS supervision to retain only cross-dependencies that persist across adjacent windows, i.e., a symmetry-preserving singular-value map that interpolates between denoising and a mild predictive correction.

A natural direction for future work is to extend the same symmetry-preserving parametrization to lead-lag cross-covariance matrices, where the relevant signal is intrinsically dynamical and cannot be reduced to a single synchronous estimator. In this setting, rather than training via the Frobenius loss, one can adopt an end-to-end decision-aware objective consistent with a trading strategy so that the shrinkage rule is learned under the same decision loss used for evaluation.

## Acknowledgments

This work was performed using HPC resources from the “Mésocentre” computing center of CentraleSupélec and École Normale Supérieure Paris-Saclay supported by CNRS and Région Île-de-France ([mesocentre.centralesupelec.fr](http://mesocentre.centralesupelec.fr/)). E.M. acknowledges a fellowship funded by PNRR for the PhD DOT1608375 in Sistemi complessi per le scienze fisiche, socio-economiche e della vita of Catania University.

## References

* [1]
  K. M. Abadir, W. Distaso, and F. Žikeš (2014)
  Design-free estimation of variance matrices.
  Journal of Econometrics 181 (2),  pp. 165–180.
  Cited by: [§6.2](https://arxiv.org/html/2601.07687v1#S6.SS2.p1.1 "6.2 Cross-Validation Algorithm ‣ 6 Cross-validated Singular-Value Shrinkage ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [2]
  F. Benaych-Georges, J. Bouchaud, and M. Potters (2023)
  Optimal cleaning for singular values of cross-covariance matrices.
  The Annals of Applied Probability 33 (2),  pp. 1295–1326.
  Cited by: [§1](https://arxiv.org/html/2601.07687v1#S1.p3.4 "1 Introduction ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§2](https://arxiv.org/html/2601.07687v1#S2.p2.5 "2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [Table 1](https://arxiv.org/html/2601.07687v1#S3.T1 "In 3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§3](https://arxiv.org/html/2601.07687v1#S3.p1.1 "3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§5.1](https://arxiv.org/html/2601.07687v1#S5.SS1.p2.3 "5.1 BBP Analytical Shrinkage: Algorithm 1 ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§5.3](https://arxiv.org/html/2601.07687v1#S5.SS3.p5.4 "5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§5](https://arxiv.org/html/2601.07687v1#S5.p1.1 "5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§7.1](https://arxiv.org/html/2601.07687v1#S7.SS1.SSSx1.p1.1 "Benchmark I:Finite-Rank Spiked Models ‣ 7.1 Synthetic Benchmarks ‣ 7 Synthetic Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§7.1](https://arxiv.org/html/2601.07687v1#S7.SS1.SSSx1.p1.5 "Benchmark I:Finite-Rank Spiked Models ‣ 7.1 Synthetic Benchmarks ‣ 7 Synthetic Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§7.1](https://arxiv.org/html/2601.07687v1#S7.SS1.SSSx2.p1.5 "Benchmark II: Heavy-Tailed Bulk Models ‣ 7.1 Synthetic Benchmarks ‣ 7 Synthetic Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§7.1](https://arxiv.org/html/2601.07687v1#S7.SS1.SSSx3.p1.2 "Benchmark III: White Heavy-Tailed Cross-Correlation Models ‣ 7.1 Synthetic Benchmarks ‣ 7 Synthetic Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§7.1](https://arxiv.org/html/2601.07687v1#S7.SS1.SSSx3.p1.5 "Benchmark III: White Heavy-Tailed Cross-Correlation Models ‣ 7.1 Synthetic Benchmarks ‣ 7 Synthetic Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§7.2](https://arxiv.org/html/2601.07687v1#S7.SS2.p4.6 "7.2 Training on Synthetic Data ‣ 7 Synthetic Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§7](https://arxiv.org/html/2601.07687v1#S7.p1.1 "7 Synthetic Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [3]
  C. Bongiorno, D. Challet, and G. Loeper (2023)
  Filtering time-dependent covariance matrices using time-independent eigenvalues.
  Journal of Statistical Mechanics: Theory and Experiment 2023 (2),  pp. 023402.
  Cited by: [§1](https://arxiv.org/html/2601.07687v1#S1.p4.1 "1 Introduction ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [4]
  C. Bongiorno and D. Challet (2023)
  Non-linear shrinkage of the price return covariance matrix is far from optimal for portfolio optimization.
  Finance Research Letters 52,  pp. 103383.
  Cited by: [§1](https://arxiv.org/html/2601.07687v1#S1.p5.1 "1 Introduction ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [5]
  C. Bongiorno, E. Manolakis, and R. N. Mantegna (2025)
  End-to-end large portfolio optimization for variance minimization with neural networks through covariance cleaning.
  arXiv preprint arXiv:2507.01918.
  Cited by: [§1](https://arxiv.org/html/2601.07687v1#S1.p5.1 "1 Introduction ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§2](https://arxiv.org/html/2601.07687v1#S2.p4.4 "2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§8.1](https://arxiv.org/html/2601.07687v1#S8.SS1.p1.1 "8.1 Universe Selection ‣ 8 Market Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [6]
  C. Bongiorno, E. Manolakis, and R. N. Mantegna (2025)
  Neural network-driven volatility drag mitigation under aggressive leverage.
  In Proceedings of the 6th ACM International Conference on AI in Finance,
   pp. 449–455.
  Cited by: [§1](https://arxiv.org/html/2601.07687v1#S1.p5.1 "1 Introduction ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [7]
  J. Bun, J. Bouchaud, and M. Potters (2017)
  Cleaning large correlation matrices: tools from random matrix theory.
  Physics Reports 666,  pp. 1–109.
  Cited by: [§1](https://arxiv.org/html/2601.07687v1#S1.p2.2 "1 Introduction ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [8]
  A. Bykhovskaya and V. Gorin (2024)
  Canonical correlation analysis.
  arXiv preprint arXiv:2411.15625.
  Cited by: [§5.3](https://arxiv.org/html/2601.07687v1#S5.SS3.p1.4 "5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [9]
  V. K. Chopra, W. T. Ziemba, et al. (1993)
  The effect of errors in means, variances, and covariances on optimal portfolio choice.
  Journal of Portfolio Management 19 (2),  pp. 6–11.
  Cited by: [§1](https://arxiv.org/html/2601.07687v1#S1.p2.2 "1 Introduction ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [10]
  M. Efstratios and B. Christian (2026)
  CrossRIE.
  Note: <https://github.com/Efstratios7/CrossRIE/>
  Cited by: [§2](https://arxiv.org/html/2601.07687v1#S2.p8.4 "2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [11]
  M. Gavish and D. L. Donoho (2017)
  Optimal shrinkage of singular values.
  IEEE Transactions on Information Theory 63 (4),  pp. 2137–2152.
  Cited by: [§1](https://arxiv.org/html/2601.07687v1#S1.p3.4 "1 Introduction ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [12]
  T. Jendoubi and K. Strimmer (2019)
  A whitening approach to probabilistic canonical correlation analysis for omics data integration.
  BMC bioinformatics 20 (1),  pp. 15.
  Cited by: [§5.3](https://arxiv.org/html/2601.07687v1#S5.SS3.p1.4 "5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [13]
  J. Kim, I. Tae, and Y. Lee (2025)
  Estimating covariance for global minimum variance portfolio: a decision-focused learning approach.
   pp. 105–113.
  External Links: ISBN 9798400722202
  Cited by: [§1](https://arxiv.org/html/2601.07687v1#S1.p5.1 "1 Introduction ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [14]
  C. Lam (2016)
  Nonparametric eigenvalue-regularized precision or covariance matrix estimator.
  The Annals of Statistics 44 (3),  pp. 928–953.
  Cited by: [§6.2](https://arxiv.org/html/2601.07687v1#S6.SS2.p1.1 "6.2 Cross-Validation Algorithm ‣ 6 Cross-validated Singular-Value Shrinkage ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [15]
  R. J. Muirhead (2009)
  Aspects of multivariate statistical theory.
   John Wiley & Sons.
  Cited by: [§5.3](https://arxiv.org/html/2601.07687v1#S5.SS3.p1.4 "5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"),
  [§5.3](https://arxiv.org/html/2601.07687v1#S5.SS3.p2.6 "5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [16]
  D. V. Ouellette (1981)
  Schur complements and statistics.
  Linear Algebra and its Applications 36,  pp. 187–295.
  Cited by: [§5.3](https://arxiv.org/html/2601.07687v1#S5.SS3.p3.3 "5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [17]
  E. Troiani, V. Erba, F. Krzakala, A. Maillard, and L. Zdeborová (2022)
  Optimal denoising of rotationally invariant rectangular matrices.
  In Mathematical and Scientific Machine Learning,
   pp. 97–112.
  Cited by: [§1](https://arxiv.org/html/2601.07687v1#S1.p3.4 "1 Introduction ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").
* [18]
  U.S. Securities and Exchange Commission (2024)
  17 CFR §240.12d2-2 – Removal from Listing and Registration.
  Note: <https://www.law.cornell.edu/cfr/text/17/240.12d2-2>
  Cited by: [§8.1.1](https://arxiv.org/html/2601.07687v1#S8.SS1.SSS1.p2.1 "8.1.1 Delisting Risk and Alternative Remedies ‣ 8.1 Universe Selection ‣ 8 Market Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").

## 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN

This section rewrites the analytical BBP singular-value cleaner [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")] using the notation of Section [2](https://arxiv.org/html/2601.07687v1#S2 "2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"), and clarifies why the proposed two-stream neural architecture contains that analytical mapping as a special case.

### 5.1 BBP Analytical Shrinkage: Algorithm 1

Let {𝐱​(t)∈ℝnx,𝐲​(t)∈ℝny}t=1Δ​tin\{\mathbf{x}(t)\in\mathbb{R}^{n\_{x}},\mathbf{y}(t)\in\mathbb{R}^{n\_{y}}\}\_{t=1}^{\Delta t\_{\textrm{in}}} denote standardized observations on a window of length Δ​tin\Delta t\_{\textrm{in}}, and let
𝐂^X​Y\widehat{\mathbf{C}}\_{XY}, 𝐂^X​X\widehat{\mathbf{C}}\_{XX}, and 𝐂^Y​Y\widehat{\mathbf{C}}\_{YY} be the corresponding empirical cross-correlation and marginal correlation matrices. Write the SVD

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂^X​Y=∑k=1rs^k​𝐮^k​𝐯^k⊤,r:=min⁡(nx,ny),\widehat{\mathbf{C}}\_{XY}=\sum\_{k=1}^{r}\widehat{s}\_{k}\,\widehat{\mathbf{u}}\_{k}\widehat{\mathbf{v}}\_{k}^{\top},\qquad r:=\min(n\_{x},n\_{y}), |  | (10) |

and define the marginal projections (Section [2](https://arxiv.org/html/2601.07687v1#S2 "2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ^k(x):=𝐮^k⊤​𝐂^X​X​𝐮^k,γ^k(y):=𝐯^k⊤​𝐂^Y​Y​𝐯^k.\widehat{\gamma}^{(x)}\_{k}:=\widehat{\mathbf{u}}\_{k}^{\top}\widehat{\mathbf{C}}\_{XX}\widehat{\mathbf{u}}\_{k},\qquad\widehat{\gamma}^{(y)}\_{k}:=\widehat{\mathbf{v}}\_{k}^{\top}\widehat{\mathbf{C}}\_{YY}\widehat{\mathbf{v}}\_{k}. |  | (11) |

When nx≠nyn\_{x}\neq n\_{y}, BBP requires also the aggregate marginal energy in the “extra” directions of the larger side. Without loss of generality assume nx≤nyn\_{x}\leq n\_{y} (otherwise swap the roles of XX and YY); then r=nxr=n\_{x} and we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ^r+(y):=∑ℓ=r+1ny𝐯^ℓ⊤​𝐂^Y​Y​𝐯^ℓ,\widehat{\gamma}^{(y)}\_{r+}:=\sum\_{\ell=r+1}^{n\_{y}}\widehat{\mathbf{v}}\_{\ell}^{\top}\widehat{\mathbf{C}}\_{YY}\widehat{\mathbf{v}}\_{\ell}, |  | (12) |

where {𝐯^ℓ}ℓ=r+1ny\{\widehat{\mathbf{v}}\_{\ell}\}\_{\ell=r+1}^{n\_{y}} completes {𝐯^k}k=1r\{\widehat{\mathbf{v}}\_{k}\}\_{k=1}^{r} to an orthonormal basis of ℝny\mathbb{R}^{n\_{y}}.

The authors then defines, for each index k∈{1,…,r}k\in\{1,\dots,r\}, the complex spectral point

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζk:=s^k+i​η,η:=(r​ny​Δ​tin)−1/12,\zeta\_{k}:=\widehat{s}\_{k}+i\eta,\qquad\eta:=(r\,n\_{y}\,\Delta t\_{\textrm{in}})^{-1/12}, |  | (13) |

and the scalar functionals

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H​(ζk)\displaystyle H(\zeta\_{k}) | :=1Δ​tin​∑ℓ=1rs^ℓ2ζk2−s^ℓ2,\displaystyle:=\frac{1}{\Delta t\_{\textrm{in}}}\sum\_{\ell=1}^{r}\frac{\widehat{s}\_{\ell}^{2}}{\zeta\_{k}^{2}-\widehat{s}\_{\ell}^{2}}, |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A​(ζk)\displaystyle A(\zeta\_{k}) | :=1Δ​tin​∑ℓ=1rγ^ℓ(x)ζk2−s^ℓ2,\displaystyle:=\frac{1}{\Delta t\_{\textrm{in}}}\sum\_{\ell=1}^{r}\frac{\widehat{\gamma}^{(x)}\_{\ell}}{\zeta\_{k}^{2}-\widehat{s}\_{\ell}^{2}}, |  | (15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | B​(ζk)\displaystyle B(\zeta\_{k}) | :=1Δ​tin​(∑ℓ=1rγ^ℓ(y)ζk2−s^ℓ2+ζk−2​γ^r+(y)).\displaystyle:=\frac{1}{\Delta t\_{\textrm{in}}}\left(\sum\_{\ell=1}^{r}\frac{\widehat{\gamma}^{(y)}\_{\ell}}{\zeta\_{k}^{2}-\widehat{s}\_{\ell}^{2}}+\zeta\_{k}^{-2}\widehat{\gamma}^{(y)}\_{r+}\right). |  | (16) |

With

|  |  |  |  |
| --- | --- | --- | --- |
|  | Θ​(ζk):=ζk2​A​(ζk)​B​(ζk)1+H​(ζk),L​(ζk):=H​(ζk)−Θ​(ζk)1+H​(ζk)−Θ​(ζk),\Theta(\zeta\_{k}):=\frac{\zeta\_{k}^{2}\,A(\zeta\_{k})\,B(\zeta\_{k})}{1+H(\zeta\_{k})},\qquad L(\zeta\_{k}):=H(\zeta\_{k})-\frac{\Theta(\zeta\_{k})}{1+H(\zeta\_{k})-\Theta(\zeta\_{k})}, |  | (17) |

the analytical cleaned singular values are

|  |  |  |  |
| --- | --- | --- | --- |
|  | s^kBBP:=s^k​(ℑ⁡L​(ζk)ℑ⁡H​(ζk))+,(x)+:=max⁡{x,0}.\widehat{s}^{\mathrm{BBP}}\_{k}:=\widehat{s}\_{k}\left(\frac{\Im L(\zeta\_{k})}{\Im H(\zeta\_{k})}\right)\_{+},\qquad(x)\_{+}:=\max\{x,0\}. |  | (18) |

Optionally, Ref. [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")] suggests enforcing monotonicity of k↦s^kBBPk\mapsto\widehat{s}^{\mathrm{BBP}}\_{k} via isotonic regression on the pairs (s^k,s^kBBP)(\widehat{s}\_{k},\widehat{s}^{\mathrm{BBP}}\_{k}).

Finally, the BBP rotationally invariant estimator is reconstructed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂^X​YBBP:=∑k=1rs^kBBP​𝐮^k​𝐯^k⊤.\widehat{\mathbf{C}}^{\mathrm{BBP}}\_{XY}:=\sum\_{k=1}^{r}\widehat{s}^{\mathrm{BBP}}\_{k}\,\widehat{\mathbf{u}}\_{k}\widehat{\mathbf{v}}\_{k}^{\top}. |  | (19) |

### 5.2 Relationship Between the Two-Stream NN and the Analytical Shrinkage

The key observation is that the BBP map in Eq. ([18](https://arxiv.org/html/2601.07687v1#S5.E18 "In 5.1 BBP Analytical Shrinkage: Algorithm 1 ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) depends on the data only through (i) the empirical singular spectrum {s^ℓ}ℓ=1r\{\widehat{s}\_{\ell}\}\_{\ell=1}^{r}, (ii) the marginal projections {γ^ℓ(x)}ℓ=1r\{\widehat{\gamma}^{(x)}\_{\ell}\}\_{\ell=1}^{r} and {γ^ℓ(y)}ℓ=1ny\{\widehat{\gamma}^{(y)}\_{\ell}\}\_{\ell=1}^{n\_{y}} (through γ^r+(y)\widehat{\gamma}^{(y)}\_{r+}), and (iii) the aspect ratios qx=nx/Δ​tinq\_{x}=n\_{x}/\Delta t\_{\textrm{in}} and qy=ny/Δ​tinq\_{y}=n\_{y}/\Delta t\_{\textrm{in}} (which enter through η\eta and, more generally, through the high-dimensional scaling). In particular, once the empirical singular vectors are fixed, BBP is a deterministic permutation-equivariant mapping

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝐬^,𝜸^(x),𝜸^(y),qx,qy)⟼(s^1BBP,…,s^rBBP),(\widehat{\mathbf{s}},\widehat{\boldsymbol{\gamma}}^{(x)},\widehat{\boldsymbol{\gamma}}^{(y)},q\_{x},q\_{y})\longmapsto(\widehat{s}^{\mathrm{BBP}}\_{1},\dots,\widehat{s}^{\mathrm{BBP}}\_{r}), |  | (20) |

with 𝐬^=(s^1,…,s^r)\widehat{\mathbf{s}}=(\widehat{s}\_{1},\dots,\widehat{s}\_{r}) and similarly for the projection vectors.

Our NN is constructed precisely to take as input these BBP-sufficient statistics. Using the padded sequences of Eq.  ([3](https://arxiv.org/html/2601.07687v1#S2.E3 "In 2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) in Section [2](https://arxiv.org/html/2601.07687v1#S2 "2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"), we build the stream-specific tokens

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝉k(x):=(γk(x),sk,qx)⊤,𝝉k(y):=(γk(y),sk,qy)⊤,k=1,…,p,\boldsymbol{\tau}^{(x)}\_{k}:=(\gamma^{(x)}\_{k},\,s\_{k},\,q\_{x})^{\top},\qquad\boldsymbol{\tau}^{(y)}\_{k}:=(\gamma^{(y)}\_{k},\,s\_{k},\,q\_{y})^{\top},\qquad k=1,\dots,p, |  | (21) |

and process them via a shared encoder, additive fusion, a bidirectional LSTM aggregator, and a pointwise head to output δk\delta\_{k} and hence s~k=s^k+δk\widetilde{s}\_{k}=\widehat{s}\_{k}+\delta\_{k} (Eq. ([7](https://arxiv.org/html/2601.07687v1#S2.E7 "In 2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) in Section [2](https://arxiv.org/html/2601.07687v1#S2 "2 Two-Stream Architecture for Cross–Covariance Cleaning ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")). Because BBP is rotationally invariant, recovering it amounts to producing the particular residual

|  |  |  |  |
| --- | --- | --- | --- |
|  | δkBBP:=s^kBBP−s^k=s^k​[(ℑ⁡L​(ζk)ℑ⁡H​(ζk))+−1],k=1,…,r,\delta\_{k}^{\mathrm{BBP}}:=\widehat{s}^{\mathrm{BBP}}\_{k}-\widehat{s}\_{k}=\widehat{s}\_{k}\left[\left(\frac{\Im L(\zeta\_{k})}{\Im H(\zeta\_{k})}\right)\_{+}-1\right],\qquad k=1,\dots,r, |  | (22) |

and leaving the empirical singular vectors unchanged, which matches our reconstruction by design.

To see that the NN modules can represent this mapping, it suffices to track how each BBP ingredient can be implemented within the architecture. First, the shared token-wise encoder EθE\_{\theta} can be set to pass through (possibly after a linear rescaling) the components (sk,γk(x),γk(y),qx,qy)(s\_{k},\gamma^{(x)}\_{k},\gamma^{(y)}\_{k},q\_{x},q\_{y}) into the latent sequence representation; in particular, the additive fusion 𝐳k=𝐞k(x)+𝐞k(y)\mathbf{z}\_{k}=\mathbf{e}^{(x)}\_{k}+\mathbf{e}^{(y)}\_{k} provides a symmetric mechanism to combine the two marginals while preserving equivariance under permutations of XX and YY coordinates.

Second, the bidirectional LSTM aggregator is precisely a mechanism to attach global spectral context to each index kk. In BBP, this global context appears through the sums defining H​(ζk)H(\zeta\_{k}), A​(ζk)A(\zeta\_{k}), and B​(ζk)B(\zeta\_{k}), which couple the local point ζk\zeta\_{k} (hence s^k\widehat{s}\_{k}) to the entire set {(s^ℓ,γ^ℓ(x),γ^ℓ(y))}ℓ\{(\widehat{s}\_{\ell},\widehat{\gamma}^{(x)}\_{\ell},\widehat{\gamma}^{(y)}\_{\ell})\}\_{\ell}. Since ζk=s^k+i​η\zeta\_{k}=\widehat{s}\_{k}+i\eta is fixed once kk is fixed, each of these quantities is a continuous function of the finite sequence of tokens, obtained by composing elementary operations (squaring, addition, reciprocal) with sequence-wise summation. The LSTM hidden state provides exactly the capacity required to encode such sequence-level aggregates (including the extra-marginal scalar γ^r+(y)\widehat{\gamma}^{(y)}\_{r+} when ny>nxn\_{y}>n\_{x}) and to make them available at each position kk.

Third, given access to approximations of H​(ζk)H(\zeta\_{k}), A​(ζk)A(\zeta\_{k}), and B​(ζk)B(\zeta\_{k}) in its context-aware state 𝐡k\mathbf{h}\_{k}, the pointwise head gθg\_{\theta} can implement the remaining BBP algebra: it can form Θ​(ζk)\Theta(\zeta\_{k}), then L​(ζk)L(\zeta\_{k}), and finally the ratio ℑ⁡L​(ζk)/ℑ⁡H​(ζk)\Im L(\zeta\_{k})/\Im H(\zeta\_{k}) and the residual δkBBP\delta\_{k}^{\mathrm{BBP}}. Concretely, this is a scalar continuous map from the state variables to δk\delta\_{k}, and thus falls within the representational capacity of a two-layer MLP head. Therefore, there exists a parameter configuration θBBP\theta\_{\mathrm{BBP}} for which the overall NN mapping coincides with BBP on the domain of interest:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s~k​(θBBP)=s^kBBP,k=1,…,r.\widetilde{s}\_{k}(\theta\_{\mathrm{BBP}})=\widehat{s}^{\mathrm{BBP}}\_{k},\qquad k=1,\dots,r. |  | (23) |

In summary, the architecture is a symmetry-preserving parametrization of rotationally invariant shrinkage rules: BBP corresponds to a particular choice of parameters that reproduces its analytical nonlinear map from empirical singular values and marginal projections to cleaned singular values, while training allows the same constrained hypothesis class to depart from that stationary prescription when the data are non-stationary or violate BBP regularity conditions.

### 5.3 Admissible Singular Values Under Fixed Marginals

A cross–correlation block cannot be specified independently of its marginals: given marginal correlation matrices 𝐂X​X∈ℝnx×nx\mathbf{C}\_{XX}\in\mathbb{R}^{n\_{x}\times n\_{x}} and 𝐂Y​Y∈ℝny×ny\mathbf{C}\_{YY}\in\mathbb{R}^{n\_{y}\times n\_{y}}, a candidate cross–correlation 𝐂X​Y∈ℝnx×ny\mathbf{C}\_{XY}\in\mathbb{R}^{n\_{x}\times n\_{y}} is feasible if and only if the full block correlation matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂:=(𝐂X​X𝐂X​Y𝐂Y​X𝐂Y​Y)\mathbf{C}:=\begin{pmatrix}\mathbf{C}\_{XX}&\mathbf{C}\_{XY}\\ \mathbf{C}\_{YX}&\mathbf{C}\_{YY}\end{pmatrix} |  | (24) |

is positive semidefinite[[15](https://arxiv.org/html/2601.07687v1#bib.bib20 "Aspects of multivariate statistical theory")]. We now express this constraint in terms of the singular values after whitening [[8](https://arxiv.org/html/2601.07687v1#bib.bib23 "Canonical correlation analysis"), [12](https://arxiv.org/html/2601.07687v1#bib.bib22 "A whitening approach to probabilistic canonical correlation analysis for omics data integration")], and show how the general (non-whitened) case reduces to the identity-marginal case.

Assume 𝐂X​X≻𝟎\mathbf{C}\_{XX}\succ\mathbf{0} and 𝐂Y​Y≻𝟎\mathbf{C}\_{YY}\succ\mathbf{0}, so that the symmetric square roots 𝐂X​X±1/2\mathbf{C}\_{XX}^{\pm 1/2} and 𝐂Y​Y±1/2\mathbf{C}\_{YY}^{\pm 1/2} are well-defined. Define the whitened cross–correlation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂X​Y(w):=𝐂X​X−1/2​𝐂X​Y​𝐂Y​Y−1/2∈ℝnx×ny.\mathbf{C}^{(w)}\_{XY}:=\mathbf{C}\_{XX}^{-1/2}\,\mathbf{C}\_{XY}\,\mathbf{C}\_{YY}^{-1/2}\in\mathbb{R}^{n\_{x}\times n\_{y}}. |  | (25) |

Consider the block-diagonal congruence transform with 𝐖:=diag​(𝐂X​X−1/2,𝐂Y​Y−1/2)\mathbf{W}:=\mathrm{diag}(\mathbf{C}\_{XX}^{-1/2},\mathbf{C}\_{YY}^{-1/2}), which yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐖𝐂𝐖⊤=(𝐈nx𝐂X​Y(w)𝐂X​Y(w)⊤𝐈ny)=:𝐂(w).\mathbf{W}\,\mathbf{C}\,\mathbf{W}^{\top}=\begin{pmatrix}\mathbf{I}\_{n\_{x}}&\mathbf{C}^{(w)}\_{XY}\\ \mathbf{C}^{(w)\top}\_{XY}&\mathbf{I}\_{n\_{y}}\end{pmatrix}=:\mathbf{C}^{(w)}. |  | (26) |

Since 𝐖\mathbf{W} is invertible, congruence preserves definiteness [[15](https://arxiv.org/html/2601.07687v1#bib.bib20 "Aspects of multivariate statistical theory")], hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂⪰𝟎⟺𝐂(w)⪰𝟎,𝐂≻𝟎⟺𝐂(w)≻𝟎.\mathbf{C}\succeq\mathbf{0}\ \Longleftrightarrow\ \mathbf{C}^{(w)}\succeq\mathbf{0},\qquad\mathbf{C}\succ\mathbf{0}\ \Longleftrightarrow\ \mathbf{C}^{(w)}\succ\mathbf{0}. |  | (27) |

We can therefore analyze feasibility in the identity-marginal regime represented by 𝐂(w)\mathbf{C}^{(w)}. Because the top-left block of 𝐂(w)\mathbf{C}^{(w)} is 𝐈nx\mathbf{I}\_{n\_{x}}, the Schur complement [[16](https://arxiv.org/html/2601.07687v1#bib.bib21 "Schur complements and statistics")] gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂(w)⪰𝟎⟺𝐈ny−𝐂X​Y(w)⊤​𝐂X​Y(w)⪰𝟎,\mathbf{C}^{(w)}\succeq\mathbf{0}\quad\Longleftrightarrow\quad\mathbf{I}\_{n\_{y}}-\mathbf{C}^{(w)\top}\_{XY}\mathbf{C}^{(w)}\_{XY}\succeq\mathbf{0}, |  | (28) |

and similarly 𝐈nx−𝐂X​Y(w)​𝐂X​Y(w)⊤⪰𝟎\mathbf{I}\_{n\_{x}}-\mathbf{C}^{(w)}\_{XY}\mathbf{C}^{(w)\top}\_{XY}\succeq\mathbf{0}. Let r:=min⁡(nx,ny)r:=\min(n\_{x},n\_{y}) and write the SVD 𝐂X​Y(w)=∑k=1rsk(w)​𝐮k​𝐯k⊤\mathbf{C}^{(w)}\_{XY}=\sum\_{k=1}^{r}s\_{k}^{(w)}\,\mathbf{u}\_{k}\mathbf{v}\_{k}^{\top}, with singular values s1(w)≥⋯≥sr(w)≥0s^{(w)}\_{1}\geq\cdots\geq s^{(w)}\_{r}\geq 0. The nonzero eigenvalues of 𝐂X​Y(w)⊤​𝐂X​Y(w)\mathbf{C}^{(w)\top}\_{XY}\mathbf{C}^{(w)}\_{XY} are {(sk(w))2}k=1r\{(s\_{k}^{(w)})^{2}\}\_{k=1}^{r}, so Eq. ([28](https://arxiv.org/html/2601.07687v1#S5.E28 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤sk(w)≤1,k=1,…,r.0\leq s\_{k}^{(w)}\leq 1,\qquad k=1,\dots,r. |  | (29) |

Moreover, the strict constraint

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤sk(w)<1,k=1,…,r,0\leq s\_{k}^{(w)}<1,\qquad k=1,\dots,r, |  | (30) |

is sufficient to ensure positive definiteness: indeed, Eq. ([30](https://arxiv.org/html/2601.07687v1#S5.E30 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) implies 𝐈ny−𝐂X​Y(w)⊤​𝐂X​Y(w)≻𝟎\mathbf{I}\_{n\_{y}}-\mathbf{C}^{(w)\top}\_{XY}\mathbf{C}^{(w)}\_{XY}\succ\mathbf{0}, hence 𝐂(w)≻𝟎\mathbf{C}^{(w)}\succ\mathbf{0} by the Schur complement, and therefore 𝐂≻𝟎\mathbf{C}\succ\mathbf{0} by Eq. ([27](https://arxiv.org/html/2601.07687v1#S5.E27 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")). Consequently, in the general-marginal setting, testing feasibility reduces to computing 𝐂X​Y(w)\mathbf{C}^{(w)}\_{XY} via Eq. ([25](https://arxiv.org/html/2601.07687v1#S5.E25 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) and verifying that its singular values satisfy 0≤sk(w)≤10\leq s\_{k}^{(w)}\leq 1 (or sk(w)<1s\_{k}^{(w)}<1 for strict positive definiteness).

Finally, the whitening relation can be inverted as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂X​Y=𝐂X​X1/2​𝐂X​Y(w)​𝐂Y​Y1/2,\mathbf{C}\_{XY}=\mathbf{C}\_{XX}^{1/2}\,\mathbf{C}^{(w)}\_{XY}\,\mathbf{C}\_{YY}^{1/2}, |  | (31) |

so any procedure that produces a cleaned 𝐂X​Y(w)\mathbf{C}^{(w)}\_{XY} with singular values in [0,1][0,1] automatically yields a block matrix 𝐂\mathbf{C} that is positive semidefinite, and enforcing sk(w)<1s\_{k}^{(w)}<1 guarantees that 𝐂\mathbf{C} is positive definite when 𝐂X​X\mathbf{C}\_{XX} and 𝐂Y​Y\mathbf{C}\_{YY} are positive definite.

A final remark concerns the meaning of “shrinkage” versus feasibility. Conditions such as s~k≤s^k\tilde{s}\_{k}\leq\hat{s}\_{k} (cleaned singular values smaller than empirical ones) [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")] are typical of pure denoising: under stationarity, the empirical spectrum is interpreted as signal contaminated by sampling noise, and optimal corrections shrink modes toward zero. In our setting, however, the objective is not only denoising but also OOS forecasting. Enforcing a universal shrinkage inequality s~k≤s^k\tilde{s}\_{k}\leq\hat{s}\_{k} would be unnecessarily stringent, because improving predictive performance may require amplifying specific modes that are weak in-sample yet systematically predictive OOS. The relevant requirement is therefore feasibility in the sense of producing a valid block correlation matrix under fixed marginals, while allowing s~k\tilde{s}\_{k} to exceed s^k\hat{s}\_{k} in selected directions when this improves forecasting. This distinction is supported by the analysis in Appendix [8.4](https://arxiv.org/html/2601.07687v1#S8.SS4 "8.4 Feasibility Diagnostic via Canonical-Correlation Boundedness ‣ 8 Market Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").

## 6 Cross-validated Singular-Value Shrinkage

### 6.1 Boundness in the Presence of a Mode

The analytical BBP shrinkage is derived under high-dimensional assumptions that include boundedness of the operator norm of the population covariance of the concatenated vector. In practice this condition can fail in the presence of a strong common mode. A standard illustration is the equicorrelation matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐀n=(1−m)​𝐈n+m​ 11⊤,0<m<1,\mathbf{A}\_{n}=(1-m)\mathbf{I}\_{n}+m\,\mathbf{1}\mathbf{1}^{\top},\qquad 0<m<1, |  | (32) |

where 𝟏𝟏⊤\mathbf{1}\mathbf{1}^{\top} has eigenvalue nn along 𝟏\mathbf{1} and 0 on the (n−1)(n-1)-dimensional orthogonal subspace. Hence the eigenvalues of 𝐀n\mathbf{A}\_{n} are

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ1=(1−m)+m​n=1+m​(n−1),λ2=⋯=λn=1−m,\lambda\_{1}=(1-m)+mn=1+m(n-1),\qquad\lambda\_{2}=\cdots=\lambda\_{n}=1-m, |  | (33) |

so that ‖𝐀n‖op=λ1∼m​n→∞\|\mathbf{A}\_{n}\|\_{\mathrm{op}}=\lambda\_{1}\sim mn\to\infty as n→∞n\to\infty. If such a block is embedded as a principal submatrix of the full population covariance 𝚺\mathbf{\Sigma}, then ‖𝚺‖op≥‖𝐀n‖op\|\mathbf{\Sigma}\|\_{\mathrm{op}}\geq\|\mathbf{A}\_{n}\|\_{\mathrm{op}}, and 𝚺\mathbf{\Sigma} is not bounded in the sense required by the analytical derivation. We therefore introduce a Cross-validation (CV) singular-value shrinkage that provides a stationary BBP-like construction without relying on boundedness of ‖𝚺‖op\|\mathbf{\Sigma}\|\_{\mathrm{op}}.

### 6.2 Cross-Validation Algorithm

CV offers a direct, model-free proxy for cleaning singular values. The key idea is to estimate the singular directions on a training subsample and to evaluate their associated mode strengths on an independent test subsample; under approximate stationarity within the window, this replaces an optimistically biased in-sample assessment of each mode by an OOS estimate, and fold-averaging further reduces the variance of these mode-wise proxies. This logic is not ad hoc: in the covariance setting, closely related holdout/CV eigenvalue-regularization schemes (NERCOME and variants) come with high-dimensional convergence guarantees, showing that the holdout/CV error approaches the nonlinear-shrinkage/oracle error under standard assumptions [[14](https://arxiv.org/html/2601.07687v1#bib.bib24 "Nonparametric eigenvalue-regularized precision or covariance matrix estimator"), [1](https://arxiv.org/html/2601.07687v1#bib.bib25 "Design-free estimation of variance matrices")].

Let {𝐗,𝐘}={𝐱t∈ℝnx,𝐲t∈ℝny}t=1Δ​tin\{\mathbf{X,\mathbf{Y\}=}}\{\mathbf{x}\_{t}\in\mathbb{R}^{n\_{x}},\mathbf{y}\_{t}\in\mathbb{R}^{n\_{y}}\}\_{t=1}^{\Delta t\_{\textrm{in}}} denote standardized observations on an in-sample window of length Δ​tin\Delta t\_{\textrm{in}}. We form the empirical cross-correlation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂^X​Y=1Δ​tin​∑t=1Δ​tin𝐱t​𝐲t⊤=𝐔^​diag​(𝐬^)​𝐕^⊤,\widehat{\mathbf{C}}\_{XY}=\frac{1}{\Delta t\_{\textrm{in}}}\sum\_{t=1}^{\Delta t\_{\textrm{in}}}\mathbf{x}\_{t}\mathbf{y}\_{t}^{\top}=\widehat{\mathbf{U}}\,\mathrm{diag}(\hat{\mathbf{s}})\,\widehat{\mathbf{V}}^{\top}, |  | (34) |

where 𝐬^=(s^1,…,s^r)\hat{\mathbf{s}}=(\hat{s}\_{1},\ldots,\hat{s}\_{r}) and r:=min⁡(nx,ny)r:=\min(n\_{x},n\_{y}) are the empirical singular values, and (𝐔^,𝐕^)(\widehat{\mathbf{U}},\widehat{\mathbf{V}}) are empirical singular-vector matrices. The oracle within the rotationally invariant class keeps the empirical singular vectors fixed and replaces s^k\hat{s}\_{k} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | sk⋆=𝐮^k⊤​𝐂X​Y​𝐯^k,s^{\star}\_{k}=\widehat{\mathbf{u}}\_{k}^{\top}\mathbf{C}\_{XY}\,\widehat{\mathbf{v}}\_{k}, |  | (35) |

where 𝐂X​Y\mathbf{C}\_{XY} denotes the population cross-correlation and (𝐮^k,𝐯^k)(\widehat{\mathbf{u}}\_{k},\widehat{\mathbf{v}}\_{k}) are the empirical singular vectors111When the Oracle is reported on real data, it is used only as an ex post lower bound for the achievable OOS MSE within the rotationally invariant class, and not to construct the cross-validated estimator. Accordingly, the unobservable population cross-correlation 𝐂X​Y\mathbf{C}\_{XY} in Eq. ([35](https://arxiv.org/html/2601.07687v1#S6.E35 "In 6.2 Cross-Validation Algorithm ‣ 6 Cross-validated Singular-Value Shrinkage ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) is replaced by the realized OOS cross-covariance/cross-correlation computed on the OOS window.. We estimate these oracle diagonals by CV.

We split the time index set {1,…,Δ​tin}\{1,\ldots,\Delta t\_{\textrm{in}}\} into κ\kappa disjoint folds. For each fold ff, we define training and test sets ℐtrain(f)\mathcal{I}^{(f)}\_{\mathrm{train}} and ℐtest(f)\mathcal{I}^{(f)}\_{\mathrm{test}} and compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂^X​Y,train(f)=1|ℐtrain(f)|​∑t∈ℐtrain(f)𝐱t​𝐲t⊤,𝐂^X​Y,test(f)=1|ℐtest(f)|​∑t∈ℐtest(f)𝐱t​𝐲t⊤.\widehat{\mathbf{C}}^{(f)}\_{XY,\mathrm{train}}=\frac{1}{|\mathcal{I}^{(f)}\_{\mathrm{train}}|}\sum\_{t\in\mathcal{I}^{(f)}\_{\mathrm{train}}}\mathbf{x}\_{t}\mathbf{y}\_{t}^{\top},\qquad\widehat{\mathbf{C}}^{(f)}\_{XY,\mathrm{test}}=\frac{1}{|\mathcal{I}^{(f)}\_{\mathrm{test}}|}\sum\_{t\in\mathcal{I}^{(f)}\_{\mathrm{test}}}\mathbf{x}\_{t}\mathbf{y}\_{t}^{\top}. |  | (36) |

Let the SVD of the training matrix be

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂^X​Y,train(f)=𝐔^train(f)​diag​(𝐬^train(f))​𝐕^train(f)⊤.\widehat{\mathbf{C}}^{(f)}\_{XY,\mathrm{train}}=\widehat{\mathbf{U}}^{(f)}\_{\mathrm{train}}\,\mathrm{diag}\!\big(\hat{\mathbf{s}}^{(f)}\_{\mathrm{train}}\big)\,\widehat{\mathbf{V}}^{(f)\top}\_{\mathrm{train}}. |  | (37) |

We then define fold-wise CV targets by projecting the held-out matrix onto the training singular directions,

|  |  |  |  |
| --- | --- | --- | --- |
|  | s~k(f):=𝐮^train,k(f)⊤​𝐂^X​Y,test(f)​𝐯^train,k(f),k=1,…,r,\tilde{s}^{(f)}\_{k}:=\widehat{\mathbf{u}}^{(f)\top}\_{\mathrm{train},k}\,\widehat{\mathbf{C}}^{(f)}\_{XY,\mathrm{test}}\,\widehat{\mathbf{v}}^{(f)}\_{\mathrm{train},k},\qquad k=1,\ldots,r, |  | (38) |

and average over folds,

|  |  |  |  |
| --- | --- | --- | --- |
|  | s~kCV:=1κ​∑f=1κs~k(f).\tilde{s}^{\mathrm{CV}}\_{k}:=\frac{1}{\kappa}\sum\_{f=1}^{\kappa}\tilde{s}^{(f)}\_{k}. |  | (39) |

Optionally, we enforce monotonicity of the shrinkage map by isotonic regression, fitting a non-decreasing sequence s~kiso\tilde{s}^{\mathrm{iso}}\_{k} to the pairs (s^k,s~kCV)(\hat{s}\_{k},\tilde{s}^{\mathrm{CV}}\_{k}). The final CV-cleaned estimator is reconstructed in the empirical singular-vector basis of the full-sample matrix,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂~X​YCV:=𝐔^​diag​(𝐬~iso)​𝐕^⊤.\widetilde{\mathbf{C}}^{\mathrm{CV}}\_{XY}:=\widehat{\mathbf{U}}\,\mathrm{diag}(\tilde{\mathbf{s}}^{\mathrm{iso}})\,\widehat{\mathbf{V}}^{\top}. |  | (40) |

This provides a stationary BBP-like baseline that is directly computable from data splits and projections and does not require boundedness of ‖𝚺‖op\|\mathbf{\Sigma}\|\_{\mathrm{op}}.

## 7 Synthetic Data Validation

Most of the benchmark models presented here are based on Ref. [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")]. These experiments are designed to verify the performance of the proposed NN shrinkage estimator within specific spectral regimes, ranging from finite-rank signals to heavy-tailed noise. For completeness, we included a fourth benchmark that includes a positive mode.

### 7.1 Synthetic Benchmarks

#### Benchmark I:Finite-Rank Spiked Models

The first set of benchmarks are reported as Models 1–5 in Ref. [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")]. We consider a Gaussian block model for (X,Y)∈ℝnx×ℝny(X,Y)\in\mathbb{R}^{n\_{x}}\times\mathbb{R}^{n\_{y}} with population covariance

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺:=(𝐈nx𝚺X​Y𝚺X​Y⊤𝚺X​Y⊤​𝚺X​Y+σ2​𝐈ny),\boldsymbol{\Sigma}:=\begin{pmatrix}\mathbf{I}\_{n\_{x}}&\boldsymbol{\Sigma}\_{XY}\\ \boldsymbol{\Sigma}\_{XY}^{\top}&\boldsymbol{\Sigma}\_{XY}^{\top}\boldsymbol{\Sigma}\_{XY}+\sigma^{2}\mathbf{I}\_{n\_{y}}\end{pmatrix}, |  | (41) |

with σ2=0.5\sigma^{2}=0.5 as in Ref. [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")]. The cross-block 𝚺X​Y\boldsymbol{\Sigma}\_{XY} is constructed as a finite-rank matrix with Haar-distributed singular vectors and a fraction ξ\xi of non-zero singular values (“spikes”): letting ρ:=⌊ξ​min⁡(nx,ny)⌋\rho:=\lfloor\xi\,\min(n\_{x},n\_{y})\rfloor,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺X​Y=𝐔​diag​(s1,…,sρ,0,…)​𝐕⊤,si​∼i.i.d.​Unif​[0.2,0.5],\boldsymbol{\Sigma}\_{XY}=\mathbf{U}\,\mathrm{diag}(s\_{1},\ldots,s\_{\rho},0,\ldots)\,\mathbf{V}^{\top},\qquad s\_{i}\overset{\mathrm{i.i.d.}}{\sim}\mathrm{Unif}[0.2,0.5], |  | (42) |

where 𝐔∈ℝnx×nx\mathbf{U}\in\mathbb{R}^{n\_{x}\times n\_{x}} and 𝐕∈ℝny×ny\mathbf{V}\in\mathbb{R}^{n\_{y}\times n\_{y}} are independent Haar orthogonal matrices.

This benchmark therefore fixes an isotropic and perfectly conditioned XX-marginal, while inducing a structured YY-marginal aligned with the cross-covariance directions plus an additional isotropic noise component σ2​𝐈ny\sigma^{2}\mathbf{I}\_{n\_{y}}; Panel A of Table [1](https://arxiv.org/html/2601.07687v1#S3.T1 "Table 1 ‣ 3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") reports performance as ξ\xi varies from 0%0\% to 40%40\%.

#### Benchmark II: Heavy-Tailed Bulk Models

The second family (Models 6–10 in Ref. [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")]) assesses performance under heavy-tailed regimes where the spectrum is broad and no explicit finite-rank spike component is planted. We define a rectangular matrix 𝐖\mathbf{W} of size n×2​nn\times 2n (with n:=nx+nyn:=n\_{x}+n\_{y}) with entries drawn from a distribution which is either standard Gaussian (Model 6) or a symmetric heavy-tailed law with tail exponent α\alpha (Models 7–10). The population covariance matrix of the concatenated vector (𝐗⊤,𝐘⊤)⊤(\mathbf{X}^{\top},\mathbf{Y}^{\top})^{\top} is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺:=12​n​𝐖𝐖⊤,\boldsymbol{\Sigma}:=\frac{1}{2n}\mathbf{W}\mathbf{W}^{\top}, |  | (43) |

and 𝚺X​X\boldsymbol{\Sigma}\_{XX}, 𝚺X​Y\boldsymbol{\Sigma}\_{XY}, 𝚺Y​Y\boldsymbol{\Sigma}\_{YY} denote its blocks under the partition n:=nx+nyn:=n\_{x}+n\_{y}. Lower values of α\alpha represent heavier tails. In this construction, any cross-dependence between 𝐗\mathbf{X} and 𝐘\mathbf{Y} is not driven by isolated spikes but instead emerges from the random anisotropy of 𝚺\boldsymbol{\Sigma}, whose eigenvalue distribution becomes increasingly dispersed as α\alpha decreases. Panel B of Table [1](https://arxiv.org/html/2601.07687v1#S3.T1 "Table 1 ‣ 3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") compares the estimators across varying tail exponents.

#### Benchmark III: White Heavy-Tailed Cross-Correlation Models

The third family (Models 11–15 in Ref. [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")]) isolates the cross-block estimation problem by enforcing spherical auto-covariance blocks while retaining the same cross-block induced by the heavy-tailed construction of Benchmark II. Starting from the population covariance 𝚺\boldsymbol{\Sigma} in Benchmark II, we extract the corresponding cross-block 𝚺X​Y\boldsymbol{\Sigma}\_{XY}. We then define a “white-marginals” population covariance by replacing the marginal blocks with scaled identities while keeping the cross-block fixed:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺:=(smax​𝐈nx𝚺X​Y𝚺X​Y⊤smax​𝐈ny),smax:=‖𝚺X​Y‖2.\boldsymbol{\Sigma}:=\begin{pmatrix}s\_{\max}\mathbf{I}\_{n\_{x}}&\boldsymbol{\Sigma}\_{XY}\\ \boldsymbol{\Sigma}\_{XY}^{\top}&s\_{\max}\mathbf{I}\_{n\_{y}}\end{pmatrix},\qquad s\_{\max}:=\left\|\boldsymbol{\Sigma}\_{XY}\right\|\_{2}. |  | (44) |

This construction removes any marginal anisotropy present in 𝚺X​X\boldsymbol{\Sigma}\_{XX} and 𝚺Y​Y\boldsymbol{\Sigma}\_{YY}. Panel C of Table [1](https://arxiv.org/html/2601.07687v1#S3.T1 "Table 1 ‣ 3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") reports the results as the tail exponent α\alpha (inherited from Benchmark II) varies across the values considered in Ref. [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")].

#### Benchmark IV: Gaussian Bulk Models with Common Mode

This benchmark starts from the Gaussian instance of Benchmark II (Model 6), i.e., the bulk-only construction with 𝐖\mathbf{W} i.i.d. standard normal and population covariance

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺(G):=12​n​𝐖𝐖⊤,n:=nx+ny.\boldsymbol{\Sigma}^{(G)}:=\frac{1}{2n}\mathbf{W}\mathbf{W}^{\top},\qquad n:=n\_{x}+n\_{y}. |  | (45) |

To emulate empirical “market-mode” behavior (a positive common component across all variables), we inject an equicorrelated mode through a multiplicative (congruence) transformation. For a mode strength m∈[0,1]m\in[0,1], we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐌:=(1−m)​𝐈n+m​𝟏𝟏⊤,\mathbf{M}:=(1-m)\mathbf{I}\_{n}+m\mathbf{1}\mathbf{1}^{\top}, |  | (46) |

and set

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺(M)=𝐌1/2​𝚺(G)​𝐌1/2,𝐃:=diag​(𝚺(M)),𝚺=𝐃−1/2​𝚺(M)​𝐃−1/2.\boldsymbol{\Sigma}^{(M)}=\mathbf{M}^{1/2}\,\boldsymbol{\Sigma}^{(G)}\,\mathbf{M}^{1/2},\qquad\mathbf{D}:=\mathrm{diag}\left(\boldsymbol{\Sigma}^{(M)}\right),\qquad\boldsymbol{\Sigma}=\mathbf{D}^{-1/2}\,\boldsymbol{\Sigma}^{(M)}\,\mathbf{D}^{-1/2}. |  | (47) |

Here 𝐌1/2\mathbf{M}^{1/2} denotes the unique positive definite square root of 𝐌\mathbf{M}, and the diagonal normalization 𝐃−1/2​(⋅)​𝐃−1/2\mathbf{D}^{-1/2}(\cdot)\mathbf{D}^{-1/2} rescales the result to unit diagonal (correlation form). Finally, we extract by 𝚺X​X\boldsymbol{\Sigma}\_{XX}, 𝚺X​Y\boldsymbol{\Sigma}\_{XY}, and 𝚺Y​Y\boldsymbol{\Sigma}\_{YY} the blocks of 𝚺\boldsymbol{\Sigma} under the partition n:=nx+nyn:=n\_{x}+n\_{y}.

### 7.2 Training on Synthetic Data

We train an NN model for each benchmark described above. The training uses batches that are generated on the fly, so the network is effectively exposed to a virtually unbounded stream of non-repeated observations. This design mitigates memorization of a finite training set and helps the learned shrinkage map generalize across the benchmark’s parameter range.

The total system dimension is sampled uniformly from n∼𝒰​[50,500]n\sim\mathcal{U}[50,500], and the sample length is sampled from Δ​tin∼𝒰​[200,1200]\Delta t\_{\textrm{in}}\sim\mathcal{U}[200,1200] every batch. The relative dimension is drawn as ν∼𝒰​[0.05,0.95]\nu\sim\mathcal{U}[0.05,0.95], and to ensure broad coverage, the spike percentage ξ\xi is sampled uniformly on every instance from 𝒰​[0.2,0.35]\mathcal{U}[0.2,0.35] for model I, and the tail exponent α\alpha is uniformly sampled from 𝒰​[1.5,2.5]\mathcal{U}[1.5,2.5] for models II and II models; finally, the mode mm of model IV is sampled unifomely in 𝒰​[0.2,0.3]\mathcal{U}[0.2,0.3],

The neural network’s weights are optimized using the Adam optimizer with an initial learning rate of 0.0010.001 and an exponential decay rate of 0.990.99 per epoch over 50 epochs. We employ gradient accumulation over 44 steps with a base batch size of 3232 (resulting in an effective batch size of 128128) to allow for multiple shapes (n,Δ​tinn,\Delta t\_{\textrm{in}}) within the same effective batch.

For testing (Table [1](https://arxiv.org/html/2601.07687v1#S3.T1 "Table 1 ‣ 3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")), we set nx=200n\_{x}=200, ny=350n\_{y}=350, and Δ​tin=500\Delta t\_{\textrm{in}}=500 as in Ref. [[2](https://arxiv.org/html/2601.07687v1#bib.bib5 "Optimal cleaning for singular values of cross-covariance matrices")]. While the dimensions nn and Δ​tin\Delta t\_{\textrm{in}} are set roughly around their training ranges, the benchmark parameters (ξ,α,m)(\xi,\alpha,m) are tested out of the training distribution.

## 8 Market Data Validation

### 8.1 Universe Selection

The data filtering procedure largely follows Ref. [[5](https://arxiv.org/html/2601.07687v1#bib.bib7 "End-to-end large portfolio optimization for variance minimization with neural networks through covariance cleaning")]. Our objective is to construct a time-varying investable universe that enforces (i) stable short-term liquidity and (ii) sufficiently long and homogeneous trading histories, while aiming to mitigate lookahead biases in the selection process.

The dataset comprises all NYSE- and NASDAQ-listed equities from January 1, 1990, to December 31, 2024, including ADRs, and excludes ETFs, funds, and non-operating vehicles. Only common shares are retained. To avoid the main source of look-ahead bias, the eligible universe on each day tt is determined using information available strictly prior to tt, and any stock that will be delisted within the subsequent Δ​tout=240\Delta t\_{\text{out}}=240 trading days is excluded. While this screening necessarily introduces a mild survivorship bias, our objective is to assess cross-covariance estimation and forecasting accuracy rather than to backtest a tradable investment strategy; accordingly, we expect its impact on our conclusions to be limited. See Appendix [8.1.1](https://arxiv.org/html/2601.07687v1#S8.SS1.SSS1 "8.1.1 Delisting Risk and Alternative Remedies ‣ 8.1 Universe Selection ‣ 8 Market Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") for a discussion of the alternatives.

Each candidate stock must exhibit a stable trading history over the full five-year lookback window. In particular, within every rolling one-year subwindow, the stock must participate in the closing auction on at least 95%95\% of trading days. This removes securities with fragmented price histories arising from recent IPOs, prolonged suspensions, ticker changes, or other corporate events. Additional liquidity requirements are imposed on the most recent 5​–​2205\text{--}220 days: the closing auction must execute each day, daily traded volume must exceed 1%1\% of both shares outstanding and market capitalization, the prior-day share price must satisfy (10≤pt−1≤2000)(10\leq p\_{t-1}\leq 2000) USD, and the number of shares outstanding must exceed 55 million. These constraints prevent the inclusion of illiquid or distressed securities that would lead to unstable cross-covariance estimates.

To avoid degeneracies in the covariance matrices, we remove stocks with almost zero short-term variance. Such cases, typically acquisition targets trading near their offer price, flatten the volatility structure and collapse multivariate optimization problems into trivial univariate ones. We eliminate all securities whose log-standard-deviation falls below 1.51.5 IQRs of the cross-sectional distribution, computed over both 55- and 2020-day windows. We also retain only one share class per issuer (selecting the class with the highest market capitalization) and remove the lower-cap member of any pair with in-sample correlation greater than 0.950.95.

After applying all filters, the remaining stocks are ranked by market capitalization, and the top 10001000 are selected each trading day. The universe size is therefore fixed at 10001000, though membership naturally changes over time, particularly near the lower tail of the size distribution. The final panel spans 1995−20241995-2024, comprising roughly 2.72.7 million stock–day observations and approximately 4,0004,000 unique securities.

#### 8.1.1 Delisting Risk and Alternative Remedies

In the stock-selection step, we restrict the OOS universe to names for which returns are observed throughout the full one-year OOS window, thereby avoiding mechanically missing observations induced by delistings. This choice introduces a mild look-ahead (survivorship) bias, since survival over the OOS horizon is implicitly conditioned on future information. There are, however, three practical ways to remove this bias.

One option is to shorten the OOS horizon to a window that does not exceed the public-notice period preceding an exchange delisting; in particular, delisting via Form 25 becomes effective 10 days after filing and exchanges are required to provide public notice no fewer than 10 days in advance [[18](https://arxiv.org/html/2601.07687v1#bib.bib26 "17 CFR §240.12d2-2 – Removal from Listing and Registration")], so an OOS window on the order of 10 days limits the amount of forward-looking conditioning, at the cost of higher variance in the learning signal due to fewer OOS observations.

A second option is to estimate correlations using pairwise-overlapping observations (i.e., computing each product only over dates on which both series are observed), which eliminates the need to pre-filter for full-horizon availability but can yield an indefinite “correlation” estimate with negative eigenvalues; since our objective is an MSE criterion against a target and feasibility is enforced downstream, this alternative target need not be detrimental in principle, although it changes the estimation problem.

A third option is to keep the present protocol for training (to maintain strict comparability across methods) and, at the application stage, quantify sensitivity by relaxing the survivorship restriction in the OOS evaluation and reporting how performance varies with the degree of testing-time rigor.

At the current stage, where we do not yet map forecasts into a trading strategy with a well-defined economic objective, this last dimension is secondary, because we lack an external criterion that would justify selecting one debiasing protocol over another.

### 8.2 Training on Real Market Data

The model is trained under a walk-forward optimization protocol on a universe of U.S. equities, with an OOS evaluation spanning 2017–2024. We fit a sequence of 7 distinct models using an expanding training window. Specifically, at each iteration, the network is trained from scratch on data from 1995 up to the year immediately preceding the corresponding test segment; the training set is then expanded, and the procedure is repeated for the next iteration.

To ensure that the model learns to operate across varying problem dimensions, we adopt a stochastic dynamic sampling strategy. In each training batch, the total number of assets is drawn uniformly at random as n∼𝒰​[50,500]n\sim\mathcal{U}[50,500]. This set is partitioned into two disjoint groups, 𝐗\mathbf{X} and 𝐘\mathbf{Y}, according to a random relative dimension ν∼𝒰​[0.05,0.95]\nu\sim\mathcal{U}[0.05,0.95]. The lookback window length is sampled every batch in the range Δ​tin∼𝒰​[200,1200]\Delta t\_{\textrm{in}}\sim\mathcal{U}[200,1200] days.

The inputs are the empirical correlation matrices computed from daily adjusted-close returns. Specifically, we estimate the in-sample correlation matrices 𝐂^x​x\widehat{\mathbf{C}}\_{xx} and 𝐂^y​y\widehat{\mathbf{C}}\_{yy}, together with the in-sample cross-correlation matrix 𝐂^x​y\widehat{\mathbf{C}}\_{xy}, all computed over a window of length Δ​tin\Delta t\_{\mathrm{in}}. These three matrices are provided as input to the network. The model outputs a cleaned estimate of the cross-correlation, which is trained by minimizing the MSE with respect to the realized OOS target 𝐂x​yOOS\mathbf{C}\_{xy}^{\mathrm{OOS}}, computed over a future hold-out window of Δ​tout=240\Delta t\_{\mathrm{out}}=240 trading days.

When explicitly testing the role of non-stationarity, the pipeline above is modified through a shuffling procedure designed to destroy temporal structure while preserving the daily cross-sectional distribution of returns. Concretely, we first merge the IS and OOS segments into a single pool of trading days (each day represented by the full vector of cross-sectional returns), and then apply a random permutation to these days. We then re-split the permuted sequence into in-sample and OOS windows with the same lengths as in the original protocol. From these reshuffled returns, we recompute the corresponding empirical input matrices (𝐂^x​x,𝐂^y​y,𝐂^x​y)(\widehat{\mathbf{C}}\_{xx},\widehat{\mathbf{C}}\_{yy},\widehat{\mathbf{C}}\_{xy}) and the realized target 𝐂x​yOOS\mathbf{C}\_{xy}^{\mathrm{OOS}} using the same estimators and window lengths as above. By construction, the resulting IS and OOS sets are drawn from the same distribution and therefore differ only through finite-sample fluctuations (i.e., sampling noise induced by finite Δ​tin\Delta t\_{\mathrm{in}} and Δ​tout\Delta t\_{\mathrm{out}}).

Finally, the neural network’s weights are optimized using the Adam optimizer with an initial learning rate of 0.0010.001 and an exponential decay rate of 0.990.99 per epoch over 50 epochs. We employ gradient accumulation over 44 steps with a base batch size of 3232 (resulting in an effective batch size of 128128) to allow for multiple shapes (n,Δ​tinn,\Delta t\_{\textrm{in}}) within the same effective batch.

### 8.3 Market-Mode Removal as a Boundedness Diagnostic

![Refer to caption](x6.png)

![Refer to caption](x7.png)

![Refer to caption](x8.png)

![Refer to caption](x9.png)

Figure 3: OOS MSE for cross-correlation estimators on financial data covering 2017–2024 with the market mode removed. For each test window, the estimator is trained on an expanding sample from 1995 up to the year immediately preceding the test period, and the reported value averages 1,000 independent runs for each OOS year. The left panels preserve the chronological order between in-sample and OOS windows, whereas the right panels shuffle dates. The upper panels vary the total number of assets for ν=0.25\nu=0.25, while the lower panels vary the relative dimension ν\nu for n=1000n=1000. The error bars indicate a 95%95\% bootstrap confidence interval.

In the market experiment of Section [3](https://arxiv.org/html/2601.07687v1#S3 "3 Validation on Synthetic and Market Data ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"), the analytical BBP shrinkage deteriorates sharply as the system size increases, and can even underperform the unfiltered MLE. Our working hypothesis is that this is not primarily a consequence of temporal non-stationarity, but rather a structural failure induced by the presence of a macroscopic market mode. In particular, a strong common component can violate the boundedness assumption required by the BBP asymptotics (cf. Appendix [6.1](https://arxiv.org/html/2601.07687v1#S6.SS1 "6.1 Boundness in the Presence of a Mode ‣ 6 Cross-validated Singular-Value Shrinkage ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")), making the corresponding shrinkage map unstable in finite samples. To test this mechanism directly, we repeat the full real-data pipeline after explicitly removing the market mode from returns, and we re-train the neural estimator on the transformed data to keep the comparison protocol unchanged.

Let Ri,tR\_{i,t} denote the raw daily return of asset i∈{1,…,n}i\in\{1,\dots,n\} on day t∈{1,…,Δ​tin}t\in\{1,\dots,\Delta t\_{\textrm{in}}\} within a given estimation window. We define the market mode operationally as the cross-sectional mean return on each day and subtract it from every asset,

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^t:=1n​∑i=1nRi,t,Ri,t(0):=Ri,t−μ^t.\hat{\mu}\_{t}:=\frac{1}{n}\sum\_{i=1}^{n}R\_{i,t},\qquad R^{(0)}\_{i,t}:=R\_{i,t}-\hat{\mu}\_{t}. |  | (48) |

This transformation is applied independently within each window, both in-sample and OOS. From the mode-removed returns {Ri,t(0)}\{R^{(0)}\_{i,t}\} we then recompute the same empirical input matrices as in the baseline protocol, namely (𝐂^x​x,𝐂^y​y,𝐂^x​y)(\widehat{\mathbf{C}}\_{xx},\widehat{\mathbf{C}}\_{yy},\widehat{\mathbf{C}}\_{xy}) on an in-sample window of length Δ​tin\Delta t\_{\mathrm{in}}, as well as the realized target 𝐂x​yOOS\mathbf{C}^{\mathrm{OOS}}\_{xy} on a subsequent hold-out window of length Δ​tout=240\Delta t\_{\mathrm{out}}=240 trading days, leaving all estimators unchanged. The NN is trained again under the identical walk-forward expanding-window scheme described in Appendix C.2 (including the same dynamic batching over (n,ν,Δ​tin)(n,\nu,\Delta t\_{\textrm{in}})), so that any performance change can be attributed to the preprocessing rather than to a modified learning protocol.

Figure [3](https://arxiv.org/html/2601.07687v1#S8.F3 "Figure 3 ‣ 8.3 Market-Mode Removal as a Boundedness Diagnostic ‣ 8 Market Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") reports the resulting OOS MSE for 2017–2024, averaging 1,0001{,}000 independent runs per OOS year. In this mode-removed regime, the gross BBP underperformance is substantially reduced: the sharp deterioration observed in the raw-return experiment is no longer present, and BBP becomes again competitive with the other cleaners across both the nn-sweep (at fixed ν\nu) and the ν\nu-sweep (at fixed n=1000n=1000).

Importantly, this improvement does not eliminate the systematic gap to the learned estimator when the data are kept in the original chronological order. Across most problem sizes, both BBP and the CV-based shrinkage remain consistently worse than the NN in OOS MSE. The only notable exception occurs at n=1000n=1000, where BBP attains NN-level performance and can even marginally outperform it. This regime, however, is decisively out-of-distribution for the network, since training batches were restricted to n≤500n\leq 500; as a consequence, the n=1000n=1000 comparison probes a different spectral scale than the one observed during training and should be interpreted as a robustness stress test rather than an in-distribution performance claim.

### 8.4 Feasibility Diagnostic via Canonical-Correlation Boundedness

![Refer to caption](x10.png)

![Refer to caption](x11.png)

![Refer to caption](x12.png)

![Refer to caption](x13.png)

Figure 4: Feasibility diagnostic for the reconstructed cross–correlation block. Top row: empirical distributions of canonical singular values (singular values of the whitened block 𝐂~X​Y(w)\widetilde{\mathbf{C}}^{(w)}\_{XY} obtained via Eq. ([25](https://arxiv.org/html/2601.07687v1#S5.E25 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets"))) for the original chronological pipeline (left) and the shuffled control (right). Bottom row: cleaned singular values in the unwhitened domain plotted against the empirical singular values, again for the original pipeline (left) and the shuffled control (right).

Appendix [5.3](https://arxiv.org/html/2601.07687v1#S5.SS3 "5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") characterizes when a candidate cross–correlation block is compatible with fixed marginal correlation matrices. Specifically, for given marginals 𝐂^X​X≻𝟎\widehat{\mathbf{C}}\_{XX}\succ\mathbf{0} and 𝐂^Y​Y≻𝟎\widehat{\mathbf{C}}\_{YY}\succ\mathbf{0}, feasibility of a cleaned cross–block 𝐂~X​Y\widetilde{\mathbf{C}}\_{XY} is equivalent to positive semidefiniteness of the associated block correlation matrix in Eq. ([24](https://arxiv.org/html/2601.07687v1#S5.E24 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")). By the whitening reduction in Eq. ([25](https://arxiv.org/html/2601.07687v1#S5.E25 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")), this constraint is in turn equivalent to boundedness of the singular values of the whitened block, i.e., the canonical correlations must satisfy 0≤sk(w)≤10\leq s^{(w)}\_{k}\leq 1 as stated in Eq. ([29](https://arxiv.org/html/2601.07687v1#S5.E29 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) (and the strict inequality in Eq. ([30](https://arxiv.org/html/2601.07687v1#S5.E30 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) suffices for positive definiteness).

We use this result as an ex–post diagnostic for the neural estimator in the market experiment. We consider 3,2003{,}200 OOS realizations produced by the final walk-forward model (trained on the longest available history), fixing n=300n=300, ν=0.3\nu=0.3, and Δ​tin=1000\Delta t\_{\textrm{in}}=1000. For each realization we form (𝐂^X​X,𝐂^Y​Y,𝐂^X​Y)(\widehat{\mathbf{C}}\_{XX},\widehat{\mathbf{C}}\_{YY},\widehat{\mathbf{C}}\_{XY}), apply the network to obtain 𝐂~X​Y\widetilde{\mathbf{C}}\_{XY}, whiten it by applying Eq. ([25](https://arxiv.org/html/2601.07687v1#S5.E25 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")) with (𝐂^X​X,𝐂^Y​Y,𝐂~X​Y)(\widehat{\mathbf{C}}\_{XX},\widehat{\mathbf{C}}\_{YY},\widetilde{\mathbf{C}}\_{XY}), and record the singular values of the resulting 𝐂~X​Y(w)\widetilde{\mathbf{C}}^{(w)}\_{XY}. Figure [4](https://arxiv.org/html/2601.07687v1#S8.F4 "Figure 4 ‣ 8.4 Feasibility Diagnostic via Canonical-Correlation Boundedness ‣ 8 Market Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") (top left) shows that the canonical singular values are overwhelmingly feasible: 99.96%99.96\% of them lie in [0,1][0,1], only 0.04%0.04\% exceed 11, and none fall below 0. Hence, feasibility violations are extremely rare, and the reconstructed block matrix is almost always positive semidefinite in the sense of Eq. ([24](https://arxiv.org/html/2601.07687v1#S5.E24 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")).

Importantly, this diagnostic is not equivalent to requiring a shrinkage condition (s~k≤s^k\tilde{s}\_{k}\leq\widehat{s}\_{k}) in the unwhitened singular spectrum. Indeed, Figure [4](https://arxiv.org/html/2601.07687v1#S8.F4 "Figure 4 ‣ 8.4 Feasibility Diagnostic via Canonical-Correlation Boundedness ‣ 8 Market Data Validation ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets") (bottom left) shows that the learned map can produce s~k>s^k\tilde{s}\_{k}>\widehat{s}\_{k} for a non-negligible set of directions, which would be ruled out by a multiplicative sigmoid parametrization s~k=s^k​σ​(⋅)\tilde{s}\_{k}=\widehat{s}\_{k}\,\sigma(\cdot). This behavior is nonetheless compatible with feasibility because positive semidefiniteness is controlled by the canonical bound of Eq. ([29](https://arxiv.org/html/2601.07687v1#S5.E29 "In 5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets")), not by an ordering between unwhitened singular values. The latter type of inequality is specific to purely denoising interpretations under stationarity assumptions, whereas here the network is trained against an OOS target and may optimally amplify some directions while still satisfying the feasibility constraint implied by Appendix [5.3](https://arxiv.org/html/2601.07687v1#S5.SS3 "5.3 Admissible Singular Values Under Fixed Marginals ‣ 5 BBP Analytical Cleaner as a Limiting Case of the Two-Stream NN ‣ Physics-Informed Singular-Value Learning for Cross-Covariances Forecasting in Financial Markets").

Finally, in the shuffled control (where the chronological structure is destroyed), the feasibility diagnostic becomes exact: no canonical singular values fall outside [0,1][0,1] (top right). In addition, the predicted singular values become automatically monotone (bottom right), without requiring isotonic post-processing, and closely resemble the stationary BBP-like shrinkage. The remaining discrepancy concentrates in the leading modes, which are associated with the market component and are precisely the directions where BBP is most fragile in the real-data benchmarks.