---
authors:
- Lan Bu
- Ning Cai
- Chenxi Xia
- Jingping Yang
doc_id: arxiv:2602.08039v1
family_id: arxiv:2602.08039
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2602.08039v1
url_html: https://arxiv.org/html/2602.08039v1
venue: arXiv q-fin
version: 1
year: 2026
---

\OneAndAHalfSpacedXII\EquationsNumberedThrough\TheoremsNumberedThrough\ECRepeatTheorems\MANUSCRIPTNO

MOOR-0001-2024.00

\RUNAUTHOR

Bu, Cai, Xia and Yang

\RUNTITLE

Perfectly Fitting CDO Prices Across Tranches

\TITLE

Perfectly Fitting CDO Prices Across Tranches: A Theoretical Framework with Efficient Algorithms

\ARTICLEAUTHORS\AUTHOR

Lan Bu
\AFFFinancial Technology Thrust, Hong Kong University of Science and Technology (Guangzhou) \EMAILbulan@pku.edu.cn
\AUTHORNing Cai
\AFFFinancial Technology Thrust, Hong Kong University of Science and Technology (Guangzhou) \EMAILningcai@hkust-gz.edu.cn
\AUTHORChenxi Xia
\AFFSchool of Mathematical Sciences, Peking University \EMAILxiacx@pku.edu.cn
\AUTHORJingping Yang
\AFFSchool of Mathematical Sciences, Peking University \EMAILyangjp@math.pku.edu.cn

\ABSTRACT

This paper addresses a key challenge in CDO modeling: achieving a perfect fit to market prices across all tranches using a single, consistent model. The existence of such a perfect-fit model implies the absence of arbitrage among CDO tranches and is thus essential for unified risk management and the pricing of nonstandard credit derivatives.
To address this central challenge, we face three primary difficulties: standard parametric models typically fail to achieve a perfect fit; the calibration of standard parametric models inherently relies on computationally intensive simulation-based optimization; and there is a lack of formal theory to determine when a perfect-fit model exists and, if it exists, how to construct it. We propose a theoretical framework to overcome these difficulties. We first introduce and define two compatibility levels of market prices—weak compatibility and strong compatibility. Specifically, market prices across all tranches are said to be weakly (resp. strongly) compatible if there exists a single model (resp. a single conditionally i.i.d. model) that perfectly fits these market prices.
We then derive sufficient and necessary conditions for both levels of compatibility by establishing a relationship between compatibility and linear programming (LP) problems.
Furthermore, under either condition, we construct a corresponding concrete copula model that achieves a perfect fit. Notably, our framework not only allows for efficient verification of weak compatibility and strong compatibility through LP problems but also facilitates the construction of the corresponding copula models that achieve a perfect fit, eliminating the need for simulation-based optimization.
The practical applications of our framework are demonstrated in risk management (e.g., designing effective hedging strategies and estimating loss distributions for credit portfolios) and the pricing of nonstandard credit derivatives.

\KEYWORDS

CDO modeling, Perfect fit, Copula, Weak compatibility, Strong compatibility

## 1 Introduction

### 1.1 Background and Motivations

Collateralized Debt Obligations (CDOs) constitute a significant segment of the credit markets, as underscored both by their substantial trading volume with the notional value of iTraxx/CDX tranches traded in 2023 estimated at $335 billion (Godec and Masabathula [2024](https://arxiv.org/html/2602.08039v1#bib.bib70 "Fixed Income Special Report 2023")) and by their instrumental role as primary tools for correlation trading (Mounfield [2009](https://arxiv.org/html/2602.08039v1#bib.bib24 "Synthetic cdos: modelling, valuation and risk management")). A critical objective in CDO modeling is to develop a single, consistent model that achieves a “perfect fit” to market prices across all tranches—by this, we mean a model capable of generating prices that exactly align with market prices across all tranches (Hull and White [2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")). Such a consistent model with perfect fit (called a “perfect-fit” model hereafter) is essential for important applications, such as unified risk management and the pricing of nonstandard credit derivatives. It not only offers a cohesive framework for designing self-consistent hedging strategies for credit portfolios and calculating credit portfolios’ loss distributions, but also enables the arbitrage-free pricing of nonstandard credit derivatives, including CDOs with nonstandard attachment and detachment points and CDOs with a nonstandard number of underlying names.

There are three primary difficulties in achieving the “perfect fit” objective. First, standard parametric models generally fall short of attaining a perfect fit to market prices across all tranches. Regarding the seminal and influential Gaussian copula model proposed by Li ([2000](https://arxiv.org/html/2602.08039v1#bib.bib20 "On default correlation: a copula function approach")), identifying a single Gaussian copula model that perfectly fits market prices across all tranches proves difficult. Indeed, “correlation smiles” emerge (Moosbrucker [2006](https://arxiv.org/html/2602.08039v1#bib.bib22 "Explaining the correlation smile using variance gamma distributions")), indicating that different tranches imply different correlations, thereby rendering Gaussian copula models inadequate for achieving a perfect fit. A more serious limitation is that even when a single Gaussian copula model is used to fit the market prices of an individual tranche, the implied correlation is often non-unique or even non-existent (e.g., Brigo et al. [2010](https://arxiv.org/html/2602.08039v1#bib.bib64 "Credit models and the crisis: a journey into cdos, copulas, correlations and dynamic models") and McNeil et al. [2015](https://arxiv.org/html/2602.08039v1#bib.bib1 "Quantitative risk management: concepts, techniques and tools")). In the literature, a variety of different parametric copula models have been proposed, including elliptical copulas (e.g., the Student’s tt copula), Archimedean copulas (e.g., the Clayton and nested Archimedean families; see, e.g., Prange and Scherer [2009](https://arxiv.org/html/2602.08039v1#bib.bib33 "Correlation smile matching for collateralized debt obligation tranches with α-stable distributions and fitted Archimedean copula models") and Hofert [2010](https://arxiv.org/html/2602.08039v1#bib.bib18 "Sampling nested Archimedean copulas with applications to CDO pricing")), and other advanced models based on the normal inverse Gaussian (NIG) or α\alpha-stable distributions (e.g., Kalemanova et al. [2007](https://arxiv.org/html/2602.08039v1#bib.bib21 "The normal inverse Gaussian distribution for synthetic CDO pricing") and Prange and Scherer [2009](https://arxiv.org/html/2602.08039v1#bib.bib33 "Correlation smile matching for collateralized debt obligation tranches with α-stable distributions and fitted Archimedean copula models")). While these parametric models offer greater flexibility, the related research indicates that these models also fail to achieve a perfect fit across all tranches.

Second, due to the general inadequacy of standard parametric models to achieve a perfect fit, a common approach when calibrating them to market prices across all tranches is to minimize some calibration error metrics. Given that closed-form pricing formulas for CDO tranches are typically unavailable, this approach usually entails solving simulation-based optimization problems, which are computationally intensive as many key quantities involved in the numerical optimization have to be computed via simulation.

Third, and most importantly, to the best of our knowledge, the literature lacks a general formal theory to determine when a perfect-fit model exists and, if it exists, how to construct it. A pioneering study in identifying a perfect-fit model across all tranches is Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")). Nonetheless, it seems that their attention is confined to a relatively narrow class of models with specific assumptions; they assume that default times are independent conditional on a random hazard rate that can take one of a finite number of states, and then calibrate the probabilities of these states to achieve a perfect fit.

The celebrated work of Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")) motivates us to consider general models with minimal assumptions for achieving a perfect fit and to establish a general formal theory concerning the existence and construction of a general perfect-fit model. Moreover, it will be desirable to develop efficient algorithms to verify the existence of a general perfect-fit model and, if it exists, to construct such a model, without resorting to computationally intensive simulation-based optimization.

### 1.2 Our Contributions

In this paper, we propose a theoretical framework to examine when a general perfect-fit model exists and, if it exists, how to construct it. Our study focuses on the existence and construction of general “perfect-fit” copula functions. This is without loss of generality because, according to Sklar’s theorem (Cherubini et al. [2004](https://arxiv.org/html/2602.08039v1#bib.bib62 "Copula methods in finance")), any probabilistic model for CDOs, including structural models of asset values (e.g., Kijima et al. [2010](https://arxiv.org/html/2602.08039v1#bib.bib32 "Pricing of CDOs based on the multivariate Wang transform"), Collin-Dufresne et al. [2012](https://arxiv.org/html/2602.08039v1#bib.bib73 "On the relative pricing of long-maturity index options and collateralized debt obligations"), and Seo and Wachter [2018](https://arxiv.org/html/2602.08039v1#bib.bib68 "Do rare events explain CDX tranche spreads?")) and reduced-form models of default intensities (e.g., Peng and Kou [2008](https://arxiv.org/html/2602.08039v1#bib.bib4 "Connecting the top-down to the bottom-up: pricing CDO under a conditional survival (CS) model") and Frey and Schmidt [2012](https://arxiv.org/html/2602.08039v1#bib.bib76 "Pricing and hedging of credit derivatives via the innovations approach to nonlinear filtering")), implies a joint distribution of default times and, in turn, a corresponding copula function.

Specifically, we first introduce a new concept—weak compatibility—as the most natural and comprehensive characterization of the consistency of CDO market prices across all tranches. CDO market prices across all tranches on the same underlying portfolio are said to be weakly compatible if there exists any copula (equivalent to the existence of any probabilistic model) that can perfectly fit them. Notably, weak compatibility represents the minimal requirement for the theoretical consistency of market prices, as it guarantees the existence of a unified pricing measure (i.e., an equivalent martingale measure), thus ensuring the absence of arbitrage in the market. Furthermore, it enables consistent pricing of nonstandard credit derivatives on the same portfolio, such as CDOs with nonstandard attachment and detachment points.

While weak compatibility addresses the minimal requirement for the theoretical consistency of market prices, practical applications often demand more structure. For instance, a general copula that meets weak compatibility may have a complex functional form, making it difficult to apply to solving certain practically important problems, such as the efficient pricing of CDOs with a nonstandard number of underlying names and the computation of credit portfolios’ loss distributions for risk management. To address these practical needs, we introduce another new concept: strong compatibility; CDO market prices across all tranches on the same underlying portfolio are said to be strongly compatible if there exists a copula from the class of conditionally independent and identically distributed (i.i.d.) models that can perfectly fit them. Beyond enabling solutions to the aforementioned practical problems, strong compatibility is also well-motivated by the fact that both structural and reduced-form credit models, when applied under a homogeneity assumption, implicitly rely on a conditionally i.i.d. structure.

Indeed, it is straightforward to see that strong compatibility implies weak compatibility. Furthermore, failure to be weak compatibility essentially implies “incompatibility”, meaning that there exists no copula that perfectly fits the CDO market prices across all tranches and thus underscoring the fact that weak compatibility represents the minimal requirement for the theoretical consistency of market prices.
See Figure [1](https://arxiv.org/html/2602.08039v1#S1.F1 "Figure 1 ‣ 1.2 Our Contributions ‣ 1 Introduction") for their relationship.

Figure 1: Categorization of CDO Market Prices Across All Tranches Based on Their Compatibility

![Refer to caption](x1.png)

*Notes.* This figure illustrates the categorization of CDO market prices across all tranches on the same underlying portfolio based on their compatibility: (i) incompatible (grey), (ii) weakly compatible (blue), and (iii) strongly compatible (green). Indeed, “strongly compatible” implies “weakly compatible”. Furthermore, failure to be “weakly compatible” implies “incompatible”, underscoring the fact that “weakly compatible” represents the minimal requirement for the theoretical consistency of market prices.

For both weak compatibility and strong compatibility, we derive a sufficient and necessary condition by establishing a relationship between each concept and a linear programming (LP) problem. Specifically, for weak compatibility, we propose a DPM-based approach to reduce its verification to an LP problem, where the DPM, abbreviated from the “default probability matrix”, summarizes information about the default count distribution at a finite number of prespecified time points. For strong compatibility, a novel and flexible family of copulas termed “gamma-distorted copulas” is introduced to establish the sufficient and necessary condition. Furthermore, for each, when the established sufficient and necessary condition holds, we demonstrate how to construct a corresponding concrete copula model that achieves a perfect fit. Our framework not only enables the efficient verification of weak compatibility and strong compatibility through LP problems but also facilitates the construction of the corresponding concrete copula models, eliminating the need for computationally intensive simulation-based optimization.

In summary, the main contributions of our paper are threefold.

1. ∙\bullet

   We establish a formal theoretical framework to address two questions: when a general copula model exists that can perfectly fit CDO market prices across all tranches, and if it exists, how to construct such a perfect-fit copula model. To this end, we put forward two new concepts—weak compatibility and strong compatibility—to fill the literature gap, which respectively address the existence of a general copula model and a general conditionally i.i.d. copula model that can achieve a perfect fit.
2. ∙\bullet

   For both weak compatibility and strong compatibility, we derive a sufficient and necessary condition by reducing its verification to an LP problem. In addition, for each, when the associated condition holds, we demonstrate how to construct a corresponding concrete perfect-fit copula model. Both the verification and construction processes are efficient because the related LP problems can be readily solved numerically, without resorting to computationally intensive simulation-based optimization.
3. ∙\bullet

   We apply weak compatibility and strong compatibility to several important practical applications. Specifically,
   the former is employed to construct effective model-independent hedging strategies for credit portfolios and to price CDOs with nonstandard attachment and detachment points, while the latter is used to compute the loss distributions of credit portfolios and to price CDOs with a nonstandard number of underlying names. See Table [1](https://arxiv.org/html/2602.08039v1#S1.T1 "Table 1 ‣ 1.2 Our Contributions ‣ 1 Introduction") for a summary of these applications.

Table 1: Applications of Weak Compatibility and Strong Compatibility

|  |  |  |
| --- | --- | --- |
|  | Weak Compatibility | Strong Compatibility |
| Pricing nonstandard credit derivatives | Pricing CDOs with nonstandard attachment and detachment points | Pricing CDOs with a nonstandard number of underlying names |
| Conducting risk management | Constructing model-independent hedging strategies for credit portfolios | Estimating the loss distributions of credit portfolios |

### 1.3 Comparison with Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach"))

The work by Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")) stands as a seminal contribution, marking the first explicit emphasis on the criticality of achieving a perfect fit to CDO market prices across all tranches. Their “implied copula” method offers an influential demonstration of how such calibration might be practically accomplished, and their work serves as a core motivation for our research. Our paper builds on the “perfect fit” objective they lay out and establishes a formal theoretical foundation for this problem. Specifically, our theoretical framework extends their analysis along three key dimensions.

First, our theoretical framework is substantially more general.
The implied copula method of Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")) relies on a specific functional form derived from the assumption that default times are independent conditional on a random hazard rate that can take one of a finite number of states. In contrast, our weak compatibility framework adopts the most general perspective, considering the set of all valid copulas without imposing any a priori structural assumptions.
This generality enables us to establish the model-independent conditions for price consistency. Furthermore, even our strong compatibility framework remains highly general, encompassing all conditionally i.i.d. copula models—with the model considered in Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")) included as a special case.

Second, our theoretical framework is developed for the general multi-period setting inherent in standard CDO contracts. While the implied copula method of Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")) values cash flows across multiple periods, its dependence structure is effectively static.
In their model, the default count distributions at all time points are governed by a single set of calibrated state probabilities, which implies that if the default distribution for any single date is known, the distributions for all other dates are automatically determined.
By contrast, our strong compatibility framework provides the necessary degrees of freedom to characterize the conditions for a perfect fit in a truly multi-period setting.
Therefore, our strong compatibility framework can be viewed not only as an extension of Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")) to the general class of conditionally i.i.d. copulas but also as a multi-period extension of the modeling approach in Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")).

Third, and most importantly,
we establish the formal theoretical conditions for the existence of a perfect-fit model, or more precisely, for the existence of a general copula model capable of achieving a perfect fit.
The constructive method of Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")) successfully achieved a perfect fit to their dataset and has proven effective in many practical market scenarios (Brigo et al. [2010](https://arxiv.org/html/2602.08039v1#bib.bib64 "Credit models and the crisis: a journey into cdos, copulas, correlations and dynamic models")).
However, since they consider only a relatively narrow class of models, their method offers no guarantees of the existence of a perfect-fit model. Furthermore, they do not delineate the general conditions under which a perfect-fit model exists. Our paper addresses this theoretical gap by deriving the sufficient and necessary conditions for both weak compatibility and strong compatibility. In doing so, we answer the fundamental question of when a perfect-fit model is possible, a question that precedes the task of determining how to construct it.

The remainder of our paper is organized as follows.
Section [2](https://arxiv.org/html/2602.08039v1#S2 "2 Definitions of Weak Compatibility and Strong Compatibility") formally defines weak compatibility and strong compatibility.
Sections [3](https://arxiv.org/html/2602.08039v1#S3 "3 Weak Compatibility") and [4](https://arxiv.org/html/2602.08039v1#S4 "4 Strong Compatibility") present the main results for weak compatibility and strong compatibility, respectively, whereas Section [5](https://arxiv.org/html/2602.08039v1#S5 "5 Applications of Weak Compatibility and Strong Compatibility") discusses their various applications.
Empirical results are reported in Section [6](https://arxiv.org/html/2602.08039v1#S6 "6 Empirical Studies"). All the proofs and some auxiliary results are deferred to the e-companion.

## 2 Definitions of Weak Compatibility and Strong Compatibility

### 2.1 Valuation Framework for CDO Tranches

Before introducing the new concepts of weak compatibility and strong compatibility, we first outline the valuation framework for CDO tranches as preliminary groundwork. Consider a CDO that references a portfolio of nn underlying assets or names. For j=1,2,…,nj=1,2,\ldots,n, let τj\tau\_{j} denote the default time of the jj-th asset.
According to Sklar’s theorem (Cherubini et al. [2004](https://arxiv.org/html/2602.08039v1#bib.bib62 "Copula methods in finance")), the joint distribution function Fjoint​(t1,…,tn)F\_{\mathrm{joint}}(t\_{1},\ldots,t\_{n}) of τ1,…,τn\tau\_{1},\ldots,\tau\_{n} can be decomposed into their respective marginal distribution functions F1​(⋅),…,Fn​(⋅)F\_{1}(\cdot),\ldots,F\_{n}(\cdot) and a copula function CC that describes the dependence structure:

|  |  |  |
| --- | --- | --- |
|  | Fjoint​(t1,…,tn)=C​(F1​(t1),…,Fn​(tn))for tj≥0 with j=1,⋯,n.F\_{\mathrm{joint}}(t\_{1},\ldots,t\_{n})=C(F\_{1}(t\_{1}),\ldots,F\_{n}(t\_{n}))\quad\text{for $t\_{j}\geq 0$ with $j=1,\cdots,n$}. |  |

For simplicity, we assume a constant recovery rate RjR\_{j} for the jj-th name in this standard framework.
Then the cumulative loss process of the portfolio up to time tt is given by

|  |  |  |
| --- | --- | --- |
|  | Lt=∑j=1n(1−Rj)​Aj​𝟏{τj≤t}for t≥0,L\_{t}=\sum\_{j=1}^{n}(1-R\_{j})A\_{j}\mathbf{1}\_{\{\tau\_{j}\leq t\}}\quad\text{for $t\geq 0$,} |  |

where AjA\_{j} denotes the notional amount of the jj-th reference entity and 𝟏B\mathbf{1}\_{B} (for any event BB) represents an indicator function that equals 11 if BB occurs and 0 otherwise.

Let 0<T1<⋯<Tm=T0<T\_{1}<\cdots<T\_{m}=T denote the predefined payment dates of the CDO contract, with T0:=0T\_{0}:=0 and TT representing the contract’s maturity.
Given that its cash flows are unaffected by any defaults occurring beyond maturity TT, we assume,
for mathematical completeness and notational convenience, the existence of a subsequent time point Tm+1>TT\_{m+1}>T, by which all assets in the portfolio are certain to have defaulted.
Then it holds that Fj​(Tm+1)=1F\_{j}(T\_{m+1})=1 for all j=1,…,nj=1,\ldots,n.

The CDO structure partitions the total portfolio loss into MM tranches, each characterized by an attachment point ala\_{l} and a detachment point blb\_{l} (0≤al<bl≤10\leq a\_{l}<b\_{l}\leq 1).
These tranches are denoted by [al,bl][a\_{l},b\_{l}] for l=1,…,Ml=1,\ldots,M.
The loss allocated to tranche [al,bl][a\_{l},b\_{l}] up to time tt, denoted by Lt[al,bl]L\_{t}^{[a\_{l},b\_{l}]}, is the portion of the total portfolio loss LtL\_{t} that falls within this tranche:

|  |  |  |
| --- | --- | --- |
|  | Lt[al,bl]=(Lt−al)+−(Lt−bl)+for l=1,…,M,L\_{t}^{[a\_{l},b\_{l}]}={(L\_{t}-a\_{l})}^{+}-{(L\_{t}-b\_{l})}^{+}\quad\text{for $l=1,\ldots,M$}, |  |

where (x)+:=max⁡(x,0){(x)}^{+}:=\max(x,0) for any x∈ℝx\in\mathbb{R}.

The value of a CDO tranche derives from the net cash flows between the protection buyer and seller.
These cash flows comprise two legs: the premium leg (payments from the buyer to the seller) and the default leg (payments from the seller to the buyer).

Specifically, the discounted value of the premium leg for tranche [al,bl][a\_{l},b\_{l}] can be expressed as the sum of any up-front payment and the discounted value of the running spread payments on the outstanding tranche notional:

|  |  |  |
| --- | --- | --- |
|  | PreLeg[al,bl]=uf[al,bl]​(bl−al)+s[al,bl]​∑i=1m[D​(Ti)​(Ti−Ti−1)​(bl−al−LTi[al,bl])]for l=1,…,M,{\rm PreLeg}^{[a\_{l},b\_{l}]}=\text{uf}^{[a\_{l},b\_{l}]}(b\_{l}-a\_{l})+s^{[a\_{l},b\_{l}]}\sum\_{i=1}^{m}\left[D(T\_{i})(T\_{i}-T\_{i-1})(b\_{l}-a\_{l}-L^{[a\_{l},b\_{l}]}\_{T\_{i}})\right]\quad\text{for $l=1,\ldots,M$}, |  |

where uf[al,bl]\text{uf}^{[a\_{l},b\_{l}]} and s[al,bl]s^{[a\_{l},b\_{l}]} denote the up-front payment and the running spread for tranche [al,bl][a\_{l},b\_{l}], respectively, and D​(⋅)D(\cdot) represents the risk-free discount function.
Market conventions dictate how these parameters are quoted.
The equity and junior tranches are typically quoted via up-front payments (with uf[al,bl]\text{uf}^{[a\_{l},b\_{l}]} as the market variable and s[al,bl]s^{[a\_{l},b\_{l}]} as a fixed running spread), while other tranches are quoted by their running spread (with s[al,bl]s^{[a\_{l},b\_{l}]} as the market variable and uf[al,bl]\text{uf}^{[a\_{l},b\_{l}]} as 0).
See Table [2](https://arxiv.org/html/2602.08039v1#S6.T2 "Table 2 ‣ 6.1.1 Data ‣ 6.1 Data and Verification of Compatibility ‣ 6 Empirical Studies") in Section [6](https://arxiv.org/html/2602.08039v1#S6 "6 Empirical Studies") for an example of market quotes.

The discounted value of the default leg for tranche [al,bl][a\_{l},b\_{l}] represents the present value of payments made by the protection seller to cover realized losses on that tranche:

|  |  |  |
| --- | --- | --- |
|  | DefLeg[al,bl]=∫0TD​(t)​𝑑Lt[al,bl]for l=1,…,M.{\rm DefLeg}^{[a\_{l},b\_{l}]}=\int\_{0}^{T}D(t)dL\_{t}^{[a\_{l},b\_{l}]}\quad\text{for $l=1,\ldots,M$}. |  |

For computational purposes, it is common in the literature to assume that defaults (and thus the incremental losses d​Lt[al,bl]dL\_{t}^{[a\_{l},b\_{l}]}) occur only at discrete time points, specifically the midpoints of the mm coupon payment periods [T0,T1],…,[Tm−1,Tm][T\_{0},T\_{1}],\ldots,[T\_{m-1},T\_{m}] (see, e.g., Peng and Kou [2008](https://arxiv.org/html/2602.08039v1#bib.bib4 "Connecting the top-down to the bottom-up: pricing CDO under a conditional survival (CS) model") and Papageorgiou and Sircar [2009](https://arxiv.org/html/2602.08039v1#bib.bib5 "Multiscale intensity models and name grouping for valuation of multi-name credit derivatives")).
Under this midpoint timing assumption, we can obtain

|  |  |  |
| --- | --- | --- |
|  | DefLeg[al,bl]=∑i=1mD​(Ti−1+Ti2)​(LTi[al,bl]−LTi−1[al,bl])for l=1,…,M.{\rm DefLeg}^{[a\_{l},b\_{l}]}=\sum\_{i=1}^{m}D\left(\frac{T\_{i-1}+T\_{i}}{2}\right)(L\_{T\_{i}}^{[a\_{l},b\_{l}]}-L\_{T\_{i-1}}^{[a\_{l},b\_{l}]})\quad\text{for $l=1,\ldots,M$}. |  |

Consider a long protection position in tranche [al,bl][a\_{l},b\_{l}]. Its net present value (NPV) V[al,bl]V^{[a\_{l},b\_{l}]} is then given by the value received (default leg) minus the value paid (premium leg):

|  |  |  |  |
| --- | --- | --- | --- |
|  | V[al,bl]=DefLeg[al,bl]−PreLeg[al,bl]for l=1,…,M.V^{[a\_{l},b\_{l}]}={\rm DefLeg}^{[a\_{l},b\_{l}]}-{\rm PreLeg}^{[a\_{l},b\_{l}]}\quad\text{for $l=1,\ldots,M$}. |  | (1) |

For pricing and calibration purposes, we are interested in the expected NPVs

|  |  |  |
| --- | --- | --- |
|  | v[al,bl]:=𝔼​[V[al,bl]]for l=1,…,Mv^{[a\_{l},b\_{l}]}:=\mathbb{E}[V^{[a\_{l},b\_{l}]}]\quad\text{for $l=1,\ldots,M$} |  |

under a risk-neutral measure.
If we assume that the observed market prices (the running spreads s[al,bl]s^{[a\_{l},b\_{l}]} and the up-front payments uf[al,bl]\text{uf}^{[a\_{l},b\_{l}]}) are fair, then the theoretical expected NPV v[al,bl]v^{[a\_{l},b\_{l}]} calculated using these market quotes should be zero for all traded tranches, i.e., v[al,bl]=0v^{[a\_{l},b\_{l}]}=0 for l=1,…,Ml=1,\ldots,M.

### 2.2 Definitions of Weak Compatibility and Strong Compatibility

The valuation process of CDO tranches requires several inputs. The marginal default distributions F1​(⋅),…,Fn​(⋅)F\_{1}(\cdot),\ldots,F\_{n}(\cdot) can typically be derived from the market prices of CDS for the individual names in the portfolio.
The risk-free discount function D​(⋅)D(\cdot) can be obtained from market interest rate curves.
Given these market-implied inputs, the expected NPV v[al,bl]v^{[a\_{l},b\_{l}]} of a tranche depends on two key components: the dependence structure of the underlying assets, described by the copula CC, and the market quotes for the tranches, 𝐬=(s[a1,b1],uf[a1,b1],…,s[aM,bM],uf[aM,bM])\mathbf{s}=(s^{[a\_{1},b\_{1}]},\textrm{uf}^{[a\_{1},b\_{1}]},\ldots,s^{[a\_{M},b\_{M}]},\textrm{uf}^{[a\_{M},b\_{M}]}). We can thus explicitly express the expected NPV as v[al,bl]​(C;𝐬)v^{[a\_{l},b\_{l}]}(C;\mathbf{s}) for l=1,…,Ml=1,\ldots,M.

Accordingly, calibrating a CDO model capable of perfectly fitting market prices across all tranches (i.e., identifying a copula CC (from a chosen family) whose model-implied fair prices replicate the observed market prices) is equivalent to identifying a copula CC (from a chosen family) that simultaneously satisfies the fair value condition for all market-quoted tranches:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v[al,bl]​(C;𝐬)=0for l=1,…,M.\displaystyle v^{[a\_{l},b\_{l}]}(C;\mathbf{s})=0\quad\text{for $l=1,\ldots,M$}. |  | (2) |

Building on this idea, we formally define compatibility of market prices across all tranches with respect to a specified family of copulas.

###### Definition 2.1

(Compatibility of Market Prices Across All Tranches With Respect to a Specified Family of Copulas 𝒞\mathcal{C})
Consider an MM-tranche CDO with a known discount function D​(⋅)D(\cdot), recovery rates R1,…,RnR\_{1},\ldots,R\_{n}, and marginal distributions F1​(⋅),…,Fn​(⋅)F\_{1}(\cdot),\ldots,F\_{n}(\cdot) (typically derived from market data). Let 𝒞\mathcal{C} denote a specified family of nn-dimensional copulas.
The observed market prices 𝐬=(s[a1,b1],uf[a1,b1],…,s[aM,bM],uf[aM,bM])\mathbf{s}=(s^{[a\_{1},b\_{1}]},\textrm{uf}^{[a\_{1},b\_{1}]},\ldots,s^{[a\_{M},b\_{M}]},\textrm{uf}^{[a\_{M},b\_{M}]}) across all MM tranches is said to be compatible with respect to 𝒞\mathcal{C} if there exists a copula C∈𝒞C\in\mathcal{C} such that ([2](https://arxiv.org/html/2602.08039v1#S2.E2 "In 2.2 Definitions of Weak Compatibility and Strong Compatibility ‣ 2 Definitions of Weak Compatibility and Strong Compatibility")) holds.
In this case, we also say that the copula CC achieves a perfect fit to market prices across all tranches.

Consider two important general families of copulas, and then we can define two levels of compatibilities: weak compatibility and strong compatibility.

###### Definition 2.2

(Weak Compatibility of Market Prices Across All Tranches)
Consider the general family 𝒞0\mathcal{C}\_{0} of copulas, which includes all nn-dimensional copulas. Compatibility with respect to 𝒞0\mathcal{C}\_{0} is termed weak compatibility.

###### Definition 2.3

(Strong Compatibility of Market Prices Across All Tranches)
Consider the general family 𝒞1\mathcal{C}\_{1} of copulas, which includes all nn-dimensional, conditionally i.i.d. copulas. Compatibility with respect to 𝒞1\mathcal{C}\_{1} is termed strong compatibility.

Since 𝒞1\mathcal{C}\_{1} is a subset of 𝒞0\mathcal{C}\_{0}, strong compatibility implies weak compatibility. Indeed, weak compatibility confirms the existence of at least one general probabilistic model whose model-implied fair prices can replicate the market prices. In contrast, strong compatibility imposes a stricter requirement: such a model must belong to the class of conditionally i.i.d. models.

Notably, weak compatibility represents the minimal requirement for the theoretical consistency of market prices. If market prices satisfy weak compatibility, there exists at least one general copula C∈𝒞0C\in\mathcal{C}\_{0} that can achieve a perfect fit to market prices across all tranches and hence can simultaneously justify all observed tranche prices. Furthermore, weak compatibility implies the absence of arbitrage opportunities among the CDO tranches. In addition, weak compatibility also enables the theoretically consistent pricing of nonstandard credit derivatives tied to the same portfolio, such as CDOs with nonstandard attachment and detachment points. Conversely, a failure to satisfy weak compatibility indicates that no single probabilistic model can rationalize the market prices across all tranches, pointing to a potential market anomaly.

In contrast, strong compatibility necessitates achieving a perfect fit to market prices across all tranches using a conditionally i.i.d. model. This requirement is also well-motivated for two key reasons. First, standard credit models, including both structural and reduced-form ones, implicitly rely on such a “conditionally i.i.d.” structure when applying the homogeneity assumption. Indeed, the dependence structure of these standard models is characterized by a set of common risk factors, and conditional on these factors, the individual default times become independent of one another. Second, this “conditionally i.i.d.” structure offers two critical advantages. (i) It enables the calibrated distribution of the common risk factors to be consistently applied in pricing nonstandard credit derivatives tied to a portfolio of difference size, such as CDOs with a nonstandard number of underlying names; (ii) It is particularly well-suited for CDO portfolio risk management, as it simplifies the estimation of loss distributions through a two-step simulation process: first, a path for the common risk factors is simulated, and then, conditional on the path, the individual defaults can be efficiently simulated as independent events.

###### Remark 2.1

(Comparison with Traditional Calibration Methods of Parametric Copula Models) Traditional research in the CDO literature usually first specifies a particular family of parametric copula models (e.g., Gaussian copulas or Archimedean copulas) and then derives the model-implied market quotes as functions of the model parameters using ([2](https://arxiv.org/html/2602.08039v1#S2.E2 "In 2.2 Definitions of Weak Compatibility and Strong Compatibility ‣ 2 Definitions of Weak Compatibility and Strong Compatibility")).
It is noteworthy that the use of ([2](https://arxiv.org/html/2602.08039v1#S2.E2 "In 2.2 Definitions of Weak Compatibility and Strong Compatibility ‣ 2 Definitions of Weak Compatibility and Strong Compatibility")) here is indirect: while the market quotes referenced in ([2](https://arxiv.org/html/2602.08039v1#S2.E2 "In 2.2 Definitions of Weak Compatibility and Strong Compatibility ‣ 2 Definitions of Weak Compatibility and Strong Compatibility")) are assumed to be actual market observations, they utilize ([2](https://arxiv.org/html/2602.08039v1#S2.E2 "In 2.2 Definitions of Weak Compatibility and Strong Compatibility ‣ 2 Definitions of Weak Compatibility and Strong Compatibility")) to obtain model-implied market quotes 𝐬model\mathbf{s}\_{\mathrm{model}} satisfying v[al,bl]​(C;𝐬model)=0v^{[a\_{l},b\_{l}]}(C;\mathbf{s}\_{\mathrm{model}})=0 for l=1​…,Ml=1\ldots,M.
Finally, the calibration is completed by minimizing a distance metric between the model-implied market quotes 𝐬model\mathbf{s}\_{\mathrm{model}} and the observed market quotes 𝐬\mathbf{s}.
This approach is traditionally adopted in the literature primarily because specific families of parametric copula models are relatively restrictive, and as such, they generally fail to provide a perfect fit.
Furthermore, given that the model-implied market quotes typically lack closed-form expressions and need to be computed via simulation, this approach involves solving a simulation-based optimization problem, which is computationally intensive.

Motivated by Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")), instead of deriving the model-implied market quotes as functions of the model parameters using ([2](https://arxiv.org/html/2602.08039v1#S2.E2 "In 2.2 Definitions of Weak Compatibility and Strong Compatibility ‣ 2 Definitions of Weak Compatibility and Strong Compatibility")) and then minimizing the calibration error, we consider a general class of copula models and then directly identify a copula CC that solves ([2](https://arxiv.org/html/2602.08039v1#S2.E2 "In 2.2 Definitions of Weak Compatibility and Strong Compatibility ‣ 2 Definitions of Weak Compatibility and Strong Compatibility")) exactly, where the market quotes are observed in the market. It turns out that for the two important general classes of copula models 𝒞0\mathcal{C}\_{0} and 𝒞1\mathcal{C}\_{1}, our proposed method offers not only greater mathematical convenience but also higher computational efficiency without resorting to simulation-based optimization techniques, as will be detailed in the subsequent sections.

## 3 Weak Compatibility

In this section, we aim to derive a sufficient and necessary condition for weak compatibility by establishing a connection between it and a linear programming (LP) problem through the introduction of a new concept—the default probability matrix for the underlying portfolio of a CDO. If weak compatibility is satisfied, we demonstrate how to construct a corresponding concrete copula C∈𝒞0C\in\mathcal{C}\_{0} that achieves a perfect fit.

### 3.1 The Default Probability Matrix (DPM)

We begin by introducing the DPM for the underlying portfolio of a CDO. This matrix can be used to rephrase the key Eqs. ([2](https://arxiv.org/html/2602.08039v1#S2.E2 "In 2.2 Definitions of Weak Compatibility and Strong Compatibility ‣ 2 Definitions of Weak Compatibility and Strong Compatibility")), thereby transforming the problem of identifying a copula C∈𝒞0C\in\mathcal{C}\_{0} into that of determining the corresponding DPM.

Let Nt:=∑j=1n𝟏{τj≤t}N\_{t}:=\sum\_{j=1}^{n}\mathbf{1}\_{\{\tau\_{j}\leq t\}} denote the default count (i.e., the number of defaults) by time tt. The distributions of default counts at the predefined payment dates T1,…,TmT\_{1},\ldots,T\_{m} can be summarized by the DPM Q={qi​j}1≤i≤m,0≤j≤nQ=\{q\_{ij}\}\_{1\leq i\leq m,0\leq j\leq n}, whose elements are defined as

|  |  |  |
| --- | --- | --- |
|  | qi​j:=ℙ​(NTi=j)for 1≤i≤m and 0≤j≤n.q\_{ij}:=\mathbb{P}(N\_{T\_{i}}=j)\quad\text{for $1\leq i\leq m$ and $0\leq j\leq n$}. |  |

Given the known marginal distribution Fj​(⋅)F\_{j}(\cdot) for each default time τj\tau\_{j}, the DPM QQ is then determined by the copula CC of the default times τ1,…,τn\tau\_{1},\ldots,\tau\_{n}.
For any subset S⊆{1,…,n}S\subseteq\{1,\ldots,n\}, let CSC\_{S} denote the SS-marginal copula function of CC (i.e., the joint distribution function of the uniform random variables Uk:=Fk​(τk)U\_{k}:=F\_{k}(\tau\_{k}) for k∈Sk\in S).
Using the inclusion-exclusion principle, each element
qi​jq\_{ij} of QQ can be derived as follows in a straightforward way.

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi​j=∑S⊆{1,…,n}|S|≥j(−1)|S|−j​(|S|j)​CS​(Fk​(Ti);k∈S).q\_{ij}=\sum\_{\begin{subarray}{c}S\subseteq\{1,\ldots,n\}\\ |S|\geq j\end{subarray}}{(-1)}^{|S|-j}\binom{|S|}{j}C\_{S}(F\_{k}(T\_{i});k\in S). |  | (3) |

This formula explicitly illustrates how the joint default probabilities (captured by the copula CC and the marginal distributions Fk​(⋅)F\_{k}(\cdot)) determine the probabilities qi​jq\_{ij} for 1≤i≤m1\leq i\leq m and 0≤j≤n0\leq j\leq n.

The following proposition establishes a sufficient and necessary condition for a matrix Q^∈ℝm×(n+1)\hat{Q}\in{\mathbb{R}^{m\times(n+1)}} to qualify as a DPM corresponding to some distribution of default times.

###### Proposition 3.1

For 0=T0<T1<⋯<Tm=T0=T\_{0}<T\_{1}<\cdots<T\_{m}=T and a matrix Q^={q^i​j}1≤i≤m,0≤j≤n∈ℝm×(n+1)\hat{Q}={\{\hat{q}\_{ij}\}}\_{1\leq i\leq m,0\leq j\leq n}\in{\mathbb{R}^{m\times(n+1)}}, the following three statements are equivalent.

1. (i)

   The matrix Q^\hat{Q} is a DPM, that is, there exist non-negative random variables τ^j\hat{\tau}\_{j} (for 1≤j≤n1\leq j\leq n) such that ℙ​(N^Ti=j)=q^i​j\mathbb{P}(\hat{N}\_{T\_{i}}=j)=\hat{q}\_{ij}, where N^t:=∑j=1n𝟏{τ^j≤t}\hat{N}\_{t}:=\sum\_{j=1}^{n}\mathbf{1}\_{\{\hat{\tau}\_{j}\leq t\}}.
2. (ii)

   The matrix Q^\hat{Q} is a DPM for exchangeable default times, that is, there exist non-negative exchangeable random variables τ^j\hat{\tau}\_{j} (for 1≤j≤n1\leq j\leq n) such that ℙ​(N^Ti=j)=q^i​j\mathbb{P}(\hat{N}\_{T\_{i}}=j)=\hat{q}\_{ij}, where N^t:=∑j=1n𝟏{τ^j≤t}\hat{N}\_{t}:=\sum\_{j=1}^{n}\mathbf{1}\_{\{\hat{\tau}\_{j}\leq t\}}.
3. (iii)

   The matrix Q^={q^i​j}1≤i≤m,0≤j≤n\hat{Q}={\{\hat{q}\_{ij}\}}\_{1\leq i\leq m,0\leq j\leq n} satisfies the following linear constraints:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | {∑j=0nq^i​j=1for​ 1≤i≤m,∑k≥jq^i​k≤∑k≥jq^i+1,kfor1≤i≤m−1​and​ 0≤j≤n,q^i​j≥0for​ 1≤i≤m​and​ 0≤j≤n.\left\{\begin{array}[]{ll}\sum\_{j=0}^{n}\hat{q}\_{ij}=1&\quad{\rm for}\,1\leq i\leq m,\\ \sum\_{k\geq j}\hat{q}\_{ik}\leq\sum\_{k\geq j}\hat{q}\_{i+1,k}&\quad{\rm for}1\leq i\leq m-1\,{\rm and}\,0\leq j\leq n,\\ \hat{q}\_{ij}\geq 0&\quad{\rm for}\,1\leq i\leq m\,{\rm and}\,0\leq j\leq n.\\ \end{array}\right. |  | (4) |

Proof. See Section [8](https://arxiv.org/html/2602.08039v1#S8 "8 Proofs of Propositions 3.1 and 3.2") in the e-companion. □\Box

###### Remark 3.1

The equivalence of (i) and (ii) in Proposition [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmProposition1 "Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility") implies that for any credit portfolio with default times τ1,…,τn\tau\_{1},\ldots,\tau\_{n}, one can construct an equivalent portfolio with “exchangeable” default times τ1′,…,τn′\tau\_{1}^{\prime},\ldots,\tau\_{n}^{\prime} that share the same DPM as the original one. Consequently, if the valuation of a credit derivative depends only on the default counts, one may assume that the distribution of τ1,…,τn\tau\_{1},\ldots,\tau\_{n} is exchangeable. This finding justifies the commonly used assumption in the literature (e.g., Burtschell et al. [2009](https://arxiv.org/html/2602.08039v1#bib.bib11 "A comparative analysis of CDO pricing models under the factor copula framework") and Collin-Dufresne et al. [2024](https://arxiv.org/html/2602.08039v1#bib.bib72 "How integrated are credit and equity markets? evidence from index options"))
that all assets in a portfolio share identical marginal distributions of default times and pairwise correlations.

###### Remark 3.2

(iii) in Proposition [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmProposition1 "Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility") provides a sufficient and necessary condition for a matrix Q^\hat{Q} to qualify as a valid DPM. This condition is intuitively necessary: first, the probabilities sum to one; second, cumulative default counts are non-decreasing over time. Interestingly, Proposition [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmProposition1 "Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility") establishes that this intuitively necessary condition also proves sufficient.

### 3.2 Expressing the Expected NPVs v[al,bl]​(C;𝐬)v^{[a\_{l},b\_{l}]}(C;\mathbf{s}) of Tranches in Terms of the DPM

This subsection focuses on expressing the expected NPVs v[al,bl]​(C;𝐬)v^{[a\_{l},b\_{l}]}(C;\mathbf{s}) (for 1≤l≤M1\leq l\leq M) of tranches in terms of the DPM. This, in turn, allows us to rephrase the key Eqs. ([2](https://arxiv.org/html/2602.08039v1#S2.E2 "In 2.2 Definitions of Weak Compatibility and Strong Compatibility ‣ 2 Definitions of Weak Compatibility and Strong Compatibility")) using the DPM.

In the remainder of this paper, we adopt two common assumptions from the literature (e.g., Wang et al. [2009](https://arxiv.org/html/2602.08039v1#bib.bib58 "Pricing tranches of a CDO and a CDS index: recent advances and future research"), Burtschell et al. [2009](https://arxiv.org/html/2602.08039v1#bib.bib11 "A comparative analysis of CDO pricing models under the factor copula framework"), Collin-Dufresne et al. [2012](https://arxiv.org/html/2602.08039v1#bib.bib73 "On the relative pricing of long-maturity index options and collateralized debt obligations"), and Seo and Wachter [2018](https://arxiv.org/html/2602.08039v1#bib.bib68 "Do rare events explain CDX tranche spreads?")). First, the notional amounts and recovery rates of all the names in the portfolio are the same, i.e., Aj=A=1nA\_{j}=A=\frac{1}{n} and Rj=RR\_{j}=R for all 1≤j≤n1\leq j\leq n. Second, all the marginal distributions of default times are identical, i.e., Fj​(⋅)=F​(⋅)F\_{j}(\cdot)=F(\cdot) for all 1≤j≤n1\leq j\leq n, which can be justified by Proposition [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmProposition1 "Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility") (see Remark [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmRemark1 "Remark 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility")).

###### Proposition 3.2

(Expressing the Expected NPVs v[al,bl]​(C;𝐬)v^{[a\_{l},b\_{l}]}(C;\mathbf{s}) of Tranches in Terms of the DPM)
 Given the market prices of CDO tranches 𝐬=(s[a1,b1],uf[a1,b1],…,\mathbf{s}=(s^{[a\_{1},b\_{1}]},\textrm{uf}^{[a\_{1},b\_{1}]},\ldots, s[aM,bM],uf[aM,bM])s^{[a\_{M},b\_{M}]},\textrm{uf}^{[a\_{M},b\_{M}]}), then we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | v[al,bl]​(C;𝐬)=𝝀[al,bl]​(𝐬)′​Q​𝜷[al,bl]−γ[al,bl]​(𝐬)for​l=1,…,M,v^{[a\_{l},b\_{l}]}(C;\mathbf{s})={\bm{\lambda}^{[a\_{l},b\_{l}]}}(\mathbf{s})^{\prime}Q\bm{\beta}^{[a\_{l},b\_{l}]}-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s})\quad\,{\rm for}\,l=1,\ldots,M, |  | (5) |

where Q={qi​j}1≤i≤m,0≤j≤nQ={\{q\_{ij}\}}\_{1\leq i\leq m,0\leq j\leq n} is the DPM of the underlying portfolio, 𝛃[al,bl]=(β0[al,bl],…,βn[al,bl])′\bm{\beta}^{[a\_{l},b\_{l}]}=(\beta\_{0}^{[a\_{l},b\_{l}]},\ldots,\beta\_{n}^{[a\_{l},b\_{l}]})^{\prime}, βj[al,bl]=(j​(1−R)/n−al)+−(j​(1−R)/n−bl)+\beta\_{j}^{[a\_{l},b\_{l}]}={\left(j(1-R)/n-a\_{l}\right)}^{+}-{\left(j(1-R)/n-b\_{l}\right)}^{+} for j=0,1,…,nj=0,1,\ldots,n, 𝛌[al,bl](𝐬)=(λ1[al,bl](𝐬),\bm{\lambda}^{[a\_{l},b\_{l}]}(\mathbf{s})=(\lambda\_{1}^{[a\_{l},b\_{l}]}(\mathbf{s}),
  
…,λm[al,bl](𝐬))′\ldots,\lambda\_{m}^{[a\_{l},b\_{l}]}(\mathbf{s}))^{\prime},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λi[al,bl]​(𝐬)\displaystyle\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s}) | =s[al,bl]​D​(Ti)​(Ti−Ti−1)+D​(Ti−1+Ti2)−D​(Ti+1+Ti2)​𝟏{i<m}\displaystyle=s^{[a\_{l},b\_{l}]}D(T\_{i})(T\_{i}-T\_{i-1})+D\left(\frac{T\_{i-1}+T\_{i}}{2}\right)-D\left(\frac{T\_{i+1}+T\_{i}}{2}\right)\mathbf{1}\_{\{i<m\}} |  | (6) |

for i=1,…,mi=1,\ldots,m, and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ[al,bl]​(𝐬)\displaystyle\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}) | =(bl−al)​uf[al,bl]+(bl−al)​s[al,bl]​∑i=1mD​(Ti)​(Ti−Ti−1).\displaystyle=(b\_{l}-a\_{l})\text{uf}^{[a\_{l},b\_{l}]}+(b\_{l}-a\_{l})s^{[a\_{l},b\_{l}]}\sum\_{i=1}^{m}D(T\_{i})(T\_{i}-T\_{i-1}). |  | (7) |

Proof. See Section [8](https://arxiv.org/html/2602.08039v1#S8 "8 Proofs of Propositions 3.1 and 3.2") in the e-companion. □\Box

### 3.3 A Sufficient and Necessary Condition for Weak Compatibility

According to Proposition [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmProposition2 "Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility"), identifying a copula C∈𝒞0C\in\mathcal{C}\_{0} via
v[al,bl]​(C;𝐬)=0v^{[a\_{l},b\_{l}]}(C;\mathbf{s})=0 is equivalent to identifying a DPM QQ, as the right-hand side (RHS) of ([5](https://arxiv.org/html/2602.08039v1#S3.E5 "In Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility")) depends on CC solely through QQ. Moreover, Proposition [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmProposition2 "Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility") implies that v[al,bl]v^{[a\_{l},b\_{l}]} depends affinely on the elements qi​jq\_{ij} (1≤i≤m1\leq i\leq m and 0≤j≤n0\leq j\leq n) of the DPM QQ. It turns out that this nice affine structure enables the reduction of the problem of identifying a copula C∈𝒞0C\in\mathcal{C}\_{0} to an LP problem, or more precisely, a linear feasibility problem. Theorem [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem1 "Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility") below establishes a sufficient and necessary condition for weak compatibility in terms of an LP problem, whereas Theorem [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem2 "Theorem 3.2 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility") provides a method to construct a corresponding concrete copula C∈𝒞0C\in\mathcal{C}\_{0} when weak compatibility is satisfied.

###### Theorem 3.1

(A Sufficient and Necessary Condition for Weak Compatibility)
The market prices of CDO tranches 𝐬=(s[a1,b1],uf[a1,b1],…,s[aM,bM],uf[aM,bM])\mathbf{s}=(s^{[a\_{1},b\_{1}]},\textrm{uf}^{[a\_{1},b\_{1}]},\ldots,s^{[a\_{M},b\_{M}]},\textrm{uf}^{[a\_{M},b\_{M}]}) satisfy weak compatibility if and only if there exists {q^i​j}1≤i≤m,0≤j≤n\{\hat{q}\_{ij}\}\_{1\leq i\leq m,0\leq j\leq n} that satisfies the following linear constraints:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∑i=1m∑j=0nλi[al,bl]​(𝐬)​βj[al,bl]​q^i​j−γ[al,bl]​(𝐬)=0for 1≤l≤M,∑j=0nq^i​j=1for 1≤i≤m,∑j=0nj​q^i​j=n​F​(Ti)for 1≤i≤m,∑k≥jq^i​k≤∑k≥jq^i+1,kfor 1≤i≤m−1 and 0≤j≤n,q^i​j≥0for 1≤i≤m and 0≤j≤n.\left\{\begin{array}[]{ll}\sum\_{i=1}^{m}\sum\_{j=0}^{n}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})\beta\_{j}^{[a\_{l},b\_{l}]}\hat{q}\_{ij}-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s})=0&\quad\text{{for} $1\leq l\leq M$},\\ \sum\_{j=0}^{n}\hat{q}\_{ij}=1&\quad\text{{for} $1\leq i\leq m$},\\ \sum\_{j=0}^{n}j\hat{q}\_{ij}=nF(T\_{i})&\quad\text{{for} $1\leq i\leq m$},\\ \sum\_{k\geq j}\hat{q}\_{ik}\leq\sum\_{k\geq j}\hat{q}\_{i+1,k}&\quad\text{{for} $1\leq i\leq m-1$ {and} $0\leq j\leq n$},\\ \hat{q}\_{ij}\geq 0&\quad\text{{for} $1\leq i\leq m$ {and} $0\leq j\leq n$.}\\ \end{array}\right. |  | (8) |

Proof. See Section [9](https://arxiv.org/html/2602.08039v1#S9 "9 Proofs of Theorems 3.1 and 3.2") in the e-companion. □\Box

###### Theorem 3.2

(A Method to Construct a Copula C^∈𝒞0\hat{C}\in\mathcal{C}\_{0} When Weak Compatibility is Satisfied)
Suppose that {q^i​j}1≤i≤m,0≤j≤n{\{\hat{q}\_{ij}\}}\_{1\leq i\leq m,0\leq j\leq n} is a solution to ([8](https://arxiv.org/html/2602.08039v1#S3.E8 "In Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")).
Then there exists an exchangeable copula C^\hat{C} that perfectly fits all market prices; specifically, C^\hat{C} is defined as follows.
Given yj∈{0,1,…,m+1}y\_{j}\in\{0,1,\ldots,m+1\} (for 1≤j≤n1\leq j\leq n), define uj:=F​(Tyj)u\_{j}:=F(T\_{y\_{j}}). Then the value of the copula C^\hat{C} at (u1,…,un)(u\_{1},\ldots,u\_{n}) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | C^​(u1,…,un):=1n!​∑σ∈𝒢nmin1≤j≤n⁡{∑k≥σ​(j)q^yj,k},\hat{C}(u\_{1},\ldots,u\_{n}):=\frac{1}{n!}\sum\_{\sigma\in\mathcal{G}\_{n}}\min\_{1\leq j\leq n}\left\{\sum\_{k\geq\sigma(j)}\hat{q}\_{y\_{j},k}\right\}, |  | (9) |

where 𝒢n\mathcal{G}\_{n} is the set of all permutations on the set {1,2,…,n}\{1,2,\ldots,n\}.

Proof. See Section [9](https://arxiv.org/html/2602.08039v1#S9 "9 Proofs of Theorems 3.1 and 3.2") in the e-companion. □\Box

### 3.4 An Efficient Algorithm for Verifying Weak Compatibility and Constructing a Corresponding Concrete Copula When Satisfied

Based on Theorems [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem1 "Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility") and [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem2 "Theorem 3.2 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility"), we can develop the following algorithm to verify weak compatibility and construct a corresponding concrete copula when weak compatibility is satisfied. Since the core component of this algorithm is to solve an LP problem, or more precisely, a linear feasibility problem, the algorithm exhibits high efficiency.

 



Algorithm 3.1  Verifying Weak Compatibility and Constructing a Concrete Copula

 

1. Step 1:

   Calculate Coefficients. Compute the coefficients λi[al,bl]​(𝐬)\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s}), γ[al,bl]​(𝐬)\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}), and βj[al,bl]\beta\_{j}^{[a\_{l},b\_{l}]} based on market data, as defined in Proposition [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmProposition2 "Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility").
2. Step 2:

   Verify Weak Compatibility by Solving an LP Problem. Solve the linear feasibility problem ([8](https://arxiv.org/html/2602.08039v1#S3.E8 "In Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")) for the DPM.
   If a feasible solution exists, the market prices satisfy weak compatibility; otherwise, they do not.
3. Step 3:

   Construct a Corresponding Concrete Copula When Weak Compatibility is Satisfied. If the market prices satisfy weak compatibility, use a feasible DPM Q^\hat{Q} obtained in Step 2 to construct a concrete copula C^∈𝒞0\hat{C}\in\mathcal{C}\_{0} as defined in ([9](https://arxiv.org/html/2602.08039v1#S3.E9 "In Theorem 3.2 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")).

 

Denote by 𝒬\mathcal{Q} the feasible region of ([8](https://arxiv.org/html/2602.08039v1#S3.E8 "In Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")). We refer to a feasible Q^∈𝒬\hat{Q}\in\mathcal{Q}, if it exists, as a “market-implied DPM” for the CDO. The market implied DPM may not be unique. Indeed, in such a case, the set 𝒬\mathcal{Q} encapsulates all possible DPMs that are consistent with the observed market prices of standard CDO tranches. The non-uniqueness of the market-implied DPM is reasonable. This is because 𝒞0\mathcal{C}\_{0} is extensive, encompassing all possible CDO models, while the observable market data, namely the prices of a finite number of standard CDO tranches, provides only partial information regarding the underlying CDO model. Consequently, multiple CDO models may exist, and accordingly multiple market-implied DPMs, all of which perfectly fit the market prices. Essentially, the feasible set 𝒬\mathcal{Q} precisely characterizes all possible CDO models that achieve a perfect fit to the market prices.

### 3.5 Extension to Weak Bid-Ask Compatibility

In practice, market prices of CDO tranches are quoted in the form of bid prices and ask prices. Notably, our weak compatibility framework can be readily extended to incorporate the market bid-ask prices. In such a scenario,
rather than perfectly fitting a single price point, the requirement is that there must exist a copula model whose implied fair price lies within the observed bid-ask interval for all tranches.

We introduce a new concept termed Weak Bid-Ask Compatibility to address this issue, i.e., the theoretical consistency of market bid-ask prices of CDO tranches.
For any copula CC, its model-implied fair price denoted by 𝐬model\mathbf{s}\_{\text{model}} refers to the price that equates the expected NPVs of a long protection position to zero, i.e., v[al,bl]​(C;𝐬model)=0v^{[a\_{l},b\_{l}]}(C;\mathbf{s}\_{\text{model}})=0 for 1≤l≤M1\leq l\leq M.
Weak bid-ask compatibility, in turn, requires the existence of a copula C∈𝒞0C\in\mathcal{C}\_{0} whose model-implied fair price 𝐬model\mathbf{s}\_{\text{model}} is between the market bid price 𝐬bid\mathbf{s}\_{\text{bid}} and ask price 𝐬ask\mathbf{s}\_{\text{ask}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐬bid≤𝐬model≤𝐬ask.\displaystyle\mathbf{s}\_{\text{bid}}\leq\mathbf{s}\_{\text{model}}\leq\mathbf{s}\_{\text{ask}}. |  | (10) |

Since the expected NPV v[al,bl]​(C;𝐬)v^{[a\_{l},b\_{l}]}(C;\mathbf{s}) is a monotonically decreasing function of the price 𝐬\mathbf{s} for each tranche l=1,…,Ml=1,\ldots,M, “𝐬bid≤𝐬model\mathbf{s}\_{\text{bid}}\leq\mathbf{s}\_{\text{model}}” and “𝐬model≤𝐬ask\mathbf{s}\_{\text{model}}\leq\mathbf{s}\_{\text{ask}}” are equivalent to “v[al,bl]​(C;𝐬bid)≥v[al,bl]​(C;𝐬model)=0v^{[a\_{l},b\_{l}]}(C;\mathbf{s}\_{\text{bid}})\geq v^{[a\_{l},b\_{l}]}(C;\mathbf{s}\_{\text{model}})=0” and “v[al,bl]​(C;𝐬ask)≤v[al,bl]​(C;𝐬model)=0v^{[a\_{l},b\_{l}]}(C;\mathbf{s}\_{\text{ask}})\leq v^{[a\_{l},b\_{l}]}(C;\mathbf{s}\_{\text{model}})=0”, respectively. Therefore, condition ([10](https://arxiv.org/html/2602.08039v1#S3.E10 "In 3.5 Extension to Weak Bid-Ask Compatibility ‣ 3 Weak Compatibility")) can be re-expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v[al,bl]​(C;𝐬bid)≥0andv[al,bl]​(C;𝐬ask)≤0for ​l=1,…,M.\displaystyle v^{[a\_{l},b\_{l}]}(C;\mathbf{s}\_{\text{bid}})\geq 0\quad\textrm{and}\quad v^{[a\_{l},b\_{l}]}(C;\mathbf{s}\_{\text{ask}})\leq 0\quad\text{for }l=1,\ldots,M. |  | (11) |

Compared with condition ([10](https://arxiv.org/html/2602.08039v1#S3.E10 "In 3.5 Extension to Weak Bid-Ask Compatibility ‣ 3 Weak Compatibility")), condition ([11](https://arxiv.org/html/2602.08039v1#S3.E11 "In 3.5 Extension to Weak Bid-Ask Compatibility ‣ 3 Weak Compatibility")) is more straightforward to verify. Accordingly, we adopt it as the formal definition of weak bid-ask compatibility.

###### Definition 3.1 (Weak Bid-Ask Compatibility)

Market bid-ask prices (𝐬bid,𝐬ask)(\mathbf{s}\_{\text{bid}},\mathbf{s}\_{\text{ask}}) of all MM CDO tranches are said to be *weakly bid-ask compatible* if there exists a copula C∈𝒞0C\in\mathcal{C}\_{0} such that the expected NPVs from a long protection position satisfy ([11](https://arxiv.org/html/2602.08039v1#S3.E11 "In 3.5 Extension to Weak Bid-Ask Compatibility ‣ 3 Weak Compatibility")).

The verification of weak bid-ask compatibility is analogous to Theorem [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem1 "Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility"), leading to the following Proposition [3.3](https://arxiv.org/html/2602.08039v1#S3.ThmProposition3 "Proposition 3.3 (A Sufficient and Necessary Condition for Weak Bid-Ask Compatibility) ‣ 3.5 Extension to Weak Bid-Ask Compatibility ‣ 3 Weak Compatibility") which reduces the verification problem to a linear feasibility problem.
Similar to Algorithm [3.4](https://arxiv.org/html/2602.08039v1#S3.SS4 "3.4 An Efficient Algorithm for Verifying Weak Compatibility and Constructing a Corresponding Concrete Copula When Satisfied ‣ 3 Weak Compatibility"), we can also develop an algorithm to verify weak bid-ask compatibility and, when satisfied, constructing a corresponding concrete copula. The details are omitted due to the analogy.

###### Proposition 3.3 (A Sufficient and Necessary Condition for Weak Bid-Ask Compatibility)

The market bid-ask prices (𝐬bid,𝐬ask\mathbf{s}\_{\text{bid}},\mathbf{s}\_{\text{ask}}) satisfy weak bid-ask compatibility if and only if there exists a matrix {q^i​j}1≤i≤m,0≤j≤n\{\hat{q}\_{ij}\}\_{1\leq i\leq m,0\leq j\leq n} that satisfies the following linear constraints:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∑i=1m∑j=0nλi[al,bl]​(𝐬bid)​βj[al,bl]​q^i​j−γ[al,bl]​(𝐬bid)≥0for 1≤l≤M,∑i=1m∑j=0nλi[al,bl]​(𝐬ask)​βj[al,bl]​q^i​j−γ[al,bl]​(𝐬ask)≤0for 1≤l≤M,∑j=0nq^i​j=1for 1≤i≤m,∑j=0nj​q^i​j=n​F​(Ti)for 1≤i≤m,∑k≥jq^i​k≤∑k≥jq^i+1,kfor 1≤i≤m−1 and 0≤j≤n,q^i​j≥0for 1≤i≤m and 0≤j≤n.\begin{cases}\sum\_{i=1}^{m}\sum\_{j=0}^{n}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s}\_{\text{bid}})\beta\_{j}^{[a\_{l},b\_{l}]}\hat{q}\_{ij}-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}\_{\text{bid}})\geq 0&\quad\text{{for} $1\leq l\leq M$},\\ \sum\_{i=1}^{m}\sum\_{j=0}^{n}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s}\_{\text{ask}})\beta\_{j}^{[a\_{l},b\_{l}]}\hat{q}\_{ij}-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}\_{\text{ask}})\leq 0&\quad\text{{for} $1\leq l\leq M$},\\ \sum\_{j=0}^{n}\hat{q}\_{ij}=1&\quad\text{{for} $1\leq i\leq m$},\\ \sum\_{j=0}^{n}j\hat{q}\_{ij}=nF(T\_{i})&\quad\text{{for} $1\leq i\leq m$},\\ \sum\_{k\geq j}\hat{q}\_{ik}\leq\sum\_{k\geq j}\hat{q}\_{i+1,k}&\quad\text{{for} $1\leq i\leq m-1$ {and} $0\leq j\leq n$},\\ \hat{q}\_{ij}\geq 0&\quad\text{{for} $1\leq i\leq m$ {and} $0\leq j\leq n$}.\\ \end{cases} |  | (12) |

*Proof.* The proof is similar to that of Theorem [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem1 "Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility") and is therefore omitted. □\Box

## 4 Strong Compatibility

In this section, we intend to derive a sufficient and necessary condition for strong compatibility. Additionally, if this condition is satisfied, we will provide a method to construct a corresponding concrete copula C∈𝒞1C\in\mathcal{C}\_{1} that achieves a perfect fit. Our approach is grounded in the theory of stochastic distortions.
Specifically, we introduce a new and flexible family of stochastic distortions, termed *gamma distortions*, which allows us to reframe the verification of strong compatibility as a series of LP problems, or more precisely, linear feasibility problems.
Solving these LP problems yields not only a sufficient and necessary condition for strong compatibility but also the parameters required to construct a corresponding concrete copula C∈𝒞1C\in\mathcal{C}\_{1}.

### 4.1 Conditionally I.I.D. Models and Stochastic Distortions

As preliminary preparations, we first introduce the concept of stochastic distortions and then establish the close connection between conditionally i.i.d. copulas and stochastic distortions.

###### Definition 4.1 (Stochastic Distortion, Lin et al. [2018](https://arxiv.org/html/2602.08039v1#bib.bib10 "Stochastic distortion and its transformed copula"))

A stochastic process {X​(u):u∈[0,1]}\{X(u):u\in[0,1]\} is called a *stochastic distortion* if it is non-decreasing a.s. (that is, X​(u1)≤X​(u2)X(u\_{1})\leq X(u\_{2}) a.s. for any u1<u2u\_{1}<u\_{2}) and satisfies that X​(0)=0X(0)=0 and X​(1)=1X(1)=1 a.s..

If a stochastic distortion X​(u)X(u) satisfies 𝔼​[X​(u)]=u\mathbb{E}[X(u)]=u for any u∈[0,1]u\in[0,1], then

|  |  |  |  |
| --- | --- | --- | --- |
|  | CX​(u1,…,un):=𝔼​[∏j=1nX​(uj)]for (u1,…,un)∈[0,1]nC^{X}(u\_{1},\ldots,u\_{n}):=\mathbb{E}\left[\prod\_{j=1}^{n}X(u\_{j})\right]\quad\text{for $(u\_{1},\ldots,u\_{n})\in[0,1]^{n}$} |  | (13) |

is a copula function (see Theorem 3.1 of Lin et al. [2018](https://arxiv.org/html/2602.08039v1#bib.bib10 "Stochastic distortion and its transformed copula")). In our paper, we will call
CXC^{X} the *transformed copula by the stochastic distortion XX*.

In Proposition [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmProposition1 "Proposition 4.1 (Stochastic Distortion Representations of Conditionally I.I.D. Copulas) ‣ 4.1 Conditionally I.I.D. Models and Stochastic Distortions ‣ 4 Strong Compatibility") below, we establish the equivalence between conditionally i.i.d. copulas and the existence of specific stochastic distortion representations.
As a direct consequence, each conditionally i.i.d. copula can be represented as a transformed copula by a stochastic distortion.

###### Proposition 4.1 (Stochastic Distortion Representations of Conditionally I.I.D. Copulas)

Let {Uk}k∈ℕ+{\{U\_{k}\}}\_{k\in\mathbb{N}^{+}} be an infinite sequence of uniformly distributed random variables over (0,1)(0,1) (abbreviated as 𝒰​(0,1)\mathcal{U}(0,1) random variables hereafter) on a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}). Then the following statements are equivalent.

1. (i)

   {Uk}k∈ℕ+{\{U\_{k}\}}\_{k\in\mathbb{N}^{+}} are i.i.d. conditional on some σ\sigma-field ℋ⊆ℱ\mathcal{H}\subseteq\mathcal{F}.
2. (ii)

   There exists a stochastic distortion XX with 𝔼​[X​(u)]=u\mathbb{E}[X(u)]=u for all u∈[0,1]u\in[0,1] such that for any n≥2n\geq 2, the copula CC of (U1,…,Un)(U\_{1},\ldots,U\_{n}) is identical to the transformed copula CXC^{X} by the stochastic distortion XX, i.e.,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | C​(u1,…,un)=CX​(u1,…,un).C(u\_{1},\ldots,u\_{n})=C^{X}(u\_{1},\ldots,u\_{n}). |  | (14) |

Proof. See Section [10](https://arxiv.org/html/2602.08039v1#S10 "10 Proofs of Propositions 4.1, 4.2 and 4.4") in the e-companion. □\Box

###### Remark 4.1

According to the celebrated de Finetti’s Theorem (see, e.g., Mai [2020](https://arxiv.org/html/2602.08039v1#bib.bib2 "The infinite extendibility problem for exchangeable real-valued random vectors")), (i) in Proposition [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmProposition1 "Proposition 4.1 (Stochastic Distortion Representations of Conditionally I.I.D. Copulas) ‣ 4.1 Conditionally I.I.D. Models and Stochastic Distortions ‣ 4 Strong Compatibility") is equivalent to the statement that {Uk}k∈ℕ+{\{U\_{k}\}}\_{k\in\mathbb{N}^{+}} are infinitely exchangeable.

### 4.2 Valuation of CDO Tranches under Conditionally I.I.D. Models

Next, we discuss the valuation methodology of CDO tranches under a conditionally i.i.d. model, where τ1,…,τn\tau\_{1},\ldots,\tau\_{n} are assumed to be i.i.d. conditional on some common factors represented by a σ\sigma-field ℋ\mathcal{H}. As established in Proposition [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmProposition1 "Proposition 4.1 (Stochastic Distortion Representations of Conditionally I.I.D. Copulas) ‣ 4.1 Conditionally I.I.D. Models and Stochastic Distortions ‣ 4 Strong Compatibility"), such a conditionally i.i.d. structure implies the existence of a stochastic distortion XX that satisfies 𝔼​[X​(u)]=u\mathbb{E}[X(u)]=u and is given explicitly by
X​(u)=ℙ​[F​(τ1)≤u|ℋ].X(u)=\mathbb{P}[F(\tau\_{1})\leq u|\mathcal{H}].
Then we can deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi​j=ℙ​(NTi=j)=𝔼​[ℙ​(NTi=j|ℋ)]=𝔼​[(nj)​X​(F​(Ti))j​(1−X​(F​(Ti)))n−j]\displaystyle q\_{ij}=\mathbb{P}(N\_{T\_{i}}=j)=\mathbb{E}[\mathbb{P}(N\_{T\_{i}}=j|\mathcal{H})]=\mathbb{E}\left[\binom{n}{j}X(F(T\_{i}))^{j}(1-X(F(T\_{i})))^{n-j}\right] |  | (15) |

for 1≤i≤m1\leq i\leq m and 0≤j≤n0\leq j\leq n. Plugging ([15](https://arxiv.org/html/2602.08039v1#S4.E15 "In 4.2 Valuation of CDO Tranches under Conditionally I.I.D. Models ‣ 4 Strong Compatibility")) into ([5](https://arxiv.org/html/2602.08039v1#S3.E5 "In Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility")) yields immediately the following explicit expression for the expected NPVs v[al,bl]​(CX;𝐬)v^{[a\_{l},b\_{l}]}(C^{X};\mathbf{s}) of tranches
in terms of the stochastic distortion XX:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v[al,bl]​(CX;𝐬)=∑i=1m∑j=0nλi[al,bl]​(𝐬)​βj[al,bl]​(nj)​𝔼​[X​(F​(Ti))j​(1−X​(F​(Ti)))n−j]−γ[al,bl]​(𝐬)v^{[a\_{l},b\_{l}]}(C^{X};\mathbf{s})=\sum\_{i=1}^{m}\sum\_{j=0}^{n}\lambda^{[a\_{l},b\_{l}]}\_{i}(\mathbf{s})\beta\_{j}^{[a\_{l},b\_{l}]}\binom{n}{j}\mathbb{E}\left[X(F(T\_{i}))^{j}(1-X(F(T\_{i})))^{n-j}\right]-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}) |  | (16) |

for 1≤l≤M.1\leq l\leq M.

###### Remark 4.2 (Immediate Applications to Parametric Copula Models)

The above valuation me-
  
-thodology of CDO tranches based on stochastic distortions applies directly to many widely used families of parametric copula models, including Gaussian, Archimedean, and multivariate Fréchet copulas, as they are conditionally i.i.d. and thus admit stochastic distortion representations. Consequently, the expected tranche NPVs v[al,bl]v^{[a\_{l},b\_{l}]} for any of these models can be computed by substituting the model’s specific stochastic distortion XX into the general valuation formula ([16](https://arxiv.org/html/2602.08039v1#S4.E16 "In 4.2 Valuation of CDO Tranches under Conditionally I.I.D. Models ‣ 4 Strong Compatibility")).

### 4.3 Gamma Distortions and Gamma-Distorted Copulas

This subsection introduces a novel family of stochastic distortions, termed gamma distortions.
We show that applying a discrete form of the *transformed copula by gamma distortion* to model default times, each element of the resulting DPM QQ is then a linear combination of the underlying discrete state probabilities, thereby facilitating the related analysis.

The construction of gamma distortions is based on the gamma process, a well-known stochastic process extensively studied
in the literature (see, e.g., Applebaum [2009](https://arxiv.org/html/2602.08039v1#bib.bib35 "Lévy processes and stochastic calculus") and Schoutens and Cariboni [2012](https://arxiv.org/html/2602.08039v1#bib.bib66 "Lévy processes in credit risk")).
Recall that a gamma process {Γ​(t;γ,λ):t≥0}\{\Gamma(t;\gamma,\lambda):t\geq 0\} with parameters γ>0\gamma>0 and λ>0\lambda>0 is a pure-jump Lévy process, which is increasing a.s. and satisfies that for any fixed time t>0t>0, Γ​(t;γ,λ)\Gamma(t;\gamma,\lambda) follows a gamma distribution with shape parameter γ​t\gamma t and rate parameter λ\lambda.

Consider an N∈ℕ+N\in\mathbb{N}^{+} and two independent gamma processes {ξt:t≥0}\{\xi\_{t}:t\geq 0\} and {ηt:t≥0}\{\eta\_{t}:t\geq 0\} with both parameters γ\gamma and λ\lambda equal to 11.
Suppose that {ϕ​(u):0≤u≤1}\{\phi(u):0\leq u\leq 1\} is a non-decreasing stochastic process that is independent of {ξt}\{\xi\_{t}\} and {ηt}\{\eta\_{t}\} and satisfies the following conditions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(0)=0a.s.,ϕ​(1)=Na.s.,and𝔼​[ϕ​(u)]=N​u.\phi(0)=0\quad\text{a.s.},\quad\phi(1)=N\quad\text{a.s.},\quad\text{and}\quad\mathbb{E}[\phi(u)]=Nu. |  | (17) |

Define a stochastic process {X​(u):u∈[0,1]}\{X(u):u\in[0,1]\} as follows, which proves to be a stochastic distortion.

|  |  |  |  |
| --- | --- | --- | --- |
|  | X​(u):=ξϕ​(u)ξϕ​(u)+ηN−ϕ​(u)for 0≤u≤1.X(u):=\frac{\xi\_{\phi(u)}}{\xi\_{\phi(u)}+\eta\_{N-\phi(u)}}\quad\text{for $0\leq u\leq 1$}. |  | (18) |

###### Proposition 4.2

The stochastic process XX defined in ([18](https://arxiv.org/html/2602.08039v1#S4.E18 "In 4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility")) is a stochastic distortion and satisfies 𝔼​[X​(u)]=u\mathbb{E}[X(u)]=u for 0≤u≤10\leq u\leq 1.

Proof. See Section [10](https://arxiv.org/html/2602.08039v1#S10 "10 Proofs of Propositions 4.1, 4.2 and 4.4") in the e-companion. □\Box

###### Definition 4.2 (Gamma Distortions, Gamma-Distorted Copulas, and Their Generators)

The stochastic distortion XX defined in ([18](https://arxiv.org/html/2602.08039v1#S4.E18 "In 4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility")) is referred to as a *gamma distortion*, the transformed copula by the gamma distortion XX is called a *gamma-distorted copula*, and the involved non-decreasing stochastic process {ϕ​(u):0≤u≤1}\{\phi(u):0\leq u\leq 1\} is called the *generator of the gamma distortion XX* or *the generator of the gamma-distorted copula*.

Below we introduce a particular type of gamma distortions and gamma-distorted copulas with a specific “discrete” structure.

###### Definition 4.3 (Discrete Gamma Distortions and Discrete Gamma-Distorted Copulas)

If the generator ϕ\phi of a gamma distortion XX satisfies an additional “discrete” condition that for each i=1,…,mi=1,\dots,m, the random variable ϕ​(F​(Ti))\phi(F(T\_{i})) takes only discrete values in {0,1,…,N}\{0,1,\ldots,N\} with the probability mass function pi​k=ℙ​(ϕ​(F​(Ti))=k)p\_{ik}=\mathbb{P}(\phi(F(T\_{i}))=k) for any k=0,1,…,Nk=0,1,\ldots,N, we refer to the associated gamma distortion XX and gamma-distorted copula as a *discrete gamma distortion* and a *discrete gamma-distorted copula*, respectively.

Using ([15](https://arxiv.org/html/2602.08039v1#S4.E15 "In 4.2 Valuation of CDO Tranches under Conditionally I.I.D. Models ‣ 4 Strong Compatibility")), we can obtain that for a discrete gamma-distorted copula, the elements of the associated DPM can be expressed as a linear combination of the probabilities pi​kp\_{ik} for i=1,…,mi=1,\dots,m and k=0,1,…,Nk=0,1,\ldots,N:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi​j=∑k=0Nhj​k(N)​pi​kfor 1≤i≤m and 0≤j≤n,q\_{ij}=\sum\_{k=0}^{N}h\_{jk}^{(N)}p\_{ik}\quad\text{for $1\leq i\leq m$ and $0\leq j\leq n$}, |  | (19) |

where the coefficients hj​k(N)h\_{jk}^{(N)} are defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | hj​0(N):=𝟏{j=0}for 0≤j≤n,hj​k(N):=(nj)​B​(k+j,N+n−k−j)B​(k,N−k)for 0≤j≤n and 1≤k≤N−1,hj​N(N):=𝟏{j=n}for 0≤j≤n,\begin{array}[]{ll}h\_{j0}^{(N)}:=\mathbf{1}\_{\{j=0\}}&\quad\text{for $0\leq j\leq n$},\\ h\_{jk}^{(N)}:=\binom{n}{j}\frac{\mathrm{B}(k+j,N+n-k-j)}{\mathrm{B}(k,N-k)}&\quad\text{for $0\leq j\leq n$ and $1\leq k\leq N-1$},\\ h\_{jN}^{(N)}:=\mathbf{1}\_{\{j=n\}}&\quad\text{for $0\leq j\leq n$},\end{array} |  | (20) |

with B​(⋅,⋅)\mathrm{B}(\cdot,\cdot) denoting the Beta function.

### 4.4 A Sufficient and Necessary Condition for Strong Compatibility

While discrete gamma-distorted copulas represent only a specific subclass of conditionally i.i.d. copulas, this specific family exhibits a remarkable universality. Specifically, we find that for any of the entire set of strongly compatible market prices except those lying on the boundary of this set (this boundary has a zero Lebesgue measure), there always exists a discrete gamma-distorted copula that achieves a perfect fit. Furthermore, whether market prices of CDO tranches can be perfectly fit by such a copula—and thus whether they are strongly compatible—can be verified efficiently by solving LP problems.

Theorem [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem1 "Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") below provides a sufficient and necessary condition for strong compatibility. When the condition is satisfied, Theorem [4.2](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem2 "Theorem 4.2 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") below offers a method to construct a corresponding concrete conditionally i.i.d. copula C∈𝒞1C\in\mathcal{C}\_{1} that achieves a perfect fit.

###### Theorem 4.1

(A Sufficient and Necessary Condition for Strong Compatibility)
Let 𝒜⊆ℝ2​M\mathcal{A}\subseteq\mathbb{R}^{2M} denote the set of strongly compatible market prices and 𝒜∘\mathcal{A}^{\circ} denote the interior of 𝒜\mathcal{A}.
Then for each vector 𝐬∈𝒜∘\mathbf{s}\in\mathcal{A}^{\circ}, there exists an N∈ℕ+N\in\mathbb{N}^{+} such that the following system of linear constraints for {p^i​k}1≤i≤m,0≤k≤N\{\hat{p}\_{ik}\}\_{1\leq i\leq m,0\leq k\leq N} has a feasible solution.

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∑i=1m∑k=0Ngi​k​l(N)​(𝐬)​p^i​k−γ[al,bl]​(𝐬)=0for 1≤l≤M,∑k=0Np^i​k=1for 1≤i≤m,∑k=0Nk​p^i​k=N​F​(Ti)for 1≤i≤m,∑j≥kp^i​j≤∑j≥kp^i+1,jfor 1≤i≤m−1 and 0≤k≤N,p^i​k≥0for 1≤i≤m and 0≤k≤N,\begin{cases}\sum\_{i=1}^{m}\sum\_{k=0}^{N}g\_{ikl}^{(N)}(\mathbf{s})\hat{p}\_{ik}-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s})=0\,&\quad\text{{for} $1\leq l\leq M$},\\ \sum\_{k=0}^{N}\hat{p}\_{ik}=1\,&\quad\text{{for} $1\leq i\leq m$},\\ \sum\_{k=0}^{N}k\hat{p}\_{ik}=NF(T\_{i})\,&\quad\text{{for} $1\leq i\leq m$},\\ \sum\_{j\geq k}\hat{p}\_{ij}\leq\sum\_{j\geq k}\hat{p}\_{i+1,j}\,&\quad\text{{for} $1\leq i\leq m-1$ and $0\leq k\leq N$},\\ \hat{p}\_{ik}\geq 0\,&\quad\text{{for} $1\leq i\leq m$ and $0\leq k\leq N$},\\ \end{cases} |  | (21) |

where gi​k​l(N)​(𝐬)=∑j=0nhj​k(N)​λi[al,bl]​(𝐬)​βj[al,bl]g\_{ikl}^{(N)}(\mathbf{s})=\sum\_{j=0}^{n}h\_{jk}^{(N)}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})\beta\_{j}^{[a\_{l},b\_{l}]} for 1≤i≤m1\leq i\leq m, 0≤k≤N0\leq k\leq N, and 1≤l≤M1\leq l\leq M,
hj​k(N)h\_{jk}^{(N)} is defined in ([20](https://arxiv.org/html/2602.08039v1#S4.E20 "In 4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility")), and λi[al,bl]​(𝐬)\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s}) and βj[al,bl]\beta\_{j}^{[a\_{l},b\_{l}]} are given in Proposition [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmProposition2 "Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility").

Conversely, if for the market prices 𝐬\mathbf{s}, there exists an N∈ℕ+N\in\mathbb{N}^{+} such that the system of linear constraints ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) has a feasible solution, then the market prices 𝐬\mathbf{s} is strongly compatible.

Proof. See Section [11](https://arxiv.org/html/2602.08039v1#S11 "11 Proofs of Theorems 4.1 and 4.2") in the e-companion. □\Box

###### Remark 4.3

The sufficient and necessary condition provided in Theorem [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem1 "Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") is indeed a sufficient and necessary condition up to the set 𝒜\mathcal{A}’s boundary with zero Lebesgue measure, where the set 𝒜\mathcal{A} denotes the set of strongly compatible market prices. Since the set 𝒜\mathcal{A}’s boundary has a zero Lebesgue measure, it suffices for practical applications.

As for the first part of Theorem [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem1 "Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility"), we can obtain a stronger result in the following Proposition [4.3](https://arxiv.org/html/2602.08039v1#S4.ThmProposition3 "Proposition 4.3 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility"), which will be used to prove that Algorithm [4.5.2](https://arxiv.org/html/2602.08039v1#S4.SS5.SSS2 "4.5.2 Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility") will terminate in a finite number of iterations.

###### Proposition 4.3

For each vector 𝐬∈𝒜∘\mathbf{s}\in\mathcal{A}^{\circ}, there exists an N0∈ℕ+N\_{0}\in\mathbb{N}^{+} such that the system of linear constraints ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) has a feasible solution for any N≥N0N\geq N\_{0}.

Proof. See Section [12](https://arxiv.org/html/2602.08039v1#S12 "12 Proof of Proposition 4.3") in the e-companion. □\Box

Next, we shall develop a method to construct a concrete copula C∈𝒞1C\in\mathcal{C}\_{1} when strong compatibility is satisfied. Indeed, in such a case, we can construct a discrete gamma-distorted copula.

###### Proposition 4.4

Suppose that for some N∈ℕ+N\in\mathbb{N}^{+}, {p^i​k}1≤i≤m,0≤k≤N\{\hat{p}\_{ik}\}\_{1\leq i\leq m,0\leq k\leq N} is a feasible solution to the system of linear constraints ([22](https://arxiv.org/html/2602.08039v1#S4.E22 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∑k=0Np^i​k=1for 1≤i≤m,∑k=0Nk​p^i​k=N​F​(Ti)for 1≤i≤m,∑j≥kp^i​j≤∑j≥kp^i+1,jfor 1≤i≤m−1 and 0≤k≤N,p^i​k≥0for 1≤i≤m and 0≤k≤N.\begin{cases}\sum\_{k=0}^{N}\hat{p}\_{ik}=1\,&\quad\text{{for} $1\leq i\leq m$},\\ \sum\_{k=0}^{N}k\hat{p}\_{ik}=NF(T\_{i})\,&\quad\text{{for} $1\leq i\leq m$},\\ \sum\_{j\geq k}\hat{p}\_{ij}\leq\sum\_{j\geq k}\hat{p}\_{i+1,j}\,&\quad\text{{for} $1\leq i\leq m-1$ and $0\leq k\leq N$},\\ \hat{p}\_{ik}\geq 0\,&\quad\text{{for} $1\leq i\leq m$ and $0\leq k\leq N$}.\end{cases} |  | (22) |

Then the stochastic process {ϕ​(u):0≤u≤1}\{\phi(u):0\leq u\leq 1\} defined below is non-decreasing and satisfies ([17](https://arxiv.org/html/2602.08039v1#S4.E17 "In 4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(u):={∑k=0Nk​𝟏{∑j<kp^i​j<U≤∑j≤kp^i​j}for u=F​(Ti) and i=0,⋯,m+1,(F​(Ti+1)−u)​ϕ​(F​(Ti))+(u−F​(Ti))​ϕ​(F​(Ti+1))F​(Ti+1)−F​(Ti)for u∈(F​(Ti),F​(Ti+1)) and i=0,⋯,m,\phi(u):=\begin{cases}\sum\_{k=0}^{N}k\mathbf{1}\_{\left\{\sum\_{j<k}\hat{p}\_{ij}<U\leq\sum\_{j\leq k}\hat{p}\_{ij}\right\}}&\text{{for} $u=F(T\_{i})$ and $i=0,\cdots\!,m+1$},\\ \frac{(F(T\_{i+1})-u)\phi(F(T\_{i}))+(u-F(T\_{i}))\phi(F(T\_{i+1}))}{F(T\_{i+1})-F(T\_{i})}\!\!&\text{{for} $u\in\!(F(T\_{i}),F(T\_{i+1}))$ and $i=0,\cdots\!,m$},\end{cases} |  | (23) |

where U∼𝒰​(0,1)U\sim\mathcal{U}(0,1), p^0​k:=𝟏{k=0}\hat{p}\_{0k}:=\mathbf{1}\_{\{k=0\}} for k=0,1,…,Nk=0,1,\ldots,N, and p^m+1,k:=𝟏{k=N}\hat{p}\_{m+1,k}:=\mathbf{1}\_{\{k=N\}} for k=0,1,…,Nk=0,1,\ldots,N. Moreover, the stochastic process {ϕ​(u):0≤u≤1}\{\phi(u):0\leq u\leq 1\} satisfies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ϕ​(F​(Ti))=k)=p^i​kfor 1≤i≤m and 0≤k≤N.\mathbb{P}(\phi(F(T\_{i}))=k)=\hat{p}\_{ik}\quad\text{{for} $1\leq i\leq m$ {and} $0\leq k\leq N$}. |  | (24) |

Proof. See Section [10](https://arxiv.org/html/2602.08039v1#S10 "10 Proofs of Propositions 4.1, 4.2 and 4.4") in the e-companion. □\Box

Proposition [4.4](https://arxiv.org/html/2602.08039v1#S4.ThmProposition4 "Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") implies that any feasible solution to the system of linear constraints ([22](https://arxiv.org/html/2602.08039v1#S4.E22 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) can induce a stochastic process {ϕ​(u):0≤u≤1}\{\phi(u):0\leq u\leq 1\} that is qualified to serve as the generator of a discrete gamma-distorted copula. Theorem [4.2](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem2 "Theorem 4.2 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") below will show that if the feasible solution also satisfies the first set of constraints of ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")), the discrete gamma-distorted copula constructed based on {ϕ​(u):0≤u≤1}\{\phi(u):0\leq u\leq 1\} can perfectly fit the market prices across all tranches.

###### Theorem 4.2

(A Method to Construct a Copula C∈𝒞1C\in\mathcal{C}\_{1} When Strong Compatibility is Satisfied)
Suppose that for some N∈ℕ+N\in\mathbb{N}^{+}, {p^i​k}1≤i≤m,0≤k≤N\{\hat{p}\_{ik}\}\_{1\leq i\leq m,0\leq k\leq N} is a feasible solution to the system of linear constraints ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")). Then the discrete gamma-distorted copula CXC^{X} with the generator ϕ\phi defined in ([23](https://arxiv.org/html/2602.08039v1#S4.E23 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) via this feasible solution
perfectly fits the market prices across all tranches [a1,b1],…,[aM,bM][a\_{1},b\_{1}],\ldots,[a\_{M},b\_{M}].

Proof. See Section [11](https://arxiv.org/html/2602.08039v1#S11 "11 Proofs of Theorems 4.1 and 4.2") in the e-companion. □\Box

### 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied

Unlike weak compatibility, verifying strong compatibility cannot be reduced to a single LP problem.
This complexity arises because the linear feasibility problem ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) depends on the parameter NN, which is unknown a priori.
To overcome this, we propose an algorithm that iteratively verifies compatibility, proceeding sequentially across tranches.
For each tranche, the algorithm solves a series of LP problems for an increasing sequence of NN values.
Despite this iterative structure, the process is efficient because each step only involves solving computationally tractable LP problems.

#### 4.5.1 The Key Ideas of Our Iterative Algorithm

Before presenting our iterative algorithm, we first articulate the key ideas.
Let 𝒜l⊆ℝ2​l\mathcal{A}^{l}\subseteq\mathbb{R}^{2l} denote the set of strongly compatible market prices for the first ll tranches (for 1≤l≤M1\leq l\leq M), and let (𝒜l)∘(\mathcal{A}^{l})^{\circ} denote its interior.
We proceed by assuming that (s[a1,b1],uf[a1,b1],…,s[al,bl],uf[al,bl])∈(𝒜l)∘(s^{[a\_{1},b\_{1}]},\textrm{uf}^{[a\_{1},b\_{1}]},\ldots,s^{[a\_{l},b\_{l}]},\textrm{uf}^{[a\_{l},b\_{l}]})\in(\mathcal{A}^{l})^{\circ}.
Consider a system of linear constraints, which is the same as ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) except that the first set of linear constraints of ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) are replaced by ∑i=1m∑k=0Ngi​k​l′(N)​(𝐬)​p^i​k−γ[al′,bl′]​(𝐬)=0\sum\_{i=1}^{m}\sum\_{k=0}^{N}g\_{ikl^{\prime}}^{(N)}(\mathbf{s})\hat{p}\_{ik}-\gamma^{[a\_{l^{\prime}},b\_{l^{\prime}}]}(\mathbf{s})=0 for 1≤l′≤l1\leq l^{\prime}\leq l. Proposition [4.3](https://arxiv.org/html/2602.08039v1#S4.ThmProposition3 "Proposition 4.3 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") ensures that this system of linear constraints is feasible for all sufficiently large NN, and we denote its feasible region by 𝒫Nl\mathcal{P}\_{N}^{l}.

A crucial step in our iterative algorithm is that given that the prices of the first ll tranches are strongly compatible, we need to determine the price range for the (l+1)(l+1)-th tranche that preserves strong compatibility. If the market price of the (l+1)(l+1)-th tranche falls within this range, we conclude that the prices of the first l+1l+1 tranches are strongly compatible and proceed to the next tranche.
Otherwise, the full set of MM market prices is not strongly compatible, and the algorithm terminates.

The determination of this strong compatibility price range depends on how the (l+1)(l+1)-th tranche is quoted.
If it is quoted via up-front payment with fixed spread s[al+1,bl+1]s^{[a\_{l+1},b\_{l+1}]}, we denote the range by [uf¯[al+1,bl+1],uf¯[al+1,bl+1]][\underline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]},\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}], where the upper bound uf¯[al+1,bl+1]\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]} and the lower bound uf¯[al+1,bl+1]\underline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {uf¯[al+1,bl+1]=sup{x∈ℝ:(s[a1,b1],uf[a1,b1],…,s[al,bl],uf[al,bl],s[al+1,bl+1],x)∈𝒜l+1},uf¯[al+1,bl+1]=inf{x∈ℝ:(s[a1,b1],uf[a1,b1],…,s[al,bl],uf[al,bl],s[al+1,bl+1],x)∈𝒜l+1}.\begin{cases}\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}=\sup\left\{x\in\mathbb{R}:(s^{[a\_{1},b\_{1}]},\textrm{uf}^{[a\_{1},b\_{1}]},\ldots,s^{[a\_{l},b\_{l}]},\textrm{uf}^{[a\_{l},b\_{l}]},s^{[a\_{l+1},b\_{l+1}]},x)\in\mathcal{A}^{l+1}\right\},\\ \underline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}=\inf\left\{x\in\mathbb{R}:(s^{[a\_{1},b\_{1}]},\textrm{uf}^{[a\_{1},b\_{1}]},\ldots,s^{[a\_{l},b\_{l}]},\textrm{uf}^{[a\_{l},b\_{l}]},s^{[a\_{l+1},b\_{l+1}]},x)\in\mathcal{A}^{l+1}\right\}.\end{cases} |  | (25) |

If the (l+1)(l+1)-th tranche is quoted via spread, the range [s¯[al+1,bl+1],s¯[al+1,bl+1]][\underline{s}^{[a\_{l+1},b\_{l+1}]},\overline{s}^{[a\_{l+1},b\_{l+1}]}] is given analogously.

However, the strong compatibility price range given above is not directly computable. Notably, we can propose an indirect approach to computing it. Specifically, we can define a sequence of the so-called “NN-dependent price ranges”, which can be computed easily and furthermore can be proved to converge to the strong compatibility price range as NN tends to infinity.
For any fixed N∈ℕ+N\in\mathbb{N}^{+} for which the feasible set 𝒫Nl\mathcal{P}\_{N}^{l} is non-empty, we can compute the NN-dependent price range, [uf¯N[al+1,bl+1],uf¯N[al+1,bl+1]][\underline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N},\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N}] or [s¯N[al+1,bl+1],s¯N[al+1,bl+1]][\underline{s}^{[a\_{l+1},b\_{l+1}]}\_{N},\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N}], by solving a series of LP or linear fractional programming (LFP) problems (LFP problems can also be readily transformed into LP problems). We compute the bounds of these NN-dependent price ranges in the following way.

* •

  If the (l+1)(l+1)-th tranche is quoted via up-front payment (with fixed spread s[al+1,bl+1]s^{[a\_{l+1},b\_{l+1}]}), uf¯N[al+1,bl+1]\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N} and uf¯N[al+1,bl+1]\underline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N} can be computed by solving the following LP problems:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | {uf¯N[al+1,bl+1]=sup{p^i​k}∈𝒫Nl∑i=1m∑k=0Ngi,k,l+1(N)​(𝐬)​p^i​kbl+1−al+1−s[al+1,bl+1]​∑i=1mD​(Ti)​(Ti−Ti−1),uf¯N[al+1,bl+1]=inf{p^i​k}∈𝒫Nl∑i=1m∑k=0Ngi,k,l+1(N)​(𝐬)​p^i​kbl+1−al+1−s[al+1,bl+1]​∑i=1mD​(Ti)​(Ti−Ti−1).\begin{cases}\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N}=\ \sup\limits\_{\{\hat{p}\_{ik}\}\in\mathcal{P}\_{N}^{l}}\frac{\sum\_{i=1}^{m}\sum\_{k=0}^{N}g\_{i,k,l+1}^{(N)}(\mathbf{s})\hat{p}\_{ik}}{{b\_{l+1}-a\_{l+1}}}-s^{[a\_{l+1},b\_{l+1}]}\sum\_{i=1}^{m}D(T\_{i})(T\_{i}-T\_{i-1}),\\ \underline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N}=\ \inf\limits\_{\{\hat{p}\_{ik}\}\in\mathcal{P}\_{N}^{l}}\frac{\sum\_{i=1}^{m}\sum\_{k=0}^{N}g\_{i,k,l+1}^{(N)}(\mathbf{s})\hat{p}\_{ik}}{{b\_{l+1}-a\_{l+1}}}-s^{[a\_{l+1},b\_{l+1}]}\sum\_{i=1}^{m}D(T\_{i})(T\_{i}-T\_{i-1}).\end{cases} |  | (26) |
* •

  If the (l+1)(l+1)-th tranche is quoted via spread (with uf[al+1,bl+1]=0\textrm{uf}^{[a\_{l+1},b\_{l+1}]}=0), s¯N[al+1,bl+1]\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N} and s¯N[al+1,bl+1]\underline{s}^{[a\_{l+1},b\_{l+1}]}\_{N} can be computed by solving the following LFP problems:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | {s¯N[al+1,bl+1]=sup{p^i​k}∈𝒫Nl∑i=1m∑k=0N∑j=0n[D​(Ti+Ti−12)−D​(Ti+Ti+12)​1{i<m}]​βj[al+1,bl+1]​hj​k(N)​p^i​k∑i=1mD​(Ti)​(Ti−Ti−1)​((bl+1−al+1)−∑j=0n∑k=0Nβj[al+1,bl+1]​hj​k(N)​p^i​k),s¯N[al+1,bl+1]=inf{p^i​k}∈𝒫Nl∑i=1m∑k=0N∑j=0n[D​(Ti+Ti−12)−D​(Ti+Ti+12)​1{i<m}]​βj[al+1,bl+1]​hj​k(N)​p^i​k∑i=1mD​(Ti)​(Ti−Ti−1)​((bl+1−al+1)−∑j=0n∑k=0Nβj[al+1,bl+1]​hj​k(N)​p^i​k).\begin{cases}\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N}=\sup\limits\_{\{\hat{p}\_{ik}\}\in\mathcal{P}\_{N}^{l}}\frac{\sum\_{i=1}^{m}\sum\_{k=0}^{N}\sum\_{j=0}^{n}\left[D\left(\frac{T\_{i}+T\_{i-1}}{2}\right)-D\left(\frac{T\_{i}+T\_{i+1}}{2}\right)1\_{\{i<m\}}\right]\beta\_{j}^{[a\_{l+1},b\_{l+1}]}h\_{jk}^{(N)}\hat{p}\_{ik}}{\sum\_{i=1}^{m}D(T\_{i})(T\_{i}-T\_{i-1})\left((b\_{l+1}-a\_{l+1})-\sum\_{j=0}^{n}\sum\_{k=0}^{N}\beta\_{j}^{[a\_{l+1},b\_{l+1}]}h\_{jk}^{(N)}\hat{p}\_{ik}\right)},\\ \underline{s}^{[a\_{l+1},b\_{l+1}]}\_{N}=\inf\limits\_{\{\hat{p}\_{ik}\}\in\mathcal{P}\_{N}^{l}}\frac{\sum\_{i=1}^{m}\sum\_{k=0}^{N}\sum\_{j=0}^{n}\left[D\left(\frac{T\_{i}+T\_{i-1}}{2}\right)-D\left(\frac{T\_{i}+T\_{i+1}}{2}\right)1\_{\{i<m\}}\right]\beta\_{j}^{[a\_{l+1},b\_{l+1}]}h\_{jk}^{(N)}\hat{p}\_{ik}}{\sum\_{i=1}^{m}D(T\_{i})(T\_{i}-T\_{i-1})\left((b\_{l+1}-a\_{l+1})-\sum\_{j=0}^{n}\sum\_{k=0}^{N}\beta\_{j}^{[a\_{l+1},b\_{l+1}]}h\_{jk}^{(N)}\hat{p}\_{ik}\right)}.\end{cases} |  | (27) |

Proposition [4.5](https://arxiv.org/html/2602.08039v1#S4.ThmProposition5 "Proposition 4.5 ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility") below establishes that these NN-dependent price ranges converge to the strong compatibility price range as NN tends to infinity.

###### Proposition 4.5

Suppose that (s[a1,b1],uf[a1,b1],…,s[al,bl],uf[al,bl])∈(𝒜l)∘(s^{[a\_{1},b\_{1}]},\textrm{uf}^{[a\_{1},b\_{1}]},\ldots,s^{[a\_{l},b\_{l}]},\textrm{uf}^{[a\_{l},b\_{l}]})\in(\mathcal{A}^{l})^{\circ} for 1≤l≤M−11\leq l\leq M-1.
Consider the (l+1)(l+1)-th tranche. If it is quoted via up-front payment, then it holds that

|  |  |  |
| --- | --- | --- |
|  | limN→+∞uf¯N[al+1,bl+1]=uf¯[al+1,bl+1]andlimN→+∞uf¯N[al+1,bl+1]=uf¯[al+1,bl+1].\lim\_{N\to+\infty}\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N}=\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\quad\text{and}\quad\lim\_{N\to+\infty}\underline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N}=\underline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}. |  |

If it is quoted via spread, then it holds that

|  |  |  |
| --- | --- | --- |
|  | limN→+∞s¯N[al+1,bl+1]=s¯[al+1,bl+1]andlimN→+∞s¯N[al+1,bl+1]=s¯[al+1,bl+1].\lim\_{N\to+\infty}\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N}=\overline{s}^{[a\_{l+1},b\_{l+1}]}\quad\text{and}\quad\lim\_{N\to+\infty}\underline{s}^{[a\_{l+1},b\_{l+1}]}\_{N}=\underline{s}^{[a\_{l+1},b\_{l+1}]}. |  |

Proof. See Section [13](https://arxiv.org/html/2602.08039v1#S13 "13 Proofs of Proposition 4.5 and Proposition 4.6") in the e-companion. □\Box

###### Remark 4.4 (Transforming LFP problems into LP problems)

The computation of s¯N[al+1,bl+1]\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N} and s¯N[al+1,bl+1]\underline{s}^{[a\_{l+1},b\_{l+1}]}\_{N} requires solving LFP problems.
These problems can be efficiently solved by transforming them into equivalent LP problems via the Charnes-Cooper transformation (Charnes and Cooper [1962](https://arxiv.org/html/2602.08039v1#bib.bib71 "Programming with linear fractional functionals")).
For an outline of the transformation procedure, see Section [14](https://arxiv.org/html/2602.08039v1#S14 "14 Transforming an LFP Problem into an LP Problem") in the e-companion.

#### 4.5.2 Our Iterative Algorithm

Based on the key ideas articulated in Section [4.5.1](https://arxiv.org/html/2602.08039v1#S4.SS5.SSS1 "4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility"), we now present the algorithm for verifying strong compatibility and constructing the corresponding copula if strong compatibility is satisfied.
Proposition [4.5](https://arxiv.org/html/2602.08039v1#S4.ThmProposition5 "Proposition 4.5 ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility") ensures that this algorithm terminates in a finite number of steps.

 



Algorithm 4.1  Verifying Strong Compatibility and Constructing a Concrete Copula

 

1. Step 1:

   Initialization.
   Choose a strictly increasing sequence of integers N1<N2<⋯N\_{1}<N\_{2}<\cdots and a tolerance ϵ>0\epsilon>0.
2. Step 2:

   Iterative Verification Across Tranches.
   Execute an outer loop from l=0l=0 to M−1M-1. For each ll, perform the following procedure to determine whether the prices of the first (l+1)(l+1) tranches are strongly compatible.

   1. Case 1:

      The (l+1)(l+1)-th tranche is quoted via spread. Perform an inner loop for y=1,2,…y=1,2,\ldots. For each yy, set N=NyN=N\_{y} and execute the following checks.

      1. (i)

         Compute the NN-dependent price range [s¯Ny[al+1,bl+1],s¯Ny[al+1,bl+1]][\underline{s}^{[a\_{l+1},b\_{l+1}]}\_{N\_{y}},\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N\_{y}}] by solving the corresponding LFP problems ([27](https://arxiv.org/html/2602.08039v1#S4.E27 "In 2nd item ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility")), which can be transformed into LP problems as mentioned in Remark [4.4](https://arxiv.org/html/2602.08039v1#S4.ThmRemark4 "Remark 4.4 (Transforming LFP problems into LP problems) ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility").
      2. (ii)

         If the market price s[al+1,bl+1]s^{[a\_{l+1},b\_{l+1}]} is within the computed NN-dependent price range [s¯Ny[al+1,bl+1],s¯Ny[al+1,bl+1]][\underline{s}^{[a\_{l+1},b\_{l+1}]}\_{N\_{y}},\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N\_{y}}], then the market prices of the first (l+1)(l+1) tranches are strongly compatible. Exit the inner loop (over yy) and move to the next tranche.
      3. (iii)

         If y>1y>1, check if the changes in bounds are within the pre-specified tolerance ϵ\epsilon, i.e., whether |s¯Ny[al+1,bl+1]−s¯Ny−1[al+1,bl+1]|<ϵ|\underline{s}^{[a\_{l+1},b\_{l+1}]}\_{N\_{y}}-\underline{s}^{[a\_{l+1},b\_{l+1}]}\_{N\_{y-1}}|<\epsilon and |s¯Ny[al+1,bl+1]−s¯Ny−1[al+1,bl+1]|<ϵ|\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N\_{y}}-\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N\_{y-1}}|<\epsilon.
         If these inequalities hold but the market price s[al+1,bl+1]s^{[a\_{l+1},b\_{l+1}]} remains outside the computed NN-dependent price range, we claim that the full set of market prices is not strongly compatible, and the whole algorithm terminates.
   2. Case 2:

      The (l+1)(l+1)-th tranche is quoted via up-front payment. The procedure is analogous to Case 1 except that all spread notations are replaced by their up-front payment counterparts and the LFP problems ([27](https://arxiv.org/html/2602.08039v1#S4.E27 "In 2nd item ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility")) in step (i) are replaced by the LP problems ([26](https://arxiv.org/html/2602.08039v1#S4.E26 "In 1st item ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility")).
3. Step 3:

   Final Construction.
   If the loop in Step 2 reports that the market prices of all MM tranches are strongly compatible, then solve the linear feasibility problem ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) using the final value of NyN\_{y} determined in the last iteration of Step 2.
   Use the resulting feasible solution to construct the generator ϕ​(u)\phi(u) as defined in ([23](https://arxiv.org/html/2602.08039v1#S4.E23 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")), immediately leading to a gamma-distorted copula CXC^{X} that achieves a perfect fit to the market prices across all tranches.

 

###### Remark 4.5 (Comparison with the Implied Copula Method of Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")))

It is instructive to compare our strong compatibility framework with the influential implied copula method of Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")). Our framework follows in their pioneering footsteps and extends their analysis along three key dimensions. First, our strong compatibility framework is far more general, including all conditionally i.i.d. copula models, with the model considered in Hull and White ([2006](https://arxiv.org/html/2602.08039v1#bib.bib6 "Valuing credit derivatives using an implied copula approach")) as a special case. Second,
our strong compatibility framework accounts for the general multi-period setting inherent
in standard CDO contracts. Third, we establish the formal theoretical condition for the existence of a conditional i.i.d. perfect-fit model and further, if it exists, develop an efficient algorithm for constructing a concrete perfect-fit copula. For more details, please see the comprehensive summary in Section [1.3](https://arxiv.org/html/2602.08039v1#S1.SS3 "1.3 Comparison with Hull and White (2006) ‣ 1 Introduction").

### 4.6 Strong Bid-Ask Compatibility

Similar to weak compatibility, the strong compatibility framework can also be extended to accommodate market bid-ask spreads.
Parallel to Definition [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmDefinition1 "Definition 3.1 (Weak Bid-Ask Compatibility) ‣ 3.5 Extension to Weak Bid-Ask Compatibility ‣ 3 Weak Compatibility"), we define “strong bid-ask compatibility” as follows.

###### Definition 4.4 (Strong Bid-Ask Compatibility)

Market bid-ask prices (𝐬b​i​d,𝐬a​s​k)(\mathbf{s}\_{bid},\mathbf{s}\_{ask}) of all MM CDO tranches are said to be *strongly bid-ask compatible* if there exists a copula C∈𝒞1C\in\mathcal{C}\_{1} such that the expected NPVs from a long protection position satisfy ([11](https://arxiv.org/html/2602.08039v1#S3.E11 "In 3.5 Extension to Weak Bid-Ask Compatibility ‣ 3 Weak Compatibility")).

The verification of strong bid-ask compatibility through a linear feasibility problem is similar to Theorem [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem1 "Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility"), as detailed in the following proposition. In addition, similar to Algorithm [4.5.2](https://arxiv.org/html/2602.08039v1#S4.SS5.SSS2 "4.5.2 Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility"), we can also develop an algorithm to verify strong bid-ask compatibility and, when satisfied, constructing a corresponding concrete copula. The details are omitted due to the similarity.

###### Proposition 4.6 (A Sufficient and Necessary Condition for Strong Bid-Ask Compatibility)

Let 𝒜bid-ask⊆ℝ4​M\mathcal{A}\_{\textrm{bid-ask}}\subseteq\mathbb{R}^{4M} denote the set of market bid-ask prices that satisfy strong bid-ask compatibility and 𝒜bid-ask∘\mathcal{A}\_{\textrm{bid-ask}}^{\circ} the interior of 𝒜bid-ask\mathcal{A}\_{\textrm{bid-ask}}.
Then for each vector (𝐬b​i​d,𝐬a​s​k)∈𝒜bid-ask∘(\mathbf{s}\_{bid},\mathbf{s}\_{ask})\!\in\!\mathcal{A}\_{\textrm{bid-ask}}^{\circ}, there exists an N∈ℕ+N\in\mathbb{N}^{+} such that the following system of linear constraints for {p^i​k}1≤i≤m,0≤k≤N\{\hat{p}\_{ik}\}\_{1\leq i\leq m,0\leq k\leq N} has a feasible solution.

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∑i=1m∑k=0Ngi​k​l(N)​(𝐬b​i​d)​p^i​k−γ[al,bl]​(𝐬b​i​d)≥0for 1≤l≤M,∑i=1m∑k=0Ngi​k​l(N)​(𝐬a​s​k)​p^i​k−γ[al,bl]​(𝐬a​s​k)≤0for 1≤l≤M,∑k=0Np^i​k=1for 1≤i≤m,∑k=0Nk​p^i​k=N​F​(Ti)for 1≤i≤m,∑j≥kp^i​j≤∑j≥kp^i+1,jfor 1≤i≤m−1 and 1≤k≤N,p^i​k≥0for 1≤i≤m and 0≤k≤N.\begin{cases}\sum\_{i=1}^{m}\sum\_{k=0}^{N}g\_{ikl}^{(N)}(\mathbf{s}\_{bid})\hat{p}\_{ik}-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}\_{bid})\geq 0\quad&\quad\text{{for} $1\leq l\leq M$},\\ \sum\_{i=1}^{m}\sum\_{k=0}^{N}g\_{ikl}^{(N)}(\mathbf{s}\_{ask})\hat{p}\_{ik}-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}\_{ask})\leq 0\quad&\quad\text{{for} $1\leq l\leq M$},\\ \sum\_{k=0}^{N}\hat{p}\_{ik}=1\,&\quad\text{{for} $1\leq i\leq m$},\\ \sum\_{k=0}^{N}k\hat{p}\_{ik}=NF(T\_{i})\,&\quad\text{{for} $1\leq i\leq m$},\\ \sum\_{j\geq k}\hat{p}\_{ij}\leq\sum\_{j\geq k}\hat{p}\_{i+1,j}\,&\quad\text{{for} $1\leq i\leq m-1$ {and} $1\leq k\leq N$},\\ \hat{p}\_{ik}\geq 0\,&\quad\text{{for} $1\leq i\leq m$ {and} $0\leq k\leq N$}.\\ \end{cases} |  | (28) |

Conversely, if there exists an N∈ℕ+N\in\mathbb{N}^{+} such that the system of linear constraints ([28](https://arxiv.org/html/2602.08039v1#S4.E28 "In Proposition 4.6 (A Sufficient and Necessary Condition for Strong Bid-Ask Compatibility) ‣ 4.6 Strong Bid-Ask Compatibility ‣ 4 Strong Compatibility")) has a feasible solution, then (𝐬b​i​d,𝐬a​s​k)(\mathbf{s}\_{bid},\mathbf{s}\_{ask}) satisfies strong bid-ask compatibility.

Proof. See Section [13](https://arxiv.org/html/2602.08039v1#S13 "13 Proofs of Proposition 4.5 and Proposition 4.6") in the e-companion. □\Box

## 5 Applications of Weak Compatibility and Strong Compatibility

### 5.1 Applications of Weak Compatibility

Weak compatibility not only ensures a consistent, arbitrage-free pricing framework for the observed CDO tranches but also has important practical applications.
Specifically, satisfying weak compatibility enables construction of a model-independent strategy for hedging CDO tranches as well as the derivation of model-independent bounds for nonstandard credit derivatives tied to the same underlying portfolio, such as CDOs with nonstandard attachment and detachment points.

#### 5.1.1 A Model-Independent Hedging Strategy

For managers of CDO portfolios, one of the most critical risk management activities is hedging against shifts in the underlying CDS index spread.
This practice, known as index spread delta hedging, is a cornerstone of CDO risk management; see, e.g., Chen and Glasserman ([2008](https://arxiv.org/html/2602.08039v1#bib.bib60 "Sensitivity estimates for portfolio credit derivatives using Monte Carlo")), Frey and Backhaus ([2010](https://arxiv.org/html/2602.08039v1#bib.bib77 "Dynamic hedging of synthetic CDO tranches with spread risk and default contagion")), and Masol and Schoutens ([2011](https://arxiv.org/html/2602.08039v1#bib.bib46 "Comparing alternative Lévy base correlation models for pricing and hedging CDO tranches")).
The primary objective is to compute the spread delta δ[al,bl]\delta^{[a\_{l},b\_{l}]} (for 1≤l≤M1\leq l\leq M), which represents the notional amount of the CDS index required to hedge a position in a CDO tranche. It is defined as the ratio of the change in the CDO tranche’s value (i.e., Δ​v[al,bl]\Delta v^{[a\_{l},b\_{l}]}) to the change in the CDS index’s value (denoted by Δ​vC​D​S\Delta v^{CDS}) for a small shift in the CDS index spread, i.e., δ[al,bl]:=Δ​v[al,bl]Δ​vC​D​S\delta^{[a\_{l},b\_{l}]}:=\frac{\Delta v^{[a\_{l},b\_{l}]}}{\Delta v^{CDS}}.

The central challenge in computing the spread delta is to determine how the underlying default distribution changes in response to a shift in the CDS index spread. Our approach frames this as an information updating problem. We begin with a market-implied DPM Q^\hat{Q} that is supposed to be consistent with the initial market prices. When the CDS index spread shifts, this prior distribution must be updated to a new posterior distribution Q~\tilde{Q}. Intuitively, a small shift in the CDS index spread should not result in a substantial deviation of the new posterior distribution from the prior one.
Accordingly, we quantify the distribution deviation using the widely adopted relative entropy (also known as Kullback-Leibler divergence; Kullback and Leibler [1951](https://arxiv.org/html/2602.08039v1#bib.bib75 "On information and sufficiency")) and select the posterior distribution that minimizes its relative entropy with the prior.

Algorithm [5.1.1](https://arxiv.org/html/2602.08039v1#S5.SS1.SSS1 "5.1.1 A Model-Independent Hedging Strategy ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility") below provides specific procedures for calculating the spread delta, which in turn leads to a practically implementable, model-independent hedging strategy immediately. The empirical studies conducted in Section [6.2.1](https://arxiv.org/html/2602.08039v1#S6.SS2.SSS1 "6.2.1 Constructing Effective Model-Independent Hedging Strategies for CDO Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies") will illustrate its effective hedging performance.

 



Algorithm 5.1  Calculating the Model-Independent Index Spread Delta

 

1. Step 1:

   Apply a small shift (e.g., 11bp) to the CDS index spread and derive the new market-implied marginal default distribution function F~​(⋅)\tilde{F}(\cdot) using the standard market practice (see Section [15](https://arxiv.org/html/2602.08039v1#S15 "15 Standard Methods for CDS Index Calculations") in the e-companion for the details of this standard market practice; one may also see, e.g., Hull [2022](https://arxiv.org/html/2602.08039v1#bib.bib63 "Options, futures, and other derivatives")).
2. Step 2:

   Solve the following convex optimization problem (it essentially minimizes the posterior DPM’s relative entropy with the prior DPM) to find the posterior DPM Q~={q~i​j}1≤i≤m,0≤j≤n\tilde{Q}=\{\tilde{q}\_{ij}\}\_{1\leq i\leq m,0\leq j\leq n}. Here the term ϵ\epsilon is a small positive constant (e.g., 10−2010^{-20}) introduced to prevent division by zero.
     
   Minimize:

   |  |  |  |
   | --- | --- | --- |
   |  | ∑i=1m∑j=0nq~i​j​log⁡(q~i​jq^i​j+ϵ)\sum\_{i=1}^{m}\sum\_{j=0}^{n}\tilde{q}\_{ij}\log\left(\frac{\tilde{q}\_{ij}}{\hat{q}\_{ij}+\epsilon}\right) |  |

   Subject to:

   |  |  |  |
   | --- | --- | --- |
   |  | {∑j=0nq~i​j=1,for 1≤i≤m,∑j=0nj​q~i​j=n​F~​(Ti),for 1≤i≤m,∑k≥jq~i​k≤∑k≥jq~i+1,kfor 1≤i≤m−1 and 0≤j≤n,q~i​j≥0for 1≤i≤m and 0≤j≤n.\begin{cases}\sum\_{j=0}^{n}\tilde{q}\_{ij}=1,&\quad\text{for $1\leq i\leq m$},\\ \sum\_{j=0}^{n}j\tilde{q}\_{ij}=n\tilde{F}(T\_{i}),&\quad\text{for $1\leq i\leq m$},\\ \sum\_{k\geq j}\tilde{q}\_{ik}\leq\sum\_{k\geq j}\tilde{q}\_{i+1,k}&\quad\text{for $1\leq i\leq m-1$ and $0\leq j\leq n$},\\ \tilde{q}\_{ij}\geq 0&\quad\text{for $1\leq i\leq m$ and $0\leq j\leq n$.}\end{cases} |  |
3. Step 3:

   Calculate the change in the CDO tranche’s value using the prior and posterior DPMs: Δ​v[al,bl]=𝝀[al,bl]​(𝐬)′​(Q~−Q^)​𝜷[al,bl]\Delta v^{[a\_{l},b\_{l}]}=\bm{\lambda}^{[a\_{l},b\_{l}]}(\mathbf{s})^{\prime}(\tilde{Q}-\hat{Q})\bm{\beta}^{[a\_{l},b\_{l}]}.
   Then calculate the corresponding change in the CDS index’s value Δ​vC​D​S\Delta v^{CDS} using the standard method (see Section [15](https://arxiv.org/html/2602.08039v1#S15 "15 Standard Methods for CDS Index Calculations") in the e-companion for the details of this standard method; one may also refer to, e.g., Cont and Kan [2011](https://arxiv.org/html/2602.08039v1#bib.bib61 "Dynamic hedging of portfolio credit derivatives")).
4. Step 4:

   Compute the spread delta as the ratio of the two value changes:
   δ[al,bl]=Δ​v[al,bl]Δ​vC​D​S.\delta^{[a\_{l},b\_{l}]}=\frac{\Delta v^{[a\_{l},b\_{l}]}}{\Delta v^{CDS}}.

#### 5.1.2 Model-Independent and Arbitrage-Free Pricing Bounds for CDOs with Nonstandard Attachment and Detachment Points

A key application of the weak compatibility framework is to determine the arbitrage-free price range for a nonstandard CDO tranche [a~,b~][\tilde{a},\tilde{b}] with the nonstandard attachment point a~\tilde{a} and detachment point b~\tilde{b}. Furthermore, this pricing approach is model-independent because it relies only on the observed market prices of standard tranches, without depending on any specific parametric copula model.

The core idea is that the theoretical price of the aforementioned nonstandard tranche is determined by the underlying DPM. Since the market prices of standard tranches only constrain the DPM to a feasible set 𝒬\mathcal{Q} rather than determining it uniquely, the price of the nonstandard tranche is not a single value but a range. This range is bounded by the maximum and minimum possible values of the tranche’s theoretical price, optimized over all valid DPMs within the feasible set 𝒬\mathcal{Q}. This range is critically important for market participants: a market quote for the nonstandard tranche that falls outside this range implies an arbitrage opportunity.

The following Algorithm [5.1.2](https://arxiv.org/html/2602.08039v1#S5.SS1.SSS2 "5.1.2 Model-Independent and Arbitrage-Free Pricing Bounds for CDOs with Nonstandard Attachment and Detachment Points ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility") outlines the procedures for computing these price bounds, and some numerical results will be provided in Section [6.3.1](https://arxiv.org/html/2602.08039v1#S6.SS3.SSS1 "6.3.1 Pricing CDO Tranches with Nonstandard Attachment and Detachment Points ‣ 6.3 Pricing Nonstandard CDOs ‣ 6 Empirical Studies").

 



Algorithm 5.2  Calculating Model-Independent and Arbitrage-Free Pricing Bounds

 

1. Case 1:

   The tranche is quoted via spread.
   In such a case, the maximum market-implied spread s¯[a~,b~]\overline{s}^{[\tilde{a},\tilde{b}]} is given by the optimal value of the following LFP problem:

   |  |  |  |
   | --- | --- | --- |
   |  | s¯[a~,b~]=supQ^∈𝒬∑i=1m∑j=0n[D​(Ti+Ti−12)−D​(Ti+Ti+12)​1{i<m}]​βj[a~,b~]​q^i​j∑i=1mD​(Ti)​(Ti−Ti−1)​(b~−a~−∑j=0nβj[a~,b~]​q^i​j),\overline{s}^{[\tilde{a},\tilde{b}]}=\sup\_{\hat{Q}\in\mathcal{Q}}\frac{\sum\_{i=1}^{m}\sum\_{j=0}^{n}[D(\frac{T\_{i}+T\_{i-1}}{2})-D(\frac{T\_{i}+T\_{i+1}}{2})1\_{\{i<m\}}]\beta\_{j}^{[\tilde{a},\tilde{b}]}\hat{q}\_{ij}}{\sum\_{i=1}^{m}D(T\_{i})(T\_{i}-T\_{i-1})(\tilde{b}-\tilde{a}-\sum\_{j=0}^{n}\beta\_{j}^{[\tilde{a},\tilde{b}]}\hat{q}\_{ij})}, |  |

   where βj[a~,b~]=(j​(1−R)n−a~)+−(j​(1−R)n−b~)+\beta\_{j}^{[\tilde{a},\tilde{b}]}=\left(\frac{j(1-R)}{n}-\tilde{a}\right)^{+}-\left(\frac{j(1-R)}{n}-\tilde{b}\right)^{+} for 0≤j≤n.0\leq j\leq n.
   The minimum market-implied spread s¯[a~,b~]\underline{s}^{[\tilde{a},\tilde{b}]} can be identified by replacing sup\sup with inf\inf.
   We can transform these LFP problems into the LP problems via the Charnes-Cooper transformation (see Remark [4.4](https://arxiv.org/html/2602.08039v1#S4.ThmRemark4 "Remark 4.4 (Transforming LFP problems into LP problems) ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility") and Section [14](https://arxiv.org/html/2602.08039v1#S14 "14 Transforming an LFP Problem into an LP Problem") in the e-companion for the detail of this transformation), and then obtain the model-independent and arbitrage-free pricing bounds by solving the resulting LP problems.
2. Case 2:

   The tranche is quoted via up-front payment.
   In such a case, the maximum market-implied up-front payment uf¯[a~,b~]\overline{\textrm{uf}}^{[\tilde{a},\tilde{b}]} is given by the optimal value of the following LP problem:

   |  |  |  |
   | --- | --- | --- |
   |  | uf¯[a~,b~]=supQ^∈𝒬∑i=1m∑j=0nλi[a~,b~]​βj[a~,b~]​q^i​jb~−a~−s[a~,b~]​∑i=1nD​(Ti)​(Ti−Ti−1),\overline{\textrm{uf}}^{[\tilde{a},\tilde{b}]}=\sup\_{\hat{Q}\in\mathcal{Q}}\frac{\sum\_{i=1}^{m}\sum\_{j=0}^{n}\lambda\_{i}^{[\tilde{a},\tilde{b}]}\beta\_{j}^{[\tilde{a},\tilde{b}]}\hat{q}\_{ij}}{\tilde{b}-\tilde{a}}-s^{[\tilde{a},\tilde{b}]}\sum\_{i=1}^{n}D(T\_{i})(T\_{i}-T\_{i-1}), |  |

   where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | λi[a~,b~]=s[a~,b~]​D​(Ti)​(Ti−Ti−1)+D​(Ti+Ti−12)−D​(Ti+1+Ti2)​𝟏{i<m}​for​i=1,…,m.\lambda\_{i}^{[\tilde{a},\tilde{b}]}=s^{[\tilde{a},\tilde{b}]}D(T\_{i})(T\_{i}-T\_{i-1})+D\left(\frac{T\_{i}+T\_{i-1}}{2}\right)-D\left(\frac{T\_{i+1}+T\_{i}}{2}\right)\mathbf{1}\_{\{i<m\}}\,\text{for}\,i=1,\ldots,m. |  | (29) |

   The minimum market-implied up-front payment uf¯[a~,b~]\underline{\textrm{uf}}^{[\tilde{a},\tilde{b}]} can be found by replacing sup\sup with inf\inf.
   Solving these LP problems then yields the model-independent and arbitrage-free pricing bounds.

 

###### Remark 5.1

(Model-Independent and Arbitrage-Free Pricing of Other Portfolio Credit Derivatives)
The model independent and arbitrage-free pricing approach presented above using the weak compatibility framework is not limited to pricing nonstandard CDO tranches with nonstandard attachment and detachment points. Rather, it applies to pricing any claim contingent solely on the default count process NtN\_{t} at times TiT\_{i}. Indeed,
the elements q^i​j\hat{q}\_{ij} of any feasible DPM Q^\hat{Q} represent the risk-neutral probabilities ℙ​(NTi=j)\mathbb{P}(N\_{T\_{i}}=j). Therefore, this allows for model-independent and arbitrage-free pricing of various other portfolio credit derivatives, such as the kk-th to default CDSs (basket default swaps) and options on the number of defaults.

### 5.2 Applications of Strong Compatibility

The strong compatibility framework offers effective tools for a range of applications.
The conditionally i.i.d. structure, which is central to strong compatibility, is the key enabler for these applications as it enables the separation of systematic risk (the common factors) from idiosyncratic risk (the individual defaults).
We would like to elaborate on two examples: estimating loss or NPV distributions for risk management, and pricing CDOs with a nonstandard number of underlying names.

#### 5.2.1 Estimating NPV Distributions for Risk Management

For the purpose of risk management, it is essential to analyze the loss or NPV distribution of a portfolio composed of positions in multiple CDO tranches. The calibrated gamma-distorted copula is particularly well-suited for this task. This is because it models the dependence among defaults through a common set of stochastic factors and conditional on these common factors, the defaults then possess an i.i.d. structure, thereby facilitating the evaluation of the NPV distributions of all CDO tranches through simulation.

The following Algorithm [5.2.1](https://arxiv.org/html/2602.08039v1#S5.SS2.SSS1 "5.2.1 Estimating NPV Distributions for Risk Management ‣ 5.2 Applications of Strong Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility") provides detailed procedures for simulating the NPV distributions of all CDO tranches.
This algorithm can be directly applied to estimate the NPV distribution of a trading portfolio with any combination of long or short positions in various CDO tranches and the underlying CDS index. Some numerical results will be provided in Section [6.2.2](https://arxiv.org/html/2602.08039v1#S6.SS2.SSS2 "6.2.2 NPV Distributions for CDO Tranches and Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies").

 



Algorithm 5.3  Simulating NPV Distributions of the CDO Tranches

 

1. Step 1:

   Simulate Random Drivers.
   Sample n+1n+1 independent uniform random variables U,U1,…,Un∼𝒰​(0,1)U,U\_{1},\ldots,U\_{n}\sim\mathcal{U}(0,1).
   Moreover, sample two independent paths of gamma processes {ξt}\{\xi\_{t}\} and {ηt}\{\eta\_{t}\}.
2. Step 2:

   Construct a Stochastic Distortion Path.
   Use a feasible solution {p^i​k}\{\hat{p}\_{ik}\} of ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) and the sampled random variable UU to construct a single path for the generator {ϕ​(u):0≤u≤1}\{{\phi}(u):0\leq u\leq 1\} as defined in ([23](https://arxiv.org/html/2602.08039v1#S4.E23 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")). Then, construct the corresponding path for the stochastic distortion process:
   X​(F​(t))=ξϕ​(F​(t))ξϕ​(F​(t))+ηN−ϕ​(F​(t)).X(F(t))=\frac{\xi\_{{\phi}(F(t))}}{\xi\_{{\phi}(F(t))}+\eta\_{N-{\phi}(F(t))}}.
3. Step 3:

   Simulate Defaults and Tranche Values.
   For each time point t∈{T1,…,Tm}t\in\{T\_{1},...,T\_{m}\}, calculate the aggregate number of defaults:
   Nt=∑j=1n1{Uj≤X​(F​(t))}.N\_{t}=\sum\_{j=1}^{n}1\_{\{U\_{j}\leq X(F(t))\}}.
   Then, calculate the realized NPV for each tranche [al,bl][a\_{l},b\_{l}] based on this simulated path of default counts:

   |  |  |  |
   | --- | --- | --- |
   |  | V[al,bl]=∑i=1mλi[al,bl]​(𝐬)​[((1−R)​NTin−al)+−((1−R)​NTin−bl)+]−γ[al,bl]​(𝐬).V^{[a\_{l},b\_{l}]}=\sum\_{i=1}^{m}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})\left[\left(\frac{(1-R)N\_{T\_{i}}}{n}-a\_{l}\right)^{+}-\left(\frac{(1-R)N\_{T\_{i}}}{n}-b\_{l}\right)^{+}\right]-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}). |  |

#### 5.2.2 Pricing CDOs with a Nonstandard Number of Underlying Names

The strong compatibility framework provides a consistent method for valuing CDOs on a portfolio with a nonstandard number of underlying names n~\tilde{n}.
Let NN be a sufficiently large integer such that ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) has a feasible solution, and denote its feasible set by 𝒫N\mathcal{P}\_{N}.
𝒫N\mathcal{P}\_{N} represents the calibrated systematic risk profile, which is
not inherently tied to the portfolio’s original size nn.
Thus, it can be consistently applied to a CDO tranche [a~,b~][\tilde{a},\tilde{b}] with a nonstandard number of underlying names n~\tilde{n}, provided that the new portfolio shares the same systematic risk profile.

Algorithm [5.2.2](https://arxiv.org/html/2602.08039v1#S5.SS2.SSS2 "5.2.2 Pricing CDOs with a Nonstandard Number of Underlying Names ‣ 5.2 Applications of Strong Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility") below provides detailed procedures regarding how to calculate price bounds for CDOs with a nonstandard number of underlying names. This algorithm can be readily extended to price other credit derivatives such as basket default swaps written on a nonstandard portfolio composed of CDO tranches with a nonstandard number of underlying names.

 



Algorithm 5.4  (Calculating Price Bounds for CDOs with a Nonstandard Number of Underlying Names)

 

1. Case 1:

   The tranche is quoted via spread.
   In such a case, the maximum market-implied spread s¯[a~,b~]\overline{s}^{[\tilde{a},\tilde{b}]} is given by the optimal value of the following LFP problem:

   |  |  |  |
   | --- | --- | --- |
   |  | s¯[a~,b~]=sup{p^i​k}∈𝒫N∑i=1m∑k=0N∑j=0n~[D​(Ti+Ti−12)−D​(Ti+Ti+12)​1{i<m}]​β~j[a~,b~]​h~j​k(N)​p^i​k∑i=1mD​(Ti)​(Ti−Ti−1)​(b~−a~−∑j=0n~∑k=0Nβ~j[a~,b~]​h~j​k(N)​p^i​k),\overline{s}^{[\tilde{a},\tilde{b}]}=\sup\_{\{\hat{p}\_{ik}\}\in\mathcal{P}\_{N}}\frac{\sum\_{i=1}^{m}\sum\_{k=0}^{N}\sum\_{j=0}^{\tilde{n}}[D(\frac{T\_{i}+T\_{i-1}}{2})-D(\frac{T\_{i}+T\_{i+1}}{2})1\_{\{i<m\}}]\tilde{\beta}\_{j}^{[\tilde{a},\tilde{b}]}\tilde{h}\_{jk}^{(N)}\hat{p}\_{ik}}{\sum\_{i=1}^{m}D(T\_{i})(T\_{i}-T\_{i-1})(\tilde{b}-\tilde{a}-\sum\_{j=0}^{\tilde{n}}\sum\_{k=0}^{N}\tilde{\beta}\_{j}^{[\tilde{a},\tilde{b}]}\tilde{h}\_{jk}^{(N)}\hat{p}\_{ik})}, |  |

   where β~j[a~,b~]=(j​(1−R)n~−a~)+−(j​(1−R)n~−b~)+\tilde{\beta}\_{j}^{[\tilde{a},\tilde{b}]}=\left(\frac{j(1-R)}{\tilde{n}}-\tilde{a}\right)^{+}-\left(\frac{j(1-R)}{\tilde{n}}-\tilde{b}\right)^{+} for 0≤j≤n~0\leq j\leq\tilde{n},
   h~j​0(N):=𝟏{j=0}\tilde{h}\_{j0}^{(N)}:=\mathbf{1}\_{\{j=0\}} for 0≤j≤n~0\leq j\leq\tilde{n},
   h~j​k(N):=(n~j)​B​(k+j,N+n~−k−j)B​(k,N−k)\tilde{h}\_{jk}^{(N)}:=\binom{\tilde{n}}{j}\frac{\mathrm{B}(k+j,N+\tilde{n}-k-j)}{\mathrm{B}(k,N-k)} for 0≤j≤n~0\leq j\leq\tilde{n} and 1≤k≤N−11\leq k\leq N-1, and
   h~j​N(N):=𝟏{j=n~}\tilde{h}\_{jN}^{(N)}:=\mathbf{1}\_{\{j=\tilde{n}\}} for 0≤j≤n~0\leq j\leq\tilde{n}.
   The minimum market-implied spread s¯[a~,b~]\underline{s}^{[\tilde{a},\tilde{b}]} can be identified by replacing sup\sup with inf\inf.
   We can transform these LFP problems into the LP problems via the Charnes-Cooper transformation (see Remark [4.4](https://arxiv.org/html/2602.08039v1#S4.ThmRemark4 "Remark 4.4 (Transforming LFP problems into LP problems) ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility") and Section [14](https://arxiv.org/html/2602.08039v1#S14 "14 Transforming an LFP Problem into an LP Problem") in the e-companion for the detail of this transformation), and then obtain the price bounds by solving the resulting LP problems.
2. Case 2:

   The tranche is quoted via up-front payment.
   In such a case, the maximum market-implied up-front payment uf¯[a~,b~]\overline{\textrm{uf}}^{[\tilde{a},\tilde{b}]} is given by the optimal value of the following LP problem:

   |  |  |  |
   | --- | --- | --- |
   |  | uf¯[a~,b~]=sup{p^i​k}∈𝒫N∑i=1m∑j=0n∑k=0Nλi[a~,b~]​β~j[a~,b~]​h~j​k(N)​p^i​kb~−a~−s[a~,b~]​∑i=1mD​(Ti)​(Ti−Ti−1),\overline{\textrm{uf}}^{[\tilde{a},\tilde{b}]}=\sup\_{\{\hat{p}\_{ik}\}\in\mathcal{P}\_{N}}\frac{\sum\_{i=1}^{m}\sum\_{j=0}^{n}\sum\_{k=0}^{N}\lambda\_{i}^{[\tilde{a},\tilde{b}]}\tilde{\beta}\_{j}^{[\tilde{a},\tilde{b}]}\tilde{h}\_{jk}^{(N)}\hat{p}\_{ik}}{\tilde{b}-\tilde{a}}-s^{[\tilde{a},\tilde{b}]}\sum\_{i=1}^{m}D(T\_{i})(T\_{i}-T\_{i-1}), |  |

   where λi[a~,b~]\lambda\_{i}^{[\tilde{a},\tilde{b}]} is defined as in ([29](https://arxiv.org/html/2602.08039v1#S5.E29 "In item Case 2: ‣ 5.1.2 Model-Independent and Arbitrage-Free Pricing Bounds for CDOs with Nonstandard Attachment and Detachment Points ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility")).
   The minimum market-implied up-front payment uf¯[a~,b~]\underline{\textrm{uf}}^{[\tilde{a},\tilde{b}]} can be identified by replacing sup\sup with inf\inf.
   Solving these LP problems yields the price bounds immediately.

## 6 Empirical Studies

In this section, we present empirical studies on the practical applications of both the weak and strong compatibility frameworks, illustrating how they can be utilized in risk management and the pricing of nonstandard credit derivatives.

### 6.1 Data and Verification of Compatibility

#### 6.1.1 Data

We use the market data for the iTraxx Markit Europe S42 5-year tranches on March 28, 2025, which reference 125 names. This CDO comprises four tranches: [0%,3%][0\%,3\%], [3%,6%][3\%,6\%], [6%,12%][6\%,12\%], and [12%,100%][12\%,100\%].
The first two tranches are quoted by up-front payments with a running spread of 100100 bps, while the last two are quoted by tranche spreads with an up-front payment of zero; see Table [2](https://arxiv.org/html/2602.08039v1#S6.T2 "Table 2 ‣ 6.1.1 Data ‣ 6.1 Data and Verification of Compatibility ‣ 6 Empirical Studies") for the corresponding market quotes of these tranches.

Table 2:  Market Quotes for the iTraxx Markit Europe S42 5-Year Tranches on March 28, 2025

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Tranche | [0%, 3%] | [3%, 6%] | [6%, 12%] | [12%, 100%] |
| Market Quote | 28.438% | 4.531% | 106.32 bps | 27.44 bps |

*Notes.*
The first two tranches are quoted by up-front payments with a running spread of 100100 bps, while the last two are quoted by tranche spreads with an up-front payment of zero.

The spread for the iTraxx Markit Europe S38 CDS index is sidx=58s^{\rm idx}=58 bps on March 28, 2025. The marginal distribution F​(⋅)F(\cdot) of the default times is calculated from this index spread using the standard market practice (see Section [15](https://arxiv.org/html/2602.08039v1#S15 "15 Standard Methods for CDS Index Calculations") in the e-companion or Hull [2022](https://arxiv.org/html/2602.08039v1#bib.bib63 "Options, futures, and other derivatives") for the details).
In addition, following the standard assumption in the literature (e.g., Schloegl and O’Kane [2005](https://arxiv.org/html/2602.08039v1#bib.bib23 "A note on the large homogeneous portfolio approximation with the student-t copula")), we assume a constant recovery rate R=0.4R=0.4. The risk-free interest rate rr is derived from the Euro OIS curve based on the Euro Short-Term Rate (€STR); for March 28, 2025, this rate is r=2.417%r=2.417\%.
All the LP problems in the empirical studies are solved using the CVXPY package in Python.

#### 6.1.2 Verification of Weak Compatibility and Strong Compatibility

We first apply Theorems [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem1 "Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility") and [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem1 "Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") to verify whether the market prices on March 28, 2025 satisfy weak and strong compatibility.
The results show that for the market prices on this date, the linear feasibility problems ([8](https://arxiv.org/html/2602.08039v1#S3.E8 "In Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")) and ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) (with N=100N=100) both have feasible solutions.
Therefore, we conclude that the market prices on this date satisfy both weak and strong compatibility.

Next, we conduct a further analysis to identify the boundaries of strong compatibility.
Specifically, we fix the market prices of three of the four standard tranches and then solve for the strong compatibility price range of the remaining tranche.As discussed in Section [4.5.1](https://arxiv.org/html/2602.08039v1#S4.SS5.SSS1 "4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility"), this strong compatibility price range given by ([25](https://arxiv.org/html/2602.08039v1#S4.E25 "In 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility")) is not directly computable.
Instead, we can compute a sequence of NN-dependent price ranges, which convergences to the strong compatibility price range as NN tends to infinity, as shown in Proposition [4.5](https://arxiv.org/html/2602.08039v1#S4.ThmProposition5 "Proposition 4.5 ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility").

Table [3](https://arxiv.org/html/2602.08039v1#S6.T3 "Table 3 ‣ 6.1.2 Verification of Weak Compatibility and Strong Compatibility ‣ 6.1 Data and Verification of Compatibility ‣ 6 Empirical Studies") presents the NN-dependent price ranges for each tranche corresponding to different values of the gamma distortion parameter NN. Two observations emerge. First, the actual market price for each tranche, which is given in Table [2](https://arxiv.org/html/2602.08039v1#S6.T2 "Table 2 ‣ 6.1.1 Data ‣ 6.1 Data and Verification of Compatibility ‣ 6 Empirical Studies"), falls within the corresponding NN-dependent price range for any NN used in Table [3](https://arxiv.org/html/2602.08039v1#S6.T3 "Table 3 ‣ 6.1.2 Verification of Weak Compatibility and Strong Compatibility ‣ 6.1 Data and Verification of Compatibility ‣ 6 Empirical Studies"), reaffirming that the market prices on this day are strongly compatible.
Second, the calculated NN-dependent price ranges stabilize quickly as NN increases, indicating a fast convergence. Then the calculated NN-dependent price range for a sufficiently large NN can be regarded approximately as the strong compatibility price range.

The above analysis on the strong compatibility price ranges demonstrates how to determine whether a price of a specific tranche is strongly compatible with the rest of the market prices. Indeed, any price within the computed strong compatibility price range is strongly compatible with the fixed market prices of the other three tranches.

Table 3:  NN-Dependent Price Ranges for the Four Tranches for Different Values of the Gamma Distortion Parameter NN

| Tranche | [0%, 3%] | [3%, 6%] | [6%, 12%] | [12%, 100%] |
| --- | --- | --- | --- | --- |
| N=50N=50 | [28.279%, 28.936%] | [4.372%, 5.030%] | [104.57, 111.78] bps | [27.33, 27.79] bps |
| N=75N=75 | [28.277%, 28.939%] | [4.371%, 5.033%] | [104.56, 111.83] bps | [27.33, 27.80] bps |
| N=100N=100 | [28.276%, 28.941%] | [4.369%, 5.034%] | [104.55, 111.87] bps | [27.32, 27.80] bps |
| N=125N=125 | [28.275%, 28.941%] | [4.368%, 5.034%] | [104.55, 111.89] bps | [27.32, 27.80] bps |
| N=150N=150 | [28.274%, 28.942%] | [4.368%, 5.035%] | [104.54, 111.91] bps | [27.32, 27.80] bps |
| N=175N=175 | [28.274%, 28.942%] | [4.367%, 5.036%] | [104.53, 111.92] bps | [27.32, 27.80] bps |
| N=200N=200 | [28.273%, 28.942%] | [4.367%, 5.036%] | [104.53, 111.92] bps | [27.32, 27.80] bps |

*Notes.*
The calculated NN-dependent price ranges stabilize quickly as NN increases, indicating a fast convergence. Then the calculated NN-dependent price range for a sufficiently large NN can be regarded approximately as the strong compatibility price range. Any price within each strong compatibility price range is strongly compatible with the fixed market prices of the other three tranches.

### 6.2 Risk Management for CDO Portfolios

#### 6.2.1 Constructing Effective Model-Independent Hedging Strategies for CDO Portfolios

To construct a hedging strategy for CDO portfolios, it suffices to develop a hedging strategy for each CDO tranche. By applying Algorithm [5.1.1](https://arxiv.org/html/2602.08039v1#S5.SS1.SSS1 "5.1.1 A Model-Independent Hedging Strategy ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility") developed in Section [5.1.1](https://arxiv.org/html/2602.08039v1#S5.SS1.SSS1 "5.1.1 A Model-Independent Hedging Strategy ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility"), we can compute the index spread delta δ[al,bl]\delta^{[a\_{l},b\_{l}]} for each tranche, thereby immediately yielding a model-independent hedging strategy. For comparison, we also compute the index spread deltas for all tranches using a standard Gaussian copula model. This standard Gaussian copula model serves as an appropriate benchmark because the corresponding index spread deltas are often very similar to those obtained from more complex dynamic models. For instance, Cont and Kan ([2011](https://arxiv.org/html/2602.08039v1#bib.bib61 "Dynamic hedging of portfolio credit derivatives")) demonstrate that an affine jump-diffusion model and a top-down local intensity model produce index spread deltas remarkably close to those of the Gaussian copula model.

Figure [2](https://arxiv.org/html/2602.08039v1#S6.F2 "Figure 2 ‣ 6.2.1 Constructing Effective Model-Independent Hedging Strategies for CDO Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies") presents the index spread deltas—calculated for March 28, 2025 using our model-independent method and the Gaussian copula model—as well as the corresponding index spread deltas per unit width. The results highlight two advantages of our model-independent method, both of which align with financial intuition.

First, the sum of the index spread deltas across the four tranches derived from our model-independent method is approximately one (0.1970+0.1357+0.1554+0.5071=0.99520.1970+0.1357+0.1554+0.5071=0.9952). This is consistent with the theoretical expectation that a portfolio consisting of a long position in all tranches of the CDO, hedged with a short position in the underlying CDS index, should be nearly risk-free. In contrast, the sum of the index spread deltas across the four tranches calculated from the Gaussian copula model is 0.59920.5992, which deviates significantly from this intuitive principle.

Second, our model-independent method correctly captures the seniority-based risk structure. Financial intuition dictates that the index spread delta per unit width should decrease as tranche seniority increases. The right panel of Figure [2](https://arxiv.org/html/2602.08039v1#S6.F2 "Figure 2 ‣ 6.2.1 Constructing Effective Model-Independent Hedging Strategies for CDO Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies") confirms that our method meets this expectation. In contrast, the Gaussian copula model fails this test. Its index spread delta per unit width is non-monotonic, counter-intuitively implying that the senior mezzanine tranche is more sensitive than the junior mezzanine tranche. This further underscores the capability of our model-independent approach to generate sensitivities consistent with the economic realities of CDO capital structures.

Figure 2: Comparison of Index Spread Deltas (Left Panel) and Index Spread Deltas per Unit Width (Right Panel) for March 28, 2025 between Our Model-Independent Method (“This Study”) and the Gaussian Copula Model (“Gaussian”)

![Refer to caption](x2.png)

![Refer to caption](x3.png)

*Notes.*
This figure presents the index spread deltas (left panel)—calculated for March 28, 2025 using our model-independent method and the Gaussian copula model—as well as the corresponding index spread deltas per unit width (right panel). The results highlight two advantages of our model-independent method, both of which align with financial intuition. First, the sum of the index spread deltas across the four tranches derived from our model-independent method is approximately one (0.99520.9952), while the sum calculated from the Gaussian copula model is 0.59920.5992. Second, our model-independent method correctly captures the seniority-based risk structure;
the index spread delta per unit width exhibits a monotonic decrease from the equity tranche to the super-senior tranche. In contrast, the Gaussian copula model fails this test.




Figure 3: Hedging Performance of Our Model-Independent Hedging Strategy (Daily P&L of Four Tranches)

![Refer to caption](x4.png)

*Notes.*
This figure presents the daily P&L of (i) the delta-hedged portfolios resulting from our model-independent hedging strategy (the solid curves), (ii) the unhedged portfolios (the dash-dotted curves), and (iii) the delta-hedged portfolios resulting from the Gaussian copula model (the dashed curves). It clearly illustrates the significant reduction in P&L volatility achieved by our model-independent hedging strategy, when compared with the unhedged counterparts.
Furthermore, it can be seen that our model-independent hedging strategy also yields a substantially smaller P&L volatility than the Gaussian copula model.

We further conduct a backtest to empirically validate the effectiveness of our model-independent hedging strategy. Following Cont and Kan ([2011](https://arxiv.org/html/2602.08039v1#bib.bib61 "Dynamic hedging of portfolio credit derivatives")), we assess hedging performance by analyzing the daily profit and loss (P&L) of the resulting delta-hedged portfolios. Specifically, the backtest is conducted over the period from January 1, 2025 to April 30, 2025; for each day in this window, we employ our model-independent hedging strategy to construct a delta-hedged portfolio and calculate its P&L. Figure [3](https://arxiv.org/html/2602.08039v1#S6.F3 "Figure 3 ‣ 6.2.1 Constructing Effective Model-Independent Hedging Strategies for CDO Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies") presents the daily P&L of (i) the delta-hedged portfolios resulting from our model-independent hedging strategy, (ii) the unhedged portfolios, and (iii) the delta-hedged portfolios resulting from the Gaussian copula model. It clearly illustrates the significant reduction in P&L volatility achieved by our model-independent hedging strategy, when compared with the unhedged counterparts. This is particularly evident for the equity and super-senior tranches, where our hedge remains robust in controlling P&L fluctuations, even during the heightened market volatility observed in early April. Furthermore, it can be seen that our model-independent hedging strategy also yields a substantially smaller P&L volatility than the Gaussian copula model.

In addition, in the spirit of Cont and Kan ([2011](https://arxiv.org/html/2602.08039v1#bib.bib61 "Dynamic hedging of portfolio credit derivatives")), we quantitatively assess the P&L volatility of the unhedged and two aforementioned delta-hedged portfolios by calculating the standard deviations of their respective daily P&L series. The left panel of Figure [4](https://arxiv.org/html/2602.08039v1#S6.F4 "Figure 4 ‣ 6.2.1 Constructing Effective Model-Independent Hedging Strategies for CDO Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies") presents these standard deviations, and we can see that our model-independent hedging strategy delivers superior hedging performance across all four tranches.
Furthermore, as shown in the right panel of Figure [4](https://arxiv.org/html/2602.08039v1#S6.F4 "Figure 4 ‣ 6.2.1 Constructing Effective Model-Independent Hedging Strategies for CDO Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies"), our hedging strategy achieves significant reductions in standard deviation, with reductions ranging from 74.2%74.2\% to 92.3%92.3\%, relative to the unhedged portfolios. Across all tranches, our hedging strategy significantly outperforms the Gaussian copula model, yielding a substantially lower P&L volatility.
This consistent reduction in standard deviation underscores the practical utility and robustness of our model-independent hedging strategy for CDO portfolios.

Figure 4: Hedging Performance of Our Model-Independent Hedging Strategy (Comparison of P&L Standard Deviations)

![Refer to caption](x5.png)

*Notes.*
The left panel presents the standard deviations of the daily P&L series of (i) the delta-hedged portfolios resulting from our model-independent hedging strategy, (ii) the unhedged portfolios, and (iii) the delta-hedged portfolios resulting from the Gaussian copula model. We can see that our model-independent hedging strategy delivers superior hedging performance across all four tranches. The right panel shows that our hedging strategy achieves significant reductions in standard deviation, with reductions ranging from 74.2%74.2\% to 92.3%92.3\%, relative to the unhedged portfolios. Furthermore, across all tranches, our hedging strategy significantly outperforms the Gaussian copula model, yielding a substantially lower P&L volatility.

#### 6.2.2 NPV Distributions for CDO Tranches and Portfolios

Analyzing the NPV distributions for CDO portfolios composed of multiple CDO tranches is critical for CDO portfolio risk management. However, traditional parametric models, which are often calibrated only to individual tranches, typically fail to support this analysis, as they cannot generate a single, consistent joint default distribution for the entire capital structure. In contrast, our strong compatibility framework enables precisely this portfolio-level analysis: the unified, consistent model underpinning it can perfectly fit all market prices, thereby enabling reliable estimation of NPV distributions for CDO portfolios.

We first conduct an empirical analysis on the NPV distributions of all CDO tranches, the building blocks of those of any CDO portfolio.
By applying Algorithm [5.2.1](https://arxiv.org/html/2602.08039v1#S5.SS2.SSS1 "5.2.1 Estimating NPV Distributions for Risk Management ‣ 5.2 Applications of Strong Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility"), we can simulate the NPV distributions of all CDO tranches (i.e., the distributions of V[al,bl]V^{[a\_{l},b\_{l}]} for l=1,…,Ml=1,\ldots,M) with the simulated sample size of 1,000,0001,000,000.
The left panel of Figure [5](https://arxiv.org/html/2602.08039v1#S6.F5 "Figure 5 ‣ 6.2.2 NPV Distributions for CDO Tranches and Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies") illustrates the resulting joint NPV distribution of the equity and senior mezzanine tranches. The “reverse L” shape shown in the figure clearly reflects the defining waterfall payment structure of CDO products: losses on a senior tranche begin to accrue only after the subordinated tranche has been completely wiped out. Similar waterfall payment structures are also observed in the joint NPV distributions of other tranche pairs. Furthermore, the sample mean of the NPV V[al,bl]V^{[a\_{l},b\_{l}]} for each tranche is statistically indistinguishable from zero, supporting the validity of our method.

Figure 5: Simulated NPV Distributions for CDO Tranches and Portfolios

![Refer to caption](x6.png)

![Refer to caption](x7.png)

*Notes.*
The left panel illustrates the joint NPV distribution of the equity and senior mezzanine tranches (in terms of the scatter plot). The “reverse L” shape shown in the figure clearly reflects the defining waterfall payment structure of CDO products.
The right panel shows the NPV distribution of a specific CDO portfolio composed of short 4 units of the equity tranche, long 2 units of the junior mezzanine tranche, and short 1 unit of the senior mezzanine tranche.

By aggregating the simulated NPV values of individual tranches according to the specific CDO composition, we can analyze the NPV distribution of any CDO portfolio. The right panel of Figure [5](https://arxiv.org/html/2602.08039v1#S6.F5 "Figure 5 ‣ 6.2.2 NPV Distributions for CDO Tranches and Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies") shows the NPV distribution of a specific CDO portfolio composed of short 4 units of the equity tranche, long 2 units of the junior mezzanine tranche, and short 1 unit of the senior mezzanine tranche. The resulting NPV distribution offers a practical tool for CDO portfolio risk management.

### 6.3 Pricing Nonstandard CDOs

#### 6.3.1 Pricing CDO Tranches with Nonstandard Attachment and Detachment Points

We apply Algorithm [5.1.2](https://arxiv.org/html/2602.08039v1#S5.SS1.SSS2 "5.1.2 Model-Independent and Arbitrage-Free Pricing Bounds for CDOs with Nonstandard Attachment and Detachment Points ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility") to determine the model-independent and arbitrage-free price ranges for CDO tranches with nonstandard attachment and detachment points [a,b][a,b].

The left panel of Figure [6](https://arxiv.org/html/2602.08039v1#S6.F6 "Figure 6 ‣ 6.3.1 Pricing CDO Tranches with Nonstandard Attachment and Detachment Points ‣ 6.3 Pricing Nonstandard CDOs ‣ 6 Empirical Studies") presents the numerical results of the price ranges (in terms of spreads) for equity tranches with a fixed attachment point of 0%0\% and varying detachment points bb on March 28, 2025. As expected, the spread decreases as the detachment point bb increases. For very thick tranches (e.g., when bb approaches 100%100\%), the spreads converge to the underlying index spread (5858 bps).
The arbitrage-free price range, denoted by the shaded area, is wider for detachment points typical of mezzanine tranches (approximately 20%20\% to 50%50\%) and narrows for the most junior and senior tranche segments of the capital structure.

Figure 6: Model-Independent and Arbitrage-Free Price Ranges for CDO Tranches with Nonstandard Attachment and Detachment Points

![Refer to caption](x8.png)

![Refer to caption](x9.png)

*Notes.*
The left panel presents the numerical results of the model-independent and arbitrage-free price ranges (in terms of spreads) for equity tranches with a fixed attachment point of 0%0\% and varying detachment points bb on March 28, 2025.
The right panel shows how the price ranges (in terms of up-front payments) for CDO tranches with varying attachment and detachment points [a,a+4%][a,a+4\%] having a constant width of 4%4\% change as aa increases (i.e., as tranche seniority varies).

In addition, the right panel of Figure [6](https://arxiv.org/html/2602.08039v1#S6.F6 "Figure 6 ‣ 6.3.1 Pricing CDO Tranches with Nonstandard Attachment and Detachment Points ‣ 6.3 Pricing Nonstandard CDOs ‣ 6 Empirical Studies") shows how the price ranges (in terms of up-front payments) for CDO tranches with varying attachment and detachment points [a,a+4%][a,a+4\%] having a constant width of 4%4\% change as aa increases (i.e., as tranche seniority varies).
It can be seen that the up-front payment is highest for the most junior tranche [0%,4%][0\%,4\%] and decreases monotonically as aa increases, eventually turning negative for senior tranches. Here a negative up-front payment means that the protection buyer receives a payment at inception, as the fixed running spread overcompensates for the low risk associated with these senior tranches.

#### 6.3.2 Pricing CDOs with a Nonstandard Number of Underlying Names

We utilize Algorithm [5.2.2](https://arxiv.org/html/2602.08039v1#S5.SS2.SSS2 "5.2.2 Pricing CDOs with a Nonstandard Number of Underlying Names ‣ 5.2 Applications of Strong Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility") to compute the price ranges for CDOs with a nonstandard number of underlying names. Table [4](https://arxiv.org/html/2602.08039v1#S6.T4 "Table 4 ‣ 6.3.2 Pricing CDOs with a Nonstandard Number of Underlying Names ‣ 6.3 Pricing Nonstandard CDOs ‣ 6 Empirical Studies") presents the calculated price ranges for the tranches of CDOs with varying nonstandard numbers of underlying names (5050, 100100, 150150, and 200200), using the gamma-distorted copula with parameter N=100N=100. We can see that for CDOs with a large number of underlying names (e.g., no fewer than 100100), the calculated price ranges are relatively narrow and close to the market prices of their standard counterpart with 125125 underlying names.

Table 4: The Price Ranges for CDO Tranches with a Nonstandard Number of Names

| # of Names | [0%, 3%] | [3%, 6%] | [6%, 12%] | [12%, 100%] |
| --- | --- | --- | --- | --- |
| 125 | 28.438% | 4.531% | 106.32 bps | 27.44 bps |
| 50 | [25.917%, 26.874%] | [5.497%, 6.444%] | [107.89, 113.27] bps | [27.45, 27.74] bps |
| 100 | [28.091%, 28.259%] | [4.616%, 4.800%] | [106.25, 107.36] bps | [27.44, 27.49] bps |
| 150 | [28.573%, 28.718%] | [4.314%, 4.475%] | [105.43, 106.26] bps | [27.40, 27.44] bps |
| 200 | [28.760%, 29.140%] | [3.952%, 4.382%] | [104.38, 106.45] bps | [27.35, 27.44] bps |

## 7 Code and Data Disclosure

The code and data to support our numerical experiments have been uploaded as a separate zip file.

## References

* D. Applebaum (2009)
  Lévy processes and stochastic calculus.
   Cambridge University Press, Cambridge.
  Cited by: [§4.3](https://arxiv.org/html/2602.08039v1#S4.SS3.p2.7 "4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility").
* D. Brigo, A. Pallavicini, and R. Torresetti (2010)
  Credit models and the crisis: a journey into cdos, copulas, correlations and dynamic models.
   John Wiley & Sons, Chichester.
  Cited by: [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p2.2 "1.1 Background and Motivations ‣ 1 Introduction"),
  [§1.3](https://arxiv.org/html/2602.08039v1#S1.SS3.p4.1 "1.3 Comparison with Hull and White (2006) ‣ 1 Introduction").
* X. Burtschell, J. Gregory, and J. Laurent (2009)
  A comparative analysis of CDO pricing models under the factor copula framework.
  Journal of Derivatives 16 (4),  pp. 9–37.
  Cited by: [§3.2](https://arxiv.org/html/2602.08039v1#S3.SS2.p2.5 "3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility"),
  [Remark 3.1](https://arxiv.org/html/2602.08039v1#S3.ThmRemark1.p1.3 "Remark 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility").
* A. Charnes and W.W. Cooper (1962)
  Programming with linear fractional functionals.
  Naval Research Logistics Quarterly 9 (3),  pp. 181–186.
  Cited by: [§14](https://arxiv.org/html/2602.08039v1#S14.p1.3 "14 Transforming an LFP Problem into an LP Problem"),
  [Remark 4.4](https://arxiv.org/html/2602.08039v1#S4.ThmRemark4.p1.2 "Remark 4.4 (Transforming LFP problems into LP problems) ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility").
* Z. Chen and P. Glasserman (2008)
  Sensitivity estimates for portfolio credit derivatives using Monte Carlo.
  Finance and Stochastics 12,  pp. 507–540.
  Cited by: [§5.1.1](https://arxiv.org/html/2602.08039v1#S5.SS1.SSS1.p1.5 "5.1.1 A Model-Independent Hedging Strategy ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility").
* U. Cherubini, E. Luciano, and W. Vecchiato (2004)
  Copula methods in finance.
   John Wiley & Sons, Chichester.
  Cited by: [§1.2](https://arxiv.org/html/2602.08039v1#S1.SS2.p1.1 "1.2 Our Contributions ‣ 1 Introduction"),
  [§2.1](https://arxiv.org/html/2602.08039v1#S2.SS1.p1.8 "2.1 Valuation Framework for CDO Tranches ‣ 2 Definitions of Weak Compatibility and Strong Compatibility").
* P. Collin-Dufresne, R. S. Goldstein, and F. Yang (2012)
  On the relative pricing of long-maturity index options and collateralized debt obligations.
  The Journal of Finance 67 (6),  pp. 1983–2014.
  Cited by: [§1.2](https://arxiv.org/html/2602.08039v1#S1.SS2.p1.1 "1.2 Our Contributions ‣ 1 Introduction"),
  [§3.2](https://arxiv.org/html/2602.08039v1#S3.SS2.p2.5 "3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility").
* P. Collin-Dufresne, B. Junge, and A. B. Trolle (2024)
  How integrated are credit and equity markets? evidence from index options.
  The Journal of Finance 79 (2),  pp. 949–992.
  Cited by: [Remark 3.1](https://arxiv.org/html/2602.08039v1#S3.ThmRemark1.p1.3 "Remark 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility").
* R. Cont and Y. H. Kan (2011)
  Dynamic hedging of portfolio credit derivatives.
  SIAM Journal on Financial Mathematics 2 (1),  pp. 112–140.
  Cited by: [§15](https://arxiv.org/html/2602.08039v1#S15.p1.2 "15 Standard Methods for CDS Index Calculations"),
  [item Step 3:](https://arxiv.org/html/2602.08039v1#S5.I1.ix3.p1.2 "In 5.1.1 A Model-Independent Hedging Strategy ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility"),
  [§6.2.1](https://arxiv.org/html/2602.08039v1#S6.SS2.SSS1.p1.1 "6.2.1 Constructing Effective Model-Independent Hedging Strategies for CDO Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies"),
  [§6.2.1](https://arxiv.org/html/2602.08039v1#S6.SS2.SSS1.p5.1 "6.2.1 Constructing Effective Model-Independent Hedging Strategies for CDO Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies"),
  [§6.2.1](https://arxiv.org/html/2602.08039v1#S6.SS2.SSS1.p6.2 "6.2.1 Constructing Effective Model-Independent Hedging Strategies for CDO Portfolios ‣ 6.2 Risk Management for CDO Portfolios ‣ 6 Empirical Studies").
* R. Frey and J. Backhaus (2010)
  Dynamic hedging of synthetic CDO tranches with spread risk and default contagion.
  Journal of Economic Dynamics and Control 34 (4),  pp. 710–724.
  Cited by: [§5.1.1](https://arxiv.org/html/2602.08039v1#S5.SS1.SSS1.p1.5 "5.1.1 A Model-Independent Hedging Strategy ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility").
* R. Frey and T. Schmidt (2012)
  Pricing and hedging of credit derivatives via the innovations approach to nonlinear filtering.
  Finance and Stochastics 16,  pp. 105–133.
  Cited by: [§1.2](https://arxiv.org/html/2602.08039v1#S1.SS2.p1.1 "1.2 Our Contributions ‣ 1 Introduction").
* N. Godec and S. Masabathula (2024)
  Fixed Income Special Report 2023.
  Special Report
   World Exchanges Focus.
  External Links: [Link](https://focus.world-exchanges.org/articles/fixed-income-sp)
  Cited by: [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p1.1 "1.1 Background and Motivations ‣ 1 Introduction").
* M. Hofert (2010)
  Sampling nested Archimedean copulas with applications to CDO pricing.
  Ph.D. Thesis, Universität Ulm.
  Cited by: [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p2.2 "1.1 Background and Motivations ‣ 1 Introduction").
* J. C. Hull (2022)
  Options, futures, and other derivatives.
  11th edition, Pearson, London.
  Cited by: [§15](https://arxiv.org/html/2602.08039v1#S15.p1.2 "15 Standard Methods for CDS Index Calculations"),
  [item Step 1:](https://arxiv.org/html/2602.08039v1#S5.I1.ix1.p1.2 "In 5.1.1 A Model-Independent Hedging Strategy ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility"),
  [§6.1.1](https://arxiv.org/html/2602.08039v1#S6.SS1.SSS1.p2.5 "6.1.1 Data ‣ 6.1 Data and Verification of Compatibility ‣ 6 Empirical Studies").
* J. Hull and A. White (2006)
  Valuing credit derivatives using an implied copula approach.
  Journal of Derivatives 14 (2),  pp. 8–28.
  Cited by: [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p1.1 "1.1 Background and Motivations ‣ 1 Introduction"),
  [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p4.1 "1.1 Background and Motivations ‣ 1 Introduction"),
  [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p5.1 "1.1 Background and Motivations ‣ 1 Introduction"),
  [§1.3](https://arxiv.org/html/2602.08039v1#S1.SS3 "1.3 Comparison with Hull and White (2006) ‣ 1 Introduction"),
  [§1.3](https://arxiv.org/html/2602.08039v1#S1.SS3.p1.1 "1.3 Comparison with Hull and White (2006) ‣ 1 Introduction"),
  [§1.3](https://arxiv.org/html/2602.08039v1#S1.SS3.p2.1 "1.3 Comparison with Hull and White (2006) ‣ 1 Introduction"),
  [§1.3](https://arxiv.org/html/2602.08039v1#S1.SS3.p3.1 "1.3 Comparison with Hull and White (2006) ‣ 1 Introduction"),
  [§1.3](https://arxiv.org/html/2602.08039v1#S1.SS3.p4.1 "1.3 Comparison with Hull and White (2006) ‣ 1 Introduction"),
  [Remark 2.1](https://arxiv.org/html/2602.08039v1#S2.ThmRemark1.p2.3 "Remark 2.1 ‣ 2.2 Definitions of Weak Compatibility and Strong Compatibility ‣ 2 Definitions of Weak Compatibility and Strong Compatibility"),
  [Remark 4.5](https://arxiv.org/html/2602.08039v1#S4.ThmRemark5 "Remark 4.5 (Comparison with the Implied Copula Method of Hull and White (2006)) ‣ 4.5.2 Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility"),
  [Remark 4.5](https://arxiv.org/html/2602.08039v1#S4.ThmRemark5.p1.1 "Remark 4.5 (Comparison with the Implied Copula Method of Hull and White (2006)) ‣ 4.5.2 Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility").
* A. Kalemanova, B. Schmid, and R. Werner (2007)
  The normal inverse Gaussian distribution for synthetic CDO pricing.
  Journal of Derivatives 14 (3),  pp. 80–93.
  Cited by: [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p2.2 "1.1 Background and Motivations ‣ 1 Introduction").
* M. Kijima, S. Motomiya, and Y. Suzuki (2010)
  Pricing of CDOs based on the multivariate Wang transform.
  Journal of Economic Dynamics and Control 34 (11),  pp. 2245–2258.
  Cited by: [§1.2](https://arxiv.org/html/2602.08039v1#S1.SS2.p1.1 "1.2 Our Contributions ‣ 1 Introduction").
* S. Kullback and R. A. Leibler (1951)
  On information and sufficiency.
  The Annals of Mathematical Statistics 22 (1),  pp. 79–86.
  Cited by: [§5.1.1](https://arxiv.org/html/2602.08039v1#S5.SS1.SSS1.p2.2 "5.1.1 A Model-Independent Hedging Strategy ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility").
* D. Li (2000)
  On default correlation: a copula function approach.
  Journal of Fixed Income 9 (4),  pp. 43–54.
  Cited by: [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p2.2 "1.1 Background and Motivations ‣ 1 Introduction").
* F. Lin, L. Peng, J. Xie, and J. Yang (2018)
  Stochastic distortion and its transformed copula.
  Insurance: Mathematics and Economics 79,  pp. 148–166.
  Cited by: [§4.1](https://arxiv.org/html/2602.08039v1#S4.SS1.p2.5 "4.1 Conditionally I.I.D. Models and Stochastic Distortions ‣ 4 Strong Compatibility"),
  [Definition 4.1](https://arxiv.org/html/2602.08039v1#S4.ThmDefinition1 "Definition 4.1 (Stochastic Distortion, Lin et al. 2018) ‣ 4.1 Conditionally I.I.D. Models and Stochastic Distortions ‣ 4 Strong Compatibility").
* J. Mai (2020)
  The infinite extendibility problem for exchangeable real-valued random vectors.
  Probability Surveys 17,  pp. 677–753.
  Cited by: [§10](https://arxiv.org/html/2602.08039v1#S10.p2.14 "10 Proofs of Propositions 4.1, 4.2 and 4.4"),
  [Remark 4.1](https://arxiv.org/html/2602.08039v1#S4.ThmRemark1.p1.1 "Remark 4.1 ‣ 4.1 Conditionally I.I.D. Models and Stochastic Distortions ‣ 4 Strong Compatibility").
* V. Masol and W. Schoutens (2011)
  Comparing alternative Lévy base correlation models for pricing and hedging CDO tranches.
  Quantitative Finance 11 (5),  pp. 763–773.
  Cited by: [§5.1.1](https://arxiv.org/html/2602.08039v1#S5.SS1.SSS1.p1.5 "5.1.1 A Model-Independent Hedging Strategy ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility").
* A. J. McNeil, R. Frey, and P. Embrechts (2015)
  Quantitative risk management: concepts, techniques and tools.
   Princeton University Press, Princeton.
  Cited by: [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p2.2 "1.1 Background and Motivations ‣ 1 Introduction").
* T. Moosbrucker (2006)
  Explaining the correlation smile using variance gamma distributions.
  The Journal of Fixed Income 16 (1),  pp. 71–87.
  Cited by: [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p2.2 "1.1 Background and Motivations ‣ 1 Introduction").
* C. Mounfield (2009)
  Synthetic cdos: modelling, valuation and risk management.
   Cambridge University Press, Cambridge.
  Cited by: [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p1.1 "1.1 Background and Motivations ‣ 1 Introduction").
* E. Papageorgiou and R. Sircar (2009)
  Multiscale intensity models and name grouping for valuation of multi-name credit derivatives.
  Applied Mathematical Finance 16 (4),  pp. 353–383.
  Cited by: [§2.1](https://arxiv.org/html/2602.08039v1#S2.SS1.p7.4 "2.1 Valuation Framework for CDO Tranches ‣ 2 Definitions of Weak Compatibility and Strong Compatibility").
* X. H. Peng and S. S. Kou (2008)
  Connecting the top-down to the bottom-up: pricing CDO under a conditional survival (CS) model.
  In 2008 Winter Simulation Conference,
   pp. 578–586.
  Cited by: [§1.2](https://arxiv.org/html/2602.08039v1#S1.SS2.p1.1 "1.2 Our Contributions ‣ 1 Introduction"),
  [§2.1](https://arxiv.org/html/2602.08039v1#S2.SS1.p7.4 "2.1 Valuation Framework for CDO Tranches ‣ 2 Definitions of Weak Compatibility and Strong Compatibility").
* D. Prange and W. Scherer (2009)
  Correlation smile matching for collateralized debt obligation tranches with α\alpha-stable distributions and fitted Archimedean copula models.
  Quantitative Finance 9 (4),  pp. 439–449.
  Cited by: [§1.1](https://arxiv.org/html/2602.08039v1#S1.SS1.p2.2 "1.1 Background and Motivations ‣ 1 Introduction").
* L. Schloegl and D. O’Kane (2005)
  A note on the large homogeneous portfolio approximation with the student-t copula.
  Finance and Stochastics 9,  pp. 577–584.
  Cited by: [§6.1.1](https://arxiv.org/html/2602.08039v1#S6.SS1.SSS1.p2.5 "6.1.1 Data ‣ 6.1 Data and Verification of Compatibility ‣ 6 Empirical Studies").
* W. Schoutens and J. Cariboni (2012)
  Lévy processes in credit risk.
   John Wiley & Sons, Chichester.
  Cited by: [§4.3](https://arxiv.org/html/2602.08039v1#S4.SS3.p2.7 "4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility").
* S. B. Seo and J. A. Wachter (2018)
  Do rare events explain CDX tranche spreads?.
  The Journal of Finance 73 (5),  pp. 2343–2383.
  Cited by: [§1.2](https://arxiv.org/html/2602.08039v1#S1.SS2.p1.1 "1.2 Our Contributions ‣ 1 Introduction"),
  [§3.2](https://arxiv.org/html/2602.08039v1#S3.SS2.p2.5 "3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility").
* D. Wang, S. T. Rachev, and F. J. Fabozzi (2009)
  Pricing tranches of a CDO and a CDS index: recent advances and future research.
  In Risk Assessment,
  Heidelberg,  pp. 263–286.
  Cited by: [§3.2](https://arxiv.org/html/2602.08039v1#S3.SS2.p2.5 "3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility").

\ECSwitch

E-Companion to “Perfectly Fitting CDO Prices Across Tranches: A Theoretical Framework with Efficient Algorithms”

## 8 Proofs of Propositions [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmProposition1 "Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility") and [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmProposition2 "Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility")

Proof of Proposition [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmProposition1 "Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility").
We will establish the equivalence among (i), (ii), and (iii) through the following implications: (i) ⇒\Rightarrow (ii), (ii) ⇒\Rightarrow (iii), and (iii) ⇒\Rightarrow (i).

(I) Proof of (i) ⇒\Rightarrow (ii).
Assume the existence of non-negative random variables τ^j\hat{\tau}\_{j} (for 1≤j≤n1\leq j\leq n) as specified in (i).
Let 𝒢n\mathcal{G}\_{n} denote the set of all permutations on the set {1,…,n}\{1,\ldots,n\}, and let π\pi be a random permutation uniformly distributed on 𝒢n\mathcal{G}\_{n} that is independent of (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}).

Define a new random vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | (τ^1′,…,τ^n′):=(τ^π​(1),…,τ^π​(n)).\displaystyle(\hat{\tau}\_{1}^{\prime},\ldots,\hat{\tau}\_{n}^{\prime}):=(\hat{\tau}\_{\pi(1)},\ldots,\hat{\tau}\_{\pi(n)}). |  | (30) |

We can deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(τ^1′≤x1,…,τ^n′≤xn)=\displaystyle\mathbb{P}(\hat{\tau}\_{1}^{\prime}\leq x\_{1},\ldots,\hat{\tau}\_{n}^{\prime}\leq x\_{n})= | 𝔼​[ℙ​(τ^π​(1)≤x1,…,τ^π​(n)≤xn|π)]\displaystyle\ \mathbb{E}\left[\mathbb{P}(\hat{\tau}\_{\pi(1)}\leq x\_{1},\ldots,\hat{\tau}\_{\pi(n)}\leq x\_{n}|\pi)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑σ∈𝒢n[ℙ​(π=σ)​ℙ​(τ^π​(1)≤x1,…,τ^π​(n)≤xn|π=σ)]\displaystyle\ \sum\_{\sigma\in\mathcal{G}\_{n}}\left[\mathbb{P}(\pi=\sigma)\mathbb{P}(\hat{\tau}\_{\pi(1)}\leq x\_{1},\ldots,\hat{\tau}\_{\pi(n)}\leq x\_{n}|\pi=\sigma)\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 1n!​∑σ∈𝒢nℙ​(τ^σ​(1)≤x1,…,τ^σ​(n)≤xn),\displaystyle\ \frac{1}{n!}\sum\_{\sigma\in\mathcal{G}\_{n}}\mathbb{P}(\hat{\tau}\_{\sigma(1)}\leq x\_{1},\ldots,\hat{\tau}\_{\sigma(n)}\leq x\_{n}), |  | (31) |

where the third equality holds because π\pi is uniformly distributed on 𝒢n\mathcal{G}\_{n} and is independent of (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}). ([31](https://arxiv.org/html/2602.08039v1#S8.E31 "In 8 Proofs of Propositions 3.1 and 3.2")) implies that the joint distribution of (τ^1′,…,τ^n′)(\hat{\tau}\_{1}^{\prime},\ldots,\hat{\tau}\_{n}^{\prime}) is the symmetrized version of that of (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}).
Using ([31](https://arxiv.org/html/2602.08039v1#S8.E31 "In 8 Proofs of Propositions 3.1 and 3.2")) and the substitution σ′=σ∘ρ−1\sigma^{\prime}=\sigma\circ\rho^{-1}, we can obtain that for any ρ∈𝒢n\rho\in\mathcal{G}\_{n},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(τ^1′≤xρ​(1),…,τ^n′≤xρ​(n))=\displaystyle\mathbb{P}(\hat{\tau}\_{1}^{\prime}\leq x\_{\rho(1)},\ldots,\hat{\tau}\_{n}^{\prime}\leq x\_{\rho(n)})= | 1n!​∑σ∈𝒢nℙ​(τ^σ​(1)≤xρ​(1),…,τ^σ​(n)≤xρ​(n))\displaystyle\ \frac{1}{n!}\sum\_{\sigma\in\mathcal{G}\_{n}}\mathbb{P}(\hat{\tau}\_{\sigma(1)}\leq x\_{\rho(1)},\ldots,\hat{\tau}\_{\sigma(n)}\leq x\_{\rho(n)}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1n!​∑σ′∈𝒢nℙ​(τ^σ′​(1)≤x1,…,τ^σ′​(n)≤xn)\displaystyle\ \frac{1}{n!}\sum\_{\sigma^{\prime}\in\mathcal{G}\_{n}}\mathbb{P}(\hat{\tau}\_{\sigma^{\prime}(1)}\leq x\_{1},\ldots,\hat{\tau}\_{\sigma^{\prime}(n)}\leq x\_{n}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ℙ​(τ^1′≤x1,…,τ^n′≤xn),\displaystyle\ \mathbb{P}(\hat{\tau}\_{1}^{\prime}\leq x\_{1},\ldots,\hat{\tau}\_{n}^{\prime}\leq x\_{n}), |  |

which implies that (τ^1′,…,τ^n′)(\hat{\tau}\_{1}^{\prime},\ldots,\hat{\tau}\_{n}^{\prime}) is exchangeable.

Next, we shall show that (τ^1′,…,τ^n′)(\hat{\tau}\_{1}^{\prime},\ldots,\hat{\tau}\_{n}^{\prime}) shares the same DPM with (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}).
Define

|  |  |  |
| --- | --- | --- |
|  | N^t′:=∑j=1n𝟏{τ^j′≤t}≡∑j=1n𝟏{τ^π​(j)≤t}for t≥0.\hat{N}\_{t}^{\prime}:=\sum\_{j=1}^{n}\mathbf{1}\_{\{\hat{\tau}\_{j}^{\prime}\leq t\}}\equiv\sum\_{j=1}^{n}\mathbf{1}\_{\{\hat{\tau}\_{\pi(j)}\leq t\}}\quad\text{for $t\geq 0$}. |  |

Since the two sets {π​(1),⋯,π​(n)}\{\pi(1),\cdots,\pi(n)\} and {1,⋯,n}\{1,\cdots,n\} are identical, it follows that

|  |  |  |
| --- | --- | --- |
|  | N^t′=∑j=1n𝟏{τ^j≤t}=N^tfor t≥0.\hat{N}\_{t}^{\prime}=\sum\_{j=1}^{n}\mathbf{1}\_{\{\hat{\tau}\_{j}\leq t\}}=\hat{N}\_{t}\quad\text{for $t\geq 0$}. |  |

Therefore, we have ℙ​(N^Ti′=j)=ℙ​(N^Ti=j)=q^i​j\mathbb{P}(\hat{N}^{\prime}\_{T\_{i}}=j)=\mathbb{P}(\hat{N}\_{T\_{i}}=j)=\hat{q}\_{ij} for 1≤i≤m1\leq i\leq m and 0≤j≤n0\leq j\leq n.
Accordingly, we conclude that (τ^1′,…,τ^n′)(\hat{\tau}\_{1}^{\prime},\ldots,\hat{\tau}\_{n}^{\prime}) shares the same DPM with (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}).
This completes the proof of (i) ⇒\Rightarrow (ii).

(II) Proof of (ii) ⇒\Rightarrow (iii).
The non-negativity and sum-to-one constraints are apparent from the probabilistic definition of (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}).
Moreover, since N^Ti≤N^Ti+1\hat{N}\_{T\_{i}}\leq\hat{N}\_{T\_{i+1}} for 1≤i≤m−11\leq i\leq m-1, we can obtain

|  |  |  |
| --- | --- | --- |
|  | ℙ​(N^Ti≥j)≤ℙ​(N^Ti+1≥j)for 1≤i≤m−1 and 0≤j≤n,\mathbb{P}(\hat{N}\_{T\_{i}}\geq j)\leq\mathbb{P}(\hat{N}\_{T\_{i+1}}\geq j)\quad\text{for $1\leq i\leq m-1$ and $0\leq j\leq n$}, |  |

which yields the monotonicity constraints in ([4](https://arxiv.org/html/2602.08039v1#S3.E4 "In item (iii) ‣ Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility")).
Hence, (ii) implies (iii).

(III) Proof of (iii) ⇒\Rightarrow (i).
We will use a constructive proof.
Augment the matrix Q^\hat{Q} by adding boundary rows corresponding to T0=0T\_{0}=0 and Tm+1T\_{m+1} and setting q^0​j=𝟏{j=0}\hat{q}\_{0j}=\mathbf{1}\_{\{j=0\}} and q^m+1,j=𝟏{j=n}\hat{q}\_{m+1,j}=\mathbf{1}\_{\{j=n\}} for 0≤j≤n0\leq j\leq n.
Consider a random variable U∼𝒰​(0,1)U\sim\mathcal{U}(0,1), and define a sequence of non-negative random variables

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ^j:=∑i=1m+1(Ti+Ti−12​𝟏Vi​j)for 1≤j≤n,\hat{\tau}\_{j}:=\sum\_{i=1}^{m+1}\left(\frac{T\_{i}+T\_{i-1}}{2}\mathbf{1}\_{V\_{ij}}\right)\quad\text{for $1\leq j\leq n$}, |  | (32) |

where
Vi​j:={θi−1,j<U≤θi​j}V\_{ij}:=\left\{\theta\_{i-1,j}<U\leq\theta\_{ij}\right\} for 1≤i≤m+11\leq i\leq m+1 and 1≤j≤n1\leq j\leq n and θi​j:=∑k≥jq^i​k\theta\_{ij}:=\sum\_{k\geq j}\hat{q}\_{ik} for 0≤i≤m+10\leq i\leq m+1 and 1≤j≤n1\leq j\leq n.

We shall complete the proof of this part by taking three steps. First, let us present some properties of {θi​j}\{\theta\_{ij}\} and {Vi​j}\{V\_{ij}\}.
Using the third set of constraints (i.e., the non-negativity constraints) of ([4](https://arxiv.org/html/2602.08039v1#S3.E4 "In item (iii) ‣ Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility")), we know from the definition that θi​j\theta\_{ij} is non-increasing in jj for any 0≤i≤m+10\leq i\leq m+1.

Note that the second set of constraints (i.e., the monotonicity constraints) of ([4](https://arxiv.org/html/2602.08039v1#S3.E4 "In item (iii) ‣ Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility")) implies that θ1​j≤θ2​j≤⋯≤θm​j\theta\_{1j}\leq\theta\_{2j}\leq\cdots\leq\theta\_{mj} for all 1≤j≤n1\leq j\leq n. Furthermore, we know from the definitions that θ0​j=0\theta\_{0j}=0 and θm+1,j=1\theta\_{m+1,j}=1. In addition, using the first set of constraints (i.e., the sum-to-one constraints) and the third set of constraints (i.e., the non-negativity constraints) of ([4](https://arxiv.org/html/2602.08039v1#S3.E4 "In item (iii) ‣ Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility")), we can obtain that θm​j≤1\theta\_{mj}\leq 1 and θ1​j≥0\theta\_{1j}\geq 0, respectively. Therefore, we obtain that θ0​j≤θ1​j≤⋯≤θm​j≤θm+1,j\theta\_{0j}\leq\theta\_{1j}\leq\cdots\leq\theta\_{mj}\leq\theta\_{m+1,j} for all 1≤j≤n1\leq j\leq n. This further implies that for any 1≤j≤n1\leq j\leq n, V1​j,V2​j,⋯,Vm+1,jV\_{1j},V\_{2j},\cdots,V\_{m+1,j} are mutually disjoint. On the other hand, we can deduce that for any 1≤j≤n1\leq j\leq n,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⋃i=1m+1Vi​j=⋃i=1m+1{θi−1,j<U≤θi​j}={θ0​j<U≤θm+1,j}={0<U≤1},\displaystyle\bigcup\_{i=1}^{m+1}V\_{ij}=\bigcup\_{i=1}^{m+1}\left\{\theta\_{i-1,j}<U\leq\theta\_{ij}\right\}=\left\{\theta\_{0j}<U\leq\theta\_{m+1,j}\right\}=\left\{0<U\leq 1\right\}, |  | (33) |

which indicates that for any 1≤j≤n1\leq j\leq n, the union of V1​j,V2​j,⋯,Vm+1,jV\_{1j},V\_{2j},\cdots,V\_{m+1,j} is the complete set. Consequently, we conclude that for any 1≤j≤n1\leq j\leq n, τ^j\hat{\tau}\_{j} is a discrete random variable, taking a positive value Ti+Ti−12\frac{T\_{i}+T\_{i-1}}{2} on Vi​jV\_{ij} for 1≤i≤m+11\leq i\leq m+1, where V1​j,V2​j,⋯,Vm+1,jV\_{1j},V\_{2j},\cdots,V\_{m+1,j} is a partition of the complete set and the m+1m+1 positive values T1+T02,T2+T12,⋯,Tm+1+Tm2\frac{T\_{1}+T\_{0}}{2},\frac{T\_{2}+T\_{1}}{2},\cdots,\frac{T\_{m+1}+T\_{m}}{2} are increasing and mutually different.

Second, we shall show that (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}) possesses the following two properties.

(i) They are ordered, i.e., τ^1≤τ^2≤⋯≤τ^n\hat{\tau}\_{1}\leq\hat{\tau}\_{2}\leq\cdots\leq\hat{\tau}\_{n}.

(ii) It holds that {τ^j≤Ti}≡{U≤∑k≥jq^i​k}\{\hat{\tau}\_{j}\leq T\_{i}\}\equiv\{U\leq\sum\_{k\geq j}\hat{q}\_{ik}\} for 1≤i≤m+11\leq i\leq m+1 and 1≤j≤n1\leq j\leq n.

We start with the proof of property (i). For any 1≤j≤n−11\leq j\leq n-1 and i=1,⋯,m+1i=1,\cdots,m+1, if τ^j=Ti+Ti−12\hat{\tau}\_{j}=\frac{T\_{i}+T\_{i-1}}{2}, this means that U∈(θi−1,j,θi​j]U\in(\theta\_{i-1,j},\theta\_{ij}], which further implies that U>θi−1,j+1U>\theta\_{i-1,j+1} thanks to the fact that θi​j\theta\_{ij} is non-increasing in jj for any 0≤i≤m+10\leq i\leq m+1. Then according to the definition of τ^j+1\hat{\tau}\_{j+1}, we have that τ^j+1≥Ti+Ti−12=τ^j\hat{\tau}\_{j+1}\geq\frac{T\_{i}+T\_{i-1}}{2}=\hat{\tau}\_{j}. Thus, we have proved property (i). Regarding property (ii), we can deduce that for 1≤i≤m+11\leq i\leq m+1 and 1≤j≤n1\leq j\leq n,

|  |  |  |  |
| --- | --- | --- | --- |
|  | {τ^j≤Ti}=\displaystyle\{\hat{\tau}\_{j}\leq T\_{i}\}= | ⋃l=1i{τ^j=Tl+Tl−12}=⋃l=1iVl​j={U≤∑k≥jq^i​k}.\displaystyle\ \bigcup\_{l=1}^{i}\left\{\hat{\tau}\_{j}=\frac{T\_{l}+T\_{l-1}}{2}\right\}=\bigcup\_{l=1}^{i}V\_{lj}=\ \left\{U\leq\sum\_{k\geq j}\hat{q}\_{ik}\right\}. |  |

Finally, we are ready to prove that the DPM of (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}) is {q^i​j}1≤i≤m,0≤j≤n{\{\hat{q}\_{ij}\}}\_{1\leq i\leq m,0\leq j\leq n}. Define N^t:=∑l=1n𝟏{τ^l≤t}\hat{N}\_{t}:=\sum\_{l=1}^{n}\mathbf{1}\_{\{\hat{\tau}\_{l}\leq t\}} for all t≥0t\geq 0.
Then we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(N^Ti=j)=\displaystyle\mathbb{P}(\hat{N}\_{T\_{i}}=j)= | ℙ​(∑l=1n𝟏{τ^l≤Ti}=j)=ℙ​(τ^j≤Ti,τ^j+1>Ti)=ℙ​(τ^j≤Ti)−ℙ​(τ^j+1≤Ti),\displaystyle\ \mathbb{P}\left(\sum\_{l=1}^{n}\mathbf{1}\_{\{\hat{\tau}\_{l}\leq T\_{i}\}}=j\right)=\mathbb{P}\left(\hat{\tau}\_{j}\leq T\_{i},\ \hat{\tau}\_{j+1}>T\_{i}\right)=\mathbb{P}\left(\hat{\tau}\_{j}\leq T\_{i}\right)-\mathbb{P}\left(\hat{\tau}\_{j+1}\leq T\_{i}\right), |  |

where the second and third equalities hold due to property (i) above. Then applying property (ii) above yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(N^Ti=j)=\displaystyle\mathbb{P}(\hat{N}\_{T\_{i}}=j)= | ℙ​{U≤∑k≥jq^i​k}−ℙ​{U≤∑k≥j+1q^i​k}=q^i​j.\displaystyle\ \mathbb{P}\left\{U\leq\sum\_{k\geq j}\hat{q}\_{ik}\right\}-\mathbb{P}\left\{U\leq\sum\_{k\geq j+1}\hat{q}\_{ik}\right\}=\hat{q}\_{ij}. |  |

This completes the proof of (iii) ⇒\Rightarrow (i).

Thus, we have shown that (i) ⇒\Rightarrow (ii), (ii) ⇒\Rightarrow (iii), and (iii) ⇒\Rightarrow (i). Accordingly, the whole proof of Proposition [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmProposition1 "Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility") is completed.
□\square

Proof of Proposition [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmProposition2 "Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility").
By definitions of DefLeg[al,bl]{\rm DefLeg}^{[a\_{l},b\_{l}]} and PreLeg[al,bl]{\rm PreLeg}^{[a\_{l},b\_{l}]} in Section [2.1](https://arxiv.org/html/2602.08039v1#S2.SS1 "2.1 Valuation Framework for CDO Tranches ‣ 2 Definitions of Weak Compatibility and Strong Compatibility"), we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | V[al,bl]=\displaystyle V^{[a\_{l},b\_{l}]}= | DefLeg[al,bl]−PreLeg[al,bl]\displaystyle\ {\rm DefLeg}^{[a\_{l},b\_{l}]}-{\rm PreLeg}^{[a\_{l},b\_{l}]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑i=1m[D​(Ti−1+Ti2)​(LTi[al,bl]−LTi−1[al,bl])]−s[al,bl]​[∑i=1mD​(Ti)​(Ti−Ti−1)​(bl−al−LTi[al,bl])]\displaystyle\ \sum\_{i=1}^{m}\!\left[D\!\left(\frac{T\_{i-1}+T\_{i}}{2}\right)\big(L\_{T\_{i}}^{[a\_{l},b\_{l}]}-L\_{T\_{i-1}}^{[a\_{l},b\_{l}]}\big)\right]\!-\!s^{[a\_{l},b\_{l}]}\left[\sum\_{i=1}^{m}\!D(T\_{i})(T\_{i}-T\_{i-1})(b\_{l}-a\_{l}-L\_{T\_{i}}^{[a\_{l},b\_{l}]})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −uf[al,bl]​(bl−al).\displaystyle\ -\textrm{uf}^{[a\_{l},b\_{l}]}(b\_{l}-a\_{l}). |  |

Collecting the coefficients of LTi[al,bl]L\_{T\_{i}}^{[a\_{l},b\_{l}]} for all i=1,…,m−1i=1,\ldots,m-1 and treating i=mi=m separately yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | V[al,bl]=\displaystyle V^{[a\_{l},b\_{l}]}= | ∑i=1m−1[(D​(Ti−1+Ti2)−D​(Ti+1+Ti2)+s[al,bl]​D​(Ti)​(Ti−Ti−1))​LTi[al,bl]]\displaystyle\ \sum\_{i=1}^{m-1}\!\left[\Bigg(D\!\left(\frac{T\_{i-1}+T\_{i}}{2}\right)-D\!\left(\frac{T\_{i+1}+T\_{i}}{2}\right)+s^{[a\_{l},b\_{l}]}D(T\_{i})(T\_{i}-T\_{i-1})\Bigg)L\_{T\_{i}}^{[a\_{l},b\_{l}]}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(D​(Tm−1+Tm2)+s[al,bl]​D​(Tm)​(Tm−Tm−1))​LTm[al,bl]\displaystyle\ +\Bigg(D\!\left(\frac{T\_{m-1}+T\_{m}}{2}\right)+s^{[a\_{l},b\_{l}]}D(T\_{m})(T\_{m}-T\_{m-1})\Bigg)L\_{T\_{m}}^{[a\_{l},b\_{l}]} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(bl−al)​s[al,bl]​∑i=1mD​(Ti)​(Ti−Ti−1)−uf[al,bl]​(bl−al).\displaystyle\ -(b\_{l}-a\_{l})s^{[a\_{l},b\_{l}]}\sum\_{i=1}^{m}D(T\_{i})(T\_{i}-T\_{i-1})-\textrm{uf}^{[a\_{l},b\_{l}]}(b\_{l}-a\_{l}). |  | (34) |

Using the definitions of λi[al,bl]​(𝐬)\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s}) and γ[al,bl]​(𝐬)\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}) in
([6](https://arxiv.org/html/2602.08039v1#S3.E6 "In Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility")) and ([7](https://arxiv.org/html/2602.08039v1#S3.E7 "In Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility")), ([34](https://arxiv.org/html/2602.08039v1#S8.E34 "In 8 Proofs of Propositions 3.1 and 3.2")) can be compactly written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V[al,bl]=∑i=1mλi[al,bl]​(𝐬)​LTi[al,bl]−γ[al,bl]​(𝐬).V^{[a\_{l},b\_{l}]}=\sum\_{i=1}^{m}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})L\_{T\_{i}}^{[a\_{l},b\_{l}]}-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}). |  | (35) |

Next, we will express the expected tranche loss 𝔼​[LTi[al,bl]]\mathbb{E}[L\_{T\_{i}}^{[a\_{l},b\_{l}]}] in terms of the DPM.
Indeed, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[LTi[al,bl]]=\displaystyle\mathbb{E}[L\_{T\_{i}}^{[a\_{l},b\_{l}]}]= | 𝔼​[(LTi−al)+]−𝔼​[(LTi−bl)+]\displaystyle\ \mathbb{E}[(L\_{T\_{i}}-a\_{l})^{+}]-\mathbb{E}[(L\_{T\_{i}}-b\_{l})^{+}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼​[(NTi​(1−R)n−al)+]−𝔼​[(NTi​(1−R)n−bl)+]\displaystyle\ \mathbb{E}\!\left[\left(\frac{N\_{T\_{i}}(1-R)}{n}-a\_{l}\right)^{+}\right]-\mathbb{E}\!\left[\left(\frac{N\_{T\_{i}}(1-R)}{n}-b\_{l}\right)^{+}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑j=0n[(j​(1−R)n−al)+−(j​(1−R)n−bl)+]​ℙ​(NTi=j)\displaystyle\ \sum\_{j=0}^{n}\left[\left(\frac{j(1-R)}{n}-a\_{l}\right)^{+}-\left(\frac{j(1-R)}{n}-b\_{l}\right)^{+}\right]\mathbb{P}(N\_{T\_{i}}=j) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∑j=0nβj[al,bl]​qi​j,\displaystyle\ \sum\_{j=0}^{n}\beta\_{j}^{[a\_{l},b\_{l}]}q\_{ij}, |  | (36) |

where the second equality holds because LTi=NTi​(1−R)/nL\_{T\_{i}}=N\_{T\_{i}}(1-R)/n. Then taking expectation on both sides of ([35](https://arxiv.org/html/2602.08039v1#S8.E35 "In 8 Proofs of Propositions 3.1 and 3.2")) and using ([36](https://arxiv.org/html/2602.08039v1#S8.E36 "In 8 Proofs of Propositions 3.1 and 3.2")) immediately yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | v[al,bl]\displaystyle v^{[a\_{l},b\_{l}]} | =𝔼​[V[al,bl]]=∑i=1mλi[al,bl]​(𝐬)​𝔼​[LTi[al,bl]]−γ[al,bl]​(𝐬)=∑i=1m∑j=0n[λi[al,bl]​(𝐬)​βj[al,bl]​qi​j]−γ[al,bl]​(𝐬),\displaystyle=\mathbb{E}[V^{[a\_{l},b\_{l}]}]=\sum\_{i=1}^{m}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})\,\mathbb{E}[L\_{T\_{i}}^{[a\_{l},b\_{l}]}]-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s})=\sum\_{i=1}^{m}\sum\_{j=0}^{n}\left[\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})\,\beta\_{j}^{[a\_{l},b\_{l}]}q\_{ij}\right]-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}), |  |

which can be written in matrix form as in ([5](https://arxiv.org/html/2602.08039v1#S3.E5 "In Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility")).
The proof is completed.
□\square

## 9 Proofs of Theorems [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem1 "Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility") and [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem2 "Theorem 3.2 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")

Proof of Theorem [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem1 "Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility").
The sufficiency part (i.e., LP Feasibility ⇒\Rightarrow Weak Compatibility) follows directly from Theorem [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem2 "Theorem 3.2 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility").
We now prove the necessity part (i.e., Weak Compatibility ⇒\Rightarrow LP Feasibility).

Assume that the market prices of CDO tranches 𝐬\mathbf{s} is weakly compatible.
By definition, there exists a copula C∈𝒞0C\in\mathcal{C}\_{0} such that the following fair value condition holds.

|  |  |  |
| --- | --- | --- |
|  | v[al,bl]​(C;𝐬)=0for 1≤l≤M.v^{[a\_{l},b\_{l}]}(C;\mathbf{s})=0\quad\text{for $1\leq l\leq M$}. |  |

Let Q={qi​j}1≤i≤m, 0≤j≤nQ=\{q\_{ij}\}\_{1\leq i\leq m,\,0\leq j\leq n} denote the DPM associated with this copula CC.
We shall show that QQ constitutes a feasible solution to the system of linear constraints ([8](https://arxiv.org/html/2602.08039v1#S3.E8 "In Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")).
According to Proposition [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmProposition2 "Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility"), the condition v[al,bl]​(C;𝐬)=0v^{[a\_{l},b\_{l}]}(C;\mathbf{s})=0 for 1≤l≤M1\leq l\leq M is equivalent to the first set of linear constraints in ([8](https://arxiv.org/html/2602.08039v1#S3.E8 "In Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")).
Since QQ is a valid DPM, it satisfies the sufficient and necessary condition given in (iii) of Proposition [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmProposition1 "Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility"), which corresponds to the second, fourth, and fifth sets of constraints in ([8](https://arxiv.org/html/2602.08039v1#S3.E8 "In Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")).
Moreover, by the definition of the DPM, the expected number of defaults at each TiT\_{i} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[NTi]=∑j=0nj​qi​jfor 1≤i≤m.\displaystyle\mathbb{E}[N\_{T\_{i}}]=\sum\_{j=0}^{n}j\,q\_{ij}\quad\text{for $1\leq i\leq m$}. |  | (37) |

On the other hand, by the definition of NTiN\_{T\_{i}},
simple algebra yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[NTi]=𝔼​[∑j=1n𝟏{τj≤t}]=n​F​(Ti)for 1≤i≤m.\displaystyle\mathbb{E}[N\_{T\_{i}}]=\mathbb{E}\left[\sum\_{j=1}^{n}\mathbf{1}\_{\{\tau\_{j}\leq t\}}\right]=n\,F(T\_{i})\quad\text{for $1\leq i\leq m$}. |  | (38) |

Then we conclude from ([37](https://arxiv.org/html/2602.08039v1#S9.E37 "In 9 Proofs of Theorems 3.1 and 3.2")) and ([38](https://arxiv.org/html/2602.08039v1#S9.E38 "In 9 Proofs of Theorems 3.1 and 3.2")) that QQ also satisfies the third set of constraints in ([8](https://arxiv.org/html/2602.08039v1#S3.E8 "In Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")). Therefore, we have proved that the DPM QQ associated with the copula CC satisfies all five sets of linear constraints in ([8](https://arxiv.org/html/2602.08039v1#S3.E8 "In Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")) and thus constitutes a feasible solution to  ([8](https://arxiv.org/html/2602.08039v1#S3.E8 "In Theorem 3.1 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility")).
□\square

Proof of Theorem [3.2](https://arxiv.org/html/2602.08039v1#S3.ThmTheorem2 "Theorem 3.2 ‣ 3.3 A Sufficient and Necessary Condition for Weak Compatibility ‣ 3 Weak Compatibility").
For ease of exposition, define Q^:={q^i​j}1≤i≤m,0≤j≤n\hat{Q}:=\{\hat{q}\_{ij}\}\_{1\leq i\leq m,0\leq j\leq n}.
By taking the following four steps, we will construct an exchangeable copula C^∈𝒞0\hat{C}\in\mathcal{C}\_{0} (with DPM equal to Q^\hat{Q}) that perfectly fits all market prices.

*Step 1. Constructing a sequence of ordered, non-negative random variables (τ~1,…,τ~n)(\tilde{\tau}\_{1},\ldots,\tilde{\tau}\_{n}).*
Augment Q^\hat{Q} by setting q^0​j=𝟏{j=0}\hat{q}\_{0j}=\mathbf{1}\_{\{j=0\}} for T0=0T\_{0}=0 and q^m+1,j=𝟏{j=n}\hat{q}\_{m+1,j}=\mathbf{1}\_{\{j=n\}} for Tm+1>TT\_{m+1}>T.
Consider a random variable U∼𝒰​(0,1)U\sim\mathcal{U}(0,1), and define a sequence of non-negative random variables as follows:

|  |  |  |
| --- | --- | --- |
|  | τ~j:=∑i=1m+1Ti+Ti−12​ 1{∑k≥jq^i−1,k<U≤∑k≥jq^i​k}for 1≤j≤n.\tilde{\tau}\_{j}:=\sum\_{i=1}^{m+1}\frac{T\_{i}+T\_{i-1}}{2}\,\mathbf{1}\_{\left\{\sum\_{k\geq j}\hat{q}\_{i-1,k}<U\leq\sum\_{k\geq j}\hat{q}\_{ik}\right\}}\quad\text{for $1\leq j\leq n$}. |  |

Since (τ~1,…,τ~n)(\tilde{\tau}\_{1},\ldots,\tilde{\tau}\_{n}) are defined in the same way as (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}) in ([32](https://arxiv.org/html/2602.08039v1#S8.E32 "In 8 Proofs of Propositions 3.1 and 3.2")), they possess the same properties (i) and (ii) as for (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}) (see part (III) of the proof of Proposition [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmProposition1 "Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility")).
Specifically, (τ~1,…,τ~n)(\tilde{\tau}\_{1},\ldots,\tilde{\tau}\_{n}) have the following two properties, where property (i) exactly means that (τ~1,…,τ~n)(\tilde{\tau}\_{1},\ldots,\tilde{\tau}\_{n}) are ordered.

(i) They are ordered, i.e., τ~1≤τ~2≤⋯≤τ~n\tilde{\tau}\_{1}\leq\tilde{\tau}\_{2}\leq\cdots\leq\tilde{\tau}\_{n}.

(ii) It holds that {τ~j≤Ti}≡{U≤∑k≥jq^i​k}\{\tilde{\tau}\_{j}\leq T\_{i}\}\equiv\{U\leq\sum\_{k\geq j}\hat{q}\_{ik}\} for 1≤i≤m+11\leq i\leq m+1 and 1≤j≤n1\leq j\leq n.

Because (τ~1,…,τ~n)(\tilde{\tau}\_{1},\ldots,\tilde{\tau}\_{n}) are ordered, non-negative random variables, we can regard them as ordered default times. Then we know from part (III) of the proof of Proposition [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmProposition1 "Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility") that (τ~1,…,τ~n)(\tilde{\tau}\_{1},\ldots,\tilde{\tau}\_{n}) possesses the following property (iii).

(iii) The DPM of (τ~1,…,τ~n)(\tilde{\tau}\_{1},\ldots,\tilde{\tau}\_{n}) equals Q^\hat{Q}.

Applying the above property (ii), we can obtain that for y1,…,yn∈{0,…,m+1}y\_{1},\ldots,y\_{n}\in\{0,\ldots,m+1\},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℙ​(τ~1≤Ty1,…,τ~n≤Tyn)\displaystyle\mathbb{P}(\tilde{\tau}\_{1}\leq T\_{y\_{1}},\ldots,\tilde{\tau}\_{n}\leq T\_{y\_{n}}) | =ℙ​(U≤∑k≥1q^y1,k,…,U≤∑k≥nq^yn,k)\displaystyle=\mathbb{P}\!\left(U\leq\sum\_{k\geq 1}\hat{q}\_{y\_{1},k},\ldots,U\leq\sum\_{k\geq n}\hat{q}\_{y\_{n},k}\right) |  | (39) |
|  |  | =ℙ​(U≤min1≤j≤n⁡{∑k≥jq^yj,k})=min1≤j≤n⁡{∑k≥jq^yj,k}.\displaystyle=\mathbb{P}\!\left(U\leq\min\_{1\leq j\leq n}\!\left\{\sum\_{k\geq j}\hat{q}\_{y\_{j},k}\right\}\right)=\min\_{1\leq j\leq n}\!\left\{\sum\_{k\geq j}\hat{q}\_{y\_{j},k}\right\}. |  |

*Step 2. Constructing exchangeable default times (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}) with DPM equal to Q^\hat{Q}.*
Let 𝒢n\mathcal{G}\_{n} denote the set of all permutations on the set {1,…,n}\{1,\ldots,n\}, and let π\pi be a random permutation uniformly distributed on 𝒢n\mathcal{G}\_{n} that is independent of UU.
Define a sequence of non-negative random variables

|  |  |  |
| --- | --- | --- |
|  | (τ^1,…,τ^n):=(τ~π​(1),…,τ~π​(n)),(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}):=(\tilde{\tau}\_{\pi(1)},\ldots,\tilde{\tau}\_{\pi(n)}), |  |

which can be regarded as default times.
Because (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}) is defined in the same way as (τ^1′,…,τ^n′)(\hat{\tau}^{\prime}\_{1},\ldots,\hat{\tau}^{\prime}\_{n}) in ([30](https://arxiv.org/html/2602.08039v1#S8.E30 "In 8 Proofs of Propositions 3.1 and 3.2")), we conclude that (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}) is also exchangeable (see part (I) of the proof of Proposition [3.1](https://arxiv.org/html/2602.08039v1#S3.ThmProposition1 "Proposition 3.1 ‣ 3.1 The Default Probability Matrix (DPM) ‣ 3 Weak Compatibility")).

Furthermore, define N^t:=∑j=1n𝟏{τ^j≤t}≡∑j=1n𝟏{τ~π​(j)≤t}\hat{N}\_{t}:=\sum\_{j=1}^{n}\mathbf{1}\_{\{\hat{\tau}\_{j}\leq t\}}\equiv\sum\_{j=1}^{n}\mathbf{1}\_{\{\tilde{\tau}\_{\pi(j)}\leq t\}} and N~t:=∑j=1n𝟏{τ~j≤t}\tilde{N}\_{t}:=\sum\_{j=1}^{n}\mathbf{1}\_{\{\tilde{\tau}\_{j}\leq t\}} for t≥0t\geq 0.
Since the two sets {π​(1),⋯,π​(n)}\{\pi(1),\cdots,\pi(n)\} and {1,⋯,n}\{1,\cdots,n\} are identical, it follows that

|  |  |  |
| --- | --- | --- |
|  | N^t=∑j=1n𝟏{τ~j≤t}=N~tfor t≥0.\hat{N}\_{t}=\sum\_{j=1}^{n}\mathbf{1}\_{\{\tilde{\tau}\_{j}\leq t\}}=\tilde{N}\_{t}\quad\text{for $t\geq 0$}. |  |

Therefore, we have ℙ​(N^Ti=j)=ℙ​(N~Ti=j)=q^i​j\mathbb{P}(\hat{N}\_{T\_{i}}=j)=\mathbb{P}(\tilde{N}\_{T\_{i}}=j)=\hat{q}\_{ij} for 1≤i≤m1\leq i\leq m and 0≤j≤n0\leq j\leq n.
Namely, the DPM of (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}) is equal to Q^\hat{Q}.

*Step 3. Proving that for y1,…,yn∈{0,…,m+1}y\_{1},\ldots,y\_{n}\in\{0,\ldots,m+1\},*

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(τ^1≤Ty1,…,τ^n≤Tyn)=1n!​∑σ∈𝒢nmin1≤j≤n⁡{∑k≥σ​(j)q^yj,k}.\displaystyle\mathbb{P}(\hat{\tau}\_{1}\leq T\_{y\_{1}},\ldots,\hat{\tau}\_{n}\leq T\_{y\_{n}})=\frac{1}{n!}\sum\_{\sigma\in\mathcal{G}\_{n}}\min\_{1\leq j\leq n}\!\left\{\sum\_{k\geq\sigma(j)}\hat{q}\_{y\_{j},k}\right\}. |  | (40) |

We can deduce that for y1,…,yn∈{0,…,m+1}y\_{1},\ldots,y\_{n}\in\{0,\ldots,m+1\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(τ^1≤Ty1,…,τ^n≤Tyn)=\displaystyle\mathbb{P}(\hat{\tau}\_{1}\leq T\_{y\_{1}},\ldots,\hat{\tau}\_{n}\leq T\_{y\_{n}})= | 𝔼​[ℙ​(τ~π​(1)≤Ty1,…,τ~π​(n)≤Tyn|π)]\displaystyle\ \mathbb{E}\left[\mathbb{P}(\tilde{\tau}\_{\pi(1)}\leq T\_{y\_{1}},\ldots,\tilde{\tau}\_{\pi(n)}\leq T\_{y\_{n}}|\pi)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑σ∈𝒢n[ℙ​(π=σ)​ℙ​(τ~π​(1)≤Ty1,…,τ~π​(n)≤Tyn|π=σ)]\displaystyle\ \sum\_{\sigma\in\mathcal{G}\_{n}}\left[\mathbb{P}(\pi=\sigma)\mathbb{P}(\tilde{\tau}\_{\pi(1)}\leq T\_{y\_{1}},\ldots,\tilde{\tau}\_{\pi(n)}\leq T\_{y\_{n}}|\pi=\sigma)\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 1n!​∑σ∈𝒢nℙ​(τ~σ​(1)≤Ty1,…,τ~σ​(n)≤Tyn),\displaystyle\frac{1}{n!}\sum\_{\sigma\in\mathcal{G}\_{n}}\mathbb{P}(\tilde{\tau}\_{\sigma(1)}\leq T\_{y\_{1}},\ldots,\tilde{\tau}\_{\sigma(n)}\leq T\_{y\_{n}}), |  | (41) |

where the third equality holds as π\pi is uniformly distributed on 𝒢n\mathcal{G}\_{n} and is independent of (τ~1,…,τ~n)(\tilde{\tau}\_{1},\ldots,\tilde{\tau}\_{n}).

Rearranging the terms inside the probabilities on the right hand side of ([41](https://arxiv.org/html/2602.08039v1#S9.E41 "In 9 Proofs of Theorems 3.1 and 3.2")) and then applying  ([39](https://arxiv.org/html/2602.08039v1#S9.E39 "In 9 Proofs of Theorems 3.1 and 3.2")) yields

|  |  |  |
| --- | --- | --- |
|  | ℙ​(τ^1≤Ty1,…,τ^n≤Tyn)=1n!​∑σ∈𝒢nℙ​(τ~1≤Tyσ−1​(1),…,τ~n≤Tyσ−1​(n))=1n!​∑σ∈𝒢nmin1≤l≤n⁡{∑k≥lq^yσ−1​(l),k}.\begin{split}\mathbb{P}(\hat{\tau}\_{1}\leq T\_{y\_{1}},\ldots,\hat{\tau}\_{n}\leq T\_{y\_{n}})&=\frac{1}{n!}\sum\_{\sigma\in\mathcal{G}\_{n}}\mathbb{P}(\tilde{\tau}\_{1}\leq T\_{y\_{\sigma^{-1}(1)}},\ldots,\tilde{\tau}\_{n}\leq T\_{y\_{\sigma^{-1}(n)}})\\ &=\frac{1}{n!}\sum\_{\sigma\in\mathcal{G}\_{n}}\min\_{1\leq l\leq n}\!\left\{\sum\_{k\geq l}\hat{q}\_{y\_{\sigma^{-1}(l)},k}\right\}.\end{split} |  |

By setting j=σ−1​(l)j=\sigma^{-1}(l) (and thus l=σ​(j)l=\sigma(j)), we can obtain ([40](https://arxiv.org/html/2602.08039v1#S9.E40 "In 9 Proofs of Theorems 3.1 and 3.2")) immediately.

*Step 4. Constructing an exchangeable copula C^∈𝒞0\hat{C}\in\mathcal{C}\_{0} (with DPM equal to Q^\hat{Q}) that perfectly fits all market prices.*
Define C^\hat{C} to be the copula of (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}) constructed in Step 2 above.
For uj:=F​(Tyj)u\_{j}:=F(T\_{y\_{j}}) (1≤j≤n1\leq j\leq n), applying Sklar’s theorem and then using ([40](https://arxiv.org/html/2602.08039v1#S9.E40 "In 9 Proofs of Theorems 3.1 and 3.2")) yields

|  |  |  |
| --- | --- | --- |
|  | C^​(u1,…,un)=ℙ​(τ^1≤Ty1,…,τ^n≤Tyn)=1n!​∑σ∈𝒢nmin1≤j≤n⁡{∑k≥σ​(j)q^yj,k}.\hat{C}(u\_{1},\ldots,u\_{n})=\mathbb{P}(\hat{\tau}\_{1}\leq T\_{y\_{1}},\ldots,\hat{\tau}\_{n}\leq T\_{y\_{n}})=\frac{1}{n!}\sum\_{\sigma\in\mathcal{G}\_{n}}\min\_{1\leq j\leq n}\!\left\{\sum\_{k\geq\sigma(j)}\hat{q}\_{y\_{j},k}\right\}. |  |

Furthermore, we know from Step 2 above that (τ^1,…,τ^n)(\hat{\tau}\_{1},\ldots,\hat{\tau}\_{n}) is exchangeable with DPM equal to Q^\hat{Q}. This implies that C^\hat{C} is exchangeable and its associated DPM equals Q^\hat{Q}. Therefore, C^\hat{C} can perfectly fit all market prices. The proof is completed.
□\square

## 10 Proofs of Propositions [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmProposition1 "Proposition 4.1 (Stochastic Distortion Representations of Conditionally I.I.D. Copulas) ‣ 4.1 Conditionally I.I.D. Models and Stochastic Distortions ‣ 4 Strong Compatibility"), [4.2](https://arxiv.org/html/2602.08039v1#S4.ThmProposition2 "Proposition 4.2 ‣ 4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility") and [4.4](https://arxiv.org/html/2602.08039v1#S4.ThmProposition4 "Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")

Proof of Proposition [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmProposition1 "Proposition 4.1 (Stochastic Distortion Representations of Conditionally I.I.D. Copulas) ‣ 4.1 Conditionally I.I.D. Models and Stochastic Distortions ‣ 4 Strong Compatibility").
(I) Proof of (i) ⇒\Rightarrow (ii).
Assume that {Uk}k∈ℕ+{\{U\_{k}\}}\_{k\in\mathbb{N}^{+}} are i.i.d. conditional on a σ\sigma-field ℋ⊆ℱ\mathcal{H}\subseteq\mathcal{F}.
Define a stochastic process X​(u):=ℙ​(U1≤u|ℋ)X(u):=\mathbb{P}(U\_{1}\leq u|\mathcal{H}) for u∈[0,1]u\in[0,1].
Since U1∼𝒰​(0,1)U\_{1}\sim\mathcal{U}(0,1), it is straightforward to check that {X​(u):u∈[0,1]}\{X(u):u\in[0,1]\} is a stochastic distortion that satisfies 𝔼​[X​(u)]=u\mathbb{E}[X(u)]=u for any u∈[0,1]u\in[0,1]. Therefore, we know that CX​(u1,…,un):=𝔼​[∏j=1nX​(uj)]C^{X}(u\_{1},\ldots,u\_{n}):=\mathbb{E}\left[\prod\_{j=1}^{n}X(u\_{j})\right] is the transformed copula by the stochastic distortion XX. Then
we can obtain that for any n≥2n\geq 2, the copula CC of (U1,…,Un)(U\_{1},\ldots,U\_{n}) is given by

|  |  |  |
| --- | --- | --- |
|  | C​(u1,…,un)=ℙ​(U1≤u1,…,Un≤un)=𝔼​[ℙ​(U1≤u1,…,Un≤un|ℋ)]=𝔼​[∏j=1nℙ​(Uj≤uj|ℋ)]=𝔼​[∏j=1nX​(uj)]=CX​(u1,…,un),\begin{split}C(u\_{1},\ldots,u\_{n})&=\mathbb{P}(U\_{1}\leq u\_{1},\ldots,U\_{n}\leq u\_{n})=\mathbb{E}[\mathbb{P}(U\_{1}\leq u\_{1},\ldots,U\_{n}\leq u\_{n}|\mathcal{H})]\\ &=\mathbb{E}\left[\prod\_{j=1}^{n}\mathbb{P}(U\_{j}\leq u\_{j}|\mathcal{H})\right]=\mathbb{E}\left[\prod\_{j=1}^{n}X(u\_{j})\right]=C^{X}(u\_{1},\ldots,u\_{n}),\end{split} |  |

where the third equality follows from the conditional independence of {Uk}k∈ℕ+{\{U\_{k}\}}\_{k\in\mathbb{N}^{+}}.

(II) Proof of (ii) ⇒\Rightarrow (i).
Assume that there exists a stochastic distortion XX with 𝔼​[X​(u)]=u\mathbb{E}[X(u)]=u for any u∈[0,1]u\in[0,1] such that for any n≥2n\geq 2, the copula CC of (U1,…,Un)(U\_{1},\ldots,U\_{n}) admits the stochastic distortion representation given by ([14](https://arxiv.org/html/2602.08039v1#S4.E14 "In item 2 ‣ Proposition 4.1 (Stochastic Distortion Representations of Conditionally I.I.D. Copulas) ‣ 4.1 Conditionally I.I.D. Models and Stochastic Distortions ‣ 4 Strong Compatibility")).
Let σ\sigma be any permutation on the set {1,…,n}\{1,\ldots,n\}.
Then we have

|  |  |  |
| --- | --- | --- |
|  | C​(uσ​(1),…,uσ​(n))=𝔼​[∏j=1nX​(uσ​(j))]=𝔼​[∏j=1nX​(uj)]=C​(u1,…,un),C(u\_{\sigma(1)},\ldots,u\_{\sigma(n)})=\mathbb{E}\left[\prod\_{j=1}^{n}X(u\_{\sigma(j)})\right]=\mathbb{E}\left[\prod\_{j=1}^{n}X(u\_{j})\right]=C(u\_{1},\ldots,u\_{n}), |  |

which implies that (U1,…,Un)(U\_{1},\ldots,U\_{n}) is exchangeable. Since this holds for any arbitrary n≥2n\geq 2, we conclude that {Uk}k∈ℕ+{\{U\_{k}\}}\_{k\in\mathbb{N}^{+}} is infinitely exchangeable by definition. According to de Finetti’s Theorem (see, e.g., Mai [2020](https://arxiv.org/html/2602.08039v1#bib.bib2 "The infinite extendibility problem for exchangeable real-valued random vectors")), we obtain the result (i) immediately. The proof is completed.
□\square

Proof of Proposition [4.2](https://arxiv.org/html/2602.08039v1#S4.ThmProposition2 "Proposition 4.2 ‣ 4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility").
By the properties of gamma processes, both {ξt:t≥0}\{\xi\_{t}:t\geq 0\} and {ηt:t≥0}\{\eta\_{t}:t\geq 0\} are non-negative and non-decreasing processes. Therefore, it holds that

|  |  |  |
| --- | --- | --- |
|  | ξϕ​(u1)≤ξϕ​(u2)andηN−ϕ​(u1)≥ηN−ϕ​(u2)a.s.for any 0<u1<u2<1,\xi\_{\phi(u\_{1})}\leq\xi\_{\phi(u\_{2})}\quad\text{and}\quad\eta\_{N-\phi(u\_{1})}\geq\eta\_{N-\phi(u\_{2})}\quad\text{a.s.}\quad\text{for any $0<u\_{1}<u\_{2}<1$}, |  |

where we also use the fact that {ϕ​(u)}\{\phi(u)\} is non-decreasing. Then we can deduce that for any 0<u1<u2<10<u\_{1}<u\_{2}<1,

|  |  |  |
| --- | --- | --- |
|  | X​(u1)=ξϕ​(u1)ξϕ​(u1)+ηN−ϕ​(u1)≤ξϕ​(u2)ξϕ​(u2)+ηN−ϕ​(u1)≤ξϕ​(u2)ξϕ​(u2)+ηN−ϕ​(u2)=X​(u2)a.s.,X(u\_{1})=\frac{\xi\_{\phi(u\_{1})}}{\xi\_{\phi(u\_{1})}+\eta\_{N-\phi(u\_{1})}}\leq\frac{\xi\_{\phi(u\_{2})}}{\xi\_{\phi(u\_{2})}+\eta\_{N-\phi(u\_{1})}}\leq\frac{\xi\_{\phi(u\_{2})}}{\xi\_{\phi(u\_{2})}+\eta\_{N-\phi(u\_{2})}}=X(u\_{2})\quad\text{a.s.}, |  |

which means that {X​(u):u∈[0,1]}\{X(u):u\in[0,1]\} is non-decreasing a.s.. In addition, note that ξ0=η0=0\xi\_{0}=\eta\_{0}=0, ϕ​(0)=0\phi(0)=0, ϕ​(1)=N\phi(1)=N a.s.. It follows that X​(0)=0X(0)=0 and X​(1)=1X(1)=1 a.s.. Therefore, {X​(u)}\{X(u)\} is a stochastic distortion.

Furthermore, we can deduce that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[X​(u)]=𝔼​[𝔼​[X​(u)∣ϕ​(u)]]=𝔼​[ϕ​(u)ϕ​(u)+(N−ϕ​(u))]=ufor 0<u<1,\mathbb{E}[X(u)]=\mathbb{E}\big[\mathbb{E}[X(u)\mid\phi(u)]\big]=\mathbb{E}\!\left[\frac{\phi(u)}{\phi(u)+(N-\phi(u))}\right]=u\quad\text{for $0<u<1$}, |  |

where the second equality holds because conditional on ϕ​(u)\phi(u), X​(u)X(u) follows a Beta distribution with parameters ϕ​(u)\phi(u) and N−ϕ​(u)N-\phi(u). The proof is completed. □\square

Proof of Proposition [4.4](https://arxiv.org/html/2602.08039v1#S4.ThmProposition4 "Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility").
Define Vi​k:={θi,k−1<U≤θi​k}V\_{ik}:=\left\{\theta\_{i,k-1}<U\leq\theta\_{ik}\right\} for 0≤i≤m+10\leq i\leq m+1 and 0≤k≤N0\leq k\leq N, where θi​k:=∑j≤kp^i​j\theta\_{ik}:=\sum\_{j\leq k}\hat{p}\_{ij} for 0≤i≤m+10\leq i\leq m+1 and 0≤k≤N0\leq k\leq N and θi,−1:=0\theta\_{i,-1}:=0.
Applying the fourth set of constraints (i.e., the non-negativity constraints) of ([22](https://arxiv.org/html/2602.08039v1#S4.E22 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) yields directly that 0≡θi,−1≤θi​0≤⋯≤θi​N0\equiv\theta\_{i,-1}\leq\theta\_{i0}\leq\cdots\leq\theta\_{iN} for all 0≤i≤m+10\leq i\leq m+1.
Moreover, we know from the first set of constraints (i.e., the sum-to-one constraints) of ([22](https://arxiv.org/html/2602.08039v1#S4.E22 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) that θi​N≡1\theta\_{iN}\equiv 1.
Therefore, we conclude that for any i=0,⋯,m+1i=0,\cdots,m+1, Vi​0,Vi​1,⋯,Vi​NV\_{i0},V\_{i1},\cdots,V\_{iN} is a partition of the complete set.
Using this partition result and noticing that ϕ​(F​(Ti))\phi(F(T\_{i})) can be rewritten as
ϕ​(F​(Ti))=∑k=0Nk​𝟏Vi​k\phi(F(T\_{i}))=\sum\_{k=0}^{N}k\mathbf{1}\_{V\_{ik}} for any i=0,⋯,m+1i=0,\cdots,m+1,
we can obtain that for any i=0,⋯,m+1i=0,\cdots,m+1 and k=0,⋯,Nk=0,\cdots,N,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(F​(Ti))=k\phi(F(T\_{i}))=k if and only if θi,k−1<U≤θi​k\theta\_{i,k-1}<U\leq\theta\_{ik} (i.e., Vi​kV\_{ik} happens). |  | (42) |

For any i=0,⋯,m+1i=0,\cdots,m+1 and k=0,⋯,Nk=0,\cdots,N, if ϕ​(F​(Ti))=k\phi(F(T\_{i}))=k, then we have θi,k−1<U≤θi​k\theta\_{i,k-1}<U\leq\theta\_{ik}.
This further implies that U>θi+1,k−1U>\theta\_{i+1,k-1} because θi+1,k−1≤θi,k−1\theta\_{i+1,k-1}\leq\theta\_{i,k-1} due to the third set of constraints (i.e., the monotonicity constraints) of ([22](https://arxiv.org/html/2602.08039v1#S4.E22 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")).
Then using the result ([42](https://arxiv.org/html/2602.08039v1#S10.E42 "In 10 Proofs of Propositions 4.1, 4.2 and 4.4")) again yields that ϕ​(F​(Ti+1))≥k=ϕ​(F​(Ti))\phi(F(T\_{i+1}))\geq k=\phi(F(T\_{i})).
Therefore, we have ϕ​(F​(T0))≤ϕ​(F​(T1))≤⋯≤ϕ​(F​(Tm+1))\phi(F(T\_{0}))\leq\phi(F(T\_{1}))\leq\cdots\leq\phi(F(T\_{m+1})).
Since ϕ​(u)\phi(u) is a linear interpolation of ϕ​(F​(Ti))\phi(F(T\_{i})) and ϕ​(F​(Ti+1))\phi(F(T\_{i+1})) for any u∈(F​(Ti),F​(Ti+1))u\in(F(T\_{i}),F(T\_{i+1})) and i=0,⋯,mi=0,\cdots,m, we conclude that {ϕ​(u)}\{\phi(u)\} is a non-decreasing stochastic process.

In addition, it is straightforward to verify that ϕ​(0)=0\phi(0)=0 and ϕ​(1)=N\phi(1)=N.
Furthermore, we know from the result ([42](https://arxiv.org/html/2602.08039v1#S10.E42 "In 10 Proofs of Propositions 4.1, 4.2 and 4.4")) that the distribution of ϕ​(F​(Ti))\phi(F(T\_{i})) is given by ([24](https://arxiv.org/html/2602.08039v1#S4.E24 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")).
Then we can deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​(ϕ​(F​(Ti)))=∑k=0Nk​p^i​k=N​F​(Ti)for any i=1,⋯,m,\displaystyle\mathbb{E}(\phi(F(T\_{i})))=\sum\_{k=0}^{N}k\hat{p}\_{ik}=NF(T\_{i})\quad\text{for any $i=1,\cdots,m$}, |  | (43) |

where the second equality holds due to the second set of constraints of ([22](https://arxiv.org/html/2602.08039v1#S4.E22 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")).
Using the fact that ϕ​(u)\phi(u) is a linear interpolation of ϕ​(F​(Ti))\phi(F(T\_{i})) and ϕ​(F​(Ti+1))\phi(F(T\_{i+1})) for any u∈(F​(Ti),F​(Ti+1))u\in(F(T\_{i}),F(T\_{i+1})) and i=0,⋯,mi=0,\cdots,m, we obtain that 𝔼​(ϕ​(u))=u\mathbb{E}(\phi(u))=u for any 0≤u≤10\leq u\leq 1.

Thus, we have shown that {ϕ​(u):0≤u≤1}\{\phi(u):0\leq u\leq 1\} defined in ([23](https://arxiv.org/html/2602.08039v1#S4.E23 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) is a non-decreasing stochastic process satisfying ([17](https://arxiv.org/html/2602.08039v1#S4.E17 "In 4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility")) and ([24](https://arxiv.org/html/2602.08039v1#S4.E24 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")). □\Box

## 11 Proofs of Theorems [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem1 "Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") and [4.2](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem2 "Theorem 4.2 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")

Proof of Theorem [4.1](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem1 "Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility").
The first implication (𝐬∈𝒜∘⇒\mathbf{s}\in\mathcal{A}^{\circ}\Rightarrow LP feasibility) follows directly from Proposition [4.3](https://arxiv.org/html/2602.08039v1#S4.ThmProposition3 "Proposition 4.3 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility"), whose proof will be given in Section [12](https://arxiv.org/html/2602.08039v1#S12 "12 Proof of Proposition 4.3").
Conversely, the second implication (LP feasibility ⇒𝐬∈𝒜\Rightarrow\mathbf{s}\in\mathcal{A}) is ensured by Theorem [4.2](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem2 "Theorem 4.2 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility"), which constructs a concrete conditionally i.i.d. copula that achieves a perfect fit to the market prices 𝐬\mathbf{s}.
□\square

Proof of Theorem [4.2](https://arxiv.org/html/2602.08039v1#S4.ThmTheorem2 "Theorem 4.2 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility").
Given that {p^i​k}1≤i≤m,0≤k≤N\{\hat{p}\_{ik}\}\_{1\leq i\leq m,0\leq k\leq N} is a feasible solution to the system of linear constraints ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) (the last four sets of which are exactly the linear constraints in ([22](https://arxiv.org/html/2602.08039v1#S4.E22 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility"))), we know from Proposition [4.4](https://arxiv.org/html/2602.08039v1#S4.ThmProposition4 "Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") that {ϕ​(u):0≤u≤1}\{\phi(u):0\leq u\leq 1\} defined in ([23](https://arxiv.org/html/2602.08039v1#S4.E23 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) via this feasible solution is a non-decreasing stochastic process satisfying ([17](https://arxiv.org/html/2602.08039v1#S4.E17 "In 4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility")), and thus it is qualified to serve as a generator of a discrete gamma distortion.
Moreover, the distribution of ϕ​(F​(Ti))\phi(F(T\_{i})) is given by ([24](https://arxiv.org/html/2602.08039v1#S4.E24 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) for any i=1,⋯,mi=1,\cdots,m.

Accordingly, using {ϕ​(u)}\{\phi(u)\} defined in ([23](https://arxiv.org/html/2602.08039v1#S4.E23 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) and two independent gamma processes {ξt}\{\xi\_{t}\} and {ηt}\{\eta\_{t}\} that are also independent of {ϕ​(u)}\{\phi(u)\}, we can construct a discrete gamma distortion {X​(u)}\{X(u)\} based on ([18](https://arxiv.org/html/2602.08039v1#S4.E18 "In 4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility")) and then denote by CXC^{X} the corresponding discrete gamma-distorted copula. It follows from ([19](https://arxiv.org/html/2602.08039v1#S4.E19 "In 4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility")) and ([24](https://arxiv.org/html/2602.08039v1#S4.E24 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) that the DPM QQ associated with CXC^{X} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi​j=∑k=0Nhj​k(N)​p^i​kfor 1≤i≤m and 0≤j≤n.\displaystyle q\_{ij}=\sum\_{k=0}^{N}h\_{jk}^{(N)}\hat{p}\_{ik}\quad\text{for $1\leq i\leq m$ and $0\leq j\leq n$.} |  | (44) |

Then we can deduce that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v[al,bl]​(CX;𝐬)=\displaystyle v^{[a\_{l},b\_{l}]}(C^{X};\mathbf{s})= | ∑i=1m∑j=0nλi[al,bl]​(𝐬)​βj[al,bl]​qi​j−γ[al,bl]​(𝐬)\displaystyle\ \sum\_{i=1}^{m}\sum\_{j=0}^{n}\lambda^{[a\_{l},b\_{l}]}\_{i}(\mathbf{s})\beta\_{j}^{[a\_{l},b\_{l}]}q\_{ij}-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}) |  | (45) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑i=1m∑j=0n∑k=0Nhj​k(N)​λi[al,bl]​(𝐬)​βj[al,bl]​p^i​k−γ[al,bl]​(𝐬)\displaystyle\ \sum\_{i=1}^{m}\sum\_{j=0}^{n}\sum\_{k=0}^{N}h\_{jk}^{(N)}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})\beta\_{j}^{[a\_{l},b\_{l}]}\hat{p}\_{ik}-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 0for 1≤l≤M,\displaystyle\ 0\quad\text{for $1\leq l\leq M$,} |  | (46) |

where the first equality follows from ([5](https://arxiv.org/html/2602.08039v1#S3.E5 "In Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility")), the second equality is obtained from ([44](https://arxiv.org/html/2602.08039v1#S11.E44 "In 11 Proofs of Theorems 4.1 and 4.2")), and the third equality holds due to the first set of constraints in ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")).
Hence, we conclude that the copula CXC^{X} achieves a perfect fit to the market prices 𝐬\mathbf{s}. The proof is completed.
□\square

## 12 Proof of Proposition [4.3](https://arxiv.org/html/2602.08039v1#S4.ThmProposition3 "Proposition 4.3 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")

### 12.1 Preliminary Preparations

Before proving Proposition [4.3](https://arxiv.org/html/2602.08039v1#S4.ThmProposition3 "Proposition 4.3 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility"), we first introduce some notations and present two lemmas as preparation.

For any N∈ℕ+N\in\mathbb{N}^{+}, denote by 𝒫(N)\mathcal{P}^{(N)} the feasible region to the following system of linear constraints ([47](https://arxiv.org/html/2602.08039v1#S12.E47 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) (note that ([47](https://arxiv.org/html/2602.08039v1#S12.E47 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) is the same as ([22](https://arxiv.org/html/2602.08039v1#S4.E22 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) except that the superscript (N)(N) is added to highlight the dependence of all the variables on NN).

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∑k=0Np^i​k(N)=1for ​1≤i≤m,∑k=0Nk​p^i​k(N)=N​F​(Ti)for ​1≤i≤m,∑j≥kp^i​j(N)≤∑j≥kp^i+1,j(N)for 0≤k≤N and 1≤i≤m−1,p^i​k(N)≥0,for 1≤i≤m and 0≤k≤N.\begin{cases}\sum\_{k=0}^{N}\hat{p}\_{ik}^{(N)}=1\,&\text{for }1\leq i\leq m,\\ \sum\_{k=0}^{N}k\hat{p}\_{ik}^{(N)}=NF(T\_{i})\,&\text{for }1\leq i\leq m,\\ \sum\_{j\geq k}\hat{p}\_{ij}^{(N)}\leq\sum\_{j\geq k}\hat{p}\_{i+1,j}^{(N)}\,&\text{for $0\leq k\leq N$ and $1\leq i\leq m-1$},\\ \hat{p}\_{ik}^{(N)}\geq 0,\,&\text{for $1\leq i\leq m$ and $0\leq k\leq N$}.\end{cases} |  | (47) |

For each matrix P^(N)={p^i​k(N)}1≤i≤m,0≤k≤N∈𝒫(N)\hat{P}^{(N)}=\{\hat{p}^{(N)}\_{ik}\}\_{1\leq i\leq m,0\leq k\leq N}\in\mathcal{P}^{(N)}, Proposition [4.4](https://arxiv.org/html/2602.08039v1#S4.ThmProposition4 "Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") ensures the existence of a discrete gamma-distorted copula CXC^{X} whose generator ϕ\phi satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ϕ​(F​(Ti))=k)=p^i​k(N)for 1≤i≤m,0≤k≤N.\mathbb{P}(\phi(F(T\_{i}))=k)=\hat{p}\_{ik}^{(N)}\quad\text{for $1\leq i\leq m,0\leq k\leq N$}. |  | (48) |

Consequently, given 𝐬∈ℝ2​M\mathbf{s}\in\mathbb{R}^{2M}, we can abuse the notation of v[al,bl]v^{[a\_{l},b\_{l}]}, using v[al,bl]​(P^(N);𝐬)v^{[a\_{l},b\_{l}]}(\hat{P}^{(N)};\mathbf{s}) to denote the value of v[al,bl]​(CX;𝐬)v^{[a\_{l},b\_{l}]}(C^{X};\mathbf{s}) when the copula CXC^{X} is a discrete gamma distorted copula whose generator satisfies ([48](https://arxiv.org/html/2602.08039v1#S12.E48 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")).
Specifically, by substituting ([19](https://arxiv.org/html/2602.08039v1#S4.E19 "In 4.3 Gamma Distortions and Gamma-Distorted Copulas ‣ 4 Strong Compatibility")) into ([5](https://arxiv.org/html/2602.08039v1#S3.E5 "In Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | v[al,bl]​(P^(N);𝐬)=∑i=1m∑j=0n∑k=0Nhj​k(N)​λi[al,bl]​(𝐬)​βj[al,bl]​p^i​k(N)−γ[al,bl]​(𝐬)for 1≤l≤M.v^{[a\_{l},b\_{l}]}(\hat{P}^{(N)};\mathbf{s})=\sum\_{i=1}^{m}\sum\_{j=0}^{n}\sum\_{k=0}^{N}h\_{jk}^{(N)}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})\beta\_{j}^{[a\_{l},b\_{l}]}\hat{p}\_{ik}^{(N)}-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s})\quad\text{for $1\leq l\leq M$}. |  | (49) |

Furthermore, we define 𝐯​(P^(N);𝐬):=(v[a1,b1]​(P^(N);𝐬),…,v[aM,bM]​(P^(N);𝐬))∈ℝM\mathbf{v}({\hat{P}^{(N)};\mathbf{s}}):=(v^{[a\_{1},b\_{1}]}(\hat{P}^{(N)};\mathbf{s}),\ldots,v^{[a\_{M},b\_{M}]}(\hat{P}^{(N)};\mathbf{s}))\in\mathbb{R}^{M}.

The following lemma shows that for each 𝐬∈𝒜∘\mathbf{s}\in\mathcal{A}^{\circ}, there exists a sequence of matrices in 𝒫(N)\mathcal{P}^{(N)} such that the corresponding values of 𝐯​(P^(N);𝐬)\mathbf{v}(\hat{P}^{(N)};\mathbf{s}) converge to the zero vector as NN goes to infinity.

###### Lemma 12.1

For each 𝐬∈𝒜\mathbf{s}\in\mathcal{A}, let X𝐬X\_{\mathbf{s}} be a stochastic distortion such that its transformed copula CX𝐬C^{X\_{\mathbf{s}}} provides a perfect fit for 𝐬\mathbf{s}.
Then there exists a sequence of matrices P^(N)​(X𝐬)∈𝒫(N)\hat{P}^{(N)}(X\_{\mathbf{s}})\in\mathcal{P}^{(N)} for N∈ℕ+N\in\mathbb{N}^{+} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN→+∞‖𝐯​(P^(N)​(X𝐬);𝐬)‖=0,\lim\_{N\to+\infty}\|\mathbf{v}(\hat{P}^{(N)}(X\_{\mathbf{s}});\mathbf{s})\|=0, |  | (50) |

where ∥⋅∥\|\cdot\| is the maximum norm.

Proof.
The proof is divided into three steps.
First, we construct the matrices P^(N)​(X𝐬)∈𝒫(N)\hat{P}^{(N)}(X\_{\mathbf{s}})\in\mathcal{P}^{(N)} for N∈ℕ+N\in\mathbb{N}^{+} based on the stochastic distortion X𝐬X\_{\mathbf{s}}.
Second, we show that these matrices can be used to construct gamma distortions X𝐬(N)X\_{\mathbf{s}}^{(N)} for N∈ℕ+N\in\mathbb{N}^{+}, and that X𝐬(N)​(F​(Ti))X\_{\mathbf{s}}^{(N)}(F(T\_{i})) converges in distribution to X𝐬​(F​(Ti))X\_{\mathbf{s}}(F(T\_{i})) as NN goes to +∞+\infty for 1≤i≤m1\leq i\leq m.
Third, we prove the convergence result ([50](https://arxiv.org/html/2602.08039v1#S12.E50 "In Lemma 12.1 ‣ 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")).

Step 1. Constructing matrices P^(N)​(X𝐬)∈𝒫(N)\hat{P}^{(N)}(X\_{\mathbf{s}})\in\mathcal{P}^{(N)} for N∈ℕ+N\in\mathbb{N}^{+}.
For each N∈ℕ+N\in\mathbb{N}^{+}, we define the matrix P^(N)​(X𝐬)={p^i​k(N)​(X𝐬)}1≤i≤m,0≤k≤N\hat{P}^{(N)}(X\_{\mathbf{s}})=\{\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})\}\_{1\leq i\leq m,0\leq k\leq N} as follows:

|  |  |  |
| --- | --- | --- |
|  | p^i​k(N)​(X𝐬):=∫((k−1)/N,(k+1)/N)(1−|N​y−k|)​dGX𝐬​(F​(Ti))​(y)for 0≤k≤N and 1≤i≤m,\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}}):=\int\_{((k-1)/N,(k+1)/N)}(1-|Ny-k|)\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y)\quad\text{for $0\leq k\leq N$ and $1\leq i\leq m$}, |  |

where GX𝐬​(F​(Ti))G\_{X\_{\mathbf{s}}(F(T\_{i}))} is the distribution function of the random variable X𝐬​(F​(Ti))X\_{\mathbf{s}}(F(T\_{i})).
We shall verify that P^(N)​(X𝐬)∈𝒫(N)\hat{P}^{(N)}(X\_{\mathbf{s}})\in\mathcal{P}^{(N)}.
To this end, we check the four sets of constraints in ([47](https://arxiv.org/html/2602.08039v1#S12.E47 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) one by one.

First, we note the identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=0N𝟏{(k−1)/N<y<(k+1)/N}​(1−|N​y−k|)=1for y∈[0,1] and N∈ℕ+.\sum\_{k=0}^{N}\mathbf{1}\_{\{(k-1)/N<y<(k+1)/N\}}(1-|Ny-k|)=1\quad\text{for $y\in[0,1]$ and $N\in\mathbb{N}^{+}$}. |  | (51) |

We can verify the first set of linear constraints as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=0Np^i​k(N)​(X𝐬)\displaystyle\sum\_{k=0}^{N}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}}) | =∑k=0N∫((k−1)/N,(k+1)/N)(1−|N​y−k|)​dGX𝐬​(F​(Ti))​(y)\displaystyle=\sum\_{k=0}^{N}\int\_{((k-1)/N,(k+1)/N)}(1-|Ny-k|)\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫[0,1]∑k=0N𝟏{(k−1)/N<y<(k+1)/N}​(1−|N​y−k|)​d​GX𝐬​(F​(Ti))​(y)\displaystyle=\int\_{[0,1]}\sum\_{k=0}^{N}\mathbf{1}\_{\{(k-1)/N<y<(k+1)/N\}}(1-|Ny-k|)\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫[0,1]dGX𝐬​(F​(Ti))​(y)=1for 1≤i≤m,\displaystyle=\int\_{[0,1]}\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y)=1\quad\text{for $1\leq i\leq m$}, |  |

where the first equality follows from the definitions of {p^i​k(N)​(X𝐬)}1≤i≤m,0≤k≤N\{\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})\}\_{1\leq i\leq m,0\leq k\leq N} and the third equality holds due to ([51](https://arxiv.org/html/2602.08039v1#S12.E51 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")).
Similarly, for the second set of linear constraints, we note the identity

|  |  |  |
| --- | --- | --- |
|  | ∑k=0NkN​𝟏{(k−1)/N<y<(k+1)/N}​(1−|N​y−k|)=yfor y∈[0,1] and N∈ℕ+.\sum\_{k=0}^{N}\frac{k}{N}\mathbf{1}\_{\{(k-1)/N<y<(k+1)/N\}}(1-|Ny-k|)=y\quad\text{for $y\in[0,1]$ and $N\in\mathbb{N}^{+}$}. |  |

Then it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=0Nk​p^i​k(N)​(X)\displaystyle\sum\_{k=0}^{N}k\hat{p}\_{ik}^{(N)}(X) | =∑k=0Nk​∫((k−1)/N,(k+1)/N)(1−|N​y−k|)​dGX𝐬​(F​(Ti))​(y)\displaystyle=\sum\_{k=0}^{N}k\int\_{((k-1)/N,(k+1)/N)}(1-|Ny-k|)\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =N​∫[0,1]∑k=0NkN​𝟏{(k−1)/N<y<(k+1)/N}​(1−|N​y−k|)​d​GX𝐬​(F​(Ti))​(y)\displaystyle=N\int\_{[0,1]}\sum\_{k=0}^{N}\frac{k}{N}\mathbf{1}\_{\{(k-1)/N<y<(k+1)/N\}}(1-|Ny-k|)\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =N​∫[0,1]y​dGX𝐬​(F​(Ti))​(y)=N​𝔼​[X𝐬​(F​(Ti))]=N​F​(Ti)for ​1≤i≤m.\displaystyle=N\int\_{[0,1]}y\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y)=N\mathbb{E}[X\_{\mathbf{s}}(F(T\_{i}))]=NF(T\_{i})\quad\text{for }1\leq i\leq m. |  |

To verify the third set of linear constraints, we define

|  |  |  |
| --- | --- | --- |
|  | fk(N)​(y):=(N​y+1−k)​𝟏{(k−1)/N<y<k/N}+𝟏{k/N≤y}for 0≤k≤N and N∈ℕ+.f\_{k}^{(N)}(y):=(Ny+1-k)\mathbf{1}\_{\{(k-1)/N<y<k/N\}}+\mathbf{1}\_{\{k/N\leq y\}}\quad\text{for $0\leq k\leq N$ and $N\in\mathbb{N}^{+}$}. |  |

Using this definition, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j≥kp^i​j(N)​(X)\displaystyle\sum\_{j\geq k}\hat{p}\_{ij}^{(N)}(X) | =∑j≥k∫((j−1)/N,(j+1)/N)(1−|N​y−j|)​dGX𝐬​(F​(Ti))​(y)\displaystyle=\sum\_{j\geq k}\int\_{((j-1)/N,(j+1)/N)}(1-|Ny-j|)\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫((k−1)/N,k/N)(N​y+1−k)​dGX𝐬​(F​(Ti))​(y)+∫[k/N,1]dGX𝐬​(F​(Ti))​(y)\displaystyle=\int\_{((k-1)/N,k/N)}(Ny+1-k)\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y)+\int\_{[k/N,1]}\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[fk(N)​(X𝐬​(F​(Ti)))]for 0≤k≤N and 1≤i≤m.\displaystyle=\mathbb{E}[f\_{k}^{(N)}(X\_{\mathbf{s}}(F(T\_{i})))]\quad\text{for $0\leq k\leq N$ and $1\leq i\leq m$}. |  |

Since fk(N)​(y)f\_{k}^{(N)}(y) is a non-decreasing function of yy and X𝐬​(F​(Ti))≤X𝐬​(F​(Ti+1))X\_{\mathbf{s}}(F(T\_{i}))\leq X\_{\mathbf{s}}(F(T\_{i+1})) a.s., it follows that

|  |  |  |
| --- | --- | --- |
|  | ∑j≥kp^i+1,j(N)​(X𝐬)−∑j≥kp^i​j(N)​(X𝐬)=𝔼​[fk(N)​(X𝐬​(F​(Ti+1)))]−𝔼​[fk(N)​(X𝐬​(F​(Ti)))]≥0\sum\_{j\geq k}\hat{p}\_{i+1,j}^{(N)}(X\_{\mathbf{s}})-\sum\_{j\geq k}\hat{p}\_{ij}^{(N)}(X\_{\mathbf{s}})=\mathbb{E}[f\_{k}^{(N)}(X\_{\mathbf{s}}(F(T\_{i+1})))]-\mathbb{E}[f\_{k}^{(N)}(X\_{\mathbf{s}}(F(T\_{i})))]\geq 0 |  |

for 0≤k≤N0\leq k\leq N and 1≤i≤m−11\leq i\leq m-1.
Finally, the fourth set of linear constraints (i.e., the non-negativity constraints) are satisfied trivially since all integrands are non-negative.
We have verified all the four sets of linear constraints in ([47](https://arxiv.org/html/2602.08039v1#S12.E47 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")).
Thus, we obtain that P^(N)​(X𝐬)∈𝒫(N)\hat{P}^{(N)}(X\_{\mathbf{s}})\in\mathcal{P}^{(N)}.

Step 2. Constructing gamma distortions X𝐬(N)X\_{\mathbf{s}}^{(N)} for N∈ℕ+N\in\mathbb{N}^{+} and showing the convergence in distribution.
Since P^(N)​(X𝐬)∈𝒫(N)\hat{P}^{(N)}(X\_{\mathbf{s}})\in\mathcal{P}^{(N)} for N∈ℕ+N\in\mathbb{N}^{+}, Proposition [4.4](https://arxiv.org/html/2602.08039v1#S4.ThmProposition4 "Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") ensures the existence of a discrete gamma distortion X𝐬(N)X\_{\mathbf{s}}^{(N)} whose generator ϕ𝐬(N)\phi\_{\mathbf{s}}^{(N)} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(ϕ𝐬(N)​(F​(Ti))=k)=p^i​k(N)​(X𝐬)for 1≤i≤m and 0≤k≤N.\mathbb{P}(\phi\_{\mathbf{s}}^{(N)}(F(T\_{i}))=k)=\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})\quad\text{for $1\leq i\leq m$ and $0\leq k\leq N$}. |  | (52) |

We shall show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | X𝐬(N)​(F​(Ti))→𝑑X𝐬​(F​(Ti))as N→+∞ for 1≤i≤m.X\_{\mathbf{s}}^{(N)}(F(T\_{i}))\xrightarrow{d}X\_{\mathbf{s}}(F(T\_{i}))\quad\text{as $N\to+\infty$ for $1\leq i\leq m$}. |  | (53) |

To this end, we fix 1≤i≤m1\leq i\leq m, and let y0∈[0,1]y\_{0}\in[0,1] be an arbitrary continuity point of the distribution function GX𝐬​(F​(Ti))G\_{X\_{\mathbf{s}}(F(T\_{i}))}. We need to prove that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN→+∞GX𝐬(N)​(F​(Ti))​(y0)=GX𝐬​(F​(Ti))​(y0).\lim\_{N\to+\infty}G\_{X\_{\mathbf{s}}^{(N)}(F(T\_{i}))}(y\_{0})=G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y\_{0}). |  | (54) |

Note that X𝐬(N)​(F​(Ti))X\_{\mathbf{s}}^{(N)}(F(T\_{i})) follows a Beta mixture distribution with mixing weight p^i​k(N)​(X𝐬)\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}}) on the Beta​(k,N−k)\mathrm{Beta}(k,N-k) component for each 0≤k≤N0\leq k\leq N, where Beta​(α,β)\mathrm{Beta}(\alpha,\beta) denotes a Beta distribution with parameters α>0\alpha>0 and β>0\beta>0.
Then the cumulative distribution function (CDF) of X𝐬(N)​(F​(Ti))X\_{\mathbf{s}}^{(N)}(F(T\_{i})) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | GX𝐬(N)​(F​(Ti))​(y0)=∑k=0Np^i​k(N)​(X𝐬)​FB​(y0;k,N−k),G\_{X\_{\mathbf{s}}^{(N)}(F(T\_{i}))}(y\_{0})=\sum\_{k=0}^{N}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})F^{B}(y\_{0};k,N-k), |  | (55) |

where FB​(⋅;α,β)F^{B}(\cdot;\alpha,\beta) denotes the CDF of the Beta​(α,β)\mathrm{Beta}(\alpha,\beta) distribution for α>0\alpha>0 and β>0\beta>0.
For the degenerate cases, FB​(y;0,β):=𝟏{y≥0}F^{B}(y;0,\beta):=\mathbf{1}\_{\{y\geq 0\}} and FB​(y;α,0):=𝟏{y≥1}F^{B}(y;\alpha,0):=\mathbf{1}\_{\{y\geq 1\}} represent the degenerate distributions on 0 and 11, respectively.
Since y0y\_{0} is a continuity point, for any ϵ>0\epsilon>0, there exists δ>0\delta>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |GX𝐬​(F​(Ti))​(y)−GX𝐬​(F​(Ti))​(y0)|<ϵ​ for all |y−y0|≤δ.|G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y)-G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y\_{0})|<\epsilon\text{ for all $|y-y\_{0}|\leq\delta$}. |  | (56) |

To analyse the limit of the right hand side of ([55](https://arxiv.org/html/2602.08039v1#S12.E55 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) as NN goes to +∞+\infty, we shall first establish upper and lower bounds for FB​(x;α,β)F^{B}(x;\alpha,\beta).
Let Wα,β∼Beta​(α,β)W\_{\alpha,\beta}\sim\mathrm{Beta}(\alpha,\beta).
The mean and variance of Wα,βW\_{\alpha,\beta} are given by αα+β\frac{\alpha}{\alpha+\beta} and α​β(α+β)2​(α+β+1)\frac{\alpha\beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}, respectively.
For x<αα+βx<\frac{\alpha}{\alpha+\beta}, applying Chebyshev’s inequality yields an upper bound for FB​(x;α,β)F^{B}(x;\alpha,\beta).

|  |  |  |  |
| --- | --- | --- | --- |
|  | FB​(x;α,β)=\displaystyle F^{B}(x;\alpha,\beta)= | ℙ​(Wα,β≤x)=ℙ​(Wα,β−αα+β≤x−αα+β)\displaystyle\ \mathbb{P}(W\_{\alpha,\beta}\leq x)=\mathbb{P}\left(W\_{\alpha,\beta}-\frac{\alpha}{\alpha+\beta}\leq x-\frac{\alpha}{\alpha+\beta}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | Var⁡(Wα,β)(x−αα+β)2=α​β(x−αα+β)2​(α+β)2​(α+β+1)\displaystyle\ \frac{\operatorname{Var}(W\_{\alpha,\beta})}{\left(x-\frac{\alpha}{\alpha+\beta}\right)^{2}}=\frac{\alpha\beta}{\left(x-\frac{\alpha}{\alpha+\beta}\right)^{2}(\alpha+\beta)^{2}(\alpha+\beta+1)} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 14​(x−αα+β)2​(α+β+1).\displaystyle\ \frac{1}{4\left(x-\frac{\alpha}{\alpha+\beta}\right)^{2}(\alpha+\beta+1)}. |  | (57) |

Similarly, for x>αα+βx>\frac{\alpha}{\alpha+\beta}, Chebyshev’s inequality implies a lower bound for FB​(x;α,β)F^{B}(x;\alpha,\beta).

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−FB​(x;α,β)\displaystyle 1-F^{B}(x;\alpha,\beta) | =ℙ​(Wα,β>x)=ℙ​(Wα,β−αα+β>x−αα+β)\displaystyle=\mathbb{P}(W\_{\alpha,\beta}>x)=\mathbb{P}\left(W\_{\alpha,\beta}-\frac{\alpha}{\alpha+\beta}>x-\frac{\alpha}{\alpha+\beta}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Var⁡(Wα,β)(x−αα+β)2=α​β(x−αα+β)2​(α+β)2​(α+β+1)\displaystyle\leq\frac{\operatorname{Var}(W\_{\alpha,\beta})}{\left(x-\frac{\alpha}{\alpha+\beta}\right)^{2}}=\frac{\alpha\beta}{\left(x-\frac{\alpha}{\alpha+\beta}\right)^{2}(\alpha+\beta)^{2}(\alpha+\beta+1)} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤14​(x−αα+β)2​(α+β+1).\displaystyle\leq\frac{1}{4\left(x-\frac{\alpha}{\alpha+\beta}\right)^{2}(\alpha+\beta+1)}. |  | (58) |

Note that ([12.1](https://arxiv.org/html/2602.08039v1#S12.Ex61 "12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) and ([12.1](https://arxiv.org/html/2602.08039v1#S12.Ex63 "12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) also hold for the degenerate cases when either α=0\alpha=0 or β=0\beta=0.

Now, we are ready to establish a lower bound for the right hand side of ([55](https://arxiv.org/html/2602.08039v1#S12.E55 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")).
Define K0=⌊N​(y0−δ/2)⌋K\_{0}=\lfloor N(y\_{0}-\delta/2)\rfloor.
Truncating the summation in ([55](https://arxiv.org/html/2602.08039v1#S12.E55 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) at K0K\_{0}
, we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | GX𝐬(N)​(F​(Ti))​(y0)\displaystyle G\_{X\_{\mathbf{s}}^{(N)}(F(T\_{i}))}(y\_{0}) | ≥∑k=0K0p^i​k(N)​(X𝐬)​FB​(y0;k,N−k)≥∑k=0K0p^i​k(N)​(X𝐬)​(1−14​(N+1)​(y0−k/N)2)\displaystyle\geq\sum\_{k=0}^{K\_{0}}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})F^{B}(y\_{0};k,N-k)\geq\sum\_{k=0}^{K\_{0}}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})\left(1-\frac{1}{4(N+1)(y\_{0}-k/N)^{2}}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥(1−1(N+1)​δ2)​∑k=0K0p^i​k(N)​(X𝐬),\displaystyle\geq\left(1-\frac{1}{(N+1)\delta^{2}}\right)\sum\_{k=0}^{K\_{0}}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}}), |  | (59) |

where the second inequality follows from ([12.1](https://arxiv.org/html/2602.08039v1#S12.Ex63 "12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) and the last inequality follows from the fact that y0−k/N≥δ/2y\_{0}-k/N\geq\delta/2 for k≤K0k\leq K\_{0}.

Using the inequality

|  |  |  |
| --- | --- | --- |
|  | ∑k=0K0𝟏{(k−1)/N<y<(k+1)/N}​(1−|N​y−k|)≥𝟏{0≤y≤K0/N}for y∈[0,1] and N∈ℕ+\sum\_{k=0}^{K\_{0}}\mathbf{1}\_{\{(k-1)/N<y<(k+1)/N\}}(1-|Ny-k|)\geq\mathbf{1}\_{\{0\leq y\leq K\_{0}/N\}}\quad\text{for $y\in[0,1]$ and $N\in\mathbb{N}^{+}$} |  |

and exchanging the order of integration and summation, we yield the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=0K0p^i​k(N)​(X𝐬)=\displaystyle\sum\_{k=0}^{K\_{0}}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})= | ∑k=0K0∫(k−1N,k+1N)(1−|N​y−k|)​dGX𝐬​(F​(Ti))​(y)\displaystyle\sum\_{k=0}^{K\_{0}}\int\_{(\frac{k-1}{N},\frac{k+1}{N})}(1-|Ny-k|)\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫[0,1]∑k=0K0𝟏{(k−1)/N<y<(k+1)/N}​(1−|N​y−k|)​d​GX𝐬​(F​(Ti))​(y)\displaystyle\int\_{[0,1]}\sum\_{k=0}^{K\_{0}}\mathbf{1}\_{\{(k-1)/N<y<(k+1)/N\}}(1-|Ny-k|)\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≥\displaystyle\geq | ∫[0,K0/N]dGX𝐬​(F​(Ti))​(y)=GX𝐬​(F​(Ti))​(K0N).\displaystyle\int\_{[0,K\_{0}/N]}\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y)=G\_{X\_{\mathbf{s}}(F(T\_{i}))}\left(\frac{K\_{0}}{N}\right). |  | (60) |

For N>max⁡{2/δ,1/δ2}N>\max\{2/\delta,1/\delta^{2}\}, it holds that 1−1(N+1)​δ2>01-\frac{1}{(N+1)\delta^{2}}>0, and the argument of the CDF in the right hand side of ([12.1](https://arxiv.org/html/2602.08039v1#S12.Ex67 "12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | K0N>N​(y0−δ/2)−1N=y0−δ/2−1/N>y0−δ.\frac{K\_{0}}{N}>\frac{N(y\_{0}-\delta/2)-1}{N}=y\_{0}-\delta/2-1/N>y\_{0}-\delta. |  | (61) |

Since GX𝐬​(F​(Ti))G\_{X\_{\mathbf{s}}(F(T\_{i}))} is non-decreasing, using ([56](https://arxiv.org/html/2602.08039v1#S12.E56 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) and ([61](https://arxiv.org/html/2602.08039v1#S12.E61 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | GX𝐬​(F​(Ti))​(K0N)≥GX𝐬​(F​(Ti))​(y0−δ)≥GX𝐬​(F​(Ti))​(y0)−ϵ.G\_{X\_{\mathbf{s}}(F(T\_{i}))}\left(\frac{K\_{0}}{N}\right)\geq G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y\_{0}-\delta)\geq G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y\_{0})-\epsilon. |  | (62) |

Combining the results in ([12.1](https://arxiv.org/html/2602.08039v1#S12.Ex65 "12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")), ([12.1](https://arxiv.org/html/2602.08039v1#S12.Ex67 "12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) and ([62](https://arxiv.org/html/2602.08039v1#S12.E62 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")), we find the following lower bound for GX𝐬(N)​(F​(Ti))​(y0)G\_{X\_{\mathbf{s}}^{(N)}(F(T\_{i}))}(y\_{0}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | GX(N)​(F​(Ti))​(y0)\displaystyle G\_{X^{(N)}(F(T\_{i}))}(y\_{0}) | ≥(1−1(N+1)​δ2)​(GX𝐬​(F​(Ti))​(y0)−ϵ).\displaystyle\geq\left(1-\frac{1}{(N+1)\delta^{2}}\right)(G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y\_{0})-\epsilon). |  |

By taking the limit inferior as NN goes to +∞+\infty, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infN→+∞GX𝐬(N)​(F​(Ti))​(y0)≥GX𝐬​(F​(Ti))​(y0)−ϵ.\liminf\_{N\to+\infty}G\_{X\_{\mathbf{s}}^{(N)}(F(T\_{i}))}(y\_{0})\geq G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y\_{0})-\epsilon. |  | (63) |

Next, we establish an upper bound for the right hand side of ([55](https://arxiv.org/html/2602.08039v1#S12.E55 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")).
To this end, we define K1=⌈N​(y0+δ/2)⌉K\_{1}=\lceil N(y\_{0}+\delta/2)\rceil, and split the summation in ([55](https://arxiv.org/html/2602.08039v1#S12.E55 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) into two parts (k≤K1−1k\leq K\_{1}-1 and k≥K1k\geq K\_{1}) and use the trival upper bound FB​(y0;k,N−k)≤1F^{B}(y\_{0};k,N-k)\leq 1 for the first part to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | GX(N)​(F​(Ti))​(y0)\displaystyle G\_{X^{(N)}(F(T\_{i}))}(y\_{0}) | =∑k=0Np^i​k(N)​(X𝐬)​FB​(y0;k,N−k)\displaystyle=\sum\_{k=0}^{N}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})F^{B}(y\_{0};k,N-k) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤∑k=0K1−1p^i​k(N)​(X𝐬)+∑k=K1Np^i​k(N)​(X𝐬)​FB​(y0;k,N−k).\displaystyle\leq\sum\_{k=0}^{K\_{1}-1}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})+\sum\_{k=K\_{1}}^{N}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})F^{B}(y\_{0};k,N-k). |  | (64) |

Using the inequality

|  |  |  |
| --- | --- | --- |
|  | ∑k=0K1−1𝟏{(k−1)/N<y<(k+1)/N}​(1−|N​y−k|)≤𝟏{0≤y≤K1/N}for y∈[0,1] and N∈ℕ+,\sum\_{k=0}^{K\_{1}-1}\mathbf{1}\_{\{(k-1)/N<y<(k+1)/N\}}(1-|Ny-k|)\leq\mathbf{1}\_{\{0\leq y\leq K\_{1}/N\}}\quad\text{for $y\in[0,1]$ and $N\in\mathbb{N}^{+}$}, |  |

we find that the first sum in ([64](https://arxiv.org/html/2602.08039v1#S12.E64 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) is bounded by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=0K1−1p^i​k(N)​(X𝐬)=\displaystyle\sum\_{k=0}^{K\_{1}-1}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})= | ∑k=0K1−1∫((k−1)/N,(k+1)/N)(1−|N​y−k|)​dGX𝐬​(F​(Ti))​(y)\displaystyle\sum\_{k=0}^{K\_{1}-1}\int\_{((k-1)/N,(k+1)/N)}(1-|Ny-k|)\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫[0,1]∑k=0K1−1𝟏{(k−1)/N<y<(k+1)/N}​(1−|N​y−k|)​d​GX𝐬​(F​(Ti))​(y)\displaystyle\int\_{[0,1]}\sum\_{k=0}^{K\_{1}-1}\mathbf{1}\_{\{(k-1)/N<y<(k+1)/N\}}(1-|Ny-k|)\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ∫[0,K1/N]dGX𝐬​(F​(Ti))​(y)=GX𝐬​(F​(Ti))​(K1N).\displaystyle\int\_{[0,K\_{1}/N]}\mathrm{d}G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y)=G\_{X\_{\mathbf{s}}(F(T\_{i}))}\left(\frac{K\_{1}}{N}\right). |  | (65) |

For N>2/δN>2/\delta, the argument of the CDF on the right hand side of ([12.1](https://arxiv.org/html/2602.08039v1#S12.Ex72 "12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | K1N<N​(y0+δ/2)+1N=y0+δ/2+1/N<y0+δ.\frac{K\_{1}}{N}<\frac{N(y\_{0}+\delta/2)+1}{N}=y\_{0}+\delta/2+1/N<y\_{0}+\delta. |  | (66) |

Consequently, we can bound the first sum in ([64](https://arxiv.org/html/2602.08039v1#S12.E64 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=0K1−1p^i​k(N)​(X𝐬)≤GX𝐬​(F​(Ti))​(K1N)≤GX𝐬​(F​(Ti))​(y0+δ)≤GX𝐬​(F​(Ti))​(y0)+ϵ,\sum\_{k=0}^{K\_{1}-1}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})\leq G\_{X\_{\mathbf{s}}(F(T\_{i}))}\left(\frac{K\_{1}}{N}\right)\leq G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y\_{0}+\delta)\leq G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y\_{0})+\epsilon, |  | (67) |

where the first inequality follows from ([12.1](https://arxiv.org/html/2602.08039v1#S12.Ex72 "12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")), the second inequality follows from ([66](https://arxiv.org/html/2602.08039v1#S12.E66 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")), and the last inequality follows from ([56](https://arxiv.org/html/2602.08039v1#S12.E56 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")).

For the second sum in ([64](https://arxiv.org/html/2602.08039v1#S12.E64 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")), we use the upper bound established in ([12.1](https://arxiv.org/html/2602.08039v1#S12.Ex61 "12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) to obtain

|  |  |  |
| --- | --- | --- |
|  | ∑k=K1Np^i​k(N)​(X𝐬)​FB​(y0;k,N−k)≤∑k=K1Np^i​k(N)​(X𝐬)​14​(N+1)​(k/N−y0)2.\sum\_{k=K\_{1}}^{N}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})F^{B}(y\_{0};k,N-k)\leq\sum\_{k=K\_{1}}^{N}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})\frac{1}{4(N+1)(k/N-y\_{0})^{2}}. |  |

Noticing that the condition k≥K1k\geq K\_{1} implies k/N−y0≥δ/2k/N-y\_{0}\geq\delta/2 and that ∑k=K1Np^i​k(N)​(X𝐬)≤1\sum\_{k=K\_{1}}^{N}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})\leq 1, we can bound the second sum in ([64](https://arxiv.org/html/2602.08039v1#S12.E64 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=K1Np^i​k(N)​(X𝐬)​FB​(y0;k,N−k)≤1(N+1)​δ2.\sum\_{k=K\_{1}}^{N}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})F^{B}(y\_{0};k,N-k)\leq\frac{1}{(N+1)\delta^{2}}. |  | (68) |

Combining the bounds in ([67](https://arxiv.org/html/2602.08039v1#S12.E67 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) and ([68](https://arxiv.org/html/2602.08039v1#S12.E68 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")), we can obtain the following upper bound for GX𝐬(N)​(F​(Ti))​(y0)G\_{X\_{\mathbf{s}}^{(N)}(F(T\_{i}))}(y\_{0}):

|  |  |  |
| --- | --- | --- |
|  | GX𝐬(N)​(F​(Ti))​(y0)≤GX𝐬​(F​(Ti))​(y0)+ϵ+1(N+1)​δ2.\displaystyle G\_{X\_{\mathbf{s}}^{(N)}(F(T\_{i}))}(y\_{0})\leq G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y\_{0})+\epsilon+\frac{1}{(N+1)\delta^{2}}. |  |

By taking the limit superior as NN goes to +∞+\infty, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supN→+∞GX𝐬(N)​(F​(Ti))​(y0)≤GX𝐬​(F​(Ti))​(y0)+ϵ.\limsup\_{N\to+\infty}G\_{X\_{\mathbf{s}}^{(N)}(F(T\_{i}))}(y\_{0})\leq G\_{X\_{\mathbf{s}}(F(T\_{i}))}(y\_{0})+\epsilon. |  | (69) |

Since ϵ>0\epsilon>0 is arbitrary, ([63](https://arxiv.org/html/2602.08039v1#S12.E63 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) and ([69](https://arxiv.org/html/2602.08039v1#S12.E69 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) imply the convergence in ([54](https://arxiv.org/html/2602.08039v1#S12.E54 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")).
This completes the proof of the convergence in distribution in ([53](https://arxiv.org/html/2602.08039v1#S12.E53 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")).

Step 3. Proving the convergence in ([50](https://arxiv.org/html/2602.08039v1#S12.E50 "In Lemma 12.1 ‣ 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")).
Recall that conditional on ϕ𝐬(N)​(F​(Ti))=k\phi\_{\mathbf{s}}^{(N)}(F(T\_{i}))=k, X𝐬(N)​(F​(Ti))X\_{\mathbf{s}}^{(N)}(F(T\_{i})) follows a Beta​(k,N−k)\mathrm{Beta}(k,N-k) distribution for 0≤k≤N0\leq k\leq N.
By the property of the Beta distribution and the definition of hj​k(N)h\_{jk}^{(N)}, we have

|  |  |  |
| --- | --- | --- |
|  | (nj)​𝔼​[(X𝐬(N)​(F​(Ti)))j​(1−X𝐬(N)​(F​(Ti)))n−j|ϕ𝐬(N)​(F​(Ti))=k]=hj​k(N)\binom{n}{j}\mathbb{E}\left[(X\_{\mathbf{s}}^{(N)}(F(T\_{i})))^{j}(1-X\_{\mathbf{s}}^{(N)}(F(T\_{i})))^{n-j}\big|\phi\_{\mathbf{s}}^{(N)}(F(T\_{i}))=k\right]=h\_{jk}^{(N)} |  |

for 0≤j≤n0\leq j\leq n and 0≤k≤N0\leq k\leq N.
Conditional on ϕ𝐬(N)​(F​(Ti))\phi\_{\mathbf{s}}^{(N)}(F(T\_{i})), we can derive from the law of total expectation that

|  |  |  |
| --- | --- | --- |
|  | (nj)​𝔼​[X𝐬(N)​(F​(Ti))j​(1−X𝐬(N)​(F​(Ti)))n−j]=∑k=0Nhj​k(N)​p^i​k(N)​(X𝐬)for 0≤j≤n.\binom{n}{j}\mathbb{E}\left[X\_{\mathbf{s}}^{(N)}(F(T\_{i}))^{j}(1-X\_{\mathbf{s}}^{(N)}(F(T\_{i})))^{n-j}\right]=\sum\_{k=0}^{N}h\_{jk}^{(N)}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{s}})\quad\text{for $0\leq j\leq n$}. |  |

Substituting this identity into ([49](https://arxiv.org/html/2602.08039v1#S12.E49 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")), we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | v[al,bl]​(P^(N)​(X𝐬);𝐬)=\displaystyle v^{[a\_{l},b\_{l}]}(\hat{P}^{(N)}(X\_{\mathbf{s}});\mathbf{s})= | ∑i=1m∑j=0nλi[al,bl]​(𝐬)​βj[al,bl]​(nj)​𝔼​[X𝐬(N)​(F​(Ti))j​(1−X𝐬(N)​(F​(Ti)))n−j]\displaystyle\ \sum\_{i=1}^{m}\sum\_{j=0}^{n}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})\beta\_{j}^{[a\_{l},b\_{l}]}\binom{n}{j}\mathbb{E}\left[X^{(N)}\_{\mathbf{s}}(F(T\_{i}))^{j}(1-X^{(N)}\_{\mathbf{s}}(F(T\_{i})))^{n-j}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −γ[al,bl]​(𝐬)for ​1≤l≤M.\displaystyle\ -\gamma^{[a\_{l},b\_{l}]}(\mathbf{s})\quad\text{for }1\leq l\leq M. |  | (70) |

We have shown in Step 2 that X𝐬(N)​(F​(Ti))X^{(N)}\_{\mathbf{s}}(F(T\_{i})) converges in distribution to X𝐬​(F​(Ti))X\_{\mathbf{s}}(F(T\_{i})) as NN goes to +∞+\infty for 1≤i≤m1\leq i\leq m.
Since the function y↦yj​(1−y)n−jy\mapsto y^{j}(1-y)^{n-j} is continuous and bounded on [0,1][0,1], the convergence in distribution implies the convergence of expectations.

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN→+∞𝔼​[X𝐬(N)​(F​(Ti))j​(1−X𝐬(N)​(F​(Ti)))n−j]=𝔼​[X𝐬​(F​(Ti))j​(1−X𝐬​(F​(Ti)))n−j].\lim\_{N\to+\infty}\mathbb{E}\left[X^{(N)}\_{\mathbf{s}}(F(T\_{i}))^{j}(1-X^{(N)}\_{\mathbf{s}}(F(T\_{i})))^{n-j}\right]=\mathbb{E}\left[X\_{\mathbf{s}}(F(T\_{i}))^{j}(1-X\_{\mathbf{s}}(F(T\_{i})))^{n-j}\right]. |  | (71) |

Letting NN go to +∞+\infty in ([70](https://arxiv.org/html/2602.08039v1#S12.E70 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) and using ([71](https://arxiv.org/html/2602.08039v1#S12.E71 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limN→+∞v[al,bl]​(P^(N)​(X𝐬);𝐬)\displaystyle\lim\_{N\to+\infty}v^{[a\_{l},b\_{l}]}(\hat{P}^{(N)}(X\_{\mathbf{s}});\mathbf{s}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∑i=1m∑j=0nλi[al,bl]​(𝐬)​βj[al,bl]​(nj)​𝔼​[X𝐬​(F​(Ti))j​(1−X𝐬​(F​(Ti)))n−j]−γ[al,bl]​(𝐬)\displaystyle\ \sum\_{i=1}^{m}\sum\_{j=0}^{n}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})\beta\_{j}^{[a\_{l},b\_{l}]}\binom{n}{j}\mathbb{E}\left[X\_{\mathbf{s}}(F(T\_{i}))^{j}(1-X\_{\mathbf{s}}(F(T\_{i})))^{n-j}\right]-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}) |  | (72) |

for 1≤l≤M1\leq l\leq M.
Note that the right hand side of ([12.1](https://arxiv.org/html/2602.08039v1#S12.Ex79 "12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) is exactly v[al,bl]​(CX𝐬;𝐬)v^{[a\_{l},b\_{l}]}(C^{X\_{\mathbf{s}}};\mathbf{s}) given in ([16](https://arxiv.org/html/2602.08039v1#S4.E16 "In 4.2 Valuation of CDO Tranches under Conditionally I.I.D. Models ‣ 4 Strong Compatibility")).
Furthermore, since CX𝐬C^{X\_{\mathbf{s}}} achieves a perfect fit to the market prices 𝐬\mathbf{s}, we have v[al,bl]​(CX𝐬;𝐬)=0v^{[a\_{l},b\_{l}]}(C^{X\_{\mathbf{s}}};\mathbf{s})=0 for all l=1,…,Ml=1,\ldots,M.
Consequently, we have proved the convergence in ([50](https://arxiv.org/html/2602.08039v1#S12.E50 "In Lemma 12.1 ‣ 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")).
□\square

Define 𝒪I\mathcal{O}^{I} to be the open orthant in ℝM\mathbb{R}^{M} as follows:

|  |  |  |
| --- | --- | --- |
|  | 𝒪I:={𝐱=(x1,…,xM)∈ℝM:xl>0​ for ​l∈I,xl<0​ for ​l∉I}for ​I⊆{1,…,M}.\mathcal{O}^{I}:=\{\mathbf{x}=(x\_{1},\ldots,x\_{M})\in\mathbb{R}^{M}:x\_{l}>0\text{ for }l\in I,\,x\_{l}<0\text{ for }l\notin I\}\quad\text{for }I\subseteq\{1,\ldots,M\}. |  |

The following lemma characterizes a sufficient condition for a convex set to contain the origin.

###### Lemma 12.2

Let ℰ⊆ℝM\mathcal{E}\subseteq\mathbb{R}^{M} be a convex set.
If ℰ∩𝒪I≠∅\mathcal{E}\cap\mathcal{O}^{I}\neq\emptyset for all I⊆{1,…,M}I\subseteq\{1,\ldots,M\},
then 𝟎M∈ℰ\mathbf{0}\_{M}\in\mathcal{E}.

Proof.
We use proof by contradiction.
Suppose that 𝟎M∉ℰ\mathbf{0}\_{M}\notin\mathcal{E}.
By the hyperplane separation theorem, there exists a nonzero vector 𝐱=(x1,…,xM)∈ℝM\mathbf{x}=(x\_{1},\ldots,x\_{M})\in\mathbb{R}^{M} such that 𝐱⋅𝐳≥0\mathbf{x}\cdot\mathbf{z}\geq 0 for all 𝐳∈ℰ\mathbf{z}\in\mathcal{E}.
Define I𝐱:={l:xl<0}I\_{\mathbf{x}}:=\{l:x\_{l}<0\}.
By hypothesis, there exists a vector 𝐲=(y1,…,yM)∈ℰ∩𝒪I𝐱\mathbf{y}=(y\_{1},\ldots,y\_{M})\in\mathcal{E}\cap\mathcal{O}^{I\_{\mathbf{x}}}.
By the definition of 𝒪I𝐱\mathcal{O}^{I\_{\mathbf{x}}}, we have xl​yl≤0x\_{l}y\_{l}\leq 0 for all 1≤l≤M1\leq l\leq M.
Since 𝐱≠𝟎M\mathbf{x}\neq\mathbf{0}\_{M} and all components of 𝐲\mathbf{y} are nonzero, the dot product 𝐱⋅𝐲\mathbf{x}\cdot\mathbf{y} is strictly negative.
This contradicts the fact that 𝐱⋅𝐲≥0\mathbf{x}\cdot\mathbf{y}\geq 0.
Therefore, we conclude that 𝟎M∈ℰ\mathbf{0}\_{M}\in\mathcal{E}.
□\square

### 12.2 Proof of Proposition [4.3](https://arxiv.org/html/2602.08039v1#S4.ThmProposition3 "Proposition 4.3 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")

We are now ready to prove Proposition [4.3](https://arxiv.org/html/2602.08039v1#S4.ThmProposition3 "Proposition 4.3 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility").
Consider an arbitrary vector 𝐬∈𝒜∘\mathbf{s}\in\mathcal{A}^{\circ}. Define the set

|  |  |  |
| --- | --- | --- |
|  | ℰ(N)​(𝐬)={𝐯​(P^(N);𝐬):P^(N)∈𝒫(N)}for any N∈ℕ+.\mathcal{E}^{(N)}(\mathbf{s})=\{\mathbf{v}({\hat{P}^{(N)};\mathbf{s}}):\hat{P}^{(N)}\in\mathcal{P}^{(N)}\}\quad\text{for any $N\in\mathbb{N}^{+}$}. |  |

Note that the feasibility of ([21](https://arxiv.org/html/2602.08039v1#S4.E21 "In Theorem 4.1 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")) for N∈ℕ+N\in\mathbb{N}^{+} is equivalent to the condition that 𝟎M∈ℰ(N)​(𝐬)\mathbf{0}\_{M}\in\mathcal{E}^{(N)}(\mathbf{s}). Therefore, proving Proposition [4.3](https://arxiv.org/html/2602.08039v1#S4.ThmProposition3 "Proposition 4.3 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") is equivalent to showing that 𝟎M∈ℰ(N)​(𝐬)\mathbf{0}\_{M}\in\mathcal{E}^{(N)}(\mathbf{s}) for all sufficiently large NN.
According to Lemma [12.2](https://arxiv.org/html/2602.08039v1#S12.ThmLemma2 "Lemma 12.2 ‣ 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3"), it suffices to show that for any I⊆{1,…,M}I\subseteq\{1,\ldots,M\}, we have ℰ(N)​(𝐬)∩𝒪I≠∅\mathcal{E}^{(N)}(\mathbf{s})\cap\mathcal{O}^{I}\neq\emptyset for all sufficiently large NN.

Since 𝐬\mathbf{s} lies in the interior 𝒜∘\mathcal{A}^{\circ}, there exists an open ball centered at 𝐬\mathbf{s} and contained in 𝒜\mathcal{A}.
For sufficiently small δl>0\delta\_{l}>0 (for 1≤l≤M1\leq l\leq M), we define a perturbed price 𝐬~\mathbf{\tilde{s}} lying within this ball as follows:

|  |  |  |
| --- | --- | --- |
|  | s~[al,bl]=s[al,bl]​for​ 1≤l≤M;uf~[al,bl]=uf[al,bl]+δl​for ​l∈I;uf~[al,bl]=uf[al,bl]−δl​for ​l∉I.\tilde{s}^{[a\_{l},b\_{l}]}=s^{[a\_{l},b\_{l}]}\ \,\text{for}\,1\leq l\leq M;\quad\tilde{\textrm{uf}}^{[a\_{l},b\_{l}]}=\textrm{uf}^{[a\_{l},b\_{l}]}+\delta\_{l}\ \,\text{for }l\in I;\quad\tilde{\textrm{uf}}^{[a\_{l},b\_{l}]}=\textrm{uf}^{[a\_{l},b\_{l}]}-\delta\_{l}\ \,\text{for }l\notin I. |  |

Since λi[al,bl]\lambda\_{i}^{[a\_{l},b\_{l}]} depends only on the tranche spread, this definition ensures that

|  |  |  |  |
| --- | --- | --- | --- |
|  | λi[al,bl]​(𝐬~)=λi[al,bl]​(𝐬)for 1≤i≤m and 1≤l≤M.\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{\tilde{s}})=\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})\quad\text{for $1\leq i\leq m$ and $1\leq l\leq M$}. |  | (73) |

Recalling the definition of γ[al,bl]\gamma^{[a\_{l},b\_{l}]} in ([7](https://arxiv.org/html/2602.08039v1#S3.E7 "In Proposition 3.2 ‣ 3.2 Expressing the Expected NPVs 𝑣^[𝑎_𝑙,𝑏_𝑙]⁢(𝐶;𝐬) of Tranches in Terms of the DPM ‣ 3 Weak Compatibility")), we have

|  |  |  |
| --- | --- | --- |
|  | γ[al,bl]​(𝐬~)−γ[al,bl]​(𝐬)={δl​(bl−al)>0for ​l∈I,−δl​(bl−al)<0for ​l∉I.\gamma^{[a\_{l},b\_{l}]}(\mathbf{\tilde{s}})-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s})=\begin{cases}\delta\_{l}(b\_{l}-a\_{l})>0&\text{for }l\in I,\\ -\delta\_{l}(b\_{l}-a\_{l})<0&\text{for }l\notin I.\end{cases} |  |

Define ϵ=12​min1≤l≤M⁡{|γ[al,bl]​(𝐬~)−γ[al,bl]​(𝐬)|}>0\epsilon=\frac{1}{2}\min\_{1\leq l\leq M}\{|\gamma^{[a\_{l},b\_{l}]}(\mathbf{\tilde{s}})-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s})|\}>0.
Let X𝐬~X\_{\mathbf{\tilde{s}}} be a stochastic distortion whose transformed copula achieves a perfect fit to 𝐬~\mathbf{\tilde{s}}. Applying Lemma [12.1](https://arxiv.org/html/2602.08039v1#S12.ThmLemma1 "Lemma 12.1 ‣ 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3") to 𝐬~\mathbf{\tilde{s}} and X𝐬~X\_{\mathbf{\tilde{s}}} yields

|  |  |  |
| --- | --- | --- |
|  | ‖𝐯​(P^(N)​(X𝐬~);𝐬~)‖→0as N→+∞.\|\mathbf{v}(\hat{P}^{(N)}(X\_{\mathbf{\tilde{s}}});\mathbf{\tilde{s}})\|\to 0\quad\text{as $N\to+\infty$}. |  |

Thus, there exists N0∈ℕ+N\_{0}\in\mathbb{N}^{+} such that ‖𝐯​(P^(N)​(X𝐬~);𝐬~)‖<ϵ\|\mathbf{v}(\hat{P}^{(N)}(X\_{\mathbf{\tilde{s}}});\mathbf{\tilde{s}})\|<\epsilon for all N≥N0N\geq N\_{0}.

Next, we consider 𝐯​(P^(N)​(X𝐬~);𝐬)\mathbf{v}(\hat{P}^{(N)}(X\_{\mathbf{\tilde{s}}});\mathbf{s}) for N≥N0N\geq N\_{0}.
Recalling the definition of v[al,bl]v^{[a\_{l},b\_{l}]} in ([49](https://arxiv.org/html/2602.08039v1#S12.E49 "In 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3")) and the identity ([73](https://arxiv.org/html/2602.08039v1#S12.E73 "In 12.2 Proof of Proposition 4.3 ‣ 12 Proof of Proposition 4.3")), we can obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | v[al,bl]​(P^(N)​(X𝐬~);𝐬)\displaystyle v^{[a\_{l},b\_{l}]}(\hat{P}^{(N)}(X\_{\mathbf{\tilde{s}}});\mathbf{s}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑i=1m∑j=0n∑k=0Nhj​k(N)​λi[al,bl]​(𝐬)​βj[al,bl]​p^i​k(N)​(X𝐬~)−γ[al,bl]​(𝐬)\displaystyle\sum\_{i=1}^{m}\sum\_{j=0}^{n}\sum\_{k=0}^{N}h\_{jk}^{(N)}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{s})\beta\_{j}^{[a\_{l},b\_{l}]}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{\tilde{s}}})-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | [∑i=1m∑j=0n∑k=0Nhj​k(N)​λi[al,bl]​(𝐬~)​βj[al,bl]​p^i​k(N)​(X𝐬~)−γ[al,bl]​(𝐬~)]+γ[al,bl]​(𝐬~)−γ[al,bl]​(𝐬)\displaystyle\left[\sum\_{i=1}^{m}\sum\_{j=0}^{n}\sum\_{k=0}^{N}h\_{jk}^{(N)}\lambda\_{i}^{[a\_{l},b\_{l}]}(\mathbf{\tilde{s}})\beta\_{j}^{[a\_{l},b\_{l}]}\hat{p}\_{ik}^{(N)}(X\_{\mathbf{\tilde{s}}})-\gamma^{[a\_{l},b\_{l}]}(\mathbf{\tilde{s}})\right]+\gamma^{[a\_{l},b\_{l}]}(\mathbf{\tilde{s}})-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | v[al,bl]​(P^(N)​(X𝐬~);𝐬~)+γ[al,bl]​(𝐬~)−γ[al,bl]​(𝐬).\displaystyle v^{[a\_{l},b\_{l}]}(\hat{P}^{(N)}(X\_{\mathbf{\tilde{s}}});\mathbf{\tilde{s}})+\gamma^{[a\_{l},b\_{l}]}(\mathbf{\tilde{s}})-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s}). |  |

For any l∈Il\in I, we have γ[al,bl]​(𝐬~)−γ[al,bl]​(𝐬)≥2​ϵ\gamma^{[a\_{l},b\_{l}]}(\mathbf{\tilde{s}})-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s})\geq 2\epsilon, which ensures that

|  |  |  |
| --- | --- | --- |
|  | v[al,bl]​(P^(N)​(X𝐬~);𝐬)≥−ϵ+2​ϵ=ϵ>0.v^{[a\_{l},b\_{l}]}(\hat{P}^{(N)}(X\_{\mathbf{\tilde{s}}});\mathbf{s})\geq-\epsilon+2\epsilon=\epsilon>0. |  |

Similarly, for any l∉Il\notin I, we have γ[al,bl]​(𝐬~)−γ[al,bl]​(𝐬)≤−2​ϵ\gamma^{[a\_{l},b\_{l}]}(\mathbf{\tilde{s}})-\gamma^{[a\_{l},b\_{l}]}(\mathbf{s})\leq-2\epsilon, thereby yielding

|  |  |  |
| --- | --- | --- |
|  | v[al,bl]​(P^(N)​(X𝐬~);𝐬)≤ϵ−2​ϵ=−ϵ<0.v^{[a\_{l},b\_{l}]}(\hat{P}^{(N)}(X\_{\mathbf{\tilde{s}}});\mathbf{s})\leq\epsilon-2\epsilon=-\epsilon<0. |  |

Thus we have shown that 𝐯​(P^(N)​(X𝐬~);𝐬)∈𝒪I\mathbf{v}(\hat{P}^{(N)}(X\_{\mathbf{\tilde{s}}});\mathbf{s})\in\mathcal{O}^{I} for all N≥N0N\geq N\_{0}. In addition, for any N∈ℕ+N\in\mathbb{N}^{+}, we have 𝐯​(P^(N)​(X𝐬~);𝐬)∈ℰ(N)​(𝐬)\mathbf{v}(\hat{P}^{(N)}(X\_{\mathbf{\tilde{s}}});\mathbf{s})\in\mathcal{E}^{(N)}(\mathbf{s}) because P^(N)​(X𝐬~)∈𝒫(N)\hat{P}^{(N)}(X\_{\mathbf{\tilde{s}}})\in\mathcal{P}^{(N)}. Accordingly, we can obtain that 𝐯​(P^(N)​(X𝐬~);𝐬)∈ℰ(N)​(𝐬)∩𝒪I\mathbf{v}(\hat{P}^{(N)}(X\_{\mathbf{\tilde{s}}});\mathbf{s})\in\mathcal{E}^{(N)}(\mathbf{s})\cap\mathcal{O}^{I} for all N≥N0N\geq N\_{0}. Therefore, we conclude that ℰ(N)​(𝐬)∩𝒪I≠∅\mathcal{E}^{(N)}(\mathbf{s})\cap\mathcal{O}^{I}\neq\emptyset for all N≥N0N\geq N\_{0}.
This completes the whole proof of Proposition [4.3](https://arxiv.org/html/2602.08039v1#S4.ThmProposition3 "Proposition 4.3 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility"). □\Box

## 13 Proofs of Proposition [4.5](https://arxiv.org/html/2602.08039v1#S4.ThmProposition5 "Proposition 4.5 ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility") and Proposition [4.6](https://arxiv.org/html/2602.08039v1#S4.ThmProposition6 "Proposition 4.6 (A Sufficient and Necessary Condition for Strong Bid-Ask Compatibility) ‣ 4.6 Strong Bid-Ask Compatibility ‣ 4 Strong Compatibility")

Proof of Proposition [4.5](https://arxiv.org/html/2602.08039v1#S4.ThmProposition5 "Proposition 4.5 ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility").
We will focus only on the establishment of the convergence of the upper bound for the up-front payment, i.e.,

|  |  |  |
| --- | --- | --- |
|  | limN→+∞uf¯N[al+1,bl+1]=uf¯[al+1,bl+1].\lim\_{N\to+\infty}\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N}=\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}. |  |

The convergence of the other three bounds follows by analogous arguments.

For each N∈ℕ+N\in\mathbb{N}^{+}, let 𝒞D​G(N)\mathcal{C}\_{DG}^{(N)} denote the family of discrete gamma-distorted copulas with fixed parameter NN, and let 𝒜Nl+1\mathcal{A}\_{N}^{l+1} denote the set of price vectors of the first (l+1)(l+1) tranches that are compatible with respect to 𝒞D​G(N)\mathcal{C}\_{DG}^{(N)}.
Since 𝒞D​G(N)⊆𝒞1\mathcal{C}\_{DG}^{(N)}\subseteq\mathcal{C}\_{1}, it follows that 𝒜Nl+1⊆𝒜l+1\mathcal{A}\_{N}^{l+1}\subseteq\mathcal{A}^{l+1} for all N∈ℕ+N\in\mathbb{N}^{+} (recall that 𝒜l+1\mathcal{A}^{l+1} denotes the set of strongly compatible market prices for the first l+1l+1 tranches).

Moreover, by Proposition [4.3](https://arxiv.org/html/2602.08039v1#S4.ThmProposition3 "Proposition 4.3 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility"), every interior point of 𝒜l+1\mathcal{A}^{l+1} belongs to 𝒜Nl+1\mathcal{A}\_{N}^{l+1} for all sufficiently large NN.
Hence, we can deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒜l+1)∘⊆lim infN→+∞𝒜Nl+1⊆lim supN→+∞𝒜Nl+1⊆𝒜l+1.(\mathcal{A}^{l+1})^{\circ}\subseteq\liminf\_{N\to+\infty}\mathcal{A}\_{N}^{l+1}\subseteq\limsup\_{N\to+\infty}\mathcal{A}\_{N}^{l+1}\subseteq\mathcal{A}^{l+1}. |  | (74) |

For x∈ℝx\in\mathbb{R}, define the vector 𝐬​(x)\mathbf{s}(x) as

|  |  |  |
| --- | --- | --- |
|  | 𝐬​(x):=(s[a1,b1],uf[a1,b1],…,s[al,bl],uf[al,bl],s[al+1,bl+1],x).\mathbf{s}(x):=(s^{[a\_{1},b\_{1}]},\textrm{uf}^{[a\_{1},b\_{1}]},\ldots,s^{[a\_{l},b\_{l}]},\textrm{uf}^{[a\_{l},b\_{l}]},s^{[a\_{l+1},b\_{l+1}]},x). |  |

Furthermore, define

|  |  |  |
| --- | --- | --- |
|  | 𝒮N:={x∈ℝ:𝐬​(x)∈𝒜Nl+1}for any N∈ℕ+and𝒮:={x∈ℝ:𝐬​(x)∈𝒜l+1}.\mathcal{S}\_{N}:=\{x\in\mathbb{R}:\mathbf{s}(x)\in\mathcal{A}\_{N}^{l+1}\}\quad\text{for any $N\in\mathbb{N}^{+}$}\quad\text{and}\quad\mathcal{S}:=\{x\in\mathbb{R}:\mathbf{s}(x)\in\mathcal{A}^{l+1}\}. |  |

Using these notations, the upper bounds defined in ([25](https://arxiv.org/html/2602.08039v1#S4.E25 "In 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility")) and ([26](https://arxiv.org/html/2602.08039v1#S4.E26 "In 1st item ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility")) can be expressed as

|  |  |  |
| --- | --- | --- |
|  | uf¯N[al+1,bl+1]=sup𝒮Nfor any N∈ℕ+anduf¯[al+1,bl+1]=sup𝒮.\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N}=\sup\mathcal{S}\_{N}\quad\text{for any $N\in\mathbb{N}^{+}$}\quad\text{and}\quad\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}=\sup\mathcal{S}. |  |

Given that (s[a1,b1],uf[a1,b1],…,s[al,bl],uf[al,bl])∈(𝒜l)∘(s^{[a\_{1},b\_{1}]},\textrm{uf}^{[a\_{1},b\_{1}]},\ldots,s^{[a\_{l},b\_{l}]},\textrm{uf}^{[a\_{l},b\_{l}]})\in(\mathcal{A}^{l})^{\circ}, Proposition [4.3](https://arxiv.org/html/2602.08039v1#S4.ThmProposition3 "Proposition 4.3 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility") ensures that 𝒫Nl\mathcal{P}\_{N}^{l} is non-empty for all sufficiently large NN.
This guarantees that for all sufficiently large NN, 𝒮N\mathcal{S}\_{N} is non-empty, and thus uf¯N[al+1,bl+1]\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N} is well-defined.
Moreover, the inclusion 𝒮N⊆𝒮\mathcal{S}\_{N}\subseteq\mathcal{S} for any N∈ℕ+N\in\mathbb{N}^{+} implies that 𝒮\mathcal{S} is also non-empty, and thus uf¯[al+1,bl+1]\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]} is well-defined.

Taking one-dimensional sections in the inclusion chain ([74](https://arxiv.org/html/2602.08039v1#S13.E74 "In 13 Proofs of Proposition 4.5 and Proposition 4.6")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮∘⊆lim infN→+∞𝒮N⊆lim supN→+∞𝒮N⊆𝒮.\mathcal{S}^{\circ}\subseteq\liminf\_{N\to+\infty}\mathcal{S}\_{N}\subseteq\limsup\_{N\to+\infty}\mathcal{S}\_{N}\subseteq\mathcal{S}. |  | (75) |

For x1,x2∈𝒮x\_{1},x\_{2}\in\mathcal{S} and θ∈(0,1)\theta\in(0,1), the convex combination θ​𝐬​(x1)+(1−θ)​𝐬​(x2)\theta\mathbf{s}(x\_{1})+(1-\theta)\mathbf{s}(x\_{2}) belongs to 𝒜l+1\mathcal{A}^{l+1} since a perfect fit can be achieved by mixing the two conditionally i.i.d. copulas that achieve perfect fits with 𝐬​(x1)\mathbf{s}(x\_{1}) and 𝐬​(x2)\mathbf{s}(x\_{2}), respectively.
This implies that θ​x1+(1−θ)​x2∈𝒮\theta x\_{1}+(1-\theta)x\_{2}\in\mathcal{S}, implying that 𝒮\mathcal{S} is convex.
Thus, 𝒮\mathcal{S} must be an interval or a singleton.
In both cases, ([75](https://arxiv.org/html/2602.08039v1#S13.E75 "In 13 Proofs of Proposition 4.5 and Proposition 4.6")) implies that

|  |  |  |
| --- | --- | --- |
|  | limN→+∞uf¯N[al+1,bl+1]=uf¯[al+1,bl+1].\lim\_{N\to+\infty}\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}\_{N}=\overline{\textrm{uf}}^{[a\_{l+1},b\_{l+1}]}. |  |

This completes the proof.
□\square

Proof of Proposition [4.6](https://arxiv.org/html/2602.08039v1#S4.ThmProposition6 "Proposition 4.6 (A Sufficient and Necessary Condition for Strong Bid-Ask Compatibility) ‣ 4.6 Strong Bid-Ask Compatibility ‣ 4 Strong Compatibility").
We first prove the second implication ((𝐬b​i​d,𝐬a​s​k)∈𝒜b​i​d−a​s​k∘(\mathbf{s}\_{bid},\mathbf{s}\_{ask})\in\mathcal{A}\_{bid-ask}^{\circ} ⇒\Rightarrow LP feasibility). Suppose that there exists an N∈ℕ+N\in\mathbb{N}^{+} such that ([28](https://arxiv.org/html/2602.08039v1#S4.E28 "In Proposition 4.6 (A Sufficient and Necessary Condition for Strong Bid-Ask Compatibility) ‣ 4.6 Strong Bid-Ask Compatibility ‣ 4 Strong Compatibility")) has a feasible solution {p^i​k}1≤i≤m,0≤k≤N\{\hat{p}\_{ik}\}\_{1\leq i\leq m,0\leq k\leq N}.
Note that the last four sets of linear constraints in ([28](https://arxiv.org/html/2602.08039v1#S4.E28 "In Proposition 4.6 (A Sufficient and Necessary Condition for Strong Bid-Ask Compatibility) ‣ 4.6 Strong Bid-Ask Compatibility ‣ 4 Strong Compatibility")) are exactly the constraints of ([22](https://arxiv.org/html/2602.08039v1#S4.E22 "In Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility")).
By applying Proposition [4.4](https://arxiv.org/html/2602.08039v1#S4.ThmProposition4 "Proposition 4.4 ‣ 4.4 A Sufficient and Necessary Condition for Strong Compatibility ‣ 4 Strong Compatibility"), we can construct a discrete gamma-distorted copula C∈𝒞1C\in\mathcal{C}\_{1} from {p^i​k}1≤i≤m,0≤k≤N\{\hat{p}\_{ik}\}\_{1\leq i\leq m,0\leq k\leq N}.
The first two sets of linear constraints in ([28](https://arxiv.org/html/2602.08039v1#S4.E28 "In Proposition 4.6 (A Sufficient and Necessary Condition for Strong Bid-Ask Compatibility) ‣ 4.6 Strong Bid-Ask Compatibility ‣ 4 Strong Compatibility")) ensure that the expected NPVs satisfy v[al,bl]​(C;𝐬b​i​d)≥0v^{[a\_{l},b\_{l}]}(C;\mathbf{s}\_{bid})\geq 0 and v[al,bl]​(C;𝐬a​s​k)≤0v^{[a\_{l},b\_{l}]}(C;\mathbf{s}\_{ask})\leq 0 for all l=1,…,Ml=1,\ldots,M. Namely, (𝐬b​i​d,𝐬a​s​k)(\mathbf{s}\_{bid},\mathbf{s}\_{ask}) satisfies strong bid-ask compatibility.

Next, we shall prove the first implication (LP feasibility ⇒\Rightarrow strong bid-ask compatibility).
Since (𝐬b​i​d,𝐬a​s​k)∈𝒜b​i​d​-​a​s​k∘(\mathbf{s}\_{bid},\mathbf{s}\_{ask})\in\mathcal{A}\_{bid\text{-}ask}^{\circ}, there exists 𝐬b​i​d′\mathbf{s}\_{bid}^{\prime} and 𝐬a​s​k′\mathbf{s}\_{ask}^{\prime} such that 𝐬b​i​d<𝐬b​i​d′≤𝐬a​s​k′<𝐬a​s​k\mathbf{s}\_{bid}<\mathbf{s}\_{bid}^{\prime}\leq\mathbf{s}\_{ask}^{\prime}<\mathbf{s}\_{ask} and (𝐬b​i​d′,𝐬a​s​k′)∈𝒜b​i​d​-​a​s​k(\mathbf{s}\_{bid}^{\prime},\mathbf{s}\_{ask}^{\prime})\in\mathcal{A}\_{bid\text{-}ask}.
By the definition of 𝒜b​i​d​-​a​s​k\mathcal{A}\_{bid\text{-}ask}, there exists a stochastic distortion X∗X\_{\*} satisfying

|  |  |  |
| --- | --- | --- |
|  | v[al,bl]​(CX∗;𝐬b​i​d′)≥0andv[al,bl]​(CX∗;𝐬a​s​k′)≤0for 1≤l≤M.v^{[a\_{l},b\_{l}]}(C^{X\_{\*}};\mathbf{s}\_{bid}^{\prime})\geq 0\quad\text{and}\quad v^{[a\_{l},b\_{l}]}(C^{X\_{\*}};\mathbf{s}\_{ask}^{\prime})\leq 0\quad\text{for $1\leq l\leq M$}. |  |

Since v[al,bl]​(CX∗;𝐬)v^{[a\_{l},b\_{l}]}(C^{X\_{\*}};\mathbf{s}) is strictly decreasing in each component of 𝐬\mathbf{s}, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | v[al,bl]​(CX∗;𝐬b​i​d)>0andv[al,bl]​(CX∗;𝐬a​s​k)<0for 1≤l≤M.\displaystyle v^{[a\_{l},b\_{l}]}(C^{X\_{\*}};\mathbf{s}\_{bid})>0\quad\text{and}\quad v^{[a\_{l},b\_{l}]}(C^{X\_{\*}};\mathbf{s}\_{ask})<0\quad\text{for $1\leq l\leq M$}. |  | (76) |

Using the same argument as in Lemma [12.1](https://arxiv.org/html/2602.08039v1#S12.ThmLemma1 "Lemma 12.1 ‣ 12.1 Preliminary Preparations ‣ 12 Proof of Proposition 4.3"), we can construct a sequence of matrices P^(N)​(X∗)∈𝒫(N)\hat{P}^{(N)}(X\_{\*})\in\mathcal{P}^{(N)} for N∈ℕ+N\in\mathbb{N}^{+} such that

|  |  |  |
| --- | --- | --- |
|  | limN→+∞v[al,bl]​(P^(N)​(X∗);𝐬b​i​d)=v[al,bl]​(CX∗;𝐬b​i​d)for ​1≤l≤M\lim\_{N\to+\infty}v^{[a\_{l},b\_{l}]}(\hat{P}^{(N)}(X\_{\*});\mathbf{s}\_{bid})=v^{[a\_{l},b\_{l}]}(C^{X\_{\*}};\mathbf{s}\_{bid})\quad\text{for }1\leq l\leq M |  |

and

|  |  |  |
| --- | --- | --- |
|  | limN→+∞v[al,bl]​(P^(N)​(X∗);𝐬a​s​k)=v[al,bl]​(CX∗;𝐬a​s​k)for ​1≤l≤M.\lim\_{N\to+\infty}v^{[a\_{l},b\_{l}]}(\hat{P}^{(N)}(X\_{\*});\mathbf{s}\_{ask})=v^{[a\_{l},b\_{l}]}(C^{X\_{\*}};\mathbf{s}\_{ask})\quad\text{for }1\leq l\leq M. |  |

These two convergence results along with ([76](https://arxiv.org/html/2602.08039v1#S13.E76 "In 13 Proofs of Proposition 4.5 and Proposition 4.6")) imply that
there exists a sufficiently large N0∈ℕ+N\_{0}\in\mathbb{N}^{+} such that

|  |  |  |
| --- | --- | --- |
|  | v[al,bl]​(P^(N0)​(X∗);𝐬b​i​d)≥0andv[al,bl]​(P^(N0)​(X∗);𝐬a​s​k)≤0for ​1≤l≤M.v^{[a\_{l},b\_{l}]}(\hat{P}^{(N\_{0})}(X\_{\*});\mathbf{s}\_{bid})\geq 0\quad\text{and}\quad v^{[a\_{l},b\_{l}]}(\hat{P}^{(N\_{0})}(X\_{\*});\mathbf{s}\_{ask})\leq 0\quad\text{for }1\leq l\leq M. |  |

These inequalities correspond exactly to the first two sets of linear constraints in ([28](https://arxiv.org/html/2602.08039v1#S4.E28 "In Proposition 4.6 (A Sufficient and Necessary Condition for Strong Bid-Ask Compatibility) ‣ 4.6 Strong Bid-Ask Compatibility ‣ 4 Strong Compatibility")) with N=N0N=N\_{0}. On the other hand, the fact that P^(N)​(X∗)∈𝒫(N)\hat{P}^{(N)}(X\_{\*})\in\mathcal{P}^{(N)} for all N∈ℕ+N\in\mathbb{N}^{+} implies that
P^(N0)​(X∗)\hat{P}^{(N\_{0})}(X\_{\*}) satisfies the last four sets of linear constraints in ([28](https://arxiv.org/html/2602.08039v1#S4.E28 "In Proposition 4.6 (A Sufficient and Necessary Condition for Strong Bid-Ask Compatibility) ‣ 4.6 Strong Bid-Ask Compatibility ‣ 4 Strong Compatibility")) with N=N0N=N\_{0}. Thus, we conclude that P^(N)​(X∗)\hat{P}^{(N)}(X\_{\*}) is a feasible solution to ([28](https://arxiv.org/html/2602.08039v1#S4.E28 "In Proposition 4.6 (A Sufficient and Necessary Condition for Strong Bid-Ask Compatibility) ‣ 4.6 Strong Bid-Ask Compatibility ‣ 4 Strong Compatibility")). This completes the proof.
□\square

## 14 Transforming an LFP Problem into an LP Problem

Remark [4.4](https://arxiv.org/html/2602.08039v1#S4.ThmRemark4 "Remark 4.4 (Transforming LFP problems into LP problems) ‣ 4.5.1 The Key Ideas of Our Iterative Algorithm ‣ 4.5 An Efficient Algorithm for Verifying Strong Compatibility and Constructing a Corresponding Concrete Conditionally i.i.d. Copula When Satisfied ‣ 4 Strong Compatibility") mentioned that the computation of s¯N[al+1,bl+1]\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N} and s¯N[al+1,bl+1]\underline{s}^{[a\_{l+1},b\_{l+1}]}\_{N} requires solving LFP problems, which can be readily transformed into equivalent LP problems via the Charnes-Cooper transformation (Charnes and Cooper [1962](https://arxiv.org/html/2602.08039v1#bib.bib71 "Programming with linear fractional functionals")).
In this section, we outline the transformation procedure for the upper bound s¯N[al+1,bl+1]\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N}, and the lower bound can be treated in an analogous manner.

First, we express the LFP problem associated with s¯N[al+1,bl+1]\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N} in a more compact form:

|  |  |  |
| --- | --- | --- |
|  | s¯N[al+1,bl+1]=sup{p^i​k}∈𝒫Nl∑i=1m∑k=0NBi​k​p^i​kC1−∑i=1m∑k=0NAi​k​p^i​k,\overline{s}^{[a\_{l+1},b\_{l+1}]}\_{N}=\sup\_{\{\hat{p}\_{ik}\}\in\mathcal{P}\_{N}^{l}}\frac{\sum\_{i=1}^{m}\sum\_{k=0}^{N}B\_{ik}\hat{p}\_{ik}}{C\_{1}-\sum\_{i=1}^{m}\sum\_{k=0}^{N}A\_{ik}\hat{p}\_{ik}}, |  |

where Ai​kA\_{ik}, Bi​kB\_{ik}, and C1C\_{1} are pre-computed constants defined as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ai​k\displaystyle A\_{ik} | =∑j=0nD​(Ti)​(Ti−Ti−1)​βj[al+1,bl+1]​hj​k(N),\displaystyle=\sum\_{j=0}^{n}D(T\_{i})(T\_{i}-T\_{i-1})\beta\_{j}^{[a\_{l+1},b\_{l+1}]}h\_{jk}^{(N)}, | for ​1≤i≤m​0≤k≤N,\displaystyle\text{for }1\leq i\leq m0\leq k\leq N, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Bi​k\displaystyle B\_{ik} | =∑j=0n[D​(Ti+Ti−12)−D​(Ti+Ti+12)​1{i<m}]​βj[al+1,bl+1]​hj​k(N)\displaystyle=\sum\_{j=0}^{n}\left[D\left(\frac{T\_{i}+T\_{i-1}}{2}\right)-D\left(\frac{T\_{i}+T\_{i+1}}{2}\right)1\_{\{i<m\}}\right]\beta\_{j}^{[a\_{l+1},b\_{l+1}]}h\_{jk}^{(N)} | for ​1≤i≤m,0≤k≤N,\displaystyle\text{for }1\leq i\leq m,0\leq k\leq N, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C1\displaystyle C\_{1} | =∑i=1mD​(Ti)​(Ti−Ti−1)​(bl+1−al+1).\displaystyle=\sum\_{i=1}^{m}D(T\_{i})(T\_{i}-T\_{i-1})(b\_{l+1}-a\_{l+1}). |  | |

The transformation introduces a new scalar decision variable t^\hat{t} and a set of new decision variables Y^={y^i​k}1≤i≤m,0≤k≤N\hat{Y}=\{\hat{y}\_{ik}\}\_{1\leq i\leq m,0\leq k\leq N}, which are related to the original decision variables p^i​k\hat{p}\_{ik}:

|  |  |  |
| --- | --- | --- |
|  | t^:=1C1−∑i=1m∑k=0NAi​k​p^i​kandy^i​k:=p^i​k​t^.\hat{t}:=\frac{1}{C\_{1}-\sum\_{i=1}^{m}\sum\_{k=0}^{N}A\_{ik}\hat{p}\_{ik}}\quad\text{and}\quad\hat{y}\_{ik}:=\hat{p}\_{ik}\hat{t}. |  |

Plugging these new decision variables transforms into the the LFP problem yields the following equivalent LP problem in terms of the new decision variables {Y^,t^}\{\hat{Y},\hat{t}\}:
  
Maximize:

|  |  |  |
| --- | --- | --- |
|  | ∑i=1m∑k=0NBi​k​y^i​k\sum\_{i=1}^{m}\sum\_{k=0}^{N}B\_{ik}\hat{y}\_{ik} |  |

  

Subject to:

|  |  |  |
| --- | --- | --- |
|  | {C1​t^−∑i=1m∑k=0NAi​k​y^i​k−1=0,∑i=1m∑k=0Ngi​k​l′(N)​(𝐬)​y^i​k−γ[al′​bl′]​(𝐬)​t^=0for 1≤l′≤l,∑k=0Nk​y^i​k−N​F​(Ti)​t^=0for 1≤i≤m,∑j≥ky^i​j−∑j≥ky^i+1,j≤0for 1≤i≤m−1 and 1≤k≤N,y^i​k≥0for 1≤i≤m and 0≤k≤N,t^≥0.\begin{cases}C\_{1}\hat{t}-\sum\_{i=1}^{m}\sum\_{k=0}^{N}A\_{ik}\hat{y}\_{ik}-1=0,\\ \sum\_{i=1}^{m}\sum\_{k=0}^{N}g\_{ikl^{\prime}}^{(N)}(\mathbf{s})\hat{y}\_{ik}-\gamma^{[a\_{l^{\prime}}b\_{l^{\prime}}]}(\mathbf{s})\hat{t}=0\quad&\text{for $1\leq l^{\prime}\leq l$},\\ \sum\_{k=0}^{N}k\hat{y}\_{ik}-NF(T\_{i})\hat{t}=0\quad&\text{for $1\leq i\leq m$},\\ \sum\_{j\geq k}\hat{y}\_{ij}-\sum\_{j\geq k}\hat{y}\_{i+1,j}\leq 0\quad&\text{for $1\leq i\leq m-1$ and $1\leq k\leq N$},\\ \hat{y}\_{ik}\geq 0\quad&\text{for $1\leq i\leq m$ and $0\leq k\leq N$},\\ \hat{t}\geq 0.\end{cases} |  |

## 15 Standard Methods for CDS Index Calculations

This section details two methods used in our paper for CDS index calculation, and these two methods are standard in the literature (see, e.g., Cont and Kan [2011](https://arxiv.org/html/2602.08039v1#bib.bib61 "Dynamic hedging of portfolio credit derivatives"), and Hull [2022](https://arxiv.org/html/2602.08039v1#bib.bib63 "Options, futures, and other derivatives")). The first method (i.e., Algorithm [15](https://arxiv.org/html/2602.08039v1#S15 "15 Standard Methods for CDS Index Calculations")) shows how to derive the marginal default distribution F​(⋅)F(\cdot) from the market index spread sidxs^{\rm idx}.

 



Algorithm 15.1  Calculating the Marginal Distribution of Default Times

 

1. Step 1:

   For any μ>0\mu>0, define

   |  |  |  |
   | --- | --- | --- |
   |  | J1​(μ):=∑i=1m[e−μ​Ti​(Ti−Ti−1)​D​(Ti)],J2​(μ):=12​∑i=1m[(e−μ​Ti−1−e−μ​Ti)​(Ti−Ti−1)​D​(Ti+Ti−12)],J3​(μ):=(1−R)​∑i=1m[(e−μ​Ti−1−e−μ​Ti)​D​(Ti+Ti−12)].\begin{split}J\_{1}(\mu)&:=\sum\_{i=1}^{m}\left[e^{-\mu T\_{i}}(T\_{i}-T\_{i-1})D(T\_{i})\right],\\ J\_{2}(\mu)&:=\frac{1}{2}\sum\_{i=1}^{m}\left[\left(e^{-\mu T\_{i-1}}-e^{-\mu T\_{i}}\right)(T\_{i}-T\_{i-1})D\left(\frac{T\_{i}+T\_{i-1}}{2}\right)\right],\\ J\_{3}(\mu)&:=(1-R)\sum\_{i=1}^{m}\left[\left(e^{-\mu T\_{i-1}}-e^{-\mu T\_{i}}\right)D\left(\frac{T\_{i}+T\_{i-1}}{2}\right)\right].\end{split} |  |

   Here μ\mu represents the hazard rate of default times and is to be determined in Step 2.
2. Step 2:

   Solve for the hazard rate μ\mu that equates the present values of the premium and default legs of the CDS index:

   |  |  |  |
   | --- | --- | --- |
   |  | sidx​(J1​(μ)+J2​(μ))=J3​(μ).s^{\rm idx}(J\_{1}(\mu)+J\_{2}(\mu))=J\_{3}(\mu). |  |

   The marginal default distribution is then F​(t)=1−exp⁡(−μ​t)F(t)=1-\exp(-\mu t).

 

Algorithm [15](https://arxiv.org/html/2602.08039v1#S15 "15 Standard Methods for CDS Index Calculations") below details the standard method for calculating the change in the CDS index’s value Δ​vC​D​S\Delta v^{CDS} in response to a small CDS index spread change Δ​s\Delta s. Note that here Δ​vC​D​S\Delta v^{CDS} is the denominator of the spread delta δ[al,bl]\delta^{[a\_{l},b\_{l}]}, which Algorithm [5.1.1](https://arxiv.org/html/2602.08039v1#S5.SS1.SSS1 "5.1.1 A Model-Independent Hedging Strategy ‣ 5.1 Applications of Weak Compatibility ‣ 5 Applications of Weak Compatibility and Strong Compatibility") aims to compute.

 



Algorithm 15.2  Calculating the CDS Index’s Value Change Δ​vC​D​S\Delta v^{CDS} for a Spread Change Δ​s\Delta s

 

1. Step 1:

   Given the marginal default distribution F​(⋅)F(\cdot), calculate the value of PV01\mathrm{PV01} (risky annuity):

   |  |  |  |
   | --- | --- | --- |
   |  | PV01=∑i=1m(Ti−Ti−1)​(1−F​(Ti))​D​(Ti)+12​∑i=1m(Ti−Ti−1)​(F​(Ti)−F​(Ti−1))​D​(Ti+Ti−12).\mathrm{PV01}=\sum\_{i=1}^{m}(T\_{i}-T\_{i-1})(1-F(T\_{i}))D(T\_{i})+\frac{1}{2}\sum\_{i=1}^{m}(T\_{i}-T\_{i-1})(F(T\_{i})-F(T\_{i-1}))D\left(\frac{T\_{i}+T\_{i-1}}{2}\right). |  |
2. Step 2:

   The change in the CDS index’s value Δ​vC​D​S\Delta v^{CDS} for an index spread change Δ​s\Delta s is then computed as follows:

   |  |  |  |
   | --- | --- | --- |
   |  | Δ​vC​D​S=PV01×Δ​s.\Delta v^{CDS}=\mathrm{PV01}\times\Delta s. |  |