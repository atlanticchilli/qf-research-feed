---
authors:
- Graham L Giller
doc_id: arxiv:2512.11666v2
family_id: arxiv:2512.11666
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Risk Limited Asset Allocation with a Budget Threshold Utility Function and
  Leptokurtotic Distributions of Returns
url_abs: http://arxiv.org/abs/2512.11666v2
url_html: https://arxiv.org/html/2512.11666v2
venue: arXiv q-fin
version: 2
year: 2025
---


Graham L. Giller
[graham@gillerinvestments.com](mailto:graham@gillerinvestments.com)

(Date: December 16, 2025)

###### Abstract.

An analytical solution to single-horizon asset allocation for an investor with a piecewise-linear utility function, called herein the “budget threshold utility,” and exogenous position limits is presented. The resulting functional form has a surprisingly simple structure and can be readily interpreted as representing the addition of a simple “risk cost” to otherwise frictionless trading.

## 1. Introduction

Beginning with the pioneering work of Markowitz[harry1952markowitz], the theory of optimal investment (and optimal trading) has been the subject of extensive analytical work, both in academia and within financial institutions. The purpose of this note is not to provide a comprehensive discussion of the subject, which can be found in numerous places such as the work of Ziemba and MacLean[ziemba2017problems], the recent book by Paleologo[paleologo2025elements], and the author’s own works[giller2023essays]. Nor is to provide a thoroughly developed theory of investment in theory or in practice, which can be found in many places including those cited, but merely to present an interesting111At least to the author. analytical result that is of relevance to the general subject. Properly, this might be thought of as sitting somewhere between fully optimal investment strategy and a completely naïve investment strategy, as an informed reader will be able to readily identify structural flaws in some of the major propositions. In fact, a correspondent of the author went as far as to describe the shape of the utility function discussed as “irrational.”[viole2025private]. Nevertheless, the result presented is fully optimal given the assumptions presented, connects a gap between risk neutral investment and risk averse investment, and is of a remarkably simple analytical form.

## 2. The Budget-Threshold Utility Function

