---
authors:
- Peng Liu
- Steven Vanduffel
- Yi Xia
doc_id: arxiv:2511.08662v1
family_id: arxiv:2511.08662
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Robust distortion risk metrics and portfolio optimization
url_abs: http://arxiv.org/abs/2511.08662v1
url_html: https://arxiv.org/html/2511.08662v1
venue: arXiv q-fin
version: 1
year: 2025
---


Peng Liu
Department of Mathematics, Statistics and Actuarial Science, University of Essex, UK. Email: peng.liu@essex.ac.uk
  
Steven Vanduffel
Department of Economics and Political Science, Vrije Universiteit Brussel, Belgium. Email: Steven.Vanduffel@vub.be
  
Yi Xia
Department of Mathematics, Statistics and Actuarial Science, University of Essex, UK. Email: yx21416@essex.ac.uk

(November 11, 2025)

###### Abstract

We establish sharp upper and lower bounds for distortion risk metrics under distributional uncertainty. The uncertainty sets are
characterized by four key features of the underlying
distribution: mean, variance, unimodality, and Wasserstein distance to a reference distribution.

We first examine very general distortion risk metrics, assuming only finite variation for the underlying distortion function and without requiring continuity or monotonicity. This broad framework includes notable distortion risk metrics such as range value-at-risk, glue value-at-risk, Gini deviation, mean-median deviation and inter-quantile difference. In this setting, when the uncertainty set is characterized by a fixed mean, variance and a Wasserstein distance, we determine both the worst- and best-case values of a given distortion risk metric and identify the corresponding extremal distribution. When the uncertainty set is further constrained by unimodality with a fixed inflection point, we establish for the case of absolutely continuous distortion functions the extremal values
along with their respective extremal distributions.

We apply our results to robust portfolio optimization and model risk assessment offering improved decision-making under model uncertainty.

Key-words: Robust distortion risk metrics; Mean-variance; Wasserstein metrics; Unimodality; Portfolio optimization.

## 1 Introduction

In traditional decision-making frameworks, a decision-maker assumes a known distribution function FF for the random variable XX at hand, and uses a law-invariant functional 𝒱\mathcal{V} such as variance, expected (dis)utility or value-at-risk to assess the risk V​(X):=V​(F)V(X):=V(F). This approach, however, relies heavily on the correctness of a single probabilistic model, and it is well understood that it may lead to poor decisions if the true probabilities are uncertain or misspecified. As a result, the question of how to account for distributional ambiguity in decision making has become a central concern in a number of fields, including economics, finance, engineering and operations research. A major modeling paradigm to address ambiguity is distributionally robust optimization (DRO). In its standard form, DRO amounts to dealing with a problem of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | minθ∈Θ⁡maxF𝐗∈ℱ⁡𝒱​(f​(θ,𝐗)).\displaystyle\min\_{{\mathbf{\theta}}\in\Theta}\max\_{F\_{{\mathbf{X}}}\in\mathcal{F}}\mathcal{V}(f({{\mathbf{\theta}}},\mathbf{X})). |  | (1) |

Here, ff is a loss function, θ\theta reflects a decision vector (e.g., weights), F𝐗F\_{\mathbf{X}} is an admissible distribution function for a given risk vector 𝐗\mathbf{X} and ℱ\mathcal{F} is the uncertainty set containing all admissible distribution functions. A DRO thus reflects the basic idea that one aims to make decisions that perform optimal under worst-case scenarios. In this paper, we contribute to the literature by solving for uncertainty sets that are reflective for real world ambiguity the inner max problem for a very broad class of decision functionals 𝒱\mathcal{V} that have been used in real-world decision making. We apply the results to deal with novel robust portfolio selection problems that are of high practical interest.

The min-max formulation for optimal decision making under ambiguity appears to find its pedigree in Scarf ([1958](https://arxiv.org/html/2511.08662v1#bib.bib34)), who studied the newsvendor problem under distributional ambiguity of the demand function. Its theoretical appeal stems from the axiomatisation of Gilboa and Schmeidler ([1987](https://arxiv.org/html/2511.08662v1#bib.bib20)) for the case of expected utility under ambiguity, where choices are based on the worst-case expected utility over a set of plausible probability distributions; see also Hansen and Sargent ([2001](https://arxiv.org/html/2511.08662v1#bib.bib22)) who propose the min-max formulation for robust control problems. The arrival of modern robust optimization techniques in the last decade, see e.g., Ben-Tal et al. ([2009](https://arxiv.org/html/2511.08662v1#bib.bib5)) has further contributed to the successful application of DROs in various areas including engineering, finance, operations research and economics.

As for the choice of the decision functional 𝒱\mathcal{V}, adopting the expected (dis)utility framework appears to be the most natural choice given its prominent place in the academic literature. There are however a series of shortcomings to its use (Starmer ([2000](https://arxiv.org/html/2511.08662v1#bib.bib38))). First, it is not obvious at all for a decision maker to specify his utility function. In the context of optimal portfolio strategies, Brennan and Solanki ([1981](https://arxiv.org/html/2511.08662v1#bib.bib11)) point out that “from a practical
point of view, it may well prove easier for the investor to choose directly his optimal
quantile function than it would be for him to communicate his utility function to a portfolio manager.” The same observation has led Goldstein et al. ([2008](https://arxiv.org/html/2511.08662v1#bib.bib21)) to introduce a tool, called the distribution builder, which makes it possible for investors to analyse their desired payoff function and to elicit a utility to explain their choice. Second, there is ample empirical evidence that real world decision making cannot be reconciled with the use of utility functions (e.g., Allais ([1953](https://arxiv.org/html/2511.08662v1#bib.bib1))). In response to this criticism, numerous alternatives, such as Yaari’s dual theory
(Yaari ([1987](https://arxiv.org/html/2511.08662v1#bib.bib43))), rank-dependent utility theory (Quiggin ([1982](https://arxiv.org/html/2511.08662v1#bib.bib32))) and cumulative prospect theory (Tversky and Kahneman ([1992](https://arxiv.org/html/2511.08662v1#bib.bib40))), have been proposed.

All these theories have been justified by proposing axioms that are considered “sensible.” While providing a prescriptive foundation for a decision theory—as a practical guide to making choices—is important, the real issue lies in understanding how people actually choose, and observed real-world behavior should not be dismissed simply because it violates conventional choice axioms (Starmer ([2000](https://arxiv.org/html/2511.08662v1#bib.bib38))).
In this context, Yaari’s dual theory has a lot of appeal, because it aligns more closely with observed decision-making behavior. Indeed, this theory gives rise to quantile based functionals, called distortion risk measures, such as value-at-risk (VaR), range value at risk (RVaR), tail value at risk (TVaR), all of which are actually used in real world decision making with the main reason being that they are reflecting the human tendency to ask questions like “What if this happens?” or “What would I lose under this scenario111Roese and Olson ([1995](https://arxiv.org/html/2511.08662v1#bib.bib33)) attribute this to mental simulation and counterfactual thinking. That is, people naturally engage in mental simulations of (extreme) events, imagining what could happen in those scenarios; see also Tversky and Kahneman Tversky and Kahneman ([1973](https://arxiv.org/html/2511.08662v1#bib.bib39)) who explain this behaviour because extreme events are more memorable.?” Our set-up is however broader in that we do not require the distortion function to be non-decreasing. This makes it possible to extend the scope and to also include the inter quartile range (IQR), the Gini deviation (GD), the mean-median deviation or the difference of two distortion risk measures in our framework. Specifically, the functionals that we consider are labeled distortion risk metrics222In the paper of Wang et al. ([2020](https://arxiv.org/html/2511.08662v1#bib.bib41)), they are called distortion riskmetrics, which is slightly different from ours. and will be denoted by ρg\rho\_{g} where gg reflects the underlying distortion function. They were first proposed in Wang et al. ([2020](https://arxiv.org/html/2511.08662v1#bib.bib42)).

We are not the first to pursue DRO using distortion risk measures and its generalization distortion risk metrics. This was first done by Ben-Tal et al. ([2009](https://arxiv.org/html/2511.08662v1#bib.bib5)) for the case of VaR, further extended in Chen et al. ([2011](https://arxiv.org/html/2511.08662v1#bib.bib14)) to include the the case of TVaR, and then significantly generalized by Li ([2018](https://arxiv.org/html/2511.08662v1#bib.bib24)) to the entire class of convex distortion risk measures, and by Cai et al. ([2025](https://arxiv.org/html/2511.08662v1#bib.bib13)) to general distortion risk measures. In all these works the ambiguity set ℱ\mathcal{F} is characterized by the mean and covariance matrix of the random vector 𝐗\mathbf{X}.

To deal with a DRO, one needs to first solve an inner problem of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxFY∈ℱ~⁡ρg​(Y).\displaystyle\max\_{F\_{{{Y}}}\in\widetilde{\mathcal{F}}}\rho\_{g}({Y}). |  | (2) |

Problem [2](https://arxiv.org/html/2511.08662v1#S1.E2 "In 1 Introduction ‣ Robust distortion risk metrics and portfolio optimization") specifically deals with the extent to which measurements can be affected by model misspecification. This problem is of particular relevance in statistics—where it has been studied under the notion of robust statistics—and in the financial industry, where the assessment of model uncertainty became a regulatory priority in the aftermath of the 2008–2009 financial crisis. For instance, in February 2017, the European Central Bank published its Guide to the Targeted Review of Internal Models, in which it declared that every institution “should have a model risk management framework in place that allows it to identify, understand, and manage its model risk” (European Central Bank ([2017](https://arxiv.org/html/2511.08662v1#bib.bib16))).
An early contribution in this regard is the seminal Cantelli bounds on tail risk (survival probabilities); by inversion, this result yield a sharp bound on Value-at-Risk (VaR). An explicit formula can be traced back to El Ghaoui et al. ([2003](https://arxiv.org/html/2511.08662v1#bib.bib17)). Interestingly, the bound on VaR is achieved by a two-point distribution, and it follows that the same bound also applies to Tail Value-at-Risk (TVaR), which can be viewed as the concave distortion risk measure closest to VaR. Since then, it has become apparent that this correspondence between VaR and its concavation TVaR carries over to general distortion risk measures. Indeed, Li ([2018](https://arxiv.org/html/2511.08662v1#bib.bib24)), Cai et al. ([2025](https://arxiv.org/html/2511.08662v1#bib.bib13)) and Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29)) show that for suitable uncertainty sets Problem [2](https://arxiv.org/html/2511.08662v1#S1.E2 "In 1 Introduction ‣ Robust distortion risk metrics and portfolio optimization") is equivalent to the case in which gg is replaced by the smallest concave function g∗g^{\*} that dominates gg. This is a very relevant result, as when in the DRO (problem [1](https://arxiv.org/html/2511.08662v1#S1.E1 "In 1 Introduction ‣ Robust distortion risk metrics and portfolio optimization")) ff is concave in θ\theta it becomes a convex-concave optimisation problem for which powerful computational methods are available. As shown in Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29)), the stated equivalence does not hold true if the Wasserstein distance is involved, which is the case in our study. For more studies of worst-case problems in operations research and its applications, see e.g., Chen et al. ([2011](https://arxiv.org/html/2511.08662v1#bib.bib14)) and Zymler et al. ([2013](https://arxiv.org/html/2511.08662v1#bib.bib44)).

The ambiguity set is a key component of any distributionally robust optimization model. Rather than letting mathematical convenience drive the choice of the set, it should be primarily guided by available data, possibly complemented by expert opinion. It should be large enough to reasonably include the true distribution but not so broad that it admits implausible distributions, as this could lead to overly conservative decision-making. For example, the distribution function that maximizes VaR and TVaR (i.e., the Cantelli bound) under the sole knowledge of mean and variance has only two mass points, which is not plausible in practice, also highlighting that more (possibly qualitative) information should be used.
In this paper, we study bounds on distortion risk metrics for ambiguity sets that are arguably practically highly relevant, including the case in which the ambiguity set in addition to containing distributions with given first two moments is also restricted to unimodal distributions that are close to some reference distribution. The assumption of unimodality is very reasonable in that it usually complies with data, which also explains why unimodal
distributions are routineously used in engineering, operations research and in insurance and financial risk modeling. For instance, Pareto, Gamma, Normal, Log-Normal, Beta, Weibull, and Student t-distributions are all unimodal. The literature on risk bounds for unimodal distribution functions is limited. Popescu ([2005](https://arxiv.org/html/2511.08662v1#bib.bib30)) proposes semidefinite programming to determine best-possible bounds on tail (survival) probabilities under mean, variance and unimodality constraint from which by numerical inversion VaR\mathrm{VaR} bounds can be obtained. Li et al. ([2018](https://arxiv.org/html/2511.08662v1#bib.bib25)) and Bernard, Kazzi and Vanduffel ([2023](https://arxiv.org/html/2511.08662v1#bib.bib7)) derive explicit bounds on Range Value-at-Risk (RVaR), but results for general distortion risk metrics appear to be missing.

In this paper we show that bounds on distortion risk metrics obtained under the unimodality assumption significantly improve over bounds obtained without making this assumption. To address the natural requirement that admissible distributions are “close enough” to a reference distribution, we use the 2-Wasserstein distance. This choice, aside from offering mathematical convenience, allows us to handle distributions with differing supports.

### 1.1 Our contributions

For the uncertainty sets with fixed mean, variance and 2-Wasserstein distance, we obtain the worst-case value for general distortion risk metrics, where the distortion function is only required to have a finite variation. In particular, our results also cover non-monotone and discontinuous distortion functions. If the distortion function is upper semi-continuous, we also derive the worst-case distribution. Our results extend those in Bernard et al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib8)), where the increasing and absolutely continuous distortion functions were considered. The projection method used in Bernard et al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib8)) does not work for discontinuous distortion functions, and a different technique is required. The method we employ is a variant of the concave envelope approach, differing from the one adopted in Cai et al. ([2025](https://arxiv.org/html/2511.08662v1#bib.bib13)) and Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29)), and requiring non-trivial technical proofs. In these papers, the envelope is constructed on the distortion function. However, to handle the Wasserstein constraint we construct the concave envelope on a linear combination of the distortion function and a functional of the reference distribution with a combination parameter. We then choose the best parameter, where the continuity of the concave envelope with respect to the parameter is crucial and its proof is non-trivial.
Applying our results, we derive the explicit sharp bounds for GlueVaR\mathrm{GlueVaR}333Introduced by Belles-Sampera et al. ([2013](https://arxiv.org/html/2511.08662v1#bib.bib3)) as a measure that makes it possible to strike a balance between two popular risk measures VaR\mathrm{VaR} and ES\mathrm{ES} as the former tends to underestimate risk exposure, whereas the latter is often found to be overly conservative. Cai et al. ([2025](https://arxiv.org/html/2511.08662v1#bib.bib13)) point out that there is a very practical need in industry for having such measures., inter-quantile-difference and the discrepancy between expected shortfall (ES\mathrm{ES}) and VaR\mathrm{VaR}, all of which are not available in the literature.

When the uncertainty sets are characterized by four features, namely mean, variance, Wasserstein distance and unimodality, we derive bounds on distortion risk metrics in case of absolutely continuous distortion functions. We start with the uncertainty sets characterized by fixed mean, variance and unimodality with a fixed inflection point. Employing the projection of a function on the set of all increasing and concave-convex functions with a fixed inflection point on (0,1)(0,1), we obtain the worst-case value and the worst-case distribution for the distortion risk metrics under this uncertainty set. In the literature, only some special risk measures (Range-Value-at-Risk or VaR\mathrm{VaR}) are considered under the similar uncertainty set (although the inflection point is not fixed), but in our paper, we build up a general theory to involve unimodality in the uncertainty set. Although the projection method is powerful, it appears often difficult to obtain the explicit expression of the projection. To address this, we design an efficient algorithm to approximate the worst-case distribution and the worst-case value with any desired degree of precision. Based on this result and employing the projection method, we also find the worst-case value and distribution for the distortion risk metrics when the uncertainty set is characterized by the features of mean, variance, unimodality and Wasserstein distance. Finally, we also discuss the case of unimodality with unknown inflection point, i.e., we provide bounds when the inflection point is in an interval.

All the above results are applied to the portfolio optimization problem and quantification of risk under model uncertainty.

## 2 Preliminary

Let (Ω,𝒜,ℙ)(\Omega,\mathcal{A},\mathbb{P}) be a given atomless probability space. Denote by L2L^{2} the set of all real-valued random variables with finite second moment and by ℳ2\mathcal{M}^{2} the set of all corresponding distribution functions. We interpret a positive value of a random variable as a financial loss. All random variables and distribution functions we mention hereafter are assumed to belong to L2L^{2} resp. ℳ2\mathcal{M}^{2}. The left quantile and right quantile of a distribution function GG are defined as

|  |  |  |
| --- | --- | --- |
|  | G−1​(p)=inf{x∈ℝ:G​(x)⩾p},p∈(0,1],G^{-1}(p)=\inf\{x\in\mathbb{R}:G(x)\geqslant p\},~p\in(0,1], |  |

and

|  |  |  |
| --- | --- | --- |
|  | G+−1​(p)=inf{x∈ℝ:G​(x)>p},p∈[0,1)G\_{+}^{-1}(p)=\inf\{x\in\mathbb{R}:G(x)>p\},~p\in[0,1)~ |  |

respectively, with the convention that inf∅=∞\inf\emptyset=\infty. A left quantile is often also called a Value-at-Risk (VaR). The notation VaR will be used for denoting a left quantile and VaR+ is used to denote right quantiles. The expected shortfall (ES\mathrm{ES}) is another regulatory risk measures widely used in banking and finance, which is defined as

|  |  |  |
| --- | --- | --- |
|  | ESα​(G)=11−α​∫α1G−1​(t)​dt,0⩽α<1.\mathrm{ES}\_{\alpha}(G)=\frac{1}{1-\alpha}\int\_{\alpha}^{1}G^{-1}(t)\mathrm{d}t,~0\leqslant\alpha<1. |  |

We denote by ℋ\mathcal{H} the set of functions g:[0,1]→ℝg:[0,1]\to\mathbb{R} with bounded variation satisfying g​(0)=g​(0+)=0g(0)=g(0+)=0 and g​(1)=g​(1−)g(1)=g(1-). For g∈ℋg\in\mathcal{H}, define g^​(x)=max⁡{g​(x−),g​(x),g​(x+)}\hat{g}(x)=\max\{g(x-),g(x),g(x+)\} for x∈(0,1)x\in(0,1) and g^​(x)=g​(x)\hat{g}(x)=g(x) for x=0,1x=0,1. Hence, g^\hat{g} is the upper semicontinuous version of gg. For g∈ℋg\in\mathcal{H}, a distortion risk metric ρg:ℳ2→ℝ\rho\_{g}:\mathcal{M}^{2}\to\mathbb{R} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρg​(G)=∫0∞g​(1−G​(x))​dx+∫−∞0(g​(1−G​(x))−g​(1))​dx.\displaystyle\rho\_{g}(G)=\int\_{0}^{\infty}g(1-G(x))\mathrm{d}x+\int\_{-\infty}^{0}(g(1-G(x))-g(1))\mathrm{d}x. |  | (3) |

In this paper, we aim to determine the *worst-case* and *best-case* values of a distortion risk metric ρg\rho\_{g} over certain distributional uncertainty sets ℱ⊆ℳ2\mathcal{F}\subseteq{\mathcal{M}^{2}}. That is, we deal with problems of the form

The sets ℱ\mathcal{F} will contain all distribution functions with a given mean and variance that are within a Wasserstein ball around a given reference distribution FF and/or that are unimodal. The set of the quantile functions corresponding to the cdfs contained in ℱ\mathcal{F} will be denoted by ℱ−1\mathcal{F}^{-1}.

In addition to the worst- and best-case values, we also study *worst-case* and *best-case distribution functions* if they exist – that is, the distribution functions attaining ([4a](https://arxiv.org/html/2511.08662v1#S2.E4.1 "In 4 ‣ 2 Preliminary ‣ Robust distortion risk metrics and portfolio optimization")) and ([4b](https://arxiv.org/html/2511.08662v1#S2.E4.2 "In 4 ‣ 2 Preliminary ‣ Robust distortion risk metrics and portfolio optimization")), respectively.

Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | infG∈ℱρg​(G)=−supG∈ℱ−ρg​(G)=−supG∈ℱρ−g​(G),\displaystyle\inf\_{G\in\mathcal{F}}\rho\_{g}(G)=-\sup\_{G\in\mathcal{F}}-\rho\_{g}(G)=-\sup\_{G\in\mathcal{F}}\rho\_{-g}(G), |  | (5) |

where ρ−g\rho\_{-g} is also a distortion risk metric. Moreover, G∗G^{\*} is the worst-case distribution for supG∈ℱρ−g​(G)\sup\_{G\in\mathcal{F}}\rho\_{-g}(G) if and only if it is the best-case distribution for infG∈ℱρg​(G)\inf\_{G\in\mathcal{F}}\rho\_{g}(G). Hence, the problem for ([4b](https://arxiv.org/html/2511.08662v1#S2.E4.2 "In 4 ‣ 2 Preliminary ‣ Robust distortion risk metrics and portfolio optimization")) can be fully transferred to problem ([4a](https://arxiv.org/html/2511.08662v1#S2.E4.1 "In 4 ‣ 2 Preliminary ‣ Robust distortion risk metrics and portfolio optimization")). This is one of the motivations to study distortion risk metrics rather than distortion risk measures, as stated in Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29)). In this paper, we mainly focus on ([4a](https://arxiv.org/html/2511.08662v1#S2.E4.1 "In 4 ‣ 2 Preliminary ‣ Robust distortion risk metrics and portfolio optimization")).

We end the section with a discussion of various distortion risk metrics of our interest. We first provide three variability measures that are also distortion risk metrics, namely the Gini deviation (GD\mathrm{GD}), the mean-median deviation (MMD\mathrm{MMD}), and the inter-quantile difference (IQD\mathrm{IQD}).

The GD\mathrm{GD} of a distribution function GG is defined as

|  |  |  |
| --- | --- | --- |
|  | GD​(G)=12​𝔼​(|X−Y|):=ρgGD​(G),\mathrm{GD}(G)=\frac{1}{2}\mathbb{E}(|X-Y{}|):=\rho\_{g\_{\mathrm{GD}}}(G), |  |

where X∼GX\sim G and Y∼GY\sim G are independent and gGD​(t)=t−t2,t∈[0,1]g\_{\mathrm{GD}}(t)=t-t^{2},~t\in[0,1]. The Gini deviation thus measures the average absolute difference between two randomly chosen realisations of GG. After normalization, it becomes the Gini coefficient, which is widely used to measure income inequality. In finance, it was proposed by Shalit and Yitzhaki ([1984](https://arxiv.org/html/2511.08662v1#bib.bib35)) as a substitute for variance as a measure of risk within Markowitz’s portfolio selection model. Specifically, these authors develop a portfolio selection approach based on the mean and the Gini deviation as measures of return and risk, respectively. Apart from being more robust, the use of the Gini deviation also enables the derivation of necessary conditions for stochastic dominance, allowing agents to eliminate from the efficient set any feasible solutions that are stochastically dominated by others.

Furthermore, the MMD\mathrm{MMD} of GG is defined as

|  |  |  |
| --- | --- | --- |
|  | MMD​(G)=minx∈ℝ⁡𝔼​(|X−x|)=𝔼​(|X−G−1​(1/2)|):=ρgMMD​(G),\mathrm{MMD}(G)=\min\_{x\in\mathbb{R}}\mathbb{E}(|X-x|)=\mathbb{E}(|X-G^{-1}(1/2)|):=\rho\_{g\_{\mathrm{MMD}}}(G), |  |

where X∼GX\sim G and gMMD​(t)=t∧(1−t),t∈[0,1]g\_{\mathrm{MMD}}(t)=t\wedge(1-t),~t\in[0,1].

As for IQD\mathrm{IQD}, we define

|  |  |  |
| --- | --- | --- |
|  | IQDα+​(G)=G+−1​(1−α)−G−1​(α):=ρgIQD+​(G),α∈(0,1/2],\mathrm{IQD}\_{\alpha}^{+}(G)=G\_{+}^{-1}(1-\alpha)-G^{-1}(\alpha):=\rho\_{g\_{\mathrm{IQD}^{+}}}(G),~\alpha\in(0,1/2], |  |

and

|  |  |  |
| --- | --- | --- |
|  | IQDα−​(G)=G−1​(1−α)−G+−1​(α):=ρgIQD−​(G),α∈(0,1/2),\mathrm{IQD}\_{\alpha}^{-}(G)=G^{-1}(1-\alpha)-G\_{+}^{-1}(\alpha):=\rho\_{g\_{\mathrm{IQD}^{-}}}(G),~\alpha\in(0,1/2), |  |

where gIQD+​(t)=𝟙[α,1−α]​(t),t∈[0,1]g\_{\mathrm{IQD}^{+}}(t)=\mathds{1}\_{[\alpha,1-\alpha]}(t),~t\in[0,1] and gIQD−​(t)=𝟙(α,1−α)​(t),t∈[0,1]g\_{\mathrm{IQD}^{-}}(t)=\mathds{1}\_{(\alpha,1-\alpha)}(t),~t\in[0,1].
Note that the definitions of IQDα+\mathrm{IQD}\_{\alpha}^{+} and IQDα−\mathrm{IQD}\_{\alpha}^{-} can be found in Bellini et al. ([2022](https://arxiv.org/html/2511.08662v1#bib.bib4)) and Lauzier et al. ([2023](https://arxiv.org/html/2511.08662v1#bib.bib23)), respectively. The measures MMD\mathrm{MMD} and IQD\mathrm{IQD} play a prominent role in robust statistics, and are therefore also useful in portfolio selection and risk management, where resilience to outliers (data contamination) is desired. Their application to the problem of risk sharing can be found in Lauzier et al. ([2023](https://arxiv.org/html/2511.08662v1#bib.bib23)).

The GlueVaR\mathrm{GlueVaR} of a distribution GG was introduced in Belles-Sampera et al. ([2013](https://arxiv.org/html/2511.08662v1#bib.bib3)) and is defined as the distortion risk metric ρg​(G)\rho\_{g}(G) in which the distortion g:=gβ,αh1,h2g:=g^{h\_{1},h\_{2}}\_{\beta,\alpha} is given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | gβ,αh1,h2​(t)={h11−β​t,0⩽t<1−β,h1+h2−h1β−α​[t−(1−β)],1−β⩽t⩽1−α,1,1−α<t⩽1,g^{h\_{1},h\_{2}}\_{\beta,\alpha}(t)=\begin{cases}\frac{h\_{1}}{1-\beta}t,&0\leqslant t<1-\beta,\\ h\_{1}+\frac{h\_{2}-h\_{1}}{\beta-\alpha}[t-(1-\beta)],&1-\beta\leqslant t\leqslant 1-\alpha,\\ 1,&1-\alpha<t\leqslant 1,\end{cases} |  | (6) |

where α,β∈[0,1]\alpha,\beta\in[0,1] such that α⩽β\alpha\leqslant\beta, h1∈[0,1]h\_{1}\in[0,1], and h2∈[h1,1]h\_{2}\in[h\_{1},1].

Note that VaRα\mathrm{VaR}\_{\alpha},
ESα\mathrm{ES}\_{\alpha} and Range-Value-at-Risk (RVaR\mathrm{RVaR}) are particular cases of this family of risk measures with the corresponding distortion functions gα,α0,0​(u)g^{0,0}\_{\alpha,\alpha}(u), gα,α1,1​(u)g^{1,1}\_{\alpha,\alpha}(u) and gβ,α0,1​(u)g^{0,1}\_{\beta,\alpha}(u) with α<β\alpha<\beta, respectively, where RVaR\mathrm{RVaR} introduced by Cont et al. ([2010](https://arxiv.org/html/2511.08662v1#bib.bib15)) as a family of robust risk measures is defined as

|  |  |  |
| --- | --- | --- |
|  | RVaRα,β​(G)=1β−α​∫αβG−1​(t)​dt,0<α<β<1.\mathrm{RVaR}\_{\alpha,\beta}(G)=\frac{1}{\beta-\alpha}\int\_{\alpha}^{\beta}G^{-1}(t)\mathrm{d}t,~0<\alpha<\beta<1. |  |

Furthermore, GlueVaR\mathrm{GlueVaR} can be rewritten as the linear combination of ES\mathrm{ES} and VaR\mathrm{VaR}. If h11−β⩾h2−h1β−α\frac{h\_{1}}{1-\beta}\geqslant\frac{h\_{2}-h\_{1}}{\beta-\alpha}, then GlueVaRβ,αh1,h2=w1​ESα+w2​ESβ+w3​VaRα\mathrm{GlueVaR}\_{\beta,\alpha}^{h\_{1},h\_{2}}=w\_{1}\mathrm{ES}\_{\alpha}+w\_{2}\mathrm{ES}\_{\beta}+w\_{3}\mathrm{VaR}\_{\alpha} with some w1,w2,w3⩾0w\_{1},w\_{2},w\_{3}\geqslant 0 satisfying w1+w2+w3=1w\_{1}+w\_{2}+w\_{3}=1; see Belles-Sampera et al. ([2013](https://arxiv.org/html/2511.08662v1#bib.bib3)) for more details.

Finally, for 0<α1<α2<10<\alpha\_{1}<\alpha\_{2}<1, the discrepancy of ES\mathrm{ES} and VaR\mathrm{VaR} is defined as

|  |  |  |
| --- | --- | --- |
|  | ρgα1,α2=ESα1−VaRα2,\rho\_{g\_{\alpha\_{1},\alpha\_{2}}}=\mathrm{ES}\_{\alpha\_{1}}-\mathrm{VaR}\_{\alpha\_{2}}, |  |

where gα1,α2​(t)=t1−α1∧1−𝟙(1−α2,1]​(t)g\_{\alpha\_{1},\alpha\_{2}}(t)=\frac{t}{1-\alpha\_{1}}\wedge 1-\mathds{1}\_{(1-\alpha\_{2},1]}(t). In practice, one often uses the parameter values α1=0.975\alpha\_{1}=0.975 and α2=0.99\alpha\_{2}=0.99.

In what follows, the notation VV is used to denote a standard uniformly distributed random variable.

## 3 Bounds for distortion risk metrics under Wasserstein distance constraints

One popular notion used in mass transportation and distributionally robust optimization is the Wasserstein metric. For more details, one can refer to Esfahani and Kuhn ([2018](https://arxiv.org/html/2511.08662v1#bib.bib18)) and Blanchet and Murthy ([2019](https://arxiv.org/html/2511.08662v1#bib.bib10)). For two random variables XX and YY with respective distributions FF and GG, the one dimensional Wasserstein metric of order 22 is given by

|  |  |  |
| --- | --- | --- |
|  | dW​(X,Y)=dW​(F,G)=dW​(F−1,G−1)=(∫01|F−1​(x)−G−1​(x)|2​dx)1/2.d\_{W}(X,Y)=d\_{W}(F,G)=d\_{W}(F^{-1},G^{-1})=\left(\int\_{0}^{1}|F^{-1}(x)-G^{-1}(x)|^{2}\mathrm{d}x\right)^{1/2}. |  |

In this section we study problem ([4a](https://arxiv.org/html/2511.08662v1#S2.E4.1 "In 4 ‣ 2 Preliminary ‣ Robust distortion risk metrics and portfolio optimization")) when the uncertainty set ℱ\mathcal{F} is given as

|  |  |  |
| --- | --- | --- |
|  | ℱ:=ℳε​(μ,σ)={G∈ℳ2:∫ℝx​dG=μ,∫ℝx2​dG=μ2+σ2,dW​(G,F)⩽ε},\mathcal{F}:=\mathcal{M}\_{\varepsilon}(\mu,\sigma)=\left\{G\in\mathcal{M}^{2}:\int\_{\mathbb{R}}x\mathrm{d}G=\mu,\int\_{\mathbb{R}}x^{2}\mathrm{d}G=\mu^{2}+\sigma^{2},d\_{W}(G,F)\leqslant\sqrt{\varepsilon}\right\}, |  |

where μ∈ℝ\mu\in\mathbb{R}, σ>0\sigma>0, ε>0\varepsilon>0 and F∈ℳ2F\in\mathcal{M}^{2}. Here, the distribution function FF is the center of a Wasserstein ball and we denotes its mean by μF\mu\_{F} and σF>0\sigma\_{F}>0, respectively. Note that
ℳ∞​(μ,σ)={G∈ℳ2:∫ℝx​dG=μ,∫ℝx2​dG=μ2+σ2}\mathcal{M}\_{\infty}(\mu,\sigma)=\left\{G\in\mathcal{M}^{2}:\int\_{\mathbb{R}}x\mathrm{d}G=\mu,\int\_{\mathbb{R}}x^{2}\mathrm{d}G=\mu^{2}+\sigma^{2}\right\}. For g∈ℋg\in\mathcal{H}, let g∗g^{\*} and g∗g\_{\*} denote the concave and convex envelopes of gg respectively, i.e., g∗=inf{h∈ℋ:h​is concave on​[0,1]​and​h⩾g}g^{\*}=\inf\{h\in\mathcal{H}:h~\text{is concave on}~[0,1]~\text{and}~h\geqslant g\} and g∗=sup{h∈ℋ:h​is convex on​[0,1]​and​h⩽g}g\_{\*}=\sup\{h\in\mathcal{H}:h~\text{is convex on}~[0,1]~\text{and}~h\leqslant g\}. For any concave or convex function h∈ℋh\in\mathcal{H}, let h′​(t):=∂+h​(t)h^{\prime}(t):=\partial\_{+}h(t).
Let c0=C​o​r​r​(F−1​(V),(g∗)′​(1−V))c\_{0}=Corr(F^{-1}(V),(g^{\*})^{\prime}(1-V)) with the convention that that c0=0c\_{0}=0 if (g∗)′(g^{\*})^{\prime} is a constant. Note that c0⩾0c\_{0}\geqslant 0. Moreover, let gλ​(t)=g​(t)+λ​∫1−t1F−1​(s)​dsg\_{\lambda}(t)=g(t)+\lambda\int\_{1-t}^{1}F^{-1}(s)\mathrm{d}s for t∈[0,1]t\in[0,1] and λ⩾0\lambda\geqslant 0, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | hλ​(t)=μ+σ​(gλ∗)′​(1−t)−aλbλ,\displaystyle h\_{\lambda}(t)=\mu+\sigma\frac{(g\_{\lambda}^{\*})^{\prime}(1-t)-a\_{\lambda}}{b\_{\lambda}}, |  | (7) |

where aλ=E​((gλ∗)′​(V))=g​(1)+λ​μFa\_{\lambda}=E((g\_{\lambda}^{\*})^{\prime}(V))=g(1)+\lambda\mu\_{F}, bλ=V​a​r​((gλ∗)′​(V))b\_{\lambda}=\sqrt{Var((g\_{\lambda}^{\*})^{\prime}(V))}. We denote the corresponding distribution functions of hλh\_{\lambda} by HλH\_{\lambda} with Hλ−1=hλH\_{\lambda}^{-1}=h\_{\lambda}.
In order to ensure that hλh\_{\lambda} is well-defined, throughout the paper, we make the following assumption:

Assumption A: ∫01((g∗)′​(t))2​dt<∞\int\_{0}^{1}((g^{\*})^{\prime}(t))^{2}\mathrm{d}t<\infty and (gλ∗)′(g\_{\lambda}^{\*})^{\prime} is not a constant for all λ>0\lambda>0.

For G∈ℳε​(μ,σ)G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma) and g∈ℋg\in\mathcal{H}, it follows from Assumption A that

|  |  |  |
| --- | --- | --- |
|  | ρg​(G)⩽ρg∗​(G)=∫01(g∗)′​(1−t)​G−1​(t)​dt⩽σ​(∫01((g∗)′​(t))2​dt)1/2<∞.\rho\_{g}(G)\leqslant\rho\_{g^{\*}}(G)=\int\_{0}^{1}(g^{\*})^{\prime}(1-t)G^{-1}(t)\mathrm{d}t\leqslant\sigma\left(\int\_{0}^{1}((g^{\*})^{\prime}(t))^{2}\mathrm{d}t\right)^{1/2}<\infty. |  |

Hence, Assumption A also guarantees that ρg​(G)<∞\rho\_{g}(G)<\infty for all G∈ℳε​(μ,σ)G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma). The following lemma is crucial to the main results of the paper (see Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") below) and its proof is completely non-trivial, where the arguments play a key role to the proof of Corollary [2](https://arxiv.org/html/2511.08662v1#Thmcorollary2 "Corollary 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") below. We postpone it to the Appendix.

###### Lemma 1.

The function C​o​r​r​(F−1​(V),(gλ∗)′​(1−V))Corr(F^{-1}(V),(g\_{\lambda}^{\*})^{\prime}(1-V)) is continuous in λ\lambda on [0,∞)[0,\infty) and

|  |  |  |
| --- | --- | --- |
|  | limλ→∞C​o​r​r​(F−1​(V),(gλ∗)′​(1−V))=1.\lim\_{\lambda\to\infty}Corr(F^{-1}(V),(g\_{\lambda}^{\*})^{\prime}(1-V))=1. |  |

Next, we display our first main result, showing the worst-case distribution and worst-case value of the distortion risk metrics over the uncertainty set ℳε​(μ,σ)\mathcal{M}\_{\varepsilon}(\mu,\sigma).

###### Theorem 1.

Suppose g∈ℋg\in\mathcal{H} and g=g^g=\hat{g} .

1. (i)

   If (μF−μ)2+(σF−σ)2<ε<(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}<\varepsilon<(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}), then it holds that

   sup\_G∈M\_ε(μ, σ) ρ\_g(G)=ρ\_g(H\_λ\_ε),

   in which HλεH\_{\lambda\_{\varepsilon}} is the unique worst-case distribution function, determined by dW​(F,Hλε)=εd\_{W}(F,H\_{\lambda\_{\varepsilon}})=\sqrt{\varepsilon} for some λε>0\lambda\_{\varepsilon}>0.
2. (ii)

   Let ε⩾(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)\varepsilon\geqslant(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}). If (g∗)′(g^{\*})^{\prime} is not a constant, then case i) applies with λε=0\lambda\_{\varepsilon}=0.
   If (g∗)′(g^{\*})^{\prime} is a constant, then supG∈ℳε​(μ,σ)ρg​(G)=g​(1)​μ\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G)=g(1)\mu.

The conclusions in Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") hold for very general distortion functions covering many results in the literature such as Bernard et al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib8)) (increasing and absolutely continuous gg), Shao and Zhang ([2023](https://arxiv.org/html/2511.08662v1#bib.bib36)) (increasing gg and ε=∞\varepsilon=\infty), Li et al. ([2018](https://arxiv.org/html/2511.08662v1#bib.bib25)) (Range-Value-at-Risk and ε=∞\varepsilon=\infty), Li ([2018](https://arxiv.org/html/2511.08662v1#bib.bib24)) (concave and increasing gg and ε=∞\varepsilon=\infty) and Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29))(general gg and ε=∞\varepsilon=\infty). Compared with the results in the literature, the novelty of Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") is that it covers the case that gg can be non-monotone and discontinuous, especially including the distortion functions of GD\mathrm{GD}, MMD\mathrm{MMD}, VaR+\mathrm{VaR}^{+} and IQD+\mathrm{IQD}^{+} as special cases. We here emphasize that Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") exactly extends the results in Bernard et al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib8)) from the case with increasing and absolutely continuous distortion functions to the case with upper semi-continuous distortion functions with finite variation. The projection method used in Bernard et al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib8)) requires gg to be absolutely continuous and cannot be applied for the general case we consider.

The method used to prove Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") is a variant of the concave envelope technique. It differs from the approach in Cai et al. ([2025](https://arxiv.org/html/2511.08662v1#bib.bib13)), and Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29)) where the envelope is constructed on the distortion function. Here, the concave envelope is on a linear combination of the distortion function and a functional of the reference distribution FF with a combination parameter λ\lambda. We then choose the best parameter. The existence of the best parameter is based on some continuity property of this envelope as shown in Lemma [1](https://arxiv.org/html/2511.08662v1#Thmlemma1 "Lemma 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"). This continuity property is a key result to obtain Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") and its proof is highly non-trivial.

To find the worst-case distribution, the explicit expression of (gλ∗)′​(1−t)(g\_{\lambda}^{\*})^{\prime}(1-t) is crucial. Note that if gg is concave, then (gλ∗)′​(1−t)=g′​(1−t)+λ​F−1​(t),t∈(0,1)(g\_{\lambda}^{\*})^{\prime}(1-t)=g^{\prime}(1-t)+\lambda F^{-1}(t),~t\in(0,1), which covers the case of GD\mathrm{GD} and MMD\mathrm{MMD}. If gg is nonconcave, it becomes cumbersome to compute (gλ∗)′​(1−t)(g\_{\lambda}^{\*})^{\prime}(1-t). Nevertheless, Corollary [1](https://arxiv.org/html/2511.08662v1#Thmcorollary1 "Corollary 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") hereafter provides explicit expressions for the cases of VaRα+\mathrm{VaR}\_{\alpha}^{+}, IQDα+\mathrm{IQD}\_{\alpha}^{+}, and the discrepancy ρgα1,α2\rho\_{g\_{\alpha\_{1},\alpha\_{2}}} between ES\mathrm{ES} and VaR\mathrm{VaR}, respectively.
To this end, for α∈(0,1)\alpha\in(0,1) and λ⩾0\lambda\geqslant 0, let us define

|  |  |  |  |
| --- | --- | --- | --- |
|  | tα,λ=inf{t∈[0,α):1+λ​∫1−α1−tF−1​(s)​dsα−t⩾λ​F−1​(1−t)},t\_{\alpha,\lambda}=\inf\left\{t\in[0,\alpha):\frac{1+\lambda\int\_{1-\alpha}^{1-t}F^{-1}(s)\mathrm{d}s}{\alpha-t}\geqslant\lambda F^{-1}(1-t)\right\}, |  | (8) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | t^α,λ=sup{t∈(1−α,1]:λ​∫1−tαF−1​(s)​ds−1t−1+α⩽λ​F−1​(1−t)}.\displaystyle\hat{t}\_{\alpha,\lambda}=\sup\left\{t\in(1-\alpha,1]:\frac{\lambda\int\_{1-t}^{\alpha}F^{-1}(s)\mathrm{d}s-1}{t-1+\alpha}\leqslant\lambda F^{-1}(1-t)\right\}. |  | (9) |

For 0<α1<α2<10<\alpha\_{1}<\alpha\_{2}<1 and λ⩾0\lambda\geqslant 0, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | uα1,α2,λ\displaystyle u\_{\alpha\_{1},\alpha\_{2},\lambda} | =sup{t∈(1−α2,1]:(t−1+α2)∧(α2−α1)1−α1+λ​∫1−tα2F−1​(s)​ds−1t−1+α2\displaystyle=\sup\left\{t\in(1-\alpha\_{2},1]:\frac{\frac{(t-1+\alpha\_{2})\wedge(\alpha\_{2}-\alpha\_{1})}{1-\alpha\_{1}}+\lambda\int\_{1-t}^{\alpha\_{2}}F^{-1}(s)\mathrm{d}s-1}{t-1+\alpha\_{2}}\right. |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ⩽11−α1𝟙(0,1−α1)(t)+λF−1(1−t)}.\displaystyle~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\left.\leqslant\frac{1}{1-\alpha\_{1}}\mathds{1}\_{(0,1-\alpha\_{1})}(t)+\lambda F^{-1}(1-t)\right\}. |  | (10) |

We formulate the following corollary.

###### Corollary 1.

Suppose (μF−μ)2+(σF−σ)2<ε<(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}<\varepsilon<(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}).

1. (i)

   For α∈(0,1)\alpha\in(0,1), we have
   sup\_G∈M\_ε(μ, σ) VaR\_α^+(G)=μ+σ1+λε∫α1-t1-α,λεF-1(s)ds1-α-t1-α,λε-aλεbλε,
   and the worst-case quantile is hλεh\_{\lambda\_{\varepsilon}} given by ([7](https://arxiv.org/html/2511.08662v1#S3.E7 "In 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization")) with
   (g\_λ^\*)’(1-t)=λF^-1(t)1\_(0,α] ∪(1-t\_1-α,λ,1)(t)+1+λ∫α1-t1-α,λF-1(s)ds1-α-t1-α,λ1\_(α,1-t\_1-α,λ], t∈(0,1),
   where λε\lambda\_{\varepsilon} is the solution of dW​(F,Hλ)=εd\_{W}(F,H\_{\lambda})=\sqrt{\varepsilon}.
2. (ii)

   For α∈(0,1/2)\alpha\in(0,1/2), we have

   |  |  |  |
   | --- | --- | --- |
   |  | supG∈ℳε​(μ,σ)IQDα+​(G)=(1+λε​∫1−α1−tα,λεF−1​(s)​dsα−tα,λε−λε​∫1−t^α,λεαF−1​(s)​ds−1t^α,λε−1+α)​σbλε\displaystyle\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\mathrm{IQD}\_{\alpha}^{+}(G)=\left(\frac{1+\lambda\_{\varepsilon}\int\_{1-\alpha}^{1-t\_{\alpha,\lambda\_{\varepsilon}}}F^{-1}(s)\mathrm{d}s}{\alpha-t\_{\alpha,\lambda\_{\varepsilon}}}-\frac{\lambda\_{\varepsilon}\int\_{1-\hat{t}\_{\alpha,\lambda\_{\varepsilon}}}^{\alpha}F^{-1}(s)\mathrm{d}s-1}{\hat{t}\_{\alpha,\lambda\_{\varepsilon}}-1+\alpha}\right)\frac{\sigma}{b\_{\lambda\_{\varepsilon}}} |  |

   and the worst-case quantile is hλεh\_{\lambda\_{\varepsilon}} given by ([7](https://arxiv.org/html/2511.08662v1#S3.E7 "In 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization")) with

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (gλ∗)′​(1−t)\displaystyle(g\_{\lambda}^{\*})^{\prime}(1-t) | =1+λ​∫1−α1−tα,λF−1​(s)​dsα−tα,λ​𝟙(1−α,1−tα,λ)​(t)+λ​∫1−t^α,λαF−1​(s)​ds−1t^α,λ−1+α​𝟙(1−t^α,λ,α)​(t)\displaystyle=\frac{1+\lambda\int\_{1-\alpha}^{1-t\_{\alpha,\lambda}}F^{-1}(s)\mathrm{d}s}{\alpha-t\_{\alpha,\lambda}}\mathds{1}\_{(1-\alpha,1-t\_{\alpha,\lambda})}(t)+\frac{\lambda\int\_{1-\hat{t}\_{\alpha,\lambda}}^{\alpha}F^{-1}(s)\mathrm{d}s-1}{\hat{t}\_{\alpha,\lambda}-1+\alpha}\mathds{1}\_{(1-\hat{t}\_{\alpha,\lambda},\alpha)}(t) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +λ​F−1​(t)​𝟙(0,1−t^α,λ)∪(α,1−α)∪(1−tα,λ,1),t∈(0,1),\displaystyle+\lambda F^{-1}(t)\mathds{1}\_{(0,1-\hat{t}\_{\alpha,\lambda})\cup(\alpha,1-\alpha)\cup(1-t\_{\alpha,\lambda},1)},~t\in(0,1), |  |

   where λε\lambda\_{\varepsilon} is the solution of dW​(F,Hλ)=εd\_{W}(F,H\_{\lambda})=\sqrt{\varepsilon}.
3. (iii)

   For 0<α1<α2<10<\alpha\_{1}<\alpha\_{2}<1, we have

   |  |  |  |
   | --- | --- | --- |
   |  | supG∈ℳε​(μ,σ)ρgα1,α2​(G)\displaystyle\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g\_{\alpha\_{1},\alpha\_{2}}}(G) |  |
   |  |  |  |
   | --- | --- | --- |
   |  | =σ​λεbλε​(1−α1)​(∫α1α1∨(1−uα1,α2,λε)F−1​(s)​ds+∫α21F−1​(s)​ds)\displaystyle=\frac{\sigma\lambda\_{\varepsilon}}{b\_{\lambda\_{\varepsilon}}(1-\alpha\_{1})}\left(\int\_{\alpha\_{1}}^{\alpha\_{1}\vee(1-u\_{\alpha\_{1},\alpha\_{2},\lambda\_{\varepsilon}})}F^{-1}(s)\mathrm{d}s+\int\_{\alpha\_{2}}^{1}F^{-1}(s)\mathrm{d}s\right) |  |
   |  |  |  |
   | --- | --- | --- |
   |  | +σbλε​1−α2+(1−α1−uα1,α2,λε)+(1−α1)2+σ​cα1,α2,λεbλε​((α2−α1)∧(uα1,α2,λε−1+α2)1−α1−1),\displaystyle~+\frac{\sigma}{b\_{\lambda\_{\varepsilon}}}\frac{1-\alpha\_{2}+(1-\alpha\_{1}-u\_{\alpha\_{1},\alpha\_{2},\lambda\_{\varepsilon}})\_{+}}{(1-\alpha\_{1})^{2}}+\frac{\sigma c\_{\alpha\_{1},\alpha\_{2},\lambda\_{\varepsilon}}}{b\_{\lambda\_{\varepsilon}}}\left(\frac{(\alpha\_{2}-\alpha\_{1})\wedge(u\_{\alpha\_{1},\alpha\_{2},\lambda\_{\varepsilon}}-1+\alpha\_{2})}{1-\alpha\_{1}}-1\right), |  |

   and the worst-case quantile is hλεh\_{\lambda\_{\varepsilon}} given by ([7](https://arxiv.org/html/2511.08662v1#S3.E7 "In 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization")) with

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (gλ∗)′​(1−t)\displaystyle(g\_{\lambda}^{\*})^{\prime}(1-t) | =(11−α1​𝟙(α1,1)​(t)+λ​F−1​(t))​𝟙(0,1−uα1,α2,λ)∪(α2,1)​(t)\displaystyle=\left(\frac{1}{1-\alpha\_{1}}\mathds{1}\_{(\alpha\_{1},1)}(t)+\lambda F^{-1}(t)\right)\mathds{1}\_{(0,1-u\_{\alpha\_{1},\alpha\_{2},\lambda})\cup(\alpha\_{2},1)}(t) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +cα1,α2,λ​𝟙(1−uα1,α2,λ,α2)​(t),t∈(0,1),\displaystyle+c\_{\alpha\_{1},\alpha\_{2},\lambda}\mathds{1}\_{(1-u\_{\alpha\_{1},\alpha\_{2},\lambda},\alpha\_{2})}(t),~t\in(0,1), |  |

   where λε\lambda\_{\varepsilon} is the solution of dW​(F,Hλ)=εd\_{W}(F,H\_{\lambda})=\sqrt{\varepsilon} and
   c\_α\_1,α\_2,λ=(uα1,α2,λ-1+α2)∧(α2-α1)1-α1+λ∫1-uα1,α2,λα2F-1(s)ds-1uα1,α2,λ-1+α2.

Note that (i) of Corollary [1](https://arxiv.org/html/2511.08662v1#Thmcorollary1 "Corollary 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") is given in Proposition 4.6 of Bernard et al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib8)), where a detailed and complicated analysis is required. However, by applying Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we can obtain the worst-case value and the worst-case distribution for VaR+\mathrm{VaR}^{+} immediately. We observe that the corresponding worst-case quantile is a linear function of the quantile of the reference distribution on the tail parts, which is not a constant in general. This is in contrast to the case without Wasserstein constraint, where the worst-case quantile is a step function with two steps (Cantelli bound). The worst-case value and quantile for VaR+\mathrm{VaR}^{+} with only Wassertein constriant can be found in Liu et al. ([2022](https://arxiv.org/html/2511.08662v1#bib.bib26)). Moreover, (ii) of Corollary [1](https://arxiv.org/html/2511.08662v1#Thmcorollary1 "Corollary 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") is completely new showing the worst-case value of the variability or the statistical dispersion of the data with given mean, variance and the Wasserstein distance ball. The corresponding worst-case quantile is a linear function of the quantile of the reference distribution on the middle part and tail parts. Finally, the worst-case value of the discrepancy of ES\mathrm{ES} and VaR\mathrm{VaR} is given in (iii) of Corollary [1](https://arxiv.org/html/2511.08662v1#Thmcorollary1 "Corollary 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), and corresponds to the largest possible additional capital requirement by shifting from VaR\mathrm{VaR} to ES\mathrm{ES}; see the Basel regulatory framework BCBS ([2019](https://arxiv.org/html/2511.08662v1#bib.bib2)).

Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") requires that gg is upper semi-continuous, which excludes the distortion functions for VaR\mathrm{VaR}, IQD−\mathrm{IQD}^{-} and GlueVaR.
Moreover, following ([5](https://arxiv.org/html/2511.08662v1#S2.E5 "In 2 Preliminary ‣ Robust distortion risk metrics and portfolio optimization")), to derive the best-case value for ρg\rho\_{g}, it is equivalent to finding the worst-case value for ρ−g\rho\_{-g}. If gg is upper semi-continuous, then −g-g is lower-semicontinuous, which may not be covered by Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") such as VaR+\mathrm{VaR}^{+} and IQD+\mathrm{IQD}^{+} and ρgα1,α2\rho\_{g\_{\alpha\_{1},\alpha\_{2}}}. Hence, we next eliminate the restriction of upper-semicontinuity and consider all g∈ℋg\in\mathcal{H}.

###### Theorem 2.

Suppose g∈ℋg\in\mathcal{H}.

1. (i)

   If (μF−μ)2+(σF−σ)2<ε<(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}<\varepsilon<(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}) and ρg^​(Hλ)\rho\_{\hat{g}}(H\_{\lambda}) is continuous with respect to λ\lambda over (0,∞)(0,\infty), then
   sup\_G∈M\_ε(μ, σ) ρ\_g(G)=sup\_G∈M\_ε(μ, σ) ρ\_^g(G)=ρ\_^g(H\_λ\_ε),
   where λε\lambda\_{\varepsilon} is the solution of dW​(F,Hλ)=εd\_{W}(F,H\_{\lambda})=\sqrt{\varepsilon}.
2. (ii)

   Let ε⩾(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)\varepsilon\geqslant(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}). If (g∗)′(g^{\*})^{\prime} is not a constant, then
   sup\_G∈M\_ε(μ, σ) ρ\_g(G)=sup\_G∈M\_ε(μ, σ) ρ\_^g(G)=ρ\_^g(H\_0);

If (g∗)′(g^{\*})^{\prime} is a constant, then supG∈ℳε​(μ,σ)ρg​(G)=g​(1)​μ\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G)=g(1)\mu.

In (i) of Theorem [2](https://arxiv.org/html/2511.08662v1#Thmtheorem2 "Theorem 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we impose an additional assumption: the continuity of ρg^​(Hλ)\rho\_{\hat{g}}(H\_{\lambda}) with respect to λ\lambda over (0,∞)(0,\infty). This assumption is due to the Wasserstein constraint and it cannot be removed in our technical proof of Theorem [2](https://arxiv.org/html/2511.08662v1#Thmtheorem2 "Theorem 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"); see Section [A](https://arxiv.org/html/2511.08662v1#A1 "Appendix A Proof of Section 3 ‣ Robust distortion risk metrics and portfolio optimization") in Appendix. However, this assumption is valid for our concerned distortion risk metrics in Corollary [2](https://arxiv.org/html/2511.08662v1#Thmcorollary2 "Corollary 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") below. It is worth mentioning that the arguments obtained in proof of Lemma [1](https://arxiv.org/html/2511.08662v1#Thmlemma1 "Lemma 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") play a key role in the checking of this assumption.

For 0<α<β<10<\alpha<\beta<1, 0<h1<h2<10<h\_{1}<h\_{2}<1 and λ⩾0\lambda\geqslant 0, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | uα,β,λh1,h2\displaystyle u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}} | =inf{t∈[0,1−α):1−gα,βh1,h2​(t)+λ​∫α1−tF−1​(s)​ds1−α−t\displaystyle=\inf\left\{t\in[0,1-\alpha):\frac{1-g\_{\alpha,\beta}^{h\_{1},h\_{2}}(t)+\lambda\int^{1-t}\_{\alpha}F^{-1}(s)\mathrm{d}s}{1-\alpha-t}\right. |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ⩾h11−β𝟙(0,1−β)(t)+h2−h1β−α𝟙[1−β,1−α)(t)+λF−1(1−t)}.\displaystyle~~~~~~~~~~~~~~~~~~~~~~~~~~~\left.\geqslant\frac{h\_{1}}{1-\beta}\mathds{1}\_{(0,1-\beta)}(t)+\frac{h\_{2}-h\_{1}}{\beta-\alpha}\mathds{1}\_{[1-\beta,1-\alpha)}(t)+\lambda F^{-1}(1-t)\right\}. |  | (11) |

###### Corollary 2.

Suppose (μF−μ)2+(σF−σ)2<ε<(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}<\varepsilon<(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}).

1. (i)

   For α∈(0,1)\alpha\in(0,1), we have VaRα+​(Hλ)\mathrm{VaR}\_{\alpha}^{+}(H\_{\lambda}) is continuous for λ\lambda over (0,∞)(0,\infty), and
   sup\_G∈M\_ε(μ, σ) VaR\_α(G)=sup\_G∈M\_ε(μ, σ) VaR\_α^+(G)=μ+σ1+λε∫α1-t1-α,λεF-1(s)ds1-α-t1-α,λε-aλεbλε,
   where λε\lambda\_{\varepsilon} is the solution of dW​(F,Hλ)=εd\_{W}(F,H\_{\lambda})=\sqrt{\varepsilon}.
2. (ii)

   For α∈(0,1/2)\alpha\in(0,1/2), we have IQDα+​(Hλ)\mathrm{IQD}\_{\alpha}^{+}(H\_{\lambda}) is continuous for λ\lambda over (0,∞)(0,\infty), and

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | supG∈ℳε​(μ,σ)IQDα−​(G)\displaystyle\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\mathrm{IQD}\_{\alpha}^{-}(G) | =supG∈ℳε​(μ,σ)IQDα+​(G)\displaystyle=\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\mathrm{IQD}\_{\alpha}^{+}(G) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =(1+λε​∫1−α1−tα,λεF−1​(s)​dsα−tα,λε−λε​∫1−t^α,λεαF−1​(s)​ds−1t^α,λε−1+α)​σbλε,\displaystyle=\left(\frac{1+\lambda\_{\varepsilon}\int\_{1-\alpha}^{1-t\_{\alpha,\lambda\_{\varepsilon}}}F^{-1}(s)\mathrm{d}s}{\alpha-t\_{\alpha,\lambda\_{\varepsilon}}}-\frac{\lambda\_{\varepsilon}\int\_{1-\hat{t}\_{\alpha,\lambda\_{\varepsilon}}}^{\alpha}F^{-1}(s)\mathrm{d}s-1}{\hat{t}\_{\alpha,\lambda\_{\varepsilon}}-1+\alpha}\right)\frac{\sigma}{b\_{\lambda\_{\varepsilon}}}, |  |

   where λε\lambda\_{\varepsilon} is the solution of dW​(F,Hλ)=εd\_{W}(F,H\_{\lambda})=\sqrt{\varepsilon}.
3. (iii)

   For 0<α<β<10<\alpha<\beta<1 and 0<h1<h2<10<h\_{1}<h\_{2}<1 satisfying h11−β⩾h2−h1β−α\frac{h\_{1}}{1-\beta}\geqslant\frac{h\_{2}-h\_{1}}{\beta-\alpha}, we have ρg^β,αh1,h2​(Hλ)\rho\_{\hat{g}\_{\beta,\alpha}^{h\_{1},h\_{2}}}(H\_{\lambda}) is continuous for λ\lambda over (0,∞)(0,\infty),

   |  |  |  |
   | --- | --- | --- |
   |  | supG∈ℳε​(μ,σ)GlueVaRβ,αh1,h2​(G)=supG∈ℳε​(μ,σ)ρg^β,αh1,h2​(G)\displaystyle\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\mathrm{GlueVaR}\_{\beta,\alpha}^{h\_{1},h\_{2}}(G)=\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}\_{\beta,\alpha}^{h\_{1},h\_{2}}}(G) |  |
   |  |  |  |
   | --- | --- | --- |
   |  | =μ−σ​(1+λε​μF)bλε+σ​(1−h2)bλε​cα,β,λεh1,h2\displaystyle=\mu-\frac{\sigma(1+\lambda\_{\varepsilon}\mu\_{F})}{b\_{\lambda\_{\varepsilon}}}+\frac{\sigma(1-h\_{2})}{b\_{\lambda\_{\varepsilon}}}c\_{\alpha,\beta,\lambda\_{\varepsilon}}^{h\_{1},h\_{2}} |  |
   |  |  |  |
   | --- | --- | --- |
   |  | +σ​h1bλε​(1−β)​(cα,β,λεh1,h2​(1−uα,β,λεh1,h2−β)++h1​((1−β)∧uα,β,λεh1,h2)1−β+λε​∫β∨(1−uα,β,λεh1,h2)1F−1​(s)​ds)\displaystyle+\frac{\sigma h\_{1}}{b\_{\lambda\_{\varepsilon}}(1-\beta)}\left(c\_{\alpha,\beta,\lambda\_{\varepsilon}}^{h\_{1},h\_{2}}(1-u\_{\alpha,\beta,\lambda\_{\varepsilon}}^{h\_{1},h\_{2}}-\beta)\_{+}+\frac{h\_{1}((1-\beta)\wedge u\_{\alpha,\beta,\lambda\_{\varepsilon}}^{h\_{1},h\_{2}})}{1-\beta}+\lambda\_{\varepsilon}\int\_{\beta\vee(1-u\_{\alpha,\beta,\lambda\_{\varepsilon}}^{h\_{1},h\_{2}})}^{1}F^{-1}(s)\mathrm{d}s\right) |  |
   |  |  |  |
   | --- | --- | --- |
   |  | +σ​(h2−h1)bλε​(β−α)(cα,β,λεh1,h2(β∧(1−uα,β,λεh1,h2)−α)+(h2−h1)​(β−1+uα,β,λεh1,h2)+β−α\displaystyle+\frac{\sigma(h\_{2}-h\_{1})}{b\_{\lambda\_{\varepsilon}}(\beta-\alpha)}\left(c\_{\alpha,\beta,\lambda\_{\varepsilon}}^{h\_{1},h\_{2}}(\beta\wedge(1-u\_{\alpha,\beta,\lambda\_{\varepsilon}}^{h\_{1},h\_{2}})-\alpha)+\frac{(h\_{2}-h\_{1})(\beta-1+u\_{\alpha,\beta,\lambda\_{\varepsilon}}^{h\_{1},h\_{2}})\_{+}}{\beta-\alpha}\right. |  |
   |  |  |  |
   | --- | --- | --- |
   |  | +λε∫β∧(1−uα,β,λεh1,h2)βF−1(s)ds)\displaystyle~~~~~~~~~~~~~~~~~~~~~~\left.+\lambda\_{\varepsilon}\int\_{\beta\wedge(1-u\_{\alpha,\beta,\lambda\_{\varepsilon}}^{h\_{1},h\_{2}})}^{\beta}F^{-1}(s)\mathrm{d}s\right) |  |

   and the worst-case quantile for supG∈ℳε​(μ,σ)ρg^β,αh1,h2​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}\_{\beta,\alpha}^{h\_{1},h\_{2}}}(G) is hλεh\_{\lambda\_{\varepsilon}} given by ([7](https://arxiv.org/html/2511.08662v1#S3.E7 "In 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization")) with

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (gλ∗)′​(1−t)\displaystyle(g\_{\lambda}^{\*})^{\prime}(1-t) | =cα,β,λh1,h2​𝟙(α,1−uα,β,λh1,h2)​(t)+h11−β​𝟙(β∨(1−uα,β,λh1,h2),1)​(t)\displaystyle=c\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}}\mathds{1}\_{(\alpha,1-u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}})}(t)+\frac{h\_{1}}{1-\beta}\mathds{1}\_{(\beta\vee(1-u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}}),1)}(t) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +h2−h1β−α​𝟙(β∧(1−uα,β,λh1,h2),β)​(t)+λ​F−1​(t)​𝟙(0,α)∪(1−uα,β,λh1,h2,1),t∈(0,1),\displaystyle+\frac{h\_{2}-h\_{1}}{\beta-\alpha}\mathds{1}\_{(\beta\wedge(1-u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}}),\beta)}(t)+\lambda F^{-1}(t)\mathds{1}\_{(0,\alpha)\cup(1-u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}},1)},~t\in(0,1), |  |

   where λε\lambda\_{\varepsilon} is the solution of dW​(F,Hλ)=εd\_{W}(F,H\_{\lambda})=\sqrt{\varepsilon} and
   c\_α,β,λ^h\_1,h\_2=1-gα,βh1,h2(uα,β,λh1,h2)+λ∫1-uα,β,λh1,h2αF-1(s)ds1-α-uα,β,λh1,h2.

Under h11−β⩾h2−h1β−α\frac{h\_{1}}{1-\beta}\geqslant\frac{h\_{2}-h\_{1}}{\beta-\alpha}, GlueVaRβ,αh1,h2=w1​ESα+w2​ESβ+w3​VaRα\mathrm{GlueVaR}\_{\beta,\alpha}^{h\_{1},h\_{2}}=w\_{1}\mathrm{ES}\_{\alpha}+w\_{2}\mathrm{ES}\_{\beta}+w\_{3}\mathrm{VaR}\_{\alpha} with some w1,w2,w3⩾0w\_{1},w\_{2},w\_{3}\geqslant 0 satisfying w1+w2+w3=1w\_{1}+w\_{2}+w\_{3}=1. By choosing parameters, GlueVaRβ,αh1,h2\mathrm{GlueVaR}\_{\beta,\alpha}^{h\_{1},h\_{2}} can be between VaR\mathrm{VaR} and ES\mathrm{ES}, representing the attitude of more conservative than VaR\mathrm{VaR} and less conservative than ES\mathrm{ES}. Hence, (iii) of Corollary [2](https://arxiv.org/html/2511.08662v1#Thmcorollary2 "Corollary 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") gives the worst-case value of the combination of VaR\mathrm{VaR} and ES\mathrm{ES}.
Applying ([5](https://arxiv.org/html/2511.08662v1#S2.E5 "In 2 Preliminary ‣ Robust distortion risk metrics and portfolio optimization")) and Theorem [2](https://arxiv.org/html/2511.08662v1#Thmtheorem2 "Theorem 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we can also find the explicit expressions for the best-case values of VaR+\mathrm{VaR}^{+}, IQD+\mathrm{IQD}^{+} and ρgα1,α2\rho\_{g\_{\alpha\_{1},\alpha\_{2}}} similarly as Corollary [2](https://arxiv.org/html/2511.08662v1#Thmcorollary2 "Corollary 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"). The best-case value of GlueVaR can be derived using ([5](https://arxiv.org/html/2511.08662v1#S2.E5 "In 2 Preliminary ‣ Robust distortion risk metrics and portfolio optimization")) and Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization").

Note that in Theorem [2](https://arxiv.org/html/2511.08662v1#Thmtheorem2 "Theorem 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we do not give the worst-case distribution. This is because the existence of the worst-case distribution is not guaranteed if gg is not upper semicontinuous, which can be seen from the following arguments.
Under the assumption of Theorem [2](https://arxiv.org/html/2511.08662v1#Thmtheorem2 "Theorem 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), suppose the worst-case distribution exists for supG∈ℳε​(μ,σ)ρg​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G), which is denoted by G0G\_{0}. Then the conclusion in Theorem [2](https://arxiv.org/html/2511.08662v1#Thmtheorem2 "Theorem 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") implies G0G\_{0} is also a worst-case distribution for supG∈ℳε​(μ,σ)ρg^​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}}(G). The uniqueness of the worst-case distribution for supG∈ℳε​(μ,σ)ρg^​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}}(G), showed in Theroem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), implies G0=HλεG\_{0}=H\_{\lambda\_{\varepsilon}}. Using the worst-case distributions for (μF−μ)2+(σF−σ)2<ε<(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}<\varepsilon<(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}) given in Corollaries [1](https://arxiv.org/html/2511.08662v1#Thmcorollary1 "Corollary 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") and [2](https://arxiv.org/html/2511.08662v1#Thmcorollary2 "Corollary 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), direct computation shows

|  |  |  |
| --- | --- | --- |
|  | VaRα​(Hλε)=μ+σ​λ​F−1​(α)−aλεbλε,IQDα−​(Hλε)=σ​λ​F−1​(1−α)−λ​F+−1​(α)bλε,\mathrm{VaR}\_{\alpha}(H\_{\lambda\_{\varepsilon}})=\mu+\sigma\frac{\lambda F^{-1}(\alpha)-a\_{\lambda\_{\varepsilon}}}{b\_{\lambda\_{\varepsilon}}},~~\mathrm{IQD}\_{\alpha}^{-}(H\_{\lambda\_{\varepsilon}})=\sigma\frac{\lambda F^{-1}(1-\alpha)-\lambda F\_{+}^{-1}(\alpha)}{b\_{\lambda\_{\varepsilon}}}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | GlueVaRβ,αh1,h2​(Hλε)=ρg^β,αh1,h2​(Hλε)+σ​(1−h2)bλε​(λ​F−1​(α)−cα,β,λεh1,h2),\mathrm{GlueVaR}\_{\beta,\alpha}^{h\_{1},h\_{2}}(H\_{\lambda\_{\varepsilon}})=\rho\_{\hat{g}\_{\beta,\alpha}^{h\_{1},h\_{2}}}(H\_{\lambda\_{\varepsilon}})+\frac{\sigma(1-h\_{2})}{b\_{\lambda\_{\varepsilon}}}(\lambda F^{-1}(\alpha)-c\_{\alpha,\beta,\lambda\_{\varepsilon}}^{h\_{1},h\_{2}}), |  |

leading to contradictions. Hence, the worst-case distributions for VaRα\mathrm{VaR}\_{\alpha}, IQDα−\mathrm{IQD}\_{\alpha}^{-} and GlueVaRβ,αh1,h2\mathrm{GlueVaR}\_{\beta,\alpha}^{h\_{1},h\_{2}} do not exist.
The discussion of the similar issue for VaR\mathrm{VaR} with ε=∞\varepsilon=\infty can be found at e.g., Corollary 4.1 of Bernard et al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib8)) and Example 17 of Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29)).

Note that whereas it appears difficult to obtain the explicit expression of λε\lambda\_{\varepsilon} for the general g∈ℋg\in\mathcal{H}, it is possible for some special case. Specifically, we obtain the explicit expression of λε\lambda\_{\varepsilon} for concave gg.

###### Proposition 1.

If g∈ℋg\in\mathcal{H} is concave and ∫01(g′​(t))2​dt<∞\int\_{0}^{1}(g^{\prime}(t))^{2}\mathrm{d}t<\infty, then for (μF−μ)2+(σF−σ)2<ε<(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}<\varepsilon<(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}), the solution of dW​(F,Hλ)=εd\_{W}(F,H\_{\lambda})=\sqrt{\varepsilon} is given by

|  |  |  |
| --- | --- | --- |
|  | λε=−Cg,F+Cg,F2−σF2​Vg​Cε,F2−σ2​Cg,F2Cε,F2−σ2​σF2σF2,\lambda\_{\varepsilon}=\frac{-C\_{g,F}+\sqrt{C\_{g,F}^{2}-\sigma\_{F}^{2}\frac{V\_{g}C\_{\varepsilon,F}^{2}-\sigma^{2}C\_{g,F}^{2}}{C\_{\varepsilon,F}^{2}-\sigma^{2}\sigma\_{F}^{2}}}}{\sigma\_{F}^{2}}, |  |

where Cε,F=μF2+σF2+μ2+σ2−2​μ​μF−ε2⩾0C\_{\varepsilon,F}=\frac{\mu\_{F}^{2}+\sigma\_{F}^{2}+\mu^{2}+\sigma^{2}-2\mu\mu\_{F}-\varepsilon}{2}\geqslant 0, Vg=V​a​r​(g′​(V))V\_{g}=Var(g^{\prime}(V)) and Cg,F=C​o​v​(F−1​(V),g′​(1−V))⩾0C\_{g,F}=Cov(F^{-1}(V),g^{\prime}(1-V))\geqslant 0.

## 4 Bounds for Unimodal Distribution Functions with Wassertein constraint

We assume in this section that g∈ℋg\in\mathcal{H} is such that the distortion risk metrics ρg​(G)\rho\_{g}(G) admits the representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρg​(G)=∫01γ​(u)​G−1​(u)​du\displaystyle\rho\_{g}(G)=\int\_{0}^{1}\gamma(u)G^{-1}(u)\mathrm{d}u |  | (12) |

with weight function γ​(u)=∂−g​(x)|x=1−u,0<u<1\gamma(u)=\partial\_{-}g(x)|\_{x=1-u},~0<u<1, and where ∂−\partial\_{-} denotes the derivative from the left. Moreover, we assume that ∫01|γ​(u)|2​du<+∞\int\_{0}^{1}|\gamma(u)|^{2}\mathrm{d}u<+\infty. It is clear from the previous that a distortion risk metrics can also be expressed in terms of quantile functions. Specifically, we may also write ρg​(G−1)\rho\_{g}(G^{-1}) instead of ρg​(G)\rho\_{g}(G).

###### Definition 1.

A cdf G ∈ℳ2\in\mathcal{M}^{2} is unimodal if GG is convex-concave, i.e., there exists xm∈ℝx\_{m}\in\mathbb{R} (called mode) such that GG is convex on (−∞,xm)(-\infty,x\_{m}) and concave on (xm,+∞)(x\_{m},+\infty).

In what follows, we say that a (left) quantile function G−1G^{-1} is concave-convex if there exists an inflection point ξ∈[0,1]\xi\in[0,1] such that G−1G^{-1} is concave on (0,ξ)(0,\xi) and convex on (ξ,1)(\xi,1). The following lemma shows how unimodality of a cdf can be expressed in terms of its quantile function. Its proof can be found in Bernard, Kazzi and Vanduffel ([2023](https://arxiv.org/html/2511.08662v1#bib.bib7)).

###### Lemma 2.

A cdf GG is unimodal if and only if G−1G^{-1} is continuous on (0,1)(0,1) and is either concave, convex, or concave-convex.

In what follows, quantile functions for which the corresponding distribution function is unimodal will be called unimodal quantile functions. We consider the uncertainty sets

|  |  |  |
| --- | --- | --- |
|  | ℱU={G∈ℳ2,G​ is unimodal},ℱU,ξ={G∈ℱU,the inflection point is​ξ},\mathcal{F}\_{U}=\left\{G\in\mathcal{M}^{2},G\text{ is unimodal}\right\},~\mathcal{F}\_{U,\xi}=\left\{G\in\mathcal{F}\_{U},\text{the inflection point is}~\xi\right\}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ℱU,ξ​(μ,σ)={G∈ℱU,ξ:∫ℝx​dG=μ,∫ℝx2​dG=μ2+σ2},\mathcal{F}\_{U,\xi}(\mu,\sigma)=\left\{G\in\mathcal{F}\_{U,\xi}:\int\_{\mathbb{R}}x\mathrm{d}G=\mu,\int\_{\mathbb{R}}x^{2}\mathrm{d}G=\mu^{2}+\sigma^{2}\right\}, |  |

|  |  |  |
| --- | --- | --- |
|  | ℱU,ξ​(μ,σ,ε)={G∈ℱU,ξ:∫ℝx​dG=μ,∫ℝx2​dG=μ2+σ2,dW​(F,G)⩽ε},\mathcal{F}\_{U,\xi}(\mu,\sigma,\varepsilon)=\left\{G\in\mathcal{F}\_{U,\xi}:\int\_{\mathbb{R}}x\mathrm{d}G=\mu,\int\_{\mathbb{R}}x^{2}\mathrm{d}G=\mu^{2}+\sigma^{2},d\_{W}(F,G)\leqslant\sqrt{\varepsilon}\right\}, |  |

where F∈ℳ2F\in\mathcal{M}^{2}, μ∈ℝ\mu\in\mathbb{R}, σ>0\sigma>0 and ε>0\varepsilon>0. We also denote the set of all unimodal distributions with non-fixed inflection point between [ξ1,ξ2][\xi\_{1},\xi\_{2}] with 0⩽ξ1<ξ2⩽10\leqslant\xi\_{1}<\xi\_{2}\leqslant 1 by ℱU,[ξ1,ξ2]\mathcal{F}\_{U,[\xi\_{1},\xi\_{2}]}, ℱU,[ξ1,ξ2]​(μ,σ)\mathcal{F}\_{U,[\xi\_{1},\xi\_{2}]}(\mu,\sigma) and ℱU,[ξ1,ξ2]​(μ,σ,ε)\mathcal{F}\_{U,[\xi\_{1},\xi\_{2}]}(\mu,\sigma,\varepsilon), respectively. Note that ℱU,[ξ1,ξ2]=∪ξ∈[ξ1,ξ2]ℱU,ξ\mathcal{F}\_{U,[\xi\_{1},\xi\_{2}]}=\cup\_{\xi\in[\xi\_{1},\xi\_{2}]}\mathcal{F}\_{U,\xi}, ℱU,[ξ1,ξ2]​(μ,σ)=∪ξ∈[ξ1,ξ2]ℱU,ξ​(μ,σ)\mathcal{F}\_{U,[\xi\_{1},\xi\_{2}]}(\mu,\sigma)=\cup\_{\xi\in[\xi\_{1},\xi\_{2}]}\mathcal{F}\_{U,\xi}(\mu,\sigma) and ℱU,[ξ1,ξ2]​(μ,σ,ε)=∪ξ∈[ξ1,ξ2]ℱU,ξ​(μ,σ,ε)\mathcal{F}\_{U,[\xi\_{1},\xi\_{2}]}(\mu,\sigma,\varepsilon)=\cup\_{\xi\in[\xi\_{1},\xi\_{2}]}\mathcal{F}\_{U,\xi}(\mu,\sigma,\varepsilon).

In this section, we study bounds for distortion risk metrics in the case of uncertainty sets that are Wasserstein balls containing unimodal distributions with given mean and variance, and with either given or non-fixed inflection points:

as well as

### 4.1 Fixed inflection point

Recall that ℱU,ξ−1\mathcal{F}^{-1}\_{U,\xi} is the collection of all quantile functions of distribution functions in ℱU,ξ\mathcal{F}\_{U,\xi}.
Note that ℱU,ξ−1\mathcal{F}^{-1}\_{U,\xi} is a closed convex cone, which implies that the L2L\_{2}-projection of a function (with domain (0,1)(0,1)) on this set is well defined and unique; see e.g., Theorems 2.1 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12)).
Denote by γξ↑\gamma^{\uparrow}\_{\xi} the L2L\_{2}-projection of γ\gamma on FU,ξ−1{F}^{-1}\_{U,\xi} and let a^ξ=E​(γξ↑​(V))\hat{a}\_{\xi}=E(\gamma^{\uparrow}\_{\xi}(V)) and b^ξ=V​a​r​(γξ↑​(V))\hat{b}\_{\xi}=\sqrt{Var(\gamma^{\uparrow}\_{\xi}(V))} with V∼U​(0,1)V\sim U(0,1). In light of Corollary 2.3 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12)), we have a^ξ=∫01γξ↑​(u)​du=g​(1)\hat{a}\_{\xi}=\int\_{0}^{1}\gamma\_{\xi}^{\uparrow}(u)\mathrm{d}u=g(1) and b^ξ=∫01(γξ↑​(u)−g​(1))2​du\hat{b}\_{\xi}=\sqrt{\int\_{0}^{1}\left(\gamma\_{\xi}^{\uparrow}(u)-g(1)\right)^{2}\mathrm{d}u}.

###### Proposition 2 (Bounds for unimodal distribution functions with a given inflection point).

Suppose γξ↑\gamma^{\uparrow}\_{\xi} is not a constant. Then it holds that

|  |  |  |
| --- | --- | --- |
|  | supG∈ℱU,ξ​(μ,σ)ρg​(G)=μ​g​(1)+σ​∫01(γξ↑​(u)−g​(1))2​du,\sup\_{G\in\mathcal{F}\_{U,\xi}(\mu,\sigma)}\rho\_{g}(G)=\mu g(1)+\sigma\sqrt{\int\_{0}^{1}\left(\gamma\_{\xi}^{\uparrow}(u)-g(1)\right)^{2}\mathrm{d}u}, |  |

and
hξ↑​(u):=μ+σ​(γξ↑−a^ξb^ξ)h^{\uparrow}\_{\xi}(u):=\mu+\sigma\left(\frac{\gamma^{\uparrow}\_{\xi}-\hat{a}\_{\xi}}{\hat{b}\_{\xi}}\right) is the unique worst-case quantile.

Note that if unimodality is removed, then the uncertainty set becomes ℳ∞​(μ,σ)\mathcal{M}\_{\infty}(\mu,\sigma) . Let γ↑\gamma^{\uparrow} be the projection of γ\gamma on ℳ∞−1​(μ,σ)\mathcal{M}\_{\infty}^{-1}(\mu,\sigma). Then Corollay 3.9 in Bernard et al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib8)) and Theorem 5 and Remark 2 of Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29)) show that

|  |  |  |
| --- | --- | --- |
|  | supG∈ℳ∞​(μ,σ)ρg​(G)=μ​g​(1)+σ​∫01(γ↑​(u)−g​(1))2​du\sup\_{G\in\mathcal{M}\_{\infty}(\mu,\sigma)}\rho\_{g}(G)=\mu g(1)+\sigma\sqrt{\int\_{0}^{1}\left(\gamma^{\uparrow}(u)-g(1)\right)^{2}\mathrm{d}u} |  |

if γ↑\gamma^{\uparrow} is not a constant. Moreover, the worst-case quantile is given by μ+σ​(γ↑−g​(1)∫01(γ↑​(u)−g​(1))2​du)\mu+\sigma\left(\frac{\gamma^{\uparrow}-g(1)}{\sqrt{\int\_{0}^{1}\left(\gamma^{\uparrow}(u)-g(1)\right)^{2}\mathrm{d}u}}\right).

By Theorem 2.8 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12)), we have

|  |  |  |
| --- | --- | --- |
|  | ∫01(γ↑​(u)−g​(1))2​du⩾∫01(γξ↑​(u)−g​(1))2​du+∫01(γ↑​(u)−γξ↑​(u))2​du.\int\_{0}^{1}\left(\gamma^{\uparrow}(u)-g(1)\right)^{2}\mathrm{d}u\geqslant\int\_{0}^{1}\left(\gamma\_{\xi}^{\uparrow}(u)-g(1)\right)^{2}\mathrm{d}u+\int\_{0}^{1}\left(\gamma^{\uparrow}(u)-\gamma\_{\xi}^{\uparrow}(u)\right)^{2}\mathrm{d}u. |  |

Hence, if γ↑∉ℱU,ξ−1​(μ,σ)\gamma^{\uparrow}\notin\mathcal{F}^{-1}\_{U,\xi}(\mu,\sigma), the information on unimodality can effectively reduce the worst-case vaule of the distortion risk metrics.

Moreover, the worst-case distributions without the constraint of unimodality for ES\mathrm{ES} and RVaR\mathrm{RVaR} are two-point distributions, which is not desirable practically; see e.g. Bernard et al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib8)) or Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29)). However, with the constraint of unimodality, the worst-case distribution is typically not discrete.

In Li et al. ([2018](https://arxiv.org/html/2511.08662v1#bib.bib25)), the Range-Value-at-Risk (γ​(u)=1β−α​𝟙(α,β)\gamma(u)=\frac{1}{\beta-\alpha}\mathds{1}\_{(\alpha,\beta)} with 0⩽α<β⩽10\leqslant\alpha<\beta\leqslant 1) was considered with mean, variance and unimodal constraints without fixing the inflection point. Our result in Proposition [2](https://arxiv.org/html/2511.08662v1#Thmproposition2 "Proposition 2 (Bounds for unimodal distribution functions with a given inflection point). ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization") is valid for all distortion risk metrics with absolutely continuous distortion functions gg, and it is more accurate with a fixed inflection point. By maximizing the worst-case values with different inflection points, we can immediately derive the results with unknown inflection points, which is discussed in Section [4.2](https://arxiv.org/html/2511.08662v1#S4.SS2 "4.2 Unknown inflection points ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization").

Optimal solutions to problem ([13a](https://arxiv.org/html/2511.08662v1#S4.E13.1 "In 13 ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")) are thus obtained once the projection γξ↑\gamma^{\uparrow}\_{\xi} of the function γ\gamma on the set FU,ξ−1{F}^{-1}\_{U,\xi} is established. Whilst computing such projection in closed-form is in general very difficult, it can always be numerically obtained with any desired degree of precision.

The next proposition shows that for a step function γ\gamma, its projection on FU,ξ−1{F}^{-1}\_{U,\xi} is a piecewise linear function.

###### Proposition 3.

Let γ\gamma be a step function with nn steps, i.e., γ​(u)=∑i=1nyi​𝟙(xi−1,xi)​(u)\gamma(u)=\sum\_{i=1}^{n}y\_{i}\mathds{1}\_{(x\_{i-1},x\_{i})}(u) with 0=x0<x1<⋯<xn=10=x\_{0}<x\_{1}<\dots<x\_{n}=1 and yi∈ℝy\_{i}\in\mathbb{R}. Then γξ↑\gamma^{\uparrow}\_{\xi} is a piecewise linear function with at most 2​n+22n+2 pieces. More specifically, if ξ=xi0\xi=x\_{i\_{0}} for some i0=0,1,…,ni\_{0}=0,1,\dots,n, then γξ↑\gamma^{\uparrow}\_{\xi} satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂γξ↑​(u)/∂u\displaystyle\partial\gamma^{\uparrow}\_{\xi}(u)/\partial u | =∑i=1n(ci−​𝟙(xi−1,ai)​(u)+ci+​𝟙(ai,xi)​(u))\displaystyle=\sum\_{i=1}^{n}\left(c\_{i}^{-}\mathds{1}\_{(x\_{i-1},a\_{i})}(u)+c\_{i}^{+}\mathds{1}\_{(a\_{i},x\_{i})}(u)\right) |  | (15) |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γξ↑​(0)\displaystyle\gamma^{\uparrow}\_{\xi}(0) | =g​(1)−∑i=1n(ci−​(ai−xi−1)+ci+​(xi−ai))\displaystyle=g(1)-\sum\_{i=1}^{n}\left(c\_{i}^{-}(a\_{i}-x\_{i-1})+c\_{i}^{+}(x\_{i}-a\_{i})\right) |  | (16) |

with the parameters constrained in 𝒟n:={(𝐚,𝐜):ai∈[xi−1,xi],i=1,…,n\mathcal{D}\_{n}:=\{(\mathbf{a},\mathbf{c}):a\_{i}\in[x\_{i-1},x\_{i}],~i=1,\dots,n, c1−⩾c1+⩾⋯⩾ci0−⩾ci0+⩾0c\_{1}^{-}\geqslant c\_{1}^{+}\geqslant\dots\geqslant c\_{i\_{0}}^{-}\geqslant c\_{i\_{0}}^{+}\geqslant 0, 0⩽ci0+1−⩽ci0+1+⩽…cn−⩽cn+}0\leqslant c\_{i\_{0}+1}^{-}\leqslant c\_{i\_{0}+1}^{+}\leqslant\dots c\_{n}^{-}\leqslant c\_{n}^{+}\} with 𝐚=(a1,…,an)\mathbf{a}=(a\_{1},\dots,a\_{n}) and 𝐜=(c1−,c1+,…,cn−,cn+)\mathbf{c}=(c\_{1}^{-},c\_{1}^{+},\dots,c\_{n}^{-},c\_{n}^{+}).

The optimal parameters (𝐚∗,𝐜∗)(\mathbf{a}^{\*},\mathbf{c}^{\*}) are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg​min(𝐚,𝐜)∈𝒟n​∑i=1n\displaystyle\operatorname\*{arg\,min}\_{(\mathbf{a},\mathbf{c})\in\mathcal{D}\_{n}}\sum\_{i=1}^{n} | {(ai−xi−1)[(ei+)2+ei+ei−+(ei−)2]\displaystyle\left\{(a\_{i}-x\_{i-1})\left[(e\_{i}^{+})^{2}+e\_{i}^{+}e\_{i}^{-}+(e\_{i}^{-})^{2}\right]\right. |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(xi−ai)[(ei++ci+(xi−ai))2+(ei++ci+(xi−ai))ei++(ei+)2]},\displaystyle~\left.+(x\_{i}-a\_{i})\left[(e\_{i}^{+}+c\_{i}^{+}(x\_{i}-a\_{i}))^{2}+(e\_{i}^{+}+c\_{i}^{+}(x\_{i}-a\_{i}))e\_{i}^{+}+(e\_{i}^{+})^{2}\right]\right\}, |  | (17) |

where ei−=g​(1)−∑j=in(cj−​(aj−xj−1)+cj+​(xj−aj))−yie\_{i}^{-}=g(1)-\sum\_{j=i}^{n}\left(c\_{j}^{-}(a\_{j}-x\_{j-1})+c\_{j}^{+}(x\_{j}-a\_{j})\right)-y\_{i}, ei+=ei−+ci−​(ai−xi−1),i=1,…,ne\_{i}^{+}=e\_{i}^{-}+c\_{i}^{-}(a\_{i}-x\_{i-1}),~i=1,\dots,n.

If ξ∈(xi0−1,xi0)\xi\in(x\_{i\_{0}-1},x\_{i\_{0}}) for some i0=1,…,ni\_{0}=1,\dots,n, then we rewrite γ​(u)=∑i=1n+1yi′​𝟙(xi−1′,xi′)​(u)\gamma(u)=\sum\_{i=1}^{n+1}y\_{i}^{\prime}\mathds{1}\_{(x\_{i-1}^{\prime},x\_{i}^{\prime})}(u) with 0=x0′<x1′<⋯<xn+1′=10=x\_{0}^{\prime}<x\_{1}^{\prime}<\dots<x\_{n+1}^{\prime}=1, yi′∈ℝy\_{i}^{\prime}\in\mathbb{R} and xi0′=ξx\_{i\_{0}}^{\prime}=\xi. Then it is transferred to the previous case.

As it is shown in Proposition [3](https://arxiv.org/html/2511.08662v1#Thmproposition3 "Proposition 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"), for a step function γ\gamma with nn steps, finding its projection γξ↑\gamma^{\uparrow}\_{\xi} amounts to solving an optimization problem ([3](https://arxiv.org/html/2511.08662v1#S4.Ex4 "Proposition 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")) with 3​n3n or 3​n+33n+3 parameters depending on the location of ξ\xi. In light of ([15](https://arxiv.org/html/2511.08662v1#S4.E15 "In Proposition 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")) and ([16](https://arxiv.org/html/2511.08662v1#S4.E16 "In Proposition 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | γξ↑​(u)\displaystyle\gamma^{\uparrow}\_{\xi}(u) | =ei−+yi+ci−​(u−xi−1),u∈[xi−1,ai),\displaystyle=e\_{i}^{-}+y\_{i}+c\_{i}^{-}(u-x\_{i-1}),~u\in[x\_{i-1},a\_{i}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | γξ↑​(u)\displaystyle\gamma^{\uparrow}\_{\xi}(u) | =ei++yi+ci+​(u−ai),u∈[ai,xi),i=1,…,n.\displaystyle=e\_{i}^{+}+y\_{i}+c\_{i}^{+}(u-a\_{i}),~u\in[a\_{i},x\_{i}),~i=1,\dots,n. |  |

For a general γ\gamma, it can be approximated with any precision using step functions γn\gamma\_{n}. Furthermore, let γξ,n↑\gamma^{\uparrow}\_{\xi,n} denote the projection of γn\gamma\_{n} on FU,ξ−1{F}^{-1}\_{U,\xi}, and let
hξ,n↑=μ​g​(1)+σ​γξ,n↑−a^ξ,nb^ξ,nh^{\uparrow}\_{\xi,n}=\mu g(1)+\sigma\frac{\gamma\_{\xi,n}^{\uparrow}-\hat{a}\_{\xi,n}}{\hat{b}\_{\xi,n}}, where a^ξ,n=𝔼​(γξ,n↑​(V))\hat{a}\_{\xi,n}=\mathbb{E}(\gamma\_{\xi,n}^{\uparrow}(V)) and b^ξ,n=V​a​r​(γξ,n↑​(V))=∫01(γξ,n↑​(u)−a^ξ,n)2​du\hat{b}\_{\xi,n}=\sqrt{Var(\gamma\_{\xi,n}^{\uparrow}(V))}=\sqrt{\int\_{0}^{1}\left(\gamma\_{\xi,n}^{\uparrow}(u)-\hat{a}\_{\xi,n}\right)^{2}\mathrm{d}u} with V∼U​(0,1)V\sim U(0,1). Let ∥⋅∥2\|\cdot\|\_{2} denote the L2L\_{2} norm on ℱU,ξ−1\mathcal{F}^{-1}\_{U,\xi}.

###### Proposition 4.

If γξ↑\gamma^{\uparrow}\_{\xi} and γξ,n↑\gamma^{\uparrow}\_{\xi,n} are not constants, we have

|  |  |  |
| --- | --- | --- |
|  | ‖γξ,n↑−γξ↑‖2⩽‖γn−γ‖2,‖hξ,n↑−hξ↑‖2⩽(2+2​‖γ‖2+‖γn‖2b^ξ)​σb^ξ​‖γn−γ‖2,\|\gamma^{\uparrow}\_{\xi,n}-\gamma^{\uparrow}\_{\xi}\|\_{2}\leqslant\|\gamma\_{n}-\gamma\|\_{2},~~\|h^{\uparrow}\_{\xi,n}-h^{\uparrow}\_{\xi}\|\_{2}\leqslant\left(2+\frac{2\|\gamma\|\_{2}+\|\gamma\_{n}\|\_{2}}{\hat{b}\_{\xi}}\right)\frac{\sigma}{\hat{b}\_{\xi}}\|\gamma\_{n}-\gamma\|\_{2}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | |ρg​(hξ↑)−ρg​(hξ,n↑)|⩽σ​(2​‖γ‖2+‖γn‖2)​‖γn−γ‖2b^ξ.|\rho\_{g}(h^{\uparrow}\_{\xi})-\rho\_{g}(h^{\uparrow}\_{\xi,n})|\leqslant\frac{\sigma(2\|\gamma\|\_{2}+\|\gamma\_{n}\|\_{2})\|\gamma\_{n}-\gamma\|\_{2}}{\hat{b}\_{\xi}}. |  |

The inequalities in Proposition [4](https://arxiv.org/html/2511.08662v1#Thmproposition4 "Proposition 4. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization") show that the errors can be controlled by the distance between the step function γn\gamma\_{n} and original function γ\gamma, which guarantees the efficiency of our approximation method using step functions to approximate the worst-case distribution and the worst-case value of the robust distortion risk metrics.

Next, we see some concrete examples to find the projection of γ\gamma.

###### Example 1.

1. (i)

   For GD\mathrm{GD}, γ​(u)=1−2​u,u∈(0,1)\gamma(u)=1-2u,~u\in(0,1). Hence, γξ↑​(u)=1−2​u,u∈(0,1)\gamma^{\uparrow}\_{\xi}(u)=1-2u,~u\in(0,1).
2. (ii)

   For MMD\mathrm{MMD}, g​(t)=t∧(1−t),t∈[0,1]g(t)=t\wedge(1-t),~t\in[0,1]. Hence, γ​(u)=−𝟙(0,1/2)+𝟙(1/2,1)\gamma(u)=-\mathds{1}\_{(0,1/2)}+\mathds{1}\_{(1/2,1)}. If ξ=1/2\xi=1/2, then
   γξ↑​(u)=3​(u−1/2),u∈(0,1)\gamma^{\uparrow}\_{\xi}(u)=3(u-1/2),~u\in(0,1).

Next, we consider the uncertainty set ℱU,ξ​(μ,σ,ε)\mathcal{F}\_{U,\xi}(\mu,\sigma,\varepsilon) with F∈ℳ2F\in\mathcal{M}^{2}, μ∈ℝ\mu\in\mathbb{R}, σ>0\sigma>0 and ε>0\varepsilon>0. For λ>0\lambda>0, let kλ​(u)=γ​(u)+λ​F−1​(u)k\_{\lambda}(u)=\gamma(u)+\lambda F^{-1}(u), and kλ,ξ↑k\_{\lambda,\xi}^{\uparrow} be the L2L\_{2}-projection of kλk\_{\lambda} on ℱU,ξ−1\mathcal{F}\_{U,\xi}^{-1} for ξ∈[0,1]\xi\in[0,1]. Moreover, for λ>0\lambda>0, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | hλ,ξ=μ+kλ,ξ↑−aλ,ξbλ,ξ​σ,h\_{\lambda,\xi}=\mu+\frac{k\_{\lambda,\xi}^{\uparrow}-a\_{\lambda,\xi}}{b\_{\lambda,\xi}}\sigma, |  | (18) |

where aλ,ξ=E​(kλ,ξ↑​(V))=g​(1)+λ​μFa\_{\lambda,\xi}=E(k\_{\lambda,\xi}^{\uparrow}(V))=g(1)+\lambda\mu\_{F} and bλ,ξ=V​a​r​(kλ,ξ↑​(V))b\_{\lambda,\xi}=\sqrt{Var(k\_{\lambda,\xi}^{\uparrow}(V))} with V∼U​(0,1)V\sim U(0,1). Moreover, let c1=C​o​r​r​(F−1​(V),γξ↑​(V))c\_{1}=Corr(F^{-1}(V),\gamma\_{\xi}^{\uparrow}(V)).

Next, we discuss the range of ε\varepsilon for the problem ([13b](https://arxiv.org/html/2511.08662v1#S4.E13.2 "In 13 ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")) that is meaningful to study.
Let Fξ−1,↑F\_{\xi}^{-1,\uparrow} be the L2L\_{2}-projection of F−1F^{-1} on ℱU,ξ−1\mathcal{F}\_{U,\xi}^{-1} and c^0=C​o​r​r​(F−1​(V),Fξ−1,↑​(V))\hat{c}\_{0}=Corr(F^{-1}(V),F\_{\xi}^{-1,\uparrow}(V)) if Fξ−1,↑F\_{\xi}^{-1,\uparrow} is not a constant. Clearly, E​(Fξ−1,↑​(V))=μFE(F\_{\xi}^{-1,\uparrow}(V))=\mu\_{F}.

###### Lemma 3.

Suppose Fξ−1,↑F\_{\xi}^{-1,\uparrow} is not a constant. If ε<(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c^0)\varepsilon<(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-\hat{c}\_{0}), then
ℱU,ξ−1​(μ,σ,ε)=∅\mathcal{F}\_{U,\xi}^{-1}(\mu,\sigma,\varepsilon)=\varnothing; If ε=(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c^0)\varepsilon=(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-\hat{c}\_{0}), then ℱU,ξ−1​(μ,σ)={Fξ−1,↑−μFσF↑​σ+μ}\mathcal{F}\_{U,\xi}^{-1}(\mu,\sigma)=\left\{\frac{F\_{\xi}^{-1,\uparrow}-\mu\_{F}}{\sigma\_{F}^{\uparrow}}\sigma+\mu\right\}, where σF↑=V​a​r​(Fξ−1,↑​(V))\sigma\_{F}^{\uparrow}=\sqrt{Var(F\_{\xi}^{-1,\uparrow}(V))}.

Due to Lemma [3](https://arxiv.org/html/2511.08662v1#Thmlemma3 "Lemma 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"), in what follows, we only focus on the case ε>(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c^0)\varepsilon>(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-\hat{c}\_{0}), where ℱU,ξ\mathcal{F}\_{U,\xi} contains infinitely many distributions.

The following lemma shows the continuity of C​o​r​r​(F−1​(V),kλ,ξ↑​(V))Corr(F^{-1}(V),k\_{\lambda,\xi}^{\uparrow}(V)) with respect to λ\lambda, which is crucial to our main result in this subsection.

###### Lemma 4.

Suppose F−1∈ℳ2F^{-1}\in\mathcal{M}^{2}, Fξ−1,↑F\_{\xi}^{-1,\uparrow} is not a constant, and kλ,ξ↑k\_{\lambda,\xi}^{\uparrow} is not constant for all λ>0\lambda>0. Then we have C​o​r​r​(F−1​(V),kλ,ξ↑​(V))Corr(F^{-1}(V),k\_{\lambda,\xi}^{\uparrow}(V)) is continuous with respect to λ\lambda on [0,∞)[0,\infty), and

|  |  |  |
| --- | --- | --- |
|  | limλ→∞C​o​r​r​(F−1​(V),kλ,ξ↑​(V))=C​o​r​r​(F−1​(V),Fξ−1,↑​(V)).\lim\_{\lambda\to\infty}Corr(F^{-1}(V),k\_{\lambda,\xi}^{\uparrow}(V))=Corr(F^{-1}(V),F\_{\xi}^{-1,\uparrow}(V)). |  |

Note that in Lemma [4](https://arxiv.org/html/2511.08662v1#Thmlemma4 "Lemma 4. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"), the value of c^0\hat{c}\_{0} depends on whether F−1∈ℱU,ξ−1F^{-1}\in\mathcal{F}^{-1}\_{U,\xi}. If F−1∈ℱU,ξ−1F^{-1}\in\mathcal{F}^{-1}\_{U,\xi}, then c^0=1\hat{c}\_{0}=1; If F−1∉ℱU,ξ−1F^{-1}\notin\mathcal{F}^{-1}\_{U,\xi}, one can easily check that
c^0<1.\hat{c}\_{0}<1.

###### Theorem 3.

Assume F−1∈ℳ2F^{-1}\in\mathcal{M}^{2}, Fξ−1,↑F\_{\xi}^{-1,\uparrow} is not a constant, and kλ,ξ↑k\_{\lambda,\xi}^{\uparrow} are not constants for all λ>0\lambda>0.

1. (i)

   If (μF−μ)2+(σF−σ)2+2​σF​σ​(1−c^0)<ε<(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c1)(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-\hat{c}\_{0})<\varepsilon<(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{1}), then
   hλε,ξ​(u)h\_{\lambda\_{\varepsilon},\xi}(u) given by ([18](https://arxiv.org/html/2511.08662v1#S4.E18 "In 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")) is the unique worst-case quantile
   to problem ([13b](https://arxiv.org/html/2511.08662v1#S4.E13.2 "In 13 ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")) and supG∈ℱU,ξ​(μ,σ,ε)ρg​(G)=μ​g​(1)+σbλε,ξ​(∫01kλε,ξ↑​(u)​γ​(u)​du−g​(1)​(g​(1)+λε​μF))\sup\_{G\in\mathcal{F}\_{U,\xi}(\mu,\sigma,\varepsilon)}\rho\_{g}(G)=\mu g(1)+\frac{\sigma}{b\_{\lambda\_{\varepsilon},\xi}}\left(\int\_{0}^{1}k\_{\lambda\_{\varepsilon},\xi}^{\uparrow}(u)\gamma(u)\mathrm{d}u-g(1)(g(1)+\lambda\_{\varepsilon}\mu\_{F})\right), where λε>0\lambda\_{\varepsilon}>0 is the solution of dW​(hλ,ξ,F−1)=εd\_{W}(h\_{\lambda,\xi},F^{-1})=\sqrt{\varepsilon}.
2. (ii)

   Let ε⩾(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c1)\varepsilon\geqslant(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{1}). If γξ↑\gamma\_{\xi}^{\uparrow} is not a constant, then the unique worst-case quantile to problem ([13b](https://arxiv.org/html/2511.08662v1#S4.E13.2 "In 13 ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")) is hξ↑​(u)=μ+σ​(γξ↑−a^ξb^ξ)h^{\uparrow}\_{\xi}(u)=\mu+\sigma\left(\frac{\gamma^{\uparrow}\_{\xi}-\hat{a}\_{\xi}}{\hat{b}\_{\xi}}\right);
   If γξ↑\gamma\_{\xi}^{\uparrow} is a constant, then supG∈ℱU,ξ​(μ,σ)ρg​(G)=g​(1)​μ\sup\_{G\in\mathcal{F}\_{U,\xi}(\mu,\sigma)}\rho\_{g}(G)=g(1)\mu.

For the case with absolutely continuous gg, Theorem [3](https://arxiv.org/html/2511.08662v1#Thmtheorem3 "Theorem 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization") improves the results of Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") by imposing unimodality with a fixed inflection point on the underlying distributions. This implies that the worst-case value is reduced by adding this additional information in the uncertainty sets. The computation of the worst-case values is not straightforward due to the complexity of the projection and no explicit expression for λε\lambda\_{\varepsilon}. The numerical method heavily relies on Propositions [3](https://arxiv.org/html/2511.08662v1#Thmproposition3 "Proposition 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization") and [4](https://arxiv.org/html/2511.08662v1#Thmproposition4 "Proposition 4. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization").

### 4.2 Unknown inflection points

Different from ℱU,ξ−1\mathcal{F}^{-1}\_{U,\xi}, the set ℱU,[ξ1,ξ2]−1\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]} with 0⩽ξ1<ξ2⩽10\leqslant\xi\_{1}<\xi\_{2}\leqslant 1 is not convex. Hence, Theorem 2.1 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12)) cannot guarantee the existence and uniqueness of the projection. To compute the worst-case value of the distortion risk metrics, we can apply Proposition [2](https://arxiv.org/html/2511.08662v1#Thmproposition2 "Proposition 2 (Bounds for unimodal distribution functions with a given inflection point). ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization") and Theorem [3](https://arxiv.org/html/2511.08662v1#Thmtheorem3 "Theorem 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization") and the following relations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supG∈ℱU,[ξ1,ξ2]​(μ,σ)ρg​(G)\displaystyle\sup\_{G\in\mathcal{F}\_{U,[\xi\_{1},\xi\_{2}]}(\mu,\sigma)}\rho\_{g}(G) | =supξ∈[ξ1,ξ2]supG∈ℱU,ξ​(μ,σ)ρg​(G),\displaystyle=\sup\_{\xi\in[\xi\_{1},\xi\_{2}]}\sup\_{G\in\mathcal{F}\_{U,\xi}(\mu,\sigma)}\rho\_{g}(G), |  | (19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supG∈ℱU,[ξ1,ξ2]​(μ,σ,ε)ρg​(G)\displaystyle\sup\_{G\in\mathcal{F}\_{U,[\xi\_{1},\xi\_{2}]}(\mu,\sigma,\varepsilon)}\rho\_{g}(G) | =supξ∈[ξ1,ξ2]supG∈ℱU,ξ​(μ,σ,ε)ρg​(G).\displaystyle=\sup\_{\xi\in[\xi\_{1},\xi\_{2}]}\sup\_{G\in\mathcal{F}\_{U,\xi}(\mu,\sigma,\varepsilon)}\rho\_{g}(G). |  | (20) |

Although the above formulas look a bit complicated, it might be applicable numerically. Luckily, the problem ([14a](https://arxiv.org/html/2511.08662v1#S4.E14.1 "In 14 ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")) can be solved using the same method as the case with given inflection point although ℱU,[ξ1,ξ2]−1\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]} is not convex. The existence of the L2L\_{2}-projection of a function over (0,1)(0,1) on the set ℱU,[ξ1,ξ2]−1\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]} can be shown as below.

###### Lemma 5.

For any γ\gamma satisfying ∫01|γ​(u)|2​du<+∞\int\_{0}^{1}|\gamma(u)|^{2}\mathrm{d}u<+\infty, there exists γξ1,ξ2↑∈ℱU,[ξ1,ξ2]−1\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}\in\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]} such that γξ1,ξ2↑∈arg⁡minh∈ℱU,[ξ1,ξ2]−1⁡‖γ−h‖2\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}\in\arg\min\_{h\in\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]}}\|\gamma-h\|\_{2}.

Note that in Lemma [5](https://arxiv.org/html/2511.08662v1#Thmlemma5 "Lemma 5. ‣ 4.2 Unknown inflection points ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"), the uniqueness of the projection is not stated because the uniqueness may not hold due to the lack of convexity for the set ℱU,[ξ1,ξ2]−1\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]}.

Next, we study bounds for distortion risk metrics in case that the inflection point is not known. By Lemma [5](https://arxiv.org/html/2511.08662v1#Thmlemma5 "Lemma 5. ‣ 4.2 Unknown inflection points ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"), the projection of γ\gamma onto FU,[ξ1,ξ2]−1{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]} is well-defined. Denote by γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} as one of the L2L\_{2}-projection of γ\gamma on ℱU,[ξ1,ξ2]−1\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]}, and let aξ1,ξ2=E​(γξ1,ξ2↑​(V))a\_{\xi\_{1},\xi\_{2}}=E(\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(V)) and bξ1,ξ2=S​t​d​e​v​(γξ1,ξ2↑​(V))b\_{\xi\_{1},\xi\_{2}}=Stdev(\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(V)) with V∼U​(0,1)V\sim U(0,1).

###### Proposition 5 (Bounds for distortion risk measures for unimodal distribution functions).

Suppose γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} is not a constant. Then hξ1,ξ2↑​(u):=μ+σ​(γξ1,ξ2↑−aξ1,ξ2bξ1,ξ2)h\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u):=\mu+\sigma\left(\frac{\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}-a\_{\xi\_{1},\xi\_{2}}}{b\_{\xi\_{1},\xi\_{2}}}\right) is a
worst-case quantile to the problem ([14a](https://arxiv.org/html/2511.08662v1#S4.E14.1 "In 14 ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")).

Note that the worst-case distribution of Problem ([14a](https://arxiv.org/html/2511.08662v1#S4.E14.1 "In 14 ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")) given in Proposition [5](https://arxiv.org/html/2511.08662v1#Thmproposition5 "Proposition 5 (Bounds for distortion risk measures for unimodal distribution functions). ‣ 4.2 Unknown inflection points ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization") may not be unique due to the non-convexity of ℱU,[ξ1,ξ2]−1\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]}. This fact can also been seen from ([19](https://arxiv.org/html/2511.08662v1#S4.E19 "In 4.2 Unknown inflection points ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")), where there might be two different ξ∈[ξ1,ξ2]\xi\in[\xi\_{1},\xi\_{2}] such that the largest value is obtained at the quantile functions with two different inflection points respectively.
Moreover, the conclusion in Proposition [5](https://arxiv.org/html/2511.08662v1#Thmproposition5 "Proposition 5 (Bounds for distortion risk measures for unimodal distribution functions). ‣ 4.2 Unknown inflection points ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization") covers some result in Li et al. ([2018](https://arxiv.org/html/2511.08662v1#bib.bib25)), where a special case of γ\gamma, γ​(u)=1β−α​𝟙(α,β)​(u)\gamma(u)=\frac{1}{\beta-\alpha}\mathds{1}\_{(\alpha,\beta)}(u) with 0<α<β⩽10<\alpha<\beta\leqslant 1, was considered.

Due to the non-convexity of ℱU,[ξ1,ξ2]−1\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]}, it is difficult to show the similar result as in Lemma [4](https://arxiv.org/html/2511.08662v1#Thmlemma4 "Lemma 4. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization") for the case with unknown inflection point. Hence, the problem ([14b](https://arxiv.org/html/2511.08662v1#S4.E14.2 "In 14 ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")) cannot be solved using the same method as that of Theorem [3](https://arxiv.org/html/2511.08662v1#Thmtheorem3 "Theorem 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"). However, we can apply Theorem [3](https://arxiv.org/html/2511.08662v1#Thmtheorem3 "Theorem 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization") and ([20](https://arxiv.org/html/2511.08662v1#S4.E20 "In 4.2 Unknown inflection points ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")) to solve problem ([14b](https://arxiv.org/html/2511.08662v1#S4.E14.2 "In 14 ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")).

## 5 Robust portfolio optimization

In this section, we will focus on the application of our results to robust portfolio optimization under two different uncertainty sets characterized by: i) mean-variance constraint and probability constraint via Wasserstein metric on the random vector of the return; ii) one additional constraint, unimodality, on the return of the portfolios.

### 5.1 Mean-variance and Wasserstein distance constraints

Suppose Xi,i=1,…,nX\_{i},~i=1,\dots,n are the negative returns of investing 1 dollar on nn different assets in the market and (w1,…,wn)∈𝒜⊆Δn(w\_{1},\dots,w\_{n})\in\mathcal{A}\subseteq\Delta\_{n} represents the interested position of the invested portfolio, where Δn={(w1,…,wn):wi⩾0,∑i=1nwi=1}\Delta\_{n}=\{(w\_{1},\dots,w\_{n}):w\_{i}\geqslant 0,~\sum\_{i=1}^{n}w\_{i}=1\}. Hence, the negative return of the portfolio is given by ∑i=1nwi​Xi\sum\_{i=1}^{n}w\_{i}X\_{i}. Suppose only partial information is known about return vector (X1,…,Xn)(X\_{1},\dots,X\_{n}), which are the means μi\mu\_{i}, the covariance matrix Σ0\Sigma\_{0} and the Wasserstein distance between F𝐗F\_{\mathbf{X}} and the reference distribution F𝐗0F\_{\mathbf{X}\_{0}} with dW(n)​(F𝐗,F𝐗0)⩽εd\_{W}^{(n)}(F\_{\mathbf{X}},F\_{\mathbf{X}\_{0}})\leqslant\sqrt{\varepsilon} for ε>0\varepsilon>0. The Wasserstein metric between two nn-dimentional distribution FF and GG is defined by

|  |  |  |
| --- | --- | --- |
|  | dW(n)​(F,G)=inf𝐗∼F,𝐘∼G(𝔼​(‖𝐗−𝐘‖22))1/2;d\_{W}^{(n)}(F,G)=\inf\_{\mathbf{X}\sim F,\mathbf{Y}\sim G}\left(\mathbb{E}(\|\mathbf{X}-\mathbf{Y}\|\_{2}^{2})\right)^{1/2}; |  |

see e.g., Blanchet et al. ([2022](https://arxiv.org/html/2511.08662v1#bib.bib9)).
To simplify our analysis and to be more practical, we suppose the underlying distribution and the reference distribution have the same mean and covariance matrix, i.e., 𝔼​(𝐗0)=𝝁=(μ1,…,μn)\mathbb{E}(\mathbf{X}\_{0})=\boldsymbol{\mu}=(\mu\_{1},\dots,\mu\_{n}) and C​o​v​(𝐗0)=Σ0Cov(\mathbf{X}\_{0})=\Sigma\_{0}. Note that here we suppose that Σ0\Sigma\_{0} is positive-definite.

Then the uncertainty set of the negative return of portfolio ∑i=1nwi​Xi\sum\_{i=1}^{n}w\_{i}X\_{i} can be defined as, for some ε>0\varepsilon>0,

|  |  |  |
| --- | --- | --- |
|  | ℳ𝐰,ε={F∑i=1nwi​Xi:E​(𝐗)=𝝁,C​o​v​(𝐗)=Σ0}∩{F∑i=1nwi​Xi:dW(n)​(F𝐗,F𝐗0)⩽ε}.\mathcal{M}\_{\mathbf{w},\varepsilon}=\left\{F\_{\sum\_{i=1}^{n}w\_{i}X\_{i}}:E(\mathbf{X})=\boldsymbol{\mu},Cov(\mathbf{X})=\Sigma\_{0}\right\}\cap\left\{F\_{\sum\_{i=1}^{n}w\_{i}X\_{i}}:d\_{W}^{(n)}(F\_{\mathbf{X}},F\_{\mathbf{X}\_{0}})\leqslant\sqrt{\varepsilon}\right\}. |  |

The robust portfolio optimization is to solve the following optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg​min𝐰∈𝒜​supG∈ℳ𝐰,ερg​(G).\displaystyle\operatorname\*{arg\,min}\_{\mathbf{w}\in\mathcal{A}}\sup\_{G\in\mathcal{M}\_{\mathbf{w},\varepsilon}}\rho\_{g}(G). |  | (21) |

An example of 𝒜\mathcal{A} is 𝒜={𝐰∈Δn:−𝐰⊤​𝝁⩾a}\mathcal{A}=\{\mathbf{w}\in\Delta\_{n}:-\mathbf{w}^{\top}\boldsymbol{\mu}\geqslant a\} for some a>0a>0, requiring that the return of the portfolio is larger than aa.
For the robust portfolio optimization, the uncertainty set ℳ𝐰,ε\mathcal{M}\_{\mathbf{w},\varepsilon} is quite new and is different from the ones considered in the literature such as Blanchet et al. ([2022](https://arxiv.org/html/2511.08662v1#bib.bib9)), Bernard et al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib8)), Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29)) and Mao et al. ([2025](https://arxiv.org/html/2511.08662v1#bib.bib27)). In ℳ𝐰,ε\mathcal{M}\_{\mathbf{w},\varepsilon}, the probability constraint via Wasserstein metric is on the multivariate distribution of negative return vector 𝐗\mathbf{X}; while in Bernard et al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib8)), it is on the univariate distribution of the negative return of the portfolio ∑i=1nwi​Xi\sum\_{i=1}^{n}w\_{i}X\_{i}.

We can recast ℳ𝐰,ε\mathcal{M}\_{\mathbf{w},\varepsilon} as an uncertainty set with constraint only on the univariate distribution F∑i=1nwi​XiF\_{\sum\_{i=1}^{n}w\_{i}X\_{i}}, which plays an important role for the application of our results in Section [3](https://arxiv.org/html/2511.08662v1#S3 "3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization").

###### Proposition 6.

We have
ℳ𝐰,ε=ℳε​‖𝐰‖22​(𝐰⊤​𝛍,𝐰⊤​Σ0​𝐰)\mathcal{M}\_{\mathbf{w},\varepsilon}=\mathcal{M}\_{\varepsilon\|\mathbf{w}\|\_{2}^{2}}(\mathbf{w}^{\top}\boldsymbol{\mu},\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}) with F=F𝐰⊤​𝐗0F=F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}.

Proposition [6](https://arxiv.org/html/2511.08662v1#Thmproposition6 "Proposition 6. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization") implies that problem ([21](https://arxiv.org/html/2511.08662v1#S5.E21 "In 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) is equivalent to

|  |  |  |
| --- | --- | --- |
|  | arg​min𝐰∈𝒜​supG∈ℳε​‖𝐰‖22​(𝐰⊤​𝝁,𝐰⊤​Σ0​𝐰)ρg​(G),\operatorname\*{arg\,min}\_{\mathbf{w}\in\mathcal{A}}\sup\_{G\in\mathcal{M}\_{\varepsilon\|\mathbf{w}\|\_{2}^{2}}(\mathbf{w}^{\top}\boldsymbol{\mu},\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}})}\rho\_{g}(G), |  |

which allows us to apply the results in Theorems [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") and [2](https://arxiv.org/html/2511.08662v1#Thmtheorem2 "Theorem 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"). We arrive at the following conclusion.

###### Proposition 7.

Problem ([21](https://arxiv.org/html/2511.08662v1#S5.E21 "In 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) can be solved as follows.

1. (i)

   If gg is concave and (g∗)′(g^{\*})^{\prime} is not a constant, then the solution of problem ([21](https://arxiv.org/html/2511.08662v1#S5.E21 "In 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) is given by
   arg min\_w∈A{w^⊤μg(1)+w⊤Σ0wbw(V\_g+λ\_wC\_g,F\_w^⊤X\_0)},
   where Vg=V​a​r​(g′​(1−V))V\_{g}=Var(g^{\prime}(1-V)), Cg,F𝐰⊤​𝐗0=C​o​v​(F𝐰⊤​𝐗0−1​(V),g′​(1−V))C\_{g,F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}}=Cov(F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}^{-1}(V),g^{\prime}(1-V)), and
   b\_w=V\_g+2λ\_wC\_g,F\_w^⊤X\_0+λ\_w^2w^⊤Σ\_0w,   λ\_w=-Cg,Fw⊤X0+(Cg,Fw⊤X02-Vgw⊤Σ0w) Aw2Aw2-(w⊤Σ0w)2w⊤Σ0w
   with A𝐰=(𝐰⊤​Σ0​𝐰−ε​‖𝐰‖222)∨(𝐰⊤​Σ0​𝐰/Vg​Cg,F𝐰⊤​𝐗0)A\_{\mathbf{w}}=\left(\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}-\frac{\varepsilon\|\mathbf{w}\|\_{2}^{2}}{2}\right)\vee\left(\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}/V\_{g}}C\_{g,F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}}\right).
2. (ii)

   For ρ=IQDα+\rho=\mathrm{IQD}\_{\alpha}^{+} or IQDα−\mathrm{IQD}\_{\alpha}^{-} with α∈(0,1/2)\alpha\in(0,1/2), the optimal robust portfolio position is
   arg min\_w∈A{w⊤Σ0wVw,λw(1+λw∫1-α1-tα,λwFw⊤X0-1(s)dsα-tα,λw-λw∫1-^tα, λwαFw⊤X0-1(s)ds-1^tα, λw-1+α)} ,
   where V𝐰,λ=V​a​r​((gλ∗)′​(V))V\_{\mathbf{w},\lambda}=Var\left((g\_{\lambda}^{\*})^{\prime}(V)\right) and λ𝐰\lambda\_{\mathbf{w}} is the solution of dW​(F𝐰⊤​𝐗0,Hλ)=ε​‖𝐰‖2d\_{W}(F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}},H\_{\lambda})=\sqrt{\varepsilon}\|{\mathbf{w}}\|\_{2} if dW​(F𝐰⊤​𝐗0,H0)>ε​‖𝐰‖2d\_{W}(F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}},H\_{0})>\sqrt{\varepsilon}\|{\mathbf{w}}\|\_{2}; or else, λ𝐰=0\lambda\_{\mathbf{w}}=0.
3. (iii)

   For ρ=VaRα\rho=\mathrm{VaR}\_{\alpha} or VaRα+\mathrm{VaR}\_{\alpha}^{+} with α∈(0,1)\alpha\in(0,1), the optimal robust portfolio position is given by
   arg min\_w∈A{w^⊤μ+w⊤Σ0wVw,λw(1+λw∫α1-t1-α,λwFw⊤X0-1(s)ds1-α-t1-α,λw-1-λ\_ww^⊤μ)} ,
   where V𝐰,λ=V​a​r​((gλ∗)′​(V))V\_{\mathbf{w},\lambda}=Var\left((g\_{\lambda}^{\*})^{\prime}(V)\right) and λ𝐰\lambda\_{\mathbf{w}} is the solution of dW​(F𝐰⊤​𝐗0,Hλ)=ε​‖𝐰‖2d\_{W}(F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}},H\_{\lambda})=\sqrt{\varepsilon}\|{\mathbf{w}}\|\_{2} if dW​(F𝐰⊤​𝐗0,H0)>ε​‖𝐰‖2d\_{W}(F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}},H\_{0})>\sqrt{\varepsilon}\|{\mathbf{w}}\|\_{2}; or else, λ𝐰=0\lambda\_{\mathbf{w}}=0.
4. (iv)

   For ρ=GlueVaRβ,αh1,h2\rho=\mathrm{GlueVaR}\_{\beta,\alpha}^{h\_{1},h\_{2}} with 0<α<β<10<\alpha<\beta<1 and 0<h1<h2<10<h\_{1}<h\_{2}<1 satisfying h11−β⩾h2−h1β−α\frac{h\_{1}}{1-\beta}\geqslant\frac{h\_{2}-h\_{1}}{\beta-\alpha}, the solution of problem ([21](https://arxiv.org/html/2511.08662v1#S5.E21 "In 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) is given by

   |  |  |  |
   | --- | --- | --- |
   |  | arg​min𝐰∈𝒜{𝐰⊤𝝁−𝐰⊤​Σ0​𝐰V𝐰,λ𝐰(1+λ𝐰𝐰⊤𝝁−(1−h2)cα,β,λ𝐰h1,h2)\displaystyle\operatorname\*{arg\,min}\_{\mathbf{w}\in\mathcal{A}}\left\{\mathbf{w}^{\top}\boldsymbol{\mu}-\frac{\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}}{\sqrt{V\_{\mathbf{w},\lambda\_{\mathbf{w}}}}}\left(1+\lambda\_{\mathbf{w}}\mathbf{w}^{\top}\boldsymbol{\mu}-(1-h\_{2})c\_{\alpha,\beta,\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}}\right)\right. |  |
   |  |  |  |
   | --- | --- | --- |
   |  | +𝐰⊤​Σ0​𝐰V𝐰,λ𝐰h11−β(cα,β,λ𝐰h1,h2(1−uα,β,λ𝐰h1,h2−β)++h1​((1−β)∧uα,β,λ𝐰h1,h2)1−β\displaystyle+\frac{\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}}{\sqrt{V\_{\mathbf{w},\lambda\_{\mathbf{w}}}}}\frac{h\_{1}}{1-\beta}\left(c\_{\alpha,\beta,\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}}(1-u\_{\alpha,\beta,\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}}-\beta)\_{+}+\frac{h\_{1}((1-\beta)\wedge u\_{\alpha,\beta,\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}})}{1-\beta}\right. |  |
   |  |  |  |
   | --- | --- | --- |
   |  | +λ𝐰∫β∨(1−uα,β,λ𝐰h1,h2)1F𝐰⊤​𝐗0−1(s)ds)\displaystyle\quad\left.+\lambda\_{\mathbf{w}}\int\_{\beta\vee(1-u\_{\alpha,\beta,\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}})}^{1}F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}^{-1}(s)\mathrm{d}s\right) |  |
   |  |  |  |
   | --- | --- | --- |
   |  | +𝐰⊤​Σ0​𝐰V𝐰,λ𝐰h2−h1β−α(cα,β,λ𝐰h1,h2(β∧(1−uα,β,λ𝐰h1,h2)−α)+(h2−h1)​(β−1+uα,β,λ𝐰h1,h2)+β−α\displaystyle+\frac{\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}}{\sqrt{V\_{\mathbf{w},\lambda\_{\mathbf{w}}}}}\frac{h\_{2}-h\_{1}}{\beta-\alpha}\left(c\_{\alpha,\beta,\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}}(\beta\wedge(1-u\_{\alpha,\beta,\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}})-\alpha)+\frac{(h\_{2}-h\_{1})(\beta-1+u\_{\alpha,\beta,\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}})\_{+}}{\beta-\alpha}\right. |  |
   |  |  |  |
   | --- | --- | --- |
   |  | +λ𝐰∫β∧(1−uα,β,λ𝐰h1,h2)βF𝐰⊤​𝐗0−1(s)ds)},\displaystyle~~~~~~~~~~~~~~~~~~~~~~\left.\left.+\lambda\_{\mathbf{w}}\int\_{\beta\wedge(1-u\_{\alpha,\beta,\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}})}^{\beta}F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}^{-1}(s)\mathrm{d}s\right)\right\}, |  |

   where cα,β,λh1,h2c\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}} is given in (iii) of Corollary [2](https://arxiv.org/html/2511.08662v1#Thmcorollary2 "Corollary 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), V𝐰,λ=V​a​r​((gλ∗)′​(V))V\_{\mathbf{w},\lambda}=Var\left((g\_{\lambda}^{\*})^{\prime}(V)\right) and λ𝐰\lambda\_{\mathbf{w}} is the solution of dW​(F𝐰⊤​𝐗0,Hλ)=ε​‖𝐰‖2d\_{W}(F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}},H\_{\lambda})=\sqrt{\varepsilon}\|{\mathbf{w}}\|\_{2} if dW​(F𝐰⊤​𝐗0,H0)>ε​‖𝐰‖2d\_{W}(F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}},H\_{0})>\sqrt{\varepsilon}\|{\mathbf{w}}\|\_{2}; or else, λ𝐰=0\lambda\_{\mathbf{w}}=0.

In the above proposition, the optimal portfolio position 𝐰\mathbf{w} depends on the reference distribution F𝐗0F\_{\mathbf{X}\_{0}}. Next, we assume that the reference distribution is elliptical, i.e., F𝐗0∼En​(𝝁,Σ0,ψ)F\_{\mathbf{X}\_{0}}\sim E\_{n}(\boldsymbol{\mu},\Sigma\_{0},\psi), where 𝝁\boldsymbol{\mu} is the mean, Σ0\Sigma\_{0} is the covariance matrix and ψ\psi is the characteristic generator. Note that elliptical distributions include the family of multivariate normal distributions and multivariate t-distributions as special cases. It follows that F𝐰⊤​𝐗0∼E1​(𝐰⊤​𝝁,𝐰⊤​Σ0​𝐰,ψ)F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}\sim E\_{1}(\mathbf{w}^{\top}\boldsymbol{\mu},\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w},\psi). Let F0=F𝐰⊤​𝐗0−𝐰⊤​𝝁𝐰⊤​Σ0​𝐰F\_{0}=F\_{\frac{\mathbf{w}^{\top}\mathbf{X}\_{0}-\mathbf{w}^{\top}\boldsymbol{\mu}}{\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}}} and then we have F0∼E1​(0,1,ψ)F\_{0}\sim E\_{1}(0,1,\psi). Hence,
Cg,F𝐰⊤​𝐗0=𝐰⊤​Σ0​𝐰​C0C\_{g,F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}}=\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}C\_{0} with C0=C​o​v​(F0−1​(V),g′​(1−V))C\_{0}=Cov(F\_{0}^{-1}(V),g^{\prime}(1-V)).
For this special F𝐗0F\_{\mathbf{X}\_{0}}, we can simplify Proposition [7](https://arxiv.org/html/2511.08662v1#Thmproposition7 "Proposition 7. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization") as the following corollaries.

###### Corollary 3.

Suppose F𝐗0∼En​(𝛍,Σ0,ψ)F\_{\mathbf{X}\_{0}}\sim E\_{n}(\boldsymbol{\mu},\Sigma\_{0},\psi). If gg is concave and (g∗)′(g^{\*})^{\prime} is not a constant, then the solution of problem ([21](https://arxiv.org/html/2511.08662v1#S5.E21 "In 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg​min𝐰∈𝒜⁡{𝐰⊤​𝝁​g​(1)+𝐰⊤​Σ0​𝐰Vg+2​C0​B𝐰+B𝐰2​(Vg+C0​B𝐰)},\operatorname\*{arg\,min}\_{\mathbf{w}\in\mathcal{A}}\left\{\mathbf{w}^{\top}\boldsymbol{\mu}g(1)+\frac{\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}}{\sqrt{V\_{g}+2C\_{0}B\_{\mathbf{w}}+B\_{\mathbf{w}}^{2}}}\left(V\_{g}+C\_{0}B\_{\mathbf{w}}\right)\right\}, |  | (22) |

where

|  |  |  |
| --- | --- | --- |
|  | B𝐰=−C0+(C02−Vg)​A𝐰2A𝐰2−(𝐰⊤​Σ0​𝐰)2B\_{\mathbf{w}}=-C\_{0}+\sqrt{\frac{(C\_{0}^{2}-V\_{g})A\_{\mathbf{w}}^{2}}{A\_{\mathbf{w}}^{2}-\left(\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}\right)^{2}}} |  |

with A𝐰=(𝐰⊤​Σ0​𝐰−ε​‖𝐰‖222)∨(C0​𝐰⊤​Σ0​𝐰/Vg)A\_{\mathbf{w}}=\left(\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}-\frac{\varepsilon\|\mathbf{w}\|\_{2}^{2}}{2}\right)\vee\left(C\_{0}\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}/\sqrt{V\_{g}}\right).

As it is shown in the above corollary, the expected negative returns disappear in the objective function of ([22](https://arxiv.org/html/2511.08662v1#S5.E22 "In Corollary 3. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) if g​(1)=0g(1)=0. However, it can still influence the investors’ decision in term of 𝒜\mathcal{A} in the case that 𝒜\mathcal{A} is defined through 𝝁\boldsymbol{\mu}.

For the portfolio optimization using IQD\mathrm{IQD} and VaR\mathrm{VaR}, we need to define the following notation.
For α∈(0,1)\alpha\in(0,1), λ⩾0\lambda\geqslant 0 and 𝐰∈𝒜\mathbf{w}\in\mathcal{A}, let

|  |  |  |
| --- | --- | --- |
|  | tα,𝐰,λ=inf{t∈[0,α):1/𝐰⊤​Σ0​𝐰+λ​∫1−α1−tF0−1​(s)​dsα−t⩾λ​F0−1​(1−t)},t\_{\alpha,\mathbf{w},\lambda}=\inf\left\{t\in[0,\alpha):\frac{1/\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}+\lambda\int\_{1-\alpha}^{1-t}F\_{0}^{-1}(s)\mathrm{d}s}{\alpha-t}\geqslant\lambda F\_{0}^{-1}(1-t)\right\}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | t^α,𝐰,λ=sup{t∈(1−α,1]:λ​∫1−tαF0−1​(s)​ds−1/𝐰⊤​Σ0​𝐰t−α+1⩽λ​F0−1​(1−t)}.\displaystyle\hat{t}\_{\alpha,\mathbf{w},\lambda}=\sup\left\{t\in(1-\alpha,1]:\frac{\lambda\int\_{1-t}^{\alpha}F\_{0}^{-1}(s)\mathrm{d}s-1/\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}}{t-\alpha+1}\leqslant\lambda F\_{0}^{-1}(1-t)\right\}. |  |

###### Corollary 4.

Suppose F𝐗0∼En​(𝛍,Σ0,ψ)F\_{\mathbf{X}\_{0}}\sim E\_{n}(\boldsymbol{\mu},\Sigma\_{0},\psi).
If ρ=IQDα+\rho=\mathrm{IQD}\_{\alpha}^{+} or IQDα−\mathrm{IQD}\_{\alpha}^{-} with α∈(0,1/2)\alpha\in(0,1/2), then the solution of problem ([21](https://arxiv.org/html/2511.08662v1#S5.E21 "In 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) is given by

|  |  |  |
| --- | --- | --- |
|  | arg​min𝐰∈𝒜{𝐰⊤​Σ0​𝐰V𝐰,λ𝐰(1+λ𝐰​𝐰⊤​Σ0​𝐰​∫1−α1−tα,𝐰,λ𝐰F0−1​(s)​dsα−tα,𝐰,λ𝐰\displaystyle\operatorname\*{arg\,min}\_{\mathbf{w}\in\mathcal{A}}\left\{\sqrt{\frac{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}{V\_{\mathbf{w},\lambda\_{\mathbf{w}}}}}\left(\frac{1+\lambda\_{\mathbf{w}}\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{1-\alpha}^{1-t\_{\alpha,\mathbf{w},\lambda\_{\mathbf{w}}}}F\_{0}^{-1}(s)\mathrm{d}s}{\alpha-t\_{\alpha,\mathbf{w},\lambda\_{\mathbf{w}}}}\right.\right. |  |
|  |  |  |
| --- | --- | --- |
|  | −λ𝐰​𝐰⊤​Σ0​𝐰​∫1−t^α,𝐰,λ𝐰αF0−1​(s)​ds−1t^α,𝐰,λ𝐰−1+α)},\displaystyle\left.\left.~~~~~~~~~~~~~~~~~~~~~~~~~-\frac{\lambda\_{\mathbf{w}}\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{1-\hat{t}\_{\alpha,\mathbf{w},\lambda\_{\mathbf{w}}}}^{\alpha}F\_{0}^{-1}(s)\mathrm{d}s-1}{\hat{t}\_{\alpha,\mathbf{w},\lambda\_{\mathbf{w}}}-1+\alpha}\right)\right\}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | λ𝐰=η𝐰​𝟙{2​𝐰⊤​Σ0​𝐰​(1−∫1−α1F0−1​(t)​dt−∫0αF0−1​(t)​dt2​α)>ε‖𝐰∥22}\lambda\_{\mathbf{w}}=\eta\_{\mathbf{w}}\mathds{1}\_{\left\{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}\left(1-\frac{\int\_{1-\alpha}^{1}F\_{0}^{-1}(t)\mathrm{d}t-\int\_{0}^{\alpha}F\_{0}^{-1}(t)\mathrm{d}t}{\sqrt{2\alpha}}\right)>\varepsilon\|{\mathbf{w}}\|\_{2}^{2}\right\}} |  |

with η𝐰∈(0,∞)\eta\_{\mathbf{w}}\in(0,\infty) being the solution of

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−ε​‖𝐰‖222​𝐰⊤​Σ0​𝐰)​V𝐰,λ\displaystyle\left(1-\frac{\varepsilon\|\mathbf{w}\|\_{2}^{2}}{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\right)\sqrt{V\_{\mathbf{w},\lambda}} | =1+λ​𝐰⊤​Σ0​𝐰​∫1−α1−tα,𝐰,λF0−1​(s)​dsα−tα,𝐰,λ​∫1−α1−tα,𝐰,λF0−1​(t)​dt\displaystyle=\frac{1+\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{1-\alpha}^{1-t\_{\alpha,\mathbf{w},\lambda}}F\_{0}^{-1}(s)\mathrm{d}s}{\alpha-t\_{\alpha,\mathbf{w},\lambda}}\int\_{1-\alpha}^{1-t\_{\alpha,\mathbf{w},\lambda}}F\_{0}^{-1}(t)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ​𝐰⊤​Σ0​𝐰​∫1−t^α,𝐰,λαF0−1​(s)​ds−1t^α,𝐰,λ−1+α​∫1−t^α,𝐰,λαF0−1​(t)​dt\displaystyle+\frac{\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{1-\hat{t}\_{\alpha,\mathbf{w},\lambda}}^{\alpha}F\_{0}^{-1}(s)\mathrm{d}s-1}{\hat{t}\_{\alpha,\mathbf{w},\lambda}-1+\alpha}\int\_{1-\hat{t}\_{\alpha,\mathbf{w},\lambda}}^{\alpha}F\_{0}^{-1}(t)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ​𝐰⊤​Σ0​𝐰​∫(0,1−t^α,𝐰,λ)∪(α,1−α)∪(1−tα,𝐰,λ,1)(F0−1​(t))2​dt.\displaystyle+\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{(0,1-\hat{t}\_{\alpha,\mathbf{w},\lambda})\cup(\alpha,1-\alpha)\cup(1-t\_{\alpha,\mathbf{w},\lambda},1)}(F\_{0}^{-1}(t))^{2}\mathrm{d}t. |  |

Note that in Corollary [4](https://arxiv.org/html/2511.08662v1#Thmcorollary4 "Corollary 4. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization"), V𝐰,λV\_{\mathbf{w},\lambda} can be expressed in a more explicit way for computation as below:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V𝐰,λ\displaystyle V\_{\mathbf{w},\lambda} | =(1+λ​𝐰⊤​Σ0​𝐰​∫1−α1−tα,𝐰,λF0−1​(s)​dsα−tα,𝐰,λ)2​(α−tα,𝐰,λ)\displaystyle=\left(\frac{1+\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{1-\alpha}^{1-t\_{\alpha,\mathbf{w},\lambda}}F\_{0}^{-1}(s)\mathrm{d}s}{\alpha-t\_{\alpha,\mathbf{w},\lambda}}\right)^{2}(\alpha-t\_{\alpha,\mathbf{w},\lambda}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(λ​𝐰⊤​Σ0​𝐰​∫1−t^α,𝐰,λαF0−1​(s)​ds−1t^α,𝐰,λ−1+α)2​(t^α,𝐰,λ−1+α)\displaystyle+\left(\frac{\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{1-\hat{t}\_{\alpha,\mathbf{w},\lambda}}^{\alpha}F\_{0}^{-1}(s)\mathrm{d}s-1}{\hat{t}\_{\alpha,\mathbf{w},\lambda}-1+\alpha}\right)^{2}(\hat{t}\_{\alpha,\mathbf{w},\lambda}-1+\alpha) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ2​𝐰⊤​Σ0​𝐰​∫(0,1−t^α,𝐰,λ)∪(α,1−α)∪(1−tα,𝐰,λ,1)(F0−1​(t))2​dt.\displaystyle+\lambda^{2}\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}\int\_{(0,1-\hat{t}\_{\alpha,\mathbf{w},\lambda})\cup(\alpha,1-\alpha)\cup(1-t\_{\alpha,\mathbf{w},\lambda},1)}(F\_{0}^{-1}(t))^{2}\mathrm{d}t. |  |

###### Corollary 5.

Suppose F𝐗0∼En​(𝛍,Σ0,ψ)F\_{\mathbf{X}\_{0}}\sim E\_{n}(\boldsymbol{\mu},\Sigma\_{0},\psi).
If ρ=VaRα\rho=\mathrm{VaR}\_{\alpha} or VaRα+\mathrm{VaR}\_{\alpha}^{+} with α∈(0,1)\alpha\in(0,1), then the solution of problem ([21](https://arxiv.org/html/2511.08662v1#S5.E21 "In 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) is given by

|  |  |  |
| --- | --- | --- |
|  | arg​min𝐰∈𝒜⁡{𝐰⊤​𝝁+𝐰⊤​Σ0​𝐰V𝐰,λ𝐰​(1+λ𝐰​𝐰⊤​Σ0​𝐰​∫α1−t1−α,𝐰,λ𝐰F0−1​(s)​ds1−α−t1−α,𝐰,λ𝐰−1)},\displaystyle\operatorname\*{arg\,min}\_{\mathbf{w}\in\mathcal{A}}\left\{\mathbf{w}^{\top}\boldsymbol{\mu}+\sqrt{\frac{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}{V\_{\mathbf{w},\lambda\_{\mathbf{w}}}}}\left(\frac{1+\lambda\_{\mathbf{w}}\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{\alpha}^{1-t\_{1-\alpha,\mathbf{w},\lambda\_{\mathbf{w}}}}F\_{0}^{-1}(s)\mathrm{d}s}{1-\alpha-t\_{1-\alpha,\mathbf{w},\lambda\_{\mathbf{w}}}}-1\right)\right\}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | λ𝐰=η𝐰​𝟙{2​𝐰⊤​Σ0​𝐰​(1−∫α1F0−1​(t)​dtα​(1−α))>ε‖𝐰∥22}\lambda\_{\mathbf{w}}=\eta\_{\mathbf{w}}\mathds{1}\_{\left\{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}\left(1-\frac{\int\_{\alpha}^{1}F\_{0}^{-1}(t)\mathrm{d}t}{\sqrt{\alpha(1-\alpha)}}\right)>\varepsilon\|{\mathbf{w}}\|\_{2}^{2}\right\}} |  |

with η𝐰∈(0,∞)\eta\_{\mathbf{w}}\in(0,\infty) being the solution of

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−ε​‖𝐰‖222​𝐰⊤​Σ0​𝐰)​V𝐰,λ\displaystyle\left(1-\frac{\varepsilon\|\mathbf{w}\|\_{2}^{2}}{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\right)\sqrt{V\_{\mathbf{w},\lambda}} | =1+λ​𝐰⊤​Σ0​𝐰​∫α1−t1−α,𝐰,λF0−1​(s)​ds1−α−t1−α,𝐰,λ​∫α1−t1−α,𝐰,λF0−1​(t)​dt\displaystyle=\frac{1+\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{\alpha}^{1-t\_{1-\alpha,\mathbf{w},\lambda}}F\_{0}^{-1}(s)\mathrm{d}s}{1-\alpha-t\_{1-\alpha,\mathbf{w},\lambda}}\int\_{\alpha}^{1-t\_{1-\alpha,\mathbf{w},\lambda}}F\_{0}^{-1}(t)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ​𝐰⊤​Σ0​𝐰​∫(0,α)∪(1−t1−α,𝐰,λ,1)(F0−1​(t))2​dt.\displaystyle+\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{(0,\alpha)\cup(1-t\_{1-\alpha,\mathbf{w},\lambda},1)}(F\_{0}^{-1}(t))^{2}\mathrm{d}t. |  |

Note that in Corollary [5](https://arxiv.org/html/2511.08662v1#Thmcorollary5 "Corollary 5. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization"), V𝐰,λV\_{\mathbf{w},\lambda} can be expressed in a more explicit way for computation as below:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V𝐰,λ\displaystyle V\_{\mathbf{w},\lambda} | =(1+λ​𝐰⊤​Σ0​𝐰​∫α1−t1−α,𝐰,λF0−1​(s)​ds)21−α−t1−α,𝐰,λ\displaystyle=\frac{\left(1+\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{\alpha}^{1-t\_{1-\alpha,\mathbf{w},\lambda}}F\_{0}^{-1}(s)\mathrm{d}s\right)^{2}}{1-\alpha-t\_{1-\alpha,\mathbf{w},\lambda}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ2​𝐰⊤​Σ0​𝐰​∫(0,α)∪(1−t1−α,𝐰,λ,1)(F0−1​(t))2​dt−1.\displaystyle\quad+\lambda^{2}\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}\int\_{(0,\alpha)\cup(1-t\_{1-\alpha,\mathbf{w},\lambda},1)}(F\_{0}^{-1}(t))^{2}\mathrm{d}t-1. |  |

For the portfolio optimization using GlueVaR\mathrm{GlueVaR}, we need the following notation.
For 0<α<β<10<\alpha<\beta<1, 0<h1<h2<10<h\_{1}<h\_{2}<1, λ⩾0\lambda\geqslant 0 and 𝐰∈𝒜\mathbf{w}\in\mathcal{A}, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | uα,β,𝐰,λh1,h2\displaystyle u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}} | =inf{t∈[0,1−α):1−gα,βh1,h2​(t)+λ​𝐰⊤​Σ0​𝐰​∫α1−tF0−1​(s)​ds1−α−t\displaystyle=\inf\left\{t\in[0,1-\alpha):\frac{1-g\_{\alpha,\beta}^{h\_{1},h\_{2}}(t)+\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int^{1-t}\_{\alpha}F\_{0}^{-1}(s)\mathrm{d}s}{1-\alpha-t}\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩾h11−β𝟙(0,1−β)(t)+h2−h1β−α𝟙[1−β,1−α)(t)+λ𝐰⊤​Σ0​𝐰F0−1(1−t)}\displaystyle~~~~~~~~~~~~~\left.\geqslant\frac{h\_{1}}{1-\beta}\mathds{1}\_{(0,1-\beta)}(t)+\frac{h\_{2}-h\_{1}}{\beta-\alpha}\mathds{1}\_{[1-\beta,1-\alpha)}(t)+\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}F\_{0}^{-1}(1-t)\right\} |  |

and

|  |  |  |
| --- | --- | --- |
|  | d𝐰,λ=1−h2+h11−β​(1−uα,β,𝐰,λh1,h2−β)++h2−h1β−α​(β∧(1−uα,β,𝐰,λh1,h2)−α).d\_{\mathbf{w},\lambda}=1-h\_{2}+\frac{h\_{1}}{1-\beta}(1-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}}-\beta)\_{+}+\frac{h\_{2}-h\_{1}}{\beta-\alpha}(\beta\wedge(1-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}})-\alpha). |  |

###### Corollary 6.

Suppose F𝐗0∼En​(𝛍,Σ0,ψ)F\_{\mathbf{X}\_{0}}\sim E\_{n}(\boldsymbol{\mu},\Sigma\_{0},\psi).
If ρ=GlueVaRβ,αh1,h2\rho=\mathrm{GlueVaR}\_{\beta,\alpha}^{h\_{1},h\_{2}} with 0<α<β<10<\alpha<\beta<1 and 0<h1<h2<10<h\_{1}<h\_{2}<1 satisfying h11−β⩾h2−h1β−α\frac{h\_{1}}{1-\beta}\geqslant\frac{h\_{2}-h\_{1}}{\beta-\alpha}, then the solution of problem ([21](https://arxiv.org/html/2511.08662v1#S5.E21 "In 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) is given by

|  |  |  |
| --- | --- | --- |
|  | arg​min𝐰∈𝒜{𝐰⊤𝝁−𝐰⊤​Σ0​𝐰V𝐰,λ𝐰(1−h12​((1−β)∧uα,β,𝐰,λ𝐰h1,h2)(1−β)2−(h2−h1)2​(β−1+uα,β,𝐰,λ𝐰h1,h2)+(β−α)2)\displaystyle\operatorname\*{arg\,min}\_{\mathbf{w}\in\mathcal{A}}\left\{\mathbf{w}^{\top}\boldsymbol{\mu}-\frac{\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}}{\sqrt{V\_{\mathbf{w},\lambda\_{\mathbf{w}}}}}\left(1-\frac{h\_{1}^{2}((1-\beta)\wedge u\_{\alpha,\beta,\mathbf{w},\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}})}{(1-\beta)^{2}}-\frac{(h\_{2}-h\_{1})^{2}(\beta-1+u\_{\alpha,\beta,\mathbf{w},\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}})\_{+}}{(\beta-\alpha)^{2}}\right)\right. |  |
|  |  |  |
| --- | --- | --- |
|  | +𝐰⊤​Σ0​𝐰V𝐰,λ𝐰​1−gα,βh1,h2​(uα,β,𝐰,λh1,h2)1−α−uα,β,𝐰,λh1,h2​d𝐰,λ𝐰+λ𝐰​𝐰⊤​Σ0​𝐰V𝐰,λ𝐰​∫α1−uα,β,𝐰,λ𝐰h1,h2F0−1​(s)​ds1−α−uα,β,𝐰,λ𝐰h1,h2​d𝐰,λ𝐰\displaystyle+\frac{\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}}{\sqrt{V\_{\mathbf{w},\lambda\_{\mathbf{w}}}}}\frac{1-g\_{\alpha,\beta}^{h\_{1},h\_{2}}(u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}})}{1-\alpha-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}}}d\_{\mathbf{w},\lambda\_{\mathbf{w}}}+\frac{\lambda\_{\mathbf{w}}\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}{\sqrt{V\_{\mathbf{w},\lambda\_{\mathbf{w}}}}}\frac{\int^{1-u\_{\alpha,\beta,\mathbf{w},\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}}}\_{\alpha}F\_{0}^{-1}(s)\mathrm{d}s}{1-\alpha-u\_{\alpha,\beta,\mathbf{w},\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}}}d\_{\mathbf{w},\lambda\_{\mathbf{w}}} |  |
|  |  |  |
| --- | --- | --- |
|  | +λ𝐰​𝐰⊤​Σ0​𝐰V𝐰,λ𝐰(h11−β∫β∨(1−uα,β,𝐰,λ𝐰h1,h2)1F0−1(s)ds+h2−h1β−α∫β∧(1−uα,β,𝐰,λ𝐰h1,h2)βF0−1(s)ds)},\displaystyle\left.+\frac{\lambda\_{\mathbf{w}}\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}{\sqrt{V\_{\mathbf{w},\lambda\_{\mathbf{w}}}}}\left(\frac{h\_{1}}{1-\beta}\int\_{\beta\vee(1-u\_{\alpha,\beta,\mathbf{w},\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}})}^{1}F\_{0}^{-1}(s)\mathrm{d}s+\frac{h\_{2}-h\_{1}}{\beta-\alpha}\int\_{\beta\wedge(1-u\_{\alpha,\beta,\mathbf{w},\lambda\_{\mathbf{w}}}^{h\_{1},h\_{2}})}^{\beta}F\_{0}^{-1}(s)\mathrm{d}s\right)\right\}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | λ𝐰=η𝐰​𝟙{2​𝐰⊤​Σ0​𝐰​(1−(11−α​⋁h11−β)​∫β1F0−1​(t)​dt+(11−α​⋀1−h1β−α)​∫αβF0−1​(t)​dt1−β(1−α)2​⋁h121−β+β−α(1−α)2​⋀(1−h1)2β−α−1)>ε‖𝐰∥22}\lambda\_{\mathbf{w}}=\eta\_{\mathbf{w}}\mathds{1}\_{\left\{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}\left(1-\frac{\left(\frac{1}{1-\alpha}\bigvee\frac{h\_{1}}{1-\beta}\right)\int\_{\beta}^{1}F\_{0}^{-1}(t)\mathrm{d}t+\left(\frac{1}{1-\alpha}\bigwedge\frac{1-h\_{1}}{\beta-\alpha}\right)\int\_{\alpha}^{\beta}F\_{0}^{-1}(t)\mathrm{d}t}{\sqrt{\frac{1-\beta}{(1-\alpha)^{2}}\bigvee\frac{h\_{1}^{2}}{1-\beta}+\frac{\beta-\alpha}{(1-\alpha)^{2}}\bigwedge\frac{(1-h\_{1})^{2}}{\beta-\alpha}-1}}\right)>\varepsilon\|{\mathbf{w}}\|\_{2}^{2}\right\}} |  |

with η𝐰∈(0,∞)\eta\_{\mathbf{w}}\in(0,\infty) being the solution of

|  |  |  |
| --- | --- | --- |
|  | (1−ε​‖𝐰‖222​𝐰⊤​Σ0​𝐰)​V𝐰,λ\displaystyle\left(1-\frac{\varepsilon\|\mathbf{w}\|\_{2}^{2}}{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\right)\sqrt{V\_{\mathbf{w},\lambda}} |  |
|  |  |  |
| --- | --- | --- |
|  | =1−gα,βh1,h2​(uα,β,𝐰,λh1,h2)1−α−uα,β,𝐰,λh1,h2​∫α1−uα,β,𝐰,λh1,h2F0−1​(t)​dt+h11−β​∫β∨(1−uα,β,𝐰,λh1,h2)1F0−1​(t)​dt\displaystyle=\frac{1-g\_{\alpha,\beta}^{h\_{1},h\_{2}}(u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}})}{1-\alpha-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}}}\int\_{\alpha}^{1-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}}}F\_{0}^{-1}(t)\mathrm{d}t+\frac{h\_{1}}{1-\beta}\int\_{\beta\vee(1-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}})}^{1}F\_{0}^{-1}(t)\mathrm{d}t |  |
|  |  |  |
| --- | --- | --- |
|  | +h2−h1β−α​∫β∨(1−uα,β,𝐰,λh1,h2)βF0−1​(t)​dt+λ​𝐰⊤​Σ0​𝐰​∫(0,α)∪(1−uα,β,𝐰,λh1,h2,1)(F0−1​(t))2​dt\displaystyle\quad+\frac{h\_{2}-h\_{1}}{\beta-\alpha}\int\_{\beta\vee(1-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}})}^{\beta}F\_{0}^{-1}(t)\mathrm{d}t+\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{(0,\alpha)\cup(1-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}},1)}(F\_{0}^{-1}(t))^{2}\mathrm{d}t |  |
|  |  |  |
| --- | --- | --- |
|  | +λ​𝐰⊤​Σ0​𝐰1−α−uα,β,𝐰,λh1,h2​(∫α1−uα,β,𝐰,λh1,h2F0−1​(s)​ds)2.\displaystyle\quad+\frac{\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}}{1-\alpha-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}}}\left(\int^{1-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}}}\_{\alpha}F\_{0}^{-1}(s)\mathrm{d}s\right)^{2}. |  |

Note that in Corollary [6](https://arxiv.org/html/2511.08662v1#Thmcorollary6 "Corollary 6. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization"), an explicit expression for V𝐰,λV\_{\mathbf{w},\lambda} for computation is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V𝐰,λ\displaystyle V\_{\mathbf{w},\lambda} | =11−α−uα,β,𝐰,λh1,h2​(1−gα,βh1,h2​(uα,β,𝐰,λh1,h2)+λ​𝐰⊤​Σ0​𝐰​∫α1−uα,β,𝐰,λh1,h2F0−1​(t)​dt)2\displaystyle=\frac{1}{1-\alpha-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}}}\left(1-g\_{\alpha,\beta}^{h\_{1},h\_{2}}(u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}})+\lambda\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\int\_{\alpha}^{1-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}}}F\_{0}^{-1}(t)\mathrm{d}t\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +h12​((1−β)∧uα,β,𝐰,λh1,h2)(1−β)2+(h2−h1)2​(β−1+uα,β,𝐰,λh1,h2)+(β−α)2\displaystyle\quad+\frac{h\_{1}^{2}((1-\beta)\wedge u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}})}{(1-\beta)^{2}}+\frac{(h\_{2}-h\_{1})^{2}(\beta-1+u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}})\_{+}}{(\beta-\alpha)^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ2​𝐰⊤​Σ0​𝐰​∫(0,α)∪(1−uα,β,𝐰,λh1,h2,1)(F0−1​(t))2​dt−1.\displaystyle\quad+\lambda^{2}\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}\int\_{(0,\alpha)\cup(1-u\_{\alpha,\beta,\mathbf{w},\lambda}^{h\_{1},h\_{2}},1)}(F\_{0}^{-1}(t))^{2}\mathrm{d}t-1. |  |

### 5.2 Unimodal constraints

In this subsection, we additionally assume that the negative return of portfolio ∑i=1nwi​Xi\sum\_{i=1}^{n}w\_{i}X\_{i} is unimodal with the inflection point ξ∈(0,1)\xi\in(0,1). Then the uncertainty set becomes

|  |  |  |
| --- | --- | --- |
|  | ℳ𝐰,ξ,ε=ℳ𝐰,ε∩ℱU,ξ.\mathcal{M}\_{\mathbf{w},\xi,\varepsilon}=\mathcal{M}\_{\mathbf{w},\varepsilon}\cap\mathcal{F}\_{U,\xi}. |  |

By Proposition [6](https://arxiv.org/html/2511.08662v1#Thmproposition6 "Proposition 6. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization"), we have ℳ𝐰,ξ,ε=ℱU,ξ​(𝐰⊤​𝝁,𝐰⊤​Σ0​𝐰,ε​‖𝐰‖22)\mathcal{M}\_{\mathbf{w},\xi,\varepsilon}=\mathcal{F}\_{U,\xi}(\mathbf{w}^{\top}\boldsymbol{\mu},\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}},\varepsilon\|\mathbf{w}\|\_{2}^{2}).
Then the robust portfolio optimization problem is to solve

|  |  |  |  |
| --- | --- | --- | --- |
|  | arg​min𝐰∈𝒜​supG∈ℱU,ξ​(𝐰⊤​𝝁,𝐰⊤​Σ0​𝐰,ε​‖𝐰‖22)ρg​(G).\displaystyle\operatorname\*{arg\,min}\_{\mathbf{w}\in\mathcal{A}}\sup\_{G\in\mathcal{F}\_{U,\xi}(\mathbf{w}^{\top}\boldsymbol{\mu},\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}},\varepsilon\|\mathbf{w}\|\_{2}^{2})}\rho\_{g}(G). |  | (23) |

Suppose that g∈ℋg\in\mathcal{H} has a density γ​(u)=∂−g​(x)|x=1−u,0<u<1\gamma(u)=\partial\_{-}g(x)|\_{x=1-u},~0<u<1.
We first consider the case that ε=∞\varepsilon=\infty, i.e., the case without probability constraint. Recall that b^ξ=∫01(γξ↑​(u)−g​(1))2​du\hat{b}\_{\xi}=\sqrt{\int\_{0}^{1}\left(\gamma\_{\xi}^{\uparrow}(u)-g(1)\right)^{2}\mathrm{d}u}.

###### Proposition 8.

For ε=∞\varepsilon=\infty, the robust portfolio optimization ([23](https://arxiv.org/html/2511.08662v1#S5.E23 "In 5.2 Unimodal constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) is equivalent to

|  |  |  |
| --- | --- | --- |
|  | arg​min𝐰∈𝒜⁡(𝐰⊤​𝝁​g​(1)+b^ξ​𝐰⊤​Σ0​𝐰).\operatorname\*{arg\,min}\_{\mathbf{w}\in\mathcal{A}}\left(\mathbf{w}^{\top}\boldsymbol{\mu}g(1)+\hat{b}\_{\xi}\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\right). |  |

Note that for GD\mathrm{GD} and MMD\mathrm{MMD}, g​(1)=0g(1)=0. Hence, if 𝒜=Δn\mathcal{A}=\Delta\_{n}, the unimodality does not contribute to the robust portfolio optimization although it reduces the worst-case value of the distortion risk metrics of the portfolio through b^ξ\hat{b}\_{\xi}. For RVaR\mathrm{RVaR}, g​(1)=1g(1)=1, the unimodality may affect the optimal portfolios through b^ξ\hat{b}\_{\xi}.

Let (F𝐰⊤​𝐗0)ξ−1,↑(F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}})\_{\xi}^{-1,\uparrow} be the projection of F𝐰⊤​𝐗0−1F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}^{-1} on ℱU,ξ\mathcal{F}\_{U,\xi}.

###### Proposition 9.

Suppose kλ,ξ↑k\_{\lambda,\xi}^{\uparrow} are not constants for all λ⩾0\lambda\geqslant 0, and (F𝐰⊤​𝐗0)ξ−1,↑(F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}})\_{\xi}^{-1,\uparrow} are not constants for all 𝐰∈Δn\mathbf{w}\in\Delta\_{n}. For 0<ε<∞0<\varepsilon<\infty, the robust portfolio optimization ([23](https://arxiv.org/html/2511.08662v1#S5.E23 "In 5.2 Unimodal constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) is equivalent to

|  |  |  |
| --- | --- | --- |
|  | arg​min𝐰∈Δn,ε⁡(𝐰⊤​𝝁​g​(1)+𝐰⊤​Σ0​𝐰​(∫01γ​(u)​kλ𝐰,ξ↑​(u)​du−g​(1)​(g​(1)+λ𝐰​𝐰⊤​𝝁))∫01(kλ𝐰,ξ↑​(u)−g​(1)−λ𝐰​𝐰⊤​𝝁)2​du),\displaystyle\operatorname\*{arg\,min}\_{\mathbf{w}\in\Delta\_{n,\varepsilon}}\left(\mathbf{w}^{\top}\boldsymbol{\mu}g(1)+\frac{\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\left(\int\_{0}^{1}\gamma(u)k\_{\lambda\_{\mathbf{w}},\xi}^{\uparrow}(u)\mathrm{d}u-g(1)(g(1)+\lambda\_{\mathbf{w}}\mathbf{w}^{\top}\boldsymbol{\mu})\right)}{\sqrt{\int\_{0}^{1}\left(k\_{\lambda\_{\mathbf{w}},\xi}^{\uparrow}(u)-g(1)-\lambda\_{\mathbf{w}}\mathbf{w}^{\top}\boldsymbol{\mu}\right)^{2}\mathrm{d}u}}\right), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Δn,ε=𝒜∩{2​𝐰⊤​Σ0​𝐰−2​𝐰⊤​Σ0​𝐰​∫01((F𝐰⊤​𝐗0)ξ−1,↑​(u)−𝐰⊤​𝝁)2​du​<ε∥​𝐰∥22}\Delta\_{n,\varepsilon}=\mathcal{A}\cap\left\{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}-2\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\sqrt{\int\_{0}^{1}((F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}})\_{\xi}^{-1,\uparrow}(u)-\mathbf{w}^{\top}\boldsymbol{\mu})^{2}\mathrm{d}u}<\varepsilon\|\mathbf{w}\|\_{2}^{2}\right\} |  |

and

|  |  |  |
| --- | --- | --- |
|  | λ𝐰=η𝐰​𝟙{2​𝐰⊤​Σ0​𝐰−2​𝐰⊤​Σ0​𝐰​(∫01F𝐰⊤​𝐗0−1​(u)​γξ↑​(u)​du−g​(1)​𝐰⊤​𝝁)/∫01(γξ↑​(u)−g​(1))2​du>ε‖𝐰∥22}\lambda\_{\mathbf{w}}=\eta\_{\mathbf{w}}\mathds{1}\_{\left\{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}-2\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\left(\int\_{0}^{1}F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}^{-1}(u)\gamma\_{\xi}^{\uparrow}(u)\mathrm{d}u-g(1)\mathbf{w}^{\top}\boldsymbol{\mu}\right)/\sqrt{\int\_{0}^{1}\left(\gamma\_{\xi}^{\uparrow}(u)-g(1)\right)^{2}\mathrm{d}u}>\varepsilon\|\mathbf{w}\|\_{2}^{2}\right\}} |  |

with η𝐰∈(0,∞)\eta\_{\mathbf{w}}\in(0,\infty) being the solution of

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01F𝐰⊤​𝐗0−1​(u)​kλ,ξ↑​(u)​du\displaystyle\int\_{0}^{1}F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}^{-1}(u)k\_{\lambda,\xi}^{\uparrow}(u)\mathrm{d}u | =2​𝐰⊤​Σ0​𝐰−ε​‖𝐰‖222​𝐰⊤​Σ0​𝐰​∫01(kλ,ξ↑​(u)−g​(1)−λ​𝐰⊤​𝝁)2​du\displaystyle=\frac{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}-\varepsilon\|\mathbf{w}\|\_{2}^{2}}{2\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}}\sqrt{\int\_{0}^{1}\left(k\_{\lambda,\xi}^{\uparrow}(u)-g(1)-\lambda\mathbf{w}^{\top}\boldsymbol{\mu}\right)^{2}\mathrm{d}u} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝐰⊤​𝝁​(g​(1)+λ​𝐰⊤​𝝁).\displaystyle~~+\mathbf{w}^{\top}\boldsymbol{\mu}(g(1)+\lambda\mathbf{w}^{\top}\boldsymbol{\mu}). |  |

Next, we assume that the reference distribution is elliptical, i.e., F𝐗0∼En​(𝝁,Σ0,ψ)F\_{\mathbf{X}\_{0}}\sim E\_{n}(\boldsymbol{\mu},\Sigma\_{0},\psi), where 𝝁\boldsymbol{\mu} is the mean, Σ0\Sigma\_{0} is the covariance matrix and ψ\psi is the characteristic generator. It follows that F𝐰⊤​𝐗0∼E1​(𝐰⊤​μ,𝐰⊤​Σ0​𝐰,ψ)F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}}\sim E\_{1}(\mathbf{w}^{\top}\mathbf{\mu},\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w},\psi). Let F0=F𝐰⊤​𝐗0−𝐰⊤​𝝁𝐰⊤​Σ0​𝐰F\_{0}=F\_{\frac{\mathbf{w}^{\top}\mathbf{X}\_{0}-\mathbf{w}^{\top}\boldsymbol{\mu}}{\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}}} and then we have F0∼E1​(0,1,ψ)F\_{0}\sim E\_{1}(0,1,\psi). We denote by (F0)ξ−1,↑(F\_{0})\_{\xi}^{-1,\uparrow} the projection of F0−1F\_{0}^{-1} on ℱU,ξ\mathcal{F}\_{U,\xi}.

###### Corollary 7.

Suppose kλ,ξ↑k\_{\lambda,\xi}^{\uparrow} are not constants for all λ⩾0\lambda\geqslant 0, and (F0)ξ−1,↑(F\_{0})\_{\xi}^{-1,\uparrow} is not a constant. For 0<ε<∞0<\varepsilon<\infty, the robust portfolio optimization ([23](https://arxiv.org/html/2511.08662v1#S5.E23 "In 5.2 Unimodal constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization")) is equivalent to

|  |  |  |
| --- | --- | --- |
|  | arg​min𝐰∈Δn,ε⁡(𝐰⊤​𝝁​g​(1)+𝐰⊤​Σ0​𝐰​(∫01γ​(u)​kλ𝐰,ξ↑​(u)​du−g​(1)​(g​(1)+λ𝐰​𝐰⊤​𝝁))∫01(kλ𝐰,ξ↑​(u)−g​(1)−λ𝐰​𝐰⊤​𝝁)2​du),\operatorname\*{arg\,min}\_{\mathbf{w}\in\Delta\_{n,\varepsilon}}\left(\mathbf{w}^{\top}\boldsymbol{\mu}g(1)+\frac{\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\left(\int\_{0}^{1}\gamma(u)k\_{\lambda\_{\mathbf{w}},\xi}^{\uparrow}(u)\mathrm{d}u-g(1)(g(1)+\lambda\_{\mathbf{w}}\mathbf{w}^{\top}\boldsymbol{\mu})\right)}{\sqrt{\int\_{0}^{1}\left(k\_{\lambda\_{\mathbf{w}},\xi}^{\uparrow}(u)-g(1)-\lambda\_{\mathbf{w}}\mathbf{w}^{\top}\boldsymbol{\mu}\right)^{2}\mathrm{d}u}}\right), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Δn,ε=𝒜∩{2​𝐰⊤​Σ0​𝐰​(1−∫01((F0)ξ−1,↑​(u))2​du)​<ε∥​𝐰∥22}\Delta\_{n,\varepsilon}=\mathcal{A}\cap\left\{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}\left(1-\sqrt{\int\_{0}^{1}((F\_{0})\_{\xi}^{-1,\uparrow}(u))^{2}\mathrm{d}u}\right)<\varepsilon\|\mathbf{w}\|\_{2}^{2}\right\} |  |

and

|  |  |  |
| --- | --- | --- |
|  | λ𝐰=η𝐰​𝟙{2​𝐰⊤​Σ0​𝐰​(1−(∫01F0−1​(u)​γξ↑​(u)​du)/∫01(γξ↑​(u)−g​(1))2​du)>ε‖𝐰∥22}\lambda\_{\mathbf{w}}=\eta\_{\mathbf{w}}\mathds{1}\_{\left\{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}\left(1-\left(\int\_{0}^{1}F\_{0}^{-1}(u)\gamma\_{\xi}^{\uparrow}(u)\mathrm{d}u\right)/\sqrt{\int\_{0}^{1}\left(\gamma\_{\xi}^{\uparrow}(u)-g(1)\right)^{2}\mathrm{d}u}\right)>\varepsilon\|\mathbf{w}\|\_{2}^{2}\right\}} |  |

with η𝐰∈(0,∞)\eta\_{\mathbf{w}}\in(0,\infty) being the solution of

|  |  |  |
| --- | --- | --- |
|  | ∫01F0−1​(u)​kλ,ξ↑​(u)​du=2​𝐰⊤​Σ0​𝐰−ε​‖𝐰‖222​𝐰⊤​Σ0​𝐰​∫01(kλ,ξ↑​(u)−g​(1)−λ​𝐰⊤​𝝁)2​du.\int\_{0}^{1}F\_{0}^{-1}(u)k\_{\lambda,\xi}^{\uparrow}(u)\mathrm{d}u=\frac{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}-\varepsilon\|\mathbf{w}\|\_{2}^{2}}{2\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\sqrt{\int\_{0}^{1}\left(k\_{\lambda,\xi}^{\uparrow}(u)-g(1)-\lambda\mathbf{w}^{\top}\boldsymbol{\mu}\right)^{2}\mathrm{d}u}. |  |

## 6 Numerical examples

Our main results reduce robust portfolio optimization under an ambiguity set characterized by mean, variance and Wasserstain ball to minimizing a deterministic objective.
In this section, we present numerical results to illustrate the impact of model uncertainty on the portfolio optimisation for different risk metrics: GD\mathrm{GD}, MMD\mathrm{MMD}, IQD\mathrm{IQD}, VaR\mathrm{VaR}, ES\mathrm{ES} and GlueVaR\mathrm{GlueVaR}. That is, we solve the optimization problem of Corollary [3](https://arxiv.org/html/2511.08662v1#Thmcorollary3 "Corollary 3. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization") for GD\mathrm{GD}, MMD\mathrm{MMD} and ES\mathrm{ES},
Corollary [4](https://arxiv.org/html/2511.08662v1#Thmcorollary4 "Corollary 4. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization") for IQD\mathrm{IQD}, Corollary [5](https://arxiv.org/html/2511.08662v1#Thmcorollary5 "Corollary 5. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization") for VaR\mathrm{VaR} and Corollary [6](https://arxiv.org/html/2511.08662v1#Thmcorollary6 "Corollary 6. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization") for GlueVaR\mathrm{GlueVaR}.

We assume that 𝒜=Δn\mathcal{A}=\Delta\_{n} and the reference distribution 𝐗0∼N​(𝝁,Σ0)\mathbf{X}\_{0}\sim N(\boldsymbol{\mu},\Sigma\_{0}) representing the negative returns of investing 1 dollar on nn different assets in the market. To simplify our analysis, we consider the case n=2n=2. For the values of the reference mean vector, we set 𝝁=(−2,−1)⊤\boldsymbol{\mu}=(-2,-1)^{\top} representing the expected loss for each asset. Both positive and negative correlated covariance matrix Σ0\Sigma\_{0} are considered as below:

|  |  |  |
| --- | --- | --- |
|  | Σ0(1)=[40.50.51],Σ0(2)=[4−0.5−0.51].\Sigma\_{0}^{(1)}=\begin{bmatrix}4&0.5\\ 0.5&1\end{bmatrix},\quad\Sigma\_{0}^{(2)}=\begin{bmatrix}4&-0.5\\ -0.5&1\end{bmatrix}. |  |

The uncertainty is controlled by the Wasserstein radius ε\varepsilon. Three Wasserstein radius are considered: ε=1×10−10\varepsilon=1\times 10^{-10} (approximating the case when there is no uncertainty), ε=0.01\varepsilon=0.01 (small uncertainty) and ε=1\varepsilon=1 (large uncertainty). All numerical results are obtained using MATLAB.

| Σ0\Sigma\_{0} | ε\varepsilon | Optimal weight w1w\_{1} | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GD\mathrm{GD} | MMD\mathrm{MMD} | IQD0.05\mathrm{IQD}\_{0.05} | VaR0.975\mathrm{VaR}\_{0.975} | ES0.95\mathrm{ES}\_{0.95} | GlueVaR0.975,0.9513,23\mathrm{GlueVaR}\_{0.975,0.95}^{\frac{1}{3},\frac{2}{3}} |
| Σ0(1)\Sigma\_{0}^{(1)} | 1 | 0.125 0000.125\,000 | 0.125 0000.125\,000 | 0.125 0000.125\,000 | 0.303 3270.303\,327 | 0.269 1480.269\,148 | 0.270 3530.270\,353 |
| 0.01 | 0.127 6620.127\,662 | 0.138 2910.138\,291 | 0.131 5290.131\,529 | 0.328 8640.328\,864 | 0.274 0600.274\,060 | 0.232 0100.232\,010 |
| 10−1010^{-10} | 0.125 0120.125\,012 | 0.125 0160.125\,016 | 0.125 0000.125\,000 | 0.247 6840.247\,684 | 0.246 3880.246\,388 | 0.217 7900.217\,790 |
| Σ0(2)\Sigma\_{0}^{(2)} | 1 | 0.250 0000.250\,000 | 0.250 0000.250\,000 | 0.250 0000.250\,000 | 0.297 5530.297\,553 | 0.290 0890.290\,089 | 0.289 9140.289\,914 |
| 0.01 | 0.251 0060.251\,006 | 0.255 3380.255\,338 | 0.267 0940.267\,094 | 0.335 0850.335\,085 | 0.326 6090.326\,609 | 0.307 3780.307\,378 |
| 10−1010^{-10} | 0.250 0000.250\,000 | 0.249 9990.249\,999 | 0.250 0000.250\,000 | 0.316 0770.316\,077 | 0.315 3790.315\,379 | 0.300 1940.300\,194 |

Table 1: Optimal weight of asset 1 (w1w\_{1}) under different distortion risk metrics and Wasserstein radius. The Wasserstein radius ε\varepsilon controls the size of the uncertainty set, with the reference distribution F𝐗0∼N​(𝝁,Σ0)F\_{\mathbf{X}\_{0}}\sim N(\boldsymbol{\mu},\Sigma\_{0}).

Table [1](https://arxiv.org/html/2511.08662v1#S6.T1 "Table 1 ‣ 6 Numerical examples ‣ Robust distortion risk metrics and portfolio optimization") shows that model uncertainty has significant impact on robust portfolio selection for most distortion risk metrics regardless of the positivity and negativity of the correlation of the returns. More precisely, GD\mathrm{GD}, MMD\mathrm{MMD}, and IQD\mathrm{IQD} (called variability measures in Bellini et al. ([2022](https://arxiv.org/html/2511.08662v1#bib.bib4))) are less sensitive to ε\varepsilon and w1w\_{1} fluctuates near the weight of the minimum-variance portfolio (w1=0.125w\_{1}=0.125 for Σ0=Σ0(1)\Sigma\_{0}=\Sigma\_{0}^{(1)} and w1=0.25w\_{1}=0.25 for Σ0=Σ0(2)\Sigma\_{0}=\Sigma\_{0}^{(2)}). This may be due to g​(1)=0g(1)=0 for GD\mathrm{GD}, MMD\mathrm{MMD} and IQD\mathrm{IQD}, leading to no contribution of 𝝁\boldsymbol{\mu} to the portfolio optimization and behaving similarly as variance. For tail-risk measures VaR\mathrm{VaR}, ES\mathrm{ES} and GlueVaR\mathrm{GlueVaR}, more weight is materially allocated to asset 1 and they behave more sensitive to the model uncertainty. This may result from the fact that g​(1)=1g(1)=1 for VaR\mathrm{VaR}, ES\mathrm{ES} and GlueVaR\mathrm{GlueVaR} indicating the contribution of 𝝁\boldsymbol{\mu} to the portfolio optimization using those distortion risk metrics. Moreover, those distortion risk metrics only focus on the tail part of the risk beyond a threshold, which is qualitatively different from GD\mathrm{GD}, MMD\mathrm{MMD} and IQD\mathrm{IQD}.

The impact of model uncertainty for those distortion risk metrics on portfolio optimization can be clearly seen in Figure [1](https://arxiv.org/html/2511.08662v1#S6.F1 "Figure 1 ‣ 6 Numerical examples ‣ Robust distortion risk metrics and portfolio optimization"). The optimal weight w1w\_{1} for GD\mathrm{GD} remains nearly a constant, indicating model uncertainty has a small impact on the portfolio selection. In fact, w1w\_{1} performs the same pattern for all those six distortion risk metrics as ε\varepsilon changes. For small ε\varepsilon (low uncertainty), more weight is allocated to the first asset; for medium ε\varepsilon (medium uncertainty), the weight allocated to the first asset starts to decline and then becomes a constant for large ε\varepsilon (corresponding to the case that Wasserstein constraint loses the impact). The distortion risk metrics are naturally divided to two groups in Figure [1](https://arxiv.org/html/2511.08662v1#S6.F1 "Figure 1 ‣ 6 Numerical examples ‣ Robust distortion risk metrics and portfolio optimization"): the optimal weights for GD\mathrm{GD}, MMD\mathrm{MMD}, and IQD\mathrm{IQD} (variability measures) are always smaller than GD\mathrm{GD}, MMD\mathrm{MMD} and IQD\mathrm{IQD} (tail-risk measures), and the first group is less sensitive than the second group for portfolio optimization.

![Refer to caption](epsilon_analysis.png)


Figure 1: Optimal weight w1∗w\_{1}^{\*} under different Wasserstein radius ε\varepsilon with positive and negative correlations.

## References

* Allais (1953)

  Allais, M. (1953): Le Comportement de l’Homme Rationnel Devant le Risque: Critique des Axiomes et Postulats de l’Ecole Américaine. *Econometrica*, 21(4), 503–546.
* BCBS (2019)

  BCBS (2019).
  Minimum Capital Requirements for Market Risk. February 2019.
  Basel Committee on Banking
  Supervision. Basel: Bank for International Settlements. Document number d457.
* Belles-Sampera et al. (2013)

  Belles-Sampera, J., Guillén, M. and Santolino, M. (2013). Beyond value-at-risk: GlueVaR distortion risk measures. *Risk Analysis*, 34 (1), 121–134.
* Bellini et al. (2022)

  Bellini, F., Fadina, T., Wang, R. and Wei, Y. (2022). Parametric measures of variability induced by risk measures. *Insurance: Mathematics and Economics*, 106, 270–284.
* Ben-Tal et al. (2009)

  Ben-Tal, A., El Ghaoui, L. and Nemirovski, A. (2009). *Robust Optimization*. Princeton University Press, Princeton.
* Bernard et al. (2020)

  Bernard, C., Kazzi, R. and Vanduffel, S (2020). Range value-at-risk bounds for unimodal distributions under partial information. *Insurance: Mathematics and Economics*, 94, 9–24.
* Bernard, Kazzi and Vanduffel (2023)

  Bernard, C., Kazzi, R. and Vanduffel, S. (2023). Model uncertainty assessment for symmetric and right-skewed distributions.
  *Available at SSRN 4468467*
* Bernard et al. (2024)

  Bernard, C, Pesenti, S. M. and Vanduffel, S. (2024). Robust Distortion Risk Measures. *Mathematical Finance*, 34(3), 774–818.
* Blanchet et al. (2022)

  Blanchet, J., Chen, L. and Zhou, X. (2022). Distributionally robust mean-variance portfolio selection with
  Wasserstein distances. *Management Science*, 68(9), 6382–6410.
* Blanchet and Murthy (2019)

  Blanchet, J. and Murthy, K. (2019). Quantifying distributional model risk via optimal transport. *Mathematics
  of Operations Research*, 44(2), 565–600.
* Brennan and Solanki (1981)

  Brennan, M. and Solanki, R. (1981). Optimal portfolio insurance. *J. Financ. Quant. Anal.* 16, 279–300.
* Brunk (1965)

  Brunk, H. (1965). Conditional expectation given a σ\sigma-lattice and applications. *The
  Annals of Mathematical Statistics*, 36(5), 1339–1350.
* Cai et al. (2025)

  Cai, J., Li, J. Y. M. and Mao, T. (2025). Distributionally robust optimization under distorted expectations. *Operations Research*, 73(2), 969–985.
* Chen et al. (2011)

  Chen, L., He, S. and Zhang, S. (2011). Tight bounds for some risk measures, with applications to robust portfolio selection. *Operations Research*, 59 (4), 847-865.
* Cont et al. (2010)

  Cont, R., Deguest, R. and Scandolo, G. (2010). Robustness and sensitivity analysis of risk measurement procedures. *Quantitative finance*, 10 (6), 593-606.
* European Central Bank (2017)

  European Central Bank. (2017). Guidance on model risk management. European Central Bank.
* El Ghaoui et al. (2003)

  Ghaoui, L. E., Oks, M. and Oustry, F. (2003). Worst-case value-at-risk and robust portfolio optimization: A conic programming approach. *Operations Research*, 51(4), 543-556.
* Esfahani and Kuhn (2018)

  Esfahani, PM. and Kuhn, D. (2018). Data-driven distributionally robust optimization using the Wasserstein metric: Performance guarantees and
  tractable reformulations. *Math. Programming* 17 1(1):115–166.
* Föllmer and Schied (2016)

  Föllmer, H. and Schied, A. (2016). *Stochastic Finance. An Introduction in Discrete Time*. Walter de Gruyter, Berlin, Fourth Edition.
* Gilboa and Schmeidler (1987)

  Gilboa, I. and Schmeidler, D. (1989). Maxmin expected utility with non-unique prior. *Journal of Mathematical Economics*, 18(2), 141-153.
* Goldstein et al. (2008)
   Goldstein, D., Johnson, E. and Sharpe, W. (2008). Choosing outcomes versus choosing products: consumer-focused retirement investment advice. *J. Consum. Res.* 35, 440–456 (2008).
* Hansen and Sargent (2001)

  Hansen, L. P. and Sargent, T. J. (2001). Robust control and model uncertainty. *American Economic Review*, 91 (2), 60-66.
* Lauzier et al. (2023)

  Lauzier, J.G., Lin, L. and Wang, R. (2023).
  Risk sharing, measuring variability, and distortion riskmetrics. arXiv:2302.04034.
* Li (2018)

  Li, Y. (2018). Closed-form solutions for worst-case law invariant risk measures with application to robust
  portfolio optimization. *Operations Research*, 66(6), 1533–1541.
* Li et al. (2018)

  Li, L., Shao, H., Wang, R. and Yang, J. (2018). Worst-case Range Value-at-Risk with partial information.
  *SIAM Journal on Financial Mathematics*, 9(1), 190–218.
* Liu et al. (2022)

  Liu, F., Mao, T., Wang, R. and Wei, L. (2022). Inf-convolution, optimal allocations, and model uncertainty for tail risk measures. *Mathematics of Operations Research*, 47(3), 2494–2519.
* Mao et al. (2025)

  Mao, T., Wang, R. and Wu, Q. (2025). Model Aggregation for Risk Evaluation and Robust Optimization. *Management Science*, forthcoming.
* Pesenti and Vanduffel (2024)

  Pesenti, S. M. and Vanduffel, S. (2024). Optimal transport divergences induced by scoring functions.
  Available at
  https://doi.org/10.48550/arXiv.2311.12183.
* Pesenti al. (2024)

  Pesenti, S. M., Wang, Q. and Wang, R. (2024). Optimizing distortion riskmetrics with distributional uncertainty.
  *Mathematical Programming*, forthcoming.
* Popescu (2005)

  Popescu, I. (2005). A Semidefinite Programming Approach to Optimal-Moment Bounds for Convex Classes
  of Distributions. *Mathematics of Operations Research*, 30(3), 632–657.
* Popescu (2007)

  Popescu, I. (2007). Robust mean-covariance solutions for stochastic optimization. *Operations Research*, 55(1), 98–112.
* Quiggin (1982)

  Quiggin, J. (1982). A theory of anticipated utility. *Journal of Economic Behavior & Organization*, 3(4), 323–343.
* Roese and Olson (1995)

  Roese, N. J. and Olson, J. M. (1995). Counterfactual thinking: A critical overview. *Psychological Bulletin*, 118(1), 1-19.
* Scarf (1958)

  Scarf, H. E. (1958). Studies in the mathematical theory of inventory and production. In: Arrow, K.J., Karlin,
  S., Scarf, H.E. (eds.) A Min–Max Solution of an Inventory Problem, pp. 201–209. Stanford University
  Press, Stanford.
* Shalit and Yitzhaki (1984)

  Shalit, H. and Yitzhaki, S. (1984). Mean‐Gini, portfolio theory, and the pricing of risky assets. The Journal of Finance, 39(5), 1449–1468.
* Shao and Zhang (2023)

  Shao, H. and Zhang, Z.G. (2023)
  Distortion risk measure under parametric ambiguity. *European Journal of Operations Research*, 331, 1159–1172.
* Shao and Zhang (2024)

  Shao, H. and Zhang, Z.G. (2024)
  Extreme-Case Distortion Risk Measures: A Unification and Generalization of Closed-Form Solutions. *Mathematics of Operations Research*, forthcoming.
* Starmer (2000)

  Starmer, C. (2000). Developments in non-expected utility theory: The hunt for a descriptive theory of choice under risk. *Journal of Economic Literature*, 38(2), 332-382.
* Tversky and Kahneman (1973)

  Tversky, A. and Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. *Cognitive Psychology*, 5(2), 207-232.
* Tversky and Kahneman (1992)

  Tversky, A. and Kahneman, D. (1992). Advances in prospect theory: Cumulative representation of uncertainty. *Journal of Risk and Uncertainty*, 5, 297-323.
* Wang et al. (2020)

  Wang, Q., Wang, R. and Wei, Y. (2020). Distortion riskmetrics on general spaces. *ASTIN Bulletin: The Journal of the IAA*, 50(3), 827-851.
* Wang et al. (2020)

  Wang, R., Wei, R. and Willmot, G.E. (2020). Characterization, robustness, and aggregation of signed Choquet integrals. *Mathematics of Operations Research*, 45(3), 993-1015.
* Yaari (1987)

  Yaari, M. E. (1987). The dual theory of choice under risk. *Econometrica*, 55(1), 95–115.
* Zymler et al. (2013)

  Zymler, S., Kuhn, D. and Rustem, B. (2013). Distributionally robust joint chance constraints with second-order moment information. *Mathematical Programming*, 137, 167-198.

## Appendix A Proof of Section [3](https://arxiv.org/html/2511.08662v1#S3 "3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization")

In this section, we display all the proofs of the results in Section [3](https://arxiv.org/html/2511.08662v1#S3 "3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization").

Proof of Lemma [1](https://arxiv.org/html/2511.08662v1#Thmlemma1 "Lemma 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"). By definition, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​o​r​r​(F−1​(V),(gλ∗)′​(1−V))\displaystyle Corr(F^{-1}(V),(g\_{\lambda}^{\*})^{\prime}(1-V)) | =𝔼​(F−1​(V)​(gλ∗)′​(1−V))−𝔼​(F−1​(V))​𝔼​((gλ∗)′​(1−V))σF​V​a​r​((gλ∗)′​(V))\displaystyle=\frac{\mathbb{E}(F^{-1}(V)(g\_{\lambda}^{\*})^{\prime}(1-V))-\mathbb{E}(F^{-1}(V))\mathbb{E}((g\_{\lambda}^{\*})^{\prime}(1-V))}{\sigma\_{F}\sqrt{Var((g\_{\lambda}^{\*})^{\prime}(V))}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​(F−1​(V)​(gλ∗)′​(1−V))−μF​(g​(1)+λ​μF)σF​𝔼​((gλ∗)′​(V))2−(g​(1)+λ​μF)2\displaystyle=\frac{\mathbb{E}(F^{-1}(V)(g\_{\lambda}^{\*})^{\prime}(1-V))-\mu\_{F}(g(1)+\lambda\mu\_{F})}{\sigma\_{F}\sqrt{\mathbb{E}((g\_{\lambda}^{\*})^{\prime}(V))^{2}-(g(1)+\lambda\mu\_{F})^{2}}} |  |

We fix λ0∈[0,∞)\lambda\_{0}\in[0,\infty) and show that (gλ∗)′​(t)(g\_{\lambda}^{\*})^{\prime}(t) is continuous with respect to λ\lambda at λ0\lambda\_{0} if (gλ0∗)′​(t)(g\_{\lambda\_{0}}^{\*})^{\prime}(t) is continuous at tt.
For λ1,λ2∈[0,∞)\lambda\_{1},\lambda\_{2}\in[0,\infty), |gλ2​(t)−gλ1​(t)|⩽C​|λ2−λ1||g\_{\lambda\_{2}}(t)-g\_{\lambda\_{1}}(t)|\leqslant C|\lambda\_{2}-\lambda\_{1}| with C=∫01|F−1​(s)|​dsC=\int\_{0}^{1}|F^{-1}(s)|\mathrm{d}s. By definition, |gλ2∗​(t)−gλ1∗​(t)|⩽C​|λ2−λ1||g\_{\lambda\_{2}}^{\*}(t)-g\_{\lambda\_{1}}^{\*}(t)|\leqslant C|\lambda\_{2}-\lambda\_{1}|. This implies supt∈(0,1)|gλ1∗​(t)−gλ2∗​(t)|⩽C​|λ2−λ1|→0\sup\_{t\in(0,1)}|g\_{\lambda\_{1}}^{\*}(t)-g\_{\lambda\_{2}}^{\*}(t)|\leqslant C|\lambda\_{2}-\lambda\_{1}|\to 0 as |λ2−λ1|→0|\lambda\_{2}-\lambda\_{1}|\to 0. Next, we suppose by contradiction that there exists some continuous point of (gλ0∗)′(g\_{\lambda\_{0}}^{\*})^{\prime}, t∈(0,1)t\in(0,1), such that (gλ∗)′​(t)→(gλ0∗)′​(t)(g\_{\lambda}^{\*})^{\prime}(t)\to(g\_{\lambda\_{0}}^{\*})^{\prime}(t) as λ→λ0\lambda\to\lambda\_{0} does not hold. Without loss of generality, we suppose there exist λn→λ0\lambda\_{n}\to\lambda\_{0} as n→∞n\to\infty such that limn→∞(gλn∗)′​(t)=c>(gλ0∗)′​(t)\lim\_{n\to\infty}(g\_{\lambda\_{n}}^{\*})^{\prime}(t)=c>(g\_{\lambda\_{0}}^{\*})^{\prime}(t). Let us denote d=c−(gλ0∗)′​(t)>0d=c-(g\_{\lambda\_{0}}^{\*})^{\prime}(t)>0. By the continuity of (gλ0∗)′(g\_{\lambda\_{0}}^{\*})^{\prime} at tt, there exists ε>0\varepsilon>0 such that (gλ0∗)′​(s)⩽(gλ0∗)′​(t)+d/3(g\_{\lambda\_{0}}^{\*})^{\prime}(s)\leqslant(g\_{\lambda\_{0}}^{\*})^{\prime}(t)+d/3 for s∈(t−ε,t]s\in(t-\varepsilon,t]. Moreover, there exists n0n\_{0} such that (gλn∗)′​(t)>c−d/3(g\_{\lambda\_{n}}^{\*})^{\prime}(t)>c-d/3 for all n⩾n0n\geqslant n\_{0}. Note that (gλn∗)′(g\_{\lambda\_{n}}^{\*})^{\prime} is decreasing. Hence, (gλn∗)′​(s)⩾c−d/3(g\_{\lambda\_{n}}^{\*})^{\prime}(s)\geqslant c-d/3 for s∈(t−ε,t]s\in(t-\varepsilon,t] and n⩾n0n\geqslant n\_{0}. Consequently, we have ∫t−εt(gλn∗)′​(s)​ds⩾∫t−εt(gλ0∗)′​(s)​ds+(d​ε)/3\int\_{t-\varepsilon}^{t}(g\_{\lambda\_{n}}^{\*})^{\prime}(s)\mathrm{d}s\geqslant\int\_{t-\varepsilon}^{t}(g\_{\lambda\_{0}}^{\*})^{\prime}(s)\mathrm{d}s+(d\varepsilon)/3,
which can be rewritten as gλn∗​(t)−gλn∗​(t−ε)⩾gλ0∗​(t)−gλ0∗​(t−ε)+(d​ε)/3g\_{\lambda\_{n}}^{\*}(t)-g\_{\lambda\_{n}}^{\*}(t-\varepsilon)\geqslant g\_{\lambda\_{0}}^{\*}(t)-g\_{\lambda\_{0}}^{\*}(t-\varepsilon)+(d\varepsilon)/3 for all n⩾n0n\geqslant n\_{0}. This contradicts the fact that supt∈(0,1)|gλn∗​(t)−gλ0∗​(t)|⩽C​|λn−λ0|→0\sup\_{t\in(0,1)}|g\_{\lambda\_{n}}^{\*}(t)-g\_{\lambda\_{0}}^{\*}(t)|\leqslant C|\lambda\_{n}-\lambda\_{0}|\to 0 as n→∞n\to\infty. Hence, (gλ∗)′​(t)(g\_{\lambda}^{\*})^{\prime}(t) is continuous with respect to λ\lambda at λ0\lambda\_{0} if (gλ0∗)′​(t)(g\_{\lambda\_{0}}^{\*})^{\prime}(t) is continuous at tt. Note that (gλ0∗)′​(t)(g\_{\lambda\_{0}}^{\*})^{\prime}(t) is continuous over (0,1)(0,1) except countable points. Hence, we have (gλ∗)′​(t)→(gλ0∗)′​(t)(g\_{\lambda}^{\*})^{\prime}(t)\to(g\_{\lambda\_{0}}^{\*})^{\prime}(t) a.e. as λ→λ0\lambda\to\lambda\_{0}.

Define Xλ=(gλ∗)′​(1−V)X\_{\lambda}=(g\_{\lambda}^{\*})^{\prime}(1-V) and Yλ=(g∗)′​(1−V)+λ​F−1​(V)Y\_{\lambda}=(g^{\*})^{\prime}(1-V)+\lambda F^{-1}(V). Direct calculation shows ESα​(Xλ)=gλ∗​(1−α)1−α\mathrm{ES}\_{\alpha}(X\_{\lambda})=\frac{g\_{\lambda}^{\*}(1-\alpha)}{1-\alpha} and ESα​(Yλ)=g∗​(1−α)+λ​∫α1F−1​(t)​dt1−α\mathrm{ES}\_{\alpha}(Y\_{\lambda})=\frac{g^{\*}(1-\alpha)+\lambda\int\_{\alpha}^{1}F^{-1}(t)\mathrm{d}t}{1-\alpha}. Using the fact gλ∗​(t)⩽g∗​(t)+λ​∫1−t1F−1​(s)​dsg\_{\lambda}^{\*}(t)\leqslant g^{\*}(t)+\lambda\int\_{1-t}^{1}F^{-1}(s)\mathrm{d}s, we have ESα​(Xλ)⩽ESα​(Yλ)\mathrm{ES}\_{\alpha}(X\_{\lambda})\leqslant\mathrm{ES}\_{\alpha}(Y\_{\lambda}) for all α∈(0,1)\alpha\in(0,1). Moreover, we have 𝔼​(Xλ)=g​(1)+λ​μF=𝔼​(Yλ)\mathbb{E}(X\_{\lambda})=g(1)+\lambda\mu\_{F}=\mathbb{E}(Y\_{\lambda}). Hence, in light of Corollary 2.61 and Theorem 2.57 of Föllmer and Schied ([2016](https://arxiv.org/html/2511.08662v1#bib.bib19)), we have Xλ⩽cxYλX\_{\lambda}\leqslant\_{\mathrm{cx}}Y\_{\lambda}, which means X⩽YX\leqslant Y in convex order. This implies 𝔼​(Xλ2)⩽𝔼​(Yλ2)\mathbb{E}(X\_{\lambda}^{2})\leqslant\mathbb{E}(Y\_{\lambda}^{2}), i.e., ∫01((gλ∗)′​(t))2​dt⩽∫01((g∗)′​(t)+λ​F−1​(1−t))2​dt⩽2​∫01((g∗)′​(t))2​dt+2​λ2​∫01(F−1​(t))2​dt<∞\int\_{0}^{1}((g\_{\lambda}^{\*})^{\prime}(t))^{2}\mathrm{d}t\leqslant\int\_{0}^{1}((g^{\*})^{\prime}(t)+\lambda F^{-1}(1-t))^{2}\mathrm{d}t\leqslant 2\int\_{0}^{1}((g^{\*})^{\prime}(t))^{2}\mathrm{d}t+2\lambda^{2}\int\_{0}^{1}(F^{-1}(t))^{2}\mathrm{d}t<\infty.

For any ε>0\varepsilon>0, let fλ​(t)=gλ∗​(t)​𝟙{0⩽t⩽ε}+(gλ∗​(ε)+gλ∗​(1)−gλ∗​(ε)1−ε​(t−ε))​𝟙{ε<t⩽1}f\_{\lambda}(t)=g\_{\lambda}^{\*}(t)\mathds{1}\_{\{0\leqslant t\leqslant\varepsilon\}}+\left(g\_{\lambda}^{\*}(\varepsilon)+\frac{g\_{\lambda}^{\*}(1)-g\_{\lambda}^{\*}(\varepsilon)}{1-\varepsilon}(t-\varepsilon)\right)\mathds{1}\_{\{\varepsilon<t\leqslant 1\}} and kλ​(t)=rλ​(t)​𝟙{0⩽t⩽ε}+(rλ​(ε)+rλ​(1)−rλ​(ε)1−ε​(t−ε))​𝟙{ε<t⩽1}k\_{\lambda}(t)=r\_{\lambda}(t)\mathds{1}\_{\{0\leqslant t\leqslant\varepsilon\}}+\left(r\_{\lambda}(\varepsilon)+\frac{r\_{\lambda}(1)-r\_{\lambda}(\varepsilon)}{1-\varepsilon}(t-\varepsilon)\right)\mathds{1}\_{\{\varepsilon<t\leqslant 1\}}, where rλ​(t)=g∗​(t)+λ​∫1−t1F−1​(s)​dsr\_{\lambda}(t)=g^{\*}(t)+\lambda\int\_{1-t}^{1}F^{-1}(s)\mathrm{d}s. Note that both fλf\_{\lambda} and kλk\_{\lambda} are continuous concave functions on [0,1][0,1] and fλ⩽kλf\_{\lambda}\leqslant k\_{\lambda}. Moreover, fλ​(0)=kλ​(0)=0f\_{\lambda}(0)=k\_{\lambda}(0)=0 and fλ​(1)=kλ​(1)f\_{\lambda}(1)=k\_{\lambda}(1). Similarly as the above argument, one can easily check that fλ′​(1−V)⩽kλ′​(1−V)f\_{\lambda}^{\prime}(1-V)\leqslant k\_{\lambda}^{\prime}(1-V) in convex order. Hence, we have
∫01(fλ′​(t))2​dt⩽∫01(kλ′​(t))2​dt\int\_{0}^{1}(f\_{\lambda}^{\prime}(t))^{2}\mathrm{d}t\leqslant\int\_{0}^{1}(k\_{\lambda}^{\prime}(t))^{2}\mathrm{d}t. It can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0ε((gλ∗)′​(t))2​dt\displaystyle\int\_{0}^{\varepsilon}((g\_{\lambda}^{\*})^{\prime}(t))^{2}\mathrm{d}t | ⩽∫0ε((g∗)′​(t)+λ​F−1​(1−t))2​dt+(rλ​(1)−rλ​(ε))21−ε−(gλ∗​(1)−gλ∗​(ε))21−ε\displaystyle\leqslant\int\_{0}^{\varepsilon}((g^{\*})^{\prime}(t)+\lambda F^{-1}(1-t))^{2}\mathrm{d}t+\frac{(r\_{\lambda}(1)-r\_{\lambda}(\varepsilon))^{2}}{1-\varepsilon}-\frac{(g\_{\lambda}^{\*}(1)-g\_{\lambda}^{\*}(\varepsilon))^{2}}{1-\varepsilon} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽2​∫0ε((g∗)′​(t))2​dt+2​λ2​∫0ε(F−1​(1−t))2​dt\displaystyle\leqslant 2\int\_{0}^{\varepsilon}((g^{\*})^{\prime}(t))^{2}\mathrm{d}t+2\lambda^{2}\int\_{0}^{\varepsilon}(F^{-1}(1-t))^{2}\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|rλ(1)−rλ(ε)+gλ∗(1)−gλ∗(ε)∥rλ(ε)−gλ∗(ε)|1−ε.\displaystyle~+\frac{|r\_{\lambda}(1)-r\_{\lambda}(\varepsilon)+g\_{\lambda}^{\*}(1)-g\_{\lambda}^{\*}(\varepsilon)\|r\_{\lambda}(\varepsilon)-g\_{\lambda}^{\*}(\varepsilon)|}{1-\varepsilon}. |  |

Note that gλ∗​(1)=rλ​(1)=gλ​(1)g\_{\lambda}^{\*}(1)=r\_{\lambda}(1)=g\_{\lambda}(1) and gλ​(ε)⩽gλ∗​(ε)⩽rλ​(ε)g\_{\lambda}(\varepsilon)\leqslant g\_{\lambda}^{\*}(\varepsilon)\leqslant r\_{\lambda}(\varepsilon). It follows that

|  |  |  |
| --- | --- | --- |
|  | |rλ(1)−rλ(ε)+gλ∗(1)−gλ∗(ε)∥rλ(ε)−gλ∗(ε)|1−ε⩽2​(|gλ​(1)|+|rλ​(ε)|+|gλ​(ε)|)​|g∗​(ε)−g​(ε)|1−ε.\displaystyle\frac{|r\_{\lambda}(1)-r\_{\lambda}(\varepsilon)+g\_{\lambda}^{\*}(1)-g\_{\lambda}^{\*}(\varepsilon)\|r\_{\lambda}(\varepsilon)-g\_{\lambda}^{\*}(\varepsilon)|}{1-\varepsilon}\leqslant\frac{2(|g\_{\lambda}(1)|+|r\_{\lambda}(\varepsilon)|+|g\_{\lambda}(\varepsilon)|)|g^{\*}(\varepsilon)-g(\varepsilon)|}{1-\varepsilon}. |  |

We fix λ0>0\lambda\_{0}>0.
Consequently, for any η>0\eta>0, there exists ε0>0\varepsilon\_{0}>0 such that if ε<ε0\varepsilon<\varepsilon\_{0}

|  |  |  |
| --- | --- | --- |
|  | sup0⩽λ⩽λ0∫0ε((gλ∗)′​(t))2​dt⩽2​∫0ε((g∗)′​(t))2​dt+2​(λ0+1)2​∫0ε(F−1​(1−t))2​dt+M​|g∗​(ε)−g​(ε)|<η.\displaystyle\sup\_{0\leqslant\lambda\leqslant\lambda\_{0}}\int\_{0}^{\varepsilon}((g\_{\lambda}^{\*})^{\prime}(t))^{2}\mathrm{d}t\leqslant 2\int\_{0}^{\varepsilon}((g^{\*})^{\prime}(t))^{2}\mathrm{d}t+2(\lambda\_{0}+1)^{2}\int\_{0}^{\varepsilon}(F^{-1}(1-t))^{2}\mathrm{d}t+M|g^{\*}(\varepsilon)-g(\varepsilon)|<\eta. |  |

Using the similar argument, we can show that for any η>0\eta>0, there exists ε1>0\varepsilon\_{1}>0 such that if ε<ε1\varepsilon<\varepsilon\_{1}

|  |  |  |
| --- | --- | --- |
|  | sup0⩽λ⩽λ0∫1−ε1((gλ∗)′​(t))2​dt<η.\displaystyle\sup\_{0\leqslant\lambda\leqslant\lambda\_{0}}\int\_{1-\varepsilon}^{1}((g\_{\lambda}^{\*})^{\prime}(t))^{2}\mathrm{d}t<\eta. |  |

Note also that (gλ∗)′(g\_{\lambda}^{\*})^{\prime} is monotone over (0,1)(0,1).
Hence, {((gλ∗)′​(t))2,0⩽λ⩽λ0}\{((g\_{\lambda}^{\*})^{\prime}(t))^{2},0\leqslant\lambda\leqslant\lambda\_{0}\} is uniformly integrable for any λ0>0\lambda\_{0}>0.
Using Hölder’s inequality and the above conclusions, we have

|  |  |  |
| --- | --- | --- |
|  | |𝔼​(F−1​(V)​(gλ∗)′​(1−V))−𝔼​(F−1​(V)​(gλ0∗)′​(1−V))|\displaystyle|\mathbb{E}(F^{-1}(V)(g\_{\lambda}^{\*})^{\prime}(1-V))-\mathbb{E}(F^{-1}(V)(g\_{\lambda\_{0}}^{\*})^{\prime}(1-V))| |  |
|  |  |  |
| --- | --- | --- |
|  | =|∫01F−1​(t)​((gλ∗)′​(1−t)−(gλ0∗)′​(1−t))​dt|\displaystyle=\left|\int\_{0}^{1}F^{-1}(t)((g\_{\lambda}^{\*})^{\prime}(1-t)-(g\_{\lambda\_{0}}^{\*})^{\prime}(1-t))\mathrm{d}t\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ⩽(∫01(F−1​(t))2​dt)1/2​(∫01((gλ∗)′​(t)−(gλ0∗)′​(t))2​dt)1/2→0\displaystyle\leqslant\left(\int\_{0}^{1}(F^{-1}(t))^{2}\mathrm{d}t\right)^{1/2}\left(\int\_{0}^{1}((g\_{\lambda}^{\*})^{\prime}(t)-(g\_{\lambda\_{0}}^{\*})^{\prime}(t))^{2}\mathrm{d}t\right)^{1/2}\to 0 |  |

as λ→λ0\lambda\to\lambda\_{0}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼​((gλ∗)′​(V))2−𝔼​((gλ0∗)′​(V))2|\displaystyle|\mathbb{E}((g\_{\lambda}^{\*})^{\prime}(V))^{2}-\mathbb{E}((g\_{\lambda\_{0}}^{\*})^{\prime}(V))^{2}| | =|∫01((gλ∗)′​(t))2−((gλ0∗)′​(t))2​d​t|\displaystyle=\left|\int\_{0}^{1}((g\_{\lambda}^{\*})^{\prime}(t))^{2}-((g\_{\lambda\_{0}}^{\*})^{\prime}(t))^{2}\mathrm{d}t\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽(∫01((gλ∗)′​(t)+(gλ0∗)′​(t))2​dt)1/2​(∫01((gλ∗)′​(t)−(gλ0∗)′​(t))2​dt)1/2\displaystyle\leqslant\left(\int\_{0}^{1}((g\_{\lambda}^{\*})^{\prime}(t)+(g\_{\lambda\_{0}}^{\*})^{\prime}(t))^{2}\mathrm{d}t\right)^{1/2}\left(\int\_{0}^{1}((g\_{\lambda}^{\*})^{\prime}(t)-(g\_{\lambda\_{0}}^{\*})^{\prime}(t))^{2}\mathrm{d}t\right)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | →0​as​λ→λ0.\displaystyle\to 0~\text{as}~\lambda\to\lambda\_{0}. |  |

Hence, C​o​r​r​(F−1​(V),(gλ∗)′​(1−V))Corr(F^{-1}(V),(g\_{\lambda}^{\*})^{\prime}(1-V)) is continuous for λ∈[0,∞)\lambda\in[0,\infty).

Finally, we show that limλ→∞C​o​r​r​(F−1​(V),(gλ∗)′​(1−V))=1.\lim\_{\lambda\to\infty}Corr(F^{-1}(V),(g\_{\lambda}^{\*})^{\prime}(1-V))=1. Let lλ=gλλl\_{\lambda}=\frac{g\_{\lambda}}{\lambda} for λ>0\lambda>0. Then by definition, we have lλ∗=gλ∗λl\_{\lambda}^{\*}=\frac{g\_{\lambda}^{\*}}{\lambda}. Direct computation gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​o​r​r​(F−1​(V),(gλ∗)′​(1−V))\displaystyle Corr(F^{-1}(V),(g\_{\lambda}^{\*})^{\prime}(1-V)) | =C​o​r​r​(F−1​(V),(lλ∗)′​(1−V))\displaystyle=Corr(F^{-1}(V),(l\_{\lambda}^{\*})^{\prime}(1-V)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​(F−1​(V)​(lλ∗)′​(1−V))−μF​(g​(1)/λ+μF)σF​𝔼​((lλ∗)′​(U))2−(g​(1)/λ+μF)2.\displaystyle=\frac{\mathbb{E}(F^{-1}(V)(l\_{\lambda}^{\*})^{\prime}(1-V))-\mu\_{F}(g(1)/\lambda+\mu\_{F})}{\sigma\_{F}\sqrt{\mathbb{E}((l\_{\lambda}^{\*})^{\prime}(U))^{2}-(g(1)/\lambda+\mu\_{F})^{2}}}. |  |

We denote ∫1−t1F−1​(s)​ds\int\_{1-t}^{1}F^{-1}(s)\mathrm{d}s by l∞​(t)l\_{\infty}(t). Then supt∈[0,1]|lλ​(t)−l∞​(t)|⩽supt∈[0,1]|g​(t)|/λ\sup\_{t\in[0,1]}|l\_{\lambda}(t)-l\_{\infty}(t)|\leqslant\sup\_{t\in[0,1]}|g(t)|/\lambda, which implies
supt∈[0,1]|lλ∗​(t)−l∞∗​(t)|⩽supt∈[0,1]|g​(t)|/λ\sup\_{t\in[0,1]}|l\_{\lambda}^{\*}(t)-l\_{\infty}^{\*}(t)|\leqslant\sup\_{t\in[0,1]}|g(t)|/\lambda. Using the similar argument as (gλ∗)′(g\_{\lambda}^{\*})^{\prime}, we have (lλ∗)′​(t)→(l∞∗)′​(t)(l\_{\lambda}^{\*})^{\prime}(t)\to(l\_{\infty}^{\*})^{\prime}(t) a.e. on (0,1)(0,1) as λ→∞\lambda\to\infty and {(lλ∗)′​(t),1⩽λ<∞}\{(l\_{\lambda}^{\*})^{\prime}(t),~1\leqslant\lambda<\infty\} is uniformly integrable. Therefore, we have limλ→∞𝔼​(F−1​(V)​(lλ∗)′​(1−V))=𝔼​(F−1​(V)​(l∞∗)′​(1−V))=𝔼​((F−1​(V))2)\lim\_{\lambda\to\infty}\mathbb{E}(F^{-1}(V)(l\_{\lambda}^{\*})^{\prime}(1-V))=\mathbb{E}(F^{-1}(V)(l\_{\infty}^{\*})^{\prime}(1-V))=\mathbb{E}((F^{-1}(V))^{2}) and limλ→∞𝔼​((lλ∗)′​(V))2=𝔼​((l∞∗)′​(V))2=𝔼​((F−1​(V))2)\lim\_{\lambda\to\infty}\mathbb{E}((l\_{\lambda}^{\*})^{\prime}(V))^{2}=\mathbb{E}((l\_{\infty}^{\*})^{\prime}(V))^{2}=\mathbb{E}((F^{-1}(V))^{2}). Hence, limλ→∞C​o​r​r​(F−1​(V),(gλ∗)′​(1−V))=1\lim\_{\lambda\to\infty}Corr(F^{-1}(V),(g\_{\lambda}^{\*})^{\prime}(1-V))=1. ∎

Combing Theorem 5 and Remark 2 of Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29)), we immediately arrive at the following result for ε=∞\varepsilon=\infty, which will play an important role to prove Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization").

###### Lemma 6.

For g∈ℋg\in\mathcal{H}, we have

|  |  |  |
| --- | --- | --- |
|  | supG∈ℳ∞​(μ,σ)ρg​(G)=ρg^​(H0),\sup\_{G\in\mathcal{M}\_{\infty}(\mu,\sigma)}\rho\_{g}(G)=\rho\_{\hat{g}}(H\_{0}), |  |

where the supremum is uniquely attained at H0H\_{0} if g=g^g=\hat{g}.

Proof of Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"). First, note that for any G∈ℳε​(μ,σ)G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma), we have (μF−μ)2+(σF−σ)2⩽dW2​(F,G)⩽ε(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}\leqslant d\_{W}^{2}(F,G)\leqslant\varepsilon. Note that dW2​(F,G)=(μF−μ)2+(σF−σ)2d\_{W}^{2}(F,G)=(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2} implies G−1​(t)=μ+σ​F−1​(t)−μFσFG^{-1}(t)=\mu+\sigma\frac{F^{-1}(t)-\mu\_{F}}{\sigma\_{F}}, whose distribution is denoted by H∞H\_{\infty}. For the case (μF−μ)2+(σF−σ)2<dW2​(F,G)⩽ε(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}<d\_{W}^{2}(F,G)\leqslant\varepsilon, by Lemma [1](https://arxiv.org/html/2511.08662v1#Thmlemma1 "Lemma 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), there exists λ⩾0\lambda\geqslant 0 such that
dW​(F,Hλ)=dW​(F,G)d\_{W}(F,H\_{\lambda})=d\_{W}(F,G). This implies ∫01F−1​(t)​hλ​(t)​dt=∫01F−1​(t)​G−1​(t)​dt\int\_{0}^{1}F^{-1}(t)h\_{\lambda}(t)\mathrm{d}t=\int\_{0}^{1}F^{-1}(t)G^{-1}(t)\mathrm{d}t, which is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρgλ−g​(Hλ)=ρgλ−g​(G).\displaystyle\rho\_{g\_{\lambda}-g}(H\_{\lambda})=\rho\_{g\_{\lambda}-g}(G). |  | (24) |

In light of Lemma [6](https://arxiv.org/html/2511.08662v1#Thmlemma6 "Lemma 6. ‣ Appendix A Proof of Section 3 ‣ Robust distortion risk metrics and portfolio optimization"), we have supG∈ℳ∞​(μ,σ)ρgλ​(G)=ρgλ​(Hλ)\sup\_{G\in\mathcal{M}\_{\infty}(\mu,\sigma)}\rho\_{g\_{\lambda}}(G)=\rho\_{g\_{\lambda}}(H\_{\lambda}) and HλH\_{\lambda} is the unique maximizer. Hence, for G∈ℳ∞​(μ,σ)G\in\mathcal{M}\_{\infty}(\mu,\sigma), if G≠HλG\neq H\_{\lambda}, then ρgλ​(G)<ρgλ​(Hλ)\rho\_{g\_{\lambda}}(G)<\rho\_{g\_{\lambda}}(H\_{\lambda}), which can be rewritten as ρg​(G)+ρgλ−g​(G)<ρg​(Hλ)+ρgλ−g​(Hλ)\rho\_{g}(G)+\rho\_{g\_{\lambda}-g}(G)<\rho\_{g}(H\_{\lambda})+\rho\_{g\_{\lambda}-g}(H\_{\lambda}). It follows from ([24](https://arxiv.org/html/2511.08662v1#A1.E24 "In Appendix A Proof of Section 3 ‣ Robust distortion risk metrics and portfolio optimization")) that ρg​(G)<ρg​(Hλ)\rho\_{g}(G)<\rho\_{g}(H\_{\lambda}) if dW​(F,Hλ)=dW​(F,G)d\_{W}(F,H\_{\lambda})=d\_{W}(F,G) and G≠HλG\neq H\_{\lambda}. This means that the optimal solution has the form of HλH\_{\lambda} for λ∈(0,∞]\lambda\in(0,\infty].

For dW​(F,Hλ1)<dW​(F,Hλ2)d\_{W}(F,H\_{\lambda\_{1}})<d\_{W}(F,H\_{\lambda\_{2}}), we have ρgλ2−g​(Hλ2)<ρgλ2−g​(Hλ1)\rho\_{g\_{\lambda\_{2}}-g}(H\_{\lambda\_{2}})<\rho\_{g\_{\lambda\_{2}}-g}(H\_{\lambda\_{1}}). Moreover, by Lemma [6](https://arxiv.org/html/2511.08662v1#Thmlemma6 "Lemma 6. ‣ Appendix A Proof of Section 3 ‣ Robust distortion risk metrics and portfolio optimization"), we have supG∈ℳ​(μ,σ)ρgλ2​(G)=ρgλ2​(Hλ2)\sup\_{G\in\mathcal{M}(\mu,\sigma)}\rho\_{g\_{\lambda\_{2}}}(G)=\rho\_{g\_{\lambda\_{2}}}(H\_{\lambda\_{2}}). This implies ρg​(Hλ1)+ρgλ2−g​(Hλ1)=ρgλ2​(Hλ1)⩽ρgλ2​(Hλ2)=ρg​(Hλ2)+ρgλ2−g​(Hλ2)\rho\_{g}(H\_{\lambda\_{1}})+\rho\_{g\_{\lambda\_{2}}-g}(H\_{\lambda\_{1}})=\rho\_{g\_{\lambda\_{2}}}(H\_{\lambda\_{1}})\leqslant\rho\_{g\_{\lambda\_{2}}}(H\_{\lambda\_{2}})=\rho\_{g}(H\_{\lambda\_{2}})+\rho\_{g\_{\lambda\_{2}}-g}(H\_{\lambda\_{2}}). Hence, ρg​(Hλ1)<ρg​(Hλ2)\rho\_{g}(H\_{\lambda\_{1}})<\rho\_{g}(H\_{\lambda\_{2}}). Consequently, HλεH\_{\lambda\_{\varepsilon}} is the unique maximizer with λε\lambda\_{\varepsilon} satisfying dW​(F,Hλ)=εd\_{W}(F,H\_{\lambda})=\sqrt{\varepsilon}. We proved the statement of (i).

We next consider scenario (ii). If ε⩾(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)\varepsilon\geqslant(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}), and (g∗)′(g^{\*})^{\prime} is not a constant, then by Lemma [6](https://arxiv.org/html/2511.08662v1#Thmlemma6 "Lemma 6. ‣ Appendix A Proof of Section 3 ‣ Robust distortion risk metrics and portfolio optimization"), we have supG∈ℳε​(μ,σ)ρg​(G)⩽supG∈ℳ∞​(μ,σ)ρg​(G)=ρg​(H0).\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G)\leqslant\sup\_{G\in\mathcal{M}\_{\infty}(\mu,\sigma)}\rho\_{g}(G)=\rho\_{g}(H\_{0}). As H0∈ℳε​(μ,σ)H\_{0}\in\mathcal{M}\_{\varepsilon}(\mu,\sigma), we have ρg​(H0)⩽supG∈ℳε​(μ,σ)ρg​(G)\rho\_{g}(H\_{0})\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G). Hence, supG∈ℳε​(μ,σ)ρg​(G)=ρg​(H0)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G)=\rho\_{g}(H\_{0}) and H0H\_{0} is the unique maximizer.

If (g∗)′(g^{\*})^{\prime} is a constant, then c0=0c\_{0}=0 and ε⩾(μF−μ)2+(σF−σ)2+2​σF​σ\varepsilon\geqslant(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma. This implies ℳε​(μ,σ)=ℳ∞​(μ,σ)\mathcal{M}\_{\varepsilon}(\mu,\sigma)=\mathcal{M}\_{\infty}(\mu,\sigma). Note that supG∈ℳ∞​(μ,σ)ρg​(G)⩽supG∈ℳ∞​(μ,σ)ρg∗​(G)=g​(1)​μ\sup\_{G\in\mathcal{M}\_{\infty}(\mu,\sigma)}\rho\_{g}(G)\leqslant\sup\_{G\in\mathcal{M}\_{\infty}(\mu,\sigma)}\rho\_{g^{\*}}(G)=g(1)\mu. Let Gn=(1−1/n)​δμ+(1/(2​n))​δμ−n​σ+(1/(2​n))​δμ+n​σG\_{n}=(1-1/n)\delta\_{\mu}+(1/(2n))\delta\_{\mu-\sqrt{n}\sigma}+(1/(2n))\delta\_{\mu+\sqrt{n}\sigma} for n⩾1n\geqslant 1. Then Gn∈ℳ∞​(μ,σ)G\_{n}\in\mathcal{M}\_{\infty}(\mu,\sigma) and GnG\_{n} converges to δμ\delta\_{\mu} in distribution. Direct computation shows
ρg​(Gn)=g​(1)​μ+[g​(1−1/(2​n))−g​(1)+g​(1/(2​n))]​n​σ→g​(1)​μ\rho\_{g}(G\_{n})=g(1)\mu+[g(1-1/(2n))-g(1)+g(1/(2n))]\sqrt{n}\sigma\to g(1)\mu as n→∞n\to\infty. Consequently, supG∈ℳ∞​(μ,σ)ρg​(G)=g​(1)​μ\sup\_{G\in\mathcal{M}\_{\infty}(\mu,\sigma)}\rho\_{g}(G)=g(1)\mu. ∎

Proof of Corollary [1](https://arxiv.org/html/2511.08662v1#Thmcorollary1 "Corollary 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"). (i) Note that for VaRα+\mathrm{VaR}\_{\alpha}^{+}, we have g​(t)=𝟙[1−α,1]​(t)g(t)=\mathds{1}\_{[1-\alpha,1]}(t) and gλ​(t)=𝟙[1−α,1]​(t)+λ​∫1−t1F−1​(s)​dsg\_{\lambda}(t)=\mathds{1}\_{[1-\alpha,1]}(t)+\lambda\int\_{1-t}^{1}F^{-1}(s)\mathrm{d}s.
Using t1−α,λt\_{1-\alpha,\lambda}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | gλ∗​(t)\displaystyle g\_{\lambda}^{\*}(t) | =λ​∫1−t1F−1​(s)​ds​𝟙[0,t1−α,λ)​(t)+(gλ​(1−α)−gλ​(t1−α,λ)1−α−t1−α,λ​(t−t1−α,λ)+gλ​(t1−α,λ))​𝟙[t1−α,λ,1−α]​(t)\displaystyle=\lambda\int\_{1-t}^{1}F^{-1}(s)\mathrm{d}s\mathds{1}\_{[0,t\_{1-\alpha,\lambda})}(t)+\left(\frac{g\_{\lambda}(1-\alpha)-g\_{\lambda}(t\_{1-\alpha,\lambda})}{1-\alpha-t\_{1-\alpha,\lambda}}(t-t\_{1-\alpha,\lambda})+g\_{\lambda}(t\_{1-\alpha,\lambda})\right)\mathds{1}\_{[t\_{1-\alpha,\lambda},1-\alpha]}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1+λ​∫1−t1F−1​(s)​ds)​𝟙(1−α,1]​(t),\displaystyle+\left(1+\lambda\int\_{1-t}^{1}F^{-1}(s)\mathrm{d}s\right)\mathds{1}\_{(1-\alpha,1]}(t), |  |

Direct computation shows

|  |  |  |
| --- | --- | --- |
|  | (gλ∗)′​(1−t)=λ​F−1​(t)​𝟙(0,α]∪(1−t1−α,λ,1)​(t)+1+λ​∫α1−t1−α,λF−1​(s)​ds1−α−t1−α,λ​𝟙(α,1−t1−α,λ],t∈(0,1),(g\_{\lambda}^{\*})^{\prime}(1-t)=\lambda F^{-1}(t)\mathds{1}\_{(0,\alpha]\cup(1-t\_{1-\alpha,\lambda},1)}(t)+\frac{1+\lambda\int\_{\alpha}^{1-t\_{1-\alpha,\lambda}}F^{-1}(s)\mathrm{d}s}{1-\alpha-t\_{1-\alpha,\lambda}}\mathds{1}\_{(\alpha,1-t\_{1-\alpha,\lambda}]},~t\in(0,1), |  |

which implies

|  |  |  |
| --- | --- | --- |
|  | VaRα+​(Hλ)=μ+σ​1+λ​∫α1−t1−α,λF−1​(s)​ds1−α−t1−α,λ−aλbλ.\mathrm{VaR}\_{\alpha}^{+}(H\_{\lambda})=\mu+\sigma\frac{\frac{1+\lambda\int\_{\alpha}^{1-t\_{1-\alpha,\lambda}}F^{-1}(s)\mathrm{d}s}{1-\alpha-t\_{1-\alpha,\lambda}}-a\_{\lambda}}{b\_{\lambda}}. |  |

(ii) For IQDα+\mathrm{IQD}\_{\alpha}^{+}, we have g​(t)=𝟙[α,1−α]​(t)g(t)=\mathds{1}\_{[\alpha,1-\alpha]}(t) and
gλ​(t)=𝟙[α,1−α]​(t)+λ​∫1−t1F−1​(s)​dsg\_{\lambda}(t)=\mathds{1}\_{[\alpha,1-\alpha]}(t)+\lambda\int\_{1-t}^{1}F^{-1}(s)\mathrm{d}s.
It follows from the definition that

|  |  |  |  |
| --- | --- | --- | --- |
|  | gλ∗​(t)\displaystyle g\_{\lambda}^{\*}(t) | =(gλ​(α)−gλ​(tα,λ)α−tα,λ​(t−tα,λ)+gλ​(tα,λ))​𝟙[tα,λ,α]​(t)+gλ​(t)​𝟙[0,tα,λ)∪(α,1−α]∪(t^α,λ,1]​(t)\displaystyle=\left(\frac{g\_{\lambda}(\alpha)-g\_{\lambda}(t\_{\alpha,\lambda})}{\alpha-t\_{\alpha,\lambda}}(t-t\_{\alpha,\lambda})+g\_{\lambda}(t\_{\alpha,\lambda})\right)\mathds{1}\_{[t\_{\alpha,\lambda},\alpha]}(t)+g\_{\lambda}(t)\mathds{1}\_{[0,t\_{\alpha,\lambda})\cup(\alpha,1-\alpha]\cup(\hat{t}\_{\alpha,\lambda},1]}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(gλ​(t^α,λ)−gλ​(1−α)t^α,λ−1+α​(t−t^α,λ)+gλ​(t^α,λ))​𝟙(1−α,t^α,λ]​(t).\displaystyle+\left(\frac{g\_{\lambda}(\hat{t}\_{\alpha,\lambda})-g\_{\lambda}(1-\alpha)}{\hat{t}\_{\alpha,\lambda}-1+\alpha}(t-\hat{t}\_{\alpha,\lambda})+g\_{\lambda}(\hat{t}\_{\alpha,\lambda})\right)\mathds{1}\_{(1-\alpha,\hat{t}\_{\alpha,\lambda}]}(t). |  |

Direct computation gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | (gλ∗)′​(1−t)\displaystyle(g\_{\lambda}^{\*})^{\prime}(1-t) | =gλ​(α)−gλ​(tα,λ)α−tα,λ​𝟙(1−α,1−tα,λ)​(t)+gλ​(t^α,λ)−gλ​(1−α)t^α,λ−1+α​𝟙(1−t^α,λ,α)​(t)\displaystyle=\frac{g\_{\lambda}(\alpha)-g\_{\lambda}(t\_{\alpha,\lambda})}{\alpha-t\_{\alpha,\lambda}}\mathds{1}\_{(1-\alpha,1-t\_{\alpha,\lambda})}(t)+\frac{g\_{\lambda}(\hat{t}\_{\alpha,\lambda})-g\_{\lambda}(1-\alpha)}{\hat{t}\_{\alpha,\lambda}-1+\alpha}\mathds{1}\_{(1-\hat{t}\_{\alpha,\lambda},\alpha)}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ​F−1​(t)​𝟙(0,1−t^α,λ)∪(α,1−α)∪(1−tα,λ,1).\displaystyle+\lambda F^{-1}(t)\mathds{1}\_{(0,1-\hat{t}\_{\alpha,\lambda})\cup(\alpha,1-\alpha)\cup(1-t\_{\alpha,\lambda},1)}. |  |

Applying Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we have

|  |  |  |
| --- | --- | --- |
|  | IQD+​(Hλ)=gλ​(α)−gλ​(tα,λ)α−tα,λ−gλ​(t^α,λ)−gλ​(1−α)t^α,λ−1+αbλ​σ.\mathrm{IQD}^{+}(H\_{\lambda})=\frac{\frac{g\_{\lambda}(\alpha)-g\_{\lambda}(t\_{\alpha,\lambda})}{\alpha-t\_{\alpha,\lambda}}-\frac{g\_{\lambda}(\hat{t}\_{\alpha,\lambda})-g\_{\lambda}(1-\alpha)}{\hat{t}\_{\alpha,\lambda}-1+\alpha}}{b\_{\lambda}}\sigma. |  |

(iii) For g​(t)=t1−α1∧1−𝟙(1−α2,1]​(t)g(t)=\frac{t}{1-\alpha\_{1}}\wedge 1-\mathds{1}\_{(1-\alpha\_{2},1]}(t), we have gλ​(t)=t1−α1∧1+λ​∫1−t1F−1​(s)​ds−𝟙(1−α2,1]​(t)g\_{\lambda}(t)=\frac{t}{1-\alpha\_{1}}\wedge 1+\lambda\int\_{1-t}^{1}F^{-1}(s)\mathrm{d}s-\mathds{1}\_{(1-\alpha\_{2},1]}(t). By the definition, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | gλ∗​(t)\displaystyle g\_{\lambda}^{\*}(t) | =(gλ​(1−α2)+gλ​(uα1,α2,λ)−gλ​(1−α2)uα1,α2,λ−1+α2​(t−1+α2))​𝟙[1−α2,uα1,α2,λ]​(t)\displaystyle=\left(g\_{\lambda}(1-\alpha\_{2})+\frac{g\_{\lambda}(u\_{\alpha\_{1},\alpha\_{2},\lambda})-g\_{\lambda}(1-\alpha\_{2})}{u\_{\alpha\_{1},\alpha\_{2},\lambda}-1+\alpha\_{2}}(t-1+\alpha\_{2})\right)\mathds{1}\_{[1-\alpha\_{2},u\_{\alpha\_{1},\alpha\_{2},\lambda}]}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | gλ​(t)​𝟙(0,1−α2)∪(uα1,α2,λ,1)​(t).\displaystyle~g\_{\lambda}(t)\mathds{1}\_{(0,1-\alpha\_{2})\cup(u\_{\alpha\_{1},\alpha\_{2},\lambda},1)}(t). |  |

Direct computation shows

|  |  |  |  |
| --- | --- | --- | --- |
|  | (gλ∗)′​(1−t)\displaystyle(g\_{\lambda}^{\*})^{\prime}(1-t) | =(11−α1​𝟙(α1,1)​(t)+λ​F−1​(t))​𝟙(0,1−uα1,α2,λ)∪(α2,1)​(t)\displaystyle=\left(\frac{1}{1-\alpha\_{1}}\mathds{1}\_{(\alpha\_{1},1)}(t)+\lambda F^{-1}(t)\right)\mathds{1}\_{(0,1-u\_{\alpha\_{1},\alpha\_{2},\lambda})\cup(\alpha\_{2},1)}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +cα1,α2,λ​𝟙(1−uα1,α2,λ,α2)​(t),t∈(0,1).\displaystyle~+c\_{\alpha\_{1},\alpha\_{2},\lambda}\mathds{1}\_{(1-u\_{\alpha\_{1},\alpha\_{2},\lambda},\alpha\_{2})}(t),~t\in(0,1). |  |

Applying Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we obtain the desired result.
∎

Proof of Theorem [2](https://arxiv.org/html/2511.08662v1#Thmtheorem2 "Theorem 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"). In light of the conclusion in Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), it suffices to show that supG∈ℳε​(μ,σ)ρg​(G)=supG∈ℳε​(μ,σ)ρg^​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G)=\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}}(G). As g⩽g^g\leqslant\hat{g}, we have supG∈ℳε​(μ,σ)ρg​(G)⩽supG∈ℳε​(μ,σ)ρg^​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G)\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}}(G). We next show the inverse inequality.

First, suppose g​(t)≠g^​(t)g(t)\neq\hat{g}(t) at finite number of points denoted by {t1,…,tm}\{t\_{1},\dots,t\_{m}\} with t1<t2<⋯<tmt\_{1}<t\_{2}<\dots<t\_{m}. Note that we have either g^​(ti)=limt↓tig​(t)\hat{g}(t\_{i})=\lim\_{t\downarrow t\_{i}}g(t) or g^​(ti)=limt↑tig​(t)\hat{g}(t\_{i})=\lim\_{t\uparrow t\_{i}}g(t). Let 𝒟1={i:g^​(ti)=limt↓tig​(t)}\mathcal{D}\_{1}=\{i:\hat{g}(t\_{i})=\lim\_{t\downarrow t\_{i}}g(t)\} and 𝒟2={i:g^​(ti)=limt↑tig​(t)}∖𝒟1\mathcal{D}\_{2}=\{i:\hat{g}(t\_{i})=\lim\_{t\uparrow t\_{i}}g(t)\}\setminus\mathcal{D}\_{1}. For n⩾1n\geqslant 1 and t∈(0,1)t\in(0,1), let

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gn−1​(t)\displaystyle G\_{n}^{-1}(t) | =G−1​(t)​𝟙((0,1)∖∪i∈𝒟1(1−ti−1/n2,1−ti+1/n))∖∪i∈𝒟2(1−ti−1/n,1−ti+1/n2)​(t)\displaystyle=G^{-1}(t)\mathds{1}\_{\left((0,1)\setminus\cup\_{i\in\mathcal{D}\_{1}}(1-t\_{i}-1/n^{2},1-t\_{i}+1/n)\right)\setminus\cup\_{i\in\mathcal{D}\_{2}}(1-t\_{i}-1/n,1-t\_{i}+1/n^{2})}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑i∈𝒟1n2n+1​∫1−ti−1/n21−ti+1/nG−1​(s)​ds​𝟙(1−ti−1/n2,1−ti+1/n)​(t)\displaystyle+\sum\_{i\in\mathcal{D}\_{1}}\frac{n^{2}}{n+1}\int\_{1-t\_{i}-1/n^{2}}^{1-t\_{i}+1/n}G^{-1}(s)\mathrm{d}s\mathds{1}\_{(1-t\_{i}-1/n^{2},1-t\_{i}+1/n)}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑i∈𝒟2n2n+1​∫1−ti−1/n1−ti+1/n2G−1​(s)​ds​𝟙(1−ti−1/n,1−ti+1/n2)​(t).\displaystyle+\sum\_{i\in\mathcal{D}\_{2}}\frac{n^{2}}{n+1}\int\_{1-t\_{i}-1/n}^{1-t\_{i}+1/n^{2}}G^{-1}(s)\mathrm{d}s\mathds{1}\_{(1-t\_{i}-1/n,1-t\_{i}+1/n^{2})}(t). |  |

Note that if n>max⁡(1/t1,1/(1−tm),maxi=1m−1⁡2ti+1−ti)n>\max(1/t\_{1},1/(1-t\_{m}),\max\_{i=1}^{m-1}\frac{2}{t\_{i+1}-t\_{i}}), then (1−ti−1/n2,1−ti+1/n),i∈𝒟1(1-t\_{i}-1/n^{2},1-t\_{i}+1/n),~i\in\mathcal{D}\_{1} and (1−ti−1/n,1−ti+1/n2),i∈𝒟2(1-t\_{i}-1/n,1-t\_{i}+1/n^{2}),~i\in\mathcal{D}\_{2} are disjoint subintervals of (0,1)(0,1).
We denote the standard deviation of GnG\_{n} by σn\sigma\_{n} and let

|  |  |  |  |
| --- | --- | --- | --- |
|  | G^n−1​(t)=μ+Gn−1​(t)−μσn​σ.\displaystyle\widehat{G}\_{n}^{-1}(t)=\mu+\frac{G\_{n}^{-1}(t)-\mu}{\sigma\_{n}}\sigma. |  | (25) |

Note that limn→∞dW​(G^n,F)⩽limn→∞(dW​(G^n,Gn)+dW​(Gn,F))=ε\lim\_{n\to\infty}d\_{W}(\widehat{G}\_{n},F)\leqslant\lim\_{n\to\infty}(d\_{W}(\widehat{G}\_{n},G\_{n})+d\_{W}(G\_{n},F))=\sqrt{\varepsilon}. Hence, for any η>0\eta>0, there exists n0>0n\_{0}>0 such that dW​(G^n,F)⩽ε+ηd\_{W}(\widehat{G}\_{n},F)\leqslant\sqrt{\varepsilon+\eta} for all n⩾n0n\geqslant n\_{0}. This implies G^n∈ℳε+η​(μ,σ)\widehat{G}\_{n}\in\mathcal{M}\_{\varepsilon+\eta}(\mu,\sigma) for all n⩾n0n\geqslant n\_{0}. Moreover, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρg^​(G)\displaystyle\rho\_{\hat{g}}(G) | =ρg^​(Gn)+∑i∈𝒟1(∫G−1​(1−ti−1/n2)G−1​(1−ti+1/n)g^​(1−G​(x))​dx−∫G−1​(1−ti−1/n2)G−1​(1−ti+1/n)g^​(1−Gn​(x))​dx)\displaystyle=\rho\_{\hat{g}}(G\_{n})+\sum\_{i\in\mathcal{D}\_{1}}\left(\int\_{G^{-1}(1-t\_{i}-1/n^{2})}^{G^{-1}(1-t\_{i}+1/n)}\hat{g}(1-G(x))\mathrm{d}x-\int\_{G^{-1}(1-t\_{i}-1/n^{2})}^{G^{-1}(1-t\_{i}+1/n)}\hat{g}(1-G\_{n}(x))\mathrm{d}x\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑i∈𝒟2(∫G−1​(1−ti−1/n)G−1​(1−ti+1/n2)g^​(1−G​(x))​dx−∫G−1​(1−ti−1/n)G−1​(1−ti+1/n2)g^​(1−Gn​(x))​dx).\displaystyle+\sum\_{i\in\mathcal{D}\_{2}}\left(\int\_{G^{-1}(1-t\_{i}-1/n)}^{G^{-1}(1-t\_{i}+1/n^{2})}\hat{g}(1-G(x))\mathrm{d}x-\int\_{G^{-1}(1-t\_{i}-1/n)}^{G^{-1}(1-t\_{i}+1/n^{2})}\hat{g}(1-G\_{n}(x))\mathrm{d}x\right). |  |

Direct computation gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞∫G−1​(1−ti−1/n2)G−1​(1−ti+1/n)g^​(1−G​(x))​dx\displaystyle\lim\_{n\to\infty}\int\_{G^{-1}(1-t\_{i}-1/n^{2})}^{G^{-1}(1-t\_{i}+1/n)}\hat{g}(1-G(x))\mathrm{d}x | =limn→∞∫G−1​(1−ti−1/n)G−1​(1−ti+1/n2)g^​(1−G​(x))​dx\displaystyle=\lim\_{n\to\infty}\int\_{G^{-1}(1-t\_{i}-1/n)}^{G^{-1}(1-t\_{i}+1/n^{2})}\hat{g}(1-G(x))\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =g^​(ti)​(G+−1​(1−ti)−G−1​(1−ti)).\displaystyle=\hat{g}(t\_{i})(G\_{+}^{-1}(1-t\_{i})-G^{-1}(1-t\_{i})). |  |

Moreover, it follows that for i∈𝒟1i\in\mathcal{D}\_{1}, ci,n:=n2n+1​∫1−ti−1/n21−ti+1/nG−1​(s)​ds→G+−1​(1−ti)c\_{i,n}:=\frac{n^{2}}{n+1}\int\_{1-t\_{i}-1/n^{2}}^{1-t\_{i}+1/n}G^{-1}(s)\mathrm{d}s\to G\_{+}^{-1}(1-t\_{i}) as n→∞n\to\infty and for i∈𝒟2i\in\mathcal{D}\_{2}, ci,n:=n2n+1​∫1−ti−1/n1−ti+1/n2G−1​(s)​ds→G−1​(1−ti)c\_{i,n}:=\frac{n^{2}}{n+1}\int\_{1-t\_{i}-1/n}^{1-t\_{i}+1/n^{2}}G^{-1}(s)\mathrm{d}s\to G^{-1}(1-t\_{i}) as n→∞n\to\infty.
This implies that if G+−1​(1−ti)>G−1​(1−ti)G\_{+}^{-1}(1-t\_{i})>G^{-1}(1-t\_{i}), then for i∈𝒟1i\in\mathcal{D}\_{1},

|  |  |  |
| --- | --- | --- |
|  | ∫G−1​(1−ti−1/n2)G−1​(1−ti+1/n)g^​(1−Gn​(x))​dx\displaystyle\int\_{G^{-1}(1-t\_{i}-1/n^{2})}^{G^{-1}(1-t\_{i}+1/n)}\hat{g}(1-G\_{n}(x))\mathrm{d}x |  |
|  |  |  |
| --- | --- | --- |
|  | =g^​(ti+1/n2)​(ci,n−G−1​(1−ti−1/n2))+g^​(ti−1/n)​(G−1​(1−ti+1/n)−ci,n)\displaystyle=\hat{g}(t\_{i}+1/n^{2})(c\_{i,n}-G^{-1}(1-t\_{i}-1/n^{2}))+\hat{g}(t\_{i}-1/n)(G^{-1}(1-t\_{i}+1/n)-c\_{i,n}) |  |
|  |  |  |
| --- | --- | --- |
|  | →g^​(ti)​(G+−1​(1−ti)−G−1​(1−ti)),n→∞.\displaystyle~\to\hat{g}(t\_{i})(G\_{+}^{-1}(1-t\_{i})-G^{-1}(1-t\_{i})),~n\to\infty. |  |

and for i∈𝒟2i\in\mathcal{D}\_{2},

|  |  |  |
| --- | --- | --- |
|  | ∫G−1​(1−ti−1/n)G−1​(1−ti+1/n2)g^​(1−Gn​(x))​dx\displaystyle\int\_{G^{-1}(1-t\_{i}-1/n)}^{G^{-1}(1-t\_{i}+1/n^{2})}\hat{g}(1-G\_{n}(x))\mathrm{d}x |  |
|  |  |  |
| --- | --- | --- |
|  | =g^​(ti+1/n)​(ci,n−G−1​(1−ti−1/n))+g^​(ti−1/n2)​(G−1​(1−ti+1/n2)−ci,n)\displaystyle=\hat{g}(t\_{i}+1/n)(c\_{i,n}-G^{-1}(1-t\_{i}-1/n))+\hat{g}(t\_{i}-1/n^{2})(G^{-1}(1-t\_{i}+1/n^{2})-c\_{i,n}) |  |
|  |  |  |
| --- | --- | --- |
|  | →g^​(ti)​(G+−1​(1−ti)−G−1​(1−ti)),n→∞.\displaystyle~\to\hat{g}(t\_{i})(G\_{+}^{-1}(1-t\_{i})-G^{-1}(1-t\_{i})),~n\to\infty. |  |

Note that the above conclusion also holds if G+−1​(1−ti)=G−1​(1−ti)G\_{+}^{-1}(1-t\_{i})=G^{-1}(1-t\_{i}).
Consequently, we have ρg^​(G)=limn→∞ρg^​(Gn)\rho\_{\hat{g}}(G)=\lim\_{n\to\infty}\rho\_{\hat{g}}(G\_{n}). By the definition of G^n\widehat{G}\_{n} and the properties of ρg\rho\_{g}, we have ρg​(G^n)=ρg^​(G^n)\rho\_{g}(\widehat{G}\_{n})=\rho\_{\hat{g}}(\widehat{G}\_{n}) and ρg^​(Gn)=ρg^​(G^n)−μ​g​(1)σ​σn+μ​g​(1)\rho\_{\hat{g}}(G\_{n})=\frac{\rho\_{\hat{g}}(\widehat{G}\_{n})-\mu g(1)}{\sigma}\sigma\_{n}+\mu g(1). Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρg^​(G)=limn→∞ρg^​(Gn)=limn→∞ρg​(G^n)−μ​g​(1)σ​σn+μ​g​(1)=limn→∞ρg​(G^n)⩽supG∈ℳε+η​(μ,σ)ρg​(G).\displaystyle\rho\_{\hat{g}}(G)=\lim\_{n\to\infty}\rho\_{\hat{g}}(G\_{n})=\lim\_{n\to\infty}\frac{\rho\_{g}(\widehat{G}\_{n})-\mu g(1)}{\sigma}\sigma\_{n}+\mu g(1)=\lim\_{n\to\infty}\rho\_{g}(\widehat{G}\_{n})\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon+\eta}(\mu,\sigma)}\rho\_{g}(G). |  | (26) |

Therefore, we conclude that supG∈ℳε​(μ,σ)ρg^​(G)⩽supG∈ℳε+η​(μ,σ)ρg​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}}(G)\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon+\eta}(\mu,\sigma)}\rho\_{g}(G) for any η>0\eta>0.

Next, we consider the case g≠g^g\neq\hat{g} on infinite number of points denoted by {ti,i⩾1}\{t\_{i},~i\geqslant 1\}. Let gm​(t)=g^​(t)​𝟙{t1,…,tm}​(t)+g​(t)​𝟙[0,1]∖{t1,…,tm}​(t)g\_{m}(t)=\hat{g}(t)\mathds{1}\_{\{t\_{1},\dots,t\_{m}\}}(t)+g(t)\mathds{1}\_{[0,1]\setminus\{t\_{1},\dots,t\_{m}\}}(t). Note that g≠gmg\neq g\_{m} on finite number of points {t1,…,tm}\{t\_{1},\dots,t\_{m}\} and gmg\_{m} is either left- or right-continuous on those points. For any G∈ℳε​(μ,σ)G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma), let G^n(m)\widehat{G}^{(m)}\_{n} be as in ([25](https://arxiv.org/html/2511.08662v1#A1.E25 "In Appendix A Proof of Section 3 ‣ Robust distortion risk metrics and portfolio optimization")). Applying the argument in ([26](https://arxiv.org/html/2511.08662v1#A1.E26 "In Appendix A Proof of Section 3 ‣ Robust distortion risk metrics and portfolio optimization")), we have for any η>0\eta>0,

|  |  |  |
| --- | --- | --- |
|  | ρgm​(G)=limn→∞ρg​(G^n(m))⩽supG∈ℳε+η​(μ,σ)ρg​(G).\rho\_{g\_{m}}(G)=\lim\_{n\to\infty}\rho\_{g}(\widehat{G}^{(m)}\_{n})\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon+\eta}(\mu,\sigma)}\rho\_{g}(G). |  |

Note that gm​(t)↑g^​(t)g\_{m}(t)\uparrow\hat{g}(t) as m→∞m\to\infty for all t∈[0,1]t\in[0,1]. If ρg​(G)>−∞\rho\_{g}(G)>-\infty, using the monotone convergence theorem, we have limm→∞ρgm​(G)=ρg^​(G)\lim\_{m\to\infty}\rho\_{g\_{m}}(G)=\rho\_{\hat{g}}(G). Consequently, we have ρg^​(G)⩽supG∈ℳε+η​(μ,σ)ρg​(G)\rho\_{\hat{g}}(G)\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon+\eta}(\mu,\sigma)}\rho\_{g}(G). If ρg^​(G)=−∞\rho\_{\hat{g}}(G)=-\infty, the previous conclusion holds obviously. Next, we focus on the case ρg^​(G)>−∞\rho\_{\hat{g}}(G)>-\infty and ρg​(G)=−∞\rho\_{g}(G)=-\infty. Let Gn​(x)=G​(x)​𝟙{x>−n}G\_{n}(x)=G(x)\mathds{1}\_{\{x>-n\}} for n⩾1n\geqslant 1.
We denote the mean and standard deviation of GnG\_{n} by μn\mu\_{n} and σn\sigma\_{n}, respectively. Let G¯n−1​(t)=μ+Gn−1​(t)−μnσn​σ\overline{G}\_{n}^{-1}(t)=\mu+\frac{G\_{n}^{-1}(t)-\mu\_{n}}{\sigma\_{n}}\sigma. For any η>0\eta>0, there exists n1⩾1n\_{1}\geqslant 1 such that G¯n∈ℳε+η/2​(μ,σ)\overline{G}\_{n}\in\mathcal{M}\_{\varepsilon+\eta/2}(\mu,\sigma) holds for all n⩾n1n\geqslant n\_{1}. Using the above argument, we have ρgm​(G¯n)⩽supG∈ℳε+η​(μ,σ)ρg​(G).\rho\_{g\_{m}}(\overline{G}\_{n})\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon+\eta}(\mu,\sigma)}\rho\_{g}(G). Using the monotone convergence theorem, we have ρg^​(G¯n)=limm→∞ρgm​(G¯n)⩽supG∈ℳε+η​(μ,σ)ρg​(G).\rho\_{\hat{g}}(\overline{G}\_{n})=\lim\_{m\to\infty}\rho\_{g\_{m}}(\overline{G}\_{n})\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon+\eta}(\mu,\sigma)}\rho\_{g}(G).
Letting n→∞n\to\infty, it follows that ρg^​(G)⩽supG∈ℳε+η​(μ,σ)ρg​(G).\rho\_{\hat{g}}(G)\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon+\eta}(\mu,\sigma)}\rho\_{g}(G).

By the arbitrary of GG, we have
supG∈ℳε​(μ,σ)ρg^​(G)⩽supG∈ℳε+η​(μ,σ)ρg​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}}(G)\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon+\eta}(\mu,\sigma)}\rho\_{g}(G) for any η>0\eta>0. Therefore, we can conclude that

|  |  |  |
| --- | --- | --- |
|  | supG∈ℳε​(μ,σ)ρg​(G)⩽supG∈ℳε​(μ,σ)ρg^​(G)⩽limη↓0supG∈ℳε+η​(μ,σ)ρg​(G).\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G)\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}}(G)\leqslant\lim\_{\eta\downarrow 0}\sup\_{G\in\mathcal{M}\_{\varepsilon+\eta}(\mu,\sigma)}\rho\_{g}(G). |  |

Let l​(ε):=supG∈ℳε​(μ,σ)ρg^​(G)l(\varepsilon):=\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}}(G). Then we have ll is increasing and

|  |  |  |
| --- | --- | --- |
|  | limη↓0l​(ε−η)⩽supG∈ℳε​(μ,σ)ρg​(G)⩽l​(ε).\displaystyle\lim\_{\eta\downarrow 0}l(\varepsilon-\eta)\leqslant\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G)\leqslant l(\varepsilon). |  |

Note that the continuity of ρg^​(Hλ)\rho\_{\hat{g}}(H\_{\lambda}) with respect to λ\lambda over (0,∞)(0,\infty) implies the continuity of ll for (μF−μ)2+(σF−σ)2<ε<(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}<\varepsilon<(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}). Hence, we have supG∈ℳε​(μ,σ)ρg​(G)=supG∈ℳε​(μ,σ)ρg^​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G)=\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}}(G). Applying Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we obtain the conclusion of (i).

For ε>(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)\varepsilon>(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}), we have l​(ε)l(\varepsilon) is a constant. Hence, supG∈ℳε​(μ,σ)ρg​(G)=supG∈ℳε​(μ,σ)ρg^​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{g}(G)=\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}}(G) holds. For ε=(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c0)\varepsilon=(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-c\_{0}), the conclusion follows from Theorem 5 and Remark 2 of Pesenti al. ([2024](https://arxiv.org/html/2511.08662v1#bib.bib29)). Applying Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we obtain the results in (ii).
We complete the proof. ∎

Proof of Corollary [2](https://arxiv.org/html/2511.08662v1#Thmcorollary2 "Corollary 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"). (i) By Corollary [1](https://arxiv.org/html/2511.08662v1#Thmcorollary1 "Corollary 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we have

|  |  |  |
| --- | --- | --- |
|  | VaRα+​(Hλ)=μ+σ​1+λ​∫α1−t1−α,λF−1​(s)​ds1−α−t1−α,λ−aλbλ.\mathrm{VaR}\_{\alpha}^{+}(H\_{\lambda})=\mu+\sigma\frac{\frac{1+\lambda\int\_{\alpha}^{1-t\_{1-\alpha,\lambda}}F^{-1}(s)\mathrm{d}s}{1-\alpha-t\_{1-\alpha,\lambda}}-a\_{\lambda}}{b\_{\lambda}}. |  |

Clearly, aλa\_{\lambda} is continuous for λ∈(0,∞)\lambda\in(0,\infty). Note that bλ=∫01((gλ∗)′​(t))2​dt−(g​(1)+λ​μF)2b\_{\lambda}=\sqrt{\int\_{0}^{1}((g\_{\lambda}^{\*})^{\prime}(t))^{2}\mathrm{d}t-(g(1)+\lambda\mu\_{F})^{2}}. Hence, the continuity of bλb\_{\lambda} is implied
by the uniform integrability of {((gλ∗)′​(t))2,0⩽λ⩽λ0}\{((g\_{\lambda}^{\*})^{\prime}(t))^{2},0\leqslant\lambda\leqslant\lambda\_{0}\} for any λ0>0\lambda\_{0}>0 and the fact that (gλ∗)′​(t)→(gλ0∗)′​(t)(g\_{\lambda}^{\*})^{\prime}(t)\to(g\_{\lambda\_{0}}^{\*})^{\prime}(t) a.e. as λ→λ0\lambda\to\lambda\_{0}, showed in the proof of Lemma [1](https://arxiv.org/html/2511.08662v1#Thmlemma1 "Lemma 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"). Using the expression of (gλ∗)′​(t)(g\_{\lambda}^{\*})^{\prime}(t) given in (i) of Corollary [1](https://arxiv.org/html/2511.08662v1#Thmcorollary1 "Corollary 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), the fact (gλ∗)′​(t)→(gλ0∗)′​(t)(g\_{\lambda}^{\*})^{\prime}(t)\to(g\_{\lambda\_{0}}^{\*})^{\prime}(t) a.e. as λ→λ0\lambda\to\lambda\_{0} also implies

|  |  |  |
| --- | --- | --- |
|  | 1+λ​∫α1−t1−α,λF−1​(s)​ds1−α−t1−α,λ→1+λ​∫α1−t1−α,λ0F−1​(s)​ds1−α−t1−α,λ0,as​λ→λ0.\frac{1+\lambda\int\_{\alpha}^{1-t\_{1-\alpha,\lambda}}F^{-1}(s)\mathrm{d}s}{1-\alpha-t\_{1-\alpha,\lambda}}\to\frac{1+\lambda\int\_{\alpha}^{1-t\_{1-\alpha,\lambda\_{0}}}F^{-1}(s)\mathrm{d}s}{1-\alpha-t\_{1-\alpha,\lambda\_{0}}},~\text{as}~\lambda\to\lambda\_{0}. |  |

Hence, VaRα+​(Hλ)\mathrm{VaR}\_{\alpha}^{+}(H\_{\lambda}) is continuous for λ∈(0,∞)\lambda\in(0,\infty). In light of Theorem [2](https://arxiv.org/html/2511.08662v1#Thmtheorem2 "Theorem 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we obtain the desired result.

(ii) By Corollary [1](https://arxiv.org/html/2511.08662v1#Thmcorollary1 "Corollary 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we have IQD+​(Hλ)=gλ​(α)−gλ​(tα,λ)α−tα,λ−gλ​(t^α,λ)−gλ​(1−α)t^α,λ−1+αbλ​σ\mathrm{IQD}^{+}(H\_{\lambda})=\frac{\frac{g\_{\lambda}(\alpha)-g\_{\lambda}(t\_{\alpha,\lambda})}{\alpha-t\_{\alpha,\lambda}}-\frac{g\_{\lambda}(\hat{t}\_{\alpha,\lambda})-g\_{\lambda}(1-\alpha)}{\hat{t}\_{\alpha,\lambda}-1+\alpha}}{b\_{\lambda}}\sigma. The continuity of bλb\_{\lambda} is discussed in (i). Using the expression of (gλ∗)′​(t)(g\_{\lambda}^{\*})^{\prime}(t) given in (ii) of Corollary [1](https://arxiv.org/html/2511.08662v1#Thmcorollary1 "Corollary 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), the continuity of gλ​(α)−gλ​(tα,λ)α−tα,λ\frac{g\_{\lambda}(\alpha)-g\_{\lambda}(t\_{\alpha,\lambda})}{\alpha-t\_{\alpha,\lambda}} and gλ​(t^α,λ)−gλ​(1−α)t^α,λ−1+α\frac{g\_{\lambda}(\hat{t}\_{\alpha,\lambda})-g\_{\lambda}(1-\alpha)}{\hat{t}\_{\alpha,\lambda}-1+\alpha} are implied by the fact that (gλ∗)′​(t)→(gλ0∗)′​(t)(g\_{\lambda}^{\*})^{\prime}(t)\to(g\_{\lambda\_{0}}^{\*})^{\prime}(t) a.e. as λ→λ0\lambda\to\lambda\_{0} for any λ0>0\lambda\_{0}>0, showed in the proof of Lemma [1](https://arxiv.org/html/2511.08662v1#Thmlemma1 "Lemma 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"). Hence, IQD+​(Hλ)\mathrm{IQD}^{+}(H\_{\lambda}) is continuous for λ\lambda over (0,∞)(0,\infty). Applying Theorem [2](https://arxiv.org/html/2511.08662v1#Thmtheorem2 "Theorem 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we obtain the desired conclusion.

(iii) For g=g^β,αh1,h2g=\hat{g}^{h\_{1},h\_{2}}\_{\beta,\alpha}, we have
gλ​(t)=gβ,αh1,h2​(t)∧h2+λ​∫1−t1F−1​(s)​ds+(1−h2)​𝟙[1−α,1]​(t)g\_{\lambda}(t)=g^{h\_{1},h\_{2}}\_{\beta,\alpha}(t)\wedge h\_{2}+\lambda\int\_{1-t}^{1}F^{-1}(s)\mathrm{d}s+(1-h\_{2})\mathds{1}\_{[1-\alpha,1]}(t). The condition h11−β⩾h2−h1β−α\frac{h\_{1}}{1-\beta}\geqslant\frac{h\_{2}-h\_{1}}{\beta-\alpha} guarantees that gβ,αh1,h2​(t)∧h2g^{h\_{1},h\_{2}}\_{\beta,\alpha}(t)\wedge h\_{2} is concave over (0,1)(0,1). Hence, by the definition, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | gλ∗​(t)\displaystyle g\_{\lambda}^{\*}(t) | =(gλ​(uα,β,λh1,h2)+gλ​(1−α)−gλ​(uα,β,λh1,h2)1−α−uα,β,λh1,h2​(t−uα,β,λh1,h2))​𝟙[uα,β,λh1,h2,1−α]​(t)\displaystyle=\left(g\_{\lambda}(u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}})+\frac{g\_{\lambda}(1-\alpha)-g\_{\lambda}(u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}})}{1-\alpha-u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}}}(t-u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}})\right)\mathds{1}\_{[u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}},1-\alpha]}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +gλ​(t)​𝟙(0,uα,β,λh1,h2)∪(1−α,1)​(t),\displaystyle~+g\_{\lambda}(t)\mathds{1}\_{(0,u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}})\cup(1-\alpha,1)}(t), |  |

which implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | (gλ∗)′​(1−t)\displaystyle(g\_{\lambda}^{\*})^{\prime}(1-t) | =cα,β,λh1,h2​𝟙(α,1−uα,β,λh1,h2)​(t)+h11−β​𝟙(β∨(1−uα,β,λh1,h2),1)​(t)+h2−h1β−α​𝟙(β∧(1−uα,β,λh1,h2),β)​(t)\displaystyle=c\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}}\mathds{1}\_{(\alpha,1-u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}})}(t)+\frac{h\_{1}}{1-\beta}\mathds{1}\_{(\beta\vee(1-u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}}),1)}(t)+\frac{h\_{2}-h\_{1}}{\beta-\alpha}\mathds{1}\_{(\beta\wedge(1-u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}}),\beta)}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λ​F−1​(t)​𝟙(0,α)∪(1−uα,β,λh1,h2,1)​(t),t∈(0,1).\displaystyle+\lambda F^{-1}(t)\mathds{1}\_{(0,\alpha)\cup(1-u\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}},1)}(t),~t\in(0,1). |  |

Applying Theorem [1](https://arxiv.org/html/2511.08662v1#Thmtheorem1 "Theorem 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"), we can obtain the expression of supG∈ℳε​(μ,σ)ρg^β,αh1,h2​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}\_{\beta,\alpha}^{h\_{1},h\_{2}}}(G). Note that ρg^β,αh1,h2=w1​ESα+w2​ESβ+w3​VaRα+\rho\_{\hat{g}\_{\beta,\alpha}^{h\_{1},h\_{2}}}=w\_{1}\mathrm{ES}\_{\alpha}+w\_{2}\mathrm{ES}\_{\beta}+w\_{3}\mathrm{VaR}\_{\alpha}^{+} with some w1,w2,w3⩾0w\_{1},w\_{2},w\_{3}\geqslant 0 satisfying w1+w2+w3=1w\_{1}+w\_{2}+w\_{3}=1. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supG∈ℳε​(μ,σ)ρg^β,αh1,h2​(G)\displaystyle\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}\_{\beta,\alpha}^{h\_{1},h\_{2}}}(G) | =σbλ​(w11−α​∫α1(gλ∗)′​(1−t)​dt+w21−β​∫β1(gλ∗)′​(1−t)​dt+w3​cα,β,λh1,h2)\displaystyle=\frac{\sigma}{b\_{\lambda}}\left(\frac{w\_{1}}{1-\alpha}\int\_{\alpha}^{1}(g\_{\lambda}^{\*})^{\prime}(1-t)\mathrm{d}t+\frac{w\_{2}}{1-\beta}\int\_{\beta}^{1}(g\_{\lambda}^{\*})^{\prime}(1-t)\mathrm{d}t+w\_{3}c\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +μ−σ​(1+λ​μF)bλ.\displaystyle+\mu-\frac{\sigma(1+\lambda\mu\_{F})}{b\_{\lambda}}. |  |

The continuity of bλb\_{\lambda}, cα,β,λh1,h2c\_{\alpha,\beta,\lambda}^{h\_{1},h\_{2}}, ∫α1(gλ∗)′​(1−t)​dt\int\_{\alpha}^{1}(g\_{\lambda}^{\*})^{\prime}(1-t)\mathrm{d}t and ∫β1(gλ∗)′​(1−t)​dt\int\_{\beta}^{1}(g\_{\lambda}^{\*})^{\prime}(1-t)\mathrm{d}t are implied
by the uniform integrability of {((gλ∗)′​(t))2,0⩽λ⩽λ0}\{((g\_{\lambda}^{\*})^{\prime}(t))^{2},0\leqslant\lambda\leqslant\lambda\_{0}\} for any λ0>0\lambda\_{0}>0 and the fact that (gλ∗)′​(t)→(gλ0∗)′​(t)(g\_{\lambda}^{\*})^{\prime}(t)\to(g\_{\lambda\_{0}}^{\*})^{\prime}(t) a.e. as λ→λ0\lambda\to\lambda\_{0}, showed in the proof of Lemma [1](https://arxiv.org/html/2511.08662v1#Thmlemma1 "Lemma 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization").
It follows from Theorem [2](https://arxiv.org/html/2511.08662v1#Thmtheorem2 "Theorem 2. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization") that supG∈ℳε​(μ,σ)GlueVaRβ,αh1,h2​(G)=supG∈ℳε​(μ,σ)ρg^β,αh1,h2​(G)\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\mathrm{GlueVaR}\_{\beta,\alpha}^{h\_{1},h\_{2}}(G)=\sup\_{G\in\mathcal{M}\_{\varepsilon}(\mu,\sigma)}\rho\_{\hat{g}\_{\beta,\alpha}^{h\_{1},h\_{2}}}(G). This completes the proof.
∎

Proof of Proposition [1](https://arxiv.org/html/2511.08662v1#Thmproposition1 "Proposition 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization").
If gg is concave distortion function, then

|  |  |  |
| --- | --- | --- |
|  | gλ∗​(t)=gλ​(t)=g​(t)+λ​∫1−t1F−1​(s)​𝑑s,g\_{\lambda}^{\*}(t)=g\_{\lambda}(t)=g(t)+\lambda\int\_{1-t}^{1}F^{-1}(s)ds, |  |

which implies

|  |  |  |
| --- | --- | --- |
|  | (gλ∗)′​(t)=g′​(t)+λ​F−1​(1−t),hλ​(t)=μ+σ​g′​(1−t)+λ​F−1​(t)−aλbλ,(g\_{\lambda}^{\*})^{\prime}(t)=g^{\prime}(t)+\lambda F^{-1}(1-t),~h\_{\lambda}(t)=\mu+\sigma\frac{g^{\prime}(1-t)+\lambda F^{-1}(t)-a\_{\lambda}}{b\_{\lambda}}, |  |

where aλ=g​(1)+λ​μFa\_{\lambda}=g(1)+\lambda\mu\_{F} and bλ=∫01((gλ∗)′​(t))2​dt−(g​(1)+λ​μF)2b\_{\lambda}=\sqrt{\int\_{0}^{1}((g\_{\lambda}^{\*})^{\prime}(t))^{2}\mathrm{d}t-(g(1)+\lambda\mu\_{F})^{2}}. By definition, dW​(F,Hλ)=εd\_{W}(F,H\_{\lambda})=\sqrt{\varepsilon} can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | ε=μF2+σF2+μ2+σ2−2​C​o​v​(F−1​(V),hλ​(V))−2​μ​μF,\varepsilon=\mu^{2}\_{F}+\sigma^{2}\_{F}+\mu^{2}+\sigma^{2}-2Cov(F^{-1}(V),h\_{\lambda}(V))-2\mu\mu\_{F}, |  |

which implies

|  |  |  |
| --- | --- | --- |
|  | C​o​v​(F−1​(V),hλ​(V))=μF2+σF2+μ2+σ2−2​μ​μF−ε2=Cε,F⩾0.Cov(F^{-1}(V),h\_{\lambda}(V))=\frac{\mu\_{F}^{2}+\sigma\_{F}^{2}+\mu^{2}+\sigma^{2}-2\mu\mu\_{F}-\varepsilon}{2}=C\_{\varepsilon,F}\geqslant 0. |  |

Using the expression of hλh\_{\lambda}, we have

|  |  |  |
| --- | --- | --- |
|  | Cov(F−1(V),hλ(V))=σbλCov(F−1(V),g′(1−V))+λF−1(V))=σbλ(Cg,F+λσF2).\displaystyle Cov(F^{-1}(V),h\_{\lambda}(V))=\frac{\sigma}{b\_{\lambda}}Cov(F^{-1}(V),g^{\prime}(1-V))+\lambda F^{-1}(V))=\frac{\sigma}{b\_{\lambda}}(C\_{g,F}+\lambda\sigma^{2}\_{F}). |  |

Hence, we have bλ=σ​(Cg,F+λ​σF2)Cε,Fb\_{\lambda}=\frac{\sigma(C\_{g,F}+\lambda\sigma^{2}\_{F})}{C\_{\varepsilon,F}}.
Moreover, by definition, bλ=Vg+2​λ​Cg,F+λ2​σF2b\_{\lambda}=\sqrt{V\_{g}+2\lambda C\_{g,F}+\lambda^{2}\sigma\_{F}^{2}}. Hence, we have Cε,F2​(Vg+2​λ​Cg,F+λ2​σF2)=(σ​Cg,F+λ​σ​σF2)2C\_{\varepsilon,F}^{2}(V\_{g}+2\lambda C\_{g,F}+\lambda^{2}\sigma\_{F}^{2})=(\sigma C\_{g,F}+\lambda\sigma\sigma\_{F}^{2})^{2}, which can be simplified as
λ2σF2++2λCg,F+Vg​Cε,F2−σ2​Cg,F2Cε,F2−σ2​σF2=0\lambda^{2}\sigma\_{F}^{2}++2\lambda C\_{g,F}+\frac{V\_{g}C\_{\varepsilon,F}^{2}-\sigma^{2}C\_{g,F}^{2}}{C\_{\varepsilon,F}^{2}-\sigma^{2}\sigma\_{F}^{2}}=0.
Solving the quadratic equation, we have

|  |  |  |
| --- | --- | --- |
|  | λε=−Cg,F+Cg,F2−σF2​Vg​Cε,F2−σ2​Cg,F2Cε,F2−σ2​σF2σF2.\lambda\_{\varepsilon}=\frac{-C\_{g,F}+\sqrt{C\_{g,F}^{2}-\sigma\_{F}^{2}\frac{V\_{g}C\_{\varepsilon,F}^{2}-\sigma^{2}C\_{g,F}^{2}}{C\_{\varepsilon,F}^{2}-\sigma^{2}\sigma\_{F}^{2}}}}{\sigma\_{F}^{2}}. |  |

∎

## Appendix B Proofs of results in Section [4](https://arxiv.org/html/2511.08662v1#S4 "4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")

In this section, we offer the proofs for all results in Section [4](https://arxiv.org/html/2511.08662v1#S4 "4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"). Let ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle denote the inner product of two functions in ℱU,ξ−1\mathcal{F}\_{U,\xi}^{-1}.

Proof of Proposition [2](https://arxiv.org/html/2511.08662v1#Thmproposition2 "Proposition 2 (Bounds for unimodal distribution functions with a given inflection point). ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"). By definition, γξ↑​(u)∈ℱU,ξ−1\gamma^{\uparrow}\_{\xi}(u)\in\mathcal{F}\_{U,\xi}^{-1}. Since γξ↑\gamma^{\uparrow}\_{\xi} is not constant, this implies that hξ↑​(u)∈ℱU,ξ−1​(μ,σ)h^{\uparrow}\_{\xi}(u)\in\mathcal{F}\_{U,\xi}^{-1}(\mu,\sigma). Consider any h​(u)∈ℱU,ξ−1​(μ,σ)h(u)\in\mathcal{F}\_{U,\xi}^{-1}(\mu,\sigma), then k​(u)=b^ξ​(h​(u)−μ)/σ+a^ξ∈ℱU,ξ−1k(u)=\hat{b}\_{\xi}\left(h(u)-\mu\right)/\sigma+\hat{a}\_{\xi}\in\mathcal{F}\_{U,\xi}^{-1}. Moreover, it holds that ‖γξ↑‖2=‖k‖2\|\gamma^{\uparrow}\_{\xi}\|\_{2}=\|k\|\_{2}. Thus, the stated assertion follows from the following equivalent inequalities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖γ−γξ↑‖2⩽‖γ−k‖2\displaystyle\|\gamma-\gamma^{\uparrow}\_{\xi}\|\_{2}\leqslant\|\gamma-k\|\_{2}\quad | ⇔⟨γ,γξ↑⟩⩾⟨γ,k⟩\displaystyle\Leftrightarrow\quad\langle\gamma,~\gamma^{\uparrow}\_{\xi}\rangle\geqslant\langle\gamma,~k\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇔⟨γ,hξ↑⟩⩾⟨γ,h⟩\displaystyle\Leftrightarrow\quad\langle\gamma,~h^{\uparrow}\_{\xi}\rangle\geqslant\langle\gamma,~h\rangle\ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⇔ρg​(hξ↑)⩾ρg​(h).\displaystyle\Leftrightarrow\quad\rho\_{g}(h^{\uparrow}\_{\xi})\geqslant\rho\_{g}(h). |  |

Note that unless γξ↑=k\gamma\_{\xi}^{\uparrow}=k the inequalities are strict, which implies that the solution is unique. Using the above conclusion, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | supG−1∈ℱU,ξ−1​(μ,σ)ρg​(G−1)\displaystyle\sup\_{G^{-1}\in\mathcal{F}^{-1}\_{U,\xi}(\mu,\sigma)}\rho\_{g}(G^{-1}) | =⟨γ,μ+σ​(γξ↑−a^ξb^ξ)⟩\displaystyle=\left\langle\gamma,\mu+\sigma\left(\frac{\gamma^{\uparrow}\_{\xi}-\hat{a}\_{\xi}}{\hat{b}\_{\xi}}\right)\right\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =μ​g​(1)+σb^ξ​⟨γ,γξ↑−a^ξ⟩.\displaystyle=\mu g(1)+\frac{\sigma}{\hat{b}\_{\xi}}\langle\gamma,\gamma^{\uparrow}\_{\xi}-\hat{a}\_{\xi}\rangle. |  |

By Corollary 2.3 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12)), we have ⟨γ−γξ↑,γξ↑⟩=0\langle\gamma-\gamma^{\uparrow}\_{\xi},\gamma^{\uparrow}\_{\xi}\rangle=0 and ⟨γ−γξ↑,c⟩=0\langle\gamma-\gamma^{\uparrow}\_{\xi},c\rangle=0 for any c∈ℝc\in\mathbb{R}. Therefore, we have

|  |  |  |
| --- | --- | --- |
|  | ⟨γ,γξ↑−a^ξ⟩=⟨γ−γξ↑+γξ↑,γξ↑−a^ξ⟩=⟨γξ↑,γξ↑−a^ξ⟩=⟨γξ↑−a^ξ,γξ↑−a^ξ⟩=b^ξ2.\langle\gamma,\gamma^{\uparrow}\_{\xi}-\hat{a}\_{\xi}\rangle=\langle\gamma-\gamma^{\uparrow}\_{\xi}+\gamma^{\uparrow}\_{\xi},\gamma^{\uparrow}\_{\xi}-\hat{a}\_{\xi}\rangle=\langle\gamma^{\uparrow}\_{\xi},\gamma^{\uparrow}\_{\xi}-\hat{a}\_{\xi}\rangle=\langle\gamma^{\uparrow}\_{\xi}-\hat{a}\_{\xi},\gamma^{\uparrow}\_{\xi}-\hat{a}\_{\xi}\rangle=\hat{b}\_{\xi}^{2}. |  |

Hence, supG−1∈ℱU,ξ−1​(μ,σ)ρg​(G−1)​μ​g​(1)+σ​b^ξ.\sup\_{G^{-1}\in\mathcal{F}^{-1}\_{U,\xi}(\mu,\sigma)}\rho\_{g}(G^{-1})\mu g(1)+\sigma\hat{b}\_{\xi}.
This completes the proof.
∎

Proof of Proposition [3](https://arxiv.org/html/2511.08662v1#Thmproposition3 "Proposition 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"). Let γ​(u)=∑i=1nyi​𝟙(xi−1,xi)​(u)\gamma(u)=\sum\_{i=1}^{n}y\_{i}\mathds{1}\_{(x\_{i-1},x\_{i})}(u) with 0=x0<x1<⋯<xn=10=x\_{0}<x\_{1}<\dots<x\_{n}=1 and yi∈ℝy\_{i}\in\mathbb{R}. Without loss of generality, suppose ξ∈(xi0−1,xi0)\xi\in(x\_{i\_{0}-1},x\_{i\_{0}}). Then we choose one interval from {(xi−1,xi),i≠i0}∪{(xi0−1,ξ),(ξ,xi0)}\{(x\_{i-1},x\_{i}),i\neq i\_{0}\}\cup\{(x\_{i\_{0}-1},\xi),(\xi,x\_{i\_{0}})\} and denote it by (a,b)(a,b). Moreover, the value of γ\gamma over this interval is denoted by yy. Suppose b⩽ξb\leqslant\xi. Then γξ↑\gamma^{\uparrow}\_{\xi} is concave over (a,b)(a,b).

If γξ↑​(a)⩾y\gamma^{\uparrow}\_{\xi}(a)\geqslant y,
define γ1​(u)=γξ↑​(b)−γξ↑​(a)b−a​(u−a)+γξ↑​(a)\gamma\_{1}(u)=\frac{\gamma^{\uparrow}\_{\xi}(b)-\gamma^{\uparrow}\_{\xi}(a)}{b-a}(u-a)+\gamma^{\uparrow}\_{\xi}(a) for u∈(a,b)u\in(a,b) and otherwise γ1​(u)=γξ↑​(u)\gamma\_{1}(u)=\gamma^{\uparrow}\_{\xi}(u). Clearly, γ1∈FU,ξ−1\gamma\_{1}\in{F}^{-1}\_{U,\xi} and ‖γ1−γ‖2⩽‖γξ↑−γ‖2\|\gamma\_{1}-\gamma\|\_{2}\leqslant\|\gamma^{\uparrow}\_{\xi}-\gamma\|\_{2}. The uniqueness of γξ↑\gamma^{\uparrow}\_{\xi} implies γξ↑=γ1\gamma^{\uparrow}\_{\xi}=\gamma\_{1}. Hence, γξ↑\gamma^{\uparrow}\_{\xi} is linear over (a,b)(a,b).

If γξ↑​(a)<y<γξ↑​(b)\gamma^{\uparrow}\_{\xi}(a)<y<\gamma^{\uparrow}\_{\xi}(b), then there exists a<c<ba<c<b such that γξ↑​(c)=0\gamma^{\uparrow}\_{\xi}(c)=0. Define

|  |  |  |
| --- | --- | --- |
|  | γ2​(u)=(γξ↑​(b)−γξ↑​(c)b−c​(u−b)+γξ↑​(b))​⋀((γξ↑)+′​(a)​(u−a)+γξ↑​(a))\gamma\_{2}(u)=\left(\frac{\gamma^{\uparrow}\_{\xi}(b)-\gamma^{\uparrow}\_{\xi}(c)}{b-c}(u-b)+\gamma^{\uparrow}\_{\xi}(b)\right)\bigwedge\left((\gamma^{\uparrow}\_{\xi})\_{+}^{\prime}(a)(u-a)+\gamma^{\uparrow}\_{\xi}(a)\right) |  |

for u∈(a,b)u\in(a,b) and otherwise γ2​(u)=γξ↑​(u)\gamma\_{2}(u)=\gamma^{\uparrow}\_{\xi}(u), where (γξ↑)+′​(a)(\gamma^{\uparrow}\_{\xi})\_{+}^{\prime}(a) is the right derivative of γξ↑\gamma^{\uparrow}\_{\xi} at u=au=a. Clearly, γ2∈FU,ξ−1\gamma\_{2}\in{F}^{-1}\_{U,\xi} and ‖γ2−γ‖2⩽‖γξ↑−γ‖2\|\gamma\_{2}-\gamma\|\_{2}\leqslant\|\gamma^{\uparrow}\_{\xi}-\gamma\|\_{2}. Using the uniqueness of γξ↑\gamma^{\uparrow}\_{\xi}, we have γξ↑=γ2\gamma^{\uparrow}\_{\xi}=\gamma\_{2}. Hence, γξ↑\gamma^{\uparrow}\_{\xi} is linear over (a,b)(a,b).

If γξ↑​(b)⩽y\gamma^{\uparrow}\_{\xi}(b)\leqslant y, then define

|  |  |  |
| --- | --- | --- |
|  | γ3​(u)=((γξ↑)+′​(a)​(u−a)+γξ↑​(a))​⋀((γξ↑)−′​(b)​(u−b)+γξ↑​(b))\gamma\_{3}(u)=\left((\gamma^{\uparrow}\_{\xi})\_{+}^{\prime}(a)(u-a)+\gamma^{\uparrow}\_{\xi}(a)\right)\bigwedge\left((\gamma^{\uparrow}\_{\xi})\_{-}^{\prime}(b)(u-b)+\gamma^{\uparrow}\_{\xi}(b)\right) |  |

for u∈(a,b)u\in(a,b) and otherwise γ3​(u)=γξ↑​(u)\gamma\_{3}(u)=\gamma^{\uparrow}\_{\xi}(u), where (γξ↑)−′​(b)(\gamma^{\uparrow}\_{\xi})\_{-}^{\prime}(b) is the left derivative of γξ↑\gamma^{\uparrow}\_{\xi} at u=bu=b. Clearly, γ3∈FU,ξ−1\gamma\_{3}\in{F}^{-1}\_{U,\xi} and ‖γ3−γ‖2⩽‖γξ↑−γ‖2\|\gamma\_{3}-\gamma\|\_{2}\leqslant\|\gamma^{\uparrow}\_{\xi}-\gamma\|\_{2}. Using the same argument as above, we conclude that γξ↑\gamma^{\uparrow}\_{\xi} is linear over (a,b)(a,b).

Using the similar arguments, we can show the conclusion also holds for a⩾ξa\geqslant\xi, i.e., the case that γξ↑\gamma^{\uparrow}\_{\xi} is convex over (a,b)(a,b).

The above proof shows that if ξ=xi0\xi=x\_{i\_{0}} for some i0=0,1,…,ni\_{0}=0,1,\dots,n, then γξ↑\gamma^{\uparrow}\_{\xi} satisfies ([15](https://arxiv.org/html/2511.08662v1#S4.E15 "In Proposition 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")). Moreover, it follows from Corollary 2.3 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12)) that ⟨γ−γξ↑,1⟩=0\langle\gamma-\gamma^{\uparrow}\_{\xi},1\rangle=0, which implies ([16](https://arxiv.org/html/2511.08662v1#S4.E16 "In Proposition 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization")). Direct computaiton shows that

|  |  |  |
| --- | --- | --- |
|  | ∫01(γ​(u)−γξ↑​(u))2​du\displaystyle\int\_{0}^{1}(\gamma(u)-\gamma^{\uparrow}\_{\xi}(u))^{2}\mathrm{d}u |  |
|  |  |  |
| --- | --- | --- |
|  | =∑i=1n((ei+)3−(ei−)33​ci−+(ei++ci+​(xi−ai))3−(ei+)33​ci+)\displaystyle=\sum\_{i=1}^{n}\left(\frac{(e\_{i}^{+})^{3}-(e\_{i}^{-})^{3}}{3c\_{i}^{-}}+\frac{(e\_{i}^{+}+c\_{i}^{+}(x\_{i}-a\_{i}))^{3}-(e\_{i}^{+})^{3}}{3c\_{i}^{+}}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =∑i=1n((ai−xi−1)​((ei+)2+ei+​ei−+(ei−)2)3+(xi−ai)​((ei++ci+​(xi−ai))2+(ei++ci+​(xi−ai))​ei++(ei+)2)3),\displaystyle=\sum\_{i=1}^{n}\left(\frac{(a\_{i}-x\_{i-1})((e\_{i}^{+})^{2}+e\_{i}^{+}e\_{i}^{-}+(e\_{i}^{-})^{2})}{3}+\frac{(x\_{i}-a\_{i})((e\_{i}^{+}+c\_{i}^{+}(x\_{i}-a\_{i}))^{2}+(e\_{i}^{+}+c\_{i}^{+}(x\_{i}-a\_{i}))e\_{i}^{+}+(e\_{i}^{+})^{2})}{3}\right), |  |

where ei−=g​(1)−∑j=in(cj−​(aj−xj−1)+cj+​(xj−aj))−yie\_{i}^{-}=g(1)-\sum\_{j=i}^{n}\left(c\_{j}^{-}(a\_{j}-x\_{j-1})+c\_{j}^{+}(x\_{j}-a\_{j})\right)-y\_{i} and ei+=ei−+ci−​(ai−xi−1),i=1,…,ne\_{i}^{+}=e\_{i}^{-}+c\_{i}^{-}(a\_{i}-x\_{i-1}),~i=1,\dots,n. Hence, the optimal parameters are the minimizer of the above quantity over 𝒟n\mathcal{D}\_{n}. This completes the proof.
∎

Proof of Proposition [4](https://arxiv.org/html/2511.08662v1#Thmproposition4 "Proposition 4. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"). Since the projection operator is distance reducing with respect to the L2L^{2}-norm (Theorem 2.3 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12))), it follows that

|  |  |  |
| --- | --- | --- |
|  | ‖γξ,n↑−γξ↑‖2⩽‖γn−γ‖2.\|\gamma^{\uparrow}\_{\xi,n}-\gamma^{\uparrow}\_{\xi}\|\_{2}\leqslant\|\gamma\_{n}-\gamma\|\_{2}. |  |

Moreover, note that ℱU,ξ−1\mathcal{F}^{-1}\_{U,\xi} is a closed convex cone and

|  |  |  |
| --- | --- | --- |
|  | b^ξ2−b^ξ,n2=⟨γξ↑,γξ↑⟩−⟨γξ,n↑,γξ,n↑⟩−(a^ξ2−a^ξ,n2).\hat{b}\_{\xi}^{2}-\hat{b}\_{\xi,n}^{2}=\langle\gamma\_{\xi}^{\uparrow},\gamma\_{\xi}^{\uparrow}\rangle-\langle\gamma\_{\xi,n}^{\uparrow},\gamma\_{\xi,n}^{\uparrow}\rangle-(\hat{a}\_{\xi}^{2}-\hat{a}\_{\xi,n}^{2}). |  |

By Corollary 2.3 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12)), we have

|  |  |  |
| --- | --- | --- |
|  | |⟨γξ↑,γξ↑⟩−⟨γξ,n↑,γξ,n↑⟩|=|⟨γ,γξ↑⟩−⟨γ,γξ,n↑⟩|=|⟨γ,γξ↑−γξ,n↑⟩|⩽‖γ‖2​‖γn−γ‖2.\left|\langle\gamma\_{\xi}^{\uparrow},\gamma\_{\xi}^{\uparrow}\rangle-\langle\gamma\_{\xi,n}^{\uparrow},\gamma\_{\xi,n}^{\uparrow}\rangle\right|=|\langle\gamma,\gamma\_{\xi}^{\uparrow}\rangle-\langle\gamma,\gamma\_{\xi,n}^{\uparrow}\rangle|=|\langle\gamma,\gamma\_{\xi}^{\uparrow}-\gamma\_{\xi,n}^{\uparrow}\rangle|\leqslant\|\gamma\|\_{2}\|\gamma\_{n}-\gamma\|\_{2}. |  |

Moreover, direct computation shows

|  |  |  |
| --- | --- | --- |
|  | |a^ξ2−a^ξ,n2|⩽(‖γ‖2+‖γn‖2)​‖γn−γ‖2.|\hat{a}\_{\xi}^{2}-\hat{a}\_{\xi,n}^{2}|\leqslant(\|\gamma\|\_{2}+\|\gamma\_{n}\|\_{2})\|\gamma\_{n}-\gamma\|\_{2}. |  |

Hence, we have

|  |  |  |
| --- | --- | --- |
|  | |b^ξ−b^ξ,n|=|b^ξ2−b^ξ,n2|b^ξ+b^ξ,n⩽(2​‖γ‖2+‖γn‖2)​‖γn−γ‖2b^ξ.|\hat{b}\_{\xi}-\hat{b}\_{\xi,n}|=\frac{\left|\hat{b}\_{\xi}^{2}-\hat{b}\_{\xi,n}^{2}\right|}{\hat{b}\_{\xi}+\hat{b}\_{\xi,n}}\leqslant\frac{(2\|\gamma\|\_{2}+\|\gamma\_{n}\|\_{2})\|\gamma\_{n}-\gamma\|\_{2}}{\hat{b}\_{\xi}}. |  |

Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖hξ,n↑−hξ↑‖2\displaystyle\|h^{\uparrow}\_{\xi,n}-h^{\uparrow}\_{\xi}\|\_{2} | =σ​‖γξ,n↑−a^ξ,nb^ξ,n−γξ↑−a^ξb^ξ‖2⩽σ​‖γξ,n↑−γξ↑‖2+|a^ξ,n−a^ξ|b^ξ+σ​b^ξ,nb^ξ,n​b^ξ​|b^ξ,n−bn|\displaystyle=\sigma\left\|\frac{\gamma\_{\xi,n}^{\uparrow}-\hat{a}\_{\xi,n}}{\hat{b}\_{\xi,n}}-\frac{\gamma\_{\xi}^{\uparrow}-\hat{a}\_{\xi}}{\hat{b}\_{\xi}}\right\|\_{2}\leqslant\sigma\frac{\|\gamma^{\uparrow}\_{\xi,n}-\gamma^{\uparrow}\_{\xi}\|\_{2}+|\hat{a}\_{\xi,n}-\hat{a}\_{\xi}|}{\hat{b}\_{\xi}}+\sigma\frac{\hat{b}\_{\xi,n}}{\hat{b}\_{\xi,n}\hat{b}\_{\xi}}|\hat{b}\_{\xi,n}-b\_{n}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽(2+2​‖γ‖2+‖γn‖2b^ξ)​σb^ξ​‖γn−γ‖2,\displaystyle\leqslant\left(2+\frac{2\|\gamma\|\_{2}+\|\gamma\_{n}\|\_{2}}{\hat{b}\_{\xi}}\right)\frac{\sigma}{\hat{b}\_{\xi}}\|\gamma\_{n}-\gamma\|\_{2}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | |ρg​(hξ↑)−ρg​(hξ,n↑)|=σ​|b^ξ−b^ξ,n|⩽σ​(2​‖γ‖2+‖γn‖2)​‖γn−γ‖2b^ξ.\displaystyle|\rho\_{g}(h^{\uparrow}\_{\xi})-\rho\_{g}(h^{\uparrow}\_{\xi,n})|=\sigma|\hat{b}\_{\xi}-\hat{b}\_{\xi,n}|\leqslant\frac{\sigma(2\|\gamma\|\_{2}+\|\gamma\_{n}\|\_{2})\|\gamma\_{n}-\gamma\|\_{2}}{\hat{b}\_{\xi}}. |  |

This completes the proof. ∎

Proof of Example [1](https://arxiv.org/html/2511.08662v1#Thmexample1 "Example 1. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization") 
Note that (i) is trivial. Next, we consider (ii). If ξ=1/2\xi=1/2, then γξ↑\gamma^{\uparrow}\_{\xi} has the form of
(c1​(u−1/2)+a−1)​𝟙(0,1/2]​(u)+(c2​(u−1/2)+a−1)​𝟙(1/2,1)​(u)\left(c\_{1}(u-1/2)+a-1\right)\mathds{1}\_{(0,1/2]}(u)+\left(c\_{2}(u-1/2)+a-1\right)\mathds{1}\_{(1/2,1)}(u) with a∈[0,2]a\in[0,2] and c1⩾2​ac\_{1}\geqslant 2a and c2⩾2​(2−a)c\_{2}\geqslant 2(2-a). Direct computation shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01(γξ↑​(u)−γ​(u))2​du\displaystyle\int\_{0}^{1}(\gamma^{\uparrow}\_{\xi}(u)-\gamma(u))^{2}\mathrm{d}u | =c12​(∫0a/c1u2​du+∫01/2−a/c1u2​du)+c22​(∫0(2−a)/c2u2​du+∫01/2−(2−a)/c2u2​du)\displaystyle=c\_{1}^{2}\left(\int\_{0}^{a/c\_{1}}u^{2}\mathrm{d}u+\int\_{0}^{1/2-a/c\_{1}}u^{2}\mathrm{d}u\right)+c\_{2}^{2}\left(\int\_{0}^{(2-a)/c\_{2}}u^{2}\mathrm{d}u+\int\_{0}^{1/2-(2-a)/c\_{2}}u^{2}\mathrm{d}u\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =c123​((ac1)3+(12−ac1)3)+c223​((2−ac2)3+(12−2−ac2)3):=G​(c1,c2,a)\displaystyle=\frac{c\_{1}^{2}}{3}\left(\left(\frac{a}{c\_{1}}\right)^{3}+\left(\frac{1}{2}-\frac{a}{c\_{1}}\right)^{3}\right)+\frac{c\_{2}^{2}}{3}\left(\left(\frac{2-a}{c\_{2}}\right)^{3}+\left(\frac{1}{2}-\frac{2-a}{c\_{2}}\right)^{3}\right):=G(c\_{1},c\_{2},a) |  |

with the convention 00=0\frac{0}{0}=0.

Let f​(c):=c2​((ac)3+(b−ac)3)f(c):=c^{2}\left(\left(\frac{a}{c}\right)^{3}+\left(b-\frac{a}{c}\right)^{3}\right), with a>0,b>0a>0,b>0 and c⩾abc\geqslant\frac{a}{b}. Note that f​(c)a3=1+(ba​c−1)3c\frac{f(c)}{a^{3}}=\frac{1+\left(\frac{b}{a}c-1\right)^{3}}{c}. Then the solution of

|  |  |  |
| --- | --- | --- |
|  | ∂f​(c)/a3∂c=3​(ba​c−1)2​ba​c−1−(ba​c−1)3c2=(ba​c)2​(2​ba​c−3)c2=0\frac{\partial f(c)/a^{3}}{\partial c}=\frac{3\left(\frac{b}{a}c-1\right)^{2}\frac{b}{a}c-1-\left(\frac{b}{a}c-1\right)^{3}}{c^{2}}=\frac{\left(\frac{b}{a}c\right)^{2}(\frac{2b}{a}c-3)}{c^{2}}=0 |  |

is c=32​abc=\frac{3}{2}\frac{a}{b}, which is the unique minimizer of f​(c)f(c) over c⩾abc\geqslant\frac{a}{b}.

If aa is fixed, then the minimum of G​(c1,c2,a)G(c\_{1},c\_{2},a) is attained uniquely at c1=3​ac\_{1}=3a and c2=3​(2−a)c\_{2}=3(2-a). Then we have G​(3​a,3​(2−a),a)=18​(a2+(2−a)2)G(3a,3(2-a),a)=\frac{1}{8}(a^{2}+(2-a)^{2}). The minimum is attained at a=1a=1. Hence, we have γξ↑​(u)=3​(u−1/2),u∈(0,1)\gamma^{\uparrow}\_{\xi}(u)=3(u-1/2),~u\in(0,1).
∎

Proof of Lemma [3](https://arxiv.org/html/2511.08662v1#Thmlemma3 "Lemma 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"). Direct computation gives for G−1∈ℱU,ξ−1​(μ,σ)G^{-1}\in\mathcal{F}\_{U,\xi}^{-1}(\mu,\sigma),

|  |  |  |
| --- | --- | --- |
|  | dW2​(F−1,G−1)=(μ−μF)2+(σ−σF)2+2​σ​σF+2​μ​μF−2​⟨F−1,G−1⟩.\displaystyle d\_{W}^{2}(F^{-1},G^{-1})=(\mu-\mu\_{F})^{2}+(\sigma-\sigma\_{F})^{2}+2\sigma\sigma\_{F}+2\mu\mu\_{F}-2\langle F^{-1},G^{-1}\rangle. |  |

For G−1∈ℱU,ξ−1​(μF,σF↑)G^{-1}\in\mathcal{F}\_{U,\xi}^{-1}(\mu\_{F},\sigma\_{F}^{\uparrow}), by Theorem 2.2 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12)), we have

|  |  |  |
| --- | --- | --- |
|  | ⟨F−1−Fξ−1,↑,Fξ−1,↑−G−1⟩⩾0,\langle F^{-1}-F\_{\xi}^{-1,\uparrow},F\_{\xi}^{-1,\uparrow}-G^{-1}\rangle\geqslant 0, |  |

which implies

|  |  |  |
| --- | --- | --- |
|  | ⟨F−1,G−1⟩⩽⟨F−1,Fξ−1,↑⟩+⟨Fξ−1,↑,G−1⟩−⟨Fξ−1,↑,Fξ−1,↑⟩.\langle F^{-1},G^{-1}\rangle\leqslant\langle F^{-1},F\_{\xi}^{-1,\uparrow}\rangle+\langle F\_{\xi}^{-1,\uparrow},G^{-1}\rangle-\langle F\_{\xi}^{-1,\uparrow},F\_{\xi}^{-1,\uparrow}\rangle. |  |

It follows from Cauchy–Schwarz inequality that ⟨Fξ−1,↑,G−1⟩⩽⟨Fξ−1,↑,Fξ−1,↑⟩\langle F\_{\xi}^{-1,\uparrow},G^{-1}\rangle\leqslant\langle F\_{\xi}^{-1,\uparrow},F\_{\xi}^{-1,\uparrow}\rangle. Hence, for G−1∈ℱU,ξ−1​(μF,σF↑)G^{-1}\in\mathcal{F}\_{U,\xi}^{-1}(\mu\_{F},\sigma\_{F}^{\uparrow}), we have ⟨F−1,G−1⟩⩽⟨F−1,Fξ−1,↑⟩\langle F^{-1},G^{-1}\rangle\leqslant\langle F^{-1},F\_{\xi}^{-1,\uparrow}\rangle, which implies for G−1∈ℱU,ξ−1​(μ,σ)G^{-1}\in\mathcal{F}\_{U,\xi}^{-1}(\mu,\sigma),
⟨F−1,G−1⟩⩽⟨F−1,Fξ−1,↑−μFσF↑​σ+μ⟩\langle F^{-1},G^{-1}\rangle\leqslant\langle F^{-1},\frac{F\_{\xi}^{-1,\uparrow}-\mu\_{F}}{\sigma\_{F}^{\uparrow}}\sigma+\mu\rangle. Consequently, for G−1∈ℱU,ξ−1​(μ,σ)G^{-1}\in\mathcal{F}\_{U,\xi}^{-1}(\mu,\sigma),

|  |  |  |  |
| --- | --- | --- | --- |
|  | dW2​(F−1,G−1)\displaystyle d\_{W}^{2}(F^{-1},G^{-1}) | ⩾(μ−μF)2+(σ−σF)2+2​σ​σF+2​μ​μF−2​⟨F−1,Fξ−1,↑−μFσF↑​σ+μ⟩\displaystyle\geqslant(\mu-\mu\_{F})^{2}+(\sigma-\sigma\_{F})^{2}+2\sigma\sigma\_{F}+2\mu\mu\_{F}-2\langle F^{-1},\frac{F\_{\xi}^{-1,\uparrow}-\mu\_{F}}{\sigma\_{F}^{\uparrow}}\sigma+\mu\rangle |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(μ−μF)2+(σ−σF)2+2σσF(1−Corr(F−1(V),Fξ−1,↑(V)).\displaystyle=(\mu-\mu\_{F})^{2}+(\sigma-\sigma\_{F})^{2}+2\sigma\sigma\_{F}(1-Corr(F^{-1}(V),F\_{\xi}^{-1,\uparrow}(V)). |  | (27) |

Let c^0=C​o​r​r​(F−1​(V),Fξ−1,↑​(V))\hat{c}\_{0}=Corr(F^{-1}(V),F\_{\xi}^{-1,\uparrow}(V)).
We notice that, due to ([27](https://arxiv.org/html/2511.08662v1#A2.E27 "In Appendix B Proofs of results in Section 4 ‣ Robust distortion risk metrics and portfolio optimization")), if ε<(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c^0)\varepsilon<(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-\hat{c}\_{0}), then
ℱU,ξ−1​(μ,σ,ε)=∅\mathcal{F}\_{U,\xi}^{-1}(\mu,\sigma,\varepsilon)=\varnothing. If ε=(μF−μ)2+(σF−σ)2+2​σF​σ​(1−c^0)\varepsilon=(\mu\_{F}-\mu)^{2}+(\sigma\_{F}-\sigma)^{2}+2\sigma\_{F}\sigma(1-\hat{c}\_{0}), then ℱU,ξ−1​(μ,σ)={Fξ−1,↑−μFσF↑​σ+μ}\mathcal{F}\_{U,\xi}^{-1}(\mu,\sigma)=\left\{\frac{F\_{\xi}^{-1,\uparrow}-\mu\_{F}}{\sigma\_{F}^{\uparrow}}\sigma+\mu\right\}, which is a singleton. ∎

Proof of Lemma [4](https://arxiv.org/html/2511.08662v1#Thmlemma4 "Lemma 4. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"). In light of Theorem 2.3 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12)), we have ‖kλ2,ξ↑−kλ1,ξ↑‖22⩽|λ2−λ1|2​(μF2+σF2)\|k\_{\lambda\_{2},\xi}^{\uparrow}-k\_{\lambda\_{1},\xi}^{\uparrow}\|\_{2}^{2}\leqslant|\lambda\_{2}-\lambda\_{1}|^{2}(\mu\_{F}^{2}+\sigma\_{F}^{2}). This implies the continuity of C​o​r​r​(F−1​(V),kλ,ξ↑​(V))Corr(F^{-1}(V),k\_{\lambda,\xi}^{\uparrow}(V)) with respect to λ\lambda over [0,∞)[0,\infty). Note that

|  |  |  |
| --- | --- | --- |
|  | limλ→∞C​o​r​r​(F−1​(V),kλ,ξ↑​(V))=limλ↓0C​o​r​r​(F−1​(V),k^λ,ξ↑​(V)),\lim\_{\lambda\to\infty}Corr(F^{-1}(V),k\_{\lambda,\xi}^{\uparrow}(V))=\lim\_{\lambda\downarrow 0}Corr(F^{-1}(V),\hat{k}\_{\lambda,\xi}^{\uparrow}(V)), |  |

where k^λ,ξ=λ​γ+F−1\hat{k}\_{\lambda,\xi}=\lambda\gamma+F^{-1} and k^λ,ξ↑\hat{k}\_{\lambda,\xi}^{\uparrow} is the L2L\_{2}-projection of k^λ,ξ\hat{k}\_{\lambda,\xi} on ℱU,ξ−1\mathcal{F}\_{U,\xi}^{-1}. Note that k^0,ξ↑=Fξ−1,↑\hat{k}\_{0,\xi}^{\uparrow}=F\_{\xi}^{-1,\uparrow}. Applying Theorem 2.3 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12)) again, we have ‖k^λ,ξ↑−Fξ−1,↑‖22⩽λ2​‖γ‖22\|\hat{k}\_{\lambda,\xi}^{\uparrow}-F\_{\xi}^{-1,\uparrow}\|\_{2}^{2}\leqslant\lambda^{2}\|\gamma\|\_{2}^{2}. It follows that

|  |  |  |
| --- | --- | --- |
|  | limλ↓0C​o​r​r​(F−1​(V),k^λ,ξ↑​(V))=C​o​r​r​(F−1​(V),Fξ−1,↑​(V)).\lim\_{\lambda\downarrow 0}Corr(F^{-1}(V),\hat{k}\_{\lambda,\xi}^{\uparrow}(V))=Corr(F^{-1}(V),F\_{\xi}^{-1,\uparrow}(V)). |  |

We complete the proof. ∎

Proof of Theorem [3](https://arxiv.org/html/2511.08662v1#Thmtheorem3 "Theorem 3. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"). (i). In light of Lemma [4](https://arxiv.org/html/2511.08662v1#Thmlemma4 "Lemma 4. ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"), for any G−1∈FU,ξ−1​(μ,σ,ε)G^{-1}\in{F}^{-1}\_{U,\xi}(\mu,\sigma,\varepsilon), there exists hλ,ξ↑h\_{\lambda,\xi}^{\uparrow} with λ>0\lambda>0 such that
dW​(hλ,ξ↑,F−1)=dW​(G−1,F−1)d\_{W}(h\_{\lambda,\xi}^{\uparrow},F^{-1})=d\_{W}(G^{-1},F^{-1}). This implies ⟨F−1,hλ,ξ↑⟩=⟨F−1,G−1⟩\langle F^{-1},h\_{\lambda,\xi}^{\uparrow}\rangle=\langle F^{-1},G^{-1}\rangle. Applying Proposition [2](https://arxiv.org/html/2511.08662v1#Thmproposition2 "Proposition 2 (Bounds for unimodal distribution functions with a given inflection point). ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"), we have supG−1∈FU,ξ−1​(μ,σ)⟨γ+λ​F−1,G−1⟩=⟨γ+λ​F−1,hλ,ξ↑⟩\sup\_{G^{-1}\in{F}^{-1}\_{U,\xi}(\mu,\sigma)}\langle\gamma+\lambda F^{-1},G^{-1}\rangle=\langle\gamma+\lambda F^{-1},h\_{\lambda,\xi}^{\uparrow}\rangle and hλ,ξ↑h\_{\lambda,\xi}^{\uparrow} is the unique maximizer. Hence, we have ⟨γ+λ​F−1,hλ,ξ↑⟩>⟨γ+λ​F−1,G−1⟩\langle\gamma+\lambda F^{-1},h\_{\lambda,\xi}^{\uparrow}\rangle>\langle\gamma+\lambda F^{-1},G^{-1}\rangle if G−1≠hλ,ξ↑G^{-1}\neq h\_{\lambda,\xi}^{\uparrow}, which implies ρg​(hλ,ξ↑)>ρg​(G−1)\rho\_{g}(h\_{\lambda,\xi}^{\uparrow})>\rho\_{g}(G^{-1}) if G−1≠hλ,ξ↑G^{-1}\neq h\_{\lambda,\xi}^{\uparrow} and dW​(hλ,ξ↑,F−1)=dW​(G−1,F−1)d\_{W}(h\_{\lambda,\xi}^{\uparrow},F^{-1})=d\_{W}(G^{-1},F^{-1}).

For dW​(hλ1,ξ↑,F−1)<dW​(hλ2,ξ↑,F−1)d\_{W}(h\_{\lambda\_{1},\xi}^{\uparrow},F^{-1})<d\_{W}(h\_{\lambda\_{2},\xi}^{\uparrow},F^{-1}), we have ⟨F−1,hλ2,ξ↑⟩<⟨F−1,hλ1,ξ↑⟩\langle F^{-1},h\_{\lambda\_{2},\xi}^{\uparrow}\rangle<\langle F^{-1},h\_{\lambda\_{1},\xi}^{\uparrow}\rangle. In light of Proposition [2](https://arxiv.org/html/2511.08662v1#Thmproposition2 "Proposition 2 (Bounds for unimodal distribution functions with a given inflection point). ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"), it follows that supG−1∈FU,ξ−1​(μ,σ)⟨γ+λ2​F−1,G−1⟩=⟨γ+λ2​F−1,hλ2,ξ↑⟩\sup\_{G^{-1}\in{F}^{-1}\_{U,\xi}(\mu,\sigma)}\langle\gamma+\lambda\_{2}F^{-1},G^{-1}\rangle=\langle\gamma+\lambda\_{2}F^{-1},h\_{\lambda\_{2},\xi}^{\uparrow}\rangle, which implies ⟨γ+λ2​F−1,hλ2,ξ↑⟩⩾⟨γ+λ2​F−1,hλ1,ξ↑⟩\langle\gamma+\lambda\_{2}F^{-1},h\_{\lambda\_{2},\xi}^{\uparrow}\rangle\geqslant\langle\gamma+\lambda\_{2}F^{-1},h\_{\lambda\_{1},\xi}^{\uparrow}\rangle. Hence, we have ρg​(hλ2,ξ↑)>ρg​(hλ1,ξ↑)\rho\_{g}(h\_{\lambda\_{2},\xi}^{\uparrow})>\rho\_{g}(h\_{\lambda\_{1},\xi}^{\uparrow}). Consequently, the conclusion in (i) holds.

(ii) If γξ↑\gamma\_{\xi}^{\uparrow} is not a constant, then we have hξ↑∈FU,ξ−1​(μ,σ,ε)h^{\uparrow}\_{\xi}\in{F}^{-1}\_{U,\xi}(\mu,\sigma,\varepsilon). Applying Proposition [2](https://arxiv.org/html/2511.08662v1#Thmproposition2 "Proposition 2 (Bounds for unimodal distribution functions with a given inflection point). ‣ 4.1 Fixed inflection point ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"), we obtain the first conclusion in (ii). If γξ↑\gamma\_{\xi}^{\uparrow} is a constant, by Corollary 2.3 of Brunk ([1965](https://arxiv.org/html/2511.08662v1#bib.bib12)), it follows that ⟨γ,k⟩⩽⟨γξ↑,k⟩\langle\gamma,k\rangle\leqslant\langle\gamma\_{\xi}^{\uparrow},k\rangle for all k∈ℱU,ξ−1k\in\mathcal{F}\_{U,\xi}^{-1}. By taking k=±1k=\pm 1, we have γξ↑=g​(1)\gamma\_{\xi}^{\uparrow}=g(1). Consequently,

|  |  |  |
| --- | --- | --- |
|  | supG−1∈ℱU,ξ−1​(μ,σ)ρg​(G−1)⩽supG−1∈ℱU,ξ−1​(μ,σ)⟨γξ↑,G−1⟩⩽g​(1)​μ.\sup\_{G^{-1}\in\mathcal{F}^{-1}\_{U,\xi}(\mu,\sigma)}\rho\_{g}(G^{-1})\leqslant\sup\_{G^{-1}\in\mathcal{F}^{-1}\_{U,\xi}(\mu,\sigma)}\langle\gamma\_{\xi}^{\uparrow},G^{-1}\rangle\leqslant g(1)\mu. |  |

Let GnG\_{n} be the distribution of μ+σ​3​n​V​[−1/n,1/n]\mu+\sigma\sqrt{3}nV[-1/n,1/n] for n⩾1n\geqslant 1, where V​[−1/n,1/n]V[-1/n,1/n] follows uniform distribution on [−1/n,1/n][-1/n,1/n]. Then Gn−1∈ℱU,ξ−1​(μ,σ)G\_{n}^{-1}\in\mathcal{F}^{-1}\_{U,\xi}(\mu,\sigma) and limn→∞Gn−1​(t)=μ\lim\_{n\to\infty}G\_{n}^{-1}(t)=\mu for all t∈(0,1)t\in(0,1). Hence,
ρg​(Gn−1)→g​(1)​μ\rho\_{g}(G\_{n}^{-1})\to g(1)\mu as n→∞n\to\infty. Consequently, supG−1∈ℱU,ξ−1​(μ,σ)ρg​(G−1)=g​(1)​μ\sup\_{G^{-1}\in\mathcal{F}^{-1}\_{U,\xi}(\mu,\sigma)}\rho\_{g}(G^{-1})=g(1)\mu. This completes the proof. ∎

Proof of Lemma [5](https://arxiv.org/html/2511.08662v1#Thmlemma5 "Lemma 5. ‣ 4.2 Unknown inflection points ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization"). Clearly, there exists a sequence of hn∈ℱU,[ξ1,ξ2]−1,n⩾1h\_{n}\in\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]},~n\geqslant 1 such that limn→∞‖γ−hn‖2=infh∈ℱU,[ξ1,ξ2]−1‖γ−h‖2\lim\_{n\to\infty}\|\gamma-h\_{n}\|\_{2}=\inf\_{h\in\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]}}\|\gamma-h\|\_{2}. For any u∈(0,1)u\in(0,1), we have {hn​(u),n⩾1}\{h\_{n}(u),n\geqslant 1\} is a bounded sequence. Hence, there is a subsequence {hnm​(u),m⩾1}\{h\_{n\_{m}}(u),m\geqslant 1\} such that limm→∞hnm​(u)\lim\_{m\to\infty}h\_{n\_{m}}(u) exists. This implies that we could find a subsequence also denoted by {hnm​(u),m⩾1}\{h\_{n\_{m}}(u),m\geqslant 1\} such that limm→∞hnm​(u)\lim\_{m\to\infty}h\_{n\_{m}}(u) exists for any u∈(0,1)∩ℚu\in(0,1)\cap\mathbb{Q}, where ℚ\mathbb{Q} is the set of all rational numbers. Define h∗​(u)=limm→∞hnm​(u)h^{\*}(u)=\lim\_{m\to\infty}h\_{n\_{m}}(u) for all u∈(0,1)∩ℚu\in(0,1)\cap\mathbb{Q}. Note that h∗​(u)h^{\*}(u) is increasing on (0,1)∩ℚ(0,1)\cap\mathbb{Q}. Define γξ1,ξ2↑​(u)=infu′∈(u,1)∩ℚh∗​(u′)\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u)=\inf\_{u^{\prime}\in(u,1)\cap\mathbb{Q}}h^{\*}(u^{\prime}) for u∈(0,1)u\in(0,1). Then γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} is increasing and right-continuous on (0,1)(0,1).

Next, we show that γξ1,ξ2↑∈ℱU,[ξ1,ξ2]−1\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}\in\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]}. For u∈(0,1)u\in(0,1), if γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} is continuous at uu, then by definition, we have γξ1,ξ2↑​(u)=infu′∈(u,1)∩ℚh∗​(u′)=supu′∈(0,u)∩ℚh∗​(u′)\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u)=\inf\_{u^{\prime}\in(u,1)\cap\mathbb{Q}}h^{\*}(u^{\prime})=\sup\_{u^{\prime}\in(0,u)\cap\mathbb{Q}}h^{\*}(u^{\prime}). Hence, there exist sequences ul↑uu\_{l}\uparrow u and ul′↓uu\_{l}^{\prime}\downarrow u with ul,ul′∈(0,1)∩ℚu\_{l},u\_{l}^{\prime}\in(0,1)\cap\mathbb{Q} such that γξ1,ξ2↑​(u)=liml→∞h∗​(ul)=liml→∞h∗​(ul′)\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u)=\lim\_{l\to\infty}h^{\*}(u\_{l})=\lim\_{l\to\infty}h^{\*}(u\_{l}^{\prime}). It follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |hnm​(u)−γξ1,ξ2↑​(u)|\displaystyle|h\_{n\_{m}}(u)-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u)| | ⩽|hnm​(u)−hnm​(ul)|+|hnm​(ul)−h∗​(ul)|+|h∗​(ul)−γξ1,ξ2↑​(u)|\displaystyle\leqslant|h\_{n\_{m}}(u)-h\_{n\_{m}}(u\_{l})|+|h\_{n\_{m}}(u\_{l})-h^{\*}(u\_{l})|+|h^{\*}(u\_{l})-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u)| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽|hnm​(ul′)−hnm​(ul)|+|hnm​(ul)−h∗​(ul)|+|h∗​(ul)−γξ1,ξ2↑​(u)|\displaystyle\leqslant|h\_{n\_{m}}(u\_{l}^{\prime})-h\_{n\_{m}}(u\_{l})|+|h\_{n\_{m}}(u\_{l})-h^{\*}(u\_{l})|+|h^{\*}(u\_{l})-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u)| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|h∗​(ul′)−h∗​(ul)|+|h∗​(ul)−γξ1,ξ2↑​(u)|​as​m→∞,\displaystyle=|h^{\*}(u\_{l}^{\prime})-h^{\*}(u\_{l})|+|h^{\*}(u\_{l})-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u)|~\text{as}~m\to\infty, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =0​as​l→∞.\displaystyle=0~\text{as}~l\to\infty. |  |

Hence, limm→∞hnm​(u)=γξ1,ξ2↑​(u)\lim\_{m\to\infty}h\_{n\_{m}}(u)=\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u) for all u∈Cu\in C, where CC is the collection of all continuous points of γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}.
The inflection point of hnmh\_{n\_{m}} is denoted by ξm\xi\_{m}. As {ξm,m⩾3}\{\xi\_{m},~m\geqslant 3\} is bounded, there exists a subsequence such that the limit exists. Without loss of generality, we suppose limm→∞ξm=ξ∈[ξ1,ξ2]\lim\_{m\to\infty}\xi\_{m}=\xi\in[\xi\_{1},\xi\_{2}]. Let us first focus on (ξ,1)(\xi,1). For ui∈(ξ,1),i=1,2,3,4u\_{i}\in(\xi,1),~i=1,2,3,4 with u1<u2⩽u3<u4u\_{1}<u\_{2}\leqslant u\_{3}<u\_{4}, there exist ui,l∈(ξ,1)∩Cu\_{i,l}\in(\xi,1)\cap C satisfying u1,l<u2,l⩽u3,l<u4,lu\_{1,l}<u\_{2,l}\leqslant u\_{3,l}<u\_{4,l} and ui,l↓uiu\_{i,l}\downarrow u\_{i} as l→∞l\to\infty. Note that hnmh\_{n\_{m}} is convex over (ξm,1)(\xi\_{m},1) and ξm<u1\xi\_{m}<u\_{1} for all m⩾m0m\geqslant m\_{0}. Hence, we have hnm​(u2,l)−hnm​(u1,l)u2,l−u1,l⩽hnm​(u4,l)−hnm​(u3,l)u4,l−u3,l\frac{h\_{n\_{m}}(u\_{2,l})-h\_{n\_{m}}(u\_{1,l})}{u\_{2,l}-u\_{1,l}}\leqslant\frac{h\_{n\_{m}}(u\_{4,l})-h\_{n\_{m}}(u\_{3,l})}{u\_{4,l}-u\_{3,l}} for all m⩾m0m\geqslant m\_{0}. Letting m→∞m\to\infty, it follows that γξ1,ξ2↑​(u2,l)−γξ1,ξ2↑​(u1,l)u2,l−u1,l⩽γξ1,ξ2↑​(u4,l)−γξ1,ξ2↑​(u3,l)u4,l−u3,l\frac{\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u\_{2,l})-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u\_{1,l})}{u\_{2,l}-u\_{1,l}}\leqslant\frac{\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u\_{4,l})-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u\_{3,l})}{u\_{4,l}-u\_{3,l}}. The letting l→∞l\to\infty and using the fact that γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} is right-continuous, we have γξ1,ξ2↑​(u2)−γξ1,ξ2↑​(u1)u2−u1⩽γξ1,ξ2↑​(u4)−γξ1,ξ2↑​(u3)u4−u3\frac{\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u\_{2})-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u\_{1})}{u\_{2}-u\_{1}}\leqslant\frac{\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u\_{4})-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u\_{3})}{u\_{4}-u\_{3}}, which implies γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} is convex over (ξ,1)(\xi,1). Hence, γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} is also continuous over (ξ,1)(\xi,1). We can similarly show that γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} is continuous and concave over (0,ξ)(0,\xi).

If ξ=ξ1=0\xi=\xi\_{1}=0 or ξ=ξ2=1\xi=\xi\_{2}=1, then clearly, γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} is continuous over (0,1)(0,1). Next, we consider the case ξ∈(0,1)\xi\in(0,1). For any u1,u2∈(0,1)u\_{1},u\_{2}\in(0,1) satisfying ξ2<u1<ξ<u2<ξ+12\frac{\xi}{2}<u\_{1}<\xi<u\_{2}<\frac{\xi+1}{2}, using the fact that hnm∈ℱU,ξ−1h\_{n\_{m}}\in\mathcal{F}^{-1}\_{U,\xi}, we have

|  |  |  |
| --- | --- | --- |
|  | hnm​(u2)−hnm​(u1)\displaystyle h\_{n\_{m}}(u\_{2})-h\_{n\_{m}}(u\_{1}) |  |
|  |  |  |
| --- | --- | --- |
|  | ⩽max⁡{4​(hnm​(ξ/2)−hnm​(ξ/4))ξ,4​(hnm​((3+ξ)/4)−hnm​((1+ξ)/2))1−ξ}​(u2−u1).\displaystyle\leqslant\max\left\{\frac{4(h\_{n\_{m}}(\xi/2)-h\_{n\_{m}}(\xi/4))}{\xi},\frac{4(h\_{n\_{m}}((3+\xi)/4)-h\_{n\_{m}}((1+\xi)/2))}{1-\xi}\right\}(u\_{2}-u\_{1}). |  |

For the above inequality, letting m→∞m\to\infty, we have

|  |  |  |
| --- | --- | --- |
|  | γξ1,ξ2↑​(u2)−γξ1,ξ2↑​(u1)\displaystyle\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u\_{2})-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u\_{1}) |  |
|  |  |  |
| --- | --- | --- |
|  | ⩽max⁡{4​(γξ1,ξ2↑​(ξ/2)−γξ1,ξ2↑​(ξ/4))ξ,4​(γξ1,ξ2↑​((3+ξ)/4)−γξ1,ξ2↑​((1+ξ)/2))1−ξ}​(u2−u1).\displaystyle\leqslant\max\left\{\frac{4(\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(\xi/2)-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(\xi/4))}{\xi},\frac{4(\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}((3+\xi)/4)-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}((1+\xi)/2))}{1-\xi}\right\}(u\_{2}-u\_{1}). |  |

Letting u2↓ξu\_{2}\downarrow\xi and u1↑ξu\_{1}\uparrow\xi, we have γξ1,ξ2↑​(ξ+)−γξ1,ξ2↑​(ξ−)=0.\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(\xi+)-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(\xi-)=0. Hence, γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} is continuous at ξ\xi. Combing the above conclusions, we obtain the continuity of γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} over (0,1)(0,1).

Note that the continuity of γξ1,ξ2↑\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow} over (0,1)(0,1) implies limm→∞hnm​(u)=γξ1,ξ2↑​(u)\lim\_{m\to\infty}h\_{n\_{m}}(u)=\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}(u) for all u∈(0,1)u\in(0,1).
It follows from Fatou’s lemma that

|  |  |  |
| --- | --- | --- |
|  | ‖γ−γξ1,ξ2↑‖2⩽lim infn→∞‖γ−hnm‖2=infh∈ℱU,[ξ1,ξ2]−1‖γ−h‖2<∞.\|\gamma-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}\|\_{2}\leqslant\liminf\_{n\to\infty}\|\gamma-h\_{n\_{m}}\|\_{2}=\inf\_{h\in\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]}}\|\gamma-h\|\_{2}<\infty. |  |

Hence, ‖γξ1,ξ2↑‖2⩽‖γ−γξ1,ξ2↑‖2+‖γ‖2<∞\|\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}\|\_{2}\leqslant\|\gamma-\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}\|\_{2}+\|\gamma\|\_{2}<\infty. Consequently, we have γξ1,ξ2↑∈ℱU,[ξ1,ξ2]−1\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}\in\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]} and γξ1,ξ2↑∈arg⁡minh∈ℱU,[ξ1,ξ2]−1⁡‖γ−h‖2\gamma\_{\xi\_{1},\xi\_{2}}^{\uparrow}\in\arg\min\_{h\in\mathcal{F}^{-1}\_{U,[\xi\_{1},\xi\_{2}]}}\|\gamma-h\|\_{2}. ∎

Proof of Proposition [5](https://arxiv.org/html/2511.08662v1#Thmproposition5 "Proposition 5 (Bounds for distortion risk measures for unimodal distribution functions). ‣ 4.2 Unknown inflection points ‣ 4 Bounds for Unimodal Distribution Functions with Wassertein constraint ‣ Robust distortion risk metrics and portfolio optimization").
The proof is exactly the same as that of Proposition [1](https://arxiv.org/html/2511.08662v1#Thmproposition1 "Proposition 1. ‣ 3 Bounds for distortion risk metrics under Wasserstein distance constraints ‣ Robust distortion risk metrics and portfolio optimization"). The details are omitted. ∎

Proof of Proposition [6](https://arxiv.org/html/2511.08662v1#Thmproposition6 "Proposition 6. ‣ 5.1 Mean-variance and Wasserstein distance constraints ‣ 5 Robust portfolio optimization ‣ Robust distortion risk metrics and portfolio optimization"). In light of Popescu ([2007](https://arxiv.org/html/2511.08662v1#bib.bib31)), we have

|  |  |  |
| --- | --- | --- |
|  | {F∑i=1nwi​Xi:𝔼​(Xi)=μi,C​o​v​(𝐗)=Σ0}=ℳ∞​(𝐰⊤​𝝁,𝐰⊤​Σ0​𝐰).\left\{F\_{\sum\_{i=1}^{n}w\_{i}X\_{i}}:\mathbb{E}(X\_{i})=\mu\_{i},Cov(\mathbf{X})=\Sigma\_{0}\right\}=\mathcal{M}\_{\infty}\left(\mathbf{w}^{\top}\boldsymbol{\mu},\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\right). |  |

Moreover, it follows from Theorem 5 of Mao et al. ([2025](https://arxiv.org/html/2511.08662v1#bib.bib27)) that

|  |  |  |
| --- | --- | --- |
|  | {F∑i=1nwi​Xi:dWn,2​(F𝐗,F𝐗0)⩽ε}={G:dW​(F𝐰⊤​𝐗0,G)⩽ε​‖𝐰‖22}.\left\{F\_{\sum\_{i=1}^{n}w\_{i}X\_{i}}:d\_{W}^{n,2}(F\_{\mathbf{X}},F\_{\mathbf{X}\_{0}})\leqslant\sqrt{\varepsilon}\right\}=\{G:d\_{W}(F\_{\mathbf{w}^{\top}\mathbf{X}\_{0}},G)\leqslant\sqrt{\varepsilon\|\mathbf{w}\|\_{2}^{2}}\}. |  |

Combining the above results, we obtain

|  |  |  |
| --- | --- | --- |
|  | ℳ𝐰,ε=ℳε​‖𝐰‖22​(𝐰⊤​𝝁,𝐰⊤​Σ0​𝐰).\mathcal{M}\_{\mathbf{w},\varepsilon}=\mathcal{M}\_{\varepsilon\|\mathbf{w}\|\_{2}^{2}}\left(\mathbf{w}^{\top}\boldsymbol{\mu},\sqrt{\mathbf{w}^{\top}\Sigma\_{0}\mathbf{w}}\right). |  |

∎