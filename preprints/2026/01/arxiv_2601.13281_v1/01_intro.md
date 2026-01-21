---
authors:
- Koos B. Gubbels
- Andre Lucas
doc_id: arxiv:2601.13281v1
family_id: arxiv:2601.13281
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Spectral Dynamics and Regularization for High-Dimensional Copulas
url_abs: http://arxiv.org/abs/2601.13281v1
url_html: https://arxiv.org/html/2601.13281v1
venue: arXiv q-fin
version: 1
year: 2026
---


Koos B. Gubbels
[k.b.gubbels@tilburguniversity.edu](mailto:k.b.gubbels@tilburguniversity.edu)

Andre Lucas
[a.lucas@vu.nl](mailto:a.lucas@vu.nl)

###### Abstract

We introduce a novel model for time-varying, asymmetric, tail-dependent copulas in high dimensions that incorporates both spectral dynamics and regularization.
The dynamics of the dependence matrix’ eigenvalues are modeled in a score-driven way, while biases in the unconditional eigenvalue spectrum are resolved by non-linear shrinkage.
The dynamic parameterization of the copula dependence matrix ensures that it satisfies the appropriate restrictions at all times and for any dimension.
The model is parsimonious, computationally efficient, easily scalable to high dimensions, and performs well for both simulated and empirical data.
In an empirical application to financial market dynamics using 100 stocks from 10 different countries and 10 different industry sectors, we find that our copula model captures both geographic and industry related co-movements and outperforms recent computationally more intensive clustering-based factor copula alternatives.
Both the spectral dynamics and the regularization contribute to the new model’s performance.
During periods of market stress, we find that the spectral dynamics reveal strong increases in international stock market dependence, which causes reductions in diversification potential and increases in systemic risk.

###### keywords:

Copulas
, principal components
, time-varying eigenvalues
, non-linear shrinkage
, high-dimensional dependence.

††journal: t.b.d.

\NAT@set@cites

\affiliation

[UvT]organization=Department of Econometrics and Operations Research, Tilburg University,city=Tilburg,
country=The Netherlands

\affiliation

[VU]
organization=Department of Econometrics and Data Science and Tinbergen Institute, Vrije Universiteit Amsterdam,
city=Amsterdam,
country=The Netherlands

## 1 Introduction

