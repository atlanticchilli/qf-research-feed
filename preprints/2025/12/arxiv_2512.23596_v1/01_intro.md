---
authors:
- Agostino Capponi
- Chengpiao Huang
- J. Antonio Sidaoui
- Kaizheng Wang
- Jiacheng Zou
doc_id: arxiv:2512.23596v1
family_id: arxiv:2512.23596
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: The nonstationarity-complexity tradeoff in return prediction
url_abs: http://arxiv.org/abs/2512.23596v1
url_html: https://arxiv.org/html/2512.23596v1
venue: arXiv q-fin
version: 1
year: 2025
---


Agostino Capponi111Department of IEOR and Columbia Business School, Columbia University. Email: [ac3827@columbia.edu](mailto:ac3827@columbia.edu).
  
Chengpiao Huang222Department of IEOR, Columbia University. Email: [chengpiao.huang@columbia.edu](mailto:chengpiao.huang@columbia.edu).
  
J. Antonio Sidaoui333Department of IEOR, Columbia University. Email: [j.sidaoui@columbia.edu](mailto:j.sidaoui@columbia.edu).
  
Kaizheng Wang444Department of IEOR and Data Science Institute, Columbia University. Email: [kaizheng.wang@columbia.edu](mailto:kaizheng.wang@columbia.edu).
  
Jiacheng Zou555Email: [jiachengzou@alumni.stanford.edu](mailto:jiachengzou@alumni.stanford.edu).

(This version: December 29, 2025)

###### Abstract

We investigate machine learning models for stock return prediction in non-stationary environments, revealing a fundamental nonstationarity-complexity tradeoff: complex models reduce misspecification error but require longer training windows that introduce stronger non-stationarity. We resolve this tension with a novel model selection method that jointly optimizes model class and training window size using a tournament procedure that adaptively evaluates candidates on non-stationary validation data. Our theoretical analysis demonstrates that this approach balances misspecification error, estimation variance, and non-stationarity, performing close to the best model in hindsight.

Applying our method to 17 industry portfolio returns, we consistently outperform standard rolling-window benchmarks, improving out-of-sample R2R^{2} by 14–23% on average. During NBER-designated recessions, improvements are substantial: our method achieves positive R2R^{2} during the Gulf War recession while benchmarks are negative, and improves R2R^{2} in absolute terms by at least 80bps during the 2001 recession as well as superior performance during the 2008 Financial Crisis. Economically, a trading strategy based on our selected model generates 31% higher cumulative returns averaged across the industries.

Keywords: Non-stationarity, Model complexity, Return prediction, Model selection, Adaptive window selection

## 1 Introduction

Machine learning (ML) models have emerged as powerful tools for return prediction in financial markets. Recent studies demonstrate that ML models can effectively approximate stochastic discount factor (SDF) by capturing complex nonlinear relationships between risk information carried by characteristics and asset returns (GKX20; FNW20; KXi23; KMZ24). While these studies have shown impressive predictive performance, they implicitly admit a degree of freedom vis-a-vis how historical data is utilized for estimation. The literature typically adopts one of two regimes: either an expanding window that uses all historical data, or a fixed-length rolling window which uses only the most recent observations in a fixed look-back horizon. Both conventions follow the same operating logic: to firstly consider the choice of model class, such as linear regression, random forest, or any other ML model; secondly and conditioned on the model choice, pick a training window. Since financial markets are subject to shocks and exhibit cycles, this separation of model class and training window is ad-hoc rather than built upon rigorous statistical design.

We show that in a non-stationary environment, the complexity of an approximation model of SDF and the estimation window length are deeply intertwined and cannot be optimized independently. They are linked by a fundamental *nonstationarity-complexity tradeoff*. While complex models are effective at reducing model misspecification error, they simultaneously require a larger volume of training data to mitigate their inherent estimation variance. Extending the
training window to meet this data requirement increases the risk of incorporating outdated economic regimes, thereby introducing non-stationarity bias that can degrade a SDF estimator’s predictive performance. This tension creates a “less can be more” dilemma, where a complex model trained on a long window of past data may be outperformed by a simpler model trained on a shorter, more recent window of data.
Consequently, the optimal model complexity depends on the training window size, and vice versa.

A rapidly growing branch of literature has recently established the “virtue of complexity” in return prediction, demonstrating that complex, high-dimensional models can significantly outperform simpler, parsimonious benchmarks (KellyMalamud2025Understanding; Kelly2022Virtue; KMZ24). Drawing on the universal approximation property of neural networks, these studies prove that models where the number of parameters exceeds the number of observations can better leverage the information content of predictive signals by accurately approximating unknown nonlinear functions that govern asset returns. Our work complements this literature by introducing a new dimension to this framework: the role of non-stationarity in the training environment for return prediction.

The “virtue of complexity” literature demonstrates that complex ML models can effectively capture nonlinear SDF relationships. These studies typically employ expanding windows with all available historical data. They show that approximation gains from model flexibility outweigh the statistical costs of heavy parameterization in the classical bias-variance tradeoff. Our work complements this literature by examining how non-stationarity in financial markets, arising from structural breaks and economic cycles, affects the optimal choice of model complexity and training window. When the data generating process shifts over time, realizing the virtue of complexity requires carefully selecting how much historical data to include in training.

Our findings suggest that model complexity and training window size cannot be optimized independently as fixed hyperparameters; rather, they must be chosen jointly to balance misspecification error, statistical uncertainty, and environmental drift. This is the central problem studied in our paper:

*How to jointly choose the model complexity and training window size?*

We complement the insights of the machine learning asset pricing literature, including the surprising dominance of large factor models (DKK24) and the success of deep learning and complexity in return prediction (Kelly2022Virtue and their extensions), by considering the case of unknown temporal distribution shifts. By proposing a data-driven framework that adaptively selects the optimal model class and training window size simultaneously, we offer a method for navigating the complex relationships between predictors and returns as they evolve over time. Our method adaptively selects validation data tailored to the local non-stationarity, allowing for a near-optimal estimation of a model’s future performance. Our framework is general: it can compare any candidate models from different model classes trained on different horizons in any manner.

Our main contributions are three-fold. First, we provide empirical and theoretical investigations of a fundamental nonstationarity-complexity tradeoff in return prediction under non-stationarity. In an empirical study on industry portfolio return prediction, we show that models with greater expressive power or longer training windows may underpreform when the environment changes over time. We then formalize this phenomenon through a finite-sample bound that characterizes the prediction error of a model ff in terms of its model class ℱ\mathcal{F} and training window size kk:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Prediction Error​(f)≲Misspecification​(ℱ)+Uncertainty​(ℱ,nk)+Non-stationarity​(k).\textrm{Prediction Error}(f)~\lesssim~\textrm{Misspecification}(\mathcal{F})+\textrm{Uncertainty}(\mathcal{F},n\_{k})+\textrm{Non-stationarity}(k). |  | (1.1) |

The bound decomposes the prediction error into three sources: the model misspecification error of the model class ℱ\mathcal{F}, the statistical uncertainty associated with learning the model using nkn\_{k} samples in the training window, and the non-stationarity within the last kk periods. This characterization quantifies how model complexity and training window length jointly influence the model’s predictive performance.

