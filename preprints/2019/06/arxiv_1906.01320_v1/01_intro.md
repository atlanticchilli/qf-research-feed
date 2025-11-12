---
authors:
- Jin Sun
- Kevin Fergusson
- Eckhard Platen
- Pavel V. Shevchenko
doc_id: arxiv:1906.01320v1
family_id: arxiv:1906.01320
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[1906.01320] Fair Pricing of Variable Annuities with Guarantees under the
  Benchmark Approach'
url_abs: http://arxiv.org/abs/1906.01320v1
url_html: https://ar5iv.org/html/1906.01320v1
venue: arXiv q-fin
version: 1
year: 2019
---


Jin Sun
  
Kevin Fergusson\correfcorrauth
  
Eckhard Platen
  
Pavel V. Shevchenko

###### Abstract

In this paper we consider the pricing of variable annuities (VAs) with guaranteed minimum withdrawal benefits. We consider two pricing approaches, the classical risk-neutral approach and the benchmark approach, and we examine the associated static and optimal behaviors of both the investor and insurer. The first model considered is the so-called minimal market model, where pricing is achieved using the benchmark approach. The benchmark approach was introduced by Platen in 2001 and has received wide acceptance in the finance community. Under this approach, valuing an asset involves determining the minimum-valued replicating portfolio, with reference to the growth optimal portfolio under the real-world probability measure, and it both subsumes classical risk-neutral pricing as a particular case and extends it to situations where risk-neutral pricing is impossible.
The second model is the Black-Scholes model for the equity index, where the pricing of contracts is performed within the risk-neutral framework. Crucially, we demonstrate that when the insurer prices and reserves using the Black-Scholes model, while the insured employs a dynamic withdrawal strategy based on the minimal market model, the insurer may be underestimating the value and associated reserves of the contract.

JEL classification: C61, G22

Keywords:
variable annuity guarantee, stochastic optimal control, stochastic reserve, benchmark approach

{frontmatter}

\ead

jin.sun@uts.edu.au

\cortext

[corrauth]Corresponding author
\eadkevin.fergusson@unimelb.edu.au

\ead

eckhard.platen@uts.edu.au

\ead

pavel.shevchenko@mq.edu.au

\address

[utsm]Faculty of Science, University of Technology Sydney
\address[melbaddr]Centre for Actuarial Studies, Department of Economics, University of Melbourne, Victoria, Australia
\address[csiro]Data 61, CSIRO Docklands
\address[mqaddr1]Department of Actuarial Studies and Business Analytics, Macquarie University, Australia
\address[utsb]UTS Business School, University of Technology Sydney

## 1 Introduction

Variable annuities (VA) with guarantees of living and death benefits are offered by wealth management and insurance companies worldwide to assist individuals in managing their pre-retirement and post-retirement financial plans. These products take advantage of market growth while providing a protection of the savings against market downturns. The VA contract cash flows received by the policyholder are linked to the choice of investment portfolio (e.g. the choice of mutual fund and its strategy) and its performance while traditional annuities provide a pre-defined income stream in exchange for a lump sum payment.

