---
authors:
- Rupendra Yadav
- Amita Sharma
- Aparna Mehra
doc_id: arxiv:2601.20643v1
family_id: arxiv:2601.20643
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency
  Across Market Dimensions'
url_abs: http://arxiv.org/abs/2601.20643v1
url_html: https://arxiv.org/html/2601.20643v1
venue: arXiv q-fin
version: 1
year: 2026
---


Rupendra Yadava, Amita Sharmab, Aparna Mehraa
Department of Mathematics, Indian Institute of Technology Delhi, Hauz Khas, New Delhi - 110016, India
Department of Mathematics, Netaji Subhash University of Technology, Dwarka Sec 3, New Delhi -110078, India

###### Abstract

The mean-variance model remains the most prevalent investment framework, built on diversification principles. However, it consistently struggles with estimation errors in expected returns and the covariance matrix, its core parameters. To address this concern, this research evaluates the performance of mean-variance (MV) and global minimum-variance (GMV) models across various shrinkage estimators designed to improve these parameters. Specifically, we examine five shrinkage estimators for expected returns and eleven for the covariance matrix.
To compare multiple portfolios, we employ a super-efficient data envelopment analysis model to rank the portfolios according to investors’ risk-return preferences. Our comprehensive empirical investigation utilizes six real-world datasets with different dimensional characteristics, applying a rolling window methodology across three out-of-sample testing periods. Following the ranking process, we examine the chosen shrinkage-based MV or GMV portfolios against five traditional portfolio optimization techniques—classical MV and GMV for sample estimates, MiniMax, conditional value-at-risk, and semi-mean absolute deviation risk measures. Our empirical findings reveal that, in most scenarios, the GMV model combined with the Ledoit-Wolf two-parameter shrinkage covariance estimator (COV2) represents the optimal selection for a broad spectrum of investors. Meanwhile, the MV model utilizing COV2 alongside the sample mean (SM) proves more suitable for return-oriented investors. These two identified models demonstrate superior performance compared to traditional benchmark approaches. Overall, this study lays the groundwork for a more comprehensive understanding of how specific shrinkage models perform across diverse investor profiles and market setups.

###### keywords:

Mean-Variance model, Global Mean-Variance model , Shrinkage estimators , Mean and covariance matrices , Data Envelopment Analysis

††journal: abc

Highlights

* 1.

  Deliver empirical evidence on the practical value and benefits of shrinkage estimators in portfolio selection.
* 2.

  Integrates shrinkage estimators into mean-variance and global minimum-variance optimization frameworks.
* 3.

  Evaluate the effectiveness of shrinkage estimators across diverse low- and high-dimensional emerging and developed financial markets.
* 4.

  Employing a super-efficiency DEA model to rank the shrinkage-based optimal portfolios.
* 5.

  Observed that the two-parameter shrinkage covariance estimator outperforms other benchmark models.

## 1 Introduction

### 1.1 Motivation and Background

