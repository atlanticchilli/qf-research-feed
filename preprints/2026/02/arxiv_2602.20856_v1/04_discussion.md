---
authors:
- Doron Avramov
- Xin He
doc_id: arxiv:2602.20856v1
family_id: arxiv:2602.20856
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to
  Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman,
  Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu,
  Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion,
  Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang,
  Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou,
  Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem,
  Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance
  and Economics, University of Science and Technology of China, Xiamen University,
  Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech,
  AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference
  on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop
  2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions
  and feedback. The authors acknowledge financial support from Inquire Europe. Avramov
  (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel.
  He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China.
  All authors contributed equally to this work.'
url_abs: http://arxiv.org/abs/2602.20856v1
url_html: https://arxiv.org/html/2602.20856v1
venue: arXiv q-fin
version: 1
year: 2026
---


Doron Avramov
  
Reichman University (IDC), Herzliya, Israel
  
Xin He
  
University of Science and Technology of China

(February 24, 2026)

###### Abstract

This paper develops a unified framework that links firm-level predictive signals, cross-asset spillovers, and the stochastic discount factor (SDF). Signals and spillovers are jointly estimated by maximizing the Sharpe ratio, yielding an interpretable SDF that both ranks characteristic relevance and uncovers the direction of predictive influence across assets. Out-of-sample, the SDF consistently outperforms self-predictive and expected-return benchmarks across investment universes and market states. The inferred information network highlights large, low-turnover firms as net transmitters. The framework offers a clear, economically grounded view of the informational architecture underlying cross-sectional return dynamics.

Key Words:
Asset Pricing,
Connection Matrix,
Cross-Asset Spillover,
Sharpe Ratio,
Stochastic Discount Factor.

JEL classification: C1, G11, G12.

## 1 Introduction

The central objective of empirical asset pricing is to identify firm-level signals that explain the cross-section of expected stock returns—whether through exposure to risk factors or persistent mispricing. The dominant paradigm, grounded in the assumption of self-predictability, asserts that a firm’s own characteristics forecast its own returns (see, e.g., cochrane2011presidential; harvey2016and). Complementing this view is a growing literature on cross-predictability—the idea that the characteristics or returns of one asset can help forecast the returns of others (see, e.g., lo1990contrarian; hou2007industry; cohen2008economic; cohen2012complicated; huang2021psychological; huang2022frog). A key mechanism underpinning this phenomenon is the presence of lead–lag effects, whereby price movements or information from one firm precede and predict those of related firms. Such effects can stem from staggered information diffusion, peer influence within industries, supply chain linkages, or correlated trading by institutional investors that induces price pressure across related assets.

Despite recent methodological advances in modeling cross-stock predictability, several foundational questions remain unresolved. Chief among them is how a mean–variance investor can analytically integrate multiple predictive signals when returns are interconnected across assets. Equally crucial is developing a framework that jointly captures both the relevance of individual signals and the structure of return spillovers—enhancing portfolio performance while preserving interpretability.

This paper addresses these questions by proposing a unified and systematic framework for constructing maximum–Sharpe ratio strategies. We combine firm-level signals through a flexible weighting vector (the signal-aggregation vector Λ\Lambda) and model cross-asset spillovers using a structured connection matrix (the spillover matrix Ψ\Psi). The resulting optimal strategy admits a transparent analytical characterization. This formulation naturally connects to the stochastic discount factor (SDF; see hansen1991implications; cochrane2009asset; back2017asset), which, in this context, takes the form of a single factor that prices the cross-section of returns.

An important distinction in the asset pricing literature lies between conditional and unconditional Sharpe ratio optimization. As emphasized by hansen1987role, conditional optimization targets the best return–risk trade-off at each point in time using the information then available, whereas unconditional optimization maximizes this trade-off in expectation using long-run moments.111See also lewellen2006, who emphasize the distinction between conditional and unconditional beta pricing.
Our framework follows the latter approach: while it incorporates time-varying signals—such as firm characteristics and cross-asset linkages—the stochastic discount factor is optimized to perform well on average over time. This orientation prioritizes long-horizon performance over period-by-period efficiency, yielding strategies that are transparent, robust, and empirically grounded.

While the analytical formulation provides a population-level characterization of the Sharpe-optimal SDF, our empirical implementation uses a regression-based procedure tailored for high-dimensional applications. We build on the approach of britten1999sampling and employ ridge-type regularization—with a single tuning parameter λ\lambda chosen by five-fold cross-validation—to estimate both the signal weights and the connection matrix. This method converges to the theoretical solution in large samples while enhancing numerical stability and interpretability. Unlike expected return-maximization—which, under certain specifications, can lead to extreme concentration in a single predictor—Sharpe ratio-maximization encourages diversification across signals, thereby enhancing robustness and practical relevance.

To build intuition, we start with a low-dimensional toy example using five well-known firm characteristics and nine portfolios sorted by size and book-to-market. This simplified setting enables us to illustrate the estimated signal weights, cross-asset linkages, and resulting trading strategy in full detail. We evaluate performance with a rolling out-of-sample procedure, re-estimating the strategy each month using the prior 10 years of data. Even in this controlled environment, the maximum–Sharpe ratio strategy based on cross-stock predictability attains an annualized Sharpe ratio of 1.22, compared with 0.60 for the self-predictive benchmark—an improvement driven simultaneously by cross-asset spillovers, shifts in signal relevance, and their interaction.

We then scale the framework to a comprehensive empirical setting using 138 firm-level signals from the jensen2023there dataset. Our primary investment universe consists of 138 univariate spread portfolios spanning 1963–2023. We also consider a broader set of 544 bivariate portfolios sorted by firm size and a secondary characteristic. Applying the same rolling 10-year estimation scheme, the maximum–Sharpe ratio (MS) strategy attains annualized Sharpe ratios of 2.21 and 3.32 on the spread and bi-sort portfolios, respectively—consistently outperforming both self-predictive benchmarks and maximum-expected return (MR) strategies.
Specifically, the Sharpe ratio of our cross-predictive SDF strategy exceeds that of a self-predictive Sharpe ratio–maximizing benchmark by 0.79 on spread portfolios and more than 1.26 on bi-sorted portfolios—translating into economically meaningful gains in certainty-equivalent returns. Moreover, compared to expected return–maximizing strategies, our Sharpe ratio–maximizing SDF improves risk-adjusted performance by factors of 4–10, depending on the investment universe and market regime.

To assess robustness, we evaluate performance across different market environments. We split the test sample by investor sentiment and by volatility regimes based on the VIX index. The Sharpe ratio–maximizing strategy maintains strong performance across all subsamples. For example, in high-sentiment periods, the strategy delivers a Sharpe ratio of 2.19 on spread portfolios and 3.58 on bi-sort portfolios. Even in low-sentiment or high-volatility regimes—conditions that typically challenge individual anomaly-based strategies—the strategy sustains Sharpe ratios above 2. These results contrast with the more state-dependent performance of expected return–maximizing portfolios.

The SDF defines a single factor that, ex ante, prices the cross-sectional variation in expected returns of the test assets. We evaluate whether this factor’s payoffs are priced by leading asset pricing models and find sizable, statistically significant alphas relative to a broad set of benchmarks. These include the liquidity factor pastor2003, the Fama–French five-factor model fama2015five, the q-factors hou2015, the mispricing factors stambaugh2017, the behavioral factors daniel2020short, and a comprehensive fourteen-factor model. Across all specifications, the strategy delivers alphas of about 0.25% per month with tt-statistics above 11, indicating that the return variation embedded in cross-asset spillovers is not captured by existing models.

Upon optimizing the Sharpe ratio, we uncover the underlying economic drivers of return predictability. By examining the estimated weights assigned to firm-level characteristics, we find that the most influential predictors cluster in the categories of investment, value, and profitability, with signals such as liquidity of book assets, dividend yield, and return on equity consistently receiving the highest weights. In contrast, return-based signals—including momentum, short-term reversal, and seasonality—exhibit persistently low weights. This pattern suggests that the cross-predictive SDF is primarily anchored in stable firm fundamentals rather than transitory market signals.

In optimizing the Sharpe ratio, we also obtain a connection matrix, denoted by Ψ\Psi, that encodes the predictive relationships across stocks. Each entry Ψi,j\Psi\_{i,j} reflects the extent to which signals from asset ii forecast the returns of asset jj, while diagonal elements represent self-predictive strength. Empirically, the average off-diagonal entry is substantial—often exceeding the average diagonal—indicating that cross-asset predictive linkages carry more information than self-predictive signals alone. Aggregating rows and columns of the matrix following diebold2014network, we uncover a directional structure: certain stocks consistently act as net transmitters of predictive signals, while others serve primarily as net receivers. Transmitters are typically large and low-turnover, whereas receivers tend to be smaller, high-turnover stocks with characteristics such as value orientation, high profitability, low investment activity, and strong past returns.

It is worth noting that the Sharpe ratio of the cross-predictive strategy is time-varying and declines notably after 2000. In the 1990s, the strategy delivers exceptional performance, with Sharpe ratios exceeding 2 on spread portfolios and above 4 on bi-sort portfolios. However, performance attenuates in the post-2000 period, mirroring the broader decline in self-predictability. For instance, green2017characteristics document that many anomaly portfolios become less profitable after 2003, attributing the decline to the widespread adoption of anomaly-based strategies, improved market liquidity, and the growth of passive ETF investing.

Despite this attenuation, the proposed strategy maintains strong performance from 2000 to 2023, achieving Sharpe ratios of 1.58 (spread portfolios) and 2.21 (bi-sort portfolios)—substantially higher than those of standard benchmark factors: 0.41 (market), 0.27 (size), 0.20 (value), 0.54 (profitability), 0.43 (investment), and 0.09 (momentum). By the end of 2023, five-year trailing Sharpe ratios decline to approximately 1.2 for the spread and bi-sort strategies, yet both remain consistently superior to traditional benchmarks even in recent years.

The paper proceeds as follows. Section [2](https://arxiv.org/html/2602.20856v1#S2 "2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") presents the econometric framework. Section [3](https://arxiv.org/html/2602.20856v1#S3 "3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") outlines the estimation methodology. Section [4](https://arxiv.org/html/2602.20856v1#S4 "4 Data ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") describes the data. Section [5](https://arxiv.org/html/2602.20856v1#S5 "5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") reports the empirical findings. Section [6](https://arxiv.org/html/2602.20856v1#S6 "6 Conclusion ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") concludes.

## 2 Econometric Framework

We consider an investment universe consisting of NN risky assets. At each time tt, the investor observes a signal matrix St∈ℝN×MS\_{t}\in\mathbb{R}^{N\times M}, where each row corresponds to one asset and contains MM predictive characteristics (e.g., size, valuation, profitability, investment, past returns). Each column of StS\_{t} is cross-sectionally standardized to have zero mean and unit variance. Although our framework allows for a time-varying number of assets, the empirical analysis focuses on a fixed cross-section of sorted portfolios. We define t=1t=1 as the first period in which signals are observed, and t=T+1t=T+1 as the final period in which asset returns are realized.

### 2.1 Trading Strategy

A linear strategy that incorporates multiple signals and cross-predictability is specified as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωt′=Λ′​St′​Ψ,\omega\_{t}^{\prime}=\Lambda^{\prime}\,S\_{t}^{\prime}\,\Psi, |  | (1) |

where ωt∈ℝN\omega\_{t}\in\mathbb{R}^{N} denotes the portfolio weights, Λ∈ℝM\Lambda\in\mathbb{R}^{M} assigns loadings to each signal, and Ψ∈ℝN×N\Psi\in\mathbb{R}^{N\times N} encodes how signals from one asset influence positions across all assets. Specifically, the weight on asset ii is determined by multiplying Λ′\Lambda^{\prime}, St′S\_{t}^{\prime}, and the iith column of Ψ\Psi, allowing all signals in StS\_{t} to contribute to each asset’s position. The element Ψi,j\Psi\_{i,j} quantifies the predictive impact of asset ii’s signals on asset jj.

Relative to brandt2009parametric, who model portfolio weights as a function of firm-specific attributes, our framework generalizes the approach by allowing economically meaningful cross-asset spillovers to shape portfolio allocations. Moreover, although we focus on linear strategies, the framework readily accommodates nonlinear extensions by enriching the signal matrix with polynomial or Fourier-based transformations.
For instance, one can construct an expanded signal matrix of dimension N×M​PN\times MP, where the first N×MN\times M block corresponds to the original StS\_{t}, the second to its elementwise square, and subsequent blocks to higher-order transformations up to the PPth power. Importantly, such extensions preserve the dimension of the Ψ\Psi matrix, while the
Λ\Lambda vector expands accordingly to accommodate the enlarged set of predictors—including higher-order powers of the original signals. We leave the formal development and empirical implementation of such nonlinear extensions to future research.

We construct managed-portfolio returns in excess of the risk-free rate by interacting future returns with the current values of predictive signals:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πs=(IN⊗rs)​St,\Pi\_{s}=\bigl(I\_{N}\otimes r\_{s}\bigr)\,S\_{t}, |  | (2) |

where Πs\Pi\_{s} is an N2×MN^{2}\times M matrix of managed-portfolio returns, INI\_{N} is the N×NN\times N identity matrix, rsr\_{s} is a vector of NN excess returns realized at time s>ts>t, and ⊗\otimes denotes the Kronecker product.

The expected returns on these managed-portfolios are then defined as Π=E​[Πs]\Pi=E\bigl[\Pi\_{s}\bigr]. Additionally, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ=vec​(Ψ′),\Phi=\mathrm{vec}\bigl(\Psi^{\prime}\bigr), |  | (3) |

so that Φ∈ℝN2\Phi\in\mathbb{R}^{N^{2}}. The vectorized Φ\Phi and the matrix Π\Pi streamline later expressions for portfolio outcomes.

To aid interpretation, limit extreme equity positions, and stabilize estimation, we impose Euclidean norm constraints on key parameters. Specifically, we set

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ′​Λ=1,Φ′​Φ=1,\Lambda^{\prime}\Lambda=1,\quad\Phi^{\prime}\Phi=1, |  | (4) |

where the Euclidean norm constraint on the vector Φ\Phi is equivalent to a Frobenius norm constraint on the matrix Ψ\Psi. From a Bayesian perspective, these constraints correspond to zero-mean Gaussian priors on Λ\Lambda and Φ\Phi, inducing ridge-type regularization that penalizes large parameter values.

Proposition [1](https://arxiv.org/html/2602.20856v1#Thmproposition1 "Proposition 1. ‣ 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") formulates the realized return of the strategy in a convenient form, along with the expected return and Sharpe ratio. Appendix [A](https://arxiv.org/html/2602.20856v1#A1 "Appendix A Proof of Proposition 1 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") provides the proof.

###### Proposition 1.

The investment metrics are as follows:

* •

  The realized and expected returns can be expressed as

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  |  | πs=Λ′​Πs​Φ,\displaystyle\pi\_{s}=\Lambda^{\prime}\Pi\_{s}\Phi, |  | (5) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  |  | E​(πs)=Λ′​Π​Φ.\displaystyle E(\pi\_{s})=\Lambda^{\prime}\Pi\Phi. |  | (6) |
* •

  The square of the Sharpe Ratio (S​R2SR^{2}) is given by the following two equivalent expressions:

  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | S​R2\displaystyle SR^{2} | =\displaystyle= | Λ′​AΦ​ΛΛ′​BΦ​Λ,\displaystyle\frac{\Lambda^{\prime}A\_{\Phi}\Lambda}{\Lambda^{\prime}B\_{\Phi}\Lambda}, |  | (7) |
  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | S​R2\displaystyle SR^{2} | =\displaystyle= | Φ′​AΛ​ΦΦ′​BΛ​Φ.\displaystyle\frac{\Phi^{\prime}A\_{\Lambda}\Phi}{\Phi^{\prime}B\_{\Lambda}\Phi}. |  | (8) |

  Here, AΦ=Π′​Φ​Φ′​ΠA\_{\Phi}=\Pi^{\prime}\Phi\Phi^{\prime}\Pi, BΦ=(Φ′⊗IM)​ΣΦ​(Φ⊗IM)B\_{\Phi}=(\Phi^{\prime}\otimes I\_{M})\Sigma\_{\Phi}(\Phi\otimes I\_{M}), ΣΦ\Sigma\_{\Phi} is the covariance matrix of vec​(Πs′)\text{vec}(\Pi\_{s}^{\prime}), and IMI\_{M} is the identity matrix of order MM. Similarly, AΛ=Π​Λ​Λ′​Π′A\_{\Lambda}=\Pi\Lambda\Lambda^{\prime}\Pi^{\prime}, BΛ=(Λ′⊗IN2)​ΣΛ​(Λ⊗IN2)B\_{\Lambda}=\left(\Lambda^{\prime}\otimes I\_{N^{2}}\right)\Sigma\_{\Lambda}\left(\Lambda\otimes I\_{N^{2}}\right), ΣΛ\Sigma\_{\Lambda} is the covariance matrix of vec​(Πs)\text{vec}(\Pi\_{s}), and IN2I\_{N^{2}} is the identity matrix of order N2N^{2}.

We offer several remarks regarding Proposition [1](https://arxiv.org/html/2602.20856v1#Thmproposition1 "Proposition 1. ‣ 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.").

First, our empirical analysis primarily focuses on maximizing the Sharpe ratio, using expected return-maximization as a benchmark for comparison. While both objectives rely on the same expressions for expected returns, they lead to different optimal estimates for the signal weight vector Λ\Lambda and the vectorized connection matrix Ψ\Psi. In particular, expected return-maximization reduces to a bilinear optimization problem with closed-form solutions, whereas Sharpe ratio-maximization entails solving a generalized eigenvalue problem via an iterative procedure.

Importantly, maximizing the squared Sharpe ratio necessitates the use of both representations of the Sharpe ratio provided in Proposition [1](https://arxiv.org/html/2602.20856v1#Thmproposition1 "Proposition 1. ‣ 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") when estimating the optimal values of Λ\Lambda and Φ\Phi. Explicit solutions for both the expected return and Sharpe ratio-maximization problems are presented later in the paper.

Second, Proposition [1](https://arxiv.org/html/2602.20856v1#Thmproposition1 "Proposition 1. ‣ 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") makes extensive use of the vectorized form of Ψ\Psi, which fully retains the cross-predictive structure embedded in Ψ\Psi. As a result, the information content relevant for cross-predictability is entirely preserved in Φ\Phi, ensuring that the resulting strategy remains grounded in the same underlying predictive relationships.

Third, the expression for investment return offers an intuitive economic interpretation of our trading strategy. Recall that Π\Pi denotes the matrix of managed-portfolio expected returns, with each of its N2N^{2} rows representing the expected value of one asset’s return multiplied by one of the MM signals across the NN assets. Under the normalization 𝔼​[St]=0\mathbb{E}[S\_{t}]=0, Π\Pi simplifies to the covariance matrix between future asset returns and contemporaneous signal values. If characteristic mm of stock jj helps predict the future return of stock ii, the corresponding element of Π\Pi will be nonzero, reflecting this predictability.

Thus, in this framework, Λ\Lambda assigns relative weights to signals, Φ\Phi encodes cross-asset interactions, and together they operate on the matrix Π\Pi to optimize investment metrics.

Fourth, the expected return of the trading strategy can alternatively be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(πs)=∑m=1MΛm​μm,E(\pi\_{s})=\sum\_{m=1}^{M}\Lambda\_{m}\mu\_{m}, |  | (9) |

where μm=∑p=1N2Πp​m​Φp\mu\_{m}=\sum\_{p=1}^{N^{2}}\Pi\_{pm}\Phi\_{p} represents a weighted combination of portfolio expected returns, with Πp​m\Pi\_{pm} denoting the expected return of the corresponding managed-portfolio and Φp\Phi\_{p} capturing the strength of the pp-th relationship within the strategy.

This expected-return expression is informative because it demonstrates that, whether subject to an L1L\_{1} constraint or left unconstrained, the optimal solution is a corner solution: the trading strategy is entirely driven by the predictor with the largest absolute value of μm\mu\_{m}, denoted predictor jj, with |Λj|=1|\Lambda\_{j}|=1 and all other elements of Λ\Lambda equal to zero. In contrast, under an L2L\_{2} constraint, the optimal Λ\Lambda (given Φ\Phi) is proportional to the MM-vector that collects the μm\mu\_{m} values. By comparison, Sharpe ratio-maximization effectively harnesses the benefits of diversification across predictors, assigning meaningful weight to multiple signals.

In the context of expected return-maximization, he2024PPMulti extend the principal portfolios framework of kelly2023principal from a single-signal to a multi-signal setting by introducing a three-dimensional prediction tensor. Our study should not be viewed as a multi-predictor extension of principal portfolios. Rather, we propose a framework that differs in both econometric structure and economic objective. From a modeling standpoint, we focus on a two-dimensional matrix Π\Pi, where one dimension captures multiple signals and the other encodes cross-predictive relationships across assets. From an economic perspective, the proposed methodology is explicitly designed to flexibly optimize the Sharpe ratio.

Fifth, the realized return πs\pi\_{s} of the maximum-Sharpe ratio portfolio is proportional to the stochastic discount factor (SDF), as implied by the fundamental asset pricing identity (hansen1991implications; cochrane2009asset; back2017asset):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ms=1−ω′​rs,with𝔼​[Ms​rs]=0,M\_{s}=1-\omega^{\prime}r\_{s},\quad\text{with}\quad\mathbb{E}[M\_{s}r\_{s}]=0, |  | (10) |

where MsM\_{s} denotes the pricing kernel and ω\omega is the vector of slope coefficients.
Identifying the true ω\omega is challenging in finite samples due to the “limits to learning” highlighted by didisheim2024apt. While the literature has proposed various estimators of the SDF, our approach introduces a novel proxy that explicitly captures cross-asset spillovers, distinguishing it from prior work.

Sixth, kelly2023principal focus on expected return-maximization and propose an alpha-beta decomposition: the antisymmetric and symmetric components of the prediction matrix yield the principal alpha and principal exposure portfolios, respectively. Although our expected return-maximizing strategy can be cast within this framework, our Sharpe ratio-maximizing strategy—by construction—excludes alpha, consistent with the SDF interpretation in Equation ([10](https://arxiv.org/html/2602.20856v1#S2.E10 "In 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")).

Empirically, we demonstrate that expected return-maximizing and Sharpe ratio-maximizing strategies—both accounting for cross-asset spillovers—lead to substantially different outcomes. The Sharpe ratio-maximizing strategy consistently delivers significantly higher Sharpe ratios across the full sample, as well as during both expansion and contraction periods.

Next, sorting assets by the estimated weights surfaces the portfolio’s informational backbone: it ranks assets by how much they raise the strategy’s risk-adjusted payoff. High-ranked (large-weight) assets are those that sharpen the payoff of the pricing kernel in three complementary ways: they carry economically meaningful fundamentals; they occupy advantageous positions in the web of cross-asset co-movements that let the portfolio harness spillovers; and they help balance the residual risks created elsewhere in the strategy. An asset can rank highly even if its own return is not strongly predictable—when it acts as a conduit that improves how the portfolio captures cross-asset structure or when it completes the diversification needed to express valuable payoff directions more cleanly. Lower-ranked assets contribute less to efficiency either because their information is largely redundant or because they add volatility without commensurate benefit.

Finally, as shown in Appendix [B](https://arxiv.org/html/2602.20856v1#A2 "Appendix B Relating Φ to 𝐵 When 𝑀=1 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work."), the connection matrix Ψ\Psi closely aligns with the projection of stock returns onto the distinct elements of the signals.

### 2.2 Zero-Cost and Leverage Constraints

Up to this point, we have only imposed norm constraints on the strategy’s positions. However, empirical asset pricing typically requires a trading strategy, factor, or anomaly to take the form of a long-short portfolio—that is, to be zero-cost with total leverage equal to two.

The following proposition imposes this zero-cost constraint on the strategy.

###### Proposition 2.

A zero-cost trading strategy can be expressed as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ωt′\displaystyle\omega\_{t}^{\prime} | =\displaystyle= | Λ′​St′​Ψ−1N​Λ′​St′​Ψ​A,\displaystyle\Lambda^{\prime}S\_{t}^{\prime}\Psi-\frac{1}{N}\Lambda^{\prime}S\_{t}^{\prime}\Psi A, |  | (11) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | =\displaystyle= | Λ′​St′​Ψ​Θ,\displaystyle\Lambda^{\prime}S\_{t}^{\prime}\Psi\Theta, |  | (12) |

where AA is an N×NN\times N matrix, with each element set to one, and Θ\Theta = IN−1N​AI\_{N}-\frac{1}{N}A.

Notice that ωt′​ιN=0\omega\_{t}^{\prime}\iota\_{N}=0, where ιN\iota\_{N} is an NN-vector of ones. Fortunately, all previous derivations remain valid under the zero-cost constraint.

The necessary modifications are as follows. Define Πs​i=Θ​(rs​Si​t′)\Pi\_{si}=\Theta(r\_{s}S\_{it}^{\prime}) for each i=1,2,…,Ni=1,2,\ldots,N, and construct Πs\Pi\_{s} by vertically stacking Πs​i\Pi\_{si}. All investment metrics in Proposition [1](https://arxiv.org/html/2602.20856v1#Thmproposition1 "Proposition 1. ‣ 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") can then be re-derived under the zero-cost constraint.

In Appendix [C](https://arxiv.org/html/2602.20856v1#A3 "Appendix C Proof of Expected Return Reduction due to Zero-Cost Constraint ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work."), we demonstrate that the zero-cost constraint reduces the expected profitability of the trading strategy. However, this constraint is essential for ensuring comparability across strategies.

In our empirical analyses, we primarily focus on zero-cost strategies, where the long and short positions are of equal magnitude by construction. To further ensure comparability, we rescale these positions so that total portfolio leverage equals two. This adjustment aligns our strategies with standard practice in the literature (e.g., fama1993common).

## 3 Estimating the Unknown Parameters

We provide methods for estimating the unknown parameters underlying the trading strategy.

### 3.1 Maximizing Expected Return

The following proposition presents the solution for the strategy that maximizes expected return.

###### Proposition 3.

By the Singular Value Decomposition (SVD), Π\Pi can be decomposed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π=U​ΛΠ​V′,\Pi=U\Lambda\_{\Pi}V^{\prime}, |  | (13) |

where UU is an N2×N2N^{2}\times N^{2} orthogonal matrix, ΛΠ\Lambda\_{\Pi} is an N2×MN^{2}\times M diagonal matrix of singular values, and V′V^{\prime} is an M×MM\times M orthogonal matrix.

The estimated parameters that maximize expected returns are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ^=V​(:,1),\displaystyle\hat{\Lambda}=V(:,1), |  | (14) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ^=U​(:,1).\displaystyle\hat{\Phi}=U(:,1). |  | (15) |

These estimates correspond to the first singular vectors from the matrices VV and UU, respectively. This choice ensures that the optimal trading strategy leverages the directions that capture the greatest variance in the prediction matrix Π\Pi, thereby extracting the most informative signal structure. Importantly, Λ^\hat{\Lambda} and Φ^\hat{\Phi} are obtained from the singular value decomposition of the sample-based matrix Π\Pi, and should therefore be interpreted as empirical estimators rather than population parameters.

### 3.2 Maximizing Sharpe Ratio

The following propositions formulate the estimates that maximize the squared Sharpe ratio. Appendix [D](https://arxiv.org/html/2602.20856v1#A4 "Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") provides the proof and detailed derivations.

###### Proposition 4.

Assume that Φ\Phi is given. Based on ([7](https://arxiv.org/html/2602.20856v1#S2.E7 "In 2nd item ‣ Proposition 1. ‣ 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")), define

|  |  |  |  |
| --- | --- | --- | --- |
|  | CΦ=BΦ−1​AΦ.C\_{\Phi}=B\_{\Phi}^{-1}A\_{\Phi}. |  | (16) |

The optimal Λ\Lambda is the principal eigenvector Λmax\Lambda\_{\max} of the eigenvalue problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | CΦ​Λ=λ​Λ.C\_{\Phi}\,\Lambda=\lambda\,\Lambda. |  | (17) |

Similarly, assume Λ\Lambda is given. Based on Equation ([8](https://arxiv.org/html/2602.20856v1#S2.E8 "In 2nd item ‣ Proposition 1. ‣ 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")), define CΛ=BΛ−1​AΛC\_{\Lambda}=B^{-1}\_{\Lambda}A\_{\Lambda}. The optimal value for Φ\Phi is the largest eigenvector Φm​a​x\Phi\_{max} of the following eigenvalue problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CΛ​Φ=λ​Φ.C\_{\Lambda}\Phi=\lambda\Phi. |  | (18) |

The optimal solutions for Λ\Lambda and Φ\Phi are obtained by iteratively applying these two equations until convergence. We further rescale each solution to have unit norm.

In this way, we utilize both alternative expressions for the Sharpe ratio in Proposition [1](https://arxiv.org/html/2602.20856v1#Thmproposition1 "Proposition 1. ‣ 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") to iteratively estimate the optimal parameters Λ\Lambda and Φ\Phi. However, the eigenvalue problems in ([17](https://arxiv.org/html/2602.20856v1#S3.E17 "In Proposition 4. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) and ([18](https://arxiv.org/html/2602.20856v1#S3.E18 "In Proposition 4. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) require computing the inverse of large matrices, which is challenging in high-dimensional settings. To address this, we propose the following proposition to iteratively estimate Λ\Lambda and Ψ\Psi.

###### Proposition 5.

Consider a set of managed-portfolios χΦ\chi\_{\Phi} of dimension T×MT\times M:

|  |  |  |  |
| --- | --- | --- | --- |
|  | χΦ=[(χΦ)2′(χΦ)3′⋮(χΦ)T+1′],\chi\_{\Phi}=\begin{bmatrix}(\chi\_{\Phi})\_{2}^{\prime}\\ (\chi\_{\Phi})\_{3}^{\prime}\\ \vdots\\ (\chi\_{\Phi})\_{T+1}^{\prime}\\ \end{bmatrix}, |  | (19) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | (χΦ)s=Πs′​Φ.(\chi\_{\Phi})\_{s}=\Pi\_{s}^{\prime}\Phi. |  | (20) |

The problem in ([17](https://arxiv.org/html/2602.20856v1#S3.E17 "In Proposition 4. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) is essentially an asset‐allocation exercise: it seeks to maximize the squared Sharpe ratio by investing in χΦ\chi\_{\Phi} composed of MM assets.
This is equivalent to estimating Λ\Lambda as the mean-variance efficient portfolio weights.

Following britten1999sampling, the estimate of Λ\Lambda is obtained from the following regression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏=χΦ​Λ+𝐮,\mathbf{1}=\chi\_{\Phi}\Lambda+\mathbf{u}, |  | (21) |

where 𝟏\mathbf{1} is a TT-vector of ones and TT denotes the sample size.
To handle high-dimensional settings, we adopt ridge regression (kelly2023FML; shen2024can).
The estimator for Λ\Lambda is then given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ^=(χΦ′​χΦ+λ​IM)−1​χΦ′​𝟏,\hat{\Lambda}=(\chi\_{\Phi}^{\prime}\chi\_{\Phi}+\lambda I\_{M})^{-1}\chi\_{\Phi}^{\prime}\mathbf{1}, |  | (22) |

where λ\lambda is a Ridge-type parameter that shrinks the regression coefficients towards zero.

Similarly, we define a set of managed-portfolios χΛ\chi\_{\Lambda} of dimension T×N2T\times N^{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | χΛ=[(χΛ)2′(χΛ)3′⋮(χΛ)T+1′],\chi\_{\Lambda}=\begin{bmatrix}(\chi\_{\Lambda})\_{2}^{\prime}\\ (\chi\_{\Lambda})\_{3}^{\prime}\\ \vdots\\ (\chi\_{\Lambda})\_{T+1}^{\prime}\\ \end{bmatrix}, |  | (23) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | (χΛ)s=Πs​Λ.(\chi\_{\Lambda})\_{s}=\Pi\_{s}\Lambda. |  | (24) |

The problem in ([18](https://arxiv.org/html/2602.20856v1#S3.E18 "In Proposition 4. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) is another asset allocation exercise: it seeks to maximize the squared Sharpe ratio by investing in χΛ\chi\_{\Lambda}.
The estimator for Φ\Phi is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ^=(χΛ′​χΛ+λ​IN2)−1​χΛ′​𝟏.\hat{\Phi}=(\chi\_{\Lambda}^{\prime}\chi\_{\Lambda}+\lambda I\_{N^{2}})^{-1}\chi\_{\Lambda}^{\prime}\mathbf{1}. |  | (25) |

We highlight several key aspects of Sharpe ratio-maximization.

First, the preceding propositions recast the problem as a managed-portfolio optimization, yielding the optimal weights for the tangency portfolio—or equivalently, for the stochastic discount factor (SDF).

Second, we impose a common ridge penalty λ\lambda when estimating both Λ\Lambda and Φ\Phi, thereby enforcing uniform shrinkage across all components. This shared regularization parameter simplifies exposition, enhances replicability, and mitigates overfitting in finite samples.
We implement the five-fold cross-validation scheme to select λ\lambda dynamically.

Third, although the generalized eigenvalue solution provides a population-level characterization of the Sharpe ratio-maximizer, in practice we replace the unknown moment matrices with their sample analogues and apply the same ridge penalty. Rather than solving a generalized eigenvalue problem directly, we cast the estimation as a single ridge-penalized regression. This approach recovers the optimal SDF direction in finite samples, improves numerical stability by shrinking weights on weak or collinear signals, and avoids the computational burden of eigendecomposition. The resulting weight vector exactly coincides with the theoretical maximizer under the ridge-regularized sample formulation.

Fourth, the solution to the Sharpe ratio-maximizing strategy can be interpreted as a regularized linear combination of the principal components (PCs) of the matrix Π\Pi, with both Λ\Lambda and Φ\Phi estimated via ridge regressions on projected versions of Π\Pi. Unlike expected return-maximizing approaches that primarily load on the leading PCs, this strategy optimizes portfolio weights across the full spectrum of PCs. As a result, it captures predictive signals even in low-variance directions—consistent with the findings of kelly2025universal—and achieves superior risk-adjusted performance.

Fifth, our methodology for estimating the stochastic discount factor offers a distinct contribution to recent advances that emphasize firm characteristics (e.g., kelly2019characteristics; lettau2020factors; chen2024deep; feng2024deep; didisheim2024apt; cong2025growing; liu2025genetic). Unlike these approaches that treat assets independently, we incorporate structured cross-asset dependencies. This not only enhances empirical performance in out-of-sample tests but also yields a more interpretable economic narrative for how information propagates across securities.

Cross-asset dependencies are also central to recent transformer-based approaches in asset pricing, which leverage multi-headed attention mechanisms to extract and aggregate predictive signals across assets. For instance, cong2022alphaportfolio introduce AlphaPortfolio, a deep reinforcement learning framework with cross-asset attention networks (CAAN) that model interdependencies among securities. Similarly, the AIPM framework of Kelly2024aipm embeds transformer architectures within the SDF, showing that nonlinear information sharing across assets can significantly improve empirical performance.

While these transformer models offer substantial modeling flexibility, our framework provides a complementary linear alternative that emphasizes transparency and interpretability. We capture cross-asset spillovers through a connection matrix Ψ\Psi, where each element Ψi,j\Psi\_{i,j} quantifies the predictive influence of asset ii’s signals on asset jj’s returns. Although related to the linear surrogate of the transformer, our approach differs in a key respect. The linear transformer models the attention matrix as a function of asset-level signals, requiring estimation of O​(M3)O(M^{3}) parameters, where MM denotes the number of characteristics. In such setups, signal relevance and cross-asset dependencies are entangled within the signal space.

By contrast, we disentangle these two components: signal relevance is captured by a vector Λ\Lambda, while cross-asset connections are modeled separately via Ψ\Psi. This separation reduces parameter complexity to O​(M+N2)O(M+N^{2}), promotes computational efficiency, enables straightforward replication, and delivers an economically interpretable decomposition of predictive strength and cross-asset signal spillovers.

## 4 Data

Our dataset combines monthly stock returns from the Center for Research in Security Prices (CRSP), accounting variables from Compustat, and analyst coverage and earnings forecasts from the Institutional Brokers’ Estimate System (IBES). We assume that quarterly and annual financial statements from Compustat become publicly available four months after the end of the corresponding fiscal quarter. The full sample spans January 1963 to December 2023. Out-of-sample evaluation begins in February 1973, with estimation windows based on rolling samples of the most recent 120 monthly observations.

### 4.1 Predictive Characteristics

We employ 138 firm-level signals across 13 characteristic themes: Accruals, Debt Issuance, Investment, Leverage, Low Risk, Momentum, Profit Growth, Profitability, Quality, Seasonality, Size, Short-Term Reversal, and Value. These signals originate from jensen2023there.222We use the “Global Stock Returns and Characteristics” dataset under “Contributed Data Forms” on WRDS: <https://wrds-www.wharton.upenn.edu/pages/get-data/contributed-data-forms/global-factor-data/>. Table IA.II of jensen2023there details the signal definitions and references. Of the original 153 signals, we exclude 15 that begin after 1963 to satisfy the sample-coverage requirements of kelly2023principal. We apply standard filters to retain only observations with: (i) excntry = “USA”, (ii) CRSP shrcd ∈{10,11}\in\{10,11\}, (iii) CRSP exchcd ∈{1,2,3}\in\{1,2,3\}, and (iv) non-missing monthly excess return (ret\_exc) and next-month excess return (ret\_exc\_lead1m). Each characteristic is standardized to have a mean of zero and a standard deviation of one.

### 4.2 Spread Portfolios

For each of the 138 signals, we sort stocks into terciles each month and compute high-minus-low factor returns. To form factor-level signals, we aggregate stock-level signals into corresponding factor portfolios. Returns and signals are value-weighted by market equity, with individual market-equity weights winsorized at the 80th percentile of NYSE capitalization, following the data providers’ recommendations.

### 4.3 Bivariate Sorting on Size and Other Characteristics

We also construct bivariate sorted portfolios to serve as alternative investment universe. First, stocks are sorted into two size groups (big vs. small) based on market equity. Independently, each signal sorts stocks into three groups (high, medium, low). Cross-classifying these sorts produces six portfolios; we retain only the high and low portfolios for each size group, resulting in four portfolios per signal. As with the spread portfolios, returns and signals are capped-value-weighted by winsorized market equity. We omit the bivariate portfolios for the characteristic ami\_126d due to missing returns in 2023. Moreover, since size already plays a role in the sorting procedure, we consider a total of 136×4=544136\times 4=544 portfolios.

Thus, we consider two investment universes: one constructed from univariate sorts comprising 138 spread portfolios, and the other from bivariate sorts comprising 544 portfolios. Each portfolio is associated with a time series of returns and 138 signal observations.

## 5 Results

### 5.1 An Illustrative Toy Example

To build intuition for the proposed framework, we construct a low-dimensional toy dataset comprising five firm characteristics—market equity (ME), book-to-market ratio (BM), operating profits to lagged book equity (OP), asset growth (INV), and 12-month momentum (MOM)—and nine portfolios formed by a 3×33\times 3 sort on ME and BM (ranging from ME1×BM1 to ME3×BM3).

This simplified setup allows us to explicitly report the estimated low-dimensional parameters Λ\Lambda and Ψ\Psi, as well as the weight vector ω\omega. It also enables a comparison of key performance metrics for: (i) strategies subject to unit-norm constraints without an explicit zero-cost requirement; and (ii) zero-cost strategies with total leverage constrained to two.

We implement expected return and Sharpe ratio-maximizing strategies, as formulated in sections [2](https://arxiv.org/html/2602.20856v1#S2 "2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") and [3](https://arxiv.org/html/2602.20856v1#S3 "3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work."). These strategies, which target different objectives, yield notable differences in parameter estimates and performance outcomes. Table [1](https://arxiv.org/html/2602.20856v1#S5.T1 "Table 1 ‣ 5.1 An Illustrative Toy Example ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") summarize the monthly average returns, monthly standard deviations, and *annualized* Sharpe ratios for each strategy over the out‐of‐sample period from February 1973 to December 2023.

The first two rows of the table consider the case in which the zero-cost assumption is not imposed. The results show that the strategy maximizing expected return (MR Cross) delivers a high average monthly return of 5.56%, but with substantial volatility (standard deviation of 61.9%), yielding a Sharpe ratio of just 0.31.

The Sharpe ratio-maximizing strategy (MS Cross) attains a mean return of 2.36% and a much lower volatility (9.78 %), yielding a Sharpe ratio of 0.84. Consequently, a mean–variance investor would find the Sharpe ratio‐maximizing strategy considerably more attractive, whereas an investor solely targeting expected returns would prefer the expected return‐maximizing strategy. Thus far, the out‐of‐sample performance aligns closely with the ex ante investment objectives.

Next, we consider a strategy that maximizes the Sharpe ratio using self‐prediction to isolate the incremental contribution of cross‐predictive relations relative to self‐predictive relations. The key distinction between these two strategies lies in the structure of the connection matrix Ψ\Psi. Under cross‐prediction, Ψ\Psi is a full 9×99\times 9 matrix, capturing all pairwise interactions among the characteristics and returns of assets. In contrast, under self‐prediction, Ψ\Psi is restricted to its diagonal terms.

The second and third rows of Table [1](https://arxiv.org/html/2602.20856v1#S5.T1 "Table 1 ‣ 5.1 An Illustrative Toy Example ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") report the performance of the Sharpe ratio–maximizing strategies under cross‐prediction and self‐prediction, respectively. The cross‐prediction strategy (MS Cross) delivers a Sharpe ratio of 0.84 with a mean return of 2.36%, whereas the self‐prediction variant (MS Self) achieves a lower Sharpe ratio of 0.60 and the lowest mean return of 1.31% . This gap in both risk‐adjusted and absolute returns illustrates the incremental benefit of incorporating cross‐predictive relationships beyond self‐prediction alone, underscoring the pivotal role of cross‐predictive dynamics in enhancing portfolio performance.

To provide further economic perspective on the value of accounting for cross-stock predictability, we compute the certainty equivalent return of the investment strategies. The certainty equivalent is defined as C​E=μ−γ2​σ2CE=\mu-\frac{\gamma}{2}\sigma^{2}, where μ\mu and σ\sigma are the expected return and volatility of the strategy, respectively, and the risk aversion parameter γ\gamma is set to 2. Accounting for cross-predictability, the certainty equivalent rate of return is approximately 16.84% per year—8.00% higher than that of self-predictability—indicating economically significant gains.

We next maximize expected return and Sharpe ratio under the zero‐cost and leverage‐two constraints. The fourth and fifth rows of Table [1](https://arxiv.org/html/2602.20856v1#S5.T1 "Table 1 ‣ 5.1 An Illustrative Toy Example ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") report these constrained strategies, confirming that imposing the zero‐cost restriction reduces expected returns for both objectives. Nevertheless, even with zero cost and fixed leverage, the Sharpe ratio–maximizing strategy outperforms the expected‐return–maximizing strategy, delivering a higher mean return (0.50% vs. 0.49%) and a substantially higher Sharpe ratio (1.22 vs. 0.53).

To provide additional insight into cross-prediction and self-prediction strategies, Table [2](https://arxiv.org/html/2602.20856v1#S5.T2 "Table 2 ‣ 5.1 An Illustrative Toy Example ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") reports the estimated values of Λ\Lambda, Ψ\Psi, and ω\omega for each approach without imposing the zero-cost constraint. The estimation window spans 120 months, from December 2003 to November 2023, covering our last out-of-sample period. Panel A presents the Sharpe ratio-maximizing cross-prediction strategy; Panel B presents the Sharpe ratio-maximizing self-prediction strategy; and Panel C reports the differences in the portfolio weights ω\omega between the two.

In Table [2](https://arxiv.org/html/2602.20856v1#S5.T2 "Table 2 ‣ 5.1 An Illustrative Toy Example ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work."), Panel A shows that the estimated Λ\Lambda coefficient for book‐to‐market equity (BM) is −0.34-0.34, whereas the coefficients for the other four characteristics are all positive, with the smallest value at 0.210.21. This suggests that the Sharpe ratio–maximizing strategy with cross‑prediction is well balanced across the five characteristics. The full 9×99\times 9 matrix Ψ\Psi exhibits substantial values both on and off the diagonal: the average absolute value of its diagonal entries is 0.00680.0068, compared to an average absolute off‑diagonal entry of 0.08050.0805, indicating that cross‑predictive relationships play an even more substantial role in defining the trading strategy.

Panel B of Table [2](https://arxiv.org/html/2602.20856v1#S5.T2 "Table 2 ‣ 5.1 An Illustrative Toy Example ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") shows that under self‐prediction the estimated Λ\Lambda coefficients exhibit greater dispersion—asset growth (INV) even turns negative—while Ψ\Psi is constrained to its diagonal (average absolute value of 0.02880.0288, all off‐diagonals zero).
This contrast highlights the structural effect of cross-predictability: including cross-predictive terms not only yields nonzero off-diagonal elements of Ψ\Psi but also shifts the estimated Λ\Lambda coefficients, altering the relative importance of characteristics.

Panel C reports how the optimal weights ω\omega shift between cross‐ and self‐prediction:
under cross‐prediction, long exposures to ME3 BM1 decrease,
and shorts in ME1 BM2 deepen.
For example, the ME1 BM2 position is −0.27-0.27 under cross‐prediction—driven by off‐diagonal Ψ\Psi entries of 0.240.24 and 0.250.25—whereas it is substantially smaller under self‐prediction.

As noted earlier, the optimal trading strategy that accounts for cross-predictability delivers a 8.00% higher certainty equivalent return, suggesting that the estimated Λ\Lambda and Ψ\Psi, which determine the portfolio weights ω\omega, differ to an economically significant degree when cross-predictability is incorporated, relative to the benchmark case of self-predictability.

In summary, the results in Tables [1](https://arxiv.org/html/2602.20856v1#S5.T1 "Table 1 ‣ 5.1 An Illustrative Toy Example ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") and [2](https://arxiv.org/html/2602.20856v1#S5.T2 "Table 2 ‣ 5.1 An Illustrative Toy Example ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") confirm that incorporating cross‑predictive relationships is valuable for constructing robust investment strategies, even in a low‑dimensional illustrative setting.

Table 1: Performance of Strategies of a Toy Example

This table reports the monthly average return (%), monthly standard deviation (%), and annualized Sharpe ratio for five strategies in a low‐dimensional toy example involving five characteristics and nine assets. The strategies are:

1. 1.

   Unconstrained expected return-maximization with cross‐prediction;
2. 2.

   Unconstrained Sharpe ratio-maximization with cross‐prediction;
3. 3.

   Unconstrained Sharpe ratio-maximization with self‐prediction;
4. 4.

   Zero‐cost, leverage‐two expected return-maximization with cross‐prediction;
5. 5.

   Zero‐cost, leverage‐two Sharpe ratio-maximization with cross‐prediction.

|  | μ\mu | σ\sigma | SR | Cost |
| --- | --- | --- | --- | --- |
| MR Cross | 5.56 | 61.9 | 0.31 | Not Zero Cost |
| MS Cross | 2.36 | 9.78 | 0.84 | Not Zero Cost |
| MS Self | 1.31 | 7.57 | 0.60 | Not Zero Cost |
| MR Cross ZC | 0.49 | 3.22 | 0.53 | Zero Cost |
| MS Cross ZC | 0.50 | 1.43 | 1.22 | Zero Cost |

Table 2: Estimates for Λ\Lambda and Ψ\Psi of a Toy Example

This tables reports the estimates for λ\lambda, Ψ\Psi, and ω\omega of the Sharpe ratio-maximization strategies of the last rolling-window estimation, with cross-prediction in Panel A and self-prediction in Panel B. These strategies are free from zero-cost and leverage-two constraints.
The Λ\Lambda vector has five elements corresponding to five characteristics: ME, BM, OP, INV, and MOM.
There are nine assets for investment: the three-by-three sorted portfolios on ME and BM.
Specifically, they are ME1 BM1, ME1 BM2, ME1 BM3, ME2 BM1, ME2 BM2, ME2 BM3, ME3 BM1, ME3 BM2, ME3 BM3.
The Ψ\Psi is a nine-by-nine matrix, where the element i,j corresponds to the strength of the predictive relationship of the asset i’s signals to asset j’s returns.
For cross-prediction in Panel A, the Ψ\Psi has 81 values to estimate, while for self-prediction in Panel B, the Ψ\Psi is only active in 9 values in the diagonal.
In addition, the following two rows of panels A and B report the absolute average of the diagonal and off-diagonal terms of Ψ\Psi.
Finally, Panel C shows the change of ω\omega from cross- to self-prediction strategies.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Panel A: Cross-Prediction | | | | | | | | |  |
| Λ\Lambda | ME | BM | OP | INV | MOM |  |  |  |  |
|  | 0.21 | -0.34 | 0.29 | 0.53 | 0.69 |  |  |  |  |
| Ψ\Psi | 0.02 | -0.05 | 0.01 | -0.01 | 0.03 | -0.03 | -0.01 | -0.04 | 0.02 |
|  | 0.03 | -0.21 | -0.05 | 0.06 | 0.16 | -0.09 | 0.01 | -0.06 | 0.15 |
|  | 0.03 | 0.24 | -0.08 | -0.02 | -0.17 | 0.18 | -0.04 | 0.09 | -0.17 |
|  | -0.12 | 0.15 | 0.06 | 0.02 | 0.12 | -0.22 | 0.00 | -0.03 | 0.07 |
|  | 0.09 | -0.03 | -0.09 | -0.04 | -0.01 | 0.04 | 0.02 | 0.10 | -0.01 |
|  | -0.03 | -0.13 | 0.12 | -0.05 | -0.11 | 0.04 | 0.11 | -0.07 | 0.07 |
|  | 0.13 | -0.14 | 0.14 | 0.01 | -0.26 | 0.23 | 0.08 | 0.00 | -0.21 |
|  | -0.14 | 0.25 | -0.26 | -0.05 | 0.13 | 0.00 | -0.10 | 0.03 | 0.15 |
|  | -0.02 | -0.09 | 0.15 | 0.09 | 0.09 | -0.14 | -0.06 | -0.02 | -0.06 |
|  | Absolute Average of Diagonal Terms Ψ\Psi | | | | | | | | 0.0068 |
|  | Absolute Average of Off-Diagonal Terms Ψ\Psi | | | | | | | | 0.0805 |
| ω\omega | -0.03 | -0.27 | 0.20 | 0.00 | -0.03 | 0.03 | 0.09 | -0.06 | -0.06 |
| Panel B: Self-Prediction | | | | | | | | | |
| Λ\Lambda | ME | BM | OP | INV | MOM |  |  |  |  |
|  | -0.09 | -0.89 | 0.41 | -0.14 | 0.12 |  |  |  |  |
| Ψ\Psi | -0.14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | 0 | 0.51 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | 0 | 0 | -0.13 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | 0 | 0 | 0 | -0.04 | 0 | 0 | 0 | 0 | 0 |
|  | 0 | 0 | 0 | 0 | 0.41 | 0 | 0 | 0 | 0 |
|  | 0 | 0 | 0 | 0 | 0 | 0.02 | 0 | 0 | 0 |
|  | 0 | 0 | 0 | 0 | 0 | 0 | 0.35 | 0 | 0 |
|  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -0.63 | 0 |
|  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -0.09 |
|  | Absolute Average of Diagonal Terms Ψ\Psi | | | | | | | | 0.0288 |
|  | Absolute Average of Off-Diagonal Terms Ψ\Psi | | | | | | | | 0 |
| ω\omega | -0.14 | -0.10 | 0.19 | -0.03 | 0.00 | -0.02 | 0.47 | -0.32 | 0.08 |
| Panel C: Change of Weights from Cross- to Self-Prediction | | | | | | | | | |
| ID | ME1 BM1 | ME1 BM2 | ME1 BM3 | ME2 BM1 | ME2 BM2 | ME2 BM3 | ME3 BM1 | ME3 BM2 | ME3 BM3 |
|  | 0.10 | -0.17 | 0.00 | 0.03 | -0.03 | 0.05 | -0.37 | 0.26 | -0.13 |

Table 3: Performance of Cross-Predictive Strategies

This table reports the monthly average return (%), monthly standard deviation (%), and annualized Sharpe ratio of cross-predictive strategies. The strategies are zero-cost and leverage two.
MR and MS are strategies to maximize expected return and Sharpe ratio, respectively.
Panels A and C are for investing in 138 spread portfolios, and Panels B and D are for 544 bivariate sorted portfolios.
In Panels A and B, we report the results of the whole out-of-sample period from February 1973 to December 2023 and the high and low sentiment periods split by the sentiment median value over the sample periods from February 1973 to December 2023.
In Panels C and D, we report for January 1990 to December 2023, and the high and low VIX periods split by the VIX median value over the sample periods from 1990 to 2023.

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1973:02-2023:12 | | |  | SENT High | | |  | SENT Low | | |
|  | μ\mu | σ\sigma | SR |  | μ\mu | σ\sigma | SR |  | μ\mu | σ\sigma | SR |
| Panel A: Spread Portfolios | | | | | | | | | | | |
| MR | 0.42 | 3.23 | 0.45 |  | 0.73 | 3.79 | 0.67 |  | 0.11 | 2.53 | 0.15 |
| MS | 0.29 | 0.45 | 2.21 |  | 0.30 | 0.47 | 2.19 |  | 0.27 | 0.43 | 2.22 |
| Panel B: BiSort Portfolios | | | | | | | | | | | |
| MR | 0.45 | 3.02 | 0.52 |  | 0.48 | 3.35 | 0.49 |  | 0.42 | 2.66 | 0.54 |
| MS | 0.26 | 0.27 | 3.32 |  | 0.28 | 0.27 | 3.58 |  | 0.24 | 0.27 | 3.08 |
|  | 1990:01-2023:12 | | |  | VIX High | | |  | VIX Low | | |
|  | μ\mu | σ\sigma | SR |  | μ\mu | σ\sigma | SR |  | μ\mu | σ\sigma | SR |
| Panel C: Spread Portfolios | | | | | | | | | | | |
| MR | 0.33 | 3.83 | 0.30 |  | 0.59 | 4.97 | 0.41 |  | 0.07 | 2.14 | 0.12 |
| MS | 0.24 | 0.43 | 1.92 |  | 0.30 | 0.52 | 2.02 |  | 0.18 | 0.31 | 1.98 |
| Panel D: BiSort Portfolios | | | | | | | | | | | |
| MR | 0.39 | 3.20 | 0.42 |  | 0.57 | 3.87 | 0.51 |  | 0.20 | 2.33 | 0.30 |
| MS | 0.24 | 0.29 | 2.90 |  | 0.28 | 0.34 | 2.89 |  | 0.20 | 0.22 | 3.13 |

### 5.2 Zero-Cost Linear Strategies

Table [3](https://arxiv.org/html/2602.20856v1#S5.T3 "Table 3 ‣ 5.1 An Illustrative Toy Example ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") reports the performance of linear cross‑predictive strategies implemented as zero‑cost, leverage‑two portfolios, comparable to common factor and anomaly implementations. MR and MS denote the strategies that maximize expected return and the Sharpe ratio, respectively.
In Panel A, we consider an investment universe with 138 spread portfolios detailed in the data section. Over the full sample period, MR achieves a monthly average return of 0.42% with an annualized Sharpe ratio of 0.45, whereas MS records a lower monthly average return of 0.29% but a substantially higher annualized Sharpe ratio of 2.21.

We further analyze performance during evolving market states by splitting the out‑of‑sample period at the median of the investor sentiment index (baker2006investor).333The sentiment data spans July 1965 to December 2023 and is obtained from the variable ‘SENT” on Jeffrey Wurgler’s website: <https://pages.stern.nyu.edu/~jwurgler/data/SENTIMENT.xlsx>. During high‑sentiment regimes, MR delivers an average monthly return of 0.73%, while in low‑sentiment regimes its return falls to 0.11%. The MS strategy exhibits robust Sharpe ratios across both regimes: 2.19 in high‑sentiment periods and 2.22 in low‑sentiment periods.

In Panel B, we evaluate investments in 544 bi‑variate sorted portfolios as detailed in the data section. Over the full out‑of‑sample period (January 1973–December 2023), MR delivers a monthly average return of 0.45% and an annualized Sharpe ratio of 0.52, whereas MS achieves an exceptionally high annualized Sharpe ratio of 3.32. In sub‑period analyses, MR’s average return increases during high‑sentiment regimes, while MS maintains Sharpe ratios above 3 in both high‑ and low‑sentiment periods.

In Panels C and D, we split the period January 1990–December 2023 at the median of the VIX index.444The VIX data spans 1990 to 2023 and is obtained from the CBOE: <http://www.cboe.com/products/vix-index-volatility/vix-options-and-futures/vix-index/vix-historical-data/>. In Panel C (spread portfolios), MR’s average return is 0.59% during high‑VIX regimes and 0.07% during low‑VIX regimes (0.33% full sample), while MS records Sharpe ratios of 2.02 and 1.98 in high‑ and low‑VIX regimes (1.92 full sample).

In Panel D (bi‑variate sorted portfolios), MR attains a monthly average return of 0.39% and an annualized Sharpe ratio of 0.42, while MS achieves a Sharpe ratio of 2.90. MR’s return remains higher in high‑VIX regimes, and MS sustains Sharpe ratios around 3 in both high‑ and low‑VIX regimes.

In summary, MR strategies deliver high expected returns during high‑sentiment and high‑VIX regimes, but considerably lower expected returns otherwise. In contrast, MS strategies consistently achieve superior Sharpe ratios across all market states.

#### 5.2.1 Comparing with Principal Portfolios (PP)

We compare the principal portfolio-based trading strategies of kelly2023principal with our own over the out-of-sample period from 1973 to 2019, as in their study. The results are reported in Table [4](https://arxiv.org/html/2602.20856v1#S5.T4 "Table 4 ‣ 5.2.1 Comparing with Principal Portfolios (PP) ‣ 5.2 Zero-Cost Linear Strategies ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.").

Panel A, row 1 (PP–ME), reports the performance of the first principal portfolio on the market-equity signal: a 3.27% monthly expected return, a 0.51 annualized Sharpe ratio, and a sum of absolute equity positions equal to 23.22. Rows 2 and 3 present the first principal portfolios for the book-to-market and momentum signals, which achieve Sharpe ratios of 0.60 and 0.48, respectively, with similarly high leverage.
The principal portfolio can be applied to only one signal at a time. We also consider to take the 1/N equal-weighted strategy of the first principal portfolios across all 138 signals, namely the PPEW strategy, which delivers a 2.83% monthly expected return and a 0.56 annualized Sharpe ratio. Notably, the leverage of PPEW is only 1.35, reflecting substantial diversification benefits by equal weighted average across predictors.

Our maximum-expected return strategy achieves an 135.14% monthly expected return and a 0.52 annualized Sharpe ratio, with leverage of 537.70. Overall, the maximum-expected return strategy slightly underperforms the principal portfolios in Sharpe ratio, albeit remains reasonably close to them.

By contrast, the MS strategy harnesses multiple predictors to diversify exposures and optimize risk-adjusted returns, achieving an annualized Sharpe ratio of 2.22 with a leverage factor of 438.01. While the principal portfolio approach targets expected return subject to a volatility constraint, our strategy is derived directly from Sharpe ratio-maximization. As a result, it places greater emphasis on balancing return and risk, leading to improved performance on risk-adjusted metrics in our empirical setting.

To enhance implementability, we impose zero‐cost and leverage‐two constraints on both strategies. Panel B of Table [4](https://arxiv.org/html/2602.20856v1#S5.T4 "Table 4 ‣ 5.2.1 Comparing with Principal Portfolios (PP) ‣ 5.2 Zero-Cost Linear Strategies ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") reports the resulting performance. Under these constraints, the maximum‐expected‐return strategy (Row 1) achieves a 0.46% monthly expected return and an annualized Sharpe ratio of 0.51, while the maximum‐Sharpe ratio strategy (Row 2) attains a 0.30% monthly expected return and an annualized Sharpe ratio of 2.33. In both cases, the portfolios maintain zero net cost and a constant leverage of two in every period.

Overall, the maximum‑Sharpe ratio strategy remains highly competitive—delivering superior risk‑adjusted performance relative to a range of recent approaches, including principal portfolios. Accordingly, we focus our subsequent analyses to the constrained max‑SR strategy.

Table 4: A First Comparison on the Performance of PP, MR, and MS

This table reports each strategy’s monthly average return (%), monthly standard deviation (%), annualized Sharpe ratio, time-series average of the sum of positions on basic assets, and time-series average of the absolute sum of positions on basic assets. PP‑ME is the Principal Portfolio strategy using the market‑equity signal; PP‑BM uses book‑to‑market; PP‑MOM uses momentum. PP‑EW is an equal‑weighted combination of the first principal portfolios of 138 signals. MR is our maximum‑expected return strategy, and MS is our maximum‑Sharpe ratio strategy. Panel A places no leverage or cost constraints on the strategies. Panel B imposes two constraints—a zero‑cost requirement and a leverage restriction—on all strategies. Data span January 1963 through December 2019 (from PP’s replication package on the Journal of Finance website), with the out‑of‑sample period running from February 1973 to December 2019.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Strategy | μ\mu | σ\sigma | SR | Sum | ASum |
| Panel A: Strategies | | | | | |
| PP-ME | 3.27 | 22.32 | 0.51 | 23.21 | 23.22 |
| PP-BM | 4.64 | 26.94 | 0.60 | 12.62 | 14.45 |
| PP-MOM | 3.65 | 26.41 | 0.48 | 23.94 | 25.34 |
| PPEW | 2.83 | 17.52 | 0.56 | 1.03 | 1.35 |
| MR | 135.14 | 895.59 | 0.52 | 95.83 | 537.70 |
| MS | 68.65 | 107.15 | 2.22 | 48.33 | 438.01 |
| Panel B: Strategies with Zero Cost | | | | | |
| MR | 0.46 | 3.10 | 0.51 | 0.00 | 2.00 |
| MS | 0.30 | 0.45 | 2.33 | 0.00 | 2.00 |

Table 5: Cross- vs Self-Prediction

This table reports the monthly average returns (%), monthly standard deviation(%), and annualized Sharpe ratio, time-series average of the sum of positions on basic assets, and time-series average of the absolute sum of positions on basic assets. The objective of the strategies is to maximize the Sharpe ratio.
Notably, the cross-prediction strategies can be solved with and without the zero-cost constraint; however, the self-prediction strategy does not have an analytic solution once adding the zero-cost constraint.
Panel A invests on spread portfolios and Panel B is for bivariate sorted portfolios.
The out-of-sample period is February 1973 to December 2023.

|  | μ\mu | σ\sigma | SR | Sum | ASum |
| --- | --- | --- | --- | --- | --- |
| Panel A: Spread Portfolios | | | | | |
| MS Self | 6.76 | 16.54 | 1.42 | 1.26 | 30.93 |
| MS Cross | 64.43 | 107.19 | 2.08 | 45.06 | 438.46 |
| MS Cross ZC | 0.29 | 0.45 | 2.21 | 0.00 | 2.00 |
| Panel B: BiSort Portfolios | | | | | |
| MS Self | 15.83 | 26.64 | 2.06 | 2.34 | 99.05 |
| MS Cross | 389.99 | 450.02 | 3.00 | 112.14 | 2154.07 |
| MS Cross ZC | 0.26 | 0.27 | 3.32 | 0.00 | 2.00 |

#### 5.2.2 Cross-Prediction SDF versus Self-Prediction SDF

The existing literature on SDF estimation has predominantly focused on self-predictive frameworks, where each asset’s signals are used solely to forecast its own returns.
kelly2019characteristics propose Instrumented PCA with the belief that the factor loadings on SDF are determined by assets characteristics, overcoming the limitations of static loading in PCA.
lettau2020factors find that the SDF estimated on Risk-Premium PCA is more highly correlated with the true SDF than those estimated on PCA.
luo2025sdf estimate the SDF with observable characteristics-based factors with L1-penalized SDF regression; whereas, didisheim2024apt apply the L2-penalized SDF regression on observable and Random-Fourier-Feature generated factors.
All of these papers have been working on high-dimensional characteristics-based portfolios to estimate the SDF, where the belief of self-prediction are embedded the portfolios.

By contrast, our framework utilizes managed-portfolios inherently reflecting the belief of cross-prediction: πs\pi\_{s} ([6](https://arxiv.org/html/2602.20856v1#S2.E6 "In 1st item ‣ Proposition 1. ‣ 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")), χΦ\chi\_{\Phi} ([19](https://arxiv.org/html/2602.20856v1#S3.E19 "In Proposition 5. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")), and χΛ\chi\_{\Lambda} ([23](https://arxiv.org/html/2602.20856v1#S3.E23 "In Proposition 5. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")).
Whether cross-predictive strategies—where signals from one asset help predict the returns of others—can systematically outperform self-predictive ones in high-dimensional settings remains an open question.
To investigate this, we construct the self-predictive strategy by restricting the matrix Ψ\Psi to its diagonal, thereby eliminating all cross-asset interactions.

Panel A of Table [5](https://arxiv.org/html/2602.20856v1#S5.T5 "Table 5 ‣ 5.2.1 Comparing with Principal Portfolios (PP) ‣ 5.2 Zero-Cost Linear Strategies ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") reports the empirical performance of the Sharpe ratio–maximizing strategies on the 138 spread portfolios. The self-predictive strategy achieves a Sharpe ratio of 1.42, while the cross-predictive counterparts attain Sharpe ratios of 2.08 without zero-cost requirement and 2.21 with zero-cost and leverage-two constraints. This more than 0.60 difference in Sharpe ratio underscores the incremental value of incorporating cross-asset predictive signals.

Panel B reports results for the 544 bivariate sorted portfolios. The self-predictive strategy achieves a Sharpe ratio of 2.06, while the cross-predictive variants reach 3.32 and 3.00 under constrained and unconstrained implementations, respectively. This gap of more than 1.00 in Sharpe ratio highlights the significant contribution of off-diagonal elements in Ψ\Psi to improved portfolio performance.

Overall, the evidence confirms that cross-predictive strategies materially enhance the estimation and performance of stochastic discount factors—particularly in richer portfolio universes and longer samples.

#### 5.2.3 Factor Spanning Tests

We conduct a series of factor-spanning tests to assess whether the established asset pricing factors fully explain the expected returns of the Sharpe ratio-maximizing strategies.
Table [6](https://arxiv.org/html/2602.20856v1#S5.T6 "Table 6 ‣ 5.2.3 Factor Spanning Tests ‣ 5.2 Zero-Cost Linear Strategies ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") reports monthly alphas (%), factor loadings, and associated tt-statistics.
Panel A presents the Sharpe ratio-maximizing strategy on the spread portfolios, while Panel B reports for the bivariate sorted portfolios.

We first evaluate the fama2015five five-factor model (FF5).
The strategy on spread portfolio exhibits modest loadings on Market (β=−0.01\beta=-0.01, t=−2.56t=-2.56) and SMB (β=0.01\beta=0.01, t=1.78t=1.78) but insignificant exposures to the other four factors, while delivering a highly significant monthly alpha of 0.29% (t=13.29t=13.29).
This suggests that the strategy’s returns are largely orthogonal to the FF5 factors.
Also, we augment the FF5 model with momentum (UMD), short-term reversal (REV), and liquidity (LIQ) factors (pastor2003).
In this expanded specification, the strategy shows significant loadings on UMD and REV but not on LIQ, while its alpha remains economically and statistically significant at 0.26% (t=11.54t=11.54).
These findings indicate that momentum and reversal effects partially explain the strategy’s performance, with little role for liquidity risk.

Next, we then examine the hou2015 four-factor model, which incorporates investment (R\_IA) and profitability (R\_ROE) factors alongside market and size factors.
The strategy displays negligible loadings on R\_IA and R\_ROE, while maintaining a highly significant alpha.
The stambaugh2017 mispricing factors—MGMT and PERF—also fail to subsume the strategy’s returns:
The strategy shows minimal exposures to both factors, with an alpha of 0.28% (t=10.20t=10.20).
Then, we assess the daniel2020short model, which includes the market factor and two behavioral factors, PEAD and FIN.
While the strategy loads significantly on PEAD, its alpha remains robust at 0.29% (t=11.09t=11.09), and it shows no meaningful exposure to FIN.
Finally, in a comprehensive regression incorporating all fourteen factors, The strategy maintains an alpha of 0.26% (t=8.04t=8.04), with statistically significant but economically small loadings on SMB, UMD, REV, LIQ, FIN, and R\_IA.
These results collectively demonstrate that the strategy’s expected returns cannot be fully explained by existing factor models.

Panel B corroborates these findings. The strategy on bivariate sorted portfolio displays statistically significant but economically modest loadings on RMW, CMA, REV, PERF, R\_IA, MGMT, and PERF.
Notably, it maintains a monthly alpha of 0.25% (t=11.36t=11.36) even after controlling for all fourteen factors, further supporting the strategy’s robustness to established factor models.

Across all specifications—including the Fama–French five-factor model with UMD, REV, and LIQ augmentations, Hou–Xue–Zhang, Stambaugh–Yuan, and Daniel–Hirshleifer–Sun frameworks, and even the comprehensive fourteen-factor regression—the Sharpe ratio-maximizing strategies on the spread and bivariate sorted portfolios exhibit persistently large and highly significant alphas with only moderate loadings on existing factors.
This suggests that conventional models may miss the cross-asset return predictability captured by our strategy.
Below, we further analyze the pricing content of the Sharpe ratio-maximizing strategies.

Table 6: Alpha and Factor Loadings

This table reports the monthly alphas (%), factor loadings, and their tt-values (in parentheses) obtained from the factor-spanning tests of regressing the strategy returns on other asset pricing factors.
We have scaled the original strategy and factor returns by 100 for percentage compatibility, aiding coefficient comparability. This table focus on the Sharpe ratio-maximizing strategies with zero cost and leverage two.
Panel A displays the results for investing in spread portfolios, while Panel B shows for bivariate sorted portfolios.
The factors include FF5 factor, momentum factor (UMD), short-term reversal factor (REV), liquidity factor (LIQ) from pastor2003, short-horizon inattention factor (PEAD) and long-horizon financing factor (FIN) from daniel2020short, investment factor (R\_IA) and return on equity factor (R\_ROE) from hou2015, management factor (MGMT) and performance factor (PERF) from stambaugh2017.
PEAD and FIN are available before December 2018.
MGMT and PERF are available before December 2016.
All other factors are available during the whole sample period.
We report with the neweywest1987 tt-statistics using a Bartlett kernel and lag length L=4​(T/100)2/9L=4(T/100)^{2/9}.
One, two, and three asterisks indicate significance at the 10%, 5%, and 1% levels, respectively.

| Alpha | Market | SMB | HML | RMW | CMA | UMD | REV | LIQ | PEAD | FIN | R\_IA | R\_ROE | MGMT | PERF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Panel A: Spread Portfolios | | | | | | | | | | | | | | |
| 0.29\*\*\* | -0.01\*\* | 0.01\* | -0.01 | 0.01 | 0.02 |  |  |  |  |  |  |  |  |  |
| (13.29) | (-2.56) | (1.78) | (-1.02) | (0.98) | (1.53) |  |  |  |  |  |  |  |  |  |
| 0.26\*\*\* | -0.01\*\* | 0.01 | -0.00 | 0.01 | 0.01 | 0.03\*\*\* | 0.02\*\*\* | -0.00 |  |  |  |  |  |  |
| (11.54) | (-2.26) | (1.48) | (-0.16) | (0.68) | (0.91) | (3.34) | (2.74) | (-0.82) |  |  |  |  |  |  |
| 0.29\*\*\* | -0.01 |  |  |  |  |  |  |  | 0.03\*\* | 0.01 |  |  |  |  |
| (11.09) | (-1.56) |  |  |  |  |  |  |  | (2.14) | (0.91) |  |  |  |  |
| 0.28\*\*\* | -0.01\*\* | 0.01\* |  |  |  |  |  |  |  |  | 0.01 | 0.01 |  |  |
| (12.91) | (-2.56) | (1.95) |  |  |  |  |  |  |  |  | (0.73) | (1.24) |  |  |
| 0.28\*\*\* | -0.00 | 0.02\*\* |  |  |  |  |  |  |  |  |  |  | 0.02 | 0.03\*\*\* |
| (10.20) | (-0.47) | (2.51) |  |  |  |  |  |  |  |  |  |  | (1.19) | (3.66) |
| 0.26\*\*\* | -0.01 | 0.01 | -0.00 | 0.01 | -0.03 | 0.01\* | 0.03\*\*\* | -0.00 | 0.01 | 0.00 | 0.04 | -0.05\*\*\* | 0.01 | 0.04\*\*\* |
| (8.04) | (-0.92) | (0.83) | (-0.13) | (0.44) | (-0.72) | (1.74) | (3.05) | (-0.51) | (0.90) | (0.37) | (1.23) | (-2.92) | (0.51) | (2.61) |
| Panel B: BiSort Portfolios | | | | | | | | | | | | | | |
| 0.25\*\*\* | -0.00 | 0.01\* | -0.00 | 0.03\*\*\* | 0.01 |  |  |  |  |  |  |  |  |  |
| (16.67) | (-0.62) | (1.94) | (-0.62) | (3.96) | (1.20) |  |  |  |  |  |  |  |  |  |
| 0.24\*\*\* | -0.00 | 0.01 | 0.00 | 0.02\*\*\* | 0.01 | 0.02\*\* | 0.01 | -0.00 |  |  |  |  |  |  |
| (13.98) | (-0.01) | (1.59) | (0.72) | (3.92) | (0.63) | (2.21) | (1.09) | (-0.37) |  |  |  |  |  |  |
| 0.25\*\*\* | 0.00 |  |  |  |  |  |  |  | 0.02\*\* | 0.02\*\*\* |  |  |  |  |
| (13.15) | (1.23) |  |  |  |  |  |  |  | (1.99) | (2.70) |  |  |  |  |
| 0.24\*\*\* | -0.00 | 0.01\*\* |  |  |  |  |  |  |  |  | 0.01 | 0.02\*\*\* |  |  |
| (14.61) | (-0.53) | (2.03) |  |  |  |  |  |  |  |  | (1.23) | (2.68) |  |  |
| 0.26\*\*\* | 0.01\* | 0.01 |  |  |  |  |  |  |  |  |  |  | 0.02\*\*\* | 0.02\*\*\* |
| (14.12) | (1.81) | (1.55) |  |  |  |  |  |  |  |  |  |  | (3.02) | (3.92) |
| 0.25\*\*\* | 0.01 | 0.01 | 0.00 | 0.02\* | -0.02 | 0.01 | 0.01 | 0.00 | 0.01 | 0.00 | 0.03 | -0.02 | 0.01 | 0.02\*\*\* |
| (11.36) | (1.42) | (1.58) | (0.15) | (1.88) | (-0.96) | (1.04) | (1.51) | (0.12) | (1.38) | (0.39) | (1.11) | (-1.29) | (1.05) | (2.69) |

#### 5.2.4 Evolution of Sharpe Ratios over the Sample Period

To assess the persistence and evolution of risk‐adjusted returns over time, Figure [1](https://arxiv.org/html/2602.20856v1#S5.F1 "Figure 1 ‣ 5.2.4 Evolution of Sharpe Ratios over the Sample Period ‣ 5.2 Zero-Cost Linear Strategies ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") Panel A shows the ten‐year trailing Sharpe ratios of our three maximum-Sharpe ratio strategies—MS Spread, MS BiSort and MS BiSort fixed—alongside those of the market and momentum factors for comparison.
555The shrinkage parameter λ\lambda for MS Spread and MS BiSort are selected via cross-validation.
Appendix [E](https://arxiv.org/html/2602.20856v1#A5 "Appendix E Cross-Validation for 𝜆 the Ridge Shrinkage Parameter ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") reports the selected parameter values of time.
MS BiSort fixed uses a fixed λ=1\lambda=1, which is the most frequently selected value.
By smoothing over a decade window, we can observe how the trading strategies respond to changing market conditions.

These strategies deliver eye‐catching Sharpe ratios in the 1990s—MS BiSort climbs as high as 4–7 before 2000, and MS Spread approaches 4—reflecting their ability to capture persistent value-enhancing opportunities. After 2000, however, it is natural to see some attenuation: wider adoption of anomaly tradings, increased market liquidity, and a lower‐volatility regime tend to compress excess returns over time. Accordingly, by the end of 2023, the trailing Sharpe of MS Spread and MS BiSort has moderated to about 1.2.
By contrast, the MS BiSort fixed seems to deliver even higher Sharpe ratios than MS BiSort, suggesting that our cross-validation scheme is conservative and provides a low bound for the out-of-sample performance.

To make more clear comparison, Figure [1](https://arxiv.org/html/2602.20856v1#S5.F1 "Figure 1 ‣ 5.2.4 Evolution of Sharpe Ratios over the Sample Period ‣ 5.2 Zero-Cost Linear Strategies ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") Panel B shows the Sharpe ratio of each strategy relative to that of MS BiSort fixed.
In early sample before 2000, the Sharpe ratio of MS Spread (MS BiSort) is approximately 60% (90%) that of MS BiSort fixed, and market and momentum factors have below 20% Shape ratio relative to MS BiSort.
In the most recent sample, the Sharpe ratios of MS Spread, MS BiSort, MKT-RF, and UMD are 70%, 75%, 43%, and 4% that of MS BiSort fixed.

For context, both the market factor’s rolling Sharpe ratio and that of the momentum factor remain well below our strategies over the entire forty‐year span. Although the performance gap narrows in the post‐2000 era, both maximum-Sharpe ratio strategies continue to deliver robust risk‐adjusted returns relative to these benchmarks.

Table [7](https://arxiv.org/html/2602.20856v1#S5.T7 "Table 7 ‣ 5.2.4 Evolution of Sharpe Ratios over the Sample Period ‣ 5.2 Zero-Cost Linear Strategies ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") reports the (annualized) Sharpe ratios of the cross-predictive maximum-Sharpe ratio strategies, Fama-French five factors, and momentum factor for three sample periods: the whole OOS period from 1973:02 to 2023:12, before 2000:01, and after 2000:01. Although, the Sharpe ratios of our strategies attenuate after 2000, they remain competitive compared to the benchmark factors in three sample periods.

Figure 1: Sharpe Ratio of Strategies

The figure depicts ten-year trailing (annualized) Sharpe ratios for the cross-predictive maximum-Sharpe ratio strategies.
“MS Spread” is the strategy to maximize Sharpe ratio investing in the spread portfolios.“MS BiSort” is the strategy to maximize Sharpe ratio investing in the bivariate sorted portfolios.
“MS BiSort fixed” uses a fixed λ=1\lambda=1, which is the most frequently selected value.
Panel A shows the Sharpe ratio, while Panel B shows the Sharpe ratio of each strategy divided by that of “MS BiSort.”
The out-of-sample period is from February 1973 to December 2023 in monthly frequency, and the first ten-year Sharpe ratio is obtained for January 1983.
For comparison, the market factor (MKT-RF) and momentum factor (UMD) are included.

![Refer to caption](x1.png)


(a) Sharpe Ratio

![Refer to caption](x2.png)


(b) Sharpe Ratio Relative to MS BiSort

Table 7: Comparing Sharpe Ratios with Prevailing Factors

The table reports the (annualized) Sharpe ratios of the cross-predictive strategies, Fama-French five factors, and momentum. Three sample periods are 1973:02 to 2023:12, 1973:02 to 1999:12, and 2000 to 2023.

|  | MS Spread | MS BiSort | MKT-RF | SMB | HML | RMW | CMA | UMD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1973-2023 | 2.21 | 3.32 | 0.45 | 0.21 | 0.33 | 0.45 | 0.5 | 0.45 |
| 1973-1999 | 2.84 | 4.98 | 0.48 | 0.16 | 0.47 | 0.36 | 0.58 | 0.96 |
| 2000-2023 | 1.58 | 2.21 | 0.41 | 0.27 | 0.20 | 0.54 | 0.43 | 0.09 |




Table 8: Top Ten Signals by Λ\Lambda

This table reports the top ten most important signals, Panel A for spread portfolios and Panel B for bivariate sorted portfolios. The columns are abbreviation, theme, time-series average of absolute Λ\Lambda, full name, and original publication of the signals. There are 13 themes following jensen2023there.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Abbreviation | Theme | Λ\Lambda | Full Name | Publication |
| Panel A: Spread Portfolio | | | | | |
| 2 | aliq\_at | Investment | 0.139 | Liquidity of book assets | ortiz2014real |
| 34 | div12m\_me | Value | 0.126 | Dividend yield | litzenberger1979effect |
| 7 | at\_me | Value | 0.125 | Assets-to-market | eugene1992cross |
| 9 | be\_gr1a | Investment | 0.125 | Change in common equity | richardson2005accrual |
| 44 | emp\_gr1 | Investment | 0.123 | Hiring rate | belo2014labor |
| 45 | eq\_dur | Value | 0.123 | Equity duration | dechow2004implied |
| 24 | col\_gr1a | Investment | 0.123 | Change in current ope. lia. | richardson2005accrual |
| 116 | sale\_gr3 | Investment | 0.123 | Sales growth (3 years) | lakonishok1994contrarian |
| 15 | bev\_mev | Value | 0.121 | Book-to-market equity | penman2007book |
| 10 | be\_me | Value | 0.120 | Book-to-market enterprise value | rosenberg1985persuasive |
| Panel B: BiSort Portfolio | | | | | |
| 71 | ni\_be | Profitability | 0.141 | Return on equity | haugen1996commonality |
| 86 | ope\_bel1 | Profitability | 0.138 | Ope. profits-to-lagged be | fama2015five |
| 85 | ope\_be | Profitability | 0.136 | Operating profits-to-be | fama2015five |
| 77 | o\_score | Profitability | 0.135 | Ohlson O-score | dichev1998risk |
| 42 | ebit\_sale | Profitability | 0.134 | Profit margin | soliman2008use |
| 90 | prc | Size | 0.133 | Price per share | miller1982dividends |
| 41 | ebit\_bev | Profitability | 0.132 | Return on net operating assets | soliman2008use |
| 16 | bidaskhl\_21d | Low Leverage | 0.130 | The high-low bid-ask spread | corwin2012simple |
| 65 | mispricing\_perf | Quality | 0.126 | Performance Based Mispricing | stambaugh2017 |
| 58 | ivol\_capm\_252d | Low Risk | 0.126 | Idio. vol. to CAPM (21 days) | ali2003arbitrage |

Figure 2: Signal Importance

This figure depicts the heatmaps of signal importance Λ\Lambda for each rolling-window estimation.
Sub-figures (a) and (b) are for spread portfolios and bivariate sorted portfolios, respectively.
For interpretation, we focus on the absolute value of elements in Λ\Lambda.
We calculate the theme-level importance as the average of all signal-level importance within each theme.
There are 13 themes following jensen2023there.

![Refer to caption](x3.png)


(a) Spread Portfolio: Theme-Level

![Refer to caption](x4.png)


(b) BiSort Portfolio: Theme-Level

### 5.3 Signal Importance

To understand the economic underpinnings of our Sharpe ratio-maximizing strategies or SDF, we examine the estimated values of Λ\Lambda, which assign weights to firm-level predictive signals. These weights reflect the relative contribution of each signal to the SDF. We focus on the absolute value of these weights averaged over time to assess long-term signal importance.
Table [8](https://arxiv.org/html/2602.20856v1#S5.T8 "Table 8 ‣ 5.2.4 Evolution of Sharpe Ratios over the Sample Period ‣ 5.2 Zero-Cost Linear Strategies ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") presents the ten most influential signals, ranked by their time-series average of absolute |Λ||\Lambda| values, where Panel A is for spread portfolios and Panel B is for bivariate sorted portfolios.

Panel A, investing in spread portfolios, indicates that the most important signals are concentrated in the *investment* and *value* categories. For instance, the top signal—*liquidity of book assets* (ortiz2014real)—receives an average importance of 0.139, while *dividend yield* (litzenberger1979effect), the leading signal in the value theme, ranks seventh overall with an importance of 0.126. These findings suggest that the strategy places greater emphasis on firm fundamentals linked to capital structure, financing constraints, and valuation, rather than technical or return-based indicators.

As for Panel B, *profitability* dominates the top ten signals, followed by *size*, *low leverage*, and *low risk* themes. For instance, *return on equity* (haugen1996commonality) and *operating profitability-to-lagged book equity* (fama2015five) are top signals, all belonging to *profitability*.
Besides, *price per share* (miller1982dividends) emerges from the *size* theme, recalling stronger size effects in the test assets sorted on size and other signals.

Figure [2](https://arxiv.org/html/2602.20856v1#S5.F2 "Figure 2 ‣ 5.2.4 Evolution of Sharpe Ratios over the Sample Period ‣ 5.2 Zero-Cost Linear Strategies ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") presents the importance measures for all 138 signals, organized into 13 thematic categories (as defined in the Data section). Sub-figures (a) and (b) display theme-level importance for spread portfolios and bivariate-sorted portfolios, respectively.666We provide the time-varying signal-level importance measures in Figure [F.1](https://arxiv.org/html/2602.20856v1#A6.F1 "Figure F.1 ‣ Appendix F Signal-Level Importance ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") of the Appendix [F](https://arxiv.org/html/2602.20856v1#A6 "Appendix F Signal-Level Importance ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work."). The heatmap visualization employs color intensity to indicate importance levels—with red (blue) representing high (low) importance–allowing clear identification of which signals consistently influence portfolio construction.

In sub-figure (a) for spread portfolios, *investment*- and *value*-related signals dominate the red spectrum, reinforcing the role of tangible firm fundamentals. In contrast, *momentum*, *profit growth*, *debt issuance*, *seasonality*, and *short-term reversal* appear consistently in the blue range, indicating minimal weight in the Sharpe ratio-maximizing SDF.

Turning to sub-figure (b) for bivariate-sorted portfolios, the *profitability* theme dominates the heatmap, particularly following a pronounced regime shift in the late 1980s. The *size* theme exhibits persistent importance throughout the sample period, reflecting the strong cross-sectional dispersion in firm size within our test assets. In contrast, *accruals*, *profit growth*, *seasonality*, and *short-term reversal* show consistently low importance over the entire sample.

Our analysis reveals that while the dominant predictive role of *investment*, *value*, *profitability*, and *size* themes remains stable over time, certain signals—particularly *accruals* and *quality*—exhibit heightened importance during high-volatility or low-sentiment periods. This time variation suggests dynamic shifts in return predictability patterns, which our framework successfully captures through its adaptive structure.

In summary, our signal importance analysis demonstrates that the cross-predictive SDF is primarily driven by *stable, economically grounded predictors*, with negligible dependence on transient or noisy effects. These findings not only underscore the robustness and economic interpretability of our framework but also open new avenues for investigating the fundamental drivers of cross-sectional return predictability.

### 5.4 Networks in the Cross Section

To uncover the economic structure embedded in the cross-predictive matrix Ψ\Psi, we interpret Ψ\Psi as the adjacency matrix of a directed network across NN assets. This representation enables us to move beyond portfolio-level effects and examine how predictive information flows through the cross-section. That is we identify assets that function as net transmitters or receivers of signals and assessing the alignment of these linkages with economic groupings such as firm size.

Following the connectedness methodology of diebold2014network, we compute three metrics for each asset ii—outgoing connectedness (FROM\mathrm{FROM}), incoming connectedness (TO\mathrm{TO}) and net connectedness (NET\mathrm{NET})—along with a market-level overall network intensity (TOTAL\mathrm{TOTAL}).
Let Ψi,j\Psi\_{i,j} denote the predictive influence of asset ii on asset jj. We define the network metrics as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | FROMi\displaystyle\mathrm{FROM}\_{i} | =∑j=1j≠iN|Ψi,j|,\displaystyle=\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{N}|\Psi\_{i,j}|, |  | (26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | TOj\displaystyle\mathrm{TO}\_{j} | =∑i=1i≠jN|Ψi,j|,\displaystyle=\sum\_{\begin{subarray}{c}i=1\\ i\neq j\end{subarray}}^{N}|\Psi\_{i,j}|, |  | (27) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | NETk\displaystyle\mathrm{NET}\_{k} | =TOk−FROMk,\displaystyle=\mathrm{TO}\_{k}-\mathrm{FROM}\_{k}, |  | (28) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | TOTAL\displaystyle\mathrm{TOTAL} | =1N​∑i,j=1i≠jN|Ψi,j|.\displaystyle=\frac{1}{N}\sum\_{\begin{subarray}{c}i,j=1\\ i\neq j\end{subarray}}^{N}|\Psi\_{i,j}|. |  | (29) |

Here, FROMi\mathrm{FROM}\_{i} measures the total strength of predictive signals sent from asset ii to others, capturing how much ii contributes to forecasting the returns of other assets.
TOj\mathrm{TO}\_{j} measures the total strength of predictive signals received by asset jj from all other assets, reflecting how much jj is influenced by the rest of the network.
NETk\mathrm{NET}\_{k} is the difference between incoming and outgoing connectedness, indicating whether asset kk is a net transmitter (<0<0) or net receiver (>0>0) of predictive information.
TOTAL\mathrm{TOTAL} aggregates the overall off-diagonal magnitude of Ψ\Psi across all asset pairs, summarizing the average intensity of cross-asset predictive linkages in the network.
The use of absolute values follows diebold2014network and ensures all measures are non-negative, thereby capturing signal strength regardless of sign.

We compute these metrics monthly for two asset universes—138 spread portfolios and 544 bivariate sorted portfolios—over T=611T=611 months. To investigate the firm-level characteristics driving variation in connectedness, we estimate monthly cross-sectional regressions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Connectednessi,t=αt+𝜷′​Chari,t+εi,t,\mathrm{Connectedness}\_{i,t}=\alpha\_{t}+\boldsymbol{\beta}^{\prime}\mathrm{Char}\_{i,t}+\varepsilon\_{i,t}, |  | (30) |

where Connectednessi,t\mathrm{Connectedness}\_{i,t} is one of FROMi\mathrm{FROM}\_{i}, TOi\mathrm{TO}\_{i}, or NETi\mathrm{NET}\_{i}, and Chari,t\mathrm{Char}\_{i,t} is a vector of observable characteristics. We report time-series averages of the estimated coefficients along with Newey–West (neweywest1987) tt-statistics using a Bartlett kernel and lag length L=4​(T/100)2/9≈5L=4(T/100)^{2/9}\approx 5.

Table [9](https://arxiv.org/html/2602.20856v1#S5.T9 "Table 9 ‣ 5.4 Networks in the Cross Section ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") reports the results of monthly cross-sectional regressions of three network connectedness measures—FROM\mathrm{FROM}, TO\mathrm{TO}, and NET\mathrm{NET}—on firm characteristics for two groups of test assets: spread portfolios (Panel A) and bivariate sorted portfolios (Panel B). The results reveal economically intuitive patterns linking a stock’s network role to size, valuation, profitability, investment, momentum, and several trading frictions.

In Panel A for spread portfolios, the FROM\mathrm{FROM} regressions, measuring how much a stock helps predict others, we observe that smaller stocks (low ME), high book-to-market (BM), high profitability (OP), and high momentum (MOM) stocks tend to transmit stronger signals to others. These firms—small, value, profitable, and past winners—have greater forecasting influence, possibly because they aggregate market-wide information or drive co-movements.
Additionally, stocks with low illiquidity (ILL) and low turnover (TRN) exhibit higher FROM, suggesting that liquidity increase a stock’s impact to the network. Volatility (VLT), by contrast, enters positively, implying that more volatile stocks spill predictive attention. Notably, the coefficient on size (ME) becomes insignificant, once controlling five trading frictions, which means that the size effect on FROM\mathrm{FROM} is a manifestation of trading frictions but not size itself.

The TO\mathrm{TO} regressions, which capture how strongly a stock is predicted by others, show the opposite patterns on many characteristics.
Stocks with high ME, high BM, low OP, low INV, high MOM, high VLT, and high BETA receive more predictive inputs from others.
This suggests that firms that are large, volatile, illiquid, and priced as value stocks appear more susceptible to being forecasted using cross-asset information.
Interestingly, high-MOM stocks both receive and transmit signals, indicating they may act as informational amplifiers within the network.

The NET\mathrm{NET} regressions, defined as TO−FROM\mathrm{TO}-\mathrm{FROM}, consolidate these effects to identify whether a stock is a net receiver or transmitter of predictive information. Stocks that are large (high-ME), low-BM, low-OP, low-INV, and low-MOM tend to be net receivers, while small, value, profitable, non-investing, and momentum-driven stocks are net transmitters.
These directional patterns highlight a persistent asymmetry:
small, value, strong profitability, and conservative investment firms disseminate predictive signals,
while larger and illiquid firms absorb them.

In Panel B for bivariate sorted portfolio, these patterns still exist. For ease of interpretation, we focus on the NET\mathrm{NET} regressions. We find that small, low-BM, high-OP, low-INV, and low-MOM firms are net receivers in the network, while big, value, weak-profitable, conservative-investing, and high-momentum stocks are net transmitters.
After controlling five trading frictions in the regressions, the coefficient on size become significantly positive, while other four coefficients are unchanged.
As for trading frictions, stocks with low volume, low volatility, high turnover, and low market-beta tend to receive spillovers from others than transmitting signals to others.

Together, two sets of test assets demonstrate significant correlations between network connectedness and asset characteristics, shedding light on that the determinants of cross-asset spillover effects. The estimated Ψ\Psi matrix embeds an economically interpretable hierarchy of signal flows, shaped by firm fundamentals and market frictions. This structure supports imposing sparsity or blockwise restrictions to enhance interpretability and control overfitting—especially by limiting signal flows that contradict observed economic asymmetries.
Nevertheless, the correlation between connectedness and asset characteristics depends on the choice of test assets. That is, different test assets reflect different patterns in asset pricing, see feng2020taming; avramov2025sparse.
In this specific exercise, we confirm the prominent status of size as an asset characteristic in building sorted portfolios as test assets (fama1993common).

Table [9](https://arxiv.org/html/2602.20856v1#S5.T9 "Table 9 ‣ 5.4 Networks in the Cross Section ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") connects to several literature.
For bivariate portfolios (Panel B), we initially corroborate lo1990contrarian, finding big stocks lead small stocks (coefficient -0.15, row 1 on NET\mathrm{NET})—a result robust to controlling for BM, OP, INV, and MOM (coefficient -0.19, row 2). However, controlling for trading frictions reverses the size coefficient, suggesting big stocks become net receivers, warranting further investigation of size’s role in lead-lag effects.777For comparability, we replicate results for 1973-1987 (matching lo1990contrarian’s sample end) and find consistent size coefficient signs.
Contrary to chordia2000trading, we find low-turnover stocks transmit signal to high-turnover stocks after controlling for size.888While chordia2000trading uses ”Trading Volume” in their title, they actually employ daily turnover as their volume proxy. It holds for both spread and bivariate sorts.
The divergence from prior papers reflects discretion in test assets and sample periods. Moreover, the two papers focus exclusively on weekly return spillovers, whereas we incorporate multiple firm-level monthly signals, including past returns. Collectively, we demonstrate that cross-asset spillovers are fundamentally linked to asset characteristics.

Figure [3](https://arxiv.org/html/2602.20856v1#S5.F3 "Figure 3 ‣ 5.4 Networks in the Cross Section ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") depicts the TOTAL\mathrm{TOTAL} connectedness index—the average intensity of the off-diagonal elements in Ψ\Psi—for both the 138 spread portfolios (dashed line) and the 544 bi-sort portfolios (solid line) over the 1973–2023 period. Four key findings emerge.
First, the time-series of TOTAL\mathrm{TOTAL} connectedness on the spread portfolios varies markedly through time: it troughs in the mid-1980s and again after 2020, but peaks around the early 1990s and during the post financial crises, 2010s.
Second, the indices for bivariate sorted portfolios share the trough in mid-1980s and peak in early 1990s, however, slight fluctuations after 2000.
Overall, the average level of TOTAL\mathrm{TOTAL} of spread portfolios is almost equal to that of bivariate sorted portfolios before 2000, but become higher after 2000.
Third, despite these episodic surges, the time series reverts to a long-run mean near 0.72, suggesting a stable baseline level of cross-asset information transmission.

Taken together, Figure [3](https://arxiv.org/html/2602.20856v1#S5.F3 "Figure 3 ‣ 5.4 Networks in the Cross Section ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") demonstrates that cross-asset spillover effects intensify during turbulent periods but persist as a pervasive market feature. These findings underscore the importance of modeling the full Ψ\Psi matrix—rather than restricting attention to its diagonal elements—for constructing Sharpe ratio-maximizing portfolios.

Table 9: Understanding Connectedness

This table reports the time-series average and the neweywest1987 tt-statistics of cross-sectional regressions estimates for each month that regress a connectedness measure on asset characteristics. The assets are 138 spread portfolios in Panel A, and 544 bivariate sorted portfolios in Panel B.
For ease of interpretation, the coefficients are reported with values multiplied by 1000.
There are three connectedness measures: FROM\mathrm{FROM}, TO\mathrm{TO}, and NET\mathrm{NET}.
The characteristics of interest are size (“market\_equity”), book-to-market equity (“be\_me”), operating profits-to-lagged book equity (“ope\_bel1”), asset growth (“at\_gr1”), price momentum t-12 to t-1 (“ret\_12\_1”),
Amihud illiquidity(“ami\_126d”),
volume(“dolvol\_126d”),
volatility(“rvol\_21d”),
turnover(“turnover\_126d”),
CAPM beta (“beta\_60m”),
with abbreviations ME, BM, INV, OP, MOM, ILL, VLM, VLT, TRN, and BETA.
There is an intercept in the regression, but the estimates are omitted in the table.
The sample period is from February 1973 to December 2023.

|  | ME | BM | OP | INV | MOM | ILL | VLM | VLT | TRN | BETA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Panel A: Spread Portfolio | | | | | | | | | | |
| FROM | -1.26 |  |  |  |  |  |  |  |  |  |
| (-9.39) |  |  |  |  |  |  |  |  |  |
| -2.62 | 7.78 | 4.75 | 0.80 | 4.83 |  |  |  |  |  |
| (-7.62) | (16.82) | (8.39) | (3.86) | (20.28) |  |  |  |  |  |
| 0.37 | 8.9 | 7.04 | 0.41 | 6.47 | -7.49 | -7.04 | 4.68 | -2.49 | -0.07 |
| (0.16) | (27.91) | (14.08) | (1.66) | (21.42) | (-1.35) | (-1.5) | (7.36) | (-2.58) | (-0.19) |
| TO | 0.72 |  |  |  |  |  |  |  |  |  |
| (3.19) |  |  |  |  |  |  |  |  |  |
| 1.65 | 0.90 | -2.79 | -1.66 | 2.63 |  |  |  |  |  |
| (7.22) | (3.27) | (-7.43) | (-9.71) | (7.77) |  |  |  |  |  |
| 17.47 | 2.84 | -1.06 | -1.77 | 4.03 | -4.29 | -15.46 | 5.55 | -1.90 | 2.03 |
| (8.3) | (11.55) | (-3.01) | (-10.42) | (9.79) | (-1.11) | (-3.55) | (13.35) | (-2.14) | (5.38) |
| NET | 1.98 |  |  |  |  |  |  |  |  |  |
| (6.45) |  |  |  |  |  |  |  |  |  |
| 4.27 | -6.88 | -7.53 | -2.46 | -2.20 |  |  |  |  |  |
| (9.78) | (-14.07) | (-11.09) | (-11.32) | (-6.05) |  |  |  |  |  |
| 17.09 | -6.06 | -8.10 | -2.19 | -2.44 | 3.19 | -8.42 | 0.86 | 0.58 | 2.11 |
| (4.36) | (-19.12) | (-13.52) | (-8.65) | (-4.45) | (0.49) | (-1.42) | (1.06) | (0.38) | (4.22) |
| Panel B: BiSort Portfolio | | | | | | | | | | |
| FROM | 0.25 |  |  |  |  |  |  |  |  |  |
| (12.53) |  |  |  |  |  |  |  |  |  |
| 0.36 | 0.38 | -0.30 | 0.59 | 0.52 |  |  |  |  |  |
| (13.77) | (16.23) | (-16.54) | (20.59) | (20.31) |  |  |  |  |  |
| 0.32 | 0.53 | -0.16 | 0.69 | 0.73 | 1.39 | 2.22 | 0.56 | -0.93 | -0.03 |
| (1.21) | (18.89) | (-6.22) | (19.2) | (15.16) | (2.36) | (2.98) | (7.82) | (-4.57) | (-0.41) |
| TO | 0.10 |  |  |  |  |  |  |  |  |  |
| (1.66) |  |  |  |  |  |  |  |  |  |
| 0.17 | -0.26 | 0.07 | -0.33 | -0.06 |  |  |  |  |  |
| (2.86) | (-4.79) | (0.95) | (-5.14) | (-0.85) |  |  |  |  |  |
| 3.82 | -0.05 | 0.41 | -0.45 | -0.04 | 0.77 | -3.96 | -0.23 | 2.34 | -0.50 |
| (8.13) | (-0.68) | (5.21) | (-6.84) | (-0.54) | (0.7) | (-3.99) | (-1.65) | (10.22) | (-3.7) |
| NET | -0.15 |  |  |  |  |  |  |  |  |  |
| (-2.41) |  |  |  |  |  |  |  |  |  |
| -0.19 | -0.64 | 0.38 | -0.92 | -0.58 |  |  |  |  |  |
| (-3.35) | (-11.56) | (4.54) | (-11.36) | (-10.22) |  |  |  |  |  |
| 3.50 | -0.59 | 0.58 | -1.14 | -0.77 | -0.63 | -6.18 | -0.79 | 3.27 | -0.47 |
| (6.05) | (-7.97) | (6.49) | (-13.19) | (-10.66) | (-0.63) | (-5.47) | (-5.92) | (9.36) | (-3.2) |

Figure 3: Total Connectedness

This figure depicts the time-series plot of total connectedness of Ψ\Psi matrix over OOS period form February 1973 to December 2023. The blue dash line is for 138 spread portfolios, and the orange solid line is for 544 bivariate sorted portfolios.
The shadow areas indicate for NBER recession periods.

![Refer to caption](x5.png)

To analyze directional spillover effects in the bivariate-sorted portfolios more precisely, we decompose the Ψ\Psi matrix into four blocks (A, B, C, and D) according to firm size. Figure [4](https://arxiv.org/html/2602.20856v1#S5.F4 "Figure 4 ‣ 5.4 Networks in the Cross Section ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") presents the resulting predictive information flows across these partitions.

Figure [5](https://arxiv.org/html/2602.20856v1#S5.F5 "Figure 5 ‣ 5.4 Networks in the Cross Section ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") presents the time series of absolute average values for each of the four blocks in Ψ\Psi.
The results reveal consistently stronger predictive relations in Block A (Small →\rightarrow Small) and Block C (Big →\rightarrow Small) compared to Block B (Small →\rightarrow Big) and Block D (Big →\rightarrow Big), particularly during the last two decades. The time-series averages are 1.50 and 1.53 for Blocks A and C, respectively, versus 1.09 and 1.11 for Blocks B and D. Notably, the divergence between the A/C and B/D blocks has increased substantially in recent years.

These findings confirm an asymmetric predictive structure, which aligns with the NET\mathrm{NET} regression coefficient of −0.15-0.15 reported in Panel B of Table [9](https://arxiv.org/html/2602.20856v1#S5.T9 "Table 9 ‣ 5.4 Networks in the Cross Section ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work."). This result is consistent with the evidence in lo1990contrarian, showing that large stocks tend to lead small stocks, but not vice versa. The persistent and stable nature of these patterns over time supports the economic rationale for imposing restrictions on Ψ\Psi, particularly by excluding small-to-large predictive links. Furthermore, the long-run regularity of these asymmetries suggests that dynamic sparsity structures—which adapt to time-varying network block strengths while maintaining economically motivated constraints—could offer significant modeling value.

In summary, the connectedness analysis reveals that the connection matrix Ψ\Psi encodes economically meaningful structure. For bivariate sorted portfolios on size and other signals, big stocks act as net transmitters of predictive signals; controlling more signals, we find that low trading volume, high turnover ratio, and low-beta stocks are net transmitters. Meanwhile, value, profitable, non-investing, and high-momentum assets are more likely to be net receivers. The strength of cross-predictive relations is comparable to that of self-predictive effects. The overall network intensity fluctuates over time, but remains around a stable level. Decomposing Ψ\Psi by firm size shows that predictive flows from large to small firms dominate those in the reverse direction.

Figure 4: Partition of Ψ\Psi in Size.

This figure decomposes the Ψ\Psi matrix to four blocks based on firm size. They are:

* •

  A: Small (Stock Signals) →\rightarrow Small (Stock Returns),
* •

  B: Small →\rightarrow Big,
* •

  C: Big →\rightarrow Small,
* •

  D: Big →\rightarrow Big.

ABCDSmall SignalBig SignalSmall ReturnBig Return

Figure 5: Absolute Average of Four Blocks in Ψ\Psi: BiSort Portfolios

This figure shows the time-series plot of the absolute average of elements in four blocks of Ψ\Psi.
The basic assets are the bivariate sorted portfolios, where four blocks A, B, C, and D represent the strength of cross-predictive relations for
(1) small stock signals predict small stock returns,
(2) small stock signals predict big stock returns,
(3) big stock signals predict small stock returns,
and
(4) big stock signals predict big stock returns.
The sample period is form February 1973 to December 2023.
The shadow areas indicate for NBER recession periods.

![Refer to caption](x6.png)

## 6 Conclusion

This paper develops a structured framework for constructing Sharpe ratio–maximizing investment strategies using multiple firm-level signals and accounting for informational linkages across assets. By jointly estimating signal relevance and a matrix capturing cross-asset predictive relationships, our approach yields closed-form portfolio weights derived from a generalized eigenvalue decomposition. In high-dimensional settings, estimation is implemented through Ridge-SDF regressions, which offer a stable and interpretable managed-portfolio representation of the decision variables. The resulting stochastic discount factor consistently delivers high out-of-sample Sharpe ratios across a range of asset universes and market conditions, outperforming both self-predictive models and expected return-maximization. Economically, the strategy is primarily driven by fundamental characteristics related to investment, valuation, and profitability. In addition, the estimated connection matrix reveals that large and low-turnover stocks tend to act as net transmitters of predictive signals, while the overall strength of cross-asset linkages remains persistently high over time.

The paper opens several promising avenues for future research. First, the framework could be extended to other asset classes where cross-asset interdependencies are economically meaningful, such as corporate bonds, currencies, sovereign credit, or international equities. For instance, in the corporate bond market, issuer fundamentals or equity-side information may predict bond returns through industry linkages, shared ownership networks, or common analyst coverage. Similarly, in currency markets, major reserve currencies may act as informational hubs whose movements help forecast subsequent shifts in peripheral currencies. Second, incorporating economic structure into the modeling of cross-asset relationships could enhance both interpretability and predictive performance. As the number of assets and signals expands, estimating all possible interactions becomes increasingly challenging. Imposing economically motivated constraints—such as directional spillovers based on firm size or sectoral hierarchies—could provide a more structured and scalable approach.

## References

\appendixpage

## Appendix A Proof of Proposition [1](https://arxiv.org/html/2602.20856v1#Thmproposition1 "Proposition 1. ‣ 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")

##### Expected Return

We first express πs\pi\_{s}, the realized return on the trading strategy, as a function of the model parameters.
Recognize that πs=Λ′​St′​Ψ​rs=∑i=1NΨi′​rs​Si​t′​Λ=tr​[Λ​∑i=1NΨi′​Πs​i]=Λ′​Πs′​Φ\pi\_{s}=\Lambda^{\prime}S^{\prime}\_{t}\Psi r\_{s}=\sum\_{i=1}^{N}\Psi\_{i}^{\prime}r\_{s}S\_{it}^{\prime}\Lambda=\text{tr}\left[\Lambda\sum\_{i=1}^{N}\Psi\_{i}^{\prime}\Pi\_{si}\right]=\Lambda^{\prime}\Pi\_{s}^{\prime}\Phi, where Ψi′\Psi\_{i}^{\prime} is a 1×N1\times N vector which is the ii-th row of Ψ\Psi, Si​t′S\_{it}^{\prime} is a 1×M1\times M vector, which is the ii-th row of StS\_{t}, tr stands for the trace operator, and Πs\Pi\_{s} is an N2×MN^{2}\times M matrix that vertically stacks the N×MN\times M matrices Πs​i=rs​Si​t′\Pi\_{si}=r\_{s}S\_{it}^{\prime} for i=1,2,⋯,Ni=1,2,\cdots,N.

Then, on the basis of realized return, the expected value is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(πs)=Λ′​Π′​Φ=Φ′​Π​Λ.E(\pi\_{s})=\Lambda^{\prime}{\Pi}^{\prime}\Phi=\Phi^{\prime}{\Pi}\Lambda. |  | (A.1) |

##### Variance

Let ΣΦ\Sigma\_{\Phi} be the covariance matrix of vec​(Πs′)\text{vec}(\Pi\_{s}^{\prime}). We express πs\pi\_{s} in terms of vec​(Πs′)\text{vec}(\Pi\_{s}^{\prime}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | πs=Λ′​Πs′​Φ=Λ′​vec​(Πs′​Φ).\pi\_{s}=\Lambda^{\prime}\Pi\_{s}^{\prime}\Phi=\Lambda^{\prime}\text{vec}(\Pi\_{s}^{\prime}\Phi). |  | (A.2) |

Using the property of vectorization vec​(A​B​C)=(C′⊗A)​vec​(B)\text{vec}(ABC)=(C^{\prime}\otimes A)\text{vec}(B),
we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vec​(Πs′​Φ)=(Φ′⊗IM)​vec​(Πs′).\text{vec}(\Pi\_{s}^{\prime}\Phi)=(\Phi^{\prime}\otimes I\_{M})\text{vec}(\Pi\_{s}^{\prime}). |  | (A.3) |

Therefore:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πs=Λ′​(Φ′⊗IM)​vec​(Πs′).\pi\_{s}=\Lambda^{\prime}(\Phi^{\prime}\otimes I\_{M})\text{vec}(\Pi\_{s}^{\prime}). |  | (A.4) |

The variance of πs\pi\_{s} is:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Var​(πs)\displaystyle\text{Var}(\pi\_{s}) | =\displaystyle= | Λ′​(Φ′⊗IM)​ΣΦ​(Φ⊗IM)​Λ,\displaystyle\Lambda^{\prime}(\Phi^{\prime}\otimes I\_{M})\Sigma\_{\Phi}(\Phi\otimes I\_{M})\Lambda, |  | (A.5) |
|  |  | =\displaystyle= | Λ′​BΦ​Λ,\displaystyle\Lambda^{\prime}B\_{\Phi}\Lambda, |  |

where BΦ=(Φ′⊗IM)​ΣΦ​(Φ⊗IM).B\_{\Phi}=(\Phi^{\prime}\otimes I\_{M})\Sigma\_{\Phi}(\Phi\otimes I\_{M}).

We consider an alternative expression of Var​(πs)\text{Var}(\pi\_{s}). Let ΣΛ\Sigma\_{\Lambda} be the covariance matrix of vec​(Πs)\text{vec}(\Pi\_{s}). We express πs\pi\_{s} in terms of vec​(Πs)\text{vec}(\Pi\_{s}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | πs=Φ′​Πs​Λ=Φ′​vec​(Πs​Λ).\pi\_{s}=\Phi^{\prime}\Pi\_{s}\Lambda=\Phi^{\prime}\text{vec}(\Pi\_{s}\Lambda). |  | (A.6) |

Again using the property of vectorization, we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vec​(Πs​Λ)=(Λ′⊗IN2)​vec​(Πs).\text{vec}(\Pi\_{s}\Lambda)=(\Lambda^{\prime}\otimes I\_{N^{2}})\text{vec}(\Pi\_{s}). |  | (A.7) |

Therefore:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πs=Φ′​(Λ′⊗IN2)​vec​(Πs).\pi\_{s}=\Phi^{\prime}(\Lambda^{\prime}\otimes I\_{N^{2}})\text{vec}(\Pi\_{s}). |  | (A.8) |

The variance of πs\pi\_{s} is:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Var​(πs)\displaystyle\text{Var}(\pi\_{s}) | =\displaystyle= | Φ′​(Λ′⊗IN2)​ΣΛ​(Λ⊗IN2)​Φ,\displaystyle\Phi^{\prime}(\Lambda^{\prime}\otimes I\_{N^{2}})\Sigma\_{\Lambda}(\Lambda\otimes I\_{N^{2}})\Phi, |  | (A.9) |
|  |  | =\displaystyle= | Φ′​BΛ​Φ,\displaystyle\Phi^{\prime}B\_{\Lambda}\Phi, |  |

where BΛ=(Λ′⊗IN2)​ΣΛ​(Λ⊗IN2).B\_{\Lambda}=(\Lambda^{\prime}\otimes I\_{N^{2}})\Sigma\_{\Lambda}(\Lambda\otimes I\_{N^{2}}).

##### Sharpe Ratio

With the expected return and variance, we express the Sharpe ratio square as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​R2=Λ′​AΦ​ΛΛ′​BΦ​Λ,SR^{2}=\frac{\Lambda^{\prime}A\_{\Phi}\Lambda}{\Lambda^{\prime}B\_{\Phi}\Lambda}, |  | (A.10) |

where AΦ=Π′​Φ​Φ′​Π,BΦ=(Φ′⊗IM)​ΣΦ​(Φ⊗IM)A\_{\Phi}=\Pi^{\prime}\Phi\Phi^{\prime}\Pi,B\_{\Phi}=\left(\Phi^{\prime}\otimes I\_{M}\right)\Sigma\_{\Phi}\left(\Phi\otimes I\_{M}\right), and ΣΦ\Sigma\_{\Phi} is the covariance matrix of vec​(Πs′)\text{vec}(\Pi\_{s}^{\prime}). Alternatively, we express the Sharpe ratio squared as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​R2=Φ′​AΛ​ΦΦ′​BΛ​Φ,SR^{2}=\frac{\Phi^{\prime}A\_{\Lambda}\Phi}{\Phi^{\prime}B\_{\Lambda}\Phi}, |  | (A.11) |

where AΛ=Π​Λ​Λ′​Π′,BΛ=(Λ′⊗IN2)​ΣΛ​(Λ⊗IN2)A\_{\Lambda}=\Pi\Lambda\Lambda^{\prime}\Pi^{\prime},B\_{\Lambda}=\left(\Lambda^{\prime}\otimes I\_{N^{2}}\right)\Sigma\_{\Lambda}\left(\Lambda\otimes I\_{N^{2}}\right), and ΣΛ\Sigma\_{\Lambda} is the covariance matrix of vec​(Πs)\text{vec}(\Pi\_{s}). These alternative expressions of S​R2SR^{2} assist in finding the solution to maximize the Sharpe ratio.

## Appendix B Relating Φ\Phi to BB When M=1M=1

##### Setup.

Consider the return-generating process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rs=B​St+εs,r\_{s}=BS\_{t}+\varepsilon\_{s}, |  | (B.1) |

where:

* •

  St∈ℝN×1S\_{t}\in\mathbb{R}^{N\times 1} is the signal vector,
* •

  B∈ℝN×NB\in\mathbb{R}^{N\times N} is the slope matrix,
* •

  εs∼(0,Σε)\varepsilon\_{s}\sim(0,\Sigma\_{\varepsilon}) is a zero-mean innovation,
* •

  ΣS=𝔼​[St​St′]\Sigma\_{S}=\mathbb{E}[S\_{t}S\_{t}^{\prime}] is the signal covariance matrix.

##### Managed-Portfolio Return.

The managed-portfolio return vector is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πs=(IN⊗rs)​St.\Pi\_{s}=(I\_{N}\otimes r\_{s})S\_{t}. |  | (B.2) |

Taking expectations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π=𝔼​[Πs]=vec​(𝔼​[rs​St′])=vec​(B​ΣS).\Pi=\mathbb{E}[\Pi\_{s}]=\text{vec}(\mathbb{E}[r\_{s}S\_{t}^{\prime}])=\text{vec}(B\Sigma\_{S}). |  | (B.3) |

In the case of a single signal, both Π\Pi and Πs\Pi\_{s} are vectors of dimension N2N^{2}, and ΣΛ\Sigma\_{\Lambda} denotes the covariance matrix of Πs\Pi\_{s}.

##### Sharpe Ratio Maximization.

We maximize the Sharpe ratio subject to ‖Φ‖=1\|\Phi\|=1:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxΦ:‖Φ‖=1⁡Φ′​ΠΦ′​ΣΛ​Φ.\max\_{\Phi:\|\Phi\|=1}\frac{\Phi^{\prime}\Pi}{\sqrt{\Phi^{\prime}\Sigma\_{\Lambda}\Phi}}. |  | (B.4) |

The optimal solution is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ=ΣΛ−1​vec​(B​ΣS)‖ΣΛ−1​vec​(B​ΣS)‖.\Phi=\frac{\Sigma\_{\Lambda}^{-1}\text{vec}(B\Sigma\_{S})}{\|\Sigma\_{\Lambda}^{-1}\text{vec}(B\Sigma\_{S})\|}. |  | (B.5) |

Thus, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B=unvec​(ΣΛ​Φ)⋅ΣS−1,B=\text{unvec}(\Sigma\_{\Lambda}\Phi)\cdot\Sigma\_{S}^{-1}, |  | (B.6) |

where unvec\operatorname{unvec} denotes the reshaping of an N2N^{2}-vector into an N×NN\times N matrix.

##### Expected Return Maximization.

We now maximize expected return subject to ‖Φ‖=1\|\Phi\|=1:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxΦ:‖Φ‖=1⁡Φ′​vec​(B​ΣS)\max\_{\Phi:\|\Phi\|=1}\Phi^{\prime}\text{vec}(B\Sigma\_{S}) |  | (B.7) |

The solution is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ=vec​(B​ΣS)‖vec​(B​ΣS)‖.\Phi=\frac{\text{vec}(B\Sigma\_{S})}{\|\text{vec}(B\Sigma\_{S})\|}. |  | (B.8) |

Inverting gives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B=unvec​(Φ)⋅ΣS−1.B=\text{unvec}(\Phi)\cdot\Sigma\_{S}^{-1}. |  | (B.9) |

##### Intuition: Why Are the BB Matrices Different?

The difference stems from the objective:

* •

  Maximizing Expected Return: aligns Φ\Phi with the direction of highest expected payoff, ignoring variance.
* •

  Maximizing Sharpe Ratio: adjusts for risk by incorporating ΣΛ\Sigma\_{\Lambda}, penalizing high-volatility directions.

## Appendix C Proof of Expected Return Reduction due to Zero-Cost Constraint

Consider the matrix Π\Pi formed by vertically stacking NN matrices Πi\Pi\_{i}, each of dimension N×MN\times M, and let Π~\tilde{\Pi} be the matrix obtained after pre-multiplying each Πi\Pi\_{i} by the matrix Θ\Theta, where Θ=IN−1N​ιN​ιN′\Theta=I\_{N}-\frac{1}{N}\iota\_{N}\iota\_{N}^{\prime}. Here, Θ\Theta is a projection matrix that projects vectors onto the space orthogonal to the vector ιN\iota\_{N} of ones.

Properties of Θ\Theta:

* •

  Θ\Theta is symmetric and idempotent, i.e., Θ2=Θ\Theta^{2}=\Theta and Θ′=Θ\Theta^{\prime}=\Theta, confirming that it is a projection matrix.
* •

  The eigenvalues of Θ\Theta are 0 along the direction of ιN\iota\_{N} and 1 along all directions orthogonal to ιN\iota\_{N}.

Impact on Singular Values:

1. 1.

   The matrix Θ\Theta modifies Πi\Pi\_{i} by removing its component in the direction of ιN\iota\_{N}. This operation reduces the variance in Πi\Pi\_{i} that is aligned with ιN\iota\_{N}.
2. 2.

   Given the singular value decomposition of Π=U​Σ​V′\Pi=U\Sigma V^{\prime}, the transformation Π~=(Θ​Πi)\tilde{\Pi}=(\Theta\Pi\_{i}) can be viewed through the lens of modified singular vectors. Since Θ\Theta acts as an identity on the space orthogonal to ιN\iota\_{N} and zeroes out components along ιN\iota\_{N}, it does not increase the magnitude of any singular vector components.
3. 3.

   The singular values λi​(Π~)\lambda\_{i}(\tilde{\Pi}) of the transformed matrix Π~\tilde{\Pi} correspond to the norms of the vectors Θ​Ui\Theta U\_{i}, where UiU\_{i} are the left singular vectors of Π\Pi. Since Θ\Theta is a projection (and thus a norm-reducing operation except where it acts as the identity), we have:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ‖Θ​Ui‖≤‖Ui‖.\|\Theta U\_{i}\|\leq\|U\_{i}\|. |  | (C.1) |
4. 4.

   Therefore, the singular values of Π~\tilde{\Pi} must satisfy:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | λi​(Π~)≤λi​(Π).\lambda\_{i}(\tilde{\Pi})\leq\lambda\_{i}(\Pi). |  | (C.2) |

   for each ii, because the projection does not increase vector norms and reduces them for vectors with non-zero components in the direction of ιN\iota\_{N}.

To be more precise, the highest singular value of the transformed matrix does not change due to the preservation of the highest singular value by Θ\Theta. However, the transformation induced by Θ\Theta results in a reduction of singular values in the transformed matrix Π~\tilde{\Pi} in the other singular values, leading to a decrease in variance explained by certain components. Specifically, at least one singular value of Π~\tilde{\Pi} is strongly diminished compared to the corresponding singular value of the original matrix Π\Pi. This reduction underscores the effectiveness of the transformation in diminishing the influence of certain components in Π\Pi and highlights its role in variance reduction. Hence, both expected return and risk of the trading strategy are lower in the presence of the zero-cost restriction.

## Appendix D Proof and Derivations for Propositions [4](https://arxiv.org/html/2602.20856v1#Thmproposition4 "Proposition 4. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") and [5](https://arxiv.org/html/2602.20856v1#Thmproposition5 "Proposition 5. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")

This section focuses on maximizing the squared Sharpe ratio of a linear strategy. The results extend naturally to the Sharpe ratio maximization of a nonlinear strategy with an augmented signal space, for which we leave for future research.

Maximizing the squared Sharpe ratio constitutes a generalized Rayleigh quotient problem, which can be solved via an eigenvalue problem. However, in empirical settings, the solution to this eigenvalue problem often becomes ill-conditioned in high-dimensional settings.

To address this issue, we employ Ridge-SDF regressions to estimate the decision variables, providing an intuitive managed-portfolio interpretation. Finally, we present an iterative algorithm to estimate Λ\Lambda and Φ\Phi until convergence. The details are as follows.

##### Define the squared Sharpe ratio as a function of Λ\Lambda.

According to Proposition [1](https://arxiv.org/html/2602.20856v1#Thmproposition1 "Proposition 1. ‣ 2.1 Trading Strategy ‣ 2 Econometric Framework ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work."), the squared Sharpe ratio takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​R2=Λ′​AΦ​ΛΛ′​BΦ​Λ,SR^{2}=\frac{\Lambda^{\prime}A\_{\Phi}\Lambda}{\Lambda^{\prime}B\_{\Phi}\Lambda}, |  | (D.1) |

where AΦ=Π′​Φ​Φ′​ΠA\_{\Phi}=\Pi^{\prime}\Phi\Phi^{\prime}\Pi, BΦ=(Φ′⊗IM)​ΣΦ​(Φ⊗IM)B\_{\Phi}=(\Phi^{\prime}\otimes I\_{M})\Sigma\_{\Phi}(\Phi\otimes I\_{M}), and ΣΦ\Sigma\_{\Phi} is the covariance matrix of vec​(Πs′)\text{vec}(\Pi\_{s}^{\prime}).

##### Maximizing the squared Sharpe ratio with respect to Λ\Lambda.

From ([A.10](https://arxiv.org/html/2602.20856v1#A1.E10 "In Sharpe Ratio ‣ Appendix A Proof of Proposition 1 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")), the optimization problem is formulated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxΛ⁡Λ′​AΦ​ΛΛ′​BΦ​Λ.\max\_{\Lambda}\frac{\Lambda^{\prime}A\_{\Phi}\Lambda}{\Lambda^{\prime}B\_{\Phi}\Lambda}. |  | (D.2) |

This is equivalent to the constrained optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxΛ⁡Λ′​AΦ​Λs.t.Λ′​BΦ​Λ=κ.\max\_{\Lambda}\Lambda^{\prime}A\_{\Phi}\Lambda\quad\text{s.t.}\quad\Lambda^{\prime}B\_{\Phi}\Lambda=\kappa. |  | (D.3) |

Given the norm constraint on Λ\Lambda, we set κ=1\kappa=1 without loss of generality.

Applying the method of Lagrange multipliers, we define the Lagrangian function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(Λ,λ)=Λ′​AΦ​Λ−λ​(Λ′​BΦ​Λ−1).L(\Lambda,\lambda)=\Lambda^{\prime}A\_{\Phi}\Lambda-\lambda(\Lambda^{\prime}B\_{\Phi}\Lambda-1). |  | (D.4) |

Taking derivatives with respect to Λ\Lambda yields the generalized eigenvalue problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | AΦ​Λ=λ​BΦ​Λ.A\_{\Phi}\Lambda=\lambda B\_{\Phi}\Lambda. |  | (D.5) |

Multiplying both sides by BΦ−1B\_{\Phi}^{-1} gives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | BΦ−1​AΦ​Λ=λ​Λ.B\_{\Phi}^{-1}A\_{\Phi}\Lambda=\lambda\Lambda. |  | (D.6) |

Defining CΦ=BΦ−1​AΦC\_{\Phi}=B\_{\Phi}^{-1}A\_{\Phi}, we obtain the standard eigenvalue problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CΦ​Λ=λ​Λ.C\_{\Phi}\Lambda=\lambda\Lambda. |  | (D.7) |

Solving ([D.7](https://arxiv.org/html/2602.20856v1#A4.E7 "In Maximizing the squared Sharpe ratio with respect to Λ. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) provides the eigenvector corresponding to the largest eigenvalue, Λmax\Lambda\_{\text{max}}. Normalizing for the norm constraint, we set:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ=Λmax‖Λmax‖.\Lambda=\frac{\Lambda\_{\text{max}}}{||\Lambda\_{\text{max}}||}. |  | (D.8) |

Since the solution for Λ\Lambda depends on Φ\Phi, we define the function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ=arg​maxΛ⁡Λ′​AΦ​ΛΛ′​BΦ​Λ=𝚲​(Φ).\Lambda=\operatorname\*{arg\,max}\_{\Lambda}\frac{\Lambda^{\prime}A\_{\Phi}\Lambda}{\Lambda^{\prime}B\_{\Phi}\Lambda}=\mathbf{\Lambda}(\Phi). |  | (D.9) |

##### Estimating high-dimensional Λ\Lambda using ridge regression.

In high-dimensional settings where MM is large relative to the number of observations TT, the solution in ([D.9](https://arxiv.org/html/2602.20856v1#A4.E9 "In Maximizing the squared Sharpe ratio with respect to Λ. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) often fails in out-of-sample tests.

To address this, consider a set of managed-portfolios χΦ\chi\_{\Phi} of dimension T×MT\times M:

|  |  |  |  |
| --- | --- | --- | --- |
|  | χΦ=[(χΦ)2′(χΦ)3′⋮(χΦ)T+1′],\chi\_{\Phi}=\begin{bmatrix}(\chi\_{\Phi})\_{2}^{\prime}\\ (\chi\_{\Phi})\_{3}^{\prime}\\ \vdots\\ (\chi\_{\Phi})\_{T+1}^{\prime}\\ \end{bmatrix}, |  | (D.10) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | (χΦ)s=Πs′​Φ.(\chi\_{\Phi})\_{s}=\Pi\_{s}^{\prime}\Phi. |  | (D.11) |

The optimization in ([D.9](https://arxiv.org/html/2602.20856v1#A4.E9 "In Maximizing the squared Sharpe ratio with respect to Λ. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) is an asset allocation problem in which the goal is to determine the investment weights Λ\Lambda for the managed-portfolios χΦ\chi\_{\Phi} to maximize the squared Sharpe ratio. This is equivalent to estimating Λ\Lambda as the mean-variance efficient portfolio weights.

Following britten1999sampling, we estimate Λ\Lambda using the regression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏=χΦ​Λ+𝐮,\mathbf{1}=\chi\_{\Phi}\Lambda+\mathbf{u}, |  | (D.12) |

where 𝟏\mathbf{1} is a TT-vector of ones.

To improve out-of-sample performance, we adopt ridge regression, as in kelly2023FML; shen2024can:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ^=(χΦ′​χΦ+λ​IM)−1​χΦ′​𝟏,\hat{\Lambda}=(\chi\_{\Phi}^{\prime}\chi\_{\Phi}+\lambda I\_{M})^{-1}\chi\_{\Phi}^{\prime}\mathbf{1}, |  | (D.13) |

where λ\lambda is a shrinkage parameter. The solution in ([D.13](https://arxiv.org/html/2602.20856v1#A4.E13 "In Estimating high-dimensional Λ using ridge regression. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) coincides with ([D.9](https://arxiv.org/html/2602.20856v1#A4.E9 "In Maximizing the squared Sharpe ratio with respect to Λ. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) when λ=0\lambda=0. While ([D.13](https://arxiv.org/html/2602.20856v1#A4.E13 "In Estimating high-dimensional Λ using ridge regression. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) may underperform in-sample, it improves robustness for out-of-sample applications.

##### Define the squared Sharpe ratio as a function of Φ\Phi.

Alternatively, we express the squared Sharpe ratio as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​R2=Φ′​AΛ​ΦΦ′​BΛ​Φ,SR^{2}=\frac{\Phi^{\prime}A\_{\Lambda}\Phi}{\Phi^{\prime}B\_{\Lambda}\Phi}, |  | (D.14) |

where AΛ=Π​Λ​Λ′​Π′A\_{\Lambda}=\Pi\Lambda\Lambda^{\prime}\Pi^{\prime}, BΛ=(Λ′⊗IN2)​ΣΛ​(Λ⊗IN2)B\_{\Lambda}=(\Lambda^{\prime}\otimes I\_{N^{2}})\Sigma\_{\Lambda}(\Lambda\otimes I\_{N^{2}}), and ΣΛ\Sigma\_{\Lambda} is the covariance matrix of vec​(Πs)\text{vec}(\Pi\_{s}).

##### Maximizing the squared Sharpe ratio with respect to Φ\Phi.

Referring to Eq. ([A.11](https://arxiv.org/html/2602.20856v1#A1.E11 "In Sharpe Ratio ‣ Appendix A Proof of Proposition 1 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")), we formulate the optimization problem as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ=arg​maxΦ⁡Φ′​AΛ​ΦΦ′​BΛ​Φ=𝚽​(Λ).\Phi=\operatorname\*{arg\,max}\_{\Phi}\frac{\Phi^{\prime}A\_{\Lambda}\Phi}{\Phi^{\prime}B\_{\Lambda}\Phi}=\mathbf{\Phi}(\Lambda). |  | (D.15) |

Solving ([D.15](https://arxiv.org/html/2602.20856v1#A4.E15 "In Maximizing the squared Sharpe ratio with respect to Φ. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) follows the same procedure as ([D.9](https://arxiv.org/html/2602.20856v1#A4.E9 "In Maximizing the squared Sharpe ratio with respect to Λ. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")).

##### Estimating high-dimensional Φ\Phi using ridge regression.

Analogous to ([D.13](https://arxiv.org/html/2602.20856v1#A4.E13 "In Estimating high-dimensional Λ using ridge regression. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")), we define managed-portfolios χΛ\chi\_{\Lambda} of dimension T×N2T\times N^{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | χΛ=[(χΛ)2′(χΛ)3′⋮(χΛ)T+1′],\chi\_{\Lambda}=\begin{bmatrix}(\chi\_{\Lambda})\_{2}^{\prime}\\ (\chi\_{\Lambda})\_{3}^{\prime}\\ \vdots\\ (\chi\_{\Lambda})\_{T+1}^{\prime}\\ \end{bmatrix}, |  | (D.16) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | (χΛ)s=Πs​Λ.(\chi\_{\Lambda})\_{s}=\Pi\_{s}\Lambda. |  | (D.17) |

Applying ridge regression, we estimate Φ\Phi as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ^=(χΛ′​χΛ+λ​IN2)−1​χΛ′​𝟏.\hat{\Phi}=(\chi\_{\Lambda}^{\prime}\chi\_{\Lambda}+\lambda I\_{N^{2}})^{-1}\chi\_{\Lambda}^{\prime}\mathbf{1}. |  | (D.18) |

##### Algorithm and Iteration.

To solve the whole problem, we do iterations until convergence. In each iteration, we have four steps:

1. 1.

   Given Π,ΣΛ,Λ\Pi,\Sigma\_{\Lambda},\Lambda, update the values of AΛ,BΛ,CΛA\_{\Lambda},B\_{\Lambda},C\_{\Lambda},
2. 2.

   Solve Eq.([D.18](https://arxiv.org/html/2602.20856v1#A4.E18 "In Estimating high-dimensional Φ using ridge regression. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) to get the updated Φ\Phi,
3. 3.

   Given Π,ΣΦ,Φ\Pi,\Sigma\_{\Phi},\Phi, update the values of AΦ,BΦ,CΦA\_{\Phi},B\_{\Phi},C\_{\Phi},
4. 4.

   Solve Eq.([D.13](https://arxiv.org/html/2602.20856v1#A4.E13 "In Estimating high-dimensional Λ using ridge regression. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) to get the updated Λ\Lambda.

A full description of the algorithm is in Algorithm [1](https://arxiv.org/html/2602.20856v1#alg1 "Algorithm 1 ‣ Algorithm and Iteration. ‣ Appendix D Proof and Derivations for Propositions 4 and 5 ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.").

Algorithm 1  Maximize Sharpe Ratio

1:procedure MaxSR( Λ,Φ\Lambda,\Phi )

2:Input Asset returns rsr\_{s} and signals StS\_{t}.

3:outcome Investment decision variables Λ,Φ\Lambda,\Phi.

4:  Calculate Π,ΣΦ,ΣΛ\Pi,\Sigma\_{\Phi},\Sigma\_{\Lambda}. ⊳\triangleright These variables are Constant.

5:  Initialize index of iteration k=0k=0. ⊳\triangleright We use kk in notation Λ{k},Φ{k}\Lambda^{\{k\}},\Phi^{\{k\}}.

6:  Initialize Λ{0}\Lambda^{\{0\}}. ⊳\triangleright E.g., the solution in Max Expected Return strategy.

7:  while Termination Conditions not Activated do

8:    Update AΛ,BΛ,CΛA\_{\Lambda},B\_{\Lambda},C\_{\Lambda} with Λ{k}\Lambda^{\{k\}}.

9:    Update Φ{k+1}\Phi^{\{k+1\}} by solving Eq.([25](https://arxiv.org/html/2602.20856v1#S3.E25 "In Proposition 5. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")). 

|  |  |  |
| --- | --- | --- |
|  | Φ{k+1}=𝚽​(Λ{k}).\Phi^{\{k+1\}}=\mathbf{\Phi}(\Lambda^{\{k\}}). |  |

10:    Update AΦ,BΦ,CΦA\_{\Phi},B\_{\Phi},C\_{\Phi} with Φ{k+1}\Phi^{\{k+1\}},

11:    Update Λ{k+1}\Lambda^{\{k+1\}} by solving Eq.([22](https://arxiv.org/html/2602.20856v1#S3.E22 "In Proposition 5. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")).

|  |  |  |
| --- | --- | --- |
|  | Λ{k+1}=𝚲​(Φ{k+1}).\Lambda^{\{k+1\}}=\mathbf{\Lambda}(\Phi^{\{k+1\}}). |  |

12:    k=k+1k=k+1.

13:  end while

14:  return Λ{k},Φ{k}\Lambda^{\{k\}},\Phi^{\{k\}}

15:end procedure

## Appendix E Cross-Validation for λ\lambda the Ridge Shrinkage Parameter

We employ the five-fold cross-validation to select the λ\lambda parameter in ridge regressions ([22](https://arxiv.org/html/2602.20856v1#S3.E22 "In Proposition 5. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) and ([25](https://arxiv.org/html/2602.20856v1#S3.E25 "In Proposition 5. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")), and then apply to out-of-sample investment.
The parameter grid is 10x10^{x}, where x∈[4,3,2,⋯,−5,−6]x\in[4,3,2,\cdots,-5,-6].
Figure [E.1](https://arxiv.org/html/2602.20856v1#A5.F1 "Figure E.1 ‣ Appendix E Cross-Validation for 𝜆 the Ridge Shrinkage Parameter ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") shows the parameters selected by cross-validation in each rolling window estimation.
We find the selected parameters are time-varying, wandering in the parameter grid.

Figure E.1: Selected Parameter by Cross-Validation

This table reports the selection results of λ\lambda in ([22](https://arxiv.org/html/2602.20856v1#S3.E22 "In Proposition 5. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) and ([25](https://arxiv.org/html/2602.20856v1#S3.E25 "In Proposition 5. ‣ 3.2 Maximizing Sharpe Ratio ‣ 3 Estimating the Unknown Parameters ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.")) via the five-fold cross-validation. The parameter grid is [104,103,102,101,100,10−1,10−2,10−3,10−4,10−5,10−6][10^{4},10^{3},10^{2},10^{1},10^{0},10^{-1},10^{-2},10^{-3},10^{-4},10^{-5},10^{-6}]. Each point in the figure represents the selected λ\lambda for a rolling window estimation.

![Refer to caption](x7.png)


(A) Spread Portfolio

![Refer to caption](x8.png)


(B) BiSort Portfolio

## Appendix F Signal-Level Importance

Figure F.1: Signal Importance

This figure complements the theme-level signal importance in Figure [2](https://arxiv.org/html/2602.20856v1#S5.F2 "Figure 2 ‣ 5.2.4 Evolution of Sharpe Ratios over the Sample Period ‣ 5.2 Zero-Cost Linear Strategies ‣ 5 Results ‣ Stochastic Discount Factors with Cross-Asset Spillovers We are grateful to Utpal Bhattacharya, Lin Will Cong, Yi Ding, Gavin Feng, Shuyi Ge, Michael Gofman, Jingyu He, Kewei Hou, Wenjin Kang, Shikun Barry Ke, Junye Li, Sicong Li, Xin Liu, Semyon Malamud, Stefan Nagel, Zilong Niu, Alex Philipov, Gil Segal, Giorgia Simion, Robert Stambaugh, Yinan Su, Dragon Yongjun Tang, Jun Tu, Siwei Wang, Yanchu Wang, Dacheng Xiu, Jingzhou Yan, Jingyi Yao, Jun Yu, Chao Zhang, Dake Zhang, Guofu Zhou, Qi Zhou, and seminar and conference participants at Hebrew University of Jerusalem, Shanghai Jiao Tong University, Sichuan University, Southwestern University of Finance and Economics, University of Science and Technology of China, Xiamen University, Fudan International Symposium on AI in Finance 2025, Hong Kong Conference for Fintech, AI, and Big Data in Business 2025, Paris December Finance Meeting 2025, SYSU Conference on Big Data, AI, and FinTech 2025, UMacau FinTech and Financial Markets Workshop 2025, and USTC Frontiers in Finance Conference 2025, for constructive discussions and feedback. The authors acknowledge financial support from Inquire Europe. Avramov (E-mail: doron.avramov@runi.ac.il) is at Reichman University (IDC), Herzliya, Israel. He (E-mail: xin.he@ustc.edu.cn) is at University of Science and Technology of China. All authors contributed equally to this work.") by providing the 138 signal-level importance in full detail.
These signals of the same theme are grouped in the vertical axis, where the 13 themes follow jensen2023there.
For interpretation, we focus on the absolute value of elements in Λ\Lambda.
Sub-figures (a) and (b) report for spread portfolios and bivariate sorted portfolios, respectively.

![Refer to caption](x9.png)


(a) Spread Portfolio

![Refer to caption](x10.png)


(b) BiSort Portfolio