A variety of VA guarantees can be added by policyholders at the cost of additional fees. Common examples of VA guarantees include guaranteed minimum accumulation benefit (GMAB), guaranteed minimum withdrawal benefit (GMWB), guaranteed minimum income benefit (GMIB) and guaranteed minimum death benefit (GMDB), as well as combinations of these, e.g., guaranteed minimum withdrawal and death benefit (GMWDB), among others. These guarantees, generically denoted as GMxB, provide different
types of protection against market downturns, shortfall of savings due to longevity risk or assurance of stability of income streams. Precise specifications of these products can vary across categories and issuers; see Bauer et al. ([2008](#bib.bib1)); Ledlie et al. ([2008](#bib.bib8)) and Kalberer and Ravindran ([2009](#bib.bib6)) for an overview of these products.

Since the recent financial crisis, the need for accurate estimation of hedging costs of VA guarantees has become increasingly important. Such estimation includes the pricing of future cash flows that must be paid by the insurer to the policyholder in order to fulfill the liabilities of the VA guarantees, as well as the associated hedging strategy to deliver the liability payments. The standard pricing approach follows the risk-neutral pricing theory, where under the condition of no-arbitrage, the VA product is priced as the expectation of the totality of discounted future cash flows offered by the product under the so-called equivalent risk-neutral pricing measure.
There have been a number of contributions in the academic literature considering numerical methods for the pricing of VA guarantees. These include standard and regression-based Monte Carlo, partial differential equation (PDE) and direct integration methods. A comprehensive overview of numerical methods for the pricing of VA guarantees is provided in Shevchenko and Luo ([2016](#bib.bib15)).

The benchmark approach (BA) offers an alternative pricing theory.
Under very general conditions, there exists in a given investment universe a unique growth-optimal portfolio (GP). The BA takes the GP as the numeraire, or benchmark, such that any benchmarked nonnegative portfolio price process assumes zero expected instantaneous returns. The GP assumes the highest expected instantaneous growth rate among all nonnegative portfolios in the investment universe, and maximizes the expected log-utility of the terminal wealth. It is a well-diversified portfolio that draws on all tradable risk factors and the corresponding risk premia to achieve the growth optimality. Following the real-world pricing formula under the BA, real-world pricing of any given future cash flows identifies their minimal possible replication cost. The BA is considered as a generalization of the risk-neutral pricing theory, in that an equivalent risk-neutral pricing measure need not exist, yet it includes risk-neutral pricing as a special case involving additional conditions that ensure the existence of an equivalent risk-neutral probability measure. Another special case is the minimal market model (MMM), described in [B](#A2 "Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach"), which permits mean-reversion of the GP around an exponentially growing market trend and which captures both the leptokurtic behavior of logreturns, as shown in Fergusson and Platen ([2006](#bib.bib5)), and the leverage effect, manifest as a spike in volatility in a rapidly falling market; see for example Campbell and Viceira ([2005](#bib.bib3)) and Shiller ([2015](#bib.bib16)). In contrast, the Black-Scholes model (BSM), also described in [B](#A2 "Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach"), captures only mesokurtic behavior of logreturns, and is unable to model the leverage effect because of its constant volatility.

In this paper we consider a standard VA product with GMWB, which provides a guaranteed withdrawal amount per year until the maturity of the contract, regardless of the investment performance. The total withdrawal amount is such that the initial investment is guaranteed to be returned over the life of the contract. Additional features, such as a death benefit, can be added straightforwardly if so desired, see, e.g., Luo and Shevchenko ([2015](#bib.bib9)).

Two classes of withdrawal strategies of the policyholder are often considered in the literature: a static withdrawal strategy under which the policyholder withdraws a predetermined amount on each withdrawal date; or a dynamic strategy where the policyholder “optimally” decides the amount of withdrawal at each withdrawal date depending on the information available at that date, where the optimality usually refers to the maximization of the value of the current and future cash flows. By assuming an optimal policyholder’s withdrawal behavior, the pricing of the VA product corresponds to the hedging cost of the worst case scenario faced by the VA provider. In other words, the price of the VA product under the respective dynamic strategy provides an upper bound of hedging cost from the VA provider’s perspective; see Sun et al. ([2018](#bib.bib17)). It should be noted that the actual policyholders’ withdrawal strategies could be far from optimal; see, e.g., Moenig and Bauer ([2015](#bib.bib10)).

Assuming that the policyholder takes the dynamic withdrawal strategy, that is, the optimal strategy that maximizes the present value of current and future cash flows of the VA product, the actual withdrawals still depend on the pricing method adopted by the policyholder. On the other hand, the VA provider, who maintains a hedging portfolio to deliver the liability cash flows of the VA product also faces the same choices for pricing and hedging for the portfolio. In this paper, we consider two pricing methods, the risk-neutral pricing approach and the BA. We investigate the outcomes and implications of different choices of withdrawal and hedging strategies by the policyholder and the VA provider. In particular, we study empirically the cases when the two parties take different pricing approaches.
In the VA pricing literature it is most often the case that the same pricing model is adopted by both the policyholder and the VA provider. The important situation where the policyholder and the VA provider hold fundamentally different valuation perspectives, as is described in this paper, has not been investigated. This paper attempts to fill this vacancy and hopefully initiate more interest in this direction.

The paper is organized as follows. In Section [2](#S2 "2 Description of the VA Guarantee Product ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") we present the contract details of the GMWB guarantee together with its pricing formulation under a stochastic optimal control framework.
Then, in Section [3](#S3 "3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") we empirically test these pricing and corresponding withdrawal and hedging strategies, respectively, for the policyholder and the VA provider, when the two parties use the same or different modeling approaches. Section [4](#S4 "4 Conclusions ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") concludes with remarks and discussion.
The appendices contain background technical aspects of our VA modeling and pricing approaches.
[A](#A1 "Appendix A A Brief Overview of the Benchmark Approach ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") provides an overview of the benchmark approach.
In [B](#A2 "Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") we describe the pricing models under the risk-neutral approach and the BA.
Finally, in [C](#A3 "Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") the VA pricing problem is formulated for optimal policyholder’s withdrawals under both pricing frameworks and models, and the numerical algorithm to solve the problem is described.

## 2 Description of the VA Guarantee Product

We consider the VA product where a policyholder invests at time t=0𝑡0t=0 a lump-sum of W​(0)𝑊0W(0) into a wealth account W​(t),t∈[0,T]

𝑊𝑡𝑡
0𝑇W(t),t\in[0,T] that tracks an equity index S​(t),t∈[0,T]

𝑆𝑡𝑡
0𝑇S(t),t\in[0,T], where t=T𝑡𝑇t=T corresponds to the expiry date of the VA contract. We assume both W​(t)𝑊𝑡W(t) and S​(t)𝑆𝑡S(t) are discounted by the locally risk-free savings account, as are all other values of wealth encountered hereafter. The (discounted) equity index evolves under the real-world probability measure ℙℙ{\mathbb{P}} according to the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S​(t)S​(t)=μ​(t)​d​t+σ​(t)​d​B​(t),t∈[0,T],formulae-sequence𝑑𝑆𝑡𝑆𝑡𝜇𝑡𝑑𝑡𝜎𝑡𝑑𝐵𝑡𝑡0𝑇\frac{dS(t)}{S(t)}=\mu(t)dt+\sigma(t)dB(t),\qquad t\in[0,T], |  | (1) |

where μ​(t)𝜇𝑡\mu(t) and σ​(t)𝜎𝑡\sigma(t) are the instantaneous market risk premium and volatility of the index, respectively. Here B​(t)𝐵𝑡B(t), t∈[0,T]𝑡0𝑇t\in[0,T], is a standard ℙℙ{\mathbb{P}}-Brownian motion driving traded market uncertainties.

As mentioned in [B](#A2 "Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach"), the diversified equity index approximates well the GP, and we have, as a particular case of ([1](#S2.E1 "In 2 Description of the VA Guarantee Product ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")),
the Black-Scholes model (BSM) of the GP, specified by the SDE ([19](#A2.E19 "In B.1 The Black-Scholes model ‣ Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")).
Also, as another particular case of ([1](#S2.E1 "In 2 Description of the VA Guarantee Product ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")), we have the minimal market model (MMM) of the GP, specified by the SDE ([23](#A2.E23 "In B.2 The minimal market model ‣ Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")).
Further details of both of these models are supplied in [B](#A2 "Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach").

The policyholder selects a GMWB rider in order to protect his wealth account W​(t)𝑊𝑡W(t), t∈[0,T]𝑡0𝑇t\in[0,T], over the lifetime of the VA contract.
The GMWB contract allows the policyholder to withdraw from a guarantee account A​(t)𝐴𝑡A(t), t∈[0,T]𝑡0𝑇t\in[0,T], on a sequence of pre-determined contract event dates, 0=t0<t1<⋯<tN=T0subscript𝑡0subscript𝑡1⋯subscript𝑡𝑁𝑇0=t\_{0}<t\_{1}<\dots<t\_{N}=T. The initial guarantee A​(0)𝐴0A(0) matches the initial wealth W​(0)𝑊0W(0). We assume here that the guarantee account stays constant over time, unless a withdrawal is made on one of the event dates, which reduces the guarantee account balance. Other forms of guaranteed returns can be modeled similarly.
For simplicity, we do not include in our discussion features such as death or early surrender benefits. Under a more realistic setting, these additional features can be included straightforwardly within the framework described in this paper.

To simplify notations, we denote by 𝑿​(t)𝑿𝑡\bm{X}(t) the vector of state variables at time t𝑡t, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑿​(t)=(μ​(t),σ​(t),S​(t),W​(t),A​(t)),t∈[0,T].formulae-sequence𝑿𝑡𝜇𝑡𝜎𝑡𝑆𝑡𝑊𝑡𝐴𝑡𝑡0𝑇\bm{X}(t)=(\mu(t),\sigma(t),S(t),W(t),A(t)),\quad t\in[0,T]. |  | (2) |

Here, we assume that the variable S​(t)𝑆𝑡S(t) follows a Markov process, so that 𝑿​(t)𝑿𝑡\bm{X}(t) contains all the market and account balance information available at t𝑡t. For simplicity, we assume that the state variable S​(t)𝑆𝑡S(t) is continuous, and W​(t)𝑊𝑡W(t) and A​(t)𝐴𝑡A(t) are left-continuous with right-hand limit (LCRL).

On event dates tn,n=1,…,Nformulae-sequence

subscript𝑡𝑛𝑛
1

…𝑁t\_{n},n=1,\dots,N, a nominal withdrawal γnsubscript𝛾𝑛\gamma\_{n} from the guarantee account is made. The policyholder may choose γn≤A​(tn)subscript𝛾𝑛𝐴subscript𝑡𝑛\gamma\_{n}\leq A(t\_{n}) on tn<Tsubscript𝑡𝑛𝑇t\_{n}<T. Otherwise, a liquidation withdrawal of max⁡(W​(tn),A​(tn))𝑊subscript𝑡𝑛𝐴subscript𝑡𝑛\max(W(t\_{n}),A(t\_{n})) is made. That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | γn={Γ​(tn,𝑿​(tn)),n<N,max⁡(W​(tn),A​(tn)),n=N,subscript𝛾𝑛casesΓsubscript𝑡𝑛𝑿subscript𝑡𝑛𝑛𝑁𝑊subscript𝑡𝑛𝐴subscript𝑡𝑛𝑛𝑁\gamma\_{n}=\begin{cases}\Gamma(t\_{n},\bm{X}(t\_{n})),&{n<N},\\ \max\left({W(t\_{n}),A(t\_{n})}\right),&{n=N},\end{cases} |  | (3) |

where Γ​(⋅,⋅)Γ⋅⋅\Gamma(\cdot,\cdot) is referred to as the *withdrawal strategy* of the policyholder.
The net cash flow received by the policyholder, which may differ from the gross amount, is denoted by Cn​(γn,𝑿​(tn))subscript𝐶𝑛subscript𝛾𝑛𝑿subscript𝑡𝑛C\_{n}(\gamma\_{n},\bm{X}(t\_{n})). In our case this cash flow is set to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cn​(γn,𝑿​(tn))={γn−β​max⁡(γn−Gn,0),n<N,max⁡(W​(T),A​(T))−β​max⁡(A​(T)−GN,0),n=N,subscript𝐶𝑛subscript𝛾𝑛𝑿subscript𝑡𝑛casessubscript𝛾𝑛𝛽subscript𝛾𝑛subscript𝐺𝑛0𝑛𝑁𝑊𝑇𝐴𝑇𝛽𝐴𝑇subscript𝐺𝑁0𝑛𝑁C\_{n}(\gamma\_{n},\bm{X}(t\_{n}))=\begin{cases}\gamma\_{n}-\beta\max(\gamma\_{n}-G\_{n},0),&n<N,\\ \max\left({W(T),A(T)}\right)-\beta\max(A(T)-G\_{N},0),&n=N,\end{cases} |  | (4) |

where Gnsubscript𝐺𝑛G\_{n} is a pre-determined withdrawal amount specified in the GMWB contract, and β𝛽\beta is the penalty rate applied to the part of the withdrawal from the guarantee account exceeding the contractual withdrawal Gnsubscript𝐺𝑛G\_{n}. Here we assume the penalty also applies to the last withdrawal of the guarantee account A​(T)𝐴𝑇A(T). The part of the wealth account balance in excess of the guarantee account balance is not subject to the penalty.
Upon withdrawal by the policyholder, the guarantee account is reduced by the nominal withdrawal γnsubscript𝛾𝑛\gamma\_{n}, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(tn+)=A​(tn)−γn,𝐴superscriptsubscript𝑡𝑛𝐴subscript𝑡𝑛subscript𝛾𝑛A(t\_{n}^{+})=A(t\_{n})-\gamma\_{n}, |  | (5) |

where A​(tn+)𝐴superscriptsubscript𝑡𝑛A(t\_{n}^{+}) denotes the guarantee account balance “immediately after” the withdrawal. Note that A​(tn+)≥0𝐴superscriptsubscript𝑡𝑛0A(t\_{n}^{+})\geq 0. The wealth account is reduced by the amount min⁡(γn,W​(tn))subscript𝛾𝑛𝑊subscript𝑡𝑛\min(\gamma\_{n},W(t\_{n})) and remains nonnegative. That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(tn+)=max⁡(W​(tn)−γn,0),𝑊superscriptsubscript𝑡𝑛𝑊subscript𝑡𝑛subscript𝛾𝑛0W(t\_{n}^{+})=\max(W(t\_{n})-\gamma\_{n},0), |  | (6) |

where W​(tn+)𝑊superscriptsubscript𝑡𝑛W(t\_{n}^{+}) is the wealth account balance immediately after the withdrawal. It is assumed that γ0=0subscript𝛾00\gamma\_{0}=0, i.e., there are no withdrawals at the start of the contract. Both the wealth and the guarantee account balance are 0 after contract expiration. That is, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(T+)=A​(T+)=0.𝑊superscript𝑇𝐴superscript𝑇0W(T^{+})=A(T^{+})=0. |  | (7) |

Throughout the VA contract, the wealth account is charged an insurance fee continuously at rate αtotsubscript𝛼tot\alpha\_{\rm tot} for the GMWB rider by the insurer to pay for the hedging cost of the guarantee. Discrete fees may be modeled similarly without any difficulty. The wealth account in turn evolves as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​W​(t)W​(t)=(μ​(t)−αtot​(t))​d​t+σ​(t)​d​B​(t),𝑑𝑊𝑡𝑊𝑡𝜇𝑡subscript𝛼tot𝑡𝑑𝑡𝜎𝑡𝑑𝐵𝑡\frac{dW(t)}{W(t)}=(\mu(t)-\alpha\_{\rm tot}(t))dt+\sigma(t)dB(t), |  | (8) |

for any t∈[0,T]𝑡0𝑇t\in[0,T] at which no withdrawal of wealth is made. Here, αtot​(t)=αins​(t)+αm​(t)subscript𝛼tot𝑡subscript𝛼ins𝑡subscript𝛼m𝑡\alpha\_{\rm tot}(t)=\alpha\_{\rm ins}(t)+\alpha\_{\rm m}(t) is the total fee rate, where αinssubscript𝛼ins\alpha\_{\rm ins} denotes the insurance fee and αmsubscript𝛼m\alpha\_{\rm m} denotes the management fee.

We denote the VA *plus* guarantee value function at time t𝑡t by V​(t,𝑿​(t)),t∈[0,T]

𝑉𝑡𝑿𝑡𝑡
0𝑇V(t,\bm{X}(t)),t\in[0,T], which corresponds to the present value under the respective pricing model of all future cash flows entitled to the policyholder on or after the current time t𝑡t. The remaining value after the final cash flow is, obviously, 0, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(T+,𝑿​(T+))=0.𝑉superscript𝑇𝑿superscript𝑇0V(T^{+},\bm{X}(T^{+}))=0. |  | (9) |

## 3 Backtesting the Reserving and Policyholder Strategies

In this section, we conduct backtests of the two proposed pricing models for VA products. We consider both from the policyholder’s perspective, where he or she decides the optimal withdrawal amount based on the pricing model chosen by the policyholder, and from the VA provider’s perspective, where the strategy of the hedging portfolio for the VA product is based on the pricing model chosen by the provider.

We take the S&P500 index as the equity index underlying the VA product, and run simulated withdrawals and hedging strategies on the historical data of the underlying well-diversified index. In particular, we take the historically observed monthly prices of the S&P500 index from 1871 to 2018, with all dividends reinvested, and discounted by the locally risk-free savings account. The S&P500 data after 1963 are obtained from Datastream, and the earlier part from 1871 until 1963 is reconstructed in Shiller ([2015](#bib.bib16)). The S&P500 total return index provides a good approximation of the dynamics of the market portfolio (MP) of the US domestic stock market. We consider the pricing of a GMWB contract written on a VA account tracking the index over the 30-year period from Feb. 1988 to Feb. 2018, based on the underlying models estimated from the historical index prices prior to this period. We consider both the MMM and the BSM as the underlying dynamics, as specified by SDEs ([23](#A2.E23 "In B.2 The minimal market model ‣ Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) and ([19](#A2.E19 "In B.1 The Black-Scholes model ‣ Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) respectively, and compare the evolution of the guarantee values under both models and respective pricing rules.

The log-prices of the S&P500 total return index are shown in Figure [1](#S3.F1 "Figure 1 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") (a). We take the first 97 years of the available data, from Jan. 1871 to Feb 1988 for estimations. The MMM parameters were estimated as follows:
To estimate the overall trend of growth S​(t)Y​(t)=α0η​eη​t𝑆𝑡𝑌𝑡subscript𝛼0𝜂superscript𝑒𝜂𝑡\frac{S(t)}{Y(t)}=\frac{\alpha\_{0}}{\eta}e^{\eta t} for the MMM, a straight line is fitted to the log-index prices and the slope is taken as the estimated total growth rate η𝜂\eta, and the scaling factor α0subscript𝛼0\alpha\_{0} is determined from the intercept. The normalized index Y​(t)𝑌𝑡Y(t) thus obtained is shown in Figure [1](#S3.F1 "Figure 1 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") (b). The BSM volatility in ([19](#A2.E19 "In B.1 The Black-Scholes model ‣ Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) was estimated following the standard MLE estimator. The estimated parameters are shown in Table [1](#S3.T1 "Table 1 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach").

|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| (a) S&P500 index with the estimated trend | (b) normalized index with the mean |

Figure 1: Estimated trend of growth and normalized index for the MMM.




Table 1: Estimated model parameters from the S&P500 historical prices.

|  | α0subscript𝛼0\alpha\_{0} | η𝜂\eta | σ𝜎\sigma |
| --- | --- | --- | --- |
| MMM | 2.857 | 0.0435 | - |
| BSM | - | - | 0.1441 |

We consider a stylized VA contract with GMWB where the policyholder invests 1 Million units of the US dollar savings account in a mutual fund that tracks the S&P500 total return index. For illustrative purposes, we assume there are no mutual fund management fees, so that αm​(t)=0subscript𝛼m𝑡0\alpha\_{\rm m}(t)=0 in ([8](#S2.E8 "In 2 Description of the VA Guarantee Product ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")), and the insurance fee rate αi​n​ssubscript𝛼𝑖𝑛𝑠\alpha\_{ins} is set at 00. (The case with nonzero total fees can be considered strictly analogously without affecting the main results from the current discussion. )
The policyholder purchases a GMWB rider that guarantees equal annual payments of the initial investment of 1 Million savings account units over a period of 30 years. The contracted withdrawals are, therefore, rated at 33,333 units of the savings account per annum. If the policyholder decides to withdraw more than the contracted amount, a penalty charge of 10% should apply to the excess part of the withdrawal. As mentioned in Section [2](#S2 "2 Description of the VA Guarantee Product ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach"), we assume that the penalty charge also applies to thew last withdrawal. That is, if the balance of the guarantee account exceeds the contracted withdrawal amount at maturity, withdrawal of this balance is mandatory and the same penalty rate applies to the excess part.

We first consider the situation where the VA provider prices the product under the BSM with the risk-neutral pricing approach (see [B](#A2 "Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) assuming that the policyholder makes optimal withdrawals under the same pricing rule. The VA provider maintains a nominal wealth account W​(t)𝑊𝑡W(t) of the policyholder’s wealth, and a nominal guarantee account A​(t)𝐴𝑡A(t) to keep track of the remaining guaranteed withdrawal allowance. The VA provider maintains an actual hedging portfolio V​(t)𝑉𝑡V(t) consisting of shares of the index-tracking mutual fund, or the index for short, and the locally risk-free savings account. We refer to the hedging portfolio as the reserve account of the VA product, which is the only real investment account involved. The reserve account starts at value V​(0)𝑉0V(0), the initial price of the VA product, and maintains a self-financing hedging strategy until a withdrawal is made on one of the withdrawal dates tnsubscript𝑡𝑛t\_{n}, when the net cash flow Cnsubscript𝐶𝑛C\_{n} is paid out of this account to the policyholder. The strategy maintained by the reserve account between withdrawal dates is the respective delta-hedging strategy.

Following Algorithm [1](#alg1 "Algorithm 1 ‣ Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") described in [C](#A3 "Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach"), we compute recursively the price process of the VA product, based on the historical index prices. The price process is shown in Figure [2](#S3.F2 "Figure 2 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") (a), with an initial value of 1.22 Million, and a terminal value of 7.11 Million before the final liquidation. The reserve account process, realized through delta-hedging, is shown in the same plot for comparison. The intial value of the reserve account is the same as the price process, and the terminal value is 7.07 Million. After liquidation, the reserve account ended up with a small deficit of -0.0344 Million, possibly due to hedging errors from discrete hedging.

The nominal wealth account W​(t)𝑊𝑡W(t) is shown in Figure [2](#S3.F2 "Figure 2 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") (b),
the optimal withdrawals made by the policyholder are shown in Figure [2](#S3.F2 "Figure 2 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") (c), and the guarantee account balance is shown in Figure [2](#S3.F2 "Figure 2 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") (d). Note that both the wealth account and the guarantee account are nominal only, used for keeping track of the status of the policyholder’s VA contract. No actual trading happens to these accounts. The optimal withdrawals are relatively uniform, except for no withdrawals in the beginning periods, and a large withdrawal in the last period. The relatively uniform withdrawal behavior is typical for the BSM and risk-neutral pricing, where the equity index dynamics is time-homogeneous. The only motivations to change the withdrawal pattern are changing the maturity date and wealth / guarantee account ratio.

|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| (a) contract value and reserve account | (b) nominal wealth account |
| Refer to caption | Refer to caption |
| (c) withdrawals | (d) nominal guarantee account |

Figure 2: Value processes (in millions of units of the savings account) associated with the VA product when the pricing and hedging as well as optimal withdrawals are performed based on the BSM and risk-neutral pricing.

For verification purposes we consider the alternative static withdrawal behavior from the policyholder. That is, we assume the policyholder makes a uniform withdrawal equal to 1/N1𝑁1/N Million units of the savings account on any one of the N𝑁N withdrawal dates. On the other hand, the VA provider manages the reserve account in the same way as in the optimal case irrespective of the policyholder’s withdrawal behavior, which is considered suboptimal in this case. The results are shown in Figure [3](#S3.F3 "Figure 3 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach"). The contract value process in this case is the same as for the case with optimal withdrawals. The reserve account process as well as the nominal wealth account process differ from the previous case due to different (suboptimal) withdrawals. The reserve account ended up with a rather significant surplus of 1.39 Million. This is due to the loss made by the policyholder for withdrawing suboptimally. In particular, premature withdrawals led to less wealth accumulations in the nominal wealth account, leading to significantly less liquidation cash flow entitled to the policyholder. Since the reserve account maintained the same hedging strategy as in the previous case, it ended up having a surplus after paying the reduced liabilities.

|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| (a) contract value and reserve account | (b) nominal wealth account |
| Refer to caption | Refer to caption |
| (c) withdrawals | (d) nominal guarantee account |

Figure 3: Value processes associated with the VA product when the pricing and hedging are performed based on the BSM and risk-neutral pricing assuming an optimal withdrawal behavior, while the actual withdrawal behavior follows the static strategy.

We next consider the situation where the policyholder makes withdrawals based on the MMM under the BA. That is, the policyholder’s withdrawals maximize the value of the VA contract as priced by the MMM under the BA. The VA provider, believing in the BSM under the risk-neutral pricing framework, manages the reserve account in the same way as in the previous cases, and views the policyholder’s withdrawals as being suboptimal. The VA provider thus expects to receive a surplus in the reserve account after maturity of the VA contract. The outcomes of this scenario are shown in Figure [4](#S3.F4 "Figure 4 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach").

|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| (a) contract value and reserve account | (b) nominal wealth account |
| Refer to caption | Refer to caption |
| (c) withdrawals | (d) nominal guarantee account |

Figure 4: Value processes associated with the VA product when the pricing and hedging are performed based on the BSM and risk-neutral pricing assuming an optimal withdrawal behavior, while the actual withdrawal behavior follows the MMM under the BA.

To the surprise of the VA provider, instead of having a surplus, the reserve account in this case ended up with a deficit of 1 Million, as indicated in Figure [4](#S3.F4 "Figure 4 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") (a). The withdrawal behavior of the policyholder is such that there are no withdrawals until the very end of the contract term, where a number of small withdrawals were followed by a large withdrawal on the maturity date. The nominal wealth account accumulated a high level of wealth due to no withdrawals in the early stages. The liquidation of this large wealth led to the deficit of the reserve account, which followed a hedging strategy assuming more early withdrawals.

The failure of the VA provider in hedging the VA product, when the policyholder behaved optimally under a different pricing framework, indicates the potential inappropriateness of the BSM and risk-neutral pricing adopted by the VA provider. In particular, the policyholder believed in the long-term growth of the market and invested for this growth according to the MMM. The VA provider, from a risk-neutral perspective, did not recognize the long-term growth, and managed the reserve account with a short-term vision, leading to the failure of matching the performance of the policyholder’s wealth account. Note that the MMM and the associated long-term growth rate were estimated from prior returns of the index. Thus, no “looking into the future” is associated with the policyholder’s withdrawal behavior.

It is interesting to see what happens in a reversed scenario, where the VA provider prices and hedges under the MMM and BA, and the policyholder makes optimal withdrawals according to the BSM and risk-neutral pricing. Without repeating the detailed description of this scenario, the outcomes are shown in Figure [5](#S3.F5 "Figure 5 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach"), where the reserve account was managed recognizing the long-term growth under the MMM and BA, leading to a higher level of wealth accumulation than the nominal wealth account, and a surplus of 1.05 Million. The withdrawal behavior of the policyholder is similar to the first case considered, with a rather uniform withdrawal a few years into the contract term.

|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| (a) contract value and reserve account | (b) nominal wealth account |
| Refer to caption | Refer to caption |
| (c) withdrawals | (d) nominal guarantee account |

Figure 5: Value processes associated with the VA product when the pricing and hedging are performed based on the MMM and BA assuming an optimal withdrawal behavior, while the actual withdrawal behavior follows the BSM under risk-neutral pricing.

Finally, to complete the empirical study, we consider the scenario when both the VA provider and the policyholder follow the MMM under the BA. The outcomes are shown in Figure [6](#S3.F6 "Figure 6 ‣ 3 Backtesting the Reserving and Policyholder Strategies ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach"). It can be seen that the VA provider in this case successfully hedged the VA product, ending up with a small deficit of 0.0319 Million in the reserve account.

When comparing the two optimal withdrawal strategies based on the two pricing models, then one realizes that the strategy based on the BSM and risk-neutral pricing realizes a total withdrawal of 7.41 Million (of the locally risk-free security) over time, more than the total withdrawal of 6.29 Million following the static strategy. On the other hand, the optimal strategy based on the BA using the MMM realized a total withdrawal of 8.47 Million, which is producing more than 1 Million units of the savings account, thus, doubling the initial investment when counted in units of the savings account. This is considerably more than the risk-neutral approach delivered using the BSM. The reason is that the BSM under risk-neutral pricing creates a significant model error, which neglects the significantly positive long-term growth rate of the S&P500 over that of the savings account and, thus, gives major investment potential away. By changing the production method in the area of VAs as demonstrated, significantly higher returns on investment can be achieved.

|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| (a) contract value and reserve account | (b) nominal wealth account |
| Refer to caption | Refer to caption |
| (c) withdrawals | (d) nominal guarantee account |

Figure 6: Value processes associated with the VA product when the pricing and hedging as well as the optimal withdrawals are performed based on the MMM and the BA.

## 4 Conclusions

We considered the pricing of a variable annuity (VA) with GMWB under the benchmark approach (BA), where a classical equivalent risk-neutral pricing measure may not exist. We employed the real-world pricing formula to compute the value of the VA contract with GMWB under the minimal market model (MMM), and the associated hedging strategy for the VA product. We compared our results with those under the classical Black-Scholes model (BSM) under the risk-neutral pricing framework, through empirical backtests on the historical prices of the S&P500 total return index, which were taken as the underlying of the VA product.

From the empirical studies, we found that the VA provider can successfully hedge the VA product when the VA provider and the policyholder both employ the same pricing model to make hedging and withdrawal decisions. When the policyholder took a static withdrawal strategy without optimization, the VA provider ended up with a surplus. When the VA provider relied on the MMM and the BA to make hedging decisions and the policyholder took the BSM and the risk-neutral approach, the VA provider ended up with a surplus. However, when the VA provider took the BSM and risk-neutral approach, and the policyholder relied on the MMM and the BA, the VA provider ended up with a deficit. Our empirical studies show that the BSM and risk-neutral approach to the VA pricing problem may not be appropriate, in that when a sophisticated policyholder armed with a more accurate model such as the MMM, the VA provider risks having a significant deficit in the hedging of the VA product.

## References

* Bauer et al. (2008)

  Bauer, D., Kling, A., Russ, J., 2008. A universal pricing framework for
  guaranteed minimum benefits in variable annuities. ASTIN Bulletin 38 (2),
  621–651.
* Broadie and Kaya (2006)

  Broadie, M., Kaya, O., 2006. Exact simulation of stochastic volatility and
  other affine jump diffusion processes. Operational Research 54, 217–231.
* Campbell and Viceira (2005)

  Campbell, J. Y., Viceira, L., 2005. The term structure of the risk-return
  tradeoff. Tech. rep., National Bureau of Economic Research.
* Delbaen and Schachermayer (2006)

  Delbaen, F., Schachermayer, W., 2006. The Mathematics of Arbitrage. Springer
  Science & Business Media.
* Fergusson and Platen (2006)

  Fergusson, K., Platen, E., 2006. On the distributional characterization of
  log-returns of a world stock index. Applied Mathematical Finance 13 (1),
  19–38.
* Kalberer and Ravindran (2009)

  Kalberer, T., Ravindran, K., 2009. Variable Annuities. Risk Books.
* Karatzas and Shreve (1991)

  Karatzas, I., Shreve, S. E., 1991. Brownian Motion and Stochastic Calculus, 2nd
  Edition. Springer.
* Ledlie et al. (2008)

  Ledlie, M. C., Corry, D. P., Finkelstein, G. S., Ritchie, A. J., Su, K.,
  Wilson, D. C. E., 2008. Variable annuities. British Actuarial Journal 14 (2),
  327–389.
* Luo and Shevchenko (2015)

  Luo, X., Shevchenko, P., 5 2015. Valuation of variable annuities with
  guaranteed minimum withdrawal and death benefits via stochastic control
  optimization. Insurance Mathematics and Economics 62, 5–15.
* Moenig and Bauer (2015)

  Moenig, T., Bauer, D., 2015. Revisiting the risk-neutral approach to optimal
  policyholder behavior: A study of withdrawal guarantees in variable
  annuities. Review of Finance 20 (2), 759.
* Platen (2001)

  Platen, E., 2001. A minimal financial market model. In: Trends in Mathematics.
  Birkhäuser, pp. 293–301.
* Platen and Heath (2006)

  Platen, E., Heath, D., 2006. A Benchmark Approach to Quantitative Finance.
  Springer Finance. Springer.
* Platen and Rendek (2012)

  Platen, E., Rendek, R., 2012. Approximating the numeraire portfolio by naive
  diversification. Journal of Asset Management 13 (1), 34–50.
* Revuz and Yor (1999)

  Revuz, D., Yor, M., 1999. Continuous Martingales and Brownian Motion, 3rd
  Edition. Springer.
* Shevchenko and Luo (2016)

  Shevchenko, P. V., Luo, X., 2016. A unified pricing of variable annuity
  guarantees under the optimal stochastic control framework. Risks 4 (3).
* Shiller (2015)

  Shiller, R. J., 2015. Irrational Exuberance: Revised and expanded third
  edition. Princeton University Press.
* Sun et al. (2018)

  Sun, J., Shevchenko, P. V., Fung, M. C., 2018. The impact of management fees on
  the pricing of variable annuity guarantees. Risks 6 (3).

## Appendix A A Brief Overview of the Benchmark Approach

In this section, we give a brief overview of the BA under a diffusive market model. Much of this section follows from Platen and Heath ([2006](#bib.bib12)), to which interested readers are referred for a more complete treatment.

We consider a general diffusive financial market model with uncertainties driven by a d-dimensional Brownian motion 𝑾𝑾\bm{W}, with 𝑾​(t)={(W​(t)1,…,W​(t)d)⊤,t∈[0,T]}𝑾𝑡

superscript𝑊superscript𝑡1…𝑊superscript𝑡𝑑top𝑡
0𝑇\bm{W}(t)=\{(W(t)^{1},...,W(t)^{d})^{\top},\,t\in[0,T]\},
defined on a filtered probability space (Ω,ℱ,𝔽,ℙ)Ωℱ𝔽ℙ(\Omega,\mathcal{F},{\mathbb{F}},{\mathbb{P}}), where T𝑇T is some fixed time horizon, and the filtration 𝔽={ℱt,t∈[0,T]}𝔽

subscriptℱ𝑡𝑡
0𝑇\mathbb{F}=\{\mathcal{F}\_{t},\,t\in[0,T]\} satisfies the usual conditions of right continuity and completeness, and models the accumulation of information over time; see Karatzas and Shreve ([1991](#bib.bib7)). We assume that there exists a locally risk-free savings account S0​(t)superscript𝑆0𝑡S^{0}(t) and m𝑚m nonnegative risky primary security accounts 𝑺​(t)=(S1​(t),…,Sm​(t))⊤𝑺𝑡superscriptsuperscript𝑆1𝑡…superscript𝑆𝑚𝑡top\bm{S}(t)=(S^{1}(t),...,S^{m}(t))^{\top} satisfying the vector stochastic differential equation (SDE)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝑺​(t)=𝑺​(t)​(a​(t)​d​t+b​(t)⋅d​𝑾​(t)),t∈[0,T],formulae-sequence𝑑𝑺𝑡𝑺𝑡𝑎𝑡𝑑𝑡⋅𝑏𝑡𝑑𝑾𝑡𝑡0𝑇{d\bm{S}(t)}={\bm{S}(t)}\left({a(t)dt+b(t)\cdot d\bm{W}(t)}\right),\quad t\in[0,T], |  | (10) |

where a​(t)𝑎𝑡a(t) is the instantaneous drift vector and b​(t)𝑏𝑡b(t) the instantaneous volatility matrix, which both are assumed to be predictable and such that a unique strong solution of the above system of SDEs exists. We assume that all dividends and interests are reinvested. Without loss of generality, we further assume that S0​(t)≡1superscript𝑆0𝑡1S^{0}(t)\equiv 1. This means that we denominate all security prices in units of the locally risk-free savings account. In practice, the locally risk-free savings account may be approximated by the money market account that invests in short-term T-bills in a rolling manner. Thus in our notation, all primary security accounts are discounted by the locally risk-free savings account.

We denote by S𝝅superscript𝑆𝝅S^{\bm{\pi}} the value process of a strictly positive, self-financing portfolio with portfolio weights 𝝅​(t)=(π1​(t),…,πm​(t))⊤,t∈[0,T]formulae-sequence𝝅𝑡superscriptsuperscript𝜋1𝑡…superscript𝜋𝑚𝑡top𝑡0𝑇\bm{\pi}(t)=(\pi^{1}(t),...,\pi^{m}(t))^{\top},t\in[0,T], which invests at time t𝑡t a fraction πj​(t)superscript𝜋𝑗𝑡\pi^{j}(t) of the total wealth in the j𝑗jth primary security account, and the remaining wealth in the locally risk-free savings account. The value process satisfies then the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S𝝅​(t)S𝝅​(t)=𝝅​(t)⊤​(a​(t)​d​t+b​(t)⋅d​𝑾​(t)),t∈[0,T].formulae-sequence𝑑superscript𝑆𝝅𝑡superscript𝑆𝝅𝑡𝝅superscript𝑡top𝑎𝑡𝑑𝑡⋅𝑏𝑡𝑑𝑾𝑡𝑡0𝑇\frac{dS^{\bm{\pi}}(t)}{S^{\bm{\pi}}(t)}=\bm{\pi}(t)^{\top}(a(t)dt+b(t)\cdot d\bm{W}(t)),\quad t\in[0,T]. |  | (11) |

By Ito’s formula, the SDE for the log-price is of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​log⁡S𝝅​(t)=𝝅​(t)⊤​((a​(t)−12​b​(t)​b​(t)⊤​𝝅​(t))​d​t+b​(t)⋅d​𝑾​(t)),t∈[0,T].formulae-sequence𝑑superscript𝑆𝝅𝑡𝝅superscript𝑡top𝑎𝑡12𝑏𝑡𝑏superscript𝑡top𝝅𝑡𝑑𝑡⋅𝑏𝑡𝑑𝑾𝑡𝑡0𝑇d\log S^{\bm{\pi}}(t)=\bm{\pi}(t)^{\top}\left({\left({a(t)-\frac{1}{2}b(t)b(t)^{\top}\bm{\pi}(t)}\right)dt+b(t)\cdot d\bm{W}(t)}\right),\quad t\in[0,T]. |  | (12) |

We consider the growth-optimal portfolio (GP) S𝝅∗superscript𝑆superscript𝝅S^{\bm{\pi}^{\*}} of this investment universe for which the instantaneous expected growth rate, that is, the drift of ([12](#A1.E12 "In Appendix A A Brief Overview of the Benchmark Approach ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")), is maximized for all t𝑡t. This is achieved by setting the optimal portfolio weights 𝝅∗​(t)superscript𝝅𝑡\bm{\pi}^{\*}(t) to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝅∗​(t)=arg⁡max𝝅​𝝅⊤​(a​(t)−12​b​(t)​b​(t)⊤​𝝅),t∈[0,T].formulae-sequencesuperscript𝝅𝑡𝝅superscript𝝅top𝑎𝑡12𝑏𝑡𝑏superscript𝑡top𝝅𝑡0𝑇\bm{\pi}^{\*}(t)=\underset{\bm{\pi}}{\arg\max}\,\bm{\pi}^{\top}\left({a(t)-\frac{1}{2}b(t)b(t)^{\top}\bm{\pi}}\right),\quad t\in[0,T]. |  | (13) |

We assume that a solution to ([13](#A1.E13 "In Appendix A A Brief Overview of the Benchmark Approach ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) exists a.s. for all t∈[0,T]𝑡0𝑇t\in[0,T]. One potential such solution is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝅∗​(t)=(b​(t)​b​(t)⊤)+​a​(t),t∈[0,T],formulae-sequencesuperscript𝝅𝑡superscript𝑏𝑡𝑏superscript𝑡top𝑎𝑡𝑡0𝑇\bm{\pi}^{\*}(t)=\left({b(t)b(t)^{\top}}\right)^{+}a(t),\quad t\in[0,T], |  | (14) |

where (b​(t)​b​(t)⊤)+superscript𝑏𝑡𝑏superscript𝑡top\left({b(t)b(t)^{\top}}\right)^{+} denotes the Moore-Penrose generalized inverse of the self-adjoint matrix b​(t)​b​(t)⊤𝑏𝑡𝑏superscript𝑡topb(t)b(t)^{\top}. Note that the value process of the GP is unique, however, the fractions may vary due to potential redundancies in the primary security accounts

For the market model to be viable, we assume that the GP process, denoted as S​(t):=S𝝅∗​(t),t∈[0,T]formulae-sequenceassign𝑆𝑡superscript𝑆superscript𝝅𝑡𝑡0𝑇S(t):=S^{\bm{\pi}^{\*}}(t),t\in[0,T], with 𝝅∗​(t)superscript𝝅𝑡\bm{\pi}^{\*}(t) given by ([14](#A1.E14 "In Appendix A A Brief Overview of the Benchmark Approach ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")), exists and is strictly positive. By substituting ([14](#A1.E14 "In Appendix A A Brief Overview of the Benchmark Approach ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) into ([11](#A1.E11 "In Appendix A A Brief Overview of the Benchmark Approach ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")), we obtain the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S​(t)S​(t)=‖𝜽​(t)‖2​d​t+𝜽​(t)⋅d​𝑾​(t),t∈[0,T],formulae-sequence𝑑𝑆𝑡𝑆𝑡superscriptnorm𝜽𝑡2𝑑𝑡⋅𝜽𝑡𝑑𝑾𝑡𝑡0𝑇\frac{dS(t)}{S(t)}=\|\bm{\theta}(t)\|^{2}dt+\bm{\theta}(t)\cdot d\bm{W}(t),\quad t\in[0,T], |  | (15) |

where 𝜽​(t)=b​(t)⊤​𝝅∗​(t)𝜽𝑡𝑏superscript𝑡topsuperscript𝝅𝑡\bm{\theta}(t)=b(t)^{\top}\bm{\pi}^{\*}(t). The above SDE can further be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S​(t)=α​(t)​d​t+α​(t)​S​(t)​d​B​(t),t∈[0,T],formulae-sequence𝑑𝑆𝑡𝛼𝑡𝑑𝑡𝛼𝑡𝑆𝑡𝑑𝐵𝑡𝑡0𝑇dS(t)=\alpha(t)dt+\sqrt{\alpha(t)S(t)}dB(t),\quad t\in[0,T], |  | (16) |

where the drift α​(t)=‖𝜽​(t)‖2​S​(t)𝛼𝑡superscriptnorm𝜽𝑡2𝑆𝑡\alpha(t)=\|\bm{\theta}(t)\|^{2}S(t) is assumed to be strictly positive, and B∗​(t)superscript𝐵𝑡B^{\*}(t), defined by the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​B​(t)=𝜽​(t)‖𝜽​(t)‖⋅d​𝑾​(t)t∈[0,T],formulae-sequence𝑑𝐵𝑡⋅𝜽𝑡norm𝜽𝑡𝑑𝑾𝑡𝑡0𝑇dB(t)=\frac{\bm{\theta}(t)}{\|\bm{\theta}(t)\|}\cdot d\bm{W}(t)\quad t\in[0,T], |  | (17) |

with B∗​(0)=0superscript𝐵00B^{\*}(0)=0, forms a standard Brownian motion by Levy’s characterization theorem. So far, we only re-parametrized the GP dynamics different to the common volatility modeling specification. Note that the above drift α​(t)𝛼𝑡\alpha(t) can be, at this stage, still very general. Later on, we will make this drift more specific, which yields then a proper model.

The GP is the unique portfolio which, when used as numeraire or benchmark, makes any benchmarked portfolio process S^𝝅superscript^𝑆𝝅\hat{S}^{\bm{\pi}}, defined as S^𝝅​(t)=S𝝅​(t)S​(t)superscript^𝑆𝝅𝑡superscript𝑆𝝅𝑡𝑆𝑡\hat{S}^{\bm{\pi}}(t)=\frac{S^{\bm{\pi}}(t)}{S(t)}, a local martingale. If we assume the portfolio process to be nonnegative, the benchmarked portfolio process becomes a supermartingale by Fatou’s lemma.
Given an ℱTsubscriptℱ𝑇\mathcal{F}\_{T}-measurable nonnegative contingent claim H​(T)≥0𝐻𝑇0H(T)\geq 0 with maturity T𝑇T, its, so called, fair price process under the BA is given by the real-world pricing formula as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(t)=Et​(S​(t)S​(T)​H​(T)),t∈[0,T],formulae-sequence𝐻𝑡subscript𝐸𝑡𝑆𝑡𝑆𝑇𝐻𝑇𝑡0𝑇H(t)=E\_{t}\left({\frac{S(t)}{S(T)}H(T)}\right),\quad t\in[0,T], |  | (18) |

where Et(⋅)=E(⋅|ℱt)E\_{t}(\cdot)=E(\cdot|\mathcal{F}\_{t}) denotes the ℱtsubscriptℱ𝑡\mathcal{F}\_{t}-conditional expectation under the real-world probability measure ℙℙ{\mathbb{P}}.
The benchmarked fair price process, defined as H^​(t)=H​(t)S​(t)^𝐻𝑡𝐻𝑡𝑆𝑡\hat{H}(t)=\frac{H(t)}{S(t)}, forms then a nonnegative (𝔽,ℙ)𝔽ℙ(\mathbb{F},{\mathbb{P}})-martingale. The benchmarked fair price process H^^𝐻\hat{H}, if replicable, represents the least expensive portfolio among all benchmarked nonnegative self-financing replication portfolios, which form supermartingales.

## Appendix B Modeling the Underlying Equity Index

In this section we specify the model parameters of the SDE governing the underlying equity index ([1](#S2.E1 "In 2 Description of the VA Guarantee Product ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")). The model parameters are described respectively under the risk-neutral pricing framework and the BA. As mentioned in Section [2](#S2 "2 Description of the VA Guarantee Product ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach"), we take the locally risk-free security account as the numeraire, and consider all prices denominated in units of the locally risk-free savings account.

### B.1 The Black-Scholes model

The classical BSM is probably the most widely-known model to describe the price dynamics of a risky security within the framework of risk-neutral pricing theory. Under the BSM, the drift α​(t)𝛼𝑡\alpha(t) in the general formulation ([16](#A1.E16 "In Appendix A A Brief Overview of the Benchmark Approach ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) is modelled as α​(t)=σ2​S​(t)𝛼𝑡superscript𝜎2𝑆𝑡\alpha(t)=\sigma^{2}S(t), where σ𝜎\sigma is the constant volatility parameter, and the equity index follows under the real-world probability measure ℙℙ{\mathbb{P}} the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S​(t)=σ2​S​(t)​d​t+σ​S​(t)​d​B​(t),𝑑𝑆𝑡superscript𝜎2𝑆𝑡𝑑𝑡𝜎𝑆𝑡𝑑𝐵𝑡dS(t)=\sigma^{2}S(t)\,dt+\sigma S(t)\,dB(t), |  | (19) |

where B𝐵B is a standard ℙℙ{\mathbb{P}}-Brownian motion. The equity index thus follows the geometric Brownian motion

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(t)=S​(0)​exp⁡(12​σ2​t+σ​B​(t)),t∈[0,T].formulae-sequence𝑆𝑡𝑆012superscript𝜎2𝑡𝜎𝐵𝑡𝑡0𝑇S(t)=S(0)\exp\left({{\frac{1}{2}\sigma^{2}}t+\sigma B(t)}\right),\quad{t\in[0,T]}. |  | (20) |

Following the standard procedures of Girsanov’s theorem, the BSM admits a unique equivalent risk-neutral pricing measure ℚℚ{\mathbb{Q}}, with the Radon-Nikodym derivative given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z​(t)=e−σ​B​(t)−σ22​t=S​(0)S​(t),t∈[0,T],formulae-sequence𝑍𝑡superscript𝑒𝜎𝐵𝑡superscript𝜎22𝑡𝑆0𝑆𝑡𝑡0𝑇Z(t)=e^{-{\sigma}B(t)-\frac{\sigma^{2}}{2}t}={\frac{S(0)}{S(t)}},\quad t\in[0,T], |  | (21) |

which is seen to be of the same form as the discount factor in ([18](#A1.E18 "In Appendix A A Brief Overview of the Benchmark Approach ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")), as expected. Under the risk-neutral measure ℚℚ{\mathbb{Q}}, the index S𝑆S is driftless and satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S​(t)=σ​S​(t)​d​Bℚ​(t),t∈[0,T],formulae-sequence𝑑𝑆𝑡𝜎𝑆𝑡𝑑superscript𝐵ℚ𝑡𝑡0𝑇dS(t)=\sigma S(t)dB^{\mathbb{Q}}(t),\quad{t\in[0,T]}, |  | (22) |

where Bℚ​(t)=B​(t)+σ​tsuperscript𝐵ℚ𝑡𝐵𝑡𝜎𝑡B^{\mathbb{Q}}(t)=B(t)+{\sigma}t is a standard ℚℚ{\mathbb{Q}}-Brownian motion.

### B.2 The minimal market model

The minimal market model (MMM), see Platen ([2001](#bib.bib11)), is a stylized model under the BA. The MMM is incompatible with the risk-neutral pricing framework, in that an equivalent risk-neutral probability measure cannot exist.
When we apply the MMM, we make two important assumptions. First, the GP of a given investment universe is, generally, difficult to construct. However, it is shown by Platen and Rendek ([2012](#bib.bib13)) that the GP of a stock market can be approximated by a respective well-diversified equity index. The MMM assumes that the equity index is a good proxy for the GP. Second, the drift coefficient α​(t)𝛼𝑡\alpha(t) in the general GP model ([16](#A1.E16 "In Appendix A A Brief Overview of the Benchmark Approach ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) is theoretically a complicated process depending on the instantaneous market prices of risks, and is, thus, difficult to specify. The MMM makes a critical simplification by assuming that α​(t)𝛼𝑡\alpha(t) is a simple deterministic exponential function α​(t)=α0​eη​t𝛼𝑡subscript𝛼0superscript𝑒𝜂𝑡\alpha(t)=\alpha\_{0}e^{\eta t}. As a result, under the MMM, the GP S​(t)𝑆𝑡S(t) follows a time-transformed squared Bessel process of dimension four with a deterministic time transformation and satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S​(t)=(α0​eη​t)​d​t+α0​eη​t​S​(t)​d​B​(t),t∈[0,T]formulae-sequence𝑑𝑆𝑡subscript𝛼0superscript𝑒𝜂𝑡𝑑𝑡subscript𝛼0superscript𝑒𝜂𝑡𝑆𝑡𝑑𝐵𝑡𝑡0𝑇dS(t)=\left({\alpha\_{0}e^{\eta t}}\right)dt+\sqrt{\alpha\_{0}e^{\eta t}{S(t)}}dB(t),\quad{t\in[0,T]} |  | (23) |

under the real-world probability measure ℙℙ{\mathbb{P}}; see Revuz and Yor ([1999](#bib.bib14)). Here η𝜂\eta is the long-term expected growth rate of the equity index, and α0subscript𝛼0\alpha\_{0} is a constant representing the initial scale of the index.

We define in the model the normalized GP as Y​(t)=ηα0​eη​t​S​(t),t∈[0,T]formulae-sequence𝑌𝑡𝜂subscript𝛼0superscript𝑒𝜂𝑡𝑆𝑡𝑡0𝑇Y(t)=\frac{\eta}{\alpha\_{0}e^{\eta t}}S(t),t\in[0,T], which satisfies the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Y​(t)=(1−Y​(t))​η​d​t+Y​(t)​η​d​B​(t),t∈[0,T].formulae-sequence𝑑𝑌𝑡1𝑌𝑡𝜂𝑑𝑡𝑌𝑡𝜂𝑑𝐵𝑡𝑡0𝑇dY(t)=(1-Y(t))\eta dt+\sqrt{Y(t)\eta}dB(t),\quad{t\in[0,T]}. |  | (24) |

The normalized GP is seen to be mean-reverting around the level 111. The mean-reversion of the normalized index implies a “trend reversion” of the GP around its long-term exponential growth. It is well documented that a well-diversified index such as the S&P500 index moves in the long-run in a trend reverting pattern, where the trend is usually interpreted as a slowly moving “fundamental value” process; see Shiller ([2015](#bib.bib16)). By decomposing the GP into the normalized GP index Y​(t)𝑌𝑡Y(t) and a simple exponential fundamental value function α0​eη​tηsubscript𝛼0superscript𝑒𝜂𝑡𝜂\frac{\alpha\_{0}e^{\eta t}}{\eta}, the MMM parsimoniously captures this important stylized fact. Furthermore, the instantaneous squared volatility of the normalized GP equals that of the GP and is inversely proportional to the value of the normalized GP, generating the so-called leverage effect.

The normalized GP described by ([24](#A2.E24 "In B.2 The minimal market model ‣ Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) is a time transformed square-root process of dimension four, with the transition law of a noncentral Chi-squared (NCX2) distribution, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y​(u)​=ℒ​1−e−η​(u−t)4​χ42​(4​e−η​(u−t)1−e−η​(u−t)​Y​(t)),0≤t<u≤T,  𝑌𝑢ℒ1superscript𝑒𝜂𝑢𝑡4subscriptsuperscript𝜒244superscript𝑒𝜂𝑢𝑡1superscript𝑒𝜂𝑢𝑡𝑌𝑡0 𝑡𝑢𝑇Y(u)\overset{\mathcal{L}}{=}\frac{1-e^{-\eta(u-t)}}{4}\chi^{2}\_{4}\left({\frac{4e^{-\eta(u-t)}}{1-e^{-\eta(u-t)}}Y(t)}\right),\quad 0\leq t<u\leq T, |  | (25) |

where χ42​(ζ)subscriptsuperscript𝜒24𝜁\chi^{2}\_{4}(\zeta) denotes a NCX2 random variable of degree 444 and noncentrality parameter ζ𝜁\zeta; see, e.g., Broadie and Kaya ([2006](#bib.bib2)). The χ42​(ζ)subscriptsuperscript𝜒24𝜁\chi^{2}\_{4}(\zeta) random variable has finite moments of all positive orders. The probability density function (PDF) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(ζ,x)=12​e−ζ+x2​(xζ)​I1​(ζ​x),x>0,formulae-sequence𝑓𝜁𝑥12superscript𝑒𝜁𝑥2𝑥𝜁subscript𝐼1𝜁𝑥𝑥0f(\zeta,x)=\frac{1}{2}e^{-\frac{\zeta+x}{2}}\left({\sqrt{\frac{x}{\zeta}}}\right)I\_{1}\left({\sqrt{\zeta x}}\right),\quad x>0, |  | (26) |

where I1​(⋅)subscript𝐼1⋅I\_{1}(\cdot) is the first order modified Bessel function of the first kind, see, e.g., Revuz and Yor ([1999](#bib.bib14)). The transition density function of the normalized index is, thus, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(t,Y​(t);u,Y​(u))=41−e−η​(u−t)​f​(4​e−η​(u−t)1−e−η​(u−t)​Y​(t),41−e−η​(u−t)​Y​(u)).𝑝𝑡𝑌𝑡𝑢𝑌𝑢41superscript𝑒𝜂𝑢𝑡𝑓4superscript𝑒𝜂𝑢𝑡1superscript𝑒𝜂𝑢𝑡𝑌𝑡41superscript𝑒𝜂𝑢𝑡𝑌𝑢p\left({t,Y(t);u,Y(u)}\right)=\frac{4}{1-e^{-\eta(u-t)}}f\left({\frac{4e^{-\eta(u-t)}}{1-e^{-\eta(u-t)}}Y(t),\frac{4}{1-e^{-\eta(u-t)}}Y(u)}\right). |  | (27) |

It is worth mentioning that the normalized GP is dimensionless, and serves as a nontrivial state variable in that the transition density over the time period (t,u)𝑡𝑢(t,u) depends nonlinearly on the current state Y​(t)𝑌𝑡Y(t). This is in marked contrast to the BSM, where the current price serves as a scaling factor of a time-homogeneous geometric Brownian motion. An implication of this dependence is that, unlike the BSM, ([23](#A2.E23 "In B.2 The minimal market model ‣ Appendix B Modeling the Underlying Equity Index ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) is neither scale nor time invariant. Note however, the GP, as a time transformed squared Bessel process, has some self-similarity property.

## Appendix C Pricing of the VA with Guarantee

In this section we consider the pricing of the VA product described in Section [2](#S2 "2 Description of the VA Guarantee Product ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach"). For the pricing of a given set of cash flows, we adopt the concept of a stochastic discount factor (SDF), where the present value of the cash flows are given by the sum of their expected values, after discounting by the SDF, conditional on all current information. Both risk-neutral pricing and pricing under the BA can be formulated in terms of an appropriate SDF. For more information on risk-neutral pricing theory, see Delbaen and Schachermayer ([2006](#bib.bib4)) for an account. For a brief description of the BA, see [A](#A1 "Appendix A A Brief Overview of the Benchmark Approach ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach").

To price the VA with guarantee value function V​(0,𝑿​(0))𝑉0𝑿0V(0,\bm{X}(0)), we note that no withdrawal is made between any withdrawal dates (tn−1,tn)subscript𝑡𝑛1subscript𝑡𝑛(t\_{n-1},t\_{n}), and that the wealth account is self-financing within this period. This leads to the following recurrence relation for the (left-continuous with right-hand limits) guarantee value function,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(tn−1+,𝑿​(tn−1+))=Etn−1+​(D​(tn−1,tn)​V​(tn,𝑿​(tn))),𝑉superscriptsubscript𝑡𝑛1𝑿superscriptsubscript𝑡𝑛1subscript𝐸superscriptsubscript𝑡𝑛1𝐷subscript𝑡𝑛1subscript𝑡𝑛𝑉subscript𝑡𝑛𝑿subscript𝑡𝑛V(t\_{n-1}^{+},\bm{X}(t\_{n-1}^{+}))=E\_{t\_{n-1}^{+}}\left({D(t\_{n-1},t\_{n})V(t\_{n},\bm{X}(t\_{n}))}\right), |  | (28) |

where Et(⋅)=E(⋅|𝑿(t))E\_{t}(\cdot)=E(\cdot|\bm{X}(t)) is the expectation under the real-world probability measure ℙℙ{\mathbb{P}}, conditional on the current information represented by 𝑿​(t)𝑿𝑡\bm{X}(t), and D​(t,u),0≤t<u≤T

𝐷𝑡𝑢0
𝑡𝑢𝑇D(t,u),0\leq t<u\leq T is the SDF over (t,u)𝑡𝑢(t,u). Under the BA, the SDF is given by D​(t,u)=S​(t)S​(u)𝐷𝑡𝑢𝑆𝑡𝑆𝑢D(t,u)=\frac{S(t)}{S(u)}, i.e., the ratio of the inverse GP. Under the risk-neutral pricing framework, the SDF D​(t,u)=Z​(u)Z​(t)𝐷𝑡𝑢𝑍𝑢𝑍𝑡D(t,u)=\frac{Z(u)}{Z(t)}, with Z​(t):=Et​(d​ℚd​ℙ)assign𝑍𝑡subscript𝐸𝑡𝑑ℚ𝑑ℙZ(t):=E\_{t}\left({\frac{d{\mathbb{Q}}}{d{\mathbb{P}}}}\right) being the Radon-Nikodym derivative of the measure change from the real-world probability measure ℙℙ{\mathbb{P}} to the equivalent risk-neutral measure ℚℚ{\mathbb{Q}}, conditional on all available information at t𝑡t.

Upon withdrawal at time tnsubscript𝑡𝑛t\_{n}, 0<n<N0𝑛𝑁0<n<N, the left-hand limit of the value function satisfies the following jump condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(tn,𝑿​(tn))=V​(tn+,𝑿​(tn+))+C​(γn,𝑿​(tn)).𝑉subscript𝑡𝑛𝑿subscript𝑡𝑛𝑉superscriptsubscript𝑡𝑛𝑿superscriptsubscript𝑡𝑛𝐶subscript𝛾𝑛𝑿subscript𝑡𝑛V(t\_{n},\bm{X}(t\_{n}))=V(t\_{n}^{+},\bm{X}(t\_{n}^{+}))+C(\gamma\_{n},\bm{X}(t\_{n})). |  | (29) |

In other words, the guarantee value immediately before the withdrawal is the sum of the value immediately after the withdrawal and the cash flow of the withdrawal. The active policyholder follows a dynamic strategy, which we obtain as the solution of the respective stochastic control problem. That is, for 0<n<N0𝑛𝑁0<n<N, the withdrawal amount γnsubscript𝛾𝑛\gamma\_{n} is chosen according to the following total value maximizing strategy,

|  |  |  |  |
| --- | --- | --- | --- |
|  | γn=Γ​(tn,𝑿​(tn))=arg⁡max0≤γ≤A​(tn)​{V​(tn+,𝑿​(tn)∖γ)+C​(γ,𝑿​(tn))},subscript𝛾𝑛Γsubscript𝑡𝑛𝑿subscript𝑡𝑛0𝛾𝐴subscript𝑡𝑛𝑉superscriptsubscript𝑡𝑛𝑿subscript𝑡𝑛𝛾𝐶𝛾𝑿subscript𝑡𝑛\gamma\_{n}=\Gamma(t\_{n},\bm{X}(t\_{n}))=\underset{0\leq\gamma\leq A(t\_{n})}{\arg\max}{\left\{{V(t\_{n}^{+},\bm{X}(t\_{n})\setminus\gamma)+C(\gamma,\bm{X}(t\_{n}))}\right\}}, |  | (30) |

where 𝑿​(tn)∖γ𝑿subscript𝑡𝑛𝛾\bm{X}(t\_{n})\setminus\gamma denotes the state variables 𝑿​(tn+)𝑿superscriptsubscript𝑡𝑛\bm{X}(t\_{n}^{+}) after withdrawal γ𝛾\gamma is made, given the value of the state variables 𝑿​(tn)𝑿subscript𝑡𝑛\bm{X}(t\_{n}) before the withdrawal. On the other hand, the passive policyholder follows a static strategy of pre-determined withdrawal values.
The contract value V​(0,𝑿​(0))𝑉0𝑿0V(0,\bm{X}(0)) can, thus, be computed recursively from ([9](#S2.E9 "In 2 Description of the VA Guarantee Product ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")), ([5](#S2.E5 "In 2 Description of the VA Guarantee Product ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")), ([6](#S2.E6 "In 2 Description of the VA Guarantee Product ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) ([29](#A3.E29 "In Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) and ([28](#A3.E28 "In Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")), along with the chosen strategy. These procedures are summarized in Algorithm [1](#alg1 "Algorithm 1 ‣ Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach").

Algorithm 1  Recursive computation of V​(0,𝑿​(0))𝑉0𝑿0V(0,\bm{X}(0))

1:initialize V​(T+,𝑿​(T+))=0𝑉superscript𝑇𝑿superscript𝑇0V(T^{+},\bm{X}(T^{+}))=0

2:set n=N𝑛𝑁n=N

3:while n>0𝑛0n>0 do

4:   compute the withdrawal amount γnsubscript𝛾𝑛\gamma\_{n} with the optimal strategy ([30](#A3.E30 "In Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) or a pre-determined static strategy

5:   compute V​(tn,𝑿​(tn))𝑉subscript𝑡𝑛𝑿subscript𝑡𝑛V(t\_{n},\bm{X}(t\_{n})) by applying jump condition ([29](#A3.E29 "In Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) with appropriate cash flows

6:   compute V​(tn−1+,𝑿​(tn−1+))𝑉superscriptsubscript𝑡𝑛1𝑿superscriptsubscript𝑡𝑛1V(t\_{n-1}^{+},\bm{X}(t\_{n-1}^{+})) by computing ([28](#A3.E28 "In Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) with terminal value V​(tn,𝑿​(tn))𝑉subscript𝑡𝑛𝑿subscript𝑡𝑛V(t\_{n},\bm{X}(t\_{n})) and the appropriate SDF D​(tn−1,tn)𝐷subscript𝑡𝑛1subscript𝑡𝑛D(t\_{n-1},t\_{n})

7:   set n=n−1𝑛𝑛1n=n-1

8:end while

9:return V​(0,𝑿​(0))=V​(0+,𝑿​(0+))𝑉0𝑿0𝑉superscript0𝑿superscript0V(0,\bm{X}(0))=V(0^{+},\bm{X}(0^{+}))

To evaluate ([28](#A3.E28 "In Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")), we discretize the underlying risk factors and approximate the conditional expectation in ([28](#A3.E28 "In Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach")) using a finite sum. For the BSM, the risk factor is taken as the scaled Brownian motion B​(t)t𝐵𝑡𝑡\frac{B(t)}{\sqrt{t}}. For the MMM, the risk factor is the normalized GP Y​(t)𝑌𝑡Y(t). Both risk factors have closed-form transition densities to facilitate the numerical computations.
The contract value under the dynamic strategy is bounded from below by the corresponding value from any simple strategy such as the static one. If a closed-form pricing formula for the simple strategy value is available, Algorithm [1](#alg1 "Algorithm 1 ‣ Appendix C Pricing of the VA with Guarantee ‣ Fair Pricing of Variable Annuities with Guarantees under the Benchmark Approach") can be easily modified to compute the optimal withdrawal premium on top of the suboptimal value of the simple strategy.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/1906.01320)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1906.01320)
[View original  
on arXiv](https://arxiv.org/abs/1906.01320)[►](javascript: void(0))