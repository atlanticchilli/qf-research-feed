---
authors:
- Jose Da Fonseca
- Patrick Wong
doc_id: arxiv:2602.06415v1
family_id: arxiv:2602.06415
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Joint survival annuity derivative valuation in the linear-rational Wishart
  mortality model
url_abs: http://arxiv.org/abs/2602.06415v1
url_html: https://arxiv.org/html/2602.06415v1
venue: arXiv q-fin
version: 1
year: 2026
---


José Da Fonseca
Auckland University of Technology, Business School, Department of Finance, Private Bag 92006, 1142 Auckland, New Zealand. Phone: +64 9 9219999 extn 5063. Email: jose.dafonseca@aut.ac.nz and PRISM Sorbonne EA 4101, Université Paris 1 Panthéon - Sorbonne, 17 rue de la Sorbonne, 75005 Paris, France. ORCID: 0000-0002-6882-4511
  
Patrick Wong
Monash University, Business School, Department of Econometrics and Business Statistics, Melbourne, VIC, 3800, Australia. Email: patrick.wong@monash.edu. ORCID: 0000-0002-6164-901X

###### Abstract

This study proposes a linear-rational joint survival mortality model based on the Wishart process. The Wishart process, which is a stochastic continuous matrix affine process, allows for a general dependency between the mortality intensities that are constructed to be positive. Using the linear-rational framework along with the Wishart process as state variable, we derive a closed-form expression for the joint survival annuity, as well as the guaranteed joint survival annuity option. Exploiting our parameterisation of the Wishart process, we explicit the distribution of the mortality intensities and their dependency. We provide the distribution (density and cumulative distribution) of the joint survival annuity. We also develop some polynomial expansions for the underlying state variable that lead to fast and accurate approximations for the guaranteed joint survival annuity option. These polynomial expansions also significantly simplify the implementation of the model. Overall, the linear-rational Wishart mortality model provides a flexible and unified framework for modelling and managing joint mortality risk.

JEL Classification: G12; G13; C61
  
Keywords: Dependent lives, Joint survival annuity, Mortality risk, Linear-rational Wishart model, Guaranteed annuity option

Acknowledgements: We thank Qihe Tang and Francesco Ungolo from UNSW Sydney for their useful suggestions and remarks. We also thank the participants at IME 2023, Edinburgh, United Kingdom, and Longevity 19, Amsterdam, Netherlands for their remarks. The usual caveat applies.

## 1 Introduction

