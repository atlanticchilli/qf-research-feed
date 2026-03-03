---
authors:
- Nikhil Devanathan
- Dylan Rueter
- Stephen Boyd
- Emmanuel Candès
- Trevor Hastie
- Mykel J. Kochenderfer
- Arpit Apoorv
- David Soronow
- Igor Zamkovsky
doc_id: arxiv:2603.01298v1
family_id: arxiv:2603.01298
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Single-Asset Adaptive Leveraged Volatility Control
url_abs: http://arxiv.org/abs/2603.01298v1
url_html: https://arxiv.org/html/2603.01298v1
venue: arXiv q-fin
version: 1
year: 2026
---


Nikhil Devanathan
email: nikhil.devanathan@blackrock.com
BlackRock AI Lab

Dylan Rueter
BlackRock AI Lab

Stephen Boyd
BlackRock AI Lab


  
Emmanuel Candès
BlackRock AI Lab

Trevor Hastie
BlackRock AI Lab

Mykel J. Kochenderfer
BlackRock AI Lab


  
Arpit Apoorv
BlackRock Index Services

David Soronow
BlackRock Index Services

Igor Zamkovsky
BlackRock Index Services

###### Abstract

This paper introduces methodologies for constructing an index composed of a risky asset and a risk-free asset that achieves a fixed target volatility. We propose a simple proportional-control-based approach for setting the index weights, and we demonstrate in simulation that this method is more effective at consistently achieving the target volatility than an open-loop approach. We additionally present a modification to our proportional control approach that reduces index drawdowns in simulation.

## 1 Introduction

We propose a method to form an index composed of two assets only—a risky asset and a risk-free asset—achieving a
fixed pre-specified volatility. We work under two assumptions: first, the risky asset cannot be shorted and second, we have an upper limit on leverage.

Volatility‐targeting strategies trace back to the rule of scaling portfolio exposure inversely with a forecast of return variance, as formalized by [moreira2017]. Large empirical studies—e.g., [harvey2018]—confirm that such open-loop rules improve Sharpe ratios and reduce tail risk across many asset classes. However, they also highlight practical issues such as turnover, leverage spikes, and sensitivity to volatility estimation error.

Recent papers attempt to remedy these weaknesses. Conditional schemes restrict scaling to extreme volatility regimes [bongaerts2020], while Bayesian or exponentially-weighted moving average (EWMA) smoothing dampens weight oscillations [bernardi2022]. At the same time, [cederburg2020] document that out-of-sample benefits can vanish once implementation frictions are considered. In contrast, we cast volatility management as a simple proportional feedback-control problem that explicitly corrects tracking error and, in an extension, throttles leverage during drawdowns—all using transparent parameters.

## 2 Methodology

Our goal is to construct an index from a single risky asset and a single risk-free asset (for illustration, we use cash) which achieves a specified level of volatility σtar>0\sigma^{\text{tar}}>0 without exceeding a limit L>0L>0 on the weight allocated to the risky asset. We call σtar\sigma^{\text{tar}} the target volatility and LL the leverage limit. We denote by t1,t2,…t\_{1},t\_{2},\ldots the time sequence at which we
observe the returns of the risky asset, realize interest on cash balances, and have the opportunity to rebalance
the index. We define the trailing returns of the risky asset and risk-free asset at time tkt\_{k} as rk,rkrf∈ℝr\_{k},r^{\text{rf}}\_{k}\in\mathbb{R} respectively.

#### Index weights and returns.

An index is a pair of weights (wk,ck)(w\_{k},c\_{k}) at time tkt\_{k} such that wk∈ℝw\_{k}\in\mathbb{R} is the weight of the risky asset and ck∈ℝc\_{k}\in\mathbb{R} that of cash. The weights must satisfy the conditions

|  |  |  |
| --- | --- | --- |
|  | wk+ck=1,0≤wk≤L.w\_{k}+c\_{k}=1,\qquad 0\leq w\_{k}\leq L. |  |

