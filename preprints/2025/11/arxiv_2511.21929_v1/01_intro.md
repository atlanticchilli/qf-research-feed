---
authors:
- Peng Liu
- Yang Liu
- Houhan Teng
doc_id: arxiv:2511.21929v1
family_id: arxiv:2511.21929
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation
  and Risk Sharing'
url_abs: http://arxiv.org/abs/2511.21929v1
url_html: https://arxiv.org/html/2511.21929v1
venue: arXiv q-fin
version: 1
year: 2025
---


Peng Liu
School of Mathematics, Statistics and Actuarial Science, University of Essex, UK. Email: peng.liu@essex.ac.uk
  
Yang Liu
School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen, China. Email: yangliu16@cuhk.edu.cn
  
Houhan Teng
School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen, China. Email: s2447087@link.cuhk.edu.cn

###### Abstract

In this paper, we provide extended convolution bounds for the Fréchet problem and discuss related implications in quantitative risk management. First, we establish a new form of inequality for the Range-Value-at-Risk (RVaR\mathrm{RVaR}). Based on this inequality, we obtain bounds for robust risk aggregation with dependence uncertainty for (i) RVaR\mathrm{RVaR}, (ii) inter-RVaR difference and (iii) inter-quantile difference, and provide sharpness conditions.
These bounds are called extended convolution bounds, which not only complement the results in the literature (convolution bounds in Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8))) but also offer results for some variability measures. Next, applying the above inequality, we study the risk sharing for the averaged quantiles (corresponding to risk sharing for distortion risk measures with special inverse S-shaped distortion functions), which is a non-convex optimization problem. We obtain the expression of the minimal value of the risk sharing and the explicit expression for the corresponding optimal allocation, which is comonotonic risk sharing for large losses and counter-comonotonic risk sharing for small losses or large gains. Finally, we explore the dependence structure for the optimal allocations, showing that the optimal allocation does not exist if the risk is not bounded from above.

Key-words: Robust risk aggregation; Risk sharing;
Range-Value-at-Risk (RVaR\mathrm{RVaR}); Quantiles; Inter-RVaR\mathrm{RVaR} difference; Inter-quantile difference; Distortion risk measures; Dependence uncertainty

## 1 Introduction