In an era of increasing life expectancies, longevity products such as life annuities have become vital income sources for individuals in their retirement years. The complexities involved in modeling these products cannot be overstated, especially when dealing with multi-life contracts that introduce intricate dependencies among the insured parties. This paper presents a novel framework for modeling dependent mortality intensities and pricing longevity products, including joint survival annuities and options on these annuities. Taking into account our objectives, we use the stochastic differential equations (SDEs) framework outlined by Dahl ([2004](https://arxiv.org/html/2602.06415v1#bib.bib72 "Stochastic mortality in life insurance: Market reserves and mortality-linked insurance contracts")). This method, further explored by Biffis ([2005](https://arxiv.org/html/2602.06415v1#bib.bib73 "Affine processes for dynamic mortality and actuarial valuations")), is built on the vector affine process originally introduced by Duffie and Kan ([1996](https://arxiv.org/html/2602.06415v1#bib.bib95 "A yield-factor model of interest rates")). This framework, initially introduced for modelling a single mortality intensity, has been extended to the case of multiple annuitants/cohorts/populations in several works, see for example Jevtić et al. ([2013](https://arxiv.org/html/2602.06415v1#bib.bib43 "Mortality surface by means of continuous time cohort models")), Jevtić and Hurd ([2017](https://arxiv.org/html/2602.06415v1#bib.bib45 "The joint mortality of couples in continuous time")), Jevtić and Regis ([2019](https://arxiv.org/html/2602.06415v1#bib.bib44 "A continuous-time stochastic model for the mortality surface of multiple populations")), Zeddouk and Devolder ([2020](https://arxiv.org/html/2602.06415v1#bib.bib17 "Longevity modelling and pricing under a dependent multi-cohort framework")), Xu et al. ([2020](https://arxiv.org/html/2602.06415v1#bib.bib47 "Continuous-time multi-cohort mortality modelling with affine processes")), Huang et al. ([2022](https://arxiv.org/html/2602.06415v1#bib.bib16 "Modelling USA age-cohort mortality: A comparison of multi-factor affine mortality models")), Ungolo et al. ([2023](https://arxiv.org/html/2602.06415v1#bib.bib15 "Estimation, comparison, and projection of multifactor age–cohort affine mortality models")), Hainaut ([2023](https://arxiv.org/html/2602.06415v1#bib.bib66 "A calendar year mortality model in continuous time")) or Xu et al. ([2024](https://arxiv.org/html/2602.06415v1#bib.bib34 "Pricing longevity bond with affine-jump-diffusion multi-cohort mortality model")) to name a few. However, when it comes to pricing options on multi-annuitant products, such as a joint survival annuity, there is, to the best of our knowledge, no work available. This is largely due to an inherent difficulty in pricing from the exponential vector affine framework used in the aforementioned works.
To overcome this difficulty, we depart from the exponential vector affine literature by first using the Wishart process, an SDE with values in the space of positive definite matrices, a natural space for capturing dependencies. We also depart from this literature by using the potential approach of Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates")) to build a multi-annuitant mortality model for which the joint survival bond is a linear-rational function of the Wishart process. Thanks to this linear-rational structure, the density of the joint survival annuity can be computed using a one-dimensional integration and thus also provides us with key risk management indicators such as value at risk and expected shortfall. It also allows the exact pricing of the guaranteed joint survival annuity option (GAO), as well as fast and efficient GAO price approximations. We provide a complete model implementation that illustrates the analytical results and shows the impact of mortality dependence on the GAO.

In the framework introduced in Dahl ([2004](https://arxiv.org/html/2602.06415v1#bib.bib72 "Stochastic mortality in life insurance: Market reserves and mortality-linked insurance contracts")), the (joint) survival bond is an exponential affine function of the process and, as a consequence, the future annuity value, which is a sum of (joint) survival bonds, does not admit a known density. This presents two main problems. First, it makes exact pricing of GAOs impossible. The absence of an exact option pricing formula in mortality products and interest-rate products is well known and explained in detail in Biffis and Millossovich ([2006](https://arxiv.org/html/2602.06415v1#bib.bib26 "The fair value of guaranteed annuity options")). The second problem of the conventional approach stems from a property inherent to the vector affine process of Duffie and Kan ([1996](https://arxiv.org/html/2602.06415v1#bib.bib95 "A yield-factor model of interest rates")). Namely, the diffusion of this process must adhere to specific constraints, as detailed in Duffie et al. ([2003](https://arxiv.org/html/2602.06415v1#bib.bib42 "Affine processes and applications in finance")). When applied to model dependencies, this can result in certain correlation limitations, as illustrated by Da Fonseca et al. ([2007](https://arxiv.org/html/2602.06415v1#bib.bib70 "Option pricing when correlations are stochastic: An analytical framework")) in the context of an equity derivative. These are the two main problems with the conventional approach when it comes to pricing options on a (joint) survival annuity and modelling the dependence between mortality intensities, and our model will address both of them.

Following the potential approach of Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates")), we build a multi-annuitant mortality model for which the joint survival bond is a linear-rational function in the state variable. For the state variable, we use the Wishart process, which is a stochastic process with values in the space of positive definite matrices (i.e., covariances) that has strong analytical properties. Grasselli and Tebaldi ([2008](https://arxiv.org/html/2602.06415v1#bib.bib82 "Solvable affine term structure models")) show how to compute its moment generating function in closed form, it depends on a matrix Riccati differential equation that can be explicitly integrated (it is solvable), making the Wishart process as tractable as the Cox-Ingersoll-Ross process (i.e., the scalar square root process). The Wishart process is used in Da Fonseca et al. ([2007](https://arxiv.org/html/2602.06415v1#bib.bib70 "Option pricing when correlations are stochastic: An analytical framework")) to build a multi-asset equity model with dependent equity volatilities; in Chiarella et al. ([2014](https://arxiv.org/html/2602.06415v1#bib.bib69 "Pricing range notes within Wishart affine models")) to build a multi-factor interest rate model with correlated factors to price range notes derivatives; in Deelstra et al. ([2016](https://arxiv.org/html/2602.06415v1#bib.bib86 "The role of the dependence between mortality and interest rates when pricing guaranteed annuity options")) to model the dependence between interest rates and a (single) mortality intensity to price a GAO in the exponential affine framework; and in Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")) for modelling the dependence between interest rates and a (single) mortality intensity to price a GAO in a linear-rational framework. In all these works, the remarkable analytical properties of the Wishart process are crucial for obtaining the results. The Wishart process allows us to specify a very general dependence form between the different mortality intensities and the linear-rational structure of the model ensures that the joint survival annuity is a linear-rational function of the Wishart process. This property, combined with the analytical properties of the Wishart process, allows the calculation (up to numerical integration) of the density of the joint survival annuity and therefore the development of various risk management tools, such as value at risk or expected shortfall, which depend on this density. Furthermore, these properties also allow the calculation of the GAO in closed form, making the linear-rational Wishart model much more tractable than models based on the exponential affine modelling approach. Even if GAO pricing can be done efficiently, the properties of the Wishart process easily yield some interesting quantities, such as the moments of the joint survival annuity, which can be used to derive GAO price approximations in the spirit of Collin-Dufresne and Goldstein ([2002](https://arxiv.org/html/2602.06415v1#bib.bib64 "Pricing swaptions within an affine framework")) or Filipović et al. ([2013](https://arxiv.org/html/2602.06415v1#bib.bib65 "Density approximations for multivariate affine jump-diffusion processes")). We think these quantities could also be used to estimate the model using a method of moments. Beyond these analytical results, and to gain a better understanding of the model, we illustrate how the model works through several numerical experiments. One of them confirms how important the correlation between mortality intensities is when pricing a GAO.

The remainder of the paper is organised as follows. In Section [2](https://arxiv.org/html/2602.06415v1#S2 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") we introduce the instruments we intend to value, which includes the joint survival annuity and an option on the joint survival annuity, the guaranteed joint survival annuity option. Section [3](https://arxiv.org/html/2602.06415v1#S3 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") introduces the linear-rational Wishart mortality model. Here, we develop the necessary theory and background to work with our model and derive different properties of the model, in particular its characteristic function owing to the affine nature of the Wishart process. We also introduce the potential approach here, which is then used in Section [4](https://arxiv.org/html/2602.06415v1#S4 "4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") where we price the joint survival annuity and explicitly derive the positive mortality intensities. Section [5](https://arxiv.org/html/2602.06415v1#S5 "5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") prices the guaranteed joint survival annuity option, where we also develop three approximation approaches based on a Gaussian approximation, a spectral decomposition approach and a gamma approximation. An implementation and numerical experiments of our model are conducted in Section [6](https://arxiv.org/html/2602.06415v1#S6 "6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). Finally, we conclude and provide suggestions on further directions of research in Section [7](https://arxiv.org/html/2602.06415v1#S7 "7 Conclusion ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). The proofs of all the propositions in this work are presented in the Supplementary Appendix.

## 2 The modelling framework

Let (Ω,𝒢,(𝒢t)t,ℙ)(\Omega,\mathcal{G},(\mathcal{G}\_{t})\_{t},\mathbb{P}) denote a filtered probability space where ℙ\mathbb{P} is the historical probability measure. We define τx\tau\_{x} and τy\tau\_{y} as future lifetimes for annuitants aged xx and yy respectively. These lifetimes have corresponding stochastic intensities (μx​(t))t≥0(\mu\_{x}(t))\_{t\geq 0} and (μy​(t))t≥0(\mu\_{y}(t))\_{t\geq 0}. Referring to the annuitant aged xx as xx and aged yy as yy, and inspired by Dahl ([2004](https://arxiv.org/html/2602.06415v1#bib.bib72 "Stochastic mortality in life insurance: Market reserves and mortality-linked insurance contracts")) and Biffis ([2005](https://arxiv.org/html/2602.06415v1#bib.bib73 "Affine processes for dynamic mortality and actuarial valuations")), τx\tau\_{x} marks the initial jump-time of a 𝒢\mathcal{G}-counting process (Ntx)t≥0(N\_{t}^{x})\_{t\geq 0}, indicating if individual xx has passed away (Ntx≠0)(N\_{t}^{x}\neq 0) by time tt. Similarly, τy\tau\_{y} indicates the same for individual yy.

Drawing from Deelstra et al. ([2016](https://arxiv.org/html/2602.06415v1#bib.bib86 "The role of the dependence between mortality and interest rates when pricing guaranteed annuity options")), ℛt\mathcal{R}\_{t} and ℳt\mathcal{M}\_{t} are filtrations produced by the interest rate and joint mortality intensity processes respectively. Let ℱt:=ℛt∨ℳt\mathcal{F}\_{t}:=\mathcal{R}\_{t}\vee\mathcal{M}\_{t} be the minimal σ\sigma-algebra that contains ℛt∪ℳt\mathcal{R}\_{t}\cup\mathcal{M}\_{t}. The filtration (𝒢t)t≥0(\mathcal{G}\_{t})\_{t\geq 0} embodies the progressive information available, capturing the evolution of both state variables and whether the annuitants xx or yy have died at time tt. Hence, we set 𝒢t:=ℱt∨ℋt\mathcal{G}\_{t}:=\mathcal{F}\_{t}\vee\mathcal{H}\_{t}, where ℋt:=σ​({{τx≤s},{τy≤s}, 0≤s≤t})\mathcal{H}\_{t}:=\sigma(\{\{\tau\_{x}\leq s\},\,\{\tau\_{y}\leq s\},\,0\leq s\leq t\}) is the minimum filtration wherein τx\tau\_{x} and τy\tau\_{y} are established stopping times.

In line with Deelstra et al. ([2016](https://arxiv.org/html/2602.06415v1#bib.bib86 "The role of the dependence between mortality and interest rates when pricing guaranteed annuity options")), we posit that (Ntx,Nty)t≥0(N\_{t}^{x},N\_{t}^{y})\_{t\geq 0} operates as a two-dimensional Cox process, driven by an ℱ\mathcal{F} sub-filtration of 𝒢\mathcal{G}. This implies the following survival probability on the set {τx>t,τy>t}\{\tau\_{x}>t,\tau\_{y}>t\}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℚ​(τx>T,τy>T|𝒢t)=𝔼ℚ​[e−∫tTμx​(s)+μy​(s)​d​s|𝒢t],\displaystyle\mathbb{Q}(\tau\_{x}>T,\tau\_{y}>T|\mathcal{G}\_{t})=\mathbb{E}^{\mathbb{Q}}\left[\left.e^{-\int\_{t}^{T}\mu\_{x}(s)+\mu\_{y}(s)ds}\right|\mathcal{G}\_{t}\right], |  | (1) |

where ℚ\mathbb{Q} is a risk-neutral pricing measure equivalent to ℙ\mathbb{P}, and 𝔼ℚ[⋅|𝒢t]\mathbb{E}^{\mathbb{Q}}\left[\cdot|\mathcal{G}\_{t}\right] denotes the conditional expectation under ℚ\mathbb{Q} given 𝒢t\mathcal{G}\_{t}. Regarding the choice of ℚ\mathbb{Q}, we follow Deelstra et al. ([2016](https://arxiv.org/html/2602.06415v1#bib.bib86 "The role of the dependence between mortality and interest rates when pricing guaranteed annuity options")) and references therein and assume that it can be selected on the basis of available market data. For literature addressing the non-diversifiable aspect of mortality risk, which results in an incomplete market, refer to studies such as Dahl and Møller ([2006](https://arxiv.org/html/2602.06415v1#bib.bib130 "Valuation and hedging of life insurance liabilities with systematic mortality risk")), Bayraktar et al. ([2009](https://arxiv.org/html/2602.06415v1#bib.bib114 "Valuation of mortality risk via the instantaneous Sharpe ratio: Applications to life annuities")), Huang et al. ([2014](https://arxiv.org/html/2602.06415v1#bib.bib116 "Price bounds of mortality-linked security in incomplete insurance market")), and Ceci et al. ([2015](https://arxiv.org/html/2602.06415v1#bib.bib115 "Hedging of unit-linked life insurance contracts with unobservable mortality hazard rate via local risk-minimization")).

For completeness, we restate some well known equations in the literature. We note that since (Ntx,Nty)(N\_{t}^{x},N\_{t}^{y}) is a two-dimensional Cox process, then it follows that conditional on a particular trajectory (μx​(t),μy​(t))t≥0(\mu\_{x}(t),\mu\_{y}(t))\_{t\geq 0} the process (Ntx,Nty)t≥0(N\_{t}^{x},N\_{t}^{y})\_{t\geq 0} is a two-dimensional independent Poisson-inhomogeneous process with parameter (∫0tμx​(s)​𝑑s)t≥0(\int\_{0}^{t}\mu\_{x}(s)ds)\_{t\geq 0} for (Ntx)t≥0(N\_{t}^{x})\_{t\geq 0} and (∫0tμy​(s)​𝑑s)t≥0(\int\_{0}^{t}\mu\_{y}(s)ds)\_{t\geq 0} for (Nty)t≥0(N\_{t}^{y})\_{t\geq 0}. As such, for all t1≥t≥0t\_{1}\geq t\geq 0 and t2≥t≥0t\_{2}\geq t\geq 0 and nonnegative integers k1k\_{1}, k2k\_{2}, the following equality holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(k1,k2):=\displaystyle I(k\_{1},k\_{2}):= | ℚ​((Nt1x−Ntx=k1)​(Nt2y−Nty=k2)|ℋt∨ℱ∞)\displaystyle\,\mathbb{Q}((N\_{t\_{1}}^{x}-N\_{t}^{x}=k\_{1})(N\_{t\_{2}}^{y}-N\_{t}^{y}=k\_{2})|\mathcal{H}\_{t}\vee\mathcal{F}\_{\infty}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ℚ​((Nt1x−Ntx=k1)|ℋt∨ℱ∞)​ℚ​((Nt2y−Nty=k2)|ℋt∨ℱ∞)\displaystyle\,\mathbb{Q}((N\_{t\_{1}}^{x}-N\_{t}^{x}=k\_{1})|\mathcal{H}\_{t}\vee\mathcal{F}\_{\infty})\mathbb{Q}((N\_{t\_{2}}^{y}-N\_{t}^{y}=k\_{2})|\mathcal{H}\_{t}\vee\mathcal{F}\_{\infty}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (∫tt1μx​(s)​𝑑s)k1k1!​e−∫tt1μx​(s)​𝑑s​(∫tt2μy​(s)​𝑑s)k2k2!​e−∫tt2μy​(s)​𝑑s,\displaystyle\,\frac{\left(\int\_{t}^{t\_{1}}\mu\_{x}(s)ds\right)^{k\_{1}}}{k\_{1}!}e^{-\int\_{t}^{t\_{1}}\mu\_{x}(s)ds}\frac{\left(\int\_{t}^{t\_{2}}\mu\_{y}(s)ds\right)^{k\_{2}}}{k\_{2}!}e^{-\int\_{t}^{t\_{2}}\mu\_{y}(s)ds}, |  |

where we used the conditional independence between (Ntx)t≥0(N\_{t}^{x})\_{t\geq 0} and (Nty)t≥0(N\_{t}^{y})\_{t\geq 0}. Taking k1=0k\_{1}=0, k2=0k\_{2}=0 and integrating the intensities lead to ([1](https://arxiv.org/html/2602.06415v1#S2.E1 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")).

Still following the literature, see for example Dahl ([2004](https://arxiv.org/html/2602.06415v1#bib.bib72 "Stochastic mortality in life insurance: Market reserves and mortality-linked insurance contracts"), Sec. (3.4)) and Biffis ([2005](https://arxiv.org/html/2602.06415v1#bib.bib73 "Affine processes for dynamic mortality and actuarial valuations"), Eq. (10)), the 𝒢t\mathcal{G}\_{t}-conditional density of (τx,τy)(\tau\_{x},\tau\_{y}) on the set {τx>t,τy>t}\{\tau\_{x}>t,\tau\_{y}>t\}, denoted ft​(t1,t2)f\_{t}(t\_{1},t\_{2}), is given by ft​(t1,t2)=∂t1​t22ℚ​((τx>t1)​(τy>t2)|𝒢t)f\_{t}(t\_{1},t\_{2})=\partial^{2}\_{t\_{1}t\_{2}}\mathbb{Q}((\tau\_{x}>t\_{1})(\tau\_{y}>t\_{2})|\mathcal{G}\_{t}).
Note that nothing so far was said on the intensities (μx​(t),μy​(t))t≥0(\mu\_{x}(t),\mu\_{y}(t))\_{t\geq 0} apart from the fact that they have to be positive. If they are dependent, then there is a dependency between the mortality intensities even if conditionally on the intensities (Ntx)t≥0(N\_{t}^{x})\_{t\geq 0} and (Nty)t≥0(N\_{t}^{y})\_{t\geq 0} are independent. It is through the intensities that we can incorporate a dependency between the mortality events τx\tau\_{x} and τy\tau\_{y}.

Assuming 0≤t≤T0\leq t\leq T, then the pricing at time tt of an insurance contingent claim payable at TT paying 11 on the survival of annuitants aged xx and yy at time 0 is given on the set {τx>t,τy>t}\{\tau\_{x}>t,\tau\_{y}>t\} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | SB​(t,T):=𝔼ℚ​[e−∫tTr​(s)​𝑑s​𝟏{τx>T}​𝟏{τy>T}|𝒢t],\displaystyle\mathrm{SB}(t,T):=\mathbb{E}^{\mathbb{Q}}\left[\left.e^{-\int\_{t}^{T}r(s)ds}\mathbf{1}\_{\{\tau\_{x}>T\}}\mathbf{1}\_{\{\tau\_{y}>T\}}\right|\mathcal{G}\_{t}\right], |  | (2) |

where (r​(t))t≥0(r(t))\_{t\geq 0} is the risk free rate which is adapted to the filtration (ℱt)t≥0\left(\mathcal{F}\_{t}\right)\_{t\geq 0}. This instrument is commonly called the joint survival zero coupon bond. At this stage it is required to specify whether the risk free rate (r​(t))t≥0(r(t))\_{t\geq 0} depends on the mortality intensities (μx​(t),μy​(t))t≥0(\mu\_{x}(t),\mu\_{y}(t))\_{t\geq 0}. We follow the literature and assume that interest rates and the mortality risks are independent from each other, see for example Biffis ([2005](https://arxiv.org/html/2602.06415v1#bib.bib73 "Affine processes for dynamic mortality and actuarial valuations")).111We acknowledge the strand in the SDE framework literature that correlates interest rates and mortality risk. See for example Deelstra et al. ([2016](https://arxiv.org/html/2602.06415v1#bib.bib86 "The role of the dependence between mortality and interest rates when pricing guaranteed annuity options")) and Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")) for works that use the Wishart process to handle that dependence.

Furthermore, using ([1](https://arxiv.org/html/2602.06415v1#S2.E1 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) as well as the fact that the conditioning on 𝒢t\mathcal{G}\_{t} can be reduced to that on ℱt\mathcal{F}\_{t} as shown in Biffis ([2005](https://arxiv.org/html/2602.06415v1#bib.bib73 "Affine processes for dynamic mortality and actuarial valuations"), Appendix C), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | SB​(t,T)=𝟏{τx>t,τy>t}​P​(t,T)​𝔼ℚ​[e−∫tTμx​(s)+μy​(s)​d​s|ℱt],\displaystyle\mathrm{SB}(t,T)=\mathbf{1}\_{\{\tau\_{x}>t,\tau\_{y}>t\}}P(t,T)\mathbb{E}^{\mathbb{Q}}\left[\left.e^{-\int\_{t}^{T}\mu\_{x}(s)+\mu\_{y}(s)ds}\right|\mathcal{F}\_{t}\right], |  | (3) |

with P​(t,T)P(t,T) the time tt-value of a zero-coupon bond with maturity TT. Hereafter, 𝔼ℚ[⋅|ℱt]\mathbb{E}^{\mathbb{Q}}\left[\cdot|\mathcal{F}\_{t}\right] will be denoted 𝔼tℚ​[⋅]\mathbb{E}\_{t}^{\mathbb{Q}}\left[\cdot\right], so that the joint survival (zero-coupon) bond, denoted by SB​(t,T)\mathrm{SB}(t,T), is eventually given on the set {τx>t,τy>t}\{\tau\_{x}>t,\tau\_{y}>t\} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | SB​(t,T)\displaystyle\mathrm{SB}(t,T) | =P​(t,T)​𝔼tℚ​[e−∫tTμx​(s)+μy​(s)​d​s]\displaystyle=P(t,T)\mathbb{E}\_{t}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}\mu\_{x}(s)+\mu\_{y}(s)ds}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =P​(t,T)​SB0​(t,T),\displaystyle=P(t,T)\mathrm{SB}\_{0}(t,T), |  | (4) |

where we use SB0​(⋅,⋅)\mathrm{SB}\_{0}(\cdot,\cdot) to denote the joint survival bond that contains no interest rate risk. The equivalent actuarial notation is given by px​yT{}\_{T}p\_{xy}, however, due to the similarities of our work with Biffis ([2005](https://arxiv.org/html/2602.06415v1#bib.bib73 "Affine processes for dynamic mortality and actuarial valuations")) and Deelstra et al. ([2016](https://arxiv.org/html/2602.06415v1#bib.bib86 "The role of the dependence between mortality and interest rates when pricing guaranteed annuity options")), we instead follow their notation.

Using the framework introduced so far, the joint life annuity is therefore the sum of joint survival bonds, i.e., a product that pays at certain pre-specified dates an amount (possibly date dependent), conditional on the survival of both annuitants at those dates. Let T1,…,TNT\_{1},\ldots,T\_{N} be a set of yearly spaced dates such that TN=min⁡(x∗−x−1,y∗−y−1)T\_{N}=\min(x^{\*}-x-1,y^{\*}-y-1) with x∗x^{\*} and y∗y^{\*} being the maximum attainable age for the annuitants xx and yy respectively. Consider the product that pays at times TiT\_{i} the amount 11 conditional on the survival of both annuitants, the value of the product at time tt is given on the set {τx>t,τy>t}\{\tau\_{x}>t,\tau\_{y}>t\} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1NSB​(t,Ti),\displaystyle\sum\_{i=1}^{N}\mathrm{SB}(t,T\_{i}), |  | (5) |

with SB​(t,T)\mathrm{SB}(t,T) given by ([4](https://arxiv.org/html/2602.06415v1#S2.E4 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")).

Another product of interest is the guaranteed joint survival annuity option, i.e., an option on ([5](https://arxiv.org/html/2602.06415v1#S2.E5 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). We follow Deelstra et al. ([2016](https://arxiv.org/html/2602.06415v1#bib.bib86 "The role of the dependence between mortality and interest rates when pricing guaranteed annuity options"), Section 3.2), who analyse the guaranteed survival annuity option (for a single annuitant), but consider the case of multiple annuitants. Suppose a guaranteed joint survival annuity option with maturity TT and consider a set of yearly spaced dates T1,…,TNT\_{1},\ldots,T\_{N} such that T1=T+1T\_{1}=T+1 (where the units are years) and TN=min⁡(x∗−(x+T)−1,y∗−(y+T)−1)T\_{N}=\min(x^{\*}-(x+T)-1,y^{\*}-(y+T)-1) with x∗x^{\*} and y∗y^{\*} again being the maximum attainable age for annuitants xx and yy respectively. Then we denote the value of a guaranteed joint survival annuity option at time tt, exercisable at TT, on a joint survival annuity paying at times T1,…,TNT\_{1},...,T\_{N} as C​(t,T,TN)C(t,T,T\_{N}). Thus at t=Tt=T, the payoff of the option is given on the set {τx>T,τy>T}\{\tau\_{x}>T,\tau\_{y}>T\} by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C​(t=T,T,TN)\displaystyle C(t=T,T,T\_{N}) | :=max⁡(g​∑i=1NSB​(T,Ti),1)=1+g​C¯​(T,T,TN),\displaystyle:=\max\left(g\sum\_{i=1}^{N}\mathrm{SB}(T,T\_{i}),1\right)=1+g\bar{C}(T,T,T\_{N}), |  | (6) |

where gg is the fixed rate called the guaranteed joint survival annuity rate and (z)+=max⁡(z,0)(z)\_{+}=\max(z,0) and C¯​(T,T,TN)=(∑i=1NSB​(T,Ti)−1/g)+\bar{C}(T,T,T\_{N})=\left(\sum\_{i=1}^{N}\mathrm{SB}(T,T\_{i})-1/g\right)\_{+}. Therefore, the guaranteed joint survival annuity option value at time tt is given on the set {τx>t,τy>t}\{\tau\_{x}>t,\tau\_{y}>t\} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(t,T,TN)\displaystyle C(t,T,T\_{N}) | =P​(t,T)​SB0​(t,T)+g​𝔼tℚ​[e−∫tT(r​(s)+μx​(s)+μy​(s))​𝑑s​C¯​(T,T,TN)],\displaystyle=P(t,T)\mathrm{SB}\_{0}(t,T)+g\mathbb{E}\_{t}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}(r(s)+\mu\_{x}(s)+\mu\_{y}(s))ds}\bar{C}(T,T,T\_{N})\right], |  |

with C¯​(t,T,TN)\bar{C}(t,T,T\_{N}) the expectation on the right hand side above.
It is worth having a closer look at the expression of C¯​(t,T,TN)\bar{C}(t,T,T\_{N}) as it highlights some modelling issues. Using ([4](https://arxiv.org/html/2602.06415v1#S2.E4 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), we obtain on the set {τx>t,τy>t}\{\tau\_{x}>t,\tau\_{y}>t\} the equality

|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯​(t,T,TN)=𝔼tℚ​[e−∫tT(r​(s)+μx​(s)+μy​(s))​𝑑s​(∑i=1NP​(T,Ti)​SB0​(T,Ti)−1/g)+],\displaystyle\bar{C}(t,T,T\_{N})=\mathbb{E}\_{t}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}(r(s)+\mu\_{x}(s)+\mu\_{y}(s))ds}\left(\sum\_{i=1}^{N}P(T,T\_{i})\mathrm{SB}\_{0}(T,T\_{i})-1/g\right)\_{+}\right], |  | (7) |

where we can clearly see that even if the interest rate is independent with respect to the mortality intensities, its distribution impacts the option price. Given the difficulty of treating stochastic interest rates, independent or dependent of the mortality intensities, we take the interest rate to be deterministic.

Let us stress the fact that all of the equations stated above are model independent, and are not contingent on using any specific model or process.

As seen from ([7](https://arxiv.org/html/2602.06415v1#S2.E7 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), the pricing of a guaranteed (joint) annuity option is a difficult task, as it requires the law of the sum of joint survival (zero coupon) bonds. If the joint survival bond is an exponential function of the state variable, then this amounts to requiring the law of the sum of exponentials of random variables that is in general unknown. This difficulty is well explained in Biffis and Millossovich ([2006](https://arxiv.org/html/2602.06415v1#bib.bib26 "The fair value of guaranteed annuity options")) and is one of the main difficulties we need to overcome.

## 3 The linear-rational Wishart model

To build the joint mortality model we use the Wishart process defined in Bru ([1991](https://arxiv.org/html/2602.06415v1#bib.bib81 "Wishart processes")) and introduce its main properties. In the following section, we provide a concise review of the essential techniques and findings required to construct our model. This presentation is prompted by the relatively novel application of the Wishart process in mortality modeling. Given a filtered probability space (Ω,ℱ,(ℱt)t,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t},\mathbb{P}) we denote by 𝔼​[⋅]\mathbb{E}\left[\,\cdot\,\right] (resp. 𝔼t[⋅]:=𝔼[⋅|ℱt]\mathbb{E}\_{t}\left[\,\cdot\,\right]:=\mathbb{E}\left[\,\cdot\,|\mathcal{F}\_{t}\right]) the expectation (resp. conditional expectation) under the historical probability measure ℙ\mathbb{P}. The Wishart process satisfies the matrix SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​vt=(ω+m​vt+vt​m⊤)​d​t+vt​d​wt​σ+σ⊤​d​wt⊤​vt,dv\_{t}=(\omega+mv\_{t}+v\_{t}m^{\top})dt+\sqrt{v\_{t}}dw\_{t}\sigma+\sigma^{\top}dw\_{t}^{\top}\sqrt{v\_{t}}\,, |  | (8) |

where vtv\_{t} is an n×nn\times n matrix that belongs to the set of positive definite matrices denoted 𝕊n++\mathbb{S}\_{n}^{++}, m,σm,\sigma belong to the set of n×nn\times n real matrices denoted 𝖬​(n)\mathsf{M}(n), {wt;t≥0}\{w\_{t};t\geq 0\} is a matrix Brownian motion of dimension n×nn\times n (i.e., a matrix of n2n^{2} independent scalar Brownian motions) under the probability measure ℙ\mathbb{P} and ⋅⊤\cdot^{\top} stands for the matrix transposition. The matrix ω∈𝕊n++\omega\in\mathbb{S}\_{n}^{++} satisfies certain constraints involving σ⊤​σ\sigma^{\top}\sigma to ensure the positive-definiteness of the matrix process vtv\_{t}. The quantity vt\sqrt{v\_{t}} is well defined since vt∈𝕊n++v\_{t}\in\mathbb{S}\_{n}^{++}.
The matrix mm is such that {ℜ⁡(λim)<0;i=1,…,n}\{\Re(\lambda\_{i}^{m})<0;i=1,\ldots,n\} where λim∈𝖲𝗉𝖾𝖼​(m)\lambda\_{i}^{m}\in\mathsf{Spec}(m) for i=1,…,ni=1,\ldots,n and 𝖲𝗉𝖾𝖼​(m)\mathsf{Spec}(m) is the spectrum of the matrix mm, while ℜ⁡(⋅)\Re(\,\cdot\,) denotes the real component.
The matrix σ\sigma belongs to 𝖦𝖫n​(ℝ)\mathsf{GL}\_{n}(\mathbb{R}) the general linear group over ℝ\mathbb{R} (i.e., the set of real invertible matrices). Due to the invariance of the law of the Brownian motion with respect to rotations and the polar decomposition of σ\sigma, we can assume that σ∈𝕊n++\sigma\in\mathbb{S}\_{n}^{++}. We denote ei​je\_{ij} to be the basis of 𝖬​(n)\mathsf{M}(n), i.e., it is the n×nn\times n matrix with 11 in the (i,j)(i,j) place and zero elsewhere. Lastly InI\_{n} stands for the n×nn\times n identity matrix, 0n0\_{n} is the n×nn\times n null matrix while diag​(z)\textup{diag}(z) with z∈ℝnz\in\mathbb{R}^{n} is the n×nn\times n matrix with zz on its diagonal. The infinitesimal generator of the Wishart process is given by Bru ([1991](https://arxiv.org/html/2602.06415v1#bib.bib81 "Wishart processes")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=tr​[(ω+m​v+v​m⊤)​D+2​v​D​σ2​D],\displaystyle\mathcal{L}=\textup{tr}[(\omega+mv+vm^{\top})D+2vD\sigma^{2}D]\,, |  | (9) |

where tr​[⋅]\textup{tr}[\,\cdot\,] is the trace of a matrix and DD is the n×nn\times n matrix operator Di​j:=∂vi​jD\_{ij}:=\partial\_{v\_{ij}}.

The Wishart process was initially defined and analysed in Bru ([1991](https://arxiv.org/html/2602.06415v1#bib.bib81 "Wishart processes")) under the assumption that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ω=β​σ2\omega=\beta\sigma^{2} |  | (10) |

with β∈ℝ+\beta\in\mathbb{R}\_{+} such that β≥n+1\beta\geq n+1 to ensure that vt∈𝕊n++v\_{t}\in\mathbb{S}\_{n}^{++}. Hereafter, this specification will be referred to as the Bru case. It was later extended in Mayerhofer et al. ([2011](https://arxiv.org/html/2602.06415v1#bib.bib85 "On strong solutions of positive definite jump-diffusions")) (see also Cuchiero et al., [2011](https://arxiv.org/html/2602.06415v1#bib.bib84 "Affine processes on positive semidefinite matrices")) to the case ω∈𝕊n++\omega\in\mathbb{S}\_{n}^{++} and proved that if

|  |  |  |  |
| --- | --- | --- | --- |
|  | ω−β​σ2∈𝕊n++,\displaystyle\omega-\beta\sigma^{2}\in\mathbb{S}\_{n}^{++}, |  | (11) |

with β≥n+1\beta\geq n+1 then vt∈𝕊n++v\_{t}\in\mathbb{S}\_{n}^{++}.

In our work, we deliberately restrict ourselves to the Bru case, (i.e., ω=β​σ2\omega=\beta\sigma^{2}).
The advantage of the Bru case is that moment generating function can be explicitly integrated making it fully explicit. This allows us to derive analytic formulae surrounding the guaranteed joint survival annuity option and the individual mortalities in contrast to the work of Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")) which is not in the Bru case. The below result is well known. We refer to Bru ([1991](https://arxiv.org/html/2602.06415v1#bib.bib81 "Wishart processes")) or Grasselli and Tebaldi ([2008](https://arxiv.org/html/2602.06415v1#bib.bib82 "Solvable affine term structure models")) (see also Alfonsi, [2015](https://arxiv.org/html/2602.06415v1#bib.bib30 "Affine diffusions and related processes: simulation, theory and applications"), Chap. 5).222Following the introduction of the Wishart process in finance by Gouriéroux and Sufana ([2010](https://arxiv.org/html/2602.06415v1#bib.bib104 "Derivative pricing with multivariate stochastic volatility")), applications have been developed in equity and foreign exchange derivatives (see Da Fonseca et al. ([2007](https://arxiv.org/html/2602.06415v1#bib.bib70 "Option pricing when correlations are stochastic: An analytical framework")), Leung et al. ([2013](https://arxiv.org/html/2602.06415v1#bib.bib8 "Currency option pricing with Wishart process")), Gnoatto and Grasselli ([2014](https://arxiv.org/html/2602.06415v1#bib.bib7 "The explicit laplace transform for the Wishart process")), La Bua and Marazzina ([2022](https://arxiv.org/html/2602.06415v1#bib.bib9 "A new class of multidimensional Wishart-based hybrid models")), and Faraz et al. ([2025](https://arxiv.org/html/2602.06415v1#bib.bib3 "Markov-modulated and shifted Wishart processes with applications in derivatives pricing"))); in interest rate derivatives (see Gouriéroux and Sufana ([2011](https://arxiv.org/html/2602.06415v1#bib.bib5 "Discrete time Wishart term structure models")), Gnoatto ([2012](https://arxiv.org/html/2602.06415v1#bib.bib10 "The Wishart short rate model")), and Cuchiero et al. ([2019](https://arxiv.org/html/2602.06415v1#bib.bib11 "Affine multiple yield curve models"))); and in optimal portfolio choice (see Bäuerle and Li ([2013](https://arxiv.org/html/2602.06415v1#bib.bib33 "Optimal portfolios for financial markets with Wishart volatility")) and Branger et al. ([2017](https://arxiv.org/html/2602.06415v1#bib.bib103 "Optimal portfolios when variances and covariances can jump"))), to name just a few works across these fields. In all these studies, the general dependency structure among the components of the Wishart process, along with its strong analytical properties, plays a crucial modelling role.

###### Proposition 3.1.

Suppose that ω\omega in ([8](https://arxiv.org/html/2602.06415v1#S3.E8 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) is such that ω=β​σ2\omega=\beta\sigma^{2} with β∈ℝ\beta\in\mathbb{R} and β≥n+1\beta\geq n+1 then the moment generating function of vtv\_{t} for θ1∈𝕊n\theta\_{1}\in\mathbb{S}\_{n} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ​(t,θ1,v0)\displaystyle\Phi(t,\theta\_{1},v\_{0}) | =𝔼​[exp⁡(tr​[θ1​vt])]\displaystyle=\mathbb{E}\left[\exp\left(\textup{tr}[\theta\_{1}v\_{t}]\right)\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =etr​(ϑt⊤2​(2​ςt​θ1)​(In−2​ςt​θ1)−1)det(In−2​ςt​θ1)β/2,\displaystyle=\frac{\textup{etr}\left(\frac{\vartheta\_{t}^{\top}}{2}(2\varsigma\_{t}\theta\_{1})(I\_{n}-2\varsigma\_{t}\theta\_{1})^{-1}\right)}{\det(I\_{n}-2\varsigma\_{t}\theta\_{1})^{\beta/2}}, |  | (12) |

with ςt:=∫0te(t−s)​m​σ2​e(t−s)​m⊤​𝑑s\varsigma\_{t}:=\int\_{0}^{t}e^{(t-s)m}\sigma^{2}e^{(t-s)m^{\top}}ds, which is given by vec​(ςt)=𝖠−1​(e𝖠​t−In2)​vec​(σ2)\textup{vec}(\varsigma\_{t})=\mathsf{A}^{-1}(e^{\mathsf{A}t}-I\_{n^{2}})\textup{vec}(\sigma^{2}), ϑt:=ςt−1​em​t​v0​em⊤​t\vartheta\_{t}:=\varsigma\_{t}^{-1}e^{mt}v\_{0}e^{m^{\top}t}, etr​(⋅)=exp⁡(tr​[⋅])\textup{etr}(\cdot)=\exp(\textup{tr}[\cdot]) and det(⋅)\det(\cdot) the determinant of a matrix. Here vec​(⋅)\textup{vec}\left(\,\cdot\,\right) denotes the vec operator that transforms a n×nn\times n matrix into a n2n^{2} vector by stacking the columns, 𝖠:=In⊗m+m⊗In\mathsf{A}:=I\_{n}\otimes m+m\otimes I\_{n}, and ⊗\otimes denotes the Kronecker product.

The Wishart process is affine, that is the moment generating function is exponentially affine in the state variable. The equation ([12](https://arxiv.org/html/2602.06415v1#S3.E12 "In Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) is the moment generating function of a non-central Wishart distribution, hence the name of the process, and the corresponding density is given in Gupta and Nagar ([2000](https://arxiv.org/html/2602.06415v1#bib.bib127 "Matrix variate distributions"), Eq. 3.5.1 p. 114). Note that even if the density is known, computing an expectation requires to perform a n​(n+1)/2n(n+1)/2 dimensional numerical integration.

###### Remark 3.2.

Let us stress the fact that when ω≠β​σ2\omega\neq\beta\sigma^{2}, then the moment generating function of vtv\_{t} is unknown, and in particular it is not a Wishart distribution. In this case the name of the process is misleading. The analytic results derived in Section [4](https://arxiv.org/html/2602.06415v1#S4 "4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") and Section [5](https://arxiv.org/html/2602.06415v1#S5 "5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") makes use of this explicit moment generating function, which are not possible to be derived in the setting of Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")).

The results developed in this work rely on the following result, which arises from solving Lyapunov equations after rewriting the dynamics of the Wishart process. This fact is well known in the matrix Riccati literature, see for example Abou‐Kandil2003MatrixRiccati.

###### Lemma 3.3.

Let vtv\_{t} be a Wishart process described by ([8](https://arxiv.org/html/2602.06415v1#S3.E8 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). If u0∈𝖬​(n)u\_{0}\in\mathsf{M}(n), then there exist a function b0​(t)b\_{0}(t) and a matrix function a0​(t)∈𝖬​(n)a\_{0}(t)\in\mathsf{M}(n) such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[tr​[u0​vt]]\displaystyle\mathbb{E}\left[\textup{tr}[u\_{0}v\_{t}]\right] | =tr​[a0​(t)​v0]+b0​(t),\displaystyle=\textup{tr}[a\_{0}(t)v\_{0}]+b\_{0}(t), |  | (13) |

with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vec​(a0​(t)⊤)\displaystyle\textup{vec}\left(a\_{0}(t)^{\top}\right) | =e𝖠⊤​t​vec​(u0⊤),\displaystyle=e^{\mathsf{A}^{\top}t}\textup{vec}(u\_{0}^{\top}), |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | b0​(t)\displaystyle b\_{0}(t) | =vec​(u0⊤)⊤​𝖠−1​(e𝖠​t−In2)​𝖻.\displaystyle=\textup{vec}(u\_{0}^{\top})^{\top}\mathsf{A}^{-1}\left(e^{\mathsf{A}t}-I\_{n^{2}}\right)\mathsf{b}. |  | (15) |

Here 𝖻:=vec​(ω)\mathsf{b}:=\textup{vec}\left(\omega\right), 𝖠:=In⊗m+m⊗In\mathsf{A}:=I\_{n}\otimes m+m\otimes I\_{n}, and ⊗\otimes denotes the Kronecker product.

The following proposition is well known in the literature and is useful for obtaining the quadratic variation of linear functions of the Wishart process, which in turn will be utilised to derive the covariation (or instantaneous correlation) between mortality intensities. A proof of the proposition appears in p. 214 of Deelstra et al. ([2016](https://arxiv.org/html/2602.06415v1#bib.bib86 "The role of the dependence between mortality and interest rates when pricing guaranteed annuity options")) and reads as follows.

###### Proposition 3.4.

Given h1,h2∈𝖬​(n)h\_{1},h\_{2}\in\mathsf{M}(n) the quadratic variation between (tr​[h1​vt])t≥0(\textup{tr}[h\_{1}v\_{t}])\_{t\geq 0} and (tr​[h2​vt])t≥0(\textup{tr}[h\_{2}v\_{t}])\_{t\geq 0} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​⟨tr​[h1​v.],tr​[h2​v.]⟩t\displaystyle d\langle\textup{tr}[h\_{1}v\_{.}],\textup{tr}[h\_{2}v\_{.}]\rangle\_{t} | =tr​[(h1+h1⊤)​vt​(h2+h2⊤)​σ2]​d​t.\displaystyle=\textup{tr}[(h\_{1}+h\_{1}^{\top})v\_{t}(h\_{2}+h\_{2}^{\top})\sigma^{2}]dt\,. |  |

When n=2n=2, using Proposition [3.4](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), one can in particular show that the quadratic covariation between v11,tv\_{11,t} and v22,tv\_{22,t} is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​⟨v11,.,v22,.⟩t\displaystyle d\langle v\_{11,.},v\_{22,.}\rangle\_{t} | =4​v12,t​(σ2)12​d​t,\displaystyle=4v\_{12,t}(\sigma^{2})\_{12}dt, |  | (16) |

where (σ2)i​j(\sigma^{2})\_{ij} is the (i,j)(i,j) element of the matrix σ2\sigma^{2}. Note that (σ2)12=0(\sigma^{2})\_{12}=0 if σ12=0\sigma\_{12}=0, which means the dependence between v11,tv\_{11,t} and v22,tv\_{22,t} is primarily dependent on σ12\sigma\_{12}.

To obtain the derivative of the moment generating function with respect to a parameter, the next proposition provides the details in the Bru case. This result will be particularly helpful for obtaining the densities of mortality intensities, as well as risk measures such as expected shortfall and value at risk for joint survival annuities.

###### Proposition 3.5.

Suppose that ω\omega in ([8](https://arxiv.org/html/2602.06415v1#S3.E8 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) is such that ω=β​σ2\omega=\beta\sigma^{2} with β∈ℝ\beta\in\mathbb{R} and β≥n+1\beta\geq n+1 and consider the moment generating function of vtv\_{t} given by ([12](https://arxiv.org/html/2602.06415v1#S3.E12 "In Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). For θ1∈𝕊n\theta\_{1}\in\mathbb{S}\_{n} and θ2∈𝕊n\theta\_{2}\in\mathbb{S}\_{n} consider the function for ν∈ℝ\nu\in\mathbb{R}, ν→Φ​(t,θ1+ν​θ2,v0)=𝔼​[etr​((θ1+ν​θ2)​vt)]\nu\to\Phi(t,\theta\_{1}+\nu\theta\_{2},v\_{0})=\mathbb{E}\left[\textup{etr}\left((\theta\_{1}+\nu\theta\_{2})v\_{t}\right)\right] then its derivative with respect to ν\nu is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φν​(t,θ1,θ2,ν,v0)\displaystyle\Phi\_{\nu}(t,\theta\_{1},\theta\_{2},\nu,v\_{0}) | :=d​Φ​(t,θ1+ν​θ2,v0)d​ν\displaystyle:=\frac{d\Phi(t,\theta\_{1}+\nu\theta\_{2},v\_{0})}{d\nu} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(g1+g2+g3)​Φ​(t,θ1+ν​θ2,v0),\displaystyle=(g\_{1}+g\_{2}+g\_{3})\Phi(t,\theta\_{1}+\nu\theta\_{2},v\_{0}), |  | (17) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | g1​(t,θ1,θ2,ν)\displaystyle g\_{1}(t,\theta\_{1},\theta\_{2},\nu) | =tr​[ϑt⊤2​2​ςt​θ2​(In−2​ςt​(θ1+ν​θ2))−1],\displaystyle=\textup{tr}\left[\frac{\vartheta\_{t}^{\top}}{2}2\varsigma\_{t}\theta\_{2}(I\_{n}-2\varsigma\_{t}(\theta\_{1}+\nu\theta\_{2}))^{-1}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g2​(t,θ1,θ2,ν)\displaystyle g\_{2}(t,\theta\_{1},\theta\_{2},\nu) | =tr​[ϑt⊤2​2​ςt​(θ1+ν​θ2)​(In−2​ςt​(θ1+ν​θ2))−1​2​ςt​θ2​(In−2​ςt​(θ1+ν​θ2))−1],\displaystyle=\textup{tr}\left[\frac{\vartheta\_{t}^{\top}}{2}2\varsigma\_{t}(\theta\_{1}+\nu\theta\_{2})(I\_{n}-2\varsigma\_{t}(\theta\_{1}+\nu\theta\_{2}))^{-1}2\varsigma\_{t}\theta\_{2}(I\_{n}-2\varsigma\_{t}(\theta\_{1}+\nu\theta\_{2}))^{-1}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g3​(t,θ1,θ2,ν)\displaystyle g\_{3}(t,\theta\_{1},\theta\_{2},\nu) | =β2​tr​[2​ςt​θ2​(In−2​ςt​(θ1+ν​θ2))−1],\displaystyle=\frac{\beta}{2}\textup{tr}\left[2\varsigma\_{t}\theta\_{2}(I\_{n}-2\varsigma\_{t}(\theta\_{1}+\nu\theta\_{2}))^{-1}\right], |  |

and ςt\varsigma\_{t} and ϑt\vartheta\_{t} as in Proposition [3.1](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

We build on the potential approach proposed by Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates")) whose main idea is to directly specify the state-price density in ([4](https://arxiv.org/html/2602.06415v1#S2.E4 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) so that the corresponding instantaneous mortality intensities are positive.333The potential approach of Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates")) is well documented in standard textbooks (see, for example, Björk ([2009](https://arxiv.org/html/2602.06415v1#bib.bib123 "Arbitrage theory in continuous time")) and Cairns ([2004](https://arxiv.org/html/2602.06415v1#bib.bib24 "Interest rate models: an introduction"))) and has been used in several interest rate derivatives studies (see, for example, Crépey et al. ([2015](https://arxiv.org/html/2602.06415v1#bib.bib101 "Rational multi-curve models with counterparty-risk valuation adjustments")), Nguyen and Seifried ([2015](https://arxiv.org/html/2602.06415v1#bib.bib49 "The multi-curve potential model")), Filipović et al. ([2017](https://arxiv.org/html/2602.06415v1#bib.bib36 "Linear-rational term structure models")) or Nguyen and Seifried ([2021](https://arxiv.org/html/2602.06415v1#bib.bib100 "The affine rational potential model"))). When combined with a Wishart process, it has proved particularly effective in the multi-curve setting of Da Fonseca et al. ([2022](https://arxiv.org/html/2602.06415v1#bib.bib51 "A linear-rational multi-curve term structure model with stochastic spread")) and in a cross-asset context in Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")). We believe the framework still offers many modelling possibilities, including for mortality derivatives and credit risk derivatives. For example, De Giovanni et al. ([2025](https://arxiv.org/html/2602.06415v1#bib.bib1 "Joint mortality models based on subordinated linear hypercubes")) recently proposed a model that departs from the traditional modelling approach of Dahl ([2004](https://arxiv.org/html/2602.06415v1#bib.bib72 "Stochastic mortality in life insurance: Market reserves and mortality-linked insurance contracts")) and Biffis ([2005](https://arxiv.org/html/2602.06415v1#bib.bib73 "Affine processes for dynamic mortality and actuarial valuations")). However, their model differs from ours primarily in the way the state-price density is defined.  The standard approach proceeds the other way around, i.e., to specify the mortality intensities and deduce the state-price density. We briefly summarise the mathematical framework as well as develop our main results on mortality modelling.

First, we define the state-price density as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ζt\displaystyle\zeta\_{t} | :=e−α​t​(1+tr​[u0​vt]),\displaystyle:=e^{-\alpha t}(1+\textup{tr}[u\_{0}v\_{t}])\,, |  | (18) |

with α∈ℝ+\alpha\in\mathbb{R}\_{+}, u0=u1+u2u\_{0}=u\_{1}+u\_{2} with u1∈𝕊n+u\_{1}\in\mathbb{S}\_{n}^{+} (the set of positive semi-definite matrices) and u2∈𝕊n+u\_{2}\in\mathbb{S}\_{n}^{+} (so that u0∈𝕊n+u\_{0}\in\mathbb{S}\_{n}^{+}) and (vt)t≥0(v\_{t})\_{t\geq 0} a Wishart process. The state-price density can be rewritten as follows. Define the positive function f:𝕊n++→ℝ+f:\mathbb{S}\_{n}^{++}\to\mathbb{R}^{+} such that f​(v):=1+tr​[u0​v]f(v):=1+\textup{tr}[u\_{0}v] then the state-price density writes as ζt=e−α​t​f​(vt)\zeta\_{t}=e^{-\alpha t}f(v\_{t}) and is positive as ff is. Define g​(v):=(α−ℒ)​f​(v)g(v):=(\alpha-\mathcal{L})f(v) and assume that it is a positive function for sufficiently large α\alpha. Using Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates"), Eqs. (1.2),(1.3),(1.4)), the state-price density allows us to compute SB0​(t,T)\mathrm{SB}\_{0}(t,T) given by ([4](https://arxiv.org/html/2602.06415v1#S2.E4 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), or any other mortality related product, if we assume the following change of probability measure

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζt=e−∫0t(μx​(s)+μy​(s))​𝑑s​d​ℚd​ℙ|ℱt.\displaystyle\zeta\_{t}=e^{-\int\_{0}^{t}(\mu\_{x}(s)+\mu\_{y}(s))ds}\left.\frac{d\mathbb{Q}}{d\mathbb{P}}\right|\_{\mathcal{F}\_{t}}. |  | (19) |

Indeed, suppose that one needs to compute the value at time tt of Πt\Pi\_{t} that is equal to 11 at time TT conditional on the annuitants xx and yy being alive at that time, then its value is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πt\displaystyle\Pi\_{t} | =𝔼tℚ​[e−∫tT(μx​(s)+μy​(s))​𝑑s],\displaystyle=\mathbb{E}\_{t}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}(\mu\_{x}(s)+\mu\_{y}(s))ds}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼t​[ζTζt],\displaystyle=\mathbb{E}\_{t}\left[\frac{\zeta\_{T}}{\zeta\_{t}}\right], |  |

which is known explicitly for a suitable choice of the state-price density (ζt)t≥0(\zeta\_{t})\_{t\geq 0}.444Note that the pricing is done under the historical probability measure. This contrasts with the standard approach, where the dynamics of the state variable are specified under the risk-neutral measure. See Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")) for some implications. The following section shows how the expectations presented in Section [2](https://arxiv.org/html/2602.06415v1#S2 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") can be handled.555Since the interest rates are deterministic, the pricing kernel is about the mortality risk.

Our choice of the positive function f​(v)=1+tr​[u0​v]f(v)=1+\textup{tr}[u\_{0}v] is a deliberate aspect of the model specification. The potential approach proposed by Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates")) necessitates ff to be a positive function of the state variable. We selected this particular form of ff to ensure that the joint survival annuity price remains a linear-rational function of the state variable vtv\_{t}. It is important to note that alternative choices for ff could impact the results discussed later. However, we leave the exploration of these alternatives for future research.

###### Remark 3.6.

The results in this work rely upon the linear-rational structure to obtain the price of the joint survival annuity and the guaranteed joint survival annuity option. It is straightforward to see the set of admissible f:𝕊n+→ℝ+f:\mathbb{S}\_{n}^{+}\to\mathbb{R}^{+} that retains the linear-rational structure must take the form

|  |  |  |
| --- | --- | --- |
|  | f​(v)=ϕ+tr⁡[θ1​v]f(v)=\phi+\operatorname{tr}[\theta\_{1}v] |  |

where ϕ∈ℝ\phi\in\mathbb{R} and θ1\theta\_{1} is a positive semi-definite matrix. Since ϕ\phi shifts the level of f​(v)f(v), it could be difficult to disentangle with the parameters of the Wishart process that control its level. To avoid identification issues, we set ϕ=1\phi=1 and adopt the specification f​(v):=1+tr​[u0​v]f(v):=1+\textup{tr}[u\_{0}v].

## 4 Joint survival annuity valuation

To illustrate the methodology on the linear-rational Wishart mortality model, let us start with the joint survival bond that can be explicitly computed as the following proposition shows.

###### Proposition 4.1.

Let u1∈𝕊n+u\_{1}\in\mathbb{S}\_{n}^{+} and u2∈𝕊n+u\_{2}\in\mathbb{S}\_{n}^{+} and define u0=u1+u2u\_{0}=u\_{1}+u\_{2}. Assume further that ([18](https://arxiv.org/html/2602.06415v1#S3.E18 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) holds. Then on the set {τx>t,τy>t}\{\tau\_{x}>t,\tau\_{y}>t\} the joint survival bond SB​(t,T)\mathrm{SB}(t,T) given by ([4](https://arxiv.org/html/2602.06415v1#S2.E4 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) is known explicitly as we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | SB​(t,T)\displaystyle\mathrm{SB}(t,T) | =P​(t,T)​e−α​(T−t)​1+b0​(T−t)+tr​[a0​(T−t)​vt]1+tr​[u0​vt],\displaystyle=P(t,T)e^{-\alpha(T-t)}\frac{1+b\_{0}(T-t)+\textup{tr}[a\_{0}(T-t)v\_{t}]}{1+\textup{tr}[u\_{0}v\_{t}]}, |  | (20) |

where b0​(t):=b1​(t)+b2​(t)b\_{0}(t):=b\_{1}(t)+b\_{2}(t) and a0​(t):=a1​(t)+a2​(t)a\_{0}(t):=a\_{1}(t)+a\_{2}(t) with (b1​(t),a1​(t))(b\_{1}(t),a\_{1}(t)) and (b2​(t),a2​(t))(b\_{2}(t),a\_{2}(t)) two sets of functions obtained using Lemma [3.3](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") for u1u\_{1} and u2u\_{2}, respectively.

We should note that the above proposition is identical to the result derived in Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")). This is to be expected given the result is independent of the parameterisation and the modelling choices we make on the Wishart process.666Note that any symmetric positive-definite matrix-valued process sharing the Wishart drift, regardless of its diffusion term, yields the same survival-bond expression, because the expression depends only on the drift of the process. From now on, we will avoid mentioning that the expectations conditional on a given time tt are only valid on the sets {τx>t,τy>t}\{\tau\_{x}>t,\tau\_{y}>t\} or {τx>t}\{\tau\_{x}>t\}, depending on the expectation considered.

According to Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates"), Eq. (1.5)) or Björk ([2009](https://arxiv.org/html/2602.06415v1#bib.bib123 "Arbitrage theory in continuous time"), Eq. (28.42)) and Cairns ([2004](https://arxiv.org/html/2602.06415v1#bib.bib24 "Interest rate models: an introduction"), p. 134), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | μx​(s)+μy​(s)\displaystyle\mu\_{x}(s)+\mu\_{y}(s) | =(α−ℒ)​ff=α+α​tr​[u0​vs]−tr​[u0​ω]−2​tr​[u0​m​vs]1+tr​[u0​vs].\displaystyle=\frac{(\alpha-\mathcal{L})f}{f}=\frac{\alpha+\alpha\textup{tr}[u\_{0}v\_{s}]-\textup{tr}[u\_{0}\omega]-2\textup{tr}[u\_{0}mv\_{s}]}{1+\textup{tr}[u\_{0}v\_{s}]}. |  |

Through our judicious choice of ff, we are able to isolate α\alpha. Below we define the mortality intensities to be

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μx​(s)\displaystyle\mu\_{x}(s) | =α/2+α​tr​[u1​vs]−tr​[u1​ω]−2​tr​[u1​m​vs]1+tr​[u0​vs],\displaystyle=\frac{\alpha/2+\alpha\textup{tr}[u\_{1}v\_{s}]-\textup{tr}[u\_{1}\omega]-2\textup{tr}[u\_{1}mv\_{s}]}{1+\textup{tr}[u\_{0}v\_{s}]}, |  | (21) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μy​(s)\displaystyle\mu\_{y}(s) | =α/2+α​tr​[u2​vs]−tr​[u2​ω]−2​tr​[u2​m​vs]1+tr​[u0​vs],\displaystyle=\frac{\alpha/2+\alpha\textup{tr}[u\_{2}v\_{s}]-\textup{tr}[u\_{2}\omega]-2\textup{tr}[u\_{2}mv\_{s}]}{1+\textup{tr}[u\_{0}v\_{s}]}, |  | (22) |

where we have chosen to apportion the term α\alpha equally to both annuitants.777These mortality intensities are structurally the same to the short rate / mortality intensity (35)-(36) in Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")). Alternative specifications would involve either changing ff as mentioned in Remark [3.6](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem6 "Remark 3.6. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), or on how the intensities are defined in ([21](https://arxiv.org/html/2602.06415v1#S4.E21 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"))-([22](https://arxiv.org/html/2602.06415v1#S4.E22 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), or through the choices of u1,u2u\_{1},u\_{2}.
From now on, we suppose that there exists α\alpha such that μx​(s)\mu\_{x}(s) given by ([21](https://arxiv.org/html/2602.06415v1#S4.E21 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and μy​(s)\mu\_{y}(s) given by ([22](https://arxiv.org/html/2602.06415v1#S4.E22 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) are positive. The existence of an α\alpha such that the intensities are positive is dependent on the choice of the matrices u1,u2u\_{1},u\_{2} and the parameters of the Wishart process. We provide a sufficient requirement in the case when n=2n=2 subsequently.

###### Remark 4.2.

Let us reiterate the fact that the potential approach of Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates")) proceeds differently from the traditional mortality modelling approaches of Dahl ([2004](https://arxiv.org/html/2602.06415v1#bib.bib72 "Stochastic mortality in life insurance: Market reserves and mortality-linked insurance contracts")) and Biffis ([2005](https://arxiv.org/html/2602.06415v1#bib.bib73 "Affine processes for dynamic mortality and actuarial valuations")), which consist of specifying the dynamics of the mortality intensity, thereby determining the state-price density. In contrast, Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates")) specifies the state-price density, which in turn determines the intensity. Conditions on the state-price density ensure that the intensity remains positive. Note also that, since the dynamics ([8](https://arxiv.org/html/2602.06415v1#S3.E8 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) of (vt)t≥0(v\_{t})\_{t\geq 0} are given under ℙ\mathbb{P}, the dynamics of the intensities are also specified under this probability measure, and therefore pricing is conducted under ℙ\mathbb{P}. Following Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates"), p. 164), it is possible to determine the dynamics of (vt)t≥0(v\_{t})\_{t\geq 0} under the risk-neutral probability measure, and thus also the dynamics of the intensities (see Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")) for an example applied to the Wishart process). However, since these are not needed for our purposes, we omit the details.

###### Remark 4.3.

Note, we can easily extend our model to the case of an kk-joint annuity as follows. First, we should have a dimension of the Wishart process to be at least n≥kn\geq k. We then set u0=∑i=1kuiu\_{0}=\sum\_{i=1}^{k}u\_{i}, and similar to the above intensities in ([21](https://arxiv.org/html/2602.06415v1#S4.E21 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and ([22](https://arxiv.org/html/2602.06415v1#S4.E22 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), we could define the ii’th annuitant’s mortality intensity as

|  |  |  |
| --- | --- | --- |
|  | μi​(s)=α/k+α​tr​[ui​vs]−tr​[ui​ω]−2​tr​[ui​m​vs]1+tr​[u0​vs].\mu\_{i}(s)=\frac{\alpha/k+\alpha\textup{tr}[u\_{i}v\_{s}]-\textup{tr}[u\_{i}\omega]-2\textup{tr}[u\_{i}mv\_{s}]}{1+\textup{tr}[u\_{0}v\_{s}]}. |  |

In order to understand how the positivity enters into the problem let us consider the case of n=2n=2 (with noting that nn could possibly be larger, and thus be a multi-factor mortality model). By assumption u1∈𝕊n+u\_{1}\in\mathbb{S}\_{n}^{+} and u2∈𝕊n+u\_{2}\in\mathbb{S}\_{n}^{+} so that tr​[u1​ω]\textup{tr}[u\_{1}\omega], tr​[u2​ω]\textup{tr}[u\_{2}\omega], tr​[u1​vs]\textup{tr}[u\_{1}v\_{s}] and tr​[u2​vs]\textup{tr}[u\_{2}v\_{s}] are positive as ω∈𝕊n++\omega\in\mathbb{S}\_{n}^{++} while vsv\_{s} belongs to 𝕊n++\mathbb{S}\_{n}^{++}. If tr​[u1​m​vs]<0\textup{tr}[u\_{1}mv\_{s}]<0 and tr​[u2​m​vs]<0\textup{tr}[u\_{2}mv\_{s}]<0 then as long as α/2>max⁡(tr​[u1​ω],tr​[u2​ω])\alpha/2>\max(\textup{tr}[u\_{1}\omega],\textup{tr}[u\_{2}\omega]) then μx​(s)\mu\_{x}(s) and μy​(s)\mu\_{y}(s) are positive. To gain a little bit more of understanding of the positivity problem, it is worth considering the simple case n=2n=2, mm diagonal, u1=e11u\_{1}=e\_{11} and u2=e22u\_{2}=e\_{22} then in that particular case μx​(s)\mu\_{x}(s) and μy​(s)\mu\_{y}(s) rewrite as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μx​(s)\displaystyle\mu\_{x}(s) | =α/2+α​v11,s−ω11−2​m11​v11,s1+v11,s+v22,s,\displaystyle=\frac{\alpha/2+\alpha v\_{11,s}-\omega\_{11}-2m\_{11}v\_{11,s}}{1+v\_{11,s}+v\_{22,s}}, |  | (23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μy​(s)\displaystyle\mu\_{y}(s) | =α/2+α​v22,s−ω22−2​m22​v22,s1+v11,s+v22,s,\displaystyle=\frac{\alpha/2+\alpha v\_{22,s}-\omega\_{22}-2m\_{22}v\_{22,s}}{1+v\_{11,s}+v\_{22,s}}, |  | (24) |

where the condition α/2>max⁡(ω11,ω22)\alpha/2>\max(\omega\_{11},\omega\_{22}) clearly shows that it is sufficient to ensure the positivity of both μx​(s)\mu\_{x}(s) and μy​(s)\mu\_{y}(s) as the matrix mm has negative eigenvalues (which means the diagonal terms are negative since mm is diagonal). Furthermore, the correlation between these two variables is driven by d​⟨v11,.,v22,.⟩sd\langle v\_{11,.},v\_{22,.}\rangle\_{s} given by ([16](https://arxiv.org/html/2602.06415v1#S3.E16 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), which means it is controlled by the coefficient (σ2)12(\sigma^{2})\_{12} that can take any sign and is zero if σ12=0\sigma\_{12}=0. As such, σ12\sigma\_{12} is the coefficient through which we control the dependency between the two intensities. Analysing the scaled mortality intensities (1+tr​[u0​vs])​μx​(s)(1+\textup{tr}[u\_{0}v\_{s}])\mu\_{x}(s) and (1+tr​[u0​vs])​μy​(s)(1+\textup{tr}[u\_{0}v\_{s}])\mu\_{y}(s), we can find their instantaneous quadratic covariation which is given by d​⟨tr​[h1​v.],tr​[h2​v.]⟩sd\langle\textup{tr}[h\_{1}v\_{.}],\textup{tr}[h\_{2}v\_{.}]\rangle\_{s} with h1=α​u1−2​u1​mh\_{1}=\alpha u\_{1}-2u\_{1}m and h2=α​u2−2​u2​mh\_{2}=\alpha u\_{2}-2u\_{2}m. Using Proposition [3.4](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | d⟨(1+tr[u0v.])μx(.),(1+tr[u0v.])μy(.)⟩s\displaystyle d\langle(1+\textup{tr}[u\_{0}v\_{.}])\mu\_{x}(.),(1+\textup{tr}[u\_{0}v\_{.}])\mu\_{y}(.)\rangle\_{s} | =d​⟨tr​[h1​v.],tr​[h2​v.]⟩s\displaystyle=d\langle\textup{tr}[h\_{1}v\_{.}],\textup{tr}[h\_{2}v\_{.}]\rangle\_{s} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =tr​[(h1+h1⊤)​vs​(h2+h2⊤)​σ2]​d​s,\displaystyle=\textup{tr}[(h\_{1}+h\_{1}^{\top})v\_{s}(h\_{2}+h\_{2}^{\top})\sigma^{2}]ds\,, |  | (25) |

which demonstrates the impact of the parameters on the covariance between the mortality intensities. Note that when u1=e11u\_{1}=e\_{11} and u2=e22u\_{2}=e\_{22} then the covariation given by ([25](https://arxiv.org/html/2602.06415v1#S4.E25 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) will be zero if σ12=0\sigma\_{12}=0.888Note that while the scaled intensities will have a quadratic covariation of zero if σ12=0\sigma\_{12}=0, the quadratic covariation between the intensities will not zero due to the common denominators in ([21](https://arxiv.org/html/2602.06415v1#S4.E21 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and ([22](https://arxiv.org/html/2602.06415v1#S4.E22 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). Finally, analysing the mortality intensities in ([23](https://arxiv.org/html/2602.06415v1#S4.E23 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and ([24](https://arxiv.org/html/2602.06415v1#S4.E24 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), given that α>0\alpha>0, ωi​i>0\omega\_{ii}>0, and mi​i<0m\_{ii}<0, we find ∂μx​(s)∂v11>0\frac{\partial\mu\_{x}(s)}{\partial v\_{11}}>0 and ∂μx​(s)∂v22>0\frac{\partial\mu\_{x}(s)}{\partial v\_{22}}>0. This provides a natural link between the Wishart states and mortality: as v11,sv\_{11,s} and v22,sv\_{22,s} increase, the mortality intensities of xx and yy also increase, respectively. Thus, the Wishart process can replicate an increasing mortality trend over time in expectation, while remaining stationary.

The expression ([21](https://arxiv.org/html/2602.06415v1#S4.E21 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) combined with the analytical results of Propositions [3.1](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") as well as the results in Gurland ([1948](https://arxiv.org/html/2602.06415v1#bib.bib131 "Inversion formulae for the distribution of ratios")) enables the computation of the mortality density as the following proposition shows.

###### Proposition 4.4.

Let μx​(T)\mu\_{x}(T) be the mortality intensity of the annuitant xx that is given by ([21](https://arxiv.org/html/2602.06415v1#S4.E21 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and denote c1=α/2−tr​[u1​ω]c\_{1}=\alpha/2-\textup{tr}[u\_{1}\omega], h1=α​u1−2​u1​mh\_{1}=\alpha u\_{1}-2u\_{1}m, then the cumulative distribution function (conditional to time tt) of μx​(T)\mu\_{x}(T) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(μx​(T)≤z)=12−1π​∫0+∞ℑ⁡(ei​s​(c1−z)​Φ​(T−t,i​s​(h1−z​u0),vt)s)​𝑑s,\displaystyle\mathbb{P}(\mu\_{x}(T)\leq z)=\frac{1}{2}-\frac{1}{\pi}\int\_{0}^{+\infty}\Im\left(\frac{e^{\mathrm{i}s(c\_{1}-z)}\Phi(T-t,\mathrm{i}s(h\_{1}-zu\_{0}),v\_{t})}{s}\right)ds, |  | (26) |

where ℑ(.)\Im(.) stands for the imaginary part of a complex number and Φ(.,.,.)\Phi(.,.,.) is given in Proposition [3.1](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

From the above proposition, we can derive the mortality intensity density by simply taking the derivative of the cumulative distribution, which confirms the usefulness of Proposition [3.5](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), as the following result shows.

###### Corollary 4.5.

Let μx​(T)\mu\_{x}(T) be the mortality intensity of the annuitant xx that is given by ([21](https://arxiv.org/html/2602.06415v1#S4.E21 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), and thus its cumulative distribution function is given by Proposition [4.4](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), then the density (conditional to time t) of μx​(T)\mu\_{x}(T) is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​z​ℙ​(μx​(T)≤z)\displaystyle\frac{d}{dz}\mathbb{P}(\mu\_{x}(T)\leq z) | =−1π​∫0+∞ℑ⁡((−i​s+g1+g2+g3)​ei​s​(c1−z)​Φ​(T−t,i​s​(h1−z​u0),vt)s)​𝑑s,\displaystyle=-\frac{1}{\pi}\int\_{0}^{+\infty}\Im\left(\frac{(-\mathrm{i}s+g\_{1}+g\_{2}+g\_{3})e^{\mathrm{i}s(c\_{1}-z)}\Phi(T-t,\mathrm{i}s(h\_{1}-zu\_{0}),v\_{t})}{s}\right)ds, |  | (27) |

with gj=gj​(T−t,i​s​h1,−i​s​u0,z)g\_{j}=g\_{j}(T-t,\mathrm{i}sh\_{1},-\mathrm{i}su\_{0},z) for j∈{1,2,3}j\in\{1,2,3\} as in Proposition [3.5](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

###### Remark 4.6.

Note that the results above require an explicit expression for the moment generating function, which is not available under the assumptions made in Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")).

Having an explicit form of the mortality density is of significant practical importance. For example, one can compute the conditional means or higher order moments of the mortality intensities, which are modelled under the historical measure ℙ\mathbb{P}, that can guide in the operational use of the model.

Thanks to ([20](https://arxiv.org/html/2602.06415v1#S4.E20 "In Proposition 4.1. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) the joint survival bond SB​(t,T)\mathrm{SB}(t,T) (i.e., ([4](https://arxiv.org/html/2602.06415v1#S2.E4 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"))) is known and therefore the joint survival annuity ([5](https://arxiv.org/html/2602.06415v1#S2.E5 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) is also known as the next proposition shows.

###### Proposition 4.7.

Let T1<…<TNT\_{1}<\ldots<T\_{N} be a set of yearly spaced dates such that t<T<T1t<T<T\_{1} and TN=min⁡(x∗−(x+T+t)−1,y∗−(y+T+t)−1)T\_{N}=\min(x^{\*}-(x+T+t)-1,y^{\*}-(y+T+t)-1) with x∗x^{\*}, resp. y∗y^{\*}, the maximum age the xx, resp. yy, insured can reach. The joint survival annuity pays 1 conditional on the survival of both annuitants at those dates, its value at time TT is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1NSB​(T,Ti)=b3​(T,TN)+tr​[a3​(T,TN)​vT]1+tr​[u0​vT],\displaystyle\sum\_{i=1}^{N}\mathrm{SB}(T,T\_{i})=\frac{b\_{3}(T,T\_{N})+\textup{tr}[a\_{3}(T,T\_{N})v\_{T}]}{1+\textup{tr}[u\_{0}v\_{T}]}, |  | (28) |

with

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | b3​(T,TN)\displaystyle b\_{3}(T,T\_{N}) | :=∑i=1NP​(T,Ti)​e−α​(Ti−T)​(1+b0​(Ti−T)),\displaystyle:=\sum\_{i=1}^{N}P(T,T\_{i})e^{-\alpha(T\_{i}-T)}\left(1+b\_{0}(T\_{i}-T)\right), |  | (29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | a3​(T,TN)\displaystyle a\_{3}(T,T\_{N}) | :=∑i=1NP​(T,Ti)​e−α​(Ti−T)​a0​(Ti−T),\displaystyle:=\sum\_{i=1}^{N}P(T,T\_{i})e^{-\alpha(T\_{i}-T)}a\_{0}(T\_{i}-T), |  | (30) |

with b0(.),a0(.)b\_{0}(.),a\_{0}(.) given in Proposition [4.1](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

Note that the joint survival annuity ([28](https://arxiv.org/html/2602.06415v1#S4.E28 "In Proposition 4.7. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) also has a linear-rational form so its density can be computed explicitly (up to a one-dimensional numerical integration).

###### Proposition 4.8.

Let ∑i=1NSB​(T,Ti)\sum\_{i=1}^{N}\mathrm{SB}(T,T\_{i}) be a joint survival annuity defined in Proposition [4.7](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem7 "Proposition 4.7. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). Then the cumulative distribution function (conditional to time t) of ∑i=1NSB​(T,Ti)\sum\_{i=1}^{N}\mathrm{SB}(T,T\_{i}) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(∑i=1NSB​(T,Ti)≤z)=12−1π​∫0+∞ℑ⁡(ei​s​(b3−z)​Φ​(T−t,i​s​(a3−z​u0),vt)s)​𝑑s,\displaystyle\mathbb{P}\left(\sum\_{i=1}^{N}\mathrm{SB}(T,T\_{i})\leq z\right)=\frac{1}{2}-\frac{1}{\pi}\int\_{0}^{+\infty}\Im\left(\frac{e^{\mathrm{i}s(b\_{3}-z)}\Phi(T-t,\mathrm{i}s(a\_{3}-zu\_{0}),v\_{t})}{s}\right)ds, |  | (31) |

where a3a\_{3} and b3b\_{3} are the expressions in Proposition [4.7](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem7 "Proposition 4.7. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") with their dependencies dropped on (T,TN)(T,T\_{N}) and Φ(.,.,.)\Phi(.,.,.) is given in Proposition [3.1](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

Since we have the density of the future annuity value, we can compute certain risk management quantities such as the lower tail that gives the value at risk or the expected shortfall. This sharply contrasts with the mortality model based on the exponential affine framework for which these quantities are very hard to obtain. Further along this line, an option on the joint survival annuity, also named the guaranteed joint survival annuity option, can be priced very efficiently in the linear-rational Wishart mortality model as the next section shows.

## 5 Guaranteed joint survival annuity option valuation

With the joint survival annuity being priced, the next step is to calculate the value of an option on that contract and also to develop option price approximations that simplify the model implementation as well as the risk management of the product. First, we show that an option on the joint survival annuity is surprisingly simple to price in the linear-rational Wishart mortality model.

###### Proposition 5.1.

The value at time tt of a guaranteed joint survival annuity option ([7](https://arxiv.org/html/2602.06415v1#S2.E7 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) with maturity TT is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯​(t,T,TN):=P​(t,T)​e−α​(T−t)​𝔼t​[(b4​(T,TN)+tr​[a4​(T,TN)​vT])+]1+tr​[u0​v0],\displaystyle\bar{C}(t,T,T\_{N}):=P(t,T)e^{-\alpha(T-t)}\frac{\mathbb{E}\_{t}\left[(b\_{4}(T,T\_{N})+\textup{tr}[a\_{4}(T,T\_{N})v\_{T}])\_{+}\right]}{1+\textup{tr}[u\_{0}v\_{0}]}, |  | (32) |

with b4​(T,TN)b\_{4}(T,T\_{N}) a constant and a4​(T,TN)a\_{4}(T,T\_{N}) a matrix such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | b4​(T,TN)\displaystyle b\_{4}(T,T\_{N}) | :=b3​(T,TN)−1g,\displaystyle:=b\_{3}(T,T\_{N})-\frac{1}{g}, |  | (33) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | a4​(T,TN)\displaystyle a\_{4}(T,T\_{N}) | :=a3​(T,TN)−1g​u0,\displaystyle:=a\_{3}(T,T\_{N})-\frac{1}{g}u\_{0}, |  | (34) |

where b3(.)b\_{3}(.), a3(.)a\_{3}(.) are given in Proposition [4.7](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem7 "Proposition 4.7. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

As formula ([32](https://arxiv.org/html/2602.06415v1#S5.E32 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) shows, the pricing of a guaranteed joint survival annuity option can be computed using an integration. Indeed, if YT=b4​(T,TN)+tr​[a4​(T,TN)​vT]Y\_{T}=b\_{4}(T,T\_{N})+\textup{tr}[a\_{4}(T,T\_{N})v\_{T}] then its characteristic function is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΦY​(z)\displaystyle\Phi\_{Y}(z) | :=𝔼t​[ei​z​YT]=ei​z​b4​(T,TN)​Φ​(T−t,i​z​a4​(T,TN),v0),\displaystyle:=\mathbb{E}\_{t}\left[e^{\mathrm{i}zY\_{T}}\right]=e^{\mathrm{i}zb\_{4}(T,T\_{N})}\Phi(T-t,\mathrm{i}za\_{4}(T,T\_{N}),v\_{0}), |  | (35) |

with z∈ℂz\in\mathbb{C}, i=−1\mathrm{i}=\sqrt{-1} and the function Φ(.,.,.)\Phi(.,.,.) given by ([12](https://arxiv.org/html/2602.06415v1#S3.E12 "In Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). The expectation in ([32](https://arxiv.org/html/2602.06415v1#S5.E32 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) can be computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[(YT)+]=1π​∫0+∞ℜ⁡(ΦY​(z+i​zi)(i​(z+i​zi))2)​𝑑z,\displaystyle\mathbb{E}\_{t}\left[(Y\_{T})\_{+}\right]=\frac{1}{\pi}\int\_{0}^{+\infty}\Re\left(\frac{\Phi\_{Y}(z+\mathrm{i}z\_{i})}{(\mathrm{i}(z+\mathrm{i}z\_{i}))^{2}}\right)dz\,, |  | (36) |

with zi<0z\_{i}<0 and ℜ(.)\Re(.) the real part.

As the result above shows, the valuation of the guaranteed joint survival annuity option only requires one-dimensional integration. Notice that the result holds whether ω=β​σ2\omega=\beta\sigma^{2} (i.e., Bru case) is satisfied or not (see Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")) for an implementation in the non-Bru case). In that latter case, computing the moment generating function involves further numerical integration. Even if the Bru case condition can be a bit too restrictive in practice, it offers nonetheless certain advantages in terms of option price approximations that provide quick alternatives to the exact formula. In what follows we derive three different approximations to the guaranteed joint survival annuity option price. These analytic approximations are new and would not be available in Da Fonseca ([2024](https://arxiv.org/html/2602.06415v1#bib.bib28 "Pricing guaranteed annuity options in a linear-rational Wishart mortality model")).

To compute an approximation to the expectation ([32](https://arxiv.org/html/2602.06415v1#S5.E32 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), one needs the moments of the variable YT=b4​(T,TN)+tr​[a4​(T,TN)​vT]Y\_{T}=b\_{4}(T,T\_{N})+\textup{tr}[a\_{4}(T,T\_{N})v\_{T}], which by definition can be obtained by taking successive derivatives of the moment generating function. These derivatives can be tedious to perform in the general case, see for example Letac and Massam ([2008](https://arxiv.org/html/2602.06415v1#bib.bib61 "The noncentral Wishart as an exponential family, and its moments")). Fortunately, for our Bru case, it is possible to obtain the moments by a direct series expansion.

###### Proposition 5.2.

Suppose that ω\omega in ([8](https://arxiv.org/html/2602.06415v1#S3.E8 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) is such that ω=β​σ2\omega=\beta\sigma^{2} with β∈ℝ\beta\in\mathbb{R} and β≥n+1\beta\geq n+1 and let YT=b4​(T,TN)+tr​[a4​(T,TN)​vT]Y\_{T}=b\_{4}(T,T\_{N})+\textup{tr}[a\_{4}(T,T\_{N})v\_{T}] with b4​(T,TN)b\_{4}(T,T\_{N}) and a4​(T,TN)a\_{4}(T,T\_{N}) (written b4b\_{4} and a4a\_{4} for simplicity) as in  ([32](https://arxiv.org/html/2602.06415v1#S5.E32 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). The cumulants of YTY\_{T} denoted (κj)j∈ℕ+(\kappa\_{j})\_{j\in\mathbb{N}\_{+}} are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | κj\displaystyle\kappa\_{j} | =b4​δj​1+β​(j−1)!​2j−1​tr​[(ςT​a4)j]+j!​2j−1​tr​[ϑT⊤​(ςT​a4)j],\displaystyle=b\_{4}\delta\_{j1}+\beta(j-1)!2^{j-1}\textup{tr}[(\varsigma\_{T}a\_{4})^{j}]+j!2^{j-1}\textup{tr}[\vartheta\_{T}^{\top}(\varsigma\_{T}a\_{4})^{j}], |  | (37) |

with δj​1=1\delta\_{j1}=1 if j=1j=1 and 0 otherwise, ςT\varsigma\_{T} and ϑT\vartheta\_{T} given in Proposition [3.1](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). The moments of YTY\_{T}, denoted (μj)j∈ℕ+(\mu\_{j})\_{j\in\mathbb{N}\_{+}}, can be obtained from the cumulants thanks to the relation

|  |  |  |  |
| --- | --- | --- | --- |
|  | μj=∑k=1jBj,k​(κ1,…,κj−k+1),\displaystyle\mu\_{j}=\sum\_{k=1}^{j}B\_{j,k}(\kappa\_{1},\ldots,\kappa\_{j-k+1}), |  | (38) |

with Bj,kB\_{j,k} the incomplete Bell polynomials.

The cumulants/moments enable the use of Jarrow and Rudd ([1982](https://arxiv.org/html/2602.06415v1#bib.bib63 "Approximate option valuation for arbitrary stochastic processes"))’s option price approximation that was also applied in Collin-Dufresne and Goldstein ([2002](https://arxiv.org/html/2602.06415v1#bib.bib64 "Pricing swaptions within an affine framework")) to the problem of swaption pricing, which is similar to the pricing of an option on a coupon bearing bond or, equivalently, to an option on an annuity. We follow Collin-Dufresne and Goldstein ([2002](https://arxiv.org/html/2602.06415v1#bib.bib64 "Pricing swaptions within an affine framework")) in our presentation below.

###### Proposition 5.3.

Let YT=b4​(T,TN)+tr​[a4​(T,TN)​vT]Y\_{T}=b\_{4}(T,T\_{N})+\textup{tr}[a\_{4}(T,T\_{N})v\_{T}] with b4​(T,TN)b\_{4}(T,T\_{N}) and a4​(T,TN)a\_{4}(T,T\_{N}) as in  ([32](https://arxiv.org/html/2602.06415v1#S5.E32 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), and denote the first three cumulants of YTY\_{T}, given Proposition [5.2](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), to be (κ1,κ2,κ3)(\kappa\_{1},\kappa\_{2},\kappa\_{3}). Assume that the density of YTY\_{T} can be approximated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​π​κ2​e−(z−κ1)22​κ2​(∑j=03ηj​(z−κ1)j),\displaystyle\frac{1}{\sqrt{2\pi\kappa\_{2}}}e^{-\frac{(z-\kappa\_{1})^{2}}{2\kappa\_{2}}}\left(\sum\_{j=0}^{3}\eta\_{j}(z-\kappa\_{1})^{j}\right)\,, |  | (39) |

with {ηj;j∈0,…,3}\{\eta\_{j};j\in 0,\ldots,3\} some constants related to the first three cumulants of YTY\_{T}. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[(YT)+]∼∑j=03ηj​ξj+1+κ1​∑j=03ηj​ξj,\displaystyle\mathbb{E}\_{t}\left[\left(Y\_{T}\right)\_{+}\right]\sim\sum\_{j=0}^{3}\eta\_{j}\xi\_{j+1}+\kappa\_{1}\sum\_{j=0}^{3}\eta\_{j}\xi\_{j}\,, |  | (40) |

where {ξj;j=0,…,4}\{\xi\_{j};j=0,\ldots,4\} are some constants that can be computed explicitly and depend on the first three cumulants of YTY\_{T}.

The above proposition approximates the density of YTY\_{T}, the variable involved in the guaranteed joint survival annuity option, by a perturbation of the Gaussian distribution. Suppose that the eigenvalues of a4​(T,TN)+a4​(T,TN)⊤a\_{4}(T,T\_{N})+a\_{4}(T,T\_{N})^{\top} are non-negative, a4​(T,TN)+a4​(T,TN)⊤∈𝕊n+a\_{4}(T,T\_{N})+a\_{4}(T,T\_{N})^{\top}\in\mathbb{S}\_{n}^{+} and hence tr​[a4​(T,TN)​vT]>0\mathrm{tr}[a\_{4}(T,T\_{N})v\_{T}]>0. In this case, the support of the density of YTY\_{T} is on the half line and using a Gaussian approximation might not be the most natural choice.

In the Bru case, the Wishart process has a marginal distribution that follows a non-central matrix chi-squared distribution or non-central Wishart distribution. Further can be said when that distribution is projected on a rank one matrix, it appears in Letac and Massam ([2008](https://arxiv.org/html/2602.06415v1#bib.bib61 "The noncentral Wishart as an exponential family, and its moments"), Proposition 3.1) and reads as follows.

###### Proposition 5.4.

Suppose that ω\omega in ([8](https://arxiv.org/html/2602.06415v1#S3.E8 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) is such that ω=β​σ2\omega=\beta\sigma^{2} with β∈ℝ\beta\in\mathbb{R} and β≥n+1\beta\geq n+1 and given a vector γ∈ℝn\gamma\in\mathbb{R}^{n} such that ‖γ‖=1\|\gamma\|=1 then the (scalar) variable γ⊤​vT​γ/(ςT)11\gamma^{\top}v\_{T}\gamma/(\varsigma\_{T})\_{11} admits a non-central Chi-squared distribution with degrees of freedom β\beta and non-centrality parameter (ϑT⊤)11(\vartheta\_{T}^{\top})\_{11}.

The previous proposition gives us an approximation to the characteristic function of the Wishart process for a given TT when it is projected onto a rank-one matrix. In fact, in order to apply this proposition, one needs to specify a vector along which the state variable (i.e., the Wishart process) is projected. The following proposition utilises Proposition [5.4](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem4 "Proposition 5.4. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") to obtain an approximation by projecting the state variable in the direction of the eigenvectors associated with the spectral decomposition of (a4​(T,TN)+a4​(T,TN)⊤)/2\left(a\_{4}(T,T\_{N})+a\_{4}(T,T\_{N})^{\top}\right)/2 and then summing the distributions obtained from the previous proposition under the assumption of independence. This assumption is inconsistent with the state variable distribution, but can still be used to obtain a numerical approximation as detailed below.

###### Proposition 5.5.

Let YT=b4​(T,TN)+tr​[a4​(T,TN)​vT]Y\_{T}=b\_{4}(T,T\_{N})+\textup{tr}[a\_{4}(T,T\_{N})v\_{T}] of Proposition [5.1](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem1 "Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") involved in the pricing of the guaranteed annuity option through ([35](https://arxiv.org/html/2602.06415v1#S5.E35 "In 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and ([36](https://arxiv.org/html/2602.06415v1#S5.E36 "In 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). Denote the spectral decomposition of

|  |  |  |  |
| --- | --- | --- | --- |
|  | a4+a4⊤2=∑i=1nλi​γi​γi⊤,\displaystyle\frac{a\_{4}+a\_{4}^{\top}}{2}=\sum\_{i=1}^{n}\lambda\_{i}\gamma\_{i}\gamma\_{i}^{\top}, |  | (41) |

with (γi)i=1,…,n(\gamma\_{i})\_{i=1,\ldots,n} some orthonormal vectors and (λi)i=1,…,n(\lambda\_{i})\_{i=1,\ldots,n} the corresponding (real) eigenvalues (we drop the dependency of a4a\_{4} and b4b\_{4} on (T,TN)(T,T\_{N})). Rewrite YTY\_{T} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | YT=b4+∑i=1nλi​γi⊤​vT​γi,\displaystyle Y\_{T}=b\_{4}+\sum\_{i=1}^{n}\lambda\_{i}\gamma\_{i}^{\top}v\_{T}\gamma\_{i}, |  | (42) |

then according to Proposition [5.4](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem4 "Proposition 5.4. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") for each i=1,…,ni=1,\ldots,n γi⊤​vT​γi/(ςT)i​i\gamma\_{i}^{\top}v\_{T}\gamma\_{i}/(\varsigma\_{T})\_{ii} has a non-central Chi-squared distribution with degrees of freedom β\beta and non-centrality parameter (ϑT⊤)i​i(\vartheta\_{T}^{\top})\_{ii}. Then we approximate YTY\_{T} with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y~T=b4+∑i=1nλi​(ςT)i​i​χi2,\displaystyle\tilde{Y}\_{T}=b\_{4}+\sum\_{i=1}^{n}\lambda\_{i}(\varsigma\_{T})\_{ii}\chi\_{i}^{2}, |  | (43) |

where (χi2​(β,(ϑT⊤)i​i))i=1,…,n\left(\chi\_{i}^{2}(\beta,(\vartheta\_{T}^{\top})\_{ii})\right)\_{i=1,\ldots,n} is a set of independent non-central Chi-squared random variables (where β\beta is the degrees of freedom and each variable has a specific non-centrality parameter (ϑT⊤)i​i(\vartheta\_{T}^{\top})\_{ii}). In this case, 𝔼t​[(YT)+]∼𝔼t​[(Y~T)+]\mathbb{E}\_{t}[(Y\_{T})\_{+}]\sim\mathbb{E}\_{t}[(\tilde{Y}\_{T})\_{+}] and this latter expectation can be computed using ([36](https://arxiv.org/html/2602.06415v1#S5.E36 "In 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) with the characteristic function of the variable Y~T\tilde{Y}\_{T} that depends (linearly) on a generalized Chi-squared distribution.

Note that if one eigenvalue in ([41](https://arxiv.org/html/2602.06415v1#S5.E41 "In Proposition 5.5. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) dominates all the others, then the above proposition can be simplified, since the computation of the guaranteed joint survival annuity option will then only require the integration of the non-central Chi-squared distribution, instead of requiring a Fourier transform.

###### Corollary 5.6.

Let YT=b4​(T,TN)+tr​[a4​(T,TN)​vT]Y\_{T}=b\_{4}(T,T\_{N})+\textup{tr}[a\_{4}(T,T\_{N})v\_{T}] of Proposition [5.1](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem1 "Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") involved in the pricing of the guaranteed annuity option through ([35](https://arxiv.org/html/2602.06415v1#S5.E35 "In 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and ([36](https://arxiv.org/html/2602.06415v1#S5.E36 "In 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). Assume the spectral decomposition ([41](https://arxiv.org/html/2602.06415v1#S5.E41 "In Proposition 5.5. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and suppose that we have λ1≥λ2≥…≥0≥…≥λn\lambda\_{1}\geq\lambda\_{2}\geq\ldots\geq 0\geq\ldots\geq\lambda\_{n} and λ1≫|λj|,j=2,…​n\lambda\_{1}\gg|\lambda\_{j}|,\,j=2,\ldots n then approximate YTY\_{T} with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y~T=b4+λ1​γ1⊤​vT​γ1,\displaystyle\tilde{Y}\_{T}=b\_{4}+\lambda\_{1}\gamma\_{1}^{\top}v\_{T}\gamma\_{1}\,, |  | (44) |

and according to Proposition [5.4](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem4 "Proposition 5.4. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") the scalar variable γ1⊤​vT​γ1/(ςT)11\gamma\_{1}^{\top}v\_{T}\gamma\_{1}/(\varsigma\_{T})\_{11} follows a non-central Chi-squared distribution with degrees of freedom β\beta and non-centrality parameter (ϑT⊤)11(\vartheta\_{T}^{\top})\_{11}.

If λ1≥λ2≥…≥0≥…≥λn\lambda\_{1}\geq\lambda\_{2}\geq\ldots\geq 0\geq\ldots\geq\lambda\_{n} and |λn|≫|λj|,j=1,…​n−1|\lambda\_{n}|\gg|\lambda\_{j}|,\,j=1,\ldots n-1 then approximate YTY\_{T} with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y~T=b4+λn​γn⊤​vT​γn,\displaystyle\tilde{Y}\_{T}=b\_{4}+\lambda\_{n}\gamma\_{n}^{\top}v\_{T}\gamma\_{n}\,, |  | (45) |

and according to Proposition [5.4](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem4 "Proposition 5.4. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") the scalar variable γn⊤​vT​γn/(ςT)11\gamma\_{n}^{\top}v\_{T}\gamma\_{n}/(\varsigma\_{T})\_{11} follows a non-central Chi-squared distribution distribution with degrees of freedom β\beta and non-centrality parameter (ϑT⊤)11(\vartheta\_{T}^{\top})\_{11}.

In the equation ([39](https://arxiv.org/html/2602.06415v1#S5.E39 "In Proposition 5.3. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) we approximate the density of YTY\_{T} using a perturbation of the Gaussian distribution, but the marginal distribution of the Wishart process suggests that it is more natural to approximate the density with a perturbation of the (scalar) gamma distribution. Indeed, if a4​(T,TN)a\_{4}(T,T\_{N}) in Proposition [5.2](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") has positive eigenvalues, then necessarily b4<0b\_{4}<0 and the support of the density of YTY\_{T} is in [k,+∞)[k,\;+\infty) with k<0k<0 and if a4​(T,TN)a\_{4}(T,T\_{N}) has negative eigenvalues, then necessarily b4>0b\_{4}>0 and the support of the density of YTY\_{T} is in (−∞,k](-\infty,\;k] for k>0k>0. As such, the Gaussian distribution, whose support is in ℝ\mathbb{R}, might not be the most convenient distribution to approximate the density of YTY\_{T}. Further to this, taking the limit as t→∞t\to\infty in ([12](https://arxiv.org/html/2602.06415v1#S3.E12 "In Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) shows that the asymptotic distribution of the Wishart process has a moment generating function of the form 1det(In−2​ςt​θ1)β/2\frac{1}{\det(I\_{n}-2\varsigma\_{t}\theta\_{1})^{\beta/2}}, which corresponds to a matrix gamma distribution. Filipović et al. ([2013](https://arxiv.org/html/2602.06415v1#bib.bib65 "Density approximations for multivariate affine jump-diffusion processes")) show how to approximate the density of a random variable using a perturbation of the (scalar) gamma distribution, instead of the Gaussian distribution in ([39](https://arxiv.org/html/2602.06415v1#S5.E39 "In Proposition 5.3. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), if the cumulants of the variable are available. As such, Proposition [5.2](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") allows us to use their results as the following proposition shows.

###### Proposition 5.7.

Let YT=b4​(T,TN)+tr​[a4​(T,TN)​vT]Y\_{T}=b\_{4}(T,T\_{N})+\textup{tr}[a\_{4}(T,T\_{N})v\_{T}] with b4​(T,TN)b\_{4}(T,T\_{N}) and a4​(T,TN)a\_{4}(T,T\_{N}) as in  ([32](https://arxiv.org/html/2602.06415v1#S5.E32 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), and denote the first three cumulants of YTY\_{T}, given Proposition [5.2](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), to be (κ1,κ2,κ3)(\kappa\_{1},\kappa\_{2},\kappa\_{3}). If the eigenvalues of a4​(T,TN)a\_{4}(T,T\_{N}) are all positive, then we can obtain the following approximation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[(YT)+]\displaystyle\mathbb{E}\_{t}\left[\left(Y\_{T}\right)\_{+}\right] | =∑j=03∑i=0jcj​γj,iβ¯​(α¯+1)i+1​Q​(α¯+i+2,−β¯​k)\displaystyle=\sum\_{j=0}^{3}\sum\_{i=0}^{j}\frac{c\_{j}\gamma\_{j,i}}{\bar{\beta}}(\bar{\alpha}+1)\_{i+1}Q(\bar{\alpha}+i+2,-\bar{\beta}k) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∑j=03∑i=0jcj​γj,i​k​(α¯+1)i​Q​(α¯+i+1,−β¯​k),\displaystyle+\sum\_{j=0}^{3}\sum\_{i=0}^{j}c\_{j}\gamma\_{j,i}k(\bar{\alpha}+1)\_{i}Q(\bar{\alpha}+i+1,-\bar{\beta}k)\,, |  | (46) |

with {cj;j=0,…,3}\{c\_{j};j=0,\ldots,3\}, {γj,i;j,i=0,…,3}\{\gamma\_{j,i};j,i=0,\ldots,3\}, α¯\bar{\alpha} and β¯\bar{\beta} some parameters that depend on kk and the first three moments of YTY\_{T}, while Q​(s,x)Q(s,x) stands for the upper regularised incomplete gamma function while (x)n(x)\_{n} is the Pochhammer function.

If the eigenvalues of a4​(T,TN)a\_{4}(T,T\_{N}) are all negative, then we can obtain the following approximation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[(YT)+]\displaystyle\mathbb{E}\_{t}\left[\left(Y\_{T}\right)\_{+}\right] | =−∑j=03∑i=0jcj​γj,iβ¯​(α¯+1)i+1​P​(α¯+i+2,−β¯​k)\displaystyle=-\sum\_{j=0}^{3}\sum\_{i=0}^{j}\frac{c\_{j}\gamma\_{j,i}}{\bar{\beta}}(\bar{\alpha}+1)\_{i+1}P(\bar{\alpha}+i+2,-\bar{\beta}k) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −∑j=03∑i=0jcj​γj,i​k​(α¯+1)i​P​(α¯+i+1,−β¯​k),\displaystyle-\sum\_{j=0}^{3}\sum\_{i=0}^{j}c\_{j}\gamma\_{j,i}k(\bar{\alpha}+1)\_{i}P(\bar{\alpha}+i+1,-\bar{\beta}k)\,, |  | (47) |

with {cj;j=0,…,3}\{c\_{j};j=0,\ldots,3\}, {γj,i;j,i=0,…,3}\{\gamma\_{j,i};j,i=0,\ldots,3\}, α¯\bar{\alpha} and β¯\bar{\beta} some parameters that depend on kk and the first three moments of YTY\_{T}, while P​(s,x)P(s,x) stands for the lower regularised incomplete gamma function while (x)n(x)\_{n} is the Pochhammer function.

## 6 Model implementation

In this section we present numerical experiments on the linear-rational Wishart mortality model. Our numerical experiments consist of sensitivity analyses of the guaranteed joint survival annuity option price on selected parameters, it also compares the three approximation methods developed in Section [5](https://arxiv.org/html/2602.06415v1#S5 "5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") to the characteristic function pricing approach, and we also demonstrate the potential consequences of incorrectly not accounting for the dependency between annuitants demonstrated in the guaranteed joint survival annuity option price. For simpler exposition, we will refer to the guaranteed joint survival annuity option price as the option price.

The parameters utilised in our numerical experiments are presented in Tables [1](https://arxiv.org/html/2602.06415v1#S8.T1 "Table 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") and [2](https://arxiv.org/html/2602.06415v1#S8.T2 "Table 2 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). Table [1](https://arxiv.org/html/2602.06415v1#S8.T1 "Table 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") encapsulates model-specific parameters. These parameters were judiciously chosen to be consistent with values empirically observed in the extant literature.999We take r=0r=0 to analyse the effect of the Wishart parameters on the option price without contaminating influence from the interest rate discounting factor. Meanwhile Table [2](https://arxiv.org/html/2602.06415v1#S8.T2 "Table 2 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") contains the foundational values on which our subsequent sensitivity analyses are predicated.

[ Insert Table [1](https://arxiv.org/html/2602.06415v1#S8.T1 "Table 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") here ]

[ Insert Table [2](https://arxiv.org/html/2602.06415v1#S8.T2 "Table 2 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") here ]

To elucidate our model parameter selection, let us consider Table [3](https://arxiv.org/html/2602.06415v1#S8.T3 "Table 3 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). This table delineates the moments for μx​(s)\mu\_{x}(s) and μy​(s)\mu\_{y}(s) at various time points ss. These moments were derived using Corollary [4.5](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem5 "Corollary 4.5. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). Specifically, when s=2s=2, we observe that the anticipated mortality rates for annuitants xx and yy stand at 0.01990.0199 and 0.01980.0198 respectively. In a recent study by Li et al. ([2023](https://arxiv.org/html/2602.06415v1#bib.bib35 "Pricing extreme mortality risk in the wake of the COVID-19 pandemic")), the authors utilised U.S. mortality data spanning 2017-2022 and find that the excess mortality rate is approximately 0.0132.101010This computation is based on the one-year conditional expectation based on parameters reported in Table 4.1 of Li et al. ([2023](https://arxiv.org/html/2602.06415v1#bib.bib35 "Pricing extreme mortality risk in the wake of the COVID-19 pandemic")) assuming an initial excess mortality of 0. Augmenting our analysis, the one-year conditional expected mortality rate in Xu et al. ([2020](https://arxiv.org/html/2602.06415v1#bib.bib47 "Continuous-time multi-cohort mortality modelling with affine processes")) is found to be 0.0107 and is based on data from the Human Mortality Database.111111This calculation stems from the one-year conditional expectation of the one-factor mortality model reported in Table 1 of Xu et al. ([2020](https://arxiv.org/html/2602.06415v1#bib.bib47 "Continuous-time multi-cohort mortality modelling with affine processes")).

[ Insert Table [3](https://arxiv.org/html/2602.06415v1#S8.T3 "Table 3 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") here ]

One compelling advantage of the linear-rational Wishart model is its capability to accommodate explicit dependence between annuitants. This essentially means that correlations in the longevity risks of two individuals can be accurately captured by the model.121212An important note to make here is that our model can be seamlessly adapted to address larger groups, be it cohorts, entire populations or even distinct risk factors. Drawing upon ([16](https://arxiv.org/html/2602.06415v1#S3.E16 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) we can compute the instantaneous correlation between the normalised intensities μx∗​(s)=(1+tr​[u0​vs])​μx​(s)\mu\_{x}^{\*}(s)=(1+\textup{tr}[u\_{0}v\_{s}])\mu\_{x}(s) and μy∗​(s)=(1+tr​[u0​vs])​μy​(s)\mu\_{y}^{\*}(s)=(1+\textup{tr}[u\_{0}v\_{s}])\mu\_{y}(s). For clarity, this computation is explicated below and is derived using Proposition [3.4](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") and ([25](https://arxiv.org/html/2602.06415v1#S4.E25 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Corr​(d​μx∗​(s),d​μy∗​(s))\displaystyle\text{Corr}(d\mu\_{x}^{\*}(s),d\mu\_{y}^{\*}(s)) | =Cov⁡(d​μx∗​(s),d​μy∗​(s))Cov⁡(d​μx∗​(s),d​μx∗​(s))​Cov⁡(d​μy∗​(s),d​μy∗​(s))\displaystyle=\frac{\operatorname{Cov}(d\mu\_{x}^{\*}(s),d\mu\_{y}^{\*}(s))}{\sqrt{\operatorname{Cov}(d\mu\_{x}^{\*}(s),d\mu\_{x}^{\*}(s))\operatorname{Cov}(d\mu\_{y}^{\*}(s),d\mu\_{y}^{\*}(s))}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =v12,s​(σ2)12v11,s​v22,s​(σ2)11​(σ2)22​d​s.\displaystyle=\frac{v\_{12,s}(\sigma^{2})\_{12}}{\sqrt{v\_{11,s}v\_{22,s}(\sigma^{2})\_{11}(\sigma^{2})\_{22}}}ds. |  | (48) |

Armed with the values provided in Table [1](https://arxiv.org/html/2602.06415v1#S8.T1 "Table 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), we can discern an instantaneous correlation between the normalised intensities of 0.40 at the inception tt. Due to the choice of our matrix mm, we can also investigate the average ‘asymptotic’ instantaneous correlation between the two annuitants. By substituting the formula lims→∞𝔼​[vs]\lim\_{s\rightarrow\infty}\mathbb{E}[v\_{s}] from Lemma [3.3](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") into ([48](https://arxiv.org/html/2602.06415v1#S6.E48 "In 6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), our model posits an average asymptotic correlation between the normalised intensities of 0.65. The values of our correlations are reasonable and well-founded. The work Frees et al. ([1996](https://arxiv.org/html/2602.06415v1#bib.bib40 "Annuity valuation with dependent mortality")), which pegged the correlation between annuitants in last-survivor annuities within a 95% confidence band of (0.41, 0.56) based on last survivor annuity contracts provided by a Canadian insurer.

Lastly, we focus on the parameter gg outlined in Table [2](https://arxiv.org/html/2602.06415v1#S8.T2 "Table 2 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). It was carefully selected to make the guaranteed joint survival annuity option nearly ‘at-the-money’ for values of T−t=2T-t=2 and TN−t=5T\_{N}-t=5, considering the model parameters from Table [1](https://arxiv.org/html/2602.06415v1#S8.T1 "Table 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). To determine this parameter, we calculated the expected value of a joint survival annuity spanning five yearly payments, denoted as:

|  |  |  |
| --- | --- | --- |
|  | ∑i=15SB​(t,Ti),\sum\_{i=1}^{5}\mathrm{SB}(t,T\_{i}), |  |

where Ti−t=iT\_{i}-t=i for i=1,…,5i=1,...,5. Using Proposition [4.7](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem7 "Proposition 4.7. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), the computed value of the joint survival annuity is 4.467. Consequently, we chose g=1/4.467≈0.225g=1/4.467\approx 0.225, aligning the value of the joint survival annuity starting in 2 years with that of a joint survival annuity beginning immediately.

### 6.1 Sensitivity analyses

In this section, we study the sensitivity of the guaranteed joint survival annuity option price in relation to changes in various model parameters. Figure [1](https://arxiv.org/html/2602.06415v1#S8.F1 "Figure 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") displays the variations in option price as parameters α\alpha, β\beta, ρσ\rho\_{\sigma}, m11m\_{11}, σ11\sigma\_{11}, and TT are adjusted.

[ Insert Figure [1](https://arxiv.org/html/2602.06415v1#S8.F1 "Figure 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") here ]

The option price displays a nearly linear increase when parameters β\beta, ρσ\rho\_{\sigma}, m11m\_{11}, and σ11\sigma\_{11} are changed. This is consistent with expectations and is attributable to the interplay of mortality intensities as described in ([23](https://arxiv.org/html/2602.06415v1#S4.E23 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"))-([24](https://arxiv.org/html/2602.06415v1#S4.E24 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). For instance, an increase in β\beta directly increases ω\omega since our model follows ([10](https://arxiv.org/html/2602.06415v1#S3.E10 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), leading to decreased instantaneous mortality intensities. This results in a greater likelihood of option exercise due to increased joint survival probability, thus raising the option price. Similar reasoning applies to the parameters m11m\_{11} and σ11\sigma\_{11}. Given the relationship ω=β​σ2\omega=\beta\sigma^{2}, we derive:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ω11\displaystyle\omega\_{11} | =β​((σ11)2+(σ12)2),\displaystyle=\beta\left((\sigma\_{11})^{2}+(\sigma\_{12})^{2}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ω22\displaystyle\omega\_{22} | =β​((σ22)2+(σ12)2).\displaystyle=\beta\left((\sigma\_{22})^{2}+(\sigma\_{12})^{2}\right). |  |

Since σ12=ρσ​σ11​σ22\sigma\_{12}=\rho\_{\sigma}\sqrt{\sigma\_{11}\sigma\_{22}}, increasing ρσ\rho\_{\sigma} reduces the mortality intensity by increasing σ12\sigma\_{12}, which subsequently increases ω11\omega\_{11} and ω22\omega\_{22} and hence leads to an increase in the option price.

In stark contrast, the relationship between the option price and α\alpha is notably non-linear and decreasing. A mere 10% drop in α\alpha from 0.04 to 0.036 results in an almost five-fold surge in the option price, underscoring α\alpha as a pivotal parameter in the linear-rational Wishart model. This parameter is from the potential approach of Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates")) which dictates to specify the state-price density first, and then get mortality dynamics that are consistent with the specified state-price density, contrasted to the standard method of specifying mortality intensities first and then derive the state-price density. Since the state-price density is specified first, we are able to enforce positive mortality intensities, a significant advantage of our model and approach. Previous models either struggled with ensuring positive mortality intensities or lacked a versatile correlation structure. Although at first glance, changes in the option price due to α\alpha should be linear, as seen in ([23](https://arxiv.org/html/2602.06415v1#S4.E23 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"))-([24](https://arxiv.org/html/2602.06415v1#S4.E24 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), it is essential to realise that α\alpha influences the option price at multiple points, as evident from ([32](https://arxiv.org/html/2602.06415v1#S5.E32 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"))-([34](https://arxiv.org/html/2602.06415v1#S5.E34 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), amplifying its impact.

Lastly, the relationship with TT is non-linear and decreasing. This decrease is intuitive: annuitants have a higher mortality risk over extended periods. The non-linearity stems from the fact that the option’s expiry date, TT, affects the pricing equation at various stages, leading to a cumulative effect on the option price.

### 6.2 Approximation methods

Figure [2](https://arxiv.org/html/2602.06415v1#S8.F2 "Figure 2 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") showcases the effectiveness of the three approximation methods introduced in Proposition [5.3](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem3 "Proposition 5.3. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), Proposition [5.5](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem5 "Proposition 5.5. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") and Proposition [5.7](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem7 "Proposition 5.7. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") benchmarked against the characteristic function approach across various strike values. Notably, the gamma approximation from Proposition [5.7](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem7 "Proposition 5.7. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") outperforms the Gaussian approximation of Proposition [5.3](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem3 "Proposition 5.3. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") and the spectral decomposition approximation outlined in Proposition [5.5](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem5 "Proposition 5.5. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). The right panel of Figure [2](https://arxiv.org/html/2602.06415v1#S8.F2 "Figure 2 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") reveals that the absolute percentage error for the gamma method is consistently lower than the Gaussian and the spectral decomposition approximation errors. Logically, this makes sense. The asymptotic distribution of the Wishart process is a matrix gamma distribution, and thus for the scalar gamma approximation to do well is of no surprise. Interestingly, while the Gaussian approximation tends to over-estimate the option price, the spectral decomposition approximation tends to under-estimate it, while the gamma approximation initially over-estimates at low strikes and under-estimates at higher strikes, albeit very slightly. However, the Gaussian and spectral approximation methods display enhanced accuracy as the guaranteed survival annuity rate gg rises, i.e., when the option is moving in-the-money.

Even though the gamma approximation method outperforms the Gaussian and spectral methods for these numerical examples, in other parameters the other methods may outperform the gamma method. For example, if one eigenvalue of a4a\_{4} from ([34](https://arxiv.org/html/2602.06415v1#S5.E34 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) dominates its other eigenvalues then it is possible for the spectral method to perform the best. Similarly, if we are examining a problem where some of the eigenvalues are positive and some are negative, then the Gaussian approximation may perform the best.
Nevertheless, the predominant benefit of these approximation methods is their rapid computational capability, with the Gaussian and gamma approximations being especially efficient. These approximations only necessitate computations of constants and the use of the Gaussian cumulative distribution and density functions or the gamma functions, which are inherently swift.

[ Insert Figure [2](https://arxiv.org/html/2602.06415v1#S8.F2 "Figure 2 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") here ]

### 6.3 Independence vs dependence

To underscore the model risk associated with assumptions about dependencies between annuitants, we examine the differences between the outcomes when assuming either independence or dependence. Figure [3](https://arxiv.org/html/2602.06415v1#S8.F3 "Figure 3 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") showcases the option price under two scenarios:

1. 1.

   A positive correlation between the two annuitants’ mortality rates, reflected by the model parameters in Table [1](https://arxiv.org/html/2602.06415v1#S8.T1 "Table 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") (shown as blue solid).
2. 2.

   An assumption of independence between the two annuitants’ mortalities (shown as red dashed).

In the second scenario, independence is represented by setting ρσ=0\rho\_{\sigma}=0. This results in the quadratic covariation between the normalised mortality intensities d​⟨μx∗​(⋅),μy∗​(⋅)⟩s=0d\langle\mu\_{x}^{\*}(\cdot),\mu\_{y}^{\*}(\cdot)\rangle\_{s}=0, as seen in ([48](https://arxiv.org/html/2602.06415v1#S6.E48 "In 6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")).131313While d​⟨μx∗​(⋅),μy∗​(⋅)⟩s=0d\langle\mu\_{x}^{\*}(\cdot),\mu\_{y}^{\*}(\cdot)\rangle\_{s}=0, it is crucial to understand that the mortality intensities of the annuitants will not be independent. As depicted in ([23](https://arxiv.org/html/2602.06415v1#S4.E23 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"))-([24](https://arxiv.org/html/2602.06415v1#S4.E24 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), both individual mortalities rely on the common denominator 1+tr⁡[u0​vs]1+\operatorname{tr}[u\_{0}v\_{s}]. Thus, they cannot be mutually independent through the setting of ρσ=0\rho\_{\sigma}=0 alone. By adjusting ρσ\rho\_{\sigma}, we can approximate independence by nullifying the quadratic covariation between μx∗​(s)\mu\_{x}^{\*}(s) and μy∗​(s)\mu\_{y}^{\*}(s). But, setting σ12\sigma\_{12} to zero indirectly alters the quadratic variations of v11,sv\_{11,s} and v22,sv\_{22,s} as seen in ([16](https://arxiv.org/html/2602.06415v1#S3.E16 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). To account for this, we introduce a new process v~\tilde{v} built upon the parameters in Table [1](https://arxiv.org/html/2602.06415v1#S8.T1 "Table 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), from which we compute our independent option price on, except for the matrix σ\sigma, which is modified to σi​n​d\sigma^{ind}, defined by:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σ11i​n​d\displaystyle\sigma\_{11}^{ind} | =(σ11)2+(σ12)2,\displaystyle=\sqrt{\left(\sigma\_{11}\right)^{2}+\left(\sigma\_{12}\right)^{2}}, |  | (49) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σ22i​n​d\displaystyle\sigma\_{22}^{ind} | =(σ22)2+(σ12)2,\displaystyle=\sqrt{\left(\sigma\_{22}\right)^{2}+\left(\sigma\_{12}\right)^{2}}, |  | (50) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σ12i​n​d\displaystyle\sigma\_{12}^{ind} | =0.\displaystyle=0. |  | (51) |

With these adjustments, d​⟨v~11,.,v~11,.⟩s/v~11,sd\langle\tilde{v}\_{11,.},\tilde{v}\_{11,.}\rangle\_{s}/\tilde{v}\_{11,s} aligns with d​⟨v11,.,v11,.⟩s/v11,sd\langle v\_{11,.},v\_{11,.}\rangle\_{s}/v\_{11,s}, and d​⟨v~22,.,v~22,.⟩s/v~22,sd\langle\tilde{v}\_{22,.},\tilde{v}\_{22,.}\rangle\_{s}/\tilde{v}\_{22,s} aligns with d​⟨v22,.,v22,.⟩s/v22,sd\langle v\_{22,.},v\_{22,.}\rangle\_{s}/v\_{22,s}. The key distinction is that d​⟨v~11,.,v~22,.⟩s=0d\langle\tilde{v}\_{11,.},\tilde{v}\_{22,.}\rangle\_{s}=0, unlike the positive, non-zero value of d​⟨v11,.,v22,.⟩sd\langle v\_{11,.},v\_{22,.}\rangle\_{s}.

From Figure [3](https://arxiv.org/html/2602.06415v1#S8.F3 "Figure 3 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), it is evident that the option price, when assuming independence, is consistently lower than when accounting for positive dependence between the annuitants’ mortality rates. This is logically consistent: the probability of both annuitants being alive is higher under positive dependence than under independence. Furthermore, the discrepancy in prices can be substantial, with the absolute percentage error reaching up to 40% when the guaranteed survival annuity rate gg is minimal. This underscores the significance of precisely modelling dependency, given its potential economic implications. This result extends previous findings showing the importance of mortality dependence on longevity derivatives, see Frees et al. ([1996](https://arxiv.org/html/2602.06415v1#bib.bib40 "Annuity valuation with dependent mortality")) for joint / last survivor survival annuities, Wang et al. ([2015](https://arxiv.org/html/2602.06415v1#bib.bib19 "Modeling multi-country mortality dependence and its application in pricing survivor index swaps—a dynamic copula approach")) for longevity bonds or Yang and Wang ([2013](https://arxiv.org/html/2602.06415v1#bib.bib54 "Pricing and securitization of multi-country longevity risk with mortality dependence")) for the survivor swaps.141414Needless to say that any work looking at reducing longevity risks through (cross) hedging relies on this dependence, see for example Zhou ([2019](https://arxiv.org/html/2602.06415v1#bib.bib57 "Modelling mortality dependence with regime-switching copulas")).

[ Insert Figure [3](https://arxiv.org/html/2602.06415v1#S8.F3 "Figure 3 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") here ]

## 7 Conclusion

In this paper, we introduce the linear-rational Wishart mortality model, marking a significant departure from traditional mortality models. One of the prominent features of our model is the integration of the Wishart process coupled with the potential approach delineated by Rogers ([1997](https://arxiv.org/html/2602.06415v1#bib.bib83 "The potential approach to the term structure of interest rates and foreign exchange rates")). This combination provides a versatile framework, enabling a comprehensive dependency between mortality intensities. Notably, these intensities remain positive inherently, offering a clear advantage over prior models that either struggled to ensure this positivity or were lacking in a general correlation structure.

A pivotal contribution lies in the derivation of closed-form solutions for both the joint survival annuity and the guaranteed joint survival annuity option, made possible through leveraging the strong analytical properties of the Wishart process and the linear-rational structure of the model. The density of the joint survival annuity is known, so that risk indicators can be easily computed. For the guaranteed joint survival annuity option price, its computation only requires a one-dimensional integration. Further building on the analytical properties of the Wishart process, we introduce three unique approximation techniques tailored for pricing the guaranteed joint survival annuity option. The first employs the cumulants of the Wishart process and approximates its density by a perturbation of the Gaussian distribution, the second is rooted in the spectral decomposition and the third approximation is based on a perturbation of the gamma distribution. All three approximations work well, with them providing reasonably accurate results and their swift numerical implementations make them particularly valuable for practical applications in pricing of the guaranteed joint survival annuity option.

Looking ahead, there are several avenues for extension and refinement. The first is certainly the estimation of the model, where the density as well as the moments of the joint survival annuity will certainly be important. Note that the model parameters are matrices with some algebraic properties that require adapted optimisation procedures. Moreover, given the analytical attributes of our model, deriving option Greeks presents as a logical next step that will complement the risk management indicators presented in this work, further strengthening the practical applicability of our model.

The inherent flexibility of our linear-rational Wishart mortality model extends beyond the confines of our current investigation. Its generic framework is adaptable to multi-population, multi-cohort, and even cross-asset type challenges. The derivations and results showcased in this paper could be expanded to embrace these diverse frameworks.

## Declarations

* •

  The authors contributed equally to this work.
* •

  The authors report there are no competing interests to declare.
* •

  Data availability: Not applicable.
* •

  Funding organizations: Not applicable.

## References

* A. Alfonsi (2015)
  Affine diffusions and related processes: simulation, theory and applications.
  1 edition, Springer-Verlag.
  External Links: [Document](https://dx.doi.org/10.1007/978-3-319-05221-2)
  Cited by: [§3](https://arxiv.org/html/2602.06415v1#S3.p3.1 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* N. Bäuerle and Z. Li (2013)
  Optimal portfolios for financial markets with Wishart volatility.
  Journal of Applied Probability 50 (4),  pp. 1025–1043.
  External Links: [Document](https://dx.doi.org/10.1239/jap/1389370097)
  Cited by: [footnote 2](https://arxiv.org/html/2602.06415v1#footnote2 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* E. Bayraktar, M. A. Milevsky, S. D. Promislow, and V. R. Young (2009)
  Valuation of mortality risk via the instantaneous Sharpe ratio: Applications to life annuities.
  Journal of Economic Dynamics and Control 33 (3),  pp. 676–691.
  External Links: [Document](https://dx.doi.org/10.1016/j.jedc.2008.09.004)
  Cited by: [§2](https://arxiv.org/html/2602.06415v1#S2.p3.10 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* E. Biffis and P. Millossovich (2006)
  The fair value of guaranteed annuity options.
  Scandinavian Actuarial Journal 2006 (1),  pp. 23–41.
  External Links: [Document](https://dx.doi.org/10.1080/03461230500462204)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p2.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p11.1 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* E. Biffis (2005)
  Affine processes for dynamic mortality and actuarial valuations.
  Insurance: Mathematics and Economics 37 (),  pp. 443–468.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2005.05.003)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p1.20 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p5.10 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p6.11 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p7.11 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p7.2 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [Remark 4.2](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem2.p1.4.4 "Remark 4.2. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* T. Björk (2009)
  Arbitrage theory in continuous time.
  3rd edition, Oxford University Press, Oxford.
  Cited by: [§4](https://arxiv.org/html/2602.06415v1#S4.p3.10 "4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* N. Branger, M. Muck, F. T. Seifried, and S. Weisheit (2017)
  Optimal portfolios when variances and covariances can jump.
  Journal of Economic Dynamics and Control 85,  pp. 59–89.
  External Links: [Document](https://dx.doi.org/10.1016/j.jedc.2017.09.008)
  Cited by: [footnote 2](https://arxiv.org/html/2602.06415v1#footnote2 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* M. F. Bru (1991)
  Wishart processes.
  Journal of Theoretical Probability 4 (4),  pp. 725–751.
  External Links: [Document](https://dx.doi.org/10.1007/BF01259552)
  Cited by: [§3](https://arxiv.org/html/2602.06415v1#S3.p1.4 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§3](https://arxiv.org/html/2602.06415v1#S3.p1.45 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§3](https://arxiv.org/html/2602.06415v1#S3.p2.7 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§3](https://arxiv.org/html/2602.06415v1#S3.p3.1 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* A. J. G. Cairns (2004)
  Interest rate models: an introduction.
   Princeton University Press.
  Cited by: [§4](https://arxiv.org/html/2602.06415v1#S4.p3.10 "4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* C. Ceci, K. Colaneri, and A. Cretarola (2015)
  Hedging of unit-linked life insurance contracts with unobservable mortality hazard rate via local risk-minimization.
  Insurance: Mathematics and Economics 60,  pp. 47–60.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2014.10.013)
  Cited by: [§2](https://arxiv.org/html/2602.06415v1#S2.p3.10 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* C. Chiarella, J. Da Fonseca, and M. Grasselli (2014)
  Pricing range notes within Wishart affine models.
  Insurance: Mathematics and Economics 58,  pp. 193–203.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2014.07.008)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p3.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* P. Collin-Dufresne and R. Goldstein (2002)
  Pricing swaptions within an affine framework.
  Journal of Derivatives 3 (1-2),  pp. 167–179.
  External Links: [Document](https://dx.doi.org/10.3905/jod.2002.319187)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p3.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§5](https://arxiv.org/html/2602.06415v1#S5.p5.1 "5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* S. Crépey, A. Macrina, T. M. Nguyen, and D. Skovmand (2015)
  Rational multi-curve models with counterparty-risk valuation adjustments.
  Quantitative Finance 16 (6),  pp. 847–866.
  External Links: [Document](https://dx.doi.org/10.1080/14697688.2015.1095348)
  Cited by: [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* C. Cuchiero, D. Filipović, E. Mayerhofer, and J. Teichmann (2011)
  Affine processes on positive semidefinite matrices.
  The Annals of Applied Probability 21 (2),  pp. 397–463.
  External Links: [Document](https://dx.doi.org/10.1214/10-AAP710)
  Cited by: [§3](https://arxiv.org/html/2602.06415v1#S3.p2.4 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* C. Cuchiero, C. Fontana, and A. Gnoatto (2019)
  Affine multiple yield curve models.
  Mathematical Finance 29 (2),  pp. 568–611.
  External Links: [Document](https://dx.doi.org/10.1111/mafi.12183)
  Cited by: [footnote 2](https://arxiv.org/html/2602.06415v1#footnote2 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* J. Da Fonseca, K. E. Dawui, and Y. Malevergne (2022)
  A linear-rational multi-curve term structure model with stochastic spread.
  SSRN-eLibrary.
  Note: Working paper
  External Links: [Document](https://dx.doi.org/10.2139/ssrn.4176102)
  Cited by: [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* J. Da Fonseca, M. Grasselli, and C. Tebaldi (2007)
  Option pricing when correlations are stochastic: An analytical framework.
  Review of Derivatives Research 10 (2),  pp. 151–180.
  External Links: [Document](https://dx.doi.org/10.1007/s11147-008-9018-x)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p2.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§1](https://arxiv.org/html/2602.06415v1#S1.p3.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 2](https://arxiv.org/html/2602.06415v1#footnote2 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* J. Da Fonseca (2024)
  Pricing guaranteed annuity options in a linear-rational Wishart mortality model.
  Insurance: Mathematics and Economics 115 (),  pp. 122–131.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2024.01.004)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p3.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [Remark 3.2](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem2.p1.2.2 "Remark 3.2. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§3](https://arxiv.org/html/2602.06415v1#S3.p3.1 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [Remark 4.2](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem2.p1.4.4 "Remark 4.2. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [Remark 4.6](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem6.p1.1.1 "Remark 4.6. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§4](https://arxiv.org/html/2602.06415v1#S4.p2.3 "4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§5](https://arxiv.org/html/2602.06415v1#S5.p3.1 "5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 1](https://arxiv.org/html/2602.06415v1#footnote1 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 4](https://arxiv.org/html/2602.06415v1#footnote4 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 7](https://arxiv.org/html/2602.06415v1#footnote7 "In 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* M. Dahl and T. Møller (2006)
  Valuation and hedging of life insurance liabilities with systematic mortality risk.
  Insurance: Mathematics and Economics 39 (2),  pp. 193–217.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2006.02.007)
  Cited by: [§2](https://arxiv.org/html/2602.06415v1#S2.p3.10 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* M. Dahl (2004)
  Stochastic mortality in life insurance: Market reserves and mortality-linked insurance contracts.
  Insurance: Mathematics and Economics 35 (1),  pp. 113–136.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2004.05.003)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§1](https://arxiv.org/html/2602.06415v1#S1.p2.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p1.20 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p5.10 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [Remark 4.2](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem2.p1.4.4 "Remark 4.2. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* D. De Giovanni, M. Pirra, and F. Viviano (2025)
  Joint mortality models based on subordinated linear hypercubes.
  ASTIN Bulletin 55 (2),  pp. 332–351.
  External Links: [Document](https://dx.doi.org/10.1017/asb.2025.8)
  Cited by: [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* G. Deelstra, M. Grasselli, and C. Van Weverberg (2016)
  The role of the dependence between mortality and interest rates when pricing guaranteed annuity options.
  Insurance: Mathematics and Economics 71,  pp. 205–219.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2016.09.010)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p3.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p2.13 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p3.10 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p3.4 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p7.11 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§2](https://arxiv.org/html/2602.06415v1#S2.p9.14 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§3](https://arxiv.org/html/2602.06415v1#S3.p6.1 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 1](https://arxiv.org/html/2602.06415v1#footnote1 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* D. Duffie and R. Kan (1996)
  A yield-factor model of interest rates.
  Mathematical Finance 6 (4),  pp. 379–406.
  External Links: [Document](https://dx.doi.org/10.1111/j.1467-9965.1996.tb00123.x)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§1](https://arxiv.org/html/2602.06415v1#S1.p2.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* D. Duffie, D. Filipović, and W. Schachermayer (2003)
  Affine processes and applications in finance.
  The Annals of Applied Probability 13 (3),  pp. 984 – 1053.
  External Links: [Document](https://dx.doi.org/10.1214/aoap/1060202833)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p2.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* B. A. Faraz, H. Arian, and M. Escobar-Anel (2025)
  Markov-modulated and shifted Wishart processes with applications in derivatives pricing.
  International Journal of Financial Studies 13 (2).
  External Links: [Document](https://dx.doi.org/10.3390/ijfs13020091)
  Cited by: [footnote 2](https://arxiv.org/html/2602.06415v1#footnote2 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* D. Filipović, M. Larsson, and A. B. Trolle (2017)
  Linear-rational term structure models.
  The Journal of Finance 72 (2),  pp. 655–704.
  External Links: [Document](https://dx.doi.org/10.1111/jofi.12488)
  Cited by: [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* D. Filipović, E. Mayerhofer, and P. Schneider (2013)
  Density approximations for multivariate affine jump-diffusion processes.
  Journal of Econometrics 176 (2),  pp. 93–111.
  External Links: [Document](https://dx.doi.org/10.1016/j.jeconom.2012.12.003)
  Cited by: [Proof of Proposition 5.7 .](https://arxiv.org/html/2602.06415v1#Ax1.9.p1.19 "Proof of Proposition 5.7 . ‣ Supplementary Appendix ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [Proof of Proposition 5.7 .](https://arxiv.org/html/2602.06415v1#Ax1.9.p1.27 "Proof of Proposition 5.7 . ‣ Supplementary Appendix ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [Proof of Proposition 5.7 .](https://arxiv.org/html/2602.06415v1#Ax1.9.p1.34 "Proof of Proposition 5.7 . ‣ Supplementary Appendix ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§1](https://arxiv.org/html/2602.06415v1#S1.p3.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§5](https://arxiv.org/html/2602.06415v1#S5.p10.15 "5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* E. W. Frees, J. Carriere, and E. Valdez (1996)
  Annuity valuation with dependent mortality.
  The Journal of Risk and Insurance 63 (2),  pp. 229–261.
  External Links: [Document](https://dx.doi.org/10.2307/253744)
  Cited by: [§6.3](https://arxiv.org/html/2602.06415v1#S6.SS3.p3.1 "6.3 Independence vs dependence ‣ 6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§6](https://arxiv.org/html/2602.06415v1#S6.p9.3 "6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* A. Gnoatto and M. Grasselli (2014)
  The explicit laplace transform for the Wishart process.
  Journal of Applied Probability 51 (3),  pp. 640–656.
  External Links: [Document](https://dx.doi.org/10.1239/jap/1409932664)
  Cited by: [footnote 2](https://arxiv.org/html/2602.06415v1#footnote2 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* A. Gnoatto (2012)
  The Wishart short rate model.
  International Journal of Theoretical and Applied Finance 15 (08),  pp. 1250056.
  External Links: [Document](https://dx.doi.org/10.1142/S0219024912500562)
  Cited by: [footnote 2](https://arxiv.org/html/2602.06415v1#footnote2 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* C. Gouriéroux and R. Sufana (2010)
  Derivative pricing with multivariate stochastic volatility.
  Journal of Business and Economic Statistics 28 (3),  pp. 438–451.
  External Links: [Document](https://dx.doi.org/10.1198/jbes.2009.08105)
  Cited by: [footnote 2](https://arxiv.org/html/2602.06415v1#footnote2 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* C. Gouriéroux and R. Sufana (2011)
  Discrete time Wishart term structure models.
  Journal of Economic Dynamics and Control 35 (6),  pp. 815–824.
  External Links: [Document](https://dx.doi.org/10.1016/j.jedc.2011.01.007)
  Cited by: [footnote 2](https://arxiv.org/html/2602.06415v1#footnote2 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* M. Grasselli and C. Tebaldi (2008)
  Solvable affine term structure models.
  Mathematical Finance 18 (1),  pp. 135–153.
  External Links: [Document](https://dx.doi.org/10.1111/j.1467-9965.2007.00325.x)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p3.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§3](https://arxiv.org/html/2602.06415v1#S3.p3.1 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* A.K. Gupta and D.K. Nagar (2000)
  Matrix variate distributions.
   Chapman & Hall/CRC.
  Cited by: [§3](https://arxiv.org/html/2602.06415v1#S3.p4.1 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* J. Gurland (1948)
  Inversion formulae for the distribution of ratios.
  Annals of Mathematical Statistics 19 (2),  pp. 228–237.
  External Links: [Document](https://dx.doi.org/10.1214/aoms/1177730247)
  Cited by: [Proof of Proposition 4.4 .](https://arxiv.org/html/2602.06415v1#Ax1.2.p1.7 "Proof of Proposition 4.4 . ‣ Supplementary Appendix ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [Proof of Proposition 4.8 .](https://arxiv.org/html/2602.06415v1#Ax1.3.p1.5 "Proof of Proposition 4.8 . ‣ Supplementary Appendix ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§4](https://arxiv.org/html/2602.06415v1#S4.p5.1 "4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* D. Hainaut (2023)
  A calendar year mortality model in continuous time.
  ASTIN Bulletin 53 (2),  pp. 351–376.
  External Links: [Document](https://dx.doi.org/10.1017/asb.2023.2)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* Y. Huang, J. T. Tsai, S. S. Yang, and H. Cheng (2014)
  Price bounds of mortality-linked security in incomplete insurance market.
  Insurance: Mathematics and Economics 55,  pp. 30–39.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2013.11.008)
  Cited by: [§2](https://arxiv.org/html/2602.06415v1#S2.p3.10 "2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* Z. Huang, M. Sherris, A. M. Villegas, and J. Ziveyi (2022)
  Modelling USA age-cohort mortality: A comparison of multi-factor affine mortality models.
  Risks 10 (9).
  External Links: [Document](https://dx.doi.org/10.3390/risks10090183)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* R. Jarrow and A. Rudd (1982)
  Approximate option valuation for arbitrary stochastic processes.
  Journal of Financial Economics 10 (3),  pp. 347–369.
  External Links: [Document](https://dx.doi.org/10.1016/0304-405X%2882%2990007-1)
  Cited by: [§5](https://arxiv.org/html/2602.06415v1#S5.p5.1 "5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* P. Jevtić and T.R. Hurd (2017)
  The joint mortality of couples in continuous time.
  Insurance: Mathematics and Economics 75,  pp. 90–97.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2017.05.002)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* P. Jevtić, E. Luciano, and E. Vigna (2013)
  Mortality surface by means of continuous time cohort models.
  Insurance: Mathematics and Economics 53 (1),  pp. 122–133.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2013.04.005)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* P. Jevtić and L. Regis (2019)
  A continuous-time stochastic model for the mortality surface of multiple populations.
  Insurance: Mathematics and Economics 88,  pp. 181–195.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2019.07.001)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* G. La Bua and D. Marazzina (2022)
  A new class of multidimensional Wishart-based hybrid models.
  Decisions in Economics and Finance 45 (1),  pp. 209–239.
  External Links: [Document](https://dx.doi.org/10.1007/s10203-021-00357-4)
  Cited by: [footnote 2](https://arxiv.org/html/2602.06415v1#footnote2 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* G. Letac and H. Massam (2008)
  The noncentral Wishart as an exponential family, and its moments.
  Journal of Multivariate Analysis 99 (7),  pp. 1393–1417.
  External Links: [Document](https://dx.doi.org/10.1016/j.jmva.2008.04.006)
  Cited by: [§5](https://arxiv.org/html/2602.06415v1#S5.p4.1 "5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§5](https://arxiv.org/html/2602.06415v1#S5.p7.1 "5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* K. S. Leung, H. Y. Wong, and H. Y. Ng (2013)
  Currency option pricing with Wishart process.
  Journal of Computational and Applied Mathematics 238,  pp. 156–170.
  External Links: [Document](https://dx.doi.org/10.1016/j.cam.2012.08.029)
  Cited by: [footnote 2](https://arxiv.org/html/2602.06415v1#footnote2 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* H. Li, H. Liu, Q. Tang, and Z. Yuan (2023)
  Pricing extreme mortality risk in the wake of the COVID-19 pandemic.
  Insurance: Mathematics and Economics 108,  pp. 84–106.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2022.11.002)
  Cited by: [§6](https://arxiv.org/html/2602.06415v1#S6.p5.8 "6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 10](https://arxiv.org/html/2602.06415v1#footnote10 "In 6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* E. Mayerhofer, O. Pfaffel, and R. Stelzer (2011)
  On strong solutions of positive definite jump-diffusions.
  Stochastic Processes and Their Applications 121 (9),  pp. 2072–2086.
  External Links: [Document](https://dx.doi.org/10.1016/j.spa.2011.05.006)
  Cited by: [§3](https://arxiv.org/html/2602.06415v1#S3.p2.4 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* T. A. Nguyen and F. T. Seifried (2015)
  The multi-curve potential model.
  International Journal of Theoretical and Applied Finance 18 (7),  pp. 1550049.
  External Links: [Document](https://dx.doi.org/10.1142/S0219024915500491)
  Cited by: [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* T. A. Nguyen and F. T. Seifried (2021)
  The affine rational potential model.
  International Journal of Theoretical and Applied Finance 24 (06n07),  pp. 2150031.
  External Links: [Document](https://dx.doi.org/10.1142/S021902492150031X)
  Cited by: [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* L. C. G. Rogers (1997)
  The potential approach to the term structure of interest rates and foreign exchange rates.
  Mathematical Finance 7 (2),  pp. 157–176.
  External Links: [Document](https://dx.doi.org/10.1111/1467-9965.00029)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§1](https://arxiv.org/html/2602.06415v1#S1.p3.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§3](https://arxiv.org/html/2602.06415v1#S3.p10.13 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§3](https://arxiv.org/html/2602.06415v1#S3.p12.5 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§3](https://arxiv.org/html/2602.06415v1#S3.p9.1 "3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [Remark 4.2](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem2.p1.4.4 "Remark 4.2. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§4](https://arxiv.org/html/2602.06415v1#S4.p3.10 "4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§6.1](https://arxiv.org/html/2602.06415v1#S6.SS1.p2.5 "6.1 Sensitivity analyses ‣ 6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§7](https://arxiv.org/html/2602.06415v1#S7.p1.1 "7 Conclusion ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 3](https://arxiv.org/html/2602.06415v1#footnote3 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* F. Ungolo, L. P. D. M. Garces, M. Sherris, and Y. Zhou (2023)
  Estimation, comparison, and projection of multifactor age–cohort affine mortality models.
  North American Actuarial Journal 0 (0),  pp. 1–23.
  External Links: [Document](https://dx.doi.org/10.1080/10920277.2023.2238793)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* C. Wang, S. S. Yang, and H. Huang (2015)
  Modeling multi-country mortality dependence and its application in pricing survivor index swaps—a dynamic copula approach.
  Insurance: Mathematics and Economics 63,  pp. 30–39.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2015.03.019)
  Cited by: [§6.3](https://arxiv.org/html/2602.06415v1#S6.SS3.p3.1 "6.3 Independence vs dependence ‣ 6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* J. Xu, X. Chen, and Y. Yang (2024)
  Pricing longevity bond with affine-jump-diffusion multi-cohort mortality model.
  Journal of Computational and Applied Mathematics 446,  pp. 115800.
  External Links: [Document](https://dx.doi.org/10.1016/j.cam.2024.115800)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* Y. Xu, M. Sherris, and J. Ziveyi (2020)
  Continuous-time multi-cohort mortality modelling with affine processes.
  Scandinavian Actuarial Journal 2020 (6),  pp. 526–552.
  External Links: [Document](https://dx.doi.org/10.1080/03461238.2019.1696223)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [§6](https://arxiv.org/html/2602.06415v1#S6.p5.8 "6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"),
  [footnote 11](https://arxiv.org/html/2602.06415v1#footnote11 "In 6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* S. S. Yang and C. Wang (2013)
  Pricing and securitization of multi-country longevity risk with mortality dependence.
  Insurance: Mathematics and Economics 52 (2),  pp. 157–169.
  External Links: [Document](https://dx.doi.org/10.1016/j.insmatheco.2012.10.004)
  Cited by: [§6.3](https://arxiv.org/html/2602.06415v1#S6.SS3.p3.1 "6.3 Independence vs dependence ‣ 6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* F. Zeddouk and P. Devolder (2020)
  Longevity modelling and pricing under a dependent multi-cohort framework.
  Risks 8 (4).
  External Links: [Document](https://dx.doi.org/10.3390/risks8040121)
  Cited by: [§1](https://arxiv.org/html/2602.06415v1#S1.p1.1 "1 Introduction ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").
* R. Zhou (2019)
  Modelling mortality dependence with regime-switching copulas.
  ASTIN Bulletin: The Journal of the IAA 49 (2),  pp. 373–407.
  External Links: [Document](https://dx.doi.org/10.1017/asb.2019.10)
  Cited by: [footnote 14](https://arxiv.org/html/2602.06415v1#footnote14 "In 6.3 Independence vs dependence ‣ 6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

## 8 Figures and Tables

Table 1: Wishart model parameter values.

| Variable | Value |
| --- | --- |
| α\alpha | 0.04 |
| rr | 0 |
| β\beta | 3.5 |
| ρσ\rho\_{\sigma} | 0.5 |
| σ12\sigma\_{12} | ρσ​0.06×0.04\rho\_{\sigma}\sqrt{0.06\times 0.04} |
| σ\sigma | (0.06σ12σ120.04)\begin{pmatrix}0.06&\sigma\_{12}\\ \sigma\_{12}&0.04\end{pmatrix} |
| mm | (−100−1)\begin{pmatrix}-1&0\\ 0&-1\end{pmatrix} |
| v12v\_{12} | 0.5 0.005×0.0025\sqrt{0.005\times 0.0025} |
| v0v\_{0} | (0.005v12v120.0025)\begin{pmatrix}0.005&v\_{12}\\ v\_{12}&0.0025\end{pmatrix} |
| u1u\_{1} | (1000)\begin{pmatrix}1&0\\ 0&0\end{pmatrix} |
| u2u\_{2} | (0001)\begin{pmatrix}0&0\\ 0&1\end{pmatrix} |

Note. This table contains the model parameters used for our numerical experiments in Section [6](https://arxiv.org/html/2602.06415v1#S6 "6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").




Table 2: Guaranteed joint survival annuity option parameters.

| Variable | Value |
| --- | --- |
| T−tT-t | 2 |
| TN−tT\_{N}-t | 5 |
| gg | 0.225 |
| zz | −0.025-0.025 |

Note. This table contains the parameters that our analyses on the guaranteed joint survival annuity option prices are centered on. The option is exercisable in T−t=2T-t=2 years, with a joint survival annuity payable yearly for TN−t=5T\_{N}-t=5 years and guaranteed joint survival annuity rate g=0.225g=0.225 which is chosen so the option is approximately at-the-money based on the parameters in Table [1](https://arxiv.org/html/2602.06415v1#S8.T1 "Table 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").




Table 3: Moments of μx​(T)\mu\_{x}(T) and μy​(T)\mu\_{y}(T).

| T−tT-t | 1 | 2 | 5 | 10 |
| --- | --- | --- | --- | --- |
| 𝔼t​[μx​(T)]\mathbb{E}\_{t}[\mu\_{x}(T)] | 0.0193 | 0.0199 | 0.0200 | 0.0200 |
| Var⁡(μx​(T))\operatorname{Var}(\mu\_{x}(T)) | 1.06×10−41.06\times 10^{-4} | 1.20×10−41.20\times 10^{-4} | 1.20×10−41.20\times 10^{-4} | 1.20×10−41.20\times 10^{-4} |
| 𝔼t​[μy​(T)]\mathbb{E}\_{t}[\mu\_{y}(T)] | 0.0195 | 0.0198 | 0.0198 | 0.0198 |
| Var⁡(μy​(T))\operatorname{Var}(\mu\_{y}(T)) | 2.59×10−52.59\times 10^{-5} | 2.83×10−52.83\times 10^{-5} | 2.86×10−52.86\times 10^{-5} | 2.86×10−52.86\times 10^{-5} |

Note. This table contains the expectation and variance of μx​(T)\mu\_{x}(T) and μy​(T)\mu\_{y}(T) computed at the values of T−t=1,2,5,10T-t=1,2,5,10. The moments were numerically calculated using ([27](https://arxiv.org/html/2602.06415v1#S4.E27 "In Corollary 4.5. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")).




Figure 1: Sensitivity analyses.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

![Refer to caption](x5.png)

![Refer to caption](x6.png)

Note. Each panel displays the sensitivity analysis of the guaranteed joint survival annuity option price with respect to different parameters. The top left panel displays α\alpha. Top right panel displays β\beta. Middle left panel displays ρ\rho. Middle right panel displays m11m\_{11}. Bottom left panel displays σ11\sigma\_{11}. Bottom right panel displays TT, the exercise date of the guaranteed joint survival annuity option.




Figure 2: Comparison of approximation methods and errors.

![Refer to caption](x7.png)

![Refer to caption](x8.png)

Note. The left panel displays the guaranteed joint survival annuity option price across different strikes for different pricing methods: Characteristic function (blue solid), Gaussian approximation (green dotted), the spectral decomposition approximation (red dashed), and the gamma approximation (purple dotted-dashed). The right panel showcases the absolute percentage errors (%) with respect to the characteristic function pricer across different strikes associated with the Gaussian approximation (green dotted), the spectral decomposition approximation (red dashed), and the gamma approximation (purple dotted-dashed).




Figure 3: Pricing difference for independence and dependence assumption.

![Refer to caption](x9.png)

Note. This panel displays the guaranteed joint survival annuity option price across different strikes under two different pricing assumptions: Dependence between annuitants given by the parameters outlined in Table [1](https://arxiv.org/html/2602.06415v1#S8.T1 "Table 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") and independence between annuitants which is also based on Table [1](https://arxiv.org/html/2602.06415v1#S8.T1 "Table 1 ‣ 8 Figures and Tables ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") but with the matrix σ\sigma defined by ([49](https://arxiv.org/html/2602.06415v1#S6.E49 "In 6.3 Independence vs dependence ‣ 6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"))-([51](https://arxiv.org/html/2602.06415v1#S6.E51 "In 6.3 Independence vs dependence ‣ 6 Model implementation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")).

## Supplementary Appendix

###### Proof of Proposition [4.1](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") .

Using ([4](https://arxiv.org/html/2602.06415v1#S2.E4 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and the change of probability measure ([18](https://arxiv.org/html/2602.06415v1#S3.E18 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and the expression for the state-price density ([18](https://arxiv.org/html/2602.06415v1#S3.E18 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | SB0​(t,T)\displaystyle\mathrm{SB}\_{0}(t,T) | =𝔼tℚ​[e−∫tT(μx​(s)+μy​(s))​𝑑s]\displaystyle=\mathbb{E}\_{t}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}(\mu\_{x}(s)+\mu\_{y}(s))ds}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼t​[ζTζt]\displaystyle=\mathbb{E}\_{t}\left[\frac{\zeta\_{T}}{\zeta\_{t}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e−α​(T−t)​1+𝔼t​[tr​[u0​vT]]1+tr​[u0​vt],\displaystyle=e^{-\alpha(T-t)}\frac{1+\mathbb{E}\_{t}[\textup{tr}[u\_{0}v\_{T}]]}{1+\textup{tr}[u\_{0}v\_{t}]}, |  |

and we conclude using Lemma [3.3](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") with u0u\_{0}.
∎

###### Proof of Proposition [4.4](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") .

Define x1=c1+tr​[h1​vT]\mathrm{x}\_{1}=c\_{1}+\textup{tr}[h\_{1}v\_{T}] with c1:=α/2−tr​[u1​ω]c\_{1}:=\alpha/2-\textup{tr}[u\_{1}\omega], h1=α​u1−2​u1​mh\_{1}=\alpha u\_{1}-2u\_{1}m and x2=1+tr​[u0​vT]\mathrm{x}\_{2}=1+\textup{tr}[u\_{0}v\_{T}] then the moment generating function of (x1,x2)(\mathrm{x}\_{1},\mathrm{x}\_{2}) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φx1,x2​(z1,z2)\displaystyle\Phi\_{\mathrm{x}\_{1},\mathrm{x}\_{2}}(z\_{1},z\_{2}) | :=𝔼t​[ez1​x1+z2​x2]\displaystyle:=\mathbb{E}\_{t}[e^{z\_{1}\mathrm{x}\_{1}+z\_{2}\mathrm{x}\_{2}}] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =ez1​c1+z2​Φ​(T−t,z1​h1+z2​u0,vt),\displaystyle=e^{z\_{1}c\_{1}+z\_{2}}\Phi(T-t,z\_{1}h\_{1}+z\_{2}u\_{0},v\_{t}), |  | (52) |

with Φ(.,.,.)\Phi(.,.,.) given in Proposition [3.1](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). As μx​(T)\mu\_{x}(T) is the ratio of these two variables, we can use Gurland [[1948](https://arxiv.org/html/2602.06415v1#bib.bib131 "Inversion formulae for the distribution of ratios")] to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(μx​(T)≤z)=12−1π​∫0+∞ℑ⁡(Φx1,x2​(i​s,−i​s​z)s)​𝑑s,\displaystyle\mathbb{P}(\mu\_{x}(T)\leq z)=\frac{1}{2}-\frac{1}{\pi}\int\_{0}^{+\infty}\Im\left(\frac{\Phi\_{\mathrm{x}\_{1},\mathrm{x}\_{2}}(\mathrm{i}s,-\mathrm{i}sz)}{s}\right)ds, |  | (53) |

with i=−1\mathrm{i}=\sqrt{-1}. It gives the result after using ([52](https://arxiv.org/html/2602.06415v1#Ax1.E52 "In Proof of Proposition 4.4 . ‣ Supplementary Appendix ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")).
∎

###### Proof of Proposition [4.8](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem8 "Proposition 4.8. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") .

Define x1=b3+tr⁡[a3​vT]\mathrm{x}\_{1}=b\_{3}+\operatorname{tr}\left[a\_{3}v\_{T}\right] and x2=1+tr⁡[u0​vT]\mathrm{x}\_{2}=1+\operatorname{tr}\left[u\_{0}v\_{T}\right]. Then the moment generating function of (x1,x2)(\mathrm{x}\_{1},\mathrm{x}\_{2}) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φx1,x2​(z1,z2)\displaystyle\Phi\_{\mathrm{x}\_{1},\mathrm{x}\_{2}}(z\_{1},z\_{2}) | =𝔼t​[ez1​x1+z2​x2]\displaystyle=\mathbb{E}\_{t}\left[e^{z\_{1}\mathrm{x}\_{1}+z\_{2}\mathrm{x}\_{2}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ez1​b3+z2​𝔼t​[etr⁡[(z1​a3+z2​u0)​vT]]\displaystyle=e^{z\_{1}b\_{3}+z\_{2}}\mathbb{E}\_{t}\left[e^{\operatorname{tr}\left[\left(z\_{1}a\_{3}+z\_{2}u\_{0}\right)v\_{T}\right]}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ez1​b3+z2​Φ​(T−t,z1​a3+z2​u0,vt),\displaystyle=e^{z\_{1}b\_{3}+z\_{2}}\Phi(T-t,z\_{1}a\_{3}+z\_{2}u\_{0},v\_{t}), |  |

with Φ(.,.,.)\Phi(.,.,.) given in Proposition [3.1](https://arxiv.org/html/2602.06415v1#S3.Thmtheorem1 "Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"). Since ∑i=1NSB​(T,Ti)\sum\_{i=1}^{N}\text{SB}(T,T\_{i}) is the ratio of these two variables, we can use Gurland [[1948](https://arxiv.org/html/2602.06415v1#bib.bib131 "Inversion formulae for the distribution of ratios")] to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(∑i=1NSB​(T,Ti)≤z)=12−1π​∫0+∞ℑ⁡(Φx1,x2​(i​s,−i​s​z)s)​𝑑s,\displaystyle\mathbb{P}\left(\sum\_{i=1}^{N}\text{SB}(T,T\_{i})\leq z\right)=\frac{1}{2}-\frac{1}{\pi}\int\_{0}^{+\infty}\Im\left(\frac{\Phi\_{\mathrm{x}\_{1},\mathrm{x}\_{2}}(\mathrm{i}s,-\mathrm{i}sz)}{s}\right)ds, |  | (54) |

where, after using the above equation, we reach the result.
∎

###### Proof of Proposition [5.1](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem1 "Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

Starting from ([7](https://arxiv.org/html/2602.06415v1#S2.E7 "In 2 The modelling framework ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and using ([19](https://arxiv.org/html/2602.06415v1#S3.E19 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯​(t,T,TN)\displaystyle\bar{C}(t,T,T\_{N}) | =P​(t,T)​𝔼tℚ​[e−∫tT(μx​(s)+μy​(s))​𝑑s​C¯​(T,T,TN)],\displaystyle=P(t,T)\mathbb{E}\_{t}^{\mathbb{Q}}\left[e^{-\int\_{t}^{T}(\mu\_{x}(s)+\mu\_{y}(s))ds}\bar{C}(T,T,T\_{N})\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =P​(t,T)​𝔼t​[ζTζt​(∑i=1NSB​(T,Ti)−1/g)+],\displaystyle=P(t,T)\mathbb{E}\_{t}\left[\frac{\zeta\_{T}}{\zeta\_{t}}\left(\sum\_{i=1}^{N}\mathrm{SB}(T,T\_{i})-1/g\right)\_{+}\right], |  |

and combining with ([18](https://arxiv.org/html/2602.06415v1#S3.E18 "In 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")), Proposition [4.7](https://arxiv.org/html/2602.06415v1#S4.Thmtheorem7 "Proposition 4.7. ‣ 4 Joint survival annuity valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") and some simplifications gives the result after defining b4​(T,TN)b\_{4}(T,T\_{N}) and a4​(T,TN)a\_{4}(T,T\_{N}) as in ([33](https://arxiv.org/html/2602.06415v1#S5.E33 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and ([34](https://arxiv.org/html/2602.06415v1#S5.E34 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")).
∎

###### Proof of Proposition [5.2](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

By definition the cumulants are (κj)j∈ℕ(\kappa\_{j})\_{j\in\mathbb{N}} such that

|  |  |  |
| --- | --- | --- |
|  | log⁡𝔼t​[ez​YT]=∑j=1+∞κj​zjj!.\displaystyle\log\mathbb{E}\_{t}[e^{zY\_{T}}]=\sum\_{j=1}^{+\infty}\kappa\_{j}\frac{z^{j}}{j!}. |  |

From the expression ([12](https://arxiv.org/html/2602.06415v1#S3.E12 "In Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and using det(ea)=etr​[a]\det(e^{a})=\textup{etr}[a] it amounts to perform a series expansion of

|  |  |  |  |
| --- | --- | --- | --- |
|  | z\displaystyle z | →tr​[log⁡(In−2​z​ςT​a4)]\displaystyle\to\textup{tr}[\log(I\_{n}-2z\varsigma\_{T}a\_{4})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | z\displaystyle z | →tr​[ϑT⊤2​(2​z​ςT​a4)​(In−2​z​ςT​a4)−1],\displaystyle\to\textup{tr}\left[\frac{\vartheta\_{T}^{\top}}{2}(2z\varsigma\_{T}a\_{4})(I\_{n}-2z\varsigma\_{T}a\_{4})^{-1}\right], |  |

and using log⁡(In−x)=−∑j=1+∞xjj\log(I\_{n}-x)=-\sum\_{j=1}^{+\infty}\frac{x^{j}}{j} for x∈𝖬​(n)x\in\mathsf{M}(n) we get for the first function the series expansion

|  |  |  |
| --- | --- | --- |
|  | −∑j=1+∞(j−1)!​2j​tr​[(ςT​a4)j]​zjj!,\displaystyle-\sum\_{j=1}^{+\infty}(j-1)!2^{j}\textup{tr}[(\varsigma\_{T}a\_{4})^{j}]\frac{z^{j}}{j!}, |  |

while x​(In−x)−1=∑j=1+∞xjx(I\_{n}-x)^{-1}=\sum\_{j=1}^{+\infty}x^{j} leads for the other one to

|  |  |  |
| --- | --- | --- |
|  | ∑j=1+∞j!​2j−1​tr​[ϑT⊤​(ςT​a4)j]​zjj!,\displaystyle\sum\_{j=1}^{+\infty}j!2^{j-1}\textup{tr}[\vartheta\_{T}^{\top}(\varsigma\_{T}a\_{4})^{j}]\frac{z^{j}}{j!}, |  |

and combining these two series expansions we get the result.
∎

###### Proof of Proposition [5.3](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem3 "Proposition 5.3. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

If YT=b4​(T,TN)+tr​[a4​(T,TN)​vT]Y\_{T}=b\_{4}(T,T\_{N})+\textup{tr}[a\_{4}(T,T\_{N})v\_{T}] with b4​(T,TN)b\_{4}(T,T\_{N}) and a4​(T,TN)a\_{4}(T,T\_{N}) as in  ([32](https://arxiv.org/html/2602.06415v1#S5.E32 "In Proposition 5.1. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) and suppose its density can be approximated by ([39](https://arxiv.org/html/2602.06415v1#S5.E39 "In Proposition 5.3. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[(YT)+]\displaystyle\mathbb{E}\_{t}\left[\left(Y\_{T}\right)\_{+}\right] | ∼∑j=03ηj​∫0+∞12​π​κ2​z​(z−κ1)j​e−(z−κ1)22​κ2​𝑑z\displaystyle\sim\sum\_{j=0}^{3}\eta\_{j}\int\_{0}^{+\infty}\frac{1}{\sqrt{2\pi\kappa\_{2}}}z(z-\kappa\_{1})^{j}e^{-\frac{(z-\kappa\_{1})^{2}}{2\kappa\_{2}}}dz\, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=03ηj​κ2​κ2j/2​∫−κ1κ2+∞zj+1​12​π​e−z22​𝑑z+∑j=03ηj​κ1​κ2j/2​∫−κ1κ2+∞zj​12​π​e−z22​𝑑z\displaystyle=\sum\_{j=0}^{3}\eta\_{j}\sqrt{\kappa\_{2}}\kappa\_{2}^{j/2}\int\_{\frac{-\kappa\_{1}}{\sqrt{\kappa\_{2}}}}^{+\infty}z^{j+1}\frac{1}{\sqrt{2\pi}}e^{-\frac{z^{2}}{2}}dz+\sum\_{j=0}^{3}\eta\_{j}\kappa\_{1}\kappa\_{2}^{j/2}\int\_{\frac{-\kappa\_{1}}{\sqrt{\kappa\_{2}}}}^{+\infty}z^{j}\frac{1}{\sqrt{2\pi}}e^{-\frac{z^{2}}{2}}dz\, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=03ηj​ξj+1+κ1​∑j=03ηj​ξj,\displaystyle=\sum\_{j=0}^{3}\eta\_{j}\xi\_{j+1}+\kappa\_{1}\sum\_{j=0}^{3}\eta\_{j}\xi\_{j}\,, |  |

where η0=1\eta\_{0}=1, η1=−3κ22​κ33!\eta\_{1}=-\frac{3}{\kappa\_{2}^{2}}\frac{\kappa\_{3}}{3!}, η2=0\eta\_{2}=0 and η3=1κ23​κ33!\eta\_{3}=\frac{1}{\kappa\_{2}^{3}}\frac{\kappa\_{3}}{3!} while ξj=κ2j/2​∫−κ1κ2+∞zj2​π​e−z22​𝑑z\xi\_{j}=\kappa\_{2}^{j/2}\int\_{\frac{-\kappa\_{1}}{\sqrt{\kappa\_{2}}}}^{+\infty}\frac{z^{j}}{\sqrt{2\pi}}e^{-\frac{z^{2}}{2}}dz are given by ξ0=N​(κ1κ2)\xi\_{0}=N\left(\frac{\kappa\_{1}}{\sqrt{\kappa\_{2}}}\right), ξ1=κ2​φ​(κ1κ2)\xi\_{1}=\sqrt{\kappa\_{2}}\varphi\left(\frac{\kappa\_{1}}{\sqrt{\kappa\_{2}}}\right), ξ2=κ2​N​(κ1κ2)−ξ1​κ1\xi\_{2}=\kappa\_{2}N\left(\frac{\kappa\_{1}}{\sqrt{\kappa\_{2}}}\right)-\xi\_{1}\kappa\_{1}, ξ3=ξ1​(κ12+2​κ2)\xi\_{3}=\xi\_{1}(\kappa\_{1}^{2}+2\kappa\_{2}) and ξ4=3​κ22​N​(κ1κ2)−ξ1​(κ13+3​κ2​κ1)\xi\_{4}=3\kappa\_{2}^{2}N\left(\frac{\kappa\_{1}}{\sqrt{\kappa\_{2}}}\right)-\xi\_{1}(\kappa\_{1}^{3}+3\kappa\_{2}\kappa\_{1}) with N(.)N(.) and φ(.)\varphi(.) the cumulative normal distribution and normal distribution density, respectively.
∎

###### Proof of Proposition [5.4](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem4 "Proposition 5.4. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

Let γ\gamma as stated above and consider γ⊤​vT​γ=tr​[γ​γ⊤​vT]\gamma^{\top}v\_{T}\gamma=\textup{tr}[\gamma\gamma^{\top}v\_{T}] then for z∈ℝz\in\mathbb{R} using ([12](https://arxiv.org/html/2602.06415v1#S3.E12 "In Proposition 3.1. ‣ 3 The linear-rational Wishart model ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")) we get

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[ez​tr​[γ​γ⊤​vT]]=etr​(ϑT⊤2​(2​z​ςT​γ​γ⊤)​(In−2​z​ςT​γ​γ⊤)−1)det(In−2​z​ςT​γ​γ⊤)β/2,\displaystyle\mathbb{E}\_{t}[e^{z\textup{tr}[\gamma\gamma^{\top}v\_{T}]}]=\frac{\textup{etr}\left(\frac{\vartheta\_{T}^{\top}}{2}(2z\varsigma\_{T}\gamma\gamma^{\top})(I\_{n}-2z\varsigma\_{T}\gamma\gamma^{\top})^{-1}\right)}{\det(I\_{n}-2z\varsigma\_{T}\gamma\gamma^{\top})^{\beta/2}}\,, |  |

and since γ​γ⊤\gamma\gamma^{\top} is rank one there exists a basis such that γ​γ⊤\gamma\gamma^{\top} in that basis is e11e\_{11} so that det(In−2​z​ςT​e11)β/2=(1−2​z​(ςT)11)β/2\det(I\_{n}-2z\varsigma\_{T}e\_{11})^{\beta/2}=(1-2z(\varsigma\_{T})\_{11})^{\beta/2} (ςT\varsigma\_{T} has to be expressed in that basis) and that the numerator above is

|  |  |  |
| --- | --- | --- |
|  | etr​(ϑT⊤2​(2​z​ςT​e11)​(In−2​z​ςT​e11)−1)=exp⁡((ϑT⊤)11​z​(ςT)111−2​z​(ςT)11),\displaystyle\textup{etr}\left(\frac{\vartheta\_{T}^{\top}}{2}(2z\varsigma\_{T}e\_{11})(I\_{n}-2z\varsigma\_{T}e\_{11})^{-1}\right)=\exp\left(\frac{(\vartheta\_{T}^{\top})\_{11}z(\varsigma\_{T})\_{11}}{1-2z(\varsigma\_{T})\_{11}}\right)\,, |  |

with both ςT\varsigma\_{T} and ϑT\vartheta\_{T} expressed in that basis. Combining the two it leads to

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[ez​γ⊤​vT​γ]=e(ϑT⊤)11​z​(ςT)111−2​z​(ςT)11(1−2​z​(ςT)11)β/2,\displaystyle\mathbb{E}\_{t}[e^{z\gamma^{\top}v\_{T}\gamma}]=\frac{e^{\frac{(\vartheta\_{T}^{\top})\_{11}z(\varsigma\_{T})\_{11}}{1-2z(\varsigma\_{T})\_{11}}}}{(1-2z(\varsigma\_{T})\_{11})^{\beta/2}}\,, |  |

from which we get the result.
∎

###### Proof of Proposition [5.5](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem5 "Proposition 5.5. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model").

Let YT=b4​(T,TN)+tr​[a4​(T,TN)​vT]Y\_{T}=b\_{4}(T,T\_{N})+\textup{tr}[a\_{4}(T,T\_{N})v\_{T}] and rewrite tr​[a4​(T,TN)​vT]\textup{tr}[a\_{4}(T,T\_{N})v\_{T}] as tr​[(a4+a4⊤2)​vT]\textup{tr}[(\frac{a\_{4}+a\_{4}^{\top}}{2})v\_{T}], and since a4+a4⊤2∈𝕊n\frac{a\_{4}+a\_{4}^{\top}}{2}\in\mathbb{S}\_{n}, it admits the decomposition ([41](https://arxiv.org/html/2602.06415v1#S5.E41 "In Proposition 5.5. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). But tr​[γi​γi⊤​vT]=γi⊤​vT​γi\textup{tr}[\gamma\_{i}\gamma\_{i}^{\top}v\_{T}]=\gamma\_{i}^{\top}v\_{T}\gamma\_{i} and according to Proposition [5.4](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem4 "Proposition 5.4. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model"), γi⊤​vT​γi/(ςT)i​i\gamma\_{i}^{\top}v\_{T}\gamma\_{i}/(\varsigma\_{T})\_{ii} has a non-central Chi-squared distribution with degrees of freedom β\beta and non-centrality parameter (ϑT⊤)i​i(\vartheta\_{T}^{\top})\_{ii}. Note that these variables are not independent, but we can approximate YTY\_{T}, although we do not have a control of the approximation error, with Y~T\tilde{Y}\_{T} defined by ([43](https://arxiv.org/html/2602.06415v1#S5.E43 "In Proposition 5.5. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). This set of variables follows a generalized Chi-squared distribution (since it is a collection of independent scalar non-central Chi-squared variables).
∎

###### Proof of Proposition [5.7](https://arxiv.org/html/2602.06415v1#S5.Thmtheorem7 "Proposition 5.7. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model") .

We have YT=b4+tr​[a4​vT]Y\_{T}=b\_{4}+\textup{tr}[a\_{4}v\_{T}] and if the eigenvalues of a4a\_{4} are all positive then tr​[a4​v]>0\textup{tr}[a\_{4}v]>0 for v∈𝕊n++v\in\mathbb{S}\_{n}^{++} so that necessarily b4<0b\_{4}<0 (otherwise YTY\_{T} would be positive and the option would end always in the money) so that there exists k<0k<0 such that YT>kY\_{T}>k. A natural choice for kk is k=b4k=b\_{4}. Then if we denote Z=YT−kZ=Y\_{T}-k we can rewrite as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[(YT)+]=𝔼t​[(Z+k)+],\displaystyle\mathbb{E}\_{t}\left[\left(Y\_{T}\right)\_{+}\right]=\mathbb{E}\_{t}\left[\left(Z+k\right)\_{+}\right]\,, |  | (55) |

with μiZ=𝔼t​[Zi]=∑j=0i(ij)​(−1)j​μi−j​kj\mu\_{i}^{Z}=\mathbb{E}\_{t}\left[Z^{i}\right]=\sum\_{j=0}^{i}\binom{i}{j}(-1)^{j}\mu\_{i-j}k^{j} and μi=𝔼t​[YTi]\mu\_{i}=\mathbb{E}\_{t}\left[Y\_{T}^{i}\right] the i′​t​hi^{\prime}{th} moment of YTY\_{T} that can be deduced from the cumulants of YTY\_{T} thanks to ([38](https://arxiv.org/html/2602.06415v1#S5.E38 "In Proposition 5.2. ‣ 5 Guaranteed joint survival annuity option valuation ‣ Joint survival annuity derivative valuation in the linear-rational Wishart mortality model")). Note that as Z>0Z>0 by construction then μ1Z>0\mu\_{1}^{Z}>0 and we approximate its distribution by a perturbation of the (scalar) gamma distribution following Filipović et al. [[2013](https://arxiv.org/html/2602.06415v1#bib.bib65 "Density approximations for multivariate affine jump-diffusion processes")]. The density of Z​μ1Zμ2Z−(μ1Z)2\frac{Z\mu\_{1}^{Z}}{\mu\_{2}^{Z}-(\mu\_{1}^{Z})^{2}} can be approximated at order three by

|  |  |  |  |
| --- | --- | --- | --- |
|  | g3​(z)=w​(z)​∑j=03cj​Hj​(z),\displaystyle g^{3}(z)=w(z)\sum\_{j=0}^{3}c\_{j}H\_{j}(z)\,, |  | (56) |

with ww the auxiliary density function w​(z)=zα¯​e−zΓ​(1+α¯)w(z)=\frac{z^{\bar{\alpha}}e^{-z}}{\Gamma(1+\bar{\alpha})}, that is the (scalar) gamma distribution with shape 1+α¯1+\bar{\alpha} and rate 1, some known constants cjc\_{j}, and {Hj|j=0,…,3}\left\{H\_{j}\left.\right|j=0,\ldots,3\right\} an orthonormal basis of polynomials. Filipović et al. [[2013](https://arxiv.org/html/2602.06415v1#bib.bib65 "Density approximations for multivariate affine jump-diffusion processes")] prove that the functions HjH\_{j} are given by Hj=H~j‖H~j​(z)‖H\_{j}=\frac{{\tilde{H}\_{j}}}{{\left\|\tilde{H}\_{j}(z)\right\|}}, with ‖H~j​(z)‖=∏i=1j(i+α¯)j!{\left\|\tilde{H}\_{j}(z)\right\|}=\sqrt{\frac{\prod\_{i=1}^{j}(i+\bar{\alpha})}{j!}} and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H~0​(z)\displaystyle\tilde{H}\_{0}(z) | =1,\displaystyle=1\,, |  | (57) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H~1​(z)\displaystyle\tilde{H}\_{1}(z) | =−z+α¯+1,\displaystyle=-z+\bar{\alpha}+1\,, |  | (58) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H~2​(z)\displaystyle\tilde{H}\_{2}(z) | =12​(z2−2​z​(α¯+2)+α¯2+3​α¯+2),\displaystyle=\frac{1}{2}(z^{2}-2z(\bar{\alpha}+2)+\bar{\alpha}^{2}+3\bar{\alpha}+2)\,, |  | (59) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | H~3​(z)\displaystyle\tilde{H}\_{3}(z) | =16​(−z3+3​z2​(α¯+3)−3​z​(α¯2+5​α¯+6)+α¯3+6​α¯2+11​α¯+6).\displaystyle=\frac{1}{6}(-z^{3}+3z^{2}(\bar{\alpha}+3)-3z(\bar{\alpha}^{2}+5\bar{\alpha}+6)+\bar{\alpha}^{3}+6\bar{\alpha}^{2}+11\bar{\alpha}+6)\,. |  | (60) |

Following Filipović et al. [[2013](https://arxiv.org/html/2602.06415v1#bib.bib65 "Density approximations for multivariate affine jump-diffusion processes"), Section 7.1], we choose α¯=(μ1Z)2μ2Z−(μ1Z)2−1\bar{\alpha}=\frac{(\mu\_{1}^{Z})^{2}}{\mu\_{2}^{Z}-(\mu\_{1}^{Z})^{2}}-1 and β¯=μ1Zμ2Z−(μ1Z)2>0\bar{\beta}=\frac{\mu\_{1}^{Z}}{\mu\_{2}^{Z}-(\mu\_{1}^{Z})^{2}}>0 as μ1Z>0\mu\_{1}^{Z}>0 then the coefficients {ci;i=0,…,3}\{c\_{i};i=0,\ldots,3\} are given by: c0=1c\_{0}=1, c1=0c\_{1}=0, c2=0c\_{2}=0 and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | c3\displaystyle c\_{3} | =(α¯+1)​((α¯+2)​(α¯+3)−(α¯+1)2​μ3Z(μ1Z)3)6​(α¯+1)​(α¯+2)​(α¯+3).\displaystyle=\frac{(\bar{\alpha}+1)\left((\bar{\alpha}+2)(\bar{\alpha}+3)-\frac{(\bar{\alpha}+1)^{2}\mu\_{3}^{Z}}{(\mu\_{1}^{Z})^{3}}\right)}{\sqrt{6}\sqrt{(\bar{\alpha}+1)(\bar{\alpha}+2)(\bar{\alpha}+3)}}\,. |  | (61) |

Eventually, the density of ZZ, taking into account the change of variable Z​μ1Zμ2Z−(μ1Z)2\frac{Z\mu\_{1}^{Z}}{\mu\_{2}^{Z}-(\mu\_{1}^{Z})^{2}}, can be approximated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | g3​(z)=w​(β¯​z)​∑j=03cj​Hj​(β¯​z)​β¯,\displaystyle g^{3}(z)=w(\bar{\beta}z)\sum\_{j=0}^{3}c\_{j}H\_{j}(\bar{\beta}z)\bar{\beta}\,, |  | (62) |

and therefore, by rewriting Hj​(z)=∑i=0jγj,i​ziH\_{j}(z)=\sum\_{i=0}^{j}\gamma\_{j,i}z^{i}, we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼t​[(YT)+]\displaystyle\mathbb{E}\_{t}\left[\left(Y\_{T}\right)\_{+}\right] | =𝔼t​[(Z+k)+]∼∫−k+∞(z+k)​g3​(z)​𝑑z\displaystyle=\mathbb{E}\_{t}\left[\left(Z+k\right)\_{+}\right]\sim\int\_{-k}^{+\infty}(z+k)g^{3}(z)dz |  | (63) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫−β¯​k+∞(yβ¯+k)​w​(y)​∑j=03∑i=0jcj​γj,i​yi​d​y\displaystyle=\int\_{-\bar{\beta}k}^{+\infty}\left(\frac{y}{\bar{\beta}}+k\right)w(y)\sum\_{j=0}^{3}\sum\_{i=0}^{j}c\_{j}\gamma\_{j,i}y^{i}dy |  | (64) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∑j=03∑i=0jcj​γj,i​Γ​(α¯+i+2,−β¯​k)β¯​Γ​(1+α¯)+∑j=03∑i=0jcj​γj,i​k​Γ​(α¯+i+1,−β¯​k)Γ​(1+α¯),\displaystyle=\sum\_{j=0}^{3}\sum\_{i=0}^{j}c\_{j}\gamma\_{j,i}\frac{\Gamma(\bar{\alpha}+i+2,-\bar{\beta}k)}{\bar{\beta}\Gamma(1+\bar{\alpha})}+\sum\_{j=0}^{3}\sum\_{i=0}^{j}c\_{j}\gamma\_{j,i}k\frac{\Gamma(\bar{\alpha}+i+1,-\bar{\beta}k)}{\Gamma(1+\bar{\alpha})}\,, |  | (65) |

where we used the condition β¯>0\bar{\beta}>0 while Γ​(s,x)\Gamma(s,x) stands for the upper incomplete gamma function. To avoid overflows with the gamma function, we use its regularized version so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ​(α¯+i+2,−β¯​k)Γ​(1+α¯)=Q​(α¯+i+2,−β¯​k)​Γ​(α¯+i+2)Γ​(1+α¯),\displaystyle\frac{\Gamma(\bar{\alpha}+i+2,-\bar{\beta}k)}{\Gamma(1+\bar{\alpha})}=Q(\bar{\alpha}+i+2,-\bar{\beta}k)\frac{\Gamma(\bar{\alpha}+i+2)}{\Gamma(1+\bar{\alpha})}\,, |  | (66) |

and thank to the relations Q​(s,x)=Γ​(s,x)/Γ​(s)Q(s,x)=\Gamma(s,x)/\Gamma(s) and (x)n=Γ​(x+n)/Γ​(x)(x)\_{n}=\Gamma(x+n)/\Gamma(x) where (x)n(x)\_{n} is the Pochhammer function (rising factorial) we deduce the result.

If the eigenvalues of a4a\_{4} are all negative then tr​[a4​v]<0\textup{tr}[a\_{4}v]<0 for v∈𝕊n++v\in\mathbb{S}\_{n}^{++} so that necessarily b4>0b\_{4}>0 and there exists k>0k>0 such that YT<kY\_{T}<k. A natural choice for kk is k=b4k=b\_{4}. To reuse previous computations, we rewrite the expectation as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[(YT)+]=𝔼t​[(−(−b4−tr​[a4​vT]))+]\displaystyle\mathbb{E}\_{t}\left[\left(Y\_{T}\right)\_{+}\right]=\mathbb{E}\_{t}\left[\left(-(-b\_{4}-\textup{tr}[a\_{4}v\_{T}])\right)\_{+}\right] |  | (67) |

and define Z=(−b4−tr​[a4​vT])+kZ=(-b\_{4}-\textup{tr}[a\_{4}v\_{T}])+k, then 𝔼t​[(YT)+]=𝔼t​[(−(Z+k))+]\mathbb{E}\_{t}\left[\left(Y\_{T}\right)\_{+}\right]=\mathbb{E}\_{t}\left[\left(-(Z+k)\right)\_{+}\right] and using the previous case we reach the announced result.
∎