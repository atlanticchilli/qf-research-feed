---
authors:
- Luis Ontaneda Mijares
- Nick Firoozye
doc_id: arxiv:2601.22200v1
family_id: arxiv:2601.22200
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning
  in Non-stationary Time-series'
url_abs: http://arxiv.org/abs/2601.22200v1
url_html: https://arxiv.org/html/2601.22200v1
venue: arXiv q-fin
version: 1
year: 2026
---


Luis Ontaneda Mijares
  
University College London
  
luis.ont.mij@gmail.com
  
Nick Firoozye
  
Department of Computer Science, University College London
  
n.firoozye@ucl.ac.uk

###### Abstract

Overparameterized models have recently challenged conventional learning theory by exhibiting improved generalization beyond the interpolation limit, a phenomenon known as *benign overfitting*.
This work introduces *Adaptive Benign Overfitting (ABO)*, extending the recursive least-squares (RLS) framework to this regime through a numerically stable formulation based on orthogonal–triangular updates.
A QR-based exponentially weighted RLS (QR–EWRLS) algorithm is introduced, combining random Fourier feature mappings with forgetting-factor regularization to enable online adaptation under non-stationary conditions.
The orthogonal decomposition prevents the numerical divergence associated with covariance-form RLS while retaining adaptability to evolving data distributions.
Experiments on nonlinear synthetic time series confirm that the proposed approach maintains bounded residuals and stable condition numbers while reproducing the double-descent behavior characteristic of overparameterized models. Applications to forecasting foreign exchange and electricity demand show that ABO is highly accurate (comparable to baseline kernel methods) while achieving speed improvements of between 20% to 40%. The results provide a unified view linking adaptive filtering, kernel approximation, and benign overfitting within a stable online learning framework.

## 1 Introduction

Adaptive filtering, or equivalently online regression, underpins modern signal processing, control, and sequential prediction.
As modern systems operate increasingly in high-dimensional and non-stationary environments, classical stability–bias trade-offs no longer retain their relevance; it is possible to interpolate without overfitting. In this work, we revisit the Recursive Least Squares (RLS) framework through the lens of overparameterization, linking adaptive filtering with the recent theory of benign overfitting, thereby deriving a fast and practical way of doing online inference in large feature models for non-stationary time series.

### 1.1 Benign Overfitting

