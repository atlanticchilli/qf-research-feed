---
authors:
- Yinhuan Li
- Chenxin Lyu
- Ruodu Wang
doc_id: arxiv:2603.01157v1
family_id: arxiv:2603.01157
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Adaptive Window Selection for Financial Risk Forecasting
url_abs: http://arxiv.org/abs/2603.01157v1
url_html: https://arxiv.org/html/2603.01157v1
venue: arXiv q-fin
version: 1
year: 2026
---


Yinhuan Li
  
Chenxin Lyu
  
Ruodu Wang
Department of Statistics and Actuarial Science, University of Waterloo, Canada. Email: wang@uwaterloo.ca

###### Abstract

Risk forecasts in financial regulation and internal management are calculated through historical data. The unknown structural changes of financial data poses a substantial challenge in selecting an appropriate look-back window for risk modeling and forecasting. We develop a data-driven online learning method, called the bootstrap-based adaptive window selection (BAWS), that adaptively determines the window size in a sequential manner.
A central component of BAWS is to compare the realized scores against a data-dependent threshold, which is evaluate based on an idea of bootstrap. The proposed method is applicable to the forecast of risk measures that are elicitable individually or jointly, such as the Value-at-Risk (VaR) and the pair of the VaR and the corresponding Expected Shortfall. Through simulation studies and empirical analyses, we demonstrate that BAWS generally outperforms the standard rolling window approach and the recently developed method of stability-based adaptive window selection, especially when there are structural changes in the data-generating process.

Keywords: Bootstrap, online learning, elicitability, Value-at-Risk, Expected Shortfall

## 1 Introduction

