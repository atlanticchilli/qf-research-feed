---
authors:
- Visca Tri Winarty
- Sena Safarina
doc_id: arxiv:2510.15288v1
family_id: arxiv:2510.15288
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization
url_abs: http://arxiv.org/abs/2510.15288v1
url_html: https://arxiv.org/html/2510.15288v1
venue: arXiv q-fin
version: 1
year: 2025
---


Visca Tri Winarty
  
Sena Safarina

###### Abstract

Since the COVID-19 pandemic, the number of investors in the Indonesia Stock Exchange has steadily increased, emphasizing the importance of portfolio optimization in balancing risk and return. The classical mean–variance optimization model, while widely applied, depends on historical return and risk estimates that are uncertain and may result in suboptimal portfolios. To address this limitation, robust optimization incorporates uncertainty sets to improve portfolio reliability under market fluctuations. This study constructs such sets using moving-window and bootstrapping methods and applies them to Indonesian banking stock data with varying risk-aversion parameters. The results show that robust optimization with the moving-window method, particularly with a smaller risk-aversion parameter, provides a better risk–return trade-off compared to the bootstrapping approach. These findings highlight the potential of the moving-window method to generate more effective portfolio strategies for risk-tolerant investors.

###### keywords:

Portfolio Optimization, Uncertainty Set, Robust Optimization, Mean Variance Optimization

## 1 Introduction