The phenomenon of *benign overfitting*—where models generalize well despite perfectly interpolating their training data—has reshaped our understanding of generalization in high-dimensional learning.
The associated *double-descent* behavior, in which test error decreases again beyond the interpolation threshold, was first observed in deep neural networks [[39](https://arxiv.org/html/2601.22200v1#bib.bib39), [5](https://arxiv.org/html/2601.22200v1#bib.bib5), [4](https://arxiv.org/html/2601.22200v1#bib.bib4)] and later formalized for linear and kernel models [[15](https://arxiv.org/html/2601.22200v1#bib.bib15), [24](https://arxiv.org/html/2601.22200v1#bib.bib24)].
Even in simple least-squares regression, overparameterization can yield low risk (test-set error
as measured by the MSE) under mild spectral conditions on the covariance matrix.

In linear regression, benign overfitting is often analyzed through the minimum-norm, or ridgeless, estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | β^=limλ→0arg​minβ⁡(∑t‖yt−Xt​β‖2+λ​‖β‖2)\hat{\beta}=\lim\_{\lambda\to 0}\operatorname\*{\mathrm{arg\,min}}\_{\beta}\bigl(\sum\_{t}\|y\_{t}-X\_{t}\beta\|^{2}+\lambda\|\beta\|^{2}\bigr) |  | (1) |

which is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | β^=arg​minβ⁡‖β‖2s.t. ​y=X​β\hat{\beta}=\operatorname\*{\mathrm{arg\,min}}\_{\beta}\|\beta\|^{2}\quad\text{s.t. }y=X\beta |  | (2) |

In the case where XX is a N×DN\times D Gaussian i.i.d. random matrix with N/D→γ<1N/D\to\gamma<1 as N,D→∞N,D\to\infty, the test error can decrease as DD increases, provided that the spectrum of X⊤​XX^{\top}X remains well-behaved111with a sizeable number of large singular values and an arbitrarily large number of small, but not vanishing
singular values.
This phenomenon reveals that overparameterization can act as an implicit regularizer, replacing explicit shrinkage with spectral smoothing.

Although the analysis of benign overfitting was first established in static settings, analogous behavior arises naturally in adaptive and online learning.
Recursive Least Squares (RLS) and its exponentially weighted variant (EWRLS) [[17](https://arxiv.org/html/2601.22200v1#bib.bib17), [28](https://arxiv.org/html/2601.22200v1#bib.bib28)] continuously update regression coefficients as new data arrive, effectively performing a streaming analogue of ridge regression.
Their stability and their ability to generalize when overparameterized remain key questions motivating this work.

These findings, in the context of non-stationary time series, may explain why increasing model width, reducing effective condition numbers, improves generalization, particularly when noise directions are broad enough to absorb variance orthogonal to the principal components.

### 1.2 From Kernel Regression to Neural Tangent Kernels

Before introducing neural and random-feature analogues, it is helpful to recall that least-squares estimation can be viewed as kernel regression with a linear kernel.
Extending this concept to nonlinear feature maps yields kernel methods,
where generalization is governed by the eigenvalue spectrum of the kernel matrix
rather than the raw design matrix [[26](https://arxiv.org/html/2601.22200v1#bib.bib26), [16](https://arxiv.org/html/2601.22200v1#bib.bib16)].
This kernel perspective forms the foundation for both the *Neural Tangent Kernel (NTK)* and its efficient approximation via *Random Fourier Features (RFFs)*.

### 1.3 From Neural Tangent Kernels to Random Features

The Neural Tangent Kernel (NTK) framework [[22](https://arxiv.org/html/2601.22200v1#bib.bib22)] interprets the gradient-descent dynamics of the training of DNNs
in the infinite-width limit as kernel regression with a specific data-dependent kernel in a Reproducing Kernel Hilbert Space (RKHS).
The convergence and generalization properties of overparameterized neural networks can thus be analyzed through the spectral properties of the corresponding NTKs.
This viewpoint provides a direct bridge between deep learning and classical kernel theory, explaining why overparameterized neural networks behave like data-dependent kernel machines.

Kernel methods, however, scale poorly with dataset size due to the need to compute and invert large kernel matrices and
a computationally tractable analogue was introduced by *Random Fourier Features* (RFFs) [[27](https://arxiv.org/html/2601.22200v1#bib.bib27)], which approximate shift-invariant kernels through random sinusoidal bases derived from Böchner’s theorem.
Given features z​(x)∈ℝDz(x)\in\mathbb{R}^{D}, regression proceeds via

|  |  |  |
| --- | --- | --- |
|  | minβ⁡‖y−Z​β‖2+λ​‖β‖2\min\_{\beta}\|y-Z\beta\|^{2}+\lambda\|\beta\|^{2} |  |

where ZZ has fixed width independent of sample size.
RFFs therefore retain much of the expressive power of kernel methods while remaining computationally efficient. The study of RFFs in the overparameterized regime has revealed parallels with NTKs and deep networks, including benign overfitting and double-descent phenomena.

### 1.4 Double Descent in RFFs

Random Fourier Features can be interpreted as two-layer neural networks
with trigonometric activation functions; alternative nonlinearities such
as ReLU and leaky-ReLU are also viable [[32](https://arxiv.org/html/2601.22200v1#bib.bib32)]. Their
computational simplicity, together with universal-approximation
guarantees for infinitely wide networks [[8](https://arxiv.org/html/2601.22200v1#bib.bib8), [21](https://arxiv.org/html/2601.22200v1#bib.bib21)], makes RFFs an ideal setting for studying
behavior in the interpolating and non-classical regimes. In particular,
RFFs exhibit the same *double-descent* phenomenon observed in
overparameterized neural networks [[15](https://arxiv.org/html/2601.22200v1#bib.bib15), [4](https://arxiv.org/html/2601.22200v1#bib.bib4)].

To set notation, the minimum-norm interpolator is

|  |  |  |
| --- | --- | --- |
|  | y^=X​β^,β^=(X⊤​X)†​X⊤​y\hat{y}=X\hat{\beta},\qquad\hat{\beta}=(X^{\top}X)^{\dagger}X^{\top}y |  |

A convenient unifying viewpoint comes from ridge regression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β^\displaystyle\hat{\beta} | =limλ→0+(X⊤​X+λ​I)−1​X⊤​y\displaystyle=\lim\_{\lambda\to 0^{+}}(X^{\top}X+\lambda I)^{-1}X^{\top}y |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =X†​y\displaystyle=X^{\dagger}y |  |

This limit always returns the Moore–Penrose minimum-norm solution and
therefore covers both regimes:

* •

  Classical regime (D≤ND\leq N):
  X⊤​XX^{\top}X is nonsingular and
  X†=(X⊤​X)−1​X⊤X^{\dagger}=(X^{\top}X)^{-1}X^{\top}
* •

  Overparameterized regime (D>ND>N):
  X⊤​XX^{\top}X is singular and the pseudoinverse is required.

In both cases the fundamental identity

|  |  |  |
| --- | --- | --- |
|  | (X⊤​X)†​X⊤=X†(X^{\top}X)^{\dagger}X^{\top}=X^{\dagger} |  |

ensures a consistent form of the estimator.

Empirically, RFFs display the characteristic double-descent curve:

* •

  training error decreases monotonically until the interpolation
  threshold;
* •

  test error follows the classical U-shape, peaking at
  interpolation;
* •

  beyond interpolation, test error decreases again as the model
  becomes increasingly overparameterized.

![Refer to caption](DoubleDescent.png)


Figure 1: Illustration of the double-descent phenomenon in Random Fourier Features.

Double descent occurs across many random-feature constructions.
Although pseudoinverse computation becomes more expensive in the wide
regime, it also reveals how large feature sets can regularize the
estimator. generalization performance is closely tied to the
*effective condition number* of X⊤​XX^{\top}X: empirical and
theoretical analyses [[19](https://arxiv.org/html/2601.22200v1#bib.bib19)] show that test
error peaks precisely when this condition number is largest at
interpolation. As the number of features increases, the effective
condition number typically decreases, explaining the improved test error
in the overparameterized regime.

Not all settings exhibit double descent. Asymptotic theories
[[4](https://arxiv.org/html/2601.22200v1#bib.bib4)] require specific spectral properties—a few
dominant singular values and many moderate ones. If these are violated
(for example, by including extremely high deterministic frequencies),
performance may degrade. Feature weighting [[19](https://arxiv.org/html/2601.22200v1#bib.bib19)]
or bandwidth control through the RFF parameter σ\sigma mitigate this
effect: small σ\sigma leads to smoother representations, while
large σ\sigma yields highly oscillatory features that require more
samples to generalize. Thus, σ\sigma acts as a bias–variance
hyperparameter.

Finally, the behavior of RFFs can also be understood through their
Fourier-analytic origin. Let f​(t)f(t) be a square-integrable function
with Fourier transform

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f^​(ω)\displaystyle\hat{f}(\omega) | =12​π​∫f​(t)​ei​ω​t​𝑑t,\displaystyle=\frac{1}{\sqrt{2\pi}}\int f(t)\,e^{i\omega t}\,dt, |  | (3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(t)\displaystyle f(t) | =12​π​∫f^​(ω)​e−i​ω​t​𝑑ω\displaystyle=\frac{1}{\sqrt{2\pi}}\int\hat{f}(\omega)\,e^{-i\omega t}\,d\omega |  | (4) |

To connect this with kernels, note that a shift-invariant kernel
k​(xt−xs)=g​(t−s)k(x\_{t}-x\_{s})=g(t-s) is fully characterized by its lag-domain profile
g​(τ)g(\tau), which plays the role of a stationary “signal” defined on
time-lags. By Bochner’s theorem,

|  |  |  |
| --- | --- | --- |
|  | g​(τ)=∫p​(ω)​ei​ω​τ​𝑑ωg(\tau)=\int p(\omega)\,e^{i\omega\tau}\,d\omega |  |

where p​(ω)p(\omega) is the spectral density of the kernel. For the case of RBFNets, ω∼𝒩​(0,γ2)\omega\sim\mathcal{N}(0,\gamma^{2}). We note that in the general case of sampling from RFFs, the choice of γ\gamma is a form of regularization, preventing unnecessary high-frequency oscillations in the resulting interpolants (see for example [[19](https://arxiv.org/html/2601.22200v1#bib.bib19)]).

Random
Fourier Features approximate this integral via Monte Carlo sampling.
Defining

|  |  |  |
| --- | --- | --- |
|  | φ​(x)=2m​[cos⁡(ω1⊤​x+b1),…,cos⁡(ωm⊤​x+bm)]⊤\varphi(x)=\sqrt{\frac{2}{m}}\,\bigl[\cos(\omega\_{1}^{\top}x+b\_{1}),\,\ldots,\,\cos(\omega\_{m}^{\top}x+b\_{m})\bigr]^{\top} |  |

with ωj∼p\omega\_{j}\sim p and bj∼Unif​[0,2​π]b\_{j}\sim\mathrm{Unif}[0,2\pi].

Then

|  |  |  |
| --- | --- | --- |
|  | k​(xt−xs)≈φ​(xt)⊤​φ​(xs)k(x\_{t}-x\_{s})\approx\varphi(x\_{t})^{\top}\varphi(x\_{s}) |  |

so RFFs may be interpreted as a random discretization of the Fourier
representation of the kernel’s lag-domain signal.

### 1.5 Online Learning and Non-stationarity

Many real-world systems, such as financial, physiological, or environmental processes, are inherently *non-stationary*.
Exponentially Weighted RLS (EWRLS) adapts to such dynamics through a forgetting factor λ<1\lambda<1 that down-weights older data, enabling the tracking of time-varying correlations and structural breaks.

This study is motivated by the need for efficient forecasting methods for non-stationary time series commonly encountered in financial markets.
Classical tools for analysing and decomposing non-stationary signals, widely used in communications, acoustics, and signal processing, include:

* •

  Short-Time Fourier Transform (STFT): a windowed Fourier transform,

  |  |  |  |
  | --- | --- | --- |
  |  | f^λ​(t,ω)=12​π​∫−∞∞ϕλ​(t−s)​f​(s)​e−i​ω​s​𝑑s,\hat{f}\_{\lambda}(t,\omega)=\frac{1}{\sqrt{2\pi}}\int\_{-\infty}^{\infty}\phi\_{\lambda}(t-s)f(s)e^{-i\omega s}\,ds, |  |

  where the window function ϕλ​(r)=ϕ​(λ​r)\phi\_{\lambda}(r)=\phi(\lambda r) is often Gaussian with standard deviation 1/λ1/\lambda, although one-sided exponential kernels ϕλ​(r)=e−λ​r\phi\_{\lambda}(r)=e^{-\lambda r} for r>0r>0 are also feasible  [[33](https://arxiv.org/html/2601.22200v1#bib.bib33), [10](https://arxiv.org/html/2601.22200v1#bib.bib10)].
* •

  Wavelet Transform: or multiscale analysis,

  |  |  |  |
  | --- | --- | --- |
  |  | Wψ​[f]​(a,b)=∫−∞∞ψ∗​(x−ba)​f​(x)​𝑑x,W\_{\psi}[f](a,b)=\int\_{-\infty}^{\infty}\psi^{\*}\!\left(\frac{x-b}{a}\right)f(x)\,dx, |  |

  where ψ​(⋅)\psi(\cdot) is the mother wavelet of compact support, and ∗ denotes complex conjugation.
* •

  Wigner Transform: or Wigner quasi-probability distribution,

  |  |  |  |
  | --- | --- | --- |
  |  | Wf​(t,ω)=12​π​∫−∞∞f∗​(t+s)​f​(t−s)​e−i​ω​s​𝑑sW\_{f}(t,\omega)=\frac{1}{\sqrt{2\pi}}\int\_{-\infty}^{\infty}f^{\*}(t+s)\,f(t-s)\,e^{-i\omega s}\,ds |  |

Each of these methods introduces localization in time or frequency, either through compactly supported basis functions or windowing. Among them, STFTs are arguably the most commonly used, and are used in the spectral analysis of sound and music (which clearly has an evolving wave-form), among other applications. We are interested in the exponentially weighted STFT primarily because of its ease of update when new information is added.

### 1.6 STFT and EWRLS with Random Fourier Features

To connect Random Fourier Features (RFFs) with short-term Fourier analysis, consider the exponentially weighted kernel term in our objective function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | e−λ​(t−s)​k​(xt−xs)\displaystyle e^{-\lambda(t-s)}k(x\_{t}-x\_{s}) | =e−λ​τ​∫p​(ω)​ei​ω⊤​(xt−xs)​𝑑ω\displaystyle=e^{-\lambda\tau}\int p(\omega)e^{i\omega^{\top}(x\_{t}-x\_{s})}d\omega |  |

where τ=t−s\tau=t-s is the lag. The forgetting factor e−λ​τe^{-\lambda\tau} acts as a one-sided *exponential window* on the lag, modulating each Fourier component of the kernel in the same way as an exponentially weighted Short-Time Fourier Transform (STFT). Substituting this into the exponentially weighted objective yields the formulation:

|  |  |  |
| --- | --- | --- |
|  | β^t=arg​minβ​∑s≤te−λ​(t−s)​‖ys−φ​(xs)⊤​β‖2\hat{\beta}\_{t}=\operatorname\*{\mathrm{arg\,min}}\_{\beta}\sum\_{s\leq t}e^{-\lambda(t-s)}\bigl\|y\_{s}-\varphi(x\_{s})^{\top}\beta\bigr\|^{2} |  |

This problem admits the usual online solution via exponentially weighted recursive least-squares (EWRLS) updates. In this framework, the RLS algorithm behaves as a dynamic spectral estimator where the RFF weights β^t\hat{\beta}\_{t} correspond to the instantaneous amplitudes of the signal’s spectral components as resolved through the randomized basis.

#### 1.6.1 Computational Complexity and Spectral Deconvolution

A critical divergence exists in the computational order of these approaches. Traditional block-based STFT implementations leverage the Fast Fourier Transform (FFT) to achieve a complexity of O​(M​log⁡M)O(M\log M) per frame, while recursive variants can reach O​(M)O(M) [[34](https://arxiv.org/html/2601.22200v1#bib.bib34)]. In contrast, the proposed ABO framework achieves a complexity of O​(N​D)O(ND) per update, where NN is the sliding window length and DD is the number of random features.

Unlike standard covariance-form RLS which scales as O​(D2)O(D^{2}) due to the maintenance and inversion of the D×DD\times D autocorrelation matrix [[28](https://arxiv.org/html/2601.22200v1#bib.bib28), [17](https://arxiv.org/html/2601.22200v1#bib.bib17)], the QR-based formulation in ABO leverages the structural properties of the sliding window to maintain a linear dependence on the feature dimension DD. Specifically, by utilizing efficient updates for the minimum-norm least-squares solution in rank-deficient settings [[30](https://arxiv.org/html/2601.22200v1#bib.bib30)], the update process is restricted to the NN-dimensional subspace of active observations, resulting in O​(N​D)O(ND) operations. This allows the algorithm to scale effectively into the overparameterized regime required for benign overfitting.

#### 1.6.2 Extension Beyond the Time Domain

Unlike the STFT, which is mathematically confined to temporal or spatial dimensions, EWRLS-RFF generalizes spectral analysis to arbitrary high-dimensional feature spaces. Because RFFs provide an explicit mapping for any shift-invariant kernel, this adaptive framework can be applied to abstract inputs such as graph signals or multidimensional sensor arrays. In these regimes, the algorithm tracks localized structures in feature spaces where traditional grid-based FFT methods are fundamentally inapplicable.

### 1.7 Stability through QR Updates

Standard RLS methods using rank-one updates and downdates are known to be numerically unstable [[28](https://arxiv.org/html/2601.22200v1#bib.bib28), [17](https://arxiv.org/html/2601.22200v1#bib.bib17)], depending on forgetting factors. In the case of overparameterized models, the updates and downdates have to be
altered to consider the singular case (i.e., rank-increasing updates and rank-decreasing downdates). We include the details of update and downdate formulas in Appendix [A](https://arxiv.org/html/2601.22200v1#A1 "Appendix A Rank-One Updates and Downdates ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"), just for completeness. Nonetheless,
in the overparameterized regime, this rank-one formulation of RLS also suffers from numerical instability. This fragility of covariance-form RLS motivates reformulating the recursion in terms of orthogonal-triangular (QR) updates, which maintain numerical stability under sequential adaptation [[3](https://arxiv.org/html/2601.22200v1#bib.bib3), [18](https://arxiv.org/html/2601.22200v1#bib.bib18)].

The inverse covariance, or the Moore–Penrose pseudoinverse in the underdetermined regime where D<ND<N, of the Gram matrix (X⊤​X)†(X^{\top}X)^{\dagger} is updated recursively using the Sherman–Morrison formula. Although efficient, this formulation is numerically fragile: each rank-one correction involves a subtraction between nearly collinear outer products, which can destroy positive semi-definiteness and effectively double the condition number of the covariance estimate at each iteration [[18](https://arxiv.org/html/2601.22200v1#bib.bib18), [13](https://arxiv.org/html/2601.22200v1#bib.bib13)].

As a result, the covariance matrix may drift away from symmetry or become indefinite under finite-precision arithmetic, particularly in ill-conditioned or overparameterized settings.
Square-root or QR-based variants address these issues by maintaining an orthogonal and triangular factorization updated through Givens or Householder rotations [[2](https://arxiv.org/html/2601.22200v1#bib.bib2), [13](https://arxiv.org/html/2601.22200v1#bib.bib13)], ensuring that round-off errors remain bounded.

### 1.8 Contributions

Building on these insights, we propose *Adaptive Benign Overfitting (ABO)*, an adaptive, overparameterized EWRLS framework that integrates Random Fourier Features with exponentially weighted QR updates. Our contributions are twofold:

* •

  We propose a numerically stable recursive scheme using Givens rotations for rank-one updates and downdates. By explicitly maintaining the Moore-Penrose pseudoinverse, the algorithm remains well-defined in rank-deficient regimes, ensuring the minimum-norm interpolant in overparameterized settings.
* •

  Empirical evaluations on nonlinear synthetic, financial, and energy time-series demonstrate that the method achieves bounded residuals and numerical stability while successfully recovering the double-descent behavior characteristic of benign overfitting.
* •

  We show that ABO achieves O​(N​D)O(ND) complexity per update by leveraging the sliding-window structure and pseudoinverse properties. This linear scaling in feature dimension DD (where D≫ND\gg N) provides a significant improvement over the O​(D2)O(D^{2}) cost of standard RLS [[17](https://arxiv.org/html/2601.22200v1#bib.bib17)], enabling high-dimensional online learning.

This formulation bridges the gap between theoretical analyses of benign overfitting and practical recursive algorithms for online learning, offering a unified framework for adaptive modeling in non-stationary environments. We now turn to the formal model and algorithmic formulation, extending Recursive Least Squares (RLS) to the overparameterized and rank-deficient regime while preserving numerical stability under sequential updates.

### 1.9 Related Work

Classical Recursive Least Squares (RLS) algorithms have been extensively studied in adaptive filtering and signal processing [[17](https://arxiv.org/html/2601.22200v1#bib.bib17), [28](https://arxiv.org/html/2601.22200v1#bib.bib28)].
The introduction of exponential weighting improved their ability to track non-stationary signals [[3](https://arxiv.org/html/2601.22200v1#bib.bib3)], although the standard covariance formulation remains prone to numerical instability due to repeated matrix updates, even when using standard ridge penalties222Standard ridge penalties in EWRLS are typically vanishingly small when the sample size grows, due to ease of update. Consequently their stabilization properties are somewhat limited..
Square-root and QR-based variants were later developed to enhance numerical robustness [[2](https://arxiv.org/html/2601.22200v1#bib.bib2), [13](https://arxiv.org/html/2601.22200v1#bib.bib13), [18](https://arxiv.org/html/2601.22200v1#bib.bib18)], yet these analyses typically assume full-rank and well-conditioned data.

Addressing the ill-conditioning inherent in high-dimensional adaptive filtering has traditionally relied on explicit regularization, most notably through sparsity constraints. Inspired by the LASSO, Zero-Attracting RLS (ZA-RLS) algorithms and their reweighted variants impose an ℓ1\ell\_{1}-norm penalty (or approximate ℓ0\ell\_{0} or counting “norm” penalty) on the weight vector wnw\_{n}, effectively forcing ’insignificant’ coefficients to zero to reduce variance [[9](https://arxiv.org/html/2601.22200v1#bib.bib9), [20](https://arxiv.org/html/2601.22200v1#bib.bib20)]. Similar stability guarantees have been achieved using projection-based methods, such as the Adaptive Projected Subgradient Method (APSM), which constrains weights to a convex set [[38](https://arxiv.org/html/2601.22200v1#bib.bib38)].

In contrast to other regularization methods for adaptive filters, our work investigates implicit regularization arising from overparameterization, or benign overfitting, [[5](https://arxiv.org/html/2601.22200v1#bib.bib5), [4](https://arxiv.org/html/2601.22200v1#bib.bib4), [15](https://arxiv.org/html/2601.22200v1#bib.bib15)].
Rather than artificially constraining the model capacity via sparsity or projections, we expand the feature space (via RFFs, see [[27](https://arxiv.org/html/2601.22200v1#bib.bib27), [24](https://arxiv.org/html/2601.22200v1#bib.bib24), [36](https://arxiv.org/html/2601.22200v1#bib.bib36), [31](https://arxiv.org/html/2601.22200v1#bib.bib31)] ) beyond the interpolation threshold. We note that while little work has been done in the rank-deficient regime, there has been some examination of both Cholesky and rank-factorization methods in this area [[29](https://arxiv.org/html/2601.22200v1#bib.bib29), [30](https://arxiv.org/html/2601.22200v1#bib.bib30)].

As suggested by recent findings in the ’benign overfitting’ literature, our approach allows the ’noise’ energy to be distributed harmlessly across orthogonal directions in the high-dimensional space, stabilizing the RLS update without requiring the sparse structural assumptions of ZA-RLS.

The present work bridges these domains by formulating a QR-based exponentially weighted RLS algorithm that remains numerically stable in the overparameterized regime while preserving the recursive structure required for real-time applications.

## 2 System Model

The limitations of the covariance-updating approach discussed in
Appendix [A](https://arxiv.org/html/2601.22200v1#A1 "Appendix A Rank-One Updates and Downdates ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series") highlight the need for a numerically
stable recursive formulation that operates reliably in both full-rank and
rank-deficient regimes. To this end, we reformulate the RLS problem using
an orthogonal–triangular (QR) factorization, which avoids explicit
inversion of Gram matrices and preserves numerical stability under sliding
window updates.

At each time step tt we observe a raw covariate xt∈ℝdx\_{t}\in\mathbb{R}^{d}
and a scalar response yt∈ℝy\_{t}\in\mathbb{R}. Random Fourier Features
provide a nonlinear mapping

|  |  |  |
| --- | --- | --- |
|  | zt=φ​(xt)∈ℝD,z\_{t}=\varphi(x\_{t})\in\mathbb{R}^{D}, |  |

and the regression is performed on the RFF design matrix. Over a rolling
window of length NN, the design matrix and response vector are

|  |  |  |
| --- | --- | --- |
|  | Zt=[zt−N+1⊤⋮zt⊤]∈ℝN×D,Yt=[yt−N+1⋮yt]∈ℝN.Z\_{t}=\begin{bmatrix}z\_{t-N+1}^{\top}\\ \vdots\\ z\_{t}^{\top}\end{bmatrix}\in\mathbb{R}^{N\times D},\qquad Y\_{t}=\begin{bmatrix}y\_{t-N+1}\\ \vdots\\ y\_{t}\end{bmatrix}\in\mathbb{R}^{N}. |  |

Classical least squares requires forming the Gram matrix
At=Zt⊤​ZtA\_{t}=Z\_{t}^{\top}Z\_{t}, which may be singular when D>ND>N and is
numerically unstable to update rank-one. Instead, QR–RLS maintains an
orthogonal–triangular factorization

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt=Qt​Rt,Z\_{t}=Q\_{t}R\_{t}, |  | (5) |

where Qt∈ℝN×NQ\_{t}\in\mathbb{R}^{N\times N} is orthogonal and
Rt∈ℝN×DR\_{t}\in\mathbb{R}^{N\times D} is upper–trapezoidal.
As new data (zt+1,yt+1)(z\_{t+1},y\_{t+1}) arrive, and the oldest row is removed,
the factors (Qt,Rt)(Q\_{t},R\_{t}) are updated using Givens rotations, avoiding
explicit matrix inversion and ensuring numerical stability in both
full-rank and rank-deficient regimes.

### 2.1 Least squares via QR

The least-squares estimate solves

|  |  |  |
| --- | --- | --- |
|  | minβ⁡‖Zt​β−Yt‖22\min\_{\beta}\;\|Z\_{t}\beta-Y\_{t}\|\_{2}^{2} |  |

Using the QR factorization ([5](https://arxiv.org/html/2601.22200v1#S2.E5 "In 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series")) and the
orthogonality of QtQ\_{t}, the objective becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖Zt​β−Yt‖22\displaystyle\|Z\_{t}\beta-Y\_{t}\|\_{2}^{2} | =‖Qt⊤​(Zt​β−Yt)‖22\displaystyle=\|Q\_{t}^{\top}(Z\_{t}\beta-Y\_{t})\|\_{2}^{2} |  | (6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =‖Rt​β−Qt⊤​Yt‖22\displaystyle=\|R\_{t}\beta-Q\_{t}^{\top}Y\_{t}\|\_{2}^{2} |  | (7) |

Thus the LS problem reduces to solving the triangular system

|  |  |  |
| --- | --- | --- |
|  | Rt​β=Qt⊤​YtR\_{t}\beta=Q\_{t}^{\top}Y\_{t} |  |

When RtR\_{t} has full column rank (D≤ND\leq N), the solution is obtained
by back-substitution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt=Rt−1​Qt⊤​Yt\beta\_{t}=R\_{t}^{-1}Q\_{t}^{\top}Y\_{t} |  | (8) |

In the overparameterized regime (D>ND>N), RtR\_{t} is rank-deficient and
the minimum-norm solution is obtained by replacing Rt−1R\_{t}^{-1} with its
Moore–Penrose pseudoinverse:

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt=Rt†​Qt⊤​Yt\beta\_{t}=R\_{t}^{\dagger}Q\_{t}^{\top}Y\_{t} |  | (9) |

This expression holds in both regimes and avoids forming the Gram matrix
Zt⊤​ZtZ\_{t}^{\top}Z\_{t}, ensuring numerical stability.

Remark 1 (Minimum-Norm and Benign Overfitting). In the overparameterized regime (D>ND>N), Equation ([9](https://arxiv.org/html/2601.22200v1#S2.E9 "In 2.1 Least squares via QR ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series")) yields the unique minimum-ℓ2\ell\_{2}-norm interpolant:

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt=arg⁡minβ⁡‖β‖2s.t.Zt​β=Yt,\beta\_{t}=\arg\min\_{\beta}\|\beta\|\_{2}\quad\text{s.t.}\quad Z\_{t}\beta=Y\_{t}, |  | (10) |

equivalent to the Moore-Penrose solution βt=Zt†​Yt\beta\_{t}=Z\_{t}^{\dagger}Y\_{t}. In this setting, generalization is governed by the implicit regularization of the minimum-norm constraint rather than explicit shrinkage. As the null space of ZtZ\_{t} expands, the estimator distributes variance across many tail eigenvalues—a spectral property essential for *benign overfitting*. This mechanism is consistent with the double-descent behavior observed in online learning and justifies the use of stable recursive updates for the pseudoinverse solution.

### 2.2 Random Fourier Features

To introduce nonlinearity while retaining a tractable linear model, we map
each raw observation xt∈ℝdx\_{t}\in\mathbb{R}^{d} into a higher-dimensional
random feature space using *Random Fourier Features* (RFFs)
[[27](https://arxiv.org/html/2601.22200v1#bib.bib27)].

Let A∈ℝd×DA\in\mathbb{R}^{d\times D} have columns
ω1,…,ωD\omega\_{1},\dots,\omega\_{D} drawn independently from p​(ω)p(\omega),
and let b∈ℝDb\in\mathbb{R}^{D} contain i.i.d. phases sampled from
Unif​[0,2​π]\mathrm{Unif}[0,2\pi]. The random feature mapping is

|  |  |  |  |
| --- | --- | --- | --- |
|  | zt=z​(xt)=2D​cos⁡(A⊤​xt+b)∈ℝDz\_{t}=z(x\_{t})=\sqrt{\frac{2}{D}}\cos(A^{\top}x\_{t}+b)\in\mathbb{R}^{D} |  | (11) |

where the cosine is applied elementwise. We adopt this formulation for notational compactness, although many would include cos\cos and sin\sin, or adopt novel sampling schemes to ensure more efficient representations.333Improved efficiency is known to be found via Orthogonal Random Features, Quasi-Monte Carlo Random Features, Structured Orthogonal Random Features and Fast Food based sampling methods, among others.

Over a rolling window of length NN, the RFF design matrix is

|  |  |  |
| --- | --- | --- |
|  | Zt=[zt−N+1⊤⋮zt⊤]∈ℝN×DZ\_{t}=\begin{bmatrix}z\_{t-N+1}^{\top}\\ \vdots\\ z\_{t}^{\top}\end{bmatrix}\in\mathbb{R}^{N\times D} |  |

which forms the input to the QR–based recursive least-squares algorithm
described in the following sections. The dimensionality DD is fixed
and chosen independently of the sample size, enabling efficient updates in
both full-rank and overparameterized regimes.

### 2.3 QR-RLS Update via Givens Rotations

#### 2.3.1 Givens Rotations

A Givens (plane) rotation G​(i,j;c,s)∈ℝN×NG(i,j;c,s)\in\mathbb{R}^{N\times N} is the
identity matrix except on rows and columns ii and jj, where

|  |  |  |
| --- | --- | --- |
|  | G​(i,j;c,s)[i,j],[i,j]=[cs−sc],c2+s2=1G(i,j;c,s)\_{[i,j],[i,j]}=\begin{bmatrix}c&s\\ -s&c\end{bmatrix},\qquad c^{2}+s^{2}=1 |  |

Given a pivot xx and a subdiagonal entry yy in the same column, we
choose

|  |  |  |
| --- | --- | --- |
|  | r=x2+y2,c=xr,s=yrr=\sqrt{x^{2}+y^{2}},\qquad c=\frac{x}{r},\qquad s=\frac{y}{r} |  |

so that

|  |  |  |
| --- | --- | --- |
|  | [cs−sc]​[xy]=[r0]\begin{bmatrix}c&s\\ -s&c\end{bmatrix}\begin{bmatrix}x\\ y\end{bmatrix}=\begin{bmatrix}r\\ 0\end{bmatrix} |  |

A sequence of such rotations {Gℓ}\{G\_{\ell}\} is applied to eliminate the
subdiagonal entries of the augmented matrix, and their product forms the
orthogonal factor:

|  |  |  |
| --- | --- | --- |
|  | Qt⊤=G1⊤​G2⊤​⋯​Gk⊤Q\_{t}^{\top}=G\_{1}^{\top}G\_{2}^{\top}\cdots G\_{k}^{\top} |  |

This yields the QR relation

|  |  |  |
| --- | --- | --- |
|  | Qt⊤​Zt=RtQ\_{t}^{\top}Z\_{t}=R\_{t} |  |

where RtR\_{t} is the updated upper–trapezoidal factor.

#### 2.3.2 Observation Update

When a new feature vector zt⊤z\_{t}^{\top} arrives, we first form the
augmented matrix

|  |  |  |
| --- | --- | --- |
|  | R¯t=[Rt−1zt⊤]∈ℝ(N+1)×D\bar{R}\_{t}=\begin{bmatrix}R\_{t-1}\\ z\_{t}^{\top}\end{bmatrix}\in\mathbb{R}^{(N+1)\times D} |  |

which corresponds to appending the new row to the windowed design matrix
Zt−1Z\_{t-1}. This matrix is no longer upper–trapezoidal: its last row
contains subdiagonal entries that must be eliminated.

A sequence of Givens rotations GtG\_{t} is applied to zero these
subdiagonal elements:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gt⊤​[Rt−1zt⊤]=[Rt0⊤]G\_{t}^{\top}\begin{bmatrix}R\_{t-1}\\ z\_{t}^{\top}\end{bmatrix}=\begin{bmatrix}R\_{t}\\ 0^{\top}\end{bmatrix} |  | (12) |

yielding the updated triangular factor Rt∈ℝN×DR\_{t}\in\mathbb{R}^{N\times D}.
The corresponding orthogonal factor updates as

|  |  |  |
| --- | --- | --- |
|  | Qt=[Qt−1001]​GtQ\_{t}=\begin{bmatrix}Q\_{t-1}&0\\ 0&1\end{bmatrix}G\_{t} |  |

so that the augmented design matrix satisfies

|  |  |  |
| --- | --- | --- |
|  | [Zt−1zt⊤]=Qt​[Rt0⊤]\begin{bmatrix}Z\_{t-1}\\ z\_{t}^{\top}\end{bmatrix}=Q\_{t}\begin{bmatrix}R\_{t}\\ 0^{\top}\end{bmatrix} |  |

The least–squares estimate is then

|  |  |  |
| --- | --- | --- |
|  | βt=Rt†​Qt⊤​Yt\beta\_{t}=R\_{t}^{\dagger}Q\_{t}^{\top}Y\_{t} |  |

Instead of recomputing Rt†R\_{t}^{\dagger} from scratch, the pseudoinverse is
updated through the Givens transformations:

|  |  |  |
| --- | --- | --- |
|  | Rt†=(Gt⊤​[Rt−1zt⊤])†=[Rt−1zt⊤]†​GtR\_{t}^{\dagger}=\left(G\_{t}^{\top}\begin{bmatrix}R\_{t-1}\\ z\_{t}^{\top}\end{bmatrix}\right)^{\dagger}=\begin{bmatrix}R\_{t-1}\\ z\_{t}^{\top}\end{bmatrix}^{\dagger}G\_{t} |  |

which follows from (G​A)†=A†​G⊤(GA)^{\dagger}=A^{\dagger}G^{\top} for any orthogonal
matrix GG. This recursion avoids explicit inversion and preserves
numerical stability during online updates.

#### 2.3.3 Pseudoinverse Update (Greville/Cline) and Link to QR-RLS

From the previous section we have the row-augmented matrix R¯t\bar{R}\_{t},
together with its Moore–Penrose pseudoinverse R¯t†\bar{R}\_{t}^{\dagger}.

Define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | c\displaystyle c | =(I−Rt−1†​Rt−1)​zt\displaystyle=(I-R\_{t-1}^{\dagger}R\_{t-1})\,z\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | h\displaystyle h | =zt⊤​Rt−1†\displaystyle=z\_{t}^{\top}R\_{t-1}^{\dagger} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | c†\displaystyle c^{\dagger} | =c‖c‖22\displaystyle=\dfrac{c}{\|c\|\_{2}^{2}} |  |

Then the Greville/Cline update for the pseudoinverse is

|  |  |  |  |
| --- | --- | --- | --- |
|  | R¯t†=[Rt−1†−b​hb],b={c†if ​c≠0,Rt−1†​h⊤1+h​h⊤if ​c=0\bar{R}\_{t}^{\dagger}=\begin{bmatrix}R\_{t-1}^{\dagger}-bh&b\end{bmatrix},\qquad b=\begin{cases}\hskip 14.22636ptc^{\dagger}&\text{if }c\neq 0,\\[5.38193pt] \dfrac{R\_{t-1}^{\dagger}h^{\top}}{1+hh^{\top}}&\text{if }c=0\end{cases} |  | (13) |

which covers the full-column-space and dependent-column cases [[7](https://arxiv.org/html/2601.22200v1#bib.bib7)].
Unlike standard QRD-RLS, which is typically restricted to overdetermined systems (D≤ND\leq N),
ABO utilizes Greville/Cline updates to maintain a stable minimum-norm solution in the D>ND>N regime.

Define the transformed right-hand side as

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt=Qt⊤​Ytw\_{t}=Q\_{t}^{\top}Y\_{t} |  | (14) |

which can be updated recursively via

|  |  |  |
| --- | --- | --- |
|  | wt=Gt⊤​[wt−1yt]w\_{t}=G\_{t}^{\top}\begin{bmatrix}w\_{t-1}\\ y\_{t}\end{bmatrix} |  |

By orthogonality of QtQ\_{t}, we have

|  |  |  |
| --- | --- | --- |
|  | (Gt⊤​[Rt−1zt⊤])†=Rt†⟺[Rt−1zt⊤]†​Gt=Rt†\big(G\_{t}^{\top}\begin{bmatrix}R\_{t-1}\\ z^{\top}\_{t}\end{bmatrix}\big)^{\dagger}=R\_{t}^{\dagger}\;\;\Longleftrightarrow\;\;\begin{bmatrix}R\_{t-1}\\ z^{\top}\_{t}\end{bmatrix}^{\dagger}G\_{t}=R\_{t}^{\dagger} |  |

Hence, we apply GtG\_{t} to both the triangular factor and the transformed
right-hand side. By orthogonality, Gt⊤​Gt=IG\_{t}^{\top}G\_{t}=I, so

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt\displaystyle\beta\_{t} | =[Rt−1zt⊤]†​Gt​Gt⊤​[wt−1yt]\displaystyle=\begin{bmatrix}R\_{t-1}\\ z^{\top}\_{t}\end{bmatrix}^{\dagger}G\_{t}G\_{t}^{\top}\begin{bmatrix}w\_{t-1}\\ y\_{t}\end{bmatrix} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[Rt−1zt⊤]†​[wt−1yt]\displaystyle=\begin{bmatrix}R\_{t-1}\\ z^{\top}\_{t}\end{bmatrix}^{\dagger}\begin{bmatrix}w\_{t-1}\\ y\_{t}\end{bmatrix} |  |

#### 2.3.4 Weight Update

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | βt\displaystyle\beta\_{t} | =Rt†​Qt⊤​yt\displaystyle=R\_{t}^{\dagger}Q\_{t}^{\top}y\_{t} |  | (15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =[Rt−1†−b​zt⊤​Rt−1†b]​Gt​Gt⊤​[wt−1yt]\displaystyle=\begin{bmatrix}R\_{t-1}^{\dagger}-bz^{\top}\_{t}R\_{t-1}^{\dagger}&b\end{bmatrix}G\_{t}G\_{t}^{\top}\begin{bmatrix}w\_{t-1}\\ y\_{t}\end{bmatrix} |  | (16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Rt−1†​wt−1−b​zt⊤​Rt−1†​wt−1+b​yt\displaystyle=R\_{t-1}^{\dagger}w\_{t-1}-bz^{\top}\_{t}R\_{t-1}^{\dagger}w\_{t-1}+by\_{t} |  | (17) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =βt−1+b​(yt−zt⊤​βt−1)\displaystyle=\beta\_{t-1}+b(y\_{t}-z^{\top}\_{t}\beta\_{t-1}) |  | (18) |

The vector bb plays the role
of the Kalman gain; its expression depends on whether the new row ztz\_{t}
increases the rank of Rt−1R\_{t-1} (c≠0c\neq 0) or lies in its column
space (c=0c=0).

#### 2.3.5 Observation Downdate

To enforce a rolling window, the contribution of the oldest observation
must be removed from the QR factors. Let Gt−NG\_{t-N} denote the Givens
rotation that reverses the orthogonal transformation previously applied to
the first row of Qt−1Q\_{t-1} [[11](https://arxiv.org/html/2601.22200v1#bib.bib11)]. Partition
Qt−1Q\_{t-1} as

|  |  |  |
| --- | --- | --- |
|  | Qt−1=[qt−N⊤Qt−1(2:N)]Q\_{t-1}=\begin{bmatrix}q\_{t-N}^{\top}\\ Q\_{t-1}^{(2:N)}\end{bmatrix} |  |

where qt−N⊤q\_{t-N}^{\top} is the row corresponding to the discarded
observation. The downdate rotation Gt−NG\_{t-N} is chosen so that

|  |  |  |
| --- | --- | --- |
|  | Gt−N⊤​qt−N=α​e1,α∈{±1}G\_{t-N}^{\top}q\_{t-N}=\alpha e\_{1},\qquad\alpha\in\{\pm 1\} |  |

which yields

|  |  |  |
| --- | --- | --- |
|  | Qt−1​Gt−N=[α00Qt]Q\_{t-1}G\_{t-N}=\begin{bmatrix}\alpha&0\\ 0&Q\_{t}\end{bmatrix} |  |

If α=−1\alpha=-1, we flip the sign of Gt−NG\_{t-N} to preserve orientation.

Applying Gt−N⊤G\_{t-N}^{\top} to the triangular factor restores the first row of
Rt−1R\_{t-1} to its pre-rotation value zt−N⊤z\_{t-N}^{\top}. Hence

|  |  |  |
| --- | --- | --- |
|  | Gt−N⊤​Rt−1=[zt−N⊤Rt]G\_{t-N}^{\top}R\_{t-1}=\begin{bmatrix}z\_{t-N}^{\top}\\ R\_{t}\end{bmatrix} |  |

Subtracting the rank-one term e1​zt−N⊤e\_{1}z\_{t-N}^{\top} removes this restored row:

|  |  |  |
| --- | --- | --- |
|  | Gt−N⊤​Rt−1−e1​zt−N⊤=[0Rt]G\_{t-N}^{\top}R\_{t-1}-e\_{1}z\_{t-N}^{\top}=\begin{bmatrix}0\\ R\_{t}\end{bmatrix} |  |

After discarding the zero row, the remaining block is the downdated
triangular factor RtR\_{t}.

For later use, define the intermediate matrix

|  |  |  |
| --- | --- | --- |
|  | R^t:=Rt−1−Gt−N​e1​zt−N⊤\hat{R}\_{t}:=R\_{t-1}-G\_{t-N}e\_{1}z\_{t-N}^{\top} |  |

so that

|  |  |  |
| --- | --- | --- |
|  | Gt−N⊤​R^t=[0Rt]G\_{t-N}^{\top}\hat{R}\_{t}=\begin{bmatrix}0\\ R\_{t}\end{bmatrix} |  |

Since Gt−NG\_{t-N} is orthogonal, the generalized inverse identity
(G​A)†=A†​G⊤(GA)^{\dagger}=A^{\dagger}G^{\top} applies [[6](https://arxiv.org/html/2601.22200v1#bib.bib6)], giving

|  |  |  |
| --- | --- | --- |
|  | (Gt−N⊤​R^t)†=R^t†​Gt−N(G\_{t-N}^{\top}\hat{R}\_{t})^{\dagger}=\hat{R}\_{t}^{\dagger}G\_{t-N} |  |

This relation will be used to express the downdated pseudoinverse and to
connect the downdate with the subsequent weight update.

#### 2.3.6 Pseudoinverse Downdate via Generalized Sum Formulas

To apply the generalized inverse sum formulas of
[[6](https://arxiv.org/html/2601.22200v1#bib.bib6), [7](https://arxiv.org/html/2601.22200v1#bib.bib7)], introduce

|  |  |  |  |
| --- | --- | --- | --- |
|  | h\displaystyle h | =zt−N⊤​Rt−1†,k=Rt−1†​Gt−N​e1,\displaystyle=z\_{t-N}^{\top}R\_{t-1}^{\dagger},\qquad k=R\_{t-1}^{\dagger}G\_{t-N}e\_{1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | u\displaystyle u | =(I−Rt−1​Rt−1†)​Gt−N​e1,v=zt−N⊤​(I−Rt−1†​Rt−1)\displaystyle=(I-R\_{t-1}R\_{t-1}^{\dagger})G\_{t-N}e\_{1},\qquad v=z\_{t-N}^{\top}(I-R\_{t-1}^{\dagger}R\_{t-1}) |  |

For a downdate, the removed row zt−N⊤z\_{t-N}^{\top} lies in both the row and
column spaces of Rt−1R\_{t-1}, and therefore

|  |  |  |
| --- | --- | --- |
|  | u=0,v=0u=0,\qquad v=0 |  |

Singular case:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R^t†=Rt−1†−k​k†​Rt−1†−Rt−1†​h†​h+(k†​Rt−1†​h†)​k​h\hat{R}\_{t}^{\dagger}=R\_{t-1}^{\dagger}-kk^{\dagger}R\_{t-1}^{\dagger}-R\_{t-1}^{\dagger}h^{\dagger}h+(k^{\dagger}R\_{t-1}^{\dagger}h^{\dagger})\,kh |  | (19) |

Nonsingular case:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R^t†=Rt−1−1+Rt−1−1​Gt−N​e1​zt−N⊤​Rt−1−11−zt−N⊤​Rt−1−1​Gt−N​e1\hat{R}\_{t}^{\dagger}=R\_{t-1}^{-1}+\frac{R\_{t-1}^{-1}G\_{t-N}e\_{1}z\_{t-N}^{\top}R\_{t-1}^{-1}}{1-z\_{t-N}^{\top}R\_{t-1}^{-1}G\_{t-N}e\_{1}} |  | (20) |

In both cases, the downdated pseudoinverse Rt†R\_{t}^{\dagger} is obtained by
right-multiplying by the orthogonal rotation:

|  |  |  |
| --- | --- | --- |
|  | [0Rt†]=R^t†​Gt−N\begin{bmatrix}0&R\_{t}^{\dagger}\end{bmatrix}=\hat{R}\_{t}^{\dagger}G\_{t-N} |  |

This yields a fully recursive pseudoinverse downdate compatible with both
full-rank and rank-deficient regimes.

#### 2.3.7 Weight Downdate

To compute the iterative weight downdate, we begin by noting that the update of Yt−1Y\_{t-1} requires removing its first element, analogously to the removal of the first observation zt−Nz\_{t-N} in the feature matrix. Since yt−Ny\_{t-N} is a scalar, this operation can be expressed as

|  |  |  |
| --- | --- | --- |
|  | Gt−N⊤​Qt−1⊤​[yt−NYt]−[yt−N0]=[0Qt⊤​Yt]G\_{t-N}^{\top}Q\_{t-1}^{\top}\begin{bmatrix}y\_{t-N}\\[3.00003pt] Y\_{t}\end{bmatrix}-\begin{bmatrix}y\_{t-N}\\[3.00003pt] 0\end{bmatrix}=\begin{bmatrix}0\\[3.00003pt] Q\_{t}^{\top}Y\_{t}\end{bmatrix} |  |

where yt−N=e1⊤​Yt−1y\_{t-N}=e\_{1}^{\top}Y\_{t-1} denotes the first entry of the vector Yt−1Y\_{t-1}.
This relation can be rearranged as

|  |  |  |
| --- | --- | --- |
|  | [0Qt⊤​Yt]=Gt−N⊤​Qt−1⊤​Yt−1−e1​yt−N\begin{bmatrix}0\\ Q\_{t}^{\top}Y\_{t}\end{bmatrix}=G\_{t-N}^{\top}Q\_{t-1}^{\top}Y\_{t-1}-e\_{1}y\_{t-N} |  |

Consequently, the complete downdating expression for the regression weights becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt\displaystyle\beta\_{t} | =Rt†​Qt⊤​Yt\displaystyle=R\_{t}^{\dagger}Q\_{t}^{\top}Y\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(Rt−1−Gt−N​e1​zt−N⊤)†​Gt−N​(Gt−N⊤​Qt−1⊤​Yt−1−e1​yt−N)\displaystyle=\bigl(R\_{t-1}-G\_{t-N}e\_{1}z\_{t-N}^{\top}\bigr)^{\dagger}G\_{t-N}\bigl(G\_{t-N}^{\top}Q\_{t-1}^{\top}Y\_{t-1}-e\_{1}y\_{t-N}\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(Rt−1−Gt−N​e1​zt−N⊤)†​(Qt−1⊤​Yt−1−Gt−N​e1​yt−N)\displaystyle=\bigl(R\_{t-1}-G\_{t-N}e\_{1}z\_{t-N}^{\top}\bigr)^{\dagger}\bigl(Q\_{t-1}^{\top}Y\_{t-1}-G\_{t-N}e\_{1}y\_{t-N}\bigr) |  |

In the final step, the appropriate pseudoinverse or inverse update formula is substituted, depending on the regime in which the system operates—that is, whether the feature matrix is overdetermined or underdetermined.

Singular case:

To apply the generalized pseudoinverse downdate identity, we require the
standard range conditions [[6](https://arxiv.org/html/2601.22200v1#bib.bib6)]:

|  |  |  |
| --- | --- | --- |
|  | Gt−N​e1∈Range⁡(Rt−1),zt−N∈Range⁡(Rt−1⊤)G\_{t-N}e\_{1}\in\operatorname{Range}(R\_{t-1}),\qquad z\_{t-N}\in\operatorname{Range}(R\_{t-1}^{\top}) |  |

Since both Gt−N​e1G\_{t-N}e\_{1} and zt−Nz\_{t-N} are vectors, these conditions ensure
that the corresponding oblique projections vanish:

|  |  |  |
| --- | --- | --- |
|  | (I−Rt−1​Rt−1†)​Gt−N​e1=0,zt−N⊤​(I−Rt−1†​Rt−1)=0⊤(I-R\_{t-1}R\_{t-1}^{\dagger})\,G\_{t-N}e\_{1}=0,\qquad z\_{t-N}^{\top}(I-R\_{t-1}^{\dagger}R\_{t-1})=0^{\top} |  |

Under these assumptions, the rank of the augmented system is preserved:

|  |  |  |
| --- | --- | --- |
|  | ρ​(Rt−1)=ρ​(R^t)\rho(R\_{t-1})=\rho(\hat{R}\_{t}) |  |

so the downdate does not alter the column space of Rt−1R\_{t-1}.

Consider the block matrix

|  |  |  |
| --- | --- | --- |
|  | R^t−1=[Rt−1Gt−N​e1zt−N⊤D]\hat{R}\_{t-1}=\begin{bmatrix}R\_{t-1}&G\_{t-N}e\_{1}\\[3.00003pt] z\_{t-N}^{\top}&D\end{bmatrix} |  |

with Schur complement D=Gt−N​e1​Rt−1†​zt−N⊤D=G\_{t-N}e\_{1}R\_{t-1}^{\dagger}z\_{t-N}^{\top}.
Following [[14](https://arxiv.org/html/2601.22200v1#bib.bib14)], we set D=1D=1 to avoid
introducing additional scale factors.
This directly yields the normalization

|  |  |  |
| --- | --- | --- |
|  | 1=zt−N⊤​Rt−1†​Gt−N​e11=z\_{t-N}^{\top}R\_{t-1}^{\dagger}G\_{t-N}e\_{1} |  |

Because k​k†​k=kkk^{\dagger}k=k, the matrix k​k†kk^{\dagger} acts as the
orthogonal projector onto the subspace spanned by the vector k=Rt−1†​Gt−N​e1k=R\_{t-1}^{\dagger}G\_{t-N}e\_{1}.

Since the model interpolates the data within the window, the response vector
Yt−1Y\_{t-1} lies in the row space of Zt−1Z\_{t-1}.
Equivalently, the estimator βt−1\beta\_{t-1} satisfies

|  |  |  |
| --- | --- | --- |
|  | zt−N⊤​βt−1=yt−Nz\_{t-N}^{\top}\beta\_{t-1}=y\_{t-N} |  |

We now derive the downdated coefficient vector βt\beta\_{t}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt=Rt†​Qt⊤​Yt=(Rt−1†−k​k†​Rt−1†−Rt−1†​h†​h+(k†​Rt−1†​h†)​k​h)(Qt−1⊤​Yt−1−Gt−N​e1​yt−N)=βt−1−k​k†​βt−1−Rt−1†​h†​zt−N⊤​βt−1+(k†​Rt−1†​h†)​k​zt−N⊤​βt−1−k​yt−N+k​k†​k​yt−N+Rt−1†​h†​zt−N⊤​Rt−1†​Gt−N​e1​yt−N−(k†​Rt−1†​h†)​k​zt−N⊤​Rt−1†​Gt−N​e1​yt−N=βt−1−k​k†​βt−1+(Rt−1†​h†−(k†​Rt−1†​h†)​k)​(yt−N−zt−N⊤​βt−1)−k​yt−N+k​yt−Nβt=βt−1−k​k†​βt−1\begin{split}\beta\_{t}&=R^{\dagger}\_{t}Q\_{t}^{\top}Y\_{t}\\ &=(R\_{t-1}^{\dagger}-kk^{\dagger}R\_{t-1}^{\dagger}-R\_{t-1}^{\dagger}h^{\dagger}h+(k^{\dagger}R\_{t-1}^{\dagger}h^{\dagger})\,kh)\\ &\hskip 14.22636pt(Q\_{t-1}^{\top}Y\_{t-1}-G\_{t-N}e\_{1}y\_{t-N})\\ &=\beta\_{t-1}-kk^{\dagger}\beta\_{t-1}-R\_{t-1}^{\dagger}h^{\dagger}z\_{t-N}^{\top}\beta\_{t-1}\\ &\hskip 14.22636pt+(k^{\dagger}R\_{t-1}^{\dagger}h^{\dagger})kz\_{t-N}^{\top}\beta\_{t-1}\\ &\hskip 14.22636pt-ky\_{t-N}+kk^{\dagger}ky\_{t-N}\\ &\hskip 14.22636pt+R\_{t-1}^{\dagger}h^{\dagger}z\_{t-N}^{\top}R\_{t-1}^{\dagger}G\_{t-N}e\_{1}y\_{t-N}\\ &\hskip 14.22636pt-(k^{\dagger}R\_{t-1}^{\dagger}h^{\dagger})kz\_{t-N}^{\top}R\_{t-1}^{\dagger}G\_{t-N}e\_{1}y\_{t-N}\\ &=\beta\_{t-1}-kk^{\dagger}\beta\_{t-1}\\ &\hskip 14.22636pt+(R\_{t-1}^{\dagger}h^{\dagger}-(k^{\dagger}R\_{t-1}^{\dagger}h^{\dagger})k)(y\_{t-N}-z\_{t-N}^{\top}\beta\_{t-1})\\ &\hskip 14.22636pt-ky\_{t-N}+ky\_{t-N}\\ \beta\_{t}&=\beta\_{t-1}-kk^{\dagger}\beta\_{t-1}\end{split} |  | (21) |

The update is therefore the orthogonal projection of βt−1\beta\_{t-1} onto the
subspace orthogonal to kk:

|  |  |  |
| --- | --- | --- |
|  | βt=(I−k​k†)​βt−1\beta\_{t}=(I-kk^{\dagger})\,\beta\_{t-1} |  |

Since k​k†kk^{\dagger} is the projector onto Range⁡(k)\operatorname{Range}(k), the
downdated parameter satisfies

|  |  |  |
| --- | --- | --- |
|  | k⊤​βt=0k^{\top}\beta\_{t}=0 |  |

ensuring that information associated with the discarded row is completely
removed from the estimate.

Non Singular case:

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt=Rt†​Qt⊤​Yt=(Rt−1†+Rt−1†​Gt−N​e1​zt−N⊤​Rt−1†(1−zt−N⊤​Rt−1†​Gt−N​e1))(Qt−1⊤​Yt−1−Gt−N​e1​yt−N)=βt−1+Rt−1†​Gt−N​e1​zt−N⊤​βt−1(1−zt−N⊤​Rt−1†​Gt−N​e1)−yt−N​Rt−1†​Gt−N​e1​(1+zt−N⊤​Rt−1†​Gt−N​e1(1−zt−N⊤​Rt−1†​Gt−N​e1))=βt−1+Rt−1†​Gt−N​e1​zt−N⊤​βt−1(1−zt−N⊤​Rt−1†​Gt−N​e1)−yt−N​Rt−1†​Gt−N​e1(1−zt−N⊤​Rt−1†​Gt−N​e1)βt=βt−1−Rt−1†​Gt−N​e1(1−zt−N⊤​Rt−1†​Gt−N​e1)​(yt−N−zt−N⊤​βt−1)\begin{split}\beta\_{t}&=R^{\dagger}\_{t}Q\_{t}^{\top}Y\_{t}\\ &=(R^{\dagger}\_{t-1}+\frac{R^{\dagger}\_{t-1}G\_{t-N}e\_{1}z\_{t-N}^{\top}R^{\dagger}\_{t-1}}{(1-z\_{t-N}^{\top}R^{\dagger}\_{t-1}G\_{t-N}e\_{1})})\\ &\hskip 14.22636pt(Q\_{t-1}^{\top}Y\_{t-1}-G\_{t-N}e\_{1}y\_{t-N})\\ &=\beta\_{t-1}+\frac{R^{\dagger}\_{t-1}G\_{t-N}e\_{1}z\_{t-N}^{\top}\beta\_{t-1}}{(1-z\_{t-N}^{\top}R^{\dagger}\_{t-1}G\_{t-N}e\_{1})}\\ &\hskip 14.22636pt-y\_{t-N}R^{\dagger}\_{t-1}G\_{t-N}e\_{1}(1+\frac{z\_{t-N}^{\top}R^{\dagger}\_{t-1}G\_{t-N}e\_{1}}{(1-z\_{t-N}^{\top}R^{\dagger}\_{t-1}G\_{t-N}e\_{1})})\\ &=\beta\_{t-1}+\frac{R^{\dagger}\_{t-1}G\_{t-N}e\_{1}z\_{t-N}^{\top}\beta\_{t-1}}{(1-z\_{t-N}^{\top}R^{\dagger}\_{t-1}G\_{t-N}e\_{1})}\\ &\hskip 14.22636pt-\frac{y\_{t-N}R^{\dagger}\_{t-1}G\_{t-N}e\_{1}}{(1-z\_{t-N}^{\top}R^{\dagger}\_{t-1}G\_{t-N}e\_{1})}\\ \beta\_{t}&=\beta\_{t-1}-\frac{R^{\dagger}\_{t-1}G\_{t-N}e\_{1}}{(1-z\_{t-N}^{\top}R^{\dagger}\_{t-1}G\_{t-N}e\_{1})}(y\_{t-N}-z\_{t-N}^{\top}\beta\_{t-1})\end{split} |  | (22) |

In this formulation, the Kalman gain occupies its standard position as the multiplicative factor of the innovation term (yt−N−zt−N⊤​βt−1)(y\_{t-N}-z\_{t-N}^{\top}\beta\_{t-1}), thereby updating the estimate in proportion to the prediction error.

The overall recursive procedure is summarized in Algorithm [1](https://arxiv.org/html/2601.22200v1#alg1 "Algorithm 1 ‣ 2.4 QR–EWRLS Algorithm ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"), which integrates
the exponentially weighted updates and QR-based orthogonalization described above.

#### 2.3.8 Forgetting factor and Regularization

The introduction of a forgetting factor λ∈(0,1]\lambda\in(0,1] in the RLS cost function allows the algorithm to adapt to non-stationary signals by exponentially down-weighting past observations. This mechanism also acts as an implicit form of regularization, improving the numerical conditioning of the covariance matrix [[28](https://arxiv.org/html/2601.22200v1#bib.bib28), [3](https://arxiv.org/html/2601.22200v1#bib.bib3)].

The previous derivations correspond to the special case λ=1\lambda=1, where all samples are equally weighted. In practice, however, the forgetting factor is incorporated through a diagonal weighting matrix

|  |  |  |
| --- | --- | --- |
|  | Λt=diag⁡(λN−1,λN−2,…,λ0),\Lambda\_{t}=\operatorname{diag}(\sqrt{\lambda^{N-1}},\sqrt{\lambda^{N-2}},\ldots,\sqrt{\lambda^{0}}), |  |

leading to the exponentially weighted least-squares problem

|  |  |  |
| --- | --- | --- |
|  | minβ⁡‖Λt​(Zt​βt−Yt)‖22.\min\_{\beta}\,\|\Lambda\_{t}(Z\_{t}\beta\_{t}-Y\_{t})\|\_{2}^{2}. |  |

which using the QR factorization it is equal to

|  |  |  |
| --- | --- | --- |
|  | β=Rt−1†​Qt⊤​Λt​Yt\beta=R\_{t-1}^{\dagger}Q\_{t}^{\top}\Lambda\_{t}Y\_{t} |  |

To obtain a recursive QR update with exponential forgetting, assume that at
time t−1t-1

|  |  |  |
| --- | --- | --- |
|  | Λt−1​Zt−1=Qt−1​Rt−1\Lambda\_{t-1}Z\_{t-1}=Q\_{t-1}R\_{t-1} |  |

Incorporating a new observation ztz\_{t} with forgetting factor
λ∈(0,1]\lambda\in(0,1] yields

|  |  |  |
| --- | --- | --- |
|  | Λt​Zt=[λ​Λt−1001]​[Zt−1zt⊤]=[λ​Qt−1​Rt−1zt⊤]\Lambda\_{t}Z\_{t}=\begin{bmatrix}\sqrt{\lambda}\,\Lambda\_{t-1}&0\\ 0&1\end{bmatrix}\begin{bmatrix}Z\_{t-1}\\ z\_{t}^{\top}\end{bmatrix}=\begin{bmatrix}\sqrt{\lambda}\,Q\_{t-1}R\_{t-1}\\ z\_{t}^{\top}\end{bmatrix} |  |

Factoring out the orthogonal block diag⁡(Qt−1,1)\operatorname{diag}(Q\_{t-1},1) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λt​Zt=[Qt−1001]​[λ​Rt−1zt⊤]\Lambda\_{t}Z\_{t}=\begin{bmatrix}Q\_{t-1}&0\\ 0&1\end{bmatrix}\begin{bmatrix}\sqrt{\lambda}\,R\_{t-1}\\ z\_{t}^{\top}\end{bmatrix} |  | (23) |

so the update reduces to computing the QR factorization of the stacked
matrix in ([23](https://arxiv.org/html/2601.22200v1#S2.E23 "In 2.3.8 Forgetting factor and Regularization ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series")).

The weighted response vector updates analogously as

|  |  |  |
| --- | --- | --- |
|  | Λt​Yt=[λ​Λt−1​Yt−1yt]\Lambda\_{t}Y\_{t}=\begin{bmatrix}\sqrt{\lambda}\,\Lambda\_{t-1}Y\_{t-1}\\ y\_{t}\end{bmatrix} |  |

Accordingly, the recursive factorization update becomes

|  |  |  |
| --- | --- | --- |
|  | Rt=[λ​Rt−1zt⊤]R\_{t}=\begin{bmatrix}\sqrt{\lambda}\,R\_{t-1}\\ z\_{t}^{\top}\end{bmatrix} |  |

When updating the pseudoinverse matrix, the forgetting factor is absorbed by scaling

|  |  |  |
| --- | --- | --- |
|  | Rt−1†←1λ​Rt−1†R\_{t-1}^{\dagger}\leftarrow\frac{1}{\sqrt{\lambda}}R\_{t-1}^{\dagger} |  |

prior to performing the downdate step in ([13](https://arxiv.org/html/2601.22200v1#S2.E13 "In 2.3.3 Pseudoinverse Update (Greville/Cline) and Link to QR-RLS ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series")).
This adjustment ensures that the inverse recursively reflects the exponential weighting. A detailed proof is provided in Appendix [B](https://arxiv.org/html/2601.22200v1#A2 "Appendix B Proof of the Forgetting Factor Scaling ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series").

Regularization can also be introduced through *diagonal loading*, which modifies the normal equations to

|  |  |  |
| --- | --- | --- |
|  | (Z⊤​Z+δ​I)​β=Z⊤​Y(Z^{\top}Z+\delta I)\beta=Z^{\top}Y |  |

thereby converting a singular or ill-conditioned system into a well-posed one [[26](https://arxiv.org/html/2601.22200v1#bib.bib26), [17](https://arxiv.org/html/2601.22200v1#bib.bib17)].
While diagonal loading (ridge) provides stability by shifting the spectrum, ABO achieves stability through the orthogonal decomposition itself, allowing the model to utilize the full null space for variance absorption without the bias introduced by δ​I\delta I. In our setting, we deliberately avoid such explicit regularization, since our goal is to study over-parameterized regimes where the model is intentionally allowed to interpolate the data, which is entirely disallowed in the case of ridge-regularization.

### 2.4 QR–EWRLS Algorithm

We now summarize the proposed QR-based exponentially weighted recursive least-squares
(QR–EWRLS) procedure. Algorithm [1](https://arxiv.org/html/2601.22200v1#alg1 "Algorithm 1 ‣ 2.4 QR–EWRLS Algorithm ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series") presents the complete update cycle.
The following theorem establishes that, under idealized arithmetic, the algorithm computes
the minimum-norm exponentially weighted sliding-window least-squares solution.

Algorithm 1  Adaptive Benign Overfitting (ABO) via QR-EWRLS

1:Stream {(xt,yt)}\{(x\_{t},y\_{t})\}, window size NN, forgetting factor λ\lambda, RFF dimension DD

2:Online predictions {y^t}\{\hat{y}\_{t}\}, coefficient vectors {βt}\{\beta\_{t}\}

3:Initialization:

4:  Compute initial Z0∈ℝN×DZ\_{0}\in\mathbb{R}^{N\times D} and Y0∈ℝNY\_{0}\in\mathbb{R}^{N}

5:  Perform QR factorization: Z0=Q0​R0Z\_{0}=Q\_{0}R\_{0} ⊳\triangleright [([5](https://arxiv.org/html/2601.22200v1#S2.E5 "In 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

6:  Solve R0​β0=Q0⊤​Y0R\_{0}\beta\_{0}=Q\_{0}^{\top}Y\_{0} for minimum-norm β0\beta\_{0} ⊳\triangleright [([9](https://arxiv.org/html/2601.22200v1#S2.E9 "In 2.1 Least squares via QR ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

7:for t=N+1,N+2,…t=N+1,N+2,\dots do

8:  Step 1: RFF Mapping

9:    zt←2D​cos⁡(A⊤​xt+b)z\_{t}\leftarrow\sqrt{\frac{2}{D}}\cos(A^{\top}x\_{t}+b) ⊳\triangleright [([11](https://arxiv.org/html/2601.22200v1#S2.E11 "In 2.2 Random Fourier Features ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

10:  Step 2: Non-stationary Scaling

11:    Rt−1←λ​Rt−1R\_{t-1}\leftarrow\sqrt{\lambda}R\_{t-1},   Yt−1←λ​Yt−1Y\_{t-1}\leftarrow\sqrt{\lambda}Y\_{t-1} ⊳\triangleright [§[2.3.8](https://arxiv.org/html/2601.22200v1#S2.SS3.SSS8 "2.3.8 Forgetting factor and Regularization ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series")]

12:  Step 3: Observation Update (Givens Rotations) [([12](https://arxiv.org/html/2601.22200v1#S2.E12 "In 2.3.2 Observation Update ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

13:    R¯t←[Rt−1zt⊤]\bar{R}\_{t}\leftarrow\begin{bmatrix}R\_{t-1}\\
z\_{t}^{\top}\end{bmatrix},   Yt←[Yt−1yt]Y\_{t}\leftarrow\begin{bmatrix}Y\_{t-1}\\
y\_{t}\end{bmatrix}

14:    Apply GtG\_{t} such that Gt⊤​R¯t←[Rt𝟎⊤]G\_{t}^{\top}\bar{R}\_{t}\leftarrow\begin{bmatrix}R\_{t}\\
\mathbf{0}^{\top}\end{bmatrix}

15:    Qt←[Qt−1001]​GtQ\_{t}\leftarrow\begin{bmatrix}Q\_{t-1}&0\\
0&1\end{bmatrix}G\_{t}

16:  Step 4: Pseudoinverse Update

17:  h←zt⊤​Rt−1†h\leftarrow z\_{t}^{\top}R\_{t-1}^{\dagger}

18:  if D≤ND\leq N then ⊳\triangleright Classical Regime [([13](https://arxiv.org/html/2601.22200v1#S2.E13 "In 2.3.3 Pseudoinverse Update (Greville/Cline) and Link to QR-RLS ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

19:   R¯t†←[Rt−1†−Rt−1†​h⊤1+h​h⊤​hRt−1†​h⊤1+h​h⊤]\bar{R}\_{t}^{\dagger}\leftarrow\begin{bmatrix}R\_{t-1}^{\dagger}-\dfrac{R\_{t-1}^{\dagger}h^{\top}}{1+hh^{\top}}h&\dfrac{R\_{t-1}^{\dagger}h^{\top}}{1+hh^{\top}}\end{bmatrix}

20:  else⊳\triangleright Overparameterized Regime [([13](https://arxiv.org/html/2601.22200v1#S2.E13 "In 2.3.3 Pseudoinverse Update (Greville/Cline) and Link to QR-RLS ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

21:   R¯t†←[Rt−1†−c†​hc†]\bar{R}\_{t}^{\dagger}\leftarrow\begin{bmatrix}R\_{t-1}^{\dagger}-c^{\dagger}h&c^{\dagger}\end{bmatrix}⊳\triangleright Min-norm solution

22:  R¯t†​Gt←Rt†\bar{R}\_{t}^{\dagger}G\_{t}\leftarrow R\_{t}^{\dagger}

23:  Step 5: Regression Weights

24:  if D≤ND\leq N then ⊳\triangleright Classical Regime [([15](https://arxiv.org/html/2601.22200v1#S2.E15 "In 2.3.4 Weight Update ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

25:   βt←βt−1+Rt−1†​h⊤1+h​h⊤​(yt−zt⊤​βt−1)\beta\_{t}\leftarrow\beta\_{t-1}+\dfrac{R\_{t-1}^{\dagger}h^{\top}}{1+hh^{\top}}(y\_{t}-z^{\top}\_{t}\beta\_{t-1})

26:  else⊳\triangleright Overparameterized Regime [([15](https://arxiv.org/html/2601.22200v1#S2.E15 "In 2.3.4 Weight Update ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

27:   βt←βt−1+c†​(yt−zt⊤​βt−1)\beta\_{t}\leftarrow\beta\_{t-1}+c^{\dagger}(y\_{t}-z^{\top}\_{t}\beta\_{t-1})

28:  Step 6: Windowed Downdate

29:    Identify rotation Gt−NG\_{t-N} to isolate the first row of Qt−1Q\_{t-1}

30:    Update RtR\_{t} and YtY\_{t} to remove (zt−N,yt−N)(z\_{t-N},y\_{t-N}) ⊳\triangleright [§[2.3.5](https://arxiv.org/html/2601.22200v1#S2.SS3.SSS5 "2.3.5 Observation Downdate ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series")]

31:    Maintain RtR\_{t} as N×DN\times D upper-trapezoidal

32:  Step 7: Pseudoinverse Downdate

33:  h←zt−N⊤​Rt−1†,k←Rt−1†​Gt−N​e1h\leftarrow z\_{t-N}^{\top}R\_{t-1}^{\dagger},\qquad k\leftarrow R\_{t-1}^{\dagger}G\_{t-N}e\_{1}

34:  if D≤ND\leq N then ⊳\triangleright Classical Regime [([20](https://arxiv.org/html/2601.22200v1#S2.E20 "In 2.3.6 Pseudoinverse Downdate via Generalized Sum Formulas ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

35:   R^t†←Rt−1−1+k​zt−N⊤​Rt−1−11−zt−N⊤​k\hat{R}\_{t}^{\dagger}\leftarrow R\_{t-1}^{-1}+\dfrac{kz\_{t-N}^{\top}R\_{t-1}^{-1}}{1-z\_{t-N}^{\top}k}

36:  else⊳\triangleright Overparameterized Regime [([19](https://arxiv.org/html/2601.22200v1#S2.E19 "In 2.3.6 Pseudoinverse Downdate via Generalized Sum Formulas ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

37:   R^t†←Rt−1†−k​k†​Rt−1†−Rt−1†​h†​h+(k†​Rt−1†​h†)​k​h\hat{R}\_{t}^{\dagger}\leftarrow R\_{t-1}^{\dagger}-kk^{\dagger}R\_{t-1}^{\dagger}-R\_{t-1}^{\dagger}h^{\dagger}h+(k^{\dagger}R\_{t-1}^{\dagger}h^{\dagger})\,kh

38:  [0Rt†]←R^t†​Gt−N\begin{bmatrix}0&R\_{t}^{\dagger}\end{bmatrix}\leftarrow\hat{R}\_{t}^{\dagger}G\_{t-N}

39:  Step 8: Weight Downdate

40:  if D≤ND\leq N then ⊳\triangleright Classical Regime[([22](https://arxiv.org/html/2601.22200v1#S2.E22 "In 2.3.7 Weight Downdate ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

41:   βt←βt−1−k(1−zt−N⊤​k)​(yt−N−zt−N⊤​βt−1)\beta\_{t}\leftarrow\beta\_{t-1}-\dfrac{k}{(1-z\_{t-N}^{\top}k)}(y\_{t-N}-z\_{t-N}^{\top}\beta\_{t-1})

42:  else⊳\triangleright Overparameterized Regime [([21](https://arxiv.org/html/2601.22200v1#S2.E21 "In 2.3.7 Weight Downdate ‣ 2.3 QR-RLS Update via Givens Rotations ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"))]

43:   βt←βt−1−k​k†​βt−1\beta\_{t}\leftarrow\beta\_{t-1}-kk^{\dagger}\beta\_{t-1}

44:  Step 9: Prediction

45:    y^t←zt⊤​βt\hat{y}\_{t}\leftarrow z\_{t}^{\top}\beta\_{t} ⊳\triangleright Predict next value

###### Theorem 1 (Consistency with minimum-norm exponentially weighted LS).

Let β^t\hat{\beta}\_{t} denote the unique minimum-ℓ2\ell\_{2}-norm solution of the exponentially weighted
sliding-window least-squares problem at time tt,

|  |  |  |  |
| --- | --- | --- | --- |
|  | β^t=arg⁡minβ⁡‖β‖2​s.t.​β∈arg⁡minγ​∑i=0N−1λi​‖yt−i−zt−i⊤​γ‖22\hat{\beta}\_{t}=\arg\min\_{\beta}\ \|\beta\|\_{2}\quad\text{s.t.}\quad\beta\in\arg\min\_{\gamma}\sum\_{i=0}^{N-1}\lambda^{i}\|y\_{t-i}-z\_{t-i}^{\top}\gamma\|\_{2}^{2} |  | (24) |

Let βt\beta\_{t} be the estimate produced by Algorithm 1.
Assume exact arithmetic, admissible rank-preserving updates and downdates, and initialization
β0=β^0\beta\_{0}=\hat{\beta}\_{0}.
Then, for all t≥0t\geq 0, the algorithmic iterate coincides with the minimum-norm solution,

|  |  |  |
| --- | --- | --- |
|  | βt=β^t.\beta\_{t}=\hat{\beta}\_{t}. |  |

###### Proof.

The proof proceeds by induction on tt.

Base case (t=0t=0):
Algorithm 1 initializes β0\beta\_{0} via an explicit batch QR factorization of the initial
windowed design matrix. The resulting pseudoinverse solution therefore coincides with the
minimum-ℓ2\ell\_{2}-norm solution β^0\hat{\beta}\_{0}.

Inductive step:
Assume βt−1=β^t−1\beta\_{t-1}=\hat{\beta}\_{t-1}.
The update from t−1t-1 to tt consists of two operations.

First, scaling by λ\sqrt{\lambda} and row augmentation by (zt,yt)(z\_{t},y\_{t}) corresponds exactly to
adding the weighted observation λ0​zt​zt⊤\lambda^{0}z\_{t}z\_{t}^{\top} to the exponentially weighted normal
equations.
By the properties of the Greville pseudoinverse update, the resulting intermediate estimate
remains the minimum-norm solution of the augmented system.

Second, the downdate step applies an orthogonal transformation to isolate the contribution of the
oldest weighted observation λN​zt−N​zt−N⊤\lambda^{N}z\_{t-N}z\_{t-N}^{\top}, followed by a pseudoinverse downdate.
Under the admissibility assumptions, this operation is algebraically equivalent to removing that
term from the normal equations while preserving the minimum-norm property.

Since these two steps exactly implement the addition and removal of terms in the exponentially
weighted sliding-window objective, the updated estimate satisfies
βt=β^t\beta\_{t}=\hat{\beta}\_{t}.
∎

## 3 Experiments

### 3.1 Synthetic Time Series Generation

Following [[23](https://arxiv.org/html/2601.22200v1#bib.bib23)], we simulate a nonlinear autoregressive process defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt=2​xt−11+0.8​xt−12+εt,εt∼𝒰​(−1,1),x\_{t}=\frac{2x\_{t-1}}{1+0.8x\_{t-1}^{2}}+\varepsilon\_{t},\quad\varepsilon\_{t}\sim\mathcal{U}(-1,1), |  | (25) |

initialized with x0∼𝒰​(−1,1)x\_{0}\sim\mathcal{U}(-1,1).
This process exhibits bounded chaotic dynamics and is widely used to evaluate nonlinear forecasting methods.
From the simulated sequence {xt}t=110500\{x\_{t}\}\_{t=1}^{10500}, we construct lagged feature vectors

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱t=(xt−1,xt−2,…,xt−7),\mathbf{x}\_{t}=(x\_{t-1},x\_{t-2},\dots,x\_{t-7}), |  | (26) |

which serve as predictors for the current value xtx\_{t}.
We then transform these 7 lagged variables into *Random Fourier Features (RFF)* of the desired dimension, providing a nonlinear feature mapping that preserves the inner-product structure induced by a shift-invariant kernel.
The model is therefore trained to forecast xtx\_{t} from its transformed RFF representation of the 7 previous lags.

### 3.2 Data Preprocessing

All features were standardized to ensure comparability across scales and
to approximate homoscedasticity, i.e., a constant variance across time
[[12](https://arxiv.org/html/2601.22200v1#bib.bib12)]. Standardization was performed using

|  |  |  |  |
| --- | --- | --- | --- |
|  | zs​c​o​r​e=x−μσ,z\_{score}=\frac{x-\mu}{\sigma}, |  | (27) |

where μ\mu and σ\sigma denote the mean and standard deviation of each
feature, respectively. After transformation, all features satisfy
μ=0\mu=0 and σ=1\sigma=1.

The standardization was applied recursively as new observations were introduced,
ensuring consistent scaling throughout the data stream [[16](https://arxiv.org/html/2601.22200v1#bib.bib16)].

### 3.3 Stability Analysis

To assess the numerical stability of the proposed update, we conduct two complementary analyses: (i) empirical residual tracking and (ii) conditioning of the system matrix.

#### 3.3.1 Empirical Residual Errors

The empirical residuals quantify the cumulative numerical error introduced by sequential updates.
At each iteration tt, we define the residual as

|  |  |  |
| --- | --- | --- |
|  | rt=‖yt−zt⊤​βt‖2,r\_{t}=\|y\_{t}-z\_{t}^{\top}\beta\_{t}\|\_{2}, |  |

and track the mean and standard deviation of {rt}t=1N\{r\_{t}\}\_{t=1}^{N} over time.
A stable update exhibits bounded residuals that do not diverge as tt increases.

We report the following diagnostics:

* •

  Mean residual: r¯=1T​∑trt\bar{r}=\frac{1}{T}\sum\_{t}r\_{t}
* •

  Residual variance: σr2=1T−1​∑t(rt−r¯)2\sigma\_{r}^{2}=\frac{1}{T-1}\sum\_{t}(r\_{t}-\bar{r})^{2}

Low variance in rtr\_{t} indicates robustness to numerical drift.

#### 3.3.2 Condition Number Evolution

The condition number of the design or correlation matrix provides a proxy for numerical sensitivity.
At each step we compute

|  |  |  |
| --- | --- | --- |
|  | κt=cond⁡(Rt)=σmax​(Rt)σmin​(Rt),\kappa\_{t}=\operatorname{cond}(R\_{t})=\frac{\sigma\_{\max}(R\_{t})}{\sigma\_{\min}(R\_{t})}, |  |

where σmax\sigma\_{\max} and σmin\sigma\_{\min} are the largest and smallest singular values of RtR\_{t}.

A well-conditioned matrix satisfies κt≪1010\kappa\_{t}\ll 10^{10}, while a sharp growth in κt\kappa\_{t} signals loss of orthogonality or ill-conditioning.

### 3.4 Results without Forgetting Factor (λ=1\lambda=1)

For this experiment, we fix the forgetting factor to λ=1\lambda=1, corresponding to the classical RLS formulation with equal weighting of all past samples.
The remaining hyperparameters are:

Table 1: Experiment hyperparameters.

| Parameter | Value |
| --- | --- |
| Number of updates | 10000 |
| Window size | 20 |
| Kernel variance (RFF) | 1 |

This setup serves as a baseline to evaluate the stability and residual dynamics of our proposed update without exponential weighting.

Table [2](https://arxiv.org/html/2601.22200v1#S3.T2 "Table 2 ‣ 3.4 Results without Forgetting Factor (𝜆=1) ‣ 3 Experiments ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series") summarizes the mean and variance of the residuals and condition numbers across varying Random Fourier Feature (RFF) dimensions, which we denote by DD. In this and each of the following tables we print the entries in bold to indicate values that
minimize the test residual variance and MSE across all feature dimensions.
As expected, the model exhibits increasing numerical instability around the interpolation regime, with a sharp rise in both residual variance and condition number for intermediate feature sizes (e.g., D=16D=16), before stabilizing as the model becomes over-parameterized, with the
optimal value being an edge case, with likely continued monotonic decreasing behaviour.

Table 2: Mean and variance of residuals for λ=1\lambda=1

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| log2⁡(D)\log\_{2}(D) | Train Residual | | Test Residual | |
|  | Mean | Variance | Mean | Variance |
| 1 | 0.8121 | 0.9808 | 1.0008 | 1.4941 |
| 2 | 0.7061 | 0.8256 | 1.0966 | 2.0205 |
| 3 | 0.4556 | 0.4147 | 1.3103 | 3.5529 |
| 4 | 0.0813 | 0.0211 | 3.1712 | 69.2871 |
| I\* | 0.0000 | 0.0000 | 819.825 | 1.2×1091.2\times 10^{9} |
| 5 | 0.0000 | 0.0000 | 1.5744 | 8.2697 |
| 6 | 0.0000 | 0.0000 | 0.7797 | 1.2136 |
| 7 | 0.0000 | 0.0000 | 0.6197 | 0.6885 |
| 8 | 0.0000 | 0.0000 | 0.6013 | 0.6142 |
| 9 | 0.0000 | 0.0000 | 0.5749 | 0.5378 |
| 10 | 0.0000 | 0.0000 | 0.5534 | 0.4957 |
| 11 | 0.0000 | 0.0000 | 0.5547 | 0.4982 |
| 12 | 0.0000 | 0.0000 | 0.5452 | 0.4809 |
| 13 | 0.0000 | 0.0000 | 0.5447 | 0.4806 |
| 14 | 0.0000 | 0.0000 | 0.5420 | 0.4738 |

* ∗\ast

  Interpolation limit corresponds to D=N=20D=N=20, i.e. log2⁡(20)≈4.32\log\_{2}(20)\approx 4.32.

### 3.5 Results with Forgetting Factor (λ=0.9\lambda=0.9)

We now introduce a forgetting factor λ=0.9\lambda=0.9, corresponding to an effective memory length

|  |  |  |
| --- | --- | --- |
|  | Neff=11−λ=10N\_{\text{eff}}=\frac{1}{1-\lambda}=10 |  |

This exponentially down-weights older observations to enable adaptation to non-stationary dynamics [[17](https://arxiv.org/html/2601.22200v1#bib.bib17), [28](https://arxiv.org/html/2601.22200v1#bib.bib28)].
All remaining parameters are identical to the previous experiment.

Table [3](https://arxiv.org/html/2601.22200v1#S3.T3 "Table 3 ‣ 3.5 Results with Forgetting Factor (𝜆=0.9) ‣ 3 Experiments ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series") shows that the residual statistics for λ=0.9\lambda=0.9 are nearly identical to those obtained with λ=1\lambda=1.
In the overparameterized regime (D≫ND\gg N), the solution is governed by the implicit minimum-norm bias of the QR-based pseudoinverse, rendering exponential reweighting largely irrelevant for steady-state predictive performance.

Table 3: Mean and variance of residuals for λ=0.9\lambda=0.9

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| log2⁡(D)\log\_{2}(D) | Train Residual | | Test Residual | |
|  | Mean | Variance | Mean | Variance |
| 1 | 0.6267 | 0.6399 | 0.9899 | 1.5632 |
| 2 | 0.4337 | 0.3549 | 1.1232 | 2.2689 |
| 3 | 0.1727 | 0.0756 | 1.3308 | 3.8850 |
| 4 | 0.0135 | 0.0008 | 3.3350 | 73.7217 |
| I\* | 0.0000 | 0.0000 | 78534.6 | 1.02×10131.02\times 10^{13} |
| 5 | 0.0000 | 0.0000 | 1.5744 | 8.2697 |
| 6 | 0.0000 | 0.0000 | 0.7797 | 1.2136 |
| 7 | 0.0000 | 0.0000 | 0.6197 | 0.6885 |
| 8 | 0.0000 | 0.0000 | 0.6013 | 0.6142 |
| 9 | 0.0000 | 0.0000 | 0.5749 | 0.5378 |
| 10 | 0.0000 | 0.0000 | 0.5534 | 0.4957 |
| 11 | 0.0000 | 0.0000 | 0.5547 | 0.4982 |
| 12 | 0.0000 | 0.0000 | 0.5452 | 0.4809 |
| 13 | 0.0000 | 0.0000 | 0.5447 | 0.4806 |
| 14 | 0.0000 | 0.0000 | 0.5420 | 0.4738 |

### 3.6 Condition Number Analysis

Table [4](https://arxiv.org/html/2601.22200v1#S3.T4 "Table 4 ‣ 3.6 Condition Number Analysis ‣ 3 Experiments ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series") reports the condition number statistics for the case without forgetting factor (λ=1\lambda=1).
As the number of features increases and approaches the interpolation limit (D≈ND\approx N), the condition number grows substantially, indicating worsening numerical conditioning of the system matrix.
This behavior aligns with the known sensitivity of least-squares updates near the interpolation threshold, where small perturbations in the data can lead to large variations in the estimated parameters [[18](https://arxiv.org/html/2601.22200v1#bib.bib18), [13](https://arxiv.org/html/2601.22200v1#bib.bib13)].

Table 4: Mean and variance of the condition number for λ=1\lambda=1

|  |  |  |
| --- | --- | --- |
| log2⁡(D)\log\_{2}(D) | Mean | Variance |
| 1 | 1.2801 | 0.0387 |
| 2 | 1.7820 | 0.0966 |
| 3 | 4.0124 | 1.1380 |
| 4 | 21.5274 | 127.6520 |
| I\* | ∞\infty | NA |
| 5 | 15.4765 | 50.3692 |
| 6 | 7.8396 | 12.6857 |
| 7 | 5.9778 | 7.5213 |
| 8 | 5.4786 | 6.5071 |
| 9 | 5.3213 | 6.7122 |
| 10 | 5.1483 | 6.1914 |
| 11 | 5.1902 | 6.3840 |
| 12 | 5.0775 | 6.2375 |
| 13 | 5.0659 | 6.0952 |
| 14 | 5.0563 | 6.1619 |

### 3.7 Double Descent

In this plot, the model exhibits a pronounced increase in test error as the random feature dimension DD approaches the interpolation threshold, followed by a decrease in the overparameterized regime.
This behavior is characteristic of the double-descent phenomenon [[5](https://arxiv.org/html/2601.22200v1#bib.bib5), [15](https://arxiv.org/html/2601.22200v1#bib.bib15)], reflecting the transition from underparameterization to exact interpolation.

The interpolation threshold is explicitly sampled in this experiment.
The dashed vertical line indicates the theoretical interpolation point I∗≈4.32I^{\ast}\approx 4.32, corresponding to the effective equality between the number of random features and the window size.
The observed peak in test error occurs in close proximity to this threshold, confirming that the degradation in generalization performance is associated with the interpolation regime.

![Refer to caption](x1.png)


Figure 2: Double-descent behavior of test error

### 3.8 Computation Speed

Computation time was evaluated using Google Benchmark (v1.9.4) linked against optimized BLAS and LAPACK routines under single-threaded execution. Benchmarking was performed on a 13th Gen Intel® Core™ i7-1370P @ 1.90 GHz with 32 GB RAM (Windows 11, WSL2 Ubuntu 22.04 LTS), with CPU frequency scaling and ASLR disabled to ensure timing reproducibility. Table [5](https://arxiv.org/html/2601.22200v1#S3.T5 "Table 5 ‣ 3.8 Computation Speed ‣ 3 Experiments ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series") reports the mean, standard deviation, and coefficient of variation (CV) for 1,000 sequential predict–update steps across ten repetitions.

The empirical results show that the aggregate runtime increases with the RFF dimension DD, ranging from 6.11 ms6.11\text{\,}\mathrm{ms} at D=21D=2^{1} to approximately 11.97 s11.97\text{\,}\mathrm{s} at D=214D=2^{14}. The scaling remains approximately linear with respect to DD for the majority of the range, which is consistent with the theoretical O​(N​D)O(ND) complexity per update step of the QR-based formulation. While the coefficient of variation remains low at the boundaries of the test range, a transient increase in variance is observed between D=29D=2^{9} and D=213D=2^{13} (peaking at a CV of 36.64 %36.64\text{\,}\mathrm{\char 37\relax}), likely due to memory hierarchy effects or cache misses as the matrix dimensions scale. Nevertheless, the return to a low CV of 4.20 %4.20\text{\,}\mathrm{\char 37\relax} at D=214D=2^{14} confirms the numerical stability and predictable computational performance of the proposed recursive implementation at scale.

Table 5: ABO RLS update+predict runtime vs. RFF dimension DD for 1000 sequential updates (Google Benchmark; 10 repetitions).

| log2⁡(D)\log\_{2}(D) | Mean CPU (ms) | Std (ms) | CV (%) |
| --- | --- | --- | --- |
| 1 | 6.116.11 | 0.190.19 | 3.143.14 |
| 2 | 6.256.25 | 0.050.05 | 0.790.79 |
| 3 | 7.597.59 | 0.300.30 | 3.953.95 |
| 4 | 9.229.22 | 0.180.18 | 1.991.99 |
| 5 | 13.2513.25 | 0.190.19 | 1.461.46 |
| 6 | 19.7919.79 | 0.440.44 | 2.222.22 |
| 7 | 36.0036.00 | 2.112.11 | 5.865.86 |
| 8 | 64.3064.30 | 1.141.14 | 1.771.77 |
| 9 | 438.02438.02 | 160.49160.49 | 36.6436.64 |
| 10 | 887.13887.13 | 292.02292.02 | 32.9232.92 |
| 11 | 1495.531495.53 | 290.62290.62 | 19.4319.43 |
| 12 | 2699.602699.60 | 492.79492.79 | 18.2518.25 |
| 13 | 5508.045508.04 | 832.17832.17 | 15.1115.11 |
| 14 | 11 971.3011\,971.30 | 502.58502.58 | 4.204.20 |

## 4 Results and Baseline Comparisons

We evaluate the proposed Adaptive Benign Overfitting method (ABO/ QR–EWRLS) on real-world non-stationary time-series data.

All experiments follow a strictly online prequential evaluation protocol. We first perform hyperparameter selection using eight validation folds, followed by performance assessment on five disjoint test folds.

For each fold, the model is initialized with a batch whose size equals the chosen window length, after which updates and predictions are carried out sequentially, one observation at a time.

ValidationTestingBatchTime


Figure 3: Walk-forward rolling validation with overlapping windows and strictly disjoint test windows, each preceded by batch initialization

### 4.1 Baseline Performance on Real-World Data

For comparison, we report results for the windowed QR-decomposition-based recursive least-squares (QRD-RLS) algorithm [[25](https://arxiv.org/html/2601.22200v1#bib.bib25)] and the windowed RBF kernel recursive least-squares method [[37](https://arxiv.org/html/2601.22200v1#bib.bib37)]. Both methods are well-established in the adaptive filtering literature and are widely used as numerically stable baselines in windowed and online learning settings.

#### 4.1.1 EUR/USD High-Frequency Forecasting

The EUR/USD dataset consists of high-frequency foreign exchange data spanning from 24/11/2025 to 02/01/2026, sampled at a one-minute resolution, resulting in approximately 16,800 sequential observations. The data are sourced from the Dukas Copy Market Data repository.444<https://www.dukascopy.com/swiss/english/marketwatch/historical/>

Experiments are conducted in a strictly online setting using a rolling-fold evaluation protocol. Each fold consists of 960 observations for validation and 1920 observations for testing, corresponding to approximately 16 hours of market activity per fold. Model inputs are constructed from lagged observations, and learning is performed using an effective windowed update scheme.

Hyperparameters are selected using Optuna over 8 validation folds [[1](https://arxiv.org/html/2601.22200v1#bib.bib1)]. Final performance is reported on 5 disjoint test folds that are not used during tuning. All reported results are averaged across test folds.

#### 4.1.2 Electricity Load Forecasting

We additionally evaluate the proposed method on the Electricity Load Diagrams dataset [[35](https://arxiv.org/html/2601.22200v1#bib.bib35)], which contains electricity consumption measurements from the Portuguese power grid over the period 2011–2014, recorded at a 15-minute sampling frequency.

Experiments are conducted under a strictly online evaluation protocol using rolling folds with 672 observations for validation and 1344 for testing, corresponding to approximately one week of data per fold. The same rolling-fold structure is used for both validation and testing, with disjoint segments within each fold. Lagged inputs and a fixed-size windowed learning scheme are employed, with hyperparameters selected using Optuna on the validation segments and final performance reported on the corresponding test segments.

Compared to the high-frequency financial setting, this dataset exhibits pronounced diurnal and weekly seasonality and substantially lower noise levels, providing a complementary benchmark for assessing both predictive performance and numerical stability.

### 4.2 Hyperparameter Selection

Hyperparameters were selected using Bayesian optimization implemented via Optuna [[1](https://arxiv.org/html/2601.22200v1#bib.bib1)].
For each method, the search space and number of trials were fixed *a priori* and kept identical across all folds.
Optimization was performed on a validation set distinct from the test data, and the final reported results correspond to the best validation configuration evaluated on held-out test folds.

All models are evaluated on the same prediction task, with an identical forecasting start index, ensuring that performance differences arise solely from model structure and learning dynamics.

For both datasets, the lag order is fixed to L=20L=20 for all models.
For ABO and KRLS-RBF, the window size and kernel bandwidth are tuned, while for QRD-RLS only the window size is optimized, reflecting the absence of a kernel parameter in linear RLS.
The corresponding Optuna search spaces are summarized in Table [6](https://arxiv.org/html/2601.22200v1#S4.T6 "Table 6 ‣ 4.2 Hyperparameter Selection ‣ 4 Results and Baseline Comparisons ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series").

Table 6: Optuna hyperparameter search spaces.

| Dataset | Model | Folds | LL | Tuned |
| --- | --- | --- | --- | --- |
| EUR/USD (1-min) | ABO | {0,1,…,8}\{0,1,...,8\} | 20 | W,σW,\sigma |
| KRLS-RBF | {0,1,…,8}\{0,1,...,8\} | 20 | W,σW,\sigma |
| QRD-RLS | {0,1,…,8}\{0,1,...,8\} | 20 | WW |
| Electricity (15-min) | ABO | {0,1,…,8}\{0,1,...,8\} | 20 | W,σW,\sigma |
| KRLS-RBF | {0,1,…,8}\{0,1,...,8\} | 20 | W,σW,\sigma |
| QRD-RLS | {0,1,…,8}\{0,1,...,8\} | 20 | WW |

## 5 Results

### 5.1 Experimental Setup

Experiments are conducted with a fixed lag order L=20L=20 and a forgetting factor λ=1\lambda=1. Kernel hyperparameters (σ\sigma) and window sizes (WW) are optimized via Optuna. For numerical stability, QRD-RLS and KRLS-RBF utilize a diagonal regularization parameter of 10−210^{-2}. Unless otherwise specified, the random Fourier feature (RFF) dimension for ABO is fixed at D=8192D=8192 (log2⁡m=13\log\_{2}m=13).

### 5.2 EUR/USD Forecasting Results

The EUR/USD dataset represents a challenging task due to high noise levels and weak temporal structure. Performance metrics are reported in Table [7](https://arxiv.org/html/2601.22200v1#S5.T7 "Table 7 ‣ 5.2 EUR/USD Forecasting Results ‣ 5 Results ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series").

In this regime, nonlinear representations are critical; both ABO and KRLS-RBF significantly outperform the linear QRD-RLS baseline in terms of residual mean squared error (ResMSE) and residual variance (ResVAR). ABO achieves predictive performance comparable to KRLS-RBF while maintaining stable online updates without an explicit kernel representation.

Table 7: Average EUR/USD forecasting performance and relative update time (L=20,D=8192L=20,D=8192).

| Model | WW | σ\sigma | ResMSE | ResVAR | Time (×\timesABO) |
| --- | --- | --- | --- | --- | --- |
| ABO (ours) | 21 | 8.0 | 1.3587 | 1331.63 | 1.00 |
| KRLS-RBF | 421 | 0.31 | 1.3559 | 1335.34 | 1.70 |
| QRD-RLS | 272 | NA | 2.3294 | 2494.01 | 0.02 |

### 5.3 Electricity Load Forecasting Results

In contrast to the financial data, the electricity load series exhibits stronger temporal structure and lower noise. Results are summarized in Table [8](https://arxiv.org/html/2601.22200v1#S5.T8 "Table 8 ‣ 5.3 Electricity Load Forecasting Results ‣ 5 Results ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series").

In this structured setting, QRD-RLS achieves the lowest ResMSE and ResVAR, highlighting the efficacy of linear adaptive filtering. ABO remains competitive with KRLS-RBF in predictive accuracy but offers a superior computational profile by avoiding explicit kernel evaluations.

Table 8: Average electricity load forecasting performance and relative update time (L=20,D=8192L=20,D=8192).

| Model | WW | σ\sigma | ResMSE | ResVAR | Time (×\timesABO) |
| --- | --- | --- | --- | --- | --- |
| ABO (ours) | 21 | 6.5 | 1.0096 | 10.92 | 1.00 |
| KRLS-RBF | 761 | 0.32 | 1.0110 | 10.87 | 1.28 |
| QRD-RLS | 272 | NA | 0.9521 | 9.06 | 1.9×10−31.9\times 10^{-3} |

### 5.4 Sensitivity to Random Feature Dimension

Tables [9](https://arxiv.org/html/2601.22200v1#S5.T9 "Table 9 ‣ 5.4 Sensitivity to Random Feature Dimension ‣ 5 Results ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series") and [10](https://arxiv.org/html/2601.22200v1#S5.T10 "Table 10 ‣ 5.4 Sensitivity to Random Feature Dimension ‣ 5 Results ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series") isolate the effect of the random feature dimension DD on ABO. Across both datasets, increasing DD from 2048 to 8192 yields modest improvements in predictive accuracy, consistent with RFF kernel approximation theory. However, this gain results in an approximate 6×6\times increase in end-to-end wall-clock time, reflecting the O​(N​D)O(ND) per-update computational complexity of random-feature-based adaptive filtering.

Table 9: Effect of DD on ABO (EUR/USD, L=20,W=21,σ=8.0L=20,W=21,\sigma=8.0).

| DD | ResMSE | ResVAR | Te2eT\_{\text{e2e}} (ms) | Time (×\times2048) |
| --- | --- | --- | --- | --- |
| 2048 | 1.3711 | 1339.80 | 9.11 | 1.00 |
| 8192 | 1.3587 | 1331.63 | 55.32 | 6.08 |




Table 10: Effect of DD on ABO (Electricity, L=20,W=21,σ=6.5L=20,W=21,\sigma=6.5).

| DD | ResMSE | ResVAR | Te2eT\_{\text{e2e}} (ms) | Time (×\times2048) |
| --- | --- | --- | --- | --- |
| 2048 | 1.0189 | 10.86 | 8.52 | 1.00 |
| 8192 | 1.0096 | 10.92 | 52.29 | 6.13 |

## 6 Discussion

The experimental results validate that the ABO framework effectively extends the ”benign overfitting” phenomenon to recursive, non-stationary settings. The following subsections analyze the mathematical mechanisms driving these observations.

### 6.1 Implicit Regularization and the Minimum-Norm Solution

The ”double-descent” behavior observed in our RFF experiments confirms that the QR-EWRLS update performs an implicit regularization. As established in Remark [2.1](https://arxiv.org/html/2601.22200v1#S2.SS1 "2.1 Least squares via QR ‣ 2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"), the estimator converges to the unique minimum-ℓ2\ell\_{2}-norm solution when D>ND>N. This property is critical in non-stationary environments; it ensures that variance is distributed across the ”tail” of the feature spectrum. Consequently, high-frequency RFF components are only activated if they significantly contribute to reducing the residual, effectively allowing the model to interpolate the signal while remaining robust to noise—the hallmark of benign overfitting.

### 6.2 Numerical Stability in the Underdetermined Regime

A central challenge in overparameterized RLS is the singularity of the Gram matrix. In standard covariance-form RLS, the update PtP\_{t} becomes ill-conditioned as D>ND>N, leading to catastrophic divergence. By utilizing orthogonal-triangular updates via Givens rotations, ABO maintains the factor RtR\_{t} directly. Even when the system is heavily underdetermined, the condition number of the RR factor remains bounded. The Moore-Penrose pseudoinverse update via the Greville/Cline method ensures that the weight vector βt\beta\_{t} remains stable and avoids the null-space amplification typical of standard inversion.

### 6.3 Tracking vs. Overparameterization

In non-stationary environments, an inherent trade-off exists between the forgetting factor λ\lambda and the feature dimension DD. Our results indicate that overparameterization does not degrade tracking speed; rather, the increased degrees of freedom allow the filter to react more fluidly to regime shifts. The O​(N​D)O(ND) complexity of the QR-update ensures that this increased capacity does not come at a prohibitive computational cost, allowing for real-time adaptation in high-dimensional spaces.

### 6.4 Parallel Scalability and Ensemble Averaging

The decoupled nature of the RFF generation allows for a natural extension to distributed architectures. Since each feature component is independent prior to the RLS update, the feature space can be partitioned across multiple processing cores. Training sub-models on independent cores and subsequently averaging the estimators—akin to online bootstrap aggregating (bagging)—provides a secondary layer of variance reduction. This distributed approach not only reduces per-update latency but also stabilizes the estimator against heavy-tailed noise and outliers common in empirical time-series.

## 7 Conclusion

This paper introduced Adaptive Benign Overfitting (ABO), a framework that bridges the gap between modern overparameterization theory and classical adaptive filter design. By extending the Recursive Least Squares (RLS) algorithm into the D≫ND\gg N regime using Random Fourier Feature (RFF) mappings, we demonstrated that ”benign overfitting”—traditionally analyzed in batch settings—can be effectively harnessed for online learning in non-stationary environments.

The primary technical contribution is the development of a QR-based exponentially weighted RLS (QR-EWRLS) update mechanism. Unlike standard covariance-form RLS, which is prone to numerical instability in rank-deficient scenarios, our orthogonal-triangular formulation ensures numerical integrity through a recursive update of the Moore-Penrose pseudoinverse. We empirically validated that this approach reproduces the ”double descent” generalization curve while maintaining stable condition numbers, even as the feature dimension significantly exceeds the number of observations.

Furthermore, the decoupled nature of the RFF mappings suggests significant potential for computational acceleration. Future work will investigate parallelized ensemble architectures, where sub-segments of the high-dimensional feature space are processed across independent cores and aggregated via bootstrap aggregating (bagging) or variance-reduction averaging. Such a distributed approach would not only further reduce the per-update latency but also potentially enhance the robustness of the estimator in the presence of heavy-tailed noise.

## Appendix A Rank-One Updates and Downdates

Before arriving at the final QR–EWRLS formulation, an initial attempt was made using the classical covariance-form Recursive Least Squares (RLS) architecture, where the Gram matrix is defined as A=X⊤​XA=X^{\top}X.
While this formulation is conceptually straightforward, it is well known to suffer from numerical instability due to the ill-conditioning of AA under long sequences or near-collinear regressors.

To handle both full-rank and rank-deficient regimes, we employed a unified recursive strategy: the generalized matrix-sum identities of Campbell and Meyer [[6](https://arxiv.org/html/2601.22200v1#bib.bib6)] were used for singular matrices, while the Sherman–Morrison formula provided the corresponding rank-one update for non-singular cases.
This formulation enables explicit treatment of both regimes and serves as a theoretical stepping stone toward the stable QR-based approach presented later.

### A.1 Sherman–Morrison Update and Downdate Formulas

To maintain a fixed-length rolling window, it is necessary to remove the contribution of the oldest sample xt−Nx\_{t-N}.
In the non-singular case, the Sherman–Morrison formula provides the well-known rank-one update of the inverse matrix:

|  |  |  |
| --- | --- | --- |
|  | (At−1+xt​xt⊤)−1=At−1−1−At−1−1​xt​xt⊤​At−1−11+xt⊤​At−1−1​xt.(A\_{t-1}+x\_{t}x\_{t}^{\top})^{-1}=A\_{t-1}^{-1}-\frac{A\_{t-1}^{-1}x\_{t}x\_{t}^{\top}A\_{t-1}^{-1}}{1+x\_{t}^{\top}A\_{t-1}^{-1}x\_{t}}. |  |

Similarly, applying the inverse rank-one downdate yields

|  |  |  |
| --- | --- | --- |
|  | (At−1−xt−N​xt−N⊤)−1=At−1−1+At−1−1​xt−N​xt−N⊤​At−1−11−xt−N⊤​At−1−1​xt−N.(A\_{t-1}-x\_{t-N}x\_{t-N}^{\top})^{-1}=A\_{t-1}^{-1}+\frac{A\_{t-1}^{-1}x\_{t-N}x\_{t-N}^{\top}A\_{t-1}^{-1}}{1-x\_{t-N}^{\top}A\_{t-1}^{-1}x\_{t-N}}. |  |

### A.2 Rank-increasing Update and Rank-decreasing Downdate for the Singular Case

When At−1A\_{t-1} becomes singular, the classical inverse update no longer applies.
In this case, the generalized inverse identity of Campbell and Meyer can be used:

|  |  |  |
| --- | --- | --- |
|  | ct=xt⊤​(I−At−1†​At−1)c\_{t}=x\_{t}^{\top}(I-A\_{t-1}^{\dagger}A\_{t-1}) |  |

leading to the rank-increasing Sherman–Morrison-type update formula for the pseudoinverse:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (At−1+xt​xt⊤)†\displaystyle(A\_{t-1}+x\_{t}x\_{t}^{\top})^{\dagger} | =At−1†−At−1†​xt​(ct†)⊤−ct†​xt⊤​At−1†\displaystyle=A\_{t-1}^{\dagger}-A\_{t-1}^{\dagger}x\_{t}(c\_{t}^{\dagger})^{\top}-c\_{t}^{\dagger}x\_{t}^{\top}A\_{t-1}^{\dagger} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ct†​(ct†)⊤1+xt⊤​At−1†​xt\displaystyle\hskip 14.22636pt+\frac{c\_{t}^{\dagger}(c\_{t}^{\dagger})^{\top}}{1+x\_{t}^{\top}A\_{t-1}^{\dagger}x\_{t}} |  |

For the downdate, we define auxiliary quantities

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | h\displaystyle h | =xt−N⊤​At−1†,\displaystyle=x\_{t-N}^{\top}A\_{t-1}^{\dagger}, | k\displaystyle k | =At−1†​xt−N,\displaystyle=A\_{t-1}^{\dagger}x\_{t-N}, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | u\displaystyle u | =(I−At−1​At−1†)​xt−N,\displaystyle=(I-A\_{t-1}A\_{t-1}^{\dagger})x\_{t-N}, | v\displaystyle v | =xt−N⊤​(I−At−1†​At−1),\displaystyle=x\_{t-N}^{\top}(I-A\_{t-1}^{\dagger}A\_{t-1}), |  |

leading to the rank-decreasing Sherman–Morison-type downdate formula for the pseudoinverse:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (At−1−xt−N​xt−N⊤)†\displaystyle(A\_{t-1}-x\_{t-N}x\_{t-N}^{\top})^{\dagger} | =At−1†−k​k†​At−1†−At−1†​h†​h\displaystyle=A\_{t-1}^{\dagger}-kk^{\dagger}A\_{t-1}^{\dagger}-A\_{t-1}^{\dagger}h^{\dagger}h |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(k†​At−1†​h†)​k​h\displaystyle\hskip 14.22636pt+(k^{\dagger}A\_{t-1}^{\dagger}h^{\dagger})kh |  |

Although this formulation correctly handles both rank-deficient and full-rank regimes, its practical implementation proved highly sensitive to round-off errors and conditioning, particularly in long sequences.
Staub [[30](https://arxiv.org/html/2601.22200v1#bib.bib30)] reported similar instability when recursively updating the least-squares pseudoinverse

|  |  |  |
| --- | --- | --- |
|  | A†=C⊤​(C​C⊤)−1​(B​B⊤)−1​B⊤A^{\dagger}=C^{\top}(CC^{\top})^{-1}(BB^{\top})^{-1}B^{\top} |  |

where the explicit use of Gram matrices in the rank decomposition amplified numerical errors.
These limitations ultimately motivated the adoption of a QR-based orthogonal–triangular update in the classical and interpolation regimes, which is instead an orthogonal–trapezoidal update in the non-classical regime. We describe this in Section [2](https://arxiv.org/html/2601.22200v1#S2 "2 System Model ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series"). The QR updating method ensures numerical stability by preserving orthogonality and avoiding explicit matrix inversion.

## Appendix B Proof of the Forgetting Factor Scaling

We show that scaling At−1†A\_{t-1}^{\dagger} by the forgetting factor λ−1/2\lambda^{-1/2} prior to the update yields the correct recursive computation of At†A\_{t}^{\dagger}. The proof follows by expanding At†​AtA\_{t}^{\dagger}A\_{t} and exploiting the orthogonality of the residual component ctc\_{t}.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | At\displaystyle A\_{t} | =[λ​At−1at],\displaystyle=\begin{bmatrix}\sqrt{\lambda}A\_{t-1}\\[2.55005pt] a\_{t}\end{bmatrix}, | At†\displaystyle A\_{t}^{\dagger} | =[Bt−1bt]\displaystyle=\begin{bmatrix}B\_{t-1}&b\_{t}\end{bmatrix} |  |

Expanding the product At†​AtA\_{t}^{\dagger}A\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | At†​At\displaystyle A\_{t}^{\dagger}A\_{t} | =λ​Bt−1​At−1+bt​at,\displaystyle=\sqrt{\lambda}B\_{t-1}A\_{t-1}+b\_{t}a\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | At†​At​At−1†\displaystyle A\_{t}^{\dagger}A\_{t}A\_{t-1}^{\dagger} | =λ​Bt−1​At−1​At−1†+bt​at​At−1†\displaystyle=\sqrt{\lambda}B\_{t-1}A\_{t-1}A\_{t-1}^{\dagger}+b\_{t}a\_{t}A\_{t-1}^{\dagger} |  |

From this we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | At−1†\displaystyle A\_{t-1}^{\dagger} | =λ​Bt−1+bt​at​At−1†\displaystyle=\sqrt{\lambda}B\_{t-1}+b\_{t}a\_{t}A\_{t-1}^{\dagger} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Bt−1\displaystyle B\_{t-1} | =1λ​(At−1†−bt​at​At−1†)\displaystyle=\frac{1}{\sqrt{\lambda}}\bigl(A\_{t-1}^{\dagger}-b\_{t}a\_{t}A\_{t-1}^{\dagger}\bigr) |  |

Substituting into At†A\_{t}^{\dagger} gives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | At†=[1λ​(At−1†−bt​at​At−1†)bt]A\_{t}^{\dagger}=\begin{bmatrix}\frac{1}{\sqrt{\lambda}}\bigl(A\_{t-1}^{\dagger}-b\_{t}a\_{t}A\_{t-1}^{\dagger}\bigr)&b\_{t}\end{bmatrix} |  | (28) |

Define ctc\_{t} as the component of ata\_{t} orthogonal to the column space of At−1A\_{t-1}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ct\displaystyle c\_{t} | =at−at​At−1†​At−1,\displaystyle=a\_{t}-a\_{t}A\_{t-1}^{\dagger}A\_{t-1}, |  | (29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ct\displaystyle c\_{t} | =at​(I−At−1†​At−1).\displaystyle=a\_{t}(I-A\_{t-1}^{\dagger}A\_{t-1}). |  | (30) |

Substituting ([30](https://arxiv.org/html/2601.22200v1#A2.E30 "In Appendix B Proof of the Forgetting Factor Scaling ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series")) into ([28](https://arxiv.org/html/2601.22200v1#A2.E28 "In Appendix B Proof of the Forgetting Factor Scaling ‣ Adaptive Benign Overfitting (ABO): Overparameterized RLS for Online Learning in Non-stationary Time-series")) yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | At†​At\displaystyle A\_{t}^{\dagger}A\_{t} | =At−1†​At−1−bt​at​At−1†​At−1+bt​at\displaystyle=A\_{t-1}^{\dagger}A\_{t-1}-b\_{t}a\_{t}A\_{t-1}^{\dagger}A\_{t-1}+b\_{t}a\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | At†​At​At−1†\displaystyle A\_{t}^{\dagger}A\_{t}A\_{t-1}^{\dagger} | =At−1†​At−1​At−1†+bt​ct​At−1†\displaystyle=A\_{t-1}^{\dagger}A\_{t-1}A\_{t-1}^{\dagger}+b\_{t}c\_{t}A\_{t-1}^{\dagger} |  |

Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | At−1†\displaystyle A\_{t-1}^{\dagger} | =At−1†+bt​ct​At−1†\displaystyle=A\_{t-1}^{\dagger}+b\_{t}c\_{t}A\_{t-1}^{\dagger} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ct​At−1†\displaystyle c\_{t}A\_{t-1}^{\dagger} | =0\displaystyle=0 |  |

This demonstrates that ctc\_{t} is orthogonal to the row space of At−1†A\_{t-1}^{\dagger}, and therefore to the column space of At−1A\_{t-1}.
Since ct†=ct⊤‖ct‖2c\_{t}^{\dagger}=\frac{c\_{t}^{\top}}{\|c\_{t}\|^{2}} is a scalar multiple of ct⊤c\_{t}^{\top}, we have ct†​ct=1c\_{t}^{\dagger}c\_{t}=1.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ct​ct†\displaystyle c\_{t}c\_{t}^{\dagger} | =at​ct†−at​At−1†​At−1​ct†\displaystyle=a\_{t}c\_{t}^{\dagger}-a\_{t}A\_{t-1}^{\dagger}A\_{t-1}c\_{t}^{\dagger} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ct†​ct\displaystyle c\_{t}^{\dagger}c\_{t} | =at​ct†\displaystyle=a\_{t}c\_{t}^{\dagger} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | at​ct†\displaystyle a\_{t}c\_{t}^{\dagger} | =1\displaystyle=1 |  |

Define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pt\displaystyle P\_{t} | =At−1†​At−1+ct†​ct\displaystyle=A\_{t-1}^{\dagger}A\_{t-1}+c\_{t}^{\dagger}c\_{t} |  |

Then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | at​Pt\displaystyle a\_{t}P\_{t} | =at​At−1†​At−1+at​ct†​ct\displaystyle=a\_{t}A\_{t-1}^{\dagger}A\_{t-1}+a\_{t}c\_{t}^{\dagger}c\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | at​Pt\displaystyle a\_{t}P\_{t} | =at​At−1†​At−1+ct\displaystyle=a\_{t}A\_{t-1}^{\dagger}A\_{t-1}+c\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | at​Pt\displaystyle a\_{t}P\_{t} | =at\displaystyle=a\_{t} |  |

Moreover,

|  |  |  |
| --- | --- | --- |
|  | At−1​Pt=At−1A\_{t-1}P\_{t}=A\_{t-1} |  |

so PtP\_{t} acts as a right identity for AtA\_{t}:

|  |  |  |
| --- | --- | --- |
|  | Pt=At†​AtP\_{t}=A\_{t}^{\dagger}A\_{t} |  |

Now,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ct†​ct\displaystyle c\_{t}^{\dagger}c\_{t} | =Pt−At−1†​At−1\displaystyle=P\_{t}-A\_{t-1}^{\dagger}A\_{t-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ct†​ct\displaystyle c\_{t}^{\dagger}c\_{t} | =At−1†​At−1−bt​at​At−1†​At−1\displaystyle=A\_{t-1}^{\dagger}A\_{t-1}-b\_{t}a\_{t}A\_{t-1}^{\dagger}A\_{t-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +bt​at−At−1†​At−1\displaystyle\hskip 14.22636pt+b\_{t}a\_{t}-A\_{t-1}^{\dagger}A\_{t-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ct†​ct\displaystyle c\_{t}^{\dagger}c\_{t} | =bt​ct\displaystyle=b\_{t}c\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ct†\displaystyle c\_{t}^{\dagger} | =bt\displaystyle=b\_{t} |  |

Substituting back gives:

|  |  |  |
| --- | --- | --- |
|  | At†=[1λ​(At−1†−ct†​at​At−1†)ct†]A\_{t}^{\dagger}=\begin{bmatrix}\frac{1}{\sqrt{\lambda}}\bigl(A\_{t-1}^{\dagger}-c\_{t}^{\dagger}a\_{t}A\_{t-1}^{\dagger}\bigr)&c\_{t}^{\dagger}\end{bmatrix} |  |

#### Case: ct=0c\_{t}=0

When ct=0c\_{t}=0, at=at​At−1†​At−1a\_{t}=a\_{t}A\_{t-1}^{\dagger}A\_{t-1}, meaning ata\_{t} lies in the row space of At−1A\_{t-1}.
Let dt=at​At−1†d\_{t}=a\_{t}A\_{t-1}^{\dagger} and define:

|  |  |  |
| --- | --- | --- |
|  | T=At−1​At−1†−At−1​bt​dt.\displaystyle T=A\_{t-1}A\_{t-1}^{\dagger}-A\_{t-1}b\_{t}d\_{t}. |  |

As TT is symmetric, At−1​bt​dtA\_{t-1}b\_{t}d\_{t} must also be symmetric. Thus, At−1​bt=h​dt⊤A\_{t-1}b\_{t}=hd\_{t}^{\top} for some scalar hh.

Now we have

|  |  |  |
| --- | --- | --- |
|  | At​At†=[At−1​At−1†−h​dt⊤​dt1λ​(dt−h​dt​dt⊤​dt)λ​h​dt⊤h​dt⊤​dt]A\_{t}A\_{t}^{\dagger}=\begin{bmatrix}A\_{t-1}A\_{t-1}^{\dagger}-hd\_{t}^{\top}d\_{t}&\frac{1}{\sqrt{\lambda}}(d\_{t}-hd\_{t}d\_{t}^{\top}d\_{t})\\ \sqrt{\lambda}hd\_{t}^{\top}&hd\_{t}^{\top}d\_{t}\end{bmatrix} |  |

From symmetry in At​At†A\_{t}A\_{t}^{\dagger}, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​h​(dt⊤)⊤\displaystyle\sqrt{\lambda}h(d\_{t}^{\top})^{\top} | =1λ​(dt−h​dt​dt⊤​dt)\displaystyle=\frac{1}{\sqrt{\lambda}}(d\_{t}-hd\_{t}d\_{t}^{\top}d\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | dt\displaystyle d\_{t} | =h​dt​dt⊤​dt+λ​h​dt\displaystyle=hd\_{t}d\_{t}^{\top}d\_{t}+\lambda hd\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | dt\displaystyle d\_{t} | =λ​h​(1λ​dt​dt⊤​dt+dt)\displaystyle=\lambda h(\frac{1}{\lambda}d\_{t}d\_{t}^{\top}d\_{t}+d\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | h\displaystyle h | =1λ1+1λ​dt​dt⊤\displaystyle=\frac{\frac{1}{\lambda}}{1+\frac{1}{\lambda}d\_{t}d\_{t}^{\top}} |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | bt\displaystyle b\_{t} | =1λ​At−1†​dt⊤1+1λ​dt​dt⊤\displaystyle=\frac{\frac{1}{\lambda}A\_{t-1}^{\dagger}d\_{t}^{\top}}{1+\frac{1}{\lambda}d\_{t}d\_{t}^{\top}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | At†\displaystyle A\_{t}^{\dagger} | =[1λ​(At−1†−1λ​At−1†​dt⊤​dt1+1λ​dt​dt⊤)1λ​At−1†​dt⊤1+1λ​dt​dt⊤]\displaystyle=\begin{bmatrix}\frac{1}{\sqrt{\lambda}}\left(A\_{t-1}^{\dagger}-\frac{\frac{1}{\lambda}A\_{t-1}^{\dagger}d\_{t}^{\top}d\_{t}}{1+\frac{1}{\lambda}d\_{t}d\_{t}^{\top}}\right)&\frac{\frac{1}{\lambda}A\_{t-1}^{\dagger}d\_{t}^{\top}}{1+\frac{1}{\lambda}d\_{t}d\_{t}^{\top}}\end{bmatrix} |  |

This proves that pre-scaling Rt−1†R\_{t-1}^{\dagger} by the forgetting factor before the update yields the correct recursive form of Rt†R\_{t}^{\dagger}.

###### Lemma 1 (Weighted Downdate Consistency).

Let RtR\_{t} denote the upper-trapezoidal factor obtained at time tt after the update step
but before the downdate, corresponding to the exponentially weighted observations
{zt−i}i=0N\{z\_{t-i}\}\_{i=0}^{N}.
Then the application of the downdate rotation Gt−NG\_{t-N} followed by the pseudoinverse
downdate step computes the Moore–Penrose pseudoinverse of the matrix obtained by
removing the weighted observation λN​zt−N\sqrt{\lambda^{N}}\,z\_{t-N} from the sliding window.

###### Proof.

At time tt, the observation zt−Nz\_{t-N} has undergone NN successive scaling operations
by a factor λ\sqrt{\lambda}.
Its effective contribution to the factor RtR\_{t} is therefore

|  |  |  |
| --- | --- | --- |
|  | v=λN/2​zt−Nv=\lambda^{N/2}z\_{t-N} |  |

The downdate rotation Gt−NG\_{t-N} is constructed to isolate this contribution by aligning
the corresponding row with the canonical basis vector e1e\_{1}.
In the implicit-QQ formulation, this yields

|  |  |  |
| --- | --- | --- |
|  | Gt−N⊤​Rt=[v⊤R~t]=[λN​zt−N⊤R~t]G\_{t-N}^{\top}R\_{t}=\begin{bmatrix}v^{\top}\\ \widetilde{R}\_{t}\end{bmatrix}=\begin{bmatrix}\sqrt{\lambda^{N}}\,z\_{t-N}^{\top}\\ \widetilde{R}\_{t}\end{bmatrix} |  |

Applying the generalized Moore–Penrose pseudoinverse downdate formula for rank-one
removals is algebraically equivalent to subtracting the outer product v​v⊤vv^{\top} from
the corresponding Gramian:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt⊤​Rt−v​v⊤\displaystyle R\_{t}^{\top}R\_{t}-vv^{\top} | =∑i=0Nλi​zt−i​zt−i⊤−λN​zt−N​zt−N⊤\displaystyle=\sum\_{i=0}^{N}\lambda^{i}z\_{t-i}z\_{t-i}^{\top}-\lambda^{N}z\_{t-N}z\_{t-N}^{\top} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=0N−1λi​zt−i​zt−i⊤\displaystyle=\sum\_{i=0}^{N-1}\lambda^{i}z\_{t-i}z\_{t-i}^{\top} |  |

This expression is precisely the Gramian associated with the exponentially weighted
sliding window {zt−i}i=0N−1\{z\_{t-i}\}\_{i=0}^{N-1}.
Hence, removing the isolated row of the rotated factor is algebraically equivalent to
removing the oldest weighted observation from the underlying least-squares objective.
∎

## Acknowledgment

The authors would like to thank Konstaninos Ntetsikas and Andrew Ching Hoe Lee for their diligent work on the group project which became the basis for the further refinements in this paper. Nick Firoozye would also like to thank Fauziah Ariff for her insightful comments and support during the work’s lengthy gestation as well as during the preparation of this manuscript.

## References

* [1]

  Takuya Akiba, Shotaro Sano, Toshihiko Yanase, Takeru Ohta, and Masanori Koyama.
  Optuna: A next-generation hyperparameter optimization framework.
  In Proceedings of the 25th ACM SIGKDD International Conference
  on Knowledge Discovery & Data Mining, 2019.
* [2]

  S. Thomas Alexander and Avinash L. Ghimikar.
  A method for recursive least squares filtering based upon an inverse
  qr decomposition.
  IEEE Transactions on Signal Processing, 41(1):20, 1993.
* [3]

  ed. Apolinário Jr, João A.
  QRD–RLS Adaptive Filtering.
  Springer, 2009.
* [4]

  Peter L Bartlett, Philip M Long, Gábor Lugosi, and Alexander Tsigler.
  Benign overfitting in linear regression.
  Proceedings of the National Academy of Sciences,
  117(48):30063–30070, 2020.
* [5]

  Mikhail Belkin, Daniel Hsu, Siyuan Ma, and Soumik Mandal.
  Reconciling modern machine-learning practice and the classical
  bias–variance trade-off.
  Proceedings of the National Academy of Sciences,
  116(32):15849–15854, 2019.
* [6]

  Stephen L. Campbell and Carl D. Meyer.
  Generalized Inverses of Linear Transformations.
  Society for Industrial and Applied Mathematics, 2009.
* [7]

  Randall E. Cline.
  Representations for the generalized inverse of a partitioned matrix.
  Journal of the Society for Industrial and Applied Mathematics,
  12(3):588–600, 1964.
* [8]

  George Cybenko.
  Approximation by superpositions of a sigmoidal function.
  Mathematics of Control, Signals and Systems, 2:303–314, 1989.
* [9]

  Ender M. Eksioglu and A. Korhan Tanc.
  Rls algorithm with convex regularization.
  IEEE Signal Processing Letters, 18(8):470–473, 2011.
* [10]

  Patrick Flandrin.
  Time-Frequency/Time-Scale Analysis.
  Academic Press, San Diego, 1998.
* [11]

  Gene H. Golub and Charles F. Van Loan.
  Matrix Computations.
  Johns Hopkins University Press, Baltimore, MD, 3rd edition, 1996.
* [12]

  Damodar N. Gujarati and Dawn C. Porter.
  Basic Econometrics.
  McGraw-Hill, Singapore, 2003.
* [13]

  Sven Hammarling and Craig Lucas.
  Updating the qr factorization and the least squares problem.
  2008.
* [14]

  Robert Hartwig.
  Rank factorization and moore-penrose inversion.
  Industrial Mathematics, 26, 1976.
* [15]

  Trevor Hastie, Andrea Montanari, Saharon Rosset, and Ryan J. Tibshirani.
  Surprises in high-dimensional ridgeless least squares interpolation.
  Annals of Statistics, 50(2):949–986, 2022.
* [16]

  Trevor Hastie, Robert Tibshirani, and Jerome H. Friedman.
  The Elements of Statistical Learning: Data Mining, Inference,
  and Prediction.
  Springer, 2nd edition, 2009.
* [17]

  Simon Haykin.
  Adaptive Filter Theory.
  Prentice Hall, 4th edition, 2002.
* [18]

  Nicholas J. Higham.
  Accuracy and Stability of Numerical Algorithms.
  Society for Industrial and Applied Mathematics, 2nd edition, 2002.
* [19]

  David Hogg and Soledad Villar.
  Feature weighting and double descent in high-frequency interpolation.
  arXiv preprint arXiv:2305.01624, 2023.
* [20]

  Xia Hong, Junbin Gao, and Sheng Chen.
  Zero-attracting recursive least squares algorithms.
  IEEE Transactions on Vehicular Technology, 66(1):213–221,
  2017.
* [21]

  Kurt Hornik.
  Approximation capabilities of multilayer feedforward networks.
  Neural Networks, 4(2):251–257, 1991.
* [22]

  Arthur Jacot, Franck Gabriel, and Clément Hongler.
  Neural tangent kernel: Convergence and generalization in neural
  networks.
  In Proceedings of the 32nd International Conference on Neural
  Information Processing Systems (NeurIPS), 2018.
* [23]

  Holger Kantz and Thomas Schreiber.
  Nonlinear Time Series: Analysis, Methods and Applications.
  Cambridge University Press, 2004.
* [24]

  Song Mei and Andrea Montanari.
  The generalization error of random features regression: Precise
  asymptotics and double descent curve.
  Communications on Pure and Applied Mathematics, 75(4):667–766,
  2022.
* [25]

  C.-T. Pan and R.J. Plemmons.
  Least squares modifications with inverse factorizations: Parallel
  implications.
  Journal of Computational and Applied Mathematics,
  27(1):109–127, 1989.
  Special Issue on Parallel Algorithms for Numerical Linear Algebra.
* [26]

  José C. Príncipe, Weifeng Liu, and Simon Haykin.
  Kernel Adaptive Filtering: A Comprehensive Introduction.
  John Wiley & Sons, 2011.
* [27]

  Ali Rahimi and Benjamin Recht.
  Random features for large-scale kernel machines.
  In Advances in Neural Information Processing Systems (NeurIPS),
  2007.
* [28]

  Ali H. Sayed.
  Fundamentals of Adaptive Filtering.
  John Wiley & Sons, 2003.
* [29]

  Enrique Sentana.
  Econometric applications of positive rank‐one modifications of the
  symmetric factorization of a positive semi‐definite matrix.
  Spanish Economic Review, 1(1):79–90, 1999.
* [30]

  Ruben Staub and Stephan N. Steinmann.
  Efficient recursive least squares solver for rank-deficient matrices.
  Applied Mathematics and Computation, 399:125996, 2021.
* [31]

  Qian Su and Dino Sejdinovic.
  Benign overfitting and noisy features.
  Journal of the American Statistical Association,
  118(541):164–177, 2023.
* [32]

  Yitong Sun, Anna Gilbert, and Ambuj Tewari.
  On the approximation properties of random relu features.
  arXiv preprint arXiv:1810.04374, 2018.
* [33]

  Sašo Tomažič.
  On short-time fourier transform with single-sided exponential window.
  Signal Processing, 55(2):141–148, 1996.
* [34]

  Sašo Tomažič.
  On short-time Fourier transform with single-sided exponential
  window.
  Signal Processing, 55(2):141–148, 1996.
* [35]

  Artur Trindade.
  ElectricityLoadDiagrams20112014.
  UCI Machine Learning Repository, 2015.
  DOI: https://doi.org/10.24432/C58C86.
* [36]

  Alexander Tsigler and Peter L Bartlett.
  Benign overfitting in ridge regression.
  The Journal of Machine Learning Research, 24(1):5202–5277,
  2023.
* [37]

  S. Van Vaerenbergh, J. Via, and I. Santamaria.
  A sliding-window kernel rls algorithm and its application to
  nonlinear channel identification.
  In 2006 IEEE International Conference on Acoustics Speech and
  Signal Processing Proceedings, volume 5, pages V–V, 2006.
* [38]

  Isao Yamada, Nobuhiko Ogura, and Masahiro Yukawa.
  Adaptive projected subgradient method and its acceleration
  techniques.
  IFAC Proceedings Volumes, 37(12):639–644, 2004.
  IFAC Workshop on Adaptation and Learning in Control and Signal
  Processing (ALCOSP 04) and IFAC Workshop on Periodic Control Systems (PSYCO
  04), Yokohama, Japan, 30 August - 1 September, 2004.
* [39]

  Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, and Oriol Vinyals.
  Understanding deep learning requires rethinking generalization.
  In Proceedings of the International Conference on Learning
  Representations (ICLR), 2017.