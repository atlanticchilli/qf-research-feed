---
authors:
- Wang Yi
- Takashi Hasuike
doc_id: arxiv:2601.04062v2
family_id: arxiv:2601.04062
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets
url_abs: http://arxiv.org/abs/2601.04062v2
url_html: https://arxiv.org/html/2601.04062v2
venue: arXiv q-fin
version: 2
year: 2026
---


Yi Wang
[apple9238@fuji.waseda.jp](mailto:apple9238@fuji.waseda.jp)

Takashi Hasuike
[thasuike@waseda.jp](mailto:thasuike@waseda.jp)
Waseda University, Graduate School of Creative Science and Engineering, Tokyo, Japan

###### Abstract

Improvements in return forecast accuracy do not always lead to proportional improvements in portfolio decision quality, especially under realistic trading frictions and constraints. This paper adopts
the Smart Predict–then–Optimize (SPO) paradigm for portfolio optimization in
real markets, which explicitly aligns the learning objective with downstream
portfolio decision quality rather than pointwise prediction accuracy. Within
this paradigm, predictive models are trained using an SPO-based surrogate loss
that directly reflects the performance of the resulting investment decisions. To preserve interpretability and robustness, we employ linear predictors built
on return-based and technical-indicator features and integrate them with
portfolio optimization models that incorporate transaction fee, turnover
control, and regularization. We evaluate the proposed approach on U.S. ETF data
(2015–2025) using a rolling-window backtest with monthly rebalancing. Empirical
results show that decision-focused training consistently improves risk-adjusted
performance over predict–then–optimize baselines and classical optimization
benchmarks, and yields strong robustness during adverse market regimes (e.g.,
the 2020 COVID-19). These findings highlight the practical value of the Smart
Predict–then–Optimize paradigm for portfolio optimization in realistic and
non-stationary financial environments.

###### keywords:

Portfolio optimization , Decision-focused learning , Smart predict–then–optimize , Financial machine learning

††journal: Expert Systems with Applications

## 1 Introduction

Portfolio optimization is a central problem in financial decision-making, where
investors seek to allocate capital across multiple assets to balance return and
risk. With the increasing availability of financial data, machine learning
techniques have been widely adopted to support data-driven portfolio
construction and asset allocation. Despite these advances, financial markets remain highly complex systems
characterized by nonlinearity, noise, and non-stationarity, making robust and
reliable investment decision-making challenging in practice.
These characteristics expose a fundamental tension between improving
predictive accuracy and achieving high-quality portfolio decisions under realistic market frictions.

A large body of prior work focuses on improving return predictability using
advanced time-series models, including recurrent neural networks and
Transformer-based architectures. While these models have demonstrated strong
performance in various forecasting tasks, their practical benefits in financial
applications are often limited by weak periodicity, low signal-to-noise ratios,
and frequent regime shifts. Moreover, recent evidence suggests that simple and
transparent models can achieve competitive predictive performance, calling into
question the necessity of highly complex architectures in noisy financial
environments. More importantly, improved forecasting accuracy alone does not
guarantee superior portfolio performance.

Most learning-based portfolio methods adopt a predict–then–optimize (PtO)
paradigm, in which asset returns or related parameters are first estimated and
then treated as fixed inputs to a downstream optimization problem. Although
intuitive, this decoupled approach suffers from a fundamental mismatch between
the training objective and the ultimate decision goal. In particular, small
prediction errors can induce large changes in optimal portfolio weights,
especially under realistic constraints and trading frictions, leading to
suboptimal investment decisions even when predictive accuracy is high.

To address this limitation, the Smart Predict–then–Optimize (SPO) framework
and, more broadly, decision-focused learning (DFL) paradigms have been proposed
to explicitly realign the learning objective with downstream decision quality.
From a paradigm perspective, SPO departs from the conventional
predict–then–optimize workflow by embedding the optimization problem into the
training loop, thereby training predictive models based on the quality of the
resulting decisions rather than prediction error alone.

In this study, we investigate decision-focused learning for portfolio
optimization under a realistic rolling-window backtesting framework. We adopt
linear predictors for interpretability and robustness, and integrate them with
multiple portfolio optimization formulations within a unified SPO-based
architecture. Our contributions can be summarized as follows:

* 1.

  We systematically evaluate the Smart Predict–then–Optimize paradigm for portfolio optimization under realistic trading constraints and transaction fee, and contrast it with conventional predict–then–optimize approaches.
* 2.

  We propose robust extensions of the SPO framework that explicitly
  account for prediction uncertainty and demonstrate their effectiveness
  during adverse market regimes.
* 3.

  Through extensive empirical studies on U.S. ETF data across multiple
  market conditions, including crisis and bull-market periods, we show that
  decision-focused learning consistently improves portfolio decision quality
  compared to conventional predict–then–optimize baselines.

## 2 Literature Review

### 2.1 Portfolio Optimization Modeling

