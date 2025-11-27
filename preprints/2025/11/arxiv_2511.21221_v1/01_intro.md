---
authors:
- Kexin Wang
- Xiaomeng Zhang
- Xinyu Zhang
doc_id: arxiv:2511.21221v1
family_id: arxiv:2511.21221
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Portfolio Optimization via Transfer Learning
url_abs: http://arxiv.org/abs/2511.21221v1
url_html: https://arxiv.org/html/2511.21221v1
venue: arXiv q-fin
version: 1
year: 2025
---


###### Abstract

Recognizing that asset markets generally exhibit shared informational characteristics, we develop a portfolio strategy based on transfer learning that leverages cross-market information to enhance the investment performance in the market of interest by forward validation. Our strategy asymptotically identifies and utilizes the informative datasets, selectively incorporating valid information while discarding the misleading information. This enables our strategy to achieve the maximum Sharpe ratio asymptotically. The promising performance is demonstrated by numerical studies and case studies of two portfolios: one consisting of stocks dual-listed in A-shares and H-shares, and another comprising equities from various industries of the United States.

Finding optimal portfolio strategies is a fundamental challenge for investors.
When determining the portfolio strategies on a specific market or asset class that we are interested in,
the traditional strategies, such as the mean-variance portfolio theory proposed by r1 and its variants (r10; r3; r5; r6; r12; r4; r7; ledoit2017; ao2018; r16), are usually built up with the information solely on that specific market or asset class itself.
However, data specific to the market or asset class that we are interested in are often insufficient due to high volatility, structural breaks, and high-dimensional features, which can lead to suboptimal portfolio decisions. Moreover, when it comes to a emerging market or a newly thematic sector (e.g., ESG or crypto), its historical data is usually quite limited, making it more difficult to construct a reliable portfolio allocation.
Thus, this article is motivated to compensate for the insufficiency of the market dataset of interest.

In this paper, we address the insufficiency of the market dataset of interest by transferring information from other related market datasets, such as those where the same stocks are traded. We propose a new portfolio strategy based on transfer learning technology.
It possesses the asymptotic optimality in terms of maximizing the Sharpe ratio index in the large sample sense, which can balance the expected return of investors with the risk they are taking on; see r17 for a review of the development of the Sharpe ratio.

Transfer learning, a branch of machine learning, focuses on transferring related knowledge from source domains (e.g., other related market datasets) to a potentially different target domain (e.g., the market dataset of interest); see pan2010, zhuang2011 and koshiyama2022 for the literature review.
The transfer learning technology is feasible in portfolio optimization due to the fact that many markets across sectors, industries, and asset classes often display shared patterns and inter-dependencies driven by macroeconomic factors, supply chain dynamics, investor behavior and so on (see, e.g., buccheri2021; kelly2023; guo2025). For example, the analysis of the H-shares and A-shares benefits significantly from incorporating information from the other market. This utility stems from the fundamental commonality of cross-listed companies. Since the corresponding H-shares and A-shares represent ownership in the same entity, their intrinsic value drivers, such as profitability and operational risk, are closely linked. Consequently, price deviations in one market, often resulting from information asymmetry or local sentiment, can be identified through price movements in the other. This spillover effect of information provides critical incremental insights for accurate asset valuation, mispricing detection, and the development of more robust investment strategies.

To transfer knowledge from other related markets for the portfolio optimization in the market of interest,
cao2023ssrn developed a transfer learning technique, provided theoretical analyses of the transfer risk and applied it in three numerical experiments, including cross-continent transfer, cross-sector transfer and cross-frequency transfer.
However, they limited their strategy to transferring portfolio strategies from a single source dataset, rather than from multiple sources.
Although the proposed transfer risk in this research can serve as a prior to figure out the suitable source datasets, relying on only a single source dataset may yield inferior results compared to leveraging multiple sources collectively when these source datasets are regarded as having relatively low risk. Moreover, estimating this transfer risk still requires additional assumptions about the distributions of the source and target data, such as assuming multivariate normality. By contrast, our strategy allows information to be transferred from multiple source datasets simultaneously and offers corresponding theoretical foundations.

Except for cao2023ssrn, how to transfer information for portfolio construction remains relatively underexplored, although transfer learning has been widely adopted within the financial domain to improve precision and efficiency in areas such as asset pricing (r28; babi2023; lasse2024), default risk assessment (r29), and modeling industrial chain interactions (r30).
In the study of financial investment strategies, jeong2019 investigated trading system and involved transfer learning to handle the overfitting problem arising from small and highly volatile financial data. koshiyama2022 developed a fully end-to-end global trading architecture (QuantNet) based on transfer learning and meta-learning. By integrating diverse market data, QuantNet learns both market-agnostic trends and market-specific strategies by separating shared and specialized parameters, capturing general transferable dynamics and achieving superior returns. morstedt2024 focused on the
global minimum variance portfolio (r1) and proposed a nonlinear shrinkage estimator for covariance estimation that determines the shrinkage parameters using cross-validation-based transfer learning. Specifically, cross-validation-based transfer learning requires that the validation set is formed from a disjoint source dataset of assets, disjoint from the target dataset.

In this article, we directly transfer portfolio strategies across different source datasets and select the transferring weight vector by forward validation. In addition, we do not need to assume that markets share specific parameters or structural components, which allows our strategy to remain flexible and agnostic to the underlying similarity structure across markets.
We also provide three theoretical guarantees for our strategy. (i) Our strategy automatically excludes uninformative and misleading source datasets, asymptotically concentrating portfolio weights on the informative datasets,
in contrast to cao2023ssrn, which relies on pre-estimating transfer risk to choose the source dataset. (ii) Our portfolio strategy can asymptotically achieve the maximum attainable Sharpe ratio. (iii) The variance of the Sharpe ratio under our strategy is asymptotically lower than that of the N​o​n−t​r​a​n​s​f​e​rNon-transfer baseline strategy which only relies on the target dataset if there exists informative source dataset for the target market dataset.
If none of the source dataset is informative for the target, then the variance of the Sharpe ratio under our strategy is asymptotically equivalent to that of the N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy.

Our strategy is inspired by the optimal model averaging strategy (hansen2007), which is a frequentist model averaging technique aiming at optimally combine predictions or estimates from multiple candidate models; see enrique2015 for a review of the literature. More recently, hu2023 and zhang2024 have integrated the basic idea of optimal model averaging with transfer learning, introducing the concept of optimal transfer learning. However, both hu2023 and zhang2024 focused primarily on improving predictive accuracy and were not applicable for portfolio optimization. Hence, in this article, we adapt optimal transfer learning specifically for portfolio optimization.
Although our strategy is developed in the context of portfolio optimization, the central idea can be readily extended to other decision-making problems.

To validate the superiority of our strategy, we conduct numerical simulations and empirical applications focused on two scenarios: investing in stocks dual-listed in both H-shares and A-shares, and investing across different industries of the United States. Results confirm our theoretical conclusions that the inclusion of auxiliary datasets through transfer learning significantly enhances portfolio performance.

