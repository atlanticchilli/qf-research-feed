---
authors:
- Koichiro Moriya
- Akihiko Noda
doc_id: arxiv:2601.21272v1
family_id: arxiv:2601.21272
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic
  Regression Models
url_abs: http://arxiv.org/abs/2601.21272v1
url_html: https://arxiv.org/html/2601.21272v1
venue: arXiv q-fin
version: 1
year: 2026
---


Koichiro Moriyaa and Akihiko Nodab
a Graduate School of Media and Governance, Keio University, 5322 Endo, Fujisawa, Kanagawa 252-0882, Japan
b School of Commerce, Meiji University, 1-1 Kanda-Surugadai, Chiyoda-ku, Tokyo 101-8301, Japan
Corresponding Author. E-mail: moriya.koichiro@keio.jp, Tel/Fax: +81-466-49-3406.

(This Version: )

Abstract: This paper proposes a new multivariate model specification test that generalizes Durbin regression to a seemingly unrelated regression (SUR) framework and reframes the Durbin approach as a GLS-class estimator. The proposed estimator explicitly models cross-equation dependence and the joint second-order dynamics of regressors and disturbances. It remains consistent under a comparatively weak dependence condition in which conventional OLS- and GLS-based estimators can be inconsistent, and it is asymptotically efficient under stronger conditions. Monte Carlo experiments indicate that the associated Wald test achieves improved size control and competitive power in finite samples, especially when combined with a bootstrap-based bias correction. An empirical application further illustrates that the proposed procedure delivers stable inference and is practically useful for multi-equation specification testing.

Keywords: Multivariate Model; Model Specification; Durbin Regression; GLS

JEL Classification Numbers: C12; C32; C38; C58; G11.

## 1 Introduction

Economic phenomena typically involve multiple outcome variables that are simultaneously determined and interact with one another. Economists commonly employ specification tests within multivariate regression frameworks to assess the validity of economic theories. A prevalent feature of these frameworks is the correlation of error terms across equations, reflecting underlying economic mechanisms. This correlation arises in various contexts, including analyses involving firms, individuals, and countries. For instance, technological spillovers within industries frequently lead to correlated regression residuals in firm-level analyses (e.g., Bernstein and Nadiri ([1989](https://arxiv.org/html/2601.21272v1#bib.bib2130 "Research and development and intra-industry spillovers: an empirical application of dynamic duality")); Jaffe ([1989](https://arxiv.org/html/2601.21272v1#bib.bib2131 "Technological opportunity and spillovers of r&d: evidence from firms’ patents,profits, and market value")); Peremans and Aelst ([2018](https://arxiv.org/html/2601.21272v1#bib.bib2121 "Robust iference for semingly unrelated regression models"))). Similarly, panel data studies involving individuals or countries often encounter error dependence resulting from unobserved heterogeneity or coordinated policy responses (e.g., Pesaran ([2006](https://arxiv.org/html/2601.21272v1#bib.bib2132 "Estimation and inference in large heterogeneous panels with a multifactor error structure")); Martin et al. ([2007](https://arxiv.org/html/2601.21272v1#bib.bib2122 "The market for elective surgery: joint estimation of supply and demand")); Baltagi and Bresson ([2011](https://arxiv.org/html/2601.21272v1#bib.bib2133 "Maximum likelihood estimation and lagrange multiplier tests for panelseemingly unrelated regressions with spatial lag and spatial errors: anapplication to hedonic housing prices in paris"))). Ignoring these cross-equation dependencies by conducting specification tests on an equation-by-equation basis can result in size distortions and misleading inferences, as demonstrated by Breusch and Pagan ([1980](https://arxiv.org/html/2601.21272v1#bib.bib2112 "The lagrange multiplier test and its applications to model specification in econometrics")), Zhou ([1991](https://arxiv.org/html/2601.21272v1#bib.bib2129 "Small sample tests of portfolio efficiency")), and Pesaran and Yamagata ([2008](https://arxiv.org/html/2601.21272v1#bib.bib2128 "Testing slope homogeneity in large panels")). Consequently, multivariate specification tests explicitly accounting for error covariance structures are essential for rigorous model evaluation.

These error dependencies become especially pronounced during periods of significant uncertainty, such as financial crises, wars, or natural disasters (e.g., Pesaran et al. ([2004](https://arxiv.org/html/2601.21272v1#bib.bib2141 "Modeling regional interdependencies using a global error-correcting macroeconometric model")); Blomberg et al. ([2004](https://arxiv.org/html/2601.21272v1#bib.bib2143 "The macroeconomic consequences of terrorism")); Barrios et al. ([2010](https://arxiv.org/html/2601.21272v1#bib.bib2142 "Global inflation"))). For example, numerous studies documented substantial residual correlations among financial assets during the Global Financial Crisis and the COVID-19 pandemic (e.g., Diebold and Yilmaz ([2009](https://arxiv.org/html/2601.21272v1#bib.bib2052 "Measuring financial asset return and volatility spillovers, with application to global equity markets")); Billio et al. ([2012](https://arxiv.org/html/2601.21272v1#bib.bib2144 "Econometric measures of connectedness and systemic risk in the finance and insurance sectors")); Zhang et al. ([2020](https://arxiv.org/html/2601.21272v1#bib.bib2145 "Financial markets under the global pandemic of covid-19"))). These findings imply that ignoring covariance structures among asset returns may lead to incorrect interpretations of their interrelationships. Therefore, appropriate multivariate specification tests remain critical for accurately validating asset pricing models. Despite this, empirical studies frequently employ the test developed by Gibbons et al. ([1989](https://arxiv.org/html/2601.21272v1#bib.bib1878 "A test of the efficiency of a given portfolio")) (GRS test), which assumes independently and identically distributed multivariate normal residuals. However, empirical evidence shows that residuals often exhibit fat tails, skewness, and other departures from normality, even after controlling for risk factors (e.g., Cont ([2001](https://arxiv.org/html/2601.21272v1#bib.bib2110 "Empirical properties of asset returns: stylized facts and statistical issues")); Harvey and Siddique ([2002](https://arxiv.org/html/2601.21272v1#bib.bib2109 "Conditional skewness in asset pricing tests")); Huang et al. ([2012](https://arxiv.org/html/2601.21272v1#bib.bib2108 "Extreme downside risk and expected stock returns"))). Indeed, Affleck-Graves and McDonald ([1989](https://arxiv.org/html/2601.21272v1#bib.bib1501 "Nonnormalities and tests of asset pricing theories")) and Zhou ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1837 "Asset-pricing tests under alternative distributions")) demonstrate that violations of normality assumptions significantly inflate the Type I error rate of the GRS test.

To tackle heteroskedasticity and autocorrelation without imposing stringent distributional assumptions, econometricians developed heteroskedasticity- and autocorrelation-consistent (HAC) robust tests, initially proposed by Newey and West ([1987](https://arxiv.org/html/2601.21272v1#bib.bib233 "A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix"), [1994](https://arxiv.org/html/2601.21272v1#bib.bib1903 "Automatic lag selection in covariance matrix estimation")) and Andrews ([1991](https://arxiv.org/html/2601.21272v1#bib.bib13 "Heteroskedasticity and autocorrelation consistent covariance matrix estimation")). However, conventional HAC-based tests often display substantial size distortions in small samples, resulting in frequent over-rejection of the null hypothesis, as shown by Den Haan and Levin ([1997](https://arxiv.org/html/2601.21272v1#bib.bib2119 "A practitioner’s guide to robust covariance matrix estimation,")) and Müller ([2014](https://arxiv.org/html/2601.21272v1#bib.bib2120 "HAC corrections for strongly autocorrelatedtime series")). To improve size accuracy, Kiefer et al. ([2000](https://arxiv.org/html/2601.21272v1#bib.bib1937 "Simple robust testing of regression hypotheses")), Kiefer and Vogelsang ([2002a](https://arxiv.org/html/2601.21272v1#bib.bib1936 "Heteroskedasticity-autocorrelation robust standard errors using the bartlett kernel without truncation"), [b](https://arxiv.org/html/2601.21272v1#bib.bib1993 "Heteroskedasticity-autocorrelation robust testing using bandwidth equal to sample size"), [2005](https://arxiv.org/html/2601.21272v1#bib.bib2115 "A new asymptotic theory for heteroskedasticity-autocorrelation robust tests")) introduced the fixed bandwidth (bb) approach, setting bandwidth as a fixed fraction of the sample size and leveraging a nonstandard limiting distribution. Extending this approach, Phillips et al. ([2006](https://arxiv.org/html/2601.21272v1#bib.bib2116 "Spectral density estimation and robust hypothesis testing using steep origin kernels without truncation")) and Phillips et al. ([2007](https://arxiv.org/html/2601.21272v1#bib.bib1994 "Long run variance estimation and robust regression testing using sharp origin kernels with no truncation")) introduced the fixed lag (pp) method based on exponentiated kernels, offering flexible bias-variance tradeoff control. Further extending these methods, Sun et al. ([2008](https://arxiv.org/html/2601.21272v1#bib.bib2117 "Optimal bandwidth selection in heteroskedasticity-autocorrelation robust testing")) derived bandwidth selection rules via Edgeworth expansions, optimizing a loss function balancing Type I and Type II errors, and Lazarus et al. ([2018](https://arxiv.org/html/2601.21272v1#bib.bib2118 "HAR inference: recommendations for practice"), [2021](https://arxiv.org/html/2601.21272v1#bib.bib1946 "The size-power tradeoff in har inference")) advanced practical plug-in bandwidth selectors.

Despite these improvements, the HAR testing literature predominantly focuses on single-equation settings. Ray and Savin ([2008](https://arxiv.org/html/2601.21272v1#bib.bib1940 "The performance of heteroskedasticity and autocorrelation robust tests: a monte carlo study with an application to the three-factor fama: french asset-pricing model")) and Ray et al. ([2009](https://arxiv.org/html/2601.21272v1#bib.bib2113 "Testing the capm revisited")) extended the HAC-based framework to multivariate systems, assessing finite-sample performance within the multifactor model of Fama and French ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds")) and the Capital Asset Pricing Model (CAPM) of Sharpe ([1964](https://arxiv.org/html/2601.21272v1#bib.bib1915 "Capital asset prices: a theory of market equilibrium under conditions of risk")) and Lintner ([1965](https://arxiv.org/html/2601.21272v1#bib.bib1898 "The valuation of risky assets and the selection of risky investments in stock portfolios and budget constraints")). Their simulations indicate increasing size distortions as dimensionality grows, likely due to nonparametric kernel estimation suffering from the curse of dimensionality. Moreover, Baillie et al. ([2024](https://arxiv.org/html/2601.21272v1#bib.bib2090 "On robust inference in time-series regression")) highlighted a fundamental theoretical limitation of HAR tests, emphasizing that regressors correlated with errors render OLS-based HAR tests theoretically invalid due to inconsistency of the OLS estimator. To ensure valid inference, they proposed a parametric specification test based on Durbin regression (Durbin [1970](https://arxiv.org/html/2601.21272v1#bib.bib2135 "Testing for serial correlation in least-squares regression when some of the regressorsare lagged dependent variables")), demonstrating through simulations its superior performance under endogeneity. However, their approach remains limited to single-equation models, ignoring cross-equation error dependencies common in asset pricing models.

To overcome these limitations, this study introduces a novel multivariate specification test that generalize Durbin regression to the seemingly unrelated regression (SUR) setting by (Zellner [1962](https://arxiv.org/html/2601.21272v1#bib.bib2111 "An efficient method of estimating seemingly unrelated regressions and tests foraggregation bias")). Specifically, we derive dynamics dependence structure between regressors and error terms, and embed them within a SUR framework. We then construct a generalized least squares (GLS) estimator that accounts for cross-equation error covariance, and derive a Wald statistic for multivariate specification tests. Monte Carlo experiments demonstrate that the proposed Wald test exhibits superior size and power properties compared to conventional tests (the GRS and HAR tests), regardless of residual distributions or dependence structures. An empirical application to Fama and French ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds"), [2015](https://arxiv.org/html/2601.21272v1#bib.bib1869 "A five-factor asset pricing model")) multifactor models further demonstrates the robustness of our Wald test and practival reliability.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2601.21272v1#S2 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") presents the model and assumptions and develops our generalized Durbin approach by reformulating Durbin’s regression framework for a SUR system and positioning it as a GLS-class estimator. It then derives the resulting estimator and its asymptotic properties and introduces the associated Wald statistic. Section [3](https://arxiv.org/html/2601.21272v1#S3 "3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") evaluates finite-sample performance via Monte Carlo experiments, with particular emphasis on size control and the effectiveness of the bootstrap-based correction. Section [4](https://arxiv.org/html/2601.21272v1#S4 "4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") applies the proposed procedures to the Fama–French multifactor models and compares the resulting inference with competing GLS-based Wald tests and commonly used alternatives. Section [5](https://arxiv.org/html/2601.21272v1#S5 "5 Conclusion ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") concludes.

## 2 Model and Test

A common feature of economic phenomena is that multiple outcome variables are determined simultaneously and influence one another. In such settings, disturbances are often correlated across equations, so equation-by-equation estimation and specification testing can induce size distortions and misleading inference; see Breusch and Pagan ([1980](https://arxiv.org/html/2601.21272v1#bib.bib2112 "The lagrange multiplier test and its applications to model specification in econometrics")), Zhou ([1991](https://arxiv.org/html/2601.21272v1#bib.bib2129 "Small sample tests of portfolio efficiency")), and Pesaran and Yamagata ([2008](https://arxiv.org/html/2601.21272v1#bib.bib2128 "Testing slope homogeneity in large panels")). To obtain efficient system estimates and valid joint tests, Zellner ([1962](https://arxiv.org/html/2601.21272v1#bib.bib2111 "An efficient method of estimating seemingly unrelated regressions and tests foraggregation bias")) introduces the SUR framework, which extends single-equation models to multiple-equation systems and employs GLS weighting to exploit cross-equation error covariance. In time-series applications, empirical work often estimates the multiple-equation model by OLS and relies on [Newey and West](https://arxiv.org/html/2601.21272v1#bib.bib233 "A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix")’s ([1987](https://arxiv.org/html/2601.21272v1#bib.bib233 "A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix"); [1994](https://arxiv.org/html/2601.21272v1#bib.bib1903 "Automatic lag selection in covariance matrix estimation")) HAC standard errors for specification tests to address heteroskedasticity and autocorrelation. However, it is widely known that these finite-sample performance deteriorates for multivariate systems (e.g., Ray and Savin ([2008](https://arxiv.org/html/2601.21272v1#bib.bib1940 "The performance of heteroskedasticity and autocorrelation robust tests: a monte carlo study with an application to the three-factor fama: french asset-pricing model")); Ray et al. ([2009](https://arxiv.org/html/2601.21272v1#bib.bib2113 "Testing the capm revisited"))).

More fundamentally, when regressors are dynamically correlated with the disturbances, OLS can be inconsistent, rendering HAC-based inference invalid. Recent work by Baillie et al. ([2024](https://arxiv.org/html/2601.21272v1#bib.bib2090 "On robust inference in time-series regression")) shows that, in time-series settings, conventional OLS and even GLS estimators can be inconsistent under dynamic regressor–error dependence, whereas [Durbin](https://arxiv.org/html/2601.21272v1#bib.bib2135 "Testing for serial correlation in least-squares regression when some of the regressorsare lagged dependent variables")’s ([1970](https://arxiv.org/html/2601.21272v1#bib.bib2135 "Testing for serial correlation in least-squares regression when some of the regressorsare lagged dependent variables")) regression remains robust. However, their analysis is confined to a single-equation environment and therefore cannot accommodate cross-equation error covariance. In addition, their specification omits an intercept and implicitly treats regressors as mean-zero; when the true model features a nonzero intercept and regressors with nonzero means, ignoring these terms induces misspecification and can undermine consistency even in a single equation. To address these limitations, we extend Durbin’s framework to a multiple equation setting. We develop a generalized Durbin specification that explicitly models the joint second-order dynamics of regressors and disturbances, derive a feasible GLS estimator that accounts for cross-equational covariance, and provide conditions for consistency and efficiency.

### 2.1 Setup

We consider the following linear regressions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi,t=αi+𝒙i,t′​𝜷i+ui,t,i=1,…,N,t=1,…,T,y\_{i,t}=\alpha\_{i}+{\mbox{$x$}}\_{i,t}^{\prime}{\mbox{$\beta$}}\_{i}+u\_{i,t},\quad i=1,\ldots,N,\quad t=1,\ldots,T, |  | (1) |

where yi,ty\_{i,t} is the scalar dependent variable, 𝒙i,t=(xi,t,1,xi,t,2,…,xi,t,ki)′{\mbox{$x$}}\_{i,t}=(x\_{i,t,1},x\_{i,t,2},\ldots,x\_{i,t,k\_{i}})^{\prime} is a ki×1k\_{i}\times 1 vector of regressors, and ui,tu\_{i,t} is a scalar disturbance. The number of regressors kik\_{i} is allowed to vary across equations.

Let 𝒚t=(y1,t,…,yN,t)′{\mbox{$y$}}\_{t}=(y\_{1,t},\ldots,y\_{N,t})^{\prime}, 𝒖t=(u1,t,…,uN,t)′{\mbox{$u$}}\_{t}=(u\_{1,t},\ldots,u\_{N,t})^{\prime} with 𝔼​[𝒖t]=𝟎{\mathbb{E}}[{\mbox{$u$}}\_{t}]={\mbox{$0$}}, and define 𝜶=(α1,…,αN)′{\mbox{$\alpha$}}=(\alpha\_{1},\ldots,\alpha\_{N})^{\prime} and 𝜷=(𝜷1′,…,𝜷N′)′{\mbox{$\beta$}}=({\mbox{$\beta$}}\_{1}^{\prime},\ldots,{\mbox{$\beta$}}\_{N}^{\prime})^{\prime}, where k:=∑i=1Nkik:=\sum\_{i=1}^{N}k\_{i}. Further, define the block-diagonal regressor matrix

|  |  |  |
| --- | --- | --- |
|  | 𝑿t=[𝒙1,t𝟎⋯𝟎𝟎𝒙2,t⋯𝟎⋮⋮⋱⋮𝟎𝟎⋯𝒙N,t]∈ℝk×N.{\mbox{$X$}}\_{t}=\begin{bmatrix}{\mbox{$x$}}\_{1,t}&{\mbox{$0$}}&\cdots&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$x$}}\_{2,t}&\cdots&{\mbox{$0$}}\\ \vdots&\vdots&\ddots&\vdots\\ {\mbox{$0$}}&{\mbox{$0$}}&\cdots&{\mbox{$x$}}\_{N,t}\end{bmatrix}\in\mathbb{R}^{k\times N}. |  |

Stacking the NN equations, we can write the system compactly as

|  |  |  |
| --- | --- | --- |
|  | [y1,ty2,t⋮yN,t]=[α1α2⋮αN]+[𝒙1,t′𝟎⋯𝟎𝟎𝒙2,t′⋯𝟎⋮⋮⋱⋮𝟎𝟎⋯𝒙N,t′]​[𝜷1𝜷2⋮𝜷N]+[u1,tu2,t⋮uN,t],\begin{bmatrix}y\_{1,t}\\ y\_{2,t}\\ \vdots\\ y\_{N,t}\\ \end{bmatrix}=\begin{bmatrix}\alpha\_{1}\\ \alpha\_{2}\\ \vdots\\ \alpha\_{N}\\ \end{bmatrix}+\begin{bmatrix}{\mbox{$x$}}\_{1,t}^{\prime}&{\mbox{$0$}}&\cdots&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$x$}}\_{2,t}^{\prime}&\cdots&{\mbox{$0$}}\\ \vdots&\vdots&\ddots&\vdots\\ {\mbox{$0$}}&{\mbox{$0$}}&\cdots&{\mbox{$x$}}\_{N,t}^{\prime}\end{bmatrix}\begin{bmatrix}{\mbox{$\beta$}}\_{1}\\ {\mbox{$\beta$}}\_{2}\\ \vdots\\ {\mbox{$\beta$}}\_{N}\\ \end{bmatrix}+\begin{bmatrix}u\_{1,t}\\ u\_{2,t}\\ \vdots\\ u\_{N,t}\\ \end{bmatrix}, |  |

equivalently

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚t=𝜶+𝑿t′​𝜷+𝒖t,t=1,…,T.{\mbox{$y$}}\_{t}={\mbox{$\alpha$}}+{\mbox{$X$}}\_{t}^{\prime}{\mbox{$\beta$}}+{\mbox{$u$}}\_{t},\quad t=1,\ldots,T. |  | (2) |

To describe the joint second-order dynamics of regressors and disturbances, let 𝒙t=(𝒙1,t′,…,𝒙N,t′)′{\mbox{$x$}}\_{t}=({\mbox{$x$}}\_{1,t}^{\prime},\ldots,{\mbox{$x$}}\_{N,t}^{\prime})^{\prime} with 𝔼​[𝒙t]=𝝁x{\mathbb{E}}[{\mbox{$x$}}\_{t}]={\mbox{$\mu$}}\_{x}, and define

|  |  |  |
| --- | --- | --- |
|  | 𝒛t=[𝒙t𝒖t]∈ℝm,m:=k+N,{\mbox{$z$}}\_{t}=\begin{bmatrix}{\mbox{$x$}}\_{t}\\ {\mbox{$u$}}\_{t}\\ \end{bmatrix}\in\mathbb{R}^{m},\qquad m:=k+N, |  |

with mean 𝝁z:=[𝝁x,𝟎]=𝔼​[𝒛t]{\mbox{$\mu$}}\_{z}:=[{\mbox{$\mu$}}\_{x},{\mbox{$0$}}]={\mathbb{E}}[{\mbox{$z$}}\_{t}]. Let 𝒛¯t:=𝒛t−𝝁z\bar{{\mbox{$z$}}}\_{t}:={\mbox{$z$}}\_{t}-{\mbox{$\mu$}}\_{z}. We work in the Hilbert space L2​(Ω,ℱ,ℙ;ℝm)L^{2}(\Omega,\mathscr{F},\mathbb{P};\mathbb{R}^{m}) equipped with inner product ⟨U,V⟩=𝔼​[U′​V]\langle U,V\rangle={\mathbb{E}}[U^{\prime}V], and define the closed linear subspace generated by the present and past centered variables,

|  |  |  |
| --- | --- | --- |
|  | ℋt:=span¯​{𝒛¯t,𝒛¯t−1,…}.\mathscr{H}\_{t}:=\overline{\operatorname{span}}\{\bar{{\mbox{$z$}}}\_{t},\bar{{\mbox{$z$}}}\_{t-1},\ldots\}. |  |

Let 𝒫t−1\mathscr{P}\_{t-1} denote the L2L^{2}-orthogonal projection onto ℋt−1\mathscr{H}\_{t-1}. The one-step-ahead innovation is then defined by

|  |  |  |
| --- | --- | --- |
|  | 𝜺t:=𝒛¯t−𝒫t−1​[𝒛¯t]=[𝜺x,t𝜺u,t].{\mbox{$\varepsilon$}}\_{t}:=\bar{{\mbox{$z$}}}\_{t}-\mathscr{P}\_{t-1}[\bar{{\mbox{$z$}}}\_{t}]=\begin{bmatrix}{\mbox{$\varepsilon$}}\_{x,t}\\ {\mbox{$\varepsilon$}}\_{u,t}\\ \end{bmatrix}. |  |

###### Assumption 1 (Finite-predictor exactness at lag p0p\_{0}):

(A1.1)
:   The process {𝒛¯t}\{\bar{{\mbox{$z$}}}\_{t}\} is covariance-stationary with finite second moments and purely nondeterministic. For some finite p0≥1p\_{0}\geq 1,

    |  |  |  |
    | --- | --- | --- |
    |  | 𝒫t−1​[𝒛¯t]=𝒫t−1(p0)​[𝒛¯t],𝒫t−1(p0):L2→span​{𝒛¯t−1,…,𝒛¯t−p0}.\mathscr{P}\_{t-1}[\bar{{\mbox{$z$}}}\_{t}]=\mathscr{P}^{(p\_{0})}\_{t-1}[\bar{{\mbox{$z$}}}\_{t}],\qquad\mathscr{P}^{(p\_{0})}\_{t-1}:L^{2}\to\mathrm{span}\{\bar{{\mbox{$z$}}}\_{t-1},\ldots,\bar{{\mbox{$z$}}}\_{t-p\_{0}}\}. |  |

(A1.2)
:   The innovation sequence {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\} is strongly mixing with coefficients αε​(ℓ)\alpha\_{\varepsilon}(\ell) satisfying ∑ℓ=1∞αε​(ℓ)δ/(2+δ)<∞\sum\_{\ell=1}^{\infty}\alpha\_{\varepsilon}(\ell)^{\delta/(2+\delta)}<\infty for some δ>0\delta>0, has finite moments 𝔼​‖𝜺t‖4+2​δ<∞{\mathbb{E}}\|{\mbox{$\varepsilon$}}\_{t}\|^{4+2\delta}<\infty, and 𝚺:=𝔼​[𝜺t​𝜺t′]{\mbox{$\Sigma$}}:={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{t}^{\prime}] is positive definite.111The definition of the mixing coefficients aligns with Hansen ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2177 "Econometrics")).

Under Assumption (A1.1), {𝒛¯t}\{\bar{{\mbox{$z$}}}\_{t}\} is covariance-stationary and purely nondeterministic. Hence, by the Wold decomposition, 𝒛¯t\bar{{\mbox{$z$}}}\_{t} admits a unique orthogonal VMA(∞\infty) representation, with no deterministic (completely predictable) component. Furthermore, finite-predictor exactness at lag p0p\_{0} implies that {𝒛¯t}\{\bar{{\mbox{$z$}}}\_{t}\} admits a VAR(p0p\_{0}) innovations representation. We adopt a reduced-form VAR(p0p\_{0}) as the benchmark because it summarizes multivariate dynamics with minimal structural assumptions and serves as the standard workhorse in empirical macroeconomics and finance (Sims ([1980](https://arxiv.org/html/2601.21272v1#bib.bib494 "Macroeconomics and reality")); Stock and Watson ([2001](https://arxiv.org/html/2601.21272v1#bib.bib2288 "Vector autoregressions"))). Finite-order VARs can also be interpreted as practical approximations to the Wold representation for a broad class of stationary processes, which makes them a convenient parametric device for prediction and impulse-response analysis (Lütkepohl ([2005](https://arxiv.org/html/2601.21272v1#bib.bib522 "New introduction to multiple time series analysis"))).

Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(iii) establishes that this canonical VAR(p0p\_{0}) representation is stable. Since {(𝒚t,𝑿t′,𝒖t)}\{({\mbox{$y$}}\_{t},{\mbox{$X$}}\_{t}^{\prime},{\mbox{$u$}}\_{t})\} is a fixed linear transformation of 𝒛¯t\bar{{\mbox{$z$}}}\_{t}, it is also covariance-stationary. Moreover, because 𝒛¯t\bar{{\mbox{$z$}}}\_{t} admits a stable VAR(p0p\_{0}) representation driven by {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\} with finite (4+2​δ)(4+2\delta)-th moments, 𝒛¯t\bar{{\mbox{$z$}}}\_{t} can be written as a linear process with absolutely summable coefficients. Consequently, 𝒚t{\mbox{$y$}}\_{t}, 𝑿t{\mbox{$X$}}\_{t}, and 𝒖t{\mbox{$u$}}\_{t} also have finite (4+2​δ)(4+2\delta)-th moments.

###### Proposition 1:

Suppose Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") holds. Then:

(i)
:   Let 𝜺t:=𝒛¯t−𝒫t−1​[𝒛¯t]{\mbox{$\varepsilon$}}\_{t}:=\bar{{\mbox{$z$}}}\_{t}-\mathscr{P}\_{t-1}[\bar{{\mbox{$z$}}}\_{t}]. The centered process {𝒛¯t}\{\bar{{\mbox{$z$}}}\_{t}\} admits the Wold representation

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | 𝒛¯t=∑i=0∞𝚵i​𝜺t−iin ​L2,𝚵0=𝑰m,\bar{{\mbox{$z$}}}\_{t}=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{i}\,{\mbox{$\varepsilon$}}\_{t-i}\quad\text{in }L^{2},\qquad{\mbox{$\Xi$}}\_{0}={\mbox{$I$}}\_{m}, |  | (3) |

    where {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\} is (second-order) white noise: 𝔼​[𝜺t]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}]={\mbox{$0$}}, 𝔼​[𝜺t​𝜺s′]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{s}^{\prime}]={\mbox{$0$}} for s≠ts\neq t, and 𝔼​[𝜺t​𝜺t′]=𝚺{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{t}^{\prime}]={\mbox{$\Sigma$}} (constant in tt). Each 𝚵i∈ℝm×m{\mbox{$\Xi$}}\_{i}\in\mathbb{R}^{m\times m} admits the block partition

    |  |  |  |
    | --- | --- | --- |
    |  | 𝚵i=[𝚵x​x,i𝚵x​u,i𝚵u​x,i𝚵u​u,i],𝚵x​x,i∈ℝk×k,𝚵x​u,i∈ℝk×N,𝚵u​x,i∈ℝN×k,𝚵u​u,i∈ℝN×N.{\mbox{$\Xi$}}\_{i}=\begin{bmatrix}{\mbox{$\Xi$}}\_{xx,i}&{\mbox{$\Xi$}}\_{xu,i}\\ {\mbox{$\Xi$}}\_{ux,i}&{\mbox{$\Xi$}}\_{uu,i}\end{bmatrix},\quad{\mbox{$\Xi$}}\_{xx,i}\in\mathbb{R}^{k\times k},\ {\mbox{$\Xi$}}\_{xu,i}\in\mathbb{R}^{k\times N},\ {\mbox{$\Xi$}}\_{ux,i}\in\mathbb{R}^{N\times k},\ {\mbox{$\Xi$}}\_{uu,i}\in\mathbb{R}^{N\times N}. |  |

(ii)
:   There exist unique matrices {𝚿j}j=1p0⊂ℝm×m\{{\mbox{$\Psi$}}\_{j}\}\_{j=1}^{p\_{0}}\subset\mathbb{R}^{m\times m} such that the centered process admits the canonical VAR(p0p\_{0}) innovations representation

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | 𝒛¯t=∑j=1p0𝚿j​𝒛¯t−j+𝜺tin ​L2.\bar{{\mbox{$z$}}}\_{t}=\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{j}\bar{{\mbox{$z$}}}\_{t-j}+{\mbox{$\varepsilon$}}\_{t}\quad\text{in }L^{2}. |  | (4) |

    Then the VAR and VMA coefficients {𝚿j}\{{\mbox{$\Psi$}}\_{j}\} and {𝚵n}\{{\mbox{$\Xi$}}\_{n}\} satisfy, for n≥1n\geq 1,

    |  |  |  |
    | --- | --- | --- |
    |  | 𝚵0=𝑰m,𝚵n=∑j=1min⁡{p0,n}𝚿j​𝚵n−j,n≥1,{\mbox{$\Xi$}}\_{0}={\mbox{$I$}}\_{m},\qquad{\mbox{$\Xi$}}\_{n}=\sum\_{j=1}^{\min\{p\_{0},n\}}{\mbox{$\Psi$}}\_{j}{\mbox{$\Xi$}}\_{n-j},\quad n\geq 1, |  |

    equivalently 𝚿​(L)​𝚵​(L)=𝑰m{\mbox{$\Psi$}}(L){\mbox{$\Xi$}}(L)={\mbox{$I$}}\_{m} with 𝚿​(L):=𝑰m−∑j=1p0𝚿j​Lj{\mbox{$\Psi$}}(L):={\mbox{$I$}}\_{m}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{j}L^{j} and 𝚵​(L):=𝑰m+∑n=1∞𝚵n​Ln{\mbox{$\Xi$}}(L):={\mbox{$I$}}\_{m}+\sum\_{n=1}^{\infty}{\mbox{$\Xi$}}\_{n}L^{n}.

(iii)
:   The characteristic matrix polynomial 𝑷​(z):=𝑰m−∑j=1p0𝚿j​zj{\mbox{$P$}}(z):={\mbox{$I$}}\_{m}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{j}z^{j} has no zeros in or on the unit disk, that is, det𝑷​(z)≠0\det{\mbox{$P$}}(z)\neq 0 for all |z|≤1|z|\leq 1. Hence the inverse filter admits the absolutely summable power series expansion

    |  |  |  |
    | --- | --- | --- |
    |  | 𝑷​(L)−1=𝑰m+∑i=1∞𝚵i​Li,∑i=0∞‖𝚵i‖<∞.{\mbox{$P$}}(L)^{-1}={\mbox{$I$}}\_{m}+\sum\_{i=1}^{\infty}{\mbox{$\Xi$}}\_{i}L^{i},\qquad\sum\_{i=0}^{\infty}\|{\mbox{$\Xi$}}\_{i}\|<\infty. |  |

(iv)
:   The vector process {(𝒚t,𝑿t′,𝒖t)}\{({\mbox{$y$}}\_{t},{\mbox{$X$}}\_{t}^{\prime},{\mbox{$u$}}\_{t})\} is covariance-stationary as a fixed linear transform of {𝒛t}\{{\mbox{$z$}}\_{t}\}. Moreover, it is strongly mixing with coefficients α(y,X,u)​(ℓ)\alpha\_{(y,X,u)}(\ell) satisfying

    |  |  |  |
    | --- | --- | --- |
    |  | ∑ℓ=1∞α(y,X,u)​(ℓ)δ/(2+δ)<∞,\sum\_{\ell=1}^{\infty}\alpha\_{(y,X,u)}(\ell)^{\delta/(2+\delta)}<\infty, |  |

    and hence is ergodic. In addition, its components have finite (4+2​δ)(4+2\delta)-th moments:

    |  |  |  |
    | --- | --- | --- |
    |  | 𝔼​‖𝑿t‖4+2​δ<∞,𝔼​‖𝒖t‖4+2​δ<∞,𝔼​‖𝒚t‖4+2​δ<∞.{\mathbb{E}}\|{\mbox{$X$}}\_{t}\|^{4+2\delta}<\infty,\quad{\mathbb{E}}\|{\mbox{$u$}}\_{t}\|^{4+2\delta}<\infty,\quad{\mathbb{E}}\|{\mbox{$y$}}\_{t}\|^{4+2\delta}<\infty. |  |

###### Proof.

See the Appendix.
∎

Under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), the innovation covariance matrix 𝚺\Sigma can be expressed in block form as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺=[𝚺x​x𝚺x​u𝚺u​x𝚺u​u],𝚺x​x∈ℝk×k,𝚺u​u∈ℝN×N,𝚺x​u∈ℝk×N,𝚺u​x∈ℝN×k.{\mbox{$\Sigma$}}=\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$\Sigma$}}\_{xu}\\ {\mbox{$\Sigma$}}\_{ux}&{\mbox{$\Sigma$}}\_{uu}\end{bmatrix},\quad{\mbox{$\Sigma$}}\_{xx}\in\mathbb{R}^{k\times k},\quad{\mbox{$\Sigma$}}\_{uu}\in\mathbb{R}^{N\times N},\quad{\mbox{$\Sigma$}}\_{xu}\in\mathbb{R}^{k\times N},\quad{\mbox{$\Sigma$}}\_{ux}\in\mathbb{R}^{N\times k}. |  | (5) |

In addition, the VAR coefficient matrix 𝚿j∈ℝm×m{\mbox{$\Psi$}}\_{j}\in\mathbb{R}^{m\times m} for each j=1,…,p0j=1,\ldots,p\_{0} admits the following block partition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚿j=[𝚿x​x,j𝚿x​u,j𝚿u​x,j𝚿u​u,j],𝚿x​x,j∈ℝk×k,𝚿x​u,j∈ℝk×N,𝚿u​x,j∈ℝN×k,𝚿u​u,j∈ℝN×N.{\mbox{$\Psi$}}\_{j}=\begin{bmatrix}{\mbox{$\Psi$}}\_{xx,j}&{\mbox{$\Psi$}}\_{xu,j}\\ {\mbox{$\Psi$}}\_{ux,j}&{\mbox{$\Psi$}}\_{uu,j}\end{bmatrix},\ {\mbox{$\Psi$}}\_{xx,j}\in\mathbb{R}^{k\times k},\ {\mbox{$\Psi$}}\_{xu,j}\in\mathbb{R}^{k\times N},\ {\mbox{$\Psi$}}\_{ux,j}\in\mathbb{R}^{N\times k},\ {\mbox{$\Psi$}}\_{uu,j}\in\mathbb{R}^{N\times N}. |  | (6) |

Under the stable VAR(p0p\_{0}) (equivalently, absolutely summable impulse responses) representation for 𝒛¯t=[(𝒙t−𝝁x)′,𝒖t′]′\bar{{\mbox{$z$}}}\_{t}=[({\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x})^{\prime},{\mbox{$u$}}\_{t}^{\prime}]^{\prime}, the pair {{𝚿j}j=1p0,𝚺}\big\{\{{\mbox{$\Psi$}}\_{j}\}\_{j=1}^{p\_{0}},{\mbox{$\Sigma$}}\big\} fully characterizes the second-order properties of {𝒛¯t}\{\bar{{\mbox{$z$}}}\_{t}\}. The innovation covariance 𝚺\Sigma governs the contemporaneous (innovation) covariance between εx,t\varepsilon\_{x,t} and εu,t\varepsilon\_{u,t}, whereas dynamic cross-dependence is generated by the off-diagonal VAR blocks {𝚿x​u,j,𝚿u​x,j}\{{\mbox{$\Psi$}}\_{xu,j},{\mbox{$\Psi$}}\_{ux,j}\} and propagates through the impulse responses {𝚵i}\{{\mbox{$\Xi$}}\_{i}\} defined by 𝚵​(L)=𝑷​(L)−1{\mbox{$\Xi$}}(L)={\mbox{$P$}}(L)^{-1} with 𝑷​(L)=𝑰m−∑j=1p0𝚿j​Lj{\mbox{$P$}}(L)={\mbox{$I$}}\_{m}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{j}L^{j}. For any lag ℓ∈ℤ\ell\in\mathbb{Z},

|  |  |  |
| --- | --- | --- |
|  | 𝚪z​(ℓ):=ℂ​ov​(𝒛¯t,𝒛¯t−ℓ)={∑j=0∞𝚵ℓ+j​𝚺𝚵j′,ℓ≥0,𝚪z​(−ℓ)′,ℓ<0,{\mbox{$\Gamma$}}\_{z}(\ell):={\mathbb{C}\rm{ov}}(\bar{{\mbox{$z$}}}\_{t},\bar{{\mbox{$z$}}}\_{t-\ell})=\begin{cases}\displaystyle\sum\_{j=0}^{\infty}{\mbox{$\Xi$}}\_{\ell+j}{\mbox{$\Sigma$}}{\mbox{$\Xi$}}\_{j}^{\prime},&\ell\geq 0,\\ {\mbox{$\Gamma$}}\_{z}(-\ell)^{\prime},&\ell<0,\end{cases} |  |

so every contemporaneous and lead-lag covariance (in particular ℂ​ov​(𝒙t,𝒖t−ℓ){\mathbb{C}\rm{ov}}({\mbox{$x$}}\_{t},{\mbox{$u$}}\_{t-\ell})) is a deterministic function of {𝚿j}\{{\mbox{$\Psi$}}\_{j}\} and 𝚺\Sigma.

In asset-pricing applications, it is common to consider a common set of regressors shared across all equations. Leading examples include the CAPM of Sharpe ([1964](https://arxiv.org/html/2601.21272v1#bib.bib1915 "Capital asset prices: a theory of market equilibrium under conditions of risk")) and Lintner ([1965](https://arxiv.org/html/2601.21272v1#bib.bib1898 "The valuation of risky assets and the selection of risky investments in stock portfolios and budget constraints")), the arbitrage pricing theory (APT) of Ross ([1976](https://arxiv.org/html/2601.21272v1#bib.bib1912 "The arbitrage theory of capital asset pricing")), and the multi-factor models of Fama and French ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds"), [2015](https://arxiv.org/html/2601.21272v1#bib.bib1869 "A five-factor asset pricing model"), [2016](https://arxiv.org/html/2601.21272v1#bib.bib1870 "Dissecting anomalies with a five-factor model")). In these cases, 𝒙i,t=𝒙t{\mbox{$x$}}\_{i,t}={\mbox{$x$}}\_{t} for all ii. This common-regressor case is nested in our general setup, and all results under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") remain valid after a notational simplification.

###### Remark 1 (Common regressors across equations):

Suppose that the regressor vector is common across equations, i.e.,

|  |  |  |
| --- | --- | --- |
|  | 𝒙i,t:=𝒙t∈ℝrfor all ​i=1,…,N,{\mbox{$x$}}\_{i,t}:={\mbox{$x$}}\_{t}\in\mathbb{R}^{r}\quad\text{for all }i=1,\ldots,N, |  |

so that ki:=rk\_{i}:=r and hence the total regressor dimension in the general setup becomes k:=∑i=1Nki=N​rk:=\sum\_{i=1}^{N}k\_{i}=Nr. Then the multi-equation regression ([1](https://arxiv.org/html/2601.21272v1#S2.E1 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"))–([2](https://arxiv.org/html/2601.21272v1#S2.E2 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) can be written as

|  |  |  |
| --- | --- | --- |
|  | 𝒚t=𝜶+𝑿t′​𝜷+𝒖t,{\mbox{$y$}}\_{t}={\mbox{$\alpha$}}+{\mbox{$X$}}\_{t}^{\prime}{\mbox{$\beta$}}+{\mbox{$u$}}\_{t}, |  |

where 𝑿t′=(𝑰N⊗𝒙t′)∈ℝN×k{\mbox{$X$}}\_{t}^{\prime}=({\mbox{$I$}}\_{N}\otimes{\mbox{$x$}}\_{t}^{\prime})\in\mathbb{R}^{N\times k} and 𝜷=(𝜷1′,…,𝜷N′)′∈ℝk{\mbox{$\beta$}}=({\mbox{$\beta$}}\_{1}^{\prime},\ldots,{\mbox{$\beta$}}\_{N}^{\prime})^{\prime}\in\mathbb{R}^{k} with k=N​rk=Nr. Define 𝒛t:=[(𝒙t−𝝁x)′,𝒖t′]′∈ℝm{\mbox{$z$}}\_{t}:=[({\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x})^{\prime},\ {\mbox{$u$}}\_{t}^{\prime}]^{\prime}\in\mathbb{R}^{m} with m:=r+Nm:=r+N and 𝒛¯t:=𝒛t−𝝁z\bar{{\mbox{$z$}}}\_{t}:={\mbox{$z$}}\_{t}-{\mbox{$\mu$}}\_{z} as before. Under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), {𝒛¯t}\{\bar{{\mbox{$z$}}}\_{t}\} admits the stable VAR(p0p\_{0}) and Wold VMA(∞\infty) representations

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=∑j=1p0𝚿j​𝒛¯t−j+𝜺t,𝒛¯t=∑i=0∞𝚵i​𝜺t−i,𝚵​(L)=𝑷​(L)−1,\bar{{\mbox{$z$}}}\_{t}=\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{j}\bar{{\mbox{$z$}}}\_{t-j}+{\mbox{$\varepsilon$}}\_{t},\qquad\bar{{\mbox{$z$}}}\_{t}=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{i}\,{\mbox{$\varepsilon$}}\_{t-i},\quad{\mbox{$\Xi$}}(L)={\mbox{$P$}}(L)^{-1}, |  |

where 𝑷​(L)=𝑰m−∑j=1p0𝚿j​Lj{\mbox{$P$}}(L)={\mbox{$I$}}\_{m}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{j}L^{j}. The innovation covariance and VAR
coefficients admit the block partitions

|  |  |  |
| --- | --- | --- |
|  | 𝚺=𝔼​[𝜺t​𝜺t′]=[𝚺x​x𝚺x​u𝚺u​x𝚺u​u],𝚿j=[𝚿x​x,j𝚿x​u,j𝚿u​x,j𝚿u​u,j],{\mbox{$\Sigma$}}={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{t}^{\prime}]=\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$\Sigma$}}\_{xu}\\ {\mbox{$\Sigma$}}\_{ux}&{\mbox{$\Sigma$}}\_{uu}\end{bmatrix},\qquad{\mbox{$\Psi$}}\_{j}=\begin{bmatrix}{\mbox{$\Psi$}}\_{xx,j}&{\mbox{$\Psi$}}\_{xu,j}\\ {\mbox{$\Psi$}}\_{ux,j}&{\mbox{$\Psi$}}\_{uu,j}\end{bmatrix}, |  |

with 𝚺x​x∈ℝr×r{\mbox{$\Sigma$}}\_{xx}\in\mathbb{R}^{r\times r}, 𝚺u​u∈ℝN×N{\mbox{$\Sigma$}}\_{uu}\in\mathbb{R}^{N\times N},
𝚺x​u∈ℝr×N{\mbox{$\Sigma$}}\_{xu}\in\mathbb{R}^{r\times N}, and 𝚺u​x∈ℝN×r{\mbox{$\Sigma$}}\_{ux}\in\mathbb{R}^{N\times r}, and likewise
𝚿x​x,j∈ℝr×r{\mbox{$\Psi$}}\_{xx,j}\in\mathbb{R}^{r\times r}, 𝚿x​u,j∈ℝr×N{\mbox{$\Psi$}}\_{xu,j}\in\mathbb{R}^{r\times N},
𝚿u​x,j∈ℝN×r{\mbox{$\Psi$}}\_{ux,j}\in\mathbb{R}^{N\times r}, and 𝚿u​u,j∈ℝN×N{\mbox{$\Psi$}}\_{uu,j}\in\mathbb{R}^{N\times N}.

Hereafter, we establish conditions for the consistency and asymptotic normality of estimators of (𝜶′,𝜷′)′({\mbox{$\alpha$}}^{\prime},{\mbox{$\beta$}}^{\prime})^{\prime} across a variety of data-generating processes (DGPs), characterized by restrictions on {𝚿j}j=1p0\{{\mbox{$\Psi$}}\_{j}\}\_{j=1}^{p\_{0}} and 𝚺\Sigma.

### 2.2 Relationships among exogeneity conditions

In linear regression analysis, exogeneity assumptions play a central role in determining how the stochastic relationship between the regressors and the disturbances affects the consistency and efficiency of estimators and the validity of associated test statistics. In cross-sectional settings, it is often enough to require a contemporaneous orthogonality condition. In time-series settings, however, it is no longer sufficient to require that 𝒖t{\mbox{$u$}}\_{t} be uncorrelated with the contemporaneous regressors only, (i.e., 𝔼​[𝒙t​𝒖t′]=𝟎{\mathbb{E}}[{\mbox{$x$}}\_{t}{\mbox{$u$}}\_{t}^{\prime}]={\mbox{$0$}}). One must specify how 𝒖t{\mbox{$u$}}\_{t} relates to the entire temporal path of {𝒙s}\{{\mbox{$x$}}\_{s}\}, which leads to various dynamic exogeneity concepts.

Different strands of the literature formalize these orthogonality requirements in different ways. The traditional approach, following Stock and Watson ([2019](https://arxiv.org/html/2601.21272v1#bib.bib2217 "Introduction to econometrics")), imposes conditional mean-independence restrictions such as strict exogeneity and present-and-past exogeneity. Strict exogeneity requires 𝔼​[𝒖t∣…,𝒙t+2,𝒙t+1,𝒙t,𝒙t−1,𝒙t−2,…]=𝟎{\mathbb{E}}[{\mbox{$u$}}\_{t}\mid\ldots,{\mbox{$x$}}\_{t+2},{\mbox{$x$}}\_{t+1},{\mbox{$x$}}\_{t},{\mbox{$x$}}\_{t-1},{\mbox{$x$}}\_{t-2},\ldots]={\mbox{$0$}} for all tt, that is, the disturbance is mean-independent of the entire history and future path of the regressors. Present-and-past exogeneity relaxes strict exogeneity by conditioning only on current and past regressors: 𝔼​[𝒖t∣𝒙t,𝒙t−1,𝒙t−2,…]=𝟎{\mathbb{E}}[{\mbox{$u$}}\_{t}\mid{\mbox{$x$}}\_{t},{\mbox{$x$}}\_{t-1},{\mbox{$x$}}\_{t-2},\ldots]={\mbox{$0$}} for all tt. These exogeneity conditions preclude any correlation between the disturbance 𝒖t{\mbox{$u$}}\_{t} and the relevant history of the regressors. In particular, under strict exogeneity we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒖t​𝒙s′]=𝟎for all ​t,s,{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{s}^{\prime}]={\mbox{$0$}}\quad\text{for all }t,s, |  | (7) |

whereas under present-and-past exogeneity we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒖t​𝒙s′]=𝟎for all ​t​ and all ​s≤t.{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{s}^{\prime}]={\mbox{$0$}}\quad\text{for all }t\text{ and all }s\leq t. |  | (8) |

Hereafter, we refer to ([7](https://arxiv.org/html/2601.21272v1#S2.E7 "In 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) and ([8](https://arxiv.org/html/2601.21272v1#S2.E8 "In 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) as the strict exogeneity and present-and-past exogeneity conditions, respectively. In particular, strict exogeneity implies present-and-past exogeneity, and the inclusion is strict: strict exogeneity ⊊\subsetneq present-and-past exogeneity. In what follows, we use these terms in the covariance sense implied by the conditional mean restrictions (i.e., 𝔼​[𝒖t​𝒙s′]=𝟎{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{s}^{\prime}]={\mbox{$0$}}) because our joint VAR/VMA framework is stated in second-order terms.

In single-equation environments, Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")) define exogeneity conditions in terms of the Wold innovations of the disturbance process. Let {𝜺u,t}\{{\mbox{$\varepsilon$}}\_{u,t}\} denote the (vector) innovation sequence in the Wold decomposition of {𝒖t}\{{\mbox{$u$}}\_{t}\} induced by the joint representation in Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"). The same definitions extend naturally to multiple-equation systems. The regressors are said to be pre-determined if

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒙t​(𝜺u,t,𝜺u,t+1,…)′]=𝟎{\mathbb{E}}[{\mbox{$x$}}\_{t}({\mbox{$\varepsilon$}}\_{u,t},{\mbox{$\varepsilon$}}\_{u,t+1},\ldots)^{\prime}]={\mbox{$0$}} |  | (9) |

that is, 𝒙t{\mbox{$x$}}\_{t} is uncorrelated with the present and all future innovations.222Under the joint Wold representation in Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(i), 𝒙¯t:=𝒙t−𝝁x\bar{{\mbox{$x$}}}\_{t}:={\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x} is a linear function of current and past innovations. Since 𝜺t{{\mbox{$\varepsilon$}}\_{t}} is white noise, 𝒙¯t\bar{{\mbox{$x$}}}\_{t} (and hence 𝒙t{\mbox{$x$}}\_{t}) is automatically orthogonal to future 𝜺u,t+h{\mbox{$\varepsilon$}}\_{u,t+h} for h≥1h\geq 1. Hence, the only nontrivial restriction in ([9](https://arxiv.org/html/2601.21272v1#S2.E9 "In 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is 𝔼​[𝒙¯t​𝜺u,t′]=𝟎{\mathbb{E}}[\bar{{\mbox{$x$}}}\_{t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$0$}}, i.e., 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}. The regressors are said to be exogenous if

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒙t​(𝜺u,t,𝜺u,t−1,…)′]=𝟎{\mathbb{E}}[{\mbox{$x$}}\_{t}({\mbox{$\varepsilon$}}\_{u,t},{\mbox{$\varepsilon$}}\_{u,t-1},\ldots)^{\prime}]={\mbox{$0$}} |  | (10) |

so that 𝒙t{\mbox{$x$}}\_{t} is uncorrelated with present and all past innovations. In Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")), 𝔼​[𝒙t​𝜺u,t′]=𝟎{\mathbb{E}}[{\mbox{$x$}}\_{t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$0$}} is imposed as a standing condition. We incorporate it into ([9](https://arxiv.org/html/2601.21272v1#S2.E9 "In 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"))–([10](https://arxiv.org/html/2601.21272v1#S2.E10 "In 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) for notational convenience; the definitions are unchanged.

By contrast, Baillie et al. ([2024](https://arxiv.org/html/2601.21272v1#bib.bib2090 "On robust inference in time-series regression")) propose a different set of exogeneity conditions in a single-equation framework. In our multiple-equation setting, these conditions can be conveniently expressed in terms of the VAR representation for 𝒛¯t=(𝒙¯t′,𝒖t′)′\bar{{\mbox{$z$}}}\_{t}=(\bar{{\mbox{$x$}}}\_{t}^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime}. Under the Block-Diagonal (B​DBD) condition, the dynamics and innovations are block-diagonal:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒛¯t=∑j=1p0[𝚿x​x,j𝟎𝟎𝚿u​u,j]​𝒛¯t−j+𝜺t,𝚺=[𝚺x​x𝟎𝟎𝚺u​u].\bar{{\mbox{$z$}}}\_{t}=\sum\_{j=1}^{p\_{0}}\begin{bmatrix}{\mbox{$\Psi$}}\_{xx,j}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Psi$}}\_{uu,j}\\ \end{bmatrix}\bar{{\mbox{$z$}}}\_{t-j}+{\mbox{$\varepsilon$}}\_{t},\qquad{\mbox{$\Sigma$}}=\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Sigma$}}\_{uu}\\ \end{bmatrix}. |  | (11) |

The GLS-Exogeneity (G​E​X​O​GGEXOG) condition relaxes the B​DBD condition by allowing feedback from past disturbances to the regressors, while keeping the innovation covariance block-diagonal:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒛¯t=∑j=1p0[𝚿x​x,j𝚿x​u,j𝟎𝚿u​u,j]​𝒛¯t−j+𝜺t,𝚺=[𝚺x​x𝟎𝟎𝚺u​u].\bar{{\mbox{$z$}}}\_{t}=\sum\_{j=1}^{p\_{0}}\begin{bmatrix}{\mbox{$\Psi$}}\_{xx,j}&{\mbox{$\Psi$}}\_{xu,j}\\ {\mbox{$0$}}&{\mbox{$\Psi$}}\_{uu,j}\\ \end{bmatrix}\bar{{\mbox{$z$}}}\_{t-j}+{\mbox{$\varepsilon$}}\_{t},\qquad{\mbox{$\Sigma$}}=\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Sigma$}}\_{uu}\\ \end{bmatrix}. |  | (12) |

Finally, under the Error-Block-Diagonal (E​B​DEBD) condition, both directions of dynamic interaction are allowed through the VAR coefficients, while the innovation covariance matrix remains block-diagonal:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒛¯t=∑j=1p0[𝚿x​x,j𝚿x​u,j𝚿u​x,j𝚿u​u,j]​𝒛¯t−j+𝜺t,𝚺=[𝚺x​x𝟎𝟎𝚺u​u].\bar{{\mbox{$z$}}}\_{t}=\sum\_{j=1}^{p\_{0}}\begin{bmatrix}{\mbox{$\Psi$}}\_{xx,j}&{\mbox{$\Psi$}}\_{xu,j}\\ {\mbox{$\Psi$}}\_{ux,j}&{\mbox{$\Psi$}}\_{uu,j}\\ \end{bmatrix}\bar{{\mbox{$z$}}}\_{t-j}+{\mbox{$\varepsilon$}}\_{t},\qquad{\mbox{$\Sigma$}}=\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Sigma$}}\_{uu}\\ \end{bmatrix}. |  | (13) |

As is clear from these representations, the conditions satisfy the nesting relationship B​DBD ⊊\subsetneq G​E​X​O​GGEXOG ⊊\subsetneq E​B​DEBD.

However, different strands of the literature rely on different notions of exogeneity, and it is unclear how these conditions are related to one another or how strong they are in a comparative sense. Because Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") guarantees a joint VAR/VMA representation for ((𝒙t−𝝁x)′,𝒖t′)′(({\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x})^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime}, it is natural to study these exogeneity concepts through the lens of the VAR coefficients {𝚿j}\{{\mbox{$\Psi$}}\_{j}\} and the innovation covariance matrix 𝚺\Sigma. In particular, the B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD conditions can be interpreted as structural restrictions on (𝚿j,𝚺)({\mbox{$\Psi$}}\_{j},{\mbox{$\Sigma$}}) that delimit the range of dynamic feedback between regressors and disturbances.

The following proposition makes these relationships explicit under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").

###### Proposition 2:

Under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), the following statements hold:

(i)
:   The strict exogeneity and the B​DBD condition are equivalent;

(ii)
:   The pre-determined condition and the E​B​DEBD condition coincide;

(iii)
:   Within the E​B​DEBD class, the subclass of DGPs that satisfy covariance-based present-and-past exogeneity lies strictly between B​DBD and E​B​DEBD; that is, B​DBD ⊊\subsetneq {\{present-and-past exogeneity}\} ∩\cap E​B​DEBD ⊊\subsetneq E​B​DEBD.

Proposition [2](https://arxiv.org/html/2601.21272v1#Thmproposition2 "Proposition 2: ‣ 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") provides a unified characterization of exogeneity concepts from different strands of the literature and will serve as a reference point when we discuss the consistency of OLS, GLS-type, and Durbin-type estimators.

The equivalences in part (i) show that two seemingly different notions of exogeneity in the literature actually characterize the same class of data-generating processes under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"). This class corresponds to environments in which the regressors and the disturbance are separated at the second-order level: the marginal dynamics of {𝒙t}\{{\mbox{$x$}}\_{t}\} and {𝒖t}\{{\mbox{$u$}}\_{t}\} follow their own VAR laws of motion with no dynamic cross-effects. Moreover, the two innovation blocks are contemporaneously orthogonal; combined with block-diagonal dynamics, this implies ℂ​ov​(𝒙t,𝒖t−ℓ)=𝟎{\mathbb{C}\rm{ov}}({\mbox{$x$}}\_{t},{\mbox{$u$}}\_{t-\ell})={\mbox{$0$}} for all ℓ∈ℤ\ell\in\mathbb{Z}. Within this class of DGPs, conventional estimators such as OLS and GLS-type procedures that model the error dynamics independently of the regressors (e.g. Cochrane and Orcutt ([1949](https://arxiv.org/html/2601.21272v1#bib.bib1857 "Application of least squares regression to relationships containing auto-correlated error terms")); Nagakura ([2024](https://arxiv.org/html/2601.21272v1#bib.bib1985 "Cochrane–orcutt type estimator for multivariate linear regression model with serially correlated errors"))) are consistent. Furthermore, the OLS-based GLS estimator is asymptotically efficient within this class of DGPs.

The equivalence in part (ii) shows that the innovation-based pre-determined condition and the E​B​DEBD condition describe exactly the same class of data-generating processes under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"). In Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")), the proposed FGLS-D estimator in a single-equation model is claimed to be consistent under pre-determined regressors. However, within our joint VAR/VMA framework, this statement is valid only for a narrower subclass of pre-determined DGPs. In their analysis, the innovation sequence is defined from the marginal Wold decomposition of utu\_{t}, and lagged xtx\_{t} is excluded from the error law of motion. In our block-VAR notation, this corresponds to imposing Ψu​x,j=0\Psi\_{ux,j}=0 for all jj, while maintaining 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}. Hence, their maintained setting corresponds to the G​E​X​O​GGEXOG region (upper block-triangular), which is strictly contained in the full pre-determined/E​B​DEBD class. At this point, it is also useful to clarify how the innovation-based exogenous condition relates to our joint VAR/VMA framework. The next remark records its precise location relative to B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD.

###### Remark 2 (Innovation-based exogeneity and its location):

In addition to the pre-determined condition in Proposition [2](https://arxiv.org/html/2601.21272v1#Thmproposition2 "Proposition 2: ‣ 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(ii), one may consider the innovation-based exogenous condition

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒙t​(𝜺u,t,𝜺u,t−1,…)′]=𝟎,{\mathbb{E}}\big[{\mbox{$x$}}\_{t}({\mbox{$\varepsilon$}}\_{u,t},{\mbox{$\varepsilon$}}\_{u,t-1},\ldots)^{\prime}\big]={\mbox{$0$}}, |  |

where {𝜺u,t}\{{\mbox{$\varepsilon$}}\_{u,t}\} is the uu-block of the joint Wold innovation 𝜺t{\mbox{$\varepsilon$}}\_{t} of 𝒛¯t\bar{{\mbox{$z$}}}\_{t} in Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").333In Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")), the innovation sequence is defined from the marginal Wold decomposition of utu\_{t} alone. Since our innovations are defined jointly for (𝒙t,𝒖t)({\mbox{$x$}}\_{t},{\mbox{$u$}}\_{t}), the two notions need not coincide when 𝒙t{\mbox{$x$}}\_{t} helps predict 𝒖t{\mbox{$u$}}\_{t}.

Under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), the exogenous condition is strictly stronger than pre-determined/E​B​DEBD. Indeed, writing the joint Wold representation as

|  |  |  |
| --- | --- | --- |
|  | 𝒙¯t=∑i=0∞𝚵x​x,i​𝜺x,t−i+∑i=0∞𝚵x​u,i​𝜺u,t−i,\bar{{\mbox{$x$}}}\_{t}=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{xx,i}{\mbox{$\varepsilon$}}\_{x,t-i}+\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{xu,i}{\mbox{$\varepsilon$}}\_{u,t-i}, |  |

the restriction 𝚵x​u,i=𝟎{\mbox{$\Xi$}}\_{xu,i}={\mbox{$0$}} for all i≥0i\geq 0 (i.e., past uu-innovations do not enter the linear representation of 𝒙t{\mbox{$x$}}\_{t}) is sufficient for the exogenous condition to hold.444Under the regularity conditions in Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") (in particular, 𝚺u​u≻0{\mbox{$\Sigma$}}\_{uu}\succ 0), this restriction is also equivalent to the exogenous condition. In particular, since pre-determined/E​B​DEBD is equivalent to 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} (Proposition [2](https://arxiv.org/html/2601.21272v1#Thmproposition2 "Proposition 2: ‣ 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(ii)), we obtain the strict nesting

|  |  |  |
| --- | --- | --- |
|  | B​D⊊{exogenous}⊊{pre-determined}=E​B​D.BD\subsetneq\{\text{exogenous}\}\subsetneq\{\text{pre-determined}\}=EBD. |  |

The first inclusion holds because B​DBD imposes block-diagonality of both the VAR dynamics and the innovation covariance, whereas the exogenous condition only rules out the u→xu\to x channel, namely 𝚵x​u,i=𝟎{\mbox{$\Xi$}}\_{xu,i}={\mbox{$0$}} for all i≥0i\geq 0 (equivalently, under invertibility, 𝚿x​u,j=𝟎{\mbox{$\Psi$}}\_{xu,j}={\mbox{$0$}} for all jj), while allowing x→ux\to u feedback.

Finally, the exogenous condition is generally not nested with the G​E​X​O​GGEXOG condition. The exogenous condition eliminates feedback from uu to xx, while the G​E​X​O​GGEXOG condition eliminates feedback from xx to uu; hence neither condition implies the other in general.

With these innovation-based notions in place, part (iii) locates the covariance-based present-and-past exogeneity condition within the B​DBD and E​B​DEBD classes. Within the E​B​DEBD class, present-and-past exogeneity is weaker than strict exogeneity/B​DBD, but still stronger than the full E​B​DEBD condition. In this sense, the [Stock and Watson](https://arxiv.org/html/2601.21272v1#bib.bib2217 "Introduction to econometrics")’s ([2019](https://arxiv.org/html/2601.21272v1#bib.bib2217 "Introduction to econometrics")) restriction based on present-and-past exogeneity can be interpreted as a nontrivial strengthening of the innovation-orthogonality restriction 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}, because it further restricts the lagged covariances 𝔼​[𝒖t​𝒙t−ℓ′]{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{t-\ell}^{\prime}] for ℓ≥0\ell\geq 0, while still allowing richer dynamic feedback than in the B​DBD case. At the same time, there is no simple nesting relationship between present-and-past exogeneity and G​E​X​O​GGEXOG: some G​E​X​O​GGEXOG DGPs satisfy covariance-based present-and-past exogeneity, while others do not, and conversely.

Among the joint VAR-based exogeneity conditions considered in this paper, namely B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD, the E​B​DEBD class is the weakest (least restrictive). An estimator that remains consistent under E​B​DEBD is particularly valuable in empirical applications, where richer dynamic feedback between regressors and disturbances is likely. In what follows, we develop a generalized Durbin estimator for multiple-equation systems, together with its associated test statistics, providing a robust alternative to conventional OLS/GLS-type procedures.

### 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models

In empirical applications, the ordinary least squares (OLS) is routinely used to estimate the parameter vector of ([2](https://arxiv.org/html/2601.21272v1#S2.E2 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")). For notational convenience, rewrite ([2](https://arxiv.org/html/2601.21272v1#S2.E2 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚t=𝒁t′​𝜿+𝒖t,t=1,…,T,{\mbox{$y$}}\_{t}={\mbox{$Z$}}\_{t}^{\prime}{\mbox{$\kappa$}}+{\mbox{$u$}}\_{t},\quad t=1,\ldots,T, |  | (14) |

where 𝒁t′=[𝑰N,𝑿t′]∈ℝN×(N+k){\mbox{$Z$}}\_{t}^{\prime}=[{\mbox{$I$}}\_{N},{\mbox{$X$}}\_{t}^{\prime}]\in\mathbb{R}^{N\times(N+k)} and 𝜿=(𝜶′,𝜷′)′∈ℝN+k{\mbox{$\kappa$}}=({\mbox{$\alpha$}}^{\prime},{\mbox{$\beta$}}^{\prime})^{\prime}\in\mathbb{R}^{N+k}. Then the OLS estimator of ([14](https://arxiv.org/html/2601.21272v1#S2.E14 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜿^O​L​S:=(∑t=1T𝒁t​𝒁t′)−1​(∑t=1T𝒁t​𝒚t).\widehat{{\mbox{$\kappa$}}}^{OLS}:=\Big(\sum\_{t=1}^{T}{\mbox{$Z$}}\_{t}{\mbox{$Z$}}\_{t}^{\prime}\Big)^{-1}\Big(\sum\_{t=1}^{T}{\mbox{$Z$}}\_{t}{\mbox{$y$}}\_{t}\Big). |  | (15) |

While the OLS estimator of ([14](https://arxiv.org/html/2601.21272v1#S2.E14 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is often used to estimate 𝜿\kappa in time-series regressions, consistency typically requires not only a full-rank condition on the regressors but also nontrivial exogeneity restrictions. We begin with a standard identification condition.

###### Assumption 2:

𝑸Z:=𝔼​[𝒁t​𝒁t′]{\mbox{$Q$}}\_{Z}:={\mathbb{E}}[{\mbox{$Z$}}\_{t}{\mbox{$Z$}}\_{t}^{\prime}] is positive definite.

Assumption [2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") is a standard full-rank condition on the regressors. It rules out exact multicollinearity and guarantees that the parameter vector 𝜿\kappa is identified from the second-moment matrix of the regressors so that the population normal equations admit a unique solution.

Baillie et al. ([2024](https://arxiv.org/html/2601.21272v1#bib.bib2090 "On robust inference in time-series regression")) state that the B​DBD condition is required for the consistency of the OLS estimator. In contrast, Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")) formulate innovation-based exogeneity conditions–defined from the marginal Wold decomposition of utu\_{t}–as convenient sufficient conditions in their consistency analysis. As shown in Proposition [2](https://arxiv.org/html/2601.21272v1#Thmproposition2 "Proposition 2: ‣ 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(i), the B​DBD requirement coincides with (covariance-based) strict exogeneity in our joint VAR/VMA framework. These conditions, however, are stronger than is strictly necessary. Likewise, Stock and Watson ([2019](https://arxiv.org/html/2601.21272v1#bib.bib2217 "Introduction to econometrics")) treat present-and-past exogeneity as a key assumption for OLS consistency. Present-and-past exogeneity implies the contemporaneous orthogonality condition 𝔼​[𝒖t​𝒙t′]=𝟎{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{t}^{\prime}]={\mbox{$0$}}, but it is not necessary for OLS consistency. In this sense, the exogeneity assumptions imposed in these previous studies lie (generally strictly) inside a larger class of data-generating processes under which OLS can still be consistent. The next proposition summarizes the exact condition for OLS consistency in our setting and clarifies how it relates to the exogeneity classes discussed above.

###### Proposition 3:

Suppose that Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")-[2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") hold. The OLS estimator 𝛋^O​L​S\widehat{{\mbox{$\kappa$}}}^{OLS} in ([15](https://arxiv.org/html/2601.21272v1#S2.E15 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is consistent for 𝛋\kappa if and only if 𝔼​[𝐙t​𝐮t]=𝟎{\mathbb{E}}[{\mbox{$Z$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}}, equivalently (using 𝔼​[𝐮t]=𝟎{\mathbb{E}}[{\mbox{$u$}}\_{t}]={\mbox{$0$}}) if and only if the contemporaneous orthogonality condition 𝔼​[𝐗t​𝐮t]=𝟎{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}} holds.

###### Proof.

See the Appendix.
∎

Proposition [3](https://arxiv.org/html/2601.21272v1#Thmproposition3 "Proposition 3: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") shows that OLS consistency hinges on the contemporaneous orthogonality condition 𝔼​[𝑿t​𝒖t]=𝟎{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}} (equivalently, since 𝔼​[𝒖t]=𝟎{\mathbb{E}}[{\mbox{$u$}}\_{t}]={\mbox{$0$}}, 𝔼​[𝒁t​𝒖t]=𝟎{\mathbb{E}}[{\mbox{$Z$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}}). The key issue, therefore, is the mechanism through which this orthogonality can arise in dynamic environments.

Under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), the joint VAR/VMA representation of 𝒛¯t=((𝒙t−𝝁x)′,𝒖t′)′\bar{{\mbox{$z$}}}\_{t}=(({\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x})^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime} implies that contemporaneous orthogonality is generally not guaranteed by innovation orthogonality alone. In particular, even if 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} holds, dynamic feedback captured by the off-diagonal blocks of {𝚿j}\{{\mbox{$\Psi$}}\_{j}\} (equivalently, by the impulse responses {𝚵i}\{{\mbox{$\Xi$}}\_{i}\}) can propagate past shocks across blocks and generate ℂ​ov​(𝒙¯t,𝒖t)≠𝟎{\mathbb{C}\rm{ov}}(\bar{{\mbox{$x$}}}\_{t},{\mbox{$u$}}\_{t})\neq{\mbox{$0$}}. This observation motivates characterizing when 𝔼​[𝑿t​𝒖t]=𝟎{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}} holds in terms of structural restrictions on ({𝚿j},𝚺)(\{{\mbox{$\Psi$}}\_{j}\},{\mbox{$\Sigma$}}), which naturally leads to the exogeneity classes B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD.

To make this point concrete, we next locate the moment condition 𝔼​[𝑿t​𝒖t]=𝟎{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}} within the joint VAR-based exogeneity classes. We show that B​DBD is sufficient for contemporaneous orthogonality, whereas under G​E​X​O​GGEXOG (and hence within the broader E​B​DEBD class) the condition typically fails because 𝒙t{\mbox{$x$}}\_{t} may load on lagged disturbances. This establishes the precise sense in which OLS (and OLS-based GLS procedures) can be inconsistent in dynamic multi-equation environments.

###### Proposition 4:

Suppose Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") holds.

(i)
:   Under B​DBD, the contemporaneous orthogonality condition holds:
    𝔼​[𝑿t​𝒖t]=𝟎{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}} (equivalently, ℂ​ov​(𝒙¯t,𝒖t)=𝟎{\mathbb{C}\rm{ov}}(\bar{{\mbox{$x$}}}\_{t},{\mbox{$u$}}\_{t})={\mbox{$0$}}).

(ii)
:   Under G​E​X​O​G∖B​DGEXOG\setminus BD, the contemporaneous orthogonality condition 𝔼​[𝑿t​𝒖t]=𝟎{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}} fails for generic parameter values, except under additional restrictions such as 𝚿u​u,j=0​∀j{\mbox{$\Psi$}}\_{uu,j}=0\ \forall j (no serial correlation in 𝒖t{\mbox{$u$}}\_{t}) or other knife-edge cancellations. Consequently, the OLS estimator 𝜿^O​L​S\widehat{{\mbox{$\kappa$}}}^{OLS} is generically inconsistent under G​E​X​O​GGEXOG.

(iii)
:   Since G​E​X​O​G⊊E​B​DGEXOG\subsetneq EBD, the same generic inconsistency can arise within E​B​DEBD.

###### Proof.

See the Appendix.
∎

The mechanism in part (ii) is straightforward in the joint VAR/VMA framework. Although G​E​X​O​GGEXOG maintains innovation orthogonality 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}, it permits 𝒙t{\mbox{$x$}}\_{t} to depend on lagged disturbances through {𝚿x​u,j}\{{\mbox{$\Psi$}}\_{xu,j}\} (equivalently through {𝚵x​u,i}\{{\mbox{$\Xi$}}\_{xu,i}\}). When {𝚿u​u,j}\{{\mbox{$\Psi$}}\_{uu,j}\} generates serial dependence in 𝒖t{\mbox{$u$}}\_{t}, this feedback creates a nonzero contemporaneous covariance between 𝒙t{\mbox{$x$}}\_{t} and 𝒖t{\mbox{$u$}}\_{t}, so that the population orthogonality condition fails and the OLS probability limit differs from 𝜿\kappa.

A common response to serial correlation in 𝒖t{\mbox{$u$}}\_{t} is to adopt GLS-type procedures that model and remove the error dynamics. Such procedures do not, by themselves, resolve the endogeneity problem highlighted above when 𝔼​[𝑿t​𝒖t]≠𝟎{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]\neq{\mbox{$0$}}; nevertheless, they remain the workhorse approach in empirical time-series regressions and provide a useful benchmark. In practice, one typically proceeds in two steps: (i) estimate ([14](https://arxiv.org/html/2601.21272v1#S2.E14 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) by OLS and obtain residuals {𝒖^tO​L​S}\{\widehat{{\mbox{$u$}}}\_{t}^{OLS}\}, and (ii) fit a finite-order VAR model to the residual vector process, apply the [Cochrane and Orcutt](https://arxiv.org/html/2601.21272v1#bib.bib1857 "Application of least squares regression to relationships containing auto-correlated error terms")’s ([1949](https://arxiv.org/html/2601.21272v1#bib.bib1857 "Application of least squares regression to relationships containing auto-correlated error terms")) transformation, and obtain an estimator (hereafter, the CO-type estimators). In multiple-equation models, Nagakura ([2024](https://arxiv.org/html/2601.21272v1#bib.bib1985 "Cochrane–orcutt type estimator for multivariate linear regression model with serially correlated errors")) propose a CO-type estimator.

The multivariate CO-type estimator suppose that the (true) disturbance admits the VAR(p0p\_{0}) representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒖t=∑j=1p0𝚿u​u,j​𝒖t−j+𝜺u,t,𝔼​[𝜺u,t]=𝟎,𝔼​[𝜺u,t​𝜺u,t′]=𝚺u​u>0,{\mbox{$u$}}\_{t}=\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$u$}}\_{t-j}+{\mbox{$\varepsilon$}}\_{u,t},\qquad{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t}]={\mbox{$0$}},\quad{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$\Sigma$}}\_{uu}>0, |  | (16) |

with a stable characteristic polynomial 𝑷u​u​(z):=𝑰N−∑j=1p0𝚿u​u,j​zj{\mbox{$P$}}\_{uu}(z):={\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}z^{j} having no zeros in or on the unit disk. Define the lag polynomial

|  |  |  |
| --- | --- | --- |
|  | 𝑨​(L):=𝑰N−∑j=1p0𝚿u​u,j​Lj,{\mbox{$A$}}(L):={\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}L^{j}, |  |

and the transformed variables

|  |  |  |
| --- | --- | --- |
|  | 𝒚~t:=𝑨​(L)​𝒚t,𝒁~t′:=𝑨​(L)​𝒁t′,𝒖~t:=𝑨​(L)​𝒖t.\tilde{{\mbox{$y$}}}\_{t}:={\mbox{$A$}}(L){\mbox{$y$}}\_{t},\qquad\tilde{{\mbox{$Z$}}}\_{t}^{\prime}:={\mbox{$A$}}(L){\mbox{$Z$}}\_{t}^{\prime},\qquad\tilde{{\mbox{$u$}}}\_{t}:={\mbox{$A$}}(L){\mbox{$u$}}\_{t}. |  |

Under ([16](https://arxiv.org/html/2601.21272v1#S2.E16 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")), 𝒖~t=𝜺u,t\tilde{{\mbox{$u$}}}\_{t}={\mbox{$\varepsilon$}}\_{u,t}. The infeasible GLS estimator that uses (𝑨​(L),𝚺u​u)({\mbox{$A$}}(L),{\mbox{$\Sigma$}}\_{uu}) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜿^GLS​-​CO:=(∑t=p0+1T𝒁~t​𝚺u​u−1​𝒁~t′)−1​(∑t=p0+1T𝒁~t​𝚺u​u−1​𝒚~t).\widehat{{\mbox{$\kappa$}}}^{\tiny\mathrm{GLS\mbox{-}CO}}:=\Big(\sum\_{t=p\_{0}+1}^{T}\tilde{{\mbox{$Z$}}}\_{t}\,{\mbox{$\Sigma$}}\_{uu}^{-1}\tilde{{\mbox{$Z$}}}\_{t}^{\prime}\Big)^{-1}\Big(\sum\_{t=p\_{0}+1}^{T}\tilde{{\mbox{$Z$}}}\_{t}\,{\mbox{$\Sigma$}}\_{uu}^{-1}\tilde{{\mbox{$y$}}}\_{t}\Big). |  | (17) |

The feasible CO-type estimator 𝜿^FGLS​-​CO\widehat{{\mbox{$\kappa$}}}^{\tiny\mathrm{FGLS\mbox{-}CO}} is obtained by replacing (𝚿u​u,1,…,𝚿u​u,p0,𝚺u​u)({\mbox{$\Psi$}}\_{uu,1},\ldots,{\mbox{$\Psi$}}\_{uu,p\_{0}},{\mbox{$\Sigma$}}\_{uu}) by estimates (𝚿^u​u,1,…,𝚿^u​u,p0,𝚺^u​u)(\widehat{{\mbox{$\Psi$}}}\_{uu,1},\ldots,\widehat{{\mbox{$\Psi$}}}\_{uu,p\_{0}},\widehat{{\mbox{$\Sigma$}}}\_{uu}) computed from the first-step OLS residuals, and then applying the same formula ([17](https://arxiv.org/html/2601.21272v1#S2.E17 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) with the corresponding estimated filter 𝑨^​(L):=𝑰N−∑j=1p0𝚿^u​u,j​Lj\widehat{{\mbox{$A$}}}(L):={\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}\widehat{{\mbox{$\Psi$}}}\_{uu,j}L^{j} and 𝚺^u​u\widehat{{\mbox{$\Sigma$}}}\_{uu}. To ensure that the infeasible GLS estimator in ([17](https://arxiv.org/html/2601.21272v1#S2.E17 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is well defined, we impose a standard full-rank condition on the transformed regressors 𝒁~t′:=𝑨​(L)​𝒁t′\tilde{{\mbox{$Z$}}}\_{t}^{\prime}:={\mbox{$A$}}(L){\mbox{$Z$}}\_{t}^{\prime}.

###### Assumption 3:

𝑸~Z:=𝔼​[𝒁~t​𝚺u​u−1​𝒁~t′]\tilde{{\mbox{$Q$}}}\_{Z}:={\mathbb{E}}[\tilde{{\mbox{$Z$}}}\_{t}{\mbox{$\Sigma$}}\_{uu}^{-1}\tilde{{\mbox{$Z$}}}\_{t}^{\prime}] is positive definite.

This condition rules out degeneracy created by the Cochrane–Orcutt transformation; it is satisfied, for example, when the stacked vector (𝒁t′,𝒁t−1′,…,𝒁t−p0′)′({\mbox{$Z$}}\_{t}^{\prime},{\mbox{$Z$}}\_{t-1}^{\prime},\ldots,{\mbox{$Z$}}\_{t-p\_{0}}^{\prime})^{\prime} has a nonsingular second-moment matrix and 𝚺u​u≻0{\mbox{$\Sigma$}}\_{uu}\succ 0.

###### Proposition 5 (Consistency region of CO-type estimators):

Suppose that Assumptions [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")–[3](https://arxiv.org/html/2601.21272v1#Thmassumption3 "Assumption 3: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") hold and consider a two-step OLS-based GLS procedure (CO-type estimator) defined as follows:

1. 1.

   Estimate ([14](https://arxiv.org/html/2601.21272v1#S2.E14 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) by OLS and obtain residuals 𝒖^tO​L​S:=𝒚t−𝒁t′​𝜿^O​L​S\widehat{{\mbox{$u$}}}\_{t}^{\tiny OLS}:={\mbox{$y$}}\_{t}-{\mbox{$Z$}}\_{t}^{\prime}\widehat{{\mbox{$\kappa$}}}^{\tiny OLS}.
2. 2.

   Fit a VAR(p0p\_{0}) model (or an order selected consistently for p0p\_{0}) to {𝒖^tO​L​S}\{\widehat{{\mbox{$u$}}}\_{t}^{\tiny OLS}\}, construct the corresponding Cochrane–Orcutt transformation, and re-estimate ([14](https://arxiv.org/html/2601.21272v1#S2.E14 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) by OLS on the transformed system, yielding 𝜿^FGLS​-​CO\widehat{{\mbox{$\kappa$}}}^{\tiny\mathrm{FGLS\mbox{-}CO}}.

Then the following statements hold.

(i)
:   If the B​DBD condition holds (equivalently, covariance-based strict exogeneity holds), then 𝜿^FGLS​-​CO\widehat{{\mbox{$\kappa$}}}^{\tiny\mathrm{FGLS\mbox{-}CO}} is consistent for 𝛋\kappa. Moreover, 𝜿^FGLS​-​CO\widehat{{\mbox{$\kappa$}}}^{\tiny\mathrm{FGLS\mbox{-}CO}} is asymptotically equivalent to the infeasible GLS estimator that uses the true VAR law of motion for {𝒖t}\{{\mbox{$u$}}\_{t}\}, and hence attains asymptotic efficiency within the B​DBD class.

(ii)
:   Outside the B​DBD class, consistency of the CO-type estimator is not guaranteed and generically fails. In particular, under G​E​X​O​G∖B​DGEXOG\setminus BD the first-step OLS residuals do not consistently recover the true disturbance process, so the second-step GLS transformation is misspecified and the resulting estimator typically fails to converge to 𝛋\kappa (except under knife-edge parameter restrictions). Since G​E​X​O​G⊊E​B​DGEXOG\subsetneq EBD, the same phenomenon can arise within E​B​D∖B​DEBD\setminus BD.

###### Proof.

See the Appendix.
∎

Proposition [5](https://arxiv.org/html/2601.21272v1#Thmproposition5 "Proposition 5 (Consistency region of CO-type estimators): ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") also clarifies why innovation-based notions such as pre-determinedness and exogeneity, emphasized by Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")), become relevant when evaluating OLS-based GLS procedures. CO-type estimators first construct OLS residuals and then model the disturbance dynamics alone in the second step. In the joint VAR/VMA framework, this corresponds to maintaining an error model in which the law of motion for 𝒖t{\mbox{$u$}}\_{t} depends only on its own lags, that is, it excludes lagged regressors from the error dynamics (so it is correctly specified when 𝚿u​x,j=𝟎{\mbox{$\Psi$}}\_{ux,j}={\mbox{$0$}} for all jj), while treating the regressor process {𝒙t}\{{\mbox{$x$}}\_{t}\} as given when estimating the error law of motion. When this maintained restriction is violated, innovation orthogonality by itself does not prevent the first-step residuals from being contaminated, and the resulting GLS transformation becomes misspecified.

Taken together with Propositions [4](https://arxiv.org/html/2601.21272v1#Thmproposition4 "Proposition 4: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") and [5](https://arxiv.org/html/2601.21272v1#Thmproposition5 "Proposition 5 (Consistency region of CO-type estimators): ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), these results show that once the DGP departs from B​DBD, neither OLS nor OLS-based GLS procedures are reliably consistent in general. This motivates estimators that explicitly model the joint second-order dynamics of regressors and disturbances and are designed to remain consistent beyond the B​DBD class.

### 2.4 The inconsistency of FGLS-D estimator

A related but conceptually distinct approach is the FGLS procedure proposed by Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")) for a single-equation time-series regression model. Their analysis introduces innovation-based notions such as pre-determinedness and exogeneity, formulated in terms of the Wold innovations of the disturbance process.

Within our joint VAR/VMA framework, however, Proposition [2](https://arxiv.org/html/2601.21272v1#Thmproposition2 "Proposition 2: ‣ 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(ii) shows that pre-determined condition (defined using the joint Wold innovations of (𝒙t,𝒖t)({\mbox{$x$}}\_{t},{\mbox{$u$}}\_{t})) coincides with the E​B​DEBD class. This highlights an important distinction: pre-determined condition controls how 𝒙t{\mbox{$x$}}\_{t} relates to the contemporaneous uu-innovation, but it does not by itself restrict the dynamic feedback channels encoded in the off-diagonal VAR blocks. Consequently, an estimator that models the disturbance dynamics alone may still be misspecified on parts of the E​B​DEBD region.

The implementation in Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")) proceeds by fitting a finite-order model to the disturbance process and then quasi-differencing the regression using the estimated disturbance dynamics. In our block-VAR notation for 𝒛¯t=((𝒙t−𝝁x)′,𝒖t′)′\bar{{\mbox{$z$}}}\_{t}=(({\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x})^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime}, this corresponds to working under a maintained disturbance law of motion in which 𝒖t{\mbox{$u$}}\_{t} depends only on its own lags, namely

|  |  |  |
| --- | --- | --- |
|  | 𝒖t=∑j=1p0𝚿u​u,j​𝒖t−j+𝜺u,t,equivalently ​𝚿u​x,j=𝟎​ for all ​j,{\mbox{$u$}}\_{t}=\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$u$}}\_{t-j}+{\mbox{$\varepsilon$}}\_{u,t},\qquad\text{equivalently }\ {\mbox{$\Psi$}}\_{ux,j}={\mbox{$0$}}\ \text{ for all }j, |  |

while allowing 𝒙t{\mbox{$x$}}\_{t} to load on lagged disturbances through {𝚿x​u,j}\{{\mbox{$\Psi$}}\_{xu,j}\}. This maintained restriction aligns with the upper block-triangular region that we call G​E​X​O​GGEXOG. Accordingly, in what follows we derive the multivariate analogue of the FGLS-D procedure under G​E​X​O​GGEXOG and characterize its consistency region relative to B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD.

Under G​E​X​O​GGEXOG, the joint VAR(p0p\_{0}) law of motion allows feedback from lagged disturbances to the regressors but rules out feedback from lagged regressors to the disturbance. That is, 𝚿u​x,j=𝟎{\mbox{$\Psi$}}\_{ux,j}={\mbox{$0$}} for all jj, while 𝚿x​u,j{\mbox{$\Psi$}}\_{xu,j} may be nonzero. Imposing this restriction on ([5](https://arxiv.org/html/2601.21272v1#S2.E5 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"))–([6](https://arxiv.org/html/2601.21272v1#S2.E6 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒙t−𝝁x=\displaystyle{\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x}= | ∑j=1p0𝚿x​x,j​(𝒙t−j−𝝁x)+∑j=1p0𝚿x​u,j​𝒖t−j+𝜺x,t,\displaystyle\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{xx,j}\big({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x}\big)+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{xu,j}{\mbox{$u$}}\_{t-j}+{\mbox{$\varepsilon$}}\_{x,t}, |  | (18) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒖t=\displaystyle{\mbox{$u$}}\_{t}= | ∑j=1p0𝚿u​u,j​𝒖t−j+𝜺u,t,\displaystyle\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$u$}}\_{t-j}+{\mbox{$\varepsilon$}}\_{u,t}, |  | (19) |

where the dynamic feedback from 𝒙t{\mbox{$x$}}\_{t} to 𝒖t{\mbox{$u$}}\_{t} is ruled out by imposing 𝚿u​x,j=𝟎{\mbox{$\Psi$}}\_{ux,j}={\mbox{$0$}} for all jj, while feedback from past disturbances to the regressors is allowed through 𝚿x​u,j{\mbox{$\Psi$}}\_{xu,j}.

Substituting ([19](https://arxiv.org/html/2601.21272v1#S2.E19 "In 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) for 𝒖t{\mbox{$u$}}\_{t} into ([2](https://arxiv.org/html/2601.21272v1#S2.E2 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) yields the following regression

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚t=\displaystyle{\mbox{$y$}}\_{t}= | 𝜶+𝑿t′​𝜷+∑j=1p0𝚿u​u,j​𝒖t−j+𝜺u,t\displaystyle{\mbox{$\alpha$}}+{\mbox{$X$}}\_{t}^{\prime}{\mbox{$\beta$}}+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$u$}}\_{t-j}+{\mbox{$\varepsilon$}}\_{u,t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝜶+𝑿t′​𝜷+∑j=1p0𝚿u​u,j​(𝒚t−j−𝑿t−j′​𝜷−𝜶)+𝜺u,t\displaystyle{\mbox{$\alpha$}}+{\mbox{$X$}}\_{t}^{\prime}{\mbox{$\beta$}}+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}\bigl({\mbox{$y$}}\_{t-j}-{\mbox{$X$}}\_{t-j}^{\prime}{\mbox{$\beta$}}-{\mbox{$\alpha$}}\bigr)+{\mbox{$\varepsilon$}}\_{u,t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | (𝑰N−∑j=1p0𝚿u​u,j)​𝜶+𝑿t′​𝜷−∑j=1p0𝚿u​u,j​𝑿t−j′​𝜷+∑j=1p0𝚿u​u,j​𝒚t−j+𝜺u,t.\displaystyle\Bigl({\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}\Bigr){\mbox{$\alpha$}}+{\mbox{$X$}}\_{t}^{\prime}{\mbox{$\beta$}}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$X$}}\_{t-j}^{\prime}{\mbox{$\beta$}}+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$y$}}\_{t-j}+{\mbox{$\varepsilon$}}\_{u,t}. |  | (20) |

Using 𝑿t′​𝜷=𝑩𝒙t{\mbox{$X$}}\_{t}^{\prime}{\mbox{$\beta$}}={\mbox{$B$}}{\mbox{$x$}}\_{t} with 𝑩:=blkdiag​(𝜷1′,…,𝜷N′)∈ℝN×K{\mbox{$B$}}:=\mathrm{blkdiag}({\mbox{$\beta$}}\_{1}^{\prime},\ldots,{\mbox{$\beta$}}\_{N}^{\prime})\in\mathbb{R}^{N\times K}, the term −∑j=1p0𝚿u​u,j​𝑿t−j′​𝜷-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$X$}}\_{t-j}^{\prime}{\mbox{$\beta$}} in ([20](https://arxiv.org/html/2601.21272v1#S2.E20 "In 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | −∑j=1p0𝚿u​u,j​𝑿t−j′​𝜷=−∑j=1p0𝚿u​u,j​𝑩​𝒙t−j=∑j=1p0𝚫j​𝒙t−j,-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$X$}}\_{t-j}^{\prime}{\mbox{$\beta$}}=-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$B$}}\,{\mbox{$x$}}\_{t-j}=\sum\_{j=1}^{p\_{0}}{\mbox{$\Delta$}}\_{j}\,{\mbox{$x$}}\_{t-j}, |  |

where, at the population level,

|  |  |  |
| --- | --- | --- |
|  | 𝚫j:=−𝚿u​u,j​𝑩,j=1,…,p0.{\mbox{$\Delta$}}\_{j}:=-{\mbox{$\Psi$}}\_{uu,j}{\mbox{$B$}},\qquad j=1,\ldots,p\_{0}. |  |

For estimation, however, we treat {𝚫j}j=1p0\{{\mbox{$\Delta$}}\_{j}\}\_{j=1}^{p\_{0}} as unrestricted nuisance parameters so that the augmented regression remains linear in the unknown coefficients. This reparameterization does not change the population regression implied by G​E​X​O​GGEXOG; it merely avoids imposing the bilinear cross-parameter restriction 𝚫j=−𝚿u​u,j​𝑩{\mbox{$\Delta$}}\_{j}=-{\mbox{$\Psi$}}\_{uu,j}{\mbox{$B$}} during estimation.

With this linear reparameterization, ([20](https://arxiv.org/html/2601.21272v1#S2.E20 "In 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) becomes a linear regression model in which 𝒄c, 𝜷\beta, {𝚿u​u,j}j=1p0\{{\mbox{$\Psi$}}\_{uu,j}\}\_{j=1}^{p\_{0}}, and {𝚫j}j=1p0\{{\mbox{$\Delta$}}\_{j}\}\_{j=1}^{p\_{0}} enter linearly. Hence the first step of the FGLS-D procedure can be implemented by equation-by-equation OLS: for each i=1,…,Ni=1,\ldots,N, regress yi,ty\_{i,t} on the contemporaneous regressors in equation ii, the lagged dependent vectors {𝒚t−j}j=1p0\{{\mbox{$y$}}\_{t-j}\}\_{j=1}^{p\_{0}}, and the chosen lagged regressor vector(s) (e.g. {𝒙t−j}j=1p0\{{\mbox{$x$}}\_{t-j}\}\_{j=1}^{p\_{0}} or {𝒙i,t−j}j=1p0\{{\mbox{$x$}}\_{i,t-j}\}\_{j=1}^{p\_{0}}). Collecting the estimated coefficients on {𝒚t−j}j=1p0\{{\mbox{$y$}}\_{t-j}\}\_{j=1}^{p\_{0}} across ii yields 𝚿^u​u,1,…,𝚿^u​u,p0\widehat{{\mbox{$\Psi$}}}\_{uu,1},\ldots,\widehat{{\mbox{$\Psi$}}}\_{uu,p\_{0}}, and collecting those on the lagged regressor terms yields 𝚫^1,…,𝚫^p0\widehat{{\mbox{$\Delta$}}}\_{1},\ldots,\widehat{{\mbox{$\Delta$}}}\_{p\_{0}}, together with residuals 𝜺^u,t\widehat{{\mbox{$\varepsilon$}}}\_{u,t} used to estimate 𝚺u​u{\mbox{$\Sigma$}}\_{uu}. This leads to the following two-step FGLS-D procedure.

(Step 1) OLS estimation of the augmented regression and VAR error dynamics.
:   For each equation i=1,…,Ni=1,\ldots,N, run OLS on ([20](https://arxiv.org/html/2601.21272v1#S2.E20 "In 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")):

    |  |  |  |
    | --- | --- | --- |
    |  | yi,t=ci+𝒙i,t′​𝜷i+∑j=1p0𝒚t−j′​𝝍u​u,j,i+∑j=1p0𝒙t−j′​𝜹j,i+εu,i,t,y\_{i,t}=c\_{i}+{\mbox{$x$}}\_{i,t}^{\prime}{\mbox{$\beta$}}\_{i}+\sum\_{j=1}^{p\_{0}}{\mbox{$y$}}\_{t-j}^{\prime}{\mbox{$\psi$}}\_{uu,j,i}+\sum\_{j=1}^{p\_{0}}{\mbox{$x$}}\_{t-j}^{\prime}{\mbox{$\delta$}}\_{j,i}+\varepsilon\_{u,i,t}, |  |

    where 𝝍u​u,j,i′{\mbox{$\psi$}}\_{uu,j,i}^{\prime} is the ii-th row of 𝚿u​u,j{\mbox{$\Psi$}}\_{uu,j} and 𝜹j,i′{\mbox{$\delta$}}\_{j,i}^{\prime} is the ii-th row of 𝚫j{\mbox{$\Delta$}}\_{j}. Collecting {𝝍^u​u,j,i′}i=1N\{\widehat{{\mbox{$\psi$}}}\_{uu,j,i}^{\prime}\}\_{i=1}^{N} yields 𝚿^u​u,j∈ℝN×N\widehat{{\mbox{$\Psi$}}}\_{uu,j}\in\mathbb{R}^{N\times N} for each j=1,…,p0j=1,\ldots,p\_{0}. Using the OLS residuals

    |  |  |  |
    | --- | --- | --- |
    |  | 𝜺^u,t(1):=𝒚t−𝒄^−𝑿t′​𝜷^−∑j=1p0𝚿^u​u,j​𝒚t−j−∑j=1p0𝚫^j​𝒙t−j,\widehat{{\mbox{$\varepsilon$}}}\_{u,t}^{(1)}:={\mbox{$y$}}\_{t}-\widehat{{\mbox{$c$}}}-{\mbox{$X$}}\_{t}^{\prime}\widehat{{\mbox{$\beta$}}}-\sum\_{j=1}^{p\_{0}}\widehat{{\mbox{$\Psi$}}}\_{uu,j}{\mbox{$y$}}\_{t-j}-\sum\_{j=1}^{p\_{0}}\widehat{{\mbox{$\Delta$}}}\_{j}{\mbox{$x$}}\_{t-j}, |  |

    estimate the innovation covariance matrix by

    |  |  |  |
    | --- | --- | --- |
    |  | 𝚺^u​u:=1T−p0​∑t=p0+1T𝜺^u,t(1)​(𝜺^u,t(1))′.\widehat{{\mbox{$\Sigma$}}}\_{uu}:=\frac{1}{T-p\_{0}}\sum\_{t=p\_{0}+1}^{T}\widehat{{\mbox{$\varepsilon$}}}\_{u,t}^{(1)}(\widehat{{\mbox{$\varepsilon$}}}\_{u,t}^{(1)})^{\prime}. |  |

(Step 2) Quasi-differencing and GLS on the filtered system.
:   Using 𝚿^u​u,1,…,𝚿^u​u,p0\widehat{{\mbox{$\Psi$}}}\_{uu,1},\ldots,\widehat{{\mbox{$\Psi$}}}\_{uu,p\_{0}} from
    Step 1, construct the filtered (or “quasi-differenced”) series

    |  |  |  |
    | --- | --- | --- |
    |  | 𝒚FD,t:=𝒚t−∑j=1p0𝚿^u​u,j​𝒚t−j,𝑿FD,t′:=𝑿t′−∑j=1p0𝚿^u​u,j​𝑿t−j′,{\mbox{$y$}}\_{\mathrm{FD},t}:={\mbox{$y$}}\_{t}-\sum\_{j=1}^{p\_{0}}\widehat{{\mbox{$\Psi$}}}\_{uu,j}{\mbox{$y$}}\_{t-j},\qquad{\mbox{$X$}}\_{\mathrm{FD},t}^{\prime}:={\mbox{$X$}}\_{t}^{\prime}-\sum\_{j=1}^{p\_{0}}\widehat{{\mbox{$\Psi$}}}\_{uu,j}{\mbox{$X$}}\_{t-j}^{\prime}, |  |

    and define

    |  |  |  |
    | --- | --- | --- |
    |  | 𝒁FD,t′:=[(𝑰N−∑j=1p0𝚿^u​u,j),𝑿FD,t′],𝜿:=(𝜶′,𝜷′)′.{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}:=\biggl[\Bigl({\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}\widehat{{\mbox{$\Psi$}}}\_{uu,j}\Bigr),\ \ {\mbox{$X$}}\_{\mathrm{FD},t}^{\prime}\biggr],\qquad{\mbox{$\kappa$}}:=({\mbox{$\alpha$}}^{\prime},{\mbox{$\beta$}}^{\prime})^{\prime}. |  |

    Under the G​E​X​O​GGEXOG restriction and Assumptions [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")–[2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), the filtered regression satisfies

    |  |  |  |
    | --- | --- | --- |
    |  | 𝒚FD,t=𝒁FD,t′​𝜿+𝜺u,t.{\mbox{$y$}}\_{\mathrm{FD},t}={\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}{\mbox{$\kappa$}}+{\mbox{$\varepsilon$}}\_{u,t}. |  |

    The multivariate FGLS-D estimator is then given by

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | 𝜿^FGLS−D:=(∑t=p0+1T𝒁FD,t​𝚺^u​u−1​𝒁FD,t′)−1​(∑t=p0+1T𝒁FD,t​𝚺^u​u−1​𝒚FD,t).\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS\!-\!D}}:=\Biggl(\sum\_{t=p\_{0}+1}^{T}{\mbox{$Z$}}\_{\mathrm{FD},t}\,\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}\,{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}\Biggr)^{-1}\Biggl(\sum\_{t=p\_{0}+1}^{T}{\mbox{$Z$}}\_{\mathrm{FD},t}\,\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}\,{\mbox{$y$}}\_{\mathrm{FD},t}\Biggr). |  | (21) |

The above algorithm defines the multivariate FGLS-D estimator as a two-step procedure that (i) estimates an augmented regression implied by the restricted joint VAR structure under G​E​X​O​GGEXOG, and (ii) applies a quasi-differencing based on the estimated error dynamics, followed by GLS with respect to the innovation covariance 𝚺u​u{\mbox{$\Sigma$}}\_{uu}. Intuitively, this construction exploits GLS-type corrections for serial correlation and cross-equation innovation covariance while relaxing the full block-diagonality of the B​DBD condition by allowing lagged disturbances to affect the regressors (i.e., 𝚿x​u,j≠𝟎{\mbox{$\Psi$}}\_{xu,j}\neq{\mbox{$0$}}), yet maintaining the G​E​X​O​GGEXOG restriction 𝚿u​x,j=𝟎{\mbox{$\Psi$}}\_{ux,j}={\mbox{$0$}} and innovation orthogonality. To ensure that the second-step GLS estimator in ([21](https://arxiv.org/html/2601.21272v1#S2.E21 "In item (Step 2) Quasi-differencing and GLS on the filtered system. ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is well defined, we impose a full-rank condition on the filtered regressors.

###### Assumption 4:

𝑸FD:=𝔼​[𝒁FD,t​𝚺u​u−1​𝒁FD,t′]{\mbox{$Q$}}\_{\mathrm{FD}}:={\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}] is positive definite.

Assumption [4](https://arxiv.org/html/2601.21272v1#Thmassumption4 "Assumption 4: ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") guarantees that the population GLS information matrix is nonsingular. In addition, under consistency of 𝚺^u​u\widehat{{\mbox{$\Sigma$}}}\_{uu} (shown below), we have 𝚺^u​u−1→𝑝𝚺u​u−1\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}\xrightarrow{p}{\mbox{$\Sigma$}}\_{uu}^{-1}, and hence 1/(T−p0)​∑t=p0+1T𝒁FD,t​𝚺^u​u−1​𝒁FD,t′→𝑝𝑸FD≻01/(T-p\_{0})\sum\_{t=p\_{0}+1}^{T}{\mbox{$Z$}}\_{\mathrm{FD},t}\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}\xrightarrow{p}{\mbox{$Q$}}\_{\mathrm{FD}}\succ 0, so the sample matrix in ([21](https://arxiv.org/html/2601.21272v1#S2.E21 "In item (Step 2) Quasi-differencing and GLS on the filtered system. ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is nonsingular with probability approaching one.

The next proposition establishes the asymptotic properties of the multivariate FGLS-D estimator within the B​DBD/G​E​X​O​GGEXOG/E​B​DEBD framework and clarifies the extent to which it extends the consistency region relative to OLS- and CO-type estimators.

###### Proposition 6 (Consistency region of the FGLS-D estimator):

Suppose that Assumptions [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")–[2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), [4](https://arxiv.org/html/2601.21272v1#Thmassumption4 "Assumption 4: ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") hold and that the VAR order p0p\_{0} in the disturbance dynamics is fixed and correctly specified. Let 𝛋^FGLS−D\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS\!-\!D}} be the multivariate FGLS-D estimator defined by ([20](https://arxiv.org/html/2601.21272v1#S2.E20 "In 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"))–([21](https://arxiv.org/html/2601.21272v1#S2.E21 "In item (Step 2) Quasi-differencing and GLS on the filtered system. ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")). Then:

(i)
:   If the data-generating process satisfies the G​E​X​O​GGEXOG condition, then 𝜿^FGLS−D→𝑝𝜿=(𝜶′,𝜷′)′\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS\!-\!D}}\xrightarrow{p}{\mbox{$\kappa$}}=({\mbox{$\alpha$}}^{\prime},{\mbox{$\beta$}}^{\prime})^{\prime}. Moreover, 𝜿^FGLS−D\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS\!-\!D}} is asymptotically equivalent to the infeasible GLS estimator that quasi-differences the system using the true lag polynomial 𝑨​(L):=𝑰N−∑j=1p0𝚿u​u,j​Lj{\mbox{$A$}}(L):={\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}L^{j} and uses the true innovation covariance matrix 𝚺u​u{\mbox{$\Sigma$}}\_{uu}; in particular, T​(𝜿^FGLS−D−𝜿)\sqrt{T}\big(\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS\!-\!D}}-{\mbox{$\kappa$}}\big) has the same limiting distribution as its infeasible GLS counterpart. Under the B​DBD condition, this implies that 𝜿^FGLS−D\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS\!-\!D}} is asymptotically equivalent to the usual Cochrane–Orcutt-type GLS estimator based on the marginal VAR for {𝒖t}\{{\mbox{$u$}}\_{t}\}.

(ii)
:   If the data-generating process lies in E​B​D∖G​E​X​O​GEBD\setminus GEXOG (i.e., 𝚿u​x,j≠𝟎{\mbox{$\Psi$}}\_{ux,j}\neq{\mbox{$0$}} for some jj), then 𝜿^FGLS−D\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS\!-\!D}} is generically inconsistent for 𝛋\kappa (except under knife-edge parameter cancellations). In this region, {𝒖t}\{{\mbox{$u$}}\_{t}\} does not follow a closed VAR driven only by its own lags, so the quasi-differencing filter based solely on {𝚿u​u,j}\{{\mbox{$\Psi$}}\_{uu,j}\} is misspecified, and the second-step GLS regression in ([21](https://arxiv.org/html/2601.21272v1#S2.E21 "In item (Step 2) Quasi-differencing and GLS on the filtered system. ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is constructed under an incorrect error structure.

###### Proof.

See the Appendix.
∎

Proposition [6](https://arxiv.org/html/2601.21272v1#Thmproposition6 "Proposition 6 (Consistency region of the FGLS-D estimator): ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") clarifies the role of the FGLS-D estimator within the B​DBD/G​E​X​O​GGEXOG/E​B​DEBD framework. While OLS-based CO-type procedures are only guaranteed to be consistent under the narrow B​DBD class (and typically fail outside B​DBD), FGLS-D remains consistent on the larger G​E​X​O​GGEXOG region and is asymptotically equivalent to the corresponding infeasible GLS estimator within that class. In particular, even when the regressors load on lagged disturbances so that contemporaneous orthogonality—and hence OLS consistency—fails generically, the one-sided feedback structure of G​E​X​O​GGEXOG ensures that {𝒖t}\{{\mbox{$u$}}\_{t}\} admits a closed VAR(p0p\_{0}) representation driven by {𝜺u,t}\{{\mbox{$\varepsilon$}}\_{u,t}\}. Consequently, the quasi-differencing step based on the estimated {𝚿u​u,j}\{{\mbox{$\Psi$}}\_{uu,j}\} is asymptotically correctly specified, delivering an infeasible-GLS-equivalent estimator.

At the same time, Proposition [6](https://arxiv.org/html/2601.21272v1#Thmproposition6 "Proposition 6 (Consistency region of the FGLS-D estimator): ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(ii) highlights a structural limitation of FGLS-D that stems from its reliance on the restricted VAR for {𝒖t}\{{\mbox{$u$}}\_{t}\}. Once the DGP moves beyond G​E​X​O​GGEXOG into the more general E​B​D∖G​E​X​O​GEBD\setminus GEXOG region, {𝒖t}\{{\mbox{$u$}}\_{t}\} no longer follows a closed VAR driven solely by its own lags, and the quasi-differencing filter based only on {𝚿u​u,j}\{{\mbox{$\Psi$}}\_{uu,j}\} becomes misspecified. In this sense, OLS, CO-type GLS, and FGLS-D each rely—in different ways—on variants of the B​DBD/G​E​X​O​GGEXOG structure and do not provide a fully robust solution when bidirectional dynamic feedback between regressors and disturbances is present. This motivates the generalized Durbin-type estimators developed in the next subsection, which are designed to retain consistency under the weakest E​B​DEBD condition.

### 2.5 Asymptotic properties of generalized Durbin estimator

We extend Durbin regression to a multiple-equation framework and derive an estimator that remains consistent under the B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD conditions. Starting from ([2](https://arxiv.org/html/2601.21272v1#S2.E2 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")), we obtain a multiple-equation specification by exploiting the blockwise VAR(p0p\_{0}) representation of 𝒛¯t\bar{{\mbox{$z$}}}\_{t} given in Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒙t−𝝁x=\displaystyle{\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x}= | ∑j=1p0𝚿x​x,j​(𝒙t−j−𝝁x)+∑j=1p0𝚿x​u,j​𝒖t−j+𝜺x,t,\displaystyle\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{xx,j}\big({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x}\big)+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{xu,j}{\mbox{$u$}}\_{t-j}+{\mbox{$\varepsilon$}}\_{x,t}, |  | (22) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒖t=\displaystyle{\mbox{$u$}}\_{t}= | ∑j=1p0𝚿u​x,j​(𝒙t−j−𝝁x)+∑j=1p0𝚿u​u,j​𝒖t−j+𝜺u,t.\displaystyle\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{ux,j}\big({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x}\big)+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$u$}}\_{t-j}+{\mbox{$\varepsilon$}}\_{u,t}. |  | (23) |

Substituting ([23](https://arxiv.org/html/2601.21272v1#S2.E23 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) for 𝒖t{\mbox{$u$}}\_{t} into ([2](https://arxiv.org/html/2601.21272v1#S2.E2 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) yields the following regression model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚t=𝜸+𝑿t′​𝜷+∑j=1p0𝚿u​u,j​𝒚t−j+∑j=1p0𝚲j​𝒙t−j+𝜺u,t,{\mbox{$y$}}\_{t}={\mbox{$\gamma$}}+{\mbox{$X$}}\_{t}^{\prime}{\mbox{$\beta$}}+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$y$}}\_{t-j}+\sum\_{j=1}^{p\_{0}}{\mbox{$\Lambda$}}\_{j}{\mbox{$x$}}\_{t-j}+{\mbox{$\varepsilon$}}\_{u,t}, |  | (24) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝜸=(𝑰N−∑j=1p0𝚿u​u,j)​𝜶−∑j=1p0𝚿u​x,j​𝝁x,𝚲j=𝚿u​x,j−𝚿u​u,j​𝑩,{\mbox{$\gamma$}}=\bigl({\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}\bigr){\mbox{$\alpha$}}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{ux,j}{\mbox{$\mu$}}\_{x},\quad{\mbox{$\Lambda$}}\_{j}={\mbox{$\Psi$}}\_{ux,j}-{\mbox{$\Psi$}}\_{uu,j}{\mbox{$B$}}, |  |

and 𝑩=blkdiag​(𝜷1′,𝜷2′,…,𝜷N′){\mbox{$B$}}=\mathrm{blkdiag}\big({\mbox{$\beta$}}\_{1}^{\prime},{\mbox{$\beta$}}\_{2}^{\prime},\ldots,{\mbox{$\beta$}}\_{N}^{\prime}\big).

For estimation, we treat {𝚲j}j=1p0\{{\mbox{$\Lambda$}}\_{j}\}\_{j=1}^{p\_{0}} as unrestricted nuisance parameters so that the augmented regression remains linear in the unknown coefficients. This reparameterization does not alter the population regression implied by ([23](https://arxiv.org/html/2601.21272v1#S2.E23 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")); it simply avoids imposing the bilinear cross-parameter restriction 𝚲j=𝚿u​x,j−𝚿u​u,j​𝑩{\mbox{$\Lambda$}}\_{j}={\mbox{$\Psi$}}\_{ux,j}-{\mbox{$\Psi$}}\_{uu,j}{\mbox{$B$}} during estimation.

With this linear reparameterization, ([24](https://arxiv.org/html/2601.21272v1#S2.E24 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) can be estimated equation by equation. Specifically, for each i=1,…,Ni=1,\ldots,N we consider the ii-th equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi,t=γi+𝒙i,t′​𝜷i+∑j=1p0𝒚t−j′​𝝍u​u,j,i+∑j=1p0𝒙t−j′​𝝀j,i+εu,i,t,y\_{i,t}=\gamma\_{i}+{\mbox{$x$}}\_{i,t}^{\prime}{\mbox{$\beta$}}\_{i}+\sum\_{j=1}^{p\_{0}}{\mbox{$y$}}\_{t-j}^{\prime}{\mbox{$\psi$}}\_{uu,j,i}+\sum\_{j=1}^{p\_{0}}{\mbox{$x$}}\_{t-j}^{\prime}{\mbox{$\lambda$}}\_{j,i}+\varepsilon\_{u,i,t}, |  | (25) |

where 𝝍u​u,j,i′{\mbox{$\psi$}}\_{uu,j,i}^{\prime} denotes the ii-th row of 𝚿u​u,j{\mbox{$\Psi$}}\_{uu,j} (so that 𝝍u​u,j,i∈ℝN{\mbox{$\psi$}}\_{uu,j,i}\in\mathbb{R}^{N}), and 𝝀j,i{\mbox{$\lambda$}}\_{j,i} denotes the coefficient vector associated with 𝒙t−j{\mbox{$x$}}\_{t-j} in the ii-th equation (equivalently, 𝝀j,i′{\mbox{$\lambda$}}\_{j,i}^{\prime} is the ii-th row of 𝚲j{\mbox{$\Lambda$}}\_{j}). Importantly, while the lagged dependent vectors {𝒚t−j}\{{\mbox{$y$}}\_{t-j}\} and the stacked lagged regressor vectors {𝒙t−j}\{{\mbox{$x$}}\_{t-j}\} are common across equations by construction, the contemporaneous regressors 𝒙i,t{\mbox{$x$}}\_{i,t} and the slope parameters 𝜷i{\mbox{$\beta$}}\_{i} may differ across ii.

For each i=1,…,Ni=1,\ldots,N, define the equation-specific regressor vector

|  |  |  |
| --- | --- | --- |
|  | 𝒘i,t:=[1,𝒙i,t′,𝒚t−1′,…𝒚t−p0′,𝒙t−1′,…𝒙t−p0′,]′∈ℝdi,di:=1+ki+p0​N+p0​k,{\mbox{$w$}}\_{i,t}:=\begin{bmatrix}1,&{\mbox{$x$}}\_{i,t}^{\prime},&{\mbox{$y$}}\_{t-1}^{\prime},&\ldots&{\mbox{$y$}}\_{t-p\_{0}}^{\prime},&{\mbox{$x$}}\_{t-1}^{\prime},&\ldots&{\mbox{$x$}}\_{t-p\_{0}}^{\prime},&\end{bmatrix}^{\prime}\in\mathbb{R}^{d\_{i}},\quad d\_{i}:=1+k\_{i}+p\_{0}N+p\_{0}k, |  |

and the corresponding parameter vector

|  |  |  |
| --- | --- | --- |
|  | 𝜽i:=[γi𝜷i′𝝍u​u,1,i′​…𝝍u​u,p0,i′𝝀1,i′…𝝀p0,i′]′∈ℝdi.{\mbox{$\theta$}}\_{i}:=\begin{bmatrix}\gamma\_{i}&{\mbox{$\beta$}}\_{i}^{\prime}&{\mbox{$\psi$}}\_{uu,1,i}^{\prime}\ldots&{\mbox{$\psi$}}\_{uu,p\_{0},i}^{\prime}&{\mbox{$\lambda$}}\_{1,i}^{\prime}&\ldots&{\mbox{$\lambda$}}\_{p\_{0},i}^{\prime}\end{bmatrix}^{\prime}\in\mathbb{R}^{d\_{i}}. |  |

Then the ii-th equation ([25](https://arxiv.org/html/2601.21272v1#S2.E25 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) can be written compactly as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi,t=𝒘i,t′​𝜽i+εu,i,t.y\_{i,t}={\mbox{$w$}}\_{i,t}^{\prime}{\mbox{$\theta$}}\_{i}+\varepsilon\_{u,i,t}. |  | (26) |

###### Lemma 1 (Equation-by-equation properties of the Durbin regression):

Suppose Assumptions [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")–[2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") hold, and let
yi,t=𝐰i,t′​𝛉i+εu,i,ty\_{i,t}={\mbox{$w$}}\_{i,t}^{\prime}{\mbox{$\theta$}}\_{i}+\varepsilon\_{u,i,t} be defined as above.
Then, for each i=1,…,Ni=1,\ldots,N, the following statements hold.

(i)
:   There exist an ℱt−1:=σ(𝒛s:s≤t−1)\mathscr{F}\_{t-1}:=\sigma({\mbox{$z$}}\_{s}:s\leq t-1)-measurable vector 𝒉i,t∈ℝdi{\mbox{$h$}}\_{i,t}\in\mathbb{R}^{d\_{i}} and a deterministic linear map 𝒎i:ℝk→ℝdi{\mbox{$m$}}\_{i}:\mathbb{R}^{k}\to\mathbb{R}^{d\_{i}} such that

    |  |  |  |
    | --- | --- | --- |
    |  | 𝒘i,t=𝒉i,t+𝒎i​𝜺x,t.{\mbox{$w$}}\_{i,t}={\mbox{$h$}}\_{i,t}+{\mbox{$m$}}\_{i}\,{\mbox{$\varepsilon$}}\_{x,t}. |  |

    Hence 𝒘i,t{\mbox{$w$}}\_{i,t} is measurable with respect to σ​(ℱt−1,𝜺x,t)\sigma(\mathscr{F}\_{t-1},{\mbox{$\varepsilon$}}\_{x,t}). Moreover, if the innovation orthogonality condition

    |  |  |  |
    | --- | --- | --- |
    |  | 𝚺x​u:=𝔼​[𝜺x,t​𝜺u,t′]=𝟎{\mbox{$\Sigma$}}\_{xu}:={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{x,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$0$}} |  |

    holds (as it does under B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD), then

    |  |  |  |
    | --- | --- | --- |
    |  | 𝔼​[𝒘i,t​εu,i,t]=𝟎.{\mathbb{E}}[{\mbox{$w$}}\_{i,t}\,\varepsilon\_{u,i,t}]={\mbox{$0$}}. |  |

(ii)
:   𝔼​‖𝒘i,t‖2+δ<∞{\mathbb{E}}\|{\mbox{$w$}}\_{i,t}\|^{2+\delta}<\infty and 𝔼​‖𝒘i,t​εu,i,t‖2+δ<∞{\mathbb{E}}\|{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}\|^{2+\delta}<\infty.

(iii)
:   The second-moment matrices 𝑸w,i:=𝔼​[𝒘i,t​𝒘i,t′]{\mbox{$Q$}}\_{w,i}:={\mathbb{E}}[{\mbox{$w$}}\_{i,t}{\mbox{$w$}}\_{i,t}^{\prime}] is positive definite.

###### Proof.

See the Appendix.
∎

Lemma [1](https://arxiv.org/html/2601.21272v1#Thmlemma1 "Lemma 1 (Equation-by-equation properties of the Durbin regression): ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") summarizes the key properties of the augmented regressor vector 𝒘i,t{\mbox{$w$}}\_{i,t} that are used to analyze the generalized Durbin estimator. Part (i) shows that, under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") and the innovation orthogonality condition 𝚺x​u=𝔼​[𝜺x,t​𝜺u,t′]=𝟎{\mbox{$\Sigma$}}\_{xu}={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{x,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$0$}} (satisfied by all B​DBD/G​E​X​O​GGEXOG/E​B​DEBD conditions), the population orthogonality condition 𝔼​[𝒘i,t​εu,i,t]=0{\mathbb{E}}[{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}]=0 holds. Therefore, although {𝒙t}\{{\mbox{$x$}}\_{t}\} and {𝒖t}\{{\mbox{$u$}}\_{t}\} may exhibit rich dynamic feedback through the VAR coefficients {𝚿j}\{{\mbox{$\Psi$}}\_{j}\}, the population normal equations for the first-step regression yi,t=𝒘i,t′​𝜽i+εu,i,ty\_{i,t}={\mbox{$w$}}\_{i,t}^{\prime}{\mbox{$\theta$}}\_{i}+\varepsilon\_{u,i,t} remain correctly specified. Parts (ii) and (iii) provide the moment and nonsingularity conditions (together with the weak-dependence regularity implied by Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) that ensure a law of large numbers and a central limit theorem apply to the sample moments involving 𝒘i,t{\mbox{$w$}}\_{i,t}. These results will be used to establish consistency and derive the asymptotic distribution of the proposed equation-by-equation estimator.

Before deriving the asymptotic results, we first show that the Bayesian information criterion (BIC) of Schwarz ([1978](https://arxiv.org/html/2601.21272v1#bib.bib1913 "Estimating the dimension of a model")) consistently selects the true lag order. Consequently, we may replace the unknown p0p\_{0} with the data-driven choice p^BIC\widehat{p}\_{\mathrm{BIC}} without affecting the limiting distribution of the estimators.

###### Lemma 2:

Suppose Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")–[2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") and the E​B​DEBD condition hold. Let the candidate set be 𝒫={1,…,pmax}\mathcal{P}=\{1,\dots,p\_{\max}\} with fixed pmax≥p0p\_{\max}\geq p\_{0}. For each p∈𝒫p\in\mathcal{P}, estimate ([26](https://arxiv.org/html/2601.21272v1#S2.E26 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) equation by equation with pp lags and obtain residuals {ε^u,i,t​(p)}\{\widehat{\varepsilon}\_{u,i,t}(p)\}. Stack them as 𝛆^u,t​(p):=(ε^u,1,t​(p),…,ε^u,N,t​(p))′\widehat{{\mbox{$\varepsilon$}}}\_{u,t}(p):=(\widehat{\varepsilon}\_{u,1,t}(p),\ldots,\widehat{\varepsilon}\_{u,N,t}(p))^{\prime}, and define

|  |  |  |
| --- | --- | --- |
|  | 𝚺^u​u​(p):=1T−p​∑t=p+1T𝜺^u,t​(p)​𝜺^u,t​(p)′.\widehat{{\mbox{$\Sigma$}}}\_{uu}(p):=\frac{1}{T-p}\sum\_{t=p+1}^{T}\widehat{{\mbox{$\varepsilon$}}}\_{u,t}(p)\widehat{{\mbox{$\varepsilon$}}}\_{u,t}(p)^{\prime}. |  |

Define

|  |  |  |
| --- | --- | --- |
|  | BICT⁡(p):=log​det𝚺^u​u​(p)+κ​(p)​log⁡TT,κ​(p):=N+k+p​N2+p​N​k,\operatorname{BIC}\_{T}(p):=\log\det\widehat{{\mbox{$\Sigma$}}}\_{uu}(p)+\frac{\kappa(p)\log T}{T},\qquad\kappa(p):=N+k+p\,N^{2}+p\,Nk, |  |

where κ​(p)\kappa(p) is the total number of regression coefficients in the system of ([24](https://arxiv.org/html/2601.21272v1#S2.E24 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"))
(the additional N​(N+1)/2N(N+1)/2 covariance parameters do not depend on pp and hence are omitted).
Then

|  |  |  |
| --- | --- | --- |
|  | p^BIC:=min⁡arg⁡minp∈𝒫⁡BICT⁡(p)→𝑝p0.\widehat{p}\_{\mathrm{BIC}}:=\min\arg\min\_{p\in\mathcal{P}}\operatorname{BIC}\_{T}(p)\ \xrightarrow{p}\ p\_{0}. |  |

###### Proof.

See the Appendix.
∎

Lemma [2](https://arxiv.org/html/2601.21272v1#Thmlemma2 "Lemma 2: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") shows that the BIC consistently selects the true lag order p0p\_{0} from a fixed candidate set. Therefore, in the subsequent asymptotic analysis we may treat p0p\_{0} as known without loss of generality. Given a lag order p0p\_{0}, consider the augmented regression implied by ([24](https://arxiv.org/html/2601.21272v1#S2.E24 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) under the linear reparameterization, and estimate it equation by equation. The next lemma establishes consistency and asymptotic normality of this first-step (generalized Durbin) estimator.

###### Lemma 3:

Fix p0p\_{0} and consider the equation-by-equation augmented regression ([25](https://arxiv.org/html/2601.21272v1#S2.E25 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) for each i=1,…,Ni=1,\ldots,N on the effective sample t=p0+1,…,Tt=p\_{0}+1,\ldots,T, with Teff:=T−p0T\_{\mathrm{eff}}:=T-p\_{0}. Suppose Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")–[2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") hold and one of the exogeneity conditions B​DBD, G​E​X​O​GGEXOG, or E​B​DEBD holds. Define the equation-by-equation Durbin estimator

|  |  |  |
| --- | --- | --- |
|  | 𝜽^iD:=(1Teff​∑t=p0+1T𝒘i,t​𝒘i,t′)−1​(1Teff​∑t=p0+1T𝒘i,t​yi,t).\widehat{{\mbox{$\theta$}}}\_{i}^{\mathrm{D}}:=\Bigl(\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$w$}}\_{i,t}{\mbox{$w$}}\_{i,t}^{\prime}\Bigr)^{-1}\Bigl(\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$w$}}\_{i,t}y\_{i,t}\Bigr). |  |

Then, for each i=1,…,Ni=1,\ldots,N,

|  |  |  |
| --- | --- | --- |
|  | 𝜽^iD→𝑝𝜽i.\widehat{{\mbox{$\theta$}}}\_{i}^{\mathrm{D}}\xrightarrow{p}{\mbox{$\theta$}}\_{i}. |  |

###### Proof.

See the Appendix.
∎

Lemma [3](https://arxiv.org/html/2601.21272v1#Thmlemma3 "Lemma 3: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") establishes consistency of the Durbin estimators from the augmented regressions. However, these estimators do not exploit contemporaneous cross-equation dependence in 𝜺u,t{\mbox{$\varepsilon$}}\_{u,t} and are therefore generally inefficient. Moreover, the augmented regression delivers 𝜸\gamma rather than the original intercept vector 𝜶\alpha. Indeed, from ([23](https://arxiv.org/html/2601.21272v1#S2.E23 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"))–([24](https://arxiv.org/html/2601.21272v1#S2.E24 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")),

|  |  |  |
| --- | --- | --- |
|  | 𝜸=(𝑰N−∑j=1p0𝚿u​u,j)​𝜶−∑j=1p0𝚿u​x,j​𝝁x,{\mbox{$\gamma$}}=\Bigl({\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}\Bigr){\mbox{$\alpha$}}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{ux,j}{\mbox{$\mu$}}\_{x}, |  |

so recovering 𝜶\alpha requires consistent estimates of {𝚿u​u,j}\{{\mbox{$\Psi$}}\_{uu,j}\}, {𝚿u​x,j}\{{\mbox{$\Psi$}}\_{ux,j}\}, and 𝝁x{\mbox{$\mu$}}\_{x}.

To obtain an asymptotically efficient estimator and recover 𝜶\alpha, we now construct a feasible GLS transformation. Using the population identity 𝚲j=𝚿u​x,j−𝚿u​u,j​𝑩{\mbox{$\Lambda$}}\_{j}={\mbox{$\Psi$}}\_{ux,j}-{\mbox{$\Psi$}}\_{uu,j}{\mbox{$B$}}, we define the plug-in estimator

|  |  |  |
| --- | --- | --- |
|  | 𝚿^u​x,j:=𝚲^j+𝚿^u​u,j​𝑩^,j=1,…,p0.\widehat{{\mbox{$\Psi$}}}\_{ux,j}:=\widehat{{\mbox{$\Lambda$}}}\_{j}+\widehat{{\mbox{$\Psi$}}}\_{uu,j}\widehat{{\mbox{$B$}}},\qquad j=1,\ldots,p\_{0}. |  |

Since the first-step estimators are consistent, we have, for each fixed jj (and hence uniformly over j=1,…,p0j=1,\ldots,p\_{0}), 𝚿^u​u,j=𝚿u​u,j+op​(1)\widehat{{\mbox{$\Psi$}}}\_{uu,j}={\mbox{$\Psi$}}\_{uu,j}+o\_{p}(1), 𝚿^u​x,j=𝚿u​x,j+op​(1)\widehat{{\mbox{$\Psi$}}}\_{ux,j}={\mbox{$\Psi$}}\_{ux,j}+o\_{p}(1), and 𝝁^x→𝑝𝝁x\widehat{{\mbox{$\mu$}}}\_{x}\xrightarrow{p}{\mbox{$\mu$}}\_{x}. Consequently, after replacing the unknown nuisance parameters in the population transformation by their Durbin estimates, the resulting feasible transformed regression is equal to its population counterpart up to a remainder term that is asymptotically negligible (in the sense specified below). Hence, up to op​(1)o\_{p}(1) perturbations, the following regression holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚GD,t=𝒁GD,t′​𝜿+𝜺u,t,{\mbox{$y$}}\_{\mathrm{GD},t}={\mbox{$Z$}}\_{\mathrm{GD},t}^{\prime}{\mbox{$\kappa$}}+{\mbox{$\varepsilon$}}\_{u,t}, |  | (27) |

where 𝒚GD,t=𝒚t−∑j=1p0𝚿^u​u,j​𝒚t−j−∑j=1p0𝚿^u​x,j​(𝒙t−j−𝝁^x){\mbox{$y$}}\_{\mathrm{GD},t}={\mbox{$y$}}\_{t}-\sum\_{j=1}^{p\_{0}}\widehat{{\mbox{$\Psi$}}}\_{uu,j}{\mbox{$y$}}\_{t-j}-\sum\_{j=1}^{p\_{0}}\widehat{{\mbox{$\Psi$}}}\_{ux,j}\big({\mbox{$x$}}\_{t-j}-\widehat{{\mbox{$\mu$}}}\_{x}\big) and 𝒁GD,t′=[(𝑰N−∑j=1p0𝚿^u​u,j),𝑿t′−∑j=1p0𝚿^u​u,j​𝑿t−j′]{\mbox{$Z$}}\_{\mathrm{GD},t}^{\prime}=[({\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}\widehat{{\mbox{$\Psi$}}}\_{uu,j}),{\mbox{$X$}}\_{t}^{\prime}-\sum\_{j=1}^{p\_{0}}\widehat{{\mbox{$\Psi$}}}\_{uu,j}{\mbox{$X$}}\_{t-j}^{\prime}], and 𝝁^x=1/Te​f​f​∑t=p0+1T𝒙t\widehat{{\mbox{$\mu$}}}\_{x}=1/T\_{eff}\sum\_{t=p\_{0}+1}^{T}{\mbox{$x$}}\_{t}, which is consistent by the ergodic theorem.

###### Assumption 5:

(A5.1)
:   𝑸GD:=𝔼​[𝒁GD,t​𝚺u​u−1​𝒁GD,t′]{\mbox{$Q$}}\_{\mathrm{GD}}:={\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{GD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{GD},t}^{\prime}] is positive definite.

(A5.2)
:   𝔼​[𝜺u,t​𝜺u,t′∣σ​(𝒁GD,t)]=𝚺u​u{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}\mid\sigma({\mbox{$Z$}}\_{\mathrm{GD},t})]={\mbox{$\Sigma$}}\_{uu}, where 𝚺u​u{\mbox{$\Sigma$}}\_{uu} is positive definite.

###### Theorem 1:

Let 𝐲GD,t=𝐙GD,t′​𝛋+𝛆u,t{\mbox{$y$}}\_{\mathrm{GD},t}={\mbox{$Z$}}\_{\mathrm{GD},t}^{\prime}{\mbox{$\kappa$}}+{\mbox{$\varepsilon$}}\_{u,t} as in ([27](https://arxiv.org/html/2601.21272v1#S2.E27 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")), with 𝐙GD,t∈ℝm×N{\mbox{$Z$}}\_{\mathrm{GD},t}\in\mathbb{R}^{m\times N} and 𝛋∈ℝm{\mbox{$\kappa$}}\in\mathbb{R}^{m}. Suppose Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")-[2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), [5](https://arxiv.org/html/2601.21272v1#Thmassumption5 "Assumption 5: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") and one of the exogeneity conditions BD, GEXOG, or EBD holds. Let the effective sample be t=p0+1,…,Tt=p\_{0}+1,\ldots,T with Te​f​f:=T−p0T\_{eff}:=T-p\_{0}. Define

|  |  |  |
| --- | --- | --- |
|  | 𝚺^u​u=1Te​f​f​∑t=p0+1T𝜺^u,t​𝜺^u,t′,𝜺^u,t:=𝒚t−𝑾t′​𝜽^D−OLS.\widehat{{\mbox{$\Sigma$}}}\_{uu}=\frac{1}{T\_{eff}}\sum\_{t=p\_{0}+1}^{T}\widehat{{\mbox{$\varepsilon$}}}\_{u,t}\widehat{{\mbox{$\varepsilon$}}}\_{u,t}^{\prime},\qquad\widehat{{\mbox{$\varepsilon$}}}\_{u,t}:={\mbox{$y$}}\_{t}-{\mbox{$W$}}\_{t}^{\prime}\widehat{{\mbox{$\theta$}}}^{\mathrm{D\!-\!OLS}}. |  |

Then 𝚺^u​u→𝑝𝚺u​u>0\widehat{{\mbox{$\Sigma$}}}\_{uu}\xrightarrow{p}{\mbox{$\Sigma$}}\_{uu}>0 and is invertible with probability approaching one. The feasible GLS estimator

|  |  |  |
| --- | --- | --- |
|  | 𝜿^GD=(1Te​f​f​∑t=p0+1T𝒁GD,t​𝚺^u​u−1​𝒁GD,t′)−1​(1Te​f​f​∑t=p0+1T𝒁GD,t​𝚺^u​u−1​𝒚GD,t)\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}=\Big(\frac{1}{T\_{eff}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$Z$}}\_{\mathrm{GD},t}\,\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}\,{\mbox{$Z$}}\_{\mathrm{GD},t}^{\prime}\Big)^{-1}\Big(\frac{1}{T\_{eff}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$Z$}}\_{\mathrm{GD},t}\,\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}\,{\mbox{$y$}}\_{\mathrm{GD},t}\Big) |  |

satisfies 𝛋^GD→𝑝𝛋\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}\xrightarrow{p}{\mbox{$\kappa$}} and

|  |  |  |
| --- | --- | --- |
|  | Te​f​f​(𝜿^GD−𝜿)→𝑑𝒩​(𝟎,𝑽),𝑽:=(𝔼​[𝒁GD,t​𝚺u​u−1​𝒁GD,t′])−1.\sqrt{T\_{eff}}\big(\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$\kappa$}}\big)\ \xrightarrow{d}\ \mathcal{N}\big({\mbox{$0$}},\ {\mbox{$V$}}\big),\quad{\mbox{$V$}}:=\Big({\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{GD},t}\,{\mbox{$\Sigma$}}\_{uu}^{-1}\,{\mbox{$Z$}}\_{\mathrm{GD},t}^{\prime}]\Big)^{-1}. |  |

Moreover, 𝛋^GD\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}} is asymptotically efficient under E​B​DEBD, in the sense that it is asymptotically equivalent to the infeasible GLS estimator that uses the true 𝚺u​u{\mbox{$\Sigma$}}\_{uu}.

###### Proof.

See the Appendix.
∎

As a direct consequence of Theorem [1](https://arxiv.org/html/2601.21272v1#Thmtheorem1 "Theorem 1: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), we can conduct Wald-type tests for linear restrictions on 𝜿\kappa under any of the exogeneity conditions B​DBD, G​E​X​O​GGEXOG, or E​B​DEBD. The next corollary states the Wald statistic and its limiting null distribution.

###### Corollary 1:

Let 𝐲GD,t=𝐙GD,t′​𝛋+𝛆u,t{\mbox{$y$}}\_{\mathrm{GD},t}={\mbox{$Z$}}\_{\mathrm{GD},t}^{\prime}{\mbox{$\kappa$}}+{\mbox{$\varepsilon$}}\_{u,t} be as in ([27](https://arxiv.org/html/2601.21272v1#S2.E27 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")). Suppose Assumptions [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")–[2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), [5](https://arxiv.org/html/2601.21272v1#Thmassumption5 "Assumption 5: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") hold and that one of the exogeneity conditions B​DBD, G​E​X​O​GGEXOG, or E​B​DEBD holds. Let 𝐑R be a given q×mq\times m matrix with rank​(𝐑)=q≤m\mathrm{rank}({\mbox{$R$}})=q\leq m, and let 𝐫∈ℝq{\mbox{$r$}}\in\mathbb{R}^{q}. Consider testing the null hypothesis H0:𝐑𝛋=𝐫H\_{0}:{\mbox{$R$}}{\mbox{$\kappa$}}={\mbox{$r$}}. Then, under H0H\_{0}, the Wald statistic

|  |  |  |
| --- | --- | --- |
|  | 𝒲GD:=Teff​(𝑹​𝜿^GD−𝒓)′​[𝑹​𝑽^​𝑹′]−1​(𝑹​𝜿^GD−𝒓)→𝑑χq2,\mathcal{W}^{\mathrm{GD}}:=T\_{\mathrm{eff}}({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$r$}})^{\prime}\big[{\mbox{$R$}}\widehat{{\mbox{$V$}}}{\mbox{$R$}}^{\prime}\big]^{-1}({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$r$}})\ \xrightarrow{d}\ \chi^{2}\_{q}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | 𝑽^:=(1Teff​∑t=p0+1T𝒁GD,t​𝚺^u​u−1​𝒁GD,t′)−1.\widehat{{\mbox{$V$}}}:=\Big(\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$Z$}}\_{\mathrm{GD},t}\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{GD},t}^{\prime}\Big)^{-1}. |  |

###### Proof.

See the Appendix.
∎

### 2.6 Bootstrap-corrected Wald test based on the generalized Durbin estimator

Theorem [1](https://arxiv.org/html/2601.21272v1#Thmtheorem1 "Theorem 1: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") establishes Teff\sqrt{T\_{\mathrm{eff}}}-asymptotic normality of the generalized Durbin estimator 𝜿^GD\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}, which motivates Wald-type inference. In practice, however, the associated Wald test can exhibit non-negligible size distortions in finite samples. One practical source of distortion is that the generalized Durbin regression is implemented using transformed variables 𝒚GD,t{\mbox{$y$}}\_{\mathrm{GD},t} and 𝒁GD,t{\mbox{$Z$}}\_{\mathrm{GD},t} that are not directly observed. These quantities are generated by plugging in first-step estimates of nuisance parameters governing the joint second-order dynamics (e.g., {𝚿u​u,j}j=1p0\{{\mbox{$\Psi$}}\_{uu,j}\}\_{j=1}^{p\_{0}}, {𝚿u​x,j}j=1p0\{{\mbox{$\Psi$}}\_{ux,j}\}\_{j=1}^{p\_{0}}, and 𝝁x{\mbox{$\mu$}}\_{x}), and the resulting generated-regressor effect can materially affect the finite-sample distribution of the Wald statistic.

To address these finite-sample distortions, we adopt a bootstrap-based approach. Bootstrap tests are known to deliver asymptotic refinements for a broad class of (asymptotically) pivotal statistics, often yielding more accurate rejection probabilities than purely asymptotic approximations (Davidson and MacKinnon [1999](https://arxiv.org/html/2601.21272v1#bib.bib2282 "The size distortion of bootstrap tests"); MacKinnon [2006](https://arxiv.org/html/2601.21272v1#bib.bib2281 "Bootstrap methods in econometrics")). In our setting, because the relevant objects inherit serial dependence through the estimated joint dynamics, we employ the sieve bootstrap of Bühlmann ([1997](https://arxiv.org/html/2601.21272v1#bib.bib2283 "Sieve bootstrap for time series")), which approximates the dependence structure by a finite-order VAR(pp) and resamples the estimated innovations to generate pseudo-samples.

Even when inference relies on a single bootstrap pp value, the resulting test may still exhibit finite-sample level (size) distortions. A natural device to further improve accuracy is to calibrate the bootstrap pp value itself by an additional layer of resampling. This idea goes back to Beran ([1988](https://arxiv.org/html/2601.21272v1#bib.bib2284 "Prepivoting test statistics: a bootstrap view of asymptotic refinements")) and forms the basis of the iterated (double) bootstrap, which seeks higher-order improvements in level accuracy by applying a bootstrap-based transformation to an approximately pivotal quantity.

A practical drawback of the full double bootstrap is its computational burden, because it requires a nested resampling scheme with B1B\_{1} outer and B2B\_{2} inner bootstrap replications, leading to a cost proportional to B1×B2B\_{1}\times B\_{2} (e.g., Booth and Hall [1994](https://arxiv.org/html/2601.21272v1#bib.bib2285 "Monte carlo approximation and the iterated boostrap")). To retain much of the accuracy gain at a fraction of the cost, we therefore employ the fast double bootstrap (FDB) of Davidson and MacKinnon ([2007](https://arxiv.org/html/2601.21272v1#bib.bib2286 "Improving the reliability of bootstrap tests with the fast double bootstrap")). The FDB is closely related to the double bootstrap but far less computationally demanding, and it typically requires only about twice the computational effort of a single bootstrap pp value.

We now describe how the FDB is implemented for the Wald test based on the generalized Durbin estimator. The procedure combines a VAR-sieve outer bootstrap under H0H\_{0} with a single inner bootstrap draw per outer replication (i.e., B2=1B\_{2}=1), while re-estimating the nuisance components and reconstructing the GD transforms in each resample.

##### Fast double bootstrap (FDB) algorithm for the GD–Wald test.

Let H0:𝑹𝜿=𝒓H\_{0}:{\mbox{$R$}}{\mbox{$\kappa$}}={\mbox{$r$}} be the null restriction and let 𝒲G​D\mathcal{W}^{GD} denote the observed Wald statistic computed from the original sample using the generalized Durbin (GD) estimator.

1. 1.

   Original-sample estimation.
   Compute the unrestricted GD estimator 𝜿^GD\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}} and the plug-in covariance matrix 𝑽^\widehat{{\mbox{$V$}}}, and form the observed Wald statistic 𝒲G​D\mathcal{W}^{GD}. Construct the restricted GD estimator under H0H\_{0} by

   |  |  |  |
   | --- | --- | --- |
   |  | 𝜿~GD=𝜿^GD−𝑽^​𝑹′​(𝑹​𝑽^​𝑹′)−1​(𝑹​𝜿^GD−𝒓).\widetilde{{\mbox{$\kappa$}}}^{\mathrm{GD}}=\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-\widehat{{\mbox{$V$}}}\,{\mbox{$R$}}^{\prime}\bigl({\mbox{$R$}}\widehat{{\mbox{$V$}}}{\mbox{$R$}}^{\prime}\bigr)^{-1}\bigl({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$r$}}\bigr). |  |

   The restricted estimator 𝜿~GD\widetilde{{\mbox{$\kappa$}}}^{\mathrm{GD}} is used only to generate bootstrap samples under H0H\_{0}.
2. 2.

   Outer bootstrap (b=1,…,B1b=1,\dots,B\_{1}): VAR-sieve under H0H\_{0}.
   For each bb, generate a pseudo-sample using a VAR-sieve bootstrap under H0H\_{0} (based on 𝜿~GD\widetilde{{\mbox{$\kappa$}}}^{\mathrm{GD}}), re-estimate the nuisance parameters, reconstruct {𝒚GD,t∗(b),𝒁GD,t∗(b)}\{{\mbox{$y$}}\_{\mathrm{GD},t}^{\*(b)},{\mbox{$Z$}}\_{\mathrm{GD},t}^{\*(b)}\}, and compute the outer Wald statistic Wb∗W\_{b}^{\ast} using the unrestricted GD estimator on the pseudo-sample.
3. 3.

   Inner fast step (one draw per outer replication).
   For each bb, construct a restricted generator under H0H\_{0} based on the bb-th outer pseudo-sample, generate one inner pseudo-sample, and compute Wb∗∗W\_{b}^{\ast\ast} using the unrestricted GD estimator.
4. 4.

   Single-bootstrap pp value.
   Compute

   |  |  |  |
   | --- | --- | --- |
   |  | p^∗=1B1∑b=1B1𝟏{Wb∗≥𝒲G​D}.\widehat{p}^{\ast}=\frac{1}{B\_{1}}\sum\_{b=1}^{B\_{1}}\mathbf{1}\!\mathopen{}\left\{W\_{b}^{\ast}\geq\mathcal{W}^{GD}\mathclose{}\right\}. |  |
5. 5.

   FDB calibration and pp value.
   Let q1−p^∗∗∗q^{\ast\ast}\_{1-\widehat{p}^{\ast}} denote the empirical (1−p^∗)(1-\widehat{p}^{\ast}) quantile of {Wb∗∗}b=1B1\{W\_{b}^{\ast\ast}\}\_{b=1}^{B\_{1}}.
   Define the FDB-corrected pp value by

   |  |  |  |
   | --- | --- | --- |
   |  | p^FDB=1B1∑b=1B1𝟏{Wb∗≥q1−p^∗∗∗},\widehat{p}\_{\mathrm{FDB}}=\frac{1}{B\_{1}}\sum\_{b=1}^{B\_{1}}\mathbf{1}\!\mathopen{}\left\{W\_{b}^{\ast}\geq q^{\ast\ast}\_{1-\widehat{p}^{\ast}}\mathclose{}\right\}, |  |

   and reject H0H\_{0} at level α\alpha if p^FDB<α\widehat{p}\_{\mathrm{FDB}}<\alpha.

## 3 Simulation Experiment

In this section, we examine the finite-sample properties of the multivariate estimators and related test statistics under the B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD conditions through Monte Carlo experiments. We are interested in using our proposed estimators to test the validity of asset pricing models. To this end, we consider a multiple-equation regression model in which the regressors are common across all equations.

### 3.1 Simulation Design

In asset pricing models, it is typically assumed that each portfolio ii is exposed to the same set of factors. Classic examples include the multifactor models of [Fama and French](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds")’s ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds"); [2015](https://arxiv.org/html/2601.21272v1#bib.bib1869 "A five-factor asset pricing model")) and the arbitrage pricing theory of [Ross](https://arxiv.org/html/2601.21272v1#bib.bib1912 "The arbitrage theory of capital asset pricing")’s ([1976](https://arxiv.org/html/2601.21272v1#bib.bib1912 "The arbitrage theory of capital asset pricing")). In the simulation experiments, we consider a multiple-equation regression model with regressors common across all equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚t=𝜶+(𝑰N⊗𝒙t′)​𝜷+𝒖t=𝒁t′​𝜿+𝒖t,t=1,…,T,{\mbox{$y$}}\_{t}={\mbox{$\alpha$}}+\big({\mbox{$I$}}\_{N}\otimes{\mbox{$x$}}\_{t}^{\prime}\big){\mbox{$\beta$}}+{\mbox{$u$}}\_{t}={\mbox{$Z$}}\_{t}^{\prime}{\mbox{$\kappa$}}+{\mbox{$u$}}\_{t},\quad t=1,\ldots,T, |  | (28) |

where 𝒚t=(y1,t,…,yN,t)′∈ℝN{\mbox{$y$}}\_{t}=(y\_{1,t},\ldots,y\_{N,t})^{\prime}\in\mathbb{R}^{N}, 𝒙t{\mbox{$x$}}\_{t} is a k×1k\times 1 vector of common factors (k=kik=k\_{i} for all ii), and 𝜷=(𝜷1′,…,𝜷N′)′∈ℝk​N{\mbox{$\beta$}}=({\mbox{$\beta$}}\_{1}^{\prime},\ldots,{\mbox{$\beta$}}\_{N}^{\prime})^{\prime}\in\mathbb{R}^{kN}. Define 𝑿t′=(𝑰N⊗𝒙t′)∈ℝN×k​N{\mbox{$X$}}\_{t}^{\prime}=({\mbox{$I$}}\_{N}\otimes{\mbox{$x$}}\_{t}^{\prime})\in\mathbb{R}^{N\times kN} and 𝒁t′:=[𝑰N,𝑿t′]∈ℝN×(k+1)​N{\mbox{$Z$}}\_{t}^{\prime}:=[{\mbox{$I$}}\_{N},{\mbox{$X$}}\_{t}^{\prime}]\in\mathbb{R}^{N\times(k+1)N}, so that 𝜿=(𝜶′,𝜷′)′∈ℝ(k+1)​N{\mbox{$\kappa$}}=({\mbox{$\alpha$}}^{\prime},{\mbox{$\beta$}}^{\prime})^{\prime}\in\mathbb{R}^{(k+1)N} collects the intercepts and slope coefficients. Note that, as stated in Remark [2](https://arxiv.org/html/2601.21272v1#Thmremark2 "Remark 2 (Innovation-based exogeneity and its location): ‣ 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), the specification  ([28](https://arxiv.org/html/2601.21272v1#S3.E28 "In 3.1 Simulation Design ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is a special case of  ([2](https://arxiv.org/html/2601.21272v1#S2.E2 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")).

To generate 𝒛¯t=(𝒙t′−𝝁x′,𝒖t′)′\bar{{\mbox{$z$}}}\_{t}=({\mbox{$x$}}\_{t}^{\prime}-{\mbox{$\mu$}}\_{x}^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime}, we consider the following three VAR(1) processes corresponding to the B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD conditions. In all cases, we impose 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} so that the contemporaneous correlation between 𝜺x,t{\mbox{$\varepsilon$}}\_{x,t} and 𝜺u,t{\mbox{$\varepsilon$}}\_{u,t} is absent.

(1)
:   Block-diagonal vector autoregression (VAR) with 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} (B​DBD)

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | 𝒚t=𝜶+(𝑰N⊗𝒙t′)​𝜷+𝒖t,[𝒙t−𝝁x𝒖t]=[𝚿x​x,1𝟎𝟎𝚿u​u,1]​[𝒙t−1−𝝁x𝒖t−1]+[𝜺x,t𝜺u,t],[𝜺x,t𝜺u,t]∼𝒩([𝟎𝟎],[𝚺x​x𝟎𝟎𝚺u​u]).\begin{split}{\mbox{$y$}}\_{t}=&\;{\mbox{$\alpha$}}+({\mbox{$I$}}\_{N}\otimes{\mbox{$x$}}\_{t}^{\prime}){\mbox{$\beta$}}+{\mbox{$u$}}\_{t},\\ \begin{bmatrix}{\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x}\\ {\mbox{$u$}}\_{t}\\ \end{bmatrix}=&\;\begin{bmatrix}{\mbox{$\Psi$}}\_{xx,1}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Psi$}}\_{uu,1}\\ \end{bmatrix}\begin{bmatrix}{\mbox{$x$}}\_{t-1}-{\mbox{$\mu$}}\_{x}\\ {\mbox{$u$}}\_{t-1}\\ \end{bmatrix}+\begin{bmatrix}{\mbox{$\varepsilon$}}\_{x,t}\\ {\mbox{$\varepsilon$}}\_{u,t}\\ \end{bmatrix},\\ \begin{bmatrix}{\mbox{$\varepsilon$}}\_{x,t}\\ {\mbox{$\varepsilon$}}\_{u,t}\\ \end{bmatrix}\sim&\;\mathcal{N}\mathopen{}\left(\begin{bmatrix}{\mbox{$0$}}\\ {\mbox{$0$}}\\ \end{bmatrix},\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Sigma$}}\_{uu}\\ \end{bmatrix}\mathclose{}\right).\end{split} |  | (29) |

(2)
:   Triangular VAR with 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} (G​E​X​O​GGEXOG)

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | 𝒚t=𝜶+(𝑰N⊗𝒙t′)​𝜷+𝒖t,[𝒙t−𝝁x𝒖t]=[𝚿x​x,1𝚿x​u,1𝟎𝚿u​u,1]​[𝒙t−1−𝝁x𝒖t−1]+[𝜺x,t𝜺u,t],[𝜺x,t𝜺u,t]∼𝒩([𝟎𝟎],[𝚺x​x𝟎𝟎𝚺u​u]).\begin{split}{\mbox{$y$}}\_{t}=&\;{\mbox{$\alpha$}}+({\mbox{$I$}}\_{N}\otimes{\mbox{$x$}}\_{t}^{\prime}){\mbox{$\beta$}}+{\mbox{$u$}}\_{t},\\ \begin{bmatrix}{\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x}\\ {\mbox{$u$}}\_{t}\\ \end{bmatrix}=&\;\begin{bmatrix}{\mbox{$\Psi$}}\_{xx,1}&{\mbox{$\Psi$}}\_{xu,1}\\ {\mbox{$0$}}&{\mbox{$\Psi$}}\_{uu,1}\\ \end{bmatrix}\begin{bmatrix}{\mbox{$x$}}\_{t-1}-{\mbox{$\mu$}}\_{x}\\ {\mbox{$u$}}\_{t-1}\\ \end{bmatrix}+\begin{bmatrix}{\mbox{$\varepsilon$}}\_{x,t}\\ {\mbox{$\varepsilon$}}\_{u,t}\\ \end{bmatrix},\\ \begin{bmatrix}{\mbox{$\varepsilon$}}\_{x,t}\\ {\mbox{$\varepsilon$}}\_{u,t}\\ \end{bmatrix}\sim&\;\mathcal{N}\mathopen{}\left(\begin{bmatrix}{\mbox{$0$}}\\ {\mbox{$0$}}\\ \end{bmatrix},\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Sigma$}}\_{uu}\\ \end{bmatrix}\mathclose{}\right).\end{split} |  | (30) |

(3)
:   Unrestricted VAR with 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} (E​B​DEBD)

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | 𝒚t=𝜶+(𝑰N⊗𝒙t′)​𝜷+𝒖t,[𝒙t−𝝁x𝒖t]=[𝚿x​x,1𝚿x​u,1𝚿u​x,1𝚿u​u,1]​[𝒙t−1−𝝁x𝒖t−1]+[𝜺x,t𝜺u,t],[𝜺x,t𝜺u,t]∼𝒩([𝟎𝟎],[𝚺x​x𝟎𝟎𝚺u​u]).\begin{split}{\mbox{$y$}}\_{t}=&\;{\mbox{$\alpha$}}+({\mbox{$I$}}\_{N}\otimes{\mbox{$x$}}\_{t}^{\prime}){\mbox{$\beta$}}+{\mbox{$u$}}\_{t},\\ \begin{bmatrix}{\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x}\\ {\mbox{$u$}}\_{t}\\ \end{bmatrix}=&\;\begin{bmatrix}{\mbox{$\Psi$}}\_{xx,1}&{\mbox{$\Psi$}}\_{xu,1}\\ {\mbox{$\Psi$}}\_{ux,1}&{\mbox{$\Psi$}}\_{uu,1}\\ \end{bmatrix}\begin{bmatrix}{\mbox{$x$}}\_{t-1}-{\mbox{$\mu$}}\_{x}\\ {\mbox{$u$}}\_{t-1}\\ \end{bmatrix}+\begin{bmatrix}{\mbox{$\varepsilon$}}\_{x,t}\\ {\mbox{$\varepsilon$}}\_{u,t}\\ \end{bmatrix},\\ \begin{bmatrix}{\mbox{$\varepsilon$}}\_{x,t}\\ {\mbox{$\varepsilon$}}\_{u,t}\\ \end{bmatrix}\sim&\;\mathcal{N}\mathopen{}\left(\begin{bmatrix}{\mbox{$0$}}\\ {\mbox{$0$}}\\ \end{bmatrix},\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Sigma$}}\_{uu}\\ \end{bmatrix}\mathclose{}\right).\end{split} |  | (31) |

In Baillie et al. ([2024](https://arxiv.org/html/2601.21272v1#bib.bib2090 "On robust inference in time-series regression")), lagged dependent variables are explicitly included in the estimated regression. In contrast, our setup does not require pre-specifying any finite lag structure for 𝒚t{\mbox{$y$}}\_{t}. Since the Wold/VAR representation of 𝒛t=(𝒙t′−𝝁x′,𝒖t′)′{\mbox{$z$}}\_{t}=({\mbox{$x$}}\_{t}^{\prime}-{\mbox{$\mu$}}\_{x}^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime} yields an equivalent Durbin-type representation, the dynamics of 𝒚t{\mbox{$y$}}\_{t} are absorbed implicitly and need not be imposed a priori.

In all cases, we consider sample sizes T∈{100,200,400,800}T\in\{100,200,400,800\}. To investigate how the number of factors and the number of assets (equations) affect the finite-sample accuracy of the estimators and the performance of the tests, we consider k∈{2,4}k\in\{2,4\} and N∈{5,10}N\in\{5,10\}. In each replication, we simulate T+500T+500 observations and discard the first 500 observations as burn-in. For all DGPs, we perform 1,000 Monte Carlo replications.

For the VAR(1) coefficient matrix, the block restrictions depend on the DGP (B​DBD/ G​E​X​O​GGEXOG/ E​B​DEBD) as in ([29](https://arxiv.org/html/2601.21272v1#S3.E29 "In item (1) ‣ 3.1 Simulation Design ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"))–([31](https://arxiv.org/html/2601.21272v1#S3.E31 "In item (3) ‣ 3.1 Simulation Design ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")). To control persistence in a unified manner across blocks, we calibrate the magnitude of each block using its spectral norm ∥⋅∥2\|\cdot\|\_{2}. Specifically, we draw random orthogonal matrices 𝑸x∈ℝk×k{\mbox{$Q$}}\_{x}\in\mathbb{R}^{k\times k} and 𝑸u∈ℝN×N{\mbox{$Q$}}\_{u}\in\mathbb{R}^{N\times N} (via QR decomposition of i.i.d. Gaussian matrices) and set

|  |  |  |
| --- | --- | --- |
|  | 𝚿x​x,1=cx​x​𝑸x,𝚿u​u,1=cu​u​𝑸u,{\mbox{$\Psi$}}\_{xx,1}=c\_{xx}\,{\mbox{$Q$}}\_{x},\qquad{\mbox{$\Psi$}}\_{uu,1}=c\_{uu}\,{\mbox{$Q$}}\_{u}, |  |

so that ‖𝚿x​x,1‖2=cx​x\|{\mbox{$\Psi$}}\_{xx,1}\|\_{2}=c\_{xx} and ‖𝚿u​u,1‖2=cu​u\|{\mbox{$\Psi$}}\_{uu,1}\|\_{2}=c\_{uu}.

Let r≤min⁡(k,N)r\leq\min(k,N) denote a pre-specified rank (we use r=1r=1 in the baseline). We generate matrices 𝑨∈ℝk×r{\mbox{$A$}}\in\mathbb{R}^{k\times r} and 𝑩∈ℝN×r{\mbox{$B$}}\in\mathbb{R}^{N\times r} with orthonormal columns (again via QR decomposition), so that 𝑨′​𝑨=𝑰r{\mbox{$A$}}^{\prime}{\mbox{$A$}}={\mbox{$I$}}\_{r} and 𝑩′​𝑩=𝑰r{\mbox{$B$}}^{\prime}{\mbox{$B$}}={\mbox{$I$}}\_{r}. We then define the low-rank cross blocks

|  |  |  |
| --- | --- | --- |
|  | 𝚿x​u,1=cx​u​𝑨𝑩′,𝚿u​x,1=cu​x​𝑩𝑨′,{\mbox{$\Psi$}}\_{xu,1}=c\_{xu}\,{\mbox{$A$}}{\mbox{$B$}}^{\prime},\qquad{\mbox{$\Psi$}}\_{ux,1}=c\_{ux}\,{\mbox{$B$}}{\mbox{$A$}}^{\prime}, |  |

which implies ‖𝑨𝑩′‖2=1\|{\mbox{$A$}}{\mbox{$B$}}^{\prime}\|\_{2}=1 and hence ‖𝚿x​u,1‖2=cx​u\|{\mbox{$\Psi$}}\_{xu,1}\|\_{2}=c\_{xu} and ‖𝚿u​x,1‖2=cu​x\|{\mbox{$\Psi$}}\_{ux,1}\|\_{2}=c\_{ux}. This construction aligns the singular directions of 𝚿x​u,1{\mbox{$\Psi$}}\_{xu,1} and 𝚿u​x,1{\mbox{$\Psi$}}\_{ux,1}.

Following the spirit of Baillie et al. ([2024](https://arxiv.org/html/2601.21272v1#bib.bib2090 "On robust inference in time-series regression")), we construct VAR(1) data-generating processes that represent the B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD conditions. Our design can be viewed as a multi-equation extension of their single-equation setup, allowing for cross-equation dependence in 𝒖t{\mbox{$u$}}\_{t} and joint dynamics in (𝒙t′,𝒖t′)′({\mbox{$x$}}\_{t}^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime}.

For the block-diagonal DGP (B​DBD), we set 𝚿x​u,1=𝟎{\mbox{$\Psi$}}\_{xu,1}={\mbox{$0$}} and 𝚿u​x,1=𝟎{\mbox{$\Psi$}}\_{ux,1}={\mbox{$0$}}. For the triangular DGP (G​E​X​O​GGEXOG), we set 𝚿u​x,1=𝟎{\mbox{$\Psi$}}\_{ux,1}={\mbox{$0$}} while keeping 𝚿x​u,1{\mbox{$\Psi$}}\_{xu,1} unrestricted. For the unrestricted DGP (E​B​DEBD), we keep both 𝚿x​u,1{\mbox{$\Psi$}}\_{xu,1} and 𝚿u​x,1{\mbox{$\Psi$}}\_{ux,1} unrestricted. Let ρ​(𝚿)\rho({\mbox{$\Psi$}}) denote the spectral radius of 𝚿\Psi. If ρ​(𝚿)\rho({\mbox{$\Psi$}}) exceeds a target level ρ¯<1\bar{\rho}<1, we scale all blocks by a common factor,

|  |  |  |
| --- | --- | --- |
|  | 𝚿←γ​𝚿,γ=ρ¯/ρ​(𝚿),{\mbox{$\Psi$}}\leftarrow\gamma\,{\mbox{$\Psi$}},\qquad\gamma=\bar{\rho}/\rho({\mbox{$\Psi$}}), |  |

so that the resulting VAR(1) satisfies ρ​(𝚿)=ρ¯\rho({\mbox{$\Psi$}})=\bar{\rho} (up to numerical tolerance). In the baseline, we set (cx​x,cx​u,cu​x,cu​u)=(0.4,0.7,0.3,0.5)(c\_{xx},c\_{xu},c\_{ux},c\_{uu})=(0.4,0.7,0.3,0.5) and ρ¯=0.91\bar{\rho}=0.91, which allow the sinle-equation settins of Baillie et al. ([2024](https://arxiv.org/html/2601.21272v1#bib.bib2090 "On robust inference in time-series regression")) to generalize in muple-equations.

We assume that the VAR innovations satisfy 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} and draw 𝜺x,t{\mbox{$\varepsilon$}}\_{x,t} and 𝜺u,t{\mbox{$\varepsilon$}}\_{u,t} independently as

|  |  |  |
| --- | --- | --- |
|  | [𝜺x,t𝜺u,t]∼𝒩([𝟎𝟎],[𝚺x​x𝟎𝟎𝚺u​u]).\begin{bmatrix}{\mbox{$\varepsilon$}}\_{x,t}\\ {\mbox{$\varepsilon$}}\_{u,t}\end{bmatrix}\sim\mathcal{N}\!\mathopen{}\left(\begin{bmatrix}{\mbox{$0$}}\\ {\mbox{$0$}}\end{bmatrix},\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Sigma$}}\_{uu}\end{bmatrix}\mathclose{}\right). |  |

Both 𝚺x​x{\mbox{$\Sigma$}}\_{xx} and 𝚺u​u{\mbox{$\Sigma$}}\_{uu} are generated as random symmetric positive definite matrices via a Cholesky-type construction: for dimension mm, we draw a lower-triangular matrix 𝑳L with unit diagonal and i.i.d. off-diagonal entries Unif(−δ/m,,δ/m)\mathrm{Unif}\big(-\delta/\sqrt{m},,\delta/\sqrt{m}\big), and set 𝚺=𝑳𝑳′{\mbox{$\Sigma$}}={\mbox{$L$}}{\mbox{$L$}}^{\prime}. In the implementation we use δ=0.1\delta=0.1 for 𝚺x​x{\mbox{$\Sigma$}}\_{xx} (m=km=k) and δ=0.5\delta=0.5 for 𝚺u​u{\mbox{$\Sigma$}}\_{uu} (m=Nm=N). After simulating 𝒙t−𝝁x{\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x}, we add back a constant mean 𝝁x=μx​𝟏k{\mbox{$\mu$}}\_{x}=\mu\_{x}{\mbox{$1$}}\_{k} (baseline μx=0.3\mu\_{x}=0.3) to obtain 𝒙t{\mbox{$x$}}\_{t}.

### 3.2 Estimation Accuracy

Following Baillie et al. ([2024](https://arxiv.org/html/2601.21272v1#bib.bib2090 "On robust inference in time-series regression")), we examine the estimation accuracy of multiple-equation estimators (OLS, FGLS-CO, FGLS-D, GD and BC-GD: generalized durbin estimator with bootstrap bias correction). Specifically, we compute and compare the bias and mean squared error (MSE) of these estimators. For ease of interpretation, we summarize the bias and MSE of vector parameters using scalar measures based on the Euclidean norm.

Let 𝜿0∈ℝ(k+1)​N{\mbox{$\kappa$}}\_{0}\in\mathbb{R}^{(k+1)N} denote the true parameter vector and let 𝜿^T\widehat{{\mbox{$\kappa$}}}\_{T} be an estimator of 𝜿0{\mbox{$\kappa$}}\_{0} computed from a sample of size TT. Define the bias vector as

|  |  |  |
| --- | --- | --- |
|  | 𝒃T:=𝔼​[𝜿^T]−𝜿0∈ℝ(k+1)​N,{\mbox{$b$}}\_{T}:={\mathbb{E}}[\widehat{{\mbox{$\kappa$}}}\_{T}]-{\mbox{$\kappa$}}\_{0}\in\mathbb{R}^{(k+1)N}, |  |

where the expectation is taken under the data-generating process at sample size TT. We report the scalar bias as the Euclidean norm of 𝒃T{\mbox{$b$}}\_{T},

|  |  |  |
| --- | --- | --- |
|  | bias​(𝜿^T):=‖𝒃T‖2=‖𝔼​[𝜿^T]−𝜿0‖2.\mathrm{bias}(\widehat{{\mbox{$\kappa$}}}\_{T}):=\|{\mbox{$b$}}\_{T}\|\_{2}=\|{\mathbb{E}}[\widehat{{\mbox{$\kappa$}}}\_{T}]-{\mbox{$\kappa$}}\_{0}\|\_{2}. |  |

We further define the scalar MSE under quadratic loss by

|  |  |  |
| --- | --- | --- |
|  | MSE(𝜿^T):=𝔼[∥𝜿^T−𝜿0∥22]=𝔼[(𝜿^T−𝜿0)′(𝜿^T−𝜿0)].\mathrm{MSE}(\widehat{{\mbox{$\kappa$}}}\_{T}):={\mathbb{E}}\mathopen{}\left[\|\widehat{{\mbox{$\kappa$}}}\_{T}-{\mbox{$\kappa$}}\_{0}\|\_{2}^{2}\mathclose{}\right]={\mathbb{E}}\mathopen{}\left[(\widehat{{\mbox{$\kappa$}}}\_{T}-{\mbox{$\kappa$}}\_{0})^{\prime}(\widehat{{\mbox{$\kappa$}}}\_{T}-{\mbox{$\kappa$}}\_{0})\mathclose{}\right]. |  |

Then the bias–variance decomposition holds:

|  |  |  |
| --- | --- | --- |
|  | MSE(𝜿^T)=bias(𝜿^T)2+tr(𝕍ar(𝜿^T)),\mathrm{MSE}(\widehat{{\mbox{$\kappa$}}}\_{T})=\mathrm{bias}(\widehat{{\mbox{$\kappa$}}}\_{T})^{2}+\mathrm{tr}\mathopen{}\left({\mathbb{V}\rm{ar}}(\widehat{{\mbox{$\kappa$}}}\_{T})\mathclose{}\right), |  |

where

|  |  |  |
| --- | --- | --- |
|  | 𝕍ar(𝜿^T)=𝔼[(𝜿^T−𝔼[𝜿^T])(𝜿^T−𝔼[𝜿^T])′].{\mathbb{V}\rm{ar}}(\widehat{{\mbox{$\kappa$}}}\_{T})={\mathbb{E}}\mathopen{}\left[(\widehat{{\mbox{$\kappa$}}}\_{T}-{\mathbb{E}}[\widehat{{\mbox{$\kappa$}}}\_{T}])(\widehat{{\mbox{$\kappa$}}}\_{T}-{\mathbb{E}}[\widehat{{\mbox{$\kappa$}}}\_{T}])^{\prime}\mathclose{}\right]. |  |

We adopt this decomposition to compute the MSE and assess the finite-sample accuracy of the estimators.

In Monte Carlo experiments with MM replications, let 𝜿^T(m)\widehat{{\mbox{$\kappa$}}}\_{T}^{(m)} denote the estimator computed in replication mm and define the replication error 𝒆T(m):=𝜿^T(m)−𝜿0{\mbox{$e$}}\_{T}^{(m)}:=\widehat{{\mbox{$\kappa$}}}\_{T}^{(m)}-{\mbox{$\kappa$}}\_{0}. Let 1M​∑m=1M𝜿^T(m)\frac{1}{M}\sum\_{m=1}^{M}\widehat{{\mbox{$\kappa$}}}\_{T}^{(m)} and 𝕍​ar^​(𝜿^T)=1M​∑m=1M{(𝜿^T(m)−𝔼​[𝜿^T]^)​(𝜿^T(m)−𝔼​[𝜿^T]^)′}\widehat{{\mathbb{V}\rm{ar}}}(\widehat{{\mbox{$\kappa$}}}\_{T})=\frac{1}{M}\sum\_{m=1}^{M}\{(\widehat{{\mbox{$\kappa$}}}\_{T}^{(m)}-\widehat{{\mathbb{E}}[\widehat{{\mbox{$\kappa$}}}\_{T}]})(\widehat{{\mbox{$\kappa$}}}\_{T}^{(m)}-\widehat{{\mathbb{E}}[\widehat{{\mbox{$\kappa$}}}\_{T}]})^{\prime}\}denote the emprical expectation and variance of 𝜿^T\widehat{{\mbox{$\kappa$}}}\_{T}. Then, the Monte Carlo analogues of the scalar bias and MSE are given by

|  |  |  |
| --- | --- | --- |
|  | bias^(𝜿^T):=∥1M∑m=1M𝜿^T(m)−𝜿0∥2,MSE^(𝜿^T):=bias^(𝜿^T)2+𝕍​ar^(𝜿^T).\widehat{\mathrm{bias}}(\widehat{{\mbox{$\kappa$}}}\_{T}):=\mathopen{}\left\|\frac{1}{M}\sum\_{m=1}^{M}\widehat{{\mbox{$\kappa$}}}\_{T}^{(m)}-{\mbox{$\kappa$}}\_{0}\mathclose{}\right\|\_{2},\quad\widehat{\mathrm{MSE}}(\widehat{{\mbox{$\kappa$}}}\_{T}):=\widehat{\mathrm{bias}}(\widehat{{\mbox{$\kappa$}}}\_{T})^{2}+\widehat{{\mathbb{V}\rm{ar}}}(\widehat{{\mbox{$\kappa$}}}\_{T}). |  |

In what follows, we compare the estimation accuracy of the system estimators under the DGPs in ([29](https://arxiv.org/html/2601.21272v1#S3.E29 "In item (1) ‣ 3.1 Simulation Design ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"))–([31](https://arxiv.org/html/2601.21272v1#S3.E31 "In item (3) ‣ 3.1 Simulation Design ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) described in Subsection [3.2](https://arxiv.org/html/2601.21272v1#S3.SS2 "3.2 Estimation Accuracy ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"). We set the true parameters to 𝜶=𝟎N{\mbox{$\alpha$}}={\mbox{$0$}}\_{N} and 𝜷=𝟏N​k{\mbox{$\beta$}}={\mbox{$1$}}\_{Nk} (where 𝜷∈ℝN​k{\mbox{$\beta$}}\in\mathbb{R}^{Nk}), so that 𝜿0=(𝟎N′,𝟏N​k′)′{\mbox{$\kappa$}}\_{0}=({\mbox{$0$}}\_{N}^{\prime},{\mbox{$1$}}\_{Nk}^{\prime})^{\prime}.

(Table [1](https://arxiv.org/html/2601.21272v1#Sx1.T1 "Table 1 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") around here)

Table [1](https://arxiv.org/html/2601.21272v1#Sx1.T1 "Table 1 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") reports the scalar bias and MSE under the B​DBD condition. Under the B​DBD, theoretically all estimators are consistent. Hence, the bias of each estimator is expected to decrease toward zero as the sample size TT increases. In terms of efficiency, the FGLS-CO estimator is expected to be the most efficient under B​DBD, and therefore it is expected to attain the smallest MSE among the estimators considered. Consistent with this expectation, the reported bias decline with TT, in line with the consistency results established in the theory. Furthermore, the FGLS-CO and FGLS-D estimator attains the smallest MSE regardless of the number of equations NN.

(Table [2](https://arxiv.org/html/2601.21272v1#Sx1.T2 "Table 2 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") around here)

Table [2](https://arxiv.org/html/2601.21272v1#Sx1.T2 "Table 2 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") shows the results under the G​E​X​O​GGEXOG condition. As shown in Section [2](https://arxiv.org/html/2601.21272v1#S2 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), the OLS and FGLS-CO estimators are theoretically inconsistent under the G​E​X​O​GGEXOG. The resulting distortion is particularly severe for OLS: both the bias and the MSE are substantially larger than under B​DBD. By contrast, the FGLS-CO estimator mitigates the distortion relative to OLS, yielding relatively smaller bias and MSE. This finding is consistent with the simulation evidence in Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")), who argue that quasi-differencing can reduce finite-sample bias even when conventional FGLS-CO procedures remain inconsistent. Moreover, under G​E​X​O​GGEXOG, the FGLS-D and generalized Durbin estimators are consistent. Consistent with theory, their biases decrease as TT increases. Furthermore, the FGLS-D estimator is expected to be the most efficient under G​E​X​O​GGEXOG. Consistent with this prediction, it attains the smallest MSE across the values of NN and TT examined in our simulations and also exhibits the smallest bias in most cases.

(Table [3](https://arxiv.org/html/2601.21272v1#Sx1.T3 "Table 3 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") around here)

Table [3](https://arxiv.org/html/2601.21272v1#Sx1.T3 "Table 3 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") reports the results under the E​B​DEBD condition. The E​B​DEBD design violates the exogeneity requirements necessary for the OLS, FGLS-CO, and FGLS-D estimators to be consistent; however, the GD estimator remains consistent. Simulation evidence supports this prediction. While the biases of all estimators except the GD and BC-GD estimators do not decrease as TT increases, the GD and BC-GD estimators exhibit a bias that decreases with TT and is the smallest among the estimators considered. In terms of MSE, the OLS, FGLS-CO, and FGLS-D estimators have large MSEs. In contrast, the MSEs of the GD and BC-GD estimators are the smallest. This is consistent with the theoretical requirement that the GD estimator is an efficient estimator under the E​B​DEBD condition.

### 3.3 Size and power of tests

In this subsection, we examine the finite-sample size and power of the proposed Wald tests for model specification. In linear asset-pricing applications, the joint null hypothesis H0:𝜶=𝟎H\_{0}:{\mbox{$\alpha$}}={\mbox{$0$}} is commonly assessed using the GRS test (Gibbons et al. [1989](https://arxiv.org/html/2601.21272v1#bib.bib1878 "A test of the efficiency of a given portfolio")), the HAR test of Lazarus et al. ([2018](https://arxiv.org/html/2601.21272v1#bib.bib2118 "HAR inference: recommendations for practice"), [2021](https://arxiv.org/html/2601.21272v1#bib.bib1946 "The size-power tradeoff in har inference")), as well as Wald tests based on FGLS-CO (Nagakura [2024](https://arxiv.org/html/2601.21272v1#bib.bib1985 "Cochrane–orcutt type estimator for multivariate linear regression model with serially correlated errors")) and FGLS-D (Perron and González-Coya [2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")). We use these established methods as benchmarks and compare them with (i) the Wald test based on the GD estimator and (ii) its bootstrap bias-corrected variants proposed in this paper.

#### 3.3.1 GRS test

The GRS test statistic of Gibbons et al. ([1989](https://arxiv.org/html/2601.21272v1#bib.bib1878 "A test of the efficiency of a given portfolio")) is one of the most widely used statistical tests for evaluating asset pricing models (see, e.g., Fama and French ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds"), [2015](https://arxiv.org/html/2601.21272v1#bib.bib1869 "A five-factor asset pricing model"), [2016](https://arxiv.org/html/2601.21272v1#bib.bib1870 "Dissecting anomalies with a five-factor model"), [2017](https://arxiv.org/html/2601.21272v1#bib.bib1871 "International tests of a five-factor asset pricing model"), [2018](https://arxiv.org/html/2601.21272v1#bib.bib1872 "Choosing factors"), [2020](https://arxiv.org/html/2601.21272v1#bib.bib2161 "Comparing cross-section and time-seriesfactor models")); Cakici et al. ([2013](https://arxiv.org/html/2601.21272v1#bib.bib2160 "Size, value, and momentum in emerging market stock returns"))). Define the following quantities:

|  |  |  |
| --- | --- | --- |
|  | 𝒙¯=1T​∑t=1T𝒙t,𝑺x=1T−1​∑t=1T(𝒙t−𝒙¯)​(𝒙t−𝒙¯)′,𝚺^=1T−k−1​∑t=1T𝒖^t​𝒖^t′\bar{{\mbox{$x$}}}=\frac{1}{T}\sum\_{t=1}^{T}{\mbox{$x$}}\_{t},\quad{\mbox{$S$}}\_{x}=\frac{1}{T-1}\sum\_{t=1}^{T}({\mbox{$x$}}\_{t}-\bar{{\mbox{$x$}}})({\mbox{$x$}}\_{t}-\bar{{\mbox{$x$}}})^{\prime},\quad\widehat{{\mbox{$\Sigma$}}}=\frac{1}{T-k-1}\sum\_{t=1}^{T}\widehat{{\mbox{$u$}}}\_{t}\widehat{{\mbox{$u$}}}\_{t}^{\prime} |  |

where 𝒖^t\widehat{{\mbox{$u$}}}\_{t} denotes the OLS residuals. The GRS test statistic is then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​R​S=T​(T−N−k)N​(T−k−1)​(1+𝒙¯​𝑺x−1​𝒙¯)−1​𝜶^OLS⁣′​𝚺^−1​𝜶^OLSGRS=\frac{T(T-N-k)}{N(T-k-1)}(1+\bar{{\mbox{$x$}}}{\mbox{$S$}}\_{x}^{-1}\bar{{\mbox{$x$}}})^{-1}\widehat{{\mbox{$\alpha$}}}^{\mathrm{OLS}\prime}\widehat{{\mbox{$\Sigma$}}}^{-1}\widehat{{\mbox{$\alpha$}}}^{\mathrm{OLS}} |  | (32) |

Under the assumption that 𝒖t{\mbox{$u$}}\_{t} is independently and identically distributed according to a multivariate normal distribution, the statistic G​R​SGRS follows an F​(N,T−N−k)F(N,T-N-k) distribution under the null hypothesis H0:𝜶=𝟎H\_{0}:{\mbox{$\alpha$}}={\mbox{$0$}}. 555Kamstra and Shi ([2024](https://arxiv.org/html/2601.21272v1#bib.bib1935 "Testing and ranking of asset pricing models using the grs statistic")) propose a modified version of the GRS test to improve its small-sample properties. However, the performance of the original and modified GRS tests does not differ substantially once the sample size TT exceeds 200. For this reason, we rely exclusively on the original GRS test as a benchmark. This statistic jointly tests whether all pricing errors are equal to zero across portfolios.

#### 3.3.2 HAR test

When regression errors exhibit heteroskedasticity and autocorrelation, specification tests that ignore these features are invalid. A prominent approach that accounts for both heteroskedasticity and autocorrelation is the heteroskedasticity and autocorrelation robust (HAR) test based on the heteroskedasticity and autocorrelation consistent (HAC) estimators of Newey and West ([1987](https://arxiv.org/html/2601.21272v1#bib.bib233 "A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix")). Under kernel-based nonparametric estimation, the long-run covariance matrix

|  |  |  |
| --- | --- | --- |
|  | 𝛀=𝚪0+∑j=1∞(𝚪j+𝚪j′),𝚪j=𝔼​[𝒗t​𝒗t−j′],𝒗t=𝒁t​𝒖t,{\mbox{$\Omega$}}={\mbox{$\Gamma$}}\_{0}+\sum\_{j=1}^{\infty}\big({\mbox{$\Gamma$}}\_{j}+{\mbox{$\Gamma$}}\_{j}^{\prime}\big),\quad{\mbox{$\Gamma$}}\_{j}={\mathbb{E}}[{\mbox{$v$}}\_{t}{\mbox{$v$}}\_{t-j}^{\prime}],\quad{\mbox{$v$}}\_{t}={\mbox{$Z$}}\_{t}{\mbox{$u$}}\_{t}, |  |

is estimated as

|  |  |  |
| --- | --- | --- |
|  | 𝛀^​(M)=∑j=−(T−1)T−1k​(jM)​𝚲^​(j),𝚲^​(j)=1T​∑t=j+1T𝒗^t​𝒗^t−j′,𝒗^t=𝒁t​𝒖^t.\widehat{{\mbox{$\Omega$}}}(M)=\sum\_{j=-(T-1)}^{T-1}k\Big(\frac{j}{M}\Big)\widehat{{\mbox{$\Lambda$}}}(j),\quad\widehat{{\mbox{$\Lambda$}}}(j)=\frac{1}{T}\sum\_{t=j+1}^{T}\widehat{{\mbox{$v$}}}\_{t}\widehat{{\mbox{$v$}}}\_{t-j}^{\prime},\quad\widehat{{\mbox{$v$}}}\_{t}={\mbox{$Z$}}\_{t}\widehat{{\mbox{$u$}}}\_{t}. |  |

Under the conditions M→∞M\to\infty and M/T→0M/T\to 0 as T→∞T\to\infty, we can consistently estimate 𝛀\Omega. The corresponding Wald statistic is given by

|  |  |  |
| --- | --- | --- |
|  | 𝒲HAC=(𝑹𝜿^OLS−𝒓)′[𝑹(𝒁𝒁′/T)−1𝛀^(M)(𝒁𝒁′/T)−1𝑹′](𝑹𝜿^OLS−𝒓)\mathcal{W}^{\mathrm{HAC}}=({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{OLS}}-{\mbox{$r$}})^{\prime}\mathopen{}\left[{\mbox{$R$}}({\mbox{$Z$}}{\mbox{$Z$}}^{\prime}/T)^{-1}\widehat{{\mbox{$\Omega$}}}(M)({\mbox{$Z$}}{\mbox{$Z$}}^{\prime}/T)^{-1}{\mbox{$R$}}^{\prime}\mathclose{}\right]({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{OLS}}-{\mbox{$r$}}) |  |

which, under the null, converges in distribution to either the standard normal or a χ2\chi^{2} distribution depending on the normalization.

A key practical issue is the choice of the bandwidth parameter MM in the kernel estimator. In small samples, such choices can lead to substantial size distortions, often producing over-rejection. To address this problem, Kiefer et al. ([2000](https://arxiv.org/html/2601.21272v1#bib.bib1937 "Simple robust testing of regression hypotheses")) introduce a nonsingular data-dependent stochastic transformation that eliminates the need for consistent estimation of 𝛀\Omega. Specifically, they proposed the fixed-bb approach, in which the bandwidth is proportional to the sample size,

|  |  |  |
| --- | --- | --- |
|  | M=b​T,b∈(0,1].M=bT,\quad b\in(0,1]. |  |

By fixing M/T=bM/T=b, the long-run covariance estimator 𝛀^​(b​T)\widehat{{\mbox{$\Omega$}}}(bT) converges to a random limit, sacrificing consistency in favor of a nonstandard limiting distribution that depends on the kernel and bb. This approach improves finite-sample size control relative to conventional HAC-based HAR tests (e.g., Sun ([2014](https://arxiv.org/html/2601.21272v1#bib.bib2163 "Let’s fix it: fixed-b aymptotics versus small-b asymptotics in heteroskedasticity and autocorrelation robust inference"))).

Kiefer and Vogelsang ([2002a](https://arxiv.org/html/2601.21272v1#bib.bib1936 "Heteroskedasticity-autocorrelation robust standard errors using the bartlett kernel without truncation")) show that setting b=1b=1 (i.e., M=TM=T) yields a HAR statistic based on the Bartlett kernel with no truncation, which follows a nonstandard limiting distribution. Kiefer and Vogelsang ([2005](https://arxiv.org/html/2601.21272v1#bib.bib2115 "A new asymptotic theory for heteroskedasticity-autocorrelation robust tests")) generalize this framework by developing fixed-bb asymptotics for any b∈(0,1]b\in(0,1], thereby unifying the theory. Subsequent work (e.g., Jansson [2004](https://arxiv.org/html/2601.21272v1#bib.bib2162 "The error in rejection probability of simple autocorrelation robust tests")) demonstrates that fixed-bb asymptotics incorporate the sampling uncertainty of long-run covariance estimation into the first-order asymptotics, mitigating the size distortions inherent in the conventional small-bb framework. Building on these insights, Lazarus et al. ([2018](https://arxiv.org/html/2601.21272v1#bib.bib2118 "HAR inference: recommendations for practice"), [2021](https://arxiv.org/html/2601.21272v1#bib.bib1946 "The size-power tradeoff in har inference")) provide a comprehensive comparison of fixed-bb methods, established the size-power frontier, and propose loss-function-based rules for selecting bb. They show that the frontier is achieved with the quadratic spectral (QS) kernel. Against this background, we adopt the fixed-bb HAR test with the QS kernel developed by Lazarus et al. ([2018](https://arxiv.org/html/2601.21272v1#bib.bib2118 "HAR inference: recommendations for practice"), [2021](https://arxiv.org/html/2601.21272v1#bib.bib1946 "The size-power tradeoff in har inference")).

#### 3.3.3 Wald test based on the FGLS-CO estimator

Nagakura ([2024](https://arxiv.org/html/2601.21272v1#bib.bib1985 "Cochrane–orcutt type estimator for multivariate linear regression model with serially correlated errors")) extends [Cochrane and Orcutt](https://arxiv.org/html/2601.21272v1#bib.bib1857 "Application of least squares regression to relationships containing auto-correlated error terms")’s ([1949](https://arxiv.org/html/2601.21272v1#bib.bib1857 "Application of least squares regression to relationships containing auto-correlated error terms")) autoregressive GLS procedure to a multiple-equation system by assuming that the disturbance vector follows a VAR(pp) process. Since the FGLS-CO estimator has the following asymptotic variance

|  |  |  |
| --- | --- | --- |
|  | T​(𝜿^CO−𝜿)→𝑑𝒩​(𝟎,𝑽CO),𝑽CO:=𝔼​[𝒁t∗​𝛀−1​𝒁t∗⁣′]−1,\sqrt{T}\big(\widehat{{\mbox{$\kappa$}}}^{\mathrm{CO}}-{\mbox{$\kappa$}}\big)\xrightarrow{d}\mathcal{N}\big({\mbox{$0$}},\ {\mbox{$V$}}^{\mathrm{CO}}\big),\quad{\mbox{$V$}}^{\mathrm{CO}}:={\mathbb{E}}[{\mbox{$Z$}}\_{t}^{\*}{\mbox{$\Omega$}}^{-1}{\mbox{$Z$}}\_{t}^{\*\prime}]^{-1}, |  |

under the null hypothesis H0:𝑹𝜿=𝒓H\_{0}:{\mbox{$R$}}{\mbox{$\kappa$}}={\mbox{$r$}} the corresponding Wald statistic is given by

|  |  |  |
| --- | --- | --- |
|  | 𝒲CO=(𝑹​𝜿^CO−𝒓)′​[𝑹​𝑽^CO​𝑹′]−1​(𝑹​𝜿^CO−𝒓)→𝑑χd2.\mathcal{W}^{\mathrm{CO}}=\big({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{CO}}-{\mbox{$r$}}\big)^{\prime}\Big[{\mbox{$R$}}\widehat{{\mbox{$V$}}}^{\mathrm{CO}}{\mbox{$R$}}^{\prime}\Big]^{-1}\big({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{CO}}-{\mbox{$r$}}\big)\xrightarrow{d}\chi\_{d}^{2}. |  |

In contrast to the OLS-based GRS test, the Wald test based on the FGLS-CO estimator can deliver more precise inference under the B​DBD condition. However, its validity is fragile: under weaker exogeneity conditions such as G​E​X​O​GGEXOG or E​B​DEBD, the FGLS-CO estimator loses consistency, highlighting the trade-off between efficiency gains and robustness (e.g., see Proposition [5](https://arxiv.org/html/2601.21272v1#Thmproposition5 "Proposition 5 (Consistency region of CO-type estimators): ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")).

#### 3.3.4 Wald test based on the FGLS-D estimator

Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")) propose an FGLS-D estimator. The extention to the multiple-equation system is shown as in ([21](https://arxiv.org/html/2601.21272v1#S2.E21 "In item (Step 2) Quasi-differencing and GLS on the filtered system. ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")). The asymptotic normality of the FGLS-D estimator is given as

|  |  |  |
| --- | --- | --- |
|  | T​(𝜿^FGLS−D−𝜿)→𝑑𝒩​(𝟎,𝑽FGLS−D),𝑽FGLS−D:=(𝔼​[𝒁Q​D,t′​𝚺−1​𝒁Q​D,t])−1.\sqrt{T}\big(\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS-D}}-{\mbox{$\kappa$}}\big)\xrightarrow{d}\mathcal{N}\big({\mbox{$0$}},\ {\mbox{$V$}}^{\mathrm{FGLS-D}}\big),\quad{\mbox{$V$}}^{\mathrm{FGLS-D}}:=\big({\mathbb{E}}[{\mbox{$Z$}}\_{QD,t}^{\prime}{\mbox{$\Sigma$}}^{-1}{\mbox{$Z$}}\_{QD,t}]\big)^{-1}. |  |

Hence, under the null hypothesis H0:𝑹𝜿=𝒓H\_{0}:{\mbox{$R$}}{\mbox{$\kappa$}}={\mbox{$r$}}, the Wald statistic is

|  |  |  |
| --- | --- | --- |
|  | 𝒲FGLS−D=(𝑹​𝜿^FGLS−D−𝒓)′​[𝑹​𝑽^FGLS−D​𝑹′]​(𝑹​𝜿^FGLS−D−𝒓)→𝑑χd2.\mathcal{W}^{\mathrm{FGLS-D}}=\big({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS-D}}-{\mbox{$r$}}\big)^{\prime}\Big[{\mbox{$R$}}\widehat{{\mbox{$V$}}}^{\mathrm{FGLS-D}}{\mbox{$R$}}^{\prime}\Big]\big({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS-D}}-{\mbox{$r$}}\big)\xrightarrow{d}\chi\_{d}^{2}. |  |

FGLS-D differs from the conventional FGLS-CO estimator only in the prefiltering step: instead of filtering with VAR parameters fitted to OLS residuals, it estimates the lag polynomial from a Durbin regression and uses that filter to quasi-difference the system. This can deliver efficiency gains when the G​E​X​O​GGEXOG condition holds as shown in section [2](https://arxiv.org/html/2601.21272v1#S2 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"). However, under E​B​DEBD, both FGLS-CO and FGLS-D lose consistency, whereas Durbin remains consistent (and efficient).

### 3.4 Simulation Results

In this subsection, we report results from Monte Carlo experiments. First, we examine size by checking whether each test’s empirical rejection frequency under the null matches the nominal significance level. Second, we assess power, that is, the ability of each test to detect departures from the null. Together, these results illustrate how the competing procedures trade off size (Type I error) and test power (Type II error) across the three DGPs, B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD.

Throughout, 𝒲B​C​-​G​D\mathcal{W}^{BC\text{-}GD} denotes the bootstrap bias-corrected Wald test based on the GD estimator, while 𝒲G​D\mathcal{W}^{GD}, 𝒲F​G​L​S​-​D\mathcal{W}^{FGLS\text{-}D}, and 𝒲F​G​L​S​-​C​O\mathcal{W}^{FGLS\text{-}CO} denote Wald tests based on the GD, FGLS-D, and FGLS-CO estimators, respectively. We also consider the H​A​RHAR test constructed using the fixed-bb HAC estimator of Lazarus et al. ([2018](https://arxiv.org/html/2601.21272v1#bib.bib2118 "HAR inference: recommendations for practice"), [2021](https://arxiv.org/html/2601.21272v1#bib.bib1946 "The size-power tradeoff in har inference")), and the G​R​SGRS test of Gibbons et al. ([1989](https://arxiv.org/html/2601.21272v1#bib.bib1878 "A test of the efficiency of a given portfolio")). Under the null hypothesis H0:𝜶0=𝟎N,1H\_{0}:{\mbox{$\alpha$}}\_{0}={\mbox{$0$}}\_{N,1}, we report empirical rejection frequencies at the nominal 10%, 5%, and 1% significance levels.

#### 3.4.1 Rejection Frequencies under the Null Hypothesis

(Table [4](https://arxiv.org/html/2601.21272v1#Sx1.T4 "Table 4 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") around here)

Table [4](https://arxiv.org/html/2601.21272v1#Sx1.T4 "Table 4 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") reports rejection frequencies under the B​DBD condition and the null. The HAR test delivers rejection frequencies close to nominal levels regardless of the cross-sectional dimension. However, the Wald tests based on GD, FGLS-D, and FGLS-CO tends to over reject the null hypothesis in finite samples. While FGLS-CO is asymptotically efficient under B​DBD, its associated Wald statistic does not dominate in finite samples. In contrast, the Wald test based on the BC-GD performs well. Its rejection frequencies are close to nominal levels, reflecting the consistency of the underlying estimators.

(Table [5](https://arxiv.org/html/2601.21272v1#Sx1.T5 "Table 5 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") around here)

Next, we examine the size distortion of each test under the G​E​X​O​GGEXOG condition in Talbe [5](https://arxiv.org/html/2601.21272v1#Sx1.T5 "Table 5 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"). Under the G​E​X​O​GGEXOG, the OLS estimators of 𝜶\alpha and 𝜷\beta in ([2](https://arxiv.org/html/2601.21272v1#S2.E2 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) are inconsistent due to dynamic regressor-error dependence. Consequently, test statistics that rely on OLS estimator theoretically do not converge to their expected distributions. In line with this, the GRS test and the HAR test severely over-reject the null across all cross-sectional dimensions NN and factor counts kk, missing the nominal 10%, 5%, and 1% levels by wide margins. By contrast, the Wald test based on the FGLS-CO estimator exhibits smaller size distortions (though it is not exact). This pattern accords with Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")), who show, in a single-equation setting, that inference based on the FGLS-D estimator is more robust to misspecification than OLS-based procedures. As in the case of the B​DBD condition, the Wald test based on the BC-GD estimator deliver rejection frequencies close to nominal levels across NN and kk.

(Table [6](https://arxiv.org/html/2601.21272v1#Sx1.T6 "Table 6 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") around here)

Finally, we investigate the size performance under the E​B​DEBD condition in Table [6](https://arxiv.org/html/2601.21272v1#Sx1.T6 "Table 6 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"). Theory implies that only the GD estimator is consistent among the procedures considered. Accordingly, tests that depend on OLS estimator, the GRS and the HAR tests, are severely oversized. Furthermore, the Wald tests based on the FGLS-D and FGLS-CO estimators also exhibit severe size distrotions. While the GD estimator is consistent, its Wald test tend to over reject the null hypothesis. In contrast, the rejection frequencies of the Wald test based on the BC-GD estimator are close to nominal level regardless of NN and kk.

#### 3.4.2 Rejection Frequencies under the Alternative Hypothesis

Next, we examine the size-adjusted power of each test under B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD conditions. Since finite-sample size distortions can substantially affect rejection frequencies, raw power is not directly comparable across tests. We therefore report size-adjusted power to ensure that differences in rejection frequencies reflect each test’s genuine ability to detect departures from the null. Here, we consider the alternative hypothesis H1:α1=0.2H\_{1}:\alpha\_{1}=0.2 and αj=0\alpha\_{j}=0 for j≠1j\neq 1.

(Table [7](https://arxiv.org/html/2601.21272v1#Sx1.T7 "Table 7 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") around here)

Table [7](https://arxiv.org/html/2601.21272v1#Sx1.T7 "Table 7 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") reports rejection frequencies under the fixed alternative for the B​DBD condition. We evaluate size-adjusted power by examining whether rejection frequencies increase with the sample size TT and converge to one. Under B​DBD, all estimators are consistent, implying that their associated tests are consistent and should achieve power against fixed alternatives as TT grows. However, the G​R​SGRS test exhibits noticeably lower power, regardless of NN. This pattern is consistent with Affleck-Graves and McDonald ([1989](https://arxiv.org/html/2601.21272v1#bib.bib1501 "Nonnormalities and tests of asset pricing theories")), who show that departures from normality can substantially reduce the power of the G​R​SGRS test.

The HAR test also delivers reasonably good power under the B​DBD, in line with Lazarus et al. ([2021](https://arxiv.org/html/2601.21272v1#bib.bib1946 "The size-power tradeoff in har inference")), who show that the fixed-bb H​A​RHAR test with the QS kernel attains the asymptotic size–power frontier. Furthermore, the GLS-based Wald tests, those based on G​D​-​BGD\text{-}B, G​DGD, F​G​L​S​-​DFGLS\text{-}D, and F​G​L​S​-​C​OFGLS\text{-}CO, exhibit strong power across all cross-sectional dimensions considered.

(Table [8](https://arxiv.org/html/2601.21272v1#Sx1.T8 "Table 8 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") around here)

Table [8](https://arxiv.org/html/2601.21272v1#Sx1.T8 "Table 8 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") reports size-adjusted power under the G​E​X​O​GGEXOG condition. Since the OLS estimator in ([2](https://arxiv.org/html/2601.21272v1#S2.E2 "In 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is inconsistent under the G​E​X​O​GGEXOG condition, the OLS-based tests (GRS and HAR) exhibit low test power. While the FGLS-CO estimator is based on the OLS estimator, it exhibits reasonably good power. This result aligns with Perron and González-Coya ([2022](https://arxiv.org/html/2601.21272v1#bib.bib2158 "Feasible gls for time series regression")), who demonstrated that the FGLS-CO estimator is robust to moderate model misspecifications. The Wald tests based on BC-GD, GD, and FGLS-D estimators demonstrate significant power under the alternative hypothesis, with rejection frequencies increasing with TT.

(Table [9](https://arxiv.org/html/2601.21272v1#Sx1.T9 "Table 9 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") around here)

Finally, we examine the size-adjusted power under the E​B​DEBD condition, which is reported in Table [9](https://arxiv.org/html/2601.21272v1#Sx1.T9 "Table 9 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"). Under the E​B​DEBD, only the GD-based estimators are consistent, whereas the remaining estimators are misspecified and hence their associated tests lose power as TT increases. Consistent with this implication, the size-adjusted power of all competing procedures, except for G​D​-​BGD\text{-}B and G​DGD, declines markedly under E​B​DEBD. The deterioration is particularly pronounced for the OLS-based tests (G​R​SGRS and H​A​RHAR).

Taken together, the size and size-adjusted power results across the B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD designs indicate that the Wald test based on G​DGD tends to over-reject the null in finite samples. In contrast, the Wald test based on the bootstrap bias-corrected G​DGD estimator (G​D​-​BGD\text{-}B) delivers stable size control and competitive power across all DGPs.

## 4 Empirical Application

We examine whether the Wald test based on the generalized Durbin estimator proposed in this paper can mitigate the over-rejection problem observed for Wald tests based on the FGLS-D and FGLS-CO estimators. In Section [2](https://arxiv.org/html/2601.21272v1#S2 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), we show that, under the E​B​DEBD condition, the generalized Durbin estimator is consistent, whereas the FGLS-D and FGLS-CO estimators are not. Our simulation results in Section [3](https://arxiv.org/html/2601.21272v1#S3 "3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), however, indicate that the Wald test based on the generalized Durbin estimator can still exhibit non-negligible size distortions in finite samples. We therefore employ a bootstrap bias correction to improve finite-sample size control.

To illustrate the empirical relevance of our approach, we revisit the Fama–French multifactor models studied by Fama and French ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds"), [2015](https://arxiv.org/html/2601.21272v1#bib.bib1869 "A five-factor asset pricing model")). As noted by Moriya and Noda ([2024](https://arxiv.org/html/2601.21272v1#bib.bib1743 "Time instability of the fama-french multifactor models: an international evidence")), there remains ongoing debate over the validity of the FF multifactor models. In empirical studies (e.g., Fama and French ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds"), [2015](https://arxiv.org/html/2601.21272v1#bib.bib1869 "A five-factor asset pricing model"), [2016](https://arxiv.org/html/2601.21272v1#bib.bib1870 "Dissecting anomalies with a five-factor model"), [2017](https://arxiv.org/html/2601.21272v1#bib.bib1871 "International tests of a five-factor asset pricing model"), [2018](https://arxiv.org/html/2601.21272v1#bib.bib1872 "Choosing factors"), [2020](https://arxiv.org/html/2601.21272v1#bib.bib2161 "Comparing cross-section and time-seriesfactor models")); Cakici et al. ([2013](https://arxiv.org/html/2601.21272v1#bib.bib2160 "Size, value, and momentum in emerging market stock returns"))), it has become standard practice to apply the GRS test to assess the validity of FF multifactor models. However, our simulation evidence in Section [3](https://arxiv.org/html/2601.21272v1#S3 "3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") shows that both the GRS test and the HAR test can suffer severe size distortions when the B​DBD condition fails. Because B​DBD is more restrictive, and thus less empirically plausible, than E​B​DEBD, and because the GRS and HAR tests are consistent under B​DBD but not under E​B​DEBD, we do not employ these procedures in our empirical analysis. Instead, we compare the bootstrap bias-corrected Wald test based on the generalized Durbin estimator with Wald tests based on the FGLS-D and FGLS-CO estimators.

### 4.1 Fama–French Multifactor Models

Following Fama and French ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds"), [2015](https://arxiv.org/html/2601.21272v1#bib.bib1869 "A five-factor asset pricing model")), we introduce the FF multifactor models. Equation ([33](https://arxiv.org/html/2601.21272v1#S4.E33 "In 4.1 Fama–French Multifactor Models ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) presents [Fama and French](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds")’s ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds")) three-factor (hereafter referred to as FF3) model, which is the most widely known multifactor model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ri,t−Rf,t=αi+βiM​k​t​(Rm,t−Rf,t)+βiS​M​B​S​M​Bt+βiH​M​L​H​M​Lt+εi,t,R\_{i,t}-R\_{f,t}=\alpha\_{i}+\beta^{Mkt}\_{i}(R\_{m,t}-R\_{f,t})+\beta^{SMB}\_{i}SMB\_{t}+\beta^{HML}\_{i}HML\_{t}+\varepsilon\_{i,t}, |  | (33) |

where Ri,tR\_{i,t} denotes the return on the portfolio ii at time tt, Rf,tR\_{f,t} is the risk-free rate at time tt, Rm,tR\_{m,t} is the returns on the market portfolio at time tt, and εi,t\varepsilon\_{i,t} is the error term for portfolio ii at time tt. The FF3 model expands the CAPM by adding size and value risk factors to capture market anomalies. The size risk factor (S​M​BtSMB\_{t}) reflects the empirical regularity that stocks with smaller (or larger) market capitalizations tend to earn higher returns, while the value risk factor (H​M​LtHML\_{t}) accounts for the superior performance of stocks with low (or high) price-to-book ratios. Building on the FF3 model, Fama and French ([2015](https://arxiv.org/html/2601.21272v1#bib.bib1869 "A five-factor asset pricing model")) propose a five-factor model (hereafter referred to as FF5), as shown in Equation ([34](https://arxiv.org/html/2601.21272v1#S4.E34 "In 4.1 Fama–French Multifactor Models ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ri,t−Rf,t=αi+βiM​k​t​(Rm,t−Rf,t)+βiS​M​B​S​M​Bt+βiH​M​L​H​M​Lt+βiR​M​W​R​M​Wt+βiC​M​A​C​M​At+εi,t.\begin{split}R\_{i,t}-R\_{f,t}=\alpha\_{i}+\beta^{Mkt}\_{i}(R\_{m,t}-R\_{f,t})+\beta^{SMB}\_{i}SMB\_{t}+\beta^{HML}\_{i}HML\_{t}\\ +\beta^{RMW}\_{i}RMW\_{t}+\beta^{CMA}\_{i}CMA\_{t}+\varepsilon\_{i,t}.\end{split} |  | (34) |

This model adds two risk factors to FF3: the profitability risk factor (R​M​WtRMW\_{t}) and the investment risk factor (C​M​AtCMA\_{t}). The models are said to correctly capture the behavior of stock returns if all intercept terms αi\alpha\_{i} for each portfolio in Equations ([33](https://arxiv.org/html/2601.21272v1#S4.E33 "In 4.1 Fama–French Multifactor Models ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) and ([34](https://arxiv.org/html/2601.21272v1#S4.E34 "In 4.1 Fama–French Multifactor Models ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) are not significantly different from zero. Therefore, to assess the validity of the FF multifactor models, we test the following null hypothesis:

|  |  |  |
| --- | --- | --- |
|  | H0:𝜶=𝟎,H1:not​H0H\_{0}:{\mbox{$\alpha$}}={\mbox{$0$}},\ \ H\_{1}:{\rm{not}}\ H\_{0} |  |

where 𝜶={αi}i=1N{\mbox{$\alpha$}}=\mathopen{}\left\{\alpha\_{i}\mathclose{}\right\}\_{i=1}^{N} in each of Equations ([33](https://arxiv.org/html/2601.21272v1#S4.E33 "In 4.1 Fama–French Multifactor Models ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) and ([34](https://arxiv.org/html/2601.21272v1#S4.E34 "In 4.1 Fama–French Multifactor Models ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")).

### 4.2 Dataset

Fama and French ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds"), [2015](https://arxiv.org/html/2601.21272v1#bib.bib1869 "A five-factor asset pricing model")) provide the returns on the benchmark portfolios and risk factors for examining the FF multifactor models. In these models, the benchmark portfolios are formed by classifying all stocks in the market into either 2×3=6​or​ 5×5=252\times 3=6\ {\rm{or}}\ 5\times 5=25 categories using two criteria (e.g., “market capitalization (firm size) and book-to-market ratio (MB)” as proposed by Fama and French ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds"))). The average return of each portfolio is regarded as the representative portfolio in the market. Other sorting criteria have also been proposed, such as “market capitalization and profitability (MO)” and “market capitalization and investment growth rate (MI)” (Fama and French ([2015](https://arxiv.org/html/2601.21272v1#bib.bib1869 "A five-factor asset pricing model"))).

Lewellen et al. ([2010](https://arxiv.org/html/2601.21272v1#bib.bib1717 "A skeptical appraisal of asset pricing tests")) point out that many studies test the FF multifactor models using portfolios sorted by “market capitalization (firm size)” and “book-to-market ratio,” but the models may not perform as well when using portfolios sorted by other criteria. To consider the possibility that different sorting methods may affect the results, we use three types of benchmark portfolios to compare the performance of the Wald test based on the generalized Durbin estimator proposed in this paper with the GRS test.

Furthermore, the FF multifactor models are often rejected when U.S. data are used, as documented in Fama and French ([2012](https://arxiv.org/html/2601.21272v1#bib.bib1874 "Size, value, and momentum in international stock returns"), [2017](https://arxiv.org/html/2601.21272v1#bib.bib1871 "International tests of a five-factor asset pricing model")). In this study, following much of the previous literature, we use U.S. monthly data to examine whether such rejections may be driven by the use of unsuitable test statistics, such as the GRS statistic. All datasets are available from [Professor Kenneth French’s website](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). For the U.S. monthly data used in this study, the available sample spans July 1990 to November 2025. Our estimation period is restricted to the post-global financial crisis (GFC) period, from October 2008 (the month following the Lehman Brothers bankruptcy) to November 2025. We adopt this window because the estimators we employ are time-invariant and do not explicitly accommodate structural breaks.

A large literature documents that the GFC coincided with shifts in equity-market comovements and factor sensitivities. In particular, Bekaert et al. ([2014](https://arxiv.org/html/2601.21272v1#bib.bib2206 "The global crisis and equity market contagion")) report crisis-period changes in CAPM betas and increases in residual correlations around the Lehman episode. In addition, Lehkonen ([2015](https://arxiv.org/html/2601.21272v1#bib.bib2207 "Stock market integration and the globalfinancial crisis")) document regime-dependent changes in international stock-market integration during the GFC, suggesting that coefficients in FF multi-factor models may have shifted in that period. While the COVID-19 pandemic is widely viewed as a potential source of structural change in global equity markets, Ndako et al. ([2025](https://arxiv.org/html/2601.21272v1#bib.bib2198 "Structural breaks in global stock markets: are they caused by pandemics, protests or other factors?")) report that, using [Bai and Perron](https://arxiv.org/html/2601.21272v1#bib.bib1847 "Estimating and testing linear models with multiple structural changes")’s ([1998](https://arxiv.org/html/2601.21272v1#bib.bib1847 "Estimating and testing linear models with multiple structural changes"); [2003a](https://arxiv.org/html/2601.21272v1#bib.bib1848 "Computation and analysis of multiple structural change models"); [2003b](https://arxiv.org/html/2601.21272v1#bib.bib2211 "Critical values for multiple structural change tests")) multiple structural break tests, no additional break aligned with the onset of COVID-19 is detected across the countries and regions they analyze. Instead, their evidence points to the GFC as the dominant common event driving structural change in global stock market, and they conclude that the GFC generated the most pronounced breaks in those markets. Accordingly, our baseline sample spans October 2008 to November 2025.

(Table [10](https://arxiv.org/html/2601.21272v1#Sx1.T10 "Table 10 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") around here)

Table [10](https://arxiv.org/html/2601.21272v1#Sx1.T10 "Table 10 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") shows the descriptive statistics and the results of the unit root test for the returns on risk factors in the FF multifactor models. The descriptive statistics show that for all datasets, there are no inconsistent data in the perspective of the traditional mean-variance approach. In the estimations, each variable that appeared in the moment conditions should be stationary. We apply the augmented Dickey–Fuller (ADF) test of Said and Dickey ([1984](https://arxiv.org/html/2601.21272v1#bib.bib1426 "Testing for unit roots in autoregressive-moving average models of unknown order")) to check whether the variables satisfy the stationarity condition. The ADF test rejects the null hypothesis that each variable contains a unit root at the 5% significance level.666The ADF test also rejects the null hypothesis that the returns on the 6 and 25 benchmark portfolios contain a unit root at the 5% significance level, regardless of portfolio sorting method.

### 4.3 Empirical Results

In this subsection, we assess the FF multifactor models using a Wald test based on the generalized Durbin estimator and compare its performance with competing Wald tests based on the FGLS-Durbin and FGLS-CO estimators. To improve finite-sample size control, we also report a bootstrap bias-corrected Wald test based on the generalized Durbin estimator. Overall, Table [11](https://arxiv.org/html/2601.21272v1#Sx1.T11 "Table 11 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") indicates that inference on H0:𝜶=𝟎H\_{0}:{\mbox{$\alpha$}}={\mbox{$0$}} can depend materially on the choice of the estimator underlying the Wald statistic, and that the competing FGLS-based Wald tests tend to reject more frequently, particularly when the number of benchmark portfolios is large, than the bootstrap bias-corrected Wald test based on the generalized Durbin estimator.

(Table [11](https://arxiv.org/html/2601.21272v1#Sx1.T11 "Table 11 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") around here)

Table [11](https://arxiv.org/html/2601.21272v1#Sx1.T11 "Table 11 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") reports the test results for the FF3 model. For MB6, none of the reported Wald statistics rejects the null hypothesis at the 1% significance level. For MB25, the conclusion depends on the test statistic: the bootstrap bias-corrected Wald test based on the generalized Durbin estimator rejects the null at the 5% level but not at the 1% level, whereas the FGLS-based Wald tests yield much smaller pp-values and reject decisively. This contrast indicates that, as the cross-sectional dimension increases, the strength of evidence against the FF3 model becomes more sensitive to the construction of the Wald test.

Table [11](https://arxiv.org/html/2601.21272v1#Sx1.T11 "Table 11 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") also reports the results for the FF5 model and highlights an important interaction between portfolio sorting and test behavior. For benchmark portfolios sorted by MB, none of the statistics rejects the null at the 1% level for MB6, whereas for MB25 the bootstrap bias-corrected Wald test based on the generalized Durbin estimator rejects only at the 10% level while the competing FGLS-based Wald tests reject decisively. In contrast, when portfolios are sorted by MI, the bootstrap bias-corrected Wald test based on the generalized Durbin estimator does not reject the null for either MI6 or MI25, whereas the FGLS-based Wald tests reject for MI25. A similar pattern arises for portfolios sorted by MO: the null is not rejected at the 1% level for MO6 by any statistic, but for MO25 it is not rejected by the bootstrap bias-corrected Wald test based on the generalized Durbin estimator, whereas it is rejected by the FGLS-based Wald tests.

Taken together, these empirical patterns suggest that the bootstrap bias-corrected Wald test based on the generalized Durbin estimator delivers comparatively stable inference across portfolio sorts and is less prone to frequent rejections in higher-dimensional systems. By contrast, the FGLS-based Wald tests can produce substantially more aggressive rejections in the same settings. This contrast is consistent with our simulation evidence that misspecification in the dynamic dependence between regressors and errors can lead to size distortions for competing procedures, whereas the generalized Durbin approach remains reliable for multi-equation specification testing.

## 5 Conclusion

In this paper, we develop a new model specification test for multivariate regression. Our motivation is that commonly used procedures in empirical asset-pricing applications, such as the GRS test and the HAR test, can exhibit substantial size distortions and yield unreliable inference in empirically relevant settings, especially when the data depart from idealized distributional assumptions or when the system dimension is large.

Building on [Durbin](https://arxiv.org/html/2601.21272v1#bib.bib2135 "Testing for serial correlation in least-squares regression when some of the regressorsare lagged dependent variables")’s ([1970](https://arxiv.org/html/2601.21272v1#bib.bib2135 "Testing for serial correlation in least-squares regression when some of the regressorsare lagged dependent variables")) regression framework, we generalize the Durbin approach in two key respects. First, we reformulate it for multivariate seemingly unrelated regressions (SUR) so that cross-equation dependence is explicitly accommodated. This multivariate reformulation allows the test to exploit information in the full system and to remain well-defined in the presence of correlated disturbances across equations. Second, we reinterpret the Durbin correction not as an OLS-based auxiliary regression device, but as a GLS-class estimator. In particular, the proposed generalized Durbin estimator exploits cross-equation covariance and explicitly incorporates the joint second-order dynamics of regressors and disturbances, thereby targeting environments in which regressor-error dependence is dynamic rather than purely exogenous.

These features deliver two central theoretical implications. The generalized Durbin estimator remains consistent under the EBD condition, which allows dynamic dependence between regressors and errors, whereas competing estimators need not be consistent in this environment. Under stronger conditions, it attains GLS efficiency when the cross-equation covariance structure is correctly specified. Based on this estimator, we construct a Wald test for multi-equation specification testing. Because size distortions can still be non-negligible in finite samples, we also consider a bootstrap-based bias-corrected version of the Wald statistic to improve size control in practice.

Our Monte Carlo experiments provide systematic evidence on finite-sample size and test power. The proposed generalized Durbin based Wald test achieves near-nominal size with competitive power across a range of designs, and the bootstrap correction further improves finite-sample reliability. In contrast, conventional procedures can substantially over-reject: the GRS test is particularly sensitive to violations of normality, and HAR-type tests tend to become increasingly conservative or aggressive depending on bandwidth choices and, more importantly, to over-reject as the cross-sectional dimension grows. Taken together, these results underscore the value of explicitly modeling regressor-error dynamic dependence and cross-equation dependence when conducting multivariate specification tests.

Our empirical application illustrates the practical implications of these findings for evaluating the [Fama and French](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds")’s ([1993](https://arxiv.org/html/2601.21272v1#bib.bib1868 "Common risk factors in the returns on stocks and bonds"); [2015](https://arxiv.org/html/2601.21272v1#bib.bib1869 "A five-factor asset pricing model")) multifactor models. We show that inference on the pricing errors can depend materially on the choice of test statistic, especially in higher-dimensional systems and for certain portfolio sorts. In particular, the bootstrap-corrected generalized Durbin based Wald test delivers comparatively stable inference, while competing procedures can yield more aggressive rejections in the same settings. Overall, the proposed approach provides a reliable and practically useful tool for multi-equation specification testing in the presence of cross-equation dependence and regressor-error dynamic dependence, and it offers a principled alternative to conventional procedures that may be prone to size inflation.

## Acknowledgments

The authors thank Tirthatanmoy Das, Katsuhito Iwai, Akitada Kasahara, Genya Kobayashi, Daisuke Nagakura, Yohei Yamamoto, Tatsuma Wada, and participants at the 100th Annual Conference of the Western Economic Association International and the Japan Society of Monetary Economics 2025 Autumn Meeting for helpful comments and suggestions. The author also gratefully acknowledges financial support from the Japan Society for the Promotion of Science, Grant-in-Aid for Scientific Research (Grant Nos. 23H00838 and 23K25535), and from the Japan Science and Technology Agency, Moonshot Research and Development Program (Grant No. JPMJMS2215). All data and programs used in this paper are available upon request.

## References

* J. Affleck-Graves and B. McDonald (1989)
  Nonnormalities and tests of asset pricing theories.
  Journal of Finance 44 (4),  pp. 889–908.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.4.2](https://arxiv.org/html/2601.21272v1#S3.SS4.SSS2.p3.7 "3.4.2 Rejection Frequencies under the Alternative Hypothesis ‣ 3.4 Simulation Results ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* D. W. K. Andrews (1991)
  Heteroskedasticity and autocorrelation consistent covariance matrix estimation.
  Econometrica 59 (3),  pp. 817–858.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. Bai and P. Perron (1998)
  Estimating and testing linear models with multiple structural changes.
  Econometrica 66 (1),  pp. 47–78.
  Cited by: [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p4.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. Bai and P. Perron (2003a)
  Computation and analysis of multiple structural change models.
  Journal of Applied Econometrics 18 (1),  pp. 1–22.
  Cited by: [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p4.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. Bai and P. Perron (2003b)
  Critical values for multiple structural change tests.
  Econometrics Journal 6 (1),  pp. 72–78.
  Cited by: [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p4.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* R. T. Baillie, F. X. Diebold, G. Kapetanios, K. H. Kim, and A. Mora (2024)
  On robust inference in time-series regression.
  Econometrics Journal 28 (2),  pp. 131–173.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p4.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.2](https://arxiv.org/html/2601.21272v1#S2.SS2.p4.2 "2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.3](https://arxiv.org/html/2601.21272v1#S2.SS3.p3.4 "2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2](https://arxiv.org/html/2601.21272v1#S2.p2.1 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.1](https://arxiv.org/html/2601.21272v1#S3.SS1.p4.3 "3.1 Simulation Design ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.1](https://arxiv.org/html/2601.21272v1#S3.SS1.p8.5 "3.1 Simulation Design ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.1](https://arxiv.org/html/2601.21272v1#S3.SS1.p9.16 "3.1 Simulation Design ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.2](https://arxiv.org/html/2601.21272v1#S3.SS2.p1.1 "3.2 Estimation Accuracy ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* B. H. Baltagi and G. Bresson (2011)
  Maximum likelihood estimation and lagrange multiplier tests for panelseemingly unrelated regressions with spatial lag and spatial errors: anapplication to hedonic housing prices in paris.
  Journal of Urban Economics 69 (1),  pp. 24–42.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p1.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* S. Barrios, L. Bertinelli, and E. Strobl (2010)
  Global inflation.
  Review of Economics and Statistics 92 (3),  pp. 524–535.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* M. Bekaert, M. Fratzscher, and A. Mehl (2014)
  The global crisis and equity market contagion.
  Journal of Finance 69 (6),  pp. 2597–2649.
  Cited by: [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p4.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* R. Beran (1988)
  Prepivoting test statistics: a bootstrap view of asymptotic refinements.
  Journal of the American Statistical Association 83 (403),  pp. 687–697.
  Cited by: [§2.6](https://arxiv.org/html/2601.21272v1#S2.SS6.p3.2 "2.6 Bootstrap-corrected Wald test based on the generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. Bernstein and M. I. Nadiri (1989)
  Research and development and intra-industry spillovers: an empirical application of dynamic duality.
  Review of Economic Studies 56 (2),  pp. 249–267.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p1.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* M. Billio, M. Getmansky, A. W. Lo, and L. Pelizzon (2012)
  Econometric measures of connectedness and systemic risk in the finance and insurance sectors.
  Journal of Financial Economics 104 (3),  pp. 535–559.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* S. B. Blomberg, G. D. Hess, and A. Orphanides (2004)
  The macroeconomic consequences of terrorism.
  Journal of Monetary Economics 51 (5),  pp. 1007–1032.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. G. Booth and P. Hall (1994)
  Monte carlo approximation and the iterated boostrap.
  Biometrika 81 (2),  pp. 331–340.
  Cited by: [§2.6](https://arxiv.org/html/2601.21272v1#S2.SS6.p4.4 "2.6 Bootstrap-corrected Wald test based on the generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* T. S. Breusch and A. R. Pagan (1980)
  The lagrange multiplier test and its applications to model specification in econometrics.
  Review of Economic Studies 47 (1),  pp. 239–253.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p1.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2](https://arxiv.org/html/2601.21272v1#S2.p1.1 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* P. J. Brockwell and R. A. Davis (1991)
  Time series: theory and methods.
  2nd edition, Springer.
  Cited by: [§A.1](https://arxiv.org/html/2601.21272v1#Sx2.SS1.p1.21 "A.1 Proof of Proposition 1 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* P. Bühlmann (1997)
  Sieve bootstrap for time series.
  Bernoulli 3 (2),  pp. 123–148.
  Cited by: [§2.6](https://arxiv.org/html/2601.21272v1#S2.SS6.p2.1 "2.6 Bootstrap-corrected Wald test based on the generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* N. Cakici, F. J. Fabozzi, and S. Tan (2013)
  Size, value, and momentum in emerging market stock returns.
  Emerging Markets Review 16,  pp. 46–65.
  Cited by: [§3.3.1](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS1.p1.6 "3.3.1 GRS test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4](https://arxiv.org/html/2601.21272v1#S4.p2.5 "4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* D. Cochrane and G.H. Orcutt (1949)
  Application of least squares regression to relationships containing auto-correlated error terms.
  Journal of the American Statistical Association 44 (245),  pp. 32–61.
  Cited by: [§2.2](https://arxiv.org/html/2601.21272v1#S2.SS2.p8.4 "2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.3](https://arxiv.org/html/2601.21272v1#S2.SS3.p8.3 "2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.3](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS3.p1.1 "3.3.3 Wald test based on the FGLS-CO estimator ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* R. Cont (2001)
  Empirical properties of asset returns: stylized facts and statistical issues.
  Quantitative Finance 1 (2),  pp. 223–236.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* R. Davidson and J. G. MacKinnon (1999)
  The size distortion of bootstrap tests.
  Econometric Theory 15 (3),  pp. 361–376.
  Cited by: [§2.6](https://arxiv.org/html/2601.21272v1#S2.SS6.p2.1 "2.6 Bootstrap-corrected Wald test based on the generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* R. Davidson and J. G. MacKinnon (2007)
  Improving the reliability of bootstrap tests with the fast double bootstrap.
  Computational Statistics & Data Analysis 51 (7),  pp. 3259–3281.
  Cited by: [§2.6](https://arxiv.org/html/2601.21272v1#S2.SS6.p4.4 "2.6 Bootstrap-corrected Wald test based on the generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* W. J. Den Haan and A. Levin (1997)
  A practitioner’s guide to robust covariance matrix estimation,.
  In Robust Inference,
  Handbook of Statistics, Vol. 15,  pp. 299–342.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* F. X. Diebold and K. Yilmaz (2009)
  Measuring financial asset return and volatility spillovers, with application to global equity markets.
  Economic Journal 119 (534),  pp. 158–171.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. Durbin (1970)
  Testing for serial correlation in least-squares regression when some of the regressorsare lagged dependent variables.
  Econometrica 38 (3),  pp. 410–421.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p4.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2](https://arxiv.org/html/2601.21272v1#S2.p2.1 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§5](https://arxiv.org/html/2601.21272v1#S5.p2.1 "5 Conclusion ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* E. F. Fama and K. R. French (1993)
  Common risk factors in the returns on stocks and bonds.
  Journal of Financial Economics 33 (1),  pp. 3–56.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p4.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§1](https://arxiv.org/html/2601.21272v1#S1.p5.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.1](https://arxiv.org/html/2601.21272v1#S2.SS1.p8.2 "2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.1](https://arxiv.org/html/2601.21272v1#S3.SS1.p1.1 "3.1 Simulation Design ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.1](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS1.p1.6 "3.3.1 GRS test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4.1](https://arxiv.org/html/2601.21272v1#S4.SS1.p1.17 "4.1 Fama–French Multifactor Models ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p1.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4](https://arxiv.org/html/2601.21272v1#S4.p2.5 "4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§5](https://arxiv.org/html/2601.21272v1#S5.p5.1 "5 Conclusion ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* E. F. Fama and K. R. French (2012)
  Size, value, and momentum in international stock returns.
  Journal of Financial Economics 105 (3),  pp. 457–472.
  Cited by: [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p3.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* E. F. Fama and K. R. French (2015)
  A five-factor asset pricing model.
  Journal of Financial Economics 116 (1),  pp. 1–22.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p5.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.1](https://arxiv.org/html/2601.21272v1#S2.SS1.p8.2 "2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.1](https://arxiv.org/html/2601.21272v1#S3.SS1.p1.1 "3.1 Simulation Design ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.1](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS1.p1.6 "3.3.1 GRS test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4.1](https://arxiv.org/html/2601.21272v1#S4.SS1.p1.12 "4.1 Fama–French Multifactor Models ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4.1](https://arxiv.org/html/2601.21272v1#S4.SS1.p1.17 "4.1 Fama–French Multifactor Models ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p1.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4](https://arxiv.org/html/2601.21272v1#S4.p2.5 "4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§5](https://arxiv.org/html/2601.21272v1#S5.p5.1 "5 Conclusion ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* E. F. Fama and K. R. French (2016)
  Dissecting anomalies with a five-factor model.
  Review of Financial Studies 29 (1),  pp. 69–103.
  Cited by: [§2.1](https://arxiv.org/html/2601.21272v1#S2.SS1.p8.2 "2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.1](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS1.p1.6 "3.3.1 GRS test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4](https://arxiv.org/html/2601.21272v1#S4.p2.5 "4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* E. F. Fama and K. R. French (2017)
  International tests of a five-factor asset pricing model.
  Journal of Financial Economics 123 (3),  pp. 441–463.
  Cited by: [§3.3.1](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS1.p1.6 "3.3.1 GRS test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p3.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4](https://arxiv.org/html/2601.21272v1#S4.p2.5 "4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* E. F. Fama and K. R. French (2018)
  Choosing factors.
  Journal of Financial Economics 128 (2),  pp. 234–252.
  Cited by: [§3.3.1](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS1.p1.6 "3.3.1 GRS test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4](https://arxiv.org/html/2601.21272v1#S4.p2.5 "4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* E. F. Fama and K. R. French (2020)
  Comparing cross-section and time-seriesfactor models.
  Review of Financial Studies 33 (5),  pp. 1891–1926.
  Cited by: [§3.3.1](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS1.p1.6 "3.3.1 GRS test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§4](https://arxiv.org/html/2601.21272v1#S4.p2.5 "4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* M. R. Gibbons, S. A. Ross, and J. Shanken (1989)
  A test of the efficiency of a given portfolio.
  Econometrica 57 (5),  pp. 1121–1152.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.1](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS1.p1.6 "3.3.1 GRS test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3](https://arxiv.org/html/2601.21272v1#S3.SS3.p1.1 "3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.4](https://arxiv.org/html/2601.21272v1#S3.SS4.p2.8 "3.4 Simulation Results ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* B. Hansen (2022)
  Econometrics.
   Princeton University Press, New Jersey, U.S..
  Cited by: [footnote 1](https://arxiv.org/html/2601.21272v1#footnote1 "In item (A1.2) ‣ Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* C. R. Harvey and A. Siddique (2002)
  Conditional skewness in asset pricing tests.
  Journal of Finance 55 (3),  pp. 1263–1295.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* W. Huang, Q. Liu, G. Rhee, and F. Wu (2012)
  Extreme downside risk and expected stock returns.
  Journal of Banking & Finance 36 (5),  pp. 1492–1502.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* A. B. Jaffe (1989)
  Technological opportunity and spillovers of r&d: evidence from firms’ patents,profits, and market value.
  American Economic Review 76 (5),  pp. 984–1001.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p1.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* M. Jansson (2004)
  The error in rejection probability of simple autocorrelation robust tests.
  Econometrica 72 (3),  pp. 937–946.
  Cited by: [§3.3.2](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS2.p3.9 "3.3.2 HAR test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* M. J. Kamstra and R. Shi (2024)
  Testing and ranking of asset pricing models using the grs statistic.
  Journal of Risk and Financial Management 17 (4).
  Note: 168
  Cited by: [footnote 5](https://arxiv.org/html/2601.21272v1#footnote5 "In 3.3.1 GRS test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* N. M. Kiefer, T. J. Vogelsang, and H. Bunzel (2000)
  Simple robust testing of regression hypotheses.
  Econometrica 68 (3),  pp. 695–714.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.2](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS2.p2.3 "3.3.2 HAR test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* N. M. Kiefer and T. J. Vogelsang (2002a)
  Heteroskedasticity-autocorrelation robust standard errors using the bartlett kernel without truncation.
  Econometrica 70 (5),  pp. 2093–2095.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.2](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS2.p3.9 "3.3.2 HAR test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* N. M. Kiefer and T. J. Vogelsang (2002b)
  Heteroskedasticity-autocorrelation robust testing using bandwidth equal to sample size.
  Econometric Theory 18 (6),  pp. 1350–1366.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* N. M. Kiefer and T. J. Vogelsang (2005)
  A new asymptotic theory for heteroskedasticity-autocorrelation robust tests.
  Econometric Theory 21 (6),  pp. 1130–1164.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.2](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS2.p3.9 "3.3.2 HAR test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* E. Lazarus, D. J. Lewis, J. H. Stock, and M. W. Watson (2018)
  HAR inference: recommendations for practice.
  Journal of Business & Economic Statistics 36 (4),  pp. 541–559.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.2](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS2.p3.9 "3.3.2 HAR test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3](https://arxiv.org/html/2601.21272v1#S3.SS3.p1.1 "3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.4](https://arxiv.org/html/2601.21272v1#S3.SS4.p2.8 "3.4 Simulation Results ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* E. Lazarus, D. J. Lewis, and J. H. Stock (2021)
  The size-power tradeoff in har inference.
  Econometrica 89 (5),  pp. 2497–2516.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.2](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS2.p3.9 "3.3.2 HAR test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3](https://arxiv.org/html/2601.21272v1#S3.SS3.p1.1 "3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.4.2](https://arxiv.org/html/2601.21272v1#S3.SS4.SSS2.p4.7 "3.4.2 Rejection Frequencies under the Alternative Hypothesis ‣ 3.4 Simulation Results ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.4](https://arxiv.org/html/2601.21272v1#S3.SS4.p2.8 "3.4 Simulation Results ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* H. Lehkonen (2015)
  Stock market integration and the globalfinancial crisis.
  Review of Finance 19 (5),  pp. 2039–2094.
  Cited by: [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p4.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. Lewellen, S. Nagel, and J. Shanken (2010)
  A skeptical appraisal of asset pricing tests.
  Journal of Financial Economics 96 (2),  pp. 175–194.
  Cited by: [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p2.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. Lintner (1965)
  The valuation of risky assets and the selection of risky investments in stock portfolios and budget constraints.
  Review of Economics and Statistics 47 (1),  pp. 13–37.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p4.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.1](https://arxiv.org/html/2601.21272v1#S2.SS1.p8.2 "2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* H. Lütkepohl (2005)
  New introduction to multiple time series analysis.
   Springer, Berlin, Germany.
  Cited by: [§2.1](https://arxiv.org/html/2601.21272v1#S2.SS1.p4.7 "2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. D. MacKinnon (2006)
  Bootstrap methods in econometrics.
  The Economic Record 82 (s1),  pp. S2–S18.
  Cited by: [§2.6](https://arxiv.org/html/2601.21272v1#S2.SS6.p2.1 "2.6 Bootstrap-corrected Wald test based on the generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* S. Martin, N. Rice, R. Jacobs, and P. Smith (2007)
  The market for elective surgery: joint estimation of supply and demand.
  Journal of Health Economics 26 (2),  pp. 263–285.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p1.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* K. Moriya and A. Noda (2024)
  Time instability of the fama-french multifactor models: an international evidence.
  Note: [arXiv:2208.01270], Available at https://arxiv.org/abs/2208.01270
  Cited by: [§4](https://arxiv.org/html/2601.21272v1#S4.p2.5 "4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* U. Müller (2014)
  HAC corrections for strongly autocorrelatedtime series.
  Journal of Business & Economic Statistics 32 (3),  pp. 311–322.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* D. Nagakura (2024)
  Cochrane–orcutt type estimator for multivariate linear regression model with serially correlated errors.
  Note: Available at SSRN: https://ssrn.com/abstract=4951695
  Cited by: [§2.2](https://arxiv.org/html/2601.21272v1#S2.SS2.p8.4 "2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.3](https://arxiv.org/html/2601.21272v1#S2.SS3.p8.3 "2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.3](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS3.p1.1 "3.3.3 Wald test based on the FGLS-CO estimator ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3](https://arxiv.org/html/2601.21272v1#S3.SS3.p1.1 "3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. A. Ndako, T. T. Kumeka, F. F. Adedoyin, and A. Asongu (2025)
  Structural breaks in global stock markets: are they caused by pandemics, protests or other factors?.
  Transnational Corporations Review 17.
  Note: 200147
  Cited by: [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p4.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* W. K. Newey and K. D. West (1987)
  A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix.
  Econometrica 55 (3),  pp. 703–708.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2](https://arxiv.org/html/2601.21272v1#S2.p1.1 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.2](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS2.p1.6 "3.3.2 HAR test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* W. K. Newey and K. D. West (1994)
  Automatic lag selection in covariance matrix estimation.
  Review of Economic Studies 61 (4),  pp. 631–653.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2](https://arxiv.org/html/2601.21272v1#S2.p1.1 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* K. Peremans and S. V. Aelst (2018)
  Robust iference for semingly unrelated regression models.
  Journal of Multivariate Analysis 167,  pp. 212–224.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p1.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* P. Perron and E. González-Coya (2022)
  Feasible gls for time series regression.
  Note: Working Paper. Department of Economics, Boston University.
  Cited by: [§2.2](https://arxiv.org/html/2601.21272v1#S2.SS2.p3.2 "2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.2](https://arxiv.org/html/2601.21272v1#S2.SS2.p3.5 "2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.2](https://arxiv.org/html/2601.21272v1#S2.SS2.p9.11 "2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.3](https://arxiv.org/html/2601.21272v1#S2.SS3.p12.4 "2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.3](https://arxiv.org/html/2601.21272v1#S2.SS3.p3.4 "2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.4](https://arxiv.org/html/2601.21272v1#S2.SS4.p1.1 "2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.4](https://arxiv.org/html/2601.21272v1#S2.SS4.p3.2 "2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.2](https://arxiv.org/html/2601.21272v1#S3.SS2.p8.8 "3.2 Estimation Accuracy ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3.4](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS4.p1.4 "3.3.4 Wald test based on the FGLS-D estimator ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.3](https://arxiv.org/html/2601.21272v1#S3.SS3.p1.1 "3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.4.1](https://arxiv.org/html/2601.21272v1#S3.SS4.SSS1.p4.9 "3.4.1 Rejection Frequencies under the Null Hypothesis ‣ 3.4 Simulation Results ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.4.2](https://arxiv.org/html/2601.21272v1#S3.SS4.SSS2.p6.3 "3.4.2 Rejection Frequencies under the Alternative Hypothesis ‣ 3.4 Simulation Results ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [footnote 3](https://arxiv.org/html/2601.21272v1#footnote3 "In Remark 2 (Innovation-based exogeneity and its location): ‣ 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* M. H. Pesaran, T. Schuermann, and S. M. Weiner (2004)
  Modeling regional interdependencies using a global error-correcting macroeconometric model.
  Journal of Business & Economic Statistics 22 (2),  pp. 129–162.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* M. H. Pesaran and T. Yamagata (2008)
  Testing slope homogeneity in large panels.
  Journal of Econometrics 142 (1),  pp. 50–93.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p1.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2](https://arxiv.org/html/2601.21272v1#S2.p1.1 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* M. H. Pesaran (2006)
  Estimation and inference in large heterogeneous panels with a multifactor error structure.
  Econometrica 74 (4),  pp. 863–1159.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p1.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* P. C. B. Phillips, Y. Sun, and S. Jin (2006)
  Spectral density estimation and robust hypothesis testing using steep origin kernels without truncation.
  International Economic Review 47 (3),  pp. 837–894.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* P. C. B. Phillips, Y. Sun, and S. Jin (2007)
  Long run variance estimation and robust regression testing using sharp origin kernels with no truncation.
  Journal of Statistical Planning and Inference 137 (3),  pp. 985–1023.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* S. Ray, N. E. Savin, and A. Tiwari (2009)
  Testing the capm revisited.
  Journal of Empirical Finance 16 (5),  pp. 721–733.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p4.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2](https://arxiv.org/html/2601.21272v1#S2.p1.1 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* S. Ray and N. E. Savin (2008)
  The performance of heteroskedasticity and autocorrelation robust tests: a monte carlo study with an application to the three-factor fama: french asset-pricing model.
  Journal of Applied Econometrics 23 (1),  pp. 91–109.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p4.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2](https://arxiv.org/html/2601.21272v1#S2.p1.1 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* S.A. Ross (1976)
  The arbitrage theory of capital asset pricing.
  Journal of Economic Theory 13 (3),  pp. 341–360.
  Cited by: [§2.1](https://arxiv.org/html/2601.21272v1#S2.SS1.p8.2 "2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§3.1](https://arxiv.org/html/2601.21272v1#S3.SS1.p1.1 "3.1 Simulation Design ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* S.E. Said and D.A. Dickey (1984)
  Testing for unit roots in autoregressive-moving average models of unknown order.
  Biometrika 71 (3),  pp. 599–607.
  Cited by: [§4.2](https://arxiv.org/html/2601.21272v1#S4.SS2.p6.1 "4.2 Dataset ‣ 4 Empirical Application ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* G. Schwarz (1978)
  Estimating the dimension of a model.
  Annals of Statistics 6 (2),  pp. 461–464.
  Cited by: [§2.5](https://arxiv.org/html/2601.21272v1#S2.SS5.p6.2 "2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* W. F. Sharpe (1964)
  Capital asset prices: a theory of market equilibrium under conditions of risk.
  Journal of Finance 19 (3),  pp. 425–442.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p4.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.1](https://arxiv.org/html/2601.21272v1#S2.SS1.p8.2 "2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* C. A. Sims (1980)
  Macroeconomics and reality.
  Econometrica 48 (1),  pp. 1–48.
  Cited by: [§2.1](https://arxiv.org/html/2601.21272v1#S2.SS1.p4.7 "2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. H. Stock and M. W. Watson (2001)
  Vector autoregressions.
  Journal of Economic Perspectives 15 (4),  pp. 101–115.
  Cited by: [§2.1](https://arxiv.org/html/2601.21272v1#S2.SS1.p4.7 "2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* J. H. Stock and M. W. Watson (2019)
  Introduction to econometrics.
  Fourth Edition edition, Pearson.
  Cited by: [§2.2](https://arxiv.org/html/2601.21272v1#S2.SS2.p10.11 "2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.2](https://arxiv.org/html/2601.21272v1#S2.SS2.p2.5 "2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2.3](https://arxiv.org/html/2601.21272v1#S2.SS3.p3.4 "2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* Y. Sun, P. C. B. Phillips, and S. Jin (2008)
  Optimal bandwidth selection in heteroskedasticity-autocorrelation robust testing.
  Econometrica 76 (1),  pp. 175–194.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p3.2 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* Y. Sun (2014)
  Let’s fix it: fixed-b aymptotics versus small-b asymptotics in heteroskedasticity and autocorrelation robust inference.
  Journal of Econometrics 178 (3),  pp. 659–677.
  Cited by: [§3.3.2](https://arxiv.org/html/2601.21272v1#S3.SS3.SSS2.p2.6 "3.3.2 HAR test ‣ 3.3 Size and power of tests ‣ 3 Simulation Experiment ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* A. Zellner (1962)
  An efficient method of estimating seemingly unrelated regressions and tests foraggregation bias.
  Journal of the American Statistical Association 57 (298),  pp. 348–368.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p5.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2](https://arxiv.org/html/2601.21272v1#S2.p1.1 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* D. Zhang, M. Hu, and Q. Ji (2020)
  Financial markets under the global pandemic of covid-19.
  Finance Research Letters 36.
  Note: 101528
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* G. Zhou (1991)
  Small sample tests of portfolio efficiency.
  Journal of Financial Economics 30 (1),  pp. 165–191.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p1.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),
  [§2](https://arxiv.org/html/2601.21272v1#S2.p1.1 "2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").
* G. Zhou (1993)
  Asset-pricing tests under alternative distributions.
  Journal of Finance 48 (5),  pp. 1927–1942.
  Cited by: [§1](https://arxiv.org/html/2601.21272v1#S1.p2.1 "1 Introduction ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").

Table 1: Bias and MSE under the B​DBD condition

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | bias^​(𝜿^T)\widehat{\mathrm{bias}}(\widehat{{\mbox{$\kappa$}}}\_{T}) | | | | |  | MSE^​(𝜿^T)\widehat{\mathrm{MSE}}(\widehat{{\mbox{$\kappa$}}}\_{T}) | | | | |  |
|  |  |  | BC-GD | GD | FGLS-D | FGLS-CO | OLS |  | BC-GD | GD | FGLS-D | FGLS-CO | OLS |  |
| N=5/K=2N=5/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.01170.0117 | 0.01190.0119 | 0.01110.0111 | 0.01100.0110 | 0.01260.0126 |  | 0.20090.2009 | 0.20230.2023 | 0.16580.1658 | 0.16470.1647 | 0.20450.2045 |  |
|  | T=200T=200 |  | 0.00790.0079 | 0.01010.0101 | 0.00950.0095 | 0.00950.0095 | 0.01220.0122 |  | 0.09780.0978 | 0.09670.0967 | 0.07800.0780 | 0.07780.0778 | 0.10100.1010 |  |
|  | T=400T=400 |  | 0.00560.0056 | 0.00510.0051 | 0.00490.0049 | 0.00490.0049 | 0.00520.0052 |  | 0.04640.0464 | 0.04610.0461 | 0.03770.0377 | 0.03770.0377 | 0.04930.0493 |  |
|  | T=800T=800 |  | 0.00380.0038 | 0.00370.0037 | 0.00340.0034 | 0.00340.0034 | 0.00510.0051 |  | 0.02390.0239 | 0.02390.0239 | 0.01920.0192 | 0.01920.0192 | 0.02560.0256 |  |
| N=5/K=4N=5/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.01880.0188 | 0.01680.0168 | 0.01440.0144 | 0.01410.0141 | 0.01570.0157 |  | 0.33830.3383 | 0.33960.3396 | 0.25840.2584 | 0.25710.2571 | 0.34660.3466 |  |
|  | T=200T=200 |  | 0.01180.0118 | 0.01080.0108 | 0.00920.0092 | 0.00910.0091 | 0.01000.0100 |  | 0.15880.1588 | 0.15840.1584 | 0.12180.1218 | 0.12160.1216 | 0.16690.1669 |  |
|  | T=400T=400 |  | 0.00900.0090 | 0.00930.0093 | 0.00780.0078 | 0.00780.0078 | 0.00940.0094 |  | 0.07490.0749 | 0.07500.0750 | 0.05850.0585 | 0.05840.0584 | 0.08200.0820 |  |
|  | T=800T=800 |  | 0.00860.0086 | 0.00750.0075 | 0.00660.0066 | 0.00660.0066 | 0.00790.0079 |  | 0.03800.0380 | 0.03790.0379 | 0.02910.0291 | 0.02910.0291 | 0.04150.0415 |  |
| N=10/K=2N=10/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.01670.0167 | 0.02290.0229 | 0.01730.0173 | 0.01710.0171 | 0.01740.0174 |  | 0.39470.3947 | 0.39060.3906 | 0.31580.3158 | 0.30960.3096 | 0.38390.3839 |  |
|  | T=200T=200 |  | 0.01390.0139 | 0.01460.0146 | 0.01460.0146 | 0.01440.0144 | 0.01460.0146 |  | 0.18180.1818 | 0.18050.1805 | 0.14380.1438 | 0.14330.1433 | 0.18680.1868 |  |
|  | T=400T=400 |  | 0.01010.0101 | 0.00970.0097 | 0.00830.0083 | 0.00830.0083 | 0.00980.0098 |  | 0.08770.0877 | 0.08720.0872 | 0.06980.0698 | 0.06970.0697 | 0.09220.0922 |  |
|  | T=800T=800 |  | 0.00650.0065 | 0.00610.0061 | 0.00510.0051 | 0.00510.0051 | 0.00700.0070 |  | 0.04430.0443 | 0.04400.0440 | 0.03510.0351 | 0.03510.0351 | 0.04670.0467 |  |
| N=10/K=4N=10/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.02110.0211 | 0.02600.0260 | 0.02270.0227 | 0.02270.0227 | 0.02480.0248 |  | 0.70760.7076 | 0.70580.7058 | 0.54010.5401 | 0.52410.5241 | 0.67000.6700 |  |
|  | T=200T=200 |  | 0.01930.0193 | 0.01800.0180 | 0.01660.0166 | 0.01650.0165 | 0.01730.0173 |  | 0.31210.3121 | 0.31080.3108 | 0.23690.2369 | 0.23530.2353 | 0.31970.3197 |  |
|  | T=400T=400 |  | 0.01310.0131 | 0.01320.0132 | 0.01030.0103 | 0.01040.0104 | 0.01200.0120 |  | 0.14970.1497 | 0.14920.1492 | 0.11340.1134 | 0.11320.1132 | 0.15830.1583 |  |
|  | T=800T=800 |  | 0.00700.0070 | 0.00810.0081 | 0.00700.0070 | 0.00700.0070 | 0.00800.0080 |  | 0.07340.0734 | 0.07320.0732 | 0.05590.0559 | 0.05590.0559 | 0.07970.0797 |  |

Note: R version 4.5.2 was used to compute the statistics.

Table 2: Bias and MSE under the G​E​X​O​GGEXOG condition

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | bias^​(𝜿^T)\widehat{\mathrm{bias}}(\widehat{{\mbox{$\kappa$}}}\_{T}) | | | | |  | MSE^​(𝜿^T)\widehat{\mathrm{MSE}}(\widehat{{\mbox{$\kappa$}}}\_{T}) | | | | |  |
|  |  |  | BC-GD | GD | FGLS-D | FGLS-CO | OLS |  | BC-GD | GD | FGLS-D | FGLS-CO | OLS |  |
| N=5/K=2N=5/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.01180.0118 | 0.01160.0116 | 0.00970.0097 | 0.01360.0136 | 0.02250.0225 |  | 0.20160.2016 | 0.20270.2027 | 0.16130.1613 | 0.16140.1614 | 0.24520.2452 |  |
|  | T=200T=200 |  | 0.00810.0081 | 0.01010.0101 | 0.00900.0090 | 0.01200.0120 | 0.02220.0222 |  | 0.09810.0981 | 0.09670.0967 | 0.07660.0766 | 0.07990.0799 | 0.15580.1558 |  |
|  | T=400T=400 |  | 0.00560.0056 | 0.00500.0050 | 0.00470.0047 | 0.00840.0084 | 0.02000.0200 |  | 0.04650.0465 | 0.04610.0461 | 0.03710.0371 | 0.04300.0430 | 0.11540.1154 |  |
|  | T=800T=800 |  | 0.00380.0038 | 0.00380.0038 | 0.00350.0035 | 0.00970.0097 | 0.02270.0227 |  | 0.02390.0239 | 0.02390.0239 | 0.01900.0190 | 0.02530.0253 | 0.09440.0944 |  |
| N=5/K=4N=5/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.01910.0191 | 0.01710.0171 | 0.01380.0138 | 0.01600.0160 | 0.02030.0203 |  | 0.33840.3384 | 0.33990.3399 | 0.25320.2532 | 0.25730.2573 | 0.38600.3860 |  |
|  | T=200T=200 |  | 0.01170.0117 | 0.01090.0109 | 0.00930.0093 | 0.01110.0111 | 0.01780.0178 |  | 0.15880.1588 | 0.15840.1584 | 0.12060.1206 | 0.12740.1274 | 0.22960.2296 |  |
|  | T=400T=400 |  | 0.00900.0090 | 0.00930.0093 | 0.00800.0080 | 0.00910.0091 | 0.01570.0157 |  | 0.07480.0748 | 0.07500.0750 | 0.05770.0577 | 0.06470.0647 | 0.14870.1487 |  |
|  | T=800T=800 |  | 0.00860.0086 | 0.00740.0074 | 0.00630.0063 | 0.00840.0084 | 0.01630.0163 |  | 0.03800.0380 | 0.03790.0379 | 0.02870.0287 | 0.03600.0360 | 0.11370.1137 |  |
| N=10/K=2N=10/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.01610.0161 | 0.02250.0225 | 0.01660.0166 | 0.01740.0174 | 0.01990.0199 |  | 0.39690.3969 | 0.39200.3920 | 0.30630.3063 | 0.29280.2928 | 0.40140.4014 |  |
|  | T=200T=200 |  | 0.01400.0140 | 0.01490.0149 | 0.01410.0141 | 0.01630.0163 | 0.02160.0216 |  | 0.18220.1822 | 0.18090.1809 | 0.14050.1405 | 0.14120.1412 | 0.23350.2335 |  |
|  | T=400T=400 |  | 0.01000.0100 | 0.00970.0097 | 0.00840.0084 | 0.00960.0096 | 0.01610.0161 |  | 0.08760.0876 | 0.08720.0872 | 0.06820.0682 | 0.07260.0726 | 0.15330.1533 |  |
|  | T=800T=800 |  | 0.00650.0065 | 0.00610.0061 | 0.00520.0052 | 0.00750.0075 | 0.01390.0139 |  | 0.04430.0443 | 0.04400.0440 | 0.03440.0344 | 0.04020.0402 | 0.11410.1141 |  |
| N=10/K=4N=10/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.02110.0211 | 0.02500.0250 | 0.02140.0214 | 0.02210.0221 | 0.02540.0254 |  | 0.70940.7094 | 0.70710.7071 | 0.52950.5295 | 0.51000.5100 | 0.68620.6862 |  |
|  | T=200T=200 |  | 0.01910.0191 | 0.01800.0180 | 0.01710.0171 | 0.01710.0171 | 0.02010.0201 |  | 0.31240.3124 | 0.31110.3111 | 0.23340.2334 | 0.23440.2344 | 0.36840.3684 |  |
|  | T=400T=400 |  | 0.01320.0132 | 0.01330.0133 | 0.00980.0098 | 0.01040.0104 | 0.01440.0144 |  | 0.14970.1497 | 0.14930.1493 | 0.11180.1118 | 0.11680.1168 | 0.22050.2205 |  |
|  | T=800T=800 |  | 0.00700.0070 | 0.00820.0082 | 0.00720.0072 | 0.00760.0076 | 0.01140.0114 |  | 0.07340.0734 | 0.07320.0732 | 0.05510.0551 | 0.06160.0616 | 0.15050.1505 |  |

Note: As for Table [1](https://arxiv.org/html/2601.21272v1#Sx1.T1 "Table 1 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").

Table 3: Bias and MSE under the E​B​DEBD condition

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | bias^​(𝜿^T)\widehat{\mathrm{bias}}(\widehat{{\mbox{$\kappa$}}}\_{T}) | | | | |  | MSE^​(𝜿^T)\widehat{\mathrm{MSE}}(\widehat{{\mbox{$\kappa$}}}\_{T}) | | | | |  |
|  |  |  | BC-GD | GD | FGLS-D | FGLS-CO | OLS |  | BC-GD | GD | FGLS-D | FGLS-CO | OLS |  |
| N=5/K=2N=5/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.01280.0128 | 0.01270.0127 | 0.01880.0188 | 0.04360.0436 | 0.05670.0567 |  | 0.22840.2284 | 0.22960.2296 | 0.21500.2150 | 0.24380.2438 | 0.32090.3209 |  |
|  | T=200T=200 |  | 0.00900.0090 | 0.01040.0104 | 0.01680.0168 | 0.04050.0405 | 0.05580.0558 |  | 0.11330.1133 | 0.11160.1116 | 0.11880.1188 | 0.15190.1519 | 0.22660.2266 |  |
|  | T=400T=400 |  | 0.00600.0060 | 0.00520.0052 | 0.01500.0150 | 0.03880.0388 | 0.05600.0560 |  | 0.05350.0535 | 0.05270.0527 | 0.07350.0735 | 0.11170.1117 | 0.18520.1852 |  |
|  | T=800T=800 |  | 0.00380.0038 | 0.00390.0039 | 0.01720.0172 | 0.04020.0402 | 0.05840.0584 |  | 0.02810.0281 | 0.02780.0278 | 0.05220.0522 | 0.09150.0915 | 0.16320.1632 |  |
| N=5/K=4N=5/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.01940.0194 | 0.01730.0173 | 0.01570.0157 | 0.02620.0262 | 0.03320.0332 |  | 0.35270.3527 | 0.35360.3536 | 0.30200.3020 | 0.33320.3332 | 0.46520.4652 |  |
|  | T=200T=200 |  | 0.01260.0126 | 0.01130.0113 | 0.01260.0126 | 0.02300.0230 | 0.03230.0323 |  | 0.16680.1668 | 0.16610.1661 | 0.16090.1609 | 0.19490.1949 | 0.30680.3068 |  |
|  | T=400T=400 |  | 0.00920.0092 | 0.00940.0094 | 0.00900.0090 | 0.01890.0189 | 0.02950.0295 |  | 0.07840.0784 | 0.07830.0783 | 0.09160.0916 | 0.12400.1240 | 0.22070.2207 |  |
|  | T=800T=800 |  | 0.00910.0091 | 0.00760.0076 | 0.00850.0085 | 0.02000.0200 | 0.03080.0308 |  | 0.04010.0401 | 0.04000.0400 | 0.05980.0598 | 0.09280.0928 | 0.18520.1852 |  |
| N=10/K=2N=10/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.01670.0167 | 0.02270.0227 | 0.02440.0244 | 0.03650.0365 | 0.03960.0396 |  | 0.41380.4138 | 0.40820.4082 | 0.34850.3485 | 0.36500.3650 | 0.45510.4551 |  |
|  | T=200T=200 |  | 0.01420.0142 | 0.01500.0150 | 0.02390.0239 | 0.03660.0366 | 0.04120.0412 |  | 0.19000.1900 | 0.18900.1890 | 0.17630.1763 | 0.20460.2046 | 0.28720.2872 |  |
|  | T=400T=400 |  | 0.01020.0102 | 0.01010.0101 | 0.01660.0166 | 0.03020.0302 | 0.03820.0382 |  | 0.09120.0912 | 0.09080.0908 | 0.10170.1017 | 0.13410.1341 | 0.20730.2073 |  |
|  | T=800T=800 |  | 0.00660.0066 | 0.00600.0060 | 0.01600.0160 | 0.02990.0299 | 0.03720.0372 |  | 0.04650.0465 | 0.04620.0462 | 0.06660.0666 | 0.10050.1005 | 0.16900.1690 |  |
| N=10/K=4N=10/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.02150.0215 | 0.02500.0250 | 0.02310.0231 | 0.02550.0255 | 0.02790.0279 |  | 0.72400.7240 | 0.72100.7210 | 0.57970.5797 | 0.58210.5821 | 0.75010.7501 |  |
|  | T=200T=200 |  | 0.01950.0195 | 0.01860.0186 | 0.01830.0183 | 0.02040.0204 | 0.02430.0243 |  | 0.31920.3192 | 0.31690.3169 | 0.27170.2717 | 0.29310.2931 | 0.42600.4260 |  |
|  | T=400T=400 |  | 0.01330.0133 | 0.01320.0132 | 0.01110.0111 | 0.01470.0147 | 0.02000.0200 |  | 0.15290.1529 | 0.15250.1525 | 0.14590.1459 | 0.17020.1702 | 0.27670.2767 |  |
|  | T=800T=800 |  | 0.00710.0071 | 0.00820.0082 | 0.01070.0107 | 0.01390.0139 | 0.01810.0181 |  | 0.07490.0749 | 0.07480.0748 | 0.08700.0870 | 0.11280.1128 | 0.20620.2062 |  |

Note: As for Table [1](https://arxiv.org/html/2601.21272v1#Sx1.T1 "Table 1 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").

Table 4: Rejection rates (percentages) under the null hypothesis H0:𝜶=𝟎N,1H\_{0}:\mbox{{$\alpha$}}=\mathbf{0}\_{N,1} when the B​DBD holds

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 𝒲B​C​-​G​D\mathcal{W}^{BC\text{-}GD} | | |  | 𝒲G​D\mathcal{W}^{GD} | | |  | 𝒲F​G​L​S​-​D\mathcal{W}^{FGLS\text{-}D} | | |  | 𝒲F​G​L​S−C​O\mathcal{W}^{FGLS-CO} | | |  | H​A​RHAR | | |  | G​R​SGRS | | |  |
|  |  |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  |
| N=5/K=2N=5/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.11600.1160 | 0.06700.0670 | 0.01000.0100 |  | 0.24300.2430 | 0.18000.1800 | 0.07600.0760 |  | 0.21100.2110 | 0.15000.1500 | 0.06000.0600 |  | 0.19300.1930 | 0.13800.1380 | 0.05600.0560 |  | 0.11700.1170 | 0.04800.0480 | 0.01800.0180 |  | 0.14100.1410 | 0.10300.1030 | 0.04400.0440 |  |
|  | T=200T=200 |  | 0.12600.1260 | 0.06500.0650 | 0.01700.0170 |  | 0.21000.2100 | 0.13400.1340 | 0.03800.0380 |  | 0.17700.1770 | 0.10600.1060 | 0.03400.0340 |  | 0.16700.1670 | 0.09900.0990 | 0.03100.0310 |  | 0.11600.1160 | 0.06100.0610 | 0.01300.0130 |  | 0.14400.1440 | 0.09200.0920 | 0.03300.0330 |  |
|  | T=400T=400 |  | 0.11400.1140 | 0.06900.0690 | 0.02300.0230 |  | 0.14600.1460 | 0.10000.1000 | 0.03300.0330 |  | 0.12100.1210 | 0.07800.0780 | 0.02500.0250 |  | 0.11900.1190 | 0.07700.0770 | 0.02300.0230 |  | 0.10300.1030 | 0.06300.0630 | 0.02000.0200 |  | 0.11700.1170 | 0.08200.0820 | 0.03100.0310 |  |
|  | T=800T=800 |  | 0.11400.1140 | 0.06200.0620 | 0.01900.0190 |  | 0.15000.1500 | 0.08200.0820 | 0.02500.0250 |  | 0.12500.1250 | 0.06900.0690 | 0.01600.0160 |  | 0.12300.1230 | 0.06900.0690 | 0.01500.0150 |  | 0.11600.1160 | 0.06600.0660 | 0.01800.0180 |  | 0.13400.1340 | 0.10200.1020 | 0.04300.0430 |  |
| N=5/K=4N=5/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.10100.1010 | 0.06300.0630 | 0.01300.0130 |  | 0.27900.2790 | 0.19700.1970 | 0.08400.0840 |  | 0.23600.2360 | 0.15900.1590 | 0.04800.0480 |  | 0.19400.1940 | 0.12600.1260 | 0.04000.0400 |  | 0.10000.1000 | 0.05600.0560 | 0.01200.0120 |  | 0.11600.1160 | 0.07600.0760 | 0.02800.0280 |  |
|  | T=200T=200 |  | 0.10300.1030 | 0.05100.0510 | 0.01100.0110 |  | 0.19600.1960 | 0.11600.1160 | 0.04000.0400 |  | 0.15800.1580 | 0.09500.0950 | 0.03100.0310 |  | 0.14700.1470 | 0.08200.0820 | 0.02700.0270 |  | 0.09100.0910 | 0.04900.0490 | 0.01100.0110 |  | 0.11700.1170 | 0.07200.0720 | 0.02800.0280 |  |
|  | T=400T=400 |  | 0.09000.0900 | 0.05000.0500 | 0.00800.0080 |  | 0.14700.1470 | 0.08300.0830 | 0.02200.0220 |  | 0.11100.1110 | 0.06000.0600 | 0.01500.0150 |  | 0.10500.1050 | 0.05700.0570 | 0.01300.0130 |  | 0.08300.0830 | 0.04700.0470 | 0.00500.0050 |  | 0.09200.0920 | 0.05400.0540 | 0.02400.0240 |  |
|  | T=800T=800 |  | 0.10200.1020 | 0.05800.0580 | 0.01300.0130 |  | 0.17300.1730 | 0.08700.0870 | 0.02700.0270 |  | 0.11900.1190 | 0.06800.0680 | 0.02100.0210 |  | 0.11500.1150 | 0.06700.0670 | 0.01800.0180 |  | 0.10500.1050 | 0.05200.0520 | 0.01900.0190 |  | 0.12800.1280 | 0.07400.0740 | 0.03100.0310 |  |
| N=10/K=2N=10/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.09500.0950 | 0.04800.0480 | 0.00800.0080 |  | 0.42200.4220 | 0.31200.3120 | 0.16200.1620 |  | 0.34900.3490 | 0.25600.2560 | 0.12400.1240 |  | 0.32100.3210 | 0.22800.2280 | 0.09500.0950 |  | 0.06800.0680 | 0.03300.0330 | 0.00800.0080 |  | 0.07100.0710 | 0.04200.0420 | 0.01200.0120 |  |
|  | T=200T=200 |  | 0.11800.1180 | 0.06300.0630 | 0.01600.0160 |  | 0.26100.2610 | 0.17300.1730 | 0.07200.0720 |  | 0.20700.2070 | 0.13200.1320 | 0.03900.0390 |  | 0.19700.1970 | 0.12500.1250 | 0.03800.0380 |  | 0.06700.0670 | 0.03300.0330 | 0.00900.0090 |  | 0.07700.0770 | 0.04800.0480 | 0.01600.0160 |  |
|  | T=400T=400 |  | 0.10300.1030 | 0.05100.0510 | 0.01400.0140 |  | 0.18900.1890 | 0.11000.1100 | 0.03500.0350 |  | 0.14300.1430 | 0.08900.0890 | 0.02200.0220 |  | 0.13700.1370 | 0.08600.0860 | 0.01900.0190 |  | 0.08700.0870 | 0.04500.0450 | 0.01100.0110 |  | 0.06100.0610 | 0.04000.0400 | 0.01300.0130 |  |
|  | T=800T=800 |  | 0.11900.1190 | 0.06200.0620 | 0.01400.0140 |  | 0.18300.1830 | 0.10300.1030 | 0.03500.0350 |  | 0.13600.1360 | 0.07500.0750 | 0.02900.0290 |  | 0.13500.1350 | 0.07500.0750 | 0.02800.0280 |  | 0.11000.1100 | 0.05200.0520 | 0.01200.0120 |  | 0.09100.0910 | 0.05700.0570 | 0.01800.0180 |  |
| N=10/K=4N=10/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.10800.1080 | 0.05600.0560 | 0.00800.0080 |  | 0.52700.5270 | 0.42900.4290 | 0.27200.2720 |  | 0.44900.4490 | 0.34600.3460 | 0.18600.1860 |  | 0.36700.3670 | 0.26200.2620 | 0.12300.1230 |  | 0.09600.0960 | 0.05100.0510 | 0.01000.0100 |  | 0.06300.0630 | 0.03800.0380 | 0.01100.0110 |  |
|  | T=200T=200 |  | 0.09600.0960 | 0.04900.0490 | 0.01200.0120 |  | 0.30100.3010 | 0.20300.2030 | 0.08700.0870 |  | 0.23600.2360 | 0.16100.1610 | 0.05600.0560 |  | 0.20800.2080 | 0.13100.1310 | 0.04200.0420 |  | 0.08000.0800 | 0.04200.0420 | 0.00800.0080 |  | 0.07300.0730 | 0.04100.0410 | 0.01400.0140 |  |
|  | T=400T=400 |  | 0.11000.1100 | 0.06100.0610 | 0.01100.0110 |  | 0.22600.2260 | 0.14400.1440 | 0.04900.0490 |  | 0.15200.1520 | 0.09000.0900 | 0.02500.0250 |  | 0.14700.1470 | 0.07900.0790 | 0.02400.0240 |  | 0.10100.1010 | 0.05600.0560 | 0.01800.0180 |  | 0.07900.0790 | 0.04000.0400 | 0.01200.0120 |  |
|  | T=800T=800 |  | 0.08800.0880 | 0.04900.0490 | 0.00600.0060 |  | 0.17700.1770 | 0.10400.1040 | 0.03300.0330 |  | 0.11800.1180 | 0.06600.0660 | 0.01900.0190 |  | 0.11600.1160 | 0.06500.0650 | 0.01800.0180 |  | 0.09400.0940 | 0.04700.0470 | 0.01600.0160 |  | 0.07800.0780 | 0.04200.0420 | 0.01500.0150 |  |

Note: R version 4.5.2 was used to compute the statistics..

Table 5: Rejection rates (percentages) under the null hypothesis H0:𝜶=𝟎N,1H\_{0}:\mbox{{$\alpha$}}=\mathbf{0}\_{N,1} when the G​E​X​O​GGEXOG holds

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 𝒲B​C​-​G​D\mathcal{W}^{BC\text{-}GD} | | |  | 𝒲G​D\mathcal{W}^{GD} | | |  | 𝒲F​G​L​S​-​D\mathcal{W}^{FGLS\text{-}D} | | |  | 𝒲F​G​L​S−C​O\mathcal{W}^{FGLS-CO} | | |  | H​A​RHAR | | |  | G​R​SGRS | | |  |
|  |  |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  |
| N=5/K=2N=5/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.11700.1170 | 0.07100.0710 | 0.00800.0080 |  | 0.25900.2590 | 0.20100.2010 | 0.09200.0920 |  | 0.24200.2420 | 0.16800.1680 | 0.06400.0640 |  | 0.20700.2070 | 0.14400.1440 | 0.05600.0560 |  | 0.12600.1260 | 0.06200.0620 | 0.02300.0230 |  | 0.15400.1540 | 0.11000.1100 | 0.05000.0500 |  |
|  | T=200T=200 |  | 0.13000.1300 | 0.06400.0640 | 0.01600.0160 |  | 0.21400.2140 | 0.14600.1460 | 0.04700.0470 |  | 0.18900.1890 | 0.11600.1160 | 0.04300.0430 |  | 0.18200.1820 | 0.11400.1140 | 0.03300.0330 |  | 0.17900.1790 | 0.11500.1150 | 0.02700.0270 |  | 0.19100.1910 | 0.11900.1190 | 0.05400.0540 |  |
|  | T=400T=400 |  | 0.10900.1090 | 0.06800.0680 | 0.02100.0210 |  | 0.15600.1560 | 0.10300.1030 | 0.04200.0420 |  | 0.13200.1320 | 0.08700.0870 | 0.02700.0270 |  | 0.13600.1360 | 0.08800.0880 | 0.03400.0340 |  | 0.25000.2500 | 0.17400.1740 | 0.07300.0730 |  | 0.21900.2190 | 0.14400.1440 | 0.05800.0580 |  |
|  | T=800T=800 |  | 0.11300.1130 | 0.06000.0600 | 0.01700.0170 |  | 0.16900.1690 | 0.08900.0890 | 0.03000.0300 |  | 0.13600.1360 | 0.08100.0810 | 0.02000.0200 |  | 0.18400.1840 | 0.10300.1030 | 0.03000.0300 |  | 0.43700.4370 | 0.34100.3410 | 0.19800.1980 |  | 0.35400.3540 | 0.27200.2720 | 0.15300.1530 |  |
| N=5/K=4N=5/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.10400.1040 | 0.05500.0550 | 0.01200.0120 |  | 0.28800.2880 | 0.21600.2160 | 0.09100.0910 |  | 0.24300.2430 | 0.16600.1660 | 0.05700.0570 |  | 0.19800.1980 | 0.12400.1240 | 0.04300.0430 |  | 0.13800.1380 | 0.06200.0620 | 0.02200.0220 |  | 0.13200.1320 | 0.08100.0810 | 0.03300.0330 |  |
|  | T=200T=200 |  | 0.10300.1030 | 0.04800.0480 | 0.01100.0110 |  | 0.20900.2090 | 0.12700.1270 | 0.04700.0470 |  | 0.17800.1780 | 0.09200.0920 | 0.03600.0360 |  | 0.15500.1550 | 0.08800.0880 | 0.03100.0310 |  | 0.16200.1620 | 0.09200.0920 | 0.03500.0350 |  | 0.17000.1700 | 0.10700.1070 | 0.04600.0460 |  |
|  | T=400T=400 |  | 0.09200.0920 | 0.05400.0540 | 0.01000.0100 |  | 0.15900.1590 | 0.09400.0940 | 0.03000.0300 |  | 0.12000.1200 | 0.07200.0720 | 0.01700.0170 |  | 0.12500.1250 | 0.06800.0680 | 0.02100.0210 |  | 0.23700.2370 | 0.14300.1430 | 0.05000.0500 |  | 0.18900.1890 | 0.13400.1340 | 0.05700.0570 |  |
|  | T=800T=800 |  | 0.10000.1000 | 0.05400.0540 | 0.01100.0110 |  | 0.17700.1770 | 0.09800.0980 | 0.03100.0310 |  | 0.12600.1260 | 0.07800.0780 | 0.02300.0230 |  | 0.15400.1540 | 0.09000.0900 | 0.02800.0280 |  | 0.37400.3740 | 0.30200.3020 | 0.15600.1560 |  | 0.34000.3400 | 0.26300.2630 | 0.13200.1320 |  |
| N=10/K=2N=10/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.09800.0980 | 0.04800.0480 | 0.00700.0070 |  | 0.44200.4420 | 0.35400.3540 | 0.19000.1900 |  | 0.37900.3790 | 0.28100.2810 | 0.14000.1400 |  | 0.31200.3120 | 0.23300.2330 | 0.10500.1050 |  | 0.07700.0770 | 0.03300.0330 | 0.00500.0050 |  | 0.08700.0870 | 0.04700.0470 | 0.01400.0140 |  |
|  | T=200T=200 |  | 0.12400.1240 | 0.05800.0580 | 0.01300.0130 |  | 0.28100.2810 | 0.19200.1920 | 0.09000.0900 |  | 0.23600.2360 | 0.16200.1620 | 0.05500.0550 |  | 0.20600.2060 | 0.12800.1280 | 0.04400.0440 |  | 0.11600.1160 | 0.05900.0590 | 0.01000.0100 |  | 0.10800.1080 | 0.05800.0580 | 0.02200.0220 |  |
|  | T=400T=400 |  | 0.10200.1020 | 0.05200.0520 | 0.01400.0140 |  | 0.20800.2080 | 0.12800.1280 | 0.04100.0410 |  | 0.16100.1610 | 0.09800.0980 | 0.03000.0300 |  | 0.15300.1530 | 0.09000.0900 | 0.03300.0330 |  | 0.20200.2020 | 0.12900.1290 | 0.03600.0360 |  | 0.13600.1360 | 0.08900.0890 | 0.03700.0370 |  |
|  | T=800T=800 |  | 0.12000.1200 | 0.06300.0630 | 0.01500.0150 |  | 0.20200.2020 | 0.11700.1170 | 0.04300.0430 |  | 0.15200.1520 | 0.08400.0840 | 0.03200.0320 |  | 0.16500.1650 | 0.10300.1030 | 0.03300.0330 |  | 0.36300.3630 | 0.26000.2600 | 0.12000.1200 |  | 0.25800.2580 | 0.16700.1670 | 0.06800.0680 |  |
| N=10/K=4N=10/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.10700.1070 | 0.05500.0550 | 0.01200.0120 |  | 0.56000.5600 | 0.45600.4560 | 0.29600.2960 |  | 0.46500.4650 | 0.36400.3640 | 0.21400.2140 |  | 0.36100.3610 | 0.27700.2770 | 0.13200.1320 |  | 0.11600.1160 | 0.05600.0560 | 0.01000.0100 |  | 0.09600.0960 | 0.04500.0450 | 0.01600.0160 |  |
|  | T=200T=200 |  | 0.08700.0870 | 0.04600.0460 | 0.01300.0130 |  | 0.32600.3260 | 0.22200.2220 | 0.09800.0980 |  | 0.25000.2500 | 0.15800.1580 | 0.06200.0620 |  | 0.20500.2050 | 0.13700.1370 | 0.04300.0430 |  | 0.11200.1120 | 0.05800.0580 | 0.00900.0090 |  | 0.09600.0960 | 0.05300.0530 | 0.02100.0210 |  |
|  | T=400T=400 |  | 0.11100.1110 | 0.06100.0610 | 0.01200.0120 |  | 0.24600.2460 | 0.15900.1590 | 0.05900.0590 |  | 0.17400.1740 | 0.10400.1040 | 0.02900.0290 |  | 0.17100.1710 | 0.09500.0950 | 0.03300.0330 |  | 0.20800.2080 | 0.12900.1290 | 0.03100.0310 |  | 0.14800.1480 | 0.08000.0800 | 0.02800.0280 |  |
|  | T=800T=800 |  | 0.09500.0950 | 0.04700.0470 | 0.00700.0070 |  | 0.20200.2020 | 0.12100.1210 | 0.04000.0400 |  | 0.13200.1320 | 0.07700.0770 | 0.02100.0210 |  | 0.15100.1510 | 0.08600.0860 | 0.02200.0220 |  | 0.31800.3180 | 0.22200.2220 | 0.11200.1120 |  | 0.21800.2180 | 0.14700.1470 | 0.05300.0530 |  |

Note: As for Table [4](https://arxiv.org/html/2601.21272v1#Sx1.T4 "Table 4 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").

Table 6: Rejection rates (percentages) under the null hypothesis H0:𝜶=𝟎N,1H\_{0}:\mbox{{$\alpha$}}=\mathbf{0}\_{N,1} when the E​B​DEBD holds

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 𝒲B​C​-​G​D\mathcal{W}^{BC\text{-}GD} | | |  | 𝒲G​D\mathcal{W}^{GD} | | |  | 𝒲F​G​L​S​-​D\mathcal{W}^{FGLS\text{-}D} | | |  | 𝒲F​G​L​S−C​O\mathcal{W}^{FGLS-CO} | | |  | H​A​RHAR | | |  | G​R​SGRS | | |  |
|  |  |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  |
| N=5/K=2N=5/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.12300.1230 | 0.06500.0650 | 0.00700.0070 |  | 0.33800.3380 | 0.26100.2610 | 0.15300.1530 |  | 0.31600.3160 | 0.23100.2310 | 0.12000.1200 |  | 0.27900.2790 | 0.19400.1940 | 0.08900.0890 |  | 0.15300.1530 | 0.08400.0840 | 0.03300.0330 |  | 0.19500.1950 | 0.14100.1410 | 0.08100.0810 |  |
|  | T=200T=200 |  | 0.13200.1320 | 0.06500.0650 | 0.00900.0090 |  | 0.31300.3130 | 0.21600.2160 | 0.10400.1040 |  | 0.30600.3060 | 0.22400.2240 | 0.09500.0950 |  | 0.28800.2880 | 0.21700.2170 | 0.09500.0950 |  | 0.24700.2470 | 0.16100.1610 | 0.05200.0520 |  | 0.26200.2620 | 0.19200.1920 | 0.09700.0970 |  |
|  | T=400T=400 |  | 0.11600.1160 | 0.07400.0740 | 0.02400.0240 |  | 0.24700.2470 | 0.17300.1730 | 0.08000.0800 |  | 0.31300.3130 | 0.21900.2190 | 0.08800.0880 |  | 0.34300.3430 | 0.25800.2580 | 0.11100.1110 |  | 0.35700.3570 | 0.26400.2640 | 0.11900.1190 |  | 0.35400.3540 | 0.25800.2580 | 0.13100.1310 |  |
|  | T=800T=800 |  | 0.12100.1210 | 0.06800.0680 | 0.02000.0200 |  | 0.25000.2500 | 0.16300.1630 | 0.06900.0690 |  | 0.36800.3680 | 0.26600.2660 | 0.13800.1380 |  | 0.44600.4460 | 0.35800.3580 | 0.20400.2040 |  | 0.54200.5420 | 0.44600.4460 | 0.28900.2890 |  | 0.49000.4900 | 0.41000.4100 | 0.28500.2850 |  |
| N=5/K=4N=5/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.09100.0910 | 0.05800.0580 | 0.01000.0100 |  | 0.34200.3420 | 0.24800.2480 | 0.12700.1270 |  | 0.31200.3120 | 0.21700.2170 | 0.10800.1080 |  | 0.24500.2450 | 0.16800.1680 | 0.07200.0720 |  | 0.16100.1610 | 0.08400.0840 | 0.03200.0320 |  | 0.18000.1800 | 0.11600.1160 | 0.05000.0500 |  |
|  | T=200T=200 |  | 0.09000.0900 | 0.05100.0510 | 0.01500.0150 |  | 0.27800.2780 | 0.17900.1790 | 0.06700.0670 |  | 0.26100.2610 | 0.17300.1730 | 0.06300.0630 |  | 0.24500.2450 | 0.15800.1580 | 0.06200.0620 |  | 0.21100.2110 | 0.13300.1330 | 0.04500.0450 |  | 0.22700.2270 | 0.15500.1550 | 0.08000.0800 |  |
|  | T=400T=400 |  | 0.08700.0870 | 0.04300.0430 | 0.00500.0050 |  | 0.21000.2100 | 0.13000.1300 | 0.05000.0500 |  | 0.26500.2650 | 0.17600.1760 | 0.07000.0700 |  | 0.26600.2660 | 0.16500.1650 | 0.07900.0790 |  | 0.29800.2980 | 0.21500.2150 | 0.09900.0990 |  | 0.28800.2880 | 0.21000.2100 | 0.10300.1030 |  |
|  | T=800T=800 |  | 0.11200.1120 | 0.06100.0610 | 0.01500.0150 |  | 0.22500.2250 | 0.14900.1490 | 0.06000.0600 |  | 0.34900.3490 | 0.25100.2510 | 0.11500.1150 |  | 0.39000.3900 | 0.30300.3030 | 0.15700.1570 |  | 0.47300.4730 | 0.38600.3860 | 0.26900.2690 |  | 0.47100.4710 | 0.39100.3910 | 0.25500.2550 |  |
| N=10/K=2N=10/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.09800.0980 | 0.04900.0490 | 0.01100.0110 |  | 0.49400.4940 | 0.40600.4060 | 0.23900.2390 |  | 0.44400.4440 | 0.34400.3440 | 0.17700.1770 |  | 0.37000.3700 | 0.28400.2840 | 0.13300.1330 |  | 0.08700.0870 | 0.04400.0440 | 0.00800.0080 |  | 0.09700.0970 | 0.06300.0630 | 0.02000.0200 |  |
|  | T=200T=200 |  | 0.11600.1160 | 0.06000.0600 | 0.00900.0090 |  | 0.34300.3430 | 0.24200.2420 | 0.12400.1240 |  | 0.30600.3060 | 0.21800.2180 | 0.08300.0830 |  | 0.28100.2810 | 0.19100.1910 | 0.07400.0740 |  | 0.13500.1350 | 0.06700.0670 | 0.01100.0110 |  | 0.14100.1410 | 0.08600.0860 | 0.03200.0320 |  |
|  | T=400T=400 |  | 0.09400.0940 | 0.05500.0550 | 0.01400.0140 |  | 0.25600.2560 | 0.17900.1790 | 0.06400.0640 |  | 0.27500.2750 | 0.19000.1900 | 0.07600.0760 |  | 0.29400.2940 | 0.18600.1860 | 0.08200.0820 |  | 0.27100.2710 | 0.18000.1800 | 0.06400.0640 |  | 0.20400.2040 | 0.13900.1390 | 0.06500.0650 |  |
|  | T=800T=800 |  | 0.11200.1120 | 0.06300.0630 | 0.00900.0090 |  | 0.27400.2740 | 0.17200.1720 | 0.07700.0770 |  | 0.31900.3190 | 0.21400.2140 | 0.10200.1020 |  | 0.39900.3990 | 0.28800.2880 | 0.14700.1470 |  | 0.49400.4940 | 0.36700.3670 | 0.20900.2090 |  | 0.39800.3980 | 0.28800.2880 | 0.15800.1580 |  |
| N=10/K=4N=10/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.10700.1070 | 0.05700.0570 | 0.00700.0070 |  | 0.59800.5980 | 0.48800.4880 | 0.31800.3180 |  | 0.51300.5130 | 0.41000.4100 | 0.24400.2440 |  | 0.40900.4090 | 0.31500.3150 | 0.16400.1640 |  | 0.12300.1230 | 0.05500.0550 | 0.01200.0120 |  | 0.11800.1180 | 0.05900.0590 | 0.02000.0200 |  |
|  | T=200T=200 |  | 0.09400.0940 | 0.05200.0520 | 0.01200.0120 |  | 0.35900.3590 | 0.25800.2580 | 0.11900.1190 |  | 0.31800.3180 | 0.22000.2200 | 0.09500.0950 |  | 0.27900.2790 | 0.18100.1810 | 0.07900.0790 |  | 0.13500.1350 | 0.07200.0720 | 0.02000.0200 |  | 0.12100.1210 | 0.07500.0750 | 0.03300.0330 |  |
|  | T=400T=400 |  | 0.10900.1090 | 0.06100.0610 | 0.01200.0120 |  | 0.28200.2820 | 0.19300.1930 | 0.07400.0740 |  | 0.26500.2650 | 0.18700.1870 | 0.06700.0670 |  | 0.27400.2740 | 0.17800.1780 | 0.07600.0760 |  | 0.25600.2560 | 0.19300.1930 | 0.05500.0550 |  | 0.21700.2170 | 0.13500.1350 | 0.05700.0570 |  |
|  | T=800T=800 |  | 0.10100.1010 | 0.05100.0510 | 0.00500.0050 |  | 0.24500.2450 | 0.14300.1430 | 0.06200.0620 |  | 0.28600.2860 | 0.19800.1980 | 0.09200.0920 |  | 0.30400.3040 | 0.22300.2230 | 0.09400.0940 |  | 0.40100.4010 | 0.30200.3020 | 0.16600.1660 |  | 0.32200.3220 | 0.23600.2360 | 0.12000.1200 |  |

Note: As for Table [4](https://arxiv.org/html/2601.21272v1#Sx1.T4 "Table 4 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").

Table 7: Rejection rates (percentages) under the alternative hypothesis H1:α1=0.2H\_{1}:\alpha\_{1}=0.2 and αj=0\alpha\_{j}=0 (j=2,…,Nj=2,\ldots,N) when the B​DBD holds

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 𝒲B​C​-​G​D\mathcal{W}^{BC\text{-}GD} | | |  | 𝒲G​D\mathcal{W}^{GD} | | |  | 𝒲F​G​L​S​-​D\mathcal{W}^{FGLS\text{-}D} | | |  | 𝒲F​G​L​S−C​O\mathcal{W}^{FGLS-CO} | | |  | H​A​RHAR | | |  | G​R​SGRS | | |  |
|  |  |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  |
| N=5/K=2N=5/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.41000.4100 | 0.27000.2700 | 0.12500.1250 |  | 0.40800.4080 | 0.28000.2800 | 0.10100.1010 |  | 0.41400.4140 | 0.28200.2820 | 0.09100.0910 |  | 0.40900.4090 | 0.27700.2770 | 0.08600.0860 |  | 0.34800.3480 | 0.23900.2390 | 0.05800.0580 |  | 0.17600.1760 | 0.09200.0920 | 0.03200.0320 |  |
|  | T=200T=200 |  | 0.68900.6890 | 0.57200.5720 | 0.31800.3180 |  | 0.69200.6920 | 0.62100.6210 | 0.38400.3840 |  | 0.72900.7290 | 0.59300.5930 | 0.43200.4320 |  | 0.72400.7240 | 0.59300.5930 | 0.44500.4450 |  | 0.62100.6210 | 0.48500.4850 | 0.26500.2650 |  | 0.37600.3760 | 0.23600.2360 | 0.07000.0700 |  |
|  | T=400T=400 |  | 0.96000.9600 | 0.91200.9120 | 0.69400.6940 |  | 0.96500.9650 | 0.92300.9230 | 0.80000.8000 |  | 0.97400.9740 | 0.93800.9380 | 0.78800.7880 |  | 0.97300.9730 | 0.93700.9370 | 0.78700.7870 |  | 0.94600.9460 | 0.88800.8880 | 0.63300.6330 |  | 0.79500.7950 | 0.55100.5510 | 0.10600.1060 |  |
|  | T=800T=800 |  | 0.99900.9990 | 0.99800.9980 | 0.88600.8860 |  | 0.99900.9990 | 0.99900.9990 | 0.99500.9950 |  | 0.99900.9990 | 0.99900.9990 | 0.99800.9980 |  | 0.99900.9990 | 0.99900.9990 | 0.99800.9980 |  | 0.99900.9990 | 0.99700.9970 | 0.99100.9910 |  | 0.98500.9850 | 0.93700.9370 | 0.50500.5050 |  |
| N=5/K=4N=5/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.36100.3610 | 0.20800.2080 | 0.09100.0910 |  | 0.35700.3570 | 0.23200.2320 | 0.08600.0860 |  | 0.37900.3790 | 0.28600.2860 | 0.09100.0910 |  | 0.38100.3810 | 0.28800.2880 | 0.10300.1030 |  | 0.32700.3270 | 0.20100.2010 | 0.06200.0620 |  | 0.23800.2380 | 0.11900.1190 | 0.02400.0240 |  |
|  | T=200T=200 |  | 0.66600.6660 | 0.55900.5590 | 0.30400.3040 |  | 0.70200.7020 | 0.56200.5620 | 0.24500.2450 |  | 0.73400.7340 | 0.60000.6000 | 0.23400.2340 |  | 0.73600.7360 | 0.60500.6050 | 0.22000.2200 |  | 0.60400.6040 | 0.45600.4560 | 0.20400.2040 |  | 0.41300.4130 | 0.25900.2590 | 0.04000.0400 |  |
|  | T=400T=400 |  | 0.92300.9230 | 0.85800.8580 | 0.70300.7030 |  | 0.93900.9390 | 0.88100.8810 | 0.73900.7390 |  | 0.95600.9560 | 0.92100.9210 | 0.77800.7780 |  | 0.95600.9560 | 0.91900.9190 | 0.77000.7700 |  | 0.90700.9070 | 0.83100.8310 | 0.65700.6570 |  | 0.79900.7990 | 0.62000.6200 | 0.13400.1340 |  |
|  | T=800T=800 |  | 1.00001.0000 | 0.99100.9910 | 0.96400.9640 |  | 1.00001.0000 | 0.99500.9950 | 0.97200.9720 |  | 1.00001.0000 | 0.99700.9970 | 0.98300.9830 |  | 1.00001.0000 | 0.99700.9970 | 0.98200.9820 |  | 0.99200.9920 | 0.98600.9860 | 0.92400.9240 |  | 0.96300.9630 | 0.89200.8920 | 0.57400.5740 |  |
| N=10/K=2N=10/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.30100.3010 | 0.19600.1960 | 0.07600.0760 |  | 0.30800.3080 | 0.20700.2070 | 0.06200.0620 |  | 0.31900.3190 | 0.20600.2060 | 0.07200.0720 |  | 0.35400.3540 | 0.22100.2210 | 0.08400.0840 |  | 0.28200.2820 | 0.13800.1380 | 0.03400.0340 |  | 0.21500.2150 | 0.11800.1180 | 0.02600.0260 |  |
|  | T=200T=200 |  | 0.58600.5860 | 0.44000.4400 | 0.22400.2240 |  | 0.58500.5850 | 0.44400.4440 | 0.21000.2100 |  | 0.61200.6120 | 0.49200.4920 | 0.23400.2340 |  | 0.62600.6260 | 0.48500.4850 | 0.20900.2090 |  | 0.54100.5410 | 0.42200.4220 | 0.11700.1170 |  | 0.34800.3480 | 0.19200.1920 | 0.05300.0530 |  |
|  | T=400T=400 |  | 0.88800.8880 | 0.81300.8130 | 0.55900.5590 |  | 0.89200.8920 | 0.84200.8420 | 0.64000.6400 |  | 0.91500.9150 | 0.85600.8560 | 0.69000.6900 |  | 0.91200.9120 | 0.85500.8550 | 0.68300.6830 |  | 0.86300.8630 | 0.75600.7560 | 0.49200.4920 |  | 0.71700.7170 | 0.54300.5430 | 0.17800.1780 |  |
|  | T=800T=800 |  | 0.99700.9970 | 0.99400.9940 | 0.95300.9530 |  | 0.99400.9940 | 0.98700.9870 | 0.96400.9640 |  | 0.99800.9980 | 0.99300.9930 | 0.97200.9720 |  | 0.99800.9980 | 0.99300.9930 | 0.97200.9720 |  | 0.99100.9910 | 0.97900.9790 | 0.92300.9230 |  | 0.94200.9420 | 0.87200.8720 | 0.67400.6740 |  |
| N=10/K=4N=10/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.25500.2550 | 0.16300.1630 | 0.06100.0610 |  | 0.26500.2650 | 0.17300.1730 | 0.06600.0660 |  | 0.28500.2850 | 0.18800.1880 | 0.05800.0580 |  | 0.30100.3010 | 0.18300.1830 | 0.05000.0500 |  | 0.22500.2250 | 0.12500.1250 | 0.03700.0370 |  | 0.21600.2160 | 0.11600.1160 | 0.02200.0220 |  |
|  | T=200T=200 |  | 0.49100.4910 | 0.35100.3510 | 0.11700.1170 |  | 0.49200.4920 | 0.35400.3540 | 0.14900.1490 |  | 0.54700.5470 | 0.38300.3830 | 0.16100.1610 |  | 0.54500.5450 | 0.38400.3840 | 0.14300.1430 |  | 0.41000.4100 | 0.26400.2640 | 0.11000.1100 |  | 0.30700.3070 | 0.18700.1870 | 0.04700.0470 |  |
|  | T=400T=400 |  | 0.82400.8240 | 0.70800.7080 | 0.47400.4740 |  | 0.83800.8380 | 0.74400.7440 | 0.46900.4690 |  | 0.86700.8670 | 0.81100.8110 | 0.57400.5740 |  | 0.86600.8660 | 0.81000.8100 | 0.59700.5970 |  | 0.77600.7760 | 0.64900.6490 | 0.32500.3250 |  | 0.64200.6420 | 0.49900.4990 | 0.16800.1680 |  |
|  | T=800T=800 |  | 0.98800.9880 | 0.97600.9760 | 0.93400.9340 |  | 0.98800.9880 | 0.97400.9740 | 0.93100.9310 |  | 0.99600.9960 | 0.98600.9860 | 0.94600.9460 |  | 0.99600.9960 | 0.98500.9850 | 0.94600.9460 |  | 0.98200.9820 | 0.94600.9460 | 0.83300.8330 |  | 0.94100.9410 | 0.86800.8680 | 0.48900.4890 |  |

Note: R version 4.5.2 was used to compute the statistics..

Table 8: Rejection rates (percentages) under the alternative hypothesis H1:α1=0.2H\_{1}:\alpha\_{1}=0.2 and αj=0\alpha\_{j}=0 (j=2,…,Nj=2,\ldots,N) when the G​E​X​O​GGEXOG holds

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 𝒲B​C​-​G​D\mathcal{W}^{BC\text{-}GD} | | |  | 𝒲G​D\mathcal{W}^{GD} | | |  | 𝒲F​G​L​S​-​D\mathcal{W}^{FGLS\text{-}D} | | |  | 𝒲F​G​L​S−C​O\mathcal{W}^{FGLS-CO} | | |  | H​A​RHAR | | |  | G​R​SGRS | | |  |
|  |  |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  |
| N=5/K=2N=5/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.39100.3910 | 0.26300.2630 | 0.13900.1390 |  | 0.37600.3760 | 0.28100.2810 | 0.10900.1090 |  | 0.42600.4260 | 0.29900.2990 | 0.11200.1120 |  | 0.40700.4070 | 0.28000.2800 | 0.12200.1220 |  | 0.39700.3970 | 0.24700.2470 | 0.06600.0660 |  | 0.21200.2120 | 0.10700.1070 | 0.03700.0370 |  |
|  | T=200T=200 |  | 0.69100.6910 | 0.58400.5840 | 0.32300.3230 |  | 0.68900.6890 | 0.58800.5880 | 0.36800.3680 |  | 0.73400.7340 | 0.58700.5870 | 0.40500.4050 |  | 0.72700.7270 | 0.61200.6120 | 0.41800.4180 |  | 0.57000.5700 | 0.46000.4600 | 0.26000.2600 |  | 0.39500.3950 | 0.22600.2260 | 0.06500.0650 |  |
|  | T=400T=400 |  | 0.96200.9620 | 0.92400.9240 | 0.71500.7150 |  | 0.96700.9670 | 0.92500.9250 | 0.80000.8000 |  | 0.97800.9780 | 0.94000.9400 | 0.84500.8450 |  | 0.97400.9740 | 0.93400.9340 | 0.79900.7990 |  | 0.86200.8620 | 0.76900.7690 | 0.50200.5020 |  | 0.72700.7270 | 0.54700.5470 | 0.18400.1840 |  |
|  | T=800T=800 |  | 1.00001.0000 | 0.99800.9980 | 0.77600.7760 |  | 0.99900.9990 | 0.99900.9990 | 0.99600.9960 |  | 0.99900.9990 | 0.99900.9990 | 0.99800.9980 |  | 0.99900.9990 | 0.99900.9990 | 0.99500.9950 |  | 0.96200.9620 | 0.92400.9240 | 0.80800.8080 |  | 0.88900.8890 | 0.75800.7580 | 0.40900.4090 |  |
| N=5/K=4N=5/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.35900.3590 | 0.22300.2230 | 0.08600.0860 |  | 0.35700.3570 | 0.21800.2180 | 0.06300.0630 |  | 0.37900.3790 | 0.27600.2760 | 0.09700.0970 |  | 0.37000.3700 | 0.27500.2750 | 0.08400.0840 |  | 0.30200.3020 | 0.21000.2100 | 0.04400.0440 |  | 0.24100.2410 | 0.12100.1210 | 0.02000.0200 |  |
|  | T=200T=200 |  | 0.66500.6650 | 0.55700.5570 | 0.21100.2110 |  | 0.72200.7220 | 0.56600.5660 | 0.21300.2130 |  | 0.73500.7350 | 0.61300.6130 | 0.25800.2580 |  | 0.71400.7140 | 0.56300.5630 | 0.21800.2180 |  | 0.54100.5410 | 0.35200.3520 | 0.17700.1770 |  | 0.38500.3850 | 0.24000.2400 | 0.06600.0660 |  |
|  | T=400T=400 |  | 0.92300.9230 | 0.84800.8480 | 0.67900.6790 |  | 0.93200.9320 | 0.87800.8780 | 0.71600.7160 |  | 0.95600.9560 | 0.91900.9190 | 0.72800.7280 |  | 0.95000.9500 | 0.90000.9000 | 0.67600.6760 |  | 0.77100.7710 | 0.66700.6670 | 0.38200.3820 |  | 0.65000.6500 | 0.45900.4590 | 0.14000.1400 |  |
|  | T=800T=800 |  | 0.99900.9990 | 0.99300.9930 | 0.95700.9570 |  | 1.00001.0000 | 0.99600.9960 | 0.97100.9710 |  | 1.00001.0000 | 0.99900.9990 | 0.99000.9900 |  | 0.99900.9990 | 0.99600.9960 | 0.96800.9680 |  | 0.90500.9050 | 0.82300.8230 | 0.58400.5840 |  | 0.83400.8340 | 0.68200.6820 | 0.35700.3570 |  |
| N=10/K=2N=10/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.29500.2950 | 0.19800.1980 | 0.08000.0800 |  | 0.29900.2990 | 0.19600.1960 | 0.05300.0530 |  | 0.31800.3180 | 0.19600.1960 | 0.08200.0820 |  | 0.33400.3340 | 0.21300.2130 | 0.08800.0880 |  | 0.28300.2830 | 0.14400.1440 | 0.03800.0380 |  | 0.22100.2210 | 0.12800.1280 | 0.03400.0340 |  |
|  | T=200T=200 |  | 0.57400.5740 | 0.43200.4320 | 0.20500.2050 |  | 0.56900.5690 | 0.42800.4280 | 0.20600.2060 |  | 0.60900.6090 | 0.48000.4800 | 0.23800.2380 |  | 0.61400.6140 | 0.49400.4940 | 0.22300.2230 |  | 0.49500.4950 | 0.34500.3450 | 0.16500.1650 |  | 0.32800.3280 | 0.21600.2160 | 0.05600.0560 |  |
|  | T=400T=400 |  | 0.88100.8810 | 0.81900.8190 | 0.53300.5330 |  | 0.89600.8960 | 0.84300.8430 | 0.62300.6230 |  | 0.91900.9190 | 0.85400.8540 | 0.67400.6740 |  | 0.92400.9240 | 0.85100.8510 | 0.69000.6900 |  | 0.76000.7600 | 0.64100.6410 | 0.40500.4050 |  | 0.62000.6200 | 0.44200.4420 | 0.20600.2060 |  |
|  | T=800T=800 |  | 0.99900.9990 | 0.99300.9930 | 0.94000.9400 |  | 0.99500.9950 | 0.98900.9890 | 0.95700.9570 |  | 0.99700.9970 | 0.99300.9930 | 0.96700.9670 |  | 0.99700.9970 | 0.99200.9920 | 0.96000.9600 |  | 0.95200.9520 | 0.90300.9030 | 0.69400.6940 |  | 0.87700.8770 | 0.76900.7690 | 0.52600.5260 |  |
| N=10/K=4N=10/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.25000.2500 | 0.15300.1530 | 0.05400.0540 |  | 0.25600.2560 | 0.17000.1700 | 0.05700.0570 |  | 0.29700.2970 | 0.17300.1730 | 0.06100.0610 |  | 0.29900.2990 | 0.18500.1850 | 0.06100.0610 |  | 0.20900.2090 | 0.13200.1320 | 0.05300.0530 |  | 0.21200.2120 | 0.13200.1320 | 0.02600.0260 |  |
|  | T=200T=200 |  | 0.50700.5070 | 0.35000.3500 | 0.13400.1340 |  | 0.49200.4920 | 0.33700.3370 | 0.12300.1230 |  | 0.53600.5360 | 0.37300.3730 | 0.14300.1430 |  | 0.54000.5400 | 0.40100.4010 | 0.19100.1910 |  | 0.40300.4030 | 0.27900.2790 | 0.12500.1250 |  | 0.34200.3420 | 0.21700.2170 | 0.05100.0510 |  |
|  | T=400T=400 |  | 0.82600.8260 | 0.70800.7080 | 0.46100.4610 |  | 0.83700.8370 | 0.73200.7320 | 0.46500.4650 |  | 0.87800.8780 | 0.80100.8010 | 0.60800.6080 |  | 0.87600.8760 | 0.80300.8030 | 0.58500.5850 |  | 0.67200.6720 | 0.57700.5770 | 0.25500.2550 |  | 0.59200.5920 | 0.45500.4550 | 0.15100.1510 |  |
|  | T=800T=800 |  | 0.98800.9880 | 0.97600.9760 | 0.92700.9270 |  | 0.98800.9880 | 0.97500.9750 | 0.93600.9360 |  | 0.99600.9960 | 0.98800.9880 | 0.94900.9490 |  | 0.99500.9950 | 0.98500.9850 | 0.95500.9550 |  | 0.89300.8930 | 0.79800.7980 | 0.58800.5880 |  | 0.85100.8510 | 0.74900.7490 | 0.35000.3500 |  |

Note: As for Table [7](https://arxiv.org/html/2601.21272v1#Sx1.T7 "Table 7 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").

Table 9: Rejection rates (percentages) under the alternative hypothesis H1:α1=0.2H\_{1}:\alpha\_{1}=0.2 and αj=0\alpha\_{j}=0 (j=2,…,Nj=2,\ldots,N) when the E​B​DEBD holds

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 𝒲B​C​-​G​D\mathcal{W}^{BC\text{-}GD} | | |  | 𝒲G​D\mathcal{W}^{GD} | | |  | 𝒲F​G​L​S​-​D\mathcal{W}^{FGLS\text{-}D} | | |  | 𝒲F​G​L​S−C​O\mathcal{W}^{FGLS-CO} | | |  | H​A​RHAR | | |  | G​R​SGRS | | |  |
|  |  |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  | 10% | 5% | 1% |  |
| N=5/K=2N=5/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.31400.3140 | 0.19500.1950 | 0.09600.0960 |  | 0.32200.3220 | 0.20600.2060 | 0.05100.0510 |  | 0.34600.3460 | 0.23800.2380 | 0.07400.0740 |  | 0.38600.3860 | 0.25400.2540 | 0.08100.0810 |  | 0.35200.3520 | 0.18300.1830 | 0.05100.0510 |  | 0.19300.1930 | 0.10100.1010 | 0.03300.0330 |  |
|  | T=200T=200 |  | 0.59200.5920 | 0.47600.4760 | 0.31500.3150 |  | 0.61300.6130 | 0.49400.4940 | 0.21100.2110 |  | 0.65400.6540 | 0.49400.4940 | 0.30000.3000 |  | 0.62200.6220 | 0.48600.4860 | 0.26000.2600 |  | 0.52300.5230 | 0.39700.3970 | 0.22400.2240 |  | 0.32900.3290 | 0.20800.2080 | 0.05800.0580 |  |
|  | T=400T=400 |  | 0.91700.9170 | 0.83300.8330 | 0.49100.4910 |  | 0.92700.9270 | 0.84900.8490 | 0.57600.5760 |  | 0.92100.9210 | 0.85700.8570 | 0.66500.6650 |  | 0.89200.8920 | 0.82900.8290 | 0.60200.6020 |  | 0.78000.7800 | 0.65600.6560 | 0.37500.3750 |  | 0.61500.6150 | 0.42600.4260 | 0.15800.1580 |  |
|  | T=800T=800 |  | 0.99800.9980 | 0.99400.9940 | 0.72900.7290 |  | 0.99900.9990 | 0.99600.9960 | 0.94000.9400 |  | 0.99400.9940 | 0.98200.9820 | 0.93000.9300 |  | 0.97600.9760 | 0.96000.9600 | 0.83900.8390 |  | 0.90300.9030 | 0.82300.8230 | 0.63400.6340 |  | 0.76500.7650 | 0.58800.5880 | 0.28700.2870 |  |
| N=5/K=4N=5/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.34000.3400 | 0.20000.2000 | 0.06700.0670 |  | 0.34500.3450 | 0.21400.2140 | 0.05200.0520 |  | 0.33400.3340 | 0.21400.2140 | 0.07500.0750 |  | 0.33900.3390 | 0.21100.2110 | 0.07500.0750 |  | 0.28800.2880 | 0.17600.1760 | 0.03600.0360 |  | 0.21700.2170 | 0.12000.1200 | 0.02400.0240 |  |
|  | T=200T=200 |  | 0.64200.6420 | 0.49000.4900 | 0.18400.1840 |  | 0.65700.6570 | 0.51200.5120 | 0.16800.1680 |  | 0.65700.6570 | 0.54000.5400 | 0.22300.2230 |  | 0.61700.6170 | 0.44800.4480 | 0.15000.1500 |  | 0.48000.4800 | 0.31900.3190 | 0.09900.0990 |  | 0.34200.3420 | 0.17900.1790 | 0.03800.0380 |  |
|  | T=400T=400 |  | 0.89800.8980 | 0.82800.8280 | 0.62200.6220 |  | 0.91100.9110 | 0.84400.8440 | 0.64000.6400 |  | 0.88700.8870 | 0.81400.8140 | 0.61400.6140 |  | 0.85200.8520 | 0.73200.7320 | 0.49000.4900 |  | 0.67300.6730 | 0.55500.5550 | 0.23000.2300 |  | 0.55000.5500 | 0.33900.3390 | 0.14400.1440 |  |
|  | T=800T=800 |  | 0.99400.9940 | 0.98800.9880 | 0.91700.9170 |  | 0.99700.9970 | 0.98300.9830 | 0.94200.9420 |  | 0.97600.9760 | 0.95700.9570 | 0.87100.8710 |  | 0.95600.9560 | 0.91100.9110 | 0.72400.7240 |  | 0.82000.8200 | 0.64400.6440 | 0.31300.3130 |  | 0.60500.6050 | 0.45900.4590 | 0.23100.2310 |  |
| N=10/K=2N=10/K=2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.26600.2660 | 0.17200.1720 | 0.04500.0450 |  | 0.28800.2880 | 0.18000.1800 | 0.03900.0390 |  | 0.29200.2920 | 0.19000.1900 | 0.07500.0750 |  | 0.32500.3250 | 0.19200.1920 | 0.09300.0930 |  | 0.27800.2780 | 0.12600.1260 | 0.04400.0440 |  | 0.22300.2230 | 0.11800.1180 | 0.03400.0340 |  |
|  | T=200T=200 |  | 0.52400.5240 | 0.39200.3920 | 0.19600.1960 |  | 0.49300.4930 | 0.37400.3740 | 0.17000.1700 |  | 0.57100.5710 | 0.44500.4450 | 0.21300.2130 |  | 0.59600.5960 | 0.47400.4740 | 0.22300.2230 |  | 0.48000.4800 | 0.34500.3450 | 0.16300.1630 |  | 0.32600.3260 | 0.21200.2120 | 0.06000.0600 |  |
|  | T=400T=400 |  | 0.86900.8690 | 0.77100.7710 | 0.41000.4100 |  | 0.87100.8710 | 0.79300.7930 | 0.54100.5410 |  | 0.87000.8700 | 0.80000.8000 | 0.59800.5980 |  | 0.86500.8650 | 0.75400.7540 | 0.51000.5100 |  | 0.71200.7120 | 0.58300.5830 | 0.37100.3710 |  | 0.57000.5700 | 0.40700.4070 | 0.14600.1460 |  |
|  | T=800T=800 |  | 0.99500.9950 | 0.98700.9870 | 0.94000.9400 |  | 0.99100.9910 | 0.98100.9810 | 0.93300.9330 |  | 0.99200.9920 | 0.98000.9800 | 0.92300.9230 |  | 0.98200.9820 | 0.95900.9590 | 0.86700.8670 |  | 0.90600.9060 | 0.84800.8480 | 0.57800.5780 |  | 0.78900.7890 | 0.65500.6550 | 0.36100.3610 |  |
| N=10/K=4N=10/K=4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | T=100T=100 |  | 0.23300.2330 | 0.13200.1320 | 0.06400.0640 |  | 0.24400.2440 | 0.15000.1500 | 0.04600.0460 |  | 0.25600.2560 | 0.16500.1650 | 0.05700.0570 |  | 0.26500.2650 | 0.16700.1670 | 0.05300.0530 |  | 0.21700.2170 | 0.12800.1280 | 0.04200.0420 |  | 0.19300.1930 | 0.11700.1170 | 0.02800.0280 |  |
|  | T=200T=200 |  | 0.47300.4730 | 0.30600.3060 | 0.11900.1190 |  | 0.49100.4910 | 0.33200.3320 | 0.11500.1150 |  | 0.49700.4970 | 0.34200.3420 | 0.15400.1540 |  | 0.48700.4870 | 0.36300.3630 | 0.20000.2000 |  | 0.38000.3800 | 0.27200.2720 | 0.09000.0900 |  | 0.34200.3420 | 0.17400.1740 | 0.06100.0610 |  |
|  | T=400T=400 |  | 0.80600.8060 | 0.63600.6360 | 0.42100.4210 |  | 0.81300.8130 | 0.71300.7130 | 0.44700.4470 |  | 0.82100.8210 | 0.71700.7170 | 0.38500.3850 |  | 0.80600.8060 | 0.68000.6800 | 0.44800.4480 |  | 0.63200.6320 | 0.50200.5020 | 0.23200.2320 |  | 0.51500.5150 | 0.35600.3560 | 0.15100.1510 |  |
|  | T=800T=800 |  | 0.98500.9850 | 0.96700.9670 | 0.92000.9200 |  | 0.98500.9850 | 0.96900.9690 | 0.90500.9050 |  | 0.98100.9810 | 0.95100.9510 | 0.84100.8410 |  | 0.97400.9740 | 0.93900.9390 | 0.76800.7680 |  | 0.81500.8150 | 0.67100.6710 | 0.45300.4530 |  | 0.76500.7650 | 0.59700.5970 | 0.19800.1980 |  |

Note: As for Table [7](https://arxiv.org/html/2601.21272v1#Sx1.T7 "Table 7 ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models").

Table 10: Descriptive statistics and unit root tests

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Mean | SD | Min | Max |  | ADF | Lags |  | TT |  |
| FF3 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Rm−RfR\_{m}-R\_{f} |  | 0.01030.0103 | 0.04640.0464 | −0.1720-0.1720 | 0.13600.1360 |  | −4.9877-4.9877 | 77 |  | 206206 |  |
|  | S​M​BSMB |  | −0.0005-0.0005 | 0.02600.0260 | −0.0593-0.0593 | 0.07140.0714 |  | −14.9473-14.9473 | 0 |  | 206206 |  |
|  | H​M​LHML |  | −0.0015-0.0015 | 0.03410.0341 | −0.1383-0.1383 | 0.12860.1286 |  | −12.1516-12.1516 | 0 |  | 206206 |  |
| FF5 |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Rm−RfR\_{m}-R\_{f} |  | 0.01030.0103 | 0.04640.0464 | −0.1720-0.1720 | 0.13580.1358 |  | −4.9904-4.9904 | 77 |  | 206206 |  |
|  | S​M​BSMB |  | −0.0008-0.0008 | 0.02780.0278 | −0.0818-0.0818 | 0.08340.0834 |  | −10.4293-10.4293 | 11 |  | 206206 |  |
|  | H​M​LHML |  | −0.0015-0.0015 | 0.03410.0341 | −0.1383-0.1383 | 0.12860.1286 |  | −12.1516-12.1516 | 0 |  | 206206 |  |
|  | W​M​LWML |  | 0.00240.0024 | 0.01990.0199 | −0.0522-0.0522 | 0.07190.0719 |  | −12.0900-12.0900 | 0 |  | 206206 |  |
|  | C​M​ACMA |  | 0.00010.0001 | 0.02060.0206 | −0.0708-0.0708 | 0.07730.0773 |  | −12.7320-12.7320 | 0 |  | 206206 |  |

Notes:

* (1)

  “Rm−RfR\_{m}-R\_{f},” “S​M​BSMB,” “H​M​LHML,” “R​M​WRMW,” and “C​M​ACMA” denote the returns on each risk factor, wich correspond to Fama-French multi-factor models.
* (2)

  “ADF” denotes the ADF test statistics and “Lags” denotes the lag order selected by the BIC.
* (3)

  In computing the ADF test, a model with a time trend and a constant is assumed. The critical value at the 5% significance level for the ADF test is “−3.41-3.41.”
* (4)

  R version 4.5.2 was used to compute the statistics.

Table 11: Test statistics for null hypothesis 𝜶0=𝟎\mbox{{$\alpha$}}\_{0}=\mathbf{0} (FF3/FF5 models)

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | 𝒲B​C​-​G​D\mathcal{W}^{BC\text{-}GD} | 𝒲G​D\mathcal{W}^{GD} | 𝒲F​G​L​S​-​D\mathcal{W}^{FGLS\text{-}D} | 𝒲F​G​L​S​-​C​O\mathcal{W}^{FGLS\text{-}CO} |  |
| FF3 |  |  |  |  |  |  |  |
|  | MB6 |  | 7.49647.4964 | 16.411016.4110 | 16.134316.1343 | 16.011416.0114 |  |
|  |  | (0.0210)(0.0210) | (0.0117)(0.0117) | (0.0131)(0.0131) | (0.0137)(0.0137) |  |
|  | MB25 |  | 50.035850.0358 | 79.271179.2711 | 74.349474.3494 | 70.340070.3400 |  |
|  |  | (0.0420)(0.0420) | (0.0000)(0.0000) | (0.0000)(0.0000) | (0.0000)(0.0000) |  |
| FF5 |  |  |  |  |  |  |  |
|  | MB6 |  | 7.76177.7617 | 13.744813.7448 | 13.899913.8999 | 13.918913.9189 |  |
|  |  | (0.0390)(0.0390) | (0.0326)(0.0326) | (0.0308)(0.0308) | (0.0306)(0.0306) |  |
|  | MB25 |  | 55.851855.8518 | 78.966078.9660 | 72.992072.9920 | 67.688567.6885 |  |
|  |  | (0.0601)(0.0601) | (0.0000)(0.0000) | (0.0000)(0.0000) | (0.0000)(0.0000) |  |
|  | MI6 |  | 7.83357.8335 | 4.10014.1001 | 4.16574.1657 | 3.90033.9003 |  |
|  |  | (0.7237)(0.7237) | (0.6631)(0.6631) | (0.6543)(0.6543) | (0.6902)(0.6902) |  |
|  | MI25 |  | 55.516255.5162 | 61.267861.2678 | 60.837860.8378 | 56.617756.6177 |  |
|  |  | (0.1381)(0.1381) | (0.0001)(0.0001) | (0.0001)(0.0001) | (0.0003)(0.0003) |  |
|  | MO6 |  | 7.84677.8467 | 7.67727.6772 | 8.34478.3447 | 7.88407.8840 |  |
|  |  | (0.3283)(0.3283) | (0.2627)(0.2627) | (0.2139)(0.2139) | (0.2467)(0.2467) |  |
|  | MO25 |  | 54.996654.9966 | 51.712551.7125 | 49.809349.8093 | 45.779645.7796 |  |
|  |  | (0.2475)(0.2475) | (0.0013)(0.0013) | (0.0022)(0.0022) | (0.0068)(0.0068) |  |

Notes:

* (1)

  “𝒲B​C​-​G​D\mathcal{W}^{BC\text{-}GD},” “𝒲G​D\mathcal{W}^{GD},” “𝒲F​G​L​S​-​D\mathcal{W}^{FGLS\text{-}D},” and “𝒲F​G​L​S−C​O\mathcal{W}^{FGLS-CO}” denote the Wald statistics based on the bootstrap-based bias-corrected GD estimator, the GD estimator, the FGLS-D estimator, and the FGLS-CO estimator, respectively.
* (2)

  “MB,” “MO,” and “MI” denotes the portfolios sorted by “market capitalization (size of firms) and book-to-market ratio,” “market capitalization and profitability,” and “market capitalization and investment growth rate,” respectively.
* (3)

  pp-values for the test statistics under the null hypothesis are in parentheses.
* (4)

  R version 4.5.2 was used to compute the statistics.

## Appendix

### A.1 Proof of Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")

(i) Define the innovation

|  |  |  |
| --- | --- | --- |
|  | 𝜺t:=𝒛¯t−𝒫t−1​[𝒛¯t],{\mbox{$\varepsilon$}}\_{t}:=\bar{{\mbox{$z$}}}\_{t}-\mathscr{P}\_{t-1}[\bar{{\mbox{$z$}}}\_{t}], |  |

where 𝒫t−1:L2→ℋt−1\mathscr{P}\_{t-1}:L^{2}\to\mathscr{H}\_{t-1} is the L2L^{2}-orthogonal projection onto ℋt−1:=span¯​{𝒛¯t−1,𝒛¯t−2,…}\mathscr{H}\_{t-1}:=\overline{\mathrm{span}}\{\bar{{\mbox{$z$}}}\_{t-1},\bar{{\mbox{$z$}}}\_{t-2},\ldots\}. By the projection theorem (e.g. Theorem 2.3.1 in Brockwell and Davis ([1991](https://arxiv.org/html/2601.21272v1#bib.bib580 "Time series: theory and methods"))), 𝜺t∈L2{\mbox{$\varepsilon$}}\_{t}\in L^{2} and 𝜺t⟂ℋt−1{\mbox{$\varepsilon$}}\_{t}\perp\mathscr{H}\_{t-1}, i.e., 𝔼​[𝜺t′​𝑽]=0{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}^{\prime}{\mbox{$V$}}]=0 for all 𝑽∈ℋt−1{\mbox{$V$}}\in\mathscr{H}\_{t-1}. In particular, 𝔼​[𝜺t​𝒛¯t−ℓ′]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}\bar{{\mbox{$z$}}}\_{t-\ell}^{\prime}]={\mbox{$0$}} for all ℓ≥1\ell\geq 1, and since 𝜺t−h∈ℋt−1{\mbox{$\varepsilon$}}\_{t-h}\in\mathscr{H}\_{t-1} for all h≥1h\geq 1 (because 𝜺t−h∈ℋt−h⊆ℋt−1{\mbox{$\varepsilon$}}\_{t-h}\in\mathscr{H}\_{t-h}\subseteq\mathscr{H}\_{t-1}), we have 𝔼​[𝜺t​𝜺t−h′]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{t-h}^{\prime}]={\mbox{$0$}} for h≥1h\geq 1. Moreover, 𝔼​[𝒛¯t]=𝟎{\mathbb{E}}[\bar{{\mbox{$z$}}}\_{t}]={\mbox{$0$}} and every element of ℋt−1\mathscr{H}\_{t-1} has mean zero, hence 𝔼​[𝜺t]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}]={\mbox{$0$}}. Because {𝒛¯t}\{\bar{{\mbox{$z$}}}\_{t}\} is covariance-stationary, the variance 𝚺:=𝔼​[𝜺t​𝜺t′]{\mbox{$\Sigma$}}:={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{t}^{\prime}] is constant in tt. Thus {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\} is (second-order) white noise.

By definition,

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=𝒫t−1​[𝒛¯t]+𝜺t,𝒫t−1​[𝒛¯t]∈ℋt−1,𝜺t⟂ℋt−1.\bar{{\mbox{$z$}}}\_{t}=\mathscr{P}\_{t-1}[\bar{{\mbox{$z$}}}\_{t}]+{\mbox{$\varepsilon$}}\_{t},\qquad\mathscr{P}\_{t-1}[\bar{{\mbox{$z$}}}\_{t}]\in\mathscr{H}\_{t-1},\quad{\mbox{$\varepsilon$}}\_{t}\perp\mathscr{H}\_{t-1}. |  |

Since ℋt−1⊂ℋt\mathscr{H}\_{t-1}\subset\mathscr{H}\_{t} and 𝜺t∈ℋt{\mbox{$\varepsilon$}}\_{t}\in\mathscr{H}\_{t}, we obtain the orthogonal direct sum

|  |  |  |
| --- | --- | --- |
|  | ℋt=ℋt−1⊕span​{𝜺t}.\mathscr{H}\_{t}=\mathscr{H}\_{t-1}\ \oplus\ \mathrm{span}\{{\mbox{$\varepsilon$}}\_{t}\}. |  |

Iterating this identity yields, for any m≥0m\geq 0,

|  |  |  |
| --- | --- | --- |
|  | ℋt=ℋt−m−1⊕⨁j=0mspan​{𝜺t−j}.\mathscr{H}\_{t}=\mathscr{H}\_{t-m-1}\ \oplus\ \bigoplus\_{j=0}^{m}\mathrm{span}\{{\mbox{$\varepsilon$}}\_{t-j}\}. |  |

Taking m→∞m\to\infty and using that orthogonal direct sums of closed subspaces are closed, we get

|  |  |  |
| --- | --- | --- |
|  | ℋt=(⋂m≥0ℋt−m)⊕span¯​{𝜺t,𝜺t−1,…}.\mathscr{H}\_{t}=\Big(\bigcap\_{m\geq 0}\mathscr{H}\_{t-m}\Big)\ \oplus\ \overline{\mathrm{span}}\{{\mbox{$\varepsilon$}}\_{t},{\mbox{$\varepsilon$}}\_{t-1},\ldots\}. |  |

By pure nondeterminism in Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), ⋂m≥0ℋt−m={𝟎}\bigcap\_{m\geq 0}\mathscr{H}\_{t-m}=\{{\mbox{$0$}}\}, hence

|  |  |  |
| --- | --- | --- |
|  | ℋt=span¯​{𝜺t,𝜺t−1,…}.\mathscr{H}\_{t}=\overline{\mathrm{span}}\{{\mbox{$\varepsilon$}}\_{t},{\mbox{$\varepsilon$}}\_{t-1},\ldots\}. |  |

Because {𝜺t−h}h≥0\{{\mbox{$\varepsilon$}}\_{t-h}\}\_{h\geq 0} is a mutually orthogonal family that densely spans
ℋt\mathscr{H}\_{t}, every element of ℋt\mathscr{H}\_{t} admits a unique L2L^{2}-orthogonal expansion.
In particular, there exists a unique sequence of deterministic matrices
{𝚵h}h≥0⊂ℝm×m\{{\mbox{$\Xi$}}\_{h}\}\_{h\geq 0}\subset\mathbb{R}^{m\times m} such that

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=∑h=0∞𝚵h​𝜺t−hin ​L2.\bar{{\mbox{$z$}}}\_{t}=\sum\_{h=0}^{\infty}{\mbox{$\Xi$}}\_{h}\,{\mbox{$\varepsilon$}}\_{t-h}\quad\text{in }L^{2}. |  |

Moreover, the normal equations give the coefficient formula

|  |  |  |
| --- | --- | --- |
|  | 𝚵h=𝔼​[𝒛¯t​𝜺t−h′]​𝚺−1(h≥0),{\mbox{$\Xi$}}\_{h}={\mathbb{E}}[\bar{{\mbox{$z$}}}\_{t}{\mbox{$\varepsilon$}}\_{t-h}^{\prime}]\,{\mbox{$\Sigma$}}^{-1}\qquad(h\geq 0), |  |

provided 𝚺>0{\mbox{$\Sigma$}}>0 (as assumed). In particular, 𝚵0=𝔼​[𝒛¯t​𝜺t′]​𝚺−1=𝚺𝚺−1=𝑰m{\mbox{$\Xi$}}\_{0}={\mathbb{E}}[\bar{{\mbox{$z$}}}\_{t}{\mbox{$\varepsilon$}}\_{t}^{\prime}]\,{\mbox{$\Sigma$}}^{-1}={\mbox{$\Sigma$}}{\mbox{$\Sigma$}}^{-1}={\mbox{$I$}}\_{m}. Adding back the mean yields the Wold representation

|  |  |  |
| --- | --- | --- |
|  | 𝒛t=𝝁z+∑h=0∞𝚵h​𝜺t−hin ​L2.{\mbox{$z$}}\_{t}={\mbox{$\mu$}}\_{z}+\sum\_{h=0}^{\infty}{\mbox{$\Xi$}}\_{h}\,{\mbox{$\varepsilon$}}\_{t-h}\quad\text{in }L^{2}. |  |

∎

(ii) Finite-predictor exactness at lag p0p\_{0} implies that there exist matrices 𝑨j(p){\mbox{$A$}}\_{j}^{(p)} such that

|  |  |  |
| --- | --- | --- |
|  | 𝒫t−1​[𝒛¯t]=𝒫t−1(p)​[𝒛¯t]=∑j=1p𝑨j(p)​𝒛¯t−j.\mathscr{P}\_{t-1}[\bar{{\mbox{$z$}}}\_{t}]=\mathscr{P}^{(p)}\_{t-1}[\bar{{\mbox{$z$}}}\_{t}]=\sum\_{j=1}^{p}{\mbox{$A$}}\_{j}^{(p)}\bar{{\mbox{$z$}}}\_{t-j}. |  |

Since 𝜺t:=𝒛¯t−𝒫t−1​[𝒛¯t]{\mbox{$\varepsilon$}}\_{t}:=\bar{{\mbox{$z$}}}\_{t}-\mathscr{P}\_{t-1}[\bar{{\mbox{$z$}}}\_{t}], we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=∑j=1p𝑨j(p)​𝒛¯t−j+𝜺tin​L2.\bar{{\mbox{$z$}}}\_{t}=\sum\_{j=1}^{p}{\mbox{$A$}}\_{j}^{(p)}\bar{{\mbox{$z$}}}\_{t-j}+{\mbox{$\varepsilon$}}\_{t}\quad\text{in}\,L^{2}. |  |

Setting 𝚿j:=𝑨j(p){\mbox{$\Psi$}}\_{j}:={\mbox{$A$}}\_{j}^{(p)} for j=1,…,pj=1,\dots,p yields ([4](https://arxiv.org/html/2601.21272v1#S2.E4 "In item (ii) ‣ Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")). Substituting the Wold expansions 𝒛¯t−j=∑h=0∞𝚵h​𝜺t−j−h\bar{{\mbox{$z$}}}\_{t-j}=\sum\_{h=0}^{\infty}{\mbox{$\Xi$}}\_{h}{\mbox{$\varepsilon$}}\_{t-j-h} and reindexing by i=j+hi=j+h (first for finite truncations, then letting the truncation →∞\to\infty in L2L^{2}) gives

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=𝜺t+∑i=1∞(∑j=1min⁡{p,i}𝑨j(p)𝚵i−j)𝜺t−i=:∑i=0∞𝑫i(p)𝜺t−i,\bar{{\mbox{$z$}}}\_{t}={\mbox{$\varepsilon$}}\_{t}+\sum\_{i=1}^{\infty}\Big(\sum\_{j=1}^{\min\{p,i\}}{\mbox{$A$}}\_{j}^{(p)}{\mbox{$\Xi$}}\_{i-j}\Big){\mbox{$\varepsilon$}}\_{t-i}=:\sum\_{i=0}^{\infty}{\mbox{$D$}}\_{i}^{(p)}{\mbox{$\varepsilon$}}\_{t-i}, |  |

where 𝑫0(p)=𝑰m{\mbox{$D$}}\_{0}^{(p)}={\mbox{$I$}}\_{m} and 𝑫i(p):=∑j=1min⁡{p,i}𝑨j(p)​𝚵i−j{\mbox{$D$}}\_{i}^{(p)}:=\sum\_{j=1}^{\min\{p,i\}}{\mbox{$A$}}\_{j}^{(p)}{\mbox{$\Xi$}}\_{i-j} for i≥1i\geq 1. On the other hand, (i) gives 𝒛¯t=∑i=0∞𝚵i​𝜺t−i\bar{{\mbox{$z$}}}\_{t}=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{i}{\mbox{$\varepsilon$}}\_{t-i}, and the innovations are mutually orthogonal. Hence coefficients are unique, and for all i≥1i\geq 1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚵i=∑j=1min⁡{p,i}𝑨j(p)​𝚵i−j.{\mbox{$\Xi$}}\_{i}=\sum\_{j=1}^{\min\{p,i\}}{\mbox{$A$}}\_{j}^{(p)}{\mbox{$\Xi$}}\_{i-j}. |  | (35) |

Define {𝚿j}j≥1\{{\mbox{$\Psi$}}\_{j}\}\_{j\geq 1} recursively by

|  |  |  |
| --- | --- | --- |
|  | 𝚿1:=𝚵1,𝚿n:=𝚵n−∑j=1n−1𝚿j​𝚵n−j(n≥2).{\mbox{$\Psi$}}\_{1}:={\mbox{$\Xi$}}\_{1},\qquad{\mbox{$\Psi$}}\_{n}:={\mbox{$\Xi$}}\_{n}-\sum\_{j=1}^{n-1}{\mbox{$\Psi$}}\_{j}{\mbox{$\Xi$}}\_{n-j}\quad(n\geq 2). |  |

A simple induction shows that, for every i≥1i\geq 1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚵i=∑j=1i𝚿j​𝚵i−j.{\mbox{$\Xi$}}\_{i}=\sum\_{j=1}^{i}{\mbox{$\Psi$}}\_{j}{\mbox{$\Xi$}}\_{i-j}. |  | (36) |

Comparing ([35](https://arxiv.org/html/2601.21272v1#Sx2.E35 "In A.1 Proof of Proposition 1 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) and ([36](https://arxiv.org/html/2601.21272v1#Sx2.E36 "In A.1 Proof of Proposition 1 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) successively for i=1,2,…i=1,2,\dots and using 𝚵0=𝑰m{\mbox{$\Xi$}}\_{0}={\mbox{$I$}}\_{m} gives

|  |  |  |
| --- | --- | --- |
|  | 𝚿j=𝑨j(p)(j=1,…,p),𝚿j=𝟎(j>p),{\mbox{$\Psi$}}\_{j}={\mbox{$A$}}\_{j}^{(p)}\quad(j=1,\ldots,p),\qquad{\mbox{$\Psi$}}\_{j}={\mbox{$0$}}\quad(j>p), |  |

so the VAR(pp) coefficients in ([4](https://arxiv.org/html/2601.21272v1#S2.E4 "In item (ii) ‣ Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) are unique. Finally, from ([36](https://arxiv.org/html/2601.21272v1#Sx2.E36 "In A.1 Proof of Proposition 1 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) we have, for n≥1n\geq 1,

|  |  |  |
| --- | --- | --- |
|  | 𝚵0=𝑰m,𝚵n=∑j=1n𝚿j​𝚵n−j,{\mbox{$\Xi$}}\_{0}={\mbox{$I$}}\_{m},\qquad{\mbox{$\Xi$}}\_{n}=\sum\_{j=1}^{n}{\mbox{$\Psi$}}\_{j}{\mbox{$\Xi$}}\_{n-j}, |  |

which is equivalent to 𝚿​(L)​𝚵​(L)=𝑰m{\mbox{$\Psi$}}(L){\mbox{$\Xi$}}(L)={\mbox{$I$}}\_{m} with
𝚿​(L):=𝑰m−∑j=1p𝚿j​Lj{\mbox{$\Psi$}}(L):={\mbox{$I$}}\_{m}-\sum\_{j=1}^{p}{\mbox{$\Psi$}}\_{j}L^{j} and
𝚵​(L):=𝑰m+∑n=1∞𝚵n​Ln{\mbox{$\Xi$}}(L):={\mbox{$I$}}\_{m}+\sum\_{n=1}^{\infty}{\mbox{$\Xi$}}\_{n}L^{n}. ∎

(iii) Define the companion state 𝒔t:=[𝒛¯t′,𝒛¯t−1′,…,𝒛¯t−p+1′]′∈ℝm​p{\mbox{$s$}}\_{t}:=[\bar{{\mbox{$z$}}}\_{t}^{\prime},\bar{{\mbox{$z$}}}\_{t-1}^{\prime},\ldots,\bar{{\mbox{$z$}}}\_{t-p+1}^{\prime}]^{\prime}\in\mathbb{R}^{mp} and matrices

|  |  |  |
| --- | --- | --- |
|  | 𝑭:=[𝚿1𝚿2⋯𝚿p𝑰m𝟎⋯𝟎⋮⋱⋱⋮𝟎⋯𝑰m𝟎],𝑮:=[𝑰m𝟎⋮𝟎].{\mbox{$F$}}:=\begin{bmatrix}{\mbox{$\Psi$}}\_{1}&{\mbox{$\Psi$}}\_{2}&\cdots&{\mbox{$\Psi$}}\_{p}\\ {\mbox{$I$}}\_{m}&{\mbox{$0$}}&\cdots&{\mbox{$0$}}\\ \vdots&\ddots&\ddots&\vdots\\ {\mbox{$0$}}&\cdots&{\mbox{$I$}}\_{m}&{\mbox{$0$}}\end{bmatrix},\qquad{\mbox{$G$}}:=\begin{bmatrix}{\mbox{$I$}}\_{m}\\ {\mbox{$0$}}\\ \vdots\\ {\mbox{$0$}}\end{bmatrix}. |  |

Then 𝒔t=𝑭𝒔t−1+𝑮𝜺t{\mbox{$s$}}\_{t}={\mbox{$F$}}{\mbox{$s$}}\_{t-1}+{\mbox{$G$}}{\mbox{$\varepsilon$}}\_{t} in L2L^{2}. Let 𝚺s:=𝔼​[𝒔t​𝒔t′]{\mbox{$\Sigma$}}\_{s}:={\mathbb{E}}[{\mbox{$s$}}\_{t}{\mbox{$s$}}\_{t}^{\prime}] denote the (finite) state covariance (stationarity).

Suppose by contradiction that 𝑭F has an eigenvalue λ\lambda with |λ|≥1|\lambda|\geq 1 and a corresponding left eigenvector 𝒗≠𝟎{\mbox{$v$}}\neq{\mbox{$0$}} such that 𝒗′​𝑭=λ​𝒗′{\mbox{$v$}}^{\prime}{\mbox{$F$}}=\lambda\,{\mbox{$v$}}^{\prime}. Set the scalar process wt:=𝒗′​𝒔tw\_{t}:={\mbox{$v$}}^{\prime}{\mbox{$s$}}\_{t} and ηt:=𝒗′​𝑮𝜺t\eta\_{t}:={\mbox{$v$}}^{\prime}{\mbox{$G$}}{\mbox{$\varepsilon$}}\_{t}. Then wt=λ​wt−1+ηtw\_{t}=\lambda w\_{t-1}+\eta\_{t} and, since 𝜺t⟂ℋt−1{\mbox{$\varepsilon$}}\_{t}\perp\mathscr{H}\_{t-1}, ηt\eta\_{t} is uncorrelated with wt−1w\_{t-1}, so

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[wt2]=|λ|2​𝔼​[wt−12]+𝔼​[ηt2].{\mathbb{E}}[w\_{t}^{2}]=|\lambda|^{2}{\mathbb{E}}[w\_{t-1}^{2}]+{\mathbb{E}}[\eta\_{t}^{2}]. |  |

By stationarity 𝔼[wt2]=𝔼[wt−12]=:σw2{\mathbb{E}}[w\_{t}^{2}]={\mathbb{E}}[w\_{t-1}^{2}]=:\sigma\_{w}^{2}, hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−|λ|2)​σw2=𝔼​[ηt2]=𝒗′​𝑮​𝚺​𝑮′​𝒗.(1-|\lambda|^{2})\,\sigma\_{w}^{2}={\mathbb{E}}[\eta\_{t}^{2}]={\mbox{$v$}}^{\prime}{\mbox{$G$}}\,{\mbox{$\Sigma$}}\,{\mbox{$G$}}^{\prime}{\mbox{$v$}}. |  | (37) |

Write 𝒗′=(𝒗1′,…,𝒗p′){\mbox{$v$}}^{\prime}=({\mbox{$v$}}\_{1}^{\prime},\ldots,{\mbox{$v$}}\_{p}^{\prime}) with 𝒗j∈ℝm{\mbox{$v$}}\_{j}\in\mathbb{R}^{m}. From 𝒗′​𝑭=λ​𝒗′{\mbox{$v$}}^{\prime}{\mbox{$F$}}=\lambda{\mbox{$v$}}^{\prime} one checks the block recursions

|  |  |  |
| --- | --- | --- |
|  | 𝒗1′​𝚿1+𝒗2′=λ​𝒗1′,𝒗1′​𝚿2+𝒗3′=λ​𝒗2′,…,𝒗1′​𝚿p=λ​𝒗p′.{\mbox{$v$}}\_{1}^{\prime}{\mbox{$\Psi$}}\_{1}+{\mbox{$v$}}\_{2}^{\prime}=\lambda{\mbox{$v$}}\_{1}^{\prime},\quad{\mbox{$v$}}\_{1}^{\prime}{\mbox{$\Psi$}}\_{2}+{\mbox{$v$}}\_{3}^{\prime}=\lambda{\mbox{$v$}}\_{2}^{\prime},\ \ldots,\ {\mbox{$v$}}\_{1}^{\prime}{\mbox{$\Psi$}}\_{p}=\lambda{\mbox{$v$}}\_{p}^{\prime}. |  |

If 𝒗1′=𝟎{\mbox{$v$}}\_{1}^{\prime}={\mbox{$0$}}, then the block recursions imply successively 𝒗p′=⋯=𝒗2′=𝟎{\mbox{$v$}}\_{p}^{\prime}=\cdots={\mbox{$v$}}\_{2}^{\prime}={\mbox{$0$}}, hence 𝒗=𝟎{\mbox{$v$}}={\mbox{$0$}}, a contradiction. Therefore 𝒗1≠𝟎{\mbox{$v$}}\_{1}\neq{\mbox{$0$}}. Since 𝑮=[𝑰m,𝟎,…,𝟎]′{\mbox{$G$}}=[{\mbox{$I$}}\_{m},\ {\mbox{$0$}},\ldots,{\mbox{$0$}}]^{\prime}, we have ηt=𝒗′​𝑮​𝜺t=𝒗1′​𝜺t\eta\_{t}={\mbox{$v$}}^{\prime}{\mbox{$G$}}\,{\mbox{$\varepsilon$}}\_{t}={\mbox{$v$}}\_{1}^{\prime}{\mbox{$\varepsilon$}}\_{t} and 𝔼​[ηt2]=𝒗1′​𝚺𝒗1>0{\mathbb{E}}[\eta\_{t}^{2}]={\mbox{$v$}}\_{1}^{\prime}{\mbox{$\Sigma$}}{\mbox{$v$}}\_{1}>0.

Moreover 𝒔t−1∈ℋt−1{\mbox{$s$}}\_{t-1}\in\mathscr{H}\_{t-1} and 𝜺t⟂ℋt−1{\mbox{$\varepsilon$}}\_{t}\perp\mathscr{H}\_{t-1}, so

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[wt−1​ηt]=𝒗′​𝔼​[𝒔t−1​𝜺t′]​𝑮′​𝒗=0.{\mathbb{E}}[w\_{t-1}\eta\_{t}]={\mbox{$v$}}^{\prime}\,{\mathbb{E}}[{\mbox{$s$}}\_{t-1}{\mbox{$\varepsilon$}}\_{t}^{\prime}]\,{\mbox{$G$}}^{\prime}{\mbox{$v$}}=0. |  |

From wt=λ​wt−1+ηtw\_{t}=\lambda w\_{t-1}+\eta\_{t} we get (using stationarity 𝔼[wt2]=𝔼[wt−12]=:σw2<∞{\mathbb{E}}[w\_{t}^{2}]={\mathbb{E}}[w\_{t-1}^{2}]=:\sigma\_{w}^{2}<\infty) σw2=𝔼​[wt2]=|λ|2​σw2+𝔼​[ηt2]\sigma\_{w}^{2}={\mathbb{E}}[w\_{t}^{2}]=|\lambda|^{2}\sigma\_{w}^{2}+{\mathbb{E}}[\eta\_{t}^{2}] and (1−|λ|2)​σw2=𝔼​[ηt2](1-|\lambda|^{2})\sigma\_{w}^{2}={\mathbb{E}}[\eta\_{t}^{2}]. The right-hand side is strictly positive, hence 1−|λ|2>01-|\lambda|^{2}>0, i.e. |λ|<1|\lambda|<1. This contradicts the assumption |λ|≥1|\lambda|\geq 1. Therefore the companion matrix 𝑭F has no eigenvalue with modulus ≥1\geq 1; in particular ρ​(𝑭)<1\rho({\mbox{$F$}})<1.

Next, by forward iteration,

|  |  |  |
| --- | --- | --- |
|  | 𝒔t=𝑭k​𝒔t−k+∑j=0k−1𝑭j​𝑮​𝜺t−j.{\mbox{$s$}}\_{t}={\mbox{$F$}}^{k}{\mbox{$s$}}\_{t-k}+\sum\_{j=0}^{k-1}{\mbox{$F$}}^{\,j}{\mbox{$G$}}\,{\mbox{$\varepsilon$}}\_{t-j}. |  |

Since ρ​(𝑭)<1\rho({\mbox{$F$}})<1, by Gelfand’s formula there exist constants M<∞M<\infty and ρ∈(0,1)\rho\in(0,1) such that
‖𝑭j‖≤M​ρj\|{\mbox{$F$}}^{\,j}\|\leq M\rho^{\,j} for all j≥0j\geq 0. Stationarity implies 𝔼​‖𝒔t‖2<∞{\mathbb{E}}\|{\mbox{$s$}}\_{t}\|^{2}<\infty, hence

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖𝑭k​𝒔t−k‖2≤‖𝑭k‖2​𝔼​‖𝒔t−k‖2≤M2​ρ 2​k​𝔼​‖𝒔t‖2→0,as​k→∞,{\mathbb{E}}\|{\mbox{$F$}}^{k}{\mbox{$s$}}\_{t-k}\|^{2}\leq\|{\mbox{$F$}}^{k}\|^{2}\,{\mathbb{E}}\|{\mbox{$s$}}\_{t-k}\|^{2}\leq M^{2}\rho^{\,2k}\,{\mathbb{E}}\|{\mbox{$s$}}\_{t}\|^{2}\ \rightarrow 0,\quad\text{as}\ k\to\infty, |  |

so 𝑭k​𝒔t−k→𝟎{\mbox{$F$}}^{k}{\mbox{$s$}}\_{t-k}\to{\mbox{$0$}} in L2L^{2}. Letting k→∞k\to\infty gives the L2L^{2} expansion

|  |  |  |
| --- | --- | --- |
|  | 𝒔t=∑i=0∞𝑭i​𝑮​𝜺t−i.{\mbox{$s$}}\_{t}=\sum\_{i=0}^{\infty}{\mbox{$F$}}^{\,i}{\mbox{$G$}}\,{\mbox{$\varepsilon$}}\_{t-i}. |  |

Let 𝑱:=[𝑰m,𝟎,…,𝟎]∈ℝm×m​p{\mbox{$J$}}:=[{\mbox{$I$}}\_{m},\ {\mbox{$0$}},\ \ldots,\ {\mbox{$0$}}]\in\mathbb{R}^{m\times mp} be the selector of the first mm-block. Then

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=𝑱𝒔t=∑i=0∞(𝑱𝑭i𝑮)𝜺t−i=:∑i=0∞𝚵i𝜺t−i,𝚵i:=𝑱𝑭i𝑮.\bar{{\mbox{$z$}}}\_{t}={\mbox{$J$}}{\mbox{$s$}}\_{t}=\sum\_{i=0}^{\infty}\big({\mbox{$J$}}{\mbox{$F$}}^{\,i}{\mbox{$G$}}\big)\,{\mbox{$\varepsilon$}}\_{t-i}=:\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{i}\,{\mbox{$\varepsilon$}}\_{t-i},\qquad{\mbox{$\Xi$}}\_{i}:={\mbox{$J$}}{\mbox{$F$}}^{\,i}{\mbox{$G$}}. |  |

Using a submultiplicative operator norm,

|  |  |  |
| --- | --- | --- |
|  | ‖𝚵i‖=‖𝑱𝑭i​𝑮‖≤‖𝑱‖​‖𝑭i‖​‖𝑮‖≤(‖𝑱‖​‖𝑮‖​M)​ρi=M​ρi,\|{\mbox{$\Xi$}}\_{i}\|=\|{\mbox{$J$}}{\mbox{$F$}}^{i}{\mbox{$G$}}\|\ \leq\ \|{\mbox{$J$}}\|\,\|{\mbox{$F$}}^{\,i}\|\,\|{\mbox{$G$}}\|\ \leq\ (\|{\mbox{$J$}}\|\,\|{\mbox{$G$}}\|\,M)\,\rho^{\,i}=M\rho^{i}, |  |

where ‖𝑭i‖≤M​ρi\|{\mbox{$F$}}^{i}\|\leq M\rho^{i} with 0<ρ<10<\rho<1. Since 𝚵0=𝑱𝑮=𝑰m{\mbox{$\Xi$}}\_{0}={\mbox{$J$}}{\mbox{$G$}}={\mbox{$I$}}\_{m},

|  |  |  |
| --- | --- | --- |
|  | ∑i=0∞‖𝚵i‖=‖𝚵0‖+∑i=1∞‖𝚵i‖≤‖𝑰m‖+M​∑i=1∞ρi=1+M​ρ1−ρ<∞.\sum\_{i=0}^{\infty}\|{\mbox{$\Xi$}}\_{i}\|=\|{\mbox{$\Xi$}}\_{0}\|+\sum\_{i=1}^{\infty}\|{\mbox{$\Xi$}}\_{i}\|\ \leq\ \|{\mbox{$I$}}\_{m}\|+M\sum\_{i=1}^{\infty}\rho^{\,i}=1+M\,\frac{\rho}{1-\rho}\ <\ \infty. |  |

Thus the coefficients are absolutely summable. ∎

(iv) By parts (i)–(iii) (from Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")-(A1.1)), the centered process admits the Wold representation

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=∑i=0∞𝚵i​𝜺t−iin ​L2,∑i=0∞‖𝚵i‖<∞,\bar{{\mbox{$z$}}}\_{t}=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{i}{\mbox{$\varepsilon$}}\_{t-i}\quad\text{in }L^{2},\qquad\sum\_{i=0}^{\infty}\|{\mbox{$\Xi$}}\_{i}\|<\infty, |  |

where {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\} is the innovation sequence. Fix r:=4+2​δ>2r:=4+2\delta>2 and set Xi:=𝚵i​𝜺t−iX\_{i}:={\mbox{$\Xi$}}\_{i}{\mbox{$\varepsilon$}}\_{t-i}. Using a submultiplicative operator norm and stationarity of {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\},

|  |  |  |
| --- | --- | --- |
|  | ‖Xi‖Lr=(𝔼​‖𝚵i​𝜺t−i‖r)1/r≤‖𝚵i‖​(𝔼​‖𝜺t‖r)1/r.\|X\_{i}\|\_{L^{r}}=\big({\mathbb{E}}\|{\mbox{$\Xi$}}\_{i}{\mbox{$\varepsilon$}}\_{t-i}\|^{r}\big)^{1/r}\leq\|{\mbox{$\Xi$}}\_{i}\|\big({\mathbb{E}}\|{\mbox{$\varepsilon$}}\_{t}\|^{r}\big)^{1/r}. |  |

Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")-(A1.2) gives 𝔼​‖𝜺t‖r<∞{\mathbb{E}}\|{\mbox{$\varepsilon$}}\_{t}\|^{r}<\infty, and part (iii) gives ∑i=0∞‖𝚵i‖<∞\sum\_{i=0}^{\infty}\|{\mbox{$\Xi$}}\_{i}\|<\infty. By Minkowski’s inequality,

|  |  |  |
| --- | --- | --- |
|  | ‖∑i=0∞𝚵i​𝜺t−i‖Lr≤∑i=0∞‖𝚵i​𝜺t−i‖Lr≤(𝔼​‖𝜺t‖r)1/r​∑i=0∞‖𝚵i‖<∞,\Big\|\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{i}\,{\mbox{$\varepsilon$}}\_{t-i}\Big\|\_{L^{r}}\leq\sum\_{i=0}^{\infty}\|{\mbox{$\Xi$}}\_{i}\,{\mbox{$\varepsilon$}}\_{t-i}\|\_{L^{r}}\leq\big({\mathbb{E}}\|{\mbox{$\varepsilon$}}\_{t}\|^{r}\big)^{1/r}\sum\_{i=0}^{\infty}\|{\mbox{$\Xi$}}\_{i}\|<\infty, |  |

so the series ∑i=0∞𝚵i​𝜺t−i\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{i}{\mbox{$\varepsilon$}}\_{t-i} converges in LrL^{r} and

|  |  |  |
| --- | --- | --- |
|  | ‖𝒛¯t‖Lr=‖∑i=0∞𝚵i​𝜺t−i‖Lr≤(𝔼​‖𝜺t‖r)1/r​∑i=0∞‖𝚵i‖<∞.\|\bar{{\mbox{$z$}}}\_{t}\|\_{L^{r}}=\Big\|\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{i}\,{\mbox{$\varepsilon$}}\_{t-i}\Big\|\_{L^{r}}\leq\big({\mathbb{E}}\|{\mbox{$\varepsilon$}}\_{t}\|^{r}\big)^{1/r}\sum\_{i=0}^{\infty}\|{\mbox{$\Xi$}}\_{i}\|<\infty. |  |

With the selection matrices 𝑱x=[𝑰k,𝟎]{\mbox{$J$}}\_{x}=[{\mbox{$I$}}\_{k},\ {\mbox{$0$}}] and 𝑱u=[𝟎,𝑰N]{\mbox{$J$}}\_{u}=[{\mbox{$0$}},\ {\mbox{$I$}}\_{N}],

|  |  |  |
| --- | --- | --- |
|  | 𝒙t−𝔼​[𝒙t]=𝑱x​𝒛¯t=∑i=0∞(𝑱x​𝚵i)​𝜺t−i,𝒖t=𝑱u​𝒛¯t=∑i=0∞(𝑱u​𝚵i)​𝜺t−i.{\mbox{$x$}}\_{t}-{\mathbb{E}}[{\mbox{$x$}}\_{t}]={\mbox{$J$}}\_{x}\bar{{\mbox{$z$}}}\_{t}=\sum\_{i=0}^{\infty}({\mbox{$J$}}\_{x}{\mbox{$\Xi$}}\_{i}){\mbox{$\varepsilon$}}\_{t-i},\qquad{\mbox{$u$}}\_{t}={\mbox{$J$}}\_{u}\bar{{\mbox{$z$}}}\_{t}=\sum\_{i=0}^{\infty}({\mbox{$J$}}\_{u}{\mbox{$\Xi$}}\_{i}){\mbox{$\varepsilon$}}\_{t-i}. |  |

Since ‖𝑱x​𝚵i‖≤‖𝑱x‖​‖𝚵i‖\|{\mbox{$J$}}\_{x}{\mbox{$\Xi$}}\_{i}\|\leq\|{\mbox{$J$}}\_{x}\|\,\|{\mbox{$\Xi$}}\_{i}\| and similarly for 𝑱u{\mbox{$J$}}\_{u}, the same argument yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖𝒙t−𝔼​[𝒙t]‖r<∞,𝔼​‖𝒖t‖r<∞.{\mathbb{E}}\|{\mbox{$x$}}\_{t}-{\mathbb{E}}[{\mbox{$x$}}\_{t}]\|^{r}<\infty,\qquad{\mathbb{E}}\|{\mbox{$u$}}\_{t}\|^{r}<\infty. |  |

Since adding constants does not affect finiteness of rr-th moments, we conclude
𝔼​‖𝒙t‖r<∞{\mathbb{E}}\|{\mbox{$x$}}\_{t}\|^{r}<\infty and 𝔼​‖𝒖t‖r<∞{\mathbb{E}}\|{\mbox{$u$}}\_{t}\|^{r}<\infty.

Write 𝒚t=𝜶+𝑿t′​𝜷+𝒖t{\mbox{$y$}}\_{t}={\mbox{$\alpha$}}+{\mbox{$X$}}\_{t}^{\prime}{\mbox{$\beta$}}+{\mbox{$u$}}\_{t} and define 𝑩:=diag(𝜷1′,…,𝜷N′){\mbox{$B$}}:=\operatorname\*{diag}({\mbox{$\beta$}}\_{1}^{\prime},\ldots,{\mbox{$\beta$}}\_{N}^{\prime}) so that 𝑿t′​𝜷=𝑩𝒙t{\mbox{$X$}}\_{t}^{\prime}{\mbox{$\beta$}}={\mbox{$B$}}{\mbox{$x$}}\_{t}. Then

|  |  |  |
| --- | --- | --- |
|  | ‖𝒚t‖≤‖𝜶‖+‖𝑩‖​‖𝒙t‖+‖𝒖t‖.\|{\mbox{$y$}}\_{t}\|\leq\|{\mbox{$\alpha$}}\|+\|{\mbox{$B$}}\|\|{\mbox{$x$}}\_{t}\|+\|{\mbox{$u$}}\_{t}\|. |  |

By the Hölder’s inequality,

|  |  |  |
| --- | --- | --- |
|  | ‖𝒚t‖r≤3r−1​(‖𝜶‖r+‖𝑩‖r​‖𝒙t‖r+‖𝒖t‖r)\|{\mbox{$y$}}\_{t}\|^{r}\leq 3^{r-1}\big(\|{\mbox{$\alpha$}}\|^{r}+\|{\mbox{$B$}}\|^{r}\|{\mbox{$x$}}\_{t}\|^{r}+\|{\mbox{$u$}}\_{t}\|^{r}\big) |  |

so 𝔼​‖𝒚t‖r<∞{\mathbb{E}}\|{\mbox{$y$}}\_{t}\|^{r}<\infty follows from the already established finiteness of 𝔼​‖𝒙t‖r{\mathbb{E}}\|{\mbox{$x$}}\_{t}\|^{r} and 𝔼​‖𝒖t‖r{\mathbb{E}}\|{\mbox{$u$}}\_{t}\|^{r}.

For ℓ≥0\ell\geq 0,

|  |  |  |
| --- | --- | --- |
|  | ℂ​ov​(𝒛t,𝒛t−ℓ)=∑i=0∞∑j=0∞𝚵i​𝔼​[𝜺t−i​𝜺t−ℓ−j′]​𝚵j′=∑j=0∞𝚵ℓ+j​𝚺𝚵j′,{\mathbb{C}\rm{ov}}({\mbox{$z$}}\_{t},{\mbox{$z$}}\_{t-\ell})=\sum\_{i=0}^{\infty}\sum\_{j=0}^{\infty}{\mbox{$\Xi$}}\_{i}{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t-i}{\mbox{$\varepsilon$}}\_{t-\ell-j}^{\prime}]{\mbox{$\Xi$}}\_{j}^{\prime}=\sum\_{j=0}^{\infty}{\mbox{$\Xi$}}\_{\ell+j}{\mbox{$\Sigma$}}{\mbox{$\Xi$}}\_{j}^{\prime}, |  |

which depends only on ℓ\ell. Moreover,

|  |  |  |
| --- | --- | --- |
|  | ‖ℂ​ov​(𝒛t,𝒛t−ℓ)‖≤‖𝚺‖​∑j=0∞‖𝚵ℓ+j‖​‖𝚵j‖≤‖𝚺‖​(∑n=0∞‖𝚵n‖)2<∞.\big\|{\mathbb{C}\rm{ov}}({\mbox{$z$}}\_{t},{\mbox{$z$}}\_{t-\ell})\big\|\leq\|{\mbox{$\Sigma$}}\|\sum\_{j=0}^{\infty}\|{\mbox{$\Xi$}}\_{\ell+j}\|\|{\mbox{$\Xi$}}\_{j}\|\leq\|{\mbox{$\Sigma$}}\|\Big(\sum\_{n=0}^{\infty}\|{\mbox{$\Xi$}}\_{n}\|\Big)^{2}<\infty. |  |

Hence {𝒛¯t}\{\bar{{\mbox{$z$}}}\_{t}\} is covariance-stationary. Since 𝒙t=𝑱x​𝒛t{\mbox{$x$}}\_{t}={\mbox{$J$}}\_{x}{\mbox{$z$}}\_{t} and 𝒖t=𝑱u​𝒛t{\mbox{$u$}}\_{t}={\mbox{$J$}}\_{u}{\mbox{$z$}}\_{t}, both {𝒙t}\{{\mbox{$x$}}\_{t}\} and {𝒖t}\{{\mbox{$u$}}\_{t}\} (and thus {𝒚t}\{{\mbox{$y$}}\_{t}\}) are covariance-stationary as fixed linear images of {𝒛t}\{{\mbox{$z$}}\_{t}\}.

By Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")-(A1.2), the innovation sequence {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\} is strongly mixing with coefficients αε​(ℓ)\alpha\_{\varepsilon}(\ell) such that ∑ℓ≥1αε​(ℓ)δ/(2+δ)<∞\sum\_{\ell\geq 1}\alpha\_{\varepsilon}(\ell)^{\delta/(2+\delta)}<\infty and has finite (4+2​δ)(4+2\delta)-th moments. Consider the mm-truncated linear process

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t(m):=∑i=0m𝚵i​𝜺t−i.\bar{{\mbox{$z$}}}\_{t}^{(m)}:=\sum\_{i=0}^{m}{\mbox{$\Xi$}}\_{i}{\mbox{$\varepsilon$}}\_{t-i}. |  |

Then 𝒛¯t(m)\bar{{\mbox{$z$}}}\_{t}^{(m)} is a measurable function of (𝜺t,…,𝜺t−m)({\mbox{$\varepsilon$}}\_{t},\ldots,{\mbox{$\varepsilon$}}\_{t-m}), and hence is strongly mixing with

|  |  |  |
| --- | --- | --- |
|  | αz(m)​(ℓ)≤αε​(ℓ−m)(ℓ>m),\alpha\_{z^{(m)}}(\ell)\leq\alpha\_{\varepsilon}(\ell-m)\quad(\ell>m), |  |

because σ​(𝒛¯−∞(m),0)⊂σ​(𝜺−∞0)\sigma(\bar{{\mbox{$z$}}}\_{-\infty}^{(m),0})\subset\sigma({\mbox{$\varepsilon$}}\_{-\infty}^{0}) and σ​(𝒛¯ℓ(m),∞)⊂σ​(𝜺ℓ−m∞)\sigma(\bar{{\mbox{$z$}}}\_{\ell}^{(m),\infty})\subset\sigma({\mbox{$\varepsilon$}}\_{\ell-m}^{\infty}). Moreover, by Minkowski’s inequality and ∑i=0∞‖𝚵i‖<∞\sum\_{i=0}^{\infty}\|{\mbox{$\Xi$}}\_{i}\|<\infty,

|  |  |  |
| --- | --- | --- |
|  | ‖𝒛¯t−𝒛¯t(m)‖L4+2​δ≤∑i>m‖𝚵i‖​(𝔼​‖𝜺t‖4+2​δ)1/(4+2​δ)→m→∞ 0.\|\bar{{\mbox{$z$}}}\_{t}-\bar{{\mbox{$z$}}}\_{t}^{(m)}\|\_{L^{4+2\delta}}\leq\sum\_{i>m}\|{\mbox{$\Xi$}}\_{i}\|\big({\mathbb{E}}\|{\mbox{$\varepsilon$}}\_{t}\|^{4+2\delta}\big)^{1/(4+2\delta)}\ \xrightarrow{m\to\infty}\ 0. |  |

Standard approximation arguments for strongly mixing sequences (via mm-dependent truncation and comparison inequalities for mixing coefficients) yield: there exist constants C>0C>0 and θ∈(0,1)\theta\in(0,1) (depending only on 4+2​δ4+2\delta) such that, for ℓ>2​m\ell>2m,

|  |  |  |
| --- | --- | --- |
|  | αz​(ℓ)≤αz(m)​(ℓ−m)+C​‖𝒛¯t−𝒛¯t(m)‖L4+2​δθ.\alpha\_{z}(\ell)\ \leq\ \alpha\_{z^{(m)}}(\ell-m)\ +\ C\,\|\bar{{\mbox{$z$}}}\_{t}-\bar{{\mbox{$z$}}}\_{t}^{(m)}\|\_{L^{4+2\delta}}^{\theta}. |  |

Choosing m=⌊ℓ/4⌋m=\lfloor\ell/4\rfloor gives

|  |  |  |
| --- | --- | --- |
|  | αz​(ℓ)≤αε​(ℓ/2)+C​(∑i>ℓ/4∞‖𝚵i‖)θ.\alpha\_{z}(\ell)\ \leq\ \alpha\_{\varepsilon}(\ell/2)\ +\ C\,\Big(\sum\_{i>\ell/4}^{\infty}\|{\mbox{$\Xi$}}\_{i}\|\Big)^{\theta}. |  |

By part (iii), the stability of 𝑷​(L){\mbox{$P$}}(L) implies the existence of C′>0C^{\prime}>0 and ρ∈(0,1)\rho\in(0,1) such that ‖𝚵i‖≤C′​ρi\|{\mbox{$\Xi$}}\_{i}\|\leq C^{\prime}\rho^{i} (geometric decay of the impulse responses). Hence

|  |  |  |
| --- | --- | --- |
|  | ∑ℓ=1∞αz​(ℓ)δ/(2+δ)≤C​∑ℓ=1∞αε​(ℓ/2)δ/(2+δ)+C​∑ℓ=1∞(C′​ρℓ/4)θ​δ/(2+δ)<∞.\sum\_{\ell=1}^{\infty}\alpha\_{z}(\ell)^{\delta/(2+\delta)}\ \leq\ C\sum\_{\ell=1}^{\infty}\alpha\_{\varepsilon}(\ell/2)^{\delta/(2+\delta)}\ +\ C\sum\_{\ell=1}^{\infty}\big(C^{\prime}\rho^{\ell/4}\big)^{\theta\delta/(2+\delta)}\ <\ \infty. |  |

Finally, (𝒚t,𝒙t,𝒖t)({\mbox{$y$}}\_{t},{\mbox{$x$}}\_{t},{\mbox{$u$}}\_{t}) are fixed linear transforms of 𝒛t{\mbox{$z$}}\_{t}, and 𝑿t{\mbox{$X$}}\_{t} is a deterministic function of 𝒙t{\mbox{$x$}}\_{t}. Hence,

|  |  |  |
| --- | --- | --- |
|  | α(y,X,u)​(ℓ)≤αz​(ℓ)and∑ℓ=1∞α(y,X,u)​(ℓ)δ/(2+δ)<∞.\alpha\_{(y,X,u)}(\ell)\ \leq\ \alpha\_{z}(\ell)\qquad\text{and}\qquad\sum\_{\ell=1}^{\infty}\alpha\_{(y,X,u)}(\ell)^{\delta/(2+\delta)}<\infty. |  |

Since strong mixing implies ergodicity, the claim follows. ∎

### A.2 Proof of Proposition2

(i) strict exogeneity ⇔\Leftrightarrow B​DBD

#### strict exogeneity ⇒\Rightarrow B​DBD

We first show that (a covariance-based notion of) strict exogeneity implies the B​DBD condition. Throughout this subsection, by strict exogeneity we mean

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒖t​𝒙s′]=𝟎for all ​t,s∈ℤ.{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{s}^{\prime}]={\mbox{$0$}}\quad\text{for all }t,s\in\mathbb{Z}. |  |

Let 𝒙¯t:=𝒙t−𝝁x\bar{{\mbox{$x$}}}\_{t}:={\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x} and 𝒛¯t:=(𝒙¯t′,𝒖t′)′\bar{{\mbox{$z$}}}\_{t}:=(\bar{{\mbox{$x$}}}\_{t}^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime}.

##### Step 1: Orthogonality of the closed linear spans.

Define the closed linear subspaces of L2​(Ω,ℱ,ℙ;ℝm)L^{2}(\Omega,\mathscr{F},\mathbb{P};\mathbb{R}^{m}) by

|  |  |  |
| --- | --- | --- |
|  | ℋx:=span¯​{𝒙¯t:t∈ℤ},ℋu:=span¯​{𝒖t:t∈ℤ},ℋz:=span¯​{𝒛¯t:t∈ℤ}.\mathscr{H}\_{x}:=\overline{\operatorname{span}}\{\bar{{\mbox{$x$}}}\_{t}:t\in\mathbb{Z}\},\quad\mathscr{H}\_{u}:=\overline{\operatorname{span}}\{{\mbox{$u$}}\_{t}:t\in\mathbb{Z}\},\quad\mathscr{H}\_{z}:=\overline{\operatorname{span}}\{\bar{{\mbox{$z$}}}\_{t}:t\in\mathbb{Z}\}. |  |

For finite index sets S,T⊂ℤS,T\subset\mathbb{Z}, consider the finite linear combinations

|  |  |  |
| --- | --- | --- |
|  | hx=∑s∈S𝒂s′​𝒙¯s,hu=∑t∈T𝒃t′​𝒖t.h\_{x}=\sum\_{s\in S}{\mbox{$a$}}\_{s}^{\prime}\bar{{\mbox{$x$}}}\_{s},\quad h\_{u}=\sum\_{t\in T}{\mbox{$b$}}\_{t}^{\prime}{\mbox{$u$}}\_{t}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | ⟨hx,hu⟩:=𝔼​[hx​hu]=∑s∈S∑t∈T𝒂s′​𝔼​[𝒙¯s​𝒖t′]​𝒃t.\langle h\_{x},h\_{u}\rangle:={\mathbb{E}}[h\_{x}h\_{u}]=\sum\_{s\in S}\sum\_{t\in T}{\mbox{$a$}}\_{s}^{\prime}\,{\mathbb{E}}[\bar{{\mbox{$x$}}}\_{s}{\mbox{$u$}}\_{t}^{\prime}]\,{\mbox{$b$}}\_{t}. |  |

Since 𝔼​[𝒙¯s​𝒖t′]=𝔼​[(𝒙s−𝝁x)​𝒖t′]=𝔼​[𝒙s​𝒖t′]−𝝁x​𝔼​[𝒖t′]=𝟎{\mathbb{E}}[\bar{{\mbox{$x$}}}\_{s}{\mbox{$u$}}\_{t}^{\prime}]={\mathbb{E}}[({\mbox{$x$}}\_{s}-{\mbox{$\mu$}}\_{x}){\mbox{$u$}}\_{t}^{\prime}]={\mathbb{E}}[{\mbox{$x$}}\_{s}{\mbox{$u$}}\_{t}^{\prime}]-{\mbox{$\mu$}}\_{x}{\mathbb{E}}[{\mbox{$u$}}\_{t}^{\prime}]={\mbox{$0$}} under strict exogeneity and 𝔼​[𝒖t]=𝟎{\mathbb{E}}[{\mbox{$u$}}\_{t}]={\mbox{$0$}}, we obtain ⟨hx,hu⟩=0\langle h\_{x},h\_{u}\rangle=0 for all such finite linear combinations. By continuity of the inner product with respect to the L2L^{2}-norm, this orthogonality extends to the closures, so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋx⟂ℋu.\mathscr{H}\_{x}\perp\mathscr{H}\_{u}. |  | (38) |

Moreover, since 𝒛¯t=(𝒙¯t′,𝒖t′)′\bar{{\mbox{$z$}}}\_{t}=(\bar{{\mbox{$x$}}}\_{t}^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋz=span¯​(ℋx∪ℋu)=ℋx⊕ℋu.\mathscr{H}\_{z}=\overline{\operatorname{span}}(\mathscr{H}\_{x}\cup\mathscr{H}\_{u})=\mathscr{H}\_{x}\oplus\mathscr{H}\_{u}. |  | (39) |

##### Step 2: Innovation decomposition and block-diagonal innovation covariance.

For each tt, define the past closed linear spans (consistent with Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) by

|  |  |  |
| --- | --- | --- |
|  | ℋt−1:=span¯​{𝒛¯t−1,𝒛¯t−2,…},ℋx,t−1:=span¯​{𝒙¯t−1,𝒙¯t−2,…},ℋu,t−1:=span¯​{𝒖t−1,𝒖t−2,…}.\mathscr{H}\_{t-1}:=\overline{\operatorname{span}}\{\bar{{\mbox{$z$}}}\_{t-1},\bar{{\mbox{$z$}}}\_{t-2},\ldots\},\quad\mathscr{H}\_{x,t-1}:=\overline{\operatorname{span}}\{\bar{{\mbox{$x$}}}\_{t-1},\bar{{\mbox{$x$}}}\_{t-2},\ldots\},\quad\mathscr{H}\_{u,t-1}:=\overline{\operatorname{span}}\{{\mbox{$u$}}\_{t-1},{\mbox{$u$}}\_{t-2},\ldots\}. |  |

Then ([39](https://arxiv.org/html/2601.21272v1#Sx2.E39 "In Step 1: Orthogonality of the closed linear spans. ‣ strict exogeneity ⇒ 𝐵⁢𝐷 ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋt−1=ℋx,t−1⊕ℋu,t−1.\mathscr{H}\_{t-1}=\mathscr{H}\_{x,t-1}\oplus\mathscr{H}\_{u,t-1}. |  | (40) |

Let 𝒫t−1:L2→ℋt−1\mathscr{P}\_{t-1}:L^{2}\to\mathscr{H}\_{t-1} be the L2L^{2}-orthogonal projection and define the innovation

|  |  |  |
| --- | --- | --- |
|  | 𝜺t:=𝒛¯t−𝒫t−1​[𝒛¯t].{\mbox{$\varepsilon$}}\_{t}:=\bar{{\mbox{$z$}}}\_{t}-\mathscr{P}\_{t-1}[\bar{{\mbox{$z$}}}\_{t}]. |  |

Because ([40](https://arxiv.org/html/2601.21272v1#Sx2.E40 "In Step 2: Innovation decomposition and block-diagonal innovation covariance. ‣ strict exogeneity ⇒ 𝐵⁢𝐷 ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is an orthogonal direct sum, the projection respects this decomposition:

|  |  |  |
| --- | --- | --- |
|  | 𝒫t−1=𝒫x,t−1⊕𝒫u,t−1,\mathscr{P}\_{t-1}=\mathscr{P}\_{x,t-1}\oplus\mathscr{P}\_{u,t-1}, |  |

where 𝒫x,t−1:L2→ℋx,t−1\mathscr{P}\_{x,t-1}:L^{2}\to\mathscr{H}\_{x,t-1} and 𝒫u,t−1:L2→ℋu,t−1\mathscr{P}\_{u,t-1}:L^{2}\to\mathscr{H}\_{u,t-1} are the corresponding orthogonal projections. Hence

|  |  |  |
| --- | --- | --- |
|  | 𝜺t=[𝒙¯t−𝒫x,t−1​[𝒙¯t]𝒖t−𝒫u,t−1​[𝒖t]]=:[𝜺x,t𝜺u,t],{\mbox{$\varepsilon$}}\_{t}=\begin{bmatrix}\bar{{\mbox{$x$}}}\_{t}-\mathscr{P}\_{x,t-1}[\bar{{\mbox{$x$}}}\_{t}]\\ {\mbox{$u$}}\_{t}-\mathscr{P}\_{u,t-1}[{\mbox{$u$}}\_{t}]\end{bmatrix}=:\begin{bmatrix}{\mbox{$\varepsilon$}}\_{x,t}\\ {\mbox{$\varepsilon$}}\_{u,t}\end{bmatrix}, |  |

with 𝜺x,t∈ℋx{\mbox{$\varepsilon$}}\_{x,t}\in\mathscr{H}\_{x} and 𝜺u,t∈ℋu{\mbox{$\varepsilon$}}\_{u,t}\in\mathscr{H}\_{u}. By ([38](https://arxiv.org/html/2601.21272v1#Sx2.E38 "In Step 1: Orthogonality of the closed linear spans. ‣ strict exogeneity ⇒ 𝐵⁢𝐷 ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")),

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝜺x,t​𝜺u,t′]=𝟎for all ​t,{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{x,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$0$}}\quad\text{for all }t, |  |

so the innovation covariance matrix is block diagonal:

|  |  |  |
| --- | --- | --- |
|  | 𝚺:=𝔼​[𝜺t​𝜺t′]=[𝚺x​x𝟎𝟎𝚺u​u].{\mbox{$\Sigma$}}:={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{t}^{\prime}]=\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Sigma$}}\_{uu}\end{bmatrix}. |  |

##### Step 3: Block-diagonality of the VMA coefficients.

By Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(i), 𝒛¯t\bar{{\mbox{$z$}}}\_{t} admits the unique Wold representation

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=∑i=0∞𝚵i​𝜺t−iin ​L2,𝚵i=[𝚵x​x,i𝚵x​u,i𝚵u​x,i𝚵u​u,i].\bar{{\mbox{$z$}}}\_{t}=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{i}{\mbox{$\varepsilon$}}\_{t-i}\quad\text{in }L^{2},\qquad{\mbox{$\Xi$}}\_{i}=\begin{bmatrix}{\mbox{$\Xi$}}\_{xx,i}&{\mbox{$\Xi$}}\_{xu,i}\\ {\mbox{$\Xi$}}\_{ux,i}&{\mbox{$\Xi$}}\_{uu,i}\end{bmatrix}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | 𝒙¯t=∑i=0∞(𝚵x​x,i​𝜺x,t−i+𝚵x​u,i​𝜺u,t−i),𝒖t=∑i=0∞(𝚵u​x,i​𝜺x,t−i+𝚵u​u,i​𝜺u,t−i).\bar{{\mbox{$x$}}}\_{t}=\sum\_{i=0}^{\infty}\big({\mbox{$\Xi$}}\_{xx,i}{\mbox{$\varepsilon$}}\_{x,t-i}+{\mbox{$\Xi$}}\_{xu,i}{\mbox{$\varepsilon$}}\_{u,t-i}\big),\qquad{\mbox{$u$}}\_{t}=\sum\_{i=0}^{\infty}\big({\mbox{$\Xi$}}\_{ux,i}{\mbox{$\varepsilon$}}\_{x,t-i}+{\mbox{$\Xi$}}\_{uu,i}{\mbox{$\varepsilon$}}\_{u,t-i}\big). |  |

Define

|  |  |  |
| --- | --- | --- |
|  | 𝒗t:=∑i=0∞𝚵x​u,i​𝜺u,t−i.{\mbox{$v$}}\_{t}:=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{xu,i}{\mbox{$\varepsilon$}}\_{u,t-i}. |  |

Since each 𝜺u,t−i∈ℋu{\mbox{$\varepsilon$}}\_{u,t-i}\in\mathscr{H}\_{u} and ℋu\mathscr{H}\_{u} is a closed linear subspace, we have 𝒗t∈ℋu{\mbox{$v$}}\_{t}\in\mathscr{H}\_{u}. On the other hand, 𝒙¯t∈ℋx\bar{{\mbox{$x$}}}\_{t}\in\mathscr{H}\_{x} and ∑i=0∞𝚵x​x,i​𝜺x,t−i∈ℋx\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{xx,i}{\mbox{$\varepsilon$}}\_{x,t-i}\in\mathscr{H}\_{x}, hence

|  |  |  |
| --- | --- | --- |
|  | 𝒗t=𝒙¯t−∑i=0∞𝚵x​x,i​𝜺x,t−i∈ℋx.{\mbox{$v$}}\_{t}=\bar{{\mbox{$x$}}}\_{t}-\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{xx,i}{\mbox{$\varepsilon$}}\_{x,t-i}\in\mathscr{H}\_{x}. |  |

Therefore 𝒗t∈ℋx∩ℋu{\mbox{$v$}}\_{t}\in\mathscr{H}\_{x}\cap\mathscr{H}\_{u}. By ([38](https://arxiv.org/html/2601.21272v1#Sx2.E38 "In Step 1: Orthogonality of the closed linear spans. ‣ strict exogeneity ⇒ 𝐵⁢𝐷 ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")), ℋx∩ℋu={𝟎}\mathscr{H}\_{x}\cap\mathscr{H}\_{u}=\{{\mbox{$0$}}\}, so 𝒗t=𝟎{\mbox{$v$}}\_{t}={\mbox{$0$}} in L2L^{2}, i.e. 𝒗t=𝟎{\mbox{$v$}}\_{t}={\mbox{$0$}} a.s.

For any h≥0h\geq 0, using that {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\} is white noise and 𝔼​[𝜺u,t​𝜺u,t′]=𝚺u​u{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$\Sigma$}}\_{uu}, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝟎=ℂ​ov​(𝒗t,𝜺u,t−h)=∑i=0∞𝚵x​u,i​ℂ​ov​(𝜺u,t−i,𝜺u,t−h)=𝚵x​u,h​𝚺u​u.{\mbox{$0$}}={\mathbb{C}\rm{ov}}({\mbox{$v$}}\_{t},{\mbox{$\varepsilon$}}\_{u,t-h})=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{xu,i}\,{\mathbb{C}\rm{ov}}({\mbox{$\varepsilon$}}\_{u,t-i},{\mbox{$\varepsilon$}}\_{u,t-h})={\mbox{$\Xi$}}\_{xu,h}{\mbox{$\Sigma$}}\_{uu}. |  |

Since 𝚺u​u≻0{\mbox{$\Sigma$}}\_{uu}\succ 0 (as a principal submatrix of 𝚺≻0{\mbox{$\Sigma$}}\succ 0), it follows that 𝚵x​u,h=𝟎{\mbox{$\Xi$}}\_{xu,h}={\mbox{$0$}} for all h≥0h\geq 0. By the same argument applied to ∑i=0∞𝚵u​x,i​𝜺x,t−i\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{ux,i}{\mbox{$\varepsilon$}}\_{x,t-i}, we also have 𝚵u​x,i=𝟎{\mbox{$\Xi$}}\_{ux,i}={\mbox{$0$}} for all i≥0i\geq 0.
Hence each 𝚵i{\mbox{$\Xi$}}\_{i} is block diagonal.

##### Step 4: Block-diagonality of the VAR coefficients.

By Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(ii)–(iii), 𝒛¯t\bar{{\mbox{$z$}}}\_{t} admits a stable VAR(p0p\_{0}) representation and

|  |  |  |
| --- | --- | --- |
|  | 𝚿​(L)​𝚵​(L)=𝑰m,𝚿​(L):=𝑰m−∑j=1p0𝚿j​Lj,𝚵​(L):=𝑰m+∑i=1∞𝚵i​Li.{\mbox{$\Psi$}}(L){\mbox{$\Xi$}}(L)={\mbox{$I$}}\_{m},\qquad{\mbox{$\Psi$}}(L):={\mbox{$I$}}\_{m}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{j}L^{j},\quad{\mbox{$\Xi$}}(L):={\mbox{$I$}}\_{m}+\sum\_{i=1}^{\infty}{\mbox{$\Xi$}}\_{i}L^{i}. |  |

Since each 𝚵i{\mbox{$\Xi$}}\_{i} is block diagonal, 𝚵​(L){\mbox{$\Xi$}}(L) is block diagonal, and so is its inverse 𝚿​(L)=𝚵​(L)−1{\mbox{$\Psi$}}(L)={\mbox{$\Xi$}}(L)^{-1}. Therefore each VAR coefficient 𝚿j{\mbox{$\Psi$}}\_{j} is block diagonal. Together with the block-diagonal innovation covariance matrix 𝚺\Sigma, we conclude that strict exogeneity implies the B​DBD condition. ∎

#### B​DBD ⇒\Rightarrow strict exogeneity

We next show that the B​DBD condition implies strict exogeneity in the covariance sense, that is,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒖t​𝒙s′]=𝟎for all ​s,t∈ℤ.{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{s}^{\prime}]={\mbox{$0$}}\quad\text{for all }s,t\in\mathbb{Z}. |  |

Suppose that the B​DBD condition holds. Then, by Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") and Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), the marginal processes {𝒙¯t}\{\bar{{\mbox{$x$}}}\_{t}\} and {𝒖t}\{{\mbox{$u$}}\_{t}\} are covariance-stationary and purely nondeterministic, and (since the VAR coefficients and innovation covariance matrix are block diagonal) each admits its own Wold VMA(∞\infty) representation driven by the corresponding innovation block. In particular, there exist coefficient matrices {𝚵x​x,i}i≥0\{{\mbox{$\Xi$}}\_{xx,i}\}\_{i\geq 0} and {𝚵u​u,i}i≥0\{{\mbox{$\Xi$}}\_{uu,i}\}\_{i\geq 0} such that

|  |  |  |
| --- | --- | --- |
|  | 𝒙¯t=∑i=0∞𝚵x​x,i​𝜺x,t−i,𝒖t=∑i=0∞𝚵u​u,i​𝜺u,t−i,\bar{{\mbox{$x$}}}\_{t}=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{xx,i}\,{\mbox{$\varepsilon$}}\_{x,t-i},\qquad{\mbox{$u$}}\_{t}=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{uu,i}\,{\mbox{$\varepsilon$}}\_{u,t-i}, |  |

where ∑i=0∞‖𝚵x​x,i‖<∞\sum\_{i=0}^{\infty}\|{\mbox{$\Xi$}}\_{xx,i}\|<\infty, ∑i=0∞‖𝚵u​u,i‖<∞\sum\_{i=0}^{\infty}\|{\mbox{$\Xi$}}\_{uu,i}\|<\infty, and
𝚵x​x,0=𝑰k{\mbox{$\Xi$}}\_{xx,0}={\mbox{$I$}}\_{k}, 𝚵u​u,0=𝑰N{\mbox{$\Xi$}}\_{uu,0}={\mbox{$I$}}\_{N}.

The innovation process {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\} is (second-order) white noise, so

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝜺t​𝜺s′]=𝟎for all ​s≠t.{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{s}^{\prime}]={\mbox{$0$}}\quad\text{for all }s\neq t. |  |

Writing

|  |  |  |
| --- | --- | --- |
|  | 𝜺t=[𝜺x,t𝜺u,t],{\mbox{$\varepsilon$}}\_{t}=\begin{bmatrix}{\mbox{$\varepsilon$}}\_{x,t}\\ {\mbox{$\varepsilon$}}\_{u,t}\end{bmatrix}, |  |

the B​DBD condition further implies that the innovation covariance matrix is block diagonal,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝜺t​𝜺t′]=[𝚺x​x𝟎𝟎𝚺u​u],{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{t}^{\prime}]=\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Sigma$}}\_{uu}\end{bmatrix}, |  |

so that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝜺u,t​𝜺x,t′]=𝟎.{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t}{\mbox{$\varepsilon$}}\_{x,t}^{\prime}]={\mbox{$0$}}. |  |

Combining whiteness across time and block diagonality at each tt, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝜺u,r​𝜺x,q′]=𝟎for all ​r,q∈ℤ.{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,r}{\mbox{$\varepsilon$}}\_{x,q}^{\prime}]={\mbox{$0$}}\quad\text{for all }r,q\in\mathbb{Z}. |  | (41) |

Now fix arbitrary t,s∈ℤt,s\in\mathbb{Z}. Using the VMA representations and absolute summability of the coefficient sequences, we can interchange sums and expectations to write

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒖t​𝒙s′]\displaystyle{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{s}^{\prime}] | =𝔼​[(∑i=0∞𝚵u​u,i​𝜺u,t−i)​(∑j=0∞𝚵x​x,j​𝜺x,s−j)′]\displaystyle={\mathbb{E}}\Bigg[\Big(\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{uu,i}\,{\mbox{$\varepsilon$}}\_{u,t-i}\Big)\Big(\sum\_{j=0}^{\infty}{\mbox{$\Xi$}}\_{xx,j}\,{\mbox{$\varepsilon$}}\_{x,s-j}\Big)^{\prime}\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=0∞∑j=0∞𝚵u​u,i​𝔼​[𝜺u,t−i​𝜺x,s−j′]​𝚵x​x,j′.\displaystyle=\sum\_{i=0}^{\infty}\sum\_{j=0}^{\infty}{\mbox{$\Xi$}}\_{uu,i}\,{\mathbb{E}}\big[{\mbox{$\varepsilon$}}\_{u,t-i}{\mbox{$\varepsilon$}}\_{x,s-j}^{\prime}\big]\,{\mbox{$\Xi$}}\_{xx,j}^{\prime}. |  |

By ([41](https://arxiv.org/html/2601.21272v1#Sx2.E41 "In 𝐵⁢𝐷 ⇒ strict exogeneity ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")), each inner expectation vanishes:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝜺u,t−i​𝜺x,s−j′]=𝟎for all ​i,j,{\mathbb{E}}\big[{\mbox{$\varepsilon$}}\_{u,t-i}{\mbox{$\varepsilon$}}\_{x,s-j}^{\prime}\big]={\mbox{$0$}}\quad\text{for all }i,j, |  |

so every term in the double series is zero and hence

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒖t​𝒙s′]=𝟎for all ​s,t∈ℤ.{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{s}^{\prime}]={\mbox{$0$}}\quad\text{for all }s,t\in\mathbb{Z}. |  |

Recalling that 𝔼​[𝒖t]=𝟎{\mathbb{E}}[{\mbox{$u$}}\_{t}]={\mbox{$0$}} and 𝔼​[𝒙s]=𝝁x{\mathbb{E}}[{\mbox{$x$}}\_{s}]={\mbox{$\mu$}}\_{x}, this is equivalent to

|  |  |  |
| --- | --- | --- |
|  | ℂ​ov​(𝒖t,𝒙s)=𝔼​[(𝒖t−𝟎)​(𝒙s−𝝁x)′]=𝔼​[𝒖t​𝒙s′]=𝟎for all ​s,t,{\mathbb{C}\rm{ov}}({\mbox{$u$}}\_{t},{\mbox{$x$}}\_{s})={\mathbb{E}}[({\mbox{$u$}}\_{t}-{\mbox{$0$}})({\mbox{$x$}}\_{s}-{\mbox{$\mu$}}\_{x})^{\prime}]={\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{s}^{\prime}]={\mbox{$0$}}\quad\text{for all }s,t, |  |

which is precisely strict exogeneity in the covariance sense. Therefore, the B​DBD condition implies strict exogeneity. Combining result of strict exogeneity ⇒\Rightarrow B​DBD, the strict exogeneity and B​DBD condition are identical. ∎

(ii) pre-determined = E​B​DEBD

Recall from Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(i) that, under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), the joint process {𝒛t}\{{\mbox{$z$}}\_{t}\} with 𝒛t=(𝒙t′,𝒖t′)′{\mbox{$z$}}\_{t}=({\mbox{$x$}}\_{t}^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime} admits the Wold representation

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=∑i=0∞𝚵i​𝜺t−i,𝚵0=𝑰m,\bar{{\mbox{$z$}}}\_{t}=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{i}{\mbox{$\varepsilon$}}\_{t-i},\qquad{\mbox{$\Xi$}}\_{0}={\mbox{$I$}}\_{m}, |  |

where 𝒛¯t:=𝒛t−𝔼​[𝒛t]\bar{{\mbox{$z$}}}\_{t}:={\mbox{$z$}}\_{t}-{\mathbb{E}}[{\mbox{$z$}}\_{t}], {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\} is a white-noise innovation sequence with 𝔼​[𝜺t]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}]={\mbox{$0$}}, 𝔼​[𝜺t​𝜺s′]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{s}^{\prime}]={\mbox{$0$}} for t≠st\neq s, and 𝚺:=𝔼​[𝜺t​𝜺t′]>0{\mbox{$\Sigma$}}:={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{t}^{\prime}]>0. Partition

|  |  |  |
| --- | --- | --- |
|  | 𝜺t=[𝜺x,t𝜺u,t],𝚺=[𝚺x​x𝚺x​u𝚺u​x𝚺u​u],𝚵i=[𝚵x​x,i𝚵x​u,i𝚵u​x,i𝚵u​u,i].{\mbox{$\varepsilon$}}\_{t}=\begin{bmatrix}{\mbox{$\varepsilon$}}\_{x,t}\\ {\mbox{$\varepsilon$}}\_{u,t}\end{bmatrix},\qquad{\mbox{$\Sigma$}}=\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$\Sigma$}}\_{xu}\\ {\mbox{$\Sigma$}}\_{ux}&{\mbox{$\Sigma$}}\_{uu}\end{bmatrix},\qquad{\mbox{$\Xi$}}\_{i}=\begin{bmatrix}{\mbox{$\Xi$}}\_{xx,i}&{\mbox{$\Xi$}}\_{xu,i}\\ {\mbox{$\Xi$}}\_{ux,i}&{\mbox{$\Xi$}}\_{uu,i}\end{bmatrix}. |  |

Then the first block of the Wold representation can be written as

|  |  |  |
| --- | --- | --- |
|  | 𝒙¯t=∑i=0∞(𝚵x​x,i​𝜺x,t−i+𝚵x​u,i​𝜺u,t−i),\bar{{\mbox{$x$}}}\_{t}=\sum\_{i=0}^{\infty}\bigl({\mbox{$\Xi$}}\_{xx,i}{\mbox{$\varepsilon$}}\_{x,t-i}+{\mbox{$\Xi$}}\_{xu,i}{\mbox{$\varepsilon$}}\_{u,t-i}\bigr), |  |

where 𝒙¯t:=𝒙t−𝝁x\bar{{\mbox{$x$}}}\_{t}:={\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x} and 𝝁x:=𝔼​[𝒙t]{\mbox{$\mu$}}\_{x}:={\mathbb{E}}[{\mbox{$x$}}\_{t}].

We say that the regressors are pre-determined if

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒙t​𝜺u,t+h′]=𝟎for all ​t∈ℤ,h≥0,{\mathbb{E}}[{\mbox{$x$}}\_{t}{\mbox{$\varepsilon$}}\_{u,t+h}^{\prime}]={\mbox{$0$}}\quad\text{for all }t\in\mathbb{Z},\ h\geq 0, |  | (42) |

which is equivalent to ([9](https://arxiv.org/html/2601.21272v1#S2.E9 "In 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")). We say that the E​B​DEBD condition holds if and only if 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} (that is, the innovation covariance matrix is block diagonal).

We now prove that, under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), ([42](https://arxiv.org/html/2601.21272v1#Sx2.E42 "In 𝐵⁢𝐷 ⇒ strict exogeneity ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) holds if and only if 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}.

#### E​B​D⇒EBD\Rightarrow pre-determined.

Suppose that E​B​DEBD holds, i.e. 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}. Since 𝒙t=𝝁x+𝒙¯t{\mbox{$x$}}\_{t}={\mbox{$\mu$}}\_{x}+\bar{{\mbox{$x$}}}\_{t} and 𝔼​[𝜺u,t+h]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t+h}]={\mbox{$0$}}, we have 𝔼​[𝒙t​𝜺u,t+h′]=𝔼​[𝒙¯t​𝜺u,t+h′]{\mathbb{E}}[{\mbox{$x$}}\_{t}{\mbox{$\varepsilon$}}\_{u,t+h}^{\prime}]={\mathbb{E}}[\bar{{\mbox{$x$}}}\_{t}{\mbox{$\varepsilon$}}\_{u,t+h}^{\prime}]. Using the Wold expansion for 𝒙¯t\bar{{\mbox{$x$}}}\_{t} and the absolute summability of {𝚵i}\{{\mbox{$\Xi$}}\_{i}\}, we can interchange expectation and summation to obtain,
for any h≥0h\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒙t​𝜺u,t+h′]\displaystyle{\mathbb{E}}[{\mbox{$x$}}\_{t}{\mbox{$\varepsilon$}}\_{u,t+h}^{\prime}] | =𝔼​[𝒙¯t​𝜺u,t+h′]\displaystyle={\mathbb{E}}[\bar{{\mbox{$x$}}}\_{t}{\mbox{$\varepsilon$}}\_{u,t+h}^{\prime}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=0∞𝚵x​x,i​𝔼​[𝜺x,t−i​𝜺u,t+h′]+∑i=0∞𝚵x​u,i​𝔼​[𝜺u,t−i​𝜺u,t+h′].\displaystyle=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{xx,i}\,{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{x,t-i}{\mbox{$\varepsilon$}}\_{u,t+h}^{\prime}]+\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{xu,i}\,{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t-i}{\mbox{$\varepsilon$}}\_{u,t+h}^{\prime}]. |  |

Because {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\} is white noise, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝜺x,t−i​𝜺u,t+h′]={𝚺x​u,if ​t−i=t+h,𝟎,otherwise,{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{x,t-i}{\mbox{$\varepsilon$}}\_{u,t+h}^{\prime}]=\begin{cases}{\mbox{$\Sigma$}}\_{xu},&\text{if }t-i=t+h,\\ {\mbox{$0$}},&\text{otherwise},\end{cases} |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝜺u,t−i​𝜺u,t+h′]={𝚺u​u,if ​t−i=t+h,𝟎,otherwise.{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t-i}{\mbox{$\varepsilon$}}\_{u,t+h}^{\prime}]=\begin{cases}{\mbox{$\Sigma$}}\_{uu},&\text{if }t-i=t+h,\\ {\mbox{$0$}},&\text{otherwise}.\end{cases} |  |

For h>0h>0, the equalities t−i=t+ht-i=t+h cannot hold for any i≥0i\geq 0, so both matrices are zero for all ii, and hence 𝔼​[𝒙t​𝜺u,t+h′]=𝟎{\mathbb{E}}[{\mbox{$x$}}\_{t}{\mbox{$\varepsilon$}}\_{u,t+h}^{\prime}]={\mbox{$0$}}.

For h=0h=0, the condition t−i=tt-i=t implies i=0i=0, so only the i=0i=0 terms contribute:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒙t​𝜺u,t′]\displaystyle{\mathbb{E}}[{\mbox{$x$}}\_{t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}] | =𝚵x​x,0​𝚺x​u+𝚵x​u,0​𝚺u​u.\displaystyle={\mbox{$\Xi$}}\_{xx,0}\,{\mbox{$\Sigma$}}\_{xu}+{\mbox{$\Xi$}}\_{xu,0}\,{\mbox{$\Sigma$}}\_{uu}. |  |

From 𝚵0=𝑰m{\mbox{$\Xi$}}\_{0}={\mbox{$I$}}\_{m}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝚵0=[𝚵x​x,0𝚵x​u,0𝚵u​x,0𝚵u​u,0]=[𝑰k𝟎𝟎𝑰N],{\mbox{$\Xi$}}\_{0}=\begin{bmatrix}{\mbox{$\Xi$}}\_{xx,0}&{\mbox{$\Xi$}}\_{xu,0}\\ {\mbox{$\Xi$}}\_{ux,0}&{\mbox{$\Xi$}}\_{uu,0}\end{bmatrix}=\begin{bmatrix}{\mbox{$I$}}\_{k}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$I$}}\_{N}\end{bmatrix}, |  |

so that 𝚵x​x,0=𝑰k{\mbox{$\Xi$}}\_{xx,0}={\mbox{$I$}}\_{k} and 𝚵x​u,0=𝟎{\mbox{$\Xi$}}\_{xu,0}={\mbox{$0$}}. Therefore

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒙t​𝜺u,t′]=𝑰k​𝚺x​u+𝟎⋅𝚺u​u=𝚺x​u=𝟎,{\mathbb{E}}[{\mbox{$x$}}\_{t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$I$}}\_{k}\,{\mbox{$\Sigma$}}\_{xu}+{\mbox{$0$}}\cdot{\mbox{$\Sigma$}}\_{uu}={\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}, |  |

where we used the E​B​DEBD restriction 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}. Combining the cases h=0h=0 and h>0h>0 yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒙t​𝜺u,t+h′]=𝟎for all ​h≥0,{\mathbb{E}}[{\mbox{$x$}}\_{t}{\mbox{$\varepsilon$}}\_{u,t+h}^{\prime}]={\mbox{$0$}}\quad\text{for all }h\geq 0, |  |

so the pre-determined condition ([42](https://arxiv.org/html/2601.21272v1#Sx2.E42 "In 𝐵⁢𝐷 ⇒ strict exogeneity ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) holds.

#### pre-determined ⇒E​B​D\Rightarrow EBD.

Conversely, suppose that the pre-determined condition ([42](https://arxiv.org/html/2601.21272v1#Sx2.E42 "In 𝐵⁢𝐷 ⇒ strict exogeneity ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) holds. Taking h=0h=0 and using the same argument as above, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒙t​𝜺u,t′]\displaystyle{\mathbb{E}}[{\mbox{$x$}}\_{t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}] | =∑i=0∞𝚵x​x,i​𝔼​[𝜺x,t−i​𝜺u,t′]+∑i=0∞𝚵x​u,i​𝔼​[𝜺u,t−i​𝜺u,t′]\displaystyle=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{xx,i}\,{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{x,t-i}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]+\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{xu,i}\,{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t-i}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝚵x​x,0​𝚺x​u+𝚵x​u,0​𝚺u​u,\displaystyle={\mbox{$\Xi$}}\_{xx,0}\,{\mbox{$\Sigma$}}\_{xu}+{\mbox{$\Xi$}}\_{xu,0}\,{\mbox{$\Sigma$}}\_{uu}, |  |

where again only the i=0i=0 terms survive by whiteness of {𝜺t}\{{\mbox{$\varepsilon$}}\_{t}\}. Using 𝚵x​x,0=𝑰k{\mbox{$\Xi$}}\_{xx,0}={\mbox{$I$}}\_{k} and 𝚵x​u,0=𝟎{\mbox{$\Xi$}}\_{xu,0}={\mbox{$0$}} as before, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒙t​𝜺u,t′]=𝑰k​𝚺x​u=𝚺x​u.{\mathbb{E}}[{\mbox{$x$}}\_{t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$I$}}\_{k}\,{\mbox{$\Sigma$}}\_{xu}={\mbox{$\Sigma$}}\_{xu}. |  |

By pre-determinedness, the left-hand side is zero, so 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}.

Thus, under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), the innovation-based pre-determined condition ([42](https://arxiv.org/html/2601.21272v1#Sx2.E42 "In 𝐵⁢𝐷 ⇒ strict exogeneity ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) holds if and only if the innovation covariance matrix is block diagonal, that is, if and only if 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}. Equivalently, the pre-determined and E​B​DEBD conditions characterize the same class of data-generating processes. ∎

(iii) B​DBD ⊊\subsetneq (present-and-past exogeneity ∩\cap 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}) ⊊\subsetneq E​B​DEBD

We again work under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), so that Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") applies. Let B​DBD, E​B​DEBD, and “present-and-past exogeneity” denote, respectively, the sets of data-generating processes (DGPs) that satisfy the B​DBD, E​B​DEBD, and covariance-based
present-and-past exogeneity conditions:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒖t​𝒙s′]=𝟎for all ​s≤t.{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{s}^{\prime}]={\mbox{$0$}}\quad\text{for all }s\leq t. |  |

B​DBD ⊆\subseteq {present-and-past exogeneity}\bigl\{\text{present-and-past exogeneity}\bigr\} ∩\cap {𝚺x​u=𝟎}\bigl\{{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}\bigr\}

Under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), we have already shown that strict exogeneity in the covariance sense,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒖t​𝒙s′]=𝟎for all ​s,t∈ℤ,{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{s}^{\prime}]={\mbox{$0$}}\quad\text{for all }s,t\in\mathbb{Z}, |  |

is equivalent to the B​DBD condition (and to pre-determined plus exogenous). Hence B​DBD satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒖t​𝒙s′]=𝟎for all ​s≤t,{\mathbb{E}}[{\mbox{$u$}}\_{t}{\mbox{$x$}}\_{s}^{\prime}]={\mbox{$0$}}\quad\text{for all }s\leq t, |  |

so it belongs to the class of present-and-past exogeneity. Moreover, by definition of B​DBD, the innovation covariance is block diagonal,

|  |  |  |
| --- | --- | --- |
|  | 𝚺=[𝚺x​x𝟎𝟎𝚺u​u],{\mbox{$\Sigma$}}=\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Sigma$}}\_{uu}\end{bmatrix}, |  |

so 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} holds as well. Thus B​DBD ⊆\subseteq {present-and-past exogeneity}\bigl\{\text{present-and-past exogeneity}\bigr\} ∩\cap {𝚺x​u=𝟎}\bigl\{{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}\bigr\}.

To see that the inclusion is strict, we construct a scalar (k=N=1k=N=1) example that belongs to
present-and-past exogeneity with Σx​u=0\Sigma\_{xu}=0 but fails to satisfy B​DBD (equivalently, fails strict exogeneity).

Let {ηt}\{\eta\_{t}\} and {εt}\{\varepsilon\_{t}\} be mutually independent i.i.d. sequences with 𝔼​[ηt]=𝔼​[εt]=0{\mathbb{E}}[\eta\_{t}]={\mathbb{E}}[\varepsilon\_{t}]=0 and strictly positive variances 𝕍​ar​(ηt)=ση2>0{\mathbb{V}\rm{ar}}(\eta\_{t})=\sigma\_{\eta}^{2}>0, 𝕍​ar​(εt)=σε2>0{\mathbb{V}\rm{ar}}(\varepsilon\_{t})=\sigma\_{\varepsilon}^{2}>0. Consider the VAR(1) system

|  |  |  |  |
| --- | --- | --- | --- |
|  | {xt=γ​ut−1+ηt,ut=εt,\begin{cases}x\_{t}=\gamma u\_{t-1}+\eta\_{t},\\ u\_{t}=\varepsilon\_{t},\end{cases} |  | (43) |

with some γ≠0\gamma\neq 0. Define 𝒛t=(xt,ut)′{\mbox{$z$}}\_{t}=(x\_{t},u\_{t})^{\prime} and 𝜺t=(ηt,εt)′{\mbox{$\varepsilon$}}\_{t}=(\eta\_{t},\varepsilon\_{t})^{\prime}. Then ([43](https://arxiv.org/html/2601.21272v1#Sx2.E43 "In pre-determined ⇒𝐸⁢𝐵⁢𝐷. ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) can be written as

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=[0γ00]⏟:=𝚿1​𝒛¯t−1+𝜺t,\bar{{\mbox{$z$}}}\_{t}=\underbrace{\begin{bmatrix}0&\gamma\\ 0&0\end{bmatrix}}\_{:=\,{\mbox{$\Psi$}}\_{1}}\bar{{\mbox{$z$}}}\_{t-1}+{\mbox{$\varepsilon$}}\_{t}, |  |

with innovation covariance

|  |  |  |
| --- | --- | --- |
|  | 𝚺:=𝔼​[𝜺t​𝜺t′]=[ση200σε2].{\mbox{$\Sigma$}}:={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{t}^{\prime}]=\begin{bmatrix}\sigma\_{\eta}^{2}&0\\ 0&\sigma\_{\varepsilon}^{2}\end{bmatrix}. |  |

Thus 𝚺x​u=0{\mbox{$\Sigma$}}\_{xu}=0, so this DGP satisfies the innovation block-diagonality required for B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD.

Next we verify present-and-past exogeneity in the covariance sense. From ([43](https://arxiv.org/html/2601.21272v1#Sx2.E43 "In pre-determined ⇒𝐸⁢𝐵⁢𝐷. ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")),

|  |  |  |
| --- | --- | --- |
|  | ut=εt,xs=γ​us−1+ηs=γ​εs−1+ηs.u\_{t}=\varepsilon\_{t},\qquad x\_{s}=\gamma u\_{s-1}+\eta\_{s}=\gamma\varepsilon\_{s-1}+\eta\_{s}. |  |

If s≤ts\leq t, then s−1≤t−1<ts-1\leq t-1<t, so εs−1\varepsilon\_{s-1} and ηs\eta\_{s} are independent of εt\varepsilon\_{t}. Hence, for all s≤ts\leq t,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ut​xs]=𝔼​[εt​(γ​εs−1+ηs)]=γ​𝔼​[εt​εs−1]+𝔼​[εt​ηs]=0,{\mathbb{E}}[u\_{t}x\_{s}]={\mathbb{E}}\big[\varepsilon\_{t}(\gamma\varepsilon\_{s-1}+\eta\_{s})\big]=\gamma\,{\mathbb{E}}[\varepsilon\_{t}\varepsilon\_{s-1}]+{\mathbb{E}}[\varepsilon\_{t}\eta\_{s}]=0, |  |

because {εt}\{\varepsilon\_{t}\} is white noise and independent of {ηt}\{\eta\_{t}\}. Therefore,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ut​xs]=0∀s≤t,{\mathbb{E}}[u\_{t}x\_{s}]=0\quad\forall\,s\leq t, |  |

so present-and-past exogeneity holds.

However, strict exogeneity fails. Indeed,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ut​xt+1]=𝔼​[εt​(γ​εt+ηt+1)]=γ​𝔼​[εt2]+𝔼​[εt​ηt+1]=γ​σε2≠0{\mathbb{E}}[u\_{t}x\_{t+1}]={\mathbb{E}}\big[\varepsilon\_{t}(\gamma\varepsilon\_{t}+\eta\_{t+1})\big]=\gamma\,{\mathbb{E}}[\varepsilon\_{t}^{2}]+{\mathbb{E}}[\varepsilon\_{t}\eta\_{t+1}]=\gamma\,\sigma\_{\varepsilon}^{2}\neq 0 |  |

whenever γ≠0\gamma\neq 0. Thus the covariance-based strict exogeneity condition 𝔼​[ut​xs]=0{\mathbb{E}}[u\_{t}x\_{s}]=0 for all s,ts,t does not hold, and by the equivalence shown earlier, B​DBD also fails.

Consequently, the DGP ([43](https://arxiv.org/html/2601.21272v1#Sx2.E43 "In pre-determined ⇒𝐸⁢𝐵⁢𝐷. ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) belongs to (present-and-past exogeneity ∩{Σx​u=0}\cap\{\Sigma\_{xu}=0\}) but not to B​DBD, so B​DBD ⊊\subsetneq {present-and-past exogeneity}\bigl\{\text{present-and-past exogeneity}\bigr\} ∩\cap {𝚺x​u=𝟎}\bigl\{{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}\bigr\}.

{present-and-past exogeneity}\bigl\{\text{present-and-past exogeneity}\bigr\} ∩\cap {𝚺x​u=𝟎}\bigl\{{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}\bigr\} ⊆\subseteq E​B​DEBD.

By definition, the E​B​DEBD condition imposes two requirements on the joint process {𝒛t}\{{\mbox{$z$}}\_{t}\}:
The innovation covariance is block diagonal:

|  |  |  |
| --- | --- | --- |
|  | 𝚺=[𝚺x​x𝟎𝟎𝚺u​u],{\mbox{$\Sigma$}}=\begin{bmatrix}{\mbox{$\Sigma$}}\_{xx}&{\mbox{$0$}}\\ {\mbox{$0$}}&{\mbox{$\Sigma$}}\_{uu}\end{bmatrix}, |  |

that is, 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}. The VAR coefficient matrices admit the general block form

|  |  |  |
| --- | --- | --- |
|  | 𝚿j=[𝚿x​x,j𝚿x​u,j𝚿u​x,j𝚿u​u,j],j=1,…,p0,{\mbox{$\Psi$}}\_{j}=\begin{bmatrix}{\mbox{$\Psi$}}\_{xx,j}&{\mbox{$\Psi$}}\_{xu,j}\\ {\mbox{$\Psi$}}\_{ux,j}&{\mbox{$\Psi$}}\_{uu,j}\end{bmatrix},\qquad j=1,\ldots,p\_{0}, |  |

with no additional restrictions on the off-diagonal blocks.

Thus, within the class of DGPs satisfying Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), the E​B​DEBD class is exactly the set of processes for which 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}, together with the (stable) VAR representation of Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"). In particular, any DGP with 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} automatically belongs to E​B​DEBD (regardless of whether present-and-past exogeneity holds). Hence {present-and-past exogeneity}\bigl\{\text{present-and-past exogeneity}\bigr\} ∩\cap {𝚺x​u=𝟎}\bigl\{{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}\bigr\} ⊆\subseteq E​B​DEBD.

To show that the inclusion is strict, it suffices to provide a DGP that satisfies E​B​DEBD but violates present-and-past exogeneity. Consider the scalar (k=N=1k=N=1) VAR(1) system

|  |  |  |  |
| --- | --- | --- | --- |
|  | {xt=ρx​xt−1+α​ut−1+ηt,ut=ρu​ut−1+εu,t,|ρx|<1,|ρu|<1,\begin{cases}x\_{t}=\rho\_{x}x\_{t-1}+\alpha u\_{t-1}+\eta\_{t},\\ u\_{t}=\rho\_{u}u\_{t-1}+\varepsilon\_{u,t},\end{cases}\qquad|\rho\_{x}|<1,\ |\rho\_{u}|<1, |  | (44) |

where {ηt}\{\eta\_{t}\} and {εu,t}\{\varepsilon\_{u,t}\} are mutually independent i.i.d. sequences with zero mean and positive variances. Let 𝒛t=(xt,ut)′{\mbox{$z$}}\_{t}=(x\_{t},u\_{t})^{\prime} and 𝜺t=(ηt,εu,t)′{\mbox{$\varepsilon$}}\_{t}=(\eta\_{t},\varepsilon\_{u,t})^{\prime}. Then ([44](https://arxiv.org/html/2601.21272v1#Sx2.E44 "In pre-determined ⇒𝐸⁢𝐵⁢𝐷. ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) can be written as

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=[ρxα0ρu]​𝒛¯t−1+𝜺t,\bar{{\mbox{$z$}}}\_{t}=\begin{bmatrix}\rho\_{x}&\alpha\\ 0&\rho\_{u}\end{bmatrix}\bar{{\mbox{$z$}}}\_{t-1}+{\mbox{$\varepsilon$}}\_{t}, |  |

with innovation covariance

|  |  |  |
| --- | --- | --- |
|  | 𝚺:=𝔼​[𝜺t​𝜺t′]=[ση200σu2].{\mbox{$\Sigma$}}:={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{t}^{\prime}]=\begin{bmatrix}\sigma\_{\eta}^{2}&0\\ 0&\sigma\_{u}^{2}\end{bmatrix}. |  |

Hence 𝚺x​u=0{\mbox{$\Sigma$}}\_{xu}=0, and the VAR coefficient matrix has the general E​B​DEBD form (with Ψx​u,1=α≠0\Psi\_{xu,1}=\alpha\neq 0 in general), so this DGP belongs to E​B​DEBD.

We now show that present-and-past exogeneity fails. Note that utu\_{t} follows an AR(1) driven by εu,t\varepsilon\_{u,t}, so {ut}\{u\_{t}\} is serially correlated when ρu≠0\rho\_{u}\neq 0. Moreover, xt−1x\_{t-1} contains the lagged error ut−2u\_{t-2} via the term α​ut−2\alpha u\_{t-2}. In the stationary solution of ([44](https://arxiv.org/html/2601.21272v1#Sx2.E44 "In pre-determined ⇒𝐸⁢𝐵⁢𝐷. ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")), utu\_{t} and ut−2u\_{t-2} are correlated whenever ρu≠0\rho\_{u}\neq 0, and hence

|  |  |  |
| --- | --- | --- |
|  | ℂ​ov​(ut,xt−1)=ℂ​ov​(ut,ρx​xt−2+α​ut−2+ηt−1)=α​ℂ​ov​(ut,ut−2)≠0{\mathbb{C}\rm{ov}}(u\_{t},x\_{t-1})={\mathbb{C}\rm{ov}}\big(u\_{t},\rho\_{x}x\_{t-2}+\alpha u\_{t-2}+\eta\_{t-1}\big)=\alpha\,{\mathbb{C}\rm{ov}}(u\_{t},u\_{t-2})\neq 0 |  |

for suitable choices of (ρu,α)(\rho\_{u},\alpha) (e.g. ρu≠0\rho\_{u}\neq 0 and α≠0\alpha\neq 0). Thus
there exists s≤ts\leq t (take s=t−1s=t-1) such that 𝔼​[ut​xs]≠0{\mathbb{E}}[u\_{t}x\_{s}]\neq 0, so the
present-and-past exogeneity condition does not hold.

Therefore, the DGP ([44](https://arxiv.org/html/2601.21272v1#Sx2.E44 "In pre-determined ⇒𝐸⁢𝐵⁢𝐷. ‣ A.2 Proof of Proposition2 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) belongs to E​B​DEBD but not to (present-and-past exogeneity ∩{𝚺x​u=𝟎}\cap\{{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}\}), and we obtain {present-and-past exogeneity}\bigl\{\text{present-and-past exogeneity}\bigr\} ∩\cap {𝚺x​u=𝟎}\bigl\{{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}\bigr\} ⊊\subsetneq E​B​DEBD.

Combining previous results, we have established the strict nesting

|  |  |  |
| --- | --- | --- |
|  | B​D⊊{present-and-past exogeneity}∩{𝚺x​u=𝟎}⊊E​B​D.BD\subsetneq\bigl\{\text{present-and-past exogeneity}\bigr\}\cap\bigl\{{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}\bigr\}\subsetneq EBD. |  |

∎

### A.3 Proof of Proposition3

We work with the regression system in ([14](https://arxiv.org/html/2601.21272v1#S2.E14 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")):

|  |  |  |
| --- | --- | --- |
|  | 𝒚t=𝒁t′​𝜿+𝒖t,𝒁t′=[𝑰N,𝑿t′],𝜿=(𝜶′,𝜷′)′.{\mbox{$y$}}\_{t}={\mbox{$Z$}}\_{t}^{\prime}{\mbox{$\kappa$}}+{\mbox{$u$}}\_{t},\quad{\mbox{$Z$}}\_{t}^{\prime}=[{\mbox{$I$}}\_{N},{\mbox{$X$}}\_{t}^{\prime}],\quad{\mbox{$\kappa$}}=({\mbox{$\alpha$}}^{\prime},{\mbox{$\beta$}}^{\prime})^{\prime}. |  |

Then the OLS estimator is

|  |  |  |
| --- | --- | --- |
|  | 𝜿^OLS−𝜿=(1T​∑t=1T𝒁t​𝒁t′)−1​(1T​∑t=1T𝒁t​𝒖t).\widehat{{\mbox{$\kappa$}}}^{\mathrm{OLS}}-{\mbox{$\kappa$}}=\Big(\frac{1}{T}\sum\_{t=1}^{T}{\mbox{$Z$}}\_{t}{\mbox{$Z$}}\_{t}^{\prime}\Big)^{-1}\Big(\frac{1}{T}\sum\_{t=1}^{T}{\mbox{$Z$}}\_{t}{\mbox{$u$}}\_{t}\Big). |  |

(i) By Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")-(A1.1) and Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") (iii)-(iv), the processes 𝒁t{{\mbox{$Z$}}\_{t}} and 𝒖t{{\mbox{$u$}}\_{t}} are ergodic and have finite (2+δ)(2+\delta)-th moments. Hence the ergodic LLN yields

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=1T𝒁t​𝒁t′→𝑝𝑸Z:=𝔼​[𝒁t​𝒁t′]and1T​∑t=1T𝒁t​𝒖t→𝑝𝔼​[𝒁t​𝒖t],\frac{1}{T}\sum\_{t=1}^{T}{\mbox{$Z$}}\_{t}{\mbox{$Z$}}\_{t}^{\prime}\xrightarrow{p}{\mbox{$Q$}}\_{Z}:={\mathbb{E}}[{\mbox{$Z$}}\_{t}{\mbox{$Z$}}\_{t}^{\prime}]\quad\text{and}\quad\frac{1}{T}\sum\_{t=1}^{T}{\mbox{$Z$}}\_{t}{\mbox{$u$}}\_{t}\xrightarrow{p}{\mathbb{E}}[{\mbox{$Z$}}\_{t}{\mbox{$u$}}\_{t}], |  |

where 𝑸Z{\mbox{$Q$}}\_{Z} is positive definite by Assumption [2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"). Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜿^OLS→𝑝𝜿+𝑸Z−1​𝔼​[𝒁t​𝒖t].\widehat{{\mbox{$\kappa$}}}^{\mathrm{OLS}}\xrightarrow{p}{\mbox{$\kappa$}}+{\mbox{$Q$}}\_{Z}^{-1}{\mathbb{E}}[{\mbox{$Z$}}\_{t}{\mbox{$u$}}\_{t}]. |  | (45) |

Using

|  |  |  |
| --- | --- | --- |
|  | 𝒁t=[𝑰N𝑿t]and𝔼​[𝒖t]=𝟎,{\mbox{$Z$}}\_{t}=\begin{bmatrix}{\mbox{$I$}}\_{N}\\ {\mbox{$X$}}\_{t}\end{bmatrix}\quad\text{and}\quad{\mathbb{E}}[{\mbox{$u$}}\_{t}]={\mbox{$0$}}, |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒁t​𝒖t]=[𝔼​[𝒖t]𝔼​[𝑿t​𝒖t]]=[𝟎𝔼​[𝑿t​𝒖t]].{\mathbb{E}}[{\mbox{$Z$}}\_{t}{\mbox{$u$}}\_{t}]=\begin{bmatrix}{\mathbb{E}}[{\mbox{$u$}}\_{t}]\\ {\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]\\ \end{bmatrix}=\begin{bmatrix}{\mbox{$0$}}\\ {\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]\\ \end{bmatrix}. |  |

Substituting this into ([45](https://arxiv.org/html/2601.21272v1#Sx2.E45 "In A.3 Proof of Proposition3 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) yields

|  |  |  |
| --- | --- | --- |
|  | plimT→∞𝜿^OLS=𝜿+𝑸Z−1​[𝟎𝔼​[𝑿t​𝒖t]].\operatorname\*{plim}\_{T\to\infty}\widehat{{\mbox{$\kappa$}}}^{\mathrm{OLS}}={\mbox{$\kappa$}}+{\mbox{$Q$}}\_{Z}^{-1}\begin{bmatrix}{\mbox{$0$}}\\ {\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]\end{bmatrix}. |  |

Since 𝑸Z{\mbox{$Q$}}\_{Z} is nonsingular, this limit equals 𝜿\kappa if and only if

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝑿t​𝒖t]=𝟎,{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}}, |  |

that is, if and only if the present exogeneity condition holds. ∎

### A.4 Proof of Proposition4

###### Proof.

Under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") yields the joint Wold representation

|  |  |  |
| --- | --- | --- |
|  | 𝒛¯t=∑i=0∞𝚵i​𝜺t−i,𝜺t=(𝜺x,t′,𝜺u,t′)′,\bar{{\mbox{$z$}}}\_{t}=\sum\_{i=0}^{\infty}{\mbox{$\Xi$}}\_{i}{\mbox{$\varepsilon$}}\_{t-i},\quad{\mbox{$\varepsilon$}}\_{t}=({\mbox{$\varepsilon$}}\_{x,t}^{\prime},{\mbox{$\varepsilon$}}\_{u,t}^{\prime})^{\prime}, |  |

with 𝜺t{{\mbox{$\varepsilon$}}\_{t}} second-order white noise and 𝚵0=𝑰m{\mbox{$\Xi$}}\_{0}={\mbox{$I$}}\_{m}. Partition 𝚵i{\mbox{$\Xi$}}\_{i} and 𝚺:=𝔼​[𝜺t​𝜺t′]{\mbox{$\Sigma$}}:={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{t}{\mbox{$\varepsilon$}}\_{t}^{\prime}] conformably as in Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(i). Then, by whiteness and absolute summability, we have the identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒙¯t​𝒖t′]=∑i=0∞(𝚵x​x,i​𝚺x​x​𝚵u​x,i′+𝚵x​x,i​𝚺x​u​𝚵u​u,i′+𝚵x​u,i​𝚺u​x​𝚵u​x,i′+𝚵x​u,i​𝚺u​u​𝚵u​u,i′).{\mathbb{E}}[\bar{{\mbox{$x$}}}\_{t}{\mbox{$u$}}\_{t}^{\prime}]=\sum\_{i=0}^{\infty}\Big({\mbox{$\Xi$}}\_{xx,i}{\mbox{$\Sigma$}}\_{xx}{\mbox{$\Xi$}}\_{ux,i}^{\prime}+{\mbox{$\Xi$}}\_{xx,i}{\mbox{$\Sigma$}}\_{xu}{\mbox{$\Xi$}}\_{uu,i}^{\prime}+{\mbox{$\Xi$}}\_{xu,i}{\mbox{$\Sigma$}}\_{ux}{\mbox{$\Xi$}}\_{ux,i}^{\prime}+{\mbox{$\Xi$}}\_{xu,i}{\mbox{$\Sigma$}}\_{uu}{\mbox{$\Xi$}}\_{uu,i}^{\prime}\Big). |  | (46) |

Moreover, since 𝚵0=𝑰m{\mbox{$\Xi$}}\_{0}={\mbox{$I$}}\_{m}, 𝚵x​x,0=𝑰k{\mbox{$\Xi$}}\_{xx,0}={\mbox{$I$}}\_{k}, 𝚵u​u,0=𝑰N{\mbox{$\Xi$}}\_{uu,0}={\mbox{$I$}}\_{N} and 𝚵x​u,0=𝚵u​x,0=𝟎{\mbox{$\Xi$}}\_{xu,0}={\mbox{$\Xi$}}\_{ux,0}={\mbox{$0$}}, we can rewrite ([46](https://arxiv.org/html/2601.21272v1#Sx2.E46 "In Proof. ‣ A.4 Proof of Proposition4 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒙¯t​𝒖t′]=𝚺x​u+∑i=1∞(𝚵x​x,i​𝚺x​x​𝚵u​x,i′+𝚵x​x,i​𝚺x​u​𝚵u​u,i′+𝚵x​u,i​𝚺u​x​𝚵u​x,i′+𝚵x​u,i​𝚺u​u​𝚵u​u,i′).{\mathbb{E}}[\bar{{\mbox{$x$}}}\_{t}{\mbox{$u$}}\_{t}^{\prime}]={\mbox{$\Sigma$}}\_{xu}+\sum\_{i=1}^{\infty}\Big({\mbox{$\Xi$}}\_{xx,i}{\mbox{$\Sigma$}}\_{xx}{\mbox{$\Xi$}}\_{ux,i}^{\prime}+{\mbox{$\Xi$}}\_{xx,i}{\mbox{$\Sigma$}}\_{xu}{\mbox{$\Xi$}}\_{uu,i}^{\prime}+{\mbox{$\Xi$}}\_{xu,i}{\mbox{$\Sigma$}}\_{ux}{\mbox{$\Xi$}}\_{ux,i}^{\prime}+{\mbox{$\Xi$}}\_{xu,i}{\mbox{$\Sigma$}}\_{uu}{\mbox{$\Xi$}}\_{uu,i}^{\prime}\Big). |  | (47) |

(i) BD.
Under B​DBD, both the VAR coefficients and the innovation covariance are block diagonal. Equivalently, the impulse responses are block diagonal, i.e. 𝚵x​u,i=𝚵u​x,i=𝟎{\mbox{$\Xi$}}\_{xu,i}={\mbox{$\Xi$}}\_{ux,i}={\mbox{$0$}} for all i≥0i\geq 0, and 𝚺x​u=𝚺u​x=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$\Sigma$}}\_{ux}={\mbox{$0$}}. Substituting these restrictions into ([46](https://arxiv.org/html/2601.21272v1#Sx2.E46 "In Proof. ‣ A.4 Proof of Proposition4 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) yields 𝔼​[𝒙¯t​𝒖t′]=𝟎{\mathbb{E}}[\bar{{\mbox{$x$}}}\_{t}{\mbox{$u$}}\_{t}^{\prime}]={\mbox{$0$}}, hence 𝔼​[𝑿t​𝒖t]=𝟎{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}}.

(ii) GEXOG∖\setminusBD.
Under G​E​X​O​GGEXOG, 𝚺x​u=𝚺u​x=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$\Sigma$}}\_{ux}={\mbox{$0$}} and 𝚿u​x,j=𝟎{\mbox{$\Psi$}}\_{ux,j}={\mbox{$0$}} for all jj, so the characteristic polynomial is upper block-triangular. Therefore 𝚵​(L)=𝑷​(L)−1{\mbox{$\Xi$}}(L)={\mbox{$P$}}(L)^{-1} is also upper block-triangular, implying 𝚵u​x,i=𝟎{\mbox{$\Xi$}}\_{ux,i}={\mbox{$0$}} for all i≥0i\geq 0. In contrast, G​E​X​O​G∖B​DGEXOG\setminus BD means that 𝚿x​u,j≠𝟎{\mbox{$\Psi$}}\_{xu,j}\neq{\mbox{$0$}} for some jj, which generically implies 𝚵x​u,i≠𝟎{\mbox{$\Xi$}}\_{xu,i}\neq{\mbox{$0$}} for at least one i≥1i\geq 1. Hence ([46](https://arxiv.org/html/2601.21272v1#Sx2.E46 "In Proof. ‣ A.4 Proof of Proposition4 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒙¯t​𝒖t′]=∑i=1∞𝚵x​u,i​𝚺u​u​𝚵u​u,i′.{\mathbb{E}}[\bar{{\mbox{$x$}}}\_{t}{\mbox{$u$}}\_{t}^{\prime}]=\sum\_{i=1}^{\infty}{\mbox{$\Xi$}}\_{xu,i}{\mbox{$\Sigma$}}\_{uu}{\mbox{$\Xi$}}\_{uu,i}^{\prime}. |  | (48) |

If 𝒖t{\mbox{$u$}}\_{t} is serially correlated (equivalently, 𝚵u​u,i≠𝟎{\mbox{$\Xi$}}\_{uu,i}\neq{\mbox{$0$}} for some i≥1i\geq 1), then the right-hand side of ([48](https://arxiv.org/html/2601.21272v1#Sx2.E48 "In Proof. ‣ A.4 Proof of Proposition4 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) is nonzero for generic parameter values because it is a sum of nontrivial cross-block impulse-response terms weighted by 𝚺u​u>0{\mbox{$\Sigma$}}\_{uu}>0.
The only ways for ([48](https://arxiv.org/html/2601.21272v1#Sx2.E48 "In Proof. ‣ A.4 Proof of Proposition4 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) to vanish are additional restrictions such as 𝚿u​u,j=𝟎​∀j{\mbox{$\Psi$}}\_{uu,j}={\mbox{$0$}}\ \forall j (so that 𝚵u​u,i=𝟎{\mbox{$\Xi$}}\_{uu,i}={\mbox{$0$}} for all i≥1i\geq 1) or other knife-edge cancellations across lags.
Therefore, under G​E​X​O​G∖B​DGEXOG\setminus BD, contemporaneous orthogonality typically fails and, by Proposition [3](https://arxiv.org/html/2601.21272v1#Thmproposition3 "Proposition 3: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), 𝜿^O​L​S\widehat{{\mbox{$\kappa$}}}^{OLS} is generically inconsistent.

(iii) EBD.
Since G​E​X​O​G⊊E​B​DGEXOG\subsetneq EBD, the same mechanism applies within E​B​DEBD: there exist DGPs in E​B​DEBD (namely those in G​E​X​O​G∖B​DGEXOG\setminus BD) for which 𝔼​[𝑿t​𝒖t]≠𝟎{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]\neq{\mbox{$0$}} generically, so OLS can be inconsistent within the E​B​DEBD class as well.
∎

### A.5 Proof of Proposition [5](https://arxiv.org/html/2601.21272v1#Thmproposition5 "Proposition 5 (Consistency region of CO-type estimators): ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")

Throughout, let T∗:=T−p0T^{\ast}:=T-p\_{0} and implicitly restrict sums to t=p0+1,…,Tt=p\_{0}+1,\ldots,T.

(i) Consistency and asymptotic equivalence under B​DBD.
Assume the B​DBD condition holds. By Proposition [2](https://arxiv.org/html/2601.21272v1#Thmproposition2 "Proposition 2: ‣ 2.2 Relationships among exogeneity conditions ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(i), B​DBD is equivalent to covariance-based strict exogeneity, which implies 𝔼​[𝒁t​𝒖t]=𝟎{\mathbb{E}}[{\mbox{$Z$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}} and hence 𝔼​[𝑿t​𝒖t]=𝟎{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}}.
Therefore, by Proposition [3](https://arxiv.org/html/2601.21272v1#Thmproposition3 "Proposition 3: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜿^O​L​S→𝑝𝜿.\widehat{{\mbox{$\kappa$}}}^{\tiny OLS}\xrightarrow{p}{\mbox{$\kappa$}}. |  | (49) |

Write the OLS residuals as

|  |  |  |
| --- | --- | --- |
|  | 𝒖^tO​L​S=𝒚t−𝒁t′​𝜿^O​L​S=𝒖t−𝒁t′​(𝜿^O​L​S−𝜿).\widehat{{\mbox{$u$}}}\_{t}^{\tiny OLS}={\mbox{$y$}}\_{t}-{\mbox{$Z$}}\_{t}^{\prime}\widehat{{\mbox{$\kappa$}}}^{\tiny OLS}={\mbox{$u$}}\_{t}-{\mbox{$Z$}}\_{t}^{\prime}(\widehat{{\mbox{$\kappa$}}}^{\tiny OLS}-{\mbox{$\kappa$}}). |  |

Since {𝒁t}\{{\mbox{$Z$}}\_{t}\} is ergodic with finite second moments (Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(iv)), ([49](https://arxiv.org/html/2601.21272v1#Sx2.E49 "In A.5 Proof of Proposition 5 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T​∑t=1T‖𝒖^tO​L​S−𝒖t‖2≤‖𝜿^O​L​S−𝜿‖2⋅1T​∑t=1T‖𝒁t‖2→𝑝0.\frac{1}{T}\sum\_{t=1}^{T}\|\widehat{{\mbox{$u$}}}\_{t}^{\tiny OLS}-{\mbox{$u$}}\_{t}\|^{2}\leq\|\widehat{{\mbox{$\kappa$}}}^{\tiny OLS}-{\mbox{$\kappa$}}\|^{2}\cdot\frac{1}{T}\sum\_{t=1}^{T}\|{\mbox{$Z$}}\_{t}\|^{2}\xrightarrow{p}0. |  | (50) |

Under B​DBD, the joint VAR(p0p\_{0}) representation in Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(ii) is block diagonal, so in particular the uu-block follows a stable VAR(p0p\_{0}) of the form ([16](https://arxiv.org/html/2601.21272v1#S2.E16 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) with innovation covariance 𝚺u​u≻0{\mbox{$\Sigma$}}\_{uu}\succ 0.
Let 𝚿^u​u:=(𝚿^u​u,1,…,𝚿^u​u,p0)\widehat{{\mbox{$\Psi$}}}\_{uu}:=(\widehat{{\mbox{$\Psi$}}}\_{uu,1},\ldots,\widehat{{\mbox{$\Psi$}}}\_{uu,p\_{0}}) denote the VAR(p0p\_{0}) OLS estimator obtained by regressing 𝒖^tO​L​S\widehat{{\mbox{$u$}}}\_{t}^{\tiny OLS} on (𝒖^t−1O​L​S,…,𝒖^t−p0O​L​S)(\widehat{{\mbox{$u$}}}\_{t-1}^{\tiny OLS},\ldots,\widehat{{\mbox{$u$}}}\_{t-p\_{0}}^{\tiny OLS}).
By standard LLN/continuous-mapping arguments and ([50](https://arxiv.org/html/2601.21272v1#Sx2.E50 "In A.5 Proof of Proposition 5 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) (a generated-regressor argument),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚿^u​u,j→𝑝𝚿u​u,j(j=1,…,p0),𝚺^u​u→𝑝𝚺u​u.\widehat{{\mbox{$\Psi$}}}\_{uu,j}\xrightarrow{p}{\mbox{$\Psi$}}\_{uu,j}\quad(j=1,\ldots,p\_{0}),\qquad\widehat{{\mbox{$\Sigma$}}}\_{uu}\xrightarrow{p}{\mbox{$\Sigma$}}\_{uu}. |  | (51) |

Consequently, 𝑨^​(L)→𝑨​(L)\widehat{{\mbox{$A$}}}(L)\to{\mbox{$A$}}(L) coefficientwise in probability.

Define the estimated transformed variables

|  |  |  |
| --- | --- | --- |
|  | 𝒚~^t:=𝑨^​(L)​𝒚t,𝒁~^t′:=𝑨^​(L)​𝒁t′,\widehat{\tilde{{\mbox{$y$}}}}\_{t}:=\widehat{{\mbox{$A$}}}(L){\mbox{$y$}}\_{t},\qquad\widehat{\tilde{{\mbox{$Z$}}}}\_{t}^{\prime}:=\widehat{{\mbox{$A$}}}(L){\mbox{$Z$}}\_{t}^{\prime}, |  |

and recall the infeasible transforms 𝒚~t:=𝑨​(L)​𝒚t\tilde{{\mbox{$y$}}}\_{t}:={\mbox{$A$}}(L){\mbox{$y$}}\_{t} and 𝒁~t′:=𝑨​(L)​𝒁t′\tilde{{\mbox{$Z$}}}\_{t}^{\prime}:={\mbox{$A$}}(L){\mbox{$Z$}}\_{t}^{\prime}.
Using ([51](https://arxiv.org/html/2601.21272v1#Sx2.E51 "In A.5 Proof of Proposition 5 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) together with ergodicity and finite second moments of (𝒚t,𝒁t)({\mbox{$y$}}\_{t},{\mbox{$Z$}}\_{t}), we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1T∗​∑t=p0+1T𝒁~^t​𝚺^u​u−1​𝒁~^t′\displaystyle\frac{1}{T^{\ast}}\sum\_{t=p\_{0}+1}^{T}\widehat{\tilde{{\mbox{$Z$}}}}\_{t}\,\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}\widehat{\tilde{{\mbox{$Z$}}}}\_{t}^{\prime} | =1T∗​∑t=p0+1T𝒁~t​𝚺u​u−1​𝒁~t′+op​(1),\displaystyle=\frac{1}{T^{\ast}}\sum\_{t=p\_{0}+1}^{T}\tilde{{\mbox{$Z$}}}\_{t}\,{\mbox{$\Sigma$}}\_{uu}^{-1}\tilde{{\mbox{$Z$}}}\_{t}^{\prime}+o\_{p}(1), |  | (52) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1T∗​∑t=p0+1T𝒁~^t​𝚺^u​u−1​𝒚~^t\displaystyle\frac{1}{T^{\ast}}\sum\_{t=p\_{0}+1}^{T}\widehat{\tilde{{\mbox{$Z$}}}}\_{t}\,\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}\widehat{\tilde{{\mbox{$y$}}}}\_{t} | =1T∗​∑t=p0+1T𝒁~t​𝚺u​u−1​𝒚~t+op​(1).\displaystyle=\frac{1}{T^{\ast}}\sum\_{t=p\_{0}+1}^{T}\tilde{{\mbox{$Z$}}}\_{t}\,{\mbox{$\Sigma$}}\_{uu}^{-1}\tilde{{\mbox{$y$}}}\_{t}+o\_{p}(1). |  | (53) |

Moreover, by Assumption [3](https://arxiv.org/html/2601.21272v1#Thmassumption3 "Assumption 3: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") and the ergodic LLN,

|  |  |  |
| --- | --- | --- |
|  | 1T∗​∑t=p0+1T𝒁~t​𝚺u​u−1​𝒁~t′→𝑝𝑸~Z:=𝔼​[𝒁~t​𝚺u​u−1​𝒁~t′]≻0,\frac{1}{T^{\ast}}\sum\_{t=p\_{0}+1}^{T}\tilde{{\mbox{$Z$}}}\_{t}\,{\mbox{$\Sigma$}}\_{uu}^{-1}\tilde{{\mbox{$Z$}}}\_{t}^{\prime}\xrightarrow{p}\tilde{{\mbox{$Q$}}}\_{Z}:={\mathbb{E}}\!\big[\tilde{{\mbox{$Z$}}}\_{t}\,{\mbox{$\Sigma$}}\_{uu}^{-1}\tilde{{\mbox{$Z$}}}\_{t}^{\prime}\big]\succ 0, |  |

so the matrix on the left-hand side is nonsingular with probability approaching one.
Since the map (M,b)↦M−1​b(M,b)\mapsto M^{-1}b is continuous on the set of nonsingular MM,
([52](https://arxiv.org/html/2601.21272v1#Sx2.E52 "In A.5 Proof of Proposition 5 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"))–([53](https://arxiv.org/html/2601.21272v1#Sx2.E53 "In A.5 Proof of Proposition 5 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) imply

|  |  |  |
| --- | --- | --- |
|  | 𝜿^C​O−𝜿^GLS=op​(1),𝜿^C​O→𝑝𝜿,\widehat{{\mbox{$\kappa$}}}^{\tiny CO}-\widehat{{\mbox{$\kappa$}}}^{\mathrm{GLS}}=o\_{p}(1),\qquad\widehat{{\mbox{$\kappa$}}}^{\tiny CO}\xrightarrow{p}{\mbox{$\kappa$}}, |  |

where 𝜿^GLS\widehat{{\mbox{$\kappa$}}}^{\mathrm{GLS}} is the infeasible GLS estimator in ([17](https://arxiv.org/html/2601.21272v1#S2.E17 "In 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")).
Moreover, under standard regularity conditions for stable VAR estimation (yielding T\sqrt{T}-consistency of 𝚿^u​u,j\widehat{{\mbox{$\Psi$}}}\_{uu,j} and 𝚺^u​u\widehat{{\mbox{$\Sigma$}}}\_{uu}), the same argument strengthens to

|  |  |  |
| --- | --- | --- |
|  | T​(𝜿^C​O−𝜿^GLS)=op​(1),\sqrt{T}\big(\widehat{{\mbox{$\kappa$}}}^{\tiny CO}-\widehat{{\mbox{$\kappa$}}}^{\mathrm{GLS}}\big)=o\_{p}(1), |  |

so 𝜿^C​O\widehat{{\mbox{$\kappa$}}}^{\tiny CO} is asymptotically equivalent to the infeasible GLS estimator, and hence attains the GLS efficiency bound within the B​DBD class.
This proves (i).

(ii) Generic failure outside B​DBD, in particular under G​E​X​O​G∖B​DGEXOG\setminus BD.
Assume now that the DGP lies in G​E​X​O​G∖B​DGEXOG\setminus BD. By Proposition [4](https://arxiv.org/html/2601.21272v1#Thmproposition4 "Proposition 4: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(ii),
the contemporaneous orthogonality condition 𝔼​[𝑿t​𝒖t]=𝟎{\mathbb{E}}[{\mbox{$X$}}\_{t}{\mbox{$u$}}\_{t}]={\mbox{$0$}} fails for generic parameter values in G​E​X​O​G∖B​DGEXOG\setminus BD as soon as the error has serial correlation (e.g. ∃j:𝚿u​u,j≠𝟎\exists j:{\mbox{$\Psi$}}\_{uu,j}\neq{\mbox{$0$}}).
Hence, by Proposition [3](https://arxiv.org/html/2601.21272v1#Thmproposition3 "Proposition 3: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜿^O​L​S→𝑝𝜿+𝒃,𝒃≠𝟎​(generic).\widehat{{\mbox{$\kappa$}}}^{\tiny OLS}\xrightarrow{p}{\mbox{$\kappa$}}+{\mbox{$b$}},\qquad{\mbox{$b$}}\neq{\mbox{$0$}}\ \text{(generic)}. |  | (54) |

Then the first-step residuals satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒖^tO​L​S=𝒖t−𝒁t′​(𝜿^O​L​S−𝜿)=𝒖t−𝒁t′​𝒃+op​(1),\widehat{{\mbox{$u$}}}\_{t}^{\tiny OLS}={\mbox{$u$}}\_{t}-{\mbox{$Z$}}\_{t}^{\prime}(\widehat{{\mbox{$\kappa$}}}^{\tiny OLS}-{\mbox{$\kappa$}})={\mbox{$u$}}\_{t}-{\mbox{$Z$}}\_{t}^{\prime}{\mbox{$b$}}+o\_{p}(1), |  | (55) |

so the residual process converges to a different process

|  |  |  |
| --- | --- | --- |
|  | 𝒖t∗:=𝒖t−𝒁t′​𝒃,{\mbox{$u$}}\_{t}^{\ast}:={\mbox{$u$}}\_{t}-{\mbox{$Z$}}\_{t}^{\prime}{\mbox{$b$}}, |  |

not to the true disturbance 𝒖t{\mbox{$u$}}\_{t} (unless 𝒃=𝟎{\mbox{$b$}}={\mbox{$0$}}, which is non-generic).

In the second step, the VAR(p0p\_{0}) is fitted to {𝒖^tO​L​S}\{\widehat{{\mbox{$u$}}}\_{t}^{\tiny OLS}\}, which is asymptotically equivalent to fitting it to {𝒖t∗}\{{\mbox{$u$}}\_{t}^{\ast}\}. Therefore the estimated VAR coefficients converge to the pseudo-true coefficients 𝚿u​u,j∗{\mbox{$\Psi$}}\_{uu,j}^{\ast} that solve the population least-squares projection of 𝒖t∗{\mbox{$u$}}\_{t}^{\ast} on (𝒖t−1∗,…,𝒖t−p0∗)({\mbox{$u$}}\_{t-1}^{\ast},\ldots,{\mbox{$u$}}\_{t-p\_{0}}^{\ast}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚿^u​u,j→𝑝𝚿u​u,j∗≠𝚿u​u,j(generic),𝚺^u​u→𝑝𝚺u​u∗,\widehat{{\mbox{$\Psi$}}}\_{uu,j}\xrightarrow{p}{\mbox{$\Psi$}}\_{uu,j}^{\ast}\neq{\mbox{$\Psi$}}\_{uu,j}\quad\text{(generic)},\qquad\widehat{{\mbox{$\Sigma$}}}\_{uu}\xrightarrow{p}{\mbox{$\Sigma$}}\_{uu}^{\ast}, |  | (56) |

where the inequality is generic because 𝒖t∗{\mbox{$u$}}\_{t}^{\ast} has a different second-order structure from 𝒖t{\mbox{$u$}}\_{t} whenever 𝒃≠𝟎{\mbox{$b$}}\neq{\mbox{$0$}} and 𝒁t{\mbox{$Z$}}\_{t} is non-degenerate (Assumption [2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")).

Let 𝑨∗​(L):=𝑰N−∑j=1p0𝚿u​u,j∗​Lj{\mbox{$A$}}^{\ast}(L):={\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}^{\ast}L^{j} be the corresponding pseudo-true filter. Then the feasible CO transformation converges to applying 𝑨∗​(L){\mbox{$A$}}^{\ast}(L) rather than the true 𝑨​(L){\mbox{$A$}}(L). As a result, the second-step estimator converges to the pseudo-true coefficient vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜿^C​O→𝑝𝜿∗,𝜿∗=arg⁡min𝜿⁡𝔼​[‖𝚺u​u∗−1/2​𝑨∗​(L)​(𝒚t−𝒁t′​𝜿)‖2],\widehat{{\mbox{$\kappa$}}}^{\tiny CO}\xrightarrow{p}{\mbox{$\kappa$}}^{\ast},\qquad{\mbox{$\kappa$}}^{\ast}=\arg\min\_{{\mbox{$\kappa$}}}\ {\mathbb{E}}\Big[\big\|{\mbox{$\Sigma$}}\_{uu}^{\ast-1/2}{\mbox{$A$}}^{\ast}(L)({\mbox{$y$}}\_{t}-{\mbox{$Z$}}\_{t}^{\prime}{\mbox{$\kappa$}})\big\|^{2}\Big], |  | (57) |

which in general satisfies 𝜿∗≠𝜿{\mbox{$\kappa$}}^{\ast}\neq{\mbox{$\kappa$}} (generic misspecification), except under knife-edge cancellations (e.g. no serial correlation 𝚿u​u,j=𝟎{\mbox{$\Psi$}}\_{uu,j}={\mbox{$0$}} for all jj, or parameter restrictions making 𝒃=𝟎{\mbox{$b$}}={\mbox{$0$}} despite G​E​X​O​G∖B​DGEXOG\setminus BD).
Hence, outside the B​DBD class, and in particular under G​E​X​O​G∖B​DGEXOG\setminus BD, consistency of the CO-type estimator is not guaranteed and generically fails.

Finally, since G​E​X​O​G⊊E​B​DGEXOG\subsetneq EBD, the same generic failure can arise within E​B​D∖B​DEBD\setminus BD by considering any DGP in G​E​X​O​G∖B​D⊂E​B​D∖B​DGEXOG\setminus BD\subset EBD\setminus BD.
This completes the proof. ∎

### A.6 Proof of Proposition [6](https://arxiv.org/html/2601.21272v1#Thmproposition6 "Proposition 6 (Consistency region of the FGLS-D estimator): ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")

Throughout, fix p0p\_{0} and write T∗:=T−p0T^{\ast}:=T-p\_{0}, implicitly restricting sums to
t=p0+1,…,Tt=p\_{0}+1,\ldots,T (initial observations are asymptotically negligible).
Define

|  |  |  |
| --- | --- | --- |
|  | 𝑨​(L):=𝑰N−∑j=1p0𝚿u​u,j​Lj,𝑨​(1):=𝑰N−∑j=1p0𝚿u​u,j.{\mbox{$A$}}(L):={\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}L^{j},\qquad{\mbox{$A$}}(1):={\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}. |  |

Define the infeasible filtered variables

|  |  |  |
| --- | --- | --- |
|  | 𝒚FD,t:=𝑨​(L)​𝒚t,𝑿FD,t′:=𝑿t′−∑j=1p0𝚿u​u,j​𝑿t−j′,{\mbox{$y$}}\_{\mathrm{FD},t}:={\mbox{$A$}}(L){\mbox{$y$}}\_{t},\qquad{\mbox{$X$}}\_{\mathrm{FD},t}^{\prime}:={\mbox{$X$}}\_{t}^{\prime}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$X$}}\_{t-j}^{\prime}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝒁FD,t′:=[𝑨​(1),𝑿FD,t′],𝜿:=(𝜶′,𝜷′)′.{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}:=\bigl[\ {\mbox{$A$}}(1),\ \ {\mbox{$X$}}\_{\mathrm{FD},t}^{\prime}\ \bigr],\qquad{\mbox{$\kappa$}}:=({\mbox{$\alpha$}}^{\prime},{\mbox{$\beta$}}^{\prime})^{\prime}. |  |

(i) Consistency and asymptotic equivalence under G​E​X​O​GGEXOG.

Assume the DGP satisfies G​E​X​O​GGEXOG, i.e. 𝚿u​x,j=𝟎{\mbox{$\Psi$}}\_{ux,j}={\mbox{$0$}} for all jj and
𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}. Then the disturbance law of motion is closed:

|  |  |  |
| --- | --- | --- |
|  | 𝒖t=∑j=1p0𝚿u​u,j​𝒖t−j+𝜺u,t,{\mbox{$u$}}\_{t}=\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$u$}}\_{t-j}+{\mbox{$\varepsilon$}}\_{u,t}, |  |

so 𝑨​(L)​𝒖t=𝜺u,t{\mbox{$A$}}(L){\mbox{$u$}}\_{t}={\mbox{$\varepsilon$}}\_{u,t}. Applying 𝑨​(L){\mbox{$A$}}(L) to
𝒚t=𝒁t′​𝜿+𝒖t{\mbox{$y$}}\_{t}={\mbox{$Z$}}\_{t}^{\prime}{\mbox{$\kappa$}}+{\mbox{$u$}}\_{t} yields the correctly specified infeasible filtered regression

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚FD,t=𝒁FD,t′​𝜿+𝜺u,t.{\mbox{$y$}}\_{\mathrm{FD},t}={\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}{\mbox{$\kappa$}}+{\mbox{$\varepsilon$}}\_{u,t}. |  | (58) |

Let ℋt−1:=span¯​{𝒛¯s:s≤t−1}\mathscr{H}\_{t-1}:=\overline{\mathrm{span}}\{\bar{{\mbox{$z$}}}\_{s}:\ s\leq t-1\} be the closed linear span
generated by the past of 𝒛¯t=((𝒙t−𝝁x)′,𝒖t′)′\bar{{\mbox{$z$}}}\_{t}=(({\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x})^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime}.
By Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(i), the joint innovation
𝜺t=(𝜺x,t′,𝜺u,t′)′{\mbox{$\varepsilon$}}\_{t}=({\mbox{$\varepsilon$}}\_{x,t}^{\prime},{\mbox{$\varepsilon$}}\_{u,t}^{\prime})^{\prime}
satisfies 𝜺t⟂ℋt−1{\mbox{$\varepsilon$}}\_{t}\perp\mathscr{H}\_{t-1} in L2L^{2}, and 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} implies
𝜺u,t⟂𝜺x,t{\mbox{$\varepsilon$}}\_{u,t}\perp{\mbox{$\varepsilon$}}\_{x,t} in L2L^{2}. Under G​E​X​O​GGEXOG, 𝒙¯t\bar{{\mbox{$x$}}}\_{t} is a linear
function of (ℋt−1,𝜺x,t)(\mathscr{H}\_{t-1},{\mbox{$\varepsilon$}}\_{x,t}) and does not load on 𝜺u,t{\mbox{$\varepsilon$}}\_{u,t}
contemporaneously. Hence 𝒁FD,t{\mbox{$Z$}}\_{\mathrm{FD},t}—being a fixed linear function of
{𝑿t−ℓ}ℓ=0p0\{{\mbox{$X$}}\_{t-\ell}\}\_{\ell=0}^{p\_{0}} and constants—is measurable with respect to the closed linear space
span¯​(ℋt−1∪{𝜺x,t})\overline{\mathrm{span}}(\mathscr{H}\_{t-1}\cup\{{\mbox{$\varepsilon$}}\_{x,t}\}), and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒁FD,t​𝜺u,t]=𝟎.{\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\varepsilon$}}\_{u,t}]={\mbox{$0$}}. |  | (59) |

Consider the infeasible GLS estimator based on ([58](https://arxiv.org/html/2601.21272v1#Sx2.E58 "In A.6 Proof of Proposition 6 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")):

|  |  |  |
| --- | --- | --- |
|  | 𝜿^FDGLS:=(∑𝒁FD,t​𝚺u​u−1​𝒁FD,t′)−1​(∑𝒁FD,t​𝚺u​u−1​𝒚FD,t).\widehat{{\mbox{$\kappa$}}}^{\,\mathrm{GLS}}\_{\mathrm{FD}}:=\Big(\sum{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}\Big)^{-1}\Big(\sum{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$y$}}\_{\mathrm{FD},t}\Big). |  |

Using ([58](https://arxiv.org/html/2601.21272v1#Sx2.E58 "In A.6 Proof of Proposition 6 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")),

|  |  |  |
| --- | --- | --- |
|  | 𝜿^FDGLS−𝜿=(1T∗​∑𝒁FD,t​𝚺u​u−1​𝒁FD,t′)−1​(1T∗​∑𝒁FD,t​𝚺u​u−1​𝜺u,t).\widehat{{\mbox{$\kappa$}}}^{\,\mathrm{GLS}}\_{\mathrm{FD}}-{\mbox{$\kappa$}}=\Big(\frac{1}{T^{\ast}}\sum{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}\Big)^{-1}\Big(\frac{1}{T^{\ast}}\sum{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$\varepsilon$}}\_{u,t}\Big). |  |

By Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(iv), {(𝒚t,𝑿t′,𝒖t)}\{({\mbox{$y$}}\_{t},{\mbox{$X$}}\_{t}^{\prime},{\mbox{$u$}}\_{t})\} is strictly stationary,
strongly mixing with finite moments, and so is {(𝒁FD,t,𝜺u,t)}\{({\mbox{$Z$}}\_{\mathrm{FD},t},{\mbox{$\varepsilon$}}\_{u,t})\} as a fixed
linear transform of finitely many lags. Hence a LLN for strongly mixing sequences yields

|  |  |  |
| --- | --- | --- |
|  | 1T∗​∑𝒁FD,t​𝚺u​u−1​𝒁FD,t′→𝑝𝔼​[𝒁FD,t​𝚺u​u−1​𝒁FD,t′]=𝑸FD,1T∗​∑𝒁FD,t​𝚺u​u−1​𝜺u,t→𝑝𝟎,\frac{1}{T^{\ast}}\sum{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}\xrightarrow{p}{\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}]={\mbox{$Q$}}\_{\mathrm{FD}},\qquad\frac{1}{T^{\ast}}\sum{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$\varepsilon$}}\_{u,t}\xrightarrow{p}{\mbox{$0$}}, |  |

where the second convergence uses ([59](https://arxiv.org/html/2601.21272v1#Sx2.E59 "In A.6 Proof of Proposition 6 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")). Since 𝑸FD≻0{\mbox{$Q$}}\_{\mathrm{FD}}\succ 0 by
Assumption [4](https://arxiv.org/html/2601.21272v1#Thmassumption4 "Assumption 4: ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), it follows that
𝜿^FDGLS→𝑝𝜿\widehat{{\mbox{$\kappa$}}}^{\,\mathrm{GLS}}\_{\mathrm{FD}}\xrightarrow{p}{\mbox{$\kappa$}}.

Under G​E​X​O​GGEXOG, Step 1 is a correctly specified linear regression with error 𝜺u,t{\mbox{$\varepsilon$}}\_{u,t}, and
its regressors are functions of {𝒚t−j,𝒙t−j,𝒙t}j=1p0\{{\mbox{$y$}}\_{t-j},{\mbox{$x$}}\_{t-j},{\mbox{$x$}}\_{t}\}\_{j=1}^{p\_{0}} and constants, which lie in
span¯​(ℋt−1∪{𝜺x,t})\overline{\mathrm{span}}(\mathscr{H}\_{t-1}\cup\{{\mbox{$\varepsilon$}}\_{x,t}\}).
Therefore the Step 1 OLS estimators satisfy (by the same LLN/continuous-mapping arguments)

|  |  |  |
| --- | --- | --- |
|  | 𝚿^u​u,j→𝑝𝚿u​u,j(j=1,…,p0),𝚺^u​u→𝑝𝚺u​u,\widehat{{\mbox{$\Psi$}}}\_{uu,j}\xrightarrow{p}{\mbox{$\Psi$}}\_{uu,j}\quad(j=1,\ldots,p\_{0}),\qquad\widehat{{\mbox{$\Sigma$}}}\_{uu}\xrightarrow{p}{\mbox{$\Sigma$}}\_{uu}, |  |

and hence 𝑨^​(L):=𝑰N−∑j=1p0𝚿^u​u,j​Lj\widehat{{\mbox{$A$}}}(L):={\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}\widehat{{\mbox{$\Psi$}}}\_{uu,j}L^{j} converges coefficientwise
to 𝑨​(L){\mbox{$A$}}(L) and 𝚺^u​u−1→𝑝𝚺u​u−1\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}\xrightarrow{p}{\mbox{$\Sigma$}}\_{uu}^{-1}.
Let 𝒚^FD,t\widehat{{\mbox{$y$}}}\_{\mathrm{FD},t} and 𝒁^FD,t\widehat{{\mbox{$Z$}}}\_{\mathrm{FD},t} denote the feasible filtered series
constructed from (𝑨^​(L),𝚺^u​u)(\widehat{{\mbox{$A$}}}(L),\widehat{{\mbox{$\Sigma$}}}\_{uu}). Then, by ergodicity and finite moments,

|  |  |  |
| --- | --- | --- |
|  | 1T∗​∑𝒁^FD,t​𝚺^u​u−1​𝒁^FD,t′=1T∗​∑𝒁FD,t​𝚺u​u−1​𝒁FD,t′+op​(1),1T∗​∑𝒁^FD,t​𝚺^u​u−1​𝒚^FD,t=1T∗​∑𝒁FD,t​𝚺u​u−1​𝒚FD,t+op​(1).\frac{1}{T^{\ast}}\sum\widehat{{\mbox{$Z$}}}\_{\mathrm{FD},t}\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}\widehat{{\mbox{$Z$}}}\_{\mathrm{FD},t}^{\prime}=\frac{1}{T^{\ast}}\sum{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}+o\_{p}(1),\qquad\frac{1}{T^{\ast}}\sum\widehat{{\mbox{$Z$}}}\_{\mathrm{FD},t}\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}\widehat{{\mbox{$y$}}}\_{\mathrm{FD},t}=\frac{1}{T^{\ast}}\sum{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$y$}}\_{\mathrm{FD},t}+o\_{p}(1). |  |

Since 𝑸FD≻0{\mbox{$Q$}}\_{\mathrm{FD}}\succ 0 (Assumption [4](https://arxiv.org/html/2601.21272v1#Thmassumption4 "Assumption 4: ‣ 2.4 The inconsistency of FGLS-D estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")), the map (M,b)↦M−1​b(M,b)\mapsto M^{-1}b is continuous
at (𝑸FD,𝔼​[𝒁FD,t​𝚺u​u−1​𝒚FD,t])({\mbox{$Q$}}\_{\mathrm{FD}},{\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$y$}}\_{\mathrm{FD},t}]), so

|  |  |  |
| --- | --- | --- |
|  | 𝜿^FGLS−D−𝜿^FDGLS=op​(1),𝜿^FGLS−D→𝑝𝜿.\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS\!-\!D}}-\widehat{{\mbox{$\kappa$}}}^{\,\mathrm{GLS}}\_{\mathrm{FD}}=o\_{p}(1),\qquad\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS\!-\!D}}\xrightarrow{p}{\mbox{$\kappa$}}. |  |

Under standard regularity conditions ensuring T\sqrt{T}-consistency of
(𝚿^u​u,⋅,𝚺^u​u)(\widehat{{\mbox{$\Psi$}}}\_{uu,\cdot},\widehat{{\mbox{$\Sigma$}}}\_{uu}), the same argument strengthens to
T​(𝜿^FGLS−D−𝜿^FDGLS)=op​(1)\sqrt{T}\big(\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS\!-\!D}}-\widehat{{\mbox{$\kappa$}}}^{\,\mathrm{GLS}}\_{\mathrm{FD}}\big)=o\_{p}(1),
so the feasible estimator inherits the limiting distribution of its infeasible GLS counterpart.
Under B​DBD, the G​E​X​O​GGEXOG restriction holds trivially, so the same conclusion applies.

(ii) Generic inconsistency on E​B​D∖G​E​X​O​GEBD\setminus GEXOG.

Now assume the DGP lies in E​B​D∖G​E​X​O​GEBD\setminus GEXOG, i.e. 𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}} but
𝚿u​x,j≠𝟎{\mbox{$\Psi$}}\_{ux,j}\neq{\mbox{$0$}} for some jj. Then the true disturbance dynamics is

|  |  |  |
| --- | --- | --- |
|  | 𝒖t=∑j=1p0𝚿u​u,j​𝒖t−j+∑j=1p0𝚿u​x,j​(𝒙t−j−𝝁x)+𝜺u,t.{\mbox{$u$}}\_{t}=\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$u$}}\_{t-j}+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{ux,j}({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x})+{\mbox{$\varepsilon$}}\_{u,t}. |  |

Applying 𝑨​(L){\mbox{$A$}}(L) to 𝒚t=𝒁t′​𝜿+𝒖t{\mbox{$y$}}\_{t}={\mbox{$Z$}}\_{t}^{\prime}{\mbox{$\kappa$}}+{\mbox{$u$}}\_{t} yields

|  |  |  |
| --- | --- | --- |
|  | 𝒚FD,t=𝒁FD,t′𝜿+∑j=1p0𝚿u​x,j(𝒙t−j−𝝁x)+𝜺u,t=:𝒁FD,t′𝜿+𝜺~u,t,{\mbox{$y$}}\_{\mathrm{FD},t}={\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}{\mbox{$\kappa$}}+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{ux,j}({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x})+{\mbox{$\varepsilon$}}\_{u,t}=:{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}{\mbox{$\kappa$}}+\tilde{{\mbox{$\varepsilon$}}}\_{u,t}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | 𝜺~u,t:=𝜺u,t+∑j=1p0𝚿u​x,j​(𝒙t−j−𝝁x).\tilde{{\mbox{$\varepsilon$}}}\_{u,t}:={\mbox{$\varepsilon$}}\_{u,t}+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{ux,j}({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x}). |  |

As before, 𝔼​[𝒁FD,t​𝜺u,t]=𝟎{\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\varepsilon$}}\_{u,t}]={\mbox{$0$}} holds (innovation orthogonality and
𝚺x​u=𝟎{\mbox{$\Sigma$}}\_{xu}={\mbox{$0$}}). However,

|  |  |  |
| --- | --- | --- |
|  | 𝔼[𝒁FD,t𝜺~u,t]=∑j=1p0𝚿u​x,j𝔼[𝒁FD,t(𝒙t−j−𝝁x)].{\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{FD},t}\tilde{{\mbox{$\varepsilon$}}}\_{u,t}]=\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{ux,j}\ {\mathbb{E}}\!\mathopen{}\left[{\mbox{$Z$}}\_{\mathrm{FD},t}({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x})\mathclose{}\right]. |  |

The constant block 𝑨​(1){\mbox{$A$}}(1) contributes 𝑨​(1)​𝔼​[𝒙t−j−𝝁x]=𝟎{\mbox{$A$}}(1){\mathbb{E}}[{\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x}]={\mbox{$0$}}, but the regressor block
𝑿FD,t′{\mbox{$X$}}\_{\mathrm{FD},t}^{\prime} is a nontrivial linear function of 𝒙t,𝒙t−1,…,𝒙t−p0{\mbox{$x$}}\_{t},{\mbox{$x$}}\_{t-1},\ldots,{\mbox{$x$}}\_{t-p\_{0}}.
In particular, for any j∈{1,…,p0}j\in\{1,\ldots,p\_{0}\},

|  |  |  |
| --- | --- | --- |
|  | 𝔼[𝑿FD,t′(𝒙t−j−𝝁x)]=𝔼[𝑿t′(𝒙t−j−𝝁x)]−∑ℓ=1p0𝚿u​u,ℓ𝔼[𝑿t−ℓ′(𝒙t−j−𝝁x)],{\mathbb{E}}\!\mathopen{}\left[{\mbox{$X$}}\_{\mathrm{FD},t}^{\prime}({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x})\mathclose{}\right]={\mathbb{E}}\!\mathopen{}\left[{\mbox{$X$}}\_{t}^{\prime}({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x})\mathclose{}\right]-\sum\_{\ell=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,\ell}{\mathbb{E}}\!\mathopen{}\left[{\mbox{$X$}}\_{t-\ell}^{\prime}({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x})\mathclose{}\right], |  |

which is generically nonzero under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") and Assumption [2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")
(except under knife-edge cancellations, e.g. degenerate regressor dynamics or special parameter values).
Since 𝚿u​x,⋅≠𝟎{\mbox{$\Psi$}}\_{ux,\cdot}\neq{\mbox{$0$}} in E​B​D∖G​E​X​O​GEBD\setminus GEXOG, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒁FD,t​𝜺~u,t]≠𝟎(generic).{\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{FD},t}\tilde{{\mbox{$\varepsilon$}}}\_{u,t}]\neq{\mbox{$0$}}\qquad\text{(generic)}. |  |

Therefore the population normal equations for the filtered regression are violated and the probability limit
of even the infeasible GLS based on (𝑨​(L),𝚺u​u)({\mbox{$A$}}(L),{\mbox{$\Sigma$}}\_{uu}) equals

|  |  |  |
| --- | --- | --- |
|  | 𝜿∗=𝜿+(𝔼​[𝒁FD,t​𝚺u​u−1​𝒁FD,t′])−1​𝔼​[𝒁FD,t​𝚺u​u−1​𝜺~u,t]≠𝜿(generic).{\mbox{$\kappa$}}^{\ast}={\mbox{$\kappa$}}+\Big({\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{FD},t}^{\prime}]\Big)^{-1}{\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{FD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}\tilde{{\mbox{$\varepsilon$}}}\_{u,t}]\neq{\mbox{$\kappa$}}\qquad\text{(generic)}. |  |

Since the feasible FGLS-D estimator is obtained by replacing (𝑨​(L),𝚺u​u)({\mbox{$A$}}(L),{\mbox{$\Sigma$}}\_{uu}) with estimators
constructed under the maintained G​E​X​O​GGEXOG-type disturbance specification, it converges to the same pseudo-true
limit and cannot eliminate this misspecification bias. Hence 𝜿^FGLS−D\widehat{{\mbox{$\kappa$}}}^{\mathrm{FGLS\!-\!D}} is
generically inconsistent on E​B​D∖G​E​X​O​GEBD\setminus GEXOG. ∎

### A.7 Proof of Lemma1

Fix i∈{1,…,N}i\in\{1,\ldots,N\}. Recall ℱt−1:=σ(𝒛s:s≤t−1)\mathscr{F}\_{t-1}:=\sigma({\mbox{$z$}}\_{s}:\,s\leq t-1) and 𝒛t=(𝒙t′,𝒖t′)′{\mbox{$z$}}\_{t}=({\mbox{$x$}}\_{t}^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime}.

(i)
By Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(ii)–(iii) under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), 𝒛¯t=((𝒙t−𝝁x)′,𝒖t′)′\bar{{\mbox{$z$}}}\_{t}=(({\mbox{$x$}}\_{t}-{\mbox{$\mu$}}\_{x})^{\prime},{\mbox{$u$}}\_{t}^{\prime})^{\prime} admits the stable VAR(p0p\_{0}) representation, and in particular the xx-block satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝒙t=𝝁x+∑j=1p0𝚿x​x,j​(𝒙t−j−𝝁x)+∑j=1p0𝚿x​u,j​𝒖t−j+𝜺x,t.{\mbox{$x$}}\_{t}={\mbox{$\mu$}}\_{x}+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{xx,j}({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x})+\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{xu,j}{\mbox{$u$}}\_{t-j}+{\mbox{$\varepsilon$}}\_{x,t}. |  |

Let 𝑱i∈ℝki×k{\mbox{$J$}}\_{i}\in\mathbb{R}^{k\_{i}\times k} be the selection matrix extracting the iith block
(𝑱i​𝒙t=𝒙i,t{\mbox{$J$}}\_{i}{\mbox{$x$}}\_{t}={\mbox{$x$}}\_{i,t}). Define the ℱt−1\mathscr{F}\_{t-1}-measurable vector

|  |  |  |
| --- | --- | --- |
|  | 𝒉x,i,t:=𝑱i​𝝁x+∑j=1p0𝑱i​𝚿x​x,j​(𝒙t−j−𝝁x)+∑j=1p0𝑱i​𝚿x​u,j​𝒖t−j.{\mbox{$h$}}\_{x,i,t}:={\mbox{$J$}}\_{i}{\mbox{$\mu$}}\_{x}+\sum\_{j=1}^{p\_{0}}{\mbox{$J$}}\_{i}{\mbox{$\Psi$}}\_{xx,j}({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x})+\sum\_{j=1}^{p\_{0}}{\mbox{$J$}}\_{i}{\mbox{$\Psi$}}\_{xu,j}{\mbox{$u$}}\_{t-j}. |  |

Since 𝒙t−j{\mbox{$x$}}\_{t-j} and 𝒖t−j{\mbox{$u$}}\_{t-j} (j≥1j\geq 1) are ℱt−1\mathscr{F}\_{t-1}-measurable, we have 𝒉x,i,t{\mbox{$h$}}\_{x,i,t} ℱt−1\mathscr{F}\_{t-1}-measurable and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒙i,t=𝒉x,i,t+𝑱i​𝜺x,t.{\mbox{$x$}}\_{i,t}={\mbox{$h$}}\_{x,i,t}+{\mbox{$J$}}\_{i}{\mbox{$\varepsilon$}}\_{x,t}. |  | (60) |

Next note that, by construction, 𝒚t−j{\mbox{$y$}}\_{t-j} and 𝒙t−j{\mbox{$x$}}\_{t-j} (j≥1j\geq 1) are ℱt−1\mathscr{F}\_{t-1}-measurable. Moreover 11 is deterministic. Hence the equation-specific regressor vector

|  |  |  |
| --- | --- | --- |
|  | 𝒘i,t=[ 1,𝒙i,t′,𝒚t−1′,…,𝒚t−p0′,𝒙t−1′,…,𝒙t−p0′]′{\mbox{$w$}}\_{i,t}=\bigl[\,1,\ {\mbox{$x$}}\_{i,t}^{\prime},\ {\mbox{$y$}}\_{t-1}^{\prime},\ldots,{\mbox{$y$}}\_{t-p\_{0}}^{\prime},\ {\mbox{$x$}}\_{t-1}^{\prime},\ldots,{\mbox{$x$}}\_{t-p\_{0}}^{\prime}\,\bigr]^{\prime} |  |

can be written, using ([60](https://arxiv.org/html/2601.21272v1#Sx2.E60 "In A.7 Proof of Lemma1 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")), as

|  |  |  |
| --- | --- | --- |
|  | 𝒘i,t=[ 1,𝒉x,i,t′,𝒚t−1′,…,𝒚t−p0′,𝒙t−1′,…,𝒙t−p0′]′⏟=⁣:𝒉i,t+[𝟎𝑱i𝟎⋮𝟎]⏟=⁣:𝒎i​𝜺x,t.{\mbox{$w$}}\_{i,t}=\underbrace{\bigl[\,1,\ {\mbox{$h$}}\_{x,i,t}^{\prime},\ {\mbox{$y$}}\_{t-1}^{\prime},\ldots,{\mbox{$y$}}\_{t-p\_{0}}^{\prime},\ {\mbox{$x$}}\_{t-1}^{\prime},\ldots,{\mbox{$x$}}\_{t-p\_{0}}^{\prime}\,\bigr]^{\prime}}\_{=:~{\mbox{$h$}}\_{i,t}}\;+\;\underbrace{\begin{bmatrix}{\mbox{$0$}}\\ {\mbox{$J$}}\_{i}\\ {\mbox{$0$}}\\ \vdots\\ {\mbox{$0$}}\end{bmatrix}}\_{=:~{\mbox{$m$}}\_{i}}{\mbox{$\varepsilon$}}\_{x,t}. |  |

Clearly, 𝒉i,t{\mbox{$h$}}\_{i,t} is ℱt−1\mathscr{F}\_{t-1}-measurable and 𝒎i{\mbox{$m$}}\_{i} is deterministic, so this yields the desired decomposition

|  |  |  |
| --- | --- | --- |
|  | 𝒘i,t=𝒉i,t+𝒎i​𝜺x,t,{\mbox{$w$}}\_{i,t}={\mbox{$h$}}\_{i,t}+{\mbox{$m$}}\_{i}{\mbox{$\varepsilon$}}\_{x,t}, |  |

and in particular 𝒘i,t{\mbox{$w$}}\_{i,t} is measurable with respect to σ​(ℱt−1,𝜺x,t)\sigma(\mathscr{F}\_{t-1},{\mbox{$\varepsilon$}}\_{x,t}).

Finally, since 𝜺t{\mbox{$\varepsilon$}}\_{t} is the innovation sequence in the Wold/VAR representation, we have 𝔼​[𝜺u,t∣ℱt−1]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t}\mid\mathscr{F}\_{t-1}]={\mbox{$0$}} and thus 𝔼​[εu,i,t∣ℱt−1]=0{\mathbb{E}}[\varepsilon\_{u,i,t}\mid\mathscr{F}\_{t-1}]=0. Therefore,

|  |  |  |
| --- | --- | --- |
|  | 𝔼[𝒉i,tεu,i,t]=𝔼[𝒉i,t𝔼[εu,i,t∣ℱt−1]]=𝟎.{\mathbb{E}}[{\mbox{$h$}}\_{i,t}\,\varepsilon\_{u,i,t}]={\mathbb{E}}\!\mathopen{}\left[\ {\mbox{$h$}}\_{i,t}\,{\mathbb{E}}[\varepsilon\_{u,i,t}\mid\mathscr{F}\_{t-1}]\ \mathclose{}\right]={\mbox{$0$}}. |  |

Moreover, if 𝚺x​u=𝔼​[𝜺x,t​𝜺u,t′]=𝟎{\mbox{$\Sigma$}}\_{xu}={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{x,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$0$}}, then
𝔼​[𝜺x,t​εu,i,t]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{x,t}\varepsilon\_{u,i,t}]={\mbox{$0$}} and hence

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒎i​𝜺x,t​εu,i,t]=𝒎i​𝔼​[𝜺x,t​εu,i,t]=𝟎.{\mathbb{E}}[{\mbox{$m$}}\_{i}{\mbox{$\varepsilon$}}\_{x,t}\,\varepsilon\_{u,i,t}]={\mbox{$m$}}\_{i}\,{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{x,t}\varepsilon\_{u,i,t}]={\mbox{$0$}}. |  |

Combining the two displays gives 𝔼​[𝒘i,t​εu,i,t]=𝟎{\mathbb{E}}[{\mbox{$w$}}\_{i,t}\,\varepsilon\_{u,i,t}]={\mbox{$0$}}.

(ii)
By Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(iv) (finite (4+2​δ)(4+2\delta)-moments of 𝒛t{\mbox{$z$}}\_{t}), 𝔼​‖𝒙t‖4+2​δ<∞{\mathbb{E}}\|{\mbox{$x$}}\_{t}\|^{4+2\delta}<\infty and 𝔼​‖𝒚t‖4+2​δ<∞{\mathbb{E}}\|{\mbox{$y$}}\_{t}\|^{4+2\delta}<\infty, and also 𝔼​‖𝜺u,t‖4+2​δ<∞{\mathbb{E}}\|{\mbox{$\varepsilon$}}\_{u,t}\|^{4+2\delta}<\infty. Since 𝒘i,t{\mbox{$w$}}\_{i,t} is a finite stacking of the blocks 11, 𝒙i,t{\mbox{$x$}}\_{i,t}, {𝒚t−j}j=1p0\{{\mbox{$y$}}\_{t-j}\}\_{j=1}^{p\_{0}}, and {𝒙t−j}j=1p0\{{\mbox{$x$}}\_{t-j}\}\_{j=1}^{p\_{0}},
there exists a constant Ci>0C\_{i}>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖𝒘i,t‖≤Ci​(1+‖𝒙i,t‖+∑j=1p0‖𝒚t−j‖+∑j=1p0‖𝒙t−j‖).\|{\mbox{$w$}}\_{i,t}\|\leq C\_{i}\Bigl(1+\|{\mbox{$x$}}\_{i,t}\|+\sum\_{j=1}^{p\_{0}}\|{\mbox{$y$}}\_{t-j}\|+\sum\_{j=1}^{p\_{0}}\|{\mbox{$x$}}\_{t-j}\|\Bigr). |  |

Hence 𝔼​‖𝒘i,t‖2+δ<∞{\mathbb{E}}\|{\mbox{$w$}}\_{i,t}\|^{2+\delta}<\infty. Moreover, using ‖𝒘i,t​εu,i,t‖≤‖𝒘i,t‖​|εu,i,t|\|{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}\|\leq\|{\mbox{$w$}}\_{i,t}\|\,|\varepsilon\_{u,i,t}| and Hölder’s inequality,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖𝒘i,t​εu,i,t‖2+δ≤(𝔼​‖𝒘i,t‖4+2​δ)1/2​(𝔼​|εu,i,t|4+2​δ)1/2<∞.{\mathbb{E}}\|{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}\|^{2+\delta}\leq\Big({\mathbb{E}}\|{\mbox{$w$}}\_{i,t}\|^{4+2\delta}\Big)^{1/2}\Big({\mathbb{E}}|\varepsilon\_{u,i,t}|^{4+2\delta}\Big)^{1/2}<\infty. |  |

(iii)
Let 𝑸w,i:=𝔼​[𝒘i,t​𝒘i,t′]{\mbox{$Q$}}\_{w,i}:={\mathbb{E}}[{\mbox{$w$}}\_{i,t}{\mbox{$w$}}\_{i,t}^{\prime}]. For any 𝒂∈ℝdi{\mbox{$a$}}\in\mathbb{R}^{d\_{i}}, 𝒂≠𝟎{\mbox{$a$}}\neq{\mbox{$0$}},

|  |  |  |
| --- | --- | --- |
|  | 𝒂′​𝑸w,i​𝒂=𝔼​[(𝒂′​𝒘i,t)2]≥0.{\mbox{$a$}}^{\prime}{\mbox{$Q$}}\_{w,i}{\mbox{$a$}}={\mathbb{E}}[({\mbox{$a$}}^{\prime}{\mbox{$w$}}\_{i,t})^{2}]\geq 0. |  |

If 𝒂′​𝑸w,i​𝒂=0{\mbox{$a$}}^{\prime}{\mbox{$Q$}}\_{w,i}{\mbox{$a$}}=0, then 𝒂′​𝒘i,t=0{\mbox{$a$}}^{\prime}{\mbox{$w$}}\_{i,t}=0 a.s., which implies an exact linear dependence among the regressors in the iith equation. This is ruled out by Assumption [2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(A2.1) (full-rank/identification for the stacked regressor system) together with the definition of 𝒘i,t{\mbox{$w$}}\_{i,t} as the ii-specific subvector of the stacked regressor 𝒁t{\mbox{$Z$}}\_{t} augmented by finitely many lags. Hence 𝑸w,i{\mbox{$Q$}}\_{w,i} is positive definite. ∎

### A.8 Proof of Lemma2

Let p0p\_{0} be the minimal lag order in Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") (finite-predictor exactness). Fix a candidate set 𝒫={1,…,pmax}\mathcal{P}=\{1,\ldots,p\_{\max}\} with pmax≥p0p\_{\max}\geq p\_{0}.

For each p∈𝒫p\in\mathcal{P}, define the equation-by-equation augmented regression
(obtained from ([25](https://arxiv.org/html/2601.21272v1#S2.E25 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) by replacing p0p\_{0} with pp):

|  |  |  |
| --- | --- | --- |
|  | yi,t=𝒘i,t​(p)′​𝜽i​(p)+εu,i,t,t=p+1,…,T,i=1,…,N,y\_{i,t}={\mbox{$w$}}\_{i,t}(p)^{\prime}{\mbox{$\theta$}}\_{i}(p)+\varepsilon\_{u,i,t},\qquad t=p+1,\ldots,T,\quad i=1,\ldots,N, |  |

where 𝒘i,t​(p){\mbox{$w$}}\_{i,t}(p) stacks the contemporaneous regressors in equation ii and the lagged vectors {𝒚t−j}j=1p\{{\mbox{$y$}}\_{t-j}\}\_{j=1}^{p} and {𝒙t−j}j=1p\{{\mbox{$x$}}\_{t-j}\}\_{j=1}^{p}. Let 𝜽^i​(p)\widehat{{\mbox{$\theta$}}}\_{i}(p) be the OLS estimator and define residuals

|  |  |  |
| --- | --- | --- |
|  | ε^u,i,t​(p):=yi,t−𝒘i,t​(p)′​𝜽^i​(p),𝜺^u,t​(p):=(ε^u,1,t​(p),…,ε^u,N,t​(p))′.\widehat{\varepsilon}\_{u,i,t}(p):=y\_{i,t}-{\mbox{$w$}}\_{i,t}(p)^{\prime}\widehat{{\mbox{$\theta$}}}\_{i}(p),\qquad\widehat{{\mbox{$\varepsilon$}}}\_{u,t}(p):=\big(\widehat{\varepsilon}\_{u,1,t}(p),\ldots,\widehat{\varepsilon}\_{u,N,t}(p)\big)^{\prime}. |  |

Under Assumptions [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")–[2](https://arxiv.org/html/2601.21272v1#Thmassumption2 "Assumption 2: ‣ 2.3 The inconsistency of OLS and OLS-based GLS estimators in multi-equation models ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") and E​B​DEBD, Lemma [1](https://arxiv.org/html/2601.21272v1#Thmlemma1 "Lemma 1 (Equation-by-equation properties of the Durbin regression): ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") applied with pp lags implies that, for each fixed pp and each ii, {𝒘i,t​(p)}\{{\mbox{$w$}}\_{i,t}(p)\} has finite (2+δ)(2+\delta)-moments and is strictly stationary and strongly mixing, and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒘i,t​(p)​εu,i,t]=0,𝑸w,i​(p):=𝔼​[𝒘i,t​(p)​𝒘i,t​(p)′]>0.{\mathbb{E}}\!\big[{\mbox{$w$}}\_{i,t}(p)\,\varepsilon\_{u,i,t}\big]=0,\qquad{\mbox{$Q$}}\_{w,i}(p):={\mathbb{E}}[{\mbox{$w$}}\_{i,t}(p){\mbox{$w$}}\_{i,t}(p)^{\prime}]>0. |  |

Hence the usual OLS consistency argument for strongly mixing regressors yields

|  |  |  |
| --- | --- | --- |
|  | 𝜽^i​(p)→𝑝𝜽i∗​(p),𝜽i∗​(p):=arg⁡min𝜽⁡𝔼​(yi,t−𝒘i,t​(p)′​𝜽)2,\widehat{{\mbox{$\theta$}}}\_{i}(p)\xrightarrow{p}{\mbox{$\theta$}}\_{i}^{\ast}(p),\qquad{\mbox{$\theta$}}\_{i}^{\ast}(p):=\arg\min\_{{\mbox{$\theta$}}}{\mathbb{E}}\!\big(y\_{i,t}-{\mbox{$w$}}\_{i,t}(p)^{\prime}{\mbox{$\theta$}}\big)^{2}, |  |

for every p∈𝒫p\in\mathcal{P} and i=1,…,Ni=1,\ldots,N.

Define the pseudo-true residual vector

|  |  |  |
| --- | --- | --- |
|  | 𝒆t∗​(p):=(e1,t∗​(p),…,eN,t∗​(p))′,ei,t∗​(p):=yi,t−𝒘i,t​(p)′​𝜽i∗​(p),{\mbox{$e$}}\_{t}^{\ast}(p):=\big(e\_{1,t}^{\ast}(p),\ldots,e\_{N,t}^{\ast}(p)\big)^{\prime},\qquad e\_{i,t}^{\ast}(p):=y\_{i,t}-{\mbox{$w$}}\_{i,t}(p)^{\prime}{\mbox{$\theta$}}\_{i}^{\ast}(p), |  |

and its covariance matrix

|  |  |  |
| --- | --- | --- |
|  | 𝚺u​u​(p):=𝔼​[𝒆t∗​(p)​𝒆t∗​(p)′].{\mbox{$\Sigma$}}\_{uu}(p):={\mathbb{E}}\!\big[{\mbox{$e$}}\_{t}^{\ast}(p){\mbox{$e$}}\_{t}^{\ast}(p)^{\prime}\big]. |  |

Since pmaxp\_{\max} is fixed and 𝒫\mathcal{P} is finite, the above convergences hold uniformly over p∈𝒫p\in\mathcal{P}.

By definition,

|  |  |  |
| --- | --- | --- |
|  | 𝚺^u​u(p):=1T−p∑t=p+1T𝜺^u,t(p)𝜺^u,t(p)′.\widehat{{\mbox{$\Sigma$}}}\_{uu}(p):=\frac{1}{T-p}\sum\_{t=p+1}^{T}\widehat{{\mbox{$\varepsilon$}}}\_{u,t}(p)\widehat{{\mbox{$\varepsilon$}}}\_{u,t}(p)^{\prime}. |  |

Write 𝜺^u,t​(p)=𝒆t∗​(p)+𝒓t​(p)\widehat{{\mbox{$\varepsilon$}}}\_{u,t}(p)={\mbox{$e$}}\_{t}^{\ast}(p)+{\mbox{$r$}}\_{t}(p) where 𝒓t​(p){\mbox{$r$}}\_{t}(p) collects the estimation errors from replacing 𝜽i∗​(p){\mbox{$\theta$}}\_{i}^{\ast}(p) by 𝜽^i​(p)\widehat{{\mbox{$\theta$}}}\_{i}(p). Using 𝜽^i​(p)→𝑝𝜽i∗​(p)\widehat{{\mbox{$\theta$}}}\_{i}(p)\xrightarrow{p}{\mbox{$\theta$}}\_{i}^{\ast}(p), finite (2+δ)(2+\delta)-moments, and a LLN for strongly mixing sequences, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝚺^u​u​(p)=1T−p​∑t=p+1T𝒆t∗​(p)​𝒆t∗​(p)′+op​(1)→𝑝𝚺u​u​(p),\widehat{{\mbox{$\Sigma$}}}\_{uu}(p)=\frac{1}{T-p}\sum\_{t=p+1}^{T}{\mbox{$e$}}\_{t}^{\ast}(p){\mbox{$e$}}\_{t}^{\ast}(p)^{\prime}+o\_{p}(1)\xrightarrow{p}{\mbox{$\Sigma$}}\_{uu}(p), |  |

for each p∈𝒫p\in\mathcal{P}.

Therefore, by the continuous mapping theorem,

|  |  |  |
| --- | --- | --- |
|  | log​det𝚺^u​u​(p)→𝑝log​det𝚺u​u​(p),(p∈𝒫).\log\det\widehat{{\mbox{$\Sigma$}}}\_{uu}(p)\xrightarrow{p}\log\det{\mbox{$\Sigma$}}\_{uu}(p),\qquad(p\in\mathcal{P}). |  |

For p≥p0p\geq p\_{0}, the augmented regression contains all the lags required by finite-predictor exactness, so the population regression is correctly specified with the additional lag coefficients set to zero. Hence ei,t∗​(p)=εu,i,te\_{i,t}^{\ast}(p)=\varepsilon\_{u,i,t} and thus

|  |  |  |
| --- | --- | --- |
|  | 𝚺u​u​(p)=𝚺u​u(p≥p0).{\mbox{$\Sigma$}}\_{uu}(p)={\mbox{$\Sigma$}}\_{uu}\qquad(p\geq p\_{0}). |  |

For p<p0p<p\_{0}, write the omitted component in the stacked Durbin regression as

|  |  |  |
| --- | --- | --- |
|  | 𝜹t​(p):=∑j=p+1p0(𝚿u​u,j​𝒚t−j+𝚲j​𝒙t−j),{\mbox{$\delta$}}\_{t}(p):=\sum\_{j=p+1}^{p\_{0}}\Big({\mbox{$\Psi$}}\_{uu,j}{\mbox{$y$}}\_{t-j}+{\mbox{$\Lambda$}}\_{j}{\mbox{$x$}}\_{t-j}\Big), |  |

so that the (correctly specified) population regression can be written as 𝒚t=𝑾t​(p)′​𝜽​(p)+𝜹t​(p)+𝜺u,t{\mbox{$y$}}\_{t}={\mbox{$W$}}\_{t}(p)^{\prime}{\mbox{$\theta$}}(p)+{\mbox{$\delta$}}\_{t}(p)+{\mbox{$\varepsilon$}}\_{u,t}, where 𝑾t​(p){\mbox{$W$}}\_{t}(p) stacks the same regressors as {𝒘i,t​(p)}i=1N\{{\mbox{$w$}}\_{i,t}(p)\}\_{i=1}^{N}. Let 𝒫p\mathscr{P}\_{p} denote the L2L^{2}-projection onto the closed linear span of 𝑾t​(p){\mbox{$W$}}\_{t}(p). Then we can decompose

|  |  |  |
| --- | --- | --- |
|  | 𝜹t​(p)=𝒫p​[𝜹t​(p)]+𝜻t​(p),𝔼​[𝑾t​(p)​𝜻t​(p)′]=𝟎,{\mbox{$\delta$}}\_{t}(p)=\mathscr{P}\_{p}[{\mbox{$\delta$}}\_{t}(p)]+{\mbox{$\zeta$}}\_{t}(p),\qquad{\mathbb{E}}[{\mbox{$W$}}\_{t}(p){\mbox{$\zeta$}}\_{t}(p)^{\prime}]={\mbox{$0$}}, |  |

where 𝜻t​(p){\mbox{$\zeta$}}\_{t}(p) is the projection residual. By construction, 𝜻t​(p){\mbox{$\zeta$}}\_{t}(p) is measurable with respect to ℱt−1\mathscr{F}\_{t-1} (it is built from lags only), and under E​B​DEBD the innovation 𝜺u,t{\mbox{$\varepsilon$}}\_{u,t} satisfies 𝔼​[𝜺u,t∣ℱt−1]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t}\mid\mathscr{F}\_{t-1}]={\mbox{$0$}}. Therefore 𝔼​[𝜺u,t​𝜻t​(p)′]=𝟎{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t}{\mbox{$\zeta$}}\_{t}(p)^{\prime}]={\mbox{$0$}} and

|  |  |  |
| --- | --- | --- |
|  | 𝒆t∗​(p)=𝜺u,t+𝜻t​(p),𝚺u​u​(p)=𝚺u​u+𝚫​(p),𝚫​(p):=𝔼​[𝜻t​(p)​𝜻t​(p)′]≥0.{\mbox{$e$}}\_{t}^{\ast}(p)={\mbox{$\varepsilon$}}\_{u,t}+{\mbox{$\zeta$}}\_{t}(p),\qquad{\mbox{$\Sigma$}}\_{uu}(p)={\mbox{$\Sigma$}}\_{uu}+{\mbox{$\Delta$}}(p),\quad{\mbox{$\Delta$}}(p):={\mathbb{E}}[{\mbox{$\zeta$}}\_{t}(p){\mbox{$\zeta$}}\_{t}(p)^{\prime}]\geq 0. |  |

Moreover, the minimality of p0p\_{0} in Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") implies that for p<p0p<p\_{0} we cannot have 𝜹t​(p)∈span¯​{𝑾t​(p)}{\mbox{$\delta$}}\_{t}(p)\in\overline{\mathrm{span}}\{{\mbox{$W$}}\_{t}(p)\} (otherwise p0p\_{0} would not be minimal), hence Pr⁡(𝜻t​(p)≠0)>0\Pr({\mbox{$\zeta$}}\_{t}(p)\neq 0)>0 and thus 𝚫​(p)≠0{\mbox{$\Delta$}}(p)\neq 0. Since 𝚺u​u>0{\mbox{$\Sigma$}}\_{uu}>0, we have the strict Loewner inequality 𝚺u​u​(p)>𝚺u​u{\mbox{$\Sigma$}}\_{uu}(p)>{\mbox{$\Sigma$}}\_{uu} for p<p0p<p\_{0}, which implies

|  |  |  |
| --- | --- | --- |
|  | log​det𝚺u​u​(p)>log​det𝚺u​u(p<p0).\log\det{\mbox{$\Sigma$}}\_{uu}(p)>\log\det{\mbox{$\Sigma$}}\_{uu}\qquad(p<p\_{0}). |  |

Consequently, for every fixed p<p0p<p\_{0},

|  |  |  |
| --- | --- | --- |
|  | BICT⁡(p)−BICT⁡(p0)={log​det𝚺^u​u​(p)−log​det𝚺^u​u​(p0)}+{κ​(p)−κ​(p0)}​log⁡TT→𝑝c​(p)>0,\operatorname{BIC}\_{T}(p)-\operatorname{BIC}\_{T}(p\_{0})=\big\{\log\det\widehat{{\mbox{$\Sigma$}}}\_{uu}(p)-\log\det\widehat{{\mbox{$\Sigma$}}}\_{uu}(p\_{0})\big\}+\frac{\{\kappa(p)-\kappa(p\_{0})\}\log T}{T}\xrightarrow{p}c(p)>0, |  |

because the penalty term is o​(1)o(1) while the first term converges to a strictly positive constant. Hence Pr⁡(p^BIC<p0)→0\Pr(\widehat{p}\_{\mathrm{BIC}}<p\_{0})\to 0.

Fix p>p0p>p\_{0}. Since the additional lag coefficients are zero under the true DGP, the fitted model with order pp is a (nested) over-parameterization of the correctly specified order-p0p\_{0} model. Under the maintained regularity conditions (strict stationarity, strong mixing, and finite moments), the Gaussian quasi-likelihood ratio (equivalently, the reduction in the concentrated objective) satisfies the standard chi-square limit:

|  |  |  |
| --- | --- | --- |
|  | (T−p)​{log​det𝚺^u​u​(p0)−log​det𝚺^u​u​(p)}→𝑑χκ​(p)−κ​(p0)2.(T-p)\Big\{\log\det\widehat{{\mbox{$\Sigma$}}}\_{uu}(p\_{0})-\log\det\widehat{{\mbox{$\Sigma$}}}\_{uu}(p)\Big\}\xrightarrow{d}\chi^{2}\_{\kappa(p)-\kappa(p\_{0})}. |  |

In particular,

|  |  |  |
| --- | --- | --- |
|  | log​det𝚺^u​u​(p)−log​det𝚺^u​u​(p0)=Op​(T−1),(p>p0).\log\det\widehat{{\mbox{$\Sigma$}}}\_{uu}(p)-\log\det\widehat{{\mbox{$\Sigma$}}}\_{uu}(p\_{0})=O\_{p}(T^{-1}),\qquad(p>p\_{0}). |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | BICT⁡(p)−BICT⁡(p0)=Op​(T−1)+{κ​(p)−κ​(p0)}​log⁡TT→𝑝0+,\operatorname{BIC}\_{T}(p)-\operatorname{BIC}\_{T}(p\_{0})=O\_{p}(T^{-1})+\frac{\{\kappa(p)-\kappa(p\_{0})\}\log T}{T}\xrightarrow{p}0^{+}, |  |

and more precisely the second term dominates the first because log⁡T→∞\log T\to\infty:

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(BICT⁡(p)>BICT⁡(p0))→1.\Pr\!\Big(\operatorname{BIC}\_{T}(p)>\operatorname{BIC}\_{T}(p\_{0})\Big)\to 1. |  |

Hence Pr⁡(p^BIC>p0)→0\Pr(\widehat{p}\_{\mathrm{BIC}}>p\_{0})\to 0.

Using that 𝒫\mathcal{P} is finite, we obtain

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(p^BIC=p0)→1,\Pr(\widehat{p}\_{\mathrm{BIC}}=p\_{0})\to 1, |  |

which proves p^BIC→𝑝p0\widehat{p}\_{\mathrm{BIC}}\xrightarrow{p}p\_{0}. ∎

### A.9 Proof of Lemma3

Fix i∈{1,…,N}i\in\{1,\ldots,N\} and write the iith Durbin regression on the effective sample t=p0+1,…,Tt=p\_{0}+1,\ldots,T as

|  |  |  |
| --- | --- | --- |
|  | yi,t=𝒘i,t′​𝜽i+εu,i,t,Teff:=T−p0.y\_{i,t}={\mbox{$w$}}\_{i,t}^{\prime}{\mbox{$\theta$}}\_{i}+\varepsilon\_{u,i,t},\qquad T\_{\mathrm{eff}}:=T-p\_{0}. |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜽^iD−𝜽i=(1Teff​∑t=p0+1T𝒘i,t​𝒘i,t′)−1​(1Teff​∑t=p0+1T𝒘i,t​εu,i,t).\widehat{{\mbox{$\theta$}}}\_{i}^{\mathrm{D}}-{\mbox{$\theta$}}\_{i}=\Bigl(\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$w$}}\_{i,t}{\mbox{$w$}}\_{i,t}^{\prime}\Bigr)^{-1}\Bigl(\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}\Bigr). |  | (61) |

Hence it suffices to show

|  |  |  |
| --- | --- | --- |
|  | 1Teff​∑t=p0+1T𝒘i,t​𝒘i,t′→𝑝𝑸w,iwith 𝑸w,i>0,1Teff​∑t=p0+1T𝒘i,t​εu,i,t→𝑝𝟎.\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$w$}}\_{i,t}{\mbox{$w$}}\_{i,t}^{\prime}\xrightarrow{p}{\mbox{$Q$}}\_{w,i}\quad\text{with }{\mbox{$Q$}}\_{w,i}>0,\qquad\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}\xrightarrow{p}{\mbox{$0$}}. |  |

Under Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"), Proposition [1](https://arxiv.org/html/2601.21272v1#Thmproposition1 "Proposition 1: ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(iv) implies that {𝒛t}\{{\mbox{$z$}}\_{t}\} (and hence any finite-dimensional vector formed from finitely many lags/leads of 𝒛t{\mbox{$z$}}\_{t}) is strictly stationary, strongly mixing with summable mixing-rate powers, and has finite (2+δ)(2+\delta)-moments. Since 𝒘i,t{\mbox{$w$}}\_{i,t} is a finite stacking of 11, 𝒙i,t{\mbox{$x$}}\_{i,t}, {𝒚t−j}j=1p0\{{\mbox{$y$}}\_{t-j}\}\_{j=1}^{p\_{0}}, and {𝒙t−j}j=1p0\{{\mbox{$x$}}\_{t-j}\}\_{j=1}^{p\_{0}}, it follows that {𝒘i,t}\{{\mbox{$w$}}\_{i,t}\} and {𝒘i,t​εu,i,t}\{{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}\} are also strictly stationary and strongly mixing, and by Lemma [1](https://arxiv.org/html/2601.21272v1#Thmlemma1 "Lemma 1 (Equation-by-equation properties of the Durbin regression): ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(ii),

|  |  |  |
| --- | --- | --- |
|  | 𝔼​‖𝒘i,t‖2+δ<∞,𝔼​‖𝒘i,t​εu,i,t‖2+δ<∞.{\mathbb{E}}\|{\mbox{$w$}}\_{i,t}\|^{2+\delta}<\infty,\qquad{\mathbb{E}}\|{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}\|^{2+\delta}<\infty. |  |

Therefore, a law of large numbers for strongly mixing sequences applies to {𝒘i,t​𝒘i,t′}\{{\mbox{$w$}}\_{i,t}{\mbox{$w$}}\_{i,t}^{\prime}\} and {𝒘i,t​εu,i,t}\{{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}\}.

First, by Lemma [1](https://arxiv.org/html/2601.21272v1#Thmlemma1 "Lemma 1 (Equation-by-equation properties of the Durbin regression): ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(iii), the second-moment matrix

|  |  |  |
| --- | --- | --- |
|  | 𝑸w,i:=𝔼​[𝒘i,t​𝒘i,t′]{\mbox{$Q$}}\_{w,i}:={\mathbb{E}}[{\mbox{$w$}}\_{i,t}{\mbox{$w$}}\_{i,t}^{\prime}] |  |

is positive definite. Next, we show 𝔼​[𝒘i,t​εu,i,t]=𝟎{\mathbb{E}}[{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}]={\mbox{$0$}}. By Lemma [1](https://arxiv.org/html/2601.21272v1#Thmlemma1 "Lemma 1 (Equation-by-equation properties of the Durbin regression): ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(i), there exist an ℱt−1\mathscr{F}\_{t-1}-measurable vector 𝒉i,t{\mbox{$h$}}\_{i,t} and a deterministic matrix 𝒎i{\mbox{$m$}}\_{i} such that

|  |  |  |
| --- | --- | --- |
|  | 𝒘i,t=𝒉i,t+𝒎i𝜺x,t,ℱt−1:=σ(𝒛s:s≤t−1).{\mbox{$w$}}\_{i,t}={\mbox{$h$}}\_{i,t}+{\mbox{$m$}}\_{i}{\mbox{$\varepsilon$}}\_{x,t},\qquad\mathscr{F}\_{t-1}:=\sigma({\mbox{$z$}}\_{s}:\,s\leq t-1). |  |

Moreover, under each of B​DBD, G​E​X​O​GGEXOG, and E​B​DEBD we have the innovation block-orthogonality 𝚺x​u=𝔼​[𝜺x,t​𝜺u,t′]=𝟎{\mbox{$\Sigma$}}\_{xu}={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{x,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$0$}}. Using that 𝜺u,t{\mbox{$\varepsilon$}}\_{u,t} is the innovation of the joint process, we also have 𝔼​[εu,i,t∣ℱt−1]=0{\mathbb{E}}[\varepsilon\_{u,i,t}\mid\mathscr{F}\_{t-1}]=0. Hence,

|  |  |  |
| --- | --- | --- |
|  | 𝔼[𝒉i,tεu,i,t]=𝔼[𝒉i,t𝔼[εu,i,t∣ℱt−1]]=𝟎,{\mathbb{E}}[{\mbox{$h$}}\_{i,t}\varepsilon\_{u,i,t}]={\mathbb{E}}\!\mathopen{}\left[{\mbox{$h$}}\_{i,t}\,{\mathbb{E}}[\varepsilon\_{u,i,t}\mid\mathscr{F}\_{t-1}]\mathclose{}\right]={\mbox{$0$}}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒎i​𝜺x,t​εu,i,t]=𝒎i​𝔼​[𝜺x,t​εu,i,t]=𝟎.{\mathbb{E}}[{\mbox{$m$}}\_{i}{\mbox{$\varepsilon$}}\_{x,t}\,\varepsilon\_{u,i,t}]={\mbox{$m$}}\_{i}\,{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{x,t}\varepsilon\_{u,i,t}]={\mbox{$0$}}. |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒘i,t​εu,i,t]=𝟎.{\mathbb{E}}[{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}]={\mbox{$0$}}. |  | (62) |

By the LLN for strongly mixing sequences,

|  |  |  |
| --- | --- | --- |
|  | 1Teff​∑t=p0+1T𝒘i,t​𝒘i,t′→𝑝𝔼​[𝒘i,t​𝒘i,t′]=𝑸w,i,\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$w$}}\_{i,t}{\mbox{$w$}}\_{i,t}^{\prime}\xrightarrow{p}{\mathbb{E}}[{\mbox{$w$}}\_{i,t}{\mbox{$w$}}\_{i,t}^{\prime}]={\mbox{$Q$}}\_{w,i}, |  |

and similarly,

|  |  |  |
| --- | --- | --- |
|  | 1Teff​∑t=p0+1T𝒘i,t​εu,i,t→𝑝𝔼​[𝒘i,t​εu,i,t]=𝟎,\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}\xrightarrow{p}{\mathbb{E}}[{\mbox{$w$}}\_{i,t}\varepsilon\_{u,i,t}]={\mbox{$0$}}, |  |

where the last equality uses ([62](https://arxiv.org/html/2601.21272v1#Sx2.E62 "In A.9 Proof of Lemma3 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")). (The omission of the first p0p\_{0} observations is asymptotically negligible because p0p\_{0} is fixed and Teff/T→1T\_{\mathrm{eff}}/T\to 1.) Since 𝑸w,i{\mbox{$Q$}}\_{w,i} is positive definite, the continuous mapping theorem yields

|  |  |  |
| --- | --- | --- |
|  | (1Teff​∑t=p0+1T𝒘i,t​𝒘i,t′)−1→𝑝𝑸w,i−1.\Bigl(\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$w$}}\_{i,t}{\mbox{$w$}}\_{i,t}^{\prime}\Bigr)^{-1}\xrightarrow{p}{\mbox{$Q$}}\_{w,i}^{-1}. |  |

Combining this with ([61](https://arxiv.org/html/2601.21272v1#Sx2.E61 "In A.9 Proof of Lemma3 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")) and Slutsky’s theorem gives

|  |  |  |
| --- | --- | --- |
|  | 𝜽^iD−𝜽i→𝑝𝟎,\widehat{{\mbox{$\theta$}}}\_{i}^{\mathrm{D}}-{\mbox{$\theta$}}\_{i}\xrightarrow{p}{\mbox{$0$}}, |  |

i.e. 𝜽^iD→𝑝𝜽i\widehat{{\mbox{$\theta$}}}\_{i}^{\mathrm{D}}\xrightarrow{p}{\mbox{$\theta$}}\_{i}. ∎

### A.10 Proof of Theorem [1](https://arxiv.org/html/2601.21272v1#Thmtheorem1 "Theorem 1: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")

Write the effective sample as t=p0+1,…,Tt=p\_{0}+1,\ldots,T with Teff:=T−p0T\_{\mathrm{eff}}:=T-p\_{0}.
Throughout, let ∥⋅∥\|\cdot\| denote any matrix norm compatible with multiplication.

Define the infeasible (population) generalized-Durbin transformation using the true nuisance parameters:

|  |  |  |
| --- | --- | --- |
|  | 𝒚GD,t0:=𝒚t−∑j=1p0𝚿u​u,j​𝒚t−j−∑j=1p0𝚿u​x,j​(𝒙t−j−𝝁x),{\mbox{$y$}}\_{\mathrm{GD},t}^{0}:={\mbox{$y$}}\_{t}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$y$}}\_{t-j}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{ux,j}\big({\mbox{$x$}}\_{t-j}-{\mbox{$\mu$}}\_{x}\big), |  |

|  |  |  |
| --- | --- | --- |
|  | 𝒁GD,t0⁣′:=[(𝑰N−∑j=1p0𝚿u​u,j),𝑿t′−∑j=1p0𝚿u​u,j​𝑿t−j′].{\mbox{$Z$}}\_{\mathrm{GD},t}^{0\prime}:=\biggl[\Bigl({\mbox{$I$}}\_{N}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}\Bigr),\ {\mbox{$X$}}\_{t}^{\prime}-\sum\_{j=1}^{p\_{0}}{\mbox{$\Psi$}}\_{uu,j}{\mbox{$X$}}\_{t-j}^{\prime}\biggr]. |  |

Then, by construction from ([23](https://arxiv.org/html/2601.21272v1#S2.E23 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"))–([24](https://arxiv.org/html/2601.21272v1#S2.E24 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚GD,t0=𝒁GD,t0⁣′​𝜿+𝜺u,t,t=p0+1,…,T.{\mbox{$y$}}\_{\mathrm{GD},t}^{0}={\mbox{$Z$}}\_{\mathrm{GD},t}^{0\prime}{\mbox{$\kappa$}}+{\mbox{$\varepsilon$}}\_{u,t},\qquad t=p\_{0}+1,\ldots,T. |  | (63) |

Let 𝚺u​u:=𝔼​[𝜺u,t​𝜺u,t′]{\mbox{$\Sigma$}}\_{uu}:={\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}].
Define the infeasible GLS estimator (using the true 𝚺u​u{\mbox{$\Sigma$}}\_{uu}) by

|  |  |  |
| --- | --- | --- |
|  | 𝜿^ 0:=(1Teff​∑t=p0+1T𝒁GD,t0​𝚺u​u−1​𝒁GD,t0⁣′)−1​(1Teff​∑t=p0+1T𝒁GD,t0​𝚺u​u−1​𝒚GD,t0).\widehat{{\mbox{$\kappa$}}}^{\,0}:=\Bigl(\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0\prime}\Bigr)^{-1}\Bigl(\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$y$}}\_{\mathrm{GD},t}^{0}\Bigr). |  |

We prove (i) 𝜿^GD\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}} is asymptotically equivalent to 𝜿^ 0\widehat{{\mbox{$\kappa$}}}^{\,0},
(ii) 𝜿^ 0\widehat{{\mbox{$\kappa$}}}^{\,0} is consistent and asymptotically normal with asymptotic variance 𝑽V,
and (iii) 𝜿^GD\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}} is asymptotically efficient under E​B​DEBD.

Let 𝜽^D−OLS\widehat{{\mbox{$\theta$}}}^{\mathrm{D\!-\!OLS}} be the stacked first-step Durbin OLS estimator
and define 𝚫:=𝜽^D−OLS−𝜽{\mbox{$\Delta$}}:=\widehat{{\mbox{$\theta$}}}^{\mathrm{D\!-\!OLS}}-{\mbox{$\theta$}}.
By definition,

|  |  |  |
| --- | --- | --- |
|  | 𝜺^u,t=𝒚t−𝑾t′​𝜽^D−OLS=𝜺u,t−𝑾t′​𝚫,\widehat{{\mbox{$\varepsilon$}}}\_{u,t}={\mbox{$y$}}\_{t}-{\mbox{$W$}}\_{t}^{\prime}\widehat{{\mbox{$\theta$}}}^{\mathrm{D\!-\!OLS}}={\mbox{$\varepsilon$}}\_{u,t}-{\mbox{$W$}}\_{t}^{\prime}{\mbox{$\Delta$}}, |  |

where 𝜺u,t{\mbox{$\varepsilon$}}\_{u,t} is the innovation in ([23](https://arxiv.org/html/2601.21272v1#S2.E23 "In 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")).
Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺^u​u\displaystyle\widehat{{\mbox{$\Sigma$}}}\_{uu} | =1Teff​∑t=p0+1T𝜺^u,t​𝜺^u,t′\displaystyle=\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}\widehat{{\mbox{$\varepsilon$}}}\_{u,t}\widehat{{\mbox{$\varepsilon$}}}\_{u,t}^{\prime} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1Teff​∑t=p0+1T𝜺u,t​𝜺u,t′−1Teff​∑t=p0+1T𝜺u,t​(𝑾t′​𝚫)′−1Teff​∑t=p0+1T(𝑾t′​𝚫)​𝜺u,t′\displaystyle=\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$\varepsilon$}}\_{u,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}-\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$\varepsilon$}}\_{u,t}({\mbox{$W$}}\_{t}^{\prime}{\mbox{$\Delta$}})^{\prime}-\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}({\mbox{$W$}}\_{t}^{\prime}{\mbox{$\Delta$}}){\mbox{$\varepsilon$}}\_{u,t}^{\prime} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1Teff​∑t=p0+1T(𝑾t′​𝚫)​(𝑾t′​𝚫)′.\displaystyle\qquad+\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}({\mbox{$W$}}\_{t}^{\prime}{\mbox{$\Delta$}})({\mbox{$W$}}\_{t}^{\prime}{\mbox{$\Delta$}})^{\prime}. |  |

By Assumption [1](https://arxiv.org/html/2601.21272v1#Thmassumption1 "Assumption 1 (Finite-predictor exactness at lag 𝑝₀): ‣ 2.1 Setup ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") (mixing and finite moments),
a LLN yields

|  |  |  |
| --- | --- | --- |
|  | 1Teff​∑t=p0+1T𝜺u,t​𝜺u,t′→𝑝𝔼​[𝜺u,t​𝜺u,t′]=𝚺u​u.\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}{\mbox{$\varepsilon$}}\_{u,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}\xrightarrow{p}{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}]={\mbox{$\Sigma$}}\_{uu}. |  |

Moreover, Lemma [3](https://arxiv.org/html/2601.21272v1#Thmlemma3 "Lemma 3: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") gives ‖𝚫‖=op​(1)\|{\mbox{$\Delta$}}\|=o\_{p}(1), and by Cauchy–Schwarz together with LLN,

|  |  |  |
| --- | --- | --- |
|  | 1Teff​∑t=p0+1T‖𝜺u,t‖​‖𝑾t‖=Op​(1),1Teff​∑t=p0+1T‖𝑾t‖2=Op​(1).\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}\|{\mbox{$\varepsilon$}}\_{u,t}\|\,\|{\mbox{$W$}}\_{t}\|=O\_{p}(1),\qquad\frac{1}{T\_{\mathrm{eff}}}\sum\_{t=p\_{0}+1}^{T}\|{\mbox{$W$}}\_{t}\|^{2}=O\_{p}(1). |  |

Hence the two cross terms are op​(1)o\_{p}(1) and the last quadratic term is also op​(1)o\_{p}(1).
Therefore,

|  |  |  |
| --- | --- | --- |
|  | 𝚺^u​u→𝑝𝚺u​u.\widehat{{\mbox{$\Sigma$}}}\_{uu}\xrightarrow{p}{\mbox{$\Sigma$}}\_{uu}. |  |

Since 𝚺u​u>0{\mbox{$\Sigma$}}\_{uu}>0, eigenvalue continuity implies that 𝚺^u​u\widehat{{\mbox{$\Sigma$}}}\_{uu} is invertible w.p.a.1
and 𝚺^u​u−1→𝑝𝚺u​u−1\widehat{{\mbox{$\Sigma$}}}\_{uu}^{-1}\xrightarrow{p}{\mbox{$\Sigma$}}\_{uu}^{-1}.

From ([63](https://arxiv.org/html/2601.21272v1#Sx2.E63 "In A.10 Proof of Theorem 1 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")),

|  |  |  |
| --- | --- | --- |
|  | 𝜿^ 0−𝜿=(1Teff​∑t𝒁GD,t0​𝚺u​u−1​𝒁GD,t0⁣′)−1​(1Teff​∑t𝒁GD,t0​𝚺u​u−1​𝜺u,t).\widehat{{\mbox{$\kappa$}}}^{\,0}-{\mbox{$\kappa$}}=\Bigl(\frac{1}{T\_{\mathrm{eff}}}\sum\_{t}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0\prime}\Bigr)^{-1}\Bigl(\frac{1}{T\_{\mathrm{eff}}}\sum\_{t}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$\varepsilon$}}\_{u,t}\Bigr). |  |

By a LLN for strongly mixing sequences,

|  |  |  |
| --- | --- | --- |
|  | 1Teff∑t𝒁GD,t0𝚺u​u−1𝒁GD,t0⁣′→𝑝𝔼[𝒁GD,t0𝚺u​u−1𝒁GD,t0⁣′]=:𝑸GD0.\frac{1}{T\_{\mathrm{eff}}}\sum\_{t}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0\prime}\xrightarrow{p}{\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0\prime}]=:{\mbox{$Q$}}\_{\mathrm{GD}}^{0}. |  |

By Assumption [5](https://arxiv.org/html/2601.21272v1#Thmassumption5 "Assumption 5: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(A5.1), 𝑸GD0{\mbox{$Q$}}\_{\mathrm{GD}}^{0} is positive definite, hence nonsingular.

Next define the linear information set

|  |  |  |
| --- | --- | --- |
|  | 𝒢t:=σ(ℱt−1,𝜺x,t),ℱt−1:=σ(𝒛s:s≤t−1).\mathscr{G}\_{t}:=\sigma(\mathscr{F}\_{t-1},{\mbox{$\varepsilon$}}\_{x,t}),\qquad\mathscr{F}\_{t-1}:=\sigma({\mbox{$z$}}\_{s}:s\leq t-1). |  |

As in Lemma [1](https://arxiv.org/html/2601.21272v1#Thmlemma1 "Lemma 1 (Equation-by-equation properties of the Durbin regression): ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(i), 𝒁GD,t0{\mbox{$Z$}}\_{\mathrm{GD},t}^{0} is 𝒢t\mathscr{G}\_{t}-measurable.
Under B​DBD, G​E​X​O​GGEXOG, or E​B​DEBD, we have 𝚺x​u=0{\mbox{$\Sigma$}}\_{xu}=0 and, by the defining orthogonality property of the Wold innovations,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝜺u,t∣𝒢t]=𝟎.{\mathbb{E}}[{\mbox{$\varepsilon$}}\_{u,t}\mid\mathscr{G}\_{t}]={\mbox{$0$}}. |  | (64) |

Hence 𝔼​[𝒁GD,t0​𝚺u​u−1​𝜺u,t]=𝟎{\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$\varepsilon$}}\_{u,t}]={\mbox{$0$}} and a LLN yields

|  |  |  |
| --- | --- | --- |
|  | 1Teff​∑t𝒁GD,t0​𝚺u​u−1​𝜺u,t→𝑝𝟎,\frac{1}{T\_{\mathrm{eff}}}\sum\_{t}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$\varepsilon$}}\_{u,t}\xrightarrow{p}{\mbox{$0$}}, |  |

which implies 𝜿^ 0→𝑝𝜿\widehat{{\mbox{$\kappa$}}}^{\,0}\xrightarrow{p}{\mbox{$\kappa$}}.

For asymptotic normality, set 𝝍t:=𝒁GD,t0​𝚺u​u−1​𝜺u,t{\mbox{$\psi$}}\_{t}:={\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$\varepsilon$}}\_{u,t}.
A multivariate CLT for strongly mixing sequences gives

|  |  |  |
| --- | --- | --- |
|  | 1Teff​∑t𝝍t→𝑑𝒩​(𝟎,𝑺),𝑺:=∑h∈ℤ𝔼​[𝝍t​𝝍t−h′].\frac{1}{\sqrt{T\_{\mathrm{eff}}}}\sum\_{t}{\mbox{$\psi$}}\_{t}\xrightarrow{d}\mathcal{N}({\mbox{$0$}},{\mbox{$S$}}),\qquad{\mbox{$S$}}:=\sum\_{h\in\mathbb{Z}}{\mathbb{E}}[{\mbox{$\psi$}}\_{t}{\mbox{$\psi$}}\_{t-h}^{\prime}]. |  |

We simplify 𝑺S.
Fix h≥1h\geq 1. Since 𝝍t−h{\mbox{$\psi$}}\_{t-h} is ℱt−1\mathscr{F}\_{t-1}-measurable, it is 𝒢t\mathscr{G}\_{t}-measurable.
Thus, by the tower property and ([64](https://arxiv.org/html/2601.21272v1#Sx2.E64 "In A.10 Proof of Theorem 1 ‣ Appendix ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")),

|  |  |  |
| --- | --- | --- |
|  | 𝔼[𝝍t𝝍t−h′]=𝔼[𝔼(𝝍t∣𝒢t)𝝍t−h′]=𝔼[𝒁GD,t0𝚺u​u−1𝔼(𝜺u,t∣𝒢t)𝝍t−h′]=𝟎.{\mathbb{E}}[{\mbox{$\psi$}}\_{t}{\mbox{$\psi$}}\_{t-h}^{\prime}]={\mathbb{E}}\!\mathopen{}\left[{\mathbb{E}}({\mbox{$\psi$}}\_{t}\mid\mathscr{G}\_{t})\,{\mbox{$\psi$}}\_{t-h}^{\prime}\mathclose{}\right]={\mathbb{E}}\!\mathopen{}\left[{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mathbb{E}}({\mbox{$\varepsilon$}}\_{u,t}\mid\mathscr{G}\_{t})\,{\mbox{$\psi$}}\_{t-h}^{\prime}\mathclose{}\right]={\mbox{$0$}}. |  |

By symmetry, 𝔼​[𝝍t​𝝍t+h′]=𝟎{\mathbb{E}}[{\mbox{$\psi$}}\_{t}{\mbox{$\psi$}}\_{t+h}^{\prime}]={\mbox{$0$}} for h≥1h\geq 1 as well.
Hence 𝑺=𝔼​[𝝍t​𝝍t′]{\mbox{$S$}}={\mathbb{E}}[{\mbox{$\psi$}}\_{t}{\mbox{$\psi$}}\_{t}^{\prime}].

Using Assumption [5](https://arxiv.org/html/2601.21272v1#Thmassumption5 "Assumption 5: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models")(A5.2) with σ​(𝒁GD,t0)\sigma({\mbox{$Z$}}\_{\mathrm{GD},t}^{0}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑺S | =𝔼[𝒁GD,t0𝚺u​u−1𝜺u,t𝜺u,t′𝚺u​u−1𝒁GD,t0⁣′]\displaystyle={\mathbb{E}}\!\mathopen{}\left[{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$\varepsilon$}}\_{u,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0\prime}\mathclose{}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼[𝒁GD,t0𝚺u​u−1𝔼(𝜺u,t𝜺u,t′∣σ(𝒁GD,t0))𝚺u​u−1𝒁GD,t0⁣′]\displaystyle={\mathbb{E}}\!\mathopen{}\left[{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}\,{\mathbb{E}}\!\bigl({\mbox{$\varepsilon$}}\_{u,t}{\mbox{$\varepsilon$}}\_{u,t}^{\prime}\mid\sigma({\mbox{$Z$}}\_{\mathrm{GD},t}^{0})\bigr)\,{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0\prime}\mathclose{}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼[𝒁GD,t0𝚺u​u−1𝚺u​u𝚺u​u−1𝒁GD,t0⁣′]=𝔼[𝒁GD,t0𝚺u​u−1𝒁GD,t0⁣′]=𝑸GD0.\displaystyle={\mathbb{E}}\!\mathopen{}\left[{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$\Sigma$}}\_{uu}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0\prime}\mathclose{}\right]={\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{GD},t}^{0}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{GD},t}^{0\prime}]={\mbox{$Q$}}\_{\mathrm{GD}}^{0}. |  |

Therefore, with 𝑽:=(𝑸GD0)−1{\mbox{$V$}}:=({\mbox{$Q$}}\_{\mathrm{GD}}^{0})^{-1},

|  |  |  |
| --- | --- | --- |
|  | Teff​(𝜿^ 0−𝜿)→𝑑𝒩​(𝟎,𝑽).\sqrt{T\_{\mathrm{eff}}}\,(\widehat{{\mbox{$\kappa$}}}^{\,0}-{\mbox{$\kappa$}})\xrightarrow{d}\mathcal{N}({\mbox{$0$}},{\mbox{$V$}}). |  |

Define the feasible generalized-Durbin transformation as in the theorem and proceed exactly as in your original proof to show
𝜿^GD−𝜿^ 0=op​(1)\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-\widehat{{\mbox{$\kappa$}}}^{\,0}=o\_{p}(1) (and under Teff\sqrt{T\_{\mathrm{eff}}}-consistency of first-step pieces,
Teff​(𝜿^GD−𝜿^ 0)=op​(1)\sqrt{T\_{\mathrm{eff}}}(\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-\widehat{{\mbox{$\kappa$}}}^{\,0})=o\_{p}(1)).
Combining yields the stated limit distribution with 𝑽=(𝑸GD0)−1{\mbox{$V$}}=({\mbox{$Q$}}\_{\mathrm{GD}}^{0})^{-1}.

The efficiency argument under E​B​DEBD is unchanged from your original proof. ∎

### A.11 Proof of Corollary1

By Theorem [1](https://arxiv.org/html/2601.21272v1#Thmtheorem1 "Theorem 1: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models"),

|  |  |  |
| --- | --- | --- |
|  | Teff​(𝜿^GD−𝜿)→𝑑𝒩​(𝟎,𝑽),𝑽=(𝔼​[𝒁GD,t​𝚺u​u−1​𝒁GD,t′])−1,\sqrt{T\_{\mathrm{eff}}}\,(\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$\kappa$}})\ \xrightarrow{d}\ \mathcal{N}({\mbox{$0$}},{\mbox{$V$}}),\qquad{\mbox{$V$}}=\Big({\mathbb{E}}[{\mbox{$Z$}}\_{\mathrm{GD},t}{\mbox{$\Sigma$}}\_{uu}^{-1}{\mbox{$Z$}}\_{\mathrm{GD},t}^{\prime}]\Big)^{-1}, |  |

where 𝑽V is positive definite. Under H0:𝑹𝜿=𝒓H\_{0}:\ {\mbox{$R$}}{\mbox{$\kappa$}}={\mbox{$r$}},

|  |  |  |
| --- | --- | --- |
|  | 𝑹​𝜿^GD−𝒓=𝑹​(𝜿^GD−𝜿),{\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$r$}}={\mbox{$R$}}(\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$\kappa$}}), |  |

and hence, by linearity,

|  |  |  |
| --- | --- | --- |
|  | Teff​(𝑹​𝜿^GD−𝒓)→𝑑𝒩​(𝟎,𝑹𝑽𝑹′).\sqrt{T\_{\mathrm{eff}}}\,({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$r$}})\ \xrightarrow{d}\ \mathcal{N}\big({\mbox{$0$}},\ {\mbox{$R$}}{\mbox{$V$}}{\mbox{$R$}}^{\prime}\big). |  |

Let 𝑽∗:=𝑹𝑽𝑹′{\mbox{$V$}}^{\*}:={\mbox{$R$}}{\mbox{$V$}}{\mbox{$R$}}^{\prime}. Since rank⁡(𝑹)=q\operatorname{rank}({\mbox{$R$}})=q and 𝑽>0{\mbox{$V$}}>0, it follows that 𝑽∗>0{\mbox{$V$}}^{\*}>0.

Moreover, by Theorem [1](https://arxiv.org/html/2601.21272v1#Thmtheorem1 "Theorem 1: ‣ 2.5 Asymptotic properties of generalized Durbin estimator ‣ 2 Model and Test ‣ Finite-Sample Properties of Model Specification Tests for Multivariate Dynamic Regression Models") we have 𝑽^→𝑝𝑽\widehat{{\mbox{$V$}}}\xrightarrow{p}{\mbox{$V$}}, and thus
𝑽^∗:=𝑹​𝑽^​𝑹′→𝑝𝑽∗\widehat{{\mbox{$V$}}}^{\*}:={\mbox{$R$}}\widehat{{\mbox{$V$}}}{\mbox{$R$}}^{\prime}\xrightarrow{p}{\mbox{$V$}}^{\*}.
Therefore, using the (symmetric) matrix square root, (𝑽^∗)−1/2→𝑝(𝑽∗)−1/2(\widehat{{\mbox{$V$}}}^{\*})^{-1/2}\xrightarrow{p}({\mbox{$V$}}^{\*})^{-1/2}, and Slutsky’s theorem yields

|  |  |  |
| --- | --- | --- |
|  | (𝑽^∗)−1/2​Teff​(𝑹​𝜿^GD−𝒓)→𝑑𝒩​(𝟎,𝑰q).(\widehat{{\mbox{$V$}}}^{\*})^{-1/2}\,\sqrt{T\_{\mathrm{eff}}}\,({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$r$}})\ \xrightarrow{d}\ \mathcal{N}({\mbox{$0$}},{\mbox{$I$}}\_{q}). |  |

Finally, by the continuous mapping theorem applied to the quadratic form,

|  |  |  |
| --- | --- | --- |
|  | 𝒲GD=Teff​(𝑹​𝜿^GD−𝒓)′​(𝑽^∗)−1​(𝑹​𝜿^GD−𝒓)=‖(𝑽^∗)−1/2​Teff​(𝑹​𝜿^GD−𝒓)‖2→𝑑χq2.\mathcal{W}^{\mathrm{GD}}=T\_{\mathrm{eff}}({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$r$}})^{\prime}(\widehat{{\mbox{$V$}}}^{\*})^{-1}({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$r$}})=\big\|(\widehat{{\mbox{$V$}}}^{\*})^{-1/2}\sqrt{T\_{\mathrm{eff}}}({\mbox{$R$}}\widehat{{\mbox{$\kappa$}}}^{\mathrm{GD}}-{\mbox{$r$}})\big\|^{2}\ \xrightarrow{d}\ \chi^{2}\_{q}. |  |

∎