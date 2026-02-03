---
authors:
- Du-Yi Wang
- Guo Liang
- Kun Zhang
- Qianwen Zhu
doc_id: arxiv:2602.01912v1
family_id: arxiv:2602.01912
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest
  with Conformal Calibration
url_abs: http://arxiv.org/abs/2602.01912v1
url_html: https://arxiv.org/html/2602.01912v1
venue: arXiv q-fin
version: 1
year: 2026
---


Du-Yi Wang

Guo Liang

Kun Zhang

Qianwen Zhu

###### Abstract

Rapidly evolving market conditions call for real-time risk monitoring, but its online estimation remains challenging.
In this paper, we study the online estimation of one of the most widely used risk measures, Value at Risk (VaR). Its accurate and reliable estimation is essential for timely risk control and informed decision-making.
We propose to use the quantile regression forest in the offline-simulation-online-estimation (OSOA) framework. Specifically, the quantile regression forest is trained offline to learn the relationship between the online VaR and risk factors, and real-time VaR estimates are then produced online by incorporating observed risk factors. To further ensure reliability, we develop a conformalized estimator that calibrates the online VaR estimates.
To the best of our knowledge, we are the first to leverage conformal calibration to estimate real-time VaR reliably based on the OSOA formulation.
Theoretical analysis establishes the consistency and coverage validity of the proposed estimators.
Numerical experiments confirm the proposed method and demonstrate its effectiveness in practice.

###### keywords:

Value at Risk, quantile regression forest , stochastic simulation , real-time estimation , conformal calibration

\affiliation

[1]organization=Institute of Statistics and Big Data, Renmin University of China,
state=Beijing,
country=China

\affiliation

[2]organization=Department of Decision Analytics and Operations, City University of Hong Kong,
city=Kowloon,
state=Hong Kong,
country=China

\affiliation

[3]organization=School of Information, Renmin University of China,
state=Beijing,
country=China

## 1 Introduction

