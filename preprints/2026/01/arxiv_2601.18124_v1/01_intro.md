---
authors:
- Steven E. Pav
doc_id: arxiv:2601.18124v1
family_id: arxiv:2601.18124
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: The Sherman-Morrison-Markowitz Portfolio
url_abs: http://arxiv.org/abs/2601.18124v1
url_html: https://arxiv.org/html/2601.18124v1
venue: arXiv q-fin
version: 1
year: 2026
---


Steven E. Pav
[steven@gilgamath.com](mailto:steven@gilgamath.com)

###### Abstract

We show that the Markowitz portfolio is a scalar multiple of another portfolio which replaces the covariance with the second moment matrix,
via simple application of the Sherman-Morrison identity.
Moreover it is shown that when using conditional estimates of the first two moments, this “Sherman-Morrison-Markowitz” portfolio
solves the standard unconditional portfolio optimization problems.
We argue that in multi-period portfolio optimization problems it is more natural to replace variance and covariance with
their uncentered counterparts.
We extend the theory to deal with constraints in expectation, where we find a decomposition of squared effects into
spanned and orthogonal components.
Compared to the Markowitz portfolio, the Sherman-Morrison-Markowitz portfolio down-levers by a small amount that depends on the conditional squared maximal Sharpe ratio;
the practical impact will be fairly small, however.
We present some example use cases for the theory.

## 1 Introduction