The Fréchet ([1951](https://arxiv.org/html/2511.21929v1#bib.bib29)) problem in probability theory concerns the characterization of possible distributions of f​(X1,…,Xn)f(X\_{1},\dots,X\_{n}) if the distributions of the random variables X1,X2,…,XnX\_{1},X\_{2},\dots,X\_{n} are known, but their joint dependence structure is unspecified, where f:ℝn→ℝf:\mathbb{R}^{n}\to\mathbb{R} is a measurable function. Typically, ff is the sum, and we denote the sum variable by S=X1+X2+⋯+XnS=X\_{1}+X\_{2}+\dots+X\_{n}. Formally, given the set of feasible joint distributions with some fixed marginal distributions (formulated from Dall’Aglio ([1956](https://arxiv.org/html/2511.21929v1#bib.bib15))), the problem seeks to determine sharp bounds on functionals of SS, such as its cumulative distribution function (cdf) or quantiles. This problem dates back to Hoeffding ([1940](https://arxiv.org/html/2511.21929v1#bib.bib31)) and the classical Fréchet-Hoeffding bounds establish the preliminary theory on the possible dependence structure. Further, if n=2n=2, analytical results on the largest possible distribution (equivalently, the largest quantiles) of SS were derived in Makarov ([1981](https://arxiv.org/html/2511.21929v1#bib.bib43)) and Rüschendorf ([1982](https://arxiv.org/html/2511.21929v1#bib.bib50)). However, if n⩾3n\geqslant 3, the problem becomes substantially more complex when optimizing among all admissible copulas to obtain the best-possible bounds for some specific functionals. This problem has a deep connection with measure theory, functional analysis and optimal transport, as it involves constrained optimization over spaces of probability measures; see Embrechts and Puccetti ([2006](https://arxiv.org/html/2511.21929v1#bib.bib22)) and Nutz and Wang ([2022](https://arxiv.org/html/2511.21929v1#bib.bib45)).

Beyond its theoretical significance, the Fréchet problem of the sum variable plays a crucial role in risk management, where dependence assumptions significantly impact the evaluation of risk measures on SS such as Value-at-Risk (VaR; quantile) and Expected Shortfall (ES). In practice, some data from different correlated products are separately collected and thus no dependence information is available; see Embrechts et al. ([2013](https://arxiv.org/html/2511.21929v1#bib.bib23)) and Embrechts et al. ([2015](https://arxiv.org/html/2511.21929v1#bib.bib24)). Even if the data are available, the estimation of the dependence structure typically has low accuracy, resulting in a lot of uncertainty on the choice of the dependence structure; see e.g., Chapter 8 of McNeil et al. ([2015](https://arxiv.org/html/2511.21929v1#bib.bib44)). Consequently, sharp bounds for some risk functionals under dependence uncertainty indicate the worst/best-case (robust) risk aggregation and evaluation, which is hence of great significance. Besides,
the Fréchet problem has a wide application in different areas of operations research, including assembling line crew scheduling (Hsu ([1984](https://arxiv.org/html/2511.21929v1#bib.bib32))), matching theory (Boerma et al. ([2023](https://arxiv.org/html/2511.21929v1#bib.bib9))), worst-case portfolio selection (Chen et al. ([2022](https://arxiv.org/html/2511.21929v1#bib.bib12))), multiple statistical hypothesis testing (Vovk et al. ([2022](https://arxiv.org/html/2511.21929v1#bib.bib54))), etc; a comprehensive discussion was given in Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)).
Consequently, recent technical advances in optimal transport (Bartl et al. ([2022](https://arxiv.org/html/2511.21929v1#bib.bib4))), copula theory (Koike et al. ([2024](https://arxiv.org/html/2511.21929v1#bib.bib35))), variational methods and numerical optimization (Shapiro et al. ([2021](https://arxiv.org/html/2511.21929v1#bib.bib52))) have been incorporated into the study of the Fréchet problem, thereby enabling more precise characterizations in probability theory and furnishing additional tools for these various disciplines.

In the field of quantitative risk management, the Fréchet problem is often referred to as the risk aggregation problem with dependence uncertainty, which is inherently challenging due to its nature.
Explicit expressions are only available in some special cases of the marginal distributions. For general marginal distributions, only bounds are available for robust quantiles in the literature; see e.g., the dual bounds in Theorem 4.17 of Rüschendorf ([2013](https://arxiv.org/html/2511.21929v1#bib.bib51)). The explicit expression for robust quantiles is only available for marginal distributions with monotone densities; see e.g., Wang et al. ([2013](https://arxiv.org/html/2511.21929v1#bib.bib57)), Bernard et al. ([2014](https://arxiv.org/html/2511.21929v1#bib.bib6)) and Jakobsons et al. ([2016](https://arxiv.org/html/2511.21929v1#bib.bib33)), where the worst-case dependence structure is a combination of joint-mixability (see Wang and Wang ([2016](https://arxiv.org/html/2511.21929v1#bib.bib58))) and mutual exclusivity (introduced in Dhaene and Denuit ([1999](https://arxiv.org/html/2511.21929v1#bib.bib17))). Recently, Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)) offered a so-called convolution bound, which is proved to be the sharp bound for robust RVaR\mathrm{RVaR} and quantiles under some specific cases, especially including the case that all the marginal distributions have monotonic densities in the same direction on their tail parts. Here, RVaR\mathrm{RVaR} (Range-Value-at-Risk) is a two-parameter class of non-convex risk measures, including both VaR\mathrm{VaR} and ES\mathrm{ES} as special cases, which will be defined in ([2.1](https://arxiv.org/html/2511.21929v1#S2.E1 "In 2 Notation and Definitions ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")). In general, computational and optimization approaches, such as rearrangement algorithms (Embrechts et al. ([2013](https://arxiv.org/html/2511.21929v1#bib.bib23))), scheduling (Boudt et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib10))), neural networks (Eckstein et al. ([2020](https://arxiv.org/html/2511.21929v1#bib.bib19))), and linear programming formulations (Altschuler and Boix-Adserà ([2021](https://arxiv.org/html/2511.21929v1#bib.bib1))), have been developed to approximate the sharp bounds numerically, albeit with their own drawbacks. It is worth noting that the convolution bound is closely linked to the RVaR\mathrm{RVaR} inequality in Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20)), which is used to address risk-sharing problems among multiple agents with risk preferences characterized by RVaR\mathrm{RVaR}.

Indeed, the Fréchet problem offers a distinctive perspective on studying the risk sharing problem, as risk sharing can be viewed as the “inverse” of risk aggregation. The risk sharing problem concerns redistributing a total risk among multiple participants, requiring the determination of the optimal allocations. This problem has a long history, dating back to the seminal work of Borch ([1962](https://arxiv.org/html/2511.21929v1#bib.bib11)), which studied risk sharing through the framework of expected utility.
Over the past two decades, researchers have explored risk sharing problems using risk measures to represent participants’ risk preferences since the introduction of coherent and convex risk measures in Artzner et al. ([1999](https://arxiv.org/html/2511.21929v1#bib.bib2)), Föllmer and Schied ([2002](https://arxiv.org/html/2511.21929v1#bib.bib27)) and Frittelli and Rosazza Gianin ([2005](https://arxiv.org/html/2511.21929v1#bib.bib30)). For instance, Barrieu and El Karoui ([2005](https://arxiv.org/html/2511.21929v1#bib.bib3)), Jouini et al. ([2008](https://arxiv.org/html/2511.21929v1#bib.bib34)), Filipović and Svindland ([2008](https://arxiv.org/html/2511.21929v1#bib.bib26)) and Delbaen ([2012](https://arxiv.org/html/2511.21929v1#bib.bib16)) examined risk sharing problems based on risk measures satisfying convexity and law invariance, leading to comonotonic optimal allocations. Moreover, Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20)) investigated risk sharing for RVaR\mathrm{RVaR}, derived the minimal value of risk sharing (called inf-convolution) and provided explicit expressions for optimal allocations in both cooperative and competitive settings; see also Embrechts et al. ([2020](https://arxiv.org/html/2511.21929v1#bib.bib21)). Besides, some other non-convex risk measures were also studied in the risk sharing problem such as VaR\mathrm{VaR}-type distortion risk measures (Weber ([2018](https://arxiv.org/html/2511.21929v1#bib.bib60))), Lambda VaR\mathrm{VaR} (Liu ([2025](https://arxiv.org/html/2511.21929v1#bib.bib42))), inter-quantile difference (Lauzier et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib38))) and general non-convex risk measures (Liebrich ([2024](https://arxiv.org/html/2511.21929v1#bib.bib39))).

In this paper, we focus on the theoretical aspect of the Fréchet problem rather than the application side, and we elaborate on our contribution as follows.
First, we establish a new type of upper and lower bounds for robust risk aggregation with RVaR\mathrm{RVaR} under dependence uncertainty in Section [4.1](https://arxiv.org/html/2511.21929v1#S4.SS1 "4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"). We show that those bounds are sharp as upper bounds if the marginal distributions have increasing densities on their upper-tail parts and also sharp as lower bounds if the marginal distributions have decreasing densities on their lower-tail parts. These bounds use a general structure of averaged quantiles to obtain new forms of bounds, and offer new sharpness results for robust RVaR compared with those in Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)). Specifically, while the convolution bound for robust RVaR in Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)) is a sharp lower bound if the marginal distributions exhibit increasing densities on their lower-tail parts, our derived bound achieves sharpness for lower bound if marginal distributions have decreasing densities on their lower-tail parts.

Second, we obtain two more types of upper bounds for the difference between two RVaR\mathrm{RVaR}s and that between two quantiles, called inter-RVaR\mathrm{RVaR} difference (IRD\mathrm{IRD}) and, for a special case, inter-quantile difference (IQD\mathrm{IQD}) respectively in Section [4.2](https://arxiv.org/html/2511.21929v1#S4.SS2 "4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"). Note that IRD\mathrm{IRD} extends the inter-ES\mathrm{ES} proposed in Bellini et al. ([2022](https://arxiv.org/html/2511.21929v1#bib.bib5)) as an alternative to the standard deviation to measure the variability of risks. It is well known that IQD\mathrm{IQD} is frequently used to find the outliers and measure the statistical dispersion in statistics. Moreover, IQD\mathrm{IQD} is also a tool to quantify the variability of risks; see Bellini et al. ([2022](https://arxiv.org/html/2511.21929v1#bib.bib5)) and Lauzier et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib38)). Importantly, we find that the robust IRD\mathrm{IRD} (resp., IQD\mathrm{IQD}) equals the difference between the two robust RVaR\mathrm{RVaR} (resp., quantiles). Hence, the explicit expressions are derived based on the robust RVaR\mathrm{RVaR} and quantiles for marginal distributions with monotone densities on both upper- and lower-tail parts. We offer two different sharp upper bounds for IRD\mathrm{IRD} under different assumptions on the marginal distributions: the first condition requires the marginals to have decreasing densities on their upper-tail parts and increasing densities on their lower-tail parts; whereas the second requires decreasing densities on both upper- and lower-tail parts, respectively. Commonly used continuous distributions in finance or risk management (e.g., Gaussian, lognormal, t, exponential, and Pareto) mostly fall into either of the two categories.
Those two expressions for the sharp upper bound of IRD\mathrm{IRD} together with their different assumptions demonstrate the complexity of the robust risk aggregation for IRD\mathrm{IRD} and also the usefulness of our new bounds established in Section [4.1](https://arxiv.org/html/2511.21929v1#S4.SS1 "4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"). The sharp upper bound for the difference between two quantiles requires the marginals to have densities that are monotone in the same direction on both upper- and lower-tail parts, respectively, which is valid for almost all the commonly used continuous distributions. All three types of bounds established in our paper are generally called extended convolution bounds, as they can be viewed as an extension of the convolution bounds from RVaR\mathrm{RVaR} and quantiles to the corresponding variability measures introduced in Bellini et al. ([2022](https://arxiv.org/html/2511.21929v1#bib.bib5)).

Third,
we study the risk sharing problem for some averaged quantiles, which is equivalent to the risk sharing problem for distortion risk measures with some special inverse S-shaped distortion functions. This class of distortion risk measures represents the decision maker’s typical attitude: risk aversion for large losses and risk-seeking for small losses or gains; see Yaari ([1987](https://arxiv.org/html/2511.21929v1#bib.bib61)) and Tversky and Kahneman ([1992](https://arxiv.org/html/2511.21929v1#bib.bib53)). Clearly, this problem is non-convex and challenging. It turns out that the inf-convolution has a very simple form: the lower-tail ES\mathrm{ES}, which is an averaged quantile below a specified quantile of the total risk. Moreover, the optimal allocation, which is Pareto-optimal, exists if and only if the total risk is bounded from above. The structure of the optimal allocation consists of two parts: The upper-tail part of the total risk is shared comonotonically, and the lower-tail part of the risk is shared counter-monotonically. This optimal allocation is consistent with the agents’ risk attitudes: risk-aversion for large losses and risk-seeking for small losses or large gains. If the total risk is not bounded from above, the optimal allocation does not exist, where the proof is based on the analysis of the dependence structure of the optimal allocations. Instead, in this case, we find a sequence of sub-optimal allocations such that the risk exposures generated by those allocations converge to the inf-convolution. We emphasize that our optimal allocation is the combination of the existed optimal allocations for convex risk measures and quantile-based risk measures in the literature; see e.g., Jouini et al. ([2008](https://arxiv.org/html/2511.21929v1#bib.bib34)) and Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20)). Although we only solve the risk sharing problem for distortion risk measures with some special inverse S-shaped distortion functions, we emphasize that to best of our knowledge, this is the first non-constrained risk sharing result for this class of distortion risk measures with the distortion functions exaggerating the probability of large losses and the probability of large gains simultaneously. It sheds light on the further investigation into the risk sharing for general inverse-S-shaped distortion risk measures.

The rest of the paper is organized as follows. We give some notation and definitions in Section [2](https://arxiv.org/html/2511.21929v1#S2 "2 Notation and Definitions ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"). We establish a new inequality for RVaR\mathrm{RVaR} in Section [3](https://arxiv.org/html/2511.21929v1#S3 "3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"). Based on this new inequality, we obtain some bounds on risk aggregation for RVaR\mathrm{RVaR}, the difference between two RVaR\mathrm{RVaR} and the difference between two quantiles in Section [4](https://arxiv.org/html/2511.21929v1#S4 "4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"). Employing this inequality, we study the risk sharing problem for the averaged quantiles and obtain the condition for the existence of the Pareto-optimal allocations and the forms of the the Pareto-optimal allocations in Section [5](https://arxiv.org/html/2511.21929v1#S5 "5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"). Section [6](https://arxiv.org/html/2511.21929v1#S6 "6 Conclusion ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") concludes the paper.

## 2 Notation and Definitions

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be an atomless probability space and 𝒳=L0​(Ω,ℱ,ℙ)\mathcal{X}=L^{0}(\Omega,\mathcal{F},\mathbb{P}) be the set of all random variables, and 𝒳1=L1​(Ω,ℱ,ℙ)\mathcal{X}\_{1}=L^{1}(\Omega,\mathcal{F},\mathbb{P}) be the set of all random variables with finite mean. Correspondingly, we denote the set of all distributions of the random variables in 𝒳\mathcal{X} by ℳ\mathcal{M}, and by ℳ1\mathcal{M}\_{1} the set of all distributions of the random variables in 𝒳1\mathcal{X}\_{1}. To ease the notation, we treat almost surely equal random variables and events as identical and set [n]:={1,…,n}[n]:=\{1,\dots,n\} for n∈ℕ+.n\in\mathbb{N}^{+}. Throughout this paper, we use U​[a,b]\mathrm{U}[a,b] with a<ba<b to represent the uniform distribution on [a,b][a,b]. For any X∈𝒳X\in\mathcal{X}, let UX∼U​[0,1]U\_{X}\sim U[0,1] such that FX−1​(UX)=XF\_{X}^{-1}(U\_{X})=X and UXU\_{X} is usually called the probability transform of XX (e.g., Proposition 7.2 of McNeil et al. ([2015](https://arxiv.org/html/2511.21929v1#bib.bib44))); The existence of such UXU\_{X} is guaranteed (e.g.,
Lemma A.32 of Föllmer and Schied ([2016](https://arxiv.org/html/2511.21929v1#bib.bib28))). In this paper, the probability measure (μ\mu) and the distribution function (FF) are considered equivalent. Either of them may be used according to the context. Moreover, terms like “increasing” and “decreasing” are in the non-strict sense.

Next, we introduce a family of risk measures: the average quantile functional RR. For any I∈ℬ​([0,1])I\in\mathcal{B}([0,1]) with |I|>0|I|>0, the functional RI:ℳ→ℝR\_{I}:\mathcal{M}\rightarrow\mathbb{R} is defined as

|  |  |  |
| --- | --- | --- |
|  | RI​(μ)=1|I|​∫Iqt−​(μ)​dt,R\_{I}(\mu)=\frac{1}{|I|}\int\_{I}q^{-}\_{t}(\mu)\mathrm{d}t, |  |

where |I||I| is the length of II under the Lebesgue measure on ℝ\mathbb{R} and
qt−​(μ)=inf{x∈ℝ:μ​((−∞,x])⩾t}q^{-}\_{t}(\mu)=\inf\{x\in\mathbb{R}:\mu((-\infty,x])\geqslant t\} is the left quantile of distribution μ\mu with t∈(0,1]t\in(0,1]. As RIR\_{I} is a law-invariant risk measure, we abuse the notation RI​(X)R\_{I}(X) with RI​(μ)R\_{I}(\mu) for a random variable X∼μX\sim\mu. This abuse may also apply to other law-invariant risk measures in our paper.

###### Remark 1.

1. (i)

   In fact, one could also define RIR\_{I} using qt+​(μ)q\_{t}^{+}(\mu), which does not affect the value of the functional as qt−​(μ)≠qt+​(μ)q\_{t}^{-}(\mu)\neq q\_{t}^{+}(\mu) only holds at a countable number of points over (0,1)(0,1).
2. (ii)

   Further, let I⊆[0,1]I\subseteq[0,1] be a union of finite many intervals and denote by I¯\bar{I} the closure of II. As the integral value does not change if the integral region is changed within countable many points, we have RI​(μ)=RI¯​(μ)R\_{I}(\mu)=R\_{\bar{I}}(\mu).
   Thus, without loss of generality, we always write any interval in II as a closed one.

The average quantile functional includes the classic risk measure, Range-Value-at-Risk (RVaR\mathrm{RVaR}), as a special case in the following way:

|  |  |  |  |
| --- | --- | --- | --- |
|  | RVaRβ,β+α​(μ)=1α​∫ββ+αq1−t+​(μ)​dt=R[1−β−α,1−β]​(μ),μ∈ℳ,\mathrm{RVaR}\_{\beta,\beta+\alpha}(\mu)=\frac{1}{\alpha}\int\_{\beta}^{\beta+\alpha}q^{+}\_{1-t}(\mu)\mathrm{d}t=R\_{[1-\beta-\alpha,1-\beta]}(\mu),~~\mu\in\mathcal{M}, |  | (2.1) |

where 0<β<β+α⩽10<\beta<\beta+\alpha\leqslant 1. Note that RVaR\mathrm{RVaR} was first introduced by Cont et al. ([2010](https://arxiv.org/html/2511.21929v1#bib.bib14)) as a family of robust risk measures, and it was further applied to the risk sharing and optimal reinsurance problem as the preference functional in Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20)) and Fadina et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib25)). Note that RVaR\mathrm{RVaR} includes ES\mathrm{ES} and LES\mathrm{LES} (Left ES) as special cases in the following way:
For p∈(0,1]p\in(0,1],

|  |  |  |
| --- | --- | --- |
|  | ESp​(μ)=1p​∫1−p1qu−​(μ)​du=R[1−p,1]​(μ)​ and ​LESp​(μ)=1p​∫0pqu−​(μ)​du=R[0,p]​(μ),μ∈ℳ1.\mathrm{ES}\_{p}(\mu)=\frac{1}{p}\int\_{1-p}^{1}q\_{u}^{-}(\mu)\mathrm{d}u=R\_{[1-p,1]}(\mu)\mbox{~~~and~~~}\mathrm{LES}\_{p}(\mu)=\frac{1}{p}\int\_{0}^{p}q\_{u}^{-}(\mu)\mathrm{d}u=R\_{[0,p]}(\mu),~~\mu\in\mathcal{M}\_{1}. |  |

Moreover, both qβ−​(μ)q\_{\beta}^{-}(\mu) and qβ+​(μ)q\_{\beta}^{+}(\mu) for β∈(0,1)\beta\in(0,1) appear as the limits of some RIR\_{I} via

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limα↓0R[β−α,β]​(μ)=qβ−​(μ)​ and ​limα↓0R[β,β+α]=qβ+​(μ),μ∈ℳ.\displaystyle\lim\_{\alpha\downarrow 0}R\_{[\beta-\alpha,\beta]}(\mu)=q\_{\beta}^{-}(\mu)\mbox{~~~and~~~}\lim\_{\alpha\downarrow 0}R\_{[\beta,\beta+\alpha]}=q\_{\beta}^{+}(\mu),~~\mu\in\mathcal{M}. |  |

For 𝝁=(μ1,…,μn)∈ℳn\boldsymbol{\mu}=(\mu\_{1},\dots,\mu\_{n})\in\mathcal{M}^{n}, let Γ​(𝝁)\Gamma(\boldsymbol{\mu}) be the set of probability measures on ℝn\mathbb{R}^{n} with one-dimensional marginals μ1,…,μn\mu\_{1},\dots,\mu\_{n}. For a probability measure μ\mu on (ℝn,ℬ​(ℝn))(\mathbb{R}^{n},\mathcal{B}(\mathbb{R}^{n})), define λμ∈ℳ\lambda\_{\mu}\in\mathcal{M} via

|  |  |  |
| --- | --- | --- |
|  | λμ​((−∞,x])=μ​({(x1,…,xn)∈ℝn:x1+⋯+xn⩽x}),x∈ℝ.\lambda\_{\mu}((-\infty,x])=\mu(\{(x\_{1},\dots,x\_{n})\in\mathbb{R}^{n}:x\_{1}+\dots+x\_{n}\leqslant x\}),~x\in\mathbb{R}. |  |

In other words, λμ\lambda\_{\mu} is an aggregated probability measure of the sum variable ∑i=1nXi\sum\_{i=1}^{n}X\_{i}, where the random vector (X1,…,Xn)(X\_{1},\dots,X\_{n}) follows the nn-dimensional distribution μ\mu.
Moreover, let Λ​(𝝁)={λμ:μ∈Γ​(𝝁)}\Lambda(\boldsymbol{\mu})=\{\lambda\_{\mu}:\mu\in\Gamma(\boldsymbol{\mu})\} be the set of all aggregated probability measures with specified marginals 𝝁\boldsymbol{\mu}.
Define an approximate standard simplex

|  |  |  |
| --- | --- | --- |
|  | Δn={(β0,β1,…,βn)∈(0,1)×[0,1)n:∑i=0nβi=1}.\Delta\_{n}=\left\{(\beta\_{0},\beta\_{1},\dots,\beta\_{n})\in(0,1)\times[0,1)^{n}:\sum\_{i=0}^{n}\beta\_{i}=1\right\}. |  |

Note that Δn\Delta\_{n} is neither open nor closed; hence, we use the term “approximate”.
For real numbers xi,i∈[n]x\_{i},i\in[n], we use the notation ⋁i=1nxi=maxi∈[n]⁡xi\bigvee\_{i=1}^{n}x\_{i}=\max\_{i\in[n]}x\_{i} and ⋀i=1nxi=mini∈[n]⁡xi\bigwedge\_{i=1}^{n}x\_{i}=\min\_{i\in[n]}x\_{i}.
Finally, for μ∈ℳ\mu\in\mathcal{M} and r∈(0,1)r\in(0,1), let μr+\mu^{r+} be the probability measure given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | μr+​(−∞,x]=max⁡{μ​(−∞,x]−r1−r,0},x∈ℝ,\mu^{r+}(-\infty,x]=\max\left\{\frac{\mu(-\infty,x]-r}{1-r},0\right\},~~x\in\mathbb{R}, |  | (2.2) |

which is called the rr-tail distribution of μ\mu in Rockafellar and Uryasev ([2002](https://arxiv.org/html/2511.21929v1#bib.bib49)). Indeed, μr+\mu^{r+} is the distribution measure of the random variable qU−​(μ)q^{-}\_{U}(\mu), where U∼U​[r,1]U\sim U[r,1]. Equivalently, μr+\mu^{r+} is the distribution measure of μ\mu restricted beyond its rr-quantile (assuming no mass at this point). In this paper, a statement that μ\mu admits a decreasing (resp., increasing) density beyond its rr-quantile is equivalent to the one that μr+\mu^{r+} admits a decreasing (resp., increasing) density on its support. An analogous definition applies to the probability measure μr−\mu^{r-}:

|  |  |  |
| --- | --- | --- |
|  | μr−​(−∞,x]=min⁡{μ​(−∞,x]r,1},x∈ℝ.\mu^{r-}\left(-\infty,x\right]=\min\left\{\frac{\mu\left(-\infty,x\right]}{r},1\right\},~~x\in\mathbb{R}. |  |

That is, μr−\mu^{r-} is the distribution measure of the random variable qV−​(μ)q^{-}\_{V}(\mu), where V∼U​[0,r]V\sim\mathrm{U}[0,r]. A statement that μ\mu admits a decreasing (resp., increasing) density below its rr-quantile is equivalent to the one that μr−\mu^{r-} admits a decreasing (resp., increasing) density on its support.

## 3 New RVaR Inequality

In this section, we establish a new inequality for RVaR\mathrm{RVaR}. This inequality will play a crucial role in establishing the bounds for risk aggregation with dependence uncertainty and in analyzing the risk sharing problem later.
Before showing our result, we first display Propositions 1 and A.1 of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)) (originally from Theorem 4.1 of Liu and Wang ([2021](https://arxiv.org/html/2511.21929v1#bib.bib41))) as below, which will be used frequently later.

###### Lemma 1 (Propositions 1 and A.1 of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8))).

Suppose 𝛍=(μ1,…,μn)∈ℳn\boldsymbol{\mu}=(\mu\_{1},\dots,\mu\_{n})\in\mathcal{M}^{n} and 0⩽r<r+s⩽10\leqslant r<r+s\leqslant 1. We have

|  |  |  |
| --- | --- | --- |
|  | supν∈Λ​(𝝁)R[r,r+s]​(ν)=supν∈Λ​(𝝁r+)LESs1−r​(ν),infν∈Λ​(𝝁)R[r,r+s]​(ν)=infν∈Λ​(𝝁(r+s)−)ESsr+s​(ν).\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}R\_{[r,r+s]}(\nu)=\sup\_{\nu\in\Lambda(\boldsymbol{\mu}^{r+})}\mathrm{LES}\_{\frac{s}{1-r}}(\nu),~\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}R\_{[r,r+s]}(\nu)=\inf\_{\nu\in\Lambda(\boldsymbol{\mu}^{(r+s)-})}\mathrm{ES}\_{\frac{s}{r+s}}(\nu). |  |

Next, we offer a new inequality for RVaR\mathrm{RVaR}.

###### Theorem 1 (New RVaR\mathrm{RVaR} Inequality).

Let 0<r<r+s⩽10<r<r+s\leqslant 1, α1,…,αn⩾0\alpha\_{1},\dots,\alpha\_{n}\geqslant 0 and β1,…,βn>0\beta\_{1},\dots,\beta\_{n}>0 satisfying ∑i=1nαi+⋁i=1nβi⩽1−r\sum\_{i=1}^{n}\alpha\_{i}+\bigvee\_{i=1}^{n}\beta\_{i}\leqslant 1-r and ∑i=1nαi⩽s\sum\_{i=1}^{n}\alpha\_{i}\leqslant s. Then for 𝛍∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} and ν∈Λ​(𝛍)\nu\in\Lambda(\boldsymbol{\mu}), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | R[r,r+s]​(ν)⩽∑i=1n[1−r−βis​R[r,r+αi]∪[r+αi+βi,1]​(μi)+(1−1−r−βis)​R[r+αi,r+αi+βi]​(μi)].R\_{[r,r+s]}(\nu)\leqslant\sum\_{i=1}^{n}\left[\frac{1-r-\beta\_{i}}{s}R\_{[r,r+\alpha\_{i}]\cup[r+\alpha\_{i}+\beta\_{i},1]}\left(\mu\_{i}\right)+\left(1-\frac{1-r-\beta\_{i}}{s}\right)R\_{[r+\alpha\_{i},r+\alpha\_{i}+\beta\_{i}]}\left(\mu\_{i}\right)\right]. |  | (3.1) |

Moreover, ([3.1](https://arxiv.org/html/2511.21929v1#S3.E1 "In Theorem 1 (New RVaR Inequality). ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) holds for r=0r=0 if 𝛍∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n}.

###### Proof.

First, we suppose 𝝁∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n} and r>0r>0.
Let Xi∼μir+,i∈[n]X\_{i}\sim\mu\_{i}^{r+},i\in[n] (note that we define the notation in Equation ([2.2](https://arxiv.org/html/2511.21929v1#S2.E2 "In 2 Notation and Definitions ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"))) and S=∑i=1nXiS=\sum\_{i=1}^{n}X\_{i}. Throughout the proof, we assume αi,βi⩾0\alpha\_{i},\beta\_{i}\geqslant 0 and ∑i=1nαi+⋁i=1nβi⩽1\sum\_{i=1}^{n}\alpha\_{i}+\bigvee\_{i=1}^{n}\beta\_{i}\leqslant 1. By Theorem 1 of Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20)), for ⋁i=1nβi⩽u⩽1−∑i=1nαi\bigvee\_{i=1}^{n}\beta\_{i}\leqslant u\leqslant 1-\sum\_{i=1}^{n}\alpha\_{i}, we have

|  |  |  |
| --- | --- | --- |
|  | R[1−∑i=1nαi−u,1−∑i=1nαi]​(S)⩽∑i=1nR[1−αi−βi,1−αi]​(Xi).R\_{[1-\sum\_{i=1}^{n}\alpha\_{i}-u,1-\sum\_{i=1}^{n}\alpha\_{i}]}(S)\leqslant\sum\_{i=1}^{n}R\_{[1-\alpha\_{i}-\beta\_{i},1-\alpha\_{i}]}(X\_{i}). |  |

Letting 0<t<1−∑i=1nαi0<t<1-\sum\_{i=1}^{n}\alpha\_{i} and (⋁i=1nβi)∨t<u⩽1−∑i=1nαi\left(\bigvee\_{i=1}^{n}\beta\_{i}\right)\lor t<u\leqslant 1-\sum\_{i=1}^{n}\alpha\_{i}, it is easy to check

|  |  |  |
| --- | --- | --- |
|  | R[1−∑i=1nαi−u,1−∑i=1nαi−t]​(S)⩽R[1−∑i=1nαi−u,1−∑i=1nαi]​(S)⩽∑i=1nR[1−αi−βi,1−αi]​(Xi).R\_{[1-\sum\_{i=1}^{n}\alpha\_{i}-u,1-\sum\_{i=1}^{n}\alpha\_{i}-t]}(S)\leqslant R\_{[1-\sum\_{i=1}^{n}\alpha\_{i}-u,1-\sum\_{i=1}^{n}\alpha\_{i}]}(S)\leqslant\sum\_{i=1}^{n}R\_{[1-\alpha\_{i}-\beta\_{i},1-\alpha\_{i}]}(X\_{i}). |  |

Then, replacing XiX\_{i} with −Xi-X\_{i}, it follows that

|  |  |  |
| --- | --- | --- |
|  | R[∑i=1nαi+t,∑i=1nαi+u]​(S)⩾∑i=1nR[αi,αi+βi]​(Xi).R\_{[\sum\_{i=1}^{n}\alpha\_{i}+t,\sum\_{i=1}^{n}\alpha\_{i}+u]}(S)\geqslant\sum\_{i=1}^{n}R\_{[\alpha\_{i},\alpha\_{i}+\beta\_{i}]}(X\_{i}). |  |

Letting u=1−∑i=1nαiu=1-\sum\_{i=1}^{n}\alpha\_{i}, we have

|  |  |  |
| --- | --- | --- |
|  | R[∑i=1nαi+t,1]​(S)⩾∑i=1nR[αi,αi+βi]​(Xi).R\_{[\sum\_{i=1}^{n}\alpha\_{i}+t,1]}(S)\geqslant\sum\_{i=1}^{n}R\_{[\alpha\_{i},\alpha\_{i}+\beta\_{i}]}(X\_{i}). |  |

Using the fact that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(S)=(1−∑i=1nαi−t)​R[∑i=1nαi+t,1]​(S)+(∑i=1nαi+t)​R[0,∑i=1nαi+t]​(S),\mathbb{E}(S)=\left(1-\sum\_{i=1}^{n}\alpha\_{i}-t\right)R\_{[\sum\_{i=1}^{n}\alpha\_{i}+t,1]}(S)+\left(\sum\_{i=1}^{n}\alpha\_{i}+t\right)R\_{[0,\sum\_{i=1}^{n}\alpha\_{i}+t]}(S), |  |

we further have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(S)−(∑i=1nαi+t)​R[0,∑i=1nαi+t]​(S)⩾(1−∑i=1nαi−t)​∑i=1nR[αi,αi+βi]​(Xi),\mathbb{E}(S)-\left(\sum\_{i=1}^{n}\alpha\_{i}+t\right)R\_{[0,\sum\_{i=1}^{n}\alpha\_{i}+t]}(S)\geqslant\left(1-\sum\_{i=1}^{n}\alpha\_{i}-t\right)\sum\_{i=1}^{n}R\_{[\alpha\_{i},\alpha\_{i}+\beta\_{i}]}(X\_{i}), |  |

which can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | R[0,∑i=1nαi+t]​(S)⩽1∑i=1nαi+t​∑i=1n(𝔼​(Xi)−(1−∑i=1nαi−t)​R[αi,αi+βi]​(Xi)).R\_{[0,\sum\_{i=1}^{n}\alpha\_{i}+t]}(S)\leqslant\frac{1}{\sum\_{i=1}^{n}\alpha\_{i}+t}\sum\_{i=1}^{n}\left(\mathbb{E}(X\_{i})-\left(1-\sum\_{i=1}^{n}\alpha\_{i}-t\right)R\_{[\alpha\_{i},\alpha\_{i}+\beta\_{i}]}(X\_{i})\right). |  |

Noting that 𝔼​(Xi)=(1−βi)​R[0,αi]∪[αi+βi,1]​(Xi)+βi​R[αi,αi+βi]​(Xi)\mathbb{E}(X\_{i})=(1-\beta\_{i})R\_{[0,\alpha\_{i}]\cup[\alpha\_{i}+\beta\_{i},1]}(X\_{i})+\beta\_{i}R\_{[\alpha\_{i},\alpha\_{i}+\beta\_{i}]}(X\_{i}), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | R[0,∑i=1nαi+t]​(S)⩽1∑i=1nαi+t\displaystyle R\_{[0,\sum\_{i=1}^{n}\alpha\_{i}+t]}(S)\leqslant\frac{1}{\sum\_{i=1}^{n}\alpha\_{i}+t} | ∑i=1n((1−βi)​R[0,αi]∪[αi+βi,1]​(Xi)−(1−∑i=1nαi−t−βi)​R[αi,αi+βi]​(Xi)).\displaystyle\sum\_{i=1}^{n}\left((1-\beta\_{i})R\_{[0,\alpha\_{i}]\cup[\alpha\_{i}+\beta\_{i},1]}(X\_{i})-\left(1-\sum\_{i=1}^{n}\alpha\_{i}-t-\beta\_{i}\right)R\_{[\alpha\_{i},\alpha\_{i}+\beta\_{i}]}(X\_{i})\right). |  | (3.2) |

By Lemma [1](https://arxiv.org/html/2511.21929v1#Thmlemma1 "Lemma 1 (Propositions 1 and A.1 of Blanchet et al. (2025)). ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we have

|  |  |  |
| --- | --- | --- |
|  | supXi′∼μi,i∈[n],S′=∑i=1nXi′R[r,r+s]​(S′)=supXi∼μir+,i∈[n],S=∑i=1nXiR[0,s1−r]​(S).\sup\_{X\_{i}^{\prime}\sim\mu\_{i},i\in[n],S^{\prime}=\sum\_{i=1}^{n}X\_{i}^{\prime}}R\_{[r,r+s]}(S^{\prime})=\sup\_{X\_{i}\sim\mu\_{i}^{r+},i\in[n],S=\sum\_{i=1}^{n}X\_{i}}R\_{[0,\frac{s}{1-r}]}(S). |  |

Combining the above equation with ([3.2](https://arxiv.org/html/2511.21929v1#S3.E2 "In 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) and letting s1−r=∑i=1nαi+t\frac{s}{1-r}=\sum\_{i=1}^{n}\alpha\_{i}+t, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | supXi′∼μi,i∈[n],S′=∑i=1nXi′R[r,r+s]​(S′)\displaystyle\sup\_{X\_{i}^{\prime}\sim\mu\_{i},i\in[n],S^{\prime}=\sum\_{i=1}^{n}X\_{i}^{\prime}}R\_{[r,r+s]}(S^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽1∑i=1nαi+t​∑i=1n((1−βi)​R[0,αi]∪[αi+βi,1]​(Xi)−(1−∑j=1nαj−t−βi)​R[αi,αi+βi]​(Xi)).\displaystyle\leqslant\frac{1}{\sum\_{i=1}^{n}\alpha\_{i}+t}\sum\_{i=1}^{n}\left((1-\beta\_{i})R\_{[0,\alpha\_{i}]\cup[\alpha\_{i}+\beta\_{i},1]}(X\_{i})-\left(1-\sum\_{j=1}^{n}\alpha\_{j}-t-\beta\_{i}\right)R\_{[\alpha\_{i},\alpha\_{i}+\beta\_{i}]}(X\_{i})\right). |  |

As Xi∼μir+X\_{i}\sim\mu\_{i}^{r+} and Xi′∼μiX\_{i}^{\prime}\sim\mu\_{i}, for any I⊆[0,1]I\subseteq[0,1] being a union of finite many intervals, we have
RI​(Xi)=Rr+(1−r)​I​(Xi′)R\_{I}(X\_{i})=R\_{r+(1-r)I}(X\_{i}^{\prime}) for i∈[n]i\in[n]. Taking αi′=(1−r)​αi\alpha\_{i}^{\prime}=(1-r)\alpha\_{i} and βi′=(1−r)​βi\beta\_{i}^{\prime}=(1-r)\beta\_{i}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | R[r,r+s]​(S′)\displaystyle R\_{[r,r+s]}(S^{\prime}) | ⩽1−r∑i=1nαi′+(1−r)​t∑i=1n((1−βi′1−r)R[r,r+αi′]∪[r+αi′+βi′,1](Xi′)\displaystyle\leqslant\frac{1-r}{\sum\_{i=1}^{n}\alpha\_{i}^{\prime}+(1-r)t}\sum\_{i=1}^{n}\left(\left(1-\frac{\beta\_{i}^{\prime}}{1-r}\right)R\_{[r,r+\alpha\_{i}^{\prime}]\cup[r+\alpha\_{i}^{\prime}+\beta\_{i}^{\prime},1]}(X\_{i}^{\prime})\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(1−t−∑j=1nαj′+βi′1−r)R[r+αi′,r+αi′+βi′](Xi′)).\displaystyle\quad\left.-\left(1-t-\frac{\sum\_{j=1}^{n}\alpha\_{j}^{\prime}+\beta\_{i}^{\prime}}{1-r}\right)R\_{[r+\alpha\_{i}^{\prime},r+\alpha\_{i}^{\prime}+\beta\_{i}^{\prime}]}(X\_{i}^{\prime})\right). |  |

By taking αi′=αi\alpha\_{i}^{\prime}=\alpha\_{i}, βi′=βi\beta\_{i}^{\prime}=\beta\_{i} for i∈[n]i\in[n] and noticing that s=∑i=1nαi′+(1−r)​ts=\sum\_{i=1}^{n}\alpha\_{i}^{\prime}+(1-r)t, the above inequality can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | R[r,r+s]​(ν)⩽∑i=1n[1−r−βis​R[r,r+αi]∪[r+αi+βi,1]​(μi)+(1−1−r−βis)​R[r+αi,r+αi+βi]​(μi)].R\_{[r,r+s]}(\nu)\leqslant\sum\_{i=1}^{n}\left[\frac{1-r-\beta\_{i}}{s}R\_{[r,r+\alpha\_{i}]\cup[r+\alpha\_{i}+\beta\_{i},1]}\left(\mu\_{i}\right)+\left(1-\frac{1-r-\beta\_{i}}{s}\right)R\_{[r+\alpha\_{i},r+\alpha\_{i}+\beta\_{i}]}\left(\mu\_{i}\right)\right]. |  |

We establish the claim for 𝝁∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n} and r>0r>0.

For 𝝁∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} and r>0r>0, suppose Xi∼μi,i∈[n]X\_{i}\sim\mu\_{i},~i\in[n] and let S=∑i=1nXiS=\sum\_{i=1}^{n}X\_{i}. Define Xi(m)=(Xi∧m)∨(−m)X\_{i}^{(m)}=(X\_{i}\wedge m)\vee(-m) and S(m)=∑i=1nXi(m)S^{(m)}=\sum\_{i=1}^{n}X\_{i}^{(m)} for m⩾1m\geqslant 1. Clearly, Xi(m)X\_{i}^{(m)} has a finite mean, and as m→∞m\to\infty, Xi(m)→XiX\_{i}^{(m)}\to X\_{i} and S(m)→SS^{(m)}\to S a.e.. Using the above conclusion, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | R[r,r+s]​(S(m))⩽∑i=1n\displaystyle R\_{[r,r+s]}(S^{(m)})\leqslant\sum\_{i=1}^{n} | [1−r−βisR[r,r+αi]∪[r+αi+βi,1](Xi(m))\displaystyle\left[\frac{1-r-\beta\_{i}}{s}R\_{[r,r+\alpha\_{i}]\cup[r+\alpha\_{i}+\beta\_{i},1]}\left(X\_{i}^{(m)}\right)\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−1−r−βis)R[r+αi,r+αi+βi](Xi(m))].\displaystyle\left.+\left(1-\frac{1-r-\beta\_{i}}{s}\right)R\_{[r+\alpha\_{i},r+\alpha\_{i}+\beta\_{i}]}\left(X\_{i}^{(m)}\right)\right]. |  |

As r>0r>0, letting m→∞m\to\infty and applying the monotone convergence theorem for sufficiently large mm in the above inequality, we establish the claim for 𝝁∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} and r>0r>0.

For the case 𝝁∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n} and r=0r=0, letting r↓0r\downarrow 0 in ([3.1](https://arxiv.org/html/2511.21929v1#S3.E1 "In Theorem 1 (New RVaR Inequality). ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")), we obtain the desired result. This completes the proof.
∎

Note that in ([3.1](https://arxiv.org/html/2511.21929v1#S3.E1 "In Theorem 1 (New RVaR Inequality). ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")), it is possible that some II for RIR\_{I} has a length of zero. The only possible case is αi=0\alpha\_{i}=0 and r+αi+βi=1r+\alpha\_{i}+\beta\_{i}=1, implying the length of [r,r+αi]∪[r+αi+βi,1][r,r+\alpha\_{i}]\cup[r+\alpha\_{i}+\beta\_{i},1] is zero and 1−r−βis=0\frac{1-r-\beta\_{i}}{s}=0. Hence, the value of
1−r−βis​R[r,r+αi]∪[r+αi+βi,1]​(μi)\frac{1-r-\beta\_{i}}{s}R\_{[r,r+\alpha\_{i}]\cup[r+\alpha\_{i}+\beta\_{i},1]}\left(\mu\_{i}\right) is understood as zero.

In Theorem 1 of Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20)), it shows that for α1,…,αn⩾0\alpha\_{1},\dots,\alpha\_{n}\geqslant 0 and β1,…,βn>0\beta\_{1},\dots,\beta\_{n}>0 satisfying ∑i=1nαi+⋁i=1nβi<1\sum\_{i=1}^{n}\alpha\_{i}+\bigvee\_{i=1}^{n}\beta\_{i}<1, 𝝁∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} and ν∈Λ​(𝝁)\nu\in\Lambda(\boldsymbol{\mu}), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | R[r,r+s]​(ν)⩽∑i=1nR[1−αi−βi,1−αi]​(μi),R\_{[r,r+s]}(\nu)\leqslant\sum\_{i=1}^{n}R\_{[1-\alpha\_{i}-\beta\_{i},1-\alpha\_{i}]}\left(\mu\_{i}\right), |  | (3.3) |

where r+s=1−∑i=1nαir+s=1-\sum\_{i=1}^{n}\alpha\_{i} and s=⋁i=1nβis=\bigvee\_{i=1}^{n}\beta\_{i}.
Clearly, the individual and aggregate risk measures in ([3.3](https://arxiv.org/html/2511.21929v1#S3.E3 "In 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) are all RVaR\mathrm{RVaR}. However, the individual risk measures in the new RVaR\mathrm{RVaR} inequality in ([3.1](https://arxiv.org/html/2511.21929v1#S3.E1 "In Theorem 1 (New RVaR Inequality). ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) are more complicated, involving the linear combinations of RIR\_{I} with II being a union of two intervals. The aggregate risk measure still has the form of RVaR\mathrm{RVaR}. This new RVaR\mathrm{RVaR} inequality helps establish new risk aggregation bounds and sharpness conditions. It is also very useful to investigate risk sharing for different distortion risk measures with more complex distortion functions than that of Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20)).

Further, by setting 1−r−βi=s1-r-\beta\_{i}=s for the bound in Theorem [1](https://arxiv.org/html/2511.21929v1#Thmtheorem1 "Theorem 1 (New RVaR Inequality). ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we immediately arrive at a simplified upper bound displayed in the following corollary.

###### Corollary 1.

Let 0<r<r+s⩽10<r<r+s\leqslant 1 and α1,…,αn∈(0,1−r)\alpha\_{1},\dots,\alpha\_{n}\in(0,1-r) with ∑i=1nαi=s\sum\_{i=1}^{n}\alpha\_{i}=s.
Then for 𝛍∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} and ν∈Λ​(𝛍)\nu\in\Lambda(\boldsymbol{\mu}), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | R[r,r+s]​(ν)⩽∑i=1nR[r,r+αi]∪[1−s+αi,1]​(μi).R\_{[r,r+s]}(\nu)\leqslant\sum\_{i=1}^{n}R\_{[r,r+\alpha\_{i}]\cup[1-s+\alpha\_{i},1]}(\mu\_{i}). |  | (3.4) |

Moreover, ([3.4](https://arxiv.org/html/2511.21929v1#S3.E4 "In Corollary 1. ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) holds for r=0r=0 if 𝛍∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n}.

By setting r=0r=0, Corollary [1](https://arxiv.org/html/2511.21929v1#Thmcorollary1 "Corollary 1. ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") states that the lower tail of the aggregate risk can be controlled by the summation of the lower tail and the upper tail of the individual risks.
Later, we will see that the inequality in Corollary [1](https://arxiv.org/html/2511.21929v1#Thmcorollary1 "Corollary 1. ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") plays a crucial role to solve the risk sharing problem in Section [5](https://arxiv.org/html/2511.21929v1#S5 "5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing").

## 4 Extended Convolution Bounds

In this section, we obtain some bounds for the risk aggregation with dependence uncertainty for RVaR\mathrm{RVaR}, the difference between two RVaR\mathrm{RVaR}, and the difference between two quantiles. The bound for RVaR\mathrm{RVaR} is a complement to the results in Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)) by providing a different form and more sharpness results. The bounds for the difference between two RVaR\mathrm{RVaR} and the difference between two quantiles are new to the literature. We call those bounds extended convolution bounds.

### 4.1 RVaR Aggregation Upper and Lower Bounds

###### Theorem 2 (RVaR aggregation upper bound).

For either 𝛍∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} and 0<r<r+s⩽10<r<r+s\leqslant 1, or 𝛍∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n} and 0⩽r<r+s⩽10\leqslant r<r+s\leqslant 1, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supν∈Λ​(𝝁)R[r,r+s](ν)⩽inf𝜷∈(1−r)​Δnβ0⩾1−r−s{\displaystyle\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}R\_{[r,r+s]}(\nu)\leqslant\inf\_{\begin{subarray}{c}\boldsymbol{\beta}\in(1-r)\Delta\_{n}\\ \beta\_{0}\geqslant 1-r-s\end{subarray}}\bigg\{ | (1−1−r−β0s)​∑i=1nR[r+βi,r+βi+β0]​(μi)\displaystyle\left(1-\frac{1-r-\beta\_{0}}{s}\right)\sum\_{i=1}^{n}R\_{[r+\beta\_{i},r+\beta\_{i}+\beta\_{0}]}(\mu\_{i}) |  | (4.1) |
|  |  | +1−r−β0s∑i=1nR[r,r+βi]∪[r+βi+β0,1](μi)}.\displaystyle\quad\quad+\frac{1-r-\beta\_{0}}{s}\sum\_{i=1}^{n}R\_{[r,r+\beta\_{i}]\cup[r+\beta\_{i}+\beta\_{0},1]}(\mu\_{i})\bigg\}. |  |

Moreover, ([4.1](https://arxiv.org/html/2511.21929v1#S4.E1 "In Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) holds as an equality for 𝛍∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n} in the following cases:

1. (i)

   each of μ1,…,μn\mu\_{1},\dots,\mu\_{n} admits an increasing density beyond its rr-quantile;
2. (ii)

   ∑i=1nμi​[qr+​(μi),q1−​(μi))⩽1−r\sum\_{i=1}^{n}\mu\_{i}\left[q\_{r}^{+}(\mu\_{i}),q\_{1}^{-}(\mu\_{i})\right)\leqslant 1-r.

###### Proof.

In light of ([3.1](https://arxiv.org/html/2511.21929v1#S3.E1 "In Theorem 1 (New RVaR Inequality). ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) and using the assumption ∑i=1nαi+⋁i=1nβi=1−r\sum\_{i=1}^{n}\alpha\_{i}+\bigvee\_{i=1}^{n}\beta\_{i}=1-r and the transformations βi→β0,i∈[n]\beta\_{i}\to\beta\_{0},~i\in[n], αi→βi,i∈[n]\alpha\_{i}\to\beta\_{i},~i\in[n], we have, for 𝜷∈(1−r)​Δn\boldsymbol{\beta}\in(1-r)\Delta\_{n} and β0⩾1−r−s\beta\_{0}\geqslant 1-r-s,

|  |  |  |
| --- | --- | --- |
|  | R[r,r+s]​(ν)⩽(1−1−r−β0s)​∑i=1nR[r+βi,r+βi+β0]​(μi)+1−r−β0s​∑i=1nR[r,r+βi]∪[r+βi+β0,1]​(μi).R\_{[r,r+s]}(\nu)\leqslant\left(1-\frac{1-r-\beta\_{0}}{s}\right)\sum\_{i=1}^{n}R\_{[r+\beta\_{i},r+\beta\_{i}+\beta\_{0}]}(\mu\_{i})+\frac{1-r-\beta\_{0}}{s}\sum\_{i=1}^{n}R\_{[r,r+\beta\_{i}]\cup[r+\beta\_{i}+\beta\_{0},1]}(\mu\_{i}). |  |

We obtain ([4.1](https://arxiv.org/html/2511.21929v1#S4.E1 "In Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) by taking the supremum on the left-hand side of the above inequality over ν∈Λ​(𝝁)\nu\in\Lambda(\boldsymbol{\mu}) and infimum on the right-hand side of the above inequality over 𝜷∈(1−r)​Δn\boldsymbol{\beta}\in(1-r)\Delta\_{n} and β0⩾1−r−s\beta\_{0}\geqslant 1-r-s.

Next, we show that ([4.1](https://arxiv.org/html/2511.21929v1#S4.E1 "In Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) is an equality for cases (i) and (ii). If case (i) holds, then each of μ1r+,…,μnr+\mu\_{1}^{r+},\dots,\mu\_{n}^{r+} admits an increasing density. Define (Equation (3.4) in Jakobsons et al. ([2016](https://arxiv.org/html/2511.21929v1#bib.bib33)))

|  |  |  |
| --- | --- | --- |
|  | Tsn=h​(U)​𝟙{U<sn}+d​(sn)​𝟙{U>sn},T\_{s\_{n}}=h(U)\mathds{1}\_{\{U<s\_{n}\}}+d(s\_{n})\mathds{1}\_{\{U>s\_{n}\}}, |  |

where U∼U​[0,1]U\sim\mathrm{U}[0,1], h​(x)=∑i=1nyi​(x)−(n−1)​y​(x)h(x)=\sum\_{i=1}^{n}y\_{i}(x)-(n-1)y(x), d​(x)=−11−x​∫−yi​(x)y​(x)−yi​(x)z​μir+​(d​z)d(x)=-\frac{1}{1-x}\int^{y(x)-y\_{i}(x)}\_{-y\_{i}(x)}z\mu\_{i}^{r+}(\mathrm{d}z) for x∈(0,1)x\in(0,1), and sn=inf{x∈(0,1):h​(x)⩽d​(x)}s\_{n}=\inf\{x\in(0,1):h(x)\leqslant d(x)\} with y,yi,i∈[n]y,y\_{i},~i\in[n] being the continuous functions on (0,1)(0,1) satisfying

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nμir+​(−∞,−yi​(x))=x,and​μir+​[−yi​(x),y​(x)−yi​(x))=1−x,x∈(0,1).\sum\_{i=1}^{n}\mu\_{i}^{r+}(-\infty,-y\_{i}(x))=x,~~\text{and}~~\mu\_{i}^{r+}[-y\_{i}(x),y(x)-y\_{i}(x))=1-x,~x\in(0,1). |  |

In light of Lemma 3.4 of Jakobsons et al. ([2016](https://arxiv.org/html/2511.21929v1#bib.bib33)) and using the fact that each of μ1r+,…,μnr+\mu\_{1}^{r+},\dots,\mu\_{n}^{r+} admits an increasing density, there exist Xi∼μir+X\_{i}\sim\mu\_{i}^{r+} such that Tsn=∑i=1n−XiT\_{s\_{n}}=\sum\_{i=1}^{n}-X\_{i}. Moreover, using Lemma 3.3 of Jakobsons et al. ([2016](https://arxiv.org/html/2511.21929v1#bib.bib33)), we could find 𝜷′∈Δn\boldsymbol{\beta}^{\prime}\in\Delta\_{n} with β0′⩾1−s1−r\beta\_{0}^{\prime}\geqslant 1-\frac{s}{1-r} such that

|  |  |  |
| --- | --- | --- |
|  | R[0,1−s/(1−r)]​(−S)=∑i=1nR[1−βi′−β0′,1−βi′]​(−Xi)\displaystyle R\_{[0,1-s/(1-r)]}(-S)=\sum\_{i=1}^{n}R\_{[1-\beta\_{i}^{\prime}-\beta\_{0}^{\prime},1-\beta\_{i}^{\prime}]}(-X\_{i}) |  |

with S=∑i=1nXiS=\sum\_{i=1}^{n}X\_{i}. The detail of construction of such 𝜷′\boldsymbol{\beta}^{\prime} and β0′\beta\_{0}^{\prime} is omitted as it is only involving tedious computation using Lemma 3.3 of Jakobsons et al. ([2016](https://arxiv.org/html/2511.21929v1#bib.bib33)). One can refer to the proof of Theorem 1 of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)) for the similar computation.
Note that the above equation can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | R[s/(1−r),1]​(S)=∑i=1nR[βi′,βi′+β0′]​(Xi).\displaystyle R\_{[s/(1-r),1]}(S)=\sum\_{i=1}^{n}R\_{[\beta\_{i}^{\prime},\beta\_{i}^{\prime}+\beta\_{0}^{\prime}]}(X\_{i}). |  |

Using the fact

|  |  |  |
| --- | --- | --- |
|  | 𝔼​(S)=s1−r​R[0,s/(1−r)]​(S)+1−r−s1−r​R[s/(1−r),1]​(S),\mathbb{E}(S)=\frac{s}{1-r}R\_{[0,s/(1-r)]}(S)+\frac{1-r-s}{1-r}R\_{[s/(1-r),1]}(S), |  |

we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | R[0,s/(1−r)]​(S)\displaystyle R\_{[0,s/(1-r)]}(S) | =1−rs​(𝔼​(S)−1−r−s1−r​∑i=1nR[βi′,βi′+β0′]​(Xi))\displaystyle=\frac{1-r}{s}\left(\mathbb{E}(S)-\frac{1-r-s}{1-r}\sum\_{i=1}^{n}R\_{[\beta\_{i}^{\prime},\beta\_{i}^{\prime}+\beta\_{0}^{\prime}]}(X\_{i})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1−rs​∑i=1n((1−β0′)​R[0,βi′]∪[βi′+β0′,1]​(Xi)+(β0′−1−r−s1−r)​∑i=1nR[βi′,βi′+β0′]​(Xi)).\displaystyle=\frac{1-r}{s}\sum\_{i=1}^{n}\left((1-\beta\_{0}^{\prime})R\_{[0,\beta\_{i}^{\prime}]\cup[\beta\_{i}^{\prime}+\beta\_{0}^{\prime},1]}(X\_{i})+\left(\beta\_{0}^{\prime}-\frac{1-r-s}{1-r}\right)\sum\_{i=1}^{n}R\_{[\beta\_{i}^{\prime},\beta\_{i}^{\prime}+\beta\_{0}^{\prime}]}(X\_{i})\right). |  |

There exist U′∼U​[0,1]U^{\prime}\sim\mathrm{U}[0,1] and (Y1,…,Yn)(Y\_{1},\dots,Y\_{n}) such that (Y1,…,Yn)(Y\_{1},\dots,Y\_{n}) is independent of U′U^{\prime} and has the same distribution as (X1,…,Xn)(X\_{1},\dots,X\_{n}). Define

|  |  |  |
| --- | --- | --- |
|  | Xi′=Yi​𝟙{U′>r}+qU′−​(μi)​𝟙{U′<r},i∈[n],and​S′=∑i=1nXi′.X\_{i}^{\prime}=Y\_{i}\mathds{1}\_{\{U^{\prime}>r\}}+q\_{U^{\prime}}^{-}(\mu\_{i})\mathds{1}\_{\{U^{\prime}<r\}},~i\in[n],~\text{and}~S^{\prime}=\sum\_{i=1}^{n}X\_{i}^{\prime}. |  |

Clearly, Xi′∼μiX\_{i}^{\prime}\sim\mu\_{i} and S′=(∑i=1nYi)​𝟙{U′>r}+(∑i=1nqU′−​(μi))​𝟙{U′<r}S^{\prime}=(\sum\_{i=1}^{n}Y\_{i})\mathds{1}\_{\{U^{\prime}>r\}}+(\sum\_{i=1}^{n}q\_{U^{\prime}}^{-}(\mu\_{i}))\mathds{1}\_{\{U^{\prime}<r\}}. Note that R[r,s]​(S′)=R[0,s/(1−r)]​(S)R\_{[r,s]}(S^{\prime})=R\_{[0,s/(1-r)]}(S). Letting β0=(1−r)​β0′\beta\_{0}=(1-r)\beta\_{0}^{\prime} and βi=(1−r)​βi′,i∈[n]\beta\_{i}=(1-r)\beta\_{i}^{\prime},~i\in[n], we have 𝜷∈(1−r)​Δn\boldsymbol{\beta}\in(1-r)\Delta\_{n}, β0⩾1−r−s\beta\_{0}\geqslant 1-r-s and

|  |  |  |  |
| --- | --- | --- | --- |
|  | R[r,s]​(S′)\displaystyle R\_{[r,s]}(S^{\prime}) | =1−rs​∑i=1n((1−β01−r)​R[r,r+βi]∪[r+βi+β0,1]​(Xi′)+(β01−r−1−r−s1−r)​∑i=1nR[r+βi,r+βi+β0]​(Xi′))\displaystyle=\frac{1-r}{s}\sum\_{i=1}^{n}\left(\left(1-\frac{\beta\_{0}}{1-r}\right)R\_{[r,r+\beta\_{i}]\cup[r+\beta\_{i}+\beta\_{0},1]}(X\_{i}^{\prime})+\left(\frac{\beta\_{0}}{1-r}-\frac{1-r-s}{1-r}\right)\sum\_{i=1}^{n}R\_{[r+\beta\_{i},r+\beta\_{i}+\beta\_{0}]}(X\_{i}^{\prime})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−1−r−β0s)​∑i=1nR[r+βi,r+βi+β0]​(μi)+1−r−β0s​∑i=1nR[r,r+βi]∪[r+βi+β0,1]​(μi),\displaystyle=\left(1-\frac{1-r-\beta\_{0}}{s}\right)\sum\_{i=1}^{n}R\_{[r+\beta\_{i},r+\beta\_{i}+\beta\_{0}]}(\mu\_{i})+\frac{1-r-\beta\_{0}}{s}\sum\_{i=1}^{n}R\_{[r,r+\beta\_{i}]\cup[r+\beta\_{i}+\beta\_{0},1]}(\mu\_{i}), |  |

implying the inverse inequality of ([4.1](https://arxiv.org/html/2511.21929v1#S4.E1 "In Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")). Hence, ([4.1](https://arxiv.org/html/2511.21929v1#S4.E1 "In Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) holds as an equality.

If case (ii) holds, then ∑i=1nμir+​[q0+​(μir+),q1−​(μir+))⩽1\sum\_{i=1}^{n}\mu\_{i}^{r+}\left[q\_{0}^{+}(\mu\_{i}^{r+}),q\_{1}^{-}(\mu\_{i}^{r+})\right)\leqslant 1. Hence, there exist Xi∼μir+,i∈[n]X\_{i}\sim\mu\_{i}^{r+},~i\in[n] such that −Xi,i∈[n]-X\_{i},~i\in[n] are lower mutually exclusive. Hence, in light of Lemma EC.2 of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)), there exist Xi∼μir+X\_{i}\sim\mu\_{i}^{r+} and 𝜷′∈Δn\boldsymbol{\beta}^{\prime}\in\Delta\_{n}, β0′⩾1−s1−r\beta\_{0}^{\prime}\geqslant 1-\frac{s}{1-r} such that

|  |  |  |
| --- | --- | --- |
|  | R[0,1−s/(1−r)]​(−S)=∑i=1nR[1−βi′−β0′,1−βi′]​(−Xi)\displaystyle R\_{[0,1-s/(1-r)]}(-S)=\sum\_{i=1}^{n}R\_{[1-\beta\_{i}^{\prime}-\beta\_{0}^{\prime},1-\beta\_{i}^{\prime}]}(-X\_{i}) |  |

with S=∑i=1nXiS=\sum\_{i=1}^{n}X\_{i}. Repeating the procedure in the proof of case (i), we can show that ([4.1](https://arxiv.org/html/2511.21929v1#S4.E1 "In Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) holds as an equality.
∎

As a comparison, Theorem 1 of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)) gives the following (upper) convolution bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | supν∈Λ​(𝝁)R[r,r+s]​(ν)⩽inf𝜷∈(1−r)​Δnβ0⩾s∑i=1nR[1−βi−β0,1−βi]​(μi).\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}R\_{[r,r+s]}(\nu)\leqslant\inf\_{\begin{subarray}{c}\boldsymbol{\beta}\in(1-r)\Delta\_{n}\\ \beta\_{0}\geqslant s\end{subarray}}\sum\_{i=1}^{n}R\_{[1-\beta\_{i}-\beta\_{0},1-\beta\_{i}]}(\mu\_{i}). |  | (4.2) |

As stated in Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)), the bound ([4.2](https://arxiv.org/html/2511.21929v1#S4.E2 "In 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) is sharp if each of μ1,…,μn\mu\_{1},\dots,\mu\_{n} admits a decreasing density beyond its rr-quantile. However, it is not clear whether it is still sharp if each of μ1,…,μn\mu\_{1},\dots,\mu\_{n} admits an increasing density beyond its rr-quantile. Our Theorem [2](https://arxiv.org/html/2511.21929v1#Thmtheorem2 "Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") complements the result in Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)) by offering some new bound which is sharp for the case of marginals with increasing densities on their upper-tail parts. In practice, although most of the distributions have decreasing densities on their upper-tail parts, some distributions with increasing densities on the upper-tail parts still exist such as Beta distribution or triangular distribution. Moreover, the result in Theorem [2](https://arxiv.org/html/2511.21929v1#Thmtheorem2 "Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") is crucial to find the sharp bound for the best-case scenario when the marginals have decreasing densities; see Theorem [3](https://arxiv.org/html/2511.21929v1#Thmtheorem3 "Theorem 3 (RVaR aggregation lower bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") below.

Before proceeding to the lower bound, we first
obtain a simplified sharp bound if the marginal distributions are homogeneous. For μ∈ℳ\mu\in\mathcal{M}, let

|  |  |  |
| --- | --- | --- |
|  | cn​(μ)=inf{x∈(0,1n):(n−1)​q(n−1)​x−​(μ)+q1−x−​(μ)n⩽R[(n−1)​x,1−x]​(μ)}c\_{n}(\mu)=\inf\left\{x\in\left(0,\frac{1}{n}\right):\frac{(n-1)q\_{(n-1)x}^{-}(\mu)+q\_{1-x}^{-}(\mu)}{n}\leqslant R\_{[(n-1)x,1-x]}(\mu)\right\} |  |

with the convention that inf∅=1/n\inf\emptyset=1/n.

###### Proposition 1 (RVaR aggregation upper bound: homogeneous marginal).

If μ∈ℳ\mu\in\mathcal{M} has an increasing density on its support, and 0<r<r+s⩽10<r<r+s\leqslant 1 with s1−r⩽n​cn​(μ)\frac{s}{1-r}\leqslant nc\_{n}(\mu), then we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supν∈Λn​(μ)R[r,r+s]​(ν)\displaystyle\sup\_{\nu\in\Lambda\_{n}(\mu)}R\_{[r,r+s]}(\nu) | =n​R[r,r+sn]∪[1−s+sn,1]​(μ).\displaystyle=nR\_{[r,r+\frac{s}{n}]\cup[1-s+\frac{s}{n},1]}(\mu). |  | (4.3) |

###### Proof.

Suppose μ1=⋯=μn=μ\mu\_{1}=\dots=\mu\_{n}=\mu, which has an increasing density on its support. Denote by μ~\tilde{\mu} the distribution measure of −Xi-X\_{i}, where Xi∼μX\_{i}\sim\mu. Hence, μ~\tilde{\mu} has a decreasing density. Denote by ν~\tilde{\nu} the distribution measure of −∑i=1nXi-\sum\_{i=1}^{n}X\_{i}, where ∑i=1nXi∼ν\sum\_{i=1}^{n}X\_{i}\sim\nu. For 0⩽r<r+s⩽10\leqslant r<r+s\leqslant 1, write t=1−r−st=1-r-s. Using Lemma [1](https://arxiv.org/html/2511.21929v1#Thmlemma1 "Lemma 1 (Propositions 1 and A.1 of Blanchet et al. (2025)). ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | supν∈Λn​(μ)R[r,r+s]​(ν)=−infν~∈Λn​(μ~)R[1−r−s,1−r]​(ν~)=−infν~∈Λn​(μ~(t+s)−)ESst+s​(ν~).\displaystyle\sup\_{\nu\in\Lambda\_{n}(\mu)}R\_{[r,r+s]}(\nu)=-\inf\_{\tilde{\nu}\in\Lambda\_{n}(\tilde{\mu})}R\_{[1-r-s,1-r]}(\tilde{\nu})=-\inf\_{\tilde{\nu}\in\Lambda\_{n}(\tilde{\mu}^{(t+s)-})}\mathrm{ES}\_{\frac{s}{t+s}}(\tilde{\nu}). |  | (4.4) |

Note that μ~(t+s)−\tilde{\mu}^{(t+s)-} has a decreasing density on its support.
Hence, by Theorem 5.2 of Bernard et al. ([2014](https://arxiv.org/html/2511.21929v1#bib.bib6)), we have for any p∈(0,n​cn​(μ)]p\in(0,nc\_{n}(\mu)],

|  |  |  |  |
| --- | --- | --- | --- |
|  | infν∈Λn​(μ)ESp​(ν)=np​∫0pn((n−1)​q(n−1)​u−​(μ)+q1−u−​(μ))​du.\inf\_{\nu\in\Lambda\_{n}(\mu)}\mathrm{ES}\_{p}(\nu)=\frac{n}{p}\int\_{0}^{\frac{p}{n}}\left((n-1)q\_{(n-1)u}^{-}(\mu)+q\_{1-u}^{-}(\mu)\right)\mathrm{d}u. |  | (4.5) |

Using ([4.5](https://arxiv.org/html/2511.21929v1#S4.E5 "In 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")), for st+s⩽n​cn​(μ)\frac{s}{t+s}\leqslant nc\_{n}(\mu), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −infν~∈Λn​(μ~(t+s)−)ESst+s​(ν~)\displaystyle-\inf\_{\tilde{\nu}\in\Lambda\_{n}(\tilde{\mu}^{(t+s)-})}\mathrm{ES}\_{\frac{s}{t+s}}(\tilde{\nu}) | =−n​(t+s)s​∫0sn​(t+s)((n−1)​q(n−1)​u−​(μ~(t+s)−)+q1−u−​(μ~(t+s)−))​du\displaystyle=-\frac{n(t+s)}{s}\int\_{0}^{\frac{s}{n(t+s)}}\left((n-1)q\_{(n-1)u}^{-}(\tilde{\mu}^{(t+s)-})+q\_{1-u}^{-}(\tilde{\mu}^{(t+s)-})\right)\mathrm{d}u |  | (4.6) |
|  |  | =−n​(t+s)s​∫0sn​(t+s)((n−1)​q(n−1)​(t+s)​u−​(μ~)+q(1−u)​(t+s)−​(μ~))​du\displaystyle=-\frac{n(t+s)}{s}\int\_{0}^{\frac{s}{n(t+s)}}\left((n-1)q\_{(n-1)(t+s)u}^{-}(\tilde{\mu})+q\_{(1-u)(t+s)}^{-}(\tilde{\mu})\right)\mathrm{d}u |  |
|  |  | =−n​(t+s)s​(∫0(n−1)n​s1t+s​qv−​(μ~)​dv+∫t+s−snt+s1t+s​qv−​(μ~)​dv)\displaystyle=-\frac{n(t+s)}{s}\left(\int\_{0}^{\frac{(n-1)}{n}s}\frac{1}{t+s}q\_{v}^{-}(\tilde{\mu})\mathrm{d}v+\int\_{t+s-\frac{s}{n}}^{t+s}\frac{1}{t+s}q\_{v}^{-}(\tilde{\mu})\mathrm{d}v\right) |  |
|  |  | =−ns​(∫0(n−1)n​sqv−​(μ~)​dv+∫t+s−snt+sqv−​(μ~)​dv)\displaystyle=-\frac{n}{s}\left(\int\_{0}^{\frac{(n-1)}{n}s}q\_{v}^{-}(\tilde{\mu})\mathrm{d}v+\int\_{t+s-\frac{s}{n}}^{t+s}q\_{v}^{-}(\tilde{\mu})\mathrm{d}v\right) |  |
|  |  | =ns​(∫1−t−s1−t−s+snqv−​(μ)​dv+∫1−(n−1)n​s1qv−​(μ)​dv)\displaystyle=\frac{n}{s}\left(\int\_{1-t-s}^{1-t-s+\frac{s}{n}}q\_{v}^{-}(\mu)\mathrm{d}v+\int\_{1-\frac{(n-1)}{n}s}^{1}q\_{v}^{-}(\mu)\mathrm{d}v\right) |  |
|  |  | =n​R[r,r+sn]∪[1−s+sn,1]​(μ).\displaystyle=nR\_{[r,r+\frac{s}{n}]\cup[1-s+\frac{s}{n},1]}(\mu). |  |

Combining ([4.4](https://arxiv.org/html/2511.21929v1#S4.E4 "In 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) and ([4.6](https://arxiv.org/html/2511.21929v1#S4.E6 "In 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")), we have ([4.3](https://arxiv.org/html/2511.21929v1#S4.E3 "In Proposition 1 (RVaR aggregation upper bound: homogeneous marginal). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")).
∎

Based on the result in Theorem [2](https://arxiv.org/html/2511.21929v1#Thmtheorem2 "Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we immediately obtain a lower bound for the risk aggregation of RVaR\mathrm{RVaR} with fixed marginal distributions but unknown dependence structure.

###### Theorem 3 (RVaR\mathrm{RVaR} aggregation lower bound).

For either 𝛍∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} and 0⩽r<r+s<10\leqslant r<r+s<1, or 𝛍∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n} and 0⩽r<r+s⩽10\leqslant r<r+s\leqslant 1, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | infν∈Λ​(𝝁)R[r,r+s](ν)⩾sup𝜷∈(r+s)​Δnβ0⩾r{\displaystyle\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}R\_{[r,r+s]}(\nu)\geqslant\sup\_{\begin{subarray}{c}\boldsymbol{\beta}\in(r+s)\Delta\_{n}\\ \beta\_{0}\geqslant r\end{subarray}}\bigg\{ | (1−r+s−β0s)​∑i=1nR[r+s−βi−β0,r+s−βi]​(μi)\displaystyle\left(1-\frac{r+s-\beta\_{0}}{s}\right)\sum\_{i=1}^{n}R\_{[r+s-\beta\_{i}-\beta\_{0},r+s-\beta\_{i}]}(\mu\_{i}) |  | (4.7) |
|  |  | +r+s−β0s∑i=1nR[0,r+s−βi−β0]∪[r+s−βi,r+s](μi)}.\displaystyle+\frac{r+s-\beta\_{0}}{s}\sum\_{i=1}^{n}R\_{[0,r+s-\beta\_{i}-\beta\_{0}]\cup[r+s-\beta\_{i},r+s]}(\mu\_{i})\bigg\}. |  |

Moreover, ([4.7](https://arxiv.org/html/2511.21929v1#S4.E7 "In Theorem 3 (RVaR aggregation lower bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) holds as an equality for 𝛍∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n} in the following cases:

1. (i)

   each of μ1,…,μn\mu\_{1},\dots,\mu\_{n} admits a decreasing density below its (r+s)(r+s)-quantile;
2. (ii)

   ∑i=1nμi​(q0+​(μi),qr+s−​(μi)]⩽r+s\sum\_{i=1}^{n}\mu\_{i}\left(q\_{0}^{+}(\mu\_{i}),q\_{r+s}^{-}(\mu\_{i})\right]\leqslant r+s.

###### Proof.

Denote by μ~i\tilde{\mu}\_{i} the distribution measure of −Xi-X\_{i}, where Xi∼μiX\_{i}\sim\mu\_{i}, and by ν~\tilde{\nu} the distribution measure of −∑i=1nXi-\sum\_{i=1}^{n}X\_{i}, where ∑i=1nXi∼ν\sum\_{i=1}^{n}X\_{i}\sim\nu. Then we have

|  |  |  |
| --- | --- | --- |
|  | infν∈Λ​(𝝁)R[r,r+s]​(ν)=−supν~∈Λ​(𝝁~)R[1−r−s,1−r]​(ν~).\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}R\_{[r,r+s]}(\nu)=-\sup\_{\tilde{\nu}\in\Lambda(\tilde{\boldsymbol{\mu}})}R\_{[1-r-s,1-r]}(\tilde{\nu}). |  |

Applying Theorem [2](https://arxiv.org/html/2511.21929v1#Thmtheorem2 "Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we immediately establish the claim.
∎

It is worth mentioning that Theorem A.1 of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)) gives the following (lower) convolution bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | infν∈Λ​(𝝁)R[r,r+s]​(ν)⩾sup𝜷∈(r+s)​Δnβ0⩾s∑i=1nR[βi,βi+β0]​(μi).\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}R\_{[r,r+s]}(\nu)\geqslant\sup\_{\begin{subarray}{c}\boldsymbol{\beta}\in(r+s)\Delta\_{n}\\ \beta\_{0}\geqslant s\end{subarray}}\sum\_{i=1}^{n}R\_{[\beta\_{i},\beta\_{i}+\beta\_{0}]}(\mu\_{i}). |  | (4.8) |

It is shown in Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)) that ([4.8](https://arxiv.org/html/2511.21929v1#S4.E8 "In 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) is a sharp bound if each marginal distribution admits an increasing density below its (r+sr+s)-quantile. However, it is not clear whether the bound is sharp for the case with decreasing densities on the lower-tail parts. Our Theorem [3](https://arxiv.org/html/2511.21929v1#Thmtheorem3 "Theorem 3 (RVaR aggregation lower bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") fills in this gap by providing a bound which is sharp for the best case of RVaR\mathrm{RVaR} if all marginal distributions admit decreasing densities on their lower-tail parts. This gap is actually significant because many commonly used distributions in finance and risk management have decreasing densities on their lower-tail parts, including exponential, Pareto, and some gamma and chi distributions. It is reasonable to expect that the bounds in Theorems [2](https://arxiv.org/html/2511.21929v1#Thmtheorem2 "Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") and [3](https://arxiv.org/html/2511.21929v1#Thmtheorem3 "Theorem 3 (RVaR aggregation lower bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") approximate the exact values whenever the marginals are close to satisfying the sharpness conditions. Moreover, our results in Theorems [2](https://arxiv.org/html/2511.21929v1#Thmtheorem2 "Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") and [3](https://arxiv.org/html/2511.21929v1#Thmtheorem3 "Theorem 3 (RVaR aggregation lower bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") are the building blocks to consider the worst case value of the difference between two RVaR\mathrm{RVaR} in Section [4.2](https://arxiv.org/html/2511.21929v1#S4.SS2 "4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing").

Applying Proposition [1](https://arxiv.org/html/2511.21929v1#Thmproposition1 "Proposition 1 (RVaR aggregation upper bound: homogeneous marginal). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we immediately obtain a simplified sharp lower bound if the marginal distributions are homogeneous as below. For μ∈ℳ\mu\in\mathcal{M}, we denote by μ~\tilde{\mu} the distribution measure of −X-X with X∼μX\sim\mu.

###### Proposition 2 (RVaR aggregation lower bound: homogeneous marginal).

If μ∈ℳ\mu\in\mathcal{M} has a decreasing density on its support, and 0⩽r<r+s<10\leqslant r<r+s<1 with sr+s⩽n​cn​(μ~)\frac{s}{r+s}\leqslant nc\_{n}(\tilde{\mu}), then we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | infν∈Λn​(μ)R[r,r+s]​(ν)\displaystyle\inf\_{\nu\in\Lambda\_{n}(\mu)}R\_{[r,r+s]}(\nu) | =n​R[0,(n−1)​sn]∪[r+(n−1)​sn,r+s]​(μ).\displaystyle=nR\_{[0,\frac{(n-1)s}{n}]\cup[r+\frac{(n-1)s}{n},r+s]}(\mu). |  |

### 4.2 Inter-RVaR Difference Aggregation Upper Bounds

For 0⩽r1<s1⩽r2<s2⩽10\leqslant r\_{1}<s\_{1}\leqslant r\_{2}<s\_{2}\leqslant 1, the inter-RVaR\mathrm{RVaR} difference is defined as

|  |  |  |
| --- | --- | --- |
|  | IRD[r1,s1],[r2,s2]​(μ)=R[r2,s2]​(μ)−R[r1,s1]​(μ),\mathrm{IRD}\_{[r\_{1},s\_{1}],[r\_{2},s\_{2}]}(\mu)=R\_{[r\_{2},s\_{2}]}(\mu)-R\_{[r\_{1},s\_{1}]}(\mu), |  |

which can be viewed as an example of the variability measures introduced in Bellini et al. ([2022](https://arxiv.org/html/2511.21929v1#bib.bib5)).
If r1=1−s2=0r\_{1}=1-s\_{2}=0 and s1=1−r2s\_{1}=1-r\_{2}, then IRD[r1,s1],[r2,s2]​(μ)=ES1−r2​(μ)−LES1−r2​(μ)\mathrm{IRD}\_{[r\_{1},s\_{1}],[r\_{2},s\_{2}]}(\mu)=\mathrm{ES}\_{1-r\_{2}}(\mu)-\mathrm{LES}\_{1-r\_{2}}(\mu), which is the inter-ES\mathrm{ES} difference introduced by Bellini et al. ([2022](https://arxiv.org/html/2511.21929v1#bib.bib5)). If s2↓r2=1−rs\_{2}\downarrow r\_{2}=1-r and r1↑s1=rr\_{1}\uparrow s\_{1}=r, then IRD[r1,s1],[r2,s2]\mathrm{IRD}\_{[r\_{1},s\_{1}],[r\_{2},s\_{2}]} converges to the inter-quantile difference

|  |  |  |
| --- | --- | --- |
|  | IQDr+​(μ)=q1−r+​(μ)−qr−​(μ),r∈(0,12],\mathrm{IQD}\_{r}^{+}(\mu)=q\_{1-r}^{+}(\mu)-q\_{r}^{-}(\mu),~r\in\left(0,\frac{1}{2}\right], |  |

which was given by Bellini et al. ([2022](https://arxiv.org/html/2511.21929v1#bib.bib5)). An alternative definition of inter-quantile difference was introduced by Lauzier et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib38)) in the study of risk sharing, i.e.,

|  |  |  |
| --- | --- | --- |
|  | IQDr−​(μ)=q1−r−​(μ)−qr+​(μ),r∈[0,12),\mathrm{IQD}\_{r}^{-}(\mu)=q\_{1-r}^{-}(\mu)-q\_{r}^{+}(\mu),~r\in\left[0,\frac{1}{2}\right), |  |

which is the limit of IRD[r1,s1],[r2,s2]​(μ)\mathrm{IRD}\_{[r\_{1},s\_{1}],[r\_{2},s\_{2}]}(\mu) as r2↑s2=1−rr\_{2}\uparrow s\_{2}=1-r and s1↓r1=rs\_{1}\downarrow r\_{1}=r.
Note that those risk measures can be used to evaluate the variability of the financial losses or risk as an alternative of variance.
Before discussing the robust risk aggregation for IRD\mathrm{IRD}, we introduce some concepts and obtain a general result on the robust risk aggregation of the difference between two tail risk measures.

For p∈(0,1)p\in(0,1), we say ρ:ℳ→ℝ∪{∞}\rho:\mathcal{M}\to\mathbb{R}\cup\{\infty\} is a *pp-upper-tail risk measure* if ρ​(μ1)=ρ​(μ2)\rho(\mu\_{1})=\rho(\mu\_{2}) for all μ1,μ2∈ℳ\mu\_{1},\mu\_{2}\in\mathcal{M} satisfying μ1p+=μ2p+\mu\_{1}^{p+}=\mu\_{2}^{p+}; we say ρ:ℳ→ℝ∪{∞}\rho:\mathcal{M}\to\mathbb{R}\cup\{\infty\} is a *pp-lower-tail risk measure* if ρ​(μ1)=ρ​(μ2)\rho(\mu\_{1})=\rho(\mu\_{2}) for all μ1,μ2∈ℳ\mu\_{1},\mu\_{2}\in\mathcal{M} satisfying μ1p−=μ2p−\mu\_{1}^{p-}=\mu\_{2}^{p-}. Note that here the domain of ρ\rho can be restricted to ℳ1\mathcal{M}\_{1}. The pp-upper-tail risk measure is the so-called pp-tail risk measure introduced and studied in Liu and Wang ([2021](https://arxiv.org/html/2511.21929v1#bib.bib41)). We say ρ:ℳ→ℝ∪{∞}\rho:\mathcal{M}\to\mathbb{R}\cup\{\infty\} satisfies *monotonicity* if ρ​(μ1)⩽ρ​(μ2)\rho(\mu\_{1})\leqslant\rho(\mu\_{2}) for all μ1,μ2∈ℳ\mu\_{1},\mu\_{2}\in\mathcal{M} satisfying qt−​(μ1)⩽qt−​(μ2)q\_{t}^{-}(\mu\_{1})\leqslant q\_{t}^{-}(\mu\_{2}) for all t∈(0,1)t\in(0,1).

Clearly, for 0<r<s<10<r<s<1, R​[r,s]R[r,s] is an rr-upper-tail risk measure and also an ss-lower-tail risk measure; qr+q\_{r}^{+} is an rr-upper-tail risk measure and (r+ε)(r+\varepsilon)-lower-tail risk measure for some 0<ε<1−r0<\varepsilon<1-r; qr−q\_{r}^{-} is an rr-lower-tail risk measure and (r−ε)(r-\varepsilon)-upper-tail risk measure for some 0<ε<r0<\varepsilon<r. We refer to Liu and Wang ([2021](https://arxiv.org/html/2511.21929v1#bib.bib41)) for properties, applications and more examples on pp-upper-tail risk measures.

###### Theorem 4.

For 0<r⩽s<10<r\leqslant s<1, suppose that ρ1:ℳ→ℝ∪{∞}\rho\_{1}:\mathcal{M}\to\mathbb{R}\cup\{\infty\} is an ss-upper-tail risk measure and ρ2:ℳ→ℝ∪{∞}\rho\_{2}:\mathcal{M}\to\mathbb{R}\cup\{\infty\} is an rr-lower-tail risk measure. If ρ1\rho\_{1} and ρ2\rho\_{2} are monotone risk measures, for 𝛍∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n}, we have

|  |  |  |
| --- | --- | --- |
|  | supν∈Λ​(𝝁)(ρ1​(ν)−ρ2​(ν))=supν∈Λ​(𝝁)ρ1​(ν)−infν∈Λ​(𝝁)ρ2​(ν).\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}(\rho\_{1}(\nu)-\rho\_{2}(\nu))=\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\rho\_{1}(\nu)-\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}\rho\_{2}(\nu). |  |

###### Proof.

Clearly, we have

|  |  |  |
| --- | --- | --- |
|  | supν∈Λ​(𝝁)(ρ1​(ν)−ρ2​(ν))⩽supν∈Λ​(𝝁)ρ1​(ν)−infν∈Λ​(𝝁)ρ2​(ν).\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}(\rho\_{1}(\nu)-\rho\_{2}(\nu))\leqslant\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\rho\_{1}(\nu)-\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}\rho\_{2}(\nu). |  |

Next, we show the inverse inequality. In light of Theorem 3 of Liu and Wang ([2021](https://arxiv.org/html/2511.21929v1#bib.bib41)), we have

|  |  |  |
| --- | --- | --- |
|  | supν∈Λ​(𝝁)ρ1​(ν)=supν∈Λ​(𝝁𝒔+)ρ1∗​(ν)=supUi∼U​[s,1]ρ1∗​(∑i=1nqUi−​(μi)),\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\rho\_{1}(\nu)=\sup\_{\nu\in\Lambda(\boldsymbol{\mu^{s+}})}\rho\_{1}^{\*}(\nu)=\sup\_{U\_{i}\sim U[s,1]}\rho\_{1}^{\*}\left(\sum\_{i=1}^{n}q\_{U\_{i}}^{-}(\mu\_{i})\right), |  |

where ρ1∗\rho\_{1}^{\*} is the generator of ρ1\rho\_{1} satisfying ρ1​(μ)=ρ1∗​(μs+)\rho\_{1}(\mu)=\rho\_{1}^{\*}(\mu^{s+}) for all μ∈ℳ\mu\in\mathcal{M}.
Next, we show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | infν∈Λ​(𝝁)ρ2​(ν)=infν∈Λ​(𝝁𝒓−)ρ2∗​(ν)=infVi∼U​[0,r]ρ2∗​(∑i=1nqVi−​(μi)),\displaystyle\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}\rho\_{2}(\nu)=\inf\_{\nu\in\Lambda(\boldsymbol{\mu^{r-}})}\rho\_{2}^{\*}(\nu)=\inf\_{V\_{i}\sim U[0,r]}\rho\_{2}^{\*}\left(\sum\_{i=1}^{n}q\_{V\_{i}}^{-}(\mu\_{i})\right), |  | (4.9) |

where ρ2∗\rho\_{2}^{\*} satisfies ρ2​(μ)=ρ2∗​(μr−)\rho\_{2}(\mu)=\rho\_{2}^{\*}(\mu^{r-}) for all μ∈ℳ\mu\in\mathcal{M}. For any
(V1,…,Vn)(V\_{1},\dots,V\_{n}) with Vi∼U​[0,r]V\_{i}\sim\mathrm{U}[0,r], i∈[n]i\in[n], there exist (V1′,…,Vn′)(V\_{1}^{\prime},\dots,V\_{n}^{\prime}) and U′U^{\prime} such that (V1′,…,Vn′)​=𝑑​(V1,…,Vn)(V\_{1}^{\prime},\dots,V\_{n}^{\prime})\overset{d}{=}(V\_{1},\dots,V\_{n}) and U′∼U​[0,1]U^{\prime}\sim\mathrm{U}[0,1] is independent of (V1′,…,Vn′)(V\_{1}^{\prime},\dots,V\_{n}^{\prime}), where =𝑑\overset{d}{=} means equality in distribution. Let

|  |  |  |
| --- | --- | --- |
|  | Xi=qVi′−​(μi)​𝟙{U′<r}+qU′−​(μi)​𝟙{U′>r},i∈[n].X\_{i}=q\_{V\_{i}^{\prime}}^{-}(\mu\_{i})\mathds{1}\_{\{U^{\prime}<r\}}+q\_{U^{\prime}}^{-}(\mu\_{i})\mathds{1}\_{\{U^{\prime}>r\}},~i\in[n]. |  |

Then we have Xi∼μiX\_{i}\sim\mu\_{i} and

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nXi=(∑i=1nqVi′−​(μi))​𝟙{U′<r}+(∑i=1nqU′−​(μi))​𝟙{U′>r}.\sum\_{i=1}^{n}X\_{i}=\left(\sum\_{i=1}^{n}q\_{V\_{i}^{\prime}}^{-}(\mu\_{i})\right)\mathds{1}\_{\{U^{\prime}<r\}}+\left(\sum\_{i=1}^{n}q\_{U^{\prime}}^{-}(\mu\_{i})\right)\mathds{1}\_{\{U^{\prime}>r\}}. |  |

Note that ess​-​sup​∑i=1nqVi′−​(μi)⩽∑i=1nqr−​(μi)\mathrm{ess\mbox{-}sup}\sum\_{i=1}^{n}q\_{V\_{i}^{\prime}}^{-}(\mu\_{i})\leqslant\sum\_{i=1}^{n}q\_{r}^{-}(\mu\_{i}). Hence, we have

|  |  |  |
| --- | --- | --- |
|  | ρ2​(∑i=1nXi)=ρ2∗​(∑i=1nqVi′−​(μi))=ρ2∗​(∑i=1nqVi−​(μi)).\rho\_{2}\left(\sum\_{i=1}^{n}X\_{i}\right)=\rho\_{2}^{\*}\left(\sum\_{i=1}^{n}q\_{V\_{i}^{\prime}}^{-}(\mu\_{i})\right)=\rho\_{2}^{\*}\left(\sum\_{i=1}^{n}q\_{V\_{i}}^{-}(\mu\_{i})\right). |  |

Using the arbitrariness of ViV\_{i}, we have

|  |  |  |
| --- | --- | --- |
|  | infν∈Λ​(𝝁)ρ2​(ν)⩽infVi∼U​[0,r]ρ2∗​(∑i=1nqVi−​(μi)).\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}\rho\_{2}(\nu)\leqslant\inf\_{V\_{i}\sim U[0,r]}\rho\_{2}^{\*}\left(\sum\_{i=1}^{n}q\_{V\_{i}}^{-}(\mu\_{i})\right). |  |

For Xi∼μi,i∈[n]X\_{i}\sim\mu\_{i},~i\in[n], let S=∑i=1nXiS=\sum\_{i=1}^{n}X\_{i}. Let (V1,…,Vn)​=𝑑​(UX1,…,UXn)/US<r(V\_{1},\dots,V\_{n})\overset{d}{=}(U\_{X\_{1}},\dots,U\_{X\_{n}})/U\_{S}<r.
Direct computation shows ℙ​(Vi⩽x)=ℙ​(UXi⩽x,US<r)r⩽xr∧1\mathbb{P}(V\_{i}\leqslant x)=\frac{\mathbb{P}(U\_{X\_{i}}\leqslant x,U\_{S}<r)}{r}\leqslant\frac{x}{r}\wedge 1 for x∈[0,1]x\in[0,1]. Hence, there exist Vi′∼U​[0,r],i∈[n]V\_{i}^{\prime}\sim U[0,r],~i\in[n] such that Vi′⩽Vi,i∈[n]V\_{i}^{\prime}\leqslant V\_{i},~i\in[n]. Note that the monotonicity of ρ2\rho\_{2} implies the monotonicity of ρ2∗\rho\_{2}^{\*}. Consequently, we have

|  |  |  |
| --- | --- | --- |
|  | ρ2​(S)=ρ2∗​(S/US<r)=ρ2∗​(∑i=1nqVi−​(μi))⩾ρ2∗​(∑i=1nqVi′−​(μi)),\rho\_{2}(S)=\rho\_{2}^{\*}(S/U\_{S}<r)=\rho\_{2}^{\*}\left(\sum\_{i=1}^{n}q\_{V\_{i}}^{-}(\mu\_{i})\right)\geqslant\rho\_{2}^{\*}\left(\sum\_{i=1}^{n}q\_{V\_{i}^{\prime}}^{-}(\mu\_{i})\right), |  |

implying

|  |  |  |
| --- | --- | --- |
|  | infν∈Λ​(𝝁)ρ2​(ν)⩾infVi∼U​[0,r]ρ2∗​(∑i=1nqVi−​(μi)).\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}\rho\_{2}(\nu)\geqslant\inf\_{V\_{i}\sim U[0,r]}\rho\_{2}^{\*}\left(\sum\_{i=1}^{n}q\_{V\_{i}}^{-}(\mu\_{i})\right). |  |

We establish the claim ([4.9](https://arxiv.org/html/2511.21929v1#S4.E9 "In 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")).

For any (U1,…,Un)(U\_{1},\dots,U\_{n}) and (V1,…,Vn)(V\_{1},\dots,V\_{n}) with Ui∼U​[s,1]U\_{i}\sim\mathrm{U}[s,1] and Vi∼U​[0,r]V\_{i}\sim\mathrm{U}[0,r], i∈[n]i\in[n], there exist (U1′,…,Un′)(U\_{1}^{\prime},\dots,U\_{n}^{\prime}), (V1′,…,Vn′)(V\_{1}^{\prime},\dots,V\_{n}^{\prime}), and U′U^{\prime} such that (U1′,…,Un′,V1′,…,Vn′)​=𝑑​(U1,…,Un,V1,…,Vn)(U\_{1}^{\prime},\dots,U\_{n}^{\prime},V\_{1}^{\prime},\dots,V\_{n}^{\prime})\overset{d}{=}(U\_{1},\dots,U\_{n},V\_{1},\dots,V\_{n}) and U′∼U​[0,1]U^{\prime}\sim\mathrm{U}[0,1] is independent of (U1′,…,Un′,V1′,…,Vn′)(U\_{1}^{\prime},\dots,U\_{n}^{\prime},V\_{1}^{\prime},\dots,V\_{n}^{\prime}). Let

|  |  |  |
| --- | --- | --- |
|  | Xi=qUi′−​(μi)​𝟙{U′>s}+qU′−​(μi)​𝟙{r<U′⩽s}+qVi′−​(μi)​𝟙{U′⩽r}.X\_{i}=q\_{U\_{i}^{\prime}}^{-}(\mu\_{i})\mathds{1}\_{\{U^{\prime}>s\}}+q\_{U^{\prime}}^{-}(\mu\_{i})\mathds{1}\_{\{r<U^{\prime}\leqslant s\}}+q\_{V\_{i}^{\prime}}^{-}(\mu\_{i})\mathds{1}\_{\{U^{\prime}\leqslant r\}}. |  |

Clearly, Xi∼μiX\_{i}\sim\mu\_{i} and

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nXi=(∑i=1nqUi′−​(μi))​𝟙{U′>s}+(∑i=1nqU′−​(μi))​𝟙{r<U′⩽s}+(∑i=1nqVi′−​(μi))​𝟙{U′⩽r}.\sum\_{i=1}^{n}X\_{i}=\left(\sum\_{i=1}^{n}q\_{U\_{i}^{\prime}}^{-}(\mu\_{i})\right)\mathds{1}\_{\{U^{\prime}>s\}}+\left(\sum\_{i=1}^{n}q\_{U^{\prime}}^{-}(\mu\_{i})\right)\mathds{1}\_{\{r<U^{\prime}\leqslant s\}}+\left(\sum\_{i=1}^{n}q\_{V\_{i}^{\prime}}^{-}(\mu\_{i})\right)\mathds{1}\_{\{U^{\prime}\leqslant r\}}. |  |

Note that ess​-​inf​∑i=1nqUi′−​(μi)⩾∑i=1nqs−​(μi)⩾∑i=1nqr+​(μi)⩾ess​-​sup​∑i=1nqVi′−​(μi)\mathrm{ess\mbox{-}inf}\sum\_{i=1}^{n}q\_{U\_{i}^{\prime}}^{-}(\mu\_{i})\geqslant\sum\_{i=1}^{n}q\_{s}^{-}(\mu\_{i})\geqslant\sum\_{i=1}^{n}q\_{r}^{+}(\mu\_{i})\geqslant\mathrm{ess\mbox{-}sup}\sum\_{i=1}^{n}q\_{V\_{i}^{\prime}}^{-}(\mu\_{i}).
Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ1​(∑i=1nXi)−ρ2​(∑i=1nXi)\displaystyle\rho\_{1}\left(\sum\_{i=1}^{n}X\_{i}\right)-\rho\_{2}\left(\sum\_{i=1}^{n}X\_{i}\right) | =ρ1∗​(∑i=1nqUi′−​(μi))−ρ2∗​(∑i=1nqVi′−​(μi))\displaystyle=\rho\_{1}^{\*}\left(\sum\_{i=1}^{n}q\_{U\_{i}^{\prime}}^{-}(\mu\_{i})\right)-\rho\_{2}^{\*}\left(\sum\_{i=1}^{n}q\_{V\_{i}^{\prime}}^{-}(\mu\_{i})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ρ1∗​(∑i=1nqUi−​(μi))−ρ2∗​(∑i=1nqVi−​(μi))\displaystyle=\rho\_{1}^{\*}\left(\sum\_{i=1}^{n}q\_{U\_{i}}^{-}(\mu\_{i})\right)-\rho\_{2}^{\*}\left(\sum\_{i=1}^{n}q\_{V\_{i}}^{-}(\mu\_{i})\right) |  |

Using the arbitrariness of UiU\_{i} and ViV\_{i}, we have

|  |  |  |
| --- | --- | --- |
|  | supν∈Λ​(𝝁)(ρ1​(ν)−ρ2​(ν))⩾supUi∼U​[s,1]ρ1∗​(∑i=1nqUi−​(μi))−infVi∼U​[0,r]ρ2∗​(∑i=1nqVi−​(μi)),\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}(\rho\_{1}(\nu)-\rho\_{2}(\nu))\geqslant\sup\_{U\_{i}\sim U[s,1]}\rho\_{1}^{\*}\left(\sum\_{i=1}^{n}q\_{U\_{i}}^{-}(\mu\_{i})\right)-\inf\_{V\_{i}\sim U[0,r]}\rho\_{2}^{\*}\left(\sum\_{i=1}^{n}q\_{V\_{i}}^{-}(\mu\_{i})\right), |  |

which shows the inverse inequality. We complete the proof.

∎

Applying Theorem [4](https://arxiv.org/html/2511.21929v1#Thmtheorem4 "Theorem 4. ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we obtain the following results.

###### Corollary 2 (IRD aggregation upper bound).

1. (i)

   For either 𝝁∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} and 0<r1<s1⩽r2<s2⩽10<r\_{1}<s\_{1}\leqslant r\_{2}<s\_{2}\leqslant 1, or 𝝁∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n} and 0⩽r1<s1⩽r2<s2⩽10\leqslant r\_{1}<s\_{1}\leqslant r\_{2}<s\_{2}\leqslant 1, we have
   sup\_ν∈Λ(μ)IRD\_[r\_1,s\_1],[r\_2,s\_2](ν)=sup\_ν∈Λ(μ)R\_[r\_2,s\_2](ν)-inf\_ν∈Λ(μ)R\_[r\_1,s\_1](ν).
2. (ii)

   For 𝝁∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} and 0<r⩽s<10<r\leqslant s<1, we have sup\_ν∈Λ(μ) (q\_s^+(ν)-q\_r^-(ν))=sup\_ν∈Λ(μ)q\_s^+(ν)-inf\_ν∈Λ(μ)q\_r^-(ν).
3. (iii)

   For 𝝁∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} with continuous q⋅−​(μ1),…,q⋅−​(μn)q\_{\cdot}^{-}(\mu\_{1}),\dots,q\_{\cdot}^{-}(\mu\_{n}) on (0,1)(0,1) and 0<r<s<10<r<s<1, we have sup\_ν∈Λ(μ) (q\_s^-(ν)-q\_r^+(ν))=sup\_ν∈Λ(μ) (q\_s^+(ν)-q\_r^-(ν))=sup\_ν∈Λ(μ)q\_s^+(ν)-inf\_ν∈Λ(μ)q\_r^-(ν).

###### Proof.

The claims in (i) and (ii) follow directly from Theorem [4](https://arxiv.org/html/2511.21929v1#Thmtheorem4 "Theorem 4. ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"). We next focus on (iii). Note that qs−q\_{s}^{-} is an r+s2\frac{r+s}{2}-upper-tail risk measure and qr+q\_{r}^{+} is an r+s2\frac{r+s}{2}-lower-tail risk measure. Moreover, both qs−q\_{s}^{-} and qr+q\_{r}^{+} are monotone risk measures. Hence, applying Theorem [4](https://arxiv.org/html/2511.21929v1#Thmtheorem4 "Theorem 4. ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we have

|  |  |  |
| --- | --- | --- |
|  | supν∈Λ​(𝝁)(qs−​(ν)−qr+​(ν))=supν∈Λ​(𝝁)qs−​(ν)−infν∈Λ​(𝝁)qr+​(ν).\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\left(q\_{s}^{-}(\nu)-q\_{r}^{+}(\nu)\right)=\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{s}^{-}(\nu)-\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{r}^{+}(\nu). |  |

By (ii), we have

|  |  |  |
| --- | --- | --- |
|  | supν∈Λ​(𝝁)(qs+​(ν)−qr−​(ν))=supν∈Λ​(𝝁)qs+​(ν)−infν∈Λ​(𝝁)qr−​(ν).\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\left(q\_{s}^{+}(\nu)-q\_{r}^{-}(\nu)\right)=\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{s}^{+}(\nu)-\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{r}^{-}(\nu). |  |

Moreover, it follows from Lemma 4.4 of Bernard et al. ([2014](https://arxiv.org/html/2511.21929v1#bib.bib6)) and the continuity of qt−​(μ1),…,qt−​(μn)q\_{t}^{-}(\mu\_{1}),\dots,q\_{t}^{-}(\mu\_{n}) on (0,1)(0,1) that supν∈Λ​(𝝁)qt+​(ν)\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{t}^{+}(\nu) is continuous on (0,1)(0,1), which further implies infν∈Λ​(𝝁)qt−​(ν)\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{t}^{-}(\nu) is continuous on (0,1)(0,1).
Hence, we have

|  |  |  |
| --- | --- | --- |
|  | supν∈Λ​(𝝁)qt+​(ν)=supν∈Λ​(𝝁)qt−​(ν),infν∈Λ​(𝝁)qt+​(ν)=infν∈Λ​(𝝁)qt−​(ν),t∈(0,1).\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{t}^{+}(\nu)=\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{t}^{-}(\nu),~\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{t}^{+}(\nu)=\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{t}^{-}(\nu),~t\in(0,1). |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | supν∈Λ​(𝝁)(qs−​(ν)−qr+​(ν))=supν∈Λ​(𝝁)(qs+​(ν)−qr−​(ν)).\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\left(q\_{s}^{-}(\nu)-q\_{r}^{+}(\nu)\right)=\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\left(q\_{s}^{+}(\nu)-q\_{r}^{-}(\nu)\right). |  |

This completes the proof.
∎

Theorem [4](https://arxiv.org/html/2511.21929v1#Thmtheorem4 "Theorem 4. ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") suggests that robust risk aggregation of the difference between two tail risk measures with dependence uncertainty equals the difference between two robust tail risk measures if the two regions of the tails do not intersect. This is because the worst-case dependence structure only concerns the dependence in the tail corner of the marginals. In light of Corollary [2](https://arxiv.org/html/2511.21929v1#Thmcorollary2 "Corollary 2 (IRD aggregation upper bound). ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), in order to find the (sharp) bound of the robust IRD\mathrm{IRD}, it suffices to find the (sharp) bound for robust RVaR\mathrm{RVaR}, which are given in Theorems 1 and A.1 of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)) and Theorems [2](https://arxiv.org/html/2511.21929v1#Thmtheorem2 "Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") and [3](https://arxiv.org/html/2511.21929v1#Thmtheorem3 "Theorem 3 (RVaR aggregation lower bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") of this paper.

Note that (ii) of Corollary [2](https://arxiv.org/html/2511.21929v1#Thmcorollary2 "Corollary 2 (IRD aggregation upper bound). ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") shows that for r∈(0,1)r\in(0,1), the largest possible difference between qr+​(ν)q\_{r}^{+}(\nu) and qr−​(ν)q\_{r}^{-}(\nu) has the following expression:

|  |  |  |
| --- | --- | --- |
|  | supν∈Λ​(𝝁)(qr+​(ν)−qr−​(ν))=supν∈Λ​(𝝁)qr+​(ν)−infν∈Λ​(𝝁)qr−​(ν),\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\left(q\_{r}^{+}(\nu)-q\_{r}^{-}(\nu)\right)=\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{r}^{+}(\nu)-\inf\_{\nu\in\Lambda(\boldsymbol{\mu})}q\_{r}^{-}(\nu), |  |

which is strictly positive in most cases, even if all μi\mu\_{i} have decreasing densities.

In light of Theorems [2](https://arxiv.org/html/2511.21929v1#Thmtheorem2 "Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")-[3](https://arxiv.org/html/2511.21929v1#Thmtheorem3 "Theorem 3 (RVaR aggregation lower bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") and Corollary [2](https://arxiv.org/html/2511.21929v1#Thmcorollary2 "Corollary 2 (IRD aggregation upper bound). ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") of the current paper and Theorems 1-2 and A.1-A.2 of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)), we immediately obtain the bounds for robust IRD and the difference between two quantiles. In what follows, we only present the sharp bounds and the corresponding conditions on the marignal distributions.

Applying Theorem [3](https://arxiv.org/html/2511.21929v1#Thmtheorem3 "Theorem 3 (RVaR aggregation lower bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") and Corollary [2](https://arxiv.org/html/2511.21929v1#Thmcorollary2 "Corollary 2 (IRD aggregation upper bound). ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") of this paper and Theorems 1 and A.1 of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)), we immediately arrive at the following results.

###### Proposition 3.

Suppose 𝛍∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n} and 0⩽r1<s1⩽r2<s2⩽10\leqslant r\_{1}<s\_{1}\leqslant r\_{2}<s\_{2}\leqslant 1.

1. (i)

   If each of μ1,…,μn\mu\_{1},\dots,\mu\_{n} admits a decreasing density beyond its r2r\_{2}-quantile and an increasing density below its s1s\_{1}-quantile, then

   |  |  |  |
   | --- | --- | --- |
   |  | supν∈Λ​(𝝁)IRD[r1,s1],[r2,s2]​(ν)=inf𝜷∈(1−r2)​Δnβ0⩾s2−r2∑i=1nR[1−βi−β0,1−βi]​(μi)−sup𝜷∈s1​Δnβ0⩾s1−r1∑i=1nR[βi,βi+β0]​(μi).\displaystyle\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\mathrm{IRD}\_{[r\_{1},s\_{1}],[r\_{2},s\_{2}]}(\nu)=\inf\_{\begin{subarray}{c}\boldsymbol{\beta}\in(1-r\_{2})\Delta\_{n}\\ \beta\_{0}\geqslant s\_{2}-r\_{2}\end{subarray}}\sum\_{i=1}^{n}R\_{[1-\beta\_{i}-\beta\_{0},1-\beta\_{i}]}(\mu\_{i})-\sup\_{\begin{subarray}{c}\boldsymbol{\beta}\in s\_{1}\Delta\_{n}\\ \beta\_{0}\geqslant s\_{1}-r\_{1}\end{subarray}}\sum\_{i=1}^{n}R\_{[\beta\_{i},\beta\_{i}+\beta\_{0}]}(\mu\_{i}). |  |
2. (ii)

   If each of μ1,…,μn\mu\_{1},\dots,\mu\_{n} admits a decreasing density beyond its r2r\_{2}-quantile and below its s1s\_{1}-quantile respectively, then

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | supν∈Λ​(𝝁)IRD[r1,s1],[r2,s2]​(ν)\displaystyle\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\mathrm{IRD}\_{[r\_{1},s\_{1}],[r\_{2},s\_{2}]}(\nu) | =inf𝜷∈(1−r2)​Δnβ0⩾s2−r2∑i=1nR[1−βi−β0,1−βi]​(μi)\displaystyle=\inf\_{\begin{subarray}{c}\boldsymbol{\beta}\in(1-r\_{2})\Delta\_{n}\\ \beta\_{0}\geqslant s\_{2}-r\_{2}\end{subarray}}\sum\_{i=1}^{n}R\_{[1-\beta\_{i}-\beta\_{0},1-\beta\_{i}]}(\mu\_{i}) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | −sup𝜷∈s1​Δnβ0⩾s1−r1{(1−r1+s1−β0s1)∑i=1nR[r1+s1−βi−β0,r1+s1−βi](μi)\displaystyle\quad-\sup\_{\begin{subarray}{c}\boldsymbol{\beta}\in s\_{1}\Delta\_{n}\\ \beta\_{0}\geqslant s\_{1}-r\_{1}\end{subarray}}\bigg\{\left(1-\frac{r\_{1}+s\_{1}-\beta\_{0}}{s\_{1}}\right)\sum\_{i=1}^{n}R\_{[r\_{1}+s\_{1}-\beta\_{i}-\beta\_{0},r\_{1}+s\_{1}-\beta\_{i}]}(\mu\_{i}) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +r1+s1−β0s1∑i=1nR[0,r1+s1−βi−β0]∪[r1+s1−βi,r1+s1](μi)}.\displaystyle\quad+\frac{r\_{1}+s\_{1}-\beta\_{0}}{s\_{1}}\sum\_{i=1}^{n}R\_{[0,r\_{1}+s\_{1}-\beta\_{i}-\beta\_{0}]\cup[r\_{1}+s\_{1}-\beta\_{i},r\_{1}+s\_{1}]}(\mu\_{i})\bigg\}. |  |

In light of Theorem [2](https://arxiv.org/html/2511.21929v1#Thmtheorem2 "Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") and Corollary [2](https://arxiv.org/html/2511.21929v1#Thmcorollary2 "Corollary 2 (IRD aggregation upper bound). ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") of this paper and Theorem A.1 of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)), we obtain the following results.

###### Proposition 4.

Suppose 𝛍∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n} and 0⩽r1<s1⩽r2<s2⩽10\leqslant r\_{1}<s\_{1}\leqslant r\_{2}<s\_{2}\leqslant 1.

1. (i)

   If each of μ1,…,μn\mu\_{1},\dots,\mu\_{n} admits an increasing density beyond its r2r\_{2}-quantile and below its s1s\_{1}-quantile, then

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | supν∈Λ​(𝝁)IRD[r1,s1],[r2,s2]​(ν)\displaystyle\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\mathrm{IRD}\_{[r\_{1},s\_{1}],[r\_{2},s\_{2}]}(\nu) | =inf𝜷∈(1−r2)​Δnβ0⩾1−s2{(1−1−r2−β0s2−r2)∑i=1nR[r2+βi,r2+βi+β0](μi)\displaystyle=\inf\_{\begin{subarray}{c}\boldsymbol{\beta}\in(1-r\_{2})\Delta\_{n}\\ \beta\_{0}\geqslant 1-s\_{2}\end{subarray}}\bigg\{\left(1-\frac{1-r\_{2}-\beta\_{0}}{s\_{2}-r\_{2}}\right)\sum\_{i=1}^{n}R\_{[r\_{2}+\beta\_{i},r\_{2}+\beta\_{i}+\beta\_{0}]}(\mu\_{i}) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +1−r2−β0s2−r2∑i=1nR[r2,r2+βi]∪[r2+βi+β0,1](μi)}\displaystyle\quad+\frac{1-r\_{2}-\beta\_{0}}{s\_{2}-r\_{2}}\sum\_{i=1}^{n}R\_{[r\_{2},r\_{2}+\beta\_{i}]\cup[r\_{2}+\beta\_{i}+\beta\_{0},1]}(\mu\_{i})\bigg\} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | −sup𝜷∈s1​Δnβ0⩾s1−r1∑i=1nR[βi,βi+β0]​(μi).\displaystyle\quad-\sup\_{\begin{subarray}{c}\boldsymbol{\beta}\in s\_{1}\Delta\_{n}\\ \beta\_{0}\geqslant s\_{1}-r\_{1}\end{subarray}}\sum\_{i=1}^{n}R\_{[\beta\_{i},\beta\_{i}+\beta\_{0}]}(\mu\_{i}). |  |
2. (ii)

   If each of μ1,…,μn\mu\_{1},\dots,\mu\_{n} admits an increasing density beyond its r2r\_{2}-quantile and a decreasing density below its s1s\_{1}-quantile, then

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | supν∈Λ​(𝝁)IRD[r1,s1],[r2,s2]​(ν)\displaystyle\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\mathrm{IRD}\_{[r\_{1},s\_{1}],[r\_{2},s\_{2}]}(\nu) | =inf𝜷∈(1−r2)​Δnβ0⩾1−s2{(1−1−r2−β0s2−r2)∑i=1nR[r2+βi,r2+βi+β0](μi)\displaystyle=\inf\_{\begin{subarray}{c}\boldsymbol{\beta}\in(1-r\_{2})\Delta\_{n}\\ \beta\_{0}\geqslant 1-s\_{2}\end{subarray}}\bigg\{\left(1-\frac{1-r\_{2}-\beta\_{0}}{s\_{2}-r\_{2}}\right)\sum\_{i=1}^{n}R\_{[r\_{2}+\beta\_{i},r\_{2}+\beta\_{i}+\beta\_{0}]}(\mu\_{i}) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +1−r2−β0s2−r2∑i=1nR[r2,r2+βi]∪[r2+βi+β0,1](μi)}\displaystyle\quad+\frac{1-r\_{2}-\beta\_{0}}{s\_{2}-r\_{2}}\sum\_{i=1}^{n}R\_{[r\_{2},r\_{2}+\beta\_{i}]\cup[r\_{2}+\beta\_{i}+\beta\_{0},1]}(\mu\_{i})\bigg\} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | −sup𝜷∈s1​Δnβ0⩾s1−r1{(1−r1+s1−β0s1)∑i=1nR[r1+s1−βi−β0,r1+s1−βi](μi)\displaystyle\quad-\sup\_{\begin{subarray}{c}\boldsymbol{\beta}\in s\_{1}\Delta\_{n}\\ \beta\_{0}\geqslant s\_{1}-r\_{1}\end{subarray}}\bigg\{\left(1-\frac{r\_{1}+s\_{1}-\beta\_{0}}{s\_{1}}\right)\sum\_{i=1}^{n}R\_{[r\_{1}+s\_{1}-\beta\_{i}-\beta\_{0},r\_{1}+s\_{1}-\beta\_{i}]}(\mu\_{i}) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +r1+s1−β0s1∑i=1nR[0,r1+s1−βi−β0]∪[r1+s1−βi,r1+s1](μi)}.\displaystyle\quad+\frac{r\_{1}+s\_{1}-\beta\_{0}}{s\_{1}}\sum\_{i=1}^{n}R\_{[0,r\_{1}+s\_{1}-\beta\_{i}-\beta\_{0}]\cup[r\_{1}+s\_{1}-\beta\_{i},r\_{1}+s\_{1}]}(\mu\_{i})\bigg\}. |  |

Combining Corollary [2](https://arxiv.org/html/2511.21929v1#Thmcorollary2 "Corollary 2 (IRD aggregation upper bound). ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") of this paper with Theorems 2 and A.2 of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)), we obtain the following results.

###### Proposition 5.

For 𝛍∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} and 0<r⩽s<10<r\leqslant s<1, if each of μ1,…,μn\mu\_{1},\dots,\mu\_{n} has a density that is monotone in the same direction beyond its ss-quantile and also monotone in the same direction below its rr-quantile, then we have

|  |  |  |
| --- | --- | --- |
|  | supν∈Λ​(𝝁)(qs+​(ν)−qr−​(ν))=inf𝜷∈(1−s)​Δn∑i=1nR[1−βi−β0,1−βi]​(μi)−sup𝜷∈r​Δn∑i=1nR[βi,βi+β0]​(μi).\sup\_{\nu\in\Lambda(\boldsymbol{\mu})}\left(q\_{s}^{+}(\nu)-q\_{r}^{-}(\nu)\right)=\inf\_{\begin{subarray}{c}\boldsymbol{\beta}\in(1-s)\Delta\_{n}\end{subarray}}\sum\_{i=1}^{n}R\_{[1-\beta\_{i}-\beta\_{0},1-\beta\_{i}]}(\mu\_{i})-\sup\_{\begin{subarray}{c}\boldsymbol{\beta}\in r\Delta\_{n}\end{subarray}}\sum\_{i=1}^{n}R\_{[\beta\_{i},\beta\_{i}+\beta\_{0}]}(\mu\_{i}). |  |

The sharp bounds given in Propositions [3](https://arxiv.org/html/2511.21929v1#Thmproposition3 "Proposition 3. ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")-[5](https://arxiv.org/html/2511.21929v1#Thmproposition5 "Proposition 5. ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") are the upper bounds that are valid for all 𝝁∈ℳ1n\boldsymbol{\mu}\in\mathcal{M}\_{1}^{n} and 0⩽r1<s1⩽r2<s2⩽10\leqslant r\_{1}<s\_{1}\leqslant r\_{2}<s\_{2}\leqslant 1 or 𝝁∈ℳn\boldsymbol{\mu}\in\mathcal{M}^{n} and 0<r1<s1⩽r2<s2⩽10<r\_{1}<s\_{1}\leqslant r\_{2}<s\_{2}\leqslant 1. Note that the sharp bounds in (ii) of Proposition [3](https://arxiv.org/html/2511.21929v1#Thmproposition3 "Proposition 3. ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") and (i) and (ii) of Proposition [4](https://arxiv.org/html/2511.21929v1#Thmproposition4 "Proposition 4. ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") are based on the results in Theorems [2](https://arxiv.org/html/2511.21929v1#Thmtheorem2 "Theorem 2 (RVaR aggregation upper bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") and [3](https://arxiv.org/html/2511.21929v1#Thmtheorem3 "Theorem 3 (RVaR aggregation lower bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), showing their applications to risk aggregation for other risk measures. It is also worth mentioning that based on Theorem [3](https://arxiv.org/html/2511.21929v1#Thmtheorem3 "Theorem 3 (RVaR aggregation lower bound). ‣ 4.1 RVaR Aggregation Upper and Lower Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), (ii) of Proposition [3](https://arxiv.org/html/2511.21929v1#Thmproposition3 "Proposition 3. ‣ 4.2 Inter-RVaR Difference Aggregation Upper Bounds ‣ 4 Extended Convolution Bounds ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") gives a sharp upper bound for IRD\mathrm{IRD} if the marginals have decreasing densities on their upper-tail parts and lower-tail parts respectively. This assumption is valid for many practically used distributions in finance and risk management, such as exponential, Pareto, and some gamma and chi distributions.

The extended convolution bounds developed in this section, particularly the sharp bounds, can be applied directly in risk management, including risk evaluation under dependence uncertainty (conservative regulatory capital calculation; e.g., Embrechts et al. ([2013](https://arxiv.org/html/2511.21929v1#bib.bib23)) and Eckstein et al. ([2020](https://arxiv.org/html/2511.21929v1#bib.bib19))), portfolio optimization under dependence uncertainty (e.g., Pflug and Pohl ([2018](https://arxiv.org/html/2511.21929v1#bib.bib46)), Chen et al. ([2022](https://arxiv.org/html/2511.21929v1#bib.bib12)) and Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8))) and optimal insurance/reinsurance design under dependence uncertainty (e.g., Fadina et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib25))). Other applications in operations research can be seen in the discussion in Section [1](https://arxiv.org/html/2511.21929v1#S1 "1 Introduction ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing").

## 5 Risk Sharing

In this section, we consider the risk sharing problem among nn agents, where their preferences are represented by some risk functionals ρi:𝒳1→ℝ\rho\_{i}:\mathcal{X}\_{1}\to\mathbb{R}, i∈[n]i\in[n]. For a total risk X∈𝒳1X\in\mathcal{X}\_{1}, the set of all possible allocations of XX is denoted by

|  |  |  |
| --- | --- | --- |
|  | 𝔸n​(X)={(X1,…,Xn)∈(𝒳1)n:∑i=1nXi=X}.\mathbb{A}\_{n}(X)=\left\{(X\_{1},\dots,X\_{n})\in(\mathcal{X}\_{1})^{n}:\sum\_{i=1}^{n}X\_{i}=X\right\}. |  |

The *inf-convolution* of ρ1,…,ρn\rho\_{1},\dots,\rho\_{n} is defined as

|  |  |  |
| --- | --- | --- |
|  | □i=1nρi​(X)=inf{∑i=1nρi​(Xi):(X1,…,Xn)∈𝔸n​(X)},X∈𝒳1.\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{i}(X)=\inf\left\{\sum\_{i=1}^{n}\rho\_{i}(X\_{i}):(X\_{1},\dots,X\_{n})\in\mathbb{A}\_{n}(X)\right\},~~X\in\mathcal{X}\_{1}. |  |

In this section, we use risk functionals RI1,…,RInR\_{I\_{1}},\dots,R\_{I\_{n}} to represent the agents’ preferences, where Ii=[0,βi]∪[1−β+βi,1]I\_{i}=[0,\beta\_{i}]\cup[1-\beta+\beta\_{i},1] for all i∈[n]i\in[n] with a parameter vector 𝜷:=(β1,…,βn)∈(0,1)n\boldsymbol{\beta}:=(\beta\_{1},\dots,\beta\_{n})\in(0,1)^{n} satisfying β=∑i=1nβi\beta=\sum\_{i=1}^{n}\beta\_{i} and 0<β<10<\beta<1.
We aim to find the *optimal allocation* for the inf-convolution, i.e., finding (X1∗,…,Xn∗)∈𝔸n​(X)(X\_{1}^{\*},\dots,X\_{n}^{\*})\in\mathbb{A}\_{n}(X) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nRIi​(Xi∗)=□i=1nRIi​(X).\displaystyle\sum\_{i=1}^{n}R\_{I\_{i}}(X\_{i}^{\*})=\mathop{\square}\displaylimits\_{i=1}^{n}R\_{I\_{i}}(X). |  | (5.1) |

The central object in our investigation of risk sharing is the form taken by R[0,α]∪[γ,1]R\_{[0,\alpha]\cup[\gamma,1]} with 0⩽α<γ⩽10\leqslant\alpha<\gamma\leqslant 1. In the risk sharing context, the motivation of using such preference functionals can be interpreted from the fact that for λ∈(0,1)\lambda\in(0,1),

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​𝔼​(X)+(1−λ)​RIi​(X)=∫01q1−s−​(X)​dgλ,i​(s):=ρgλ,i​(X),\lambda\mathbb{E}(X)+(1-\lambda)R\_{I\_{i}}(X)=\int\_{0}^{1}q\_{1-s}^{-}(X)\mathrm{d}g\_{\lambda,i}(s):=\rho\_{g\_{\lambda,i}}(X), |  | (5.2) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | gλ,i​(s)=λ​s+1−λβ​(s∧(β−βi))​𝟙[0,1−βi]​(s)+1−λβ​(s−1+β)​𝟙[1−βi,1]​(s)\displaystyle g\_{\lambda,i}(s)=\lambda s+\frac{1-\lambda}{\beta}(s\wedge(\beta-\beta\_{i}))\mathds{1}\_{[0,1-\beta\_{i}]}(s)+\frac{1-\lambda}{\beta}(s-1+\beta)\mathds{1}\_{[1-\beta\_{i},1]}(s) |  | (5.3) |

is a distortion function. Hence, the above risk functionals ρgλ,i\rho\_{g\_{\lambda,i}} can be viewed as either a Yaari’s dual utility or a distortion risk measure; see Yaari ([1987](https://arxiv.org/html/2511.21929v1#bib.bib61)) and Chapter 4 of Föllmer and Schied ([2016](https://arxiv.org/html/2511.21929v1#bib.bib28)). Note that the distortion function gλ,ig\_{\lambda,i} has the inverse S-shape, exaggerating the probabilities for both large losses and large gains. If XX is the possible random loss in future, then the distortion risk measure defined above represents the decision maker’s attitude: risk aversion for large losses and risk-seeking for small losses or gains; see Yaari ([1987](https://arxiv.org/html/2511.21929v1#bib.bib61)) and Tversky and Kahneman ([1992](https://arxiv.org/html/2511.21929v1#bib.bib53)). The distortion risk measures with general distortion functions are also popular in insurance pricing, performance evaluation and other applications; see e.g., Wang ([1996](https://arxiv.org/html/2511.21929v1#bib.bib55)), Wang ([2000](https://arxiv.org/html/2511.21929v1#bib.bib56)), Cherny and Madan ([2009](https://arxiv.org/html/2511.21929v1#bib.bib13)) and Föllmer and Schied ([2016](https://arxiv.org/html/2511.21929v1#bib.bib28)). Note that the risk sharing for λ​𝔼​(X)+(1−λ)​RIi​(X)\lambda\mathbb{E}(X)+(1-\lambda)R\_{I\_{i}}(X) is equivalent to the risk sharing for RIiR\_{I\_{i}} in terms of the optimal risk allocations. This motivates us to consider the risk sharing for RIiR\_{I\_{i}}.

For monetary risk measures111We say a mapping ρ:𝒳→ℝ\rho:\mathcal{X}\to\mathbb{R} is a monetary risk measure if it satisfies cash invariance, i.e.,
ρ​(X+c)=ρ​(X)+c\rho(X+c)=\rho(X)+c for X∈𝒳X\in\mathcal{X} and c∈ℝc\in\mathbb{R}, and monotonicity, i.e., ρ​(X)⩽ρ​(Y)\rho(X)\leqslant\rho(Y) for X⩽YX\leqslant Y; see e.g., Chapter 4 of Föllmer and Schied ([2016](https://arxiv.org/html/2511.21929v1#bib.bib28)).,
optimality with respect to the sum (referred to as the sum optimality) is equivalent to Pareto optimality (e.g., Proposition 1 of Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20))). Clearly, RIR\_{I} and ρgλ,i\rho\_{g\_{\lambda,i}} are monetary risk measures. More economic interpretation on the inf-convolution can be found in e.g., Chapter 10 of Rüschendorf ([2013](https://arxiv.org/html/2511.21929v1#bib.bib51)).

We next give the definition of comonotonicity and counter-comonotonicity for nn random variables to interpret the optimal allocations. We say (X1,…,Xn)(X\_{1},\dots,X\_{n}) are *comonotonic* if there exist increasing functions fi,i∈[n]f\_{i},~i\in[n] such that Xi=fi​(X1+⋯+Xn)X\_{i}=f\_{i}(X\_{1}+\dots+X\_{n}) for all i∈[n]i\in[n]; we say (X1,…,Xn)(X\_{1},\dots,X\_{n}) are *counter-comonotonic* if (−Xi,Xj)(-X\_{i},X\_{j}) are comonotonic for any i≠ji\neq j. We refer to Dhaene et al. ([2002](https://arxiv.org/html/2511.21929v1#bib.bib18)) for an overview on comonotonicity, and Lauzier et al. ([2023](https://arxiv.org/html/2511.21929v1#bib.bib37)) for the characterization on counter-comonotonicity.

Our result for Problem ([5.1](https://arxiv.org/html/2511.21929v1#S5.E1 "In 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) is displayed as follows. In what follows, x+:=x∨0x\_{+}:=x\vee 0 for x∈ℝx\in\mathbb{R}.

###### Theorem 5 (Risk sharing for the average quantile).

For X∈𝒳1X\in\mathcal{X}\_{1} and 𝛃∈(0,1)n\boldsymbol{\beta}\in(0,1)^{n} satisfying β∈(0,1)\beta\in(0,1), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | □i=1nRIi​(X)=R[0,β]​(X).\mathop{\square}\displaylimits\_{i=1}^{n}R\_{I\_{i}}(X)=R\_{[0,\beta]}(X). |  | (5.4) |

Moreover, if XX is bounded from above, an optimal allocation is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xi=(X−t)​𝟙Ai+Xn​𝟙Ac+tn−1​𝟙A∖Ai,i∈[n],\displaystyle X\_{i}=(X-t)\mathds{1}\_{A\_{i}}+\frac{X}{n}\mathds{1}\_{A^{c}}+\frac{t}{n-1}\mathds{1}\_{A\setminus A\_{i}},~~i\in[n], |  | (5.5) |

where t⩾(q1−​(X))+t\geqslant(q\_{1}^{-}(X))\_{+}, A={UX⩽β}A=\{U\_{X}\leqslant\beta\} and (A1,…,An)(A\_{1},\dots,A\_{n}) is a partition of AA satisfying ℙ​(Ai)=βi\mathbb{P}(A\_{i})=\beta\_{i} for all i∈[n]i\in[n].

###### Proof.

By Corollary [1](https://arxiv.org/html/2511.21929v1#Thmcorollary1 "Corollary 1. ‣ 3 New RVaR Inequality ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | □i=1nRIi​(X)⩾R[0,β]​(X).\displaystyle\mathop{\square}\displaylimits\_{i=1}^{n}R\_{I\_{i}}(X)\geqslant R\_{[0,\beta]}(X). |  | (5.6) |

Hence, it suffices to show the inverse inequality of ([5.6](https://arxiv.org/html/2511.21929v1#S5.E6 "In 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")).
Suppose that XX is bounded from above and (X1,…,Xn)(X\_{1},\dots,X\_{n}) is given by ([5.5](https://arxiv.org/html/2511.21929v1#S5.E5 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")).
Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nXi\displaystyle\sum\_{i=1}^{n}X\_{i} | =∑i=1n(X−t)​𝟙Ai+∑i=1nXn​𝟙Ac+∑i=1ntn−1​𝟙A∖Ai\displaystyle=\sum\_{i=1}^{n}(X-t)\mathds{1}\_{A\_{i}}+\sum\_{i=1}^{n}\frac{X}{n}\mathds{1}\_{A^{c}}+\sum\_{i=1}^{n}\frac{t}{n-1}\mathds{1}\_{A\setminus A\_{i}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(X−t)​𝟙A+X​𝟙Ac+t​𝟙A=X,\displaystyle=(X-t)\mathds{1}\_{A}+X\mathds{1}\_{A^{c}}+t\mathds{1}\_{A}=X, |  |

and thus (X1,…,Xn)∈𝔸n​(X)(X\_{1},\dots,X\_{n})\in\mathbb{A}\_{n}(X).
We claim that, for each i∈[n]i\in[n],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xi​(ω1)⩽Xi​(ω2)⩽Xi​(ω3)​ for ω1∈Ai, ω2∈Ac and ω3∈A∖Ai almost surely.\displaystyle X\_{i}(\omega\_{1})\leqslant X\_{i}(\omega\_{2})\leqslant X\_{i}(\omega\_{3})\mbox{~~~for $\omega\_{1}\in A\_{i}$, $\omega\_{2}\in A^{c}$ and $\omega\_{3}\in A\setminus A\_{i}$ almost surely.} |  | (5.7) |

Note that Xi​(ω2)⩽Xi​(ω3)X\_{i}(\omega\_{2})\leqslant X\_{i}(\omega\_{3}) holds trivially.
We next show Xi​(ω1)⩽Xi​(ω2)X\_{i}(\omega\_{1})\leqslant X\_{i}(\omega\_{2}). By our construction, we have
Xi​(ω1)⩽qβ+​(X)−tX\_{i}(\omega\_{1})\leqslant q\_{\beta}^{+}(X)-t
and Xi​(ω2)∈[qβ+​(X)/n,q1−​(X)/n]X\_{i}(\omega\_{2})\in\left[q\_{\beta}^{+}(X)/n,q\_{1}^{-}(X)/n\right].
If qβ+​(X)⩽0q\_{\beta}^{+}(X)\leqslant 0, then

|  |  |  |
| --- | --- | --- |
|  | Xi​(ω1)⩽qβ+​(X)−t⩽qβ+​(X)⩽qβ+​(X)n⩽Xi​(ω2).X\_{i}(\omega\_{1})\leqslant q\_{\beta}^{+}(X)-t\leqslant q\_{\beta}^{+}(X)\leqslant\frac{q\_{\beta}^{+}(X)}{n}\leqslant X\_{i}(\omega\_{2}). |  |

If qβ+​(X)>0q\_{\beta}^{+}(X)>0, then

|  |  |  |
| --- | --- | --- |
|  | Xi​(ω1)⩽qβ+​(X)−t⩽0⩽qβ+​(X)n⩽Xi​(ω2).X\_{i}(\omega\_{1})\leqslant q\_{\beta}^{+}(X)-t\leqslant 0\leqslant\frac{q\_{\beta}^{+}(X)}{n}\leqslant X\_{i}(\omega\_{2}). |  |

Using ([5.7](https://arxiv.org/html/2511.21929v1#S5.E7 "In 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | RIi​(Xi)\displaystyle R\_{I\_{i}}(X\_{i}) | =1β​𝔼​[(X−t)​𝟙Ai+tn−1​𝟙A∖Ai]\displaystyle=\frac{1}{\beta}\mathbb{E}\left[(X-t)\mathds{1}\_{A\_{i}}+\frac{t}{n-1}\mathds{1}\_{A\setminus A\_{i}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1β​𝔼​[X​𝟙Ai]−βiβ​t+β−βi(n−1)​β​t\displaystyle=\frac{1}{\beta}\mathbb{E}[X\mathds{1}\_{A\_{i}}]-\frac{\beta\_{i}}{\beta}t+\frac{\beta-\beta\_{i}}{(n-1)\beta}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1β​𝔼​[X​𝟙Ai]+β−n​βi(n−1)​β​t.\displaystyle=\frac{1}{\beta}\mathbb{E}[X\mathds{1}\_{A\_{i}}]+\frac{\beta-n\beta\_{i}}{(n-1)\beta}t. |  |

It follows that

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nRIi​(Xi)=∑i=1n1β​𝔼​[X​𝟙Ai]+∑i=1nβ−n​βi(n−1)​β​t=1β​𝔼​[X​𝟙A]=R[0,β]​(X).\sum\_{i=1}^{n}R\_{I\_{i}}(X\_{i})=\sum\_{i=1}^{n}\frac{1}{\beta}\mathbb{E}[X\mathds{1}\_{A\_{i}}]+\sum\_{i=1}^{n}\frac{\beta-n\beta\_{i}}{(n-1)\beta}t=\frac{1}{\beta}\mathbb{E}[X\mathds{1}\_{A}]=R\_{[0,\beta]}(X). |  |

Hence, we obtain the inverse inequality of ([5.6](https://arxiv.org/html/2511.21929v1#S5.E6 "In 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")), implying that ([5.4](https://arxiv.org/html/2511.21929v1#S5.E4 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) and ([5.5](https://arxiv.org/html/2511.21929v1#S5.E5 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) hold for XX being bounded from above.

Next, we consider the case that XX is not bounded from above. For m⩾1m\geqslant 1,
let X(m)=X∧mX^{(m)}=X\wedge m and Z(m)=X−X(m)=(X−m)​𝟙{X>m}Z^{(m)}=X-X^{(m)}=(X-m)\mathds{1}\_{\{X>m\}}. Using the above result, we know that for each m⩾1m\geqslant 1, there exists (X1(m),…,Xn(m))∈𝔸n​(X(m))(X\_{1}^{(m)},\dots,X\_{n}^{(m)})\in\mathbb{A}\_{n}(X^{(m)}) such that

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nRIi​(Xi(m))=R[0,β]​(X(m))⩽R[0,β]​(X).\sum\_{i=1}^{n}R\_{I\_{i}}\left(X\_{i}^{(m)}\right)=R\_{[0,\beta]}\left(X^{(m)}\right)\leqslant R\_{[0,\beta]}\left(X\right). |  |

Let Y1(m)=X1(m)+Z(m)Y\_{1}^{(m)}=X\_{1}^{(m)}+Z^{(m)}. Then
we have (Y1(m),X2(m),…,Xn(m))∈𝔸n​(X)\left(Y\_{1}^{(m)},X\_{2}^{(m)},\dots,X\_{n}^{(m)}\right)\in\mathbb{A}\_{n}(X).
In light of Theorem 1 of Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20)), we have

|  |  |  |
| --- | --- | --- |
|  | RI1​(X1(m)+Z(m))\displaystyle\quad R\_{I\_{1}}\left(X\_{1}^{(m)}+Z^{(m)}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =β1β​R[0,β1]​(X1(m)+Z(m))+β−β1β​R[1−β+β1,1]​(X1(m)+Z(m))\displaystyle=\frac{\beta\_{1}}{\beta}R\_{[0,\beta\_{1}]}\left(X\_{1}^{(m)}+Z^{(m)}\right)+\frac{\beta-\beta\_{1}}{\beta}R\_{[1-\beta+\beta\_{1},1]}\left(X\_{1}^{(m)}+Z^{(m)}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ⩽β1β​(R[0,β1]​(X1(m))+ESβ1​(Z(m)))+β−β1β​(R[1−β+β1,1]​(X1(m))+ESβ−β1​(Z(m)))\displaystyle\leqslant\frac{\beta\_{1}}{\beta}\left(R\_{[0,\beta\_{1}]}\left(X\_{1}^{(m)}\right)+\mathrm{ES}\_{\beta\_{1}}\left(Z^{(m)}\right)\right)+\frac{\beta-\beta\_{1}}{\beta}\left(R\_{[1-\beta+\beta\_{1},1]}\left(X\_{1}^{(m)}\right)+\mathrm{ES}\_{\beta-\beta\_{1}}\left(Z^{(m)}\right)\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =RI1​(X1(m))+β1β​ESβ1​(Z(m))+β−β1β​ESβ−β1​(Z(m)).\displaystyle=R\_{I\_{1}}\left(X\_{1}^{(m)}\right)+\frac{\beta\_{1}}{\beta}\mathrm{ES}\_{\beta\_{1}}\left(Z^{(m)}\right)+\frac{\beta-\beta\_{1}}{\beta}\mathrm{ES}\_{\beta-\beta\_{1}}\left(Z^{(m)}\right). |  |

Note that

|  |  |  |
| --- | --- | --- |
|  | β1β​ESβ1​(Z(m))+β−β1β​ESβ−β1​(Z(m))⩽2β​𝔼​[Z(m)]→0​as​m→∞.\frac{\beta\_{1}}{\beta}\mathrm{ES}\_{\beta\_{1}}\left(Z^{(m)}\right)+\frac{\beta-\beta\_{1}}{\beta}\mathrm{ES}\_{\beta-\beta\_{1}}\left(Z^{(m)}\right)\leqslant\frac{2}{\beta}\mathbb{E}\left[Z^{(m)}\right]\to 0~\text{as}~m\to\infty. |  |

Therefore, for any ε>0\varepsilon>0, there exists m0>1m\_{0}>1 such that

|  |  |  |
| --- | --- | --- |
|  | RI1​(Y1(m))⩽RI1​(X1(m))+εR\_{I\_{1}}\left(Y\_{1}^{(m)}\right)\leqslant R\_{I\_{1}}\left(X\_{1}^{(m)}\right)+\varepsilon |  |

for all m>m0m>m\_{0}, which implies

|  |  |  |
| --- | --- | --- |
|  | RI1​(Y1(m))+∑i=2nRIi​(Xi(m))⩽∑i=1nRIi​(Xi(m))+ε⩽R[0,β]​(X)+ε.R\_{I\_{1}}\left(Y\_{1}^{(m)}\right)+\sum\_{i=2}^{n}R\_{I\_{i}}(X\_{i}^{(m)})\leqslant\sum\_{i=1}^{n}R\_{I\_{i}}\left(X\_{i}^{(m)}\right)+\varepsilon\leqslant R\_{[0,\beta]}\left(X\right)+\varepsilon. |  |

By the arbitrariness of ε\varepsilon, we obtain □i=1nRIi​(X)⩽R[0,β]​(X)\mathop{\square}\displaylimits\_{i=1}^{n}R\_{I\_{i}}(X)\leqslant R\_{[0,\beta]}(X), which together with ([5.6](https://arxiv.org/html/2511.21929v1#S5.E6 "In 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) implies ([5.4](https://arxiv.org/html/2511.21929v1#S5.E4 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")). The optimal allocation given in ([5.5](https://arxiv.org/html/2511.21929v1#S5.E5 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) has been checked in the above proof. This completes the proof.
∎

Note that ([5.5](https://arxiv.org/html/2511.21929v1#S5.E5 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) is also an optimal allocation if we replace tt in ([5.5](https://arxiv.org/html/2511.21929v1#S5.E5 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) by a random variable YY satisfying Y⩾(q1−​(X))+Y\geqslant(q\_{1}^{-}(X))\_{+}. There are also other types of optimal allocation; see Proposition [6](https://arxiv.org/html/2511.21929v1#Thmproposition6 "Proposition 6. ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") below. The optimal allocation in ([5.5](https://arxiv.org/html/2511.21929v1#S5.E5 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) shows that the risk is equally allocated over AcA^{c} and is counter-comonotonic over AA, i.e.,
(X−t)​𝟙Ai+tn−1​𝟙A∖Ai,i∈[n](X-t)\mathds{1}\_{A\_{i}}+\frac{t}{n-1}\mathds{1}\_{A\setminus A\_{i}},~~i\in[n] with (A1,…,An)(A\_{1},\dots,A\_{n}) being a partition of AA satisfying ℙ​(Ai)=βi\mathbb{P}(A\_{i})=\beta\_{i} for all i∈[n]i\in[n] are counter-monotonic restricted to AA.

In the literature of risk sharing, the optimal allocation is comonotonic if the risk functionals are law-invariant convex risk measures (see e.g., Jouini et al. ([2008](https://arxiv.org/html/2511.21929v1#bib.bib34)) and Filipović and Svindland ([2008](https://arxiv.org/html/2511.21929v1#bib.bib26))), and is counter-comonotonic if the risk functionals are quantile-based risk measures (see e.g., Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20)), Embrechts et al. ([2020](https://arxiv.org/html/2511.21929v1#bib.bib21)) and Liu et al. ([2022](https://arxiv.org/html/2511.21929v1#bib.bib40))). The optimal allocation in ([5.5](https://arxiv.org/html/2511.21929v1#S5.E5 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) exhibits a combination of two types of risk sharing in the literature: comonotonic risk sharing for large losses and counter-comonotonic risk sharing for small losses or large gains, which may be due to the agents’ risk attitudes: risk-aversion for large losses and risk-seeking for small losses or large gains.

In Theorem [5](https://arxiv.org/html/2511.21929v1#Thmtheorem5 "Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we only give the optimal allocation in ([5.5](https://arxiv.org/html/2511.21929v1#S5.E5 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) if XX is bounded from above. The existence of the optimal allocation is unknown from Theorem [5](https://arxiv.org/html/2511.21929v1#Thmtheorem5 "Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") if XX is unbounded from above. To answer this question requires the analysis on the dependence structure of the optimal allocations, which is not trivial.

Next, we discuss the dependence structure of (X1,…,Xn,X)(X\_{1},\dots,X\_{n},X) with (X1,…,Xn)∈𝔸n​(X)(X\_{1},\dots,X\_{n})\in\mathbb{A}\_{n}(X) such that for 𝜷∈(0,1)n\boldsymbol{\beta}\in(0,1)^{n} satisfying β=∑i=1nβi∈(0,1)\beta=\sum\_{i=1}^{n}\beta\_{i}\in(0,1), ([5.4](https://arxiv.org/html/2511.21929v1#S5.E4 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) holds.

###### Proposition 6.

For a random variable X∈𝒳1X\in\mathcal{X}\_{1} and a random vector (X1,…,Xn,X)(X\_{1},\dots,X\_{n},X) with (X1,X2,…,Xn)∈𝔸n​(X)(X\_{1},X\_{2},\dots,X\_{n})\in\mathbb{A}\_{n}(X), ([5.4](https://arxiv.org/html/2511.21929v1#S5.E4 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) holds if and only if there exist UX1,…,UXnU\_{X\_{1}},\dots,U\_{X\_{n}} and UXU\_{X} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {UX∈[0,β]}={UXi∈Ii},i∈[n].\left\{U\_{X}\in\left[0,\beta\right]\right\}=\left\{U\_{X\_{i}}\in I\_{i}\right\},\quad i\in\left[n\right]. |  | (5.8) |

Moreover, ([5.8](https://arxiv.org/html/2511.21929v1#S5.E8 "In Proposition 6. ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) implies that one of the following two statements holds:

1. (i)

   ⋃i=1n{UXi∈[0,βi]}={UX∈[0,β]}\bigcup\_{i=1}^{n}\{U\_{X\_{i}}\in[0,\beta\_{i}]\}=\{U\_{X}\in[0,\beta]\};
2. (ii)

   The set {UX∈[0,β]}∖⋃i=1n{UXi∈[0,βi]}\{U\_{X}\in[0,\beta]\}\setminus\bigcup\_{i=1}^{n}\{U\_{X\_{i}}\in[0,\beta\_{i}]\} has a positive probability, which is denoted by θ\theta. Meanwhile, random variables X1,…,XnX\_{1},\dots,X\_{n} and XX are all constants on the set {UX∈[β−θ,1]}\{U\_{X}\in[\beta-\theta,1]\}, which actually equals the set {UXi∈[βi,1−β+βi+θ]}\{U\_{X\_{i}}\in[\beta\_{i},1-\beta+\beta\_{i}+\theta]\} for all i∈[n]i\in[n].

###### Proof.

Obviously, the equation ([5.8](https://arxiv.org/html/2511.21929v1#S5.E8 "In Proposition 6. ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) is a sufficient condition for ([5.4](https://arxiv.org/html/2511.21929v1#S5.E4 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")).
We next show the only if part. Let β0=1−β\beta\_{0}=1-\beta. Then we have ∑i=0nβi=1\sum\_{i=0}^{n}\beta\_{i}=1. Note that ([5.4](https://arxiv.org/html/2511.21929v1#S5.E4 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) is equivalent to

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nR[βi,1−β+βi]​(Xi)=R[β,1]​(X),\sum\_{i=1}^{n}R\_{[\beta\_{i},1-\beta+\beta\_{i}]}(X\_{i})=R\_{[\beta,1]}(X), |  |

which is further equivalent to

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nR[1−βi−β0,1−βi]​(−Xi)=R[0,β0]​(−X).\sum\_{i=1}^{n}R\_{[1-\beta\_{i}-\beta\_{0},1-\beta\_{i}]}(-X\_{i})=R\_{[0,\beta\_{0}]}(-X). |  |

Let Yi=−Xi,i∈[n]Y\_{i}=-X\_{i},~i\in[n] and Y=−XY=-X.
For i∈[n]i\in[n], define random variables

|  |  |  |
| --- | --- | --- |
|  | Ti:=Yi​𝟙{UYi⩽1−βi}+m​𝟙{UYi>1−βi},T\_{i}:=Y\_{i}\mathds{1}\_{\{U\_{Y\_{i}}\leqslant 1-\beta\_{i}\}}+m\mathds{1}\_{\{U\_{Y\_{i}}>1-\beta\_{i}\}}, |  |

where m∈ℝm\in\mathbb{R} satisfying m<⋀i=1nq1−βi−β0−​(Yi)m<\bigwedge\_{i=1}^{n}q\_{1-\beta\_{i}-\beta\_{0}}^{-}(Y\_{i}).
By the construction of TiT\_{i}, one could see that for any s∈ℝs\in\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(∑i=1nTi>s)⩾\displaystyle\mathbb{P}\left(\sum\_{i=1}^{n}T\_{i}>s\right)\geqslant | ℙ​({∑i=1nYi>s}∩(∪i=1n{UYi>1−βi})c)\displaystyle\mathbb{P}\left(\left\{\sum\_{i=1}^{n}Y\_{i}>s\right\}\cap(\cup\_{i=1}^{n}\{U\_{Y\_{i}}>1-\beta\_{i}\})^{c}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⩾\displaystyle\geqslant | ℙ​(∑i=1nYi>s)−ℙ​(∪i=1n{UYi>1−βi})\displaystyle\mathbb{P}\left(\sum\_{i=1}^{n}Y\_{i}>s\right)-\mathbb{P}\left(\cup\_{i=1}^{n}\{U\_{Y\_{i}}>1-\beta\_{i}\}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⩾\displaystyle\geqslant | ℙ​(∑i=1nYi>s)−1+β0.\displaystyle\mathbb{P}\left(\sum\_{i=1}^{n}Y\_{i}>s\right)-1+\beta\_{0}. |  |

Thus, we have

|  |  |  |
| --- | --- | --- |
|  | qu−​(∑i=1nTi)⩾qu−1+β0−​(∑i=1nYi),∀u∈(1−β0,1].q\_{u}^{-}\left(\sum\_{i=1}^{n}T\_{i}\right)\geqslant q\_{u-1+\beta\_{0}}^{-}\left(\sum\_{i=1}^{n}Y\_{i}\right),\quad\forall u\in(1-\beta\_{0},1]. |  |

Then, combined with the subadditivity of ES\mathrm{ES}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nR[1−βi−β0,1−βi]​(Yi)=∑i=1nESβ0​(Ti)\displaystyle\sum\_{i=1}^{n}R\_{\left[1-\beta\_{i}-\beta\_{0},1-\beta\_{i}\right]}(Y\_{i})=\sum\_{i=1}^{n}\mathrm{ES}\_{\beta\_{0}}(T\_{i}) | ⩾ESβ0​(∑i=1nTi)\displaystyle\geqslant\mathrm{ES}\_{\beta\_{0}}\left(\sum\_{i=1}^{n}T\_{i}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1β0​∫1−β01qu−​(∑i=1nTi)​du\displaystyle=\frac{1}{\beta\_{0}}\int\_{1-\beta\_{0}}^{1}q\_{u}^{-}\left(\sum\_{i=1}^{n}T\_{i}\right)\mathrm{d}u |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩾1β0​∫1−β01qu−1+β0−​(Y)​du.\displaystyle\geqslant\frac{1}{\beta\_{0}}\int\_{1-\beta\_{0}}^{1}q\_{u-1+\beta\_{0}}^{-}\left(Y\right)\mathrm{d}u. |  |

Direct computation shows

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1β0​∫1−β01qu−1+β0−​(Y)​du\displaystyle\frac{1}{\beta\_{0}}\int\_{1-\beta\_{0}}^{1}q\_{u-1+\beta\_{0}}^{-}\left(Y\right)\mathrm{d}u | =1β0​∫0β0qu−​(Y)​du\displaystyle=\frac{1}{\beta\_{0}}\int\_{0}^{\beta\_{0}}q\_{u}^{-}\left(Y\right)\mathrm{d}u |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =LESβ0​(Y)\displaystyle=\mathrm{LES}\_{\beta\_{0}}\left(Y\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1nR[1−βi−β0,1−βi]​(Yi),\displaystyle=\sum\_{i=1}^{n}R\_{\left[1-\beta\_{i}-\beta\_{0},1-\beta\_{i}\right]}(Y\_{i}), |  |

which implies that ∑i=1nESβ0​(Ti)=ESβ0​(∑i=1nTi)=LESβ0​(∑i=1nYi)\sum\_{i=1}^{n}\mathrm{ES}\_{\beta\_{0}}(T\_{i})=\mathrm{ES}\_{\beta\_{0}}(\sum\_{i=1}^{n}T\_{i})=\mathrm{LES}\_{\beta\_{0}}\left(\sum\_{i=1}^{n}Y\_{i}\right). By ∑i=1nESβ0​(Ti)=ESβ0​(∑i=1nTi)\sum\_{i=1}^{n}\mathrm{ES}\_{\beta\_{0}}(T\_{i})=\mathrm{ES}\_{\beta\_{0}}(\sum\_{i=1}^{n}T\_{i}) and by Theorem 5 of Wang and Zitikis ([2021](https://arxiv.org/html/2511.21929v1#bib.bib59)), there exist UTiU\_{T\_{i}}, i∈[n]i\in[n] and U∑i=1nTiU\_{\sum\_{i=1}^{n}T\_{i}} such that {UTi∈[1−β0,1]}={U∑i=1nTi∈[1−β0,1]}\{U\_{T\_{i}}\in[1-\beta\_{0},1]\}=\{U\_{\sum\_{i=1}^{n}T\_{i}}\in[1-\beta\_{0},1]\} for all i∈[n]i\in[n].
Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESβ0​(∑i=1nTi)\displaystyle\mathrm{ES}\_{\beta\_{0}}\left(\sum\_{i=1}^{n}T\_{i}\right) | =1β0​𝔼​(∑i=1nTi​𝟙{UTi∈[1−β0,1]})\displaystyle=\frac{1}{\beta\_{0}}\mathbb{E}\left(\sum\_{i=1}^{n}T\_{i}\mathds{1}\_{\{U\_{T\_{i}}\in\left[1-\beta\_{0},1\right]\}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1β0​𝔼​(∑i=1nYi​𝟙{UTi∈[1−β0,1]})\displaystyle=\frac{1}{\beta\_{0}}\mathbb{E}\left(\sum\_{i=1}^{n}Y\_{i}\mathds{1}\_{\{U\_{T\_{i}}\in\left[1-\beta\_{0},1\right]\}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1β0​𝔼​(Y​𝟙{UTi∈[1−β0,1]})=LESβ0​(Y).\displaystyle=\frac{1}{\beta\_{0}}\mathbb{E}(Y\mathds{1}\_{\{U\_{T\_{i}}\in\left[1-\beta\_{0},1\right]\}})=\mathrm{LES}\_{\beta\_{0}}(Y). |  |

This implies that there exists UYU\_{Y} such that {UY∈[0,β0]}={UTi∈[1−β0,1]}={UYi∈[1−βi−β0,1−βi]}\{U\_{Y}\in[0,\beta\_{0}]\}=\{U\_{T\_{i}}\in[1-\beta\_{0},1]\}=\{U\_{Y\_{i}}\in[1-\beta\_{i}-\beta\_{0},1-\beta\_{i}]\} for all i∈[n]i\in[n]. Note that UX=1−UYU\_{X}=1-U\_{Y} and UXi=1−UYiU\_{X\_{i}}=1-U\_{Y\_{i}}. Hence, we have {UX∈[1−β0,1]}={UXi∈[βi,βi+β0]}\{U\_{X}\in[1-\beta\_{0},1]\}=\{U\_{X\_{i}}\in[\beta\_{i},\beta\_{i}+\beta\_{0}]\} for all i∈[n]i\in[n], which is equivalent to ([5.8](https://arxiv.org/html/2511.21929v1#S5.E8 "In Proposition 6. ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")). We establish the first claim.

Note that ([5.8](https://arxiv.org/html/2511.21929v1#S5.E8 "In Proposition 6. ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) implies ⋃i=1n{UXi∈[0,βi]}⊆{UX∈[0,β]}\bigcup\_{i=1}^{n}\{U\_{X\_{i}}\in[0,\beta\_{i}]\}\subseteq\{U\_{X}\in[0,\beta]\} and ⋃i=1n{UXi∈[βi+β0,1]}⊆{UX∈[0,β]}\bigcup\_{i=1}^{n}\{U\_{X\_{i}}\in[\beta\_{i}+\beta\_{0},1]\}\subseteq\{U\_{X}\in[0,\beta]\}.
Thus, it would be either case (i) or (ii).
For the latter case, i.e., ℙ​({UX∈[0,β]}∖⋃i=1n{UXi∈[0,βi]})>0\mathbb{P}(\{U\_{X}\in[0,\beta]\}\setminus\bigcup\_{i=1}^{n}\{U\_{X\_{i}}\in[0,\beta\_{i}]\})>0, ([5.8](https://arxiv.org/html/2511.21929v1#S5.E8 "In Proposition 6. ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | {UX∈[0,β]}∖⋃i=1n{UXi∈[0,βi]}=⋂i=1n{UXi∈[βi+β0,1]}.\{U\_{X}\in[0,\beta]\}\setminus\bigcup\_{i=1}^{n}\{U\_{X\_{i}}\in[0,\beta\_{i}]\}=\bigcap\_{i=1}^{n}\{U\_{X\_{i}}\in[\beta\_{i}+\beta\_{0},1]\}. |  | (5.9) |

Then, for any ω∈{UX∈[0,β]}∖⋃i=1n{UXi∈[0,βi]}\omega\in\{U\_{X}\in[0,\beta]\}\setminus\bigcup\_{i=1}^{n}\{U\_{X\_{i}}\in[0,\beta\_{i}]\} and any ω′∈{UX∈[β,1]}\omega^{\prime}\in\{U\_{X}\in[\beta,1]\}, it follows from ([5.8](https://arxiv.org/html/2511.21929v1#S5.E8 "In Proposition 6. ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) and ([5.9](https://arxiv.org/html/2511.21929v1#S5.E9 "In 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) that Xi​(ω)⩾Xi​(ω′)X\_{i}(\omega)\geqslant X\_{i}(\omega^{\prime}) holds for all i∈[n]i\in[n]. On the other hand, using ([5.9](https://arxiv.org/html/2511.21929v1#S5.E9 "In 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")), one has that ∑i=1nXi​(ω)⩽∑i=1nXi​(ω′)\sum\_{i=1}^{n}X\_{i}(\omega)\leqslant\sum\_{i=1}^{n}X\_{i}(\omega^{\prime}).
Thus all the above inequalities hold as equalities. By the arbitrariness of ω\omega and ω′\omega^{\prime}, we conclude that random variables X1,…,XnX\_{1},\dots,X\_{n} and XX are all constants on {UX∈[β,1]}∪({UX∈[0,β]}∖⋃i=1n{UXi∈[0,βi]})\{U\_{X}\in[\beta,1]\}\cup(\{U\_{X}\in[0,\beta]\}\setminus\bigcup\_{i=1}^{n}\{U\_{X\_{i}}\in[0,\beta\_{i}]\}). Hence, there exist UX1,…,UXnU\_{X\_{1}},\dots,U\_{X\_{n}} and UXU\_{X} such that case (ii) holds.
∎

In the following Theorem [6](https://arxiv.org/html/2511.21929v1#Thmtheorem6 "Theorem 6 (Non-existence of the optimal allocation). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we show that the optimal allocation for ([5.4](https://arxiv.org/html/2511.21929v1#S5.E4 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) does not exist if XX is not bounded from above, while we find a sequence of allocations {(X1(m),…,Xn(m))}m⩾1\{(X\_{1}^{(m)},\dots,X\_{n}^{(m)})\}\_{m\geqslant 1} such that the sum risk exposure converges to the lower bound R[0,β]​(X)R\_{[0,\beta]}(X).
For m⩾1m\geqslant 1, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xi(m)=(X−m)​𝟙Ai+Xn​𝟙Ac+mn−1​𝟙A∖Ai,i∈[n],\displaystyle X\_{i}^{(m)}=\left(X-m\right)\mathds{1}\_{A\_{i}}+\frac{X}{n}\mathds{1}\_{A^{c}}+\frac{m}{n-1}\mathds{1}\_{A\setminus A\_{i}},~~i\in[n], |  | (5.10) |

where A={UX⩽β}A=\{U\_{X}\leqslant\beta\} and (A1,…,An)(A\_{1},\dots,A\_{n}) being a partition of AA satisfying ℙ​(Ai)=βi\mathbb{P}(A\_{i})=\beta\_{i} for all i∈[n]i\in[n].

###### Theorem 6 (Non-existence of the optimal allocation).

For X∈𝒳1X\in\mathcal{X}\_{1} and 𝛃∈(0,1)n\boldsymbol{\beta}\in(0,1)^{n} satisfying β∈(0,1)\beta\in(0,1), if XX is not bounded from above, then

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nRIi​(Xi)>R[0,β]​(X)\sum\_{i=1}^{n}R\_{I\_{i}}\left(X\_{i}\right)>R\_{[0,\beta]}(X) |  |

holds for all (X1,…,Xn)∈𝔸n​(X)\left(X\_{1},\ldots,X\_{n}\right)\in\mathbb{A}\_{n}(X).
Moreover, the risk allocation (X1(m),…,Xn(m))∈𝔸n​(X)\left(X\_{1}^{(m)},\dots,X\_{n}^{(m)}\right)\in\mathbb{A}\_{n}(X), with m⩾1m\geqslant 1, defined in ([5.10](https://arxiv.org/html/2511.21929v1#S5.E10 "In 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) satisfies

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nRIi​(Xi(m))=R[0,β]​(X)+1β​𝔼​((X−am)​𝟙{X>am})\sum\_{i=1}^{n}R\_{I\_{i}}(X\_{i}^{(m)})=R\_{[0,\beta]}(X)+\frac{1}{\beta}\mathbb{E}((X-a\_{m})\mathds{1}\_{\{X>a\_{m}\}}) |  |

for m⩾(qβ−​(X)∨⋁i=1nq1−β+βi​(X))+m\geqslant(q\_{\beta}^{-}(X)\vee\bigvee\_{i=1}^{n}q\_{1-\beta+\beta\_{i}}(X))\_{+} with am=n​mn−1a\_{m}=\frac{nm}{n-1}, and

|  |  |  |
| --- | --- | --- |
|  | limm→∞∑i=1nRIi​(Xi(m))=R[0,β]​(X).\lim\_{m\to\infty}\sum\_{i=1}^{n}R\_{I\_{i}}(X\_{i}^{(m)})=R\_{[0,\beta]}\left(X\right). |  |

###### Proof.

Suppose that the total risk XX is not bounded from above and that the equality ([5.4](https://arxiv.org/html/2511.21929v1#S5.E4 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) holds for a risk allocation
(X1,…,Xn)∈𝔸n​(X)\left(X\_{1},\ldots,X\_{n}\right)\in\mathbb{A}\_{n}(X). Then, by Proposition [6](https://arxiv.org/html/2511.21929v1#Thmproposition6 "Proposition 6. ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), with β0=1−β\beta\_{0}=1-\beta,
there exist UXiU\_{X\_{i}}, i∈[n]i\in[n] and UXU\_{X} such that

|  |  |  |
| --- | --- | --- |
|  | {UX∈[0,β]}={UXi∈Ii},i∈[n],\{U\_{X}\in[0,\beta]\}=\{U\_{X\_{i}}\in I\_{i}\},\quad i\in[n], |  |

which is equivalent to

|  |  |  |
| --- | --- | --- |
|  | {UX∈[β,1]}={UXi∈[βi,1−β+βi]},i∈[n].\{U\_{X}\in[\beta,1]\}=\{U\_{X\_{i}}\in[\beta\_{i},1-\beta+\beta\_{i}]\},\quad i\in[n]. |  |

Then we have

|  |  |  |
| --- | --- | --- |
|  | ∞=ess​-​sup​X​𝟙{UX∈[β,1]}=ess​-​sup​∑i=1nXi​𝟙{UXi∈[βi,1−β+βi]}⩽∑i=1nq1−β+βi−​(Xi)<∞,\infty=\mathrm{ess\mbox{-}sup}X\mathds{1}\_{\{U\_{X}\in[\beta,1]\}}=\mathrm{ess\mbox{-}sup}\sum\_{i=1}^{n}X\_{i}\mathds{1}\_{\{U\_{X\_{i}}\in[\beta\_{i},1-\beta+\beta\_{i}]\}}\leqslant\sum\_{i=1}^{n}q\_{1-\beta+\beta\_{i}}^{-}(X\_{i})<\infty, |  |

which leads to a contradiction. Hence, there is no solution for ([5.4](https://arxiv.org/html/2511.21929v1#S5.E4 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) if XX is unbounded from above.

Next, we focus on the second statment. For m⩾(qβ−​(X)∨⋁i=1nq1−β+βi​(X))+m\geqslant(q\_{\beta}^{-}(X)\vee\bigvee\_{i=1}^{n}q\_{1-\beta+\beta\_{i}}(X))\_{+}, direct computation shows

|  |  |  |
| --- | --- | --- |
|  | RIi​(Xi(m))=1β​𝔼​((X−m)​𝟙Ai+(Xn∨mn−1)​𝟙{UX>1−β+βi}),i∈[n].\displaystyle R\_{I\_{i}}(X\_{i}^{(m)})=\frac{1}{\beta}\mathbb{E}\left((X-m)\mathds{1}\_{A\_{i}}+\left(\frac{X}{n}\vee\frac{m}{n-1}\right)\mathds{1}\_{\{U\_{X}>1-\beta+\beta\_{i}\}}\right),~i\in[n]. |  |

Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nRIi​(Xi(m))\displaystyle\sum\_{i=1}^{n}R\_{I\_{i}}(X\_{i}^{(m)}) | =1β​𝔼​((X−m)​𝟙A+(Xn∨mn−1)​∑i=1n𝟙{UX>1−β+βi})\displaystyle=\frac{1}{\beta}\mathbb{E}\left((X-m)\mathds{1}\_{A}+\left(\frac{X}{n}\vee\frac{m}{n-1}\right)\sum\_{i=1}^{n}\mathds{1}\_{\{U\_{X}>1-\beta+\beta\_{i}\}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =R[0,β]​(X)−m+1β​∑i=1n(𝔼​(Xn​𝟙{X>am})+mn−1​(β−βi−ℙ​(X>am)))\displaystyle=R\_{[0,\beta]}(X)-m+\frac{1}{\beta}\sum\_{i=1}^{n}\left(\mathbb{E}\left(\frac{X}{n}\mathds{1}\_{\{X>a\_{m}\}}\right)+\frac{m}{n-1}(\beta-\beta\_{i}-\mathbb{P}(X>a\_{m}))\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =R[0,β]​(X)+1β​𝔼​(X​𝟙{X>am})−amβ​ℙ​(X>am),\displaystyle=R\_{[0,\beta]}(X)+\frac{1}{\beta}\mathbb{E}\left(X\mathds{1}\_{\{X>a\_{m}\}}\right)-\frac{a\_{m}}{\beta}\mathbb{P}(X>a\_{m}), |  |

where am=n​mn−1a\_{m}=\frac{nm}{n-1}.
Note that amℙ(X>am)⩽𝔼(X𝟙{X>am})→0a\_{m}\mathbb{P}(X>a\_{m})\leqslant\mathbb{E}(X\mathds{1}\_{\{X>a\_{m}\})}\to 0 as m→∞m\to\infty. Hence, we have

|  |  |  |
| --- | --- | --- |
|  | limm→∞∑i=1nRIi​(Xi(m))=R[0,β]​(X).\lim\_{m\to\infty}\sum\_{i=1}^{n}R\_{I\_{i}}(X\_{i}^{(m)})=R\_{[0,\beta]}(X). |  |

This completes the proofs.
∎

In light of Theorems [5](https://arxiv.org/html/2511.21929v1#Thmtheorem5 "Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") and [6](https://arxiv.org/html/2511.21929v1#Thmtheorem6 "Theorem 6 (Non-existence of the optimal allocation). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we obtain the following results on risk sharing for distortion risk measures with special inverse S-shaped distortion functions.

###### Proposition 7.

For X∈𝒳1X\in\mathcal{X}\_{1} and 𝛃∈(0,1)n\boldsymbol{\beta}\in(0,1)^{n} satisfying β∈(0,1)\beta\in(0,1) and λ∈(0,1)\lambda\in(0,1), we have

|  |  |  |
| --- | --- | --- |
|  | □i=1nρgλ,i​(X)=λ​𝔼​(X)+(1−λ)​R[0,β]​(X).\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{g\_{\lambda,i}}(X)=\lambda\mathbb{E}(X)+(1-\lambda)R\_{[0,\beta]}(X). |  |

Moreover, if XX is bounded from above, an optimal allocation is given by ([5.5](https://arxiv.org/html/2511.21929v1#S5.E5 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")); if XX is not bounded from above, the optimal allocation does not exist and the risk allocation (X1(m),…,Xn(m))∈𝔸n​(X)\left(X\_{1}^{(m)},\dots,X\_{n}^{(m)}\right)\in\mathbb{A}\_{n}(X), with m⩾1m\geqslant 1, defined in ([5.10](https://arxiv.org/html/2511.21929v1#S5.E10 "In 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) satisfies

|  |  |  |
| --- | --- | --- |
|  | limm→∞∑i=1nρgλ,i​(Xi(m))=□i=1nρgλ,i​(X).\lim\_{m\to\infty}\sum\_{i=1}^{n}\rho\_{g\_{\lambda,i}}\left(X\_{i}^{(m)}\right)=\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{g\_{\lambda,i}}(X). |  |

Proposition [7](https://arxiv.org/html/2511.21929v1#Thmproposition7 "Proposition 7. ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") shows that the Pareto-optimal risk allocation for ρgλ,i\rho\_{g\_{\lambda,i}} is the combination of comonotonic risk sharing for large losses and counter-monotonic risk sharing for small losses or large gains, consistent with the risk preference represented by ρgλ,i\rho\_{g\_{\lambda,i}}: risk aversion for large losses and risk-seeking for small losses or large gains. Finding the optimal risk sharing for distortion risk measures with inverse S-shaped distortion functions is a very challenging problem due to the non-convexity of the corresponding distortion risk measures. Although Proposition [7](https://arxiv.org/html/2511.21929v1#Thmproposition7 "Proposition 7. ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") only solves a special case, to the best of our knowledge, it is the first result offering the optimal allocations for the non-constrained risk sharing with this class of distortion risk measures with its distortion functions exaggerating the probabilities of large losses and large gains simultaneously. This can be seen from the novelty of the optimal allocations and the condition for the existence of the optimal allocations.
Proposition [7](https://arxiv.org/html/2511.21929v1#Thmproposition7 "Proposition 7. ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") suggests that the optimal allocation exists if and only if XX is bounded from above. However, the risk sharing for distortion risk measures with general inverse S-shaped distortion functions is still unknown and will be studied in future.

Note that our result in Theorem [5](https://arxiv.org/html/2511.21929v1#Thmtheorem5 "Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") solves the dual problem of the one in Theorem 2 of Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20)).
We observe

|  |  |  |  |
| --- | --- | --- | --- |
|  | □i=1nRIi​(X)\displaystyle\mathop{\square}\displaylimits\_{i=1}^{n}R\_{I\_{i}}(X) | =inf{∑i=1nRIi​(Xi):(X1,…,Xn)∈𝔸n​(X)}\displaystyle=\inf\left\{\sum\_{i=1}^{n}R\_{I\_{i}}(X\_{i}):(X\_{1},\dots,X\_{n})\in\mathbb{A}\_{n}(X)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =inf{∑i=1n(𝔼​(Xi)β−1−ββ​R[βi,1−β+βi]​(Xi)):(X1,…,Xn)∈𝔸n​(X)}\displaystyle=\inf\left\{\sum\_{i=1}^{n}\left(\frac{\mathbb{E}(X\_{i})}{\beta}-\frac{1-\beta}{\beta}R\_{[\beta\_{i},1-\beta+\beta\_{i}]}(X\_{i})\right):(X\_{1},\dots,X\_{n})\in\mathbb{A}\_{n}(X)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​(X)β−1−ββ​sup{∑i=1nR[βi,1−β+βi]​(Xi):(X1,…,Xn)∈𝔸n​(X)}.\displaystyle=\frac{\mathbb{E}(X)}{\beta}-\frac{1-\beta}{\beta}\sup\left\{\sum\_{i=1}^{n}R\_{[\beta\_{i},1-\beta+\beta\_{i}]}(X\_{i}):(X\_{1},\dots,X\_{n})\in\mathbb{A}\_{n}(X)\right\}. |  |

Hence, the optimal allocation for □i=1nRIi​(X)\mathop{\square}\displaylimits\_{i=1}^{n}R\_{I\_{i}}(X) is the worst allocation for ∑i=1nR[βi,1−β+βi]​(Xi)\sum\_{i=1}^{n}R\_{[\beta\_{i},1-\beta+\beta\_{i}]}(X\_{i}) with (X1,…,Xn)∈𝔸n​(X)(X\_{1},\dots,X\_{n})\in\mathbb{A}\_{n}(X). Using Theorems [5](https://arxiv.org/html/2511.21929v1#Thmtheorem5 "Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing") and [6](https://arxiv.org/html/2511.21929v1#Thmtheorem6 "Theorem 6 (Non-existence of the optimal allocation). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing"), we have the following conclusion.

###### Proposition 8.

For X∈𝒳1X\in\mathcal{X}\_{1} and 𝛃∈(0,1)n\boldsymbol{\beta}\in(0,1)^{n} satisfying β∈(0,1)\beta\in(0,1), we have

|  |  |  |
| --- | --- | --- |
|  | sup{∑i=1nR[βi,1−β+βi]​(Xi):(X1,…,Xn)∈𝔸n​(X)}=𝔼​(X)−β​R[0,β]​(X)1−β=R[β,1]​(X).\sup\left\{\sum\_{i=1}^{n}R\_{[\beta\_{i},1-\beta+\beta\_{i}]}(X\_{i}):(X\_{1},\dots,X\_{n})\in\mathbb{A}\_{n}(X)\right\}=\frac{\mathbb{E}(X)-\beta R\_{[0,\beta]}(X)}{1-\beta}=R\_{[\beta,1]}(X). |  |

Moreover, if XX is bounded from above, an allocation given by ([5.5](https://arxiv.org/html/2511.21929v1#S5.E5 "In Theorem 5 (Risk sharing for the average quantile). ‣ 5 Risk Sharing ‣ Extended Convolution Bounds on the Fréchet Problem: Robust Risk Aggregation and Risk Sharing")) achieves the supremum; if XX is not bounded from above, no allocation can achieve the supremum.

## 6 Conclusion

In this paper, we obtain a new RVaR\mathrm{RVaR} inequality, differing from the one in Embrechts et al. ([2018](https://arxiv.org/html/2511.21929v1#bib.bib20)). Applying this new inequality, we obtain the upper and lower bounds for robust RVaR\mathrm{RVaR} by assuming fixed marginal distributions and unknown dependence structure, which is sharp if the marginal distributions have increasing densities on their upper-tail parts for the upper bounds and if the marginal distributions have decreasing densities on their upper-tail part for the lower bounds. Those bounds complement the results and fill in some gaps of Blanchet et al. ([2025](https://arxiv.org/html/2511.21929v1#bib.bib8)). Moreover, we obtain the sharp upper bounds for the difference between two RVaR\mathrm{RVaR} and the difference between two quantiles, extending the sharp bounds on RVaR\mathrm{RVaR} and quantiles to the corresponding variability risk measures. The application of those extended convolution bounds in portfolio optimization and optimal insurance and reinsurance is left for future investigation.
Finally, applying the new inequality, we obtain the Pareto-optimal risk allocation for some non-convex averaged quantiles, which corresponds to the Pareto-optimal risk allocation for distortion risk measures with special inverse S-shaped distortion functions exaggerating both the probability of large losses and the probability of large gains. By analyzing the dependence structure of the optimal risk allocation, we show that the optimal allocation does not exist if the risk is unbounded from above. However, we offer a sequence of allocations whose aggregate risk exposure converges to the inf-convolution. The Pareto-optimal risk sharing for distortion risk measures with general inverse S-shaped distortion functions is still an open problem due to the non-convexity nature of the distortion risk measures.

#### Acknowledgement

The authors are grateful to Ruodu Wang and members of the research group on financial mathematics and risk management at The Chinese University of Hong Kong, Shenzhen for their useful feedback and conversations.
Y. Liu acknowledges financial support from the National Natural Science Foundation of China (Grant No. 12401624), The Chinese University of Hong Kong (Shenzhen) University Development Fund (Grant No. UDF01003336) and Shenzhen Science and Technology Program (Grant No. RCBS20231211090814028, JCYJ20250604141203005, 2025TC0010) and is partly supported by the Guangdong Provincial Key Laboratory of Mathematical Foundations for Artificial Intelligence (Grant No. 2023B1212010001).

## References

* Altschuler and Boix-Adserà (2021)
   Altschuler, J. M. and Boix-Adserà, E. (2021). Hardness results for multimarginal optimal transport problems. *Discrete Optimization*, 42, 100669.
* Artzner et al. (1999)

  Artzner, P., Delbaen, F., Eber, J.-M. and Heath, D. (1999). Coherent measures of risk. *Mathematical Finance*, 9(3), 203–228.
* Barrieu and El Karoui (2005)

  Barrieu, P. and El Karoui, N. (2005). Inf-convolution of risk measures and optimal risk transfer. *Finance and
  Stochastics*, 9, 269–298.
* Bartl et al. (2022)

  Bartl, D., Kupper, M., Lux, T. and Papapantoleon, A. (2022). Marginal and dependence uncertainty: bounds, optimal transport, and sharpness. *SIAM Journal on Control and Optimization*, 60(1), 410–434.
* Bellini et al. (2022)

  Bellini, F., Fadina, T., Wang, R. and Wei, Y. (2022). Parametric measures of variability induced by risk
  measures. *Insurance: Mathematics and Economics*, 106, 270–284.
* Bernard et al. (2014)

  Bernard, C., Jiang, X. and Wang, R. (2014). Risk aggregation with dependence uncertainty. *Insurance: Mathematics and Economics*, 54, 93–108.
* Bertsimas et al. (2011)
   Bertsimas, D., Brown, D. B. and Caramanis, C. (2011). Theory and applications of robust optimization. SIAM Review, 53(3), 464–501.
* Blanchet et al. (2025)
   Blanchet, J., Lam, H.,
  Liu, Y. and Wang, R. (2025). Convolution bounds on quantile aggregation. *Operations Research*, 73(5), 2761–2781.
* Boerma et al. (2023)

  Boerma, J., Tsyvinski, A., Wang, R. and Zhang, Z. (2023). Composite sorting. *arXiv*: 2303.06701.
* Boudt et al. (2018)
  Boudt, K., Jakobsons, E., and Vanduffel, S. (2018). Block rearranging elements within matrix columns to minimize the variability of the row sums. *4OR - A Quarterly Journal of Operations Research*, 16, 31–50.
* Borch (1962)
   Borch, K. (1962). Equilibrium in a reinsurance market. Econometrica, 30(3), 424–444.
* Chen et al. (2022)

  Chen, Y., Liu, P., Liu, Y. and Wang, R. (2022). Ordering and inequalities for mixtures on risk aggregation. *Mathematical Finance*, 32, 421–451.
* Cherny and Madan (2009)

  Cherny, A. S. and Madan, D. (2009). New measures for performance evaluation. *Review of Financial Studies*, 22(7), 2571–2606.
* Cont et al. (2010)

  Cont, R., Deguest, R. and Scandolo, G. (2010). Robustness and sensitivity analysis of risk measurement procedures. *Quantitative Finance*, 10, 593–606.
* Dall’Aglio (1956)

  Dall’Aglio, G. (1956).
  Sugli estremi dei momenti delle funzioni di ripartizione doppia.
  Annali della Scuola Normale Superiore di Pisa, Serie 3, 10, 35–74.
* Delbaen (2012)

  Delbaen, F. (2012).
  Monetary Utility Functions.
  Osaka University Press, Osaka.
* Dhaene and Denuit (1999)

  Dhaene, J. and Denuit, M. (1999). The safest dependence structure among risks. *Insurance: Mathematics and Economics*, 25(1), 11–21.
* Dhaene et al. (2002)

  Dhaene, J., Denuit, M., Goovaerts, M. J., Kaas, R. and Vyncke, D. (2002). The concept of comonotonicity in actuarial science and finance: Theory. *Insurance: Mathematics and Economics*, 31(1), 3–33.
* Eckstein et al. (2020)

  Eckstein, S., Kupper, M. and Pohl, M. (2020). Robust risk aggregation with neural networks. *Mathematical Finance*, 30(4), 1229–1272.
* Embrechts et al. (2018)

  Embrechts, P., Liu, H. and Wang, R. (2018). Quantile-based risk sharing. *Operations Research*, 66(4), 936–949.
* Embrechts et al. (2020)

  Embrechts, P., Liu, H., Mao, T. and Wang, R. (2020). Quantile-based risk sharing with heterogeneous beliefs. *Mathematical Programming Series B*, 181(2), 319-347.
* Embrechts and Puccetti (2006)
   Embrechts, P. and Puccetti, G. (2006). Bounds for functions of dependent risks. *Finance and Stochastics*, 10, 341–352.
* Embrechts et al. (2013)
   Embrechts, P., Puccetti, G. and Rüschendorf, L. (2013). Model uncertainty and VaR aggregation. Journal of Banking and Finance, 37(8), 2750–2764.
* Embrechts et al. (2015)
   Embrechts, P., Wang, B. and Wang, R. (2015). Aggregation-robustness and model uncertainty of regulatory risk measures. *Finance and Stochastics*, 19(4), 763–790.
* Fadina et al. (2025)

  Fadina, T., Hu, J., Liu, P., and Xia, Y. (2025). Optimal reinsurance with multivariate risks and dependence uncertainty. *European Journal of Operational Research*, 321(1), 231–242.
* Filipović and Svindland (2008)

  Filipović, D. and Svindland, G. (2008). Optimal capital and risk allocations for law- and cash-invariant convex functions.  *Finance and Stochastics*, 12, 423–439.
* Föllmer and Schied (2002)
   Föllmer, H. and Schied, A. (2002). Convex measures of risk and trading constraints. *Finance and Stochastics*, 6(4) 429–447.
* Föllmer and Schied (2016)
   Föllmer, H. and Schied, A. (2016). Stochastic Finance. An Introduction in Discrete Time. Walter de Gruyter, Berlin, Fourth Edition.
* Fréchet (1951)

  Fréchet, M. (1951).
  Sur les tableaux de corrélation dont les marges sont données.
  Annales de l’Université de Lyon. Sect. A, 14, 53–77.
* Frittelli and Rosazza Gianin (2005)

  Frittelli, M. and Rosazza Gianin, E. (2005). Law-invariant convex risk measures. *Advances in Mathematical
  Economics*, 7, 33–46.
* Hoeffding (1940)

  Hoeffding, V. (1940).
  Masstabinvariante Korrelationstheorie.
  Schriften des Mathematischen Instituts und des Instituts für
  Angewandte Mathematik der Universität Berlin, 5, 181–233.
* Hsu (1984)

  Hsu, W.-L. (1984). Approximation algorithms for the assembly line crew scheduling problem. *Mathematics of Operations Research*, 9(3), 376–383.
* Jakobsons et al. (2016)

  Jakobsons, E., Han, X. and Wang, R. (2016). General convex order on risk aggregation. *Scandinavian Actuarial Journal*, 2016(8), 713–740.
* Jouini et al. (2008)
   Jouini, E., Schachermayer, W. and Touzi, N. (2008). Optimal risk sharing for law invariant monetary utility functions. *Mathematical Finance*, 18(2), 269–292.
* Koike et al. (2024)
   Koike, T., Lin, L. and Wang, R. (2024). Joint mixability and notions of negative dependence. *Mathematics of Operations Research*,
  49(4), 2786–2802.
* Kremer (1993)
   Kremer, M. (1993). The O-Ring theory of economic development. Quarterly Journal of Economics, 108(3), 551–575.
* Lauzier et al. (2023)

  Lauzier, J.G., Lin, L. and Wang, R. (2023). Pairwise counter-monotonicity. *Insurance:
  Mathematics and Economics*, 111, 279–287.
* Lauzier et al. (2025)

  Lauzier, J.G., Lin, L. and Wang, R. (2025).
  Risk sharing, measuring variability, and distortion riskmetrics. *Mathematical Finance*, forthcoming.
* Liebrich (2024)

  Liebrich, F.B. (2024). Risk sharing under heterogeneous beliefs without convexity. *Finance and Stochastics*, 28, 999–1033.
* Liu et al. (2022)

  Liu, F., Mao, T., Wang, R. and Wei, L. (2022). Inf-convolution, optimal allocations, and model uncertainty for tail risk measures. *Mathematics of Operations Research*, 47(3), 2494–2519.
* Liu and Wang (2021)

  Liu, F. and Wang, R. (2021). A theory for measures of tail risk. *Mathematics of Operations Research*, 46(3), 1109–1128.
* Liu (2025)

  Liu, P. (2025). Risk sharing with Lambda value at risk. *Mathematics of Operations Research*, 50(1), 313-333.
* Makarov (1981)

  Makarov, G. (1981). Estimates for the distribution function of a sum of two random variables when the marginal distributions are fixed. *Theory of Probability and Its Applications*, 26, 803–806.
* McNeil et al. (2015)

  McNeil, A. J., Frey, R. and Embrechts, P. (2015). Quantitative
  Risk Management: Concepts, Techniques and Tools. Revised Edition. Princeton, NJ:
  Princeton University Press.
* Nutz and Wang (2022)
   Nutz, M. and Wang, R. (2022). The directional optimal transport. *Annals of Applied Probability*, 32(2), 1400–1420.
* Pflug and Pohl (2018)

  Pflug, G. C. and Pohl, M. (2018). A review on ambiguity in stochastic portfolio optimization.
  *Set-Valued and Variational Analysis*, 26, 733–757.
* Puccetti and Rüschendorf (2012)

  Puccetti, G. and Rüschendorf L. (2012). Computation of sharp bounds on the distribution of a function of dependent risks. *Journal of Computational and Applied Mathematics*, 236(7), 1833-1840.
* Puccetti and
  Wang (2015)

  Puccetti, G. and Wang R. (2015).
  Extremal dependence concepts.
  *Statistical Science*, 30(4), 485–517.
* Rockafellar and Uryasev (2002)

  Rockafellar, R. T. and Uryasev, S. (2002). Conditional value-at-risk for general loss distributions. *Journal of
  Banking and Finance*, 26(7), 1443–1471.
* Rüschendorf (1982)

  Rüschendorf, L. (1982).
  Random variables with maximum sums.
  Advances in Applied Probability, 14, 623–632.
* Rüschendorf (2013)

  Rüschendorf, L. (2013).
  Mathematical Risk Analysis. Springer Series in Operations Research and Financial Engineering,
  Springer-Verlag Berlin Heidelberg.
* Shapiro et al. (2021)

  Shapiro, A., Dentcheva, D. and Ruszczynski, A. (2021). *Lectures on Stochastic Programming: Modeling and Theory*. Society for Industrial and Applied Mathematics.
* Tversky and Kahneman (1992)

  Tversky, A. and Kahneman, E. (1992). Advances in prospect theory: cumulative representation
  of uncertainty. *Journal of Risk and Uncertainty*, 5, 297-323.
* Vovk et al. (2022)
   Vovk, V., Wang, B. and Wang, R. (2022). Admissible ways of merging p-values under arbitrary dependence. *Annals of Statistics*, 50(1), 351–375.
* Wang (1996)

  Wang, S. (1996). Premium calculation by transforming the layer premium density. *ASTIN Bulletin*, 26(1), 71–92.
* Wang (2000)

  Wang, S. (2000). A class of distortion operators for pricing financial and insurance risks. *Journal of Risk and Insurance*, 67, 15–36.
* Wang et al. (2013)

  Wang, R., Peng, L. and Yang, J. (2013).
  Bounds for the sum of dependent risks and worst Value-at-Risk with
  monotone marginal densities.
  Finance and Stochastics, 17(2), 395–417.
* Wang and Wang (2016)

  Wang, B. and Wang, R. (2016).
  Joint mixability. *Mathematics of Operations Research*, 41(3), 808–826.
* Wang and Zitikis (2021)

  Wang, R. and Zitikis, R. (2020). An axiomatic foundation for the Expected Shortfall.
  *Management Science*, 67(3), 1413-1429.
* Weber (2018)
   Weber, S. (2018). Solvency II, or how to sweep the downside risk under the carpet. *Insurance: Mathematics and Economics*, 82, 191–200.
* Yaari (1987)

  Yaari, M. E. (1987). The dual theory of choice under risk. *Econometrica*, 55(1), 95-115.