The weights represent the fraction of the index invested in the risky asset and cash, respectively. A negative cash weight corresponds to leverage, or borrowing cash to invest more in the risky asset, which we can take in a limited capacity. When taking leverage, we pay interest on the borrowed cash rather than accruing positive interest on the cash. Between two consecutive times tk−1t\_{k-1} and tkt\_{k}, the index return rkindr^{\text{ind}}\_{k} is given by

|  |  |  |
| --- | --- | --- |
|  | rkind=rk​wk−1+rkrf​ck−1.r^{\text{ind}}\_{k}=r\_{k}w\_{k-1}+r^{\text{rf}}\_{k}c\_{k-1}. |  |

#### Realized volatility.

The realized volatility σ^k\hat{\sigma}\_{k} of the risky asset at time tkt\_{k} is defined as the square root of an EWMA of the squared risky asset returns r1,…,rkr\_{1},\ldots,r\_{k},

|  |  |  |  |
| --- | --- | --- | --- |
|  | (σ^k)2=1−β1−βk​∑j=1kβk−j​(rj)2,\left(\hat{\sigma}\_{k}\right)^{2}=\frac{1-\beta}{1-\beta^{k}}\sum\_{j=1}^{k}\beta^{k-j}\left(r\_{j}\right)^{2}, |  | (1) |

with a halflife h>0h>0 and decay factor β=exp⁡(−log⁡(2)/h)\beta=\exp(-\log(2)/h) [johansson2023]. (This is a EWMA estimate of the second moment, but we use the fact that daily returns have means that are much smaller in magnitude than the returns.) Note that σ^k\hat{\sigma}\_{k} is known at the time that wkw\_{k} is decided.

#### Realized index volatility.