Modern portfolio optimization originates from the mean–variance framework
proposed by Markowitz Markowitz [[1952](https://arxiv.org/html/2601.04062v2#bib.bib1 "Portfolio selection")], which formulates asset
allocation as a trade-off between expected return and risk.
Subsequent studies have extended this framework by introducing alternative
risk measures, additional constraints, and techniques to address estimation
uncertainty, including the Sharpe ratio Sharpe [[1998](https://arxiv.org/html/2601.04062v2#bib.bib2 "The sharpe ratio")] and
coherent risk measures such as Conditional Value-at-Risk (CVaR) Rockafellar and Uryasev [[2000](https://arxiv.org/html/2601.04062v2#bib.bib3 "Optimization of conditional value-at-risk")].
Robust portfolio optimization further accounts for parameter uncertainty by
optimizing portfolio decisions against worst-case scenarios within prescribed
uncertainty sets Goldfarb and Iyengar [[2003](https://arxiv.org/html/2601.04062v2#bib.bib4 "Robust portfolio selection problems")].

From both theoretical and empirical perspectives, Jagannathan and Ma Jagannathan and Ma [[2003](https://arxiv.org/html/2601.04062v2#bib.bib5 "Risk reduction in large portfolios: why imposing the wrong constraints helps")]
demonstrate that portfolio weight constraints can be interpreted as a form of
statistical regularization.
Such constraints mitigate estimation error and improve out-of-sample risk
performance, thereby providing a methodological foundation for incorporating
additional constraints and penalty terms in portfolio optimization models.

In particular, transaction fee and portfolio turnover are commonly modeled
through penalty terms in the optimization objective to account for realistic
trading frictions Boyd et al. [[2017](https://arxiv.org/html/2601.04062v2#bib.bib6 "Multi-period trading via convex optimization")].

### 2.2 Learning-based Approaches

Learning-based approaches to portfolio optimization can be broadly divided into two paradigms according to how learning and decision-making are integrated: reinforcement learning (RL) methods and predict–then–optimize (PtO) methods.

Reinforcement learning approaches formulate portfolio management as a sequential decision-making problem under a Markov decision process, where an agent learns a policy to maximize cumulative rewards through repeated interaction with a financial environment. A variety of RL Moody and Saffell [[2001](https://arxiv.org/html/2601.04062v2#bib.bib7 "Learning to trade via direct reinforcement")] and deep reinforcement learning (DRL) Jiang et al. [[2017](https://arxiv.org/html/2601.04062v2#bib.bib8 "A deep reinforcement learning framework for the financial portfolio management problem")] algorithms have been applied in this context, including DQN Pigorsch and Schäfer [[2022](https://arxiv.org/html/2601.04062v2#bib.bib10 "High-dimensional stock portfolio trading with deep reinforcement learning")], PPO Liu et al. [[2024](https://arxiv.org/html/2601.04062v2#bib.bib11 "Dynamic datasets and market environments for financial reinforcement learning")], and DDPG Deng et al. [[2017](https://arxiv.org/html/2601.04062v2#bib.bib9 "Deep direct reinforcement learning for financial signal representation and trading")]. While these approaches offer high modeling flexibility, they typically rely on carefully designed reward functions and environment simulators, which may lead to unstable training dynamics and limited interpretability in noisy and non-stationary financial markets Bai et al. [[2025](https://arxiv.org/html/2601.04062v2#bib.bib12 "A review of reinforcement learning in financial applications")].

In contrast, predict–then–optimize (PtO) methods decouple the prediction and decision stages by first learning problem parameters, such as asset returns or costs, and then solving a downstream optimization problem to obtain portfolio decisions. This paradigm preserves the structure of classical portfolio optimization models and enables the explicit incorporation of constraints and domain knowledge.

Within the PtO framework, a wide variety of machine learning and neural network models have been extensively investigated for portfolio optimization. In these approaches, learning models are used to estimate key problem parameters, including expected asset returns, risk measures, or other predictive signals, which are subsequently incorporated into classical portfolio optimization formulations. Representative predictive models include linear regression Deng and Min [[2013](https://arxiv.org/html/2601.04062v2#bib.bib18 "Applied optimization in global efficient portfolio construction using earning forecasts")], support vector machine(SVM) Paiva et al. [[2019](https://arxiv.org/html/2601.04062v2#bib.bib17 "Decision-making for financial trading: a fusion approach of machine learning and portfolio selection")], tree-based method, and deep neural network (DNN) Freitas et al. [[2009](https://arxiv.org/html/2601.04062v2#bib.bib13 "Prediction-based portfolio optimization model using neural networks")], such as recurrent neural network (RNN) and long short-term memory (LSTM) Wang et al. [[2020](https://arxiv.org/html/2601.04062v2#bib.bib16 "Portfolio formation with preselection using deep learning from long-term financial data")] network. Comprehensive reviews and empirical studies  Krauss et al. [[2017](https://arxiv.org/html/2601.04062v2#bib.bib14 "Deep neural networks, gradient-boosted trees, random forests: statistical arbitrage on the s&p 500")], Ma et al. [[2021](https://arxiv.org/html/2601.04062v2#bib.bib15 "Portfolio optimization with return prediction using deep learning and machine learning")]have examined the effectiveness of these models in portfolio-related applications. By integrating data-driven predictions with optimization-based portfolio construction, PtO methods aim to improve investment performance while maintaining the interpretability and structural advantages of traditional portfolio optimization frameworks.

However, stock market prediction remains a challenging time-series forecasting problem, as financial markets are inherently nonlinear, dynamic, noisy, and chaotic, making direct and accurate prediction difficult Deboeck [[1994](https://arxiv.org/html/2601.04062v2#bib.bib19 "Trading on the edge: neural, genetic, and fuzzy systems for chaotic financial markets")].

Recent advances in recurrent neural networks such as LSTM Lindemann et al. [[2021](https://arxiv.org/html/2601.04062v2#bib.bib26 "A survey on long short-term memory networks for time series prediction")] and Transformer-based models Wang et al. [[2024](https://arxiv.org/html/2601.04062v2#bib.bib27 "TimeXer: empowering transformers for time series forecasting with exogenous variables")], Zhang et al. [[2023](https://arxiv.org/html/2601.04062v2#bib.bib30 "TimeMixer: decomposable multiscale mixing for time series forecasting")], Nie et al. [[2023](https://arxiv.org/html/2601.04062v2#bib.bib28 "A time series is worth 64 words: long-term forecasting with transformers")], Liu et al. [[2023](https://arxiv.org/html/2601.04062v2#bib.bib29 "ITransformer: inverted transformers are effective for time series forecasting")] have demonstrated strong effectiveness across a wide range of time-series forecasting tasks. Nevertheless, these architectures often rely on inductive biases such as long-range dependency modeling or periodic pattern extraction, which are particularly suitable for structured or seasonal time series. In contrast, financial time series are characterized by weak periodicity, low signal-to-noise ratios, and frequent regime shifts, limiting the practical gains of highly complex architectures in real-world investment settings.

Moreover, the increased architectural complexity of deep recurrent and Transformer-based models raises concerns regarding training stability and interpretability in high-stakes financial decision-making. For example, recent studies such as DLinear Zeng et al. [[2023](https://arxiv.org/html/2601.04062v2#bib.bib20 "Are transformers effective for time series forecasting?")] question the necessity of complex architectures for time-series forecasting, showing that simple linear models can achieve competitive performance.

Nevertheless, even with simplified and more transparent predictive models, the relationship between prediction accuracy and downstream portfolio decision quality remains indirect. Under these circumstances, conventional predict–then–optimize (PtO) approaches that primarily focus on predictive accuracy may fail to yield optimal investment decisions. This limitation motivates the adoption of Smart Predict–then–Optimize (SPO) and other decision-focused learning frameworks, which explicitly align the learning objective with downstream portfolio optimization performance.

### 2.3 Smart Predict-then-Optimize (SPO)

The distinction between predict–then–optimize (PtO) and Smart Predict–then–Optimize (SPO) was formally introduced by Elmachtoub and Grigas Elmachtoub and Grigas [[2022](https://arxiv.org/html/2601.04062v2#bib.bib21 "Smart “predict, then optimize”")]. While PtO methods focus on minimizing prediction error independently of the downstream optimization problem, SPO explicitly aligns the learning objective with decision quality. In related literature, this paradigm is also referred to as prediction-focused learning and decision-focused learning Mandi et al. [[2024](https://arxiv.org/html/2601.04062v2#bib.bib22 "Decision-focused learning: foundations, state of the art, benchmark and future opportunities")].

In a conventional Predict-then-Optimize (PtO) framework, the predictive model is trained by minimizing a surrogate loss function, such as the mean squared error between predicted and realized parameters. The resulting predictions are then treated as fixed inputs to a downstream optimization problem. While this approach is intuitive and computationally convenient, minimizing prediction error does not necessarily lead to high-quality decisions.

This misalignment arises because small prediction errors can result in large changes in the optimal solution of the optimization problem, especially in constrained or ill-conditioned settings. Consequently, improvements in predictive accuracy do not always translate into better downstream decision quality.

To address this issue, the Smart Predict-then-Optimize (SPO) framework proposes to directly incorporate the downstream optimization problem into the learning objective. Instead of optimizing prediction accuracy alone, SPO minimizes a decision-oriented loss, typically defined in terms of decision regret, thereby explicitly aligning the training objective with the quality of the resulting portfolio decisions.

This perspective is especially relevant in financial applications. As discussed earlier, stock return prediction is inherently difficult due to market noise, non-stationarity, and complex dynamics, making prediction errors inevitable. At the same time, financial decision-making places stringent requirements on robustness, stability, and risk control, where small prediction errors may lead to disproportionately large economic losses. Under such conditions, learning paradigms that explicitly optimize decision quality rather than pointwise prediction accuracy are particularly valuable. Recent work has further emphasized the importance of robustness in decision-focused learning by proposing regret-based loss functions that explicitly hedge against adverse decision outcomes Schutte et al. [[2024](https://arxiv.org/html/2601.04062v2#bib.bib31 "Robust losses for decision-focused learning")], motivating the adoption of robust SPO-based approaches for portfolio optimization.

Preliminary ideas related to this study were explored in an earlier conference version Wang and Hasuike [[2025](https://arxiv.org/html/2601.04062v2#bib.bib23 "An end-to-end portfolio optimization framework based on the spo paradigm")]. The present work substantially extends this line of research by providing a systematic evaluation and more comprehensive modeling. Building upon this initial investigation, the present study conducts a more systematic evaluation of SPO-based methods in portfolio optimization.

In addition, this study adopts PyEPO Tang and Khalil [[2024](https://arxiv.org/html/2601.04062v2#bib.bib24 "PyEPO: a pytorch-based end-to-end predict-then-optimize library for linear and integer programming")] to implement the SPO loss. PyEPO offers a convenient and flexible framework for SPO modeling and has been increasingly used in recent working papers and preprints.

## 3 Methodology

### 3.1 Smart Predict then Optimize (SPO) based model

In this study, we adopt a Smart Predict–then–Optimize (SPO) framework for portfolio optimization, where prediction and decision-making are tightly coupled through an optimization layer.
Due to the computational and implementation complexity associated with backpropagation through optimization problems, we focus on tractable yet expressive portfolio formulations within a unified decision-focused learning architecture.

To preserve model interpretability and adhere to the principle of Occam’s razor, we consistently employ linear models as predictors across all experimental settings. Linear predictors provide a transparent mapping from input features to asset return estimates, which facilitates interpretability and contributes to improved robustness of the resulting portfolio decisions.

![Refer to caption](x1.png)


Figure 1: Overview of the Smart Predict–then–Optimize (SPO) training pipeline for portfolio optimization.

Figure [1](https://arxiv.org/html/2601.04062v2#S3.F1 "Figure 1 ‣ 3.1 Smart Predict then Optimize (SPO) based model ‣ 3 Methodology ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets") illustrates the overall predictive–optimization pipeline.
Given input features 𝒙\bm{x}, a predictor produces estimated returns 𝒓^\hat{\bm{r}}, which are then passed to a parameterized portfolio optimization module to obtain the portfolio weights.
The resulting decision is evaluated using the SPO+ loss, enabling end-to-end training by propagating gradients through both the prediction model and the optimization layer.

Within this unified structure, different portfolio optimization models are instantiated by specifying different objective functions and optimization parameters, collectively denoted by Θ\Theta.
These instantiations reflect different investment objectives and practical trading considerations.
In the following, we consider three representative formulations: MaxReturn, MaxReturn with transaction fee, and MaxReturn with ℓ2\ell\_{2} weight regularization.

#### 3.1.1 MaxReturnSPO

We first consider the basic MaxReturn formulation, which serves as the simplest instantiation of the SPO framework and forms the foundation for subsequent extensions.

Given an input feature vector 𝒙∈ℝd\bm{x}\in\mathbb{R}^{d}, a trainable predictor fθ​(⋅)f\_{\theta}(\cdot) produces an estimate of the asset return vector:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓^=fθ​(𝒙).\hat{\bm{r}}=f\_{\theta}(\bm{x}). |  | (1) |

Based on the predicted returns, the portfolio decision is obtained by solving a return-maximization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘^=arg⁡max𝒘∈𝒲⁡𝒓^⊤​𝒘,\hat{\bm{w}}=\arg\max\_{\bm{w}\in\mathcal{W}}\hat{\bm{r}}^{\top}\bm{w}, |  | (2) |

where 𝒲\mathcal{W} denotes the feasible set of portfolio weights.

During training, the realized return vector 𝒓\bm{r} is assumed to be observable, and the corresponding oracle decision is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘⋆=arg⁡max𝒘∈𝒲⁡𝒓⊤​𝒘.\bm{w}^{\star}=\arg\max\_{\bm{w}\in\mathcal{W}}\bm{r}^{\top}\bm{w}. |  | (3) |

To enable end-to-end learning, we adopt the SPO+ surrogate loss, which provides a convex upper bound on the true decision regret:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒSPO+(𝒓^,𝒓)=max𝒘∈𝒲(2𝒓^−𝒓)⊤𝒘−𝒓⊤𝒘⋆.\mathcal{L}\_{\mathrm{SPO+}}(\hat{\bm{r}},\bm{r})=\max\_{\bm{w}\in\mathcal{W}}(2\hat{\bm{r}}-\bm{r})^{\top}\bm{w}-\bm{r}^{\top}\bm{w}^{\star}. |  | (4) |

#### 3.1.2 MaxReturn with transaction fee

To account for practical trading frictions, we extend the MaxReturnSPO framework by explicitly incorporating transaction fee into the portfolio optimization objective. Let 𝒘t−1\bm{w}\_{t-1} denote the portfolio held in the previous period. The decision variable is obtained by solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘^=arg⁡max𝒘∈𝒲⁡(𝒓^⊤​𝒘−γ​∥𝒘−𝒘t−1∥1),\hat{\bm{w}}=\arg\max\_{\bm{w}\in\mathcal{W}}\left(\hat{\bm{r}}^{\top}\bm{w}-\gamma\lVert\bm{w}-\bm{w}\_{t-1}\rVert\_{1}\right), |  | (5) |

where γ>0\gamma>0 controls the transaction fee intensity.

Notation.
Let 𝒓^∈ℝn\hat{\bm{r}}\in\mathbb{R}^{n} denote the predicted return vector,
𝒓∈ℝn\bm{r}\in\mathbb{R}^{n} the realized return vector,
𝒘∈ℝn\bm{w}\in\mathbb{R}^{n} the portfolio weight vector,
and 𝒲\mathcal{W} the feasible set of portfolios.
Let 𝒘t−1\bm{w}\_{t-1} denote the portfolio held in the previous period and
γ>0\gamma>0 the transaction-fee coefficient.
We define the value function

|  |  |  |
| --- | --- | --- |
|  | f​(𝒓^)=max𝒘∈𝒲⁡[(𝒓^−𝒓)⊤​𝒘−γ​‖𝒘−𝒘t−1‖1].f(\hat{\bm{r}})=\max\_{\bm{w}\in\mathcal{W}}\left[(\hat{\bm{r}}-\bm{r})^{\top}\bm{w}-\gamma\|\bm{w}-\bm{w}\_{t-1}\|\_{1}\right]. |  |

By Danskin’s theorem, if
𝒘~∈arg⁡max𝒘∈𝒲⁡(⋅)\tilde{\bm{w}}\in\arg\max\_{\bm{w}\in\mathcal{W}}(\cdot),
then 𝒘~∈∂𝒓^f​(𝒓^)\tilde{\bm{w}}\in\partial\_{\hat{\bm{r}}}f(\hat{\bm{r}}).

#### 3.1.3 MaxReturn with ℓ2\ell\_{2} Weight Regularization

We observe that the previous formulations may yield highly concentrated portfolios, occasionally allocating most of the capital to a single asset. Such extreme allocations are often undesirable in practice due to their instability and sensitivity to prediction errors. To alleviate this issue, we introduce an ℓ2\ell\_{2} regularization term on portfolio weights, which penalizes large positions and encourages more balanced and stable allocations.

Specifically, the portfolio decision is obtained by solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘^=arg⁡max𝒘∈𝒲⁡(𝒓^⊤​𝒘−γ​‖𝒘−𝒘t−1‖1−λ​‖𝒘‖22),\hat{\bm{w}}=\arg\max\_{\bm{w}\in\mathcal{W}}\left(\hat{\bm{r}}^{\top}\bm{w}-\gamma\|\bm{w}-\bm{w}\_{t-1}\|\_{1}-\lambda\|\bm{w}\|\_{2}^{2}\right), |  | (6) |

where 𝒓^∈ℝn\hat{\bm{r}}\in\mathbb{R}^{n} denotes the predicted return vector,
𝒘∈ℝn\bm{w}\in\mathbb{R}^{n} the portfolio weight vector,
𝒲\mathcal{W} the feasible set of portfolios,
𝒘t−1\bm{w}\_{t-1} the portfolio held in the previous period,
γ>0\gamma>0 the transaction fee coefficient, and
λ>0\lambda>0 the regularization parameter controlling the strength of the ℓ2\ell\_{2} penalty.
  
Since the ℓ2\ell\_{2} regularization term does not depend on the predicted returns, the resulting optimization problem remains affine in 𝒓^\hat{\bm{r}}, and gradients can still be propagated through the optimization layer using the SPO+ surrogate.

#### 3.1.4 RobustSPO

While the standard SPO framework optimizes portfolio decisions based on point
predictions of asset returns, such predictions are inevitably subject to
estimation errors.
To improve robustness against adverse prediction perturbations, we further
extend the MaxReturnSPO formulation by incorporating robustness into the
prediction–decision pipeline.

Specifically, we consider multiplicative perturbations applied to the predicted
return vector.
Let 𝜻∈ℝn\bm{\zeta}\in\mathbb{R}^{n} denote a perturbation vector and define
the perturbed prediction as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓~=𝒓^∘(1+𝜻),\tilde{\bm{r}}=\hat{\bm{r}}\circ(1+\bm{\zeta}), |  | (7) |

where ∘\circ denotes the element-wise product.
The perturbation is assumed to lie in the uncertainty set

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒰={𝜻:‖𝜻‖∞≤ρ},\mathcal{U}=\left\{\bm{\zeta}:\|\bm{\zeta}\|\_{\infty}\leq\rho\right\}, |  | (8) |

where ρ>0\rho>0 controls the maximum relative deviation of each asset return.

Given a perturbed prediction 𝒓~\tilde{\bm{r}}, the corresponding portfolio
decision is obtained by solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘~=arg⁡max𝒘∈𝒲⁡𝒓~⊤​𝒘.\tilde{\bm{w}}=\arg\max\_{\bm{w}\in\mathcal{W}}\tilde{\bm{r}}^{\top}\bm{w}. |  | (9) |

The robust SPO objective is then formulated as a worst-case regret minimization
problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minθ⁡max𝜻∈𝒰⁡(𝒓⊤​𝒘⋆−𝒓⊤​𝒘~),\min\_{\theta}\;\max\_{\bm{\zeta}\in\mathcal{U}}\left(\bm{r}^{\top}\bm{w}^{\star}-\bm{r}^{\top}\tilde{\bm{w}}\right), |  | (10) |

where 𝒘⋆\bm{w}^{\star} denotes the oracle portfolio under the realized return vector
𝒓\bm{r}.

In practice, the inner maximization over the uncertainty set is approximated via
Monte Carlo sampling.
For each mini-batch, multiple perturbed return predictions are generated, and
the maximum SPO+ loss among these scenarios is used for backpropagation.
This robust training procedure encourages the predictor to produce portfolio
decisions that are less sensitive to unfavorable prediction errors.

### 3.2 SoftmaxDFL

Motivated by prior work Zhang et al. [[2020](https://arxiv.org/html/2601.04062v2#bib.bib25 "Deep learning for portfolio optimization")] that proposes constructing
portfolio weights via a softmax layer and directly optimizing financial
performance metrics through a loss function, we also consider an alternative
learning-based portfolio allocation approach based on a fully differentiable
allocation structure.
As a differentiable baseline, we consider a neural allocator that directly maps
input features to portfolio weights via a softmax layer, denoted as
SoftmaxDFL.
Unlike SPO-based methods that predict returns and then solve an explicit
optimization problem, SoftmaxDFL learns the allocation policy end-to-end without
an explicit optimization layer.

![Refer to caption](x2.png)


Figure 2: Architecture of the SoftmaxDFL.

Given input features 𝒙\bm{x}, a linear inferencer fθ​(⋅)f\_{\theta}(\cdot) first produces
return estimates

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓^=fθ​(𝒙).\hat{\bm{r}}=f\_{\theta}(\bm{x}). |  | (11) |

A neural allocator gθ​(⋅)g\_{\theta}(\cdot) then maps 𝒓^\hat{\bm{r}} directly to portfolio
weights via a softmax layer:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘^=gθ​(𝒓^),\hat{\bm{w}}=g\_{\theta}(\hat{\bm{r}}), |  | (12) |

which ensures nonnegative weights that sum to one.
Unlike SPO-based methods, SoftmaxDFL does not solve an explicit optimization
problem in the forward pass.

The learned allocation is evaluated based on its realized portfolio performance.

MaxReturn optimizes portfolio performance by minimizing the negative
realized return:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒMaxReturn=−𝒓⊤​𝒘^.\mathcal{L}\_{\mathrm{MaxReturn}}=-\,\bm{r}^{\top}\hat{\bm{w}}. |  | (13) |

MaxSharpe considers risk-adjusted performance by minimizing a
differentiable surrogate of the Sharpe ratio:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒMaxSharpe=−𝒓⊤​𝒘^𝒘^⊤​Σ​𝒘^,\mathcal{L}\_{\mathrm{MaxSharpe}}=-\frac{\bm{r}^{\top}\hat{\bm{w}}}{\sqrt{\hat{\bm{w}}^{\top}\Sigma\hat{\bm{w}}}}, |  | (14) |

where Σ\Sigma denotes the return covariance matrix estimated from the training
window.

### 3.3 Baselines

We consider two classical baselines for portfolio optimization.

#### 3.3.1 Max Sharpe Ratio

As a traditional optimization-based benchmark, we adopt the classical
mean–variance portfolio model.
Given the historical mean return vector 𝒓¯\bar{\bm{r}} and covariance matrix Σ\Sigma,
the optimal portfolio is obtained by solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘⋆=arg⁡max𝒘∈𝒲⁡𝒓¯⊤​𝒘𝒘⊤​Σ​𝒘.\bm{w}^{\star}=\arg\max\_{\bm{w}\in\mathcal{W}}\frac{\bar{\bm{r}}^{\top}\bm{w}}{\sqrt{\bm{w}^{\top}\Sigma\bm{w}}}. |  | (15) |

#### 3.3.2 Predict-then-Optimize (PtO)

As a Predict-then-Optimize (PtO) baseline, we combines a linear return predictor with the classical Markowitz model.
Specifically, given input features 𝒙\bm{x}, a linear model fθ​(⋅)f\_{\theta}(\cdot) is trained
to predict asset returns by minimizing the mean squared error:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒓^=fθ​(𝒙),minθ⁡‖𝒓^−𝒓‖22.\hat{\bm{r}}=f\_{\theta}(\bm{x}),\qquad\min\_{\theta}\;\|\hat{\bm{r}}-\bm{r}\|\_{2}^{2}. |  | (16) |

After training the predictor, the predicted returns are treated as fixed inputs
to the portfolio optimization stage.
The portfolio weights are then obtained by solving the Markowitz problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘PtO=arg⁡max𝒘∈𝒲⁡𝒓^⊤​𝒘.\bm{w}^{\mathrm{PtO}}=\arg\max\_{\bm{w}\in\mathcal{W}}\hat{\bm{r}}^{\top}\bm{w}. |  | (17) |

This baseline explicitly decouples return prediction and portfolio optimization,
and serves as a standard comparison to decision-focused learning approaches.

## 4 Experiment Setup

### 4.1 Data Description

To evaluate the proposed SPO framework for portfolio optimization, we employ daily historical data of U.S. exchange-traded funds (ETFs) as the experimental dataset from 2015/01/01 to 2025/01/01. Each asset in the investment universe corresponds to a tradable ETF, and the dataset spans multiple consecutive years of trading days, enabling a realistic portfolio backtesting environment.

At each trading day, the model takes return-based and technical indicator features derived from historical prices as inputs to predict the next-period asset returns (or equivalently, a cost vector), which are then fed into a portfolio optimization model to generate portfolio allocation weights. Specifically, the input features include:
  
(1) log returns, capturing short-term price movements;
  
(2) simple moving averages (SMA) and price bias, reflecting trend-following and mean-reversion characteristics;
  
(3) relative strength index (RSI) and MACD differences, capturing momentum and trend dynamics;
  
(4) Bollinger band width, measuring market volatility;
  
(5) volume-based indicators, reflecting trading activity and market participation.

These features jointly describe the market state of each asset from the perspectives of returns, trends, momentum, volatility, and trading behavior, providing economically meaningful inputs for the prediction models. This data setting naturally aligns with the decision-focused learning paradigm, where prediction quality is evaluated through downstream portfolio decisions and backtesting performance rather than pointwise forecasting accuracy.

### 4.2 Backtest Strategy

We evaluate all models using a rolling-window backtesting framework with monthly rebalancing, which reflects a realistic investment process. At each rebalancing month tt, the prediction model is retrained from scratch using only historical information available prior to tt.

![Refer to caption](x3.png)


Figure 3: Rolling-window backtesting protocol with monthly rebalancing and time-series validation.

As illustrated in Figure  [3](https://arxiv.org/html/2601.04062v2#S4.F3 "Figure 3 ‣ 4.2 Backtest Strategy ‣ 4 Experiment Setup ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets"), for each month tt, we construct a fixed-length training window covering the past 12 months [t−12,t−3][t-12,\,t-3], followed by a time-ordered validation period [t−3,t][t-3,\,t]. The window is rolled forward by one month at each rebalancing step.

Within each rolling window, hyperparameters are selected via time-series validation by Optuna, preserving the temporal order of the data. After hyperparameter selection, the model is trained on the corresponding window and used to generate predicted return vectors, which serve as inputs to the portfolio optimization problem. The resulting portfolio is held over the out-of-sample period [t,t+1][t,\,t+1] until the next rebalancing date.

In all backtesting experiments, a proportional transaction fee of 0.005 is deducted
from portfolio returns based on portfolio turnover, measured by
‖𝒘t−𝒘t−1‖1\|\bm{w}\_{t}-\bm{w}\_{t-1}\|\_{1}, to account for realistic trading frictions.
This transaction fee is applied uniformly to all compared strategies.

### 4.3 Model Configuration

Table 1: Overview of compared strategies.

| Category | Strategies |
| --- | --- |
| SoftmaxDFL | Softmax-MaxReturn, Softmax-MaxSharpe |
| Robust SPO | RobustSPO (ρ=0.01\rho=0.01), RobustSPO (ρ=0.1\rho=0.1) |
| SPO | SPO+, SPO+ with Fee, SPO+ with turnover penalty |
| PtO baseline | PtO Markowitz |
| Classical baseline | MaxSharpe |




Table 2: Model Configuration of SPO models

|  |  |
| --- | --- |
| Parameter | Values |
| Proportional transaction fee γ\gamma | 0.005 |
| ℓ2\ell\_{2} weight regularization λ\lambda | 0.42 |
| Robustness radius ρ\rho | {0.01, 0.1} |
| Training epochs | 20 to 40 |
| Learning rate | 10−410^{-4} to 5×10−25\times 10^{-2} (log-uniform) |
| Batch size | 63 |
| Optimizer | Adam |




Table 3: Model Configuration of SoftmaxDFL models

| Parameter | Values |
| --- | --- |
| Hidden Layer | 32 |
| Training epochs | 20 to 40 |
| Learning rate | 10−410^{-4} to 5×10−25\times 10^{-2} (log-uniform) |
| Batch size | 63 |
| Optimizer | Adam |

## 5 Result and Discussion

### 5.1 Overall Backtest Performance

![Refer to caption](figures/Cumulative_Return.png)


Figure 4: Cumulative net asset value (NAV) curves of all compared strategies over the full backtest period (2016–2024).




Table 4: Overall backtest performance (2016–2024).Annualized return and volatility are reported on an annual basis.

| Strategy | Ret. | Vol. | Sharpe | Sortino | MaxDD |
| --- | --- | --- | --- | --- | --- |
| Softmax-MaxReturn | 4.11 | 13.75 | 0.362 | 0.331 | -32.20 |
| Softmax-MaxSharpe | 1.32 | 13.02 | 0.166 | 0.152 | -38.37 |
| RobustSPO (ρ=0.01\rho=0.01) | 9.67 | 15.09 | 0.688 | 0.660 | -27.79 |
| RobustSPO (ρ=0.1\rho=0.1) | 8.09 | 14.96 | 0.595 | 0.582 | -29.64 |
| PtO Markowitz | 9.00 | 14.76 | 0.659 | 0.624 | -30.22 |
| SPO+ (γ=0.005\gamma=0.005) | 10.54 | 15.75 | 0.715 | 0.699 | -28.51 |
| SPO+ (γ=0.005,λ=0.42\gamma=0.005,\ \lambda=0.42) | 7.69 | 15.74 | 0.550 | 0.512 | -30.18 |
| SPO+ | 14.05 | 19.09 | 0.785 | 0.728 | -28.71 |
| MaxSharpe | 7.13 | 13.63 | 0.574 | 0.514 | -26.33 |

Table [4](https://arxiv.org/html/2601.04062v2#S5.T4 "Table 4 ‣ 5.1 Overall Backtest Performance ‣ 5 Result and Discussion ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets") reports the overall backtesting performance of all compared strategies in terms of annualized return, volatility, Sharpe ratio, Sortino ratio, and maximum drawdown.

Overall, decision-focused learning approaches consistently outperform predict–then–optimize baselines and traditional portfolio optimization methods on a risk-adjusted basis.

Since the primary objective of this study is to improve *decision quality* rather than predictive accuracy alone, the predict–then–optimize (PtO) framework serves as the most relevant baseline for comparison.

Among all strategies, SPO+ achieves the highest annualized return (14.05%) and the best risk-adjusted performance, with a Sharpe ratio of 0.785 and a Sortino ratio of 0.728.
Although SPO+ exhibits relatively higher volatility, its superior return compensates for the increased risk, resulting in the most favorable overall performance.

The SPO+ with fee variant also performs competitively, delivering strong risk-adjusted returns while explicitly accounting for trading costs.
In contrast, introducing the ℓ2\ell\_{2} weight regularization term leads to a more conservative and diversified allocation, reducing both return and Sharpe ratio while maintaining drawdown levels comparable to other baselines.

Softmax-based strategies fail to outperform other approaches in either return or risk-related metrics.
Despite their end-to-end differentiable structure, these models do not exhibit clear advantages over predict–then–optimize or decision-focused methods in the present setting.
This performance gap may be attributed to the limited interpretability and training instability of deep neural networks when applied to noisy and non-stationary financial data, which can adversely affect the quality of the induced portfolio decisions.

### 5.2 Performance during the COVID-19 Market Crisis

![Refer to caption](figures/2020COVID.png)


Figure 5: 
Cumulative net asset value (NAV) trajectories of selected strategies
during the COVID-19 market turmoil in 2020.
The inset zooms in on the early crash period from January to April 2020.
During this interval, the RobustSPO (ρ=0.1\rho=0.1) and
SPO+ with Fee strategies produce almost overlapping NAV paths,
suggesting that these models arrive at highly similar portfolio decisions
when facing severe market stress.
This behavior indicates that, under extreme market conditions, the
SPO+ with Fee solution is already sufficiently conservative due to binding constraints
and transaction cost penalties, such that additional robustness does not alter
the optimal allocation.




Table 5: Backtest performance during the COVID-19 period (January 2020–December 2020).

| Strategy | Ret. | Vol. | Sharpe | Sortino | MaxDD |
| --- | --- | --- | --- | --- | --- |
| Softmax-MaxReturn | -6.73 | 18.21 | -0.292 | -0.222 | -30.37 |
| Softmax-MaxSharpe | -4.72 | 16.51 | -0.210 | -0.161 | -26.65 |
| RobustSPO (ρ=0.01\rho=0.01) | 17.81 | 14.87 | 1.182 | 0.999 | -10.71 |
| RobustSPO (ρ=0.1\rho=0.1) | 46.92 | 18.61 | 2.170 | 2.322 | -9.58 |
| PtO Markowitz | 20.63 | 28.98 | 0.796 | 0.693 | -30.22 |
| SPO+ (γ=0.005\gamma=0.005) | 46.92 | 18.61 | 2.170 | 2.322 | -9.58 |
| SPO+ (γ=0.005,λ=0.42\gamma=0.005,\ \lambda=0.42) | -3.51 | 22.50 | -0.046 | -0.037 | -28.93 |
| SPO+ | 35.48 | 31.49 | 1.128 | 0.956 | -27.80 |
| MaxSharpe | 12.42 | 10.44 | 1.179 | 0.965 | -10.00 |

Table [5](https://arxiv.org/html/2601.04062v2#S5.T5 "Table 5 ‣ 5.2 Performance during the COVID-19 Market Crisis ‣ 5 Result and Discussion ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets") reports the backtesting performance of all strategies during the COVID-19 period from January 2020 to December 2020, which represents an extreme market regime characterized by elevated volatility and abrupt drawdowns.
Using the predict–then–optimize (PtO) Markowitz model as the primary baseline, we highlight metrics that outperform PtO to facilitate a clear comparison in terms of decision quality.

Overall, decision-focused learning methods exhibit substantial advantages over the PtO baseline during this turbulent period.
Both RobustSPO variants and SPO+ with Fee achieve significantly higher risk-adjusted performance, as reflected by markedly improved Sharpe and Sortino ratios, while simultaneously reducing maximum drawdowns relative to PtO.
In particular, RobustSPO (ρ=0.1\rho=0.1) and SPO+ with Fee demonstrate strong downside protection, with maximum drawdowns below 10%, compared to over 30% for the PtO baseline.

From a return perspective, several decision-focused models deliver higher annualized returns than PtO, indicating that explicitly incorporating the downstream optimization problem into the learning objective does not merely reduce risk but can also enhance profitability under stressed market conditions.
At the same time, the volatility levels of these models remain comparable to or lower than those of PtO, suggesting a more favorable risk–return trade-off.

In contrast, Softmax-based end-to-end allocation strategies perform poorly during the COVID-19 period, failing to outperform the PtO baseline across all evaluated metrics.
This observation suggests that fully differentiable allocation models without an explicit optimization structure may be more susceptible to estimation noise and training instability in highly non-stationary market environments.

Taken together, these results indicate that the benefits of decision-focused learning are particularly pronounced during adverse market regimes.
By aligning the learning objective directly with portfolio optimization outcomes, decision-focused models yield more robust and stable investment decisions than predict–then–optimize approaches when market uncertainty is elevated.

### 5.3 Performance during 2024 Bull Market

![Refer to caption](figures/2024Bull.png)


Figure 6: Cumulative net asset value (NAV) trajectories during the 2024 bull-market period.




Table 6: Backtest performance during the bull market period.

| Strategy | Ret. | Vol. | Sharpe | Sortino | MaxDD |
| --- | --- | --- | --- | --- | --- |
| Softmax-MaxReturn | 10.66 | 11.91 | 0.914 | 0.845 | -7.19 |
| Softmax-MaxSharpe | 8.79 | 12.09 | 0.760 | 0.713 | -7.02 |
| RobustSPO (ρ=0.01\rho=0.01) | 9.99 | 9.90 | 1.015 | 0.969 | -5.94 |
| RobustSPO (ρ=0.1\rho=0.1) | 9.38 | 10.59 | 0.903 | 0.856 | -5.99 |
| PtO Markowitz | 15.07 | 8.51 | 1.699 | 1.716 | -5.47 |
| SPO+ (γ=0.005\gamma=0.005) | 7.71 | 10.79 | 0.745 | 0.719 | -5.94 |
| SPO+ (γ=0.005,λ=0.42\gamma=0.005,\ \lambda=0.42) | 14.89 | 12.72 | 1.160 | 1.092 | -8.83 |
| SPO+ | 35.96 | 15.09 | 2.120 | 2.167 | -6.31 |
| MaxSharpe | 22.26 | 11.64 | 1.793 | 1.870 | -7.18 |

During the bull market period, models that explicitly incorporate turnover penalties or robustness constraints exhibit noticeably lower returns than the PtO Markowitz baseline.
This outcome is likely attributable to the more conservative investment behavior induced by these modeling choices, which restrains aggressive reallocation and leverage during sustained upward market trends.

This observation suggests that a substantial portion of PtO’s profitability is driven by its strong exposure to bullish market conditions.
However, it is noteworthy that the baseline SPO+ model still outperforms the PtO baseline in several key metrics, including annualized return and risk-adjusted performance.

This result indicates that, even without additional robustness or turnover constraints, decision-focused learning can effectively capture upside opportunities while maintaining a favorable risk–return trade-off.
In this sense, SPO+ strikes a balance between aggressiveness and stability, benefiting from bullish market dynamics without fully sacrificing robustness to market uncertainty.

## 6 Conclusion

In this study, we investigate decision-focused learning for portfolio optimization under a realistic rolling-window backtesting framework.
The empirical results demonstrate that aligning the learning objective with downstream portfolio decisions leads to consistently improved decision quality across different market regimes, compared with conventional predict–then–optimize approaches based on the Markowitz framework.

Our analysis highlights a fundamental trade-off between aggressiveness and robustness in portfolio construction.
While predict–then–optimize methods, including traditional Markowitz-based strategies, tend to benefit more from sustained bullish trends through stronger exposure to return forecasts, decision-focused models place greater emphasis on stability and downside risk control, resulting in superior performance under adverse market conditions.
Notably, the baseline SPO+ model achieves a balanced behavior across market regimes, outperforming traditional PtO baselines in several key metrics while maintaining the ability to capture upside opportunities without fully sacrificing robustness to market uncertainty.

These findings underscore the importance of incorporating decision awareness into learning-based portfolio optimization, particularly in environments characterized by noisy and non-stationary financial data, where purely prediction-driven Markowitz-style approaches may be insufficient to ensure robust decision quality.

## 7 Future Work

Several promising directions remain for future research. First, while the proposed framework accounts for decision-aware optimization under predicted returns, incorporating more advanced downside risk control mechanisms—such as distributionally robust optimization and Value-at-Risk (VaR)–type constraints may further enhance robustness against extreme market movements. Second, although the current study adopts simple and stable predictive models, future work may explore the integration of tree-based predictors within the decision-focused learning framework Elmachtoub et al. [[2020](https://arxiv.org/html/2601.04062v2#bib.bib33 "Decision trees for decision-making under the predict-then-optimize framework")]. From an empirical finance perspective, tree-based ensemble models have been shown to exhibit strong robustness in noisy return prediction tasks. For example, Krauss et al. Krauss et al. [[2017](https://arxiv.org/html/2601.04062v2#bib.bib14 "Deep neural networks, gradient-boosted trees, random forests: statistical arbitrage on the s&p 500")] demonstrate that random forests and gradient-boosted trees achieve competitive and often superior out-of-sample performance compared to deep neural networks in statistical arbitrage settings, where financial signals are characterized by low signal-to-noise ratios. This robustness makes tree-based predictors a promising direction for future integration into decision-focused portfolio optimization frameworks. Finally, despite the inclusion of diversification-promoting mechanisms, achieving an optimal balance between portfolio diversification and return maximization remains an open challenge. Developing principled approaches to jointly model this trade-off within decision-focused portfolio optimization frameworks constitutes an important direction for future research.

## References

* Y. Bai, Y. Gao, R. Wan, S. Zhang, and R. Song (2025)
  A review of reinforcement learning in financial applications.
  Annual Review of Statistics and Its Application 12,  pp. 209–232.
  External Links: [Document](https://dx.doi.org/10.1146/annurev-statistics-112723-034423)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p2.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* S. P. Boyd, E. Busseti, S. Diamond, R. N. Kahn, K. Koh, P. Nystrup, and J. Speth (2017)
  Multi-period trading via convex optimization.
  Foundations and Trends in Optimization 3,  pp. 1–76.
  Cited by: [§2.1](https://arxiv.org/html/2601.04062v2#S2.SS1.p3.1 "2.1 Portfolio Optimization Modeling ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* G. J. Deboeck (1994)
  Trading on the edge: neural, genetic, and fuzzy systems for chaotic financial markets.
   Wiley.
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p5.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* S. Deng and X. Min (2013)
  Applied optimization in global efficient portfolio construction using earning forecasts.
  The Journal of Investing 22 (4),  pp. 104–114.
  External Links: [Document](https://dx.doi.org/10.3905/joi.2013.22.4.104)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p4.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* Y. Deng, F. Bao, Y. Kong, Z. Ren, and Q. Dai (2017)
  Deep direct reinforcement learning for financial signal representation and trading.
  IEEE Transactions on Neural Networks and Learning Systems 28 (3),  pp. 653–664.
  External Links: [Document](https://dx.doi.org/10.1109/TNNLS.2016.2522401)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p2.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* A. N. Elmachtoub and P. Grigas (2022)
  Smart “predict, then optimize”.
  Management Science 68 (1),  pp. 9–26.
  External Links: [Document](https://dx.doi.org/10.1287/mnsc.2020.3922)
  Cited by: [§2.3](https://arxiv.org/html/2601.04062v2#S2.SS3.p1.1 "2.3 Smart Predict-then-Optimize (SPO) ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* A. N. Elmachtoub, J. C. N. Liang, and R. Mcnellis (2020)
  Decision trees for decision-making under the predict-then-optimize framework.
  In Proceedings of the 37th International Conference on Machine Learning, H. D. III and A. Singh (Eds.),
  Proceedings of Machine Learning Research, Vol. 119,  pp. 2858–2867.
  Cited by: [§7](https://arxiv.org/html/2601.04062v2#S7.p1.1 "7 Future Work ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* F. D. Freitas, A. F. De Souza, and A. R. de Almeida (2009)
  Prediction-based portfolio optimization model using neural networks.
  Neurocomputing 72 (10–12),  pp. 2155–2170.
  External Links: [Document](https://dx.doi.org/10.1016/j.neucom.2008.08.019)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p4.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* D. Goldfarb and G. Iyengar (2003)
  Robust portfolio selection problems.
  Mathematics of Operations Research 28 (1),  pp. 1–38.
  External Links: [Document](https://dx.doi.org/10.1287/moor.28.1.1.14260)
  Cited by: [§2.1](https://arxiv.org/html/2601.04062v2#S2.SS1.p1.1 "2.1 Portfolio Optimization Modeling ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* R. Jagannathan and T. Ma (2003)
  Risk reduction in large portfolios: why imposing the wrong constraints helps.
  The Journal of Finance 58 (4),  pp. 1651–1683.
  External Links: [Document](https://dx.doi.org/10.1111/1540-6261.00580)
  Cited by: [§2.1](https://arxiv.org/html/2601.04062v2#S2.SS1.p2.1 "2.1 Portfolio Optimization Modeling ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* Z. Jiang, D. Xu, and J. Liang (2017)
  A deep reinforcement learning framework for the financial portfolio management problem.
  arXiv preprint arXiv:1706.10059.
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p2.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* C. Krauss, X. A. Do, and N. Huck (2017)
  Deep neural networks, gradient-boosted trees, random forests: statistical arbitrage on the s&p 500.
  European Journal of Operational Research 259 (2),  pp. 689–702.
  External Links: [Document](https://dx.doi.org/10.1016/j.ejor.2016.10.031)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p4.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets"),
  [§7](https://arxiv.org/html/2601.04062v2#S7.p1.1 "7 Future Work ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* B. Lindemann, T. Müller, H. Vietz, N. Jazdi, and M. Weyrich (2021)
  A survey on long short-term memory networks for time series prediction.
  Procedia CIRP 99,  pp. 650–655.
  External Links: [Document](https://dx.doi.org/10.1016/j.procir.2021.03.088)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p6.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* X. Liu, Z. Xia, H. Yang, J. Gao, D. Zha, M. Zhu, C. D. Wang, Z. Wang, and J. Guo (2024)
  Dynamic datasets and market environments for financial reinforcement learning.
  Machine Learning.
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p2.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* Y. Liu, G. Qin, J. Wang, and M. Long (2023)
  ITransformer: inverted transformers are effective for time series forecasting.
  In International Conference on Learning Representations,
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p6.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* Y. Ma, R. Han, and W. Wang (2021)
  Portfolio optimization with return prediction using deep learning and machine learning.
  Expert Systems with Applications 165,  pp. 113973.
  External Links: [Document](https://dx.doi.org/10.1016/j.eswa.2020.113973)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p4.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* J. Mandi, J. Kotary, S. Berden, M. Mulamba, V. Bucarey, T. Guns, and F. Fioretto (2024)
  Decision-focused learning: foundations, state of the art, benchmark and future opportunities.
  Journal of Artificial Intelligence Research 80,  pp. 1623–1701.
  External Links: [Document](https://dx.doi.org/10.1613/jair.1.15320)
  Cited by: [§2.3](https://arxiv.org/html/2601.04062v2#S2.SS3.p1.1 "2.3 Smart Predict-then-Optimize (SPO) ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* H. Markowitz (1952)
  Portfolio selection.
  The Journal of Finance 7 (1),  pp. 77–91.
  Cited by: [§2.1](https://arxiv.org/html/2601.04062v2#S2.SS1.p1.1 "2.1 Portfolio Optimization Modeling ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* J. Moody and M. Saffell (2001)
  Learning to trade via direct reinforcement.
  IEEE Transactions on Neural Networks 12 (4),  pp. 875–889.
  External Links: [Document](https://dx.doi.org/10.1109/72.935097)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p2.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* Y. Nie, N. Nguyen, P. Sinthong, and J. Kalagnanam (2023)
  A time series is worth 64 words: long-term forecasting with transformers.
  In Advances in Neural Information Processing Systems,
  Vol. 36,  pp. 1–22.
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p6.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* F. D. Paiva, R. T. N. Cardoso, G. P. Hanaoka, and W. M. Duarte (2019)
  Decision-making for financial trading: a fusion approach of machine learning and portfolio selection.
  Expert Systems with Applications 115,  pp. 635–655.
  External Links: [Document](https://dx.doi.org/10.1016/j.eswa.2018.08.003)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p4.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* U. Pigorsch and S. Schäfer (2022)
  High-dimensional stock portfolio trading with deep reinforcement learning.
  In Proceedings of the IEEE Symposium on Computational Intelligence for Financial Engineering and Economics (CIFEr),
   pp. 1–8.
  External Links: [Document](https://dx.doi.org/10.1109/CIFEr52523.2022.9776121)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p2.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* R. T. Rockafellar and S. Uryasev (2000)
  Optimization of conditional value-at-risk.
  Journal of Risk 3,  pp. 21–41.
  Cited by: [§2.1](https://arxiv.org/html/2601.04062v2#S2.SS1.p1.1 "2.1 Portfolio Optimization Modeling ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* N. Schutte, K. Postek, and N. Yorke-Smith (2024)
  Robust losses for decision-focused learning.
  In Proceedings of the Thirty-Third International Joint Conference on
  Artificial Intelligence, IJCAI-24, K. Larson (Ed.),
   pp. 4868–4875.
  Note: Main Track
  External Links: [Document](https://dx.doi.org/10.24963/ijcai.2024/538)
  Cited by: [§2.3](https://arxiv.org/html/2601.04062v2#S2.SS3.p5.1 "2.3 Smart Predict-then-Optimize (SPO) ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* W. F. Sharpe (1998)
  The sharpe ratio.
  Journal of Portfolio Management 3 (3),  pp. 169–185.
  Cited by: [§2.1](https://arxiv.org/html/2601.04062v2#S2.SS1.p1.1 "2.1 Portfolio Optimization Modeling ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* B. Tang and E. B. Khalil (2024)
  PyEPO: a pytorch-based end-to-end predict-then-optimize library for linear and integer programming.
  Mathematical Programming Computation 16,  pp. 297–335.
  External Links: [Document](https://dx.doi.org/10.1007/s12532-024-00255-x)
  Cited by: [§2.3](https://arxiv.org/html/2601.04062v2#S2.SS3.p7.1 "2.3 Smart Predict-then-Optimize (SPO) ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* W. Wang, W. Li, N. Zhang, and K. Liu (2020)
  Portfolio formation with preselection using deep learning from long-term financial data.
  Expert Systems with Applications 143,  pp. 113042.
  External Links: [Document](https://dx.doi.org/10.1016/j.eswa.2019.113042)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p4.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* Y. Wang and T. Hasuike (2025)
  An end-to-end portfolio optimization framework based on the spo paradigm.
  Note: Preprint
  Cited by: [§2.3](https://arxiv.org/html/2601.04062v2#S2.SS3.p6.1 "2.3 Smart Predict-then-Optimize (SPO) ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* Y. Wang, H. Wu, J. Dong, G. Qin, H. Zhang, Y. Liu, Y. Qiu, J. Wang, and M. Long (2024)
  TimeXer: empowering transformers for time series forecasting with exogenous variables.
  In Advances in Neural Information Processing Systems,
  Vol. 37,  pp. 1–30.
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p6.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* A. Zeng, M. Chen, L. Zhang, and Q. Xu (2023)
  Are transformers effective for time series forecasting?.
  In Proceedings of the AAAI Conference on Artificial Intelligence,
  External Links: [Document](https://dx.doi.org/10.1609/aaai.v37i9.26317)
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p7.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* H. Zhang, H. Wu, G. Qin, J. Wang, and M. Long (2023)
  TimeMixer: decomposable multiscale mixing for time series forecasting.
  In Advances in Neural Information Processing Systems,
  Vol. 36,  pp. 1–23.
  Cited by: [§2.2](https://arxiv.org/html/2601.04062v2#S2.SS2.p6.1 "2.2 Learning-based Approaches ‣ 2 Literature Review ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").
* Z. Zhang, S. Zohren, and S. Roberts (2020)
  Deep learning for portfolio optimization.
  The Journal of Financial Data Science 2 (4),  pp. 8–20.
  External Links: [Document](https://dx.doi.org/10.3905/jfds.2020.1.042)
  Cited by: [§3.2](https://arxiv.org/html/2601.04062v2#S3.SS2.p1.1 "3.2 SoftmaxDFL ‣ 3 Methodology ‣ Smart Predict–then–Optimize Paradigm for Portfolio Optimization in Real Markets").