Since its introduction, modern portfolio theory (MPT) [[27](https://arxiv.org/html/2601.20643v1#bib.bib21 "PORTFOLIO selection")] has been a cornerstone of quantitative finance, providing a formal framework for creating portfolios that balance the trade-off between mean return and risk. A core of MPT is diversification, which aims to reduce overall portfolio risk.
However, recent global financial stresses have highlighted flaws in conventional portfolio models, especially those that rely on assumptions of stable return distributions and fail to account for severe market events. During periods of high uncertainty, the relationship between return and risk can become distorted, challenging the reliability of the standard Markowitz mean-variance framework.

A persistent challenge in implementing Mean-Variance Optimization (MVO) is the difficulty in accurately estimating mean returns and the covariance matrix of asset returns [[11](https://arxiv.org/html/2601.20643v1#bib.bib14 "The effect of errors in means, variances, and covariances on optimal portfolio choice")]. Errors in these estimations can significantly distort portfolio weights, often leading to illogical or overly concentrated allocations. Furthermore, in practice, institutional or regulatory rules often prohibit short selling, requiring new models that can incorporate these limitations while still ensuring adequate diversification.

The mean-variance optimization (MVO) framework has several documented shortcomings. MVO portfolios frequently deliver worse performance than simpler strategies like equal weighting [[12](https://arxiv.org/html/2601.20643v1#bib.bib22 "Optimal versus naive diversification: how inefficient is the 1/n portfolio strategy?"), [17](https://arxiv.org/html/2601.20643v1#bib.bib23 "Putting markowitz theory to work")] and often demonstrate poor diversification [[14](https://arxiv.org/html/2601.20643v1#bib.bib24 "When will mean-variance efficient portfolios be well diversified?")]. A core issue, as noted by Michaud [[29](https://arxiv.org/html/2601.20643v1#bib.bib25 "Efficient asset management: a practical guide to stock portfolio optimization and asset allocation")], is that the mean-variance optimizer is overly sensitive to inaccuracies in the input estimates, resulting in unstable and difficult-to-interpret results.
Furthermore, MVO typically relies on deterministic point estimates for means and covariances. This methodology fails to account for the inherent uncertainty in estimating these parameters, which can consequently produce unreliable asset allocations.

The global minimum variance (GMV) model, which ignores mean estimation errors, is one approach to reducing estimation errors in the mean-variance (MV) model. This is because it is generally accepted that estimation error in the mean is more significant than that resulting from covariance terms [[11](https://arxiv.org/html/2601.20643v1#bib.bib14 "The effect of errors in means, variances, and covariances on optimal portfolio choice"), [4](https://arxiv.org/html/2601.20643v1#bib.bib65 "On the sensitivity of mean-variance-efficient portfolios to changes in asset means: some analytical and computational results")]. Even though GMV approach is straightforward, it still faces issues, particularly when return distributions have heavy tails, which can lead to significant estimation errors in the covariance as well [[28](https://arxiv.org/html/2601.20643v1#bib.bib66 "Asset allocation and risk management")].

Alternatively, researchers impose a weight norm constraint [[12](https://arxiv.org/html/2601.20643v1#bib.bib22 "Optimal versus naive diversification: how inefficient is the 1/n portfolio strategy?")] in the MV model or explore translating it into its robust version by defining uncertainty sets for the mean vector and covariance matrix [[26](https://arxiv.org/html/2601.20643v1#bib.bib67 "Sparse and robust portfolio selection via semi-definite relaxation")]. While robust optimization provides a formal way to address input uncertainty, it is not without criticism. Scherer [[32](https://arxiv.org/html/2601.20643v1#bib.bib41 "Can robust portfolio optimisation help to build better portfolios?")] argues that robust framework often behaves similarly to applying shrinkage to input estimates and, in some cases, may even result in poorer out-of-sample performance. This critique has reinforced interest in directly improving estimation techniques, particularly in high-dimensional settings where classical estimators become unstable due to the ‘curse of dimensionality’ [[3](https://arxiv.org/html/2601.20643v1#bib.bib50 "Spectral analysis of large dimensional random matrices"), [5](https://arxiv.org/html/2601.20643v1#bib.bib61 "Testing for independence of large dimensional vectors")].

Shrinkage estimators have shown particular promise in addressing this issue. By blending sample estimates with structured priors, they produce more reliable and stable inputs for the MV model, especially when the number of assets exceeds the number of observations. This stability is crucial for high-dimensional portfolios, for example, the S&P 500 or the RUSSELL 1000 market indices, where minor estimation errors can lead to significant performance deterioration.

Several shrinkage estimators for the population mean and population covariance matrix are available in the literature. For the population mean, notable contributions include the James-Stein shrinkage estimator (JS) [[16](https://arxiv.org/html/2601.20643v1#bib.bib4 "Estimation with quadratic loss")] that improves multivariate mean estimation by shrinking sample estimates toward a common value, excelling in high-dimensional settings. Building on this, Jorion’s Bayes-Stein shrinkage estimator (BS) [[18](https://arxiv.org/html/2601.20643v1#bib.bib3 "Bayes-Stein estimation for portfolio analysis")] incorporates a Bayesian framework, adapting shrinkage based on prior information, which enhances mean estimation, particularly in financial contexts. The quadratic shrinkage estimator (QUAD) [[36](https://arxiv.org/html/2601.20643v1#bib.bib6 "Non-parametric shrinkage mean estimation for quadratic loss functions with unknown covariance matrices")] further refines the shrinkage process by applying a quadratic shrinkage function. Following this, Bodnar et al. [[8](https://arxiv.org/html/2601.20643v1#bib.bib5 "Optimal shrinkage estimator for high-dimensional mean vector")] introduced the Bodnar optimal linear shrinkage estimator (BOP), which optimizes linear shrinkage to minimize the mean squared error, offering asymptotically stable and accurate results in true mean estimation.

In parallel, the literature on shrinkage estimators for covariance matrices was advanced by Ledoit and Wolf [[19](https://arxiv.org/html/2601.20643v1#bib.bib11 "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection"), [20](https://arxiv.org/html/2601.20643v1#bib.bib12 "A well-conditioned estimator for large-dimensional covariance matrices")] for the development of linear shrinkage estimators for large covariance matrices, introducing a computationally efficient and robust approach that improves estimation accuracy in high-dimensional settings by shrinking the sample covariance matrix toward a structured target. The work of Bodnar et al. [[7](https://arxiv.org/html/2601.20643v1#bib.bib7 "On the strong convergence of the optimal linear shrinkage estimator for large dimensional covariance matrix")] presents the construction of an optimal linear shrinkage estimator (OLSE) for the covariance matrix, which is shown to asymptotically minimize the Frobenius loss with almost sure convergence.

Building on their earlier work, Ledoit and Wolf [[21](https://arxiv.org/html/2601.20643v1#bib.bib42 "Nonlinear shrinkage estimation of large-dimensional covariance matrices"), [22](https://arxiv.org/html/2601.20643v1#bib.bib43 "Spectrum estimation: a unified framework for covariance matrix estimation and PCA in large dimensions")] introduced a nonlinear shrinkage estimator using an indirect approach that recovers the population eigenvalues of the covariance matrix, achieving more precise and adaptive shrinkage, particularly when the sample size is small relative to the number of assets.
In a further advancement, Ledoit and Wolf [[23](https://arxiv.org/html/2601.20643v1#bib.bib9 "Analytical nonlinear shrinkage of large-dimensional covariance matrices")] proposed a nonlinear shrinkage technique that incorporates the Hilbert transform, which induces shrinkage by pulling nearby eigenvalues together—making the shrinkage a local phenomenon and introducing essential nonlinearity into the estimation process.
In recent times, Ledoit and Wolf [[24](https://arxiv.org/html/2601.20643v1#bib.bib10 "Shrinkage estimation of large covariance matrices: keep it simple, statistician?"), [25](https://arxiv.org/html/2601.20643v1#bib.bib8 "Quadratic shrinkage for large covariance matrices")] developed an estimation technique that retains the eigenvectors of the sample covariance matrix but applies shrinkage to the inverse eigenvalues. This approach employs a quadratic shrinkage formula that involves two targets weighted by functions of the concentration ratio, enabling more refined covariance estimation in high-dimensional settings. An example of practical implementation in this domain is the HDShOP framework proposed by Bodnar et al. [[6](https://arxiv.org/html/2601.20643v1#bib.bib68 "High-dimensional portfolio selection with HDShOP package")], which combines theoretical and empirical tools for high-dimensional shrinkage-based portfolio construction in R. Very recently, Tran et al. [[30](https://arxiv.org/html/2601.20643v1#bib.bib2 "Enhancing portfolio optimization in emerging markets: a cross-validation multi-target shrinkage approach")] introduced a multi-target shrinkage estimator, utilizing a grid search-based cross-validation method to determine optimal shrinkage intensities. Their approach demonstrated improved risk-adjusted returns and reduced volatility when tested on the Vietnamese stock market data during a stable financial period.

These developments underline the growing importance of combining robust statistical techniques with modern data and theory to overcome the limitations of classical MV portfolios.

### 1.2 Objective and Approach

Objective: Given the theoretical underpinning and financial advantages of shrinkage estimators, this study seeks to examine and analyze MV and GMV models applying various shrinkage estimators of their model parameters, mean, and covariance matrix. We examine five shrinkage estimators for the mean and eleven for the covariance on six global markets, three of which are high-dimensional, (p>n)(p>n). The analysis employs a rolling window approach, using daily data that spans approximately eleven years for each market. Only eight covariance estimators have been found to be applicable in high-dimensional markets. Thus, there are sixty-six portfolios for the datasets where n>pn>p, and forty-eight when n<pn<p. This study also analyzes three out-of-sample window sizes: 3-months, 6-months, and 1-year, within the rolling window framework. Additionally, we categorize three groups: A, B, and C, based on the return-risk profile of investors, and perform a comprehensive analysis across groups.

Overall, we conduct extensive empirical analysis to examine the advantages and performance of shrinkage estimators in portfolio selection.

Sample Data: Daily closing prices of the constituents from the six global markets, namely, Dow Jones 30 (DJ 30), NIFTY 50, FTSE 100, S&P 500, RUSSELL 1000, and TOPIX 1500, with the sample period of nearly 11 years from September 20, 2012, to Jun 6, 2024.

Execution: Three of the six datasets, S&P 500, RUSSELL 1000, and TOPIX 1500, are in the high-dimensional regime. In total, 48 MV and GMV-based portfolios are evaluated for high-dimensional datasets. For smaller-sized markets, DJ 30, NIFTY 50, and FTSE 100 (n>pn>p), we solve 66 MV and GMV models.

For the model computations, a rolling window scheme is executed for the in-sample (training) period of one year, and for the three different out-of-sample (testing) periods: (a) 3-months, (b) 6-months, and (c) 1-year.

For comprehensive analysis, we consider three groups: A, B, and C, based on the risk-return profile of investors. The groups consist of investors focused on balancing return and risk metrics (Group A), aggressive investors prioritizing return and reward-risk ratios (Group B), and conservative risk-averse investors emphasizing risk mitigation (Group C).

We suggest utilizing a super-efficiency data envelopment analysis (DEA) model with portfolios as decision-making units (DMUs). The input and output for the DEA model are the various financial metrics, categorized by the three groups, and calculated over each out-of-sample period’s return data.

Identifying Best Shrinkage Portfolio: For every market, for every group, and for each out-of-sample period, we arrange the portfolio efficiency scores in descending order and determine the top 10 portfolios.
Subsequently, we select the two optimal portfolios by two approaches: (i) the market best performer and (ii) the universal best performer. A market best-performer identifies the top performers according to the underlying market, while a universally best performer endeavors to find the portfolio that excels across the widest range of markets.

The market’s top performance is the one that rates among the top 10 throughout all three out-of-sample periods and possesses the highest geometric mean of the three efficiency ratings. The universal top performer is the portfolio that excels in the highest number of markets.

Comparative Analysis—The set of market best performers and universally best performer portfolios for each category is compared with five traditional portfolio optimization models: the semi mean-absolute deviation (SMAD) model [[13](https://arxiv.org/html/2601.20643v1#bib.bib62 "A reformulation of a mean-absolute deviation portfolio optimization model.")], which builds upon the mean absolute deviation model [[15](https://arxiv.org/html/2601.20643v1#bib.bib1 "Mean-absolute deviation portfolio optimization model and its applications to Tokyo stock market")]; the conditional value-at-risk model [[31](https://arxiv.org/html/2601.20643v1#bib.bib63 "Optimization of conditional value-at-risk")]; the MiniMax model [[9](https://arxiv.org/html/2601.20643v1#bib.bib64 "Portfolio optimization under a minimax rule")]; and the classical mean-variance (MV) and global minimum variance (GMV) models that utilize the sample mean and covariance matrix. This comparative analysis relies on out-of-sample results for financial metrics and DEA super efficiency scores.

Outcome: The numerical study reveals multiple intriguing facts: (1) The choice of shrinkage estimators is more dependent on underlying market data, the choice is even more prudent for return-seeking investors, therefore, there is no single shrinkage estimator, which works well for all the markets and for all the types of investors. (2) When seeking the majority of occasions, the GMV model with Ledoit Wolf method of two parameter shrinkage covariance (COV2) is an optimal choice for wide range of investors while the MV model with COV2 together with sample mean (SM) is more appropriate for return-seeking investors. (3) Both the GMV+COV2 and COV2+SM models perform better than traditional benchmarks like classical Markowitz portfolios with sample estimates, MiniMax, CVaR, GMV, and SMAD. (4) The shrinkage covariance (COV2) frequently appears in top choices for several instances, the sample mean (SM) shines in the mean estimation category. (5) The sample mean together with the sample covariance results to poor out-of-sample results, rendering it an undesirable option.

Broadly, this study lays the groundwork for a more in-depth comprehension of how certain shrinkage models perform for a variety of investors and in various market scenarios.

Structure: The paper is organized as follows. Section [2](https://arxiv.org/html/2601.20643v1#S2 "2 Mean-Variance and Global Minimum-Variance Portfolio Optimization Models ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") presents the mean-variance and global minimum-variance portfolio optimization models. Section [3](https://arxiv.org/html/2601.20643v1#S3 "3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") describes shrinkage estimators for the mean and covariance matrix. Section [4](https://arxiv.org/html/2601.20643v1#S4 "4 Super-efficiency DEA Model ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") outlines the DEA super-efficiency model. Section [5](https://arxiv.org/html/2601.20643v1#S5 "5 Data and Empirical Set-up ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") explains the data and empirical setup. Section [6](https://arxiv.org/html/2601.20643v1#S6 "6 Result Discussion ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") presents the results and discussion. Section [7](https://arxiv.org/html/2601.20643v1#S7 "7 Comparison with Benchmark Models ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") offers a comparison with benchmark models. Finally, Section [8](https://arxiv.org/html/2601.20643v1#S8 "8 Conclusions ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") concludes by presenting our findings and outlining future research directions.

## 2 Mean-Variance and Global Minimum-Variance Portfolio Optimization Models

Let 𝒙\bm{x} represent a portfolio composed of pp assets, denoted as 𝒙=(x1,…,xp)′\bm{x}=(x\_{1},\dots,x\_{p})^{{}^{\prime}}, where xix\_{i} is a decision variable indicating the proportion of the total capital allocated to the ii-th asset, for i=1,…,pi=1,\dots,p. For rir\_{i} be the random
return of the iith asset, the random vectors R=(r1,…,rp)R=(r\_{1},\ldots,r\_{p}) represent the random return vectors of pp-assets
portfolio. We
then calculate the return of a portfolio xx as Rx=∑i=1pri​xiR\_{x}=\sum\_{i=1}^{p}r\_{i}x\_{i}. For E​(ri)=μi​i=1,…,pE(r\_{i})=\mu\_{i}\;i=1,\ldots,p, the respective mean vector 𝝁\bm{\mu} and covariance matrix Σ\Sigma of a portfolio xx is expressed as 𝝁=(μ1,…,μp)\bm{\mu}=(\mu\_{1},\ldots,\mu\_{p}) and Σ=[σi​k]p×p\Sigma=[\sigma\_{ik}]\_{p\times p} where σi​k=covariance​(ri,rk),i,k=1,…,p\sigma\_{ik}=\textrm{covariance}(r\_{i},r\_{k}),\;i,\,k=1,\ldots,p. For a given set of admissible
portfolios, X={(x1,…,xp)′,∑i=1pxi=1,xi≥0,i=1,…,p}X=\{(x\_{1},\ldots,x\_{p})^{{}^{\prime}},\;\;\sum\_{i=1}^{p}x\_{i}=1,\;x\_{i}\geq 0,\;i=1,\ldots,p\}, where the nonnegativity constraints
xi≥0x\_{i}\geq 0 prohibit short-selling. The mean-variance (MV) model is given by the following convex quadratic program.

|  |  |  |  |
| --- | --- | --- | --- |
|  | (MV)min𝒙∈X\displaystyle\text{(MV)}\quad\min\_{\bm{x}\in X}\quad | 𝒙⊤​𝝁−γ​𝒙⊤​𝚺​𝒙,\displaystyle\bm{x}^{\top}\bm{\mu}-\gamma\bm{x}^{\top}\bm{\Sigma}\bm{x}, |  |

where γ>0\gamma>0 is a risk aversion parameter, varying it yields many efficient portfolios, each corresponding to a different risk-return profile of an investor. The global minimum-variance model is described by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (GMV)min𝒙∈X\displaystyle\text{(GMV)}\quad\min\_{\bm{x}\in X}\quad | 𝒙⊤​𝚺​𝒙.\displaystyle\bm{x}^{\top}\bm{\Sigma}\bm{x}. |  |

Traditionally, while solving the models (MV) or (GMV), the unknown parameters 𝝁\bm{\mu} and 𝚺\bm{\Sigma} are replaced by
their sample estimations using historical data or simulated data (or some empirical distribution such as uniform distribution). This results in unstable and non-robust portfolio weights. Shrinkage estimation emerges as a robust statistical tool that addresses these issues by systematically combining sample estimates with structured targets.
Shrinkage methods are based on the principle of trade-off between observed, data-driven estimates and a chosen target (often with desirable properties such as stability or sparsity) to minimize mean squared error.

## 3 Shrinkage Estimators

Shrinkage method is a linear combination of the sample
estimator of an underlying parameter and its another estimator. Formally, the shrinkage estimator for a parameter 𝜽\bm{\theta}, named 𝜽^s​h​r​i​n​k\hat{\bm{\theta}}\_{shrink}, can be expressed as:

|  |  |  |
| --- | --- | --- |
|  | 𝜽^s​h​r​i​n​k=λ​𝜽^t​a​r​g​e​t+(1−λ)​𝜽^s​a​m​p​l​e,\hat{\bm{\theta}}\_{shrink}=\lambda\,\hat{\bm{\theta}}\_{target}+(1-\lambda)\,\hat{\bm{\theta}}\_{sample}, |  |

where 𝜽^s​a​m​p​l​e\hat{\bm{\theta}}\_{sample} and 𝜽^t​a​r​g​e​t\hat{\bm{\theta}}\_{target} respectively, are the unbiased sample and target estimators of 𝜽\bm{\theta} and λ∈[0,1]\lambda\in[0,1] is the shrinkage intensity parameter.

### 3.1 Shrinkage Estimator for Mean

Shrinkage approaches to blend the sample mean vector with a more stable reference/target vector, such as a constant vector or the grand mean vector. This reduces sensitivity to outliers and estimation noise, leading to more robust mean inputs for the MV optimization model. The following describes four types of the most popular shrinkage estimators for the mean vector.

* 1.

  The James-Stein shrinkage estimator (JS): Introduced by James and Stein [[16](https://arxiv.org/html/2601.20643v1#bib.bib4 "Estimation with quadratic loss")], it is a classical shrinkage approach that improves the estimation accuracy of the mean vector μ\mu by shrinking the sample mean vector 𝒓¯\bar{\bm{r}} towards a common target. The JS estimator for the mean return vector is given by

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝝁^J​S=α^​r^0​𝟏p+(1−α^)​𝒓¯,\hat{\bm{\mu}}\_{JS}=\hat{\alpha}\hat{r}\_{0}\bm{1}\_{p}+\left(1-\hat{\alpha}\right)\bar{\bm{r}}, |  | (1) |

  where 𝟏p\bm{1}\_{p} is a
  pp-dimensional vector of ones, α^\hat{\alpha} is the shrinkage intensity and r^0​𝟏p\hat{r}\_{0}\bm{1}\_{p} is the shrinkage target defined as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | r^0=𝒓¯⊤​𝑺n−1​𝟏p𝟏p⊤​𝑺n−1​𝟏p,\hat{r}\_{0}=\frac{\bar{\bm{r}}^{\top}\bm{S}\_{n}^{-1}\bm{1}\_{p}}{\bm{1}\_{p}^{\top}\bm{S}\_{n}^{-1}\bm{1}\_{p}}, |  | (2) |

  where 𝑺n\bm{S}\_{n} denotes the sample covariance computed using sample size of nn and the shrinkage intensity is defined as

  |  |  |  |
  | --- | --- | --- |
  |  | α^=min⁡(1,p−2n​(𝒓¯−r^0​𝟏p)⊤​𝑺n−1​(𝒓¯−r^0​𝟏p)).\hat{\alpha}=\min\left(1,\ \frac{p-2}{n(\bar{\bm{r}}-\hat{r}\_{0}\bm{1}\_{p})^{\top}\bm{S}\_{n}^{-1}(\bar{\bm{r}}-\hat{r}\_{0}\bm{1}\_{p})}\right). |  |
* 2.

  The Bayes-Stein shrinkage estimator (BS): Introduced in [[18](https://arxiv.org/html/2601.20643v1#bib.bib3 "Bayes-Stein estimation for portfolio analysis")], it arises from a Bayesian framework in which the true mean return vector is modelled as a random variable with a prior distribution. It represents a Bayesian improvement over the JS estimator by incorporating prior beliefs about the mean vector 𝝁\bm{\mu} and allowing a probabilistic interpretation of the shrinkage process. With the shrinkage target as given in equation ([2](https://arxiv.org/html/2601.20643v1#S3.E2 "In item 1. ‣ 3.1 Shrinkage Estimator for Mean ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions")), the shrinkage intensity in equation ([1](https://arxiv.org/html/2601.20643v1#S3.E1 "In item 1. ‣ 3.1 Shrinkage Estimator for Mean ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions")) for the BS estimator, is defined as:

  |  |  |  |
  | --- | --- | --- |
  |  | α^=p+2p+2+n​(𝒓¯−r^0​ 1p)⊤​𝑺n−1​(𝒓¯−r^0​ 1p)\hat{\alpha}=\frac{p+2}{p+2+n\left(\bar{\bm{r}}-\hat{r}\_{0}\,\bm{1}\_{p}\right)^{\top}\bm{S}\_{n}^{-1}\left(\bar{\bm{r}}-\hat{r}\_{0}\,\bm{1}\_{p}\right)} |  |
* 3.

  The Quadratic shrinkage estimator (QUAD): The QUAD estimator introduced by [[36](https://arxiv.org/html/2601.20643v1#bib.bib6 "Non-parametric shrinkage mean estimation for quadratic loss functions with unknown covariance matrices")], proposes a data-driven shrinkage approach designed to estimate mean vector 𝝁\bm{\mu} under quadratic loss functions with unknown covariance matrices. The estimator is defined as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝝁^Q​u​a​d=R2,n​R4,nR1,n+R2,n−R3,n​𝟏p+R1,n−R3,nR1,n+R2,n−R3,n​𝒓¯\hat{\bm{\mu}}\_{Quad}=\frac{R\_{2,n}R\_{4,n}}{R\_{1,n}+R\_{2,n}-R\_{3,n}}\mathbf{1}\_{p}+\frac{R\_{1,n}-R\_{3,n}}{R\_{1,n}+R\_{2,n}-R\_{3,n}}\,\bar{\bm{r}} |  | (3) |

  where the coefficients R1,n,R2,n,R3,n,R4,nR\_{1,n},R\_{2,n},R\_{3,n},R\_{4,n} are defined as follows:

  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | R1,n\displaystyle R\_{1,n} | =1p​(n−1)​∑i≠j𝑹i⊤​𝑺n+​𝑹j,\displaystyle=\frac{1}{p(n-1)}\sum\_{i\neq j}\bm{R}\_{i}^{\top}\bm{S}\_{n}^{+}\bm{R}\_{j}, | R2,n\displaystyle R\_{2,n} | =1n​p​(∑k=1n𝑹k⊤​𝑺n+​𝑹k−1n−1​∑i≠j𝑹i⊤​𝑺n+​𝑹j),\displaystyle=\frac{1}{np}\left(\sum\_{k=1}^{n}\bm{R}\_{k}^{\top}\bm{S}\_{n}^{+}\bm{R}\_{k}-\frac{1}{n-1}\sum\_{i\neq j}\bm{R}\_{i}^{\top}\bm{S}\_{n}^{+}\bm{R}\_{j}\right), |  |
  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | R3,n\displaystyle R\_{3,n} | =1n​ 1n⊤​𝑺n+​𝟏n​∑k=1n𝟏n⊤​𝑺n+​𝑹k,\displaystyle=\frac{1}{n\,\mathbf{1}\_{n}^{\top}\bm{S}\_{n}^{+}\mathbf{1}\_{n}}\sum\_{k=1}^{n}\mathbf{1}\_{n}^{\top}\bm{S}\_{n}^{+}\bm{R}\_{k}, | R4,n\displaystyle R\_{4,n} | =1p​(n−1)​ 1n⊤​𝑺n+​𝟏n​∑i≠j𝟏n⊤​𝑺n+​𝑹i​𝑹j⊤​𝑺n+​𝟏n.\displaystyle=\frac{1}{p(n-1)\,\mathbf{1}\_{n}^{\top}\bm{S}\_{n}^{+}\mathbf{1}\_{n}}\sum\_{i\neq j}\mathbf{1}\_{n}^{\top}\bm{S}\_{n}^{+}\bm{R}\_{i}\bm{R}\_{j}^{\top}\bm{S}\_{n}^{+}\mathbf{1}\_{n}. |  |

  where 𝑺n+\bm{S}\_{n}^{+} is denoted for the Moore-Penrose inverse of 𝑺n\bm{S}\_{n} and 𝑹\bm{R} is the return rate data matrix of size n×pn\times p.
* 4.

  The Bodnar optimal linear shrinkage estimator (BOP): The BOP estimator is introduced by [[8](https://arxiv.org/html/2601.20643v1#bib.bib5 "Optimal shrinkage estimator for high-dimensional mean vector")] and is given by

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝝁^B​O​P=α^​𝝁0+β^​𝒓¯.\hat{\bm{\mu}}\_{BOP}=\hat{\alpha}\,\bm{\mu}\_{0}+\hat{\beta}\,\bar{\bm{r}}. |  | (4) |

  The shrinkage coefficients α^\hat{\alpha} and β^\hat{\beta} are obtained by minimizing the quadratic loss, which are almost surely asymptotically equivalent to

  |  |  |  |
  | --- | --- | --- |
  |  | α^=(1−β^)​𝒓¯⊤​𝑺n−1​𝝁0𝝁0⊤​𝑺n−1​𝝁0,β^=(𝒓¯⊤​𝑺n−1​𝒓¯−c1−c)​𝝁0⊤​𝑺n−1​𝝁0−(𝒓¯⊤​𝑺n−1​𝝁0)2𝒓¯⊤​𝑺n−1​𝒓¯​𝝁0⊤​𝑺n−1​𝝁0−(𝒓¯⊤​𝑺n−1​𝝁0)2\hat{\alpha}=(1-\hat{\beta})\frac{\bar{\bm{r}}^{\top}\bm{S}\_{n}^{-1}\bm{\mu}\_{0}}{\bm{\mu}\_{0}^{\top}\bm{S}\_{n}^{-1}\bm{\mu}\_{0}},\quad\hat{\beta}=\frac{\left(\bar{\bm{r}}^{\top}\bm{S}\_{n}^{-1}\bar{\bm{r}}-\frac{c}{1-c}\right)\bm{\mu}\_{0}^{\top}\bm{S}\_{n}^{-1}\bm{\mu}\_{0}-\left(\bar{\bm{r}}^{\top}\bm{S}\_{n}^{-1}\bm{\mu}\_{0}\right)^{2}}{\bar{\bm{r}}^{\top}\bm{S}\_{n}^{-1}\bar{\bm{r}}\bm{\mu}\_{0}^{\top}\bm{S}\_{n}^{-1}\bm{\mu}\_{0}-\left(\bar{\bm{r}}^{\top}\bm{S}\_{n}^{-1}\bm{\mu}\_{0}\right)^{2}} |  |

  where c=p/nc=p/n is the concentration ratio. In this study predetermined shrinkage target 𝝁0\bm{\mu}\_{0} is taken as 𝝁0=nϵ−12​𝟏p\bm{\mu}\_{0}=n^{\frac{\epsilon-1}{2}}\mathbf{1}\_{p}, with ϵ∈(0,1)\epsilon\in(0,1). This estimator is shown to dominate other shrinkage methods in high-dimensional settings in terms of quadratic loss in both empirical and simulation studies [[8](https://arxiv.org/html/2601.20643v1#bib.bib5 "Optimal shrinkage estimator for high-dimensional mean vector")].

### 3.2 Shrinkage Estimators for Covariance Matrix

Shrinkage covariance estimation becomes an essential tool in variance-based portfolio optimization models, especially when historical data is limited relative to the number of assets. Even when the number of data points is close to the number of assets, the classical sample covariance matrix becomes singular and hence is not a consistent estimator of the population covariance matrix. In high-dimensional settings, the shrinkage estimator of covariance plays a critical role in enhancing risk-adjusted performance and mitigating the pitfalls of traditional sample estimators [[6](https://arxiv.org/html/2601.20643v1#bib.bib68 "High-dimensional portfolio selection with HDShOP package")]. Below are the shrinkage estimators given for the covariance matrix:

* 1.

  Bodnar Linear Shrinkage (LS):
  This estimator is proposed by Bodnar et al. [[7](https://arxiv.org/html/2601.20643v1#bib.bib7 "On the strong convergence of the optimal linear shrinkage estimator for large dimensional covariance matrix")] and derived by minimizing the following expected quadratic loss under the Frobenius norm:

  |  |  |  |
  | --- | --- | --- |
  |  | R​(𝚺L​S)=𝔼​(‖𝑺n−𝚺L​S‖F2),R(\bm{\Sigma}\_{LS})=\mathbb{E}\left(\left\|\bm{S}\_{n}-\bm{\Sigma}\_{LS}\right\|\_{F}^{2}\right), |  |

  where 𝚺L​S\bm{\Sigma}\_{LS} is a LS estimator for covariance matrix, and ∥⋅∥F\|\cdot\|\_{F} denotes the Frobenius norm. This approach yields an estimator that is a linear combination of the sample covariance matrix 𝑺n\bm{S}\_{n} and a predetermined target matrix 𝚺𝟎\bm{\Sigma\_{0}}. Further discussion on the selection of 𝚺𝟎\bm{\Sigma\_{0}} can be found in [[20](https://arxiv.org/html/2601.20643v1#bib.bib12 "A well-conditioned estimator for large-dimensional covariance matrices"), [2](https://arxiv.org/html/2601.20643v1#bib.bib15 "Estimating high dimensional covariance matrices and its applications.")].
  The LS estimator is derived from above as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝚺^L​S=α^​𝑺n+β^​𝚺0\widehat{\bm{\Sigma}}\_{LS}=\hat{\alpha}\,\bm{S}\_{n}+\hat{\beta}\,\bm{\Sigma}\_{0}\\ |  | (5) |

  where the shrinkage coefficients α^\hat{\alpha} and β^\hat{\beta} are computed as:

  |  |  |  |
  | --- | --- | --- |
  |  | α^=1−1n​‖𝑺n‖t​r2​‖𝚺0‖F2‖𝑺n‖F2​‖𝚺0‖F2−‖𝑺n​𝚺0‖t​r2,β^=‖𝑺n​𝚺0‖t​r‖𝚺0‖F2​(1−α^).\hat{\alpha}=1-\frac{1}{n}\frac{\|\bm{S}\_{n}\|\_{tr}^{2}\,\|\bm{\Sigma}\_{0}\|\_{F}^{2}}{\|\bm{S}\_{n}\|\_{F}^{2}\,\|\bm{\Sigma}\_{0}\|\_{F}^{2}-\|\bm{S}\_{n}\bm{\Sigma}\_{0}\|\_{tr}^{2}},\quad\hat{\beta}=\frac{\|\bm{S}\_{n}\bm{\Sigma}\_{0}\|\_{tr}}{\|\bm{\Sigma}\_{0}\|\_{F}^{2}}\left(1-\hat{\alpha}\right). |  |

  Here, ∥⋅∥tr\|\cdot\|\_{\mathrm{tr}} denotes the trace norm. By construction, the estimator satisfies α^≤1\hat{\alpha}\leq 1 and β^≥0\hat{\beta}\geq 0.
  The LS estimator incorporates prior structure through the target matrix 𝚺0\bm{\Sigma}\_{0}, which can enhance performance when prior information is informative. In this study, we take 𝚺0=1p​𝑰p\bm{\Sigma}\_{0}=\frac{1}{p}\bm{I}\_{p} [[7](https://arxiv.org/html/2601.20643v1#bib.bib7 "On the strong convergence of the optimal linear shrinkage estimator for large dimensional covariance matrix")].
* 2.

  Ledoit Wolf Method (LW): Ledoit and Wolf [[19](https://arxiv.org/html/2601.20643v1#bib.bib11 "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection"), [20](https://arxiv.org/html/2601.20643v1#bib.bib12 "A well-conditioned estimator for large-dimensional covariance matrices")] introduce a family of covariance shrinkage estimators that improve the performance of the sample covariance matrix by shrinking it toward well-conditioned, structured targets. These target matrices include the identity matrix, the combination of the identity matrix and a matrix of ones, the constant correlation matrix, the diagonal matrix of variances, and a single-factor market model, which are referred to as COV1, COV2, COVCOR, COVDIAG, and COVMKT, respectively.
  The LW shrinkage estimator is defined as:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝚺^L​W=λ^​𝑻+(1−λ^)​𝑺n,\widehat{\bm{\Sigma}}\_{LW}=\hat{\lambda}\bm{T}+(1-\hat{\lambda})\bm{S}\_{n}, |  | (6) |

  where, 𝑻\bm{T} is the target matrix. By minimizing the mean-squared error between the estimator and the true covariance matrix, the optimal shrinkage intensity is obtained as

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | λ^=min⁡(1,max⁡(0,π^−ρ^n​γ^)).\hat{\lambda}=\min\left(1,\max\left(0,\frac{\hat{\pi}-\hat{\rho}}{n\hat{\gamma}}\right)\right). |  | (7) |

  Here, π^\hat{\pi} and γ^\hat{\gamma} are given by:

  |  |  |  |
  | --- | --- | --- |
  |  | π^=∑i=1p∑j=1p((Sn(2))i​j−(Sn)i​j2),γ^=∑i=1p∑j=1p((Sn)i​j−Ti​j)2\hat{\pi}=\sum\_{i=1}^{p}\sum\_{j=1}^{p}\left((S\_{n}^{(2)})\_{ij}-(S\_{n})\_{ij}^{2}\right),\;\;\hat{\gamma}=\sum\_{i=1}^{p}\sum\_{j=1}^{p}\left((S\_{n})\_{ij}-T\_{ij}\right)^{2} |  |

  where the second-moment matrix is 𝑺n(2)=1n​(𝑹(2))⊤​𝑹(2),\bm{S}\_{n}^{(2)}=\frac{1}{n}(\bm{R}^{(2)})^{\top}\bm{R}^{(2)}, with (𝑹(2))i​j=𝑹i​j2(\bm{R}^{(2)})\_{ij}=\bm{R}\_{ij}^{2} and

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ρ^=ρ^diag+ρ^off,\hat{\rho}=\hat{\rho}\_{\mathrm{diag}}+\hat{\rho}\_{\mathrm{off}}, |  | (8) |

  with the diagonal contribution is specified as: ρ^diag=∑i=1p((Sn(2))i​i−(Sn)i​i2)\hat{\rho}\_{\mathrm{diag}}=\sum\_{i=1}^{p}\left((S\_{n}^{(2)})\_{ii}-(S\_{n})\_{ii}^{2}\right) while the off-diagonal component ρ^off\hat{\rho}\_{\mathrm{off}} varies from estimator to estimator.

  1. (2a)

     One-parameter shrinkage covariance estimator (COV1) [[19](https://arxiv.org/html/2601.20643v1#bib.bib11 "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection")]: This estimator sets 𝑻=v¯​𝑰p\bm{T}=\bar{v}\bm{I}\_{p}, where v¯=1p​trace​(𝑺n)\bar{v}=\frac{1}{p}\mathrm{trace}(\bm{S}\_{n}), and uses ρ^=0\hat{\rho}=0 in ([7](https://arxiv.org/html/2601.20643v1#S3.E7 "In item 2. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions")).
  2. (2b)

     Two-parameter shrinkage covariance estimator (COV2) [[19](https://arxiv.org/html/2601.20643v1#bib.bib11 "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection")]: This estimator sets 𝑻=v¯​𝑰p+c¯​(𝑱p−𝑰p)\bm{T}=\bar{v}\bm{I}\_{p}+\bar{c}(\bm{J}\_{p}-\bm{I}\_{p}), where v¯=1p​trace​(𝑺n)\bar{v}=\frac{1}{p}\mathrm{trace}(\bm{S}\_{n}), and 𝑱p\bm{J}\_{p} is the p×pp\times p matrix of ones. It uses

     |  |  |  |
     | --- | --- | --- |
     |  | ρ^off=1p−1​[1p​n​∑t=1n((∑i=1pRt​i)2−∑i=1pRt​i2)2−1p​(∑i≠j(Sn)i​j)2]\hat{\rho}\_{\mathrm{off}}=\frac{1}{p-1}\left[\frac{1}{pn}\sum\_{t=1}^{n}\left(\left(\sum\_{i=1}^{p}R\_{ti}\right)^{2}-\sum\_{i=1}^{p}R\_{ti}^{2}\right)^{2}-\frac{1}{p}\left(\sum\_{i\neq j}(S\_{n})\_{ij}\right)^{2}\right] |  |

     in ([8](https://arxiv.org/html/2601.20643v1#S3.E8 "In item 2. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions")).
  3. (2c)

     Constant-correlation shrinkage covariance estimator (COVCOR) [[19](https://arxiv.org/html/2601.20643v1#bib.bib11 "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection")]: This estimator sets
     𝑻\bm{T} defined elementwise by

     |  |  |  |
     | --- | --- | --- |
     |  | Ti​j={r¯​(Sn)i​i​(Sn)j​j,if ​i≠j,(Sn)i​i,if ​i=j,T\_{ij}=\begin{cases}\bar{r}\sqrt{(S\_{n})\_{ii}}\sqrt{(S\_{n})\_{jj}},&\text{if }i\neq j,\\ (S\_{n})\_{ii},&\text{if }i=j,\end{cases} |  |

     where r¯\bar{r} is computed as r¯=1p​(p−1)​∑i≠j(Sn)i​j(Sn)i​i​(Sn)j​j.\bar{r}=\frac{1}{p(p-1)}\sum\_{i\neq j}\frac{(S\_{n})\_{ij}}{\sqrt{(S\_{n})\_{ii}(S\_{n})\_{jj}}}. This estimator uses the off-diagonal shrinkage adjustment in ([8](https://arxiv.org/html/2601.20643v1#S3.E8 "In item 2. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions")) as

     |  |  |  |
     | --- | --- | --- |
     |  | ρ^off=r¯​∑i=1p∑j=1pΓi​j(Sn)i​i​(Sn)j​j,\hat{\rho}\_{\mathrm{off}}=\bar{r}\sum\_{i=1}^{p}\sum\_{j=1}^{p}\frac{\Gamma\_{ij}}{(S\_{n})\_{ii}(S\_{n})\_{jj}}, |  |

     where 𝚪=1n​(𝑹(3))⊤​𝑹−(𝒗⋅𝟏p⊤)∘𝑺n,\bm{\Gamma}=\frac{1}{n}(\bm{R}^{(3)})^{\top}\bm{R}-\left(\bm{v}\cdot\bm{1}\_{p}^{\top}\right)\circ\bm{S}\_{n},
     with (𝑹(3))i​j=Ri​j3(\bm{R}^{(3)})\_{ij}=R\_{ij}^{3}, 𝒗=diag​(𝑺n)\bm{v}=\mathrm{diag}(\bm{S}\_{n}), and ∘\circ denotes Hadamard product.
  4. (2d)

     Diagonal shrinkage covariance estimator (COVDIAG) [[20](https://arxiv.org/html/2601.20643v1#bib.bib12 "A well-conditioned estimator for large-dimensional covariance matrices")]: This estimator sets 𝑻=diag​(𝑺n)\bm{T}=\mathrm{diag}(\bm{S}\_{n}), and uses ρ^=ρ^d​i​a​g\hat{\rho}=\hat{\rho}\_{diag} in ([7](https://arxiv.org/html/2601.20643v1#S3.E7 "In item 2. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions")).
  5. (2e)

     Market shrinkage covariance estimator (COVMKT) [[20](https://arxiv.org/html/2601.20643v1#bib.bib12 "A well-conditioned estimator for large-dimensional covariance matrices")]: This estimator sets
     𝑻\bm{T} defined elementwise by

     |  |  |  |
     | --- | --- | --- |
     |  | Ti​j={(𝚺R​Rmkt)i​(𝚺R​Rmkt)jσRmkt​Rmkt,if ​i≠j,(Sn)i​i,if ​i=j.T\_{ij}=\begin{cases}\displaystyle\frac{(\bm{\Sigma}\_{RR\_{\mathrm{mkt}}})\_{i}(\bm{\Sigma}\_{RR\_{\mathrm{mkt}}})\_{j}}{\sigma\_{R\_{\mathrm{mkt}}R\_{\mathrm{mkt}}}},&\text{if }i\neq j,\\[5.0pt] (S\_{n})\_{ii},&\text{if }i=j.\end{cases} |  |

     where 𝚺R​Rmkt​ and ​σRmkt​Rmkt\bm{\Sigma}\_{RR\_{\mathrm{mkt}}}\text{ and }\sigma\_{R\_{\mathrm{mkt}}R\_{\mathrm{mkt}}} are defined as

     |  |  |  |
     | --- | --- | --- |
     |  | 𝚺R​Rmkt=1n​𝑹⊤​𝑹mkt,σRmkt​Rmkt=1n​𝑹mkt⊤​𝑹mkt​where​𝑹mkt=1p​𝑹​𝟏p.\bm{\Sigma}\_{RR\_{\mathrm{mkt}}}=\frac{1}{n}\bm{R}^{\top}\bm{R}\_{\mathrm{mkt}},\;\sigma\_{R\_{\mathrm{mkt}}R\_{\mathrm{mkt}}}=\frac{1}{n}\bm{R}\_{\mathrm{mkt}}^{\top}\bm{R}\_{\mathrm{mkt}}\;\textrm{where}\;\bm{R}\_{\mathrm{mkt}}=\frac{1}{p}\bm{R}\bm{1}\_{p}. |  |

     Also, this estimator uses the off-diagonal shrinkage adjustment in ([8](https://arxiv.org/html/2601.20643v1#S3.E8 "In item 2. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions")) as

     |  |  |  |
     | --- | --- | --- |
     |  | ρ^off=2​∑i=1p∑j=1p(𝑲1)i​j​(𝚺R​Rmkt)jσRmkt​Rmkt−∑i=1p∑j=1p(𝑲2)i​j​(𝚺R​Rmkt)i​(𝚺R​Rmkt)jσRmkt​Rmkt2−∑i=1p(𝑲1)i​i​(𝚺R​Rmkt)i2σRmkt​Rmkt2,\hat{\rho}\_{\mathrm{off}}=2\sum\_{i=1}^{p}\sum\_{j=1}^{p}\frac{(\bm{K}\_{1})\_{ij}(\bm{\Sigma}\_{RR\_{\mathrm{mkt}}})\_{j}}{\sigma\_{R\_{\mathrm{mkt}}R\_{\mathrm{mkt}}}}-\sum\_{i=1}^{p}\sum\_{j=1}^{p}\frac{(\bm{K}\_{2})\_{ij}(\bm{\Sigma}\_{RR\_{\mathrm{mkt}}})\_{i}(\bm{\Sigma}\_{RR\_{\mathrm{mkt}}})\_{j}}{\sigma\_{R\_{\mathrm{mkt}}R\_{\mathrm{mkt}}}^{2}}-\sum\_{i=1}^{p}\frac{(\bm{K}\_{1})\_{ii}(\bm{\Sigma}\_{RR\_{\mathrm{mkt}}})\_{i}^{2}}{\sigma\_{R\_{\mathrm{mkt}}R\_{\mathrm{mkt}}}^{2}}, |  |

     where

     |  |  |  |
     | --- | --- | --- |
     |  | 𝑲1=1n​(𝑹(2))⊤​𝑴−𝚺R​Rmkt∘𝑺n,𝑲2=1n​𝑴⊤​𝑴−σRmkt​Rmkt​𝑺n,with​𝑴=𝑹∘𝑹mkt⊤\bm{K}\_{1}=\frac{1}{n}(\bm{R}^{(2)})^{\top}\bm{M}-\bm{\Sigma}\_{RR\_{\mathrm{mkt}}}\circ\bm{S}\_{n},\;\bm{K}\_{2}=\frac{1}{n}\bm{M}^{\top}\bm{M}-\sigma\_{R\_{\mathrm{mkt}}R\_{\mathrm{mkt}}}\bm{S}\_{n},\;\;\textrm{with}\;\bm{M}=\bm{R}\circ\bm{R}\_{\mathrm{mkt}}^{\top} |  |
* 3.

  Inverse Shrinkage-Based variance Estimators: Building on the foundational work of Stein [[33](https://arxiv.org/html/2601.20643v1#bib.bib16 "Estimation of a covariance matrix, rietz lecture"), [34](https://arxiv.org/html/2601.20643v1#bib.bib17 "Lectures on the theory of estimation of many parameters"), [35](https://arxiv.org/html/2601.20643v1#bib.bib18 "Lectures on the theory of estimation of many parameters")], recent developments reinterpret and refine his original shrinkage approach to improve both theoretical tractability and practical applicability in high-dimensional settings [[24](https://arxiv.org/html/2601.20643v1#bib.bib10 "Shrinkage estimation of large covariance matrices: keep it simple, statistician?"), [25](https://arxiv.org/html/2601.20643v1#bib.bib8 "Quadratic shrinkage for large covariance matrices")]. Specifically, this class of estimators transforms the nonlinear shrinkage of eigenvalues into a linear shrinkage in the inverse-eigenvalue domain.
  Let the sample covariance matrix 𝑺n\bm{S}\_{n} admits the spectral decomposition

  |  |  |  |
  | --- | --- | --- |
  |  | 𝑺n=𝑼​𝚲​𝑼⊤,\bm{S}\_{n}=\bm{U}\bm{\Lambda}\bm{U}^{\top}, |  |

  where 𝚲=diag​(λ1,…,λp)\bm{\Lambda}=\mathrm{diag}(\lambda\_{1},\dots,\lambda\_{p}) contains the eigenvalues arranged in increasing order, and 𝑼=[u1,…,up]\bm{U}=[u\_{1},\dots,u\_{p}] is the corresponding matrix of orthonormal eigenvectors. The key idea is to shrink the inverse eigenvalues toward structured targets, and then invert back to obtain stabilized covariance estimates. Below are the three estimators under this framework.

  1. (3a)

     Linear Inverse Shrinkage Estimator (LIS): Proposed by Ledoit and Wolf [[24](https://arxiv.org/html/2601.20643v1#bib.bib10 "Shrinkage estimation of large covariance matrices: keep it simple, statistician?")], it modifies the inverse eigenvalues of the sample covariance matrix using a linear shrinkage approach. The LIS inverse eigenvalues are defined as

     |  |  |  |
     | --- | --- | --- |
     |  | δ^iLIS=(1−c)​xi+2​c​xi​θ~n​(xi), for ​1≤i≤p.\widehat{\delta}\_{i}^{\mathrm{LIS}}=(1-c)x\_{i}+2cx\_{i}\tilde{\theta}\_{n}(x\_{i}),\text{ for }1\leq i\leq p. |  |

     where c∈(0,∞)c\in(0,\infty) is concentration ratio,
     xi=λi−1,x\_{i}=\lambda\_{i}^{-1},
     which correspond to the nonzero sample eigenvalues and the smoothed Stein shrinkage function θ~n​(xi)\tilde{\theta}\_{n}(x\_{i}) is given by
     θ~n​(xi)=1p​∑j=1min⁡(p,n)xj​(xj−xi)(xj−xi)2+hn2​xj2\tilde{\theta}\_{n}(x\_{i})=\frac{1}{p}\sum\_{j=1}^{\min(p,n)}\frac{x\_{j}(x\_{j}-x\_{i})}{(x\_{j}-x\_{i})^{2}+h\_{n}^{2}x\_{j}^{2}} with the smoothing parameter hnh\_{n} in this study is taken as hn=min(c2,,1/c2)0.35p0.35.h\_{n}=\frac{\min\;(c^{2},\;,1/c^{2})^{0.35}}{p^{0.35}}.

     To ensure regularization from above, the inverse eigenvalues are truncated as: δiLIS=min⁡(xi,δ^iLIS)\delta\_{i}^{\mathrm{LIS}}=\min(x\_{i},\widehat{\delta}\_{i}^{\mathrm{LIS}}). Therefore, with 𝚫LIS=diag​(1/δ1LIS,…,1/δpLIS)\bm{\Delta}^{\mathrm{LIS}}=\mathrm{diag}(1/\delta\_{1}^{\mathrm{LIS}},\dots,1/\delta\_{p}^{\mathrm{LIS}}), the LIS estimator of the covariance matrix is given as

     |  |  |  |
     | --- | --- | --- |
     |  | 𝚺^L​I​S=𝑼​ΔL​I​S​𝑼⊤.\widehat{\bm{\Sigma}}\_{LIS}=\bm{U}\Delta^{LIS}\bm{U}^{\top}. |  |
  2. (3b)

     Quadratic Inverse Shrinkage (QIS): In this case, Ledoit and Wolf [[25](https://arxiv.org/html/2601.20643v1#bib.bib8 "Quadratic shrinkage for large covariance matrices")], modifies the inverse eigenvalues of the sample covariance matrix using a quadratic shrinkage approach. For p≤np\leq n, the QIS shrunk eigenvalues are computed as

     |  |  |  |
     | --- | --- | --- |
     |  | δi=1(1−c)2​xi+2​c​(1−c)​xi​θ~n​(xi)+c2​xi​Aθ2​(xi), for ​1≤i≤p.\delta\_{i}=\frac{1}{(1-c)^{2}x\_{i}+2c(1-c)x\_{i}\tilde{\theta}\_{n}(x\_{i})+c^{2}x\_{i}A^{2}\_{\theta}(x\_{i})},\text{ for }1\leq i\leq p. |  |

     where Aθ2​(xi)=θ~n​(xi)2+(1p​∑j=1min⁡(p,n)hn​xj2(xj−xi)2+hn2​xj2)2A^{2}\_{\theta}(x\_{i})=\tilde{\theta}\_{n}(x\_{i})^{2}+\left(\frac{1}{p}\sum\_{j=1}^{\min(p,n)}\frac{h\_{n}x\_{j}^{2}}{(x\_{j}-x\_{i})^{2}+h\_{n}^{2}x\_{j}^{2}}\right)^{2}. While for p>np>n, the shrinkage for null eigenvalues is given as

     |  |  |  |
     | --- | --- | --- |
     |  | δ0=1(c−1)⋅1p−n​∑j=1p−nxj,\delta\_{0}=\frac{1}{(c-1)\cdot\frac{1}{p-n}\sum\_{j=1}^{p-n}x\_{j}}, |  |

     and set

     |  |  |  |
     | --- | --- | --- |
     |  | δi={δ0,for ​i=1,…,p−n,1xi​Aθ2​(xi),for ​i=p−n+1,…,p.\delta\_{i}=\begin{cases}\delta\_{0},&\text{for }i=1,\ldots,p-n,\\ \displaystyle\frac{1}{x\_{i}A^{2}\_{\theta}(x\_{i})},&\text{for }i=p-n+1,\ldots,p.\end{cases} |  |

     To ensure trace preservation, define the normalized eigenvalues as δiQIS=δi​(∑i=1pλn,i∑i=1pδi).\delta\_{i}^{\mathrm{QIS}}=\delta\_{i}\left(\frac{\sum\_{i=1}^{p}\lambda\_{n,i}}{\sum\_{i=1}^{p}\delta\_{i}}\right). With 𝚫QIS=diag​(δ1QIS,…,δpQIS)\bm{\Delta}^{\mathrm{QIS}}=\mathrm{diag}(\delta\_{1}^{\mathrm{QIS}},\ldots,\delta\_{p}^{\mathrm{QIS}}), the QIS covariance estimator is given as

     |  |  |  |
     | --- | --- | --- |
     |  | 𝚺^Q​I​S=𝑼​𝚫QIS​𝑼⊤.\widehat{\bm{\Sigma}}\_{QIS}=\bm{U}\bm{\Delta}^{\mathrm{QIS}}\bm{U}^{\top}. |  |
  3. (3c)

     Geometric Inverse Shrinkage Estimator (GIS): This method combines LIS and QIS by applying geometric averaging on the inverse eigenvalues (Ledoit and Wolf [[25](https://arxiv.org/html/2601.20643v1#bib.bib8 "Quadratic shrinkage for large covariance matrices")])

     |  |  |  |
     | --- | --- | --- |
     |  | δiGIS=δiQISδiLIS, for ​1≤i≤p.\delta\_{i}^{\mathrm{GIS}}=\sqrt{\frac{\delta\_{i}^{\mathrm{QIS}}}{\delta\_{i}^{\mathrm{LIS}}}},\text{ for }1\leq i\leq p. |  |

     For 𝚫GIS=diag​(δ1GIS,…,δpGIS)\bm{\Delta}^{\mathrm{GIS}}=\mathrm{diag}(\delta\_{1}^{\mathrm{GIS}},\ldots,\delta\_{p}^{\mathrm{GIS}}), the GIS estimator of the covariance matrix is defined as

     |  |  |  |
     | --- | --- | --- |
     |  | 𝚺^G​I​S=𝑼​𝚫GIS​𝑼⊤.\widehat{\bm{\Sigma}}\_{GIS}=\bm{U}\bm{\Delta}^{\mathrm{GIS}}\bm{U}^{\top}. |  |
* 4.

  Analytic Shrinkage Estimator (AS): Introduced by Ledoit and Wolf [[23](https://arxiv.org/html/2601.20643v1#bib.bib9 "Analytical nonlinear shrinkage of large-dimensional covariance matrices")], it uses kernel-based estimation of the spectral density to derive nonlinear shrinkage eigenvalues analytically.
  To estimate the spectral density, select a global bandwidth hn=n−1/3h\_{n}=n^{-1/3}, and define the locally adaptive bandwidth as hn,j=hn​λj,∀j=1,…,nh\_{n,j}=h\_{n}\lambda\_{j},\forall j=1,\ldots,n. Let κi​j=λi−λjhn,j\kappa\_{ij}=\frac{\lambda\_{i}-\lambda\_{j}}{h\_{n,j}}.
  The Epanechnikov kernel estimate of the spectral density at eigenvalue λn,i\lambda\_{n,i} is given by

  |  |  |  |
  | --- | --- | --- |
  |  | f^n​(λi)=1p​∑j=1p34​5​hn,j​(1−κi​j25)+,where ​[x]+=max⁡{x,0}.\widehat{f}\_{n}(\lambda\_{i})=\frac{1}{p}\sum\_{j=1}^{p}\frac{3}{4\sqrt{5}h\_{n,j}}\left(1-\frac{\kappa\_{ij}^{2}}{5}\right)\_{+},\text{where }[x]\_{+}=\max\{x,0\}. |  |

  The Hilbert transform of the spectral density is computed as

  |  |  |  |
  | --- | --- | --- |
  |  | H~f^n​(λi)=1p​∑j=1p1hn,j​π​[−310​κi​j+34​5​(1−κi​j25)​log⁡|5−κi​j5+κi​j|].\tilde{H}\_{\widehat{f}\_{n}}(\lambda\_{i})=\frac{1}{p}\sum\_{j=1}^{p}\frac{1}{h\_{n,j}\pi}\left[-\frac{3}{10}\kappa\_{ij}+\frac{3}{4\sqrt{5}}\left(1-\frac{\kappa\_{ij}^{2}}{5}\right)\log\left|\frac{\sqrt{5}-\kappa\_{ij}}{\sqrt{5}+\kappa\_{ij}}\right|\right]. |  |

  and the Analytic Shrinkage (AS) eigenvalues are then computed as

  |  |  |  |
  | --- | --- | --- |
  |  | δiAS=λi[π​c​λi​f~n​(λi)]2+[1−c−π​c​λi​H~f^n​(λi)]2.\delta\_{i}^{\mathrm{AS}}=\frac{\lambda\_{i}}{\left[\pi c\lambda\_{i}\tilde{f}\_{n}(\lambda\_{i})\right]^{2}+\left[1-c-\pi c\lambda\_{i}\tilde{H}\_{\widehat{f}\_{n}}(\lambda\_{i})\right]^{2}}. |  |

  For 𝚫AS=diag​(δ1AS,…,δPAS)\bm{\Delta}^{\mathrm{AS}}=\mathrm{diag}(\delta\_{1}^{\mathrm{AS}},\ldots,\delta\_{P}^{\mathrm{AS}}), the AS covariance estimator is defined as

  |  |  |  |
  | --- | --- | --- |
  |  | 𝚺^A​S=𝑼​𝚫AS​𝑼⊤.\widehat{\bm{\Sigma}}\_{AS}=\bm{U}\bm{\Delta}^{\mathrm{AS}}\bm{U}^{\top}. |  |

Table [1](https://arxiv.org/html/2601.20643v1#S3.T1 "Table 1 ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") summarizes the shrinkage estimators considered in this paper for easy reference.

Table 1: A total of five shrinkage estimators are implemented for the mean vector and eleven for the covariance matrix. Out of the eleven covariance estimators, GIS, LIS, and AS are not applicable for the high-dimensional data sets, i. e, when the number of time points exceeds the number of assets (p>np>n).

| Mean vector | Covariance matrix |
| --- | --- |
| 1. Classical approach: Sample mean (SM) | 1. Classical approach Sample covariance (SCV) |
| 2. James-Stein shrinkage (JS) [[16](https://arxiv.org/html/2601.20643v1#bib.bib4 "Estimation with quadratic loss")] | 2. Linear shrinkage (LS) [[7](https://arxiv.org/html/2601.20643v1#bib.bib7 "On the strong convergence of the optimal linear shrinkage estimator for large dimensional covariance matrix")] |
| 3. Bayes-Stein shrinkage (BS) [[18](https://arxiv.org/html/2601.20643v1#bib.bib3 "Bayes-Stein estimation for portfolio analysis")] | 3. One parameter shrinkage covariance (COV1) [[19](https://arxiv.org/html/2601.20643v1#bib.bib11 "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection")] |
| 4. Bodnar optimal linear shrinkage (BOP) [[8](https://arxiv.org/html/2601.20643v1#bib.bib5 "Optimal shrinkage estimator for high-dimensional mean vector")] | 4. Two parameter shrinkage covariance (COV2) [[19](https://arxiv.org/html/2601.20643v1#bib.bib11 "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection")] |
| 5. Quadratic shrinkage (QUAD) [[36](https://arxiv.org/html/2601.20643v1#bib.bib6 "Non-parametric shrinkage mean estimation for quadratic loss functions with unknown covariance matrices")] | 5. Constant-correlation shrinkage covariance (COVCOR) [[19](https://arxiv.org/html/2601.20643v1#bib.bib11 "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection")] |
|  | 6. Diagonal shrinkage covariance (COVDIAG) [[20](https://arxiv.org/html/2601.20643v1#bib.bib12 "A well-conditioned estimator for large-dimensional covariance matrices")] |
|  | 7. Market shrinkage covariance (COVMKT) [[20](https://arxiv.org/html/2601.20643v1#bib.bib12 "A well-conditioned estimator for large-dimensional covariance matrices")] |
|  | 8. Linear Inverse Shrinkage (LIS) [[24](https://arxiv.org/html/2601.20643v1#bib.bib10 "Shrinkage estimation of large covariance matrices: keep it simple, statistician?")] |
|  | 9. Quadratic Inverse Shrinkage (QIS) [[25](https://arxiv.org/html/2601.20643v1#bib.bib8 "Quadratic shrinkage for large covariance matrices")] |
|  | 10. Geometric Inverse Shrinkage (GIS) [[25](https://arxiv.org/html/2601.20643v1#bib.bib8 "Quadratic shrinkage for large covariance matrices")] |
|  | 11. Analytic shrinkage (AS) [[23](https://arxiv.org/html/2601.20643v1#bib.bib9 "Analytical nonlinear shrinkage of large-dimensional covariance matrices")] |

For the five estimators of the mean vector combined with the eleven covariance matrix estimators, we construct a total of 55 (5 × 11) MV models and 11 GMV models in the low-dimensional setting. In the high-dimensional case, using only eight covariance matrix estimators, we obtain 40 (5 × 8) MV models and 8 GMV models. With three out-of-sample-sized windows, resulting in a
large number of portfolios.

We set γ=1\gamma=1 in the (MV) model in our empirical analysis.

We need an effective and robust ranking method that incorporates key financial performance metrics, such as returns, risk indicators, and risk–reward ratios. We deploy the Data Envelopment Analysis (DEA) super-efficiency model [[10](https://arxiv.org/html/2601.20643v1#bib.bib19 "Measuring the efficiency of decision making units")] to rank the portfolios generated from the shrinkage-based MV and GMV models.

## 4 Super-efficiency DEA Model

DEA is a non-parametric linear programming approach used to evaluate the relative efficiency of homogeneous decision-making units (DMUs) that operate with multiple inputs and outputs. In the standard DEA framework, an efficient frontier is constructed based on the best-performing units. However, since all efficient units receive the same efficiency score, Andersen and Petersen [[1](https://arxiv.org/html/2601.20643v1#bib.bib20 "A procedure for ranking efficient units in data envelopment analysis")] introduced the super-efficiency DEA model to enable a complete ranking.
In the super-efficiency model, the DMU under evaluation is excluded from the reference set, allowing for efficiency scores greater than one for efficient DMUs and enabling a more granular ranking among them. The super-efficiency DEA model is well-suited for benchmarking where discrimination among efficient units is essential.

Let there be dd units, each utilizing mm inputs to produce ss outputs. Define the input matrix 𝑾∈ℝd×m\bm{W}\in\mathbb{R}^{d\times m}, where each row corresponds to a DMU and each column to an input variable. Similarly, let the output matrix 𝒀∈ℝd×s\bm{Y}\in\mathbb{R}^{d\times s} represent the outputs of all DMUs. The input and output vectors for DMU ii are denoted 𝒘i∈ℝm\bm{w}\_{i}\in\mathbb{R}^{m} and 𝒚i∈ℝs\bm{y}\_{i}\in\mathbb{R}^{s}, respectively. The super-efficiency score of DMU ii, denoted effi\textit{eff}\_{i},  i=1,…,d,i=1,\dots,d, is obtained by solving the following optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (DEA)​max\displaystyle\text{(DEA)}\;\;\max\quad | effi=∑r=1sur​yi​r\displaystyle\textit{eff}\_{i}=\sum\_{r=1}^{s}u\_{r}y\_{ir} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | subject to | ∑r=1sur​yj​r−∑k=1mvk​wj​k≤0,∀j≠i,j=1,…,d,\displaystyle\sum\_{r=1}^{s}u\_{r}y\_{jr}-\sum\_{k=1}^{m}v\_{k}w\_{jk}\leq 0,\quad\forall\;j\neq i,\;j=1,\ldots,d, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑k=1mvk​wi​k=1,\displaystyle\sum\_{k=1}^{m}v\_{k}w\_{ik}=1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ur≥0,vk≥0,∀r,k.\displaystyle u\_{r}\geq 0,\quad v\_{k}\geq 0,\quad\forall\;r,\,k. |  |

Here, uru\_{r} and vkv\_{k} denote the weights assigned to output rr and input kk, respectively.

In the context of this paper, we consider portfolios generated by various shrinkage-based MV and GMV models as DMUs. The objective is to rank these units based on multiple financial performance metrics summarized in Table [2](https://arxiv.org/html/2601.20643v1#S4.T2 "Table 2 ‣ 4 Super-efficiency DEA Model ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"). Input metrics (to be minimized) are primarily associated with risk measures, while output metrics (to be maximized) represent return and risk-adjusted ratios. The (DEA) model provides a systematic framework to evaluate shrinkage strategies by assessing how effectively they manage the trade-off between return and risk.

Table 2: Financial metrics used for computing the super-efficiency scores and comparative analysis with the benchmark models.

|  |  |  |
| --- | --- | --- |
| Metric | Input/Output | Formula / Description |
| Return |  |  |
| Mean return | Output | E​(Rx)=1n​∑l=1nRlE(R\_{x})=\displaystyle\frac{1}{n}\sum\_{l=1}^{n}R\_{l}; RlR\_{l} is a out-of-sample return of portfolio xx at time l;l=1,…,nl;l=1,\ldots,n |
| Risk |  |  |
| Standard Deviation (SD) | Input | 1n​∑l=1n(E​(Rx)−Rl)2\sqrt{\frac{1}{n}\sum\_{l=1}^{n}\left(E(R\_{x})-R\_{l}\right)^{2}} |
| Value-at-Risk (VaR(Rx)0.05{}\_{0.05}(R\_{x})) | Input | Out-of-sample Value-at-risk of portfolio xx at 95% confidence level111Typically calculated using historical simulation or parametric methods. |
| Conditional VaR (CVaR0.05) | Input | Out-of-sample conditional VaR of portfolio xx at 95% confidence level222Also known as Expected Shortfall. |
| Downside Deviation (DD) | Input | 1n​∑l=1n(min⁡(0,Rl))2\sqrt{\frac{1}{n}\sum\_{l=1}^{n}\left(\min(0,R\_{l})\right)^{2}} |
| Risk-adjusted Performance |  |  |
| Mean-CVaR ratio | Output | E​(Rx)CVaR0.05​(Rx)\displaystyle\frac{E(R\_{x})}{\text{CVaR}\_{0.05}(R\_{x})};  E​(Rx)>0E(R\_{x})>0 |
| Sharpe ratio | Output | E​(Rx)SD\displaystyle\frac{E(R\_{x})}{\text{SD}};  E​(Rx)>0E(R\_{x})>0 |
| Sortino ratio | Output | E​(Rx)DD\displaystyle\frac{E(R\_{x})}{\text{DD}};  E​(Rx)>0E(R\_{x})>0 |
| Mean-VaR ratio | Output | E​(Rx)VaR0.05​(Rx)\displaystyle\frac{E(R\_{x})}{\text{VaR}\_{0.05}(R\_{x})};  E​(Rx)>0E(R\_{x})>0 |
| Turnover | Input | 1n−1​∑l=1n−1∑j=1p|xj,l+1−xj,l|\displaystyle\frac{1}{n-1}\sum\_{l=1}^{n-1}\sum\_{j=1}^{p}\left|x\_{j,l+1}-x\_{j,l}\right| |

## 5 Data and Empirical Set-up

### 5.1 Sample Data and Sample Period

The sample data consists of daily closing prices of the constituents for the six global market indices listed in Table [3](https://arxiv.org/html/2601.20643v1#S5.T3 "Table 3 ‣ 5.1 Sample Data and Sample Period ‣ 5 Data and Empirical Set-up ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") from September 20, 2012, to Jun 6, 2024. Daily historical price data is collected from the LSEG workspace (https://www.lseg.com/en), previously Refinitiv Eikon datastream. Only assets that are actively trading and part of the index as of Jun 6, 2024.

Table 3: Financial data sets for the empirical study

| Low-dimensional data sets | High-dimensional Data Sets |
| --- | --- |
| Data Set 1: DJ 30 (USA), 30 assets | Data Set 4: S&P 500 (USA), 453 assets |
| Data Set 2: NIFTY 50 (India), 48 assets | Data Set 5: RUSSELL 1000 (USA), 664 assets |
| Data Set 3: FTSE 100 (UK), 92 assets | Data Set 6: TOPIX 1500 (Japan), 1451 assets |

The experiments are performed on a Windows 10 64-bit operating system with 12 GB RAM and a 12th Gen Intel(R) Core(TM) i7-12700T 1.40 GHz processor. We use MATLAB YALMIP with the MOSEK solver to solve all considered optimization models.

### 5.2 Rolling Window Scheme

We use a rolling window approach consisting of an in-sample period and an out-of-sample period, measured in days. All optimal portfolios are obtained by solving corresponding models over the in-sample data, which are then assessed on the out-of-sample data. The in-sample time horizon is then shifted forward by a number of days corresponding to the out-of-sample period to create a second window, and the previous procedure is repeated until the entire data set is exhausted. For the present study, we use a 1-year in-sample size (260 trading days) and three out-of-sample periods: (1) 3-months (65 trading days), leading to 43 windows (in-sample of one year is shifted forward by 3-months); (2) 6-months (130 trading days), leading to 21 windows; and (3) 1-year (260 trading days), resulting in 10 windows.

For 260 days in-sample, the concentration ratio c>1c>1 for three high-dimensional datasets, the GIS, LIS, and AS shrinkage estimators for covariance, are not defined as they require c<1c<1. Therefore, we have 55 (5×\times11) MV and 11 GMV models for low-dimensional data and 40 (5×\times8) MV and 8 GMV models for high-dimensional data in each in-sample rolling window. Each optimal portfolio is assessed across three out-of-sample windows.

This analysis of varying out-of-sample window sizes aims to provide information on the stable performance of all considered models, particularly in relation to risk-return dynamics, risk-adjusted efficiency, and the stability of portfolio allocation with respect to changes in window size.

### 5.3 Methodology

The empirical investigation of the underlying study is mainly divided into the following steps:

* 1.

  Step I- Ranking  We first rank all the portfolios generated from the shrinkage-based MV and GMV models by (DEA) models utilizing the input/output as described in Table [2](https://arxiv.org/html/2601.20643v1#S4.T2 "Table 2 ‣ 4 Super-efficiency DEA Model ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"). For this, the ranking of portfolios is done for each market, each group, and for the three sized out-of-sample windows as follows:

  1. (a)

     Group A: All ten metrics are taken into consideration. That means the input-output data matrix is 66×1066\times 10 (for a low-dimension market) and 48×1048\times 10 (for a high-dimensional market), and we have three such matrices for each of the out-of-sample periods.
  2. (b)

     Group B: When only return and risk-adjusted metrics are taken in analysis.
     The model includes five outputs namely average return, mean-CVaR ratio, Sharpe ratio, Sortino ratio, and mean-VaR ratio, and the only input is set as a vector of ones, implying equal weight or neutral performance across all DMUs. Thus, the input-output data matrix is 66×666\times 6 (for a low-dimensional market) and 48×648\times 6 (for a high-dimensional market).
  3. (c)

     Group C: When only the risk-based financial metrics are applied in ranking. The inputs for this group are standard deviation (SD), value-at-risk (VaR), conditional value-at-risk (CVaR), maximum drawdown (DD), and turnover, capturing pure risk characteristics. The only output is taken as a vector of ones. Thus, the input-output data matrix is 66×666\times 6 (for a low-dimensional market) and 48×648\times 6 (for a high-dimensional market).
* 2.

  Step II- Filtration: Based on their efficiency scores, we identify the top 10 portfolios for every market, every group, and each of the three out-of-sample windows. Out of these 10 most efficient portfolios, we finally select the two best portfolios for each group in two ways: (i) market best-performer and (ii) universal best-performer.

  + (a)

    For each of the three groups, the market’s best-performing portfolio is the one having the highest geometric mean (GM) (e​f​f1​e​f​f2​e​f​f3)1/3(eff\_{1}\;eff\_{2}\;eff\_{3})^{1/3} of the efficiency scores in the three out-of-sample windows. Thus, we have 6 of the best-performing market portfolios (one for each market) for every group.
  + (b)

    For each group, the universal best-performing portfolio is the one that is the best market performer in the maximum number of markets.
* 3.

  Step III-Comparison with the benchmark models:
  The final set of two filtered portfolios for each group are compared against the following traditional PO models over each data set:

  + 1.

    Classical Markowitz mean-variance (MV) model with the sample mean and the sample covariance [[27](https://arxiv.org/html/2601.20643v1#bib.bib21 "PORTFOLIO selection")].
  + 2.

    Classical global minimum variance (GMV) model with sample covariance [[27](https://arxiv.org/html/2601.20643v1#bib.bib21 "PORTFOLIO selection")].
  + 3.

    Semi Mean Absolute Deviation (SMAD) model [[13](https://arxiv.org/html/2601.20643v1#bib.bib62 "A reformulation of a mean-absolute deviation portfolio optimization model.")].
  + 4.

    Conditional Value at Risk (CVaR) model [[31](https://arxiv.org/html/2601.20643v1#bib.bib63 "Optimization of conditional value-at-risk")].
  + 5.

    MiniMax (MM) model [[9](https://arxiv.org/html/2601.20643v1#bib.bib64 "Portfolio optimization under a minimax rule")].

  The mathematical formulations of the optimization problems for the SMAD, CVaR, and MM models are provided in the Appendix.
  The comparative analysis provided a comprehensive evaluation of the optimal portfolios from the shrinkage-based PO with widely accepted benchmark models across the considered markets.

## 6 Result Discussion

### 6.1 Assessment for Group A

The top 10 portfolio models are shown in Table [4](https://arxiv.org/html/2601.20643v1#S6.T4 "Table 4 ‣ 6.1 Assessment for Group A ‣ 6 Result Discussion ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") based on their efficiency score computed by the (DEA) model when all financial metrics (listed in Table [2](https://arxiv.org/html/2601.20643v1#S4.T2 "Table 2 ‣ 4 Super-efficiency DEA Model ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions")) are taken into account as input and output.

The models were listed in the format of “covariance estimator + mean estimator” for the (MV) model, while it is expressed as “GMV + covariance estimator” for the (GMV) model, indicating that the mean estimator has no role to play herein.

Ranking is presented for the three distinct window sizes across each of the six datasets (Panels 1–3). Panel 4 presents the market and universal best performers for each dataset. The efficiency score for each portfolio across all datasets and varying out-of-sample window sizes is presented in the GitHub link 333https://github.com/rupendrayadav19401/Shrinkage-PO.

The following conclusions are drawn from Table [4](https://arxiv.org/html/2601.20643v1#S6.T4 "Table 4 ‣ 6.1 Assessment for Group A ‣ 6 Result Discussion ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").

* 1.

  DJ: GMV+COV2 was identified as the best-performing model, as it appears in the top 5 list over all window sizes, with the highest geometric mean efficiency score of 1.01043. We observe that COV2 demonstrates superior performance relative to other covariance estimators, followed by COV1. This is evidenced by the fact that, out of the thirty top 10 portfolios, 18 are based on COV2 and 9 on COV1. Notably, portfolios from the model GMV+COV2 appeared consistently across all three out-of-sample windows. This suggests that the COV2 becomes the best shrinkage estimator.
* 2.

  NIFTY: GMV+COV2 demonstrates superior performance as a shrinkage model, achieving a geometric mean efficiency of 1.00512. GMV+LIS ranks as the second-best performer, maintaining a position within the top two selections for the three-month and one-year out-of-sample periods. Portfolios employing sample and BS estimators for mean estimation exhibited superior performance, specifically over the 6-month and 1-year out-of-sample periods, respectively.
* 3.

  FTSE: LIS+SM is the top-performing shrinkage model, achieving a geometric mean efficiency of 1.00285. The GIS, LIS, and QIS covariance estimators outperformed the others, and the BS, sample, and QUAD estimators estimate the mean more accurately than the others. It’s notable that GMV-based models don’t make it to the top 10 rankings.
* 4.

  S&P: Like DJ and NIFTY, the GMV+COV2 model distinguishes itself as the foremost performer, achieving a geometric mean efficiency of 1.07442. Regardless of the out-of-sample duration, it consistently demonstrates exceptional performance in this market. Moreover, the COV2 and QIS shrinkage estimators of covariance exhibited superior performance during the 6-month out-of-sample interval. During the 3-month and 1-year intervals, their efficacy was, however, less pronounced.
* 5.

  RUSSELL: GMV+QIS and GMV+COV2 shrinkage-based portfolios exhibited comparable performance within this data set, with geometric means efficiency of 1.03598 and 1.0171, respectively. For all three out-of-sample periods, QIS+BS also retains its top 10 position for this market. In fact, portfolios utilizing the QIS variance estimator consistently ranked among the top 10 performers here.
* 6.

  TOPIX: GMV+COVMKT model is identified as the best-performing approach with the geometric mean efficiency value 1.05409, followed by the GMV+SCV model with a score of 1.02523. The GMV-based models consistently dominated the top 10 positions. The GMV+COV2 estimator retains its top 10 position over the 3-month and 6-month out-of-sample period; however, it missed for the 1-year period, with an efficiency score of 0.97899. Among non-GMV models, the COVMKT+BS model demonstrated superior performance.
* 7.

  Universal best performer: Except for the FTSE and TOPIX (over the 1-year window), the GMV+COV2 combination consistently placed in the top 10 across all datasets and window types. This renders the portfolio a universally superior performer. The S&P, a globally recognized market, consistently ranks GMV-COV2 as the top model across all window widths.
* 8.

  Observations on varying out-of-sample period: When the out-of-sample period is set to 3-months, GMV+COV2 is in the top 5 in all markets except FTSE. However, the observations change slightly when examining 6-month periods. GMV+COV2 drops to 6th place over NIFTY and TOPIX, but stays in the top 5 over DJ, S&P, and RUSSELL. For the 1-year out-of-sample period, GMV+COV2, on the other hand, jumps into the top 2 spots among the markets DJ, NIFTY, S&P, and RUSSELL, whereas it disappears entirely from TOPIX. This suggests that GMV+COV2 consistently ranked within the top 5 or 6 across most markets, regardless of variations in out-of-sample periods.

  The model QIS+BS comes next. It is in the top 10 across the 5 markets (DJ, FTSE, S&P, Russell, and TOPIX) except for NIFTY, for the 3-month period. However, as the investment time increases, its performance decreases: 6-months (in the top 10 over FTSE, S&P, RUSSELL, and TOPIX) and 1-year (in the top 10 in NIFTY, FTSE, and RUSSELL).

  Notably, the classical method of solving the MV model using sample mean and sample covariance fails to find a place in the top 10 for any market in any type of out-of-sample period. The GMV model with sample covariance, on the other hand, does appear in the top 10 for certain cases, such as over TOPIX (for all out-of-sample periods) and RUSSELL (over the 1-year out-of-sample period).

Table 4: Group A- The top 10 shrinkage-based MV and GMV portfolios arranged from highest to lowest ranking order as per their super efficiency scores when all the financial matrices are considered in the (DEA) model. Rankings are given for all six data sets. The Panels 1, 2, and 3, respectively, display the ranking when out-of-sample periods are set to 3-months, 6-months and 1-year in the rolling window scheme. Panel 4 describes the market-best and universal-best performer, along with the geometric mean of efficiency scores (GM of Efficiency) corresponding to each market-best performer.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Rank | DJ | NIFTY | FTSE | S&P | RUSSELL | TOPIX |
| Panel 1: Out-of-sample period= 3 months | | | | | | |
| 1 | GMV+COV2 | COV2+BS | LIS+SM | GMV+COV2 | GMV+QIS | GMV+COVMKT |
| 2 | COV2+QUAD | GMV+COV2 | COV2+SM | GMV+COV1 | GMV+COV2 | GMV+SCV |
| 3 | COV2+BS | GMV+COVDIAG | AS+SM | QIS+SM | QIS+SM | COVMKT+BS |
| 4 | COV2+JS | COV1+BS | LIS+BS | COV1+JS | QIS+BS | GMV+QIS |
| 5 | COV2+SM | COV1+SM | AS+SM | QIS+BOP | QIS+BOP | GMV+COV2 |
| 6 | GMV+COV1 | COV2+SM | GIS+SM | QIS+JS | QIS+JS | QIS+JS |
| 7 | COV2+BOP | GMV+COV1 | GIS+BS | LS+SM | GMV+COV1 | GMV+COV1 |
| 8 | COV1+QUAD | GMV+LIS | QIS+BS | LS+BOP | QIS+QUAD | GMV+LS |
| 9 | QIS+BS | COVDIAG+QUAD | AS+BS | GMV+QIS | COV1+SM | QIS+BS |
| 10 | GIS+BS | LIS+SM | LS+SM | QIS+BS | COV1+JS | COVCOR+SM |
| Panel 2: Out-of-sample period= 6 months | | | | | | |
| 1 | COV2+BS | GMV+LIS | QIS+QUAD | GMV+COV2 | GMV+QIS | GMV+COVMKT |
| 2 | COV2+SM | LIS+BS | LIS+QUAD | COV2+BS | GMV+COV2 | COVMKT+BS |
| 3 | COV2+JS | AS+BS | LIS+BS | QIS+BOP | QIS+SM | GMV+SCV |
| 4 | GMV+COV2 | COVMKT+BS | GIS+QUAD | COV2+JS | QIS+BS | GMV+QIS |
| 5 | COV2+BOP | COVDIAG+QUAD | GIS+BS | COV2+SM | COVDIAG+SM | QIS+BS |
| 6 | COV1+SM | GMV+COV2 | QIS+BS | COV2+BOP | QIS+BOP | GMV+COV2 |
| 7 | COV2+QUAD | AS+SM | LIS+SM | QIS+BS | COVDIAG+JS | QIS+JS |
| 8 | COV1+QUAD | LIS+SM | AS+QUAD | QIS+JS | QIS+JS | GMV+COV1 |
| 9 | COV1+JS | QIS+SM | GIS+SM | COV2+QUAD | COVDIAG+BS | COVCOR+JS |
| 10 | COV1+BS | COV2+SM | QIS+SM | QIS+QUAD | COVDIAG+JS | COVCOR+BS |
| Panel 3: Out-of-sample period= 1 year | | | | | | |
| 1 | GMV+COV2 | GMV+COV2 | QIS+SM | GMV+COV2 | QIS+QUAD | GMV+COV1 |
| 2 | COV2+QUAD | GMV+LIS | QIS+BS | COV2+QUAD | GMV+COV2 | GMV+QIS |
| 3 | COV2+BS | AS+BS | LIS+SM | SCV+BOP | GMV+QIS | GMV+SCV |
| 4 | COV2+SM | COV2+BS | AS+BS | LS+SM | GMV+SCV | GMV+COVMKT |
| 5 | COV2+JS | LIS+BS | GIS+SM | COV1+JS | QIS+SM | GMV+COVDIAG |
| 6 | COV2+BOP | GIS+BS | GIS+BS | LS+QUAD | QIS+JS | COVDIAG+JS |
| 7 | COV1+QUAD | QIS+BS | GIS+QUAD | COV1+SM | QIS+BS | GMV+LS |
| 8 | COV1+SM | COV1+SM | LIS+QUAD | LS+BS | QIS+BOP | COVMKT+BS |
| 9 | GMV+COV1 | AS+SM | QIS+QUAD | COVDIAG+QUAD | GMV+COV1 | GMV+COVCOR |
| 10 | QIS+QUAD | COV2+SM | LIS+BS | SCV+BS | GMV+LS | COVCOR+JS |
| Panel 4: Best performing model | | | | | | |
| Market best | GMV+COV2 | GMV+COV2 | LIS+SM | GMV+COV2 | GMV+QIS | GMV+COVMKT |
| (GM of Efficiency) | (1.01043) | (1.00512) | (1.00285) | (1.07442) | (1.03598) | (1.05409) |
| Universal best | GMV+COV2 | GMV+COV2 | GMV+COV2 | GMV+COV2 | GMV+COV2 | GMV+COV2 |

### 6.2 Assessment for Group B

Table [5](https://arxiv.org/html/2601.20643v1#S6.T5 "Table 5 ‣ 6.2 Assessment for Group B ‣ 6 Result Discussion ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") presents the (DEA) model-based rankings for the top 10 portfolios across all the datasets and varying out-of-sample windows. The following findings are noted from Table [5](https://arxiv.org/html/2601.20643v1#S6.T5 "Table 5 ‣ 6.2 Assessment for Group B ‣ 6 Result Discussion ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").

* 1.

  DJ: COV2+SM model is observed as the best-performing model, signifying the importance of the mean function in the modelling for the return-focused investor. Over this dataset, the QUAD and SAMPLE estimators demonstrated dominance as mean estimators, while COV2 and COV1 exhibited superior performance as variance estimators.
* 2.

  NIFTY: The portfolio from the COV2+SM model is identified as the best-performing shrinkage model, followed by the COV2+QUAD and SCV+QUAD models. The QUAD and SAMPLE estimators demonstrated dominance as mean estimators, while COV2 exhibited superior performance as a variance estimator.
* 3.

  FTSE: LIS+SM model is the best-performing shrinkage model. The QUAD and SAMPLE estimators demonstrated dominance as mean estimators, whereas LIS exhibited superior performance as a variance estimator, followed by GIS and QIS.
* 4.

  S&P : Model COV2+SM is identified as the best-performing shrinkage-based MV model. While models utilizing BOP-based mean estimators demonstrated strong performance, they fail to achieve the same level of consistency as the COV2+SM model.
* 5.

  RUSSELL and TOPIX: The GMV+QIS approach has been recognized as the most effective. This portfolio demonstrates consistent performance across both groups A and B in these two markets. In the RUSSELL market, the QIS+QUAD model yields the second-best portfolio, and the GMV+SCV and GMV+COVMKT models provide the second-best options for TOPIX.
  Notably, in the RUSSELL dataset, the selection of mean estimators has a negligible effect on performance; however, the QIS-based variance estimator showed enhanced efficacy.
* 6.

  Observations on varying out-of-sample period: With the exception of TOPIX and RUSSELL (1-year out-of-sample period), the COV2+SM model consistently demonstrates in the top 10 performance across all markets. Based on this output, COV2+SM is the best overall choice, i. e, a universal best performer, but it fails to be an ideal pick for the market TOPIX.

  The COV2+QUAD follows next. It has been in the top 10 for DJ, NIFTY, RUSSELL, and TOPIX for 3-months, and for DJ, NIFTY, FTSE, and SP for 6-months and 1-year. Furthermore, regardless of the time horizon in low-dimensional markets, the impact of the mean estimator (SAMPLE and QUAD) is more pronounced than that of the covariance estimator; however, in high-dimensional markets, the impact of the covariance estimator is more significant than that of the mean estimator.

  The classical (MV) model with sample estimates, SCV+SM, is a poor performer, with only presence in the top 10 in NIFTY and S&P (3-month and 1-year out-of-sample periods) and FTSE (3-month out-of-sample period). The classical (GMV) model performs better in the TOPIX, but its performance is poor in other markets.

Table 5: Group B- The top 10 shrinkage-based MV and GMV portfolios arranged from highest to lowest ranking order as per their super efficiency scores when only return and risk-adjusted metrics are considered in the (DEA) model. Rankings are given for all six data sets. The Panels 1, 2, and 3, respectively, display the ranking when out-of-sample periods are set to 3-months, 6-months and 1-year in the rolling window scheme. Panel 4 describes the market-best and universal-best performer, along with the geometric mean of efficiency scores (GM of Efficiency) corresponding to each market-best performer.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Rank | DJ | NIFTY | FTSE | S&P | RUSSELL | TOPIX |
| Panel 1: Out-of-sample period= 3 months | | | | | | |
| 1 | COV2+QUAD | COV2+SM | LIS+SM | QIS+BOP | GMV+QIS | COVCOR+QUAD |
| 2 | COV2+SM | SCV+SM | COV2+SM | LS+BOP | QIS+QUAD | GMV+QIS |
| 3 | COV1+QUAD | SCV+QUAD | GIS+SM | QIS+SM | COV2+QUAD | QIS+JS |
| 4 | LIS+QUAD | COVDIAG+QUAD | AS+SM | SCV+BOP | QIS+SM | GMV+SCV |
| 5 | COV1+SM | COV2+QUAD | QIS+SM | QIS+JS | QIS+BS | COV2+QUAD |
| 6 | GIS+QUAD | COVDIAG+SM | LS+SM | COV2+SM | QIS+BOP | QIS+BS |
| 7 | QIS+QUAD | LS+QUAD | COV1+SM | LS+SM | QIS+JS | QIS+BOP |
| 8 | AS+QUAD | LS+SM | SCV+SM | QIS+BS | COV2+BS | QIS+SM |
| 9 | COV2+BS | COV1+SM | COVDIAG+SM | SCV+SM | COV2+SM | QIS+QUAD |
| 10 | LIS+SM | COV1+QUAD | LIS+QUAD | COV1+BOP | COV1+QUAD | GMV+COVMKT |
| Panel 2: Out-of-sample period= 6 months | | | | | | |
| 1 | COV2+SM | COVDIAG+QUAD | LIS+QUAD | COV2+SM | QIS+SM | QIS+QUAD |
| 2 | COV2+QUAD | LIS+SM | QIS+QUAD | COV2+BOP | QIS+JS | GMV+QIS |
| 3 | COV1+SM | COV2+SM | GIS+QUAD | COV2+QUAD | QIS+BS | GMV+SCV |
| 4 | COV1+QUAD | COV2+QUAD | COV2+QUAD | COV2+BS | QIS+BOP | QIS+BS |
| 5 | COV2+BS | GIS+QUAD | AS+QUAD | QIS+BOP | COV2+SM | QIS+JS |
| 6 | COVMKT+SM | GIS+SM | LIS+SM | COV2+JS | COV2+JS | QIS+BOP |
| 7 | LIS+SM | LIS+QUAD | GIS+SM | LS+BOP | COV2+BS | QIS+SM |
| 8 | QIS+SM | COVDIAG+SM | AS+QUAD | COV1+BOP | COV2+BOP | GMV+COVMKT |
| 9 | GIS+SM | SCV+QUAD | COV2+SM | QIS+SM | GMV+QIS | SCV+QUAD |
| 10 | COVMKT+QUAD | AS+SM | AS+SM | QIS+QUAD | QIS+QUAD | COVCOR+QUAD |
| Panel 3: Out-of-sample period= 1 year | | | | | | |
| 1 | COV2+QUAD | COV2+SM | LIS+SM | COV2+QUAD | QIS+QUAD | GMV+QIS |
| 2 | COV2+SM | AS+SM | GIS+SM | SCV+BOP | GMV+QIS | GMV+SCV |
| 3 | COV1+QUAD | AS+QUAD | QIS+SM | COV2+BOP | GMV+SCV | QIS+JS |
| 4 | COV1+SM | COV2+QUAD | GIS+QUAD | SCV+SM | GMV+COV2 | GMV+COV1 |
| 5 | LIS+QUAD | SCV+SM | LIS+QUAD | SCV+QUAD | QIS+SM | QIS+BS |
| 6 | QIS+QUAD | SCV+QUAD | QIS+QUAD | COV2+SM | QIS+JS | GMV+LS |
| 7 | GIS+QUAD | COV1+SM | AS+SM | COV2+BS | QIS+BS | GMV+COVMKT |
| 8 | QIS+SM | COV1+QUAD | AS+QUAD | SCV+QUAD | QIS+BOP | QIS+SM |
| 9 | LIS+SM | QIS+QUAD | COV2+SM | SCV+JS | GMV+COV1 | QIS+BOP |
| 10 | GIS+SM | QIS+SM | COV2+QUAD | LS+BOP | SCV+QUAD | SCV+JS |
| Panel 4: Best performing model | | | | | | |
| Market best | COV2+SM | COV2+SM | LIS+SM | COV2+SM | GMV+QIS | GMV+QIS |
| (GM of Efficiency) | (1.00165) | (1.00077) | (1.00241) | (1.01038) | (1.00473) | (1.01921) |
| Universal best | COV2+SM | COV2+SM | COV2+SM | COV2+SM | COV2+SM | COV2+SM |

### 6.3 Assessment for Group C

Table [6](https://arxiv.org/html/2601.20643v1#S6.T6 "Table 6 ‣ 6.3 Assessment for Group C ‣ 6 Result Discussion ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") organises the efficiency scores for the top 10 portfolios across all datasets and varying out-of-sample windows.
Table [6](https://arxiv.org/html/2601.20643v1#S6.T6 "Table 6 ‣ 6.3 Assessment for Group C ‣ 6 Result Discussion ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") concludes the following results.

* 1.

  DJ, NIFTY and FTSE: In DJ, the GMV+COV2 model shows consistent best performance, and among the (MV) models, the COV2+BOP achieves the highest performance. Across the NIFTY and FTSE datasets, portfolios from the GMV+LIS model perform best, followed by GMV+COVCOR, which is second best in NIFTY and GMV+GIS in FTSE. Notably, portfolios from the GMV models consistently outperformed others in risk mitigation, as evidenced by the presence of at least three GMV models within the top 10 ranks. In contrast, models based on sample mean and variance estimators exhibited poor performance.
* 2.

  S&P, RUSSELL, and TOPIX: Portfolio from the GMV+COV2 model is identified as the best-performing model over the three high-dimensional data sets, S&P, RUSSELL, and TOPIX. The second best choice is GMV+QIS over the data sets, S&P, and RUSSELL, whereas GMV+COVCOR is the second choice for TOPIX. Similar to the set of low-dimensional markets, here also portfolios from the GMV-based model consistently outperformed others in risk mitigation, as evidenced by the presence of at least six GMV models within the top 10 rankings across all periods. In contrast to low-dimensional datasets performance of GMV+SCV is quite impressive.
* 3.

  Varying out-of-sample periods: Portfolios from the model GMV+COV2 always show up in the top 10, except for a few times, like FTSE over 3-months and NIFTY over 1-year out-of-sample period. It actually ranks in the top three for the DJ, S&P, RUSSELL, and TOPIX, regardless of the length of the investment period. In light of this, GMV+COV2 becomes a universal-best performer.

  The next contender is GMV+QIS, which features very often in the top 10 for several markets (except to FTSE over 6-months and DJ, NIFTY & TOPIX over a 1-year out-of-sample period). Meanwhile, GMV+COVMKT is in the top 10 in all markets for all out-of-sample periods except for FTSE and NIFTY for one year. The SAMPLE estimate for covariance in the GMV framework i. e. GMV+SCV occurs exclusively in high-dimensional datasets.

  Considering group C primarily targets to risk-averse investors, GMV-based models are at the top of the rankings in almost all markets, especially FTSE, S&P, RUSSELL, and TOPIX.

Table 6: Group C- The top 10 shrinkage-based MV and GMV portfolios arranged from highest to lowest ranking order as per their super efficiency scores when only risk metrics are considered in the (DEA) model. Rankings are given for all six data sets. The Panels 1, 2, and 3, respectively, display the ranking when out-of-sample periods are set to 3-months, 6-months and 1-year in the rolling window scheme. Panel 4 describes the market-best and universal-best performer, along with the geometric mean of efficiency scores (GM of Efficiency) corresponding to each market-best performer.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Rank | DJ | NIFTY | FTSE | S&P | RUSSELL | TOPIX |
| Panel 1: Out-of-sample period= 3 months | | | | | | |
| 1 | GMV+COV2 | COVDIAG+BOP | QIS+BS | GMV+COV2 | GMV+COV2 | GMV+COV2 |
| 2 | COV2+BOP | GMV+LIS | GMV+LIS | GMV+QIS | GMV+QIS | GMV+COVMKT |
| 3 | GMV+COVMKT | GMV+COVMKT | GMV+COVCOR | GMV+COV1 | GMV+SCV | GMV+COVCOR |
| 4 | COVMKT+BOP | COVMKT+BOP | LIS+BS | GMV+LS | GMV+COVMKT | GMV+SCV |
| 5 | COVMKT+JS | GMV+COVCOR | GMV+GIS | GMV+SCV | GMV+COV1 | GMV+COV1 |
| 6 | GMV+AS | GMV+AS | COVCOR+JS | GMV+COVMKT | GMV+COVDIAG | GMV+QIS |
| 7 | GMV+QIS | COVCOR+JS | LIS+JS | GMV+COVDIAG | GMV+LS | COVCOR+JS |
| 8 | GMV+GIS | GMV+QIS | QIS+JS | QIS+BS | GMV+COVCOR | GMV+LS |
| 9 | GMV+LIS | GMV+GIS | GIS+JS | QIS+JS | COVMKT+SM | GMV+COVDIAG |
| 10 | LIS+BOP | GMV+COV2 | GMV+QIS | QIS+SM | COVMKT+JS | COVCOR+BS |
| Panel 2: Out-of-sample period= 6 months | | | | | | |
| 1 | GMV+COV2 | GMV+COVMKT | COVCOR+BS | GMV+COV2 | GMV+COV1 | GMV+COV2 |
| 2 | COVDIAG+BOP | GMV+LIS | GMV+COV2 | GMV+QIS | GMV+QIS | GMV+COVCOR |
| 3 | GMV+COVMKT | GMV+COVCOR | GMV+LIS | GMV+COV1 | GMV+COV2 | GMV+COVMKT |
| 4 | COVDIAG+JS | GMV+AS | GMV+GIS | QIS+JS | GMV+SCV | GMV+COV1 |
| 5 | GMV+AS | COVCOR+JS | GIS+JS | QIS+BS | GMV+COVMKT | GMV+SCV |
| 6 | COV2+JS | GMV+GIS | QIS+JS | GMV+COVMKT | GMV+LS | GMV+LS |
| 7 | QIS+BOP | GMV+COV2 | LIS+JS | GMV+SCV | GMV+COVDIAG | GMV+LS |
| 8 | COVMKT+BOP | GMV+QIS | LIS+JS | QIS+SM | GMV+COVCOR | COVCOR+BS |
| 9 | COV2+BOP | COVMKT+JS | COVMKT+JS | GMV+LS | COVDIAG+SM | GMV+COVDIAG |
| 10 | GMV+QIS | LIS+JS | GMV+AS | QIS+QUAD | COVDIAG+JS | GMV+QIS |
| Panel 3: Out-of-sample period= 1 year | | | | | | |
| 1 | COV2+BOP | GMV+LIS | GMV+COV2 | GMV+COV2 | GMV+SCV | GMV+COV2 |
| 2 | COVMKT+BOP | LIS+BOP | GMV+GIS | GMV+QIS | GMV+COV2 | GMV+COV1 |
| 3 | GMV+COV2 | COVMKT+BOP | GMV+LIS | GMV+COVCOR | GMV+QIS | GMV+COVCOR |
| 4 | GMV+COVMKT | AS+BOP | GMV+QIS | GMV+COV1 | GMV+COVMKT | GMV+SCV |
| 5 | COVMKT+JS | QIS+BOP | GMV+AS | GMV+COVMKT | GMV+COV1 | GMV+COVMKT |
| 6 | COV2+JS | SCV+BOP | GMV+COV1 | GMV+COVDIAG | GMV+LS | GMV+LS |
| 7 | GMV+COVCOR | GIS+BOP | LIS+JS | GMV+SCV | QIS+SM | COVCOR+JS |
| 8 | AS+BOP | COVDIAG+BOP | GMV+COVMKT | QIS+JS | QIS+JS | COVCOR+BS |
| 9 | QIS+BOP | GMV+COVCOR | GIS+JS | COVMKT+BS | QIS+BS | GMV+QIS |
| 10 | GIS+BOP | GMV+GIS | GMV+COVCOR | LS+BS | QIS+BOP | GMV+COVDIAG |
| Panel 4: Best performing model | | | | | | |
| Market best | GMV+COV2 | GMV+LIS | GMV+LIS | GMV+COV2 | GMV+COV2 | GMV+COV2 |
| (GM of Efficiency) | (1.00913) | (1.00355) | (1.00149) | (1.06506) | (1.01091) | (1.09658) |
| Universal best | GMV+COV2 | GMV+COV2 | GMV+COV2 | GMV+COV2 | GMV+COV2 | GMV+COV2 |

## 7 Comparison with Benchmark Models

Tables LABEL:tab4-LABEL:tab6 report the financial performance of the five optimal portfolios from benchmark PO models, the shrinkage-based market best performer, and the universal best performer across all the datasets. The tables also present super-efficiency scores of portfolios from groups A, B, and C, under the headings Efficiency-A, Efficiency-B, and Efficiency-C, respectively. The following conclusions are drawn from the tables.

* 1.

  DJ: The GMV+COV2 model, which is identified as both the market and universal best-performing method over the data set DJ for the groups A and C, demonstrates superior efficiency relative to all the benchmark PO models in all three out-of-sample periods. However, for group B, the COV2+SM model, which is selected as the top performer for DJ as well as the universal best performer, outperforms all except MM over the 3-month out-of-sample period.
* 2.

  NIFTY: The GMV+COV2, which is the market-best as well as the universal best-performing model for group A, demonstrates superior efficiency relative to benchmark models except for classical MV. For group B, the COV2+SM model, the market best and the universal best performer, outperforms all benchmark models in all out-of-sample periods. For group C, the market-best performer, GMV+LIS demonstrates superior efficiency relative to all benchmark models in all out-of-sample periods. The universal best-performing GMV+COV2 for group C is seen to outperform all benchmark models for the 6-month out-of-sample period. However, for the 3-month and 1-year out-of-sample periods, classical GMV has better super-efficiency.
* 3.

  FTSE: The market best performer for groups A and B over FTSE, the LIS+SM model performs better except for the CVaR model in group A for a 3-month out-of-sample period and MM over the 6-month out-of-sample period. LIS+SM exceeds the performance of classical MV, GMV, and SMAD in the 3-month and 6-month out-of-sample periods while surpassing all benchmarks in the 1-year out-of-sample period. The market best performer for group C, GMV+LIS, emerged as the superior model over all benchmark models in all out-of-sample periods.

  The GMV+COV2 model performs poorly with this data set. The FTSE market acted differently from other markets, ignoring GMV+COV2 for groups A and B altogether. It only chooses it for group A over the 1-year out-of-sample period. In fact, GMV+COV2 performs better than other benchmark models in group C. For group B, the universal best performer, COV2+SM, outperforms classical MV, GMV, and SMAD in both the 3-month and 6-month out-of-sample periods, and it also outperforms CVaR in the 1-year out-of-sample period.
* 4.

  S&P: For both groups A and C, the GMV+COV2 model, the best-performing model (market as well as universal), demonstrates a superior efficiency score relative to all the other benchmark models except for MM in group A for the case of the 1-year out-of-sample period. This indicates that the portfolio from the model GMV+COV2 is a robust choice for both groups A and C in this market.
  For Group B, the COV2+SM model (market best as well as the universal best performer) has a superior efficiency score relative to all the other benchmark models, except for classical MV in the 3-month out-of-sample period and MM in the 3-month and 1-year out-of-sample periods.
* 5.

  RUSSELL: For both groups A and B, the GMV+QIS model demonstrates its superior efficiency relative to all the other benchmark models except for MM for group A in the 3-month and 6-month out-of-sample periods and except for CVaR for the 1-year period. For Group B, GMV+QIS outperforms the benchmark models in all out-of-sample periods. On the other hand, for group C, the GMV+COV2 model (market best as well as the universal best performer) surpasses all the benchmark models except SMAD in all periods.

  The GMV+COV2, which is selected as the universal best-performer for group A, demonstrates its superior efficiency relative to all the other benchmark models in all 3 out-of-sample periods except for MM in the 3-month and 6-month out-of-sample periods. For group B, the universal best-performing model, COV2+SM, outperforms all benchmark models in the 3-month and 6-month out-of-sample periods. However, in the 1-year out-of-sample period, it outperforms only SMAD.
* 6.

  TOPIX: GMV+COVMKT (market best performer) model for group A is superior in efficiency relative to all benchmark models except SMAD in all periods. For Group B, GMV+QIS (the market’s best performer) outperforms all benchmark models in the 1-year out-of-sample period; however, in the 3-month and 6-month out-of-sample periods, MM surpasses it. The COV2+SM (universal best performer) surpasses only the CVaR portfolio in all periods. For group C, the market and universal best-performing model, GMV+COV2, exhibits superior efficiency than all benchmark models, except SMAD, in all periods. Additionally, classical GMV also performs well in the 3-month out-of-sample period. GMV+COV2, which is universally best for group A, demonstrates superior efficiency relative to CVaR and MM in all out-of-sample periods.

Table 7: Comparative study with benchmark models: Out-of-sample performance analysis of the selected market-best and universal-best performer with the five benchmark models when the out-of-sample period is set to 3-months. The comparison analysis is based on the efficiency scores from the (DEA) model with respect to all the groups of investors, A, B, and C. The analysis is presented for all six data sets.

| Efficiency | Benchmark Models | | | | | Shrinkage-based | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MV | CVaR | SMAD | MM | GMV | Group A | | Group B | | Group C | |
|  |  |  |  |  | Market | Universal | Market | Universal | Market | Universal |
| DJ | | | | | | GMV+ | GMV+ | COV2+ | COV2+ | GMV+ | GMV+ |
| COV2 | COV2 | SM | SM | COV2 | COV2 |
| Efficiency-A | 0.90130 | 0.84430 | 0.89500 | 0.95960 | 0.87950 | 1.27690 | 1.27690 | 1.04150 | 1.04150 | 1.27690 | 1.27690 |
| Efficiency-B | 0.88480 | 0.83390 | 0.85790 | 1.09390 | 0.82180 | 0.92950 | 0.92950 | 1.02690 | 1.02690 | 0.92950 | 0.92950 |
| Efficiency-C | 0.97210 | 0.96010 | 0.98260 | 0.83410 | 1.00420 | 1.17520 | 1.17520 | 0.96180 | 0.96180 | 1.17520 | 1.17520 |
| NIFTY | | | | | | GMV+ | GMV+ | COV2+ | COV2+ | GMV+ | GMV+ |
| COV2 | COV2 | SM | SM | LIS | COV2 |
| Efficiency-A | 1.01870 | 0.80790 | 0.99690 | 0.67870 | 1.00790 | 1.01110 | 1.01110 | 1.02650 | 1.02650 | 1.00140 | 1.01110 |
| Efficiency-B | 1.00170 | 0.86820 | 0.94960 | 0.77470 | 0.95200 | 0.94170 | 0.94170 | 1.01510 | 1.01510 | 0.93480 | 0.94170 |
| Efficiency-C | 0.96110 | 0.88080 | 0.99720 | 0.82930 | 1.00000 | 0.99980 | 0.99980 | 0.94610 | 0.94610 | 1.00690 | 0.99980 |
| FTSE | | | | | | LIS+ | GMV+ | LIS+ | COV2+ | GMV+ | GMV+ |
| SM | COV2 | SM | SM | LIS | COV2 |
| Efficiency-A | 0.96130 | 1.18540 | 0.68650 | 0.91260 | 0.78420 | 1.03530 | 0.89170 | 1.03530 | 1.00030 | 0.93070 | 0.89170 |
| Efficiency-B | 0.86940 | 1.17000 | 0.60550 | 1.02110 | 0.68320 | 0.90520 | 0.69100 | 0.90520 | 0.89530 | 0.71180 | 0.69100 |
| Efficiency-C | 0.98410 | 0.96050 | 1.01660 | 0.82180 | 0.99440 | 0.97930 | 0.99660 | 0.97930 | 0.98120 | 1.00910 | 0.99660 |
| S&P | | | | | | GMV+ | GMV+ | COV2+ | COV2+ | GMV+ | GMV+ |
| COV2 | COV2 | SM | SM | COV2 | COV2 |
| Efficiency-A | 1.04850 | 0.97660 | 0.93650 | 1.00310 | 0.97330 | 1.21110 | 1.21110 | 1.00940 | 1.00940 | 1.21110 | 1.21110 |
| Efficiency-B | 1.01920 | 0.97670 | 0.82180 | 1.06130 | 0.92560 | 0.94290 | 0.94290 | 0.99180 | 0.99180 | 0.94290 | 0.94290 |
| Efficiency-C | 0.96860 | 0.90110 | 1.10460 | 0.88390 | 0.99660 | 1.17890 | 1.17890 | 0.96740 | 0.96740 | 1.17890 | 1.17890 |
| RUSSELL | | | | | | GMV+ | GMV+ | GMV+ | COV2+ | GMV+ | GMV+ |
| QIS | COV2 | QIS | SM | COV2 | COV2 |
| Efficiency-A | 0.94610 | 0.94460 | 0.67640 | 1.04260 | 0.92680 | 1.05360 | 1.02220 | 1.05360 | 0.95180 | 1.02220 | 1.02220 |
| Efficiency-B | 0.95460 | 0.86830 | 0.55350 | 0.96210 | 0.92160 | 1.03980 | 0.98550 | 1.03980 | 0.97850 | 0.98550 | 0.98550 |
| Efficiency-C | 0.97210 | 1.03180 | 1.11860 | 0.98260 | 0.99490 | 1.01150 | 1.03720 | 1.01150 | 0.96000 | 1.03720 | 1.03720 |
| TOPIX | | | | | | GMV+ | GMV+ | GMV+ | COV2+ | GMV+ | GMV+ |
| COVMKT | COV2 | QIS | SM | COV2 | COV2 |
| Efficiency-A | 0.95760 | 0.78100 | 1.20080 | 0.90060 | 1.01880 | 1.10590 | 0.93390 | 1.01740 | 0.81200 | 0.93390 | 0.93390 |
| Efficiency-B | 0.99770 | 0.87150 | 0.89410 | 1.10420 | 1.00690 | 0.99820 | 0.87830 | 1.01720 | 0.91810 | 0.87830 | 0.87830 |
| Efficiency-C | 0.88060 | 0.73260 | 1.12630 | 0.73710 | 1.01180 | 1.05200 | 1.00520 | 0.99590 | 0.71280 | 1.00520 | 1.00520 |




Table 8:  Comparative study with benchmark models: Out-of-sample performance analysis of the selected market-best and universal-best performer with the five benchmark models when the out-of-sample period is set to 6-months. The comparison analysis is based on the efficiency scores from the (DEA) model with respect to all the groups of investors, A, B, and C. The analysis is presented for all six data sets.

| Efficiency | Benchmark Models | | | | | Shrinkage-based | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MV | CVaR | SMAD | MM | GMV | Group A | | Group B | | Group C | |
|  |  |  |  |  | Market | Universal | Market | Universal | Market | Universal |
| DJ | | | | | | GMV+ | GMV+ | COV2+ | COV2+ | GMV+ | GMV+ |
| COV2 | COV2 | SM | SM | COV2 | COV2 |
| Efficiency-A | 0.93380 | 0.86060 | 0.85850 | 0.83560 | 0.85890 | 1.15350 | 1.15350 | 1.02170 | 1.02170 | 1.15350 | 1.15350 |
| Efficiency-B | 0.90670 | 0.84710 | 0.82540 | 0.96550 | 0.80710 | 0.91440 | 0.91440 | 1.02110 | 1.02110 | 0.91440 | 0.91440 |
| Efficiency-C | 0.96820 | 0.96730 | 0.97630 | 0.82170 | 1.00070 | 1.16950 | 1.16950 | 0.96040 | 0.96040 | 1.16950 | 1.16950 |
| NIFTY | | | | | | GMV+ | GMV+ | COV2+ | COV2+ | GMV+ | GMV+ |
| COV2 | COV2 | SM | SM | LIS | COV2 |
| Efficiency-A | 1.02700 | 0.82510 | 0.96070 | 0.72300 | 1.00020 | 1.01180 | 1.01180 | 1.04140 | 1.04140 | 1.00590 | 1.01180 |
| Efficiency-B | 1.00270 | 0.88190 | 0.90930 | 0.80850 | 0.93720 | 0.93570 | 0.93570 | 1.02150 | 1.02150 | 0.93040 | 0.93570 |
| Efficiency-C | 0.95750 | 0.87820 | 0.98570 | 0.83690 | 1.00080 | 1.00300 | 1.00300 | 0.94480 | 0.94480 | 1.01160 | 1.00300 |
| FTSE | | | | | | LIS+ | GMV+ | LIS+ | COV2+ | GMV+ | GMV+ |
| SM | COV2 | SM | SM | LIS | COV2 |
| Efficiency-A | 0.94450 | 0.99260 | 0.72370 | 1.17560 | 0.82200 | 1.03310 | 0.93040 | 1.03310 | 1.01110 | 0.95060 | 0.93040 |
| Efficiency-B | 0.86940 | 0.94440 | 0.64770 | 1.32360 | 0.75190 | 0.94190 | 0.76160 | 0.94190 | 0.93290 | 0.78270 | 0.76160 |
| Efficiency-C | 0.97820 | 0.93350 | 1.00330 | 0.82450 | 0.99390 | 0.96740 | 1.00600 | 0.96740 | 0.97110 | 1.00590 | 1.00600 |
| S&P | | | | | | GMV+ | GMV+ | COV2+ | COV2+ | GMV+ | GMV+ |
| COV2 | COV2 | SM | SM | COV2 | COV2 |
| Efficiency-A | 0.97100 | 0.80400 | 0.83970 | 0.92030 | 0.86660 | 1.12720 | 1.12720 | 1.02030 | 1.02030 | 1.12720 | 1.12720 |
| Efficiency-B | 0.95600 | 0.77760 | 0.75420 | 0.92340 | 0.83330 | 0.90930 | 0.90930 | 1.00760 | 1.00760 | 0.90930 | 0.90930 |
| Efficiency-C | 0.98040 | 0.93410 | 1.07000 | 0.91700 | 0.99650 | 1.23600 | 1.23600 | 0.97680 | 0.97680 | 1.23600 | 1.23600 |
| RUSSELL | | | | | | GMV+ | GMV+ | GMV+ | COV2+ | GMV+ | GMV+ |
| QIS | COV2 | QIS | SM | COV2 | COV2 |
| Efficiency-A | 0.97680 | 0.96500 | 0.90880 | 1.06600 | 0.92960 | 1.05050 | 1.00530 | 1.05050 | 0.98350 | 1.00530 | 1.00530 |
| Efficiency-B | 0.98450 | 0.93570 | 0.80340 | 0.98830 | 0.92550 | 1.03020 | 0.97900 | 1.03020 | 1.01430 | 0.97900 | 0.97900 |
| Efficiency-C | 0.96500 | 0.95940 | 1.12200 | 0.96900 | 0.99190 | 1.01110 | 1.02690 | 1.01110 | 0.95800 | 1.02690 | 1.02690 |
| TOPIX | | | | | | GMV+ | GMV+ | GMV+ | COV2+ | GMV+ | GMV+ |
| COVMKT | COV2 | QIS | SM | COV2 | COV2 |
| Efficiency-A | 0.94820 | 0.78150 | 1.27930 | 0.88730 | 1.03010 | 1.07020 | 0.95500 | 1.02020 | 0.79580 | 0.95500 | 0.95500 |
| Efficiency-B | 0.99340 | 0.88540 | 0.95500 | 1.03170 | 1.00650 | 0.98510 | 0.85830 | 1.02370 | 0.93250 | 0.85830 | 0.85830 |
| Efficiency-C | 0.90300 | 0.80590 | 1.09630 | 0.82140 | 1.00970 | 1.03740 | 1.05020 | 0.99390 | 0.75480 | 1.05020 | 1.05020 |




Table 9:  Comparative study with benchmark models: Out-of-sample performance analysis of the selected market-best and universal-best performer with the five benchmark models when the out-of-sample period is set to 1-year. The comparison analysis is based on the efficiency scores from the (DEA) model with respect to all the groups of investors, A, B, and C. The analysis is presented for all six data sets.

| Efficiency | Benchmark Models | | | | | Shrinkage-based | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MV | CVaR | SMAD | MM | GMV | Group A | | Group B | | Group C | |
|  |  |  |  |  | Market | Universal | Market | Universal | Market | Universal |
| DJ | | | | | | GMV+ | GMV+ | COV2+ | COV2+ | GMV+ | GMV+ |
| COV2 | COV2 | SM | SM | COV2 | COV2 |
| Efficiency-A | 0.89950 | 0.80810 | 0.86700 | 0.75410 | 0.81420 | 1.10170 | 1.10170 | 0.99880 | 0.99880 | 1.10170 | 1.10170 |
| Efficiency-B | 0.88470 | 0.77960 | 0.81580 | 0.84220 | 0.76660 | 0.89340 | 0.89340 | 0.99770 | 0.99770 | 0.89340 | 0.89340 |
| Efficiency-C | 0.97090 | 0.98720 | 0.98500 | 0.86510 | 1.00050 | 1.14360 | 1.14360 | 0.96640 | 0.96640 | 1.14360 | 1.14360 |
| NIFTY | | | | | | GMV+ | GMV+ | COV2+ | COV2+ | GMV+ | GMV+ |
| COV2 | COV2 | SM | SM | LIS | COV2 |
| Efficiency-A | 1.02000 | 0.78310 | 0.98540 | 0.68520 | 1.00680 | 1.01090 | 1.01090 | 1.03370 | 1.03370 | 1.00320 | 1.01090 |
| Efficiency-B | 1.00160 | 0.84010 | 0.92960 | 0.75150 | 0.93530 | 0.93750 | 0.93750 | 1.01930 | 1.01930 | 0.93230 | 0.93750 |
| Efficiency-C | 0.95030 | 0.87610 | 0.99390 | 0.84290 | 1.00520 | 1.00110 | 1.00110 | 0.93990 | 0.93990 | 1.00780 | 1.00110 |
| FTSE | | | | | | LIS+ | GMV+ | LIS+ | COV2+ | GMV+ | GMV+ |
| SM | COV2 | SM | SM | LIS | COV2 |
| Efficiency-A | 0.96600 | 0.65380 | 0.86370 | 0.88880 | 0.96560 | 1.04740 | 0.98700 | 1.04740 | 0.98230 | 1.00030 | 0.98700 |
| Efficiency-B | 0.95680 | 0.69400 | 0.82820 | 0.99990 | 0.91650 | 1.03330 | 0.89620 | 1.03330 | 0.98160 | 0.91420 | 0.89620 |
| Efficiency-C | 0.95530 | 0.90230 | 0.98980 | 0.85390 | 0.99130 | 0.96090 | 1.00840 | 0.96090 | 0.95300 | 1.00740 | 1.00840 |
| S&P | | | | | | GMV+ | GMV+ | COV2+ | COV2+ | GMV+ | GMV+ |
| COV2 | COV2 | SM | SM | COV2 | COV2 |
| Efficiency-A | 1.02110 | 0.96600 | 0.77240 | 1.12390 | 0.96660 | 1.08540 | 1.08540 | 1.01230 | 1.01230 | 1.08540 | 1.08540 |
| Efficiency-B | 0.95780 | 0.93970 | 0.69460 | 1.09340 | 0.88640 | 0.92060 | 0.92060 | 0.97960 | 0.97960 | 0.92060 | 0.92060 |
| Efficiency-C | 0.97400 | 1.00900 | 1.04360 | 1.01480 | 1.01060 | 1.12450 | 1.12450 | 0.96170 | 0.96170 | 1.12450 | 1.12450 |
| RUSSELL | | | | | | GMV+ | GMV+ | GMV+ | COV2+ | GMV+ | GMV+ |
| QIS | COV2 | QIS | SM | COV2 | COV2 |
| Efficiency-A | 0.97450 | 1.02500 | 0.83650 | 1.00220 | 1.01170 | 1.01800 | 1.09560 | 1.01800 | 0.95750 | 1.09560 | 1.09560 |
| Efficiency-B | 0.97370 | 0.99760 | 0.73820 | 0.96840 | 1.00170 | 1.00310 | 0.99640 | 1.00310 | 0.95110 | 0.99640 | 0.99640 |
| Efficiency-C | 0.96160 | 0.97470 | 1.13230 | 1.01730 | 0.98310 | 1.00380 | 1.05580 | 1.00380 | 0.97150 | 1.05580 | 1.05580 |
| TOPIX | | | | | | GMV+ | GMV+ | GMV+ | COV2+ | GMV+ | GMV+ |
| COVMKT | COV2 | QIS | SM | COV2 | COV2 |
| Efficiency-A | 0.89490 | 0.77110 | 1.19100 | 0.74380 | 1.04800 | 1.07530 | 0.99150 | 1.02810 | 0.76440 | 0.99150 | 0.99150 |
| Efficiency-B | 0.92040 | 0.82080 | 0.89660 | 0.79050 | 1.00300 | 0.98320 | 0.90810 | 1.04180 | 0.83670 | 0.90810 | 0.90810 |
| Efficiency-C | 0.92140 | 0.87940 | 1.15180 | 0.90570 | 1.01240 | 1.01060 | 1.06570 | 0.98240 | 0.80590 | 1.06570 | 1.06570 |

In closing, we present the box plot of efficiencies for the benchmark models (MV & GMV with sample estimates, CVaR, MAD, MM) and the universal best-performing shrinkage models across all three groups in Figure [1](https://arxiv.org/html/2601.20643v1#S7.F1 "Figure 1 ‣ 7 Comparison with Benchmark Models ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"). The analysis includes 18 efficiency scores (6 markets × 3 out-of-sample periods) for each of the five benchmark models and the universal best-performing shrinkage model (GMV+COV2 for Groups A and B, and COV2+SM for Group C). Observations from the Figure [1](https://arxiv.org/html/2601.20643v1#S7.F1 "Figure 1 ‣ 7 Comparison with Benchmark Models ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions") are described in the summary points below.

![Refer to caption](A.jpg)


(a) Group A

![Refer to caption](B.jpg)


(b) Group B

![Refer to caption](C.jpg)


(c) Group C

Figure 1: Efficiency scores distribution framed over different datasets and varying out-of-sample period size of the five benchmark models (MV & GMV with sample estimates, CVaR, MAD, MM) and the universal best-performing models corresponding to the groups A, B, and C.

Summary points

* 1.

  For group A, when all financial metrics are considered, the model GMV+COV2 performs well over the majority of the data sets, DJ, NIFTY, S&P, and RUSSELL, while GMV+COVMKT for the TOPIX and LIS+SM for the FTSE. The GMV+COV2 model dominates all the benchmark models in terms of efficiency score as observed in Figure [1(a)](https://arxiv.org/html/2601.20643v1#S7.F1.sf1 "In Figure 1 ‣ 7 Comparison with Benchmark Models ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* 2.

  The investigation could not identify a single shrinkage-based model for group B that performed better. The COV2+SM model demonstrates superior performance in the DJ, NIFTY, and S&P markets; LIS+SM excels in the FTSE; and GMV+QIS in the RUSSELL and TOPIX. As noted in Figure [1(b)](https://arxiv.org/html/2601.20643v1#S7.F1.sf2 "In Figure 1 ‣ 7 Comparison with Benchmark Models ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"), COV2+SM surpasses CVaR, SMAD, and classical GMV portfolio models; however, the MM model outperforms it, while the conventional mean-variance model is comparable.
* 3.

  Analysis of group C reveals the predominance of GMV models wherein the GMV+COV2 performs the best, followed by GMV+QIS and GMV+COVMKT. The universal best-performing GMV+COV2 model is seen to outperform the benchmark PO models, MV, GMV, CVaR, and MM, as illustrated in Figure [1(c)](https://arxiv.org/html/2601.20643v1#S7.F1.sf3 "In Figure 1 ‣ 7 Comparison with Benchmark Models ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"). The performance of SMAD is comparable to its performance in high-dimensional datasets, primarily due to its low turnover ratio. With the dominance of GMV models for group C investors, the classical GMV model with sample covariance performs poorly in low-dimensional markets (DJ, NIFTY, FTSE) while it fits well for the S&P 500, RUSSELL, and TOPIX.
* 4.

  COV2 places the most effective shrinkage covariance estimators irrespective of the profile of investors and investment duration as GMV+COV2 ranks universal-best performer for the groups A and C while COV2+SM becomes universal-best for the group B. The next performance is shown by the covariance estimator QIS, as it frequently appears in top positions either with GMV or MV.
* 5.

  It’s intriguing that the sample mean SM dominates other shrinkage mean estimators as the (MV) model based on SM, i. e, COV2+SM, becomes universal-best for group B. When the non-GMV model was the first choice for the FTSE market in group A, it was the sample mean-based MV model, which was LIS+SM. In fact, LIS+SM is the best choice for the data set FTSE over both groups, A and B. But the sample mean is never a good choice when combined with the sample covariance for any market and for any group of investors.
* 6.

  In summary, certain shrinkage-based portfolios exhibit superior performance compared to the benchmark models across the three groups: A, B, and C. The GMV+COV2, which performs best for groups A and C, outperforms over several data sets except for FTSE (for group A & for group C over 3-months out-of-sample period) and TOPIX (for group A) markets. On the other hand, the performance of shrinkage is more reliant on the underlying market structure for group B, i. e. return-focused investors.

## 8 Conclusions

This research conducts an extensive examination of Markowitz portfolio optimization using mean-variance (MV) and global mean-variance (GMV) modeling approaches, integrated with several widely-used shrinkage estimation techniques for both the mean vector and covariance matrix. The analysis employs five shrinkage estimators for the mean and eleven for the covariance matrix. Performance evaluation is conducted across six international datasets, including three high-dimensional cases where the number of assets (pp) exceeds the number of time observations (nn). This configuration yields sixty-six portfolio combinations for datasets with n>pn>p, and forty-eight combinations when n<pn<p.

Given that there are numerous portfolios to compare, we suggest utilizing a super-efficiency data envelopment analysis (DEA) model with portfolios as decision-making units (DMUs). The input and output for the DEA model are various financial metrics, such as mean return, risk measures, and reward-risk ratios. The study analyses three variations of out-of-sample window sizes: 3-months, 6-months, and 1-year, within the rolling window framework. Additionally, we categorize three groups: A, B, and C, based on the return-risk profile of investors, and perform a (DEA) ranking across the three groups. For every market and for every group, we select the two optimal portfolios: (i) the market best performer and (ii) the universal best performer.

The empirical analysis concludes with many interesting facts: (1) Though the choice is more dependent on the underlying market, the GMV model with the Ledoit-Wolf method of two-parameter shrinkage covariance (COV2) represents an optimal strategy for a broad spectrum of investors, though preferences shift for those prioritizing higher returns. (2) The (MV) model with COV2, together with the sample mean (SM), is more appropriate for return-seeking investors. (3) Both the models (GMV + COV2 and COV2 + SM) exhibit enhanced performance relative to conventional benchmarks such as Markowitz portfolios with sample estimates, MiniMax, CVaR, GMV, and SMAD. (4) The shrinkage covariance (COV2) often appears in top choices for all groups of investors and over several markets, establishing it as a preferred covariance estimation method, while the sample mean (SM) shines in the mean estimation category. (5) The sample mean together with the sample covariance accounts for poor out-of-sample results, rendering it an undesirable option.

In summary, this research establishes a foundation for gaining deeper insights into how particular shrinkage models perform across varying market environments. Future research could build upon this work by investigating the effectiveness of these models in developed versus emerging markets, or in periods of stability versus periods of high volatility.

## Data Availability

The data sources used in this study are referenced within the article. The intermediate findings of our empirical analysis are publicly available on GitHub:
  
https://github.com/rupendrayadav19401/Shrinkage-PO.

## Acknowledgment

The first author is grateful for the financial support received from the Council of Scientific and Industrial Research (CSIR), India (award number 09/0086(17076)/2023-EMR-I) for conducting research work. The DST-FIST grant SR/FST/MS-1/2019/45 is acknowledged for the computing facility in the department at IIT Delhi.

## Appendix A Benchmark Portfolio Optimization Models

For the uniform probability vector Pj=1n,j=1,…,n,P\_{j}=\frac{1}{n},\;j=1,\ldots,n,, following are the modeling structure of the three benchmark PO models considered for the comparison analysis:

### SMAD (Semi Mean Absolute Deviation) Model [[13](https://arxiv.org/html/2601.20643v1#bib.bib62 "A reformulation of a mean-absolute deviation portfolio optimization model.")]

The model introduces auxiliary variables dj∈ℝd\_{j}\in\mathbb{R} to represent absolute deviations from the mean portfolio return. The model is formulated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | (SMAD)min𝒙∈X,d\displaystyle\text{(SMAD)}\quad\min\_{\bm{x}\in X,\,d}\quad | 1n​∑j=1ndj,\displaystyle\frac{1}{n}\sum\_{j=1}^{n}d\_{j}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | dj+𝒓j⊤​𝒙≥𝒓¯⊤​𝒙,∀j=1,…,n,\displaystyle d\_{j}+\bm{r}\_{j}^{\top}\bm{x}\geq\bm{\bar{r}}^{\top}\bm{x},\quad\forall\;j=1,\ldots,n, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | dj≥0,∀j=1,…,n.\displaystyle d\_{j}\geq 0,\quad\forall\;j=1,\ldots,n. |  |

### CVaR (Conditional Value-at-Risk) Model [[31](https://arxiv.org/html/2601.20643v1#bib.bib63 "Optimization of conditional value-at-risk")]

Let α∈(0,1)\alpha\in(0,1) denote the confidence level. The model introduces β∈ℝ\beta\in\mathbb{R} as the Value-at-Risk (VaR) threshold and uj∈ℝu\_{j}\in\mathbb{R} as auxiliary variables for losses exceeding the VaR. The CVaR model is formulated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | (CVaR)min𝒙∈X,β,u\displaystyle\text{(CVaR)}\quad\min\_{\bm{x}\in X,\,\beta,\,u}\quad | β+1α​n​∑j=1nuj−𝒓¯⊤​𝒙,\displaystyle\beta+\frac{1}{\alpha n}\sum\_{j=1}^{n}u\_{j}-\bm{\bar{r}^{\top}x}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | uj≥0,∀j=1,…,n,\displaystyle u\_{j}\geq 0,\quad\forall\;j=1,\ldots,n, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | uj+β+𝒓𝒋⊤​𝒙≥0,∀j=1,…,n.\displaystyle u\_{j}+\beta+\bm{r\_{j}^{\top}x}\geq 0,\quad\forall\;j=1,\ldots,n. |  |

### MiniMax Model [[9](https://arxiv.org/html/2601.20643v1#bib.bib64 "Portfolio optimization under a minimax rule")]

It introduces an auxiliary variable y∈ℝy\in\mathbb{R} representing the minimum portfolio return across all scenarios. The goal is to maximize the worst-case scenario return, formulated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | (MM)min𝒙∈X,y\displaystyle\text{(MM)}\quad\min\_{\bm{x}\in X,\,y}\quad | −y−𝒓¯⊤​𝒙,\displaystyle-y-\bm{\bar{r}^{\top}x}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | 𝒓𝒋⊤​𝒙≥y,∀j=1,…,n.\displaystyle\bm{r\_{j}^{\top}x}\geq y,\quad\forall\;j=1,\ldots,n. |  |

## References

* [1]
  P. Andersen and N. C. Petersen (1993)
  A procedure for ranking efficient units in data envelopment analysis.
  Management Science 39 (10),  pp. 1261–1264.
  Cited by: [§4](https://arxiv.org/html/2601.20643v1#S4.p1.1 "4 Super-efficiency DEA Model ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [2]
  J. Bai and S. Shi (2011)
  Estimating high dimensional covariance matrices and its applications..
  Annals of Economics & Finance 12 (2).
  Cited by: [item 1.](https://arxiv.org/html/2601.20643v1#S3.I2.ix1.p1.5 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [3]
  Z. Bai, J. W. Silverstein, et al. (2010)
  Spectral analysis of large dimensional random matrices.
   Springer.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p5.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [4]
  M. J. Best and R. R. Grauer (2015)
  On the sensitivity of mean-variance-efficient portfolios to changes in asset means: some analytical and computational results.
  The Review of Financial Studies 4 (2),  pp. 315–342.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p4.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [5]
  T. Bodnar, H. Dette, and N. Parolya (2019)
  Testing for independence of large dimensional vectors.
  The Annals of Statistics 47 (5),  pp. 2977–3008.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p5.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [6]
  T. Bodnar, S. Dmytriv, Y. Okhrin, D. Otryakhin, and N. Parolya (2025)
  High-dimensional portfolio selection with HDShOP package.
  The European Journal of Finance,  pp. 1–23 .
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p9.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [§3.2](https://arxiv.org/html/2601.20643v1#S3.SS2.p1.1 "3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [7]
  T. Bodnar, A. K. Gupta, and N. Parolya (2014)
  On the strong convergence of the optimal linear shrinkage estimator for large dimensional covariance matrix.
  Journal of Multivariate Analysis 132,  pp. 215–228.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p8.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 1.](https://arxiv.org/html/2601.20643v1#S3.I2.ix1.p1.8 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 1.](https://arxiv.org/html/2601.20643v1#S3.I2.ix1.p2.5 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.3.2.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [8]
  T. Bodnar, O. Okhrin, and N. Parolya (2019)
  Optimal shrinkage estimator for high-dimensional mean vector.
  Journal of Multivariate Analysis 170,  pp. 63–79.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p7.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 4.](https://arxiv.org/html/2601.20643v1#S3.I1.ix4.p1.6 "In 3.1 Shrinkage Estimator for Mean ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 4.](https://arxiv.org/html/2601.20643v1#S3.I1.ix4.p1.7 "In 3.1 Shrinkage Estimator for Mean ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.5.4.1 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [9]
  X. Cai, K. Teo, X. Yang, and X. Y. Zhou (2000)
  Portfolio optimization under a minimax rule.
  Management Science 46 (7),  pp. 957–972.
  Cited by: [Appendix A](https://arxiv.org/html/2601.20643v1#A1.SSx3 "MiniMax Model [9] ‣ Appendix A Benchmark Portfolio Optimization Models ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [§1.2](https://arxiv.org/html/2601.20643v1#S1.SS2.p10.1 "1.2 Objective and Approach ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 5.](https://arxiv.org/html/2601.20643v1#S5.I1.i3.I1.ix5.p1.1 "In item 3 ‣ 5.3 Methodology ‣ 5 Data and Empirical Set-up ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [10]
  A. Charnes, W.W. Cooper, and E. Rhodes (1978)
  Measuring the efficiency of decision making units.
  European Journal of Operational Research 2 (6),  pp. 429–444.
  Cited by: [§3.2](https://arxiv.org/html/2601.20643v1#S3.SS2.p6.1 "3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [11]
  V. K. Chopra, W. T. Ziemba, et al. (1993)
  The effect of errors in means, variances, and covariances on optimal portfolio choice.
  Journal of Portfolio Management 19 (2),  pp. 6–11.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p2.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p4.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [12]
  V. DeMiguel, L. Garlappi, and R. Uppal (2009)
  Optimal versus naive diversification: how inefficient is the 1/n portfolio strategy?.
  The Review of Financial Studies 22 (5),  pp. 1915–1953.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p3.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p5.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [13]
  C. D. Feinstein and M. N. Thapa (1993)
  A reformulation of a mean-absolute deviation portfolio optimization model..
  Management Science 39 (12),  pp. 1552 – 1553.
  Cited by: [Appendix A](https://arxiv.org/html/2601.20643v1#A1.SSx1 "SMAD (Semi Mean Absolute Deviation) Model [13] ‣ Appendix A Benchmark Portfolio Optimization Models ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [§1.2](https://arxiv.org/html/2601.20643v1#S1.SS2.p10.1 "1.2 Objective and Approach ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 3.](https://arxiv.org/html/2601.20643v1#S5.I1.i3.I1.ix3.p1.1 "In item 3 ‣ 5.3 Methodology ‣ 5 Data and Empirical Set-up ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [14]
  R. C. Green and B. Hollifield (1992)
  When will mean-variance efficient portfolios be well diversified?.
  The Journal of Finance 47 (5),  pp. 1785–1809.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p3.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [15]
  H. Y. Hiroshi Konno (1991)
  Mean-absolute deviation portfolio optimization model and its applications to Tokyo stock market.
  Management Science 37,  pp. 519–531.
  Cited by: [§1.2](https://arxiv.org/html/2601.20643v1#S1.SS2.p10.1 "1.2 Objective and Approach ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [16]
  W. James, C. Stein, et al. (1961)
  Estimation with quadratic loss.
  In Proceedings of the fourth Berkeley symposium on mathematical statistics and probability,
  Vol. 1,  pp. 361–379.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p7.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 1.](https://arxiv.org/html/2601.20643v1#S3.I1.ix1.p1.2 "In 3.1 Shrinkage Estimator for Mean ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.3.2.1 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [17]
  J. D. Jobson and R. M. Korkie (1981)
  Putting markowitz theory to work.
  The Journal of Portfolio Management 7 (4),  pp. 70–74.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p3.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [18]
  P. Jorion (1986)
  Bayes-Stein estimation for portfolio analysis.
  Journal of Financial and Quantitative Analysis 21 (3),  pp. 279–292.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p7.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 2.](https://arxiv.org/html/2601.20643v1#S3.I1.ix2.p1.1 "In 3.1 Shrinkage Estimator for Mean ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.4.3.1 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [19]
  O. Ledoit and M. Wolf (2003)
  Improved estimation of the covariance matrix of stock returns with an application to portfolio selection.
  Journal of empirical finance 10 (5),  pp. 603–621.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p8.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item (2a)](https://arxiv.org/html/2601.20643v1#S3.I2.ix2.I1.ix1.p1.3 "In item 2. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item (2b)](https://arxiv.org/html/2601.20643v1#S3.I2.ix2.I1.ix2.p1.4 "In item 2. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item (2c)](https://arxiv.org/html/2601.20643v1#S3.I2.ix2.I1.ix3.p1.1.1 "In item 2. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 2.](https://arxiv.org/html/2601.20643v1#S3.I2.ix2.p1.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.4.3.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.5.4.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.6.5.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [20]
  O. Ledoit and M. Wolf (2004)
  A well-conditioned estimator for large-dimensional covariance matrices.
  Journal of multivariate analysis 88 (2),  pp. 365–411.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p8.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 1.](https://arxiv.org/html/2601.20643v1#S3.I2.ix1.p1.5 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item (2d)](https://arxiv.org/html/2601.20643v1#S3.I2.ix2.I1.ix4.p1.2.1 "In item 2. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item (2e)](https://arxiv.org/html/2601.20643v1#S3.I2.ix2.I1.ix5.p1.1.1 "In item 2. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 2.](https://arxiv.org/html/2601.20643v1#S3.I2.ix2.p1.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.7.6.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.8.7.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [21]
  O. Ledoit and M. Wolf (2012)
  Nonlinear shrinkage estimation of large-dimensional covariance matrices.
  The Annals of Statistics 40 (2),  pp. 1024–1060.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p9.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [22]
  O. Ledoit and M. Wolf (2015)
  Spectrum estimation: a unified framework for covariance matrix estimation and PCA in large dimensions.
  Journal of Multivariate Analysis 139,  pp. 360–384.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p9.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [23]
  O. Ledoit and M. Wolf (2020)
  Analytical nonlinear shrinkage of large-dimensional covariance matrices.
  The Annals of Statistics 48 (5),  pp. 3043–3065.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p9.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 4.](https://arxiv.org/html/2601.20643v1#S3.I2.ix4.p1.4 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.12.11.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [24]
  O. Ledoit and M. Wolf (2021)
  Shrinkage estimation of large covariance matrices: keep it simple, statistician?.
  Journal of Multivariate Analysis 186,  pp. 104796.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p9.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item (3a)](https://arxiv.org/html/2601.20643v1#S3.I2.ix3.I2.ix1.p1.7 "In item 3. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 3.](https://arxiv.org/html/2601.20643v1#S3.I2.ix3.p1.1 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.9.8.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [25]
  O. Ledoit and M. Wolf (2022)
  Quadratic shrinkage for large covariance matrices.
  Bernoulli 28 (3),  pp. 1519–1547.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p9.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item (3b)](https://arxiv.org/html/2601.20643v1#S3.I2.ix3.I2.ix2.p1.1 "In item 3. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item (3c)](https://arxiv.org/html/2601.20643v1#S3.I2.ix3.I2.ix3.p1.2 "In item 3. ‣ 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 3.](https://arxiv.org/html/2601.20643v1#S3.I2.ix3.p1.1 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.10.9.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.11.10.2 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [26]
  Y. Lee, M. J. Kim, J. H. Kim, J. R. Jang, and W. C. Kim (2020)
  Sparse and robust portfolio selection via semi-definite relaxation.
  Journal of the Operational Research Society 71 (5),  pp. 687–699.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p5.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [27]
  H. Markowitz (1952)
  PORTFOLIO selection.
  The Journal of Finance 7 (1),  pp. 77–91.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p1.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 1.](https://arxiv.org/html/2601.20643v1#S5.I1.i3.I1.ix1.p1.1 "In item 3 ‣ 5.3 Methodology ‣ 5 Data and Empirical Set-up ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 2.](https://arxiv.org/html/2601.20643v1#S5.I1.i3.I1.ix2.p1.1 "In item 3 ‣ 5.3 Methodology ‣ 5 Data and Empirical Set-up ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [28]
  H. Martin (2009)
  Asset allocation and risk management.
  Note: <http://www.columbia.edu/~mh2078/QRM-assetallocation.pdf>Lecture notes: IEOR E4602: Quantitative Risk Management
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p4.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [29]
  R. O. Michaud and T. Ma (2001)
  Efficient asset management: a practical guide to stock portfolio optimization and asset allocation.
   Oxford University Press.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p3.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [30]
  T. A. T. Minh Tran (2025)
  Enhancing portfolio optimization in emerging markets: a cross-validation multi-target shrinkage approach.
  Results in Control and Optimization 21,  pp. 100611.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p9.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [31]
  R. T. Rockafellar and S. Uryasev (2000)
  Optimization of conditional value-at-risk.
  Journal of Risk 2,  pp. 21–42.
  Cited by: [Appendix A](https://arxiv.org/html/2601.20643v1#A1.SSx2 "CVaR (Conditional Value-at-Risk) Model [31] ‣ Appendix A Benchmark Portfolio Optimization Models ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [§1.2](https://arxiv.org/html/2601.20643v1#S1.SS2.p10.1 "1.2 Objective and Approach ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 4.](https://arxiv.org/html/2601.20643v1#S5.I1.i3.I1.ix4.p1.1 "In item 3 ‣ 5.3 Methodology ‣ 5 Data and Empirical Set-up ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [32]
  B. Scherer (2007)
  Can robust portfolio optimisation help to build better portfolios?.
  Journal of Asset Management 7 (6),  pp. 374–387.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p5.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [33]
  C. Stein (1975)
  Estimation of a covariance matrix, rietz lecture.
  39th Annual Meeting IMS, Atlanta, GA.
  Cited by: [item 3.](https://arxiv.org/html/2601.20643v1#S3.I2.ix3.p1.1 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [34]
  C. Stein (1977)
  Lectures on the theory of estimation of many parameters.
  Studies in the Statistical Theory of Estimation I 74,  pp. 4–65.
  Cited by: [item 3.](https://arxiv.org/html/2601.20643v1#S3.I2.ix3.p1.1 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [35]
  C. Stein (1986)
  Lectures on the theory of estimation of many parameters.
  Journal of Soviet Mathematics 34 (1),  pp. 1373–1403.
  Cited by: [item 3.](https://arxiv.org/html/2601.20643v1#S3.I2.ix3.p1.1 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").
* [36]
  C. Wang, T. Tong, L. Cao, and B. Miao (2014)
  Non-parametric shrinkage mean estimation for quadratic loss functions with unknown covariance matrices.
  Journal of Multivariate Analysis 125,  pp. 222–232.
  Cited by: [§1.1](https://arxiv.org/html/2601.20643v1#S1.SS1.p7.1 "1.1 Motivation and Background ‣ 1 Introduction ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [item 3.](https://arxiv.org/html/2601.20643v1#S3.I1.ix3.p1.1 "In 3.1 Shrinkage Estimator for Mean ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions"),
  [Table 1](https://arxiv.org/html/2601.20643v1#S3.T1.8.6.5.1 "In 3.2 Shrinkage Estimators for Covariance Matrix ‣ 3 Shrinkage Estimators ‣ Shrinkage Estimators for Mean and Covariance: Evidence on Portfolio Efficiency Across Market Dimensions").