Second, motivated by this tradeoff, we develop an adaptive model selection approach for jointly choosing the model class and training window length. Our method is a sequential elimination tournament procedure, and uses a pairwise model comparison subroutine that adaptively selects non-stationary validation data to compare two given models. We prove that our algorithm jointly chooses a model class and training window that near-optimally balance the nonstationarity-complexity tradeoff ([1.1](https://arxiv.org/html/2512.23596v1#S1.E1 "Equation 1.1 ‣ 1 Introduction ‣ The nonstationarity-complexity tradeoff in return prediction")), up to logarithmic factors. Furthermore, we develop a variant tailored to the out-of-sample R2R^{2} metric commonly used in asset pricing.

Third, we demonstrate the empirical efficacy of this framework on daily returns of 17 industry portfolios, and show that it adapts to the local non-stationarity and significantly improves the out-of-sample (OOS) R2R^{2} compared to non-adaptive fixed-window baselines. Over the 1990–2016 OOS period, our method delivers an average R2R^{2} of 0.049 across all industries, representing a 14% improvement over fixed-horizon training with long-horizon validation, and more than doubling the performance of short-horizon validation.

Our method’s advantages are most pronounced during recessions, when non-stationarity is most evident. We examine the three recessions identified by National Bureau of Economic Research (NBER) in its [NBER Business Cycle Dating](https://www.nber.org/research/business-cycle-dating) that fall within our OOS period. During the 1990 Gulf War recession, our framework achieves a positive R2R^{2} of 0.027 while all benchmarks produce negative R2R^{2}, demonstrating the critical importance of handling non-stationarity properly. In the 2001 recession, our method attains an R2R^{2} of 0.125, outperforming the cross-validation benchmark which attains 0.071, a 540 basis point improvement, and the long-window validation benchmark which achieves 0.117, an 80 basis point improvement. During the 2008 Financial Crisis, our method again delivers the strongest performance. These gains are robust across all benchmark methods (Table [2](https://arxiv.org/html/2512.23596v1#S5.T2 "Table 2 ‣ Recession Performance Analysis. ‣ 5.3 Empirical Results: 17 Industry Portfolios ‣ 5 Explaining the Cross-Section of Industry Portfolio Returns ‣ The nonstationarity-complexity tradeoff in return prediction")) and persistent across industries (Figure [5](https://arxiv.org/html/2512.23596v1#S5.F5 "Figure 5 ‣ Recession Performance Analysis. ‣ 5.3 Empirical Results: 17 Industry Portfolios ‣ 5 Explaining the Cross-Section of Industry Portfolio Returns ‣ The nonstationarity-complexity tradeoff in return prediction")), confirming that our adaptive approach effectively navigates the nonstationarity-complexity tradeoff.

Economically, our predictive gains translate to meaningful value: a simple trading strategy based on our selected models generates 31% higher returns than the best-performing validation benchmark, averaged across the 17 industries. This confirms that jointly optimizing model complexity and training window size to address non-stationarity yields substantial benefits for investors.

### 1.1 Related Literature

The integration of machine learning into asset pricing was initially driven by the “multidimensional challenge”, that is, the need to identify which of the hundreds of proposed firm characteristics provide independent information for expected returns.

Early influential work by GKX20 demonstrated that nonlinear interactions missed by traditional regressions are a primary source of predictive gains, identifying trees and neural networks as superior methods. FNW20 used adaptive group LASSO to show that only a small subset of characteristics provides incremental information when nonlinearities are properly accounted for. ChoiJiangZhang2025 applied machine learning to 32 international markets, concluding that market-specific neural networks achieve stronger results than global models by capturing local return-characteristic relationships. We refer to KXi23 for an excellent survey on financial machine learning.

Building on these empirical successes, a series of theoretical papers have formalized the virtue of complexity, proving that out-of-sample forecast accuracy and portfolio Sharpe ratios can be strictly increasing in model complexity. This phenomenon occurs because high complexity induces “implicit shrinkage”, which reduces prediction variance without the heavy bias costs associated with explicit shrinkage. This line of research advocates for the largest approximating model one can compute, because the gains from better approximation of the unknown truth dominate the statistical costs of heavy parameterization. Foundational works in this stream of literature include Kelly2022Virtue; KellyMalamud2025Understanding; KMZ24. They focus on time-series return prediction and market timing, resolving the “double limit” problem of growing parameters and observations to show that complexity captures unknown nonlinearities that improve Sharpe ratios. A recent study by DKK24 extends these insights to the cross-section of returns, tackling a “three infinities” problem involving a simultaneously large number of assets, parameters, and observations. Their work proposes using random Fourier features to generate vast numbers of nonlinear factors, shifting the statistical objective from pure return prediction to minimizing pricing errors and constructing a high-complexity stochastic discount factor that reflects the true drivers of investors’ marginal rates of substitution.

The above surveyed works provide compelling empirical evidence and theoretical justifications for the superiority of complex machine learning models over simple linear models. However, they typically treat the training window as a fixed hyperparameter, often setting it to an expanding window that includes all available historical data. Furthermore, their theoretical analysis typically assumes that the training data is i.i.d. Our work points out that, as the financial market is in constant motion due to structural breaks, shifting risk regimes, and economic cycles, accounting for non-stationarity beyond complexity may lead to even further improvements.

A rich literature has developed statistical frameworks for detecting structural breaks and change points (BUr05). Foundational works such as Cho60; And93; BPe98; Chi98 established rigorous methods to identify structural changes, which have been applied to financial time series including realized volatility (LMa07) and speculative bubbles (HBr12). While these studies focus on identifying when breaks occur, our work addresses how to optimally use non-stationary data for estimation. Rather than pinpointing change points, we determine the optimal training window to minimize prediction error in
the presence of non-stationarity.

A complementary literature examines optimal training window selection under non-stationarity. PTi07 showed that under structural breaks, optimal window selection should balance the bias from including pre-break data against the variance from using only post-break data. Subsequent work explored various selection criteria, including minimizing estimation loss functions (PTi07; IJR17) and aggregating predictions across multiple windows (PPi11). However, these approaches typically assume linear models and specific non-stationary structures, such as single breaks or random walks. Our contribution differs in two key ways. First, we take a model-free approach that does not impose parametric assumptions on either the prediction function or the non-stationary dynamics, allowing us to handle more general patterns. Second, we extend the bias-variance tradeoff identified by PTi07 to the machine learning context by jointly optimizing model complexity and training window size, whereas prior work typically selects windows for a pre-specified model. This joint selection accounts for the fact that more complex models introduce additional misspecification-variance tradeoffs that interact with the choice of training window.

The rest of the paper is organized as follows. [Section˜2](https://arxiv.org/html/2512.23596v1#S2 "2 Problem Setup ‣ The nonstationarity-complexity tradeoff in return prediction") describes the problem setup. [Section˜3](https://arxiv.org/html/2512.23596v1#S3 "3 The Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction") investigates the nonstationarity-complexity tradeoff. [Section˜4](https://arxiv.org/html/2512.23596v1#S4 "4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction") presents the adaptive model selection algorithm. [Section˜5](https://arxiv.org/html/2512.23596v1#S5 "5 Explaining the Cross-Section of Industry Portfolio Returns ‣ The nonstationarity-complexity tradeoff in return prediction") illustrates our algorithm on real datasets. [Section˜6](https://arxiv.org/html/2512.23596v1#S6 "6 Conclusions ‣ The nonstationarity-complexity tradeoff in return prediction") concludes the paper and discusses future directions. Mathematical proofs are deferred to the supplemental materials.

##### Notation and Terminology.

We introduce the mathematical notation used throughout the paper. Let ℤ+={1,2,…}\mathbb{Z}\_{+}=\{1,2,...\} be the set of positive integers. For n∈ℤ+n\in\mathbb{Z}\_{+}, define [n]={1,2,…,n}[n]=\{1,2,...,n\}. For a,b∈ℝa,b\in\mathbb{R}, define a∧b=min⁡{a,b}a\wedge b=\min\{a,b\} and a∨b=max⁡{a,b}a\vee b=\max\{a,b\}. For x∈ℝx\in\mathbb{R}, let x+=x∨0x\_{+}=x\vee 0. The sign of a real number x∈ℝx\in\mathbb{R} is defined by sign​(x)=1\textrm{sign}(x)=1 if x>0x>0, sign​(x)=0\textrm{sign}(x)=0 if x=0x=0, and sign​(x)=−1\textrm{sign}(x)=-1 if x<0x<0. For non-negative sequences {an}n=1∞\{a\_{n}\}\_{n=1}^{\infty} and {bn}n=1∞\{b\_{n}\}\_{n=1}^{\infty}, we write an=O​(bn)a\_{n}=O(b\_{n}) if there exists C>0C>0 such that for all n∈ℤ+n\in\mathbb{Z}\_{+}, an≤C​bna\_{n}\leq Cb\_{n}. We write an=Θ​(bn)a\_{n}=\Theta(b\_{n}) if an=O​(bn)a\_{n}=O(b\_{n}) and bn=O​(an)b\_{n}=O(a\_{n}). Unless otherwise stated, an≲bna\_{n}\lesssim b\_{n} also represents an=O​(bn)a\_{n}=O(b\_{n}). For a finite set SS, we use |S||S| to denote its cardinality.

## 2 Problem Setup

We consider the problem of predicting a response variable y∈ℝy\in\mathbb{R}, such as an asset return, using a vector of covariates 𝒙\bm{x} in a space 𝒳⊆ℝd\mathcal{X}\subseteq\mathbb{R}^{d}. A key feature in our setting is *non-stationarity*: in each time period t=1,…,Tt=1,...,T, the covariates and response (𝒙,y)(\bm{x},y) follow a time-varying joint distribution PtP\_{t}. At the beginning of period tt, we have access to historical data {𝒟j}j=1t−1\{\mathcal{D}\_{j}\}\_{j=1}^{t-1}, where 𝒟j={(𝒙j,i,yj,i)}i=1Bj\mathcal{D}\_{j}=\{(\bm{x}\_{j,i},y\_{j,i})\}\_{i=1}^{B\_{j}} is a set of i.i.d. samples collected from PjP\_{j} at time jj.
Throughout our paper, we will assume that the samples are independent across time.

###### Assumption 2.1 (Independent data).

For each j∈ℤ+j\in\mathbb{Z}\_{+}, the dataset {(𝐱j,i,yj,i)}i=1Bj\{(\bm{x}\_{j,i},y\_{j,i})\}\_{i=1}^{B\_{j}} consists of i.i.d. samples. The datasets {𝒟j}j=1∞\{\mathcal{D}\_{j}\}\_{j=1}^{\infty} are independent.

While financial time series inherently exhibit temporal dependence, Assumption [2.1](https://arxiv.org/html/2512.23596v1#S2.Thmassumption1 "Assumption 2.1 (Independent data). ‣ 2 Problem Setup ‣ The nonstationarity-complexity tradeoff in return prediction") is a standard simplification in the theoretical analysis of machine learning for return prediction and asset pricing (KMZ24; DKK24). Adopting this independence assumption allows us to isolate the effect of non-stationarity, without introducing additional technicalities from temporal dependence.

Our goal is to use the historical data {𝒟j}j=1t−1\{\mathcal{D}\_{j}\}\_{j=1}^{t-1} to construct a prediction model ft:𝒳→ℝf\_{t}:\mathcal{X}\to\mathbb{R} that performs well on the current, unobserved distribution PtP\_{t}.
The performance of a model f:𝒳→ℝf:\mathcal{X}\to\mathbb{R} with respect to the data distribution PtP\_{t} is measured by the mean squared error (MSE):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt​(f)=𝔼(𝒙,y)∼Pt​[(f​(𝒙)−y)2].L\_{t}(f)=\mathbb{E}\_{(\bm{x},y)\sim P\_{t}}\left[\left(f(\bm{x})-y\right)^{2}\right]. |  | (2.1) |

In line with the empirical finance literature, we also use the R2R^{2} metric to evaluate the performance of a given modeling procedure or algorithm alg that produces a prediction model ftalgf\_{t}^{\texttt{alg}} at each time tt. The out-of-sample R2R^{2} for the algorithm alg over an evaluation period [t1,t2][t\_{1},t\_{2}] is computed as666We note that in the R2R^{2} metric ([2.2](https://arxiv.org/html/2512.23596v1#S2.E2 "Equation 2.2 ‣ 2 Problem Setup ‣ The nonstationarity-complexity tradeoff in return prediction")), the denominator is the sum of the squared responses yt,i2y\_{t,i}^{2} *without demeaning*. In other words, we are benchmarking against a forecast of zero rather than the historical mean as in the statistical R2R^{2} metric. As noted by GKX20, predicting future excess stock returns with historical averages can be problematic and is not assumption-free, because the historical mean is estimated with significant noise, often performing worse than a forecast of zero.

|  |  |  |  |
| --- | --- | --- | --- |
|  | R[t1,t2]2​(alg)=1−∑t=t1t2∑i=1Bt(ftalg​(xt,i)−yt,i)2∑t=t1t2∑i=1Btyt,i2.R\_{[t\_{1},t\_{2}]}^{2}(\texttt{alg})=1-\frac{\sum\_{t=t\_{1}}^{t\_{2}}\sum\_{i=1}^{B\_{t}}\left(f\_{t}^{\texttt{alg}}(x\_{t,i})-y\_{t,i}\right)^{2}}{\sum\_{t=t\_{1}}^{t\_{2}}\sum\_{i=1}^{B\_{t}}y\_{t,i}^{2}}. |  | (2.2) |

For completeness, in the appendices we also present results using the statistical R2R^{2} metric

|  |  |  |  |
| --- | --- | --- | --- |
|  | R[t1,t2],s2​(alg)=1−∑t=t1t2∑i=1Bt(ftalg​(xt,i)−yt,i)2∑t=t1t2∑i=1Bt(yt,i−y¯)2,R\_{[t\_{1},t\_{2}],\texttt{s}}^{2}(\texttt{alg})=1-\frac{\sum\_{t=t\_{1}}^{t\_{2}}\sum\_{i=1}^{B\_{t}}\left(f\_{t}^{\texttt{alg}}(x\_{t,i})-y\_{t,i}\right)^{2}}{\sum\_{t=t\_{1}}^{t\_{2}}\sum\_{i=1}^{B\_{t}}(y\_{t,i}-\bar{y})^{2}}, |  | (2.3) |

where y¯\bar{y} is the mean of the samples {yt,i:t∈[t1,t2],i∈[Bt]}\{y\_{t,i}:t\in[t\_{1},t\_{2}],\,i\in[B\_{t}]\}.

In a stationary environment where Pt=PP\_{t}=P for all t∈[T]t\in[T], the standard approach for learning a model ff consists in choosing a model class ℱ\mathcal{F} (e.g., linear model, random forest) and then finding a model f^∈ℱ\widehat{f}\in\mathcal{F} by minimizing the empirical loss over the training data. The choice of the model class ℱ\mathcal{F} involves a classic bias-variance trade-off. A simple class may exhibit high bias due to model misspecification, while a complex class may suffer from high estimation variance.

When the environment is non-stationary (that is, Pi≠PjP\_{i}\neq P\_{j} for i≠ji\neq j), the problem becomes significantly more complicated. One must now make two critical choices simultaneously: the model class ℱ\mathcal{F} and the amount of historical data used for training. Data from the distant past may no longer be representative of the current environment, and can be misleading for model training. This creates the core tension of our paper: complex models require more data to reduce estimation variance, but using more data may introduce stronger non-stationarity that increases bias. Thus, it is possible for simple models with less training data to outperform complex models trained on more data. Our goal is to develop an approach to jointly choose the model class and training window size.

## 3 The Nonstationarity-Complexity Tradeoff

### 3.1 Empirical Evidence

We begin with an empirical illustration that highlights the challenges of jointly choosing a model class and a training window under non-stationarity. The task is to forecast the excess returns of 1717 industry portfolios from Kenneth French’s data library using a set of covariates, with training data starting from September 1987 and ending in October 2016.777More details about the dataset are provided in LABEL:sm:sec-experiments. We highlight that our data spans several recessions documented in [NBER Business Cycle Dating](https://www.nber.org/research/business-cycle-dating): the 1990 Gulf War recession, the 2001 dot-com bubble bust and the 9/11 attack, and the 2007-2009 Financial Crisis. To show that model performance is fundamentally linked to non-stationarity, we document a simple ranking of linear and nonlinear models in each period, across the different industries.

In each month tt, for each industry, we fit three prediction models: (1) a linear model trained by ridge regression using the most recent 6464 months of data, (2) a random forest trained on the most recent 6464 months of data, and (3) a random forest trained on all historical data. More details of the experiments are given in LABEL:sm:sec-tradeoff-empirics-details.

We compute each model’s annual out-of-sample R2R^{2} for every industry. To visualize the models’ relative performance across industries, we count the number of industries in which each model achieves the highest out-of-sample R2R^{2} for a given year. LABEL:sm:fig-tradeoff-dominance summarizes the result. To provide a more granular understanding of the models’ performance, LABEL:sm:fig-tradeoff-industry further plots the annual out-of-sample R2R^{2} of the models for the 1717 industries.

Figure 1: Number of Industries where Each Model Attains the Highest Annual Out-of-Sample R2R^{2}.

![Refer to caption](x1.png)


This figure reports the relative performance of three models in predicting the excess returns of the 1717 industry portfolios. The three models are: (1) a linear model trained by ridge regression on the most recent 6464 months of data (orange), (2) a random forest trained on the most recent 6464 months of data (blue), and (3) a random forest trained on all historical data (white). For each year from 1990 to 2016, we compute the annual out-of-sample R2R^{2} of the models for each of the 1717 industry portfolios, and then count, for each model, the number of industries in which it outperforms the other two models in terms of the annual out-of-sample R2R^{2}.




Figure 2: Annual Out-of-Sample R2R^{2} of Three Models for 1717 Industry Portfolios.

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

![Refer to caption](x5.png)

![Refer to caption](x6.png)

![Refer to caption](x7.png)

![Refer to caption](x8.png)

![Refer to caption](x9.png)

![Refer to caption](x10.png)

![Refer to caption](x11.png)

![Refer to caption](x12.png)

![Refer to caption](x13.png)

![Refer to caption](x14.png)

![Refer to caption](x15.png)

![Refer to caption](x16.png)

![Refer to caption](x17.png)

![Refer to caption](x18.png)

This figure reports, for each of the 1717 industry portfolios, the annual out-of-sample R2R^{2} from 1990 to 2016 for three models: (1) a linear model trained by ridge regression on the most recent 6464 months of data (red), (2) a random forest trained using the most recent 6464 months of data (gray), and (3) a random forest trained using all available historical data up to that year (black). In periods of strong non-stationarity, such as 1990-1991, 2001-2002 and 2008-2009, the linear model trained on a small window constantly outperforms the more complex random forest trained on a large window. The labels in each figure is the Kenneth French acronym for the industries. For full names of these industries, please refer to Table [4](https://arxiv.org/html/2512.23596v1#A1.T4 "Table 4 ‣ A.2 Figures and tables ‣ Appendix A Additional details for empirical asset pricing ‣ The nonstationarity-complexity tradeoff in return prediction").

We make two key observations. First, within the same model class, using less training data may lead to better performance. For example, in several years including 19941994, 19961996 and 20032003, the random forest trained on the most recent 6464 months of data outperforms the random forest trained on all historical data for at least half of the industries.

Second, and more strikingly, a simple model trained on a short window can outperform a complex model trained on a long window. In particular, during the three NBER-designated recessions, the simple linear model trained on 6464 months of data outperforms the more complex random forest model trained on all historical data for over half of the industries. This consistent pattern shows that the advantage of a more expressive model class can be completely negated by the non-stationarity in the training data. In LABEL:sm:sec-select, we propose data-driven approaches to select the best-performing model during such unusual economic regimes.

These empirical findings highlight that in a non-stationary environment, the model complexity and training data size are intricately linked with each other. We call this phenomenon the *nonstationarity-complexity tradeoff*. Crucially, the optimal choice of model class and training window size is not fixed; instead, it generally varies with the degree of the non-stationarity.

### 3.2 Theoretical Characterization

We provide theoretical support for the nonstationarity-complexity tradeoff, by deriving a finite-sample bound on a model’s prediction error under non-stationarity. The bound decomposes the prediction error into three key components: model misspecification error, statistical uncertainty, and non-stationarity, and shows how they interact with the choice of model class and training window length.

Consider a model f^\widehat{f} trained from a model class ℱ\mathcal{F} by minimizing the empirical loss over training data from the last kk periods, denoted by {𝒟jtr}j=t−kt−1\big\{\mathcal{D}^{\operatorname{\mathrm{tr}}}\_{j}\big\}\_{j=t-k}^{t-1}, where 𝒟jtr={(𝒙j,itr,yj,itr)}i=1mj\mathcal{D}^{\operatorname{\mathrm{tr}}}\_{j}=\big\{\big(\bm{x}^{\operatorname{\mathrm{tr}}}\_{j,i},y^{\operatorname{\mathrm{tr}}}\_{j,i}\big)\big\}\_{i=1}^{m\_{j}} is the training data in period jj. That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^=argminf∈ℱ1mt,k​∑j=t−kt−1∑i=1mj[f​(𝒙j,itr)−yj,itr]2,\widehat{f}=\mathop{\mathrm{argmin}}\_{f\in\mathcal{F}}\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}\sum\_{i=1}^{m\_{j}}\left[f(\bm{x}^{\operatorname{\mathrm{tr}}}\_{j,i})-y^{\operatorname{\mathrm{tr}}}\_{j,i}\right]^{2}, |  | (3.1) |

where mt,k=∑j=t−kt−1mjm\_{t,k}=\sum\_{j=t-k}^{t-1}m\_{j} is the number of training data points in {𝒟jtr}j=t−kt−1\big\{\mathcal{D}^{\operatorname{\mathrm{tr}}}\_{j}\big\}\_{j=t-k}^{t-1}.

Define the Bayes optimal least squares estimator ft∗​(⋅)=𝔼(𝒙,y)∼Pt​[y∣𝒙=⋅]f\_{t}^{\*}(\cdot)=\mathbb{E}\_{(\bm{x},y)\sim P\_{t}}[y\mid\bm{x}=\cdot], which minimizes the MSE Lt​(f)L\_{t}(f) over all possible prediction models f:𝒳→ℝf:\mathcal{X}\to\mathbb{R}. Our bound will be stated in terms of the *excess risk*

|  |  |  |
| --- | --- | --- |
|  | ℰt​(f)=Lt​(f)−Lt​(ft∗),\mathcal{E}\_{t}(f)=L\_{t}(f)-L\_{t}(f\_{t}^{\*}), |  |

which compares the prediction error of a model ff against that of ft∗f\_{t}^{\*}. To facilitate analysis, we make the following boundedness assumption.

###### Assumption 3.1 (Boundedness).

There exists a constant M>0M>0 such that for all models ff in the class ℱ\mathcal{F}, (𝐱,y)∼Pj(\bm{x},y)\sim P\_{j} and j∈ℤ+j\in\mathbb{Z}\_{+}, we have |f​(𝐱)|≤M|f(\bm{x})|\leq M, and |y|≤M|y|\leq M. Without loss of generality we assume M≥1M\geq 1.

To quantify the effective complexity of the model class ℱ\mathcal{F} relative to the training window size kk, we employ a measure rt,k​(ℱ)r\_{t,k}(\mathcal{F}) derived from the theory of *local Rademacher complexity* (BBM05).
Given the technical nature of this measure, we defer its formal definition to LABEL:sm:sec-tradeoff-theory-appendix.
The local Rademacher complexity measures the ability of the near-optimal models in ℱ\mathcal{F} to fit random noise using data within the training window kk. A higher complexity indicates a richer model class that is capable of approximating complex patterns, but also signals a higher estimation variance and thus a higher risk of overfitting.
As an illustration, we now present the complexity measure rt,k​(ℱ)r\_{t,k}(\mathcal{F}) for several common model classes. The results are proved in LABEL:sm:sec-proof-eg-classes.

###### Example 3.1 (Finite class).

If |ℱ|<∞|\mathcal{F}|<\infty, then rt,k​(ℱ)≤(4​M​log⁡|ℱ|)/mt,kr\_{t,k}(\mathcal{F})\leq(4M\log|\mathcal{F}|)/m\_{t,k}.

###### Example 3.2 (Linear class).

Recall 𝒳⊆ℝd\mathcal{X}\subseteq\mathbb{R}^{d}. For every 𝛉∈ℝd\bm{\theta}\in\mathbb{R}^{d}, define f𝛉:𝒳→ℝf\_{\bm{\theta}}:\mathcal{X}\to\mathbb{R} by f𝛉​(𝐱)=⟨𝛉,𝐱⟩f\_{\bm{\theta}}(\bm{x})=\langle\bm{\theta},\bm{x}\rangle. Suppose that ℱ⊆{f𝛉:𝛉∈ℝd}\mathcal{F}\subseteq\{f\_{\bm{\theta}}:\bm{\theta}\in\mathbb{R}^{d}\}. Then,
rt,k​(ℱ)≤c​d/mt,kr\_{t,k}(\mathcal{F})\leq cd/m\_{t,k} holds with some constant cc.

###### Example 3.3 (Kernel class).

Let ℍ\mathbb{H} be a reproducing kernel Hilbert space (Wah90) with inner product ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle and norm ∥⋅∥ℍ\|\cdot\|\_{\mathbb{H}}, and ϕ:𝒳→ℍ\phi:\mathcal{X}\to\mathbb{H} be a feature mapping. For any 𝛉∈ℍ\bm{\theta}\in\mathbb{H}, define f𝛉:𝒳→ℝf\_{\bm{\theta}}:\mathcal{X}\to\mathbb{R} by f𝛉​(𝐱)=⟨𝛉,ϕ​(𝐱)⟩f\_{\bm{\theta}}(\bm{x})=\langle\bm{\theta},\phi(\bm{x})\rangle. Consider the function class ℱ={f𝛉:‖𝛉‖ℍ≤R}\mathcal{F}=\{f\_{\bm{\theta}}:\|\bm{\theta}\|\_{\mathbb{H}}\leq R\} for some constant R>0R>0. Model fitting in this class can be efficiently implemented through kernel ridge regression, which is a finite-dimensional convex program even if ℍ\mathbb{H} and ℱ\mathcal{F} are infinite-dimensional.

Suppose there exists a trace-class operator 𝐒:ℍ→ℍ\bm{S}:\mathbb{H}\to\mathbb{H} such that for any j∈ℤ+j\in\mathbb{Z}\_{+} and 𝐯∈ℍ\bm{v}\in\mathbb{H}, we have 𝔼(𝐱,y)∼Pj​|⟨ϕ​(𝐱),𝐯⟩|2≤⟨𝐯,𝐒​𝐯⟩\mathbb{E}\_{(\bm{x},y)\sim P\_{j}}|\langle\phi(\bm{x}),\bm{v}\rangle|^{2}\leq\langle\bm{v},\bm{S}\bm{v}\rangle. Let {μk}k=1∞\{\mu\_{k}\}\_{k=1}^{\infty} be the eigenvalues of 𝐒\bm{S} sorted in descending order. We have the following results:

* •

  (Exponential decay) If there are constants c1,c2>0c\_{1},c\_{2}>0 such that μk≤c1​e−c2​k\mu\_{k}\leq c\_{1}e^{-c\_{2}k} holds for all kk, then rt,k​(ℱ)≤(C​log⁡mt,k)/mt,kr\_{t,k}(\mathcal{F})\leq(C\log m\_{t,k})/m\_{t,k} holds with some constant CC.
* •

  (Polynomial decay) If there are constants c>0c>0 and α≥1\alpha\geq 1 such that μk≤c​k−2​α\mu\_{k}\leq ck^{-2\alpha} holds for all kk, then rt,k​(ℱ)≤C​mt,k−2​α2​α+1r\_{t,k}(\mathcal{F})\leq Cm\_{t,k}^{-\frac{2\alpha}{2\alpha+1}} holds with some constant CC.

Examples of the above two cases include function spaces induced by the Gaussian kernel and Sobolev spaces, respectively (Wai19).

In the classical setting where the training data {𝒟j}j=t−kt−1\{\mathcal{D}\_{j}\}\_{j=t-k}^{t-1} is i.i.d., the complexity measure rt,k​(ℱ)r\_{t,k}(\mathcal{F}) is a key component in bounding the excess risk of f^\widehat{f}: with high probability,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰt​(f^)≲minf∈ℱ⁡ℰt​(f)+(rt,k​(ℱ)+1mt,k).\mathcal{E}\_{t}(\widehat{f})\lesssim\min\_{f\in\mathcal{F}}\mathcal{E}\_{t}(f)+\left(r\_{t,k}(\mathcal{F})+\frac{1}{m\_{t,k}}\right). |  | (3.2) |

In particular, the prediction error is decomposed into two terms:

1. 1.

   *Model misspecification error*

   |  |  |  |
   | --- | --- | --- |
   |  | minf∈ℱ⁡ℰt​(f)=minf∈ℱ⁡Lt​(f)−Lt​(ft∗),\min\_{f\in\mathcal{F}}\mathcal{E}\_{t}(f)=\min\_{f\in\mathcal{F}}L\_{t}(f)-L\_{t}(f\_{t}^{\*}), |  |

   which describes how well ℱ\mathcal{F} can approximate the Bayes optimal least squares estimator ft∗f\_{t}^{\*} at time tt. A more complex model class tends to reduce the model misspecification error.
2. 2.

   *Statistical uncertainty*

   |  |  |  |
   | --- | --- | --- |
   |  | rt,k​(ℱ)+1mt,k,r\_{t,k}(\mathcal{F})+\frac{1}{m\_{t,k}}, |  |

   which quantifies the estimation variance of the model f^\widehat{f}. As is discussed above, using a more complex model class increases the statistical uncertainty of the fitted model. Consequently, a more complex model typically requires a longer training window kk to mitigate its estimation variance.

The classical error bound ([3.2](https://arxiv.org/html/2512.23596v1#S3.E2 "Equation 3.2 ‣ 3.2 Theoretical Characterization ‣ 3 The Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction")) shows that in the i.i.d. case, increasing the training window size kk always reduces the statistical uncertainty, thereby lowering the total prediction error. However, we now present our theory to show that under non-stationarity, this logic is incomplete. As we increase the window size kk to reduce estimation variance, we inadvertently include older data distributions that differ from the target, introducing a third error component. We formalize this in the following theorem.

###### Theorem 3.1 (Prediction error bound).

Let Assumptions [2.1](https://arxiv.org/html/2512.23596v1#S2.Thmassumption1 "Assumption 2.1 (Independent data). ‣ 2 Problem Setup ‣ The nonstationarity-complexity tradeoff in return prediction") and [3.1](https://arxiv.org/html/2512.23596v1#S3.Thmassumption1 "Assumption 3.1 (Boundedness). ‣ 3.2 Theoretical Characterization ‣ 3 The Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction") hold, and fix δ∈(0,1)\delta\in(0,1). With probability at least 1−δ1-\delta, the model f^\widehat{f} defined by ([3.1](https://arxiv.org/html/2512.23596v1#S3.E1 "Equation 3.1 ‣ 3.2 Theoretical Characterization ‣ 3 The Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction")) satisfies

|  |  |  |
| --- | --- | --- |
|  | ℰt​(f^)≲minf∈ℱ⁡ℰt​(f)+M2​(rt,k​(ℱ)+log⁡(1/δ)mt,k)+M2​maxt−k≤j≤t−1⁡TV⁡(Pj,Pt).\mathcal{E}\_{t}(\widehat{f})\lesssim\min\_{f\in\mathcal{F}}\mathcal{E}\_{t}(f)+M^{2}\left(r\_{t,k}(\mathcal{F})+\frac{\log(1/\delta)}{m\_{t,k}}\right)+M^{2}\max\_{t-k\leq j\leq t-1}\operatorname{TV}\left(P\_{j},P\_{t}\right). |  |

Here ≲\lesssim hides a universal constant, and TV⁡(Pj,Pt)=maxA⁡|Pj​(A)−Pt​(A)|\operatorname{TV}(P\_{j},P\_{t})=\max\_{A}|P\_{j}(A)-P\_{t}(A)| is the total variation distance.

###### Proof of LABEL:sm:thm-tradeoff.

See LABEL:sm:sec-tradeoff-theory-appendix.
∎

LABEL:sm:thm-tradeoff reveals that the non-stationarity adds a third dimension to the classical prediction error bound ([3.2](https://arxiv.org/html/2512.23596v1#S3.E2 "Equation 3.2 ‣ 3.2 Theoretical Characterization ‣ 3 The Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction")), namely, a *non-stationarity* term

|  |  |  |
| --- | --- | --- |
|  | maxt−k≤j≤t−1⁡TV⁡(Pj,Pt),\max\_{t-k\leq j\leq t-1}\operatorname{TV}\left(P\_{j},P\_{t}\right), |  |

which quantifies the distribution drift in the environment within the last kk periods. Unlike the statistical uncertainty, this error component increases with the window size kk.
In LABEL:sm:tab-generalization-components, we summarize how the model complexity and the training window size kk impact the three sources of error.

Table 1: Impacts of Model Complexity and Training Window Size on Prediction Error

|  |  |  |  |
| --- | --- | --- | --- |
|  | Misspecification Error | Statistical Uncertainty | Non-Stationarity |
| Model Complexity ↗\nearrow | ↘\searrow | ↗\nearrow | - |
| Training Window kk ↗\nearrow | - | ↘\searrow | ↗\nearrow |

The error decomposition in LABEL:sm:thm-tradeoff formalizes the empirical observations in LABEL:sm:sec-tradeoff-empirics: (i) Using a more expressive model class reduces misspecification error but increases the risk of overfitting, and (ii) using a longer training window reduces statistical uncertainty but increases non-stationarity. As a result, neither greater model complexity nor more training data is uniformly beneficial under non-stationarity.
Below we illustrate this phenomenon through a simple example.

###### Example 3.4 (Selection of model class and window under non-stationarity).

Let η,γ∈[0,1]\eta,\gamma\in[0,1] be two small constants. Suppose that at each time tt, the covariate and response (x,y)∼Pt(x,y)\sim P\_{t} satisfy x∼Uniform​[0,1]x\sim\textrm{Uniform}[0,1], y|x∼N​(ft∗​(x),1)y|x\sim N(f\_{t}^{\*}(x),1), and

|  |  |  |
| --- | --- | --- |
|  | ft∗​(x)=ct​x+γ​sin⁡(2​π​x),f\_{t}^{\*}(x)=c\_{t}x+\gamma\sin(2\pi x), |  |

where {ct}t=1∞\{c\_{t}\}\_{t=1}^{\infty} is a deterministic sequence in [0,1][0,1] satisfying |ct+1−ct|=η|c\_{t+1}-c\_{t}|=\eta. We observe a single sample per period. Consider two model classes: linear class and kernel class with a first-order Sobolev kernel (see, e.g., Example 12.16 in Wai19).

* •

  If we train a linear model with a training window kk, then the three components of the prediction error bound in [Theorem˜3.1](https://arxiv.org/html/2512.23596v1#S3.Thmtheorem1 "Theorem 3.1 (Prediction error bound). ‣ 3.2 Theoretical Characterization ‣ 3 The Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction") satisfy

  |  |  |  |
  | --- | --- | --- |
  |  | minf∈ℱ⁡ℰt​(f)≍γ2,rt,k​(ℱ)≍k−1,maxt−k≤j≤t−1⁡TV⁡(Pj,Pt)≍k​η.\min\_{f\in\mathcal{F}}\mathcal{E}\_{t}(f)\asymp\gamma^{2},\qquad r\_{t,k}(\mathcal{F})\asymp k^{-1},\qquad\max\_{t-k\leq j\leq t-1}\operatorname{TV}\left(P\_{j},P\_{t}\right)\asymp k\eta. |  |

  Optimizing their sum over kk yields the optimal window size k∗≍η−1/2k^{\*}\asymp\eta^{-1/2}, which leads to an O​(γ2+η1/2)O(\gamma^{2}+\eta^{1/2}) bound on the prediction error.
* •

  If we use the kernel class, then ft∗f\_{t}^{\*} is well-specified. For a training window kk, we have

  |  |  |  |
  | --- | --- | --- |
  |  | minf∈ℱ⁡ℰt​(f)=0,rt,k​(ℱ)≍k−2/3,maxt−k≤j≤t−1⁡TV⁡(Pj,Pt)≍k​η.\min\_{f\in\mathcal{F}}\mathcal{E}\_{t}(f)=0,\qquad r\_{t,k}(\mathcal{F})\asymp k^{-2/3},\qquad\max\_{t-k\leq j\leq t-1}\operatorname{TV}\left(P\_{j},P\_{t}\right)\asymp k\eta. |  |

  The optimal training window is k∗≍η−3/5k^{\*}\asymp\eta^{-3/5}, which results in a prediction error of O​(η2/5)O(\eta^{2/5}).

We observe that for both classes, the optimal window size depends on the severity of the drift η\eta, and is in general not the full window size. If one naïvely uses the kernel class with a large window size, then the resulting error scales as O​(k​η)O(k\eta), which is linear in kk and can be much worse than the above bounds.

As expected, the preferable model class depends on the interplay between misspecification γ\gamma and drift η\eta. The kernel class is more expressive but more sensitive to drift. When η=O​(γ5)\eta=O(\gamma^{5}), drift is relatively mild and the kernel is optimal, consistent with the “virtue of complexity” (KellyMalamud2025Understanding; Kelly2022Virtue; KMZ24). However, when η≫γ5\eta\gg\gamma^{5}, severe non-stationarity requires shorter training windows under which sample sizes are too limited for the kernel estimator to fully exploit its flexibility advantage. In this high-drift regime, the linear class achieves better performance with its shorter optimal window, explaining the “less can be more” phenomenon observed in our experiments.

## 4 Adaptive Model and Data Selection under Non-Stationarity

LABEL:sm:sec-tradeoff shows that the predictive performance of a model depends jointly on its complexity and the size of the training data, and that the optimal choice often varies over time with the non-stationarity. As the non-stationarity is generally unknown *a priori*, the selection of the model class and training window calls for a data-driven approach.

In this section, we develop a novel method that uses historical validation data to select the best model from a set of candidates. These candidate models can come from different model classes, be trained on different time windows, or use different hyperparameters. The main challenge is that the same non-stationarity that complicates model training also incapacitates standard model selection techniques such as holdout and cross validation.
Specifically, in a non-stationary environment, a model that performs well on a validation set from the distant past may not perform as well in the future. Our solution is to adaptively select the relevant validation data that best reflects the current environment, allowing for a more accurate comparison of the candidate models’ future performance.

We now formally set up the framework, illustrated in [Figure˜3](https://arxiv.org/html/2512.23596v1#S4.F3 "In 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction"). In each period tt, we split the available data {𝒟j}j=1t−1\{\mathcal{D}\_{j}\}\_{j=1}^{t-1} into a training dataset {𝒟jtr}j=1t−1\{\mathcal{D}\_{j}^{\operatorname{\mathrm{tr}}}\}\_{j=1}^{t-1} and a validation dataset {𝒟jva}j=1t−1\{\mathcal{D}\_{j}^{\operatorname{\mathrm{va}}}\}\_{j=1}^{t-1}. We use the training data {𝒟jtr}j=1t−1\{\mathcal{D}\_{j}^{\operatorname{\mathrm{tr}}}\}\_{j=1}^{t-1} to produce a finite set of candidate models {fλ}λ=1Λ\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda}.
These candidates can come from different model classes, be trained on different data horizons, or use different hyperparameters. We will use the validation data {𝒟jva}j=1t−1\{\mathcal{D}\_{j}^{\operatorname{\mathrm{va}}}\}\_{j=1}^{t-1} to select a good model f^=fλ^\widehat{f}=f\_{\widehat{\lambda}} that performs best at time tt.

Figure 3: Our Framework for Model Training and Selection under Non-stationarity.

![Refer to caption](x19.png)

### 4.1 Adaptive Tournament Model Selection

In this section, we describe our model selection approach, which uses a sequential elimination tournament. The procedure relies on a pairwise comparison subroutine 𝒜\mathcal{A} which is designed to compare two given models ff and f′f^{\prime}, and output the better model, denoted by 𝒜​(f,f′)\mathcal{A}(f,f^{\prime}). In each round, we choose one remaining model ff as a pivot model and compare it against each remaining model f′f^{\prime} using 𝒜\mathcal{A}. If the pivot ff wins all pairwise comparisons, it is declared the winner; otherwise, the models that defeated ff advance to the next round. The procedure is formally described in LABEL:sm:alg-tournament.

Input: Candidate models {fλ}λ=1Λ\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda}, validation data {𝒟jva}j=1t\{\mathcal{D}^{\operatorname{\mathrm{va}}}\_{j}\}\_{j=1}^{t}, pairwise model comparison subroutine 𝒜\mathcal{A}.

Initialize S={fλ}λ=1ΛS=\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda}. // collection of remaining models

while |S|>1|S|>1

Choose a pivot model f∈Sf\in S uniformly at random.

Initialize S′←∅S^{\prime}\leftarrow\emptyset. // collection of models in SS that outperform ff

for f′∈S\{f}f^{\prime}\in S\backslash\{f\}

Run 𝒜\mathcal{A} to compare {f,f′}\{f,f^{\prime}\} to obtain 𝒜​(f,f′)\mathcal{A}(f,f^{\prime}).

If 𝒜​(f,f′)=f′\mathcal{A}(f,f^{\prime})=f^{\prime}, set S′←S′∪{f′}S^{\prime}\leftarrow S^{\prime}\cup\{f^{\prime}\}.

if S′=∅S^{\prime}=\emptyset

return f^=f\widehat{f}=f. // if no model outperforms ff, output ff

else

Set S←S′S\leftarrow S^{\prime}.

return the only model f^∈S\widehat{f}\in S.

Algorithm 1  Adaptive Tournament Model Selection (ATOMS)

LABEL:sm:alg-tournament has two attractive properties. First, in terms of computational efficiency, the expected number of pairwise comparisons scales linearly with the number of models Λ\Lambda.

###### Lemma 4.1 (Computational complexity).

LABEL:sm:alg-tournament calls the subroutine 𝒜\mathcal{A} for Θ​(Λ)\Theta(\Lambda) times in expectation.

###### Proof of LABEL:sm:lem-complexity-tournament.

See LABEL:sm:sec-lem-complexity-tournament-proof.
∎

Second, regarding the statistical accuracy of model selection, we show later that LABEL:sm:alg-tournament preserves the performance guarantee of any pairwise comparison subroutine 𝒜\mathcal{A}, incurring only a logarithmic factor overhead in the number of models Λ\Lambda.

##### Pairwise comparison subroutine.

We now detail the model comparison subroutine 𝒜\mathcal{A}. As we mentioned before, directly comparing the models on the non-stationary validation data {𝒟jva}j=1t−1\{\mathcal{D}^{\operatorname{\mathrm{va}}}\_{j}\}\_{j=1}^{t-1} may lead to significantly biased estimates of the model performance. To address this problem, we take an approach based on the adaptive rolling window framework developed by HHW24.

The main idea is as follows. To choose between two models, it suffices to determine the sign of their *performance gap*

|  |  |  |
| --- | --- | --- |
|  | Δt=Lt​(f1)−Lt​(f2).\Delta\_{t}=L\_{t}(f\_{1})-L\_{t}(f\_{2}). |  |

Indeed, f2f\_{2} is better than f1f\_{1} if and only if Δt>0\Delta\_{t}>0. To estimate Δt\Delta\_{t} from the non-stationary validation data, a natural idea is to take a *look-back window* ℓ∈[t−1]\ell\in[t-1], and use the validation data from the last ℓ\ell periods, 𝒟jva={(𝒙j,iva,yj,iva)}i=1nj\mathcal{D}^{\operatorname{\mathrm{va}}}\_{j}=\big\{\big(\bm{x}^{\operatorname{\mathrm{va}}}\_{j,i},y^{\operatorname{\mathrm{va}}}\_{j,i}\big)\big\}\_{i=1}^{n\_{j}}, j=t−ℓ,…,t−1j=t-\ell,...,t-1, to form a rolling window estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ^t,ℓ=1nt,ℓ​∑j=t−ℓt−1∑i=1njuj,i,whereuj,i=[f1​(𝒙j,iva)−yj,iva]2−[f2​(𝒙j,iva)−yj,iva]2,\widehat{\Delta}\_{t,\ell}=\frac{1}{n\_{t,\ell}}\sum\_{j=t-\ell}^{t-1}\sum\_{i=1}^{n\_{j}}u\_{j,i},\quad\text{where}\quad u\_{j,i}=\left[f\_{1}(\bm{x}^{\operatorname{\mathrm{va}}}\_{j,i})-y^{\operatorname{\mathrm{va}}}\_{j,i}\right]^{2}-\left[f\_{2}(\bm{x}^{\operatorname{\mathrm{va}}}\_{j,i})-y^{\operatorname{\mathrm{va}}}\_{j,i}\right]^{2}, |  | (4.1) |

and nt,ℓ=∑j=t−ℓt−1njn\_{t,\ell}=\sum\_{j=t-\ell}^{t-1}n\_{j}. The accuracy of model comparison depends on the estimation accuracy of Δ^t,ℓ\widehat{\Delta}\_{t,\ell}. The critical challenge is choosing a validation window size ℓ\ell such that the estimation error |Δ^t,ℓ−Δt||\widehat{\Delta}\_{t,\ell}-\Delta\_{t}| is small.

The choice of the validation window ℓ\ell involves a bias-variance tradeoff: with probability at least 1−δ1-\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Δ^t,ℓ−Δt|≤ϕ​(t,ℓ)+ψ​(t,ℓ,δ).\big|\widehat{\Delta}\_{t,\ell}-\Delta\_{t}\big|\leq\phi(t,\ell)+\psi(t,\ell,\delta). |  | (4.2) |

Here,

|  |  |  |
| --- | --- | --- |
|  | ϕ​(t,ℓ)=maxt−ℓ≤j≤t−1⁡|Δj−Δt|\phi(t,\ell)=\max\_{t-\ell\leq j\leq t-1}|\Delta\_{j}-\Delta\_{t}| |  |

is the bias term that measures the non-stationarity of Δj\Delta\_{j} in the last ℓ\ell periods, and

|  |  |  |
| --- | --- | --- |
|  | ψ​(t,ℓ,δ)={8​M2,if ​nt,ℓ=1σt,ℓ​2​log⁡(2/δ)nt,ℓ+16​M2​log⁡(2/δ)3​nt,ℓ,if ​nt,ℓ≥2,withσt,ℓ2=1nt,ℓ​∑j=t−ℓt−1nj​var⁡(uj,1),\psi(t,\ell,\delta)=\begin{cases}8M^{2},&\ \text{if }n\_{t,\ell}=1\\[6.0pt] \displaystyle\sigma\_{t,\ell}\sqrt{\frac{2\log(2/\delta)}{n\_{t,\ell}}}+\frac{16M^{2}\log(2/\delta)}{3n\_{t,\ell}},&\ \text{if }n\_{t,\ell}\geq 2\end{cases},\quad\text{with}\quad\sigma\_{t,\ell}^{2}=\frac{1}{n\_{t,\ell}}\sum\_{j=t-\ell}^{t-1}n\_{j}\operatorname{{\rm var}}(u\_{j,1}), |  |

is the variance term that quantifies the statistical uncertainty associated with the estimate Δ^t,ℓ\widehat{\Delta}\_{t,\ell} via a Bernstein concentration inequality. In general, as the window ℓ\ell increases, we expect the bias ϕ​(t,ℓ)\phi(t,\ell) to increase and the variance term ψ​(t,ℓ)\psi(t,\ell) to decrease. The ideal validation window size ℓ∗\ell^{\*} should strike a balance between the bias and variance:

|  |  |  |
| --- | --- | --- |
|  | ℓ∗=argminℓ∈[t−1]{ϕ​(t,ℓ)+ψ​(t,ℓ,δ)}.\ell^{\*}=\mathop{\mathrm{argmin}}\_{\ell\in[t-1]}\left\{\phi(t,\ell)+\psi(t,\ell,\delta)\right\}. |  |

However, as both ϕ​(t,ℓ)\phi(t,\ell) and ψ​(t,ℓ)\psi(t,\ell) depend on the unknown non-stationarity, ℓ∗\ell^{\*} cannot be directly computed.

To tackle this problem, we construct proxies ψ^\widehat{\psi} and ϕ^\widehat{\phi} for ψ\psi and ϕ\phi, respectively. The proxy for ψ​(t,ℓ,δ)\psi(t,\ell,\delta) is constructed by replacing the unknown variance σt,ℓ2\sigma\_{t,\ell}^{2} by the sample variance

|  |  |  |  |
| --- | --- | --- | --- |
|  | v^t,ℓ2=1nt,ℓ−1​∑j=t−ℓt−1∑i=1nj(uj,i−Δ^t,ℓ)2,\widehat{v}\_{t,\ell}^{2}=\frac{1}{n\_{t,\ell}-1}\sum\_{j=t-\ell}^{t-1}\sum\_{i=1}^{n\_{j}}\big(u\_{j,i}-\widehat{\Delta}\_{t,\ell}\big)^{2}, |  | (4.3) |

which gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ^​(t,ℓ,δ)={8​M2,if ​nt,ℓ=1v^t,ℓ​2​log⁡(2/δ)nt,ℓ+64​M2​log⁡(2/δ)3​(nt,ℓ−1),if ​nt,ℓ≥2.\widehat{\psi}(t,\ell,\delta)=\begin{cases}8M^{2},&\ \text{if }n\_{t,\ell}=1\\[6.0pt] \displaystyle\widehat{v}\_{t,\ell}\sqrt{\frac{2\log(2/\delta)}{n\_{t,\ell}}}+\frac{64M^{2}\log(2/\delta)}{3(n\_{t,\ell}-1)},&\ \text{if }n\_{t,\ell}\geq 2\end{cases}. |  | (4.4) |

The proxy for the bias term is inspired by the Goldenshluger-Lepski method for adaptive non-parametric estimation (GLe08):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^(t,ℓ,δ)=maxi∈[ℓ](|Δ^t,ℓ−Δ^t,i|−[ψ^(t,ℓ,δ)+ψ^(t,i,δ)])+.\widehat{\phi}(t,\ell,\delta)=\max\_{i\in[\ell]}\bigg(\big|\widehat{\Delta}\_{t,\ell}-\widehat{\Delta}\_{t,i}\big|-\big[\widehat{\psi}\left(t,\ell,\delta\right)+\widehat{\psi}\left(t,i,\delta\right)\big]\bigg)\_{+}. |  | (4.5) |

To interpret ϕ^\widehat{\phi}, in light of the bias-variance decomposition in ([4.2](https://arxiv.org/html/2512.23596v1#S4.E2 "Equation 4.2 ‣ Pairwise comparison subroutine. ‣ 4.1 Adaptive Tournament Model Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")), the quantity

|  |  |  |  |
| --- | --- | --- | --- |
|  | (|Δ^t,ℓ−Δ^t,i|−[ψ^​(t,ℓ,δ)+ψ^​(t,i,δ)])+\left(|\widehat{\Delta}\_{t,\ell}-\widehat{\Delta}\_{t,i}|-\big[\widehat{\psi}\left(t,\ell,\delta\right)+\widehat{\psi}\left(t,i,\delta\right)\big]\right)\_{+} |  | (4.6) |

can be viewed as a measure of the bias between the window ℓ\ell and a smaller window i≤ℓi\leq\ell, where subtracting ψ^​(t,ℓ,δ)\widehat{\psi}\left(t,\ell,\delta\right) and ψ^​(t,i,δ)\widehat{\psi}\left(t,i,\delta\right) eliminates the stochastic error and teases out the bias. The term ϕ^​(t,ℓ,δ)\widehat{\phi}(t,\ell,\delta) is then formed by taking the maximum of ([4.6](https://arxiv.org/html/2512.23596v1#S4.E6 "Equation 4.6 ‣ Pairwise comparison subroutine. ‣ 4.1 Adaptive Tournament Model Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")) over all smaller windows i∈[ℓ]i\in[\ell].

After constructing the bias and variance proxies, one chooses a window size ℓ^\widehat{\ell} that minimizes their sum:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ^=argminℓ∈[t−1]{ϕ^​(t,ℓ)+ψ^​(t,ℓ,δ)}.\widehat{\ell}=\mathop{\mathrm{argmin}}\_{\ell\in[t-1]}\left\{\widehat{\phi}(t,\ell)+\widehat{\psi}(t,\ell,\delta)\right\}. |  | (4.7) |

We then use Δ^t,ℓ^\widehat{\Delta}\_{t,\widehat{\ell}} as our estimate of Δt\Delta\_{t} for model comparison. In particular, the subroutine selects f1f\_{1} if and only if Δ^t,ℓ^≤0\widehat{\Delta}\_{t,\widehat{\ell}}\leq 0. The procedure is summarized in LABEL:sm:alg-compare.

Input: Candidate models {f1,f2}\{f\_{1},f\_{2}\}, validation data {𝒟jva}j=1t−1\{\mathcal{D}^{\operatorname{\mathrm{va}}}\_{j}\}\_{j=1}^{t-1}, hyperparameters δ′\delta^{\prime} and MM.

for ℓ=1,⋯,t−1\ell=1,\cdots,t-1

Compute Δ^t,ℓ\widehat{\Delta}\_{t,\ell}, ψ^​(t,ℓ,δ′)\widehat{\psi}(t,\ell,\delta^{\prime}) and ϕ^​(t,ℓ,δ′)\widehat{\phi}(t,\ell,\delta^{\prime}) according to ([4.1](https://arxiv.org/html/2512.23596v1#S4.E1 "Equation 4.1 ‣ Pairwise comparison subroutine. ‣ 4.1 Adaptive Tournament Model Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")), ([4.4](https://arxiv.org/html/2512.23596v1#S4.E4 "Equation 4.4 ‣ Pairwise comparison subroutine. ‣ 4.1 Adaptive Tournament Model Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")) and ([4.5](https://arxiv.org/html/2512.23596v1#S4.E5 "Equation 4.5 ‣ Pairwise comparison subroutine. ‣ 4.1 Adaptive Tournament Model Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")).

Choose window size

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ^∈argminℓ∈[t−1]{ϕ^​(t,ℓ,δ′)+ψ^​(t,ℓ,δ′)}.\widehat{\ell}\in\mathop{\mathrm{argmin}}\_{\ell\in[t-1]}\Big\{\widehat{\phi}(t,\ell,\delta^{\prime})+\widehat{\psi}(t,\ell,\delta^{\prime})\Big\}. |  | (4.8) |

Select λ^=1\widehat{\lambda}=1 if Δ^t,ℓ^≤0\widehat{\Delta}\_{t,\widehat{\ell}}\leq 0, and λ^=2\widehat{\lambda}=2 otherwise.

return f^=fλ^\widehat{f}=f\_{\widehat{\lambda}}.

Algorithm 2  Adaptive Rolling Window for Model Comparison

By using LABEL:sm:alg-compare as the model comparison subroutine in LABEL:sm:alg-tournament, we obtain an algorithm that adaptively uses chooses non-stationary data to perform model selection. We call the algorithm Adaptive Tournament Model Selection, or ATOMS in short.

### 4.2 Theoretical Guarantees

We now present the theoretical guarantees for our model selection framework. LABEL:sm:thm-model-comparison below establishes a performance bound for the pairwise model comparison subroutine (LABEL:sm:alg-compare).

###### Theorem 4.1 (Near-optimal model comparison).

Let Assumptions [2.1](https://arxiv.org/html/2512.23596v1#S2.Thmassumption1 "Assumption 2.1 (Independent data). ‣ 2 Problem Setup ‣ The nonstationarity-complexity tradeoff in return prediction") and [3.1](https://arxiv.org/html/2512.23596v1#S3.Thmassumption1 "Assumption 3.1 (Boundedness). ‣ 3.2 Theoretical Characterization ‣ 3 The Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction") hold. Choose δ∈(0,1)\delta\in(0,1) and take δ′=δ/(3​t)\delta^{\prime}=\delta/(3t) in LABEL:sm:alg-compare. With probability at least 1−δ1-\delta, the output f^\widehat{f} of LABEL:sm:alg-compare satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰt​(f^)≲min⁡{ℰt​(f1),ℰt​(f2)}+M2​log⁡(t/δ)⋅minℓ∈[t−1]⁡{maxt−ℓ≤j≤t−1⁡TV⁡(Pj,Pt)+1nt,ℓ}.\mathcal{E}\_{t}(\widehat{f})\lesssim\min\{\mathcal{E}\_{t}(f\_{1}),\mathcal{E}\_{t}(f\_{2})\}+M^{2}\log(t/\delta)\cdot\min\_{\ell\in[t-1]}\left\{\max\_{t-\ell\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})+\frac{1}{n\_{t,\ell}}\right\}. |  | (4.9) |

Here ≲\lesssim hides a universal constant.

###### Proof of LABEL:sm:thm-model-comparison.

See LABEL:sm:sec-thm-model-comparison-proof.
∎

LABEL:sm:thm-model-comparison gives a finite-sample oracle inequality ([4.9](https://arxiv.org/html/2512.23596v1#S4.E9 "Equation 4.9 ‣ Theorem 4.1 (Near-optimal model comparison). ‣ 4.2 Theoretical Guarantees ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")). It states that the excess risk of the f^\widehat{f} does not exceed that of the better model between f1f\_{1} and f2f\_{2}, plus an additional error term that reflects the difficulty of using the non-stationary data to make the comparison. Inside this additional term, the quantity

|  |  |  |
| --- | --- | --- |
|  | maxt−ℓ≤j≤t−1⁡TV⁡(Pj,Pt)+1nt,ℓ\max\_{t-\ell\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})+\frac{1}{n\_{t,\ell}} |  |

represents the two sources of errors that arise when using a validation window ℓ\ell to compare models, namely, the non-stationarity maxt−ℓ≤j≤t−1⁡TV⁡(Pj,Pt)\max\_{t-\ell\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t}) and the statistical uncertainty 1/nt,ℓ1/n\_{t,\ell} associated with the nt,ℓn\_{t,\ell} validation samples. The bound takes the minimum over all validation window sizes ℓ\ell, meaning that LABEL:sm:alg-compare performs almost as well as an oracle that knows in hindsight which validation window size ℓ\ell would lead to the most accurate comparison. This shows that LABEL:sm:alg-compare adaptively chooses a near-optimal validation window tailored to the local non-stationarity.

Building on this pairwise guarantee, LABEL:sm:thm-select-tournament below shows that our model selection algorithm ATOMS inherits the same oracle property when selecting from multiple candidate models {fλ}λ=1Λ\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda}.

###### Theorem 4.2 (Near-optimal model selection).

Let Assumptions [2.1](https://arxiv.org/html/2512.23596v1#S2.Thmassumption1 "Assumption 2.1 (Independent data). ‣ 2 Problem Setup ‣ The nonstationarity-complexity tradeoff in return prediction") and [3.1](https://arxiv.org/html/2512.23596v1#S3.Thmassumption1 "Assumption 3.1 (Boundedness). ‣ 3.2 Theoretical Characterization ‣ 3 The Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction") hold. Choose δ∈(0,1)\delta\in(0,1) and take δ′=δ/(3​Λ2​t)\delta^{\prime}=\delta/(3\Lambda^{2}t) in ATOMS. With probability at least 1−δ1-\delta, ATOMS outputs a model f^\widehat{f} satisfying

|  |  |  |
| --- | --- | --- |
|  | ℰt​(f^)≲minλ∈[Λ]⁡ℰt​(fλ)+M2​log⁡(Λ​t/δ)⋅minℓ∈[t−1]⁡{maxt−ℓ≤j≤t−1⁡TV⁡(Pj,Pt)+1nt,ℓ}.\mathcal{E}\_{t}(\widehat{f})\lesssim\min\_{\lambda\in[\Lambda]}\mathcal{E}\_{t}(f\_{\lambda})+M^{2}\log(\Lambda t/\delta)\cdot\min\_{\ell\in[t-1]}\left\{\max\_{t-\ell\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})+\frac{1}{n\_{t,\ell}}\right\}. |  |

Here ≲\lesssim hides a universal constant.

###### Proof of LABEL:sm:thm-select-tournament.

See LABEL:sm:sec-thm-select-tournament-proof.
∎

LABEL:sm:thm-select-tournament states that the excess risk of the model f^\widehat{f} chosen by the tournament is at most the excess risk of the best model in {fλ}λ=1Λ\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda}, up to an additional term that has the same form as in the pairwise comparison bound, with an extra O​(log⁡Λ)O(\log\Lambda) multiplicative factor. In other words, ATOMS identifies a model whose performance is nearly as good as the best candidate one could have selected in hindsight using the non-stationary validation data.

We remark that our model selection framework (LABEL:sm:alg-tournament) is general and can be combined with any model comparison subroutine 𝒜\mathcal{A}. In particular, in LABEL:sm:sec-thm-select-tournament-proof, we prove a general reduction lemma (LABEL:sm:lem-select-tournament-reduction) that converts any theoretical guarantee of the subroutine 𝒜\mathcal{A} to a guarantee of LABEL:sm:alg-tournament. In LABEL:sm:sec-select-R2, we further develop a R2R^{2}-based pairwise comparison subroutine that targets the R2R^{2} metric. When equipped with this R2R^{2}-based subroutine, LABEL:sm:alg-tournament enjoys a guarantee with respect to the R2R^{2} metric.

###### Remark 1 (Comparison with prior work).

Our model selection framework builds upon the model comparison method of HHW24. Below we briefly discuss the main differences between our work and theirs. First, their analysis of the model comparison procedure (LABEL:sm:alg-compare) assumes that the distribution of the covariates 𝐱\bm{x} remains fixed across time. Our theory removes this assumption entirely, and covers the general non-stationary setting where the joint data distribution (𝐱,y)(\bm{x},y) can change arbitrarily. Second, for model selection, they propose a single-elimination procedure which performs Λ−1\Lambda-1 model comparisons, but incurs additional factors (log⁡Λ)2(\log\Lambda)^{2} in the performance bound. In contrast, our approach maintains a linear complexity in Λ\Lambda in expectation while achieving a sharper bound.

### 4.3 Application to Joint Model Class and Training Window Size Selection

Finally, we apply LABEL:sm:thm-select-tournament to the joint selection of model class and training sample size.
Let ℱ\mathscr{F} be a finite collection of model classes, e.g., ℱ={linear model,random forest of a certain size}\mathscr{F}=\{\text{linear model},\text{random forest of a certain size}\}. For each model class ℱ∈ℱ\mathcal{F}\in\mathscr{F}, we train models on different windows k∈[t−1]k\in[t-1] of the training data {𝒟jtr}j=1t−1\{\mathcal{D}\_{j}^{\operatorname{\mathrm{tr}}}\}\_{j=1}^{t-1}. Let h^​(ℱ,k)\widehat{h}(\mathcal{F},k) denote the model from ℱ\mathcal{F} trained on {𝒟jtr}j=t−kt−1\{\mathcal{D}\_{j}^{\operatorname{\mathrm{tr}}}\}\_{j=t-k}^{t-1}. Then, the set of candidate models is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {fλ}λ=1Λ={h^​(ℱ,k):ℱ∈ℱ,k∈[t−1]}.\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda}=\left\{\widehat{h}(\mathcal{F},k):\mathcal{F}\in\mathscr{F},\,k\in[t-1]\right\}. |  | (4.10) |

Applying LABEL:sm:thm-select-tournament to this set of candidate models yields the following guarantee. For simplicity, we assume that training-validation data splitting ratio is fixed across time.

###### Assumption 4.1 (Balanced training-validation split).

There exists c>0c>0 such that |𝒟jtr|/|𝒟jva|=c|\mathcal{D}\_{j}^{\operatorname{\mathrm{tr}}}|/|\mathcal{D}\_{j}^{\operatorname{\mathrm{va}}}|=c for all j∈ℤ+j\in\mathbb{Z}\_{+}.

###### Theorem 4.3 (Near-optimal model-and-data selection).

Let Assumptions [2.1](https://arxiv.org/html/2512.23596v1#S2.Thmassumption1 "Assumption 2.1 (Independent data). ‣ 2 Problem Setup ‣ The nonstationarity-complexity tradeoff in return prediction"), [3.1](https://arxiv.org/html/2512.23596v1#S3.Thmassumption1 "Assumption 3.1 (Boundedness). ‣ 3.2 Theoretical Characterization ‣ 3 The Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction") and [4.1](https://arxiv.org/html/2512.23596v1#S4.Thmassumption1 "Assumption 4.1 (Balanced training-validation split). ‣ 4.3 Application to Joint Model Class and Training Window Size Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction") hold. Suppose the set of candidate models is given by ([4.10](https://arxiv.org/html/2512.23596v1#S4.E10 "Equation 4.10 ‣ 4.3 Application to Joint Model Class and Training Window Size Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")). Choose δ∈(0,1)\delta\in(0,1) and take δ′=δ/(6​|ℱ|2​t3)\delta^{\prime}=\delta/(6|\mathscr{F}|^{2}t^{3}) in ATOMS. Then, with probability at least 1−δ1-\delta, the output f^\widehat{f} of ATOMS satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰt​(f^)≲minℱ∈ℱ,k∈[t−1]⁡{minf∈ℱ⁡ℰt​(f)+(rt,k​(ℱ)+1Bt,k)+maxt−k≤j≤t−1⁡TV⁡(Pj,Pt)},\mathcal{E}\_{t}(\widehat{f})\lesssim\min\_{\mathcal{F}\in\mathscr{F},\,k\in[t-1]}\left\{\min\_{f\in\mathcal{F}}\mathcal{E}\_{t}(f)+\left(r\_{t,k}(\mathcal{F})+\frac{1}{B\_{t,k}}\right)+\max\_{t-k\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})\right\}, |  | (4.11) |

where Bt,k=∑j=t−kt−1(|𝒟jtr|+|𝒟jva|)B\_{t,k}=\sum\_{j=t-k}^{t-1}\left(|\mathcal{D}\_{j}^{\operatorname{\mathrm{tr}}}|+|\mathcal{D}\_{j}^{\operatorname{\mathrm{va}}}|\right) is the total sample size, and ≲\lesssim hides the constants MM and cc and logarithmic factors of tt, δ−1\delta^{-1} and |ℱ||\mathscr{F}|.

###### Proof of LABEL:sm:thm-joint-selection.

See LABEL:sm:sec-thm-joint-selection-proof.
∎

We note that the term

|  |  |  |
| --- | --- | --- |
|  | minf∈ℱ⁡ℰt​(f)+(rt,k​(ℱ)+1Bt,k)+maxt−k≤j≤t−1⁡TV⁡(Pj,Pt)\min\_{f\in\mathcal{F}}\mathcal{E}\_{t}(f)+\left(r\_{t,k}(\mathcal{F})+\frac{1}{B\_{t,k}}\right)+\max\_{t-k\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t}) |  |

on the right hand side of ([4.11](https://arxiv.org/html/2512.23596v1#S4.E11 "Equation 4.11 ‣ Theorem 4.3 (Near-optimal model-and-data selection). ‣ 4.3 Application to Joint Model Class and Training Window Size Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")) is exactly the model performance bound of the model h​(ℱ,k)h(\mathcal{F},k) in LABEL:sm:thm-tradeoff. Thus, our algorithm selects a near-optimal pair of model class and training window size, up to logarithmic factors.

## 5 Explaining the Cross-Section of Industry Portfolio Returns

In this section, we investigate whether our algorithm helps explain the cross-section of stock returns using industry portfolios as test assets. Rather than simply building predictive models, we approximate time-varying stochastic discount factors that capture the evolving relationship between risk and return. First, we describe our comprehensive dataset of firm-characteristic managed portfolios and industry portfolios. Then, we report our finding that our adaptive algorithm ATOMS achieves superior out-of-sample performance in explaining expected returns compared to fixed window and expanding window approaches across different economic regimes.

### 5.1 Data

We examine the pricing of 17 industry portfolio returns from Kenneth French’s data library, covering the period from September 1987 to November 2016. Our predictor set combines macroeconomic factors, risk premia from characteristic-sorted portfolios, and lagged returns to capture the complex dynamics driving industry returns, sourced for widely cited public datasets.888More specifically, our data combines daily and monthly sources to construct a comprehensive time series of covariates combining macroeconomic and cross-sectional signals. The final sample spans the time period from September 1987 to November 2016. We merge daily CRSP excess returns with monthly characteristics from GKX20, which provides 94 standardized characteristics for U.S. equities encompassing valuation ratios, profitability measures, investment activity, liquidity, and past return dynamics. These characteristics have become the canonical set of firm-level predictors in modern empirical asset pricing. We construct daily long-short portfolios by sorting firms into deciles based on each characteristic and taking the difference between the top and bottom decile returns, following the methodology of GKX20. We provide full details of the dataset construction in LABEL:sm:sec-dataapdx, including data preprocessing and long-short portfolio constructions.

##### Macroeconomic and Systematic Factors.

We incorporate 15 factors from CPZ24, who estimate a SDF using deep learning while imposing no-arbitrage restrictions. These factors include: (i) the estimated SDF representing the aggregate price of risk; (ii) ten beta-sorted decile portfolios based on firms’ SDF exposure; and (iii) four macroeconomic hidden states extracted from 178 macro time series via a generative adversarial network. These monthly observations are assigned to all trading days within each month. We also include the daily Fama-French three factors (market, size, and value) from FFr93 as benchmark risk factors.

##### Characteristic-Sorted Portfolios.

Following GKX20, we construct 94 long-short portfolios sorted on firm characteristics that capture price trends, liquidity, size, and risk measures. For each characteristic, we form decile portfolios using all CRSP-listed stocks and create a long-short strategy that buys the top decile and shorts the bottom decile. This approach transforms firm-level characteristics into interpretable factor returns that isolate the pricing implications of each characteristic.

##### Predictor Set.

Our final predictor set comprises: (i) 15 macroeconomic factors from CPZ24; (ii) 3 Fama-French factors; (iii) 94 characteristic-sorted long-short portfolio returns; and (iv) the 17 lagged industry returns. This comprehensive set combines traditional risk factors with modern high-dimensional representations, allowing us to test whether our adaptive asset pricing framework can effectively navigate the complex, time-varying relationships between these predictors and industry returns.

### 5.2 Return model

We evaluate our adaptive algorithm ATOMS using candidate models from different specifications with varying parameters and estimation windows. We take one month as a period, where the data 𝒟t={(𝒙t,i,yt,i)}i=1Bt\mathcal{D}\_{t}=\{(\bm{x}\_{t,i},y\_{t,i})\}\_{i=1}^{B\_{t}} in month tt consists of daily covariate-return pairs within that month.

##### Model Specifications.

We consider the following specifications that approximate stochastic discount factors. For a vector of covariates 𝒙∈ℝd\bm{x}\in\mathbb{R}^{d}, we write 𝒙~=(𝒙⊤,1)⊤∈ℝd+1\widetilde{\bm{x}}=(\bm{x}^{\top},1)^{\top}\in\mathbb{R}^{d+1}.

1. 1.

   Non-linear specification using random forests (RF). Given training data {(𝒙i,yi)}i=1n\{(\bm{x}\_{i},y\_{i})\}\_{i=1}^{n}, and two parameters, namely the number of trees ntreen\_{\texttt{tree}} and the maximum tree depth dmaxd\_{\max}, RF estimates a random forest model.
2. 2.

   Linear specification estimated with ridge regularization (Ridge). Given training data {(𝒙i,yi)}i=1n\{(\bm{x}\_{i},y\_{i})\}\_{i=1}^{n} and regularization parameter α>0\alpha>0, Ridge estimates a linear model f​(𝒙)=⟨𝜽^,𝒙~⟩f(\bm{x})=\langle\widehat{\bm{\theta}},\,\widetilde{\bm{x}}\rangle by

   |  |  |  |
   | --- | --- | --- |
   |  | 𝜽^=argmin𝜽∈ℝd+1{1n​∑i=1n(⟨𝜽,𝒙~i⟩−yi)2+α‖𝜽∥22}.\widehat{\bm{\theta}}=\mathop{\mathrm{argmin}}\_{\bm{\theta}\in\mathbb{R}^{d+1}}\left\{\frac{1}{n}\sum\_{i=1}^{n}\left(\langle\bm{\theta},\,\widetilde{\bm{x}}\_{i}\rangle-y\_{i}\right)^{2}+\alpha\|\bm{\theta}\|\_{2}^{2}\right\}. |  |
3. 3.

   Linear specification with LASSO regularization (LASSO). Given training data {(𝒙i,yi)}i=1n\{(\bm{x}\_{i},y\_{i})\}\_{i=1}^{n} and regularization parameter α>0\alpha>0, LASSO estimates a linear model f​(𝒙)=⟨𝜽^,𝒙~⟩f(\bm{x})=\langle\widehat{\bm{\theta}},\,\widetilde{\bm{x}}\rangle by

   |  |  |  |
   | --- | --- | --- |
   |  | 𝜽^=argmin𝜽∈ℝd+1{12⋅1n​∑i=1n(⟨𝜽,𝒙~i⟩−yi)2+α‖𝜽∥1}.\widehat{\bm{\theta}}=\mathop{\mathrm{argmin}}\_{\bm{\theta}\in\mathbb{R}^{d+1}}\left\{\frac{1}{2}\cdot\frac{1}{n}\sum\_{i=1}^{n}\left(\langle\bm{\theta},\,\widetilde{\bm{x}}\_{i}\rangle-y\_{i}\right)^{2}+\alpha\|\bm{\theta}\|\_{1}\right\}. |  |
4. 4.

   Linear specification with elastic net regularization (E-Net). Given training data {(𝒙i,yi)}i=1n\{(\bm{x}\_{i},y\_{i})\}\_{i=1}^{n} and regularization parameters α>0\alpha>0 and r∈(0,1)r\in(0,1), E-Net estimates a linear model f​(𝒙)=⟨𝜽^,𝒙~⟩f(\bm{x})=\langle\widehat{\bm{\theta}},\,\widetilde{\bm{x}}\rangle by

   |  |  |  |
   | --- | --- | --- |
   |  | 𝜽^=argmin𝜽∈ℝd+1{12⋅1n​∑i=1n(⟨𝜽,𝒙~i⟩−yi)2+α​r‖𝜽∥1+α2​(1−r)​‖𝜽‖22}.\widehat{\bm{\theta}}=\mathop{\mathrm{argmin}}\_{\bm{\theta}\in\mathbb{R}^{d+1}}\left\{\frac{1}{2}\cdot\frac{1}{n}\sum\_{i=1}^{n}\left(\langle\bm{\theta},\,\widetilde{\bm{x}}\_{i}\rangle-y\_{i}\right)^{2}+\alpha r\|\bm{\theta}\|\_{1}+\frac{\alpha}{2}(1-r)\|\bm{\theta}\|\_{2}^{2}\right\}. |  |

In each month tt, we estimate models from these specifications on estimation windows of 4k∧(t−1)4^{k}\wedge(t-1) months, where 0≤k≤50\leq k\leq 5. We detail the parameter choices for the specifications in LABEL:sm:sec-hyperparameters.

##### Benchmark Approaches.

To verify the adaptivity of our framework, we compare it with two non-adaptive benchmarks that use a fixed window for estimation and/or validation.

1. 1.

   Fixed validation window for specification selection (Fixed-val​(ℓ)\texttt{Fixed-val}(\ell)). This is the non-adaptive fixed-window counterpart of ATOMS. In each month tt, we estimate the same candidate specifications above, then use validation data from the last ℓ\ell periods {𝒟jva}j=t−ℓt−1\{\mathcal{D}\_{j}^{\operatorname{\mathrm{va}}}\}\_{j=t-\ell}^{t-1} to perform specification selection. The detailed description of Fixed-val​(ℓ)\texttt{Fixed-val}(\ell) is given in LABEL:sm:alg-fixed. We consider validation window sizes ℓ=32,128,512\ell=32,128,512 months, where ℓ=512\ell=512 corresponds to using all historical validation data at all times.
2. 2.

   Fixed-window cross-validation (Fixed-CV). In each month tt, we use data from the last 3636 months {𝒟j}j=t−36t−1\{\mathcal{D}\_{j}\}\_{j=t-36}^{t-1} to perform 55-fold cross-validation to estimate and select a specification out of the candidate specifications with the same sets of parameters.

We run each of these approaches over 2020 random splits of estimation and validation data. More details can be found in LABEL:sm:sec-hyperparameters.

Input: Candidate specifications {fλ}λ=1Λ\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda}, validation data {𝒟jva}j=1t−1\{\mathcal{D}^{\operatorname{\mathrm{va}}}\_{j}\}\_{j=1}^{t-1}, validation window size ℓ\ell.

Select

|  |  |  |
| --- | --- | --- |
|  | λ^=argminλ∈[Λ]∑j=(t−ℓ)∨1t−1∑i=1nj[fλ​(𝒙j,iva)−yj,iva]2.\widehat{\lambda}=\mathop{\mathrm{argmin}}\_{\lambda\in[\Lambda]}\sum\_{j=(t-\ell)\vee 1}^{t-1}\sum\_{i=1}^{n\_{j}}\left[f\_{\lambda}(\bm{x}^{\operatorname{\mathrm{va}}}\_{j,i})-y^{\operatorname{\mathrm{va}}}\_{j,i}\right]^{2}. |  |

return f^=fλ^\widehat{f}=f\_{\widehat{\lambda}}.

Algorithm 3  Fixed Validation Window for Specification Selection (Fixed-val​(ℓ)\texttt{Fixed-val}(\ell))

##### Performance Metrics.

We measure the performance of each approach using the out-of-sample R2R^{2} metric ([2.2](https://arxiv.org/html/2512.23596v1#S2.E2 "Equation 2.2 ‣ 2 Problem Setup ‣ The nonstationarity-complexity tradeoff in return prediction")) that benchmarks against a zero forecast. We compute both the overall out-of-sample R2R^{2} from January 1990 to November 2016, and the annual out-of-sample R2R^{2}. The latter provides a more granular understanding of the approaches’ performance over time. In LABEL:sm:sec-experiments-standard-R2, we also report results for the standard R2R^{2} metric ([2.3](https://arxiv.org/html/2512.23596v1#S2.E3 "Equation 2.3 ‣ 2 Problem Setup ‣ The nonstationarity-complexity tradeoff in return prediction")).

### 5.3 Empirical Results: 17 Industry Portfolios

We next turn to the empirical analysis of pricing the 17 industry portfolios. The fundamental premise of our adaptive framework is that asset pricing relationships exhibit time-varying dynamics rather than remaining stationary across economic conditions. This non-stationarity is particularly pronounced during economic recessions, when structural breaks in risk premia, sudden shifts in investor risk aversion, and disruptions to market liquidity mechanisms create environments where long-term historical pricing relationships provide poor guidance for future returns. Recessions therefore serve as a natural laboratory for testing the adaptivity of our framework: if our approach can successfully navigate these turbulent periods when non-stationarity is most severe, it provides compelling evidence for the value of adaptive model selection in asset pricing more generally.

##### Recession Performance Analysis.

Our most striking empirical finding relates to the differential performance of ATOMS during economic downturns. LABEL:sm:tab:oos\_r2\_industry\_time presents out-of-sample R2R^{2} values across distinct economic regimes, revealing that ATOMS exhibits particular strength during recessionary periods when market dynamics are most volatile and traditional models typically fail. The adaptive framework achieves an out-of-sample R2R^{2} of 0.049 across the full sample period, representing a 14.0% improvement over the best fixed-window benchmark Fixed-val​(512)\texttt{Fixed-val}(512) which has R2=0.043R^{2}=0.043.

Table 2: Out-of-Sample R2R^{2} Averages Across Industries by Time Period

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Method | Full OOS Period | Recessions | | |
| Gulf War | 2001 Recession | Financial Crisis |
| ATOMS | 0.0490.049 | 0.0270.027 | 0.1250.125 | 0.0410.041 |
| Fixed-val​(32)\texttt{Fixed-val}(32) | 0.0220.022 | 0.0090.009 | 0.0960.096 | −0.001-0.001 |
| Fixed-val​(512)\texttt{Fixed-val}(512) | 0.0430.043 | −0.031-0.031 | 0.1170.117 | 0.0390.039 |
| Fixed-CV | 0.0350.035 | −0.007-0.007 | 0.0710.071 | 0.0140.014 |

This table reports out-of-sample (OOS) R2R^{2} averages for return prediction models across all 17 industry portfolios. Full OOS Period refers our largest available OOS period covering 01/1990∼\sim11/2016. Columns report OOS R2R^{2} averages across all industries and highlight this metric during three recessions, as documented in [NBER Business Cycle Dating](https://www.nber.org/research/business-cycle-dating):

* •

  the 1990 Gulf War recession (06/1990∼\sim10/1990);
* •

  the 2001 Recession of dot-com bubble burst and the 9/11 attack (05/2001∼\sim10/2001);
* •

  the Financial Crisis led by defaults of subprime mortgages (11/2007∼\sim06/2009).

That is, the OOS performance in Gulf War column focuses on model performance comparisons exclusively in the out-of-sample period of 06/1990∼\sim10/1990. All values are calculated using monthly return data.

During the 2001 recession, characterized by the dot-com bubble collapse and the September 11 terrorist attacks, ATOMS achieves an impressive R2R^{2} of 0.125, outperforming Fixed-val​(512)\texttt{Fixed-val}(512) by 6.8% (0.117) and substantially exceeding Fixed-CV’s 0.071. This superior performance suggests that our adaptive framework effectively captures the rapid regime shifts that occurred during this period, when technology-related stocks experienced dramatic revaluation and risk premia underwent fundamental restructuring.

The 1990 Gulf War recession provides particularly compelling evidence of our framework’s adaptability. While ATOMS maintains a positive R2R^{2} of 0.0270.027 during this sharp but brief contraction, the fixed-window benchmark Fixed-val​(512)\texttt{Fixed-val}(512) produces a negative R2R^{2} of −0.031-0.031, indicating worse performance than a simple forecast of zero. This divergence highlights the critical importance of adaptivity during periods of sudden market stress, when historical relationships between risk factors and returns break down most severely. The adaptive framework’s ability to rapidly adjust its validation window allows it to recognize and respond to the changing market dynamics that fixed-window models miss entirely.

During the Global Financial Crisis of 2007-2009, ATOMS achieves an R2R^{2} of 0.041, marginally outperforming Fixed-val​(512)\texttt{Fixed-val}(512) (0.039) and substantially exceeding Fixed-CV (0.014). The relatively smaller performance gap during this period is primarily driven by the fact that NBER defines the Financial Crisis-related recession with a much longer period that spans from 2007 to 2009, where eventually new data observed in the recession itself could be factored into training and validation for our benchmarked model that uses fixed look-back horizon. In other words, the long duration of this recession attenuates the advantages of our method. Nevertheless, ATOMS maintained its advantage throughout this long period, demonstrating robustness across different types of economic contractions.

Figure 4: Box Plot of Out-of-Sample R2R^{2} of ATOMS and Fixed-Window Baselines for 1717 Industry Portfolios.

![Refer to caption](x20.png)


This figure describes the distribution of each method’s OOS R2R^{2}. Each box corresponds to all industries and all years in our OOS horizon.




Figure 5: Annual Out-of-Sample R2R^{2} of ATOMS and Fixed-Window Baselines for 1717 Industry Portfolios.

![Refer to caption]()

![Refer to caption](x22.png)

![Refer to caption](x23.png)

![Refer to caption](x24.png)

![Refer to caption](x25.png)

![Refer to caption](x26.png)

![Refer to caption](x27.png)

![Refer to caption](x28.png)

![Refer to caption](x29.png)

![Refer to caption](x30.png)

![Refer to caption](x31.png)

![Refer to caption](x32.png)

![Refer to caption](x33.png)

![Refer to caption](x34.png)

![Refer to caption](x35.png)

![Refer to caption](x36.png)

![Refer to caption](x37.png)

This figure reports the annual out-of-sample R2R^{2} of our adaptive model selection algorithm ATOMS (black dashed line with ×\times’s), as well as the fixed-window baselines Fixed-val​(32)\texttt{Fixed-val}(32) (blue ▼\blacktriangledown’s), Fixed-val​(128)\texttt{Fixed-val}(128) (orange ■\blacksquare’s), and Fixed-val​(512)\texttt{Fixed-val}(512) (red), which use the last 3232, last 128128 and all months of validation data. The title in each subfigure is Kenneth French’s acronym for each industry. For the full names of these industries, please refer to Table [4](https://arxiv.org/html/2512.23596v1#A1.T4 "Table 4 ‣ A.2 Figures and tables ‣ Appendix A Additional details for empirical asset pricing ‣ The nonstationarity-complexity tradeoff in return prediction").

##### Economic Interpretation.

The superior recession performance of ATOMS has important implications for asset pricing theory and practice. Traditional asset pricing models assume stationary risk-return relationships, an assumption that becomes particularly problematic during economic downturns when risk aversion typically increases and market liquidity conditions deteriorate. Our adaptive framework explicitly recognizes this non-stationarity by allowing the validation window to expand or contract based on recent predictive performance.

The empirical evidence suggests that during recessions, the optimal window for model selection shrinks significantly, reflecting the rapid evolution of risk premia. The 1990 Gulf War recession provides the clearest example: its sudden onset and brief duration created an environment where only models with very recent validation data could accurately capture the new pricing dynamics. Conversely, during more prolonged downturns like the Global Financial Crisis, the optimal window likely expanded gradually as new market conditions became established.

From a theoretical perspective, these findings support the view that stochastic discount factors exhibit time-varying dynamics that are particularly pronounced during economic stress. The adaptive framework’s ability to track these dynamics more effectively than fixed-window approaches suggests that the non-stationarity of asset pricing relationships is not merely a statistical artifact but reflects fundamental economic mechanisms that vary with the business cycle.

##### Robustness Across Industries.

We conduct industry-by-industry robustness check to confirm that the recession outperformance of ATOMS is not driven by a subset of industries but represents a broad-based phenomenon. Firstly, we report in Figure [4](https://arxiv.org/html/2512.23596v1#S5.F4 "Figure 4 ‣ Recession Performance Analysis. ‣ 5.3 Empirical Results: 17 Industry Portfolios ‣ 5 Explaining the Cross-Section of Industry Portfolio Returns ‣ The nonstationarity-complexity tradeoff in return prediction") that ATOMS overall has better R2R^{2} across all years, as its median, and level position of the box is higher than those of the other methods.

In more details, LABEL:sm:fig-industry-yearly plots the annual out-of-sample R2R^{2} of ATOMS and the baselines in each industry. We observe that ATOMS maintains its advantage across diverse sectors including cyclical industries (Durbl, Cars, Trans) and defensive sectors (Food, Utils, Cnsum). This cross-sectional consistency strengthens our confidence that the observed performance reflects genuine adaptivity to changing market conditions rather than industry-specific anomalies.

Notably, the adaptive algorithm shows particular strength in industries most sensitive to business cycle fluctuations, such as durable goods (Durbl), consumer discretionary (Rtail), and financial services (Finan). This pattern aligns with economic intuition, as these sectors experience the most dramatic shifts in risk premia during economic transitions. Our method’s ability to capture these dynamics more effectively than benchmarks suggests it successfully identifies the changing risk-return tradeoffs that characterize different phases of the business cycle.

### 5.4 Trading Strategies

To assess the economic significance of our asset pricing framework, we implement trading strategies based on its return predictions and evaluate wealth accumulation—this tests whether the documented predictive power translates into economic value for investors.

Our trading protocol is standard: we start with initial wealth W0=1W\_{0}=1. At the beginning of each month tt, the model yields a predicted return f^t\hat{f}\_{t}. We trade based on the sign of this predicted return. That is, on each trading day i∈[Bt]i\in[B\_{t}] of month tt, we trade according to the sign of the predicted return f^t​(𝐱t,i)\hat{f}\_{t}(\mathbf{x}\_{t,i}): we take a long position if f^t​(𝐱t,i)>0\hat{f}\_{t}(\mathbf{x}\_{t,i})>0, and a short position otherwise. Consequently, the portfolio wealth evolves according to the realized daily returns yt,iy\_{t,i}, adjusted by the position direction. The cumulative wealth WtW\_{t} at the end of month tt is given by:

|  |  |  |
| --- | --- | --- |
|  | Wt=Wt−1​∏i=1Bt(1+yt,i⋅sign​(f^t​(𝒙t,i))).W\_{t}=W\_{t-1}\prod\_{i=1}^{B\_{t}}\left(1+y\_{t,i}\cdot\textrm{sign}\big(\widehat{f}\_{t}(\bm{x}\_{t,i})\big)\right). |  |

Iterating this process, the final wealth WTW\_{T} at time TT is

|  |  |  |
| --- | --- | --- |
|  | WT=W0​∏t=1T∏i=1Bt(1+yt,i⋅sign​(f^t​(𝒙t,i))).W\_{T}=W\_{0}\prod\_{t=1}^{T}\prod\_{i=1}^{B\_{t}}\left(1+y\_{t,i}\cdot\textrm{sign}\big(\widehat{f}\_{t}(\bm{x}\_{t,i})\big)\right). |  |

Figure 6: Cumulative Wealth Curve of ATOMS and Baselines for 1717 Industry Portfolios.

![Refer to caption](x38.png)

![Refer to caption](x39.png)

![Refer to caption](x40.png)

![Refer to caption](x41.png)

![Refer to caption](x42.png)

![Refer to caption](x43.png)

![Refer to caption](x44.png)

![Refer to caption](x45.png)

![Refer to caption](x46.png)

![Refer to caption](x47.png)

![Refer to caption](x48.png)

![Refer to caption](x49.png)

![Refer to caption](x50.png)

![Refer to caption](x51.png)

![Refer to caption](x52.png)

![Refer to caption](x53.png)

![Refer to caption](x54.png)

This figure reports the cumulative wealth (in log scale) of trading strategies based on predictions from our adaptive algorithm ATOMS (black line), as well as the fixed-window baselines Fixed-val​(32)\texttt{Fixed-val}(32) (blue), Fixed-val​(128)\texttt{Fixed-val}(128) (orange), Fixed-val​(512)\texttt{Fixed-val}(512) (red), and Fixed-CV (gray dashed line). For most industries, our algorithm ATOMS consistently attains more cumulative wealth than the fixed-window baselines. The title in each subfigure is Kenneth French’s acronym for each industry. For the full names of these industries, please refer to Table [4](https://arxiv.org/html/2512.23596v1#A1.T4 "Table 4 ‣ A.2 Figures and tables ‣ Appendix A Additional details for empirical asset pricing ‣ The nonstationarity-complexity tradeoff in return prediction").

Our investment starts in January 1990 as the first month t=1t=1, and ends in November 2016. We generate wealth trajectories {Wtalg}t=1T\big\{W\_{t}^{\texttt{alg}}\big\}\_{t=1}^{T} for our algorithm and the fixed-window baselines alg∈{ATOMS,Fixed-val​(ℓ),Fixed-CV}\texttt{alg}\in\{\texttt{ATOMS},\,\texttt{Fixed-val}(\ell),\,\texttt{Fixed-CV}\}.

LABEL:sm:fig-industry-wealth-yearly depicts the evolution of the log cumulative wealth log⁡Wtalg\log W\_{t}^{\texttt{alg}} for each method at the end of each year from 1990 to 2016. We observe that for most industries, the adaptive algorithm ATOMS consistently yields higher cumulative wealth than the fixed-window baselines, surpassing both the short and long validation windows. This superior performance highlights the algorithm’s capacity to generate substantial excess returns by balancing the trade-off between non-stationarity and model complexity.

To further quantify the performance gain across the 1717 industries, we compute an Excess Ratio of WTATOMS/WTalg−1W\_{T}^{\texttt{ATOMS}}/W\_{T}^{\texttt{alg}}-1 against any baseline alg∈{Fixed-val​(ℓ),Fixed-CV}\texttt{alg}\in\{\texttt{Fixed-val}(\ell),\texttt{Fixed-CV}\}, and take its average across all 17 industries. This simple arithmetic average can be considered as an equal-weighted portfolio that invests 1/171/17th initial wealth in each of the industries. A value greater than zero indicates that our adaptive method ATOMS accumulates higher terminal wealth than the benchmark alg. In LABEL:sm:tab-cumwealth, we report the average Excess Ratio over the 1717 industries. The positive values of Excess Ratio indicate that ATOMS consistently generates superior wealth accumulation compared to the fixed-window benchmarks for the equal-weighted portfolio of industries. Compared with the best-performing benchmark of long horizon validation Fixed-val​(512)\texttt{Fixed-val}(512), our method yields 31% higher return for its investor by the end of our OOS period. With weaker benchmarked methods such as model picked by Fixed-CV that uses cross-validation, our method obtains 3.54 times more wealth over the investment horizon of 1990 to 2016.

Table 3: Average Cumulative Wealth Relative Excess of ATOMS over Baselines.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Baseline Model | Fixed-val​(32)\texttt{Fixed-val}(32) | Fixed-val​(128)\texttt{Fixed-val}(128) | Fixed-val​(512)\texttt{Fixed-val}(512) | Fixed-CV |
| Excess Ratio | 3.383.38 | 0.480.48 | 0.310.31 | 3.543.54 |

This table reports the Excess Ratio. For each industry, we compute an Excess Ratio, then report average across the 17 computed industries. This metric can also be considered as the Excess Ratio if we were to invest in an equal-weighted portfolio that allocates evenly among all 17 industries in the initial period.

## 6 Conclusions

Our empirical results demonstrate the practical value of this framework across multiple dimensions. Most notably, during periods of heightened economic stress, our adaptive method ATOMS exhibits superior performance compared to fixed-window approaches. Our approach is well motivated by the documented facts in LABEL:sm:sec-tradeoff-empirics that, during recession periods including the 1990 Gulf War recession, the 2001 dot-com bubble burst and 9/11 attack, and the 2007-2009 Financial Crisis, simpler models trained on shorter windows consistently outperformed more complex models trained on longer windows. This empirical evidence validates our theory of the nonstationarity-complexity tradeoff.

The adaptive algorithm’s performance during economic downturns is worth pointing out. As shown in LABEL:sm:tab:oos\_r2\_industry\_time, ATOMS achieves an out-of-sample R2R^{2} of 0.0270.027 during the brief but severe 1990 Gulf War recession, while the best fixed-window benchmark Fixed-val​(512)\texttt{Fixed-val}(512) produces a negative R2R^{2} of −0.031-0.031. During the 2001 recession, ATOMS attains an impressive R2R^{2} of 0.1250.125, outperforming Fixed-val​(512)\texttt{Fixed-val}(512) by 6.8% (0.117). Even during the prolonged Global Financial Crisis of 2007-2009, ATOMS maintains its advantage with an R2R^{2} of 0.0410.041 compared to Fixed-val​(512)\texttt{Fixed-val}(512)’s 0.0390.039. Beyond statistical performance metrics, the economic significance of our approach is demonstrated through trading strategy analysis. Averaged across the industries, our model yields 31% higher return than the best performing benchmark in the OOS period.

Several future directions are worth exploring. First, our adaptive model selection framework relies on the assumption that data is independent across time even though the distribution can change arbitrarily. While numerical experiments show that our method is robust against temporal dependence in real-world financial time series, it would be interesting and important to extend the framework in a principled way. Second, our framework of joint model and training window selection requires training a large number of candidate models, which can be computationally intensive. A valuable future direction is to reduce the these training costs. For example, a heuristic approach is to utilize the optimized parameters from previous periods as “warm starts” for subsequent training.

## Acknowledgement

Agostino Capponi’s research was supported in part through grants of the Global Risk Institute and of Fi-Tek.
Chengpiao Huang and Kaizheng Wang’s research is supported by National Science Foundation grants DMS-2210907 and DMS-2515679.

Appendix

## Appendix A Additional details for empirical asset pricing

In this section, we provide additional details for the numerical experiments in LABEL:sm:sec-experiments.

### A.1 Data

We aim to explain the cross-section of 1717 industry portfolio returns from Kenneth French’s website999<https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_17_ind_port.html>. We first describe our rich set of covariates, which combines daily and monthly sources to construct a comprehensive time series combining macroeconomic and cross-sectional signals. The final daily-frequency sample spans the time period from September 1987 to November 2016.

##### Common Factors.

To capture the underlying macroeconomic and systematic risk structure in our response variables, we include 15 common factors from the monthly dataset of CPZ24, who develop a deep learning framework for estimating the stochastic discount factor (SDF) consistent with the no-arbitrage condition.101010Their model integrates three neural network components: a feedforward network to approximate the nonlinear functional form of the SDF, a recurrent Long-Short Term Memory (LSTM) network to extract macroeconomic state variables, and a generative adversarial network (GAN) that constructs the most informative test assets for pricing. This architecture yields an empirically estimated SDF that represents the conditional mean-variance efficient portfolio of all U.S. equities.

The CPZ24 dataset provides three distinct elements relevant to our analysis:
(i) the estimated stochastic discount factor (SDF), capturing the aggregate price of risk implied by their no-arbitrage model;
(ii) the returns of ten equal-weighted decile portfolios sorted by firms’ exposure to the SDF (beta-sorted), which serve as cross-sectional test assets; and
(iii) four macroeconomic hidden state variables, derived from the GAN model, that summarize the joint dynamics of 178 macroeconomic time series into a small set of nonlinear factors reflecting business cycle conditions and systemic risk.111111These components jointly span the main drivers of systematic variation in expected returns. The SDF and beta-sorted deciles capture the cross-sectional risk-return trade-offs, while the macroeconomic hidden states track time variation in the pricing kernel associated with expansions, recessions, and crisis periods. The dataset covers the period 1967-2016; to align frequencies with our daily response data, each monthly observation is assigned to all trading days within the corresponding month.

In addition to these 15 factors, we incorporate the daily Fama-French three factors (FF3) from FFr93, which include the excess market return (MKT), the size factor (SMB), and the value factor (HML). These factors provide a benchmark set of linear risk exposures that have been shown to explain broad cross-sectional patterns in stock returns. Each factor is lagged appropriately to avoid look-ahead bias.

This unified set of common factors allows us to incorporate both the traditional linear risk structure captured by FF3 and the nonlinear, macroeconomically conditioned dynamics extracted from CPZ24.

##### Firm-Level Returns and Characteristics.

We augment the dataset with daily firm-level stock returns obtained from the CRSP database. Excess returns are computed relative to the daily risk-free rate from Kenneth French’s data library.121212To mitigate the impact of outliers that can distort cross-sectional averages, we Winsorize the daily cross-section of excess returns by removing the top and bottom 1% of firms within each day based on their excess return values. This procedure ensures that the resulting portfolio and factor constructions are not unduly influenced by extreme realizations. To characterize the cross-sectional heterogeneity in firm fundamentals and trading behavior, we incorporate the comprehensive panel of firm-level characteristics from GKX20. Their dataset provides 94 standardized monthly characteristics for U.S. equities, constructed to ensure comparability across firms and over time.

Specifically, GKX20 identify three dominant groups of predictive signals: (i) Price trend variables: measures of short- and long-term momentum, industry momentum, and short-term reversal that capture the persistence of returns and investor underreaction; (ii) Liquidity and size variables: market capitalization, trading volume, turnover, and bid-ask spread, which reflect trading frictions and the limits to arbitrage; (iii) Volatility and risk variables: total and idiosyncratic volatility, market beta, and higher-order terms such as beta squared, which proxy for systematic and residual risk exposure.131313Because the GKX20 characteristics are available only at a monthly frequency, we assign each monthly vector of characteristics to all trading days within that month for the corresponding firm. This alignment ensures consistency between the daily CRSP return data and the lower-frequency fundamental information.

#### A.1.1 Size Filter

We apply a size-based filter to focus the analysis on the subset of firms that are most representative of the small-cap universe. Specifically, within each day tt, we retain only the bottom 25% of firms by market equity.141414We measure market equity with the (monthly) “mvel1” size covariate from GKX20, this variable represents the firm’s market capitalization at the end of month mm, standardized for comparability across firms and time.

Formally, let Si,mS\_{i,m} denote the size of firm ii in month mm. For all trading days tt belonging to month mm, we retain only those firms satisfying

|  |  |  |
| --- | --- | --- |
|  | Si,m≤Q0.25​({Sj,m}j∈ℱm),S\_{i,m}\leq Q\_{0.25}\big(\{S\_{j,m}\}\_{j\in\mathcal{F}\_{m}}\big), |  |

where Q0.25​(⋅)Q\_{0.25}(\cdot) denotes the 25th percentile of the cross-sectional size distribution, and ℱm\mathcal{F}\_{m} is the set of all firms available in month mm. Restricting the sample in this way allows us to study the predictive role of firm characteristics and macroeconomic factors within a homogeneous segment of the equity market, mitigating heterogeneity arising from scale effects in firm size.

#### A.1.2 Long-Short Decile Portfolios from Characteristics

To transform the firm-level characteristics into tradable, interpretable covariates, we construct daily long-short portfolios sorted on each of the GKX20 characteristics. For each of the 94 characteristics, denoted by c∈{1,…,94}c\in\{1,\dots,94\}, and for each day tt, we sort firms into ten equal-weighted portfolios based on the value of characteristic cc.

Formally, let Xi,c,mX\_{i,c,m} denote the value of characteristic cc for firm ii in month mm, which is assigned to all trading days within that month, and let Ri,texR\_{i,t}^{\text{ex}} denote the daily excess return of firm ii on day tt. We compute monthly breakpoints for characteristic cc using cross-sectional quantiles:

|  |  |  |
| --- | --- | --- |
|  | bc,k,m=Qk/10​({Xi,c,m}i∈ℱt),k=1,…,10,b\_{c,k,m}=Q\_{k/10}\big(\{X\_{i,c,m}\}\_{i\in\mathcal{F}\_{t}}\big),\quad k=1,\dots,10, |  |

where Qp​(⋅)Q\_{p}(\cdot) denotes the pp-th empirical quantile, and ℱt\mathcal{F}\_{t} is the set of all firms observed in day tt.

We then compute the daily return of the kk-th decile portfolio for characteristic cc as:

|  |  |  |
| --- | --- | --- |
|  | Dc,k,t=1Nc,k,t​∑i:bc,k−1,m<Xi,c,m≤bc,k,mRi,tex,D\_{c,k,t}=\frac{1}{N\_{c,k,t}}\sum\_{i:\,b\_{c,k-1,m}<X\_{i,c,m}\leq b\_{c,k,m}}R\_{i,t}^{\text{ex}}, |  |

where Nc,k,tN\_{c,k,t} is the number of firms assigned to the kk-th decile at time tt. Each decile is equal-weighted to ensure that portfolio performance reflects cross-sectional variation in firm characteristics rather than differences in market capitalization.

The corresponding long-short portfolio return for characteristic cc is defined as:

|  |  |  |
| --- | --- | --- |
|  | LSc,t=Dc,10,t−Dc,1,t,\text{LS}\_{c,t}=D\_{c,10,t}-D\_{c,1,t}, |  |

representing the daily return to a strategy that is long the highest-decile firms (those with the largest values of Xi,c,mX\_{i,c,m}) and short the lowest-decile firms (those with the smallest values of Xi,c,mX\_{i,c,m}).

This construction yields a balanced set of long-short factor returns that isolate the pricing implications of each firm characteristic. Repeating this procedure for all c∈{1,…,94}c\in\{1,\dots,94\} produces a time series matrix of 94 characteristic-sorted long-short portfolio returns at the daily frequency.

#### A.1.3 Final Covariate Set

Our final set of predictors integrates macroeconomic, factor-based, and cross-sectional sources of variation to form a unified time series of covariates for forecasting the Russell 2000 index and the French 17 industry portfolio returns. The resulting dataset combines information from three complementary dimensions of the asset pricing literature:

1. 1.

   Macroeconomic and systematic factors: the 10 equal-weighted beta-sorted decile portfolios, the 4 macroeconomic hidden states, and the estimated stochastic discount factor (SDF) from CPZ24.
2. 2.

   Benchmark risk factors: the daily Fama-French 3 factors (FF3) from FFr93, consisting of the market excess return (MKT), the size factor (SMB), and the value factor (HML).
3. 3.

   Cross-sectional characteristic factors: the 94 daily long-short characteristic-sorted portfolio returns, from the GKX20 characteristics.
4. 4.

   Lagging features: we augment the feature set with one-day lagged returns. For the prediction of the Russell 2000 index return, we use the index’s own lag. For the prediction of the 1717 industry portfolio returns, we use the full vector of the 1717 industry portfolio lagged returns.

By combining the first three components, our dataset links the macroeconomic and cross-sectional perspectives on asset pricing. The CPZ24 factors embed the nonlinear, time-varying structure of the stochastic discount factor, while the GKX20 characteristic-sorted long-short portfolios summarize the cross-sectional distribution of risk premia across firms. Incorporating the Fama-French 3 factors provides a benchmark for evaluating whether these modern, high-dimensional representations offer predictive power beyond the traditional linear framework.

### A.2 Figures and tables

Table 4: Name Mapping for the 17 Industries

|  |  |
| --- | --- |
| Industry Acronym | Full Industry Name |
| Food | Food |
| Mines | Mining and Minerals |
| Oil | Oil and Petroleum Products |
| Clths | Textiles, Apparel & Footwear |
| Durbl | Consumer Durables |
| Chems | Chemicals |
| Cnsum | Drugs, Soap, Perfumes, Tobacco |
| Cnstr | Construction and Construction Materials |
| Steel | Steel Works Etc |
| FabPr | Fabricated Products |
| Machn | Machinery and Business Equipment |
| Cars | Automobiles |
| Trans | Transportation |
| Utils | Utilities |
| Rtail | Retail Stores |
| Finan | Banks, Insurance Companies, and Other Financials |
| Other | Other |

### A.3 Machine learning model implementation details

In this appendix, we provide detailed specifications for the hyperparameter tuning procedures and training configurations used in our empirical analysis. These technical details complement the main text by offering comprehensive information about the model selection process and computational implementation.

#### A.3.1 Model Hyperparameter Grids

For each model class considered in our analysis, we systematically explore a comprehensive grid of hyperparameter values for model selection. The hyperparameter grids are designed to balance computational efficiency with thorough exploration of the model space.

##### Linear Models with Regularization.

For the ridge regression (Ridge), LASSO (LASSO), and elastic net (E-Net) models, we consider the following hyperparameter specifications:

1. 1.

   For ridge regression, we consider values of the regularization parameter α\alpha on a logarithmic scale:

   |  |  |  |
   | --- | --- | --- |
   |  | α∈{10−3,10−1.5,1,101.5,103}.\alpha\in\{10^{-3},10^{-1.5},1,10^{1.5},10^{3}\}. |  |

   This range allows for both strong regularization (small α\alpha) and weak regularization (large α\alpha), accommodating different levels of multicollinearity in our high-dimensional covariate space.
2. 2.

   For LASSO, we consider values of the regularization parameter α\alpha on a lagoarithmic scale:

   |  |  |  |
   | --- | --- | --- |
   |  | α∈{10−5,10−3.5,10−2,10−0.5,10}.\alpha\in\{10^{-5},10^{-3.5},10^{-2},10^{-0.5},10\}. |  |

   The ℓ1\ell\_{1} penalty in LASSO facilitates feature selection, which is particularly valuable given our large set of covariates.
3. 3.

   For the elastic net, we consider the following combinations of the regularization parameter α\alpha and the mixing parameter rr:

   |  |  |  |
   | --- | --- | --- |
   |  | α∈{10−3,1,103},r∈{0.01,0.05,0.1}.\alpha\in\{10^{-3},1,10^{3}\},\qquad r\in\{0.01,0.05,0.1\}. |  |

   This grid explores the balance between feature selection and coefficient shrinkage.

##### Random Forest.

For the random forest models, we consider the following combinations of the number of trees ntreen\_{\texttt{tree}} and the maximum tree depth dmaxd\_{\max}:

|  |  |  |
| --- | --- | --- |
|  | ntree∈{10,100,200},dmax∈{3,5,10}.n\_{\texttt{tree}}\in\{10,100,200\},\qquad d\_{\max}\in\{3,5,10\}. |  |

Increasing the number of trees generally improves model stability and reduces variance, though with diminishing returns beyond a certain point. Trees with shallower depths provide stronger regularization, while deeper trees can capture more complex nonlinear relationships.

#### A.3.2 Training Window Configurations

To assess the performance of our adaptive model selection algorithm across different data regimes, we train models on estimation windows of varying lengths. For each month tt, we consider training windows of 4k∧(t−1)4^{k}\wedge(t-1) months with 0≤k≤50\leq k\leq 5. In particular, since t∈{1,…,350}t\in\{1,...,350\}, then k=5k=5 corresponds to a full training window of (t−1)(t-1) months. This yields the following window lengths:

Table 5: Training Window Lengths by Value of kk

|  |  |  |
| --- | --- | --- |
| kk | Window Length (months) | Approximate Years |
| 0 | 1 | 0.08 |
| 1 | 4 | 0.33 |
| 2 | 16 | 1.33 |
| 3 | 64 | 5.33 |
| 4 | 256 | 21.33 |
| 5 | t−1t-1 | (t−1)/12(t-1)/12 |

This exponential scaling allows us to examine how model performance varies with the amount of historical data available for training. Shorter windows capture recent market dynamics but may be susceptible to noise, while longer windows provide more stable parameter estimates but may miss structural changes in the data-generating process.

#### A.3.3 Hyperparameter for ATOMS

In our implementation of ATOMS, we set δ′=0.1\delta^{\prime}=0.1 and M2=5×10−4M^{2}=5\times 10^{-4}.

#### A.3.4 Computational Implementation

All models are implemented using Python 3.9 with the following libraries:

* •

  Linear models: scikit-learn version 1.0.2, specifically Ridge, Lasso, and ElasticNet.
* •

  Random forest: scikit-learn’s RandomForestRegressor with random\_state=0.
* •

  Data manipulation: pandas version 1.4.2 and numpy version 1.21.5.

## Appendix B Extension: Model Selection with the R2R^{2} Metric

In this section, we propose a variant of our model selection method that is tailored to the R2R^{2} metric. We consider the following population form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R~t2​(f)=1−𝔼(𝒙,y)∼Pt​[(f​(𝒙)−y)2]𝔼(𝒙,y)∼Pt​[y2],\widetilde{R}^{2}\_{t}(f)=1-\frac{\mathbb{E}\_{(\bm{x},y)\sim P\_{t}}\left[\left(f(\bm{x})-y\right)^{2}\right]}{\mathbb{E}\_{(\bm{x},y)\sim P\_{t}}[y^{2}]}, |  | (B.1) |

Define Vt=𝔼(𝒙,y)∼Pt​[y2]V\_{t}=\mathbb{E}\_{(\bm{x},y)\sim P\_{t}}[y^{2}], then R~t2​(f)=1−Lt​(f)/Vt\widetilde{R}^{2}\_{t}(f)=1-L\_{t}(f)/V\_{t}. For simplicity, we assume that at the beginning of each period t∈ℤ+t\in\mathbb{Z}\_{+}, we have access to {Vj}j=1t−1\{V\_{j}\}\_{j=1}^{t-1}. In our numerical experiments, we will approximate VjV\_{j} by its empirical counterpart computed from the validation data 𝒟jva\mathcal{D}\_{j}^{\operatorname{\mathrm{va}}}. For the population R2R^{2} metric to be well defined, we assume for simplicity that {Vt}t=1∞\{V\_{t}\}\_{t=1}^{\infty} are bounded away from zero.

###### Assumption B.1 (Uniformly lower bounded second moments).

There exists v>0v>0 such that Vt≥vV\_{t}\geq v for all t∈ℤ+t\in\mathbb{Z}\_{+}.

We first define the model comparison subroutine, which aims to output the better of two given candidate models f1f\_{1} and f2f\_{2}. Define the R2R^{2} performance gap

|  |  |  |
| --- | --- | --- |
|  | ΔtR=R~t2​(f2)−R~t2​(f1)=Lt​(f1)−Lt​(f2)Vt.\Delta^{R}\_{t}=\widetilde{R}^{2}\_{t}(f\_{2})-\widetilde{R}^{2}\_{t}(f\_{1})=\frac{L\_{t}(f\_{1})-L\_{t}(f\_{2})}{V\_{t}}. |  |

Then f2f\_{2} outperforms f1f\_{1} if and only if ΔtR>0\Delta^{R}\_{t}>0. For each window size ℓ∈[t−1]\ell\in[t-1], we can form a rolling-window estimator of ΔtR\Delta^{R}\_{t}, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ^t,ℓR=Δ^t,ℓVt,ℓ\widehat{\Delta}^{R}\_{t,\ell}=\frac{\widehat{\Delta}\_{t,\ell}}{V\_{t,\ell}} |  | (B.2) |

where Δ^t,ℓ\widehat{\Delta}\_{t,\ell} is defined by ([4.1](https://arxiv.org/html/2512.23596v1#S4.E1 "Equation 4.1 ‣ Pairwise comparison subroutine. ‣ 4.1 Adaptive Tournament Model Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")), and Vt,ℓ=1nt,ℓ​∑j=t−kt−1nj​VjV\_{t,\ell}=\frac{1}{n\_{t,\ell}}\sum\_{j=t-k}^{t-1}n\_{j}V\_{j}. We establish a bias-variance decomposition for the estimation error of Δ^t,ℓR\widehat{\Delta}^{R}\_{t,\ell}.

###### Lemma B.1 (Bias-variance decomposition).

Let Assumptions [2.1](https://arxiv.org/html/2512.23596v1#S2.Thmassumption1 "Assumption 2.1 (Independent data). ‣ 2 Problem Setup ‣ The nonstationarity-complexity tradeoff in return prediction"), [3.1](https://arxiv.org/html/2512.23596v1#S3.Thmassumption1 "Assumption 3.1 (Boundedness). ‣ 3.2 Theoretical Characterization ‣ 3 The Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction") and [B.1](https://arxiv.org/html/2512.23596v1#A2.Thmassumption1 "Assumption B.1 (Uniformly lower bounded second moments). ‣ Appendix B Extension: Model Selection with the 𝑅² Metric ‣ The nonstationarity-complexity tradeoff in return prediction") hold. Let σt,ℓR=σt,ℓ/Vt,ℓ\sigma^{R}\_{t,\ell}=\sigma\_{t,\ell}/V\_{t,\ell}, where σt,ℓ\sigma\_{t,\ell} is defined by ([4.4](https://arxiv.org/html/2512.23596v1#S4.E4 "Equation 4.4 ‣ Pairwise comparison subroutine. ‣ 4.1 Adaptive Tournament Model Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")). For δ∈(0,1)\delta\in(0,1), define

|  |  |  |
| --- | --- | --- |
|  | ϕR​(t,ℓ)=maxt−ℓ≤j≤t−1⁡|ΔjR−ΔtR|,\displaystyle\phi\_{R}(t,\ell)=\max\_{t-\ell\leq j\leq t-1}\big|\Delta^{R}\_{j}-\Delta^{R}\_{t}\big|, |  |
|  |  |  |
| --- | --- | --- |
|  | ψR​(t,ℓ,δ)={8​M2/v,if ​nt,ℓ=1σt,ℓR​2​log⁡(2/δ)nt,ℓ+16​(M2/v)​log⁡(2/δ)3​nt,ℓ,if ​nt,ℓ≥2.\displaystyle\psi\_{R}(t,\ell,\delta)=\begin{cases}8M^{2}/v,&\ \text{if }n\_{t,\ell}=1\\[6.0pt] \displaystyle\sigma^{R}\_{t,\ell}\sqrt{\frac{2\log(2/\delta)}{n\_{t,\ell}}}+\frac{16(M^{2}/v)\log(2/\delta)}{3n\_{t,\ell}},&\ \text{if }n\_{t,\ell}\geq 2\end{cases}. |  |

With probability at least 1−δ1-\delta,

|  |  |  |
| --- | --- | --- |
|  | |Δ^t,ℓR−ΔtR|≤ϕR​(t,ℓ)+ψR​(t,ℓ,δ).\big|\widehat{\Delta}^{R}\_{t,\ell}-\Delta^{R}\_{t}\big|\leq\phi\_{R}(t,\ell)+\psi\_{R}(t,\ell,\delta). |  |

###### Proof.

See LABEL:sm:sec-lem-bias-variance-decomp-R-proof.
∎

Based on LABEL:sm:lem-bias-variance-decomp-R and following the same idea as ([4.4](https://arxiv.org/html/2512.23596v1#S4.E4 "Equation 4.4 ‣ Pairwise comparison subroutine. ‣ 4.1 Adaptive Tournament Model Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")), we form a data-driven proxy for ψR​(t,ℓ,δ)\psi\_{R}(t,\ell,\delta), given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ^R​(t,ℓ,δ)={8​M2/v,if ​nt,ℓ=1v^t,ℓR​2​log⁡(2/δ)nt,ℓ+64​(M2/v)​log⁡(2/δ)3​(nt,ℓ−1),if ​nt,ℓ≥2,\widehat{\psi}\_{R}(t,\ell,\delta)=\begin{cases}8M^{2}/v,&\ \text{if }n\_{t,\ell}=1\\[6.0pt] \displaystyle\widehat{v}^{R}\_{t,\ell}\sqrt{\frac{2\log(2/\delta)}{n\_{t,\ell}}}+\frac{64(M^{2}/v)\log(2/\delta)}{3(n\_{t,\ell}-1)},&\ \text{if }n\_{t,\ell}\geq 2\end{cases}, |  | (B.3) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | v^t,ℓR=v^t,ℓVt,ℓ,\widehat{v}^{R}\_{t,\ell}=\frac{\widehat{v}\_{t,\ell}}{V\_{t,\ell}}, |  | (B.4) |

and v^t,ℓ\widehat{v}\_{t,\ell} is defined in ([4.3](https://arxiv.org/html/2512.23596v1#S4.E3 "Equation 4.3 ‣ Pairwise comparison subroutine. ‣ 4.1 Adaptive Tournament Model Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")). Following the same idea as ([4.5](https://arxiv.org/html/2512.23596v1#S4.E5 "Equation 4.5 ‣ Pairwise comparison subroutine. ‣ 4.1 Adaptive Tournament Model Selection ‣ 4 Adaptive Model and Data Selection under Non-Stationarity ‣ The nonstationarity-complexity tradeoff in return prediction")), we also form a data-driven proxy for ϕR​(t,ℓ,δ)\phi\_{R}(t,\ell,\delta):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ^R(t,ℓ,δ)=maxi∈[ℓ](|Δ^t,ℓR−Δ^t,iR|−[ψ^R(t,ℓ,δ)+ψ^R(t,i,δ)])+.\widehat{\phi}\_{R}(t,\ell,\delta)=\max\_{i\in[\ell]}\bigg(\big|\widehat{\Delta}^{R}\_{t,\ell}-\widehat{\Delta}^{R}\_{t,i}\big|-\big[\widehat{\psi}\_{R}\left(t,\ell,\delta\right)+\widehat{\psi}\_{R}\left(t,i,\delta\right)\big]\bigg)\_{+}. |  | (B.5) |

This yields LABEL:sm:alg-compare-R as the model comparison routine.

Input: Candidate models {f1,f2}\{f\_{1},f\_{2}\}, validation data {𝒟jva}j=1t−1\{\mathcal{D}^{\operatorname{\mathrm{va}}}\_{j}\}\_{j=1}^{t-1}, variances {Vj}j=1t−1\{V\_{j}\}\_{j=1}^{t-1}, hyperparameters δ′\delta^{\prime}, MM, vv.

for ℓ=1,⋯,t−1\ell=1,\cdots,t-1

Compute Δ^t,ℓR\widehat{\Delta}^{R}\_{t,\ell}, v^t,ℓR\widehat{v}^{R}\_{t,\ell}, ψ^R​(t,ℓ,δ′)\widehat{\psi}\_{R}(t,\ell,\delta^{\prime}) and ϕ^R​(t,ℓ,δ′)\widehat{\phi}\_{R}(t,\ell,\delta^{\prime}) according to ([B.2](https://arxiv.org/html/2512.23596v1#A2.E2 "Equation B.2 ‣ Appendix B Extension: Model Selection with the 𝑅² Metric ‣ The nonstationarity-complexity tradeoff in return prediction")), ([B.4](https://arxiv.org/html/2512.23596v1#A2.E4 "Equation B.4 ‣ Appendix B Extension: Model Selection with the 𝑅² Metric ‣ The nonstationarity-complexity tradeoff in return prediction")), ([B.3](https://arxiv.org/html/2512.23596v1#A2.E3 "Equation B.3 ‣ Appendix B Extension: Model Selection with the 𝑅² Metric ‣ The nonstationarity-complexity tradeoff in return prediction")) and ([B.5](https://arxiv.org/html/2512.23596v1#A2.E5 "Equation B.5 ‣ Appendix B Extension: Model Selection with the 𝑅² Metric ‣ The nonstationarity-complexity tradeoff in return prediction")).

Choose window size

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ^∈argminℓ∈[t−1]{ϕ^R​(t,ℓ,δ′)+ψ^R​(t,ℓ,δ′)}.\widehat{\ell}\in\mathop{\mathrm{argmin}}\_{\ell\in[t-1]}\Big\{\widehat{\phi}\_{R}(t,\ell,\delta^{\prime})+\widehat{\psi}\_{R}(t,\ell,\delta^{\prime})\Big\}. |  | (B.6) |

Select λ^=1\widehat{\lambda}=1 if Δ^t,ℓ^R≤0\widehat{\Delta}^{R}\_{t,\widehat{\ell}}\leq 0, and λ^=2\widehat{\lambda}=2 otherwise.

return f^=fλ^\widehat{f}=f\_{\widehat{\lambda}}.

Algorithm 4  Adaptive Rolling Window for Model Comparison (R2R^{2} Metric)

By using LABEL:sm:alg-compare-R as the pairwise comparison subroutine 𝒜\mathcal{A} in LABEL:sm:alg-tournament, we obtain an R2R^{2}-based model selection algorithm, which we call ATOMS-R2. We establish the following guarantee in terms of the R2R^{2} metric.

###### Theorem B.1 (Near-optimal model selection with R2R^{2}).

Let Assumptions [2.1](https://arxiv.org/html/2512.23596v1#S2.Thmassumption1 "Assumption 2.1 (Independent data). ‣ 2 Problem Setup ‣ The nonstationarity-complexity tradeoff in return prediction") and [3.1](https://arxiv.org/html/2512.23596v1#S3.Thmassumption1 "Assumption 3.1 (Boundedness). ‣ 3.2 Theoretical Characterization ‣ 3 The Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction") hold. Choose δ∈(0,1)\delta\in(0,1) and set δ′=1/(3​Λ2​t)\delta^{\prime}=1/(3\Lambda^{2}t) in LABEL:sm:alg-tournament. With probability at least 1−δ1-\delta, the output f^\widehat{f} of ATOMS-R2 satisfies

|  |  |  |
| --- | --- | --- |
|  | maxλ∈[Λ]⁡R~t2​(fλ)−R~t2​(f^)≲log⁡(Λ​t/δ)⋅minℓ∈[t−1]⁡{maxt−ℓ≤j≤t−1⁡maxλ∈[Λ]⁡|R~j2​(fλ)−R~t2​(fλ)|+M2/vnt,ℓ}.\max\_{\lambda\in[\Lambda]}\widetilde{R}^{2}\_{t}(f\_{\lambda})-\widetilde{R}^{2}\_{t}(\widehat{f})\lesssim\log(\Lambda t/\delta)\cdot\min\_{\ell\in[t-1]}\left\{\max\_{t-\ell\leq j\leq t-1}\max\_{\lambda\in[\Lambda]}\big|\widetilde{R}^{2}\_{j}(f\_{\lambda})-\widetilde{R}^{2}\_{t}(f\_{\lambda})\big|+\frac{M^{2}/v}{\sqrt{n\_{t,\ell}}}\right\}. |  |

Here ≲\lesssim hides a universal constant.

###### Proof of LABEL:sm:thm-select-tournament-R.

See LABEL:sm:sec-thm-select-tournament-R-proof.
∎

LABEL:sm:thm-select-tournament-R shares a similar interpretation as LABEL:sm:thm-select-tournament. The term

|  |  |  |
| --- | --- | --- |
|  | maxt−ℓ≤j≤t−1⁡maxλ∈[Λ]⁡|R~j2​(fλ)−R~t2​(fλ)|\max\_{t-\ell\leq j\leq t-1}\max\_{\lambda\in[\Lambda]}\big|\widetilde{R}^{2}\_{j}(f\_{\lambda})-\widetilde{R}^{2}\_{t}(f\_{\lambda})\big| |  |

quantifies the shift in the R2R^{2} metric of the models within the last ℓ\ell periods, and (M2/v)/nt,ℓ(M^{2}/v)/\sqrt{n\_{t,\ell}} represents the statistical uncertainty associated with the nt,ℓn\_{t,\ell} validation data points. Together, they represent the errors that arise when using a fixed validation window ℓ\ell to select models. LABEL:sm:thm-select-tournament-R shows that our R2R^{2}-based model selection algorithm ATOMS-R2 is comparable to an oracle that uses the optimal validation window in hindsight to attain the highest R2R^{2}.

In LABEL:sm:sec-experiments-adaptive-R2, we present numerical experiment results for ATOMS-R2, which are similar to those for ATOMS.

## Appendix C Theoretical Analysis of Nonstationarity-Complexity Tradeoff

In this section, we provide more details on LABEL:sm:thm-tradeoff and its proof.

We first set up some mathematical notation. Recall that ft∗​(⋅)=𝔼(𝒙,y)∼Pt​[y∣𝒙=⋅]f\_{t}^{\*}(\cdot)=\mathbb{E}\_{(\bm{x},y)\sim P\_{t}}[y\mid\bm{x}=\cdot] is the Bayes optimal least squares estimator, which minimizes Lt​(f)L\_{t}(f) over all measurable f:𝒳→ℝf:\mathcal{X}\to\mathbb{R}. Let

|  |  |  |
| --- | --- | --- |
|  | f¯t=argminf∈ℱLt​(f),\bar{f}\_{t}=\mathop{\mathrm{argmin}}\_{f\in\mathcal{F}}L\_{t}(f), |  |

which minimizes Lt​(f)L\_{t}(f) over all f∈ℱf\in\mathcal{F}. For each tt, let Pt,𝒙P\_{t,\bm{x}} be the marginal distribution of PtP\_{t} with respect to the covariates 𝒙\bm{x}. The distribution Pt,𝒙P\_{t,\bm{x}} induces a norm ∥⋅∥t\|\cdot\|\_{t}, given by

|  |  |  |
| --- | --- | --- |
|  | ‖f‖t=𝔼𝒙∼Pt,𝒙​[f​(𝒙)2].\|f\|\_{t}=\sqrt{\mathbb{E}\_{\bm{x}\sim P\_{t,\bm{x}}}\left[f(\bm{x})^{2}\right]}. |  |

It can be shown that ℰt​(f)=‖f−ft∗‖t2\mathcal{E}\_{t}(f)=\|f-f\_{t}^{\*}\|\_{t}^{2} for all f:𝒳→ℝf:\mathcal{X}\to\mathbb{R}.

### C.1 A Non-Stationary Local Rademacher complexity

We now formally define rt,k​(ℱ)r\_{t,k}(\mathcal{F}) through a non-stationary version of the *local Rademacher complexity* (BBM05). We first define the *Rademacher complexity*, which reflects the richness of a function class with respect to certain data samples.

###### Definition C.1 (Rademacher complexity).

Let {𝐳i}i=1n\{\bm{z}\_{i}\}\_{i=1}^{n} be independent random variables in 𝒳\mathcal{X}. Let 𝒢\mathcal{G} be a class of functions from 𝒳\mathcal{X} to ℝ\mathbb{R}. The Rademacher complexity of 𝒢\mathcal{G} associated with {𝐳i}i=1n\{\bm{z}\_{i}\}\_{i=1}^{n} is defined by

|  |  |  |
| --- | --- | --- |
|  | ℜ​(𝒢;{𝒛i}i=1n)=𝔼​[supg∈𝒢1n​∑i=1nεi​g​(𝒛i)],\mathfrak{R}(\mathcal{G};\{\bm{z}\_{i}\}\_{i=1}^{n})=\mathbb{E}\left[\sup\_{g\in\mathcal{G}}\frac{1}{n}\sum\_{i=1}^{n}\varepsilon\_{i}g(\bm{z}\_{i})\right], |  |

where ε1,…,εn\varepsilon\_{1},...,\varepsilon\_{n} are i.i.d. random variables following the Rademacher distribution ℙ​(ε1=1)=ℙ​(ε1=−1)=1/2\mathbb{P}(\varepsilon\_{1}=1)=\mathbb{P}(\varepsilon\_{1}=-1)=1/2, and are independent of {zi}i=1n\{z\_{i}\}\_{i=1}^{n}.

The local Rademacher complexity is the Rademacher complexity of some local function class centered at f¯t\bar{f}\_{t}.

###### Definition C.2 (Local function class).

For every r≥0r\geq 0, define the local function class

|  |  |  |
| --- | --- | --- |
|  | ℱt,k​(r)={f∈ℱ:1mt,k​∑j=t−kt−1mj​‖f−f¯t‖j2≤r}.\mathcal{F}\_{t,k}(r)=\bigg\{f\in\mathcal{F}:\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\left\|f-\bar{f}\_{t}\right\|\_{j}^{2}\leq r\bigg\}. |  |

In words, ℱt,k​(r)\mathcal{F}\_{t,k}(r) consists of functions f∈ℱf\in\mathcal{F} that are close to f¯t\bar{f}\_{t} with respect to the distributions {Pj,𝒙}j=t−kt−1\{P\_{j,\bm{x}}\}\_{j=t-k}^{t-1} on average. We are now ready to define the quantity rt,k​(ℱ)r\_{t,k}(\mathcal{F}), which is more formally known as the *critical radius* of the function

|  |  |  |
| --- | --- | --- |
|  | ℜt,k​(r;ℱ)=ℜ​(ℱt,k​(r);𝒟t,ktr).\mathfrak{R}\_{t,k}(r;\mathcal{F})=\mathfrak{R}\left(\mathcal{F}\_{t,k}(r);\mathcal{D}\_{t,k}^{\operatorname{\mathrm{tr}}}\right). |  |

###### Definition C.3 (Subroot function).

A function ψ:ℝ+→ℝ+\psi:\mathbb{R}\_{+}\to\mathbb{R}\_{+} is subroot if it is increasing and r↦ψ​(r)/rr\mapsto\psi(r)/\sqrt{r} is decreasing on (0,∞)(0,\infty).

###### Definition C.4 (Critical radius).

The critical radius of ℜt,k​(r;ℱ)\mathfrak{R}\_{t,k}(r;\mathcal{F}) is defined by

|  |  |  |
| --- | --- | --- |
|  | rt,k​(ℱ)=inf{r≥0:∃subroot ​ψ​ such that ​ψ​(r)=r, and ​ψ​(s)≥ℜt,k​(s;ℱ)​∀s≥r}.r\_{t,k}(\mathcal{F})=\inf\left\{r\geq 0:\exists\,\text{subroot }\psi\text{ such that }\psi(r)=r,\text{ and }\psi(s)\geq\mathfrak{R}\_{t,k}(s;\mathcal{F})\ \forall s\geq r\right\}. |  |

### C.2 Proof of LABEL:sm:thm-tradeoff

We now prove LABEL:sm:thm-tradeoff. In the proof, we will write f^=f^t,k\widehat{f}=\widehat{f}\_{t,k} to emphasize its dependence on the time tt and the training window size kk. The key of the proof is the following lemma, which is a non-stationary version of Theorem 3.3 in BBM05.

###### Lemma C.1 (Localized uniform concentration).

Let 𝐳1,…,𝐳n\bm{z}\_{1},...,\bm{z}\_{n} be independent random variables taking values in a space 𝒵⊆ℝd+1\mathcal{Z}\subseteq\mathbb{R}^{d+1}. Let 𝒢\mathcal{G} be a collection of functions from 𝒵\mathcal{Z} to [a,b][a,b]. Suppose that there exist T:𝒢→ℝ+T:\mathcal{G}\to\mathbb{R}\_{+} and C,η1,…,ηn≥0C,\eta\_{1},...,\eta\_{n}\geq 0 such that the following noise condition holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1n​∑i=1nvar⁡[g​(𝒛i)]≤T​(g)≤C⋅1n​∑i=1n(𝔼​[g​(𝒛i)]+ηi),∀g∈𝒢.\frac{1}{n}\sum\_{i=1}^{n}\operatorname{{\rm var}}\left[g(\bm{z}\_{i})\right]\leq T(g)\leq C\cdot\frac{1}{n}\sum\_{i=1}^{n}\big(\mathbb{E}\left[g(\bm{z}\_{i})\right]+\eta\_{i}\big),\qquad\forall g\in\mathcal{G}. |  | (C.1) |

Let ψ\psi be a sub-root function with a fixed point r∗r^{\*} satisfying

|  |  |  |
| --- | --- | --- |
|  | ψ​(r)≥C⋅ℜ​({g∈𝒢:T​(g)≤r};{𝒛i}i=1n),∀r≥r∗.\psi(r)\geq C\cdot\mathfrak{R}\big(\{g\in\mathcal{G}:T(g)\leq r\};\{\bm{z}\_{i}\}\_{i=1}^{n}\big),\qquad\forall r\geq r^{\*}. |  |

Take δ∈(0,1)\delta\in(0,1). With probability at least 1−δ1-\delta, for all g∈𝒢g\in\mathcal{G} and K>1K>1,

|  |  |  |
| --- | --- | --- |
|  | 1n​∑i=1n𝔼​[g​(𝒛i)]≤KK−1⋅1n​∑i=1ng​(𝒛i)+c​[KC​r∗+((b−a)+C​K)​log⁡(1/δ)n]+1K−1⋅1n​∑i=1nηi.\frac{1}{n}\sum\_{i=1}^{n}\mathbb{E}\left[g(\bm{z}\_{i})\right]\leq\frac{K}{K-1}\cdot\frac{1}{n}\sum\_{i=1}^{n}g(\bm{z}\_{i})+c\left[\frac{K}{C}r^{\*}+\left((b-a)+CK\right)\frac{\log(1/\delta)}{n}\right]+\frac{1}{K-1}\cdot\frac{1}{n}\sum\_{i=1}^{n}\eta\_{i}. |  |

Here c>0c>0 is a universal constant.

###### Proof of LABEL:sm:lem-local-uniform-concentration.

See LABEL:sm:sec-proof-lem-local-uniform-concentration.
∎

For every f∈ℱf\in\mathcal{F}, define ℓf:𝒳×ℝ→ℝ\ell\_{f}:\mathcal{X}\times\mathbb{R}\to\mathbb{R} by ℓf​((𝒙,y))=[f​(𝒙)−y]2\ell\_{f}((\bm{x},y))=[f(\bm{x})-y]^{2}. We also denote (𝒙,y)(\bm{x},y) by 𝒛\bm{z}. In LABEL:sm:lem-local-uniform-concentration, take {𝒛i}i=1n=ℬt,ktr\{\bm{z}\_{i}\}\_{i=1}^{n}=\mathcal{B}\_{t,k}^{\operatorname{\mathrm{tr}}} and 𝒢={ℓf−ℓf¯t:f∈ℱ}\mathcal{G}=\{\ell\_{f}-\ell\_{\bar{f}\_{t}}:f\in\mathcal{F}\}. The following lemma suggests a choice of gig\_{i} and TT for which ([C.1](https://arxiv.org/html/2512.23596v1#A3.E1 "Equation C.1 ‣ Lemma C.1 (Localized uniform concentration). ‣ C.2 Proof of ‣ Appendix C Theoretical Analysis of Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction")) holds.

###### Lemma C.2 (Noise condition).

Let Assumption LABEL:sm:assumption-bounded hold. For all f,f¯∈ℱf,\bar{f}\in\mathcal{F},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1mt,k​∑j=t−kt−1mj​var𝒛∼Pj⁡[ℓf​(𝒛)−ℓf¯​(𝒛)]\displaystyle\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\operatorname{{\rm var}}\_{\bm{z}\sim P\_{j}}\left[\ell\_{f}(\bm{z})-\ell\_{\bar{f}}(\bm{z})\right] | ≤16​M2⋅1mt,k​∑j=t−kt−1mj​‖f−f¯‖j2\displaystyle\leq 16M^{2}\cdot\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\|f-\bar{f}\|\_{j}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤32​M2⋅1mt,k​∑j=t−kt−1mj​{𝔼𝒛∼Pj​[ℓf​(𝒛)−ℓf¯​(𝒛)]+2​ℰj​(f¯)}.\displaystyle\leq 32M^{2}\cdot\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\left\{\mathbb{E}\_{\bm{z}\sim P\_{j}}\left[\ell\_{f}(\bm{z})-\ell\_{\bar{f}}(\bm{z})\right]+2\mathcal{E}\_{j}(\bar{f})\right\}. |  |

###### Proof of LABEL:sm:lem-noise-condition-regression.

See LABEL:sm:sec-proof-lem-noise-condition-regression.
∎

Define

|  |  |  |
| --- | --- | --- |
|  | T​(ℓf−ℓf¯t)=16​M2⋅1mt,k​∑j=t−kt−1mj​‖f−f¯t‖j2,∀f∈ℱ.T(\ell\_{f}-\ell\_{\bar{f}\_{t}})=16M^{2}\cdot\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\left\|f-\bar{f}\_{t}\right\|\_{j}^{2},\qquad\forall f\in\mathcal{F}. |  |

By LABEL:sm:lem-noise-condition-regression, the noise condition ([C.1](https://arxiv.org/html/2512.23596v1#A3.E1 "Equation C.1 ‣ Lemma C.1 (Localized uniform concentration). ‣ C.2 Proof of ‣ Appendix C Theoretical Analysis of Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction")) holds with C=32​M2C=32M^{2}, and LABEL:sm:lem-local-uniform-concentration is applicable. Moreover, for all r≥0r\geq 0,

|  |  |  |
| --- | --- | --- |
|  | ℜ​({ℓf−ℓf¯t:f∈ℱ,T​(ℓf−ℓf¯t)≤r};𝒟t,ktr)\displaystyle\mathfrak{R}\left(\left\{\ell\_{f}-\ell\_{\bar{f}\_{t}}:f\in\mathcal{F},\,T(\ell\_{f}-\ell\_{\bar{f}\_{t}})\leq r\right\};\mathcal{D}^{\operatorname{\mathrm{tr}}}\_{t,k}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝔼​sup{1mt,k​∑j=t−kt−1∑i=1mjεj,i​[f​(𝒙j,i)−yj,i]2:f∈ℱ,T​(ℓf−ℓf¯t)≤r}\displaystyle\qquad=\mathbb{E}\sup\left\{\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}\sum\_{i=1}^{m\_{j}}\varepsilon\_{j,i}\left[f(\bm{x}\_{j,i})-y\_{j,i}\right]^{2}:f\in\mathcal{F},\,T(\ell\_{f}-\ell\_{\bar{f}\_{t}})\leq r\right\} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤4​M⋅𝔼​sup{1mt,k​∑j=t−kt−1∑i=1mjεj,i​[f​(𝒙j,i)−yj,i]:f∈ℱ,T​(ℓf−ℓf¯t)≤r}\displaystyle\qquad\leq 4M\cdot\mathbb{E}\sup\left\{\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}\sum\_{i=1}^{m\_{j}}\varepsilon\_{j,i}\left[f(\bm{x}\_{j,i})-y\_{j,i}\right]:f\in\mathcal{F},\,T(\ell\_{f}-\ell\_{\bar{f}\_{t}})\leq r\right\} |  |
|  |  |  |
| --- | --- | --- |
|  | =4​M⋅𝔼​sup{1mt,k​∑j=t−kt−1∑i=1mjεj,i​f​(𝒙j,i):f∈ℱ,T​(ℓf−ℓf¯t)≤r}\displaystyle\qquad=4M\cdot\mathbb{E}\sup\left\{\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}\sum\_{i=1}^{m\_{j}}\varepsilon\_{j,i}f(\bm{x}\_{j,i}):f\in\mathcal{F},\,T(\ell\_{f}-\ell\_{\bar{f}\_{t}})\leq r\right\} |  |
|  |  |  |
| --- | --- | --- |
|  | =4​M⋅ℜ​({f∈ℱ:T​(ℓf−ℓf¯t)≤r};𝒟t,ktr),\displaystyle\qquad=4M\cdot\mathfrak{R}\left(\left\{f\in\mathcal{F}:T(\ell\_{f}-\ell\_{\bar{f}\_{t}})\leq r\right\};\mathcal{D}^{\operatorname{\mathrm{tr}}}\_{t,k}\right), |  |

where {εj,i}\{\varepsilon\_{j,i}\} are i.i.d. Rademacher random variables, and the inequality is due to Theorem A.6 in BBM05.

Define

|  |  |  |
| --- | --- | --- |
|  | Lt,ktr​(f)=1mt,k​∑j=t−kt−1mj​Lj​(f).L\_{t,k}^{\operatorname{\mathrm{tr}}}(f)=\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}L\_{j}(f). |  |

Applying LABEL:sm:lem-local-uniform-concentration with g=f^t,k−f¯tg=\widehat{f}\_{t,k}-\bar{f}\_{t}, we obtain that if ψ~:ℝ+→ℝ+\widetilde{\psi}:\mathbb{R}\_{+}\to\mathbb{R}\_{+} is a sub-root function with fixed point r~\widetilde{r} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ~​(r)≥128​M3⋅ℜ​({f∈ℱ:T​(ℓf−ℓf¯t)≤r};𝒟t,ktr),∀r≥r~,\widetilde{\psi}(r)\geq 128M^{3}\cdot\mathfrak{R}\left(\left\{f\in\mathcal{F}:T(\ell\_{f}-\ell\_{\bar{f}\_{t}})\leq r\right\};\mathcal{D}^{\operatorname{\mathrm{tr}}}\_{t,k}\right),\qquad\forall r\geq\widetilde{r}, |  | (C.2) |

then with probability at least 1−δ1-\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt,ktr​(f^t,k)−Lt,ktr​(f¯t)\displaystyle L^{\operatorname{\mathrm{tr}}}\_{t,k}(\widehat{f}\_{t,k})-L^{\operatorname{\mathrm{tr}}}\_{t,k}(\bar{f}\_{t}) | ≲(L^t,ktr​(f^t,k)−L^t,ktr​(f¯t))+[r~M2+M2​log⁡(1/δ)mt,k]+maxt−k≤j≤t−1⁡ℰj​(f¯t)\displaystyle\lesssim\left(\widehat{L}\_{t,k}^{\operatorname{\mathrm{tr}}}(\widehat{f}\_{t,k})-\widehat{L}\_{t,k}^{\operatorname{\mathrm{tr}}}(\bar{f}\_{t})\right)+\left[\frac{\widetilde{r}}{M^{2}}+\frac{M^{2}\log(1/\delta)}{m\_{t,k}}\right]+\max\_{t-k\leq j\leq t-1}\mathcal{E}\_{j}(\bar{f}\_{t}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≲[r~M2+M2​log⁡(1/δ)mt,k]+maxt−k≤j≤t−1⁡ℰj​(f¯t),\displaystyle\lesssim\left[\frac{\widetilde{r}}{M^{2}}+\frac{M^{2}\log(1/\delta)}{m\_{t,k}}\right]+\max\_{t-k\leq j\leq t-1}\mathcal{E}\_{j}(\bar{f}\_{t}), |  | (C.3) |

where ≲\lesssim hides a universal constant, and the second inequality is due to L^t,ktr​(f^t,k)≤L^t,ktr​(f¯t)\widehat{L}^{\operatorname{\mathrm{tr}}}\_{t,k}(\widehat{f}\_{t,k})\leq\widehat{L}^{\operatorname{\mathrm{tr}}}\_{t,k}(\bar{f}\_{t}).

It remains to express r~\widetilde{r} in terms of rt,kr\_{t,k}, and convert ([C.3](https://arxiv.org/html/2512.23596v1#A3.E3 "Equation C.3 ‣ C.2 Proof of ‣ Appendix C Theoretical Analysis of Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction")) into a bound for Lt​(f^t,k)L\_{t}(\widehat{f}\_{t,k}). We work on r~\widetilde{r} first. Take a subroot function ψ:ℝ+→ℝ+\psi:\mathbb{R}\_{+}\to\mathbb{R}\_{+} with fixed point rt,kr\_{t,k} such that

|  |  |  |
| --- | --- | --- |
|  | ψ​(r)≥ℜ​({f∈ℱ:1nt,k​∑j=t−kt−1nj​‖f−f¯t‖j2≤r}),∀r≥rt,k.\psi(r)\geq\mathfrak{R}\bigg(\bigg\{f\in\mathcal{F}:\frac{1}{n\_{t,k}}\sum\_{j=t-k}^{t-1}n\_{j}\left\|f-\bar{f}\_{t}\right\|\_{j}^{2}\leq r\bigg\}\bigg),\quad\forall r\geq r\_{t,k}. |  |

We now show that ψ~​(r)=128​M3​ψ​(r16​M2)\widetilde{\psi}(r)=128M^{3}\psi\left(\frac{r}{16M^{2}}\right) satisfies ([C.2](https://arxiv.org/html/2512.23596v1#A3.E2 "Equation C.2 ‣ C.2 Proof of ‣ Appendix C Theoretical Analysis of Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction")). By LABEL:sm:lem-property-subroot, the fixed point r~\widetilde{r} of ψ~\widetilde{\psi} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | min{1,8M}216M2rt,k≤r~≤max{1,8M}216M2rt,k.\min\{1,8M\}^{2}16M^{2}r\_{t,k}\leq\widetilde{r}\leq\max\{1,8M\}^{2}16M^{2}r\_{t,k}. |  | (C.4) |

For all r≥r~r\geq\widetilde{r}, since r≥rt,kr\geq r\_{t,k}, then

|  |  |  |
| --- | --- | --- |
|  | ψ~​(r)≥128​M3⋅ℜ​({f∈ℱ:16​M2⋅1nt,k​∑j=t−kt−1nj​‖f−f¯t‖j2≤r}),\widetilde{\psi}(r)\geq 128M^{3}\cdot\mathfrak{R}\bigg(\bigg\{f\in\mathcal{F}:16M^{2}\cdot\frac{1}{n\_{t,k}}\sum\_{j=t-k}^{t-1}n\_{j}\left\|f-\bar{f}\_{t}\right\|\_{j}^{2}\leq r\bigg\}\bigg), |  |

so ([C.2](https://arxiv.org/html/2512.23596v1#A3.E2 "Equation C.2 ‣ C.2 Proof of ‣ Appendix C Theoretical Analysis of Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction")) holds for this choice of ψ~\widetilde{\psi}, and ([C.3](https://arxiv.org/html/2512.23596v1#A3.E3 "Equation C.3 ‣ C.2 Proof of ‣ Appendix C Theoretical Analysis of Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt,ktr​(f^t,k)−Lt,ktr​(f¯t)≲M2​[rt,k+log⁡(1+δ−1)mt,k]+maxt−k≤j≤t−1⁡ℰj​(f¯t).L^{\operatorname{\mathrm{tr}}}\_{t,k}(\widehat{f}\_{t,k})-L^{\operatorname{\mathrm{tr}}}\_{t,k}(\bar{f}\_{t})\lesssim M^{2}\left[r\_{t,k}+\frac{\log(1+\delta^{-1})}{m\_{t,k}}\right]+\max\_{t-k\leq j\leq t-1}\mathcal{E}\_{j}(\bar{f}\_{t}). |  | (C.5) |

Finally, we will convert ([C.5](https://arxiv.org/html/2512.23596v1#A3.E5 "Equation C.5 ‣ C.2 Proof of ‣ Appendix C Theoretical Analysis of Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction")) into a bound for Lt​(f^t,k)L\_{t}(\widehat{f}\_{t,k}). We invoke the following lemma.

###### Lemma C.3.

For all f∈ℱf\in\mathcal{F} and j,t∈ℤ+j,t\in\mathbb{Z}\_{+},

|  |  |  |
| --- | --- | --- |
|  | |Lj​(f)−Lt​(f)|≤4​M2​TV⁡(Pj,Pt),\displaystyle\left|L\_{j}(f)-L\_{t}(f)\right|\leq 4M^{2}\operatorname{TV}\left(P\_{j},P\_{t}\right), |  |
|  |  |  |
| --- | --- | --- |
|  | |ℰj​(f)−ℰt​(f)|≤4​M2​TV⁡(Pj,Pt).\displaystyle\left|\mathcal{E}\_{j}(f)-\mathcal{E}\_{t}(f)\right|\leq 4M^{2}\operatorname{TV}\left(P\_{j},P\_{t}\right). |  |

###### Proof of LABEL:sm:lem-risk-to-TV.

For every f∈ℱf\in\mathcal{F},

|  |  |  |
| --- | --- | --- |
|  | |Lj​(f)−Lt​(f)|=|𝔼(x,y)∼Pj​{[f​(x)−y]2}−𝔼(x,y)∼Pt​{[f​(x)−y]2}|≤4​M2⋅TV⁡(Pj,Pt).\left|L\_{j}(f)-L\_{t}(f)\right|=\left|\mathbb{E}\_{(x,y)\sim P\_{j}}\left\{\left[f(x)-y\right]^{2}\right\}-\mathbb{E}\_{(x,y)\sim P\_{t}}\left\{\left[f(x)-y\right]^{2}\right\}\right|\leq 4M^{2}\cdot\operatorname{TV}(P\_{j},P\_{t}). |  |

To prove the second inequality, since Lt​(ft∗)≤Lt​(fj∗)L\_{t}(f\_{t}^{\*})\leq L\_{t}(f\_{j}^{\*}), then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰj​(f)−ℰt​(f)\displaystyle\mathcal{E}\_{j}(f)-\mathcal{E}\_{t}(f) | =[Lj​(f)−Lj​(fj∗)]−[Lt​(f)−Lt​(ft∗)]\displaystyle=\big[L\_{j}(f)-L\_{j}(f\_{j}^{\*})\big]-\big[L\_{t}(f)-L\_{t}(f\_{t}^{\*})\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤[Lj​(f)−Lj​(fj∗)]−[Lt​(f)−Lt​(fj∗)]\displaystyle\leq\big[L\_{j}(f)-L\_{j}(f\_{j}^{\*})\big]-\big[L\_{t}(f)-L\_{t}(f\_{j}^{\*})\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼(x,y)∼Pj​{[f​(x)−y]2−[fj∗​(x)−y]2}−𝔼(x,y)∼Pt​{[f​(x)−y]2−[fj∗​(x)−y]2}\displaystyle=\mathbb{E}\_{(x,y)\sim P\_{j}}\left\{\left[f(x)-y\right]^{2}-\left[f\_{j}^{\*}(x)-y\right]^{2}\right\}-\mathbb{E}\_{(x,y)\sim P\_{t}}\left\{\left[f(x)-y\right]^{2}-\left[f\_{j}^{\*}(x)-y\right]^{2}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤4​M2⋅TV⁡(Pj,Pt).\displaystyle\leq 4M^{2}\cdot\operatorname{TV}\left(P\_{j},P\_{t}\right). |  |

By symmetry, ℰt​(f)−ℰj​(f)≤M2⋅TV⁡(Pj,Pt)\mathcal{E}\_{t}(f)-\mathcal{E}\_{j}(f)\leq M^{2}\cdot\operatorname{TV}\left(P\_{j},P\_{t}\right), so

|  |  |  |
| --- | --- | --- |
|  | maxt−k≤j≤t−1⁡|ℰj​(f)−ℰt​(f)|≤4​M2​maxt−k≤j≤t−1⁡TV⁡(Pj,Pt).\max\_{t-k\leq j\leq t-1}\left|\mathcal{E}\_{j}(f)-\mathcal{E}\_{t}(f)\right|\leq 4M^{2}\max\_{t-k\leq j\leq t-1}\operatorname{TV}\left(P\_{j},P\_{t}\right). |  |

This finishes the proof.
∎

Since

|  |  |  |
| --- | --- | --- |
|  | |Lt,ktr​(f)−Lt​(f)|≤maxt−k≤j≤t−1⁡|Lj​(f)−Lt​(f)|,\big|L^{\operatorname{\mathrm{tr}}}\_{t,k}(f)-L\_{t}(f)\big|\leq\max\_{t-k\leq j\leq t-1}|L\_{j}(f)-L\_{t}(f)|, |  |

then substituting LABEL:sm:lem-risk-to-TV into ([C.5](https://arxiv.org/html/2512.23596v1#A3.E5 "Equation C.5 ‣ C.2 Proof of ‣ Appendix C Theoretical Analysis of Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction")) yields

|  |  |  |
| --- | --- | --- |
|  | Lt​(f^t,k)−Lt​(f¯t)≲M2​[rt,k+log⁡(1+δ−1)mt,k]+ℰt​(f¯t)+M2​maxt−k≤j≤t−1⁡TV⁡(Pj,Pt).L\_{t}(\widehat{f}\_{t,k})-L\_{t}(\bar{f}\_{t})\lesssim M^{2}\left[r\_{t,k}+\frac{\log(1+\delta^{-1})}{m\_{t,k}}\right]+\mathcal{E}\_{t}(\bar{f}\_{t})+M^{2}\max\_{t-k\leq j\leq t-1}\operatorname{TV}\left(P\_{j},P\_{t}\right). |  |

Since ℰt​(f)=Lt​(f)−Lt​(ft∗)\mathcal{E}\_{t}(f)=L\_{t}(f)-L\_{t}(f\_{t}^{\*}), then

|  |  |  |
| --- | --- | --- |
|  | ℰ​(f^t,k)≲ℰt​(f¯t)+M2​[rt,k+log⁡(1+δ−1)mt,k]+M2​maxt−k≤j≤t−1⁡TV⁡(Pj,Pt).\mathcal{E}(\widehat{f}\_{t,k})\lesssim\mathcal{E}\_{t}(\bar{f}\_{t})+M^{2}\left[r\_{t,k}+\frac{\log(1+\delta^{-1})}{m\_{t,k}}\right]+M^{2}\max\_{t-k\leq j\leq t-1}\operatorname{TV}\left(P\_{j},P\_{t}\right). |  |

This completes the proof.

### C.3 Proof of LABEL:sm:lem-local-uniform-concentration

The core techniques are the same as those of Theorem 3.3 in BBM05, with small changes in the quantities to bound. For r,λ>0r,\lambda>0, let

|  |  |  |
| --- | --- | --- |
|  | w​(g)=min⁡{r​λk:k∈{0}∪ℤ+,r​λk≥T​(g)},𝒢r={rw​(g)​g:g∈𝒢},w(g)=\min\{r\lambda^{k}:k\in\{0\}\cup\mathbb{Z}\_{+},\,r\lambda^{k}\geq T(g)\},\qquad\mathcal{G}\_{r}=\left\{\frac{r}{w(g)}g:g\in\mathcal{G}\right\}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Vr+=supg∈𝒢{rw​(g)⋅1n​∑i=1n(𝔼​[g​(𝒛i)]−g​(𝒛i))}.V\_{r}^{+}=\sup\_{g\in\mathcal{G}}\left\{\frac{r}{w(g)}\cdot\frac{1}{n}\sum\_{i=1}^{n}\big(\mathbb{E}[g(\bm{z}\_{i})]-g(\bm{z}\_{i})\big)\right\}. |  |

Similar to Lemma 3.8 of BBM05, for every K>1K>1 and g∈𝒢g\in\mathcal{G},

|  |  |  |
| --- | --- | --- |
|  | Vr+≤rλ​C​Kimplies1n​∑i=1n𝔼​[g​(𝒛i)]≤KK−1⋅1n​∑i=1ng​(𝒛i)+rλ​C​K+1K−1⋅1n​∑i=1nηi.V\_{r}^{+}\leq\frac{r}{\lambda CK}\quad\text{implies}\quad\frac{1}{n}\sum\_{i=1}^{n}\mathbb{E}[g(\bm{z}\_{i})]\leq\frac{K}{K-1}\cdot\frac{1}{n}\sum\_{i=1}^{n}g(\bm{z}\_{i})+\frac{r}{\lambda CK}+\frac{1}{K-1}\cdot\frac{1}{n}\sum\_{i=1}^{n}\eta\_{i}. |  |

We now invoke a uniform convergence result to give a bound for Vr+V\_{r}^{+}. It is a non-stationary version of Theorem 2.1 in BBM05.

###### Lemma C.4 (Uniform concentration).

Consider the setting of LABEL:sm:lem-local-uniform-concentration. Define

|  |  |  |
| --- | --- | --- |
|  | v=1n​supg∈𝒢∑i=1nvar⁡[g​(𝒛i)].v=\frac{1}{n}\sup\_{g\in\mathcal{G}}\sum\_{i=1}^{n}\operatorname{{\rm var}}[g(\bm{z}\_{i})]. |  |

Let δ∈(0,1)\delta\in(0,1). With probability at least 1−δ1-\delta,

|  |  |  |
| --- | --- | --- |
|  | supg∈𝒢1n​∑i=1n(𝔼​[g​(𝒛i)]−g​(𝒛i))\displaystyle\sup\_{g\in\mathcal{G}}\frac{1}{n}\sum\_{i=1}^{n}\big(\mathbb{E}[g(\bm{z}\_{i})]-g(\bm{z}\_{i})\big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≲infα>0{(1+α)​ℜ​(𝒢;{𝒛i}i=1n)+v​log⁡(1/δ)n+(1+α−1)​(b−a)​log⁡(1/δ)n},\displaystyle\qquad\lesssim\inf\_{\alpha>0}\left\{(1+\alpha)\mathfrak{R}(\mathcal{G};\{\bm{z}\_{i}\}\_{i=1}^{n})+\sqrt{\frac{v\log(1/\delta)}{n}}+(1+\alpha^{-1})\frac{(b-a)\log(1/\delta)}{n}\right\}, |  |

where ≲\lesssim hides a universal constant.

###### Proof of LABEL:sm:lem-uniform-concentration.

Let Z=supg∈𝒢1n​∑i=1n[g​(𝒛i)−𝔼​g​(𝒛i)]Z=\sup\_{g\in\mathcal{G}}\frac{1}{n}\sum\_{i=1}^{n}\left[g(\bm{z}\_{i})-\mathbb{E}g(\bm{z}\_{i})\right]. Adapting the proof of Theorem 4 in Mas00, with probability at least 1−δ1-\delta,

|  |  |  |
| --- | --- | --- |
|  | Z−𝔼​Z≲log⁡(1/δ)n​(v+(b−a)​𝔼​Z)+(b−a)​log⁡(1/δ)n,Z-\mathbb{E}Z\lesssim\sqrt{\frac{\log(1/\delta)}{n}\left(v+(b-a)\mathbb{E}Z\right)}+\frac{(b-a)\log(1/\delta)}{n}, |  |

where ≲\lesssim hides a universal constant. By Young’s inequality, for every α>0\alpha>0,

|  |  |  |
| --- | --- | --- |
|  | log⁡(1/δ)n​(b−a)​𝔼​Z≤α​𝔼​Z+α−1​(b−a)​log⁡(1/δ)n.\sqrt{\frac{\log(1/\delta)}{n}(b-a)\mathbb{E}Z}\leq\alpha\mathbb{E}Z+\alpha^{-1}\frac{(b-a)\log(1/\delta)}{n}. |  |

By Rademacher symmetrization (e.g., Lemma A.5 in BBM05), for i.i.d. Rademacher random variables ε1,…,εn\varepsilon\_{1},...,\varepsilon\_{n} independent of 𝒛1,…,𝒛n\bm{z}\_{1},...,\bm{z}\_{n}, it holds that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​Z≤2​𝔼​[supg∈𝒢1n​∑i=1nεi​g​(𝒛i)]=2​ℜ​(𝒢;{𝒛i}i=1n).\mathbb{E}Z\leq 2\mathbb{E}\left[\sup\_{g\in\mathcal{G}}\frac{1}{n}\sum\_{i=1}^{n}\varepsilon\_{i}g(\bm{z}\_{i})\right]=2\mathfrak{R}(\mathcal{G};\{\bm{z}\_{i}\}\_{i=1}^{n}). |  |

This completes the proof.
∎

By LABEL:sm:lem-uniform-concentration, each of the following inequalities holds with probability at least 1−δ1-\delta:

|  |  |  |
| --- | --- | --- |
|  | Vr+≲infα>0{(1+α)​ℜ​(𝒢r;{𝒛i}i=1n)+v​log⁡(1/δ)n+(1+α−1)​(b−a)​log⁡(1/δ)n},V\_{r}^{+}\lesssim\inf\_{\alpha>0}\left\{(1+\alpha)\mathfrak{R}(\mathcal{G}\_{r};\{\bm{z}\_{i}\}\_{i=1}^{n})+\sqrt{\frac{v\log(1/\delta)}{n}}+(1+\alpha^{-1})\frac{(b-a)\log(1/\delta)}{n}\right\}, |  |

The rest of the proof follows that in Section 3.2 of BBM05.

### C.4 Proof of LABEL:sm:lem-noise-condition-regression

Recall that for 𝒛=(𝒙,y)\bm{z}=(\bm{x},y), we define ℓf​(𝒛)=[f​(𝒙)−y]2\ell\_{f}(\bm{z})=[f(\bm{x})-y]^{2}. Then

|  |  |  |
| --- | --- | --- |
|  | 1mt,k​∑j=t−kt−1mj​var𝒛∼Pj⁡[ℓf​(𝒛)−ℓf¯​(𝒛)]\displaystyle\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\operatorname{{\rm var}}\_{\bm{z}\sim P\_{j}}\left[\ell\_{f}(\bm{z})-\ell\_{\bar{f}}(\bm{z})\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =1mt,k​∑j=t−kt−1mj​var(𝒙,y)∼Pj⁡[(f​(𝒙)−y)2−(f¯​(𝒙)−y)2]\displaystyle\qquad=\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\operatorname{{\rm var}}\_{(\bm{x},y)\sim P\_{j}}\left[\big(f(\bm{x})-y\big)^{2}-\big(\bar{f}(\bm{x})-y\big)^{2}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤1mt,k​∑j=t−kt−1mj​𝔼(𝒙,y)∼Pj​{[(f​(𝒙)−y)2−(f¯​(𝒙)−y)2]2}\displaystyle\qquad\leq\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\mathbb{E}\_{(\bm{x},y)\sim P\_{j}}\left\{\left[\big(f(\bm{x})-y\big)^{2}-\big(\bar{f}(\bm{x})-y\big)^{2}\right]^{2}\right\} |  |
|  |  |  |
| --- | --- | --- |
|  | =1mt,k​∑j=t−kt−1mj​𝔼(𝒙,y)∼Pj​[(f​(𝒙)−f¯​(𝒙))2​(f​(𝒙)+f¯​(𝒙)−2​y)2]\displaystyle\qquad=\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\mathbb{E}\_{(\bm{x},y)\sim P\_{j}}\left[\big(f(\bm{x})-\bar{f}(\bm{x})\big)^{2}\big(f(\bm{x})+\bar{f}(\bm{x})-2y\big)^{2}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤16​M2⋅1mt,k​∑j=t−kt−1mj​𝔼(𝒙,y)∼Pj​[(f​(𝒙)−f¯​(𝒙))2]=16​M2⋅1mt,k​∑j=t−kt−1mj​‖f−f¯‖j2\displaystyle\qquad\leq 16M^{2}\cdot\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\mathbb{E}\_{(\bm{x},y)\sim P\_{j}}\left[\left(f(\bm{x})-\bar{f}(\bm{x})\right)^{2}\right]=16M^{2}\cdot\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\|f-\bar{f}\|\_{j}^{2} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤32​M2⋅1mt,k​∑j=t−kt−1mj​(‖f−fj∗‖j2+‖f¯−fj∗‖j2)\displaystyle\qquad\leq 32M^{2}\cdot\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\left(\|f-f\_{j}^{\*}\|\_{j}^{2}+\|\bar{f}-f\_{j}^{\*}\|\_{j}^{2}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =32​M2⋅1mt,k​∑j=t−kt−1mj​{𝔼𝒛∼Pj​[ℓf​(𝒛)−ℓf¯​(𝒛)]+2​ℰj​(f¯)}.\displaystyle\qquad=32M^{2}\cdot\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}m\_{j}\left\{\mathbb{E}\_{\bm{z}\sim P\_{j}}\left[\ell\_{f}(\bm{z})-\ell\_{\bar{f}}(\bm{z})\right]+2\mathcal{E}\_{j}(\bar{f})\right\}. |  |

This finishes the proof.

### C.5 Proofs for LABEL:sm:eg-finite-class, LABEL:sm:eg-linear and LABEL:sm:eg-kernel

LABEL:sm:eg-finite-class follows from the result below. If is an immediate extension of Proposition 6.1 and Lemma D.1 in DJL21 to independent samples with non-identical distributions. The proof is omitted.

###### Lemma C.5.

Let 𝐳1,…,𝐳n\bm{z}\_{1},...,\bm{z}\_{n} be independent random variables taking values in 𝒳\mathcal{X}, and let ε1,…,εn\varepsilon\_{1},...,\varepsilon\_{n} be i.i.d. Rademacher random variables independent of {𝐳i}i=1n\{\bm{z}\_{i}\}\_{i=1}^{n}. Let ℱ\mathcal{F} be a finite class of functions from 𝒳\mathcal{X} to [−M,M][-M,M]. Take an arbitrary function f¯:𝒳→[−M,M]\bar{f}:\mathcal{X}\to[-M,M]. For r≥0r\geq 0, define

|  |  |  |
| --- | --- | --- |
|  | ℛ​(r)=𝔼​max⁡{1n​∑i=1nεi​f​(𝒛i):f∈ℱ,1n​∑i=1n𝔼​[(f​(𝒛i)−f¯​(𝒛i))2]≤r}.\mathcal{R}(r)=\mathbb{E}\max\left\{\frac{1}{n}\sum\_{i=1}^{n}\varepsilon\_{i}f(\bm{z}\_{i}):f\in\mathcal{F},~\frac{1}{n}\sum\_{i=1}^{n}\mathbb{E}\left[\left(f(\bm{z}\_{i})-\bar{f}(\bm{z}\_{i})\right)^{2}\right]\leq r\right\}. |  |

Then for every r≥0r\geq 0,

|  |  |  |
| --- | --- | --- |
|  | ℛ​(r)≤2​max⁡{r​log⁡|ℱ|n,2​M​log⁡|ℱ|n}.\mathcal{R}(r)\leq 2\max\left\{\sqrt{\frac{r\log|\mathcal{F}|}{n}},\frac{2M\log|\mathcal{F}|}{n}\right\}. |  |

Moreover, the function on the right hand side is subroot, and has a unique fixed point

|  |  |  |
| --- | --- | --- |
|  | r=4​max⁡{M,1}​log⁡|ℱ|n.r=\frac{4\max\{M,1\}\log|\mathcal{F}|}{n}. |  |

To obtain the results in LABEL:sm:eg-linear and LABEL:sm:eg-kernel, we invoke a useful lemma. It is an extension of Theorem 41 in Men02 to the non-i.i.d. case. The proof is omitted.

###### Lemma C.6.

Take 𝛉¯∈B​(𝟎,M)⊆ℝd\bar{\bm{\theta}}\in B(\bm{0},\sqrt{M})\subseteq\mathbb{R}^{d}. Suppose 𝐱i∼Qi\bm{x}\_{i}\sim Q\_{i}, i∈[n]i\in[n] are independent random vectors in ℝd\mathbb{R}^{d}. Let ε1,…,εn\varepsilon\_{1},...,\varepsilon\_{n} be i.i.d. Rademacher random variables independent of {𝐱i}i=1n\{\bm{x}\_{i}\}\_{i=1}^{n}. For r≥0r\geq 0, define

|  |  |  |
| --- | --- | --- |
|  | ℛ​(r)=𝔼​sup{1n​∑i=1nεi​𝒙i⊤​𝜽:1n​∑i=1n𝔼​[(𝒙i⊤​(𝜽−𝜽¯))2]≤r,‖𝜽‖22≤M}.\mathcal{R}(r)=\mathbb{E}\sup\left\{\frac{1}{n}\sum\_{i=1}^{n}\varepsilon\_{i}\bm{x}\_{i}^{\top}\bm{\theta}:\frac{1}{n}\sum\_{i=1}^{n}\mathbb{E}\left[\big(\bm{x}\_{i}^{\top}(\bm{\theta}-\bar{\bm{\theta}})\big)^{2}\right]\leq r,~\|\bm{\theta}\|\_{2}^{2}\leq M\right\}. |  |

Let 𝚺=1n​∑i=1n𝔼​(𝐱i​𝐱i⊤)\bm{\Sigma}=\frac{1}{n}\sum\_{i=1}^{n}\mathbb{E}(\bm{x}\_{i}\bm{x}\_{i}^{\top}), and denote by {λi}i=1d\{\lambda\_{i}\}\_{i=1}^{d} its eigenvalues sorted in descending order. Then

|  |  |  |
| --- | --- | --- |
|  | ℛ​(r)≤cn​∑i=1dmin⁡{r,M​λi}.\mathcal{R}(r)\leq\sqrt{\frac{c}{n}\sum\_{i=1}^{d}\min\{r,M\lambda\_{i}\}}. |  |

The above lemma leads to ℛ​(r)≤c​r​d/n\mathcal{R}(r)\leq\sqrt{crd/n}.
The right-hand side is subroot and has a unique fixed point r=c​d/nr=cd/n. This verifies LABEL:sm:eg-linear.

To get LABEL:sm:eg-kernel, we apply [Lemma˜C.6](https://arxiv.org/html/2512.23596v1#A3.Thmlemma6 "Lemma C.6. ‣ C.5 Proofs for , and ‣ Appendix C Theoretical Analysis of Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction") to the transformed features ϕ​(𝒙j,i)\phi(\bm{x}\_{j,i}) rather than the raw ones. Correspondingly, the feature space becomes ℍ\mathbb{H}, and the matrix 𝚺\bm{\Sigma} in LABEL:sm:eg-kernel becomes
1mt,k​∑j=t−kt−1∑i=1mj𝔼​[ϕ​(𝒙j,i)⊗ϕ​(𝒙j,i)]\frac{1}{m\_{t,k}}\sum\_{j=t-k}^{t-1}\sum\_{i=1}^{m\_{j}}\mathbb{E}[\phi(\bm{x}\_{j,i})\otimes\phi(\bm{x}\_{j,i})]. Here ⊗\otimes denotes the tensor product.

In LABEL:sm:eg-kernel, the assumption regarding the trace-class operator 𝑺\bm{S} forces 𝚺⪯𝑺\bm{\Sigma}\preceq\bm{S}.
Then, [Lemma˜C.6](https://arxiv.org/html/2512.23596v1#A3.Thmlemma6 "Lemma C.6. ‣ C.5 Proofs for , and ‣ Appendix C Theoretical Analysis of Nonstationarity-Complexity Tradeoff ‣ The nonstationarity-complexity tradeoff in return prediction") yields

|  |  |  |
| --- | --- | --- |
|  | ℛ​(r)≲1mt,k​∑i=1∞min⁡{r,μi}≤1mt,k​mins≥1⁡s​r+∑i=s+1∞μi,\mathcal{R}(r)\lesssim\sqrt{\frac{1}{m\_{t,k}}\sum\_{i=1}^{\infty}\min\{r,\mu\_{i}\}}\leq\frac{1}{\sqrt{m\_{t,k}}}\min\_{s\geq 1}\sqrt{sr+\sum\_{i=s+1}^{\infty}\mu\_{i}}, |  |

where ≲\lesssim hides a constant factor.

* •

  If there are constants c1,c2>0c\_{1},c\_{2}>0 such that μk≤c1​e−c2​k\mu\_{k}\leq c\_{1}e^{-c\_{2}k} holds for all kk, then
  ∑i=s+1∞μi≲e−c2​s\sum\_{i=s+1}^{\infty}\mu\_{i}\lesssim e^{-c\_{2}s}. Taking s=⌈c2−1​log⁡(1/r)⌉s=\lceil c\_{2}^{-1}\log(1/r)\rceil, we get

  |  |  |  |
  | --- | --- | --- |
  |  | ℛ​(r)≲1mt,k​r​⌈c2−1​log⁡(1/r)+1⌉.\mathcal{R}(r)\lesssim\frac{1}{\sqrt{m\_{t,k}}}\sqrt{r\lceil c\_{2}^{-1}\log(1/r)+1\rceil}. |  |

  The right-hand side is sub-root. Elementary calculation yields
  rt,k​(ℱ)≲(log⁡mt,k)/mt,kr\_{t,k}(\mathcal{F})\lesssim(\log m\_{t,k})/m\_{t,k}
* •

  If there are constants c>0c>0 and α≥1\alpha\geq 1 such that μk≤c​k−2​α\mu\_{k}\leq ck^{-2\alpha} holds for all kk, then
  ∑i=s+1∞μi≲s1−2​α\sum\_{i=s+1}^{\infty}\mu\_{i}\lesssim s^{1-2\alpha}. Taking s=⌈r−1/(2​α)⌉s=\lceil r^{-1/(2\alpha)}\rceil, we get

  |  |  |  |
  | --- | --- | --- |
  |  | ℛ​(r)≲r1−1/(2​α)mt,k.\mathcal{R}(r)\lesssim\sqrt{\frac{r^{1-1/(2\alpha)}}{m\_{t,k}}}. |  |

  The right-hand side is sub-root. Then, we can easily get
  rt,k​(ℱ)≲mt,k−2​α2​α+1r\_{t,k}(\mathcal{F})\lesssim m\_{t,k}^{-\frac{2\alpha}{2\alpha+1}}.

## Appendix D Proofs for LABEL:sm:sec-select and LABEL:sm:sec-select-R2

### D.1 Proof of LABEL:sm:lem-complexity-tournament

Given two models f,f′∈ℱf,f^{\prime}\in\mathcal{F}, denote the output of 𝒜\mathcal{A} by 𝒜​(f,f′)∈{f,f′}\mathcal{A}(f,f^{\prime})\in\{f,f^{\prime}\}. Let T​(Λ)T(\Lambda) be the maximum expected number of times LABEL:sm:alg-tournament can call 𝒜\mathcal{A} after there are Λ\Lambda remaining models {fλ}λ=1Λ\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda} at the end of a while loop, where the maximum is taken over all possible choices of {fλ}λ=1Λ\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda}. Then T​(Λ)T(\Lambda) is increasing in Λ\Lambda, and T​(Λ)≤Λ2/2T(\Lambda)\leq\Lambda^{2}/2. Let NN denote the number of remaining models at the end of the next while loop. Since that while loop calls 𝒜\mathcal{A} at most Λ−1\Lambda-1 times, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​(Λ)≤(Λ−1)+𝔼​[T​(N)].T(\Lambda)\leq(\Lambda-1)+\mathbb{E}\left[T(N)\right]. |  | (D.1) |

For each λ∈[Λ]\lambda\in[\Lambda], let nλ=|{λ′∈[Λ]\{λ}:𝒜​(fλ,fλ′)=fλ′}|n\_{\lambda}=|\{\lambda^{\prime}\in[\Lambda]\backslash\{\lambda\}:\mathcal{A}(f\_{\lambda},f\_{\lambda^{\prime}})=f\_{\lambda^{\prime}}\}| be the number of remaining models that would beat fλf\_{\lambda} if they were paired. Since LABEL:sm:alg-tournament chooses each fλf\_{\lambda} as the pivot model uniformly at random, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[T​(N)]=𝔼​[1Λ​∑λ=1ΛT​(nλ)].\mathbb{E}\left[T(N)\right]=\mathbb{E}\left[\frac{1}{\Lambda}\sum\_{\lambda=1}^{\Lambda}T(n\_{\lambda})\right]. |  | (D.2) |

Since ∑λ=1Λnλ\sum\_{\lambda=1}^{\Lambda}n\_{\lambda} counts exactly one of (fλ,fλ′)(f\_{\lambda},f\_{\lambda^{\prime}}) and (fλ′,fλ)(f\_{\lambda^{\prime}},f\_{\lambda}) for all λ≠λ′\lambda\neq\lambda^{\prime}, then ∑λ=1Λnλ=Λ​(Λ−1)/2\sum\_{\lambda=1}^{\Lambda}n\_{\lambda}=\Lambda(\Lambda-1)/2. Let n(1)≤⋯≤n(Λ)n\_{(1)}\leq\cdots\leq n\_{(\Lambda)} be the order statistics of n1,…,nΛn\_{1},...,n\_{\Lambda}. Then for all i=1,…,⌈Λ/3⌉i=1,...,\lceil\Lambda/3\rceil,

|  |  |  |
| --- | --- | --- |
|  | n(i)≤n(⌈Λ/3⌉)≤1Λ−⌈Λ/3⌉+1​∑i=⌈Λ/3⌉Λni≤32​Λ⋅Λ​(Λ−1)2=3​(Λ−1)4.n\_{(i)}\leq n\_{(\lceil\Lambda/3\rceil)}\leq\frac{1}{\Lambda-\lceil\Lambda/3\rceil+1}\sum\_{i=\lceil\Lambda/3\rceil}^{\Lambda}n\_{i}\leq\frac{3}{2\Lambda}\cdot\frac{\Lambda(\Lambda-1)}{2}=\frac{3(\Lambda-1)}{4}. |  |

By the monotonicity of TT,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1Λ​∑λ=1ΛT​(nλ)=1Λ​∑i=1ΛT​(n(i))\displaystyle\frac{1}{\Lambda}\sum\_{\lambda=1}^{\Lambda}T(n\_{\lambda})=\frac{1}{\Lambda}\sum\_{i=1}^{\Lambda}T(n\_{(i)}) | ≤1Λ(⌊Λ/3⌋T(⌈3Λ/4⌉)+(Λ−⌊Λ/3⌋)T(Λ−1)]\displaystyle\leq\frac{1}{\Lambda}\bigg(\lfloor\Lambda/3\rfloor T(\lceil 3\Lambda/4\rceil)+\left(\Lambda-\lfloor\Lambda/3\rfloor\right)T(\Lambda-1)\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤13​T​(⌈3​Λ/4⌉)+(23+1Λ)​T​(Λ)\displaystyle\leq\frac{1}{3}T(\lceil 3\Lambda/4\rceil)+\left(\frac{2}{3}+\frac{1}{\Lambda}\right)T(\Lambda) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤13​T​(⌈3​Λ/4⌉)+23​T​(Λ)+Λ.\displaystyle\leq\frac{1}{3}T(\lceil 3\Lambda/4\rceil)+\frac{2}{3}T(\Lambda)+\Lambda. |  |

Substituting this into ([D.2](https://arxiv.org/html/2512.23596v1#A4.E2 "Equation D.2 ‣ D.1 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) and ([D.1](https://arxiv.org/html/2512.23596v1#A4.E1 "Equation D.1 ‣ D.1 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) gives

|  |  |  |
| --- | --- | --- |
|  | T​(Λ)≤6​Λ+T​(⌈3​Λ/4⌉).T(\Lambda)\leq 6\Lambda+T(\lceil 3\Lambda/4\rceil). |  |

By the Master Theorem (Theorem 4.1) in CLRS22, we conclude that T​(Λ)=Θ​(Λ)T(\Lambda)=\Theta(\Lambda).

### D.2 Proof of LABEL:sm:thm-model-comparison

We will prove the following stronger result: with probability at least 1−δ1-\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰt​(f^)−ℰt​(f2)≲M​log⁡(t/δ)⋅(maxt−ℓ≤j≤t−1⁡TV⁡(Pj,Pt)+1nt,ℓ)1/2.\sqrt{\mathcal{E}\_{t}(\widehat{f})}-\sqrt{\mathcal{E}\_{t}(f\_{2})}\lesssim M\sqrt{\log(t/\delta)}\cdot\left(\max\_{t-\ell\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})+\frac{1}{n\_{t,\ell}}\right)^{1/2}. |  | (D.3) |

The bound in LABEL:sm:thm-model-comparison is obtained by squaring both sides of ([D.3](https://arxiv.org/html/2512.23596v1#A4.E3 "Equation D.3 ‣ D.2 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")).

Without loss of generality, assume Lt​(f1)≥Lt​(f2)L\_{t}(f\_{1})\geq L\_{t}(f\_{2}), so minλ∈[2]⁡Lt​(fλ)=Lt​(f2)\min\_{\lambda\in[2]}L\_{t}(f\_{\lambda})=L\_{t}(f\_{2}). By Theorem 4.2 in HHW24, with probability at least 1−δ1-\delta, LABEL:sm:alg-compare outputs a model f^\widehat{f} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt​(f^)−Lt​(f2)\displaystyle L\_{t}(\widehat{f})-L\_{t}(f\_{2}) | ≤|Δ^t,ℓ^−Δt|\displaystyle\leq|\widehat{\Delta}\_{t,\widehat{\ell}}-\Delta\_{t}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≲minℓ∈[t−1]⁡{log⁡(t/δ)⋅maxt−ℓ≤j≤t−1⁡|Δj−Δt|+σt,ℓ​log⁡(t/δ)nt,ℓ+M2​log⁡(t/δ)nt,ℓ},\displaystyle\lesssim\min\_{\ell\in[t-1]}\left\{\sqrt{\log(t/\delta)}\cdot\max\_{t-\ell\leq j\leq t-1}|\Delta\_{j}-\Delta\_{t}|+\sigma\_{t,\ell}\sqrt{\frac{\log(t/\delta)}{n\_{t,\ell}}}+\frac{M^{2}\log(t/\delta)}{n\_{t,\ell}}\right\}, |  |

where ≲\lesssim hides a universal constant. When this event happens, it holds for all ℓ∈[t−1]\ell\in[t-1] that

|  |  |  |
| --- | --- | --- |
|  | Lt​(f^)−Lt​(f2)≲log⁡(t/δ)⋅maxt−ℓ≤j≤t−1⁡|Δj−Δt|+σt,ℓ​log⁡(t/δ)nt,ℓ+M2​log⁡(t/δ)nt,ℓ.L\_{t}(\widehat{f})-L\_{t}(f\_{2})\lesssim\sqrt{\log(t/\delta)}\cdot\max\_{t-\ell\leq j\leq t-1}|\Delta\_{j}-\Delta\_{t}|+\sigma\_{t,\ell}\sqrt{\frac{\log(t/\delta)}{n\_{t,\ell}}}+\frac{M^{2}\log(t/\delta)}{n\_{t,\ell}}. |  |

When f^=f2\widehat{f}=f\_{2}, ([D.3](https://arxiv.org/html/2512.23596v1#A4.E3 "Equation D.3 ‣ D.2 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) automatically holds and there is nothing to prove.

Now consider the case when f^=f1\widehat{f}=f\_{1}. Fix ℓ∈[t−1]\ell\in[t-1]. Define

|  |  |  |
| --- | --- | --- |
|  | ℰt,ℓva​(f)=1nt,ℓ​∑j=t−ℓt−1nj​[Lj​(f)−Lj​(fj∗)].\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f)=\frac{1}{n\_{t,\ell}}\sum\_{j=t-\ell}^{t-1}n\_{j}\big[L\_{j}(f)-L\_{j}(f\_{j}^{\*})\big]. |  |

Since

|  |  |  |
| --- | --- | --- |
|  | |[ℰt,ℓva​(f1)−ℰt,ℓva​(f2)]−[Lt​(f1)−Lt​(f2)]|≤maxt−ℓ≤j≤t−1⁡|Δj−Δt|,\left|\big[\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{1})-\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{2})\big]-\big[L\_{t}(f\_{1})-L\_{t}(f\_{2})\big]\right|\leq\max\_{t-\ell\leq j\leq t-1}|\Delta\_{j}-\Delta\_{t}|, |  |

then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰt,ℓva​(f1)−ℰt,ℓva​(f2)\displaystyle\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{1})-\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{2}) | ≤Lt​(f1)−Lt​(f2)+maxt−ℓ≤j≤t−1⁡|Δj−Δt|\displaystyle\leq L\_{t}(f\_{1})-L\_{t}(f\_{2})+\max\_{t-\ell\leq j\leq t-1}|\Delta\_{j}-\Delta\_{t}| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤C​[log⁡(t/δ)⋅maxt−ℓ≤j≤t−1⁡|Δj−Δt|+σt,ℓ​log⁡(t/δ)nt,ℓ+M2​log⁡(t/δ)nt,ℓ]\displaystyle\leq C\left[\sqrt{\log(t/\delta)}\cdot\max\_{t-\ell\leq j\leq t-1}|\Delta\_{j}-\Delta\_{t}|+\sigma\_{t,\ell}\sqrt{\frac{\log(t/\delta)}{n\_{t,\ell}}}+\frac{M^{2}\log(t/\delta)}{n\_{t,\ell}}\right] |  | (D.4) |

for some universal constant C≥1C\geq 1. The variance term σt,ℓ2\sigma\_{t,\ell}^{2} can be bounded by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σt,ℓ2\displaystyle\sigma\_{t,\ell}^{2} | =1nt,ℓ​∑j=t−ℓt−1nj​var(𝒙,y)∼Pj⁡[(f1​(𝒙)−y)2−(f2​(𝒙)−y)2]\displaystyle=\frac{1}{n\_{t,\ell}}\sum\_{j=t-\ell}^{t-1}n\_{j}\operatorname{{\rm var}}\_{(\bm{x},y)\sim P\_{j}}\left[\big(f\_{1}(\bm{x})-y\big)^{2}-\big(f\_{2}(\bm{x})-y\big)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​∑λ=12[1nt,ℓ​∑j=t−ℓt−1nj​var(𝒙,y)∼Pj⁡[(fλ​(𝒙)−y)2−(fj∗​(𝒙)−y)2]].\displaystyle\leq 2\sum\_{\lambda=1}^{2}\left[\frac{1}{n\_{t,\ell}}\sum\_{j=t-\ell}^{t-1}n\_{j}\operatorname{{\rm var}}\_{(\bm{x},y)\sim P\_{j}}\left[\big(f\_{\lambda}(\bm{x})-y\big)^{2}-\big(f\_{j}^{\*}(\bm{x})-y\big)^{2}\right]\right]. |  |

For each λ∈[2]\lambda\in[2] and j∈ℤ+j\in\mathbb{Z}\_{+},

|  |  |  |  |
| --- | --- | --- | --- |
|  | var(𝒙,y)∼Pj⁡[(fλ​(𝒙)−y)2−(fj∗​(𝒙)−y)2]\displaystyle\operatorname{{\rm var}}\_{(\bm{x},y)\sim P\_{j}}\left[\big(f\_{\lambda}(\bm{x})-y\big)^{2}-\big(f\_{j}^{\*}(\bm{x})-y\big)^{2}\right] | ≤𝔼(𝒙,y)∼Pj​{[(fλ​(𝒙)−y)2−(fj∗​(𝒙)−y)2]2}\displaystyle\leq\mathbb{E}\_{(\bm{x},y)\sim P\_{j}}\left\{\left[\big(f\_{\lambda}(\bm{x})-y\big)^{2}-\big(f\_{j}^{\*}(\bm{x})-y\big)^{2}\right]^{2}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼(𝒙,y)∼Pj​[(fλ​(𝒙)−fj∗​(𝒙))2​(fλ+fj∗​(𝒙)−2​y)2]\displaystyle=\mathbb{E}\_{(\bm{x},y)\sim P\_{j}}\left[\big(f\_{\lambda}(\bm{x})-f\_{j}^{\*}(\bm{x})\big)^{2}\big(f\_{\lambda}+f\_{j}^{\*}(\bm{x})-2y\big)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤16​M2​𝔼(𝒙,y)∼Pj​[(fλ​(𝒙)−fj∗​(𝒙))2]\displaystyle\leq 16M^{2}\mathbb{E}\_{(\bm{x},y)\sim P\_{j}}\left[\big(f\_{\lambda}(\bm{x})-f\_{j}^{\*}(\bm{x})\big)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =16​M2​ℰj​(fλ).\displaystyle=16M^{2}\mathcal{E}\_{j}(f\_{\lambda}). |  |

Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | σt,ℓ2≤32​M2⋅∑λ=12[1nt,ℓ​∑j=t−ℓt−1nj​ℰj​(fλ)]=32​M2​[ℰt,ℓva​(f1)+ℰt,ℓva​(f2)].\sigma\_{t,\ell}^{2}\leq 32M^{2}\cdot\sum\_{\lambda=1}^{2}\left[\frac{1}{n\_{t,\ell}}\sum\_{j=t-\ell}^{t-1}n\_{j}\mathcal{E}\_{j}(f\_{\lambda})\right]=32M^{2}\big[\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{1})+\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{2})\big]. |  | (D.5) |

Substituting ([D.5](https://arxiv.org/html/2512.23596v1#A4.E5 "Equation D.5 ‣ D.2 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) into ([D.4](https://arxiv.org/html/2512.23596v1#A4.E4 "Equation D.4 ‣ D.2 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) yields

|  |  |  |
| --- | --- | --- |
|  | ℰt,ℓva​(f1)−ℰt,ℓva​(f2)≤2​A​(ℰt,ℓva​(f1)+ℰt,ℓva​(f2))+D,\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{1})-\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{2})\leq 2A\left(\sqrt{\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{1})}+\sqrt{\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{2})}\,\right)+D, |  |

where

|  |  |  |
| --- | --- | --- |
|  | A=2​2​C​M​log⁡(t/δ)nt,ℓandD=C​[log⁡(t/δ)​maxt−ℓ≤j≤t−1⁡|Δj−Δt|+M2​log⁡(t/δ)nt,ℓ]A=2\sqrt{2}CM\sqrt{\frac{\log(t/\delta)}{n\_{t,\ell}}}\quad\text{and}\quad D=C\left[\sqrt{\log(t/\delta)}\max\_{t-\ell\leq j\leq t-1}|\Delta\_{j}-\Delta\_{t}|+\frac{M^{2}\log(t/\delta)}{n\_{t,\ell}}\right] |  |

Completing the squares gives

|  |  |  |
| --- | --- | --- |
|  | (ℰt,ℓva​(f1)−A)2≤(ℰt,ℓva​(f2)+A)2+D,\left(\sqrt{\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{1})}-A\right)^{2}\leq\left(\sqrt{\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{2})}+A\right)^{2}+D, |  |

which implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰt,ℓva​(f1)−ℰt,ℓva​(f2)\displaystyle\sqrt{\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{1})}-\sqrt{\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{2})} | ≤2​A+D\displaystyle\leq 2A+\sqrt{D} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≲M​log⁡(t/δ)nt,ℓ+[log⁡(t/δ)​maxt−ℓ≤j≤t−1⁡|Δj−Δt|+M2​log⁡(t/δ)nt,ℓ]1/2\displaystyle\lesssim M\sqrt{\frac{\log(t/\delta)}{n\_{t,\ell}}}+\left[\sqrt{\log(t/\delta)}\max\_{t-\ell\leq j\leq t-1}|\Delta\_{j}-\Delta\_{t}|+\frac{M^{2}\log(t/\delta)}{n\_{t,\ell}}\right]^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≲log⁡(t/δ)⋅(maxt−ℓ≤j≤t−1⁡|Δj−Δt|+M2nt,ℓ)1/2\displaystyle\lesssim\sqrt{\log(t/\delta)}\cdot\left(\max\_{t-\ell\leq j\leq t-1}|\Delta\_{j}-\Delta\_{t}|+\frac{M^{2}}{n\_{t,\ell}}\right)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≲M​log⁡(t/δ)⋅(maxt−ℓ≤j≤t−1⁡TV⁡(Pj,Pt)+1nt,ℓ)1/2,\displaystyle\lesssim M\sqrt{\log(t/\delta)}\cdot\left(\max\_{t-\ell\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})+\frac{1}{n\_{t,\ell}}\right)^{1/2}, |  |

where the last inequality is due to

|  |  |  |
| --- | --- | --- |
|  | |Δj−Δt|≲M2⋅TV⁡(Pj,Pt).|\Delta\_{j}-\Delta\_{t}|\lesssim M^{2}\cdot\operatorname{TV}(P\_{j},P\_{t}). |  |

Finally, by LABEL:sm:lem-risk-to-TV, for every f∈{f1,f2}f\in\{f\_{1},f\_{2}\},

|  |  |  |
| --- | --- | --- |
|  | |ℰt,ℓva​(f)−ℰt​(f)|≤|ℰt,ℓva​(f)−ℰt​(f)|≤maxt−ℓ≤j≤t−1⁡|ℰj​(f)−ℰt​(f)|≤2​M​maxt−ℓ≤j≤t−1⁡TV⁡(Pj,Pt),\displaystyle\left|\sqrt{\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f)}-\sqrt{\mathcal{E}\_{t}(f)}\right|\leq\sqrt{\big|\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f)-\mathcal{E}\_{t}(f)\big|}\leq\max\_{t-\ell\leq j\leq t-1}\sqrt{\big|\mathcal{E}\_{j}(f)-\mathcal{E}\_{t}(f)\big|}\leq 2M\max\_{t-\ell\leq j\leq t-1}\sqrt{\operatorname{TV}(P\_{j},P\_{t})}, |  |

so

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰt​(f1)−ℰt​(f2)\displaystyle\sqrt{\mathcal{E}\_{t}(f\_{1})}-\sqrt{\mathcal{E}\_{t}(f\_{2})} | ≤ℰt,ℓva​(f1)−ℰt,ℓva​(f2)+4​M​maxt−ℓ≤j≤t−1⁡TV⁡(Pj,Pt)\displaystyle\leq\sqrt{\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{1})}-\sqrt{\mathcal{E}\_{t,\ell}^{\operatorname{\mathrm{va}}}(f\_{2})}+4M\max\_{t-\ell\leq j\leq t-1}\sqrt{\operatorname{TV}(P\_{j},P\_{t})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≲M​log⁡(t/δ)⋅(maxt−ℓ≤j≤t−1⁡TV⁡(Pj,Pt)+1nt,ℓ)1/2.\displaystyle\lesssim M\sqrt{\log(t/\delta)}\cdot\left(\max\_{t-\ell\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})+\frac{1}{n\_{t,\ell}}\right)^{1/2}. |  |

As f^=f1\widehat{f}=f\_{1}, this finishes the proof.

### D.3 Proof of LABEL:sm:thm-select-tournament

We first prove the following lemma, which converts any performance guarantee of the subroutine 𝒜\mathcal{A} to that of LABEL:sm:alg-tournament.

###### Lemma D.1 (From comparison to selection).

Take a performance metric ℒ:{fλ}λ=1Λ→ℝ\mathcal{L}:\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda}\to\mathbb{R}, and U:(0,1)→ℝ+U:(0,1)\to\mathbb{R}\_{+}. Fix δ∈(0,1)\delta\in(0,1). Suppose that the model comparison subroutine 𝒜\mathcal{A} in LABEL:sm:alg-tournament satisfies the following property: given two models h1,h2∈{fλ}λ=1Λh\_{1},h\_{2}\in\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda}, it outputs a model h^∈{h1,h2}\widehat{h}\in\{h\_{1},h\_{2}\} satisfying

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ℒ​(h^)−min⁡{ℒ​(h1),ℒ​(h2)}≤U​(δ))≥1−δ.\mathbb{P}\left(\mathcal{L}(\widehat{h})-\min\left\{\mathcal{L}(h\_{1}),\mathcal{L}(h\_{2})\right\}\leq U(\delta)\right)\geq 1-\delta. |  |

Then the output f^\widehat{f} of LABEL:sm:alg-tournament satisfies

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ℒ​(f^)−minλ∈[Λ]⁡ℒ​(fλ)≤2​U​(δ))≥1−Λ2​δ.\mathbb{P}\left(\mathcal{L}(\widehat{f})-\min\_{\lambda\in[\Lambda]}\mathcal{L}(f\_{\lambda})\leq 2U(\delta)\right)\geq 1-\Lambda^{2}\delta. |  |

###### Proof of LABEL:sm:lem-select-tournament-reduction.

Given two models f,f′∈ℱf,f^{\prime}\in\mathcal{F}, denote the output of 𝒜\mathcal{A} by 𝒜​(f,f′)∈{f,f′}\mathcal{A}(f,f^{\prime})\in\{f,f^{\prime}\}. For notational convenience we also set 𝒜​(f,f)=f\mathcal{A}(f,f)=f for every f∈ℱf\in\mathcal{F}. By a union bound, with probability at least 1−Λ2​δ1-\Lambda^{2}\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(𝒜​(fλ′,fλ′′))−minλ∈{λ′,λ′′}⁡ℒ​(fλ)≤U​(δ),∀λ′,λ′′∈[Λ].\mathcal{L}\left(\mathcal{A}\big(f\_{\lambda^{\prime}},f\_{\lambda^{\prime\prime}}\big)\right)-\min\_{\lambda\in\{\lambda^{\prime},\lambda^{\prime\prime}\}}\mathcal{L}(f\_{\lambda})\leq U(\delta),\qquad\forall\lambda^{\prime},\lambda^{\prime\prime}\in[\Lambda]. |  | (D.6) |

From now on suppose that ([D.6](https://arxiv.org/html/2512.23596v1#A4.E6 "Equation D.6 ‣ Proof of . ‣ D.3 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) holds. Take f¯∈{fλ}λ=1Λ\bar{f}\in\{f\_{\lambda}\}\_{\lambda=1}^{\Lambda} such that ℒ​(f¯)=minλ∈[Λ]⁡ℒ​(fλ)\mathcal{L}(\bar{f})=\min\_{\lambda\in[\Lambda]}\mathcal{L}(f\_{\lambda}).

If LABEL:sm:alg-tournament outputs f^=f¯\widehat{f}=\bar{f}, then there is nothing to prove. Now assume that f^≠f¯\widehat{f}\neq\bar{f}. Then, there exists ℓ∈ℤ+\ell\in\mathbb{Z}\_{+} such that at the end of the KK-th while loop, f¯\bar{f} is not in S′S^{\prime}. Take the smallest such KK. Let gKg\_{K} denote the pivot model ff during the KK-th while loop, and let SK′S^{\prime}\_{K} denote the set S′S^{\prime} at the end of the KK-th while loop. There are two cases.

1. 1.

   If at the end of the KK-th while loop, SK′=∅S^{\prime}\_{K}=\emptyset and LABEL:sm:alg-tournament outputs f^\widehat{f}, then during this while loop, a call of LABEL:sm:alg-compare has yielded 𝒜​({f^,f¯})=f^\mathcal{A}(\{\widehat{f},\bar{f}\})=\widehat{f}, so by ([D.6](https://arxiv.org/html/2512.23596v1#A4.E6 "Equation D.6 ‣ Proof of . ‣ D.3 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")), ℒ​(f^)−ℒ​(f¯)≤U​(δ)\mathcal{L}(\widehat{f})-\mathcal{L}(\bar{f})\leq U(\delta).
2. 2.

   Otherwise, at the end of the KK-th while loop, SK′≠∅S^{\prime}\_{K}\neq\emptyset. There are two cases.

   1. (a)

      If gK=f¯g\_{K}=\bar{f}, then every f∈SK′f\in S^{\prime}\_{K}, a call of 𝒜\mathcal{A} has yielded 𝒜​({f¯,f})=f\mathcal{A}(\{\bar{f},f\})=f, so by ([D.6](https://arxiv.org/html/2512.23596v1#A4.E6 "Equation D.6 ‣ Proof of . ‣ D.3 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")), ℒ​(f)−ℒ​(f¯)≤U​(δ)\mathcal{L}(f)-\mathcal{L}(\bar{f})\leq U(\delta).
      Since the output f^\widehat{f} must come from SK′S^{\prime}\_{K}, then automatically ℒ​(f^)−ℒ​(f¯)≤U​(δ)\mathcal{L}(\widehat{f})-\mathcal{L}(\bar{f})\leq U(\delta).
   2. (b)

      If gK≠f¯g\_{K}\neq\bar{f}, then for every f∈SK′f\in S^{\prime}\_{K}, a call of 𝒜\mathcal{A} has yielded 𝒜​({gK,f})=f\mathcal{A}(\{g\_{K},f\})=f, so by ([D.6](https://arxiv.org/html/2512.23596v1#A4.E6 "Equation D.6 ‣ Proof of . ‣ D.3 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")),

      |  |  |  |  |
      | --- | --- | --- | --- |
      |  | ℒ​(f)−ℒ​(gK)≤U​(δ).\mathcal{L}(f)-\mathcal{L}(g\_{K})\leq U(\delta). |  | (D.7) |

      Since f¯∉SK′\bar{f}\not\in S^{\prime}\_{K}, then a call of LABEL:sm:alg-compare has yielded 𝒜​({gK,f¯})=gK\mathcal{A}(\{g\_{K},\bar{f}\})=g\_{K}, so by ([D.6](https://arxiv.org/html/2512.23596v1#A4.E6 "Equation D.6 ‣ Proof of . ‣ D.3 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")),

      |  |  |  |  |
      | --- | --- | --- | --- |
      |  | ℒ​(gK)−ℒ​(f¯)≤U​(δ).\mathcal{L}(g\_{K})-\mathcal{L}(\bar{f})\leq U(\delta). |  | (D.8) |

      Putting together ([D.7](https://arxiv.org/html/2512.23596v1#A4.E7 "Equation D.7 ‣ Item 2b ‣ Item 2 ‣ Proof of . ‣ D.3 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) and ([D.8](https://arxiv.org/html/2512.23596v1#A4.E8 "Equation D.8 ‣ Item 2b ‣ Item 2 ‣ Proof of . ‣ D.3 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) yields that for all f∈SK′f\in S^{\prime}\_{K},

      |  |  |  |
      | --- | --- | --- |
      |  | ℒ​(f)≤ℒ​(gK)+U​(δ)≤ℒ​(f¯)+2​U​(δ).\mathcal{L}(f)\leq\mathcal{L}(g\_{K})+U(\delta)\leq\mathcal{L}(\bar{f})+2U(\delta). |  |

      Since the output f^\widehat{f} must come from SK′S^{\prime}\_{K}, then automatically ℒ​(f^)−ℒ​(f¯)≤2​U​(δ)\mathcal{L}(\widehat{f})-\mathcal{L}(\bar{f})\leq 2U(\delta).

In all the cases above, we have ℒ​(f^)−ℒ​(f¯)≤2​U​(δ)\mathcal{L}(\widehat{f})-\mathcal{L}(\bar{f})\leq 2U(\delta).
∎

We now prove LABEL:sm:thm-select-tournament. By the stronger bound ([D.3](https://arxiv.org/html/2512.23596v1#A4.E3 "Equation D.3 ‣ D.2 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) in the proof of LABEL:sm:thm-model-comparison, we can set in LABEL:sm:lem-select-tournament-reduction ℒ​(f)=ℰt​(f)\mathcal{L}(f)=\sqrt{\mathcal{E}\_{t}(f)} and

|  |  |  |
| --- | --- | --- |
|  | U(δ)=CMlog⁡(t/δ)⋅minℓ∈[t−1](maxt−ℓ≤j≤t−1TV(Pj,Pt)+1nt,ℓ)1/2,U(\delta)=CM\sqrt{\log(t/\delta)}\cdot\min\_{\ell\in[t-1]}\left(\max\_{t-\ell\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})+\frac{1}{n\_{t,\ell}}\right)^{1/2}, |  |

for some universal constant C>0C>0. Then, by LABEL:sm:lem-select-tournament-reduction and the choice of δ′\delta^{\prime}, with probability 1−δ1-\delta, the output f^\widehat{f} of LABEL:sm:alg-tournament satisfies

|  |  |  |
| --- | --- | --- |
|  | ℰt​(f^)−minλ∈[Λ]ℰt​(fλ)≲U(δ/Λ2)≲Mlog⁡(Λ​t/δ)⋅minℓ∈[t−1](maxt−ℓ≤j≤t−1TV(Pj,Pt)+1nt,ℓ)1/2.\sqrt{\mathcal{E}\_{t}(\widehat{f})}-\min\_{\lambda\in[\Lambda]}\sqrt{\mathcal{E}\_{t}(f\_{\lambda})}\lesssim U(\delta/\Lambda^{2})\lesssim M\sqrt{\log(\Lambda t/\delta)}\cdot\min\_{\ell\in[t-1]}\left(\max\_{t-\ell\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})+\frac{1}{n\_{t,\ell}}\right)^{1/2}. |  |

Here ≲\lesssim only hides universal constants. This finishes the proof.

### D.4 Proof of LABEL:sm:thm-joint-selection

Recall that |𝒟jtr|=mj|\mathcal{D}\_{j}^{\operatorname{\mathrm{tr}}}|=m\_{j}, |𝒟jva|=nj|\mathcal{D}\_{j}^{\operatorname{\mathrm{va}}}|=n\_{j}, |𝒟j|=mj+nj|\mathcal{D}\_{j}|=m\_{j}+n\_{j}, mt,k=∑j=t−kt−1mjm\_{t,k}=\sum\_{j=t-k}^{t-1}m\_{j}, nt,ℓ=∑j=t−ℓt−1njn\_{t,\ell}=\sum\_{j=t-\ell}^{t-1}n\_{j}, and Bt,k=mt,k+nt,kB\_{t,k}=m\_{t,k}+n\_{t,k}. Since there are (t−1)​|ℱ|(t-1)|\mathscr{F}| candidate models, then by LABEL:sm:thm-select-tournament, with probability at least 1−δ/21-\delta/2, the output f^\widehat{f} of LABEL:sm:alg-tournament satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰt​(f^)≲minℱ∈ℱ,k∈[t−1]⁡ℰt​(h^​(ℱ,k))+M2​log⁡(t2​|ℱ|/δ)⋅minℓ∈[t−1]⁡{maxt−ℓ≤j≤t−1⁡TV⁡(Pj,Pt)+1nt,ℓ}.\mathcal{E}\_{t}(\widehat{f})\lesssim\min\_{\mathcal{F}\in\mathscr{F},\,k\in[t-1]}\mathcal{E}\_{t}\big(\widehat{h}(\mathcal{F},k)\big)+M^{2}\log\big(t^{2}|\mathscr{F}|/\delta\big)\cdot\min\_{\ell\in[t-1]}\left\{\max\_{t-\ell\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})+\frac{1}{n\_{t,\ell}}\right\}. |  | (D.9) |

By LABEL:sm:thm-tradeoff and a union bound, with probability at least 1−δ/21-\delta/2,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰt​(h^​(ℱ,k))≲minf∈ℱ⁡ℰt​(f)+M2​(rt,k​(ℱ)+log⁡(t​|ℱ|/δ)mt,k)+M2​maxt−k≤j≤t−1⁡TV⁡(Pj,Pt).\mathcal{E}\_{t}\big(\widehat{h}(\mathcal{F},k)\big)\lesssim\min\_{f\in\mathcal{F}}\mathcal{E}\_{t}(f)+M^{2}\left(r\_{t,k}(\mathcal{F})+\frac{\log(t|\mathscr{F}|/\delta)}{m\_{t,k}}\right)+M^{2}\max\_{t-k\leq j\leq t-1}\operatorname{TV}\left(P\_{j},P\_{t}\right). |  | (D.10) |

Combining ([D.9](https://arxiv.org/html/2512.23596v1#A4.E9 "Equation D.9 ‣ D.4 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) and ([D.10](https://arxiv.org/html/2512.23596v1#A4.E10 "Equation D.10 ‣ D.4 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) yields that, with probability at least 1−δ1-\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰt​(f^)\displaystyle\mathcal{E}\_{t}(\widehat{f}) | ≲minℱ∈ℱ,k∈[t−1]⁡{minf∈ℱ⁡ℰt​(f)+M2​(rt,k​(ℱ)+log⁡(t​|ℱ|/δ)mt,k)+M2​maxt−k≤j≤t−1⁡TV⁡(Pj,Pt)}\displaystyle\lesssim\min\_{\mathcal{F}\in\mathscr{F},\,k\in[t-1]}\left\{\min\_{f\in\mathcal{F}}\mathcal{E}\_{t}(f)+M^{2}\left(r\_{t,k}(\mathcal{F})+\frac{\log(t|\mathscr{F}|/\delta)}{m\_{t,k}}\right)+M^{2}\max\_{t-k\leq j\leq t-1}\operatorname{TV}\left(P\_{j},P\_{t}\right)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +M2​log⁡(t2​|ℱ|/δ)⋅minℓ∈[t−1]⁡{maxt−ℓ≤j≤t−1⁡TV⁡(Pj,Pt)+1nt,ℓ}\displaystyle\qquad+M^{2}\log\big(t^{2}|\mathscr{F}|/\delta\big)\cdot\min\_{\ell\in[t-1]}\left\{\max\_{t-\ell\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})+\frac{1}{n\_{t,\ell}}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≲minℱ∈ℱ,k∈[t−1]⁡{minf∈ℱ⁡ℰt​(f)+M2​(rt,k​(ℱ)+log⁡(t​|ℱ|/δ)Bt,k)+M2​maxt−k≤j≤t−1⁡TV⁡(Pj,Pt)}\displaystyle\lesssim\min\_{\mathcal{F}\in\mathscr{F},\,k\in[t-1]}\left\{\min\_{f\in\mathcal{F}}\mathcal{E}\_{t}(f)+M^{2}\left(r\_{t,k}(\mathcal{F})+\frac{\log(t|\mathscr{F}|/\delta)}{B\_{t,k}}\right)+M^{2}\max\_{t-k\leq j\leq t-1}\operatorname{TV}\left(P\_{j},P\_{t}\right)\right\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +M2​log⁡(t2​|ℱ|/δ)⋅mink∈[t−1]⁡{maxt−k≤j≤t−1⁡TV⁡(Pj,Pt)+1Bt,k}\displaystyle\qquad+M^{2}\log\big(t^{2}|\mathscr{F}|/\delta\big)\cdot\min\_{k\in[t-1]}\left\{\max\_{t-k\leq j\leq t-1}\operatorname{TV}(P\_{j},P\_{t})+\frac{1}{B\_{t,k}}\right\} |  | (by Assumption LABEL:sm:assumption-data-split) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≲log⁡(t​|ℱ|/δ)⋅minℱ∈ℱ,k∈[t−1]⁡{minf∈ℱ⁡ℰt​(f)+M2​(rt,k​(ℱ)+1Bt,k)+M2​maxt−k≤j≤t−1⁡TV⁡(Pj,Pt)}.\displaystyle\lesssim\log\big(t|\mathscr{F}|/\delta\big)\cdot\min\_{\mathcal{F}\in\mathscr{F},\,k\in[t-1]}\left\{\min\_{f\in\mathcal{F}}\mathcal{E}\_{t}(f)+M^{2}\left(r\_{t,k}(\mathcal{F})+\frac{1}{B\_{t,k}}\right)+M^{2}\max\_{t-k\leq j\leq t-1}\operatorname{TV}\left(P\_{j},P\_{t}\right)\right\}. |  |

Here the second inequality hides the constant cc in Assumption LABEL:sm:assumption-data-split. This completes the proof.

### D.5 Proof of LABEL:sm:lem-bias-variance-decomp-R

By the triangle inequality,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Δ^t,ℓR−ΔtR|≤|Δ^t,ℓR−Δt,ℓR|+|Δt,ℓR−ΔtR|,\big|\widehat{\Delta}^{R}\_{t,\ell}-\Delta^{R}\_{t}\big|\leq\big|\widehat{\Delta}^{R}\_{t,\ell}-\Delta^{R}\_{t,\ell}\big|+\big|\Delta^{R}\_{t,\ell}-\Delta^{R}\_{t}\big|, |  | (D.11) |

where

|  |  |  |
| --- | --- | --- |
|  | Δt,ℓR=𝔼​[Δ^t,ℓR]=Δt,ℓVt,ℓ.\Delta^{R}\_{t,\ell}=\mathbb{E}\big[\widehat{\Delta}^{R}\_{t,\ell}\big]=\frac{\Delta\_{t,\ell}}{V\_{t,\ell}}. |  |

By LABEL:sm:lem-max-diff-ratio,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Δt,ℓR−ΔtR|=|Δt,ℓVt,ℓ−ΔtVt|≤maxt−ℓ≤j≤t−1⁡|ΔjR−ΔtR|.\big|\Delta^{R}\_{t,\ell}-\Delta^{R}\_{t}\big|=\left|\frac{\Delta\_{t,\ell}}{V\_{t,\ell}}-\frac{\Delta\_{t}}{V\_{t}}\right|\leq\max\_{t-\ell\leq j\leq t-1}|\Delta^{R}\_{j}-\Delta^{R}\_{t}|. |  | (D.12) |

We have

|  |  |  |
| --- | --- | --- |
|  | Δ^t,ℓR=1nt,ℓ​∑j=t−ℓt−1∑i=1njuj,iVt,ℓ,\widehat{\Delta}^{R}\_{t,\ell}=\frac{1}{n\_{t,\ell}}\sum\_{j=t-\ell}^{t-1}\sum\_{i=1}^{n\_{j}}\frac{u\_{j,i}}{V\_{t,\ell}}, |  |

where uj,i=[f1​(𝒙j,iva)−yj,iva]2−[f2​(𝒙j,iva)−yj,iva]2u\_{j,i}=\big[f\_{1}(\bm{x}\_{j,i}^{\operatorname{\mathrm{va}}})-y\_{j,i}^{\operatorname{\mathrm{va}}}\big]^{2}-\big[f\_{2}(\bm{x}\_{j,i}^{\operatorname{\mathrm{va}}})-y\_{j,i}^{\operatorname{\mathrm{va}}}\big]^{2}. By Assumptions LABEL:sm:assumption-bounded and LABEL:sm:assumption-positive-variance, |uj,i/Vt,ℓ|≤8​M2/v|u\_{j,i}/V\_{t,\ell}|\leq 8M^{2}/v for all jj and ii. By Bernstein’s concentration inequality (LABEL:sm:lem-Bernstein), with probability at least 1−δ1-\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Δ^t,ℓR−Δt,ℓR|≤σt,ℓR​2​log⁡(2/δ)nt,ℓ+16​(M2/v)​log⁡(2/δ)3​nt,ℓ.\big|\widehat{\Delta}^{R}\_{t,\ell}-\Delta^{R}\_{t,\ell}\big|\leq\sigma^{R}\_{t,\ell}\sqrt{\frac{2\log(2/\delta)}{n\_{t,\ell}}}+\frac{16(M^{2}/v)\log(2/\delta)}{3n\_{t,\ell}}. |  | (D.13) |

Substituting ([D.12](https://arxiv.org/html/2512.23596v1#A4.E12 "Equation D.12 ‣ D.5 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) and ([D.13](https://arxiv.org/html/2512.23596v1#A4.E13 "Equation D.13 ‣ D.5 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) into ([D.11](https://arxiv.org/html/2512.23596v1#A4.E11 "Equation D.11 ‣ D.5 Proof of ‣ Appendix D Proofs for and ‣ The nonstationarity-complexity tradeoff in return prediction")) completes the proof.

### D.6 Proof of LABEL:sm:thm-select-tournament-R

We first prove the following theoretical guarantee for the R2R^{2}-based comparison subroutine LABEL:sm:alg-compare-R.

###### Theorem D.1 (Near-optimal model comparison with R2R^{2}).

Let Assumptions LABEL:sm:assumption-bounded and LABEL:sm:assumption-positive-variance hold. Choose δ∈(0,1)\delta\in(0,1) and set δ′=1/(3​t)\delta^{\prime}=1/(3t) in LABEL:sm:alg-tournament. With probability at least 1−δ1-\delta, the output f^\widehat{f} of LABEL:sm:alg-compare-R satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxλ∈[2]⁡R~t2​(fλ)−R~t2​(f^)≲log⁡(t/δ)⋅minℓ∈[t−1]⁡{maxt−ℓ≤j≤t−1⁡maxλ∈[2]⁡|R~j2​(fλ)−R~t2​(fλ)|+M2/vnt,ℓ}.\max\_{\lambda\in[2]}\widetilde{R}^{2}\_{t}(f\_{\lambda})-\widetilde{R}^{2}\_{t}(\widehat{f})\lesssim\log(t/\delta)\cdot\min\_{\ell\in[t-1]}\left\{\max\_{t-\ell\leq j\leq t-1}\max\_{\lambda\in[2]}\big|\widetilde{R}^{2}\_{j}(f\_{\lambda})-\widetilde{R}^{2}\_{t}(f\_{\lambda})\big|+\frac{M^{2}/v}{\sqrt{n\_{t,\ell}}}\right\}. |  | (D.14) |

Here ≲\lesssim hides a universal constant.

###### Proof of LABEL:sm:thm-model-comparison-R.

Following the same argument as Theorem 4.2 in HHW24, we can show that with probability at least 1−δ1-\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxλ∈[2]⁡R~t2​(fλ)−R~t2​(f^)\displaystyle\max\_{\lambda\in[2]}\widetilde{R}^{2}\_{t}(f\_{\lambda})-\widetilde{R}^{2}\_{t}(\widehat{f}) | ≤|Δ^t,ℓ^R−ΔtR|\displaystyle\leq\big|\widehat{\Delta}^{R}\_{t,\widehat{\ell}}-\Delta^{R}\_{t}\big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≲log⁡(t/δ)⋅minℓ∈[t−1]⁡{maxt−ℓ≤j≤t−1⁡|ΔjR−ΔtR|+v^t,ℓRnt,ℓ+M2/vnt,ℓ}.\displaystyle\lesssim\log(t/\delta)\cdot\min\_{\ell\in[t-1]}\left\{\max\_{t-\ell\leq j\leq t-1}\big|\Delta^{R}\_{j}-\Delta^{R}\_{t}\big|+\frac{\widehat{v}^{R}\_{t,\ell}}{\sqrt{n\_{t,\ell}}}+\frac{M^{2}/v}{n\_{t,\ell}}\right\}. |  |

We finish the proof by noting that σt,ℓR≲M2/v\sigma^{R}\_{t,\ell}\lesssim M^{2}/v and

|  |  |  |
| --- | --- | --- |
|  | |ΔjR−ΔtR|=|[R~j2​(f1)−R~j2​(f2)]−[R~t2​(f1)−R~t2​(f2)]|≤2​maxλ∈[2]⁡|R~j2​(fλ)−R~j2​(fλ)|.\big|\Delta^{R}\_{j}-\Delta^{R}\_{t}\big|=\left|\Big[\widetilde{R}^{2}\_{j}(f\_{1})-\widetilde{R}^{2}\_{j}(f\_{2})\Big]-\Big[\widetilde{R}^{2}\_{t}(f\_{1})-\widetilde{R}^{2}\_{t}(f\_{2})\Big]\right|\leq 2\max\_{\lambda\in[2]}\left|\widetilde{R}^{2}\_{j}(f\_{\lambda})-\widetilde{R}^{2}\_{j}(f\_{\lambda})\right|. |  |

∎

We can now use LABEL:sm:lem-select-tournament-reduction to translate LABEL:sm:thm-model-comparison to a theoretical guarantee for general model selection. Set ℒ​(f)=1−R~t2​(f)\mathcal{L}(f)=1-\widetilde{R}^{2}\_{t}(f) and

|  |  |  |
| --- | --- | --- |
|  | U​(δ)=C​log⁡(t/δ)⋅minℓ∈[t−1]⁡{maxt−ℓ≤j≤t−1⁡maxλ∈[Λ]⁡|R~j2​(fλ)−R~t2​(fλ)|+M2/vnt,ℓ},U(\delta)=C\log(t/\delta)\cdot\min\_{\ell\in[t-1]}\left\{\max\_{t-\ell\leq j\leq t-1}\max\_{\lambda\in[\Lambda]}\big|\widetilde{R}^{2}\_{j}(f\_{\lambda})-\widetilde{R}^{2}\_{t}(f\_{\lambda})\big|+\frac{M^{2}/v}{\sqrt{n\_{t,\ell}}}\right\}, |  |

for a sufficiently large universal constant C>0C>0. Then for any ff,

|  |  |  |
| --- | --- | --- |
|  | ℒ​(f)−minλ∈[Λ]⁡ℒ​(fλ)=maxλ∈[Λ]⁡R~t2​(fλ)−R~t2​(f).\mathcal{L}(f)-\min\_{\lambda\in[\Lambda]}\mathcal{L}(f\_{\lambda})=\max\_{\lambda\in[\Lambda]}\widetilde{R}^{2}\_{t}(f\_{\lambda})-\widetilde{R}^{2}\_{t}(f). |  |

By LABEL:sm:lem-select-tournament-reduction and the choice of δ′\delta^{\prime}, the output f^\widehat{f} of LABEL:sm:alg-tournament satisfies that with probability at least 1−δ1-\delta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxλ∈[Λ]⁡R~t2​(fλ)−R~t2​(f^)\displaystyle\max\_{\lambda\in[\Lambda]}\widetilde{R}^{2}\_{t}(f\_{\lambda})-\widetilde{R}^{2}\_{t}(\widehat{f}) | ≲U​(δ/Λ2)\displaystyle\lesssim U(\delta/\Lambda^{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≲log⁡(Λ​t/δ)⋅minℓ∈[t−1]⁡{maxt−ℓ≤j≤t−1⁡maxλ∈[Λ]⁡|R~j2​(fλ)−R~t2​(fλ)|+M2/vnt,ℓ}.\displaystyle\lesssim\log(\Lambda t/\delta)\cdot\min\_{\ell\in[t-1]}\left\{\max\_{t-\ell\leq j\leq t-1}\max\_{\lambda\in[\Lambda]}\big|\widetilde{R}^{2}\_{j}(f\_{\lambda})-\widetilde{R}^{2}\_{t}(f\_{\lambda})\big|+\frac{M^{2}/v}{\sqrt{n\_{t,\ell}}}\right\}. |  |

Here ≲\lesssim only hides universal constants.

## Appendix E Technical Lemmas

###### Lemma E.1.

Let ψ:ℝ+→ℝ+\psi:\mathbb{R}\_{+}\to\mathbb{R}\_{+} be a sub-root function with fixed point r∗>0r^{\*}>0. For all A,a>0A,a>0, the function ψ~​(r)=A​ψ​(a​r)\widetilde{\psi}(r)=A\psi(ar) is sub-root and its fixed point r~\widetilde{r} satisfies

|  |  |  |
| --- | --- | --- |
|  | min{1,Aa}2a​r∗≤r~≤max{1,Aa}2a​r∗.\frac{\min\{1,Aa\}^{2}}{a}r^{\*}\leq\widetilde{r}\leq\frac{\max\{1,Aa\}^{2}}{a}r^{\*}. |  |

###### Proof of [Lemma˜E.1](https://arxiv.org/html/2512.23596v1#A5.Thmlemma1 "Lemma E.1. ‣ Appendix E Technical Lemmas ‣ The nonstationarity-complexity tradeoff in return prediction").

It is easy to verify that ψ~\widetilde{\psi} is subroot. We now study r~\widetilde{r}. First consider the case a=1a=1. Since A​ψ​(r~)=r~A\psi(\widetilde{r})=\widetilde{r}, then ψ​(r~)/r~=r~/A\psi(\widetilde{r})/\sqrt{\widetilde{r}}=\sqrt{\widetilde{r}}/A. There are two cases.

* •

  If r~≥r∗\widetilde{r}\geq r^{\*}, then ψ​(r~)/r~≤ψ​(r∗)/r∗=r∗\psi(\widetilde{r})/\sqrt{\widetilde{r}}\leq\psi(r^{\*})/\sqrt{r^{\*}}=\sqrt{r^{\*}}, so r~≤A2​r∗\widetilde{r}\leq A^{2}r^{\*}.
* •

  If r~≤r∗\widetilde{r}\leq r^{\*}, then ψ​(r~)/r~≥ψ​(r∗)/r∗=r∗\psi(\widetilde{r})/\sqrt{\widetilde{r}}\geq\psi(r^{\*})/\sqrt{r^{\*}}=\sqrt{r^{\*}}, so r~≥A2​r∗\widetilde{r}\geq A^{2}r^{\*}.

Therefore, if A<1A<1, then A2​r∗≤r~<r∗A^{2}r^{\*}\leq\widetilde{r}<r^{\*}. If A>1A>1, then r∗<r~≤A2​r∗r^{\*}<\widetilde{r}\leq A^{2}r^{\*}. This shows that

|  |  |  |
| --- | --- | --- |
|  | min{1,A}2r∗≤r~≤max{1,A}2r∗.\min\{1,A\}^{2}r^{\*}\leq\widetilde{r}\leq\max\{1,A\}^{2}r^{\*}. |  |

In the general case of a>0a>0, the function r↦a−1​ψ​(a​r)r\mapsto a^{-1}\psi(ar) is sub-root and has fixed point a−1​r∗a^{-1}r^{\*}. The proof is finished by noting ψ~​(r)=(A​a)⋅a−1​ψ​(a​r)\widetilde{\psi}(r)=(Aa)\cdot a^{-1}\psi(ar).
∎

###### Lemma E.2 (Bernstein’s concentration inequality).

Let {xi}i=1n\{x\_{i}\}\_{i=1}^{n} be independent random variables taking values in [a,b][a,b] almost surely. Define the average variance σ2=1n​∑i=1nvar⁡(xi)\sigma^{2}=\frac{1}{n}\sum\_{i=1}^{n}\operatorname{{\rm var}}(x\_{i}). For any δ∈(0,1)\delta\in(0,1), with probability at least 1−δ1-\delta,

|  |  |  |
| --- | --- | --- |
|  | |1n​∑i=1n(xi−𝔼​xi)|≤σ​2​log⁡(2/δ)n+2​(b−a)​log⁡(2/δ)3​n.\bigg|\frac{1}{n}\sum\_{i=1}^{n}(x\_{i}-\mathbb{E}x\_{i})\bigg|\leq\sigma\sqrt{\frac{2\log(2/\delta)}{n}}+\frac{2(b-a)\log(2/\delta)}{3n}. |  |

###### Proof of [Lemma˜E.2](https://arxiv.org/html/2512.23596v1#A5.Thmlemma2 "Lemma E.2 (Bernstein’s concentration inequality). ‣ Appendix E Technical Lemmas ‣ The nonstationarity-complexity tradeoff in return prediction").

Inequality (2.10) in BLM13 implies that for any t≥0t\geq 0,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(1n​∑i=1n(xi−𝔼​xi)>t)≤exp⁡(−n​t2/2σ2+(b−a)​t/3).\mathbb{P}\bigg(\frac{1}{n}\sum\_{i=1}^{n}(x\_{i}-\mathbb{E}x\_{i})>t\bigg)\leq\exp\left(-\frac{nt^{2}/2}{\sigma^{2}+(b-a)t/3}\right). |  |

Fix δ∈(0,1)\delta\in(0,1). Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | exp⁡(−n​t2/2σ2+(b−a)​t/3)≤δ\displaystyle\quad\exp\left(-\frac{nt^{2}/2}{\sigma^{2}+(b-a)t/3}\right)\leq\delta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | n​t22≥σ2​log⁡(1/δ)+t​(b−a)​log⁡(1/δ)3\displaystyle\quad\frac{nt^{2}}{2}\geq\sigma^{2}\log(1/\delta)+\frac{t(b-a)\log(1/\delta)}{3} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\Leftrightarrow | n2​(t−(b−a)​log⁡(1/δ)3​n)2≥σ2​log⁡(1/δ)+n2​((b−a)​log⁡(1/δ)3​n)2\displaystyle\quad\frac{n}{2}\bigg(t-\frac{(b-a)\log(1/\delta)}{3n}\bigg)^{2}\geq\sigma^{2}\log(1/\delta)+\frac{n}{2}\bigg(\frac{(b-a)\log(1/\delta)}{3n}\bigg)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇐\displaystyle\Leftarrow | (t−(b−a)​log⁡(1/δ)3​n)2≥(σ​2​log⁡(1/δ)n+(b−a)​log⁡(1/δ)3​n)2\displaystyle\quad\bigg(t-\frac{(b-a)\log(1/\delta)}{3n}\bigg)^{2}\geq\bigg(\sigma\sqrt{\frac{2\log(1/\delta)}{n}}+\frac{(b-a)\log(1/\delta)}{3n}\bigg)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇐\displaystyle\Leftarrow | t≥σ​2​log⁡(1/δ)n+2​(b−a)​log⁡(1/δ)3​n.\displaystyle\quad t\geq\sigma\sqrt{\frac{2\log(1/\delta)}{n}}+\frac{2(b-a)\log(1/\delta)}{3n}. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(1n​∑i=1n(xi−𝔼​xi)>σ​2​log⁡(1/δ)n+2​(b−a)​log⁡(1/δ)3​n)≤δ.\mathbb{P}\left(\frac{1}{n}\sum\_{i=1}^{n}(x\_{i}-\mathbb{E}x\_{i})>\sigma\sqrt{\frac{2\log(1/\delta)}{n}}+\frac{2(b-a)\log(1/\delta)}{3n}\right)\leq\delta. |  |

Replacing each xix\_{i} by −xi-x\_{i} gives bounds on the lower tail and the absolute deviation.
∎

###### Lemma E.3.

For all a,a1,…,an≥0a,a\_{1},...,a\_{n}\geq 0 and b,b1,…,bn>0b,b\_{1},...,b\_{n}>0, it holds that

|  |  |  |
| --- | --- | --- |
|  | |ab−∑i=1nai∑i=1nbi|≤maxi∈[n]⁡|ab−aibi|.\left|\frac{a}{b}-\frac{\sum\_{i=1}^{n}a\_{i}}{\sum\_{i=1}^{n}b\_{i}}\right|\leq\max\_{i\in[n]}\left|\frac{a}{b}-\frac{a\_{i}}{b\_{i}}\right|. |  |

###### Proof of [Lemma˜E.3](https://arxiv.org/html/2512.23596v1#A5.Thmlemma3 "Lemma E.3. ‣ Appendix E Technical Lemmas ‣ The nonstationarity-complexity tradeoff in return prediction").

This is due to

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ab−∑i=1nai∑i=1nbi|=|ab−∑i=1nbi∑j=1nbj⋅aibi|\displaystyle\left|\frac{a}{b}-\frac{\sum\_{i=1}^{n}a\_{i}}{\sum\_{i=1}^{n}b\_{i}}\right|=\left|\frac{a}{b}-\sum\_{i=1}^{n}\frac{b\_{i}}{\sum\_{j=1}^{n}b\_{j}}\cdot\frac{a\_{i}}{b\_{i}}\right| | =|∑i=1nbi∑j=1nbj⋅(ab−aibi)|\displaystyle=\left|\sum\_{i=1}^{n}\frac{b\_{i}}{\sum\_{j=1}^{n}b\_{j}}\cdot\left(\frac{a}{b}-\frac{a\_{i}}{b\_{i}}\right)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑i=1nbi∑j=1nbj⋅|ab−aibi|≤maxi∈[n]⁡|ab−aibi|.\displaystyle\leq\sum\_{i=1}^{n}\frac{b\_{i}}{\sum\_{j=1}^{n}b\_{j}}\cdot\left|\frac{a}{b}-\frac{a\_{i}}{b\_{i}}\right|\leq\max\_{i\in[n]}\left|\frac{a}{b}-\frac{a\_{i}}{b\_{i}}\right|. |  |

This finishes the proof.
∎

## Appendix F Additional Experiment Details

### F.1 Summary Statistics of the Dataset

We now provide an overview of the long–short firm characteristic covariates used in the analysis, their time-series behavior, and cross-sectional dependence as well as a brief summary of the stochastic discount factor (SDF) and decile portfolios from CPZ24. Recall that all of the long-short characteristic portfolios are computed at the daily frequency, for the subsequent summary plots, we have aggregated them into the monthly frequency using within-month averages, in line with the standard practice of aligning signals with monthly returns. The monthly aggregation smooths out day-to-day noise and highlights the economically relevant medium-horizon variations.

##### Monthly Evolution of Covariates.

Figure [7](https://arxiv.org/html/2512.23596v1#A6.F7 "Figure 7 ‣ Monthly Evolution of Covariates. ‣ F.1 Summary Statistics of the Dataset ‣ Appendix F Additional Experiment Details ‣ The nonstationarity-complexity tradeoff in return prediction") displays the time series of monthly mean values for the twelve most volatile covariates, ranked by their total-sample standard deviation. The figure highlights that variables such as retvol, mom12m, and baspread exhibit pronounced month-to-month fluctuations, while others such as turn and operprof remain relatively stable. These series reveal persistent heteroskedasticity and regime shifts over time, particularly during market dislocations such as the early 2000s and 2008 crises.

Figure 7: Monthly Means of the 12 Most Volatile Covariates.

![Refer to caption](x55.png)


Each panel shows the monthly mean of a long–short firm characteristic.
Covariates are ranked by total-sample volatility.
The time series reveal which characteristics exhibit the greatest month-to-month variation and long-run persistence.

##### Distributional and Correlation Structure.

Figure [8](https://arxiv.org/html/2512.23596v1#A6.F8 "Figure 8 ‣ Distributional and Correlation Structure. ‣ F.1 Summary Statistics of the Dataset ‣ Appendix F Additional Experiment Details ‣ The nonstationarity-complexity tradeoff in return prediction") summarizes the time-series distributions of the same twelve covariates using standardized (z-scored) monthly values. The median, interquartile range, and whiskers capture the magnitude and symmetry of fluctuations across time. Most variables display near-zero median values but differ in dispersion and tail behavior, consistent with heterogeneous economic mechanisms underlying each characteristic.

Figure 8: Distributions (Boxplots) of Standardized Monthly Covariates.

![Refer to caption](x56.png)


Z-scored monthly series for the twelve most volatile covariates. The figure compares dispersion and tail behavior across characteristics, highlighting differences in amplitude and symmetry.

For example, variables such as retvol, baspread, and mom12m exhibit wide interquartile ranges and thick tails, suggesting that these signals experience substantial time variation and occasional extreme realizations. In contrast, variables such as turn and operprof have narrower boxes, implying greater stability through time.

Each distribution is constructed by pooling monthly observations over the entire sample period for that specific covariate. This provides a concise view of the temporal heterogeneity and persistence of each characteristic after accounting for scale differences. The figure thus complements the time-series plots in Figure [7](https://arxiv.org/html/2512.23596v1#A6.F7 "Figure 7 ‣ Monthly Evolution of Covariates. ‣ F.1 Summary Statistics of the Dataset ‣ Appendix F Additional Experiment Details ‣ The nonstationarity-complexity tradeoff in return prediction") by providing a scale-free summary of long-run variability and skewness in the underlying long–short characteristics.

The pairwise dependence structure among the top thirty covariates (in terms of volatility) is visualized in Figure [9](https://arxiv.org/html/2512.23596v1#A6.F9 "Figure 9 ‣ Distributional and Correlation Structure. ‣ F.1 Summary Statistics of the Dataset ‣ Appendix F Additional Experiment Details ‣ The nonstationarity-complexity tradeoff in return prediction"). The heatmap reveals clusters of strongly correlated signals, such as volatility-related measures (retvol, idiovol, roavol) and liquidity-related variables (baspread, zerotrade, turn). The presence of such correlation blocks indicates there could be shared economic channels.

Figure 9: Correlation Heatmap of the 30 Most Volatile Covariates.

![Refer to caption](x57.png)


The matrix shows pairwise Pearson correlations between the thirty most volatile monthly covariates.
Red indicates positive correlation and blue indicates negative correlation.
Distinct blocks suggest clusters of related characteristics.

##### Time-Varying Volatility of Covariates.

Figure [10](https://arxiv.org/html/2512.23596v1#A6.F10 "Figure 10 ‣ Time-Varying Volatility of Covariates. ‣ F.1 Summary Statistics of the Dataset ‣ Appendix F Additional Experiment Details ‣ The nonstationarity-complexity tradeoff in return prediction") plots the 12-month rolling standard deviation of the twelve most volatile covariates. Unlike Figure [7](https://arxiv.org/html/2512.23596v1#A6.F7 "Figure 7 ‣ Monthly Evolution of Covariates. ‣ F.1 Summary Statistics of the Dataset ‣ Appendix F Additional Experiment Details ‣ The nonstationarity-complexity tradeoff in return prediction"), which ranks variables by overall volatility, the rolling volatility tracks how the variability of each covariate evolves through time. Periods such as the dot-com bubble and the global financial crisis correspond to distinct spikes in volatility across multiple signals, indicating that the informational strength and instability of certain factors are regime-dependent.

Figure 10: Twelve-Month Rolling Volatility of the Most Volatile Covariates.

![Refer to caption](x58.png)


The panels show rolling standard deviations computed using a 12-month moving window for each of the twelve most volatile covariates.
This highlights temporal variation in the stability and amplitude of the long-short signals.

##### SDF and Decile Portfolios.

Finally, Figure [11](https://arxiv.org/html/2512.23596v1#A6.F11 "Figure 11 ‣ SDF and Decile Portfolios. ‣ F.1 Summary Statistics of the Dataset ‣ Appendix F Additional Experiment Details ‣ The nonstationarity-complexity tradeoff in return prediction") plots the monthly time series of the stochastic discount factor (SDF) alongside the ten equal-weighted decile portfolios sorted by the underlying characteristic. The decile portfolios exhibit substantial comovement, with the SDF (shown in black) fluctuating more smoothly. This figure provides a benchmark for comparing the magnitude and temporal alignment of the SDF with characteristic-sorted portfolio returns, and serves as a diagnostic for whether the constructed SDF captures systematic components of asset pricing variation.

Figure 11: Monthly SDF and Decile Portfolios.

![Refer to caption](x59.png)


The black line represents the stochastic discount factor (SDF), while the colored lines correspond to ten equal-weighted decile portfolios sorted on firm characteristics.
The comovement between the SDF and the characteristic-sorted portfolios provides an initial indication of factor relevance.

### F.2 Experiment Details for LABEL:sm:sec-tradeoff-empirics

In this section, we given more details on our empirical investigations of the nonstationarity-complexity tradeoff in LABEL:sm:sec-tradeoff-empirics.

The three prediction models, along with their hyperparameters, are: (1) a linear model trained by Ridge regression using the most recent 6464 months of data, with α=1\alpha=1, (2) a random forest trained on the most recent 6464 months of data, with ntree=200n\_{\texttt{tree}}=200 and dmax=5d\_{\max}=5, and (3) a random forest trained on all historical data, with ntree=200n\_{\texttt{tree}}=200 and dmax=5d\_{\max}=5.

In each month tt, we construct training data by randomly subsampling 4/54/5 of the observations 𝒟j\mathcal{D}\_{j} in each previous month j∈[t−1]j\in[t-1]. The process is repeated 2020 times with independent random seeds. We then average the out-of-sample R2R^{2} over the 2020 random seeds, which are then used to produce the figures in LABEL:sm:sec-tradeoff-empirics.

## Appendix G Additional Experiment Results

### G.1 Experiment Results with the Standard R2R^{2} Metric

In LABEL:sm:sec-experiments, we evaluated predictive performance using the zero-benchmark R2R^{2} to avoid the noise inherent in historical mean estimation. For completeness, this section reports the corresponding results using the standard out-of-sample R2R^{2} metric, which benchmarks model performance against the historical sample mean. Qualitatively, the relative performance among models remains consistent with the the observations in LABEL:sm:sec-experiments: our adaptive algorithm ATOMS continues to outperform fixed-window benchmarks. Quantitatively, we observe that the standard R2R^{2} values are generally lower than their zero-benchmark counterparts.

LABEL:sm:tab:oos\_r2\_industry\_time-standardR2 presents out-of-sample standard R2R^{2} values of ATOMS and baselines across distinct economic regimes, serving as the counterpart to LABEL:sm:tab:oos\_r2\_industry\_time in the main text.

Table 6: OOS Standard R2R^{2} Averages Across Industries by Time Period.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Method | Full OOS Period | Recessions | | |
| Gulf War | 2001 Recession | Financial Crisis |
| ATOMS | 0.0410.041 | −0.019-0.019 | 0.1150.115 | 0.0390.039 |
| Fixed-val​(32)\texttt{Fixed-val}(32) | 0.0130.013 | −0.038-0.038 | 0.0850.085 | −0.003-0.003 |
| Fixed-val​(512)\texttt{Fixed-val}(512) | 0.0340.034 | −0.080-0.080 | 0.1070.107 | 0.0370.037 |
| Fixed-CV | 0.0260.026 | −0.056-0.056 | 0.0600.060 | 0.0120.012 |

This table reports OOS standard R2R^{2} averages for return prediction models across all 17 industry portfolios. Full OOS Period refers to OOS period covering 01/1990∼\sim11/2016. Columns report OOS R2R^{2} averages across all industries and highlight this metric during three recessions, as documented in [NBER Business Cycle Dating](https://www.nber.org/research/business-cycle-dating):

* •

  the 1990 Gulf War recession (06/1990∼\sim10/1990);
* •

  the 2001 Recession of dot-com bubble burst and the 9/11 attack (05/2001∼\sim10/2001);
* •

  the Financial Crisis led by defaults of subprime mortgages (11/2007∼\sim06/2009).

That is, the OOS performance in Gulf War column focuses on model performance comparisons exclusively in the out-of-sample period of 06/1990∼\sim10/1990. All values are calculated using monthly return data.

LABEL:sm:fig-boxplot-standardR2 gives a box plot of the OOS standard R2R^{2} of ATOMS and the fixed-window baselines over the 17 industry portfolios, mirroring LABEL:sm:fig-boxplot.

Figure 12: Box Plot of OOS Standard R2R^{2} of ATOMS and Baselines for 1717 Industry Portfolios.

![Refer to caption](x60.png)


This figure describes the distribution of each method’s OOS R2R^{2}. Each box corresponds to all industries and all years in our OOS horizon.

Finally, LABEL:sm:fig-industry-yearly-standardR2 plots the annual out-of-sample R2R^{2} for the 1717 industry portfolios, paralleling LABEL:sm:fig-industry-yearly.

Figure 13: Annual OOS Standard R2R^{2} of Different Approaches for 1717 Industry Portfolios.

![Refer to caption](x61.png)

![Refer to caption](x62.png)

![Refer to caption](x63.png)

![Refer to caption](x64.png)

![Refer to caption](x65.png)

![Refer to caption](x66.png)

![Refer to caption](x67.png)

![Refer to caption](x68.png)

![Refer to caption](x69.png)

![Refer to caption](x70.png)

![Refer to caption](x71.png)

![Refer to caption](x72.png)

![Refer to caption](x73.png)

![Refer to caption](x74.png)

![Refer to caption](x75.png)

![Refer to caption](x76.png)

![Refer to caption](x77.png)

This figure reports the annual OOS standard R2R^{2} of our adaptive model selection algorithm ATOMS (black dashed line with ×\times’s), as well as the fixed-window baselines Fixed-val​(32)\texttt{Fixed-val}(32) (blue ▼\blacktriangledown’s), Fixed-val​(128)\texttt{Fixed-val}(128) (orange ■\blacksquare’s), and Fixed-val​(512)\texttt{Fixed-val}(512) (red), which use the last 3232, last 128128 and all months of validation data. The title in each subfigure is Kenneth French’s acronym for each industry. For the full names of these industries, please refer to Table LABEL:sm:tab-industry-name-mapping.

### G.2 Experiment Results for ATOMS-R2

In this section, we present experiment results for the R2R^{2}-based model selection method ATOMS-R2 developed in LABEL:sm:sec-select-R2. We set its hyperparameters δ′=0.1\delta^{\prime}=0.1 and M2=5M^{2}=5. Its performance is similar to the MSE-based approach ATOMS. We will report results for the R2R^{2} metric that benchmarks against a zero forecast.

In LABEL:sm:fig-boxplot-supp, we give a box plot of the overall out-of-sample R2R^{2} of ATOMS-R2 along with ATOMS and the fixed-window benchmarks across the 1717 industries. In LABEL:sm:fig-industry-yearly-supp, we compare the annual out-of-sample R2R^{2} of ATOMS-R2 and ATOMS for the 1717 industries. Again, ATOMS-R2 and ATOMS have similar performance.

Figure 14: Box Plot of Out-of-Sample R2R^{2} of ATOMS-R2, ATOMS and Baselines for 1717 Industry Portfolios.

![Refer to caption](x78.png)


This figure describes the distribution of each method’s OOS R2R^{2}. Each box corresponds to all industries and all years in our OOS horizon.




Figure 15: Annual Out-of-Sample R2R^{2} of ATOMS-R2 and ATOMS for 1717 Industry Portfolios.

![Refer to caption](x79.png)

![Refer to caption](x80.png)

![Refer to caption](x81.png)

![Refer to caption](x82.png)

![Refer to caption](x83.png)

![Refer to caption](x84.png)

![Refer to caption](x85.png)

![Refer to caption](x86.png)

![Refer to caption](x87.png)

![Refer to caption](x88.png)

![Refer to caption](x89.png)

![Refer to caption](x90.png)

![Refer to caption](x91.png)

![Refer to caption](x92.png)

![Refer to caption](x93.png)

![Refer to caption](x94.png)

![Refer to caption](x95.png)

This figure reports the annual OOS R2R^{2} of our adaptive model selection algorithms ATOMS-R2 (orange line with ■\blacksquare’s) and ATOMS (black dashed line with ×\times’s). The title in each subfigure is Kenneth French’s acronym for each industry. For the full names of these industries, please refer to Table LABEL:sm:tab-industry-name-mapping.