Since the emergence of the COVID-19 pandemic, the Indonesia Stock Exchange (IDX) has reported a gradual increase in the number of capital market investors. As of December 2022, the total number of investors had reached 10.23 million, representing an increase compared to previous years. This upward trend is projected to continue in the subsequent year [[9](https://arxiv.org/html/2510.15288v1#bib.bib9)]. With the rising number of investors in Indonesia’s capital market, the implementation of portfolio optimization becomes increasingly relevant for achieving balanced investment outcomes in terms of the risk-return trade-off.

Portfolio optimization is a fundamental concept in investment, with the primary objective of minimizing risk or maximizing expected returns. Harry Markowitz [[8](https://arxiv.org/html/2510.15288v1#bib.bib8)] introduced the modern portfolio optimization model, which has been widely applied to guide investors in constructing an efficient portfolio. The classical model is formulated below.

|  |  |  |  |
| --- | --- | --- | --- |
|  | min:γ2​𝒙T​𝚺𝒙−𝝁T​𝒙,s.t:𝒆T​𝒙=1,0≤xi≤1fori=1,2,…,n.\displaystyle\begin{array}[]{rcl}\min&:&\frac{\gamma}{2}\mbox{$x$}^{T}\mbox{$\Sigma$}\mbox{$x$}-\mbox{$\mu$}^{T}\mbox{$x$},\\ \text{s.t}&:&\boldsymbol{e}^{T}\mbox{$x$}=1,\\ &&0\leq{x\_{i}}\leq 1\quad\mbox{for}\quad i=1,2,\ldots,n.\end{array} |  | (4) |

In model ([4](https://arxiv.org/html/2510.15288v1#S1.E4 "In 1 Introduction ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")), the important variable is 𝒙∈ℝn\boldsymbol{x}\in\mbox{$\mathbb{R}$}^{n}, which denotes the vector of nn-asset allocation. The objective is to minimize the trade-off between the risk, γ2​Var​(𝒓T​𝒙)=γ2​𝒙T​𝚺𝒙\frac{\gamma}{2}\mbox{Var}(\boldsymbol{r}^{T}\mbox{$x$})=\frac{\gamma}{2}\mbox{$x$}^{T}\mbox{$\Sigma$}\mbox{$x$}, and the expected portfolio return, E​(𝒓T​𝒙)=𝝁T​𝒙E(\boldsymbol{r}^{T}\mbox{$x$})=\mbox{$\mu$}^{T}\mbox{$x$}. The constraint 𝒆T​𝒙=1\boldsymbol{e}^{T}\mbox{$x$}=1 ensures that the total asset allocation
equals 100%100\%, with 𝒆∈ℝn\boldsymbol{e}\in\mbox{$\mathbb{R}$}^{n} denoting the vector of ones. Finally, the bound 0≤xi≤10\leq x\_{i}\leq 1 for i=1,2,…,ni=1,2,\ldots,n indicates no short selling in this classical model.

In the objective function, γ∈ℝ++\gamma\in\mbox{$\mathbb{R}$}\_{++} represents the risk-aversion parameter and 𝝁T=[μ1​μ2​⋯​μn]\mbox{$\mu$}^{T}=[\mu\_{1}\ \mu\_{2}\ \cdots\mu\_{n}] denotes the vector of expected assets’ return, computed by

|  |  |  |  |
| --- | --- | --- | --- |
|  | μi=1m​∑t=1mri,t\mu\_{i}=\frac{1}{m}\sum\_{t=1}^{m}r\_{i,t} |  | (5) |

where ri,tr\_{i,t} is the daily return of asset-ii and for period-tt and mm is the length of observation period. Furthermore, the variance-covariance matrix 𝚺\Sigma can be obtained by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σi,j=1m​∑t=1m(ri,t−μi)​(rj,t−μj)\sigma\_{i,j}=\frac{1}{m}\sum\_{t=1}^{m}(r\_{i,t}-\mu\_{i})(r\_{j,t}-\mu\_{j}) |  | (6) |

for i,j∈{1,2,⋯,n}i,j\in\{1,2,\cdots,n\}.

The classical model ([4](https://arxiv.org/html/2510.15288v1#S1.E4 "In 1 Introduction ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")) presumes that both parameters ([5](https://arxiv.org/html/2510.15288v1#S1.E5 "In 1 Introduction ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")) and ([6](https://arxiv.org/html/2510.15288v1#S1.E6 "In 1 Introduction ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")) are known with certainty. However, in practice, the problem faces the uncertainty of future data, since both asset returns and risk measures are unknown and must be estimated from historical data [[10](https://arxiv.org/html/2510.15288v1#bib.bib10)]. However, these estimates are often subject to significant errors, as past observations may not accurately reflect future market conditions. To address such a limitation, the mean–variance optimization model is often reformulated as a robust optimization model [[1](https://arxiv.org/html/2510.15288v1#bib.bib1), [4](https://arxiv.org/html/2510.15288v1#bib.bib4), [7](https://arxiv.org/html/2510.15288v1#bib.bib7), [11](https://arxiv.org/html/2510.15288v1#bib.bib11)]. The key advantage of robust optimization lies in its ability to generate portfolio solutions that remain effective in worst-case scenarios. This approach has been widely applied in finance, particularly in the construction of optimal portfolios.

Tütüncü and Koenig [[11](https://arxiv.org/html/2510.15288v1#bib.bib11)] showed that robust optimization improves portfolio performance when uncertain inputs are represented within an uncertainty set. Several approaches can be used to construct such a set; for instance, Tütüncü and Koenig [[11](https://arxiv.org/html/2510.15288v1#bib.bib11)] proposed a moving-window method, while Abdurakhman [[1](https://arxiv.org/html/2510.15288v1#bib.bib1)] employed bootstrapping. Motivated by these studies, this research adopts both methods to build the uncertainty set and compares their effects on the optimal portfolio solution obtained from the robust optimization model. The model is then solved in MATLAB for different risk-aversion parameters, where a smaller value reflects a higher tolerance for investment risk. In particular, this research focuses on implementing and comparing robust optimization with moving-window and bootstrapping methods using Indonesian banking stocks data.

The rest of this paper is ordered as follows. In Section 2, we explain robust portfolio optimization, as well as the implementation of moving window and bootstrapping methods to obtain the uncertainty set. Section 3 shows the numerical results for comparing robust portfolio optimization with moving window and bootstrapping methods. We also compare both results with the classical MVO. In Section 4, we present conclusions and discussions for future directions.

## 2 Robust Optimization

Robust optimization is an approach to solving optimization problems that require information about uncertainty sets in order to determine the worst-case scenarios to be optimized [[2](https://arxiv.org/html/2510.15288v1#bib.bib2)]. Robust optimization modeling addresses the limitations of mean-variance optimization by formulating the problem based on the worst-case scenarios within the mean-variance optimization model [[3](https://arxiv.org/html/2510.15288v1#bib.bib3)]. Problem ([4](https://arxiv.org/html/2510.15288v1#S1.E4 "In 1 Introduction ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")) can be therefore reformulated using robust optimization as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max:(min𝝁∈Uμ⁡𝝁T​𝒙)−(max𝚺∈UΣ⁡12​γ​𝒙T​𝚺​𝐱)s.t.:𝒆T​𝒙=1,0≤xi≤1,i=1,…,n.\begin{array}[]{rcl}\max&:&\left(\min\limits\_{\boldsymbol{\mu}\in U\_{\mu}}{\mbox{$\mu$}}^{T}\mbox{$x$}\right)-\left(\max\limits\_{\boldsymbol{\Sigma}\in U\_{\Sigma}}\tfrac{1}{2}\gamma\,\mbox{$x$}^{T}\mbox{$\Sigma$}\mathbf{x}\right)\\ \text{s.t.}&:&\boldsymbol{e}^{T}\boldsymbol{x}=1,\\ &&0\leq x\_{i}\leq 1,\quad i=1,\ldots,n.\end{array} |  | (7) |

where, UμU\_{\mu} and UΣU\_{\Sigma} denote uncertainty sets of the mean vector and the covariance matrix.

Various forms of uncertainty sets have been proposed in the literature. In this study, the uncertainty set is defined in the form of intervals, as introduced by [[5](https://arxiv.org/html/2510.15288v1#bib.bib5)]:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Uμ\displaystyle U\_{\mu} | ={𝝁∈ℝn|μi0−βi≤μi≤μi0+βi,i=1,…,n,βi≥0},\displaystyle=\left\{\boldsymbol{\mu}\in\mathbb{R}^{n}\;\middle|\;\mu\_{i}^{0}-\beta\_{i}\leq\mu\_{i}\leq\mu\_{i}^{0}+\beta\_{i},\;i=1,\ldots,n,\;\beta\_{i}\geq 0\right\}, |  | (8) |
|  | UΣ\displaystyle U\_{\Sigma} | ={𝚺∈ℝn×n|σi​k0−δi​k≤σi​k≤σi​k0+δi​k,i,k=1,…,n,δi​k≥0}.\displaystyle=\left\{\boldsymbol{\Sigma}\in\mathbb{R}^{n\times n}\;\middle|\;\sigma\_{ik}^{0}-\delta\_{ik}\leq\sigma\_{ik}\leq\sigma\_{ik}^{0}+\delta\_{ik},\;i,k=1,\ldots,n,\;\delta\_{ik}\geq 0\right\}. |  |

These sets are constructed based on the interval bounds for the parameters:

|  |  |  |
| --- | --- | --- |
|  | μil≤μi≤μiuandσi​kl≤σi​k≤σi​ku\displaystyle\mu\_{i}^{l}\leq\mu\_{i}\leq\mu\_{i}^{u}\quad\text{and}\quad\sigma\_{ik}^{l}\leq\sigma\_{ik}\leq\sigma\_{ik}^{u} |  |

for i,k∈{1,2,⋯,n}i,k\in\{1,2,\cdots,n\}. Here, μil\mu^{l}\_{i} and μiu\mu^{u}\_{i} represent lower and upper bounds of the asset return means, while σi​kl\sigma^{l}\_{ik} and σi​ku\sigma^{u}\_{ik} denote lower and upper bounds of the asset return covariances. The notation used in ([8](https://arxiv.org/html/2510.15288v1#S2.E8 "In 2 Robust Optimization ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")), including μi0\mu\_{i}^{0}, σi​k0\sigma\_{ik}^{0}, βi\beta\_{i}, and δi​k\delta\_{ik}, is defined below:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μi0=μiu+μil2,βi=μiu−μil2,σi​k0=σiu+σil2,and​δi​k=σiu+σil2\displaystyle\mu\_{i}^{0}=\frac{\mu\_{i}^{u}+\mu\_{i}^{l}}{2},\ \beta\_{i}=\frac{\mu\_{i}^{u}-\mu\_{i}^{l}}{2},\ \sigma\_{ik}^{0}=\frac{\sigma\_{i}^{u}+\sigma\_{i}^{l}}{2},\ \text{and}\ \delta\_{ik}=\frac{\sigma\_{i}^{u}+\sigma\_{i}^{l}}{2} |  | (9) |

Thus, problem ([7](https://arxiv.org/html/2510.15288v1#S2.E7 "In 2 Robust Optimization ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | max:(𝝁𝟎)T​𝒙−𝜷T​𝒙−12​γ​𝒙T​𝚺𝟎​𝒙−12​γ​𝒙T​𝚫​𝒙s.t.:𝒆T​𝒙=1,0≤xi≤1,i=1,…,n\displaystyle\begin{array}[]{rcl}\max&:&(\boldsymbol{\mu^{0}})^{T}\boldsymbol{x}-\boldsymbol{\beta}^{T}\boldsymbol{x}-\frac{1}{2}\gamma\boldsymbol{x}^{T}\boldsymbol{\Sigma^{0}}\boldsymbol{x}-\frac{1}{2}\gamma\boldsymbol{x}^{T}\boldsymbol{\Delta}\boldsymbol{x}\\ \text{s.t.}&:&\boldsymbol{e}^{T}\boldsymbol{x}=1,\\ &&0\leq{x\_{i}}\leq 1,\quad i=1,\ldots,n\end{array} |  | (13) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝝁𝟎=(μ10,…,μn0)T,𝜷=(β1,…,βn)T,𝚺𝟎=[σ110⋯σ1​n0⋮⋱⋮σn​10⋯σn​n0],and​𝚫=[δ11⋯δ1​n⋮⋱⋮δn​1⋯δn​n].\boldsymbol{\mu^{0}}=(\mu^{0}\_{1},\ldots,\mu^{0}\_{n})^{T},\boldsymbol{\beta}=(\beta\_{1},\ldots,\beta\_{n})^{T},\boldsymbol{\Sigma^{0}}=\begin{bmatrix}\sigma^{0}\_{11}&\cdots&\sigma^{0}\_{1n}\\ \vdots&\ddots&\vdots\\ \sigma^{0}\_{n1}&\cdots&\sigma^{0}\_{nn}\end{bmatrix},\text{and}\ \boldsymbol{\Delta}=\begin{bmatrix}\delta\_{11}&\cdots&\delta\_{1n}\\ \vdots&\ddots&\vdots\\ \delta\_{n1}&\cdots&\delta\_{nn}\end{bmatrix}. |  |

As mentioned previously, we will derive the uncertainty sets using two different approaches: the moving-window and bootstrapping.

### 2.1 Moving-window Method

The moving-window is a method for generating an uncertainty set by selecting a specific-sized window (a sub-sample of the data) to calculate the mean vector and covariance matrix for each window. The algorithm for constructing the uncertainty set is presented below:

Input : Number of assets nn, number of time periods mm

Output : Uncertainty set for the mean vector and covariance matrix

1exStep 1: Let R∈ℝm×nR\in\mathbb{R}^{m\times n} be the return matrix of nn assets over mm periods.

Step 2: Choose a window size KK such that K<mK<m.

Step 3: For t=1t=1 to m−K+1m-K+1 do:

Extract the submatrix Rt=[rt,rt+1,…,rt+K−1]R\_{t}=[r\_{t},r\_{t+1},\ldots,r\_{t+K-1}].

Compute the mean vector 𝝁t\boldsymbol{\mu}\_{t} and covariance matrix 𝚺t\boldsymbol{\Sigma}\_{t} for RtR\_{t}.

Step 4: After all windows are processed:

For each asset ii:

* •

  Compute μiL=mint⁡μt,i\mu\_{i}^{L}=\min\_{t}\mu\_{t,i} and μiU=maxt⁡μt,i\mu\_{i}^{U}=\max\_{t}\mu\_{t,i}.

For each covariance element (i,k)(i,k):

* •

  Compute σi​kL=mint⁡σt,i​k\sigma\_{ik}^{L}=\min\_{t}\sigma\_{t,ik} and σi​kU=maxt⁡σt,i​k\sigma\_{ik}^{U}=\max\_{t}\sigma\_{t,ik}.

return *Uncertainty set: [μiL,μiU][\mu\_{i}^{L},\mu\_{i}^{U}] and [σi​kL,σi​kU][\sigma\_{ik}^{L},\sigma\_{ik}^{U}] for all i,ki,k*

Algorithm 1 Construction of the Uncertainty Set using the Moving-Window Method [[11](https://arxiv.org/html/2510.15288v1#bib.bib11)]

### 2.2 Bootstrapping Method

Unlike the moving-window method, the bootstrapping method utilizes random samples from the data population to generate an uncertainty set. This approach involves resampling the data, creating new samples from the existing dataset, and computing the mean vector and covariance matrix for each sample. The resulting uncertainty set is then used as the input for robust optimization model [[1](https://arxiv.org/html/2510.15288v1#bib.bib1)]. The algorithm for constructing the uncertainty set using bootstrapping is presented below. In this algorithm, α\alpha is a confidence level where [[11](https://arxiv.org/html/2510.15288v1#bib.bib11)] typically sets α=0.05\alpha=0.05; and Nb​o​o​tN\_{boot} is the number of bootstrap replications, which is usually chosen to be a large number.

Input : Number of assets nn, number of time periods mm, significance level α\alpha

Output : Uncertainty set for mean vector 𝝁\boldsymbol{\mu} and covariance matrix 𝚺\boldsymbol{\Sigma}

1exStep 1: Let R∈ℝm×nR\in\mathbb{R}^{m\times n} be the return matrix of nn assets over mm periods.

Step 2: Set block length L=⌊m1/3⌋L=\lfloor m^{1/3}\rfloor.

Step 3: Compute the number of blocks as B=⌊m/L⌋B=\lfloor m/L\rfloor.

Step 4: for *i=1i=1 to N*boot*N\_{\text{boot}}* do

for *j=1j=1 to BB* do

Randomly resample LL returns with replacement from RR to form block Ri​jR\_{ij}.

Concatenate the BB blocks to form bootstrap sample R(i)R^{(i)}.

Compute sample mean μ(i)\mu^{(i)} and covariance matrix Σ(i)\Sigma^{(i)} from R(i)R^{(i)}.

Step 5: For each asset kk, define the uncertainty bounds as:

* •

  μkl=percentileα/2​(μk(1),…,μk(Nboot))\mu\_{k}^{l}=\text{percentile}\_{\alpha/2}\left(\mu\_{k}^{(1)},\ldots,\mu\_{k}^{(N\_{\text{boot}})}\right)
* •

  μku=percentile1−α/2​(μk(1),…,μk(Nboot))\mu\_{k}^{u}=\text{percentile}\_{1-\alpha/2}\left(\mu\_{k}^{(1)},\ldots,\mu\_{k}^{(N\_{\text{boot}})}\right)

Step 6: For each covariance entry (p,q)(p,q), define:

* •

  σp​ql=percentileα/2​(σp​q(1),…,σp​q(Nboot))\sigma\_{pq}^{l}=\text{percentile}\_{\alpha/2}\left(\sigma\_{pq}^{(1)},\ldots,\sigma\_{pq}^{(N\_{\text{boot}})}\right)
* •

  σp​qu=percentile1−α/2​(σp​q(1),…,σp​q(Nboot))\sigma\_{pq}^{u}=\text{percentile}\_{1-\alpha/2}\left(\sigma\_{pq}^{(1)},\ldots,\sigma\_{pq}^{(N\_{\text{boot}})}\right)

return *Uncertainty set: [μkl,μku][\mu\_{k}^{l},\mu\_{k}^{u}] and [σp​ql,σp​qu][\sigma\_{pq}^{l},\sigma\_{pq}^{u}] for all k,p,qk,p,q*

Algorithm 2 Construction of Uncertainty Set using Bootstrapping

## 3 Numerical Results

We conducted numerical simulations of the robust optimization problem ([13](https://arxiv.org/html/2510.15288v1#S2.E13 "In 2 Robust Optimization ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")). The method was implemented using Matlab R2021b with the CPLEX 12.10.0 setting and executed on a Windows 10 PC. The data set, taken from the Yahoo Finance, consists of the daily closing stock of 45 banking companies in Indonesia during the period from March 25, 2022, to March 24, 2023, which spans 247 consecutive trading days. The stock codes of the banks used in this study are listed in Table [1](https://arxiv.org/html/2510.15288v1#S3.T1 "Table 1 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization").

Using the data, we first generated important parameters in portfolio optimization, return asset vector (𝝁\mu) and variance-covariance matrix (𝚺\Sigma), using equation ([5](https://arxiv.org/html/2510.15288v1#S1.E5 "In 1 Introduction ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")) and ([6](https://arxiv.org/html/2510.15288v1#S1.E6 "In 1 Introduction ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")), respectively, as in ([14](https://arxiv.org/html/2510.15288v1#S3.E14 "In 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")) and ([15](https://arxiv.org/html/2510.15288v1#S3.E15 "In 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")). These two parameters are then used to construct the intervals that capture the uncertainty by applying moving-window and bootstrapping methods, following Algorithms [1](https://arxiv.org/html/2510.15288v1#algorithm1 "In 2.1 Moving-window Method ‣ 2 Robust Optimization ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization") and [2](https://arxiv.org/html/2510.15288v1#algorithm2 "In 2.2 Bootstrapping Method ‣ 2 Robust Optimization ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization"), respectively.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝁T=[−0.00439−0.00179−0.00055⋯0.003060.000260.00023]\mbox{$\mu$}^{T}=\begin{bmatrix}-0.00439&-0.00179&-0.00055&\cdots&0.00306&0.00026&0.00023\end{bmatrix} |  | (14) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺=[0.001370.000260.00005⋯0.000310.000210.000040.000260.000480.00006⋯0.000120.000150.000020.000050.000060.00097⋯0.00007−0.000040.00002⋮⋮⋮⋱⋮⋮⋮0.000310.000120.00007⋯0.001820.000810.000030.000210.00015−0.00004⋯0.000810.001240.000010.000040.000020.00002⋯0.000030.000010.00011]\mbox{$\Sigma$}=\begin{bmatrix}0.00137&0.00026&0.00005&\cdots&0.00031&0.00021&0.00004\\ 0.00026&0.00048&0.00006&\cdots&0.00012&0.00015&0.00002\\ 0.00005&0.00006&0.00097&\cdots&0.00007&-0.00004&0.00002\\ \vdots&\vdots&\vdots&\ddots&\vdots&\vdots&\vdots\\ 0.00031&0.00012&0.00007&\cdots&0.00182&0.00081&0.00003\\ 0.00021&0.00015&-0.00004&\cdots&0.00081&0.00124&0.00001\\ 0.00004&0.00002&0.00002&\cdots&0.00003&0.00001&0.00011\\ \end{bmatrix} |  | (15) |

Table 1: Stock codes of 45 Indonesian banking companies used in the dataset

| ii | Asset Code | ii | Asset Code | ii | Asset Code | ii | Asset Code | ii | Asset Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AGRO | 10 | BBKP | 19 | BGTG | 28 | BNII | 37 | MASB |
| 2 | AGRS | 11 | BBMD | 20 | BINA | 29 | BNLI | 38 | MAYA |
| 3 | AMAR | 12 | BBNI | 21 | BJBR | 30 | BRIS | 39 | MCOR |
| 4 | ARTO | 13 | BBRI | 22 | BJTM | 31 | BSIM | 40 | MEGA |
| 5 | BABP | 14 | BBSI | 23 | BKSW | 32 | BTPN | 41 | NISP |
| 6 | BACA | 15 | BBTN | 24 | BMAS | 33 | BTPS | 42 | NOBU |
| 7 | BANK | 16 | BBYB | 25 | BMRI | 34 | BVIC | 43 | PNBN |
| 8 | BBCA | 17 | BCIC | 26 | BNBA | 35 | DNAR | 44 | PNBS |
| 9 | BBHI | 18 | BDMN | 27 | BNGA | 36 | INPC | 45 | SDRA |

In the moving-window method, the uncertainty set is constructed by selecting a data sub-sample of fixed size. In this research, a window length of 90 days (K=90K=90) is used, corresponding to quarterly financial reporting periods (February, May, August, and November), which are considered appropriate times for stock trading. With the chosen window length of K=90K=90, the procedure requires 158 iterations to obtain the corresponding intervals.

Unlike the moving-window method, the length of bootstrap block LL is determined based on the sample size mm. For 247 consecutive trading days, we have m=247m=247, and based on Step 2 in Algorithm [2](https://arxiv.org/html/2510.15288v1#algorithm2 "In 2.2 Bootstrapping Method ‣ 2 Robust Optimization ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization"),

|  |  |  |
| --- | --- | --- |
|  | L=2471/3=6.2743.L=247^{1/3}=6.2743. |  |

Using this block length, the number of blocks required to form one bootstrap resample is

|  |  |  |
| --- | --- | --- |
|  | mL=2476.2743≈40.\frac{m}{L}=\frac{247}{6.2743}\approx 40. |  |

Then, both parameters LL and mL\frac{m}{L} are used to construct the intervals in the bootstrap method. In addition, we set Nb​o​o​t=1000N\_{boot}=1000 and α=0.05\alpha=0.05.

The lower and upper bounds from the generated interval for the mean return vectors are presented in Table [2](https://arxiv.org/html/2510.15288v1#S3.T2 "Table 2 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization"). The first column of the table indicates the method used, while the remaining columns show the lower bound μil\mu\_{i}^{l} and the upper bound μiu\mu\_{i}^{u} for each asset code.

Table 2: Lower and Upper Bounds of the Mean Return from Two Methods.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | Bounds | AGRO | AGRS | AMAR | ⋯\cdots | PNBN | PNBS | SDRA |
| Moving-window | (μil)M​W(\mu\_{i}^{l})\_{MW} | -0.00669 | -0.00400 | -0.00501 | ⋯\cdots | -0.00684 | -0.00412 | -0.00073 |
| (μiu)M​W(\mu\_{i}^{u})\_{MW} | -0.00024 | 0.00065 | 0.00292 | ⋯\cdots | 0.01344 | 0.00521 | 0.00102 |
| Bootstrapping | (μil)B(\mu\_{i}^{l})\_{B} | -0.01519 | -0.00852 | -0.00948 | ⋯\cdots | -0.00927 | -0.00965 | -0.00277 |
| (μiu)B(\mu\_{i}^{u})\_{B} | 0.00793 | 0.00579 | 0.00957 | ⋯\cdots | 0.01699 | 0.01156 | 0.00377 |

In order to get the parameters for Robust Optimization, the lower and upper bounds from the moving-window method in Table [2](https://arxiv.org/html/2510.15288v1#S3.T2 "Table 2 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization") is used to compute the vector 𝝁𝟎\boldsymbol{\mu^{0}} and 𝜷\boldsymbol{\beta} using the formula μi0=μiu+μil2\mu\_{i}^{0}=\frac{\mu\_{i}^{u}+\mu\_{i}^{l}}{2} and β=μiu−μil2\beta=\frac{\mu\_{i}^{u}-\mu\_{i}^{l}}{2} so that

|  |  |  |
| --- | --- | --- |
|  | 𝝁M​W0=(−0.00346;…;0.00014)T​and​𝜷M​W=(0.00323;…;0.00087)T.\boldsymbol{\mu}\_{MW}^{0}=(-0.00346;\ldots;0.00014)^{T}\ \text{and}\ \boldsymbol{\beta}\_{MW}=(0.00323;\ldots;0.00087)^{T}. |  |

This is also done to the lower and upper bounds from the bootstrapping method:

|  |  |  |
| --- | --- | --- |
|  | 𝝁B0=(−0.00386;…;0.00014)T​and​𝜷B=(0.01200;…;0.00087)T.\displaystyle\boldsymbol{\mu}\_{B}^{0}=(-0.00386;\ldots;0.00014)^{T}\ \text{and}\ \boldsymbol{\beta}\_{B}=(0.01200;\ldots;0.00087)^{T}. |  |

All bounds are then used to compute the matrices 𝚺𝟎\boldsymbol{\Sigma^{0}} and 𝚫\boldsymbol{\Delta} using equation (6), based on the values presented in Tables [3](https://arxiv.org/html/2510.15288v1#S3.T3 "Table 3 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization") and [4](https://arxiv.org/html/2510.15288v1#S3.T4 "Table 4 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization"), resulting in the following matrices:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺M​W0=[0.00160…0.00004⋮⋱⋮0.00004…0.00010]​and​𝚫M​W=[0.00051…0.00006⋮⋱⋮0.00006…0.00004].\displaystyle\boldsymbol{\Sigma}\_{MW}^{0}=\begin{bmatrix}0.00160&\ldots&0.00004\\ \vdots&\ddots&\vdots\\ 0.00004&\ldots&0.00010\end{bmatrix}\text{and}\ \boldsymbol{\Delta}\_{MW}=\begin{bmatrix}0.00051&\ldots&0.00006\\ \vdots&\ddots&\vdots\\ 0.00006&\ldots&0.00004\end{bmatrix}. |  | (16) |

Similarly, from the bootstrapping method, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺B0=[0.00190…0.00003⋮⋱⋮0.00003…0.00013]​and​𝚫B=[0.00148…0.00012⋮⋱⋮0.00012…0.00007].\boldsymbol{\Sigma}\_{B}^{0}=\begin{bmatrix}0.00190&\ldots&0.00003\\ \vdots&\ddots&\vdots\\ 0.00003&\ldots&0.00013\end{bmatrix}\text{and}\ \boldsymbol{\Delta}\_{B}=\begin{bmatrix}0.00148&\ldots&0.00012\\ \vdots&\ddots&\vdots\\ 0.00012&\ldots&0.00007\end{bmatrix}. |  | (17) |

Table 3: Lower and Upper Bounds of Return Covariance from moving-window Method.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Bounds | AGRO | AGRS | AMAR | ⋯\boldsymbol{\cdots} | PNBN | PNBS | SDRA |
| AGRO | σi​kl{\sigma\_{ik}^{l}} | 0.00109 | 0.00009 | -0.00002 | ⋯\cdots | 0.00007 | 0.00004 | -0.00002 |
| σi​ku{\sigma\_{ik}^{u}} | 0.00211 | 0.00037 | 0.00012 | ⋯\cdots | 0.00049 | 0.00030 | 0.00010 |
| AGRS | σi​kl{\sigma\_{ik}^{l}} | 0.00009 | 0.00027 | -0.00001 | ⋯\cdots | 0.00005 | -0.00006 | -0.00003 |
| σi​ku{\sigma\_{ik}^{u}} | 0.00037 | 0.00072 | 0.00015 | ⋯\cdots | 0.00018 | 0.00027 | 0.00007 |
| AMAR | σi​kl{\sigma\_{ik}^{l}} | -0.00002 | -0.00001 | 0.00065 | ⋯\cdots | -0.00013 | -0.00044 | -0.00004 |
| σi​ku{\sigma\_{ik}^{u}} | 0.00012 | 0.00015 | 0.00120 | ⋯\cdots | 0.00026 | 0.00030 | 0.00005 |
| ⋮\boldsymbol{\vdots} | ⋮\boldsymbol{\vdots} | ⋮\boldsymbol{\vdots} | ⋮\boldsymbol{\vdots} | ⋮\boldsymbol{\vdots} | ⋱\boldsymbol{\ddots} | ⋮\boldsymbol{\vdots} | ⋮\boldsymbol{\vdots} | ⋮\boldsymbol{\vdots} |
| PNBN | σi​kl{\sigma\_{ik}^{l}} | 0.00007 | 0.00005 | -0.00013 | ⋯\cdots | 0.00100 | 0.00033 | -0.00008 |
| σi​ku{\sigma\_{ik}^{u}} | 0.00049 | 0.00018 | 0.00026 | ⋯\cdots | 0.00292 | 0.00137 | 0.00007 |
| PNBS | σi​kl{\sigma\_{ik}^{l}} | 0.00004 | -0.00006 | -0.00044 | ⋯\cdots | 0.00033 | 0.00045 | -0.00008 |
| σi​ku{\sigma\_{ik}^{u}} | 0.00030 | 0.00027 | 0.00030 | ⋯\cdots | 0.00137 | 0.00223 | 0.00006 |
| SDRA | σi​kl{\sigma\_{ik}^{l}} | -0.00002 | -0.00003 | -0.00004 | ⋯\cdots | -0.00008 | -0.00008 | 0.00006 |
| σi​ku{\sigma\_{ik}^{u}} | 0.00010 | 0.00007 | 0.00005 | ⋯\cdots | 0.00007 | 0.00006 | 0.00014 |




Table 4: Lower and Upper Bounds of Return Covariance from Bootstrapping Method.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Bounds | AGRO | AGRS | AMAR | ⋯\boldsymbol{\cdots} | PNBN | PNBS | SDRA |
| AGRO | σi​kl\sigma\_{ik}^{l} | 0.00054 | 0.00004 | -0.00028 | ⋯\cdots | -0.00017 | -0.00017 | -0.00010 |
| σi​ku\sigma\_{ik}^{u} | 0.00351 | 0.00059 | 0.00038 | ⋯\cdots | 0.00081 | 0.00058 | 0.00014 |
| AGRS | σi​kl\sigma\_{ik}^{l} | 0.00004 | 0.00023 | -0.00014 | ⋯\cdots | -0.00017 | -0.00011 | -0.00005 |
| σi​ku\sigma\_{ik}^{u} | 0.00059 | 0.00079 | 0.00026 | ⋯\cdots | 0.00044 | 0.00056 | 0.00010 |
| AMAR | σi​kl\sigma\_{ik}^{l} | -0.00028 | -0.00014 | 0.00050 | ⋯\cdots | -0.00030 | -0.00062 | -0.00010 |
| σi​ku\sigma\_{ik}^{u} | 0.00038 | 0.00026 | 0.00159 | ⋯\cdots | 0.00049 | 0.00035 | 0.00012 |
| ⋮\boldsymbol{\vdots} | ⋮\vdots | ⋮\vdots | ⋮\vdots | ⋮\vdots | ⋱\ddots | ⋮\vdots | ⋮\vdots | ⋮\vdots |
| PNBN | σi​kl\sigma\_{ik}^{l} | -0.00017 | -0.00017 | -0.00030 | ⋯\cdots | 0.00074 | 0.00023 | -0.00014 |
| σi​ku\sigma\_{ik}^{u} | 0.00081 | 0.00044 | 0.00049 | ⋯\cdots | 0.00344 | 0.00176 | 0.00018 |
| PNBS | σi​kl\sigma\_{ik}^{l} | -0.00017 | -0.00011 | -0.00062 | ⋯\cdots | 0.00023 | 0.00050 | -0.00016 |
| σi​ku\sigma\_{ik}^{u} | 0.00058 | 0.00056 | 0.00035 | ⋯\cdots | 0.00176 | 0.00316 | 0.00012 |
| SDRA | σi​kl\sigma\_{ik}^{l} | -0.00010 | -0.00005 | -0.00010 | ⋯\cdots | -0.00014 | -0.00016 | 0.00006 |
| σi​ku\sigma\_{ik}^{u} | 0.00014 | 0.00010 | 0.00012 | ⋯\cdots | 0.00018 | 0.00012 | 0.00019 |

Once the values of 𝝁0\boldsymbol{\mu}^{0}, 𝜷\boldsymbol{\beta}, 𝚺0\boldsymbol{\Sigma}^{0} and 𝚫\boldsymbol{\Delta} are obtained, they are substituted into ([13](https://arxiv.org/html/2510.15288v1#S2.E13 "In 2 Robust Optimization ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization")) to derive the robust optimization solution, yielding results such as selected assets, asset proportions, and the objective function value.

Table 5: Allocation of Chosen Asset’s Proportion and Objective Function Value.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Proportion | Moving Window | | | Bootstrapping | | |
| 𝜸=𝟓\boldsymbol{\gamma=5} | 𝜸=𝟓𝟎\boldsymbol{\gamma=50} | 𝜸=𝟏𝟎𝟎\boldsymbol{\gamma=100} | 𝜸=𝟓\boldsymbol{\gamma=5} | 𝜸=𝟓𝟎\boldsymbol{\gamma=50} | 𝜸=𝟏𝟎𝟎\boldsymbol{\gamma=100} |
| BBCA | 0.07923 | 0.04409 | 0.01827 | 0 | 0 | 0 |
| BBMD | 0 | 0.04584 | 0.05815 | 0 | 0 | 0.00994 |
| BBNI | 0 | 0 | 0 | 0 | 0 | 0 |
| BDMN | 0 | 0 | 0 | 0 | 0 | 0 |
| BINA | 0.10324 | 0.03235 | 0.02277 | 0 | 0 | 0 |
| BJBR | 0 | 0.10305 | 0.11073 | 0 | 0.13762 | 0.1508 |
| BJTM | 0 | 0.19754 | 0.24193 | 0.44471 | 0.4168 | 0.38734 |
| BMAS | 0 | 0 | 0 | 0 | 0 | 0 |
| BMRI | 0.08743 | 0 | 0 | 0 | 0 | 0 |
| BNGA | 0.52335 | 0.14778 | 0.1045 | 0 | 0.03982 | 0.03897 |
| BNII | 0 | 0 | 0.01915 | 0 | 0 | 0.02309 |
| BNLI | 0 | 0 | 0.01231 | 0 | 0 | 0.0038 |
| BRIS | 0 | 0 | 0 | 0 | 0 | 0 |
| BSIM | 0 | 0.03671 | 0.03587 | 0 | 0.00971 | 0.01612 |
| BTPN | 0 | 0.00123 | 0.02361 | 0 | 0.04952 | 0.05379 |
| MASB | 0 | 0.06208 | 0.05241 | 0 | 0 | 0.00391 |
| MEGA | 0 | 0 | 0.00459 | 0 | 0 | 0 |
| NISP | 0.00482 | 0.07177 | 0.06518 | 0.02681 | 0.08367 | 0.07791 |
| PNBN | 0 | 0 | 0 | 0 | 0 | 0 |
| PNBS | 0 | 0 | 0 | 0 | 0 | 0 |
| SDRA | 0.20192 | 0.25755 | 0.24126 | 0.52848 | 0.26286 | 0.23433 |
| fv​a​lf\_{val} | 0.00076 | 0.00221 | 0.00286 | 0.00313 | 0.00499 | 0.00694 |

Table [5](https://arxiv.org/html/2510.15288v1#S3.T5 "Table 5 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization") shows the results of selecting different values of γ\gamma. The first column lists the assets, the second to fourth columns present the asset allocations obtained using uncertainty sets generated from the moving-window method, while the remaining columns present the allocations derived from the bootstrapping method.

In this research, three levels of the risk aversion coefficient were considered, namely γ={5,50,\gamma=\{5,50, and 100}100\}. These values were selected to represent different degrees of risk preference, ranging from relatively low to high, and to observe how the robust optimization model responds to variations in risk aversion. Although these values are not standard benchmarks, they provide representative cases for exploratory analysis. A broader sensitivity analysis with additional γ\gamma values is left for future research.

It can be observed from the table that different values of γ\gamma lead to different asset selections in constructing the portfolio. For instance, the moving-window method produces an optimal allocation of 7.92% in stock BBCA, 10.32% in stock BINA, 8.74% in stock BMRI, 52.34% in stock BNGA, 0.48% in stock NISP, and 20.19% in stock SDRA. In contrast, the bootstrapping method yields a different set of selected assets, with optimal allocations of 44.47% in stock BJTM, 2.68% in stock NISP, and 52.85% in stock SDRA. Furthermore, the objective value (fv​a​l)(f\_{val}), which reflects the risk–return trade-off, is lower under the moving-window method compared to the bootstrapping method, indicating a more favorable balance between risk and return.

Moreover, the objective function values confirm that, across different methods and risk aversion coefficients γ\gamma, robust optimization with uncertainty sets derived from the moving-window method consistently produces better results than those derived from the bootstrapping method, as shown by its smaller objective values. This can be explained by the fact that, although both methods use the same historical data, the moving-window method relies only on the most recent subset of data, making the resulting uncertainty sets more reflective of current market conditions, whereas the bootstrapping method resamples from the entire dataset and thus captures a wider range of variability, including past periods that may no longer represent the present market situation. Consequently, the moving-window method often yields narrower and more relevant uncertainty sets, while the bootstrapping method produces more conservative allocations. As explained earlier, we used 90-day window length (K=90K=90), corresponding to quarterly financial reporting periods (February, May, August, and November). This choice provides a reasonable balance between capturing recent market dynamics and avoiding overfitting to very short-term fluctuations. To further illustrate the practical implications of these optimization results, we present an investment scenario.

Suppose an investor intends to invest Rp. 100,000.00 (Indonesian Rupiah) on 24 March 2023. The optimal stock proportions obtained from Table [6](https://arxiv.org/html/2510.15288v1#S3.T6 "Table 6 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization") are multiplied by the investment capital of Rp. 100,000.00 to obtain the stock price allocation. Subsequently, the number of shares is obtained by dividing the allocated amount by the closing price on 24 March 2023. Tables [6](https://arxiv.org/html/2510.15288v1#S3.T6 "Table 6 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization") and [7](https://arxiv.org/html/2510.15288v1#S3.T7 "Table 7 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization") present the resulting investment allocation from the moving-window and bootstrapping methods, respectively.

Table 6: Fund Allocation for Portfolio from Robust Optimization with moving-window.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Asset | |  | | --- | | Price | | (24/3/2023) | | moving-window | | | | | |
| 𝜸=𝟓\boldsymbol{\gamma=5} | | 𝜸=𝟓𝟎\boldsymbol{\gamma=50} | | 𝜸=𝟏𝟎𝟎\boldsymbol{\gamma=100} | |
| Alokasi | Lembar | Alokasi | Lembar | Alokasi | Lembar |
| BBCA | 8825 | Rp7,923.00 | 1 | Rp4,409.00 | 0 | Rp1,827.00 | 0 |
| BBMD | 1960 | Rp0.00 | 0 | Rp4,584.00 | 2 | Rp5,815.00 | 3 |
| BBNI | 9625 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| BDMN | 2830 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| BINA | 3990 | Rp10,324.00 | 3 | Rp3,235.00 | 1 | Rp2,277.00 | 1 |
| BJBR | 1335 | Rp0.00 | 0 | Rp10,305.00 | 8 | Rp11,073.00 | 8 |
| BJTM | 735 | Rp0.00 | 0 | Rp19,754.00 | 27 | Rp24,193.00 | 33 |
| BMAS | 1395 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| BMRI | 5450 | Rp8,743.00 | 2 | Rp0.00 | 0 | Rp0.00 | 0 |
| BNGA | 1225 | Rp52,335.00 | 43 | Rp14,778.00 | 12 | Rp10,450.00 | 9 |
| BNII | 226 | Rp0.00 | 0 | Rp0.00 | 0 | Rp1,915.00 | 8 |
| BNLI | 930 | Rp0.00 | 0 | Rp0.00 | 0 | Rp1,231.00 | 1 |
| BRIS | 1610 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| BSIM | 890 | Rp0.00 | 0 | Rp3,671.00 | 4 | Rp3,587.00 | 4 |
| BTPN | 2490 | Rp0.00 | 0 | Rp123.00 | 0 | Rp2,361.00 | 1 |
| MASB | 3420 | Rp0.00 | 0 | Rp6,208.00 | 2 | Rp5,241.00 | 2 |
| MEGA | 5075 | Rp0.00 | 0 | Rp0.00 | 0 | Rp459.00 | 0 |
| NISP | 755 | Rp482.00 | 1 | Rp7,177.00 | 10 | Rp6,518.00 | 9 |
| PNBN | 1415 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| PNBS | 58 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| SDRA | 585 | Rp20,192.00 | 35 | Rp25,755.00 | 44 | Rp23,054.00 | 39 |




Table 7: Fund Allocation for Portfolio from Robust Optimization with Bootstrapping.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Asset | |  | | --- | | Price | | (24/3/2023) | | Bootstrapping | | | | | |
| 𝜸=𝟓\boldsymbol{\gamma=5} | | 𝜸=𝟓𝟎\boldsymbol{\gamma=50} | | 𝜸=𝟏𝟎𝟎\boldsymbol{\gamma=100} | |
| Alokasi | Lembar | Alokasi | Lembar | Alokasi | Lembar |
| BBCA | 8825 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| BBMD | 1960 | Rp0.00 | 0 | Rp0.00 | 0 | Rp994.00 | 1 |
| BBNI | 9625 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| BDMN | 2830 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| BINA | 3990 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| BJBR | 1335 | Rp0.00 | 0 | Rp13,762.00 | 10 | Rp15,080.00 | 11 |
| BJTM | 735 | Rp44,471.00 | 61 | Rp41,680.00 | 57 | Rp38,734.00 | 53 |
| BMAS | 1395 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| BMRI | 5450 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| BNGA | 1225 | Rp0.00 | 0 | Rp3,982.00 | 3 | Rp3,897.00 | 3 |
| BNII | 226 | Rp0.00 | 0 | Rp0.00 | 0 | Rp2,309.00 | 10 |
| BNLI | 930 | Rp0.00 | 0 | Rp0.00 | 0 | Rp380.00 | 0 |
| BRIS | 1610 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| BSIM | 890 | Rp0.00 | 0 | Rp971.00 | 1 | Rp1,612.00 | 2 |
| BTPN | 2490 | Rp0.00 | 0 | Rp4,952.00 | 2 | Rp5,379.00 | 2 |
| MASB | 3420 | Rp0.00 | 0 | Rp0.00 | 0 | Rp391.00 | 0 |
| MEGA | 5075 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| NISP | 755 | Rp2,681.00 | 4 | Rp8,367.00 | 11 | Rp7,791.00 | 10 |
| PNBN | 1415 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| PNBS | 58 | Rp0.00 | 0 | Rp0.00 | 0 | Rp0.00 | 0 |
| SDRA | 585 | Rp52,848.00 | 90 | Rp26,286.00 | 45 | Rp23,433.00 | 40 |

The performance measure used to evaluate portfolio outcome is capital gain, which refers to the positive difference or profit obtained when selling an asset at a price higher than the purchase price. Conversely, a capital loss occurs when the asset is sold at a lower price [[6](https://arxiv.org/html/2510.15288v1#bib.bib6)]. Thus, profit or loss is calculated by subtracting the purchase price from the selling price and multiplying it by the number of shares. Table [8](https://arxiv.org/html/2510.15288v1#S3.T8 "Table 8 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization") presents the profit or loss obtained under favorable stock market conditions for each optimization method. For instance, if an investor wants to invest on 30 March 2023 in a good market condition, the moving-window method yields profits of Rp. 11,715.00 for γ=5\gamma=5, Rp. 1,030.00 for γ=50\gamma=50, and Rp. 892.00 for γ=100\gamma=100. Similarly, the bootstrapping method yields profits of Rp. 60.00 for γ=5\gamma=5, Rp. 625.00 for γ=50\gamma=50, and Rp. 685.00 for γ=100\gamma=100.

Table 8: Capital Gain (Loss) on Good Market Condition.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Asset | |  | | --- | | Price | | (30/3/2023) | | Moving Window | | | Bootstrapping | | |
| 𝜸=𝟓\boldsymbol{\gamma=5} | 𝜸=𝟓𝟎\boldsymbol{\gamma=50} | 𝜸=𝟏𝟎𝟎\boldsymbol{\gamma=100} | 𝜸=𝟓\boldsymbol{\gamma=5} | 𝜸=𝟓𝟎\boldsymbol{\gamma=50} | 𝜸=𝟏𝟎𝟎\boldsymbol{\gamma=100} |
| BBCA | 8825 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BBMD | 1960 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BBNI | 9350 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BDMN | 2890 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BINA | 3990 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BJBR | 1370 | Rp0.00 | Rp280.00 | Rp280.00 | Rp0.00 | Rp350.00 | Rp385.00 |
| BJTM | 735 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BMAS | 1415 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BMRI | 10225 | Rp9,550.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BNGA | 1275 | Rp2,150.00 | Rp600.00 | Rp450.00 | Rp0.00 | Rp150.00 | Rp150.00 |
| BNII | 230 | Rp0.00 | Rp0.00 | Rp32.00 | Rp0.00 | Rp0.00 | Rp40.00 |
| BNLI | 945 | Rp0.00 | Rp0.00 | Rp15.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BRIS | 1640 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BSIM | 890 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BTPN | 2470 | Rp0.00 | Rp0.00 | -Rp20.00 | Rp0.00 | -Rp40.00 | -Rp40.00 |
| MASB | 3420 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| MEGA | 5125 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| NISP | 770 | Rp15.00 | Rp150.00 | Rp135.00 | Rp60.00 | Rp165.00 | Rp150.00 |
| PNBN | 1385 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| PNBS | 60 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| SDRA | 590 | Rp175.00 | Rp220.00 | Rp195.00 | Rp450.00 | Rp225.00 | Rp200.00 |
| Total | | Rp11,715.00 | Rp1,030.00 | Rp892.00 | Rp60.00 | Rp625.00 | Rp685.00 |

Now, we present a different case in which the profit or loss is obtained under poor market conditions, as shown in Table [9](https://arxiv.org/html/2510.15288v1#S3.T9 "Table 9 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization"). The moving-window method yields profits of Rp. 735.00 for γ=5\gamma=5, losses of Rp. 2,040.00 for γ=50\gamma=50, and losses of Rp. 2,629.00 for γ=100\gamma=100. On the other hand, the bootstrapping method results in losses across all cases Rp. 3,830.00 for γ=5\gamma=5, Rp. 3,870.00 for γ=20\gamma=20, and Rp. 3,830.00 for γ=100\gamma=100.

Table 9: Capital Gain (Loss) on Bad Market Condition.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Asset | |  | | --- | | Proice | | (2/5/2023) | | Moving Window | | | Bootstrapping | | |
| 𝜸=𝟓\boldsymbol{\gamma=5} | 𝜸=𝟓𝟎\boldsymbol{\gamma=50} | 𝜸=𝟏𝟎𝟎\boldsymbol{\gamma=100} | 𝜸=𝟓\boldsymbol{\gamma=5} | 𝜸=𝟓𝟎\boldsymbol{\gamma=50} | 𝜸=𝟏𝟎𝟎\boldsymbol{\gamma=100} |
| BBCA | 9050 | Rp225.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BBMD | 1925 | Rp0.00 | -Rp70.00 | -Rp105.00 | Rp0.00 | Rp0.00 | -Rp35.00 |
| BBNI | 9550 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BDMN | 2770 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BINA | 3970 | -Rp60.00 | -Rp20.00 | -Rp20.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BJBR | 1220 | Rp0.00 | -Rp920.00 | -Rp920.00 | Rp0.00 | -Rp1,150.00 | -Rp1,265.00 |
| BJTM | 665 | Rp0.00 | -Rp1,890.00 | -Rp2,310.00 | -Rp4,270.00 | -Rp3,990.00 | -Rp3,710.00 |
| BMAS | 1235 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BMRI | 5250 | -Rp400.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BNGA | 1245 | Rp860.00 | Rp240.00 | Rp180.00 | Rp0.00 | Rp60.00 | Rp60.00 |
| BNII | 228 | Rp0.00 | Rp0.00 | Rp16.00 | Rp0.00 | Rp0.00 | Rp20.00 |
| BNLI | 950 | Rp0.00 | Rp0.00 | Rp20.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BRIS | 1685 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BSIM | 890 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| BTPN | 2490 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| MASB | 3180 | Rp0.00 | -Rp480.00 | -Rp480.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| MEGA | 4980 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| NISP | 865 | Rp110.00 | Rp1,100.00 | Rp990.00 | Rp440.00 | Rp1,210.00 | Rp1,100.00 |
| PNBN | 1040 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| PNBS | 58 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 | Rp0.00 |
| SDRA | 560 | -Rp875.00 | -Rp1,100.00 | -Rp975.00 | -Rp2,250.00 | -Rp1,125.00 | -Rp1,000.00 |
| Total | | Rp735.00 | -Rp2,040.00 | -Rp2,629.00 | -Rp3,830.00 | -Rp3,870.00 | -Rp3,830.00 |

Based on these two market conditions and the three values of risk aversion, it can be observed that the portfolio generated by robust optimization using the moving-window method yields profits in both good and bad market conditions, particularly when γ=5\gamma=5.. This indicates that robust optimization with the moving-window method produces a resilient portfolio across different market scenarios, especially for risk-taking investors.

When assessing stock market performance under both good and poor market conditions, price movements from 27 March 2023 to 15 June 2023 suggest that the market can be classified as in good condition if the overall increase in stock prices is significant. However, identifying market conditions solely from short-term price fluctuations remains challenging.

A comparison of portfolio returns is conducted for the 19 selected stocks in Table [5](https://arxiv.org/html/2510.15288v1#S3.T5 "Table 5 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization"), which are expected to be chosen by investors using the three optimization methods. The portfolio return dynamics over the period from 27 March 2023 to 15 June 2023 are shown in Figure [1](https://arxiv.org/html/2510.15288v1#S3.F1 "Figure 1 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization"), Figure [2](https://arxiv.org/html/2510.15288v1#S3.F2 "Figure 2 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization"), and Figure [3](https://arxiv.org/html/2510.15288v1#S3.F3 "Figure 3 ‣ 3 Numerical Results ‣ Portfolio Optimization of Indonesian Banking Stocks Using Robust Optimization"). For γ=5\gamma=5, robust optimization with the moving-window method produced higher profits, as its return curve is consistently positioned above those of the other optimization methods. For higher values of γ\gamma, namely 50 and 100, the results show that mean-variance optimization yielded greater profits, with its return curve predominantly above the others. This demonstrates that for lower γ\gamma values—corresponding to more risk-taking investors—robust optimization with the moving-window method is preferable to achieve higher profits. Conversely, for risk-averse investors (higher γ\gamma values), mean-variance optimization is more suitable, as it provides higher profits.

![Refer to caption](foto/gamma5.png)


Figure 1: Portfolio Return from 27 March 2023 to 15 June 2023 for γ=5\gamma=5.

![Refer to caption](foto/gamma50.png)


Figure 2: Portfolio Return from 27 March 2023 to 15 June 2023 for γ=50\gamma=50.

![Refer to caption](foto/gamma100.png)


Figure 3: Portfolio Return from 27 March 2023 to 15 June 2023 for γ=100\gamma=100.

## 4 Conclusion

Based on the conducted experiments, both the moving-window method and the bootstrapping method were employed to construct uncertainty sets for the mean and covariance. These uncertainty sets were then used as inputs for robust optimization, influencing the resulting asset allocations within the portfolio to maximize profits. The procedure for determining uncertainty sets was applied consistently across assets, yielding 45 uncertainty intervals for both the mean and covariance.

The results demonstrate that robust optimization with uncertainty sets derived from the moving-window method offers better performance for investors. First, across different γ\gamma values, the objective function values obtained from the moving-window method are consistently lower than those from the bootstrapping method, indicating a more favorable risk–return trade-off. Second, under both good and poor market conditions, robust optimization with the moving-window method generated profits, suggesting that investors can achieve positive returns regardless of market fluctuations. Finally, portfolio return graphs across different γ\gamma values show that the moving-window method delivers higher profits when γ=5\gamma=5, corresponding to risk-taking investors, while still maintaining competitive performance under higher γ\gamma values.

## Acknowledgment

This research was supported by the Departmental Research Funding Program, Batch 1 (2025), under Contract No. 2320/PKS/ITS/2025, between the Directorate of Research and Community Service, Institut Teknologi Sepuluh Nopember (ITS), and Sena Safarina, S.Si., M.Sc., D.Sc.

## References

* [1]

  Abdurakhman: Asset allocation in indonesian stocks using portfolio robust.
  Mathematics and Statistics 10(6), 1313–1319 (2022)
* [2]

  Ben-Tal, A., Nemirovski, A.: Robust convex optimization. Mathematics of
  Operations Research 23(4), 769–805 (1998)
* [3]

  Cornuejols, G., Tutuncu, R.: Optimization Methods in Finance, vol. 5. Cambridge
  University Press (2006)
* [4]

  Costa, G., Kwon, R.: A robust framework for risk parity portfolios. Journal of
  Asset Management 21(5), 447–466 (2020)
* [5]

  Engels, M.: Portfolio Optimization: Beyond Markowitz. Master’s thesis, Leiden
  University (2004)
* [6]

  Hermuningsih, S.: Pengantar Pasar Modal Indonesia. STIM YKPN (2019)
* [7]

  Isavnin, A.G., Galiev, D.R., Karamyshev, A.N., Makhmutov, I.I.: Robust
  optimization of the investment portfolio under uncertainty conditions.
  Journal of Environmental Treatment Techniques 7(Special Issue), 1093–1098
  (2019)
* [8]

  Markowitz, H.: Modern portfolio theory. Journal of Finance 7(11), 77–91
  (1952)
* [9]

  Mulyana, R.N.: Lokal mendominasi, investor pasar modal diprediksi tumbuh hingga
  30% di 2023 (Dec 2022),
  <https://investasi.kontan.co.id/news/lokal-mendominasi-investor-pasar-modal-diprediksi-tumbuh-hingga-30-di-2023>,
  accessed: 2025-09-07
* [10]

  Palomar, D.P.: Portfolio Optimization: Theory and Application. Cambridge
  University Press (2025), available online at
  <https://portfoliooptimizationbook.com/portfolio-optimization-book.pdf>
* [11]

  Tutuncu, R.H., Koenig, M.: Robust asset allocation. Annals of Operations
  Research 132, 157–187 (2004)