Influenced by the work of Nawrocki and Viole[viole2011utility], and the author’s personal experience in proprietary trading at a large investment bank[giller2022adventures], we construct a piecewise linear utility function that is indifferent to wealth, WW​, above a pre-defined threshold, or “budget,” β\beta, and linear in the dis-utility of wealth below that budget. Mathematically, this can be written

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | U​(W,β)={βW≥βWW<β,U(W,\beta)=\begin{cases}\beta&W\geq\beta\\ W&W<\beta\end{cases}, |  |

and is illustrated, for several values of β\beta, in figure [1](https://arxiv.org/html/2512.11666v2#S2.F1 "Figure 1 ‣ 2. The Budget-Threshold Utility Function ‣ Risk Limited Asset Allocation with a Budget Threshold Utility Function and Leptokurtotic Distributions of Returns"), below.

![Refer to caption](utility.png)


Figure 1. Functional form of the budget-threshold utility function for several values of the budget, β\beta.

Viole’s criticism of this form222Viole, as previously cited is that:

1. (i)

   there is no “credit” received for wealth increases above the budget which, in an inter-temporal setting, could be used to decrease the instantaneous budget requirement for the next investment period while leaving the temporal average of the budget unchanged; and,
2. (ii)

   the linear dis-utility of losses does not sufficiently deter risk-taking behaviour when compared to, for example, quadratic functions such as those that appear in mean-variance optimization[harry1952markowitz].

Nevertheless, this is a concave function that might be thought of as describing the objectives of “some” investors or traders, and is interesting to investigate.

## 3. The Distribution of Returns

The distribution of asset returns over the investment horizon considered is taken to be represented by the Generalized Error distribution333Sometimes called the Generalized Normal distribution or the Exponential Power distribution., which is a symmetric univariate distribution from the exponential family[forbes2011statistical] that may be parametrically deformed into a range of shapes including both the Laplace distribution and the Normal distribution, as well as more leptokurtotic varieties and platykurtotic varieties up to a limiting form as the Uniform density. This choice is motivated by the author’s personal research into describing the distribution of returns in securities markets that are consistent over extensive periods of history[giller2022adventures].

The GED\mathrm{GED} has many parameterizations, but the one used here is:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | r∼GED​(μ,σ,κ)⇔f​(r|μ,σ,κ)=e−12​|r−μσ|1κ2κ+1​σ​Γ​(κ+1)r\sim\mathrm{GED}(\mu,\sigma,\kappa)\Leftrightarrow f(r|\mu,\sigma,\kappa)=\frac{e^{-\frac{1}{2}\left|\frac{r-\mu}{\sigma}\right|^{\frac{1}{\kappa}}}}{2^{\kappa+1}\sigma\Gamma(\kappa+1)} |  |

where f​(⋅)f(\cdot) is the probability density function of rr given parameters (μ,σ,κ)(\mu,\sigma,\kappa). These specify the location, scale, and kurtosis444The kurtosis is a function of κ\kappa and the standard deviation is a function of σ\sigma and κ\kappa, see Giller[giller2005generalized]. of the distribution of returns, respectively. This form is chosen specifically so that the Normal limit (κ=1/2\kappa=1/2) appears naturally, in its common form, without a required reparameterization of σ\sigma.
If rr is taken to be a major market index, such as the S&P 500, it is found that, for most of recorded history:555i.e. From 1929–2025. μ>0\mu>0; σ\sigma follows some form of asymmetric GARCH process[glosten1993relation, engle2001garch]; and κ\kappa is around 0.750.75[giller2022adventures].

## 4. Choice of Budget and Expected Utility

To find an optimal holding, h^\hat{h}, in an asset with some expected return, α\alpha, it is necessary to compute the expected utility under the given distribution of returns and then maximize the resultant function. i.e.

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | h^=arg​maxh⁡𝔼​[U​(W​(h),β)|α].\hat{h}=\operatorname\*{arg~max}\_{h}\mathbb{E}[U(W(h),\beta)|\alpha]. |  |

To obtain a solution, the following choices are made:666Equivalently, the entire discussion can be framed in terms of marginal utility without any required changes.

1. (i)

   the initial wealth is zero, thus the wealth in the utility expression is solely a function of the incremental profits due to investment;
2. (ii)

   the future wealth, given hh and rr, is then simply their product, h​rhr; and,
3. (iii)

   the budget is taken to be the expected value of the future wealth, or h​αh\alpha.

Then

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | 𝔼​[U]​(h|α,σ,κ)=∫−∞∞U​(h​r,h​α)​f​(r|α,σ,κ)​𝑑r.\mathbb{E}[U](h|\alpha,\sigma,\kappa)=\int\_{-\infty}^{\infty}U(hr,h\alpha)f(r|\alpha,\sigma,\kappa)\,dr. |  |

As the utility is piecewise linear, it is immediately obvious that, in the framework of Nawrocki and Viole, this function is the sum of the lower-partial moment777The conventional statistical moment of order nn about aa, μn′​(a)=𝔼​[(x−a)n]\mu\_{n}^{\prime}(a)=\mathbb{E}[(x-a)^{n}], may be partitioned into the sum of a lower-partial moment, ln′​(a)=𝔼​[(x−a)n|x≤a]l\_{n}^{\prime}(a)=\mathbb{E}[(x-a)^{n}|x\leq a], and an upper-partial moment, un′​(a)=𝔼​[(x−a)n​|x>​a]u\_{n}^{\prime}(a)=\mathbb{E}[(x-a)^{n}|x>a]. of order 11 and the upper-partial model of order 0, both evaluated with reference to the expected profit, h​αh\alpha. i.e.

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | 𝔼​[U]=l1′​(h​α)+u0′​(h​α)\mathbb{E}[U]=l\_{1}^{\prime}(h\alpha)+u\_{0}^{\prime}(h\alpha) |  |

Furthermore, due to the linearity, this integral exists and may be evaluated. It may be shown to be

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (6) |  | 𝔼​[U]​(h|α,σ,κ)\displaystyle\mathbb{E}[U](h|\alpha,\sigma,\kappa) | =h​(α−σ​τ​(κ)​sgnh)\displaystyle=h\left(\alpha-\sigma\tau(\kappa)\operatorname\*{sgn}h\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (7) |  | where​τ​(κ)\displaystyle\mathrm{where}\;\tau(\kappa) | =Γ​(2​κ+1)22−κ​Γ​(κ+1).\displaystyle=\frac{\Gamma(2\kappa+1)}{2^{2-\kappa}\Gamma(\kappa+1)}. |  |

Although, as a ratio of Gamma functions, τ​(κ)\tau(\kappa) is strongly divergent, within the region of interest, 1/2≤κ≤11/2\leq\kappa\leq 1, it is remarkably well behaved, growing relatively slowly from 1/2​π1/\sqrt{2\pi} at the lower edge of this range to just 11 at the upper edge.

![Refer to caption](tau.png)


Figure 2. The risk scaling function over the region of interest.

## 5. Maximum Expected Utility Subject to an Exogenous Risk-Limit

With asymptotically linear utility functions an obvious defect exists: there is no upper or lower limit to the positions taken that arises naturally from the problem specification. This is unlike mean-variance optimization in which the quadratic form guarantees a finite solution for finite arguments. However, this defect can be regularized away by introducing an exogenous risk limit, L>0L>0, to the problem. i.e.

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | h^=arg​maxh⁡𝔼​[U]​(h|α,σ,κ)​becomes​h^=arg​maxh∈[−L,+L]⁡𝔼​[U]​(h|α,σ,κ).\hat{h}=\operatorname\*{arg~max}\_{h}\mathbb{E}[U](h|\alpha,\sigma,\kappa)\;\mathrm{becomes}\;\hat{h}=\operatorname\*{arg~max}\_{h\in[-L,+L]}\mathbb{E}[U](h|\alpha,\sigma,\kappa). |  |

There is no practical loss of generality to this modification of the problem as all real investors face such constraints, whether they arise naturally from their finite wealth and credit prospects or from an institutional risk-management role. With this regularization step, the optimal position is readily obtained and is given in theorem [1](https://arxiv.org/html/2512.11666v2#Thmtheorem1 "Theorem 1. ‣ 5. Maximum Expected Utility Subject to an Exogenous Risk-Limit ‣ Risk Limited Asset Allocation with a Budget Threshold Utility Function and Leptokurtotic Distributions of Returns").

###### Theorem 1.

The position for a risk-limited investor with a budget threshold utility function that maximizes the expected utility when returns are drawn from a Generalized Error distribution is given by:

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | h^={L​sgnα|α|>σ​τ​(κ)0otherwise.\hat{h}=\begin{cases}L\operatorname\*{sgn}\alpha&|\alpha|>\sigma\tau(\kappa)\\ 0&\mathrm{otherwise}\end{cases}. |  |

###### Proof.

Consider h>0h>0: in this circumstance equation [6](https://arxiv.org/html/2512.11666v2#S4.E6 "In 4. Choice of Budget and Expected Utility ‣ Risk Limited Asset Allocation with a Budget Threshold Utility Function and Leptokurtotic Distributions of Returns") becomes, simply,

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | Ω​(h)=𝔼​[U]​(h|α,σ,κ)=h​(α−σ​τ​(κ))⇒d​Ωd​h|h>0=α−σ​τ​(κ).\Omega(h)=\mathbb{E}[U](h|\alpha,\sigma,\kappa)=h\left(\alpha-\sigma\tau(\kappa)\right)\;\Rightarrow\;\left.\frac{d\Omega}{dh}\right|\_{h>0}=\alpha-\sigma\tau(\kappa). |  |

It follows that for any given h>0h>0 such that α>σ​τ​(κ)\alpha>\sigma\tau(\kappa) it is always true that there exists h′∈(h,L]:Ω​(h′)>Ω​(h)h^{\prime}\in(h,L]:\Omega(h^{\prime})>\Omega(h). Thus, if α>σ​τ​(κ)\alpha>\sigma\tau(\kappa) then h^=+L\hat{h}=+L.
Now consider h>0h>0 but 0≤α≤σ​τ​(κ)0\leq\alpha\leq\sigma\tau(\kappa): in this circumstance Ω​(h)≤0\Omega(h)\leq 0 but we observe that Ω​(0)=0\Omega(0)=0. Thus it is sub-optimal to chose a non-zero position when 0<α≤σ​τ​(κ)0<\alpha\leq\sigma\tau(\kappa), or h^=0\hat{h}=0.

Consider h<0h<0: complementary arguments clearly lead to the same conclusions for negative alphas but with the sign exchanged.
Finally, consider α=0\alpha=0: for this case Ω​(h)<0​∀h≠0\Omega(h)<0\;\forall\;h\neq 0, therefore h^=0\hat{h}=0.
∎

## 6. Interpretation of the Result and a Practical Algorithm for Traders

I believe that, despite the apparent naïvety of the problem proposed, the solution is, in fact, quite interesting. It is well known that a risk-limited gross-profit maximizing investor should obtain a position as large as possible in the direction of the alpha[giller2023essays]. The introduction of the budget threshold, as specified in this work, changes such a long-short, or “binary,” trading algorithm to a three state system that considers long, short, and flat positions only. The term σ​τ​(κ)\sigma\tau(\kappa) can be thought of as a “risk cost” that must be exceeded to make risk-taking worthwhile to the investor.

This risk cost is a function of the parameterization of the distribution of returns, albeit not a particularly strongly varying function. For returns described by equation [2](https://arxiv.org/html/2512.11666v2#S3.E2 "In 3. The Distribution of Returns ‣ Risk Limited Asset Allocation with a Budget Threshold Utility Function and Leptokurtotic Distributions of Returns"), the variance of returns is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | s2=𝕍​[r]=22​κ​Γ​(3​κ)Γ​(κ)×σ2.s^{2}=\mathbb{V}[r]=\frac{2^{2\kappa}\Gamma(3\kappa)}{\Gamma(\kappa)}\times\sigma^{2}. |  |

Expressing the risk cost in terms of ss, the standard deviation of returns, gives

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | σ​τ​(κ)=14​Γ​(κ)Γ​(3​κ)​Γ​(2​κ+1)Γ​(κ+1)×s.\sigma\tau(\kappa)=\frac{1}{4}\sqrt{\frac{\Gamma(\kappa)}{\Gamma(3\kappa)}}\frac{\Gamma(2\kappa+1)}{\Gamma(\kappa+1)}\times s. |  |

It can clearly be seen from figure [3](https://arxiv.org/html/2512.11666v2#S6.F3 "Figure 3 ‣ 6. Interpretation of the Result and a Practical Algorithm for Traders ‣ Risk Limited Asset Allocation with a Budget Threshold Utility Function and Leptokurtotic Distributions of Returns") that the leptokurtosis of the distribution of returns barely affects the scaling of the standard deviation, ss, in the formula for the size of the risk cost “barrier.” Thus this is a clear example of a circumstance in which assuming Normally distributed returns doesn’t actually damage the optimal policy framework.

![Refer to caption](risk.png)


Figure 3. Scaling of the risk cost factor with the kurtosis parameter of the distribution of returns over the region of interest. The “Normal distribution theory” value is represented by the dotted line.

Nevertheless, given the commonly acknowledged non-stationarity of financial distributions and the simplicity of the optimal algorithm, it seems well motivated to follow a “semi-empirical” approach, similar to that adopted in Nuclear Physics[bethe1936semf, weizsacker1935semf], and replace this parametric expression with a simple constant, KK, to be determined from empirical optimization (i.e. backtesting). A practical algorithm for traders is then

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | h^={L​sgnα|α|>K​s0otherwise,\hat{h}=\begin{cases}L\operatorname\*{sgn}\alpha&|\alpha|>Ks\\ 0&\mathrm{otherwise}\end{cases}, |  |

where α\alpha and ss are the mean and standard deviation of future returns under the conditional distribution used by a trader for a given asset, and K≈0.4K\approx 0.4. This trading algorithm, in the form of a “holding function,”888Literally a function that tells the trader want position to hold in response to their inputs. is illustrated in figure [4](https://arxiv.org/html/2512.11666v2#S6.F4 "Figure 4 ‣ 6. Interpretation of the Result and a Practical Algorithm for Traders ‣ Risk Limited Asset Allocation with a Budget Threshold Utility Function and Leptokurtotic Distributions of Returns").

![Refer to caption](algo.png)


Figure 4. The “holding function” corresponding to the optimal strategy for a trader with a budget threshold utility function expressed as the relative position size as a function of the standardized alpha.