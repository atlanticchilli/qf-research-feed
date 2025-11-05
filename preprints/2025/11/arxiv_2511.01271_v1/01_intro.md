---
authors:
- Zhaoxing Gao
- Sihan Tu
- Ruey S. Tsay
doc_id: arxiv:2511.01271v1
family_id: arxiv:2511.01271
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions
url_abs: http://arxiv.org/abs/2511.01271v1
url_html: https://arxiv.org/html/2511.01271v1
venue: arXiv q-fin
version: 1
year: 2025
---

This paper investigates
estimation and inference of a Spatial Arbitrage Pricing Theory (SAPT) model that integrates spatial interactions with multi-factor analysis, accommodating both observable and latent factors.
Building on the classical mean-variance analysis, we
introduce a class of Spatial Capital Asset Pricing Models (SCAPM) that account for spatial effects in high-dimensional assets, where we define spatial rho as a counterpart to market beta in CAPM. We then extend SCAPM to a general SAPT framework under a complete market setting by incorporating multiple factors.
For SAPT with observable factors, we propose a generalized shrinkage Yule-Walker (SYW) estimation method that integrates ridge regression to estimate spatial and factor coefficients. When factors are latent, we first apply an autocovariance-based eigenanalysis to extract factors,
then employ the SYW
method using the estimated factors. We establish asymptotic properties for these estimators under high-dimensional settings where both the dimension and sample size diverge.
Finally, we use simulated and real data examples to demonstrate
the efficacy and usefulness of the proposed model and method.

Keywords: Spatial Arbitrage Pricing Theory, Multi-factor Analysis, Yule-Walker Estimation, Eigenanalysis, High Dimension

## 1 Introduction