The remainder of this article is organized as follows. [Section 1](https://arxiv.org/html/2511.21221v1#S1 "1 Model framework ‣ Portfolio Optimization via Transfer Learning") presents the problem of interest and the model framework. [Section 2](https://arxiv.org/html/2511.21221v1#S2 "2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") establishes the asymptotic properties of our procedure. The performance of the proposed strategy is investigated via
numerical simulations in [Section 3](https://arxiv.org/html/2511.21221v1#S3 "3 Simulation studies ‣ Portfolio Optimization via Transfer Learning") and the empirical applications in [Section 4](https://arxiv.org/html/2511.21221v1#S4 "4 Applications ‣ Portfolio Optimization via Transfer Learning"). [Section 5](https://arxiv.org/html/2511.21221v1#S5 "5 Conclusion ‣ Portfolio Optimization via Transfer Learning") concludes the article with some discussion. All technical details including detailed proofs are provided in the Appendix.

## 1 Model framework

The concept of Sharpe ratio (S​R)(SR), also known as the Sharpe Index, was introduced by sharpe1966 to define a measure of the ratio of the return and the volatility. Its mathematical expression is

|  |  |  |
| --- | --- | --- |
|  | S​R=E⁡(rp)−rfσp,SR=\frac{\operatorname{E}(r\_{p})-r\_{f}}{\sigma\_{p}}, |  |

where E⁡(rp)\operatorname{E}(r\_{p}) represents the expected return of the portfolio, rfr\_{f} stands for risk-free asset and σp\sigma\_{p} is the standard deviation of the portfolio which is used to measure the overall risk of the portfolio. Obviously, Sharpe ratio not only focuses on the return of the assets, but also focuses on the risk of the assets.

Consider a capital market consisting of dd assets with the excess return vector 𝒓=(r1,…,rd)⊤\bm{r}=(r\_{1},\dots,r\_{d})^{\top}. If the corresponding asset allocation is ϕ=(ϕ1,…,ϕd)⊤\bm{\phi}=(\phi\_{1},\dots,\phi\_{d})^{\top}, the payoff is ϕ⊤​𝒓\bm{\phi}^{\top}\bm{r}. Denote the mean vector of the excess return as 𝝁\bm{\mu}, the covariance matrix as 𝚺\bm{\Sigma} and Φ={ϕ∈[0,1]d|∑i=1dϕi=1}\Phi=\{\bm{\phi}\in[0,1]^{d}|\ \sum\_{i=1}^{d}\phi\_{i}=1\}. The optimal portfolio problem is to find the maximum Sharpe ratio by solving the following optimization problem.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕo=arg⁡maxϕ∈Φ​E⁡(ϕ⊤​𝒓)Var⁡(ϕ⊤​𝒓)=arg⁡maxϕ∈Φ​𝝁⊤​ϕϕ⊤​𝚺​ϕ,\bm{\phi}\_{o}=\underset{\bm{\phi}\in\Phi}{\arg\max}\frac{\operatorname{E}\left(\bm{\phi}^{\top}\bm{r}\right)}{\sqrt{\operatorname{Var}\left(\bm{\phi}^{\top}\bm{r}\right)}}=\underset{\bm{\phi}\in\Phi}{\arg\max}\frac{\bm{\mu}^{\top}\bm{\phi}}{\sqrt{\bm{\phi}^{\top}\bm{\Sigma}\bm{\phi}}}, |  | (1) |

where ϕo\bm{\phi}\_{o} represents the optimal portfolio allocation that maximizes the Sharpe ratio.

Since there may exist other available assets which provide useful information when investing in the target assets, we want to make full use of the possible effective information to invest in the target assets. Assume that there are MM available source datasets, and denote the target data as TT and the source data as {Sm|m=1,…,M}\{S\_{m}|\ m=1,\dots,M\}, respectively. We treat MM as fixed and allow dd to diverge. The sample sizes of the target data TT and the source data SmS\_{m} are N0N\_{0} and NmN\_{m}, respectively. Let N~=min​{N0,…,NM}\widetilde{N}=\text{min}\{N\_{0},\dots,N\_{M}\}. For simplicity, denote the excess return of the target assets as {𝒓0,t∈Rd|t=−(N0−N~−1),…,N~}\{\bm{r}\_{0,t}\in\text{R}^{d}|\ t=-(N\_{0}-\widetilde{N}-1),\dots,\widetilde{N}\} and the excess return of the source assets as {𝒓m,t∈Rd|m=1,…,M,t=−(Nm−N~−1),…,N~}\{\bm{r}\_{m,t}\in\text{R}^{d}|\ m=1,\dots,M,\ t=-(N\_{m}-\widetilde{N}-1),\dots,\widetilde{N}\}, respectively. For m=0,1,…,Mm=0,1,\dots,M and t=−(Nm−N~−1),…,N~t=-(N\_{m}-\widetilde{N}-1),\dots,\widetilde{N}, denote the mean vector of the excess return 𝒓m,t\bm{r}\_{m,t} as 𝝁m,t\bm{\mu}\_{m,t} and the covariance matrix of the excess return 𝒓m,t\bm{r}\_{m,t} as 𝚺m,t\bm{\Sigma}\_{m,t}. Under these true parameters, the optimal asset allocation, denoted as ϕm,t\bm{\phi}\_{m,t}, can be derived using ([2](https://arxiv.org/html/2511.21221v1#S1.Ex3 "Equation 2 ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕm,t=arg⁡maxϕ∈Φ​𝝁m,t⊤​ϕϕ⊤​𝚺m,t​ϕ.\bm{\phi}\_{m,t}=\underset{\bm{\phi}\in\Phi}{\arg\max}\frac{\bm{\mu}\_{m,t}^{\top}\bm{\phi}}{\sqrt{\bm{\phi}^{\top}\bm{\Sigma}\_{m,t}\bm{\phi}}}. |  | (2) |

However, we never know these parameters in practice. Empirically, 𝝁m,t\bm{\mu}\_{m,t} and 𝚺m,t\bm{\Sigma}\_{m,t} are estimated from the historical return. For m=0,1,…,M,t=2,…,N~m=0,1,\dots,M,\ t=2,\dots,\widetilde{N}, we use the historical sample mean and historical sample covariance to estimate. That is, the estimators 𝝁^m,t\widehat{\bm{\mu}}\_{m,t} and 𝚺^m,t\widehat{\bm{\Sigma}}\_{m,t} for 𝝁m,t\bm{\mu}\_{m,t} and 𝚺m,t\bm{\Sigma}\_{m,t} can be calculated using

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝁^m,t=1t−1+Nm−N~​∑j=−(Nm−N~−1)t−1𝒓m,j\widehat{\bm{\mu}}\_{m,t}=\frac{1}{t-1+N\_{m}-\widetilde{N}}\sum\_{j=-(N\_{m}-\widetilde{N}-1)}^{t-1}\bm{r}\_{m,j} |  | (3) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺^m,t=1t−2+Nm−N~​∑j=−(Nm−N~−1)t−1(𝒓m,j−𝝁^m,t)​(𝒓m,j−𝝁^m,t)⊤,\widehat{\bm{\Sigma}}\_{m,t}=\frac{1}{t-2+N\_{m}-\widetilde{N}}\sum\_{j=-(N\_{m}-\widetilde{N}-1)}^{t-1}(\bm{r}\_{m,j}-\widehat{\bm{\mu}}\_{m,t})(\bm{r}\_{m,j}-\widehat{\bm{\mu}}\_{m,t})^{\top}, |  | (4) |

respectively. Given 𝝁^m,t\widehat{\bm{\mu}}\_{m,t} and 𝚺^m,t\widehat{\bm{\Sigma}}\_{m,t}, the optimal investment strategy can be estimated.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^m,t=arg⁡maxϕ∈Φ​𝝁^m,t⊤​ϕϕ⊤​𝚺^m,t​ϕ.\widehat{\bm{\phi}}\_{m,t}=\underset{\bm{\phi}\in\Phi}{\arg\max}\frac{\widehat{\bm{\mu}}\_{m,t}^{\top}\bm{\phi}}{\sqrt{\bm{\phi}^{\top}\widehat{\bm{\Sigma}}\_{m,t}\bm{\phi}}}. |  | (5) |

Denote the set 𝒲={𝒘∈[0,1]M+1|∑m=0Mwm=1}\mathcal{W}=\{\bm{w}\in[0,1]^{M+1}|\ \sum\_{m=0}^{M}\ w\_{m}=1\} and the weight vector 𝒘=(w0,w1,…,wM)⊤\bm{w}=(w\_{0},w\_{1},\dots,w\_{M})^{\top}. Define the weighted allocation of the target data at time tt as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^t​(𝒘)=∑m=0Mwm​ϕ^m,t.\widehat{\bm{\phi}}\_{t}(\bm{w})=\sum\_{m=0}^{M}w\_{m}\widehat{\bm{\phi}}\_{m,t}. |  | (6) |

As specified in ([6](https://arxiv.org/html/2511.21221v1#S1.Ex7 "Equation 6 ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning")), the proposed estimator combines optimal portfolio estimators from multiple source datasets at time tt through a weighted integration scheme, where the weight vector 𝒘\bm{w} facilitates efficient information transfer across domains.

### 1.1 A motivation example

To demonstrate the advantages of incorporating source assets, we construct a simplified example where all datasets span N~\widetilde{N} identical time periods. For analytical tractability, we assume that the excess returns {𝒓m,t|t=1,…,N~}\{\bm{r}\_{m,t}|\ t=1,\dots,\widetilde{N}\} are independently and identically distributed both across different datasets and within each individual dataset across tt. For each dataset, calculate 𝝁^m,N~+1\widehat{\bm{\mu}}\_{m,\widetilde{N}+1} and 𝚺^m,N~+1\widehat{\bm{\Sigma}}\_{m,\widetilde{N}+1} according to ([3](https://arxiv.org/html/2511.21221v1#S1.Ex4 "Equation 3 ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning")) and ([4](https://arxiv.org/html/2511.21221v1#S1.Ex5 "Equation 4 ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning")), respectively. Thus, applying ([5](https://arxiv.org/html/2511.21221v1#S1.Ex6 "Equation 5 ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning")), we can obtain ϕ^0,N~+1\widehat{\bm{\phi}}\_{0,\widetilde{N}+1} for the target assets TT and {ϕ^m,N~+1|m=1,…,M}\{\widehat{\bm{\phi}}\_{m,\widetilde{N}+1}|\ m=1,\dots,M\} for the source assets {Sm|m=1,…,M}\{S\_{m}|\ m=1,\dots,M\}, respectively. Denote ϕ^N~+1e​q​u​a​l\widehat{\bm{\phi}}^{equal}\_{\widetilde{N}+1} as the equal weighted allocation ∑m=0Mϕ^m,N~+1/(M+1)\sum\_{m=0}^{M}\widehat{\bm{\phi}}\_{m,\widetilde{N}+1}/(M+1). A direct performance comparison is made through Sharpe ratio S​R~0,N~+1\widetilde{SR}\_{0,\widetilde{N}+1} and S​R~0,N~+1e​q​u​a​l\widetilde{SR}\_{0,\widetilde{N}+1}^{equal} evaluation at time N~+1\widetilde{N}+1, where

|  |  |  |
| --- | --- | --- |
|  | S​R~0,N~+1=𝝁0,N~+1⊤​ϕ^0,N~+1ϕ^0,N~+1⊤​𝚺0,N~+1​ϕ^0,N~+1,S​R~0,N~+1e​q​u​a​l=𝝁0,N~+1⊤​ϕ^N~+1e​q​u​a​l(ϕ^N~+1e​q​u​a​l)⊤​𝚺0,N~+1​ϕ^N~+1e​q​u​a​l.\widetilde{SR}\_{0,\widetilde{N}+1}=\frac{\bm{\mu}\_{0,\widetilde{N}+1}^{\top}\widehat{\bm{\phi}}\_{0,\widetilde{N}+1}}{\sqrt{\widehat{\bm{\phi}}\_{0,\widetilde{N}+1}^{\top}\bm{\Sigma}\_{0,\widetilde{N}+1}\widehat{\bm{\phi}}\_{0,\widetilde{N}+1}}},\ \widetilde{SR}\_{0,\widetilde{N}+1}^{equal}=\frac{\bm{\mu}\_{0,\widetilde{N}+1}^{\top}\widehat{\bm{\phi}}\_{\widetilde{N}+1}^{equal}}{\sqrt{(\widehat{\bm{\phi}}\_{\widetilde{N}+1}^{equal})^{\top}\bm{\Sigma}\_{0,\widetilde{N}+1}\widehat{\bm{\phi}}\_{\widetilde{N}+1}^{equal}}}. |  |

Denote S​R0,N~+1SR\_{0,\widetilde{N}+1} as the maximum attainable Sharpe ratio for the target assets.

|  |  |  |
| --- | --- | --- |
|  | S​R0,N~+1=𝝁0,N~+1⊤​ϕ0,N~+1ϕ0,N~+1⊤​𝚺0,N~+1​ϕ0,N~+1.SR\_{0,\widetilde{N}+1}=\frac{\bm{\mu}\_{0,\widetilde{N}+1}^{\top}\bm{\phi}\_{0,\widetilde{N}+1}}{\sqrt{\bm{\phi}\_{0,\widetilde{N}+1}^{\top}\bm{\Sigma}\_{0,\widetilde{N}+1}\bm{\phi}\_{0,\widetilde{N}+1}}}. |  |

###### Proposition 1.

When N~→∞\widetilde{N}\rightarrow\infty, if sup‖𝒂‖2=1,𝒂∈Rd​E​‖𝒂⊤​(𝒓m,t−𝝁m,t)‖4≤c1<∞\underset{\left\|\bm{a}\right\|\_{2}=1,\ \bm{a}\in\text{R}^{d}}{\text{sup}}\text{E}\left\|\bm{a}^{\top}(\bm{r}\_{m,t}-\bm{\mu}\_{m,t})\right\|^{4}\leq c\_{1}<\infty and 0<c2≤λm​i​n​(Σ0,N~+1)0<c\_{2}\leq\lambda\_{min}(\Sigma\_{0,\widetilde{N}+1}) hold uniformly for some positive constants c1c\_{1} and c2c\_{2}, and d/N~→0d/\widetilde{N}\rightarrow 0, then

|  |  |  |
| --- | --- | --- |
|  | S​R~0,N~+1S​R0,N~+1=1+op​(1),S​R~0,N~+1e​q​u​a​lS​R0,N~+1=1+op​(1),\frac{\widetilde{SR}\_{0,\widetilde{N}+1}}{SR\_{0,\widetilde{N}+1}}=1+o\_{p}(1),\ \ \frac{\widetilde{SR}\_{0,\widetilde{N}+1}^{equal}}{SR\_{0,\widetilde{N}+1}}=1+o\_{p}(1), |  |

|  |  |  |
| --- | --- | --- |
|  | Var​(S​R~0,N~+1e​q​u​a​l)Var​(S​R~0,N~+1)→1(M+1)2.\frac{\text{Var}(\widetilde{SR}^{equal}\_{0,\widetilde{N}+1})}{\text{Var}(\widetilde{SR}\_{0,\widetilde{N}+1})}\rightarrow\frac{1}{(M+1)^{2}}. |  |

[Proposition 1](https://arxiv.org/html/2511.21221v1#Thmproposition1 "Proposition 1. ‣ 1.1 A motivation example ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning") implies that the resulting Sharpe ratio will converge to the maximum value S​R0,N~+1SR\_{0,\widetilde{N}+1} in probability, irrespective of whether we employ ϕ^0,N~+1\widehat{\bm{\phi}}\_{0,\widetilde{N}+1} or ϕ^N~+1e​q​u​a​l\widehat{\bm{\phi}}^{equal}\_{\widetilde{N}+1}. However, the asymptotic variance differs significantly between these strategies. Specifically, S​R~0,N~+1e​q​u​a​l\widetilde{SR}\_{0,\widetilde{N}+1}^{equal} achieves a superior convergence rate, as it exhibits a lower variance. See Appendix E for the proof of [Proposition 1](https://arxiv.org/html/2511.21221v1#Thmproposition1 "Proposition 1. ‣ 1.1 A motivation example ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning"). The following example provides an intuitive illustration of [Proposition 1](https://arxiv.org/html/2511.21221v1#Thmproposition1 "Proposition 1. ‣ 1.1 A motivation example ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning").

Example 1.
Let M=5M=5 and assume the asset returns of the source and target assets follow the same multivariate normal distribution MVN​(𝝁,𝚺)\text{MVN}(\bm{\mu},\bm{\Sigma}). That is, for m=0,1,…,5m=0,1,\dots,5 and t=1,…,N~t=1,\dots,\widetilde{N},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓m,t∼MVN​(𝝁,𝚺),\bm{r}\_{m,t}\sim\text{MVN}(\bm{\mu},\bm{\Sigma}), |  | (7) |

where 𝝁=(1.5,1.9,2.8,1.7,−0.9)⊤\bm{\mu}=(1.5,1.9,2.8,1.7,-0.9)^{\top} and the components of the covariance matrix are
𝚺​(i,j)=0.5|i−j|\bm{\Sigma}(i,j)=0.5^{|i-j|}. Generate the target data and the source data with the sample size N~\widetilde{N} using ([7](https://arxiv.org/html/2511.21221v1#S1.Ex12 "Equation 7 ‣ 1.1 A motivation example ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning")), respectively, where N~∈{30,60,90,120,150,250,300,400,500}\widetilde{N}\in\{30,60,90,120,150,250,300,400,500\}. Calculate S​R~0,N~+1\widetilde{SR}\_{0,\widetilde{N}+1} and S​R~0,N~+1e​q​u​a​l\widetilde{SR}^{equal}\_{0,\widetilde{N}+1}. Let E​S​R0,N~+1ESR\_{0,\widetilde{N}+1} and E​S​R0,N~+1e​q​u​a​lESR^{equal}\_{0,\widetilde{N}+1} denote the sample mean of S​R~0,N~+1\widetilde{SR}\_{0,\widetilde{N}+1} and S​R~0,N~+1e​q​u​a​l\widetilde{SR}^{equal}\_{0,\widetilde{N}+1} over 10001000 replications, respectively. Let V​S​R0,N~+1VSR\_{0,\widetilde{N}+1} and V​S​R0,N~+1e​q​u​a​lVSR^{equal}\_{0,\widetilde{N}+1} denote the sample variance of S​R~0,N~+1\widetilde{SR}\_{0,\widetilde{N}+1} and S​R~0,N~+1e​q​u​a​l\widetilde{SR}^{equal}\_{0,\widetilde{N}+1} over 10001000 replications, respectively. In detail, the four indexes can be derived using the following formulas. Denote ϕ^0,N~+1j\widehat{\bm{\phi}}^{j}\_{0,\widetilde{N}+1} and ϕ^N~+1e​q​u​a​l,j\widehat{\bm{\phi}}\_{\widetilde{N}+1}^{equal,j} as the asset allocation calculated in the jjth replication, respectively.

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​R~0,N~+1j=𝝁0,N~+1⊤​ϕ^0,N~+1jϕ^0,N~+1j⊤​𝚺0,N~+1​ϕ^0,N~+1j,\displaystyle\widetilde{SR}\_{0,\widetilde{N}+1}^{j}=\frac{\bm{\mu}\_{0,\widetilde{N}+1}^{\top}\widehat{\bm{\phi}}^{j}\_{0,\widetilde{N}+1}}{\sqrt{\widehat{\bm{\phi}}\_{0,\widetilde{N}+1}^{j\top}\bm{\Sigma}\_{0,\widetilde{N}+1}\widehat{\bm{\phi}}^{j}\_{0,\widetilde{N}+1}}}, | S​R~0,N~+1e​q​u​a​l,j=𝝁0,N~+1⊤​ϕ^N~+1e​q​u​a​l,j(ϕ^N~+1e​q​u​a​l,j)⊤​𝚺0,N~+1​ϕ^N~+1e​q​u​a​l,j,\displaystyle\ \ \widetilde{SR}\_{0,\widetilde{N}+1}^{equal,j}=\frac{\bm{\mu}\_{0,\widetilde{N}+1}^{\top}\widehat{\bm{\phi}}\_{\widetilde{N}+1}^{equal,j}}{\sqrt{(\widehat{\bm{\phi}}\_{\widetilde{N}+1}^{equal,j})^{\top}\bm{\Sigma}\_{0,\widetilde{N}+1}\widehat{\bm{\phi}}\_{\widetilde{N}+1}^{equal,j}}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E​S​R0,N~+1=11000​∑j=11000S​R~0,N~+1j,\displaystyle ESR\_{0,\widetilde{N}+1}=\frac{1}{1000}\sum\_{j=1}^{1000}\widetilde{SR}\_{0,\widetilde{N}+1}^{j}, | E​S​R0,N~+1e​q​u​a​l=11000​∑j=11000S​R~0,N~+1e​q​u​a​l,j,\displaystyle\ \ ESR^{equal}\_{0,\widetilde{N}+1}=\frac{1}{1000}\sum\_{j=1}^{1000}\widetilde{SR}^{equal,j}\_{0,\widetilde{N}+1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | V​S​R0,N~+1=11000​∑j=11000\displaystyle VSR\_{0,\widetilde{N}+1}=\frac{1}{1000}\sum\_{j=1}^{1000} | (S​R~0,N~+1j−E​S​R0,N~+1)2,\displaystyle(\widetilde{SR}\_{0,\widetilde{N}+1}^{j}-ESR\_{0,\widetilde{N}+1})^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | V​S​R0,N~+1e​q​u​a​l=11000​∑j=11000\displaystyle VSR^{equal}\_{0,\widetilde{N}+1}=\frac{1}{1000}\sum\_{j=1}^{1000} | (S​R~0,N~+1e​q​u​a​l,j−E​S​R0,N~+1e​q​u​a​l)2.\displaystyle(\widetilde{SR}^{equal,j}\_{0,\widetilde{N}+1}-ESR^{equal}\_{0,\widetilde{N}+1})^{2}. |  |

Furthermore, to evaluate the relative performance of the equal-weighted allocation strategy, we conduct a comparative analysis with a baseline strategy that augments the target dataset size. Specifically, we compute the portfolio ϕ^0,N~+1P​o​o​l\widehat{\bm{\phi}}\_{0,\widetilde{N}+1}^{Pool} by pooling all available observations from each dataset.
We proceed to compute the resulting Sharpe ratio, denoted as S​R~0,N~+1P​o​o​l\widetilde{SR}\_{0,\widetilde{N}+1}^{Pool}, for the merged-sample strategy. Let ϕ^0,N~+1P​o​o​l,j\widehat{\bm{\phi}}\_{0,\widetilde{N}+1}^{Pool,j} and S​R~0,N~+1P​o​o​l,j\widetilde{SR}\_{0,\widetilde{N}+1}^{Pool,j} denote the portfolio strategy and the resulting Sharpe ratio estimated in the jjth replication by data merging, respectively. The expected Sharpe ratio E​S​R0,N~+1P​o​o​lESR\_{0,\widetilde{N}+1}^{Pool} is estimated using the sample average over 10001000 independent replications. That is,

|  |  |  |
| --- | --- | --- |
|  | E​S​R0,N~+1P​o​o​l=11000​∑j=11000S​R~0,N~+1P​o​o​l,j,where​S​R~0,N~+1P​o​o​l,j=𝝁0,N~+1⊤​ϕ^N~+1P​o​o​l,j(ϕ^N~+1P​o​o​l,j)⊤​𝚺0,N~+1​ϕ^N~+1P​o​o​l,j.ESR^{Pool}\_{0,\widetilde{N}+1}=\frac{1}{1000}\sum\_{j=1}^{1000}\widetilde{SR}^{Pool,j}\_{0,\widetilde{N}+1},\ \text{where}\ \widetilde{SR}\_{0,\widetilde{N}+1}^{Pool,j}=\frac{\bm{\mu}\_{0,\widetilde{N}+1}^{\top}\widehat{\bm{\phi}}\_{\widetilde{N}+1}^{Pool,j}}{\sqrt{(\widehat{\bm{\phi}}\_{\widetilde{N}+1}^{Pool,j})^{\top}\bm{\Sigma}\_{0,\widetilde{N}+1}\widehat{\bm{\phi}}\_{\widetilde{N}+1}^{Pool,j}}}. |  |

With the population mean vector 𝝁\bm{\mu} and covariance matrix 𝚺\bm{\Sigma} specified, the attainable maximum Sharpe ratio is analytically determined to be S​R0,N~+1=2.95SR\_{0,\widetilde{N}+1}=2.95 as our benchmark. [Figure 1](https://arxiv.org/html/2511.21221v1#S1.F1 "Figure 1 ‣ 1.1 A motivation example ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning") demonstrates that both S​R~0,N~+1\widetilde{SR}\_{0,\widetilde{N}+1} and S​R~0,N~+1e​q​u​a​l\widetilde{SR}^{equal}\_{0,\widetilde{N}+1} exhibit asymptotic convergence to the theoretical maximum S​R0,N~+1SR\_{0,\widetilde{N}+1}. However, S​R~0,N~+1e​q​u​a​l\widetilde{SR}^{equal}\_{0,\widetilde{N}+1} exhibits superior finite sample properties, consistently dominating S​R~0,N~+1\widetilde{SR}\_{0,\widetilde{N}+1} across all N~\widetilde{N}. Under the identical data generating processes of each dataset, incorporating additional source data effectively expands the informational basis for estimation. The analysis of the variance indicates that as N~→∞\widetilde{N}\to\infty, V​S​R0,N~+1e​q​u​a​l/V​S​R0,N~+1VSR\_{0,\widetilde{N}+1}^{equal}/VSR\_{0,\widetilde{N}+1} converges to its theoretical limit 1/(M+1)2=1/361/(M+1)^{2}=1/36. This also indicates that S​R~0,N~+1e​q​u​a​l\widetilde{SR}^{equal}\_{0,\widetilde{N}+1} exhibits a higher convergence rate to its asymptotic limit compared to the conventional estimator S​R~0,N~+1\widetilde{SR}\_{0,\widetilde{N}+1}.

(a) Simulation comparison of Sharpe ratio

![Refer to caption](x1.png)

(b) Simulation comparison of variance

![Refer to caption](x2.png)

Figure 1: Performance of different portfolio strategies

The figure presents a comparative analysis of the Sharpe ratio values obtained through different portfolio strategies across varying sample sizes N~\widetilde{N}. In the left panel, we demonstrate E​S​R0,N~+1e​q​u​a​lESR\_{0,\widetilde{N}+1}^{equal} (blue line with left-pointing marks), E​S​R0,N~+1P​o​o​lESR\_{0,\widetilde{N}+1}^{Pool} (gray line with star markers), E​S​R0,N~+1ESR\_{0,\widetilde{N}+1} (orange line with right-pointing markers) and the maximum Sharpe ratio attainable for the target (black line). In the right panel, we demonstrate the sample V​S​R0,N~+1e​q​u​a​l/V​S​R0,N~+1VSR\_{0,\widetilde{N}+1}^{equal}/VSR\_{0,\widetilde{N}+1} (blue line with circular markers) and the theoretical limit of the ratio (black line).

### 1.2 Transfer learning strategy by forward validation

In the motivation example, we demonstrate the efficacy of integrating data from multiple sources to enhance the investment performance of the target. Our findings reveal that even a naive equal weighted combination strategy yields significant improvements. Nevertheless, empirical evidence often reveals substantial heterogeneity across different markets, which renders equal weighted combination suboptimal and may induce negative transfer effects that significantly degrade model performance. To better accommodate the potential heterogeneity in empirical data, we propose a novel data-driven weighting strategy that adaptively adjusts to market conditions and improves the investment performance of the target market at time N~+1\widetilde{N}+1. To choose the weight 𝒘\bm{w} in ϕ^t​(𝒘)\widehat{\bm{\phi}}\_{t}(\bm{w}), we propose the criterion in [Algorithm 1](https://arxiv.org/html/2511.21221v1#alg1 "Algorithm 1 ‣ 1.2 Transfer learning strategy by forward validation ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning"). Denote [x][x] as the maximum integer that do not larger than xx.

Algorithm 1  Transfer Learning (T​LTL) algorithm

Step 1. Split the target data and source data.

Divide each dataset into [N~/h][\widetilde{N}/h] disjoint parts in time order. Within this partitioning, the initial segment of each dataset contains Nm−([N~/h]−1)​hN\_{m}-([\widetilde{N}/h]-1)h samples, while all subsequent segments maintain a constant size of hh samples.

Step 2. Renumbering the timestamp.

After each interval boundary, index the subsequent temporal points as τi\tau\_{i} where i=1,…,[N~/h]i=1,\dots,[\widetilde{N}/h].111For pedagogical clarity, we demonstrate [Step 1](https://arxiv.org/html/2511.21221v1#alg1.l1 "In Algorithm 1 ‣ 1.2 Transfer learning strategy by forward validation ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning") and [Step 2](https://arxiv.org/html/2511.21221v1#alg1.l3 "In Algorithm 1 ‣ 1.2 Transfer learning strategy by forward validation ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning") through a specific case. Consider a scenario with parameters M=3,N0=300,N1=400,N2=500,N3=600,h=50M=3,\ N\_{0}=300,\ N\_{1}=400,\ N\_{2}=500,\ N\_{3}=600,\ h=50. In this configuration, each dataset is partitioned into [N~/h]=[N0/h]=6[\widetilde{N}/h]=[N\_{0}/h]=6 parts and the subsequent evaluation time points after each interval boundary are t∈{51,101,151,201,251,301}t\in\{51,101,151,201,251,301\}. Relabel these time points as τi\tau\_{i}, where i=1,…,6\ i=1,\dots,6, respectively.

Step 3. Calculate the related parameter estimators of each dataset at time τi\tau\_{i}.

For m=0m=0 to MM:

1. 1.

   Calculate 𝝁^m,τi\widehat{\bm{\mu}}\_{m,\tau\_{i}} and 𝚺^m,τi\widehat{\bm{\Sigma}}\_{m,\tau\_{i}} using the latest hh samples and ([3](https://arxiv.org/html/2511.21221v1#S1.Ex4 "Equation 3 ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning"))-([4](https://arxiv.org/html/2511.21221v1#S1.Ex5 "Equation 4 ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning")), respectively.
2. 2.

   Estimate 𝝁m,τi\bm{\mu}\_{m,\tau\_{i}} and 𝚺m,τi\bm{\Sigma}\_{m,\tau\_{i}} using all the former samples and ([3](https://arxiv.org/html/2511.21221v1#S1.Ex4 "Equation 3 ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning"))-([4](https://arxiv.org/html/2511.21221v1#S1.Ex5 "Equation 4 ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning")). Given the estimators, apply ([5](https://arxiv.org/html/2511.21221v1#S1.Ex6 "Equation 5 ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning")) to calculate ϕ^m,τi\widehat{\bm{\phi}}\_{m,\tau\_{i}}.

Step 4. Solve weights.

Solve ([8](https://arxiv.org/html/2511.21221v1#S1.Ex15 "Equation 8In Algorithm 1 ‣ 1.2 Transfer learning strategy by forward validation ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning")) to obtain the optimal transferring weight.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘^=arg⁡max𝒘∈𝒲​1[N~/h]−1​∑i=1[N~/h]−1(𝝁^0,τi+1⊤)​ϕ^τi​(𝒘)ϕ^τi​(𝒘)⊤​𝚺^0,τi+1​ϕ^τi​(𝒘).\widehat{\bm{w}}=\underset{\bm{w}\in\mathcal{W}}{\arg\max}\ \frac{1}{[\widetilde{N}/h]-1}\sum\_{i=1}^{[\widetilde{N}/h]-1}\frac{(\widehat{\bm{\mu}}\_{0,\tau\_{i+1}}^{\top})\widehat{\bm{\phi}}\_{\tau\_{i}}(\bm{w})}{\sqrt{\widehat{\bm{\phi}}\_{\tau\_{i}}(\bm{w})^{\top}\widehat{\bm{\Sigma}}\_{0,\tau\_{i+1}}\widehat{\bm{\phi}}\_{\tau\_{i}}(\bm{w})}}. |  | (8) |

Step 5. Calculate the asset allocation at time N~+1\widetilde{N}+1.

Let w^m\widehat{w}\_{m} be the (m+1)(m+1)th component of 𝒘^\widehat{\bm{w}}. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^N~+1​(𝒘^)=∑m=0Mw^m​ϕ^m,N~+1.\widehat{\bm{\phi}}\_{\widetilde{N}+1}(\widehat{\bm{w}})=\sum\limits\_{m=0}\limits^{M}\widehat{w}\_{m}\widehat{\bm{\phi}}\_{m,\widetilde{N}+1}. |  | (9) |

The schematic diagram in [Figure 2](https://arxiv.org/html/2511.21221v1#S1.F2 "Figure 2 ‣ 1.2 Transfer learning strategy by forward validation ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning") provides an intuitive illustration of the algorithmic workflow. For demonstrative purposes and without loss of generality, we consider the case where N~=N0\widetilde{N}=N\_{0} in this exposition.

![Refer to caption](x3.png)

Figure 2: Schematic illustration of the proposed T​LTL strategy

The figure provides an intuitive visualization of the operational workflow of the proposed T​LTL strategy for the case where M=3M=3 and N~=N0\widetilde{N}=N\_{0}.

## 2 Asymptotic properties

In this section, we demonstrate that our proposed T​LTL strategy can
automatically assign all weights to the informative datasets and asymptotically achieve the maximum attainable
Sharpe ratio. Furthermore, we conduct a comparative analysis of the variance between the Sharpe ratio achieved through our proposed T​LTL strategy and the N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy. To present the asymptotic properties, we need some regularity conditions. Unless otherwise stated, all limiting properties are set when the sample size of each dataset goes to infinity.

###### Assumption 1.

For m=0,1,…,Mm=0,1,\dots,M, there exist a constant ζ>0\zeta>0, parameters {𝝁m,τi∗|i=1,…,[N~/h]}\{\bm{\mu}^{\*}\_{m,\tau\_{i}}|\ i=1,\dots,[\widetilde{N}/h]\} and {𝚺m,τi∗|i=1,…,[N~/h]}\{\bm{\Sigma}^{\*}\_{m,\tau\_{i}}|\ i=1,\dots,[\widetilde{N}/h]\}, such that

(i)(\text{i}) dζ​h−12=o​(1)d^{\zeta}h^{-\frac{1}{2}}=o(1);

(ii)(\text{ii}) h12​d−ζ​‖𝝁^m,τi−𝝁m,τi∗‖2=Op​(1)h^{\frac{1}{2}}d^{-\zeta}\parallel\widehat{\bm{\mu}}\_{m,\tau\_{i}}-\bm{\mu}^{\*}\_{m,\tau\_{i}}\parallel\_{2}=O\_{p}(1) and h12​d−ζ​‖𝚺^m,τi−𝚺m,τi∗‖F=Op​(1);h^{\frac{1}{2}}d^{-\zeta}\parallel\widehat{\bm{\Sigma}}\_{m,\tau\_{i}}-\bm{\Sigma}^{\*}\_{m,\tau\_{i}}\parallel\_{\text{F}}=O\_{p}(1);

(iii)(\text{iii}) h12​d−ζ​‖𝝁m,τi+1∗−𝝁m,τi∗‖2=O​(1)h^{\frac{1}{2}}d^{-\zeta}\parallel\bm{\mu}^{\*}\_{m,\tau\_{i+1}}-\bm{\mu}^{\*}\_{m,\tau\_{i}}\parallel\_{2}=O(1) and h12​d−ζ​‖𝚺m,τi+1∗−𝚺m,τi∗‖F=O​(1).h^{\frac{1}{2}}d^{-\zeta}\parallel\bm{\Sigma}^{\*}\_{m,\tau\_{i+1}}-\bm{\Sigma}^{\*}\_{m,\tau\_{i}}\parallel\_{\text{F}}=O(1).

[Assumption 1(i)](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") restricts the divergence rate of dd. [Assumption 1(ii)](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") requires that there exist convergence relationships between the historical sample estimators 𝝁^m,τi\widehat{\bm{\mu}}\_{m,\tau\_{i}}, 𝚺^m,τi\widehat{\bm{\Sigma}}\_{m,\tau\_{i}} and the limit parameters 𝝁m,τi∗\bm{\mu}^{\*}\_{m,\tau\_{i}}, 𝚺m,τi∗\bm{\Sigma}^{\*}\_{m,\tau\_{i}}, respectively.
[Assumption 1(iii)](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") imposes additional conditions on the sequences {𝝁m,τi∗|i=1,…,[N~/h]}\{\bm{\mu}^{\*}\_{m,\tau\_{i}}|\ i=1,\dots,[\widetilde{N}/h]\} and {𝚺m,τi∗|i=1,…,[N~/h]}\{\bm{\Sigma}^{\*}\_{m,\tau\_{i}}|\ i=1,\dots,[\widetilde{N}/h]\} by requiring the internal convergence. In the case of multivariate sample mean and multivariate sample covariance, the reviews of the literature on the
dependence of the error of approximation on the dimension dd are given (see, e.g., Zitikis2006; bentkus1986; bentkus2003; bloznelis1989; gotze1991; nagaev2006). bentkus2003 proves the existence of ζ\zeta, where ζ=1/4\zeta=1/4, {𝝁m,τi∗|i=1,…,[N~/h]}\{\bm{\mu}^{\*}\_{m,\tau\_{i}}|\ i=1,\dots,[\widetilde{N}/h]\} and {𝚺m,τi∗|i=1,…,[N~/h]}\{\bm{\Sigma}^{\*}\_{m,\tau\_{i}}|\ i=1,\dots,[\widetilde{N}/h]\} under some specific conditions where the samples are i.i.di.i.d, the expectation exists, the covariance matrix is positive definite and the third-order moment is finite. This assumption remains valid according to the conclusion of Zitikis2006, where the relationship between the convergence rates of the multivariate sample mean, multivariate sample covariance matrix and the divergent rate of the parameters dd and hh are established under other regularity conditions.

Denote

|  |  |  |
| --- | --- | --- |
|  | S​R~0,τi+1∗​(𝒘)=(𝝁0,τi+1⊤)​ϕ^τi​(𝒘)ϕ^τi​(𝒘)⊤​𝚺0,τi+1​ϕ^τi​(𝒘),M​S~N~∗​(𝒘)=1[N~/h]−1​∑i=1[N~/h]−1S​R~0,τi+1∗​(𝒘),\widetilde{SR}^{\*}\_{0,\tau\_{i+1}}(\bm{w})=\frac{(\bm{\mu}\_{0,\tau\_{i+1}}^{\top})\widehat{\bm{\phi}}\_{\tau\_{i}}(\bm{w})}{\sqrt{\widehat{\bm{\phi}}\_{\tau\_{i}}(\bm{w})^{\top}\bm{\Sigma}\_{0,\tau\_{i+1}}\widehat{\bm{\phi}}\_{\tau\_{i}}(\bm{w})}},\ \ \widetilde{MS}^{\*}\_{\widetilde{N}}(\bm{w})=\frac{1}{[\widetilde{N}/h]-1}\sum\_{i=1}^{[\widetilde{N}/h]-1}\widetilde{SR}^{\*}\_{0,\tau\_{i+1}}(\bm{w}), |  |

|  |  |  |
| --- | --- | --- |
|  | S​R0,τi+1=(𝝁0,τi+1⊤)​ϕ0,τi+1ϕ0,τi+1⊤​𝚺0,τi+1​ϕ0,τi+1,M​SN~=1[N~/h]−1​∑i=1[N~/h]−1S​R0,τi+1.SR\_{0,\tau\_{i+1}}=\frac{(\bm{\mu}\_{0,\tau\_{i+1}}^{\top})\bm{\phi}\_{0,\tau\_{i+1}}}{\sqrt{\bm{\phi}\_{0,\tau\_{i+1}}^{\top}\bm{\Sigma}\_{0,\tau\_{i+1}}\bm{\phi}\_{0,\tau\_{i+1}}}},\ \ MS\_{\widetilde{N}}=\frac{1}{[\widetilde{N}/h]-1}\sum\_{i=1}^{[\widetilde{N}/h]-1}SR\_{0,\tau\_{i+1}}. |  |

We can calculate the corresponding asset allocation ϕm,τi∗\bm{\phi}\_{m,\tau\_{i}}^{\*} under the parameters 𝝁m,τi∗\bm{\mu}^{\*}\_{m,\tau\_{i}}, 𝚺m,τi∗\bm{\Sigma}^{\*}\_{m,\tau\_{i}} and Equation ([1](https://arxiv.org/html/2511.21221v1#S1.Ex2 "Equation 1 ‣ 1 Model framework ‣ Portfolio Optimization via Transfer Learning")). If ‖ϕ0,τi−ϕm,τi∗‖2=o​(1)\parallel\bm{\phi}\_{0,\tau\_{i}}-\bm{\phi}\_{m,\tau\_{i}}^{\*}\parallel\_{2}=o(1) holds for each τi\tau\_{i}, define the corresponding dataset as an effective information set which can provide effective information for the investment in the target. Under [Assumption 1](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning"), if the limit parameters 𝝁m,τi∗\bm{\mu}^{\*}\_{m,\tau\_{i}} and 𝚺m,τi∗\bm{\Sigma}^{\*}\_{m,\tau\_{i}} satisfy that ‖𝝁0,τi−𝝁m,τi∗‖2=o​(1)\parallel\bm{\mu}\_{0,\tau\_{i}}-\bm{\mu}^{\*}\_{m,\tau\_{i}}\parallel\_{2}=o(1) and ‖𝚺0,τi−𝚺m,τi∗‖F=o​(1)\parallel\bm{\Sigma}\_{0,\tau\_{i}}-\bm{\Sigma}^{\*}\_{m,\tau\_{i}}\parallel\_{\text{F}}=o(1), then ‖ϕ0,τi−ϕm,τi∗‖2=o​(1)\parallel\bm{\phi}\_{0,\tau\_{i}}-\bm{\phi}\_{m,\tau\_{i}}^{\*}\parallel\_{2}=o(1), which implies that the dataset with index mm is an effective information set when the difference between the corresponding limit parameters 𝝁m,τi∗\bm{\mu}^{\*}\_{m,\tau\_{i}}, 𝚺m,τi∗\bm{\Sigma}^{\*}\_{m,\tau\_{i}} and the population parameters of the target 𝝁0,τi\bm{\mu}\_{0,\tau\_{i}}, 𝚺0,τi\bm{\Sigma}\_{0,\tau\_{i}} asymptotically converge to 0, respectively. Let 𝒟⊆{0,1,…,M}\mathcal{D}\subseteq\{0,1,\dots,M\} denote the index set of datasets which can provide effective information for the target and 𝒟c\mathcal{D}^{c} denote the
complement of 𝒟\mathcal{D}. Denote Γ​(𝒘)=∑m∈𝒟wm\Gamma(\bm{w})=\sum\_{m\in\mathcal{D}}w\_{m}, where wmw\_{m} is the (m+1)(m+1)th element of 𝒘\bm{w}, then Γ​(𝒘^)=∑m∈𝒟w^m\Gamma(\widehat{\bm{w}})=\sum\_{m\in\mathcal{D}}\widehat{w}\_{m}. Let ξ~N~∗=M​SN~−sup𝒘∈𝒲,Γ​(𝒘)=0​M​S~N~∗​(𝒘)\widetilde{\xi}^{\*}\_{\widetilde{N}}=MS\_{\widetilde{N}}-\text{sup}\_{\bm{w}\in\mathcal{W},\Gamma(\bm{w})=0}\ \widetilde{MS}^{\*}\_{\widetilde{N}}(\bm{w}).

###### Assumption 2.

ξ~N~∗−1​h−12​dζ=o​(1)\widetilde{\xi}\_{\widetilde{N}}^{\*-1}h^{-\frac{1}{2}}d^{\zeta}=o(1).

[Assumption 2](https://arxiv.org/html/2511.21221v1#Thmassumption2 "Assumption 2. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") postulates the convergence rate of the difference between the maximum Sharpe ratio M​SN~MS\_{\widetilde{N}} and the weighted Sharpe ratio M​S~N~∗​(𝒘)\widetilde{MS}^{\*}\_{\widetilde{N}}(\bm{w}) when the weight proportion on the datasets which can provide effective information is set to be 0. If there exists a source dataset SjS\_{j} which just provides ineffective information, in other words, the corresponding optimal asset allocation under the parameters 𝝁m,τi∗\bm{\mu}^{\*}\_{m,\tau\_{i}} and 𝚺m,τi∗\bm{\Sigma}^{\*}\_{m,\tau\_{i}}, denoted as ϕj,t∗\bm{\phi}^{\*}\_{j,t}, is greatly different from the optimal asset allocation ϕ0,t\bm{\phi}\_{0,t}, the Sharpe ratio obtained using the allocation ϕj,t∗\bm{\phi}^{\*}\_{j,t} must be less than the maximum Sharpe ratio. From this point of view, this assumption is easy to be satisfied.

###### Assumption 3.

(i)(\text{i}) h12​d−ζ​‖𝝁0,τi−𝝁0,τi∗‖2=O​(1)h^{\frac{1}{2}}d^{-\zeta}\parallel\bm{\mu}\_{0,\tau\_{i}}-\bm{\mu}^{\*}\_{0,\tau\_{i}}\parallel\_{2}=O(1);

(ii)(\text{ii}) h12​d−ζ​‖𝚺0,τi−𝚺0,τi∗‖F=O​(1).h^{\frac{1}{2}}d^{-\zeta}\parallel\bm{\Sigma}\_{0,\tau\_{i}}-\bm{\Sigma}^{\*}\_{0,\tau\_{i}}\parallel\_{\text{F}}=O(1).

[Assumption 3](https://arxiv.org/html/2511.21221v1#Thmassumption3 "Assumption 3. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") imposes convergence constraints on parameters 𝝁0,τi∗\bm{\mu}^{\*}\_{0,\tau\_{i}} and 𝚺0,τi∗\bm{\Sigma}^{\*}\_{0,\tau\_{i}}, which can be economically rationalized through two fundamental market dynamics. First, the assumption captures the local stationarity property observed in high-frequency financial data (diebold2001) through 𝝁0,τi∗\bm{\mu}^{\*}\_{0,\tau\_{i}} and 𝚺0,τi∗\bm{\Sigma}^{\*}\_{0,\tau\_{i}}, where market microstructure effects dominate short-term price movements. Second, it accommodates the equilibrium convergence behavior characteristic of long-term market data (cochrane2009) through the convergence properties, where fundamental economic forces drive asset prices towards their steady-state values. Combined with [Assumption 1](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning"), [Assumption 3](https://arxiv.org/html/2511.21221v1#Thmassumption3 "Assumption 3. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") implies that the historical sample estimators 𝝁^0,τi\widehat{\bm{\mu}}\_{0,\tau\_{i}} and 𝚺^0,τi\widehat{\bm{\Sigma}}\_{0,\tau\_{i}} consistently estimate the population mean and covariance of the target, which can be implied by 0∈𝒟0\in\mathcal{D}.

###### Assumption 4.

For m=0,1,…,Mm=0,1,\dots,M and i=1,…,[N~/h]i=1,\dots,[\widetilde{N}/h], the estimated covariance matrix at time τi\tau\_{i}, denoted as 𝚺^m,τi\widehat{\bm{\Sigma}}\_{m,\tau\_{i}}, is positive definite almost surely.

In [Assumption 4](https://arxiv.org/html/2511.21221v1#Thmassumption4 "Assumption 4. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning"), we impose restrictions on covariance estimators at time τi\tau\_{i} for each dataset. Our methodological framework is based on portfolio Sharpe ratio optimization, which fundamentally requires strictly positive variance for all admissible investment strategies. We impose the assumption of an almost sure positive definiteness on the covariance estimator to satisfy the fact that for any column vector 𝒙≠𝟎\bm{x}\neq\bm{0}, there exists 𝒙⊤​𝚺^m,τi​𝒙>0\bm{x}^{\top}\widehat{\bm{\Sigma}}\_{m,\tau\_{i}}\bm{x}>0 almost surely.

###### Theorem 1.

If [Assumptions 1](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning")-[4](https://arxiv.org/html/2511.21221v1#Thmassumption4 "Assumption 4. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") are satisfied, then

|  |  |  |
| --- | --- | --- |
|  | Γ​(𝒘^)→1\Gamma(\bm{\widehat{w}})\rightarrow 1 |  |

in probability.

This theorem demonstrates a kind of informative dataset selection consistency, in that our strategy can automatically assign all the weights to the datasets which can provide effective information for the target. It is worth to note that this theorem holds only for the case where the estimators calculated by the target data need to be helpful. This theorem also effectively avoids the problem of negative transfer. See Appendix B for the proof of [Theorem 1](https://arxiv.org/html/2511.21221v1#Thmtheorem1 "Theorem 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning").

Having established the convergence properties of the weight estimator, we now characterize the Sharpe ratio of the target portfolio at time N~+1\widetilde{N}+1 under our proposed strategy. Denote

|  |  |  |
| --- | --- | --- |
|  | S​R~0,τi+1​(𝒘)=(𝝁0,τi+1⊤)​ϕ^τi+1​(𝒘)ϕ^τi+1​(𝒘)⊤​𝚺0,τi+1​ϕ^τi+1​(𝒘),M​S~N~​(𝒘)=1[N~/h]−1​∑i=1[N~/h]−1S​R~0,τi+1​(𝒘).\widetilde{SR}\_{0,\tau\_{i+1}}(\bm{w})=\frac{(\bm{\mu}\_{0,\tau\_{i+1}}^{\top})\widehat{\bm{\phi}}\_{\tau\_{i+1}}(\bm{w})}{\sqrt{\widehat{\bm{\phi}}\_{\tau\_{i+1}}(\bm{w})^{\top}\bm{\Sigma}\_{0,\tau\_{i+1}}\widehat{\bm{\phi}}\_{\tau\_{i+1}}(\bm{w})}},\ \ \widetilde{MS}\_{\widetilde{N}}(\bm{w})=\frac{1}{[\widetilde{N}/h]-1}\sum\_{i=1}^{[\widetilde{N}/h]-1}\widetilde{SR}\_{0,\tau\_{i+1}}(\bm{w}). |  |

###### Theorem 2.

If [Assumptions 1](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning")-[4](https://arxiv.org/html/2511.21221v1#Thmassumption4 "Assumption 4. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") are satisfied, then

|  |  |  |
| --- | --- | --- |
|  | S​R~0,N~+1​(𝒘^)S​R0,N~+1=1+op​(1).\frac{\widetilde{SR}\_{0,\widetilde{N}+1}(\widehat{\bm{w}})}{SR\_{0,\widetilde{N}+1}}=1+o\_{p}(1). |  |

This theorem demonstrates that our strategy can
asymptotically obtain the maximum Sharpe ratio S​R0,N~+1SR\_{0,\widetilde{N}+1}. See Appendix C for the proof of [Theorem 2](https://arxiv.org/html/2511.21221v1#Thmtheorem2 "Theorem 2. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning").

We have already examined the asymptotic behaviors of the weight estimators 𝒘^\widehat{\bm{w}} and the resulting Sharpe ratio S​R~0,N~+1​(𝒘^)\widetilde{SR}\_{0,\widetilde{N}+1}(\widehat{\bm{w}}). Considering that the traditional N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy also asymptotically obtains the maximum Sharpe ratio S​R0,N~+1SR\_{0,\widetilde{N}+1} under [Assumption 1](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") and [Assumption 3](https://arxiv.org/html/2511.21221v1#Thmassumption3 "Assumption 3. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") (see Appendix C), we compare the variances between the Sharpe ratios of our proposed strategy and the N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy. We further need the following assumptions.

###### Assumption 5.

For m=1,…,Mm=1,\dots,M, limsup ​(N0/Nm)≤1\underset{}{\text{limsup\ }}(N\_{0}/N\_{m})\leq 1.

[Assumption 5](https://arxiv.org/html/2511.21221v1#Thmassumption5 "Assumption 5. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") imposes certain restrictions on the sample size of each dataset. It is common and reasonable in practice, since the sample size of the target data is usually smaller. Given that all datasets in our analysis share the same sampling frequency, this assumption is very easy to be satisfied in our framework.

###### Assumption 6.

There exists 𝒘∗∈𝒲\bm{w}^{\*}\in\mathcal{W} such that 𝒘^→𝒘∗\widehat{\bm{w}}\rightarrow\bm{w}^{\*} in probability.

This assumption necessitates the convergence of the weight estimator, which can usually be achieved through an appropriate initial value and a fixed iterative direction.

Let ϕ[−d]∈Rd−1\bm{\phi}^{[-d]}\in\text{R}^{d-1} denote the truncated vector comprising the first d−1d-1 components of ϕ∈Rd\bm{\phi}\in\text{R}^{d}.

###### Assumption 7.

For m,n∈𝒟m,n\in\mathcal{D}, ‖[Nm​Var​(ϕ^m,N~+1[−d])]​[Nn​Var​(ϕ^n,N~+1[−d])]−1−𝑰d−1‖F→0\parallel[N\_{m}\text{Var}(\widehat{\bm{\phi}}^{[-d]}\_{m,\widetilde{N}+1})][N\_{n}\text{Var}(\widehat{\bm{\phi}}^{[-d]}\_{n,\widetilde{N}+1})]^{-1}-\bm{I}\_{d-1}\parallel\_{\text{F}}\rightarrow 0.

This assumption reveals the fundamental relationship between the variance of the estimator and the size of the training samples. Specifically, for m,n∈𝒟m,n\in\mathcal{D}, the relationship between Var​(ϕ^m,τi)\text{Var}(\widehat{\bm{\phi}}\_{m,\tau\_{i}}) and Var​(ϕ^n,τi)\text{Var}(\widehat{\bm{\phi}}\_{n,\tau\_{i}}) is asymptotically determined by the sample sizes used for estimation. Referring to the Theorem 11 in central, we provide a proof of this assumption based on some regularity conditions in Appendix F. A concrete example can also be found in [Simulation 1](https://arxiv.org/html/2511.21221v1#S3.SS3 "3.3 Simulation 1: Benchmark DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning"), where the estimators derived from S1S\_{1} and S5S\_{5} exhibit precisely this property.

Denote

|  |  |  |
| --- | --- | --- |
|  | S​R~0,τi+1=(𝝁0,τi+1⊤)​ϕ^0,τi+1ϕ^0,τi+1⊤​𝚺0,τi+1​ϕ^0,τi+1,M​S~N~=1[N~/h]−1​∑i=1[N~/h]−1S​R~0,τi+1.\widetilde{SR}\_{0,\tau\_{i+1}}=\frac{(\bm{\mu}\_{0,\tau\_{i+1}}^{\top})\widehat{\bm{\phi}}\_{0,\tau\_{i+1}}}{\sqrt{\widehat{\bm{\phi}}\_{0,\tau\_{i+1}}^{\top}\bm{\Sigma}\_{0,\tau\_{i+1}}\widehat{\bm{\phi}}\_{0,\tau\_{i+1}}}},\ \ \widetilde{MS}\_{\widetilde{N}}=\frac{1}{[\widetilde{N}/h]-1}\sum\_{i=1}^{[\widetilde{N}/h]-1}\widetilde{SR}\_{0,\tau\_{i+1}}. |  |

###### Theorem 3.

If [Assumptions 1](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning")-[7](https://arxiv.org/html/2511.21221v1#Thmassumption7 "Assumption 7. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") are satisfied, then

|  |  |  |
| --- | --- | --- |
|  | Var​(S​R~0,N~+1​(𝒘^))≤Var​(S​R~0,N~+1)​(1+o​(1)).\text{Var}(\widetilde{SR}\_{0,\widetilde{N}+1}(\widehat{\bm{w}}))\leq\text{Var}(\widetilde{SR}\_{0,\widetilde{N}+1})(1+o(1)). |  |

[Theorem 3](https://arxiv.org/html/2511.21221v1#Thmtheorem3 "Theorem 3. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") demonstrates the comparison of the volatility of the Sharpe ratio obtained using the T​LTL strategy and that of the N​o​n−t​r​a​n​s​f​e​rNon-transfer baseline strategy. See Appendix D for the proof of [Theorem 3](https://arxiv.org/html/2511.21221v1#Thmtheorem3 "Theorem 3. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning").

## 3 Simulation studies

In this section, we conduct two simulation studies to evaluate the performance of our proposed investment strategy and empirically validate the theoretical results established in [Section 2](https://arxiv.org/html/2511.21221v1#S2 "2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning"). To thoroughly compare investment strategies, we employed two different data generation processes (DGP) in [Simulation 1](https://arxiv.org/html/2511.21221v1#S3.SS3 "3.3 Simulation 1: Benchmark DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning") and [Simulation 2](https://arxiv.org/html/2511.21221v1#S3.SS4 "3.4 Simulation 2: FF3 model-based DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning"), respectively. In [Simulation 1](https://arxiv.org/html/2511.21221v1#S3.SS3 "3.3 Simulation 1: Benchmark DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning"), we implement a standard experimental setup. First, we systematically compare the investment performance of the proposed T​LTL strategy with several benchmark strategies under progressively increasing distributional shifts between the target and some source datasets. Second, by incrementally expanding the sample size of each dataset, we empirically validate the theoretical properties of the T​LTL strategy, as derived in [Section 2](https://arxiv.org/html/2511.21221v1#S2 "2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning"). Then, we conduct a comparative analysis between our strategy and another transfer learning-based investment strategy proposed in cao2023ssrn to assess their performance. Furthermore, based on empirical Fama French three factor model parameters derived from real market data, we simulate each dataset in [Simulation 2](https://arxiv.org/html/2511.21221v1#S3.SS4 "3.4 Simulation 2: FF3 model-based DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning") to conduct a rigorous comparative analysis across different investment strategies.

### 3.1 Alternative portfolio strategies

To assess the efficacy of our proposed strategy, we conduct a comprehensive comparative analysis with the following four established strategies in our simulation studies.

T​Le​q​u​a​lTL\_{equal}: The target data and the source data are combined using equal weighting proportions in the transfer process. That is,

|  |  |  |
| --- | --- | --- |
|  | ϕ^N~+1=∑m=0M1M+1​ϕ^m,N~+1.\widehat{\bm{\phi}}\_{\widetilde{N}+1}=\sum\limits\_{m=0}^{M}\frac{1}{M+1}\widehat{\bm{\phi}}\_{m,\widetilde{N}+1}. |  |

N​o​n−t​r​a​n​s​f​e​rNon-transfer: Maximize the Sharpe ratio of the target assets. That is,

|  |  |  |
| --- | --- | --- |
|  | ϕ^N~+1=arg⁡maxϕ∈Φ​𝝁^0,N~+1⊤​ϕϕ⊤​𝚺^0,N~+1​ϕ.\widehat{\bm{\phi}}\_{\widetilde{N}+1}=\underset{\bm{\phi}\in\Phi}{\arg\max}\frac{\widehat{\bm{\mu}}\_{0,\widetilde{N}+1}^{\top}\bm{\phi}}{\sqrt{\bm{\phi}^{\top}\widehat{\bm{\Sigma}}\_{0,\widetilde{N}+1}\bm{\phi}}}. |  |

P​o​o​lPool: Combine the target and source datasets into a unified sample population and estimate the mean and covariance using the historical sample mean and historical sample covariance of the combined data. In detail, the estimated mean vector is

|  |  |  |
| --- | --- | --- |
|  | 𝝁^0,N~+1∗=1N0+⋯+NM​∑m=0M∑j=−(Nm−N~−1)N~𝒓m,j,\widehat{\bm{\mu}}^{\*}\_{0,\widetilde{N}+1}=\frac{1}{N\_{0}+\dots+N\_{M}}\sum\limits\_{m=0}^{M}\sum\limits\_{j=-(N\_{m}-\widetilde{N}-1)}\limits^{\widetilde{N}}\bm{r}\_{m,j}, |  |

and
the estimated covariance matrix is

|  |  |  |
| --- | --- | --- |
|  | 𝚺^0,N~+1∗=1N0+⋯+NM−1​∑m=0M∑j=−(Nm−N~−1)N~(𝒓m,j−𝝁^0,N~+1∗)​(𝒓m,j−𝝁^0,N~+1∗)⊤.\widehat{\bm{\Sigma}}^{\*}\_{0,\widetilde{N}+1}=\frac{1}{N\_{0}+\dots+N\_{M}-1}\sum\limits\_{m=0}^{M}\sum\limits\_{j=-(N\_{m}-\widetilde{N}-1)}\limits^{\widetilde{N}}(\bm{r}\_{m,j}-\widehat{\bm{\mu}}^{\*}\_{0,\widetilde{N}+1})(\bm{r}\_{m,j}-\widehat{\bm{\mu}}^{\*}\_{0,\widetilde{N}+1})^{\top}. |  |

Hence, the asset allocation can be estimated by

|  |  |  |
| --- | --- | --- |
|  | ϕ^N~+1=arg⁡maxϕ∈Φ​𝝁^0,N~+1∗⊤​ϕϕ⊤​𝚺^0,N~+1∗​ϕ.\widehat{\bm{\phi}}\_{\widetilde{N}+1}=\underset{\bm{\phi}\in\Phi}{\arg\max}\frac{\widehat{\bm{\mu}}\_{0,\widetilde{N}+1}^{\*\top}\bm{\phi}}{\sqrt{\bm{\phi}^{\top}\widehat{\bm{\Sigma}}^{\*}\_{0,\widetilde{N}+1}\bm{\phi}}}. |  |

### 3.2 Evaluation methodology

We employ the following indicator to evaluate the out-of-sample forecasting performance across different strategies. Denote 𝒪\mathcal{O} as the set of time points designated for out-of-sample prediction.

S​S​RSSR: Calculate the sample Sharpe ratio (SSR) of the portfolio strategy, defined as

|  |  |  |
| --- | --- | --- |
|  | S​S​R=E¯​(ϕ^t⊤​𝒓t)V¯​(ϕ^t⊤​𝒓t),t∈𝒪,SSR=\frac{\bar{E}(\widehat{\bm{\phi}}\_{t}^{\top}\bm{r}\_{t})}{\sqrt{\bar{V}(\widehat{\bm{\phi}}\_{t}^{\top}\bm{r}\_{t})}},\ t\in\mathcal{O}, |  |

where E¯(.)\bar{E}(.) and V¯(.)\bar{V}(.) represent the sample mean and sample variance, respectively.

### 3.3 Simulation 1: Benchmark DGP

Consider a capital market consisting of 55 assets, that is, d=5d=5. The DGP follows the simulation settings in r32.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓m,t=𝜶+𝑿t​𝚷m,t+𝒆m,t,𝑿t+1=𝑩​𝑿t+𝜸t+1,\displaystyle\bm{r}\_{m,t}=\bm{\alpha}+\bm{X}\_{t}\bm{\Pi}\_{m,t}+\bm{e}\_{m,t},\ \ \bm{X}\_{t+1}=\bm{BX}\_{t}+\bm{\gamma}\_{t+1}, |  | (10) |

where 𝒓m,t∈R5,𝑿t∈R5×3,𝚷m,t∈R3,𝒆m,t∈R5,𝑩∈R5×5,𝜸t∈R5×3\bm{r}\_{m,t}\in\text{R}^{5},\ \bm{X}\_{t}\in\text{R}^{5\times 3},\ \bm{\Pi}\_{m,t}\in\text{R}^{3},\ \bm{e}\_{m,t}\in\text{R}^{5},\ \bm{B}\in\text{R}^{5\times 5},\ \bm{\gamma}\_{t}\in\text{R}^{5\times 3} and m=0,…,5,t=1,…,Nm\ m=0,\dots,5,\ t=1,\dots,N\_{m}. The term 𝜶=(0.5,0.5,0.5,0.5,0.5)⊤\bm{\alpha}=(0.5,0.5,0.5,0.5,0.5)^{\top}.
For the isolation term, 𝒆m,t\bm{e}\_{m,t} and every column of 𝜸t\bm{\gamma}\_{t} are independently identically distributed and follow a multivariate normal distribution MVN​(𝟎,𝛀)\text{MVN}(\bm{0},\bm{\Omega}), where the components of the covariance matrix 𝛀\bm{\Omega} are 𝛀​(i,j)=0.5|i−j|\bm{\Omega}(i,j)=0.5^{|i-j|}. To ensure the stationarity of 𝑿t\bm{X}\_{t}, the elements of the parameter matrix 𝑩\bm{B} are randomly generated from a uniform distribution over (−1,1)(-1,1), with the additional constraint that all eigenvalues must lie within the unit circle. Regarding the regression parameters in this simulation, the following settings are used.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝚷0,t=(0.9,0.6,0.7)⊤,t=1,…,N0,\displaystyle\bm{\Pi}\_{0,t}=(9,6,7)^{\top},\ \ t=1,\dots,N\_{0}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝚷m,t=(0.9,0.6,0.7)⊤+1t×𝜹m,m=1,5,t=1,…,Nm,\displaystyle\bm{\Pi}\_{m,t}=(9,6,7)^{\top}+\frac{1}{t}\times\bm{\delta}\_{m},\ \ m=1,5,\ t=1,\dots,N\_{m}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝚷m,t=(0.9,0.6,0.7)⊤+ρ×𝜹m,m=2,3,4,t=1,…,Nm,\displaystyle\bm{\Pi}\_{m,t}=(9,6,7)^{\top}+\rho\times\bm{\delta}\_{m},\ \ m=2,3,4,\ t=1,\dots,N\_{m}, |  |

where 𝜹m∼MVN​(𝟎,0.1​𝑰)\bm{\delta}\_{m}\sim\text{MVN}(\bm{0},0.1\bm{I}). We assign time-dependent parameters to the source data S1S\_{1} and S5S\_{5} in our simulation framework. On the one hand, it ensures that the historical sample mean and historical covariance matrix estimators for S1S\_{1} and S5S\_{5} satisfy [Assumption 1](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning"). On the other hand, it allows these source parameters to asymptotically converge to their target counterparts, thereby ensuring that S1S\_{1} and S5S\_{5} provide effective transferable information. For S2S\_{2}, S3S\_{3} and S4S\_{4}, we introduce the term ρ×𝜹m\rho\times\bm{\delta}\_{m} to the regression parameters 𝚷m,t\bm{\Pi}\_{m,t} to modulate the divergence between the source datasets and the target dataset.

#### 3.3.1 Investment performance under varying divergence

Recall that the scaling parameters {ρ×𝜹m|m=2,3,4}\{\rho\times\bm{\delta}\_{m}|m=2,3,4\} govern the divergence between the target data and the non-informative source data. To evaluate the performance of each strategy, we systematically vary ρ\rho while holding 𝜹m{\bm{\delta}\_{m}} constant and compare the performance of each investment strategy in the part.

Generate N0=500,Nm=(m+1)​N0N\_{0}=500,\ N\_{m}=(m+1)N\_{0} samples for each dataset and use the final 5050 samples to do the out-of-sample forecasting. Repeat the total process 100100 times. Set hh to be N0/5N\_{0}/5. As we incrementally increase ρ\rho to 1010, the S​S​RSSR values computed using each strategy are presented in [Figure 3](https://arxiv.org/html/2511.21221v1#S3.F3 "Figure 3 ‣ 3.3.1 Investment performance under varying divergence ‣ 3.3 Simulation 1: Benchmark DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning").

![Refer to caption](x4.png)

Figure 3: The investment effect of each portfolio strategy

This figure presents a comparative analysis of S​S​RSSR across T​LTL strategy (red dashed line with circular markers), T​Le​q​u​a​lTL\_{equal} strategy (blue solid line with left-pointing triangular markers), N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy (orange solid line with right-pointing triangular markers) and P​o​o​lPool strategy (gray solid line with star markers) as the divergence parameter ρ\rho increases from 11 to 1010. The parameter ρ\rho modulates the distributional discrepancy between the non-informative source datasets S2S\_{2}, S3S\_{3}, S4S\_{4} and the target data TT systematically.

As evidenced by [Figure 3](https://arxiv.org/html/2511.21221v1#S3.F3 "Figure 3 ‣ 3.3.1 Investment performance under varying divergence ‣ 3.3 Simulation 1: Benchmark DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning"), the T​LTL strategy consistently achieves the maximal S​S​RSSR values among these investment strategies. Notably, the performance of the P​o​o​lPool strategy deteriorates progressively as ρ\rho increases, suggesting that indiscriminate data merging becomes increasingly suboptimal when the divergence between the source and target data increases. Both the T​LTL strategy and the T​Le​q​u​a​lTL\_{equal} strategy exhibit a decreasing efficacy with increasing ρ\rho, although T​LTL strategy maintains superior performance throughout. This shows that the targeted utilization of source data information, rather than naive aggregation, is crucial to optimize the investment decisions of the target assets and enhance the returns. Furthermore, the comparison of the T​LTL and N​o​n−t​r​a​n​s​f​e​rNon-transfer strategies reveals that the performance gap in S​S​RSSR decreases as ρ\rho increases, but the gap between the two strategies never vanishes. Accordingly, we investigate the investment performance for each strategy using only the non-informative source datasets S2S\_{2}, S3S\_{3} and S4S\_{4} when N0=500N\_{0}=500. As evidenced by [Figure 4](https://arxiv.org/html/2511.21221v1#S3.F4 "Figure 4 ‣ 3.3.1 Investment performance under varying divergence ‣ 3.3 Simulation 1: Benchmark DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning"), when utilizing only the non-informative datasets, the T​LTL strategy slightly outperforms the N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy at ρ=1\rho=1. However, its performance deteriorates as ρ\rho increases. Once ρ\rho exceeds 22, the N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy emerges as superior, rendering the T​LTL strategy suboptimal under these conditions.

![Refer to caption](x5.png)

Figure 4: The investment effect of each portfolio strategy while only utilizing the non-informative datasets S2S\_{2}, S3S\_{3} and S4S\_{4}

This figure presents the S​S​RSSR across T​LTL strategy (red dashed line with circular markers), T​Le​q​u​a​lTL\_{equal} strategy (blue solid line with left-pointing triangular markers), N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy (orange solid line with right-pointing triangular markers) and P​o​o​lPool strategy (gray solid line with star markers) as the divergence parameter ρ\rho increases from 11 to 1010 while utilizing the non-informative datasets S2S\_{2}, S3S\_{3} and S4S\_{4} when N0=500N\_{0}=500.

#### 3.3.2 Validity of the convergence of weight

To evaluate the capability to autonomously identify the datasets which can provide effective information for the target of the proposed T​LTL strategy, we calculate Γ​(𝒘^)\Gamma(\widehat{\bm{w}}) at N0+1N\_{0}+1 across varying sample sizes in this part.

Under different N0N\_{0}, set hh to be N0/5N\_{0}/5, Nm=(m+1)​N0N\_{m}=(m+1)N\_{0} and ρ\rho to be 33. Let N0N\_{0} be in the set {300,500,800,1000,1200,1500,2000,4000,8000,16000,40000}\{300,500,800,1000,1200,1500,2000,4000,8000,16000,40000\}. It can be seen that 𝒟={0,1,5}\mathcal{D}=\{0,1,5\}, so Γ​(𝒘^)=w^0+w^1+w^5\Gamma(\widehat{\bm{w}})=\widehat{w}\_{0}+\widehat{w}\_{1}+\widehat{w}\_{5}. Using the specified experimental configuration, we generate synthetic datasets and evaluate Γ​(𝒘^)\Gamma(\widehat{\bm{w}}) for target data at time N0+1N\_{0}+1. Repeat the whole procedure 10001000 times.

![Refer to caption](x6.png)

Figure 5: Γ​(𝒘^)\Gamma(\widehat{\bm{w}}) under different hh

This figure demonstrates the weight summation assigned to the datasets that can provide effective information under different estimation window hh. The gray area is calculated by adding or subtracting 1.961.96 standard error from the average value of Γ​(𝒘^)\Gamma(\widehat{\bm{w}}) in 10001000 repetitions, which exhibits the corresponding variation of Γ​(𝒘^)\Gamma(\widehat{\bm{w}}) in different hh.

[Figure 5](https://arxiv.org/html/2511.21221v1#S3.F5 "Figure 5 ‣ 3.3.2 Validity of the convergence of weight ‣ 3.3 Simulation 1: Benchmark DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning") shows Γ​(𝒘^)\Gamma(\widehat{\bm{w}}) across different hh. As shown, the aggregated weights assigned to informative datasets monotonically increase with sample size, asymptotically approaching 11. This empirical result strongly corroborates the theoretical convergence established in [Theorem 1](https://arxiv.org/html/2511.21221v1#Thmtheorem1 "Theorem 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning").

![Refer to caption](x7.png)

Figure 6: The box plots of S​S​RSSR obtained by various strategies

This figure demonstrates box plots comparing S​S​RSSR across T​LTL strategy (red box plot), T​Le​q​u​a​lTL\_{equal} strategy (blue box plot), N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy (orange box plot) and P​o​o​lPool strategy (gray box plot). The horizontal lines within each box plot represent the sample mean of S​S​RSSR computed over 100100 simulation replicates, while the box widths correspond to the inter-quartile ranges, illustrating the variance in S​S​RSSR performance for each strategy.

#### 3.3.3 Comparison of the variance

We further evaluate the performance of each strategy by computing S​S​RSSR. For N0=5000N\_{0}=5000, use h=N0/5h=N\_{0}/5, Nm=(m+1)​N0N\_{m}=(m+1)N\_{0}, respectively. The accuracy of the out-of-sample forecasting is evaluated using the final 10001000 target observations. From [Figure 6](https://arxiv.org/html/2511.21221v1#S3.F6 "Figure 6 ‣ 3.3.2 Validity of the convergence of weight ‣ 3.3 Simulation 1: Benchmark DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning"), a smaller variance can be observed in the index S​S​RSSR when using the T​LTL strategy relative to other strategies, which can verify the conclusion of [Theorem 3](https://arxiv.org/html/2511.21221v1#Thmtheorem3 "Theorem 3. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning") in this article. Under [Assumption 1](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning"), we can show that the index S​S​RSSR converges almost surely to S​R~0,N0+1​(𝒘^)\widetilde{SR}\_{0,N\_{0}+1}(\widehat{\bm{w}}) as N0N\_{0} and the cardinality of 𝒪\mathcal{O} approaches infinity. Furthermore, leveraging the stationarity property of the target dataset, we can explicitly compute its population mean and covariance parameters. This enables the determination of the theoretically optimal Sharpe ratio, which is found to be 0.6380.638 for this target domain.

#### 3.3.4 Investment performance comparison: TL vs. TLc

To further evaluate the performance of our strategy, we conduct a comparative analysis with the portfolio optimization strategy based on transfer learning proposed in cao2023ssrn. Their strategy incorporates the information from the source domain through a corrective framework, solving the following optimization problem to determine the optimal asset allocations.

|  |  |  |
| --- | --- | --- |
|  | ϕ^T=arg⁡maxϕ∈Φ​𝝁^T⊤​ϕϕ⊤​𝚺^T​ϕ−λ​‖ϕ^S−ϕ‖22,\widehat{\bm{\phi}}\_{T}=\underset{\bm{\phi}\in\Phi}{\arg\max}\frac{\widehat{\bm{\mu}}\_{T}^{\top}\bm{\phi}}{\sqrt{\bm{\phi}^{\top}\widehat{\bm{\Sigma}}\_{T}\bm{\phi}}}-\lambda\left\|\widehat{\bm{\phi}}\_{S}-\bm{\phi}\right\|\_{2}^{2}, |  |

where ϕ^T\widehat{\bm{\phi}}\_{T}
denotes the asset allocation of the target data and ϕ^S\widehat{\bm{\phi}}\_{S} denotes the asset allocation of the source data estimated using the N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy. 𝝁^T\widehat{\bm{\mu}}\_{T} and 𝚺^T\widehat{\bm{\Sigma}}\_{T} are the historical sample mean and historical sample variance of the target data. Denote this strategy as T​L​cTLc strategy. Following cao2023ssrn, we adopt the same regularization parameter λ=0.2\lambda=0.2 for comparative analysis. Given the constraint of single-source dataset utilization of the T​L​cTLc strategy, we evaluate the performance using both the target data and the previously generated single source dataset. Set N0N\_{0} to be 500500, Nm=(m+1)​N0N\_{m}=(m+1)N\_{0} and hh to be 6060. Use the final 5050 samples to do the out-of-sample forecasting and repeat the total process 100100 times.

We first evaluate the strategies using S1S\_{1} as the source dataset, representing the case where the source data provides effective transferable information for the target domain. Since S1S\_{1} and S5S\_{5} follow identical distributional characteristics, the choice between them is substantively inconsequential. As demonstrated in [Table 1](https://arxiv.org/html/2511.21221v1#S3.T1 "Table 1 ‣ 3.3.4 Investment performance comparison: TL vs. TLc ‣ 3.3 Simulation 1: Benchmark DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning"), the T​LTL strategy is slightly better than the T​L​cTLc strategy.

Table 1: The investment effect of each portfolio strategy across different N0N\_{0}

| strategy | S​S​RSSR |
| --- | --- |
| T​LTL | 0.550 (0.052) |
| T​Le​q​u​a​lTL\_{equal} | 0.549 (0.052) |
| N​o​n−t​r​a​n​s​f​e​rNon-transfer | 0.541 (0.051) |
| P​o​o​lPool | 0.551 (0.052) |
| T​LcTL\_{c} | 0.549 (0.052) |

This table
presents the S​S​RSSR performance comparing the proposed strategy with alternative strategies when utilizing the informative source dataset S1S\_{1}. We bold the results of the best strategy and mark the results of the suboptimal strategy in italics.

To further evaluate the performance of each strategy under non-informative source conditions, we introduce controlled variation in the source data and employ S3S\_{3} as the representative dataset. Notably, since S2S\_{2}, S3S\_{3} and S4S\_{4} share identical distributional properties, the selection among them is substantively equivalent for our comparative analysis.

![Refer to caption](x8.png)

Figure 7: The investment effect of each portfolio strategy when only utilizing the non-informative dataset S3S\_{3}

This figure presents the S​S​RSSR performance comparing the proposed T​LTL strategy (red dashed line with circular markers) with alternative T​Le​q​u​a​lTL\_{equal} strategy (blue solid line with left-pointing triangular markers), N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy (orange solid line with right-pointing triangular markers), P​o​o​lPool strategy (gray solid line with star markers) and T​L​cTLc strategy (purple solid line with upward-pointing when utilizing source dataset S3S\_{3}.

[Figure 7](https://arxiv.org/html/2511.21221v1#S3.F7 "Figure 7 ‣ 3.3.4 Investment performance comparison: TL vs. TLc ‣ 3.3 Simulation 1: Benchmark DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning") demonstrate the index S​S​RSSR of each strategy when the gap between S3S\_{3} and the target data increases when N0=500N\_{0}=500. In general, the T​LTL strategy and
N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy perform better than others. When ρ\rho is larger, T​LTL strategy is slightly inferior than the N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy. We can see that the proposed strategy consistently outperforms T​L​cTLc strategy across all ρ\rho values. Furthermore, the T​LTL, T​Le​q​u​a​lTL\_{equal}, T​L​cTLc and P​o​o​lPool strategies exhibit a monotonically decreasing performance as ρ\rho increases.

### 3.4 Simulation 2: FF3 model-based DGP

To enhance the realism of our simulated data, we use empirical market data and estimate the Fama French three factor model (F​F​3FF3) using the ordinary least squares strategy. The simulated data are then generated based on the estimated model parameters. The F​F​3FF3 model, introduced by fama1993, addresses the limitations of Capital Asset Pricing Model. Their seminal work demonstrates that the market beta alone cannot fully explain cross-sectional stock return variations while three firm-specific characteristics, denoted as market capitalization, book-to-market ratio, and earnings-to-price ratio, significantly improve explanatory power. The F​F​3FF3 model is formally specified as

|  |  |  |
| --- | --- | --- |
|  | rt−rf=α+β1​S​M​Bt+β2​H​M​Lt+β3​M​K​Tt+ϵt,r\_{t}-r\_{f}=\alpha+\beta\_{1}SMB\_{t}+\beta\_{2}HML\_{t}+\beta\_{3}MKT\_{t}+\epsilon\_{t}, |  |

where rtr\_{t} refers to the return of individual stocks and rfr\_{f} refers to the risk-free interest rate. S​M​BSMB represents the average return of the stock portfolio of small-market companies minus the average return of the stock portfolio of large-market companies (according to small-market effect). H​M​LHML refers to the portfolio return rate obtained by shorting companies with a high book value ratio and M​K​TMKT refers to the excess return of the market portfolio.
The three factors required (M​K​TMKT, S​M​BSMB, H​M​LHML) are obtained from the C​R​S​PCRSP database for the period from January 20212021 to December 20232023. For our empirical analysis, we use the daily returns of the five American real estate industries, denoted as E​X​P​IEXPI, V​I​C​IVICI, N​M​R​KNMRK, I​N​V​HINVH, and J​L​LJLL, and analyze their daily returns over the same 33 year period from January 20212021 to December 20232023 (753753 trading days). Each observation is indexed chronologically as t=1,…,753t=1,\dots,753, where t=1t=1 corresponds to January 44, 20212021 (the first trading day of 20212021). Given the daily return of the five stocks and the three factors, fit the F​F​3FF3 model and we can get the parameters 𝜶=(α1,…,α5)⊤∈R5\bm{\alpha}=(\alpha\_{1},\dots,\alpha\_{5})^{\top}\in\text{R}^{5} and {𝜷p=(β1,p,β2,p,β3,p)⊤∈R3|p=1,…,5}\{\bm{\beta}\_{p}=(\beta\_{1,p},\beta\_{2,p},\beta\_{3,p})^{\top}\in\text{R}^{3}|\ p=1,\dots,5\}, respectively.

We generate synthetic target and source data through the following DGP.

|  |  |  |
| --- | --- | --- |
|  | 𝒓m,t=𝜶+𝑿​𝚷m,t+𝒆m,t,m=0,1,…,5,t=1,…,Nm,\bm{r}\_{m,t}=\bm{\alpha}+\bm{X}\bm{\Pi}\_{m,t}+\bm{e}\_{m,t},\ m=0,1,\dots,5,\ t=1,\dots,N\_{m}, |  |

where 𝒓m,t∈R5,𝒆m,t∈R5∼MVN​(𝟎,𝛀)\bm{r}\_{m,t}\in\text{R}^{5},\ \bm{e}\_{m,t}\in\text{R}^{5}\sim\text{MVN}(\bm{0},\bm{\Omega}) and the components of the covariance matrix are 𝛀​(i,j)=0.5|i−j|\bm{\Omega}(i,j)=0.5^{|i-j|}.
For the definition of 𝑿\bm{X} and 𝚷m,t\bm{\Pi}\_{m,t}, use the following settings.

|  |  |  |
| --- | --- | --- |
|  | 𝑿=(𝜷1,𝜷2,𝜷3,𝜷4,𝜷5)⊤∈R5×3,\bm{X}=(\bm{\beta}\_{1},\bm{\beta}\_{2},\bm{\beta}\_{3},\bm{\beta}\_{4},\bm{\beta}\_{5})^{\top}\in\text{R}^{5\times 3}, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝚷m,t=(S​M​Bt,H​M​Lt,M​K​Tt)⊤,m=0,t=1,…,N0,\bm{\Pi}\_{m,t}=(SMB\_{t},HML\_{t},MKT\_{t})^{\top},\ m=0,\ t=1,\dots,N\_{0}, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝚷m,t=(S​M​Bt,H​M​Lt,M​K​Tt)⊤+1t×ϵm,t,m=1,5,t=1,…,Nm,\bm{\Pi}\_{m,t}=(SMB\_{t},HML\_{t},MKT\_{t})^{\top}+\frac{1}{t}\times\bm{\epsilon}\_{m,t},\ m=1,5,\ t=1,\dots,N\_{m}, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝚷m,t=(S​M​Bt,H​M​Lt,M​K​Tt)⊤+ρ×ϵm,t,m=2,3,4,t=1,…,Nm,\bm{\Pi}\_{m,t}=(SMB\_{t},HML\_{t},MKT\_{t})^{\top}+\rho\times\bm{\epsilon}\_{m,t},\ m=2,3,4,\ t=1,\dots,N\_{m}, |  |

where ϵm,t∈R3∼MVN​(𝟎,0.1​𝑰)\bm{\epsilon}\_{m,t}\in\text{R}^{3}\sim\text{MVN}(\bm{0},0.1\bm{I}).

Generate N0=⋯=N5=500N\_{0}=\dots=N\_{5}=500 samples for each dataset. Take h=N0/5h=N\_{0}/5 and use the final 5050 samples to do the out-of-sample forecasting. Repeat the total process 100100 times.222To ensure temporal consistency across all datasets, we maintain identical sample sizes for both the factor data and stock returns in our simulation.

![Refer to caption](x9.png)

Figure 8: The investment effect of each portfolio strategy

This figure presents a comparative analysis of S​S​RSSR across T​LTL strategy (red dashed line with circular markers), T​Le​q​u​a​lTL\_{equal} strategy (blue solid line with left-pointing triangular markers), N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy (orange solid line with right-pointing triangular markers) and P​o​o​lPool strategy (gray solid line with star markers) as the divergence parameter ρ\rho increases from 11 to 1010. The parameters for the DGP of each dataset are determined by fitting the F​F​3FF3 model. The parameter ρ\rho systematically modulates the distributional discrepancy between the non-informative source datasets S2S\_{2}, S3S\_{3}, S4S\_{4} and the target data TT.

[Figure 8](https://arxiv.org/html/2511.21221v1#S3.F8 "Figure 8 ‣ 3.4 Simulation 2: FF3 model-based DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning") presents S​S​RSSR performance across all evaluated strategies, using parameters calibrated from empirical market data. These findings are consistent with the results presented in [Figure 3](https://arxiv.org/html/2511.21221v1#S3.F3 "Figure 3 ‣ 3.3.1 Investment performance under varying divergence ‣ 3.3 Simulation 1: Benchmark DGP ‣ 3 Simulation studies ‣ Portfolio Optimization via Transfer Learning"). As shown, our approach demonstrates a clear advantage. Furthermore, the data generated for each dataset in this simulation do not necessarily satisfy [Assumption 1](https://arxiv.org/html/2511.21221v1#Thmassumption1 "Assumption 1. ‣ 2 Asymptotic properties ‣ Portfolio Optimization via Transfer Learning"). Despite this relaxation, the proposed T​LTL strategy still has obvious advantages, which also reflects the robustness of our strategy.

## 4 Applications

We evaluate the performance of our strategy using two distinct datasets: one comprising dual-listed A-share and H-share stocks, and the other consisting of stocks from various industrial sectors of the United States. The results based on the two stock universes are reported in [Section 4.1](https://arxiv.org/html/2511.21221v1#S4.SS1 "4.1 Optimizing portfolios across H-shares and A-shares ‣ 4 Applications ‣ Portfolio Optimization via Transfer Learning") and [Section 4.2](https://arxiv.org/html/2511.21221v1#S4.SS2 "4.2 Optimizing portfolios across sectors ‣ 4 Applications ‣ Portfolio Optimization via Transfer Learning"), respectively.

### 4.1 Optimizing portfolios across H-shares and A-shares

Many leading Chinese enterprises are dually listed on both the Shanghai/Shenzhen Stock Exchanges (A-shares) and the Hong Kong Stock Exchange (H-shares). This arrangement offers a valuable natural laboratory for our research. Although A-shares and H-shares represent claims on the same underlying firms, differences in investor composition, market regulations, and capital controls cause them to exhibit distinct price discovery dynamics and risk appetite. Rather than being mere noise, these differences create a solid foundation for informational complementarity.

From the perspective of using Hong Kong market data to inform A-share analysis, the highly internationalized and institution-dominated Hong Kong market tends to respond more swiftly and accurately to global macroeconomic trends, geopolitical developments, and sector-specific shifts. As a result, H-share price movements often incorporate global information that has not yet been fully reflected in the more retail-driven and relatively insulated A-share market. Incorporating H-share returns as a leading indicator into predictive models acts as an effective information set, capturing globally sourced fundamental changes and thereby improving the foresight and accuracy of A-share return forecasts. For example, in the cases of commodity firms or large technology companies, H-share prices may earlier reflect shifts in global supply-demand conditions or technological disruptions, thereby aiding in the more precise estimation of subsequent A-share performance.

Conversely, using A-shares data to interpret H-shares dynamics is equally valuable. The A-share market, with its substantial retail investor presence, serves as a direct barometer of domestic investor sentiment and reactions to local policy changes. Subtle shifts relating to local consumption trends, industrial policies, or regional risks often emerge first in A-share prices. For Mainland companies listed in Hong Kong, these locally-driven sentiments and expectations represent critical dimensions that international investors may overlook or respond to with a lag. Thus, A-share return dynamics provide essential information for understanding H-shares behavior.

Through bidirectional modeling, researchers can better disentangle global versus local drivers of firm value. This approach facilitates a deeper analysis of the the asset returns. In summary, integrating data from both markets combines two distinct information sets to form a more comprehensive and robust view of the target asset. We collect earnings data for five listed companies from four sectors: Energy, Manufacturing, Finance, and Medical, across both H-shares and A-shares. See Appendix G for the detailed information of the listed companies.

Table 2: The investment effect of each portfolio strategy in different target markets

| Strategy  Target market | Energy | | Manufacturing | |
| --- | --- | --- | --- | --- |
| A-shares | H-shares | A-shares | H-shares |
| T​LTL | 0.129 | 0.448 | 0.138 | 0.191 |
| T​Le​q​u​a​lTL\_{equal} | 0.101 | 0.394 | 0.118 | 0.149 |
| N​o​n−t​r​a​n​s​f​e​rNon-transfer | 0.128 | 0.364 | 0.124 | 0.196 |
| P​o​o​lPool | 0.111 | 0.358 | 0.069 | 0.175 |
| T​L​cTLc | 0.085 | 0.413 | 0.093 | 0.185 |
| Strategy  Target market | Financial | | Medical | |
| A-shares | H-shares | A-shares | H-shares |
| T​LTL | 0.132 | 0.244 | 0.186 | 0.968 |
| T​Le​q​u​a​lTL\_{equal} | 0.125 | 0.237 | 0.177 | 0.728 |
| N​o​n−t​r​a​n​s​f​e​rNon-transfer | 0.130 | 0.219 | 0.183 | 0.753 |
| P​o​o​lPool | 0.113 | 0.252 | 0.154 | 0.651 |
| T​L​cTLc | 0.131 | 0.241 | 0.148 | 0.553 |

This table demonstrates the S​S​RSSR index gained using the proposed strategy and the alternative strategies when investing in five listed companies from four sectors: Energy, Manufacturing, Finance, and Medical, across both H-shares and A-shares. For the convenience of comparison, we bold the results of the best strategy and mark the results of the suboptimal strategy in italics.

Our analysis alternately designates one market as the target and the other as the source market. Take their daily return from July 2021 to June 2025 for analysis and the data from January 2025 to June 2025 are used to make out-of-sample forecasts. In detail, every dataset covers 968968 time periods and |𝒪|=117|\mathcal{O}|=117. The data information comes from C​o​m​p​u​s​t​a​tCompustat database. Building on these comprehensive datasets, we conduct a comparative performance analysis between our proposed strategy and established benchmark strategies for the construction of the target assets portfolio. [Table 2](https://arxiv.org/html/2511.21221v1#S4.T2 "Table 2 ‣ 4.1 Optimizing portfolios across H-shares and A-shares ‣ 4 Applications ‣ Portfolio Optimization via Transfer Learning") presents the comparative performance of portfolio strategies across different industry sectors. Overall, the method proposed in this article has performed quite well when investing in the H-shares and A-shares of different industries. The complementary nature of the information between these two markets can generate substantial added value for investors. [Table 3](https://arxiv.org/html/2511.21221v1#S4.T3 "Table 3 ‣ 4.1 Optimizing portfolios across H-shares and A-shares ‣ 4 Applications ‣ Portfolio Optimization via Transfer Learning") demonstrates the average transferring weight of different target markets within the period of out-of-sample forecasting when the T​LTL strategy is adopted. As shown, the source dataset has been effectively utilized in the T​LTL strategy we proposed.

Table 3: The average transferring weight of different target markets when T​LTL strategy is adopted

| Target market  Weights | | w0w\_{0} | w1w\_{1} |
| --- | --- | --- | --- |
| Energy | A-shares | 0.970 | 0.030 |
| H-shares | 0.632 | 0.368 |
| Manufacturing | A-shares | 0.854 | 0.146 |
| H-shares | 0.837 | 0.163 |
| Financial | A-shares | 0.751 | 0.249 |
| H-shares | 0.872 | 0.128 |
| Medical | A-shares | 0.852 | 0.148 |
| H-shares | 0.743 | 0.257 |

This table demonstrates the average transferring weight of different target markets within the period of out-of-sample forecasting when the T​LTL strategy is adopted. As mentioned before, w0w\_{0} is the weight assigned in the target market and w1w\_{1} is the weight assigned in the source market.

### 4.2 Optimizing portfolios across sectors

The real estate sector constitutes a fundamental pillar of modern economic systemsand plays a critical role in both developed and emerging economies. As a tangible assetclass, residential properties provide not only shelter but also represent one of the mostsigniffcant components of household wealth portfolios globally. The sector also offersmultiple pathways for value creation, including capital appreciation through strategicacquisitions and stable income generation via rental operations. As a linchpin sector with extensive backward and forward links, real estate exhibitsremarkable stimulating effects across upstream industries (e.g., construction materials,steel production, and heavy machinery) and downstream sectors (e.g., interior design,home furnishings, and appliance manufacturing). The financial phenomenon between different sectors became particularly evident during the global ffnancial crisis in 2008,where mortgage-backed securities and real estate derivatives ampliffed systemic riskthrough complex ffnancial channels. This intricate web of inter-sectoral dependenciesraises a critical research question: can stock return data from correlated sectors beleveraged to enhance the investment performance of the interested market?

Table 4: The investment effect of each portfolio strategy in different target markets

|  | Real Estate | Financial | Construction |
| --- | --- | --- | --- |
| T​LTL | 0.129 | 0.354 | 0.089 |
| T​Le​q​u​a​lTL\_{equal} | 0.162 | 0.199 | 0.064 |
| N​o​n−t​r​a​n​s​f​e​rNon-transfer | -0.004 | 0.198 | -0.072 |
| P​o​o​lPool | 0.015 | 0.161 | 0.020 |
|  | Furniture | Manufacturing | Marketing |
| T​LTL | -0.002 | 0.181 | 0.084 |
| T​Le​q​u​a​lTL\_{equal} | -0.018 | 0.129 | 0.029 |
| N​o​n−t​r​a​n​s​f​e​rNon-transfer | -0.046 | -0.012 | 0.053 |
| P​o​o​lPool | -0.090 | 0.303 | -0.001 |

This table demonstrates the S​S​RSSR performance comparing our proposed strategy with alternative strategies when investing in the real estate industry, financial industry, construction industry, furniture industry, manufacturing industry and marketing industry in the American stock market. In each setting, we bold the results of the best strategy and mark the results of the suboptimal strategy in italics.

We implement a comprehensive cross-sector analysis using the real estate industry
data, financial industry data, construction industry data, furniture industry data, manufacturing industry data and marketing industry data in American stock market, systematically rotating each industry sector as the target domain while employing all other sectors as source domains. Select the five largest market capitalization stocks from both target and the source industries. Take their daily return from January 20202020 to December 20232023 for analysis and the data from October 20232023 to December 20232023 are used to make out-of-sample forecasts. In detail, every dataset covers 877877 time periods and |𝒪|=63|\mathcal{O}|=63. The data information comes from O​s​i​r​i​sOsiris, C​R​S​PCRSP and C​o​m​p​u​s​t​a​tCompustat database. Building on these comprehensive datasets, we conduct a comparative performance
analysis between our proposed strategy and established benchmark strategies for the construction of the target assets portfolio.

Table 5: The average transferring weight of each dataset when T​LTL strategy is adopted in different target markets

| Target market | Real Estate | Financial | Construction |
| --- | --- | --- | --- |
| Real Estate | 0.523 | 0.236 | 0.061 |
| Financial | 0.175 | 0.451 | 0.018 |
| Construction | 0.000 | 0.058 | 0.349 |
| Furniture | 0.243 | 0.255 | 0.000 |
| Manufacture | 0.000 | 0.000 | 0.519 |
| Marketing | 0.059 | 0.000 | 0.053 |
| Target market | Furniture | Manufacture | Marketing |
| Real Estate | 0.219 | 0.047 | 0.034 |
| Financial | 0.000 | 0.000 | 0.000 |
| Construction | 0.000 | 0.514 | 0.218 |
| Furniture | 0.781 | 0.008 | 0.082 |
| Manufacture | 0.000 | 0.431 | 0.638 |
| Marketing | 0.000 | 0.000 | 0.028 |

This table demonstrates the average transferring weight of different target markets within the period of out-of-sample forecasting when the T​LTL strategy is adopted. Each column of this table quantifies the transferring weight of each dataset (listed on the left) when a specific dataset serves as the target.

[Table 4](https://arxiv.org/html/2511.21221v1#S4.T4 "Table 4 ‣ 4.2 Optimizing portfolios across sectors ‣ 4 Applications ‣ Portfolio Optimization via Transfer Learning") presents the comparative performance
of portfolio strategies across different industry sectors. The TL strategy achieves either optimal or near-optimal S​S​RSSR in the tested industry pairs, while N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy consistently underperforms. These findings provide robust empirical evidence that cross-industry data in American equity markets contain economically significant predictive signals for investment decision making. [Table 5](https://arxiv.org/html/2511.21221v1#S4.T5 "Table 5 ‣ 4.2 Optimizing portfolios across sectors ‣ 4 Applications ‣ Portfolio Optimization via Transfer Learning") demonstrates the average transferring weight of different target markets within the period of out-of-sample forecasting when the T​LTL strategy is adopted. As shown, the source dataset in this example has also been effectively utilized in the T​LTL strategy we proposed.

## 5 Conclusion

In this article, we develop a novel transfer learning framework for portfolio optimization that systematically leverages cross-domain information to improve the investment performance of the target. Our theoretical analysis establishes that the proposed strategy possesses the weight consistency property and asymptotically achieves the maximum Sharpe ratio while maintaining a smaller variance than the conventional N​o​n−t​r​a​n​s​f​e​rNon-transfer strategy. The proposed strategy is relatively simple and easy to implement.

This study adopts the Sharpe ratio as our primary performance metric, which differs from the conventional mean-variance framework prevalent in the literature. In the absence of estimation errors, the Sharpe ratio maximization and utility maximization are equivalent. But the Sharpe ratio is simpler because it does not require information about risk aversion parameters and is widely used by researchers and practitioners to compare trading strategies and models. In our implementation, we set the parameter h=N0/5h=N\_{0}/5. Importantly, the theoretical guarantees of the proposed T​LTL strategy remain valid even when N0/h→∞N\_{0}/h\rightarrow\infty, as demonstrated in the Appendix. Although the choice of hh does not affect the theoretical properties of the strategy, determining its optimal selection remains an open question with considerable research significance, offering a promising direction for future investigations.