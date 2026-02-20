---
authors:
- Srijan Sood
- Kassiani Papasotiriou
- Marius Vaiciulis
- Tucker Balch
doc_id: arxiv:2602.17098v1
family_id: arxiv:2602.17098
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative
  Study with Mean-Variance Optimization'
url_abs: http://arxiv.org/abs/2602.17098v1
url_html: https://arxiv.org/html/2602.17098v1
venue: arXiv q-fin
version: 1
year: 2026
---


Srijan Sood, 1
Kassiani Papasotiriou, 1
Marius Vaiciulis,2
Tucker Balch 1

###### Abstract

Portfolio Management is the process of overseeing a group of investments, referred to as a portfolio, with the objective of achieving predetermined investment goals. Portfolio optimization is a key component that involves allocating the portfolio assets so as to maximize returns while minimizing risk taken. It is typically carried out by financial professionals who use a combination of quantitative techniques and investment expertise to make decisions about the portfolio allocation.

Recent applications of Deep Reinforcement Learning (DRL) have shown promising results when used to optimize portfolio allocation by training model-free agents on historical market data. Many of these methods compare their results against basic benchmarks or other state-of-the-art DRL agents but often fail to compare their performance against traditional methods used by financial professionals in practical settings.
One of the most commonly used methods for this task is Mean-Variance Portfolio Optimization (MVO), which uses historical time series information to estimate expected asset returns and covariances, which are then used to optimize for an investment objective.

Our work is a thorough comparison between model-free DRL and MVO for optimal portfolio allocation. We detail the specifics of how to make DRL for portfolio optimization work in practice, also noting the adjustments needed for MVO. Backtest results demonstrate strong performance of the DRL agent across many metrics, including Sharpe ratio, maximum drawdowns, and absolute returns.\*\*\*Published at the FinPlan’23 Workshop, the 33rd International Conference on Automated Planning and Scheduling (ICAPS).

## 1 Introduction