Analogously, we define the realized index volatility σ^kind\hat{\sigma}^{\text{ind}}\_{k} at time tkt\_{k} as the square root of the EWMA of the squared index returns r1ind,…,rkindr\_{1}^{\text{ind}},\ldots,r\_{k}^{\text{ind}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | (σ^kind)2=1−β1−βk​∑j=1kβk−j​(rjind)2.\left(\hat{\sigma}^{\text{ind}}\_{k}\right)^{2}=\frac{1-\beta}{1-\beta^{k}}\sum\_{j=1}^{k}\beta^{k-j}\left(r\_{j}^{\text{ind}}\right)^{2}. |  | (2) |

Note that σ^kind\hat{\sigma}^{\text{ind}}\_{k} is known at the time that wkw\_{k} is decided.

#### Tracking error.

We define our relative instantaneous volatility tracking error eke\_{k} at time tkt\_{k} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ek=log⁡(σ^kind/σtar).e\_{k}=\log(\hat{\sigma}^{\text{ind}}\_{k}/\sigma^{\text{tar}}). |  | (3) |

The instantaneous tracking error eke\_{k} is approximately the percentage difference between the realized index volatility σ^kind\hat{\sigma}^{\text{ind}}\_{k} and the target volatility σtar\sigma^{\text{tar}}. Over a period tj,tj+1,…,tkt\_{j},t\_{j+1},\ldots,t\_{k}, the average absolute volatility tracking error is

|  |  |  |
| --- | --- | --- |
|  | 1k−j+1​∑i=jk|ei|.\frac{1}{k-j+1}\sum\_{i=j}^{k}|e\_{i}|. |  |

#### The volatility control problem.

The problem is to determine a policy that chooses wkw\_{k} and ckc\_{k} at time tkt\_{k} based on information known at time tkt\_{k} (such as σ^k,σ^kind,ek\hat{\sigma}\_{k},\hat{\sigma}\_{k}^{\text{ind}},e\_{k}) in such a way that the average absolute volatility tracking error is minimized.

### 2.1 Open-loop approach

In the simplest, ideal case, the returns of the risk-free asset are known constants and the returns of the risky asset are independently and identically distributed according to a normal distribution with mean μ∈ℝ\mu\in\mathbb{R} and standard deviation σ>0\sigma>0 at each time t1,…t\_{1},\ldots. In this case, the index returns at time tk+1t\_{k+1} are distributed according to a normal distribution with mean wk​μ+ck​rk+1rfw\_{k}\mu+c\_{k}r^{\text{rf}}\_{k+1} and standard deviation wk​σw\_{k}\sigma. If we assume that |μ|≪σ|\mu|\ll\sigma and rkrf≪σr^{\text{rf}}\_{k}\ll\sigma, then the expected value of (rk+1)2(r\_{k+1})^{2} is approximately σ2\sigma^{2} and the expected value of (rk+1ind)2(r\_{k+1}^{\text{ind}})^{2} is approximately wk2​σ2w\_{k}^{2}\sigma^{2}. It follows by the linearity of expectation that the expected variance (σ^k)2(\hat{\sigma}\_{k})^{2} of the risky asset is approximately (σ)2(\sigma)^{2}.

In this case, a natural approach to choosing wkw\_{k} and ckc\_{k} such that the expected value of (rk+1ind)2(r\_{k+1}^{\text{ind}})^{2} is equal to σtar\sigma^{\text{tar}} is to set

|  |  |  |  |
| --- | --- | --- | --- |
|  | wk=min⁡{σtar/σ^k,L},ck=1−wk.w\_{k}=\min\{\sigma^{\text{tar}}/\hat{\sigma}\_{k},L\},\qquad c\_{k}=1-w\_{k}. |  | (4) |

When σtar/σ^k≤L\sigma^{\text{tar}}/\hat{\sigma}\_{k}\leq L, we set the risky asset weight wkw\_{k} so that the expected value of the index variance is equal to the target variance. When σtar/σ^k>L\sigma^{\text{tar}}/\hat{\sigma}\_{k}>L, we set wk=Lw\_{k}=L, accepting that this is the best we can do given the leverage limit. We call this approach the “open-loop” approach because the weights wkw\_{k} are set without any regard to the previous index weights w1,…,wk−1w\_{1},\ldots,w\_{k-1}.

This methodology is summarized in Algorithm [1](#alg1 "Algorithm 1 ‣ 2.1 Open-loop approach ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control").

Algorithm 1  Open-loop solution to index construction

1:

Input: σtar,L\sigma^{\text{tar}},L

2:

for k=1,2,…k=1,2,\ldots do

3:   

Observe risky asset volatility σ^k\hat{\sigma}\_{k}

4:      

Set risky asset weight wk=min​{σtar/σ^k,L}w\_{k}=\text{min}\{\sigma^{\text{tar}}/\hat{\sigma}\_{k},L\}

5:      

Set cash weight ck=1−wkc\_{k}=1-w\_{k}

In practice, although this method may sometimes perform reasonably, it fares poorly when there are
changes in the prevailing volatility of the risky asset. This is illustrated in §[3](#S3 "3 Results ‣ Single-Asset Adaptive Leveraged Volatility Control").

### 2.2 Volatility control

We now modify the methodology from §[2.1](#S2.SS1 "2.1 Open-loop approach ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control") to better react to shifts in the volatility
of the risky asset. To achieve this, we add a control parameter κk∈ℝ\kappa\_{k}\in\mathbb{R} to our policy ([4](#S2.E4 "In 2.1 Open-loop approach ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control")) and set wkw\_{k} and ckc\_{k} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | wk=min​{exp⁡(κk)​σtar/σ^k,L},ck=1−wk.w\_{k}=\text{min}\{\exp(\kappa\_{k})\sigma^{\text{tar}}/\hat{\sigma}\_{k},L\},\qquad c\_{k}=1-w\_{k}. |  | (5) |

Above, the term exp⁡(κk)\exp(\kappa\_{k}) scales the risk target and thus allows
us to adjust for persistent overestimation or underestimation of the volatility of the risky asset. Scaling via exp⁡(κk)\exp(\kappa\_{k}) rather than κk\kappa\_{k} is a matter of convention. It is motivated by the observation that the volatility of a stock tends to vary on a logarithmic scale: for an asset with a mean volatility of X%X\%, periods of 2​X%2X\% and 12​X%\frac{1}{2}X\% volatility will be approximately equally likely.

It remains to discuss how to dynamically set the control parameter κk\kappa\_{k}, and we describe a simple methodology, which depends on only four parameters. The four parameters are a proportional gain g>0g>0, a control parameter lower bound κmin<0\kappa\_{\text{min}}<0, an upper bound κmax>0\kappa\_{\text{max}}>0, and a smoothing factor θ∈(0,1)\theta\in(0,1). After setting these parameters, we compute κk\kappa\_{k} via

|  |  |  |  |
| --- | --- | --- | --- |
|  | κk=(1−θ)​clip​(−g​ek;I)+θ​κk−1\kappa\_{k}=(1-\theta)\text{clip}(-ge\_{k};I)+\theta\kappa\_{k-1} |  | (6) |

in which

|  |  |  |  |
| --- | --- | --- | --- |
|  | I=[κmin,κmax],clip​(t;[a,b])={a,t<a,t,a≤t≤b,bt>b.I=[\kappa\_{\text{min}},\kappa\_{\text{max}}],\qquad\text{clip}(t;[a,b])=\begin{cases}a,&t<a,\\ t,&a\leq t\leq b,\\ b&t>b.\end{cases} |  | (7) |

This controller is designed to adjust κk\kappa\_{k} based on the discrepancy between the realized volatility of the index σ^kind\hat{\sigma}^{\text{ind}}\_{k} and the target volatility σtar\sigma^{\text{tar}}. To simplify, assume θ=0\theta=0 (no smoothing) and that the volatility of the index has recently been lower than the target. Then the error eke\_{k} will be negative, and the term −g​ek-ge\_{k} will be positive, meaning that we will target a higher volatility in the next iteration. Conversely, if the volatility of the index has recently been higher than the target, then eke\_{k} will be positive, and −g​ek-ge\_{k} will be negative, meaning that we will target a lower volatility in the next iteration.

The gain parameter gg influences how reactive κk\kappa\_{k} is to discrepancies between the realized and target volatilities. The clipping imposes reasonable limits on κk\kappa\_{k} to prevent it from becoming too large or too small. The smoothing factor θ\theta determines how quickly κk\kappa\_{k} can change; a larger value of θ\theta means that κk\kappa\_{k} will change more slowly, while a smaller value implies κk\kappa\_{k} will change more quickly.

Since the volatility control methodology assumes our index has some history (for volatility estimation),
we recommend either running or simulating the open-loop method for some time before switching to the volatility control
methodology.

The volatility control methodology is summarized in Algorithm [2](#alg2 "Algorithm 2 ‣ 2.2 Volatility control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control") and its performance is demonstrated in §[3](#S3 "3 Results ‣ Single-Asset Adaptive Leveraged Volatility Control").

Algorithm 2  Volatility control for index weight selection

1:

Input: σtar,L,g,κmin,κmax,θ\sigma^{\text{tar}},L,g,\kappa\_{\text{min}},\kappa\_{\text{max}},\theta

2:

Set κ0=0\kappa\_{0}=0

3:

for tk=tstart,…t\_{k}=t\_{\text{start}},\ldots do

4:   

Produce an index volatility estimate σ^kind\hat{\sigma}^{\text{ind}}\_{k} from historical index returns

5:      

Compute volatility control error as in ([3](#S2.E3 "In Tracking error. ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control"))

6:      

Compute volatility control parameter as in ([6](#S2.E6 "In 2.2 Volatility control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control"))

7:      

Set risky asset weight wk=min​{exp⁡(κk)​σtar/σ^k,L}w\_{k}=\text{min}\{\exp(\kappa\_{k})\sigma^{\text{tar}}/\hat{\sigma}\_{k},L\}

8:      

Set cash weight ck=1−wkc\_{k}=1-w\_{k}

### 2.3 Leverage control

While producing an index realizing a fixed volatility is the primary objective, we would also like to mitigate drawdowns resulting from
using leverage during market downturns. To achieve this, we introduce a methodology which sacrifices some volatility-tracking performance in order to
attempt to reduce the leverage of the index during periods of negative returns. We achieve this by adding a control parameter κklev≤0\kappa\_{k}^{\text{lev}}\leq 0 to the leverage limit LL in our policy ([5](#S2.E5 "In 2.2 Volatility control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control")), and set our weights such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | wk=min​{exp⁡(κk)​σtar/σ^k,exp⁡(κklev)​L},ck=1−wk.w\_{k}=\text{min}\{\exp(\kappa\_{k})\sigma^{\text{tar}}/\hat{\sigma}\_{k},\exp(\kappa\_{k}^{\text{lev}})L\},\qquad c\_{k}=1-w\_{k}. |  | (8) |

We mandate κminlev≤κklev≤0\kappa^{\text{lev}}\_{\text{min}}\leq\kappa\_{k}^{\text{lev}}\leq 0, where κminlev<0\kappa^{\text{lev}}\_{\text{min}}<0 is a fixed lower bound, so that we will only ever reduce the leverage limit LL or leave it as it is. Its purpose is to reduce the leverage limit LL when the index is trending downwards.

Let

|  |  |  |
| --- | --- | --- |
|  | Rkind=∏j=1k(1+rjind)R\_{k}^{\text{ind}}=\prod\_{j=1}^{k}(1+r\_{j}^{\text{ind}}) |  |

be the cumulative return of the index at time tkt\_{k}.
From R1ind,…,RkindR\_{1}^{\text{ind}},\ldots,R\_{k}^{\text{ind}}, we compute EWMAs MAklong\text{MA}\_{k}^{\text{long}} and MAkshort\text{MA}\_{k}^{\text{short}} of RkindR\_{k}^{\text{ind}} with halflives hlong>hshort>0h^{\text{long}}>h^{\text{short}}>0.
We then set

|  |  |  |  |
| --- | --- | --- | --- |
|  | κklev=clip​(−gℓ​log⁡(MAklong/MAkshort);[κminlev,0]).\kappa\_{k}^{\text{lev}}=\text{clip}\left(-g\_{\ell}\log\left({\text{MA}\_{k}^{\text{long}}}/{\text{MA}\_{k}^{\text{short}}}\right);[\kappa^{\text{lev}}\_{\text{min}},0]\right). |  | (9) |

This has a simple interpretation: when the short-term moving average is smaller than the long-term moving average, the leverage limit is reduced. As earlier, the parameter gℓ>0g\_{\ell}>0 is a gain that determines how quickly the leverage limit is reduced.

The leverage control methodology is summarized in Algorithm [3](#alg3 "Algorithm 3 ‣ 2.3 Leverage control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control").

Algorithm 3  Volatility + Leverage control for index weight selection

1:

Input: σtar,L,g,gℓ,κmin,κmax,κminlev,hlong,hshort,θ\sigma^{\text{tar}},L,g,g\_{\ell},\kappa\_{\text{min}},\kappa\_{\text{max}},\kappa\_{\text{min}}^{\text{lev}},h^{\text{long}},h^{\text{short}},\theta

2:

Set κ0=0\kappa\_{0}=0

3:

for tk=tstart,…t\_{k}=t\_{\text{start}},\ldots do

4:   

Produce an index volatility estimate σ^kind\hat{\sigma}^{\text{ind}}\_{k} from historical index returns

5:      

Compute volatility control error as in ([3](#S2.E3 "In Tracking error. ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control"))

6:      

Compute volatility control parameter as in ([6](#S2.E6 "In 2.2 Volatility control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control"))

7:      

Compute leverage control parameter as in ([9](#S2.E9 "In 2.3 Leverage control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control"))

8:      

Set risky asset weight wk=min​{exp⁡(κk)​σtar/σ^k,exp⁡(κklev)​L}w\_{k}=\text{min}\{\exp(\kappa\_{k})\sigma^{\text{tar}}/\hat{\sigma}\_{k},\exp(\kappa\_{k}^{\text{lev}})L\}

9:      

Set cash weight ck=1−wkc\_{k}=1-w\_{k}

In general, varying the leverage limit in order to reduce downside effects is a difficult problem since it is effectively equivalent to timing the market. Certainly,
using the leverage controller does not guarantee smaller drawdowns or greater returns than using the volatility controller alone. In the
example from §[3](#S3 "3 Results ‣ Single-Asset Adaptive Leveraged Volatility Control"), we see that the leverage controller works well, but this is not uniformly the case for all the risky assets we have tested.
The leverage controller also seems more sensitive to the choice of the gain parameter gℓg\_{\ell} than the volatility controller is to gg, though
we provide the parameter values that have worked well for us in our experiments in §[3](#S3 "3 Results ‣ Single-Asset Adaptive Leveraged Volatility Control"). We document the leverage controller
because we feel it shows some promise, but we do not fully endorse it.

## 3 Results

In this section, we present results about the performance of Algorithms [1](#alg1 "Algorithm 1 ‣ 2.1 Open-loop approach ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control"), [2](#alg2 "Algorithm 2 ‣ 2.2 Volatility control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control"), and [3](#alg3 "Algorithm 3 ‣ 2.3 Leverage control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control").

#### Simulation details.

Our simulation spans the trading days from June 6th, 2000 to April 9th, 2025, inclusive.
The risky asset is IVV, the iShares Core S&P 500 exchange traded fund (ETF), which provides broad exposure to large-cap U.S. equities. We use close-to-close returns for IVV and assume that returns are observed, new weights are computed, and the index is rebalanced instantaneously at market close. The return on cash is the daily Federal Funds Effective Rate. We compute the risky asset volatility estimate σ^k\hat{\sigma}\_{k} as the square root of an EWMA of the squared risky asset returns r1,…,rkr\_{1},\ldots,r\_{k} with a halflife of 126 trading days.
We set the leverage limit to L=1.5L=1.5 and the target volatility to σtar=0.15/252\sigma^{\text{tar}}=0.15/\sqrt{252}, corresponding to an annualized volatility of 15%15\%.

In Algorithm [2](#alg2 "Algorithm 2 ‣ 2.2 Volatility control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control"), we set g=50g=50, κmin=−1\kappa\_{\text{min}}=-1, κmax=1\kappa\_{\text{max}}=1, and θ=0.5\theta=0.5. In Algorithm [3](#alg3 "Algorithm 3 ‣ 2.3 Leverage control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control")
we additionally set gℓ=20g\_{\ell}=20, κminlev=−2\kappa\_{\text{min}}^{\text{lev}}=-2, and otherwise use the same values for all the other parameters.
We use a 126-trading-day EWMA of the cumulative index returns for MAklong\text{MA}\_{k}^{\text{long}} and a
42-trading-day EWMA for MAkshort\text{MA}\_{k}^{\text{short}}.
For both Algorithms [2](#alg2 "Algorithm 2 ‣ 2.2 Volatility control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control") and [3](#alg3 "Algorithm 3 ‣ 2.3 Leverage control ‣ 2 Methodology ‣ Single-Asset Adaptive Leveraged Volatility Control"), we run the method for the first 10 trading days before engaging control. In both cases,
we compute the index volatility estimate σ^kind\hat{\sigma}^{\text{ind}}\_{k} as the square root of an EWMA of the
squared index returns r1ind,…,rkindr\_{1}^{\text{ind}},\ldots,r\_{k}^{\text{ind}} with a halflife of 126 trading days.

#### Discussion.

Figure [1](#S3.F1 "Figure 1 ‣ Discussion. ‣ 3 Results ‣ Single-Asset Adaptive Leveraged Volatility Control") shows the cumulative returns of the IVV, the open-loop method, the volatility control method, and the
volatility plus leverage control method. Figure [2](#S3.F2 "Figure 2 ‣ Discussion. ‣ 3 Results ‣ Single-Asset Adaptive Leveraged Volatility Control") shows the running estimated volatility of IVV and that of the three
methods over the same period. The Monte Carlo methodology described in Appendix [A](#A1 "Appendix A Evaluation ‣ Single-Asset Adaptive Leveraged Volatility Control") was used to compute 10th and 90th percentiles for
the running volatility estimate of an asset with a true volatility of 15%15\%.

Table [1](#S3.T1 "Table 1 ‣ Discussion. ‣ 3 Results ‣ Single-Asset Adaptive Leveraged Volatility Control") summarizes the performance of the four methods over the simulation period. The volatility tracking error is computed as the
mean absolute error between the running volatility estimate of the method and the target volatility σtar\sigma^{\text{tar}}, scaled by 252\sqrt{252} to
give an annualized value. Although IVV does not track a volatility target, we still provide a volatility tracking error for IVV for reference.

As shown in the figures and table, the leverage control method provides a slightly greater return and a slightly smaller maximum drawdown than the
volatility control method. This performance does come at the cost of some tracking error with respect to the 15%15\% target. Both the leverage
control and volatility control methods outperform the open-loop method in terms of return, volatility tracking error, and maximum drawdown.

![Refer to caption](2603.01298v1/x1.png)


Figure 1: Cumulative returns of four indices.

![Refer to caption](2603.01298v1/x2.png)


Figure 2: Running annualized estimated volatility of four indices. 15% target volatility is shown as a solid black line. A 90% confidence interval for the running volatility estimate of an asset with a true volatility of 15%15\% is shown as a shaded region.



|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | IVV | Open-Loop | Volatility Control | Leverage Control |
| Volatility Tracking Error | 5.2%5.2\% | 2.3%2.3\% | 0.4%\mathbf{0.4\%} | 0.6%0.6\% |
| Annualized Return | 9.0%9.0\% | 7.4%7.4\% | 9.0%9.0\% | 9.7%\mathbf{9.7\%} |
| Annualized Volatility | 19.2%19.2\% | 15.1%15.1\% | 14.9%\mathbf{14.9\%} | 14.7%14.7\% |
| Sharpe Ratio | 0.470.47 | 0.490.49 | 0.610.61 | 0.66\mathbf{0.66} |
| Maximum Drawdown | 55.3%55.3\% | 38.7%38.7\% | 38.3%38.3\% | 32.9%\mathbf{32.9\%} |

Table 1: Summary of performance metrics for four indices.

## Acknowledgments

We would like to acknowledge Gabriel Maher, Rob Tibshirani, and Ludovic Breger for their work on an initial methodology we built upon. We would additionally like to thank Veronica Mai, Logan Bell, Alex Tzikas, Raphael Chinchilla, and Ron Kahn for helpful discussions and feedback.

## References

## Appendix A Evaluation

Suppose we produced an index that had a volatility exactly equal to σtar\sigma^{\text{tar}}. Any empirical estimate of the volatility σkeval\sigma^{\text{eval}}\_{k} from realized returns will almost surely not equal σtar\sigma^{\text{tar}}.
It is thus important to understand
how closely we can expect our volatility estimates to match the target volatility.

For this purpose, we suggest the following benchmarking methodology:

1. 1.

   Independently sample NN (for some large integer NN) synthetic return values r1synth,…,rNsynthr\_{1}^{\text{synth}},\ldots,r\_{N}^{\text{synth}} from a normal
   distribution with mean 0 and standard deviation σtar\sigma^{\text{tar}}.
2. 2.

   Compute volatility estimates σksynth\sigma^{\text{synth}}\_{k} from the synthetic returns r1synth,…,rksynthr\_{1}^{\text{synth}},\ldots,r\_{k}^{\text{synth}} using the
   same method we used to compute σkeval\sigma^{\text{eval}}\_{k} from the index returns r1ind,…,rkindr\_{1}^{\text{ind}},\ldots,r\_{k}^{\text{ind}}.
3. 3.

   Discard the first nn values of σksynth\sigma^{\text{synth}}\_{k} (where nn is a burn-in period for the volatility estimate).
4. 4.

   Compute statistics of interest from the remaining values of σn+1synth,…,σNsynth\sigma^{\text{synth}}\_{n+1},\ldots,\sigma^{\text{synth}}\_{N}.

Specifically, because we do not have the ability to observe the true volatility of our index, this methodology allows us to quantify the uncertainty of volatility estimates and understand the fluctuations we can expect to see if the index is tracking the target volatility.

### A.1 Example

Suppose we estimate the volatility of our index via a EWMA with halflife hh. We define α=exp⁡(−log⁡(2)/h)\alpha=\exp(-\log(2)/h) to be the corresponding decay factor of the EWMA.
If we had infinitely many synthetic returns values from a normal distribution with mean 0 and standard deviation σtar\sigma^{\text{tar}},
then we can define the infinite-sample, halflife-hh EWMA volatility estimate

|  |  |  |
| --- | --- | --- |
|  | σsynth=(1−α)​∑i=1∞αi−1​(risynth)2.\sigma^{\text{synth}}=\sqrt{(1-\alpha)\sum\_{i=1}^{\infty}\alpha^{i-1}\left(r\_{i}^{\text{synth}}\right)^{2}}. |  |

It is a result of probability that σsynth\sigma^{\text{synth}} is approximately distributed according to a scaled χ\chi distribution with
1−α2(1−α)2\frac{1-\alpha^{2}}{(1-\alpha)^{2}} degrees of freedom and a scale factor of σ​1−α1−α2\sigma\frac{1-\alpha}{\sqrt{1-\alpha^{2}}}. From this
approximation, we can estimate the standard deviation
of these of EWMA volatility estimates as a function of the halflife hh. For σtar=0.15/252\sigma^{\text{tar}}=0.15/\sqrt{252},
corresponding to an annualized volatility of 15%15\%, we show the estimated standard deviation of σsynth\sigma^{\text{synth}} as a function of hh in
Figure [3](#A1.F3 "Figure 3 ‣ A.1 Example ‣ Appendix A Evaluation ‣ Single-Asset Adaptive Leveraged Volatility Control").

![Refer to caption](2603.01298v1/x3.png)


Figure 3: Approximate standard deviation of the ideal EWMA volatility estimate σsynth\sigma^{\text{synth}} as a function of halflife hh for σtar=0.15/252\sigma^{\text{tar}}=0.15/\sqrt{252}.

Returning to the sampling-based methodology we proposed, we can verify that for reasonably large NN, the synthetic volatility estimates
σn+1synth,…,σNsynth\sigma^{\text{synth}}\_{n+1},\ldots,\sigma^{\text{synth}}\_{N} will be distributed according to the distribution of σsynth\sigma^{\text{synth}}.
For σtar=0.15/252\sigma^{\text{tar}}=0.15/\sqrt{252} and halflives h=21,126h=21,126, we demonstrate this in Figure [4](#A1.F4 "Figure 4 ‣ A.1 Example ‣ Appendix A Evaluation ‣ Single-Asset Adaptive Leveraged Volatility Control").

![Refer to caption](2603.01298v1/x4.png)


Figure 4: Distribution of EWMA volatility estimates σsynth\sigma^{\text{synth}} from Monte Carlo simulation with N=10000N=10000 samples and the first n=252n=252 discarded. The dashed lines show the approximate distribution of σsynth\sigma^{\text{synth}} for halflives h=21,126h=21,126.

As evidenced by Figures [3](#A1.F3 "Figure 3 ‣ A.1 Example ‣ Appendix A Evaluation ‣ Single-Asset Adaptive Leveraged Volatility Control") and [4](#A1.F4 "Figure 4 ‣ A.1 Example ‣ Appendix A Evaluation ‣ Single-Asset Adaptive Leveraged Volatility Control"), EWMA volatility estimates of σtar\sigma^{\text{tar}} with longer
halflives have significantly less variance.
As such, we recommend using halflives of at least 63 when evaluating the performance of our index construction methods.

BETA