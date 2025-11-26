---
authors:
- Gilles Zumbach
doc_id: arxiv:2511.18125v1
family_id: arxiv:2511.18125
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2511.18125v1
url_html: https://arxiv.org/html/2511.18125v1
venue: arXiv q-fin
version: 1
year: 2025
---

Random processes for long-term market simulations

Gilles Zumbach
  

Edgelab
Avenue de la Rasude 5
1006 Lausanne
Switzerland

gilles.zumbach@bluewin.ch

gilles.zumbach@evooq.ch

November 10, 2025

###### Abstract

For long term investments, model portfolios are defined at the level of indexes, a setup known as Strategic Asset Allocation (SAA).
The possible outcomes at a scale of a few decades can be obtained by Monte Carlo simulations, resulting in a probability density for the possible portfolio values at the investment horizon.
Such studies are critical for long term wealth plannings, for example in the financial component of social insurances or in accumulated capital for retirement.
The quality of the results depends on two inputs: the process used for the simulations and its parameters.
The base model is a constant drift, a constant covariance and normal innovations, as pioneered by Bachelier.
Beyond this model, this document presents in details a multivariate process that incorporate the most recent advances in the models for financial time series.
This includes the negative correlations of the returns at a scale of a few years, the heteroskedasticity (i.e. the volatility’ dynamics), and the fat tails and asymmetry for the distributions of returns.
For the parameters, the quantitative outcomes depend critically on the estimate for the drift, because this is a non random contribution acting at each time step.
Replacing the point forecast by a probabilistic forecast allows us to analyze the impact of the drift values, and then to incorporate this uncertainty in the Monte Carlo simulations.
The main change introduced by the negative return correlations is the partial decoupling between the volatility (along the time direction) from the standard deviation of the terminal values.
The definition for the process is supplemented by graphs comparing empirical results obtained from major indices with the values computed with Monte Carlo simulations.
Finally, the main statistics for the wealth at increasing time are presented, showing the key features added by the components beyond the basic normal random walk.

Keywords:
Long term simulations, drift uncertainty, trend following, mean reversion, multivariate ARCH processes, non-central student distribution

JEL codes: C32, C53, C55, C63

## 1 Introduction

Long term financial planning is an important part of the investment activities, being for pension funds, insurances, or individual retirement plans.
Such planning involves defining a coarse-grained investment strategy using various indexes, and to check if the defined goals can be reached with the chosen strategy.
In the industry, such long term coarse-grained strategy are known as SAA, for *Strategic Asset Allocation*, in opposition to the short-term detailed investment choices known as TAA, for Tactical Asset Allocation.
The time scales are quite different for both allocations, being of the order of decades for SAA, while TAA are done at the scale of days to months with actual invested positions.

SAA establishes a long-term investment plan that allocates the invested amount in different asset classes based on an investor’s risk tolerance, financial goals, investment horizon, and possible other illiquid assets like real estate, private equities, or participation in businesses.
The simplest example is to decide on the balance between fixed income versus equities, hence controlling the target plan in term of risk and return.
SAA is a passive investment strategy that focuses on achieving a diversified portfolio of asset classes, that align with an investor’s long-term financial objectives.
At this level, the asset classes are represented by the corresponding indexes.
For SAA, the crucial part is to check, say using Monte Carlo simulations, that the selected strategy can reach the defined goal with a chosen probability.
As an example, consider a pension fund, or an individual sparing for its retirement, with a question like: will the selected investment strategy reaches a target goal with 95% probability.
In order to answer such questions, the distribution for the terminal wealth is needed.

The description in the previous paragraphs involves statements about the future value of an investment strategy, at some selected long time horizons.
In order to answer such questions, processes should be set, first for the evolution of the financial indexes, second for the investment strategy.
Both are quite different.
The financial world evolves according to a statistical description, at the core level as a random walk, and the investors suffer the price changes.
Very differently, the investment strategy is under control of investor(s) and manager(s), who will decide about the actual positions.
Hence, both models should incorporate these fundamental differences.
For the investment strategy, the simplest base model is a fixed-weights with periodic re-balancement, where at some predefined dates, the positions in a portfolio are bought or sold so as to be again at some defined target weights.
The periodic re-balancement is fairly simple to model and to implement, using the constraint that no in-flow or out-flow of cash is involved in the trades.
A much more difficult topic is to model the long term evolution of the financial world, and this is the subject of this paper.

