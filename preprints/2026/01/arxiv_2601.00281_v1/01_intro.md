---
authors:
- Yifan Liu
- Shi-Dong Liang
doc_id: arxiv:2601.00281v1
family_id: arxiv:2601.00281
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: "A Global Optimal Theory of Portfolio beyond R-\U0001D70E Model"
url_abs: http://arxiv.org/abs/2601.00281v1
url_html: https://arxiv.org/html/2601.00281v1
venue: arXiv q-fin
version: 1
year: 2026
---


Yifan Liu and Shi-Dong Liang
  
School of Physics, Sun Yat-Sen University
  
Guangzhou, China
liuyfsysu@163.comstslsd@mail.sysu.edu.cn

(January 1, 2026)

###### Abstract

The deviation of the efficient market hypothesis (EMH) for the practical economic system
allows us gain the arbitrary or risk premium in finance markets.
We propose the triplet (R,H,σ)(R,H,\sigma) theory to give the local and global optimal
portfolio, which generalize from the (R,σ)(R,\sigma) model.
We present the formulation of the triplet (R,H,σ)(R,H,\sigma) model and give the Pareto optimal solution as well as comparing it with the numerical investigations for the Chinese stock market. We define the local optimal weights of the triplet (𝐰R,𝐰H,𝐰σ)(\mathbf{w}\_{R},\mathbf{w}\_{H},\mathbf{w}\_{\sigma}), which constructs
the triangle of the quasi-optimal investing subspace such that we further define the
centroid of the triangle or the incenter of the triangle
as the optimal investing weights, which optimizes the mean return, the arbitrary or risk
premium and the volatility risk. By investigating numerically the Chinese stock market as an example we demonstrate the validity of the formulation and obtain the global optimal
strategy and quasi-optimal investing subspace. The theory provides an efficient way to design the portfolio for different style investors, conservative or aggressive investors, in finance market to maximize the mean return and arbitrary or risk premium with a small volatility risk.

## 1 Introduction

