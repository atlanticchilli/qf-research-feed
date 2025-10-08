---
authors:
- Ivan Guo
- Jan Obłój
doc_id: arxiv:2510.05463v1
family_id: arxiv:2510.05463
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Robust Pricing and Hedging of American Options in Continuous Time
url_abs: http://arxiv.org/abs/2510.05463v1
url_html: https://arxiv.org/html/2510.05463v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ivan Guo
School of Mathematics, Monash University
Centre for Quantitative Finance and Investment Strategies, Monash University

Jan Obłój
Ivan Guo’s work was partially supported by the Australian Research Council (Grant DP220103106). We are grateful to Anna Aksamit, Libo Li and Gregoire Loeper for fruitful discussions. Our sincere thanks go to Vlad Tuchilus for his help with editing the manuscript.
  
For open access purposes, the authors have applied a CC BY public copyright licence to any author accepted manuscript version arising from this submission.
Mathematical Institute, University of Oxford

(October 6, 2025)

###### Abstract

We consider the robust pricing and hedging of American options in a continuous time setting. We assume asset prices are continuous semimartingales, but we allow for general model uncertainty specification via adapted closed convex constraints on the volatility. We prove the robust pricing-hedging duality. When European options with given prices are available for static trading, we show that duality holds against richer models where these options are traded dynamically. Our proofs rely on probabilistic treatment of randomised stopping times and suitable measure decoupling, and on optimal transport duality. In addition, similarly to the approach of Aksamit et al. ([2019](https://arxiv.org/html/2510.05463v1#bib.bib1)) in discrete time, we identify American options with European options on an enlarged space.

Keywords: robust pricing and hedging, American options, duality, optimal transport, volatility restrictions, Azéma supermartingale

## 1 Introduction

Option pricing is at the origins of modern quantitative finance, with the Black-Scholes formula one of its most iconic manifestations and often billed as one of the equations which changed the world, see Stewart ([2012](https://arxiv.org/html/2510.05463v1#bib.bib57)). The intuition behind it, going back to the seminal works of Black and Scholes ([1973](https://arxiv.org/html/2510.05463v1#bib.bib10)); Merton ([1973](https://arxiv.org/html/2510.05463v1#bib.bib43)), links pricing to hedging: if a hedging strategy can replicate the option’s cashflow, then the two should have the same initial price, or else markets would admit plain arbitrage opportunities. In some probabilistic models for the underlying’s dynamics, such as the Black-Scholes model, we can compute this price by taking risk-neutral expectations. In more general, incomplete models a perfect hedging strategy may not exist but the principle generalises to the so-called pricing-hedging duality: the cost of the cheapest superhedging strategy is equal to the supremum of the payoff’s expectations under all risk-neutral measures, see (Föllmer and Schied, [2004](https://arxiv.org/html/2510.05463v1#bib.bib26), Chp. 7) (Karatzas and Shreve, [1998](https://arxiv.org/html/2510.05463v1#bib.bib39), Chp. 5).

The above classical results require us to fix a probabilistic model for the dynamics of the risky assets. This perspective, while allowing for an efficient description of the risk within the chosen model, is silent on the errors related to the model choice itself, errors often referred to as the *Knightian uncertainty* after Knight ([1921](https://arxiv.org/html/2510.05463v1#bib.bib40)), *model ambiguity or misspecification* or *epistemic uncertainty*, see Hansen and Marinacci ([2016](https://arxiv.org/html/2510.05463v1#bib.bib32)); Walley ([1991](https://arxiv.org/html/2510.05463v1#bib.bib60)). This shortcoming became a focal point after the 2008 global financial crisis and led to the development of *robust methods* in mathematical finance. Rich literature emerged tackling the foundational questions on how to best capture, mathematically speaking, diversity of models, how to properly define an arbitrage opportunity if a single model is not specified and to obtain a *robust fundamental theorem of asset pricing* that would characterise absence of arbitrage. And how to formulate, and prove, a *robust pricing-hedging duality*. In discrete time settings, these questions were answered using two points of view. One, the so-called *quasi-sure* perspective, relied on families of probability measures which, while potentially mutually singular, have enough structure to obtain a complete set of results, see Bouchard and Nutz ([2015](https://arxiv.org/html/2510.05463v1#bib.bib11)) and the references therein. The other point of view adopted a pointwise (or pathwise), ω\omega by ω\omega, also leading to complete robust equivalent of the classical results, see Burzoni et al. ([2019](https://arxiv.org/html/2510.05463v1#bib.bib14)) and the references therein. The two approaches are naturally just different ways to see the problem and can be shown to be equivalent, see Obłój and Wiesel ([2021](https://arxiv.org/html/2510.05463v1#bib.bib50)).
Analogous efforts were undertaken in continuous time settings, with quasi-sure analysis advanced in, e.g, Denis and Martini ([2006](https://arxiv.org/html/2510.05463v1#bib.bib19)); Neufeld and Nutz ([2013](https://arxiv.org/html/2510.05463v1#bib.bib48)); Possamaï et al. ([2013](https://arxiv.org/html/2510.05463v1#bib.bib53)) and pathwise arguments used by, e.g, Mykland ([2003](https://arxiv.org/html/2510.05463v1#bib.bib45)); Vovk ([2012](https://arxiv.org/html/2510.05463v1#bib.bib59)); Allan et al. ([2023](https://arxiv.org/html/2510.05463v1#bib.bib3)); Dolinsky and Soner ([2014](https://arxiv.org/html/2510.05463v1#bib.bib21)); Hou and Obłój ([2018](https://arxiv.org/html/2510.05463v1#bib.bib36)). The formidable technical challenge in continuous time relates to the necessity to consider suitable classes of admissible trading strategies and to define their outcomes, given by stochastic integrals, simultaneously under many different, often singular, probability measures. To the best of our knowledge, while a lot of progress has been done and many partial exciting results exist, in contrast to the discrete time setting, in continuous time no complete robust theory has been obtained. Our work contributes to the ongoing development of robust mathematical finance in continuous time.

In the context of robust pricing and hedging, if no modelling assumptions are made, the range of possible no-arbitrage prices for a given contingent claim can be impractically large. A natural way to narrow it is to use available market information. In this way, arbitrary constraints coming from modeller’s choices are replaced with observable market prices. The latter would be taken into the account in the classical approach via a reverse-engineering process, in which a particular model is selected, say from a parametric class of models, to best fit observed market prices via *calibration*. In the robust approach instead, such market prices are added as constraints to the original problem. This perspective in fact was behind the foundational works of Hobson ([1998](https://arxiv.org/html/2510.05463v1#bib.bib33)); Brown et al. ([2001](https://arxiv.org/html/2510.05463v1#bib.bib13)) which solved robust pricing and hedging of lookback and barrier options using probabilistic methods of Skorokhod embeddings, see Obłój ([2004](https://arxiv.org/html/2510.05463v1#bib.bib49)); Hobson ([2011](https://arxiv.org/html/2510.05463v1#bib.bib34)); Cox and Obłój ([2011](https://arxiv.org/html/2510.05463v1#bib.bib16)), based on the classical observation of Breeden and Litzenberger ([1978](https://arxiv.org/html/2510.05463v1#bib.bib12)) that incorporating market prices of call options with a maturity TT is equivalent to fixing the marginal distribution at TT under the risk-neutral measure. In subsequent seminal contributions Beiglböck et al. ([2013](https://arxiv.org/html/2510.05463v1#bib.bib8)); Galichon et al. ([2014](https://arxiv.org/html/2510.05463v1#bib.bib28)) re-wrote the robust pricing and hedging problem as an optimal transport (OT) problem with a martingale constraint, i.e., a *martingale optimal transport* (MOT) problem. These ideas brought rich and powerful techniques of OT to robust mathematical finance, allowing in particular to develop numerical methods and perform empirical studies for robust methods, see Guo and Obłój ([2019](https://arxiv.org/html/2510.05463v1#bib.bib29)); Eckstein et al. ([2021](https://arxiv.org/html/2510.05463v1#bib.bib23)), and obtain robust pricing-hedging duality results under general constraints, see Guo et al. ([2017](https://arxiv.org/html/2510.05463v1#bib.bib30)); Guo and Loeper ([2021](https://arxiv.org/html/2510.05463v1#bib.bib31)).

Interestingly, as first observed by Neuberger ([2007](https://arxiv.org/html/2510.05463v1#bib.bib47)), these ideas were not sufficient to consider robust pricing and hedging for American options, and their naive extension could lead to a gap in the pricing-hedging duality. Instead, a weak formulation was suggested by Neuberger ([2007](https://arxiv.org/html/2510.05463v1#bib.bib47)) and further explored in Hobson and Neuberger ([2017](https://arxiv.org/html/2510.05463v1#bib.bib35)). Another technical solution, via randomised models, was proposed by Bayraktar et al. ([2015](https://arxiv.org/html/2510.05463v1#bib.bib7)); Bayraktar and Zhou ([2017](https://arxiv.org/html/2510.05463v1#bib.bib6)). A more comprehensive explanation was proposed by Aksamit et al. ([2019](https://arxiv.org/html/2510.05463v1#bib.bib1)) who analysed the problem through the lens of information — while stock prices are observed, and traded on, dynamically, the constraining market option prices are given statically at time t=0t=0 and not updated afterwards, limiting the class of exercise policies for the American option holders. They linked duality to a robust version of the dynamic programming principle (DPP), used for classical American option pricing. This also explained why Dolinsky ([2014](https://arxiv.org/html/2510.05463v1#bib.bib20)), who studied game options, which include American options, in a nondominated discrete time market, did not encounter duality gap issues since his setup had no statically traded options. Aksamit et al. ([2019](https://arxiv.org/html/2510.05463v1#bib.bib1)) then showed that the pricing-hedging duality can be restored by considering a richer class of models where options are traded dynamically as well.

Our work makes a decisive new contribution to this literature by developing robust pricing and hedging duality for American options in continuous time. We show that πgA\pi^{A}\_{g}, the superhedging price of an American option ZZ using dynamic trading in the stocks and static trading in European options with payoffs gg, is equal to

|  |  |  |
| --- | --- | --- |
|  | supℙ^∈𝒬^,τ^∈𝒯^ℙ^𝔼ℙ^​Zτ^,\sup\_{\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}},\widehat{\tau}\in\widehat{\mathcal{T}}^{\widehat{\mathbb{P}}}}\mathbb{E}^{\widehat{\mathbb{P}}}Z\_{\widehat{\tau}}, |  |

where 𝒬^\widehat{\mathcal{Q}} corresponds to risk neutral measures for joint dynamics of stocks and options gg, and the stopping times τ^\widehat{\tau} are allowed to depend on the information about both. The exact statement of that duality is given in Theorem [5.2](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem2 "Theorem 5.2. ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") and it allows to further restrict models to those with volatility taking values in pre-specified sets. These could be general, but could also be given by a point, in which way our results recover the to classical model-specific pricing-hedging duality for American options, as in Myneni ([1992](https://arxiv.org/html/2510.05463v1#bib.bib46)), as a special case. When no statically traded options are available, g=0g=0, then we can restrict to martinagle measures 𝒬\mathcal{Q} on Ω\Omega and exercise policies τ∈𝒯\tau\in\mathcal{T}.
To prove the above duality we adopt ideas pioneered in Aksamit et al. ([2019](https://arxiv.org/html/2510.05463v1#bib.bib1)) and show that an American option can be identified with a European option in an enlarged space Ω¯\bar{\Omega}. However, unlike in Aksamit et al. ([2019](https://arxiv.org/html/2510.05463v1#bib.bib1)), to link the pricing in the two perspectives, we do not go via a dynamic programming representation but instead rely on probabilistic techniques related to randomised stopping times and Azéma supermartingales, see Theorem [3.1](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") and other results in section [3](https://arxiv.org/html/2510.05463v1#S3 "3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time"). Also on the hedging side, we encounter genuine novel difficulties in the continuous time setup. We lift models to allow for dynamic trading in the European options with given time zero market prices. However, while we work with continuous asset prices, we can not ensure that option prices, defined via conditional expectations, are continuous. In fact, they may be random at time t=0t=0. To account for that, we have to consider fictitious markets with trading on [−δ,1][-\delta,1], see section [4](https://arxiv.org/html/2510.05463v1#S4 "4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time"). This allows us to establish a chain of inequalities between potential superhedging and pricing valuations, see Proposition [4.5](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3 Duality gap and a dynamic extension for statically traded European options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time"). The final piece of the jigsaw is to show the LHS and RHS of this long chain of inequalities are equal, which boils down to establishing pricing-hedging duality for European options on Ω¯\bar{\Omega}. We do this in section [5](https://arxiv.org/html/2510.05463v1#S5 "5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") using OT-duality methods, in analogy to Guo and Loeper ([2021](https://arxiv.org/html/2510.05463v1#bib.bib31)); Tan et al. ([2013](https://arxiv.org/html/2510.05463v1#bib.bib58)).

## 2 Preliminaries

Let Ω:=D​([0,1];ℝd)\Omega:=D([0,1];\mathbb{R}^{d}) be the set of right-continuous and with left limits (rcll) paths and XX be the canonical process. For each t∈[0,1]t\in[0,1], let Ωt:={ω⋅∧t:ω∈Ω}\Omega\_{t}:=\{\omega\_{\cdot\wedge t}:\omega\in\Omega\} be the set of paths stopped at time tt and let Λ:={(t,ω):t∈[0,1],ω∈Ωt}\Lambda:=\{(t,\omega):t\in[0,1],\omega\in\Omega\_{t}\}.
Let 𝔽=(ℱt)0≤t≤1\mathbb{F}=(\mathcal{F}\_{t})\_{0\leq t\leq 1} be the canonical filtration generated by XX. For any given probability measure ℙ\mathbb{P} on (Ω,𝔽)(\Omega,\mathbb{F}), let 𝔽ℙ\mathbb{F}^{\mathbb{P}} be the augmentation of 𝔽\mathbb{F} with respect to ℙ\mathbb{P}. We denote by 𝒯\mathcal{T} (resp. by 𝒯ℙ\mathcal{T}^{\mathbb{P}}) the set of 𝔽\mathbb{F} (resp. 𝔽ℙ\mathbb{F}^{\mathbb{P}}) stopping times.
The spaces Ω\Omega and Ωt\Omega\_{t} are equipped the with the norm ‖ω‖∞=supt∈[0,1]|ωt|\left\|\omega\right\|\_{\infty}=\sup\_{t\in[0,1]}|\omega\_{t}|, while Λ\Lambda is
equipped with the metric d∞​((t,ω),(t′,ω′))=|t−t′|+‖ω⋅∧t−ω⋅∧t′′‖∞d\_{\infty}((t,\omega),(t^{\prime},\omega^{\prime}))=|t-t^{\prime}|+\left\|\omega\_{\cdot\wedge t}-\omega^{\prime}\_{\cdot\wedge t^{\prime}}\right\|\_{\infty}. We note that a process qq on Ω\Omega is 𝔽\mathbb{F}–progressively measurable if and only if it is a measurable map from Λ\Lambda to ℝ\mathbb{R}.

Given a Polish space 𝒳\mathcal{X} equipped with its Borel σ\sigma-algebra, let C​(𝒳)C(\mathcal{X}) be the set of continuous functions on 𝒳\mathcal{X}, Cb​(𝒳)C\_{b}(\mathcal{X}) be the set of bounded continuous functions and ℳ​(𝒳)\mathcal{M}(\mathcal{X}) be the set of signed finite Borel measures on 𝒳\mathcal{X}.
On Cb​(𝒳)C\_{b}(\mathcal{X}), let 𝔗k\mathfrak{T}\_{k} denote the topology of uniform convergence on compact sets of 𝒳\mathcal{X}. Denote by 𝔗t\mathfrak{T}\_{t} the finest locally convex topology on Cb​(𝒳)C\_{b}(\mathcal{X}) which agrees with 𝔗k\mathfrak{T}\_{k} on closed balls of Cb​(𝒳)C\_{b}(\mathcal{X}) (via the uniform norm). The topology 𝔗t\mathfrak{T}\_{t} was introduced by Le Cam ([1957](https://arxiv.org/html/2510.05463v1#bib.bib41)) and is also known as the “mixed topology” Fremlin et al. ([1972](https://arxiv.org/html/2510.05463v1#bib.bib27)) or the “substrict topology” Sentilles ([1972](https://arxiv.org/html/2510.05463v1#bib.bib54)). For this paper, we will make use the following key result:

###### Proposition 2.1 (Fremlin et al. ([1972](https://arxiv.org/html/2510.05463v1#bib.bib27)); Sentilles ([1972](https://arxiv.org/html/2510.05463v1#bib.bib54))).

The 𝔗t\mathfrak{T}\_{t} dual of Cb​(𝒳)C\_{b}(\mathcal{X}) can be identified with Cb​(𝒳)∗=ℳ​(𝒳)C\_{b}(\mathcal{X})^{\*}=\mathcal{M}(\mathcal{X}).

###### Remark 2.2.

The choice of topology 𝔗t\mathfrak{T}\_{t} will allow the applications of our duality argument in non-locally compact settings, and to avoid the issue of Cb​(Ω)∗C\_{b}(\Omega)^{\*} being identified with the set of all regular, signed, finite and finitely additive Borel measures (Dunford and Schwartz ([1958](https://arxiv.org/html/2510.05463v1#bib.bib22)) Theorem IV.6.2) under the usual uniform norm topology.

Let 𝕊d\mathbb{S}^{d}, 𝕊+d\mathbb{S}^{d}\_{+} and 𝕊++d\mathbb{S}^{d}\_{++} denote the sets of symmetric matrices, positive semidefinite matrices and positive definite matrices, respectively, with a:b:=tr⁡(a⊺​b)a:b:=\operatorname{tr}(a^{\intercal}b), for any a,b∈𝕊da,b\in\mathbb{S}^{d}.
We denote L∞​(𝒳)L^{\infty}(\mathcal{X}) the set of bounded measurable functions and L1​(𝒳,μ)L^{1}(\mathcal{X},\mu) the set of μ\mu-integrable functions, where μ∈ℳ+​(𝒳)⊂ℳ​(𝒳)\mu\in\mathcal{M}\_{+}(\mathcal{X})\subset\mathcal{M}(\mathcal{X}) is a positive measure on 𝒳\mathcal{X}. The respective vector valued version of such spaces are denoted in the natural way, e.g., Cb​(𝒳;ℝm)C\_{b}(\mathcal{X};\mathbb{R}^{m}), ℳ​(𝒳;ℝm)\mathcal{M}(\mathcal{X};\mathbb{R}^{m}), L1​(𝒳,μ;ℝm)L^{1}(\mathcal{X},\mu;\mathbb{R}^{m}) and so on. In this paper, the typical choices of 𝒳\mathcal{X} are Ω\Omega, Λ\Lambda, ℝm\mathbb{R}^{m}, their products, as well as their subspaces. We will also use the shorthand μ​(f):=∫𝒳f​μ​(d​x)\mu(f):=\int\_{\mathcal{X}}f\mu(dx).
By convention, XX is a column vector but q∈Cb​(Λ;ℝd)q\in C\_{b}(\Lambda;\mathbb{R}^{d}) is a row vector, with q​XqX denoting their scalar product.

Let 𝒫\mathcal{P} be the set of Borel probability measures on (Ω,ℱ1)(\Omega,\mathcal{F}\_{1}). We will work with measures ℙ\mathbb{P} under which XX is a semimartingale and we will need to define stochastic integrals ∫0⋅qt​𝑑Xt\int\_{0}^{\cdot}q\_{t}dX\_{t} simultaneously for many such ℙ\mathbb{P}’s, which may well be mutually singular. Naturally, this requires some restrictions on the integrand qq and/or on the measures considered. We defer the details to section [4](https://arxiv.org/html/2510.05463v1#S4 "4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time"). For now, we introduce the set 𝒬⊆𝒫\mathcal{Q}\subseteq\mathcal{P} of probability measures under which XX is a square integrable martingale.

### 2.1 The enlarged space

A key idea in the robust hedging of American options is to progressively encode the optimal stopping decision in the probability space and its filtration. It relies on observing that an American option in the original space can be, in a suitable sense, interpreted as a European option in an enlarged space, see El Karoui and Tan ([2013](https://arxiv.org/html/2510.05463v1#bib.bib24)); Aksamit et al. ([2019](https://arxiv.org/html/2510.05463v1#bib.bib1)). In this subsection, we will set up the appropriate enlarged space and establish the robust pricing-hedging duality for European options in this space.
Consider the set Θ⊂C​([0,1],ℝ)\Theta\subset C([0,1],\mathbb{R}) defined by

|  |  |  |
| --- | --- | --- |
|  | Θ:={ϑ∈C​([0,1],ℝ):ϑt=θ∧t, for some ​θ∈[0,1]}.\Theta:=\{\vartheta\in C([0,1],\mathbb{R}):\vartheta\_{t}=\theta\wedge t,\text{ for some }\theta\in[0,1]\}. |  |

The space Θ\Theta is isometric to [0,1][0,1], with an obvious bijection between θ∈[0,1]\theta\in[0,1] and ϑ∈Θ\vartheta\in\Theta via ϑ=θ∧⋅\vartheta=\theta\wedge\cdot or θ=ϑ1\theta=\vartheta\_{1}.
When there’s no confusion, we will simply use θ\theta to denote elements of Θ\Theta, while ϑ\vartheta is reserved when it is necessary to refer to the whole path.
Define the product space Ω¯:=Θ×Ω\bar{\Omega}:=\Theta\times\Omega, which is a subset of D​([0,1],ℝd+1)D([0,1],\mathbb{R}^{d+1}) and inherits its topology. Also extend the canonical process via X¯t​(ω¯)=(ϑt,Xt​(ω))\bar{X}\_{t}(\bar{\omega})=(\vartheta\_{t},X\_{t}(\omega)) and the canonical filtration to 𝔽¯\bar{\mathbb{F}}.
For each ω¯=(ϑ,ω)∈Ω¯\bar{\omega}=(\vartheta,\omega)\in\bar{\Omega}, let ω¯⋅∧t:=(ϑ⋅∧t,ω⋅∧t)\bar{\omega}\_{\cdot\wedge t}:=(\vartheta\_{\cdot\wedge t},\omega\_{\cdot\wedge t}) denote the stopped path at time tt.
Analogous to Λ\Lambda from the original space, we define Λ¯:={(t,ω¯⋅∧t):t∈[0,1],ω¯∈Ω¯}\bar{\Lambda}:=\{(t,\bar{\omega}\_{\cdot\wedge t}):t\in[0,1],\bar{\omega}\in\bar{\Omega}\}. As before, for convenience, we will often write elements of Λ¯\bar{\Lambda} as
(t,ω¯⋅∧t)=(t,ϑ⋅∧t,ω⋅∧t)=(t,θ∧t,ω⋅∧t)(t,\bar{\omega}\_{\cdot\wedge t})=(t,\vartheta\_{\cdot\wedge t},\omega\_{\cdot\wedge t})=(t,\theta\wedge t,\omega\_{\cdot\wedge t}).

Similar to before, let 𝒫¯\bar{\mathcal{P}} be the set of Borel probability measures on Ω¯\bar{\Omega} and let 𝒬¯⊂𝒫¯\bar{\mathcal{Q}}\subset\bar{\mathcal{P}} be the set of measures under which XX is a square integrable martingale.

## 3 Robust pricing of American options

In this section, we represent the robust price of an American option as the robust price of a corresponding European option in the enlarged space. Put differently, we show that optimising linear functionals on 𝒯×𝒬\mathcal{T}\times\mathcal{Q} is equivalent to optimising on the enlarged space 𝒬¯\bar{\mathcal{Q}}.
An American option payoff is given as a measurable function Z∈L0​(Λ)Z\in L^{0}(\Lambda), i.e., if exercised at time tt, the option pays Zt​(ω)=Z​(t,ωt∧⁣⋅)Z\_{t}(\omega)=Z(t,\omega\_{t\land\cdot}), and such an option can be naturally also exercised at a stopping time τ\tau and we write ZτZ\_{\tau} for its payoff Z​(τ​(ω),ω⋅∧τ​(ω))Z(\tau(\omega),\omega\_{\cdot\land\tau(\omega)}). Note also that ZZ naturally induces a random variable on Ω¯\bar{\Omega} via Z¯​(ω¯)=Z​(θ,ω⋅∧θ)\bar{Z}(\bar{\omega})=Z(\theta,\omega\_{\cdot\land\theta}), i.e., the composition of ZZ with the map

|  |  |  |
| --- | --- | --- |
|  | Ω¯∋ω¯=(ϑ,ω)⟶(ϑ1,ω⋅∧ϑ1)∈Λ,\bar{\Omega}\ni\bar{\omega}=(\vartheta,\omega)\longrightarrow(\vartheta\_{1},\omega\_{\cdot\land\vartheta\_{1}})\in\Lambda, |  |

which is continuous with our choice of norms.

For any E=(E1,E2)∈ℬ​(Ω)×ℬ​(Λ)E=(E\_{1},E\_{2})\in\mathcal{B}(\Omega)\times\mathcal{B}(\Lambda),
define E¯1:=Θ×E1∈ℬ​(Ω¯)\bar{E}\_{1}:=\Theta\times E\_{1}\in\mathcal{B}(\bar{\Omega}) and

|  |  |  |
| --- | --- | --- |
|  | E¯2={(t,θ∧t,X⋅∧t)∈Λ¯:(t,X⋅∧t)∈E2}∈ℬ​(Λ¯).\bar{E}\_{2}=\{(t,\theta\wedge t,X\_{\cdot\wedge t})\in\bar{\Lambda}:(t,X\_{\cdot\wedge t})\in E\_{2}\}\in\mathcal{B}(\bar{\Lambda}). |  |

Next, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒬E={ℙ∈𝒬:ℙ​(E1)=λ⊗ℙ​(E2)=1},𝒬¯E={ℙ¯∈𝒬¯:ℙ¯​(E¯1)=λ⊗ℙ¯​(E¯2)=1},\begin{split}\mathcal{Q}^{E}&=\{\mathbb{P}\in\mathcal{Q}:\mathbb{P}(E\_{1})=\lambda\otimes\mathbb{P}(E\_{2})=1\},\\ \bar{\mathcal{Q}}^{E}&=\{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}:\bar{\mathbb{P}}(\bar{E}\_{1})=\lambda\otimes\bar{\mathbb{P}}(\bar{E}\_{2})=1\},\end{split} |  | (1) |

where λ\lambda is the Lebesgue measure, so λ⊗ℙ∈𝒫​(Λ)\lambda\otimes\mathbb{P}\in\mathcal{P}(\Lambda) and λ⊗ℙ¯∈𝒫​(Λ¯)\lambda\otimes\bar{\mathbb{P}}\in\mathcal{P}(\bar{\Lambda}).

We state now our main result:

###### Theorem 3.1.

Let E1∈ℬ​(Ω)E\_{1}\in\mathcal{B}(\Omega) and E2∈ℬ​(Λ)E\_{2}\in\mathcal{B}(\Lambda).
Then for any Z∈L0​(Λ)Z\in L^{0}(\Lambda) and bounded from below, we have

|  |  |  |
| --- | --- | --- |
|  | supℙ∈𝒬E,τ∈𝒯ℙ𝔼ℙ​Zτ=supℙ¯∈𝒬¯E𝔼ℙ¯​Z​(θ,ω⋅∧θ).\sup\_{\mathbb{P}\in\mathcal{Q}^{E},\tau\in\mathcal{T}^{\mathbb{P}}}\mathbb{E}^{\mathbb{P}}Z\_{\tau}=\sup\_{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}}\mathbb{E}^{\bar{\mathbb{P}}}Z(\theta,\omega\_{\cdot\land\theta}). |  |

The set EE above is a technical device that will allow us to apply Theorem [3.1](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") to a variety of settings.
The proof of the theorem is split into two main steps. Lemma [3.8](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.1 Convexifying stopping times and measures ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") connects measures on Ω¯\bar{\Omega} to measures on Ω\Omega and stopping times. Lemma [3.10](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3.2 Preservation of the martingale property ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") ensures that the martingale property is preserved along the way. The latter, we feel, is the more subtle of the two steps. If one does not care about the preservation of the martingale property, then there are much more direct approaches to the first step.

### 3.1 Convexifying stopping times and measures

We are interested in pairs of the form (τ,ℙ)(\tau,\mathbb{P}) where ℙ\mathbb{P} belongs to some subset of probability measures on Ω\Omega and τ\tau is an 𝔽ℙ\mathbb{F}^{\mathbb{P}}-stopping time, τ∈𝒯ℙ\tau\in\mathcal{T}^{\mathbb{P}}.
Each pair (τ,ℙ)(\tau,\mathbb{P}) defines a linear map on the space of jointly measurable functions on (t,Ω)(t,\Omega) via ϕ→𝔼ℙ​(ϕτ)\phi\to\mathbb{E}^{\mathbb{P}}(\phi\_{\tau}).
In order to employ convex duality techniques to solve optimisation problems of the form sup(τ,ℙ)𝔼ℙ​(ϕτ)\sup\_{(\tau,\mathbb{P})}\mathbb{E}^{\mathbb{P}}(\phi\_{\tau}), we need to identify the convex hull of such pairs (τ,ℙ)(\tau,\mathbb{P}) or linear maps.
Since many problems have objectives or constraints on ℙ\mathbb{P}, the convexification should be done in a way that preserves the convexity of ℙ\mathbb{P} (or the induced linear map on measurable functions on Ω\Omega).

A natural approach (see e.g., El Karoui and Tan ([2013](https://arxiv.org/html/2510.05463v1#bib.bib24)); Aksamit et al. ([2019](https://arxiv.org/html/2510.05463v1#bib.bib1))) is to identify (τ,ℙ)(\tau,\mathbb{P}) with a measure from 𝒫​(Ω¯)\mathcal{P}(\bar{\Omega}). However, a general element in 𝒫​(Ω¯)\mathcal{P}(\bar{\Omega}) usually corresponds to a random time (not even a randomised stopping time, see Example [3.3](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem3 "Example 3.3. ‣ 3.1 Convexifying stopping times and measures ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time")). The approach of Aksamit et al. ([2019](https://arxiv.org/html/2510.05463v1#bib.bib1)) overcomes this by explicitly constructing an optimal stopping time via backward induction in discrete time, which cannot be applied in continuous time settings.
Our approach is to use 𝒫​(Ω¯)\mathcal{P}(\bar{\Omega}) as well and to use the non-anticipative nature of American payoffs together with the martingale property of our pricing measures to show that we can indeed restrict to randomised stopping times.

###### Definition 3.2.

A *randomised stopping time* is an (Ω,𝔽)(\Omega,\mathbb{F})-adapted, right-continuous, increasing process AA with A0=0A\_{0}=0 and A1=1A\_{1}=1.

Randomised stopping times have been studied in
Baxter and Chacon ([1977](https://arxiv.org/html/2510.05463v1#bib.bib5)), see also Meyer ([1978](https://arxiv.org/html/2510.05463v1#bib.bib44)), and in many works since, see Beiglböck et al. ([2016](https://arxiv.org/html/2510.05463v1#bib.bib9)) for a good discussion in relation to OT methods for Skorokhod embeddings. If τ\tau is an 𝔽\mathbb{F}-stopping time, then Atτ=𝟙τ≤tA^{\tau}\_{t}=\mathds{1}\_{\tau\leq t} is a randomised stopping time which has a particularly simple structure: it is equal to zero and then jumps to one at time τ\tau. More generally, AtA\_{t} can be interpreted as the proportion of mass that has been stopped along each path by the time tt. The non-anticipative property of AA helps eliminate the possibility of random times that are not randomised stopping times. Our aim is to extract an appropriate non-anticipative AA from each μ∈𝒫​(Ω¯)\mu\in\mathcal{P}(\bar{\Omega}). First however, we give a simple example to show that naive convexification of pairs (τ,ℙ)(\tau,\mathbb{P}) would not result in randomised stopping times.

###### Example 3.3.

Consider two pairs of stopping times and martingale measures, (τ,ℙ)(\tau,\mathbb{P}) and (τ′,ℙ′)(\tau^{\prime},\mathbb{P}^{\prime}), where τ=0\tau=0, τ′=1\tau^{\prime}=1, ℙ\mathbb{P} is the law of a constant process, and ℙ′\mathbb{P}^{\prime} is the law of the same constant process on t∈[0,1/2]t\in[0,1/2] followed by a Brownian motion on t∈[1/2,1]t\in[1/2,1]. Let ℙ¯=δ0⊗ℙ\bar{\mathbb{P}}=\delta\_{0}\otimes\mathbb{P} and ℙ¯′=δ1⊗ℙ′\bar{\mathbb{P}}^{\prime}=\delta\_{1}\otimes\mathbb{P}^{\prime} be the corresponding measures in the enlarged space. The average ℙ¯′′=(ℙ¯+ℙ¯′)/2\bar{\mathbb{P}}^{\prime\prime}=(\bar{\mathbb{P}}+\bar{\mathbb{P}}^{\prime})/2 is a martingale measure, however its θ\theta component does not correspond to a stopping time or a randomised stopping time, as it requires the knowledge of the process from t=1/2t=1/2 to determine the stopping decision at t=0t=0. In particular, at t=0t=0 it will immediately stop all paths that will be constant on t∈[1/2,1]t\in[1/2,1]. However, at time t=0t=0, it is not possible to distinguish those paths from those which will follow a Brownian motion on [1/2,1][1/2,1].

We recall the following simple properties of randomised stopping times.

###### Lemma 3.4 (Shmaya and Solan ([2014](https://arxiv.org/html/2510.05463v1#bib.bib55))).

Let AA be a randomised stopping time and for each r∈[0,1]r\in[0,1], define τr=inf{t≥0:At≥r}\tau\_{r}=\operatorname\*{\vphantom{p}inf}\{t\geq 0:A\_{t}\geq r\}. Then (τr,r∈[0,1])(\tau\_{r},r\in[0,1]) is a non-decreasing family of stopping times and

|  |  |  |
| --- | --- | --- |
|  | At(ω)=λ(r∈[0,1]:τr(ω)≤t),t∈[0,1],A\_{t}(\omega)=\lambda({r\in[0,1]:\tau\_{r}(\omega)\leq t}),\quad t\in[0,1], |  |

where λ\lambda is the Lebesgue measure. Consequently, for any η∈L∞​(Ω¯)\eta\in L^{\infty}(\bar{\Omega}),

|  |  |  |
| --- | --- | --- |
|  | ∫01η​(θ,ω)​𝑑Aθ=∫01η​(τr,ω)​𝑑r.\int\_{0}^{1}\eta(\theta,\omega)\,dA\_{\theta}=\int\_{0}^{1}\eta(\tau\_{r},\omega)\,dr. |  |

We also need to recall the Itô–Watanabe multiplicative decomposition of non-negative supermartingales.

###### Theorem 3.5 (Itô and Watanabe ([1965](https://arxiv.org/html/2510.05463v1#bib.bib37))).

Let ξ\xi be a non-negative right continuous supermartingale with ξ0>0\xi\_{0}>0 defined on a filtered probability space satisfying the usual hypothesis. Then ξ\xi has the decomposition

|  |  |  |
| --- | --- | --- |
|  | ξ=M​A\xi=MA |  |

with a positive local martingale MM and a natural decreasing process AA. If there are two such factorisations, then they are identical up to Tξ=inf{t≥0:ξt=0}T\_{\xi}=\operatorname\*{\vphantom{p}inf}\{t\geq 0:\xi\_{t}=0\}.

Furthermore, if there exists a constant K>0K>0 and an almost surely finite stopping time TT such that 1/K≤ξt≤K1/K\leq\xi\_{t}\leq K for t<Tt<T and ξt=ξT\xi\_{t}=\xi\_{T} for t≥Tt\geq T, then the local martingale MM in the decomposition is a (true) martingale.

The distinction between local and true martingale in Theorem [3.5](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem5 "Theorem 3.5 (Itô and Watanabe (1965)). ‣ 3.1 Convexifying stopping times and measures ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") actually creates some difficulties for us, but we will work around it by focusing on the following type of measures in 𝒫​(Ω¯)\mathcal{P}(\bar{\Omega}).

###### Definition 3.6.

For ϵ∈(0,1)\epsilon\in(0,1), we say that μ∈𝒫​(Ω¯)\mu\in\mathcal{P}(\bar{\Omega}) is *ϵ\epsilon-modified* if μ​({1}×Γ)≥ϵ​μΩ​(Γ)\mu(\{1\}\times\Gamma)\geq\epsilon\mu^{\Omega}(\Gamma) for any Γ∈ℱ1\Gamma\in\mathcal{F}\_{1}, and where μΩ\mu^{\Omega} is the Ω\Omega-marginal of μ\mu.

###### Lemma 3.7.

Let ϵ∈(0,1)\epsilon\in(0,1), μ∈𝒫​(Ω¯)\mu\in\mathcal{P}(\bar{\Omega}) and δ1∈𝒫​([0,1])\delta\_{1}\in\mathcal{P}([0,1]) be the Dirac mass at 1. Then μϵ:=(1−ϵ)​μ+ϵ​(δ1×μΩ)\mu^{\epsilon}:=(1-\epsilon)\mu+\epsilon(\delta\_{1}\times\mu^{\Omega}) is ϵ\epsilon-modified and has the same Ω\Omega-marginal as μ\mu. In addition, if μ∈𝒬¯E\mu\in\bar{\mathcal{Q}}^{E} then μϵ∈𝒬¯E\mu^{\epsilon}\in\bar{\mathcal{Q}}^{E}.

The proof is immediate and we omit the details. We call μϵ\mu^{\epsilon} the ϵ\epsilon-modification of μ\mu. In our proofs, we will establish the desired statements for μϵ\mu^{\epsilon} and take ϵ↘0\epsilon\searrow 0.

The following lemma is the first step in the proof of Theorem [3.1](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time"). It shows that when the American payoff is adapted we can identify a measure on Ω¯\bar{\Omega} with a measure on Ω\Omega and a randomised stopping time. This randomised stopping time is extracted by applying the multiplicative decomposition to an Azéma supermatingale (Azéma ([1972](https://arxiv.org/html/2510.05463v1#bib.bib4))), a technique also used in Li et al. ([2022](https://arxiv.org/html/2510.05463v1#bib.bib42)) in the context of option pricing with default risks. In the subsequent section we will look at the martingale property of such measures.

###### Lemma 3.8.

Let μ∈𝒫​(Ω¯)\mu\in\mathcal{P}(\bar{\Omega}) be ϵ\epsilon-modified. Then there exists a probability measure ℙ∈𝒫​(Ω)\mathbb{P}\in\mathcal{P}(\Omega) equivalent to μΩ\mu^{\Omega} and a right-continuous, increasing and 𝔽ℙ\mathbb{F}^{\mathbb{P}}-adapted process AA with A0=0A\_{0}=0 and A1=1A\_{1}=1, such that for every 𝔽ℙ\mathbb{F}^{\mathbb{P}}-adapted process ψ\psi,

|  |  |  |
| --- | --- | --- |
|  | μ​(ψθ​(ω))=𝔼ℙ​∫01ψt​𝑑At.\mu(\psi\_{\theta}(\omega))=\mathbb{E}^{\mathbb{P}}\int\_{0}^{1}\psi\_{t}\,dA\_{t}. |  |

This can be written as

|  |  |  |
| --- | --- | --- |
|  | μ​(ψθ​(ω))=𝔼ℙ​∫01ψτr​𝑑r.\mu(\psi\_{\theta}(\omega))=\mathbb{E}^{\mathbb{P}}\int\_{0}^{1}\psi\_{\tau\_{r}}\,dr. |  |

for a family of 𝔽ℙ\mathbb{F}^{\mathbb{P}}-stopping times {τr}r\{\tau\_{r}\}\_{r} that satisfies τr=1\tau\_{r}=1 for r>1−ϵr>1-\epsilon.

###### Proof.

Instead of ψ\psi, it suffices to check functions of the form ψt=𝟙​(t>s,ω∈Γ)\psi\_{t}=\mathds{1}(t>s,\omega\in\Gamma) for any fixed ss and any Γ∈ℱsμΩ\Gamma\in\mathcal{F}^{\mu\_{\Omega}}\_{s}.

Define the raw IV process RR from μ\mu (by say, disintegrating in ω\omega and taking the distribution functions with respect to θ\theta), so

|  |  |  |
| --- | --- | --- |
|  | ∫Ω¯𝟙​(θ>s,ω∈Γ)​𝑑μ=𝔼μΩ​((1−Rs)​𝟙​(ω∈Γ)),s∈[0,1].\int\_{\bar{\Omega}}\mathds{1}(\theta>s,\omega\in\Gamma)\,d\mu=\mathbb{E}^{\mu\_{\Omega}}\big((1-R\_{s})\mathds{1}(\omega\in\Gamma)\big),\quad s\in[0,1]. |  |

Let Rto:=𝔼μΩ​(Rt|ℱtμΩ){}^{o}R\_{t}:=\mathbb{E}^{\mu\_{\Omega}}(R\_{t}\,|\,\mathcal{F}^{\mu\_{\Omega}}\_{t}) be the optional projection of RR. Then 1−Ro1-{}^{o}R is a non-negative μΩ\mu\_{\Omega}-supermartingale, and in particular we can and will work with its rcll version,
often known as the Azéma supermartingale after Azéma ([1972](https://arxiv.org/html/2510.05463v1#bib.bib4)).
Moreover, since μ\mu is ϵ\epsilon-modified, 1≥1−R1o>ϵ1\geq 1-{}^{o}R\_{1}>\epsilon.
By Theorem [3.5](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem5 "Theorem 3.5 (Itô and Watanabe (1965)). ‣ 3.1 Convexifying stopping times and measures ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time"), it admits a multiplicative decomposition 1−Ro=M​(1−A)1-{}^{o}R=M(1-A), for some positive (𝔽μΩ,μΩ)(\mathbb{F}^{\mu\_{\Omega}},\mu\_{\Omega})-martingale MM and an increasing 𝔽μΩ\mathbb{F}^{\mu\_{\Omega}}-adapted process AA with M0=1,A0=0,A1=1M\_{0}=1,A\_{0}=0,A\_{1}=1. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼μΩ​((1−Rs)​𝟙​(ω∈Γ))\displaystyle\mathbb{E}^{\mu\_{\Omega}}\big((1-R\_{s})\mathds{1}(\omega\in\Gamma)\big) | =𝔼μΩ​((1−Rso)​𝟙​(ω∈Γ))\displaystyle=\mathbb{E}^{\mu\_{\Omega}}\big((1-{}^{o}R\_{s})\mathds{1}(\omega\in\Gamma)\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼μΩ​(Ms​(1−As)​𝟙​(ω∈Γ))\displaystyle=\mathbb{E}^{\mu\_{\Omega}}\big(M\_{s}(1-A\_{s})\mathds{1}(\omega\in\Gamma)\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ​((1−As)​𝟙​(ω∈Γ)),\displaystyle=\mathbb{E}^{\mathbb{P}}\big((1-A\_{s})\mathds{1}(\omega\in\Gamma)\big), |  |

where d​ℙ/d​μΩ=M1d\mathbb{P}/d\mu\_{\Omega}=M\_{1}.
The last part follows from Lemma [3.4](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem4 "Lemma 3.4 (Shmaya and Solan (2014)). ‣ 3.1 Convexifying stopping times and measures ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time").
∎

###### Remark 3.9.

The above proposition has the following interpretation.
We showed that every measure in 𝒫​(Ω¯)\mathcal{P}(\bar{\Omega}) is equivalent to some measure in 𝒫​(Λ)\mathcal{P}(\Lambda), when tested only against non-anticipative functions. The measure from 𝒫​(Λ)\mathcal{P}(\Lambda) is then equivalent to a pair (A,ℙ)(A,\mathbb{P}) where AA characterises a randomised stopping time, while ℙ\mathbb{P} is only uniquely determined until the randomised stopping time finishes. This makes sense since elements of Λ\Lambda cannot see into the future.

### 3.2 Preservation of the martingale property

Now we will see that if μ\mu was a martingale measure in 𝒫​(Ω¯)\mathcal{P}(\bar{\Omega}), then ℙ\mathbb{P} in Lemma [3.8](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.1 Convexifying stopping times and measures ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") is also a martingale measure in 𝒫​(Ω)\mathcal{P}(\Omega) with the same characteristics on Ω\Omega.

###### Lemma 3.10.

Let μ∈𝒬¯\mu\in\bar{\mathcal{Q}} be ϵ\epsilon-modified.
Then ℙ\mathbb{P} from Lemma [3.8](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.1 Convexifying stopping times and measures ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") satisfies ℙ∈𝒬\mathbb{P}\in\mathcal{Q}. If in addition μ∈𝒬¯E\mu\in\bar{\mathcal{Q}}^{E}, then ℙ∈𝒬E\mathbb{P}\in\mathcal{Q}^{E}.

###### Proof.

Take ℙ\mathbb{P} and {τr}r∈[0,1]\{\tau\_{r}\}\_{r\in[0,1]} from Lemma [3.8](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.1 Convexifying stopping times and measures ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time"). Since τr:Ω→ℝ\tau\_{r}:\Omega\to\mathbb{R} is an 𝔽ℙ\mathbb{F}^{\mathbb{P}}-stopping time (and hence 𝔽μΩ\mathbb{F}^{\mu\_{\Omega}}-stopping time), its (obvious) embedding as a map Ω¯→ℝ\bar{\Omega}\to\mathbb{R} is an 𝔽¯μ\bar{\mathbb{F}}^{\mu}-stopping time. This follows from the fact that if Γ\Gamma is a null set under μΩ\mu\_{\Omega}, then Θ×Γ\Theta\times\Gamma is a null set under μ\mu.

For any s,a∈[0,1]s,a\in[0,1] and Γ∈ℱsℙ\Gamma\in\mathcal{F}^{\mathbb{P}}\_{s}, we let ℐt​(ω):=𝟙Γ​(ω)​𝟙(s,1]​(t)​(Xt−Xs)\mathcal{I}\_{t}(\omega):=\mathds{1}\_{\Gamma}(\omega)\mathds{1}\_{(s,1]}(t)(X\_{t}-X\_{s}) and note that t→ℐt∧τat\to\mathcal{I}\_{t\wedge\tau\_{a}} is an 𝔽ℙ\mathbb{F}^{\mathbb{P}}-adapted process. We will show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫a1𝔼ℙ​(𝟙Γ​𝟙τr>s​(Xτr−Xs))​𝑑r=∫a1𝔼ℙ​(ℐτr)​𝑑r=0.\displaystyle\int\_{a}^{1}\mathbb{E}^{\mathbb{P}}(\mathds{1}\_{\Gamma}\mathds{1}\_{\tau\_{r}>s}(X\_{\tau\_{r}}-X\_{s}))\,dr=\int\_{a}^{1}\mathbb{E}^{\mathbb{P}}(\mathcal{I}\_{\tau\_{r}})\,dr=0. |  | (2) |

Recall that since μ\mu is ϵ\epsilon-modified, we have τa=1\tau\_{a}=1 for any 1>a>1−ϵ1>a>1-\epsilon. Choosing such an aa shows that for each s<1s<1, 𝔼ℙ​(𝟙Γ​(X1−Xs))=0\mathbb{E}^{\mathbb{P}}(\mathds{1}\_{\Gamma}(X\_{1}-X\_{s}))=0, thus XX is an (𝔽ℙ,ℙ)(\mathbb{F}^{\mathbb{P}},\mathbb{P})-martingale.

It remains to establish ([2](https://arxiv.org/html/2510.05463v1#S3.E2 "In 3.2 Preservation of the martingale property ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time")). By the optional stopping theorem

|  |  |  |
| --- | --- | --- |
|  | μ​(ℐθ∧τa)=0.\mu(\mathcal{I}\_{\theta\wedge\tau\_{a}})=0. |  |

This is because both θ\theta and τa\tau\_{a} are ℱ¯μ\bar{\mathcal{F}}^{\mu}-stopping times, 𝟙Γ​𝟙​(θ∧τa>s)\mathds{1}\_{\Gamma}\mathds{1}(\theta\wedge\tau\_{a}>s) is ℱ¯sμ\bar{\mathcal{F}}^{\mu}\_{s} measurable, while XX is an (𝔽¯,μ)(\bar{\mathbb{F}},\mu)- and hence (𝔽¯μ,μ)(\bar{\mathbb{F}}^{\mu},\mu)-martingale.
Applying Lemmas [3.4](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem4 "Lemma 3.4 (Shmaya and Solan (2014)). ‣ 3.1 Convexifying stopping times and measures ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time"), [3.8](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.1 Convexifying stopping times and measures ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") and Fubini’s theorem,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=μ​(ℐθ∧τa)\displaystyle 0=\mu(\mathcal{I}\_{\theta\wedge\tau\_{a}}) | =𝔼ℙ​∫01ℐt∧τa​𝑑At=∫01𝔼ℙ​(ℐτr∧τa)​𝑑r\displaystyle=\mathbb{E}^{\mathbb{P}}\int\_{0}^{1}\mathcal{I}\_{t\wedge\tau\_{a}}\,dA\_{t}=\int\_{0}^{1}\mathbb{E}^{\mathbb{P}}(\mathcal{I}\_{\tau\_{r}\wedge\tau\_{a}})\,dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0a𝔼ℙ​(ℐτr)​𝑑r+(1−a)​𝔼ℙ​(ℐτa).\displaystyle=\int\_{0}^{a}\mathbb{E}^{\mathbb{P}}(\mathcal{I}\_{\tau\_{r}})\,dr+(1-a)\mathbb{E}^{\mathbb{P}}(\mathcal{I}\_{\tau\_{a}}). |  |

Let Cr=𝔼ℙ​(ℐτr)C\_{r}=\mathbb{E}^{\mathbb{P}}(\mathcal{I}\_{\tau\_{r}}), we arrive at the equation

|  |  |  |
| --- | --- | --- |
|  | 1a−1​∫0aCr​𝑑r=Ca.\frac{1}{a-1}\int\_{0}^{a}C\_{r}\,dr=C\_{a}. |  |

Hence CaC\_{a} is differentiable for a<1a<1. Multiplying both sides by (a−1)(a-1) and differentiating,

|  |  |  |
| --- | --- | --- |
|  | Ca=Ca+(a−1)​∂aCa⟹∂aCa=0,a<1.C\_{a}=C\_{a}+(a-1)\partial\_{a}C\_{a}\quad\implies\quad\partial\_{a}C\_{a}=0,\ a<1. |  |

The only possible solution is Cr=0C\_{r}=0 for r<1r<1.
Therefore our claim ([2](https://arxiv.org/html/2510.05463v1#S3.E2 "In 3.2 Preservation of the martingale property ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time")) is proven.

Finally, if μ∈𝒬¯E\mu\in\bar{\mathcal{Q}}^{E}, then by definition μΩ∈𝒬E\mu\_{\Omega}\in\mathcal{Q}^{E}. Since ℙ\mathbb{P} is absolutely continuous with respect to μΩ\mu\_{\Omega}, we also have ℙ∈𝒬E\mathbb{P}\in\mathcal{Q}^{E}.
∎

###### Proof of Theorem [3.1](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time").

Given each ℙ∈𝒬E\mathbb{P}\in\mathcal{Q}^{E} and τ∈𝒯ℙ\tau\in\mathcal{T}^{\mathbb{P}}, we can define ℙ¯∈ℳ​(Ω¯)\bar{\mathbb{P}}\in\mathcal{M}(\bar{\Omega}) to be the pushforward measure of ℙ\mathbb{P} with respect to the map ω→(τ​(ω),ω)\omega\to(\tau(\omega),\omega). It is straightforward to check that ℙ¯∈𝒬¯E\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E} and hence

|  |  |  |
| --- | --- | --- |
|  | supℙ∈𝒬E,τ∈𝒯ℙ𝔼ℙ​Z​(τ,ω)≤supℙ¯∈𝒬¯E𝔼ℙ¯​Z​(θ,ω).\sup\_{\mathbb{P}\in\mathcal{Q}^{E},\tau\in\mathcal{T}^{\mathbb{P}}}\mathbb{E}^{\mathbb{P}}Z(\tau,\omega)\leq\sup\_{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}}\mathbb{E}^{\bar{\mathbb{P}}}Z(\theta,\omega). |  |

For the reverse direction, we first show that it suffices to only focus on ϵ\epsilon-modified measures. Note that ℙ¯∈𝒬¯E\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E} implies that ℙ¯ϵ∈𝒬¯E\bar{\mathbb{P}}^{\epsilon}\in\bar{\mathcal{Q}}^{E}.
Since ZZ is bounded below, there exists some constant CC such that 𝔼ℙ¯ϵ​Z≥(1−ϵ)​𝔼ℙ¯​Z+ϵ​C\mathbb{E}^{\bar{\mathbb{P}}^{\epsilon}}Z\geq(1-\epsilon)\mathbb{E}^{\bar{\mathbb{P}}}Z+\epsilon C. So if we can prove

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ¯ϵ​Z≤supℙ∈𝒬E,τ∈𝒯ℙ𝔼ℙ​Z​(τ,ω),\mathbb{E}^{\bar{\mathbb{P}}^{\epsilon}}Z\leq\sup\_{\mathbb{P}\in\mathcal{Q}^{E},\tau\in\mathcal{T}^{\mathbb{P}}}\mathbb{E}^{\mathbb{P}}Z(\tau,\omega), |  |

for every such ℙ¯ϵ\bar{\mathbb{P}}^{\epsilon}, the we can complete the proof by taking ϵ→0\epsilon\to 0.

So, without loss of generality, assume that ℙ¯∈𝒬¯E\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E} is already ϵ\epsilon-modified. By Lemma [3.8](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.1 Convexifying stopping times and measures ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time"), to ℙ¯\bar{\mathbb{P}} we can associate ℙ∈𝒫\mathbb{P}\in\mathcal{P} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ¯​Z​(θ,ω)=∫01𝔼ℙ​Z​(τr,ω)​𝑑r.\mathbb{E}^{\bar{\mathbb{P}}}Z(\theta,\omega)=\int\_{0}^{1}\mathbb{E}^{\mathbb{P}}Z(\tau\_{r},\omega)\,dr. |  |

Applying Lemma [3.10](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3.2 Preservation of the martingale property ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time"), we deduce that ℙ∈𝒬E\mathbb{P}\in\mathcal{Q}^{E}.
We conclude that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ¯​Z​(θ,ω)≤ess​supr∈[0,1]⁡𝔼ℙ​Z​(τr,ω)≤supℙ∈𝒬E,τ∈𝒯ℙ𝔼ℙ​Z​(τ,ω).\mathbb{E}^{\bar{\mathbb{P}}}Z(\theta,\omega)\leq\operatornamewithlimits{ess\,sup}\_{r\in[0,1]}\mathbb{E}^{\mathbb{P}}Z(\tau\_{r},\omega)\leq\sup\_{\mathbb{P}\in\mathcal{Q}^{E},\tau\in\mathcal{T}^{\mathbb{P}}}\mathbb{E}^{\mathbb{P}}Z(\tau,\omega). |  |

Since this holds for every ZZ, our proof is complete. Note that we have established, in particular, that 𝒬E=∅\mathcal{Q}^{E}=\emptyset if and only if 𝒬¯E=∅\bar{\mathcal{Q}}^{E}=\emptyset.
∎

###### Remark 3.11.

Fix a random variable g:Ω→ℝg:\Omega\to\mathbb{R}. Define 𝒬gE:=𝒬E∩{ℙ:𝔼ℙ​(g)=0}\mathcal{Q}^{E}\_{g}:=\mathcal{Q}^{E}\cap\{\mathbb{P}:\mathbb{E}^{\mathbb{P}}(g)=0\} and 𝒬¯gE:=𝒬¯E∩{ℙ¯:𝔼ℙ¯​(g)=0}\bar{\mathcal{Q}}^{E}\_{g}:=\bar{\mathcal{Q}}^{E}\cap\{\bar{\mathbb{P}}:\mathbb{E}^{\bar{\mathbb{P}}}(g)=0\}.
We cannot apply Theorem [3.1](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") to the set 𝒬gE\mathcal{Q}^{E}\_{g}. In fact, we may have

|  |  |  |
| --- | --- | --- |
|  | supℙ∈𝒬gE,τ∈𝒯ℙ𝔼ℙ​Z​(τ,ω)<supℙ¯∈𝒬¯gE𝔼ℙ¯​Z​(θ,ω).\sup\_{\mathbb{P}\in\mathcal{Q}^{E}\_{g},\tau\in\mathcal{T}^{\mathbb{P}}}\mathbb{E}^{\mathbb{P}}Z(\tau,\omega)<\sup\_{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}\_{g}}\mathbb{E}^{\bar{\mathbb{P}}}Z(\theta,\omega). |  |

The inequality may arise because when we construct the measure ℙ\mathbb{P} from ℙ¯Ω\bar{\mathbb{P}}\_{\Omega}, there is no guarantee that the constraint 𝔼ℙ​g=0\mathbb{E}^{\mathbb{P}}g=0 is preserved. This is further explored in section [4.3](https://arxiv.org/html/2510.05463v1#S4.SS3 "4.3 Duality gap and a dynamic extension for statically traded European options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time"), which shows that when static European options are included, there could be a duality gap between the robust hedging and robust pricing. Both will follow from Example [4.3](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem3 "Example 4.3. ‣ 4.3 Duality gap and a dynamic extension for statically traded European options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time") and Theorem [5.2](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem2 "Theorem 5.2. ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time").

## 4 Robust hedging of American options and weak pricing-hedging duality

### 4.1 Pathwise stochastic integration

Dynamic trading is described through stochastic integrals, so we need to define ∫0⋅qt​𝑑Xt\int\_{0}^{\cdot}q\_{t}dX\_{t} simultaneously for many martingale measures ℙ\mathbb{P}’s, which may well be mutually singular. This requires some restrictions on the objects we consider. In our setup, we can naturally restrict to suitably continuous integrands qq and define the stochastic integrals pathwise as limits of certain discrete Riemann-sum approximations, setting the integrals to be zero if limits are not defined. A successful construction simply has to ensure that the set of paths for which the limits exist has full ℙ\mathbb{P}-measure, for all ℙ\mathbb{P}’s considered, and the pathwise integrals coincide ℙ\mathbb{P}-a.s. with their classical Itô counterparts. Such an approach to pathwise integration has been considered in many works; see Karandikar ([1995](https://arxiv.org/html/2510.05463v1#bib.bib38)); Föllmer ([1981](https://arxiv.org/html/2510.05463v1#bib.bib25)); Peng ([2019](https://arxiv.org/html/2510.05463v1#bib.bib51)); Denis and Martini ([2006](https://arxiv.org/html/2510.05463v1#bib.bib19)); Davis et al. ([2018](https://arxiv.org/html/2510.05463v1#bib.bib18)); Perkowski and Prömel ([2015](https://arxiv.org/html/2510.05463v1#bib.bib52)); Cont and Fournié ([2013](https://arxiv.org/html/2510.05463v1#bib.bib15)). It is worth noting that a different approach to this question of *aggregation* was proposed in Soner et al. ([2013](https://arxiv.org/html/2510.05463v1#bib.bib56)) who worked with the properties of the set of measures considered instead.

For our purposes, Karandikar ([1995](https://arxiv.org/html/2510.05463v1#bib.bib38)) provides the most elegant and simplest aggregation method. Given two functions ρ,η\rho,\eta on [0,t][0,t], ρ\rho right-continuous and with left limits (rcll), or left-continuous with right limits (lcrl) and η\eta rcll, their integral ρ⋅η\rho\bm{\cdot}\eta is defined as a rcll function on [0,t][0,t], and (ρ⋅η)t=(ρ~⋅η)t(\rho\bm{\cdot}\eta)\_{t}=(\tilde{\rho}\bm{\cdot}\eta)\_{t} if ρ\rho and ρ~\tilde{\rho} are versions of each other with different (right- or left-) continuity properties. In fact, ρ⋅η\rho\bm{\cdot}\eta is given as the limit, in the topology of uniform convergence, of ρn⋅η\rho^{n}\bm{\cdot}\eta, where ρn\rho^{n} is piece-wise constant and hence the integral is simply a sum, with ρ⋅η=0\rho\bm{\cdot}\eta=0 on the set where the sequence does not converge. The latter is the same as the set where the sequence is not Cauchy and is a measurable set in ℱt\mathcal{F}\_{t}. It is also a null set under any semimartingale measure, since by (Karandikar, [1995](https://arxiv.org/html/2510.05463v1#bib.bib38), Thm. 3) this pathwise construction a.s. coincides with the Itô stochastic integral of an adapted rcll (or lcrl) process against a continuous semimartingale, both defined on some filtered probability space satisfying the usual hypothesis. We also note that if we consider the construction on [0,s][0,s] and [0,t][0,t], with s<ts<t, then the two approximations ρn⋅η\rho^{n}\bm{\cdot}\eta coincide on [0,s][0,s]. It follows that (ρ⋅η)t∈[0,1](\rho\bm{\cdot}\eta)\_{t\in[0,1]} is a measurable map on Λ\Lambda, i.e., is progressively measurable and has continuous paths on the (ℱ1\mathcal{F}\_{1}–measurable) set where the approximations converge uniformly on [0,1][0,1]. This justifies our use of the integral notation, we write:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (q​(ω)⋅X​(ω))t=∫0tqs​(ω)​𝑑Xs​(ω)=(∫0tqs​𝑑Xs)​(ω),(q(\omega)\bm{\cdot}X(\omega))\_{t}=\int\_{0}^{t}q\_{s}(\omega)dX\_{s}(\omega)=\left(\int\_{0}^{t}q\_{s}dX\_{s}\right)(\omega), |  | (3) |

where usually q∈C​(Λ)q\in C(\Lambda) and the process qt​(ω):=q​(t,ω⋅∧t)q\_{t}(\omega):=q(t,\omega\_{\cdot\land t}), t∈[0,1]t\in[0,1] has continuous paths for all ω∈Ω\omega\in\Omega and is 𝔽\mathbb{F}-progressively measurable. For q∈C​(Λ;ℝd)q\in C(\Lambda;\mathbb{R}^{d}) and XX an ℝd\mathbb{R}^{d} valued process, the integrals are defined component-wise.

### 4.2 Robust superhedging of American Options

We return now to the problem of superhedging an American option with payoff Z∈Cb​(Λ)Z\in C\_{b}(\Lambda). The seller of the option wants to robustly hedge their exposure. They can trade dynamically in the underlying XX and, since they observe the exercise time, can also adjust the hedging strategy accordingly: we start with a hedging strategy qq and switch to quq^{u} if the option is exercised at time uu. To parametrise the latter, we introduce the set

|  |  |  |
| --- | --- | --- |
|  | Λ¯≥={(t,u,ωt∧⁣⋅):u∈[0,1],t∈[u,1],ω∈Ω}⊆Λ¯,\bar{\Lambda}\_{\geq}=\{(t,u,\omega\_{t\land\cdot}):u\in[0,1],t\in[u,1],\omega\in\Omega\}\subseteq\bar{\Lambda}, |  |

with metric inherited from Λ¯\bar{\Lambda}. We recall the sets of martingale measures 𝒬E\mathcal{Q}^{E} and 𝒬¯E\bar{\mathcal{Q}}^{E} defined in ([1](https://arxiv.org/html/2510.05463v1#S3.E1 "In 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time")). We will later use E2E\_{2} to encode the seller’s pathwise beliefs about the range of asset behaviour they want to hedge against. In addition, the seller can trade statically in the European options at their market prices observed today. Without any loss of generality, we can assume these options have zero prices today since, as we ignore transaction costs, we can simply shift the options’ payoffs by their true prices. The options’ payoffs are thus given by some g∈Cb​(Ω;ℝm)g\in C\_{b}(\Omega;\mathbb{R}^{m}), where we assume gg is bounded to be able to later apply OT-duality methods, see Proposition [5.4](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem4 "Proposition 5.4 (Guo and Loeper (2021)). ‣ 5.1 Duality for European options ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time").
Naturally, the motivating example is that of gg being a vector of put payoffs, call options being converted to puts via call-put parity. Finally, the set of calibrated martingale measures is given by 𝒬gE={ℙ∈𝒬E:𝔼ℙ​(g)=0}\mathcal{Q}^{E}\_{g}=\{\mathbb{P}\in\mathcal{Q}^{E}:\mathbb{E}^{\mathbb{P}}(g)=0\}. We recall also that for ℙ∈𝒬\mathbb{P}\in\mathcal{Q}, 𝔽ℙ\mathbb{F}^{\mathbb{P}} is the right-continuous and completed version of the natural filtration. Throughout this section we assume that 𝒬E\mathcal{Q}^{E}, 𝒬gE\mathcal{Q}^{E}\_{g} are non-empty.

The superhedging price of the American option is defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πg,EA(Z):=inf{\displaystyle\pi^{A}\_{g,E}(Z):=\operatorname\*{\vphantom{p}inf}\bigg\{ | x:∃(q,q~,h)∈Cb​(Λ;ℝd)×Cb​(Λ¯≥;ℝd)×ℝm,s.t.​x+∫0uq​(t,ωt∧⁣⋅)​𝑑Xt​(ω)\displaystyle x:\exists(q,\tilde{q},h)\in C\_{b}(\Lambda;\mathbb{R}^{d})\times C\_{b}(\bar{\Lambda}\_{\geq};\mathbb{R}^{d})\times\mathbb{R}^{m},\ \text{s.t.}\ x+\int\_{0}^{u}q(t,\omega\_{t\land\cdot})dX\_{t}(\omega) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫u1q~u(t,ωt∧⁣⋅)dXt(ω)+hg≥Z(u,ω⋅∧u),∀u∈[0,1],𝒬gE(dω)-q.s.},\displaystyle\quad+\int\_{u}^{1}\tilde{q}^{u}(t,\omega\_{t\land\cdot})dX\_{t}(\omega)+hg\geq Z(u,\omega\_{\cdot\wedge u}),\ \forall\,u\in[0,1],\ \mathcal{Q}^{E}\_{g}(d\omega)\text{-\text{q.s.}}\bigg\}, |  |

where 𝒬gE​-q.s.\mathcal{Q}^{E}\_{g}\text{-\text{q.s.}} means ℙ\mathbb{P}-a.s. for any ℙ∈𝒬gE\mathbb{P}\in\mathcal{Q}^{E}\_{g}.
When we want to stress the dependence on the set restrictions on the martingale test measures, we write πg,EA​(Z)\pi^{A}\_{g,E}(Z).
On the other hand, when there are no traded European options, g=0g=0, we may simply write πA​(Z)\pi^{A}(Z).
It is intuitive that in this case, there is no need to hedge after the exercise time.

###### Lemma 4.1.

Let Z∈Cb​(Λ)Z\in C\_{b}(\Lambda) and suppose g=0g=0. Then πEA​(Z)=π~EA​(Z)\pi^{A}\_{E}(Z)=\tilde{\pi}^{A}\_{E}(Z), where

|  |  |  |
| --- | --- | --- |
|  | π~EA(Z):=inf{x:∃q∈Cb(Λ;ℝd)s.t.x+∫0uqtdXt≥Zu,∀u∈[0,1],𝒬E(dω)-q.s.,}.\tilde{\pi}^{A}\_{E}(Z):=\operatorname\*{\vphantom{p}inf}\bigg\{x:\exists q\in C\_{b}(\Lambda;\mathbb{R}^{d})\ \text{s.t.}\ x+\int\_{0}^{u}q\_{t}dX\_{t}\geq Z\_{u},\ \forall\,u\in[0,1],\ \mathcal{Q}^{E}(d\omega)\text{-\text{q.s.}},\bigg\}. |  |

###### Proof.

It is clear that π~A​(Z)≥πA​(Z)\tilde{\pi}^{A}(Z)\geq\pi^{A}(Z). Let (q,q~,h)(q,\tilde{q},h) be a superhedging strategy for πA​(Z)\pi^{A}(Z) starting from xx. We claim that (x,q)(x,q) is then a superhedging strategy for π~A​(Z)\tilde{\pi}^{A}(Z) which gives the reverse inequality.
Fix u∈[0,1]u\in[0,1] and ℙ∈𝒬E\mathbb{P}\in\mathcal{Q}^{E}. Let Mtu=∫utq~tu​𝑑XtM^{u}\_{t}=\int\_{u}^{t}\tilde{q}^{u}\_{t}dX\_{t}, t∈[u,1]t\in[u,1], which is a ℙ\mathbb{P}–martingale with Muu=0M^{u}\_{u}=0. The superhedging property means that

|  |  |  |
| --- | --- | --- |
|  | x+∫0uqt​𝑑Xt+M1u≥Zu,ℙ−a.s.x+\int\_{0}^{u}q\_{t}dX\_{t}+M^{u}\_{1}\geq Z\_{u},\quad\mathbb{P}-\text{a.s.} |  |

and taking ℱu\mathcal{F}\_{u}-conditional expectations, we obtain x+∫0uqt​𝑑Xt≥Zux+\int\_{0}^{u}q\_{t}dX\_{t}\geq Z\_{u} ℙ\mathbb{P}-a.s. Since both LHS and RHS are right-continuous processes, we see that the inequality holds for all u∈[0,1]u\in[0,1], ℙ\mathbb{P}-a.s. and hence also 𝒬E\mathcal{Q}^{E}-q.s. since ℙ\mathbb{P} was an arbitrary element of 𝒬E\mathcal{Q}^{E}.
∎

From the above proof it follows that for any u∈[0,1]u\in[0,1] and any ℙ∈𝒬E\mathbb{P}\in\mathcal{Q}^{E}, MuM^{u} is a martingale starting in zero and with M1u≥0M^{u}\_{1}\geq 0 ℙ\mathbb{P}-a.s., and hence in fact M1u=0M^{u}\_{1}=0 𝒬E\mathcal{Q}^{E}-q.s., so that we not only can, but must, have q~≡0\tilde{q}\equiv 0 𝒬E\mathcal{Q}^{E}-q.s.

We now come back to the richer case when g≠0g\neq 0 and observe that the so-called weak pricing-hedging duality holds in general.

###### Proposition 4.2.

Let Z∈Cb​(Λ)Z\in C\_{b}(\Lambda), g∈Cb​(Ω;ℝm)g\in C\_{b}(\Omega;\mathbb{R}^{m}) and suppose 𝒬gE≠∅\mathcal{Q}^{E}\_{g}\neq\emptyset. Then

|  |  |  |
| --- | --- | --- |
|  | πg,EA​(Z)≥supℙ∈𝒬gE,τ∈𝒯ℙ𝔼ℙ​Zτ.\pi^{A}\_{g,E}(Z)\geq\sup\_{\mathbb{P}\in\mathcal{Q}^{E}\_{g},\tau\in\mathcal{T}^{\mathbb{P}}}\mathbb{E}^{\mathbb{P}}Z\_{\tau}. |  |

###### Proof.

Take any ℙ∈𝒬gE\mathbb{P}\in\mathcal{Q}^{E}\_{g}, τ∈𝒯ℙ\tau\in\mathcal{T}^{\mathbb{P}} and any πgA​(Z)\pi^{A}\_{g}(Z) superhedging strategy (x,q,q~,h)(x,q,\tilde{q},h). For t∈[0,1]t\in[0,1], note that ω→q~τ​(ω)​(t,ωt∧⁣⋅)​𝟙t>τ​(ω)\omega\to\tilde{q}^{\tau(\omega)}(t,\omega\_{t\land\cdot})\mathds{1}\_{t>\tau(\omega)} is a composition of ω→(t,t∧τ​(ω),ωt∧⁣⋅)\omega\to(t,t\land\tau(\omega),\omega\_{t\land\cdot}), which is ℱtℙ\mathcal{F}\_{t}^{\mathbb{P}}-measurable with (t,u,ωt∧⁣⋅)→q~u​(t,ωt∧⁣⋅)​𝟙t>u(t,u,\omega\_{t\land\cdot})\to\tilde{q}^{u}(t,\omega\_{t\land\cdot})\mathds{1}\_{t>u} which is measurable. It follows that t→q~τ​(t,ωt∧⁣⋅)​𝟙t>τt\to\tilde{q}^{\tau}(t,\omega\_{t\land\cdot})\mathds{1}\_{t>\tau} is adapted and left-continuous (with right limits), so progressive and

|  |  |  |
| --- | --- | --- |
|  | ∫τ1q~τ​𝑑Xt=∫01q~τ​(ω)​(t,ωt∧⁣⋅)​𝟙t>τ​𝑑Xt\int\_{\tau}^{1}\tilde{q}^{\tau}dX\_{t}=\int\_{0}^{1}\tilde{q}^{\tau(\omega)}(t,\omega\_{t\land\cdot})\mathds{1}\_{t>\tau}dX\_{t} |  |

is well defined ℙ\mathbb{P}-a.s., and it coincides ℙ\mathbb{P}-a.s. with the pathwise version in ([3](https://arxiv.org/html/2510.05463v1#S4.E3 "In 4.1 Pathwise stochastic integration ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time")). Naturally, the pathwise stochastic integral of q~τ​𝟙t>τ\tilde{q}^{\tau}\mathds{1}\_{t>\tau} and of q~u​𝟙t>u\tilde{q}^{u}\mathds{1}\_{t>u} coincide for ω∈Ω\omega\in\Omega such that τ​(ω)=u\tau(\omega)=u. By the superhedging property we thus have

|  |  |  |
| --- | --- | --- |
|  | x+∫01q​𝟙t≤τ​𝑑Xt+∫01q~τ​𝟙t>τ​𝑑Xt+h​g≥Zτx+\int\_{0}^{1}q\mathds{1}\_{t\leq\tau}dX\_{t}+\int\_{0}^{1}\tilde{q}^{\tau}\mathds{1}\_{t>\tau}dX\_{t}+hg\geq Z\_{\tau} |  |

𝒬gE\mathcal{Q}\_{g}^{E}-q.s. and in particular ℙ\mathbb{P}-a.s., and hence the same equality holds ℙ\mathbb{P}-a.s., with the stochastic integral replacing the pathwise integral. The desired inequality is obtained taking expectations under ℙ\mathbb{P} on both sides, noting that the expectation of the stochastic integral is zero since q~\tilde{q} is bounded and ℙ∈𝒬gE\mathbb{P}\in\mathcal{Q}^{E}\_{g}, so XX is a square integrable martingale under ℙ\mathbb{P}.
∎

### 4.3 Duality gap and a dynamic extension for statically traded European options

As discussed in the introduction, the pricing-hedging duality may then fail for an American option, i.e., the inequality in Proposition [4.2](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.2 Robust superhedging of American Options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time") may be strict. This was originally observed by Neuberger ([2007](https://arxiv.org/html/2510.05463v1#bib.bib47)); Hobson and Neuberger ([2017](https://arxiv.org/html/2510.05463v1#bib.bib35)), in a discrete time setting, and explored in a series of subsequent works. In particular, Aksamit et al. ([2019](https://arxiv.org/html/2510.05463v1#bib.bib1)) linked this to the failure of the dynamic programming principle and shown that if the option exercise times are allowed to depend on richer information, namely on dynamic prices of gg, then pricing-hedging duality is recovered. We establish now the analogous set of results in a continuous time setting. We start with an example where a duality gap arises.

###### Example 4.3.

Consider d=1d=1 and ℙ0∈𝒬\mathbb{P}\_{0}\in\mathcal{Q} be such that Xt≡1X\_{t}\equiv 1, t∈[0,1]t\in[0,1], i.e., ℙ0\mathbb{P}\_{0} is a constant stock price model. Consider also ℙ1\mathbb{P}\_{1} under which Xt≡1X\_{t}\equiv 1, for t∈[0,1/2]t\in[0,1/2] and then follows the SDE

|  |  |  |
| --- | --- | --- |
|  | d​Xt=β¯​Xt​d​Wt,dX\_{t}=\bar{\beta}X\_{t}dW\_{t}, |  |

until XX reaches 100100 or t=1t=1, whichever comes first, and where β¯>0\bar{\beta}>0 is given and WtW\_{t} is a Brownian motion (possibly from a larger space).
In other words, the stock price is constant for half of the time and then behaves as a scaled geometric Brownian motion which stops if it hits the level 100100.

Let the set 𝒬E\mathcal{Q}^{E} be the convex hull of ℙ0,ℙ1\mathbb{P}\_{0},\mathbb{P}\_{1}, so

|  |  |  |
| --- | --- | --- |
|  | E1={X[0,1/2]=1},E2={β[1/2,1]=0}∪{βt=β¯2​ωt2​𝟏sups≤tωs<100,t∈[1/2,1]},E\_{1}=\{X\_{[0,1/2]}=1\},\quad E\_{2}=\{\beta\_{[1/2,1]}=0\}\cup\{\beta\_{t}=\bar{\beta}^{2}\omega\_{t}^{2}\mathbf{1}\_{\sup\_{s\leq t}\omega\_{s}<100},t\in[1/2,1]\}, |  |

where β\beta is the diffusion characteristic of XX.
In particular, ℙ~∈𝒬E\tilde{\mathbb{P}}\in\mathcal{Q}^{E}, where ℙ~=12​ℙ0+12​ℙ1\tilde{\mathbb{P}}=\frac{1}{2}\mathbb{P}\_{0}+\frac{1}{2}\mathbb{P}\_{1}. Finally, we let g=(X1−1)+−pg=(X\_{1}-1)^{+}-p, where pp is such that 𝔼ℙ~​[(X1−1)+]=p=12​𝔼ℙ1​[(X1−1)+]\mathbb{E}^{\tilde{\mathbb{P}}}[(X\_{1}-1)^{+}]=p=\frac{1}{2}\mathbb{E}^{\mathbb{P}\_{1}}[(X\_{1}-1)^{+}], so that ℙ~∈𝒬gE\tilde{\mathbb{P}}\in\mathcal{Q}^{E}\_{g}.

We now define the American option payoff via Zt=3​p/2−6​p​|t−1/4|+(Xt−1)+∧100Z\_{t}=3p/2-6p|t-1/4|+(X\_{t}-1)^{+}\land 100 for t∈[0,1/2]t\in[0,1/2] and Zt=(Xt−1)+∧100Z\_{t}=(X\_{t}-1)^{+}\land 100 for t∈(1/2,1]t\in(1/2,1]. Clearly, by definition, Z∈Cb​(Λ)Z\in C\_{b}(\Lambda). Note also that for any ℙ∈𝒬E\mathbb{P}\in\mathcal{Q}^{E}, we have X1≤100X\_{1}\leq 100 ℙ\mathbb{P}-a.s., so that Z1=(X1−1)+Z\_{1}=(X\_{1}-1)^{+} 𝒬E\mathcal{Q}^{E}-q.s., and Z1/4=3​p/2Z\_{1/4}=3p/2, 𝒬E\mathcal{Q}^{E}-q.s. In fact, for any ℙ∈𝒬E\mathbb{P}\in\mathcal{Q}^{E}, ZtZ\_{t} is a deterministic process on [0,1/2][0,1/2] which attains its maximum at time t=1/4t=1/4. In addition, for t∈[1/2,1]t\in[1/2,1], Zt=f​(Xt)Z\_{t}=f(X\_{t}), for a convex function f​(w)=(w−1)+f(w)=(w-1)^{+} and since ℙ\mathbb{P} is a martingale measure, ZtZ\_{t} is a submartingale on [1/2,1][1/2,1] and, in particular, 𝔼ℙ​[Zτ]≤𝔼ℙ​[Z1]\mathbb{E}^{\mathbb{P}}[Z\_{\tau}]\leq\mathbb{E}^{\mathbb{P}}[Z\_{1}], for any stopping time τ\tau taking values in [1/2,1][1/2,1]. It follows that the American option will only ever be optimally exercised at times t=1/4t=1/4 or t=1t=1. In particular, Z1/4>ZtZ\_{1/4}>Z\_{t} for all t≠1/4t\neq 1/4 ℙ0\mathbb{P}\_{0}-a.s., and under this measure the optimal exercise time is τ0=1/4\tau\_{0}=1/4. In contrast, under ℙ1\mathbb{P}\_{1}, we have 𝔼ℙ1​[Z1∣ℱ1/4]=2​p>Z1/4\mathbb{E}^{\mathbb{P}\_{1}}[Z\_{1}\mid\mathcal{F}\_{1/4}]=2p>Z\_{1/4} and the optimal exercise policy is τ1≡1\tau\_{1}\equiv 1. However, under any ℙ∈𝒬gE\mathbb{P}\in\mathcal{Q}^{E}\_{g} we have 𝔼ℙ​[Z1∣ℱ1/4ℙ]=𝔼ℙ​[Z1]=p<Z1/4\mathbb{E}^{\mathbb{P}}[Z\_{1}\mid\mathcal{F}\_{1/4}^{\mathbb{P}}]=\mathbb{E}^{\mathbb{P}}[Z\_{1}]=p<Z\_{1/4} and hence τ0\tau\_{0} is the optimal exercise policy:

|  |  |  |
| --- | --- | --- |
|  | supℙ∈𝒬gEsupτ∈𝒯ℙ𝔼ℙ​Zτ=3​p/2.\sup\_{\mathbb{P}\in\mathcal{Q}^{E}\_{g}}\sup\_{\tau\in\mathcal{T}^{\mathbb{P}}}\mathbb{E}^{\mathbb{P}}Z\_{\tau}=3p/2. |  |

We will now show that this value is strictly smaller than the superhedging price. In fact, we will show that the above supremum can be strictly increased by allowing a richer family of stopping times. Specifically, consider a two-dimensional standard Brownian motion (B,W)(B,W) on some probability space (S,𝒮,μ)(S,\mathcal{S},\mu).
Let βt=0\beta\_{t}=0 for t∈[0,1/2]t\in[0,1/2] and

|  |  |  |
| --- | --- | --- |
|  | βt={0if ​B1/4<0,β¯2​Xt2​𝟏sups≤tXs<100if ​B1/4≥0,​ for ​t∈(1/2,1],\beta\_{t}=\begin{cases}0&\text{if }B\_{1/4}<0,\\ \bar{\beta}^{2}X\_{t}^{2}\mathbf{1}\_{\sup\_{s\leq t}X\_{s}<100}&\text{if }B\_{1/4}\geq 0,\end{cases}\text{ for }t\in(1/2,1], |  |

where X0=1X\_{0}=1 and d​Xt=βt​d​WtdX\_{t}=\sqrt{\beta\_{t}}dW\_{t}. Observe that the distribution of XX under μ\mu is given by ℙ~\tilde{\mathbb{P}},
ℙ~=μ∘X−1\tilde{\mathbb{P}}=\mu\circ X^{-1}. Consider now Yt=𝔼μ​[g∣𝒢t]Y\_{t}=\mathbb{E}^{\mu}[g\mid\mathcal{G}\_{t}], where 𝒢t=σ(Bs,Ws:s≤t)μ\mathcal{G}\_{t}=\sigma(B\_{s},W\_{s}:s\leq t)^{\mu}. Note that YY is a continuous martingale and that Y0=0Y\_{0}=0 while Y1/4=−p​𝟏B1/4<0+p​𝟏B1/4≥0Y\_{1/4}=-p\mathbf{1}\_{B\_{1/4}<0}+p\mathbf{1}\_{B\_{1/4}\geq 0}. Let ℙ^:=μ∘(X,Y)−1\hat{\mathbb{P}}:=\mu\circ(X,Y)^{-1} which is a martingale measure on the canonical space with d=2d=2. Note that τ∗=14​𝟏Y1/4<0+𝟏Y1/4>0\tau\_{\*}=\frac{1}{4}\mathbf{1}\_{Y\_{1/4}<0}+\mathbf{1}\_{Y\_{1/4}>0} is a stopping time in its natural filtration and we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ^​[Zτ∗]=12​3​p/2+12​2​p=7​p/4>3​p/2.\mathbb{E}^{\hat{\mathbb{P}}}[Z\_{\tau\_{\*}}]=\frac{1}{2}3p/2+\frac{1}{2}2p=7p/4>3p/2. |  |

It will follow directly from Proposition [4.5](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3 Duality gap and a dynamic extension for statically traded European options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time") below that this provides a lower bound on πg,EA​(Z)\pi^{A}\_{g,E}(Z) and hence there is a strict inequality in the weak duality in Proposition [4.2](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.2 Robust superhedging of American Options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time").

To address the issue identified in the above example, in analogy to the discrete time results in Aksamit et al. ([2019](https://arxiv.org/html/2510.05463v1#bib.bib1)), we consider dynamic *lifts* in which options gg are traded for all time t∈[0,1]t\in[0,1]. This is a technical device, a fictitious lift as first pioneered by Cvitanic and Karatzas ([1993](https://arxiv.org/html/2510.05463v1#bib.bib17)) in the context of trading constraints, which is needed to establish a suitable pricing-hedging duality. The intuition is that these option prices can provide an additional signal which allows to build optimal exercise policies. However, an additional technical difficulty arises in continuous time in relation to how and when additional information is revealed. In Example [4.3](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem3 "Example 4.3. ‣ 4.3 Duality gap and a dynamic extension for statically traded European options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time") above we used an additional Brownian motion to, essentially, generate a flip of a coin at time t=1/2t=1/2. This allowed us to ensure the option prices YY were continuous and Y0=0Y\_{0}=0 was a constant. However, this is not always the case. For a trivial counterexample, suppose ℙ\mathbb{P} is a convex combination of two Black-Scholes models with volatilities σ1<σ2\sigma\_{1}<\sigma\_{2}. This can be realised by flipping an independent coin at time t=0t=0 and deciding which model is used. In such a setup, option price Y0Y\_{0} defined via conditional expectations (and taken right-continuous) would be random at time t=0t=0 (taking two values). Naturally, if ℙ\mathbb{P} is calibrated then we have 𝔼ℙ​[Y0]=0\mathbb{E}^{\mathbb{P}}[Y\_{0}]=0 and we simply have to mandate that trading in options happens at time “t=0−t=0-”, i.e., before the information is revealed, we refer to Aksamit et al. ([2020](https://arxiv.org/html/2510.05463v1#bib.bib2)) for a detailed discussion. We implement this by working on a time horizon [−δ,1][-\delta,1] with all processes required to be constant on [−δ,0)[-\delta,0), where δ∈(0,1)\delta\in(0,1) is small.

We thus introduce the enlarged space Ω^=D​([−δ,1];ℝd+m)\widehat{\Omega}=D([-\delta,1];\mathbb{R}^{d+m}) with the canonical process X^=(X,Y)\widehat{X}=(X,Y) and their natural filtration 𝔽^\widehat{\mathbb{F}}. We write 𝔽X\mathbb{F}^{X} for the filtration on Ω^\widehat{\Omega} generated by XX. For any probability measure ℙ^\widehat{\mathbb{P}} on Ω^\widehat{\Omega}, let 𝔽^ℙ^\widehat{\mathbb{F}}^{\widehat{\mathbb{P}}} be the augmented filtration.
Also let 𝒯^\widehat{\mathcal{T}} (resp. 𝒯^ℙ^\widehat{\mathcal{T}}^{\widehat{\mathbb{P}}}) be the set of 𝔽^\widehat{\mathbb{F}}-stopping times (resp. 𝔽^ℙ^\widehat{\mathbb{F}}^{\widehat{\mathbb{P}}}-stopping times). The space of stopped paths on Ω^\widehat{\Omega} is denoted Λ^\widehat{\Lambda}. Spaces Ω^¯\bar{\widehat{\Omega}} and Λ^¯\bar{\widehat{\Lambda}} are defined as previously, with Ω^\widehat{\Omega} (resp. Λ^\widehat{\Lambda}) replacing Ω\Omega (resp. Λ\Lambda). All these spaces are now defined for time index t∈[−δ,1]t\in[-\delta,1].

We note that all of the results in section [3](https://arxiv.org/html/2510.05463v1#S3 "3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") can be applied in the context of martingale measures on Ω^\widehat{\Omega}. Further, we will now make use of the additional pathwise restrictions introduced there to lift calibrated martingale measures on Ω\Omega to restricted martingale measures on Ω^\widehat{\Omega}. Given E1∈ℬ​(Ω)E\_{1}\in\mathcal{B}(\Omega) and E2∈ℬ​(Λ)E\_{2}\in\mathcal{B}(\Lambda) we let

|  |  |  |  |
| --- | --- | --- | --- |
|  | E^1\displaystyle\widehat{E}\_{1} | :={ω^∈Ω^:ω|[0,1]∈E1,Xt​(ω^)=X0​(ω^),Yt​(ω^)=0,t∈[−δ,0),Y1​(ω^)=g​(X​(ω^))}∈ℬ​(Ω^),\displaystyle:=\left\{\widehat{\omega}\in\widehat{\Omega}:\omega\_{|[0,1]}\in E\_{1},\ X\_{t}(\widehat{\omega})=X\_{0}(\widehat{\omega}),Y\_{t}(\widehat{\omega})=0,t\in[-\delta,0),\ Y\_{1}(\widehat{\omega})=g(X(\widehat{\omega}))\right\}\in\mathcal{B}(\widehat{\Omega}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | E^2\displaystyle\widehat{E}\_{2} | :={(t,X⋅∧t,Y⋅∧t)∈Λ^:(t,X⋅∧t)t∈[0,1]∈E2}∈ℬ​(Λ^).\displaystyle:=\left\{(t,X\_{\cdot\land t},Y\_{\cdot\land t})\in\widehat{\Lambda}:(t,X\_{\cdot\land t})\_{t\in[0,1]}\in E\_{2}\right\}\in\mathcal{B}(\widehat{\Lambda}). |  |

Note that Xt​(ω^)=X0​(ω^),Yt​(ω^)=0,t∈[−δ,0)X\_{t}(\widehat{\omega})=X\_{0}(\widehat{\omega}),Y\_{t}(\widehat{\omega})=0,t\in[-\delta,0) is a measurable constraint as it is enough to ensure this for rational tt thanks to right-continuity of paths. We write 𝒬^E^={ℙ^∈𝒬^:ℙ^​(E^1)=λ⊗ℙ^​(E^2)=1}\widehat{\mathcal{Q}}^{\widehat{E}}=\{\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}}:\widehat{\mathbb{P}}(\widehat{E}\_{1})=\lambda\otimes\widehat{\mathbb{P}}(\widehat{E}\_{2})=1\}. With this notation, we show that every model in 𝒬gE\mathcal{Q}^{E}\_{g} can be lifted to a model in 𝒬^E^\widehat{\mathcal{Q}}^{\widehat{E}}.

###### Lemma 4.4.

For any ℙ^∈𝒬^E^\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}}^{\widehat{E}}, ℙ^∘((Xt)t∈[0,1])−1∈𝒬gE\widehat{\mathbb{P}}\circ\left((X\_{t})\_{t\in[0,1]}\right)^{-1}\in\mathcal{Q}^{E}\_{g}. Conversely, for any ℙ∈𝒬gE\mathbb{P}\in\mathcal{Q}^{E}\_{g}, there exists a ℙ^∈𝒬^E^\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}}^{\widehat{E}} such that the ℙ^∘((Xt)t∈[0,1])−1=ℙ\widehat{\mathbb{P}}\circ\left((X\_{t})\_{t\in[0,1]}\right)^{-1}=\mathbb{P}.

###### Proof.

Let ℙ^∈𝒬^E^\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}}^{\widehat{E}} and define ℙ:=ℙ^∘((Xt)t∈[0,1])−1\mathbb{P}:=\widehat{\mathbb{P}}\circ\left((X\_{t})\_{t\in[0,1]}\right)^{-1}. Since a martingale remains a martingale in its natural filtration, we have ℙ∈𝒬\mathbb{P}\in\mathcal{Q}. In addition, by definition of sets E^1\widehat{E}\_{1}, E^2\widehat{E}\_{2}, ℙ∈𝒬E\mathbb{P}\in\mathcal{Q}^{E}. Finally, since YY is a ℙ^\widehat{\mathbb{P}}-martingale with Y−δ=0Y\_{-\delta}=0, we have 𝔼ℙ​[g​(X​(ω))]=𝔼ℙ^​[g​(X​(ω^))]=𝔼ℙ^​[Y1​(ω^)]=0\mathbb{E}^{\mathbb{P}}[g(X(\omega))]=\mathbb{E}^{\widehat{\mathbb{P}}}[g(X(\widehat{\omega}))]=\mathbb{E}^{\widehat{\mathbb{P}}}[Y\_{1}(\widehat{\omega})]=0 which establishes ℙ∈𝒬gE\mathbb{P}\in\mathcal{Q}^{E}\_{g}, as required.
To show the converse, fix ℙ∈𝒬gE\mathbb{P}\in\mathcal{Q}^{E}\_{g}. Define gt0:=𝔼ℙ​[g∣ℱtℙ]g^{0}\_{t}:=\mathbb{E}^{\mathbb{P}}[g\mid\mathcal{F}^{\mathbb{P}}\_{t}] and let (gt)t∈[0,1](g\_{t})\_{t\in[0,1]} be the rcll martingale modification of (gt0)t∈[0,1](g^{0}\_{t})\_{t\in[0,1]}. Note that g1=g​(X)g\_{1}=g(X) ℙ\mathbb{P}-a.s. and 𝔼ℙ​[g0]=0\mathbb{E}^{\mathbb{P}}[g\_{0}]=0. Extend processes X⋅X\_{\cdot} and g⋅g\_{\cdot} to [−δ,1][-\delta,1] via Xt≡X0X\_{t}\equiv X\_{0} and gt=0g\_{t}=0 for t∈[−δ,0)t\in[-\delta,0), noting they remain martingales on [−δ,1][-\delta,1]. We now define ℙ^:=ℙ∘(X⋅,g⋅)−1\widehat{\mathbb{P}}:=\mathbb{P}\circ(X\_{\cdot},g\_{\cdot})^{-1}. The martingale property gives us P^∈𝒬^\widehat{P}\in\widehat{\mathcal{Q}}, by definition ℙ^​(E^1)=λ⊗ℙ^​(E^2)=1\widehat{\mathbb{P}}(\widehat{E}\_{1})=\lambda\otimes\widehat{\mathbb{P}}(\widehat{E}\_{2})=1 and ℙ^∘((Xt)t∈[0,1])−1=ℙ\widehat{\mathbb{P}}\circ\left((X\_{t})\_{t\in[0,1]}\right)^{-1}=\mathbb{P}, so that ℙ^∈𝒬^E^\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}}^{\widehat{E}}, as required.
∎

Next, let us extend the notion of superhedging price to the extended model. This requires us to lift the American option payoff ZZ to Ω^\widehat{\Omega}. On [0,1][0,1] this is done via the obvious lift, Z^​((t,ω^⋅∧t)):=Z​((t,X​(ω^)|[0,t]))\widehat{Z}((t,\widehat{\omega}\_{\cdot\land t})):=Z((t,X(\widehat{\omega})\_{|[0,t]})), but we also need to define the American payoff on [−δ,0)[-\delta,0) and we do it in such a way that if X^\widehat{X} is constant on [−δ,0)[-\delta,0) ℙ\mathbb{P}-a.s., then so is the American option payoff: Z^​(t,ω^⋅∧t):=Z​((0,X​(ω^)t)),t∈[−δ,0)\widehat{Z}(t,\widehat{\omega}\_{\cdot\land t}):=Z((0,X(\widehat{\omega})\_{t})),t\in[-\delta,0). The superhedging price for Z^\widehat{Z} is defined in analogy to πg,EA​(Z)\pi^{A}\_{g,E}(Z).

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^E^A(Z^):=inf{\displaystyle\widehat{\pi}^{A}\_{\widehat{E}}(\widehat{Z}):=\operatorname\*{\vphantom{p}inf}\bigg\{ | x:∃(q,q~)∈Cb​(Λ^;ℝd+m)×Cb​(Λ^¯≥;ℝd+m),s.t.​x+∫−δuq​(t,ω^t∧⁣⋅)​𝑑X^t​(ω)\displaystyle x:\exists(q,\tilde{q})\in C\_{b}(\widehat{\Lambda};\mathbb{R}^{d+m})\times C\_{b}(\bar{\widehat{\Lambda}}\_{\geq};\mathbb{R}^{d+m}),\ \text{s.t.}\ x+\int\_{-\delta}^{u}q(t,\widehat{\omega}\_{t\land\cdot})d\widehat{X}\_{t}(\omega) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫u1q~u(t,ω^t∧⁣⋅)dX^t(ω)≥Z^(u,ω^⋅∧u),∀u∈[−δ,1],𝒬^E^(dω^)-q.s.,}\displaystyle\quad+\int\_{u}^{1}\tilde{q}^{u}(t,\widehat{\omega}\_{t\land\cdot})d\widehat{X}\_{t}(\omega)\geq\widehat{Z}(u,\widehat{\omega}\_{\cdot\wedge u}),\ \forall\,u\in[-\delta,1],\ \widehat{\mathcal{Q}}^{\widehat{E}}(d\widehat{\omega})\text{-\text{q.s.}},\bigg\} |  |

###### Proposition 4.5.

For E1∈ℬ​(Ω)E\_{1}\in\mathcal{B}(\Omega), E2∈ℬ​(Λ)E\_{2}\in\mathcal{B}(\Lambda), Z∈Cb​(Λ)Z\in C\_{b}(\Lambda), g∈Cb​(Ω;ℝm)g\in C\_{b}(\Omega;\mathbb{R}^{m}) such that 𝒬gE≠∅\mathcal{Q}^{E}\_{g}\neq\emptyset, we have the following chain of inequalities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πg,EA​(Z)≥π^E^A​(Z^)≥supℙ^∈𝒬^E,τ^∈𝒯^ℙ^𝔼ℙ^​Z^τ^=supℙ^¯∈𝒬^¯E𝔼ℙ^¯​Z^​(θ,ω^⋅∧θ)≥supℙ¯∈𝒬¯gE𝔼ℙ¯​Z¯.\displaystyle\pi^{A}\_{g,E}(Z)\geq\widehat{\pi}^{A}\_{\widehat{E}}(\widehat{Z})\geq\sup\_{\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}}^{E},\widehat{\tau}\in\widehat{\mathcal{T}}^{\widehat{\mathbb{P}}}}\mathbb{E}^{\widehat{\mathbb{P}}}\widehat{Z}\_{\widehat{\tau}}=\sup\_{\bar{\widehat{\mathbb{P}}}\in\bar{\widehat{\mathcal{Q}}}^{E}}\mathbb{E}^{\bar{\widehat{\mathbb{P}}}}\widehat{Z}(\theta,\widehat{\omega}\_{\cdot\land\theta})\geq\sup\_{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}\_{g}}\mathbb{E}^{\bar{\mathbb{P}}}\bar{Z}. |  | (4) |

###### Proof.

First, focus on the inequality πg,EA​(Z)≥π^E^A​(Z^)\pi^{A}\_{g,E}(Z)\geq\widehat{\pi}^{A}\_{\widehat{E}}(\widehat{Z}). Consider any superhedging strategy (x,q,q~,h)(x,q,\tilde{q},h) for πg,EA\pi^{A}\_{g,E}. We need to show that we can lift it to a superhedging strategy on Ω^\widehat{\Omega} for Z^\widehat{Z}. We do this by simply buying and holding XX on [−δ,0][-\delta,0], in accordance to the initial position of q​(0,X−δ​(ω^))q(0,X\_{-\delta}(\widehat{\omega})) and then trading in XX according to (q,q~)(q,\tilde{q}) on [0,1][0,1] as functions of (t,X​(ω^)|[0,t])(t,X(\widehat{\omega})\_{|[0,t]}).
If the option holder exercises on [δ,0)[\delta,0) then we do not change the strategy and respond with q~0\tilde{q}^{0} from time t=0t=0 onwards.
We do no dynamic trading in YY but only buy and hold hh of YY on [−δ,1][-\delta,1].
The superhedging property is easily obtained with a contradiction argument, noting that for any ℙ^∈𝒬^E^\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}}^{\widehat{E}}, XX and ZZ are constant on [−δ,0][-\delta,0] and Y−δ=0Y\_{-\delta}=0, ℙ^\widehat{\mathbb{P}}-a.s., and using the first part of Lemma [4.4](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.3 Duality gap and a dynamic extension for statically traded European options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time").

Next, π^EA​(Z^)≥supℙ^∈𝒬^E,τ^∈𝒯^ℙ^𝔼ℙ^​Z^τ^\widehat{\pi}^{A}\_{E}(\widehat{Z})\geq\sup\_{\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}}^{E},\widehat{\tau}\in\widehat{\mathcal{T}}^{\widehat{\mathbb{P}}}}\mathbb{E}^{\widehat{\mathbb{P}}}\widehat{Z}\_{\widehat{\tau}} is the weak duality analogous to Proposition [4.2](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.2 Robust superhedging of American Options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time"), but applied to the extended model. It is immediate to check that the proof extends to this setting. Note that 𝒬gE\mathcal{Q}^{E}\_{g} is non-empty and hence, by Lemma [4.4](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.3 Duality gap and a dynamic extension for statically traded European options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time"), so is 𝒬^E\widehat{\mathcal{Q}}^{E}. Analogously, the equality supℙ^∈𝒬^E,τ^∈𝒯^ℙ^𝔼ℙ^​Z^τ^=supℙ^¯∈𝒬^¯E𝔼ℙ^¯​Z^​(θ,ω^⋅∧θ)\sup\_{\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}}^{E},\widehat{\tau}\in\widehat{\mathcal{T}}^{\widehat{\mathbb{P}}}}\mathbb{E}^{\widehat{\mathbb{P}}}\widehat{Z}\_{\widehat{\tau}}=\sup\_{\bar{\widehat{\mathbb{P}}}\in\bar{\widehat{\mathcal{Q}}}^{E}}\mathbb{E}^{\bar{\widehat{\mathbb{P}}}}\widehat{Z}(\theta,\widehat{\omega}\_{\cdot\land\theta}) follows from Theorem [3.1](https://arxiv.org/html/2510.05463v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time"), also applied to the extended model.

Finally, recall that Lemma [4.4](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.3 Duality gap and a dynamic extension for statically traded European options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time") states that every measure in 𝒬gE\mathcal{Q}^{E}\_{g} can be lifted to a measure in 𝒬^E\widehat{\mathcal{Q}}^{E}. Similarly, and with obvious definitions, the same arguments show that every measure in 𝒬¯gE\bar{\mathcal{Q}}^{E}\_{g} can be lifted to a measure in 𝒬^¯E\bar{\widehat{\mathcal{Q}}}^{E}. Since Z^\widehat{Z} only depends on (t,ω⋅∧t)(t,\omega\_{\cdot\wedge t}), the last inequality follows:
supℙ^¯∈𝒬^¯E𝔼ℙ^¯​Z^​(θ,ω^⋅∧θ)≥supℙ¯∈𝒬¯gE𝔼ℙ¯​Z​(θ,ω⋅∧θ)\sup\_{\bar{\widehat{\mathbb{P}}}\in\bar{\widehat{\mathcal{Q}}}^{E}}\mathbb{E}^{\bar{\widehat{\mathbb{P}}}}\widehat{Z}(\theta,\widehat{\omega}\_{\cdot\land\theta})\geq\sup\_{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}\_{g}}\mathbb{E}^{\bar{\mathbb{P}}}Z(\theta,\omega\_{\cdot\land\theta}).
∎

###### Remark 4.6.

We note that the assumptions we made on ZZ and gg were stronger than required for the results in this section. We made no use of continuity of gg and we used that it is bounded to conclude that its conditional expectations defined a square integrable martingale. In fact, all results in section [4](https://arxiv.org/html/2510.05463v1#S4 "4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time") extend instantly to g∈L0​(Ω)g\in L^{0}(\Omega) with 𝒬gE\mathcal{Q}^{E}\_{g} redefined as

|  |  |  |
| --- | --- | --- |
|  | {ℙ∈𝒬E:𝔼ℙ​(g2)<∞​ and ​𝔼ℙ​(g)=0}\left\{\mathbb{P}\in\mathcal{Q}^{E}:\mathbb{E}^{\mathbb{P}}(g^{2})<\infty\text{ and }\mathbb{E}^{\mathbb{P}}(g)=0\right\} |  |

and assumed non-empty. Similarly, we did not use that Z∈Cb​(Λ)Z\in C\_{b}(\Lambda) and it would have been enough to assume that Z∈L0​(Λ)Z\in L^{0}(\Lambda), bounded from below and such that t→Z​(t,ω⋅∧t)t\to Z(t,\omega\_{\cdot\land t}) is rcll 𝒬E​(d​ω)\mathcal{Q}^{E}(d\omega)-q.s. We made stronger assumptions in the statements as this, we feel, streamlines the presentation allowing to match the assumptions to those made in the next section, where they are actually needed for the results, and to obtain the robust pricing-hedging duality.

## 5 Robust pricing-hedging duality for American options

The previous sections provided the connection between the robust prices of American options and the robust prices of European options in the enlarged space. In order to obtain duality for American options, we must first establish the robust pricing-hedging duality for European options in the enlarged space.

To this end, we restrict our probability space to continuous paths, i.e., Ω=C​([0,1],ℝd)\Omega=C([0,1],\mathbb{R}^{d}). All associated objects, such as 𝔽,𝒬,Ω¯,𝔽¯,𝒬¯\mathbb{F},\mathcal{Q},\bar{\Omega},\bar{\mathbb{F}},\bar{\mathcal{Q}} and so on, are defined in the same way as before.
In terms of the family of candidate models, we require some restrictions on the quadratic variation of the underlying asset.
Similarly to Soner et al. ([2013](https://arxiv.org/html/2510.05463v1#bib.bib56)), define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨X⟩t:=Xt​Xt⊺−2​∫0tXu​𝑑Xu,andβt:=lim supn→∞⟨X⟩t−⟨X⟩t−2−n2−n,t∈(0,1],\langle X\rangle\_{t}:=X\_{t}X\_{t}^{\intercal}-2\int\_{0}^{t}X\_{u}dX\_{u},\quad\text{and}\quad\beta\_{t}:=\limsup\_{n\to\infty}\frac{\langle X\rangle\_{t}-\langle X\rangle\_{t-2^{-n}}}{2^{-n}},\quad t\in(0,1], |  | (5) |

with ⟨X⟩0=β0=0\langle X\rangle\_{0}=\beta\_{0}=0. We let ΩQ​V,t⊂Ωt\Omega\_{QV,t}\subset\Omega\_{t} be the set of paths on which (X⋅X)s∈[0,t](X\bm{\cdot}X)\_{s\in[0,t]} in ([3](https://arxiv.org/html/2510.05463v1#S4.E3 "In 4.1 Pathwise stochastic integration ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time")) is the uniform limit of its approximations.
By the above, ΩQ​V,t∈ℱt\Omega\_{QV,t}\in\mathcal{F}\_{t}. Note that the set of absolutely continuous functions is a Borel subset of all continuous functions and hence the further subset ΩQ​V,tA​C⊂ΩQ​V,t\Omega\_{QV,t}^{AC}\subset\Omega\_{QV,t} of paths on which ⟨X⟩s∈[0,t]\langle X\rangle\_{s\in[0,t]} is an absolutely continuous function is measurable, ΩQ​V,tA​C∈ℱt\Omega\_{QV,t}^{AC}\in\mathcal{F}\_{t}, t∈(0,1]t\in(0,1]. Similarly, βs∈[0,t]\beta\_{s\in[0,t]} is a limsup of measurable functions (defined on (2−n,1](2^{-n},1] and extended by continuity to [0,1][0,1]) and hence is measurable, so that the process β\beta is progressively measurable and we have ⟨X⟩1=∫01βt​𝑑t\langle X\rangle\_{1}=\int\_{0}^{1}\beta\_{t}dt on ΩQ​V,1A​C\Omega\_{QV,1}^{AC}.

If XX is a local martingale under some ℙ∈𝒫\mathbb{P}\in\mathcal{P} then, by (Karandikar, [1995](https://arxiv.org/html/2510.05463v1#bib.bib38), Thm. 2), we see that ⟨X⟩\langle X\rangle is its quadratic variation (such a process being normally only defined ℙ\mathbb{P}-a.s.) and that for any q∈Cb​(Λ)q\in C\_{b}(\Lambda) the pathwise stochastic integral in ([3](https://arxiv.org/html/2510.05463v1#S4.E3 "In 4.1 Pathwise stochastic integration ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time")) coincides with the usual Itô integral ℙ\mathbb{P}-a.s. In addition, since β\beta is progressively measurable and ΩQ​V,1A​C∈ℱ1\Omega\_{QV,1}^{AC}\in\mathcal{F}\_{1}, we can define the set 𝒬\mathcal{Q} of measures ℙ∈𝒫\mathbb{P}\in\mathcal{P} such that XX is a square integrable ℙ\mathbb{P}-martingale and ⟨X⟩⋅\langle X\rangle\_{\cdot} is absolutely continuous with βt∈𝕊+d\beta\_{t}\in\mathbb{S}^{d}\_{+} for all t∈[0,1]t\in[0,1], ℙ\mathbb{P}-a.s. Note that XX is a square integrable ℙ\mathbb{P}-martingale if and only if XX is a ℙ\mathbb{P}-local martingale with 𝔼ℙ​(∫01|βt|​𝑑t)<∞.\mathbb{E}^{\mathbb{P}}\left(\int\_{0}^{1}|\beta\_{t}|\,dt\right)<\infty.

Often it is useful to restrict the diffusion characteristic β\beta of XX to take value in a subset that depends on (t,ω⋅∧t)(t,\omega\_{\cdot\wedge t}). We impose the following market assumptions.

###### Assumption 5.1.

The initial asset prices are given by x0∈ℝdx\_{0}\in\mathbb{R}^{d}. Volatility is restricted by a set-valued process 𝔈:Λ→ℬ​(𝕊+d)\mathfrak{E}:\Lambda\to\mathcal{B}(\mathbb{S}^{d}\_{+}) with 𝔈​(t,ω⋅∧t)⊆𝕊+d\mathfrak{E}(t,\omega\_{\cdot\wedge t})\subseteq\mathbb{S}^{d}\_{+} closed, convex, and globally bounded for (t,ω⋅∧t)∈Λ(t,\omega\_{\cdot\wedge t})\in\Lambda and such that
𝔈\mathfrak{E} is continuous with respect to the topology induced by the Hausdorff metric on compact subsets.
We let g∈Cb​(Ω;ℝm)g\in C\_{b}(\Omega;\mathbb{R}^{m}),

|  |  |  |
| --- | --- | --- |
|  | E1={ω∈Ω:ω0=x0},E2={(t,ωt∧⁣⋅):β​(t,ωt∧⁣⋅)∈𝔈​(t,ωt∧⁣⋅)}E\_{1}=\{\omega\in\Omega:\omega\_{0}=x\_{0}\},\quad E\_{2}=\{(t,\omega\_{t\land\cdot}):\beta(t,\omega\_{t\land\cdot})\in\mathfrak{E}(t,\omega\_{t\land\cdot})\} |  |

and define the pricing measures via ([1](https://arxiv.org/html/2510.05463v1#S3.E1 "In 3 Robust pricing of American options ‣ Robust Pricing and Hedging of American Options in Continuous Time")). We assume that 𝒬gE≠∅\mathcal{Q}^{E}\_{g}\neq\emptyset.

We now present the main robust pricing-hedging duality result for American options. We recall the notation associated to the dynamic lift, as introduced in section [4.3](https://arxiv.org/html/2510.05463v1#S4.SS3 "4.3 Duality gap and a dynamic extension for statically traded European options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time").

###### Theorem 5.2.

Suppose Assumption [5.1](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem1 "Assumption 5.1. ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") holds and Z∈Cb​(Λ)Z\in C\_{b}(\Lambda). Then we have equalities throughout in Proposition [4.5](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3 Duality gap and a dynamic extension for statically traded European options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time") and in particular

|  |  |  |
| --- | --- | --- |
|  | πg,EA​(Z)=supℙ^∈𝒬^E^,τ^∈𝒯^ℙ^𝔼ℙ^​Z^τ^.\pi^{A}\_{g,E}(Z)=\sup\_{\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}}^{\widehat{E}},\widehat{\tau}\in\widehat{\mathcal{T}}^{\widehat{\mathbb{P}}}}\mathbb{E}^{\widehat{\mathbb{P}}}{\widehat{Z}}\_{\widehat{\tau}}. |  |

###### Remark 5.3.

In the case that there are no static European hedging instruments, Theorem [5.2](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem2 "Theorem 5.2. ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") reduces to a robust pricing-hedging duality of the form

|  |  |  |
| --- | --- | --- |
|  | πEA​(Z)=supℙ∈𝒬E,τ∈𝒯ℙ𝔼ℙ​Zτ.\pi^{A}\_{E}(Z)=\sup\_{\mathbb{P}\in\mathcal{Q}^{E},\tau\in\mathcal{T}^{\mathbb{P}}}\mathbb{E}^{\mathbb{P}}Z\_{\tau}. |  |

While our result work for general restrictions 𝔈\mathfrak{E} on volatility, and this includes the special case of 𝔈\mathfrak{E} being a singleton. In particular, we can have 𝒬E={ℙ}\mathcal{Q}^{E}=\{\mathbb{P}\} be a singleton and recover the classical pricing-hedging duality of Myneni ([1992](https://arxiv.org/html/2510.05463v1#bib.bib46)), for the case of a bounded, continuous volatility model.

The proof of this theorem identifies the superhedging price of an American option on Ω\Omega with that of a European option on an enlarged space Ω¯\bar{\Omega} and establishes pricing-hedging duality for the latter. This, in turn, is possible since the restrictions on the diffusion characteristic in Assumption [5.1](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem1 "Assumption 5.1. ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") allow for the application of the semimartingale optimal transport duality from Guo and Loeper ([2021](https://arxiv.org/html/2510.05463v1#bib.bib31)) to establish European option dualities. In particular, if a cost function returns 0 when βt∈𝔈​(t,ωt∧⁣⋅)\beta\_{t}\in\mathfrak{E}(t,\omega\_{t\land\cdot}) and returns +∞+\infty otherwise, then it would be convex, lower semicontinuous and coercive, while its convex conjugate would be continuous, which are the required properties.

### 5.1 Duality for European options

The financial interpretation of the setup introduced so far is standard. The process XX models price dynamics of dd assets traded continuously and in which investors are allowed to trade in a frictionless manner. We assume interest rates are deterministic and all prices are given in discounted units. Likewise, European or other payoffs, are expressed as functions of the discounted asset prices.

We start with a brief summary of the relevant robust pricing and hedging results for European options. As recalled in the introduction, many variants of continuous time pricing-hedging duality exist and they differ by assumptions they impose, the hedging strategies they consider and the regularity of the option payoff they can cover. Here, we adopt the OT-driven framework of Guo and Loeper ([2021](https://arxiv.org/html/2510.05463v1#bib.bib31)). We consider a function g∈Cb​(Ω;ℝm)g\in C\_{b}(\Omega;\mathbb{R}^{m}) which represents a vector of liquidly traded payoffs shifted by their market prices, so that a pricing measure ℙ\mathbb{P} is calibrated if 𝔼ℙ​(g)=0\mathbb{E}^{\mathbb{P}}(g)=0. We denote 𝒬gE⊂𝒬E\mathcal{Q}^{E}\_{g}\subset\mathcal{Q}^{E} the subset of calibrated pricing measures.

Suppose 𝒬gE\mathcal{Q}^{E}\_{g} represents all the pricing models we consider. Then for a European payoff ff its *robust model price* is given by

|  |  |  |
| --- | --- | --- |
|  | supℙ∈𝒬gE𝔼ℙ​f.\sup\_{\mathbb{P}\in\mathcal{Q}^{E}\_{g}}\mathbb{E}^{\mathbb{P}}f. |  |

On the other hand, we can consider a pricing-via-hedging argument, and look for the *superhedging price* defined as the smallest initial capital such that it is possible to construct a portfolio which superreplicates the payoff ff. Portfolios to consider can trade dynamically in the stock and also statically (buy-and-hold at time t=0t=0) in the vector gg of options with fixed market prices. In addition, the superreplication property needs to hold 𝒬gE\mathcal{Q}^{E}\_{g} quasi-surely (q.s.), that is ℙ\mathbb{P}-a.s., for all ℙ∈𝒬gE\mathbb{P}\in\mathcal{Q}^{E}\_{g}. So the superhedging price is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | πg,E​(f):=inf{x:∃(q,h)∈Cb​(Λ;ℝd)×ℝm,s.t.​x+∫01qt​𝑑Xt+h​g≥f,𝒬gE​-q.s.}.\pi\_{g,E}(f):=\operatorname\*{\vphantom{p}inf}\left\{x:\exists(q,h)\in C\_{b}(\Lambda;\mathbb{R}^{d})\times\mathbb{R}^{m},\ \text{s.t.}\ x+\int\_{0}^{1}q\_{t}dX\_{t}+hg\geq f,\ \mathcal{Q}^{E}\_{g}\text{-\text{q.s.}}\right\}. |  | (6) |

The key result, known as the *robust pricing-hedging duality*, asserts that these two approaches to computing the robust price for ff are consistent and give the same result.

###### Proposition 5.4 (Guo and Loeper ([2021](https://arxiv.org/html/2510.05463v1#bib.bib31))).

Suppose Assumption [5.1](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem1 "Assumption 5.1. ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") holds. Then for any f∈Cb​(Ω)f\in C\_{b}(\Omega),
πg,E​(f)=supℙ∈𝒬gE𝔼ℙ​[f]\pi\_{g,E}(f)=\sup\_{\mathbb{P}\in\mathcal{Q}^{E}\_{g}}\mathbb{E}^{\mathbb{P}}[f].

Note that we have restricted the hedging strategies to q∈Cb​(Λ;ℝd)q\in C\_{b}(\Lambda;\mathbb{R}^{d}) and, in particular, both sides of the superhedging inequality in the definition of πg,E​(f)\pi\_{g,E}(f) make sense pathwise on Ω\Omega thanks to ([3](https://arxiv.org/html/2510.05463v1#S4.E3 "In 4.1 Pathwise stochastic integration ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time")). Restricting to continuous integrands is sufficient since we only consider payoffs f∈Cb​(Ω)f\in C\_{b}(\Omega). For more general ff’s, we would need a larger class of hedging strategies, e.g., Denis and Martini ([2006](https://arxiv.org/html/2510.05463v1#bib.bib19)); Hou and Obłój ([2018](https://arxiv.org/html/2510.05463v1#bib.bib36)). This has been researched in detail in the past, see the discussion in section [1](https://arxiv.org/html/2510.05463v1#S1 "1 Introduction ‣ Robust Pricing and Hedging of American Options in Continuous Time") above. On the other hand, using only q∈Cb​(Λ;ℝd)q\in C\_{b}(\Lambda;\mathbb{R}^{d}) means we do not have to worry about fine questions of admissibility: since qq is bounded, the stochastic integral ∫0tqs​𝑑Xs\int\_{0}^{t}q\_{s}dX\_{s}, t∈[0,1]t\in[0,1], is a square integrable martingale under any ℙ∈𝒬\mathbb{P}\in\mathcal{Q}, and in particular its expectation is zero.

As shown in the previous section, the robust price of an American option is equal to the robust price of the corresponding European option in the enlarged space.
Hence, in order to establish dualities for American options, we will first establish dualities for European options in the enlarged space, in an analogue of Proposition [5.4](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem4 "Proposition 5.4 (Guo and Loeper (2021)). ‣ 5.1 Duality for European options ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time").

### 5.2 Duality for European options in the enlarged space

Under any probability measure ℙ\mathbb{P} on Ω¯\bar{\Omega}, ϑ\vartheta is a semimartingale with characteristics (𝟙[0,θ]​(t),0)(\mathds{1}\_{[0,\theta]}(t),0) and the integral t→∫0tqs​𝑑ϑst\to\int\_{0}^{t}q\_{s}d\vartheta\_{s} is defined pathwise on Ω¯\bar{\Omega} for q∈C​(Λ¯)q\in C(\bar{\Lambda}).
We let 𝒬¯\bar{\mathcal{Q}} be the set of probability measures ℙ\mathbb{P} on Ω¯\bar{\Omega} such that ℙ\mathbb{P} restricted to (Ω,𝔽1)(\Omega,\mathbb{F}\_{1}) is in 𝒬\mathcal{Q} and such that XX is a (ℙ,𝔽¯)(\mathbb{P},\bar{\mathbb{F}})-martingale. We recall that ⟨X⟩\langle X\rangle and β\beta were defined pathwise in ([5](https://arxiv.org/html/2510.05463v1#S5.E5 "In 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time")) and these definitions extend to Ω¯\bar{\Omega} with
⟨X⟩​(ω¯)=⟨X⟩​(ω)\langle X\rangle(\bar{\omega})=\langle X\rangle(\omega) and hence β​(ω¯)=β​(ω)\beta(\bar{\omega})=\beta(\omega).
For restrictions on β\beta, we consider Assumption [5.1](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem1 "Assumption 5.1. ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time"). Note that ϑ\vartheta automatically has a diffusion characteristic of 0, and we also don’t allow 𝔈\mathfrak{E} to depend on ϑ\vartheta. Then the set 𝒬¯E⊂Q¯\bar{\mathcal{Q}}^{E}\subset\bar{Q}, of martingale measures where β∈𝔈\beta\in\mathfrak{E}, and its subset 𝒬¯gE⊂𝒬¯E\bar{\mathcal{Q}}^{E}\_{g}\subset\bar{\mathcal{Q}}^{E} of calibrated measures, are clearly defined.

The definition of the *superhedging price* in ([6](https://arxiv.org/html/2510.05463v1#S5.E6 "In 5.1 Duality for European options ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time")) naturally extends to Ω¯\bar{\Omega}:

|  |  |  |
| --- | --- | --- |
|  | π¯g,E​(f):=inf{x:∃(q,h)∈Cb​(Λ¯;ℝd)×ℝm,s.t.​x+∫01qt​𝑑Xt+h​g≥f,𝒬¯gE​-q.s.}.\bar{\pi}\_{g,E}(f):=\operatorname\*{\vphantom{p}inf}\{x:\exists(q,h)\in C\_{b}(\bar{\Lambda};\mathbb{R}^{d})\times\mathbb{R}^{m},\ \text{s.t.}\ x+\int\_{0}^{1}q\_{t}dX\_{t}+hg\geq f,\ \bar{\mathcal{Q}}^{E}\_{g}\text{-\text{q.s.}}\}. |  |

When the vector gg is empty we will simply write π¯E​(f)\bar{\pi}\_{E}(f).

###### Proposition 5.5.

Suppose Assumption [5.1](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem1 "Assumption 5.1. ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") holds and f∈Cb​(Ω¯)f\in C\_{b}(\bar{\Omega}).
Then
π¯g,E​(f)=supℙ¯∈𝒬¯gE𝔼ℙ¯​f\bar{\pi}\_{g,E}(f)=\sup\_{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}\_{g}}\mathbb{E}^{\bar{\mathbb{P}}}f.

###### Proof.

By taking expectations, it is easy to check that

|  |  |  |
| --- | --- | --- |
|  | π¯g,E​(f)≥supℙ¯∈𝒬¯gE𝔼ℙ¯​f.\bar{\pi}\_{g,E}(f)\geq\sup\_{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}\_{g}}\mathbb{E}^{\bar{\mathbb{P}}}f. |  |

To show the reverse inequality we apply the main duality result of Guo and Loeper ([2021](https://arxiv.org/html/2510.05463v1#bib.bib31)) on the enlarged spaces Ω¯\bar{\Omega} and Λ¯\bar{\Lambda}, with a cost function that
equals 0 if β​(t,ω⋅∧t)∈𝔈​(t,ω⋅∧t)\beta(t,\omega\_{\cdot\wedge t})\in\mathfrak{E}(t,\omega\_{\cdot\wedge t}), or equals infinity otherwise.
The duality gives us that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supℙ¯∈𝒬¯gE𝔼ℙ¯​f=infh∈ℝm,ϕ∈C01,1,2​(Λ¯)ϕ​(0,0,X0),\displaystyle\sup\_{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}\_{g}}\mathbb{E}^{\bar{\mathbb{P}}}f=\operatorname\*{\vphantom{p}inf}\_{h\in\mathbb{R}^{m},\phi\in C^{1,1,2}\_{0}(\bar{\Lambda})}\phi(0,0,X\_{0}), |  | (7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | subject toϕ(1,⋅,⋅)≥f−hgand𝒟tϕ+𝟙(t≤θ)∇θϕ+supβ∈𝔈12β:∇x2ϕ≤0,\displaystyle\text{subject to}\quad\phi(1,\cdot,\cdot)\geq f-hg\quad\text{and}\quad\mathcal{D}\_{t}\phi+\mathds{1}(t\leq\theta)\nabla\_{\theta}\phi+\sup\_{\beta\in\mathfrak{E}}\frac{1}{2}\beta:\nabla\_{x}^{2}\phi\leq 0, |  | (8) |

where the set of test functions is defined as follows.
We say ϕ∈C1,1,2​(Λ¯)\phi\in C^{1,1,2}(\bar{\Lambda}) if ϕ∈Cb​(Λ¯)\phi\in C\_{b}(\bar{\Lambda}) and there exist functions (𝒟t​ϕ,∇θϕ,∇xϕ,∇x2ϕ)∈Cb​(Λ¯;ℝd+2×𝕊d)(\mathcal{D}\_{t}\phi,\nabla\_{\theta}\phi,\nabla\_{x}\phi,\nabla\_{x}^{2}\phi)\in C\_{b}(\bar{\Lambda};\mathbb{R}^{d+2}\times\mathbb{S}^{d}) such that, for any ℙ¯∈𝒬¯\bar{\mathbb{P}}\in\bar{\mathcal{Q}} and u∈[0,1]u\in[0,1], the following *functional Itô formula* holds:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ϕ​(u,ϑ,X)−ϕ​(0,ϑ,X)\displaystyle\phi(u,\vartheta,X)-\phi(0,\vartheta,X) | =∫0u𝒟t​ϕ​𝑑s+∇θϕ​d​ϑs+∇xϕ​d​Xs+12​∇x2ϕ:d​⟨X⟩s\displaystyle=\int\_{0}^{u}\mathcal{D}\_{t}\phi\,ds+\nabla\_{\theta}\phi\,d\vartheta\_{s}+\nabla\_{x}\phi\,dX\_{s}+\frac{1}{2}\nabla\_{x}^{2}\phi:d\langle X\rangle\_{s} |  | (9) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0u(𝒟t​ϕ+𝟙[0,θ]​∇θϕ)​𝑑s+∇xϕ​d​Xs+12​∇x2ϕ:d​⟨X⟩s,ℙ¯​-a.s.\displaystyle=\int\_{0}^{u}(\mathcal{D}\_{t}\phi+\mathds{1}\_{[0,\theta]}\nabla\_{\theta}\phi)\,ds+\nabla\_{x}\phi\,dX\_{s}+\frac{1}{2}\nabla\_{x}^{2}\phi:d\langle X\rangle\_{s},\quad\bar{\mathbb{P}}\text{-\text{a.s.}} |  |

From this definition, it follows directly that for each ϕ\phi satisfying ([8](https://arxiv.org/html/2510.05463v1#S5.E8 "In 5.2 Duality for European options in the enlarged space ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time")) and each ℙ¯∈𝒬¯E\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}, the following holds ℙ¯\bar{\mathbb{P}}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
|  | f−h​g−ϕ​(0,0,X0)≤\displaystyle f-hg-\phi(0,0,X\_{0})\leq | ϕ​(1,⋅,⋅)−ϕ​(0,0,X0)\displaystyle\ \phi(1,\cdot,\cdot)-\phi(0,0,X\_{0}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01(𝒟tϕ+𝟙[0,θ]∇θϕ+12βℙ:∇x2ϕ)dt+∇xϕdXt\displaystyle=\int\_{0}^{1}(\mathcal{D}\_{t}\phi+\mathds{1}\_{[0,\theta]}\nabla\_{\theta}\phi+\,\frac{1}{2}\beta^{\mathbb{P}}:\nabla\_{x}^{2}\phi)dt+\nabla\_{x}\phi\,dX\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫01∇xϕ​d​Xt.\displaystyle\leq\int\_{0}^{1}\nabla\_{x}\phi\,dX\_{t}. |  |

As ∇xϕ∈Cb​(Λ¯;ℝd)\nabla\_{x}\phi\in C\_{b}(\bar{\Lambda};\mathbb{R}^{d}) is an admissible hedging strategy, we deduce that ϕ​(0,0,X0)≥π¯g,E​(f)\phi(0,0,X\_{0})\geq\bar{\pi}\_{g,E}(f). Since this holds for all ϕ\phi satisfying ([8](https://arxiv.org/html/2510.05463v1#S5.E8 "In 5.2 Duality for European options in the enlarged space ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time")), it implies supℙ¯∈𝒬¯gE𝔼ℙ¯​f≥π¯g,E​(f)\sup\_{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}\_{g}}\mathbb{E}^{\bar{\mathbb{P}}}f\geq\bar{\pi}\_{g,E}(f), completing the proof.
∎

###### Remark 5.6.

We defined the set C1,1,2​(Λ¯)C^{1,1,2}(\bar{\Lambda}) by requiring that the functional Itô formula holds for all ℙ¯∈𝒬¯\bar{\mathbb{P}}\in\bar{\mathcal{Q}}, which is a smaller set than the set of all semimartingale measures with integrable characteristics used in Guo and Loeper ([2021](https://arxiv.org/html/2510.05463v1#bib.bib31)). This means that the equality in ([7](https://arxiv.org/html/2510.05463v1#S5.E7 "In 5.2 Duality for European options in the enlarged space ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time")) shown therein could, *a priori*, turn to an inequality “LHS≥\geq RHS” with our definition. However, the rest of the proof then shows that the equality in fact holds through the sandwiching with the first inequality.

###### Remark 5.7.

It follows from the proof that in the definition of the superhedging price, we can restrict further the hedging strategies and instead of (q,h)∈Cb​(Λ¯;ℝd)×ℝm(q,h)\in C\_{b}(\bar{\Lambda};\mathbb{R}^{d})\times\mathbb{R}^{m} it suffices to consider (q,h)∈Cx​(Λ¯;ℝd)×ℝm(q,h)\in C\_{x}(\bar{\Lambda};\mathbb{R}^{d})\times\mathbb{R}^{m}, where

|  |  |  |
| --- | --- | --- |
|  | Cx​(Λ¯;ℝd)={∇xϕ:ϕ∈C1,1,2​(Λ¯)}.C\_{x}(\bar{\Lambda};\mathbb{R}^{d})=\left\{\nabla\_{x}\phi:\phi\in C^{1,1,2}(\bar{\Lambda})\right\}. |  |

We also note that for such (q,h)∈Cx​(Λ¯;ℝd)×ℝm(q,h)\in C\_{x}(\bar{\Lambda};\mathbb{R}^{d})\times\mathbb{R}^{m}, the functional Itô formula can be used to *define* the integral ∫0⋅qs​𝑑Xs\int\_{0}^{\cdot}q\_{s}dX\_{s} pathwise on Ω¯\bar{\Omega}. This definition would potentially differ from ([3](https://arxiv.org/html/2510.05463v1#S4.E3 "In 4.1 Pathwise stochastic integration ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time")) but the two agree ℙ¯\bar{\mathbb{P}}-a.s., for any ℙ¯∈𝒬¯\bar{\mathbb{P}}\in\bar{\mathcal{Q}}.

### 5.3 Duality for American options

Finally, we can return to the problem of superhedging of American options and link it to the superhedging for European options in the enlarged space. Recall that for Z∈Cb​(Λ)Z\in C\_{b}(\Lambda) we write Z¯​(ω¯)=Z​(θ,ω⋅∧θ)\bar{Z}(\bar{\omega})=Z(\theta,\omega\_{\cdot\land\theta}).
Following Remark [5.7](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem7 "Remark 5.7. ‣ 5.2 Duality for European options in the enlarged space ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") we observe that in the setup of Proposition [5.5](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem5 "Proposition 5.5. ‣ 5.2 Duality for European options in the enlarged space ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | π¯g,E​(Z¯)\displaystyle\bar{\pi}\_{g,E}(\bar{Z}) | =inf{x:∃(q¯,h¯)∈Cx​(Λ¯)×ℝm,s.t.​x+∫01q¯t​𝑑Xt+h¯​g≥Z¯,𝒬¯gE​-q.s.}.\displaystyle=\operatorname\*{\vphantom{p}inf}\{x:\exists(\bar{q},\bar{h})\in C\_{x}(\bar{\Lambda})\times\mathbb{R}^{m},\ \text{s.t.}\ x+\int\_{0}^{1}\bar{q}\_{t}dX\_{t}+\bar{h}g\geq\bar{Z},\ \bar{\mathcal{Q}}^{E}\_{g}\text{-\text{q.s.}}\}. |  |

We then have the following inequality.

###### Lemma 5.8.

Suppose Assumption [5.1](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem1 "Assumption 5.1. ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time") holds and Z∈Cb​(Λ)Z\in C\_{b}(\Lambda). Then π¯g,E​(Z¯)≥πg,EA​(Z)\bar{\pi}\_{g,E}(\bar{Z})\geq\pi^{A}\_{g,E}(Z).

###### Proof.

Suppose (q¯,h¯)(\bar{q},\bar{h}) is a superhedge for π¯g,E​(Z¯)\bar{\pi}\_{g,E}(\bar{Z}).
We construct the following superhedge (q,q~,h)(q,\tilde{q},h) for πg,EA​(Z)\pi^{A}\_{g,E}(Z), noting that q~θ​(t,⋅)\tilde{q}^{\theta}(t,\cdot) is only relevant for t≥θt\geq\theta.

|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(t,ω⋅∧t)\displaystyle q(t,\omega\_{\cdot\wedge t}) | =q¯​(t,t,ω⋅∧t),\displaystyle=\bar{q}(t,t,\omega\_{\cdot\wedge t}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | q~θ​(t,ω⋅∧t)\displaystyle\tilde{q}^{\theta}(t,\omega\_{\cdot\wedge t}) | =q¯​(t,θ,ω⋅∧t),t≥θ,\displaystyle=\bar{q}(t,\theta,\omega\_{\cdot\wedge t}),\quad t\geq\theta, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | h\displaystyle h | =h¯.\displaystyle=\bar{h}. |  |

It remains to check that (q,q~,h)(q,\tilde{q},h) is indeed a superhedge for πg,EA​(Z)\pi^{A}\_{g,E}(Z).
For each rational u∈[0,1]u\in[0,1] and ℙ∈𝒬gE\mathbb{P}\in\mathcal{Q}^{E}\_{g}, we can define ℙ¯=δu×ℙ\bar{\mathbb{P}}=\delta\_{u}\times\mathbb{P}. It is easy to check that ℙ¯∈𝒬¯gE\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}\_{g}.
Hence

|  |  |  |
| --- | --- | --- |
|  | x+∫0uq​𝑑Xt+∫u1q~u​𝑑Xt+h​g≥Zu,ℙ​-a.s..x+\int\_{0}^{u}qdX\_{t}+\int\_{u}^{1}\tilde{q}^{u}dX\_{t}+hg\geq Z\_{u},\quad\mathbb{P}\text{-\text{a.s.}}. |  |

To extend from rational uu to all reals, first note that ZuZ\_{u} is continuous in uu. On the other side, by the definition of qq and q~u\tilde{q}^{u},

|  |  |  |
| --- | --- | --- |
|  | ∫0uq​𝑑Xt+∫u1q~u​𝑑Xt=∫01q¯​(t,u∧t,⋅)​𝑑Xt.\displaystyle\int\_{0}^{u}qdX\_{t}+\int\_{u}^{1}\tilde{q}^{u}dX\_{t}=\int\_{0}^{1}\bar{q}(t,u\wedge t,\cdot)dX\_{t}. |  |

Recall q¯∈Cx​(Λ¯)\bar{q}\in C\_{x}(\bar{\Lambda}), so there exists ϕ∈C1,1,2​(Λ¯)\phi\in C^{1,1,2}(\bar{\Lambda}) such that q¯=∇xϕ\bar{q}=\nabla\_{x}\phi. Then by the functional Itô formula in ([9](https://arxiv.org/html/2510.05463v1#S5.E9 "In 5.2 Duality for European options in the enlarged space ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time")),

|  |  |  |
| --- | --- | --- |
|  | ∫01q¯​(t,u∧t,⋅)​𝑑Xt=ϕ​(1,u,⋅)−ϕ​(0,u,⋅)−∫01(𝒟t​ϕ+𝟙[0,u]​∇θϕ)​𝑑s+12​∇x2ϕ:d​⟨X⟩s,ℙ​-a.s.\displaystyle\int\_{0}^{1}\bar{q}(t,u\wedge t,\cdot)dX\_{t}=\phi(1,u,\cdot)-\phi(0,u,\cdot)-\int\_{0}^{1}(\mathcal{D}\_{t}\phi+\mathds{1}\_{[0,u]}\nabla\_{\theta}\phi)\,ds+\frac{1}{2}\nabla\_{x}^{2}\phi:d\langle X\rangle\_{s},\quad\mathbb{P}\text{-\text{a.s.}} |  |

Since ϕ,𝒟t​ϕ,∇θϕ,∇x2ϕ\phi,\mathcal{D}\_{t}\phi,\nabla\_{\theta}\phi,\nabla\_{x}^{2}\phi are all bounded and continuous, and XX has a bounded diffusion characteristic under ℙ\mathbb{P}, the right hand side, and hence also the left hand side, is continuous in uu.
Thus

|  |  |  |
| --- | --- | --- |
|  | x+∫0uq​𝑑Xt+∫u1q~u​𝑑Xt+h​g≥Zu,∀u∈[0,1],ℙ​-a.s.x+\int\_{0}^{u}qdX\_{t}+\int\_{u}^{1}\tilde{q}^{u}dX\_{t}+hg\geq Z\_{u},\quad\forall\,u\in[0,1],\quad\mathbb{P}\text{-\text{a.s.}} |  |

Since this holds for all ℙ∈𝒬gE\mathbb{P}\in\mathcal{Q}^{E}\_{g}, it must be a πg,EA​(Z)\pi^{A}\_{g,E}(Z) superhedge. Thus π¯g,E​(Z¯)≥πg,EA​(Z)\bar{\pi}\_{g,E}(\bar{Z})\geq\pi^{A}\_{g,E}(Z).
∎

###### Proof of Theorem [5.2](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem2 "Theorem 5.2. ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time").

The required result follows from the following chain of inequalities

|  |  |  |  |
| --- | --- | --- | --- |
|  | π¯g​(Z¯)≥πgA​(Z)≥π^A​(Z^)≥supℙ^∈𝒬^E,τ^∈𝒯^ℙ^𝔼ℙ^​Z^τ^=supℙ^¯∈𝒬^¯E𝔼ℙ^¯​Z^¯≥supℙ¯∈𝒬¯gE𝔼ℙ¯​Z¯=π¯g​(Z¯),\displaystyle\bar{\pi}\_{g}(\bar{Z})\geq\pi^{A}\_{g}(Z)\geq\widehat{\pi}^{A}(\widehat{Z})\geq\sup\_{\widehat{\mathbb{P}}\in\widehat{\mathcal{Q}}^{E},\widehat{\tau}\in\widehat{\mathcal{T}}^{\widehat{\mathbb{P}}}}\mathbb{E}^{\widehat{\mathbb{P}}}\widehat{Z}\_{\widehat{\tau}}=\sup\_{\bar{\widehat{\mathbb{P}}}\in\bar{\widehat{\mathcal{Q}}}^{E}}\mathbb{E}^{\bar{\widehat{\mathbb{P}}}}\bar{\widehat{Z}}\geq\sup\_{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}\_{g}}\mathbb{E}^{\bar{\mathbb{P}}}\bar{Z}=\bar{\pi}\_{g}(\bar{Z}), |  | (10) |

which implies that there must be equality throughout. We will now justify each step.

The first inequality π¯g​(Z¯)≥πgA​(Z)\bar{\pi}\_{g}(\bar{Z})\geq\pi^{A}\_{g}(Z) was just established in Lemma [5.8](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem8 "Lemma 5.8. ‣ 5.3 Duality for American options ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time"), while the last equality π¯g​(Z¯)=supℙ¯∈𝒬¯gE𝔼ℙ¯​Z¯\bar{\pi}\_{g}(\bar{Z})=\sup\_{\bar{\mathbb{P}}\in\bar{\mathcal{Q}}^{E}\_{g}}\mathbb{E}^{\bar{\mathbb{P}}}\bar{Z} is the European duality in the enlarged space, proven in Proposition [5.5](https://arxiv.org/html/2510.05463v1#S5.Thmtheorem5 "Proposition 5.5. ‣ 5.2 Duality for European options in the enlarged space ‣ 5 Robust pricing-hedging duality for American options ‣ Robust Pricing and Hedging of American Options in Continuous Time"). The remaining chain of inequalities was proven in Proposition [4.5](https://arxiv.org/html/2510.05463v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3 Duality gap and a dynamic extension for statically traded European options ‣ 4 Robust hedging of American options and weak pricing-hedging duality ‣ Robust Pricing and Hedging of American Options in Continuous Time").
∎

## References

* Aksamit et al. (2019)

  Anna Aksamit, Shuoqing Deng, Jan Obłój, and Xiaolu Tan.
  The robust pricing–hedging duality for American options in
  discrete time financial markets.
  *Mathematical Finance*, 29(3):861–897,
  2019.
* Aksamit et al. (2020)

  Anna Aksamit, Zhaoxu Hou, and Jan Obłój.
  Robust framework for quantifying the value of information in pricing
  and hedging.
  *SIAM Journal on Financial Mathematics*, 11(1):27–59, 2020.
* Allan et al. (2023)

  Andrew L. Allan, Chong Liu, and David J. Prömel.
  A càdlàg rough path foundation for robust finance.
  *Finance and Stochastics*, 28(1):215–257,
  2023.
* Azéma (1972)

  Jacques Azéma.
  Quelques applications de la théorie générale des processus.
  I.
  *Inventiones Mathematicae*, 18:293–336, 1972.
* Baxter and Chacon (1977)

  J. R. Baxter and R. V. Chacon.
  Compactness of stopping times.
  *Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte
  Gebiete*, 40(3):169–181, 1977.
* Bayraktar and Zhou (2017)

  Erhan Bayraktar and Zhou Zhou.
  Super-hedging American options with semi-static trading strategies
  under model uncertainty.
  *International Journal of Theoretical and Applied Finance*,
  20(06):1750036, 2017.
* Bayraktar et al. (2015)

  Erhan Bayraktar, Yu-Jui Huang, and Zhou Zhou.
  On hedging American options under model uncertainty.
  *SIAM Journal on Financial Mathematics*, 6(1):425–447, 2015.
* Beiglböck et al. (2013)

  Mathias Beiglböck, Pierre Henry-Labordère, and Friedrich Penkner.
  Model-independent bounds for option prices: a mass transport
  approach.
  *Finance and Stochastics*, 17(3):477–501,
  2013.
* Beiglböck et al. (2016)

  Mathias Beiglböck, Alexander M. G. Cox, and Martin Huesmann.
  Optimal transport and Skorokhod embedding.
  *Inventiones mathematicae*, 208(2):327–400,
  2016.
* Black and Scholes (1973)

  Fischer Black and Myron Scholes.
  The pricing of options and corporate liabilities.
  *Journal of Political Economy*, 81(3):637–654, 1973.
* Bouchard and Nutz (2015)

  Bruno Bouchard and Marcel Nutz.
  Arbitrage and duality in nondominated discrete-time models.
  *The Annals of Applied Probability*, 25(2):823–859, 2015.
* Breeden and Litzenberger (1978)

  Douglas T. Breeden and Robert H. Litzenberger.
  Prices of state-contingent claims implicit in option prices.
  *Journal of Business*, pages 621–651, 1978.
* Brown et al. (2001)

  Haydyn Brown, David Hobson, and L. C. G. Rogers.
  Robust hedging of barrier options.
  *Mathematical Finance*, 11(3):285–314,
  2001.
* Burzoni et al. (2019)

  Matteo Burzoni, Marco Frittelli, Zhaoxu Hou, Marco Maggis, and Jan Obłój.
  Pointwise arbitrage pricing theory in discrete time.
  *Mathematics of Operations Research*, 44(3):1034–1057, 2019.
* Cont and Fournié (2013)

  Rama Cont and David-Antoine Fournié.
  Functional Itô calculus and stochastic integral representation of
  martingales.
  *The Annals of Probability*, 41(1):109–133,
  2013.
* Cox and Obłój (2011)

  Alexander M. G. Cox and Jan Obłój.
  Robust pricing and hedging of double no-touch options.
  *Finance and Stochastics*, 15(3):573–605,
  2011.
* Cvitanic and Karatzas (1993)

  Jaksa Cvitanic and Ioannis Karatzas.
  Hedging contingent claims with constrained portfolios.
  *The Annals of Applied Probability*, 3(3), 1993.
* Davis et al. (2018)

  Mark Davis, Jan Obłój, and Pietro Siorpaes.
  Pathwise stochastic calculus with local times.
  *Annales de l’Institut Henri Poincaré, Probabilités et
  Statistiques*, 54(1):1–21, 2018.
* Denis and Martini (2006)

  Laurent Denis and Claude Martini.
  A theoretical framework for the pricing of contingent claims in the
  presence of model uncertainty.
  *The Annals of Applied Probability*, 16(2):827–852, 2006.
* Dolinsky (2014)

  Yan Dolinsky.
  Hedging of game options under model uncertainty in discrete time.
  *Electronic Communications in Probability*, 19:1–11,
  2014.
* Dolinsky and Soner (2014)

  Yan Dolinsky and H Mete Soner.
  Martingale optimal transport and robust hedging in continuous time.
  *Probability Theory and Related Fields*, 160(1-2):391–427, 2014.
* Dunford and Schwartz (1958)

  Nelson Dunford and Jacob T. Schwartz.
  *Linear Operators Part I: General Theory*, volume 7 of
  *Pure and Applied Mathematics*.
  Interscience Publishers, New York, 1958.
* Eckstein et al. (2021)

  Stephan Eckstein, Gaoyue Guo, Tongseok Lim, and Jan Obłój.
  Robust pricing and hedging of options on multiple assets and its
  numerics.
  *SIAM Journal on Financial Mathematics*, 12(1):158–188, 2021.
* El Karoui and Tan (2013)

  Nicole El Karoui and Xiaolu Tan.
  Capacities, measurable selection and dynamic programming Part II:
  Application in stochastic control problems.
  *arXiv preprint arXiv:1310.3364*, 2013.
* Föllmer (1981)

  Hans Föllmer.
  Calcul d’Itô sans probabilites.
  In *Séminaire de Probabilités XV 1979/80*, pages
  143–150, Berlin, Heidelberg, 1981. Springer Berlin Heidelberg.
* Föllmer and Schied (2004)

  Hans Föllmer and Alexander Schied.
  *Stochastic Finance: An Introduction in Discrete Time*.
  Walter de Gruyter, 2nd edition, 2004.
* Fremlin et al. (1972)

  D. H. Fremlin, D. J. H. Garling, and R. G. Haydon.
  Bounded measures on topological spaces.
  *Proceedings of the London Mathematical Society*, 3(1):115–136, 1972.
* Galichon et al. (2014)

  Alfred Galichon, Pierre Henry-Labordère, and Nizar Touzi.
  A stochastic control approach to no-arbitrage bounds given marginals,
  with an application to lookback options.
  *The Annals of Applied Probability*, 24(1):312–336, 2014.
* Guo and Obłój (2019)

  Gaoyue Guo and Jan Obłój.
  Computational methods for martingale optimal transport problems.
  *The Annals of Applied Probability*, 29(6):pp. 3311–3347, 2019.
* Guo et al. (2017)

  Gaoyue Guo, Xiaolu Tan, and Nizar Touzi.
  Tightness and duality of martingale transport on the Skorokhod
  space.
  *Stochastic Processes and their Applications*, 127(3):927–956, 2017.
* Guo and Loeper (2021)

  Ivan Guo and Gregoire Loeper.
  Path dependent optimal transport and model calibration on exotic
  derivatives.
  *The Annals of Applied Probability*, 31(3):1232–1263, 2021.
* Hansen and Marinacci (2016)

  Lars Peter Hansen and Massimo Marinacci.
  Ambiguity aversion and model misspecification: An economic
  perspective.
  *Statistical Science*, 31(4):511–515, 2016.
* Hobson (1998)

  David Hobson.
  Robust hedging of the lookback option.
  *Finance and Stochastics*, 2(4):329–347,
  1998.
* Hobson (2011)

  David Hobson.
  The Skorokhod embedding problem and model-independent bounds for
  option prices.
  In *Paris-Princeton Lectures on Mathematical Finance
  2010*, volume 2003 of *Lecture Notes in Math.*, pages 267–318.
  Springer, Berlin, 2011.
* Hobson and Neuberger (2017)

  David Hobson and Anthony Neuberger.
  Model uncertainty and the pricing of American options.
  *Finance and Stochastics*, 21(1):285–329,
  2017.
* Hou and Obłój (2018)

  Zhaoxu Hou and Jan Obłój.
  Robust pricing-hedging dualities in continuous time.
  *Finance and Stochastics*, 22(3):511–567,
  2018.
* Itô and Watanabe (1965)

  Kiyosi Itô and Shinzo Watanabe.
  Transformation of Markov processes by multiplicative functionals.
  *Annales de l’Institut Fourier*, 15(1):13–30, 1965.
* Karandikar (1995)

  Rajeeva L. Karandikar.
  On pathwise stochastic integration.
  *Stochastic Processes and their Applications*, 57(1):11–18, 1995.
* Karatzas and Shreve (1998)

  Ioannis Karatzas and Steven E. Shreve.
  *Methods of Mathematical Finance*, volume 39 of
  *Probability Theory and Stochastic Modelling*.
  Springer, 1998.
* Knight (1921)

  Frank H. Knight.
  *Risk, Uncertainty, and Profit*.
  Houghton Mifflin, Boston, 1921.
* Le Cam (1957)

  Lucien Le Cam.
  Convergence in distribution of stochastic processes.
  *University of California Publications in Statistics*,
  2:207–236, 1957.
* Li et al. (2022)

  Libo Li, Ruyi Liu, and Marek Rutkowski.
  Vulnerable european and american options in a market model with
  optional hazard process.
  *arXiv preprint arXiv:2212.12860*, 2022.
* Merton (1973)

  Robert C. Merton.
  Theory of rational option pricing.
  *The Bell Journal of Economics and Management Science*,
  4(1):141–183, 1973.
* Meyer (1978)

  P. A. Meyer.
  Convergence faible et compacite des temps d’arret d’apres baxter et
  chacon.
  In *Séminaire de Probabilités XII*, pages 411–423.
  Springer Berlin Heidelberg, 1978.
* Mykland (2003)

  Per Aslak Mykland.
  Financial options and statistical prediction intervals.
  *The Annals of Statistics*, 31(5):1413–1438, 2003.
* Myneni (1992)

  Ravi Myneni.
  The pricing of the American option.
  *Ann. Appl. Probab.*, 2(1):1–23, 1992.
* Neuberger (2007)

  Anthony Neuberger.
  Bounds on the American option.
  *Preprint, http://ssrn.com/abstract=966333*, 2007.
* Neufeld and Nutz (2013)

  Ariel Neufeld and Marcel Nutz.
  Superreplication under volatility uncertainty for measurable
  claims.
  *Electronic Journal of Probability*, 18:1–14, 2013.
* Obłój (2004)

  Jan Obłój.
  The Skorokhod embedding problem and its offspring.
  *Probability Surveys*, 1:321–392, 2004.
  doi: 10.1214/154957804100000060.
* Obłój and Wiesel (2021)

  Jan Obłój and Johannes Wiesel.
  A unified framework for robust modelling of financial markets in
  discrete time.
  *Finance and Stochastics*, 25(3):427–468,
  2021.
* Peng (2019)

  Shige Peng.
  *Nonlinear Expectations and Stochastic Calculus under
  Uncertainty: with Robust CLT and G-Brownian Motion*.
  Springer Berlin Heidelberg, 2019.
* Perkowski and Prömel (2015)

  Nicolas Perkowski and David Prömel.
  Local times for typical price paths and pathwise Tanaka formulas.
  *Electronic Journal of Probability*, 20:1–15, 2015.
* Possamaï et al. (2013)

  Dylan Possamaï, Guillaume Royer, and Nizar Touzi.
  On the robust superhedging of measurable claims.
  *Electronic Communications in Probability*, 18:1–13,
  2013.
* Sentilles (1972)

  F. Dennis Sentilles.
  Bounded continuous functions on a completely regular space.
  *Transactions of the American Mathematical Society*,
  168:311–336, 1972.
* Shmaya and Solan (2014)

  Eran Shmaya and Eilon Solan.
  Equivalence between random stopping times in continuous time.
  *arXiv preprint arXiv:1403.7886*, 2014.
* Soner et al. (2013)

  H. Mete Soner, Nizar Touzi, and Jianfeng Zhang.
  Dual formulation of second order target problems.
  *Annals of Applied Probability*, 23(1):308–347, 2013.
* Stewart (2012)

  Ian Stewart.
  *Seventeen equations that changed the world*.
  Profile, London, 2012.
* Tan et al. (2013)

  Xiaolu Tan, Nizar Touzi, et al.
  Optimal transportation under controlled stochastic dynamics.
  *The annals of probability*, 41(5):3201–3240, 2013.
* Vovk (2012)

  Vladimir Vovk.
  Continuous-time trading and the emergence of probability.
  *Finance and Stochastics*, 16(4):561–609,
  2012.
* Walley (1991)

  Peter Walley.
  *Statistical Reasoning with Imprecise Probabilities*.
  Chapman & Hall, 1991.