Portfolio management is a key issue in the financial services domain. It involves allocating funds across a variety of assets, typically to generate uncorrelated returns while minimizing risk and operational costs. Portfolios can constitute holdings across asset classes (cash, bonds, equities, etc.), or can also be optimized within a specific asset class (e.g., picking the appropriate composition of stocks for an equity portfolio). Investors may choose to optimize for various performance criteria, often centered around maximizing portfolio returns relative to risk taken. Since the advent of Modern Portfolio Theory (Markowitz [1952](https://arxiv.org/html/2602.17098v1#bib.bib30)), a lot of progress has been made in both theoretical and applied aspects of portfolio optimization.
These range from improvements in the optimization process, to the framing of additional constraints that might be desirable to rational investors (Cornuejols and
Tütüncü [2006](https://arxiv.org/html/2602.17098v1#bib.bib10); Li and Hoi [2014](https://arxiv.org/html/2602.17098v1#bib.bib24); Kalayci et al. [2017](https://arxiv.org/html/2602.17098v1#bib.bib21); Ghahtarani, Saif, and Ghasemi [2022](https://arxiv.org/html/2602.17098v1#bib.bib16)). Recently, the community has tapped the many advancements in Machine Learning (ML) to aid with feature selection, forecasting and estimation of asset means and covariances, as well as using gradient-based methods for optimization.

Concurrently, the past decade has witnessed the success of Reinforcement Learning (RL) in the fields of gaming, robotics, natural language processing, etc. (Silver et al. [2017](https://arxiv.org/html/2602.17098v1#bib.bib41); Nguyen and La [2019](https://arxiv.org/html/2602.17098v1#bib.bib36); Su et al. [2016](https://arxiv.org/html/2602.17098v1#bib.bib43)). The sequential decision making nature of Deep RL, along with its success in applied settings, has captured the attention of the finance research community.
In particular, some of the most popular areas of focus of the application of DRL in finance have been on automated stock trading (Yang et al. [2020](https://arxiv.org/html/2602.17098v1#bib.bib50); Théate and Ernst [2021](https://arxiv.org/html/2602.17098v1#bib.bib46); Zhang, Zohren, and Roberts [2020](https://arxiv.org/html/2602.17098v1#bib.bib52); Wu et al. [2020](https://arxiv.org/html/2602.17098v1#bib.bib49)), risk management through deep hedging (Buehler et al. [2019](https://arxiv.org/html/2602.17098v1#bib.bib4); Du et al. [2020](https://arxiv.org/html/2602.17098v1#bib.bib13); Cao et al. [2021](https://arxiv.org/html/2602.17098v1#bib.bib5); Benhamou et al. [2020b](https://arxiv.org/html/2602.17098v1#bib.bib2)) and portfolio optimization.
In the following section, we examine the landscape of DRL in portfolio optimization and trading problems. While these approaches exhibit improved performance over previous studies, they do have some shortcomings. For instance, some generate discrete asset trading signals which limit their use in broader portfolio management. Additionally, the majority of these approaches compare results against ML or buy-and-hold baselines, and do not consider classical portfolio optimization techniques, such as Mean-Variance Optimization.

In our work, we aim to compare a simple and robust DRL framework, that was designed around risk-adjusted returns, with one of the traditional finance methods for portfolio optimization, MVO. We train policy-gradient-based agents on a multi-asset trading environment that simulates the US Equities market (using market data replay), and create observation states derived from the observed asset prices. The agents optimize for risk-adjusted returns, similar to the traditional MVO methods. We compare the performance of the DRL strategy against MVO through a series of systematic backtests, and observe improved performance along many performance metrics, including risk-adjusted returns, max drawdown, and portfolio turnover.

## 2 Related Work

There is a lot of recent research interest into the application of Deep RL in trading and portfolio management problems.
For portfolio optimization, a lot of the research focuses on defining various policy network configurations and reports results that outperform various traditional baseline methods (Wang et al. [2019](https://arxiv.org/html/2602.17098v1#bib.bib47); Liang et al. [2018](https://arxiv.org/html/2602.17098v1#bib.bib26); Lu [2017](https://arxiv.org/html/2602.17098v1#bib.bib29); Jiang and Liang [2017](https://arxiv.org/html/2602.17098v1#bib.bib20); Wang et al. [2021](https://arxiv.org/html/2602.17098v1#bib.bib48); Deng et al. [2016](https://arxiv.org/html/2602.17098v1#bib.bib12); Cong et al. [2021](https://arxiv.org/html/2602.17098v1#bib.bib8)). Other work explores frameworks that inject information in the RL agent’s state by incorporating asset endogenous information such as technical indicators (Liu et al. [2020](https://arxiv.org/html/2602.17098v1#bib.bib28); Sun et al. [2021](https://arxiv.org/html/2602.17098v1#bib.bib44); Du and Tanaka-Ishii [2020](https://arxiv.org/html/2602.17098v1#bib.bib14)) as well as exogenous information such as information extracted from news data (Ye et al. [2020](https://arxiv.org/html/2602.17098v1#bib.bib51); Lima Paiva et al. [2021](https://arxiv.org/html/2602.17098v1#bib.bib27)).

The current benchmarks for DRL frameworks typically involve comparing results against other DRL or ML approaches, a buy-and-hold baseline, or market/index performance. However, these benchmarks may be overly simplistic or provide only a relative comparison. To truly gauge the effectiveness of a DRL agent, it would be more meaningful to benchmark it against methodologies used by financial professionals in practice, such as Mean Variance Optimization (MVO).

While there are some approaches that compare DRL performance with MVO (Li et al. [2019](https://arxiv.org/html/2602.17098v1#bib.bib25); Koratamaddi et al. [2021](https://arxiv.org/html/2602.17098v1#bib.bib22); i Alonso, Srivastava et al. [2020](https://arxiv.org/html/2602.17098v1#bib.bib19)), the comparison simply serves as another baseline, and the methodology is not clearly described because an in-depth comparison is not the primary focus of their study.
To our knowledge, there is only one study that goes into a robust in-depth comparison of MVO and DRL (Benhamou et al. [2020a](https://arxiv.org/html/2602.17098v1#bib.bib1)).
However, across all these studies, there is usually a discrepancy between the reward function used to train the RL agent, and the objective function used for MVO (e.g., daily returns maximization vs risk minimization). In order to make a fair comparison, it is crucial that both approaches optimize for the same goal. Additionally, some of these approaches provide exogenous information (e.g., signals from news data) to the DRL agent, which makes for a biased comparison with MVO. Moreover, none of these works provide implementation details for the MVO frameworks they used for their comparison. We aim to address these issues by conducting a robust comparison of Deep RL and Mean-Variance Optimization for the Portfolio Allocation problem.

## 3 Background

The goal of portfolio optimization is to continuously diversify and reallocate funds across assets with the objective of maximizing realized rewards while simultaneously restraining the risk.
In practice, portfolio management often aims to not only maximize risk-adjusted returns but also to perform as consistently as possible over a given time interval (e.g. on a quarterly or yearly basis).

Markowitz introduced the modern portfolio theory (MPT) (Markowitz [1952](https://arxiv.org/html/2602.17098v1#bib.bib30)), a framework that allows an investor to mathematically balance risk tolerance and return expectations to obtain efficiently diversified portfolios. This framework relies on the assumption that a rational investor will prefer a portfolio with less risk for a specified level of return and concludes that risk can be reduced by diversifying a portfolio.
In this section, we will introduce Mean Variance Optimization (MVO) – one of the main techniques of the MPT – which we later compare to the performance of our DRL framework. Additionally, we introduce RL preliminaries, describing the technique independent of portfolio optimization.

### 3.1 Mean-Variance Portfolio Optimization

Mean-Variance Optimization (MVO) is the mathematical process of allocating capital across a portfolio of assets (optimizing portfolio weights) to achieve a desired investment goal, usually: 1. Maximize returns for a given level of risk, 2. Achieve a desired rate of return while minimizing risk, or 3. Maximize returns generated *per* unit risk. Risk is usually measured by the volatility of a portfolio (or asset), which is the variance of its rate of return.
For a given set of assets, this process requires as inputs the rates of returns for each asset, along with their covariances. As the true asset returns are unknown, in practice, these are estimated or forecasted using various techniques that leverage historical data.

This task is then framed as an optimization problem, single or multi-objective, which can be solved in a variety of ways (Cornuejols and
Tütüncü [2006](https://arxiv.org/html/2602.17098v1#bib.bib10); Kalayci et al. [2017](https://arxiv.org/html/2602.17098v1#bib.bib21); Ghahtarani, Saif, and Ghasemi [2022](https://arxiv.org/html/2602.17098v1#bib.bib16)).

A typical procedure is to solve it as a convex optimization problem and generate an efficient frontier of portfolios such that no portfolio can be improved without sacrificing some measure of performance (e.g., returns, risk).
Let ww be the weight vector for a set of assets, μ\mu be the expected returns, the portfolio risk can be described as wT​Σ​ww^{T}\Sigma w, for covariance matrix Σ\Sigma. To achieve a desired rate of return μ∗\mu^{\*}, we can solve the portfolio optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minw\displaystyle\min\_{w} | wT​Σ​w\displaystyle w^{T}\Sigma w |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | wT​μ≥μ∗\displaystyle w^{T}\mu\geq\mu^{\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | wi≥0\displaystyle w\_{i}\geq 0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑iwi=1\displaystyle\sum\_{i}w\_{i}=1 |  |

Varying μ∗\mu^{\*} gives us the aforementioned efficient frontier.

Another common objective is the Sharpe Ratio (Sharpe [1998](https://arxiv.org/html/2602.17098v1#bib.bib40); Chen, He, and Zhang [2011](https://arxiv.org/html/2602.17098v1#bib.bib7)), which measures the return per unit risk. Formally, for portfolio pp, the Sharpe Ratio is defined as:

|  |  |  |
| --- | --- | --- |
|  | Sharpe Ratiop=E​[Rp−Rf]σp\text{Sharpe Ratio}\_{p}=\frac{E[R\_{p}-R\_{f}]}{\sigma\_{p}} |  |

where RpR\_{p} are the returns of the portfolio, σp\sigma\_{p} is the standard deviation of these returns, and RfR\_{f} is a constant risk-free rate (e.g., US Treasuries, approximated by 0.0% in recent history). Although tricky to solve in its direct form –

|  |  |  |
| --- | --- | --- |
|  | maxw⁡μT​w−Rf(wT​Σ​w)1/2\max\_{w}\frac{\mu^{T}w-R\_{f}}{\left(w^{T}\Sigma w\right)^{1/2}} |  |

– it can be framed as a convex optimization problem through the use of a variable substitution (Cornuejols and
Tütüncü [2006](https://arxiv.org/html/2602.17098v1#bib.bib10)). We choose the Sharpe Ratio as our desired objective function for this study as we can optimize for risk-adjusted returns without having to specify explicit figures for minimum expected returns or maximum risk tolerance.

### 3.2 Reinforcement Learning

Reinforcement Learning (RL) is a sub-field of machine learning that refers to a class of techniques that involve learning by optimizing long-term reward sequences obtained by interactions with an environment (Sutton and Barto [2018](https://arxiv.org/html/2602.17098v1#bib.bib45)).
An environment is typically formalized by means of a Markov Decision Process (MDP). An MDP consists of a 5-tuple (S,A,Pa,Ra,γ){(S,A,P\_{a},R\_{a},\gamma)}, where:

* •

  SS is a set of states
* •

  AA is a set of actions
* •

  Pa​(s,s′)=Pr⁡(st+1=s′∣st=s,at=a)P\_{a}(s,s^{\prime})=\Pr(s\_{t+1}=s^{\prime}\mid s\_{t}=s,a\_{t}=a) is the probability that action aa in state ss at time tt will lead to state s′s^{\prime} at time t+1t+1
* •

  Ra​(s,s′)R\_{a}(s,s^{\prime}) is the immediate reward received after transitioning from state ss to state s′s^{\prime}, due to action aa
* •

  γ\gamma is a discount factor between [0,1][0,1] that represents the difference in importance between present and future rewards

A solution to an MDP is a policy π\pi that specifies the action π​(s)\pi(s) that the decision maker will choose when in state ss. The objective is to choose a policy π\pi that will maximize the expected discounted sum of rewards over a potentially infinite horizon:

|  |  |  |
| --- | --- | --- |
|  | E​[∑t=0∞γt​Rat​(st,st+1)]{E\left[\sum\_{t=0}^{\infty}{\gamma^{t}R\_{a\_{t}}(s\_{t},s\_{t+1})}\right]} |  |

The field of Deep Reinforcement Learning (DRL) leverages the advancements in Deep Learning by using Neural Networks as function approximators to estimate state-action value functions, or to learn policy mappings π\pi. These techniques have seen tremendous success in game-playing, robotics, continuous control, and finance (Mnih et al. [2013](https://arxiv.org/html/2602.17098v1#bib.bib33); Berner et al. [2019](https://arxiv.org/html/2602.17098v1#bib.bib3); Nguyen and La [2019](https://arxiv.org/html/2602.17098v1#bib.bib36); Hambly, Xu, and Yang [2021](https://arxiv.org/html/2602.17098v1#bib.bib17); Charpentier, Elie, and
Remlinger [2021](https://arxiv.org/html/2602.17098v1#bib.bib6)).

#### RL for Portfolio Allocation

Given its success in stochastic control problems, RL extends nicely to the problem of portfolio optimization. Therefore, it is not surprising that the use of DRL to perform tasks such as trading and portfolio optimization has received a lot of attention lately.
Recent methods focus on learning deep features and state representations, for example, through the use of embedding features derived from deep neural networks such as autoencoders and LSTM models. These embeddings capture price related features which can range from technical indicators (Wang et al. [2019](https://arxiv.org/html/2602.17098v1#bib.bib47); Soleymani and Paquet [2020](https://arxiv.org/html/2602.17098v1#bib.bib42); Wang et al. [2021](https://arxiv.org/html/2602.17098v1#bib.bib48)), to information extracted from news in order to account for price fluctuations (Ye et al. [2020](https://arxiv.org/html/2602.17098v1#bib.bib51)). Other proposed features use attention networks or graph structures (Wang et al. [2021](https://arxiv.org/html/2602.17098v1#bib.bib48), [2019](https://arxiv.org/html/2602.17098v1#bib.bib47)) to perform cross-asset interrelationship feature extraction.

## 4 Problem Setup

We frame the portfolio optimization problem in the RL setting. As described in Section [3](https://arxiv.org/html/2602.17098v1#S3 "3 Background ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization"), RL entails learning in a framework with interactions between an agent and an environment. For the portfolio optimization setting, we create an environment that simulates the US Equities market (using market data replay), and create observation states derived from the observed asset prices. The agent’s actions output a set of portfolio weights, which are used to rebalance the portfolio at each timestep.

### 4.1 Actions

For portfolio allocation over NN assets, an agent selects portfolio weights 𝒘=[w1,…,wN]\bm{w}=[{w\_{1},\dots,w\_{N}}] such that ∑i=1Nwi=1\sum\_{i=1}^{N}w\_{i}=1, where 0≤wi≤10\leq w\_{i}\leq 1.
An asset weight of 0 indicates zero holdings of a particular asset in a portfolio, whereas a weight of 11 means the entire portfolio is concentrated in said asset. In extensions of this framework, wi<0w\_{i}<0 would allow for shorting an asset, whereas wi>1w\_{i}>1 indicates a leveraged position. However, for our case, we restrict actions to non-leveraged long-only positions. These constraints can be enforced by applying the softmax function to an agent’s continuous actions.

### 4.2 States

An asset’s price at time tt is denoted by PtP\_{t}. The one-period simple return is defined as Rt=Pt−Pt−1Pt−1R\_{t}=\frac{P\_{t}-P\_{t-1}}{P\_{t-1}}. Consequently, the one-period gross return can be defined as PtPt−1=Rt+1\frac{P\_{t}}{P\_{t-1}}=R\_{t}+1. Further, we can define the one-period log return as rt=log⁡(PtPt−1)=log⁡(Rt+1)r\_{t}=\log\!\left(\frac{P\_{t}}{P\_{t-1}}\right)=\log(R\_{t}+1). For our setting, we choose the time period to be daily, and therefore calculate daily log returns using end-of-day close prices.
An asset’s log returns over a lookback period TT can then be captured as 𝒓𝒕=[rt−1,rt−2,…,rt−T+1]\bm{r\_{t}}=[{r\_{t-1},r\_{t-2},\dots,r\_{t-T+1}}]. In our case, the lookback period is T=60T=60 days.

For a selection of n+1n+1 assets – nn securities and cash (denoted by cc) – we form the agent’s observation state at time tt, 𝑺𝒕\bm{S\_{t}} as a [(n+1)×T][(n+1)\times T] matrix:

|  |  |  |
| --- | --- | --- |
|  | St=[w1r1,t−1…r1,t−T+1w2r2,t−1…r2,t−T+1⋮⋱⋮wnrn,t−1…rn,t−T+1wcvol20vol20vol60VIXt​…]{S\_{t}}=\begin{bmatrix}w\_{1}&r\_{1,t-1}&\dots&r\_{1,t-T+1}\\ w\_{2}&r\_{2,t-1}&\dots&r\_{2,t-T+1}\\ \vdots&&\ddots&\vdots\\ w\_{n}&r\_{n,t-1}&\dots&r\_{n,t-T+1}\\ w\_{c}&\text{vol}\_{20}&\frac{\text{vol}\_{20}}{\text{vol}\_{60}}&\text{VIX}\_{t}\dots\end{bmatrix} |  |

The first column is the agent’s portfolio allocation vector 𝒘\bm{w} as it enters timestep tt. This might differ slightly from the portfolio weights it chooses at the timestep before, as we convert the continuous weights into an actual allocation (whole shares only), and rebalance the allocation such that it sums to 11.

For each non-cash asset, we include the log returns over TT. These are represented by the vector [rn,t−1,…,rn,t−T+1][{r\_{n,t-1},\dots,r\_{n,t-T+1}}] for asset nn in the state matrix above.

Additionally, in the last row, we include three market volatility indicators at time tt: vol20\text{vol}\_{20}, vol20vol60\frac{\text{vol}\_{20}}{\text{vol}\_{60}}, VIX, which we describe in detail in Section [5](https://arxiv.org/html/2602.17098v1#S5 "5 Experiments ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization").

### 4.3 Reward

Rather than maximizing returns, most modern portfolio managers attempt to maximize risk-adjusted returns. Since we wish to utilize DRL for portfolio allocation, we want a reward function that helps optimize for risk-adjusted returns. The Sharpe ratio is the most widely-used measure for this, however, it is inappropriate for online learning settings as it is defined over a period of time TT.
To combat this, we use the Differential Sharpe Ratio DtD\_{t} (Moody et al. [1998](https://arxiv.org/html/2602.17098v1#bib.bib35)) which represents the risk-adjusted returns at each timestep tt and has been found to yield more consistent returns than maximizing profit (Moody and Saffell [2001](https://arxiv.org/html/2602.17098v1#bib.bib34); Dempster and Leemans [2006](https://arxiv.org/html/2602.17098v1#bib.bib11)). Therefore, an agent that aims to maximize its future Differential Sharpe rewards learns how to optimize for risk-adjusted returns.

We can define the Sharpe Ratio over a period of tt returns RtR\_{t}, in terms of estimates of the first and second moments of the returns’ distributions:

|  |  |  |
| --- | --- | --- |
|  | St=AtKt​(Bt−At2)1/2S\_{t}=\frac{A\_{t}}{K\_{t}(B\_{t}-A\_{t}^{2})^{1/2}} |  |

with

|  |  |  |
| --- | --- | --- |
|  | At=1t​∑i=1tRi​and​Bt=1t​∑i=1tRi2,Kt=(tt−1)1/2A\_{t}=\frac{1}{t}\sum\_{i=1}^{t}R\_{i}~~\text{and}~B\_{t}=\frac{1}{t}\sum\_{i=1}^{t}R\_{i}^{2}~,~K\_{t}=\left(\frac{t}{t-1}\right)^{1/2} |  |

where KtK\_{t} is a normalizing factor.

AA and BB can be recursively estimated as exponential moving averages of the returns and standard deviation of returns on time scale η−1{\eta}^{-1}. We can obtain a *differential* Sharpe ratio DtD\_{t} by expanding StS\_{t} to first order in η\eta:

|  |  |  |
| --- | --- | --- |
|  | St≈St−1+η​Dt|η=0+O​(η2)S\_{t}\approx S\_{t-1}+\eta D\_{t}|\_{\eta=0}+O(\eta^{2}) |  |

Where Differential Sharpe Ratio DtD\_{t}:

|  |  |  |
| --- | --- | --- |
|  | Dt≡∂St∂η=Bt−1​Δ​At−12​At−1​Δ​Bt(Bt−1−At−12)3/2D\_{t}\equiv\frac{\partial S\_{t}}{\partial\eta}=\frac{B\_{t-1}\Delta A\_{t}-\frac{1}{2}A\_{t-1}\Delta B\_{t}}{(B\_{t-1}-A\_{t-1}^{2})^{3/2}} |  |

with

|  |  |  |
| --- | --- | --- |
|  | At=At−1+η​Δ​AtA\_{t}=A\_{t-1}+\eta\Delta A\_{t} |  |

|  |  |  |
| --- | --- | --- |
|  | Bt=Bt−1+η​Δ​BtB\_{t}=B\_{t-1}+\eta\Delta B\_{t} |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​At=Rt−At−1\Delta A\_{t}=R\_{t}-A\_{t-1} |  |

|  |  |  |
| --- | --- | --- |
|  | Δ​Bt=Rt2−Bt−1\Delta B\_{t}=R\_{t}^{2}-B\_{t-1} |  |

initialized with A0=B0=0A\_{0}=B\_{0}=0. We pick η≈1252\eta\approx\frac{1}{252} (a year has approximately 252 trading days).

### 4.4 Learning Algorithm

RL algorithms can be mainly divided into two categories, model-based and model-free, depending on whether the agent has access to or has to learn a model of the environment.
Model-free algorithms seek to learn the outcomes of their actions through collecting experience via algorithms such as Policy Gradient, Q-Learning, etc. Such an algorithm will try an action multiple times and adjust its policy (its strategy) based on the outcomes of its action in order to optimize rewards.

#### Policy Optimization

Policy optimization methods are centered around the policy πθ​(a|s)\pi\_{\theta}(a|s) which is the function that maps the agent’s state ss to the distribution of its next action aa. These methods optimize the parameters θ\theta either by gradient ascent on the performance objective J​(πθ)J(\pi\_{\theta}) or by maximizing local approximations of J​(πθ)J(\pi\_{\theta}). This optimization is almost always performed on-policy since the experiences are collected using the latest learned policy, and then using that experience to improve the policy.
Some examples of popular policy optimization methods are A2C/A3C (Mnih et al. [2016](https://arxiv.org/html/2602.17098v1#bib.bib32)) and PPO (Schulman et al. [2017](https://arxiv.org/html/2602.17098v1#bib.bib39)). For our experiments we use PPO.

### 4.5 RL Environment Specifics

The environment serves as a wrapper for the market, sliding over historical data in an approach called market replay. It also serves as a broker and exchange; at every timestep, it processes the agents’ actions and rebalances the portfolio using the latest prices and the given allocation. As the day shifts and new prices are received, it communicates these to the agent as observations, along with the Differential Sharpe reward. For the purposes of this study, we assume that there are no transaction costs in the environment, and we allow for immediate rebalancing of the portfolio.

At the beginning of each timestep tt, the environment calculates the current portfolio value:

|  |  |  |
| --- | --- | --- |
|  | port\_valt=∑iPi,t⋅sharesi,t−1+ct−1\text{port\\_val}\_{t}=\sum\_{i}P\_{i,t}\cdot\text{shares}\_{i,t-1}+c\_{t-1} |  |

In the above expression, PiP\_{i} is the price of index ii at day tt, sharesi,t−1\text{shares}\_{i,t-1} are the index shares at t−1t-1, and ct−1c\_{t-1} is the amount of cash at t−1t-1.

In order to calculate sharesi,t\text{shares}\_{i,t} and ctc\_{t}, the environment allocates port\_valt\text{port\\_val}\_{t} to the indices and cash according to the new weights wiw\_{i}. Next, it rebalances the portfolio weights wiw\_{i} to wi​\_​rebw\_{i\\_\text{reb}} by multiplying wiw\_{i} with the current portfolio value, rounding down the number of shares and converting the remaining shares into cash.

After rebalancing, the environment creates the next state St+1S\_{t+1} and proceeds to the next timestep t+1t+1.
It calculates the new portfolio value based on Pt+1P\_{t+1} and computes the reward Rt=DtR\_{t}=D\_{t} which it returns to the agent.

## 5 Experiments

### 5.1 Data & Features

For our experiments, we use daily adjusted close price data of the S&P 500 sector indices as shown in Figure [1](https://arxiv.org/html/2602.17098v1#S5.F1 "Figure 1 ‣ 5.1 Data & Features ‣ 5 Experiments ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization"), the VIX index and the S&P 500 index between 20062006 and 20212021 (inclusive), extracted from Yahoo Finance. The price data is used to compute log returns, as described in Section [4.2](https://arxiv.org/html/2602.17098v1#S4.SS2 "4.2 States ‣ 4 Problem Setup ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization").

![Refer to caption](figures/sectors.png)


Figure 1: S&P 500 and its 11 sector indices between 2006 and 2021.

To capture market regime, we compute three volatility metrics from the S&P 500 index. The first one, vol20\text{vol}\_{20}, is the 2020-day rolling window standard deviation of the daily S&P 500 index returns, the second, vol60\text{vol}\_{60}, is the 6060-day rolling window standard deviation of the daily S&P 500 index returns and the third is the ratio of these two vol20vol60\frac{\text{vol}\_{20}}{\text{vol}\_{60}}. This ratio indicates the short-term versus the long-term volatility trend. If vol20vol60>1\frac{\text{vol}\_{20}}{\text{vol}\_{60}}>1, that indicates that the past 2020-day daily returns of the S&P 500 have been more volatile than the past 6060-day daily returns, which might indicate a movement from lower volatility to a higher volatility regime (and vice versa). We use the first and third metrics in the observation matrix, along with the value of the VIX index. These values are standardized by subtracting the mean and dividing by the standard deviation, where the mean and standard deviation are estimated using an expanding lookback window to prevent information leakage.

### 5.2 Deep RL Approach

#### Training Process

Although financial data is notoriously scarce (at least on the daily scale), we want to test the DRL framework across multiple years (backtests). Additionally, financial time series exhibit non-stationarity (Cont [2001](https://arxiv.org/html/2602.17098v1#bib.bib9)); this can be tackled by retraining or fine-tuning models by utilizing the most recently available data. In light of these stylized facts, we devise our experiment framework as follows:

The data is split into 1010 sliding window groups (shifted by 11-year). Each group contains 77 years worth of data, the first 55 years are used for training, the next 11 year is a burn year used for training validation, and the last year is kept out-of-sample for backtesting.

During the first round of training, we initialize 55 agents (different seeds) with the hyperparameters described in the following section. All five agents start training on data from [2006−2011)[2006-2011) and their performance is periodically evaluated using the validation period 20112011.
At the end of the first round of training, we save the best performing agent (based on highest mean episode validation reward). The final year (20122012) is kept held-out for backtesting.

This agent is used as a seed policy for the next group of 5 agents in the following training window [2007−2012)[2007-2012), validation year 20122012 and testing year 20132013, where this experiment is repeated. This process continues till we reach the final validation period of 20202020, generating a total of 5050 agents (1010 periods x 55 agents), and 1010 corresponding backtests (described in a following section).

#### PPO Implementation & Hyperparameters

We use the StableBaselines3 (Raffin et al. [2021](https://arxiv.org/html/2602.17098v1#bib.bib37)) implementation of PPO, and report the hyperparameters used in Table [1](https://arxiv.org/html/2602.17098v1#S5.T1 "Table 1 ‣ PPO Implementation & Hyperparameters ‣ 5.2 Deep RL Approach ‣ 5 Experiments ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization"). These were picked based on empirical studies (Henderson et al. [2018](https://arxiv.org/html/2602.17098v1#bib.bib18); Engstrom et al. [2019](https://arxiv.org/html/2602.17098v1#bib.bib15); Rao et al. [2020](https://arxiv.org/html/2602.17098v1#bib.bib38)), as well as a coarse grid search over held-out validation data.

|  |  |
| --- | --- |
| training\_timesteps | 7.5M |
| n\_envs | 10 |
| n\_steps | 756 |
| batch\_size | 1260 |
| n\_epochs | 16 |
| gamma | 0.9 |
| gae\_lambda | 0.9 |
| clip\_range | 0.25 |
| learning\_rate | 3e-4 annealed to 1e-5 |

Table 1: Hyperparameters used for PPO.

Additionally, we make use of the Vectorized SubProcVecEnv environment wrappers provided by StableBaselines3 to collect experience rollouts through multiprocessing across independent instances of our environment. Therefore, instead of training the DRL agent on one environment per step, we train on n​\_​e​n​v​s=10n\\_envs=10 environments per step in order to gain more diverse experience and speed up training.

Each round of training lasted a total 7.5M timesteps so as to have approximately 600 episodes per round per environment:
(252 trading days per yr×5 yrs per round)×(10 environments)×(600 episodes)≈7.5M timesteps(\text{252 trading days per yr}\times\text{5 yrs per round})\times(\text{10 environments})\times(\text{600 episodes})\approx\text{7.5M timesteps}.
The rollout buffer size was set to n​\_​s​t​e​p​s=252×3×n​\_​e​n​v​sn\\_steps=252\times 3\times n\\_envs so as to collect sufficient experiences across environments. We set up the learning rate as a decaying function of the current progress remaining, starting from 3​e−43e-4, annealed to a final value of 1​e−51e-5. We used a b​a​t​c​h​\_​s​i​z​ebatch\\_size of 1260=(252×5)1260=(252\times 5), set the number of epochs when optimizing the surrogate loss to n​\_​e​p​o​c​h​s=16n\\_epochs=16, picked the discount factor γ=0.9\gamma=0.9, set the bias-variance trade-off factor for Generalized Advantage Estimator g​a​e​\_​l​a​m​b​d​a=0.9gae\\_lambda=0.9 and c​l​i​p​\_​r​a​n​g​e=0.25clip\\_range=0.25.
Additionally, we use a [64,64][64,64] fully-connected architecture with t​a​n​htanh activations, and initialize the policy with a log standard deviation l​o​g​\_​s​t​d​\_​i​n​i​t=−1log\\_std\\_init=-1.

### 5.3 Mean-Variance Optimization Approach

As we wish to compare the model-free DRL approach with MVO, we equalize the training and operational conditions. For training, the MVO approach uses a 6060-day lookback period (same as DRL) to estimate the means and covariances of assets. Asset means are simply the sample means over the lookback period. However, we do not directly use the sample covariance, as this has been shown to be subject to estimation error that is incompatible with MVO. To tackle this, we make use of the Ledoit-Wolf Shrinkage operator (Ledoit and Wolf [2004](https://arxiv.org/html/2602.17098v1#bib.bib23)). Additionally, we enforce non-singular and positive-semi-definite conditions on the covariance matrices, setting negative eigenvalues to 0, and then rebuilding the non-compliant matrices.

Given the estimated means and covariances for a lookback period, we then optimize for the Sharpe Maximization problem and obtain the weights at every timestep. We use the implementation in PyPortfolioOpt (Martin [2021](https://arxiv.org/html/2602.17098v1#bib.bib31)) to aid us with this process.

![Refer to caption](figures/backtest.png)


Figure 2: Backtest Results: MVO vs DRL Portfolio Allocation.

![Refer to caption](figures/DRL_returns.jpg)


Figure 3: a) DRL Monthly Returns b) DRL Annual Returns c) DRL Monthly Distribution of Returns.

![Refer to caption](figures/MVO_returns.jpg)


Figure 4: a) MVO Monthly Returns b) MVO Annual Returns c) MVO Monthly Distribution of Returns.

### 5.4 Evaluation & Backtesting

We evaluate the performance of both techniques through 1010 independent backtests [2012−2021][2012-2021]. Both strategies start each backtest period with an all cash portfolio allocation of $​100,000\mathdollar 100,000. Then, the strategies trade daily using the portfolio weights obtained by each method, enforcing weight constraints ∑iwi=1,0≤wi≤1\sum\_{i}w\_{i}=1,0\leq w\_{i}\leq 1, and ensuring only whole number of shares are purchased. By doing so, we can obtain daily portfolio values (and returns), which we subsequently use to compute the statistics we will discuss in the Results section. These are computed with the aid of the Python library Pyfolio.

DRL Agent: We evaluate the trained PPO agents in deterministic mode. For each backtest, the agent used has a gap burn year between the last day seen in training and the backtest period. For example, a DRL backtest carried out in 20122012 would use an agent trained in [2006−2011)[2006-2011), with 20112011 being the burn year.

MVO: As the MVO approach does not require any training, it simply uses the past 6060-day lookback period before any given day to calculate portfolio weights. For example, an MVO backtest starting January 20122012 will use data starting October 20112011 (this 6060-day window shifts with each day).

## 6 Results

Figure [2](https://arxiv.org/html/2602.17098v1#S5.F2 "Figure 2 ‣ 5.3 Mean-Variance Optimization Approach ‣ 5 Experiments ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization") illustrates the performance metrics obtained by applying the aforementioned backtest process on all testing periods [2012-2021]. The DRL agent outperforms the MVO portfolio by exhibiting higher Sharpe and lower yearly maximum drawdowns in virtually every year throughout the backtest period. It also outperforms the MVO portfolio in terms of having marginally lower maximum drawdown.

| Metric | DRL | MVO |
| --- | --- | --- |
| Annual return | 0.1211 | 0.0653 |
| Cumulative returns | 0.1195 | 0.0650 |
| Annual volatility | 0.1249 | 0.1460 |
| Sharpe ratio | 1.1662 | 0.6776 |
| Calmar ratio | 2.3133 | 1.1608 |
| Stability | 0.6234 | 0.4841 |
| Max drawdown | -0.3296 | -0.3303 |
| Omega ratio | 1.2360 | 1.1315 |
| Sortino ratio | 1.7208 | 1.0060 |
| Skew | -0.4063 | -0.3328 |
| Kurtosis | 2.7054 | 2.6801 |
| Tail ratio | 1.0423 | 0.9448 |
| Daily value at risk | -0.0152 | -0.0181 |

Table 2: Statistics for the DRL and MVO approaches. All metrics are averaged across 1010 backtests (backtesting period: [2012−2021]){[}2012-2021{]}), except Max Drawdown which is reported as the maximum seen in any period.

To compare overall performance on the entire backtest period between the two methods, we compute the average performance across all 10 backtest periods. For DRL, we average the performance across the 5 agents (each trained on a different seed) for each year and then average performance across all backtest periods. Similarly, for MVO, we average its performance across all 10 years. By looking at Table [2](https://arxiv.org/html/2602.17098v1#S6.T2 "Table 2 ‣ 6 Results ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization") we observe that DRL annual returns and Sharpe ratio are ≈1.85×{\approx}1.85\times higher than those of the MVO portfolio. The DRL strategy achieves a Sharpe ratio of 1.17 over the full backtest period, compared to 0.68 for MVO.

Figure [3](https://arxiv.org/html/2602.17098v1#S5.F3 "Figure 3 ‣ 5.3 Mean-Variance Optimization Approach ‣ 5 Experiments ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization")a) and Figure [4](https://arxiv.org/html/2602.17098v1#S5.F4 "Figure 4 ‣ 5.3 Mean-Variance Optimization Approach ‣ 5 Experiments ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization")a) plot the monthly returns over all backtest periods for the two methods. It is evident that DRL is experiencing more steady returns month-to-month than MVO. On the other hand, MVO swings between periods of high returns to periods of low returns a lot more frequently without a steady positive return trajectory. Similarly, in Figure [3](https://arxiv.org/html/2602.17098v1#S5.F3 "Figure 3 ‣ 5.3 Mean-Variance Optimization Approach ‣ 5 Experiments ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization")b) and Figure [4](https://arxiv.org/html/2602.17098v1#S5.F4 "Figure 4 ‣ 5.3 Mean-Variance Optimization Approach ‣ 5 Experiments ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization")b), we plot the annual returns for the two methods. The vertical dashed line indicates the average annual return across the 10 backtests. For DRL we observe positive returns for almost all backtest years which is a lot more consistent than the behavior of MVO’s annual returns. Figure [3](https://arxiv.org/html/2602.17098v1#S5.F3 "Figure 3 ‣ 5.3 Mean-Variance Optimization Approach ‣ 5 Experiments ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization")c) and Figure [4](https://arxiv.org/html/2602.17098v1#S5.F4 "Figure 4 ‣ 5.3 Mean-Variance Optimization Approach ‣ 5 Experiments ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization")c) plot the distribution of monthly returns averaged across all months. The DRL monthly returns distribution has a lower standard deviation and spread than MVO and a positive mean.

Further, we compute the daily portfolio change for each strategy by measuring the change in its portfolio weights. Δ​pw\Delta{p\_{w}} is the absolute value of the element-wise difference between two allocations (ignoring the cash component). As buying and selling are treated as individual transactions, Δ​pw∈[0.0,2.0]\Delta{p\_{w}}\in[0.0,2.0]. For example, take a case where the portfolio at time t−1t-1 is concentrated in non-cash asset A, and at time tt is entirely concentrated in non-cash asset B. This requires selling all holdings of A, and acquiring the equivalent shares in B, leading to Δ​pw=2.0\Delta{p\_{w}}=2.0.

Using metric Δ​pw\Delta{p\_{w}}, we observe that the Reinforcement Learning strategy has less frequent changes to its portfolio. In practice, this would result in lower average transaction costs. In particular, the average change in portfolio composition is nearly double for Mean-Variance portfolio compared to the DRL strategy during market downturn in March 2020, as shown in Figure [2](https://arxiv.org/html/2602.17098v1#S5.F2 "Figure 2 ‣ 5.3 Mean-Variance Optimization Approach ‣ 5 Experiments ‣ Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization"), when trading conditions were particularly challenging (i.e. significantly lower market liquidity and elevated bid/ask spreads). Finally, the DRL strategy’s performance is derived from the average of five individual agents initialized with different seeds, providing additional regularization which is likely to result in a more stable out-of-sample strategy compared to the MVO strategy.

## 7 Conclusion

We highlight our key contributions as follows:

* •

  We have designed a simple environment that serves as a wrapper for the market, sliding over historical data using market replay. The environment can allocate multiple assets and can be easily modified to reflect transaction costs.
* •

  We compare our framework’s performance during ten backtest experiments over different periods for the US Equities Market using S&P 500 Sector indices. Our experiments demonstrate the improved performance of the deep reinforcement learning framework over Mean-Variance portfolio optimization.
* •

  The profitability of the framework surpasses MVO in terms of Annual Returns, Sharpe ratio and Maximum Drawdown. Additionally, we observe that DRL strategy leads to more consistent returns and more stable portfolios with decreased turnover. This has implications for live-deployment, where transaction costs and slippage affect P&L.

### 7.1 Future Work

In our future work, we would like to model transaction costs and slippage either by explicitly calculating them during asset reallocation or as a penalty term to our reward.
Moreover, we would like to explore adding a drawdown minimization component to our reward that will potentially help the agent learn a more consistent trading strategy.

Another area of exploration is training a regime switching model which will balance its funds amongst two agents depending on market volatility (low vs high). One of them will be a low-volatility trained agent and the other a high volatility trained agent. We would like to compare performance between our current implicit regime parametrization and an explicit one.

## Acknowledgements

This paper was prepared for information purposes by the Artificial Intelligence Research group of J. P. Morgan Chase & Co. and its affiliates (“J. P. Morgan”), and is not a product of the Research Department of J. P. Morgan. J. P. Morgan makes no representation and warranty whatsoever and disclaims all liability, for the completeness, accuracy or reliability of the information contained herein. This document is not intended as investment research or investment advice, or a recommendation, offer or solicitation for the purchase or sale of any security, financial instrument, financial product or service, or to be used in any way for evaluating the merits of participating in any transaction, and shall not constitute a solicitation under any jurisdiction or to any person, if such solicitation under such jurisdiction or to such person would be unlawful.

## References

* Benhamou et al. (2020a)

  Benhamou, E.; Saltiel, D.; Ungari, S.; and Mukhopadhyay, A. 2020a.
  Bridging the gap between Markowitz planning and deep reinforcement
  learning.
  *arXiv preprint arXiv:2010.09108*.
* Benhamou et al. (2020b)

  Benhamou, E.; Saltiel, D.; Ungari, S.; and Mukhopadhyay, A. 2020b.
  Time your hedge with deep reinforcement learning.
  *arXiv preprint arXiv:2009.14136*.
* Berner et al. (2019)

  Berner, C.; Brockman, G.; Chan, B.; Cheung, V.; Debiak, P.; Dennison, C.;
  Farhi, D.; Fischer, Q.; Hashme, S.; Hesse, C.; et al. 2019.
  Dota 2 with large scale deep reinforcement learning.
  *arXiv preprint arXiv:1912.06680*.
* Buehler et al. (2019)

  Buehler, H.; Gonon, L.; Teichmann, J.; and Wood, B. 2019.
  Deep hedging.
  *Quantitative Finance*, 19(8): 1271–1291.
* Cao et al. (2021)

  Cao, J.; Chen, J.; Hull, J.; and Poulos, Z. 2021.
  Deep hedging of derivatives using reinforcement learning.
  *The Journal of Financial Data Science*, 3(1): 10–27.
* Charpentier, Elie, and
  Remlinger (2021)

  Charpentier, A.; Elie, R.; and Remlinger, C. 2021.
  Reinforcement learning in economics and finance.
  *Computational Economics*, 1–38.
* Chen, He, and Zhang (2011)

  Chen, L.; He, S.; and Zhang, S. 2011.
  When all risk-adjusted performance measures are the same: In praise
  of the Sharpe ratio.
  *Quantitative Finance*, 11(10): 1439–1447.
* Cong et al. (2021)

  Cong, L. W.; Tang, K.; Wang, J.; and Zhang, Y. 2021.
  AlphaPortfolio: Direct construction through deep reinforcement
  learning and interpretable AI.
  *Available at SSRN*, 3554486.
* Cont (2001)

  Cont, R. 2001.
  Empirical properties of asset returns: stylized facts and statistical
  issues.
  *Quantitative finance*, 1(2): 223.
* Cornuejols and
  Tütüncü (2006)

  Cornuejols, G.; and Tütüncü, R. 2006.
  *Optimization methods in finance*, volume 5.
  Cambridge University Press.
* Dempster and Leemans (2006)

  Dempster, M. A.; and Leemans, V. 2006.
  An automated FX trading system using adaptive reinforcement learning.
  *Expert Systems with Applications*, 30(3): 543–552.
* Deng et al. (2016)

  Deng, Y.; Bao, F.; Kong, Y.; Ren, Z.; and Dai, Q. 2016.
  Deep direct reinforcement learning for financial signal
  representation and trading.
  *IEEE transactions on neural networks and learning systems*,
  28(3): 653–664.
* Du et al. (2020)

  Du, J.; Jin, M.; Kolm, P. N.; Ritter, G.; Wang, Y.; and Zhang, B. 2020.
  Deep reinforcement learning for option replication and hedging.
  *The Journal of Financial Data Science*, 2(4): 44–57.
* Du and Tanaka-Ishii (2020)

  Du, X.; and Tanaka-Ishii, K. 2020.
  Stock embeddings acquired from news articles and price history, and
  an application to portfolio optimization.
  In *Proceedings of the 58th annual meeting of the association
  for computational linguistics*, 3353–3363.
* Engstrom et al. (2019)

  Engstrom, L.; Ilyas, A.; Santurkar, S.; Tsipras, D.; Janoos, F.; Rudolph, L.;
  and Madry, A. 2019.
  Implementation matters in deep rl: A case study on ppo and trpo.
  In *International conference on learning representations*.
* Ghahtarani, Saif, and Ghasemi (2022)

  Ghahtarani, A.; Saif, A.; and Ghasemi, A. 2022.
  Robust portfolio selection problems: a comprehensive review.
  *Operational Research*, 1–62.
* Hambly, Xu, and Yang (2021)

  Hambly, B.; Xu, R.; and Yang, H. 2021.
  Recent advances in reinforcement learning in finance.
  *arXiv preprint arXiv:2112.04553*.
* Henderson et al. (2018)

  Henderson, P.; Islam, R.; Bachman, P.; Pineau, J.; Precup, D.; and Meger, D.
  2018.
  Deep reinforcement learning that matters.
  In *Proceedings of the AAAI conference on artificial
  intelligence*, volume 32.
* i Alonso, Srivastava et al. (2020)

  i Alonso, M. N.; Srivastava, S.; et al. 2020.
  Deep reinforcement learning for asset allocation in us equities.
  Technical report.
* Jiang and Liang (2017)

  Jiang, Z.; and Liang, J. 2017.
  Cryptocurrency portfolio management with deep reinforcement learning.
  In *2017 Intelligent Systems Conference (IntelliSys)*, 905–913.
  IEEE.
* Kalayci et al. (2017)

  Kalayci, C.; Ertenlice, O.; Akyer, H.; and Aygören, H. 2017.
  A review on the current applications of genetic algorithms in
  mean-variance portfolio optimization.
  *Pamukkale University Journal of Engineering Sciences*, 23:
  470–476.
* Koratamaddi et al. (2021)

  Koratamaddi, P.; Wadhwani, K.; Gupta, M.; and Sanjeevi, S. G. 2021.
  Market sentiment-aware deep reinforcement learning approach for stock
  portfolio allocation.
  *Engineering Science and Technology, an International Journal*,
  24(4): 848–859.
* Ledoit and Wolf (2004)

  Ledoit, O.; and Wolf, M. 2004.
  Honey, I shrunk the sample covariance matrix.
  *The Journal of Portfolio Management*, 30(4): 110–119.
* Li and Hoi (2014)

  Li, B.; and Hoi, S. C. 2014.
  Online portfolio selection: A survey.
  *ACM Computing Surveys (CSUR)*, 46(3): 1–36.
* Li et al. (2019)

  Li, X.; Li, Y.; Zhan, Y.; and Liu, X.-Y. 2019.
  Optimistic bull or pessimistic bear: Adaptive deep reinforcement
  learning for stock portfolio allocation.
  *arXiv preprint arXiv:1907.01503*.
* Liang et al. (2018)

  Liang, Z.; Chen, H.; Zhu, J.; Jiang, K.; and Li, Y. 2018.
  Adversarial deep reinforcement learning in portfolio management.
  *arXiv preprint arXiv:1808.09940*.
* Lima Paiva et al. (2021)

  Lima Paiva, F. C.; Felizardo, L. K.; Bianchi, R. A. d. C.; and Costa, A. H. R.
  2021.
  Intelligent trading systems: a sentiment-aware reinforcement learning
  approach.
  In *Proceedings of the Second ACM International Conference on AI
  in Finance*, 1–9.
* Liu et al. (2020)

  Liu, X.-Y.; Yang, H.; Chen, Q.; Zhang, R.; Yang, L.; Xiao, B.; and Wang, C. D.
  2020.
  FinRL: A deep reinforcement learning library for automated stock
  trading in quantitative finance.
  *arXiv preprint arXiv:2011.09607*.
* Lu (2017)

  Lu, D. W. 2017.
  Agent inspired trading using recurrent reinforcement learning and
  lstm neural networks.
  *arXiv preprint arXiv:1707.07338*.
* Markowitz (1952)

  Markowitz, H. 1952.
  Portfolio Selection.
  *The Journal of Finance*, 7(1): 77–91.
* Martin (2021)

  Martin, R. A. 2021.
  PyPortfolioOpt: portfolio optimization in Python.
  *Journal of Open Source Software*, 6(61): 3066.
* Mnih et al. (2016)

  Mnih, V.; Badia, A. P.; Mirza, M.; Graves, A.; Lillicrap, T.; Harley, T.;
  Silver, D.; and Kavukcuoglu, K. 2016.
  Asynchronous methods for deep reinforcement learning.
  In *International conference on machine learning*, 1928–1937.
  PMLR.
* Mnih et al. (2013)

  Mnih, V.; Kavukcuoglu, K.; Silver, D.; Graves, A.; Antonoglou, I.; Wierstra,
  D.; and Riedmiller, M. 2013.
  Playing atari with deep reinforcement learning.
  *arXiv preprint arXiv:1312.5602*.
* Moody and Saffell (2001)

  Moody, J.; and Saffell, M. 2001.
  Learning to trade via direct reinforcement.
  *IEEE transactions on neural Networks*, 12(4): 875–889.
* Moody et al. (1998)

  Moody, J.; Wu, L.; Liao, Y.; and Saffell, M. 1998.
  Performance functions and reinforcement learning for trading systems
  and portfolios.
  *Journal of Forecasting*, 17(5-6): 441–470.
* Nguyen and La (2019)

  Nguyen, H.; and La, H. 2019.
  Review of deep reinforcement learning for robot manipulation.
  In *2019 Third IEEE International Conference on Robotic
  Computing (IRC)*, 590–595. IEEE.
* Raffin et al. (2021)

  Raffin, A.; Hill, A.; Gleave, A.; Kanervisto, A.; Ernestus, M.; and Dormann, N.
  2021.
  Stable-Baselines3: Reliable Reinforcement Learning Implementations.
  *Journal of Machine Learning Research*, 22(268): 1–8.
* Rao et al. (2020)

  Rao, N.; Aljalbout, E.; Sauer, A.; and Haddadin, S. 2020.
  How to make deep RL work in practice.
  *arXiv preprint arXiv:2010.13083*.
* Schulman et al. (2017)

  Schulman, J.; Wolski, F.; Dhariwal, P.; Radford, A.; and Klimov, O. 2017.
  Proximal policy optimization algorithms.
  *arXiv preprint arXiv:1707.06347*.
* Sharpe (1998)

  Sharpe, W. F. 1998.
  The sharpe ratio.
  *Streetwise–the Best of the Journal of Portfolio Management*,
  169–185.
* Silver et al. (2017)

  Silver, D.; Schrittwieser, J.; Simonyan, K.; Antonoglou, I.; Huang, A.; Guez,
  A.; Hubert, T.; Baker, L.; Lai, M.; Bolton, A.; et al. 2017.
  Mastering the game of go without human knowledge.
  *nature*, 550(7676): 354–359.
* Soleymani and Paquet (2020)

  Soleymani, F.; and Paquet, E. 2020.
  Financial portfolio optimization with online deep reinforcement
  learning and restricted stacked autoencoder—DeepBreath.
  *Expert Systems with Applications*, 156: 113456.
* Su et al. (2016)

  Su, P.-H.; Gasic, M.; Mrksic, N.; Rojas-Barahona, L.; Ultes, S.; Vandyke, D.;
  Wen, T.-H.; and Young, S. 2016.
  On-line active reward learning for policy optimisation in spoken
  dialogue systems.
  *arXiv preprint arXiv:1605.07669*.
* Sun et al. (2021)

  Sun, S.; Wang, R.; He, X.; Zhu, J.; Li, J.; and An, B. 2021.
  Deepscalper: A risk-aware deep reinforcement learning framework for
  intraday trading with micro-level market embedding.
  *arXiv preprint arXiv:2201.09058*.
* Sutton and Barto (2018)

  Sutton, R. S.; and Barto, A. G. 2018.
  *Reinforcement learning: An introduction*.
  MIT press.
* Théate and Ernst (2021)

  Théate, T.; and Ernst, D. 2021.
  An application of deep reinforcement learning to algorithmic trading.
  *Expert Systems with Applications*, 173: 114632.
* Wang et al. (2019)

  Wang, J.; Zhang, Y.; Tang, K.; Wu, J.; and Xiong, Z. 2019.
  Alphastock: A buying-winners-and-selling-losers investment strategy
  using interpretable deep reinforcement attention networks.
  In *Proceedings of the 25th ACM SIGKDD international conference
  on knowledge discovery & data mining*, 1900–1908.
* Wang et al. (2021)

  Wang, Z.; Huang, B.; Tu, S.; Zhang, K.; and Xu, L. 2021.
  DeepTrader: A Deep Reinforcement Learning Approach for Risk-Return
  Balanced Portfolio Management with Market Conditions Embedding.
  *Proceedings of the AAAI Conference on Artificial Intelligence*,
  35(1): 643–650.
* Wu et al. (2020)

  Wu, X.; Chen, H.; Wang, J.; Troiano, L.; Loia, V.; and Fujita, H. 2020.
  Adaptive stock trading strategies with deep reinforcement learning
  methods.
  *Information Sciences*, 538: 142–158.
* Yang et al. (2020)

  Yang, H.; Liu, X.-Y.; Zhong, S.; and Walid, A. 2020.
  Deep reinforcement learning for automated stock trading: An ensemble
  strategy.
  In *Proceedings of the First ACM International Conference on AI
  in Finance*, 1–8.
* Ye et al. (2020)

  Ye, Y.; Pei, H.; Wang, B.; Chen, P.-Y.; Zhu, Y.; Xiao, J.; and Li, B. 2020.
  Reinforcement-learning based portfolio management with augmented
  asset movement prediction states.
  In *Proceedings of the AAAI Conference on Artificial
  Intelligence*, volume 34, 1112–1119.
* Zhang, Zohren, and Roberts (2020)

  Zhang, Z.; Zohren, S.; and Roberts, S. 2020.
  Deep reinforcement learning for trading.
  *The Journal of Financial Data Science*, 2(2): 25–40.