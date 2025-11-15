---
authors:
- Paul Ruelloux
- Christian Bongiorno
- Damien Challet
doc_id: arxiv:2511.10478v1
family_id: arxiv:2511.10478
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Noise-proofing Universal Portfolio Shrinkage
url_abs: http://arxiv.org/abs/2511.10478v1
url_html: https://arxiv.org/html/2511.10478v1
venue: arXiv q-fin
version: 1
year: 2025
---


Paul Ruelloux1,2, Christian Bongiorno1, Damien Challet1,
  
1Université Paris-Saclay, Laboratoire de Mathématiques et Informatique pour la Complexité et les Systèmes (MICS)
  
2Barclays Bank Ireland PLC
  
{name}.{surname}@centralesupelec.fr

###### Abstract

We enhance the Universal Portfolio Shrinkage Approximator (UPSA) of Kelly et al. ([2023](https://arxiv.org/html/2511.10478v1#bib.bib9)) by making it more robust with respect to estimation noise and covariate shift. UPSA optimizes the realized Sharpe ratio using a relatively small calibration window, leveraging ridge penalties and cross-validation to yield better portfolios. Yet, it still suffers from the staggering amount of noise in financial data. We propose two methods to make UPSA more robust and improve its efficiency: time-averaging of the optimal penalty weights and using the Average Oracle correlation eigenvalues to make covariance matrices less noisy and more robust to covariate shift. Combining these two long-term averages outperforms UPSA by a large margin in most specifications.

## 1 Introduction

Markowitz portfolio theory (Markowitz, [1952](https://arxiv.org/html/2511.10478v1#bib.bib12)) prescribes efficient portfolios that achieve maximum risk-adjusted performance, but the quality of such portfolios depends critically on the accuracy of the estimated covariance matrix (Michaud, [1989](https://arxiv.org/html/2511.10478v1#bib.bib13)). In practice, estimation noise severely undermines performance, especially when the number of assets nn is of the same order as the sample size Δ​t\Delta t, i.e., in the high-dimensional case: sample covariance matrix estimates become very noisy and require filtering. Current state-of-the-art shrinkage methods address this problem by transforming the in-sample (IS) eigenvalues to minimize the expected mean-squared error (MSE) between the sample and population covariance matrices, thereby indirectly improving the out-of-sample (OOS) portfolio performance (Bun et al., [2017](https://arxiv.org/html/2511.10478v1#bib.bib4); Ledoit and
Péché, [2011](https://arxiv.org/html/2511.10478v1#bib.bib11)).

The Universal Portfolio Shrinkage Approximator (UPSA), proposed by Kelly et al. ([2023](https://arxiv.org/html/2511.10478v1#bib.bib9)), is a flexible nonlinear spectral shrinkage method that aims to maximize the expected OOS Sharpe ratio. Its robustness comes from Cross-Validation (CV) and weighted set of portfolios associated to ridge penalization factors. While improves upon simpler shrinkage techniques, it still suffers from sample noise: the optimal ridge portfolio weights tend to be concentrated on a single one, which itself varies much as a function of time. This comes from the fact that CV still leaves too much noise in high-dimensional settings and cannot account for covariate shift (Cawley and Talbot, [2010](https://arxiv.org/html/2511.10478v1#bib.bib5); Arlot and Celisse, [2010](https://arxiv.org/html/2511.10478v1#bib.bib1)). As a consequence, the performance of UPSA substantially depends on the ridge penalty grid and can be improved by further filtering.

We propose two simple remedies that boost UPSA performance by reducing the influence of sample noise. First, we replace sample-specific optimal weights of ridge-penalized portfolios with their time averages (computed over expanding time windows). Second, we apply a pre-filtering of correlation eigenvalues known as the Average Oracle (AO) method (Bongiorno et al., [2023](https://arxiv.org/html/2511.10478v1#bib.bib3)), which also replaces local filtering with time averages of optimal eigenvalues; this method is known to over-perform CV (Bongiorno et al., [2023](https://arxiv.org/html/2511.10478v1#bib.bib3); Bongiorno and Challet, [2024](https://arxiv.org/html/2511.10478v1#bib.bib2)). Combining both improvements brings better performance than either UPSA or AO alone when applied on monthly factor returns.

This letter is organized as follows. Section 2 introduces the rationale and construction of UPSA and discusses its limitations and introduces the proposed remedies. Section 3 reports empirical results across different configurations. Section 4 concludes and proposes to interpret UPSA as first-order improvement of Average Oracle.

## 2 Estimators

### 2.1 Universal Portfolio Shrinkage Approximator (UPSA)

The objective of a shrinkage approach is to obtain an improved estimate of the unknown population covariance matrix 𝚺\boldsymbol{\Sigma} from a finite-sample covariance estimator
𝚺^=1Δ​t​(𝑿−𝝁^)​(𝑿−𝝁^)⊤\hat{\boldsymbol{\Sigma}}=\frac{1}{\Delta t}(\boldsymbol{X}-\hat{\boldsymbol{\mu}})(\boldsymbol{X}-\hat{\boldsymbol{\mu}})^{\top},
where XX denotes the n×Δ​tn\times\Delta t matrix of observations with true mean 𝝁\boldsymbol{\mu} and covariance 𝚺\boldsymbol{\Sigma}.
The method proceeds from the spectral decomposition of 𝚺^\hat{\boldsymbol{\Sigma}}, expressed as
𝚺^=𝑽^​𝚲^​𝑽^⊤\hat{\boldsymbol{\Sigma}}=\hat{\boldsymbol{V}}\hat{\boldsymbol{\Lambda}}\hat{\boldsymbol{V}}^{\top},
where 𝑽^\hat{\boldsymbol{V}} is the orthogonal matrix of eigenvectors and 𝚲^\hat{\boldsymbol{\Lambda}} is the diagonal matrix of sample eigenvalues 𝝀={λk}k=1n\boldsymbol{\lambda}=\{\lambda\_{k}\}\_{k=1}^{n}.
Shrinkage consists in replacing the empirical eigenvalues λ^k\hat{\lambda}\_{k} with shrunk (adjusted) values f^​(λ^k)\hat{f}(\hat{\lambda}\_{k}),
where f^\hat{f} is a shrinkage function that optimizes a well-chosen cost function: while the so-called Non-Linear Shrinkage (NLS) estimators minimize the estimation error of 𝚺^\hat{\boldsymbol{\Sigma}} (Ledoit and
Péché, [2011](https://arxiv.org/html/2511.10478v1#bib.bib11)), UPSA aims at maximizing the realized Sharpe ratio. Both methods use data from the calibration window only. As a consequence, the shrinkage function ff itself is subject to noise and is denoted by f^\hat{f}.

The resulting covariance estimator takes the general form

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚵^=𝑽^​Diag ​(f^​(𝝀^))​𝑽^⊤,\boldsymbol{\hat{\Xi}}=\boldsymbol{\hat{V}}\,\textrm{Diag }(\hat{f}(\hat{\boldsymbol{\lambda}}))\boldsymbol{\hat{V}^{\top}}, |  | (1) |

where we used a slight abuse of notation: f^​(𝝀^)\hat{f}(\hat{\boldsymbol{\lambda}}) denotes the vector of shrunk eigenvalues f^​(λ^i)\hat{f}(\hat{\lambda}\_{i}).

In the general formulation, a shrinkage function f:ℐ⊂ℝ+→ℝ+f:\mathcal{I}\subset\mathbb{R}\_{+}\rightarrow\mathbb{R}\_{+} can be expressed as a function of a positive finite measure ν\nu on ℝ+\mathbb{R}\_{+} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀λ∈ℝ+,f​(λ)=∫0∞1z+λ​𝑑ν​(z).\forall\lambda\in\mathbb{R}\_{+},\quad f(\lambda)=\int\_{0}^{\infty}\frac{1}{z+\lambda}\,d\nu(z). |  | (2) |

Thus, finding the optimal f^\hat{f} given the calibration data and a choice of loss function is equivalent to finding the optimal ν^\hat{\nu}.
Kelly et al. ([2023](https://arxiv.org/html/2511.10478v1#bib.bib9)) replace the integral by a weighted combination of ridge-penalized terms ζi​k:=(λk+zi)−1\zeta\_{ik}:=(\lambda\_{k}+z\_{i})^{-1}

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(λ)≈f​(λk∣𝐳,𝜶)=∑i=1ℓαi​ζi​k=∑i=1ℓαizi+λk,withk=1,…,n,f(\lambda)\approx f(\lambda\_{k}\mid\mathbf{z},\boldsymbol{\alpha})=\sum\_{i=1}^{\ell}\alpha\_{i}\zeta\_{ik}=\sum\_{i=1}^{\ell}\frac{\alpha\_{i}}{z\_{i}+\lambda\_{k}},\quad\text{with}\quad k=1,\dots,n, |  | (3) |

where ziz\_{i} are the ridge penalties associated with each weight αi\alpha\_{i}. Given a set of ridge penalties 𝐳={zi}i=1ℓ\mathbf{z}=\{z\_{i}\}\_{i=1}^{\ell}, the weights 𝜶={αi}i=1ℓ\boldsymbol{\alpha}=\{\alpha\_{i}\}\_{i=1}^{\ell} are chosen so as to optimize the loss function.

Let us focus on the Sharpe ratio-maximizing procedure of UPSA: the mixture weights 𝜶\boldsymbol{\alpha} are estimated through a leave-one-out procedure that separates IS estimation from OOS evaluation. For each fold and each ridge level ziz\_{i}, the method applies the eigenvalue shrinkage defined by ζi​k:=(λk+zi)−1\zeta\_{ik}:=(\lambda\_{k}+z\_{i})^{-1} to the IS covariance estimator 𝚵^\hat{\boldsymbol{\Xi}} and, using the resulting filtered precision matrix together with IS means, computes the IS maximum–Sharpe-ratio portfolio. This portfolio is then evaluated on the held-out data to obtain its OOS return. Averaging these basis returns over all the folds yields the OOS mean vector and covariance matrix of basis returns, denoted 𝒎^​(𝐳)∈ℝℓ\hat{\boldsymbol{m}}(\mathbf{z})\in\mathbb{R}^{\ell}and 𝑺^​(𝐳)∈ℝℓ×ℓ\hat{\boldsymbol{S}}(\mathbf{z})\in\mathbb{R}^{\ell\times\ell}. The weights 𝜶\boldsymbol{\alpha} are then chosen to maximize a concave quadratic objective aligned with the Sharpe criterion, yielding pseudo OOS optimal ridge weights:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶^UPSA=arg⁡max𝜶≥0, 1⊤​𝜶=1⁡𝜶⊤​𝒎^​(𝐳)−12​𝜶⊤​𝑺^​(𝐳)​𝜶.\hat{\boldsymbol{\alpha}}\_{\mathrm{UPSA}}=\arg\max\_{\boldsymbol{\alpha}\geq 0,\;\mathbf{1}^{\top}\boldsymbol{\alpha}=1}\;\;\boldsymbol{\alpha}^{\top}\hat{\boldsymbol{m}}(\mathbf{z})-\frac{1}{2}\,\boldsymbol{\alpha}^{\top}\hat{\boldsymbol{S}}(\mathbf{z})\,\boldsymbol{\alpha}. |  | (4) |

Because all moments entering this program are computed on held-out data via the leave-one-out construction, the procedure aims to improve OOS performance.

Finally, the UPSA weights 𝜶^UPSA\hat{\boldsymbol{\alpha}}\_{\mathrm{UPSA}} are be plugged in Eq. ([3](https://arxiv.org/html/2511.10478v1#S2.E3 "In 2.1 Universal Portfolio Shrinkage Approximator (UPSA) ‣ 2 Estimators ‣ Noise-proofing Universal Portfolio Shrinkage")) to recover the filtered covariance as in Eq. ([1](https://arxiv.org/html/2511.10478v1#S2.E1 "In 2.1 Universal Portfolio Shrinkage Approximator (UPSA) ‣ 2 Estimators ‣ Noise-proofing Universal Portfolio Shrinkage")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^​(λ∣𝐳,𝜶^UPSA)=∑i=1ℓα^i,UPSAzi+λ,thus,𝚵^UPSA=𝑽^​Diag ​(f^​(𝚲^∣𝐳,𝜶^UPSA))​𝑽^⊤.\hat{f}(\lambda\mid\mathbf{z},\hat{\boldsymbol{\alpha}}\_{\mathrm{UPSA}})=\sum\_{i=1}^{\ell}\frac{\hat{\alpha}\_{i,\mathrm{UPSA}}}{z\_{i}+\lambda},\qquad\mathrm{thus,}\qquad\hat{\boldsymbol{\Xi}}\_{\mathrm{UPSA}}=\hat{\boldsymbol{V}}\,\textrm{Diag }(\hat{f}(\hat{\boldsymbol{\Lambda}}\mid\mathbf{z},\hat{\boldsymbol{\alpha}}\_{\mathrm{UPSA}})\,)\hat{\boldsymbol{V}}^{\top}. |  | (5) |

Keeping all the hats was notation-wise heavy but rewarding as it made the sources of noise explicit. In fact, we have neglected the fact that the choice of the grid 𝐳\mathbf{z} may also depend on the calibration data.

### 2.2 Noise-proofing UPSA

While UPSA is mathematically sound, it can be further improved. A strong (self-imposed) constraint in UPSA is the use of a relatively short calibration window. This choice mechanically leads to quite noisy outcomes, especially when computing optimal quantities, even with a leave-one-out approach. Figure [1](https://arxiv.org/html/2511.10478v1#S2.F1 "Figure 1 ‣ 2.2 Noise-proofing UPSA ‣ 2 Estimators ‣ Noise-proofing Universal Portfolio Shrinkage") displays the UPSA weights 𝜶^UPSA\hat{\boldsymbol{\alpha}}\_{\mathrm{UPSA}} as a function of time, computed on the same dataset as Kelly et al. ([2023](https://arxiv.org/html/2511.10478v1#bib.bib9)), described below in section [3](https://arxiv.org/html/2511.10478v1#S3 "3 Empirical Results ‣ Noise-proofing Universal Portfolio Shrinkage"). We also report the Herfindal Index, a measure of weight concentration, defined here as 1/∑i=1ℓ|αi|21/\sum\_{i=1}^{\ell}|\alpha\_{i}|^{2}; it equals 1 for perfectly concentrated vectors, and ℓ\ell for uniform weights (Sleuwaegen et al., [1989](https://arxiv.org/html/2511.10478v1#bib.bib14)). The average absolute change of weights between two calibrations is about 0.45. In short, the weights are highly concentrated on values that change very often.

![Refer to caption](x1.png)


Figure 1: Top : Heatmap of UPSA ridge weights in time computed on JKP US factors’ monthly returns, with n=153n=153 factors, with a ridge penalty grid of ℓ=20\ell=20 log-spaced points in [10−10,10−1][10^{-10},10^{-1}]. Bottom: Herfindahl Index (HI) vs time.

#### Averaged UPSA Ridge Weights (AvgUPSA)

The most basic way to mitigate noisy weights is to replace them with a time average (with expanding window): at time tt, Eq. ([4](https://arxiv.org/html/2511.10478v1#S2.E4 "In 2.1 Universal Portfolio Shrinkage Approximator (UPSA) ‣ 2 Estimators ‣ Noise-proofing Universal Portfolio Shrinkage")) , 𝜶^UPSA,t\hat{\boldsymbol{\alpha}}\_{\mathrm{UPSA},t} becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶^AvgUPSA,t=1t−t0​∑t′=t0t𝜶^UPSA,t′.\hat{\boldsymbol{\alpha}}\_{\mathrm{AvgUPSA},\,t}=\frac{1}{t-t\_{0}}\sum\_{t^{\prime}=t\_{0}}^{t}\hat{\boldsymbol{\alpha}}\_{\mathrm{UPSA},\,t^{\prime}}\,. |  | (6) |

This solves the noise in the t≫t0t\gg t\_{0} limit but is bound to lack reactivity.

#### Average Oracle (AO)

A major cause of noise in the UPSA weights is the estimation of the covariance matrices. While LOO does filter some noise out, it is far less efficient than other cross-validation techniques in this context (Lamrani et al., [2025](https://arxiv.org/html/2511.10478v1#bib.bib10)). In addition, if at all possible, one should account for the typical way covariance matrices change between calibration window and the test window due to covariate shift. This is the idea behind the Average Oracle, which replaces the sample eigenvalues by rank-wise averages of past "oracle" eigenvalues: it uses the data from past test windows to compute optimal eigenvalues and thus accounts for some covariate shift (Bongiorno et al., [2023](https://arxiv.org/html/2511.10478v1#bib.bib3)).
In order to calibrate the oracle eigenvalues, one considers many consecutive calibration/test sub-windows of a long IS period. For one such pair indexed by bb, (Ical,b,Itest,b)(I\_{\mathrm{cal},b},I\_{\mathrm{test},b}) of corresponding sample covariance matrices (𝚺^cal,b,𝚺^test,b)(\hat{\boldsymbol{\Sigma}}\_{\mathrm{cal},b},\hat{\boldsymbol{\Sigma}}\_{\mathrm{test},b}), one computes the vector of Oracle eigenvalues:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝀^O,b=Diag​(𝑽^cal,b⊤​𝚺^test,b​𝑽^cal,b),\hat{\boldsymbol{\lambda}}\_{\mathrm{O,b}}=\mathrm{Diag}\left(\hat{\boldsymbol{V}}\_{\mathrm{cal},b}^{\top}\hat{\boldsymbol{\Sigma}}\_{\mathrm{test},b}\hat{\boldsymbol{V}}\_{\mathrm{cal},b}\right), |  | (7) |

where V^cal\hat{V}\_{\mathrm{cal}} is the eigenvector matrix of Σ^cal\hat{\Sigma}\_{\mathrm{cal}}. This choice corresponds to the optimal rotationally invariant shrinkage of Σ^cal\hat{\Sigma}\_{\mathrm{cal}} for predicting Σ^test\hat{\Sigma}\_{\mathrm{test}} (Ledoit and
Péché, [2011](https://arxiv.org/html/2511.10478v1#bib.bib11)). 111This result stems from minimizing the Frobenius norm ‖𝚺next−𝚵​(𝚺next)‖F||\boldsymbol{\Sigma}\_{\mathrm{next}}-\boldsymbol{\Xi}(\boldsymbol{\Sigma}\_{\mathrm{next}})||\_{\mathrm{F}}.
The Average Oracle eigenvalues are then obtained as rank-wise averages of calibrated oracle eigenvalues: having computed B≫1B\gg 1 oracle eigenvalues:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝀^AO=1B​∑b=1B𝝀^O,b.\hat{\boldsymbol{\lambda}}\_{\mathrm{AO}}=\frac{1}{B}\sum\_{b=1}^{B}\hat{\boldsymbol{\lambda}}\_{\mathrm{O,b}}. |  | (8) |

To avoid look-ahead bias, only oracles computed in the strict past of each evaluation date are included in the averaging. The resulting shrinkage operator is thus:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚵^AO​(𝚺^)=𝑽^​Diag ​(𝝀^AO)​𝑽^⊤.\hat{\boldsymbol{\Xi}}\_{\mathrm{AO}}(\hat{\boldsymbol{\Sigma}})=\hat{\boldsymbol{V}}\,\textrm{Diag }(\hat{\boldsymbol{\lambda}}\_{\mathrm{AO}})\,\hat{\boldsymbol{V}}^{\top}. |  | (9) |

AO has been shown to be an effective zeroth-order shrinkage estimator, outperforming state-of-the-art nonlinear shrinkage estimators in many time-varying settings, including large portfolios of equity data (Bongiorno et al., [2023](https://arxiv.org/html/2511.10478v1#bib.bib3); Bongiorno and Challet, [2024](https://arxiv.org/html/2511.10478v1#bib.bib2)). In addition, by removing entirely the noise of eigenvalues, it leads to much less time-varying portfolio weights.

#### Combined estimators (UPSA–AO, AvgUPSA–AO)

We use AO eigenvalues to filter all the covariance matrices used in UPSA: those defining ridge portfolios and those used within the cross-validation procedure. Note that AO filters the correlation matrices; the filtered covariance matrices are then reconstructed by rescaling with the original sample volatilities.
We call the estimator obtained through this procedure UPSA–AO. We expect the time-variation of the optimal ridge weights to be appreciably smaller than with UPSA alone.

The AvgUPSA–AO estimator combines both enhancements: AO pre-filtering of correlation matrices and the averaging of UPSA-AO weights across past windows.
In short, the AO step provides a robust noise reduction of correlation eigenvalues and some robustness to covariate shift prior to the UPSA stage, while the subsequent temporal averaging of UPSA weights further stabilizes the solution against fluctuations induced by grid discretization and sampling noise.

## 3 Empirical Results

### 3.1 Data

We use the same dataset as Kelly et al. ([2023](https://arxiv.org/html/2511.10478v1#bib.bib9)): monthly returns of 153 characteristic-managed portfolios of US equities between 1970 and 2024 from Jensen et al. ([2023](https://arxiv.org/html/2511.10478v1#bib.bib8)).222Data available at: <https://jkpfactors.com/> We consider five filtering schemes: UPSA, AvgUPSA, AO, UPSA-AO and AvgUPSA-AO. We define the OOS Sharpe ratio of a portfolio π\pi, held for 6 months, with realized returns and risk:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SR=𝝅⊤​𝝁^OOS𝝅⊤​𝚺^OOS​𝝅,\mathrm{SR}=\frac{\boldsymbol{\pi}^{\top}\hat{\boldsymbol{\mu}}\_{\mathrm{OOS}}}{\sqrt{\boldsymbol{\pi}^{\top}\hat{\boldsymbol{\Sigma}}\_{\mathrm{OOS}}\,\boldsymbol{\pi}}}, |  | (10) |

where 𝝁^OOS\hat{\boldsymbol{\mu}}\_{\text{OOS}} and 𝚺^OOS\hat{\boldsymbol{\Sigma}}\_{\text{OOS}} are respectively the realized mean vector and the realized covariance matrix over the 6-month period after calibration of π\pi. This definition of the Sharpe Ratio ensures a purely out-of-sample measurement of performance.

UPSA portfolios are computed using LOO CV; AvgUPSA adds an expanding-window mean of the optimized UPSA ridge weights. All of the Average Oracle eigenvalues use an exponentially weighted moving average of calibrated oracles with a half-life of 24 months. AO portfolios correspond to the efficient portfolios with AO-filtered correlation matrix (without UPSA). UPSA-AO and AvgUPSA-AO are obtained by pre-filtering all cross-sectional correlation matrices with AO eigenvalues, including the ones used during CV.

### 3.2 Penalization grid

We first choose the same ridge penalty grid as Kelly et al. ([2023](https://arxiv.org/html/2511.10478v1#bib.bib9)), which correspond to the left-most points in Figure [2](https://arxiv.org/html/2511.10478v1#S3.F2 "Figure 2 ‣ 3.2 Penalization grid ‣ 3 Empirical Results ‣ Noise-proofing Universal Portfolio Shrinkage"). All the AO-based filtering schemes over-perform vanilla UPSA and AvgUPSA in a statistically significant way.

![Refer to caption](x2.png)


Figure 2: Mean Annualized Sharpe ratio against the penalty grid lower bound, for portfolios of the different proposed estimators on JKP US characteristic factors monthly returns, 153 assets, in-sample window size T=120T=120M. Portfolios are rebalanced every month over the period 1985–2024. The realized OOS Sharpe Ratio is computed as the realized return over the 6 months divided by its realized volatility.

Kelly et al. ([2023](https://arxiv.org/html/2511.10478v1#bib.bib9)) recommend to use a grid that contains all the sample non-zero eigenvalues, which range from 10−710^{-7} to 10−110^{-1} in the considered data set. We found indeed that the grid upper bound does not significantly affect the results provided that it is larger than the largest sample eigenvalue. However, the influence of the grid lower bound on UPSA and AvgUPSA performance is far from negligible. Figure [2](https://arxiv.org/html/2511.10478v1#S3.F2 "Figure 2 ‣ 3.2 Penalization grid ‣ 3 Empirical Results ‣ Noise-proofing Universal Portfolio Shrinkage") reports the OOS Sharpe ratio as a function of the grid lower bound. While the AO-based methods are only weakly sensitive to this choice, UPSA and AvgUPSA are much improved once the lower bound impose larger minimal penalization. However, setting the grid lower bound to 10−410^{-4} is unsatisfactory in principle, as this value roughly corresponds to the mean of the empirical eigenvalue distribution. If the eigenvalues did not require any shrinkage, such a choice would therefore enforce an unnecessarily strong penalization, leading to suboptimal portfolios.

The sharp performance drop observed for AO-based estimators when the grid lower bound increases further is a direct consequence of this effect: because AO pre-filtering already compresses the smallest eigenvalues, imposing an excessively high minimal ridge penalty results in an over-shrunk covariance spectrum.
In other words, the additional penalization acts on already filtered eigenvalues, effectively degrading precision rather than improving stability. Finally the large over-performance of UPSA-AO over UPSA is linked to the fact that the optimal ridge weights vary much less between two calibration windows (mean turnover of 0.35 vs 0.42, a highly significant difference) (see sec. [2.2](https://arxiv.org/html/2511.10478v1#S2.SS2 "2.2 Noise-proofing UPSA ‣ 2 Estimators ‣ Noise-proofing Universal Portfolio Shrinkage")).

### 3.3 Calibration window length

We investigate the mean performance of the considered estimators on the 1985–2024 period with respect to the IS calibration window size TT. We consider the same dataset as before and fix the ridge penalty grid to 20 logarithmically spaced points in [10−8,10−1][10^{-8},10^{-1}]. We run 13 experiments for TT varying between 33 and 1515 years. In each run, Oracles are calibrated using folds IcalI\_{\mathrm{cal}} and ItestI\_{\mathrm{test}} of respective sizes TT and TOOS=6T\_{\mathrm{OOS}}=6 months. We can observe a consistent over-performance of combined estimators UPSA-AO and AvgUPSA-AO over UPSA.

![Refer to caption](x3.png)


Figure 3: Mean Annualized Sharpe ratio against the in-sample window size, using JKP US factors monthly returns, with N=153N=153 assets and a penalty grid of 20 log-spaced points in [10−810^{-8}, 10−110^{-1}].

The historical Sharpe ratio performance on the period 1985–2024 can also be visualized as the cumulative log-returns in Fig. [4](https://arxiv.org/html/2511.10478v1#S3.F4 "Figure 4 ‣ 3.3 Calibration window length ‣ 3 Empirical Results ‣ Noise-proofing Universal Portfolio Shrinkage"). Portfolios are rebalanced every month, and their return is measured as the realized return over the following month. The resulting cumulative log-returns are rescaled using a centered 6-month rolling standard deviation, targeting an annualized volatility of 10%. The in-sample calibration window is set to T=120T=120 months.

![Refer to caption](x4.png)


Figure 4: Cumulative log-returns scaled by point-wise 66M centered rolling standard deviations to achieve 10%10\% annual volatility, on JKP US factors’ monthly returns with a fixed in-sample window size of T=120M, and a penalty grid of 20 log-spaced points in [10−810^{-8}, 10−1]10^{-1}]. The graph shows clear consistent historical over-performance of proposed AO-based estimators over UPSA.

### 3.4 Statistical analysis

Table [1](https://arxiv.org/html/2511.10478v1#S3.T1 "Table 1 ‣ 3.4 Statistical analysis ‣ 3 Empirical Results ‣ Noise-proofing Universal Portfolio Shrinkage") reports the main statistics of the maximum–Sharpe portfolios obtained from the five estimators applied to monthly factor returns over the period 1985–2024, using an in-sample calibration window of T=120T=120 months and a fixed grid of 20 logarithmically spaced penalty values between 10−810^{-8} and 10−110^{-1}.
All Sharpe ratios and associated statistical tests are computed from the out-of-sample Sharpe ratio defined in Eq. ([10](https://arxiv.org/html/2511.10478v1#S3.E10 "In 3.1 Data ‣ 3 Empirical Results ‣ Noise-proofing Universal Portfolio Shrinkage")).
The table displays, in order, the mean annualized Sharpe ratio, average diversification (inverse of the sum of squared portfolio weights), mean turnover, gross leverage, maximum monthly drawdown, and the outcomes of the statistical tests.

Using one-sided Wilcoxon signed-rank tests for performance comparisons, we find that the proposed AvgUPSA–AO estimator achieves the highest out-of-sample Sharpe ratio, outperforming all others, including the second best. UPSA–AO, with a pp–value of 0.0120.012.
It is also superior to the other estimators in all criteria except for the maximum drawdown.
In contrast, AvgUPSA is found to perform slightly worse than UPSA under this configuration, though this difference is not statistically significant (pp–value equal to 0.38).
However, for alternative penalty grids with higher lower bounds, AvgUPSA outperforms UPSA. In fact AvgUPSA is consistently better than UPSA when considering monthly rebalancing of the portfolios and for every penalty grid, as can be observed in Figure [4](https://arxiv.org/html/2511.10478v1#S3.F4 "Figure 4 ‣ 3.3 Calibration window length ‣ 3 Empirical Results ‣ Noise-proofing Universal Portfolio Shrinkage").

To ensure robustness in the statistical assessment, we further apply the Model Confidence Set (MCS) procedure (Hansen et al., [2011](https://arxiv.org/html/2511.10478v1#bib.bib7)), which identifies the subset of estimators that are statistically indistinguishable from the best-performing one, using the negative out-of-sample Sharpe ratio as loss function.
The MCS results confirm that both UPSA–AO and AvgUPSA–AO belong to the superior set of models (test size of 0.050.05). , confirming their advantage over the other estimators.

In summary, the AvgUPSA–AO estimator demonstrates a statistically significant and robust improvement over all alternatives.
Its performance gains stem from the combination of the AO pre-filtering, which stabilizes correlation estimation, and the averaging of optimized weights. Quite notably, it is better than either UPSA or AO of their own.

| Key statistics / Estimators | UPSA | AvgUPSA | AO | UPSA-AO | AvgUPSA-AO |
| --- | --- | --- | --- | --- | --- |
| Mean Annualized Sharpe | 2.077 | 2.061 | 2.267 | 2.462 | 2.493 |
| Mean Diversification | 6.7 | 3.8 | 6.1 | 16.4 | 17.7 |
| Mean Turnover | 1.71 | 1.27 | 0.67 | 0.31 | 0.25 |
| Mean Gross Leverage | 5.38 | 6.01 | 4.18 | 2.50 | 2.32 |
| Max Drawdown | -2.66 | -4.64 | -2.36 | -2.65 | -2.73 |
| Wilcoxon p-value (Est - UPSA) | / | 3.8e-01 | 5.31e-03 | 2.1e-10 | 3.1e-11 |
| Wilcoxon p-value (AvgUPSA-AO - Est) | 3.1e-11 | 2.8e-10 | 8.1e-05 | 1.2e-02 | / |
| MCS included (size 0.05) | No | No | No | Yes | Yes |

Table 1: Key statistics of efficient Max Sharpe portfolios estimated on monthly factor returns over the 1985–2024 period.
Reported quantities are, from top to bottom: mean annualized Sharpe ratio as computed in Eq. [10](https://arxiv.org/html/2511.10478v1#S3.E10 "In 3.1 Data ‣ 3 Empirical Results ‣ Noise-proofing Universal Portfolio Shrinkage"), average diversification (inverse sum of squared weights), mean portfolio turnover, gross leverage, and maximum monthly drawdown.
The last three rows show one-sided Wilcoxon signed-rank tests comparing Sharpe ratios of estimators vs. UPSA, AvgUPSA-AO vs. estimators and the Model Confidence Set (MCS) inclusion at 5% test size.
  
Portfolios are optimized with an in-sample window size of T=120T=120 months.
The ridge penalty grid contains 20 logarithmically spaced values in [10−8,10−1][10^{-8},10^{-1}].

## 4 Conclusion

Despite its undeniable filtering abilities, UPSA suffers from too much noise and a strong dependence on the choice of penalty grid. Filtering noise further increases the abilities of UPSA.
First, using long time averages of past optimal ridge weights improves the performance of UPSA for well chosen grids.
Second, pre-filtering covariance matrices with Average Oracle provides a strong baseline, effectively stabilizing covariance estimates and accounting partly for covariate shift before the UPSA refinement.
Finally, compounding averaging and AO filtering yields the novel estimator AvgUPSA-AO that inherits the regularization benefits of both approaches and outperforms statistically significantly all other tested methods across most settings.

From a broader perspective, the UPSA part of AvgUPSA-AO acts as a first-order improvement over AO, a zeroth-order nonlinear filtering method. This opens the question of using the UPSA technique to optimize the optimal oracle values directly, as well as using adaptive grid bounds. Other future directions include exploring new parametrized families of covariance filtering, such as the James–Stein shrinkage for eigenvectors by Goldberg and Kercheval ([2023](https://arxiv.org/html/2511.10478v1#bib.bib6)).

## Acknowledgments

P.R. acknowledges funding from ANRT, under the CIFRE contract nr 2025/0279.

This publication used HPC resources from the “Mésocentre” computing center of CentraleSupélec and École Normale
Supérieure Paris-Saclay supported by CNRS and Région Île-de-France.

## References

* Arlot and Celisse (2010)

  Sylvain Arlot and Alain Celisse.
  A survey of cross-validation procedures for model selection.
  *Statistics Surveys*, 4(none):40 – 79,
  2010.
  doi: 10.1214/09-SS054.
* Bongiorno and Challet (2024)

  Christian Bongiorno and Damien Challet.
  Covariance matrix filtering and portfolio optimisation: the average
  oracle vs non-linear shrinkage and all the variants of DCC-NLS.
  *Quantitative Finance*, 24(9):1227–1234,
  2024.
* Bongiorno et al. (2023)

  Christian Bongiorno, Damien Challet, and Grégoire Loeper.
  Filtering time-dependent covariance matrices using time-independent
  eigenvalues.
  *Journal of Statistical Mechanics: Theory and Experiment*,
  2023(2):023402, 2023.
* Bun et al. (2017)

  Joël Bun, Jean-Philippe Bouchaud, and Marc Potters.
  Cleaning large correlation matrices: tools from random matrix theory.
  *Physics Reports*, 666:1–109, 2017.
* Cawley and Talbot (2010)

  Gavin Cawley and Nicola Talbot.
  On over-fitting in model selection and subsequent selection bias in
  performance evaluation.
  *Journal of Machine Learning Research*, 11:2079–2107,
  07 2010.
* Goldberg and Kercheval (2023)

  Lisa R. Goldberg and Alec N. Kercheval.
  James–Stein for the leading eigenvector.
  *Proceedings of the National Academy of Sciences*, 120(2):e2207046120, 2023.
  doi: 10.1073/pnas.2207046120.
* Hansen et al. (2011)

  Peter R. Hansen, Asger Lunde, and James M. Nason.
  The model confidence set.
  *Econometrica*, 79(2):453–497, 2011.
  doi: https://doi.org/10.3982/ECTA5771.
* Jensen et al. (2023)

  Theis Jensen, Bryan Kelly, and Lasse Pedersen.
  Is there a replication crisis in finance?
  *The Journal of Finance*, 78:2465–2518, 06 2023.
  doi: 10.1111/jofi.13249.
* Kelly et al. (2023)

  Bryan T Kelly, Semyon Malamud, Mohammad Pourmohammadi, and Fabio Trojani.
  Universal portfolio shrinkage.
  Working Paper 32004, National Bureau of Economic Research, December
  2023.
* Lamrani et al. (2025)

  Lamia Lamrani, Christian Bongiorno, and Marc Potters.
  Optimal data splitting for holdout cross-validation in large
  covariance matrix estimation.
  *arXiv preprint arXiv:2503.15186*, 2025.
* Ledoit and
  Péché (2011)

  Olivier Ledoit and Sandrine Péché.
  Eigenvectors of some large sample covariance matrix ensembles.
  *Probability Theory and Related Fields*, 151(1):233–264, 2011.
* Markowitz (1952)

  Harry Markowitz.
  Portfolio selection.
  *The Journal of Finance*, 7(1):77–91, 1952.
  ISSN 00221082, 15406261.
* Michaud (1989)

  Richard O Michaud.
  The Markowitz optimization enigma: Is ‘optimized’optimal?
  *Financial Analysts Journal*, 45(1):31–42, 1989.
* Sleuwaegen et al. (1989)

  Leo E Sleuwaegen, Raymond R De Bondt, and Wim V Dehandschutter.
  The Herfindahl index and concentration ratios revisited.
  *Antitrust Bull.*, 34:625, 1989.