As one of fundamental classic finance theories, Efficient Market Hypothesis (EMH) has been questioned by some practical economic systems, such as the stock markets.[[1](https://arxiv.org/html/2601.00281v1#bib.bib1), [2](https://arxiv.org/html/2601.00281v1#bib.bib2), [3](https://arxiv.org/html/2601.00281v1#bib.bib3)] Some novel financial phenomena, such as momentum and contrarian effect, mean reversion effect indicate stock returns follows the stable Levy distribution rather than standard Gaussian distribution. [[4](https://arxiv.org/html/2601.00281v1#bib.bib4)] The stock price movements are influenced by the investors’ psychology. Edgar E. Peters proposed Fractal Market Hypothesis (FMH) to analyze the capital markets by non-linear and fractal theories and methods. [[12](https://arxiv.org/html/2601.00281v1#bib.bib12)] The key features of FMH are that the time sequences of the asset prices show the self-similarity and has the long-term correlation. [[6](https://arxiv.org/html/2601.00281v1#bib.bib6), [7](https://arxiv.org/html/2601.00281v1#bib.bib7), [8](https://arxiv.org/html/2601.00281v1#bib.bib8)] In principle, the Hurst exponent (0<H​u​r​s​t<1)(0<Hurst<1) can be used as an index to measure quantitatively the long-term correlation. Some studies showed that Hurst exponent could be regarded as a kind of risk premium: the bigger is, the more risk or speculate premium one asset contains, and investors could get the risk premium by using trend or reversal strategies.[[9](https://arxiv.org/html/2601.00281v1#bib.bib9), [10](https://arxiv.org/html/2601.00281v1#bib.bib10)]

Using the fractal and multifractal theories to analyze stock market become a branch of econophysics. Markwitz proposed a mean-variance (R,σ)(R,\sigma) model based on the standard Gaussian process for the optimization asset allocation, which guides the investor to maximize the mean return and minimize the risk. [[11](https://arxiv.org/html/2601.00281v1#bib.bib11)] However, some practical stock markets deviate the standard Gaussian process and exhibit fractal characteristic, [[12](https://arxiv.org/html/2601.00281v1#bib.bib12), [13](https://arxiv.org/html/2601.00281v1#bib.bib13)] which provides some chance to optimize their asset allocation by using these fractal behaviors. The question is how to design an optimal investing strategy or how to select the asset allocation or portfolio based on the fractal stochastic time sequences and their historical data.

In this paper, we generalize the mean-variance model of portfolio to a triplet mathematical model (R,σ,H)(R,\sigma,H) of portfolio, which contains the mean return, risk and speculate premium. Based on this model we give the Pareto optimal solution of portfolio and the global optimal solution of portfolio as well as the quasi-optimal subspace for different investment options. We also propose two practical strategies to find out the optimal or relative optimal investing schemes of portfolio for different investors. In Sec. II, we will present the triplet mathematical model of portfolio (R,σ,H)(R,\sigma,H) and its Pareto optimal solution. We will define the global optimal solution and the quasi-optimal subspace of portfolio in Sec. III. We propose two practical strategies to find out the global and quasi-optimal solutions of portfolio in Sec. V. Finally, we will give the conclusion.

## 2 (R,σ,H)(R,\sigma,H) model of portfolio and its Pareto solution

The main goal of portfolio is to maximize the return and minimize the risk.
Based on the EMH, the higher return, the higher risk, which implies
that there does not exist the arbitrage space. However,
the practical economic systems deviate the EMH, namely the stochastic processes
deviate the standard Gaussian process, which induces some arbitrage space.
Since the Hurst exponent measures the deviation of the stochastic process from
the standard Gaussian process, we take the Hurst exponent into account
to set up a triplet mathematical model (R,σ,H)(R,\sigma,H), where RR denotes the expected
returns and its corresponding variance σ\sigma. HH is the Hurst exponent, which
provides some information for the risk or speculate premium.
This model generalizes the mean-variance model (R,σ)(R,\sigma) by Markwitz.[[11](https://arxiv.org/html/2601.00281v1#bib.bib11)]

Let us set {ri​(τk)}\{r\_{i}(\tau\_{k})\} be the time sequence of the expected returns for the asset ii at the time interval τk=tk−tk−1\tau\_{k}=t\_{k}-t\_{k-1}, where i=1,2,…​Ni=1,2,...N labels different asset and k=1,2,…​Mk=1,2,...M labels the time interval.
The time-mean return of the asset vector in the whole period is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐑:=(R1,R2,⋯,RN)=1M​∑k=1M𝐫​(τk)\mathbf{R}:=\left(R\_{1},R\_{2},\cdots,R\_{N}\right)=\frac{1}{M}\sum\_{k=1}^{M}\mathbf{r}(\tau\_{k}) |  | (1) |

where
Ri=(∑k=1Mr1​(τk),∑k=1Mr2​(τk),⋯,∑k=1MrM​(τk))/MR\_{i}=\left(\sum\_{k=1}^{M}r\_{1}(\tau\_{k}),\sum\_{k=1}^{M}r\_{2}(\tau\_{k}),\cdots,\sum\_{k=1}^{M}r\_{M}(\tau\_{k})\right)/M.

Suppose that the portfolio weights for different assets are denoted by a vector,
𝐰={wi}∈Ω\mathbf{w}=\{w\_{i}\}\in\Omega with ∑i=1Nwi=1\sum\_{i=1}^{N}w\_{i}=1, and wi≥0w\_{i}\geq 0, where Ω\Omega is the sample space in the probability space of the portfolio.
The total return of the portfolio can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨R⟩=𝐰⊤​𝐑\left\langle R\right\rangle=\mathbf{w}^{\top}\mathbf{R} |  | (2) |

with its corresponding variance

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(𝐰)=⟨(Ri−⟨R⟩)2⟩=𝐰⊤​𝐂𝐰\sigma^{2}(\mathbf{w})=\left\langle\left(R\_{i}-\left\langle R\right\rangle\right)^{2}\right\rangle=\mathbf{w}^{\top}\mathbf{C}\mathbf{w} |  | (3) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂=(σi​j)\mathbf{C}=(\sigma\_{ij}) |  | (4) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | σi​j=⟨Ri​Rj⟩−⟨Ri⟩​⟨Rj⟩\sigma\_{ij}=\langle R\_{i}R\_{j}\rangle-\langle R\_{i}\rangle\langle R\_{j}\rangle |  | (5) |

is the correlation matrix of the return.

For a given asset ii, its return is a stochastic series
with the time step kk, {ri​(τk)}\{r\_{i}(\tau\_{k})\}. Suppose that the time series {ri​(τk)}\{r\_{i}(\tau\_{k})\}
deviate the standard Gaussian process, which can be measured by the Hurst exponent.
When Hi=1/2H\_{i}=1/2 means the time series {ri​(τk)}\{r\_{i}(\tau\_{k})\} runs with the standard Gaussian process, and Hi>1/2H\_{i}>1/2 predicts a persistency correlation, and
Hi<1/2H\_{i}<1/2 predicts an anti-persistency correlation.
The deviation of the standard Gaussian process
provides some arbitrage space for investors.
The investigation of the Chinese stock market indicates that the stock series
deviates the standard Gaussian process and its Hurst exponent is around 0.6[[14](https://arxiv.org/html/2601.00281v1#bib.bib14), [15](https://arxiv.org/html/2601.00281v1#bib.bib15)].
This implies that the stock market runs a fractal Browan process and
there exists some arbitrage space or risk premium in the stochastic
market. We may assume that the investors favor the non-standard Gaussian process
in the stochastic market because the non-standard Gaussian process implies the existence of
some information for speculation.
The Hurst exponent can be calculated by (see Appendix)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hi=log⁡(Fi​(s)/C)log⁡sH\_{i}=\frac{\log(F\_{i}(s)/C)}{\log s} |  | (6) |

where Fi​(s)F\_{i}(s) is the fluctuation function of the stochastic sequences.
We introduce the mean Hurst exponent,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨H⟩=∑i=1Nwi​Hi=𝐰⊤​𝐇\langle H\rangle=\sum\_{i=1}^{N}w\_{i}H\_{i}=\mathbf{w}^{\top}\mathbf{H} |  | (7) |

In general, it can be assumed that any asset time series is a non-Markov chain and
non-standard Gaussian process. The non-Markov properties of the stochastic
sequences promise the predicability of the stochastic sequences based on the prior
information of the sequences. The non-standard Gaussian properties of the stochastic
sequences provide an arbitrage space for investors.

The question is how investors design an optimal asset allocation or portfolio based on the prior information of the stochastic sequences.
In general we can define the optimal weight of the portfolio.

Definition: The Pareto optimal weight of the portfolio is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {𝐰∗∈ΩN|max𝐰∗∈Ω⁡R​(𝐰),min𝐰∗∈Ω⁡σ2​(𝐰),(𝐰∗⊤​𝐇)≥12,𝟏⊤​𝐰∗=1}\left\{\mathbf{w}^{\*}\in\Omega^{N}\left|\max\_{\mathbf{w}^{\*}\in\Omega}R(\mathbf{w}),\right.\min\_{\mathbf{w}^{\*}\in\Omega}\sigma^{2}(\mathbf{w}),\left(\mathbf{w}^{\*\top}\mathbf{H}\right)\geq\frac{1}{2},\mathbf{1}^{\top}\mathbf{w}^{\*}=1\right\} |  | (8) |

where 𝟏⊤=(1,1,⋯,1N)\mathbf{1}^{\top}=(1,1,\cdots,1\_{N}).

The main goal of investors is to design a weight for portfolio to maximize the return max𝐰∗∈Ω⁡RM\max\_{\mathbf{w}^{\*}\in\Omega}R\_{M} and to minimize the uncertainty and risk.
The constraint (𝐰∗⊤​𝐇)≥12\left(\mathbf{w}^{\*\top}\mathbf{H}\right)\geq\frac{1}{2} means that we can search for the bigger arbitrage space for investors.
The optimal asset portfolio problem is a multi-objected optimization problem from the mathematical point of views. Thus, the portfolio space
can be generalized to three-dimensional space Return-Risk-Arbitrage (RRA) from
the conventional two-dimensional space Return-Risk (RR).[[16](https://arxiv.org/html/2601.00281v1#bib.bib16)]
We may define the Lagrangian function by[[16](https://arxiv.org/html/2601.00281v1#bib.bib16)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | L=R​(𝐰)−σ2​(𝐰)+λ​(𝐠​(𝐰)−𝐛)L=R(\mathbf{w})-\sigma^{2}(\mathbf{w})+\mathbf{\lambda}(\mathbf{g}(\mathbf{w})-\mathbf{b}) |  | (9) |

where
λ=(λ1,λ2)\mathbf{\lambda}=(\lambda\_{1},\lambda\_{2}) is the Lagrangian multiplier vector and

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | R​(𝐰)\displaystyle R(\mathbf{w}) | =\displaystyle= | 𝐰⊤​𝐑\displaystyle\mathbf{w}^{\top}\mathbf{R} |  | (10) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | σ2​(𝐰)\displaystyle\sigma^{2}(\mathbf{w}) | =\displaystyle= | 𝐰⊤​𝐂𝐰\displaystyle\mathbf{w}^{\top}\mathbf{C}\mathbf{w} |  | (11) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝐠​(𝐰)\displaystyle\mathbf{g}(\mathbf{w}) | =\displaystyle= | ((𝐰⊤​𝐇),𝐰)⊤\displaystyle\left(\left(\mathbf{w}^{\top}\mathbf{H}\right),\mathbf{w}\right)^{\top} |  | (12) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝐛\displaystyle\mathbf{b} | =\displaystyle= | (12,1)⊤\displaystyle\left(\frac{1}{2},1\right)^{\top} |  | (13) |

The Lagrangian function as the objective function can be maximized by the Kuhn-Tucker theorem.[[16](https://arxiv.org/html/2601.00281v1#bib.bib16)] The Kuhn-Tucker conditions are

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐑−2​𝐂𝐰+λ1​𝐇+λ2​𝟏≤𝟎\displaystyle\mathbf{R}-2\mathbf{C}\mathbf{w}+\lambda\_{1}\mathbf{H}+\lambda\_{2}\mathbf{1}\leq\mathbf{0} |  | (14) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐰⊤​𝐇−12≥0\displaystyle\mathbf{w}^{\top}\mathbf{H}-\frac{1}{2}\geq 0 |  | (15) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐰⊤​𝟏−1=0\displaystyle\mathbf{w}^{\top}\mathbf{1}-1=0 |  | (16) |

By solving the Kuhn-Tucker conditions, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐰∗=12​𝐂−1​(𝐑+λ1​𝐇+λ2​𝟏)\mathbf{w}^{\*}=\frac{1}{2}\mathbf{C}^{-1}\left(\mathbf{R}+\lambda\_{1}\mathbf{H}+\lambda\_{2}\mathbf{1}\right) |  | (18) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | (λ1λ1)=1det𝐐​(α​𝟏⊤​𝐂−1​𝟏−β​𝐇⊤​𝐂−1​𝟏−α​𝟏⊤​𝐂−1​𝐇+β​𝐇⊤​𝐂−1​𝐇)\left(\begin{array}[]{c}\lambda\_{1}\\ \lambda\_{1}\end{array}\right)=\frac{1}{\det\mathbf{Q}}\left(\begin{array}[]{c}\alpha\mathbf{1}^{\top}\mathbf{C}^{-1}\mathbf{1}-\beta\mathbf{H}^{\top}\mathbf{C}^{-1}\mathbf{1}\\ -\alpha\mathbf{1}^{\top}\mathbf{C}^{-1}\mathbf{H}+\beta\mathbf{H}^{\top}\mathbf{C}^{-1}\mathbf{H}\end{array}\right) |  | (19) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐐=(𝐇⊤​𝐂−1​𝐇𝐇⊤​𝐂−1​𝟏𝟏⊤​𝐂−1​𝐇𝟏⊤​𝐂−1​𝟏)\mathbf{Q}=\left(\begin{array}[]{cc}\mathbf{H}^{\top}\mathbf{C}^{-1}\mathbf{H}&\quad\mathbf{H}^{\top}\mathbf{C}^{-1}\mathbf{1}\\ \mathbf{1}^{\top}\mathbf{C}^{-1}\mathbf{H}&\mathbf{1}^{\top}\mathbf{C}^{-1}\mathbf{1}\end{array}\right) |  | (20) |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | α\displaystyle\alpha | =\displaystyle= | 1−𝐇⊤​𝐂−1​𝐑\displaystyle 1-\mathbf{H}^{\top}\mathbf{C}^{-1}\mathbf{R} |  | (21) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | β\displaystyle\beta | =\displaystyle= | 2−𝟏⊤​𝐂−1​𝐑\displaystyle 2-\mathbf{1}^{\top}\mathbf{C}^{-1}\mathbf{R} |  | (22) |

The formulation on portfolio we obtain from ([18](https://arxiv.org/html/2601.00281v1#S2.E18 "In 2 (𝑅,𝜎,𝐻) model of portfolio and its Pareto solution ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model")) to ([21](https://arxiv.org/html/2601.00281v1#S2.E21 "In 2 (𝑅,𝜎,𝐻) model of portfolio and its Pareto solution ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model")) provides a
efficient way to search for the Pareto optimal weight of portfolio for investors.

## 3 Global optimal solution and Quasi-optimal subspace

However, the Pareto optimal solution is based on the constraint
(𝐰∗⊤​𝐇)≥12\left(\mathbf{w}^{\*\top}\mathbf{H}\right)\geq\frac{1}{2}. There should be either
some bigger arbitrage space for the aggressive investors or concrete space for
the conservative investors. Thus, we define the local optimal weight of portfolio.

Definition of Local optimum:
The weights 𝐰R,𝐰σ,𝐰H∈Ω\mathbf{w}\_{R},\mathbf{w}\_{\sigma},\mathbf{w}\_{H}\in\Omega
are local optimal respectively if they satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝐰R,𝐰σ,𝐰H):=(max𝐰∈Ω⁡{⟨R⟩},min𝐰∈Ω⁡{σ},max𝐰∈Ω⁡{H})(\mathbf{w}\_{R},\mathbf{w}\_{\sigma},\mathbf{w}\_{H}):=\left(\max\_{\mathbf{w}\in\Omega}\{\langle R\rangle\},\min\_{\mathbf{w}\in\Omega}\{\sigma\},\max\_{\mathbf{w}\in\Omega}\{H\}\right) |  | (23) |

where
𝐰R:={wiR}max𝐰∈Ω⁡{⟨R⟩}\mathbf{w}\_{R}:=\{w^{R}\_{i}\}\_{\max\_{\mathbf{w}\in\Omega}\{\langle R\rangle\}}, 𝐰σ:={wiσ}min𝐰∈Ω⁡{σ}\mathbf{w}\_{\sigma}:=\{w\_{i}^{\sigma}\}\_{\min\_{\mathbf{w}\in\Omega}\{\sigma\}}, and 𝐰H:={wiH}max𝐰∈Ω⁡{H}\mathbf{w}\_{H}:=\{w\_{i}^{H}\}\_{\max\_{\mathbf{w}\in\Omega}\{H\}} .

In general 𝐰R≠𝐰σ≠𝐰H\mathbf{w}\_{R}\neq\mathbf{w}\_{\sigma}\neq\mathbf{w}\_{H} and they
could be competed each other for different benefits, which give the extreme values for
investors to estimate their expected return, the biggest arbitrage space and
the worst risk. For convenience we define a quasi-subspace within the whole
investing space as a domain of investment for different strategies of different style investors. Suppose that (𝐰R,𝐰σ,𝐰H)(\mathbf{w}\_{R},\mathbf{w}\_{\sigma},\mathbf{w}\_{H})
forms a triangle in the sample space without losing generality.

Definition of Quasi-optimal subspace ΩT\Omega\_{T}: The subset ΩT⊂Ω\Omega\_{T}\subset\Omega is the quasi-optimal subspace if it is within
the triangle consisted of the vertex (𝐰R,𝐰σ,𝐰H)\left(\mathbf{w}\_{R},\mathbf{w}\_{\sigma},\mathbf{w}\_{H}\right) in the sample space.

This quasi-optimal subspace provides a practical domain of portfolio in the investing space
for different investing style investors. The aggressive investors may
select the weights close to 𝐰R\mathbf{w}\_{R} and the conservative investors
may select the weights close to 𝐰σ\mathbf{w}\_{\sigma}.

What is the global optimal weight for investors?
If we assume to share equally the three factors, return, risk and arbitrage,
the global optimal weight should close the three local
optimal weights as much as possible. Therefore,
We define the global optimal weight 𝐰O\mathbf{w}\_{O} by

Definition of Global optimum 𝐰O\mathbf{w}\_{O}: The weight of the portfolio 𝐰O={wi}O∈Ω\mathbf{w}\_{O}=\{w\_{i}\}\_{O}\in\Omega is global optimal if it satisfies
(min𝐰∈Ω⁡dO,R,min𝐰∈Ω⁡dO,σ,min𝐰∈Ω⁡dO,H)\left(\min\_{\mathbf{w}\in\Omega}d\_{O,R},\min\_{\mathbf{w}\in\Omega}d\_{O,\sigma},\min\_{\mathbf{w}\in\Omega}d\_{O,H}\right) simultaneously.
where dO,αd\_{O,\alpha} is the distance between
𝐰O\mathbf{w}\_{O} and 𝐰α\mathbf{w}\_{\alpha}, where α=R,σ,H\alpha=R,\sigma,H.

This global optimal weight can be regarded as a Pareto solution of the triplet game.
The weight can be viewed as a vector. Thus, we can define the distance between two local weights by the norm of the difference between two weight vectors in Euclidian space.

Definition of Distance:
The distance between two vectors 𝐰α,𝐰β\mathbf{w}\_{\alpha},\mathbf{w}\_{\beta} is defined by
the norm in Euclidian space,

|  |  |  |  |
| --- | --- | --- | --- |
|  | dα,β=‖𝐰α−𝐰β‖d\_{\alpha,\beta}=\|\mathbf{w}\_{\alpha}-\mathbf{w}\_{\beta}\| |  | (24) |

Based on the definition of the distance between two local weights, we can define the distance for any investing weight away from the global optimal weight.

|  |  |  |  |
| --- | --- | --- | --- |
|  | d𝐰,O:=‖𝐰−𝐰R‖+‖𝐰−𝐰σ‖+‖𝐰−𝐰H‖d\_{\mathbf{w},O}:=\|\mathbf{w}-\mathbf{w}\_{R}\|+\|\mathbf{w}-\mathbf{w}\_{\sigma}\|+\|\mathbf{w}-\mathbf{w}\_{H}\| |  | (25) |

Thus, the basic idea to find out the global optimal weight is to minimize dO:=min𝐰𝐎∈Ω⁡d𝐰,Od\_{O}:=\min\_{\mathbf{w\_{O}}\in\Omega}d\_{\mathbf{w},O}.
It implies the global optimal solution is within the triangle constructed by the
local optimal weights, 𝐰O∈ΩT\mathbf{w}\_{O}\in\Omega\_{T}. Thus, we propose two schemes to find out the global optimal solution of portfolio.

Global optimal solution: The global optimal solution of portfolio
is either

(1) the centroid of the triangle ΩT\Omega\_{T},

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi,O(c)=13​(wiR+wiσ+wiH)w\_{i,O}^{(c)}=\frac{1}{3}(w\_{i}^{R}+w\_{i}^{\sigma}+w\_{i}^{H}) |  | (26) |

or

(2) the incenter of the triangle ΩI​C\Omega\_{IC},

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi,O(i​c)=dσ,H​wiR+dR,H​wiσ+dR,σ​wiHdσ,H+dR,H+dR,σw\_{i,O}^{(ic)}=\frac{d\_{\sigma,H}w\_{i}^{R}+d\_{R,H}w\_{i}^{\sigma}+d\_{R,\sigma}w\_{i}^{H}}{d\_{\sigma,H}+d\_{R,H}+d\_{R,\sigma}} |  | (27) |

where dα,βd\_{\alpha,\beta} is the distance between the weights of α\alpha and β\beta.

Quasi-optimal subspace: The quasi-optimal subspace is either

(1) the triangle ΩT\Omega\_{T} constructed by the local optimal weights, (𝐰R,𝐰H,𝐰σ)\left(\mathbf{w}\_{R},\mathbf{w}\_{H},\mathbf{w}\_{\sigma}\right).

or

(2) the incenter of the triangle ΩI​C\Omega\_{IC}, which radius is

|  |  |  |  |
| --- | --- | --- | --- |
|  | rI=(s−dσ,H)​(s−dR,H)​(s−dR,σ)sr\_{I}=\sqrt{\frac{(s-d\_{\sigma,H})(s-d\_{R,H})(s-d\_{R,\sigma})}{s}} |  | (28) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | s=dσ,H+dR,H+dR,σ3s=\frac{d\_{\sigma,H}+d\_{R,H}+d\_{R,\sigma}}{3} |  | (29) |

The global optimal solution and the quasi-optimal subspace provide a lot of investing strategies or schemes for different style investors to gain their expected mean returns.
The optimal solutions of portfolio, the centroid of the triangle and the incenter of the triangle, balance the mean return, arbitrary premium and volatility risk, which can be regarded a Pareto solution of the triplet game.
The two quasi-optimal subspaces, the triangle and the incircle of the triangle,
can be regarded as two efficient subspace in the investing space, which provide
a lot of choices for differential style investors to play their investing strategies.
The aggressive investor may choose the weights near the local optimum of the mean return 𝐰R\mathbf{w}\_{R} or near both of 𝐰R,𝐰H\mathbf{w}\_{R},\mathbf{w}\_{H} inside of the
triangle. The conservative investors may choose the weights near the local optimum of the volatility 𝐰σ\mathbf{w}\_{\sigma} inside of the triangle.

It should be remarked that the quasi-optimal subspace ΩT\Omega\_{T} could depend on the
time interval τ\tau we choose. We denote the quasi-optimal subspace ΩTτ\Omega\_{T}^{\tau}
for given time interval τ\tau. In order to reduce the uncertainty induced by
the time interval we choose, we propose two schemes to enhance the predicability
of the optimal strategies. One is that we make the average of the local optimal
weights for different time interval τ\tau, which is defined by

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝐰Rτ:\displaystyle\mathbf{w}\_{R}^{\tau}: | =\displaystyle= | 1Nτ​∑nNτ𝐰Rτn\displaystyle\frac{1}{N\_{\tau}}\sum\_{n}^{N\_{\tau}}\mathbf{w}\_{R}^{\tau\_{n}} |  | (30) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝐰στ:\displaystyle\mathbf{w}\_{\sigma}^{\tau}: | =\displaystyle= | 1Nτ​∑nNτ𝐰στn\displaystyle\frac{1}{N\_{\tau}}\sum\_{n}^{N\_{\tau}}\mathbf{w}\_{\sigma}^{\tau\_{n}} |  | (31) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝐰Hτ:\displaystyle\mathbf{w}\_{H}^{\tau}: | =\displaystyle= | 1Nτ​∑nNτ𝐰Hτn\displaystyle\frac{1}{N\_{\tau}}\sum\_{n}^{N\_{\tau}}\mathbf{w}\_{H}^{\tau\_{n}} |  | (32) |

where NτN\_{\tau} is the number of the time intervals we choose.
The averages of the local optimal weights for different time intervals
as an effective local optimal weights can reduce the uncertainty of the time intervals
we choose. Based on this effective local optimal weights we can
define the effective quasi-optimal subspace by the triangle consisted of the vertexes
(𝐰Rτ,𝐰στ,𝐰Hτ)(\mathbf{w}\_{R}^{\tau},\mathbf{w}\_{\sigma}^{\tau},\mathbf{w}\_{H}^{\tau}).

The other way to reduce the uncertainty from the time interval is that we
define the effective quasi-optimal subspace ΩT\Omega\_{T} by the overlap of the quasi-optimal subspaces for different given time interval τ\tau.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΩTe​f​f=⋂τΩTτ\Omega\_{T}^{eff}=\bigcap\_{\tau}\Omega\_{T}^{\tau} |  | (33) |

The averages of the local optimal weights enhance the predicability of the optimal
strategies. The effective quasi-optimal subspace provides a way to shrink the
effective investing space of portfolio.

![Refer to caption](x1.png)


Figure 1: (Color online)The log⁡F​(s)−log⁡(s)\log F(s)-\log(s) of the index subseries of the Chinese stock market.

## 4 Applications in Stock market

### 4.1 Fractal characteristic in Stock market

The stock market is a stochastic time sequences.
We analyze the basic characteristic of the Chinese stock market based on the Hurst exponent method. We use 12921292 daily data of the Shanghai (securities) composite index from Jan. 4 2013 to Apr. 27 2018. The subsequences length ss of the stock index log-return series is from s=5s=5 to 12921292. By plotting log⁡(F​(s))−log⁡(s)\log(F(s))-\log(s) (see Fig. [1](https://arxiv.org/html/2601.00281v1#S3.F1 "Figure 1 ‣ 3 Global optimal solution and Quasi-optimal subspace ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model")) with the linear fitting. We obtain the Hurst exponent of the Shanghai (securities) composite index 0.59570.5957, which means that the Chinese stock market does not follow the geometric Brownian motion, but the fractal Brownian motion.

![Refer to caption](x2.png)


Figure 2: (Color online):The investing space based on the (R,σ,H)(R,\sigma,H) model, where
the time interval is one day.
The red points are the local optimal weights for (max⁡R,min⁡σ,max⁡H)(\max R,\min\sigma,\max H).

The fractal characteristic emerging in Chinese stock market
implies that there exists the speculate or risk premium for investors.
The rational investors can optimize their asset allocation based on maximizing |H−0.5||H-0.5| .
This provides some chance to optimize the portfolio based on the above formulation of portfolio.

Table 1: Optimal Weights and Their Mean Returns

| LOW1 | 𝐰R​(0,0,1)\mathbf{w}\_{R}(0,0,1) | 𝐰H​(0,1,0)\mathbf{w}\_{H}(0,1,0) | 𝐰σ​(0.40,0.48,0.12)\mathbf{w}\_{\sigma}(0.40,0.48,0.12) |
| --- | --- | --- | --- |
| DMR2 | 0.12% | 0.11 % | 0.094% |
| VR3 | 0.0328 | 0.0196 | 0.0160 |
| OW4 | 𝐰Oc​(0.49,0.37,0.14)\mathbf{w}^{c}\_{O}(0.49,0.37,0.14) | 𝐰Oi​c​(0.56,0.26,0.18)\mathbf{w}^{ic}\_{O}(0.56,0.26,0.18) | 𝐰O∗​(0.5071,0.3003,0.1925)6\mathbf{w}^{\*}\_{O}(0.5071,0.3003,0.1925)^{6} |
| ODMR5 | 0.090% | 0.087% | 0.089% |
| VR3 | 0.0161 | 0.0178 | 0.0165 |

1LOW: Local Optimal Weight; 2DMR: Daily Mean Return;
3VR: Volatility Risk;
  
4OW: Optimal Weight:𝐰c\mathbf{w}^{c}: Centroid of triangle;
𝐰i​c\mathbf{w}^{ic}: Incenter of triangle
  
5ODMR: Optimal Daily Mean Return;
6Calculated by Eqs. ([18](https://arxiv.org/html/2601.00281v1#S2.E18 "In 2 (𝑅,𝜎,𝐻) model of portfolio and its Pareto solution ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model"))-([30](https://arxiv.org/html/2601.00281v1#S3.E30 "In 3 Global optimal solution and Quasi-optimal subspace ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model"))

### 4.2 Optimal strategic space

The (R,σ,H)(R,\sigma,H) model we generalized provides more opportunities to gain the
arbitrage or risk premium for investors. Let us analyze some stock running
as an example to demonstrate how our method works.
We investigate the strategic space of three stocks,
Yunnan Baiyao (000538.SZ), Guizhou Maotai (600519.SH) and Iflytek (002230.SZ),
in Chinese stock market based on the formulation in Eqs. ([18](https://arxiv.org/html/2601.00281v1#S2.E18 "In 2 (𝑅,𝜎,𝐻) model of portfolio and its Pareto solution ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model"))-([30](https://arxiv.org/html/2601.00281v1#S3.E30 "In 3 Global optimal solution and Quasi-optimal subspace ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model")) and the numerical method in Eq. ([23](https://arxiv.org/html/2601.00281v1#S3.E23 "In 3 Global optimal solution and Quasi-optimal subspace ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model")). The data we investigated are from Jan. 4, 2013 to April 27, 2018 and the time intervals we chose are one day.

![Refer to caption](x3.png)


Figure 3: (Color online): The quasi-optimal investing subspace of (R,σ,H)(R,\sigma,H) model.

The investing space of the (R,σ,H)(R,\sigma,H) model for these three stocks in Chinese stock market is shown in Fig. ([2](https://arxiv.org/html/2601.00281v1#S4.F2 "Figure 2 ‣ 4.1 Fractal characteristic in Stock market ‣ 4 Applications in Stock market ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model")), in which the red points are the local optimal weights for (max⁡R,min⁡σ,max⁡H)(\max R,\min\sigma,\max H). These points provide a guideline for different style investors, aggressive or conservative investors.

The local optimal weights, optimal weights and their daily mean returns are
calculated by the formulation in Eqs. ([18](https://arxiv.org/html/2601.00281v1#S2.E18 "In 2 (𝑅,𝜎,𝐻) model of portfolio and its Pareto solution ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model"))-([30](https://arxiv.org/html/2601.00281v1#S3.E30 "In 3 Global optimal solution and Quasi-optimal subspace ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model")) and by the numerical results directly from the definition ([23](https://arxiv.org/html/2601.00281v1#S3.E23 "In 3 Global optimal solution and Quasi-optimal subspace ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model")), which are listed in the table I.

Table 2: The Averages of Optimal Weights and Their Mean Returns

| ALOW1 | 𝐰R​(0,0,1)\mathbf{w}\_{R}(0,0,1) | 𝐰H​(0,0.9,0.1)\mathbf{w}\_{H}(0,0.9,0.1) | 𝐰σ​(0.51,0.42,0.07)\mathbf{w}\_{\sigma}(0.51,0.42,0.07) |
| --- | --- | --- | --- |
| ADMR2 | 0.12% | 0.11 % | 0.088% |
| SE3 | 0.0328 | 0.0185 | 0.0161 |
| AOW4 | 𝐰Oc​(0.44,0.39,0.21)\mathbf{w}^{c}\_{O}(0.44,0.39,0.21) | 𝐰Oi​c​(0.50,0.29,0.17)\mathbf{w}^{ic}\_{O}(0.50,0.29,0.17) | 𝐰O∗​(0.5373,0.2585,0.2042)6\mathbf{w}^{\*}\_{O}(0.5373,0.2585,0.2042)^{6} |
| AODMR5 | 0.093% | 0.090% | 0.088% |
| SE3 | 0.0161 | 0.0166 | 0.0167 |

1ALOW: Average of Local Optimal Weight of the time interval from 1 to 10 days
  
2ADMR: Average of Daily Mean Return;
3SE: Standard Errors for different time intervals;
  
4AOW: Averages of Optimal Weight:
𝐰c\mathbf{w}^{c}: Centroid of triangle; 𝐰i​c\mathbf{w}^{ic}: Incenter of triangle
  
5AODMR: Average of Optimal Daily Mean Return;
6Calculated by Eqs. ([18](https://arxiv.org/html/2601.00281v1#S2.E18 "In 2 (𝑅,𝜎,𝐻) model of portfolio and its Pareto solution ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model"))-([30](https://arxiv.org/html/2601.00281v1#S3.E30 "In 3 Global optimal solution and Quasi-optimal subspace ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model"))

It can be seen that the daily returns of the local optimal weights is best
at the local maximum mean return point 𝐰R\mathbf{w}\_{R}, the second at the local maximum
Hurst exponent point 𝐰H\mathbf{w}\_{H} and the lowest at the minimum variance point𝐰σ\mathbf{w}\_{\sigma}.
However, the volatility risk is inverse the biggest for 𝐰R\mathbf{w}\_{R}, the lowest
for 𝐰σ\mathbf{w}\_{\sigma}. This make sense. The daily mean return of optimal weight at the centroid of the triangle is better that at the incenter of the triangle, which
implies that the optimal weight estimated by the centroid of triangle is better than
the weight by the incenter of triangle from the daily mean return point of views.
Both of them are close to the analytic result by the formulation ([18](https://arxiv.org/html/2601.00281v1#S2.E18 "In 2 (𝑅,𝜎,𝐻) model of portfolio and its Pareto solution ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model"))-([30](https://arxiv.org/html/2601.00281v1#S3.E30 "In 3 Global optimal solution and Quasi-optimal subspace ‣ A Global Optimal Theory of Portfolio beyond R-𝜎 Model")).

In order to examine the effect of the time interval we investigate the
local optimal weights, optimal weights and their mean returns by the time intervals from one to ten days. The average results in this period are listed in the table II.

The average results show that the local optimal weights are very similar to the one-day results and their corresponding mean returns have the same order, namely
R​(𝐰R)>R​(𝐰H)>R​(𝐰σ)R(\mathbf{w}\_{R})>R(\mathbf{w}\_{H})>R(\mathbf{w}\_{\sigma}) and
R​(𝐰Oc)>R​(𝐰Oi​c)R(\mathbf{w}^{c}\_{O})>R(\mathbf{w}^{ic}\_{O}). The standard errors for different
time intervals from 1 to 10 days are around 0.016∼0.0330.016\sim 0.033, which implies
that the time intervals in the short periods are not very sensitive for our
predictions.

The (R,σ,H)(R,\sigma,H) model provides an efficient way to find out the local and global
optimal investing schemes for different style investors, conservative and aggressive
investors. In principle the triangle based on the local optimal weights
can be regarded a quasi-optimal subspace for investors, which provides a various
portfolio for investors. The centroid or incenter of the triangle can be regarded as
the optimal portfolio, which balance the mean return, the arbitrary or risk premium and
volatility risk.

## 5 Conclusions

There have been many evidences demonstrating the practical economic system, such as
the stock market, deviates the efficient market hypothesis (EMH), which induces
two fundamental issues. How do we avoid the risk or gain the arbitrary or risk premium
in finance markets? We propose the triplet (R,σ,H)(R,\sigma,H) theory to give the local and global optimal portfolio, which generalize from the (R,σ)(R,\sigma) model.[[11](https://arxiv.org/html/2601.00281v1#bib.bib11)]
We give the formulation to give the Pareto optimal solution and compare
it with numerical investigations for the Chinese stock market to demonstrate the validity of
this formulation. Based on this theory we define the local optimal weights of the triplet (𝐰R,𝐰H,𝐰σ)(\mathbf{w}\_{R},\mathbf{w}\_{H},\mathbf{w}\_{\sigma}), which consist of
the triangle of the quasi-optimal investing subspace such that we give the
global optimal solution of this triplet game, centroid of the triangle or the incenter of the triangle as the optimal investing weights, which optimizes the mean return, the arbitrary or risk premium with a small volatility risk.

The theory provides an efficient way to design the portfolio for different style investors, conservative or aggressive investors, in finance market to maximize the mean return with
a relative small volatility risk. This idea could be generalize to other economic systems to find out the Pareto solution.

## 6 Appendices

### 6.1 Hurst exponent

Hurst exponent is introduced by Hurst to describe the fractal Brownian motion and stochastic time series as well as their long-term correlation. Hurst exponent is within three different regions:

(1) 0<H<0.50<H<0.5 means that the stochastic time series is anti-persistency, namely the past and future series are negative correlation. The sequence contains a sudden reversal property.

(2) H=0.5H=0.5 means that the time series follows independent stochastic distribution, namely the standard Brownian motion. The past and future series are independent.

(3) H<0.5<1H<0.5<1 means that the time series is persistency, namely the past and future series are positive correlation.

### 6.2 Calculating method of Hurst exponent

In general the Hurst exponent of the time series can be calculated by the Rescale Range Analysis (R/S) or the Detrended Fluctuation Analysis (DFA). Here we use the DFA method to calculate Hurst exponent.

For a time series x:={x​(τk)}x:=\{x(\tau\_{k})\}, where τk=tk−tk−1\tau\_{k}=t\_{k}-t\_{k-1} and k=1,2,…,Mk=1,2,...,M. The procedure of calculating Hurst exponent contains 5 steps.

(1) Construct a mean variance series X​(j)X(j) based on {x​(τk)}\{x(\tau\_{k})\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | X​(j)=∑k=1j[x​(τk)−⟨x⟩]X(j)=\sum\_{k=1}^{j}[x(\tau\_{k})-\langle x\rangle] |  | (34) |

where j=1,2,…​Mj=1,2,...M and ⟨x​(τk)⟩=1M​∑k=1Mx​(τk)\langle x(\tau\_{k})\rangle=\frac{1}{M}\sum\_{k=1}^{M}x(\tau\_{k}).

(2) Divide the series X​(t)X(t) into MsM\_{s} non overlapping subsequences, where Ms=i​n​t​[M/s]M\_{s}=int[M/s]. When MM is big enough, we can ignore the remainder.

(3) Calculate the detrended fluctuation function for every subsequences

|  |  |  |  |
| --- | --- | --- | --- |
|  | fν​(s)=1s​∑k=1s{Xν​[(ν−1)​s+k]−Xν​(k)}2f\_{\nu}(s)=\frac{1}{s}\sum\_{k=1}^{s}\left\{X\_{\nu}\left[(\nu-1)s+k\right]-X\_{\nu}(k)\right\}^{2} |  | (35) |

Where ν=1,2,…​Ns\nu=1,2,...N\_{s}. XνX\_{\nu} is the λ\lambda-order polynomial fitting function of subsequence ν\nu by the least square method. Thus, we call this D​F​A−λDFA-\lambda.

(4) The D​F​A−λDFA-\lambda fluctuation function is the mean square root of all subsequences detrended fluctuation function

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(s)=(1Ns​∑ν=1Nsfν​(s))1/2F(s)=\left(\frac{1}{N\_{s}}\sum\_{\nu=1}^{N\_{s}}f\_{\nu}(s)\right)^{1/2} |  | (36) |

(5) Calculating F​(s)F(s) for given different ss, which satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(s)=C​sHF(s)=Cs^{H} |  | (37) |

where CC is a constant. Plotting log⁡(F​(s)/C)\log(F(s)/C) versus log⁡(s)\log(s) by the double logarithmic axes.
The slope of log⁡(F​(s)/C)\log(F(s)/C) versus log⁡(s)\log(s) is Hurst exponent.
The Hurst exponent can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H=log⁡(F​(s)/C)log⁡sH=\frac{\log(F(s)/C)}{\log s} |  | (38) |

Therefore Hurst exponent can be an index describing the environment of the stochastic time series. When H>0.5H>0.5, the environment shows a tendency, which implies that investors could earn the speculate premium by using the trend following strategy like the momentum trading strategy. When H<0.5H<0.5, the environment oscillates, which implies that investors could use the trend reversal strategy like contrarian trading strategy to optimize their returns. The Hurst exponent plays a signal role to indicate the arbitrary premium. Many practical investigations demonstrate that the Hurst exponent of Chinese stock index sequences is approximately 0.60.6,[[14](https://arxiv.org/html/2601.00281v1#bib.bib14), [15](https://arxiv.org/html/2601.00281v1#bib.bib15)] which implies there exists chance to gain the arbitrary premium from the Chinese stock market.

## References

* [1]

  F. M. De Bondt, R. Thaler. Does the stock market overreat? TheJournal of Finance,
  40(3),793-805(1985)¡£
* [2]

  T. Loughran, J. R. Ritter. The new issues puzzle. The Journal of Finance, 50(1),
  23-51(1995).
* [3]

  N.-F. Chen, R. Roll and S. A. Ross. Economic forces and the stock market. The Journal of
  business, 59(3) 383-403(1986).
* [4]

  ANTEGNA R N, STANLEY H E. Scaling behavior in the dynamics of an economic index[J]. Nature, 376 46-49(1995) .
* [5]

  E. E. Peters. Fractal market analysis: applying chaos theory to investment and economics. A Wiley Finance Edition, 39-53(1994).
* [6]

  N. Jegadeesh, S. Titman. Profitability of momentum strategies: an evaluation of alternati-
  ve explanations. The Journal of Finance, 56(2) 699-720(2001).
* [7]

  W. R. Gebhardt, S. Hvidkjaer and B. Swaminathan. Stock and bond market interaction: Does
  Momentum spill over? Journal ofFinancial Economics, 75(3) 651-690(2005).
* [8]

  M. E. Drew. Do momentum strategies work? Australian evidence. Managerial Finance,
  33(10),772-787 (2007).
* [9]

  Wei Chen, Shinong Wu. Studies of long-term memory on Chinese stock markets. CONTEMPORARAY FINANCE and ECONOMICS, 24(6), 49-51(2003).
* [10]

  Hongbin Gao, Jin Pan, Hongmin, Chen. Volatility’s Hurst expoment of Chinese security markets[J]. Journal of Donghua University , 27(4), 22-25(2001).
* [11]

  Markowitz, H.M. March, ”Portfolio Selection”. The Journal of Finance. 7 (1), 77-91(1952).
* [12]

  Peters E E. Fractal Maket Analysis: Applying Chaos Theory to Investment and Economics[M].
  Hoboken,HJ: Wiley-Blackwell, (1994).
* [13]

  PETERS E E. Chaos and order in the Capital Markets: A New View of Cycles, Prices, and
  Market Volatility[M]. Hoboken,HJ: Wiley-Blackwell, (1996).
* [14]

  Yongdong Shi, Yonggang Zhao, Chinese stock markets’fractal structural-Practical studies on stocks’long term memory.[J]. Mathematics in Practice and Theory, 09(2006).
* [15]

  Guowen Han, Haibo, Han. Fractal market theory and practical analysis on Chinese security market. Journal of Beijing Jiaotong University, 01(2008).
* [16]

  Jack Clark Francis, Dongcheol Kim, Modern Portfolio Theory: Foundations, Analysis, and
  New Developments, John Wiley and Sons Inc, (2013).