High-dimensional models for dependence play an important role in quantitative risk management and finance; for an overview, see, e.g., McNeil et al. [[2005](https://arxiv.org/html/2601.13281v1#bib.bib35 "Quantitative risk management")].
In such high-dimensional settings, standard multivariate densities are typically too tightly parameterized to describe the data well.
The standard solution to this problem, which is also adopted in this article, is to use the more flexible copula perspective.
Here, one splits the modeling process into two steps: a first stage where one builds univariate models for the marginal properties of each of the observed time series, and a second stage where one formulates a copula to capture the multivariate dependence structure between the different series [see for instance Joe, [2006](https://arxiv.org/html/2601.13281v1#bib.bib26 "Dependence modeling with copulas")].

To capture financial market data well, there are three stylized facts that any good copula model should pick up, namely (i) time-variation of the dependence structure, (ii) asymmetry, and (iii) tail-dependence.
In addition, a good high-dimensional copula model should be able to deal with (iv) the increase in the number of parameters as the dimensionality grows, and (v) the biases arising in a high-dimensional context for typical dependence measures like covariance matrices or copula dependence matrices [see, for instance, Ledoit and Wolf, [2004b](https://arxiv.org/html/2601.13281v1#bib.bib52 "Honey, i shrunk the covariance matrix"), [2012](https://arxiv.org/html/2601.13281v1#bib.bib51 "Nonlinear shrinkage estimation of large-dimensional covariance matrices")].
Earlier literature typically deals with some, but not all of these challenges simultaneously, and a unified model dealing with all these challenges at the same time is currently lacking.
For instance, Lucas et al. [[2017](https://arxiv.org/html/2601.13281v1#bib.bib34 "Modeling financial sector joint tail risk in the euro area")] use a dynamic, skewed and fat-tailed copula model for the time-varying dependence between 73 sovereigns and banks, but adopt a highly restrictive block-equicorrelation structure as in Engle and Kelly [[2012](https://arxiv.org/html/2601.13281v1#bib.bib19 "Dynamic equicorrelation")] to keep the number of parameters manageable in high dimensions.
Engle et al. [[2019](https://arxiv.org/html/2601.13281v1#bib.bib20 "Large dynamic covariance matrices")] on the other hand consider a vast-dimensional setting and use non-linear shrinkage to overcome the biases in the estimation of the long-term mean of the dynamic correlation matrix in the DCC specification of Engle [[2002](https://arxiv.org/html/2601.13281v1#bib.bib18 "Dynamic conditional correlation: a simple class of multivariate generalized autoregressive conditional heteroskedasticity models")].
They do not take a copula perspective, however, and do not account for possible skewness in the dependence structure.
Moreover, if dd denotes the number of assets, their dynamics are imposed on the entire d×dd\times d correlation matrix via the DCC specification, rather than on the dynamics of the much lower dimensional spectrum itself.

A different stream of literature use a factor-based copula approach with exogenous [Creal and S., [2015](https://arxiv.org/html/2601.13281v1#bib.bib9 "High dimensional dynamic stochastic copula models"), Oh and Patton, [2017](https://arxiv.org/html/2601.13281v1#bib.bib38 "Modeling dependence in high dimensions with factor copulas"), Opschoor et al., [2021](https://arxiv.org/html/2601.13281v1#bib.bib41 "Closed-form multi-factor copula models with observation-driven dynamic factor loadings")] or endogenous [via clustering; Oh and Patton, [2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")] assignment of cross-sectional units to groups with similar factor exposures.
These factor copulas are typically dynamic and fat-tailed (and sometimes skewed), whereas the dimensionality challenges are tackled via the allocation of assets to groups and the pooling of factor loadings.
Such group structures may, however, not be exact or may not even exist in particular applications, in which case a group-based factor copula model approach can become suboptimal or even biased.
Moreover, endogenously deciding on the number of clusters and factors in the context of a non-linear dynamic model can be quite challenging and become computationally prohibitively expensive in high dimensions.

In this article, we therefore propose a new high-dimensional copula model that addresses all the above challenges in one unified framework.
Our copula model includes skewness and tail dependence by starting from the generalized hyperbolic skewed tt copula as in, for instance, Lucas et al. [[2017](https://arxiv.org/html/2601.13281v1#bib.bib34 "Modeling financial sector joint tail risk in the euro area")].
We address the challenge of high-dimensionality by focusing on the spectral decomposition of the dependence matrix, modeling the dominant eigenvalues as dynamic, while keeping the remaining eigenvalues static and debiasing the eigenvalue spectrum using non-linear shrinkage techniques developed by Ledoit and Wolf [[2022b](https://arxiv.org/html/2601.13281v1#bib.bib30 "The power of (non-) linear shrinking: a review and guide to covariance matrix estimation"), [a](https://arxiv.org/html/2601.13281v1#bib.bib31 "Quadratic shrinkage for large covariance matrices")].
Hetland et al. [[2023](https://arxiv.org/html/2601.13281v1#bib.bib47 "Dynamic conditional eigenvalue garch")] study eigenvalue dynamics of a covariance matrix in a low-dimensional context and find that the score-driven dynamics of Creal et al. [[2013](https://arxiv.org/html/2601.13281v1#bib.bib8 "Generalized autoregressive score models with applications")] and Harvey [[2013](https://arxiv.org/html/2601.13281v1#bib.bib23 "Dynamic models for volatility and heavy tails: with applications to financial and economic time series")] work well for eigenvalues.
We extend their framework (i) to a copula context with skewness and fat-tailedness, and (ii) to a high-dimensional context by including the regularization techniques required for debiasing the spectrum [Ledoit and Wolf, [2004a](https://arxiv.org/html/2601.13281v1#bib.bib29 "A well-conditioned estimator for large-dimensional covariance matrices"), [2022b](https://arxiv.org/html/2601.13281v1#bib.bib30 "The power of (non-) linear shrinking: a review and guide to covariance matrix estimation"), [2022a](https://arxiv.org/html/2601.13281v1#bib.bib31 "Quadratic shrinkage for large covariance matrices")].
In contrast to Hetland et al. [[2023](https://arxiv.org/html/2601.13281v1#bib.bib47 "Dynamic conditional eigenvalue garch")], we explicitly distinguish between the marginal and the copula time series.
Therefore, our dynamic eigenvalues solely reflect the dependence structure, allowing us to show that market movements with increased dependence are followed by subsequent periods with high dependence.

We show in a simulation study that our copula model can recover cluster-based dependence structures with limited performance loss compared to cluster factor copulas of Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")] if the latter form the true data generating process (dgp).
However, when the dependence structure increasingly deviates from an exact group structure, our high-dimensional copulas pick up the dependence structure more accurately than the cluster-based factor copula alternative.
In an application to the dynamic dependence structure of global financial markets using 100 stocks from 10 different countries and 10 different industry sectors, we corroborate these results.
So far, high-dimensional copula studies have mainly focused on stocks from a single country, such as the US [Oh and Patton, [2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")].
The large number of possible country and sector combinations in our current application complicates the detection of a proper factor structure using standard clustering approaches.
We find that high-dimensional copulas with regularized spectral dynamics perform well under these challenging circumstances.
For the empirical data considered in the application, both the dynamics of the spectrum and the regularization of the spectrum contribute to the new model’s performance.
Moreover, the spectral copula dynamics reveal that in times of financial distress the stock market dependence structure stretches along the first spectral dimension, reducing diversification possibilities and increasing systemic risk.

The remainder of the paper is structured as follows.
In Section [2](https://arxiv.org/html/2601.13281v1#S2 "2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") we introduce the modeling framework and discuss regularization of the dynamic spectra and estimation of the static parameters.
Section [3](https://arxiv.org/html/2601.13281v1#S3 "3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") presents simulation evidence.
Section [4](https://arxiv.org/html/2601.13281v1#S4 "4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") applies the new model to global financial markets.
Section [5](https://arxiv.org/html/2601.13281v1#S5 "5 Conclusion ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") concludes.

## 2 The model

### 2.1 Generalized hyperbolic skewed t copula

Consider a vector-valued time series 𝒚t=(y1,t,…,yd,t)⊤∈ℝd×1\bm{y}\_{t}=(y\_{1,t},\ldots,y\_{d,t})^{\top}\in\mathbb{R}^{d\times 1} observed for t=1,…,Tt=1,\ldots,T.
For each yi,ty\_{i,t}, assume the availability of a conditional marginal model in the form of a cumulative distribution function (cdf) Fi(⋅|ℱt−1)F\_{i}(\,\cdot\,|\mathcal{F}\_{t-1}) for a common information set ℱt={𝒚s}s≤t\mathcal{F}\_{t}=\{\bm{y}\_{s}\}\_{s\leq t}; see Patton [[2006](https://arxiv.org/html/2601.13281v1#bib.bib48 "Modelling asymmetric exchange rate dependence")].
We use these marginal models to construct conditional probability integral transforms (PITs) 𝒖t=(u1,t,…,ud,t)⊤∈ℝd×1\bm{u}\_{t}=(u\_{1,t},\ldots,u\_{d,t})^{\top}\in\mathbb{R}^{d\times 1} with ui,t=Fi​(yi,t∣ℱt−1)u\_{i,t}=F\_{i}(y\_{i,t}\mid\mathcal{F}\_{t-1}), whose multivariate distribution is the main focus in the remainder of our analysis.
We assume the following dynamic conditional copula specification for the PITs:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒖t\displaystyle\bm{u}\_{t} | ∼c​(𝒖t∣ℱt−1,𝜽c,t)=c​(𝒖t;𝜽c,t)=g​(G1−1​(u1,t;𝜽c,t),…,Gd−1​(ud,t;𝜽c,t))g1​(G1−1​(u1,t;𝜽c,t))​⋯​gd​(Gd−1​(ud,t;𝜽c,t)),\displaystyle\sim c(\bm{u}\_{t}\mid\mathcal{F}\_{t-1},\bm{\theta}\_{c,t})=c(\bm{u}\_{t};\bm{\theta}\_{c,t})=\frac{g\left(G\_{1}^{-1}(u\_{1,t};\bm{\theta}\_{c,t}),\ldots,G\_{d}^{-1}(u\_{d,t};\bm{\theta}\_{c,t})\right)}{g\_{1}\left(G\_{1}^{-1}(u\_{1,t};\bm{\theta}\_{c,t})\right)\cdots g\_{d}\left(G\_{d}^{-1}(u\_{d,t};\bm{\theta}\_{c,t})\right)}, |  | (1) |

where the dynamic copula parameter 𝜽c,t\bm{\theta}\_{c,t} summarizes all the dependence information from the information set ℱt−1\mathcal{F}\_{t-1} as needed for the copula, and where g​(⋅)g(\,\cdot\,) is an appropriate multivariate density with marginal pdfs gi​(⋅;⋅)g\_{i}(\,\cdot\,;\,\cdot\,) and cdfs Gi​(⋅;⋅)G\_{i}(\,\cdot\,;\,\cdot\,) for i=1,…,di=1,\ldots,d.
As an appropriate choice for g​(⋅;⋅)g(\,\cdot\,;\,\cdot\,), we consider the multivariate generalized hyperbolic skewed tt copula with degrees-of-freedom parameter ν\nu, skewness parameter 𝜸\bm{\gamma}, and scale matrix 𝑹t=𝑹​(𝜽c,t)\bm{R}\_{t}=\bm{R}(\bm{\theta}\_{c,t}), as generated by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g​(𝒚⋆t;𝜽c,t)\displaystyle g\left(\bm{y^{\star}}\_{t};\bm{\theta}\_{c,t}\right) | =2−ν/2+1​νν/2​αt(d+ν)/2(2​π)d/2​Γ​(ν/2)​|𝑹t|1/2​e𝒚⋆t​𝜷t⊤​K(ν+d)/2​(αt​ν+𝒚⋆t​𝑹t−1⊤​𝒚⋆t)(ν+𝒚⋆t​𝑹t−1⊤​𝒚⋆t)(d+ν)/4,\displaystyle=\frac{2^{-\nu/2+1}\nu^{\nu/2}\alpha\_{t}^{(d+\nu)/2}}{(2\pi)^{d/2}\Gamma(\nu/2)|\bm{R}\_{t}|^{1/2}}\frac{e^{\bm{y^{\star}}\_{t}{}^{\top}\bm{\beta}\_{t}}K\_{(\nu+d)/2}\left(\alpha\_{t}\sqrt{\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t}}\right)}{\left(\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t}\right)^{(d+\nu)/4}}, |  | (2) |

where 𝒚⋆t=(y1,t⋆,…,yd,t⋆)⊤\bm{y^{\star}}\_{t}=(y^{\star}\_{1,t},\ldots,y^{\star}\_{d,t})^{\top}, with yi,t⋆=Gi−1​(ui,t;𝜽c,t)=Gi−1​(ui,t;ν,γi)y^{\star}\_{i,t}=G\_{i}^{-1}\left(u\_{i,t};\bm{\theta}\_{c,t}\right)=G\_{i}^{-1}\left(u\_{i,t};\nu,\gamma\_{i}\right) for i=1,…,di=1,\ldots,d, and where 𝜷t=𝑹t−1​𝜸\bm{\beta}\_{t}=\bm{R}\_{t}^{-1}\bm{\gamma} and αt=(𝜸⊤​𝑹t−1​𝜸)1/2\alpha\_{t}=(\bm{\gamma}^{\top}\bm{R}\_{t}^{-1}\bm{\gamma})^{1/2}; see also Demarta and McNeil [[2005](https://arxiv.org/html/2601.13281v1#bib.bib11 "The t copula and related copulas")].
As the marginal scales of the copula are not identified, we restrict the diagonal of 𝑹t\bm{R}\_{t} to be equal to one, such that 𝑹t\bm{R}\_{t} has a correlation matrix form.

The multivariate generalized hyperbolic skewed tt distribution in ([2](https://arxiv.org/html/2601.13281v1#S2.E2 "In 2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) can be constructed as a mean-variance mixture

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒚⋆t\displaystyle\bm{y^{\star}}\_{t} | =\varvt​𝜸+\varvt​𝑹t1/2​𝒛t,\displaystyle=\varv\_{t}\,\bm{\gamma}+\sqrt{\varv\_{t}}\,\bm{R}\_{t}^{1/2}\bm{z}\_{t}, |  | (3) |

where 𝒛t∼N​(𝟎d,𝐈d)\bm{z}\_{t}\sim{\rm N}(\bm{0}\_{d},\mathbf{I}\_{d}) is a multivariate standard normally distributed random variable, and \varvt∼IG​(ν/2,ν/2)\varv\_{t}\sim{\rm IG}(\nu/2,\nu/2) is Inverse Gamma distributed and independent of 𝒛t\bm{z}\_{t}.
Here 𝑹t1/2\bm{R}\_{t}^{1/2} denotes the symmetric root of 𝑹t\bm{R}\_{t}.
The above distribution has been a popular choice to study dynamic dependence structures in financial markets [Lucas et al., [2014](https://arxiv.org/html/2601.13281v1#bib.bib33 "Conditional euro area sovereign default risk"), Opschoor et al., [2021](https://arxiv.org/html/2601.13281v1#bib.bib41 "Closed-form multi-factor copula models with observation-driven dynamic factor loadings"), Oh and Patton, [2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")].
The distribution is both flexible and analytically tractable and accommodates skewness as well as fat tails.
It is immediately clear from ([3](https://arxiv.org/html/2601.13281v1#S2.E3 "In 2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) that the marginal distribution of yi,t⋆y^{\star}\_{i,t} is univariate skewed tt with shape parameter ν\nu, skewness parameter γi\gamma\_{i}, and scale parameter 1.
The marginal pdfs gi​(⋅;⋅)g\_{i}(\,\cdot\,;\,\cdot\,) in ([1](https://arxiv.org/html/2601.13281v1#S2.E1 "In 2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) are thus known analytically.

### 2.2 Spectral dynamics

The core challenge for a high-dimensional time-varying copula model is the curse of dimensionality and the explosion of the number of free parameters in 𝑹t\bm{R}\_{t}.
Different solutions have been proposed.
Oh and Patton [[2018](https://arxiv.org/html/2601.13281v1#bib.bib39 "Time-varying systemic risk: evidence from a dynamic copula model of cds spreads")] and Opschoor et al. [[2021](https://arxiv.org/html/2601.13281v1#bib.bib41 "Closed-form multi-factor copula models with observation-driven dynamic factor loadings")] study factor copulas where 𝑹t\bm{R}\_{t} is decomposed into a low-rank matrix plus a diagonal matrix, both of which can vary over time.
Further parsimony can be imposed by pooling the dynamic parameters across pre-specified groups, for example, industries, or by choosing the groups in a data-driven way, e.g., using clustering techniques as in Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")].
Clustering in the context of a non-linear model can quickly become time-consuming if either the sample size or the number of assets becomes large.
Moreover, clustering techniques may face challenges if the cluster structure is only approximate; see Section [3](https://arxiv.org/html/2601.13281v1#S3 "3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") for the effects of such deviations in a controlled setting.

To overcome these issues, we do not impose a group structure, but instead use a normalized spectral decomposition of the copula dependence matrix 𝑹t\bm{R}\_{t} by imposing

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑹t\displaystyle\bm{R}\_{t} | =diag(𝑾𝚲t𝑾⊤)−1/2𝑾𝚲t𝑾⊤diag(𝑾𝚲t𝑾⊤)−1/2,\displaystyle=\operatorname{diag}\left(\bm{W}\bm{\Lambda}\_{t}\bm{W}^{\top}\right)^{-1/2}\ \bm{W}\bm{\Lambda}\_{t}\bm{W}^{\top}\operatorname{diag}\left(\bm{W}\bm{\Lambda}\_{t}\bm{W}^{\top}\right)^{-1/2}, |  | (4) |

where 𝑾\bm{W} is orthogonal and 𝚲t\bm{\Lambda}\_{t} is time-varying and diagonal with strictly positive entries.
Note that the parameterization of 𝑹t\bm{R}\_{t} automatically ensures that 𝑹t\bm{R}\_{t} has the format of a correlation matrix as long as the diagonal elements of 𝚲t\bm{\Lambda}\_{t} are strictly positive.
The latter can be ensured by using an exponential link function for the diagonal elements of 𝚲t\bm{\Lambda}\_{t}.
Alternatives for parameterizing dynamic correlation matrices are, for example, the hypersphere parameterization of Jaeckel and Rebonato [[2000](https://arxiv.org/html/2601.13281v1#bib.bib54 "The most general methodology for creating a valid correlation matrix for risk management and option pricing purposes")] as used in Creal et al. [[2011](https://arxiv.org/html/2601.13281v1#bib.bib53 "A dynamic multivariate heavy-tailed model for time-varying volatilities and correlations")] and Buccheri et al. [[2021](https://arxiv.org/html/2601.13281v1#bib.bib57 "A score-driven conditional correlation model for noisy and asynchronous data: an application to high-frequency covariance dynamics")], or the log-correlation matrix parameterization of Archakov and Hansen [[2021](https://arxiv.org/html/2601.13281v1#bib.bib55 "A new parametrization of correlation matrices")] as used in Hafner and Wang [[2023](https://arxiv.org/html/2601.13281v1#bib.bib56 "A dynamic conditional score model for the log correlation matrix")].
By concentrating on the eigenvalues, the number of free dynamic parameters is considerably less than in these alternative parameterizations, which helps for the model’s tractability in high-dimensional settings.
Moreover, the spectral parameterization of the correlation matrix in ([4](https://arxiv.org/html/2601.13281v1#S2.E4 "In 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) still allows for explicit derivative expressions with respect to all nonzero elements in 𝚲t\bm{\Lambda}\_{t}.

We describe the dynamics of 𝚲t\bm{\Lambda}\_{t} using the score-driven approach of Creal et al. [[2013](https://arxiv.org/html/2601.13281v1#bib.bib8 "Generalized autoregressive score models with applications")] and Harvey [[2013](https://arxiv.org/html/2601.13281v1#bib.bib23 "Dynamic models for volatility and heavy tails: with applications to financial and economic time series")],

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒇t+1\displaystyle\bm{f}\_{t+1} | =𝝎+𝑩​𝒇t+𝑨​∇t,\displaystyle=\bm{\omega}+\bm{B}\,\bm{f}\_{t}+\bm{A}\,\bm{\nabla}\_{t}, |  | (5) |

where ∇t=∂g​(𝒚⋆t;𝜽c,t)/∂𝒇t\bm{\nabla}\_{t}=\partial g(\bm{y^{\star}}\_{t};\bm{\theta}\_{c,t})/\partial\bm{f}\_{t} is the score of the copula density, 𝒇t=log⁡𝝀t\bm{f}\_{t}=\log\bm{\lambda}\_{t}, and where we use unit scaling as defined by Creal et al. [[2013](https://arxiv.org/html/2601.13281v1#bib.bib8 "Generalized autoregressive score models with applications")].
The relevant score equations for the new parameterization from ([4](https://arxiv.org/html/2601.13281v1#S2.E4 "In 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) in the copula setting are given by the following proposition, the proof of which can be found in the appendix.

###### Proposition 1 (score equations for spectral dynamics).

Let c​(𝐮t;𝛉c,t)=c​(𝐮t;𝐑t,ν,𝛄)c\left(\bm{u}\_{t};\bm{\theta}\_{c,t}\right)=c\left(\bm{u}\_{t};\bm{R}\_{t},\nu,\bm{\gamma}\right) be the skewed tt copula density from ([1](https://arxiv.org/html/2601.13281v1#S2.E1 "In 2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) and ([2](https://arxiv.org/html/2601.13281v1#S2.E2 "In 2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")), let fi,t=log⁡λi,tf\_{i,t}=\log\lambda\_{i,t}, λi,t=Λi,i,t\lambda\_{i,t}=\Lambda\_{i,i,t} and α~t=αt​ν+𝐲⋆t​𝐑t−1⊤​𝐲⋆t\tilde{\alpha}\_{t}=\alpha\_{t}\sqrt{\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t}} with αt=𝛄⊤​𝐑t−1​𝛄\alpha\_{t}=\sqrt{\bm{\gamma}^{\top}\bm{R}\_{t}^{-1}\bm{\gamma}}.
Then, using ∇t=(∇1,t,…,∇d,t)⊤=∂log⁡c​(𝐮t;𝛉c,t)/∂𝐟t\bm{\nabla}\_{t}=(\nabla\_{1,t},\ldots,\nabla\_{d,t})^{\top}=\partial\log c\left(\bm{u}\_{t};\bm{\theta}\_{c,t}\right)/\partial\bm{f}\_{t}, we have that the unit-scaled score dynamics are given by Eq. ([5](https://arxiv.org/html/2601.13281v1#S2.E5 "In 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")), with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∇i,t\displaystyle\nabla\_{i,t} | =∂log⁡c​(𝒖t;𝑹t,ν,𝜸)∂fi,t=−12​∂log⁡|𝑹t|∂fi,t−12​𝒚⋆t​∂𝑹t−1∂fi,t⊤​(ν~t​𝒚⋆t−2​𝜸)\displaystyle=\frac{\partial\log c(\bm{u}\_{t};\bm{R}\_{t},\nu,\bm{\gamma})}{\partial f\_{i,t}}=-\tfrac{1}{2}\ \frac{\partial\log|\bm{R}\_{t}|}{\partial f\_{i,t}}-\tfrac{1}{2}\ \bm{y^{\star}}\_{t}{}^{\top}\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}\left(\tilde{\nu}\_{t}\ \bm{y^{\star}}\_{t}-2\bm{\gamma}\right) |  | (6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​α~t⋅k(ν+d)/2′​(α~t)×(𝜸⊤​(∂𝑹t−1/∂fi,t)​𝜸𝜸⊤​𝑹t−1​𝜸+𝒚⋆t(∂𝑹t−1/∂fi,t)⊤𝒚⋆tν+𝒚⋆t​𝑹t−1⊤​𝒚⋆t),\displaystyle\qquad\qquad+\tfrac{1}{2}\,\tilde{\alpha}\_{t}\cdot k^{\prime}\_{(\nu+d)/2}\left(\tilde{\alpha}\_{t}\right)\times\Bigg(\frac{\bm{\gamma}^{\top}\left(\partial\bm{R}\_{t}^{-1}/\partial f\_{i,t}\right)\bm{\gamma}}{\bm{\gamma}^{\top}\bm{R}\_{t}^{-1}\bm{\gamma}}+\frac{\bm{y^{\star}}\_{t}{}^{\top}\left(\partial\bm{R}\_{t}^{-1}/\partial f\_{i,t}\right)\bm{y^{\star}}\_{t}}{\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t}}\Bigg), |  |

where ν~t=(d+ν)/(ν+𝐲⋆t​𝐑t−1⊤​𝐲⋆t)\tilde{\nu}\_{t}=(d+\nu)/(\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t}), and

|  |  |  |
| --- | --- | --- |
|  | 𝑹t=diag(𝚺t)−1/2𝑾𝚲t𝑾⊤diag(𝚺t)−1/2,𝚺t=𝑾𝚲t𝑾⊤,\displaystyle\bm{R}\_{t}=\operatorname{diag}(\bm{\Sigma}\_{t})^{-1/2}\ \bm{W}\bm{\Lambda}\_{t}\bm{W}^{\top}\ \operatorname{diag}(\bm{\Sigma}\_{t})^{-1/2},\qquad\bm{\Sigma}\_{t}=\bm{W}\bm{\Lambda}\_{t}\bm{W}^{\top},\qquad |  |
|  |  |  |
| --- | --- | --- |
|  | ∂log⁡|𝑹t|∂fi,t=1−λi,t​∑j=1dwj,i2Σj,j,t,𝚺˙i,t=12​λi,t​diag⁡(w1,i2Σ1,1,t,…,wd,i2Σd,d,t),\displaystyle\frac{\partial\log|\bm{R}\_{t}|}{\partial f\_{i,t}}=1-\lambda\_{i,t}\sum\_{j=1}^{d}\frac{w^{2}\_{j,i}}{\Sigma\_{j,j,t}},\qquad\dot{\bm{\Sigma}}\_{i,t}=\tfrac{1}{2}\lambda\_{i,t}\operatorname{diag}\left(\frac{w\_{1,i}^{2}}{\Sigma\_{1,1,t}},\ldots,\frac{w\_{d,i}^{2}}{\Sigma\_{d,d,t}}\right), |  |
|  |  |  |
| --- | --- | --- |
|  | ∂𝑹t−1∂fi,t=−diag(𝚺t)1/2𝒘i​𝒘i⊤λi,tdiag(𝚺t)1/2+𝚺˙i,t𝑹t−1+𝑹t−1𝚺˙i,t,\displaystyle\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}=-\operatorname{diag}(\bm{\Sigma}\_{t})^{1/2}\,\frac{\bm{w}\_{i}\bm{w}\_{i}^{\top}}{\lambda\_{i,t}}\,\operatorname{diag}(\bm{\Sigma}\_{t})^{1/2}+\dot{\bm{\Sigma}}\_{i,t}\,\bm{R}\_{t}^{-1}+\bm{R}\_{t}^{-1}\,\dot{\bm{\Sigma}}\_{i,t}, |  |

and kν′​(x)=∂log⁡(xν⋅Kν​(x))/∂xk\_{\nu}^{\prime}(x)=\partial\log\left(x^{\nu}\cdot K\_{\nu}(x)\right)/\partial x for given ν>0\nu>0 and x∈ℝ+x\in\mathbb{R}^{+}, where 𝐰i\bm{w}\_{i} denotes the iith column of 𝐖\bm{W} and wj,iw\_{j,i} its (j,i)(j,i)th element, and Σj,j,t\Sigma\_{j,j,t} denotes the (j,j)(j,j)th element of 𝚺t\bm{\Sigma}\_{t}.

The eigenvalue dynamics in Proposition [1](https://arxiv.org/html/2601.13281v1#Thmtheorem1 "Proposition 1 (score equations for spectral dynamics). ‣ 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") are substantially different from the Gaussian and Student’s tt based eigenvalue dynamics in Hetland et al. [[2023](https://arxiv.org/html/2601.13281v1#bib.bib47 "Dynamic conditional eigenvalue garch")] in at least three respects: the dynamics in Proposition [1](https://arxiv.org/html/2601.13281v1#Thmtheorem1 "Proposition 1 (score equations for spectral dynamics). ‣ 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") relate to (i) a high-dimensional copula setting, (ii) a correlation matrix rather than a covariance matrix parameterization, and (iii) a more general class of distributions.
Still, the dynamics of 𝝀t\bm{\lambda}\_{t} given in Proposition [1](https://arxiv.org/html/2601.13281v1#Thmtheorem1 "Proposition 1 (score equations for spectral dynamics). ‣ 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") have an intuitive form.
To see this, we introduce a scaled and rotated version of 𝒚⋆t\bm{y^{\star}}\_{t}, namely 𝒚~t⋆=𝑾⊤diag(𝚺t)1/2𝒚⋆t\tilde{\bm{y}}^{\star}\_{t}=\bm{W}^{\top}\operatorname{diag}(\bm{\Sigma}\_{t})^{1/2}\bm{y^{\star}}\_{t}.
We also define the corresponding rescaled and rotated version of 𝜸\bm{\gamma}, namely 𝜸~t=𝑾⊤diag(𝚺t)1/2𝜸\tilde{\bm{\gamma}}\_{t}=\bm{W}^{\top}\operatorname{diag}(\bm{\Sigma}\_{t})^{1/2}\bm{\gamma}.
We can now rewrite ([6](https://arxiv.org/html/2601.13281v1#S2.E6 "In Proposition 1 (score equations for spectral dynamics). ‣ 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇i,t=\displaystyle\nabla\_{i,t}= | 12​(ν~t​y~i,t⋆2λi,t−1)−γ~i,t​y~i,t⋆λi,t−12​α~t⋅k(ν+d)/2′​(α~t)⋅(γ~i,t2/λi,t𝜸~t⊤​𝚲t−1​𝜸~t+y~i,t⋆/2λi,tν+𝒚~t⋆​𝚲t−1⊤​𝒚~t⋆)\displaystyle\tfrac{1}{2}\,\left(\tilde{\nu}\_{t}\frac{\tilde{y}^{\star}\_{i,t}{}^{2}}{\lambda\_{i,t}}-1\right)-\frac{\tilde{\gamma}\_{i,t}\tilde{y}^{\star}\_{i,t}}{\lambda\_{i,t}}-\tfrac{1}{2}\,\tilde{\alpha}\_{t}\cdot k^{\prime}\_{(\nu+d)/2}\left(\tilde{\alpha}\_{t}\right)\cdot\left(\frac{\tilde{\gamma}\_{i,t}^{2}/\lambda\_{i,t}}{\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{\gamma}}\_{t}}+\frac{\tilde{y}^{\star}\_{i,t}{}^{2}/\lambda\_{i,t}}{\nu+\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(ν~t​𝒚~t⋆​𝚲t−1⊤​𝒚¯i,t⋆−trace⁡(𝚺˙i,t))+(𝜸~t​𝚲t−1⊤​𝒚¯i,t⋆+𝜸¯i,t⊤​𝚲t−1​𝒚~t⋆)\displaystyle-\,\left(\tilde{\nu}\_{t}\,\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{y}}^{\star}\_{i,t}-\operatorname{trace}(\dot{\bm{\Sigma}}\_{i,t})\right)+\left(\tilde{\bm{\gamma}}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{y}}^{\star}\_{i,t}+\bar{\bm{\gamma}}\_{i,t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +α~t⋅k(ν+d)/2′​(α~t)⋅(𝜸~t⊤​𝚲t−1​𝜸¯i,t𝜸~t⊤​𝚲t−1​𝜸~t+𝒚~t⋆​𝚲t−1⊤​𝒚¯i,t⋆ν+𝒚~t⋆​𝚲t−1⊤​𝒚~t⋆),\displaystyle+\tilde{\alpha}\_{t}\cdot k^{\prime}\_{(\nu+d)/2}\left(\tilde{\alpha}\_{t}\right)\cdot\left(\tfrac{\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{\gamma}}\_{i,t}}{\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{\gamma}}\_{t}}+\tfrac{\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{y}}^{\star}\_{i,t}}{\nu+\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}}\right), |  | (7) |

where 𝒚¯i,t⋆\bar{\bm{y}}^{\star}\_{i,t} and 𝜸¯i,t\bar{\bm{\gamma}}\_{i,t} are similar rescaled and rotated versions of 𝒚⋆t\bm{y^{\star}}\_{t} and 𝜸\bm{\gamma}, respectively, as defined in the proof of ([A](https://arxiv.org/html/2601.13281v1#A1.Ex31 "Proof of Eq. () ‣ Appendix A Proofs ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) in [A](https://arxiv.org/html/2601.13281v1#A1 "Appendix A Proofs ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").

The score in ([A](https://arxiv.org/html/2601.13281v1#A1.Ex31 "Proof of Eq. () ‣ Appendix A Proofs ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) consists of two main parts: terms 1 to 3, and terms 4 to 6.
The first term holds the familiar weighted EGARCH-like volatility dynamics ν~ty~i,t⋆/2λi,t−1\tilde{\nu}\_{t}\/\tilde{y}^{\star}\_{i,t}{}^{2}/\lambda\_{i,t}-1 that is familiar from the literature on score-driven models for a time-varying log-variance [see Creal et al., [2013](https://arxiv.org/html/2601.13281v1#bib.bib8 "Generalized autoregressive score models with applications"), Harvey, [2013](https://arxiv.org/html/2601.13281v1#bib.bib23 "Dynamic models for volatility and heavy tails: with applications to financial and economic time series")].
This is intuitive, as the iith eigenvalue is the variance of the the iith spectral projection y~i,t⋆\tilde{y}^{\star}\_{i,t}.
The weighting factor ν~t\tilde{\nu}\_{t} causes extreme observations to have less impact on the eigenvalue dynamics for finite ν\nu, and it collapses to unity if ν→∞\nu\to\infty.
The second and third term of ([A](https://arxiv.org/html/2601.13281v1#A1.Ex31 "Proof of Eq. () ‣ Appendix A Proofs ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) are due to the skewness of the copula specification.
They vanish if γ~i,t\tilde{\gamma}\_{i,t} equals zero.
If γ~i,t>0\tilde{\gamma}\_{i,t}>0, then a large positive y~i,t⋆\tilde{y}^{\star}\_{i,t} has a smaller impact on the next eigenvalue λi,t+1\lambda\_{i,t+1} than a large negative y~i,t⋆\tilde{y}^{\star}\_{i,t}.
This is because large positive outcomes are more likely under positive skewness and are, therefore, not attributed to volatility increases along the corresponding spectral dimension.
For negative skewness, the opposite holds.

The second main part of the score in ([A](https://arxiv.org/html/2601.13281v1#A1.Ex31 "Proof of Eq. () ‣ Appendix A Proofs ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")), terms 4–6, stem from our parameterization of 𝑹t\bm{R}\_{t} as a correlation matrix.
These three terms mimic the first three terms, but with an opposite sign.
We first see a weighted EGARCH type term (ν~t𝒚~t⋆𝚲−1⊤𝒚¯i,t⋆−trace(𝚺˙i,t)(\tilde{\nu}\_{t}\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}^{-1}\bar{\bm{y}}^{\star}\_{i,t}-\operatorname{trace}(\dot{\bm{\Sigma}}\_{i,t}), followed by a term related to the skewness, and a term related to the combination of skewness and kurtosis.
These additional, more complex terms adjust the dynamics of the eigenvalues to account for the fact that 𝑹t\bm{R}\_{t} has unit diagonal elements by construction.
They therefore involve all the spectral projections in 𝒚~t⋆\tilde{\bm{y}}^{\star}\_{t} simultaneously, combined with a related spectral projection 𝒚¯i,t⋆\bar{\bm{y}}^{\star}\_{i,t} that includes an additional scaling by 𝚺˙i,t\dot{\bm{\Sigma}}\_{i,t}.
Despite its more complex expression, the score is still easy to compute and available in analytical form and decomposable into different terms that are attributable to the features of the skewed tt copula.

Due to the explicit normalization of 𝑹t\bm{R}\_{t} in Eq. ([4](https://arxiv.org/html/2601.13281v1#S2.E4 "In 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) and Proposition [1](https://arxiv.org/html/2601.13281v1#Thmtheorem1 "Proposition 1 (score equations for spectral dynamics). ‣ 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), 𝑹t\bm{R}\_{t} is a proper correlation matrix for any update of 𝒇t\bm{f}\_{t}.
The number of time-varying parameters in 𝑹t\bm{R}\_{t}, however, is considerably less than in a full dynamic hypersphere or log-correlation matrix parameterization as in Creal et al. [[2011](https://arxiv.org/html/2601.13281v1#bib.bib53 "A dynamic multivariate heavy-tailed model for time-varying volatilities and correlations")], Buccheri et al. [[2021](https://arxiv.org/html/2601.13281v1#bib.bib57 "A score-driven conditional correlation model for noisy and asynchronous data: an application to high-frequency covariance dynamics")], Archakov and Hansen [[2021](https://arxiv.org/html/2601.13281v1#bib.bib55 "A new parametrization of correlation matrices")], or Hafner and Wang [[2023](https://arxiv.org/html/2601.13281v1#bib.bib56 "A dynamic conditional score model for the log correlation matrix")].
Also note that not all parameters in the parameterization of 𝑹t\bm{R}\_{t} in ([4](https://arxiv.org/html/2601.13281v1#S2.E4 "In 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) can be identified simultaneously.
For instance, both 𝝀t\bm{\lambda}\_{t} and k⋅𝝀tk\cdot\bm{\lambda}\_{t} for some constant k>0k>0 give the same copula dependence matrix 𝑹t\bm{R}\_{t} in ([4](https://arxiv.org/html/2601.13281v1#S2.E4 "In 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")).
We solve this by restricting the elements of 𝝎\bm{\omega} in the recurrence relation for 𝒇t+1\bm{f}\_{t+1} later on using a targeting approach.

The spectral copula approach of Proposition [1](https://arxiv.org/html/2601.13281v1#Thmtheorem1 "Proposition 1 (score equations for spectral dynamics). ‣ 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") comes with several advantages.
First, the approach is purely data-driven, as opposed to using a pre-defined group classification based on, for instance, industries as in Oh and Patton [[2018](https://arxiv.org/html/2601.13281v1#bib.bib39 "Time-varying systemic risk: evidence from a dynamic copula model of cds spreads")] and Opschoor et al. [[2021](https://arxiv.org/html/2601.13281v1#bib.bib41 "Closed-form multi-factor copula models with observation-driven dynamic factor loadings")].
Second, the spectral decomposition is computationally much less demanding compared to a full clustering-based approach as in, for example, Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")].
Third, the approach imposes no restrictions on the dependence matrix.
Fourth, the spectral approach facilitates an exploratory phase of the modeling process.
For instance, using an initial guess of ν\nu and 𝜸\bm{\gamma} (such as the standard normal 𝜸=𝟎\bm{\gamma}=\bm{0} and ν→∞\nu\to\infty), the inverse cdf transforms 𝒚⋆t\bm{y^{\star}}\_{t} of the PITs 𝒖t\bm{u}\_{t} immediately lead to an initial estimate of 𝑾^\hat{\bm{W}} based on the unconditional correlation matrix of 𝒚⋆t\bm{y^{\star}}\_{t}.
This, in turn, allows us to construct preliminary estimates of the spectral projections of the data in y~i,t⋆\tilde{y}^{\star}\_{i,t}, which one can inspect visually to get an impression of the extent of time-variation in the volatility of y~i,t⋆\tilde{y}^{\star}\_{i,t}, i.e., in λi,t\lambda\_{i,t}.
We can use such information to impose further parsimony on the model, e.g., by restricting some of the spectral dimensions to have constant rather than time-varying volatility.
We come back to this in Section [4.1](https://arxiv.org/html/2601.13281v1#S4.SS1 "4.1 Data ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").

### 2.3 Non-linear shrinkage and model selection

In high-dimensions it becomes challenging to estimate the copula correlation matrix.
It is known that for large dimension dd the sample eigenvalues {𝝀^t}t=1d\{\hat{\bm{\lambda}}\_{t}\}\_{t=1}^{d} become a biased estimator of the true spectrum {𝝀t}t=1d\{\bm{\lambda}\_{t}\}\_{t=1}^{d} when d,T→∞d,T\to\infty and d/Td/T converges to some positive, nonzero constant [Marčenko and Pastur, [1967](https://arxiv.org/html/2601.13281v1#bib.bib49 "Distribution of eigenvalues for some sets of random matrices"), Johnstone, [2001](https://arxiv.org/html/2601.13281v1#bib.bib59 "On the distribution of the largest eigenvalue in principal components analysis"), Ledoit and Wolf, [2012](https://arxiv.org/html/2601.13281v1#bib.bib51 "Nonlinear shrinkage estimation of large-dimensional covariance matrices"), [2022b](https://arxiv.org/html/2601.13281v1#bib.bib30 "The power of (non-) linear shrinking: a review and guide to covariance matrix estimation"), [2022a](https://arxiv.org/html/2601.13281v1#bib.bib31 "Quadratic shrinkage for large covariance matrices")].
Engle et al. [[2019](https://arxiv.org/html/2601.13281v1#bib.bib20 "Large dynamic covariance matrices")] use shrinkage techniques to correct these biases by adjusting the (targeted) high-dimensional intercept in their DCC transition equation.
They show that such a shrinkage procedure for the d×dd\times d volatility intercept provides better results than a targeting procedure without shrinkage.
We follow a similar procedure, using the de-biased spectrum based on the more recent quadratic shrinkage techniques of Ledoit and Wolf [[2022a](https://arxiv.org/html/2601.13281v1#bib.bib31 "Quadratic shrinkage for large covariance matrices")] as our target.
If 𝝀^t\hat{\bm{\lambda}}\_{t} denotes the sample spectrum at time tt, the quadratic shrinkage formula fQSf\_{\rm QS} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | λˇi,t−1\displaystyle\check{\lambda}\_{i,t}^{-1} | =fQS​(𝝀^t−1)=(1−q)2​λ^i,t−1+2​q​(1−q)​λ^i,t−1​1d​∑j=1dλ^j,t−1​λ^j,t−1−λ^i,t−1(λ^j,t−1−λ^i,t−1)2+h2​λ^j,t−2\displaystyle=f\_{\rm QS}(\hat{\bm{\lambda}}\_{t}^{-1})=\left(1-q\right)^{2}\hat{\lambda}\_{i,t}^{-1}+2q\left(1-q\right)\hat{\lambda}\_{i,t}^{-1}\frac{1}{d}\sum\_{j=1}^{d}\hat{\lambda}\_{j,t}^{-1}\frac{\hat{\lambda}\_{j,t}^{-1}-\hat{\lambda}\_{i,t}^{-1}}{(\hat{\lambda}\_{j,t}^{-1}-\hat{\lambda}\_{i,t}^{-1})^{2}+h^{2}\hat{\lambda}\_{j,t}^{-2}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +q2​λ^i,t−1​([1d​∑j=1dλ^j,t−1​λ^j,t−1−λ^i,t−1(λ^j,t−1−λ^i,t−1)2+h2​λ^j,t−2]2+[1d​∑j=1dλj,t−1​h​λ^j,t−1(λ^j,t−1−λ^i,t−1)2+h2​λ^j,t−2]2),\displaystyle\qquad+q^{2}\hat{\lambda}\_{i,t}^{-1}\left(\left[\frac{1}{d}\sum\_{j=1}^{d}\hat{\lambda}\_{j,t}^{-1}\frac{\hat{\lambda}\_{j,t}^{-1}-\hat{\lambda}\_{i,t}^{-1}}{(\hat{\lambda}\_{j,t}^{-1}-\hat{\lambda}\_{i,t}^{-1})^{2}+h^{2}\hat{\lambda}\_{j,t}^{-2}}\right]^{2}+\left[\frac{1}{d}\sum\_{j=1}^{d}\lambda\_{j,t}^{-1}\frac{h\,\hat{\lambda}\_{j,t}^{-1}}{(\hat{\lambda}\_{j,t}^{-1}-\hat{\lambda}\_{i,t}^{-1})^{2}+h^{2}\hat{\lambda}\_{j,t}^{-2}}\right]^{2}\right), |  | (8) |

where 𝝀ˇt=(λˇ1,t,…,λˇd,t)⊤\check{\bm{\lambda}}\_{t}=\big(\check{\lambda}\_{1,t},\ldots,\check{\lambda}\_{d,t}\big)^{\top} denotes the de-biased spectrum, q=d/Tq=d/T, and hh is a smoothness parameter.
Ledoit and Wolf [[2022a](https://arxiv.org/html/2601.13281v1#bib.bib31 "Quadratic shrinkage for large covariance matrices")] show that this type of shrinkage mapping is asymptotically optimal under various loss metrics, such as Frobenius loss.
They advise to take h=min(q2,q−2)0.35⋅d−0.35h=\min(q^{2},q^{-2})^{0.35}\cdot d^{-0.35} and demonstrate that their non-linear shrinkage estimator has excellent in-sample and out-of-sample performance in a wide range of settings.

In combination with the above shrinkage approach to overcome eigenvalue biases in high dimensions, we also impose parsimony on the model by limiting the number of dynamic eigenvalues.
We do so using standard model-selection criteria.
In applications to stock return data as in Section [4](https://arxiv.org/html/2601.13281v1#S4 "4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), one typically finds that the first few eigenvalues are much larger than the remaining ones.
The notion of a few dominant eigenvalues that drive the dependence structure is conceptually in line with the perspective of a ‘spiked’ eigenvalue dependence model [see, e.g., Johnstone, [2001](https://arxiv.org/html/2601.13281v1#bib.bib59 "On the distribution of the largest eigenvalue in principal components analysis"), Fan et al., [2013](https://arxiv.org/html/2601.13281v1#bib.bib60 "Large covariance estimation by thresholding principal orthogonal complements"), Donoho et al., [2018](https://arxiv.org/html/2601.13281v1#bib.bib58 "Optimal shrinkage of eigenvalues in the spiked covariance model")] and corresponds closely to the typical covariance structure present in financial markets [see, for instance, Fama and French, [1993](https://arxiv.org/html/2601.13281v1#bib.bib61 "Common risk factors in the returns on stocks and bonds"), [1998](https://arxiv.org/html/2601.13281v1#bib.bib62 "Value versus growth: the international evidence"), and many more].
Capturing the dynamics of the largest eigenvalues is therefore most important and contributes most to the model’s fit.
For the lowest eigenvalues, it is more important to prevent them from becoming too close to zero due to the high-dimensional biases, which would result in poor out-of-sample performance.
To select the number of dynamic eigenvalues, we therefore implement the following model selection strategy.
Starting from a model with only static eigenvalues, we increase the number of dynamic eigenvalues one-by-one, starting from the largest eigenvalue.
We then compute the change in BIC relative to the static model by accounting for the change in the in-sample log-likelihood and the change in the number of parameters.
We select the dynamic model with the lowest BIC.
The procedure typically results in a limited number of dynamic eigenvalues and a large number of static ones.
Combined with the high-dimensional shrinkage procedure for targeting the intercepts, this results in a considerable reduction of the parameter space.
We show later using simulated and empirical data that this approach efficiently captures the salient features of the data, including their dynamics.

### 2.4 Parameter estimation

We split the estimation procedure in two standard steps.
We first estimate the marginal behavior of each original univariate series ri,tr\_{i,t} by an AR(1)-GARCH(1,1) model using standard quasi maximum likelihood (QMLE).
From the devolatilized residuals yi,t=ϵi,t/σi,ty\_{i,t}=\epsilon\_{i,t}/\sigma\_{i,t}, we use the non-parametric rank transformation ui,t=rank​(yi,t)/(T+1/2)u\_{i,t}=\text{rank}(y\_{i,t})/(T+1/2) to obtain the PITs.
This makes the construction of the PITs more robust to any potential mis-specification of the marginal distributions, in line with the use of QMLE to estimate the AR(1)-GARCH(1,1) marginal models.

Next, we estimate the dynamic dependence structure by maximizing the copula density ([1](https://arxiv.org/html/2601.13281v1#S2.E1 "In 2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")).
For a given tail shape parameter ν\nu and skewness parameter 𝜸\bm{\gamma}, we can compute the inverse marginal cdf projections 𝒚⋆t=𝒚⋆t​(ν,𝜸)=G−1​(ui,t;𝜸,ν)\bm{y^{\star}}\_{t}=\bm{y^{\star}}\_{t}(\nu,\bm{\gamma})=G^{-1}(u\_{i,t};\bm{\gamma},\nu).
Let 𝑺⋆=𝔼[𝒚⋆t𝒚⋆t]⊤\bm{S}^{\star}=\mathbb{E}[\bm{y^{\star}}\_{t}\bm{y^{\star}}\_{t}{}^{\top}] and 𝑹=𝔼​[𝑹t]\bm{R}=\mathbb{E}[\bm{R}\_{t}], then for the skewed tt distribution we have that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑺⋆\displaystyle\bm{S}^{\star} | =νν−2​𝑹+2​ν2(ν−2)2​(ν−4)​𝜸​𝜸⊤⇔𝑹=ν−2ν​𝑺⋆−2​ν(ν−2)​(ν−4)​𝜸​𝜸⊤.\displaystyle=\frac{\nu}{\nu-2}\bm{R}+\frac{2\nu^{2}}{(\nu-2)^{2}(\nu-4)}\bm{\gamma}\bm{\gamma}^{\top}\quad\Leftrightarrow\quad\bm{R}=\frac{\nu-2}{\nu}\bm{S}^{\star}-\frac{2\nu}{(\nu-2)(\nu-4)}\bm{\gamma}\bm{\gamma}^{\top}. |  | (9) |

Replacing 𝑺⋆\bm{S}^{\star} in ([9](https://arxiv.org/html/2601.13281v1#S2.E9 "In 2.4 Parameter estimation ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) by the sample estimator 𝑺^⋆=T−1∑t=1T𝒚⋆t𝒚⋆t⊤\hat{\bm{S}}^{\star}=T^{-1}\sum\_{t=1}^{T}\bm{y^{\star}}\_{t}\bm{y^{\star}}\_{t}{}^{\top}, we then define the estimators

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺^=𝚺^​(𝜸,ν)=𝑾^​(𝜸,ν)​𝚲^​(𝜸,ν)​𝑾^​(𝜸,ν)⊤=ν−2ν​𝑺^⋆−2​ν(ν−2)​(ν−4)​𝜸​𝜸⊤,𝑹^=diag(𝚺^)−1/2𝚺^diag(𝚺^)−1/2.\begin{split}\hat{\bm{\Sigma}}&=\hat{\bm{\Sigma}}(\bm{\gamma},\nu)=\hat{\bm{W}}(\bm{\gamma},\nu)\ \hat{\bm{\Lambda}}(\bm{\gamma},\nu)\ \hat{\bm{W}}(\bm{\gamma},\nu)^{\top}=\frac{\nu-2}{\nu}\hat{\bm{S}}^{\star}-\frac{2\nu}{(\nu-2)(\nu-4)}\bm{\gamma}\bm{\gamma}^{\top},\\ \hat{\bm{R}}&=\operatorname{diag}(\hat{\bm{\Sigma}})^{-1/2}\ \hat{\bm{\Sigma}}\ \operatorname{diag}(\hat{\bm{\Sigma}})^{-1/2}.\end{split} |  | (10) |

The intercepts of the score-driven transition Eq. ([5](https://arxiv.org/html/2601.13281v1#S2.E5 "In 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) are targeted as explained in Section [2.3](https://arxiv.org/html/2601.13281v1#S2.SS3 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") using the quadratic shrinkage procedure of Ledoit and Wolf [[2022a](https://arxiv.org/html/2601.13281v1#bib.bib31 "Quadratic shrinkage for large covariance matrices")] from Eq. ([8](https://arxiv.org/html/2601.13281v1#S2.E8 "In 2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")), yielding the final (shrunken) estimators

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | 𝚺ˇ\displaystyle\check{\bm{\Sigma}} | =𝚺ˇ​(𝜸,ν)=𝑾^​(𝜸,ν)​𝚲ˇ​(𝜸,ν)​𝑾^​(𝜸,ν)⊤,\displaystyle=\check{\bm{\Sigma}}(\bm{\gamma},\nu)=\hat{\bm{W}}(\bm{\gamma},\nu)\ \check{\bm{\Lambda}}(\bm{\gamma},\nu)\ \hat{\bm{W}}(\bm{\gamma},\nu)^{\top}, | 𝑹ˇ\displaystyle\check{\bm{R}} | =diag(𝚺ˇ)−1/2𝚺ˇdiag(𝚺ˇ)−1/2,\displaystyle=\operatorname{diag}(\check{\bm{\Sigma}})^{-1/2}\ \check{\bm{\Sigma}}\ \operatorname{diag}(\check{\bm{\Sigma}})^{-1/2}, |  | (11) |

where 𝚲ˇ=𝚲ˇ​(𝜸,ν)\check{\bm{\Lambda}}=\check{\bm{\Lambda}}(\bm{\gamma},\nu) holds the quadratically shrunken spectrum from Eq. ([8](https://arxiv.org/html/2601.13281v1#S2.E8 "In 2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")).
Note that all these quantities are still functions of 𝜸\bm{\gamma} and ν\nu.
Finally, we compute the copula log-likelihood function as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒ​(𝝍)\displaystyle\mathcal{L}(\bm{\psi}) | =∑t=1T(log⁡g​(𝒚⋆t;𝑹ˇt,𝜸,ν)−∑i=1dlog⁡gi​(yi,t⋆;γi,ν)),\displaystyle=\sum\_{t=1}^{T}\left(\log g\left(\bm{y^{\star}}\_{t};\check{\bm{R}}\_{t},\bm{\gamma},\nu\right)-\sum\_{i=1}^{d}\log g\_{i}\left(y^{\star}\_{i,t};\gamma\_{i},\nu\right)\right), |  | (12) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑹ˇt\displaystyle\check{\bm{R}}\_{t} | =diag(𝚺ˇt)−1/2𝚺ˇtdiag(𝚺ˇt)−1/2,𝚺ˇt=𝑾^𝚲ˇt𝑾^⊤,\displaystyle=\operatorname{diag}(\check{\bm{\Sigma}}\_{t})^{-1/2}\,\check{\bm{\Sigma}}\_{t}\,\operatorname{diag}(\check{\bm{\Sigma}}\_{t})^{-1/2},\qquad\check{\bm{\Sigma}}\_{t}=\hat{\bm{W}}\,\check{\bm{\Lambda}}\_{t}\,\hat{\bm{W}}^{\top}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | log⁡λˇi,t+1\displaystyle\log\check{\lambda}\_{i,t+1} | ={(1−bi)​log⁡λˇi+bi​log⁡λˇi,t+ai​∇i,t,for ​i=1,…,d0,log⁡λˇi,for ​i=d0+1,…,d,\displaystyle=\left\{\begin{array}[]{ll}(1-b\_{i})\log\check{\lambda}\_{i}+b\_{i}\,\log\check{\lambda}\_{i,t}+a\_{i}\nabla\_{i,t},&\text{for }i=1,\ldots,d\_{0},\\ \log\check{\lambda}\_{i},&\text{for }i=d\_{0}+1,\ldots,d,\end{array}\right. |  | (15) |

where 𝝍\bm{\psi} gathers all the static parameters 𝑨\bm{A}, 𝑩\bm{B}, 𝜸\bm{\gamma}, and ν\nu of the model, and where we use the BIC to select the number of time-varying eigenvalues d0d\_{0}, as explained in Section [2.3](https://arxiv.org/html/2601.13281v1#S2.SS3 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
The static parameter vector 𝝍\bm{\psi} is then estimated using Maximum Likelihood.

## 3 Simulation study

To assess the performance of the high-dimensional dynamic copula model with spectral regularization in a controlled environment, we perform two simulation experiments.
In the first experiment, we focus on the performance of the spectral copula structure vis-à-vis a grouped factor copula structure [as used in, e.g., Oh and Patton, [2017](https://arxiv.org/html/2601.13281v1#bib.bib38 "Modeling dependence in high dimensions with factor copulas"), [2018](https://arxiv.org/html/2601.13281v1#bib.bib39 "Time-varying systemic risk: evidence from a dynamic copula model of cds spreads"), [2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments"), Opschoor et al., [2021](https://arxiv.org/html/2601.13281v1#bib.bib41 "Closed-form multi-factor copula models with observation-driven dynamic factor loadings")]. We investigate how the different copula structures and the shrinkage method behave under controlled deviations from a grouped factor structure.
In our second experiment, we focus on the parameter estimation performance of our new model.

### 3.1 Experiment 1: spectral versus grouped copula structures

In both experiments, we specify the unconditional correlation matrix structure 𝑹\bm{R} in our data generating process (dgp) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ri,j=βM2+βGi2​δGi,Gj+βI2​δi,j+βC2​e−|Ci−Cj|/2βM2+βGi2+βC2+βI2βM2+βGj2+βC2+βI2.R\_{i,j}=\frac{\beta\_{M}^{2}+\beta\_{G\_{i}}^{2}\delta\_{G\_{i},G\_{j}}+\beta\_{I}^{2}\delta\_{i,j}+\beta\_{C}^{2}e^{-|C\_{i}-C\_{j}|/2}}{\sqrt{\beta\_{M}^{2}+\beta\_{G\_{i}}^{2}+\beta\_{C}^{2}+\beta\_{I}^{2}}\ \ \sqrt{\beta\_{M}^{2}+\beta\_{G\_{j}}^{2}+\beta\_{C}^{2}+\beta\_{I}^{2}}\ }. |  | (16) |

Here, δi,j\delta\_{i,j} is the Kronecker delta with δi,j=1\delta\_{i,j}=1 if i=ji=j, and zero else.
We can interpret this correlation structure as corresponding to a factor model of the form:
βM​FtM+βGi​FtGi+βCi​FtCi+βI​ηi,t\beta\_{M}\,F^{M}\_{t}+\beta\_{G\_{i}}\,F^{G\_{i}}\_{t}+\beta\_{C\_{i}}\,F^{C\_{i}}\_{t}+\beta\_{I}\,\eta\_{i,t},
where βM\beta\_{M} is the loading coefficient of a common market factor FtMF^{M}\_{t} to which all assets are exposed;
βGi\beta\_{G\_{i}} is the factor loading for a group factor FtGiF^{G\_{i}}\_{t} corresponding to group GiG\_{i} of asset ii, e.g., an industry factor;
βC\beta\_{C} is the factor loading for the factor FtCiF^{C\_{i}}\_{t}, which defines, for instance, a country factor, i.e., a second grouping structure over and above the first (industry) grouping effect;
and finally βI\beta\_{I} represents the size of the idiosyncratic noise component.
Higher values of βI\beta\_{I} decrease the signal-to-noise ratio.
In our example, the (industry) indicators GiG\_{i} and (country) indicators CiC\_{i} both range from 1 to 10, and the factors have zero means and are uncorrelated with each other.
The only exception is the country factor FtCiF^{C\_{i}}\_{t}, which is correlated between countries CiC\_{i} with a correlation that varies with the distance |Ci−Cj||C\_{i}-C\_{j}|.

If βC=0\beta\_{C}=0, the dgp collapses to a pure group structure as in Oh and Patton [[2017](https://arxiv.org/html/2601.13281v1#bib.bib38 "Modeling dependence in high dimensions with factor copulas"), [2018](https://arxiv.org/html/2601.13281v1#bib.bib39 "Time-varying systemic risk: evidence from a dynamic copula model of cds spreads"), [2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")] and Opschoor et al. [[2021](https://arxiv.org/html/2601.13281v1#bib.bib41 "Closed-form multi-factor copula models with observation-driven dynamic factor loadings")].
For βC>0\beta\_{C}>0, however, the group structure is only approximate, which allows us to study the effect of such deviations on both our new copula structure as well as alternatives from the literature.
We consider d=100d=100 assets, where each asset corresponds to a unique pair (Gi,Ci)(G\_{i},C\_{i}).
If βC>0\beta\_{C}>0, the correlation structure can no longer be easily restored by a simple extension of the number of factors, while retaining the block-diagonality of the factor loading matrix and the orthogonality of the group factors; see Supplementary [B.1](https://arxiv.org/html/2601.13281v1#A2.SS1 "B.1 Reference model ‣ Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").

Table 1:  Correlation properties of the empirical data set and the stylized dependence model. We show the properties of Gaussian rank correlations, such as the cross-sectional mean, standard deviation and the range over all correlations. We show also the mean, standard deviation and the range over two specific sectors, namely the industry sector with highest average correlation and lowest average correlation.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Empirical | | |  | Simulation | | |
|  | mean | std. dev. | range |  | mean | std. dev. | range |
| All correlations | 0.29 | 0.12 | [0.00−0.78][0.00-0.78] |  | 0.29 | 0.15 | [0.05−0.73][0.05-0.73] |
| Lowest correlated sector | 0.30 | 0.12 | [0.11−0.56][0.11-0.56] |  | 0.31 | 0.13 | [0.14−0.58][0.14-0.58] |
| Highest correlated sector | 0.54 | 0.08 | [0.41−0.71][0.41-0.71] |  | 0.59 | 0.07 | [0.49−0.73][0.49-0.73] |

We select the values of the parameters in the dgp to resemble the empirical complexity of the international stock market data as used in Section [4](https://arxiv.org/html/2601.13281v1#S4 "4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
We set βI=1\beta\_{I}=1, βM=0.75\beta\_{M}=0.75 and let βGi=1.75−0.15​i\beta\_{G\_{i}}=1.75-0.15i to have groups with different intragroup (industry) copula correlations.
For βC\beta\_{C}, we consider a parameter range βC∈{0,0.75,1.5}\beta\_{C}\in\{0,0.75,1.5\}.
This means that country-effects are either fully absent, or are smaller than industry-effects, or have a comparable size.
For βC=0\beta\_{C}=0, the grouped factor structure defined by the groups GiG\_{i} is exact and all within-group correlations have the same value.
For βC>0\beta\_{C}>0, the within-group correlations start to differ and the group structure based only on GiG\_{i} no longer captures the full heterogeneity in the dependence structure.
Having considerable heterogeneity is in line with our empirical data study in Section [4](https://arxiv.org/html/2601.13281v1#S4 "4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").

Table [1](https://arxiv.org/html/2601.13281v1#S3.T1 "Table 1 ‣ 3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") shows various properties of unconditional Gaussian rank correlations for the empirical data from Section [4](https://arxiv.org/html/2601.13281v1#S4 "4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), and for simulated Gaussian copula data based on the stylized correlation matrix with βC=1.5\beta\_{C}=1.5.
The two sets of correlations and their heterogeneity show similar properties between the simulated dgp and the empirical data.
The stylized parameters result in a cross-sectional average correlation of 0.29, which includes both intrasector correlations and cross-sector correlations.
The correlations averaged over each sector in the simulation vary from 0.31 to 0.59.
The intrasector correlations themselves vary from 0.14 to 0.58 within the lowest correlated sector and from 0.49 to 0.73 within the highest correlated sector.
Similar values and ranges are found for the data set used in Section [4](https://arxiv.org/html/2601.13281v1#S4 "4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
The simulation setting thus mirrors the stylized facts in the empirical data quite well.

As our benchmark model in the simulations and in the empirical application later on, we use the dynamic factor copula approach of Opschoor et al. [[2021](https://arxiv.org/html/2601.13281v1#bib.bib41 "Closed-form multi-factor copula models with observation-driven dynamic factor loadings")] and Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")].
We select the optimal number of clusters endogenously using the clustering methodology of Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")] based on their computer code.
See Supplementary [B](https://arxiv.org/html/2601.13281v1#A2 "Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") for more details on the dependence structure imposed by their methodology.
We consider a d=100d=100 dimensional time series and set the number of simulated observations to T∈{250,1000}T\in\{250,1000\}.
We compute the models’ performance metrics both in-sample and out-of-sample to illustrate the effect of over-fitting and of shrinkage.
On top of the TT in-sample observations, we therefore generate an additional 1000 observations from the same dgp and re-calculate the log-likelihood without re-estimating the model’s parameters to obtain the out-of-sample log-likelihood.
To simulate the data, we use a skewed tt with ν=25\nu=25 and 𝜸=γ​𝜾\bm{\gamma}=\gamma\,\bm{\iota}, where γ=−0.25\gamma=-0.25 and 𝜾\bm{\iota} is a vector of ones, as in Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")].
These parameter values are similar to those obtained from empirical data.

Table 2: 
Comparison of in-sample and out-of-sample log-likelihoods (ℓi​n\ell\_{in} and ℓo​u​t\ell\_{out}) for different correlation structures, estimation methods and sample sizes TT in d=100d=100 dimensions.
The true copula dependence structure 𝑹\bm{R} is given in ([16](https://arxiv.org/html/2601.13281v1#S3.E16 "In 3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) and either has a single clear grouped correlation structure (such as industry-only, βC=0\beta\_{C}=0), or a stylized, but realistic additional intra and inter-group correlation structure (e.g. country, βC=0.75\beta\_{C}=0.75 or 1.5).
The TT in-sample observations are used to estimate the models.
An additional TT simulated out-of-sample observations are used to compute ℓo​u​t\ell\_{out}.
In the dgp, data are generated using the skew tt copula with ν=25\nu=25 and 𝜸=−0.25​𝜾\bm{\gamma}=-0.25\,\bm{\iota}.
Best performing models per combination of dependence structure and sample size (row-wise) are bolded.

| βC\beta\_{C} | TT | True | |  | Regularized | |  | Sample | |  | Factor | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | ℓi​n\ell\_{in} | ℓo​u​t\ell\_{out} |  | ℓi​n\ell\_{in} | ℓo​u​t\ell\_{out} |  | ℓi​n\ell\_{in} | ℓo​u​t\ell\_{out} |  | ℓi​n\ell\_{in} | ℓo​u​t\ell\_{out} |
| 0 | 10001000 | 35,168 | 36,206 |  | 36,899 | 34,798 |  | 37,563 | 33,366 |  | 34,811 | 𝟑𝟓,𝟕𝟗𝟏\bm{35,791} |
| 0 | 250250 | 8,562 | 8,577 |  | 9,925 | 7,694 |  | 11,496 | 4,380 |  | 8,555 | 𝟖,𝟓𝟎𝟕\bm{8,507} |
| 0.75 | 10001000 | 39,392 | 39,665 |  | 41,062 | 𝟑𝟖,𝟏𝟑𝟓\bm{38,135} |  | 41,800 | 36,805 |  | 30,922 | 31,304 |
| 0.75 | 250 | 9,422 | 9,414 |  | 10,903 | 𝟖,𝟐𝟖𝟑\bm{8,283} |  | 12,399 | 5,168 |  | 7,402 | 7,313 |
| 1.5 | 10001000 | 55,693 | 55,748 |  | 57,185 | 𝟓𝟒,𝟒𝟓𝟗\bm{54,459} |  | 58,132 | 52,906 |  | 33,943 | 33,439 |
| 1.5 | 250 | 13,611 | 13,529 |  | 15,051 | 𝟏𝟐,𝟒𝟔𝟒\bm{12,464} |  | 16,601 | 9,295 |  | 8,343 | 8,120 |

Table [2](https://arxiv.org/html/2601.13281v1#S3.T2 "Table 2 ‣ 3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") presents the results.
There are three main takeaways.
First, if there is a true factor structure (βC=0\beta\_{C}=0), then the factor cluster copula model of Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")], labeled Factor, performs best based on the out-of-sample log-likelihood ℓo​u​t\ell\_{out}, with the regularized spectral model in second place.
This is encouraging, as the out-of-sample performance loss for the spectral method vis-à-vis a correctly specified more parsimonious model is limited.
To appreciate this, we note that the spectral dynamic copula model is agnostic about the true model structure and therefore still requires the estimation of 4950 different correlation parameters.

Second, we see that MLE combined with the sample correlation matrix (in the column Sample) suffers from the curse of dimensionality for large correlation matrices, as expected [Ledoit and Wolf, [2022b](https://arxiv.org/html/2601.13281v1#bib.bib30 "The power of (non-) linear shrinking: a review and guide to covariance matrix estimation")].
The out-of-sample performance of the MLE is significantly worse than its in-sample performance.
The biases in the spectrum become more pronounced if the number of in-sample data points decreases to, e.g., T=250T=250.
The problem of overfitting is resolved either when a parsimonious model structure is imposed through a cluster factor structure (in the column Factor) or when we use the quadratic shrinkage approach of Ledoit and Wolf [[2022a](https://arxiv.org/html/2601.13281v1#bib.bib31 "Quadratic shrinkage for large covariance matrices")] (in the column Regularized).

Third, when we depart from the true group structure, the results for βC=0.75\beta\_{C}=0.75 and 1.5 show that the spectral copula approach with regularization performs best by a wide margin.
Again, when shrinkage is not applied, we see similar biases as before.
Also, the effect of shrinkage becomes larger as the ratio d/Td/T increases.
We also see that the differences in out-of-sample log-likelihood performance between the clustering and the regularized approach is large for βC=0.75\beta\_{C}=0.75 and 1.5.
This holds even if one allows for an endogenous choice of the number of groups and asset group assignments as in Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")].
In the stylized correlation matrix from Eq. ([4](https://arxiv.org/html/2601.13281v1#S2.E4 "In 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")), there are variations in correlations both within groups and across groups, while the cluster factor approach imposes that all correlations for stocks belonging to a group are the same.
Moreover, the cluster factor structure does not span the full space of correlation matrices (see Supplementary [B](https://arxiv.org/html/2601.13281v1#A2 "Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")).
As a result, the cluster factor structure can miss out on important forms of heterogeneity in the data, both in the simulation and the empirical study.

### 3.2 Experiment 2: quality of point and path estimates

Table 3:  Simulation results for the copula parameter estimates based on the dynamic skew tt copula as dgp with the dependence structure from ([16](https://arxiv.org/html/2601.13281v1#S3.E16 "In 3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")). The sample size is T=1000T=1000 in d=100d=100 dimensions.
Sample ML uses the sample spectrum of 𝑹^\hat{\bm{R}} in Eq. ([10](https://arxiv.org/html/2601.13281v1#S2.E10 "In 2.4 Parameter estimation ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")), while Regularized ML uses the quadratic shrinkage formula of Ledoit and Wolf [[2022a](https://arxiv.org/html/2601.13281v1#bib.bib31 "Quadratic shrinkage for large covariance matrices")]. The simulations are repeated 100 times. The mean and the standard deviation of the estimates are reported.

|  |  |  | Regularized ML | |  | Sample ML | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Parameter | True |  | Mean | Std. dev. |  | Mean | Std. dev. |
| λ1\lambda\_{1} | 29.8 |  | 29.4 | (1.8) |  | 29.7 | (1.7) |
| λ2\lambda\_{2} | 10.7 |  | 10.7 | (0.8) |  | 10.8 | (0.7) |
| λ99\lambda\_{99} | 0.160 |  | 0.171 | (0.008) |  | 0.101 | (0.003) |
| λ100\lambda\_{100} | 0.160 |  | 0.164 | (0.009) |  | 0.097 | (0.003) |
| a1a\_{1} | 0.10 |  | 0.09 | (0.01) |  | 0.09 | (0.01) |
| b1b\_{1} | 0.90 |  | 0.89 | (0.03) |  | 0.89 | (0.03) |
| a2a\_{2} | 0.10 |  | 0.09 | (0.02) |  | 0.08 | (0.02) |
| b2b\_{2} | 0.90 |  | 0.88 | (0.06) |  | 0.88 | (0.07) |
| ν\nu | 25.0 |  | 24.6 | (1.8) |  | 29.2 | (2.2) |
| γ\gamma | -0.25 |  | -0.28 | (0.07) |  | -0.31 | (0.08) |

So far, the simulation study concentrated on the unconditional dependence structure of the copula and the performance of the shrinkage procedure.
Next, we consider the quality of the point estimates of the copula parameters, the selection of the number of dynamic components, and the path estimates of the dynamic eigenvalues.
We take the score-driven dynamic spectral copula model from Section [2](https://arxiv.org/html/2601.13281v1#S2 "2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") as our dgp.
The stylized correlation matrix from ([16](https://arxiv.org/html/2601.13281v1#S3.E16 "In 3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) is again used with βC=1.5\beta\_{C}=1.5.
The other parameter values (see Table [1](https://arxiv.org/html/2601.13281v1#S3.T1 "Table 1 ‣ 3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) are chosen to be similar to the empirical results from Section [4](https://arxiv.org/html/2601.13281v1#S4 "4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
The first 2 eigenvalues in the dgp are dynamic, while the remaining 98 eigenvalues in the dgp are static, also in line with the empirical results.
We estimate the static parameters using the Sample ML as well as the Regularized ML procedure as described in Section [2.3](https://arxiv.org/html/2601.13281v1#S2.SS3 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
The estimation results can be found in Table [3](https://arxiv.org/html/2601.13281v1#S3.T3 "Table 3 ‣ 3.2 Experiment 2: quality of point and path estimates ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").

The results in Table [3](https://arxiv.org/html/2601.13281v1#S3.T3 "Table 3 ‣ 3.2 Experiment 2: quality of point and path estimates ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") confirm that the Sample ML approach suffers from biases in the estimation of the eigenvalues at the lower end of the spectrum, i.e., for small eigenvalues.
At the upper end of the spectrum, i.e., for the large eigenvalues, the effect of shrinkage is less pronounced.
This means that the Regularized ML estimator successfully removes the biases at the low end of the spectrum, while leaving ‘spiked’ eigenvalues intact.
We note that also all other parameters, such as aia\_{i}, bib\_{i}, ν\nu, and 𝜸=γ​𝜾\bm{\gamma}=\gamma\,\bm{\iota}, are estimated accurately.

![Refer to caption](x1.png)


Figure 1: Performance of the skewed tt copula with regularized spectral dynamics. The left plot shows changes in the (in-sample) BIC of a model with static eigenvalues versus a model with eigenvalues 1,…,i1,\ldots,i being dynamic, as a function of the spectral index ii.
The BIC is minimal for i=2i=2, which is also the true number of dynamic eigenvalues in the dgp. The average result of 10 Monte Carlo simulations is shown. The right-hand plot shows the dynamics of the first eigenvalue for a single MC simulation, where the true dynamics of the dgp is compared with the predicted dynamics from the estimated model. The period after 4 years is an out-of-sample forecast.

Figure [1](https://arxiv.org/html/2601.13281v1#S3.F1 "Figure 1 ‣ 3.2 Experiment 2: quality of point and path estimates ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") presents the results for the model selection procedure to determine the number of dynamic eigenvalues.
In each Monte Carlo simulation and for i=1,…,7i=1,\ldots,7, we successively estimate models with eigenvalues 1,…,i1,\ldots,i as dynamic, and eigenvalues i+1,…,di+1,\ldots,d as static.
We compute the in-sample BIC decrease with respect to a fully static model (i=0i=0), as well as its out-of-sample log-likelihood increase.

The left-hand panel in Figure [1](https://arxiv.org/html/2601.13281v1#S3.F1 "Figure 1 ‣ 3.2 Experiment 2: quality of point and path estimates ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") shows that the average Δ\DeltaBIC curve has its minimum at the correct number of d0=2d\_{0}=2 dynamic components.
This analysis validates our choice to use BIC for selecting the number of dynamic eigenvalues in the empirical study of Section [4](https://arxiv.org/html/2601.13281v1#S4 "4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
From the out-of-sample log-likelihood increases (right-hand axis in Figure [1](https://arxiv.org/html/2601.13281v1#S3.F1 "Figure 1 ‣ 3.2 Experiment 2: quality of point and path estimates ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")), we see that it is particularly important to include the dynamics of the first eigenvalue, since it has the largest impact.
For spectral indices above i=2i=2, there are no further increases in log-likelihood if we make these eigenvalues dynamic, and the BIC grows linearly in the number of parameters.
The stable out-of-sample log-likelihood suggests that the risk in overfitting the number of dynamic components is relatively low, since overstating the number of dynamic eigenvalues does not have a negative effect on the out-of-sample log-likelihood.

The right-hand panel in Figure [1](https://arxiv.org/html/2601.13281v1#S3.F1 "Figure 1 ‣ 3.2 Experiment 2: quality of point and path estimates ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") shows a simulated path of the first dynamic eigenvalue with the dgp and the estimated path from the dynamic copula model.
This shows that the eigenvalue dynamics are captured accurately.
An additional simulation experiment in Supplementary [B.2](https://arxiv.org/html/2601.13281v1#A2.SS2 "B.2 Experiment: mis-specification ‣ Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") confirms that the dynamic score-driven model can still recover the true, unobserved eigenvalue dynamics even if it is mis-specified, in line with theoretical consistency results in Beutner et al. [[2023](https://arxiv.org/html/2601.13281v1#bib.bib63 "Consistency, distributional convergence, and optimality of score-driven filters")].

## 4 Empirical study

### 4.1 Data

In our empirical study, we consider daily log return data for 100 stocks from 10 different industry sectors and 10 different European countries over a period of 10 years.
The data are obtained from LSEG (formerly known as Refinitiv), so that our industry sectors are based on The Refinitiv Business Classification (TRBC), which distinguishes between Financials (FI), Industrials (IN), Technology (TE), Basic Materials (BM), Consumer Cyclicals (CC), Consumer Non-Cyclicals (CN), Utilities (UT), Health Care (HC), Energy (EN) and Real Estate (RE).
We select stocks that are issued and traded in 10 different European countries: Germany (DE), United Kingdom (UK), France (FR), Spain (ES), Italy (IT), Sweden (SE), Norway (NO), The Netherlands (NL), Belgium (BE) and Switzerland (CH). For each sector and country combination, we select stocks with the largest market capitalizations after the end of the observation period, while also requiring that each stock is fully observed over the 10 year period from January 2015 to 31 December 2024.
We have a few (8) missing country-industry combinations that do not satisfy our criteria, e.g., because they are not observed over the full sample period.
In such cases, we take the stock from another country in that same industry (with second highest market capitalization).
We are able to do so in such a way that we end up with each of the 10 countries and the 10 sectors occurring precisely 10 times, where some country-sector combinations will be missing, while other combinations occur twice.
Table [C.1](https://arxiv.org/html/2601.13281v1#A3.T1 "Table C.1 ‣ Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") of Supplementary [C](https://arxiv.org/html/2601.13281v1#A3 "Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") lists the full set of all 100 stocks across countries and sectors.

Thus far, high-dimensional copula studies have mainly focused on stocks from a single country, such as the US [see, e.g., Oh and Patton, [2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")].
The large number of possible country and sector combinations increases the complexity of the dependence structure in the current data set and poses challenges to standard factor clustering algorithms.
As a result, copulas that do not impose strong restrictions on the correlation structure can achieve substantial performance gains.

Table 4:  Summary statistics of univariate times series. Panel A presents the unconditional mean, standard deviation, skewness and kurtosis of the daily log-returns. Panel B shows the estimated parameters of the marginal AR(1)-GARCH(1,1) models for the univariate time series,
ri,t=δi+ϕi​ri,t−1+ϵi,tr\_{i,t}=\delta\_{i}+\phi\_{i}r\_{i,t-1}+\epsilon\_{i,t} and σi,t2=ωi+αi​ϵi,t−12+βi​σi,t−12\sigma^{2}\_{i,t}=\omega\_{i}+\alpha\_{i}\epsilon^{2}\_{i,t-1}+\beta\_{i}\sigma^{2}\_{i,t-1}, estimated by QMLE.
Panel C shows the correlations of the devolatilized returns yi,t=ϵi,t/σi,ty\_{i,t}=\epsilon\_{i,t}/\sigma\_{i,t}. In all cases the mean and the range over the cross-sectional dimension of 100 stocks is given.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section |  | mean | range |  |  | mean | range |
| Panel A: log-returns ri,tr\_{i,t} | | | | | | | |
| Mean |  | 0.000 | [−0.001, 0.001][-0.001,\,0.001] |  | Skewness | −0.406-0.406 | [−1.82, 1.25][-1.82,\,1.25] |
| Std. dev. |  | 0.018 | [0.011, 0.030][0.011,\,0.030] |  | Kurtosis | 12.95 | [5.72, 35.25][5.72,\,35.25] |
| Panel B: univariate AR(1)-GARCH(1,1) parameter estimation results | | | | | | | |
| ωi\sqrt{\omega\_{i}} |  | 0.004 | [0.001, 0.011][0.001,\,0.011] |  | δi\delta\_{i} | 0.000 | [−0.001, 0.001][-0.001,\,0.001] |
| αi\alpha\_{i} |  | 0.090 | [0.013, 0.317][0.013,\,0.317] |  | ϕi\phi\_{i} | -0.023 | [−0.195, 0.061][-0.195,\,0.061] |
| βi\beta\_{i} |  | 0.846 | [0.548, 0.979][0.548,\,0.979] |  |  |  |  |
| Panel C: Average cross-sectional correlations devolatilized residuals yi,t=ϵi,t/σi,ty\_{i,t}=\epsilon\_{i,t}/\sigma\_{i,t} | | | | | | | |
| ρi,j\rho\_{i,j} |  | 0.275 | [0.004, 0.786][0.004,\,0.786] |  |  |  |  |

We merge the time series of the log-returns from different countries based on common trading days.
This results in a data set with T=2,425T=2,425 daily returns ri,tr\_{i,t} for each asset i=1,…,di=1,\ldots,d.
Summary statistics of the data are presented in Panel A of Table [4](https://arxiv.org/html/2601.13281v1#S4.T4 "Table 4 ‣ 4.1 Data ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), confirming standard stylized facts such as unconditional left-skewness and substantial excess kurtosis of the raw log-returns.

We filter each time series ri,tr\_{i,t} using a standard AR(1)-GARCH(1,1) filter
and proceed the analysis with the devolatilized residuals yi,t=ϵi,t/σi,ty\_{i,t}=\epsilon\_{i,t}/\sigma\_{i,t}.
Panel B of Table [4](https://arxiv.org/html/2601.13281v1#S4.T4 "Table 4 ‣ 4.1 Data ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") summarizes the univariate estimation results.
The first two columns of panels in Fig. [2](https://arxiv.org/html/2601.13281v1#S4.F2 "Figure 2 ‣ 4.1 Data ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") show the autocorrelation functions for absolute log-returns |ri,t||r\_{i,t}| and for absolute devolatilized returns |yi,t||y\_{i,t}| for 3 (arbitrarily chosen) stocks.
As expected, we observe strong serial correlation for the |ri,t||r\_{i,t}|, which indicates clear volatility clustering effects.
After applying the univariate AR(1)-GARCH(1,1) filters, the standardized absolute residuals |yi,t||y\_{i,t}| no longer indicate any substantial volatility clustering.
We take these standardized residuals yi,ty\_{i,t} as input for the Probability Integral Transformations (PITs) using the rank-based transforms ui,t=rank​(yi,t)/(T+1/2)u\_{i,t}=\text{rank}(y\_{i,t})/(T+1/2) as motivated in Section [2.4](https://arxiv.org/html/2601.13281v1#S2.SS4 "2.4 Parameter estimation ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
Our final sample consists of T=2,425T=2,425 pseudo-copula observations in d=100d=100 dimensions.
We use the first half of the data for estimation, and the second half for our out-of-sample performance evaluation.

![Refer to caption](x2.png)


Figure 2: Autocorrelation functions for log-returns |ri,t||r\_{i,t}|, devolatilized residuals |yi,t||y\_{i,t}|, |yi,t⋆|=|G−1​(ui,t)||y^{\star}\_{i,t}|=|G^{-1}(u\_{i,t})| and spectral projections |y~i,t⋆||\tilde{y}^{\star}\_{i,t}| for i=1,2,10i=1,2,10. The Gaussian copula (γ=𝟎d\gamma=\bm{0}\_{d} and ν−1=0\nu^{-1}=0) is used to determine yi,t⋆y^{\star}\_{i,t} and y~i,t⋆\tilde{y}^{\star}\_{i,t}.

Interestingly, we can use the pseudo-copula observations yi,t⋆=Gi​(ui,t)y^{\star}\_{i,t}=G\_{i}(u\_{i,t}) to explore whether there will be time-variation in the eigenvalues of the copula dependence matrix.
The third column in Figure [2](https://arxiv.org/html/2601.13281v1#S4.F2 "Figure 2 ‣ 4.1 Data ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") provides the autocorrelation function of the absolute pseudo-copula observations |yi,t⋆||y^{\star}\_{i,t}|.
Again, we see no substantial signal of volatility clustering in the values of yi,t⋆y^{\star}\_{i,t}.
However, if we compute the eigenvalue-eigenvector decomposition of the sample correlation matrix of 𝒚t\bm{y}\_{t} and use it to compute initial estimates of the spectral projections y~i,t⋆\tilde{y}^{\star}\_{i,t}, the last column of Figure [2](https://arxiv.org/html/2601.13281v1#S4.F2 "Figure 2 ‣ 4.1 Data ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") clearly shows volatility clustering effects for the first spectral projection, which is indicative of time-variation in λ1,t\lambda\_{1,t}.
As another example, also the second spectral projection is shown, for which the time-varying volatility, i.e., a time-varying λ2,t\lambda\_{2,t}, is less strong.
The further down in the spectrum we consider the spectral projections, the less evidence we find for a time-varying λi,t\lambda\_{i,t}.
For instance, for i=10i=10 the lower-right autocorrelation function largely remains within the confidence band.
This indicates that a modeling approach with a limited number of time-varying λi,t\lambda\_{i,t}s for the copula dependence parameters is both parsimonious and congruent with the financial data at hand.

Before presenting the estimation results for the dynamic spectral regularized copula specification, we note that our analysis differs conceptually from existing (spectral) GARCH models in the literature, such as the orthogonal GARCH or the λ\lambda GARCH models [e.g., Hetland et al., [2023](https://arxiv.org/html/2601.13281v1#bib.bib47 "Dynamic conditional eigenvalue garch")].
The latter do not explicitly distinguish between the marginal and the copula time series.
As a result, the conditional volatility effects in spectral directions in those models could stem from marginal volatility increases as well as from increased correlation effects.
In our framework, by contrast, a larger conditional variance λ1,t\lambda\_{1,t} solely reflects the dynamics of the copula, allowing us to answer whether strongly dependent market movements (as measured by the first spectral projections) are followed by periods of higher dependence.

### 4.2 Estimation results

Given that the time-variation in λi,t\lambda\_{i,t} is concentrated in the first few spectral projections according to the autocorrelograms in Figure [2](https://arxiv.org/html/2601.13281v1#S4.F2 "Figure 2 ‣ 4.1 Data ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), we use a BIC guided selection procedure to determine the final number of dynamic components.
We start from the static skew tt copula, after which we make the first eigenvalue dynamic.
We report the change in (unregularized) BIC relative to the static model.
After that, we also make the second value dynamic and report the change in BIC relative to the static model, and so on.
We do not apply shrinkage at this stage.
Figure [3](https://arxiv.org/html/2601.13281v1#S4.F3 "Figure 3 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") shows the changes in the BIC vis-à-vis the static model when adding the dynamic eigenvalues for the skewed tt copula one by one for i=1,…,7i=1,...,7.
Clearly, the largest gain is obtained by allowing the first λi,t\lambda\_{i,t} to be dynamic, followed by a smaller improvement for i=2i=2.
The BIC is at its minimum for i=2i=2 dynamic components, which therefore is the value we use in the remainder of the analysis.
We use the same number of 2 dynamic eigenvalues for the three different copula densities, endowing them with the score-driven dynamics from Section [2.2](https://arxiv.org/html/2601.13281v1#S2.SS2 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").

Table 5: 
Performance of various static and dynamic copula specifications with either a factor structure or a regularized spectral structure for the correlation matrix. We consider 100 European stocks from 10 different countries and industry sectors (d=100d=100) with 10 years of daily data. The first 5 years are used for estimation and the last 5 years for out-of-sample performance.
Panel A shows the in-and out-of-sample log-likelihood for dynamic copula specifications.
Panel B shows the same results based on static copula specifications.
The best performing copula specification is indicated in bold, which is the dynamic skew tt copula with non-linear shrinkage.

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Regularized | | |  | Sample | | |  | Factor | | |
|  | G | tdt\_{d} | skew tdt\_{d} |  | G | tdt\_{d} | skew tdt\_{d} |  | G | tdt\_{d} | skew tdt\_{d} |
| Panel A: dynamic copula likelihoods | | | | | | | | | |  |  |
| ℓi​n\ell\_{in} | 38,068 | 38,537 | 38,574 |  | 38,220 | 39,012 | 39,045 |  | 28,376 | 29,641 | 29,686 |
| ℓo​u​t\ell\_{out} | 27,882 | 29,725 | 𝟐𝟗,𝟕𝟓𝟐\bm{29,752} |  | 27,139 | 28,705 | 28,733 |  | 24,882 | 26,531 | 26,555 |
| Panel B: static copula likelihoods | | | | | | | | | |  |  |
| ℓi​n\ell\_{in} | 37,397 | 38,058 | 38,104 |  | 37,664 | 38,650 | 38,691 |  | 28,088 | 29,481 | 29,529 |
| ℓo​u​t\ell\_{out} | 26,769 | 29,529 | 29,549 |  | 25,513 | 28,230 | 28,253 |  | 23,605 | 25,696 | 25,727 |

Table [5](https://arxiv.org/html/2601.13281v1#S4.T5 "Table 5 ‣ 4.2 Estimation results ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") shows the performance for the three different approaches (Regularized spectral copula, Sample-based spectral copula, and the Factor copula with clustering) and three different choices for the copula density (Gaussian, Student’s tt, and the skewed tt).
We estimate the factor model with optimal cluster assignment in 100 dimensions using the algorithm of Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")], where 17 clusters turn out to be optimal in terms of BIC.
Panels A and B of Table [5](https://arxiv.org/html/2601.13281v1#S4.T5 "Table 5 ‣ 4.2 Estimation results ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") show the in-sample and out-of-sample log-likelihood values for the different dynamic and static models, respectively.
First, we find that the spectral dynamic copula models (panel A) perform significantly better than the static copula models (panel B), both in-sample and out-of-sample.
Modeling the dynamics of the dependence structure thus significantly improves the fit and predictive power of the models, even in the current parsimonious setting where only 2 out of the 100 eigenvalues are dynamic.
Second, the dynamic factor copula specifications with endogenous clustering perform significantly worse compared to the regularized dynamic spectral copula specifications.
This is mainly due to their more restrictive dependence structure compared to the spectral copula specification.
Third, as expected and as mentioned earlier, the tt copula performs substantially better than its Gaussian counterpart.
Performance differences between the symmetric and the skew tt copulas, by contrast, are modest, though there is a slight increase in the log-likelihood, both in-sample and out-of-sample.
Finally, non-linear shrinkage of the unconditional eigenvalues leads to significant improvements of +1000+1000 points in the out-of-sample log-likelihood compared to the sample eigenvalues.
Spectral dynamics and regularization thus emerge as the most important aspects in modeling the copula dependence spectrum for large dd and TT.

In Table [6](https://arxiv.org/html/2601.13281v1#S4.T6 "Table 6 ‣ 4.2 Estimation results ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), we show the parameter estimates for the two dynamic spectral indices of the best performing dynamic skew tt copula with regularization.
To obtain confidence intervals for the estimates, the block bootstrap method was used on pseudo-copula observations ui,tu\_{i,t} using 20 trading days as block length and 200 bootstrap samples.
For both eigenvalues, the dynamics are highly persistent with b1b\_{1} and b2b\_{2} equal to 0.9 or higher.
The value of a1a\_{1} can be accurately estimated and appears clearly significant, signaling a time-varying dependence structure.
The value of a2a\_{2} can be less accurately estimated and the corresponding improvement in log-likelihood is smaller, but it is still yields a lower BIC and also the out-of-sample log-likelihood improves.
Such observations are also in line with Figure [2](https://arxiv.org/html/2601.13281v1#S4.F2 "Figure 2 ‣ 4.1 Data ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
The estimated value for the skewness parameter γ\gamma is significantly negative, while the estimated tail parameter ν\nu is fairly large with values around 45. Still, the improvement in log-likelihood is substantial when allowing for tail-dependence, both in sample and out-of-sample, as can be seen from Table [6](https://arxiv.org/html/2601.13281v1#S4.T6 "Table 6 ‣ 4.2 Estimation results ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") when comparing the (skewed) tt copula with its Gaussian counterpart.

Table 6: 
Estimation results for the skew tt copula with spectral dynamics based on 100 European stocks and 5 years of historic data.
The 90% confidence intervals are determined with the block bootstrap method on the pseudo-copula observations ui,tu\_{i,t} using 20 trading days as block length.

| Par. | Est. | 90% CI | Par. | Est. | 90% CI | Par. | Est. | 90% CI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| λˇ1\check{\lambda}\_{1} | 30.6 | [26.2,  35.5] | a1a\_{1} | 0.06 | [0.05,  0.07] | b1b\_{1} | 0.90 | [0.86,  0.94] |
| λˇ2\check{\lambda}\_{2} | 5.8 | [ 5.3,   6.6] | a2a\_{2} | 0.06 | [0.03,  0.21] | b2b\_{2} | 0.97 | [0.26,  0.99] |
| ν\nu | 44.1 | [41.7,  54.8] | γ\gamma | -0.37 | [-0.47,  -0.21] |  |  |  |

### 4.3 Eigenvalues and eigenvectors

![Refer to caption](x3.png)


Figure 3: Spectral dynamics of the first spectral eigenvalue, where the ratio of the first eigenvalue and the sum of the higher eigenvalues is plotted over time. Under normal market circumstances, the first eigenvalue explains about 30% of the spectral variance, leading to a ratio below 1/2. When the ratio increases, it signals enhanced spectral variance in the parallel direction (first eigenvector) compared to the total spectral variance in the orthogonal directions, indicating less diversification and higher systemic risk or return. The three most pronounced events are given an economic interpretation. The period from January 2020 to December 2024 represents an out-of-sample forecast.

To conclude the empirical analysis, we zoom in on several aspects of the estimation results, such as the eigenvalue dynamics and its relation to financial crises, as well as the interpretation of the first eigenvectors.
We use the best performing copula model, namely the skew tdt\_{d} copula with regularized spectral dynamics.
In the right plot of Fig. [3](https://arxiv.org/html/2601.13281v1#S4.F3 "Figure 3 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), we show the dynamics of the first eigenvalue λ1,t\lambda\_{1,t}, where we plot the ratio of the first eigenvalue to the sum of the smaller eigenvalues (i≤2i\leq 2) over time.
Under normal market circumstances, the first eigenvalue explains about 30% of the spectral variance, leading to a ratio around 30/70, which is below 0.5.
There is strong serial dependence in the first eigenvalue, in line with the earlier result in the right-hand panels in Figure [2](https://arxiv.org/html/2601.13281v1#S4.F2 "Figure 2 ‣ 4.1 Data ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") and Panel A in Table [6](https://arxiv.org/html/2601.13281v1#S4.T6 "Table 6 ‣ 4.2 Estimation results ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
As is seen in Figure [4](https://arxiv.org/html/2601.13281v1#S4.F4 "Figure 4 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), the first eigenvector takes a more or less equally weighted position in each of the assets, thus reflecting a parallel movement in the market.
Increases in the first eigenvalue compared to the remaining ones therefore result in correlation matrices with less diversification potential, leading to periods with higher systemic risk.
The right-hand panel in Figure [3](https://arxiv.org/html/2601.13281v1#S4.F3 "Figure 3 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") reveals that such parallel-to-orthogonal variance ratio increases can reach up to a factor two or higher during crisis periods, implying the first eigenvalue explains up to 70% of the spectral variance during such times.
During these crisis events, the cross-sectional average correlation 𝑹¯t\bar{\bm{R}}\_{t} peaks at 0.65, while the unconditional average is only 0.30.
The three most pronounced events in the time period of Figure [3](https://arxiv.org/html/2601.13281v1#S4.F3 "Figure 3 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") are the flash crash in 2015, the Brexit in 2016 and the Covid pandemic in 2020, which corroborate the lack of diversification potential during such periods.

![Refer to caption](x4.png)

![Refer to caption](ev2.png)

Figure 4: Heatmap of estimated eigenvectors weights w^i,j\hat{w}\_{i,j} of the unconditional copula correlation matrix 𝑹^\hat{\bm{R}} from Eq. ([10](https://arxiv.org/html/2601.13281v1#S2.E10 "In 2.4 Parameter estimation ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")). The first two eigenvectors are shown (j=1,2j=1,2). The stocks ii are ordered in terms of countries along the xx-axis and in terms of sectors along the yy-axis. The white color indicates that the country-sector combination is absent in the data set. In case of two stocks per country-sector combination, the result for the first stock from Table [C.1](https://arxiv.org/html/2601.13281v1#A3.T1 "Table C.1 ‣ Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") is shown. The first eigenvector has positive weights for all stocks, corresponding to a parallel market movement. We compare the second eigenvector with optimal cluster assigments using Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")] giving 17 clusters, indicated by the numbers in each sector-country cell. The colors relate to the value of the corresponding element of the eigenvectors in the spectral copula specification.
The bottom panel contains the same information as the right-hand panel, but the stocks are ordered per cluster (in order of their average value of the second eigenvector elements).

In Figure [4](https://arxiv.org/html/2601.13281v1#S4.F4 "Figure 4 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), we analyze the eigenvectors corresponding to the largest two dynamic eigenvalues in more detail and compare them to the cluster assignments based on Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")].
This is an extention to Gubbels et al. [[2025](https://arxiv.org/html/2601.13281v1#bib.bib17 "Principal component copulas for capital modelling and systemic risk")], who perform the eigenvector analysis solely for country-effects in a static spectral copula context.
The left panel shows the first eigenvector as a heatmap.
All elements are positive and of roughly equal magnitude, so that the first eigenvector represents the collective movement of the European stock market as a whole.
This is in line with the market factor interpretation of the first factor by Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")]: the estimated intercepts of the factor loadings for the optimal number (using the BIC) of 17 clusters are all positive, see Table [C.2](https://arxiv.org/html/2601.13281v1#A3.T2 "Table C.2 ‣ Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") of Supplementary [C](https://arxiv.org/html/2601.13281v1#A3 "Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
Moreover, we also see from Figure [4](https://arxiv.org/html/2601.13281v1#S4.F4 "Figure 4 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") that the stocks with lowest weight in the first eigenvector (green color in the left panel) all correspond to cluster 11, which has the lowest market co-movement in Table [C.2](https://arxiv.org/html/2601.13281v1#A3.T2 "Table C.2 ‣ Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
More generally, the inner product of the first eigenvectors of the unconditional correlation matrix from both approaches is 0.994.

To further compare the spectral eigenvectors with the optimal cluster assignments based on the methodology of Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")], we label each of the assets by their cluster number 1,…,17, where 17 denotes the optimal number of clusters in terms of the BIC.
The right-hand panel in Figure [4](https://arxiv.org/html/2601.13281v1#S4.F4 "Figure 4 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") shows the heatmap of the second eigenvector, which is orthogonal to the first eigenvector.
It represents the most important cross-sectional direction for diversification in the European stock market.
The eigenvector mainly captures the diversification between different sectors, where the financial, energy and basic material sectors have opposite sign to the real estate, health, utility and consumer non-cyclical sectors.
From Table [C.2](https://arxiv.org/html/2601.13281v1#A3.T2 "Table C.2 ‣ Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") and Figure [1(b)](https://arxiv.org/html/2601.13281v1#A3.F1.sf2 "In Figure C.1 ‣ Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), we see that clusters 3, 7, 12, 14 have the largest absolute cluster loadings ωiC\omega^{C}\_{i}) and represent the sectors real estate, financials, utilities and energy.
For these clusters, the corresponding eigenvector weights are most negative for sectors 7 and 14, and most positive for sectors 3 and 12.
This means that there is alignment between the two models in identifying co-moving stocks.
Although weaker than sector effects, we also observe country effects in the second eigenvector.
The colors that correspond to Norway are more aligned with Sweden than with the UK, for example.
This shows that in our heterogeneous data set both industry sectors and countries have intertwined effects.
To further illustrate the alignment between cluster assignments and the second eigenvector, the bottom panel in Figure [4](https://arxiv.org/html/2601.13281v1#S4.F4 "Figure 4 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") shows the heatmap of the weights grouped per cluster and sorted by their (cluster) average weight.
The cluster factor selects clusters with similar second eigenvalue weights in the spectral decomposition.
The main difference between the two approaches, however, lies in the handling of the between-cluster correlations: in the cluster factor approach with its block-diagonal cluster loading matrix (see Supplementary [B.1](https://arxiv.org/html/2601.13281v1#A2.SS1 "B.1 Reference model ‣ Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) the off-diagonal factor loadings are restricted to zero, whereas no such restriction applies in the spectral approach.
This is the primary cause why the spectral approach obtains a better fit to the data.

![Refer to caption](x5.png)


Figure 5: Estimated eigenvalues excluding and including shrinkage, λ^i\hat{\lambda}\_{i} and μ^i\hat{\mu}\_{i}, of the unconditional copula correlation matrix for the dynamic skew tt copula. The sample eigenvalues are ordered from high to low. The left plot shows the first 10 eigenvalues and the middle plot the other 90 eigenvalues. The sample eigenvalues are shown in blue, while the eigenvalues after applying shrinkage are shown in red. The right plot shows the out-of-sample log-likelihood improvement when the first ii sample eigenvalues are replaced with shrinkage eigenvalues. The largest improvements stem from the highest spectral indices, whose sample eigenvalues are most severely biased.

As final analysis, we zoom in on the effect of shrinkage on the empirical results.
When d=100d=100, the concentration ratio d/Td/T is 8%, since we use T=1,213T=1,213 in-sample observations for estimation.
Though modest, the biasing effect on the spectrum is clearly present, as we have seen in the earlier results.
To understand how the quadratic shrinkage procedure contributes to the fit of the model to the empirical data, Figure [5](https://arxiv.org/html/2601.13281v1#S4.F5 "Figure 5 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") shows the largest 10 and the remaining 90 shrunken and unshrunken targeted intercepts ω^i\hat{\omega}\_{i} from the score-driven transition dynamics in ([5](https://arxiv.org/html/2601.13281v1#S2.E5 "In 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")).
For the largest eigenvalues we observe that shrinkage leads to a (slight) downward adjustment, since the sample eigenvalues have an upward bias.
For the lowest eigenvalues, the converse happens.
The relative impact of shrinkage is much larger at the lower end of the spectrum.
It is precisely this correction at the lower end of the spectrum that causes the substantial increases in out-of-sample log-likelihood.
To see this, Figure [5](https://arxiv.org/html/2601.13281v1#S4.F5 "Figure 5 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") plots the improvement in out-of-sample log-likelihood for the dynamic skew tt copula due to non-linear shrinkage as a function of the spectral index.
We calculate this change in log-likelihood by only replacing the sample eigenvalues with regularized eigenvalues up to spectral index ii, for i=1,…,100i=1,\ldots,100, such that i=100i=100 corresponds to the fully regularized model.
The figure shows that the bulk of the out-of-sample likelihood improvement comes from the highest spectral indices (i>70i>70).
It underlines the importance of the regularization step for in the new model’s set-up for the small eigenvalues jointly with introducing dynamics for the largest eigenvalues.

## 5 Conclusion

In this article, we proposed a new dynamic copula model for high-dimensional time-dependent financial applications based on the skewed tt copula.
The model does not require variables to be grouped in clusters, but rather uses a spectral decomposition of the copula dependence matrix.
Asymptotic biases in the spectrum are avoided by regularization of the correlation matrix, while the dynamics are captured via time-varying volatilities in the principal spectral dimensions, where the number of dynamic components is kept to a minimum via a model selection procedure based on the BIC.
The combination of all three elements results in a parsimonious, yet flexible time-varying dependence model with limited complexity and increased interpretability.

A simulation study confirmed that the regularized dynamic copula performs well out-of-sample in high-dimensional settings with general dependence structures.
In an empirical study, we showed that regularized score-driven spectral dynamics can be used to study contractions in the dependence structure of the international financial market during crisis times, which reduces diversification potential and enhances systemic risk.
We also showed that regularization outperforms cluster assignments in terms of in-sample and out-of-sample performance for our heterogeneous data set containing a broad range of countries and sectors.
In particular, regularization turned out to be most important at the low end of the spectrum, while the introduction of dynamics was most important for the highest eigenvalues.

## References

* I. Archakov and P. R. Hansen (2021)
  A new parametrization of correlation matrices.
  Econometrica 89,  pp. 1699–1715.
  Cited by: [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p2.8 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p7.11 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* E. A. Beutner, Y. Lin, and A. Lucas (2023)
  Consistency, distributional convergence, and optimality of score-driven filters.
  Technical report
  Technical Report TI 2023-051/III, Tinbergen Institute Discussion Paper.
  Cited by: [§3.2](https://arxiv.org/html/2601.13281v1#S3.SS2.p5.1 "3.2 Experiment 2: quality of point and path estimates ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* G. Buccheri, G. Bormetti, F. Corsi, and F. Lillo (2021)
  A score-driven conditional correlation model for noisy and asynchronous data: an application to high-frequency covariance dynamics.
  Journal of Business & Economic Statistics 39 (4),  pp. 920–936.
  Cited by: [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p2.8 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p7.11 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* D. D. Creal, S. Koopman, and A. Lucas (2013)
  Generalized autoregressive score models with applications.
  Journal of Applied Econometrics 28,  pp. 777–795.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p4.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p3.1 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p3.3 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p5.12 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* D. D. Creal and Tsay,R. S. (2015)
  High dimensional dynamic stochastic copula models.
  Journal of Econometrics 189 (2),  pp. 335–345.
  External Links: ISSN 0304-4076,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.jeconom.2015.03.027)
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p3.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* D. Creal, S. J. Koopman, and A. Lucas (2011)
  A dynamic multivariate heavy-tailed model for time-varying volatilities and correlations.
  Journal of Business & Economic Statistics 29 (4),  pp. 552–563.
  External Links: [Document](https://dx.doi.org/10.1198/jbes.2011.10070),
  [Link](https://doi.org/10.1198/jbes.2011.10070)
  Cited by: [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p2.8 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p7.11 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* S. Demarta and A.J. McNeil (2005)
  The t copula and related copulas.
  International Statistical Review 73 (1),  pp. 111–129.
  Cited by: [§2.1](https://arxiv.org/html/2601.13281v1#S2.SS1.p1.25 "2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* D. L. Donoho, M. Gavish, and I. M. Johnstone (2018)
  Optimal shrinkage of eigenvalues in the spiked covariance model.
  Annals of statistics 46 (4),  pp. 1742–1778.
  Cited by: [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p2.1 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* R.F. Engle, O. Ledoit, and M. Wolf (2019)
  Large dynamic covariance matrices.
  Journal of Business & Economic Statistics 37,  pp. 363–375.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p2.2 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p1.9 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* R.F. Engle (2002)
  Dynamic conditional correlation: a simple class of multivariate generalized autoregressive conditional heteroskedasticity models.
  Journal of Business & Economic Statistics 20,  pp. 339–350.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p2.2 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* R. Engle and B. Kelly (2012)
  Dynamic equicorrelation.
  Journal of Business & Economic Statistics 30 (2),  pp. 212–228.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p2.2 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* E. F. Fama and K. R. French (1993)
  Common risk factors in the returns on stocks and bonds.
  Journal of Financial Economics 33 (1),  pp. 3–56.
  Cited by: [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p2.1 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* E. F. Fama and K. R. French (1998)
  Value versus growth: the international evidence.
  The Journal of Finance 53 (6),  pp. 1975–1999.
  External Links: [Document](https://dx.doi.org/10.1111/0022-1082.00085),
  [Link](onlinelibrary.wiley.com)
  Cited by: [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p2.1 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* J. Fan, Y. Liao, and M. Mincheva (2013)
  Large covariance estimation by thresholding principal orthogonal complements.
  Journal of the Royal Statistical Society Series B: Statistical Methodology 75,  pp. 603––680.
  Cited by: [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p2.1 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* K.B. Gubbels, Y. Ypma, and C.W. Oosterlee (2025)
  Principal component copulas for capital modelling and systemic risk.
  Computational Economics.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1007/s10614-025-11051-7)
  Cited by: [§4.3](https://arxiv.org/html/2601.13281v1#S4.SS3.p2.1 "4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* C. M. Hafner and L. Wang (2023)
  A dynamic conditional score model for the log correlation matrix.
  Journal of Econometrics 237 (2, Part B),  pp. 105176.
  External Links: [Document](https://dx.doi.org/10.1016/j.jeconom.2023.105176)
  Cited by: [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p2.8 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p7.11 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* A. Harvey (2013)
  Dynamic models for volatility and heavy tails: with applications to financial and economic time series.
   Cambridge University Press.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p4.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p3.1 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p5.12 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* S. Hetland, R. S. Pedersen, and A. Rahbek (2023)
  Dynamic conditional eigenvalue garch.
  Journal of Econometrics 237 (2),  pp. 105175.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p4.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p4.6 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§4.1](https://arxiv.org/html/2601.13281v1#S4.SS1.p6.2 "4.1 Data ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* P. Jaeckel and R. Rebonato (2000)
  The most general methodology for creating a valid correlation matrix for risk management and option pricing purposes.
  Journal of Risk 2 (2),  pp. 17–28.
  External Links: [Document](https://dx.doi.org/10.21314/JOR.2000.023),
  [Link](https://doi.org/10.21314/JOR.2000.023)
  Cited by: [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p2.8 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* H. Joe (2006)
  Dependence modeling with copulas.
   Chapman & Hall.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p1.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* I. M. Johnstone (2001)
  On the distribution of the largest eigenvalue in principal components analysis.
  Annals of statistics 29 (2),  pp. 295–327.
  Cited by: [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p1.9 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p2.1 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* O. Ledoit and M. Wolf (2004a)
  A well-conditioned estimator for large-dimensional covariance matrices.
  Journal of Multivariate Analysis 88,  pp. 365–411.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p4.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* O. Ledoit and M. Wolf (2022a)
  Quadratic shrinkage for large covariance matrices.
  Bernoulli 28,  pp. 1519–1547.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p4.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p1.13 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p1.9 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.4](https://arxiv.org/html/2601.13281v1#S2.SS4.p2.19 "2.4 Parameter estimation ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3.1](https://arxiv.org/html/2601.13281v1#S3.SS1.p7.1 "3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [Table 3](https://arxiv.org/html/2601.13281v1#S3.T3 "In 3.2 Experiment 2: quality of point and path estimates ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [Table 3](https://arxiv.org/html/2601.13281v1#S3.T3.8.4 "In 3.2 Experiment 2: quality of point and path estimates ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* O. Ledoit and M. Wolf (2022b)
  The power of (non-) linear shrinking: a review and guide to covariance matrix estimation.
  Journal of Financial Econometrics 20,  pp. 187–218.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p4.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p1.9 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3.1](https://arxiv.org/html/2601.13281v1#S3.SS1.p7.1 "3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* O. Ledoit and M. Wolf (2004b)
  Honey, i shrunk the covariance matrix.
  The Journal of Portfolio Management 30 (4),  pp. 110–119.
  External Links: [Document](https://dx.doi.org/10.3905/jpm.2004.110),
  [Link](https://doi.org/10.3905/jpm.2004.110)
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p2.2 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* O. Ledoit and M. Wolf (2012)
  Nonlinear shrinkage estimation of large-dimensional covariance matrices.
  The Annals of Statistics 40 (2),  pp. 1024–1060.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p2.2 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p1.9 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* A. Lucas, B. Schwaab, and X. Zhang (2014)
  Conditional euro area sovereign default risk.
  Journal of Business & Economic Statistics 32 (2),  pp. 271–284.
  Cited by: [§2.1](https://arxiv.org/html/2601.13281v1#S2.SS1.p2.11 "2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* A. Lucas, B. Schwaab, and X. Zhang (2017)
  Modeling financial sector joint tail risk in the euro area.
  Journal of Applied Econometrics 32 (1),  pp. 171–191.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p2.2 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§1](https://arxiv.org/html/2601.13281v1#S1.p4.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* V.A. Marčenko and L.A. Pastur (1967)
  Distribution of eigenvalues for some sets of random matrices.
  Sb. Math. 1,  pp. 457–483.
  Cited by: [§2.3](https://arxiv.org/html/2601.13281v1#S2.SS3.p1.9 "2.3 Non-linear shrinkage and model selection ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* A.J. McNeil, R. Frey, and P. Embrechts (2005)
  Quantitative risk management.
   Princeton University Press.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p1.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* D. H. Oh and A. J. Patton (2017)
  Modeling dependence in high dimensions with factor copulas.
  Journal of Business & Economic Statistics 35 (1),  pp. 139–154.
  Cited by: [§1](https://arxiv.org/html/2601.13281v1#S1.p3.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3.1](https://arxiv.org/html/2601.13281v1#S3.SS1.p2.5 "3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3](https://arxiv.org/html/2601.13281v1#S3.p1.1 "3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* D. H. Oh and A. J. Patton (2018)
  Time-varying systemic risk: evidence from a dynamic copula model of cds spreads.
  Journal of Business & Economic Statistics 36 (2),  pp. 181–195.
  Cited by: [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p1.2 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p8.11 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3.1](https://arxiv.org/html/2601.13281v1#S3.SS1.p2.5 "3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3](https://arxiv.org/html/2601.13281v1#S3.p1.1 "3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* D. H. Oh and A.J. Patton (2023)
  Dynamic factor copula models with estimated cluster assignments.
  Journal of Econometrics 237 (2, Part C),  pp. 105374.
  Cited by: [§B.1](https://arxiv.org/html/2601.13281v1#A2.SS1.p1.3 "B.1 Reference model ‣ Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§B.1](https://arxiv.org/html/2601.13281v1#A2.SS1.p2.3 "B.1 Reference model ‣ Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§B.1](https://arxiv.org/html/2601.13281v1#A2.SS1.p3.1 "B.1 Reference model ‣ Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§B.1](https://arxiv.org/html/2601.13281v1#A2.SS1.p4.1 "B.1 Reference model ‣ Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§B.1](https://arxiv.org/html/2601.13281v1#A2.SS1.p4.2 "B.1 Reference model ‣ Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [Figure C.1](https://arxiv.org/html/2601.13281v1#A3.F1 "In Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [Figure C.1](https://arxiv.org/html/2601.13281v1#A3.F1.2.1 "In Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [Appendix C](https://arxiv.org/html/2601.13281v1#A3.p3.1 "Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§1](https://arxiv.org/html/2601.13281v1#S1.p3.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§1](https://arxiv.org/html/2601.13281v1#S1.p5.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.1](https://arxiv.org/html/2601.13281v1#S2.SS1.p2.11 "2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p1.2 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p8.11 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3.1](https://arxiv.org/html/2601.13281v1#S3.SS1.p2.5 "3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3.1](https://arxiv.org/html/2601.13281v1#S3.SS1.p5.8 "3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3.1](https://arxiv.org/html/2601.13281v1#S3.SS1.p6.2 "3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3.1](https://arxiv.org/html/2601.13281v1#S3.SS1.p8.3 "3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3](https://arxiv.org/html/2601.13281v1#S3.p1.1 "3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [Figure 4](https://arxiv.org/html/2601.13281v1#S4.F4 "In 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [Figure 4](https://arxiv.org/html/2601.13281v1#S4.F4.12.6 "In 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§4.1](https://arxiv.org/html/2601.13281v1#S4.SS1.p2.1 "4.1 Data ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§4.2](https://arxiv.org/html/2601.13281v1#S4.SS2.p2.7 "4.2 Estimation results ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§4.3](https://arxiv.org/html/2601.13281v1#S4.SS3.p2.1 "4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§4.3](https://arxiv.org/html/2601.13281v1#S4.SS3.p3.1 "4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* A. Opschoor, A. Lucas, I. Barra, and D. Van Dijk (2021)
  Closed-form multi-factor copula models with observation-driven dynamic factor loadings.
  Journal of Business & Economic Statistics 39 (4),  pp. 1066–1079.
  Cited by: [§B.1](https://arxiv.org/html/2601.13281v1#A2.SS1.p1.3 "B.1 Reference model ‣ Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§B.1](https://arxiv.org/html/2601.13281v1#A2.SS1.p2.3 "B.1 Reference model ‣ Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§1](https://arxiv.org/html/2601.13281v1#S1.p3.1 "1 Introduction ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.1](https://arxiv.org/html/2601.13281v1#S2.SS1.p2.11 "2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p1.2 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§2.2](https://arxiv.org/html/2601.13281v1#S2.SS2.p8.11 "2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3.1](https://arxiv.org/html/2601.13281v1#S3.SS1.p2.5 "3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3.1](https://arxiv.org/html/2601.13281v1#S3.SS1.p5.8 "3.1 Experiment 1: spectral versus grouped copula structures ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"),
  [§3](https://arxiv.org/html/2601.13281v1#S3.p1.1 "3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
* A. J. Patton (2006)
  Modelling asymmetric exchange rate dependence.
  International economic review 47 (2),  pp. 527–556.
  Cited by: [§2.1](https://arxiv.org/html/2601.13281v1#S2.SS1.p1.7 "2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").

Supplementary Materials for
  
“Spectral Dynamics and Regularization for High-Dimensional Copulas”

Koos Gubbelsa and Andre Lucasb

a: Tilburg University

b: Vrije Universiteit Amsterdam and Tinbergen Institute

## Appendix A Proofs

#### Proof of Proposition [1](https://arxiv.org/html/2601.13281v1#Thmtheorem1 "Proposition 1 (score equations for spectral dynamics). ‣ 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")

Using Eqs. ([1](https://arxiv.org/html/2601.13281v1#S2.E1 "In 2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) and ([2](https://arxiv.org/html/2601.13281v1#S2.E2 "In 2.1 Generalized hyperbolic skewed t copula ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) and noting that yi,t⋆=yi,t⋆​(ui,t,ν,γi)=Gi−1​(ui,t;𝜽c,t)y^{\star}\_{i,t}=y^{\star}\_{i,t}(u\_{i,t},\nu,\gamma\_{i})=G\_{i}^{-1}(u\_{i,t};\bm{\theta}\_{c,t}) depends on ν\nu and γi\gamma\_{i}, but not on 𝒇t\bm{f}\_{t}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇i,t\displaystyle\nabla\_{i,t} | =∂c​(𝒖t∣ℱt−1,𝜽c,t)∂fi,t=∂∂fi,t​log⁡g​(𝒚⋆t;𝜽c,t)−∑i=1d∂∂fi,t​log⁡gi​(yi,t⋆;𝜽c,t)\displaystyle=\frac{\partial c(\bm{u}\_{t}\mid\mathcal{F}\_{t-1},\bm{\theta}\_{c,t})}{\partial f\_{i,t}}=\frac{\partial}{\partial f\_{i,t}}\log g(\bm{y^{\star}}\_{t};\bm{\theta}\_{c,t})-\sum\_{i=1}^{d}\frac{\partial}{\partial f\_{i,t}}\log g\_{i}(y^{\star}\_{i,t};\bm{\theta}\_{c,t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−12​∂log⁡|𝑹t|∂fi,t+𝒚⋆t​∂𝜷t∂fi,t⊤−(d+ν)2​∂log⁡(ν+𝒚⋆t​𝑹t−1⊤​𝒚⋆t)∂fi,t+∂log⁡(α~t(d+ν)/2​K(d+ν)/2​(α~t))∂fi,t,\displaystyle=-\tfrac{1}{2}\frac{\partial\log|\bm{R}\_{t}|}{\partial f\_{i,t}}+\bm{y^{\star}}\_{t}{}^{\top}\frac{\partial\bm{\beta}\_{t}}{\partial f\_{i,t}}-\frac{(d+\nu)}{2}\frac{\partial\log\left(\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t}\right)}{\partial f\_{i,t}}+\frac{\partial\log\left(\tilde{\alpha}\_{t}^{(d+\nu)/2}\,K\_{(d+\nu)/2}\left(\tilde{\alpha}\_{t}\right)\right)}{\partial f\_{i,t}}, |  |

where αt=𝜸⊤​𝑹t−1​𝜸\alpha\_{t}=\sqrt{\bm{\gamma}^{\top}\bm{R}\_{t}^{-1}\bm{\gamma}}, 𝜷t=𝑹t−1​𝜸\bm{\beta}\_{t}=\bm{R}\_{t}^{-1}\bm{\gamma}, and α~t=αt⋅ν+𝒚⋆t​𝑹t−1⊤​𝒚⋆t\tilde{\alpha}\_{t}=\alpha\_{t}\cdot\sqrt{\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t}}.
Defining kν′​(x)=∂log⁡(xν​Kν​(x))/∂xk^{\prime}\_{\nu}(x)=\partial\log(x^{\nu}\,K\_{\nu}(x))/\partial x and ν~t=(d+ν)/(ν+𝒚⋆t​𝑹t−1⊤​𝒚⋆t)\tilde{\nu}\_{t}=(d+\nu)/(\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t}), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇i,t\displaystyle\nabla\_{i,t} | =−12​∂log⁡|𝑹t|∂fi,t+𝒚⋆t​∂𝑹t−1∂fi,t⊤​𝜸−12​d+νν+𝒚⋆t​𝑹t−1⊤​𝒚⋆t​𝒚⋆t​∂𝑹t−1∂fi,t⊤​𝒚⋆t+k(d+ν)/2′​(α~t)​∂α~t∂fi,t,\displaystyle=-\tfrac{1}{2}\frac{\partial\log|\bm{R}\_{t}|}{\partial f\_{i,t}}+\bm{y^{\star}}\_{t}{}^{\top}\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}\bm{\gamma}-\tfrac{1}{2}\ \frac{d+\nu}{\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t}}\bm{y^{\star}}\_{t}{}^{\top}\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}\bm{y^{\star}}\_{t}+k^{\prime}\_{(d+\nu)/2}\left(\tilde{\alpha}\_{t}\right)\frac{\partial\tilde{\alpha}\_{t}}{\partial f\_{i,t}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−12​∂log⁡|𝑹t|∂fi,t+𝒚⋆t​∂𝑹t−1∂fi,t⊤​𝜸−12​ν~t​𝒚⋆t​∂𝑹t−1∂fi,t⊤​𝒚⋆t+12​α~t​k(d+ν)/2′​(α~t)⋅(𝜸⊤​∂𝑹t−1∂fi,t​𝜸𝜸⊤​𝑹t−1​𝜸+𝒚⋆t​∂𝑹t−1∂fi,t⊤​𝒚⋆tν+𝒚⋆t​𝑹t−1⊤​𝒚⋆t).\displaystyle=-\tfrac{1}{2}\frac{\partial\log|\bm{R}\_{t}|}{\partial f\_{i,t}}+\bm{y^{\star}}\_{t}{}^{\top}\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}\bm{\gamma}-\tfrac{1}{2}\tilde{\nu}\_{t}\,\bm{y^{\star}}\_{t}{}^{\top}\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}\bm{y^{\star}}\_{t}+\tfrac{1}{2}\tilde{\alpha}\_{t}\,k^{\prime}\_{(d+\nu)/2}\left(\tilde{\alpha}\_{t}\right)\cdot\left(\frac{\bm{\gamma}^{\top}\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}\bm{\gamma}}{\bm{\gamma}^{\top}\bm{R}\_{t}^{-1}\bm{\gamma}}+\frac{\bm{y^{\star}}\_{t}{}^{\top}\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}\bm{y^{\star}}\_{t}}{\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t}}\right). |  |

Defining 𝚺t=𝑾​𝚲t​𝑾⊤\bm{\Sigma}\_{t}=\bm{W}\bm{\Lambda}\_{t}\bm{W}^{\top} and 𝚫𝚺t=diag⁡(𝚺t)\bm{\Delta}\_{\bm{\Sigma}\_{t}}=\operatorname{diag}(\bm{\Sigma}\_{t}) as a diagonal matrix holding the diagonal of 𝚺t\bm{\Sigma}\_{t}.
With fi,t=log⁡λi,tf\_{i,t}=\log\lambda\_{i,t}, the result now follows by noting that

|  |  |  |
| --- | --- | --- |
|  | 𝑹t−1=𝚫𝚺t1/2​𝑾​𝚲t−1​𝑾⊤​𝚫𝚺t1/2,\displaystyle\bm{R}\_{t}^{-1}=\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\ \bm{W}\bm{\Lambda}\_{t}^{-1}\bm{W}^{\top}\ \bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}, |  |
|  |  |  |
| --- | --- | --- |
|  | 𝑾​∂𝚲−1∂fi,t​𝑾⊤=−𝒘i​𝒘i⊤λi,t,\displaystyle\bm{W}\,\frac{\partial\bm{\Lambda}^{-1}}{\partial f\_{i,t}}\,\bm{W}^{\top}=-\,\frac{\bm{w}\_{i}\bm{w}\_{i}^{\top}}{\lambda\_{i,t}}, |  |
|  |  |  |
| --- | --- | --- |
|  | ∂Σj,j,t∂fi,t=∂∂fi,t​∑k=1dλk,t​wj,k2=λi,t​wj,i2,\displaystyle\frac{\partial\Sigma\_{j,j,t}}{\partial f\_{i,t}}=\frac{\partial}{\partial f\_{i,t}}\sum\_{k=1}^{d}\lambda\_{k,t}w\_{j,k}^{2}=\lambda\_{i,t}w\_{j,i}^{2}, |  |
|  |  |  |
| --- | --- | --- |
|  | ∂log⁡|𝑹t|∂fi,t=∂log⁡|𝚲t|∂fi,t−∂log⁡|𝚫𝚺t|∂fi,t=1−∑j=1d1Σj,j,t​∂Σj,j,t∂fi,t=1−λi,t​∑j=1dwj,i2Σj,j,t,\displaystyle\frac{\partial\log|\bm{R}\_{t}|}{\partial f\_{i,t}}=\frac{\partial\log|\bm{\Lambda}\_{t}|}{\partial f\_{i,t}}-\frac{\partial\log|\bm{\Delta}\_{\bm{\Sigma}\_{t}}|}{\partial f\_{i,t}}=1-\sum\_{j=1}^{d}\frac{1}{\Sigma\_{j,j,t}}\,\frac{\partial\Sigma\_{j,j,t}}{\partial f\_{i,t}}=1-\lambda\_{i,t}\sum\_{j=1}^{d}\frac{w\_{j,i}^{2}}{\Sigma\_{j,j,t}}, |  |
|  |  |  |
| --- | --- | --- |
|  | ∂𝑹t−1∂fi,t=−𝚫𝚺t1/2​𝒘i​𝒘i⊤λi,t​𝚫𝚺t1/2+𝚺˙i,t​𝑹t−1+𝑹t−1​𝚺˙i,t⊤,\displaystyle\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}=-\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\,\frac{\bm{w}\_{i}\bm{w}\_{i}^{\top}}{\lambda\_{i,t}}\,\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}+\dot{\bm{\Sigma}}\_{i,t}\,\bm{R}\_{t}^{-1}+\bm{R}\_{t}^{-1}\,\dot{\bm{\Sigma}}\_{i,t}^{\top}, |  |
|  |  |  |
| --- | --- | --- |
|  | 𝚺˙i,t=𝚺˙i,t⊤=∂𝚫𝚺t1/2∂fi,t𝚫𝚺t−1/2=12λi,tdiag(w1,i2Σ1,1,t,…,wd,i2Σd,d,t,).\displaystyle\dot{\bm{\Sigma}}\_{i,t}=\dot{\bm{\Sigma}}\_{i,t}^{\top}=\frac{\partial\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}}{\partial f\_{i,t}}\,\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{-1/2}=\tfrac{1}{2}\,\lambda\_{i,t}\,\operatorname{diag}\left(\frac{w\_{1,i}^{2}}{\Sigma\_{1,1,t}},\ldots,\frac{w\_{d,i}^{2}}{\Sigma\_{d,d,t}},\right). |  |

Since ∂Kν​(x)/∂x=−1/2​(Kν+1​(x)+Kν−1​(x))\partial K\_{\nu}(x)/\partial x=-1/2(K\_{\nu+1}(x)+K\_{\nu-1}(x)), all derivatives are determined analytically.
This proves the result.

#### Proof of Eq. ([A](https://arxiv.org/html/2601.13281v1#A1.Ex31 "Proof of Eq. () ‣ Appendix A Proofs ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"))

Define 𝒆i\bm{e}\_{i} as the iith column from the identity matrix, and 𝚫𝒘i\bm{\Delta}\_{\bm{w}\_{i}} as a diagonal matrix holding the iith eigenvector 𝒘i\bm{w}\_{i} from 𝑾\bm{W}.
Using the definitions

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚~t⋆\displaystyle\tilde{\bm{y}}^{\star}\_{t} | =𝑾⊤​𝚫𝚺t1/2​𝒚⋆t,𝜸~t=𝑾⊤​𝚫𝚺t1/2​𝜸,𝒚¯i,t⋆=𝑾⊤​𝚫𝚺t1/2​𝚺˙i,t​𝒚⋆t,𝜸¯i,t=𝑾⊤​𝚫𝚺t1/2​𝚺˙i,t​𝜸,\displaystyle=\bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{y^{\star}}\_{t},\qquad\tilde{\bm{\gamma}}\_{t}=\bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{\gamma},\qquad\bar{\bm{y}}^{\star}\_{i,t}=\bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\dot{\bm{\Sigma}}\_{i,t}\bm{y^{\star}}\_{t},\qquad\bar{\bm{\gamma}}\_{i,t}=\bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\dot{\bm{\Sigma}}\_{i,t}\bm{\gamma}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | αt\displaystyle\alpha\_{t} | =𝜸⊤​𝑹t−1​𝜸=𝜸⊤​𝚫𝚺t1/2​𝑾​𝚲t−1​𝑾⊤​𝚫𝚺t1/2​𝜸=𝜸~t⊤​𝚲t−1​𝜸~t,\displaystyle=\sqrt{\bm{\gamma}^{\top}\bm{R}\_{t}^{-1}\bm{\gamma}}=\sqrt{\bm{\gamma}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{W}\bm{\Lambda}\_{t}^{-1}\bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{\gamma}}=\sqrt{\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{\gamma}}\_{t}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | α~t\displaystyle\tilde{\alpha}\_{t} | =αt⋅ν+𝒚⋆t​𝑹t−1⊤​𝒚⋆t=αt⋅ν+𝒚⋆t​𝚫𝚺t1/2⊤​𝑾​𝚲t−1​𝑾⊤​𝚫𝚺t1/2​𝒚⋆t=αt⋅ν+𝒚~t⋆​𝚲t−1⊤​𝒚~t⋆,\displaystyle=\alpha\_{t}\cdot\sqrt{\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t}}=\alpha\_{t}\cdot\sqrt{\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{W}\bm{\Lambda}\_{t}^{-1}\bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{y^{\star}}\_{t}}=\alpha\_{t}\cdot\sqrt{\nu+\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ν~t\displaystyle\tilde{\nu}\_{t} | =(ν+d)/(ν+𝒚⋆t​𝑹t−1⊤​𝒚⋆t)=(ν+d)/(ν+𝒚~t⋆​𝚲t−1⊤​𝒚~t⋆),\displaystyle=(\nu+d)/(\nu+\bm{y^{\star}}\_{t}{}^{\top}\bm{R}\_{t}^{-1}\bm{y^{\star}}\_{t})=(\nu+d)/(\nu+\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺~i,t\displaystyle\tilde{\bm{\Sigma}}\_{i,t} | =𝚺˙i,t​𝑹t−1+𝑹t−1​𝚺˙i,t,𝚺˙i,t=12​λi,t​𝚫𝚺t−1​𝚫𝒘i2,\displaystyle=\dot{\bm{\Sigma}}\_{i,t}\bm{R}\_{t}^{-1}+\bm{R}\_{t}^{-1}\dot{\bm{\Sigma}}\_{i,t},\qquad\dot{\bm{\Sigma}}\_{i,t}=\tfrac{1}{2}\,\lambda\_{i,t}\,\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{-1}\bm{\Delta}\_{\bm{w}\_{i}}^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂𝑹t−1∂fi,t\displaystyle\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}} | =−λi,t−1​𝚫𝚺t1/2​𝑾​𝒆i​𝒆i⊤​𝑾⊤​𝚫𝚺t1/2+𝚺~i,t,\displaystyle=-\lambda\_{i,t}^{-1}\,\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{W}\bm{e}\_{i}\bm{e}\_{i}^{\top}\bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}+\tilde{\bm{\Sigma}}\_{i,t}, |  |

we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜸⊤​𝚺~i,t​𝜸\displaystyle\bm{\gamma}^{\top}\tilde{\bm{\Sigma}}\_{i,t}\bm{\gamma} | =𝜸⊤​𝚺˙i,t​𝚫𝚺t1/2​𝑾​𝚲t−1​𝑾⊤​𝚫𝚺t1/2​𝜸+𝜸⊤​𝚫𝚺t1/2​𝑾​𝚲t−1​𝑾⊤​𝚫𝚺t1/2​𝚺˙i,t​𝜸\displaystyle=\bm{\gamma}^{\top}\dot{\bm{\Sigma}}\_{i,t}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{W}\ \bm{\Lambda}\_{t}^{-1}\ \bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{\gamma}+\bm{\gamma}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{W}\ \bm{\Lambda}\_{t}^{-1}\ \bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\dot{\bm{\Sigma}}\_{i,t}\bm{\gamma} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝜸¯i,t⊤​𝚲t−1​𝜸~t+𝜸~t⊤​𝚲t−1​𝜸¯i,t=2​𝜸~t⊤​𝚲t−1​𝜸¯i,t,\displaystyle=\bar{\bm{\gamma}}\_{i,t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{\gamma}}\_{t}+\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{\gamma}}\_{i,t}=2\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{\gamma}}\_{i,t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜸⊤​𝚺~i,t​𝒚⋆t\displaystyle\bm{\gamma}^{\top}\tilde{\bm{\Sigma}}\_{i,t}\bm{y^{\star}}\_{t} | =𝜸⊤​𝚺˙i,t​𝚫𝚺t1/2​𝑾​𝚲t−1​𝑾⊤​𝚫𝚺t1/2​𝒚⋆t+𝜸⊤​𝚫𝚺t1/2​𝑾​𝚲t−1​𝑾⊤​𝚫𝚺t1/2​𝚺˙i,t​𝒚⋆t\displaystyle=\bm{\gamma}^{\top}\dot{\bm{\Sigma}}\_{i,t}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{W}\ \bm{\Lambda}\_{t}^{-1}\ \bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{y^{\star}}\_{t}+\bm{\gamma}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{W}\ \bm{\Lambda}\_{t}^{-1}\ \bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\dot{\bm{\Sigma}}\_{i,t}\bm{y^{\star}}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝜸¯i,t⊤​𝚲t−1​𝒚~t⋆+𝜸~t⊤​𝚲t−1​𝒚¯i,t⋆,\displaystyle=\bar{\bm{\gamma}}\_{i,t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}+\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{y}}^{\star}\_{i,t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚⋆t​𝚺~i,t⊤​𝒚⋆t\displaystyle\bm{y^{\star}}\_{t}{}^{\top}\tilde{\bm{\Sigma}}\_{i,t}\bm{y^{\star}}\_{t} | =𝒚⋆t​𝚺˙i,t⊤​𝚫𝚺t1/2​𝑾​𝚲t−1​𝑾⊤​𝚫𝚺t1/2​𝒚⋆t+𝒚⋆t​𝚫𝚺t1/2⊤​𝑾​𝚲t−1​𝑾⊤​𝚫𝚺t1/2​𝚺˙i,t​𝒚⋆t\displaystyle=\bm{y^{\star}}\_{t}{}^{\top}\dot{\bm{\Sigma}}\_{i,t}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{W}\ \bm{\Lambda}\_{t}^{-1}\ \bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{y^{\star}}\_{t}+\bm{y^{\star}}\_{t}{}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\bm{W}\ \bm{\Lambda}\_{t}^{-1}\ \bm{W}^{\top}\bm{\Delta}\_{\bm{\Sigma}\_{t}}^{1/2}\dot{\bm{\Sigma}}\_{i,t}\bm{y^{\star}}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝒚¯i,t⋆​𝚲t−1⊤​𝒚~t⋆+𝒚~t⋆​𝚲t−1⊤​𝒚¯i,t⋆=2​𝒚¯i,t⋆​𝚲t−1⊤​𝒚~t⋆,\displaystyle=\bar{\bm{y}}^{\star}\_{i,t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}+\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{y}}^{\star}\_{i,t}=2\bar{\bm{y}}^{\star}\_{i,t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜸⊤​∂𝑹t−1∂fi,t​𝜸\displaystyle\bm{\gamma}^{\top}\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}\bm{\gamma} | =−λi,t−1​𝜸~t⊤​𝒆i​𝒆i⊤​𝜸~t+𝜸⊤​𝚺~i,t​𝜸=−γ~i,t2λi,t+2​𝜸~t⊤​𝚲t−1​𝜸¯i,t,\displaystyle=-\lambda\_{i,t}^{-1}\,\tilde{\bm{\gamma}}\_{t}^{\top}\bm{e}\_{i}\bm{e}\_{i}^{\top}\tilde{\bm{\gamma}}\_{t}+\bm{\gamma}^{\top}\tilde{\bm{\Sigma}}\_{i,t}\bm{\gamma}=-\,\frac{\tilde{\gamma}\_{i,t}^{2}}{\lambda\_{i,t}}+2\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{\gamma}}\_{i,t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜸⊤​∂𝑹t−1∂fi,t​𝒚⋆t\displaystyle\bm{\gamma}^{\top}\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}\bm{y^{\star}}\_{t} | =−λi,t−1​𝜸~t⊤​𝒆i​𝒆i⊤​𝒚~t⋆+𝜸⊤​𝚺~i,t​𝒚⋆t=−γ~i,t​y~i,t⋆λi,t+𝜸¯i,t⊤​𝚲t−1​𝒚~t⋆+𝜸~t⊤​𝚲t−1​𝒚¯i,t⋆,\displaystyle=-\lambda\_{i,t}^{-1}\,\tilde{\bm{\gamma}}\_{t}^{\top}\bm{e}\_{i}\bm{e}\_{i}^{\top}\tilde{\bm{y}}^{\star}\_{t}+\bm{\gamma}^{\top}\tilde{\bm{\Sigma}}\_{i,t}\bm{y^{\star}}\_{t}=-\,\frac{\tilde{\gamma}\_{i,t}\tilde{y}^{\star}\_{i,t}}{\lambda\_{i,t}}+\bar{\bm{\gamma}}\_{i,t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}+\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{y}}^{\star}\_{i,t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒚⋆t​∂𝑹t−1∂fi,t⊤​𝒚⋆t\displaystyle\bm{y^{\star}}\_{t}{}^{\top}\frac{\partial\bm{R}\_{t}^{-1}}{\partial f\_{i,t}}\bm{y^{\star}}\_{t} | =−λi,t−1​𝒚~t⋆​𝒆i⊤​𝒆i⊤​𝒚~t⋆+𝒚⋆t​𝚺~i,t⊤​𝒚⋆t=−y~i,t⋆2λi,t+2​𝒚~t⋆​𝚲t−1⊤​𝒚¯i,t⋆.\displaystyle=-\lambda\_{i,t}^{-1}\,\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{e}\_{i}\bm{e}\_{i}^{\top}\tilde{\bm{y}}^{\star}\_{t}+\bm{y^{\star}}\_{t}{}^{\top}\tilde{\bm{\Sigma}}\_{i,t}\bm{y^{\star}}\_{t}=-\,\frac{\tilde{y}^{\star}\_{i,t}{}^{2}}{\lambda\_{i,t}}+2\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{y}}^{\star}\_{i,t}. |  |

We can now rewrite ([6](https://arxiv.org/html/2601.13281v1#S2.E6 "In Proposition 1 (score equations for spectral dynamics). ‣ 2.2 Spectral dynamics ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇i,t\displaystyle\nabla\_{i,t} | =(−12+12​λi,t​∑j=1dwj,i2Σj,j,t)+(−γ~i,t​y~i,t⋆λi,t+𝜸⊤​𝚺~i,t​𝒚⋆t)+(12​ν~t​y~i,t⋆2λi,t−12​ν~t​𝒚⋆t​𝚺~i,t⊤​𝒚⋆t)\displaystyle=\left(-\tfrac{1}{2}+\tfrac{1}{2}\lambda\_{i,t}\sum\_{j=1}^{d}\frac{w\_{j,i}^{2}}{\Sigma\_{j,j,t}}\right)+\left(-\,\frac{\tilde{\gamma}\_{i,t}\tilde{y}^{\star}\_{i,t}}{\lambda\_{i,t}}+\bm{\gamma}^{\top}\tilde{\bm{\Sigma}}\_{i,t}\bm{y^{\star}}\_{t}\right)+\left(\tfrac{1}{2}\,\tilde{\nu}\_{t}\,\frac{\tilde{y}^{\star}\_{i,t}{}^{2}}{\lambda\_{i,t}}-\tfrac{1}{2}\,\tilde{\nu}\_{t}\,\bm{y^{\star}}\_{t}{}^{\top}\tilde{\bm{\Sigma}}\_{i,t}\bm{y^{\star}}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12​α~t⋅k(ν+d)/2′​(α~t)⋅(γ~i,t2/λi,t𝜸~t⊤​𝚲t−1​𝜸~t+y~i,t⋆/2λi,tν+𝒚~t⋆​𝚲t−1⊤​𝒚~t⋆)\displaystyle\qquad-\tfrac{1}{2}\,\tilde{\alpha}\_{t}\cdot k^{\prime}\_{(\nu+d)/2}\left(\tilde{\alpha}\_{t}\right)\cdot\left(\frac{\tilde{\gamma}\_{i,t}^{2}/\lambda\_{i,t}}{\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{\gamma}}\_{t}}+\frac{\tilde{y}^{\star}\_{i,t}{}^{2}/\lambda\_{i,t}}{\nu+\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​α~t⋅k(ν+d)/2′​(α~t)⋅(𝜸⊤​𝚺~i,t​𝜸𝜸~t⊤​𝚲t−1​𝜸~t+𝒚⋆t​𝚺~i,t⊤​𝒚⋆tν+𝒚~t⋆​𝚲t−1⊤​𝒚~t⋆)\displaystyle\qquad+\tfrac{1}{2}\,\tilde{\alpha}\_{t}\cdot k^{\prime}\_{(\nu+d)/2}\left(\tilde{\alpha}\_{t}\right)\cdot\left(\frac{\bm{\gamma}^{\top}\tilde{\bm{\Sigma}}\_{i,t}\bm{\gamma}}{\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{\gamma}}\_{t}}+\frac{\bm{y^{\star}}\_{t}{}^{\top}\tilde{\bm{\Sigma}}\_{i,t}\bm{y^{\star}}\_{t}}{\nu+\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​(ν~t​y~i,t⋆2λi,t−1−2​γ~i,t​y~i,t⋆λi,t)−12​α~t⋅k(ν+d)/2′​(α~t)⋅(γ~i,t2/λi,t𝜸~t⊤​𝚲t−1​𝜸~t+y~i,t⋆/2λi,tν+𝒚~t⋆​𝚲t−1⊤​𝒚~t⋆)\displaystyle=\tfrac{1}{2}\,\left(\tilde{\nu}\_{t}\,\frac{\tilde{y}^{\star}\_{i,t}{}^{2}}{\lambda\_{i,t}}-1-2\frac{\tilde{\gamma}\_{i,t}\tilde{y}^{\star}\_{i,t}}{\lambda\_{i,t}}\right)-\tfrac{1}{2}\,\tilde{\alpha}\_{t}\cdot k^{\prime}\_{(\nu+d)/2}\left(\tilde{\alpha}\_{t}\right)\cdot\left(\frac{\tilde{\gamma}\_{i,t}^{2}/\lambda\_{i,t}}{\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{\gamma}}\_{t}}+\frac{\tilde{y}^{\star}\_{i,t}{}^{2}/\lambda\_{i,t}}{\nu+\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(ν~t​𝒚~t⋆​𝚲t−1⊤​𝒚¯i,t⋆−trace⁡(𝚺˙i,t)−𝜸~t​𝚲t−1⊤​𝒚¯i,t⋆−𝜸¯i,t⊤​𝚲t−1​𝒚~t⋆)\displaystyle\qquad-\,\left(\tilde{\nu}\_{t}\,\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{y}}^{\star}\_{i,t}-\operatorname{trace}(\dot{\bm{\Sigma}}\_{i,t})-\tilde{\bm{\gamma}}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{y}}^{\star}\_{i,t}-\bar{\bm{\gamma}}\_{i,t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +α~t⋅k(ν+d)/2′​(α~t)⋅(𝜸~t⊤​𝚲t−1​𝜸¯i,t𝜸~t⊤​𝚲t−1​𝜸~t+𝒚~t⋆​𝚲t−1⊤​𝒚¯i,t⋆ν+𝒚~t⋆​𝚲t−1⊤​𝒚~t⋆).\displaystyle\qquad+\tilde{\alpha}\_{t}\cdot k^{\prime}\_{(\nu+d)/2}\left(\tilde{\alpha}\_{t}\right)\cdot\left(\frac{\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{\gamma}}\_{i,t}}{\tilde{\bm{\gamma}}\_{t}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{\gamma}}\_{t}}+\frac{\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\bar{\bm{y}}^{\star}\_{i,t}}{\nu+\tilde{\bm{y}}^{\star}\_{t}{}^{\top}\bm{\Lambda}\_{t}^{-1}\tilde{\bm{y}}^{\star}\_{t}}\right). |  |

This proves the result.

## Appendix B Supplementary material simulation study

### B.1 Reference model

As a reference model in our simulation and empirical studies, we use the dynamic factor copula model, which was introduced by Opschoor et al. [[2021](https://arxiv.org/html/2601.13281v1#bib.bib41 "Closed-form multi-factor copula models with observation-driven dynamic factor loadings")] and refined by Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")]. The factor loadings are normalized as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝀~i,t=𝝀i,t1+𝝀i,t′​𝝀i,t,σi,t2=𝝀i,t1+𝝀i,t′​𝝀i,t\tilde{\bm{\lambda}}\_{i,t}=\frac{\bm{\lambda}\_{i,t}}{\sqrt{1+\bm{\lambda}^{\prime}\_{i,t}\bm{\lambda}\_{i,t}}},\quad\sigma^{2}\_{i,t}=\frac{\bm{\lambda}\_{i,t}}{\sqrt{1+\bm{\lambda}^{\prime}\_{i,t}\bm{\lambda}\_{i,t}}} |  | (B.1) |

The copula correlation matrix is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑹t=𝑳~t​𝑳~t+𝑫t\bm{R}\_{t}=\tilde{\bm{L}}\_{t}\tilde{\bm{L}}\_{t}+\bm{D}\_{t} |  | (B.2) |

Here, we have that 𝑳~t=[𝝀~1,t,…,𝝀~d,t]\tilde{\bm{L}}\_{t}=[\tilde{\bm{\lambda}}\_{1,t},...,\tilde{\bm{\lambda}}\_{d,t}] and 𝑫t=diag​(σ1,t2,…,σd,t2)\bm{D}\_{t}={\rm diag}(\sigma^{2}\_{1,t},...,\sigma^{2}\_{d,t}).

In particular, we use the following multi-factor structure considered by Opschoor et al. [[2021](https://arxiv.org/html/2601.13281v1#bib.bib41 "Closed-form multi-factor copula models with observation-driven dynamic factor loadings")] and Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")] with 2​nG2n\_{G} factor loadings.
Suppose there are nG=25n\_{G}=25 groups with 4 assets per group. The matrix 𝑳~t\tilde{\bm{L}}\_{t} is then generated by the following tensor product of a matrix with a vector:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑳~t=(λ~1,tMλ~1,tC0…0λ~2,tM0λ~2,tC…0……………λ~nG,tM00…λ~nG,tC)⊗(1111)\tilde{\bm{L}}\_{t}=\begin{pmatrix}\tilde{\lambda}^{M}\_{1,t}&\tilde{\lambda}^{C}\_{1,t}&0&...&0\\ \tilde{\lambda}^{M}\_{2,t}&0&\tilde{\lambda}^{C}\_{2,t}&...&0\\ ...&...&...&...&...\\ \tilde{\lambda}^{M}\_{n\_{G},t}&0&0&...&\tilde{\lambda}^{C}\_{n\_{G},t}\\ \end{pmatrix}\otimes\begin{pmatrix}1\\ 1\\ 1\\ 1\end{pmatrix} |  | (B.3) |

Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")] have developed a method to optimally group stocks into clusters. We use their algorithm to determine the optimal number of clusters and the optimal assignment of indices.

The dynamics of the reference model is given by [Oh and Patton, [2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λg,t+1M\displaystyle\lambda^{M}\_{g,t+1} | =\displaystyle= | ωgM+αM​∂log⁡c​(𝒖𝒕;𝑹t,ν,𝜸)∂λg,tM+βM​λg,tM,\displaystyle\omega^{M}\_{g}+\alpha^{M}\frac{\partial\log c(\bm{u\_{t}};\bm{R}\_{t},\nu,\bm{\gamma})}{\partial\lambda^{M}\_{g,t}}+\beta^{M}\lambda^{M}\_{g,t}, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | λg,t+1C\displaystyle\lambda^{C}\_{g,t+1} | =\displaystyle= | ωgC+αC​∂log⁡c​(𝒖𝒕;𝑹t,ν,𝜸)∂λg,tC+βC​λg,tC.\displaystyle\omega^{C}\_{g}+\alpha^{C}\frac{\partial\log c(\bm{u\_{t}};\bm{R}\_{t},\nu,\bm{\gamma})}{\partial\lambda^{C}\_{g,t}}+\beta^{C}\lambda^{C}\_{g,t}. |  | (B.4) |

We estimate the model by Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")] on our data set using their code. The parameter estimation results are shown in Table [C.2](https://arxiv.org/html/2601.13281v1#A3.T2 "Table C.2 ‣ Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").

### B.2 Experiment: mis-specification

We perform an additional simulation experiment to show that the skew tt copula with score-driven eigenvalues can recover general patterns over time, even if the model is mis-specified; see Figure [B.1](https://arxiv.org/html/2601.13281v1#A2.F1 "Figure B.1 ‣ B.2 Experiment: mis-specification ‣ Appendix B Supplementary material simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
In the experiment, we used the same model parameters as in Section [3.2](https://arxiv.org/html/2601.13281v1#S3.SS2 "3.2 Experiment 2: quality of point and path estimates ‣ 3 Simulation study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), but now the true dynamics are given by periodic patterns over time: λ1,t=λ1​(1+sin⁡(4​π​t/T)/2)\lambda\_{1,t}=\lambda\_{1}(1+\sin(4\pi t/T)/2) and λ2,t=λ2​(1+cos⁡(4​π​t/T)/2)\lambda\_{2,t}=\lambda\_{2}(1+\cos(4\pi t/T)/2).
We estimate the model using regularized spectral score-driven dynamics with Eq. ([12](https://arxiv.org/html/2601.13281v1#S2.E12 "In 2.4 Parameter estimation ‣ 2 The model ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas")).
We find that the model recovers the true dynamics of the eigenvalues well, even though the model was not informed about the periodic specification.

![Refer to caption](x6.png)


Figure B.1: Dynamics of first and second eigenvalue, where the true dynamics of the dgp are based on a prespecified periodic pattern, while the estimated model is based on GAS. The true dynamics are compared to the predicted dynamics from the estimated model. The period after 4 years is an out-of-sample forecast.

## Appendix C Supplementary material empirical study

In Table [C.1](https://arxiv.org/html/2601.13281v1#A3.T1 "Table C.1 ‣ Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas"), we list 100 stocks based on 10 countries and 10 sectors.
These stocks are used in the empirical analyses.
In a few cases, there was no stock available for the country-sector combination based on the requirement of a full data history.
Consequently, other country-sector combinations have been selected twice.
In total, each country and each sector occurs precisely 10 times in the data set.

Table C.1:  RIC codes of 100 stocks that are included in the empirical study. The first column shows the two-letter country code, while the first row and the middle row show the industry sector.

|  | Financials | Industrials | Basic | Consumer | Utilities |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Materials | Non- Cyclicals |  |
| DE | ALVG | SIEG | BASF | BEIG | EONG |
| FR | AXAF | SCHN | AIRP | OREP | ENGIE |
| UK | HSBA | RR | RIO | ULVR | NG |
| ES | SAN | ACS | VID | EBRO | IBE,  ELE |
| IT | CRDI | LDOF | BZU | CPRI | ENEI,  TRN |
| SW | INVE | ATCO | SAND | LIFCO |  |
| NO | DNB | KOG | NHY | ORK | SCATC |
| NL | INGA | WLSN | AKZO | HEIN |  |
| BE | KBC | ACKB | UMI | ABI | ELI |
| CH | UBSG | ABBN | HOLN | NESN | BKWB |
|  | Consumer | Technology | Health Care | Energy | Real Estate |
|  | Cyclicals |  |  |  |  |
| DE | BMWG | SAPG | MRCG | PNEG | VNA |
| FR | LVMH | ORAN | ESLX | TTEF | LOIM |
| UK | CPG | RELNG | AZN | SHEL | SGRO |
| ES | ITX | AMA |  | REP | MRL |
| IT | MONC | TLIT | RECI | ENI |  |
| SW | ASSA,  HM | HEXA | SOBIV,  SECT |  | SAGA |
| NO | VENDA | TEL |  | EQNR,  AKRBP | OLT |
| NL |  | ASML | PHG | VOPA,  SBMO | ECMPA,  WEHA |
| BE | IETB | MLXS | UCB | CMBT | WDPP |
| CH | CFR | SCMN | NOVN,  RO |  | SPSN |

Table [C.2](https://arxiv.org/html/2601.13281v1#A3.T2 "Table C.2 ‣ Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") shows the estimated parameters for the static skew tt copula with estimated cluster assignments for empirical study in 100 dimensions.

Table C.2:  Parameter estimation of the static skew tt copula for empirical study with 100 stocks using optimal cluster assignments.

| Par | Est |  | Par | Est |  | Par | Est |  | Par | Est |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ω1M\omega^{M}\_{1} | 0.99 |  | ω10M\omega^{M}\_{10} | 1.23 |  | ω1C\omega^{C}\_{1} | 0.002 |  | ω10C\omega^{C}\_{10} | 0.26 |
| ω2M\omega^{M}\_{2} | 1.26 |  | ω11M\omega^{M}\_{11} | 0.29 |  | ω2C\omega^{C}\_{2} | 0.53 |  | ω11C\omega^{C}\_{11} | 0.20 |
| ω3M\omega^{M}\_{3} | 0.721 |  | ω12M\omega^{M}\_{12} | 0.87 |  | ω3C\omega^{C}\_{3} | 0.68 |  | ω12C\omega^{C}\_{12} | 0.78 |
| ω4M\omega^{M}\_{4} | 0.84 |  | ω13M\omega^{M}\_{13} | 0.65 |  | ω4C\omega^{C}\_{4} | 0.26 |  | ω13C\omega^{C}\_{13} | 0.32 |
| ω5M\omega^{M}\_{5} | 0.52 |  | ω14M\omega^{M}\_{14} | 0.88 |  | ω5C\omega^{C}\_{5} | 0.21 |  | ω14C\omega^{C}\_{14} | 0.90 |
| ω6M\omega^{M}\_{6} | 0.67 |  | ω15M\omega^{M}\_{15} | 0.72 |  | ω6C\omega^{C}\_{6} | 0.004 |  | ω15C\omega^{C}\_{15} | 0.47 |
| ω7M\omega^{M}\_{7} | 1.21 |  | ω16M\omega^{M}\_{16} | 0.41 |  | ω7C\omega^{C}\_{7} | 0.87 |  | ω16C\omega^{C}\_{16} | 0.28 |
| ω8M\omega^{M}\_{8} | 0.73 |  | ω17M\omega^{M}\_{17} | 0.77 |  | ω8C\omega^{C}\_{8} | 0.52 |  | ω17C\omega^{C}\_{17} | 0.52 |
| ω9M\omega^{M}\_{9} | 0.80 |  | ν\nu | 33.9 |  | ω9C\omega^{C}\_{9} | 0.59 |  | γ\gamma | -0.23 |

Finally, Figure [1(b)](https://arxiv.org/html/2601.13281v1#A3.F1.sf2 "In Figure C.1 ‣ Appendix C Supplementary material empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas") compares the loadings of the cluster-based factor copula of Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")] versus the elements of the first and second spectral eigenvector.

![Refer to caption](ev1vsomegaM.png)


(a) ωM\omega\_{M} versus first spectral eigenvector w^i,1\hat{w}\_{i,1}

![Refer to caption](ev2vsomegaC.png)


(b) ωC\omega\_{C} versus first spectral eigenvector w^i,2\hat{w}\_{i,2}

Figure C.1: Loadings of the cluster-based factor copula of Oh and Patton [[2023](https://arxiv.org/html/2601.13281v1#bib.bib40 "Dynamic factor copula models with estimated cluster assignments")] versus the elements of the first and second spectral eigenvectors. Elements are grouped by cluster number 1…17, which is the BIC optimal number of clusters. Each dot corresponds to an single stock, and the colors correspond to the average value of the loadings as in Figure [4](https://arxiv.org/html/2601.13281v1#S4.F4 "Figure 4 ‣ 4.3 Eigenvalues and eigenvectors ‣ 4 Empirical study ‣ Spectral Dynamics and Regularization for High-Dimensional Copulas").
The loadings of the first eigenvector of the spectral copula and the loadings of the first factor in the factor copula almost linearly relate.
The magnitudes of the second eigenvector elements of the spectral approach and those of the individual clusters of the factor copula group factors, also clearly relate, where differences in signs can be captured by the signs of the different group factors in the factor copula approach. Note that all second eigenvector elements in the spectral approach are weighted by λˇ2,t\check{\lambda}\_{2,t}, such that sign differences must be reflected in the eigenvector elements themselves.