The Markowitz portfolio plays a central role in the theory of quantitative portfolio management, as it solves several varieties of portfolio
optimization problems.
[[10](https://arxiv.org/html/2601.18124v1#bib.bib25 "Portfolio selection"), [16](https://arxiv.org/html/2601.18124v1#bib.bib21 "Statistics and Finance: An Introduction")]
Yet despite the theoretical backing, the Markowitz portfolio has limited practical reach, largely due to estimation error.
[[11](https://arxiv.org/html/2601.18124v1#bib.bib8 "The Markowitz optimization enigma: is ‘optimized’ optimal?"), [5](https://arxiv.org/html/2601.18124v1#bib.bib22 "Optimal versus naive diversification: how inefficient is the 1/N portfolio strategy?"), [13](https://arxiv.org/html/2601.18124v1#bib.bib10 "Bounds on portfolio quality")]
Real world portfolio optimization also usually imposes constraints which do not admit closed form solutions,
leading to a gap in the theoretical understanding of practical portfolio construction methodology.

The Markowitz portfolio solves both the Sharpe maximization and mean-variance optimization problems in the single period model of investment.
In this note we consider the multi-period (or “intertemporal”) variants of these problems,
where one has access to some features upon which one can condition the investment decision.
The objective of the multi-period investment problem is to construct some function from the features to portfolios which optimizes
the unconditional multi-period moments of returns.
The main results of this note are:

1. 1.

   The Markowitz portfolio conditional on the features is not optimal for the multi-period problem, rather a closely related portfolio is.
2. 2.

   The two portfolios are scaled versions of each other, and are connected by the Sherman-Morrison formula for the inverse of a
   rank-one update of a matrix.
3. 3.

   Under the multi-period problem it is more natural to work with the second moment and second moment matrix than the variance
   and covariance matrix.
   Moreover, it is more natural to work with the (squared) Hansen ratio, defined by [Černý](https://arxiv.org/html/2601.18124v1#bib.bib23 "The Hansen ratio in mean–variance portfolio theory") as mean divided by square root of second moment,
   than the Sharpe ratio. [[3](https://arxiv.org/html/2601.18124v1#bib.bib23 "The Hansen ratio in mean–variance portfolio theory")]

Moreover, because of the rescaling property, our “Sherman-Morrison-Markowitz portfolio” is optimal in the single period case as
well, even though the Markowitz portfolio is not optimal in the multi-period case.
We seek to turn portfolio theory not quite upside down, but perhaps sideways, by suggesting that the covariance and variance in
Markowitz portfolio and Sharpe ratio be replaced by their uncentered variants.

The Sherman-Morrison formula relates the inverse of a rank-one update of a matrix to the original matrix inverse. [[6](https://arxiv.org/html/2601.18124v1#bib.bib14 "Updating the Inverse of a Matrix")]
Letting 𝝁\boldsymbol{\mu} and Σ\mathsf{\Sigma} be the expected value and covariance matrix of returns,
this formula implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Σ+𝝁​𝝁⊤)−1​𝝁=11+𝝁⊤​Σ−1​𝝁​Σ−1​𝝁,{{\left(\mathsf{\Sigma}+\boldsymbol{\mu}{\boldsymbol{\mu}}^{\top}\right)}^{-1}}\boldsymbol{\mu}=\frac{1}{1+{\boldsymbol{\mu}}^{\top}{\mathsf{\Sigma}}^{-1}\boldsymbol{\mu}}{\mathsf{\Sigma}}^{-1}\boldsymbol{\mu}, |  | (1) |

which can also be verified by direct multiplication of both sides by the second moment matrix Σ+𝝁​𝝁⊤{\mathsf{\Sigma}+\boldsymbol{\mu}{\boldsymbol{\mu}}^{\top}}.
The vector Σ−1​𝝁{\mathsf{\Sigma}}^{-1}\boldsymbol{\mu} is the Markowitz portfolio, which is usually scaled by some positive constant depending on constraints or
other particulars of the problem at hand, while (Σ+𝝁​𝝁⊤)−1​𝝁{{\left(\mathsf{\Sigma}+\boldsymbol{\mu}{\boldsymbol{\mu}}^{\top}\right)}^{-1}}\boldsymbol{\mu} is the Sherman-Morrison-Markowitz portfolio.
The optimality of the latter comes not from chosing a different portfolio direction for each period, but
rather by downscaling by (1+𝝁⊤​Σ−1​𝝁)−1\left(1+{\boldsymbol{\mu}}^{\top}{\mathsf{\Sigma}}^{-1}\boldsymbol{\mu}\right)^{-1} in each period, compared to the Markowitz portfolio.

In this note we make a number of departures from the typical assumptions of portfolio problems.
For one we discard the assumption of a fully invested portfolio, the so-called “self-financing condition”;
one can view our problem as an optimization over risky assets while the remainder of one’s wealth, long or short,
is implicitly invested in the risk-free asset.

Secondly we focus on maximizing the unconditional, or multi-period, Sharpe ratio, or the multi-period mean-variance objective.
This is somewhat unorthodox among academic papers, but should not be unnatural for practitioners.
Indeed, common practice is to backtest trading systems which make several trading decisions,
then estimate the Sharpe ratio from the entire backtest period.
Investors might ask how such a trading system would perform in some economic crisis in the distant past,
implicitly performing some kind of mental averaging over an entire economic cycle.
Moreover, investors often surrender their capital to fund managers for longer periods than horizon of a a single investment decision,
so managers should be cognizant of the multi-period objective.

Thirdly the constraints that we impose–an overall cap on unconditional risk, hedging constraints–are couched in terms of
long term expectations, rather than single-period constraints.
These choices were expedient, as they make the math work out neatly, but may be unsatisfactory since they can violate
risk constraints in the single period problem.
The conditional constrants can be achieved by assuming a set of basis portfolio functions.
However, our exposition can only handle the case where that set is finite;
further work is required for the case of an infinite set of basis functions.

## 2 Unconditional Sharpe Maximization

Let 𝒚t{\boldsymbol{y}}\_{t} be a kk-length vector of the (percent) returns of some assets.
Suppose that prior to the investment decision you observe a random ll-vector of “features,” 𝒙t{\boldsymbol{x}}\_{t} which can guide your investment decision.
Let the density of 𝒙t{\boldsymbol{x}}\_{t} be f​(𝒙t)f\left({\boldsymbol{x}}\_{t}\right).
Express the conditional mean and second moment of 𝒚t{\boldsymbol{y}}\_{t}, conditional on 𝒙t{\boldsymbol{x}}\_{t}, as the following functions:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝝁​(𝒙t)\displaystyle\boldsymbol{\mu}\left({\boldsymbol{x}}\_{t}\right) | =dfE⁡[𝒚t|𝒙t],\displaystyle=\_{\operatorname{df}}\operatorname{E}\left[{\boldsymbol{y}}\_{t}\left|\,{\boldsymbol{x}}\_{t}\right.\right], |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖠2​(𝒙t)\displaystyle{\mathsf{A}}\_{2}\left({\boldsymbol{x}}\_{t}\right) | =dfE⁡[𝒚t​𝒚t⊤|𝒙t].\displaystyle=\_{\operatorname{df}}\operatorname{E}\left[{\boldsymbol{y}}\_{t}{\boldsymbol{y}}^{\top}\_{t}\left|\,{\boldsymbol{x}}\_{t}\right.\right]. |  | (3) |

Based on these we define the conditional covariance and optimal Sharpe ratio as the functions

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Σ​(𝒙t)\displaystyle\mathsf{\Sigma}\left({\boldsymbol{x}}\_{t}\right) | =df𝖠2​(𝒙t)−𝝁​(𝒙t)​𝝁⊤​(𝒙t),\displaystyle=\_{\operatorname{df}}{\mathsf{A}}\_{2}\left({\boldsymbol{x}}\_{t}\right)-\boldsymbol{\mu}\left({\boldsymbol{x}}\_{t}\right){{\boldsymbol{\mu}}^{\top}}\left({\boldsymbol{x}}\_{t}\right), |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ζ∗​(𝒙t)\displaystyle{\zeta}\_{\*}\left({\boldsymbol{x}}\_{t}\right) | =df𝝁⊤​(𝒙t)​Σ−1​(𝒙t)​𝝁​(𝒙t).\displaystyle=\_{\operatorname{df}}\sqrt{{{\boldsymbol{\mu}}^{\top}}\left({\boldsymbol{x}}\_{t}\right){\mathsf{\Sigma}}^{-1}\left({\boldsymbol{x}}\_{t}\right)\boldsymbol{\mu}\left({\boldsymbol{x}}\_{t}\right)}. |  | (5) |

Suppose that in response to observing 𝒙t{\boldsymbol{x}}\_{t}, you allocate 𝝂​(𝒙t)\boldsymbol{\nu}\left({\boldsymbol{x}}\_{t}\right) of your wealth into each of the kk assets,
for 𝝂​(⋅)\boldsymbol{\nu}\left(\cdot\right) selected from some set of acceptable functions which takes ℝl\mathbb{R}^{l} to ℝk\mathbb{R}^{k}.
The expected return of your portfolio conditional on observing 𝒙t{\boldsymbol{x}}\_{t} is then 𝝂⊤​(𝒙t)​𝝁​(𝒙t){{\boldsymbol{\nu}}^{\top}}\left({\boldsymbol{x}}\_{t}\right)\boldsymbol{\mu}\left({\boldsymbol{x}}\_{t}\right),
and the conditional expected squared return of your portfolio is 𝝂⊤​(𝒙t)​𝖠2​(𝒙t)​𝝂​(𝒙t){{\boldsymbol{\nu}}^{\top}}\left({\boldsymbol{x}}\_{t}\right){\mathsf{A}}\_{2}\left({\boldsymbol{x}}\_{t}\right)\boldsymbol{\nu}\left({\boldsymbol{x}}\_{t}\right).
The *unconditional* mean return, second moment of return, variance of return and risk
are
defined as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μ​(𝝂)\displaystyle\mu\left(\boldsymbol{\nu}\right) | =df∫𝝁⊤​(𝒙)​𝝂​(𝒙)​f​(𝒙)​d𝒙,\displaystyle=\_{\operatorname{df}}\int{{\boldsymbol{\mu}}^{\top}}\left(\boldsymbol{x}\right)\boldsymbol{\nu}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}, |  | (6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | a2​(𝝂)\displaystyle{{a}\_{2}}\left(\boldsymbol{\nu}\right) | =df∫𝝂⊤​(𝒙)​𝖠2​(𝒙)​𝝂​(𝒙)​f​(𝒙)​d𝒙,\displaystyle=\_{\operatorname{df}}\int{{\boldsymbol{\nu}}^{\top}}\left(\boldsymbol{x}\right){\mathsf{A}}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\nu}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}, |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σ2​(𝝂)\displaystyle\sigma^{2}\left(\boldsymbol{\nu}\right) | =dfa2​(𝝂)−(μ​(𝝂))2,\displaystyle=\_{\operatorname{df}}{{a}\_{2}}\left(\boldsymbol{\nu}\right)-\left(\mu\left(\boldsymbol{\nu}\right)\right)^{2}, |  | (8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σ​(𝝂)\displaystyle\sigma\left(\boldsymbol{\nu}\right) | =dfσ2​(𝝂).\displaystyle=\_{\operatorname{df}}\sqrt{\sigma^{2}\left(\boldsymbol{\nu}\right)}. |  | (9) |

Note that these functionals are homogeneous of certain degree.
That is for scalar cc define c⋅𝝂c\cdot\boldsymbol{\nu} as the function 𝝂\boldsymbol{\nu} scaled by cc:

|  |  |  |
| --- | --- | --- |
|  | (c⋅𝝂)​(𝒙t)=c​𝝂​(𝒙t).\left(c\cdot\boldsymbol{\nu}\right)\left({\boldsymbol{x}}\_{t}\right)=c\boldsymbol{\nu}\left({\boldsymbol{x}}\_{t}\right). |  |

We can think of c⋅𝝂c\cdot\boldsymbol{\nu} as the allocation 𝝂\boldsymbol{\nu} scaled up (or down) by cc.
Then for scalar cc we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | μ​(c⋅𝝂)\displaystyle\mu\left(c\cdot\boldsymbol{\nu}\right) | =c​μ​(𝝂),\displaystyle=c\mu\left(\boldsymbol{\nu}\right), | a2​(c⋅𝝂)\displaystyle{{a}\_{2}}\left(c\cdot\boldsymbol{\nu}\right) | =c2​a2​(𝝂),\displaystyle=c^{2}{{a}\_{2}}\left(\boldsymbol{\nu}\right), |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | σ2​(c⋅𝝂)\displaystyle\sigma^{2}\left(c\cdot\boldsymbol{\nu}\right) | =c2​σ2​(𝝂),\displaystyle=c^{2}\sigma^{2}\left(\boldsymbol{\nu}\right), | σ​(c⋅𝝂)\displaystyle\sigma\left(c\cdot\boldsymbol{\nu}\right) | =|c|​σ​(𝝂).\displaystyle=\left|c\right|\sigma\left(\boldsymbol{\nu}\right). |  |

We are interested portfolio functions 𝝂​(𝒙t)\boldsymbol{\nu}\left({\boldsymbol{x}}\_{t}\right) which maximize the Sharpe ratio (μ​(𝝂)−r0)/σ​(𝝂),\left(\mu\left(\boldsymbol{\nu}\right)-{{r}\_{0}}\right)/{\sigma\left(\boldsymbol{\nu}\right)},
for some risk-free rate r0{{r}\_{0}}, or which maximize the mean-variance objective

|  |  |  |
| --- | --- | --- |
|  | ψγ​(𝝂)=dfμ​(𝝂)−γ2​σ2​(𝝂),{\psi}\_{\gamma}\left(\boldsymbol{\nu}\right)=\_{\operatorname{df}}\mu\left(\boldsymbol{\nu}\right)-\frac{\gamma}{2}\sigma^{2}\left(\boldsymbol{\nu}\right), |  |

for some risk intolerance γ>0\gamma>0.
We define the Sharpe ratio functional for zero risk-free rate as

|  |  |  |
| --- | --- | --- |
|  | ζ​(𝝂)=dfμ​(𝝂)σ​(𝝂),\zeta\left(\boldsymbol{\nu}\right)=\_{\operatorname{df}}\frac{\mu\left(\boldsymbol{\nu}\right)}{\sigma\left(\boldsymbol{\nu}\right)}, |  |

which is positively homogeneous of degree zero.
That is, ζ​(c⋅𝝂)=sign⁡(c)​ζ​(𝝂)\zeta\left(c\cdot\boldsymbol{\nu}\right)=\operatorname{sign}\left(c\right)\zeta\left(\boldsymbol{\nu}\right).
The mean variance objective ψγ​(𝝂){\psi}\_{\gamma}\left(\boldsymbol{\nu}\right) is not homogeneous,
which indicates that γ\gamma is not unitless, and may depend on the investment horizon.

We consider portfolio functions which are members of L2{L}^{2}, which is defined as the set of of
𝝂​(𝒙)\boldsymbol{\nu}\left(\boldsymbol{x}\right) such that

|  |  |  |
| --- | --- | --- |
|  | ∫𝝂⊤​(𝒙)​𝝂​(𝒙)​f​(𝒙)​d𝒙<∞\int{{\boldsymbol{\nu}}^{\top}}\left(\boldsymbol{x}\right)\boldsymbol{\nu}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}<\infty |  |

Moreover, we will assume that 𝝂\boldsymbol{\nu} are drawn from some positive cone 𝒞⊆L2\mathcal{C}\subseteq{L}^{2}.
A positive cone is a set of functions such that if 𝝂∈𝒞\boldsymbol{\nu}\in\mathcal{C} then
c⋅𝝂∈𝒞c\cdot\boldsymbol{\nu}\in\mathcal{C} for every positive constant cc.
In the most generic setting 𝒞\mathcal{C} will be L2{L}^{2} itself, but we consider portfolio constraints in the sequel
where 𝒞\mathcal{C} is some set of acceptable allocations.

Now for r0≥0{{r}\_{0}}\geq 0 and R>0R>0 consider the Sharpe ratio optimization problem with a risk budget:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈𝒞:σ​(𝝂)≤R⁡μ​(𝝂)−r0σ​(𝝂).\max\_{\boldsymbol{\nu}\in\mathcal{C}\,:\,\sigma\left(\boldsymbol{\nu}\right)\leq R}\frac{\mu\left(\boldsymbol{\nu}\right)-{{r}\_{0}}}{\sigma\left(\boldsymbol{\nu}\right)}. |  | (10) |

Here r0{{r}\_{0}} is the risk-free rate, and RR is the maximum allowable risk.
By a series of transformations we aim to show that the solution to this optimization problem
is related to the solution of the following problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈𝒞:a2​(𝝂)=1⁡μ​(𝝂).\max\_{\boldsymbol{\nu}\in\mathcal{C}\,:\,{{a}\_{2}}\left(\boldsymbol{\nu}\right)=1}\mu\left(\boldsymbol{\nu}\right). |  | (11) |

By “related to” we mean that one can rescale a solution to Problem [11](https://arxiv.org/html/2601.18124v1#S2.E11 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") in a formulaic
way by a positive scalar to arrive at a solution to Problem [10](https://arxiv.org/html/2601.18124v1#S2.E10 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"), thus one can instead focus on the latter problem.

First we show that any solution to Problem [10](https://arxiv.org/html/2601.18124v1#S2.E10 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") will saturate the risk budget if r0>0{{r}\_{0}}>0.
If r0=0{{r}\_{0}}=0, then a solution to Problem [10](https://arxiv.org/html/2601.18124v1#S2.E10 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") can be positively rescaled to saturate the risk
budget without changing the objective, and thus we can replace that problem with the equivalent problem,

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈𝒞:σ​(𝝂)=R⁡μ​(𝝂)−r0σ​(𝝂).\max\_{\boldsymbol{\nu}\in\mathcal{C}\,:\,\sigma\left(\boldsymbol{\nu}\right)=R}\frac{\mu\left(\boldsymbol{\nu}\right)-{{r}\_{0}}}{\sigma\left(\boldsymbol{\nu}\right)}. |  | (12) |

Towards a contradiction, let 𝝂∗{{\boldsymbol{\nu}}\_{{}\*}} optimize Problem [10](https://arxiv.org/html/2601.18124v1#S2.E10 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"), but suppose that
σ​(𝝂∗)<R\sigma\left({{\boldsymbol{\nu}}\_{{}\*}}\right)<R.
Then there is scalar c=1+λc=1+\lambda with λ>0\lambda>0 such that
σ​((1+λ)⋅𝝂∗)=R\sigma\left(\left(1+\lambda\right)\cdot{{\boldsymbol{\nu}}\_{{}\*}}\right)=R.
But then, using homogeneity

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​((1+λ)⋅𝝂∗)−r0σ​((1+λ)⋅𝝂∗)\displaystyle\frac{\mu\left(\left(1+\lambda\right)\cdot{{\boldsymbol{\nu}}\_{{}\*}}\right)-{{r}\_{0}}}{\sigma\left(\left(1+\lambda\right)\cdot{{\boldsymbol{\nu}}\_{{}\*}}\right)} | =(1+λ)​μ​(𝝂∗)−r0(1+λ)​σ​(𝝂∗)\displaystyle=\frac{\left(1+\lambda\right)\mu\left({{\boldsymbol{\nu}}\_{{}\*}}\right)-{{r}\_{0}}}{\left(1+\lambda\right)\sigma\left({{\boldsymbol{\nu}}\_{{}\*}}\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1+λ)​μ​(𝝂∗)−(1+λ)​r0+λ​r0(1+λ)​σ​(𝝂∗)\displaystyle=\frac{\left(1+\lambda\right)\mu\left({{\boldsymbol{\nu}}\_{{}\*}}\right)-\left(1+\lambda\right){{r}\_{0}}+\lambda{{r}\_{0}}}{\left(1+\lambda\right)\sigma\left({{\boldsymbol{\nu}}\_{{}\*}}\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =μ​(𝝂∗)−r0σ​(𝝂∗)+λ​r0(1+λ)​σ​(𝝂∗).\displaystyle=\frac{\mu\left({{\boldsymbol{\nu}}\_{{}\*}}\right)-{{r}\_{0}}}{\sigma\left({{\boldsymbol{\nu}}\_{{}\*}}\right)}+\frac{\lambda{{r}\_{0}}}{\left(1+\lambda\right)\sigma\left({{\boldsymbol{\nu}}\_{{}\*}}\right)}. |  |

Now this is at least equal to the objective of 𝝂∗{{\boldsymbol{\nu}}\_{{}\*}} and strictly greater than it if r0>0{{r}\_{0}}>0.
This would be a contradiction to the optimality of 𝝂∗{{\boldsymbol{\nu}}\_{{}\*}} if r0>0{{r}\_{0}}>0, and otherwise establishes that we can,
without loss of generality when r0=0{{r}\_{0}}=0, solve Problem [12](https://arxiv.org/html/2601.18124v1#S2.E12 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") instead.

But with the risk budget saturated, trivially we can rewrite that optimization problem as

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈𝒞:σ​(𝝂)=R⁡μ​(𝝂)−r0R.\max\_{\boldsymbol{\nu}\in\mathcal{C}\,:\,\sigma\left(\boldsymbol{\nu}\right)=R}\frac{\mu\left(\boldsymbol{\nu}\right)-{{r}\_{0}}}{R}. |  | (13) |

Given that RR is fixed and positive, it suffices to instead solve the problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈𝒞:σ​(𝝂)=R⁡μ​(𝝂).\max\_{\boldsymbol{\nu}\in\mathcal{C}\,:\,\sigma\left(\boldsymbol{\nu}\right)=R}\mu\left(\boldsymbol{\nu}\right). |  | (14) |

Because this optimization saturates the risk budget, we can shift it to the denominator of the objective
to arrive at the equivalent problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈𝒞:σ​(𝝂)=R⁡μ​(𝝂)σ​(𝝂).\max\_{\boldsymbol{\nu}\in\mathcal{C}\,:\,\sigma\left(\boldsymbol{\nu}\right)=R}\frac{\mu\left(\boldsymbol{\nu}\right)}{\sigma\left(\boldsymbol{\nu}\right)}. |  | (15) |

Now consider the following diagram, where cc is some positive scalar:

σ​(𝝂)\sigma\left(\boldsymbol{\nu}\right)μ​(𝝂)\mu\left(\boldsymbol{\nu}\right)a2​(𝝂)\sqrt{{{a}\_{2}}\left(\boldsymbol{\nu}\right)}θ\thetaσ​(c⋅𝝂)\sigma\left(c\cdot\boldsymbol{\nu}\right)μ​(c⋅𝝂)\mu\left(c\cdot\boldsymbol{\nu}\right)a2​(c⋅𝝂)\sqrt{{{a}\_{2}}\left(c\cdot\boldsymbol{\nu}\right)}θ\theta

Problem [15](https://arxiv.org/html/2601.18124v1#S2.E15 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") requires us to find the 𝝂\boldsymbol{\nu} that maximizes the tangent of θ\theta,
equivalently that maximizes θ\theta, subject to an equality constraint on the horizontal leg.
However, it is easily seen that to solve that problem it suffices to maximize θ\theta subject
to any other equality constraint that is positively homogeneous of degree 1, then rescale the result.
That is, to solve Problem [15](https://arxiv.org/html/2601.18124v1#S2.E15 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") it suffices to instead solve

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈𝒞:a2​(𝝂)=1⁡μ​(𝝂),\max\_{\boldsymbol{\nu}\in\mathcal{C}\,:\,{{a}\_{2}}\left(\boldsymbol{\nu}\right)=1}\mu\left(\boldsymbol{\nu}\right), |  | (16) |

and rescale the optimal portfolio function to achieve the requisite equality constraint.

We sketch the proof for any skeptics:
let 𝝂∗{{\boldsymbol{\nu}}\_{{}\*}} be a solution to Problem [16](https://arxiv.org/html/2601.18124v1#S2.E16 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"), then consider scalar cc such that

|  |  |  |
| --- | --- | --- |
|  | σ​(c⋅𝝂∗)=R.\sigma\left(c\cdot{{\boldsymbol{\nu}}\_{{}\*}}\right)=R. |  |

Now suppose 𝝂1{{\boldsymbol{\nu}}\_{1}} is some other portfolio such that
σ​(𝝂1)=R\sigma\left({{\boldsymbol{\nu}}\_{1}}\right)=R, but which gives strictly larger expected return:

|  |  |  |
| --- | --- | --- |
|  | μ​(𝝂1)>μ​(c⋅𝝂∗).\mu\left({{\boldsymbol{\nu}}\_{1}}\right)>\mu\left(c\cdot{{\boldsymbol{\nu}}\_{{}\*}}\right). |  |

Now

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(c⋅𝝂∗)\displaystyle\sigma^{2}\left(c\cdot{{\boldsymbol{\nu}}\_{{}\*}}\right) | =σ2​(𝝂1),\displaystyle=\sigma^{2}\left({{\boldsymbol{\nu}}\_{1}}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | a2​(c⋅𝝂∗)−(μ​(c⋅𝝂∗))2\displaystyle{{a}\_{2}}\left(c\cdot{{\boldsymbol{\nu}}\_{{}\*}}\right)-\left(\mu\left(c\cdot{{\boldsymbol{\nu}}\_{{}\*}}\right)\right)^{2} | =a2​(𝝂1)−(μ​(𝝂1))2,\displaystyle={{a}\_{2}}\left({{\boldsymbol{\nu}}\_{1}}\right)-\left(\mu\left({{\boldsymbol{\nu}}\_{1}}\right)\right)^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | c2=a2​(c⋅𝝂∗)\displaystyle c^{2}={{a}\_{2}}\left(c\cdot{{\boldsymbol{\nu}}\_{{}\*}}\right) | >a2​(𝝂1),\displaystyle>{{a}\_{2}}\left({{\boldsymbol{\nu}}\_{1}}\right), |  |

where the last inequality follows from the inequality on means.
Thus there is some k>c−1k>c^{-1} such that a2​(k​𝝂1)=1{{a}\_{2}}\left(k{{\boldsymbol{\nu}}\_{1}}\right)=1.
But then μ​(k​𝝂1)=k​μ​(𝝂1)>c−1​μ​(c⋅𝝂∗)=μ​(𝝂∗),\mu\left(k{{\boldsymbol{\nu}}\_{1}}\right)=k\mu\left({{\boldsymbol{\nu}}\_{1}}\right)>c^{-1}\mu\left(c\cdot{{\boldsymbol{\nu}}\_{{}\*}}\right)=\mu\left({{\boldsymbol{\nu}}\_{{}\*}}\right),
which is a contradiction to 𝝂∗{{\boldsymbol{\nu}}\_{{}\*}} solving Problem [16](https://arxiv.org/html/2601.18124v1#S2.E16 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").
Thus c⋅𝝂∗c\cdot{{\boldsymbol{\nu}}\_{{}\*}} must be a solution to Problem [15](https://arxiv.org/html/2601.18124v1#S2.E15 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").

The reverse implication follows similarly, establishing an equivalence between Problem [16](https://arxiv.org/html/2601.18124v1#S2.E16 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") and
Problem [15](https://arxiv.org/html/2601.18124v1#S2.E15 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"), up to scaling by some constant.
Moreover, this shows that to solve Problem [10](https://arxiv.org/html/2601.18124v1#S2.E10 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"), it suffices to solve Problem [16](https://arxiv.org/html/2601.18124v1#S2.E16 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") and rescale
the portfolio to saturate the risk constraint.

### 2.1 Unconstrained Case

We now consider solutions to Problem [16](https://arxiv.org/html/2601.18124v1#S2.E16 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") when 𝒞\mathcal{C} is the entire space of square-integrable functions.
Without the cone constraint, this
is an example of an *isoperimetric problem*. [[8](https://arxiv.org/html/2601.18124v1#bib.bib24 "Calculus of variations: mechanics, control, and other applications")]
That is, we can write it as

|  |  |  |
| --- | --- | --- |
|  | max𝝂​(𝒙)​∫L​(𝒙,𝝂)​d𝒙s.t.∫M​(𝒙,𝝂)​d𝒙=1,\max\_{\boldsymbol{\nu}\left(\boldsymbol{x}\right)}\int L\left(\boldsymbol{x},\boldsymbol{\nu}\right)\,\mathrm{d}{\boldsymbol{x}}\quad\mbox{s.t.}\quad\int M\left(\boldsymbol{x},\boldsymbol{\nu}\right)\,\mathrm{d}{\boldsymbol{x}}=1, |  |

for certain functions LL and MM.
To be specific

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(𝒙,𝝂)\displaystyle L\left(\boldsymbol{x},\boldsymbol{\nu}\right) | =𝝂⊤​𝝁​(𝒙)​f​(𝒙),\displaystyle={{\boldsymbol{\nu}}^{\top}}\boldsymbol{\mu}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | M​(𝒙,𝝂)\displaystyle M\left(\boldsymbol{x},\boldsymbol{\nu}\right) | =𝝂⊤​𝖠2​(𝒙)​𝝂​f​(𝒙).\displaystyle={{\boldsymbol{\nu}}^{\top}}{\mathsf{A}}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\nu}f\left(\boldsymbol{x}\right). |  |

These functions have no dependence on the gradient of 𝝂\boldsymbol{\nu}, which makes them atypical of problems in the calculus of
variations,
and the solution to our problem is relatively simple.
A necessary condition for a solution 𝝂​(𝒙t)\boldsymbol{\nu}\left({\boldsymbol{x}}\_{t}\right) is that either MM satisfies the Euler-Lagrange equation,
or for some λ\lambda the linear combination N=L+λ​MN=L+\lambda M satisfies the Euler-Lagrange equation.
Without any dependence on the gradient of 𝝂\boldsymbol{\nu} the Euler-Lagrange equation reduces to what looks like a typical elementary
calculus necessary condition for an optimum, namely at a solution either

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇𝝂M=𝟎,or∇𝝂N=𝟎.{{\nabla}\_{\boldsymbol{\nu}}}M=\boldsymbol{0},\quad\mbox{or}\quad{{\nabla}\_{\boldsymbol{\nu}}}N=\boldsymbol{0}. |  | (17) |

Given the definition of the objective and constraint, these reduce to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​𝖠2​(𝒙)​𝝂​(𝒙)​f​(𝒙)=𝟎,or𝝁​(𝒙)​f​(𝒙)+2​λ​𝖠2​(𝒙)​𝝂​(𝒙)​f​(𝒙)=𝟎.2{\mathsf{A}}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\nu}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)=\boldsymbol{0},\quad\mbox{or}\quad\boldsymbol{\mu}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)+2\lambda{\mathsf{A}}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\nu}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)=\boldsymbol{0}. |  | (18) |

We need only describe the behavior of 𝝂​(𝒙)\boldsymbol{\nu}\left(\boldsymbol{x}\right) for the case where f​(𝒙)>0f\left(\boldsymbol{x}\right)>0, as other 𝒙\boldsymbol{x} are
from a set of measure zero.
We follow common convention and state that a predicate holds “almost surely” if it holds for all 𝒙\boldsymbol{x} except
possibly some 𝒙\boldsymbol{x} where f​(𝒙)=0f\left(\boldsymbol{x}\right)=0.

Because the matrix 𝖠2​(𝒙){\mathsf{A}}\_{2}\left(\boldsymbol{x}\right) is a positive definite matrix, the first equation cannot hold unless
𝝂​(𝒙)=𝟎\boldsymbol{\nu}\left(\boldsymbol{x}\right)=\boldsymbol{0} almost surely.
This would not satisfy the constraint, so we can ignore this possibility and can focus on the second equation, which reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝂​(𝒙)=c​𝖠2−1​(𝒙)​𝝁​(𝒙),\boldsymbol{\nu}\left(\boldsymbol{x}\right)=c{\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right), |  | (19) |

for some constant cc, almost surely. The risk constraint of Problem [12](https://arxiv.org/html/2601.18124v1#S2.E12 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") will fix the value of cc as

|  |  |  |
| --- | --- | --- |
|  | c=Rq−q2,whereq=df∫𝝁⊤​(𝒙)​𝖠2−1​(𝒙)​𝝁​(𝒙)​f​(𝒙)​d𝒙.c=\frac{R}{\sqrt{q-{q}^{2}}},\quad\mbox{where}\quad q=\_{\operatorname{df}}\int{{\boldsymbol{\mu}}^{\top}}\left(\boldsymbol{x}\right){\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}. |  |

As discussed laster, q1/2{q}^{1/2} is the (unconditional) Hansen ratio of the optimal portfolio allocation.

Thus we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝂∗​(𝒙)=dfRq−q2​𝖠2−1​(𝒙)​𝝁​(𝒙)a.s.{{\boldsymbol{\nu}}\_{{}\*}}\left(\boldsymbol{x}\right)=\_{\operatorname{df}}\frac{R}{\sqrt{q-{q}^{2}}}{\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right)\quad\mbox{a.s.} |  | (20) |

We are assuming that 𝖠2−1​(𝒙)​𝝁​(𝒙)∈L2{\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right)\in{L}^{2}, which will require that 𝖠2​(𝒙){\mathsf{A}}\_{2}\left(\boldsymbol{x}\right) have strictly positive eigenvalues, almost surely.
For this choice of portfolio function we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | μ​(𝝂∗)\displaystyle\mu\left({{\boldsymbol{\nu}}\_{{}\*}}\right) | =R​q1−q,\displaystyle=R\sqrt{\frac{q}{1-q}}, | a2​(𝝂∗)\displaystyle{{a}\_{2}}\left({{\boldsymbol{\nu}}\_{{}\*}}\right) | =R2​11−q,\displaystyle=R^{2}\frac{1}{1-q}, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | σ2​(𝝂∗)\displaystyle\sigma^{2}\left({{\boldsymbol{\nu}}\_{{}\*}}\right) | =R2,\displaystyle=R^{2}, | σ​(𝝂∗)\displaystyle\sigma\left({{\boldsymbol{\nu}}\_{{}\*}}\right) | =R.\displaystyle=R. |  |

The objective takes optimal value

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μ​(𝝂∗)−r0σ​(𝝂∗)\displaystyle\frac{\mu\left({{\boldsymbol{\nu}}\_{{}\*}}\right)-{{r}\_{0}}}{\sigma\left({{\boldsymbol{\nu}}\_{{}\*}}\right)} | =q1−q−r0R.\displaystyle=\sqrt{\frac{q}{1-q}}-\frac{{{r}\_{0}}}{R}. |  | (21) |

#### 2.1.1 Hansen Ratio

[Černý](https://arxiv.org/html/2601.18124v1#bib.bib23 "The Hansen ratio in mean–variance portfolio theory") defined the Hansen ratio as the mean return of a strategy divided by the square root of the second
moment of returns. [[3](https://arxiv.org/html/2601.18124v1#bib.bib23 "The Hansen ratio in mean–variance portfolio theory")]
For our multi-period problem this is written as μ​(𝝂)/a2​(𝝂){\mu\left(\boldsymbol{\nu}\right)}/{\sqrt{{{a}\_{2}}\left(\boldsymbol{\nu}\right)}}.
Repeating the diagram from above illustrates the connection between the Sharpe ratio and the Hansen ratio:

σ​(𝝂)\sigma\left(\boldsymbol{\nu}\right)μ​(𝝂)\mu\left(\boldsymbol{\nu}\right)a2​(𝝂)\sqrt{{{a}\_{2}}\left(\boldsymbol{\nu}\right)}θ\theta

With θ\theta the indicated angle of this triangle, the Sharpe ratio of 𝝂\boldsymbol{\nu} is tan⁡θ\tan{\theta} while its Hansen ratio is sin⁡θ\sin{\theta}.
Note that this immediately establishes that the Hansen ratio never exceeds one in absolute value.
To maximize either of these quantities is equivalent to maximizing θ\theta.
Generally speaking when we seek a portfolio which maximizes the Sharpe ratio, we can instead maximize the Hansen ratio.
Then in particular, Problem [10](https://arxiv.org/html/2601.18124v1#S2.E10 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") has the same solution as

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈𝒞:σ​(𝝂)≤R⁡μ​(𝝂)a2​(𝝂).\max\_{\boldsymbol{\nu}\in\mathcal{C}\,:\,\sigma\left(\boldsymbol{\nu}\right)\leq R}\frac{\mu\left(\boldsymbol{\nu}\right)}{\sqrt{{{a}\_{2}}\left(\boldsymbol{\nu}\right)}}. |  | (22) |

The optimal objective of this problem is q1/2{q}^{1/2}.

If ζ\zeta is the Sharpe ratio of a portfolio, and hh is its Hansen ratio then

|  |  |  |
| --- | --- | --- |
|  | ζ=ftas​(h)=h1−h2,andh=ftas−1​(ζ)=ζ1+ζ2.\zeta={{f}\_{\mbox{tas}}}\left(h\right)=\frac{h}{\sqrt{1-h^{2}}},\quad\mbox{and}\quad h={f}^{-1}\_{\mbox{tas}}\left(\zeta\right)=\frac{\zeta}{\sqrt{1+{\zeta}^{2}}}. |  |

Here “tas” stands for “tangent of arcsin”. [[14](https://arxiv.org/html/2601.18124v1#bib.bib19 "The Sharpe ratio: statistics and applications")]

Now rewrite
the Sharpe ratio of the optimal allocation from Equation [21](https://arxiv.org/html/2601.18124v1#S2.E21 "In 2.1 Unconstrained Case ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μ​(𝝂∗)−r0σ​(𝝂∗)\displaystyle\frac{\mu\left({{\boldsymbol{\nu}}\_{{}\*}}\right)-{{r}\_{0}}}{\sigma\left({{\boldsymbol{\nu}}\_{{}\*}}\right)} | =q1−q−r0R=ftas​(q1/2)−r0R.\displaystyle=\sqrt{\frac{q}{1-q}}-\frac{{{r}\_{0}}}{R}={{f}\_{\mbox{tas}}}\left({q}^{1/2}\right)-\frac{{{r}\_{0}}}{R}. |  | (23) |

This establishes that q1/2{q}^{1/2} is the Hansen ratio of the optimal portfolio, under zero risk-free rate.

We note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | q\displaystyle q | =∫𝝁⊤​(𝒙)​𝖠2−1​(𝒙)​𝝁​(𝒙)​f​(𝒙)​d𝒙,\displaystyle=\int{{\boldsymbol{\mu}}^{\top}}\left(\boldsymbol{x}\right){\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E𝒙⁡[𝝁⊤​(𝒙)​𝖠2−1​(𝒙)​𝝁​(𝒙)],\displaystyle={{\operatorname{E}}\_{\boldsymbol{x}}}\left[{{\boldsymbol{\mu}}^{\top}}\left(\boldsymbol{x}\right){\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right)\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E𝒙⁡[𝝁⊤​(𝒙)​Σ−1​(𝒙)​𝝁​(𝒙)1+𝝁⊤​(𝒙)​Σ−1​(𝒙)​𝝁​(𝒙)],\displaystyle={{\operatorname{E}}\_{\boldsymbol{x}}}\left[\frac{{{\boldsymbol{\mu}}^{\top}}\left(\boldsymbol{x}\right){\mathsf{\Sigma}}^{-1}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right)}{1+{{\boldsymbol{\mu}}^{\top}}\left(\boldsymbol{x}\right){\mathsf{\Sigma}}^{-1}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right)}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E𝒙⁡[ζ∗2​(𝒙)1+ζ∗2​(𝒙)],\displaystyle={{\operatorname{E}}\_{\boldsymbol{x}}}\left[\frac{{\zeta}^{2}\_{\*}\left(\boldsymbol{x}\right)}{1+{\zeta}^{2}\_{\*}\left(\boldsymbol{x}\right)}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E𝒙⁡[q​(𝒙)],\displaystyle={{\operatorname{E}}\_{\boldsymbol{x}}}\left[q\left(\boldsymbol{x}\right)\right], |  |

where
we define

|  |  |  |
| --- | --- | --- |
|  | q​(𝒙)=df𝝁⊤​(𝒙)​𝖠2−1​(𝒙)​𝝁​(𝒙)=(ftas−1​(ζ∗​(𝒙)))2.q\left(\boldsymbol{x}\right)=\_{\operatorname{df}}{{\boldsymbol{\mu}}^{\top}}\left(\boldsymbol{x}\right){\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right)=\left({f}^{-1}\_{\mbox{tas}}\left({\zeta}\_{\*}\left(\boldsymbol{x}\right)\right)\right)^{2}. |  |

Thus qq, the squared (unconditional) Hansen ratio of the optimal portfolio is the expectation, over 𝒙\boldsymbol{x},
of the squared conditional Hansen ratio of the optimal conditional portfolio.
Thus the (squared) Hansen ratio aggregates in a very natural way from the conditional to unconditional settings.
On the other hand,
the aggregation of Sharpe ratio (or squared Sharpe ratio) from conditional to unconditional requires transformation by the “tas” function.

### 2.2 Constrained Case

For this section we consider it more convenient to introduce the inner product notation.
For vector-valued functions 𝒈,𝒉∈L2\boldsymbol{g},\boldsymbol{h}\in{L}^{2}, define

|  |  |  |
| --- | --- | --- |
|  | ⟨𝒈,𝒉⟩=∫𝒈⊤​(𝒙)​𝒉​(𝒙)​f​(𝒙)​d𝒙.\langle{\boldsymbol{g}},{\boldsymbol{h}}\rangle=\int{{\boldsymbol{g}}^{\top}}\left(\boldsymbol{x}\right)\boldsymbol{h}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}. |  |

We now consider solutions to Problem [16](https://arxiv.org/html/2601.18124v1#S2.E16 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") where 𝒞\mathcal{C} is the intersection of a number of integral constraints:

|  |  |  |
| --- | --- | --- |
|  | 𝒞={𝝂|⟨𝝂,𝒈j⟩=0,j=1,2,…,J}.\mathcal{C}=\left\{\boldsymbol{\nu}\left|\;{\langle{\boldsymbol{\nu}},{{\boldsymbol{g}}\_{j}}\rangle=0,\,j=1,2,\ldots,J}\right.\right\}. |  |

Here the 𝒈j{\boldsymbol{g}}\_{j} are given portfolio functions which we wish to be orthogonal, in expectation, to our selected portfolio.
Note that via this formulation we can capture things like a zero net dollar constraint
(by taking 𝒈j{\boldsymbol{g}}\_{j} to be the function that is the constant ones vector).
We can also capture *hedging constraints* where we wish to hold a portfolio whose returns have zero covariance
to some other portfolio, say 𝒘\boldsymbol{w}.
The zero covariance constraint is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =⟨𝝂,𝖠2​𝒘⟩−⟨𝝂,𝝁⟩​⟨𝒘,𝝁⟩,\displaystyle=\langle{\boldsymbol{\nu}},{{\mathsf{A}}\_{2}\boldsymbol{w}}\rangle-\langle{\boldsymbol{\nu}},{\boldsymbol{\mu}}\rangle\langle{\boldsymbol{w}},{\boldsymbol{\mu}}\rangle, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨𝝂,𝖠2​𝒘−(⟨𝒘,𝝁⟩)⋅𝝁⟩,\displaystyle=\langle{\boldsymbol{\nu}},{{\mathsf{A}}\_{2}\boldsymbol{w}-\left(\langle{\boldsymbol{w}},{\boldsymbol{\mu}}\rangle\right)\cdot\boldsymbol{\mu}}\rangle, |  |

which is of the requisite form.

Note that these constraints are *in expectation*, and do not hold conditionally.
That is, the “zero net dollar constraint” does not constrain us to portfolio functions with 𝟏⊤​𝝂​(𝒙)=0{\boldsymbol{1}}^{\top}\boldsymbol{\nu}\left(\boldsymbol{x}\right)=0,
but instead the expectation, over 𝒙\boldsymbol{x}, of 𝟏⊤​𝝂​(𝒙){\boldsymbol{1}}^{\top}\boldsymbol{\nu}\left(\boldsymbol{x}\right) is zero.
To get conditional constraints, one needs to further limit the space of acceptable allocation functions to
respect the constraints.

Thus in the constrained case we are seeking to solve the optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈L2⁡⟨𝝂,𝝁⟩s.t.⟨𝝂,𝖠2​𝝂⟩=1,⟨𝝂,𝒈j⟩=0,j=1,2,…,J.\max\_{\boldsymbol{\nu}\in{L}^{2}}\langle{\boldsymbol{\nu}},{\boldsymbol{\mu}}\rangle\quad\mbox{s.t.}\quad\langle{\boldsymbol{\nu}},{{\mathsf{A}}\_{2}\boldsymbol{\nu}}\rangle=1,\,\langle{\boldsymbol{\nu}},{{\boldsymbol{g}}\_{j}}\rangle=0,\,j=1,2,\ldots,J. |  | (24) |

This is still an isoperimetric problem.
The necessary conditions at a solution, as in the unconstrained case,
require that a linear combination of the integrands satisfy the Euler Lagrange equation.
That is

|  |  |  |
| --- | --- | --- |
|  | ∇𝝂N=𝟎,whereN​(𝒙,𝝂)=𝝂⊤​𝝁​(𝒙)​f​(𝒙)+λ0​𝝂⊤​𝖠2​(𝒙)​𝝂​f​(𝒙)+∑jλj​𝝂⊤​𝒈j​(𝒙)​f​(𝒙).{{\nabla}\_{\boldsymbol{\nu}}}N=\boldsymbol{0},\quad\mbox{where}\quad N\left(\boldsymbol{x},\boldsymbol{\nu}\right)={{\boldsymbol{\nu}}^{\top}}\boldsymbol{\mu}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)+\lambda\_{0}{{\boldsymbol{\nu}}^{\top}}{\mathsf{A}}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\nu}f\left(\boldsymbol{x}\right)+\sum\_{j}\lambda\_{j}{{\boldsymbol{\nu}}^{\top}}{{\boldsymbol{g}}\_{j}\left(\boldsymbol{x}\right)}f\left(\boldsymbol{x}\right). |  |

Taking the gradient and
factoring out the density of 𝒙\boldsymbol{x}, the necessary condition is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟎=𝝁​(𝒙)+2​λ0​𝖠2​(𝒙)​𝝂+∑jλj​𝒈j​(𝒙)almost surely.\boldsymbol{0}=\boldsymbol{\mu}\left(\boldsymbol{x}\right)+2\lambda\_{0}{\mathsf{A}}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\nu}+\sum\_{j}\lambda\_{j}{\boldsymbol{g}}\_{j}\left(\boldsymbol{x}\right)\quad\mbox{almost surely.} |  | (25) |

This has solution

|  |  |  |
| --- | --- | --- |
|  | 𝝂∗​(𝒙)=c​𝖠2−1​(𝒙)​(𝝁​(𝒙)+∑jcj​𝒈j​(𝒙)),{{\boldsymbol{\nu}}\_{{}\*}}\left(\boldsymbol{x}\right)=c{\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right)\left(\boldsymbol{\mu}\left(\boldsymbol{x}\right)+\sum\_{j}c\_{j}{\boldsymbol{g}}\_{j}\left(\boldsymbol{x}\right)\right), |  |

where cc is some overall constant which will be set by the risk budget constraint.

For this solution to satisfy the hedging constraints we must further have

|  |  |  |
| --- | --- | --- |
|  | 0=⟨𝒈i,𝝂∗⟩=c​(⟨𝒈i,𝖠2−1​𝝁⟩+∑jcj​⟨𝒈i,𝖠2−1​𝒈j⟩),0=\langle{{\boldsymbol{g}}\_{i}},{{{\boldsymbol{\nu}}\_{{}\*}}}\rangle=c\left(\langle{{\boldsymbol{g}}\_{i}},{{\mathsf{A}}^{-1}\_{2}\boldsymbol{\mu}}\rangle+\sum\_{j}c\_{j}\langle{{\boldsymbol{g}}\_{i}},{{\mathsf{A}}^{-1}\_{2}{\boldsymbol{g}}\_{j}}\rangle\right), |  |

for i=1,2,…,Ji=1,2,\ldots,J.
This imposes JJ equality constraints for the JJ unknowns c1,…,cJc\_{1},\ldots,c\_{J},
since the cc factors out.
This can be expressed as a linear system:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖬​𝒄=𝒃,\mathsf{M}\boldsymbol{c}=\boldsymbol{b}, |  | (26) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖬i,j=⟨𝒈i,𝖠2−1​𝒈j⟩,𝒃i=−⟨𝒈i,𝖠2−1​𝝁⟩.{\mathsf{M}}\_{i,j}=\langle{{\boldsymbol{g}}\_{i}},{{\mathsf{A}}^{-1}\_{2}{\boldsymbol{g}}\_{j}}\rangle,\quad{\boldsymbol{b}}\_{i}=-\langle{{\boldsymbol{g}}\_{i}},{{\mathsf{A}}^{-1}\_{2}\boldsymbol{\mu}}\rangle. |  | (27) |

Now we consider the unconditional first and second moments of this optimal portfolio. These are

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨𝝁,𝝂∗⟩\displaystyle\langle{\boldsymbol{\mu}},{{{\boldsymbol{\nu}}\_{{}\*}}}\rangle | =c​(⟨𝝁,𝖠2−1​𝝁⟩+∑jcj​⟨𝝁,𝖠2−1​𝒈j⟩),\displaystyle=c\left(\langle{\boldsymbol{\mu}},{{\mathsf{A}}^{-1}\_{2}\boldsymbol{\mu}}\rangle+\sum\_{j}c\_{j}\langle{\boldsymbol{\mu}},{{\mathsf{A}}^{-1}\_{2}{\boldsymbol{g}}\_{j}}\rangle\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c​(⟨𝝁,𝖠2−1​𝝁⟩−𝒃⊤​𝖬−1​𝒃),\displaystyle=c\left(\langle{\boldsymbol{\mu}},{{\mathsf{A}}^{-1}\_{2}\boldsymbol{\mu}}\rangle-{{\boldsymbol{b}}^{\top}}{{\mathsf{M}}^{-1}}\boldsymbol{b}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c​qg,\displaystyle=c{q}\_{g}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨𝝂∗,𝖠2​𝝂∗⟩\displaystyle\langle{{{\boldsymbol{\nu}}\_{{}\*}}},{{\mathsf{A}}\_{2}{{\boldsymbol{\nu}}\_{{}\*}}}\rangle | =⟨𝝂∗,c​𝝁+c​∑jcj​𝒈j⟩,\displaystyle=\langle{{{\boldsymbol{\nu}}\_{{}\*}}},{c\boldsymbol{\mu}+c\sum\_{j}c\_{j}{\boldsymbol{g}}\_{j}}\rangle, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c​⟨𝝂∗,𝝁⟩+c​∑jcj​⟨𝝂∗,𝒈j⟩,\displaystyle=c\langle{{{\boldsymbol{\nu}}\_{{}\*}}},{\boldsymbol{\mu}}\rangle+c\sum\_{j}c\_{j}\langle{{{\boldsymbol{\nu}}\_{{}\*}}},{{\boldsymbol{g}}\_{j}}\rangle, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c​⟨𝝂∗,𝝁⟩,\displaystyle=c\langle{{{\boldsymbol{\nu}}\_{{}\*}}},{\boldsymbol{\mu}}\rangle, |  |

because 𝝂∗{{\boldsymbol{\nu}}\_{{}\*}} is orthogonal to all the 𝒈j{\boldsymbol{g}}\_{j}, so the latter sum is over all zeros.
We define qg{q}\_{g} to be the quantity in parentheses above; it corresponds to the optimal squared
Hansen ratio under the given constraints.
To saturate the risk budget we need

|  |  |  |
| --- | --- | --- |
|  | R2=c​⟨𝝂∗,𝝁⟩−⟨𝝂∗,𝝁⟩2=c2​(qg−qg2).R^{2}=c\langle{{{\boldsymbol{\nu}}\_{{}\*}}},{\boldsymbol{\mu}}\rangle-{\langle{{{\boldsymbol{\nu}}\_{{}\*}}},{\boldsymbol{\mu}}\rangle}^{2}=c^{2}\left({q}\_{g}-{q}^{2}\_{g}\right). |  |

This fixes the identity of cc thus we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝂∗=Rqg−qg2​𝖠2−1​(𝝁+∑jcj​𝒈j).{{\boldsymbol{\nu}}\_{{}\*}}=\frac{R}{\sqrt{{q}\_{g}-{q}^{2}\_{g}}}{\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{\mu}+\sum\_{j}c\_{j}{\boldsymbol{g}}\_{j}\right). |  | (28) |

The Sharpe ratio of this portfolio, including the risk-free rate, is

|  |  |  |
| --- | --- | --- |
|  | ⟨𝝂∗,𝝁⟩−r0c​(qg−qg2)=qg1−qg−r0R.\frac{\langle{{{\boldsymbol{\nu}}\_{{}\*}}},{\boldsymbol{\mu}}\rangle-{{r}\_{0}}}{c\sqrt{\left({q}\_{g}-{q}^{2}\_{g}\right)}}=\sqrt{\frac{{q}\_{g}}{1-{q}\_{g}}}-\frac{{{r}\_{0}}}{R}. |  |

Now consider the impact on the squared Hansen ratio from imposing the hedge constraints.
We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | q−qg\displaystyle q-{q}\_{g} | =𝒃⊤​𝖬−1​𝒃.\displaystyle={{\boldsymbol{b}}^{\top}}{{\mathsf{M}}^{-1}}\boldsymbol{b}. |  |

The right hand side can be interpreted as the “loss” in squared Hansen ratio incurred by imposing
the constraints.
We note that it can be interpreted as the squared Hansen ratio of a different constrained optimization problem:
suppose that one optimizes the Sharpe ratio (or Hansen ratio) over portfolios of the form

|  |  |  |
| --- | --- | --- |
|  | 𝝂​(𝒙)=∑jcj​𝖠2−1​(𝒙)​𝒈j​(𝒙).\boldsymbol{\nu}\left(\boldsymbol{x}\right)=\sum\_{j}c\_{j}{\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right){\boldsymbol{g}}\_{j}\left(\boldsymbol{x}\right). |  |

Then the optimal squared Hansen ratio of this portfolio is 𝒃⊤​𝖬−1​𝒃{{\boldsymbol{b}}^{\top}}{{\mathsf{M}}^{-1}}\boldsymbol{b}, as we show in
Section [2.4](https://arxiv.org/html/2601.18124v1#S2.SS4 "2.4 Optimizing Over Basis Portfolios ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").
Thus there is a kind of Pythagorean theorem at work here, where the squared Hansen ratio of the unconditional
optimal portfolio is the sum of the squared Hansen ratios of the two orthogonal optimal portfolios.

#### 2.2.1 Hedging Example

Consider the simple case where there is a single constraint consisting of a portfolio which should be hedged out.
That is, one should have zero covariance against the portfolio 𝒎​(𝒙)\boldsymbol{m}\left(\boldsymbol{x}\right).
As noted above this means

|  |  |  |
| --- | --- | --- |
|  | 𝒈1=𝖠2​𝒎−(⟨𝒎,𝝁⟩)⋅𝝁.{\boldsymbol{g}}\_{1}={{\mathsf{A}}\_{2}\boldsymbol{m}-\left(\langle{\boldsymbol{m}},{\boldsymbol{\mu}}\rangle\right)\cdot\boldsymbol{\mu}}. |  |

To find the constant c1c\_{1} in 𝝂∗{{\boldsymbol{\nu}}\_{{}\*}} we must solve the single equation

|  |  |  |
| --- | --- | --- |
|  | 0=⟨𝒈1,𝖠2−1​𝝁⟩+c1​⟨𝒈1,𝖠2−1​𝒈1⟩,0={\langle{{\boldsymbol{g}}\_{1}},{{\mathsf{A}}^{-1}\_{2}\boldsymbol{\mu}}\rangle+c\_{1}\langle{{\boldsymbol{g}}\_{1}},{{\mathsf{A}}^{-1}\_{2}{\boldsymbol{g}}\_{1}}\rangle}, |  |

or

|  |  |  |  |
| --- | --- | --- | --- |
|  | c1\displaystyle c\_{1} | =−⟨𝒈1,𝖠2−1​𝝁⟩⟨𝒈1,𝖠2−1​𝒈1⟩,\displaystyle=-\frac{\langle{{\boldsymbol{g}}\_{1}},{{\mathsf{A}}^{-1}\_{2}\boldsymbol{\mu}}\rangle}{\langle{{\boldsymbol{g}}\_{1}},{{\mathsf{A}}^{-1}\_{2}{\boldsymbol{g}}\_{1}}\rangle}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−⟨𝒎,𝝁⟩−⟨𝒎,𝝁⟩​⟨𝝁,𝖠2−1​𝝁⟩⟨𝒎,𝖠2​𝒎⟩−2​⟨𝒎,𝝁⟩2+⟨𝒎,𝝁⟩2​⟨𝝁,𝖠2−1​𝝁⟩.\displaystyle=-\frac{\langle{\boldsymbol{m}},{\boldsymbol{\mu}}\rangle-\langle{\boldsymbol{m}},{\boldsymbol{\mu}}\rangle\langle{\boldsymbol{\mu}},{{\mathsf{A}}^{-1}\_{2}\boldsymbol{\mu}}\rangle}{\langle{\boldsymbol{m}},{{\mathsf{A}}\_{2}\boldsymbol{m}}\rangle-2\langle{\boldsymbol{m}},{\boldsymbol{\mu}}\rangle^{2}+\langle{\boldsymbol{m}},{\boldsymbol{\mu}}\rangle^{2}\langle{\boldsymbol{\mu}},{{\mathsf{A}}^{-1}\_{2}\boldsymbol{\mu}}\rangle}. |  |

For this value of c1c\_{1} we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | qg\displaystyle{q}\_{g} | =⟨𝝁,𝖠2−1​𝝁⟩+c1​⟨𝝁,𝖠2−1​𝒈1⟩,\displaystyle=\langle{\boldsymbol{\mu}},{{\mathsf{A}}^{-1}\_{2}\boldsymbol{\mu}}\rangle+c\_{1}\langle{\boldsymbol{\mu}},{{\mathsf{A}}^{-1}\_{2}{\boldsymbol{g}}\_{1}}\rangle, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨𝝁,𝖠2−1​𝝁⟩−⟨𝝁,𝖠2−1​𝒈1⟩2⟨𝒈1,𝖠2−1​𝒈1⟩,\displaystyle=\langle{\boldsymbol{\mu}},{{\mathsf{A}}^{-1}\_{2}\boldsymbol{\mu}}\rangle-\frac{\langle{\boldsymbol{\mu}},{{\mathsf{A}}^{-1}\_{2}{\boldsymbol{g}}\_{1}}\rangle^{2}}{\langle{{\boldsymbol{g}}\_{1}},{{\mathsf{A}}^{-1}\_{2}{\boldsymbol{g}}\_{1}}\rangle}, |  |

This can be further expanded in terms of the definition of 𝒈1{\boldsymbol{g}}\_{1}, but it only makes the expression more complicated, rather
than less.

### 2.3 Discrete Features

Now consider the case where the 𝒙t{\boldsymbol{x}}\_{t} is discrete, taking one of a finite number, SS, of values.
Without loss of generality it suffices to consider 𝒙t{\boldsymbol{x}}\_{t} taking a value from 11 to SS.
Let πs{{\pi}\_{s}} be the probability that we observe value ss, which we will refer to as “observing state ss.”
Let 𝝁s{{\boldsymbol{\mu}}\_{s}} be the conditional expected return of the assets conditional on observing state ss,
and similarly let 𝖠2,s{\mathsf{A}}\_{2,s} be the conditional expected second moment, and
Σs{\mathsf{\Sigma}}\_{s} be the conditional covariance: Σs=𝖠2,s−𝝁s​𝝁s⊤{\mathsf{\Sigma}}\_{s}={\mathsf{A}}\_{2,s}-{{\boldsymbol{\mu}}\_{s}}{\boldsymbol{\mu}}^{\top}\_{s}.
Conditional on observing state ss we allocate into portfolio 𝝂s{{\boldsymbol{\nu}}\_{s}}.

The exposition above suggests that we should compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | q=∑1≤s≤Sπs​𝝁s⊤​𝖠2,s−1​𝝁s,q=\sum\_{1\leq s\leq S}{{\pi}\_{s}}{\boldsymbol{\mu}}^{\top}\_{s}{\mathsf{A}}^{-1}\_{2,s}{{\boldsymbol{\mu}}\_{s}}, |  | (29) |

then conditional on observing state ss to allocate to

|  |  |  |
| --- | --- | --- |
|  | 𝝂s,∗=R​q1−q​𝖠2,s−1​𝝁s.{{\boldsymbol{\nu}}\_{{s,}\*}}=R\sqrt{\frac{q}{1-q}}{\mathsf{A}}^{-1}\_{2,s}{{\boldsymbol{\mu}}\_{s}}. |  |

Note that this is different than the conditional Markowitz portfolio, which would take value
c​Σs−1​𝝁sc{{\mathsf{\Sigma}}^{-1}\_{s}}{{\boldsymbol{\mu}}\_{s}} for some constant cc independent of ss.

As the proof based on calculus of variations has many steps, and may rely on unfamiliar machinery,
we show directly in this case that the optimal solution takes the form we wrote above.
The expected return and variance of returns of our portfolio is

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​(𝝂)\displaystyle\mu\left(\boldsymbol{\nu}\right) | =∑1≤s≤Sπs​𝝁s⊤​𝝂s,\displaystyle=\sum\_{1\leq s\leq S}{{\pi}\_{s}}{\boldsymbol{\mu}}^{\top}\_{s}{{\boldsymbol{\nu}}\_{s}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | a2​(𝝂)\displaystyle{{a}\_{2}}\left(\boldsymbol{\nu}\right) | =∑1≤s≤Sπs​𝝂s⊤​𝖠2,s​𝝂s.\displaystyle=\sum\_{1\leq s\leq S}{{\pi}\_{s}}{\boldsymbol{\nu}}^{\top}\_{s}{\mathsf{A}}\_{2,s}{{\boldsymbol{\nu}}\_{s}}. |  |

Starting from Problem [12](https://arxiv.org/html/2601.18124v1#S2.E12 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"), the Lagrangian function is

|  |  |  |
| --- | --- | --- |
|  | ℒ​(𝝂,λ)=μ​(𝝂)−r0σ​(𝝂)+λ​(σ​(𝝂)−R).\mathcal{L}\left(\boldsymbol{\nu},\lambda\right)=\frac{\mu\left(\boldsymbol{\nu}\right)-{{r}\_{0}}}{\sigma\left(\boldsymbol{\nu}\right)}+\lambda\left(\sigma\left(\boldsymbol{\nu}\right)-R\right). |  |

We now take the gradient with respect to the subvector 𝝂s{{\boldsymbol{\nu}}\_{s}} and set to zero. This yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇𝝂sℒ​(𝝂,λ)\displaystyle{{\nabla}\_{{{\boldsymbol{\nu}}\_{s}}}}\mathcal{L}\left(\boldsymbol{\nu},\lambda\right) | =πs​𝝁sσ​(𝝂)−μ​(𝝂)−r0σ2​(𝝂)​∇𝝂sσ​(𝝂)+λ​∇𝝂sσ​(𝝂),\displaystyle=\frac{{{\pi}\_{s}}{{\boldsymbol{\mu}}\_{s}}}{\sigma\left(\boldsymbol{\nu}\right)}-\frac{\mu\left(\boldsymbol{\nu}\right)-{{r}\_{0}}}{\sigma^{2}\left(\boldsymbol{\nu}\right)}{{\nabla}\_{{{\boldsymbol{\nu}}\_{s}}}}\sigma\left(\boldsymbol{\nu}\right)+\lambda{{\nabla}\_{{{\boldsymbol{\nu}}\_{s}}}}\sigma\left(\boldsymbol{\nu}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c1​πs​𝝁s+c2​∇𝝂sσ​(𝝂),\displaystyle=c\_{1}{{\pi}\_{s}}{{\boldsymbol{\mu}}\_{s}}+c\_{2}{{\nabla}\_{{{\boldsymbol{\nu}}\_{s}}}}\sigma\left(\boldsymbol{\nu}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c1​πs​𝝁s+c2​(∇𝝂sa2​(𝝂)−2​μ​(𝝂)​πs​𝝁s),\displaystyle=c\_{1}{{\pi}\_{s}}{{\boldsymbol{\mu}}\_{s}}+c\_{2}\left({{\nabla}\_{{{\boldsymbol{\nu}}\_{s}}}}{{a}\_{2}}\left(\boldsymbol{\nu}\right)-2\mu\left(\boldsymbol{\nu}\right){{\pi}\_{s}}{{\boldsymbol{\mu}}\_{s}}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c1​πs​𝝁s+c2​(2​πs​𝖠2,s​𝝂s−2​μ​(𝝂)​πs​𝝁s),\displaystyle=c\_{1}{{\pi}\_{s}}{{\boldsymbol{\mu}}\_{s}}+c\_{2}\left(2{{\pi}\_{s}}{\mathsf{A}}\_{2,s}{{\boldsymbol{\nu}}\_{s}}-2\mu\left(\boldsymbol{\nu}\right){{\pi}\_{s}}{{\boldsymbol{\mu}}\_{s}}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =πs​(c1′​𝝁s+c2′​𝖠2,s​𝝂s),\displaystyle={{\pi}\_{s}}\left(c\_{1}^{\prime}{{\boldsymbol{\mu}}\_{s}}+c\_{2}^{\prime}{\mathsf{A}}\_{2,s}{{\boldsymbol{\nu}}\_{s}}\right), |  |

where the constants ci′c\_{i}^{\prime} depend on 𝝂\boldsymbol{\nu} and λ\lambda, but do not depend on the state ss.
Setting this to zero we can find 𝝂s,∗{{\boldsymbol{\nu}}\_{{s,}\*}} up to scaling.
Namely we have

|  |  |  |
| --- | --- | --- |
|  | 𝝂s,∗=c​𝖠2,s−1​𝝁s.{{\boldsymbol{\nu}}\_{{s,}\*}}=c{\mathsf{A}}^{-1}\_{2,s}{{\boldsymbol{\mu}}\_{s}}. |  |

The constant cc does not depend on ss. It is a simple exercise to establish the identity of cc based on saturating the risk
budget.

We can rewrite Equation [29](https://arxiv.org/html/2601.18124v1#S2.E29 "In 2.3 Discrete Features ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") via the Sherman-Morrison identity as

|  |  |  |  |
| --- | --- | --- | --- |
|  | q\displaystyle q | =∑1≤s≤Sπs​𝝁s⊤​𝖠2,s−1​𝝁s,\displaystyle=\sum\_{1\leq s\leq S}{{\pi}\_{s}}{\boldsymbol{\mu}}^{\top}\_{s}{\mathsf{A}}^{-1}\_{2,s}{{\boldsymbol{\mu}}\_{s}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑1≤s≤Sπs​𝝁s⊤​(Σs+𝝁s​𝝁s⊤)−1​𝝁s,\displaystyle=\sum\_{1\leq s\leq S}{{\pi}\_{s}}{\boldsymbol{\mu}}^{\top}\_{s}{{\left({\mathsf{\Sigma}}\_{s}+{{\boldsymbol{\mu}}\_{s}}{\boldsymbol{\mu}}^{\top}\_{s}\right)}^{-1}}{{\boldsymbol{\mu}}\_{s}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑1≤s≤Sπs​𝝁s⊤​Σs−1​𝝁s1+𝝁s⊤​Σs−1​𝝁s,\displaystyle=\sum\_{1\leq s\leq S}{{\pi}\_{s}}\frac{{\boldsymbol{\mu}}^{\top}\_{s}{\mathsf{\Sigma}}^{-1}\_{s}{{\boldsymbol{\mu}}\_{s}}}{1+{\boldsymbol{\mu}}^{\top}\_{s}{\mathsf{\Sigma}}^{-1}\_{s}{{\boldsymbol{\mu}}\_{s}}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1−∑1≤s≤Sπs​11+𝝁s⊤​Σs−1​𝝁s.\displaystyle=1-\sum\_{1\leq s\leq S}{{\pi}\_{s}}\frac{1}{1+{\boldsymbol{\mu}}^{\top}\_{s}{\mathsf{\Sigma}}^{-1}\_{s}{{\boldsymbol{\mu}}\_{s}}}. |  | (30) |

We would like to compare this to the Hansen ratio of the investor who holds the unconditional Markowitz portfolio in every period,
but found no obvious simplification of their difference or ratio.
Instead we consider a simple example.

#### 2.3.1 An Example

Consider the case of two assets, and S=2S=2 discrete states.
Suppose that π1=π2=1/2{{\pi}\_{1}}={{\pi}\_{2}}=1/2 and

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 𝝁1\displaystyle{{\boldsymbol{\mu}}\_{1}} | =[11],\displaystyle=\left[\begin{array}[]{r}{1}\\ {1}\end{array}\right], | 𝝁2\displaystyle{{\boldsymbol{\mu}}\_{2}} | =[22],\displaystyle=\left[\begin{array}[]{r}{2}\\ {2}\end{array}\right], | Σ1\displaystyle{\mathsf{\Sigma}}\_{1} | =[1001],\displaystyle=\left[\begin{array}[]{cc}{1}&{0}\\ {0}&{1}\end{array}\right], | Σ2\displaystyle{\mathsf{\Sigma}}\_{2} | =[2002].\displaystyle=\left[\begin{array}[]{cc}{2}&{0}\\ {0}&{2}\end{array}\right]. |  |

Then we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝝂1,∗\displaystyle{{\boldsymbol{\nu}}\_{{1,}\*}} | =c​[2112]−1​[11]=[1/31/3],\displaystyle=c{{\left[\begin{array}[]{cc}{2}&{1}\\ {1}&{2}\end{array}\right]}^{-1}}\left[\begin{array}[]{r}{1}\\ {1}\end{array}\right]=\left[\begin{array}[]{r}{1/3}\\ {1/3}\end{array}\right], | 𝝂2,∗\displaystyle{{\boldsymbol{\nu}}\_{{2,}\*}} | =c​[6446]−1​[22]=[1/51/5].\displaystyle=c{{\left[\begin{array}[]{cc}{6}&{4}\\ {4}&{6}\end{array}\right]}^{-1}}\left[\begin{array}[]{r}{2}\\ {2}\end{array}\right]=\left[\begin{array}[]{r}{1/5}\\ {1/5}\end{array}\right]. |  |

Moreover we compute qq as

|  |  |  |
| --- | --- | --- |
|  | q=12​(23+45)=1115.q=\frac{1}{2}\left(\frac{2}{3}+\frac{4}{5}\right)=\frac{11}{15}. |  |

Supposing R=1R=1 and r0=0{{r}\_{0}}=0, the objective of our optimization problem takes value

|  |  |  |
| --- | --- | --- |
|  | q1−q=114.\sqrt{\frac{q}{1-q}}=\sqrt{\frac{11}{4}}. |  |

Now consider instead holding the conditional Markowitz portfolio in each of the two states.
That is, in both s=1,2s=1,2 one holds c​Σs−1​𝝁sc{\mathsf{\Sigma}}^{-1}\_{s}{{\boldsymbol{\mu}}\_{s}}, or

|  |  |  |
| --- | --- | --- |
|  | c​[1001]−1​[11]=c​[2002]−1​[22]=c​[11].c{{\left[\begin{array}[]{cc}{1}&{0}\\ {0}&{1}\end{array}\right]}^{-1}}\left[\begin{array}[]{r}{1}\\ {1}\end{array}\right]=c{{\left[\begin{array}[]{cc}{2}&{0}\\ {0}&{2}\end{array}\right]}^{-1}}\left[\begin{array}[]{r}{2}\\ {2}\end{array}\right]=c\left[\begin{array}[]{r}{1}\\ {1}\end{array}\right]. |  |

The mean return and risk of this strategy are

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​(𝝂)\displaystyle\mu\left(\boldsymbol{\nu}\right) | =c2​(2+4)=3​c,\displaystyle=\frac{c}{2}\left(2+4\right)=3c, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(𝝂)\displaystyle\sigma^{2}\left(\boldsymbol{\nu}\right) | =c22​(6+20)−9​c2=c2​(13−9)=4​c2,\displaystyle=\frac{c^{2}}{2}\left(6+20\right)-9c^{2}=c^{2}\left(13-9\right)=4c^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(𝝂)\displaystyle\sigma\left(\boldsymbol{\nu}\right) | =2​c.\displaystyle=2c. |  |

Thus the objective of the conditional Markowitz portfolio is only 32<112\frac{3}{2}<\frac{\sqrt{11}}{2}.
The boost to the Sharpe ratio by holding the Sherman-Morrison-Markowitz portfolio in this case is approximately 10.5%.

#### 2.3.2 Omitted States

The optimal objective value in the case of discrete features is

|  |  |  |
| --- | --- | --- |
|  | q1−q−r0R,\sqrt{\frac{q}{1-q}}-\frac{{{r}\_{0}}}{R}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | q=∑sπs​𝝁s⊤​𝖠2,s−1​𝝁s.q=\sum\_{s}{{\pi}\_{s}}{\boldsymbol{\mu}}^{\top}\_{s}{\mathsf{A}}^{-1}\_{2,s}{{\boldsymbol{\mu}}\_{s}}. |  |

Now consider the case where one does not observe all SS states,
rather whenever states 11 or 22 hold, one observes them as, say, state 3/23/2.
We consider the impact on qq.
The impact to qq will be

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​q\displaystyle\Delta q | =π3/2​𝝁3/2⊤​𝖠2,3/2−1​𝝁3/2−∑s=1,2πs​𝝁s⊤​𝖠2,s−1​𝝁s,\displaystyle={{\pi}\_{3/2}}{\boldsymbol{\mu}}^{\top}\_{3/2}{\mathsf{A}}^{-1}\_{2,3/2}{{\boldsymbol{\mu}}\_{3/2}}-\sum\_{s=1,2}{{\pi}\_{s}}{\boldsymbol{\mu}}^{\top}\_{s}{\mathsf{A}}^{-1}\_{2,s}{{\boldsymbol{\mu}}\_{s}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(π1+π2)​π1​𝝁1⊤+π2​𝝁2⊤π1+π2​(π1​𝖠2,1+π2​𝖠2,2π1+π2)−1​π1​𝝁1+π2​𝝁2π1+π2−∑s=1,2πs​𝝁s⊤​𝖠2,s−1​𝝁s,\displaystyle=\left({{\pi}\_{1}}+{{\pi}\_{2}}\right)\frac{{{\pi}\_{1}}{\boldsymbol{\mu}}^{\top}\_{1}+{{\pi}\_{2}}{\boldsymbol{\mu}}^{\top}\_{2}}{{{\pi}\_{1}}+{{\pi}\_{2}}}{{\left(\frac{{{\pi}\_{1}}{\mathsf{A}}\_{2,1}+{{\pi}\_{2}}{\mathsf{A}}\_{2,2}}{{{\pi}\_{1}}+{{\pi}\_{2}}}\right)}^{-1}}\frac{{{\pi}\_{1}}{{\boldsymbol{\mu}}\_{1}}+{{\pi}\_{2}}{{\boldsymbol{\mu}}\_{2}}}{{{\pi}\_{1}}+{{\pi}\_{2}}}-\sum\_{s=1,2}{{\pi}\_{s}}{\boldsymbol{\mu}}^{\top}\_{s}{\mathsf{A}}^{-1}\_{2,s}{{\boldsymbol{\mu}}\_{s}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(π1​𝝁1+π2​𝝁2)⊤​(π1​𝖠2,1+π2​𝖠2,2)−1​(π1​𝝁1+π2​𝝁2)−∑s=1,2πs​𝝁s⊤​𝖠2,s−1​𝝁s,\displaystyle={{\left({{\pi}\_{1}}{{\boldsymbol{\mu}}\_{1}}+{{\pi}\_{2}}{{\boldsymbol{\mu}}\_{2}}\right)}^{\top}}{{\left({{\pi}\_{1}}{\mathsf{A}}\_{2,1}+{{\pi}\_{2}}{\mathsf{A}}\_{2,2}\right)}^{-1}}\left({{\pi}\_{1}}{{\boldsymbol{\mu}}\_{1}}+{{\pi}\_{2}}{{\boldsymbol{\mu}}\_{2}}\right)-\sum\_{s=1,2}{{\pi}\_{s}}{\boldsymbol{\mu}}^{\top}\_{s}{\mathsf{A}}^{-1}\_{2,s}{{\boldsymbol{\mu}}\_{s}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =π1​[(𝝁1+γ​𝝁2)⊤​(𝖠2,1+γ​𝖠2,2)−1​(𝝁1+γ​𝝁2)−𝝁1⊤​𝖠2,1−1​𝝁1−γ​𝝁2⊤​𝖠2,2−1​𝝁2],\displaystyle={{\pi}\_{1}}\left[{{\left({{\boldsymbol{\mu}}\_{1}}+\gamma{{\boldsymbol{\mu}}\_{2}}\right)}^{\top}}{{\left({\mathsf{A}}\_{2,1}+\gamma{\mathsf{A}}\_{2,2}\right)}^{-1}}\left({{\boldsymbol{\mu}}\_{1}}+\gamma{{\boldsymbol{\mu}}\_{2}}\right)-{\boldsymbol{\mu}}^{\top}\_{1}{\mathsf{A}}^{-1}\_{2,1}{{\boldsymbol{\mu}}\_{1}}-\gamma{\boldsymbol{\mu}}^{\top}\_{2}{\mathsf{A}}^{-1}\_{2,2}{{\boldsymbol{\mu}}\_{2}}\right], |  |

where γ=π2/π1\gamma={{\pi}\_{2}}/{{\pi}\_{1}}.
The worst case largest drop in qq occurs when 𝝁1=−γ​𝝁2{{\boldsymbol{\mu}}\_{1}}=-\gamma{{\boldsymbol{\mu}}\_{2}}, and the contribution to qq of state 3/23/2 is exactly zero.
In that case we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​q\displaystyle\Delta q | =π1​[−𝝁1⊤​𝖠2,1−1​𝝁1−γ​𝝁2⊤​𝖠2,2−1​𝝁2],\displaystyle={{\pi}\_{1}}\left[-{\boldsymbol{\mu}}^{\top}\_{1}{\mathsf{A}}^{-1}\_{2,1}{{\boldsymbol{\mu}}\_{1}}-\gamma{\boldsymbol{\mu}}^{\top}\_{2}{\mathsf{A}}^{-1}\_{2,2}{{\boldsymbol{\mu}}\_{2}}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =π1​[−𝝁1⊤​𝖠2,1−1​𝝁1−1γ​𝝁1⊤​𝖠2,2−1​𝝁1],\displaystyle={{\pi}\_{1}}\left[-{\boldsymbol{\mu}}^{\top}\_{1}{\mathsf{A}}^{-1}\_{2,1}{{\boldsymbol{\mu}}\_{1}}-\frac{1}{\gamma}{\boldsymbol{\mu}}^{\top}\_{1}{\mathsf{A}}^{-1}\_{2,2}{{\boldsymbol{\mu}}\_{1}}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−π1​𝝁1⊤​(𝖠2,1−1+1γ​𝖠2,2−1)​𝝁1.\displaystyle=-{{\pi}\_{1}}{\boldsymbol{\mu}}^{\top}\_{1}\left({\mathsf{A}}^{-1}\_{2,1}+\frac{1}{\gamma}{\mathsf{A}}^{-1}\_{2,2}\right){{\boldsymbol{\mu}}\_{1}}. |  |

This means that it is possible to have two different states such that if they were undifferentiated the impact on qq would be
disastrous, with Δ​q\Delta q approaching −1-1.
Getting useful bounds for the omitted variable impact requires further assumptions.

### 2.4 Optimizing Over Basis Portfolios

Suppose that the function space of acceptable portfolio functions 𝝂​(𝒙)\boldsymbol{\nu}\left(\boldsymbol{x}\right) is spanned by a finite set of
basis functions 𝝂i​(𝒙){{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right).
That is any portfolio function can be uniquely expressed as

|  |  |  |
| --- | --- | --- |
|  | 𝝂​(𝒙)=∑iβi​𝝂i​(𝒙).\boldsymbol{\nu}\left(\boldsymbol{x}\right)=\sum\_{i}\beta\_{i}{{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right). |  |

Then the portfolio optimization of Problem [10](https://arxiv.org/html/2601.18124v1#S2.E10 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") can be expressed as finding the optimal values of the βi\beta\_{i}.
First note that

|  |  |  |
| --- | --- | --- |
|  | μ​(∑iβi​𝝂i​(𝒙))=∑iβi​μ​(𝝂i​(𝒙))\mu\left(\sum\_{i}\beta\_{i}{{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right)\right)=\sum\_{i}\beta\_{i}\mu\left({{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right)\right) |  |

by linearity of the integral.
Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | a2​(∑iβi​𝝂i​(𝒙))\displaystyle{{a}\_{2}}\left(\sum\_{i}\beta\_{i}{{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right)\right) | =∫(∑iβi​𝝂i​(𝒙))⊤​𝖠2​(𝒙)​(∑jβj​𝝂j​(𝒙))​f​(𝒙)​d𝒙,\displaystyle=\int{{\left(\sum\_{i}\beta\_{i}{{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right)\right)}^{\top}}{\mathsf{A}}\_{2}\left(\boldsymbol{x}\right)\left(\sum\_{j}\beta\_{j}{{\boldsymbol{\nu}}\_{j}}\left(\boldsymbol{x}\right)\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i,jβi​βj​∫𝝂i​(𝒙)⊤​𝖠2​(𝒙)​𝝂j​(𝒙)​f​(𝒙)​d𝒙,\displaystyle=\sum\_{i,j}\beta\_{i}\beta\_{j}\int{{{{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right)}^{\top}}{\mathsf{A}}\_{2}\left(\boldsymbol{x}\right){{\boldsymbol{\nu}}\_{j}}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}, |  |

thus the second moment is bilinear in the β\beta.
We can write this mean and second moment as operations on the vector 𝜷\boldsymbol{\beta} of βi\beta\_{i} coefficients as

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​(∑iβi​𝝂i​(𝒙))\displaystyle\mu\left(\sum\_{i}\beta\_{i}{{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right)\right) | =𝜷⊤​𝝁,\displaystyle={{\boldsymbol{\beta}}^{\top}}\boldsymbol{\mu}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | a2​(∑iβi​𝝂i​(𝒙))\displaystyle{{a}\_{2}}\left(\sum\_{i}\beta\_{i}{{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right)\right) | =𝜷⊤​𝖠2​𝜷,\displaystyle={{\boldsymbol{\beta}}^{\top}}{\mathsf{A}}\_{2}\boldsymbol{\beta}, |  |

where we define the vector 𝝁\boldsymbol{\mu} and matrix 𝖠2{\mathsf{A}}\_{2} via

|  |  |  |  |
| --- | --- | --- | --- |
|  | μi\displaystyle{{\mu}\_{i}} | =∫𝝁​(𝒙)⊤​𝝂i​(𝒙)​f​(𝒙)​d𝒙,\displaystyle=\int{{\boldsymbol{\mu}\left(\boldsymbol{x}\right)}^{\top}}{{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖠2,i,j\displaystyle{\mathsf{A}}\_{2,i,j} | =∫𝝂i​(𝒙)⊤​𝖠2​(𝒙)​𝝂j​(𝒙)​f​(𝒙)​d𝒙.\displaystyle=\int{{{{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right)}^{\top}}{\mathsf{A}}\_{2}\left(\boldsymbol{x}\right){{\boldsymbol{\nu}}\_{j}}\left(\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}. |  |

Let Σ=𝖠2−𝝁​𝝁⊤\mathsf{\Sigma}={\mathsf{A}}\_{2}-\boldsymbol{\mu}{\boldsymbol{\mu}}^{\top}.
Then Problem [10](https://arxiv.org/html/2601.18124v1#S2.E10 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝜷:𝜷⊤​Σ​𝜷≤R2⁡𝜷⊤​𝝁−r0𝜷⊤​Σ​𝜷.\max\_{\boldsymbol{\beta}:{{\boldsymbol{\beta}}^{\top}}\mathsf{\Sigma}\boldsymbol{\beta}\leq R^{2}}\frac{{{\boldsymbol{\beta}}^{\top}}\boldsymbol{\mu}-{{r}\_{0}}}{\sqrt{{{\boldsymbol{\beta}}^{\top}}\mathsf{\Sigma}\boldsymbol{\beta}}}. |  | (31) |

This looks like a typical portfolio optimization problem with a finite number of assets,
which in this case are the portfolios 𝝂i​(𝒙){{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right).

Introducing the Lagrange multiplier, and after some simplification, the necessary condition of a solution to this problem is that

|  |  |  |
| --- | --- | --- |
|  | c1​𝝁+c2​Σ​𝜷=0,c\_{1}\boldsymbol{\mu}+c\_{2}\mathsf{\Sigma}\boldsymbol{\beta}=0, |  |

and thus the problem is solved by 𝜷=c​Σ−1​𝝁\boldsymbol{\beta}=c{\mathsf{\Sigma}}^{-1}\boldsymbol{\mu}.
To saturate the risk budget we take

|  |  |  |
| --- | --- | --- |
|  | c=Rζ∗,c=\frac{R}{{\zeta}\_{\*}}, |  |

where ζ∗2=𝝁⊤​Σ−1​𝝁{\zeta}^{2}\_{\*}={\boldsymbol{\mu}}^{\top}{\mathsf{\Sigma}}^{-1}\boldsymbol{\mu}.
Using the Sherman-Morrison identity as above this can be equivalently written as

|  |  |  |
| --- | --- | --- |
|  | 𝜷=R​(1+ζ∗2)ζ∗​𝖠2−1​𝝁.\boldsymbol{\beta}=\frac{R\left(1+{\zeta}^{2}\_{\*}\right)}{{\zeta}\_{\*}}{\mathsf{A}}\_{2}^{-1}\boldsymbol{\mu}. |  |

The maximized objective of this portfolio is ζ∗−r0R{\zeta}\_{\*}-\frac{{{r}\_{0}}}{R}.
The squared Hansen ratio of this optimal portfolio is

|  |  |  |
| --- | --- | --- |
|  | 𝝁⊤​𝖠2−1​𝝁.{{\boldsymbol{\mu}}^{\top}}{\mathsf{A}}^{-1}\_{2}\boldsymbol{\mu}. |  |

Now suppose the basis functions are all of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝂i​(𝒙)=𝖠2−1​(𝒙)​𝒈j​(𝒙).{{\boldsymbol{\nu}}\_{i}}\left(\boldsymbol{x}\right)={\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right){\boldsymbol{g}}\_{j}\left(\boldsymbol{x}\right). |  | (32) |

Then the vector 𝝁\boldsymbol{\mu} is equal to −𝒃-\boldsymbol{b} as given in Equation [27](https://arxiv.org/html/2601.18124v1#S2.E27 "In 2.2 Constrained Case ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"),
and the matrix 𝖠2{\mathsf{A}}\_{2} is equal to the matrix 𝖬\mathsf{M} in Equation [27](https://arxiv.org/html/2601.18124v1#S2.E27 "In 2.2 Constrained Case ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").
This confirms the Pythagorean theorem quoted in the section on hedging:
the optimal squared Hansen ratio is the sum of the squared Hansen ratio on the spanned space
and the squared Hansen ratio over the orthogonal space.

#### 2.4.1 Linear Portfolio Functions

Consider the case where the target portfolios are to be linear in the features 𝒙t{\boldsymbol{x}}\_{t}.
That is 𝝂​(𝒙t)=𝖶​𝒙t\boldsymbol{\nu}\left({\boldsymbol{x}}\_{t}\right)=\mathsf{W}{\boldsymbol{x}}\_{t} for an appropriately sized matrix 𝖶\mathsf{W}.
This is just a special case of the analysis above where the basis portfolio functions are
𝝂i,j​(𝒙t)=𝟏i​𝟏j⊤​𝒙t{{\boldsymbol{\nu}}\_{i,j}}\left({\boldsymbol{x}}\_{t}\right)={{\boldsymbol{1}}\_{i}}{\boldsymbol{1}}^{\top}\_{j}{\boldsymbol{x}}\_{t}.
Then we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μ​(𝝂i,j​(𝒙))\displaystyle\mu\left({{\boldsymbol{\nu}}\_{i,j}}\left(\boldsymbol{x}\right)\right) | =∫𝝁⊤​(𝒙)​𝟏i​𝟏j⊤​𝒙​f​(𝒙)​d𝒙,\displaystyle=\int{{\boldsymbol{\mu}}^{\top}}\left(\boldsymbol{x}\right){{\boldsymbol{1}}\_{i}}{\boldsymbol{1}}^{\top}\_{j}\boldsymbol{x}f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}, |  | (33) |

which takes the expected value of the conditional expected value of the ithi^{\text{th}} asset with respect to the jthj^{\text{th}} element of the
features.
That is, μ​(𝝂i,j​(𝒙))\mu\left({{\boldsymbol{\nu}}\_{i,j}}\left(\boldsymbol{x}\right)\right) is the unconditional expected value of the i,jthi,j^{\text{th}} element of
the “pseudo-asset”, 𝒚t⊗𝒙t{\boldsymbol{y}}\_{t}\otimes{\boldsymbol{x}}\_{t}.
Similarly the second moment matrix is the second moment matrix on the pseudo-assets.
Thus one can simply perform classical portfolio optimization techniques on the pseudo-assets 𝒚t⊗𝒙t{\boldsymbol{y}}\_{t}\otimes{\boldsymbol{x}}\_{t},
a method known as the “flattening trick” or “augmenting the asset space”.
[[14](https://arxiv.org/html/2601.18124v1#bib.bib19 "The Sharpe ratio: statistics and applications"), [2](https://arxiv.org/html/2601.18124v1#bib.bib20 "Dynamic portfolio selection by augmenting the asset space")]

### 2.5 Mean Variance Optimization

Consider now the mean variance optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈L2⁡μ​(𝝂)−γ2​σ2​(𝝂).\max\_{\boldsymbol{\nu}\in{L}^{2}}\mu\left(\boldsymbol{\nu}\right)-\frac{\gamma}{2}\sigma^{2}\left(\boldsymbol{\nu}\right). |  | (34) |

Suppose 𝝂∗​(𝒙){{\boldsymbol{\nu}}\_{{}\*}}\left(\boldsymbol{x}\right) is some function which solves Problem [34](https://arxiv.org/html/2601.18124v1#S2.E34 "In 2.5 Mean Variance Optimization ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"),
and let R=σ​(𝝂∗)R=\sigma\left({{\boldsymbol{\nu}}\_{{}\*}}\right).
Then we claim that 𝝂∗{{\boldsymbol{\nu}}\_{{}\*}} is a solution to

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈L2:σ​(𝝂)=R⁡μ​(𝝂)−γ​R22.\max\_{\boldsymbol{\nu}\in{L}^{2}\,:\,\sigma\left(\boldsymbol{\nu}\right)=R}\mu\left(\boldsymbol{\nu}\right)-\frac{\gamma R^{2}}{2}. |  | (35) |

Now note that Problem [35](https://arxiv.org/html/2601.18124v1#S2.E35 "In 2.5 Mean Variance Optimization ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") is
equivalent to Problem [14](https://arxiv.org/html/2601.18124v1#S2.E14 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"),
which has solution of the form given in Equation [19](https://arxiv.org/html/2601.18124v1#S2.E19 "In 2.1 Unconstrained Case ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"),
except that the constant cc may be computed differently.
Thus, as in the case of Sharpe maximization, the optimal portfolio is the Sherman-Morrison Markowitz portfolio.

Consider now the identity of the scaling constant cc.
We wish to solve Problem [34](https://arxiv.org/html/2601.18124v1#S2.E34 "In 2.5 Mean Variance Optimization ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") subject to 𝝂​(𝒙)=c​𝖠2−1​(𝒙)​𝝁​(𝒙)\boldsymbol{\nu}\left(\boldsymbol{x}\right)=c{\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right), which is to say

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxcc​μ​(𝝂∗)−c2γ​σ2​(𝝂∗),\max\_{c}\quad c\mu\left({{\boldsymbol{\nu}}\_{{}\*}}\right)-\frac{c^{2}}{\gamma}\sigma^{2}\left({{\boldsymbol{\nu}}\_{{}\*}}\right), |  | (36) |

where 𝝂∗​(𝒙)=𝖠2−1​(𝒙)​𝝁​(𝒙){{\boldsymbol{\nu}}\_{{}\*}}\left(\boldsymbol{x}\right)={\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right) is the unscaled Sherman-Morrison-Markowitz portfolio.
By basic calculus this is solved when

|  |  |  |  |
| --- | --- | --- | --- |
|  | c=γ​μ​(𝝂∗)2​σ2​(𝝂∗)=γ​q2​(q−q2)=γ2​(1−q).c=\frac{\gamma\mu\left({{\boldsymbol{\nu}}\_{{}\*}}\right)}{2\sigma^{2}\left({{\boldsymbol{\nu}}\_{{}\*}}\right)}=\frac{\gamma q}{2\left(q-{q}^{2}\right)}=\frac{\gamma}{2\left(1-q\right)}. |  | (37) |

The optimal value of the objective for this portfolio is equal to

|  |  |  |
| --- | --- | --- |
|  | γ4​q1−q.\frac{\gamma}{4}\frac{q}{1-q}. |  |

#### 2.5.1 Kelly Criterion

The Kelly Criterion is a bet-sizing scheme devised in the 1950’s
designed to maximize expected log terminal wealth. [[7](https://arxiv.org/html/2601.18124v1#bib.bib15 "A new interpretation of information rate"), [15](https://arxiv.org/html/2601.18124v1#bib.bib16 "The Kelly criterion and the stock market"), [9](https://arxiv.org/html/2601.18124v1#bib.bib18 "The Kelly capital growth investment criterion")]
We will employ the usual quadratic expansion of the logarithm to show
that a Kelly investor should also hold the Sherman-Morrison-Markowitz portfolio, if they can ignore skewness
and higher order moments.

Let yty\_{t} be the simple returns gained by an investor after time period tt.
The Kelly criterion is based on maximizing

|  |  |  |
| --- | --- | --- |
|  | ∑tE⁡[log⁡(1+yt)].\sum\_{t}\operatorname{E}\left[\operatorname{log}\left(1+y\_{t}\right)\right]. |  |

The expectation is over the realizations of yty\_{t}.
In our formulation, the investor observes 𝒙t{\boldsymbol{x}}\_{t} prior to the investment decision,
in response to which they allocate 𝝂​(𝒙t)\boldsymbol{\nu}\left({\boldsymbol{x}}\_{t}\right).
Their returns are then yt=𝒚t⊤​𝝂​(𝒙t).y\_{t}={\boldsymbol{y}}^{\top}\_{t}\boldsymbol{\nu}\left({\boldsymbol{x}}\_{t}\right).

First, by the “tower rule” of expectations,

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[log⁡(1+y)]\displaystyle\operatorname{E}\left[\operatorname{log}\left(1+y\right)\right] | =E𝒙⁡[E⁡[log⁡(1+𝒚⊤​𝝂​(𝒙))|𝒙]].\displaystyle={{\operatorname{E}}\_{\boldsymbol{x}}}\left[\operatorname{E}\left[\operatorname{log}\left(1+{\boldsymbol{y}}^{\top}\boldsymbol{\nu}\left(\boldsymbol{x}\right)\right)\left|\,\boldsymbol{x}\right.\right]\right]. |  |

Now we use the quadratic expansion of the log, namely log⁡(1+ϵ)≈ϵ−12​ϵ2\operatorname{log}\left(1+\epsilon\right)\approx\epsilon-\frac{1}{2}\epsilon^{2}
to rewrite the expectation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[log⁡(1+y)]\displaystyle\operatorname{E}\left[\operatorname{log}\left(1+y\right)\right] | ≈E𝒙⁡[E⁡[𝒚⊤​𝝂​(𝒙)−12​(𝒚⊤​𝝂​(𝒙))2|𝒙]],\displaystyle\approx{{\operatorname{E}}\_{\boldsymbol{x}}}\left[\operatorname{E}\left[{\boldsymbol{y}}^{\top}\boldsymbol{\nu}\left(\boldsymbol{x}\right)-\frac{1}{2}\left({\boldsymbol{y}}^{\top}\boldsymbol{\nu}\left(\boldsymbol{x}\right)\right)^{2}\left|\,\boldsymbol{x}\right.\right]\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =E𝒙⁡[𝝁⊤​(𝒙)​𝝂​(𝒙)−12​𝝂⊤​(𝒙)​𝖠2​(𝒙)​𝝂​(𝒙)],\displaystyle={{\operatorname{E}}\_{\boldsymbol{x}}}\left[{{\boldsymbol{\mu}}^{\top}}\left(\boldsymbol{x}\right)\boldsymbol{\nu}\left(\boldsymbol{x}\right)-\frac{1}{2}{{\boldsymbol{\nu}}^{\top}}\left(\boldsymbol{x}\right){\mathsf{A}}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\nu}\left(\boldsymbol{x}\right)\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =μ​(𝝂)−12​a2​(𝝂).\displaystyle=\mu\left(\boldsymbol{\nu}\right)-\frac{1}{2}{{a}\_{2}}\left(\boldsymbol{\nu}\right). |  |

And thus a Kelly investor who accepts this approximation will seek to solve the portfolio problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝝂∈L2⁡μ​(𝝂)−12​a2​(𝝂),\max\_{\boldsymbol{\nu}\in{L}^{2}}\mu\left(\boldsymbol{\nu}\right)-\frac{1}{2}{{a}\_{2}}\left(\boldsymbol{\nu}\right), |  | (38) |

As with the mean variance analysis above, if we let r=a2​(𝝂∗)r={{a}\_{2}}\left({{\boldsymbol{\nu}}\_{{}\*}}\right) for the
optimal portfolio function 𝝂∗​(𝒙){{\boldsymbol{\nu}}\_{{}\*}}\left(\boldsymbol{x}\right), then this problem is equivalent to
a variant of Problem [16](https://arxiv.org/html/2601.18124v1#S2.E16 "In 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").
Once again the solution is to hold the Sherman-Morrison-Markowitz portfolio as given in Equation [19](https://arxiv.org/html/2601.18124v1#S2.E19 "In 2.1 Unconstrained Case ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").
Again, the leading constant cc can be found, via simple calculus, to be

|  |  |  |
| --- | --- | --- |
|  | c=μ​(𝝂∗)a2​(𝝂∗)=qq=1.c=\frac{\mu\left({{\boldsymbol{\nu}}\_{{}\*}}\right)}{{{a}\_{2}}\left({{\boldsymbol{\nu}}\_{{}\*}}\right)}=\frac{q}{q}=1. |  |

And thus the (approximate) Kelly investor will hold the unscaled Sherman-Morrison-Markowitz portfolio, 𝖠2−1​(𝒙)​𝝁​(𝒙){\mathsf{A}}^{-1}\_{2}\left(\boldsymbol{x}\right)\boldsymbol{\mu}\left(\boldsymbol{x}\right).
The objective value of this portfolio is q/2q/2.
A “fractional Kelly” investor will hold some down-levered fraction of the full Sherman-Morrison-Markowitz portfolio,
to reduce the probability of a single disastrous loss.
[[9](https://arxiv.org/html/2601.18124v1#bib.bib18 "The Kelly capital growth investment criterion")]

## 3 Applications

We briefly mention a few practical applications of the theory of the Sherman-Morrison-Markowitz portfolio.

### 3.1 Linear Conditional Expectation Model

Consider the *linear conditional expectation model*, [[12](https://arxiv.org/html/2601.18124v1#bib.bib9 "Asymptotic distribution of the Markowitz portfolio")]

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝁​(𝒙t)\displaystyle\boldsymbol{\mu}\left({\boldsymbol{x}}\_{t}\right) | =𝖡​𝒙t,\displaystyle=\mathsf{B}{\boldsymbol{x}}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖠2​(𝒙t)\displaystyle{\mathsf{A}}\_{2}\left({\boldsymbol{x}}\_{t}\right) | =Σ+(𝖡​𝒙t)​(𝖡​𝒙t)⊤.\displaystyle=\mathsf{\Sigma}+\left(\mathsf{B}{\boldsymbol{x}}\_{t}\right){{\left(\mathsf{B}{\boldsymbol{x}}\_{t}\right)}^{\top}}. |  |

The optimal portfolio, by Equation [20](https://arxiv.org/html/2601.18124v1#S2.E20 "In 2.1 Unconstrained Case ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio") is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝂∗​(𝒙t)\displaystyle{{\boldsymbol{\nu}}\_{{}\*}}\left({\boldsymbol{x}}\_{t}\right) | =Rq−q2​11+(𝖡​𝒙t)⊤​Σ−1​(𝖡​𝒙t)​Σ−1​𝖡​𝒙t.\displaystyle=\frac{R}{\sqrt{q-{q}^{2}}}\frac{1}{1+{{\left(\mathsf{B}{\boldsymbol{x}}\_{t}\right)}^{\top}}{\mathsf{\Sigma}}^{-1}\left(\mathsf{B}{\boldsymbol{x}}\_{t}\right)}{\mathsf{\Sigma}}^{-1}\mathsf{B}{\boldsymbol{x}}\_{t}. |  |

The optimal objective for this portfolio is

|  |  |  |
| --- | --- | --- |
|  | q1−q−r0R,\sqrt{\frac{q}{1-q}}-\frac{{{r}\_{0}}}{R}, |  |

where qq takes value

|  |  |  |  |
| --- | --- | --- | --- |
|  | q\displaystyle q | =∫(𝖡​𝒙)⊤​(Σ+(𝖡​𝒙)​(𝖡​𝒙)⊤)−1​(𝖡​𝒙)​f​(𝒙)​d𝒙,\displaystyle=\int{{\left(\mathsf{B}\boldsymbol{x}\right)}^{\top}}{{\left(\mathsf{\Sigma}+\left(\mathsf{B}\boldsymbol{x}\right){{\left(\mathsf{B}\boldsymbol{x}\right)}^{\top}}\right)}^{-1}}\left(\mathsf{B}\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫(𝖡​𝒙)⊤​Σ−1​(𝖡​𝒙)1+(𝖡​𝒙)⊤​Σ−1​(𝖡​𝒙)​f​(𝒙)​d𝒙.\displaystyle=\int\frac{{{\left(\mathsf{B}\boldsymbol{x}\right)}^{\top}}{{\mathsf{\Sigma}}^{-1}}\left(\mathsf{B}\boldsymbol{x}\right)}{1+{{\left(\mathsf{B}\boldsymbol{x}\right)}^{\top}}{{\mathsf{\Sigma}}^{-1}}\left(\mathsf{B}\boldsymbol{x}\right)}f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}. |  |

In contrast the conditional Markowitz portfolio is equal to

|  |  |  |
| --- | --- | --- |
|  | c​Σ−1​𝖡​𝒙tc{\mathsf{\Sigma}}^{-1}\mathsf{B}{\boldsymbol{x}}\_{t} |  |

for some constant cc. The unconditional mean and variance of this allocation are

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ\displaystyle\mu | =c​∫(𝖡​𝒙)⊤​Σ−1​𝖡​𝒙​f​(𝒙)​d𝒙,\displaystyle=c\int{{\left(\mathsf{B}\boldsymbol{x}\right)}^{\top}}{\mathsf{\Sigma}}^{-1}\mathsf{B}\boldsymbol{x}f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c​tr⁡(𝖡⊤​Σ−1​𝖡​E⁡[𝒙​𝒙⊤]).\displaystyle=c\operatorname{tr}\left({{\mathsf{B}}^{\top}}{\mathsf{\Sigma}}^{-1}\mathsf{B}\operatorname{E}\left[\boldsymbol{x}{{\boldsymbol{x}}^{\top}}\right]\right). |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2\displaystyle{\sigma}^{2} | =∫(c​Σ−1​𝖡​𝒙)⊤​(Σ+(𝖡​𝒙)​(𝖡​𝒙)⊤)​(c​Σ−1​𝖡​𝒙)​f​(𝒙)​d𝒙−μ2,\displaystyle=\int{{\left(c{\mathsf{\Sigma}}^{-1}\mathsf{B}\boldsymbol{x}\right)}^{\top}}\left(\mathsf{\Sigma}+\left(\mathsf{B}\boldsymbol{x}\right){{\left(\mathsf{B}\boldsymbol{x}\right)}^{\top}}\right)\left(c{\mathsf{\Sigma}}^{-1}\mathsf{B}\boldsymbol{x}\right)f\left(\boldsymbol{x}\right)\,\mathrm{d}{\boldsymbol{x}}-\mu^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c​μ+c2​E⁡[(tr⁡(𝖡⊤​Σ−1​𝖡​𝒙​𝒙⊤))2]−μ2.\displaystyle=c\mu+c^{2}\operatorname{E}\left[\left(\operatorname{tr}\left({{\mathsf{B}}^{\top}}{\mathsf{\Sigma}}^{-1}\mathsf{B}\boldsymbol{x}{{\boldsymbol{x}}^{\top}}\right)\right)^{2}\right]-\mu^{2}. |  |

#### 3.1.1 An Example

Further simplificiation of the equations above to compare the performance gap between the Sherman-Morrison-Markowitz portfolio and the Markowitz portfolio does not seem easily attained.
However, we can compare them numerically based on some population data that we concocted.
Suppose that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒙t\displaystyle{\boldsymbol{x}}\_{t} | ∼𝒩​([11−2],𝖨3),\displaystyle\sim\mathcal{N}\left(\left[\begin{array}[]{r}{1}\\ {1}\\ {-2}\end{array}\right],{\mathsf{I}}\_{3}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖡\displaystyle\mathsf{B} | =[0.040.02−0.03−0.03−0.020.02],\displaystyle=\left[\begin{array}[]{ccc}{0.04}&{0.02}&{-0.03}\\ {-0.03}&{-0.02}&{0.02}\end{array}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ\displaystyle\mathsf{\Sigma} | =[1−0.1−0.11].\displaystyle=\left[\begin{array}[]{cc}{1}&{-0.1}\\ {-0.1}&{1}\end{array}\right]. |  |

Via Monte Carlo simulations we estimate the integrals and find that the unconditional Sharpe ratio of the Sherman-Morrison-Markowitz portfolio is

|  |  |  |
| --- | --- | --- |
|  | ζ∗=q1−q≈0.156.{\zeta}\_{\*}=\sqrt{\frac{q}{1-q}}\approx 0.156. |  |

Meanwhile the manager who holds the conditional Markowitz portfolio in every period enjoys nearly the same Sharpe ratio.
The difference in Sharpe ratios is estimated to be only

|  |  |  |
| --- | --- | --- |
|  | Δ​ζ∗≈3.724×10−5,\Delta{\zeta}\_{\*}\approx 3.724\times 10^{-5}, |  |

a value so small it will have no practical effect.
This result will come as no surprise when we consider the effect of rescaling constant,

|  |  |  |
| --- | --- | --- |
|  | (1+(𝖡​𝒙)⊤​Σ−1​(𝖡​𝒙))−1.{{\left(1+{{\left(\mathsf{B}\boldsymbol{x}\right)}^{\top}}{{\mathsf{\Sigma}}^{-1}}\left(\mathsf{B}\boldsymbol{x}\right)\right)}^{-1}}. |  |

We estimate the standard deviation of this rescaling constant in this example to be only 0.0180.018,
thus there is little average difference between the scale of the conditional Markowitz portfolio and that of the Sherman-Morrison-Markowitz portfolio.

### 3.2 A Neural Net Recipe

One failing of the linear conditional expectation model is that it does not recognize the predictable changes in volatility
which are often visible in asset returns. [[4](https://arxiv.org/html/2601.18124v1#bib.bib26 "Empirical properties of asset returns: stylized facts and statistical issues"), [1](https://arxiv.org/html/2601.18124v1#bib.bib27 "A conditionally heteroskedastic time series model for speculative prices and rates of return")]
Another weakness is that it forces us to perform featurizations of observable data or assume that linear functions are good enough.
Both of these defects can be addressed by using a neural net to approximate the functions 𝝁​(𝒙)\boldsymbol{\mu}\left(\boldsymbol{x}\right) and 𝖠2​(𝒙){\mathsf{A}}\_{2}\left(\boldsymbol{x}\right).
We provide a high level recipe for doing so, recognizing that there are myriad omitted details.
While mathematically the features 𝒙t{\boldsymbol{x}}\_{t} are expressed as a vector, in reality these variables are likely to come in two
forms: those which are specific to the assets, and those which are “macroeconomic” or otherwise apply to all assets.
For example, when considering equities trading we expect features to consist of a bunch of time-by-stock matrices,
perhaps measured at different frequencies; the latter can be expressed as a collection of single time series.
The neural net should be designed to ingest these, perhaps keeping applying the same computations to the per-stock features,
and otherwise ingesting the macroeconomic features.
The output should consist of “heads” for 𝝁​(𝒙)\boldsymbol{\mu}\left(\boldsymbol{x}\right) and 𝖠2​(𝒙){\mathsf{A}}\_{2}\left(\boldsymbol{x}\right).
Likely the latter should be computed as some low rank update to a diagonal matrix.
Because of the danger of overfitting we recommend the network contain some low dimensional “bottleneck” between features
and output.
To perform model fitting, one could assume some elliptical distribution of asset returns then maximize likelihood.

### 3.3 Investigating Leverage

One odd possible application of the theory is in investigating whether an existing strategy makes optimal use of leverage.
Alternatively one can view this as creating a kind of overlay which acts on top of an existing strategy.
It works as follows: suppose you observe the period returns of a strategy, call them ztz\_{t}, as well as the leverage of the
strategy, defined as the sum of absolute proportional allocation in each asset. Denote this leverage by xtx\_{t}.
Now consider the returns of the unit-levered version of the strategy, defined as

|  |  |  |
| --- | --- | --- |
|  | yt=ztxt.y\_{t}=\frac{z\_{t}}{x\_{t}}. |  |

While the feature and returns are scalars instead of vectors, we can think of this problem in the same framework as above.
Since the strategy somehow chooses to allocate to total leverage of xtx\_{t}, this feature is clearly observable to us
prior to the investment decision. The optimal leverage in each period is

|  |  |  |
| --- | --- | --- |
|  | c​μ​(xt)a2​(xt).c\frac{\mu\left(x\_{t}\right)}{{{a}\_{2}}\left(x\_{t}\right)}. |  |

If we could estimate this function, then plot it against xtx\_{t}, we should hope to see a straight line through the origin.
We can estimate the numerator and denominator in this fraction separately,
perhaps via non-parametric techniques, since they correspond to how yty\_{t} and yt2y\_{t}^{2} vary with xtx\_{t} in a given sample.
Care should be taken to force the denominator to be non-negative.

## 4 Conclusion and Future Directions

We established optimality of the Sherman-Morrison-Markowitz portfolio for portfolio optimization problems under the unconditional Sharpe ratio objective as well as
the mean-variance objective, including approximate Kelly criterion optimization.
The Sherman-Morrison-Markowitz portfolio differs from the conditional Markowitz portfolio in each period by relatively down-levering when the conditional squared
Sharpe ratio is higher.
We show that the optimal squared Hansen ratio is the expected value of the conditional squared Hansen ratio;
in the multi-period context we find that replacing the centered variance or covariance matrix
with the uncentered versions is more natural and simplifies certain computations.
We separately prove the result in the discrete feature case, confirming the result.
We show how to deal with constraints in expectation, as well as how to optimize over a finite set of basis portfolios.
We establish a Pythagorean theorem for squared Hansen ratio of the spanned and orthogonal optimal portfolios.
Simulations show that the Sherman-Morrison-Markowitz portfolio only provides modest improvements over the Markowitz portfolio in terms of achieved Sharpe ratio.
The practical impacts of switching to the Sherman-Morrison-Markowitz portfolio will likely be small, but one may find some solace in holding the optimal
portfolio.

We envision the following for further revisions of this work:

1. 1.

   This work assumes that the functions 𝝁​(𝒙t)\boldsymbol{\mu}\left({\boldsymbol{x}}\_{t}\right) and 𝖠2​(𝒙t){\mathsf{A}}\_{2}\left({\boldsymbol{x}}\_{t}\right) are known, while in reality they have to be
   estimated from data.
   While estimation of the mean is fairly straightforward under most commonly assumed models, modeling the second moment matrix
   function is unusual.
   Further work would establish the correct way to do this.
2. 2.

   Similarly, while much is known about performing inference on the Sharpe ratio [[14](https://arxiv.org/html/2601.18124v1#bib.bib19 "The Sharpe ratio: statistics and applications")], much less is known about doing
   so on the Hansen ratio, either in the conditional case, or in the unconditional optimal allocation we outline here.
   Moreover, if one could trade on one of two different universes of assets, with different observational histories, how should one
   make that decision? How does estimation error affect the achieved outcomes?
3. 3.

   We suspect one can establish bounds on the gap in performance between the Markowitz portfolio and the Sherman-Morrison-Markowitz portfolio.
   Doing so would help practitioners judge the value of switching to the Sherman-Morrison-Markowitz portfolio.
4. 4.

   Our neural net recipe lacks specifics; more battle-tested recommendations would be welcome.
5. 5.

   Similarly, it would be interesting to concoct a traditional “linear” model that takes into account conditional
   heteroskedasticity and compare it against a neural net recipe.

## References

* [1]
  T. Bollerslev (1987)
  A conditionally heteroskedastic time series model for speculative prices and rates of return.
  The Review of Economics and Statistics 69 (3),  pp. pp. 542–547 (English).
  External Links: [Link](http://www.jstor.org/stable/1925546),
  ISSN 00346535
  Cited by: [§3.2](https://arxiv.org/html/2601.18124v1#S3.SS2.p1.5 "3.2 A Neural Net Recipe ‣ 3 Applications ‣ The Sherman-Morrison-Markowitz Portfolio").
* [2]
  M. W. Brandt and P. Santa-Clara (2006)
  Dynamic portfolio selection by augmenting the asset space.
  The Journal of Finance 61 (5),  pp. 2187–2217.
  External Links: ISSN 1540-6261,
  [Link](http://faculty.fuqua.duke.edu/~mbrandt/papers/published/condport.pdf),
  [Document](https://dx.doi.org/10.1111/j.1540-6261.2006.01055.x)
  Cited by: [§2.4.1](https://arxiv.org/html/2601.18124v1#S2.SS4.SSS1.p1.10 "2.4.1 Linear Portfolio Functions ‣ 2.4 Optimizing Over Basis Portfolios ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").
* [3]
  A. Černý (2020)
  The Hansen ratio in mean–variance portfolio theory.
  External Links: 2007.15980,
  [Link](https://arxiv.org/abs/2007.15980)
  Cited by: [item 3](https://arxiv.org/html/2601.18124v1#S1.I1.i3.p1.1 "In 1 Introduction ‣ The Sherman-Morrison-Markowitz Portfolio"),
  [§2.1.1](https://arxiv.org/html/2601.18124v1#S2.SS1.SSS1.p1.1 "2.1.1 Hansen Ratio ‣ 2.1 Unconstrained Case ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").
* [4]
  R. Cont (2001)
  Empirical properties of asset returns: stylized facts and statistical issues.
  Quantitative Finance 1 (2),  pp. 223–236.
  External Links: [Document](https://dx.doi.org/10.1080/713665670),
  [Link](http://personal.fmipa.itb.ac.id/khreshna/files/2011/02/cont2001.pdf)
  Cited by: [§3.2](https://arxiv.org/html/2601.18124v1#S3.SS2.p1.5 "3.2 A Neural Net Recipe ‣ 3 Applications ‣ The Sherman-Morrison-Markowitz Portfolio").
* [5]
  V. DeMiguel, L. Garlappi, and R. Uppal (2009)
  Optimal versus naive diversification: how inefficient is the 1/N portfolio strategy?.
  Review of Financial Studies 22 (5),  pp. 1915–1953.
  External Links: [Link](http://faculty.london.edu/avmiguel/DeMiguel-Garlappi-Uppal-RFS.pdf)
  Cited by: [§1](https://arxiv.org/html/2601.18124v1#S1.p1.1 "1 Introduction ‣ The Sherman-Morrison-Markowitz Portfolio").
* [6]
  W. W. Hager (1989-06)
  Updating the Inverse of a Matrix.
  SIAM Review 31 (2),  pp. 221–239.
  Note: Publisher: Society for Industrial and Applied Mathematics
  External Links: ISSN 0036-1445,
  [Link](https://epubs.siam.org/doi/10.1137/1031049),
  [Document](https://dx.doi.org/10.1137/1031049)
  Cited by: [§1](https://arxiv.org/html/2601.18124v1#S1.p3.2 "1 Introduction ‣ The Sherman-Morrison-Markowitz Portfolio").
* [7]
  J. L. Kelly (1956)
  A new interpretation of information rate.
  The Bell System Technical Journal 35 (4),  pp. 917–926.
  External Links: [Document](https://dx.doi.org/10.1002/j.1538-7305.1956.tb03809.x),
  [Link](http://www.edwardothorp.com/wp-content/uploads/2016/11/TheKellyCriterionAndTheStockMarket.pdf)
  Cited by: [§2.5.1](https://arxiv.org/html/2601.18124v1#S2.SS5.SSS1.p1.1 "2.5.1 Kelly Criterion ‣ 2.5 Mean Variance Optimization ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").
* [8]
  C. R. MacCluer (2005)
  Calculus of variations: mechanics, control, and other applications.
   Pearson/Prentice Hall.
  External Links: ISBN 9780131423831,
  LCCN 2004040069,
  [Link](https://books.google.com/books?id=rqQrAAAAYAAJ)
  Cited by: [§2.1](https://arxiv.org/html/2601.18124v1#S2.SS1.p1.1 "2.1 Unconstrained Case ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").
* [9]
  L. C. MacLean, E. O. Thorp, and W. T. Ziemba (2011)
  The Kelly capital growth investment criterion.
   edition, World Scientific, .
  External Links: [Document](https://dx.doi.org/10.1142/7598),
  [Link](https://www.worldscientific.com/doi/abs/10.1142/7598),
  https://www.worldscientific.com/doi/pdf/10.1142/7598
  Cited by: [§2.5.1](https://arxiv.org/html/2601.18124v1#S2.SS5.SSS1.p1.1 "2.5.1 Kelly Criterion ‣ 2.5 Mean Variance Optimization ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"),
  [§2.5.1](https://arxiv.org/html/2601.18124v1#S2.SS5.SSS1.p3.6 "2.5.1 Kelly Criterion ‣ 2.5 Mean Variance Optimization ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").
* [10]
  H. Markowitz (1952)
  Portfolio selection.
  The Journal of Finance 7 (1),  pp. pp. 77–91 (English).
  External Links: [Link](http://www.jstor.org/stable/2975974),
  [Document](https://dx.doi.org/10.1111/j.1540-6261.1952.tb01525.x),
  ISSN 00221082
  Cited by: [§1](https://arxiv.org/html/2601.18124v1#S1.p1.1 "1 Introduction ‣ The Sherman-Morrison-Markowitz Portfolio").
* [11]
  R. O. Michaud (1989)
  The Markowitz optimization enigma: is ‘optimized’ optimal?.
  Financial Analysts Journal,  pp. 31–42.
  External Links: [Link](http://newfrontieradvisors.com/Research/Articles/documents/markowitz-optimization-enigma-010189.pdf)
  Cited by: [§1](https://arxiv.org/html/2601.18124v1#S1.p1.1 "1 Introduction ‣ The Sherman-Morrison-Markowitz Portfolio").
* [12]
  S. E. Pav (2013)
  Asymptotic distribution of the Markowitz portfolio.
  Note: Privately Published
  External Links: [Link](http://arxiv.org/abs/1312.0557)
  Cited by: [§3.1](https://arxiv.org/html/2601.18124v1#S3.SS1.p1.2 "3.1 Linear Conditional Expectation Model ‣ 3 Applications ‣ The Sherman-Morrison-Markowitz Portfolio").
* [13]
  S. E. Pav (2014)
  Bounds on portfolio quality.
  Note: Privately Published
  External Links: [Link](http://arxiv.org/abs/1409.5936)
  Cited by: [§1](https://arxiv.org/html/2601.18124v1#S1.p1.1 "1 Introduction ‣ The Sherman-Morrison-Markowitz Portfolio").
* [14]
  S. E. Pav (2021)
  The Sharpe ratio: statistics and applications.
   CRC Press.
  Cited by: [§2.1.1](https://arxiv.org/html/2601.18124v1#S2.SS1.SSS1.p3.3 "2.1.1 Hansen Ratio ‣ 2.1 Unconstrained Case ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"),
  [§2.4.1](https://arxiv.org/html/2601.18124v1#S2.SS4.SSS1.p1.10 "2.4.1 Linear Portfolio Functions ‣ 2.4 Optimizing Over Basis Portfolios ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio"),
  [item 2](https://arxiv.org/html/2601.18124v1#S4.I1.i2.p1.1 "In 4 Conclusion and Future Directions ‣ The Sherman-Morrison-Markowitz Portfolio").
* [15]
  L. M. Rotando and E. O. Thorp (1992-12)
  The Kelly criterion and the stock market.
  The American Mathematical Monthly (EN).
  Note: Publisher: Taylor & Francis
  External Links: ISSN 0002-9890,
  [Link](https://www.tandfonline.com/doi/abs/10.1080/00029890.1992.11995955),
  [Document](https://dx.doi.org/10.2307/2324484)
  Cited by: [§2.5.1](https://arxiv.org/html/2601.18124v1#S2.SS5.SSS1.p1.1 "2.5.1 Kelly Criterion ‣ 2.5 Mean Variance Optimization ‣ 2 Unconditional Sharpe Maximization ‣ The Sherman-Morrison-Markowitz Portfolio").
* [16]
  D. Ruppert (2006)
  Statistics and Finance: An Introduction.
   Springer.
  Cited by: [§1](https://arxiv.org/html/2601.18124v1#S1.p1.1 "1 Introduction ‣ The Sherman-Morrison-Markowitz Portfolio").