Forecasting risk measures is a fundamental task in risk management, playing a crucial role in capital reserving, regulatory compliance, and strategic decision-making. Commonly used risk measures, such as Value-at-Risk (VaR) and Expected Shortfall (ES), rely on the underlying loss distribution and are typically estimated using historical financial data. Regardless of the specific model employed, a central practical question is how much historical data should be used when forecasting risk measures. In reality, financial markets evolve with macroeconomic conditions and frequently experience unknown structural breaks, rendering the data highly non-stationary. For example, systemic shocks such as the 2008 global financial crisis (GFC) and the COVID-19 pandemic (COVID) triggered substantial changes in market dynamics and led to abrupt shifts in the loss distribution (Huber et al., [2021](#bib.bib37 "Market shocks and professionals’ investment behavior–evidence from the COVID-19 crash")).
Determining an appropriate estimation window under such changing market conditions therefore remains a challenging problem.

A rule-of-thumb for addressing this issue is the rolling window approach, which applies a fixed-length window that moves forward over time to update forecasts (Rapach and Zhou, [2013](#bib.bib21 "Forecasting stock returns")).
However, the choice of window size in this approach is typically ad hoc. Regulatory frameworks such as Basel II/III and the FRTB provide only minimum requirements, for instance, using at least 250 observations and an additional 12-month stress period for ES forecasts.
As a result, researchers and practitioners often rely on heuristics: DeMiguel et al. ([2009](#bib.bib34 "Optimal versus naive diversification: how inefficient is the 1/n portfolio strategy?")) and Capponi and Rubtsov ([2022](#bib.bib35 "Systemic risk-driven portfolio selection")) employ a five- or ten-year window for portfolio selection, while Hoga and Demetrescu ([2023](#bib.bib27 "Monitoring value-at-risk and expected shortfall forecasts")) and Wang et al. ([2025](#bib.bib26 "E-backtesting")) adopt 250- or 500-day windows for risk forecasting and backtesting.

Nevertheless, the rolling window approach faces several important limitations, as it implicitly assumes that the data are stationary within each fixed window.
The first limitation is that forecast performance is highly sensitive to the choice of window size (Rossi and Inoue, [2012](#bib.bib36 "Out-of-sample forecast tests robust to the choice of window size")). Such sensitivity can be understood through the bias–variance trade-off inherent in fixed-window estimation: a large window generally yields low-variance forecasts (estimates) but becomes highly biased when structural breaks occur, while a short window reduces the bias induced by the nonstationarity but produces more volatile forecasts.
The second limitation arises from the fixed-window mechanism itself, which cannot automatically adapt to evolving market conditions. Reliable risk forecasts must respond rapidly to changes in order to ensure adequate capital reserves; however, a fixed window tend to dilute extreme losses by averaging over excessive pre-shift data, leading to severe underestimation of risk. These limitations imply that no single window size can perform well across various market conditions, motivating the development of window selection strategies more resilient to distributional changes.

A growing literature studies the role of estimation window choice in forecasting when economic time series, such as financial returns, exhibit instabilities or structural breaks; see, e.g., Rapach and Zhou ([2013](#bib.bib21 "Forecasting stock returns")), Rossi ([2021](#bib.bib17 "Forecasting in the presence of instabilities: how we know whether models predict well and how to improve them")), and the references therein. Existing approaches to window selection and adaptive forecasting are typically motivated by parameter instability in predictive models.
Pesaran and Timmermann ([2007](#bib.bib18 "Selection of estimation window in the presence of breaks")) show that pre-break observations may remain informative for parameter estimation in the presence of one or multiple structural breaks. They propose two approaches exploiting the bias-variance trade-off: selecting a single estimation window via cross-validation, or combining forecasts obtained from different windows. Clark and McCracken ([2009](#bib.bib23 "Improving forecast accuracy by combining recursive and rolling forecasts")) further consider combinations of recursive and rolling forecasts, deriving optimal time-varying combination weights under abrupt parameter changes. Likewise, Inoue et al. ([2017](#bib.bib20 "Rolling window selection for out-of-sample forecasting with time-varying parameters")) study the selection of the optimal rolling window size for linear predictive models with time-varying coefficients and Feng and Zhang ([2025](#bib.bib22 "Forecasting realized volatility: the choice of window size"))
investigate the optimal rolling window size by comparing the prediction performance of volatility
under various window sizes via Diebold–Mariano test.
Beyond window selection, several studies have explored alternative ways to adaptively utilize historical information to improve forecasting performance. For instance, Pesaran et al. ([2013](#bib.bib19 "Optimal forecasts in the presence of structural breaks")) propose assigning optimal weights to past observations, Giraitis et al. ([2013](#bib.bib24 "Adaptive forecasting in the presence of recent and ongoing structural change")) focus on selecting an optimal rate of downweighting older data, and Wang et al. ([2021](#bib.bib25 "Forecasting stock returns: a time-dependent weighted least squares approach")) investigate time-varying weighting schemes for historical observations. Most, if not all, of these approaches are developed for linear predictive regression and aim to minimize mean squared forecast error (MSFE), thereby targeting conditional mean forecasts. Therefore, they are not directly applicable to risk forecasting, where the object of interest is the tail risk measure rather than the conditional mean.

Complementary to these studies, this paper aims to design a model-free adaptive window selection strategy for risk forecasting that dynamically searches for an optimal window while accounting for the bias-variance trade-off and adapting to market changes.
Our method builds upon stability-based adaptive window selection (SAWS) of Huang and Wang ([2025](#bib.bib14 "A stability principle for learning under nonstationarity")), which iteratively compares empirical losses across candidate windows using deterministic thresholds. While effective under some regularity conditions, such as strong convexity and smoothness, or Lipschitz continuity of the population loss function, their approach constructs thresholds purely based on the order of stochastic errors and ad-hoc predetermined constants, without incorporating the data characteristics. Moreover, the thresholding scheme does not generalize well beyond two classes of loss functions considered in Huang and Wang ([2025](#bib.bib14 "A stability principle for learning under nonstationarity")).
Inspired by the idea of rejection regions in hypothesis testing, we instead develop a bootstrap-based adaptive window selection (BAWS) framework, that constructs thresholds using the bootstrap method. The proposed procedure relies only on a single hyperparameter that can be interpreted as a threshold level, and yields a flexible window-selection rule suitable for a wide range of risk forecasting settings.

Our method compares forecasts obtained under a large window with those from smaller candidate windows using empirical scores, which requires scoring functions that are consistent for risk measures of interest. Elicitability provides this foundation:
a risk measure is elicitable if it can be represented as a minimizer of an expected scoring function; see Gneiting ([2011](#bib.bib12 "Making and evaluating point forecasts")), Fissler and Ziegel ([2016](#bib.bib5 "Higher order elicitability and Osband’s principle")) and Fissler et al. ([2025](#bib.bib15 "Elicitability and identifiability of tail risk measures")). This property allows us to apply the proposed adaptive window-selection framework to risk forecasting. VaR (quantile) is a prototypical example of elicitable risk measures, and although ES on its own is not elicitable, the pair (VaR, ES) is jointly elicitable (Acerbi and Szekely, [2014](#bib.bib6 "Backtesting expected shortfall"); Fissler et al., [2015](#bib.bib4 "Expected shortfall is jointly elicitable with value at risk-implications for backtesting")).
Some other popular statistical quantities that are elicitable include the mean, the (mean,variance) pair, and the expectile (Newey and Powell, [1987](#bib.bib3 "Asymmetric least squares estimation and testing")).
For relevance in risk forecasts, we focus on the adaptive window selection for VaR or ES forecasts, leveraging their (joint) elicitability to construct data-driven criteria for comparing competing candidate windows.

Through three simulation studies and a real data analysis, we demonstrate that the proposed BAWS approach generally shows superior out-of-sample performance, though not uniformly in every scenario. Across three non-stationary settings—discrete breaks, smooth and continuous changes, and time-varying volatility—our adaptive window approach delivers lower cumulative risk and forecast loss than fixed or full window approaches and are competitive with (often superior to) SAWS. For instance, under the GARCH volatility-shift design, our method attains the lowest MSE, cumulative risk, and forecast loss among all competing procedures, highlighting its favorable bias–variance trade-off and swift reaction to regime changes.

In the empirical analysis of the S&P 500 index from 2005 to 2025, the adaptive window methods (BAWS and SAWS) yield the low cumulative forecast loss and respond more promptly to extreme events, such as the 2008 financial crisis and the COVID-19 pandemic, while fixed and full windows react with substantial delays.

The paper is structured as follows. Section [2](#S2 "2 Methodology ‣ Adaptive Window Selection for Financial Risk Forecasting") states the research problem and introduces the bootstrap-based threshold, as well as the error control characterization. Section [3](#S3 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting") introduces the elicitability of risk measures, while Section [4](#S4 "4 Theoretical guarantee in a simple setting ‣ Adaptive Window Selection for Financial Risk Forecasting") presents some theoretical results and examples under two-regime switching. Section [5](#S5 "5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting") contains simulation results under three different scenarios. Section [6](#S6 "6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting") presents the empirical analysis of (VaR, ES) forecasts for the financial market. Section [7](#S7 "7 Conclusion ‣ Adaptive Window Selection for Financial Risk Forecasting") concludes the paper.

## 2 Methodology

### 2.1 Problem setup

Let
Θ⊆ℝd\Theta\subseteq\mathbb{R}^{d} be a dd-dimensional parameter space. We consider a stochastic process {Xt}t⩾1\{X\_{t}\}\_{t\geqslant 1}, where the random variable XtX\_{t} follows an unknown distribution ℙt\mathbb{P}\_{t} on ℝk\mathbb{R}^{k}. The time horizon can be finite or infinite.

Let ℓ:ℝk×Θ→ℝ\ell:\mathbb{R}^{k}\times\Theta\to\mathbb{R} be a known loss function, and
define the population loss at time tt as

|  |  |  |
| --- | --- | --- |
|  | Ft​(𝜽)=𝔼​[ℓ​(Xt,𝜽)].F\_{t}(\bm{\theta})=\mathbb{E}\!\left[\ell(X\_{t},\bm{\theta})\right]. |  |

The target parameter at time tt is the minimizer of the population loss,

|  |  |  |
| --- | --- | --- |
|  | 𝜽t∗=arg⁡min𝜽∈Θ⁡Ft​(𝜽).\bm{\theta}\_{t}^{\*}=\arg\min\_{\bm{\theta}\in\Theta}F\_{t}(\bm{\theta}). |  |

In practice, the distribution ℙt\mathbb{P}\_{t} is unknown, so the population loss
Ft​(𝜽)F\_{t}(\bm{\theta}) cannot be obtained directly.
Because the data arrive sequentially, the past observations
{x1,…,xt−1}\{x\_{1},\dots,x\_{t-1}\} are available at time tt.
If the data were stationary, a natural estimate of Ft​(𝜽)F\_{t}(\bm{\theta})
would be the full-sample average 1t−1​∑i=1t−1ℓ​(xi,𝜽).\frac{1}{t-1}\sum\_{i=1}^{t-1}\ell(x\_{i},\bm{\theta}).
However, in many cases, the distribution ℙt\mathbb{P}\_{t} may shift
over time due to discrete or continuous structural changes.
Including too much pre-break data in the estimation may introduce substantial
estimation bias.
A more robust strategy is therefore to approximate Ft​(𝜽)F\_{t}(\bm{\theta})
using only a recent look-back window of length kk, within which we believe that the distribution has no significant shift.
This leads to the empirical loss

|  |  |  |  |
| --- | --- | --- | --- |
|  | ft,k​(𝜽)=1k​∑i=t−kt−1ℓ​(xi,𝜽),f\_{t,k}(\bm{\theta})=\frac{1}{k}\sum\_{i=t-k}^{t-1}\ell(x\_{i},\bm{\theta}), |  | (1) |

based on {xi}t−kt−1\{x\_{i}\}\_{t-k}^{t-1} and the corresponding minimizer 𝜽^t,k∈arg⁡min𝜽∈Θ⁡ft,k​(𝜽)\hat{\bm{\theta}}\_{t,k}\in\arg\min\_{\bm{\theta}\in\Theta}f\_{t,k}(\bm{\theta})
serves as an approximation to the target parameter 𝜽t∗\bm{\theta}\_{t}^{\*}.

This paper focuses on selecting a largest window k^t\hat{k}\_{t} in which the distribution shift remains negligible, and then obtain the estimated parameter 𝜽^t,k^t\hat{\bm{\theta}}\_{t,\hat{k}\_{t}}.
We follow the selection framework in Huang and Wang ([2025](#bib.bib14 "A stability principle for learning under nonstationarity")), which is based on a stability principle: A statistically more stable solution is preferred unless it is significantly worse.
In other words, if {ℙi}i=t−kt−1\{\mathbb{P}\_{i}\}\_{i=t-k}^{t-1} are close, incorporating sufficient historical data can improve statistical efficiency without introducing a significantly higher bias.

Following Huang and Wang ([2025](#bib.bib14 "A stability principle for learning under nonstationarity")), we construct a pairwise test

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ti,k={1,if​ft,i​(𝜽^t,k)−ft,i​(𝜽^t,i)>τ​(t,i)0,if​ft,i​(𝜽^t,k)−ft,i​(𝜽^t,i)⩽τ​(t,i)T\_{i,k}=\begin{cases}1,~\text{if}~f\_{t,i}(\hat{\bm{\theta}}\_{t,k})-f\_{t,i}(\hat{\bm{\theta}}\_{t,i})>\tau(t,i)\\ 0,~\text{if}~f\_{t,i}(\hat{\bm{\theta}}\_{t,k})-f\_{t,i}(\hat{\bm{\theta}}\_{t,i})\leqslant\tau(t,i)\end{cases} |  | (2) |

for a candidate window size k∈[t−1]k\in[t-1] and each reference window size i<ki<k, where [t−1]={1,…,t−1}[t-1]=\{1,\dots,t-1\}. Since 𝜽^t,i\hat{\bm{\theta}}\_{t,i} is the minimizer of ft,i​(𝜽)f\_{t,i}(\bm{\theta}), 𝜽^t,k\hat{\bm{\theta}}\_{t,k} cannot achieve a lower loss within the smaller window ii, that is, ft,i​(𝜽^t,k)−ft,i​(𝜽^t,i)⩾0f\_{t,i}(\hat{\bm{\theta}}\_{t,k})-f\_{t,i}(\hat{\bm{\theta}}\_{t,i})\geqslant 0. Given a threshold functions τ​(t,i)\tau(t,i), Ti,k=0T\_{i,k}=0 would imply that 𝜽^t,k\hat{\bm{\theta}}\_{t,k} is not significantly worse than 𝜽^t,i\hat{\bm{\theta}}\_{t,i}. If Ti,k=0T\_{i,k}=0 holds for all i<ki<k, then window kk is regarded as
admissible, meaning that no significant distributional shift
is detected within {t−k,…,t−1}\{t-k,\dots,t-1\}.
We denote this by Tk=0T\_{k}=0. Otherwise, if Ti,k=1T\_{i,k}=1 for some i<ki<k, we set Tk=1T\_{k}=1, indicating a potential distribution shift over this period.

Smaller windows incorporate most recent observations and are more likely to reflect the current distribution ℙt\mathbb{P}\_{t}. Therefore, comparing each candidate window kk against all smaller windows provides a useful mechanism for detecting distributional changes over time. Our objective is to determine the largest admissible window k^t=max⁡{k∈[t−1]:Tk=0}\hat{k}\_{t}=\max\{k\in[t-1]:T\_{k}=0\} and further set 𝜽^t=𝜽^t,k^t\hat{\bm{\theta}}\_{t}=\hat{\bm{\theta}}\_{t,\hat{k}\_{t}}.

### 2.2 Bootstrap-based threshold specification

While large windows help reduce estimation variance, they increase the risk of bias due to potential distributional shifts. Thus, a well-specified threshold function is critical for balancing the bias-variance trade-off in estimation.

If no significant distribution shift occurs within a window ii, the distribution {ℙl}l=t−it−1\{\mathbb{P}\_{l}\}\_{l=t-i}^{t-1} should, if not identical, be sufficiently similar. It motivates us to develop a bootstrap-based method to construct the threshold τ​(t,i)\tau(t,i). The procedure is as follows: Choose a parameter β∈(0,1)\beta\in(0,1), typically close to 11, such as 0.90.9. For the time tt and the window size ii,

* •

  Step 1. Draw a sample of size ii with replacement from observations {xt−i,…,xt−1}\{x\_{t-i},\dots,x\_{t-1}\} and denote the sample as {xt−i(b),…,xt−1(b)}\{x\_{t-i}^{(b)},\dots,x\_{t-1}^{(b)}\}.
* •

  Step 2. Compute the bootstrapped objective function

  |  |  |  |
  | --- | --- | --- |
  |  | ft,i(b)​(𝜽)=1i​∑l=t−it−1f​(xl(b),𝜽),f\_{t,i}^{(b)}(\bm{\theta})=\frac{1}{i}\sum\_{l=t-i}^{t-1}f(x\_{l}^{(b)},\bm{\theta}), |  |

  and obtain the corresponding estimator by
  solving

  |  |  |  |
  | --- | --- | --- |
  |  | 𝜽^t,i(b)=arg​min𝜽∈Θ⁡ft,i(b)​(𝜽).\hat{\bm{\theta}}^{(b)}\_{t,i}=\operatorname\*{arg\,min}\_{\bm{\theta}\in\Theta}f\_{t,i}^{(b)}(\bm{\theta}). |  |
* •

  Step 3. Repeat Steps 1 and 2 BB times and derive the set {𝜽^t,i(b)}b=1B\{\hat{\bm{\theta}}^{(b)}\_{t,i}\}\_{b=1}^{B}.
* •

  Step 4. Calculate the empirical β\beta-quantile of

  |  |  |  |
  | --- | --- | --- |
  |  | {ft,i​(𝜽^t,i(b))−ft,i​(𝜽^t,i)}\{f\_{t,i}(\hat{\bm{\theta}}\_{t,i}^{(b)})-f\_{t,i}(\hat{\bm{\theta}}\_{t,i})\} |  |

  and use it as the threshold τ​(t,i)\tau(t,i), where the hyperparameter β∈(0,1)\beta\in(0,1) can be interpreted as a threshold level.

Under the pairwise null hypothesis

|  |  |  |
| --- | --- | --- |
|  | H0t,i,k:{Xt−k,…,Xt−i−1}​and​{Xt−i,…,Xt−1}​are identically distributed,H^{t,i,k}\_{0}:\ \{X\_{t-k},\ldots,X\_{t-i-1}\}\ \text{and}\ \{X\_{t-i},\ldots,X\_{t-1}\}\ \text{are identically distributed}, |  |

define the *theoretical* β\beta-quantile

|  |  |  |
| --- | --- | --- |
|  | qt,i,k​(β):=inf{q∈ℝ:ℙ​(ft,i​(θ^t,k)−ft,i​(θ^t,i)⩽q∣H0t,i,k)⩾β}.q\_{t,i,k}(\beta):=\inf\Bigl\{q\in\mathbb{R}:\ \mathbb{P}\bigl(f\_{t,i}\!\big(\hat{\theta}\_{t,k}\big)\;-\;f\_{t,i}\!\big(\hat{\theta}\_{t,i}\big)\leqslant q\mid H^{t,i,k}\_{0}\bigr)\geqslant\beta\Bigr\}. |  |

We approximate qt,i,k​(β)q\_{t,i,k}(\beta) by the bootstrap quantile q^t,i​(β)\hat{q}\_{t,i}(\beta) computed from

|  |  |  |
| --- | --- | --- |
|  | {ft,i​(θ^t,i(b))−ft,i​(θ^t,i)}b=1B,\Bigl\{\,f\_{t,i}(\hat{\theta}^{(b)}\_{t,i})-f\_{t,i}(\hat{\theta}\_{t,i})\,\Bigr\}\_{b=1}^{B}, |  |

and set τ​(t,i)=q^t,i​(β)\tau(t,i)=\hat{q}\_{t,i}(\beta). When the data within a window are approximately independent and identically distributed, the classic bootstrap method is useful and the above bootstrap procedure applies. For dependent data, a moving block bootstrap procedure is more suitable, as it accounts for temporal dependence; see Künsch ([1989](#bib.bib29 "The jackknife and the bootstrap for general stationary observations")). In this case, we replace Step 1 by Step 1\* and perform Steps 2-4 using the block sample obtained in Step 1\*. For given tt and ii, we define the block ℬt,i,l={xt−l−li+1,…,xt−l}\mathcal{B}\_{t,i,l}=\{x\_{t-l-l\_{i}+1},\dots,x\_{t-l}\} with the block length lil\_{i} satisfying li→∞l\_{i}\to\infty and mi=⌊i/li⌋→∞m\_{i}=\lfloor i/l\_{i}\rfloor\to\infty as i→∞i\to\infty. We select li=c​⌈i1/3⌉l\_{i}=c\lceil i^{1/3}\rceil for some positive constant cc.

* •

  Step 1∗. Resample mim\_{i} blocks with replacement from {ℬt,i,1​…​ℬt,i,i−li+1}\{\mathcal{B}\_{t,i,1}\dots\mathcal{B}\_{t,i,i-l\_{i}+1}\} and arrange all elements of mim\_{i} blocks in a sequence to get the bootstrapped sample {xt−mi​li(b),…,xt−1(b)}\{x\_{t-m\_{i}l\_{i}}^{(b)},\dots,x\_{t-1}^{(b)}\}.

In principle, all window sizes in the set {1,…,t−1}\{1,\dots,t-1\} could be considered.
However, very small windows tend to produce highly unstable estimates, so it is
reasonable to set a minimum window length k0k\_{0}. For computational efficiency, we adopt an increasing-interval strategy to construct a sparse but representative set of candidate windows. Specifically, window lengths grow more coarsely as they become larger. For example, we may use increments of 5 for windows below 50, increments of 10
for windows between 50 and 100, increments of 20 for windows between 100 and 300,
and increments of 50 between 300 and 1000.
Beyond length 1000, only increments of 100 (e.g., 1100, 1200, 1300, …)
are considered. The candidate set is further dynamically adjusted. When selecting the window at time tt, we incorporate the previously selected window k^t−1\hat{k}\_{t-1} as the useful reference. Windows smaller than k^t−1+1\hat{k}\_{t-1}+1 follow the increment rules above, while
larger windows are explored at increments of 50 starting from
k^t−1+1\hat{k}\_{t-1}+1 up to t−1t-1. We denote the candidate window set by 𝒦t\mathcal{K}\_{t}.

Since the data arrives sequentially, the proposed procedure can be applied
online to generate forecasts for the next period as new observations become
available. We refer to this framework as Bootstrap-based adaptive window selection (BAWS), which is summarized in Algorithm [1](#algorithm1 "In 2.2 Bootstrap-based threshold specification ‣ 2 Methodology ‣ Adaptive Window Selection for Financial Risk Forecasting"). We assume that observations are collected sequentially up to time T−1T-1,
and the forecasting procedure begins at an initial time point t0t\_{0}.

Input: Sequential data {xi}i=1T−1\{x\_{i}\}\_{i=1}^{T-1} and threshold level β\beta.

For t=t0,…,T:t=t\_{0},\dots,T:

For k∈𝒦tk\in\mathcal{K}\_{t}:

Using samples {xi}i=t−kt−1\{x\_{i}\}\_{i=t-k}^{t-1}, compute a minimizer 𝜽^t,k\hat{\bm{\theta}}\_{t,k} of ft,kf\_{t,k}, and

calculate τ​(t,k)\tau(t,k) via the bootstrap procedure;

For all i<ki<k and i∈𝒦ti\in\mathcal{K}\_{t}, judge if Ti,k=0T\_{i,k}=0; If so, let Tk=0T\_{k}=0.

Return k^t=max⁡{k∈𝒦t:Tk=0}\hat{k}\_{t}=\max\{k\in\mathcal{K}\_{t}:T\_{k}=0\} and the estimator 𝜽^t=𝜽^t,k^t\hat{\bm{\theta}}\_{t}=\hat{\bm{\theta}}\_{t,\hat{k}\_{t}}.

Output:  {k^t}t=T0T\{\hat{k}\_{t}\}\_{t=T\_{0}}^{T} and {𝜽^t}t=T0T\{\hat{\bm{\theta}}\_{t}\}\_{t=T\_{0}}^{T}.

Algorithm 1 Bootstrap-based adaptive window selection (BAWS)

### 2.3 Error control in window selection

Given a specific time tt and a window kk, the test procedure ([2](#S2.E2 "In 2.1 Problem setup ‣ 2 Methodology ‣ Adaptive Window Selection for Financial Risk Forecasting")) could be interpreted as testing a null hypothesis:

|  |  |  |
| --- | --- | --- |
|  | H0t,k:Xt−k,…,Xt−1∼ℙt.{H}\_{0}^{t,k}:X\_{t-k},\dots,X\_{t-1}\sim\mathbb{P}\_{t}. |  |

Under H0t,k{H}\_{0}^{t,k}, all observations in the window kk are drawn from the same distribution and we can use them to forecast the parameter at time tt.
It could be decomposed into a sequence of pairwise hypotheses: for i<ki<k,

|  |  |  |
| --- | --- | --- |
|  | H0t,i,k:Xt−k,…,Xt−i−1​has the same distribution as ​Xt−i,…,Xt−1.{H}\_{0}^{t,i,k}:~X\_{t-k},\dots,X\_{t-i-1}~\text{has the same distribution as }X\_{t-i},\dots,X\_{t-1}. |  |

In other words, if we assume that the most recent window ii can reflect the current distribution, then the larger window kk is tested for the distributional consistency with it.
Therefore, we can construct the reject region via the foregoing bootstrap-based method.

When ft,i​(𝜽^t,k)−ft,i​(𝜽^t,i)>τ​(t,i)f\_{t,i}(\hat{\bm{\theta}}\_{t,k})-f\_{t,i}(\hat{\bm{\theta}}\_{t,i})>\tau(t,i), we should reject the null hypothesis H0t,i,kH\_{0}^{t,i,k}. By definition of qt,i,k​(β)q\_{t,i,k}(\beta),

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ft,i​(θ^t,k)−ft,i​(θ^t,i)>qt,i,k​(β)∣H0t,i,k)=1−β.\mathbb{P}\!\left(f\_{t,i}\!\big(\hat{\theta}\_{t,k}\big)\;-\;f\_{t,i}\!\big(\hat{\theta}\_{t,i}\big)>q\_{t,i,k}(\beta)\mid H^{t,i,k}\_{0}\right)=1-\beta. |  |

Using the bootstrap-calibrated threshold τ​(t,i)=q^t,i​(β)\tau(t,i)=\hat{q}\_{t,i}(\beta) aims to match the pairwise Type-I error level,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ft,i​(θ^t,k)−ft,i​(θ^t,i)>τ​(t,i)∣H0t,i,k)≈1−β,\mathbb{P}\!\left(f\_{t,i}\!\big(\hat{\theta}\_{t,k}\big)\;-\;f\_{t,i}\!\big(\hat{\theta}\_{t,i}\big)>\tau(t,i)\mid H^{t,i,k}\_{0}\right)\approx 1-\beta, |  |

so that β\beta can be interpreted as the *pairwise* acceptance level (equivalently, 1−β1-\beta is the pairwise rejection probability under H0t,i,kH^{t,i,k}\_{0}).
Consequently, the FWER (family-wise error rate) bound
ℙ​(⋃i<k{ft,i​(θ^t,k)−ft,i​(θ^t,i)>τ​(t,i)}∣H0t,k)⩽∑i<kℙ​(ft,i​(θ^t,k)−ft,i​(θ^t,i)>τ​(t,i)∣H0t,i,k)\mathbb{P}\!\left(\bigcup\_{i<k}\{f\_{t,i}\!\big(\hat{\theta}\_{t,k}\big)\;-\;f\_{t,i}\!\big(\hat{\theta}\_{t,i}\big)>\tau(t,i)\}\mid H^{t,k}\_{0}\right)\leqslant\sum\_{i<k}\mathbb{P}\!\left(f\_{t,i}\!\big(\hat{\theta}\_{t,k}\big)\;-\;f\_{t,i}\!\big(\hat{\theta}\_{t,i}\big)>\tau(t,i)\mid H^{t,i,k}\_{0}\right)
is conservative due to strong dependence among nested tests.
In this study, we focus on controlling the PCER (per-comparison error rate) through the single tuning parameter β\beta. If one wishes to control the FWER at a pre-specified level, a standard Bonferroni correction can be applied as stated below. Let us fix a time tt and a candidate window length kk, and let α∈(0,1)\alpha\in(0,1) be a target FWER level. Let {αt,i∈(0,1)}i<k\{\alpha\_{t,i}\in(0,1)\}\_{i<k} be a collection of *local significance levels* where
∑i<kαt,i⩽α\sum\_{i<k}\alpha\_{t,i}\leqslant\alpha,
and choose thresholds {τ​(t,i)}i<k\{\tau(t,i)\}\_{i<k} such that, for every i<ki<k,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ft,i​(θ^t,k)−ft,i​(θ^t,i)>τ​(t,i)∣H0t,i,k)⩽αt,i.\mathbb{P}\!\left(f\_{t,i}\!\big(\hat{\theta}\_{t,k}\big)\;-\;f\_{t,i}\!\big(\hat{\theta}\_{t,i}\big)>\tau(t,i)\mid H\_{0}^{t,i,k}\right)\leqslant\alpha\_{t,i}. |  |

###### Proposition 1.

Under the global null H0t,k:Xt−k,…,Xt−1∼PtH\_{0}^{t,k}:\ X\_{t-k},\ldots,X\_{t-1}\sim P\_{t}, the family-wise error rate satisfies

|  |  |  |
| --- | --- | --- |
|  | ℙ(⋃i<k{ft,i(θ^t,k)−ft,i(θ^t,i)>τ(t,i)}|H0t,k)⩽∑i<kαt,i⩽α.\mathbb{P}\!\left(\bigcup\_{i<k}\{f\_{t,i}\!\big(\hat{\theta}\_{t,k}\big)\;-\;f\_{t,i}\!\big(\hat{\theta}\_{t,i}\big)>\tau(t,i)\}\,\middle|\,H\_{0}^{t,k}\right)\leqslant\sum\_{i<k}\alpha\_{t,i}\leqslant\alpha. |  |

###### Proof.

By the union bound,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ℙ(⋃i<k{ft,i(θ^t,k)−ft,i(θ^t,i)>τ(t,i)}|H0t,k)\displaystyle\mathbb{P}\!\left(\bigcup\_{i<k}\Bigl\{f\_{t,i}\!\big(\hat{\theta}\_{t,k}\big)-f\_{t,i}\!\big(\hat{\theta}\_{t,i}\big)>\tau(t,i)\Bigr\}\,\middle|\,H\_{0}^{t,k}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽∑i<kℙ(ft,i(θ^t,k)−ft,i(θ^t,i)>τ(t,i)|H0t,i,k)\displaystyle\leqslant\sum\_{i<k}\mathbb{P}\!\left(f\_{t,i}\!\big(\hat{\theta}\_{t,k}\big)-f\_{t,i}\!\big(\hat{\theta}\_{t,i}\big)>\tau(t,i)\,\middle|\,H\_{0}^{t,i,k}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽∑i<kαt,i⩽α.\displaystyle\leqslant\sum\_{i<k}\alpha\_{t,i}\leqslant\alpha. |  |

as desired.
∎

In particular, letting s:=|{i∈𝒦t:i<k}|s:=|\{i\in\mathcal{K}\_{t}:i<k\}| denote the number of pairwise comparisons for the candidate window kk,
the Bonferroni choice αt,i=α/s\alpha\_{t,i}=\alpha/s yields

|  |  |  |
| --- | --- | --- |
|  | ℙ(⋃i<k{ft,i(θ^t,k)−ft,i(θ^t,i)>τBon(t,i)}|H0t,k)⩽α,\mathbb{P}\!\left(\bigcup\_{i<k}\{f\_{t,i}\!\big(\hat{\theta}\_{t,k}\big)\;-\;f\_{t,i}\!\big(\hat{\theta}\_{t,i}\big)>\tau\_{\mathrm{Bon}}(t,i)\}\,\middle|\,H\_{0}^{t,k}\right)\leqslant\alpha, |  |

where τBon​(t,i)\tau\_{\mathrm{Bon}}(t,i) is any threshold satisfying
ℙ​(ft,i​(θ^t,k)−ft,i​(θ^t,i)>τBon​(t,i)∣H0t,i,k)⩽α/s\mathbb{P}(f\_{t,i}\!\big(\hat{\theta}\_{t,k}\big)\;-\;f\_{t,i}\!\big(\hat{\theta}\_{t,i}\big)>\tau\_{\mathrm{Bon}}(t,i)\mid H\_{0}^{t,i,k})\leqslant\alpha/s for all i<ki<k.

###### Remark 1.

In practice, τBon​(t,i)\tau\_{\mathrm{Bon}}(t,i) can be obtained by the same bootstrap procedure by replacing the pairwise level 1−β1-\beta with α/s\alpha/s (equivalently, using the bootstrap βBon\beta\_{\mathrm{Bon}}-quantile with βBon=1−α/s\beta\_{\mathrm{Bon}}=1-\alpha/s).

Because the candidate windows are nested and overlapping, the events that the difference will exceed the threshold are dependent, so Bonferroni-type FWER control can be conservative.
We therefore use β\beta as a single tuning parameter to target an approximate pairwise Type-I error level 1−β1-\beta; if FWER control is desired, Proposition 1 suggests tightening the pairwise level to approximately (1−β)/s(1-\beta)/s (equivalently, using βBon=1−(1−β)/s\beta\_{\mathrm{Bon}}=1-(1-\beta)/s in the bootstrap calibration).

## 3 Window selection for VaR and ES forecasts

Elicitability is useful in model selection, forecast comparison, and backtesting of financial risk measures; see Gneiting ([2011](#bib.bib12 "Making and evaluating point forecasts")) and Fissler et al. ([2015](#bib.bib4 "Expected shortfall is jointly elicitable with value at risk-implications for backtesting")).
We now apply BAWS to forecast elicitable risk measures, specifically VaR and ES, which are important for financial regulation and portfolio management practice; for VaR and ES in regulation, see Embrechts et al. ([2014](#bib.bib1 "An academic response to basel 3.5")) and McNeil et al. ([2015](#bib.bib2 "Quantitative risk management: concepts, techniques and tools-revised edition")).

Let Xt∼ℙtX\_{t}\sim\mathbb{P}\_{t} denote the random variable of the financial loss at time tt, and {x1,…,xt−1}\{x\_{1},\dots,x\_{t-1}\} be the observed historical losses over time. Recall that the VaR at level α∈(0,1)\alpha\in(0,1) for the loss XtX\_{t} is defined as

|  |  |  |
| --- | --- | --- |
|  | VaRα​(Xt)=inf{x∈ℝ:ℙ​(Xt⩽x)⩾α}.\mathrm{VaR}\_{\alpha}(X\_{t})=\inf\{x\in\mathbb{R}:\mathbb{P}(X\_{t}\leqslant x)\geqslant\alpha\}. |  |

Since VaR is elicitable (Gneiting, [2011](#bib.bib12 "Making and evaluating point forecasts")),
it can be characterized as the minimizer of an expected scoring function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα​(Xt)=arg​minv∈ℝ⁡𝔼​[SV,α​(Xt,v)]\mathrm{VaR}\_{\alpha}(X\_{t})=\operatorname\*{arg\,min}\_{v\in\mathbb{R}}\mathbb{E}\left[S\_{V,\alpha}(X\_{t},v)\right] |  | (3) |

with

|  |  |  |
| --- | --- | --- |
|  | SV,α​(x,v)=(𝟏​{x<v}−α)​[G​(v)−G​(x)]S\_{V,\alpha}(x,v)=({\bf 1}\{x<v\}-\alpha)\left[G(v)-G(x)\right] |  |

being a scoring function, where GG is a strictly increasing function such that the expectation 𝔼​[G​(X)]\mathbb{E}[G(X)] exists; see Fissler et al. ([2015](#bib.bib4 "Expected shortfall is jointly elicitable with value at risk-implications for backtesting")). Specifically, we can take G​(x)=xG(x)=x and then SV,α​(x,v)S\_{V,\alpha}(x,v) is known as the check function. Under the assumption of continuity of the quantile function of XtX\_{t} at α\alpha, VaRα​(Xt)\mathrm{VaR}\_{\alpha}(X\_{t}) is the unique minimizer of ([3](#S3.E3 "In 3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting")).

For the random variable XtX\_{t} with a finite mean, Expected Shortfall (ES) is defined as

|  |  |  |
| --- | --- | --- |
|  | ESα​(Xt)=11−α​∫α1VaRβ​(Xt)​dβ.\mathrm{ES}\_{\alpha}(X\_{t})=\frac{1}{1-\alpha}\int\_{\alpha}^{1}\mathrm{VaR}\_{\beta}(X\_{t})\mathrm{d}\beta. |  |

Since the pair (VaRα,ESα)(\mathrm{VaR}\_{\alpha},\mathrm{ES}\_{\alpha}) is jointly elicitable (Fissler and Ziegel, [2016](#bib.bib5 "Higher order elicitability and Osband’s principle")), we can obtain the pair by the following optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | (VaRα​(Xt),ESα​(Xt))=arg​min(v,e)∈ℝ2⁡𝔼​[SV,E,α​(Xt,v,e)],\left(\mathrm{VaR}\_{\alpha}(X\_{t}),\mathrm{ES}\_{\alpha}(X\_{t})\right)=\operatorname\*{arg\,min}\limits\_{(v,e)\in\mathbb{R}^{2}}\mathbb{E}\left[S\_{V,E,\alpha}(X\_{t},v,e)\right], |  | (4) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | SV,E,α​(x,v,e)\displaystyle S\_{V,E,\alpha}(x,v,e) | =(1​{x<v}−α)​[G1​(v)−G1​(x)]\displaystyle=(\textbf{1}\{x<v\}-\alpha)\left[G\_{1}(v)-G\_{1}(x)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +11−α​G2​(e)​1​{x⩾v}​(v−x)\displaystyle\quad+\frac{1}{1-\alpha}G\_{2}(e)\textbf{1}\{x\geqslant v\}(v-x) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +G2​(e)​(e−v)−𝒢2​(e),\displaystyle\quad+G\_{2}(e)(e-v)-{\mathcal{G}}\_{2}(e), |  | (5) |

where G1G\_{1} and G2G\_{2} are strictly increasing and continuously differentiable such that the expectation 𝔼​[G1​(Xt)]\mathbb{E}\left[G\_{1}(X\_{t})\right] exists, and

|  |  |  |
| --- | --- | --- |
|  | limx→+∞G2​(x)=0​and​𝒢2′=G2.\lim\_{x\to+\infty}G\_{2}(x)=0~\text{and}~{\mathcal{G}}^{\prime}\_{2}=G\_{2}. |  |

As we define the risk measure based on the loss rather than the return, ([3](#S3.Ex20 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting")) and the corresponding conditions are induced from Corollary 5.5 of Fissler and Ziegel ([2016](#bib.bib5 "Higher order elicitability and Osband’s principle")). Note that any specification of G1​(x)G\_{1}(x) and G2​(x)G\_{2}(x) satisfying the above properties will lead to the unique minimizer of ([4](#S3.E4 "In 3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting")). Here, we set
G1​(x)=xG\_{1}(x)=x and G2​(x)=−exp⁡{−x}1+exp⁡{−x}G\_{2}(x)=-\frac{\exp\{-x\}}{1+\exp\{-x\}}, following Fissler and Ziegel ([2016](#bib.bib5 "Higher order elicitability and Osband’s principle")).

When the distribution ℙt\mathbb{P}\_{t} is unknown, expected scores in ([3](#S3.E3 "In 3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting")) and ([4](#S3.E4 "In 3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting")) need to be approximated using the sample average of the observed data. Given a window of size kk and observations {xi}i=t−kt−1\{x\_{i}\}\_{i=t-k}^{t-1}, we estimate VaR and ES via empirical loss functions, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaR^α​(Xt)=arg​minv⁡1k​∑l=t−kt−1SV,α​(xl,v)\widehat{\mathrm{VaR}}\_{\alpha}(X\_{t})=\operatorname\*{arg\,min}\_{v}\frac{1}{k}\sum\_{l=t-k}^{t-1}S\_{V,\alpha}(x\_{l},v) |  | (6) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | (VaR^α​(Xt),ES^α​(Xt))=arg​minv,e⁡1k​∑l=t−kt−1SV,E,α​(xl,v,e),\left(\widehat{\mathrm{VaR}}\_{\alpha}(X\_{t}),\widehat{\mathrm{ES}}\_{\alpha}(X\_{t})\right)=\operatorname\*{arg\,min}\limits\_{v,e}\frac{1}{k}\sum\_{l=t-k}^{t-1}S\_{V,E,\alpha}(x\_{l},v,e), |  | (7) |

where VaR^α​(Xt)\widehat{\mathrm{VaR}}\_{\alpha}(X\_{t}) and ES^α​(Xt)\widehat{\mathrm{ES}}\_{\alpha}(X\_{t}) denote empirical VaR and ES, respectively.

To cope with potential structural changes in financial losses,
we apply the proposed window-selection framework to VaR and ES forecasting,
using the empirical loss functions in ([6](#S3.E6 "In 3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting")) and ([7](#S3.E7 "In 3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting"))
as particular cases of ft,kf\_{t,k} in ([1](#S2.E1 "In 2.1 Problem setup ‣ 2 Methodology ‣ Adaptive Window Selection for Financial Risk Forecasting")).

Beyond VaR and ES, the elicitability of many other classes of risk measures have been characterized in the literature. For instance, coherent risk measures have been studied by Ziegel ([2016](#bib.bib13 "Coherence and elicitability")), convex risk measures by Bellini and Bignozzi ([2015](#bib.bib8 "On elicitable risk measures")) and Delbaen et al. ([2016](#bib.bib9 "Risk measures with the cxls property")), tail risk measures by Liu and Wang ([2021](#bib.bib16 "A theory for measures of tail risk")) and Fissler et al. ([2025](#bib.bib15 "Elicitability and identifiability of tail risk measures")), and distortion risk measures by Kou and Peng ([2016](#bib.bib10 "On the measurement of economic tail risk")) and Wang and Ziegel ([2015](#bib.bib11 "Elicitable distortion risk measures: a concise proof")). Therefore, our proposed window selection strategy could be extended to other elicitable risk measures via the corresponding scoring functions.
In view of the importance of VaR and ES in financial practice, we omit the discussions on scoring functions for other risk measures.

## 4 Theoretical guarantee in a simple setting

The full BAWS procedure couples a data-dependent, bootstrap-calibrated threshold with a nested sequence of window comparisons, which makes a complete theoretical characterization technically challenging in general nonstationary settings.
To provide analytical insight, we therefore focus on a simplified setting with a single structural break within the candidate window, which isolates the key mechanism of the stability test and yields a clean, interpretable result. For the proof we only use the squared-loss specialization, under which the empirical risk minimizer is
μ^t,k=X¯t,k\hat{\mu}\_{t,k}=\bar{X}\_{t,k} and the stability statistic admits the exact identity

|  |  |  |
| --- | --- | --- |
|  | ft,i​(μ^t,k)−ft,i​(μ^t,i)=(X¯t,k−X¯t,i)2,i<k.f\_{t,i}(\hat{\mu}\_{t,k})-f\_{t,i}(\hat{\mu}\_{t,i})=\bigl(\bar{X}\_{t,k}-\bar{X}\_{t,i}\bigr)^{2},\qquad i<k. |  |

We consider the squared loss ℓ​(x,μ)=(x−μ)2\ell(x,\mu)=(x-\mu)^{2} and the empirical mean
μ^t,k=X¯t,k:=1k​∑l=t−kt−1Xl\hat{\mu}\_{t,k}=\bar{X}\_{t,k}:=\frac{1}{k}\sum\_{l=t-k}^{t-1}X\_{l}.
Under H1H\_{1}, assume that for some k0<kk\_{0}<k the window {t−k,…,t−1}\{t-k,\ldots,t-1\} contains a single change-point at t−k0t-k\_{0}, i.e.

|  |  |  |
| --- | --- | --- |
|  | Xt−k,…,Xt−k0−1∼P1,Xt−k0,…,Xt−1∼P2,X\_{t-k},\ldots,X\_{t-k\_{0}-1}\sim P\_{1},\qquad X\_{t-k\_{0}},\ldots,X\_{t-1}\sim P\_{2}, |  |

with 𝔼P1​[X]=μ1\mathbb{E}\_{P\_{1}}[X]=\mu\_{1} and 𝔼P2​[X]=μ2\mathbb{E}\_{P\_{2}}[X]=\mu\_{2}.
Assume k0→∞k\_{0}\to\infty, k−k0→∞k-k\_{0}\to\infty, and k0/k→0k\_{0}/k\to 0.

###### Theorem 1.

Let k^t\hat{k}\_{t} be the largest admissible window selected by BAWS. Then, under H1H\_{1},

|  |  |  |
| --- | --- | --- |
|  | ℙ​(k^t⩾k)→0,equivalentlyℙ​(k^t<k)→1.\mathbb{P}(\hat{k}\_{t}\geqslant k)\to 0,\qquad\text{equivalently}\qquad\mathbb{P}(\hat{k}\_{t}<k)\to 1. |  |

###### Proof.

Let τ​(t,k0)\tau(t,k\_{0}) be the threshold used in the stability test.
Recall that k^t\hat{k}\_{t} is the largest admissible window, i.e.

|  |  |  |
| --- | --- | --- |
|  | {k^t⩾k}⊆⋂i<k{ft,i​(μ^t,k)−ft,i​(μ^t,i)⩽τ​(t,i)}.\{\hat{k}\_{t}\geqslant k\}\subseteq\bigcap\_{i<k}\left\{f\_{t,i}(\hat{\mu}\_{t,k})-f\_{t,i}(\hat{\mu}\_{t,i})\leqslant\tau(t,i)\right\}. |  |

In particular, taking i=k0i=k\_{0} yields

|  |  |  |
| --- | --- | --- |
|  | {k^t⩾k}⊆{ft,k0​(μ^t,k)−ft,k0​(μ^t,k0)⩽τ​(t,k0)},\{\hat{k}\_{t}\geqslant k\}\subseteq\left\{f\_{t,k\_{0}}(\hat{\mu}\_{t,k})-f\_{t,k\_{0}}(\hat{\mu}\_{t,k\_{0}})\leqslant\tau(t,k\_{0})\right\}, |  |

hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(k^t​<k∣​H1)⩾ℙ​(ft,k0​(μ^t,k)−ft,k0​(μ^t,k0)>τ​(t,k0)|H1).\mathbb{P}(\hat{k}\_{t}<k\mid H\_{1})\ \geqslant\ \mathbb{P}\!\left(f\_{t,k\_{0}}(\hat{\mu}\_{t,k})-f\_{t,k\_{0}}(\hat{\mu}\_{t,k\_{0}})>\tau(t,k\_{0})\ \Big|\ H\_{1}\right). |  | (8) |

Under squared loss, for any μ\mu we have the identity

|  |  |  |
| --- | --- | --- |
|  | ft,k0​(μ)−ft,k0​(X¯t,k0)=(μ−X¯t,k0)2,f\_{t,k\_{0}}(\mu)-f\_{t,k\_{0}}(\bar{X}\_{t,k\_{0}})=(\mu-\bar{X}\_{t,k\_{0}})^{2}, |  |

therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | ft,k0​(μ^t,k)−ft,k0​(μ^t,k0)=(X¯t,k−X¯t,k0)2.f\_{t,k\_{0}}(\hat{\mu}\_{t,k})-f\_{t,k\_{0}}(\hat{\mu}\_{t,k\_{0}})=\big(\bar{X}\_{t,k}-\bar{X}\_{t,k\_{0}}\big)^{2}. |  | (9) |

Now decompose the kk-window mean under H1H\_{1} into the pre- and post-break parts:

|  |  |  |
| --- | --- | --- |
|  | X¯t,k=k−k0k​1k−k0​∑l=t−kt−k0−1Xl+k0k​1k0​∑l=t−k0t−1Xl,X¯t,k0=X¯2.\bar{X}\_{t,k}=\frac{k-k\_{0}}{k}\frac{1}{k-k\_{0}}\sum\_{l=t-k}^{t-k\_{0}-1}X\_{l}+\frac{k\_{0}}{k}\frac{1}{k\_{0}}\sum\_{l=t-k\_{0}}^{t-1}X\_{l},\qquad\bar{X}\_{t,k\_{0}}=\bar{X}\_{2}. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | X¯t,k−X¯t,k0=k−k0k​(X¯1−X¯2).\bar{X}\_{t,k}-\bar{X}\_{t,k\_{0}}=\frac{k-k\_{0}}{k}(\bar{X}\_{1}-\bar{X}\_{2}). |  |

By the weak law of large numbers,

|  |  |  |
| --- | --- | --- |
|  | X¯1→𝑝μ1,X¯2→𝑝μ2,\bar{X}\_{1}\xrightarrow{p}\mu\_{1},\qquad\bar{X}\_{2}\xrightarrow{p}\mu\_{2}, |  |

and since k−k0k→1\frac{k-k\_{0}}{k}\to 1, we obtain

|  |  |  |
| --- | --- | --- |
|  | X¯t,k−X¯t,k0→𝑝μ1−μ2,(X¯t,k−X¯t,k0)2→𝑝(μ1−μ2)2.\bar{X}\_{t,k}-\bar{X}\_{t,k\_{0}}\xrightarrow{p}\mu\_{1}-\mu\_{2},\qquad\big(\bar{X}\_{t,k}-\bar{X}\_{t,k\_{0}}\big)^{2}\xrightarrow{p}(\mu\_{1}-\mu\_{2})^{2}. |  |

Combining this with
ℙ​(τ​(t,k0)⩽(μ2−μ1)2−ε)→1\mathbb{P}(\tau(t,k\_{0})\leqslant(\mu\_{2}-\mu\_{1})^{2}-\varepsilon)\to 1,
it follows that

|  |  |  |
| --- | --- | --- |
|  | ℙ​((X¯t,k−X¯t,k0)2>τ​(t,k0)|H1)→1.\mathbb{P}\!\left(\big(\bar{X}\_{t,k}-\bar{X}\_{t,k\_{0}}\big)^{2}>\tau(t,k\_{0})\ \Big|\ H\_{1}\right)\to 1. |  |

Using ([9](#S4.E9 "In Proof. ‣ 4 Theoretical guarantee in a simple setting ‣ Adaptive Window Selection for Financial Risk Forecasting")) and then ([8](#S4.E8 "In Proof. ‣ 4 Theoretical guarantee in a simple setting ‣ Adaptive Window Selection for Financial Risk Forecasting")), we conclude that
ℙ​(k^t​<k∣​H1)→1\mathbb{P}(\hat{k}\_{t}<k\mid H\_{1})\to 1, i.e. ℙ​(k^t⩾k∣H1)→0\mathbb{P}(\hat{k}\_{t}\geqslant k\mid H\_{1})\to 0.
∎

###### Remark 2.

Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 4 Theoretical guarantee in a simple setting ‣ Adaptive Window Selection for Financial Risk Forecasting") is stated for a generic threshold τ​(t,i)\tau(t,i).
In BAWS, τ​(t,i)\tau(t,i) is implemented as a bootstrap quantile q^t,i​(β)\hat{q}\_{t,i}(\beta) constructed from the ii-window data as in Section 2.2.
Therefore, the conclusion of Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 4 Theoretical guarantee in a simple setting ‣ Adaptive Window Selection for Financial Risk Forecasting") applies provided the bootstrap-calibrated threshold satisfies
q^t,k0​(β)⩽(μ2−μ1)2−ε\hat{q}\_{t,k\_{0}}(\beta)\leqslant(\mu\_{2}-\mu\_{1})^{2}-\varepsilon with probability tending to one under H1H\_{1}.

Assume additionally that the pre- and post-break observations are independent Gaussian:

|  |  |  |
| --- | --- | --- |
|  | Xt−k,…,Xt−k0−1∼i.i.d.𝒩​(μ1,σ12),Xt−k0,…,Xt−1∼i.i.d.𝒩​(μ2,σ22),X\_{t-k},\ldots,X\_{t-k\_{0}-1}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}\mathcal{N}(\mu\_{1},\sigma\_{1}^{2}),\qquad X\_{t-k\_{0}},\ldots,X\_{t-1}\stackrel{{\scriptstyle\text{i.i.d.}}}{{\sim}}\mathcal{N}(\mu\_{2},\sigma\_{2}^{2}), |  |

with the two blocks independent. Then X¯t,k0∼𝒩​(μ2,σ22/k0)\bar{X}\_{t,k\_{0}}\sim\mathcal{N}(\mu\_{2},\sigma\_{2}^{2}/k\_{0}) and

|  |  |  |
| --- | --- | --- |
|  | X¯t,k=k−k0k​X¯1+k0k​X¯2,X¯1∼𝒩​(μ1,σ12k−k0),X¯2∼𝒩​(μ2,σ22k0),\bar{X}\_{t,k}=\frac{k-k\_{0}}{k}\bar{X}\_{1}+\frac{k\_{0}}{k}\bar{X}\_{2},\qquad\bar{X}\_{1}\sim\mathcal{N}\!\Big(\mu\_{1},\frac{\sigma\_{1}^{2}}{k-k\_{0}}\Big),\quad\bar{X}\_{2}\sim\mathcal{N}\!\Big(\mu\_{2},\frac{\sigma\_{2}^{2}}{k\_{0}}\Big), |  |

where X¯1\bar{X}\_{1} and X¯2\bar{X}\_{2} are independent. Define

|  |  |  |
| --- | --- | --- |
|  | mt,k0:=k−k0k​(μ1−μ2),vt,k0:=(k−k0k)2​(σ12k−k0+σ22k0).m\_{t,k\_{0}}:=\frac{k-k\_{0}}{k}(\mu\_{1}-\mu\_{2}),\qquad v\_{t,k\_{0}}:=\Big(\frac{k-k\_{0}}{k}\Big)^{2}\Big(\frac{\sigma\_{1}^{2}}{k-k\_{0}}+\frac{\sigma\_{2}^{2}}{k\_{0}}\Big). |  |

###### Corollary 1.

Conditioning on a fixed threshold τ​(t,k0)>0\tau(t,k\_{0})>0, under H1H\_{1} we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ((X¯t,k−X¯t,k0)2>τ(t,k0)|H1)\displaystyle\mathbb{P}\!\left(\big(\bar{X}\_{t,k}-\bar{X}\_{t,k\_{0}}\big)^{2}>\tau(t,k\_{0})\,\middle|\,H\_{1}\right) | =1−Φ​(τ​(t,k0)−mt,k0vt,k0)\displaystyle=1-\Phi\!\Big(\frac{\sqrt{\tau(t,k\_{0})}-m\_{t,k\_{0}}}{\sqrt{v\_{t,k\_{0}}}}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Φ​(−τ​(t,k0)−mt,k0vt,k0).\displaystyle\quad+\Phi\!\Big(\frac{-\sqrt{\tau(t,k\_{0})}-m\_{t,k\_{0}}}{\sqrt{v\_{t,k\_{0}}}}\Big). |  |

where Φ\Phi is the standard normal cumulative distribution function.

###### Proof.

Under the Gaussian block assumptions,
X¯t,k−X¯t,k0∼𝒩​(mt,k0,vt,k0)\bar{X}\_{t,k}-\bar{X}\_{t,k\_{0}}\sim\mathcal{N}(m\_{t,k\_{0}},v\_{t,k\_{0}}) under H1H\_{1}.
Let Y:=X¯t,k−X¯t,k0Y:=\bar{X}\_{t,k}-\bar{X}\_{t,k\_{0}} and write Y=mt,k0+vt,k0​ZY=m\_{t,k\_{0}}+\sqrt{v\_{t,k\_{0}}}\,Z with Z∼𝒩​(0,1)Z\sim\mathcal{N}(0,1).
Then

|  |  |  |
| --- | --- | --- |
|  | ℙ​(|Y|>τ)=ℙ​(Z>τ−mt,k0vt,k0)+ℙ​(Z<−τ−mt,k0vt,k0),\mathbb{P}(|Y|>\sqrt{\tau})=\mathbb{P}\!\left(Z>\frac{\sqrt{\tau}-m\_{t,k\_{0}}}{\sqrt{v\_{t,k\_{0}}}}\right)+\mathbb{P}\!\left(Z<\frac{-\sqrt{\tau}-m\_{t,k\_{0}}}{\sqrt{v\_{t,k\_{0}}}}\right), |  |

which equals the stated expression by the definition of Φ\Phi.
∎

###### Example 1 (Naive two-regime example: BAWS selects 250250 over 500500).

Let t=501t=501 and consider a single break at 250250:

|  |  |  |
| --- | --- | --- |
|  | X1,…,X250∼i​i​dℙ1,X251,…,X500∼i​i​dℙ2,X\_{1},\ldots,X\_{250}\stackrel{{\scriptstyle iid}}{{\sim}}\mathbb{P}\_{1},\qquad X\_{251},\ldots,X\_{500}\stackrel{{\scriptstyle iid}}{{\sim}}\mathbb{P}\_{2}, |  |

with 𝔼​[X]=μ1\mathbb{E}[X]=\mu\_{1} under ℙ1\mathbb{P}\_{1}, 𝔼​[X]=μ2\mathbb{E}[X]=\mu\_{2} under ℙ2\mathbb{P}\_{2}, and
Var⁡(Xt)=σ2<∞\operatorname{Var}(X\_{t})=\sigma^{2}<\infty for all t⩽500t\leqslant 500.
Restrict the candidate windows at time tt to {250,500}\{250,500\} and use squared loss
ℓ​(x,μ)=(x−μ)2\ell(x,\mu)=(x-\mu)^{2}, so that μ^t,k=X¯t,k\hat{\mu}\_{t,k}=\bar{X}\_{t,k}.

Suppose BAWS declares k∈{250,500}k\in\{250,500\} admissible if the stability test at i=250i=250 passes:

|  |  |  |
| --- | --- | --- |
|  | ft,250​(μ^t,k)−ft,250​(μ^t,250)⩽τ​(t,250)f\_{t,250}(\hat{\mu}\_{t,k})-f\_{t,250}(\hat{\mu}\_{t,250})\leqslant\tau(t,250) |  |

and

|  |  |  |
| --- | --- | --- |
|  | k^t=max⁡{k∈{250,500}:k​ is admissible}.\hat{k}\_{t}=\max\{k\in\{250,500\}:k\text{ is admissible}\}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | ℙ​(k^t=250)→1.\mathbb{P}(\hat{k}\_{t}=250)\to 1. |  |

To show this, fix t=501t=501. Since ℓ​(x,μ)=(x−μ)2\ell(x,\mu)=(x-\mu)^{2}, the empirical risk minimizer is the sample mean:

|  |  |  |
| --- | --- | --- |
|  | μ^t,k=X¯t,k:=1k​∑l=t−kt−1Xl.\hat{\mu}\_{t,k}=\bar{X}\_{t,k}:=\frac{1}{k}\sum\_{l=t-k}^{t-1}X\_{l}. |  |

Define

|  |  |  |
| --- | --- | --- |
|  | X¯1:=1250​∑l=1250Xl,X¯2:=1250​∑l=251500Xl.\bar{X}\_{1}:=\frac{1}{250}\sum\_{l=1}^{250}X\_{l},\qquad\bar{X}\_{2}:=\frac{1}{250}\sum\_{l=251}^{500}X\_{l}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | μ^t,250=X¯t,250=X¯2,μ^t,500=X¯t,500=250​X¯1+250​X¯2500=12​(X¯1+X¯2),\hat{\mu}\_{t,250}=\bar{X}\_{t,250}=\bar{X}\_{2},\qquad\hat{\mu}\_{t,500}=\bar{X}\_{t,500}=\frac{250\bar{X}\_{1}+250\bar{X}\_{2}}{500}=\frac{1}{2}(\bar{X}\_{1}+\bar{X}\_{2}), |  |

so

|  |  |  |
| --- | --- | --- |
|  | μ^t,500−μ^t,250=12​(X¯1−X¯2).\hat{\mu}\_{t,500}-\hat{\mu}\_{t,250}=\frac{1}{2}(\bar{X}\_{1}-\bar{X}\_{2}). |  |

Using the squared-loss identity, for any μ\mu,

|  |  |  |
| --- | --- | --- |
|  | ft,250​(μ)−ft,250​(μ^t,250)=(μ−μ^t,250)2,f\_{t,250}(\mu)-f\_{t,250}(\hat{\mu}\_{t,250})=\bigl(\mu-\hat{\mu}\_{t,250}\bigr)^{2}, |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | ft,250​(μ^t,500)−ft,250​(μ^t,250)=(μ^t,500−μ^t,250)2=14​(X¯1−X¯2)2.f\_{t,250}(\hat{\mu}\_{t,500})-f\_{t,250}(\hat{\mu}\_{t,250})=\bigl(\hat{\mu}\_{t,500}-\hat{\mu}\_{t,250}\bigr)^{2}=\frac{1}{4}(\bar{X}\_{1}-\bar{X}\_{2})^{2}. |  |

By the weak law of large numbers, X¯1→𝑝μ1\bar{X}\_{1}\xrightarrow{p}\mu\_{1} and X¯2→𝑝μ2\bar{X}\_{2}\xrightarrow{p}\mu\_{2}, hence

|  |  |  |
| --- | --- | --- |
|  | 14​(X¯1−X¯2)2→𝑝(μ2−μ1)24.\frac{1}{4}(\bar{X}\_{1}-\bar{X}\_{2})^{2}\ \xrightarrow{p}\ \frac{(\mu\_{2}-\mu\_{1})^{2}}{4}. |  |

Combining this with the naive condition on the threshold yields

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ft,250​(μ^t,500)−ft,250​(μ^t,250)>τ​(t,250))→1,\mathbb{P}\!\left(f\_{t,250}(\hat{\mu}\_{t,500})-f\_{t,250}(\hat{\mu}\_{t,250})>\tau(t,250)\right)\to 1, |  |

so k=500k=500 is inadmissible with probability tending to one. Therefore k^t=250\hat{k}\_{t}=250 with
probability tending to one.

## 5 Simulation studies

In this section, we conduct three simulation studies to evaluate the forecast performance of BAWS compared to various existing approaches. These simulations are designed to reflect real-world changes in financial markets, including abrupt break in market conditions, continuous changes in market trends, and time-varying volatility in market risk. Specifically, we employ mean and VaR estimation as simple illustrative examples to investigate the effect of window selection on their forecast performance. The details of these simulations are provided in Sections [5.1](#S5.SS1 "5.1 Scenario 1: Discrete structural changes ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting")-[5.3](#S5.SS3 "5.3 Scenario 3: Dynamic volatility shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting").

### 5.1 Scenario 1: Discrete structural changes

In this study, we consider the independent data exhibiting structural breaks over time. Here, the structural break refers to the abrupt change in the data-generating process, such as a sudden shift in the mean or variance parameter.

The simulated data xtx\_{t} is independently generated from a normal distribution N​(μt,σt2)N(\mu\_{t},\sigma^{2}\_{t}) with mean μt\mu\_{t} and variance σt2\sigma^{2}\_{t} for t=1,…,Tt=1,\dots,T, where T=2000T=2000. For a comprehensive evaluation, we consider three parameter settings in this scenario.

* •

  Setting A1 (Two regimes with an abrupt mean shift).
  The process has constant variance and a single break in the mean:

  |  |  |  |
  | --- | --- | --- |
  |  | μt={1,t⩽T/2,2,t>T/2,σt2=0.25.\mu\_{t}=\begin{cases}1,&t\leqslant T/2,\\ 2,&t>T/2,\end{cases}\qquad\sigma\_{t}^{2}=0.25. |  |
* •

  Setting A2 (Three regimes with piecewise-constant mean).
  The variance remains constant, while the mean exhibits two structural breaks:

  |  |  |  |
  | --- | --- | --- |
  |  | μt={1,t⩽800,0,800<t⩽1400,2,t>1400,σt2=0.25.\mu\_{t}=\begin{cases}1,&t\leqslant 800,\\ 0,&800<t\leqslant 1400,\\ 2,&t>1400,\end{cases}\qquad\sigma\_{t}^{2}=0.25. |  |
* •

  Setting A3 (Structural breaks in both mean and variance).
  The mean follows the same three-regime pattern as in Setting A2,
  while the variance changes as:

  |  |  |  |
  | --- | --- | --- |
  |  | σt2={0.25,t⩽800,1,800<t⩽1400,0.49,t>1400.\sigma\_{t}^{2}=\begin{cases}0.25,&t\leqslant 800,\\ 1,&800<t\leqslant 1400,\\ 0.49,&t>1400.\end{cases} |  |

The data is therefore piecewise stationary and an appropriate window is required for forecasting. We set the threshold level to β=0.9\beta=0.9 and estimate the thresholds using
500500 bootstrap replications. Each experiment is replicated
n=1000n=1000 times.
The forecasting procedure for both the mean and VaR begins at t0=501t\_{0}=501, and we compare our method with SAWS approach of Huang and Wang ([2025](#bib.bib14 "A stability principle for learning under nonstationarity")), the rolling window approach, and full (recursive) window approach. We consider the risk level of α=0.95\alpha=0.95 in VaR forecasting.

For the SAWS approach, we follow the parameter settings in Section 7.1 of
Huang and Wang ([2025](#bib.bib14 "A stability principle for learning under nonstationarity")), motivated by the fact that the expected loss
functions for mean and VaR forecasting are, respectively, strongly convex and smooth,
and Lipschitz continuous. Specifically, we set ατ=0.1\alpha\_{\tau}=0.1 and
Cτ=0.3C\_{\tau}=0.3 for mean forecasts, and ατ=0.1\alpha\_{\tau}=0.1 and
Cτ=0.5C\_{\tau}=0.5 for VaR forecasts.
At each time tt, the fixed-window approach uses rolling windows of
sizes k∈{250,500,750}k\in\{250,500,750\}, corresponding approximately to one-, two-,
and three-year windows. The full-window approach incorporates all available
historical observations up to time t−1t-1. For the fixed window with k=750k=750,
the full window is used whenever fewer than 750 past observations are available.

Table [1](#S5.T1 "Table 1 ‣ 5.1 Scenario 1: Discrete structural changes ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting") presents the mean absolute bias (MAB), mean variance, mean squared error (MSE), cumulative risk, and cumulative forecast loss of mean and VaR forecasts in various settings and the above comparable approaches. The mean absolute bias is computed as MAB=1T−t0+1​∑t=t0T|1n​∑l=1n𝜽^t(l)−𝜽t|\text{MAB}=\frac{1}{T-t\_{0}+1}\sum\_{t=t\_{0}}^{T}\big|\frac{1}{n}\sum\_{l=1}^{n}\hat{\bm{\theta}}\_{t}^{(l)}-\bm{\theta}\_{t}\big|, where 𝜽^t(l)\hat{\bm{\theta}}\_{t}^{(l)} is the estimated mean or VaR for the llth experiment and 𝜽t\bm{\theta}\_{t} is the corresponding true parameter at t{t}. Similarly, the average variance given by Var=1T−t0+1​∑t=t0T1n−1​∑l=1n(𝜽^t(l)−1n​∑l=1n𝜽^t(l))2\text{Var}=\frac{1}{T-t\_{0}+1}\sum\_{t=t\_{0}}^{T}\frac{1}{n-1}\sum\_{l=1}^{n}\left(\hat{\bm{\theta}}\_{t}^{(l)}-\frac{1}{n}\sum\_{l=1}^{n}\hat{\bm{\theta}}\_{t}^{(l)}\right)^{2} and the mean squared error is MSE=1T−t0+1​∑t=t0T1n​∑l=1n(𝜽^t(l)−𝜽t)2\text{MSE}=\frac{1}{T-t\_{0}+1}\sum\_{t=t\_{0}}^{T}\frac{1}{n}\sum\_{l=1}^{n}\left(\hat{\bm{\theta}}\_{t}^{(l)}-\bm{\theta}\_{t}\right)^{2}.
The cumulative risk (CR) over time is defined as the average cumulative excess risk based on the expected loss function F​(θ)F(\theta), given by

|  |  |  |
| --- | --- | --- |
|  | CR=1n​∑l=1n∑t=t0T{F​(𝜽^t(l))−F​(𝜽t)}:=1n​∑l=1n∑t=t0TCRt(l).\text{CR}=\frac{1}{n}\sum\_{l=1}^{n}\sum\_{t=t\_{0}}^{T}\left\{F(\hat{\bm{\theta}}\_{t}^{(l)})-F(\bm{\theta}\_{t})\right\}:=\frac{1}{n}\sum\_{l=1}^{n}\sum\_{t=t\_{0}}^{T}\text{CR}\_{t}^{(l)}. |  |

Particularly, CRt(l)=(𝜽^t(l)−μt)2\text{CR}\_{t}^{(l)}=(\hat{\bm{\theta}}\_{t}^{(l)}-\mu\_{t})^{2} for the mean forecast, and

|  |  |  |
| --- | --- | --- |
|  | CRt(l)=−α​𝜽^t(l)−𝔼​{xt​𝟙​(xt<𝜽^t(l))}+𝔼​{xt​𝟙​(xt<VaRt​(α))}+𝜽^t(l)​ℙ​(xt<𝜽^t(l))\text{CR}\_{t}^{(l)}=-\alpha\hat{\bm{\theta}}\_{t}^{(l)}-\mathbb{E}\{x\_{t}\mathds{1}(x\_{t}<\hat{\bm{\theta}}\_{t}^{(l)})\}+\mathbb{E}\{x\_{t}\mathds{1}(x\_{t}<\mathrm{VaR}\_{t}(\alpha))\}+\hat{\bm{\theta}}\_{t}^{(l)}\mathbb{P}(x\_{t}<\hat{\bm{\theta}}\_{t}^{(l)}) |  |

for the VaR forecast, where VaRt​(α)=μt+σt​Φ−1​(α)\text{VaR}\_{t}(\alpha)=\mu\_{t}+\sigma\_{t}\Phi^{-1}(\alpha), with Φ−1​(α)\Phi^{-1}(\alpha) being the α\alpha-quantile of the standard normal distribution and 𝟙​(⋅)\mathds{1}(\cdot) denoting the indicator function. Note that CR for estimated mean is equal to MSE multiplied by T−t0+1T-t\_{0}+1. Therefore, we omit the MSE of mean estimators for clarity. The average cumulative forecast loss is given by CL=1n​∑l=1n∑t=t0Tℓ​(xt,𝜽^t(l)).\text{CL}=\frac{1}{n}\sum\_{l=1}^{n}\sum\_{t=t\_{0}}^{T}\ell(x\_{t},\hat{\bm{\theta}}\_{t}^{(l)}). These values indicate the overall forecast performance across various approaches. The following findings are observed from Table [1](#S5.T1 "Table 1 ‣ 5.1 Scenario 1: Discrete structural changes ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting"):

First, across all three settings, both the mean and VaR forecast show that the rolling window approach uniformly outperforms the full-window benchmark in terms of MAB, CR, and CL. This is not surprising, as the full window is the optimal only when no structural break is present. Among rolling windows, although using a larger window achieves relatively small variance, MAB, MSE (for VaR), CR, and CL improve as the rolling-window size decreases from 750 to 250. This illustrates the sensitivity of forecast accuracy to the window size and highlights the importance of selecting an appropriate window rather than relying on prespecified choices.

Second, for the mean forecast, adaptive window selection methods (BAWS and SAWS) consistently produce lower absolute biases, cumulative risks, and forecast losses compared to rolling window approaches.
BAWS calibrates its threshold via bootstrap, making it data-driven and responsive to the local volatility. This is beneficial in more challenging environments, such as Setting A3, where the piecewise variance complicates window selection. The bootstrap threshold adjusts to changes in uncertainty and reduces the risk of selecting windows that mix pre- and post-break observations, whereas the deterministic threshold in SAWS cannot adapt to such changes. In more stable regimes (Settings A1-A2), BAWS and SAWS perform similarly, although BAWS has a slightly worse performance.

Third, for the VaR forecast, BAWS achieves the lowest absolute bias, MSE, CR, and CL across all considered settings, indicating a more favorable bias-variance trade-off and better out-of-sample performance than the competing approaches. This illustrates the empirical advantages of BAWS in forecasting the tail risk measure VaR.

Figures [1](#S5.F1 "Figure 1 ‣ 5.1 Scenario 1: Discrete structural changes ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting")-[3](#S5.F3 "Figure 3 ‣ 5.1 Scenario 1: Discrete structural changes ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting") showcase the temporal pattern of the estimated mean (left panels) and the estimated VaR (right panels) across simulation settings and forecasting methods. In the pre-break regime, all methods produce stable estimates that align closely with the true parameters. After a structural break occurs, the full-window benchmark continues to pool pre-break observations, and fixed rolling windows still mix pre- and post-break data for roughly one window length, thereby delaying adaptation to the new regime. In contrast, the adaptive window selection procedures react more rapidly to the break, with BAWS typically adjusting the selected window more decisively around the change point.

Table 1: The bias, variance, MSE, cumulative risk, and forecast loss for mean and VaR across BAWS, SAWS, fixed windows (250, 500, 750), and full window across Settings A1–A3.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mean |  | BAWS | SAWS | Fixed Window | | | Full |
|  | 250 | 500 | 750 |
| A1 | MAB | 0.0077 | 0.0083 | 0.0845 | 0.1678 | 0.2511 | 0.4631 |
| Var | 0.0079 | 0.0073 | 0.0010 | 0.0005 | 0.0003 | 0.0002 |
| CR | 17.9276 | 14.8314 | 85.5601 | 168.4481 | 251.7759 | 501.8624 |
| CL | 392.9567 | 389.8877 | 460.3182 | 543.2237 | 626.4365 | 876.6553 |
| A2 | MAB | 0.0169 | 0.0123 | 0.2514 | 0.5010 | 0.7106 | 0.7744 |
| Var | 0.0086 | 0.0088 | 0.0010 | 0.0005 | 0.0003 | 0.0002 |
| CR | 41.7347 | 22.6393 | 420.4758 | 836.3033 | 1188.3080 | 1201.3810 |
| CL | 417.3304 | 397.9329 | 795.9474 | 1211.8626 | 1564.1570 | 1577.5416 |
| A3 | MAB | 0.0216 | 0.0133 | 0.2516 | 0.5010 | 0.7106 | 0.7744 |
| Var | 0.0227 | 0.1941 | 0.0025 | 0.0012 | 0.0008 | 0.0004 |
| CR | 64.1937 | 297.7890 | 422.8770 | 837.5919 | 1189.3490 | 1201.7770 |
| CL | 1034.7530 | 1265.8910 | 1393.0080 | 1807.9140 | 2160.1410 | 2173.0750 |
| VaR |  | BAWS | SAWS | Fixed Window | | | Full |
|  | 250 | 500 | 750 |
| A1 | MB | 0.0597 | 0.1603 | 0.0478 | 0.0968 | 0.1360 | 0.2536 |
| Var | 0.0055 | 0.0131 | 0.0047 | 0.0025 | 0.0018 | 0.0013 |
| MSE | 0.0191 | 0.0722 | 0.0282 | 0.0501 | 0.0710 | 0.1254 |
| CR | 5.0391 | 20.3860 | 7.8254 | 14.5752 | 20.7891 | 35.3949 |
| CL | 82.3192 | 97.7356 | 85.1195 | 91.9120 | 98.1440 | 112.7323 |
| A2 | MAB | 0.0853 | 0.4371 | 0.1807 | 0.3592 | 0.4864 | 0.6068 |
| Var | 0.0082 | 0.0092 | 0.0052 | 0.0029 | 0.0021 | 0.0013 |
| MSE | 0.0587 | 0.3734 | 0.1563 | 0.3030 | 0.3927 | 0.5034 |
| CR | 11.9871 | 31.5068 | 26.3002 | 51.5869 | 54.4521 | 72.5658 |
| CL | 89.4111 | 108.9197 | 103.7431 | 129.0042 | 131.8705 | 149.9281 |
| A3 | MAB | 0.0810 | 0.1282 | 0.0839 | 0.1653 | 0.2351 | 0.3761 |
| Var | 0.0166 | 0.0214 | 0.0107 | 0.0047 | 0.0030 | 0.0017 |
| MSE | 0.0433 | 0.0577 | 0.0588 | 0.1017 | 0.1427 | 0.2868 |
| CR | 7.3705 | 9.5938 | 11.1873 | 20.7544 | 28.9645 | 59.8289 |
| CL | 128.1061 | 130.2987 | 131.8753 | 141.5166 | 149.7327 | 180.5282 |

![Refer to caption](2603.01157v1/x1.png)


Figure 1: The patterns of estimators over time under Setting A1.

![Refer to caption](2603.01157v1/x2.png)


Figure 2: The patterns of estimators over time under Setting A2.

![Refer to caption](2603.01157v1/x3.png)


Figure 3: The patterns of estimators over time under Setting A3.

### 5.2 Scenario 2: Continuous mean shifts

We next simulate dynamic mean shifts in the data-generating process, mimicking continuous and gradual changes in market trends over time. In this scenario, no historical observations are drawn from the same distribution as the future data. Nevertheless, we show that recent observations remain informative for future forecasts.

We consider the same data-generating distribution as Section [5.1](#S5.SS1 "5.1 Scenario 1: Discrete structural changes ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting"). Parameter settings are as follows:

* •

  Setting B1 (Mean generated by a sine function).
  The parameters are given by

  |  |  |  |
  | --- | --- | --- |
  |  | μt=sin⁡(2​π​tT),σt2=0.25,t=1,…,T.\mu\_{t}=\sin\!\left(\frac{2\pi t}{T}\right),\qquad\sigma\_{t}^{2}=0.25,\quad t=1,\ldots,T. |  |
* •

  Setting B2 (Mean generated by a Brownian motion).
  The mean parameter μt\mu\_{t} changes according to

  |  |  |  |
  | --- | --- | --- |
  |  | μt−μt−1​∼i.i.d.​N​(0,1/T),σt2=0.25,t=1,…,T.\mu\_{t}-\mu\_{t-1}\overset{\text{i.i.d.}}{\sim}N(0,1/T),\qquad\sigma\_{t}^{2}=0.25,\quad t=1,\ldots,T. |  |
* •

  Setting B3 (Mean generated by a geometric Brownian motion).
  The mean parameter follows

  |  |  |  |
  | --- | --- | --- |
  |  | μt=μ0​exp⁡((μ−12​σ2)​tT+σ​Wt),\mu\_{t}=\mu\_{0}\exp\!\left(\left(\mu-\tfrac{1}{2}\sigma^{2}\right)\frac{t}{T}+\sigma W\_{t}\right), |  |

  where Wt−Wt−1​∼i.i.d.​N​(0,1/T)W\_{t}-W\_{t-1}\overset{\text{i.i.d.}}{\sim}N(0,1/T) for t=1,…,Tt=1,\ldots,T.
  We set μ0=1\mu\_{0}=1, μ=0.5\mu=0.5, σ2=σt2=0.25\sigma^{2}=\sigma\_{t}^{2}=0.25.

Table [2](#S5.T2 "Table 2 ‣ 5.2 Scenario 2: Continuous mean shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting") summarizes the absolute bias, variance, MSE, cumulative risk, and forecast loss. Under Setting B1, the proposed approach attains the lowest absolute bias, MSE (for VaR), cumulative risk and forecast loss for both mean and VaR forecasting. Under Setting B2, it continues to deliver superior performance for mean forecasting and remains competitive for VaR forecasting. These results indicate that BAWS performs well in the environments with cyclic fluctuations (B1) or persistent stochastic drift (B2), where the long window is clearly mismatched with the current period and the bootstrap threshold effectively captures such deviation and rejects the overlong window. Under Setting B3, the performance of BAWS becomes slightly worse than the alternatives in terms of the cumulative risk and forecast loss, but is still comparable to the optimal approach (SAWS and fixed window (250) for mean and VaR forecast, respectively).

Figures [4](#S5.F4 "Figure 4 ‣ 5.2 Scenario 2: Continuous mean shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting")–[6](#S5.F6 "Figure 6 ‣ 5.2 Scenario 2: Continuous mean shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting") illustrate the estimation performance over time and are broadly consistent with Table [2](#S5.T2 "Table 2 ‣ 5.2 Scenario 2: Continuous mean shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting").
Under Settings B1 and B2, both BAWS and SAWS closely track the true mean dynamics, while for VaR forecasting BAWS performs substantially better than SAWS under the parameter settings of Section 7.1 in Huang and Wang ([2025](#bib.bib14 "A stability principle for learning under nonstationarity")). In contrast, the benchmark models respond with long lags. Under Setting B3, all approaches produce forecasts that deviate noticeably from the true path of mean and VaR.
Nevertheless, the proposed approach remains closer to the true dynamics, which is consistent with its low absolute bias reported in Table [2](#S5.T2 "Table 2 ‣ 5.2 Scenario 2: Continuous mean shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting"). Overall, the results suggest that BAWS is more effective in the environment with pronounced distribution changes, whereas its benefits may decline under some smoother scenarios.

Table 2: The bias, variance, MSE, cumulative risk, and forecast loss for mean and VaR across BAWS, SAWS, fixed windows (250, 500, 750), and full window across Settings B1–B3.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mean |  | BAWS | SAWS | Fixed Window | | | Full |
|  | 250 | 500 | 750 |
| B1 | MAB | 0.0488 | 0.0782 | 0.2277 | 0.4104 | 0.5269 | 0.6790 |
| Var | 0.0120 | 0.0099 | 0.0010 | 0.0005 | 0.0003 | 0.0002 |
| CR | 22.1111 | 25.9628 | 101.7474 | 330.5937 | 570.5037 | 952.2810 |
| CL | 397.4562 | 401.3663 | 477.2601 | 706.3232 | 946.2050 | 1327.7445 |
| B2 | MAB | 0.0538 | 0.0707 | 0.1368 | 0.1922 | 0.2306 | 0.3531 |
| Var | 0.0119 | 0.0099 | 0.0010 | 0.0005 | 0.0003 | 0.0002 |
| CR | 24.3699 | 25.8738 | 41.9695 | 74.8076 | 104.7016 | 255.1436 |
| CL | 399.6568 | 401.0672 | 417.1856 | 450.0374 | 479.8901 | 630.3935 |
| B3 | MAB | 0.0364 | 0.0469 | 0.0896 | 0.1289 | 0.1597 | 0.1817 |
| Var | 0.0100 | 0.0081 | 0.0010 | 0.0005 | 0.0003 | 0.0002 |
| CR | 17.9327 | 17.2064 | 20.0657 | 34.5248 | 53.1077 | 78.2319 |
| CL | 393.0637 | 392.3147 | 395.1584 | 409.7283 | 428.3650 | 453.5585 |
| VaR |  | BAWS | SAWS | Fixed Window | | | Full |
|  | 250 | 500 | 750 |
| B1 | MAB | 0.1277 | 0.8796 | 0.2463 | 0.4801 | 0.6688 | 0.9496 |
| Var | 0.0137 | 0.0046 | 0.0047 | 0.0026 | 0.0020 | 0.0013 |
| MSE | 0.0343 | 1.0879 | 0.0858 | 0.3287 | 0.6681 | 1.2127 |
| CR | 5.0469 | 52.7609 | 10.1735 | 27.6309 | 41.2991 | 57.8267 |
| CL | 82.4291 | 130.0980 | 87.5898 | 105.0332 | 118.6737 | 135.1667 |
| B2 | MAB | 0.1218 | 0.2737 | 0.1248 | 0.1668 | 0.1916 | 0.2801 |
| Var | 0.0077 | 0.0025 | 0.0047 | 0.0024 | 0.0017 | 0.0012 |
| MSE | 0.0279 | 0.1035 | 0.0277 | 0.0395 | 0.0509 | 0.1075 |
| CR | 5.3636 | 24.9300 | 4.8871 | 7.8038 | 10.6236 | 26.0673 |
| CL | 82.7521 | 102.3475 | 82.3065 | 85.2086 | 88.0052 | 103.4857 |
| B3 | MAB | 0.0836 | 0.1699 | 0.0853 | 0.1230 | 0.1478 | 0.1708 |
| Var | 0.0070 | 0.0012 | 0.0045 | 0.0023 | 0.0016 | 0.0011 |
| MSE | 0.0177 | 0.0446 | 0.0155 | 0.0229 | 0.0310 | 0.0451 |
| CR | 3.2406 | 9.3411 | 2.7337 | 4.1502 | 5.8178 | 9.4544 |
| CL | 80.6187 | 86.7233 | 80.0953 | 81.5247 | 83.1921 | 86.8311 |

![Refer to caption](2603.01157v1/x4.png)


Figure 4: The patterns of estimators over time under Setting B1.

![Refer to caption](2603.01157v1/x5.png)


Figure 5: The patterns of estimators over time under Setting B2.

![Refer to caption](2603.01157v1/x6.png)


Figure 6: The patterns of estimators over time under Setting B3.

### 5.3 Scenario 3: Dynamic volatility shifts

Lastly, we focus on scenarios where the volatility of the data-generating distribution gradually changes over time.

Following Hoga and Demetrescu ([2023](#bib.bib27 "Monitoring value-at-risk and expected shortfall forecasts")) and Wang et al. ([2025](#bib.bib26 "E-backtesting")), we adopt a skewed-tt GARCH(1,1) process:

|  |  |  |
| --- | --- | --- |
|  | Lt=−σt​εt,σt2=0.00001+0.04​Lt−12+γt​σt−12L\_{t}=-\sigma\_{t}\varepsilon\_{t},\sigma\_{t}^{2}=0.00001+0.04L\_{t-1}^{2}+\gamma\_{t}\sigma\_{t-1}^{2} |  |

and {εt}t=1T\{\varepsilon\_{t}\}\_{t=1}^{T} are i.i.d innovations from a skewed Student-tt distribution proposed by Fernández and Steel ([1998](#bib.bib28 "On Bayesian modeling of fat tails and skewness")), with zero mean, unit variance, degrees of freedom ν=5\nu=5 and skewness parameter r=0.95r=0.95. Let T=2000T=2000 and γt=0.7+0.25​𝟙​(t>1000)\gamma\_{t}=0.7+0.25\mathds{1}(t>1000), which indicates a structural change of the data-generating process after the time 10001000.

![Refer to caption](2603.01157v1/x7.png)


Figure 7: The pattern of VaR forecasts over time under GARCH setting.




Table 3: VaR forecasting under GARCH: bias, variance, MSE, cumulative risk, and loss for BAWS, SAWS, and fixed windows (250, 500, 750), and full window.

| GARCH | BAWS | SAWS | Fixed Window | | | Full |
| --- | --- | --- | --- | --- | --- | --- |
| 250 | 500 | 750 |
| MAB | 0.0034 | 0.0156 | 0.0031 | 0.0056 | 0.0081 | 0.0153 |
| Var | 1.6746 | 0.1771 | 1.5499 | 0.9016 | 0.5994 | 0.1979 |
| MSE | 0.0001 | 0.0006 | 0.0002 | 0.0003 | 0.0004 | 0.0005 |
| CR | 0.2816 | 1.5481 | 0.4175 | 0.6823 | 0.9021 | 1.5220 |
| CL | 4.1676 | 5.4367 | 4.2793 | 4.5471 | 4.7674 | 5.3874 |

* •

  Variances should be obtained by multiplying the reported numbers by 10−410^{-4}.

As the conditional mean of LtL\_{t} is zero, our objective is to forecast VaR of the process LtL\_{t}. As mentioned in Section [2.2](#S2.SS2 "2.2 Bootstrap-based threshold specification ‣ 2 Methodology ‣ Adaptive Window Selection for Financial Risk Forecasting"), when the data is serially dependent, the moving block bootstrap is more helpful to keep the dependence structure. We therefore perform this bootstrap method with B=500B=500 and li=⌈i1/3⌉l\_{i}=\lceil i^{1/3}\rceil . Table [3](#S5.T3 "Table 3 ‣ 5.3 Scenario 3: Dynamic volatility shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting") compares various approaches under the GARCH setting. Overall, BAWS delivers the reliable performance: it achieves the lowest MSE, CR, and CL among the considered methods, while its absolute bias is slightly higher than that of fixed window with length 250. In contrast, fixed-window benchmarks are less responsive to the dynamic change of volatility. The less restrictive threshold specification in SAWS tends to admit overly large windows and leads to the similar result as the full window approach. These findings indicate that BAWS is suitable for VaR forecasting when volatility evolves over time, which is also consistent with the pattern in Figure [7](#S5.F7 "Figure 7 ‣ 5.3 Scenario 3: Dynamic volatility shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting"). BAWS adjusts rapidly after the structural change in volatility dynamics and follows the true VaR path more closely over time. In contrast, the fixed window methods adapt more slowly to volatility shifts and achieve accurate forecasts only after all pre-break observations have been discarded.

Overall, these results highlight the importance of dynamically adjusting the window size to improve forecasting accuracy. While the rolling window approachs can accommodate non-stationarity to some extent, they lack the sensitivity to respond promptly to the most recent and substantial distribution shifts. The proposed approach addresses this limitation by incorporating the data characteristics into the threshold, thereby enhancing the overall estimation accuracy. This improvement, however, slightly compromises the statistical efficiency, as the method may occasionally select smaller sample sizes than necessary.

## 6 Empirical analysis

In this section, we apply BAWS to a real-world dataset and compare its VaR and ES forecast performance with the SAWS, rolling window, and full window approaches. Specifically, we analyze the daily losses, defined as the negative log-returns, of the S&P500 index from January 4, to October 30, 2025. As shown in Figure [8](#S6.F8 "Figure 8 ‣ 6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting"), this period includes several significant market fluctuations associated with the 2008 global financial crisis (GFC), COVID-19 pandemic (COVID), and Trump’s tariff policies (Tariff).

![Refer to caption](2603.01157v1/x8.png)


Figure 8: Realize losses of the S&P 500 index form January 1, 2005 to October 30 2025.

Using historical data, we perform a rolling estimation of the VaR and ES from December 28, 2006 to October 30, 2025 by employing adaptive windows determined by BAWS and SAWS methods, fixed windows of size {250,500,750}\{250,500,750\}, or full window. We perform the moving block bootstrap method with B=1000B=1000 and li=⌈i1/3⌉l\_{i}=\lceil i^{1/3}\rceil . Considering the non-stationarity of financial markets, we cap the maximum window of BAWS at 1000 to promptly discard the outdated information and ensure the computational efficiency. We consider the threshold level as 0.9. For SAWS approach, ατ\alpha\_{\tau} and CτC\_{\tau} are set as 0.1 and 0.05, respectively, considering the typical magnitude of financial loss data.

We evaluate the VaR forecast performance of various approaches by comparing their average forecast losses over the full prediction period (2006–2025) as well as across three extreme episodes (the GFC, the COVID-19 crisis, and the Trump’s tariff), as reported in Table [4](#S6.T4 "Table 4 ‣ 6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting").
Over the full out-of-sample period, BAWS attains the lowest average forecast loss, indicating a superior overall predictive accuracy. The sub-period results further suggest that BAWS remains competitive during three stress periods, supporting its ability to adapt to changing market conditions.

![Refer to caption](2603.01157v1/x9.png)


Figure 9: VaR and ES forecasts from December 28, 2006 to October 30, 2025 across various approaches. Left panel: Realized loss and VaR forecast. Right panel: Realized loss and ES forecast.

![Refer to caption](2603.01157v1/x10.png)


Figure 10: Temporal dynamics of optimal window sizes, VaR and ES forecasts during the 2008 global financial crisis. Top panel: Optimal window. Middle panel: VaR forecasts. Bottom panel: ES forecasts.

![Refer to caption](2603.01157v1/x11.png)


Figure 11: Temporal dynamics of optimal window sizes, VaR, and ES forecasts during COVID-19 pandemic. Top panel: Optimal window. Middle panel: VaR forecasts. Bottom panel: ES forecasts.

![Refer to caption](2603.01157v1/x12.png)


Figure 12: Temporal dynamics of optimal window sizes, VaR, and ES forecasts during 2025 Trump tariff policies. Top panel: Optimal window. Middle panel: VaR forecasts. Bottom panel: ES forecasts.

Figure [9](#S6.F9 "Figure 9 ‣ 6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting") depicts the temporal evolution of VaR and ES estimates across different methodologies. The left panel presents the dynamics of VaR estimates and the realized loss, while the right panel provides the corresponding ES estimates. These two panels jointly provide a comprehensive view of the forecast performance. As shown in the figure, BAWS and SAWS adjust more quickly around stress episodes, whereas longer fixed windows and the full window produce smoother trajectories with more pronounced inertia. In particular, SAWS exhibits sharper spikes in tail-risk forecasts during extreme-loss periods, suggesting an overreaction (overfitting) to transient shocks.

Figures [10](#S6.F10 "Figure 10 ‣ 6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting")–[12](#S6.F12 "Figure 12 ‣ 6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting") present the optimal window sizes and the corresponding VaR and ES estimates across three extreme events. Figure [10](#S6.F10 "Figure 10 ‣ 6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting") covers the period from July 2, 2007, to December 31, 2009, encompassing the 2008 financial crisis. Figure [11](#S6.F11 "Figure 11 ‣ 6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting") spans from December 2, 2019, to December 31, 2020, capturing the drastic market volatility during the COVID-19 pandemic. Figure [12](#S6.F12 "Figure 12 ‣ 6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting") corresponds to the period from January 3, 2025 to October 30, 2025, around the implementation of Trump’s tariff policies, which began on February 4, 2025, with additional measures introduced in April 2025. When the market undergoes significant changes, the market losses tend to deviate from historical trend. In such scenarios, a smaller window is typically preferred to reduce the deviation, as demonstrated in top panels in Figures [10](#S6.F10 "Figure 10 ‣ 6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting")-[12](#S6.F12 "Figure 12 ‣ 6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting"). As conditions stabilize, the selected window size tends to expand. Conversely, during periods of market stability, incorporating more data points helps decrease variance in the estimates. The forecast performance depicted in these figures is consistent with the results presented in Table [4](#S6.T4 "Table 4 ‣ 6 Empirical analysis ‣ Adaptive Window Selection for Financial Risk Forecasting"). The two adaptive window selection approaches outperform most fixed-window and full-window benchmarks overall.

Table 4: Average forecast loss across periods for BAWS, SAWS, fixed windows, and full window.

| Forecast Loss | BAWS | SAWS | Fixed Window | | | Full |
| --- | --- | --- | --- | --- | --- | --- |
| 250 | 500 | 750 |
| 2006–2025 | 2.2642 | 2.3145 | 2.3565 | 2.4118 | 2.4174 | 2.4447 |
| GFC | 3.2513 | 3.1852 | 3.6631 | 3.8319 | 4.0414 | 4.1779 |
| COVID | 4.0501 | 3.8752 | 4.1750 | 4.1057 | 4.2218 | 4.1412 |
| Tariff | 2.3124 | 2.3856 | 2.3891 | 2.4041 | 2.3021 | 2.3292 |

* •

  The numbers are expressed in percentage (%).

## 7 Conclusion

We propose BAWS, the bootstrap-based adaptive window selection method, for risk forecasting under non-stationarity. The method is driven by a stability test: candidate windows are compared with shorter reference windows using empirical scoring losses, and the largest admissible window is selected; the admissibility threshold is calibrated by bootstrap (with block bootstrap for dependent time series). On the theoretical side, we provide an exact characterization under squared loss, showing that overly long windows are rejected with high probability under a single mean shift, together with a two-regime example illustrating the resulting window choice. Simulations and an empirical study on S&P 500 for the period of 2005–2025 show that BAWS reduces cumulative forecast loss relative to fixed/full windows and are competitive with SAWS, adjusting around major market episodes. Substantial future work is needed to develop Type-I error control tailored to overlapping windows and incorporate uncertainty quantification into the bootstrap threshold to improve finite-sample validity.

## References

* C. Acerbi and B. Szekely (2014)
  Backtesting expected shortfall.
  Risk 27 (11),  pp. 76–81.
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* F. Bellini and V. Bignozzi (2015)
  On elicitable risk measures.
  Quantitative Finance 15 (5),  pp. 725–733.
  Cited by: [§3](#S3.p6.1 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").
* A. Capponi and A. Rubtsov (2022)
  Systemic risk-driven portfolio selection.
  Operations Research 70 (3),  pp. 1598–1612.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* T. E. Clark and M. W. McCracken (2009)
  Improving forecast accuracy by combining recursive and rolling forecasts.
  International Economic Review 50 (2),  pp. 363–395.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* F. Delbaen, F. Bellini, V. Bignozzi, and J. F. Ziegel (2016)
  Risk measures with the cxls property.
  Finance and Stochastics 20 (2),  pp. 433–453.
  Cited by: [§3](#S3.p6.1 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").
* V. DeMiguel, L. Garlappi, and R. Uppal (2009)
  Optimal versus naive diversification: how inefficient is the 1/n portfolio strategy?.
  The Review of Financial Studies 22 (5),  pp. 1915–1953.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* P. Embrechts, G. Puccetti, L. Rüschendorf, R. Wang, and A. Beleraj (2014)
  An academic response to basel 3.5.
  Risks 2 (1),  pp. 25–48.
  Cited by: [§3](#S3.p1.1 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").
* Y. Feng and Y. Zhang (2025)
  Forecasting realized volatility: the choice of window size.
  Journal of Forecasting 44 (2),  pp. 692–705.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* C. Fernández and M. F. Steel (1998)
  On Bayesian modeling of fat tails and skewness.
  Journal of the American Statistical Association 93 (441),  pp. 359–371.
  Cited by: [§5.3](#S5.SS3.p2.8 "5.3 Scenario 3: Dynamic volatility shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting").
* T. Fissler, F. Liu, R. Wang, and L. Wei (2025)
  Elicitability and identifiability of tail risk measures.
  Mathematical Finance,  pp. 1–14.
  External Links: [Document](https://dx.doi.org/10.1111/mafi.70016)
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§3](#S3.p6.1 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").
* T. Fissler, J. F. Ziegel, and T. Gneiting (2015)
  Expected shortfall is jointly elicitable with value at risk-implications for backtesting.
  arXiv preprint arXiv:1507.00244.
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§3](#S3.p1.1 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§3](#S3.p2.12 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").
* T. Fissler and J. F. Ziegel (2016)
  Higher order elicitability and Osband’s principle.
  The Annals of Statistics 44 (4),  pp. 1680–1707.
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§3](#S3.p3.2 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§3](#S3.p3.9 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").
* L. Giraitis, G. Kapetanios, and S. Price (2013)
  Adaptive forecasting in the presence of recent and ongoing structural change.
  Journal of Econometrics 177 (2),  pp. 153–170.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* T. Gneiting (2011)
  Making and evaluating point forecasts.
  Journal of the American Statistical Association 106 (494),  pp. 746–762.
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§3](#S3.p1.1 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§3](#S3.p2.13 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").
* Y. Hoga and M. Demetrescu (2023)
  Monitoring value-at-risk and expected shortfall forecasts.
  Management Science 69 (5),  pp. 2954–2971.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§5.3](#S5.SS3.p2.1 "5.3 Scenario 3: Dynamic volatility shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting").
* C. Huang and K. Wang (2025)
  A stability principle for learning under nonstationarity.
  Operations Research 73 (6),  pp. 3044–3064.
  External Links: [Document](https://dx.doi.org/10.1287/opre.2024.0766)
  Cited by: [§1](#S1.p5.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§2.1](#S2.SS1.p4.3 "2.1 Problem setup ‣ 2 Methodology ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§2.1](#S2.SS1.p5.21 "2.1 Problem setup ‣ 2 Methodology ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§5.1](#S5.SS1.p3.5 "5.1 Scenario 1: Discrete structural changes ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§5.1](#S5.SS1.p4.8 "5.1 Scenario 1: Discrete structural changes ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§5.2](#S5.SS2.p4.1 "5.2 Scenario 2: Continuous mean shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting").
* C. Huber, J. Huber, and M. Kirchler (2021)
  Market shocks and professionals’ investment behavior–evidence from the COVID-19 crash.
  Journal of Banking & Finance 133,  pp. 106247.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* A. Inoue, L. Jin, and B. Rossi (2017)
  Rolling window selection for out-of-sample forecasting with time-varying parameters.
  Journal of Econometrics 196 (1),  pp. 55–67.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* S. Kou and X. Peng (2016)
  On the measurement of economic tail risk.
  Operations Research 64 (5),  pp. 1056–1072.
  Cited by: [§3](#S3.p6.1 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").
* H. R. Künsch (1989)
  The jackknife and the bootstrap for general stationary observations.
  The Annals of Statistics 17 (3),  pp. 1217–1241.
  Cited by: [§2.2](#S2.SS2.p2.21 "2.2 Bootstrap-based threshold specification ‣ 2 Methodology ‣ Adaptive Window Selection for Financial Risk Forecasting").
* F. Liu and R. Wang (2021)
  A theory for measures of tail risk.
  Mathematics of Operations Research 46 (3),  pp. 1109–1128.
  Cited by: [§3](#S3.p6.1 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").
* A. J. McNeil, R. Frey, and P. Embrechts (2015)
  Quantitative risk management: concepts, techniques and tools-revised edition.
   Princeton university press.
  Cited by: [§3](#S3.p1.1 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").
* W. K. Newey and J. L. Powell (1987)
  Asymmetric least squares estimation and testing.
  Econometrica: Journal of the Econometric Society,  pp. 819–847.
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* M. H. Pesaran, A. Pick, and M. Pranovich (2013)
  Optimal forecasts in the presence of structural breaks.
  Journal of Econometrics 177 (2),  pp. 134–152.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* M. H. Pesaran and A. Timmermann (2007)
  Selection of estimation window in the presence of breaks.
  Journal of Econometrics 137 (1),  pp. 134–161.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* D. Rapach and G. Zhou (2013)
  Forecasting stock returns.
  In Handbook of Economic Forecasting,
  Vol. 2,  pp. 328–383.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§1](#S1.p4.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* B. Rossi and A. Inoue (2012)
  Out-of-sample forecast tests robust to the choice of window size.
  Journal of Business & Economic Statistics 30 (3),  pp. 432–453.
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* B. Rossi (2021)
  Forecasting in the presence of instabilities: how we know whether models predict well and how to improve them.
  Journal of Economic Literature 59 (4),  pp. 1135–1190.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* Q. Wang, R. Wang, and J. F. Ziegel (2025)
  E-backtesting.
  Management Science.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting"),
  [§5.3](#S5.SS3.p2.1 "5.3 Scenario 3: Dynamic volatility shifts ‣ 5 Simulation studies ‣ Adaptive Window Selection for Financial Risk Forecasting").
* R. Wang and J. F. Ziegel (2015)
  Elicitable distortion risk measures: a concise proof.
  Statistics & Probability Letters 100,  pp. 172–175.
  Cited by: [§3](#S3.p6.1 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").
* Y. Wang, X. Hao, and C. Wu (2021)
  Forecasting stock returns: a time-dependent weighted least squares approach.
  Journal of Financial Markets 53,  pp. 100568.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Adaptive Window Selection for Financial Risk Forecasting").
* J. F. Ziegel (2016)
  Coherence and elicitability.
  Mathematical Finance 26 (4),  pp. 901–918.
  Cited by: [§3](#S3.p6.1 "3 Window selection for VaR and ES forecasts ‣ Adaptive Window Selection for Financial Risk Forecasting").

BETA