The base model for market simulations follows the footsteps of [Bachelier, [1900](https://arxiv.org/html/2511.18125v1#bib.bib1)] using a simple multivariate normal random walk, with constant drifts, constant covariance matrix, and normal innovations.
The parameters for this model are the drifts, volatilities and the correlation between the assets.
In the SAA context, they are collectively known as the Capital Market Assumptions, or CMA for short.
Essentially, they are long term forecasts used as input for the simulations.
The CMA are usually provided by banks, where a team of economists and data scientists reevaluate such values each year, akin to making economic forecasts at a scale of decade(s).
For the present work, the CMA are taken as given.
As shown by research on financial time series over the last 40 years, the simple model provided by Bachelier is deficient in several respects, yet is at the core of all more advanced processes.
Our goal is to incorporate in a multivariate long term model these advances, in particular the heteroskedasticity (i.e. the time dependent volatility) and the fat tails distribution for the returns.

For the empirical analyses and the Monte Carlo simulations, this paper focuses on common indexes.
Essentially, we want to simulate the long term behavior of the financial universe.
For SAA, an investment strategy is a portfolio made of positions in this universe, together with a (time dependent) allocation on these positions.
The simplest one is a buy-and-hold strategy where the initial positions are given and the portfolio is never rebalanced.
The most common strategy is using fixed-weights, where the positions are periodically rebalanced toward some target weights.
Moreover, periodic in-flows or out-flows can be used, for example modeling the contributions or consumptions of a retirement fund.
Another common strategy is a gradual shift from risky investments to fixed incomes.
Clearly, the number of interesting portfolios and strategies over a given universe is quite large, and is an interesting subject in itself but beyond the scope of this paper.
The point is that, if the dynamical and distributional properties for the indexes are correct, and if the dependencies are correctly captured, then the time series and statistics for any portfolios and strategies are also correct.
For this reason, the present empirical studies are done exclusively on indexes.

In long term studies used in SAA, the focus is often on the terminal distributions, say after 10 or 20 years.
Yet, because of the possible dynamic components in an investment strategy, it is also very important to model correctly the distributions of prices at all intermediate times.
This description must include crashes and crises, with the related high volatility.
Even though the impact of such events can average out in the long term for the indexes, this might not be the case for an investment strategy.
For example, an out-flow from a portfolio during a crash can have a large impact on its subsequent values.
For these reasons, this study attempts at best to compare empirical and simulated distributions at the longest time horizon possible, in particular in the tails.
Similarly, statistics sensitive to the dynamics of the financial time series are critical.

The core difficulty for the present study is to extract relevant information from empirical time series, in particular for long time intervals.
As an order of magnitude, at an analysis time interval Δ​T\Delta T of 1 years, 20 years of data lead to 20 independent returns.
Of course, oversampling can be used, say sampling daily or monthly the one year returns.
This will give some more information, but these returns are correlated until a lag of 1 year, and at the end, the effective sample size is still of the order of 20.
This back-of-the-envelope estimation shows the difficulty of the empirical estimations for increasing Δ​T\Delta T.

The strategies that are used to extract at best information from time series are detailed in Sec. [6](https://arxiv.org/html/2511.18125v1#S6 "6 Statistical estimators").
Due to the lack of strong empirical statistics, we are certainly not in a comfortable position with respect to validation!
Yet, long term plannings are done anyway in the financial industry, say for pension funds or retirement plans.
Therefore, we better accept the inherent limitations in the empirical validations, and produce the best possible model given the current knowledge and historical data.
Even if imperfect, this is better than doing nothing, or using a simple normal random walk for the simulations.

To our best knowledge, many parts in the present empirical analysis and the multivariate process are new, in particular the analysis of the drift and its long term impact, the large multivariate LMARCH process, and the multivariate non-central Student.
A crucial part in long term simulations is the drifts, which are difficult to estimate.
A simple model for the drift uncertainty (DU) is introduced, taking onto account the inherent limitations of such estimations.
The uncertainty on the drift can be measured by an equivalent calibration time, essentially the length of the available historical data used to evaluate the drift.
Then, (negative) lagged correlations for the returns are added to a base constant drift, in effect stabilizing the process over long time span.
Together, these different pieces build a process suitable for long term Monte Carlo simulations of a cross-section of the financial market.

This introduction presents mainly the context and motivation for the present contribution.
Beside the historical reference to [Bachelier, [1900](https://arxiv.org/html/2511.18125v1#bib.bib1)] about the process commonly used today, the author is not aware of relevant academic contributions along the general lines explained above.
The differentiation between SAA and TAA seems to be a common work path and wording in the industry, but likely without a clear academic origin.
Similarly, a large literature exist on allocations, comparing historical performances and risks, but this is not the topic of the present paper, focusing on long term multivariate processes.
Yet, several publications concern the specific components of the present process.
For these reasons, the references to previous contributions have been deported in the introduction sections for each main topics, in [4](https://arxiv.org/html/2511.18125v1#S4 "4 The multivariate process structure"), [8.1](https://arxiv.org/html/2511.18125v1#S8.SS1 "8.1 Overview ‣ 8 The drift"), [9.1](https://arxiv.org/html/2511.18125v1#S9.SS1 "9.1 Overview ‣ 9 The covariance"), [10.1](https://arxiv.org/html/2511.18125v1#S10.SS1 "10.1 Random generators and non-central Student distribution ‣ 10 Distribution for the returns and innovations"), where each field is summarized with the proper references.

The organization of this paper mainly follows the presentation of the introduction.
A scalar version of the process is introduced in [2](https://arxiv.org/html/2511.18125v1#S2 "2 The base process settings"), setting the key components and the mathematical backdrop for the process using a discrete time increment.
The scaling analysis of drift and volatility, with the impact on long term simulations, is discussed in Sec. [3](https://arxiv.org/html/2511.18125v1#S3 "3 The core scaling of drift and volatility").
Section [4](https://arxiv.org/html/2511.18125v1#S4 "4 The multivariate process structure") introduces the multivariate structure for the processes with its main components: drift, covariance matrix, and innovations.
The technical material is presented then, namely the definitions of returns, volatilities and innovations used in this paper (Sec. [5](https://arxiv.org/html/2511.18125v1#S5 "5 Definitions of historical return, volatility and innovation")), the statistical estimators used for the graphs (Sec. [6](https://arxiv.org/html/2511.18125v1#S6 "6 Statistical estimators")), and the time series used for the empirical study (Sec. [7](https://arxiv.org/html/2511.18125v1#S7 "7 Empirical data")).
The core structure for the processes is introduced in Sec. [4](https://arxiv.org/html/2511.18125v1#S4 "4 The multivariate process structure"), the details for its components are given in section [8](https://arxiv.org/html/2511.18125v1#S8 "8 The drift") for the drift, in [9](https://arxiv.org/html/2511.18125v1#S9 "9 The covariance") for the covariance, and in [10](https://arxiv.org/html/2511.18125v1#S10 "10 Distribution for the returns and innovations") for the innovations.
These 3 sections contain graphs comparing the relevant statistics from empirical data and from Monte Carlo simulations.
After having introduced the 3 main ingredients, section [11](https://arxiv.org/html/2511.18125v1#S11 "11 Processes comparison") compares a selection of 5 processes in order to show their main characteristics, before the conclusions.
The more technical materials are given in appendices: appendix [A](https://arxiv.org/html/2511.18125v1#A1 "Appendix A A simple model with drift uncertainty") presents a theoretical model for the drift uncertainty, [B](https://arxiv.org/html/2511.18125v1#A2 "Appendix B Non-Central Student-t: random draws and evaluation of 𝜃⁢(𝜈)") for the non-central multivariate Student generator, and [C](https://arxiv.org/html/2511.18125v1#A3 "Appendix C Long term expectations") for the long term expectation of the LMARCH process with non-central Student innovations.
The supporting statistics and graphs are given in the respective sections about each topic.

## 2 The base process settings

In order to understand the setting for the process and the scaling issue in the next section, let us first focus on the univariate case.
The setting is identical for the multivariate case, with the equations [6](https://arxiv.org/html/2511.18125v1#S4.E6 "In 4 The multivariate process structure") given below.
The base univariate process used in this paper to model the evolution of a financial index or asset is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | r​(t+δ​t)\displaystyle r(t+\delta t) | =μ​(t)+σ​(t)​ϵ​(t+δ​t)\displaystyle=\mu(t)+\sigma(t)\,\epsilon(t+\delta t) |  | (1a) |
|  | p​(t+δ​t)\displaystyle p(t+\delta t) | =p​(t)⋅(1+r​(t+δ​t)).\displaystyle=p(t)\cdot\left(1+r(t+\delta t)\right). |  | (1b) |

In these equations, the current time is tt, with the past information known up to and including tt.
This means that the drift μ​(t)\mu(t) and the volatility σ​(t)\sigma(t) can be evaluated using the information up to tt (i.e. they are in the information set, or are in the filtration ℱ​(t)\mathcal{F}(t), or are tt-measurable).
The innovations ϵ​(t+δ​t)\epsilon(t+\delta t) is unknown at tt, independent from the previous draws, and described by a random variable with a distribution pϵ​(0,1)p\_{\epsilon}(0,1).
This distribution has a zero mean and unit variance.
Importantly, pϵp\_{\epsilon} is stationary, namely the distribution’s shape is fixed.
The equation [1a](https://arxiv.org/html/2511.18125v1#S2.E1.1 "In 1 ‣ 2 The base process settings") specifies the (random) return over one time step δ​t\delta t, Eq. [1b](https://arxiv.org/html/2511.18125v1#S2.E1.2 "In 1 ‣ 2 The base process settings") the time evolution of the (random) prices given the return.
As seen from tt, ϵ​(t+δ​t)\epsilon(t+\delta t), r​(t+δ​t)r(t+\delta t) and p​(t+δ​t)p(t+\delta t) are random variables.
At t+δ​tt+\delta t, the realized price p​(t+δ​t)p(t+\delta t) becomes known, from which r​(t+δ​t)r(t+\delta t) and ϵ​(t+δ​t)\epsilon(t+\delta t) can be evaluated by inverting the above equations, namely all become part of the filtration ℱ​(t+δ​t)\mathcal{F}(t+\delta t).

The point of view used in this paper is of a random process with a discrete time increment δ​t\delta t.
Because of the distribution pϵp\_{\epsilon} has fat tailed in order to be realistic, and because of the drift and volatility dynamics provided by μ​(t)\mu(t) and σ​(t)\sigma(t), the present specifications are unlikely to have a continuum limit and to be described by some Ito stochastic differential equations.
Hence, only a discrete time formulation of the process is used.

Both equations [1](https://arxiv.org/html/2511.18125v1#S2.E1 "In 2 The base process settings") or [6](https://arxiv.org/html/2511.18125v1#S4.E6 "In 4 The multivariate process structure") can be used directly in Monte Carlo simulations for applications in finance.
As stated in the introduction, our goal is to have realistic long term processes, matching the empirical properties of the financial markets.
Rigorous mathematical questions are not studied, say like the existence of asymptotic long term distributions for the return or the variance.
For the simulations used to produce the figures, a time step δ​t\delta t of 1 month was used.
Yet, the equations are not rooted at a particular value for the time increment, and a step of 1 day or 1 year could be used, depending on the application.

## 3 The core scaling of drift and volatility

For the sake of the present scaling argument, let us assume that the drift and volatility have no time dependency, namely are real numbers, say equal to their long term values.
These parameters are in general given at an annual scale, for example the typical annualized volatility of a stock index is between 15 to 30%.
Yet, the process is formulated at the scale δ​t\delta t, and the parameters have to be scaled to δ​t\delta t such that the resulting random walk has the correct behavior at longer time scale, say for example the specified annualized volatility.
Intuitively, the drift and volatility parameters must decrease with δ​t\delta t such that the drift and volatility at 1 year correspond to the desired values.
In the equation [1a](https://arxiv.org/html/2511.18125v1#S2.E1.1 "In 1 ‣ 2 The base process settings"), μ\mu and σ\sigma are respectively of order δ​t\delta t and δ​t\sqrt{\delta t}, originating in the deterministic and in the diffusive components of a random walk.
The δ​t\delta t dependency can be made explicit by using annualized parameters, with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | μ=\displaystyle\mu= | μδ​t=μ1y​δ​t1y\displaystyle\mu\_{\delta t}=\mu\_{\text{1y}}\,\frac{\delta t}{\text{1y}} |  | (2a) |
|  | σ=\displaystyle\sigma= | σδ​t=σ1y​δ​t1y\displaystyle\sigma\_{\delta t}=\sigma\_{\text{1y}}\,\sqrt{\frac{\delta t}{\text{1y}}} |  | (2b) |

where “1y” is a one year time interval, the subscript “1y” denotes annualized parameters, and the subscript “δ​t\delta t” makes explicit the implicit time scale in the drift and volatility.
The ratio δ​t/1y\delta t/\text{1y} is the process time step expressed in year.
The same relation can be used for any time interval Δ​T\Delta T, showing that the drift grows as Δ​T\Delta T while the diffusive part grows as Δ​T\sqrt{\Delta T}, as usual for a random walk.

These different scalings for the drift and volatility are crucial to understand the dominant behavior of a random walk, and the long time problems in finance.
For small Δ​T\Delta T, say from days to a few years, the volatility dominates the drift, and the random component is the leading feature of the process.
This is the regime where most computations are done in finance, for example in portfolio optimization, risk evaluation, or option pricing.
For large Δ​T\Delta T, say above one decade, the drift dominates the random part, and this deterministic component is the leading feature of the process.
The cross-over from diffusion to drift occurs at a time Δ​T×{\Delta T\_{\!\times}} when

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ1y​Δ​T×1y−σ1y​Δ​T×1y=0.\mu\_{\text{1y}}\frac{{\Delta T\_{\!\times}}}{\text{1y}}-\sigma\_{\text{1y}}\sqrt{\frac{{\Delta T\_{\!\times}}}{\text{1y}}}=0. |  | (3) |

In term of the probability distribution of the return, this equation says that the center of the distribution (the term in μ1y\mu\_{\text{1y}}) is one sigma away (the term in σ1y\sigma\_{\text{1y}}) from 0.
Essentially, after the time Δ​T×{\Delta T\_{\!\times}}, the drift is large enough to become visible with a good probability.
The equation [3](https://arxiv.org/html/2511.18125v1#S3.E3 "In 3 The core scaling of drift and volatility") can be solved for Δ​T×{\Delta T\_{\!\times}}

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​T×=(σ1yμ1y)2​1y{\Delta T\_{\!\times}}=\left(\frac{\sigma\_{\text{1y}}}{\mu\_{\text{1y}}}\right)^{2}\,\text{1y} |  | (4) |

where Δ​T×{\Delta T\_{\!\times}} is expressed in year.
Notice that μ1y\mu\_{\text{1y}} appears in the denominator.
The more familiar Sharpe ratio is closely related with the cross-over time

|  |  |  |  |
| --- | --- | --- | --- |
|  | rSharpe=μ1yσ1y=1yΔ​T×.r\_{\text{Sharpe}}=\frac{\mu\_{\text{1y}}}{\sigma\_{\text{1y}}}=\sqrt{\frac{\text{1y}}{{\Delta T\_{\!\times}}}}. |  | (5) |

When estimated from empirical time series, the drift is depending only on the start and end values of the sample, therefore carry a large uncertainty.
The mean volatility appears to have better estimation properties, at least for constant volatility process.
Yet, the heteroskedasticity makes it also dependent from the sample, roughly with a very large crisis each 10 years.
Therefore, the empirical estimation of both μ\mu and σ\sigma have important dependencies on the available empirical sample.
Hence, the cross-over time and the Sharpe ratio are “fragile” with respect to the empirical estimation of μ\mu and σ\sigma, and should be considered only as an order of magnitude.

Using long spans of historical data, the drift, volatility and cross-over time can be evaluated for a few indexes, as reported in the table [1](https://arxiv.org/html/2511.18125v1#S3.T1 "Table 1 ‣ 3 The core scaling of drift and volatility").
Roughly, the cross-over time is of the order of months to 1 decade for fixed income indexes, and around years to a few decades for equity indexes.
These numbers are in line with the typical investment advice, namely fixed income investments should be used for low risk and short investment periods, while equities are more risky and should be considered for long investment periods.
A balanced portfolio allows to adjust the investment strategy to the desired risk and return profile.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| name | category | return | volatility | Δ​T×{\Delta T\_{\!\times}} | Sharpe ratio |
| U.S. Short Duration Government | FI | 0.021 | 0.014 | 0.42 | 1.53 |
| Chinese Government Bonds | FI | 0.048 | 0.038 | 0.64 | 1.25 |
| U.S. Aggregate Bonds | FI | 0.032 | 0.042 | 1.77 | 0.75 |
| U.S. High Yield Bonds | FI | 0.065 | 0.094 | 2.10 | 0.69 |
| U.S. Inv Grade Corporate Bonds | FI | 0.042 | 0.066 | 2.45 | 0.64 |
| U.S. Government Bond | FI | 0.025 | 0.045 | 3.15 | 0.56 |
| Emerging Markets Sovereign Debt | FI | 0.049 | 0.094 | 3.65 | 0.52 |
| Euro High Yield Bonds | FI | 0.057 | 0.157 | 7.71 | 0.36 |
| U.S. Long (20+ Yr) Treasuries | FI | 0.037 | 0.140 | 13.96 | 0.27 |
| World Government Bonds | FI | 0.017 | 0.067 | 16.06 | 0.25 |
| Euro Inv Grade Corp Bonds | FI | 0.021 | 0.111 | 27.35 | 0.19 |
| Canadian Large Cap | Equity | 0.082 | 0.119 | 2.10 | 0.69 |
| U.S. Large Cap | Equity | 0.098 | 0.155 | 2.51 | 0.63 |
| U.S. Small Cap | Equity | 0.073 | 0.204 | 7.83 | 0.36 |
| European Small Cap | Equity | 0.059 | 0.223 | 14.20 | 0.26 |
| European Large Cap | Equity | 0.043 | 0.188 | 18.75 | 0.23 |
| MSCI China Equity | Equity | 0.053 | 0.259 | 24.09 | 0.20 |
| UK Small Cap | Equity | 0.045 | 0.225 | 24.74 | 0.20 |
| UK Large Cap | Equity | 0.035 | 0.175 | 24.83 | 0.20 |
| Emerging Markets Equity | Equity | 0.040 | 0.210 | 28.03 | 0.19 |
| Japanese Equity | Equity | 0.027 | 0.151 | 31.23 | 0.18 |
| Relative Value Hedge Funds | Alt. | 0.051 | 0.049 | 0.93 | 1.04 |
| Event Driven Hedge Funds | Alt. | 0.051 | 0.070 | 1.90 | 0.72 |
| Macro Hedge Funds | Alt. | 0.033 | 0.048 | 2.07 | 0.70 |
| Conservative Hedge Funds | Alt. | 0.027 | 0.041 | 2.29 | 0.66 |
| Diversified Hedge Funds | Alt. | 0.028 | 0.050 | 3.11 | 0.57 |
| Long Bias Hedge Funds | Alt. | 0.046 | 0.089 | 3.67 | 0.52 |
| Global Core Infrastructure | Alt. | 0.021 | 0.162 | 59.30 | 0.13 |

Table 1: Mean return, mean volatility, cross-over time Δ​T×{\Delta T\_{\!\times}} (in year) and Sharpe ratio for some financial assets.
All values are computed in USD, over the period Jan 2006 to Dec 2023, with monthly returns, then annualized.
The values are ordered according to the asset type (Fixed Income, Equity and Alternative), then by increasing cross-over time.

In all these scaling arguments, a risk free rate rrisk-freer\_{\text{risk-free}} can be subtracted from the drift or be inserted explicitly in the equations, depending on the reader preferences and the domain of application.
In view of the small values for the short term interest rates over the last two decades (between negative to 1%), including rrisk-freer\_{\text{risk-free}} does not change the core of the present order of magnitudes.

Returning to the problem of long term market simulations, the key point is that *the drift is the critical parameter* since the simulation time is at a scale of decades, namely above the cross-over time.
This setting is fundamentally different from most computations done in finance where the drift is a second order correction to results dominated by σ\sigma (say for example in the Black-Sholes option pricing formula, or in market risk evaluation).
For this reason, the drift is an important part of this paper, and includes a dynamical component to introduce a mean reversion, and a study of the error on the final distribution induced by the numerical uncertainty on the mean drift parameters (see Sec. [8](https://arxiv.org/html/2511.18125v1#S8 "8 The drift")).

## 4 The multivariate process structure

The multivariate version of Eq. [1](https://arxiv.org/html/2511.18125v1#S2.E1 "In 2 The base process settings") is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | 𝒓​(t+δ​t)\displaystyle\bm{r}(t+\delta t) | =𝝁​(t)+(𝚺​(t))1/2​ϵ​(t+δ​t)\displaystyle=\bm{\mu}(t)+\left(\bm{\Sigma}(t)\right)^{1/2}\,\bm{\epsilon}(t+\delta t) |  | (6a) |
|  | 𝒑​(t+δ​t)\displaystyle\bm{p}(t+\delta t) | =𝒑​(t)⊙(1+𝒓​(t+δ​t))\displaystyle=\bm{p}(t)\odot\left(1+\bm{r}(t+\delta t)\right) |  | (6b) |

where vectors and matrices are denoted with bold-face characters.
The prices 𝒑\bm{p} follow a random walk driven by the relative returns, with the same process setting as for Eq. [1](https://arxiv.org/html/2511.18125v1#S2.E1 "In 2 The base process settings"), namely with a finite time increment δ​t\delta t.
Beware that in Eq. [6b](https://arxiv.org/html/2511.18125v1#S4.E6.2 "In 6 ‣ 4 The multivariate process structure"), the product denoted by ⊙\odot in the rhs is an element-wise product (known as the Hadamard product).
The volatility matrix used in the process is a square root of the covariance matrix 𝚺\bm{\Sigma}.
Eq. [6a](https://arxiv.org/html/2511.18125v1#S4.E6.1 "In 6 ‣ 4 The multivariate process structure") is the specification for the return process used in this paper, and where the drift vector 𝝁​(t)\bm{\mu}(t), covariance matrix 𝚺​(t)\bm{\Sigma}(t), and innovation distribution pϵp\_{\bm{\epsilon}} should be specified.
As for the univariate case, the multivariate distribution pϵp\_{\bm{\epsilon}} is assumed to be stationary, with a zero mean and unit variance, but is not assumed to be normal.
With this structure, all the dependencies from the past are summarized in 𝝁​(t)\bm{\mu}(t) and 𝚺​(t)\bm{\Sigma}(t).
In particular, the vast family of ARCH model falls into this framework.
An important task is to justify empirically these dynamical components.

The simplest model is the Bachelier process, with constant drift and volatility, and a normal distribution for the innovations, with the multivariate parameters:

* •

  the vector of drift 𝝁\bm{\mu},
* •

  the vector of volatility 𝝈\bm{\sigma}, and
* •

  the matrix of correlation 𝝆\bm{\rho}.

With these parameters, the covariance is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺=𝝈𝑫⋅𝝆⋅𝝈𝑫\bm{\Sigma}=\bm{\sigma\_{D}}\cdot\bm{\rho}\cdot\bm{\sigma\_{D}} |  | (7) |

and 𝝈𝑫\bm{\sigma\_{D}} is the diagonal matrix containing the volatility for the assets given in 𝝈\bm{\sigma}.
This set of parameters are known as CMA, and are forecasts for the corresponding values.
Some long term econometric models can be used to derive them, mainly the drift 𝝁\bm{\mu} and volatility 𝝈\bm{\sigma}.
As a simple alternative, all CMA parameters can be evaluated with historical data (using an implicit stationary assumption).
For the present work, the CMA are taken as granted.

The CMA parameters have some constraints.
There is no constraint on the drifts, and the volatilities must be positive.
The most important constraint is on the correlation matrix, which must be a definite positive matrix.
This limitation originates in the process equation, where the square root of the covariance matrix must be taken111Mathematically, the correlation matrix must be non negative, namely all eigenvalues obey ϵi≥0\epsilon\_{i}\geq 0.
Because the square root will be computed numerically, the eigenvalues must be above zero within some tolerance ϵi≥ϵmin>0\epsilon\_{i}\geq\epsilon\_{\text{min}}>0 in order to ensure that, numerically, the square root can always be evaluated.
.
This constraint on a matrix is fairly limiting, and prevent to mangle with the correlation elements (say for example that some selected correlation values are projected to be larger).
Essentially, the correlation matrix must be computed from past returns, and with the same formula and time span for all time series.
An alternative approach is to project in some sense a non-positive correlation matrix on a space of positive correlation matrices, see for example [van der Schans and Boer, [2014](https://arxiv.org/html/2511.18125v1#bib.bib10)] for a recent work in this direction.

On top of the constant CMA parameters, dynamics can be added on 𝝁​(t)\bm{\mu}(t) and 𝚺​(t)\bm{\Sigma}(t), and the probability distribution for the innovations must be specified.
Since these parts are independent, a brief summary is given here, while a specific introduction, the analytical formula and validation statistics are presented respectively in sections [8](https://arxiv.org/html/2511.18125v1#S8 "8 The drift"), [9](https://arxiv.org/html/2511.18125v1#S9 "9 The covariance") and [10](https://arxiv.org/html/2511.18125v1#S10 "10 Distribution for the returns and innovations") respectively.

As mentioned above, the drift is the critical parameter in this long time problem.
Large error bars should be assumed on the CMA drift, and an error of order δ​μ\delta\mu on the drift has an impact Δ​T⋅δ​μ\Delta T\cdot\delta\mu after a time Δ​T\Delta T.
This behavior is dominant compare to the diffusive term, which grows as the square root of Δ​T\Delta T, hence it is important to include such uncertainties in the long term projections.
The simplest *drift uncertainty* (DU) model is to assume random drifts with a normal distribution centered around the CMA value.

Beside, lagged correlations for the returns and innovations point to positive correlations up to a few months, and negative correlations around a few years.
Such statistics are in agreement with short term “trend following” of traders, and with a “mean reversion” at longer time scales.
This behavior is embedded in the drift dynamics 𝝁​(t)\bm{\mu}(t) by lagged return terms, generating similar statistics in Monte Carlo simulations.
The most important term is the negative lagged correlations, which introduce a correcting effect after large drops or rises in the simulated prices, effectively “stabilizing” the long term process.
We have called this term *Negative Return Correlation* (NRC).

The model used for the drift is detailed in Sec. [8](https://arxiv.org/html/2511.18125v1#S8 "8 The drift"), with a specific overview [8.1](https://arxiv.org/html/2511.18125v1#S8.SS1 "8.1 Overview ‣ 8 The drift"), the Monte Carlo simulations is explained in [8.2](https://arxiv.org/html/2511.18125v1#S8.SS2 "8.2 Drift Uncertainty (DU) ‣ 8 The drift") (DU) and [8.3](https://arxiv.org/html/2511.18125v1#S8.SS3 "8.3 Negative Return Correlations (NRC) ‣ 8 The drift") (NRC), the empirical statistics on the drifts are presented in Sec. [8.4](https://arxiv.org/html/2511.18125v1#S8.SS4 "8.4 Empirical validation: NRC ‣ 8 The drift"), and the analytical model for the drift uncertainty is given in the Appendix [A](https://arxiv.org/html/2511.18125v1#A1 "Appendix A A simple model with drift uncertainty").

The volatility dynamics is another important component of a process used to describe the time evolution of financial assets.
Since the seminal works of Engle and Bollerslev on ARCH processes [Engle, [1982](https://arxiv.org/html/2511.18125v1#bib.bib5); Bollerslev, [1986](https://arxiv.org/html/2511.18125v1#bib.bib3)], the heteroskedasticity, namely the non-constant volatility of the empirical data, has been recognized as an important stylized fact.
The extensive family of ARCH processes can model the changing volatility that occur in the financial time series.
Among them, the Long-Memory ARCH process (LMARCH) is a very good workhorse for many applications in finance [Zumbach, [2004](https://arxiv.org/html/2511.18125v1#bib.bib12), [2012](https://arxiv.org/html/2511.18125v1#bib.bib15)].
This process is fairly sparse, has a few parameters which do not need to be estimated on empirical data, and allows to compute volatility forecasts for any desired horizons.
In short, this process is a robust base model to describe the heteroskedasticity present in financial time series.

Our goal is to describe a multivariate universe of correlated indexes.
This raises significantly the challenge since a multivariate ARCH process is needed, a difficult task.
A key issue is the increasing number of parameters with the universe size nn, since the proposed extensions have a number of parameters growing as n2n^{2}, or even n4n^{4}, making them untractable even for moderate universe size.
Hence, the challenge is to write a simple but good enough multivariate ARCH process.
For this purpose, we leverage the good model of heteroskedasticity for all financial time series provided by the LMARCH process *with the same parameters*.
Essentially, the multivariate process is a cross-product of one univariate LMARCH process.
The number of parameters is given by the asymptotic long term covariance matrix, namely nn asset volatilities and n​(n−1)/2n(n-1)/2 correlations (all provided in the CMA), and a fixed number of parameters to describe the memory decay of the LMARCH process.
The multivariate dynamical model used for the covariance is described in Sec. [9](https://arxiv.org/html/2511.18125v1#S9 "9 The covariance"),
with an overview on this topic ([9.1](https://arxiv.org/html/2511.18125v1#S9.SS1 "9.1 Overview ‣ 9 The covariance")), the constant covariance model provided by the CMA ([9.2](https://arxiv.org/html/2511.18125v1#S9.SS2 "9.2 Constant Covariance ‣ 9 The covariance")), the LMARCH extension ([9.3](https://arxiv.org/html/2511.18125v1#S9.SS3 "9.3 LMARCH Covariance ‣ 9 The covariance")),
and the statistics for the volatility in [9.4](https://arxiv.org/html/2511.18125v1#S9.SS4 "9.4 Empirical validation: volatility ‣ 9 The covariance").
The asymptotic property of the mean covariance is verified in Appendix [C](https://arxiv.org/html/2511.18125v1#A3 "Appendix C Long term expectations").

The last component in the process is the multivariate random generator for the innovations.
The default solution is to use a normal generator, with covariance Σ\Sigma.
Yet, as shown by many empirical studies and by the investigations in Sec. [10](https://arxiv.org/html/2511.18125v1#S10 "10 Distribution for the returns and innovations") below, the distributions are clearly fat-tailed.
Moreover, a systematic asymmetry is observed, with larger down moves than up moves.
This asymmetry is observed for stock indexes (larger crashes than rallies), but also for fixed income indexes (more abrupt interest rate increases than decreases).
These observations call for an asymmetric fat-tailed distribution, and the univariate non-central Student distribution provides for a simple and good description of the empirical data.
For Monte Carlo simulations, a multivariate generator is needed, with a specified mean 𝝁\bm{\mu} and covariance 𝚺\bm{\Sigma}.
[McNeil et al., [2015](https://arxiv.org/html/2511.18125v1#bib.bib7)] gives an algorithm to generate multivariate non-central Student variates, but the mean and covariance cannot be specified simply.
This algorithm has been reformulated so that the mean and covariance are as specified.
The random generator issues are presented in ([10.1](https://arxiv.org/html/2511.18125v1#S10.SS1 "10.1 Random generators and non-central Student distribution ‣ 10 Distribution for the returns and innovations")), the analyses of the empirical and simulated distributions for the returns and innovations are provided in Sec. [10.2](https://arxiv.org/html/2511.18125v1#S10.SS2 "10.2 Empirical validation: innovation distributions ‣ 10 Distribution for the returns and innovations") and [10.3](https://arxiv.org/html/2511.18125v1#S10.SS3 "10.3 Empirical validation: return distributions ‣ 10 Distribution for the returns and innovations"), the random generator algorithm is detailed in Appendix [B](https://arxiv.org/html/2511.18125v1#A2 "Appendix B Non-Central Student-t: random draws and evaluation of 𝜃⁢(𝜈)").

Finally, 2 points need to be discussed with respect to Eq. [6](https://arxiv.org/html/2511.18125v1#S4.E6 "In 4 The multivariate process structure").
First, as such, the prices do not necessarily stay positive.
An absorbing state at zero is added, with p​(t+δ​t)p(t+\delta t) replaced by zero when p​(t+δ​t)≤pminp(t+\delta t)\leq p\_{\text{min}}.
The parameter pminp\_{\text{min}} can be set at a small enough value, appropriate for each index, say 1.
Since the intention is to model broad indexes, reaching the absorbing state means the bankruptcy of a state or an economy, an unlikely event.
At the start of a simulation, the current price p​(0)p(0) is known, and the minimal price is set at p​(0)/100p(0)/100.
If reaching such events are too likely in a simulation, this denotes that the model or the model’s parameters are inappropriate.
This consideration has lead to the introduction of the NRC term (negative return correlation) in order to stabilize the long term diffusion.
Yet, if this model is used for stocks, bankruptcy is a possible outcome and must be properly included.

Second, the simulation universe can be over several currencies, and FX rates need to be included.
This can be done in 2 ways.
If a reference currency is given, all indexes can be converted to the reference currencies, and the CMA parameters are including the exchange rates impacts.
This is the simplest solution with respect to the applications, since the FX rate effects are included in the CMA, but the CMA become dependent on the reference currency.
The second solution is to include explicitly the FX rates in the simulation universe, and to do the FX conversions where appropriate.
In this case, the CMA for the indexes are given in their respective home currency, but the simulation universe and the CMA have to be extended for the FX rates.
As an example, consider a fixed income index in EUR with a 1% (annualized) volatility, included in a USD portfolio.
The EUR/USD fx rate has a typical volatility of 8%.
With the first solution, the volatility of the fixed income EUR index is computed in USD, with a resulting volatility around 8% due to the FX fluctuations, while with the second solution, the FX rate is included explicitly and each components retain its volatility.
The first solution is simpler at the level of the implementation for the process and subsequent portfolio evaluation, the second is simpler for the evaluation of the CMA.
Yet, the equations [6](https://arxiv.org/html/2511.18125v1#S4.E6 "In 4 The multivariate process structure") remains unchanged for both solutions.
Beside, with respect to FX, all the empirical statistics reported in this paper have been evaluated in their home currency.

## 5 Definitions of historical return, volatility and innovation

The time interval of interest is denoted by Δ​T\Delta T, the time step for the historical data or the simulation process is δ​t\delta t.
The current time is tt, and the information is available up to this time (i.e. the filtration is ℱ​(t)\mathcal{F}(t)).
With a time series of prices p​(t)p(t), either historical or simulated, the (realized) relative return is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | r​(t;Δ​T)=p​(t)−p​(t−Δ​T)p​(t−Δ​T)r(t;\Delta T)=\frac{p(t)-p(t-\Delta T)}{p(t-\Delta T)} |  | (8) |

This definition is equivalent to Eq. [1b](https://arxiv.org/html/2511.18125v1#S2.E1.2 "In 1 ‣ 2 The base process settings"), but at the scale Δ​T\Delta T.
The resulting returns are at the scale Δ​T\Delta T, they can be annualized using the scaling r1y=rΔ​T​1y/Δ​Tr\_{\text{1y}}=r\_{\Delta T}\sqrt{\text{1y}/\Delta T}.

The forecast for the variance σ2\sigma^{2} over the interval [t,t+Δ​T][t,t+\Delta T] is computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(t;Δ​T)=∑t′≤tw​(t−t′,Δ​T)​r2​(t′;δ​t)=∑0≤l≤lmaxw​(l,Δ​T)​r2​(t−l​δ​t;δ​t)\sigma^{2}(t;\Delta T)=\sum\_{t^{\prime}\leq t}w(t-t^{\prime},\Delta T)\,r^{2}(t^{\prime};\delta t)=\sum\_{0\leq l\leq l\_{\text{max}}}w(l,\Delta T)\,r^{2}(t-l\,\delta t;\delta t) |  | (9) |

where the sum runs over t′t^{\prime} in the past of tt, namely t′=t−l​δ​tt^{\prime}=t-l\,\delta t, or equivalently over the lag ll.
The volatility forecast is at the scale δ​t\delta t, a pre-factor can be included in order to scale the variance at the scale Δ​T\Delta T or at 1 year.
The weights ww sum to 1 regardless of Δ​T\Delta T

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t′≤tw​(t−t′,Δ​T)=∑l≥0w​(l,Δ​T)=1.\sum\_{t^{\prime}\leq t}w(t-t^{\prime},\Delta T)=\sum\_{l\geq 0}w(l,\Delta T)=1. |  | (10) |

Essentially, the variance forecast at the horizon Δ​T\Delta T is a sum of the past squared returns at the scale δ​t\delta t, with weights depending on the distance to the present time tt, and on the forecast horizon Δ​T\Delta T.
The decay of the past information is set by w​(l,Δ​T)w(l,\Delta T) with ll the lag from the present time tt.
Different weights ww lead to various volatility estimators, and 2 estimators are used for the empirical analyses.

The first estimator is the RMA, for Rectangular Moving Average, with constant weights in a window of length Δ​T\Delta T, namely w​(l,Δ​T)=δ​t/Δ​Tw(l,\Delta T)=\delta t/\Delta T for 0≤l<Δ​T0\leq l<\Delta T and zero otherwise.
With this definition, σ​(t;Δ​T)\sigma(t;\Delta T) computes the realized volatility over the interval (t−Δ​T,t)(t-\Delta T,t), and does not use information in the past of t−Δ​Tt-\Delta T.

The second estimator is derived from the Long-Memory ARCH process.
This volatility process specifies the 1 step volatility weights w​(l,δ​t)w(l,\delta t) with a slow decay with respect to the lag ll, capturing the slow decay of the information as the return r​(t−l​δ​t;δ​t)r(t-l\,\delta t;\delta t) recedes in the distant past with increasing lag ll.
Because of its simple quadratic structure, expectations of the variance between tt and t+Δ​Tt+\Delta T can be evaluated analytically conditional on the information available up to tt. This expectation allows to compute variance forecasts for any horizon Δ​T\Delta T with the formula [9](https://arxiv.org/html/2511.18125v1#S5.E9 "In 5 Definitions of historical return, volatility and innovation") (rigorously, the forecasts should carry a tilde, and a volatility forecast is the square root of a variance forecast).
The weights w​(l,Δ​T)w(l,\Delta T) are computed from the 1-step weights w​(l,δ​t)w(l,\delta t) with a recursive equation.
The key point is that no new parameters are needed, namely the volatility forecast for the horizon Δ​T\Delta T is obtain from the 1-step forecast.
Moreover, the same parametric weights w​(l,δ​t)w(l,\delta t) describe correctly most free-floating financial assets, regardless of the asset type (indexes, equities, fixed incomes) and geographic area [Zumbach, [2006](https://arxiv.org/html/2511.18125v1#bib.bib13)].
In short, the LMARCH model is a good default model, that can be used for any time series, and without estimating specific parameters.
It is not the best model in store, but it is very efficient in term of capturing the heteroskedasticity, namely crashes versus quiet periods, and with a low complexity.

Eq. [1a](https://arxiv.org/html/2511.18125v1#S2.E1.1 "In 1 ‣ 2 The base process settings") is interesting to analyze historical time series because it allows us to define the realized innovations for one asset with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵ​(t+δ​t)=r​(t+δ​t)−μ​(t;δ​t)σ​(t;δ​t).\epsilon(t+\delta t)=\frac{r(t+\delta t)-\mu(t;\delta t)}{\sigma(t;\delta t)}. |  | (11) |

Essentially, this formula “de-GARCH” the returns.
In the process definition, it is assumed that the distribution pϵp\_{\epsilon} is stationary.
The equivalent statement on historical data is that Eq. [11](https://arxiv.org/html/2511.18125v1#S5.E11 "In 5 Definitions of historical return, volatility and innovation") should lead to a stationary time series, at least to a good approximation.
The formula [11](https://arxiv.org/html/2511.18125v1#S5.E11 "In 5 Definitions of historical return, volatility and innovation") is obtained from a process with a time step δ​t\delta t.
The same formula can be used at a scale Δ​T\Delta T to define ϵ​(t+Δ​T)\epsilon(t+\Delta T),
where σ\sigma is a volatility forecast for the horizon Δ​T\Delta T and computed at tt.
Essentially, this formula removes from r​(t+Δ​T)r(t+\Delta T) the information known at tt in term of the location μ​(t;Δ​T)\mu(t;\Delta T) and size σ​(t;Δ​T)\sigma(t;\Delta T), in order to measure the “surprise” ϵ​(t+Δ​T)\epsilon(t+\Delta T) over the interval Δ​T\Delta T.

From the empirical statistical analysis, long term asymptotic values are desired.
Usually in finance, the historical returns are used, say for example to estimate the mean variance.
Yet, the returns have a changing variance, namely the return are heteroskedastic, with very large crises recurring approximately each decade (for stocks over the last 30 years: dot.com bubble, subprime crisis, covid).
Hence, an asymptotic estimate for the variance requires a couple of decades of data.
The situation is similar with other estimates, say the return distribution and its tails, or lagged correlations.
Because stationary, the statistical properties of the innovations converge faster to their asymptotic (long sample) limits.
This is particularly interesting for studies at long time horizons, because the effective sample size is always small for large Δ​T\Delta T.

## 6 Statistical estimators

### 6.1 General context

Because of the poor samples for long term statistics, it is important to select good statistical estimators, for the distributions and for the dynamical properties.
Several strategies are used to extract at best information from historical data.

* •

  Obviously, use long time series, but this is limited by the availability of data.
  Another limit is the long term stability of the economy and the financial system, say at the scale of several decades.
* •

  Use a cross-section of indexes, for equities and fixed incomes, and with a good geographical coverage.
  The purpose here is to obtain *universal properties*, or “stylized facts”, namely statistics occurring similarly across indexes, eventually depending on the asset class (e.g.equity indexes versus fixed income indexes).
  Such properties allow to build universal and robust model for the process, by focusing only on the dominant behaviors.
  Yet, the correlations between indexes limit the diversification provided by large cross-sections, in particular for equity indexes.
* •

  Use efficient statistical estimators.
  Two statistics are used in this work.
  First, distributional information is needed, and *folded-cdf* are used to display the core and both tails of various quantities.
  Second, “*lag-one correlation*” statistics at increasing Δ​T\Delta T are used to obtain information about the dynamics.
  Both statistics are explained below.
* •

  Extract information about several quantities, in particular returns, volatilities and innovations.
  Sec. [5](https://arxiv.org/html/2511.18125v1#S5 "5 Definitions of historical return, volatility and innovation") gives the definitions used in this work.
* •

  Extract information on increasing time intervals, ranging from 1 month to a few years.
  In line with the effective sample size argument presented in the introduction, the statistical uncertainties grow with the analysis time interval Δ​T\Delta T.
  More confidence is build when a consistent picture emerges, when increasing Δ​T\Delta T and cross-sectionally.
* •

  Take care of the finite sample bias.
  Because the computed statistics are never in a large sample regime, important finite sample bias are present.
  Monte Carlo simulations with a base normal random walk allow to estimate the bias.

### 6.2 Folded-cdf

Given a sample of data, either from historical data or Monte Carlo simulations, the cdf (cumulative distribution function) can be evaluated simply by a counting procedure.
This contrast with a pdf where a density must be evaluated with some kernel, which is distorting the empirical data.
For the graphical representation, we plot the “folded-cdf”, or f-cdf, namely cdf⁡(x)\operatorname{cdf}(x) for cdf≤\operatorname{cdf}\leq 1/2, and 1−cdf⁡(x)1-\operatorname{cdf}(x) for cdf\operatorname{cdf} ¿ 1/2.
With this representation of f-cdf(xx) versus xx, a vertical logarithmic axis allows to show both tails of the cdf, together with the core of the distribution.
Cumulative probabilities are shown directly on the graph, allowing for a direct visualization of VaR values.
The cdf’s are computed for increasing Δ​T\Delta T on annualized data, in order to remove the trivial random walk scaling.
Showing on the same graph the folded-cdf for increasing Δ​T\Delta T emphasizes the similarities and changes in the distributions.
On some f-cdf graph, the cdf of a normal distribution as been added for comparison, represented with a dashed black line.
Its mean and standard deviation are the empirical moment estimators for the 1 month data.

### 6.3 Lag-one correlations

For two quantities XX and YY measured at a time horizon Δ​T\Delta T, the correlation between X​(t)X(t) and Y​(t+Δ​T)Y(t+\Delta T) gives the largest information contained in XX about the subsequent evolution of YY at the scale Δ​T\Delta T.
The time displacement in YY is chosen such that there is no trivial overlap in the underlying prices or returns for the computation of XX and YY.
For two quantities XX and YY, we call the “lag-one Δ​T\Delta T correlations” the lagged correlations at one-Δ​T\Delta T as function of Δ​T\Delta T.
The return-return lag-one correlations (Fig. [1](https://arxiv.org/html/2511.18125v1#S8.F1 "Figure 1 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift") to [3](https://arxiv.org/html/2511.18125v1#S8.F3 "Figure 3 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift")) are particularly important for the present analysis, since this modifies the long term dispersion of the prices.
Notice that this is different from the usual approach of computing XX and YY at the smallest scale δ​t\delta t, then to compute the lagged correlations for increasing lag k​δ​tk\,\delta t.
The variable is the increasing lag in the usual approach, whereas the increasing value Δ​T\Delta T is used as the parameter in our approach, a parameter that impacts both the quantities XX and YY, and the lag.
Because this maximizes the information about XX on the subsequent YY for all scales Δ​T\Delta T, there is no need to evaluate correlations for larger lags, say k​Δ​Tk\,\Delta T for k>1k>1.

The lag-one correlation for the volatility is also very important since measuring the heteroskedasticity, namely the clustering of the volatility as function of Δ​T\Delta T.
When using σLMARCH​[Δ​T]\sigma\_{\text{LMARCH}}[\Delta T] at tt and t+Δ​Tt+\Delta T, the long memory kernel creates a spurious dependency since some squared returns are common to both volatilities.
Furthermore, the volatility has a clearly skewed distribution, whereas the logarithmic volatility shows a more symmetric distribution.
In order to avoid both issues, the heteroskedasticity is best quantified with X=log⁡(σLMARCH​[Δ​T])X=\log(\sigma\_{\text{LMARCH}}[\Delta T]) (with σLMARCH​[Δ​T]\sigma\_{\text{LMARCH}}[\Delta T] a volatility forecast for a time horizon Δ​T\Delta T computed with an LMARCH process), and Y=log⁡(σRMA​[Δ​T])Y=\log(\sigma\_{\text{RMA}}[\Delta T]) (a volatility computed with equal weights over a span Δ​T\Delta T of monthly squared returns).

For Monte Carlo simulations, the lag-one correlations ρX,Y​(Δ​T)\rho\_{X,Y}(\Delta T) are computed for each path.
Then, the average mMC, X, Ym\_{\text{MC, X, Y}} and standard deviation σMC, X, Y\sigma\_{\text{MC, X, Y}} of ρX,Y\rho\_{X,Y} are evaluated over the paths.
On the graph for the lag-one correlation obtained from Monte Carlo simulations, see figures [3](https://arxiv.org/html/2511.18125v1#S8.F3 "Figure 3 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift") and [5](https://arxiv.org/html/2511.18125v1#S9.F5 "Figure 5 ‣ 9.4 Empirical validation: volatility ‣ 9 The covariance"), the average mMCm\_{\text{MC}} is plotted with a black line.
Two red lines are added at a distance of ±1.95​σMC\pm 1.95\sigma\_{\text{MC}} to denote the 95% confidence bounds for this quantity.
Since the Monte Carlo simulations are done for the same time length as the empirical data, a similar confidence bound can be assumed for the empirical graphs.

## 7 Empirical data

A good model should reproduce at best the statistical properties of financial markets.
A validation must be done comparing some statistics computed with market prices and with Monte Carlo simulations.
The difficulties are on the market data side, since an order of 20 years of historical data are available with a large market cross-section.
At the scale of 1 month to a few years, empirical statistics can be computed, even though the error bars are quite large.
This is not comfortable, but this is the best we can do.

Most of the figures included in this document have been computed with the time series for the MSCI index “World Net Total Return USD Index”, Bloomberg ticker ’SPTR’, and called “Developed World Equity” for short in this document.
This index represents the worldwide state of the stock market, summarizing many indexes.
For the bond market, the index “Bloomberg Barclays US Agg Total Return” is used, ticker ’LBUSTRUU’, and called ’U.S. Aggregate Bonds’ for short in this document.

The empirical samples used for most figures in this document start on 2000-01-31 and end on 2024-02-29 for all time series, giving a sample size of 24 years, with a good cross-section.
Clearly, the effective sample size is inconveniently small above one year, but this sample is characteristic of the recent market conditions.
In order to limit the number of figures, only computations done on this 2000-2024 sample are reported, together with simulations done on an equivalent 24 years period.

Some time series are available on longer samples, say starting in 1970, giving us 54 years of data, but with a much smaller cross-section.
Yet, the period 1970 to 1990 was characterized by a high inflation, and high interest rates, whereas the inflation is consistently low since 1990.
This difference distorts some statistics, in particular related to the long term mean returns and drifts, which become larger.
Otherwise, most statistics on distributions and lagged correlations give similar results on this longer sample.
Such consistency with a longer sample (but a smaller cross-section) give us some confidence about the estimation of long term statistical properties.

Underlying this discussion is a stationary hypothesis for the economy, clearly important when doing projection at the scale of decades.
Beside the changing level for the inflation and interest rates, no obvious changes are observed in the historical data.
This stationarity brings support to estimate the CMA over a few decades of historical data, and to the process used to simulated the possible market evolution.
Going beyond that would require to include in the model the inflation level, and its relation to interest rates and fixed income indexes.
This is clearly an interesting econometric project, which is left for further investigations.

## 8 The drift

### 8.1 Overview

As discussed in the introduction, the drift 𝝁​(t)\bm{\mu}(t) is an essential part of the process equation for long term simulations.
For a time horizon of 15 years and above, the random process is always in the drift dominated regime, hence the crucial importance of the drift for long term simulations.
The simplest model for the drift is a constant value, say as given by the CMA parameters

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝁​(t)=𝝁CMA.\bm{\mu}(t)=\bm{\mu}\_{\text{{\scriptsize CMA}}}. |  | (12) |

This base model is used almost universally for simulations, with the value for μ\mu representing the long term grow of the economy (and the inflation) for the corresponding index.
For long-term Monte Carlo simulations, two modifications of this base constant model can be made.

First, the value for μCMA\mu\_{\text{{\scriptsize CMA}}} is indeed a long term point forecast, a notoriously difficult number to evaluate, and which contains an error compared to the unknown realized value.
The past is certainly of some help, and the mean historical drift over the past few decades can be used (with a stationary hypothesis to project the past values in the future).
Yet, large error bars should be assumed.
This error is quantitatively important, because the end value for the drift is Δ​T​μ\Delta T\,\mu, hence the error is also multiplied by Δ​T\Delta T.
This issue is summarized in subsection [8.2](https://arxiv.org/html/2511.18125v1#S8.SS2 "8.2 Drift Uncertainty (DU) ‣ 8 The drift") below, and explored in depth for a simple model in appendix [A](https://arxiv.org/html/2511.18125v1#A1 "Appendix A A simple model with drift uncertainty").
Assuming a normal distribution for the drift, its impact is investigated analytically on a simple normal random walk.
The analytic computation allows to understand the impact of the errors on the drift values, and the process is modified to include the uncertainty on the drift.
This modification is called the Drift Uncertainty (DU).
In the Monte Carlo simulations, the DU is included simply by altering the mean drift by a random term.
This term is defined and analyzed in subsection [8.2](https://arxiv.org/html/2511.18125v1#S8.SS2 "8.2 Drift Uncertainty (DU) ‣ 8 The drift").
As an alternative, an econometric approach of the uncertainty on the CMA is presented in [Ortec Finance, [2021](https://arxiv.org/html/2511.18125v1#bib.bib9)].

Lagged correlations for the returns and innovations point to positive correlations up to a few months, and negative correlations around a few years.
Such statistics are in agreement with short term “trend following” of traders, and with a “mean reversion” at longer time scales.
This behavior is embedded in the drift dynamics 𝝁​(t)\bm{\mu}(t) by lagged return terms, generating similar statistics in Monte Carlo simulations.
The most important term is the negative lagged correlations, which introduce a correcting effect after large drops or rises in the simulated prices, effectively “stabilizing” the long term process.
We have called this term *Negative Return Correlation* (NRC).
The mechanism is similar to an AR (Auto Regressive) process, but for the present long term problem the drift equation has been modified in order to have simple terms acting at selected time scales.
This term is defined and analyzed in subsection [8.3](https://arxiv.org/html/2511.18125v1#S8.SS3 "8.3 Negative Return Correlations (NRC) ‣ 8 The drift").

Consider now the standard deviation σW\sigma\_{\text{W}} of the terminal wealth of simulated paths at a given Δ​T\Delta T, with the volatility for the paths given by σdiffusion\sigma\_{\text{diffusion}}.
Let us emphasize that σW\sigma\_{\text{W}} measures the cross-sectional dispersion of the simulated values while σdiffusion\sigma\_{\text{diffusion}} measures the volatility in the time direction of the paths.
With a constant drift, the standard deviation is directly related to the volatility by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σW​(Δ​T)=Δ​T​σdiffusion\sigma\_{\text{W}}(\Delta T)=\sqrt{\Delta T}\,\sigma\_{\text{diffusion}} |  | (13) |

regardless of μ\mu.
Let us consider a stock index, with a typical annualized volatility of σdiffusion=\sigma\_{\text{diffusion}}= 20%.
At the scale of 16 years, these values lead to σW\sigma\_{\text{W}} = 80%.
This is a very large uncertainty on the terminal values, leading to large probabilities for implausible large gains or losses (quantitatively depending also on μ\mu).
This feature is not realistic, since financial markets in the long term tend to correct themselves, with exuberant periods followed by crashes, and crashes followed by recoveries.
This is precisely the behavior introduced in the process by the negative return correlations.
Its impact is to lower σW\sigma\_{\text{W}} compared to Δ​T​σdiffusion\sqrt{\Delta T}\,\sigma\_{\text{diffusion}}, modifying the relation [13](https://arxiv.org/html/2511.18125v1#S8.E13 "In 8.1 Overview ‣ 8 The drift").
Then, the random uncertainty on the drift has the effect to increase the dispersion of the paths, effectively increasing σW\sigma\_{\text{W}} as Δ​T3/2=Δ​T1/2⋅Δ​T\Delta T^{3/2}=\Delta T^{1/2}\cdot\Delta T and altering the scaling in Eq. [13](https://arxiv.org/html/2511.18125v1#S8.E13 "In 8.1 Overview ‣ 8 The drift").
In short, the NRC term decreases σW\sigma\_{\text{W}} while the DU increases σW\sigma\_{\text{W}} proportionally to Δ​T\Delta T.
Both terms in μ​(t)\mu(t) modify σW​(Δ​T)\sigma\_{\text{W}}(\Delta T) and the parameters in the drift become important for the path dispersion, and for the control of the risk of an investment strategy.

### 8.2 Drift Uncertainty (DU)

The base constant drift 𝝁CMA\bm{\mu}\_{\text{{\scriptsize CMA}}} is a point forecast for the forthcoming realized drift, and as any forecast, it has an inherent uncertainty.
A better point of view is to replace the point forecast by a distributional forecast p​(μ)p(\mu), acknowledging the uncertainty in μ\mu.
With this view, the CMA drift parameter is an estimate for the mean drift μ¯\overline{\mu}, and the related uncertainty parameter σμ\sigma\_{\mu} should be estimated.
In a first step, the distribution for μ\mu can be taken as a normal distribution.
A simple model along these lines is explored analytically in the appendix [A](https://arxiv.org/html/2511.18125v1#A1 "Appendix A A simple model with drift uncertainty").
In particular, it allows to relate the uncertainty σμ\sigma\_{\mu} on μ\mu to the volatility σdiffusion\sigma\_{\text{diffusion}} and to the length Δ​Tcal\Delta T\_{\text{cal}} of a (hypothetical) calibration sample used to estimate the historical drift μ^\hat{\mu}.
The analytical result is that σμ\sigma\_{\mu} is proportional to σdiffusion\sigma\_{\text{diffusion}} and inversely proportional to Δ​Tcal\sqrt{\Delta T\_{\text{cal}}}, namely a good drift estimate is obtained with a small volatility and a long sample.

In Monte Carlo simulations, the uncertainty on the drift can be incorporated by adding a random component to the drift for each path using

|  |  |  |  |
| --- | --- | --- | --- |
|  | μDU(k)=σCMAΔ​Tcal​ϵ(k)\mu\_{\text{DU}}^{(k)}=\frac{\sigma\_{\text{{\scriptsize CMA}}}}{\sqrt{\Delta T\_{\text{cal}}}}\,\epsilon^{(k)} |  | (14) |

where ϵ(k)∼𝒩​(0,1)\epsilon^{(k)}\sim\mathcal{N}(0,1) and kk indexes the paths.
In a multivariate context, the uncertainty ϵ(k)\epsilon^{(k)} is drawn independently for each time series.
The parameter Δ​Tcal\Delta T\_{\text{cal}} calibrates the importance of this term, and its quantitative impact on the standard deviation.

As shown in appendix [A](https://arxiv.org/html/2511.18125v1#A1 "Appendix A A simple model with drift uncertainty"), the effect of the random drift is to increase the standard deviation of the prices at a given time horizon Δ​T\Delta T by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σW​(Δ​T)≃Δ​T​σdiffusion, 1y​(1+12​Δ​TΔ​Tcal).\sigma\_{\text{W}}(\Delta T)\simeq\sqrt{\Delta T}\,\sigma\_{\text{diffusion, 1y}}\left(1+\frac{1}{2}\,\frac{\Delta T}{\Delta T\_{\text{cal}}}\right). |  | (15) |

where σdiffusion, 1y\sigma\_{\text{diffusion, 1y}} is the annualized volatility along the paths.
In particular, the correction term grows as Δ​T\Delta T, namely the drift uncertainty makes the uncertainty on the terminal value to increase faster than Δ​T\sqrt{\Delta T} when Δ​T>Δ​Tcal\Delta T>\Delta T\_{\text{cal}}.
The numerical simulations have been done with Δ​Tcal\Delta T\_{\text{cal}} = 25 years, leading to an increase of σW\sigma\_{\text{W}} by a factor 1.5 after 25 years.

### 8.3 Negative Return Correlations (NRC)

A discussed around Eq. [13](https://arxiv.org/html/2511.18125v1#S8.E13 "In 8.1 Overview ‣ 8 The drift"), the purely diffusive volatility σdiffusion\sigma\_{\text{diffusion}} leads to large dispersions for the standard deviation of the price σW\sigma\_{\text{W}} at long horizons, mainly for stock indices.
In particular, some paths can end in the “bankrupt” area, with very small values.
Such occurrences are possible for individual stocks, but unlikely for indices constructed from the largest stocks on an exchange.
In order to have realistic long term distributions, a long-term mechanism to reduce the dispersion needs to be introduced.

This is done with a negative correlation between returns, introduced at a few selected time interval Δ​Tk\Delta T\_{k}.
The NRC drift component for a given asset is introduced with the following term

|  |  |  |  |
| --- | --- | --- | --- |
|  | μNRC​(t)=∑kγk​δ​tΔ​Tk​(p​(t)D−1​(Δ​Tk)​p​(t−Δ​Tk)−1).\mu\_{\text{NRC}}(t)=\sum\_{k}\gamma\_{k}\,\frac{\delta t}{\Delta T\_{k}}\,\left(\frac{p(t)}{D^{-1}(\Delta T\_{k})\,p(t-\Delta T\_{k})}-1\right). |  | (16) |

The discount factor D​(Δ​T)D(\Delta T) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​(Δ​T)=(1+μCMA)−Δ​T/δ​t,D(\Delta T)=(1+\mu\_{\text{{\scriptsize CMA}}})^{-\Delta T/\delta t}, |  | (17) |

and D−1​(Δ​T)D^{-1}(\Delta T) moves forward the price by Δ​T\Delta T.
In ([17](https://arxiv.org/html/2511.18125v1#S8.E17 "In 8.3 Negative Return Correlations (NRC) ‣ 8 The drift")), μCMA\mu\_{\text{{\scriptsize CMA}}} is the drift at scale δ​t\delta t and plays the role of the interest rate.
Since Δ​Tk\Delta T\_{k} can be of the order of years, it is important for the historical return evaluation to properly move to tt the price p​(t−Δ​Tk)p(t-\Delta T\_{k}).
In Eq. [16](https://arxiv.org/html/2511.18125v1#S8.E16 "In 8.3 Negative Return Correlations (NRC) ‣ 8 The drift"), the term in parentheses is the return at scale Δ​Tk\Delta T\_{k}, computed at tt.
The term δ​t/Δ​Tk\delta t/\Delta T\_{k} is a convenient scaling factor so that all historical returns are scaled to δ​t\delta t, regardless of Δ​Tk\Delta T\_{k}.
The coefficient γk\gamma\_{k} fixes the magnitude of the return correlation at the time scale Δ​Tk\Delta T\_{k}.
In order to obtain the actual history dependent drift, the NRC drift component is added to the base constant drift, and possibly a DU component is also added.

In Eq. [16](https://arxiv.org/html/2511.18125v1#S8.E16 "In 8.3 Negative Return Correlations (NRC) ‣ 8 The drift"), if γ\gamma is positive, the past returns are amplified, while a negative γ\gamma dampens the price fluctuations by inducing a correction in the opposite direction.
The coefficients γk\gamma\_{k} have been adjusted so that the process match the empirical statistics for the lag-one correlations for the returns and innovations, see the figure [3](https://arxiv.org/html/2511.18125v1#S8.F3 "Figure 3 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift") for such an investigation.
Two time horizons Δ​Tk\Delta T\_{k} already provide for a satisfactory agreement with empirical lagged correlations for the returns, while 3 time horizons do not improve significantly.
The parameter γk\gamma\_{k} can in principle be adjusted for each index, we found that it is sufficient to have values depending only on the asset class.
This is consistent with the view that all the stock indexes behave statistically in a similar way, but stock and bond indexes could have a different dynamics.

In finance, many diffusion models include a mean reverting component, mainly to describe interest rate dynamics or stochastic volatility dynamics.
Generically, they are known as Orstein-Uhlenbeck (OU) processes, or as CIR processes for interest rates, with analytical solutions for the simplest specifications.
The drift equation in a OU process can be adapted to our long-term simulation horizon.
An OU diffusion acts similarly as the NRC term by limiting the diffusion, but over the full drifted path for a OU term while only at the scale Δ​Tk\Delta T\_{k} for the NRC.
The OU term is stronger, leading to a constant asymptotic standard deviation, namely σvalue​(Δ​T)\sigma\_{\text{value}}(\Delta T) is not growing with Δ​T\sqrt{\Delta T} but converges to a constant for large Δ​T\Delta T.
This limited diffusion behavior is realistic for interest rates and implied volatilities that are fundamentally bounded, but not for stock indexes which can grow without limitation.
Hence our focus on the NRC term.

### 8.4 Empirical validation: NRC

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 1: Lag-one correlations for the returns (top) and innovations (bottom), for equity indices.



![Refer to caption](x3.png)

![Refer to caption](x4.png)

Figure 2: Lag-one correlations for the returns (top) and innovations (bottom), for fixed income indices.

A drift term depending on the past values introduces lagged correlations between returns and between innovations (for Δ​T>δ​t\Delta T>\delta t).
This is most efficiently measured by using the “lag-one” correlation for the returns and the innovations, as described in Sec. [6.3](https://arxiv.org/html/2511.18125v1#S6.SS3 "6.3 Lag-one correlations ‣ 6 Statistical estimators").
Figures [1](https://arxiv.org/html/2511.18125v1#S8.F1 "Figure 1 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift") and [2](https://arxiv.org/html/2511.18125v1#S8.F2 "Figure 2 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift") display the lag-one correlations respectively for a set of stock indices and bond indices, computed with a sample from 2000-01-31 to 2024-02-29.
The similarity between all the curves points to a universal behavior (within each asset class), that can be reproduced with one set of parameters (per asset class) for the NRC term.
The same computation for a few time series starting in 1970 gives a similar figure, as well as a larger sample on a shorter time span.
Hence, these empirical correlations seem fairly robust against the choice of time series and sample periods (the fixed income indices being the most sensitive to the start and end dates).
Yet, the substantial correlations between markets introduce an unquantified dependency between the lag-one correlations, making dependent the various curves in these figures.
The weakest dependency is between equities and bonds, and the similarities between Fig [1](https://arxiv.org/html/2511.18125v1#S8.F1 "Figure 1 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift") and [2](https://arxiv.org/html/2511.18125v1#S8.F2 "Figure 2 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift") point to a similar behavior.

On the empirical figure for equity indexes, positive lagged correlations are observed at a scale of one to a few months.
Likely, these positive correlations result from trend following market participants.
At the scale of 1 year to a few years, negative lagged correlations are observed, with values of the order of -30% to -60% for stock indices.
These negative correlations indicate medium term market corrections, with moves in one direction followed by a move in the opposite direction.

The short term interest rates have positive lagged correlations, say up to 1 year, likely due to the decision pattern of the central banks: their decisions on the overnight rates are to increase or decrease by small increments but many times and over a long period.
In turn, these decisions propagate toward longer maturities along the yield curves.
This decision pattern induces clear lagged correlations, mainly for the short term bonds, but also for longer maturities.
Beside, the main bond markets are US and Europe, and these central banks have correlated behaviors.
These two effects make difficult the construction of a set of independent bond indexes.
The indexes used for the figure [2](https://arxiv.org/html/2511.18125v1#S8.F2 "Figure 2 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift") are US and European specific indexes, mitigating somehow these correlations.
At the scale of 1 year to a few years, negative lagged correlations are observed, with values of the order of 10 to -30% for bond indices.

Based on the empirical correlations, 2 terms have been added in the drift according to Eq. [16](https://arxiv.org/html/2511.18125v1#S8.E16 "In 8.3 Negative Return Correlations (NRC) ‣ 8 The drift"), at scale of 6 months with a positive coefficient and at scales 40 months with negative coefficients.
The resulting lag-one correlations are plotted in [3](https://arxiv.org/html/2511.18125v1#S8.F3 "Figure 3 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift"), which reproduces the main characteristics of figures [1](https://arxiv.org/html/2511.18125v1#S8.F1 "Figure 1 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift") and [2](https://arxiv.org/html/2511.18125v1#S8.F2 "Figure 2 ‣ 8.4 Empirical validation: NRC ‣ 8 The drift").
For the 2 models without NRC (line b and c on the figure), notice the downward tendency for large Δ​T\Delta T, whereas these models have a zero lagged correlation for all Δ​T\Delta T.
This tendency is due to a small sample bias for this statistical estimator, which is hidden by the lagged correlations in line a and d.

![Refer to caption](x5.png)

![Refer to caption](x6.png)

(a) Historical time series: ’Developed World Equity’ (left),
’U.S. Aggregate Bonds’ (right).

![Refer to caption](x7.png)

![Refer to caption](x8.png)

(b) Simulated time series: constant drift; constant covariance; normal innovations.

![Refer to caption](x9.png)

![Refer to caption](x10.png)

(c) Simulated time series: constant drift; LMARCH; NC-Student innovations.

![Refer to caption](x11.png)

![Refer to caption](x12.png)

(d) Simulated time series: drift with NRC and DU; LMARCH; NC-Student innovations.

Figure 3: 
The lag-one correlations between the returns (historical and realized), versus the time horizon Δ​T\Delta T on the x-axis, for empirical data and various processes.

## 9 The covariance

### 9.1 Overview

The covariance matrix is the multivariate extension of the squared volatility, and it controls several aspect of the process.
First, it fixes the volatility of each indexes, and the correlations between them.
This can be achieved by a constant covariance, with n​(n+1)/2n(n+1)/2 parameters.
A constant covariance term also fixes the long term properties of more sophisticated model.
Second, a dynamic component can be added, in the spirit of the GARCH(1, 1) process for the univariate case.
The vast family of ARCH-like processes provides for many analytical structures that can capture features of empirical time series with various level of details.
At the core, these processes can model the quiet periods, agitated periods, and crises that are observed in the economy and in the financial time series.

A vast literature exists on the multivariate extension of ARCH like models, in general leading to very complex model for increasing size nn.
The Multivariate Generalized Autoregressive Conditional Heteroskedasticity (MGARCH) model, along with its extensions, could be used for multivariate portfolio simulation, see e.g. [Bauwens et al., [2006](https://arxiv.org/html/2511.18125v1#bib.bib2)] for a review.
Yet, many of these models suffer from a significant limitation because the number of parameters increases rapidly with the number of assets.
For instance in the BEKK(1,1,1) model (see [Engle and Kroner, [1995](https://arxiv.org/html/2511.18125v1#bib.bib6)]), there are n​(5​n+1)/2n(5n+1)/2 parameters, resulting in 24 parameters for only three assets.
Such models are clearly unsuitable for a large universe, due to the quadratic grow of the number of parameters that must be estimated.

In order to construct a simple model regardless of the universe size, we are using a convex combination between a constant covariance and a dynamical part built from a Long Memory ARCH (LMARCH) process.
The LMARCH component captures efficiently the dynamics of the volatility, and importantly with the same few parameters for all time series.
The convex combination between the static and dynamic estimations is controlled by 1 parameter denoted by w∞w\_{\infty}, building an affine model for the covariance (as a function of the squared returns).
This model is minimal, yet describes correctly the key aspects of the multivariate volatility dynamics.

The static and dynamic components of the covariance matrix are introduced in the next two subsections, followed by a comparison between the lagged correlation of the volatility for empirical data and for numerical simulations.

### 9.2 Constant Covariance

The simplest possible model for the covariance is to take a constant matrix, with the values given by the CMA parameters.
The covariance is conveniently decomposed into volatility and correlation using

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺​(t)=𝚺CMA=𝝈CMA⋅𝝆CMA⋅𝝈CMA\displaystyle\bm{\Sigma}(t)=\bm{\Sigma}\_{\text{{\scriptsize CMA}}}=\bm{\sigma}\_{\text{{\scriptsize CMA}}}\cdot\bm{\rho}\_{\text{{\scriptsize CMA}}}\cdot\bm{\sigma}\_{\text{{\scriptsize CMA}}} |  | (18) |

where 𝝆CMA\bm{\rho\_{\text{{\scriptsize CMA}}}} is the correlation matrix and 𝝈CMA\bm{\sigma}\_{\text{{\scriptsize CMA}}} the diagonal matrix of volatilities.
This model has nn parameters for the volatilities and n​(n−1)/2n(n-1)/2 parameters for the correlations, leading to a total of n​(n+1)/2n(n+1)/2 parameters.
These parameters are set in the CMA (Capital Market Assumptions).
For Monte Carlo simulations, the constant covariance has the advantage that its square root can be computed once, leading to fast simulations.

In general, the volatilities provided in the CMA are at an annual scale.
They must be scaled at δ​t\delta t using a factor (δt/1y)\sqrt{(}\delta t/\text{1y}).

### 9.3 LMARCH Covariance

For univariate time series, the LMARCH process proved to be a very convenient workhorse for several financial applications, see e.g. [Zumbach, [2012](https://arxiv.org/html/2511.18125v1#bib.bib15)] and the reference therein.
The long memory embedded in the weights captures correctly the slow decay of the correlations for the volatility.
Another point of view is that the clustering of the volatility occurs at time scales ranging from days to years, and a processes with one time scale like I-GARCH(1) or GARCH(1,1) are unable to reproduce such behaviors which requires a multi-scale model.
Another very interesting property of the LMARCH model is its very sparse parametrization, and the ability to describe well most time series with the same small set of parameters.
Essentially, the memory kernel for the volatility depends on 1 parameter fixing the decay of the weights, while the other parameters are essentially cut-offs that are less important.
For these reasons, this process can be used for many applications (risk valuation, portfolio covariance estimate, option pricing), without the necessity to optimize parameters.

As given by Eq. [9](https://arxiv.org/html/2511.18125v1#S5.E9 "In 5 Definitions of historical return, volatility and innovation"), the univariate linear LMARCH process evaluates the covariance with a sum of past squared returns, with weights decaying gradually as the lag increases.
Because of its simple quadratic structure, it generalizes naturally in the multivariate case

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ΣLM-ARCH, linearα,β​(t;δ​t)=\displaystyle\Sigma\_{\text{LM-ARCH, linear}}^{\alpha,\beta}(t;\delta t)= |  | (19) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑0≤l<lmaxw​(l,δ​t)​(rα​(t−l​δ​t;δ​t)−μα)⋅(rβ​(t−l​δ​t;δ​t)−μβ).\displaystyle\hskip 20.00003pt\sum\_{0\leq l<l\_{\text{max}}}w(l,\delta t)~\left(r\_{\alpha}(t-l\,\delta t;\delta t)-\mu\_{\alpha}\right)\cdot\left(r\_{\beta}(t-l\,\delta t;\delta t)-\mu\_{\beta}\right). |  |

where α\alpha and β\beta index the time series.
Notice that the weight function w​(l,δ​t)w(l,\delta t) does not have a dependency on α\alpha and β\beta, namely the weights are independent of the time series.
This simple extension was used in [Zumbach, [2011](https://arxiv.org/html/2511.18125v1#bib.bib14)] to investigate the empirical properties of large covariance matrices.

A process with the covariance defined by Eq. [19](https://arxiv.org/html/2511.18125v1#S9.E19 "In 9.3 LMARCH Covariance ‣ 9 The covariance") is purely auto-regressive, similar to an I-GARCH process for the univariate case.
For Monte Carlo simulations, the mean volatility is not defined by the covariance, and such processes are unstable (more precisely the asymptotic probability distribution is singular, see [Nelson, [1990](https://arxiv.org/html/2511.18125v1#bib.bib8); Corradi, [2000](https://arxiv.org/html/2511.18125v1#bib.bib4)] for an analysis using the I-GARCH(1) model).
A mean covariance must be added in order to stabilize the process for long term simulations, leading to an affine model for the covariance (affine in term of the squared returns and covariance).
For the multivariate case, this leads to the covariance

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺​(t;δ​t)=𝚺LM-ARCH, affine​(t)=w∞⋅𝚺CMA+(1−w∞)⋅𝚺LM-ARCH, linear​(t;δ​t)\displaystyle\bm{\Sigma}(t;\delta t)=\bm{\Sigma}\_{\text{LM-ARCH, affine}}(t)=w\_{\infty}\cdot\bm{\Sigma}\_{\text{{\scriptsize CMA}}}+(1-w\_{\infty})\cdot\bm{\Sigma}\_{\text{LM-ARCH, linear}}(t;\delta t) |  | (20) |

with 0≤w∞≤10\leq w\_{\infty}\leq 1.
The parameter w∞w\_{\infty} controls the balance between the long term covariance and the auto-regressive covariance.
Large values for w∞w\_{\infty} lead to a model close to a constant covariance, with small volatility clustering, narrow distributions for the volatility, and small lagged correlations for the volatility, while small values for w∞w\_{\infty} leads to larger excursion of volatility, in line with typical market behavior.

For the Monte Carlo simulations, the parameter w∞w\_{\infty} has been adjusted so that the probability distributions and the lagged correlations of the volatility match at best between empirical and simulated time series.
These statistics point to low value for w∞w\_{\infty}.
Yet, with long term simulations, a small value for w∞w\_{\infty} can lead to small values for the simulated prices.
In practice, an index value p​(t)p(t) smaller than 1/100 of the initial value p​(0)p(0) is considered as unrealistic (at least for the indexes used in this study).
A similar argument can be made for unrealistic large values.
This condition induces a lower bound on w∞w\_{\infty}, given by the probability of too small prices to be negligible.

This trade-off is also influenced by the model used for the drift, either constant or with a NRC term.
Negative return correlations stabilize the long term process, reducing the width for the terminal wealth’s distribution, hence diminishing the probability for unrealistic low or high values.
With a NRC term in the drift, a lower value for w∞w\_{\infty} can be used, leading to a better agreement with empirical statistics.

### 9.4 Empirical validation: volatility

![Refer to caption](x13.png)

![Refer to caption](x14.png)

Figure 4: Lag-one correlations for the volatilities for equity indexes (top) and fixed income indices (bottom).

The volatility dynamics is measured by the lagged correlations for the volatility, with their definitions given in Sec. [5](https://arxiv.org/html/2511.18125v1#S5 "5 Definitions of historical return, volatility and innovation").
The graph [4](https://arxiv.org/html/2511.18125v1#S9.F4 "Figure 4 ‣ 9.4 Empirical validation: volatility ‣ 9 The covariance") shows the empirical lag-one correlations between the historical LMARCH volatility and the realized RMA volatilities at increasing time scale Δ​T\Delta T.
The parameters Δ​T\Delta T is on the horizontal axis, and the lagged correlations are evaluated for a selection of equity and fixed income indices.
Essentially, these graphs measure the dependency from the past of the volatility at increasing time horizons Δ​T\Delta T, from 1 month to 8 years.
Overall, the correlation is in the 20 to 40% range for Δ​T\Delta T between a few months to 1 year.
This is quantitatively the largest dynamical effect of financial time series, showing the importance of the volatility clustering.

![Refer to caption](x15.png)![Refer to caption](x16.png)

(a) Historical time series: ’Developed World Equity’ (left),
’U.S. Aggregate Bonds’ (right).

![Refer to caption](x17.png)

![Refer to caption](x18.png)

(b) Simulated time series: constant drift; constant covariance; normal innovations.

![Refer to caption](x19.png)

![Refer to caption](x20.png)

(c) Simulated time series: constant drift; LMARCH; NC-Student innovations.

![Refer to caption](x21.png)

![Refer to caption](x22.png)

(d) Simulated time series: drift with NRC and DU; LMARCH; NC-Student innovations.

Figure 5: Lag-one correlations for the volatility. Empirical (top) and for 4 processes.

The graph [5](https://arxiv.org/html/2511.18125v1#S9.F5 "Figure 5 ‣ 9.4 Empirical validation: volatility ‣ 9 The covariance") shows the “lag-one” correlation of the volatility for some processes.
The graphs on line a are based on empirical time series, with the indexes given in the caption.
The graphs in line b use a process with constant covariance.
Since the volatility dynamics is absent for this process, this correlation is zero.
Notice the negative biases due to the small effective sample at increasing Δ​T\Delta T.
The graphs on line c are computed with no NRC term, a LMARCH process (with w∞=0.55w\_{\infty}=0.55), and a non-central Student distribution,
while the graphs on line d are computed with a NRC term, a LMARCH process (with w∞=0.40w\_{\infty}=0.40), and a non-central Student distribution.
A process with no NRC and w∞=0.40w\_{\infty}=0.40 is not shown: it has a finite probability to end in the “bankrupt” domain with too small values, which is not realistic.
Essentially, the NRC term is acting to lower the terminal wealth variance.
The qualitative behavior reproduces well the empirical correlations, albeit quantitatively on the small side.
More sophisticated models would be needed to reach a better quantitative agreement.

![Refer to caption](x23.png)

![Refer to caption](x24.png)

(a) Historical time series: ’Developed World Equity’ (left),
’U.S. Aggregate Bonds’ (right).

![Refer to caption](x25.png)

![Refer to caption](x26.png)

(b) Simulated time series: constant drift; constant covariance; normal innovations.

![Refer to caption](x27.png)

![Refer to caption](x28.png)

(c) Simulated time series: constant drift; LMARCH; NC-Student innovations.

![Refer to caption](x29.png)

![Refer to caption](x30.png)

(d) Simulated time series: drift with NRC and DU; LMARCH; NC-Student innovations.

Figure 6: The folded-cdf for the volatility (measured with equal weights in the interval Δ​T\Delta T), at increasing time horizon Δ​T\Delta T.

The distribution for the volatility is important since depending on its dynamics, and controlling partly both tails of the return distributions.
Figure [6](https://arxiv.org/html/2511.18125v1#S9.F6 "Figure 6 ‣ 9.4 Empirical validation: volatility ‣ 9 The covariance") shows the folded-cdf for the RMA volatility over the period Δ​T\Delta T, and annualized.
The figure compares the empirical distributions for the same processes.
Clearly, a process with constant covariance cannot reproduce the broader distributions of the empirical volatility.
Another default of the constant covariance is the fast convergence to the long term volatility, since the width of the distribution is depending only on the number of squared returns in the evaluation of the volatility (i.e. decreasing as 1m/Δ​T\sqrt{\text{1m}/\Delta T} for monthly returns).
The bottom figure shows the good agreement between the LMARCH process and the empirical cdf, emphasizing the impact of the volatility dynamics on the distribution.
As a caveat, the CMA used for the simulations have been computed on the same empirical time period, hence the very good agreement for the median between empirical and simulated graphs.
In a true out-of-sample simulation, the agreement would not be necessarily of this quality.

## 10 Distribution for the returns and innovations

### 10.1 Random generators and non-central Student distribution

The last important part of the process that needs to be specified is the distribution for the innovations.
The standard choice is to use a multivariate normal pϵ=N​(𝟎,𝕀)p\_{\bm{\epsilon}}=N(\bm{0},\bm{\mathbb{I}}), leading to the distribution for the returns p𝒓=N​(𝝁,𝚺)p\_{\bm{r}}=N(\bm{\mu},\bm{\Sigma}), and this distribution decays exponentially fast.
As shown by several empirical studies, financial markets experience more brutal events compared to the exponential decay of the normal distribution.
This is remedied by using instead a Student distribution, which decays as a power law for large innovations.
For both normal and Student distributions, the multivariate extensions are well known and can be found in many textbooks, see for example [McNeil et al., [2015](https://arxiv.org/html/2511.18125v1#bib.bib7)].

In the univariate case, the empirical distributions from the returns can be directly obtained from the prices.
Removing the heteroskedasticity is interesting since leading to stationary time series, with better convergence properties for the cdf.
The innovations can be obtained by using Eq. [11](https://arxiv.org/html/2511.18125v1#S5.E11 "In 5 Definitions of historical return, volatility and innovation") at scale Δ​T\Delta T, computing the return and volatility on historical data, and finally computing the time series of realized innovations and their distributions.
A normal distribution clearly lacks heavy tails, while a Student distribution matches decently both empirical distributions, with a tail index of the order of 3 to 10 at the monthly scale.
Yet, the empirical distributions for the returns and innovations are asymmetric, with larger moves on the down side than on the upside, particularly for stock indexes but also for bond indexes.
A Student distribution is symmetric, therefore cannot reproduce this market asymmetry.

A non-central Student distribution provides for a simple solution, where the asymmetry is controlled by one new parameter γ\gamma, and with a simple algorithm to generate random draws.
The distribution and related random generator is presented for example in [McNeil et al., [2015](https://arxiv.org/html/2511.18125v1#bib.bib7)], or with slightly different specification in [Wikipedia, [2023](https://arxiv.org/html/2511.18125v1#bib.bib11)].
Remain to have a non-central Student random generator for the multivariate case.
Such an algorithm is given in [McNeil et al., [2015](https://arxiv.org/html/2511.18125v1#bib.bib7)] when presenting the “normal mean-variance mixture” algorithms, depending on the parameters 𝝁\bm{\mu}, 𝚺\bm{\Sigma}, and a vector 𝜸\bm{\gamma} specifying the asymmetry.
For 𝜸=0\bm{\gamma}=0, the multivariate non-central Student distribution reduces to the usual Student distribution.

Yet, the equations provided in [McNeil et al., [2015](https://arxiv.org/html/2511.18125v1#bib.bib7)] are mixing the parameters, in particular the mean and covariance of the generated vectors is not equal to 𝝁\bm{\mu} and 𝚺\bm{\Sigma}, respectively, but have contributions in 𝜸\bm{\gamma}.
As provided, this parameter’s mixing makes the algorithm difficult to use in an application.
Fortunately, the equations can be modified so that the means and the covariance matrix of the generated random vectors are given by the corresponding parameters.
This part is a bit technical, and is presented in Appendix [B](https://arxiv.org/html/2511.18125v1#A2 "Appendix B Non-Central Student-t: random draws and evaluation of 𝜃⁢(𝜈)").
The key result is that multi-variate random deviates ϵ\bm{\epsilon} can be generated with zero mean, unit variance, fat tails, and the asymmetry specified by 𝜸\bm{\gamma}.
Figure [7](https://arxiv.org/html/2511.18125v1#S10.F7 "Figure 7 ‣ 10.1 Random generators and non-central Student distribution ‣ 10 Distribution for the returns and innovations") shows the main distributions in the univariate case, namely normal, Student and non-central Student for increasing non-centrality parameter.

![Refer to caption](x31.png)


Figure 7: The folded-cdf f-cdf(ϵ\epsilon) for different distributions for the innovation ϵ\epsilon in the univariate case.
All Student have 8 degree of freedoms

The vector of random returns 𝒓\bm{r} is obtained with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒓\displaystyle\bm{r} | =𝝁+𝑨⋅ϵ\displaystyle=\bm{\mu}+\bm{A}\cdot\bm{\epsilon} |  | (21) |

where 𝑨\bm{A} is a square root of 𝚺\bm{\Sigma}.
Using the expectation and variance of ϵ\bm{\epsilon}, simple computations leads to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | E​[𝒓]\displaystyle E\!\left[\bm{r}\right] | =𝝁\displaystyle=\bm{\mu} |  | (22a) |
|  | var⁡[𝒓]\displaystyle\operatorname{var}\left[\bm{r}\right] | =𝚺.\displaystyle=\bm{\Sigma}. |  | (22b) |

The parameters values for 𝜸\bm{\gamma} have been adjusted on empirical data.
A cross-sectional study shows that it is sufficient to have one value per broad sector, like stock indexes or fixed incomes indexes.
These studies show that the asymmetry is always on the negative side (larger down moves than up moves), and with a slightly larger asymmetry for stock indexes than for fixed income indexes.

### 10.2 Empirical validation: innovation distributions

![Refer to caption](x32.png)

![Refer to caption](x33.png)

(a) Historical time series: ’Developed World Equity’ (left),
’U.S. Aggregate Bonds’ (right).

![Refer to caption](x34.png)

![Refer to caption](x35.png)

(b) Simulated time series: constant drift; constant covariance; normal innovations.

![Refer to caption](x36.png)

![Refer to caption](x37.png)

(c) Simulated time series: constant drift; LMARCH; NC-Student innovations.

![Refer to caption](x38.png)

![Refer to caption](x39.png)

(d) Simulated time series: drift with NRC and DU; LMARCH; NC-Student innovations.

Figure 8: The folded-cdf f-cdf(ϵ​(Δ​T)\epsilon(\Delta T)) for the innovations ϵ​(Δ​T)\epsilon(\Delta T) at increasing time horizon Δ​T\Delta T.

The empirical and simulated distributions of the innovations for the standard visualization set is shown in Fig. [8](https://arxiv.org/html/2511.18125v1#S10.F8 "Figure 8 ‣ 10.2 Empirical validation: innovation distributions ‣ 10 Distribution for the returns and innovations").
All the figures are generated from whole price paths, historical market prices (line a) or simulated Monte Carlo prices (line b, c, d), on which the formula [11](https://arxiv.org/html/2511.18125v1#S5.E11 "In 5 Definitions of historical return, volatility and innovation") is used to compute the innovations ϵ​(Δ​T)\epsilon(\Delta T) at scale Δ​T\Delta T.
On the empirical graphs (line a), the deep tails asymmetry is clearly visible, and is due to strong down moves (crashes) occurring after a period of low volatility (e.g. Covid crisis, Ukraine war).
The asymmetry is particularly strong at the scales of 2 to 6 months, with quite large negative innovations.
Such large persistent asymmetry cannot be reproduced with the current process. A term braking the r→−rr\rightarrow-r symmetry should be introduced, like a leverage effect term in the volatility (the volatility becomes larger following a price drop).
Introducing such a term in a multivariate context will complicate significantly the model, and we decided not to pursue this venue.

### 10.3 Empirical validation: return distributions

![Refer to caption](x40.png)

![Refer to caption](x41.png)

(a) Historical time series: ’Developed World Equity’ (left),
’U.S. Aggregate Bonds’ (right).

![Refer to caption](x42.png)

![Refer to caption](x43.png)

(b) Simulated time series: constant drift; constant covariance; normal innovations.

![Refer to caption](x44.png)

![Refer to caption](x45.png)

(c) Simulated time series: constant drift; LMARCH; NC-Student innovations.

![Refer to caption](x46.png)

![Refer to caption](x47.png)

(d) Simulated time series: drift with NRC and DU; LMARCH; NC-Student innovations.

Figure 9: The folded-cdf f-cdf(r​(Δ​T)r(\Delta T)) for the annualized return r​(Δ​T)r(\Delta T) at increasing time horizon Δ​T\Delta T.

The same plot but for the returns r​(Δ​T)r(\Delta T) is shown in Fig. [9](https://arxiv.org/html/2511.18125v1#S10.F9 "Figure 9 ‣ 10.3 Empirical validation: return distributions ‣ 10 Distribution for the returns and innovations").
For this figure, the returns are computed with a logarithmic return formula r​(t,Δ​T)=log⁡(p​(t)/p​(t−Δ​T))r(t,\Delta T)=\log(p(t)/p(t-\Delta T)), because both prices play a symmetric role, leading to more symmetric distributions.
The returns at scale Δ​T\Delta T are annualized with a factor 1​y/Δ​T\sqrt{1y/\Delta T}, resulting in comparable distribution shapes.
The location parameter (mean or median) should be annualized with a factor 1​y/Δ​T1y/\Delta T, hence a remaining scaling factor 1​y/Δ​T\sqrt{1y/\Delta T} for the median on these distributions.
This simple scaling difference explains the shift to higher values for the median at increasing Δ​T\Delta T (i.e. the point at cdf = 1/2).
Overall, this figure shows the important similarity in the shape of the distributions when increasing Δ​T\Delta T.
The black line is the cdf for a normal distribution with the same location and size as the 1 month returns.
The asymmetry and fat-tails of the distributions are clearly visible.
Interestingly, the distributions at 3 and 6 months show even larger tail and asymmetry, a feature observed in most empirical time series.

The corresponding figures for Monte Carlo simulations are displayed on the following lines, with an overall fair agreement with the empirical distributions.
For these processes, the aggregation necessarily reduces the tails and asymmetry, and more sophisticated processes are required to model the respective increases at a few months scale.
The agreement for the width of the distribution at 1 month results from using the CMA computed on historical data, hence is not surprising.
The interesting feature is the reducing width when increasing Δ​T\Delta T, which is similar for the empirical and simulated time series.
This shows that the LMARCH process captures correctly the time aggregation of the returns.

## 11 Processes comparison

The main new features of the processes are the ARCH volatility, together with the NRC and DU terms that modify the link between the standard deviation of the simulated values from the volatility in the time direction.
Another notable feature is the dependency from the past at the simulation start introduced by the LMARCH volatility and the NRC term.
Different processes are compared in the following subsections, using Monte Carlo simulations with 50,000 paths, and a simulation length of 20 years with monthly steps.

The start date is May 31, 2020, namely when the Covid crisis was in full swing.
At this date, the market was lower and with a high volatility, but already recovering from the sharp plunge in February.
This particular date was selected in order to show clearly the impact of the initial conditions, corresponding to a major crisis.
Outside of this particular period, the market is more “typical”, with less dependency on the initial conditions.

Five processes have been selected for the comparison, with combinations of the followings.
The base drift is constant, and a NRC and/or DU terms can be added.
The volatility can be constant or with a LMARCH covariance.
The innovations can be normal, or an asymmetric Student.
The parameters for the various components are chosen so as to match overall the corresponding statistical properties, as described in the previous sections.
For the DU term, the calibration time span Δ​Tcal\Delta T\_{\text{cal}} in Eq. [14](https://arxiv.org/html/2511.18125v1#S8.E14 "In 8.2 Drift Uncertainty (DU) ‣ 8 The drift") is taken as 25 years.
Five combinations of the above have been selected in order to show the salient features introduced by each term.
The base reference process is the combination (constant drift, constant volatility, normal innovations), corresponding to the usual (multiplicative) normal random walk.

One asset is used for the simulation, with the CMA corresponding to the developed world equity.
Because only one asset is present, there is no rebalancing or strategy.
Notice that realistic simulations involve a portfolio together with a strategy (periodic rebalancing, cash-in or cash-out).
In this setting, the strategy can have a further impact on the wealth, depending on the process used for the simulations.
For example, a cash-out during a crisis will have a large impact, and a LMARCH volatility or an asymmetric Student innovation can create larger price moves.
For this reason, a realistic process must be used in actual simulations, but a study of portfolios and strategies is beyond the present scope.

### 11.1 Drift for the wealth

![Refer to caption](x48.png)


Figure 10: The mean drift for different processes, as function of the simulation length.

The Fig. [10](https://arxiv.org/html/2511.18125v1#S11.F10 "Figure 10 ‣ 11.1 Drift for the wealth ‣ 11 Processes comparison") shows the simulated expected drift for the selected processes.
The mean wealth value after the simulation time Δ​T\Delta T is annualized, so as to remove the leading Δ​T\Delta T scaling.
The processes with constant covariance and the LMARCH volatility have a constant drift, as set by the CMA value for μ\mu.
Adding a DU term does not change the mean drift.

The impact of the NRC term is seen on the last 2 processes (in red and blue, with the red data below the blue ones).
Due to the short term trend following included in the NRC term, the initial NRC contribution is negative and decrease the drift as set by the CMA.
At the scale of a few years, the mean reversion dominates and increases the drift.
Then, after a few simulation years, the long term drift is set by the CMA values because the transient effects induced by the initial market conditions subside.
Adding the DU term has no effect on the mean drift, in agreement with the simple model used in Appendix [A](https://arxiv.org/html/2511.18125v1#A1 "Appendix A A simple model with drift uncertainty").

### 11.2 Standard deviation for the wealth

![Refer to caption](x49.png)


Figure 11: The standard deviation for different processes, as function of the simulation length.

The graph [11](https://arxiv.org/html/2511.18125v1#S11.F11 "Figure 11 ‣ 11.2 Standard deviation for the wealth ‣ 11 Processes comparison") shows the standard deviation of the simulated wealth (vertical axis) as function of the simulation length Δ​T\Delta T (horizontal axis).
The standard deviation has been annualized, so that the leading Δ​T\sqrt{\Delta T} scaling is removed.
The base line process with constant drift, constant volatility and normal innovation has no dependency from the past, hence the constant standard deviation, at the level sets by the CMA.
The same process but with a DU term on the drift shows clearly the linear increase of the standard deviation with the simulation length.
This larger uncertainty on the wealth is due to the uncertainty on the CMA drift, as captured by the DU term.

The LMARCH process starts with a higher value due to the crisis, and subside to the long term value as set by the CMA values.
Because the ARCH process has a long memory, the cross-over takes a few years.
Adding a NRC in the drift increase the standard deviation at short term at this starting date, due to the large value for the NRC term.
As expected, the NRC term decreases the long term standard deviation, with the difference controlled by the magnitude in the NRC term.
Intuitively, a large long term deviation from the expected drift is likely to induce a correction, hence a smaller standard deviation.
Finally, adding the NRC and DU terms increase the standard deviation linearly, as derived with a simple model in Appendix [A](https://arxiv.org/html/2511.18125v1#A1 "Appendix A A simple model with drift uncertainty").
But the increase is tamed by the NRC term, which creates a pull back effect for large DU random drift.

### 11.3 VaR at a 5% level

![Refer to caption](x50.png)


Figure 12: The 5% relative VaR for different processes, as function of the simulation length Δ​T\Delta T.

The 5% quantiles of the terminal wealth after Δ​T\Delta T, equivalent to a VaR at 95% for the losses, measure the level of wealth that is not reached in 5% of the case.
This is a common measure of risk in portfolio management, and is reported in Fig. [12](https://arxiv.org/html/2511.18125v1#S11.F12 "Figure 12 ‣ 11.3 VaR at a 5% level ‣ 11 Processes comparison") as function of the simulation time Δ​T\Delta T.
On this figure, a higher level means less risk, since larger values for the wealth are obtained with a 95% probability.

Overall, the quantiles decrease during the first years, meaning more risk.
This is due to the diffusion, that dominates the drift for small Δ​T\Delta T, as explained in Sec. [3](https://arxiv.org/html/2511.18125v1#S3 "3 The core scaling of drift and volatility").
The details of the process matter for the 5% VaR, and the LMARCH volatility is higher due to the Covid crisis, leading to a larger risk up to a few years.
For large Δ​T\Delta T, the drift dominates, leading to the steady increases of the quantiles, therefore a diminishing risk.
In between, a cross-over takes place at the scale of a few years, in this case between 3 to 7 years.
The CMA value used for this asset are μ\mu = 8.9% and σ\sigma = 16.6%, leading to a cross-over time Δ​T×≃{\Delta T\_{\!\times}}\simeq 3.5 year.
This figure gives a clear illustration of the impact of the random walk scaling (Δ​T\Delta T for the drift versus Δ​T\sqrt{\Delta T} for the volatility) and the induced cross-over.
Notice also the fairly long time needed to have the 5% VaR at the initial value of the portfolio (depending on the process, between 8 to 20 years).

The NRC and DU terms alter the drift, hence the different long term behaviors.
As can be expected, the LMARCH volatility and DU term increase the risk, while the NRC term reduces the risk.

### 11.4 Lower tail risks

![Refer to caption](x51.png)


Figure 13: The VaR ratio VaR(0.01)/VaR(0.05) for different processes, as function of the simulation length Δ​T\Delta T.

The more extreme risks in the lower tail can be measured by VaR, say at the 1% level.
An interesting measure is the ratio VaR(0.01)/VaR(0.05) which quantify “how fat is the tail”.
A low value means that VaR(0.01) is low compared to VaR(0.05), namely larger extreme risks.
The figure [13](https://arxiv.org/html/2511.18125v1#S11.F13 "Figure 13 ‣ 11.4 Lower tail risks ‣ 11 Processes comparison") shows this VaR ratio, low values mean larger tails, or more extreme risks.
The overall decreasing values with Δ​T\Delta T mean larger tails for increasing investment horizons.
Then, a LMARCH volatility and a DU term both increase the extreme risks, due to the increased probability of lower wealth.
In the other direction, the usual random walk process has the smallest tail.
This is likely underestimating the extreme risk, since all modifications of this process produce heavier tails.

## 12 Conclusions

Multivariate long term models for the market evolution are required for a variety of long term financial plannings, like for pension funds, social insurances, or in wealth management.
The simplest model is a multivariate normal process, but the stylized facts accumulated over the last 40 years point toward more complex models.
A critical issue is the validation of such models, since the long time horizons preclude using a large enough effective sample in order to evaluate significant statistics.
The validation step is why the construction of models beyond the usual normal process has been largely ignored in the academic literature.
Yet, such models are used anyway in the industry, because plannings and validations need to be done in order to check the adequacy of an investment strategy toward the desired long term goals.
Hence, it is better to construct a model incorporating today’s knowledge, even though a validation cannot be done with all the desired rigor.
The present contribution is a step in this direction, trying at best to extract long term empirical information from market data in order to validate a process.
Clearly, the exercise is fundamentally limited, yet the present contribution is an honest attempt to improve over a simple normal random walk commonly used today.

Backed by several empirical statistics aimed to extract at best statistical information at long time scales from the financial markets, several additions are made to the core normal random walk with respect to the drifts, covariance matrix and the distribution for the innovations.
Compared to the basic normal random walk, the salient outcome of using the proposed process is the increased risk.
Most components push in this direction: the drift uncertainty, the dynamic volatility, and the skewed and fat-tailed innovations.
Only the NRC term provides for a stabilization.
Another difference is the dependencies on the recent market states introduced by the NRC and the dynamic covariance, making for a different mean and risk over a few years.
Given this picture, it is possible that many long term investment plans, say pension funds, underestimate their tail risks.

## Acknowledgments

The author is indebted to Alexandra Tchalakian for many discussions and for important contributions in the implementation of the present model and statistics.

This work was part of a larger project made with the bank J.P.Morgan, and this paper benefited from the many comments made by the project participants.

## Appendix A A simple model with drift uncertainty

Let us assume that the forecast for the drift μ\mu is a random variable with distribution

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(μ)=N​(μ¯,σμ2)p(\mu)=N(\overline{\mu},\sigma\_{\mu}^{2}) |  | (A.1) |

where μ¯\overline{\mu} is the value provided by the CMA.
The uncertainty over this value is controlled by σμ\sigma\_{\mu}.

The simplest model for the logarithmic return rr is a normal distribution

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(r|μ)=N​(Δ​T​μ,Δ​T​σr2)p(r|\mu)=N(\Delta T\,\mu,\Delta T\,\sigma\_{r}^{2}) |  | (A.2) |

where Δ​T\Delta T is the desired time interval up to the terminal value.
We want to evaluate the terminal return distribution, taking into account the uncertainty on the drift

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(r)=∫𝑑μ​p​(r|μ)​p​(μ).p(r)=\int d\mu\,p(r|\mu)\,p(\mu). |  | (A.3) |

Because both distributions are normal, the computation can be done analytically, and p​(r)p(r) is a normal distribution with annualized variance Δ​T​σeff,r2\Delta T\,\sigma\_{\text{eff},r}^{2}.
The result at leading order for the annualized standard deviation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | σeff,r≃σr​(1+12​Δ​T​(σμσr)2).\sigma\_{\text{eff},r}\simeq\sigma\_{r}\left(1+\frac{1}{2}\,\Delta T\,\left(\frac{\sigma\_{\mu}}{\sigma\_{r}}\right)^{2}\right). |  | (A.4) |

Due to the linear scaling of the drift, the correction term for the standard deviation is also linear in Δ​T\Delta T.
Let us emphasize that the volatility at time horizon Δ​T\Delta T is Δ​T​σeff,r\sqrt{\Delta T}\sigma\_{\text{eff},r} hence the short term leading scaling is in Δ​T1/2\Delta T^{1/2} but the long term correction grows as Δ​T3/2\Delta T^{3/2}.

In order to see if the correction is quantitatively important, a model for the uncertainty on μ\mu should be established, essentially relating σμ\sigma\_{\mu} to the other quantities.
Let us assume that the model is calibrated using historical data available over a time span Δ​Tcal\Delta T\_{\text{cal}} (and assuming that distributions are stationary).
The realized return is one draw from the distribution N​(Δ​Tcal​μ¯,Δ​Tcal​σr2)N(\Delta T\_{\text{cal}}\overline{\mu},\Delta T\_{\text{cal}}\sigma\_{r}^{2}), i.e.

|  |  |  |
| --- | --- | --- |
|  | r=Δ​Tcal​μ¯+Δ​Tcal​σr​ϵi,r=\Delta T\_{\text{cal}}\,\overline{\mu}+\sqrt{\Delta T\_{\text{cal}}}\,\sigma\_{r}\,\epsilon\_{i}, |  |

with ϵi∼N​(0,1)\epsilon\_{i}\sim N(0,1).
The historical estimation for the annualized drift is μ^=r/Δ​Tcal\hat{\mu}=r/\Delta T\_{\text{cal}}, or

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^=μ¯+σrΔ​Tcal​ϵi.\hat{\mu}=\overline{\mu}+\frac{\sigma\_{r}}{\sqrt{\Delta T\_{\text{cal}}}}\,\epsilon\_{i}. |  | (A.5) |

Therefore, the uncertainty on the estimated value is

|  |  |  |  |
| --- | --- | --- | --- |
|  | σμ=σrΔ​Tcal.\sigma\_{\mu}=\frac{\sigma\_{r}}{\sqrt{\Delta T\_{\text{cal}}}}. |  | (A.6) |

Inserting this relation in ([A.4](https://arxiv.org/html/2511.18125v1#A1.E4 "In Appendix A A simple model with drift uncertainty")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | σeff,r≃σr​(1+12​Δ​TΔ​Tcal).\sigma\_{\text{eff},r}\simeq\sigma\_{r}\left(1+\frac{1}{2}\,\frac{\Delta T}{\Delta T\_{\text{cal}}}\right). |  | (A.7) |

Typically, a few decades of historical data are available, say 20 to 40 years.
Taking say 25 years of historical data for the calibration leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | σμ≈15​σr,\sigma\_{\mu}\approx\frac{1}{5}\,\sigma\_{r}, |  | (A.8) |

which is a pretty small uncertainty.
With a target simulation time of a few decades, say 20 to 30 years, the correction term is not negligible but also not dominant.
In the range of Δ​T\Delta T amenable for statistics, essentially up to 1 year, the correction is small.

## Appendix B Non-Central Student-t: random draws and evaluation of θ​(ν)\theta(\nu)

The algorithm presented in [McNeil et al., [2015](https://arxiv.org/html/2511.18125v1#bib.bib7)] is modified as follow.
A random variable ww is introduced, with ν/w∼χ2​(ν)\nu/w\sim\chi^{2}(\nu) and ν\nu the degrees of freedom.
A convenient function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ​(ν)=var⁡[w]E​[w]=1−(E​[w])2E​[w]\theta(\nu)=\frac{\operatorname{var}\left[\sqrt{w}\right]}{E\!\left[w\right]}=1-\frac{(E\!\left[\sqrt{w}\right])^{2}}{E\!\left[w\right]} |  | (B.1) |

which measure in relative term the variance of the mixing variable w\sqrt{w}.
The non-centrality parameter is 𝜸\bm{\gamma}, and a matrix 𝝌\bm{\chi} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝌=𝕀+θ​𝜸⋅𝜸′\displaystyle\bm{\chi}=\mathbb{I}+\theta\,\bm{\gamma}\cdot\bm{\gamma}^{\prime} |  | (B.2) |

The matrix 𝝌\bm{\chi} is symmetric and positive definite, hence all its eigenvalues are real and positive.
Consequently, the inverse square root of the matrix 𝝌\bm{\chi} is well defined, and can be evaluated from the eigenvalues and eigenvectors.
Finally, because the inverse and the square root are well defined, the relation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝌−1/2⋅𝝌⋅𝝌−1/2=𝕀\displaystyle\bm{\chi}^{-1/2}\cdot\bm{\chi}\cdot\bm{\chi}^{-1/2}=\mathbb{I} |  | (B.3) |

holds.

The multivariate non-central Student random generator for the variable ϵ\bm{\epsilon} is defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ϵ\displaystyle\bm{\epsilon} | =𝝌−1/2​{w−E​[w]E​[w]⋅𝜸+wE​[w]​𝒁}\displaystyle=\bm{\chi}^{-1/2}\left\{\frac{\sqrt{w}-E\!\left[\sqrt{w}\right]}{\sqrt{E\!\left[w\right]}}\cdot\bm{\gamma}+\frac{\sqrt{w}}{\sqrt{E\!\left[w\right]}}\bm{Z}\right\} |  | (B.4) |

where 𝒁\bm{Z} is a vector of independent normal variable with zα∼N​(0,1)z\_{\alpha}\sim N(0,1), and ϵ\bm{\epsilon} is a random vector of innovations.
The explicit expressions for E​[w]E\!\left[\sqrt{w}\right] and E​[w]E\!\left[w\right] are given below in Eq. [B.7](https://arxiv.org/html/2511.18125v1#A2.E7 "In Appendix B Non-Central Student-t: random draws and evaluation of 𝜃⁢(𝜈)").
Notice that with the definitions [B.4](https://arxiv.org/html/2511.18125v1#A2.E4 "In Appendix B Non-Central Student-t: random draws and evaluation of 𝜃⁢(𝜈)"), both fractions depending on ww are independent of the scale selected for ww, namely the same random variables ϵ\bm{\epsilon} are obtained when using α/w∼χ2​(ν)\alpha/w\sim\chi^{2}(\nu) regardless of 0<α<∞0<\alpha<\infty.
The usual convention is to take α=ν\alpha=\nu.
With this specifications, the vector of random innovations ϵ\bm{\epsilon} has a non-central Student distribution with E​[ϵ]=0E\!\left[\bm{\epsilon}\right]=0 and var⁡[ϵ]=𝕀\operatorname{var}\left[\bm{\epsilon}\right]=\mathbb{I} (where the relation [B.3](https://arxiv.org/html/2511.18125v1#A2.E3 "In Appendix B Non-Central Student-t: random draws and evaluation of 𝜃⁢(𝜈)") is used in the derivation).
The non-central Student random number generation involves the expectations for w\sqrt{w} and ww, where ν/w\nu/w is distributed according to a chi-square distribution.
In the scalar case, and for a slightly different specification, these expectations are available in wikipedia [Wikipedia, [2023](https://arxiv.org/html/2511.18125v1#bib.bib11)].
By identification, the desired expectations are obtained.
The wikipedia specification for the scalar random variate xx is

|  |  |  |  |
| --- | --- | --- | --- |
|  | x=μ+w​γ+w​z.x=\mu+\sqrt{w}\,\gamma+\sqrt{w}\,z. |  | (B.5) |

For these specifications, the following expression are obtained for the mean and variance

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | E​[x]\displaystyle E\!\left[x\right] | =μ+E​[w]​γ,\displaystyle=\mu+E\!\left[\sqrt{w}\right]\,\gamma, |  | (B.6a) |
|  | var⁡[x]\displaystyle\operatorname{var}\left[x\right] | =E​[w]⋅1+var⁡[w]​γ2.\displaystyle=E\!\left[w\right]\cdot 1+\operatorname{var}\left[\sqrt{w}\right]\gamma^{2}. |  | (B.6b) |

Comparing with the explicit expressions given in wikipedia, the desired expectations are obtained

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | E​[w]\displaystyle E\!\left[\sqrt{w}\right] | ≅(1−34​ν−1)−1,\displaystyle\cong\left(1-\frac{3}{4\nu-1}\right)^{-1}, |  | (B.7a) |
|  | E​[w]\displaystyle E\!\left[w\right] | =νν−2.\displaystyle=\frac{\nu}{\nu-2}. |  | (B.7b) |

From both expressions, the value of θ=θ​(ν)\theta=\theta(\nu) is obtained.
An asymptotic expansion in 1/ν1/\nu leads to θ≃1/(2​ν)\theta\simeq 1/(2\nu), while a very good approximation in the domain of interest is θ≃1/(2​(ν−1.7))\theta\simeq 1/(2\,(\nu-1.7)).
The value of θ\theta and the approximation are shown in figure [14](https://arxiv.org/html/2511.18125v1#A2.F14 "Figure 14 ‣ Appendix B Non-Central Student-t: random draws and evaluation of 𝜃⁢(𝜈)").

![Refer to caption](x52.png)


Figure 14: The function θ\theta and its approximation versus ν\nu.

Essentially, in the region of interest with ν≃6\nu\simeq 6 to 10, θ​(ν)\theta(\nu) is small with θ≃\theta\simeq 0.12 to 0.05.

## Appendix C Long term expectations

This section focuses on the long term expectations of the process, in particular for the drift and covariance matrix.
For this section, the multivariate process includes a constant drift (i.e. no NRC and DU term), a LMARCH volatility, and non-central Student innovations.
The stationary values are assumed to exist, namely for a sufficiently large time tt, the values E​[𝒓​(t)]E\!\left[\bm{r}(t)\right] and E​[𝒓​(t)⋅𝒓​(t)′]E\!\left[\bm{r}(t)\cdot\bm{r}(t)^{\prime}\right] converge to a given vector and matrix, respectively, that are independent of the time tt and of the initial conditions.
The expectations E​[⋅]E\!\left[\cdot\right] are taken with respect to the random realization of the innovations distributed according to a non-central student distribution.

For the mean, equation [21](https://arxiv.org/html/2511.18125v1#S10.E21 "In 10.1 Random generators and non-central Student distribution ‣ 10 Distribution for the returns and innovations") together with E​[ϵ]=0E\!\left[\bm{\epsilon}\right]=0 gives the desired result, namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[𝒓​(𝒕)]=𝝁∀t.E\!\left[\bm{r(t)}\right]=\bm{\mu}\hskip 20.00003pt\forall t. |  | (C.8) |

This result is stronger than needed since valid for all times.

The covariance 𝚺​(t)\bm{\Sigma}(t) is defined in Eq. [19](https://arxiv.org/html/2511.18125v1#S9.E19 "In 9.3 LMARCH Covariance ‣ 9 The covariance") and [20](https://arxiv.org/html/2511.18125v1#S9.E20 "In 9.3 LMARCH Covariance ‣ 9 The covariance"), repeated here

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
|  | 𝚺LM-ARCH, linear​(t)=∑0≤k<kmaxw​(k,δ​t)​(𝒓​(t−k​δ​t)−𝝁)⋅(𝒓​(t−k​δ​t)−𝝁)′\displaystyle\bm{\Sigma}\_{\text{LM-ARCH, linear}}(t)=\sum\_{0\leq k<k\_{\text{max}}}w(k,\delta t)~\left(\bm{r}(t-k\,\delta t)-\bm{\mu}\right)\cdot\left(\bm{r}(t-k\,\delta t)-\bm{\mu}\right)^{\prime} |  | (C.9a) |
|  | 𝚺​(t)=w∞⋅𝚺CMA+(1−w∞)⋅𝚺LM-ARCH, linear​(t).\displaystyle\bm{\Sigma}(t)=w\_{\infty}\cdot\bm{\Sigma}\_{\text{{\scriptsize CMA}}}+(1-w\_{\infty})\cdot\bm{\Sigma}\_{\text{LM-ARCH, linear}}(t). |  | (C.9b) |

and where the time scale δ​t\delta t is implicit in 𝒓\bm{r} and 𝚺LM-ARCH, linear\bm{\Sigma}\_{\text{LM-ARCH, linear}}.
For times tt larger than the memory of the LM-ARCH process, namely t≫t0+kmax​δ​tt\gg t\_{0}+k\_{\text{max}}\,\delta t where t0t\_{0} is the start time of the simulations, all the vectors 𝒓\bm{r} used to compute 𝚺LM-ARCH, linear\bm{\Sigma}\_{\text{LM-ARCH, linear}} are random and drawn from a non-central Student distribution with covariance 𝚺​(t)\bm{\Sigma}(t).
Assuming a fixed value 𝚺¯\overline{\bm{\Sigma}} for the expectation of 𝚺​(t)\bm{\Sigma}(t) for large enough tt, the linear covariance is

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[ΣLM-ARCH, linear​(t)]\displaystyle E\!\left[\Sigma\_{\text{LM-ARCH, linear}}(t)\right] | =∑0≤k<kmaxw​(k,δ​t)​E​[𝚺​(t−k​δ​t)]\displaystyle=\sum\_{0\leq k<k\_{\text{max}}}w(k,\delta t)\,E\!\left[\bm{\Sigma}(t-k\,\delta t)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑0≤k<kmaxw​(k,δ​t)​𝚺¯\displaystyle=\sum\_{0\leq k<k\_{\text{max}}}w(k,\delta t)\,\overline{\bm{\Sigma}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝚺¯\displaystyle=\overline{\bm{\Sigma}} |  | (C.10) |

where the normalization property ∑kw​(k,δ​t)=1\sum\_{k}w(k,\delta t)=1 of the LM-ARCH weights has been used.
Taking the expectation of [C.9b](https://arxiv.org/html/2511.18125v1#A3.E9.2 "In C.9 ‣ Appendix C Long term expectations") leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺¯=w∞⋅𝚺CMA+(1−w∞)⋅𝚺¯\overline{\bm{\Sigma}}=w\_{\infty}\cdot\bm{\Sigma}\_{\text{{\scriptsize CMA}}}+(1-w\_{\infty})\cdot\overline{\bm{\Sigma}} |  | (C.11) |

with solution

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺¯=𝚺CMA\overline{\bm{\Sigma}}=\bm{\Sigma}\_{\text{{\scriptsize CMA}}} |  | (C.12) |

for w∞>0w\_{\infty}>0.
This shows that for a (non-central) student distribution, the long term expectation of the covariance is the CMA covariance matrix, regardless of the distribution for ϵ\bm{\epsilon} as parametrized by ν\nu and 𝜸\bm{\gamma}.

## References

* Bachelier [1900]

  Louis Bachelier.
  Théorie de la spéculation.
  *Ann. de l’Ecole Norm. Sup.*, 3(17):21–86,
  1900.
* Bauwens et al. [2006]

  L. Bauwens, S. Laurent, and J.K.V. Rombouts.
  Multivariate GARCH models: a survey.
  *Journal of Applied Econometrics*, 21:79–109, 2006.
    
  URL <https://onlinelibrary.wiley.com/doi/pdf/10.1002/jae.842>.
* Bollerslev [1986]

  Tim Bollerslev.
  Generalized autoregressive conditional heteroskedasticity.
  *Journal of Econometrics*, 31:307–327, 1 1986.
* Corradi [2000]

  Valentina Corradi.
  Reconsidering the continuous time limit of the GARCH(1,1)
  process.
  *Journal of Econometrics*, 96:145–153, 2000.
* Engle [1982]

  R. F. Engle.
  Autoregressive Conditional Heteroskedasticity with Estimates of the
  Variance of U. K. Inflation.
  *Econometrica*, 50:987–1008, January 1982.
* Engle and Kroner [1995]

  R. F. Engle and K. F. Kroner.
  Multivariate simulataneous generalized ARCH.
  *Economic Theory*, 11:122–150, 1995.
* McNeil et al. [2015]

  Alexander McNeil, Rüdiger Frey, and Paul Embrechts.
  *Quantitative Risk Management*.
  Princeton University Press, 2015.
  ISBN 9780691166278.
* Nelson [1990]

  D.B. Nelson.
  Stationarity and Persistence in the GARCH(1,1) model.
  *Econometric Theory*, 6:318–34, 1990.
* Ortec Finance [2021]

  Ortec Finance.
  The uncertainty of long-term capital market assumptions, 2021.
    
  URL <www.ortecfinance.com/en/insights#mediatype=Research>.
* van der Schans and Boer [2014]

  Martin van der Schans and Alex Boer.
  A heuristic for completing covariance and correlation matrices, 2014.
  URL <www.ortecfinance.com/en/insights#mediatype=Research>.
* Wikipedia [2023]

  Wikipedia.
  Noncentral t-distribution, 2023.
    
  URL <en.wikipedia.org/wiki/Noncentralt-distribution>.
* Zumbach [2004]

  Gilles Zumbach.
  Volatility processes and volatility forecast with long memory.
  *Quantitative Finance*, 4:70–86, 2004.
* Zumbach [2006]

  Gilles Zumbach.
  The RiskMetrics 2006 methodology.
  Technical report, RiskMetrics Group, 2006.
  available at www.ssrn.com.
* Zumbach [2011]

  Gilles Zumbach.
  The empirical properties of large covariance matrices.
  *Quantitative Finance*, 11:1091–1102, 2011.
* Zumbach [2012]

  Gilles Zumbach.
  *Discrete Time Series, Processes, and Applications in Finance*.
  Springer, 2012.