Risk management is central to the daily operations of financial institutions, where accurate real-time risk measurement supports trading limits, margin requirements, capital allocation, and regulatory compliance (see, e.g., Jiang et al., [2020](https://arxiv.org/html/2602.01912v1#bib.bib77 "Online risk monitoring using offline simulation"); Huang et al., [2022](https://arxiv.org/html/2602.01912v1#bib.bib7 "Nonparametric mean-lower partial moment model and enhanced index investment"); Valle, [2025](https://arxiv.org/html/2602.01912v1#bib.bib9 "Portfolio optimisation: bridging the gap between theory and practice")).
A famous example is J.P. Morgan’s “4:15 report,” which requires firm-wide risk aggregation within 15 minutes after market close to manage overnight exposures and inform next-day trading decisions (Jorion, [2006](https://arxiv.org/html/2602.01912v1#bib.bib26 "Value at risk: the new benchmark for managing financial risk"); Jiang et al., [2020](https://arxiv.org/html/2602.01912v1#bib.bib77 "Online risk monitoring using offline simulation")).
Notably, Jiang et al. ([2020](https://arxiv.org/html/2602.01912v1#bib.bib77 "Online risk monitoring using offline simulation")) refer to this setting as the online risk monitoring problem.

In this online monitoring context, the risk measure, a function of portfolio losses, is computed after observing the current risk factors, such as stock prices, interest rates, and exchange rates.
Thus the computation can be viewed as estimating a conditional risk measure, i.e., a risk measure conditional on observed risk factors.
Jiang et al. ([2020](https://arxiv.org/html/2602.01912v1#bib.bib77 "Online risk monitoring using offline simulation")) adopt the offline-simulation-online-estimation (OSOA) framework (Hong and Jiang, [2019](https://arxiv.org/html/2602.01912v1#bib.bib78 "Offline simulation online application: a new framework of simulation-based decision making")).
Specifically, offline, one simulates pairs of risk factors and portfolio losses to learn their functional relationship; then, online, one estimates risk by inputting real-time risk factors into the learned relationship.
In fact, different conditional risk measures correspond to different functional relations. For example, Jiang et al. ([2020](https://arxiv.org/html/2602.01912v1#bib.bib77 "Online risk monitoring using offline simulation")) study the probability of large losses conditional on real-time risk factors, and propose to use logistic regression to learn the functional relation.
In this paper, we focus on Value at Risk (VaR), one of the most widely used risk measures, and its online estimation with theoretical justification.

VaR is defined as a quantile of the probability distribution of the portfolio loss at a given confidence level. Accordingly, the online VaR estimation is essentially the conditional quantile estimation, and, further, under the OSOA framework, it amounts to learn a conditional quantile function, that is, quantile regression.
Moreover, beyond accuracy and timeliness, the reliability of risk measures is particularly crucial, especially in the context of VaR (see, e.g., Basel Committee on Banking Supervision, [1996](https://arxiv.org/html/2602.01912v1#bib.bib4 "Supervisory framework for the use of “backtesting” in conjunction with the internal models approach to market risk capital requirements"); Campbell, [2006](https://arxiv.org/html/2602.01912v1#bib.bib6 "A review of backtesting and backtesting procedures")).
Reliability differs from accuracy because it distinguishes underestimation from overestimation for risk measures.
For example, over 200 trading days, a 99%99\% daily VaR should produce approximately two exceptions on average, where an exception is recorded when the trading outcome exceeds the estimate.
One or three exceptions may result in the same evaluation errors under symmetric accuracy metrics; however, in practice, one exception (VaR overestimation) is preferable to three (VaR underestimation) and is therefore considered more reliable.
This preference arises from the fact that underestimation can trigger supervisory responses, including increases in the multiplication factor applicable to the internal models capital requirement, and in more severe cases, requirements to revise the model.
By contrast, VaR overestimation leads to less exceptions and is less likely to elicit supervisory action (Basel Committee on Banking Supervision, [1996](https://arxiv.org/html/2602.01912v1#bib.bib4 "Supervisory framework for the use of “backtesting” in conjunction with the internal models approach to market risk capital requirements")).

In this paper, our goal is to estimate VaR in real time with theoretical guarantees.
The problem is challenging due to three aspects: accuracy, timeliness, and reliability.
First, to address accuracy, we adopt quantile regression forests (QRF) (Meinshausen, [2006](https://arxiv.org/html/2602.01912v1#bib.bib69 "Quantile regression forests.")) to learn the conditional quantile function.
Note that large-scale portfolios induce high-dimensional risk factors (Broadie et al., [2015](https://arxiv.org/html/2602.01912v1#bib.bib38 "Risk estimation via regression")).
Moreover, since the mapping from risk factors to portfolio losses is highly nonlinear (Broadie et al., [2015](https://arxiv.org/html/2602.01912v1#bib.bib38 "Risk estimation via regression")), the associated conditional quantile is inherently complex.
Thus, QRF is appropriate because it performs well in high-dimensional structures and can capture complex conditional quantile surfaces (Gnecco et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib63 "Extremal random forests")).
In addition, QRF has the advantages of requiring little tuning and possessing relatively well-understood statistical properties, compared to other machine learning methods (Athey et al., [2019](https://arxiv.org/html/2602.01912v1#bib.bib64 "Generalized random forests"); Grinsztajn et al., [2022](https://arxiv.org/html/2602.01912v1#bib.bib24 "Why do tree-based models still outperform deep learning on typical tabular data?")).
Second, timeliness is achieved by applying the OSOA framework, since prediction via the learned function is sufficient to meet the online time limit.
Third, to ensure reliability, we propose to incorporate conformal calibration into QRF, which is a technique that has been increasingly studied in the machine learning (Angelopoulos and Bates, [2023](https://arxiv.org/html/2602.01912v1#bib.bib73 "Conformal prediction: a gentle introduction")) and large language models (Cherian et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib81 "Language models with conformal factuality guarantees"); Mohri and Hashimoto, [2024](https://arxiv.org/html/2602.01912v1#bib.bib80 "Language models with conformal factuality guarantees")) literature in recent years .
The calibration recovers the target coverage level by correcting the QRF estimator using a held-out calibration set that empirically characterizes the error of the original QRF estimator.

In our algorithm, we train the QRF model offline on simulated pairs of risk factors and portfolio losses, and then estimate VaR online by evaluating the fitted model at the observed risk factor.
Specifically, for QRF, in the training phase, it constructs a weighted empirical conditional distribution using the neighborhood observations in the leaf node across trees, and in the prediction phase, it estimates conditional quantiles from this distribution.
Furthermore, after training the QRF model, we compute residuals relative to the QRF estimate on a calibration set and adjust the original estimate by the corresponding empirical quantile of these residuals, yielding the conformalized estimate.
Our theoretical analysis establishes consistency for the proposed QRF estimator and provides coverage guarantees for the conformalized estimator.

We summarize our contributions as follows.

1. 1.

   We propose a QRF estimator for the online VaR estimation problem.
   Since online VaR corresponds to a conditional quantile, we formulate the problem as a quantile regression task within the OSOA framework and solve it using QRF.
   The OSOA framework ensures timeliness by moving time-consuming computation to the offline stage, so online estimation requires only fast evaluation of the learned regression model.
   Moreover, QRF enhances accuracy, as it is well suited for complex and high-dimensional conditional quantile functions.
2. 2.

   We further develop a conformalized QRF estimator that offers improved reliability.
   Conformal calibration quantifies the exceedance error of QRF and compensates for this error to restore the coverage level.
   We compute calibration residuals relative to the QRF estimate on a held-out set, and correct the estimate by an empirical quantile of these residuals, so the resulting conformalized estimate attains the target level.
   To the best of our knowledge, despite that conformal prediction has been widely studied in machine learning (Angelopoulos and Bates, [2023](https://arxiv.org/html/2602.01912v1#bib.bib73 "Conformal prediction: a gentle introduction")), its potential in risk measurement remains underexplored.
   In this paper, we highlight a paradigm that leverages conformal calibration to recover the target coverage and thereby achieve the reliability of risk measures, using the OSOA-based formulation as a bridge between quantile regression and online VaR estimation.
3. 3.

   We provide a theoretical analysis of the performance of two proposed estimators.
   We establish pointwise and L2L^{2} consistency for the QRF estimator, which indicates that as the offline sample size grows, the estimator asymptotically converges to the true conditional quantile both for each fixed risk factor and on average over risk factors.
   Moreover, we show coverage guarantees for the conformal QRF estimator.
   The estimator yields finite-sample, model-free marginal coverage validity, that is, for any real-time risk factors, the corresponding portfolio loss falls below the estimate with at least the target probability, for any finite calibration sample size and any regression models.
   Further, this guarantee strengthens from marginal to conditional validity as the offline sample size increases.
   These theoretical results ensure the accuracy and reliability of our estimates, thereby making subsequent managerial decisions more informed and convincing.
4. 4.

   We conduct numerical experiments to verify the performance of our method.
   We use comprehensive metrics, including mean root integrated squared error, mean pinball loss, and mean coverage rate, to thoroughly evaluate the estimators on a realistic portfolio risk measurement example.
   Numerical results are provided to demonstrate the effectiveness of our method and to validate the theoretical analysis of the proposed estimators.

### 1.1 Literature Review

Our work is related to three lines of literature.

Offline simulation online estimation.
The OSOA framework is proposed by Hong and Jiang ([2019](https://arxiv.org/html/2602.01912v1#bib.bib78 "Offline simulation online application: a new framework of simulation-based decision making")), and has motivated a growing literature (Jiang et al., [2020](https://arxiv.org/html/2602.01912v1#bib.bib77 "Online risk monitoring using offline simulation"); Cai et al., [2020](https://arxiv.org/html/2602.01912v1#bib.bib61 "Online risk measure estimation via natural gradient boosting"); Jiang et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib76 "Real-time derivative pricing and hedging with consistent metamodels"); Luo et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib79 "Reliable online decision making with covariates"); Keslin et al., [2025](https://arxiv.org/html/2602.01912v1#bib.bib75 "Ranking and contextual selection"); Zhang et al., [2025](https://arxiv.org/html/2602.01912v1#bib.bib20 "Conditional generative modeling for enhanced credit risk management in supply chain finance"); Lin et al., [2025](https://arxiv.org/html/2602.01912v1#bib.bib62 "Contextual strongly convex simulation optimization: optimize then predict with inexact solutions")).
Among this body of work, most online applications are optimization tasks, whereas only a few address portfolio risk measure estimation problems.
Specifically, Jiang et al. ([2020](https://arxiv.org/html/2602.01912v1#bib.bib77 "Online risk monitoring using offline simulation")) use logistic regression to estimate the probability of large losses and to classify the risk category. They theoretically show that both the probability of a large deviation of the estimated probability from its true value and the probability of misclassification converge exponentially fast as the offline sample size goes to infinity.
Moreover, Cai et al. ([2020](https://arxiv.org/html/2602.01912v1#bib.bib61 "Online risk measure estimation via natural gradient boosting")) apply natural gradient boosting to learn the conditional distribution, and then estimate different types of risk measures.
Nonetheless, they do not establish consistency for the estimators since gradient boosting methods are used (Duan et al., [2020](https://arxiv.org/html/2602.01912v1#bib.bib66 "Ngboost: natural gradient boosting for probabilistic prediction"); Velthoen et al., [2023](https://arxiv.org/html/2602.01912v1#bib.bib67 "Gradient boosting for extreme quantile regression")).
In this paper, we focus on online VaR estimation and establish theoretical guarantees.

Quantile regression.
Quantile regression is introduced by Koenker and Bassett Jr ([1978](https://arxiv.org/html/2602.01912v1#bib.bib30 "Regression quantiles")), while early parametric quantile regression may introduce additional bias when the conditional quantile surface is complex (Koenker, [2017](https://arxiv.org/html/2602.01912v1#bib.bib68 "Quantile regression: 40 years on"); Gnecco et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib63 "Extremal random forests")). Nonparametric kernel (Yu and Jones, [1998](https://arxiv.org/html/2602.01912v1#bib.bib31 "Local linear quantile regression")) and spline methods (Koenker et al., [1994](https://arxiv.org/html/2602.01912v1#bib.bib28 "Quantile smoothing splines")) are more flexible but degrade quickly in moderate to high dimensions due to the curse of dimensionality (Gnecco et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib63 "Extremal random forests")).
Furthermore, advances in machine learning have led to a surge in quantile regression methods, including gradient boosting (Friedman, [2001](https://arxiv.org/html/2602.01912v1#bib.bib32 "Greedy function approximation: a gradient boosting machine"); Velthoen et al., [2023](https://arxiv.org/html/2602.01912v1#bib.bib67 "Gradient boosting for extreme quantile regression")), neural network (Taylor, [2000](https://arxiv.org/html/2602.01912v1#bib.bib25 "A quantile regression neural network approach to estimating the conditional density of multiperiod returns")), and random forest (Meinshausen, [2006](https://arxiv.org/html/2602.01912v1#bib.bib69 "Quantile regression forests."); Athey et al., [2019](https://arxiv.org/html/2602.01912v1#bib.bib64 "Generalized random forests"); Gnecco et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib63 "Extremal random forests")).
These methods perform well in situations with high-dimensional covariates and complex conditional quantile surfaces (Gnecco et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib63 "Extremal random forests")).

Conformalized quantile regression.
Conformal prediction is a general methodology for constructing prediction intervals with finite-sample coverage guarantees (see, e.g., Angelopoulos and Bates, [2023](https://arxiv.org/html/2602.01912v1#bib.bib73 "Conformal prediction: a gentle introduction")), and has been applied in large language models for uncertainty quantification (Cherian et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib81 "Language models with conformal factuality guarantees"); Mohri and Hashimoto, [2024](https://arxiv.org/html/2602.01912v1#bib.bib80 "Language models with conformal factuality guarantees")).
Recent work by Romano et al. ([2019](https://arxiv.org/html/2602.01912v1#bib.bib18 "Conformalized quantile regression")) introduces conformalized quantile regression (CQR), which produces the predition intervals that adapt to local variability in highly heteroscedastic settings.
Importantly, the conformal framework is agnostic to the underlying quantile regression methods and can therefore be naturally integrated with QRF.
Further theoretical analyses of CQR, including pointwise coverage properties and comparisons among different procedures, are provided in Sesia and Candès ([2020](https://arxiv.org/html/2602.01912v1#bib.bib19 "A comparison of some conformal quantile regression methods")). In this paper, we incorporate the conformal calibration technique into QRF to ensure the reliability of VaR estimators and establish the coverage guarantees.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2602.01912v1#S2 "2 Problem Formulation ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") formulates the real-time VaR estimation problem.
Section [3](https://arxiv.org/html/2602.01912v1#S3 "3 The QRF Estimator ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") presents the offline learning and online estimation algorithms based on QRF.
Section [4](https://arxiv.org/html/2602.01912v1#S4 "4 The Conformal QRF Estimator ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") develops the conformal QRF estimator.
Section [5](https://arxiv.org/html/2602.01912v1#S5 "5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") provides theoretical guarantees for the proposed estimators.
Section [6](https://arxiv.org/html/2602.01912v1#S6 "6 Numerical Experiments ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") reports numerical results, and Section [7](https://arxiv.org/html/2602.01912v1#S7 "7 Conclusion ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") concludes the paper.

## 2 Problem Formulation

Let 𝐒​(t)=(S1​(t),…,Sd​(t))⊤∈ℝd\mathbf{S}(t)=(S\_{1}(t),\ldots,S\_{d}(t))^{\top}\in\mathbb{R}^{d} for 0≤t≤T0\leq t\leq T, denote the price dynamics of market variables at time tt, such as interest rates, stock prices, exchange rates, and other tradable assets.
Let ℱt\mathcal{F}\_{t} be the filtration generated by the market evolution up to time tt.
We define three critical time points satisfying 0<u<τ<T0<u<\tau<T in the following.

* 1.

  TT: the maturity of derivative instruments in the portfolio (e.g., options).
* 2.

  τ\tau: the risk horizon at which the portfolio risk is to be evaluated.
* 3.

  uu: the real-time monitoring time when risk estimates are required.

Let L​(τ)∈ℝL(\tau)\in\mathbb{R} denote the portfolio loss at the risk horizon τ\tau, and let 𝐗​(t)=(X1​(t),…,Xν​(t))⊤∈ℝν\mathbf{X}(t)=(X\_{1}(t),\ldots,X\_{\nu}(t))^{\top}\in\mathbb{R}^{\nu} for ν≥d\nu\geq d denote the risk factors at time tt, 0≤t≤T0\leq t\leq T, so that 𝐗​(τ)\mathbf{X}(\tau) represents the risk factors at the risk horizon.
The portfolio typically contains derivative securities with nonlinear payoffs. Therefore, L​(τ)L(\tau) is an expectation of (discounted) loss of a portfolio at maturity conditional on risk factors 𝐗​(τ)\mathbf{X}(\tau). By the Markovian property of 𝐒​(t)\mathbf{S}(t), 𝐗​(τ)\mathbf{X}(\tau) can be constructed by 𝐒​(t)t∈[0,τ]\mathbf{S}(t)\_{t\in[0,\tau]}.
For example, in addition to 𝐒​(τ)\mathbf{S}(\tau), 𝐗​(τ)\mathbf{X}(\tau) may also include path-dependent state variables, such as the running maximum of the underlying price for barrier options or the running average for Asian options, as in (see, e.g., Lai et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib50 "Simulating confidence intervals for conditional value-at-risk via least-squares metamodels")).

At monitoring time uu, we observe a realization of risk factors, denoted by 𝐱​(u)=(x1​(u),…,xν​(u))⊤∈ℝν\mathbf{x}(u)=(x\_{1}(u),\ldots,x\_{\nu}(u))^{\top}\in\mathbb{R}^{\nu}, based on the available information ℱu\mathcal{F}\_{u}. Then the online risk measure problem is to estimate the conditional risk measure of L​(τ)L(\tau) given 𝐗​(u)=𝐱​(u)\mathbf{X}(u)=\mathbf{x}(u):

|  |  |  |
| --- | --- | --- |
|  | fu​(𝐱​(u))=ρ​(L​(τ)∣𝐗​(u)=𝐱​(u)),\displaystyle f\_{u}(\mathbf{x}(u))=\rho\left(L(\tau)\mid\mathbf{X}(u)=\mathbf{x}(u)\right), |  |

where ρ​(⋅)\rho(\cdot) denotes a generic risk measure functional. In this paper, we are interested in online VaR estimation, where the target function is the conditional α\alpha-quantile of L​(τ)L(\tau) given 𝐗​(u)=𝐱​(u)\mathbf{X}(u)=\mathbf{x}(u) with confidence level α∈(0,1)\alpha\in(0,1):

|  |  |  |  |
| --- | --- | --- | --- |
|  | vα​(𝐱​(u))=fu​(𝐱​(u))\displaystyle v\_{\alpha}(\mathbf{x}(u))=f\_{u}(\mathbf{x}(u)) | =Qα​(L​(τ)∣𝐗​(u)=𝐱​(u))\displaystyle=Q\_{\alpha}(L(\tau)\mid\mathbf{X}(u)=\mathbf{x}(u)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =inf{y∈ℝ:ℙ​(L​(τ)≤y∣𝐗​(u)=𝐱​(u))≥α},\displaystyle=\inf\left\{y\in\mathbb{R}:\mathbb{P}\left(L(\tau)\leq y\mid\mathbf{X}(u)=\mathbf{x}(u)\right)\geq\alpha\right\}, |  |

where Qα(⋅∣⋅)Q\_{\alpha}(\cdot\mid\cdot) denotes the conditional α\alpha-quantile operator.

Here we provide intuition for this target function to explain why the problem is nontrivial.
The portfolio loss function L​(τ)L(\tau) is nonlinear and has no closed forms (Broadie et al., [2015](https://arxiv.org/html/2602.01912v1#bib.bib38 "Risk estimation via regression"); Hong et al., [2017](https://arxiv.org/html/2602.01912v1#bib.bib49 "Kernel smoothing for nested estimation with application to portfolio risk measurement"); Jiang et al., [2020](https://arxiv.org/html/2602.01912v1#bib.bib77 "Online risk monitoring using offline simulation"); Wang et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib51 "Smooth nested simulation: bridging cubic and square root convergence rates in high dimensions")).
Moreover, our target function is a conditional quantile of L​(τ)L(\tau), which is inherently more difficult to estimate, since conditioning reduces effective sample size locally and tail quantiles further amplify data scarcity.

## 3 The QRF Estimator

To address real-time estimation challenges, we adopt the OSOA paradigm. The paradigm consists of two stages: an offline stage for heavy computation and an online stage for fast evaluation (Hong and Jiang, [2019](https://arxiv.org/html/2602.01912v1#bib.bib78 "Offline simulation online application: a new framework of simulation-based decision making")). In the following, we provide a detailed description of each stage.

1. 1.

   The Offline Stage: Simulation and Learning.
     
   We simulate nn independent sample paths 𝐒i​(t)t∈[0,τ]\mathbf{S}\_{i}(t)\_{t\in[0,\tau]}, i=1,…,ni=1,\ldots,n, from the underlying stochastic model, and meanwhile obtain the corresponding portfolio losses Li​(τ)L\_{i}(\tau) by nested simulation.
   Specifically, given each generated path 𝐒i​(t)t∈[0,τ]\mathbf{S}\_{i}(t)\_{t\in[0,\tau]}, we sample mm independent inner paths 𝐒i,j​(t)t∈[τ,T]\mathbf{S}\_{i,j}(t)\_{t\in[\tau,T]}, j=1,…,mj=1,\ldots,m, calculate the terminal payoff at time TT and the corresponding loss li,j​(τ)l\_{i,j}(\tau), and then compute the portfolio loss Li​(τ)L\_{i}(\tau) using the average ∑j=1mli,j​(τ)/m\sum\_{j=1}^{m}l\_{i,j}(\tau)/m.
   This procedure yields a dataset {(𝐗i​(u),Li​(τ))}i=1n\{(\mathbf{X}\_{i}(u),L\_{i}(\tau))\}\_{i=1}^{n}.
     
   Based on this data set, we train a conditional quantile regression model to learn the mapping from 𝐗​(u)\mathbf{X}(u) to the conditional α\alpha-quantile of L​(τ)L(\tau), denoted by f^u​(⋅)\hat{f}\_{u}(\cdot).
2. 2.

   The Online Stage: Estimation.
     
   After observing the real-world risk factor 𝐱​(u)\mathbf{x}(u), we input it into the learned model, and return f^u​(𝐱​(u))\hat{f}\_{u}(\mathbf{x}(u)) as the real-time VaR estimate.

We make several remarks on this algorithm.
First, details of the nested simulation procedure for computing Li​(τ)L\_{i}(\tau) can be found in Gordy and Juneja ([2010](https://arxiv.org/html/2602.01912v1#bib.bib46 "Nested simulation in portfolio risk measurement")) and Zhang et al. ([2022](https://arxiv.org/html/2602.01912v1#bib.bib48 "Bootstrap-based budget allocation for nested simulation")), while the construction of 𝐗i​(u)\mathbf{X}\_{i}(u) could follow Lai et al. ([2024](https://arxiv.org/html/2602.01912v1#bib.bib50 "Simulating confidence intervals for conditional value-at-risk via least-squares metamodels")).
Second, we do not account for the error from using a finite number of inner samples. This is reasonable because computational time is abundant during the offline stage, allowing us to allocate a sufficient budget to the inner simulations, which makes the inner error nearly negligible (Jiang et al., [2020](https://arxiv.org/html/2602.01912v1#bib.bib77 "Online risk monitoring using offline simulation"); Cai et al., [2020](https://arxiv.org/html/2602.01912v1#bib.bib61 "Online risk measure estimation via natural gradient boosting")).
Third, to learn the model fu​(⋅){f}\_{u}(\cdot), we adopt QRF (Meinshausen, [2006](https://arxiv.org/html/2602.01912v1#bib.bib69 "Quantile regression forests.")) as a quantile regression alternative within the OSOA framework.
In the following, we present the detailed procedure of QRF.

In the offline stage, to obtain f^u​(⋅)\hat{f}\_{u}(\cdot), we construct an ensemble of BB regression trees T​(θb)b=1B{T(\theta\_{b})}\_{b=1}^{B}, where θb\theta\_{b} collects all randomness in the construction of tree bb, using bootstrap resampling and randomized splitting rules.
In the online stage, the new data point 𝐱​(u)\mathbf{x}(u) is propagated down each tree T​(θb)T(\theta\_{b}) to a leaf node l​(𝐱​(u),θb)l(\mathbf{x}(u),\theta\_{b}) with the associated region Rl​(𝐱​(u),θb)R\_{l(\mathbf{x}(u),\theta\_{b})}. For each training sample 𝐗i​(u)\mathbf{X}\_{i}(u), i=1,…,ni=1,\ldots,n, its tree weight is defined as

|  |  |  |
| --- | --- | --- |
|  | wi​(𝐱​(u),θb)=𝟏​{𝐗i​(u)∈Rl​(𝐱​(u),θb)}#​{j:𝐗j​(u)∈Rl​(𝐱​(u),θb)},\displaystyle w\_{i}(\mathbf{x}(u),\theta\_{b})=\frac{\mathbf{1}\{\mathbf{X}\_{i}(u)\in R\_{l(\mathbf{x}(u),\theta\_{b})}\}}{\#\{j:\mathbf{X}\_{j}(u)\in R\_{l(\mathbf{x}(u),\theta\_{b})}\}}, |  |

where #​{⋅}\#\{\cdot\} denotes the cardinality of a set and 𝟏​{⋅}\mathbf{1}\{\cdot\} denotes the indicator function. Averaging across all trees then yields the forest weight

|  |  |  |
| --- | --- | --- |
|  | wi​(𝐱​(u))=1B​∑t=1Bwi​(𝐱​(u),θb).\displaystyle w\_{i}(\mathbf{x}(u))=\frac{1}{B}\sum\_{t=1}^{B}w\_{i}(\mathbf{x}(u),\theta\_{b}). |  |

Therefore, the conditional α\alpha-quantile, i.e., the VaR at confidence level α\alpha , is estimated as

|  |  |  |
| --- | --- | --- |
|  | v^α​(𝐱​(u))=f^u​(𝐱​(u))=inf{y∈ℝ:∑i=1nwi​(𝐱​(u))​𝟏​{Li​(τ)≤y}≥α}.\displaystyle\hat{v}\_{\alpha}(\mathbf{x}(u))=\hat{f}\_{u}(\mathbf{x}(u))=\inf\left\{y\in\mathbb{R}:\sum\_{i=1}^{n}w\_{i}(\mathbf{x}(u))\mathbf{1}\{L\_{i}(\tau)\leq y\}\geq\alpha\right\}. |  |

We refer to this estimator as the QRF estimator.

## 4 The Conformal QRF Estimator

The QRF estimator is designed to achieve accurate prediction, but does not distinguish between underestimation and overestimation.
However, in practice, overestimation is often preferred to underestimation.
For example, when estimated VaR is used to determine margin requirements, holding a larger margin buffer is generally preferable; otherwise, the institution may face substantial downside risk due to an insufficient capital cushion.
In a word, slight overestimation is often acceptable, whereas underestimation is undesirable.

Motivated by this consideration, we further develop an estimator to meet the coverage criteria.
The main idea comes from CQR (Romano et al., [2019](https://arxiv.org/html/2602.01912v1#bib.bib18 "Conformalized quantile regression")), which provides a calibration step that adjusts a base quantile estimator to achieve a specified coverage level.
Our algorithm implements this idea as follows.
In the offline stage, given the dataset {(𝐗i​(u),Li​(τ))}i=1n\{(\mathbf{X}\_{i}(u),L\_{i}(\tau))\}\_{i=1}^{n}, we split the index set into a training set and a calibration set disjointly, denoted by ℐ1\mathcal{I}\_{1} and ℐ2\mathcal{I}\_{2}, respectively.
The quantile regression model (e.g., QRF) is trained using only the data indexed by ℐ1\mathcal{I}\_{1} to obtain v^α​(⋅)\hat{v}\_{\alpha}(\cdot) or say f^u​(⋅)\hat{f}\_{u}(\cdot).
We then calculate the conformity scores on the calibration set ℐ2\mathcal{I}\_{2},

|  |  |  |
| --- | --- | --- |
|  | Ei=Li​(τ)−v^α​(𝐗i​(u)),i∈ℐ2,\displaystyle E\_{i}=L\_{i}(\tau)-\hat{v}\_{\alpha}(\mathbf{X}\_{i}(u)),\quad i\in\mathcal{I}\_{2}, |  |

and define qα​(E,ℐ2)q\_{\alpha}(E,\mathcal{I}\_{2}) as the empirical α\alpha-quantile of the conformity scores {Ei}i∈ℐ2\{E\_{i}\}\_{i\in\mathcal{I}\_{2}}.
In the online stage, given a new observation 𝐱​(u)\mathbf{x}(u), the conformal QRF estimator is given by

|  |  |  |
| --- | --- | --- |
|  | v^αc​(𝐱​(u))=v^α​(𝐱​(u))+qα​(E,ℐ2).\displaystyle\hat{v}^{\mathrm{c}}\_{\alpha}(\mathbf{x}(u))=\hat{v}\_{\alpha}(\mathbf{x}(u))+q\_{\alpha}(E,\mathcal{I}\_{2}). |  |

We offer several remarks on this estimator.
This procedure can be considered as a flexible calibration step applied after the conditional quantile regression, which conformalizes the initial regression estimate using the calibration set to improve coverage validity.
Moreover, due to its model-free nature, the calibration idea can be combined with a broad class of quantile regression methods beyond QRF.

## 5 Theoretical Guarantees

For notational convenience, we denote 𝐗=𝐗​(u)\mathbf{X}=\mathbf{X}(u), 𝐱=𝐱​(u)\mathbf{x}=\mathbf{x}(u), and Y=L​(τ)Y=L(\tau), ignoring the time index, which is not involved in our analysis.
We write F​(y∣𝐱)=ℙ​(Y≤y∣𝐗=𝐱)F(y\mid\mathbf{x})=\mathbb{P}(Y\leq y\mid\mathbf{X}=\mathbf{x}).
Moreover, g​(n)=o​(f​(n))g(n)=o(f(n)) stands for g​(n)/f​(n)→0g(n)/f(n)\to 0, as n→∞n\to\infty.
Furthermore, for two sequences of random variables {Un}\left\{U\_{n}\right\} and {Vn}\left\{V\_{n}\right\}, Un=op​(Vn)U\_{n}=o\_{p}\left(V\_{n}\right) denotes that Un/Vn→𝑝0U\_{n}/V\_{n}\xrightarrow{p}0, as n→∞n\to\infty.
To facilitate analysis for the estimators, we make the following assumptions.

###### Assumption 1.

The support of 𝐗\mathbf{X}, denoted by 𝒳⊂ℝν\mathcal{X}\subset\mathbb{R}^{\nu}, is bounded, and the density of 𝐗\mathbf{X} is positive and bounded from above and below by positive constants.

Assumption [1](https://arxiv.org/html/2602.01912v1#Thmassumption1 "Assumption 1. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") is made about the distribution of risk factors, and is used in the literature such as Wang et al. ([2024](https://arxiv.org/html/2602.01912v1#bib.bib51 "Smooth nested simulation: bridging cubic and square root convergence rates in high dimensions")).

###### Assumption 2.

Denote the size of a leaf node ll from a tree constructed with parameter θ\theta by kθ​(l)=#​{i∈{1,…,n}:𝐗i∈Rl​(𝐱,θ)}k\_{\theta}(l)=\#\left\{i\in\{1,\ldots,n\}:\mathbf{X}\_{i}\in R\_{l(\mathbf{x},\theta)}\right\}.
As n→∞n\to\infty, maxl,θ⁡kθ​(l)=o​(n)\max\_{l,\theta}k\_{\theta}(l)=o(n) and 1/minl,θ⁡kθ​(l)=o​(1)1/\min\_{l,\theta}k\_{\theta}(l)=o(1).

Assumption [2](https://arxiv.org/html/2602.01912v1#Thmassumption2 "Assumption 2. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") imposes two conditions on the leaf nodes.
Specifically, the proportion of observations in any leaf node relative to all observations vanishes as nn grows, and the minimum number of observations in each leaf node diverges to infinity.

###### Assumption 3.

Let rr be an arbitrary node in the tree, with nrn\_{r} observations.
If rr is split, then there exists a constant C0>0C\_{0}>0 such that, for any coordinate m∈{1,…,ν}m\in\{1,\ldots,\nu\}, the probability that dimension mm is selected as the split variable is at least C0C\_{0}.
Moreover, there exists a constant γ∈(0,1/2]\gamma\in(0,1/2] such that, whenever node rr is split, each resulting child node rcr\_{c} satisfies nrc/rv≥γn\_{r\_{c}}/r\_{v}\geq\gamma.

Assumption [3](https://arxiv.org/html/2602.01912v1#Thmassumption3 "Assumption 3. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") imposes two standard regularity conditions for leaf nodes in tree-based methods.
The first condition ensures the probability of selecting any feature for splitting is not too small.
The second condition ensures that the resulting child nodes do not have highly imbalanced sample sizes after the split.
Assumptions [2](https://arxiv.org/html/2602.01912v1#Thmassumption2 "Assumption 2. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") and [3](https://arxiv.org/html/2602.01912v1#Thmassumption3 "Assumption 3. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") are standard regularity conditions in the literature related to random forests (Meinshausen, [2006](https://arxiv.org/html/2602.01912v1#bib.bib69 "Quantile regression forests."); Wager and Athey, [2018](https://arxiv.org/html/2602.01912v1#bib.bib23 "Estimation and inference of heterogeneous treatment effects using random forests"); Athey et al., [2019](https://arxiv.org/html/2602.01912v1#bib.bib64 "Generalized random forests"); Cevid et al., [2022](https://arxiv.org/html/2602.01912v1#bib.bib22 "Distributional random forests: heterogeneity adjustment and multivariate distributional regression")).

###### Assumption 4.

For any 𝐱,𝐱′∈𝒳\mathbf{x},\mathbf{x}^{\prime}\in\mathcal{X}, there exists a constant C>0C>0 such that

|  |  |  |
| --- | --- | --- |
|  | supy∈ℝ|F(y∣𝐱)−F(y∣𝐱′)|≤C∥𝐱−𝐱′∥1,\displaystyle\sup\_{y\in\mathbb{R}}\left|F(y\mid\mathbf{x})-F\left(y\mid\mathbf{x}^{\prime}\right)\right|\leq C\left\|\mathbf{x}-\mathbf{x}^{\prime}\right\|\_{1}, |  |

where ∥⋅∥1\|\cdot\|\_{1} denotes the ℓ1\ell\_{1} norm.

Assumption [4](https://arxiv.org/html/2602.01912v1#Thmassumption4 "Assumption 4. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") states that the conditional distribution function is Lipschitz continuous with respect to 𝐱\mathbf{x} with parameter CC.

###### Assumption 5.

For any 𝐱∈𝒳\mathbf{x}\in\mathcal{X}, F​(y∣𝐱)F(y\mid\mathbf{x}) is strictly monotonically increasing in yy.

Assumptions [4](https://arxiv.org/html/2602.01912v1#Thmassumption4 "Assumption 4. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") and [5](https://arxiv.org/html/2602.01912v1#Thmassumption5 "Assumption 5. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") are used in Meinshausen ([2006](https://arxiv.org/html/2602.01912v1#bib.bib69 "Quantile regression forests.")).

###### Theorem 1.

Under Assumptions 1–5, for any 𝐱∈𝒳\mathbf{x}\in\mathcal{X}, the proposed online estimator for VaR with confidence level α\alpha satisfies

|  |  |  |
| --- | --- | --- |
|  | v^α​(𝐱)→𝑝vα​(𝐱),n→∞,\displaystyle\hat{v}\_{\alpha}(\mathbf{x})\xrightarrow{p}v\_{\alpha}(\mathbf{x}),\quad n\rightarrow\infty, |  |

where nn is the offline sample size.

###### Proof.

In the following, we prove the result by applying the continuous mapping theorem for functionals (Wainwright, [2019](https://arxiv.org/html/2602.01912v1#bib.bib13 "High-dimensional statistics: a non-asymptotic viewpoint")). To this end, we need to verify two conditions.
With Assumptions 1-5, by Theorem 1 in Meinshausen ([2006](https://arxiv.org/html/2602.01912v1#bib.bib69 "Quantile regression forests.")), we have

|  |  |  |
| --- | --- | --- |
|  | ∥F^n(⋅∣𝐱)−F(⋅∣𝐱)∥∞=supy∈ℝ|F^n(y∣𝐱)−F(y∣𝐱)|→𝑝0,n→∞,\displaystyle\|\hat{F}\_{n}(\cdot\mid\mathbf{x})-F(\cdot\mid\mathbf{x})\|\_{\infty}=\sup\_{y\in\mathbb{R}}|\hat{F}\_{n}(y\mid\mathbf{x})-F(y\mid\mathbf{x})|\xrightarrow{p}0,\quad n\to\infty, |  |

where F^n​(y∣𝐱)=∑i=1nwi​(𝐱)​𝟏​{Yi≤y}\hat{F}\_{n}(y\mid\mathbf{x})=\sum\_{i=1}^{n}w\_{i}(\mathbf{x})\mathbf{1}\left\{Y\_{i}\leq y\right\}. Thus, the first condition is checked.
Note that the conditional quantile estimator and true conditional quantile can be rewritten as a quantile functional QαQ^{\alpha} of F^n​(y∣𝐱)\hat{F}\_{n}(y\mid\mathbf{x}) and F​(y∣𝐱){F}(y\mid\mathbf{x}), respectively, where Qα​(G)=inf{z∈ℝ:G​(z)≥α}Q^{\alpha}(G)=\inf\{z\in\mathbb{R}:G(z)\geq\alpha\}.
For convenience, we write q=vα​(𝐱)q=v\_{\alpha}(\mathbf{x}) and thus F​(q∣𝐱)=αF(q\mid\mathbf{x})=\alpha.
From Assumption 5, we have that, for any ϵ>0\epsilon>0, F​(q−ϵ∣𝐱)<F​(q∣𝐱)<F​(q+ϵ∣𝐱)F(q-\epsilon\mid\mathbf{x})<F(q\mid\mathbf{x})<F(q+\epsilon\mid\mathbf{x}).
Let

|  |  |  |
| --- | --- | --- |
|  | δ=min⁡{α−F​(q−ϵ∣𝐱),F​(q+ϵ∣𝐱)−α}>0.\delta=\min\{\alpha-F(q-\epsilon\mid\mathbf{x}),F(q+\epsilon\mid\mathbf{x})-\alpha\}>0. |  |

If ∥F^n(⋅∣𝐱)−F(⋅∣𝐱)∥∞≤δ\|\hat{F}\_{n}(\cdot\mid\mathbf{x})-F(\cdot\mid\mathbf{x})\|\_{\infty}\leq\delta, then supy∈ℝ|F^n(y∣𝐱)−F(y∣𝐱)|≤δ\sup\_{y\in\mathbb{R}}|\hat{F}\_{n}(y\mid\mathbf{x})-F(y\mid\mathbf{x})|\leq\delta, and thus for any z∈ℝz\in\mathbb{R}, |F^n(z∣𝐱)−F(z∣𝐱)|≤supy∈ℝ|F^n(y∣𝐱)−F(y∣𝐱)|≤δ|\hat{F}\_{n}(z\mid\mathbf{x})-F(z\mid\mathbf{x})|\leq\sup\_{y\in\mathbb{R}}|\hat{F}\_{n}(y\mid\mathbf{x})-F(y\mid\mathbf{x})|\leq\delta.
In other words, −δ≤F^n​(z|𝐱)−F​(z|𝐱)≤δ-\delta\leq\hat{F}\_{n}(z|\mathbf{x})-F(z|\mathbf{x})\leq\delta, that is, F​(z∣𝐱)−δ≤F^n​(z∣𝐱)≤F​(z∣𝐱)+δF(z\mid\mathbf{x})-\delta\leq\hat{F}\_{n}(z\mid\mathbf{x})\leq F(z\mid\mathbf{x})+\delta.
If z≤q−ϵz\leq q-\epsilon, we have F^n​(z∣𝐱)≤F^n​(q−ϵ∣𝐱)≤F​(q−ϵ∣𝐱)+δ<α\hat{F}\_{n}(z\mid\mathbf{x})\leq\hat{F}\_{n}(q-\epsilon\mid\mathbf{x})\leq F(q-\epsilon\mid\mathbf{x})+\delta<\alpha, where the last inequality comes from the definition of δ\delta.
Similarly, if z≥q+ϵz\geq q+\epsilon, we have F^n​(z∣𝐱)≥F^n​(q+ϵ∣𝐱)≥F​(q+ϵ∣𝐱)−δ>α\hat{F}\_{n}(z\mid\mathbf{x})\geq\hat{F}\_{n}(q+\epsilon\mid\mathbf{x})\geq F(q+\epsilon\mid\mathbf{x})-\delta>\alpha.
Hence, q−ϵ<Qα​(F^n​(y∣𝐱))<q+ϵq-\epsilon<Q^{\alpha}(\hat{F}\_{n}(y\mid\mathbf{x}))<q+\epsilon, that is, |Qα(F^n(y∣𝐱))−q|=|Qα(F^n(y∣𝐱))−Qα(F(y∣𝐱))|<ϵ|Q^{\alpha}(\hat{F}\_{n}(y\mid\mathbf{x}))-q|=|Q^{\alpha}(\hat{F}\_{n}(y\mid\mathbf{x}))-Q^{\alpha}(F(y\mid\mathbf{x}))|<\epsilon.
The second condition is verified that QαQ^{\alpha} is continuous at FF with respect to the supremum norm using the definition.
Therefore, the proof is complete.
∎

Theorem [1](https://arxiv.org/html/2602.01912v1#Thmtheorem1 "Theorem 1. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") establishes the pointwise consistency of the QRF estimator, ensuring that the estimated conditional quantile converges in probability to the true VaR as the offline sample size increases. While consistency ensures that the estimator is asymptotically correct, it allows for the possibility of rare but arbitrarily large estimation errors and provides no control over the moment of the estimation error, which limits its usefulness for online analysis. To strengthen this result, we impose an additional moment condition and establish convergence in the mean squared sense in Theorem [2](https://arxiv.org/html/2602.01912v1#Thmtheorem2 "Theorem 2. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").

###### Assumption 6.

There exist constants δ>0\delta>0 and M<∞M<\infty, such that, for all 𝐱\mathbf{x},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|Y|2+δ∣𝐗=𝐱]≤M.\displaystyle\mathbb{E}\!\left[|Y|^{2+\delta}\mid\mathbf{X}=\mathbf{x}\right]\leq M. |  |

###### Theorem 2.

Suppose that Assumptions 1–6 hold.
Assume further that the tree construction satisfies an *honesty* condition (see, e.g., Athey and Imbens, [2016](https://arxiv.org/html/2602.01912v1#bib.bib12 "Recursive partitioning for heterogeneous causal effects"); Wager and Athey, [2018](https://arxiv.org/html/2602.01912v1#bib.bib23 "Estimation and inference of heterogeneous treatment effects using random forests")).
Specifically, the randomization used to determine the tree structure, i.e., the sequence of splits, is independent of the response samples {Yi}i=1n\{Y\_{i}\}\_{i=1}^{n}, so that the responses are used only to estimate quantities within the leaves of a fixed, data-independent partition.
Then, we have

|  |  |  |
| --- | --- | --- |
|  | limn→∞𝔼​[(v^α​(𝐗)−vα​(𝐗))2]=0,\displaystyle\lim\_{n\to\infty}\mathbb{E}\!\left[\big(\hat{v}\_{\alpha}(\mathbf{X})-v\_{\alpha}(\mathbf{X})\big)^{2}\right]=0, |  |

where nn denotes the offline sample size.

###### Proof.

The proof proceeds in three steps. We first establish convergence in probability at a random covariate 𝐗\mathbf{X}.
We then derive uniform (2+δ)(2+\delta)-moment bounds for both vα​(𝐗)v\_{\alpha}(\mathbf{X}) and v^α​(𝐗)\hat{v}\_{\alpha}(\mathbf{X}).
Finally, we combine these results to conclude L2L^{2} convergence via uniform integrability.

Step 1: Convergence in probability at random 𝐗\mathbf{X}.

Theorem [1](https://arxiv.org/html/2602.01912v1#Thmtheorem1 "Theorem 1. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") shows that for any fixed 𝐱\mathbf{x},

|  |  |  |
| --- | --- | --- |
|  | v^α​(𝐱)→𝑝vα​(𝐱),n→∞.\displaystyle\hat{v}\_{\alpha}(\mathbf{x})\xrightarrow{p}v\_{\alpha}(\mathbf{x}),\qquad n\to\infty. |  |

Let ε>0\varepsilon>0. Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(|v^α​(𝐗)−vα​(𝐗)|>ε)=𝔼​[ℙ​(|v^α​(𝐗)−vα​(𝐗)|>ε∣𝐗)].\displaystyle\mathbb{P}\big(|\hat{v}\_{\alpha}(\mathbf{X})-v\_{\alpha}(\mathbf{X})|>\varepsilon\big)=\mathbb{E}\Big[\mathbb{P}\big(|\hat{v}\_{\alpha}(\mathbf{X})-v\_{\alpha}(\mathbf{X})|>\varepsilon\mid\mathbf{X}\big)\Big]. |  | (1) |

For almost every realization of 𝐗\mathbf{X}, the conditional probability on the right-hand side converges to zero by pointwise consistency.
Since it is bounded between 0 and 11, the dominated convergence theorem yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | v^α​(𝐗)−vα​(𝐗)→𝑝0,n→∞.\displaystyle\hat{v}\_{\alpha}(\mathbf{X})-v\_{\alpha}(\mathbf{X})\xrightarrow{p}0,\qquad n\to\infty. |  | (2) |

Step 2: (2+δ)(2+\delta)-moment bounds.

We first derive a moment bound for vα​(𝐗)v\_{\alpha}(\mathbf{X}).
Let p=2+δp=2+\delta and β=min⁡{α,1−α}\beta=\min\{\alpha,1-\alpha\}.
By the definition of vα​(𝐱)v\_{\alpha}(\mathbf{x}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(|Y|≥|vα​(𝐱)|∣𝐗=𝐱)≥β.\displaystyle\mathbb{P}\big(|Y|\geq|v\_{\alpha}(\mathbf{x})|\mid\mathbf{X}=\mathbf{x}\big)\geq\beta. |  | (3) |

On the other hand, Markov’s inequality implies

|  |  |  |
| --- | --- | --- |
|  | ℙ​(|Y|≥|vα​(𝐱)|∣𝐗=𝐱)≤𝔼​[|Y|p∣𝐗=𝐱]|vα​(𝐱)|p.\displaystyle\mathbb{P}\big(|Y|\geq|v\_{\alpha}(\mathbf{x})|\mid\mathbf{X}=\mathbf{x}\big)\leq\frac{\mathbb{E}\big[|Y|^{p}\mid\mathbf{X}=\mathbf{x}\big]}{|v\_{\alpha}(\mathbf{x})|^{p}}. |  |

Combining this inequality with ([3](https://arxiv.org/html/2602.01912v1#S5.E3 "In Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration")) yields

|  |  |  |
| --- | --- | --- |
|  | |vα​(𝐱)|p≤1β​𝔼​[|Y|p∣𝐗=𝐱]≤Mβ,\displaystyle|v\_{\alpha}(\mathbf{x})|^{p}\leq\frac{1}{\beta}\mathbb{E}\big[|Y|^{p}\mid\mathbf{X}=\mathbf{x}\big]\leq\frac{M}{\beta}, |  |

where the last inequality follows from Assumption [6](https://arxiv.org/html/2602.01912v1#Thmassumption6 "Assumption 6. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
Consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|vα​(𝐗)|2+δ]<∞.\displaystyle\mathbb{E}\big[|v\_{\alpha}(\mathbf{X})|^{2+\delta}\big]<\infty. |  | (4) |

We next derive a deterministic bound for v^α​(𝐱)\hat{v}\_{\alpha}(\mathbf{x}).
For any 𝐱\mathbf{x}, we claim that for every realization of {Yi}i=1n\{Y\_{i}\}\_{i=1}^{n} and {wi​(𝐱)}i=1n\{w\_{i}(\mathbf{x})\}\_{i=1}^{n},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |v^α​(𝐱)|p≤1β​∑i=1nwi​(𝐱)​|Yi|p.\displaystyle|\hat{v}\_{\alpha}(\mathbf{x})|^{p}\leq\frac{1}{\beta}\sum\_{i=1}^{n}w\_{i}(\mathbf{x})\,|Y\_{i}|^{p}. |  | (5) |

To see this, note that the definition of v^α​(𝐱)\hat{v}\_{\alpha}(\mathbf{x}) implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nwi​(𝐱)​𝟏​{|Yi|≥|v^α​(𝐱)|}≥β,\displaystyle\sum\_{i=1}^{n}w\_{i}(\mathbf{x})\mathbf{1}\big\{|Y\_{i}|\geq|\hat{v}\_{\alpha}(\mathbf{x})|\big\}\geq\beta, |  | (6) |

which follows by considering the cases v^α​(𝐱)≤0\hat{v}\_{\alpha}(\mathbf{x})\leq 0 and v^α​(𝐱)≥0\hat{v}\_{\alpha}(\mathbf{x})\geq 0 separately.
Applying the inequality

|  |  |  |
| --- | --- | --- |
|  | 𝟏​{|a|≥t}≤|a|p/tp,t>0,\displaystyle\mathbf{1}\{|a|\geq t\}\leq|a|^{p}/t^{p},\qquad t>0, |  |

with t=|v^α​(𝐱)|t=|\hat{v}\_{\alpha}(\mathbf{x})| and combining with ([6](https://arxiv.org/html/2602.01912v1#S5.E6 "In Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration")) yields ([5](https://arxiv.org/html/2602.01912v1#S5.E5 "In Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration")).

Taking expectations in ([5](https://arxiv.org/html/2602.01912v1#S5.E5 "In Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration")), conditional on 𝐗\mathbf{X}, {𝐗i}i=1n\{\mathbf{X}\_{i}\}\_{i=1}^{n}, and the tree structure θb\theta\_{b}, honesty implies

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∑i=1nwi​(𝐗)​|Yi|p|𝐗,{𝐗i}i=1n,θb]=∑i=1nwi​(𝐗)​𝔼​[|Yi|p∣𝐗i]≤M.\displaystyle\mathbb{E}\!\left[\sum\_{i=1}^{n}w\_{i}(\mathbf{X})|Y\_{i}|^{p}\ \Big|\ \mathbf{X},\{\mathbf{X}\_{i}\}\_{i=1}^{n},\theta\_{b}\right]=\sum\_{i=1}^{n}w\_{i}(\mathbf{X})\mathbb{E}\big[|Y\_{i}|^{p}\mid\mathbf{X}\_{i}\big]\leq M. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supn≥1𝔼​[|v^α​(𝐗)|2+δ]≤Mβ<∞.\displaystyle\sup\_{n\geq 1}\mathbb{E}\big[|\hat{v}\_{\alpha}(\mathbf{X})|^{2+\delta}\big]\leq\frac{M}{\beta}<\infty. |  | (7) |

Step 3: Uniform integrability and L2L^{2} convergence.

Using the inequality |a−b|p≤2p−1​(|a|p+|b|p)|a-b|^{p}\leq 2^{p-1}(|a|^{p}+|b|^{p}) with p=2+δp=2+\delta, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|v^α​(𝐗)−vα​(𝐗)|2+δ]≤21+δ​(𝔼​|v^α​(𝐗)|2+δ+𝔼​|vα​(𝐗)|2+δ).\displaystyle\mathbb{E}\big[|\hat{v}\_{\alpha}(\mathbf{X})-v\_{\alpha}(\mathbf{X})|^{2+\delta}\big]\leq 2^{1+\delta}\Big(\mathbb{E}|\hat{v}\_{\alpha}(\mathbf{X})|^{2+\delta}+\mathbb{E}|v\_{\alpha}(\mathbf{X})|^{2+\delta}\Big). |  |

Combining ([4](https://arxiv.org/html/2602.01912v1#S5.E4 "In Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration")) and ([7](https://arxiv.org/html/2602.01912v1#S5.E7 "In Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | supn≥1𝔼​[|v^α​(𝐗)−vα​(𝐗)|2+δ]<∞.\displaystyle\sup\_{n\geq 1}\mathbb{E}\big[|\hat{v}\_{\alpha}(\mathbf{X})-v\_{\alpha}(\mathbf{X})|^{2+\delta}\big]<\infty. |  | (8) |

By Theorem 4.6.2 of Durrett ([2019](https://arxiv.org/html/2602.01912v1#bib.bib16 "Probability: theory and examples")), this bound implies that the family
{(v^α​(𝐗)−vα​(𝐗))2}n≥1\{(\hat{v}\_{\alpha}(\mathbf{X})-v\_{\alpha}(\mathbf{X}))^{2}\}\_{n\geq 1} is uniformly integrable.

Together with the convergence in probability established in ([2](https://arxiv.org/html/2602.01912v1#S5.E2 "In Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration")),
Theorem 4.6.3 of Durrett ([2019](https://arxiv.org/html/2602.01912v1#bib.bib16 "Probability: theory and examples")) yields L1L^{1} convergence of the squared error.
Consequently,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(v^α​(𝐗)−vα​(𝐗))2]→0,n→∞.\displaystyle\mathbb{E}\Big[(\hat{v}\_{\alpha}(\mathbf{X})-v\_{\alpha}(\mathbf{X}))^{2}\Big]\to 0,\qquad n\to\infty. |  |

This establishes the desired L2L^{2} convergence.
∎

The additional moment condition in Assumption [6](https://arxiv.org/html/2602.01912v1#Thmassumption6 "Assumption 6. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") excludes excessively heavy-tailed response distributions, ensuring that the conditional VaR remains well-behaved and that the quantile estimation error admits a finite second moment. Together with the honesty condition on tree construction, these assumptions yield convergence of the QRF-based VaR estimator in the mean squared sense. More importantly, this stronger form of convergence provides a fundamental building block for establishing the asymptotic validity and now we analyze the conformal QRF estimator v^αc\hat{v}\_{\alpha}^{\mathrm{c}}.

###### Proposition 1.

If the samples {(𝐗i,Yi)}i=1n+1\{(\mathbf{X}\_{i},Y\_{i})\}\_{i=1}^{n+1} are exchangeable, then

|  |  |  |
| --- | --- | --- |
|  | ℙ​{Yn+1≤v^αc​(𝐗n+1)}≥α.\displaystyle\mathbb{P}\{Y\_{n+1}\leq\hat{v}^{\mathrm{c}}\_{\alpha}(\mathbf{X}\_{n+1})\}\geq\alpha. |  |

Proposition [1](https://arxiv.org/html/2602.01912v1#Thmproposition1 "Proposition 1. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") follows from Theorem 1 in Romano et al. ([2019](https://arxiv.org/html/2602.01912v1#bib.bib18 "Conformalized quantile regression")).
It provides a finite-sample, model-free marginal coverage probability guarantee for the conformalized online VaR estimator, if we regard 𝐗n+1\mathbf{X}\_{n+1} as the observed risk factor online.
In addition, note that exchangeability is weaker than the independent and identically distributed condition in our setting, and therefore, it is easy to satisfy.
Moreover, one may be interested in a stronger, conditional form, which Theorem [3](https://arxiv.org/html/2602.01912v1#Thmtheorem3 "Theorem 3. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") formalizes by establishing an asymptotic conditional coverage guarantee.

###### Theorem 3.

Under the condition of Theorem [2](https://arxiv.org/html/2602.01912v1#Thmtheorem2 "Theorem 2. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"), assume additionally that the density of the conformity scores EE is bounded away from zero in an open neighborhood of zero, and the conditional distribution of YY given 𝐗=𝐱\mathbf{X}=\mathbf{x} admits a continuous density with respect to the Lebesgue measure.
Then there exists a sequence of random sets Λn⊆ℝd\Lambda\_{n}\subseteq\mathbb{R}^{d} such that ℙ​(𝐗∈Λn)=1−o​(1)\mathbb{P}(\mathbf{X}\in\Lambda\_{n})=1-o(1) and

|  |  |  |
| --- | --- | --- |
|  | sup𝐱∈Λn|ℙ(Y≤v^α,nc(𝐱)|𝐗=𝐱)−α|=op(1).\displaystyle\sup\_{\mathbf{x}\in\Lambda\_{n}}\left|\mathbb{P}\!\left(Y\leq\hat{v}^{\mathrm{c}}\_{\alpha,n}(\mathbf{x})|\mathbf{X}=\mathbf{x}\right)-\alpha\right|=o\_{{p}}(1). |  |

###### Proof.

The conclusion follows immediately by combining the L2L^{2} convergence established in Theorem [2](https://arxiv.org/html/2602.01912v1#Thmtheorem2 "Theorem 2. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") with the additional regularity assumptions, and applying Corollary 1 of Sesia and Candès ([2020](https://arxiv.org/html/2602.01912v1#bib.bib19 "A comparison of some conformal quantile regression methods")).
∎

In addition, the results may be extended to settings without honesty by following what has been done in random forests (Wager and Walther, [2015](https://arxiv.org/html/2602.01912v1#bib.bib17 "Adaptive concentration of regression trees, with application to random forests")).

## 6 Numerical Experiments

We consider a realistic portfolio risk measurement problem involving options written on multiple underlying assets, with the setting adapted from Hong et al. ([2017](https://arxiv.org/html/2602.01912v1#bib.bib49 "Kernel smoothing for nested estimation with application to portfolio risk measurement")).
In particular, the asset price dynamics 𝐒​(t)\mathbf{S}(t) are governed by a dd-dimensional geometric Brownian motion with drifts μi′\mu\_{i}^{\prime}, volatilities σi\sigma\_{i}, and pairwise correlations ρi​j\rho\_{ij}, i,j=1,…,di,j=1,\ldots,d.
Specifically, each underlying asset price evolves according to

|  |  |  |
| --- | --- | --- |
|  | d​Si​(t)Si​(t)=μi′​d​t+∑j=1iAi​j​d​Bj​(t),i=1,…,d,\displaystyle\frac{\mathrm{d}S\_{i}(t)}{S\_{i}(t)}=\mu\_{i}^{\prime}\,\mathrm{d}t+\sum\_{j=1}^{i}A\_{ij}\,\mathrm{d}B\_{j}(t),\qquad i=1,\ldots,d, |  |

where {Bj​(t)}j=1d\{B\_{j}(t)\}\_{j=1}^{d} are independent standard Brownian motions, and the lower triangular matrix AA satisfies Σ=A​A⊤\Sigma=AA^{\top} with the covariance matrix Σ=(Σi​j)\Sigma=(\Sigma\_{ij}) given by Σi​j=σi​σj​ρi​j\Sigma\_{ij}=\sigma\_{i}\sigma\_{j}\rho\_{ij}.

By Itô’s formula, the asset prices admit the explicit expression

|  |  |  |
| --- | --- | --- |
|  | Si​(t)=Si​(0)​exp⁡{(μi′−12​σi2)​t+∑j=1iAi​j​Bj​(t)},i=1,…,d.\displaystyle S\_{i}(t)=S\_{i}(0)\exp\left\{\left(\mu\_{i}^{\prime}-\tfrac{1}{2}\sigma\_{i}^{2}\right)t+\sum\_{j=1}^{i}A\_{ij}B\_{j}(t)\right\},\quad i=1,\ldots,d. |  |

Note that the drift parameter μ′\mu^{\prime} is specified as the real-world expected return μ\mu over the risk horizon [0,τ][0,\tau], and as the risk-free rate rr under the risk-neutral probability measure over (τ,T](\tau,T].
For simplicity, we assume all assets share the same parameters and thus omit subscripts in these notations. We set S​(0)=100S(0)=100, μ=0.08\mu=0.08, r=0.05r=0.05, σ=15%\sigma=15\%, and ρ=0.3\rho=0.3.

In our example, we set d=4d=4, and the portfolio consists of twenty European call options, with five options written on each underlying asset at strike prices K1=90K\_{1}=90, K2=95K\_{2}=95, K3=100K\_{3}=100, K4=105K\_{4}=105, and K5=110K\_{5}=110. All options are assumed to share a common maturity TT.
We set T=1/12T=1/12, i.e., one month, τ=1/52\tau=1/52, i.e., one week, and the monitoring time point for online estimation u=1/252u=1/252, i.e., one day.
The portfolio value at time 0, denoted by V​(0)V(0), can be computed analytically using the Black–Scholes formula. The portfolio value at the risk horizon τ\tau is given by

|  |  |  |
| --- | --- | --- |
|  | V​(τ)=𝔼​[∑k=1d∑j=15e−r​(T−τ)​(Sk​(T)−Kj)+|𝐗​(τ)],\displaystyle V(\tau)=\mathbb{E}\!\left[\left.\sum\_{k=1}^{d}\sum\_{j=1}^{5}\mathrm{e}^{-r(T-\tau)}\big(S\_{k}(T)-K\_{j}\big)^{+}\right|\mathbf{X}(\tau)\right], |  |

where 𝐗​(τ)=𝐒​(τ)\mathbf{X}(\tau)=\mathbf{S}(\tau) in this example.
Accordingly, the portfolio loss at time τ\tau is defined as

|  |  |  |
| --- | --- | --- |
|  | L​(τ)=V​(0)−V​(τ).\displaystyle L(\tau)=V(0)-V(\tau). |  |

Specifically, when computing V​(τ)V(\tau), we approximate the conditional expectation using 500500 inner simulation paths, which is considered sufficient to make the inner error negligible relative to the estimation error (Jiang et al., [2020](https://arxiv.org/html/2602.01912v1#bib.bib77 "Online risk monitoring using offline simulation"); Cai et al., [2020](https://arxiv.org/html/2602.01912v1#bib.bib61 "Online risk measure estimation via natural gradient boosting")).

To verify the consistency of the QRF estimator in Theorems [1](https://arxiv.org/html/2602.01912v1#Thmtheorem1 "Theorem 1. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") and [2](https://arxiv.org/html/2602.01912v1#Thmtheorem2 "Theorem 2. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"), we examine the estimation errors across varying offline sample sizes.
For the conformal QRF estimator, we use 70%70\% of the offline samples for training and the remaining 30%30\% for calibration.
Furthermore, we vary the confidence level α\alpha to examine the performance of the methods in different situations.
In particular, α\alpha is set to be 90.0%90.0\%, 95.0%95.0\%, 99.0%99.0\%, and 99.5%99.5\%.

We use two metrics to quantify the estimation error. The first is the mean root integrated squared error (MRISE), which is used in empirical studies of quantile regression (see, e.g., Bondell et al., [2010](https://arxiv.org/html/2602.01912v1#bib.bib11 "Noncrossing quantile regression curve estimation")), defined as

|  |  |  |
| --- | --- | --- |
|  | MRISE=1m′​∑i=1m′1n′​∑j=1n′(vα​(𝐱i,j)−v^α​(𝐱i,j))2,\displaystyle\mathrm{MRISE}=\frac{1}{m^{\prime}}\sum\_{i=1}^{m^{\prime}}\sqrt{\frac{1}{n^{\prime}}\sum\_{j=1}^{n^{\prime}}\left(v\_{\alpha}(\mathbf{x}\_{i,j})-\hat{v}\_{\alpha}(\mathbf{x}\_{i,j})\right)^{2}}, |  |

where n′n^{\prime} denotes the number of covariate evaluation points and m′m^{\prime} denotes the number of replications.
Here, n′n^{\prime} and m′m^{\prime} are introduced to stabilize the performance evaluation by averaging over multiple covariate points and repeated model training runs, thereby accounting for uncertainty arising from both covariate variation and model learning.
Throughout all experiments, we set n′=1000n^{\prime}=1000 and m′=40m^{\prime}=40.

The second metric is the mean pinball loss (MPL).
Compared with MRISE, MPL captures the asymmetric situation, which imposes a larger penalty on underestimation than on overestimation.
Similar asymmetric metrics are also used in regulatory evaluation approaches (Lopez, [1998](https://arxiv.org/html/2602.01912v1#bib.bib2 "Methods for evaluating value-at-risk estimates")).
Thus, an estimator that errs on the conservative side, i.e., slightly overestimates the target, tends to attain a smaller MPL.
More specifically, it is defined as

|  |  |  |
| --- | --- | --- |
|  | MPL=1m′​∑i=1m′(1n′​∑i=1n′ρα​(vα​(𝐱i,j)−v^α​(𝐱i,j))),ρα​(a)={α​a,a>0,(α−1)​a,a≤0.\displaystyle\mathrm{MPL}=\frac{1}{m^{\prime}}\sum\_{i=1}^{m^{\prime}}\left(\frac{1}{n^{\prime}}\sum\_{i=1}^{n^{\prime}}\rho\_{\alpha}\left(v\_{\alpha}(\mathbf{x}\_{i,j})-\hat{v}\_{\alpha}(\mathbf{x}\_{i,j})\right)\right),\;\rho\_{\alpha}(a)=\begin{cases}\alpha a,&a>0,\\ (\alpha-1)a,&a\leq 0.\end{cases} |  |

![Refer to caption](x1.png)


Figure 1: MRISE of QRF (left) and Conformal QRF (right) under varying offline sample sizes and quantile levels.

Figure [1](https://arxiv.org/html/2602.01912v1#S6.F1 "Figure 1 ‣ 6 Numerical Experiments ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") plots the MRISE of QRF and conformal QRF across different offline sample sizes and VaR confidence levels.
For each confidence level, the MRISE of the QRF estimator decreases and converges as the offline sample size increases, consistent with the theoretical guarantees established in Theorems [1](https://arxiv.org/html/2602.01912v1#Thmtheorem1 "Theorem 1. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") and [2](https://arxiv.org/html/2602.01912v1#Thmtheorem2 "Theorem 2. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
Moreover, it can also be observed that MRISE of QRF tends to increase as the confidence level rises, which comes from the intrinsic estimation difficulty of tail quantiles when data points in extreme regions are scarce (Gnecco et al., [2024](https://arxiv.org/html/2602.01912v1#bib.bib63 "Extremal random forests")).
For conformal QRF, however, the MRISE does not decrease after the calibration step, except for α=99.5%\alpha=99.5\%.
This is acceptable because the conformalization is not tailored to such a symmetric metric.
Moreover, it is reassuring to see that the conformal QRF estimator exhibits a convergence trend similar to the QRF estimator, offering empirical evidence for its reliability in practical use.

![Refer to caption](x2.png)


Figure 2: MPL of QRF (left) and Conformal QRF (right) under varying offline sample sizes and quantile levels.

Figure [2](https://arxiv.org/html/2602.01912v1#S6.F2 "Figure 2 ‣ 6 Numerical Experiments ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration") compares the MPL of QRF and conformal QRF over varying offline sample sizes and VaR confidence levels.
It can be observed that conformal QRF yields a smaller MPL than QRF, different from MRISE performance in Figure [1](https://arxiv.org/html/2602.01912v1#S6.F1 "Figure 1 ‣ 6 Numerical Experiments ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"), confirming the effectiveness of the designed calibration step.
Interestingly, after conformal calibration, as the confidence level becomes more extreme, the MPL decreases more markedly.
It looks a little counterintuitive because, in general, more extreme quantiles are harder to estimate and therefore incur larger errors.
In fact, this pattern comes from the definition of MPL, which penalizes overestimation by the factor 1−α1-\alpha and the factor becomes negligible when α\alpha is large.
Hence, a more conservative estimator that tends to overestimate can achieve a smaller MPL.
Note that conformal QRF is such an estimator, so it is reasonable that it improves MPL across all confidence levels, with the improvement being most marked at the most extreme level.
In addition, MPL values are not comparable across different confidence levels since the pinball loss depends on α\alpha, whereas comparisons of MRISE across levels are meaningful.

![Refer to caption](x3.png)


Figure 3: MCR of QRF and Conformal QRF under varying offline sample sizes and quantile levels.

We then investigate the coverage rate results in Theorem [3](https://arxiv.org/html/2602.01912v1#Thmtheorem3 "Theorem 3. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
Specifically, for the evaluated covariate 𝐱\mathbf{x}, we generate M=25,000M=25{,}000 independent realizations of the portfolio loss {Y(m)}m=1M\{Y^{(m)}\}\_{m=1}^{M} using the same data-generating process as in the construction of the offline samples.
Then the coverage rate (CR) is calculated by

|  |  |  |
| --- | --- | --- |
|  | CR=1n′​∑i=1n′(1M​∑m=1M𝟏​{Yi(m)≤v^α​(𝐱i)}).\displaystyle\mathrm{CR}=\frac{1}{n^{\prime}}\sum\_{i=1}^{n^{\prime}}\left(\frac{1}{M}\sum\_{m=1}^{M}\mathbf{1}\{Y\_{i}^{(m)}\leq\hat{v}\_{\alpha}(\mathbf{x}\_{i})\}\right). |  |

For clarity, we report the mean CR (MCR), obtained by averaging CR over m′m^{\prime} covariates, since results for individual covariate points are much noisy despite being consistent with the overall trend.

The MCRs of QRF and conformal QRF with respect to different offline sample sizes for several VaR confidence levels are plotted in Figure [3](https://arxiv.org/html/2602.01912v1#S6.F3 "Figure 3 ‣ 6 Numerical Experiments ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
It can be seen that the conformal QRF estimator achieves the target level, which verifies the coverage guarantee in Theorem [3](https://arxiv.org/html/2602.01912v1#Thmtheorem3 "Theorem 3. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
Moreover, the QRF estimator approaches the target level as the offline sample size increases but remains significantly undercoverage, which is exactly the motivation for us to introduce the conformal calibration step to recover the coverage rate and to mitigate the undesirable underestimation, and can serve as the supporting empirical evidence.

## 7 Conclusion

In this paper, we have studied the real-time VaR estimation problem for financial portfolios under the OSOA framework, proposed the QRF estimator and the conformal QRF estimator, and analyzed their theoretical properties.
We have demonstrated the efficiency and the reliability of our method through numerical results.

## CRediT authorship contribution statement

Du-Yi Wang: Writing – original draft, Methodology, Software, Visualization, Data Curation.
Guo Liang: Writing – review & editing, Methodology, Validation.
Kun Zhang: Writing – review & editing, Conceptualization, Methodology, Funding acquisition, Supervision, Project administration, Validation.
Qianwen Zhu: Writing – original draft, Methodology, Conceptualization, Investigation, Software, Formal analysis.

## Declaration of competing interest

None declared.

## Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

During the preparation of this work, the authors used ChatGPT in order to polish the language. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article.

## Data availability statement

Data will be made available on request.

## References

* A. N. Angelopoulos and S. Bates (2023)
  Conformal prediction: a gentle introduction.
  Foundations and Trends® in Machine Learning 16 (4),  pp. 494–591.
  Cited by: [item 2](https://arxiv.org/html/2602.01912v1#S1.I1.i2.p1.1 "In 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p4.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§1](https://arxiv.org/html/2602.01912v1#S1.p4.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* S. Athey and G. Imbens (2016)
  Recursive partitioning for heterogeneous causal effects.
  Proceedings of the National Academy of Sciences 113 (27),  pp. 7353–7360.
  Cited by: [Theorem 2](https://arxiv.org/html/2602.01912v1#Thmtheorem2.p1.1.1 "Theorem 2. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* S. Athey, J. Tibshirani, and S. Wager (2019)
  Generalized random forests.
  The Annals of Statistics 47 (2),  pp. 1148–1178.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p3.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§1](https://arxiv.org/html/2602.01912v1#S1.p4.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§5](https://arxiv.org/html/2602.01912v1#S5.p4.1 "5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* Basel Committee on Banking Supervision (1996)
  Supervisory framework for the use of “backtesting” in conjunction with the internal models approach to market risk capital requirements.
  Technical report
   Bank for International Settlements, Basel.
  Cited by: [§1](https://arxiv.org/html/2602.01912v1#S1.p3.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* H. D. Bondell, B. J. Reich, and H. Wang (2010)
  Noncrossing quantile regression curve estimation.
  Biometrika 97 (4),  pp. 825–838.
  Cited by: [§6](https://arxiv.org/html/2602.01912v1#S6.p5.7 "6 Numerical Experiments ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* M. Broadie, Y. Du, and C. C. Moallemi (2015)
  Risk estimation via regression.
  Operations Research 63 (5),  pp. 1077–1097.
  Cited by: [§1](https://arxiv.org/html/2602.01912v1#S1.p4.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§2](https://arxiv.org/html/2602.01912v1#S2.p4.2 "2 Problem Formulation ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* X. Cai, Y. Yang, and G. Jiang (2020)
  Online risk measure estimation via natural gradient boosting.
  In 2020 Winter Simulation Conference (WSC),
   pp. 2341–2352.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p2.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§3](https://arxiv.org/html/2602.01912v1#S3.p3.3 "3 The QRF Estimator ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§6](https://arxiv.org/html/2602.01912v1#S6.p3.17 "6 Numerical Experiments ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* S. D. Campbell (2006)
  A review of backtesting and backtesting procedures.
  Journal of Risk 9,  pp. 1–7.
  Cited by: [§1](https://arxiv.org/html/2602.01912v1#S1.p3.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* D. Cevid, L. Michel, J. Näf, P. Bühlmann, and N. Meinshausen (2022)
  Distributional random forests: heterogeneity adjustment and multivariate distributional regression.
  Journal of Machine Learning Research 23 (333),  pp. 1–79.
  Cited by: [§5](https://arxiv.org/html/2602.01912v1#S5.p4.1 "5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* J. Cherian, I. Gibbs, and E. Candes (2024)
  Language models with conformal factuality guarantees.
  In Advances in Neural Information Processing Systems,
   pp. 114812–114842.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p4.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§1](https://arxiv.org/html/2602.01912v1#S1.p4.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* T. Duan, A. Anand, D. Y. Ding, K. K. Thai, S. Basu, A. Ng, and A. Schuler (2020)
  Ngboost: natural gradient boosting for probabilistic prediction.
  In International Conference on Machine Learning,
   pp. 2690–2700.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p2.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* R. Durrett (2019)
  Probability: theory and examples.
  5th edition, Cambridge University Press.
  Cited by: [§5](https://arxiv.org/html/2602.01912v1#S5.10.p9.3 "Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§5](https://arxiv.org/html/2602.01912v1#S5.11.p10.1 "Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* J. H. Friedman (2001)
  Greedy function approximation: a gradient boosting machine.
  The Annals of Statistics 29 (5),  pp. 1189–1232.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p3.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* N. Gnecco, E. M. Terefe, and S. Engelke (2024)
  Extremal random forests.
  Journal of the American Statistical Association 119 (548),  pp. 3059–3072.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p3.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§1](https://arxiv.org/html/2602.01912v1#S1.p4.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§6](https://arxiv.org/html/2602.01912v1#S6.p7.1 "6 Numerical Experiments ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* M. B. Gordy and S. Juneja (2010)
  Nested simulation in portfolio risk measurement.
  Management Science 56 (10),  pp. 1833–1848.
  Cited by: [§3](https://arxiv.org/html/2602.01912v1#S3.p3.3 "3 The QRF Estimator ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* L. Grinsztajn, E. Oyallon, and G. Varoquaux (2022)
  Why do tree-based models still outperform deep learning on typical tabular data?.
  In Advances in Neural Information Processing Systems,
  Vol. 35,  pp. 507–520.
  Cited by: [§1](https://arxiv.org/html/2602.01912v1#S1.p4.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* L. J. Hong and G. Jiang (2019)
  Offline simulation online application: a new framework of simulation-based decision making.
  Asia-Pacific Journal of Operational Research 36 (06),  pp. 1940015.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p2.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§1](https://arxiv.org/html/2602.01912v1#S1.p2.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§3](https://arxiv.org/html/2602.01912v1#S3.p1.1 "3 The QRF Estimator ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* L. J. Hong, S. Juneja, and G. Liu (2017)
  Kernel smoothing for nested estimation with application to portfolio risk measurement.
  Operations Research 65 (3),  pp. 657–673.
  Cited by: [§2](https://arxiv.org/html/2602.01912v1#S2.p4.2 "2 Problem Formulation ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§6](https://arxiv.org/html/2602.01912v1#S6.p1.6 "6 Numerical Experiments ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* J. Huang, Y. Li, and H. Yao (2022)
  Nonparametric mean-lower partial moment model and enhanced index investment.
  Computers & Operations Research 144,  pp. 105814.
  Cited by: [§1](https://arxiv.org/html/2602.01912v1#S1.p1.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* G. Jiang, L. J. Hong, and B. L. Nelson (2020)
  Online risk monitoring using offline simulation.
  INFORMS Journal on Computing 32 (2),  pp. 356–375.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p2.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§1](https://arxiv.org/html/2602.01912v1#S1.p1.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§1](https://arxiv.org/html/2602.01912v1#S1.p2.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§2](https://arxiv.org/html/2602.01912v1#S2.p4.2 "2 Problem Formulation ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§3](https://arxiv.org/html/2602.01912v1#S3.p3.3 "3 The QRF Estimator ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§6](https://arxiv.org/html/2602.01912v1#S6.p3.17 "6 Numerical Experiments ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* G. Jiang, L. J. Hong, and H. Shen (2024)
  Real-time derivative pricing and hedging with consistent metamodels.
  INFORMS Journal on Computing 36 (5),  pp. 1168–1189.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p2.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* P. Jorion (2006)
  Value at risk: the new benchmark for managing financial risk.
  3rd edition, McGraw-Hill, New York, NY.
  Cited by: [§1](https://arxiv.org/html/2602.01912v1#S1.p1.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* G. Keslin, B. L. Nelson, B. Pagnoncelli, M. Plumlee, and H. Rahimian (2025)
  Ranking and contextual selection.
  Operations Research 73 (5),  pp. 2695–2707.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p2.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* R. Koenker and G. Bassett Jr (1978)
  Regression quantiles.
  Econometrica 46 (1),  pp. 33–50.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p3.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* R. Koenker, P. Ng, and S. Portnoy (1994)
  Quantile smoothing splines.
  Biometrika 81 (4),  pp. 673–680.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p3.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* R. Koenker (2017)
  Quantile regression: 40 years on.
  Annual Review of Economics 9 (1),  pp. 155–176.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p3.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* Q. Lai, G. Liu, B. Zhang, and K. Zhang (2024)
  Simulating confidence intervals for conditional value-at-risk via least-squares metamodels.
  INFORMS Journal on Computing 37 (4),  pp. 1087–1105.
  Cited by: [§2](https://arxiv.org/html/2602.01912v1#S2.p2.14 "2 Problem Formulation ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§3](https://arxiv.org/html/2602.01912v1#S3.p3.3 "3 The QRF Estimator ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* N. Lin, H. Luo, and L. J. Hong (2025)
  Contextual strongly convex simulation optimization: optimize then predict with inexact solutions.
  arXiv preprint arXiv:2512.06270.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p2.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* J. A. Lopez (1998)
  Methods for evaluating value-at-risk estimates.
  Economic Policy Review 4 (3),  pp. 119–124.
  Cited by: [§6](https://arxiv.org/html/2602.01912v1#S6.p6.1 "6 Numerical Experiments ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* H. Luo, Z. Liang, and L. J. Hong (2024)
  Reliable online decision making with covariates.
  In 2024 Winter Simulation Conference (WSC),
   pp. 3265–3276.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p2.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* N. Meinshausen (2006)
  Quantile regression forests..
  Journal of Machine Learning Research 7 (6),  pp. 983–999.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p3.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§1](https://arxiv.org/html/2602.01912v1#S1.p4.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§3](https://arxiv.org/html/2602.01912v1#S3.p3.3 "3 The QRF Estimator ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§5](https://arxiv.org/html/2602.01912v1#S5.1.p1.25 "Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§5](https://arxiv.org/html/2602.01912v1#S5.p4.1 "5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§5](https://arxiv.org/html/2602.01912v1#S5.p6.1 "5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* C. Mohri and T. Hashimoto (2024)
  Language models with conformal factuality guarantees.
  In International Conference on Machine Learning,
  Proceedings of Machine Learning Research, Vol. 235,  pp. 36029–36047.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p4.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§1](https://arxiv.org/html/2602.01912v1#S1.p4.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* Y. Romano, E. Patterson, and E. Candes (2019)
  Conformalized quantile regression.
  In Advances in Neural Information Processing Systems,
  Vol. 32,  pp. 3543–3553.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p4.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§4](https://arxiv.org/html/2602.01912v1#S4.p2.7 "4 The Conformal QRF Estimator ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§5](https://arxiv.org/html/2602.01912v1#S5.p9.1 "5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* M. Sesia and E. J. Candès (2020)
  A comparison of some conformal quantile regression methods.
  Stat 9 (1),  pp. e261.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p4.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§5](https://arxiv.org/html/2602.01912v1#S5.12.p1.1 "Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* J. W. Taylor (2000)
  A quantile regression neural network approach to estimating the conditional density of multiperiod returns.
  Journal of Forecasting 19 (4),  pp. 299–311.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p3.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* C. A. Valle (2025)
  Portfolio optimisation: bridging the gap between theory and practice.
  Computers & Operations Research 175,  pp. 106918.
  Cited by: [§1](https://arxiv.org/html/2602.01912v1#S1.p1.1 "1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* J. Velthoen, C. Dombry, J. Cai, and S. Engelke (2023)
  Gradient boosting for extreme quantile regression.
  Extremes 26 (4),  pp. 639–667.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p2.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p3.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* S. Wager and S. Athey (2018)
  Estimation and inference of heterogeneous treatment effects using random forests.
  Journal of the American Statistical Association 113 (523),  pp. 1228–1242.
  Cited by: [§5](https://arxiv.org/html/2602.01912v1#S5.p4.1 "5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [Theorem 2](https://arxiv.org/html/2602.01912v1#Thmtheorem2.p1.1.1 "Theorem 2. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* S. Wager and G. Walther (2015)
  Adaptive concentration of regression trees, with application to random forests.
  arXiv preprint arXiv:1503.06388.
  Cited by: [§5](https://arxiv.org/html/2602.01912v1#S5.p10.1 "5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* M. J. Wainwright (2019)
  High-dimensional statistics: a non-asymptotic viewpoint.
  Vol. 48, Cambridge University Press.
  Cited by: [§5](https://arxiv.org/html/2602.01912v1#S5.1.p1.25 "Proof. ‣ 5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* W. Wang, Y. Wang, and X. Zhang (2024)
  Smooth nested simulation: bridging cubic and square root convergence rates in high dimensions.
  Management Science 70 (12),  pp. 9031–9057.
  Cited by: [§2](https://arxiv.org/html/2602.01912v1#S2.p4.2 "2 Problem Formulation ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration"),
  [§5](https://arxiv.org/html/2602.01912v1#S5.p2.1 "5 Theoretical Guarantees ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* K. Yu and M. Jones (1998)
  Local linear quantile regression.
  Journal of the American Statistical Association 93 (441),  pp. 228–237.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p3.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* K. Zhang, G. Liu, and S. Wang (2022)
  Bootstrap-based budget allocation for nested simulation.
  Operations Research 70 (2),  pp. 1128–1142.
  Cited by: [§3](https://arxiv.org/html/2602.01912v1#S3.p3.3 "3 The QRF Estimator ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").
* Q. Zhang, L. J. Hong, and H. Yan (2025)
  Conditional generative modeling for enhanced credit risk management in supply chain finance.
  Naval Research Logistics, Publish Online.
  Cited by: [§1.1](https://arxiv.org/html/2602.01912v1#S1.SS1.p2.1 "1.1 Literature Review ‣ 1 Introduction ‣ Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration").