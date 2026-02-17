---
authors:
- Ruike Wu
- Yonghe Lu
- Yanrong Yang
doc_id: arxiv:2602.14439v1
family_id: arxiv:2602.14439
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Sustainable Investment: ESG Impacts on Large Portfolio'
url_abs: http://arxiv.org/abs/2602.14439v1
url_html: https://arxiv.org/html/2602.14439v1
venue: arXiv q-fin
version: 1
year: 2026
---


Ruike Wu
Shanghai University of Finance and Economics
Key Laboratory of Mathematical Economics (Shanghai University of Finance and Economics), Ministry of Education

Yonghe Lu
The Australian National University

Yanrong Yang
The Australian National University

###### Abstract

This paper investigates the impact of environmental, social, and governance (ESG) constraint on a regularized mean-variance (MV) portfolio optimization problem in a large-dimensional setting, in which a positive definite regularization matrix is imposed on the sample covariance matrix. We first derive the asymptotic results for the out-of-sample (OOS) Sharpe ratio (SR) of the proposed portfolio, which help quantify the impact of imposing an ESG-level constraint as well as the effect of estimation error arising from the sample mean estimation of the assets’ ESG score. Furthermore, to study the influence of the choices of the regularization matrix, we develop an estimator for the OOS Sharpe ratio. The corresponding asymptotic properties of the Sharpe ratio estimator are established based on random matrix theory. Simulation results show that the proposed estimators perform close to the corresponding oracle level. Moreover, we numerically investigate the impact of various forms of regularization matrices on the OOS SR, which provides useful guidance for practical implementation.
Finally, based on OOS SR estimator, we propose an adaptive regularized portfolio which uses the best regularization matrix yielding the highest estimated SR (among a set of candidates) at each decision node.
Empirical evidence based on the S&P 500 index demonstrates that the proposed adaptive ESG-constrained portfolio achieves a high OOS SR while satisfying the required ESG level, offering a practically effective approach for sustainable investment.

Keywords: ESG; Large Portfolio; Out-of-sample Sharpe Ratio; Regularization Matrix

## 1 Introduction

The mean-variance (MV) optimization, first introduced by Markowitz ([1952](https://arxiv.org/html/2602.14439v1#bib.bib31 "Portfolio selection")), is a fundamental
cornerstone in modern portfolio allocation theory. For a universe of pp assets, the investors try to choose an allocation 𝒘∗\bm{w}^{\*} to maximize their utility as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘∗=arg⁡max𝒘​𝒘⊤​𝝁−γ2​𝒘⊤​𝚺​𝒘,\displaystyle\bm{w}^{\*}=\underset{\bm{w}}{\arg\max}\;\bm{w}^{\top}{{\bm{\mu}}}-\frac{\gamma}{2}\bm{w}^{\top}{{\bm{\Sigma}}}\bm{w}, |  | (1.1) |

where 𝝁=(μ1,μ2,…,μp)⊤{\bm{\mu}}=\left(\mu\_{1},\mu\_{2},...,\mu\_{p}\right)^{\top} is the expected return of assets return vector 𝒓=(r1,r2,…,rp)⊤\bm{r}=\left(r\_{1},r\_{2},...,r\_{p}\right)^{\top}, and 𝚺{\bm{\Sigma}} is the corresponding covariance matrix, and γ\gamma is a tuning parameter measuring the degree of risk aversion. Clearly, the solution 𝒘∗\bm{w}^{\*} of this optimization problem is 𝚺−1​𝝁/γ{\bm{\Sigma}}^{-1}{\bm{\mu}}/\gamma, which theoretically achieves the maximum Sharpe ratio.

In recent years, motivated by sustainable development goals and rising pro-social preferences, socially responsible investment (SRI) has become a rapidly expanding field. Environmental, social and governance (ESG) concerns—often regarded as ethical and non-financial dimensions of firm performance—have received substantial attention in both academia and industry. A growing number of investors actively allocate capital toward ESG-oriented products, and green or sustainability-themed funds have experienced substantial inflows in global markets. Meanwhile, regulatory initiatives are increasingly pushing investors to incorporate ESG criteria into their portfolio decisions.
Numerous studies incorporate ESG information into portfolio decision and explore the trade-off between sustainability and financial returns (Barber et al., [2021](https://arxiv.org/html/2602.14439v1#bib.bib165 "Impact investing"); Pedersen et al., [2021](https://arxiv.org/html/2602.14439v1#bib.bib173 "Responsible investing: the esg-efficient frontier"); Makridis and Simaan, [2023](https://arxiv.org/html/2602.14439v1#bib.bib166 "Balancing returns and responsibility: evidence from shrinkage-based portfolios"); Berg et al., [2024](https://arxiv.org/html/2602.14439v1#bib.bib167 "Quantifying the returns of esg investing: an empirical analysis with six esg metrics."); Lo and Zhang, [2024](https://arxiv.org/html/2602.14439v1#bib.bib168 "Quantifying the impact of impact investing"); Lauria et al., [2025](https://arxiv.org/html/2602.14439v1#bib.bib12 "Environmental, social and governance-valued portfolio optimization and dynamic asset pricing")). In the mean-variance framework, a widely adopted approach imposes a minimum ESG score constraint, requiring the portfolio average ESG score to exceed a target threshold s¯\bar{s} (Pedersen et al., [2021](https://arxiv.org/html/2602.14439v1#bib.bib173 "Responsible investing: the esg-efficient frontier"); Cesarone et al., [2022](https://arxiv.org/html/2602.14439v1#bib.bib174 "Does esg impact really enhance portfolio profitability?"); De Spiegeleer et al., [2023](https://arxiv.org/html/2602.14439v1#bib.bib169 "ESG: a new dimension in portfolio allocation"); Lo and Zhang, [2025](https://arxiv.org/html/2602.14439v1#bib.bib164 "Performance attribution for portfolio constraints")). As such, investors then seek allocations that maximize their mean-variance utility while ensuring ESG level; see optimization problem ([2.1](https://arxiv.org/html/2602.14439v1#S2.E1 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")). This mechanism embeds ethical intentions directly into the mean-variance portfolio decision process and is elegant mathematically.

However, the primary challenge lies in ensuring trustworthy implementation. In practice, the population parameters 𝝁,𝚺{\bm{\mu}},{\bm{\Sigma}} as well as assets’ ESG mean level are unknown and must be replaced by their empirical estimators. In modern markets, investors often manage hundreds or even thousands of tradable assets while only having access to limited historical observations. As a result, ESG-constrained MV optimization is commonly performed in large- or high-dimensional environments, in which the sample estimators of 𝝁{\bm{\mu}} and 𝚺{\bm{\Sigma}} suffer from severe estimation error and become statistically unreliable (Ao et al., [2019](https://arxiv.org/html/2602.14439v1#bib.bib55 "Approaching mean-variance efficiency for large portfolios"); Ding et al., [2021](https://arxiv.org/html/2602.14439v1#bib.bib54 "High dimensional minimum variance portfolio estimation under statistical factor models"); Fan et al., [2024b](https://arxiv.org/html/2602.14439v1#bib.bib129 "Time-varying minimum variance portfolio"); Bodnar et al., [2022b](https://arxiv.org/html/2602.14439v1#bib.bib48 "Optimal shrinkage-based portfolio selection in high dimensions"); Wu et al., [2025](https://arxiv.org/html/2602.14439v1#bib.bib13 "Making distributionally robust portfolios feasible in high dimension"); Ao et al., [2025](https://arxiv.org/html/2602.14439v1#bib.bib27 "Robust large portfolio optimization with heteroscedastic and heavy-tailed returns"); Meng et al., [2025](https://arxiv.org/html/2602.14439v1#bib.bib170 "Estimation of out-of-sample sharpe ratio for high dimensional portfolio optimization")). Moreover, when the number of assets is larger than the number of historical observations, the sample MV portfolio may even fail. Ethical intentions may be undermined if portfolio performance is overly distorted by estimation errors, resulting in a poorer balance between sustainable objectives and financial outcomes, and raising concerns about responsible decision-making in finance. Thus, ensuring both financial performance and ethical validity of ESG-based allocation under vast data conditions (particularly large assets number) requires statistically principled and trustworthy methodologies.

In this paper, we investigate a regularized ESG-constrained mean–variance portfolios, aiming to achieve high Sharpe ratio while satisfying sustainable investment requirements, in large-dimensional settings. Specifically, based on the sample version of ESG-constrained mean-variance problem, we propose adding a positive-definite regularization matrix to sample covariance matrix.
Although this operation originates from statistical reasoning to address the ill conditioning of sample covariance estimation, imposing regularization on the sample covariance matrix can be equivalently reformulated as a quadratic constraint on the portfolio weights. And when the covariance matrix of the assets’ ESG scores is employed as the regularization matrix, this constraint effectively places an upper bound on the variance of the portfolio’s ESG scores. For the regularized portfolio, we first derive the asymptotic results for the out-of-sample (OOS) Sharpe ratio (SR) of the proposed regularized portfolio based on random matrix theory, which quantifies the impacts of imposing an ESG-level constraint as well as the estimation error, arising from estimating the unknown ESG score mean level, in large dimensional situation. In the special case where the regularization matrix is set to a large multiple of the population covariance matrix, the estimation error in the sample ESG mean score contributes to an improvement in the OOS SR. As a result, we can safely use the sample ESG mean as a proxy for the unknown ESG score in large dimensional situation. Furthermore, the OOS SR performance depends on the choice of the imposed regularization matrix, obtaining a theoretical optimum is challenging in the large-dimensional setting, where the number of assets may diverge with the sample size. Thus, in order to study the impacts of the choice of the regularization matrix on the OOS portfolio SR, we propose an estimator for OOS SR of our newly proposed portfolio. As such, investors can estimate the OOS SRs of the proposed portfolio at each desicion node under various choices of the regularization matrix, and then select the one that delivers the highest Sharpe ratio. The asymptotic consistency of SR estimator is also established.

Our simulation results show that the proposed OOS SR estimator works well and is close to the unknown oracle level under large-dimensional situations when simulation setup is calibrated from real data. Furthermore, we investigate the impacts of several specifications of regularization matrix on portfolio performance. The results show that setting the regularization matrix equal to the unknown true covariance matrix yields the best performance in terms of both SR and ESG score; however, this choice is infeasible in practice. Among feasible candidates, using the identity matrix, the diagonal matrix of the sample covariance matrix, and the nonlinear shrinkage estimator of the covariance matrix proposed by Ledoit and Wolf ([2017](https://arxiv.org/html/2602.14439v1#bib.bib65 "Nonlinear shrinkage of the covariance matrix for portfolio selection: Markowitz meets Goldilocks")) leads to high OOS SR and the required ESG score, beating the naive sample version of ESG-constrained mean-variance portfolio. As such, these feasible choices can serve as useful guidance for practical implementation. Regularization matrices constructed using ESG score information (e.g. using covariance matrix of ESG scores as regularization matrix) fail to deliver satisfactory Sharpe ratio performance, indicating that the existing covariance structure of assets’ ESG scores contributes little to improving performance of sample ESG-constrained mean-variance portfolio when an additional ESG variance constraint is further imposed.

Finally, an empirical analysis based on the components of the S&P 500 index is conducted. Due to the complexity of real data, we apply an adaptive version of the newly proposed portfolio: at each decision node, we first estimate the OOS SR for various candidate regularization matrices (in our study, the candidates include the identity matrix, the diagonal matrix of the sample covariance matrix, and the nonlinear shrinkage covariance matrix estimator), and then select the regularization matrix that exhibits the highest estimated Sharpe ratio.
Compared with other feasible ESG-constrained strategies, the proposed adaptive regularized portfolio achieves first-tier OOS SR performance in most cases, while maintaining the ESG levels that satisfactorily meet the prescribed constraint and exhibit low variability.

This paper makes several contributions to the literature on sustainable investment and constrained large portfolio allocation:

* (1)

  We investigate a regularized ESG-constrained mean–variance optimization problem in large dimensional situation. We derive the limit of OOS SR of the proposed portfolio, which quantifies the impacts of imposing an ESG-level constraint as well as the estimation error from ESG mean level estimator in large dimensional situation.
* (2)

  We develop an estimator for the OOS SR of the regularized portfolio, which is useful for investors to select the best forms of regularization matrix in terms of maximizing OOS SR.
  The asymptotic properties are established based on random matrix theory.
* (3)

  We study the impact of various forms of regularization matrices on the performance of ESG-constrained mean-variance portfolios through simulation experiments, and conclude that, using the identity matrix, the diagonal matrix of the sample return covariance matrix, and the nonlinear shrinkage covariance estimator leads to high OOS Sharpe ratios while satisfying the required ESG score, thereby providing useful guidance for empirical applications.
* (4)

  We propose an adaptive regularized ESG-constrained mean-variance portfolio that uses the regularization matrix yielding the highest estimated OOS Sharpe ratio among a set of candidates at each decision node. The empirical analyses based on S&P 500 constituent data show that, the proposed adaptive portfolio achieves a high OOS SR while obtaining stable ESG scores satisfying the target level well. This provides a practically effective approach for balancing financial performance with sustainability goals.

This paper is related to the studies that integrate ESG information into portfolio selection.
Utz et al. ([2015](https://arxiv.org/html/2602.14439v1#bib.bib44 "Tri-criterion modeling for constructing more-sustainable mutual funds")) incorporate sustainability as a third criterion, in addition to the mean-variance trade-off, within a tri-criterion portfolio selection framework.
Gasser et al. ([2017](https://arxiv.org/html/2602.14439v1#bib.bib10 "Markowitz revisited: social portfolio engineering")), Pedersen et al. ([2021](https://arxiv.org/html/2602.14439v1#bib.bib173 "Responsible investing: the esg-efficient frontier")), and Schmidt ([2022](https://arxiv.org/html/2602.14439v1#bib.bib11 "Optimal esg portfolios: an example for the dow jones index")) incorporate ESG measure into portfolio optimizing utility function, and provide ESG-Sharpe ratio efficient frontier.
Makridis and Simaan ([2023](https://arxiv.org/html/2602.14439v1#bib.bib166 "Balancing returns and responsibility: evidence from shrinkage-based portfolios")) introduce ESG scores into portfolio allocation based on linear shrinkage covariance estimator (Ledoit and Wolf, [2004](https://arxiv.org/html/2602.14439v1#bib.bib46 "A well-conditioned estimator for large-dimensional covariance matrices")), they study the situations where the target matrix is defined using the reciprocal
of the ESG ratings. De Spiegeleer et al. ([2023](https://arxiv.org/html/2602.14439v1#bib.bib169 "ESG: a new dimension in portfolio allocation")) examine the impact of including ESG criteria in the allocation of equity portfolios under mean-variance framework empirically.
Lo and Zhang ([2025](https://arxiv.org/html/2602.14439v1#bib.bib164 "Performance attribution for portfolio constraints")) propose a performance attribution framework for mean-variance optimal portfolio constraints, and study the financial impact of the ESG level constraint empirically.
Lauria et al. ([2025](https://arxiv.org/html/2602.14439v1#bib.bib12 "Environmental, social and governance-valued portfolio optimization and dynamic asset pricing")) incorporate ESG scores into a dynamic asset pricing framework by constructing an ESG-valued log return, defined as a linear combination of the raw return and the scaled ESG scores. All these studies are confined to cases where the sample size substantially exceeds the number of dimensions, and do not examine (theoretically) the performance of constrained portfolios in high-dimensional settings.

This paper also connects to the regularized portfolio allocation and high dimensional portfolio allocation. DeMiguel et al. ([2009a](https://arxiv.org/html/2602.14439v1#bib.bib29 "A generalized approach to portfolio optimization: improving performance by constraining portfolio norms")) developed a general framework that solves the global minimum variance problem (GMVP) by incorporating the A-norm constraint for
the portfolio weight vector. Fan et al. ([2013](https://arxiv.org/html/2602.14439v1#bib.bib56 "Large covariance estimation by thresholding principal orthogonal complements")) proposed a latent factor–based covariance estimation method, and the underlying idea of employing factor models to alleviate the curse of dimensionality has been extensively adopted in portfolio allocation research. Ding et al. ([2021](https://arxiv.org/html/2602.14439v1#bib.bib54 "High dimensional minimum variance portfolio estimation under statistical factor models")) developed a unified GMVP under statistical factor models in high-dimensional situations, Fan et al. ([2024b](https://arxiv.org/html/2602.14439v1#bib.bib129 "Time-varying minimum variance portfolio")) proposed a time-varying minimum variance portfolio by letting time-varying factor loading, and Wu et al. ([2025](https://arxiv.org/html/2602.14439v1#bib.bib13 "Making distributionally robust portfolios feasible in high dimension")) extend the famous distributionally-robust mean-variance portfolio of Blanchet et al. ([2022](https://arxiv.org/html/2602.14439v1#bib.bib140 "Distributionally robust mean-variance portfolio selection with Wasserstein distances")) into high dimensional situation based on factor structure.
Ao et al. ([2019](https://arxiv.org/html/2602.14439v1#bib.bib55 "Approaching mean-variance efficiency for large portfolios")) studied the mean–variance optimization with an ℓ1\ell\_{1}-norm regularization by reformulating it as a regression problem in high dimensional situation, and this approach has been further generalized to accommodate high-dimensional settings where dimension is larger than sample size (Li et al., [2022a](https://arxiv.org/html/2602.14439v1#bib.bib143 "A synthetic regression model for large portfolio allocation"); Chen et al., [2025](https://arxiv.org/html/2602.14439v1#bib.bib9 "Cross-sectional learning and inference for the stochastic discount factor")), as well as heteroskedastic and heavy-tailed data (Ao et al., [2025](https://arxiv.org/html/2602.14439v1#bib.bib27 "Robust large portfolio optimization with heteroscedastic and heavy-tailed returns")). Meng et al. ([2025](https://arxiv.org/html/2602.14439v1#bib.bib170 "Estimation of out-of-sample sharpe ratio for high dimensional portfolio optimization")) proposed to correct the
sample covariance matrix by adding a regularization within the framework of mean-variance problem, in high dimensional setup, and provided a consistent estimator of
OOS SR of the regularized portfolio. All the aforementioned studies focus solely on the mean-variance problem and do not incorporate additional information such as ESG scores for non-financial objectives.

This paper is organized as follows:
Section [2](https://arxiv.org/html/2602.14439v1#S2 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio") introduces the regularized ESG-constrained mean-variance portfolio. Section [3](https://arxiv.org/html/2602.14439v1#S3 "3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") develops the asymptotic results for the OOS SR of the regularized portfolio, proposes OOS SR estimator and establishes its asymptotic properties. Section [4](https://arxiv.org/html/2602.14439v1#S4 "4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio") presents simulation studies. Section [5](https://arxiv.org/html/2602.14439v1#S5 "5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio") proposes adaptive regularized ESG-constrained mean-variance portfolio, and conducts empirical analysis based on the components of the S&P 500 index. Section [6](https://arxiv.org/html/2602.14439v1#S6 "6 Conclusion ‣ Sustainable Investment: ESG Impacts on Large Portfolio") concludes the paper.

In this paper, ‖𝑨‖\|{\bm{A}}\|, ‖𝑨‖1\|{\bm{A}}\|\_{1}, ‖𝑨‖F\|{\bm{A}}\|\_{F}, ‖𝑨‖∞\|{\bm{A}}\|\_{\infty} and ‖𝑨‖tr\|{\bm{A}}\|\_{\textup{tr}} denote the spectral norm, L1L\_{1} norm, Frobenius norm, max norm and trace norm of a matrix 𝑨{\bm{A}}, defined respectively by ‖𝑨‖=λmax1/2​(𝑨⊤​𝑨)\|{\bm{A}}\|=\lambda\_{\max}^{1/2}({\bm{A}}^{\top}{\bm{A}}), ‖𝑨‖1=maxj​∑i|𝑨i​j|\|{\bm{A}}\|\_{1}=\max\_{j}\sum\_{i}|{\bm{A}}\_{ij}|, ‖𝑨‖F=tr1/2​(𝑨⊤​𝑨)\|{\bm{A}}\|\_{F}=\text{tr}^{1/2}({\bm{A}}^{\top}{\bm{A}}), ‖𝑨‖∞=maxi​∑j|𝑨i​j|\|{\bm{A}}\|\_{\infty}=\max\_{i}\sum\_{j}|{\bm{A}}\_{ij}| and ‖𝑨‖tr=tr⁡[(𝑨⊤​𝑨)1/2]\|{\bm{A}}\|\_{\textup{tr}}=\operatorname{tr}[({\bm{A}}^{\top}{\bm{A}})^{1/2}],
λmax​(𝑨)\lambda\_{\max}({\bm{A}}) (λmin​(𝑨)\lambda\_{\min}({\bm{A}})) denotes the maximum (minimum) eigenvalues of a matrix 𝑨{\bm{A}} and tr​(𝑨)\text{tr}({\bm{A}}) is the trace of a matrix 𝑨{\bm{A}}. If 𝑨{\bm{A}} is a column vector, both ‖𝑨‖\|{\bm{A}}\| and ‖𝑨‖F\|{\bm{A}}\|\_{F} equal the Euclidean norm ‖𝑨‖2\|{\bm{A}}\|\_{2}, and ‖𝑨‖∞=maxi⁡|𝑨i|\|{\bm{A}}\|\_{\infty}=\max\_{i}|{\bm{A}}\_{i}|. aT≍bTa\_{T}\asymp b\_{T} means that for some constants c,C>0c,C>0, c<|aT|/|bT|<Cc<|a\_{T}|/|b\_{T}|<C for all TT.

## 2 Regularized ESG-Constrained Problem

Consider the following portfolio optimization problem, which regulates the portfolio’s ESG score to s¯{\bar{s}}:111Without loss of generality, we consider the equality constraint on the ESG level, rather than the inequality one.

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg⁡max𝒘​𝒘⊤​𝝁−γ2​𝒘⊤​𝚺​𝒘s.t.𝒘⊤​𝒔/𝒘⊤​𝟏=s¯,\displaystyle\underset{\bm{w}}{\arg\max}\;\bm{w}^{\top}{{\bm{\mu}}}-\frac{\gamma}{2}\bm{w}^{\top}{{\bm{\Sigma}}}\bm{w}\qquad\text{s.t.}\quad\bm{w}^{\top}{\bm{s}}/\bm{w}^{\top}\bm{1}={\bar{s}}, |  | (2.1) |

where 𝒘⊤​𝒔/𝒘⊤​𝟏=s¯\bm{w}^{\top}{\bm{s}}/\bm{w}^{\top}\bm{1}={\bar{s}} is
the sustainability requirement (hereafter, ESG level constraint) on standardized portfolio ESG score, and 𝒔=E​(𝒂t){\bm{s}}=\textbf{E}({\bm{a}}\_{t}) is the expected ESG score of considered assets, and 𝒂t{\bm{a}}\_{t} is the ESG score vector.222The sustainable variable, the ESG score, can be replaced by other variables (e.g., carbon emissions, sustainability) for impact investing purposes.
Define 𝒔~:=𝒔−𝟏​s¯{\tilde{{\bm{s}}}}:={\bm{s}}-\bm{1}{\bar{s}}, then the ESG level constraint can be rewritten as 𝒘⊤​𝒔~=0\bm{w}^{\top}{\tilde{{\bm{s}}}}=0. The constrained optimization problem ([2.1](https://arxiv.org/html/2602.14439v1#S2.E1 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) has the following optimal solution in closed-form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘∗=1γ​𝚺−1​(𝝁+ξ​𝒔~),{\bm{w}^{\ast}}=\frac{1}{\gamma}{{\bm{\Sigma}}}^{-1}\left({{\bm{\mu}}}+{\xi}{{\tilde{{\bm{s}}}}}\right), |  | (2.2) |

where ξ=−𝝁⊤​𝚺−1​𝒔~/𝒔~⊤​𝚺−1​𝒔~.\xi=-{{\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}}/{{\tilde{{\bm{s}}}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}}. A straightforward calculation shows that the OOS Sharpe ratio of the oracle portfolio 𝒘∗\bm{w}^{\ast} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | θm​a​x=𝝁⊤​𝚺−1​𝝁−(𝝁⊤​𝚺−1​𝒔~)2𝒔~⊤​𝚺−1​𝒔~.\displaystyle\theta\_{max}=\sqrt{{\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\bm{\mu}}-\frac{({\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}})^{2}}{{\tilde{{\bm{s}}}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}}}. |  | (2.3) |

From the oracle-population perspective, imposing the ESG constraint strictly reduces the Sharpe ratio of the optimal allocation unless 𝝁⊤​𝚺−1​𝒔~=0{\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}=0, given that 𝚺−1{\bm{\Sigma}}^{-1} is positive definite.
The oracle Sharpe ratio θmax\theta\_{\max} serves as a theoretical upper bound for estimated ESG-constrained portfolios.

In practical application, due to the lack of information of 𝝁{\bm{\mu}}, 𝚺{\bm{\Sigma}}, and 𝒔~{\tilde{{\bm{s}}}}, the practical optimization using sample estimations is considered as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg⁡max𝒘​𝒘⊤​𝝁^−γ2​𝒘⊤​𝚺^​𝒘s.t.𝒘⊤​𝒔~^=0,\displaystyle\underset{\bm{w}}{\arg\max}\;\bm{w}^{\top}{\widehat{{\bm{\mu}}}}-\frac{\gamma}{2}\bm{w}^{\top}{\widehat{\bm{\Sigma}}}\bm{w}\qquad\text{s.t.}\quad\bm{w}^{\top}\widehat{{\tilde{{\bm{s}}}}}=0, |  | (2.4) |

where 𝝁^,𝚺^{\widehat{{\bm{\mu}}}},{\widehat{\bm{\Sigma}}} and 𝒔~^\widehat{{\tilde{{\bm{s}}}}} are sample estimations calculated based on collected data.
By using the first-order arguments, the optimization ([2.4](https://arxiv.org/html/2602.14439v1#S2.E4 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) is equivalent to the following non-constrained problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg⁡max𝒘​𝒘⊤​(𝝁^+ξ^​𝒔~^)−γ2​𝒘⊤​𝚺^​𝒘,\displaystyle\underset{\bm{w}}{\arg\max}\;\bm{w}^{\top}\left({\widehat{{\bm{\mu}}}}+\widehat{\xi}\widehat{{\tilde{{\bm{s}}}}}\right)-\frac{\gamma}{2}\bm{w}^{\top}{\widehat{\bm{\Sigma}}}\bm{w}, |  | (2.5) |

where ξ^=−𝒔~^⊤​𝚺^−1​𝝁^/𝒔~^⊤​𝚺^−1​𝒔~^.\widehat{\xi}=-{\widehat{{\tilde{{\bm{s}}}}}^{\top}{\widehat{\bm{\Sigma}}}^{-1}{\widehat{{\bm{\mu}}}}}/{\widehat{{\tilde{{\bm{s}}}}}^{\top}{\widehat{\bm{\Sigma}}}^{-1}\widehat{{\tilde{{\bm{s}}}}}}.
From ([2.5](https://arxiv.org/html/2602.14439v1#S2.E5 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")), the ESG level constraint essentially penalizes the sample mean estimation, which is known to be unreliable in large dimensional settings (DeMiguel et al., [2009a](https://arxiv.org/html/2602.14439v1#bib.bib29 "A generalized approach to portfolio optimization: improving performance by constraining portfolio norms"); Ao et al., [2019](https://arxiv.org/html/2602.14439v1#bib.bib55 "Approaching mean-variance efficiency for large portfolios"); Bodnar et al., [2019](https://arxiv.org/html/2602.14439v1#bib.bib3 "Optimal shrinkage estimator for high-dimensional mean vector")). Therefore, 𝒔~^\widehat{{\tilde{{\bm{s}}}}} serves as a penalization term on the sample mean estimation.
Furthermore, it is also well known that the empirical covariance estimator performs poorly in large dimensional situations, particularly in the filed of portfolio allocation (Michaud, [1989](https://arxiv.org/html/2602.14439v1#bib.bib34 "The Markowitz optimization enigma: is ‘optimized’optimal?"); Jagannathan and Ma, [2003](https://arxiv.org/html/2602.14439v1#bib.bib1 "Risk reduction in large portfolios: why imposing the wrong constraints helps"); Kan and Zhou, [2007](https://arxiv.org/html/2602.14439v1#bib.bib161 "Optimal portfolio choice with parameter uncertainty"); Bodnar et al., [2022b](https://arxiv.org/html/2602.14439v1#bib.bib48 "Optimal shrinkage-based portfolio selection in high dimensions"); Lassance et al., [2024](https://arxiv.org/html/2602.14439v1#bib.bib40 "The risk of expected utility under parameter uncertainty")). As such,
in order to mitigate the bad condition number of the sample covariance estimation, particularly when dimension is larger than sample size, similar to formulation of the sample mean part, we consider adding an regularization matrix term 𝑸{\bm{Q}} on the sample covariance (Ledoit and Wolf, [2003](https://arxiv.org/html/2602.14439v1#bib.bib81 "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection"); DeMiguel et al., [2009a](https://arxiv.org/html/2602.14439v1#bib.bib29 "A generalized approach to portfolio optimization: improving performance by constraining portfolio norms"); Makridis and Simaan, [2023](https://arxiv.org/html/2602.14439v1#bib.bib166 "Balancing returns and responsibility: evidence from shrinkage-based portfolios"); Meng et al., [2025](https://arxiv.org/html/2602.14439v1#bib.bib170 "Estimation of out-of-sample sharpe ratio for high dimensional portfolio optimization")), and thus consider the following problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg⁡max𝒘​𝒘⊤​𝝁^−γ2​𝒘⊤​(𝚺^+η​𝑸)​𝒘,𝒘⊤​𝒔~^=0,\displaystyle\underset{\bm{w}}{\arg\max}\;\bm{w}^{\top}{\widehat{{\bm{\mu}}}}-\frac{\gamma}{2}\bm{w}^{\top}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)\bm{w},\quad\bm{w}^{\top}\widehat{{\tilde{{\bm{s}}}}}=0, |  | (2.6) |

where 𝑸{\bm{Q}} is a positive definite deterministic square matrix that determines the direction of regularization, and the coefficient η\eta controls the degree of penalization.
Similarly, the optimization problem ([2.6](https://arxiv.org/html/2602.14439v1#S2.E6 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) has a closed-form optimal solution as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘∗^=1γ​(𝚺^+η​𝑸)−1​(𝝁^+ζ^​𝒔~^),\widehat{{\bm{w}}^{\ast}}=\frac{1}{\gamma}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)^{-1}\left({\widehat{{\bm{\mu}}}}+\widehat{\zeta}\widehat{{\tilde{{\bm{s}}}}}\right), |  | (2.7) |

where ζ^​(η)=−𝒔~^⊤​(𝚺^+η​𝑸)−1​𝝁^/𝒔~^⊤​(𝚺^+η​𝑸)−1​𝒔~^\widehat{\zeta}(\eta)=-{\widehat{{\tilde{{\bm{s}}}}}^{\top}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{\widehat{{\bm{\mu}}}}}/{\widehat{{\tilde{{\bm{s}}}}}^{\top}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}\widehat{{\tilde{{\bm{s}}}}}}. It is worth noting that although adding a well-behaved regularization term to address poor conditioning is common in high-dimensional statistical inference, applying such a regularization to portfolio optimization also carries a meaningful economic interpretation in the context of ESG-based portfolio allocation.

###### Remark 1.

By simple calculation shown in our online Appendix A, the optimal solution of problem ([2.6](https://arxiv.org/html/2602.14439v1#S2.E6 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) is equivalent to the solution to following optimization

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝒘​𝒘⊤​𝝁^−γ2​𝒘⊤​𝚺^​𝒘s.t.𝒘⊤​𝒔~^=0,𝒘⊤​𝑸​𝒘=δ​(η),\displaystyle\underset{\bm{w}}{\max}\;\bm{w}^{\top}{\widehat{{\bm{\mu}}}}-\frac{\gamma}{2}\bm{w}^{\top}{\widehat{\bm{\Sigma}}}\bm{w}\qquad\text{s.t.}\quad\bm{w}^{\top}\widehat{{\tilde{{\bm{s}}}}}=0,\;\;\bm{w}^{\top}{\bm{Q}}\bm{w}=\delta(\eta), |  | (2.8) |

where δ​(η)=(𝛍^+ζ^​(η)​𝐬~^)⊤​(𝚺^+η​𝐐)−1​𝐐​(𝚺^+η​𝐐)−1​(𝛍^+ζ^​(η)​𝐬~^)/γ2\delta(\eta)=\left({\widehat{{\bm{\mu}}}}+\widehat{\zeta}(\eta)\widehat{{\tilde{{\bm{s}}}}}\right)^{\top}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)^{-1}{\bm{Q}}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)^{-1}\left({\widehat{{\bm{\mu}}}}+\widehat{\zeta}(\eta)\widehat{{\tilde{{\bm{s}}}}}\right)/\gamma^{2}. Adding a regularization matrix to the sample covariance matrix is equivalent to imposing an additional constraint that the A-norm of the portfolio weight equals a threshold δ​(η)\delta(\eta) (DeMiguel et al., [2009a](https://arxiv.org/html/2602.14439v1#bib.bib29 "A generalized approach to portfolio optimization: improving performance by constraining portfolio norms")). In particular, if 𝐐=𝛀{\bm{Q}}=\bm{\Omega} where 𝛀\bm{\Omega} is the covariance matrix of assets’ ESG scores, the quadratic constraint 𝐰⊤​𝛀​𝐰=δ​(η)\bm{w}^{\top}\bm{\Omega}\bm{w}=\delta(\eta) requires that the variance of portfolio ESG scores is restricted to the target level δ\delta.
Therefore, the optimization problem ([2.6](https://arxiv.org/html/2602.14439v1#S2.E6 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) maximizes the investor’s utility subject to two sustainability constraints on the portfolio’s ESG average level and variance. Clearly, an appropriate specification of
𝐐{\bm{Q}} can provide valuable guidance for the design and quantification of ESG scores, enabling investors to achieve superior performance while maintaining sustainability requirements. Furthermore, when 𝐐=𝐈p{\bm{Q}}=\bm{I}\_{p}, there is a one-to-one correspondence between the A-norm-constrained portfolios and unconstrained portfolios computed based on the linear shrinkage covariance matrix (Ledoit and Wolf, [2004](https://arxiv.org/html/2602.14439v1#bib.bib46 "A well-conditioned estimator for large-dimensional covariance matrices")).

###### Remark 2.

The studies of Hu et al. ([2025](https://arxiv.org/html/2602.14439v1#bib.bib4 "Sustainability-valued discrete option pricing in complete markets")) and Lauria et al. ([2025](https://arxiv.org/html/2602.14439v1#bib.bib12 "Environmental, social and governance-valued portfolio optimization and dynamic asset pricing")) integrate the ESG information into decision-making by using the ESG-valued return 𝐫te​s​g\bm{r}\_{t}^{esg}, which is defined as 𝐫te​s​g=(1−ι)​𝐫t+ι​𝐚~t\bm{r}\_{t}^{esg}=(1-\iota)\bm{r}\_{t}+\iota\tilde{{\bm{a}}}\_{t} where 𝐚~t\tilde{{\bm{a}}}\_{t} is the scaled ESG score and ι∈(0,1)\iota\in(0,1) is the intensity of ESG preference. Note that E​(𝐫te​s​g)=(1−ι)​(𝛍+ι1−ι​E​(𝐚~t))\textbf{E}(\bm{r}\_{t}^{esg})=(1-\iota)\left({\bm{\mu}}+\frac{\iota}{1-\iota}\textbf{E}(\tilde{{\bm{a}}}\_{t})\right) and Cov⁡(𝐫te​s​g)=(1−ι)2​(𝚺+ι2(1−ι)2​𝛀~)\operatorname{Cov}(\bm{r}\_{t}^{esg})=(1-\iota)^{2}\left({\bm{\Sigma}}+\frac{\iota^{2}}{(1-\iota)^{2}}\tilde{\bm{\Omega}}\right) if 𝐚~t\tilde{{\bm{a}}}\_{t} and 𝐫t\bm{r}\_{t} are uncorrelated, and 𝛀~\tilde{\bm{\Omega}} is the covariance matrix of 𝐚~t\tilde{{\bm{a}}}\_{t}. As a result, when the ESG-valued return is applied to mean-variance problem ([1.1](https://arxiv.org/html/2602.14439v1#S1.E1 "In 1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) with 𝐚~t=𝐚t−𝟏​s¯\tilde{{\bm{a}}}\_{t}={\bm{a}}\_{t}-\bm{1}{\bar{s}} and risk aversion parameter γ=γ1/(1−ι)\gamma=\gamma\_{1}/(1-\iota), it is equivalent to solving the population version of the regularized problem ([2.6](https://arxiv.org/html/2602.14439v1#S2.E6 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) with γ=γ1\gamma=\gamma\_{1}, 𝐐=𝛀{\bm{Q}}=\bm{\Omega}, and η=ζ​(η)2=(ι/(1−ι))2\eta=\zeta(\eta)^{2}=(\iota/(1-\iota))^{2}.

###### Remark 3.

When 𝐐{\bm{Q}} is a diagonal matrix with positive diagonal entries, the term 𝐰⊤​(η​γ2​𝐐)​𝐰\bm{w}^{\top}\left(\frac{\eta\gamma}{2}{\bm{Q}}\right)\bm{w} can be interpreted as explicitly accounting for transaction costs; see, e.g., Hautsch and Voigt ([2019](https://arxiv.org/html/2602.14439v1#bib.bib6 "Large-scale portfolio allocation under transaction costs and model uncertainty")) and Fan et al. ([2024a](https://arxiv.org/html/2602.14439v1#bib.bib5 "Cost-aware portfolios in a large universe of assets")). As a result, with an appropriately selected penalization matrix 𝐐{\bm{Q}}, our model promotes more stable allocations.

Based on optimal solution ([2.7](https://arxiv.org/html/2602.14439v1#S2.E7 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")), the OOS SR of estimated regularized ESG-constrained mean-variance can be further defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ∗​(η,𝑸):=(𝝁^+ζ^​𝒔~^)⊤​(𝚺^+η​𝑸)−1​𝝁(𝝁^+ζ^​𝒔~^)⊤​(𝚺^+η​𝑸)−1​𝚺​(𝚺^+η​𝑸)−1​(𝝁^+ζ^​𝒔~^).\theta^{\ast}(\eta,{\bm{Q}}):=\frac{\left({\widehat{{\bm{\mu}}}}+\widehat{\zeta}\widehat{{\tilde{{\bm{s}}}}}\right)^{\top}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{\bm{\mu}}}{\sqrt{\left({\widehat{{\bm{\mu}}}}+\widehat{\zeta}\widehat{{\tilde{{\bm{s}}}}}\right)^{\top}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{\bm{\Sigma}}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}\left({\widehat{{\bm{\mu}}}}+\widehat{\zeta}\widehat{{\tilde{{\bm{s}}}}}\right)}}. |  | (2.9) |

From ([2.9](https://arxiv.org/html/2602.14439v1#S2.E9 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")), it is evident that θ∗​(η,𝑸)\theta^{\ast}(\eta,{\bm{Q}}) depends on the choice of 𝑸{\bm{Q}} and η\eta, and in what follows we drop (η,𝑸)(\eta,{\bm{Q}}) whenever this dependence is clear from the context. In the next section, we study the asymptotic properties of the OOS SR of the estimated ESG-constrained portfolio, which provides insight into how the ESG constraint affects portfolio performance in large-dimensional settings.

## 3 Asymptotic Analysis

In this section, we conduct an asymptotic analysis of the out-of-sample (OOS) Sharpe ratio (SR) for ESG-constrained portfolios. Before deriving the asymptotic behavior of θ∗​(η,𝑸){\theta}^{\ast}(\eta,{\bm{Q}}), we first introduce some required assumptions.

###### Assumption 1.

We consider an asymptotic setup where T,p→∞T,p\rightarrow\infty, and p/T→c∈(0,1)∪(1,∞)p/T\rightarrow c\in(0,1)\cup(1,\infty).

Assumption [1](https://arxiv.org/html/2602.14439v1#Thmassumption1 "Assumption 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") is quite standard in the literature of random matrix theory. We exclude the knife-edge case c=1c=1 because the sample eigenvalue density diverges near zero in this regime, leading to additional technical complications (Ledoit and Péché, [2011](https://arxiv.org/html/2602.14439v1#bib.bib175 "Eigenvectors of some large sample covariance matrix ensembles"); Ledoit and Wolf, [2017](https://arxiv.org/html/2602.14439v1#bib.bib65 "Nonlinear shrinkage of the covariance matrix for portfolio selection: Markowitz meets Goldilocks"); Lu et al., [2024](https://arxiv.org/html/2602.14439v1#bib.bib8 "Double descent in portfolio optimization: dance between theoretical sharpe ratio and estimation accuracy")).

###### Assumption 2.

The excess returns vector at time tt is generated as 𝐫t=𝛍+𝚺12​𝐳t\bm{r}\_{t}={\bm{\mu}}+{\bm{\Sigma}}^{\frac{1}{2}}{\bm{z}}\_{t}, where 𝐳t∼i.i.d.𝒩​(𝟎,𝐈p){\bm{z}}\_{t}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}\mathcal{N}\left(\bm{0},\bm{I}\_{p}\right).

Gaussianity assumption for return data is common and standard in random-matrix-based portfolio theory; see, for example, El Karoui ([2010](https://arxiv.org/html/2602.14439v1#bib.bib100 "High-dimensionality effects in the markowitz problem and other quadratic programs with linear constraints: risk underestimation")), Bodnar et al. ([2022a](https://arxiv.org/html/2602.14439v1#bib.bib2 "Recent advances in shrinkage-based high-dimensional inference")), Li et al. ([2022b](https://arxiv.org/html/2602.14439v1#bib.bib179 "Spectrally-corrected estimation for high-dimensional markowitz mean-variance optimization")) and Bodnar et al. ([2024](https://arxiv.org/html/2602.14439v1#bib.bib180 "Two is better than one: regularized shrinkage of large minimum variance portfolios")).
Stacking the TT observations yields the asset return matrix 𝑹=𝟏T​𝝁⊤+𝑿{\bm{R}}=\bm{1}\_{T}{\bm{\mu}}^{\top}+\bm{X}, where 𝟏T\bm{1}\_{T} is a TT-dimensional column vector of ones and 𝑿=𝒁​𝚺12\bm{X}=\bm{Z}{\bm{\Sigma}}^{\frac{1}{2}}, with 𝒁=[𝒛1⊤,…,𝒛T⊤]⊤∈ℝT×p\bm{Z}=[\,{\bm{z}}\_{1}^{\top},\ldots,{\bm{z}}\_{T}^{\top}\,]^{\top}\in\mathbb{R}^{T\times p}. Under this representation, the sample covariance matrix is 𝚺^:=𝑿⊤​𝑿/T{\widehat{\bm{\Sigma}}}:=\bm{X}^{\top}\bm{X}/T.

###### Assumption 3.

The matrix 𝚺{\bm{\Sigma}} is well scaled as ∥𝚺/p∥tr≤C\lVert{\bm{\Sigma}}/p\rVert\_{\textup{tr}}\leq C for some constant C>0C>0. Denote the eigenvalues of 𝚺{\bm{\Sigma}} as λ1≥⋯≥λp\lambda\_{1}\geq\cdots\geq\lambda\_{p}, one of the following conditions hold:
  
1. When p<Tp<T, we allow arbitrary number of diverging eigenvalues.
  
2. When p>Tp>T, we allow at most a fixed number KK of diverging eigenvalues, and λ1≤C​λK2\lambda\_{1}\leq C\lambda\_{K}^{2} for some constant C>0C>0.

Both cases accommodate factor-type covariance structures with spiked eigenvalues that may diverge as pp grows. The distinction between Cases 1 and 2 is mainly technical and depends on the dimensionality regime.

###### Assumption 4.

The positive definite regularization matrix 𝐐∈𝒬{\bm{Q}}\in\mathcal{Q}, independent of 𝐗\bm{X}, satisfies the following: there exist constants c1≥c\_{1}\geq, c2>0c\_{2}>0, with c12+c22>0c\_{1}^{2}+c\_{2}^{2}>0, and 𝐐1{\bm{Q}}\_{1} and 𝐐2{\bm{Q}}\_{2} such that 𝐐=c1​𝐐1+c2​𝐐2{\bm{Q}}=c\_{1}{\bm{Q}}\_{1}+c\_{2}{\bm{Q}}\_{2}. The matrices 𝐐1{\bm{Q}}\_{1} and 𝐐2{\bm{Q}}\_{2} satisfies c′​𝐈⪯𝐐1⪯C′​𝐈c^{\prime}\bm{I}\preceq{\bm{Q}}\_{1}\preceq C^{\prime}\bm{I} and c′​𝐈⪯𝚺−1/2​𝐐2​𝚺−1/2⪯C′​𝐈c^{\prime}\bm{I}\preceq{\bm{\Sigma}}^{-1/2}{\bm{Q}}\_{2}{\bm{\Sigma}}^{-1/2}\preceq C^{\prime}\bm{I} for some constant c′,C′>0c^{\prime},C^{\prime}>0.

Assumption [4](https://arxiv.org/html/2602.14439v1#Thmassumption4 "Assumption 4. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") rules out ill-conditioned choices of the regularization matrix 𝑸{\bm{Q}}.

###### Assumption 5.

The ESG score vector 𝐚t{\bm{a}}\_{t} corresponding to the pp assets at time tt is generated as 𝐚t=𝐬+𝛀12​𝐲t{\bm{a}}\_{t}={\bm{s}}+\bm{\Omega}^{\frac{1}{2}}{\bm{y}}\_{t}, where 𝐲t∼i.i.d.𝒩​(𝟎,𝐈p){\bm{y}}\_{t}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}\mathcal{N}\left(\bm{0},\bm{I}\_{p}\right). The 𝛀\bm{\Omega} has uniformly bounded spectral norm; that is, λmax​(𝛀)≤C\lambda\_{\max}(\bm{\Omega})\leq C for some constant C>0C>0. In addition, 𝐬⊤​𝚺−1​𝐬,𝐬⊤​𝚺−1​𝟏,𝟏⊤​𝚺−1​𝟏{\bm{s}}^{\top}{\bm{\Sigma}}^{-1}{\bm{s}},{\bm{s}}^{\top}{\bm{\Sigma}}^{-1}\bm{1},\bm{1}^{\top}{\bm{\Sigma}}^{-1}\bm{1} are bounded, and 𝐚t{\bm{a}}\_{t} is assumed to be independent of the return 𝐫t\bm{r}\_{t}.

Assumption [5](https://arxiv.org/html/2602.14439v1#Thmassumption5 "Assumption 5. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") postulates that the asset-level ESG score vector 𝒂t{\bm{a}}\_{t} follows a multivariate normal distribution, which serves as a technical requirement for the random matrix theory framework.
When the covariance matrix 𝛀\bm{\Omega} is close to the zero matrix, 𝒂t{\bm{a}}\_{t} can be treated as approximately time-invariant. The condition that 𝟏⊤​𝚺−1​𝟏\bm{1}^{\top}{\bm{\Sigma}}^{-1}\bm{1} is bounded holds when the minimum risk is non-diversifiable; see Example 2.2 of Ding et al. ([2021](https://arxiv.org/html/2602.14439v1#bib.bib54 "High dimensional minimum variance portfolio estimation under statistical factor models")). The boundedness of 𝒔⊤​𝚺−1​𝒔{\bm{s}}^{\top}{\bm{\Sigma}}^{-1}{\bm{s}} and 𝒔⊤​𝚺−1​𝟏{\bm{s}}^{\top}{\bm{\Sigma}}^{-1}\bm{1} is mild, given that ESG scores are measured on arbitrary, provider-specific scales and can be standardized prior to evaluation. Based on Assumption [5](https://arxiv.org/html/2602.14439v1#Thmassumption5 "Assumption 5. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio"), the sample mean of ESG score is 𝒔^:=1T​∑t=1T𝒂t\widehat{{\bm{s}}}:=\frac{1}{T}\sum\_{t=1}^{T}{\bm{a}}\_{t},
and the centered ESG exposure is 𝒔~^=𝒔^−𝟏​s¯\widehat{{\tilde{{\bm{s}}}}}=\widehat{{\bm{s}}}-\bm{1}\,{\bar{s}}. For technical conciseness, the ESG scores and returns are assumed to be independent. We also conduct statistical analysis on the real datasets and find that, the ESG scores and returns indeed have weak correlations.

The following quantities will be used repeatedly in subsequent analysis. For notational convenience, we first define
𝔾:=(𝚺1+s0+η​𝑸)−1\mathbb{G}:=\left(\frac{{\bm{\Sigma}}}{1+s\_{0}}+\eta{\bm{Q}}\right)^{-1}and ℍ:=(𝚺1+s0+η​𝑸)−1​𝚺​(𝚺1+s0+η​𝑸)−1,\mathbb{H}:=\left(\frac{{\bm{\Sigma}}}{1+s\_{0}}+\eta{\bm{Q}}\right)^{-1}{\bm{\Sigma}}\left(\frac{{\bm{\Sigma}}}{1+s\_{0}}+\eta{\bm{Q}}\right)^{-1},
where s0s\_{0} is defined as the unique solution to
s0=cp​tr⁡[𝚺​(𝚺1+s0+η​𝑸)−1],s\_{0}=\frac{c}{p}\operatorname{tr}\left[{\bm{\Sigma}}\left(\frac{{\bm{\Sigma}}}{1+s\_{0}}+\eta{\bm{Q}}\right)^{-1}\right],
and s1,𝚺s\_{1,{\bm{\Sigma}}} is given by
s1,𝚺=(s1,𝚺(1+s0)2−1)​cp​tr⁡[𝚺​(𝚺1+s0+η​𝑸)−1​𝚺​(𝚺1+s0+η​𝑸)−1].s\_{1,{\bm{\Sigma}}}=\left(\frac{s\_{1,{\bm{\Sigma}}}}{(1+s\_{0})^{2}}-1\right)\frac{c}{p}\operatorname{tr}\left[{\bm{\Sigma}}\left(\frac{{\bm{\Sigma}}}{1+s\_{0}}+\eta{\bm{Q}}\right)^{-1}{\bm{\Sigma}}\left(\frac{{\bm{\Sigma}}}{1+s\_{0}}+\eta{\bm{Q}}\right)^{-1}\right].
Under these conditions, the following lemma characterizes the limit of OOS Sharpe ratio θ∗\theta^{\ast} of proposed ESG-constrained portfolio.

###### Lemma 1.

Suppose Assumptions [1](https://arxiv.org/html/2602.14439v1#Thmassumption1 "Assumption 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio")-[5](https://arxiv.org/html/2602.14439v1#Thmassumption5 "Assumption 5. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") hold true, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ∗−𝝁⊤​𝔾​𝝁−(𝝁⊤​𝔾​𝒔~)2𝒔~⊤​𝔾​𝒔~+T−1​tr⁡[𝔾​𝛀]1−s1,𝚺(1+s0)2​𝝁⊤​ℍ​𝝁+T−1​tr⁡[ℍ​𝚺]+(𝝁⊤​𝔾​𝒔~)2​(𝒔~⊤​ℍ​𝒔~+T−1​tr⁡[ℍ​𝛀])(𝒔~⊤​𝔾​𝒔~+T−1​tr⁡[𝔾​𝛀])2−2​𝝁⊤​𝔾​𝒔~​𝝁⊤​ℍ​𝒔~𝒔~⊤​𝔾​𝒔~+T−1​tr⁡[𝔾​𝛀]​⟶a.s​0.\displaystyle{\theta}^{\*}-\frac{{\bm{\mu}}^{\top}\mathbb{G}{\bm{\mu}}-\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}+T^{-1}\operatorname{tr}\left[\mathbb{G}\bm{\Omega}\right]}}{{\sqrt{1-\frac{s\_{1,{\bm{\Sigma}}}}{(1+s\_{0})^{2}}}}\sqrt{{\bm{\mu}}^{\top}\mathbb{H}{\bm{\mu}}+T^{-1}\operatorname{tr}\left[\mathbb{H}{\bm{\Sigma}}\right]+\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}\left({\tilde{{\bm{s}}}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}+T^{-1}\operatorname{tr}\left[\mathbb{H}\bm{\Omega}\right]\right)}{\left({\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}+T^{-1}\operatorname{tr}\left[\mathbb{G}\bm{\Omega}\right]\right)^{2}}-2\frac{{\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}{\bm{\mu}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}+T^{-1}\operatorname{tr}\left[\mathbb{G}\bm{\Omega}\right]}}}\overset{a.s}{\longrightarrow}0. |  | (3.1) |

Lemma [1](https://arxiv.org/html/2602.14439v1#Thmlemma1 "Lemma 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") shows the limit of OOS SR of the newly proposed regularized ESG-constrained mean-variance portfolio ([2.7](https://arxiv.org/html/2602.14439v1#S2.E7 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")). The limit of θ∗\theta^{\ast} is complicated. Thus, in order to better analyze the asymptotic behavior of OOS SR, we further introduce the following mixed-information regularized optimization problem which relies on population ESG information 𝒔~{\tilde{{\bm{s}}}}, while using the sample mean and sample covariance matrix of assets return:

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg⁡max𝒘​𝒘⊤​𝝁^−γ2​𝒘⊤​(𝚺^+η​𝑸)​𝒘,𝒘⊤​𝒔~=0.\displaystyle\underset{\bm{w}}{\arg\max}\;\bm{w}^{\top}{\widehat{{\bm{\mu}}}}-\frac{\gamma}{2}\bm{w}^{\top}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)\bm{w},\quad\bm{w}^{\top}{{\tilde{{\bm{s}}}}}=0. |  | (3.2) |

The solution to ([3.2](https://arxiv.org/html/2602.14439v1#S3.E2 "In 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) is given by 𝒘ˇ=(𝚺^+η​𝑸)−1​(𝝁^+ζ~​𝒔~)/γ\check{\bm{w}}=\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)^{-1}\left({\widehat{{\bm{\mu}}}}+\tilde{\zeta}{{\tilde{{\bm{s}}}}}\right)/\gamma, where ζˇ\check{\zeta} is defined as ζˇ=−𝒔~⊤​(𝚺^+η​𝑸)−1​𝝁^/𝒔~⊤​(𝚺^+η​𝑸)−1​𝒔~\check{\zeta}=-{{{\tilde{{\bm{s}}}}}^{\top}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{\widehat{{\bm{\mu}}}}}/{{{\tilde{{\bm{s}}}}}^{\top}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{{\tilde{{\bm{s}}}}}}, and thus the corresponding OOS SR of 𝒘ˇ\check{\bm{w}} is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θˇ∗​(η,𝑸):=(𝝁^+ζˇ​𝒔~)⊤​(𝚺^+η​𝑸)−1​𝝁(𝝁^+ζˇ​𝒔~)⊤​(𝚺^+η​𝑸)−1​𝚺​(𝚺^+η​𝑸)−1​(𝝁^+ζˇ​𝒔~).\check{\theta}^{\ast}(\eta,{\bm{Q}}):=\frac{\left({\widehat{{\bm{\mu}}}}+\check{\zeta}{{\tilde{{\bm{s}}}}}\right)^{\top}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{\bm{\mu}}}{\sqrt{\left({\widehat{{\bm{\mu}}}}+\check{\zeta}{{\tilde{{\bm{s}}}}}\right)^{\top}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{\bm{\Sigma}}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}\left({\widehat{{\bm{\mu}}}}+\check{\zeta}{{\tilde{{\bm{s}}}}}\right)}}. |  | (3.3) |

###### Lemma 2.

Suppose Assumptions [1](https://arxiv.org/html/2602.14439v1#Thmassumption1 "Assumption 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio")-[5](https://arxiv.org/html/2602.14439v1#Thmassumption5 "Assumption 5. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") hold true, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | θˇ∗−𝝁⊤​𝔾​𝝁−(𝝁⊤​𝔾​𝒔~)2𝒔~⊤​𝔾​𝒔~1−s1,𝚺(1+s0)2​𝝁⊤​ℍ​𝝁+T−1​tr⁡[ℍ​𝚺]+(𝝁⊤​𝔾​𝒔~)2​𝒔~⊤​ℍ​𝒔~(𝒔~⊤​𝔾​𝒔~)2−2​𝝁⊤​𝔾​𝒔~​𝝁⊤​ℍ​𝒔~𝒔~⊤​𝔾​𝒔~​⟶a.s​0.\displaystyle\check{\theta}^{\ast}-\frac{{\bm{\mu}}^{\top}\mathbb{G}{\bm{\mu}}-\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}}}{{\sqrt{1-\frac{s\_{1,{\bm{\Sigma}}}}{(1+s\_{0})^{2}}}}\sqrt{{\bm{\mu}}^{\top}\mathbb{H}{\bm{\mu}}+T^{-1}\operatorname{tr}\left[\mathbb{H}{\bm{\Sigma}}\right]+\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}{\tilde{{\bm{s}}}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}}{\left({\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}}-2\frac{{\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}{\bm{\mu}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}}}}\overset{a.s}{\longrightarrow}0. |  | (3.4) |

Lemma [2](https://arxiv.org/html/2602.14439v1#Thmlemma2 "Lemma 2. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") presents the asymptotic result of θˇ∗\check{\theta}^{\ast}. Compare the limits in Lemmas [1](https://arxiv.org/html/2602.14439v1#Thmlemma1 "Lemma 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") and [2](https://arxiv.org/html/2602.14439v1#Thmlemma2 "Lemma 2. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
the impacts of estimation error from estimating ESG scores mean level in high dimensional situation can be quantified. Specifically, it is evident that, the estimation error of sample mean of ESG scores introduces an additional term tr⁡[𝔾​𝛀]/T\operatorname{tr}\left[\mathbb{G}\bm{\Omega}\right]/T (or tr⁡[ℍ​𝛀]/T\operatorname{tr}\left[\mathbb{H}\bm{\Omega}\right]/T) to the term 𝒔~⊤​𝔾​𝒔~{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}} (or 𝒔~⊤​ℍ​𝒔~{\tilde{{\bm{s}}}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}), and thus affect the financial performance of estimated portfolio. Clearly, when assets’ ESG scores are stable enough so that 𝛀\bm{\Omega} is close to zero matrix 𝟎p×p\bm{0}\_{p\times p}, the limit in ([3.1](https://arxiv.org/html/2602.14439v1#S3.E1 "In Lemma 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) degenerates to that in ([3.4](https://arxiv.org/html/2602.14439v1#S3.E4 "In Lemma 2. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio")).

###### Remark 4.

Let 𝐰~\tilde{\bm{w}} denote the solution of max𝐰​𝐰⊤​𝛍−γ2​𝐰⊤​(𝚺^+η​𝐐)​𝐰\underset{\bm{w}}{\max}\;\bm{w}^{\top}{\bm{\mu}}-\frac{\gamma}{2}\bm{w}^{\top}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)\bm{w} subject to 𝐰⊤​𝐬~=0\bm{w}^{\top}{{\tilde{{\bm{s}}}}}=0. For this optimization problem, only sample covariance matrix is applied, and population mean of return and ESG scores are considered as known.
By using the similar arguments of Lemma [2](https://arxiv.org/html/2602.14439v1#Thmlemma2 "Lemma 2. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio"), the OOS SR of 𝐰~\tilde{\bm{w}} (denoted as θ~∗\tilde{\theta}^{\ast}) has a limit of

|  |  |  |
| --- | --- | --- |
|  | limT→∞𝝁⊤​𝔾​𝝁−(𝝁⊤​𝔾​𝒔~)2𝒔~⊤​𝔾​𝒔~1−s1,𝚺(1+s0)2​𝝁⊤​ℍ​𝝁+(𝝁⊤​𝔾​𝒔~)2​𝒔~⊤​ℍ​𝒔~(𝒔~⊤​𝔾​𝒔~)2−2​𝝁⊤​𝔾​𝒔~​𝝁⊤​ℍ​𝒔~𝒔~⊤​𝔾​𝒔~.\lim\_{T\rightarrow\infty}\frac{{\bm{\mu}}^{\top}\mathbb{G}{\bm{\mu}}-\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}}}{{\sqrt{1-\frac{s\_{1,{\bm{\Sigma}}}}{(1+s\_{0})^{2}}}}\sqrt{{\bm{\mu}}^{\top}\mathbb{H}{\bm{\mu}}+\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}{\tilde{{\bm{s}}}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}}{\left({\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}}-2\frac{{\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}{\bm{\mu}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}}}}. |  |

A similar result for unconstrained mean-variance portfolio can be referred to Meng et al. ([2025](https://arxiv.org/html/2602.14439v1#bib.bib170 "Estimation of out-of-sample sharpe ratio for high dimensional portfolio optimization")). As such, Lemma [2](https://arxiv.org/html/2602.14439v1#Thmlemma2 "Lemma 2. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") also quantifies the impact of the estimation error of the sample mean in high-dimensional situations, i.e., introducing an additional term tr⁡[ℍ​𝚺]/T\operatorname{tr}\left[\mathbb{H}{\bm{\Sigma}}\right]/T. It is worth noting that, under the conditions of Lemma [2](https://arxiv.org/html/2602.14439v1#Thmlemma2 "Lemma 2. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio"), if 𝐐=C​𝚺{\bm{Q}}=C{\bm{\Sigma}} with a sufficiently large constant CC, the θ~∗\tilde{\theta}^{\ast} converges to the theoretical maximum Sharpe ratio θmax\theta\_{\max} defined in ([2.3](https://arxiv.org/html/2602.14439v1#S2.E3 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")). As such, with an appropriate choice of 𝐐{\bm{Q}}, it is possible to approximate the theoretical maximum Sharpe ratio in high-dimensional settings when only sample covariance matrix is applied. However, when sample mean is further applied (i.e. problem ([3.2](https://arxiv.org/html/2602.14439v1#S3.E2 "In 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio"))), designing 𝐐{\bm{Q}} to be proportional to 𝚺{\bm{\Sigma}} cannot attain the theoretical maximum due to the presence of tr⁡[ℍ​𝚺]/T\operatorname{tr}\left[\mathbb{H}{\bm{\Sigma}}\right]/T.

###### Remark 5.

Let 𝐰˙\dot{\bm{w}} denote the solution of max𝐰​𝐰⊤​𝛍^−γ2​𝐰⊤​(𝚺^+η​𝐐)​𝐰\underset{\bm{w}}{\max}\;\bm{w}^{\top}{\widehat{{\bm{\mu}}}}-\frac{\gamma}{2}\bm{w}^{\top}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)\bm{w} without ESG level constraint, the limit of OOS SR of 𝐰˙\dot{\bm{w}} is limT→∞𝛍⊤​𝔾​𝛍1−s1,𝚺(1+s0)2​𝛍⊤​ℍ​𝛍+1T​tr⁡[ℍ​𝚺]\lim\_{T\rightarrow\infty}\frac{{\bm{\mu}}^{\top}\mathbb{G}{\bm{\mu}}}{{\sqrt{1-\frac{s\_{1,{\bm{\Sigma}}}}{(1+s\_{0})^{2}}}}\sqrt{{\bm{\mu}}^{\top}\mathbb{H}{\bm{\mu}}+\frac{1}{T}\operatorname{tr}\left[\mathbb{H}{\bm{\Sigma}}\right]}}. Compare to ([3.4](https://arxiv.org/html/2602.14439v1#S3.E4 "In Lemma 2. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio")), it is clear that imposing the ESG level constraint reduces the value of the numerator. The impact on the denominator, however, depends on the specific choice of the regularization matrix. In the special case where 𝐐=C​𝚺{\bm{Q}}=C{\bm{\Sigma}} with sufficiently large CC, the limiting OOS SR of 𝐰˙\dot{\bm{w}} can be rewritten as 𝛍⊤​𝚺−1​𝛍𝛍⊤​𝚺−1​𝛍+c\frac{{\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\bm{\mu}}}{\sqrt{{\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\bm{\mu}}+c}}, and that of 𝐰ˇ\check{\bm{w}} (optimal portfolio with ESG level constraint) is
𝛍⊤​𝚺−1​𝛍−(𝛍⊤​𝚺−1​𝐬~)2𝐬~⊤​𝚺−1​𝐬~𝛍⊤​𝚺−1​𝛍+c−(𝛍⊤​𝚺−1​𝐬~)2𝐬~⊤​𝚺−1​𝐬~\frac{{\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\bm{\mu}}-\frac{({\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}})^{2}}{{\tilde{{\bm{s}}}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}}}{\sqrt{{\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\bm{\mu}}+c-\frac{({\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}})^{2}}{{\tilde{{\bm{s}}}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}}}}, see Proposition [1](https://arxiv.org/html/2602.14439v1#Thmproposition1 "Proposition 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") below. Since the function f​(x)=x/x+cf(x)=x/\sqrt{x+c} is increasing in xx, imposing the ESG constraint leads to a decrease in the OOS SR.

A general comparison without specifying the form of 𝑸{\bm{Q}} is analytically intractable. As such, we now focus on a special situation where 𝑸=C​𝚺{\bm{Q}}=C{\bm{\Sigma}} with sufficiently large CC, which is the optimal choice for the regularized mean-variance problem using sample covariance matrix but population mean return and mean ESG score, as discussed in Remark [4](https://arxiv.org/html/2602.14439v1#Thmremark4 "Remark 4. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio").

###### Proposition 1.

Under the conditions of Lemma [1](https://arxiv.org/html/2602.14439v1#Thmlemma1 "Lemma 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio"), when 𝐐=C​𝚺{\bm{Q}}=C{\bm{\Sigma}}, where CC is allowed to depend on TT and satisfies C→∞C\to\infty as T→∞T\to\infty,
we have

|  |  |  |
| --- | --- | --- |
|  | θˇ∗−𝝁⊤​𝚺−1​𝝁−(𝝁⊤​𝚺−1​𝒔~)2𝒔~⊤​𝚺−1​𝒔~𝝁⊤​𝚺−1​𝝁+c−(𝝁⊤​𝚺−1​𝒔~)2𝒔~⊤​𝚺−1​𝒔~​⟶a.s​0,\displaystyle\check{\theta}^{\*}-\frac{{\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\bm{\mu}}-\frac{({\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}})^{2}}{{\tilde{{\bm{s}}}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}}}{\sqrt{{\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\bm{\mu}}+c-\frac{({\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}})^{2}}{{\tilde{{\bm{s}}}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}}}}\overset{a.s}{\longrightarrow}0, |  |
|  |  |  |
| --- | --- | --- |
|  | θ∗−𝝁⊤​𝚺−1​𝝁−(𝝁⊤​𝚺−1​𝒔~)2𝒔~⊤​𝚺−1​𝒔~+T−1​tr⁡[𝚺−1​𝛀]𝝁⊤​𝚺−1​𝝁+c−(𝝁⊤​𝚺−1​𝒔~)2𝒔~⊤​𝚺−1​𝒔~+T−1​tr⁡[𝚺−1​𝛀]​⟶a.s​0.\displaystyle{\theta}^{\*}-\frac{{\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\bm{\mu}}-\frac{({\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}})^{2}}{{\tilde{{\bm{s}}}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}+T^{-1}\operatorname{tr}\left[{\bm{\Sigma}}^{-1}\bm{\Omega}\right]}}{\sqrt{{\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\bm{\mu}}+c-\frac{({\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}})^{2}}{{\tilde{{\bm{s}}}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}+T^{-1}\operatorname{tr}\left[{\bm{\Sigma}}^{-1}\bm{\Omega}\right]}}}\overset{a.s}{\longrightarrow}0. |  |

First, for both 𝒘ˇ\check{\bm{w}} and 𝒘∗^\widehat{{\bm{w}}^{\ast}}, their OOS SR cannot attain the theoretical maximum θmax\theta\_{\max} due to the presence of the term c=limT→∞p/Tc=\lim\_{T\to\infty}p/T in the denominator. Nevertheless, our simulation results indicate that setting 𝑸=𝚺{\bm{Q}}={\bm{\Sigma}} remains a good choice, as it yields a higher OOS SR than the other considered alternatives of 𝑸{\bm{Q}} under finite sample. Second, interestingly, the estimation error in the ESG score mean does not adversely affect the financial results and, in fact, leads to higher Sharpe ratio performance. Specifically, let A:=𝝁⊤​𝚺−1​𝝁A:={\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\bm{\mu}}, B:=𝝁⊤​𝚺−1​𝒔~B:={\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}.
For function f​(x)=(A−B2/x)/A+c−B2/xf(x)=(A-B^{2}/x)/\sqrt{A+c-B^{2}/x}, by simple algebra, it is derivative with respect to xx is B2(A+2c−B2/x)/(2x2(A+c−B2x)3/2){B^{2}}(A+2c-{B^{2}}/{x})/\left(2x^{2}\right(A+c-\frac{B^{2}}{x})^{3/2}), which is strictly positive at x=𝒔~⊤​𝚺−1​𝒔~x={\tilde{{\bm{s}}}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}}, given that (𝝁⊤​𝚺−1​𝝁)​(𝒔~⊤​𝚺−1​𝒔~)≥(𝝁⊤​𝚺−1​𝒔~)2({\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\bm{\mu}})({\tilde{{\bm{s}}}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}})\geq({\bm{\mu}}^{\top}{\bm{\Sigma}}^{-1}{\tilde{{\bm{s}}}})^{2} from Cauchy-Schwarz inequality. As such, a positive value of tr⁡[𝚺−1​𝛀]\operatorname{tr}[{\bm{\Sigma}}^{-1}\bm{\Omega}] implies that the estimation error from sample ESG scores has a favorable impact on the OOS SR, whereas a negative value indicates a negative effect on portfolio performance.
Since 𝚺{\bm{\Sigma}} and 𝛀\bm{\Omega} are covariance matrices, which are symmetric and assumed to be positive definite, it is evident that the estimation error from estimating ESG score mean lead to an improvement in SR. As a result, we can safely use the sample ESG mean estimation as a proxy for the unknown the ESG mean level in large dimensional situation. Lastly, we note that, our analytical framework is not restricted to ESG scores and can be readily extended to other asset-level characteristics, thereby allowing the study of impact investing with respect to alternative dimensions. For readers’ convenience, Table [1](https://arxiv.org/html/2602.14439v1#S3.T1 "Table 1 ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") summarizes the optimization problems mentioned above and their corresponding limits of OOS SR.

Table 1: Optimization problems and the corresponding limit of OOS SRs.

|  |  |
| --- | --- |
| Optimization Problem | Limit of OOS SR |
| max𝒘​𝒘⊤​𝝁^−γ2​𝒘⊤​(𝚺^+η​𝑸)​𝒘\underset{\bm{w}}{\max}\;\bm{w}^{\top}{\widehat{{\bm{\mu}}}}-\frac{\gamma}{2}\bm{w}^{\top}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)\bm{w} | limT→∞𝝁⊤​𝔾​𝝁−(𝝁⊤​𝔾​𝒔~)2𝒔~⊤​𝔾​𝒔~+1T​tr⁡[𝔾​𝛀]1−s1,𝚺(1+s0)2​𝝁⊤​ℍ​𝝁+1T​tr⁡[ℍ​𝚺]+(𝝁⊤​𝔾​𝒔~)2​(𝒔~⊤​ℍ​𝒔~+1T​tr⁡[ℍ​𝛀])(𝒔~⊤​𝔾​𝒔~+1T​tr⁡[𝔾​𝛀])2−2​𝝁⊤​𝔾​𝒔~​𝝁⊤​ℍ​𝒔~𝒔~⊤​𝔾​𝒔~+1T​tr⁡[𝔾​𝛀]\lim\_{T\rightarrow\infty}\frac{{\bm{\mu}}^{\top}\mathbb{G}{\bm{\mu}}-\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}+\frac{1}{T}\operatorname{tr}\left[\mathbb{G}\bm{\Omega}\right]}}{{\sqrt{1-\frac{s\_{1,{\bm{\Sigma}}}}{(1+s\_{0})^{2}}}}\sqrt{{\bm{\mu}}^{\top}\mathbb{H}{\bm{\mu}}+\frac{1}{T}\operatorname{tr}\left[\mathbb{H}{\bm{\Sigma}}\right]+\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}\left({\tilde{{\bm{s}}}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}+\frac{1}{T}\operatorname{tr}\left[\mathbb{H}\bm{\Omega}\right]\right)}{\left({\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}+\frac{1}{T}\operatorname{tr}\left[\mathbb{G}\bm{\Omega}\right]\right)^{2}}-2\frac{{\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}{\bm{\mu}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}+\frac{1}{T}\operatorname{tr}\left[\mathbb{G}\bm{\Omega}\right]}}} |
| s.t.𝒘⊤𝒔~^=0s.t.\quad\bm{w}^{\top}\widehat{{\tilde{{\bm{s}}}}}=0 |  |
| max𝒘​𝒘⊤​𝝁^−γ2​𝒘⊤​(𝚺^+η​𝑸)​𝒘\underset{\bm{w}}{\max}\;\bm{w}^{\top}{\widehat{{\bm{\mu}}}}-\frac{\gamma}{2}\bm{w}^{\top}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)\bm{w} | limT→∞𝝁⊤​𝔾​𝝁−(𝝁⊤​𝔾​𝒔~)2𝒔~⊤​𝔾​𝒔~1−s1,𝚺(1+s0)2​𝝁⊤​ℍ​𝝁+1T​tr⁡[ℍ​𝚺]+(𝝁⊤​𝔾​𝒔~)2​𝒔~⊤​ℍ​𝒔~(𝒔~⊤​𝔾​𝒔~)2−2​𝝁⊤​𝔾​𝒔~​𝝁⊤​ℍ​𝒔~𝒔~⊤​𝔾​𝒔~\lim\_{T\rightarrow\infty}\frac{{\bm{\mu}}^{\top}\mathbb{G}{\bm{\mu}}-\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}}}{{\sqrt{1-\frac{s\_{1,{\bm{\Sigma}}}}{(1+s\_{0})^{2}}}}\sqrt{{\bm{\mu}}^{\top}\mathbb{H}{\bm{\mu}}+\frac{1}{T}\operatorname{tr}\left[\mathbb{H}{\bm{\Sigma}}\right]+\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}{\tilde{{\bm{s}}}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}}{\left({\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}}-2\frac{{\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}{\bm{\mu}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}}}} |
| s.t.𝒘⊤𝒔~=0s.t.\quad\bm{w}^{\top}{{\tilde{{\bm{s}}}}}=0 |  |
| max𝒘​𝒘⊤​𝝁−γ2​𝒘⊤​(𝚺^+η​𝑸)​𝒘\underset{\bm{w}}{\max}\;\bm{w}^{\top}{\bm{\mu}}-\frac{\gamma}{2}\bm{w}^{\top}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)\bm{w} | limT→∞𝝁⊤​𝔾​𝝁−(𝝁⊤​𝔾​𝒔~)2𝒔~⊤​𝔾​𝒔~1−s1,𝚺(1+s0)2​𝝁⊤​ℍ​𝝁+(𝝁⊤​𝔾​𝒔~)2​𝒔~⊤​ℍ​𝒔~(𝒔~⊤​𝔾​𝒔~)2−2​𝝁⊤​𝔾​𝒔~​𝝁⊤​ℍ​𝒔~𝒔~⊤​𝔾​𝒔~\lim\_{T\rightarrow\infty}\frac{{\bm{\mu}}^{\top}\mathbb{G}{\bm{\mu}}-\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}}}{{\sqrt{1-\frac{s\_{1,{\bm{\Sigma}}}}{(1+s\_{0})^{2}}}}\sqrt{{\bm{\mu}}^{\top}\mathbb{H}{\bm{\mu}}+\frac{\left({\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}{\tilde{{\bm{s}}}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}}{\left({\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}\right)^{2}}-2\frac{{\bm{\mu}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}{\bm{\mu}}^{\top}\mathbb{H}{\tilde{{\bm{s}}}}}{{\tilde{{\bm{s}}}}^{\top}\mathbb{G}{\tilde{{\bm{s}}}}}}} |
| s.t.𝒘⊤𝒔~=0s.t.\quad\bm{w}^{\top}{{\tilde{{\bm{s}}}}}=0 |  |
| max𝒘​𝒘⊤​𝝁^−γ2​𝒘⊤​(𝚺^+η​𝑸)​𝒘\underset{\bm{w}}{\max}\;\bm{w}^{\top}{\widehat{{\bm{\mu}}}}-\frac{\gamma}{2}\bm{w}^{\top}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)\bm{w} | limT→∞𝝁⊤​𝔾​𝝁1−s1,𝚺(1+s0)2​𝝁⊤​ℍ​𝝁+1T​tr⁡[ℍ​𝚺]\lim\_{T\rightarrow\infty}\frac{{\bm{\mu}}^{\top}\mathbb{G}{\bm{\mu}}}{{\sqrt{1-\frac{s\_{1,{\bm{\Sigma}}}}{(1+s\_{0})^{2}}}}\sqrt{{\bm{\mu}}^{\top}\mathbb{H}{\bm{\mu}}+\frac{1}{T}\operatorname{tr}\left[\mathbb{H}{\bm{\Sigma}}\right]}} |

In practice, the selection of the regularization matrix η​𝑸\eta{\bm{Q}} is important. Different choices of η​𝑸\eta{\bm{Q}} may result in different OOS SR performance.
Although Remark [4](https://arxiv.org/html/2602.14439v1#Thmremark4 "Remark 4. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") provides guidance for the optimal choice of the regularization matrix 𝑸{\bm{Q}} for the problem in which only the covariance matrix is replaced by its sample counterpart, there still exists a gap between the theoretical maximum Sharpe ratio θmax\theta\_{\max} and the OOS SR (shown in Proposition [1](https://arxiv.org/html/2602.14439v1#Thmproposition1 "Proposition 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) achieved by the proposed ESG-constrained portfolio. Furthermore, it is also of interest to determine an optimal tuning parameter η\eta that yields the best performance in finite samples given 𝑸{\bm{Q}}. However, given 𝑸{\bm{Q}} and η\eta, the out of sample Sharpe ratio θ∗\theta^{\*} is still not attainable based on historical data since it includes the unknown population parameter 𝝁{\bm{\mu}} and 𝚺{\bm{\Sigma}}. Clearly, if θ∗\theta^{\ast} can be consistently estimated using in-sample data, investors can readily evaluate the performance associated with different choices of η​𝑸\eta{\bm{Q}} and select the one that maximizes the out-of-sample Sharpe ratio of the proposed regularized ESG-constrained portfolio.
Accordingly, we propose an estimator for θ∗\theta^{\ast} under a given choice of 𝑸{\bm{Q}} and η\eta. Lastly, we note that, the estimation of the OOS SR, obtained by simply replacing the unknown 𝝁{\bm{\mu}} and 𝚺{\bm{\Sigma}} with their sample counterparts, is not a good choice in large-dimensional situations, as the naive empirical estimator often suffers from poor accuracy (Ao et al., [2019](https://arxiv.org/html/2602.14439v1#bib.bib55 "Approaching mean-variance efficiency for large portfolios"); Kan et al., [2024](https://arxiv.org/html/2602.14439v1#bib.bib7 "In-sample and out-of-sample sharpe ratios of multi-factor asset pricing models")).

We define the following quantities:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒟T,1​(η,𝑸)\displaystyle\mathcal{D}\_{T,1}(\eta,{\bm{Q}}) | :=(𝝁^+ζ^​𝒔~^)⊤​(𝚺^+η​𝑸)−1​𝝁,\displaystyle:={\left({\widehat{{\bm{\mu}}}}+\widehat{\zeta}\widehat{{\tilde{{\bm{s}}}}}\right)}^{\top}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)^{-1}{\bm{\mu}}, |  | (3.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒟T,2​(η,𝑸)\displaystyle\mathcal{D}\_{T,2}(\eta,{\bm{Q}}) | :=(𝝁^+ζ^​𝒔~^)⊤​(𝚺^+η​𝑸)−1​𝚺​(𝚺^+η​𝑸)−1​(𝝁^+ζ^​𝒔~^).\displaystyle:={\left({\widehat{{\bm{\mu}}}}+\widehat{\zeta}\widehat{{\tilde{{\bm{s}}}}}\right)}^{\top}\left({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}}\right)^{-1}{{\bm{\Sigma}}}\left({\widehat{\bm{\Sigma}}}+\eta{{\bm{Q}}}\right)^{-1}{\left({\widehat{{\bm{\mu}}}}+\widehat{\zeta}\widehat{{\tilde{{\bm{s}}}}}\right)}. |  | (3.6) |

The OOS SR of estimated ESG-constrained portfolio can be re-expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ∗​(η,𝑸)=𝒟T,1​(η,𝑸)|𝒟T,2​(η,𝑸)|.\theta^{\*}(\eta,{\bm{Q}})=\frac{\mathcal{D}\_{T,1}(\eta,{\bm{Q}})}{\sqrt{\lvert\mathcal{D}\_{T,2}(\eta,{\bm{Q}})\rvert}}. |  | (3.7) |

###### Theorem 1.

Suppose Assumptions [1](https://arxiv.org/html/2602.14439v1#Thmassumption1 "Assumption 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio")–[5](https://arxiv.org/html/2602.14439v1#Thmassumption5 "Assumption 5. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") hold true, define

|  |  |  |
| --- | --- | --- |
|  | 𝒟^T,1​(η,𝑸):=𝝁^⊤​(𝚺^+η​𝑸)−1​𝝁^+ζ^​𝒔~^⊤​(𝚺^+η​𝑸)−1​𝝁^−tr⁡((𝚺^+η​𝑸)−1​𝚺^)T−tr⁡((𝚺^+η​𝑸)−1​𝚺^),\displaystyle\widehat{\mathcal{D}}\_{T,1}(\eta,{\bm{Q}}):={\widehat{{\bm{\mu}}}}^{\top}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{\widehat{{\bm{\mu}}}}+\widehat{\zeta}\widehat{{\tilde{{\bm{s}}}}}^{\top}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{\widehat{{\bm{\mu}}}}-\frac{\operatorname{tr}\left(({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{\widehat{\bm{\Sigma}}}\right)}{T-\operatorname{tr}\left(({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{\widehat{\bm{\Sigma}}}\right)}, |  |
|  |  |  |
| --- | --- | --- |
|  | 𝒟^T,2​(η,𝑸):=(𝝁^+ζ^​𝒔~^)⊤​(𝚺^+η​𝑸)−1​𝚺^​(𝚺^+η​𝑸)−1​(𝝁^+ζ^​𝒔~^)/(1−cp​tr⁡(𝚺^​(𝚺^+𝑸)−1))2.\displaystyle\widehat{\mathcal{D}}\_{T,2}(\eta,{\bm{Q}}):=({\widehat{{\bm{\mu}}}}+\widehat{\zeta}\widehat{{\tilde{{\bm{s}}}}})^{\top}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}{\widehat{\bm{\Sigma}}}({\widehat{\bm{\Sigma}}}+\eta{\bm{Q}})^{-1}({\widehat{{\bm{\mu}}}}+\widehat{\zeta}\widehat{{\tilde{{\bm{s}}}}})/\left(1-\frac{c}{p}\operatorname{tr}\left({\widehat{\bm{\Sigma}}}({\widehat{\bm{\Sigma}}}+{\bm{Q}})^{-1}\right)\right)^{2}. |  |

Then as T→∞T\to\infty,

|  |  |  |
| --- | --- | --- |
|  | 𝒟^T,1​(η,𝑸)−𝒟T,1​(η,𝑸)→a.s.0,𝒟^T,2​(η,𝑸)−𝒟T,2​(η,𝑸)→a.s.0.\widehat{\mathcal{D}}\_{T,1}(\eta,{\bm{Q}})-{\mathcal{D}}\_{T,1}(\eta,{\bm{Q}})\xrightarrow{\mathrm{a.s.}}0,\qquad\widehat{\mathcal{D}}\_{T,2}(\eta,{\bm{Q}})-{\mathcal{D}}\_{T,2}(\eta,{\bm{Q}})\xrightarrow{\mathrm{a.s.}}0. |  |

Accordingly, the estimator of the out-of-sample Sharpe ratio is

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ^∗​(η,𝑸):=𝒟^T,1​(η,𝑸)𝒟^T,2​(η,𝑸),\widehat{\theta}^{\*}(\eta,{\bm{Q}}):=\frac{\widehat{\mathcal{D}}\_{T,1}(\eta,{\bm{Q}})}{\sqrt{\widehat{\mathcal{D}}\_{T,2}(\eta,{\bm{Q}})}}, |  | (3.8) |

and satisfies θ^∗​(η,𝐐)/θ∗​(η,𝐐)​⟶a.s​1\widehat{\theta}^{\*}(\eta,{\bm{Q}})/{\theta}^{\*}(\eta,{\bm{Q}})\overset{a.s}{\longrightarrow}1.

Theorem [1](https://arxiv.org/html/2602.14439v1#Thmtheorem1 "Theorem 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") establishes asymptotic consistency of θ^∗​(η,𝑸)\widehat{\theta}^{\*}(\eta,{\bm{Q}}) with respect to θ∗​(η,𝑸)\theta^{\*}(\eta,{\bm{Q}}), and thus provides a feasible tool for investors to
estimate OOS SR of proposed portfolio without requiring the knowledge of 𝝁{\bm{\mu}} and 𝚺{\bm{\Sigma}}. Consequently, investors can compare the estimated OOS SR θ^∗\widehat{\theta}^{\ast} across different combinations of (η,𝑸)(\eta,{\bm{Q}}) and select the one that achieves the highest SR.
Moreover, with SR estimator θ^∗\widehat{\theta}^{\ast} in hand, given a specific 𝑸{\bm{Q}}, it is natural for investors to select an optimal regularization coefficient η\eta by maximizing the OOS SR over a prespecified closed-interval candidate set 𝒢\mathcal{G}, i.e.,

|  |  |  |
| --- | --- | --- |
|  | η^∗=arg⁡maxη∈𝒢⁡θ^∗​(η,𝑸).\widehat{\eta}^{\*}=\arg\max\_{\eta\in\mathcal{G}}\widehat{\theta}^{\*}(\eta,{\bm{Q}}). |  |

As a result, the optimal choice of η\eta for a given regularization matrix 𝑸{\bm{Q}} can be implemented in practice to achieve the best Sharpe ratio performance in finite samples. In our simulation study, we also numerically assess the proximity of η^∗\widehat{\eta}^{\*} to the corresponding oracle value η∗:=arg⁡maxη∈𝒢⁡θ∗​(η,𝑸)\eta^{\*}:=\arg\max\_{\eta\in\mathcal{G}}{\theta}^{\*}(\eta,{\bm{Q}}), and the results demonstrate good performance. Finally, we note that, in theory, one could select an optimal 𝑸η:=η​𝑸{\bm{Q}}\_{\eta}:=\eta{\bm{Q}} to maximize the OOS SR estimation; however, since 𝑸η{\bm{Q}}\_{\eta} is a p×pp\times p positive definite matrix with large, achieving this goal using simple optimization techniques is challenging and time-consuming.

## 4 Simulation

In this section, we conduct Monte Carlo simulations to assess the performance of the newly developed Sharpe ratio estimator, and to evaluate the impact of different choices of 𝑸{\bm{Q}} on the OOS SR.

### 4.1 Basic Setup

The virtual return data and ESG score data are both generated from multivariate normal distributions with mean vectors 𝝁r{\bm{\mu}}\_{r} and 𝝁e​s​g{\bm{\mu}}\_{esg}, and covariance matrices 𝚺r{\bm{\Sigma}}\_{r} and 𝛀e​s​g\bm{\Omega}\_{esg}, respectively; that is, 𝒓t∼𝒩​(𝝁r,𝚺r),𝒂t∼𝒩​(𝝁e​s​g,𝛀e​s​g)\bm{r}\_{t}\sim\mathcal{N}({\bm{\mu}}\_{r},{\bm{\Sigma}}\_{r}),{\bm{a}}\_{t}\sim\mathcal{N}({\bm{\mu}}\_{esg},\bm{\Omega}\_{esg}).
To mimic the real world, the values of population parameters are calibrated from real monthly return and ESG scores data of the largest pp components (measured by market values) of the S&P 500 index from 01/2011 to 12/2019.333See more data descriptions in the section of empirical analysis. Specifically, 𝝁r{\bm{\mu}}\_{r} is calibrated as the sample means of the asset monthly return, and we set 𝚺r{\bm{\Sigma}}\_{r} to be the principal orthogonal
complement thresholding (POET) covariance estimator proposed by Fan et al. ([2013](https://arxiv.org/html/2602.14439v1#bib.bib56 "Large covariance estimation by thresholding principal orthogonal complements")) such that the population covariance matrix is positive definite (in the context of p>Tp>T) and has a factor structure.444The factor number is set to 2, which is estimated by the selection procedure of Bai and Ng ([2002](https://arxiv.org/html/2602.14439v1#bib.bib80 "Determining the number of factors in approximate factor models")). The adaptive thresholding estimation of sparse idiosyncratic covariance matrix is applied with thresholding parameter 1 and soft thresholding function (Cai and Liu, [2011](https://arxiv.org/html/2602.14439v1#bib.bib62 "Adaptive thresholding for sparse covariance matrix estimation"); Fan et al., [2013](https://arxiv.org/html/2602.14439v1#bib.bib56 "Large covariance estimation by thresholding principal orthogonal complements")).
For 𝝁e​s​g{\bm{\mu}}\_{esg} and 𝛀e​s​g\bm{\Omega}\_{esg}, we set them to the sample mean and sample covariance matrix of the ESG scores data.555For cases where p>Tp>T, we set 𝛀e​s​g=𝛀^e​s​g+ϵ1​Ip\bm{\Omega}\_{esg}=\hat{\bm{\Omega}}\_{esg}+\epsilon\_{1}I\_{p} to ensure positive definiteness, where 𝛀^e​s​g\hat{\bm{\Omega}}\_{esg} is the sample covariance matrix estimators and ϵ1\epsilon\_{1} is set to 10−610^{-6}.

### 4.2 Performance of SR estimator

In this subsection, we evaluate the performance of the newly proposed SR estimator. Specifically, we report the simulation results for SR estimation shown in ([3.8](https://arxiv.org/html/2602.14439v1#S3.E8 "In Theorem 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) and the corresponding oracle OOS SR shown in ([2.9](https://arxiv.org/html/2602.14439v1#S2.E9 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")). For our regularized ESG-constraint portfolio, we consider two specifications for the regularization matrix 𝑸{\bm{Q}}. (1) The first sets 𝑸=𝚺r{\bm{Q}}={\bm{\Sigma}}\_{r}, corresponding to the population covariance matrix, which is theoretically optimal when only sample covariance matrix is applied, see Remark [4](https://arxiv.org/html/2602.14439v1#Thmremark4 "Remark 4. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio"). (2) The second sets 𝑸=Ip{\bm{Q}}=I\_{p}, the identity matrix, which serves as a naive benchmark. Clearly, IpI\_{p} only regularizes the eigenvalues, whereas 𝚺r{\bm{\Sigma}}\_{r} not only adjusts the eigenvalues but also incorporates additional structural information. We note that, when 𝑸=Ip{\bm{Q}}=I\_{p}, 𝚺^+η​𝑸{\widehat{\bm{\Sigma}}}+\eta{\bm{Q}} is equivalent to the shrinkage covariance estimator proposed by Ledoit and Wolf ([2004](https://arxiv.org/html/2602.14439v1#bib.bib46 "A well-conditioned estimator for large-dimensional covariance matrices")) with shrinking intensity η\eta.
For the tuning parameter η\eta, its values are set to range from 0.2 to 10 with an increment of 0.2 in the first case, and from 0.0002 to 0.01 with an increment of 0.0002 in the second case.
The expected portfolio ESG score s¯{\bar{s}} is set to 0.8, which is larger than the ESG score of unconstrained oracle portfolio.
For the combinations of pp and TT, we consider (p,T)∈(60,120),(180,120),(180,360)(p,T)\in{(60,120),(180,120),(180,360)}, which correspond to p/Tp/T ratios of 0.5 and 1.5.
The simulation is replicated 1,000 times, and the reported results are the averages across these replications.

![Refer to caption](x1.png)


(a)

![Refer to caption](x2.png)


(b)

Figure 1: Simulation results of Sharpe ratio estimator and the corresponding oracle level with respect to η\eta.

Figure ([1(a)](https://arxiv.org/html/2602.14439v1#S4.F1.sf1 "In Figure 1 ‣ 4.2 Performance of SR estimator ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) and ([1(b)](https://arxiv.org/html/2602.14439v1#S4.F1.sf2 "In Figure 1 ‣ 4.2 Performance of SR estimator ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) show the simulation results for both situations. First of all, it is evident that the value of θ^∗​(η,𝑸)\widehat{\theta}^{\*}(\eta,{\bm{Q}}) matches the value of θ∗​(η,𝑸){\theta}^{\*}(\eta,{\bm{Q}}) well across various η\eta in most cases. As sample size TT increases, the SR estimations θ^∗​(η,𝑸)\widehat{\theta}^{\*}(\eta,{\bm{Q}}) becomes closer to the corresponding oracle level. Second, when 𝑸=𝚺r{\bm{Q}}={\bm{\Sigma}}\_{r}, we can observe that, as η\eta increases, the OOS SR of the proposed ESG-constrained portfolio increases. This is because the matrix 𝚺^+η​𝚺r\hat{{\bm{\Sigma}}}+\eta{\bm{\Sigma}}\_{r} becomes increasingly dominated by the term η​𝚺r\eta{\bm{\Sigma}}\_{r}, which is proportional to the true covariance matrix. In addition,
when 𝑸=𝑰p{\bm{Q}}=\bm{I}\_{p}, it can be observed that θ∗​(η,𝑸){\theta}^{\*}(\eta,{\bm{Q}}) first increases and then decreases as η\eta grows, indicating the existence of an optimal η\eta that maximizes the OOS SR. More importantly, we can observe that the proposed SR estimator θ^∗\widehat{\theta}^{\ast} closely replicates the pattern of θ∗\theta^{\ast}. Consequently, in practical applications, one can select the value of η\eta that maximizes the OOS SR without requiring knowledge of the true population parameters, and thus determine the optimal regularization matrix η​𝑸\eta{\bm{Q}} for a given 𝑸{\bm{Q}} over a deterministic candidate set 𝒢\mathcal{G} of η\eta.

![Refer to caption](x3.png)


(a)

![Refer to caption](x4.png)


(b)

Figure 2: Boxplots of the difference between estimated Sharpe ratio and the corresponding oracle level.

Next, we further evaluate the accuracy of the optimal η^∗\hat{\eta}^{\*} selected based on θ^∗\widehat{\theta}^{\ast}, by examining the discrepancy between η^∗\widehat{\eta}^{\ast} and the population level η∗\eta^{\ast} that maximizes the true (but unknown) θ∗\theta^{\ast}, i.e., η∗=arg​maxη∈𝒢⁡θ∗​(η,𝑸)\eta^{\*}=\operatorname\*{arg\,max}\_{\eta\in\mathcal{G}}\theta^{\*}(\eta,{\bm{Q}}). We focus on the case where 𝑸=𝑰p{\bm{Q}}=\bm{I}\_{p}, since Figure ([1(b)](https://arxiv.org/html/2602.14439v1#S4.F1.sf2 "In Figure 1 ‣ 4.2 Performance of SR estimator ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) indicates that the optimal η∗\eta^{\ast} lies in the interior of the candidate set 𝒢=[0.0002,0.01]\mathcal{G}=[0.0002,0.01].

Specifically, the y-axis of Figures ([2(a)](https://arxiv.org/html/2602.14439v1#S4.F2.sf1 "In Figure 2 ‣ 4.2 Performance of SR estimator ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) and ([2(b)](https://arxiv.org/html/2602.14439v1#S4.F2.sf2 "In Figure 2 ‣ 4.2 Performance of SR estimator ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) gives the boxplot of the discrepancies (i.e., arg​maxη∈𝒢⁡θ∗​(η,𝑸)−arg​maxη∈𝒢⁡θ^∗​(η,𝑸)\operatorname\*{arg\,max}\_{\eta\in\mathcal{G}}\theta^{\*}(\eta,{\bm{Q}})-\operatorname\*{arg\,max}\_{\eta\in\mathcal{G}}\widehat{\theta}^{\*}(\eta,{\bm{Q}})) over 1000 independent simulation experiments for various situations. In Figure ([2(a)](https://arxiv.org/html/2602.14439v1#S4.F2.sf1 "In Figure 2 ‣ 4.2 Performance of SR estimator ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio")), the p/Tp/T ratio is fixed at 0.5 with p=60,120,p=60,120, and 180180. In Figure ([2(b)](https://arxiv.org/html/2602.14439v1#S4.F2.sf2 "In Figure 2 ‣ 4.2 Performance of SR estimator ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio")), we fix p=180p=180 and consider increasing sample sizes of T=120,240,T=120,240, and 480480 such that p/Tp/T ratio decreases.
It can be observed that, under a fixed p/Tp/T ratio, as the sample size increases, the variability of the difference between the optimal η∗\eta^{\*} and its estimator η^∗\widehat{\eta}^{\*} decreases, and its mean value becomes closer to zero. Similarly, as the ratio p/Tp/T decreases (i.e., with a larger sample size), the discrepancy between η^∗\widehat{\eta}^{\ast} and η∗\eta^{\ast} diminishes. As such, these results indicate that selecting the optimal value of η\eta based on the proposed Sharpe ratio estimator is approximately as efficient as using the true Sharpe ratio θ∗\theta^{\ast}, highlighting the excellent performance of our out-of-sample Sharpe ratio estimator.

### 4.3 The Choices of Regularization Matrix

In this subsection, we evaluate the performance of the proposed regularized portfolios by examining how different choices of 𝑸{\bm{Q}} affect the out-of-sample financial and sustainable performance of the portfolio. Specifically, we consider the OOS average return A​MAM, standard deviation S​DSD, Sharpe ratio S​RSR, average portfolio ESG score A​Me​s​gAM\_{esg}, and the standard deviation of portfolio ESG scores S​De​s​gSD\_{esg} for estimated portfolio, which are defined respectively as follows:

|  |  |  |
| --- | --- | --- |
|  | A​M=𝒘^⊤​𝝁,S​D=𝒘^⊤​𝚺​𝒘^,S​R=𝒘^⊤​𝝁𝒘^⊤​𝚺​𝒘^,\displaystyle AM=\widehat{\bm{w}}^{\top}{\bm{\mu}},\quad SD=\sqrt{\widehat{\bm{w}}^{\top}{\bm{\Sigma}}\widehat{\bm{w}}},\quad SR=\frac{\widehat{\bm{w}}^{\top}{\bm{\mu}}}{\sqrt{\widehat{\bm{w}}^{\top}{\bm{\Sigma}}\widehat{\bm{w}}}}, |  |
|  |  |  |
| --- | --- | --- |
|  | A​Me​s​g=𝒘^⊤​μe​s​g,S​De​s​g=𝒘^⊤​𝛀e​s​g​𝒘^.\displaystyle AM\_{esg}=\widehat{\bm{w}}^{\top}\mu\_{esg},\quad SD\_{esg}=\sqrt{\widehat{\bm{w}}^{\top}\bm{\Omega}\_{esg}\widehat{\bm{w}}}. |  |

Here, 𝒘^\widehat{\bm{w}} denotes the scaled estimated portfolio such that 𝒘^⊤​𝟏=1\widehat{\bm{w}}^{\top}\bm{1}=1.

Since we are interested in the choice of regularization term η​𝑸\eta{\bm{Q}}, we consider the following several specifications for 𝑸{\bm{Q}}: (1) Identity matrix, denoted as 𝑰p\bm{I}\_{p};
(2) Diagonal matrix of sample return covariance matrix, denoted as 𝚺^d\hat{{\bm{\Sigma}}}\_{d};
(3) Linear shrinkage covariance matrix estimation proposed by Ledoit and Wolf ([2004](https://arxiv.org/html/2602.14439v1#bib.bib46 "A well-conditioned estimator for large-dimensional covariance matrices")), denoted as 𝚺^l​i​n​e​a​r{\widehat{\bm{\Sigma}}}\_{linear}, the shrinkage intensity is determined following Ledoit and Wolf ([2003](https://arxiv.org/html/2602.14439v1#bib.bib81 "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection"));
(4) Nonlinear shrinkage covariance matrix estimation proposed by Ledoit and Wolf ([2017](https://arxiv.org/html/2602.14439v1#bib.bib65 "Nonlinear shrinkage of the covariance matrix for portfolio selection: Markowitz meets Goldilocks")), denoted as 𝚺^N​o​n​l​i​n​e​a​r{\widehat{\bm{\Sigma}}}\_{Nonlinear};
(5) POET covariance estimation proposed by Fan et al. ([2013](https://arxiv.org/html/2602.14439v1#bib.bib56 "Large covariance estimation by thresholding principal orthogonal complements")), 𝚺^P​O​E​T{\widehat{\bm{\Sigma}}}\_{POET}, the factor number is selected by the procedure of Bai and Ng ([2002](https://arxiv.org/html/2602.14439v1#bib.bib80 "Determining the number of factors in approximate factor models")), and the sparse covariance matrix is estimated by using soft thresholding function with threshold parameter 0.5;
(6) Sample covariance matrix of assets’ ESG scores, denoted as 𝛀^e​s​g\widehat{\bm{\Omega}}\_{esg}, and we use 𝛀^e​s​g+10−6​Ip\widehat{\bm{\Omega}}\_{esg}+10^{-6}I\_{p} to ensure the positive definiteness when p>Tp>T; (7) Diagonal matrix whose diagonal elements are the reciprocals of the corresponding sample mean ESG scores, denoted as 𝑫−1\bm{D}^{-1};
(8) Diagonal matrix whose diagonal elements are the corresponding sample mean ESG scores, denoted as 𝑫\bm{D};
(9) Population return covariance matrix, denoted as 𝚺r{\bm{\Sigma}}\_{r}; (10) Population covariance matrix of assets’ ESG scores, denoted as 𝛀e​s​g\bm{\Omega}\_{esg}.
Case (1) is a naive choice that ensures the positive definiteness of 𝚺^+η​𝑸\widehat{{\bm{\Sigma}}}+\eta{\bm{Q}}; Cases (2)–(5) employ return covariance matrix estimators commonly used in the portfolio allocation literature as the regularization matrix. Cases (6)–(8) incorporate information from ESG score variables for penalization. Cases (9) and (10) rely on unknown population quantities, which are infeasible in practice and therefore serve only as benchmark cases.
We report the results using η^∗\widehat{\eta}^{\*} and η∗\eta^{\*}. The results of our new portfolio are labeled as Re-MV (Regularized esg-constrained Mean-Variance portfolio). The candidate set 𝒢\mathcal{G} ranges from 0.0002 to 0.01 with an increment of 0.0002 for Case (1), from 0.02 to 1 with an increment of 0.02 for Cases (7)–(8), and from 0.2 to 10 with an increment of 0.2 for the remaining cases.

For comparison, the results of following benchmarks are reported: (1) Oracle: mean-variance portfolio using population parameter values in ([1.1](https://arxiv.org/html/2602.14439v1#S1.E1 "In 1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio")); (2) Sample: mean-variance portfolio using sample mean and sample covariance matrix in ([1.1](https://arxiv.org/html/2602.14439v1#S1.E1 "In 1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio")); (3) M-MV-O: mean-variance portfolio with ESG level constraint shown in ([2.1](https://arxiv.org/html/2602.14439v1#S2.E1 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) using population parameters; (4) M-MV-S: mean-variance portfolio with ESG level constraint shown in ([2.1](https://arxiv.org/html/2602.14439v1#S2.E1 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) using sample mean return, sample covariance of return, and sample mean ESG score;
(5) Q-MV: regularized mean-variance portfolio in ([2.6](https://arxiv.org/html/2602.14439v1#S2.E6 "In 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio")) without ESG level constraint using sample mean and sample covariance.

Table 2: Simulation results for considered strategies across various regularization matrix 𝑸{\bm{Q}}. p=180,T=360p=180,T=360, respectively. The target ESG level s¯{\bar{s}} is set to 0.80.8.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | A​MAM | S​DSD | S​RSR | A​Me​s​gAM\_{esg} | S​De​s​gSD\_{esg} | A​MAM | S​DSD | S​RSR | A​Me​s​gAM\_{esg} | S​De​s​gSD\_{esg} |
| Oracle | 0.0850 | 0.074 | 1.154 | -0.402 | 0.268 | - | - | - | - | - |
| M-MV-O | 0.1097 | 0.101 | 1.083 | 0.800 | 0.234 | - | - | - | - | - |
| Sample | 0.1403 | 0.205 | 0.697 | -1.139 | 0.534 | - | - | - | - | - |
| M-MV-S | 0.1476 | 0.630 | 0.592 | 0.778 | 1.373 | - | - | - | - | - |
|  | 𝑸=𝑰p{\bm{Q}}=\bm{I}\_{p} | | | | | 𝑸=𝚺^d{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{d} | | | | |
| Q-MV(η^∗\hat{\eta}^{\*}) | 0.0498 | 0.056 | 0.897 | 0.153 | 0.145 | 0.0479 | 0.052 | 0.925 | 0.145 | 0.150 |
| Q-MV(η∗{\eta}^{\*}) | 0.0491 | 0.055 | 0.901 | 0.162 | 0.143 | 0.0473 | 0.051 | 0.928 | 0.153 | 0.148 |
| Re-MV(η^∗\hat{\eta}^{\*}) | 0.0615 | 0.074 | 0.830 | 0.799 | 0.133 | 0.0562 | 0.066 | 0.856 | 0.799 | 0.121 |
| Re-MV(η∗{\eta}^{\*}) | 0.0602 | 0.072 | 0.834 | 0.799 | 0.129 | 0.0551 | 0.064 | 0.860 | 0.799 | 0.118 |
|  | 𝑸=𝑫{\bm{Q}}=\bm{D} | | | | | 𝑸=𝑫−1{\bm{Q}}=\bm{D}^{-1} | | | | |
| Q-MV(η^∗\hat{\eta}^{\*}) | 0.0286 | 0.037 | 0.777 | 0.385 | 0.092 | 0.0214 | 0.034 | 0.632 | 0.569 | 0.055 |
| Q-MV(η∗{\eta}^{\*}) | 0.0286 | 0.037 | 0.777 | 0.385 | 0.092 | 0.0214 | 0.034 | 0.632 | 0.569 | 0.055 |
| Re-MV(η^∗\hat{\eta}^{\*}) | 0.0339 | 0.046 | 0.729 | 0.799 | 0.075 | 0.0236 | 0.038 | 0.613 | 0.800 | 0.037 |
| Re-MV(η∗{\eta}^{\*}) | 0.0339 | 0.046 | 0.729 | 0.799 | 0.075 | 0.0236 | 0.038 | 0.613 | 0.800 | 0.037 |
|  | 𝑸=𝚺^l​i​n​e​a​r{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{linear} | | | | | 𝑸=𝚺^N​o​n​l​i​n​e​a​r{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{Nonlinear} | | | | |
| Q-MV(η^∗\hat{\eta}^{\*}) | 0.0951 | 0.126 | 0.756 | -0.508 | 0.333 | 0.067 | 0.075 | 0.900 | -0.078 | 0.196 |
| Q-MV(η∗{\eta}^{\*}) | 0.0951 | 0.126 | 0.756 | -0.508 | 0.333 | 0.067 | 0.075 | 0.900 | -0.079 | 0.196 |
| Re-MV(η^∗\hat{\eta}^{\*}) | 0.2392 | 0.418 | 0.683 | 0.781 | 0.865 | 0.096 | 0.116 | 0.831 | 0.799 | 0.215 |
| Re-MV(η∗{\eta}^{\*}) | 0.2392 | 0.418 | 0.683 | 0.781 | 0.865 | 0.097 | 0.116 | 0.831 | 0.799 | 0.215 |
|  | 𝑸=𝛀^e​s​g{\bm{Q}}=\widehat{\bm{\Omega}}\_{esg} | | | | | 𝑸=𝛀e​s​g{\bm{Q}}={\bm{\Omega}}\_{esg} | | | | |
| Q-MV(η^∗\hat{\eta}^{\*}) | 0.0839 | 0.120 | 0.702 | -0.263 | 0.005 | 0.0838 | 0.120 | 0.703 | -0.261 | 0.004 |
| Q-MV(η∗{\eta}^{\*}) | 0.0834 | 0.119 | 0.703 | -0.257 | 0.003 | 0.0834 | 0.119 | 0.703 | -0.257 | 0.003 |
| Re-MV(η^∗\hat{\eta}^{\*}) | 0.0743 | 0.277 | 0.646 | 0.800 | 0.011 | -2.0725 | 3.718 | 0.646 | 0.801 | 0.092 |
| Re-MV(η∗{\eta}^{\*}) | 0.0684 | 0.267 | 0.646 | 0.800 | 0.007 | -2.0767 | 3.711 | 0.647 | 0.801 | 0.089 |
|  | 𝑸=𝚺^P​O​E​T{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{POET} | | | | | 𝑸=𝚺r{\bm{Q}}={\bm{\Sigma}}\_{r} | | | | |
| Q-MV(η^∗\hat{\eta}^{\*}) | 0.1232 | 0.282 | 0.844 | -0.769 | 0.854 | 0.089 | 0.091 | 0.982 | -0.455 | 0.290 |
| Q-MV(η∗{\eta}^{\*}) | 0.1274 | 0.408 | 0.827 | -1.010 | 1.226 | 0.089 | 0.090 | 0.983 | -0.455 | 0.290 |
| Re-MV(η^∗\hat{\eta}^{\*}) | 0.2234 | 0.775 | 0.623 | 0.806 | 1.654 | 0.123 | 0.136 | 0.906 | 0.798 | 0.300 |
| Re-MV(η∗{\eta}^{\*}) | 0.6013 | 1.594 | 0.479 | 0.794 | 3.239 | 0.123 | 0.136 | 0.907 | 0.798 | 0.300 |

For the optimization with the ESG-level constraint, we again set the threshold to 0.8,666The ESG score of oracle mean-variance portfolio is less than 0.8 in our simulation. and focus on simulation replications where the out-of-sample ESG score of the sample mean–variance portfolio falls below this value.777When the ESG score of the sample mean–variance portfolio exceeds the preset threshold s¯{\bar{s}}, the ESG-level constraint becomes non-binding for M-MV-S and Re-MV, and thus M-MV-S degenerates to sample and Re-MV degenerates to Q-MV. The results of our method is labeled as Re-MV. Two combinations {p=180,T=120}\{p=180,T=120\} and {p=180,T=360}\{p=180,T=360\} of pp and TT are considered, risk aversion parameter γ\gamma is set to 5, and simulation results are the average level over 1000 replications.

Table 3: Simulation results for considered strategies across various regularization matrix 𝑸{\bm{Q}}. p=180,T=120p=180,T=120, respectively. The target ESG level s¯{\bar{s}} is set to 0.80.8.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | A​MAM | S​DSD | S​RSR | A​Me​s​gAM\_{esg} | S​De​s​gSD\_{esg} | A​MAM | S​DSD | S​RSR | A​Me​s​gAM\_{esg} | S​De​s​gSD\_{esg} |
| Oracle | 0.0850 | 0.074 | 1.154 | -0.402 | 0.268 | - | - | - | - | - |
| M-MV-O | 0.1097 | 0.101 | 1.083 | 0.800 | 0.234 | - | - | - | - | - |
|  | 𝑸=𝑰p{\bm{Q}}=\bm{I}\_{p} | | | | | 𝑸=𝚺^d{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{d} | | | | |
| Q-MV(η^∗\hat{\eta}^{\*}) | 0.0470 | 0.072 | 0.689 | 0.220 | 0.152 | 0.0415 | 0.056 | 0.744 | 0.250 | 0.139 |
| Q-MV(η∗{\eta}^{\*}) | 0.0357 | 0.049 | 0.727 | 0.350 | 0.106 | 0.0350 | 0.046 | 0.764 | 0.329 | 0.113 |
| Re-MV(η^∗\hat{\eta}^{\*}) | 0.0636 | 0.157 | 0.618 | 0.801 | 0.239 | 0.0502 | 0.081 | 0.675 | 0.798 | 0.140 |
| Re-MV(η∗{\eta}^{\*}) | 0.0436 | 0.066 | 0.661 | 0.798 | 0.100 | 0.0402 | 0.057 | 0.699 | 0.798 | 0.093 |
|  | 𝑸=𝑫{\bm{Q}}=\bm{D} | | | | | 𝑸=𝑫−1{\bm{Q}}=\bm{D}^{-1} | | | | |
| Q-MV(η^∗\hat{\eta}^{\*}) | 0.0277 | 0.040 | 0.691 | 0.397 | 0.091 | 0.0214 | 0.036 | 0.600 | 0.570 | 0.056 |
| Q-MV(η∗{\eta}^{\*}) | 0.0277 | 0.040 | 0.691 | 0.398 | 0.091 | 0.0214 | 0.036 | 0.600 | 0.570 | 0.056 |
| Re-MV(η^∗\hat{\eta}^{\*}) | 0.0338 | 0.054 | 0.627 | 0.798 | 0.082 | 0.0239 | 0.042 | 0.569 | 0.799 | 0.040 |
| Re-MV(η∗{\eta}^{\*}) | 0.0337 | 0.054 | 0.627 | 0.798 | 0.081 | 0.0239 | 0.042 | 0.569 | 0.799 | 0.040 |
|  | 𝑸=𝚺^l​i​n​e​a​r{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{linear} | | | | | 𝑸=𝚺^N​o​n​l​i​n​e​a​r{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{Nonlinear} | | | | |
| Q-MV(η^∗\hat{\eta}^{\*}) | 0.062 | 0.180 | 0.559 | -0.094 | 0.366 | 0.051 | 0.072 | 0.722 | 0.158 | 0.152 |
| Q-MV(η∗{\eta}^{\*}) | 0.062 | 0.180 | 0.559 | -0.094 | 0.366 | 0.052 | 0.072 | 0.722 | 0.153 | 0.154 |
| Re-MV(η^∗\hat{\eta}^{\*}) | 0.062 | 0.458 | 0.456 | 0.756 | 0.787 | 0.062 | 0.129 | 0.640 | 0.800 | 0.207 |
| Re-MV(η∗{\eta}^{\*}) | 0.062 | 0.458 | 0.456 | 0.756 | 0.787 | 0.064 | 0.131 | 0.641 | 0.800 | 0.211 |
|  | 𝑸=𝛀^e​s​g{\bm{Q}}=\widehat{\bm{\Omega}}\_{esg} | | | | | 𝑸=𝛀e​s​g{\bm{Q}}={\bm{\Omega}}\_{esg} | | | | |
| Q-MV(η^∗\hat{\eta}^{\*}) | 0.0652 | 0.363 | 0.367 | -0.119 | 0.008 | 0.030 | 0.503 | 0.365 | 0.129 | 0.011 |
| Q-MV(η∗{\eta}^{\*}) | 0.1358 | 0.391 | 0.477 | -0.848 | 0.008 | 0.064 | 0.369 | 0.381 | -0.082 | 0.008 |
| Re-MV(η^∗\hat{\eta}^{\*}) | -0.0406 | 0.632 | 0.280 | 0.800 | 0.014 | 0.259 | 1.223 | 0.281 | 0.802 | 0.026 |
| Re-MV(η∗{\eta}^{\*}) | 0.0702 | 0.430 | 0.384 | 0.800 | 0.009 | 0.065 | 0.980 | 0.295 | 0.800 | 0.021 |
|  | 𝑸=𝚺^P​O​E​T{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{POET} | | | | | 𝑸=𝚺r{\bm{Q}}={\bm{\Sigma}}\_{r} | | | | |
| Q-MV(η^∗\hat{\eta}^{\*}) | 0.166 | 0.436 | 0.526 | -1.332 | 1.037 | 0.0887 | 0.177 | 0.752 | -0.468 | 0.471 |
| Q-MV(η∗{\eta}^{\*}) | -0.059 | 1.075 | 0.521 | 2.331 | 2.443 | 0.1048 | 0.147 | 0.780 | -0.653 | 0.410 |
| Re-MV(η^∗\hat{\eta}^{\*}) | 0.844 | 1.790 | 0.363 | 1.027 | 4.957 | 0.0470 | 0.404 | 0.634 | 0.812 | 0.839 |
| Re-MV(η∗{\eta}^{\*}) | -0.048 | 1.005 | 0.278 | 0.788 | 1.904 | 0.1321 | 0.427 | 0.663 | 0.800 | 0.923 |

Tables [2](https://arxiv.org/html/2602.14439v1#S4.T2 "Table 2 ‣ 4.3 The Choices of Regularization Matrix ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio")-[3](https://arxiv.org/html/2602.14439v1#S4.T3 "Table 3 ‣ 4.3 The Choices of Regularization Matrix ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio") report the simulation results for various forms of 𝑸{\bm{Q}} under considered two sample-dimension combinations, respectively. Several findings can be summarized as follows: (1) First, the two oracle portfolios achieve the highest SRs, 1.154 and 1.083, respectively. The unconstrained oracle portfolio exhibits a low ESG score of −0.402-0.402, whereas the ESG-constrained oracle portfolio satisfies the required ESG level. Imposing an ESG-level constraint can substantially improve OOS ESG performance with only a slight sacrifice in portfolio SR. (2) Second, compared to the oracle portfolios, the constrained and unconstrained sample mean–variance portfolios achieve much lower Sharpe ratios, 0.697 and 0.592, respectively, and the unconstrained sample portfolio exhibits a substantially lower ESG level of −1.139-1.139 (in the case of p<Tp<T). (3) Third, for the regularized (un)constrained portfolios, it is evident that different choices of the regularization matrix 𝑸{\bm{Q}} lead to different performance outcomes. Specifically, when 𝑸=𝚺r{\bm{Q}}={\bm{\Sigma}}\_{r}, both Q-MV and Re-MV achieve the highest OOS SRs. However, 𝚺r{\bm{\Sigma}}\_{r} is unattainable in practice. Among all feasible choices of 𝑸{\bm{Q}}, setting 𝑸=𝚺^d{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{d} yields the highest OOS SRs for the regularized portfolios, substantially improving on the performance of the sample portfolio. Furthermore, the corresponding ESG level of the Re-MV portfolio is very close to the required standard 0.8. In the case of p>Tp>T, the OOS SRs of Re-MV with 𝑸=𝚺^d{\bm{Q}}=\widehat{{\bm{\Sigma}}}\_{d} using η^∗\hat{\eta}^{\ast} and η∗\eta^{\ast} are 0.675 and 0.699, respectively, both of which exceed the corresponding values of 0.634 and 0.663 obtained by Re-MV with 𝑸=𝚺r{\bm{Q}}={\bm{\Sigma}}\_{r} using η^∗\hat{\eta}^{\ast} and η∗\eta^{\ast}, respectively.
The second-tier SR performance is achieved by choosing 𝑸=Ip{\bm{Q}}=I\_{p} and 𝑸=𝚺^N​o​n​l​i​n​e​a​r{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{Nonlinear}. We note that, since the population parameters are calibrated using real return and ESG score data, we believe that these choices are capable of delivering good performance in practical applications and can therefore serve as useful guidance for practical implementation. (4) Under the situations in which 𝑸{\bm{Q}} is set to the (estimated) covariance of ESG scores (i.e. 𝑸=𝛀e​s​g,𝛀^e​s​g{\bm{Q}}=\bm{\Omega}\_{esg},\widehat{\bm{\Omega}}\_{esg}), the regularized portfolios exhibit SRs similar to those of the corresponding sample portfolios and provide slight improvement in SR performance. Based on the economic interpretation in Remark [1](https://arxiv.org/html/2602.14439v1#Thmremark1 "Remark 1. ‣ 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio"), for an ESG-concerned investor who solves the mean–variance optimization problem with additional ESG-mean and ESG-variance constraints (i.e., problem ([2.8](https://arxiv.org/html/2602.14439v1#S2.E8 "In Remark 1. ‣ 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio"))), imposing an ESG risk constraint to restrict the portfolio ESG variance contributes little to improving SR performance. As a result, for data providers, ESG measure designers, and even policymakers, adjusting the covariance structure of assets’ ESG scores to align with other considered forms of 𝑸{\bm{Q}} (e.g., 𝚺^d{\widehat{\bm{\Sigma}}}\_{d}) can enable ESG-motivated investors to achieve better financial performance in high-dimensional settings when portfolio ESG-variance constraints are further imposed. (5) Comparing the results obtained with 𝑸=𝑫{\bm{Q}}=\bm{D} and 𝑸=𝑫−1{\bm{Q}}=\bm{D}^{-1}, it is evident that using ESG score levels yields better SR performance than using the reciprocals of ESG levels, as considered in Makridis and Simaan ([2023](https://arxiv.org/html/2602.14439v1#bib.bib166 "Balancing returns and responsibility: evidence from shrinkage-based portfolios")).
(6) Next, it can be observed that the performances of Q-MV and Re-MV based on θ^∗\widehat{\theta}^{\*} are close to those obtained using the oracle θ∗{\theta}^{\*}, indicating that the estimation of the optimal η\eta is accurate and performs well in practice. (7) It is evident that, with an appropriately chosen 𝑸{\bm{Q}}, the newly proposed optimization problem performs well in the case of p>Tp>T. As such, our method extends the classic sample portfolio to settings where p>Tp>T.
(8) Moreover, based on the ESG variance measure S​De​s​gSD\_{esg}, it is evident that Re-MV also achieves the lower OOS portfolio ESG volatility, compared to both oracle portfolios and sample portfolios. Although choosing 𝑸{\bm{Q}} different from 𝛀e​s​g\bm{\Omega}\_{esg} does not explicitly restrict the variance of the portfolio ESG scores, it still leads to improved stability of ESG outcomes. (9) Finally, comparing the results of Q-MV and Re-MV reveals that, in high-dimensional settings, the desired sustainable ESG level can be attained by imposing the ESG-level constraint, without incurring a significant reduction in the SR. As a consequence, with an appropriately chosen regularization matrix 𝑸{\bm{Q}}, the proposed portfolio can achieve a stable ESG score that satisfies the required level while maintaining an ideal OOS SR.

## 5 Empirical application

In this section, we evaluate the out-of-sample economic and ESG performance of our proposed regularized ESG-constrained mean-variance portfolio using real market data. Specifically, the evaluation procedure is conducted under the rolling-window scheme. At each decision point, we use the historical data of length TT to construct portfolios, which are then held for the next several periods (say Th​o​l​dT\_{hold}) to gain the OOS realized excess portfolio return and OOS portfolio ESG score. After holding portfolios for Th​o​l​dT\_{hold} periods, we re-balance the portfolio allocation using the updated data till the new decision point. This process is repeated until the end of the out-of-sample periods.

### 5.1 Data

We consider monthly return data of component stocks of the S&P 500 index, sourced from the Center for Research in Security Prices (CRSP). The S&P 500 index consists of large-cap stocks, representing the largest publicly traded companies in the U.S. The data cover the period from January 2010 to December 2024, comprising 180 monthly observations over 15 years. We delete those stocks that do not have complete historical data at the first decision point. To avoid look-ahead bias due to missing data during the rolling window process, we simply drop the corresponding assets from the basket (Ao et al., [2019](https://arxiv.org/html/2602.14439v1#bib.bib55 "Approaching mean-variance efficiency for large portfolios"); Fan et al., [2024b](https://arxiv.org/html/2602.14439v1#bib.bib129 "Time-varying minimum variance portfolio"); Wu et al., [2025](https://arxiv.org/html/2602.14439v1#bib.bib13 "Making distributionally robust portfolios feasible in high dimension")).
The risk-free data are downloaded from the Ken French’s data library.888<https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html> For the ESG score data corresponding to each asset in the considered investment universe over the considered periods, we obtained them from the Refinitiv ESG dataset provided by London Stock Exchange Group (LSEG).999<https://www.lseg.com/en> LSEG ESG provides one of the most comprehensive ESG datasets in the industry, covering over 88% of the global market capitalization and more than 700 individual ESG metrics.

Based on the components of the S&P 500 index, we consider two scenarios:
(1) the largest (randomly selected) p=60p=60 stocks (measured by market capitalization) with a sample size of T=90T=90, thus the sample size is larger than the number of assets; and
(2) the largest (randomly selected) p=180p=180 stocks with a sample size of T=90T=90, thus the sample size is smaller than the dimension. The out of sample periods for both cases is from 06/2017 to 12/2024, also covering 90 periods.

### 5.2 Portfolios and Measures

For the newly proposed regularized ESG-constrained portfolio, our simulation results indicate the importance of selecting an appropriate form of the regularization matrix 𝑸{\bm{Q}}, as it has a substantial impact on portfolio SR performance. Although our simulations suggest that 𝑸=𝚺^d{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{d} is the best feasible choice among considered candidates, practical settings are likely to be considerably more complex than the simulation environment considered here.
Fortunately, the availability of proposed OOS SR estimator θ^∗\widehat{\theta}^{\*} allows us to evaluate portfolio OOS performance at each decision node based on historical data. Therefore, we can estimate the OOS SRs for portfolios constructed with different choices of 𝑸{\bm{Q}} and the corresponding estimated η^∗\hat{\eta}^{\ast}, and select the regularization matrix η^∗​𝑸\hat{\eta}^{\ast}{\bm{Q}} that yields the highest estimated SR. In our empirical studies, we apply this adaptive strategy and consider 𝑸=𝚺^d{\bm{Q}}={\widehat{\bm{\Sigma}}}\_{d}, 𝚺^N​o​n​l​i​n​e​a​r{\widehat{\bm{\Sigma}}}\_{Nonlinear}, and IpI\_{p} as candidate choices. The results are labeled as Re-MV. The candidate set 𝒢\mathcal{G} for η\eta takes the same range as those used in our simulation study.

As benchmarks, beyond the feasible strategies introduced in the simulation section, we further include the following six portfolios for comparison: (1)-(2) mean–variance portfolio with (without) ESG level constraint (M-MV-POET / MV-POET), based on factor-model-estimated means and the POET covariance estimator (Fan et al., [2013](https://arxiv.org/html/2602.14439v1#bib.bib56 "Large covariance estimation by thresholding principal orthogonal complements"); Wu et al., [2025](https://arxiv.org/html/2602.14439v1#bib.bib13 "Making distributionally robust portfolios feasible in high dimension")); The number of common factors is selected by BIC criterion of Bai and Ng ([2002](https://arxiv.org/html/2602.14439v1#bib.bib80 "Determining the number of factors in approximate factor models")), and the adaptive sparse thresholding parameter is set to 0.5. (3)-(4) Mean-variance portfolio with (without) ESG level constraint (M-MV-Li / MV-Li), based on sample mean and linear shrinkage estimator of Ledoit and Wolf ([2004](https://arxiv.org/html/2602.14439v1#bib.bib46 "A well-conditioned estimator for large-dimensional covariance matrices")); (3) mean-variance portfolio with (without) ESG level constraint (M-MV-NL / MV-NL), based on sample mean and nonlinear shrinkage estimator of Ledoit and Wolf ([2017](https://arxiv.org/html/2602.14439v1#bib.bib65 "Nonlinear shrinkage of the covariance matrix for portfolio selection: Markowitz meets Goldilocks")). For the Q-MV strategy, we apply the same procedure for selecting η^∗​𝑸\hat{\eta}^{\*}{\bm{Q}} as that used for Re-MV.
For portfolios with ESG level constraint, we set the target ESG score to 0.8 and 0.9. The holding periods for all portfolios are set to one month, corresponding to Th​o​l​d=1T\_{hold}=1.

For evaluating measures, we report the results for OOS SR, OOS average ESG score, the 25th percentile of OOS ESG scores, and the standard deviation of OOS ESG score, defined as follows, respectively:

|  |  |  |
| --- | --- | --- |
|  | SR=1𝕋​∑t=1𝕋rp,t1𝕋−1​∑t=1𝕋(rp,t−1𝕋​∑t=1𝕋rp,t)2,ESGL​Q=inf{x:1𝕋​∑t=1𝕋𝕀​(E​S​Gp,t≤x)>0.25}\displaystyle\text{SR}=\frac{\frac{1}{\mathbb{T}}\sum\_{t=1}^{\mathbb{T}}r\_{p,t}}{\sqrt{\frac{1}{\mathbb{T}-1}\sum\_{t=1}^{\mathbb{T}}\left(r\_{p,t}-\frac{1}{\mathbb{T}}\sum\_{t=1}^{\mathbb{T}}r\_{p,t}\right)^{2}}},\quad\text{ESG}\_{LQ}=\inf\left\{x:\frac{1}{\mathbb{T}}\sum\_{t=1}^{\mathbb{T}}\mathbb{I}(ESG\_{p,t}\leq x)>0.25\right\} |  |
|  |  |  |
| --- | --- | --- |
|  | ESGM=1𝕋​∑t=1𝕋E​S​Gp,t,SDe​s​g=1𝕋−1​∑t=1𝕋(E​S​Gp,t−1𝕋​∑t=1𝕋E​S​Gp,t)2,\displaystyle\text{ESG}\_{M}=\frac{1}{\mathbb{T}}\sum\_{t=1}^{\mathbb{T}}ESG\_{p,t},\quad\text{SD}\_{esg}=\sqrt{\frac{1}{\mathbb{T}-1}\sum\_{t=1}^{\mathbb{T}}\left(ESG\_{p,t}-\frac{1}{\mathbb{T}}\sum\_{t=1}^{\mathbb{T}}ESG\_{p,t}\right)^{2}}, |  |

where 𝕋\mathbb{T} is the number of out-of-sample observations, rp,t=w^⊤​rtr\_{p,t}=\widehat{w}^{\top}r\_{t} is the OOS portfolio excess return, w^\widehat{w} is estimated portfolio and rtr\_{t} is the OOS excess assets return vector, E​S​Gp,t=w^⊤​E​S​Gt/∑i=1pw^iESG\_{p,t}=\widehat{w}^{\top}ESG\_{t}/\sum\_{i=1}^{p}\widehat{w}\_{i} is the standardized ESG score, E​S​GtESG\_{t} is the OOS assets’ ESG scores.

In practical applications, transaction costs play a crucial role for investors. Following DeMiguel et al. ([2009b](https://arxiv.org/html/2602.14439v1#bib.bib28 "Optimal versus naive diversification: How inefficient is the /1N portfolio strategy?")); Ao et al. ([2019](https://arxiv.org/html/2602.14439v1#bib.bib55 "Approaching mean-variance efficiency for large portfolios")) and Fan et al. ([2024b](https://arxiv.org/html/2602.14439v1#bib.bib129 "Time-varying minimum variance portfolio")), the excess portfolio return net of transaction cost is computed as,

|  |  |  |  |
| --- | --- | --- | --- |
|  | rpl,net=(1−∑i=1pc​|w^l+1,i−w^l,i+|)​(1+rpl)−1,r\_{p}^{l,\text{net}}=\left(1-\sum\_{i=1}^{p}c\left|\widehat{w}\_{l+1,i}-\widehat{w}\_{l,i}^{+}\right|\right)(1+r\_{p}^{l})-1, |  | (5.1) |

where rplr\_{p}^{l} is the excess return of the portfolio without transaction cost at the time of the llth rebalancing, w^l+1\widehat{w}\_{l+1} is the estimated portfolio weight at (l+1)t​h(l+1)^{th} rebalancing, and w^l+\widehat{w}\_{l}^{+} represents the portfolio weight before the (l+1)t​h(l+1)^{th} rebalancing.101010The definition of w^l+\widehat{w}\_{l}^{+} can be found, e.g., DeMiguel et al. ([2009b](https://arxiv.org/html/2602.14439v1#bib.bib28 "Optimal versus naive diversification: How inefficient is the /1N portfolio strategy?")) and Kan et al. ([2022](https://arxiv.org/html/2602.14439v1#bib.bib51 "Optimal portfolio choice with estimation risk: no risk-free asset case")). The parameter cc controls the level of the transaction cost, and in this study, it is set to 10 basis points following Ao et al. ([2019](https://arxiv.org/html/2602.14439v1#bib.bib55 "Approaching mean-variance efficiency for large portfolios")), Ke et al. ([2019](https://arxiv.org/html/2602.14439v1#bib.bib47 "Predicting returns with text data")), Li et al. ([2022a](https://arxiv.org/html/2602.14439v1#bib.bib143 "A synthetic regression model for large portfolio allocation")), and Wu et al. ([2025](https://arxiv.org/html/2602.14439v1#bib.bib13 "Making distributionally robust portfolios feasible in high dimension")). The Sharpe ratios considering transaction costs reported in the following tables are labeled as SRt​c\text{SR}\_{tc}. Furthermore, we also report the portfolio turnover rate for each strategy, which is defined as

|  |  |  |
| --- | --- | --- |
|  | TO=∑l=1R​T∑i=1p|w^l+1,i−w^l,i+|/R​T,\text{TO}=\sum\_{l=1}^{RT}\sum\_{i=1}^{p}|\widehat{w}\_{l+1,i}-\widehat{w}\_{l,i}^{+}|/RT, |  |

where R​TRT is the number of rebalancing.

### 5.3 Results

Table 4: Empirical results when assets pool consists of largest 60 stocks in S&P 500 index. Sample size is 9090. Out of sample period is from 06/2017 to 12/2024.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | SR | SRtc | ESGM | ESGLQ | SDesg | TO |
|  | s¯=0.9{\bar{s}}=0.9 | | | | | |
| Re-MV | 0.243 | 0.234 | 0.915 | 0.899 | 0.024 | 0.435 |
| M-MV-S | 0.174 | 0.127 | 0.936 | 0.803 | 0.178 | 592.475 |
| M-MV-POET | 0.177 | 0.171 | 0.887 | 0.874 | 0.021 | 0.490 |
| M-MV-Linear | 0.273 | 0.248 | 0.943 | 0.882 | 0.072 | 12.780 |
| M-MV-Nonlinear | 0.254 | 0.235 | 0.944 | 0.903 | 0.068 | 9.410 |
|  | s¯=0.8{\bar{s}}=0.8 | | | | | |
| Re-MV | 0.240 | 0.233 | 0.825 | 0.807 | 0.021 | 0.446 |
| M-MV-S | 0.193 | 0.134 | 0.841 | 0.724 | 0.150 | 303.992 |
| M-MV-POET | 0.177 | 0.171 | 0.887 | 0.874 | 0.021 | 0.490 |
| M-MV-Linear | 0.301 | 0.276 | 0.855 | 0.806 | 0.060 | 12.843 |
| M-MV-Nonlinear | 0.281 | 0.262 | 0.856 | 0.827 | 0.055 | 9.359 |
|  | Unconstrained Portfolio | | | | | |
| 1/N | 0.227 | 0.226 | 0.741 | 0.741 | 0.010 | 0.048 |
| Sample | 0.205 | 0.154 | 0.693 | 0.583 | 0.135 | 257.467 |
| Q-MV | 0.317 | 0.304 | 0.707 | 0.662 | 0.083 | 0.435 |
| MV-POET | 0.216 | 0.212 | 0.766 | 0.756 | 0.022 | 0.393 |
| MV-Linear | 0.343 | 0.318 | 0.697 | 0.654 | 0.085 | 13.315 |
| MV-Nonlinear | 0.314 | 0.295 | 0.709 | 0.662 | 0.082 | 9.668 |




Table 5: Empirical results when assets pool consists of largest 180 stocks in S&P 500 index. Sample size is 9090. Out of sample period is from 06/2017 to 12/2024.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | SR | SRtc | ESGM | ESGLQ | SDesg | TO |
|  | s¯=0.9{\bar{s}}=0.9 | | | | | |
| Re-MV | 0.197 | 0.188 | 0.903 | 0.890 | 0.020 | 1.151 |
| M-MV-S | - | - | - | - | - | - |
| M-MV-POET | -0.088 | -0.099 | 0.889 | 0.873 | 0.045 | 6.800 |
| M-MV-Linear | 0.217 | 0.169 | 0.881 | 0.839 | 0.065 | 825.261 |
| M-MV-Nonlinear | 0.192 | 0.164 | 0.894 | 0.872 | 0.050 | 83.744 |
|  | s¯=0.8{\bar{s}}=0.8 | | | | | |
| Re-MV | 0.216 | 0.208 | 0.819 | 0.806 | 0.017 | 1.164 |
| M-MV-S | - | - | - | - | - | - |
| M-MV-POET | -0.088 | -0.099 | 0.889 | 0.873 | 0.045 | 6.800 |
| M-MV-Linear | 0.234 | 0.191 | 0.803 | 0.761 | 0.059 | 323.868 |
| M-MV-Nonlinear | 0.206 | 0.179 | 0.814 | 0.792 | 0.044 | 97.793 |
|  | Unconstrained Portfolio | | | | | |
| 1/N | 0.203 | 0.202 | 0.685 | 0.678 | 0.011 | 0.049 |
| Sample | - | - | - | - | - | - |
| Q-MV | 0.244 | 0.226 | 0.551 | 0.521 | 0.047 | 1.182 |
| MV-POET | 0.191 | 0.173 | 0.680 | 0.671 | 0.028 | 1.350 |
| MV-Linear | 0.278 | 0.239 | 0.544 | 0.504 | 0.061 | 149.910 |
| MV-Nonlinear | 0.241 | 0.214 | 0.554 | 0.522 | 0.045 | 97.470 |

The empirical results are shown in Tables [4](https://arxiv.org/html/2602.14439v1#S5.T4 "Table 4 ‣ 5.3 Results ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio")-[7](https://arxiv.org/html/2602.14439v1#S5.T7 "Table 7 ‣ 5.3 Results ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio"). First, it can be observed that the newly proposed Re-MV portfolio, using η^∗​𝑸\widehat{\eta}^{\*}{\bm{Q}} that yields the highest estimated Sharpe ratio, attains the top-ranked OOS SR, both with and without transaction costs, among all ESG-constrained portfolios. For example, in the case of the largest p=180p=180 stocks with target level s¯=0.9{\bar{s}}=0.9 and transaction costs, the SR of Re-MV is 0.188, which is the highest among all ESG-constrained portfolios.
More importantly, compared with the naive M-MV-S strategy, the newly proposed Re-MV outperforms it economically in all cases without sacrificing the ESG target, demonstrating the advantage of the new portfolio. We note that, in some cases, M-MV-Li achieves high SR. However, this strategy is in fact unstable, as indicated by its high turnover rate. Our unreported results further show that its OOS returns are highly volatile.

Table 6: Empirical results when assets pool consists of randomly selected 60 stocks in S&P 500 index. Sample size is 90. Out of sample period is from 06/2017 to 12/2024.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | SR | SRtc | ESGM | ESGLQ | SDesg | TO |
|  | s¯=0.9{\bar{s}}=0.9 | | | | | |
| Re-MV | 0.206 | 0.196 | 0.899 | 0.870 | 0.044 | 0.339 |
| M-MV-S | 0.071 | 0.026 | 0.799 | 0.647 | 0.193 | 349.939 |
| M-MV-POET | -0.001 | -0.006 | 0.860 | 0.836 | 0.030 | 0.280 |
| M-MV-Linear | 0.177 | 0.155 | 0.883 | 0.852 | 0.041 | 7.841 |
| M-MV-Nonlinear | 0.170 | 0.150 | 0.893 | 0.872 | 0.039 | 6.033 |
|  | s¯=0.8{\bar{s}}=0.8 | | | | | |
| Re-MV | 0.218 | 0.209 | 0.823 | 0.797 | 0.032 | 0.339 |
| M-MV-S | 0.080 | 0.031 | 0.749 | 0.622 | 0.175 | 263.183 |
| M-MV-POET | -0.001 | -0.006 | 0.860 | 0.836 | 0.030 | 0.280 |
| M-MV-Linear | 0.192 | 0.170 | 0.814 | 0.798 | 0.029 | 7.958 |
| M-MV-Nonlinear | 0.191 | 0.171 | 0.822 | 0.809 | 0.029 | 6.109 |
|  | Unconstrained Portfolio | | | | | |
| 1/N | 0.182 | 0.181 | 0.181 | 0.029 | 0.055 | 0.055 |
| Sample | 0.084 | 0.036 | 0.560 | 0.188 | 359.352 | 359.352 |
| Q-MV | 0.209 | 0.196 | 0.691 | 0.027 | 0.337 | 0.337 |
| MV-POET | 0.054 | 0.050 | 0.627 | 0.028 | 0.192 | 0.192 |
| MV-Linear | 0.205 | 0.184 | 0.688 | 0.026 | 8.056 | 8.056 |
| MV-Nonlinear | 0.209 | 0.190 | 0.690 | 0.028 | 6.197 | 6.197 |




Table 7: Empirical results when assets pool consists of randomly selected 180 stocks in S&P 500 index. Sample size is 90. Out of sample period is from 06/2017 to 12/2024.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | SR | SRtc | ESGM | ESGLQ | SDesg | TO |
|  | s¯=0.9{\bar{s}}=0.9 | | | | | |
| Re-MV | 0.185 | 0.176 | 0.895 | 0.890 | 0.037 | 1.018 |
| M-MV-S | - | - | - | - | - | - |
| M-MV-POET | 0.170 | 0.154 | 0.892 | 0.860 | 0.040 | 0.802 |
| M-MV-Linear | 0.187 | 0.160 | 0.860 | 0.832 | 0.051 | 68.534 |
| M-MV-Nonlinear | 0.184 | 0.159 | 0.815 | 0.770 | 0.082 | 45.729 |
|  | s¯=0.8{\bar{s}}=0.8 | | | | | |
| Re-MV | 0.209 | 0.201 | 0.793 | 0.773 | 0.028 | 1.017 |
| M-MV-S | - | - | - | - | - | - |
| M-MV-POET | 0.170 | 0.154 | 0.892 | 0.860 | 0.040 | 0.802 |
| M-MV-Linear | 0.198 | 0.174 | 0.793 | 0.770 | 0.036 | 85.604 |
| M-MV-Nonlinear | 0.199 | 0.174 | 0.749 | 0.719 | 0.065 | 44.631 |
|  | Unconstrained Portfolio | | | | | |
| 1/N | 0.203 | 0.202 | 0.202 | 0.202 | 0.022 | 0.058 |
| Sample | - | - | - | - | - | - |
| Q-MV | 0.236 | 0.221 | 0.529 | 0.448 | 0.091 | 1.013 |
| MV-POET | 0.177 | 0.166 | 0.641 | 0.620 | 0.027 | 0.594 |
| MV-Linear | 0.231 | 0.209 | 0.613 | 0.597 | 0.036 | 123.699 |
| MV-Nonlinear | 0.239 | 0.212 | 0.534 | 0.458 | 0.089 | 41.629 |

Second, in terms of ESG measures, all ESG-constrained strategies achieve OOS ESG scores close to the prespecified threshold, and the proposed portfolio satisfies this threshold best overall. For example, in the case of the largest p=180p=180 stocks with target level s¯=0.9{\bar{s}}=0.9, the average OOS ESG score of Re-MV is 0.903, while the second-closest (to target) ESG score is achieved by M-MV-Nonlinear at 0.894. Furthermore, the OOS ESG scores of Re-MV exhibit low variability. On the one hand, the lower 25th percentile of the OOS ESG scores remains close to the target level, indicating that the OOS portfolio ESG scores stay near the target in most periods; In contrast, the lower 25th percentile of ESG score for other constrained portfolios (particularly M-MV-Linear) shows a substantial larger deviation from the target level.
On the other hand, the standard deviation of ESG score of Re-MV is either the lowest or very close to the lowest among all competing strategies.
As a result, our regularized ESG-constrained portfolio stably achieves a sustainable ESG level while maintaining a high Sharpe ratio. Additionally, we can observe that the proposed Re-MV exhibits a low turnover rate. For example, in the case of the largest p=60p=60 stocks, the Re-MV strategy exhibits a turnover rate of 1.151, which is the second lowest among the considered strategies. The lowest turnover rate is achieved by the equal weighting strategy. As a result, when transaction costs are taken into account (or play more important role), the superiority of the Re-MV strategy becomes more pronounced. Lastly, compared with the corresponding unconstrained strategies, imposing an ESG-level constraint generally reduces Sharpe ratio performance while improving ESG performance. A tighter constraint (with s¯{\bar{s}} increasing from 0.8 to 0.9) leads to a larger decrease in OOS SR. However, it is worth noting that, compared to Q-MV, the proposed Re-MV can possibly achieve a higher Sharpe ratio, as indicated by the results in Lemma [1](https://arxiv.org/html/2602.14439v1#Thmlemma1 "Lemma 1. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio") and Remark [5](https://arxiv.org/html/2602.14439v1#Thmremark5 "Remark 5. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio"). This theoretical insight is further supported by our empirical results with randomly selected assets. As reported in Table [6](https://arxiv.org/html/2602.14439v1#S5.T6 "Table 6 ‣ 5.3 Results ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio"), when s¯=0.8{\bar{s}}=0.8 without transaction costs, the SR of Re-MV is 0.218, which exceeds the corresponding value of 0.209 for Q-MV.

## 6 Conclusion

This paper studies a regularized ESG-constrained mean-variance (MV) portfolio optimization in large-dimensional situation. We first quantify the impact of imposing an ESG-level constraint, as well as the estimation error arising from the sample mean estimation of the ESG score mean level, by deriving the limiting OOS Sharpe ratio of the proposed portfolio. Then, we further propose an estimator for OOS SR such that we can evaluate the impacts of various specification of regularization matrix based on historical data. The theoretical consistency is also provided.

Simulation results show that the proposed estimators perform close to the corresponding unknown oracle counterparts. Moreover, we numerically investigate the impact of various forms of regularization matrices on the OOS SR, which provides useful guidance for practical implementation.
Finally, based on OOS SR estimator, we propose an adaptive regularized portfolio which uses the best regularization matrix yielding the highest estimated SR (among a set of candidates) at each decision node.
Empirical evidence based on the S&P 500 index demonstrates that the proposed adaptive ESG-constrained portfolio achieves a high OOS SR while satisfying the required ESG level. Overall, this study provides a statistically rigorous and practically effective solution for integrating sustainability into high-dimensional portfolio allocation.

## References

* M. Ao, L. Chen, Y. Li, and X. Zheng (2025)
  Robust large portfolio optimization with heteroscedastic and heavy-tailed returns.
  Technical report
   SSRN.
  Note: URL: http://dx.doi.org/10.2139/ssrn.5197964
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p3.3 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§1](https://arxiv.org/html/2602.14439v1#S1.p9.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* M. Ao, Y. Li, and X. Zheng (2019)
  Approaching mean-variance efficiency for large portfolios.
  The Review of Financial Studies 32 (7),  pp. 2890–2919.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p3.3 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§1](https://arxiv.org/html/2602.14439v1#S1.p9.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§2](https://arxiv.org/html/2602.14439v1#S2.p2.8 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§3](https://arxiv.org/html/2602.14439v1#S3.p12.18 "3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.1](https://arxiv.org/html/2602.14439v1#S5.SS1.p1.1 "5.1 Data ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p4.10 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p4.8 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* J. Bai and S. Ng (2002)
  Determining the number of factors in approximate factor models.
  Econometrica 70 (1),  pp. 191–221.
  Cited by: [§4.3](https://arxiv.org/html/2602.14439v1#S4.SS3.p2.18 "4.3 The Choices of Regularization Matrix ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p2.2 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [footnote 4](https://arxiv.org/html/2602.14439v1#footnote4 "In 4.1 Basic Setup ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* B. M. Barber, A. Morse, and A. Yasuda (2021)
  Impact investing.
  Journal of Financial Economics 139 (1),  pp. 162–185.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p2.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* F. Berg, A. W. Lo, R. Rigobon, M. Singh, and R. Zhang (2024)
  Quantifying the returns of esg investing: an empirical analysis with six esg metrics..
  Journal of Portfolio Management 50 (8).
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p2.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* J. Blanchet, L. Chen, and X. Y. Zhou (2022)
  Distributionally robust mean-variance portfolio selection with Wasserstein distances.
  Management Science 68 (9),  pp. 6382–6410.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p9.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* O. Bodnar, T. Bodnar, and N. Parolya (2022a)
  Recent advances in shrinkage-based high-dimensional inference.
  Journal of Multivariate Analysis 188,  pp. 104826.
  Cited by: [§3](https://arxiv.org/html/2602.14439v1#S3.p3.7 "3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* T. Bodnar, O. Okhrin, and N. Parolya (2019)
  Optimal shrinkage estimator for high-dimensional mean vector.
  Journal of Multivariate Analysis 170,  pp. 63–79.
  Cited by: [§2](https://arxiv.org/html/2602.14439v1#S2.p2.8 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* T. Bodnar, Y. Okhrin, and N. Parolya (2022b)
  Optimal shrinkage-based portfolio selection in high dimensions.
  Journal of Business & Economic Statistics 41 (1),  pp. 140–156.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p3.3 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§2](https://arxiv.org/html/2602.14439v1#S2.p2.8 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* T. Bodnar, N. Parolya, and E. Thorsén (2024)
  Two is better than one: regularized shrinkage of large minimum variance portfolios.
  Journal of Machine Learning Research 25 (173),  pp. 1–32.
  Cited by: [§3](https://arxiv.org/html/2602.14439v1#S3.p3.7 "3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* T. Cai and W. Liu (2011)
  Adaptive thresholding for sparse covariance matrix estimation.
  Journal of the American Statistical Association: Theory and Methods 106 (494),  pp. 672–684.
  Cited by: [footnote 4](https://arxiv.org/html/2602.14439v1#footnote4 "In 4.1 Basic Setup ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* F. Cesarone, M. L. Martino, and A. Carleo (2022)
  Does esg impact really enhance portfolio profitability?.
  Sustainability 14 (4),  pp. 2050.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p2.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* Z. Chen, Y. Ding, Y. Li, and X. Zheng (2025)
  Cross-sectional learning and inference for the stochastic discount factor.
  Technical report
   SSRN.
  Note: URL: <http://dx.doi.org/10.2139/ssrn.5391303>
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p9.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* J. De Spiegeleer, S. Höcht, D. Jakubowski, S. Reyners, and W. Schoutens (2023)
  ESG: a new dimension in portfolio allocation.
  Journal of Sustainable Finance & Investment 13 (2),  pp. 827–867.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p2.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§1](https://arxiv.org/html/2602.14439v1#S1.p8.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* V. DeMiguel, L. Garlappi, F. J. Nogales, and R. Uppal (2009a)
  A generalized approach to portfolio optimization: improving performance by constraining portfolio norms.
  Management Science 55 (5),  pp. 798–812.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p9.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§2](https://arxiv.org/html/2602.14439v1#S2.p2.8 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [Remark 1](https://arxiv.org/html/2602.14439v1#Thmremark1.p1.8.8 "Remark 1. ‣ 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* V. DeMiguel, L. Garlappi, and R. Uppal (2009b)
  Optimal versus naive diversification: How inefficient is the 1/N{1/N} portfolio strategy?.
  The Review of Financial Studies 22 (5),  pp. 1915–1953.
  Cited by: [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p4.10 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [footnote 10](https://arxiv.org/html/2602.14439v1#footnote10 "In 5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* Y. Ding, Y. Li, and X. Zheng (2021)
  High dimensional minimum variance portfolio estimation under statistical factor models.
  Journal of Econometrics 222 (1B),  pp. 502–515.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p3.3 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§1](https://arxiv.org/html/2602.14439v1#S1.p9.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§3](https://arxiv.org/html/2602.14439v1#S3.p6.8 "3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* N. El Karoui (2010)
  High-dimensionality effects in the markowitz problem and other quadratic programs with linear constraints: risk underestimation.
  The Annals of Statistics 38 (6),  pp. 3487 – 3566.
  Cited by: [§3](https://arxiv.org/html/2602.14439v1#S3.p3.7 "3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* J. Fan, Y. Liao, and M. Mincheva (2013)
  Large covariance estimation by thresholding principal orthogonal complements.
  Journal of the Royal Statistical Society: Series B (Statistical Methodology) 75 (4),  pp. 603–680.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p9.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§4.1](https://arxiv.org/html/2602.14439v1#S4.SS1.p1.11 "4.1 Basic Setup ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§4.3](https://arxiv.org/html/2602.14439v1#S4.SS3.p2.18 "4.3 The Choices of Regularization Matrix ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p2.2 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [footnote 4](https://arxiv.org/html/2602.14439v1#footnote4 "In 4.1 Basic Setup ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* Q. Fan, M. C. Medeiros, H. Yang, and S. Yang (2024a)
  Cost-aware portfolios in a large universe of assets.
  arXiv preprint arXiv:2412.11575.
  Cited by: [Remark 3](https://arxiv.org/html/2602.14439v1#Thmremark3.p1.3.3 "Remark 3. ‣ 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* Q. Fan, R. Wu, Y. Yang, and W. Zhong (2024b)
  Time-varying minimum variance portfolio.
  Journal of Econometrics 239,  pp. 105339.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p3.3 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§1](https://arxiv.org/html/2602.14439v1#S1.p9.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.1](https://arxiv.org/html/2602.14439v1#S5.SS1.p1.1 "5.1 Data ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p4.10 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* S. M. Gasser, M. Rammerstorfer, and K. Weinmayer (2017)
  Markowitz revisited: social portfolio engineering.
  European Journal of Operational Research 258 (3),  pp. 1181–1190.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p8.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* N. Hautsch and S. Voigt (2019)
  Large-scale portfolio allocation under transaction costs and model uncertainty.
  Journal of Econometrics 212 (1),  pp. 221–240.
  Cited by: [Remark 3](https://arxiv.org/html/2602.14439v1#Thmremark3.p1.3.3 "Remark 3. ‣ 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* Y. Hu, W. B. Lindquist, and S. T. Rachev (2025)
  Sustainability-valued discrete option pricing in complete markets.
  Journal of Sustainable Finance & Investment 15 (2),  pp. 403–437.
  Cited by: [Remark 2](https://arxiv.org/html/2602.14439v1#Thmremark2.p1.15.15 "Remark 2. ‣ 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* R. Jagannathan and T. Ma (2003)
  Risk reduction in large portfolios: why imposing the wrong constraints helps.
  The Journal of Finance 58 (4),  pp. 1651–1683.
  Cited by: [§2](https://arxiv.org/html/2602.14439v1#S2.p2.8 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* R. Kan, X. Wang, and X. Zheng (2024)
  In-sample and out-of-sample sharpe ratios of multi-factor asset pricing models.
  Journal of Financial Economics 155,  pp. 103837.
  Cited by: [§3](https://arxiv.org/html/2602.14439v1#S3.p12.18 "3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* R. Kan, X. Wang, and G. Zhou (2022)
  Optimal portfolio choice with estimation risk: no risk-free asset case.
  Management Science 68 (3),  pp. 2047–2068.
  Cited by: [footnote 10](https://arxiv.org/html/2602.14439v1#footnote10 "In 5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* R. Kan and G. Zhou (2007)
  Optimal portfolio choice with parameter uncertainty.
  Journal of Financial and Quantitative Analysis 42 (3),  pp. 621–656.
  Cited by: [§2](https://arxiv.org/html/2602.14439v1#S2.p2.8 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* Z. T. Ke, B. T. Kelly, and D. Xiu (2019)
  Predicting returns with text data.
  Technical report
   National Bureau of Economic Research.
  Cited by: [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p4.8 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* N. Lassance, A. Martín-Utrera, and M. Simaan (2024)
  The risk of expected utility under parameter uncertainty.
  Management Science 70 (11),  pp. 7644–7663.
  Cited by: [§2](https://arxiv.org/html/2602.14439v1#S2.p2.8 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* D. Lauria, W. B. Lindquist, S. Mittnik, and S. T. Rachev (2025)
  Environmental, social and governance-valued portfolio optimization and dynamic asset pricing.
  Journal of Risk and Financial Management 18 (3),  pp. 153.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p2.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§1](https://arxiv.org/html/2602.14439v1#S1.p8.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [Remark 2](https://arxiv.org/html/2602.14439v1#Thmremark2.p1.15.15 "Remark 2. ‣ 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* O. Ledoit and S. Péché (2011)
  Eigenvectors of some large sample covariance matrix ensembles.
  Probability Theory and Related Fields 151 (1),  pp. 233–264.
  Cited by: [§3](https://arxiv.org/html/2602.14439v1#S3.p2.1 "3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* O. Ledoit and M. Wolf (2003)
  Improved estimation of the covariance matrix of stock returns with an application to portfolio selection.
  Journal of Empirical Finance 10 (5),  pp. 603–621.
  Cited by: [§2](https://arxiv.org/html/2602.14439v1#S2.p2.8 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§4.3](https://arxiv.org/html/2602.14439v1#S4.SS3.p2.18 "4.3 The Choices of Regularization Matrix ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* O. Ledoit and M. Wolf (2004)
  A well-conditioned estimator for large-dimensional covariance matrices.
  Journal of Multivariate Analysis 88 (2),  pp. 365–411.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p8.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§4.2](https://arxiv.org/html/2602.14439v1#S4.SS2.p1.14 "4.2 Performance of SR estimator ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§4.3](https://arxiv.org/html/2602.14439v1#S4.SS3.p2.18 "4.3 The Choices of Regularization Matrix ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p2.2 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [Remark 1](https://arxiv.org/html/2602.14439v1#Thmremark1.p1.8.8 "Remark 1. ‣ 2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* O. Ledoit and M. Wolf (2017)
  Nonlinear shrinkage of the covariance matrix for portfolio selection: Markowitz meets Goldilocks.
  The Review of Financial Studies 30 (12),  pp. 4349–4388.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p5.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§3](https://arxiv.org/html/2602.14439v1#S3.p2.1 "3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§4.3](https://arxiv.org/html/2602.14439v1#S4.SS3.p2.18 "4.3 The Choices of Regularization Matrix ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p2.2 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* G. Li, L. Huang, J. Yang, and W. Zhang (2022a)
  A synthetic regression model for large portfolio allocation.
  Journal of Business & Economic Statistics 40 (4),  pp. 1665–1677.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p9.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p4.8 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* H. Li, Z. Bai, W. Wong, and M. McAleer (2022b)
  Spectrally-corrected estimation for high-dimensional markowitz mean-variance optimization.
  Econometrics and Statistics 24,  pp. 133–150.
  Cited by: [§3](https://arxiv.org/html/2602.14439v1#S3.p3.7 "3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* A. W. Lo and R. Zhang (2024)
  Quantifying the impact of impact investing.
  Management Science 70 (10),  pp. 7161–7186.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p2.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* A. W. Lo and R. Zhang (2025)
  Performance attribution for portfolio constraints.
  Management Science 71 (9),  pp. 7537–7559.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p2.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§1](https://arxiv.org/html/2602.14439v1#S1.p8.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* Y. Lu, Y. Yang, and T. Zhang (2024)
  Double descent in portfolio optimization: dance between theoretical sharpe ratio and estimation accuracy.
  arXiv preprint arXiv:2411.18830.
  Cited by: [§3](https://arxiv.org/html/2602.14439v1#S3.p2.1 "3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* C. Makridis and M. Simaan (2023)
  Balancing returns and responsibility: evidence from shrinkage-based portfolios.
  Available at SSRN 4597152.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p2.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§1](https://arxiv.org/html/2602.14439v1#S1.p8.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§2](https://arxiv.org/html/2602.14439v1#S2.p2.8 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§4.3](https://arxiv.org/html/2602.14439v1#S4.SS3.p5.34 "4.3 The Choices of Regularization Matrix ‣ 4 Simulation ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* H. Markowitz (1952)
  Portfolio selection.
  Journal of Finance 7 (1),  pp. 77–91.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p1.2 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* X. Meng, Y. Cao, and W. Wang (2025)
  Estimation of out-of-sample sharpe ratio for high dimensional portfolio optimization.
  Journal of the American Statistical Association 0 (0),  pp. 1–13.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p3.3 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§1](https://arxiv.org/html/2602.14439v1#S1.p9.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§2](https://arxiv.org/html/2602.14439v1#S2.p2.8 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [Remark 4](https://arxiv.org/html/2602.14439v1#Thmremark4.p1.14.9 "Remark 4. ‣ 3 Asymptotic Analysis ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* R. O. Michaud (1989)
  The Markowitz optimization enigma: is ‘optimized’optimal?.
  Financial Analysts Journal 45 (1),  pp. 31–42.
  Cited by: [§2](https://arxiv.org/html/2602.14439v1#S2.p2.8 "2 Regularized ESG-Constrained Problem ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* L. H. Pedersen, S. Fitzgibbons, and L. Pomorski (2021)
  Responsible investing: the esg-efficient frontier.
  Journal of Financial Economics 142 (2),  pp. 572–597.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p2.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§1](https://arxiv.org/html/2602.14439v1#S1.p8.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* A. B. Schmidt (2022)
  Optimal esg portfolios: an example for the dow jones index.
  Journal of Sustainable Finance & Investment 12 (2),  pp. 529–535.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p8.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* S. Utz, M. Wimmer, and R. E. Steuer (2015)
  Tri-criterion modeling for constructing more-sustainable mutual funds.
  European Journal of Operational Research 246 (1),  pp. 331–338.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p8.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio").
* R. Wu, Y. Yang, H. L. Shang, and H. Zhu (2025)
  Making distributionally robust portfolios feasible in high dimension.
  Journal of Econometrics 252,  pp. 106118.
  Cited by: [§1](https://arxiv.org/html/2602.14439v1#S1.p3.3 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§1](https://arxiv.org/html/2602.14439v1#S1.p9.1 "1 Introduction ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.1](https://arxiv.org/html/2602.14439v1#S5.SS1.p1.1 "5.1 Data ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p2.2 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio"),
  [§5.2](https://arxiv.org/html/2602.14439v1#S5.SS2.p4.8 "5.2 Portfolios and Measures ‣ 5 Empirical application ‣ Sustainable Investment: ESG Impacts on Large Portfolio").