With the rapid advancement in information technology, large-scale datasets have become ubiquitous across
all scientific areas with important applications. These datasets also introduce new analytical challenges in financial econometrics and statistics, particularly in high-dimensional settings.
As a fundamental tool for dimension reduction and feature extraction, factor models
provide a crucial link between economic theory and data analysis.
Since the seminal work of Markowitz ([1952](https://arxiv.org/html/2511.01271v1#bib.bib38)) on portfolio theory, factor-based pricing models have played a central role in asset pricing, investment analysis and risk assessment. The Capital Asset Pricing Model (CAPM), developed by Sharpe, Lintner, and Mossin in the 1960s, introduced the concept of market beta to quantify systematic risk-return relationships. Ross ([1976](https://arxiv.org/html/2511.01271v1#bib.bib43)) proposed the Arbitrage Pricing Theory (APT), which extended the single-factor CAPM by incorporating multiple systematic risk factors under no-arbitrage principles, allowing for a more flexible representation of expected returns.
Modern factor-based pricing research has evolved into two dominant approaches to address
the growing market complexity. The first approach, developed by Fama and French ([1993](https://arxiv.org/html/2511.01271v1#bib.bib13), [2015](https://arxiv.org/html/2511.01271v1#bib.bib14)), relies on the theory-driven observable factors, such as market returns and firm characteristics. Building on this framework, numerous factor models for asset returns have been proposed; for instance, Feng et al. ([2020](https://arxiv.org/html/2511.01271v1#bib.bib17)) propose the Double-Selection LASSO to evaluate the marginal contribution of individual factors relative to an existing high-dimensional factor set.
While these models offer strong economic interpretability, their fixed factor structures limit their ability to capture modern dynamic market interactions.
Recent studies by Forni et al. ([2000](https://arxiv.org/html/2511.01271v1#bib.bib18)), Bai and Ng ([2002](https://arxiv.org/html/2511.01271v1#bib.bib7)), Bai ([2003](https://arxiv.org/html/2511.01271v1#bib.bib5)), Forni et al. ([2005](https://arxiv.org/html/2511.01271v1#bib.bib19)), Lam and Yao ([2012](https://arxiv.org/html/2511.01271v1#bib.bib30)), Fan et al. ([2013](https://arxiv.org/html/2511.01271v1#bib.bib15)), Gao and Tsay ([2022](https://arxiv.org/html/2511.01271v1#bib.bib23), [2023](https://arxiv.org/html/2511.01271v1#bib.bib24)), among others, have focused on latent factor models as an alternative approach. These models provide a methodology for inferring unobserved common factors from covariance structures. Lettau and Pelger ([2020](https://arxiv.org/html/2511.01271v1#bib.bib34)) and Giglio et al. ([2025](https://arxiv.org/html/2511.01271v1#bib.bib26)) further demonstrate the effectiveness of their tailored latent factor models in asset pricing, offering deeper insights into the underlying structure of financial markets. Liu et al. ([2025](https://arxiv.org/html/2511.01271v1#bib.bib37))
show that one can improve the
estimation of portfolio risk by augmenting the Fama and French factors with latent factors extracted from
a matrix-variate dataset of asset returns.

Despite the effectiveness of factor models in explaining cross-sectional and dynamic dependence, many economic and financial applications often manifest intricate spatial interconnections. Consider, for example, the spatial distribution of economic indicators across regions, where the performance of one region may influence its neighbors; see Anselin ([1988](https://arxiv.org/html/2511.01271v1#bib.bib3)) and Cressie ([2015](https://arxiv.org/html/2511.01271v1#bib.bib12)). Since the seminal work of Cliff and Ord ([1973](https://arxiv.org/html/2511.01271v1#bib.bib10)) on spatial autocorrelations, spatial models are often used to model cross-sectional dependence of different economic units or individuals at different locations.
More recently, the spatial models have been extended to spatial dynamic panel data (SDPD) models by adding a time-lagged direction to account for serial correlations across different economic units or individuals; see, for example, Lee and Yu ([2010](https://arxiv.org/html/2511.01271v1#bib.bib33)). Empirically, the spatial interactions among the panel may exist in many large-dimensional economic and financial systems, together with other comovements or common factors. For example, Pirinsky and Wang ([2006](https://arxiv.org/html/2511.01271v1#bib.bib42)) found the spatial effect in the U.S. equity market by studying the comovements of common stock returns of U.S. corporations in the same geographic area; Kou et al. ([2018](https://arxiv.org/html/2511.01271v1#bib.bib29)) proposed an asset pricing model with spatial interactions and discovered significant spatial interactions in the futures contracts on S&P/Case-Shiller Home Price Indices. Therefore, augmenting factor models with spatial interactions not only extends these models with additional common factors but also enriches spatio-temporal models by integrating common factor structures.

In this paper, we focus on spatial panel models with common factors in the context of arbitrage pricing under high-dimensional settings. Building on the classical mean-variance analysis, we first introduce a class of Spatial Capital Asset Pricing Models (SCAPM) that account for spatial effects in high-dimensional assets under a “complete market” or “minimum complete market” assumption, where we introduce a spatial rho as a counterpart to market beta in CAPM.
Within the spatial CAPM framework, we extend the model to a Spatial Arbitrage Pricing Theory (SAPT) by incorporating a multifactor structure. This formulation captures both systematic risk factors and spatial spillover effects, offering a unified approach to modeling interdependencies in asset returns.

While prior studies, such as Pesaran and Tosetti ([2011](https://arxiv.org/html/2511.01271v1#bib.bib41)), Kou et al. ([2018](https://arxiv.org/html/2511.01271v1#bib.bib29)), Bai and Li ([2021](https://arxiv.org/html/2511.01271v1#bib.bib6)), Yang ([2021](https://arxiv.org/html/2511.01271v1#bib.bib48)), and Hu et al. ([2023](https://arxiv.org/html/2511.01271v1#bib.bib28)), have examined similar spatial interactions in factor models, the SAPT studied in this paper differs from the existing models for several reasons.
First, unlike Pesaran and Tosetti ([2011](https://arxiv.org/html/2511.01271v1#bib.bib41)), which focuses on spatial autocorrelation in unobserved errors, our model explicitly captures spatial correlations among panel units. Second, the proposed SAPT model functions as a pure spatial arbitrage pricing factor model without lagged or exogenous variables, distinguishing it from the models in Bai and Li ([2021](https://arxiv.org/html/2511.01271v1#bib.bib6)) and Yang ([2021](https://arxiv.org/html/2511.01271v1#bib.bib48)), which incorporate exogenous features and assume a homogeneous spatial coefficient. This structure presents challenges in identifying suitable instrumental variables for method-of-moments estimation.
Third, we consider both observable and latent factor structures. When factors are observable, our model aligns with the spatial asset pricing models of Kou et al. ([2018](https://arxiv.org/html/2511.01271v1#bib.bib29)) and Hu et al. ([2023](https://arxiv.org/html/2511.01271v1#bib.bib28)) for financial returns. However, when factors are unobservable, which is not considered in Kou et al. ([2018](https://arxiv.org/html/2511.01271v1#bib.bib29)) or Hu et al. ([2023](https://arxiv.org/html/2511.01271v1#bib.bib28)), our model extends the statistical and econometric factor models by incorporating spatial interaction terms, capturing additional panel information beyond common latent factors.
Fourth, our model accommodates panel dimensions that can grow to infinity, differing from the quasi-maximum likelihood estimation (QMLE) framework in Aquaro et al. ([2021](https://arxiv.org/html/2511.01271v1#bib.bib4)) and Hu et al. ([2023](https://arxiv.org/html/2511.01271v1#bib.bib28)), where the dimension is fixed. This flexibility enables broader applications in high-dimensional settings.

These distinctive features of the proposed SAPT model introduce additional estimation challenges, making conventional spatial econometric methods inadequate.
For models with observable factors, the widely used QMLE approach, as discussed in Lee ([2004](https://arxiv.org/html/2511.01271v1#bib.bib32)), Yu et al. ([2008](https://arxiv.org/html/2511.01271v1#bib.bib49)), and Bai and Li ([2021](https://arxiv.org/html/2511.01271v1#bib.bib6)), often encounters computational difficulties due to the large matrix determinants involved in the likelihood function. These challenges become even more pronounced in high-dimensional settings, especially when estimating numerous unit-specific spatial coefficients.
In cases with heteroskedastic disturbances, Lin and Lee ([2010](https://arxiv.org/html/2511.01271v1#bib.bib36)) demonstrated that the QML estimator for the spatial autoregressive (SAR) model is inconsistent if heteroskedasticity is ignored. To address this problem, they proposed a GMM estimator, which is computationally more efficient than QMLE. However, the SAPT model considered here lacks lagged or exogenous variables, making it difficult to identify suitable instrumental variables for constructing sufficiently many estimating equations.

In view of this, we propose a ridge-regularized Yule-Walker estimator that integrates shrinkage techniques with method-of-moments. By incorporating lagged common factors as instrumental variables, we reformulate parameter estimation as a system of L2L\_{2}-penalty Yule-Walker equations for each panel component, thereby addressing the issue of insufficient number of estimating equations in settings without exogenous variables or structural constraints on spatial effects.
In contrast to the regularized method-of-moments approaches proposed by Liao ([2013](https://arxiv.org/html/2511.01271v1#bib.bib35)) and Carrasco and Tchuente ([2015](https://arxiv.org/html/2511.01271v1#bib.bib8)), which primarily focus on selecting instruments or moment conditions, our method applies ridge regularization directly to the Yule-Walker equations to mitigate potential singularity and improve estimation robustness. We establish the asymptotic properties of our estimator in the setting where both the dimension NN and the sample size TT approach infinity. Despite the bias inherent in ridge estimators, we demonstrate the feasibility of conducting joint parameter inference. This contrasts with QML estimators in Aquaro et al. ([2021](https://arxiv.org/html/2511.01271v1#bib.bib4)) and Hu et al. ([2023](https://arxiv.org/html/2511.01271v1#bib.bib28)) which often require finite NN and inevitably accumulate asymptotic bias as NN diverges with TT; See Remarks 6 and 7 in Aquaro et al. ([2021](https://arxiv.org/html/2511.01271v1#bib.bib4)) for a discussion.
While alternative methods, such as those proposed by Bai and Li ([2021](https://arxiv.org/html/2511.01271v1#bib.bib6)), ensure parameter consistency under structural constraints and complex bias correction, it remains unclear whether their approach is feasible for the SAPT considered in this paper with heterogeneous spatial interactions.

In the presence of latent factors, our model can be reformulated as an approximate factor model. We propose a two-step procedure to extract latent factors and to estimate unknown parameters. Given the white noise assumption on the error terms in the SAPT model (see Kou et al. ([2018](https://arxiv.org/html/2511.01271v1#bib.bib29)), Aquaro et al. ([2021](https://arxiv.org/html/2511.01271v1#bib.bib4)), and Hu et al. ([2023](https://arxiv.org/html/2511.01271v1#bib.bib28))), we first apply the auto-covariance-based eigenanalysis approach from Lam and Yao ([2012](https://arxiv.org/html/2511.01271v1#bib.bib30)) and Gao and Tsay ([2022](https://arxiv.org/html/2511.01271v1#bib.bib23)) to estimate dynamically dependent factors. This ensures that the factors and their lagged counterparts remain uncorrelated with the noise terms, enabling their use as instrumental variables.
Once the factors are extracted via eigenanalysis, we implement the Yule-Walker estimation method, replacing the unknown factors with their estimated counterparts. Furthermore, we establish the asymptotic properties of the estimated factors, scalar coefficients, and loading vectors as both the dimension
NN and sample size
TT approach infinity. Notably, we also derive the limiting distributions of the estimated factors under a proper rotation matrix, a result not presented in Lam and Yao ([2012](https://arxiv.org/html/2511.01271v1#bib.bib30)), offering independent interest for readers.

We conduct extensive simulations to evaluate the accuracy of our estimation method, particularly in estimating the spatial rho and the loading matrix, while examining the convergence and asymptotic properties of the jointly estimated parameters.
Moreover, we compare our method’s predictive performance with QML estimators. The results show that our approach outperforms these alternatives in out-of-sample forecasting. Empirically, we apply our method to two real datasets on U.S. stock returns and housing prices, respectively. In both cases, it achieves superior out-of-sample forecasting performance compared to QMLE and the classical Fama-French factor model, reinforcing its practical advantages in high-dimensional economic and financial analysis.

This paper makes several significant contributions. First, rather than relying on a mathematical formulation, we derive the SCAPM from a classical mean-variance perspective and extend it to a SAPT framework by integrating a multifactor structure. This approach offers a new perspective for economists and practitioners in understanding spatial asset pricing theory.
Second, from a modeling standpoint, the proposed framework is flexible, accommodating both observable and latent factors. This extension provides an opportunity to explore the dynamics of large-dimensional economic and financial panel systems.
Third, from a methodological perspective, since QMLE methods require extensive computation and may be impractical in high-dimensional settings with general covariance structures, we propose a shrinkage estimation approach with joint inferential theory for the proposed models. While individual estimators may not be consistent, joint estimation allows for consistent inference. Our procedure is computationally efficient and avoids the need for restrictive distributional or covariance assumptions when using the Yule-Walker estimation method. More importantly, the proposed shrinkage estimation method outperforms the QMLE method in out-of-sample evaluations, highlighting their empirical advantages in high-dimensional applications.

The remainder of the paper is structured as follows. Section [2](https://arxiv.org/html/2511.01271v1#S2 "2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") outlines the formulations of the SCAPM and SAPT models under study. Section [3](https://arxiv.org/html/2511.01271v1#S3 "3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") provides the modeling framework and its estimation procedure. Section [4](https://arxiv.org/html/2511.01271v1#S4 "4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") establishes the asymptotic properties of the derived estimators. Section [5](https://arxiv.org/html/2511.01271v1#S5 "5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") evaluates the finite-sample performance of the proposed approach through simulations and Section [6](https://arxiv.org/html/2511.01271v1#S6 "6 Empirical Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") illustrates the proposed model and method with two empirical applications. Section 5 concludes. All proofs and derivations for the asymptotic results are relegated to an online Appendix.

Notation: We use the following notation. For a p×1p\times 1 vector
𝐮=(u1,…,up)′{\mathbf{u}}=(u\_{1},...,u\_{p})^{\prime}, ‖𝐮‖1=∑i=1p|ui|\|{\mathbf{u}}\|\_{1}=\sum\_{i=1}^{p}|u\_{i}| is the ℓ1\ell\_{1}-norm and ‖𝐮‖∞=max1≤i≤p⁡|ui|\|{\mathbf{u}}\|\_{\infty}=\max\_{1\leq i\leq p}|u\_{i}| is the ℓ∞\ell\_{\infty}-norm. 𝐈p{\mathbf{I}}\_{p} denotes the p×pp\times p identity matrix. For a matrix 𝐇{\mathbf{H}}, its Frobenius norm is ‖𝐇‖=[trace​(𝐇′​𝐇)]1/2\|{\mathbf{H}}\|=[\mathrm{trace}({\mathbf{H}}^{\prime}{\mathbf{H}})]^{1/2} and its operator norm is ‖𝐇‖2=λmax​(𝐇′​𝐇)\|{\mathbf{H}}\|\_{2}=\sqrt{\lambda\_{\max}({\mathbf{H}}^{\prime}{\mathbf{H}})}, where
λmax​(⋅)\lambda\_{\max}(\cdot) denotes the largest eigenvalue of a matrix, and ‖𝐇‖min\|{\mathbf{H}}\|\_{\min} is the square root of the minimum non-zero eigenvalue of 𝐇𝐇′{\mathbf{H}}{\mathbf{H}}^{\prime}. |𝐇||{\mathbf{H}}| denotes the absolute value of 𝐇{\mathbf{H}} elementwisely. The superscript ′ denotes the
transpose of a vector or matrix. We also use the notation a≍ba\asymp b to denote a=O​(b)a=O(b) and b=O​(a)b=O(a) or aa and bb have the same order of stochastic bound when they are random variables.

## 2 Spatial CAMP and Spatial APT

In this section, we develop a Spatial Capital Asset Pricing Model (SCAPM) using mean-variance analysis within a complete market framework. Additionally, we construct a spatial arbitrage pricing theory model by incorporating a multifactor structure.

### 2.1 Complete Market Assumption

We consider a one-period economy with NN risky assets in the market whose random returns are denoted as 𝐫=(r1,…,rN)′{\mathbf{r}}=(r\_{1},...,r\_{N})^{\prime} over the period.
The expected return is 𝝁=(μ1,…,μN)′\boldsymbol{\mu}=(\mu\_{1},...,\mu\_{N})^{\prime} and the risk-free asset return is rfr\_{f}. Let rMr\_{M} be the return of the market portfolio or the tangency portfolio in the mean-variance framework of Markowitz ([1952](https://arxiv.org/html/2511.01271v1#bib.bib38)) with expected return μM\mu\_{M}.

Suppose the NN assets are diverse, with NN sufficiently large, and encompass a wide spectrum of asset categories. It is reasonable to assume that each individual asset exhibits some degree of association with the others. Within this framework, we introduce the concept of a complete market, which implies that the extensive set of assets enables the formation of suitable linear combinations to replicate the returns of any specific asset in the market. The definition of a complete market, or equivalently, a minimum complete market, is provided in Definition [1](https://arxiv.org/html/2511.01271v1#Thmdefinition1 "Definition 1 (Complete Market). ‣ 2.1 Complete Market Assumption ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") and equivalently in Definition [2](https://arxiv.org/html/2511.01271v1#Thmdefinition2 "Definition 2 (Minimum Complete Market). ‣ 2.1 Complete Market Assumption ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") below.

###### Definition 1 (Complete Market).

Suppose there are
NN risky assets in the market, where
NN is sufficiently large. The market is said to be complete if the return of any asset
rjr\_{j} can be expressed as a linear combination of the remaining
N−1N-1 assets, i.e., those indexed by {1,…,N}∖{j}\{1,...,N\}\setminus\{j\}, for j=1,…,Nj=1,...,N, However,
rjr\_{j} cannot be replicated using only
N−2N-2 assets from {1,…,N}∖{j}\{1,...,N\}\setminus\{j\}.

###### Definition 2 (Minimum Complete Market).

A market is called a minimum complete market if it contains at least
N−1N-1 assets from a complete market, as the return of the remaining asset can be fully replicated by a linear combination of the other
N−1N-1 assets in this minimum complete market.

This conceptualization of a complete market aligns with the idea that the abundance and diversity of assets enable the construction of portfolios capable of replicating the performance of any individual asset. It suggests that the richness of the market, in terms of asset variety, allows for the creation of synthetic versions of assets by leveraging a diverse set of available instruments.

In a high-dimensional setting, market completeness arises from the vast number and diversity of assets, facilitating the construction of well-diversified portfolios that can closely approximate the returns of specific assets. The concept of a complete market is closely tied to the absence of arbitrage opportunities. In such a market, no-arbitrage conditions ensure that riskless profits cannot be generated through linear combinations of available assets. If arbitrage opportunities existed, they would indicate an incomplete market, as investors could exploit them to create new assets beyond those initially available.

However, achieving a truly complete market in practice is challenging. Real-world markets often face limitations in asset variety, and factors such as transaction costs, market frictions, and short-selling constraints can hinder perfect asset replication. Nonetheless, the notion of a complete market provides a framework for understanding the relationships among assets and their pricing dynamics in a diversified financial environment.

### 2.2 From CAPM to Spatial CAPM

![Refer to caption](x1.png)


Figure 1: Mean-variance efficient frontier with a risk-free asset. The horizontal axis denotes the standard deviation of the portfolio and the vertical axis denotes the expected return of the corresponding portfolio. Available at <https://quantpedia.com/markowitz-model/>.

Based on the mean-variance analysis (e.g., Cochrane ([2009](https://arxiv.org/html/2511.01271v1#bib.bib11))), there exists a weight vector 𝜽=(θ1,…,θN)′\boldsymbol{\theta}=(\theta\_{1},...,\theta\_{N})^{\prime} such that the market (or tangency) portfolio can be expressed as
rM=𝜽′​𝐫r\_{M}=\boldsymbol{\theta}^{\prime}{\mathbf{r}}, as illustrated in Figure [1](https://arxiv.org/html/2511.01271v1#S2.F1 "Figure 1 ‣ 2.2 From CAPM to Spatial CAPM ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). For the jj-th asset with return rjr\_{j} and expected return μj\mu\_{j}, the capital asset pricing model (CAPM) of Sharpe ([1964](https://arxiv.org/html/2511.01271v1#bib.bib44)) states that

|  |  |  |
| --- | --- | --- |
|  | μj−rf=Cov​(rj,rM)Var​(rM)​(μM−rf),\mu\_{j}-r\_{f}=\frac{\textnormal{Cov}(r\_{j},r\_{M})}{\textnormal{Var}(r\_{M})}(\mu\_{M}-r\_{f}), |  |

where the quantity βj=Cov​(rj,t,rM,t)Var​(rM,t)\beta\_{j}=\frac{\textnormal{Cov}(r\_{j,t},r\_{M,t})}{\textnormal{Var}(r\_{M,t})} is referred to as the market beta of the jjth asset in the finance literature. In practice, the S&P 500 index return often
serves as a proxy for the market portfolio, and the market beta can be estimated by running an OLS regression over TT periods. For further details, see Chapters 5 and 9 of Cochrane ([2009](https://arxiv.org/html/2511.01271v1#bib.bib11)).

Next, we formulate a spatial capital asset pricing model (SCAPM), building on the mean-variance analysis within a complete market defined in Definition [1](https://arxiv.org/html/2511.01271v1#Thmdefinition1 "Definition 1 (Complete Market). ‣ 2.1 Complete Market Assumption ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions").
For each jj, we remove rjr\_{j} from the portfolio return vector 𝐫{\mathbf{r}} and consider the mean-variance analysis of the remaining N−1N-1 risky assets and the risk-free rate rfr\_{f}. Through
the classic mean-variance optimization, we obtain the portfolio weight 𝐰j{\mathbf{w}}\_{j}, where the jj-th position of 𝐰j{\mathbf{w}}\_{j} is zero and 𝐰j′​𝟏N=1{\mathbf{w}}\_{j}^{\prime}{\bf 1}\_{N}=1 such that the portfolio 𝐰j′​𝐫{\mathbf{w}}\_{j}^{\prime}{\mathbf{r}} is a tangency portfolio, as illustrated in Figure [1](https://arxiv.org/html/2511.01271v1#S2.F1 "Figure 1 ‣ 2.2 From CAPM to Spatial CAPM ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") without the jj-th asset. The optimal portfolios lie along the capital allocation line (CAL) in the mean-variance framework, with a slope

|  |  |  |
| --- | --- | --- |
|  | μj,M−rfσj,M,\frac{\mu\_{j,M}-r\_{f}}{\sigma\_{j,M}}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | μj,M=E(𝐰j′𝐫),andσj,M=Var(𝐰j′𝐫).\mu\_{j,M}=E({\mathbf{w}}\_{j}^{\prime}{\mathbf{r}}),\,\,\text{and}\,\,\sigma\_{j,M}=\sqrt{\textnormal{Var}({\mathbf{w}}\_{j}^{\prime}{\mathbf{r}}}). |  |

Then, for the asset jj with expected return μj\mu\_{j}, we have the following theorem.

###### Theorem 1.

Suppose the
NN risky assets are in a complete market, as described in Definition [1](https://arxiv.org/html/2511.01271v1#Thmdefinition1 "Definition 1 (Complete Market). ‣ 2.1 Complete Market Assumption ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). For the
jj-th risky asset with expected return μj\mu\_{j}, we have the following relationship:

|  |  |  |
| --- | --- | --- |
|  | μj−rf=Cov​(rj,𝐰j′​𝐫)Var​(𝐰j′​𝐫)​(μj,M−rf),\mu\_{j}-r\_{f}=\frac{\textnormal{Cov}(r\_{j},{\mathbf{w}}\_{j}^{\prime}{\mathbf{r}})}{\textnormal{Var}({\mathbf{w}}\_{j}^{\prime}{\mathbf{r}})}(\mu\_{j,M}-r\_{f}), |  |

where μj,M\mu\_{j,M} is the expected return of the tangency portfolio rj,M=𝐰j′​𝐫r\_{j,M}={\mathbf{w}}\_{j}^{\prime}{\mathbf{r}} with the jj-th asset excluded from the portfolio. We define ρj=Cov​(rj,𝐰j′​𝐫)Var​(𝐰j′​𝐫)\rho\_{j}=\frac{\textnormal{Cov}(r\_{j},{\mathbf{w}}\_{j}^{\prime}{\mathbf{r}})}{\textnormal{Var}({\mathbf{w}}\_{j}^{\prime}{\mathbf{r}})} and refer to it as the “spatial rho” for the jj-th asset.

The proof of Theorem [1](https://arxiv.org/html/2511.01271v1#Thmtheorem1 "Theorem 1. ‣ 2.2 From CAPM to Spatial CAPM ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") can be found in the Appendix. From Theorem [1](https://arxiv.org/html/2511.01271v1#Thmtheorem1 "Theorem 1. ‣ 2.2 From CAPM to Spatial CAPM ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we observe that the spatial rho is asset-specific, similar to the market beta in the CAPM. However, the key difference is that the spatial tangent portfolio is also asset-specific, which contrasts with the classical CAPM, where the market portfolio is fixed and unique for all assets.

### 2.3 Spatial Arbitrage Pricing Theory

In this section, we derive a spatial arbitrage pricing theory model following the framework of Ross ([1976](https://arxiv.org/html/2511.01271v1#bib.bib43)). To better illustrate the application of the proposed model in asset pricing, we use the notation 𝐫t=(r1,t,…,rN,t)′{\mathbf{r}}\_{t}=(r\_{1,t},...,r\_{N,t})^{\prime} to denote a vector of returns to NN risky assets at time tt. Letting 𝝁0=(μ0,1,…,μ0,N)′\boldsymbol{\mu}\_{0}=(\mu\_{0,1},...,\mu\_{0,N})^{\prime} be the expected returns of 𝐫t{\mathbf{r}}\_{t}, we consider the following asset pricing model with spatial interactions and multi-factors:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐫t\displaystyle{\mathbf{r}}\_{t} | =𝐃​(𝝆)​𝐖𝐫t+𝝂0+𝐁𝐟t+𝜺t,\displaystyle={\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}}{\mathbf{r}}\_{t}+\boldsymbol{\nu}\_{0}+{\mathbf{B}}{\mathbf{f}}\_{t}+\mbox{$\varepsilon$}\_{t}, |  | (1) |

where 𝐟t=(f1,t{\mathbf{f}}\_{t}=(f\_{1,t},…,fK,t)′f\_{K,t})^{\prime} consists of KK observable factors for which the expected return
of fi,tf\_{i,t} is μi\mu\_{i}, for i=1,…,Ki=1,...,K. The columns of 𝐁=(𝜹1,…,𝜹K){\mathbf{B}}=(\boldsymbol{\delta}\_{1},...,\boldsymbol{\delta}\_{K}) are the associated KK loading vectors of the KK factors, and 𝝂0=(𝐈N−𝐃​(𝝆)​𝐖)​𝝁0\boldsymbol{\nu}\_{0}=({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})\boldsymbol{\mu}\_{0}, where 𝝆\boldsymbol{\rho} is a vector of spatial rhos.
𝐖{\mathbf{W}} is a known spatial weight matrix with zero main diagonal elements, and 𝐃​(𝝆)=d​i​a​g​(ρ1,…,ρN){\mathbf{D}}(\boldsymbol{\rho})=diag(\rho\_{1},...,\rho\_{N}), where ρj\rho\_{j} can be estimated by the method in Section [3](https://arxiv.org/html/2511.01271v1#S3 "3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") below. We may assume each row of 𝐖{\mathbf{W}}, denoted as 𝐰j{\mathbf{w}}\_{j}, can be calculated either based on some economic distance or through
the mean-variance analysis.
We introduce some notations before the derivation of the spatial arbitrage pricing theory. We use 𝟏N{\bf 1}\_{N} to denote the NN-dimensional vector of 1, e.g., 𝟏N=(1,…,1)′∈RN{\bf 1}\_{N}=(1,...,1)^{\prime}\in R^{N}. Let 𝜽=(θ1,…,θN)′\boldsymbol{\theta}=(\theta\_{1},...,\theta\_{N})^{\prime} represent the weight vector that will be used to construct an arbitrage portfolio. Our derivation proceeds in the following three steps.

Step 1.
Suppose the random vector of returns 𝐫t{\mathbf{r}}\_{t} satisfies Model ([1](https://arxiv.org/html/2511.01271v1#S2.E1 "In 2.3 Spatial Arbitrage Pricing Theory ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). We use a weight vector 𝜽\boldsymbol{\theta} to construct an arbitrage portfolio of NN assets, where we assume 𝜽′​𝟏N=0\boldsymbol{\theta}^{\prime}{\bf 1}\_{N}=0, implying that there is no wealth invested in the portfolio. We also
require 𝜽\boldsymbol{\theta} to be a well-diversified portfolio weight with each component θi\theta\_{i} being of order 1/N1/N in magnitude as in Ross ([1976](https://arxiv.org/html/2511.01271v1#bib.bib43)).

Step 2. The random return of the portfolio can be written as

|  |  |  |
| --- | --- | --- |
|  | 𝜽′​𝐫t=𝜽′​𝝁0+𝜽′​(𝐈N−𝐃​(𝝆)​𝐖)−1​𝐁𝐟t+𝜽′​(𝐈N−𝐃​(𝝆)​𝐖)−1​𝜺t,\boldsymbol{\theta}^{\prime}{\mathbf{r}}\_{t}=\boldsymbol{\theta}^{\prime}\boldsymbol{\mu}\_{0}+\boldsymbol{\theta}^{\prime}({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}{\mathbf{B}}{\mathbf{f}}\_{t}+\boldsymbol{\theta}^{\prime}({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}\mbox{$\varepsilon$}\_{t}, |  |

where 𝝁0=(𝐈N−𝐃​(𝝆)​𝐖)−1​𝝂0\boldsymbol{\mu}\_{0}=({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}\boldsymbol{\nu}\_{0}. We further assume that εi,t{\varepsilon}\_{i,t}’s are independent with each other, for ii and tt, which is a commonly used assumption in the spatial econometrics literature, and each element of 𝐒​(𝝆)−1=(𝐈N−𝐃​(𝝆)​𝐖)−1{\mathbf{S}}(\boldsymbol{\rho})^{-1}=({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1} are of order 1/N1/N in absolute magnitude. Together with Assumption [2](https://arxiv.org/html/2511.01271v1#Thmassumption2 "Assumption 2. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") in Section [4](https://arxiv.org/html/2511.01271v1#S4 "4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") below, by the law of large numbers, we can show that

|  |  |  |
| --- | --- | --- |
|  | 𝜽′​(𝐈N−𝐃​(𝝆)​𝐖)−1​𝜺t=op​(1),\boldsymbol{\theta}^{\prime}({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}\mbox{$\varepsilon$}\_{t}=o\_{p}(1), |  |

and, hence,

|  |  |  |
| --- | --- | --- |
|  | 𝜽′​𝐫t≈𝜽′​𝝁0+𝜽′​(𝐈N−𝐃​(𝝆)​𝐖)−1​𝐁𝐟t.\boldsymbol{\theta}^{\prime}{\mathbf{r}}\_{t}\approx\boldsymbol{\theta}^{\prime}\boldsymbol{\mu}\_{0}+\boldsymbol{\theta}^{\prime}({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}{\mathbf{B}}{\mathbf{f}}\_{t}. |  |

Step 3. If we require that the arbitrage portfolio with weight 𝜽\boldsymbol{\theta} be chosen with no systematic risk, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜽′​(𝐈N−𝐃​(𝝆)​𝐖)−1​𝜹i=0,i=1,…,K.\boldsymbol{\theta}^{\prime}({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}\boldsymbol{\delta}\_{i}=0,\quad i=1,...,K. |  | (2) |

This condition ensures that the return of the arbitrage portfolio becomes 𝜽′​𝝁0\boldsymbol{\theta}^{\prime}\boldsymbol{\mu}\_{0}. Using the constraint of no wealth that 𝜽′​𝟏N=0\boldsymbol{\theta}^{\prime}{\bf 1}\_{N}=0, the return must be zero to prevent arbitrarily large disequilibrium positions. Therefore, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜽′​𝝁0=0.\boldsymbol{\theta}^{\prime}\boldsymbol{\mu}\_{0}=0. |  | (3) |

From the relationships in ([2](https://arxiv.org/html/2511.01271v1#S2.E2 "In 2.3 Spatial Arbitrage Pricing Theory ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), ([3](https://arxiv.org/html/2511.01271v1#S2.E3 "In 2.3 Spatial Arbitrage Pricing Theory ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), and 𝜽′​𝟏N=0\boldsymbol{\theta}^{\prime}{\bf 1}\_{N}=0, we conclude that 𝝁0\boldsymbol{\mu}\_{0}, 𝟏N{\bf 1}\_{N}, and (𝐈N−𝐃​(𝝆)​𝐖)−1​𝜹i({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}\boldsymbol{\delta}\_{i} are on the same hyperplane, for i=1,…,Ki=1,...,K. Then there exist γ0\gamma\_{0}, γ1\gamma\_{1},…, γK\gamma\_{K} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝁0=γ0,i​𝟏N+γi​(𝐈N−𝐃​(𝝆)​𝐖)−1​𝜹i,i=1,…,K.\boldsymbol{\mu}\_{0}=\gamma\_{0,i}{\bf 1}\_{N}+\gamma\_{i}({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}\boldsymbol{\delta}\_{i},\quad i=1,...,K. |  | (4) |

We will solve the above equations for γ0,i\gamma\_{0,i} and γi\gamma\_{i} by a plug-in method. Note that when 𝝁0=rf​𝟏N\boldsymbol{\mu}\_{0}=r\_{f}{\bf 1}\_{N}, the return vector of a risk-free asset, the loadings associated with the factors are zero, i.e., 𝜹i=𝟎\boldsymbol{\delta}\_{i}={\bf 0}, for i=1,…,Ki=1,...,K. Furthermore, if we take 𝐫t=fi,t​𝟏N{\mathbf{r}}\_{t}=f\_{i,t}{\bf 1}\_{N}, then 𝝁0=μi​𝟏N\boldsymbol{\mu}\_{0}=\mu\_{i}{\bf 1}\_{N}, and the spatial parameter 𝝆=𝟎\boldsymbol{\rho}={\bf 0}, since there is no spatial effect for a single asset. In this case, the exposure to the ii-th factor is 𝜹i=𝟏N\boldsymbol{\delta}\_{i}={\bf 1}\_{N}, while the exposures to the other factors are zero.
These special cases result in the following equations:

|  |  |  |
| --- | --- | --- |
|  | {rf​𝟏N=γ0,i​𝟏N,μi​𝟏N=γ0,i​𝟏N+γi​𝟏N,i=1,…,K.\left\{\begin{array}[]{cc}r\_{f}{\bf 1}\_{N}=\gamma\_{0,i}{\bf 1}\_{N},\\ \mu\_{i}{\bf 1}\_{N}=\gamma\_{0,i}{\bf 1}\_{N}+\gamma\_{i}{\bf 1}\_{N},\quad i=1,...,K.\end{array}\right. |  |

It follows from the above equations that

|  |  |  |
| --- | --- | --- |
|  | γ0,i=rf,γi=μi−rf,i=1,…,K,\gamma\_{0,i}=r\_{f},\,\,\gamma\_{i}=\mu\_{i}-r\_{f},\quad i=1,...,K, |  |

where γ0,i\gamma\_{0,i} turns out to be independent of ii.
Then, ([4](https://arxiv.org/html/2511.01271v1#S2.E4 "In 2.3 Spatial Arbitrage Pricing Theory ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) becomes

|  |  |  |
| --- | --- | --- |
|  | 𝝁0=rf​𝟏N+(𝐈N−𝐃​(𝝆)​𝐖)−1​𝜹1​(μ1−rf)+…+(𝐈N−𝐃​(𝝆)​𝐖)−1​𝜹K​(μK−rf),\boldsymbol{\mu}\_{0}=r\_{f}{\bf 1}\_{N}+({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}\boldsymbol{\delta}\_{1}(\mu\_{1}-r\_{f})+...+({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}\boldsymbol{\delta}\_{K}(\mu\_{K}-r\_{f}), |  |

or equivalently,

|  |  |  |
| --- | --- | --- |
|  | (𝐈N−𝐃​(𝝆)​𝐖)​(𝝁0−rf​𝟏N)=𝜹1​(μ1−rf)+…+𝜹K​(μK−rf),({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})(\boldsymbol{\mu}\_{0}-r\_{f}{\bf 1}\_{N})=\boldsymbol{\delta}\_{1}(\mu\_{1}-r\_{f})+...+\boldsymbol{\delta}\_{K}(\mu\_{K}-r\_{f}), |  |

which is a spatial APT model that extends the SCAMP in Section [2.2](https://arxiv.org/html/2511.01271v1#S2.SS2 "2.2 From CAPM to Spatial CAPM ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") with multi-factors, where μi−rf\mu\_{i}-r\_{f} is the risk premium of the ii-th factor and 𝝁0−rf​𝟏N\boldsymbol{\mu}\_{0}-r\_{f}{\bf 1}\_{N} is the vector of NN excessive asset returns. For the jj-th asset, we can derive that

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ0,j−rf=ρj​𝐰j′​(𝝁0−rf​𝟏N)+𝜹1,j​(μ1−rf)+…+𝜹K,j​(μK−rf),j=1,…,N.\mu\_{0,j}-r\_{f}=\rho\_{j}{\mathbf{w}}\_{j}^{\prime}(\boldsymbol{\mu}\_{0}-r\_{f}{\bf 1}\_{N})+\boldsymbol{\delta}\_{1,j}(\mu\_{1}-r\_{f})+...+\boldsymbol{\delta}\_{K,j}(\mu\_{K}-r\_{f}),\,\,j=1,...,N. |  | (5) |

Therefore, we may construct a new asset-specific factor, called the spatial factor, defined as 𝐰j′​(𝝁0−rf​𝟏N){\mathbf{w}}\_{j}^{\prime}(\boldsymbol{\mu}\_{0}-r\_{f}{\bf 1}\_{N}) associated with the jj-th asset where the jj-th element of 𝐰j{\mathbf{w}}\_{j} is zero according to the definition of the spatial weight. The scalar ρj\rho\_{j} represents the spatial effect on the
jj-th asset, which is termed the spatial rho, in contrast to the market beta in the classic CAPM of Sharpe ([1964](https://arxiv.org/html/2511.01271v1#bib.bib44)).

In the next section, we examine a general APT model that incorporates spatial interactions and propose a Yule-Walker estimation and inference method using factor instruments and ridge techniques for the model.

## 3 General Model and Methodology

### 3.1 Setup

Let 𝐲t=(y1,t,…,yN,t)′{\mathbf{y}}\_{t}=(y\_{1,t},...,y\_{N,t})^{\prime} be an NN-dimensional observable panel of time series at time tt, where we assume all the data are centered with zero mean. Thus, 𝐲t{\mathbf{y}}\_{t} replaces (𝐫t−𝝁0)({\mathbf{r}}\_{t}-\boldsymbol{\mu}\_{0}) in Model ([1](https://arxiv.org/html/2511.01271v1#S2.E1 "In 2.3 Spatial Arbitrage Pricing Theory ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), and the factors {𝐟t}\{{\mathbf{f}}\_{t}\}, for t=1,…,Tt=1,...,T, are assumed to have zero mean. Based on the SAPT model in Section [2.3](https://arxiv.org/html/2511.01271v1#S2.SS3 "2.3 Spatial Arbitrage Pricing Theory ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we assume that 𝐲t{\mathbf{y}}\_{t} follows the following general structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐲t=𝐃​(𝝆)​𝐖𝐲t+𝐁𝐟t+𝜺t,t=1,…,T,{\mathbf{y}}\_{t}={\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}}{\mathbf{y}}\_{t}+{\mathbf{B}}{\mathbf{f}}\_{t}+\mbox{$\varepsilon$}\_{t},\,\,t=1,...,T, |  | (6) |

where 𝐟t{\mathbf{f}}\_{t} is a KK-dimensional factor process that is either observable or unobservable, 𝐁{\mathbf{B}} is the loading matrix associated with the factors, 𝐖{\mathbf{W}} is the N×NN\times N spatial weight matrix that measures the dependence among different economic units or individuals of 𝐲t{\mathbf{y}}\_{t}. 𝐃​(𝝆)=diag​(ρ1,…,ρN){\mathbf{D}}(\boldsymbol{\rho})=\mbox{diag}(\rho\_{1},...,\rho\_{N}), where ρj\rho\_{j} is an unknown coefficient parameter for the jj-th individual. 𝜺t\mbox{$\varepsilon$}\_{t} is a white noise term that is uncorrelated with 𝐟t{\mathbf{f}}\_{t}, but we allow for dependence between 𝐟t+j{\mathbf{f}}\_{t+j} and 𝜺t\mbox{$\varepsilon$}\_{t}, for j≥1j\geq 1, since the factors 𝐟t{\mathbf{f}}\_{t}’s are usually serially dependent, which may be correlated with some lagged noise terms.

It is a common practice in spatial econometrics to assume that 𝐖{\mathbf{W}} is known, and the main diagonal elements of 𝐖{\mathbf{W}} are zero. The weights may be based on physical distance, social networks, or “economic” distance, as seen in Case et al. ([1993](https://arxiv.org/html/2511.01271v1#bib.bib9)). For example, we may take wi​j:=(si​di​j)−1w\_{ij}:=(s\_{i}d\_{ij})^{-1}, for i≠ji\neq j, and wi​i=0w\_{ii}=0, where di​jd\_{ij} is the physical distance between location ii and location jj, and si:=∑jdi​j−1s\_{i}:=\sum\_{j}d\_{ij}^{-1}. Alternatively, we may take di​j−1d\_{ij}^{-1} as the sample correlation between the ii-th and jj-th economic units when there is no clear physical distance between them.
When ρ1=…=ρN\rho\_{1}=...=\rho\_{N}, the spatial interaction term in Model ([6](https://arxiv.org/html/2511.01271v1#S3.E6 "In 3.1 Setup ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) reduces to the classical setting in the spatial econometrics literature, such as Lee ([2004](https://arxiv.org/html/2511.01271v1#bib.bib32)), among others.

For a given spatial weight matrix 𝐖=(𝐰1,…,𝐰N)′{\mathbf{W}}=({\mathbf{w}}\_{1},\dots,{\mathbf{w}}\_{N})^{\prime}, where 𝐰i{\mathbf{w}}\_{i} is the ii-th row vector of 𝐖{\mathbf{W}}, our goal is to estimate the unknown coefficients in 𝝆\boldsymbol{\rho} and 𝐁{\mathbf{B}} when the factors 𝐟t{\mathbf{f}}\_{t}’s are observable. When the factors 𝐟t{\mathbf{f}}\_{t}’s are latent, we also need to recover the latent factors.

### 3.2 Shrinkage Yule-Walker Estimation with Observed Factors

In this section, we study the scenario when the factors are observed and propose a generalized shrinkage Yule-Walker method to estimate the unknown coefficients, which is essentially a combination of ridge regression and the method-of-moments. To this end, we begin with some useful notation. Define 𝚺y​f​(k)=Cov​(𝐲t,𝐟t−k)\boldsymbol{\Sigma}\_{yf}(k)=\textnormal{Cov}({\mathbf{y}}\_{t},{\mathbf{f}}\_{t-k}) as the covariance matrix between 𝐲t{\mathbf{y}}\_{t} and the past lagged factor variables 𝐟t−k{\mathbf{f}}\_{t-k}, and 𝚺f​(k)=Cov​(𝐟t,𝐟t−k)\boldsymbol{\Sigma}\_{f}(k)=\textnormal{Cov}({\mathbf{f}}\_{t},{\mathbf{f}}\_{t-k}) as the lag-kk auto-covariance matrix of 𝐟t{\mathbf{f}}\_{t}, for k≥0k\geq 0.
Then, Model ([6](https://arxiv.org/html/2511.01271v1#S3.E6 "In 3.1 Setup ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺y​f​(k)=𝐃​(𝝆)​𝐖​𝚺y​f​(k)+𝐁​𝚺f​(k),k≥0.\boldsymbol{\Sigma}\_{yf}(k)={\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}}\boldsymbol{\Sigma}\_{yf}(k)+{\mathbf{B}}\boldsymbol{\Sigma}\_{f}(k),\quad k\geq 0. |  | (7) |

Let 𝐞i{\mathbf{e}}\_{i} be the iith unit vector with the iith element equal to 11 and other elements being zero. For each k≥0k\geq 0, it follows from ([7](https://arxiv.org/html/2511.01271v1#S3.E7 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐞i′​𝚺y​f​(k)=𝐞i′​𝐃​(𝝆)​𝐖​𝚺y​f​(k)+𝐞i′​𝐁​𝚺f​(k),i=1,…,N.{\mathbf{e}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(k)={\mathbf{e}}\_{i}^{\prime}{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}}\boldsymbol{\Sigma}\_{yf}(k)+{\mathbf{e}}\_{i}^{\prime}{\mathbf{B}}\boldsymbol{\Sigma}\_{f}(k),\quad i=1,...,N. |  | (8) |

Note that 𝐞i′​𝐃​(𝝆)​𝐖=ρi​𝐰i′{\mathbf{e}}\_{i}^{\prime}{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}}=\rho\_{i}{\mathbf{w}}\_{i}^{\prime} and 𝐞i′​𝐁=𝐛i′{\mathbf{e}}\_{i}^{\prime}{\mathbf{B}}={\mathbf{b}}\_{i}^{\prime}, where 𝐰i{\mathbf{w}}\_{i} and 𝐛i{\mathbf{b}}\_{i} are the iith row vectors of 𝐖{\mathbf{W}} and 𝐁{\mathbf{B}}, respectively. Then, ([8](https://arxiv.org/html/2511.01271v1#S3.E8 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺y​f′​(k)​𝐞i=𝚺y​f′​(k)​𝐰i​ρi+𝚺f′​(k)​𝐛i,i=1,…,N.\boldsymbol{\Sigma}\_{yf}^{\prime}(k){\mathbf{e}}\_{i}=\boldsymbol{\Sigma}\_{yf}^{\prime}(k){\mathbf{w}}\_{i}\rho\_{i}+\boldsymbol{\Sigma}\_{f}^{\prime}(k){\mathbf{b}}\_{i},\quad i=1,...,N. |  | (9) |

In practice, given the sample data {(𝐲t,𝐟t):t=1,…,T}\{({\mathbf{y}}\_{t},{\mathbf{f}}\_{t}):t=1,...,T\}, by a similar argument to the Yule-Walker estimation method with a given lag k≥0k\geq 0, we may solve the following minimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ρ^i,𝐛^i′)′=arg⁡minρ∈R,𝐛∈Rr⁡{‖𝚺^y​f′​(k)​𝐞i−𝚺^y​f′​(k)​𝐰i​ρ−𝚺^f′​(k)​𝐛‖22},i=1,…,N,(\widehat{\rho}\_{i},\widehat{\mathbf{b}}\_{i}^{\prime})^{\prime}=\arg\min\_{\rho\in R,{\mathbf{b}}\in R^{r}}\{\|\widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}(k){\mathbf{e}}\_{i}-\widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}(k){\mathbf{w}}\_{i}\rho-\widehat{\boldsymbol{\Sigma}}\_{f}^{\prime}(k){\mathbf{b}}\|\_{2}^{2}\},\,\,i=1,...,N, |  | (10) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝚺^y​f​(k)=1T​∑t=k+1T𝐲t​𝐟t−kand𝚺^f​(k)=1T​∑t=k+1T𝐟t​𝐟t−k′\widehat{\boldsymbol{\Sigma}}\_{yf}(k)=\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{y}}\_{t}{\mathbf{f}}\_{t-k}\quad\text{and}\quad\widehat{\boldsymbol{\Sigma}}\_{f}(k)=\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{f}}\_{t}{\mathbf{f}}\_{t-k}^{\prime} |  |

are the sample versions of 𝚺y​f​(k)\boldsymbol{\Sigma}\_{yf}(k) and 𝚺f​(k)\boldsymbol{\Sigma}\_{f}(k), respectively. For each ii, we observe that there are K+1K+1 unknown coefficients in the optimization problem ([10](https://arxiv.org/html/2511.01271v1#S3.E10 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), but there are only KK equations for each lag kk in ([10](https://arxiv.org/html/2511.01271v1#S3.E10 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), which implies that the optimization problem is not well-defined if we only make use of a single kk in the Yule-Walker estimation. To see this, we cast problem ([10](https://arxiv.org/html/2511.01271v1#S3.E10 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) into the framework of the generalized method of moments (GMM) (Hansen ([1982](https://arxiv.org/html/2511.01271v1#bib.bib27))). Let 𝐟t−k{\mathbf{f}}\_{t-k} be the instrument, the moment conditions for ([6](https://arxiv.org/html/2511.01271v1#S3.E6 "In 3.1 Setup ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) are

|  |  |  |
| --- | --- | --- |
|  | E​𝐡t,k​(ρi,𝐛i)=0,where​𝐡t,k​(ρi,𝐛i)=(yi,t−ρi​𝐰i′​𝐲t−𝐛i′​𝐟t)​𝐟t−k′,i=1,…,N,E{\mathbf{h}}\_{t,k}(\rho\_{i},{\mathbf{b}}\_{i})=0,\,\,\text{where}\,\,{\mathbf{h}}\_{t,k}(\rho\_{i},{\mathbf{b}}\_{i})=(y\_{i,t}-\rho\_{i}{\mathbf{w}}\_{i}^{\prime}{\mathbf{y}}\_{t}-{\mathbf{b}}\_{i}^{\prime}{\mathbf{f}}\_{t}){\mathbf{f}}\_{t-k}^{\prime},\,\,i=1,...,N, |  |

which is equivalent to that in ([9](https://arxiv.org/html/2511.01271v1#S3.E9 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) for each kk. When k=0k=0, it is not hard to see that

|  |  |  |
| --- | --- | --- |
|  | 𝐡t,0​(ρi,𝐛i)=∂εi,t​(ρi,𝐛i)∂𝐛i,{\mathbf{h}}\_{t,0}(\rho\_{i},{\mathbf{b}}\_{i})=\frac{\partial{\varepsilon}\_{i,t}(\rho\_{i},{\mathbf{b}}\_{i})}{\partial{\mathbf{b}}\_{i}}, |  |

where εi,t​(ρi,𝐛i)=(yi,t−ρi​𝐰i′​𝐲t−𝐛i′​𝐟t)2{\varepsilon}\_{i,t}(\rho\_{i},{\mathbf{b}}\_{i})=(y\_{i,t}-\rho\_{i}{\mathbf{w}}\_{i}^{\prime}{\mathbf{y}}\_{t}-{\mathbf{b}}\_{i}^{\prime}{\mathbf{f}}\_{t})^{2}. Therefore, the equations produced by only taking partial derivatives concerning parameter 𝐛i{\mathbf{b}}\_{i} are not sufficient to estimate ρi\rho\_{i} and 𝐛i{\mathbf{b}}\_{i} simultaneously. Then we conclude that estimation equations in ([10](https://arxiv.org/html/2511.01271v1#S3.E10 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) are not sufficient for any given k≥0k\geq 0.

To address this challenge, we combine two sets of estimating equations, resulting in 2​K2K equations, which exceed the number of parameters by K+1K+1 when K≥1K\geq 1. We first note the importance of cross-sectional dependence in asset returns and economic data, so we retain the k=0k=0 equations, which align with GMM using 𝐟t{\mathbf{f}}\_{t} as instruments and the Least-Squares method. Additionally, since short-term dependence is more significant than long-term in economic and financial data, we focus on Equation ([10](https://arxiv.org/html/2511.01271v1#S3.E10 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) with k=0k=0 and k=1k=1. These lags capture the key dynamic information, reflecting the most relevant dependencies while excluding less impactful higher lags.

Specifically, let

|  |  |  |
| --- | --- | --- |
|  | 𝐘^i=(𝚺^y​f′​𝐞i𝚺^y​f′​(1)​𝐞i)​and​𝐗^i=(𝚺^y​f′​𝐰i𝚺^f𝚺^y​f′​(1)​𝐰i𝚺^f′​(1)),\widehat{\mathbf{Y}}\_{i}=\left(\begin{array}[]{c}\widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}{\mathbf{e}}\_{i}\\ \widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}(1){\mathbf{e}}\_{i}\end{array}\right)\,\,\text{and}\,\,\widehat{\mathbf{X}}\_{i}=\left(\begin{array}[]{cc}\widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}{\mathbf{w}}\_{i}&\widehat{\boldsymbol{\Sigma}}\_{f}\\ \widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&\widehat{\boldsymbol{\Sigma}}\_{f}^{\prime}(1)\end{array}\right), |  |

where 𝚺^y​f=𝚺^y​f​(0)\widehat{\boldsymbol{\Sigma}}\_{yf}=\widehat{\boldsymbol{\Sigma}}\_{yf}(0) and 𝚺^f=𝚺^f​(0)\widehat{\boldsymbol{\Sigma}}\_{f}=\widehat{\boldsymbol{\Sigma}}\_{f}(0). Due to the spatial nature of Model ([6](https://arxiv.org/html/2511.01271v1#S3.E6 "In 3.1 Setup ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), 𝐗^i\widehat{\mathbf{X}}\_{i} is asymptotically singular, though not in finite samples. To address this, we apply ridge regression. Define 𝜷=(ρ^,𝐛′)′∈ℝK+1\boldsymbol{\beta}=(\widehat{\rho},{\mathbf{b}}^{\prime})^{\prime}\in\mathbb{R}^{K+1} and solve the following optimization problem for a given λi>0\lambda\_{i}>0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜷^i​(λi)=(ρ^i,𝐛^i′)′=arg⁡minρ∈R,𝐛∈RK⁡{‖𝐘^i−𝐗^i​𝜷‖22+λi​‖𝜷‖22},i=1,…,N.\widehat{\boldsymbol{\beta}}\_{i}(\lambda\_{i})=(\widehat{\rho}\_{i},\widehat{\mathbf{b}}\_{i}^{\prime})^{\prime}=\arg\min\_{\rho\in R,{\mathbf{b}}\in R^{K}}\{\|\widehat{\mathbf{Y}}\_{i}-\widehat{\mathbf{X}}\_{i}\boldsymbol{\beta}\|\_{2}^{2}+\lambda\_{i}\|\boldsymbol{\beta}\|\_{2}^{2}\},\,\,i=1,...,N. |  | (11) |

The estimator has the explicit form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜷^i​(λi)=(𝐗^i′​𝐗^i+λi​𝐈K+1)−1​𝐗^i′​𝐘^i,i=1,…,N,\widehat{\boldsymbol{\beta}}\_{i}(\lambda\_{i})=(\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i}+\lambda\_{i}{\mathbf{I}}\_{K+1})^{-1}\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{Y}}\_{i},\,\,i=1,...,N, |  | (12) |

which is the ridge estimator. In the subsequent analysis, we denote (𝐗^i′​𝐗^i)+(\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i})^{+} as the Moore-Penrose generalized inverse and let 𝜷^i=𝜷^i​(0)\widehat{\boldsymbol{\beta}}\_{i}=\widehat{\boldsymbol{\beta}}\_{i}(0) as λi→0\lambda\_{i}\to 0. Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") establishes the joint asymptotic distribution under these conditions, enabling joint inference. In finite samples, the estimator depends on the number of lagged auto-covariances used in the Yule-Walker estimation in ([10](https://arxiv.org/html/2511.01271v1#S3.E10 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), but its asymptotic convergence remains valid, as demonstrated in Section [4](https://arxiv.org/html/2511.01271v1#S4 "4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions").

### 3.3 Boosting the Strength of Factor Instruments

In practice, we stack only the cases when k=0k=0 and k=1k=1 as discussed in Section [3.2](https://arxiv.org/html/2511.01271v1#S3.SS2 "3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). This
approach provides a jointly consistent estimator and avoids unnecessary errors in the generalized method of moments estimation. The choice of k=1k=1 is based on the assumption that short-term dependence is often
more relevant than long-term dependence. If necessary, we can define a measure to select the optimal lag k∗k^{\*} as follows:

|  |  |  |
| --- | --- | --- |
|  | k∗=arg⁡max1≤k≤k¯⁡|det(𝚺^f​(k))|,k^{\*}=\arg\max\_{1\leq k\leq\bar{k}}|\det(\widehat{\boldsymbol{\Sigma}}\_{f}(k))|, |  |

where k¯\bar{k} is a small positive integer, and |det(𝚺^f​(k))||\det(\widehat{\boldsymbol{\Sigma}}\_{f}(k))| is the product of the singular values of 𝚺^f​(k)\widehat{\boldsymbol{\Sigma}}\_{f}(k). This measure captures the correlation strength between the lagged instruments and the contemporaneous factors. We then define

|  |  |  |
| --- | --- | --- |
|  | 𝐘^i,∗=(𝚺^y​f′​𝐞i𝚺^y​f′​(k∗)​𝐞i)​and​𝐗^i,∗=(𝚺^y​f′​𝐰i𝚺^f𝚺^y​f′​(k∗)​𝐰i𝚺^f′​(k∗)),\widehat{\mathbf{Y}}\_{i,\*}=\left(\begin{array}[]{c}\widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}{\mathbf{e}}\_{i}\\ \widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}(k^{\*}){\mathbf{e}}\_{i}\end{array}\right)\,\,\text{and}\,\,\widehat{\mathbf{X}}\_{i,\*}=\left(\begin{array}[]{cc}\widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}{\mathbf{w}}\_{i}&\widehat{\boldsymbol{\Sigma}}\_{f}\\ \widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}(k^{\*}){\mathbf{w}}\_{i}&\widehat{\boldsymbol{\Sigma}}\_{f}^{\prime}(k^{\*})\end{array}\right), |  |

and substitute them into ([11](https://arxiv.org/html/2511.01271v1#S3.E11 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), yielding the refined estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜷^i,∗​(λi)=(𝐗^i,∗′​𝐗^i,∗+λi​𝐈K+1)−1​𝐗^i,∗′​𝐘^i,∗,i=1,…,N.\widehat{\boldsymbol{\beta}}\_{i,\*}(\lambda\_{i})=(\widehat{\mathbf{X}}\_{i,\*}^{\prime}\widehat{\mathbf{X}}\_{i,\*}+\lambda\_{i}{\mathbf{I}}\_{K+1})^{-1}\widehat{\mathbf{X}}\_{i,\*}^{\prime}\widehat{\mathbf{Y}}\_{i,\*},\quad i=1,...,N. |  | (13) |

### 3.4 Estimation When Factors Are Latent

In this section, we address the case where the factor processes 𝐟t{\mathbf{f}}\_{t} are unobservable. We focus on latent factors that represent the internal dynamics driving the data 𝐲t{\mathbf{y}}\_{t},
because the case with factors arising from some external data sources is similar to the diffusion-index framework in Stock and Watson ([2002](https://arxiv.org/html/2511.01271v1#bib.bib45)) and Gao and Tsay ([2024](https://arxiv.org/html/2511.01271v1#bib.bib25)). The estimation of the proposed model becomes more complex because, in addition to estimating the parameters in 𝝆\boldsymbol{\rho} and 𝐁{\mathbf{B}}, we must also recover the unknown factors. Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐲t=(𝐈N−𝐃​(𝝆)​𝐖)−1​𝐁𝐟t+(𝐈N−𝐃​(𝝆)​𝐖)−1​𝜺t=𝚲​𝐟t+𝝃t,{\mathbf{y}}\_{t}=({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}{\mathbf{B}}{\mathbf{f}}\_{t}+({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}\mbox{$\varepsilon$}\_{t}=\boldsymbol{\Lambda}{\mathbf{f}}\_{t}+\boldsymbol{\xi}\_{t}, |  | (14) |

where 𝚲=(𝐈N−𝐃​(𝝆)​𝐖)−1​𝐁\boldsymbol{\Lambda}=({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}{\mathbf{B}} and 𝝃t=(𝐈N−𝐃​(𝝆)​𝐖)−1​𝜺t\boldsymbol{\xi}\_{t}=({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}\mbox{$\varepsilon$}\_{t} are the loading matrix associated with the factor process 𝐟t{\mathbf{f}}\_{t} and the idiosyncratic term, respectively. Symbolically, ([14](https://arxiv.org/html/2511.01271v1#S3.E14 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) is a factor model with unknown factors and loading matrix, both of which need to be estimated from the data 𝐲t{\mathbf{y}}\_{t}, for t=1,…,Tt=1,...,T.

Under the framework of Model ([14](https://arxiv.org/html/2511.01271v1#S3.E14 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), we have a factor model with static factors
and could use either the PCA method of Bai and Ng ([2002](https://arxiv.org/html/2511.01271v1#bib.bib7)) to estimate cross-sectional factors or the eigen-analysis method in Lam and Yao ([2012](https://arxiv.org/html/2511.01271v1#bib.bib30)) to extract dynamically dependent factors. However, the PCA method is not suitable for the spatial interactions in Model ([14](https://arxiv.org/html/2511.01271v1#S3.E14 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), as the idiosyncratic noise recovered by PCA is often serially correlated. In contrast, the noise term 𝜺t\mbox{$\varepsilon$}\_{t} (or 𝝃t\boldsymbol{\xi}\_{t}) in the spatial model is white noise, which contradicts the PCA framework.

For spatial panel dynamic models in econometrics, the noise term 𝜺t\mbox{$\varepsilon$}\_{t} (or 𝝃t\boldsymbol{\xi}\_{t}) is white with zero serial correlation, while the dynamically dependent factors 𝐟t{\mathbf{f}}\_{t} capture all the dynamic information of the data 𝐲t{\mathbf{y}}\_{t}. This framework aligns with Lam et al. ([2011](https://arxiv.org/html/2511.01271v1#bib.bib31)), Lam and Yao ([2012](https://arxiv.org/html/2511.01271v1#bib.bib30)), and Gao and Tsay ([2022](https://arxiv.org/html/2511.01271v1#bib.bib23)), among others. Based on the auto-covariance-based eigenanalysis in Lam et al. ([2011](https://arxiv.org/html/2511.01271v1#bib.bib31)), we propose a two-step procedure to estimate the factors and other unknown coefficients, assuming the number of factors KK is known. The method for determining KK will be discussed later.

Note that 𝚲\boldsymbol{\Lambda} and 𝐟t{\mathbf{f}}\_{t} are not uniquely determined in ([14](https://arxiv.org/html/2511.01271v1#S3.E14 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) and they require certain identification conditions. For simplicity, we assume that 𝚲\boldsymbol{\Lambda} is a semi-orthogonal matrix scaled by N\sqrt{N} such that 𝚲′​𝚲/N=𝐈K\boldsymbol{\Lambda}^{\prime}\boldsymbol{\Lambda}/N={\mathbf{I}}\_{K}. However, the loading and factors are still not uniquely identified because we can replace (𝚲,𝐟t)(\boldsymbol{\Lambda},{\mathbf{f}}\_{t}) with (𝚲​𝐇,𝐇′​𝐟t)(\boldsymbol{\Lambda}{\mathbf{H}},{\mathbf{H}}^{\prime}{\mathbf{f}}\_{t}) for any orthonormal matrix 𝐇∈ℝK×K{\mathbf{H}}\in\mathbb{R}^{K\times K}. Nevertheless, the linear space spanned by the columns of 𝚲\boldsymbol{\Lambda}, denoted ℳ​(𝚲)\mathcal{M}(\boldsymbol{\Lambda}), is uniquely defined and referred to as the factor loading space.

Under the assumption that 𝜺t\mbox{$\varepsilon$}\_{t} is a white noise process and Cov​(𝐟t,𝜺t+j)=0\textnormal{Cov}({\mathbf{f}}\_{t},\mbox{$\varepsilon$}\_{t+j})=0, for j≥0j\geq 0, we allow for the possibility that 𝐟t{\mathbf{f}}\_{t} may depend on the past lagged noises 𝜺t−k\mbox{$\varepsilon$}\_{t-k}, for some k≥1k\geq 1, as 𝐟t{\mathbf{f}}\_{t} is a dynamically dependent process. For any integer k≥1k\geq 1, define the following covariance matrices of interest:

|  |  |  |
| --- | --- | --- |
|  | 𝚺y​(k)=Cov​(𝐲t,𝐲t−k),𝚺f​(k)=Cov​(𝐟t,𝐟t−k),and​𝚺f​ξ​(k)=Cov​(𝐟t,𝝃t−k).\boldsymbol{\Sigma}\_{y}(k)=\textnormal{Cov}({\mathbf{y}}\_{t},{\mathbf{y}}\_{t-k}),\,\,\boldsymbol{\Sigma}\_{f}(k)=\textnormal{Cov}({\mathbf{f}}\_{t},{\mathbf{f}}\_{t-k}),\,\,\text{and}\,\,\boldsymbol{\Sigma}\_{f\xi}(k)=\textnormal{Cov}({\mathbf{f}}\_{t},\boldsymbol{\xi}\_{t-k}). |  |

From ([14](https://arxiv.org/html/2511.01271v1#S3.E14 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺y​(k)=𝚲​𝚺f​(k)​𝚲′+𝚲​𝚺f​ξ​(k),k≥1.\boldsymbol{\Sigma}\_{y}(k)=\boldsymbol{\Lambda}\boldsymbol{\Sigma}\_{f}(k)\boldsymbol{\Lambda}^{\prime}+\boldsymbol{\Lambda}\boldsymbol{\Sigma}\_{f\xi}(k),\quad k\geq 1. |  | (15) |

For a pre-specified integer k0>0k\_{0}>0, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐌=∑k=1k0𝚺y​(k)​𝚺y′​(k)=𝚲​∑k=1k0[𝚺f​(k)​𝚲′+𝚺f​ξ​(k)]​[𝚲​𝚺f′​(k)+𝚺f​ξ′​(k)]​𝚲′,{\mathbf{M}}=\sum\_{k=1}^{k\_{0}}\boldsymbol{\Sigma}\_{y}(k)\boldsymbol{\Sigma}\_{y}^{\prime}(k)=\boldsymbol{\Lambda}\sum\_{k=1}^{k\_{0}}[\boldsymbol{\Sigma}\_{f}(k)\boldsymbol{\Lambda}^{\prime}+\boldsymbol{\Sigma}\_{f\xi}(k)][\boldsymbol{\Lambda}\boldsymbol{\Sigma}\_{f}^{\prime}(k)+\boldsymbol{\Sigma}\_{f\xi}^{\prime}(k)]\boldsymbol{\Lambda}^{\prime}, |  | (16) |

which is an N×NN\times N semi-positive definite matrix. Let 𝚲c\boldsymbol{\Lambda}\_{c} denote the orthogonal complement matrix of 𝚲\boldsymbol{\Lambda}. We observe that 𝐌​𝚲c=𝟎{\mathbf{M}}\boldsymbol{\Lambda}\_{c}=\mathbf{0}, implying that the columns of 𝚲c\boldsymbol{\Lambda}\_{c} are the eigenvectors corresponding to the zero eigenvalues of 𝐌{\mathbf{M}}. The factor loading space ℳ​(𝚲)\mathcal{M}(\boldsymbol{\Lambda}) is thus spanned by the eigenvectors (scaled by N\sqrt{N}) corresponding to the KK non-zero eigenvalues of 𝐌{\mathbf{M}}. The integer k0k\_{0} in ([16](https://arxiv.org/html/2511.01271v1#S3.E16 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) is a prescribed value that allows us to accumulate dynamic information across different lags. Since the dynamic dependence between 𝐲t{\mathbf{y}}\_{t} and 𝐲t−k{\mathbf{y}}\_{t-k} typically decreases as kk increases for stationary processes, a small k0k\_{0} is generally sufficient in practice. For further details on the rationale for using ([16](https://arxiv.org/html/2511.01271v1#S3.E16 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) to estimate the loading space from a projection perspective, we refer readers to Gao and Tsay ([2021](https://arxiv.org/html/2511.01271v1#bib.bib22)).

In practice, given the sample data {𝐲t∣t=0,1,…,T}\{{\mathbf{y}}\_{t}\mid t=0,1,\dots,T\}, the first step of the procedure is to estimate the loading matrix 𝚲\boldsymbol{\Lambda} or its column space ℳ​(𝚲)\mathcal{M}(\boldsymbol{\Lambda}), and to recover the factor process 𝐟t{\mathbf{f}}\_{t}, assuming that the number of factors KK is known. The estimation of KK will be discussed later. Let 𝚺^y​(k)\widehat{\boldsymbol{\Sigma}}\_{y}(k) denote the lag-kk sample autocovariance matrix of 𝐲t{\mathbf{y}}\_{t}, defined similarly to those in ([10](https://arxiv.org/html/2511.01271v1#S3.E10 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). To estimate ℳ​(𝚲)\mathcal{M}(\boldsymbol{\Lambda}), we perform an eigen-analysis of the sample version of 𝐌{\mathbf{M}}, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐌^=∑k=1k0𝚺^y​(k)​𝚺^y′​(k).\widehat{\mathbf{M}}=\sum\_{k=1}^{k\_{0}}\widehat{\boldsymbol{\Sigma}}\_{y}(k)\widehat{\boldsymbol{\Sigma}}\_{y}^{\prime}(k). |  | (17) |

Let 𝚲^\widehat{\boldsymbol{\Lambda}} be the standardized semi-orthogonal matrix consisting of the eigenvectors of 𝐌^\widehat{\mathbf{M}}, scaled by N\sqrt{N}, as its columns. The recovered factor processes are denoted as 𝐟^t=1N​𝚲^′​𝐲t\widehat{\mathbf{f}}\_{t}=\frac{1}{N}\widehat{\boldsymbol{\Lambda}}^{\prime}{\mathbf{y}}\_{t}, which can be obtained by the Ordinary Least Squares (OLS) method.

In the second step, we estimate the scalar coefficient vector 𝝆\boldsymbol{\rho} and the loading matrix 𝐁{\mathbf{B}} in Model ([6](https://arxiv.org/html/2511.01271v1#S3.E6 "In 3.1 Setup ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). Let 𝐟^1,…,𝐟^T{\widehat{\mathbf{f}}\_{1},\dots,\widehat{\mathbf{f}}\_{T}} denote the estimated factors obtained in the first step. Define the following quantities:

|  |  |  |
| --- | --- | --- |
|  | 𝚺~y​f​(k)=1T​∑t=k+1T𝐲t​𝐟^t−k′,𝚺~f​(k)=∑t=k+1T𝐟^t​𝐟^t−k′,and​𝚺~ε​f​(k)=1T​∑t=k+1T𝜺t​𝐟^t−k′,\widetilde{\boldsymbol{\Sigma}}\_{yf}(k)=\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{y}}\_{t}\widehat{\mathbf{f}}\_{t-k}^{\prime},\,\,\widetilde{\boldsymbol{\Sigma}}\_{f}(k)=\sum\_{t=k+1}^{T}\widehat{\mathbf{f}}\_{t}\widehat{\mathbf{f}}\_{t-k}^{\prime},\,\,\text{and}\,\,\widetilde{\boldsymbol{\Sigma}}\_{{\varepsilon}f}(k)=\frac{1}{T}\sum\_{t=k+1}^{T}\mbox{$\varepsilon$}\_{t}\widehat{\mathbf{f}}\_{t-k}^{\prime}, |  |

and 𝚺~y​f=𝚺~y​f​(0)\widetilde{\boldsymbol{\Sigma}}\_{yf}=\widetilde{\boldsymbol{\Sigma}}\_{yf}(0), 𝚺~f=𝚺~f​(0)\widetilde{\boldsymbol{\Sigma}}\_{f}=\widetilde{\boldsymbol{\Sigma}}\_{f}(0), and 𝚺~ε​f=𝚺~ε​f​(0)\widetilde{\boldsymbol{\Sigma}}\_{{\varepsilon}f}=\widetilde{\boldsymbol{\Sigma}}\_{{\varepsilon}f}(0). Following a similar procedure to the shrinkage Yule-Walker estimation in Section [3.2](https://arxiv.org/html/2511.01271v1#S3.SS2 "3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), where the factors are observable, we formulate the following optimization problem for the case of augmenting only k=0k=0 and k=1k=1, with a given λi>0\lambda\_{i}>0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜷~i​(λi)=(ρ~i,𝐛~i′)′=arg⁡minρ∈R,𝐛∈Rr⁡{‖𝐘~i−𝐗~i​𝜷‖22+λi​‖𝜷‖22},i=1,…,N,\widetilde{\boldsymbol{\beta}}\_{i}(\lambda\_{i})=(\widetilde{\rho}\_{i},\widetilde{\mathbf{b}}\_{i}^{\prime})^{\prime}=\arg\min\_{\rho\in R,{\mathbf{b}}\in R^{r}}\{\|\widetilde{\mathbf{Y}}\_{i}-\widetilde{\mathbf{X}}\_{i}\boldsymbol{\beta}\|\_{2}^{2}+\lambda\_{i}\|\boldsymbol{\beta}\|\_{2}^{2}\},\,\,i=1,...,N, |  | (18) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝐘~i=(𝚺~y​f′​𝐞i𝚺~y​f′​(1)​𝐞i)​and​𝐗~i=(𝚺~y​f′​𝐰i𝚺~f′𝚺~y​f′​(1)​𝐰i𝚺~f′​(1))\widetilde{\mathbf{Y}}\_{i}=\left(\begin{array}[]{c}\widetilde{\boldsymbol{\Sigma}}\_{yf}^{\prime}{\mathbf{e}}\_{i}\\ \widetilde{\boldsymbol{\Sigma}}\_{yf}^{\prime}(1){\mathbf{e}}\_{i}\end{array}\right)\,\,\text{and}\,\,\widetilde{\mathbf{X}}\_{i}=\left(\begin{array}[]{cc}\widetilde{\boldsymbol{\Sigma}}\_{yf}^{\prime}{\mathbf{w}}\_{i}&\widetilde{\boldsymbol{\Sigma}}\_{f}^{\prime}\\ \widetilde{\boldsymbol{\Sigma}}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&\widetilde{\boldsymbol{\Sigma}}\_{f}^{\prime}(1)\end{array}\right) |  |

represent the response variables and covariates, respectively.
The Yule-Walker estimation in ([18](https://arxiv.org/html/2511.01271v1#S3.E18 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) then yields the least squares (LS) estimator for 𝜷\boldsymbol{\beta} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜷~i​(λi)=(𝐗~i′​𝐗~i+λi​𝐈K+1)−1​𝐗~i′​𝐘~i,i=1,…,N.\widetilde{\boldsymbol{\beta}}\_{i}(\lambda\_{i})=(\widetilde{\mathbf{X}}\_{i}^{\prime}\widetilde{\mathbf{X}}\_{i}+\lambda\_{i}{\mathbf{I}}\_{K+1})^{-1}\widetilde{\mathbf{X}}\_{i}^{\prime}\widetilde{\mathbf{Y}}\_{i},\,\,i=1,...,N. |  | (19) |

Thus, we perform NN Yule-Walker estimation procedures, for i=1,…,Ni=1,\dots,N and obtain the estimators 𝝆~=(ρ~1,…,ρ~N)′\widetilde{\boldsymbol{\rho}}=(\widetilde{\rho}\_{1},\dots,\widetilde{\rho}\_{N})^{\prime} and 𝐁~=(𝐛~1,…,𝐛~N)′\widetilde{\mathbf{B}}=(\widetilde{\mathbf{b}}\_{1},\dots,\widetilde{\mathbf{b}}\_{N})^{\prime}. We can similarly define 𝜷~i=β~i​(0)\widetilde{\boldsymbol{\beta}}\_{i}=\widetilde{\beta}\_{i}(0) by adopting the Moore-Penrose inverse of 𝐗~i′​𝐗~i\widetilde{\mathbf{X}}\_{i}^{\prime}\widetilde{\mathbf{X}}\_{i} as in ([12](https://arxiv.org/html/2511.01271v1#S3.E12 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). Theorem [6](https://arxiv.org/html/2511.01271v1#Thmtheorem6 "Theorem 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") in Section [4](https://arxiv.org/html/2511.01271v1#S4 "4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") establishes the joint asymptotic distribution, which can be utilized for joint inference under this condition.

In practice, we may also use the boosting method described in Section [3.3](https://arxiv.org/html/2511.01271v1#S3.SS3 "3.3 Boosting the Strength of Factor Instruments ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") to select the optimal lag k∗k\*. We can then replace 𝚺~y​f​(1)\widetilde{\boldsymbol{\Sigma}}\_{yf}(1) and 𝚺~f​(1)\widetilde{\boldsymbol{\Sigma}}\_{f}(1) with 𝚺~y​f​(k∗)\widetilde{\boldsymbol{\Sigma}}\_{yf}(k^{\*}) and 𝚺~f​(k∗)\widetilde{\boldsymbol{\Sigma}}\_{f}(k^{\*}), respectively, in 𝐘~i\widetilde{\mathbf{Y}}\_{i} and 𝐗~i\widetilde{\mathbf{X}}\_{i}. The estimator 𝜷~i,∗​(λi)\widetilde{\boldsymbol{\beta}}\_{i,\*}(\lambda\_{i}) can be obtained in the same manner as that described in Section [3.3](https://arxiv.org/html/2511.01271v1#S3.SS3 "3.3 Boosting the Strength of Factor Instruments ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions").

### 3.5 Selecting the Number of Factors and the Penalty Parameters

In this section, we discuss the determination of the number of factors
KK in Model ([14](https://arxiv.org/html/2511.01271v1#S3.E14 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), which is typically unknown in practice. Over the past decades, several methods have been developed to estimate
KK, including the information criteria proposed by Bai and Ng ([2002](https://arxiv.org/html/2511.01271v1#bib.bib7)), the random matrix theory approach in Onatski ([2010](https://arxiv.org/html/2511.01271v1#bib.bib39)), the ratio-based method in Lam and Yao ([2012](https://arxiv.org/html/2511.01271v1#bib.bib30)) and Ahn and Horenstein ([2013](https://arxiv.org/html/2511.01271v1#bib.bib2)), the canonical correlation analysis technique in Gao and Tsay ([2019](https://arxiv.org/html/2511.01271v1#bib.bib21)), and the white noise testing approach in Gao and Tsay ([2022](https://arxiv.org/html/2511.01271v1#bib.bib23)), among others.
In this paper, we introduce two widely used methods for estimating KK.

The first method is an information criterion introduced by Bai and Ng ([2002](https://arxiv.org/html/2511.01271v1#bib.bib7)). It estimates KK by

|  |  |  |  |
| --- | --- | --- | --- |
|  | K^=arg⁡min0≤j≤J⁡log⁡(1N​T​∑t=1T‖𝐲t−1N​𝚲^j​𝚲^j′​𝐲t‖22)+j​g​(T,N),\widehat{K}=\arg\min\_{0\leq j\leq J}\log(\frac{1}{NT}\sum\_{t=1}^{T}\|{\mathbf{y}}\_{t}-\frac{1}{N}\widehat{\boldsymbol{\Lambda}}\_{j}\widehat{\boldsymbol{\Lambda}}\_{j}^{\prime}{\mathbf{y}}\_{t}\|\_{2}^{2})+jg(T,N), |  | (20) |

where JJ is a prescribed upper bound, 𝚲^j\widehat{\boldsymbol{\Lambda}}\_{j} is a N×jN\times j estimated loading matrix, and g​(T,N)g(T,N) is a penalty function of (N,T)(N,T) such that g​(T,N)=o​(1)g(T,N)=o(1) and min⁡{N,T}​g​(T,N)→∞\min\{N,T\}g(T,N)\rightarrow\infty. Two examples of g​(T,N)g(T,N) suggested by Bai and Ng ([2002](https://arxiv.org/html/2511.01271v1#bib.bib7)) are IC1 and IC2 given below:

|  |  |  |
| --- | --- | --- |
|  | I​C​1=N+TN​T​log⁡(N​TN+T)andI​C​2=N+TN​T​log⁡(min⁡{N,T}).IC1=\frac{N+T}{NT}\log(\frac{NT}{N+T})\quad\text{and}\quad IC2=\frac{N+T}{NT}\log(\min\{N,T\}). |  |

For the estimation of KK, in addition to the information criterion in ([20](https://arxiv.org/html/2511.01271v1#S3.E20 "In 3.5 Selecting the Number of Factors and the Penalty Parameters ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), we can adopt the ratio-based method proposed in Lam and Yao ([2012](https://arxiv.org/html/2511.01271v1#bib.bib30)) and Ahn and Horenstein ([2013](https://arxiv.org/html/2511.01271v1#bib.bib2)). Let μ^1≥⋯≥μ^N\widehat{\mu}\_{1}\geq\dots\geq\widehat{\mu}\_{N} be the NN eigenvalues of 𝐌^\widehat{\mathbf{M}}. We estimate KK by

|  |  |  |  |
| --- | --- | --- | --- |
|  | K^=arg⁡min1≤l≤R⁡μ^l+1/μ^l,\widehat{K}=\arg\min\_{1\leq l\leq R}{{\widehat{\mu}\_{l+1}}/{\widehat{\mu}\_{l}}}, |  | (21) |

where R=⌊N/2⌋R=\lfloor N/2\rfloor is commonly used, as suggested by Lam and Yao ([2012](https://arxiv.org/html/2511.01271v1#bib.bib30)).

For the selection of the penalty parameter λi\lambda\_{i}, it is common to assume that λi∈𝒮\lambda\_{i}\in\mathcal{S}, where 𝒮\mathcal{S} is a candidate set consisting of possible penalty choices. We split the data sample into two segments, 𝐲1,…,𝐲T1{{\mathbf{y}}\_{1},\dots,{\mathbf{y}}\_{T\_{1}}} and 𝐲T1+1,…,𝐲T{{\mathbf{y}}\_{T\_{1}+1},\dots,{\mathbf{y}}\_{T}}. Suppose ρ^i​(λ)\widehat{\rho}\_{i}(\lambda) and 𝐛^i​(λ)\widehat{\mathbf{b}}\_{i}(\lambda) are the estimators obtained from the first segment. The optimal λ\lambda is chosen by solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ^i=argminλ∈𝒮​1T−T1​∑t=T1+1T‖yi,t−ρ^i​(λ)​𝐰i′​𝐲t−𝐛^i​(λ)​𝐟t‖22.\widehat{\lambda}\_{i}=\mbox{argmin}\_{\lambda\in\mathcal{S}}\frac{1}{T-T\_{1}}\sum\_{t=T\_{1}+1}^{T}\|y\_{i,t}-\widehat{\rho}\_{i}(\lambda){\mathbf{w}}\_{i}^{\prime}{\mathbf{y}}\_{t}-\widehat{\mathbf{b}}\_{i}(\lambda){\mathbf{f}}\_{t}\|\_{2}^{2}. |  | (22) |

When the factors are unobservable, we replace 𝐟t{\mathbf{f}}\_{t} with 𝐟^t\widehat{\mathbf{f}}\_{t}, which is estimated from the second segment using the estimator 𝚲^​(λ)\widehat{\boldsymbol{\Lambda}}(\lambda) obtained from the first segment.

## 4 Theoretical Properties

In this section, we present the asymptotic theory for the estimation method of Section [3](https://arxiv.org/html/2511.01271v1#S3 "3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), when both the dimension NN and the sample size TT tend to infinity. We focus on the estimating equations with lags k=0k=0 and k=1k=1, which typically capture the majority of the cross-sectional and dynamic dependencies in the data. A constant CC is used generically, with its value potentially varying across different parts of the analysis. We begin with some assumptions.

###### Assumption 1.

The process {(𝐲t,𝐟t)}\{({\mathbf{y}}\_{t},{\mathbf{f}}\_{t})\} is strictly stationary and α\alpha-mixing with the mixing coefficient satisfying the condition ∑k=1∞αN​(k)1−2/γ<∞\sum\_{k=1}^{\infty}\alpha\_{N}(k)^{1-2/\gamma}<\infty for some γ>2\gamma>2, where

|  |  |  |
| --- | --- | --- |
|  | αN​(k)=supisupA∈ℱ−∞i,B∈ℱi+k∞|P​(A∩B)−P​(A)​P​(B)|,\alpha\_{N}(k)=\sup\_{i}\sup\_{A\in\mathcal{F}\_{-\infty}^{i},B\in\mathcal{F}\_{i+k}^{\infty}}|P(A\cap B)-P(A)P(B)|, |  |

and ℱij\mathcal{F}\_{i}^{j} is the σ\sigma-field generated by {(𝐲t,𝐟t):i≤t≤j}\{({\mathbf{y}}\_{t},{\mathbf{f}}\_{t}):i\leq t\leq j\}.

###### Assumption 2.

The spatial weight matrix 𝐖{\mathbf{W}} is known with zero main diagonal elements, and the matrix 𝐒N​(𝛒):=𝐈N−𝐃​(𝛒)​𝐖{\mathbf{S}}\_{N}(\boldsymbol{\rho}):={\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}} is invertible. The row and column sums of |𝐖||{\mathbf{W}}| and |𝐒N​(𝛒)−1||{\mathbf{S}}\_{N}(\boldsymbol{\rho})^{-1}| are bounded uniformly in NN.

###### Assumption 3.

{𝜺t}\{\mbox{$\varepsilon$}\_{t}\} is a white noise process satisfying Cov​(𝐲t−j,𝛆t)=𝟎\textnormal{Cov}({\mathbf{y}}\_{t-j},\mbox{$\varepsilon$}\_{t})={\bf 0} and Cov​(𝐟t−k,𝛆t)=𝟎\textnormal{Cov}({\mathbf{f}}\_{t-k},\mbox{$\varepsilon$}\_{t})={\bf 0}, for j≥1j\geq 1 and k≥0k\geq 0, respectively.

###### Assumption 4.

(i) If 𝐟t{\mathbf{f}}\_{t}’s are observed, each element in 𝐁{\mathbf{B}} are bounded uniformly in NN; (ii) If 𝐟t{\mathbf{f}}\_{t}’s are latent, the loading matrix 𝐁{\mathbf{B}} is of full rank
such that 1N​𝐁′​𝐒N′​(𝛒)−1​𝐒N​(𝛒)−1​𝐁=𝐈r\frac{1}{N}{\mathbf{B}}^{\prime}{\mathbf{S}}\_{N}^{\prime}(\boldsymbol{\rho})^{-1}{\mathbf{S}}\_{N}(\boldsymbol{\rho})^{-1}{\mathbf{B}}={\mathbf{I}}\_{r}, which is an identity matrix.

###### Assumption 5.

For 1≤j≤K1\leq j\leq K and 1≤k≤N1\leq k\leq N, E​|fj,t|2​γ<CE|f\_{j,t}|^{2\gamma}<C and E​|εk,t|2​γ<CE|{\varepsilon}\_{k,t}|^{2\gamma}<C, where γ\gamma is given in Assumption [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions").

###### Assumption 6.

For i=1,…,Ni=1,...,N, the rank of matrix 𝐗i′​𝐗i+λ​𝐈K+1{\mathbf{X}}\_{i}^{\prime}{\mathbf{X}}\_{i}+\lambda{\mathbf{I}}\_{K+1} is K+1K+1, for any λ>0\lambda>0, where

|  |  |  |
| --- | --- | --- |
|  | 𝐗i=(𝚺y​f′​𝐰i𝚺f′𝚺y​f′​(1)​𝐰i𝚺f′​(1)).{\mathbf{X}}\_{i}=\left(\begin{array}[]{cc}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}&\boldsymbol{\Sigma}\_{f}^{\prime}\\ \boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&\boldsymbol{\Sigma}\_{f}^{\prime}(1)\end{array}\right). |  |

Assumption [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") is standard for dependent random processes. See Gao et al. ([2019](https://arxiv.org/html/2511.01271v1#bib.bib20)) for a theoretical justification for VAR models. In fact, the assumption of strict stationarity can be removed and we only need to replace definitions of 𝚺y​(k)\boldsymbol{\Sigma}\_{y}(k) and 𝚺f​(k)\boldsymbol{\Sigma}\_{f}(k) with 1T​∑t=k+1TCov​(𝐲t,𝐟t−k)\frac{1}{T}\sum\_{t=k+1}^{T}\textnormal{Cov}({\mathbf{y}}\_{t},{\mathbf{f}}\_{t-k}) and 1T​∑t=k+1TCov​(𝐟t,𝐟t−k)\frac{1}{T}\sum\_{t=k+1}^{T}\textnormal{Cov}({\mathbf{f}}\_{t},{\mathbf{f}}\_{t-k}), respectively, and the results still hold throughout the paper. Assumption [2](https://arxiv.org/html/2511.01271v1#Thmassumption2 "Assumption 2. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") is commonly used in the spatial econometrics literature to limit the dependence across different locations or economic units; see, for example, Lee and Yu ([2010](https://arxiv.org/html/2511.01271v1#bib.bib33)). Assumption [3](https://arxiv.org/html/2511.01271v1#Thmassumption3 "Assumption 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") is weaker than the independence assumptions imposed in the spatial econometrics literature and we also allow for possible dependence between 𝐲t+j{\mathbf{y}}\_{t+j} and 𝐟t+k{\mathbf{f}}\_{t+k} and past lagged of noises, for j≥0j\geq 0 and k≥1k\geq 1.
Assumption [4](https://arxiv.org/html/2511.01271v1#Thmassumption4 "Assumption 4. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") is standard for the loading matrix under the scenarios when the factors are either observed or latent. Assumption [5](https://arxiv.org/html/2511.01271v1#Thmassumption5 "Assumption 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") imposes some moment conditions on the factors and noise terms. It is not hard to see that E​|yi,t|2​γ<CE|y\_{i,t}|^{2\gamma}<C under Assumptions [2](https://arxiv.org/html/2511.01271v1#Thmassumption2 "Assumption 2. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), [4](https://arxiv.org/html/2511.01271v1#Thmassumption4 "Assumption 4. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")
and [5](https://arxiv.org/html/2511.01271v1#Thmassumption5 "Assumption 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). Furthermore, this also implies that E​|𝐰i′​𝚺y​f​𝐟t|2​γ<CE|{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}{\mathbf{f}}\_{t}|^{2\gamma}<C, E​|𝐰i′​𝚺y​f​(1)​𝐟t−1|2​γ<CE|{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1){\mathbf{f}}\_{t-1}|^{2\gamma}<C, E​‖𝚺f​𝐟t‖22​γ<CE\|\boldsymbol{\Sigma}\_{f}{\mathbf{f}}\_{t}\|\_{2}^{2\gamma}<C, and E​‖𝚺f​(1)​𝐟t−1‖22​γ<CE\|\boldsymbol{\Sigma}\_{f}(1){\mathbf{f}}\_{t-1}\|\_{2}^{2\gamma}<C, which are used to establish the convergence of the variance of 𝐒N,T{\mathbf{S}}\_{N,T}, as defined in ([IA.8](https://arxiv.org/html/2511.01271v1#S1.E8 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) of the online Appendix. Assumption [6](https://arxiv.org/html/2511.01271v1#Thmassumption6 "Assumption 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") ensures that the ridge solutions in ([12](https://arxiv.org/html/2511.01271v1#S3.E12 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) and ([19](https://arxiv.org/html/2511.01271v1#S3.E19 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) are well-defined.

Now, we present the asymptotic properties of 𝜷^i\widehat{\boldsymbol{\beta}}\_{i}, for i=1,…,Ni=1,\dots,N.

###### Theorem 2.

Let Assumptions [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") −- [6](https://arxiv.org/html/2511.01271v1#Thmassumption6 "Assumption 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") hold.
  
(i) If N=o​(T)N=o(T), we have

|  |  |  |
| --- | --- | --- |
|  | ‖𝜷^i​(λi)−𝐗^i​(λi)−1​𝐗^i​𝐗^i′​𝜷i‖2=Op​(T−1/2),i=1,…,N,\|\widehat{\boldsymbol{\beta}}\_{i}(\lambda\_{i})-\widehat{\mathbf{X}}\_{i}(\lambda\_{i})^{-1}\widehat{\mathbf{X}}\_{i}\widehat{\mathbf{X}}\_{i}^{\prime}\boldsymbol{\beta}\_{i}\|\_{2}=O\_{p}(T^{-1/2}),\quad i=1,...,N, |  |

as N,T→∞N,T\rightarrow\infty, where 𝐗^i​(λi)=𝐗^i′​𝐗^i+λi​𝐈K+1\widehat{\mathbf{X}}\_{i}(\lambda\_{i})=\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i}+\lambda\_{i}{\mathbf{I}}\_{K+1}.
  
(ii) If N=o​(T)N=o(T) and let λi→0\lambda\_{i}\rightarrow 0, we have

|  |  |  |
| --- | --- | --- |
|  | ‖(𝐗^i′​𝐗^i)​(𝜷^i−𝜷i)‖2=Op​(T−1/2),i=1,…,N,\|(\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i})(\widehat{\boldsymbol{\beta}}\_{i}-\boldsymbol{\beta}\_{i})\|\_{2}=O\_{p}(T^{-1/2}),\quad i=1,...,N, |  |

as N,T→∞N,T\rightarrow\infty.

Theorem [2](https://arxiv.org/html/2511.01271v1#Thmtheorem2 "Theorem 2. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") implies that the ridge estimator for 𝜷\boldsymbol{\beta} is biased, which is a common issue in ridge estimation. However, we can establish the joint convergence of ρ^i\widehat{\rho}\_{i} and 𝐛i{\mathbf{b}}\_{i}, as stated in Theorem [2](https://arxiv.org/html/2511.01271v1#Thmtheorem2 "Theorem 2. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")(ii). Since ρi\rho\_{i} and 𝐛i{\mathbf{b}}\_{i} represent loadings for all possible factors, this result is useful because these coefficients can be jointly estimated and inferred in many economic contexts, such as financial networks, as described in Wang and Shojaie ([2021](https://arxiv.org/html/2511.01271v1#bib.bib47)).

Next, we provide the joint limiting distributions of the shrinkage estimators. For i=1,…,Ni=1,...,N, define

|  |  |  |
| --- | --- | --- |
|  | 𝚺f​εi​(0,0)=Cov​(𝐟t​εi,t,𝐟t​εi,t),𝚺f​εi​(1,0)=Cov​(𝐟t​εi,t,𝐟t−1​εi,t),𝛀f​εi​(0,0)=Cov​(𝐟t−1​εi,t,𝐟t−1​εi,t),\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0,0)=\textnormal{Cov}({\mathbf{f}}\_{t}{\varepsilon}\_{i,t},{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}),\,\,\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1,0)=\textnormal{Cov}({\mathbf{f}}\_{t}{\varepsilon}\_{i,t},{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}),\,\,\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0,0)=\textnormal{Cov}({\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t},{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}), |  |

|  |  |  |
| --- | --- | --- |
|  | 𝚺f​εi​(k,j)=Cov​(𝐟t+j​εi,t+j,𝐟t−k​εi,t)+Cov​(𝐟t​εi,t,𝐟t−k+j​εi,t+j),j≥1,k≥0,\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(k,j)=\textnormal{Cov}({\mathbf{f}}\_{t+j}{\varepsilon}\_{i,t+j},{\mathbf{f}}\_{t-k}{\varepsilon}\_{i,t})+\textnormal{Cov}({\mathbf{f}}\_{t}{\varepsilon}\_{i,t},{\mathbf{f}}\_{t-k+j}{\varepsilon}\_{i,t+j}),\,\,j\geq 1,k\geq 0, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝛀f​εi​(0,j)=Cov​(𝐟t−1+j​εi,t+j,𝐟t−1​εi,t)+Cov​(𝐟t−1​εi,t,𝐟t−1+j​εi,t+j),j≥1,\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0,j)=\textnormal{Cov}({\mathbf{f}}\_{t-1+j}{\varepsilon}\_{i,t+j},{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t})+\textnormal{Cov}({\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t},{\mathbf{f}}\_{t-1+j}{\varepsilon}\_{i,t+j}),\quad j\geq 1, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝚺f​εi​(0)=∑j=0∞𝚺f​εi​(0,j),𝚺f​εi​(1)=∑j=0∞𝚺f​εi​(1,j),𝛀f​εi​(0)=∑j=0∞𝛀f​εi​(0,j).\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0)=\sum\_{j=0}^{\infty}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0,j),\,\,\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1)=\sum\_{j=0}^{\infty}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1,j),\,\,\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0)=\sum\_{j=0}^{\infty}\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0,j). |  |

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐕i=(𝐰i′​𝚺y​f​𝚺y​f′​𝐰i+𝐰i′​𝚺y​f​(1)​𝚺y​f′​(1)​𝐰i𝐰i′​𝚺y​f​𝚺f+𝐰i′​𝚺y​f​(1)​𝚺f′​(1)𝚺f​𝚺y​f′​𝐰i+𝚺f​(1)​𝚺y​f′​(1)​𝐰i𝚺f2+𝚺f​(1)​𝚺f′​(1)){\mathbf{V}}\_{i}=\left(\begin{array}[]{cc}{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1)\\ \boldsymbol{\Sigma}\_{f}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}+\boldsymbol{\Sigma}\_{f}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&\boldsymbol{\Sigma}\_{f}^{2}+\boldsymbol{\Sigma}\_{f}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1)\end{array}\right) |  | (23) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐔i=(𝚺f​εi​(0)𝚺f​εi​(1)𝚺f​εi′​(1)𝛀f​εi​(0)).{\mathbf{U}}\_{i}=\left(\begin{array}[]{cc}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0)&\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1)\\ \boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}^{\prime}(1)&\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0)\end{array}\right). |  | (24) |

The following theorem establishes the joint asymptotic normality of the estimators.

###### Theorem 3.

Let Assumptions [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") −- [6](https://arxiv.org/html/2511.01271v1#Thmassumption6 "Assumption 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") hold. If N=o​(T)N=o(T) and λi→0\lambda\_{i}\rightarrow 0, we have

|  |  |  |
| --- | --- | --- |
|  | T​𝐕i​(𝜷^i−𝜷i)⟶dN​(𝟎,𝐗i′​𝐔i​𝐗i),\sqrt{T}{\mathbf{V}}\_{i}(\widehat{\boldsymbol{\beta}}\_{i}-\boldsymbol{\beta}\_{i})\longrightarrow\_{d}N({\bf 0},{\mathbf{X}}\_{i}^{\prime}{\mathbf{U}}\_{i}{\mathbf{X}}\_{i}), |  |

for i=1,…,Ni=1,...,N as N,T→∞N,T\rightarrow\infty, where 𝐔i{\mathbf{U}}\_{i} and 𝐕i{\mathbf{V}}\_{i} are defined in ([24](https://arxiv.org/html/2511.01271v1#S4.E24 "In 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) and ([23](https://arxiv.org/html/2511.01271v1#S4.E23 "In 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), respectively.

From Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we see that the Yule-Walker estimators obtained in ([12](https://arxiv.org/html/2511.01271v1#S3.E12 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) are asymptotically normal when the dimension NN diverges. The convergence rate is the standard T\sqrt{T} under the assumption that N/T→0N/T\rightarrow 0, which is a similar requirement in spatial panel dynamic models; see Yu et al. ([2008](https://arxiv.org/html/2511.01271v1#bib.bib49)), among others. The condition N/T→0N/T\rightarrow 0 is weaker than the one in Gao et al. ([2019](https://arxiv.org/html/2511.01271v1#bib.bib20)), where N/T→0N/\sqrt{T}\rightarrow 0 is required, because we assume the dimension of 𝐟t{\mathbf{f}}\_{t} is KK, a finite integer. The convergence of 𝚺^y​f​(k)\widehat{\boldsymbol{\Sigma}}\_{yf}(k) to 𝚺y​f​(k)\boldsymbol{\Sigma}\_{yf}(k) only requires N/T→0N/T\rightarrow 0, whereas the convergence of 𝚺^y​(k)=1T​∑t=k+1T𝐲t​𝐲t−k′\widehat{\boldsymbol{\Sigma}}\_{y}(k)=\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{y}}\_{t}{\mathbf{y}}\_{t-k}^{\prime} to its population version requires N/T→0N/\sqrt{T}\rightarrow 0 as stated in Gao et al. ([2019](https://arxiv.org/html/2511.01271v1#bib.bib20)).
By the form of 𝐗i{\mathbf{X}}\_{i} in Assumption [6](https://arxiv.org/html/2511.01271v1#Thmassumption6 "Assumption 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we can show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐗i′​𝐔i​𝐗i=(𝚺i,11𝚺i,12𝚺i,21𝚺i,22),{\mathbf{X}}\_{i}^{\prime}{\mathbf{U}}\_{i}{\mathbf{X}}\_{i}=\left(\begin{array}[]{cc}\boldsymbol{\Sigma}\_{i,11}&\boldsymbol{\Sigma}\_{i,12}\\ \boldsymbol{\Sigma}\_{i,21}&\boldsymbol{\Sigma}\_{i,22}\end{array}\right), |  | (25) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺i,11=\displaystyle\boldsymbol{\Sigma}\_{i,11}= | 𝐰i′​𝚺y​f​𝚺f​εi​(0)​𝚺y​f′​𝐰i+𝐰i′​𝚺y​f​𝚺f​εi​(1)​𝚺y​f′​(1)​𝐰i+𝐰i′​𝚺y​f​(1)​𝚺f​εi′​(1)​𝚺y​f′​𝐰i\displaystyle{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}^{\prime}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝐰i′​𝚺y​f​(1)​𝛀f​εi​(0)​𝚺y​f′​(1)​𝐰i,\displaystyle+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺i,22=\displaystyle\boldsymbol{\Sigma}\_{i,22}= | 𝚺f​𝚺f​εi​(0)​𝚺f+𝚺f​𝚺f​εi​(1)​𝚺f′​(1)+𝚺f​(1)​𝚺f​εi′​(1)​𝚺f+𝚺f​(1)​Ωf​εi​(0)​𝚺f′​(1),\displaystyle\boldsymbol{\Sigma}\_{f}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{f}+\boldsymbol{\Sigma}\_{f}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1)+\boldsymbol{\Sigma}\_{f}(1)\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}^{\prime}(1)\boldsymbol{\Sigma}\_{f}+\boldsymbol{\Sigma}\_{f}(1)\Omega\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{f}^{\prime}(1), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺i,12=\displaystyle\boldsymbol{\Sigma}\_{i,12}= | 𝐰i′​𝚺y​f​𝚺f​εi​(0)​𝚺f+𝐰i′​𝚺y​f​𝚺f​εi​(1)​𝚺f′​(1)+𝐰i′​𝚺y​f​(1)​𝚺f​εi′​(1)​𝚺f\displaystyle{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{f}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1)+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}^{\prime}(1)\boldsymbol{\Sigma}\_{f} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝐰i′​𝚺y​f​(1)​𝛀f​εi​(0)​𝚺f′​(1),\displaystyle+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{f}^{\prime}(1), |  |

and 𝚺i,21=𝚺i,12′\boldsymbol{\Sigma}\_{i,21}=\boldsymbol{\Sigma}\_{i,12}^{\prime}. These matries can all be estimated from the data.

Finally, we turn to the case when the factors are latent. We need to make two more assumptions to establish the uniform convergence and the limiting distributions of the estimated factors.

###### Assumption 7.

𝐟t{\mathbf{f}}\_{t} and 𝛆t\mbox{$\varepsilon$}\_{t} are sub-exponentially distributed in the sense that

|  |  |  |
| --- | --- | --- |
|  | P​(|𝐯1′​𝐟t|>x)≤C​exp⁡(−C​x),and​P​(|𝐯2′​𝜺t|>x)≤C​exp⁡(−C​x),P(|{\mathbf{v}}\_{1}^{\prime}{\mathbf{f}}\_{t}|>x)\leq C\exp(-Cx),\,\,\text{and}\,\,P(|{\mathbf{v}}\_{2}^{\prime}\mbox{$\varepsilon$}\_{t}|>x)\leq C\exp(-Cx), |  |

for any x>0x>0, where ‖𝐯1‖2=1\|{\mathbf{v}}\_{1}\|\_{2}=1 and ‖𝐯2‖2=1\|{\mathbf{v}}\_{2}\|\_{2}=1 are any two constant vectors.

###### Assumption 8.

For each t=1,…,Tt=1,...,T, as N→∞N\rightarrow\infty,

|  |  |  |
| --- | --- | --- |
|  | 1N​∑i=1N𝐩i​εi,t⟶dN​(0,𝚪t),\frac{1}{\sqrt{N}}\sum\_{i=1}^{N}{\mathbf{p}}\_{i}{\varepsilon}\_{i,t}\longrightarrow\_{d}N(0,\boldsymbol{\Gamma}\_{t}), |  |

where 𝐩i{\mathbf{p}}\_{i} is the iith column of 𝚲′​(𝐈N−𝐃​(𝛒)​𝐖)−1\boldsymbol{\Lambda}^{\prime}({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}, and 𝚪t=limN→∞1N​∑i=1N∑j=1N𝐩i​𝐩j′​E​(εi,t​εj,t)\boldsymbol{\Gamma}\_{t}=\lim\_{N\rightarrow\infty}\frac{1}{N}\sum\_{i=1}^{N}\sum\_{j=1}^{N}{\mathbf{p}}\_{i}{\mathbf{p}}\_{j}^{\prime}E({\varepsilon}\_{i,t}{\varepsilon}\_{j,t}) in probability.

Assumption [7](https://arxiv.org/html/2511.01271v1#Thmassumption7 "Assumption 7. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") is commonly used in the statistical and econometrics literature to establish uniform convergence. The sub-exponential distribution is a broader class of distributions than the sub-Gaussian distribution and includes the uniform distribution over every convex body, following the Brunn-Minkowski inequality. For further details, see, for example, Vershynin ([2018](https://arxiv.org/html/2511.01271v1#bib.bib46)). Assumption [8](https://arxiv.org/html/2511.01271v1#Thmassumption8 "Assumption 8. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") is similar to Assumption F(3) in Bai ([2003](https://arxiv.org/html/2511.01271v1#bib.bib5)), which is used to establish the limiting distribution of the estimated factors.

We first state the convergence of the estimated loading matrix below, where we introduce a rotational matrix 𝐇N​T{\mathbf{H}}\_{NT} in the proof of the following theorem. This approach differs from the techniques used in Lam et al. ([2011](https://arxiv.org/html/2511.01271v1#bib.bib31)).

###### Theorem 4.

Let Assumptions [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") −- [6](https://arxiv.org/html/2511.01271v1#Thmassumption6 "Assumption 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") hold. If N=o​(T)N=o(T), then there exists an invertible matrix 𝐇N​T{\mathbf{H}}\_{NT} such that

|  |  |  |
| --- | --- | --- |
|  | 1N​‖𝚲^−𝚲​𝐇N​T′‖F=Op​(1T).\frac{1}{\sqrt{N}}\|\widehat{\boldsymbol{\Lambda}}-\boldsymbol{\Lambda}{\mathbf{H}}\_{NT}^{\prime}\|\_{F}=O\_{p}(\frac{1}{\sqrt{T}}). |  |

###### Remark 1.

(i) Unlike the proof in Lam et al. ([2011](https://arxiv.org/html/2511.01271v1#bib.bib31)) where a matrix perturbation theory is used to show the convergence of the estimated loading matrix, we developed a new approach in the Appendix to show the convergence rate of 𝚲^\widehat{\boldsymbol{\Lambda}}. One of the advantages of the new approach is that we can specify the rotational matrix 𝐇N​T{\mathbf{H}}\_{NT} which is defined as

|  |  |  |
| --- | --- | --- |
|  | 𝐇N​T′=∑k=1k0𝐆1,k​𝐆1,k′​𝚲′​𝚲^​𝐕^N​T−1,where​𝐆1,k=1T​∑t=k+1T(𝐟t​𝐟t−k′​𝚲′+𝐟t​𝝃t−k′),{\mathbf{H}}\_{NT}^{\prime}=\sum\_{k=1}^{k\_{0}}{\mathbf{G}}\_{1,k}{\mathbf{G}}\_{1,k}^{\prime}\boldsymbol{\Lambda}^{\prime}\widehat{\boldsymbol{\Lambda}}\widehat{\mathbf{V}}\_{NT}^{-1},\,\text{where}\,\,{\mathbf{G}}\_{1,k}=\frac{1}{T}\sum\_{t=k+1}^{T}({\mathbf{f}}\_{t}{\mathbf{f}}\_{t-k}^{\prime}\boldsymbol{\Lambda}^{\prime}+{\mathbf{f}}\_{t}\boldsymbol{\xi}\_{t-k}^{\prime}), |  |

and 𝐕^N​T∈Rr\widehat{\mathbf{V}}\_{NT}\in R^{r} is a diagonal matrix with diagonal elements being the top KK eigenvalues of 𝐌^\widehat{\mathbf{M}}. See the proof of Theorem [4](https://arxiv.org/html/2511.01271v1#Thmtheorem4 "Theorem 4. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") in the online Appendix for details.
  
(ii) Note that we impose that 𝚲′​𝚲/N=𝐈r\boldsymbol{\Lambda}^{\prime}\boldsymbol{\Lambda}/N={\mathbf{I}}\_{r}, whereas Lam et al. ([2011](https://arxiv.org/html/2511.01271v1#bib.bib31)) assumes that 𝚲′​𝚲=𝐈r\boldsymbol{\Lambda}^{\prime}\boldsymbol{\Lambda}={\mathbf{I}}\_{r}. Therefore, the convergence rate is the same as the one in Theorem 1 of Lam et al. ([2011](https://arxiv.org/html/2511.01271v1#bib.bib31)), where we assume δ=0\delta=0 in our paper, corresponding to the case of strong factors.

Next, we establish the uniform convergence of the estimated factors and the corresponding limiting distributions.

###### Theorem 5.

Let Assumptions [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") −- [6](https://arxiv.org/html/2511.01271v1#Thmassumption6 "Assumption 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") hold.
  
(i) If 𝛆t\mbox{$\varepsilon$}\_{t} and 𝐟t{\mathbf{f}}\_{t} are sub-exponentially distributed as in Assumption [7](https://arxiv.org/html/2511.01271v1#Thmassumption7 "Assumption 7. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), then there exists an invertible matrix 𝐊N​T∈ℝr{\mathbf{K}}\_{NT}\in\mathbb{R}^{r} such that

|  |  |  |
| --- | --- | --- |
|  | max1≤t≤T⁡‖𝐟^t−𝐊N​T​𝐟t‖2=Op​{(1N+1T)​log⁡(T)}.\max\_{1\leq t\leq T}\|\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t}\|\_{2}=O\_{p}\{(\frac{1}{\sqrt{N}}+\frac{1}{\sqrt{T}})\log(T)\}. |  |

(ii) Let Assumption [8](https://arxiv.org/html/2511.01271v1#Thmassumption8 "Assumption 8. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") also hold. If N=o​(T)N=o(T), then there exists an invertible matrix 𝐊N​T∈ℝr{\mathbf{K}}\_{NT}\in\mathbb{R}^{r} and its limit 𝐇∈ℝr{\mathbf{H}}\in\mathbb{R}^{r} such that

|  |  |  |
| --- | --- | --- |
|  | N​(𝐟^t−𝐊N​T​𝐟t)=𝐇​1N​∑i=1N𝐩i​εi,t+op​(1)⟶dN​(0,𝐇​𝚪t​𝐇′),\sqrt{N}(\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t})={\mathbf{H}}\frac{1}{\sqrt{N}}\sum\_{i=1}^{N}{\mathbf{p}}\_{i}{\varepsilon}\_{i,t}+o\_{p}(1)\longrightarrow\_{d}N(0,{\mathbf{H}}\boldsymbol{\Gamma}\_{t}{\mathbf{H}}^{\prime}), |  |

where 𝐩i{\mathbf{p}}\_{i} is the iith column of 𝚲′​(𝐈N−𝐃​(𝛒)​𝐖)−1\boldsymbol{\Lambda}^{\prime}({\mathbf{I}}\_{N}-{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}})^{-1}, 𝐇{\mathbf{H}} is the limit of 𝐇N​T{\mathbf{H}}\_{NT} as shown in Lemma 2 of the online Appendix, and 𝚪t\boldsymbol{\Gamma}\_{t} is defined as in Assumption [8](https://arxiv.org/html/2511.01271v1#Thmassumption8 "Assumption 8. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions").

###### Remark 2.

(I) A remarkable feature in Theorem [5](https://arxiv.org/html/2511.01271v1#Thmtheorem5 "Theorem 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") is that we only require N/T→0N/T\to 0, and the asymptotic normality of 𝐟t{\mathbf{f}}\_{t} can still be achieved.
  
(ii) Note that we adopt the matrix 𝐊N​T{\mathbf{K}}\_{NT} as a rotational matrix for 𝐟t{\mathbf{f}}\_{t}, which is defined as

|  |  |  |
| --- | --- | --- |
|  | 𝐊N​T=1N​𝚲^′​𝚲.{\mathbf{K}}\_{NT}=\frac{1}{N}\widehat{\boldsymbol{\Lambda}}^{\prime}\boldsymbol{\Lambda}. |  |

See the proof of Theorem [5](https://arxiv.org/html/2511.01271v1#Thmtheorem5 "Theorem 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") in the Appendix. In fact, according to Lemma 1 of the Appendix, we may replace 𝐊N​T{\mathbf{K}}\_{NT} by 𝐇N​T{\mathbf{H}}\_{NT}, and the results in Theorem [5](https://arxiv.org/html/2511.01271v1#Thmtheorem5 "Theorem 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") still hold. This can be shown by rewriting the term 1N​𝚲^′​𝚲​𝐟t\frac{1}{N}\widehat{\boldsymbol{\Lambda}}^{\prime}\boldsymbol{\Lambda}{\mathbf{f}}\_{t} in ([IA.19](https://arxiv.org/html/2511.01271v1#S1.E19 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) as

|  |  |  |
| --- | --- | --- |
|  | 1N​(𝚲^−𝚲​𝐇N​T′)′​𝚲​𝐟t+𝐇N​T​𝐟t,\frac{1}{N}(\widehat{\boldsymbol{\Lambda}}-\boldsymbol{\Lambda}{\mathbf{H}}\_{NT}^{\prime})^{\prime}\boldsymbol{\Lambda}{\mathbf{f}}\_{t}+{\mathbf{H}}\_{NT}{\mathbf{f}}\_{t}, |  |

where the first term is still asymptotically negligible. However, we do not adopt this formula since it will introduce a bias term in establishing the limiting distributions of the 𝐟^t\widehat{\mathbf{f}}\_{t}. Nevertheless, it is not hard to show that 𝐊N​T{\mathbf{K}}\_{NT} and 𝐇N​T{\mathbf{H}}\_{NT} have the same limit as N,T→∞N,T\to\infty.

Furthermore, we study the limiting distributions of the estimated parameters in ([19](https://arxiv.org/html/2511.01271v1#S3.E19 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). Similar to the case when the factors are observable, we provide some notation used in the following Theorem. Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐕iH=(𝐰i′​𝚺y​f​𝚺y​f′​𝐰i+𝐰i′​𝚺y​f​(1)​𝚺y​f′​(1)​𝐰i𝐰i′​𝚺y​f​𝚺f​𝐇′+𝐰i′​𝚺y​f​(1)​𝚺f′​(1)​𝐇′𝐇​𝚺f​𝚺y​f′​𝐰i+𝐇​𝚺f​(1)​𝚺y​f′​(1)​𝐰i𝐇​𝚺f2​𝐇′+𝐇​𝚺f​(1)​𝚺f′​(1)​𝐇′){\mathbf{V}}\_{i}^{H}=\left(\begin{array}[]{cc}{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f}{\mathbf{H}}^{\prime}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1){\mathbf{H}}^{\prime}\\ {\mathbf{H}}\boldsymbol{\Sigma}\_{f}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}+{\mathbf{H}}\boldsymbol{\Sigma}\_{f}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&{\mathbf{H}}\boldsymbol{\Sigma}\_{f}^{2}{\mathbf{H}}^{\prime}+{\mathbf{H}}\boldsymbol{\Sigma}\_{f}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1){\mathbf{H}}^{\prime}\end{array}\right) |  | (26) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐔iH=(𝐇​𝚺f​εi​(0)​𝐇′𝐇​𝚺f​εi​(1)​𝐇′𝐇​𝚺f​εi′​(1)​𝐇′𝐇​𝛀f​εi​(0)​𝐇′).{\mathbf{U}}\_{i}^{H}=\left(\begin{array}[]{cc}{\mathbf{H}}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0){\mathbf{H}}^{\prime}&{\mathbf{H}}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1){\mathbf{H}}^{\prime}\\ {\mathbf{H}}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}^{\prime}(1){\mathbf{H}}^{\prime}&{\mathbf{H}}\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0){\mathbf{H}}^{\prime}\end{array}\right). |  | (27) |

The following theorem establishes the asymptotic normality of the estimators in ([19](https://arxiv.org/html/2511.01271v1#S3.E19 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) when the factors are latent and the dimension NN is diverging.

###### Theorem 6.

Let Assumptions [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") −- [8](https://arxiv.org/html/2511.01271v1#Thmassumption8 "Assumption 8. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") hold.
  
(i) If N=o​(T)N=o(T) and T=o​(N)\sqrt{T}=o(N), then there exists an invertible matrix 𝐊N​T∈Rr{\mathbf{K}}\_{NT}\in R^{r} such that

|  |  |  |
| --- | --- | --- |
|  | 𝜷~i​(λi)−𝐗~i​(λi)−1​𝐗~i′​𝐗~i​𝐊N​T∗​𝜷i=Op​(T−1/2),\widetilde{\boldsymbol{\beta}}\_{i}(\lambda\_{i})-\widetilde{\mathbf{X}}\_{i}(\lambda\_{i})^{-1}\widetilde{\mathbf{X}}\_{i}^{\prime}\widetilde{\mathbf{X}}\_{i}{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{i}=O\_{p}(T^{-1/2}), |  |

where 𝐗~i​(λi)=𝐗~i′​𝐗~i+λi​𝐈K+1\widetilde{\mathbf{X}}\_{i}(\lambda\_{i})=\widetilde{\mathbf{X}}\_{i}^{\prime}\widetilde{\mathbf{X}}\_{i}+\lambda\_{i}{\mathbf{I}}\_{K+1}.
  
(ii) If N=o​(T)N=o(T) and T=o​(N)\sqrt{T}=o(N), let λi→0\lambda\_{i}\rightarrow 0, there exists an invertible matrix 𝐊N​T∈Rr{\mathbf{K}}\_{NT}\in R^{r} such that

|  |  |  |
| --- | --- | --- |
|  | T​𝐕iH​(𝜷~i−𝐊N​T∗​𝜷i)⟶dN​(𝟎,𝐗iH​𝐔iH′​𝐗iH),\sqrt{T}{\mathbf{V}}\_{i}^{H}(\widetilde{\boldsymbol{\beta}}\_{i}-{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{i})\longrightarrow\_{d}N({\bf 0},{\mathbf{X}}\_{i}^{H}{{}^{\prime}}{\mathbf{U}}\_{i}^{H}{\mathbf{X}}\_{i}^{H}), |  |

for i=1,…,Ni=1,...,N as T→∞T\rightarrow\infty, where 𝐊N​T∗=diag​(1,(𝐊N​T′)−1){\mathbf{K}}\_{NT}^{\*}=\mbox{diag}(1,({\mathbf{K}}\_{NT}^{\prime})^{-1}) is a block-diagonal matrix, and 𝐔iH{\mathbf{U}}\_{i}^{H} and 𝐕iH{\mathbf{V}}\_{i}^{H} are defined in ([27](https://arxiv.org/html/2511.01271v1#S4.E27 "In 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) and ([26](https://arxiv.org/html/2511.01271v1#S4.E26 "In 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), respectively, and

|  |  |  |
| --- | --- | --- |
|  | 𝐗iH=(𝐇​𝚺y​f′​𝐰i𝐇​𝚺f​𝐇′𝐇​𝚺y​f′​(1)​𝐰i𝐇​𝚺f′​(1)​𝐇′).{\mathbf{X}}\_{i}^{H}=\left(\begin{array}[]{cc}{\mathbf{H}}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}&{\mathbf{H}}\boldsymbol{\Sigma}\_{f}{\mathbf{H}}^{\prime}\\ {\mathbf{H}}\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&{\mathbf{H}}\boldsymbol{\Sigma}\_{f}^{\prime}(1){\mathbf{H}}^{\prime}\end{array}\right). |  |

###### Remark 3.

(i) From Theorem [6](https://arxiv.org/html/2511.01271v1#Thmtheorem6 "Theorem 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we see that the convergence rate is still the standard T\sqrt{T}, which is the same as that in Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") when the factors are observable. On the other hand, we note that the scalar coefficient can be uniquely determined, but the coefficient vector 𝐛i{\mathbf{b}}\_{i} can be estimated up to a rotational matrix 𝐊N​T{\mathbf{K}}\_{NT}, which is reasonable due to the identification issue in the factor analysis.
  
(ii) Recall that this is a two-step procedure. The statistical inference is usually difficult to establish in the second step because the errors incurred in the first step sometimes create a biased term. As discussed in Remark 2(ii), we adopt a rotational matrix 𝐊N​T{\mathbf{K}}\_{NT} instead of 𝐇N​T{\mathbf{H}}\_{NT} in Theorems [5](https://arxiv.org/html/2511.01271v1#Thmtheorem5 "Theorem 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") and [6](https://arxiv.org/html/2511.01271v1#Thmtheorem6 "Theorem 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") such that the bias term can be erased, although 𝐊N​T{\mathbf{K}}\_{NT} and 𝐇N​T{\mathbf{H}}\_{NT} have the same limit. See the proof of Theorem [6](https://arxiv.org/html/2511.01271v1#Thmtheorem6 "Theorem 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") in the online Appendix for details.

It can be easily shown that the variance term in Theorem [6](https://arxiv.org/html/2511.01271v1#Thmtheorem6 "Theorem 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")(ii) can be expressed as

|  |  |  |
| --- | --- | --- |
|  | 𝐗iH​𝐔iH′​𝐗iH=(𝚺i,11H𝚺i,12H𝚺i,21H𝚺i,22H),{\mathbf{X}}\_{i}^{H}{{}^{\prime}}{\mathbf{U}}\_{i}^{H}{\mathbf{X}}\_{i}^{H}=\left(\begin{array}[]{cc}\boldsymbol{\Sigma}\_{i,11}^{H}&\boldsymbol{\Sigma}\_{i,12}^{H}\\ \boldsymbol{\Sigma}\_{i,21}^{H}&\boldsymbol{\Sigma}\_{i,22}^{H}\end{array}\right), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺i,11H=\displaystyle\boldsymbol{\Sigma}\_{i,11}^{H}= | 𝐰i′​𝚺y​f​𝚺f​εi​(0)​𝚺y​f′​𝐰i+𝐰i′​𝚺y​f​𝚺f​εi​(1)​𝚺y​f′​(1)​𝐰i+𝐰i′​𝚺y​f​(1)​𝚺f​εi′​(1)​𝚺y​f′​𝐰i\displaystyle{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}^{\prime}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝐰i′​𝚺y​f​(1)​𝛀f​εi​(0)​𝚺y​f′​(1)​𝐰i,\displaystyle+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺i,22H=\displaystyle\boldsymbol{\Sigma}\_{i,22}^{H}= | 𝐇​𝚺f​𝚺f​εi​(0)​𝚺f​𝐇′+𝐇​𝚺f​𝚺f​εi​(1)​𝚺f′​(1)​𝐇′+𝐇​𝚺f​(1)​𝚺f​εi′​(1)​𝚺f​𝐇′+𝐇​𝚺f​(1)​Ωf​εi​(0)​𝚺f′​(1)​𝐇′,\displaystyle{\mathbf{H}}\boldsymbol{\Sigma}\_{f}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{f}{\mathbf{H}}^{\prime}+{\mathbf{H}}\boldsymbol{\Sigma}\_{f}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1){\mathbf{H}}^{\prime}+{\mathbf{H}}\boldsymbol{\Sigma}\_{f}(1)\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}^{\prime}(1)\boldsymbol{\Sigma}\_{f}{\mathbf{H}}^{\prime}+{\mathbf{H}}\boldsymbol{\Sigma}\_{f}(1)\Omega\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{f}^{\prime}(1){\mathbf{H}}^{\prime}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺i,12H=\displaystyle\boldsymbol{\Sigma}\_{i,12}^{H}= | 𝐰i′​𝚺y​f​𝚺f​εi​(0)​𝚺f​𝐇′+𝐰i′​𝚺y​f​𝚺f​εi​(1)​𝚺f′​(1)​𝐇′+𝐰i′​𝚺y​f​(1)​𝚺f​εi′​(1)​𝚺f​𝐇′\displaystyle{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{f}{\mathbf{H}}^{\prime}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1){\mathbf{H}}^{\prime}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}^{\prime}(1)\boldsymbol{\Sigma}\_{f}{\mathbf{H}}^{\prime} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝐰i′​𝚺y​f​(1)​𝛀f​εi​(0)​𝚺f′​(1)​𝐇′,\displaystyle+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0)\boldsymbol{\Sigma}\_{f}^{\prime}(1){\mathbf{H}}^{\prime}, |  |

and 𝚺i,21H=𝚺i,12H′\boldsymbol{\Sigma}\_{i,21}^{H}=\boldsymbol{\Sigma}\_{i,12}^{H}{{}^{\prime}}.

The consistency of the estimated number of factors using the information criterion in ([20](https://arxiv.org/html/2511.01271v1#S3.E20 "In 3.5 Selecting the Number of Factors and the Penalty Parameters ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) or the ratio-based method in ([21](https://arxiv.org/html/2511.01271v1#S3.E21 "In 3.5 Selecting the Number of Factors and the Penalty Parameters ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) can be established by a standard argument as that in Bai and Ng ([2002](https://arxiv.org/html/2511.01271v1#bib.bib7)) or Ahn and Horenstein ([2013](https://arxiv.org/html/2511.01271v1#bib.bib2)). We omit the details.

###### Remark 4.

In the estimation procedure above, we primarily focus on the augmented method by stacking factor lags for k=0k=0 and k=1k=1. In fact, ridge regression can be applied by taking any finite number of lagged factors in the Yule-Walker estimation. The theory can be established in a similar way.

###### Remark 5.

The QMLE method proposed in Aquaro et al. ([2021](https://arxiv.org/html/2511.01271v1#bib.bib4)) and Hu et al. ([2023](https://arxiv.org/html/2511.01271v1#bib.bib28)) can yield pointwise consistent estimators but is feasible only when the dimension NN is small and fixed. Additionally, they only focus on cases when the factors are observable. As NN increases, additional bias can arise, and the asymptotic results do not hold anymore (see Remarks 6–7 in Aquaro et al. ([2021](https://arxiv.org/html/2511.01271v1#bib.bib4))). Moreover, the computational cost of the QMLE method becomes prohibitive for large NN. In contrast, the proposed generalized Yule-Walker method is designed to handle scenarios with large or diverging NN while remaining computationally efficient. Simulations and real data analyses in Sections [5](https://arxiv.org/html/2511.01271v1#S5 "5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")-[6](https://arxiv.org/html/2511.01271v1#S6 "6 Empirical Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") show that the proposed method can even outperform the QML approach, achieving smaller out-of-sample forecasting errors.

## 5 Simulation Studies

In this section, we use Monte Carlo simulations to evaluate the performance of the proposed methodology across a spectrum of finite samples.

Consider the model in Section [3](https://arxiv.org/html/2511.01271v1#S3 "3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") with common factors generated from a VAR(1) process 𝐟t=𝚽​𝐟t−1+𝜼t{\mathbf{f}}\_{t}=\boldsymbol{\Phi}{\mathbf{f}}\_{t-1}+\boldsymbol{\eta}\_{t}. Here, 𝚽\boldsymbol{\Phi} is a diagonal matrix, with entries independently sampled from a uniform distribution U​(0.5,0.9)U(0.5,0.9) and the error term 𝜼𝒕∼N​(0,𝐈K)\boldsymbol{\eta\_{t}}\sim N(0,{\mathbf{I}}\_{K}).
For each realization of 𝐲t{\mathbf{y}}\_{t}, the elements of the loading matrix 𝐁{\mathbf{B}} are independently drawn from U​(−2,2)U(-2,2), and the idiosyncratic error term 𝜺t\mbox{$\varepsilon$}\_{t} is generated from N​(0,IN)N(0,I\_{N}). The spatial 𝝆\rho is sampled independently from a power-law distribution with an exponent α=5\alpha=5. To construct the spatial matrices, the qq neighboring off-diagonal elements are set to 1 and the diagonal elements are 0, followed by row normalization to ensure each row sums to 1. We set q=3q=3 and the true number of factors K=3K=3, with dimension N=25,50,100,200N=25,50,100,200, and sample size T=50,100,200,400,1000T=50,100,200,400,1000. We use 1000 replications for each configuration of (T,N)(T,N). To make the results below replicable, the seed is set to be 1234 in the R programming.

We first examine the joint convergence properties of 𝜷^i\widehat{\boldsymbol{\beta}}\_{i} established in [Theorem 2](https://arxiv.org/html/2511.01271v1#Thmtheorem2 "Theorem 2. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). To evaluate its overall estimation accuracy, we use the root-mean-square error (RMSE), defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | RMSEβ^={(1N​∑i=1N‖(𝐗^i′​𝐗^i)​(𝜷^i−𝜷i)‖22)1/2,if ​λi→0(1N​∑i=1N‖𝜷^i​(λi)−𝐗^i​(λi)−1​𝐗^i​𝐗^i′​𝜷i‖22)1/2,otherwise.\mathrm{RMSE}\_{\widehat{\beta}}=\left\{\begin{array}[]{ll}\left(\frac{1}{N}\sum\_{i=1}^{N}\|(\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i})(\widehat{\boldsymbol{\beta}}\_{i}-\boldsymbol{\beta}\_{i})\|\_{2}^{2}\right)^{1/2},&\text{if }\lambda\_{i}\to 0\\ \left(\frac{1}{N}\sum\_{i=1}^{N}\|\widehat{\boldsymbol{\beta}}\_{i}(\lambda\_{i})-\widehat{{\mathbf{X}}}\_{i}(\lambda\_{i})^{-1}\widehat{{\mathbf{X}}}\_{i}\widehat{{\mathbf{X}}}\_{i}^{\prime}\boldsymbol{\beta}\_{i}\|\_{2}^{2}\right)^{1/2},&\text{{otherwise}.}\end{array}\right. |  | (28) |

Here, λi\lambda\_{i} is the ridge penalty parameter applied to the Yule-Walker equations for each sample. We examine two cases: a relatively large λi=10−3\lambda\_{i}=10^{-3} and a much smaller λi=10−9\lambda\_{i}=10^{-9}. When λi→0\lambda\_{i}\to 0 (e.g., λi=10−9\lambda\_{i}=10^{-9}), the estimator closely resembles
that of the ordinary least squares (OLS) estimation, but we set λi=10−9\lambda\_{i}=10^{-9} to avoid singularity of (𝐗^i′​𝐗^i)(\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i}).
Figure [2](https://arxiv.org/html/2511.01271v1#S5.F2 "Figure 2 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")(a) and (b) present the boxplots of the RMSEs of 𝜷^​(λi)\widehat{\boldsymbol{\beta}}(\lambda\_{i})’s (denoted by RMSE𝜷^{}\_{\widehat{\boldsymbol{\beta}}}) and ρ^i​(λi)\widehat{\rho}\_{i}(\lambda\_{i})’s (denoted by RMSEρ^{}\_{\widehat{\rho}}), respectively, computed using the second formula in ([28](https://arxiv.org/html/2511.01271v1#S5.E28 "In 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). From Figure [2](https://arxiv.org/html/2511.01271v1#S5.F2 "Figure 2 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we see that the RMSEβ^\mathrm{RMSE}\_{\widehat{\beta}} and RMSEρ^{}\_{\widehat{\rho}} decrease as the sample size TT increases, which is in agreement with the theoretical results in Theorem [2](https://arxiv.org/html/2511.01271v1#Thmtheorem2 "Theorem 2. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). Similar patterns can also be found in Figure [3](https://arxiv.org/html/2511.01271v1#S5.F3 "Figure 3 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") for λ→0\lambda\rightarrow 0 using the RMSE defined in the first line of ([28](https://arxiv.org/html/2511.01271v1#S5.E28 "In 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")).

![Refer to caption](x2.png)


Figure 2: Boxplots of estimator convergence for Eq ([11](https://arxiv.org/html/2511.01271v1#S3.E11 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) with a fixed large ridge penalty parameter (λi=10−3\lambda\_{i}=10^{-3}), where NN and TT denote the dimension and sample size,
respectively. (a) shows the joint estimation performance of 𝜷^i\widehat{\boldsymbol{\beta}}\_{i} measured by RMSEβ^\mathrm{RMSE}\_{\widehat{\beta}}, and (b) shows the estimation performance of the spatial parameter ^​𝝆\widehat{}\mbox{$\rho$} measured by RMSEρ^\mathrm{RMSE}\_{\widehat{\rho}}.



![Refer to caption](x3.png)

Figure 3: Boxplots of the joint convergence error for model ([11](https://arxiv.org/html/2511.01271v1#S3.E11 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) with λ=0\lambda=0. The statistics are defined in Figure [2](https://arxiv.org/html/2511.01271v1#S5.F2 "Figure 2 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), based on the first line of ([28](https://arxiv.org/html/2511.01271v1#S5.E28 "In 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")).

.

![Refer to caption](x4.png)


Figure 4: Histograms of the five spatial coefficient estimates and their corresponding empirical and theoretical distribution plots for Eq ([11](https://arxiv.org/html/2511.01271v1#S3.E11 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")).The histograms show the distribution of the first component of 𝐕i​(𝜷^i−𝜷i){\mathbf{V}}\_{i}(\widehat{\boldsymbol{\beta}}\_{i}-\boldsymbol{\beta}\_{i}) over 1000 iterations, under the setting of N=25N=25 and T=1500T=1500. The superimposed normal curve represents the theoretical distribution from Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), with mean 0 and variance given by the first diagonal element of 𝐗i′​𝐔i​𝐗i{\mathbf{X}}\_{i}^{\prime}{\mathbf{U}}\_{i}{\mathbf{X}}\_{i}. Here, i=1,3,5,7,9i=1,3,5,7,9 correspond to the 1st, 3rd, 5th, 7th, and 9th component in a dataset of dimension N=25N=25.




Table 1: Coverage rates for 𝐕i​(𝜷^i−𝜷i){\mathbf{V}}\_{i}(\widehat{\boldsymbol{\beta}}\_{i}-\boldsymbol{\beta}\_{i}) across different significance levels.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Significance | Coverage | | | | | |
| 0.1 | 0.801(0.013) | 0.852(0.011) | 0.941(0.007) | 0.966(0.006) | 0.989(0.003) | 0.998(0.001) |
| 0.05 | 0.842(0.012) | 0.891(0.010) | 0.957(0.006) | 0.983(0.004) | 0.997(0.002) | 1.000(0.000) |
| 0.01 | 0.898(0.010) | 0.935(0.008) | 0.980(0.004) | 0.993(0.003) | 0.998(0.001) | 1.000(0.000) |
| TT | 250 | 500 | 1000 | 2000 | 3000 | 5000 |

Note: This table shows the coverage rate of the first component of 𝐕1​(𝜷^1−𝜷1){\mathbf{V}}\_{1}(\widehat{\boldsymbol{\beta}}\_{1}-\boldsymbol{\beta}\_{1}) within the confidence intervals from the theoretical distribution in Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). The theoretical distribution has a zero mean and a variance equal to the first diagonal element of 𝐗1′​𝐔1​𝐗1{\mathbf{X}}\_{1}^{\prime}{\mathbf{U}}\_{1}{\mathbf{X}}\_{1}. TT is the sample size. The results are based on 1000 iterations with a cross-sectional dimension N=25N=25.

To assess the distributional properties of the estimates in Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we present histograms of the first component of 𝐕^i​(𝜷^i−𝜷i)\widehat{\mathbf{V}}\_{i}(\widehat{\boldsymbol{\beta}}\_{i}-\boldsymbol{\beta}\_{i}), for i=1,3,5,7i=1,3,5,7 and 99 in [Figure 4](https://arxiv.org/html/2511.01271v1#S5.F4 "Figure 4 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), along with their theoretical density curves computed from the limiting distribution in Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), where 𝐕^i\widehat{\mathbf{V}}\_{i} is the sample estimator for 𝐕i{\mathbf{V}}\_{i} defined in Eq ([23](https://arxiv.org/html/2511.01271v1#S4.E23 "In 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). The histograms and their corresponding QQ-plots in Figure [4](https://arxiv.org/html/2511.01271v1#S5.F4 "Figure 4 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") suggest that the entries of 𝐕^i​(𝜷^i−𝜷i)\widehat{\mathbf{V}}\_{i}(\widehat{\boldsymbol{\beta}}\_{i}-\boldsymbol{\beta}\_{i}) asymptotically follow a normal distribution, which aligns with our theoretical results. Furthermore, in [Table 1](https://arxiv.org/html/2511.01271v1#S5.T1 "Table 1 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we evaluate the asymptotic properties by reporting the coverage rates of the estimators in Eq ([11](https://arxiv.org/html/2511.01271v1#S3.E11 "In 3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) under varying significance levels and sample sizes
TT. As
TT increases, the coverage rates exhibit a clear improvement, consistent with the theoretical results in [Theorem 3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions").

As a shrinkage-based approach, it is interesting to directly assess the estimation accuracy of 𝜷i\boldsymbol{\beta}\_{i}. We define the coefficient error (CE) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | CEβ^=(1N​∑i=1N‖(𝜷^i​(λi)−𝜷i)‖22)1/2,\mathrm{CE}\_{\widehat{\beta}}=\left(\frac{1}{N}\sum\_{i=1}^{N}\|(\widehat{\boldsymbol{\beta}}\_{i}(\lambda\_{i})-\boldsymbol{\beta}\_{i})\|\_{2}^{2}\right)^{1/2}, |  | (29) |

which measures the deviation of 𝜷^i\widehat{\boldsymbol{\beta}}\_{i} from the true parameter 𝜷i\boldsymbol{\beta}\_{i}, thereby capturing the overall estimation error.
[Table 2](https://arxiv.org/html/2511.01271v1#S5.T2 "Table 2 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") reports the coefficient error for the ridge regression estimates 𝜷^i​(λi)\widehat{\boldsymbol{\beta}}\_{i}(\lambda\_{i}) when factors are observed.
The results indicate that ridge regression (λi=10−3\lambda\_{i}=10^{-3}) yields lower error and variance compared to OLS (λi=10−9\lambda\_{i}=10^{-9}). Additionally, the estimation errors are reduced when stacking the cases of
k=0k=0 and
k=1k=1 together in the Yule-Walker equations, compared to relying solely on
k=0k=0.

Table 2: Comparison of CE for ridge regression estimators with observed factors across different penalized parameter λi\lambda\_{i} and the lagging factor impact.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | k=1​(λi=10−9)k=1\kern 5.0pt(\lambda\_{i}=10^{-9}) | |  | k=1​(λi=10−3)k=1\kern 5.0pt(\lambda\_{i}=10^{-3}) | |  | k=0​(λi=10−3)k=0\kern 5.0pt(\lambda\_{i}=10^{-3}) | |
| N | T |  | CEβ^\mathrm{CE}\_{\widehat{\beta}} | CEρ^\mathrm{CE}\_{\widehat{\rho}} |  | CEβ^\mathrm{CE}\_{\widehat{\beta}} | CEρ^\mathrm{CE}\_{\widehat{\rho}} |  | CEβ^\mathrm{CE}\_{\widehat{\beta}} | CEρ^\mathrm{CE}\_{\widehat{\rho}} |
| 25 | 50 |  | 1.394(0.495) | 0.291(0.276) |  | 1.021(0.263) | 0.135(0.102) |  | 1.251(0.122) | 0.165(0.132) |
| 100 |  | 1.405(0.510) | 0.357(0.326) |  | 1.012(0.260) | 0.124(0.101) |  | 1.238(0.129) | 0.164(0.136) |
| 200 |  | 1.444(0.509) | 0.488(0.379) |  | 0.971(0.235) | 0.120(0.097) |  | 1.239(0.125) | 0.167(0.131) |
| 400 |  | 1.562(0.533) | 0.662(0.399) |  | 0.936(0.220) | 0.117(0.096) |  | 1.233(0.124) | 0.171(0.137) |
| 1000 |  | 1.810(0.522) | 0.925(0.358) |  | 0.976(0.219) | 0.133(0.113) |  | 1.236(0.122) | 0.175(0.137) |
| 1500 |  | 1.906(0.522) | 0.990(0.347) |  | 1.000(0.210) | 0.129(0.104) |  | 1.231(0.125) | 0.171(0.136) |
| 50 | 50 |  | 1.424(0.444) | 0.328(0.248) |  | 1.009(0.210) | 0.154(0.089) |  | 1.219(0.086) | 0.203(0.124) |
| 100 |  | 1.429(0.445) | 0.412(0.307) |  | 0.992(0.206) | 0.144(0.082) |  | 1.218(0.085) | 0.200(0.124) |
| 200 |  | 1.444(0.457) | 0.525(0.333) |  | 0.934(0.195) | 0.131(0.073) |  | 1.213(0.089) | 0.202(0.124) |
| 400 |  | 1.587(0.479) | 0.713(0.349) |  | 0.900(0.182) | 0.130(0.079) |  | 1.215(0.084) | 0.202(0.124) |
| 1000 |  | 1.838(0.460) | 0.947(0.310) |  | 0.931(0.174) | 0.133(0.079) |  | 1.205(0.087) | 0.192(0.116) |
| 1500 |  | 1.918(0.445) | 1.010(0.290) |  | 0.966(0.170) | 0.144(0.089) |  | 1.208(0.086) | 0.198(0.125) |
| 100 | 50 |  | 1.467(0.415) | 0.318(0.239) |  | 1.010(0.181) | 0.125(0.053) |  | 1.177(0.057) | 0.172(0.077) |
| 100 |  | 1.471(0.400) | 0.407(0.271) |  | 0.995(0.173) | 0.120(0.048) |  | 1.172(0.059) | 0.168(0.075) |
| 200 |  | 1.502(0.414) | 0.556(0.325) |  | 0.916(0.158) | 0.104(0.043) |  | 1.175(0.061) | 0.163(0.074) |
| 400 |  | 1.591(0.445) | 0.725(0.324) |  | 0.847(0.152) | 0.101(0.041) |  | 1.172(0.060) | 0.169(0.075) |
| 1000 |  | 1.829(0.425) | 0.937(0.284) |  | 0.877(0.148) | 0.106(0.053) |  | 1.174(0.059) | 0.166(0.080) |
| 1500 |  | 1.920(0.386) | 1.008(0.245) |  | 0.913(0.143) | 0.113(0.049) |  | 1.171(0.060) | 0.171(0.079) |
| 200 | 50 |  | 1.443(0.431) | 0.273(0.238) |  | 0.988(0.195) | 0.086(0.042) |  | 1.174(0.038) | 0.120(0.064) |
| 100 |  | 1.434(0.430) | 0.352(0.283) |  | 0.969(0.184) | 0.080(0.040) |  | 1.169(0.041) | 0.114(0.062) |
| 200 |  | 1.458(0.436) | 0.505(0.322) |  | 0.897(0.171) | 0.072(0.036) |  | 1.167(0.041) | 0.114(0.061) |
| 400 |  | 1.566(0.462) | 0.680(0.346) |  | 0.843(0.150) | 0.068(0.034) |  | 1.165(0.041) | 0.113(0.061) |
| 1000 |  | 1.834(0.453) | 0.938(0.303) |  | 0.868(0.145) | 0.072(0.037) |  | 1.165(0.042) | 0.116(0.062) |
| 1500 |  | 1.910(0.427) | 0.995(0.274) |  | 0.909(0.140) | 0.076(0.039) |  | 1.167(0.041) | 0.117(0.062) |

Note: Here, k=1k=1 represents the application of the stacking strategy, which incorporates lagged factors 𝐟t−1{\mathbf{f}}\_{t-1} as instrumental variables, whereas k=0k=0 indicates the stacking strategy is not applied, relying exclusively on the contemporaneous factors 𝐟t{\mathbf{f}}\_{t}, as detailed in Section [3.2](https://arxiv.org/html/2511.01271v1#S3.SS2 "3.2 Shrinkage Yule-Walker Estimation with Observed Factors ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions").

Next, we investigate the performance of our proposed method in scenarios where the common factors are unobserved, focusing on the recovery of latent factors 𝐟^t\widehat{\mathbf{f}}\_{t} and the estimation accuracy of the parameters 𝝆\rho and 𝐁{\mathbf{B}} in Eq ([14](https://arxiv.org/html/2511.01271v1#S3.E14 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). [Figure 5](https://arxiv.org/html/2511.01271v1#S5.F5 "Figure 5 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") illustrates the convergence behavior of the estimated loading matrix and latent factors using our method. In Panel (a) of [Figure 5](https://arxiv.org/html/2511.01271v1#S5.F5 "Figure 5 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), it is evident that the loading matrix converges steadily as TT increases. On the other hand, for each fixed NN, Panel (b) reveals that max1≤t≤T⁡‖𝐟^t−𝐊N​T​𝐟t‖2\max\_{1\leq t\leq T}\|\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t}\|\_{2} increases with TT, which is reasonable since the uniform distance is measured over the entire TT-period. However, for each fixed TT, the uniform distance will become smaller as NN increases, which is in agreement with our theoretical results.

Now, we examine the asymptotic normality of the estimated latent factors. [Figure 6](https://arxiv.org/html/2511.01271v1#S5.F6 "Figure 6 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") presents the histograms and QQ-plots of the first element of 𝐟^t−𝐊N​T​𝐟t\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t} for t=1,3,5,7t=1,3,5,7 and 99 when T=1500T=1500, which clearly show an asymptotic normality pattern across all settings. In addition, [Table 3](https://arxiv.org/html/2511.01271v1#S5.T3 "Table 3 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") presents the average coverage rates of the first component of 𝐟^t−𝐊N​T​𝐟t\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t} for t∈{1,6,11,…,96}t\in\{1,6,11,...,96\}, with a total of 20 factors, across different significance levels and values of NN. As NN increases, the average coverage rates gradually improve, accompanied by reduced variance. These findings align with [Theorem 4](https://arxiv.org/html/2511.01271v1#Thmtheorem4 "Theorem 4. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") and [Theorem 5](https://arxiv.org/html/2511.01271v1#Thmtheorem5 "Theorem 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions").

![Refer to caption](x5.png)


Figure 5: Boxplots of the convergence performance for the estimated loading matrices and latent factors in Eq ([14](https://arxiv.org/html/2511.01271v1#S3.E14 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")).

![Refer to caption](x6.png)


Figure 6: Histograms of 𝐟^t−𝐊N​T​𝐟t\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t} and their corresponding
empirical and theoretical distribution plots for Model ([14](https://arxiv.org/html/2511.01271v1#S3.E14 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). The results are based on 1000 iterations, focusing on the first element of 𝐟^t−𝐊N​T​𝐟t\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t}, for t = 1, 3, 5, 7, 9. The superimposed normal curves represent the theoretical distribution derived in Theorem [5](https://arxiv.org/html/2511.01271v1#Thmtheorem5 "Theorem 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")(ii), with mean 0 and variance given by the first diagonal element of 𝐇​𝚪t​𝐇′{\mathbf{H}}\boldsymbol{\Gamma}\_{t}{\mathbf{H}}^{\prime}. The simulation results are obtained under (N,T)=(25,1500)(N,T)=(25,1500).




Table 3: Coverage rates of 𝐟^t−𝐊N​T​𝐟t\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t} across different significance levels

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Significance | Coverage | | | |
| 0.1 | 0.910(0.0090) | 0.922(0.0085) | 0.943(0.0073) | 0.987(0.0036) |
| 0.05 | 0.957(0.0064) | 0.959(0.0063) | 0.974(0.0059) | 0.993(0.0026) |
| 0.01 | 0.991(0.0030) | 0.991(0.0030) | 0.994(0.0024) | 0.998(0.0014) |
| NN | 25 | 50 | 100 | 200 |

Note: This table shows the coverage rate of the first component of 𝐟^t−𝐊N​T​𝐟t\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t} within the confidence intervals from the theoretical distribution in Theorem [5](https://arxiv.org/html/2511.01271v1#Thmtheorem5 "Theorem 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")(ii). The theoretical distribution has mean zero and variance given by the first diagonal element of 𝐇​𝚪t​𝐇′{\mathbf{H}}\boldsymbol{\Gamma}\_{t}{\mathbf{H}}^{\prime}. The results are based on 1000 iterations with sample size T=1500T=1500.

With the estimated factors 𝐟^t\widehat{\mathbf{f}}\_{t},
[Figure 7](https://arxiv.org/html/2511.01271v1#S5.F7 "Figure 7 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") demonstrates the boxplots of the RMSE of 𝜷~i\widetilde{\boldsymbol{\beta}}\_{i} under increasing TT, where the RMSE is similarly define as ([28](https://arxiv.org/html/2511.01271v1#S5.E28 "In 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). The patterns of the RMSEs in [Figure 7](https://arxiv.org/html/2511.01271v1#S5.F7 "Figure 7 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") are similar to those in Figure [3](https://arxiv.org/html/2511.01271v1#S5.F3 "Figure 3 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), and we omit the details here. To validate the distributional properties, [Figure 8](https://arxiv.org/html/2511.01271v1#S5.F8 "Figure 8 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") displays the histogram and QQ-plot of the first component of 𝐕iH​(𝜷~i−𝐊N​T∗​𝜷i){\mathbf{V}}\_{i}^{H}(\widetilde{\boldsymbol{\beta}}\_{i}-{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{i}), for i=1,3,5,7i=1,3,5,7 and 99. From Figure [7](https://arxiv.org/html/2511.01271v1#S5.F7 "Figure 7 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we can see clearly an asymptotic normality pattern across all settings, which is in line with our theoretical results in Theorem [6](https://arxiv.org/html/2511.01271v1#Thmtheorem6 "Theorem 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). Moreover, we verify the coverage probabilities of the first component of 𝐕1H​(𝜷~1−𝐊N​T∗​𝜷1){\mathbf{V}}\_{1}^{H}(\widetilde{\boldsymbol{\beta}}\_{1}-{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{1}) in Table [8](https://arxiv.org/html/2511.01271v1#S5.F8 "Figure 8 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), which are also in agreement with our theory.

Next, we present the coefficient error (CE) results for ridge estimators in the case of unknown factors in [Table 5](https://arxiv.org/html/2511.01271v1#S5.T5 "Table 5 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). From [Table 5](https://arxiv.org/html/2511.01271v1#S5.T5 "Table 5 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") we see that integrating the stacking strategy with proper ridge penalty improves the estimation accuracy, further validating the proposed method.

![Refer to caption](x7.png)


Figure 7: Boxplots of estimator convergence for model ([18](https://arxiv.org/html/2511.01271v1#S3.E18 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) with fixed small λi\lambda\_{i}.

![Refer to caption](x8.png)


Figure 8: Histograms of the five spatial coefficient estimates and their corresponding empirical and theoretical distribution plots for model ([18](https://arxiv.org/html/2511.01271v1#S3.E18 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). The histograms show the distribution of the first component of 𝐕iH​(𝜷~i−𝐊N​T∗​𝜷i){\mathbf{V}}\_{i}^{H}(\widetilde{\boldsymbol{\beta}}\_{i}-{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{i}) as defined in [Theorem 6](https://arxiv.org/html/2511.01271v1#Thmtheorem6 "Theorem 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). The superimposed normal curve represents the theoretical distribution from Theorem [6](https://arxiv.org/html/2511.01271v1#Thmtheorem6 "Theorem 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). Here, i=1,3,5,7,9i=1,3,5,7,9 correspond to the 1st, 3rd, 5th, 7th, and 9th samples in a dataset of size NN. The results are based on 1,000 iterations with (N,T)=(25,3000)(N,T)=(25,3000).




Table 4: Coverage performance of 𝐕iH​(𝜷~i−𝐊N​T∗​𝜷i){\mathbf{V}}\_{i}^{H}(\widetilde{\boldsymbol{\beta}}\_{i}-{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{i}) under latent factor estimation across different significance levels.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Significance | Coverage | | | | | | | |
| 0.1 | 0.343(0.016) | 0.438(0.017) | 0.531(0.017) | 0.663(0.016) | 0.819(0.013) | 0.932(0.008) | 0.979(0.005) | 1.000(0.000) |
| 0.05 | 0.399(0.016) | 0.507(0.017) | 0.595(0.017) | 0.718(0.015) | 0.866(0.011) | 0.974(0.005) | 1.000(0.000) | 1.000(0.000) |
| 0.01 | 0.477(0.017) | 0.595(0.017) | 0.692(0.016) | 0.786(0.014) | 0.946(0.008) | 1.000(0.000) | 1.000(0.000) | 1.000(0.000) |
| TT | 50 | 100 | 200 | 400 | 1000 | 2000 | 3000 | 5000 |

Note: This table shows the coverage rate of the first component of 𝐕1H​(𝜷~1−𝐊N​T∗​𝜷1){\mathbf{V}}\_{1}^{H}(\widetilde{\boldsymbol{\beta}}\_{1}-{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{1}), illustrating the asymptotic performance of ρ~1\widetilde{\rho}\_{1} within the confidence intervals derived from the theoretical distribution, based on 1,000 iterations with N=25N=25. The theoretical distribution has zero mean and variance corresponding to the first diagonal element of 𝐗1H​𝐔1H′​𝐗1H{\mathbf{X}}\_{1}^{H}{{}^{\prime}}{\mathbf{U}}\_{1}^{H}{\mathbf{X}}\_{1}^{H}, which is defined in [Theorem 6](https://arxiv.org/html/2511.01271v1#Thmtheorem6 "Theorem 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions").




Table 5: Comparison of coefficient error (CE) for ridge regression estimators with latent factors across different penalized parameter λi\lambda\_{i} and the lagging factor impact.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | k=1​(λi=10−9)k=1\kern 5.0pt(\lambda\_{i}=10^{-9}) | |  | k=1​(λi=1)k=1\kern 5.0pt(\lambda\_{i}=1) | |  | k=0​(λi=1)k=0\kern 5.0pt(\lambda\_{i}=1) | |
| N | T |  | CEβ^\mathrm{CE}\_{\widehat{\beta}} | CEρ^\mathrm{CE}\_{\widehat{\rho}} |  | CEβ^\mathrm{CE}\_{\widehat{\beta}} | CEρ^\mathrm{CE}\_{\widehat{\rho}} |  | CEβ^\mathrm{CE}\_{\widehat{\beta}} | CEρ^\mathrm{CE}\_{\widehat{\rho}} |
| 25 | 50 |  | 2.417(0.139) | 1.201(0.184) |  | 2.336(0.122) | 1.072(0.235) |  | 2.339(0.142) | 1.080(0.251) |
| 100 |  | 2.410(0.152) | 1.194(0.202) |  | 2.322(0.130) | 1.068(0.247) |  | 2.330(0.143) | 1.066(0.263) |
| 200 |  | 2.394(0.166) | 1.190(0.178) |  | 2.324(0.128) | 1.076(0.236) |  | 2.327(0.141) | 1.077(0.242) |
| 400 |  | 2.396(0.178) | 1.173(0.183) |  | 2.314(0.128) | 1.073(0.232) |  | 2.336(0.131) | 1.090(0.241) |
| 1000 |  | 2.419(0.144) | 1.199(0.173) |  | 2.310(0.143) | 1.070(0.244) |  | 2.334(0.139) | 1.080(0.260) |
| 1500 |  | 2.435(0.153) | 1.195(0.190) |  | 2.323(0.126) | 1.078(0.234) |  | 2.323(0.139) | 1.080(0.247) |
| 50 | 50 |  | 2.346(0.142) | 1.001(0.230) |  | 2.262(0.150) | 0.838(0.306) |  | 2.288(0.117) | 0.973(0.277) |
| 100 |  | 2.334(0.119) | 1.062(0.179) |  | 2.267(0.134) | 0.937(0.270) |  | 2.302(0.104) | 1.041(0.232) |
| 200 |  | 2.325(0.100) | 1.055(0.175) |  | 2.259(0.134) | 0.905(0.281) |  | 2.282(0.105) | 0.998(0.268) |
| 400 |  | 2.362(0.123) | 1.087(0.162) |  | 2.288(0.134) | 0.937(0.263) |  | 2.306(0.114) | 1.013(0.254) |
| 1000 |  | 2.359(0.106) | 1.084(0.167) |  | 2.285(0.122) | 0.920(0.254) |  | 2.300(0.104) | 1.027(0.239) |
| 1500 |  | 2.362(0.108) | 1.087(0.163) |  | 2.278(0.136) | 0.926(0.262) |  | 2.288(0.115) | 1.029(0.225) |
| 100 | 50 |  | 2.244(0.122) | 0.828(0.243) |  | 2.219(0.135) | 0.797(0.291) |  | 2.289(0.108) | 1.057(0.258) |
| 100 |  | 2.261(0.102) | 0.912(0.232) |  | 2.227(0.119) | 0.767(0.302) |  | 2.299(0.097) | 1.033(0.266) |
| 200 |  | 2.248(0.126) | 0.931(0.237) |  | 2.220(0.127) | 0.835(0.289) |  | 2.317(0.075) | 1.115(0.179) |
| 400 |  | 2.265(0.113) | 0.947(0.223) |  | 2.245(0.128) | 0.880(0.304) |  | 2.309(0.094) | 1.081(0.228) |
| 1000 |  | 2.278(0.091) | 0.965(0.194) |  | 2.242(0.119) | 0.929(0.266) |  | 2.314(0.071) | 1.139(0.185) |
| 1500 |  | 2.267(0.102) | 0.939(0.214) |  | 2.246(0.124) | 0.870(0.291) |  | 2.308(0.092) | 1.089(0.208) |
| 200 | 50 |  | 2.230(0.116) | 0.864(0.282) |  | 2.230(0.086) | 0.886(0.230) |  | 2.352(0.055) | 1.213(0.148) |
| 100 |  | 2.228(0.098) | 0.890(0.232) |  | 2.217(0.101) | 0.849(0.262) |  | 2.345(0.066) | 1.218(0.166) |
| 200 |  | 2.247(0.096) | 0.945(0.248) |  | 2.230(0.098) | 0.921(0.231) |  | 2.350(0.047) | 1.230(0.104) |
| 400 |  | 2.251(0.096) | 0.950(0.233) |  | 2.231(0.110) | 0.918(0.250) |  | 2.333(0.084) | 1.184(0.231) |
| 1000 |  | 2.251(0.086) | 0.970(0.214) |  | 2.217(0.104) | 0.880(0.271) |  | 2.331(0.080) | 1.180(0.242) |
| 1500 |  | 2.254(0.094) | 0.978(0.223) |  | 2.259(0.093) | 0.986(0.237) |  | 2.339(0.093) | 1.198(0.228) |

Finally, we compare the predictive performance of our method with QMLE by evaluating their out-of-sample forecasting accuracy under heterogeneous conditions. The forecasting error (FE) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | FE=(1N​(T−T1)​∑t=T1+1T‖(𝐲^t−𝐲t)‖22)1/2,\mathrm{FE}=\left(\frac{1}{N(T-T\_{1})}\sum\_{t=T\_{1}+1}^{T}\|(\widehat{\mathbf{y}}\_{t}-{\mathbf{y}}\_{t})\|\_{2}^{2}\right)^{1/2}, |  | (30) |

where 𝐲^t\widehat{\mathbf{y}}\_{t} denotes the predicted value using the estimated coefficients from the training sample, and 𝐲t{\mathbf{y}}\_{t} represents the actual value. [Table 6](https://arxiv.org/html/2511.01271v1#S5.T6 "Table 6 ‣ 5 Simulation Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") presents the forecasting error and standard deviation of both method across different cross-sectional dimensions (NN), with the out-of-sample period set from T1+1=321T\_{1}+1=321 and T1+1=400T\_{1}+1=400.
The proposed model with lagged factor instruments (k=1)(k=1) achieves lower forecast error across all
NN dimensions, outperforming QMLE. This results aligns with prior simulations that emphasize the benefits of combining shrinkage techniques with lagging factor integration to enhance accuracy.

Table 6: Out-of-sample simulation evaluation of different models with best ones in boldface.

|  | Proposed Model (λi=10−3)(\lambda\_{i}=10^{-3}) | |  | Proposed Model (λi=10−9)(\lambda\_{i}=10^{-9}) | |  | QML |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NN | k=0k=0 | k=1k=1 |  | k=0k=0 | k=1k=1 |  |
| 25 | 2.672(0.714) | 1.046(0.087) |  | 2.605(0.689) | 1.047(0.088) |  | 1.900(0.399) |
| 50 | 2.750(1.043) | 1.047(0.090) |  | 2.618(0.978) | 1.048(0.091) |  | 1.577(0.353) |
| 100 | 2.925(1.589) | 1.051(0.093) |  | 2.634(1.386) | 1.055(0.096) |  | 1.357(0.224) |
| 200 | 3.423(2.753) | 1.055(0.101) |  | 2.666(1.996) | 1.062(0.111) |  | 1.353(0.347) |

Note: This table compares out-of-sample forecast errors between the proposed model and QML method under varying configurations of regularization parameters (λi=10−3\lambda\_{i}=10^{-3} and λi=10−9\lambda\_{i}=10^{-9}) and lagging factor instruments (k=0k=0 and k=1k=1). The settings for the simulation include T=400T=400 (time periods) and K=3K=3 (factor dimensions).

## 6 Empirical Studies

In this section, we apply the proposed method to two arbitrage pricing case studies. The first one focuses on modeling and forecasting stock returns of the S&P 500 constituents, while the second examines quarterly changes in real housing prices across U.S. Metropolitan Statistical Areas (MSAs). For each case, we use the R software with a fixed random seed (1234) to randomly select a subset of cross-sectional units (denoted by NN) and a subsample from the beginning of the full time span (denoted by TT). The first 80%80\% of each subsample is used as the training set, and the remaining 20%20\% as the testing set for evaluating out-of-sample forecasting performance. We compare the proposed approach with the QMLE method and the classical Fama-French factor model without spatial interaction.

### 6.1 Empirical Application to Stock Returns

Companies located in close geographic proximity often share exposure to regional policies and industrial clusters, highlighting the importance of accounting for spatial dependencies. In this example, we investigate how firm locations influence stock returns. Our analysis focuses on the daily log excess returns of S&P 500 constituents from January 2004 to December 2016, comprising 3,273 time points across 205 companies. The companies are selected in the order provided by the original dataset, which is publicly available at <https://mpelger.people.stanford.edu/data-and-code>, with further details documented in Pelger ([2020](https://arxiv.org/html/2511.01271v1#bib.bib40)). As common factors, we incorporate the Fama-French variables, including the market factor (MKT), size factor (SMB), and value factor (HML).
To capture spatial dependence in each selected subsample with cross-sectional dimension NN and time dimension TT, we construct a spatial weight matrix following a standard geographic approach from spatial econometrics. Specifically, we define an N×NN\times N spatial weight matrix WW, where each off-diagonal entry wi​jw\_{ij} is given by wi​j=(si​di​j)−1w\_{ij}=(s\_{i}d\_{ij})^{-1} for i≠ji\neq j, and wi​i=0w\_{ii}=0. Here, di​jd\_{ij} denotes the Haversine distance between the headquarters of companies ii and jj, and si=∑j=1Ndi​j−1s\_{i}=\sum\_{j=1}^{N}d\_{ij}^{-1} serves as a normalization factor to ensure that each row of WW sums to one. This construction ensures that the weights represent the relative geographic influence of company jj on company ii.

Table [7](https://arxiv.org/html/2511.01271v1#S6.T7 "Table 7 ‣ 6.1 Empirical Application to Stock Returns ‣ 6 Empirical Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") presents a detailed comparison of the forecasting performance of our proposed method against QMLE and the classical Fama-French factor model across various configurations and industry classifications. As shown in the table, our method consistently achieves lower forecasting errors than both QMLE and the factor model, highlighting its effectiveness and the value of incorporating spatial dependencies into the arbitrage pricing framework.
In terms of computational efficiency, our method offers a substantial advantage over QMLE. For example, when N=200N=200 and T=1000T=1000, QMLE requires over six hours on a standard CPU, while our approach produces comparable results in just a few minutes. This notable efficiency gain makes our method particularly attractive for large-scale applications, offering a favorable trade-off between accuracy and computational cost.

Table 7: Forecast error comparison for stock returns with observed factors.

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | | Proposed method | | |  | QMLE | | |  | Factor model | | |
| N=100N=100 | N=150N=150 | N=200N=200 |  | N=100N=100 | N=150N=150 | N=200N=200 |  | N=100N=100 | N=150N=150 | N=200N=200 |
| T=500T=500 |  | 0.8601 (0.2173) | 0.8546 (0.2396) | 0.8462 (0.2510) |  | 0.8665 (0.2177) | 0.8768 (0.2461) | 0.8772 (0.2653) |  | 0.8606 (0.2173) | 0.8551 (0.2396) | 0.8476 (0.2518) |
| T=1000T=1000 |  | 0.9640 (0.1999) | 0.9668 (0.2352) | 0.9866 (0.2791) |  | 0.9861 (0.2038) | 1.0161 (0.2505) | 1.0542 (0.3073) |  | 0.9646 (0.2005) | 0.9678 (0.2360) | 0.9873 (0.2801) |
| T=2000T=2000 |  | 0.5630 (0.0641) | 0.5704 (0.0745) | 0.5623 (0.0818) |  | 0.6042 (0.0844) | 0.6439 (0.1156) | 0.6723 (0.1510) |  | 0.5705 (0.0725) | 0.5821 (0.0863) | 0.5774 (0.0957) |
| GICS Class |  | Information Technology (N=36)(N=36) | | |  | Financials (N=31)(N=31) | | |  | Consumer Staples (N=19)(N=19) | | |
|  | Proposed method | QMLE | Factor model |  | Proposed method | QMLE | Factor model |  | Proposed method | QMLE | Factor model |
| T=500T=500 |  | 0.7683(0.1371) | 0.8061(0.1431) | 0.7701(0.1369) |  | 0.7661(0.1223) | 0.7730(0.1256) | 0.7669(0.1223) |  | 0.8765(0.1396) | 0.8766(0.1399) | 0.8767(0.1398) |
| T=1000T=1000 |  | 0.8338(0.1252) | 0.8697(0.1281) | 0.8352(0.1249) |  | 1.1530(0.2088) | 1.1535(0.2069) | 1.1628(0.2123) |  | 0.9823(0.1024) | 0.9844(0.1021) | 0.9837(0.1021) |
| T=2000T=2000 |  | 0.6440(0.0726) | 0.6951(0.0804) | 0.6441(0.0726) |  | 0.3859(0.0351) | 0.3963(0.0366) | 0.3884(0.0351) |  | 0.6756(0.0556) | 0.6821(0.0565) | 0.6793(0.0561) |

Note: This table compares the forecast errors of the proposed model, QMLE, and the factor model across different combinations of NN and TT, as well as three industry classifications: Information Technology, Financials, and Consumer Staples. These classifications are based on the Global Industry Classification Standard (GICS).

Furthermore, we evaluate the forecasting errors for stock returns driven by unobserved factors, with the results summarized in Table [8](https://arxiv.org/html/2511.01271v1#S6.T8 "Table 8 ‣ 6.1 Empirical Application to Stock Returns ‣ 6 Empirical Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). As shown in the table, the findings are consistent with our earlier results, further demonstrating the scalability and practicality of the proposed method for large-scale applications.

Table 8: Forecast error comparison for stock returns with latent factors

| Method | | Proposed method | | |  | QMLE | | |  | Factor model | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N=100N=100 | N=150N=150 | N=200N=200 |  | N=100N=100 | N=150N=150 | N=200N=200 |  | N=100N=100 | N=150N=150 | N=200N=200 |
| T=500T=500 |  | 0.8218(0.2138) | 0.8251(0.2353) | 0.8157(0.2449) |  | 0.8468 (0.2132) | 0.8422 (0.2361) | 0.8353 (0.2491) |  | 0.8468(0.2137) | 0.8267(0.2346) | 0.8164(0.2444) |
| T=1000T=1000 |  | 0.9092(0.1919) | 0.9315(0.2261) | 0.9250(0.2601) |  | 0.9369 (0.1968) | 0.9472 (0.2320) | 0.9605 (0.2669) |  | 0.9244(0.1931) | 0.9322(0.2257) | 0.9429(0.2591) |
| T=2000T=2000 |  | 0.5441(0.0690) | 0.5501(0.0810) | 0.5491(0.0902) |  | 0.5560 (0.0704) | 0.5712 (0.0839) | 0.5698 (0.0938) |  | 0.5460(0.0695) | 0.5559(0.0823) | 0.5532(0.0913) |

Note: This table compares the forecast errors of the proposed model with QMLE and factor model under different combinations of NN and TT. The number of latent factors is determined using the information criterion proposed by Bai and Ng ([2002](https://arxiv.org/html/2511.01271v1#bib.bib7)).

### 6.2 Empirical Application to U.S. Housing Market

Our second application examines quarterly changes in real housing prices across 377 U.S. Metropolitan Statistical Areas (MSAs) from 1975-Q1 to 2014-Q4, as studied in Aquaro et al. ([2021](https://arxiv.org/html/2511.01271v1#bib.bib4)). Due to shared supply and demand dynamics among neighboring regions, spatial models are essential for capturing such dependencies and enhancing predictive accuracy.

To account for broader economic influences—particularly the impact of stock market movements on real estate investment sentiment and capital allocation—we incorporate factor proxies from the previous example. For spatial dependence, we adopt the spatial weight matrix W75W\_{75} proposed in Aquaro et al. ([2021](https://arxiv.org/html/2511.01271v1#bib.bib4)), in which MSAs within a specified radius dd are treated as neighbors (assigned a weight of 1), while non-neighbors receive a weight of 0. The resulting matrix is row-normalized to obtain the final weight matrix WW.

Table [9](https://arxiv.org/html/2511.01271v1#S6.T9 "Table 9 ‣ 6.2 Empirical Application to U.S. Housing Market ‣ 6 Empirical Studies ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") presents a detailed comparison of forecasting errors for our proposed method, the QMLE approach from Aquaro et al. ([2021](https://arxiv.org/html/2511.01271v1#bib.bib4)), and the Fama-French factor model without spatial interactions. As shown in the table, our method consistently yields lower forecast errors in most cases, demonstrating its robustness and efficiency across different data settings and reinforcing its applicability to spatial econometric forecasting.

Table 9: Forecast error comparison for U.S. housing prices with observed factors.

| Method | | Proposed method | | |  | QMLE | | |  | Factor model | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N = 20 | N=50 | N = 200 |  | N = 20 | N = 50 | N = 200 |  | N = 20 | N=50 | N = 200 |
| T = 50 |  | 1.2520(0.3110) | 1.6515(0.8584) | 1.5533(2.3174) |  | 1.2680(0.2254) | 1.6605(0.7631) | 1.5863(1.5341) |  | 1.2881(0.2231) | 1.6931(0.7788) | 1.7533(1.5479) |
| T = 100 |  | 2.2001(0.6841) | 2.1557(1.0271) | 2.1723(2.4108) |  | 2.2015(0.5007) | 2.1577(0.7837) | 2.1737(2.3700) |  | 2.2163(0.4752) | 2.1715(0.7257) | 2.2269(1.4651) |
| T = 150 |  | 2.8807(0.3411) | 2.8876(0.4750) | 2.7555(1.5827) |  | 2.8854(0.3358) | 2.8910(0.4665) | 2.7887(1.0758) |  | 2.8870(0.3356) | 2.8951(0.4645) | 2.8076(1.0340) |

Note: This table compares the forecast errors of the proposed model, QMLE and factor model in predicting U.S. housing prices, utilizing factors from the Fama-French three-factor model and a spatial weight matrix based on geometric distances.

In summary, the comparative analyses of S&P 500 stock returns and U.S. housing prices demonstrate that our proposed method delivers superior predictive accuracy and computational efficiency, confirming its effectiveness across diverse spatial and temporal settings.

## 7 Conclusion

This paper introduced a Spatial Arbitrage Pricing Theory (SAPT) model that integrates spatial interactions with multifactor structures involving both observable and latent variables. The SAPT framework offers two key conceptual innovations for asset pricing: (1) it introduces a spatial rho parameter, serving as a counterpart to the market beta in the classical CAPM; and (2) it captures spatial correlations typically unaccounted for in traditional Arbitrage Pricing Theory (APT) models, thereby extending the scope of standard CAPM and enhancing econometric tools for asset pricing analysis. For estimation, we proposed a generalized shrinkage Yule-Walker method that accommodates both observable and latent factors. The proposed methodology provides a flexible and computationally efficient framework for theoretical advancement and empirical research in financial and economic modeling.

## References

* (1)
* Ahn and Horenstein (2013)

  Ahn, S. C., and A. R. Horenstein (2013): “Eigenvalue ratio
  test for the number of factors,” *Econometrica*, 81(3), 1203–1227.
* Anselin (1988)

  Anselin, L. (1988): *Spatial econometrics: methods and models*,
  vol. 4. Springer Science & Business Media.
* Aquaro et al. (2021)

  Aquaro, M., N. Bailey, and M. H. Pesaran (2021):
  “Estimation and inference for spatial models with heterogeneous
  coefficients: an application to US house prices,” *Journal of Applied
  Econometrics*, 36(1), 18–44.
* Bai (2003)

  Bai, J. (2003): “Inferential theory for factor models of large
  dimensions,” *Econometrica*, 71(1), 135–171.
* Bai and Li (2021)

  Bai, J., and K. Li (2021): “Dynamic spatial panel data
  models with common shocks,” *Journal of Econometrics*, 224(1),
  134–160.
* Bai and Ng (2002)

  Bai, J., and S. Ng (2002): “Determining the number of
  factors in approximate factor models,” *Econometrica*, 70(1), 191–221.
* Carrasco and Tchuente (2015)

  Carrasco, M., and G. Tchuente (2015): “Regularized LIML
  for many instruments,” *Journal of Econometrics*, 186(2), 427–442.
* Case et al. (1993)

  Case, A. C., H. S. Rosen, and J. R. Hines (1993): “Budget
  spillovers and fiscal policy interdependence: Evidence from the states,”
  *Journal of Public Economics*, 52(3), 285–307.
* Cliff and Ord (1973)

  Cliff, A., and J. Ord (1973): *Spatial
  autocorrelation.* Sage Publications Sage CA: Thousand Oaks, CA.
* Cochrane (2009)

  Cochrane, J. (2009): *Asset pricing: Revised edition*. Princeton
  university press.
* Cressie (2015)

  Cressie, N. (2015): *Statistics for spatial data*. John Wiley &
  Sons.
* Fama and French (1993)

  Fama, E. F., and K. R. French (1993): “Common risk factors
  in the returns on stocks and bonds,” *Journal of Financial Economics*,
  33(1), 3–56.
* Fama and French (2015)

     (2015): “A five-factor asset pricing model,”
  *Journal of Financial Economics*, 116(1), 1–22.
* Fan et al. (2013)

  Fan, J., Y. Liao, and M. Mincheva (2013): “Large
  covariance estimation by thresholding principal orthogonal complements,”
  *Journal of the Royal Statistical Society: Series B (Statistical
  Methodology)*, 75(4), 603–680.
* Fan and Yao (2003)

  Fan, J., and Q. Yao (2003): *Nonlinear time series:
  nonparametric and parametric methods*, vol. 20. Springer.
* Feng et al. (2020)

  Feng, G., S. Giglio, and D. Xiu (2020): “Taming the factor
  zoo: A test of new factors,” *The Journal of Finance*, 75(3),
  1327–1370.
* Forni et al. (2000)

  Forni, M., M. Hallin, M. Lippi, and L. Reichlin (2000):
  “The generalized dynamic-factor model: Identification and estimation,”
  *Review of Economics and statistics*, 82(4), 540–554.
* Forni et al. (2005)

     (2005): “The generalized dynamic factor model: one-sided
  estimation and forecasting,” *Journal of the American Statistical
  Association*, 100(471), 830–840.
* Gao et al. (2019)

  Gao, Z., Y. Ma, H. Wang, and Q. Yao (2019): “Banded
  spatio-temporal autoregressions,” *Journal of Econometrics*, 208(1),
  211–230.
* Gao and Tsay (2019)

  Gao, Z., and R. S. Tsay (2019): “A structural-factor
  approach to modeling high-dimensional time series and space-time data,”
  *Journal of Time Series Analysis*, 40(3), 343–362.
* Gao and Tsay (2021)

     (2021): “A Two-Way Transformed Factor Model for
  Matrix-Variate Time Series,” *Econometrics and Statistics*.
* Gao and Tsay (2022)

     (2022): “Modeling high-dimensional time series: A factor
  model with dynamically dependent factors and diverging eigenvalues,”
  *Journal of the American Statistical Association*, 117(539), 1398–1414.
* Gao and Tsay (2023)

     (2023): “Divide-and-conquer: a distributed hierarchical
  factor approach to modeling large-scale time series data,” *Journal of
  the American Statistical Association*, 118(544), 2698–2711.
* Gao and Tsay (2024)

     (2024): “Supervised dynamic pca: Linear dynamic
  forecasting with many predictors,” *Journal of the American Statistical
  Association*, pp. 1–15.
* Giglio et al. (2025)

  Giglio, S., D. Xiu, and D. Zhang (2025): “Test assets and
  weak factors,” *The Journal of Finance*, 80(1), 259–319.
* Hansen (1982)

  Hansen, L. P. (1982): “Large sample properties of generalized method
  of moments estimators,” *Econometrica: Journal of the econometric
  society*, pp. 1029–1054.
* Hu et al. (2023)

  Hu, J., H. Ding, and X. Liu (2023): “Arbitrage pricing
  with heterogeneous spatial effects and heteroscedastic disturbances,”
  *Journal of Financial Econometrics*, 21(4), 1169–1195.
* Kou et al. (2018)

  Kou, S., X. Peng, and H. Zhong (2018): “Asset pricing with
  spatial interaction,” *Management Science*, 64(5), 2083–2101.
* Lam and Yao (2012)

  Lam, C., and Q. Yao (2012): “Factor modeling for
  high-dimensional time series: inference for the number of factors,”
  *The Annals of Statistics*, pp. 694–726.
* Lam et al. (2011)

  Lam, C., Q. Yao, and N. Bathia (2011): “Estimation of
  latent factors for high-dimensional time series,” *Biometrika*, 98(4),
  901–918.
* Lee (2004)

  Lee, L.-F. (2004): “Asymptotic distributions of quasi-maximum
  likelihood estimators for spatial autoregressive models,”
  *Econometrica*, 72(6), 1899–1925.
* Lee and Yu (2010)

  Lee, L.-f., and J. Yu (2010): “Some recent developments in
  spatial panel data models,” *Regional Science and Urban Economics*,
  40(5), 255–271.
* Lettau and Pelger (2020)

  Lettau, M., and M. Pelger (2020): “Estimating Latent Asset
  Pricing Factors,” *Journal of Econometrics*, 218(1), 1–31.
* Liao (2013)

  Liao, Z. (2013): “Adaptive GMM shrinkage estimation with consistent
  moment selection,” *Econometric Theory*, 29(5), 857–904.
* Lin and Lee (2010)

  Lin, X., and L.-f. Lee (2010): “GMM estimation of spatial
  autoregressive models with unknown heteroskedasticity,” *Journal of
  Econometrics*, 157(1), 34–52.
* Liu et al. (2025)

  Liu, X., J. Guerard, R. Chen, and R. Tsay (2025):
  “Improving estimation of portfolio risk using new statistical factors,”
  *Annals of Operations Research*, 346, 245–261.
* Markowitz (1952)

  Markowitz, H. M. (1952): “Portfolio selection,” *Journal of
  Finance*, 7(1), 71–91.
* Onatski (2010)

  Onatski, A. (2010): “Determining the number of factors from
  empirical distribution of eigenvalues,” *The Review of Economics and
  Statistics*, 92(4), 1004–1016.
* Pelger (2020)

  Pelger, M. (2020): “Understanding systematic risk: A high-frequency
  approach,” *The Journal of Finance*, 75(4), 2179–2220.
* Pesaran and Tosetti (2011)

  Pesaran, M. H., and E. Tosetti (2011): “Large panels with
  common factors and spatial correlation,” *Journal of Econometrics*,
  161(2), 182–202.
* Pirinsky and Wang (2006)

  Pirinsky, C., and Q. Wang (2006): “Does corporate
  headquarters location matter for stock returns?,” *The Journal of
  Finance*, 61(4), 1991–2015.
* Ross (1976)

  Ross, S. A. (1976): “The arbitrage theory of capital asset
  pricing,” *Journal of Economic Theory*, 13(3), 341–360.
* Sharpe (1964)

  Sharpe, W. F. (1964): “Capital asset prices: A theory of market
  equilibrium under conditions of risk,” *The journal of finance*, 19(3),
  425–442.
* Stock and Watson (2002)

  Stock, J. H., and M. Watson (2002): “Macroeconomic
  Forecasting Using Diffusion Indexes,” *Journal of Business &
  Economic Statistics*, 20, 147–162.
* Vershynin (2018)

  Vershynin, R. (2018): *High-dimensional probability: An
  introduction with applications in data science*, vol. 47. Cambridge
  university press.
* Wang and Shojaie (2021)

  Wang, X., and A. Shojaie (2021): “Joint estimation and
  inference for multi-experiment networks of high-dimensional point
  processes,” *arXiv preprint arXiv:2109.11634*.
* Yang (2021)

  Yang, C. F. (2021): “Common factors and spatial dependence: An
  application to US house prices,” *Econometric Reviews*, 40(1), 14–50.
* Yu et al. (2008)

  Yu, J., R. De Jong, and L.-f. Lee (2008): “Quasi-maximum
  likelihood estimators for spatial dynamic panel data with fixed effects when
  both n and T are large,” *Journal of Econometrics*, 146(1), 118–134.

Online Appendix for
  
High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions

The online appendix collects the mathematical proofs that support the main text.

Keywords: Spatial Arbitrage Pricing Theory, Multi-factor Analysis, Yule-Walker Estimation, Eigenanalysis, High Dimension

## IA.A Proofs of the Theorems

We will use CC or cc to denote a generic constant the value of which may change at different places.

Proof of Theorem 1. We only consider a one-period economy and omit the subscript index tt. We consider a small perturbation of the tangency portfolio rj,Mr\_{j,M} and start with a portfolio consisting of rjr\_{j}, rj,Mr\_{j,M}, and rfr\_{f} with weights α\alpha, 11, and −α-\alpha, respective. The total wealth is (α+1−α)=1(\alpha+1-\alpha)=1. Denote the new portfolio by rαr\_{\alpha} and it can be written as

|  |  |  |
| --- | --- | --- |
|  | rα=rj,M+α​rj−α​rf.r\_{\alpha}=r\_{j,M}+\alpha r\_{j}-\alpha r\_{f}. |  |

The variance of rαr\_{\alpha} is

|  |  |  |
| --- | --- | --- |
|  | σα2=Var​(rj,M+α​rj−α​rf)=σj,M2+2​α​γj,M+α2​σj2,\sigma\_{\alpha}^{2}=\textnormal{Var}(r\_{j,M}+\alpha r\_{j}-\alpha r\_{f})=\sigma\_{j,M}^{2}+2\alpha\gamma\_{j,M}+\alpha^{2}\sigma\_{j}^{2}, |  |

where σj,M2=Var​(rj,M)\sigma\_{j,M}^{2}=\textnormal{Var}(r\_{j,M}), σj2=Var​(rj)\sigma\_{j}^{2}=\textnormal{Var}(r\_{j}), and γj,M=Cov​(rj,M,rj)\gamma\_{j,M}=\textnormal{Cov}(r\_{j,M},r\_{j}). The expected return of rαr\_{\alpha} is

|  |  |  |
| --- | --- | --- |
|  | μα=μj,M+α​μj−α​rf.\mu\_{\alpha}=\mu\_{j,M}+\alpha\mu\_{j}-\alpha r\_{f}. |  |

It follows that

|  |  |  |
| --- | --- | --- |
|  | ∂μα∂α=μj−rf,\frac{\partial\mu\_{\alpha}}{\partial\alpha}=\mu\_{j}-r\_{f}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∂σα∂α=12​(σj,M2+2​α​γj,M+α2​σj2)−1/2​(2​γj,M+2​α​σj2).\frac{\partial\sigma\_{\alpha}}{\partial\alpha}=\frac{1}{2}(\sigma\_{j,M}^{2}+2\alpha\gamma\_{j,M}+\alpha^{2}\sigma\_{j}^{2})^{-1/2}(2\gamma\_{j,M}+2\alpha\sigma\_{j}^{2}). |  |

At the tangency portfolio with α=0\alpha=0, it is known from the mean-variance theory that the slop of the capital allocation line (CAL) in Figure [1](https://arxiv.org/html/2511.01271v1#S2.F1 "Figure 1 ‣ 2.2 From CAPM to Spatial CAPM ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") is
μj,M−rfσj,M\frac{\mu\_{j,M}-r\_{f}}{\sigma\_{j,M}} as mentioned above.
On the other hand

|  |  |  |
| --- | --- | --- |
|  | ∂μα/∂α∂σα/∂α|α=0=μj−rfγj,M/σj,M.\frac{\partial\mu\_{\alpha}/\partial\alpha}{\partial\sigma\_{\alpha}/\partial\alpha}|\_{\alpha=0}=\frac{\mu\_{j}-r\_{f}}{\gamma\_{j,M}/\sigma\_{j,M}}. |  |

From the mean-variance theory and the efficiency of the tangency portfolio rj,Mr\_{j,M} on the frontier together with the complete market assumption as Definition [1](https://arxiv.org/html/2511.01271v1#Thmdefinition1 "Definition 1 (Complete Market). ‣ 2.1 Complete Market Assumption ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") and Definition [2](https://arxiv.org/html/2511.01271v1#Thmdefinition2 "Definition 2 (Minimum Complete Market). ‣ 2.1 Complete Market Assumption ‣ 2 Spatial CAMP and Spatial APT ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we can conclude that the ratio between the partial derivatives above is equal to the slope of the capital allocation line:

|  |  |  |
| --- | --- | --- |
|  | μj,M−rfσj,M=μj−rfγj,M/σj,M,\frac{\mu\_{j,M}-r\_{f}}{\sigma\_{j,M}}=\frac{\mu\_{j}-r\_{f}}{\gamma\_{j,M}/\sigma\_{j,M}}, |  |

implying that

|  |  |  |
| --- | --- | --- |
|  | μj−rf=γj,Mσj,M2​(μj,M−rf)=Cov​(rj,𝐰j′​𝐫)Var​(𝐰j′​𝐫)​(μj,M−rf)=ρj​(μj,M−rf),\mu\_{j}-r\_{f}=\frac{\gamma\_{j,M}}{\sigma\_{j,M}^{2}}(\mu\_{j,M}-r\_{f})=\frac{\textnormal{Cov}(r\_{j},{\mathbf{w}}\_{j}^{\prime}{\mathbf{r}})}{\textnormal{Var}({\mathbf{w}}\_{j}^{\prime}{\mathbf{r}})}(\mu\_{j,M}-r\_{f})=\rho\_{j}(\mu\_{j,M}-r\_{f}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | ρj=Cov​(rj,𝐰j′​𝐫)Var​(𝐰j′​𝐫),\rho\_{j}=\frac{\textnormal{Cov}(r\_{j},{\mathbf{w}}\_{j}^{\prime}{\mathbf{r}})}{\textnormal{Var}({\mathbf{w}}\_{j}^{\prime}{\mathbf{r}})}, |  |

is the spatial rho associated with the jj-th asset rjr\_{j}. This completes the proof. □\Box

Proof of Theorem [2](https://arxiv.org/html/2511.01271v1#Thmtheorem2 "Theorem 2. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). By ([6](https://arxiv.org/html/2511.01271v1#S3.E6 "In 3.1 Setup ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), it follows that

|  |  |  |
| --- | --- | --- |
|  | 𝚺^y​f=1T​∑t=1T𝐲t​𝐟t′=𝐃​(𝝆)​𝐖​1T​∑t=1T𝐲t​𝐟t′+𝐁​1T​∑t=1T𝐟t​𝐟t′+1T​∑t=1T𝜺t​𝐟t′\widehat{\boldsymbol{\Sigma}}\_{yf}=\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{y}}\_{t}{\mathbf{f}}\_{t}^{\prime}={\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}}\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{y}}\_{t}{\mathbf{f}}\_{t}^{\prime}+{\mathbf{B}}\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\mathbf{f}}\_{t}^{\prime}+\frac{1}{T}\sum\_{t=1}^{T}\mbox{$\varepsilon$}\_{t}{\mathbf{f}}\_{t}^{\prime} |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝚺^y​f​(1)=1T​∑t=2T𝐲t​𝐟t−1′=𝐃​(𝝆)​𝐖​1T​∑t=2T𝐲t​𝐟t−k′+𝐁​1T​∑t=2T𝐟t​𝐟t−1′+1T​∑t=2T𝜺t​𝐟t−1′.\widehat{\boldsymbol{\Sigma}}\_{yf}(1)=\frac{1}{T}\sum\_{t=2}^{T}{\mathbf{y}}\_{t}{\mathbf{f}}\_{t-1}^{\prime}={\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}}\frac{1}{T}\sum\_{t=2}^{T}{\mathbf{y}}\_{t}{\mathbf{f}}\_{t-k}^{\prime}+{\mathbf{B}}\frac{1}{T}\sum\_{t=2}^{T}{\mathbf{f}}\_{t}{\mathbf{f}}\_{t-1}^{\prime}+\frac{1}{T}\sum\_{t=2}^{T}\mbox{$\varepsilon$}\_{t}{\mathbf{f}}\_{t-1}^{\prime}. |  |

Then,

|  |  |  |
| --- | --- | --- |
|  | 𝚺^y​f′​𝐞i=𝚺^y​f′​𝐰i​ρi+𝚺^f​𝐛i+𝚺^ε​f′​𝐞i,\widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}{\mathbf{e}}\_{i}=\widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}{\mathbf{w}}\_{i}\rho\_{i}+\widehat{\boldsymbol{\Sigma}}\_{f}{\mathbf{b}}\_{i}+\widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}^{\prime}{\mathbf{e}}\_{i}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝚺^y​f​(1)′​𝐞i=𝚺^y​f​(1)′​𝐰i​ρi+𝚺^f​(1)′​𝐛i+𝚺^ε​f​(1)′​𝐞i.\widehat{\boldsymbol{\Sigma}}\_{yf}(1)^{\prime}{\mathbf{e}}\_{i}=\widehat{\boldsymbol{\Sigma}}\_{yf}(1)^{\prime}{\mathbf{w}}\_{i}\rho\_{i}+\widehat{\boldsymbol{\Sigma}}\_{f}(1)^{\prime}{\mathbf{b}}\_{i}+\widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}(1)^{\prime}{\mathbf{e}}\_{i}. |  |

Therefore, we obtain that

|  |  |  |
| --- | --- | --- |
|  | 𝐘^i=(𝚺^y​f′​𝐰i𝚺^f′𝚺^y​f​(1)′​𝐰i𝚺^f​(1)′)​𝜷i+(𝚺^ε​f′​𝐞i𝚺^ε​f​(1)′​𝐞i)=𝐗^i​𝜷i+(𝚺^ε​f′​𝐞i𝚺^ε​f​(1)′​𝐞i).\widehat{\mathbf{Y}}\_{i}=\left(\begin{array}[]{cc}\widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}{\mathbf{w}}\_{i}&\widehat{\boldsymbol{\Sigma}}\_{f}^{\prime}\\ \widehat{\boldsymbol{\Sigma}}\_{yf}(1)^{\prime}{\mathbf{w}}\_{i}&\widehat{\boldsymbol{\Sigma}}\_{f}(1)^{\prime}\end{array}\right)\boldsymbol{\beta}\_{i}+\left(\begin{array}[]{c}\widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}^{\prime}{\mathbf{e}}\_{i}\\ \widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}(1)^{\prime}{\mathbf{e}}\_{i}\end{array}\right)=\widehat{\mathbf{X}}\_{i}\boldsymbol{\beta}\_{i}+\left(\begin{array}[]{c}\widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}^{\prime}{\mathbf{e}}\_{i}\\ \widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}(1)^{\prime}{\mathbf{e}}\_{i}\end{array}\right). |  |

It follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜷^i​(λi)=(𝐗^i​(λi))−1​𝐗^i′​𝐘^i=(𝐗^i​(λi))−1​𝐗^i′​𝐗^i​𝜷i+(𝐗^i​(λi))−1​𝐗^i′​(𝚺^ε​f′​𝐞i𝚺^ε​f​(1)′​𝐞i),\widehat{\boldsymbol{\beta}}\_{i}(\lambda\_{i})=(\widehat{\mathbf{X}}\_{i}(\lambda\_{i}))^{-1}\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{Y}}\_{i}=(\widehat{\mathbf{X}}\_{i}(\lambda\_{i}))^{-1}\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i}\boldsymbol{\beta}\_{i}+(\widehat{\mathbf{X}}\_{i}(\lambda\_{i}))^{-1}\widehat{\mathbf{X}}\_{i}^{\prime}\left(\begin{array}[]{c}\widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}^{\prime}{\mathbf{e}}\_{i}\\ \widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}(1)^{\prime}{\mathbf{e}}\_{i}\end{array}\right), |  | (IA.1) |

where 𝐗^i​(λi)=𝐗^i′​𝐗^i+λi​𝐈K+1\widehat{\mathbf{X}}\_{i}(\lambda\_{i})=\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i}+\lambda\_{i}{\mathbf{I}}\_{K+1}.
By Assumption [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") and a similar argument as that in (A.2) of the supplement of Gao and Tsay ([2022](https://arxiv.org/html/2511.01271v1#bib.bib23)), we can show that

|  |  |  |
| --- | --- | --- |
|  | ‖𝚺^y​f′​(k)​𝐰i−𝚺y​f′​(k)​𝐰i‖F=Op​(NT),\|\widehat{\boldsymbol{\Sigma}}\_{yf}^{\prime}(k){\mathbf{w}}\_{i}-\boldsymbol{\Sigma}\_{yf}^{\prime}(k){\mathbf{w}}\_{i}\|\_{F}=O\_{p}(\sqrt{\frac{N}{T}}), |  |

and

|  |  |  |
| --- | --- | --- |
|  | ‖𝚺^f​(k)−𝚺f​(k)‖F=Op​(1T),\|\widehat{\boldsymbol{\Sigma}}\_{f}(k)-\boldsymbol{\Sigma}\_{f}(k)\|\_{F}=O\_{p}(\sqrt{\frac{1}{T}}), |  |

where the first rate N/T\sqrt{N/T} can be reduced if some weak cross-sectional dependence is imposed.
Furthermore, by a similar argument, we can show that

|  |  |  |
| --- | --- | --- |
|  | 𝚺^ε​f​(k)′​𝐞i=1T​∑t=k+1T𝐟t−k​εi,t=Op​(1T).\widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}(k)^{\prime}{\mathbf{e}}\_{i}=\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{f}}\_{t-k}{\varepsilon}\_{i,t}=O\_{p}(\sqrt{\frac{1}{T}}). |  |

Therefore, if N=o​(T)N=o(T), by Assumption [6](https://arxiv.org/html/2511.01271v1#Thmassumption6 "Assumption 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we have

|  |  |  |
| --- | --- | --- |
|  | ‖𝜷^i​(λi)−𝐗^i​(λi)−1​𝐗^i′​𝐗^i​𝜷i‖2≤C​‖(𝐗^i​(λi))−1​𝐗^i′‖2​‖(𝚺^ε​f′​𝐞i𝚺^ε​f​(1)′​𝐞i)‖2=Op​(T−1/2),\|\widehat{\boldsymbol{\beta}}\_{i}(\lambda\_{i})-\widehat{\mathbf{X}}\_{i}(\lambda\_{i})^{-1}\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i}\boldsymbol{\beta}\_{i}\|\_{2}\leq C\|(\widehat{\mathbf{X}}\_{i}(\lambda\_{i}))^{-1}\widehat{\mathbf{X}}\_{i}^{\prime}\|\_{2}\left\|\left(\begin{array}[]{c}\widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}^{\prime}{\mathbf{e}}\_{i}\\ \widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}(1)^{\prime}{\mathbf{e}}\_{i}\end{array}\right)\right\|\_{2}=O\_{p}(T^{-1/2}), |  |

and letting λi→0\lambda\_{i}\rightarrow 0,

|  |  |  |
| --- | --- | --- |
|  | ‖(𝐗^i′​𝐗^i)​(𝜷^i−𝜷i)‖2≤C​‖𝐗^i′‖2​‖(𝚺^ε​f′​𝐞i𝚺^ε​f​(1)′​𝐞i)‖2=Op​(T−1/2).\|(\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i})(\widehat{\boldsymbol{\beta}}\_{i}-\boldsymbol{\beta}\_{i})\|\_{2}\leq C\|\widehat{\mathbf{X}}\_{i}^{\prime}\|\_{2}\left\|\left(\begin{array}[]{c}\widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}^{\prime}{\mathbf{e}}\_{i}\\ \widehat{\boldsymbol{\Sigma}}\_{{\varepsilon}f}(1)^{\prime}{\mathbf{e}}\_{i}\end{array}\right)\right\|\_{2}=O\_{p}(T^{-1/2}). |  |

This completes the proof. □\Box

Proof of Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). We only prove the case when NN is diverging in Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")(ii) as the proof for (i) is similar. By ([IA.1](https://arxiv.org/html/2511.01271v1#S1.E1 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")),

|  |  |  |
| --- | --- | --- |
|  | (𝐗^i′​𝐗^i)​(𝜷^i−𝜷i)=𝐗^i′​(1T​∑t=1T𝐟t​εi,t1T​∑t=2T𝐟t−1​εi,t).(\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i})(\widehat{\boldsymbol{\beta}}\_{i}-\boldsymbol{\beta}\_{i})=\widehat{\mathbf{X}}\_{i}^{\prime}\left(\begin{array}[]{c}\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}\\ \frac{1}{T}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}\end{array}\right). |  |

To prove Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")(ii), it is sufficient to show the following two statements,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐗^i′​𝐗^i→p𝐕i,\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i}\rightarrow\_{p}{\mathbf{V}}\_{i}, |  | (IA.2) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​(1T​∑t=1T𝐟t​εi,t1T​∑t=2T𝐟t−1​εi,t)→dN​(𝟎,𝐔i).\sqrt{T}\left(\begin{array}[]{c}\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}\\ \frac{1}{T}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}\end{array}\right)\rightarrow\_{d}N({\bf 0},{\mathbf{U}}\_{i}). |  | (IA.3) |

By a similar argument as that in the proof of Theorem 1 above, we can show that

|  |  |  |
| --- | --- | --- |
|  | 𝐗^i→p𝐗i:=(𝚺y​f′​𝐰i𝚺f′𝚺y​f​(1)′​𝐰i𝚺f​(1)′),\widehat{\mathbf{X}}\_{i}\rightarrow\_{p}{\mathbf{X}}\_{i}:=\left(\begin{array}[]{cc}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}&\boldsymbol{\Sigma}\_{f}^{\prime}\\ \boldsymbol{\Sigma}\_{yf}(1)^{\prime}{\mathbf{w}}\_{i}&\boldsymbol{\Sigma}\_{f}(1)^{\prime}\end{array}\right), |  |

if N=o​(T)N=o(T). Therefore, we have

|  |  |  |
| --- | --- | --- |
|  | 𝐗^i′​𝐗^i→p(𝐰i′​𝚺y​f​𝚺y​f′​𝐰i+𝐰i′​𝚺y​f​(1)​𝚺y​f′​(1)​𝐰i𝐰i′​𝚺y​f​𝚺f​𝐰i+𝐰i′​𝚺y​f​(1)​𝚺f′​(1)𝚺f​𝚺y​f′​𝐰i+𝚺f​(1)​𝚺y​f′​(1)​𝐰i𝚺f2+𝚺f​(1)​𝚺f′​(1))=𝐕i.\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i}\rightarrow\_{p}\left(\begin{array}[]{cc}{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f}{\mathbf{w}}\_{i}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1)\\ \boldsymbol{\Sigma}\_{f}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}+\boldsymbol{\Sigma}\_{f}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&\boldsymbol{\Sigma}\_{f}^{2}+\boldsymbol{\Sigma}\_{f}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1)\end{array}\right)={\mathbf{V}}\_{i}. |  |

By a similar argument as that in the proof of Theorem [2](https://arxiv.org/html/2511.01271v1#Thmtheorem2 "Theorem 2. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we can show that

|  |  |  |
| --- | --- | --- |
|  | 𝐗^i′​𝐗^i−𝐗i′​𝐗i=Op​(N−1/2​T1/2),\widehat{\mathbf{X}}\_{i}^{\prime}\widehat{\mathbf{X}}\_{i}-{\mathbf{X}}\_{i}^{\prime}{\mathbf{X}}\_{i}=O\_{p}(N^{-1/2}T^{1/2}), |  |

which implies ([IA.2](https://arxiv.org/html/2511.01271v1#S1.E2 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) if N=o​(T)N=o(T).
To show ([IA.3](https://arxiv.org/html/2511.01271v1#S1.E3 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), it is sufficient to prove that, for any vector 𝐚=(𝐚1′,𝐚2′)′{\mathbf{a}}=({\mathbf{a}}\_{1}^{\prime},{\mathbf{a}}\_{2}^{\prime})^{\prime} with 𝐚1∈RK{\mathbf{a}}\_{1}\in R^{K} and 𝐚2∈RK{\mathbf{a}}\_{2}\in R^{K},

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​𝐚′​(1T​∑t=1T𝐟t​εi,t1T​∑t=2T𝐟t−1​εi,t)=𝐚1′​1T​∑t=1T𝐟t​εi,t+𝐚2′​1T​∑t=1T𝐟t−1​εi,t\displaystyle\sqrt{T}{\mathbf{a}}^{\prime}\left(\begin{array}[]{c}\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}\\ \frac{1}{T}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}\end{array}\right)={\mathbf{a}}\_{1}^{\prime}\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}+{\mathbf{a}}\_{2}^{\prime}\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t} |  | (IA.6) |

is asymptotically normal.
Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐒N,T=a1​1T​∑t=1T𝐟t​εi,t+𝐚2′​1T​∑t=2T𝐟t−1​εi,t,\displaystyle{\mathbf{S}}\_{N,T}=a\_{1}\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}+{\mathbf{a}}\_{2}^{\prime}\frac{1}{\sqrt{T}}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}, |  | (IA.8) |

we only need to show the asymptotic normality of 𝐒N,T{\mathbf{S}}\_{N,T}. By Schwarz’s Inequality and Assumptions [2](https://arxiv.org/html/2511.01271v1#Thmassumption2 "Assumption 2. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") and [5](https://arxiv.org/html/2511.01271v1#Thmassumption5 "Assumption 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we can derive that

|  |  |  |
| --- | --- | --- |
|  | E​|𝐟t​εi,t|γ≤(E​|𝐟t|2​γ)1/2​(E​|εi​t|2​γ)1/2<∞.E|{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}|^{\gamma}\leq(E|{\mathbf{f}}\_{t}|^{2\gamma})^{1/2}(E|{\varepsilon}\_{it}|^{2\gamma})^{1/2}<\infty. |  |

We now calculate the variance of 𝐒N,T{\mathbf{S}}\_{N,T}. Since it involves 16 terms in total and we start with the first term in ([IA.8](https://arxiv.org/html/2511.01271v1#S1.E8 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). By definition and an elementary argument, we have

|  |  |  |
| --- | --- | --- |
|  | Var​(1T​∑t=1T𝐟t​εi,t)=𝚺f​εi​(0)+∑j=1T−1(1−jT)​𝚺f​εi​(0,j).\textnormal{Var}(\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t})=\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0)+\sum\_{j=1}^{T-1}(1-\frac{j}{T})\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0,j). |  |

Note that ∑j=1∞αN​(j)1−2/γ<∞\sum\_{j=1}^{\infty}\alpha\_{N}(j)^{1-2/\gamma}<\infty from Assumption [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), by Proposition 2.5 of Fan and Yao ([2003](https://arxiv.org/html/2511.01271v1#bib.bib16)), we have

|  |  |  |
| --- | --- | --- |
|  | supi∑j=1∞|𝚺f​εi​(0,j)|≤C​supi∑j=1∞α​(j)1−2/γ​(E​|𝐟t|2​γ)1/γ​(E​|εi,t|2​γ)1/γ<∞.\displaystyle\sup\_{i}\sum\_{j=1}^{\infty}|\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0,j)|\leq C\sup\_{i}\sum\_{j=1}^{\infty}\alpha(j)^{1-2/\gamma}(E|{\mathbf{f}}\_{t}|^{2\gamma})^{1/\gamma}(E|{\varepsilon}\_{i,t}|^{2\gamma})^{1/\gamma}<\infty. |  |

We can calculate all the terms of 𝐒N,T{\mathbf{S}}\_{N,T} and sum them up, by the Dominated Convergence theorem, we have

|  |  |  |
| --- | --- | --- |
|  | Var​(𝐒N,T)→𝐚′​𝐔i​𝐚.\textnormal{Var}\left({\mathbf{S}}\_{N,T}\right)\rightarrow{\mathbf{a}}^{\prime}{\mathbf{U}}\_{i}{\mathbf{a}}. |  |

To show the asymptotic normality of 𝐒N,T{\mathbf{S}}\_{N,T}, we employ the small-block and large-block techniques commonly used for weakly dependent data. Specifically, we partition the set {1,…,T}\{1,...,T\} into 2​kT+12k\_{T}+1 subsets with large blocks of size lTl\_{T}, small blocks of size sTs\_{T}, and the last remaining set of size T−kT​(lT+sT)T-k\_{T}(l\_{T}+s\_{T}). Let

|  |  |  |
| --- | --- | --- |
|  | lT=[T/log⁡(T)],sT=[T​log⁡(T)]δ,kT=[T/(lT+sT)],l\_{T}=[\sqrt{T}/\log(T)],\,\,s\_{T}=[\sqrt{T}\log(T)]^{\delta},\,\,k\_{T}=[T/(l\_{T}+s\_{T})], |  |

where [x][x] is the greatest integer less than or equal to xx, and 1−2/γ≤δ<11-2/\gamma\leq\delta<1.
It is not hard to see that

|  |  |  |
| --- | --- | --- |
|  | lT/T→0,sT/lT→0,and​kT=O​(T​log⁡(T)).l\_{T}/\sqrt{T}\rightarrow 0,\,\,s\_{T}/l\_{T}\rightarrow 0,\,\,\text{and}\,\,k\_{T}=O(\sqrt{T}\log(T)). |  |

By Assumption [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") that ∑j=1∞αN​(j)1−2/γ\sum\_{j=1}^{\infty}\alpha\_{N}(j)^{1-2/\gamma}, we have αN​(sT)=o​(sT−γ/(γ−2))\alpha\_{N}(s\_{T})=o(s\_{T}^{-\gamma/(\gamma-2)}). It follows that

|  |  |  |
| --- | --- | --- |
|  | kT​αN​(sT)=o​(kT/sTγ/(γ−2))=o​(1).k\_{T}\alpha\_{N}(s\_{T})=o(k\_{T}/s\_{T}^{\gamma/(\gamma-2)})=o(1). |  |

Then,
we rewrite 𝐒N,T{\mathbf{S}}\_{N,T} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐒N,T=\displaystyle{\mathbf{S}}\_{N,T}= | 𝐚1′​1T​∑j=1kT𝝃j(1)+𝐚2′​1T​∑j=1kT𝝃j(2)+𝐚1′​1T​∑j=1kT𝜼j(1)+𝐚2′​1T​∑j=1kT𝜼j(2)\displaystyle{\mathbf{a}}\_{1}^{\prime}\frac{1}{\sqrt{T}}\sum\_{j=1}^{k\_{T}}\boldsymbol{\xi}\_{j}^{(1)}+{\mathbf{a}}\_{2}^{\prime}\frac{1}{\sqrt{T}}\sum\_{j=1}^{k\_{T}}\boldsymbol{\xi}\_{j}^{(2)}+{\mathbf{a}}\_{1}^{\prime}\frac{1}{\sqrt{T}}\sum\_{j=1}^{k\_{T}}\boldsymbol{\eta}\_{j}^{(1)}+{\mathbf{a}}\_{2}^{\prime}\frac{1}{\sqrt{T}}\sum\_{j=1}^{k\_{T}}\boldsymbol{\eta}\_{j}^{(2)} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝐚1′​1T​𝜻j(1)+𝐚2′​1T​𝜻j(2),\displaystyle+{\mathbf{a}}\_{1}^{\prime}\frac{1}{\sqrt{T}}\boldsymbol{\zeta}\_{j}^{(1)}+{\mathbf{a}}\_{2}^{\prime}\frac{1}{\sqrt{T}}\boldsymbol{\zeta}\_{j}^{(2)}, |  | (IA.9) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝝃j(1)=∑t=(j−1)​(lT+sT)+1j​lT+(j−1)​sT𝐟t​εi,t,𝜼j(1)=∑t=j​lT+(j−1)​sT+1j​(lT+sT)𝐟t​εi,t,\boldsymbol{\xi}\_{j}^{(1)}=\sum\_{t=(j-1)(l\_{T}+s\_{T})+1}^{jl\_{T}+(j-1)s\_{T}}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t},\,\,\boldsymbol{\eta}\_{j}^{(1)}=\sum\_{t=jl\_{T}+(j-1)s\_{T}+1}^{j(l\_{T}+s\_{T})}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝜻j(1)=∑t=kT​(lT+sT)+1T𝐟t​εi,t,𝝃j(2)=∑t=(j−1)​(lT+sT)+1j​lT+(j−1)​sT𝐟t−1​εi,t,\boldsymbol{\zeta}\_{j}^{(1)}=\sum\_{t=k\_{T}(l\_{T}+s\_{T})+1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t},\,\,\boldsymbol{\xi}\_{j}^{(2)}=\sum\_{t=(j-1)(l\_{T}+s\_{T})+1}^{jl\_{T}+(j-1)s\_{T}}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝜼j(2)=∑t=j​lT+(j−1)​sT+1j​(lT+sT)𝐟t−1​εi,t,𝜻j(2)=∑t=kT​(lT+sT)+1T𝐟t−1​εi,t,\boldsymbol{\eta}\_{j}^{(2)}=\sum\_{t=jl\_{T}+(j-1)s\_{T}+1}^{j(l\_{T}+s\_{T})}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t},\,\,\boldsymbol{\zeta}\_{j}^{(2)}=\sum\_{t=k\_{T}(l\_{T}+s\_{T})+1}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}, |  |

Note that αN​(T)=o​(T2/γ−1)\alpha\_{N}(T)=o(T^{2/\gamma-1}), kT​sT/T→0k\_{T}s\_{T}/T\rightarrow 0, and (lT+s−T)/T→0(l\_{T}+s-T)/T\rightarrow 0, it follows from Proposition 2.7 of Fan and Yao ([2003](https://arxiv.org/html/2511.01271v1#bib.bib16)) that

|  |  |  |
| --- | --- | --- |
|  | 1T​∑j=1kT𝜼j(l)=op​(1),and​1T​𝜻j(l)=op​(1),l=1,2,3,4.\frac{1}{\sqrt{T}}\sum\_{j=1}^{k\_{T}}\boldsymbol{\eta}\_{j}^{(l)}=o\_{p}(1),\,\,\text{and}\,\,\frac{1}{\sqrt{T}}\boldsymbol{\zeta}\_{j}^{(l)}=o\_{p}(1),\,\,l=1,2,3,4. |  |

Then,

|  |  |  |
| --- | --- | --- |
|  | 𝐒N,T=𝐚1′​1T​∑j=1kT𝝃j(1)+𝐚2′​1T​∑j=1kT𝝃j(2)+op​(1).{\mathbf{S}}\_{N,T}={\mathbf{a}}\_{1}^{\prime}\frac{1}{\sqrt{T}}\sum\_{j=1}^{k\_{T}}\boldsymbol{\xi}\_{j}^{(1)}+{\mathbf{a}}\_{2}^{\prime}\frac{1}{\sqrt{T}}\sum\_{j=1}^{k\_{T}}\boldsymbol{\xi}\_{j}^{(2)}+o\_{p}(1). |  |

By a similar argument as Theorem 2.21 of Fan and Yao ([2003](https://arxiv.org/html/2511.01271v1#bib.bib16)), we can show that

|  |  |  |
| --- | --- | --- |
|  | T​𝐚′​(1T​∑t=1T𝐟t​εi,t1T​∑t=2T𝐟t−1​εi,t)⟶dN​(0,𝐚′​𝐔i​𝐚).\sqrt{T}{\mathbf{a}}^{\prime}\left(\begin{array}[]{c}\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}\\ \frac{1}{T}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}\end{array}\right)\longrightarrow\_{d}N({0},{\mathbf{a}}^{\prime}{\mathbf{U}}\_{i}{\mathbf{a}}). |  |

We replace 𝐚{\mathbf{a}} by (𝐔i−1/2)′​𝐚({\mathbf{U}}\_{i}^{-1/2})^{\prime}{\mathbf{a}} and obtain

|  |  |  |
| --- | --- | --- |
|  | T​𝐚′​𝐔i−1/2​(1T​∑t=1T𝐟t​εi,t1T​∑t=2T𝐟t−1​εi,t)⟶dN​(0,1),\sqrt{T}{\mathbf{a}}^{\prime}{\mathbf{U}}\_{i}^{-1/2}\left(\begin{array}[]{c}\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}\\ \frac{1}{T}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}\end{array}\right)\longrightarrow\_{d}N({0},1), |  |

which implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​𝐔i−1/2​(1T​∑t=1T𝐟t​εi,t1T​∑t=2T𝐟t−1​εi,t)⟶dN​(𝟎,𝐈2​K).\sqrt{T}{\mathbf{U}}\_{i}^{-1/2}\left(\begin{array}[]{c}\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}\\ \frac{1}{T}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}\end{array}\right)\longrightarrow\_{d}N({\bf 0},{\mathbf{I}}\_{2K}). |  | (IA.10) |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​𝐕i​(𝜷^i−𝜷i)⟶dN​(𝟎,𝐗i′​𝐔i​𝐗i).\sqrt{T}{\mathbf{V}}\_{i}(\widehat{\boldsymbol{\beta}}\_{i}-\boldsymbol{\beta}\_{i})\longrightarrow\_{d}N({\bf 0},{\mathbf{X}}\_{i}^{\prime}{\mathbf{U}}\_{i}{\mathbf{X}}\_{i}). |  | (IA.11) |

Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") follows from ([IA.2](https://arxiv.org/html/2511.01271v1#S1.E2 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) and ([IA.11](https://arxiv.org/html/2511.01271v1#S1.E11 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")). This completes the proof. □\Box

Proof of Theorem [4](https://arxiv.org/html/2511.01271v1#Thmtheorem4 "Theorem 4. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺^y​(k)=\displaystyle\widehat{\boldsymbol{\Sigma}}\_{y}(k)= | 1T​∑t=k+1T𝐲t​𝐲t−k′\displaystyle\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{y}}\_{t}{\mathbf{y}}\_{t-k}^{\prime} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1T​∑t=k+1T{𝚲​𝐟t​𝐟t−k′​𝚲′+𝚲​𝐟t​𝝃t−k′+𝝃t​𝐟t​k′​𝚲′+𝝃t​𝝃t−k′}\displaystyle\frac{1}{T}\sum\_{t=k+1}^{T}\{\boldsymbol{\Lambda}{\mathbf{f}}\_{t}{\mathbf{f}}\_{t-k}^{\prime}\boldsymbol{\Lambda}^{\prime}+\boldsymbol{\Lambda}{\mathbf{f}}\_{t}\boldsymbol{\xi}\_{t-k}^{\prime}+\boldsymbol{\xi}\_{t}{\mathbf{f}}\_{tk}^{\prime}\boldsymbol{\Lambda}^{\prime}+\boldsymbol{\xi}\_{t}\boldsymbol{\xi}\_{t-k}^{\prime}\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝚲​1T​∑t=k+1T(𝐟t​𝐟t−k′​𝚲′+𝐟t​𝝃t−k′)+1T​∑t=k+1T(𝝃t​𝐟t−k′​𝚲′+𝝃t​𝝃t−k′)\displaystyle\boldsymbol{\Lambda}\frac{1}{T}\sum\_{t=k+1}^{T}({\mathbf{f}}\_{t}{\mathbf{f}}\_{t-k}^{\prime}\boldsymbol{\Lambda}^{\prime}+{\mathbf{f}}\_{t}\boldsymbol{\xi}\_{t-k}^{\prime})+\frac{1}{T}\sum\_{t=k+1}^{T}(\boldsymbol{\xi}\_{t}{\mathbf{f}}\_{t-k}^{\prime}\boldsymbol{\Lambda}^{\prime}+\boldsymbol{\xi}\_{t}\boldsymbol{\xi}\_{t-k}^{\prime}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝚲​𝐆1,k+𝐆2,k,\displaystyle\boldsymbol{\Lambda}{\mathbf{G}}\_{1,k}+{\mathbf{G}}\_{2,k}, |  | (IA.12) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝐆1,k=1T​∑t=k+1T(𝐟t​𝐟t−k′​𝚲′+𝐟t​𝝃t−k′),𝐆2,k=1T​∑t=k+1T(𝝃t​𝐟t−k′​𝚲′+𝝃t​𝝃t−k′).{\mathbf{G}}\_{1,k}=\frac{1}{T}\sum\_{t=k+1}^{T}({\mathbf{f}}\_{t}{\mathbf{f}}\_{t-k}^{\prime}\boldsymbol{\Lambda}^{\prime}+{\mathbf{f}}\_{t}\boldsymbol{\xi}\_{t-k}^{\prime}),\,\,{\mathbf{G}}\_{2,k}=\frac{1}{T}\sum\_{t=k+1}^{T}(\boldsymbol{\xi}\_{t}{\mathbf{f}}\_{t-k}^{\prime}\boldsymbol{\Lambda}^{\prime}+\boldsymbol{\xi}\_{t}\boldsymbol{\xi}\_{t-k}^{\prime}). |  |

It follows from the definition of 𝐌^\widehat{\mathbf{M}} in ([17](https://arxiv.org/html/2511.01271v1#S3.E17 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐌^=\displaystyle\widehat{\mathbf{M}}= | ∑k=1k0𝚺^y​(k)​𝚺^y′​(k)\displaystyle\sum\_{k=1}^{k\_{0}}\widehat{\boldsymbol{\Sigma}}\_{y}(k)\widehat{\boldsymbol{\Sigma}}\_{y}^{\prime}(k) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑k=1k0(𝚲​𝐆1,k+𝐆2,k)​(𝚲​𝐆1,k+𝐆2,k)′\displaystyle\sum\_{k=1}^{k\_{0}}(\boldsymbol{\Lambda}{\mathbf{G}}\_{1,k}+{\mathbf{G}}\_{2,k})(\boldsymbol{\Lambda}{\mathbf{G}}\_{1,k}+{\mathbf{G}}\_{2,k})^{\prime} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝚲​∑k=1k0𝐆1,k​𝐆1,k′​𝚲′+∑k=1k0(𝚲​𝐆1,k​𝐆2,k′+𝐆2,k​𝐆1,k′​𝚲′+𝐆2,k​𝐆2,k′).\displaystyle\boldsymbol{\Lambda}\sum\_{k=1}^{k\_{0}}{\mathbf{G}}\_{1,k}{\mathbf{G}}\_{1,k}^{\prime}\boldsymbol{\Lambda}^{\prime}+\sum\_{k=1}^{k\_{0}}(\boldsymbol{\Lambda}{\mathbf{G}}\_{1,k}{\mathbf{G}}\_{2,k}^{\prime}+{\mathbf{G}}\_{2,k}{\mathbf{G}}\_{1,k}^{\prime}\boldsymbol{\Lambda}^{\prime}+{\mathbf{G}}\_{2,k}{\mathbf{G}}\_{2,k}^{\prime}). |  | (IA.13) |

Let 𝐕^N​T∈Rr\widehat{\mathbf{V}}\_{NT}\in R^{r} be a diagonal matrix with diagonal elements being the top KK eigenvalues of 𝐌^\widehat{\mathbf{M}}, it follows from Assumptions [3](https://arxiv.org/html/2511.01271v1#Thmassumption3 "Assumption 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") and [4](https://arxiv.org/html/2511.01271v1#Thmassumption4 "Assumption 4. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") that 𝐕^N​T≍O​(N2)\widehat{\mathbf{V}}\_{NT}\asymp O(N^{2}). Since the columns of 𝚲^\widehat{\boldsymbol{\Lambda}} are the eigenvectors of 𝐌^\widehat{\mathbf{M}}, it follows that

|  |  |  |
| --- | --- | --- |
|  | 𝐌^​𝚲^=𝚲^​𝐕^N​T,\widehat{\mathbf{M}}\widehat{\boldsymbol{\Lambda}}=\widehat{\boldsymbol{\Lambda}}\widehat{\mathbf{V}}\_{NT}, |  |

implying that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚲^=\displaystyle\widehat{\boldsymbol{\Lambda}}= | 𝐌^​𝚲^​𝐕^N​T−1\displaystyle\widehat{\mathbf{M}}\widehat{\boldsymbol{\Lambda}}\widehat{\mathbf{V}}\_{NT}^{-1} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝚲​∑k=1k0𝐆1,k​𝐆1,k′​𝚲′​𝚲^​𝐕^N​T−1+∑k=1k0[𝚲​𝐆1,k​𝐆2,k′+𝐆2,k​𝐆1,k′​𝚲′+𝐆2,k​𝐆2,k′]​𝚲^​𝐕^N​T−1.\displaystyle\boldsymbol{\Lambda}\sum\_{k=1}^{k\_{0}}{\mathbf{G}}\_{1,k}{\mathbf{G}}\_{1,k}^{\prime}\boldsymbol{\Lambda}^{\prime}\widehat{\boldsymbol{\Lambda}}\widehat{\mathbf{V}}\_{NT}^{-1}+\sum\_{k=1}^{k\_{0}}\left[\boldsymbol{\Lambda}{\mathbf{G}}\_{1,k}{\mathbf{G}}\_{2,k}^{\prime}+{\mathbf{G}}\_{2,k}{\mathbf{G}}\_{1,k}^{\prime}\boldsymbol{\Lambda}^{\prime}+{\mathbf{G}}\_{2,k}{\mathbf{G}}\_{2,k}^{\prime}\right]\widehat{\boldsymbol{\Lambda}}\widehat{\mathbf{V}}\_{NT}^{-1}. |  | (IA.14) |

Let 𝐇N​T′=∑k=1k0𝐆1,k​𝐆1,k′​𝚲′​𝚲^​𝐕^N​T−1{\mathbf{H}}\_{NT}^{\prime}=\sum\_{k=1}^{k\_{0}}{\mathbf{G}}\_{1,k}{\mathbf{G}}\_{1,k}^{\prime}\boldsymbol{\Lambda}^{\prime}\widehat{\boldsymbol{\Lambda}}\widehat{\mathbf{V}}\_{NT}^{-1}, it follows that 𝐇=Op​(1){\mathbf{H}}=O\_{p}(1) and 𝐇−1=Op​(1){\mathbf{H}}^{-1}=O\_{p}(1). Then ([IA.A](https://arxiv.org/html/2511.01271v1#S1.Ex98 "IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚲^−𝚲​𝐇N​T′=∑k=1k0[𝚲​𝐆1,k​𝐆2,k′+𝐆2,k​𝐆1,k′​𝚲′+𝐆2,k​𝐆2,k′]​𝚲^​𝐕^N​T−1.\widehat{\boldsymbol{\Lambda}}-\boldsymbol{\Lambda}{\mathbf{H}}\_{NT}^{\prime}=\sum\_{k=1}^{k\_{0}}\left[\boldsymbol{\Lambda}{\mathbf{G}}\_{1,k}{\mathbf{G}}\_{2,k}^{\prime}+{\mathbf{G}}\_{2,k}{\mathbf{G}}\_{1,k}^{\prime}\boldsymbol{\Lambda}^{\prime}+{\mathbf{G}}\_{2,k}{\mathbf{G}}\_{2,k}^{\prime}\right]\widehat{\boldsymbol{\Lambda}}\widehat{\mathbf{V}}\_{NT}^{-1}. |  | (IA.15) |

First, by Assumption [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") and a similar argument as that in (A.2) of the supplement of Gao and Tsay ([2022](https://arxiv.org/html/2511.01271v1#bib.bib23)), we can show that

|  |  |  |
| --- | --- | --- |
|  | ‖𝐆1,k‖F=‖1T​∑t=k+1T(𝐟t​𝐟t−k′​𝚲′+𝐟t​𝝃t−k′)‖F=Op​(N)+Op​(1+NT)=Op​(N),\|{\mathbf{G}}\_{1,k}\|\_{F}=\|\frac{1}{T}\sum\_{t=k+1}^{T}({\mathbf{f}}\_{t}{\mathbf{f}}\_{t-k}^{\prime}\boldsymbol{\Lambda}^{\prime}+{\mathbf{f}}\_{t}\boldsymbol{\xi}\_{t-k}^{\prime})\|\_{F}=O\_{p}(\sqrt{N})+O\_{p}(1+\sqrt{\frac{N}{T}})=O\_{p}(\sqrt{N}), |  |

and

|  |  |  |
| --- | --- | --- |
|  | ‖𝐆2,k‖F=‖1T​∑t=k+1T(𝝃t​𝐟t−k′​𝚲′+𝝃t​𝝃t−k′)‖F=Op​(NT​N)+Op​(N2T)=Op​(N2T).\|{\mathbf{G}}\_{2,k}\|\_{F}=\|\frac{1}{T}\sum\_{t=k+1}^{T}(\boldsymbol{\xi}\_{t}{\mathbf{f}}\_{t-k}^{\prime}\boldsymbol{\Lambda}^{\prime}+\boldsymbol{\xi}\_{t}\boldsymbol{\xi}\_{t-k}^{\prime})\|\_{F}=O\_{p}(\sqrt{\frac{N}{T}}\sqrt{N})+O\_{p}(\sqrt{\frac{N^{2}}{T}})=O\_{p}(\sqrt{\frac{N^{2}}{T}}). |  |

Then, it follows from ([IA.15](https://arxiv.org/html/2511.01271v1#S1.E15 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) and the above rates that

|  |  |  |
| --- | --- | --- |
|  | ‖𝚲^−𝚲​𝐇′‖F=Op​(N​N​N2T+N​N​N2T+N2T)​Op​(N/N2)=Op​(NT),\|\widehat{\boldsymbol{\Lambda}}-\boldsymbol{\Lambda}{\mathbf{H}}^{\prime}\|\_{F}=O\_{p}(\sqrt{N}\sqrt{N}\sqrt{\frac{N^{2}}{T}}+\sqrt{N}\sqrt{N}\sqrt{\frac{N^{2}}{T}}+\frac{N^{2}}{T})O\_{p}(\sqrt{N}/N^{2})=O\_{p}(\sqrt{\frac{N}{T}}), |  |

implying that

|  |  |  |
| --- | --- | --- |
|  | 1N​‖𝚲^−𝚲​𝐇′‖F=Op​(T−1/2).\frac{1}{\sqrt{N}}\|\widehat{\boldsymbol{\Lambda}}-\boldsymbol{\Lambda}{\mathbf{H}}^{\prime}\|\_{F}=O\_{p}(T^{-1/2}). |  |

This completes the proof of Theorem [4](https://arxiv.org/html/2511.01271v1#Thmtheorem4 "Theorem 4. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). □\Box

###### Lemma 1.

Let Assumptions [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")–[8](https://arxiv.org/html/2511.01271v1#Thmassumption8 "Assumption 8. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") hold. Then, as N,T→∞N,T\rightarrow\infty,

|  |  |  |
| --- | --- | --- |
|  | 𝐇N​T​𝐇N​T′=𝐈K+Op​(T−1/2),and​𝐇N​T′​𝐇N​T=𝐈K+Op​(T−1/2).{\mathbf{H}}\_{NT}{\mathbf{H}}\_{NT}^{\prime}={\mathbf{I}}\_{K}+O\_{p}(T^{-1/2}),\,\,\text{and}\,\,{\mathbf{H}}\_{NT}^{\prime}{\mathbf{H}}\_{NT}={\mathbf{I}}\_{K}+O\_{p}(T^{-1/2}). |  |

Proof. First, note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐇N​T​𝐇N​T′−𝐈K=\displaystyle{\mathbf{H}}\_{NT}{\mathbf{H}}\_{NT}^{\prime}-{\mathbf{I}}\_{K}= | 𝐇N​T​𝚲′​𝚲N​𝐇N​T′−𝚲^′​𝚲^N\displaystyle{\mathbf{H}}\_{NT}\frac{\boldsymbol{\Lambda}^{\prime}\boldsymbol{\Lambda}}{N}{\mathbf{H}}\_{NT}^{\prime}-\frac{\widehat{\boldsymbol{\Lambda}}^{\prime}\widehat{\boldsymbol{\Lambda}}}{N} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 1N​(𝐇N​T​𝚲′−𝚲^′)​1N​𝚲​𝐇N​T′+1N​𝚲^′​(𝚲​𝐇N​T′−𝚲^)/N.\displaystyle\frac{1}{\sqrt{N}}({\mathbf{H}}\_{NT}\boldsymbol{\Lambda}^{\prime}-\widehat{\boldsymbol{\Lambda}}^{\prime})\frac{1}{\sqrt{N}}\boldsymbol{\Lambda}{\mathbf{H}}\_{NT}^{\prime}+\frac{1}{\sqrt{N}}\widehat{\boldsymbol{\Lambda}}^{\prime}(\boldsymbol{\Lambda}{\mathbf{H}}\_{NT}^{\prime}-\widehat{\boldsymbol{\Lambda}})/\sqrt{N}. |  | (IA.16) |

Then, it follows from Theorem 3 that

|  |  |  |
| --- | --- | --- |
|  | ‖𝐇N​T​𝐇N​T′−𝐈K‖F=Op​(T−1/2).\|{\mathbf{H}}\_{NT}{\mathbf{H}}\_{NT}^{\prime}-{\mathbf{I}}\_{K}\|\_{F}=O\_{p}(T^{-1/2}). |  |

Furthermore, since 𝐇N​T=Op​(1){\mathbf{H}}\_{NT}=O\_{p}(1) and 𝐇N​T−1=Op​(1){\mathbf{H}}\_{NT}^{-1}=O\_{p}(1), then

|  |  |  |
| --- | --- | --- |
|  | 𝐇N​T′​𝐇N​T​𝐇N​T′=𝐇N​T′+Op​(T−1/2),{\mathbf{H}}\_{NT}^{\prime}{\mathbf{H}}\_{NT}{\mathbf{H}}\_{NT}^{\prime}={\mathbf{H}}\_{NT}^{\prime}+O\_{p}(T^{-1/2}), |  |

we multiply 𝐇N​T−1{\mathbf{H}}\_{NT}^{-1} on the right of both sides and obtain

|  |  |  |
| --- | --- | --- |
|  | 𝐇N​T′​𝐇N​T=𝐈K+Op​(T−1/2).{\mathbf{H}}\_{NT}^{\prime}{\mathbf{H}}\_{NT}={\mathbf{I}}\_{K}+O\_{p}(T^{-1/2}). |  |

This completes the proof. □\Box

###### Lemma 2.

Let Assumptions [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")–[8](https://arxiv.org/html/2511.01271v1#Thmassumption8 "Assumption 8. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") hold. Then, as N,T→∞N,T\rightarrow\infty,

|  |  |  |
| --- | --- | --- |
|  | 𝚲^′​𝐌^​𝚲^=𝐕^N​T→p𝐕,\widehat{\boldsymbol{\Lambda}}^{\prime}\widehat{\mathbf{M}}\widehat{\boldsymbol{\Lambda}}=\widehat{\mathbf{V}}\_{NT}\rightarrow\_{p}{\mathbf{V}}, |  |

where 𝐕{\mathbf{V}} is a diagonal matrix consisting of the top KK eigenvalues of 𝐌{\mathbf{M}} defined in ([16](https://arxiv.org/html/2511.01271v1#S3.E16 "In 3.4 Estimation When Factors Are Latent ‣ 3 General Model and Methodology ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")).

Proof. The proof is similar to Theorem 1 of Lam and Yao ([2012](https://arxiv.org/html/2511.01271v1#bib.bib30)). We omit the details to save space. □\Box

###### Lemma 3.

Let Assumptions [1](https://arxiv.org/html/2511.01271v1#Thmassumption1 "Assumption 1. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")–[8](https://arxiv.org/html/2511.01271v1#Thmassumption8 "Assumption 8. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions") hold. Then there exists an orthogonal matrix 𝐇∈RK{\mathbf{H}}\in R^{K} such that
𝐇N​T→p𝐇{\mathbf{H}}\_{NT}\rightarrow\_{p}{\mathbf{H}} with probability tending to one as N,T→∞N,T\rightarrow\infty.

Proof. Note that

|  |  |  |
| --- | --- | --- |
|  | 𝐆1,k=𝚺^f​(k)​𝚲′+𝚺^f​ξ​(k).{\mathbf{G}}\_{1,k}=\widehat{\boldsymbol{\Sigma}}\_{f}(k)\boldsymbol{\Lambda}^{\prime}+\widehat{\boldsymbol{\Sigma}}\_{f\xi}(k). |  |

If N=o​(T)N=o(T), we have that 𝚺^f​(k)→p𝚺f​(k)\widehat{\boldsymbol{\Sigma}}\_{f}(k)\rightarrow\_{p}\boldsymbol{\Sigma}\_{f}(k) and 𝚺^f​ξ​(k)→p𝚺f​ξ​(k)\widehat{\boldsymbol{\Sigma}}\_{f\xi}(k)\rightarrow\_{p}\boldsymbol{\Sigma}\_{f\xi}(k).
By definition,

|  |  |  |
| --- | --- | --- |
|  | 𝐇N​T′=∑k=1k0𝐆1,k​𝐆1,k′​𝚲′​𝚲^​𝐕^N​T−1=∑k=1k0𝐆1,k​𝐆1,k′​𝚲′​𝚲​𝐇N​T′​𝐕−1+op​(1).{\mathbf{H}}\_{NT}^{\prime}=\sum\_{k=1}^{k\_{0}}{\mathbf{G}}\_{1,k}{\mathbf{G}}\_{1,k}^{\prime}\boldsymbol{\Lambda}^{\prime}\widehat{\boldsymbol{\Lambda}}\widehat{\mathbf{V}}\_{NT}^{-1}=\sum\_{k=1}^{k\_{0}}{\mathbf{G}}\_{1,k}{\mathbf{G}}\_{1,k}^{\prime}\boldsymbol{\Lambda}^{\prime}\boldsymbol{\Lambda}{\mathbf{H}}\_{NT}^{\prime}{\mathbf{V}}^{-1}+o\_{p}(1). |  |

Then, by Lemma [1](https://arxiv.org/html/2511.01271v1#Thmlemma1 "Lemma 1. ‣ IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐇N​T′​𝐕N2​𝐇N​T=\displaystyle{\mathbf{H}}\_{NT}^{\prime}\frac{{\mathbf{V}}}{N^{2}}{\mathbf{H}}\_{NT}= | 1N∑k=1k0(𝚺f(k)𝚲′+𝚺f​ξ(k)))(𝚺f(k)𝚲′+𝚺f​ξ(k)))′+op(1)\displaystyle\frac{1}{N}\sum\_{k=1}^{k\_{0}}(\boldsymbol{\Sigma}\_{f}(k)\boldsymbol{\Lambda}^{\prime}+\boldsymbol{\Sigma}\_{f\xi}(k)))(\boldsymbol{\Sigma}\_{f}(k)\boldsymbol{\Lambda}^{\prime}+\boldsymbol{\Sigma}\_{f\xi}(k)))^{\prime}+o\_{p}(1) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∑k=1k0𝚺f​(k)​𝚺f′​(k)+op​(1).\displaystyle\sum\_{k=1}^{k\_{0}}\boldsymbol{\Sigma}\_{f}(k)\boldsymbol{\Sigma}\_{f}^{\prime}(k)+o\_{p}(1). |  | (IA.17) |

Therefore, 𝐇N​T{\mathbf{H}}\_{NT} will converge to the matrix consisting of the eigenvectors of ∑k=1k0𝚺f​(k)​𝚺f′​(k)\sum\_{k=1}^{k\_{0}}\boldsymbol{\Sigma}\_{f}(k)\boldsymbol{\Sigma}\_{f}^{\prime}(k), denoted by 𝐇{\mathbf{H}}. This completes the proof. □\Box

Proof of Theorem [5](https://arxiv.org/html/2511.01271v1#Thmtheorem5 "Theorem 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). We first show Theorem [5](https://arxiv.org/html/2511.01271v1#Thmtheorem5 "Theorem 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")(i). Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐟^t=\displaystyle\widehat{\mathbf{f}}\_{t}= | 1N​𝚲^′​𝐲t\displaystyle\frac{1}{N}\widehat{\boldsymbol{\Lambda}}^{\prime}{\mathbf{y}}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1N​𝚲^′​(𝚲​𝐟t+𝝃t)\displaystyle\frac{1}{N}\widehat{\boldsymbol{\Lambda}}^{\prime}(\boldsymbol{\Lambda}{\mathbf{f}}\_{t}+\boldsymbol{\xi}\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1N​𝚲^′​𝚲​𝐟t+1N​𝚲^′​𝝃t\displaystyle\frac{1}{N}\widehat{\boldsymbol{\Lambda}}^{\prime}\boldsymbol{\Lambda}{\mathbf{f}}\_{t}+\frac{1}{N}\widehat{\boldsymbol{\Lambda}}^{\prime}\boldsymbol{\xi}\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝐊N​T​𝐟t+1N​(𝚲^−𝚲​𝐇N​T′)′​𝝃t+1N​𝐇N​T​𝚲′​𝝃t,\displaystyle{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t}+\frac{1}{N}(\widehat{\boldsymbol{\Lambda}}-\boldsymbol{\Lambda}{\mathbf{H}}\_{NT}^{\prime})^{\prime}\boldsymbol{\xi}\_{t}+\frac{1}{N}{\mathbf{H}}\_{NT}\boldsymbol{\Lambda}^{\prime}\boldsymbol{\xi}\_{t}, |  | (IA.18) |

where 𝐊N​T=1N​𝚲^′​𝚲{\mathbf{K}}\_{NT}=\frac{1}{N}\widehat{\boldsymbol{\Lambda}}^{\prime}\boldsymbol{\Lambda} which has the same limit 𝐇{\mathbf{H}} as that of 𝐇N​T{\mathbf{H}}\_{NT}, but they are not identical in finite samples.
By Assumption [7](https://arxiv.org/html/2511.01271v1#Thmassumption7 "Assumption 7. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), it is not hard to show that

|  |  |  |
| --- | --- | --- |
|  | max1≤t≤t⁡|fi,t|=Op​(log⁡(T)),and​max1≤t≤T⁡|εi,t|=Op​(log⁡(T)).\max\_{1\leq t\leq t}|f\_{i,t}|=O\_{p}(\log(T)),\,\,\text{and}\,\,\max\_{1\leq t\leq T}|{\varepsilon}\_{i,t}|=O\_{p}(\log(T)). |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | max1≤t≤T⁡‖1N​(𝚲^−𝚲​𝐇N​T′)′​𝝃t‖F≤1N​‖𝚲^−𝚲​𝐇N​T′‖F​max1≤t≤T⁡‖𝝃tN‖F=Op​(T−1/2​log⁡(T)),\max\_{1\leq t\leq T}\|\frac{1}{N}(\widehat{\boldsymbol{\Lambda}}-\boldsymbol{\Lambda}{\mathbf{H}}\_{NT}^{\prime})^{\prime}\boldsymbol{\xi}\_{t}\|\_{F}\leq\frac{1}{\sqrt{N}}\|\widehat{\boldsymbol{\Lambda}}-\boldsymbol{\Lambda}{\mathbf{H}}\_{NT}^{\prime}\|\_{F}\max\_{1\leq t\leq T}\|\frac{\boldsymbol{\xi}\_{t}}{\sqrt{N}}\|\_{F}=O\_{p}(T^{-1/2}\log(T)), |  |

and

|  |  |  |
| --- | --- | --- |
|  | max1≤t≤T⁡‖1N​𝐇N​T​𝚲′​𝝃t‖F≤C​1N​‖𝐇N​T‖F​max1≤t≤T⁡‖1N​𝚲′​𝝃t‖F=Op​(N−1/2​log⁡(T)).\max\_{1\leq t\leq T}\|\frac{1}{N}{\mathbf{H}}\_{NT}\boldsymbol{\Lambda}^{\prime}\boldsymbol{\xi}\_{t}\|\_{F}\leq C\frac{1}{\sqrt{N}}\|{\mathbf{H}}\_{NT}\|\_{F}\max\_{1\leq t\leq T}\|\frac{1}{\sqrt{N}}\boldsymbol{\Lambda}^{\prime}\boldsymbol{\xi}\_{t}\|\_{F}=O\_{p}(N^{-1/2}\log(T)). |  |

Then, it follows from the above rates that

|  |  |  |
| --- | --- | --- |
|  | max1≤t≤t⁡‖𝐟^t−𝐊N​T​𝐟t‖F=Op​((1T+1N)​log⁡(T)).\max\_{1\leq t\leq t}\|\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t}\|\_{F}=O\_{p}((\frac{1}{\sqrt{T}}+\frac{1}{\sqrt{N}})\log(T)). |  |

This proves Theorem [5](https://arxiv.org/html/2511.01271v1#Thmtheorem5 "Theorem 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")(i).

For Theorem [5](https://arxiv.org/html/2511.01271v1#Thmtheorem5 "Theorem 5. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")(ii), if N=o​(T)N=o(T),

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​(𝐟^t−𝐊N​T​𝐟t)=𝐇​1N​𝚲′​𝝃t+op​(1).\sqrt{N}(\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t})={\mathbf{H}}\frac{1}{\sqrt{N}}\boldsymbol{\Lambda}^{\prime}\boldsymbol{\xi}\_{t}+o\_{p}(1). |  | (IA.19) |

By Assumption [8](https://arxiv.org/html/2511.01271v1#Thmassumption8 "Assumption 8. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we have

|  |  |  |
| --- | --- | --- |
|  | N​(𝐟^t−𝐊N​T​𝐟t)⟶dN​(0,𝐇​𝚪t​𝐇′).\sqrt{N}(\widehat{\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t})\longrightarrow\_{d}N(0,{\mathbf{H}}\boldsymbol{\Gamma}\_{t}{\mathbf{H}}^{\prime}). |  |

This completes the proof. □\Box

Proof of Theorem [6](https://arxiv.org/html/2511.01271v1#Thmtheorem6 "Theorem 6. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). We use 𝐇{\mathbf{H}} instead of 𝐇N​T{\mathbf{H}}\_{NT} for simplicity in this proof. By definition,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺~y​f​(k)=\displaystyle\widetilde{\boldsymbol{\Sigma}}\_{yf}(k)= | 1T​∑t=k+1T𝐲t​𝐟^t−k′\displaystyle\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{y}}\_{t}\widehat{\mathbf{f}}\_{t-k}^{\prime} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1T​∑t=k+1T𝐃​(𝝆)​𝐖𝐲t​𝐟^t−k′+𝐁​1T​∑t=k+1T𝐟t​𝐟^t−k′+1T​∑t=k+1T𝜺t​𝐟^t−k′\displaystyle\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}}{\mathbf{y}}\_{t}\widehat{\mathbf{f}}\_{t-k}^{\prime}+{\mathbf{B}}\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{f}}\_{t}\widehat{\mathbf{f}}\_{t-k}^{\prime}+\frac{1}{T}\sum\_{t=k+1}^{T}\mbox{$\varepsilon$}\_{t}\widehat{\mathbf{f}}\_{t-k}^{\prime} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝐃​(𝝆)​𝐖​𝚺~y​f​(k)+𝐁𝐊N​T−1​𝚺~f​(k)+𝐁​1T​∑t=k+1T(𝐟t−𝐊N​T−1​𝐟^t)​𝐟^t−k′+1T​∑t=k+1T𝜺t​𝐟^t−k′.\displaystyle{\mathbf{D}}(\boldsymbol{\rho}){\mathbf{W}}\widetilde{\boldsymbol{\Sigma}}\_{yf}(k)+{\mathbf{B}}{\mathbf{K}}\_{NT}^{-1}\widetilde{\boldsymbol{\Sigma}}\_{f}(k)+{\mathbf{B}}\frac{1}{T}\sum\_{t=k+1}^{T}({\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}^{-1}\widehat{\mathbf{f}}\_{t})\widehat{\mathbf{f}}\_{t-k}^{\prime}+\frac{1}{T}\sum\_{t=k+1}^{T}\mbox{$\varepsilon$}\_{t}\widehat{\mathbf{f}}\_{t-k}^{\prime}. |  | (IA.20) |

Then, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺~y​f​(k)′​𝐞i=𝚺~y​f​(k)′​𝐰i​ρi+𝚺~f​(k)′​(𝐊N​T′)−1​𝐛i+1T​∑t=k+1T𝐟^t−k​(𝐟t−𝐊N​T−1​𝐟^t)′​𝐛i+1T​∑t=k+1T𝐟^t−k​εi,t.\widetilde{\boldsymbol{\Sigma}}\_{yf}(k)^{\prime}{\mathbf{e}}\_{i}=\widetilde{\boldsymbol{\Sigma}}\_{yf}(k)^{\prime}{\mathbf{w}}\_{i}\rho\_{i}+\widetilde{\boldsymbol{\Sigma}}\_{f}(k)^{\prime}({\mathbf{K}}\_{NT}^{\prime})^{-1}{\mathbf{b}}\_{i}+\frac{1}{T}\sum\_{t=k+1}^{T}\widehat{\mathbf{f}}\_{t-k}({\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}^{-1}\widehat{\mathbf{f}}\_{t})^{\prime}{\mathbf{b}}\_{i}+\frac{1}{T}\sum\_{t=k+1}^{T}\widehat{\mathbf{f}}\_{t-k}{\varepsilon}\_{i,t}. |  | (IA.21) |

We now analyze the last two terms. First,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T​∑t=k+1T𝐟^t−k​(𝐟t−𝐊N​T−1​𝐟^t)′​𝐛i=\displaystyle\frac{1}{T}\sum\_{t=k+1}^{T}\widehat{\mathbf{f}}\_{t-k}({\mathbf{f}}\_{t}-{\mathbf{K}}\_{NT}^{-1}\widehat{\mathbf{f}}\_{t})^{\prime}{\mathbf{b}}\_{i}= | 1T​∑t=k+1T(𝐟^t−k−𝐊N​T​𝐟t−k)​(𝐊N​T​𝐟t−𝐟^t)′​(𝐊N​T′)−1​𝐛i\displaystyle\frac{1}{T}\sum\_{t=k+1}^{T}(\widehat{\mathbf{f}}\_{t-k}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t-k})({\mathbf{K}}\_{NT}{\mathbf{f}}\_{t}-\widehat{\mathbf{f}}\_{t})^{\prime}({\mathbf{K}}\_{NT}^{\prime})^{-1}{\mathbf{b}}\_{i} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1T​∑t=k+1T𝐊N​T​𝐟t−k​(𝐊N​T​𝐟t−𝐟^t)′​(𝐊N​T′)−1​𝐛i,\displaystyle+\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t-k}({\mathbf{K}}\_{NT}{\mathbf{f}}\_{t}-\widehat{\mathbf{f}}\_{t})^{\prime}({\mathbf{K}}\_{NT}^{\prime})^{-1}{\mathbf{b}}\_{i}, |  | (IA.22) |

where

|  |  |  |
| --- | --- | --- |
|  | ∥1T∑t=k+1T(𝐟^t−k−𝐊N​T𝐟t−k)(𝐊N​T𝐟t−𝐟^t)′(𝐊N​T′)−1𝐛i∥2=Op((1T+1N)log(T)2).\|\frac{1}{T}\sum\_{t=k+1}^{T}(\widehat{\mathbf{f}}\_{t-k}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t-k})({\mathbf{K}}\_{NT}{\mathbf{f}}\_{t}-\widehat{\mathbf{f}}\_{t})^{\prime}({\mathbf{K}}\_{NT}^{\prime})^{-1}{\mathbf{b}}\_{i}\|\_{2}=O\_{p}((\frac{1}{T}+\frac{1}{N})\log(T)^{2}). |  |

By ([IA.19](https://arxiv.org/html/2511.01271v1#S1.E19 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), and 𝐟t−k{\mathbf{f}}\_{t-k} and 𝝃t\boldsymbol{\xi}\_{t} are uncorrelated, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T​∑t=k+1T𝐊N​T​𝐟t−k​(𝐊N​T​𝐟t−𝐟^t)′​(𝐊N​T′)−1​𝐛i=\displaystyle\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t-k}({\mathbf{K}}\_{NT}{\mathbf{f}}\_{t}-\widehat{\mathbf{f}}\_{t})^{\prime}({\mathbf{K}}\_{NT}^{\prime})^{-1}{\mathbf{b}}\_{i}= | 1T​∑t=k+1T𝐊N​T​𝐟t−k​𝝃t′​(𝚲​𝐇N​T′−𝚲^)​(𝐊N​T)−1​𝐛i/N\displaystyle\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t-k}\boldsymbol{\xi}\_{t}^{\prime}(\boldsymbol{\Lambda}{\mathbf{H}}\_{NT}^{\prime}-\widehat{\boldsymbol{\Lambda}})({\mathbf{K}}\_{NT})^{-1}{\mathbf{b}}\_{i}/N |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −1T​∑t=k+1T𝐊N​T​𝐟t−k​𝝃t′​𝚲​𝐇N​T′​(𝐊N​T)−1​𝐛i/N\displaystyle-\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t-k}\boldsymbol{\xi}\_{t}^{\prime}\boldsymbol{\Lambda}{\mathbf{H}}\_{NT}^{\prime}({\mathbf{K}}\_{NT})^{-1}{\mathbf{b}}\_{i}/N |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | Op​(1T+1N​T).\displaystyle O\_{p}(\frac{1}{T}+\frac{1}{\sqrt{NT}}). |  | (IA.23) |

Next, we consider the last term of ([IA.21](https://arxiv.org/html/2511.01271v1#S1.E21 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")).

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=k+1T𝐟^t−k​εi,t=1T​∑t=k+1T𝐊N​T​𝐟t−k​εi,t+1T​∑t=k+1T(𝐟^t−k−𝐊N​T​𝐟t−k)​εi,t.\frac{1}{T}\sum\_{t=k+1}^{T}\widehat{\mathbf{f}}\_{t-k}{\varepsilon}\_{i,t}=\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t-k}{\varepsilon}\_{i,t}+\frac{1}{T}\sum\_{t=k+1}^{T}(\widehat{\mathbf{f}}\_{t-k}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t-k}){\varepsilon}\_{i,t}. |  |

By a similar argument as ([IA.A](https://arxiv.org/html/2511.01271v1#S1.Ex124 "IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")), we can show that

|  |  |  |
| --- | --- | --- |
|  | ‖1T​∑t=k+1T(𝐟^t−k−𝐊N​T​𝐟t−k)​εi,t‖F=Op​(1T+1N​T).\|\frac{1}{T}\sum\_{t=k+1}^{T}(\widehat{\mathbf{f}}\_{t-k}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t-k}){\varepsilon}\_{i,t}\|\_{F}=O\_{p}(\frac{1}{T}+\frac{1}{\sqrt{NT}}). |  |

Then it follows from ([IA.21](https://arxiv.org/html/2511.01271v1#S1.E21 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) that

|  |  |  |
| --- | --- | --- |
|  | 𝐘~i=𝐗~i𝐊N​T∗𝜷i+(𝐊N​T​1T​∑t=1T𝐟t​εi,t𝐊N​T​1T​∑t=2T𝐟t−1​εi,t)+Op(1N​T+(1T+1N)log(T)2),\widetilde{\mathbf{Y}}\_{i}=\widetilde{\mathbf{X}}\_{i}{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{i}+\left(\begin{array}[]{c}{\mathbf{K}}\_{NT}\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}\\ {\mathbf{K}}\_{NT}\frac{1}{T}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}\end{array}\right)+O\_{p}(\frac{1}{\sqrt{NT}}+(\frac{1}{T}+\frac{1}{N})\log(T)^{2}), |  |

where 𝐊N​T∗=diag​(1,𝐊N​T){\mathbf{K}}\_{NT}^{\*}=\mbox{diag}(1,{\mathbf{K}}\_{NT}) and 𝜷i=(ρi,𝐛i′)′\boldsymbol{\beta}\_{i}=(\rho\_{i},{\mathbf{b}}\_{i}^{\prime})^{\prime}. Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜷~i​(λi)=𝐗~i​(λi)−1​𝐗~i′​𝐗~i​𝐊N​T∗​𝜷i+𝐗~i​(λi)−1​𝐗~i′​(𝐊N​T​1T​∑t=1T𝐟t​εi,t𝐊N​T​1T​∑t=2T𝐟t−1​εi,t)+𝐑i,\widetilde{\boldsymbol{\beta}}\_{i}(\lambda\_{i})=\widetilde{\mathbf{X}}\_{i}(\lambda\_{i})^{-1}\widetilde{\mathbf{X}}\_{i}^{\prime}\widetilde{\mathbf{X}}\_{i}{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{i}+\widetilde{\mathbf{X}}\_{i}(\lambda\_{i})^{-1}\widetilde{\mathbf{X}}\_{i}^{\prime}\left(\begin{array}[]{c}{\mathbf{K}}\_{NT}\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}\\ {\mathbf{K}}\_{NT}\frac{1}{T}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}\end{array}\right)+{\mathbf{R}}\_{i}, |  | (IA.24) |

where 𝐑i{\mathbf{R}}\_{i} is the remaining term, and we will show that T​𝐑i=op​(1)\sqrt{T}{\mathbf{R}}\_{i}=o\_{p}(1). Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺~y​f​(k)=1T​∑t=k+1T𝐲t​𝐟^t−k′=\displaystyle\widetilde{\boldsymbol{\Sigma}}\_{yf}(k)=\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{y}}\_{t}\widehat{\mathbf{f}}\_{t-k}^{\prime}= | 1T​∑t=k+1T𝐲t​𝐟t−k′​𝐊N​T′+1T​∑t=k+1T𝐲t​(𝐟~t−k−𝐊N​T​𝐟t)′\displaystyle\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{y}}\_{t}{\mathbf{f}}\_{t-k}^{\prime}{\mathbf{K}}\_{NT}^{\prime}+\frac{1}{T}\sum\_{t=k+1}^{T}{\mathbf{y}}\_{t}(\widetilde{\mathbf{f}}\_{t-k}-{\mathbf{K}}\_{NT}{\mathbf{f}}\_{t})^{\prime} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝚺^y​f​𝐊N​T′+Op​(N−1/2+T−1/2)\displaystyle\widehat{\boldsymbol{\Sigma}}\_{yf}{\mathbf{K}}\_{NT}^{\prime}+O\_{p}(N^{-1/2}+T^{-1/2}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | →p\displaystyle\rightarrow\_{p} | 𝚺^y​f​𝐊N​T′,\displaystyle\widehat{\boldsymbol{\Sigma}}\_{yf}{\mathbf{K}}\_{NT}^{\prime}, |  | (IA.25) |

if N=o​(T)N=o(T). Similarly, we can show that

|  |  |  |
| --- | --- | --- |
|  | 𝚺~f​(k)=𝐇​𝚺f​(k)​𝐇′+op​(1).\widetilde{\boldsymbol{\Sigma}}\_{f}(k)={\mathbf{H}}\boldsymbol{\Sigma}\_{f}(k){\mathbf{H}}^{\prime}+o\_{p}(1). |  |

Therefore, if N=o​(T)N=o(T),

|  |  |  |
| --- | --- | --- |
|  | 𝐗~i=(𝚺~y​f′​𝐰i𝚺~f′𝚺~y​f′​(1)​𝐰i𝚺~f′​(1))→p𝐗iH=(𝐇​𝚺y​f′​𝐰i𝐇​𝚺f​𝐇′𝐇​𝚺y​f′​(1)​𝐰i𝐇​𝚺f′​(1)​𝐇′),\widetilde{\mathbf{X}}\_{i}=\left(\begin{array}[]{cc}\widetilde{\boldsymbol{\Sigma}}\_{yf}^{\prime}{\mathbf{w}}\_{i}&\widetilde{\boldsymbol{\Sigma}}\_{f}^{\prime}\\ \widetilde{\boldsymbol{\Sigma}}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&\widetilde{\boldsymbol{\Sigma}}\_{f}^{\prime}(1)\end{array}\right)\rightarrow\_{p}{\mathbf{X}}\_{i}^{H}=\left(\begin{array}[]{cc}{\mathbf{H}}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}&{\mathbf{H}}\boldsymbol{\Sigma}\_{f}{\mathbf{H}}^{\prime}\\ {\mathbf{H}}\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&{\mathbf{H}}\boldsymbol{\Sigma}\_{f}^{\prime}(1){\mathbf{H}}^{\prime}\end{array}\right), |  |

and hence

|  |  |  |
| --- | --- | --- |
|  | 𝐗^i′​𝐗~i→p(𝐰i′​𝚺y​f​𝚺y​f′​𝐰i+𝐰i′​𝚺y​f​(1)​𝚺y​f′​(1)​𝐰i𝐰i′​𝚺y​f​𝚺f​𝐇′+𝐰i′​𝚺y​f​(1)​𝚺f′​(1)​𝐇′𝐇​𝚺f​𝚺y​f′​𝐰i+𝐇​𝚺f​(1)​𝚺y​f′​(1)​𝐰i𝐇​𝚺f2​𝐇′+𝐇​𝚺f​(1)​𝚺f′​(1)​𝐇′)=𝐕iH.\widehat{\mathbf{X}}\_{i}^{\prime}\widetilde{\mathbf{X}}\_{i}\rightarrow\_{p}\left(\begin{array}[]{cc}{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}\boldsymbol{\Sigma}\_{f}{\mathbf{H}}^{\prime}+{\mathbf{w}}\_{i}^{\prime}\boldsymbol{\Sigma}\_{yf}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1){\mathbf{H}}^{\prime}\\ {\mathbf{H}}\boldsymbol{\Sigma}\_{f}\boldsymbol{\Sigma}\_{yf}^{\prime}{\mathbf{w}}\_{i}+{\mathbf{H}}\boldsymbol{\Sigma}\_{f}(1)\boldsymbol{\Sigma}\_{yf}^{\prime}(1){\mathbf{w}}\_{i}&{\mathbf{H}}\boldsymbol{\Sigma}\_{f}^{2}{\mathbf{H}}^{\prime}+{\mathbf{H}}\boldsymbol{\Sigma}\_{f}(1)\boldsymbol{\Sigma}\_{f}^{\prime}(1){\mathbf{H}}^{\prime}\end{array}\right)={\mathbf{V}}\_{i}^{H}. |  |

It follows that

|  |  |  |
| --- | --- | --- |
|  | (𝐗~i′​𝐗~i+λi​𝐈K+1)−1​𝐗~i=Op​(1),(\widetilde{\mathbf{X}}\_{i}^{\prime}\widetilde{\mathbf{X}}\_{i}+\lambda\_{i}{\mathbf{I}}\_{K+1})^{-1}\widetilde{\mathbf{X}}\_{i}=O\_{p}(1), |  |

implying that T​𝐑i=op​(1)\sqrt{T}{\mathbf{R}}\_{i}=o\_{p}(1). Then ([IA.24](https://arxiv.org/html/2511.01271v1#S1.E24 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) implies that

|  |  |  |
| --- | --- | --- |
|  | 𝜷~i​(λi)−𝐗~i​(λi)−1​𝐗~i′​𝐗~i​𝐊N​T∗​𝜷i=Op​(T−1/2).\widetilde{\boldsymbol{\beta}}\_{i}(\lambda\_{i})-\widetilde{\mathbf{X}}\_{i}(\lambda\_{i})^{-1}\widetilde{\mathbf{X}}\_{i}^{\prime}\widetilde{\mathbf{X}}\_{i}{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{i}=O\_{p}(T^{-1/2}). |  |

Let λi→0\lambda\_{i}\rightarrow 0, we obtain that

|  |  |  |
| --- | --- | --- |
|  | T​(𝐗~i′​𝐗~i)​(𝜷~i−𝐊N​T∗​𝜷i)=𝐗~i′​(𝐊N​T​1T​∑t=1T𝐟t​εi,t𝐊N​T​1T​∑t=2T𝐟t−1​εi,t)+op​(1).\sqrt{T}(\widetilde{\mathbf{X}}\_{i}^{\prime}\widetilde{\mathbf{X}}\_{i})(\widetilde{\boldsymbol{\beta}}\_{i}-{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{i})=\widetilde{\mathbf{X}}\_{i}^{\prime}\left(\begin{array}[]{c}{\mathbf{K}}\_{NT}\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}\\ {\mathbf{K}}\_{NT}\frac{1}{\sqrt{T}}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}\end{array}\right)+o\_{p}(1). |  |

By a similar argument as that in the proof of Theorem [3](https://arxiv.org/html/2511.01271v1#Thmtheorem3 "Theorem 3. ‣ 4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​(𝐊N​T​1T​∑t=1T𝐟t​εi,t𝐊N​T​1T​∑t=2T𝐟t−1​εi,t)⟶dN​(𝟎,𝐔iH),\sqrt{T}\left(\begin{array}[]{c}{\mathbf{K}}\_{NT}\frac{1}{T}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}\\ {\mathbf{K}}\_{NT}\frac{1}{T}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}\end{array}\right)\longrightarrow\_{d}N({\bf 0},{{\mathbf{U}}\_{i}^{H}}), |  | (IA.26) |

where

|  |  |  |
| --- | --- | --- |
|  | Var​(𝐊N​T​1T​∑t=1T𝐟t​εi,t𝐊N​T​1T​∑t=2T𝐟t−1​εi,t)→𝐔iH,\textnormal{Var}\left(\begin{array}[]{c}{\mathbf{K}}\_{NT}\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}{\mathbf{f}}\_{t}{\varepsilon}\_{i,t}\\ {\mathbf{K}}\_{NT}\frac{1}{\sqrt{T}}\sum\_{t=2}^{T}{\mathbf{f}}\_{t-1}{\varepsilon}\_{i,t}\end{array}\right)\rightarrow{\mathbf{U}}\_{i}^{H}, |  |

which is defined as

|  |  |  |
| --- | --- | --- |
|  | 𝐔iH=(𝐇​𝚺f​εi​(0)​𝐇′𝐇​𝚺f​εi​(1)​𝐇′𝐇​𝚺f​εi′​(1)​𝐇′𝐇​𝛀f​εi​(0)​𝐇′),{\mathbf{U}}\_{i}^{H}=\left(\begin{array}[]{cc}{\mathbf{H}}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0){\mathbf{H}}^{\prime}&{\mathbf{H}}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1){\mathbf{H}}^{\prime}\\ {\mathbf{H}}\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}^{\prime}(1){\mathbf{H}}^{\prime}&{\mathbf{H}}\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0){\mathbf{H}}^{\prime}\end{array}\right), |  |

where
𝚺f​εi​(0)\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(0), 𝚺f​εi​(1)\boldsymbol{\Sigma}\_{f{\varepsilon}\_{i}}(1), and 𝛀f​εi​(0)\boldsymbol{\Omega}\_{f{\varepsilon}\_{i}}(0) are defined in Section [4](https://arxiv.org/html/2511.01271v1#S4 "4 Theoretical Properties ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions"). It follows from ([IA.26](https://arxiv.org/html/2511.01271v1#S1.E26 "In IA.A Proofs of the Theorems ‣ High-Dimensional Spatial Arbitrage Pricing Theory with Heterogeneous Interactions")) that

|  |  |  |
| --- | --- | --- |
|  | T​𝐕iH​(𝜷^i−𝐊N​T∗​𝜷i)⟶dN​(𝟎,𝐗iH​𝐔iH′​𝐗iH).\sqrt{T}{\mathbf{V}}\_{i}^{H}(\widehat{\boldsymbol{\beta}}\_{i}-{\mathbf{K}}\_{NT}^{\*}\boldsymbol{\beta}\_{i})\longrightarrow\_{d}N({\bf 0},{\mathbf{X}}\_{i}^{H}{{}^{\prime}}{\mathbf{U}}\_{i}^{H}{\mathbf{X}}\_{i}^{H}). |  |

This completes the proof. □\Box